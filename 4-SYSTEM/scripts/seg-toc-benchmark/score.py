#!/usr/bin/env python3
"""
Score a segmented + TOC-ingested commentary against the human-processed gold file.

    python3 score.py <gold.md> <pred.md> [--json out.json] [--label NAME] [--tol 2]

Everything is measured in the squeezed content stream (see bench_lib), so layout,
whitespace, transclusions and block IDs never affect the alignment.

SEGMENTATION
  blocks            gold vs predicted block counts, median/p90 syllables
  boundary P/R/F1   exact, and within ±tol squeezed chars
  block exact       share of gold blocks reproduced exactly (same start and end)
  verse whole       share of gold stanza blocks reproduced exactly

TOC (editorial headings — ids I-, II-, a-, b- — are scored separately)
  heading P/R/F1    by title (normalised: ordinal prefix, tshegs, shads removed;
                    match = SequenceMatcher ratio >= 0.8), one-to-one in doc order
  placement exact   matched headings inserted at exactly the gold offset
  placement ±30     … within 30 squeezed chars
  id exact          predicted ^block-id equals gold (tree path)
  level exact       markdown heading level equals gold
  parent ok         predicted parent maps to the gold parent

BODY IDS
  body id exact     among exactly-reproduced gold blocks, same ^id

INTEGRITY
  text identical    squeezed predicted content == squeezed gold content
"""
from __future__ import annotations

import argparse
import json
import statistics as st
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from bench_lib import parse, norm_title  # noqa: E402


def prf(tp, n_pred, n_gold):
    p = tp / n_pred if n_pred else 0.0
    r = tp / n_gold if n_gold else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    return p, r, f


def boundary_scores(gold: set, pred: set, tol: int):
    exact = len(gold & pred)
    # tolerant one-to-one matching
    used = set()
    tp = 0
    for g in sorted(gold):
        cands = [p for p in pred if abs(p - g) <= tol and p not in used]
        if cands:
            used.add(min(cands, key=lambda p: abs(p - g)))
            tp += 1
    return prf(exact, len(pred), len(gold)), prf(tp, len(pred), len(gold))


def parent_of(headings, i):
    lv = headings[i].level
    for j in range(i - 1, -1, -1):
        if headings[j].level < lv:
            return j
    return None


def match_headings(gh, ph):
    """One-to-one, document-order-respecting greedy match by normalised title."""
    pairs = {}
    used = set()
    last_p = -1
    for gi, g in enumerate(gh):
        gn = norm_title(g.title)
        best, best_r = None, 0.0
        for pi, p in enumerate(ph):
            if pi in used:
                continue
            r = SequenceMatcher(None, gn, norm_title(p.title)).ratio()
            # prefer candidates after the previous match (document order)
            bonus = 0.001 if pi > last_p else 0.0
            if r + bonus > best_r:
                best, best_r = pi, r + bonus
        if best is not None and best_r >= 0.8:
            pairs[gi] = best
            used.add(best)
            last_p = best
    return pairs


