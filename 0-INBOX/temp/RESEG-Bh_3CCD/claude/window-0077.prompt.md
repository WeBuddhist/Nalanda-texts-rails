=== SYSTEM PROMPT ===
You are an expert in classical Tibetan Buddhist commentary (འགྲེལ་པ་) structure.

You are given a numbered list of blocks from a Tibetan verse commentary. A
rule-based segmenter has already cut them; most cuts are right. Your job is to
output the few merge/split operations that bring the blocks to the layout the
human editors of this vault use.

━━━ TARGET LAYOUT — one block per FUNCTIONAL UNIT ━━━

OPENER       A node's division announcement together with the first-child opener
             that follows it is ONE block:
               "<topic> ལ་གསུམ། A། B། C་འོ། །དང་པོ་ནི།"
             A sibling opener "གཉིས་པ་ <title> ནི།" is its own block.
ROOT QUOTE   A quoted root stanza is its own block. These blocks are tagged
             [VERSE]; they are protected — never include them in any operation.
EXPLANATION  The gloss that follows a quote ("ཞེས་པ་སྟེ། …", "ཞེས་པ་ནི། …", or a
             running explanation) is ONE block up to the next opener, quote or
             heading — even when it is long (100–250 syllables) and contains several
             sentence ends, a question and answer ("…ལོ། །གང་ལ་ན། …"), a side remark
             on a variant reading ("…ཞེས་འགྱུར་བཅོས་…"), a cross-reference
             ("འདི་དང་འོག་གི་ས་བཅད་…"), or a mantra cited in passing.
SECOND LEVEL A passage that re-reads the same stanza on another level — opening
             "སྦས་དོན་ནི།", "ངེས་དོན་ནི།", "ངེས་པའི་དོན་དུ།", "ཟབ་དོན་ནི།",
             "དེའི་ནང་གི་དོན་ལ།", "མཐར་ཐུག་གི་དོན་ནི།" or the like after the literal
             gloss — is its OWN block, never merged into the literal gloss before it
             (the editors keep the two readings apart). Within that passage, M1 applies.
FRAME        The namo line alone; each of the author's own verses one block;
             "སྨྲས་པ།" alone; the colophon ("ཅེས་ … སྦྱར་བའོ། །" + closing wishes) one block.

━━━ MERGE — adjacent blocks that are one unit ━━━

M1  CONTINUED EXPLANATION
    A block that goes on explaining the same quote/topic as the block before it —
    no new opener, no new quote, no new verse being treated — belongs to that block.
    This is the most common fix. Do NOT keep a cut just because a sentence ends.
    Exception: a SECOND LEVEL opener (see above) always starts a new block.
M2  INCOMPLETE SENTENCE
    A block ending in a connector (དང་། / ཞིང་། / ཅིང་། / ནས། / སྟེ། / ཏེ།) that
    the next block completes.
M3  OPENER CHAIN
    An enumeration block followed by "དང་པོ་ནི།" / "དང་པོ་ལ་ N།" (and further
    nested first-child enumerations) — merge them into one opener block.
M4  COLOPHON
    The parts of the closing colophon and its final wishes form one block.

━━━ SPLIT — one block that holds two units ━━━

S1  A new node opener (ordinal + title + "ནི།" or "ལ་ N།") buried mid-block:
    split before it.
S2  The treatment of a new verse/topic starts mid-block (e.g. "ཡང་ཕྱག་གང་ལ་འཚལ་ན"
    starting the next homage): split before it.
S3  An introductory opener "… ནི།" fused to the explanation of the PREVIOUS
    quote: split so the opener starts the next unit.

Never split a block only because it is long.

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

━━━ HEADING / VERSE BLOCKS — always KEEP ━━━

Blocks tagged [HEADING] or [VERSE] are NEVER part of any operation.

━━━ OUTPUT FORMAT ━━━

A JSON array of operations. Blocks not mentioned are kept as-is.

[
  {"op": "merge", "blocks": [N, M]},
  {"op": "merge", "blocks": [N, M, P]},
  {"op": "split", "block": N, "after": "<verbatim unique substring ending at split point>"},
  {"op": "split", "block": N, "after": ["<sub1>", "<sub2>", "<sub3>"]}
]

Rules for the output:
- Block numbers are CONTINUOUS and INCLUDE heading and verse blocks. You may only
  merge blocks with consecutive numbers (N and N+1). Never merge across a heading
  or a verse block, and never propose a merge whose numbers skip over one.
- Each block number appears in AT MOST ONE operation.
- For each "after" substring: copy a verbatim slice from the block that ends exactly
  at the split point and is UNIQUE within that block (10–20 characters is usually enough).
- If nothing needs to change in this window, output: []
- Output ONLY the JSON array. No explanation, no commentary, no code fences.

=== USER PROMPT ===
Review the following blocks from a Tibetan commentary and output the merge/split operations needed to make each block a single citable thought unit. Block numbers are global (file-level).

--- BEGIN BLOCKS ---
[Block 2696]
[^1770]

[Block 2697]
དེ་ནས་སྟོན་པ་ཞེས་པ་ནས་དགོངས་པ་མ་ཡིན་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་སྤྲོས་པ་འདི་དག་ཐམས་ཅད་རང་བཞིན་མེད་པར་བསྟན་པས་སོ། །

[Block 2698]
དགོན་པ་ཞེས་པ་ནས་དྲང་བའི་དོན༌[^1771]ངེས་པའི་དོན་དུ་བཤད་པ་ཞེས༌[^1772]བྱ་བའི་བར་དུ༌[^1773]དྲང་བའི་དོན་གྱི་ཕྱོགས་སུ་རྣམ་པར་དབེན་པའི་གནས་ཀྱི་ཁྱད་པར་རབ་ཏུ་བསྟན་པས་སོ། །

[Block 2699]
ངེས་པའི་དོན་ལ་ཡང་ཆོས་ཀྱི་སྐུ་ལ་སོགས་པའི་ཉེ་བར་དམིགས་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2700]
ལུས་དང་ཞེས་པ་ནས་དགོངས་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་ལྕགས་གསུམ་ལ་སོགས་པའི་སྒྲའི་སྒོ་ནས་ཡེ་ཤེས་གསུམ་རྣམ་པར་དག་པའི་མཚན་ཉིད་འོད་གསལ་བའི་དེ་ཁོ་ཉིད་བསྟན་པས་སོ། །

[Block 2701]
འཁོར་ལོ་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པས་བཤད་ཅེས་བྱ་བའི་བར་དུ་ནི་འཁོར་ལོ་དང་། རྡོ་རྗེ་དང་། པདྨ་དང་། རིན་པོ་ཆེ་དང་། རལ་གྲིའི་རིག་པ་འཛིན་པའི་དངོས་གྲུབ་དང་། རི་ལུ༌[^1774]དང་མིག་སྨན་གྱི་དངོས་གྲུབ་དང་། རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་དེ་བཞིན་གཤེགས་པའི་སྐུ་བསྐྱེད་པ་དང་། བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པའི་བསྙེན་པ་ལ་སོགས་པ་བཞི་པོ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2702]
རྟོག་པའི༌[^1775]སྒྲས་ཤེས་པར་བྱ་ཞེས་དགོངས་སོ། །

[Block 2703]
བསྙེན་པའི་ཡེ་ཤེས་ཞེས་པ་ནས་དགོངས་པས་བཤད་ཅེས་པའི་བར་དུ་ནི་འགལ་བའི་སྒྲས་བརྗོད་པའི་རྫོགས་པའི་རིམ་པའི་མཚན་ཉིད་ཅན་རྣལ་འབྱོར་གྱི་ཡན་ལག་དྲུག་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2704]
དགོན་པ་ཆེན་པོ་ཞེས་པ་ནས་དྲང་བ༌[^1776]དང་ངེས་པའི་དོན་དུ༌[^1777]བཤད་ཅེས་བྱ་བའི་བར་དུ་ནི་དྲང་བའི་དོན་གྱི༌[^1778]ཕྱོགས་སུ་ནི་ཕྱིའི་གནས་ཙམ་སོ་སོར་བསྟན་པས་སོ། །