def score(gold_path, pred_path, tol=2):
    g = parse(Path(gold_path).read_text(encoding='utf-8'))
    p = parse(Path(pred_path).read_text(encoding='utf-8'))
    res = {'gold': str(gold_path), 'pred': str(pred_path)}
    res['text_identical'] = g.stream == p.stream
    if not res['text_identical']:
        # report the first divergence
        i = next((k for k, (a, b) in enumerate(zip(g.stream, p.stream)) if a != b),
                 min(len(g.stream), len(p.stream)))
        res['first_divergence'] = {'offset': i, 'gold': g.stream[i:i + 40],
                                   'pred': p.stream[i:i + 40]}

    # segmentation
    gb, pb = g.boundaries, p.boundaries
    (ep, er, ef), (tp_, tr, tf) = boundary_scores(gb, pb, tol)
    gset = {(b.start, b.end) for b in g.blocks}
    pset = {(b.start, b.end) for b in p.blocks}
    gverse = [(b.start, b.end) for b in g.blocks if b.is_verse]
    res['seg'] = {
        'gold_blocks': len(g.blocks), 'pred_blocks': len(p.blocks),
        'gold_median_syl': st.median([b.syl for b in g.blocks]),
        'pred_median_syl': st.median([b.syl for b in p.blocks]) if p.blocks else 0,
        'gold_p90_syl': sorted(b.syl for b in g.blocks)[int(.9 * len(g.blocks))],
        'pred_p90_syl': sorted(b.syl for b in p.blocks)[int(.9 * len(p.blocks))] if p.blocks else 0,
        'boundary_exact': {'P': ep, 'R': er, 'F1': ef},
        f'boundary_tol{tol}': {'P': tp_, 'R': tr, 'F1': tf},
        'block_exact_rate': len(gset & pset) / len(gset),
        'verse_whole_rate': (sum(1 for v in gverse if v in pset) / len(gverse)) if gverse else None,
        'gold_verse_blocks': len(gverse),
    }

    # spacing fidelity: whitespace inside blocks, ignoring block boundaries
    gw, pw = g.inner_ws(), p.inner_ws()
    bset = g.boundaries | p.boundaries
    gw, pw = gw - bset, pw - bset
    res['spacing'] = {
        'jaccard': (len(gw & pw) / len(gw | pw)) if (gw | pw) else 1.0,
        'missing': len(gw - pw), 'extra': len(pw - gw),
        'shad_space_shad_gold': sum(b.text.count('། །') for b in g.blocks),
        'shad_space_shad_pred': sum(b.text.count('། །') for b in p.blocks),
    }

    # TOC
    def split(hs):
        return [h for h in hs if not h.editorial], [h for h in hs if h.editorial]
    g_sb, g_ed = split(g.headings)
    p_all = p.headings
    pairs = match_headings(g_sb, p_all)
    # predicted headings that compete for gold sa bcad titles: every non-editorial one,
    # plus any editorial one that a gold numbered heading was matched to (a gold file may
    # number a section the pipeline treats as frame, e.g. Drakpa's `3 མཛད་བྱང།`)
    n_pred_sb = len([h for h in p_all if not h.editorial]) + \
        sum(1 for pi in pairs.values() if p_all[pi].editorial)
    P, R, F = prf(len(pairs), n_pred_sb, len(g_sb))
    place_exact = sum(1 for gi, pi in pairs.items() if g_sb[gi].offset == p_all[pi].offset)
    place_30 = sum(1 for gi, pi in pairs.items() if abs(g_sb[gi].offset - p_all[pi].offset) <= 30)
    id_exact = sum(1 for gi, pi in pairs.items() if g_sb[gi].block_id == p_all[pi].block_id)
    lvl_exact = sum(1 for gi, pi in pairs.items() if g_sb[gi].level == p_all[pi].level)
    # parent agreement (within sa bcad lists)
    g_index = {id(h): i for i, h in enumerate(g_sb)}
    par_ok = 0
    for gi, pi in pairs.items():
        gpar = parent_of(g_sb, gi)
        ppar = parent_of(p_all, pi)
        if gpar is None and (ppar is None or p_all[ppar].editorial):
            par_ok += 1
        elif gpar is not None and pairs.get(gpar) == ppar:
            par_ok += 1
    n = len(pairs) or 1
    misses = [{'gold_id': g_sb[i].block_id, 'title': g_sb[i].title}
              for i in range(len(g_sb)) if i not in pairs]
    extras_idx = set(range(len(p_all))) - set(pairs.values())
    extras = [{'pred_id': p_all[i].block_id, 'title': p_all[i].title}
              for i in sorted(extras_idx) if not p_all[i].editorial]
    displaced = [{'gold_id': g_sb[gi].block_id, 'pred_id': p_all[pi].block_id,
                  'title': g_sb[gi].title, 'delta_chars': p_all[pi].offset - g_sb[gi].offset}
                 for gi, pi in pairs.items() if g_sb[gi].offset != p_all[pi].offset]
    title_exact = sum(1 for gi, pi in pairs.items()
                      if g_sb[gi].title.replace('*', '').strip() == p_all[pi].title.replace('*', '').strip())
    # editorial headings: recall by title, and placement
    ed_pairs = match_headings(g_ed, [h for h in p_all])
    ed_place = sum(1 for gi, pi in ed_pairs.items() if g_ed[gi].offset == p_all[pi].offset)
    ed_id = sum(1 for gi, pi in ed_pairs.items() if g_ed[gi].block_id == p_all[pi].block_id)
    res['toc'] = {
        'gold_sabcad_headings': len(g_sb), 'pred_headings': n_pred_sb,
        'heading_title': {'P': P, 'R': R, 'F1': F},
        'placement_exact_rate': place_exact / n, 'placement_within30_rate': place_30 / n,
        'id_exact_rate': id_exact / n, 'level_exact_rate': lvl_exact / n,
        'parent_ok_rate': par_ok / n,
        'title_exact_rate': title_exact / n,
        'gold_editorial_headings': len(g_ed),
        'editorial_recall': (len(ed_pairs) / len(g_ed)) if g_ed else None,
        'editorial_placement_exact': (ed_place / len(g_ed)) if g_ed else None,
        'editorial_id_exact': (ed_id / len(g_ed)) if g_ed else None,
        'missed': misses, 'extra': extras, 'displaced': displaced,
    }

    # body IDs
    pmap = {(b.start, b.end): b.block_id for b in p.blocks}
    same = [(b.block_id, pmap[(b.start, b.end)]) for b in g.blocks
            if (b.start, b.end) in pmap and b is not g.title_block]
    res['body_ids'] = {
        'pred_blocks_with_id': sum(1 for b in p.blocks if b.block_id),
        'id_exact_on_exact_blocks': (sum(1 for a, b in same if a == b) / len(same)) if same else 0.0,
    }

    # composite (unweighted mean of the headline numbers)
    comp = [ef, F, res['toc']['placement_exact_rate'] * R, res['toc']['id_exact_rate'] * R]
    res['composite'] = sum(comp) / len(comp)
    return res