[Block 2705]
ངེས་པའི་དོན་གྱི་ཕྱོགས་སུ་ནི་ཡེ་ཤེས་ལྔའི་ཉེ་བར་དམིགས་པའི་གཞི་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2706]
དུས་བཞི་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པས་བཤད་ཅེས་བྱ་བའི་བར་དུ་ནི་དམན་པ་ལ་སོགས་པ་དབྱེ་བས་དུས་ཀྱི༌[^1779]དབྱེ་བ་གང་གིས་དངོས་གྲུབ་བསྟན་པའི་ཕྱིར་དེ་ཡང་སོགས་པའི་སྒྲས་ཤེས་པར་བྱའོ། །

[Block 2707]
གསང་བ་ཞེས་པ་ནས་དགོངས་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་ཟླ་བ་ཕྱེད་ལ་སོགས་པའི་འགལ་བའི་སྒྲས་དེ་ཁོ་ན་ཉིད་ཐོབ་པར་རབ་ཏུ་བསྟན་པས་སོ། །

[Block 2708]
དེ་ལ་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་རྣལ་འབྱོར་ཆེན་པོའི་ཡན་ལག་ཏུ་གྱུར་པ་སྐུ་རྡོ་རྗེ་ལ་སོགས་པ་གསུམ༌[^1780]ལ་གསོལ་བ༌[^1781]གདབ་པ་ཙམ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2709]
སོགས་པའི་སྒྲས་ཡིན་ཞེས་དགོངས་སོ། །

[Block 2710]
ལེའུ་བཅུ་གཉིས་པའི་ཞེས་པས་ནི་ཉེ་བར་སྡུད་པ་བསྟན་ཏོ། །

[Block 2711]
[^1782]

[Block 2712]
དེ་ནས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས། སྒྲ་ཇི་བཞིན་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་དང་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་ཁྲོ་བོ་རྣམས་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་གསོལ་པ་གདབ་པར་གྱུར་པས་སོ། །

[Block 2713]
ཨེ་མའོ་ཞེས་པ་ནས་དགོངས་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་སངས་རྒྱས་ལ་སོགས་པ་ཞེས་འགལ་བའི་སྒྲས་རྣལ་འབྱོར་ཡན་ལག་དྲུག་ལ་སོགས་པའི་དེ་ཁོ་ན་ཉིད་བསྟན་པས་སོ། །

[Block 2714]
མ་སྐྱེས་ཞེས་པ་ནས་དགོངས་པ་མ་ཡིན་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་རང་བཞིན་གྱིས་རྣམ་པར་དག་པའི་ངོ་བོ་ཉིད་མེད་པའི་ཕྱོགས་སུ་ཡང་བསྟན་པ་དང་བསྟན་བྱའི་སྒོ་ནས་ཡེ་ཤེས་སྐྱེ་བ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2715]
ཡིད་འོང་ཞེས་པ་ནས་དགོངས་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་འགལ་བའི་སྒྲས་རྡོ་རྗེ་བཟླས་པ༌[^1783]བཅུ་གཅིག་སོ་སོར་བསྟན་པས་སོ། །

[Block 2716]
འདོད་ཆགས་ཞེས་པ་ནས། སྒྲ་ཇི་བཞིན་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་འདོད་ཆགས་ལ་སོགས་པའི་སྒྲས༌[^1784]རིགས་ཅན་རྣལ་འབྱོར་པ་རྣམས་ལ་རྡོ་རྗེ་བཟླས་པའི་ཕན་ཡོན་བསྟན་པས་སོ། །

[Block 2717]
གཏི་མུག་ཅེས་པ་ནས་དྲང་བའི་དོན་དང་ངེས་པའི་དོན་དུ་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་དྲང་བའི་དོན་གྱི་ཕྱོགས་སུ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་ལྷ་རྣམས་ཀྱི་རང་རང་གི་ས་བོན་ལས་བསྐྱེད་པ་བསྟན་པས་སོ། །

[Block 2718]
ངེས་པའི་དོན་གྱི་ཕྱོགས་སུ་ནི་རང་བཞིན་དང་སྣང་བའི་རིམ་པས་འོད་གསལ་བ་ལ་འཇུག་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2719]
ཡེ་ཤེས་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པས་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་དེ་བཞིན་གཤེགས་པ་ལྔའི་སྐུའི་སྒོ་ནས་ཞི་བ་ལ་སོགས་པའི་ལས་ཀྱི་རབ་འབྱམས་ལྔ་བསྟན་པས་སོ། །

[Block 2720 [VERSE]]
རྟོག་པའི་སྒྲས་ཤེས་པར་བྱའོ། །
ནམ་མཁའ་རྡོ་རྗེ་ཞེས་པ་ནས། །

[Block 2721]
དགོངས་པས་བཤད་ཅེས་བྱ་བའི་བར་དུ་ནི་འགལ་བའི་སྒྲའི་སྦྱོར་བས་ལུས་དང་ངག་དང་ཡིད་ཉེ་བར་སྡུད༌[^1785]པས་འོད་གསལ་བར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2722]
རྣམ་པ་ཞེས་པ་ནས། སྒྲ་ཇི་བཞིན་བཤད་ཅེས་པའི་བར་དུ་ནི་ཆུ་རེངས་པ་བསྟན་པས་སོ། །

[Block 2723]
རྟོག་པའི༌[^1786]སྒྲས་ཤེས་པར་བྱ་ཞེས་དགོངས་སོ། །

[Block 2724]
རྐང་པ་ཞེས་པ་ནས། དགོངས་པས༌[^1787]བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་འགལ་བའི་སྒྲའི༌[^1788]སྒོ་ནས་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་ངོ་བོ་རྡོ་རྗེའི་སྐུ་བསྟན་པས་སོ། །

[Block 2725]
དབང་ཆེན་ཞེས་པ་ནས་སྒྲ་ཇི་བཞིན་པས༌[^1789]བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་ངག༌[^1790]རེངས་པ་དང་དཔུང་རེངས་པ་དང་གདུག་པ་ཅན༌[^1791]ཕུར་བུས་གདབ་པ་དང་གྲོང་དང་གྲོང་ཁྱེར་ལ་སོགས་པ་དག་ཏུ་ཞི་བ་ལ་སོགས་པ་སྒྲུབ་པ་དང་། གཤིན་རྗེ་གཤེད་ལ་སོགས་པའི་ཁྲོ་བོའི་འཁོར་ལོ་བསྐྱེད་པའི་རིམ་པ་བསྟན་པས་སོ། །

[Block 2726]
རྟོག་པའི་སྒྲ་དང་སོགས་པའི་སྒྲས་ཤེས་པར་བྱའོ། །

[Block 2727]
འགོག་པ་ཞེས་པ་ནས་དྲང་བའི་དོན་དང་ངེས་པའི་དོན་དུ་བཤད་པ་ཞེས་བྱ་བའི་བར་དུ་ནི་དྲང་བའི་དོན་གྱི༌[^1792]ཕྱོགས་སུ་ནི་སྲུང་བའི༌[^1793]འཁོར་ལོའི༌[^1794]དབུས་ཀྱི་བདག་པོའི་ཏིང་ངེ་འཛིན་བསྲུང་བས་སོ། །

[Block 2728]
ངེས་པའི་དོན་གྱི་ཕྱོགས་སུ་ནི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་སོ་སོར་བསྟན་པས་སོ། །

[Block 2729]
ལེའུ་བཅུ་གསུམ་པའི་ཞེས་པས་ཉེ་བར་སྡུད༌[^1795]པའོ། །

[Block 2730]
[^1796]

[Block 2731]
ལེའུ་བཅུ་བཞི་པ་ལ་སོགས་པ་ཞེས་བྱ་བ་ལ། ཕྲེང་བའི་སྔགས་རྣམས་ནི་ལས་ཀྱི་རབ་འབྱམས་སྒྲུབ་པར་བྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2732]
ལས་ཀྱི་རབ་འབྱམས་ནི་ཞི་བ་ལ་སོགས་པའོ། །

[Block 2733]
སྒྲ་ཇི་བཞིན་པ་ནི་སོགས་པའི་སྒྲ་དང་རྟོག་པའི་སྒྲ་བརྗོད་པས་སོ། །

[Block 2734]
བར་བར་ན་ཞེས་པ་ནི་སྐབས་སྐབས་སུའོ། །

[Block 2735]
ལ་ལ་ནི་ཞེས་པ་ལ་རིམ་པ་མེད་པར་གནས་པའོ། །
--- END BLOCKS ---