def fmt(res, label):
    s, t, b = res['seg'], res['toc'], res['body_ids']
    lines = [
        f'### {label}',
        f"- text identical to gold: **{res['text_identical']}**",
        f"- blocks: gold {s['gold_blocks']} / pred {s['pred_blocks']}; median syl gold {s['gold_median_syl']} / pred {s['pred_median_syl']}",
        f"- boundary exact P/R/F1: {s['boundary_exact']['P']:.2f} / {s['boundary_exact']['R']:.2f} / **{s['boundary_exact']['F1']:.2f}**",
        f"- block exact-match: {s['block_exact_rate']:.2f}; stanzas whole: {s['verse_whole_rate']}",
        f"- headings (sa bcad) gold {t['gold_sabcad_headings']} / pred {t['pred_headings']}; title P/R/F1 {t['heading_title']['P']:.2f} / {t['heading_title']['R']:.2f} / **{t['heading_title']['F1']:.2f}**",
        f"- placement exact {t['placement_exact_rate']:.2f}, ±30 {t['placement_within30_rate']:.2f}; id exact {t['id_exact_rate']:.2f}; level exact {t['level_exact_rate']:.2f}; parent ok {t['parent_ok_rate']:.2f}",
        f"- heading title exact (incl. ordinal + final shad): {t['title_exact_rate']:.2f}",
        f"- editorial headings: recall {t['editorial_recall']}, placed exactly {t['editorial_placement_exact']}, id exact {t['editorial_id_exact']}",
        f"- spacing inside blocks (Jaccard vs gold): {res['spacing']['jaccard']:.3f}; '། །' gold {res['spacing']['shad_space_shad_gold']} / pred {res['spacing']['shad_space_shad_pred']}",
        f"- body ids: {b['pred_blocks_with_id']} stamped; exact on exact blocks {b['id_exact_on_exact_blocks']:.2f}",
        f"- **composite {res['composite']:.3f}**",
    ]
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('gold')
    ap.add_argument('pred')
    ap.add_argument('--json')
    ap.add_argument('--label', default='prediction')
    ap.add_argument('--tol', type=int, default=2)
    a = ap.parse_args()
    res = score(a.gold, a.pred, a.tol)
    if a.json:
        Path(a.json).write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding='utf-8')
    print(fmt(res, a.label))


if __name__ == '__main__':
    main()
