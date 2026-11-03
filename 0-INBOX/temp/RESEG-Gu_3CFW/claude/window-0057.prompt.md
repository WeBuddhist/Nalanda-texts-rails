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
[Block 1996]
འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས།

[Block 1997]
བཙུན་པ། ཇི་ཙམ་གྱིས་རང་བཞིན་དུ་གནས་པ་མ་ལགས་པར་འགྱུར། ཉེ་བ༌[^1755]འཁོར་ཇི་ཙམ་གྱིས་ལྷག་པར་སྤྱད་པ་མ་ཡིན་པ་ལྷག་པར་སྤྱོད་ཅིང་དགེ་སློང་གི༌[^1756]བསླབ་པ་ལ་མི་བསླབ་པ་སྟེ། ཉེ་བ༌[^1757]འཁོར་དེ་ཙམ་གྱིས་རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1998]
འདིས་ནི་གང་ཡང་རུང་བས་འཁྲུལ་པར་གྱུར་ཅིང་དགེ་སློང་གི་རང་བཞིན་ལས་ཉམས་པར་འགྱུར་བ་ཉིད་ཅེས་བྱ་བའོ། །

[Block 1999]
དེ་ཉིད་ཀྱིས༌[^1758]རང་བཞིན་དུ་གནས་པ༌[^1759]ཡིན་པ་དེ་བསྟན་ཏོ། །

[Block 2000]
རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པ་དེ་ཉིད་ཀྱིས་ནི་ཕྱིར་ཟློག་པར་འོས་པ་ཉིད་མ་ཡིན་པར་གསུངས་ཏེ། དེ་ལྟར་ཡང་འདིར་གཞུང་ནི། བཙུན་པ། གང་ཟག་དུ་དག་གིས༌[^1760]སླར་བཟློག་པ་མི་ཆགས། ཉེ་བ༌[^1761]འཁོར་བཅུ་གཉིས་ཏེ། བྱིས་པ་དང་རྨོངས་པ་མི་གསལ་བ་དང་། མི་མཁས་པ་དང་ངོ་ཚ་མེད་པ་དང་། ནད་དང་བཅས་པ་དང་། མཚམས་ཀྱི་ཕྱི་རོལ་ན་གནས་པ་དང་། གནས་ནས་ཕྱུང་བ་དང་ཚིག་ཡང་དག་པར་མ་བསྡམས་པ༌[^1762]དང་། སྤྱོད་ལམ་ལས་ཉམས་པ་དང་། རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པ་དང་། བསླབ་པ་བྱིན་པས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2001]
འདིར་དགེ་སློང་ཉམས་པ་ལ་རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པ་དེའི་དོན་ཏོ། །

[Block 2002]
སུ་ཞིག་འཁྲུལ་པ་མ་ཡིན་པ་ལ་ནི་དགེ་སློང་གི་རང་བཞིན་དུ་གྱུར་པ་ཉིད་མ་ཡིན་ནོ། །གང་གིས༌[^1763]འཁྲུལ་པ་དང་བཅས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བསྡམས་པར་བྱས་པས་ཀྱང་ཡིན་གྱི་བཤགས་པར་བྱ་བ་འབའ་ཞིག་གིས་ཡིན་པར་མ་ཟད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ།

[Block 2003]
འདིར་གཞུང་ནི་དགག་དབྱེའི་གཞི་ལས།

[Block 2004]
གལ་ཏེ་དེས་བསྡམ་པར༌[^1764]བྱ་བ་རྣམས་ཞེ༌[^1765]ན་བསྡམ་པར༌[^1766]བྱ་སྟེ། དགག་དབྱེ་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེང་དང་པོར་བྱ་སྟེ། དེ་ཉིད་ཀྱི་མཐར༌[^1767]གཞུང་ནི་རང་བཞིན་བྱེད་པ་དང་། རྣམ་པ་དུ་མས་ཞེས༌[^1768]གསུངས་པ་ཡིན་ནོ། །

[Block 2005]
རང་བཞིན་དུ་གནས་ཏེ་སེམས་པ་ལ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་འདི་ལ་གཞན་ཕམ་པ༌[^1769]བྱེད་པ་རྣམས་བསྟན་པའི་ཕྱིར་འཁྲུལ་པ་དང་བཅས་པ་ཞེས་བྱའོ། །

[Block 2006]
འདིར་འཁྲུལ་པ་ཡོ་བྱད་འདི་བྱེད་བཞིན་ལ་འཁྲུལ་པ་མ༌[^1770]ཡིན་པ་ལྟར་བལྟ་བར་བྱ་བ་ཉིད་ཅེས་བྱ་བ་དེ་ལ་བརྗོད་པར་བྱ་སྟེ། བྱིན་གྱིས་བརླབས་པས་དག་པ་ཉིད་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་ལྷག་མ་དང་སྤང་བའི་ལྟུང་བྱེད་ནི་བྱིན་གྱིས་བརླབས་ཏེ་འདུག་པར་བྱའོ། །

[Block 2007]
ལྷག་མ་བསྡམ་པར༌[^1771]བྱ་བ་ལེན་པར་བྱེད་ན་བྱིན་གྱིས་བརླབས་པ་བསྐོ་བ་འདི་ལ་ཁ་སྐོང་བ་མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བ་དེ་མཐུན་པ་ཉིད་དོ། །

[Block 2008]
ནུས་པ་ཉིད་ཡིན་ན་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་འཆགས་ནུས་པ་ཉིད་ཡིན་ན། བྱིན་གྱིས་བརླབས་པས་དག་པ་ཉིད་དུ་མི་འགྱུར་བའོ། །

[Block 2009]
གང་གི་ཕྱིར་འདི་སྐད་བསྟན་ཏེ། གལ་ཏེ་ཕམ་པར་འགྱུར་བ་དག་ཤེས་ན༌[^1772]བསྙིལ་ཏེ༌[^1773]དགག་དབྱེ་བྱའོ། །

[Block 2010]
གལ་ཏེ་དགེ་འདུན་ལྷག་མ་དག་ཤེས་ན་བྱིན་གྱིས་བརླབས་ཏེ་དགག་དབྱེ་བྱའོ། །

[Block 2011]
གལ་ཏེ་སྤོང་བ༌[^1774]ཤེས་ན་བྱིན་གྱིས་བརླབས་ཏེ་དགག་དབྱེ་བྱའོ། །

[Block 2012]
གལ་ཏེ་ལྟུང་བྱེད་དེ༌[^1775]དག་ཤེས་ན་བཤགས་ཏེ་དགག་དབྱེ་བྱའོ། །

[Block 2013]
གལ་ཏེ་སོ་སོར་བཤགས་པར་བྱ་བ་དག་ཤེས་ན་སོ་སོར་བཤགས་ཏེ་དགག་དབྱེ་བྱའོ། །

[Block 2014]
གལ་ཏེ་བཤགས་པར་བྱ་བའི་ཉེས་བྱས་དག་ཤེས་ན་བཤགས་ཏེ་དགག་དབྱེ་བྱའོ། །

[Block 2015]
གལ་ཏེ་བསྡམ་པར༌[^1776]བྱ་བའི་ཉེས་བྱས་དག་ཤེས་ན་བསྡམས་ཏེ་དགག་དབྱེ་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2016]
གང་ཞིག་སྐབས་འདིར་ལྷུང་བཟེད༌[^1777]ལ་སོགས་པ་རྣམས་ཀྱི་ཚིག་འདིས་བྱས་པར་འགྱུར་བར་ནུས་པ་ཉིད་ཡིན་ན་བྱིན་གྱིས་བརླབས་པས་དག་པ་འགྲུབ་པ་ཉིད་དུ་མི༌[^1778]འགྱུར་རོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 2017]
ཡང་ནུས་པ་ཉིད་གང་ཞེ་ན། དེའི་ཕྱིར། དེའི་ཚེ་ལེན་པ་ཡོད་ན་ལྟུང་བྱེད་འབའ་ཞིག་ཏུ་གྱུར་པ་དང་། སོ་སོར་བཤགས་པར་བྱ་བ་དང་ཕྱིར་བཅོས་པར་བྱ་བའི་ཉེས་བྱས་ནི་ནུས་པ་ཉིད་ཡིན་ཏེ་བཤགས་པ་ཙམ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཚེ་ལེན་པ་ཡོད་ན་ཞེས་བྱ་བ་ནི་ཉི་མ་དེ་ཉིད་ལ་ལས་བྱེད་པ་དེའི་ཚེ་ཕྱིར་བཅོས་པར་ནུས་པ་ཉིད་དོ། །

[Block 2018]
གང་དག་བཤགས་པ་ལ་ལེན་པ་གང་གི་ཕྱིར་དེ་རྣམས་ལ་དེའི་མདུན་དུ་བཤགས་པ༌[^1779]ཙམ་གྱིས་ཕྱིར་བཅོས་པ་དག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2019]
ལྟུང་བ་ཆུང༌[^1780]བ་ལ་ནི་འདུ་ཤེས་ཇི་ལྟ་བ་བཞིན་དུ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ལྷག་མ་དང་བཅས་པར་འདུ་ཤེས་པ་རྣམས་ཀྱིས་ནི་བྱིན་གྱིས་བརླབ་ཏུ་གཞུག་པའམ། ཕྱིར་བཅོས་པ་བྱེད་དུ་བཅུག་ནས་དེ་དང་ལྷན་ཅིག་ལས་བྱའོ། །

[Block 2020]
ལྷག་མ་མེད་པར་འདུ་ཤེས་པ་རྣམས་ཀྱིས༌[^1781]ནི་དེ་མེད་པར་ལས་བྱའོ། །

[Block 2021]
གཅིག་ལ་དེ་ལྟར་བསྙིལ་བ་དང་། མི་བསྙིལ་བ་དང་ཕྱིར་བཅོས་པ་རྣམ་པ་དུ་མ་ནི་རིགས་པ་ཁོ་ནའོ་ཞེས་བྱ་བ་ནི། ལྷག་མ་མེད་པར་འདུ་ཤེས་པ་རྣམས་ཀྱིས་ནི་དེ་བསྙིལ་བར་བྱའོ། །

[Block 2022]
ལྷག་མ་དང་བཅས་པར་འདུ་ཤེས་པ་རྣམས་ཀྱིས་ནི་བསྡུ་བར་བྱའོ། །

[Block 2023]
བཤགས་པར་བྱ་བ༌[^1782]འདུ་ཤེས་པ་རྣམས་ཀྱིས་ནི། བཤགས་པའི་བདག་ཉིད་ཀྱི་ཕྱིར་བཅོས་པར་བྱེད་དུ་གཞུག་གོ། །

[Block 2024]
བསྡམ་པར༌[^1783]བྱ་བར་འདུ་ཤེས་པ་རྣམས་ཀྱིས་ནི་བསྡམས་པའི་བདག་ཉིད་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་གཅིག་ལ་མི་རིགས་པར་འགྱུར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2025]
དེ་དག་ནི་བྱེད་པ་པོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་མ༌[^1784]རྫོགས་པ་ལ་སོགས་པ་རྣམས་ལས་ཀྱི་བྱེད་པ་པོ་མ་ཡིན་ནོ། །

[Block 2026]
འདིར་གཞུང་ནི་གླེང་གཞི་དག་ལས།

[Block 2027]
བཙུན་པ། བསླབ་པ་བརྩལ༌[^1785]བས་ལས་དག་བགྱིས་ན་བགྱིས་ཞེས་བརྗོད་པར་བགྱིའམ་འོན་ཏེ་མ༌[^1786]བགྱིས་ཞེས༌[^1787]བརྗོད་པར་བགྱི། ཉེ་བ༌[^1788]འཁོར་མ་བྱས་ཞེས་བརྗོད་པར་བྱ་སྟེ། ཡང་བྱ་བ་དག་ཡིན་ནོ། །

[Block 2028]
བཙུན་པ་ཟ་མ་དང་མ་ནིང་དང་དགེ་སློང་མ་སུན་ཕྱུང་བ་དང་། མ་བཀུམ་པ་དང་ཕ་བཀུམ་པ་དང་དགྲ་བཅོམ་པ་བཀུམ་པ་དང་། དགེ་འདུན་གྱི་དབྱེན་བགྱིས་པ་དང་། དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བ་དང་། མུ་སྟེགས་ཅན་དང་མུ་སྟེགས་ཅན་ཞུགས་པ་དང་། རྐུ་ཐབས་སུ་གནས་པ་དང་ཐ་དད་པར་གནས་པ་དང་གནས་པར་མི་བགྱི་བས་ལས་དག་བགྱིས་ན་བགྱིས་ཞེས༌[^1789]བགྱིའམ། འོན་ཏེ་མ་བགྱིས་ཞེས་བརྗོད་པར་བགྱི།[^1790] ཉེ་བ༌[^1791]འཁོར་མ་བྱས་ཞེས་བརྗོད་པར་བྱ་བ༌[^1792]སྟེ། ཡང་བྱ་བ་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2029]
གང་ཚོགས་ཀྱི་ཁ་སྐོང་བར་མི་འོས་པ་དེ་དང་། དེས་ལས་བྱ་བས་ཐག་རིང་དུ་སྤང་བ༌[^1793]ཁོ་ན་ཡིན་ཏེ། ལས་བྱེད་པ་ནི་ཚོགས་ཀྱིས༌[^1794]ཁ་སྐོང་བ་གཞན་དག་པས་ཆེས་གཅེས་པ་ཡིན་པའི་ཕྱིར་དང་དགེ་འདུན་གྱི་གཙོ་བོར་གྱུར་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2030]
དགེ་འདུན་གྱི་སྒོར་གྱུར་པ་ཉིད་ཀྱིས་ལས་ཀྱི་ཡན་ལག་གཞན་ལས་ལས་ཀྱི་ཡན་ལག༌[^1795]འདི་ལ་གླེང་གཞི་ལས་གསུངས་པའི་བསླབ་པ་བརྩལ་བ༌[^1796]ལ་སོགས་པ་རྣམས་ལ་གཞན་རྣམས་ནི་ལྷག་མའོ། །

[Block 2031]
འདིར་དེ་རྣམས་ལ་ལས་བྱེད་པ་པོ་ཉིད་བཀག་པ་ལ་ཡོངས་སུ་བསྡུ་བའོ། །

[Block 2032]
ལྷག་མ་དང་བཅས་པའི་ཕྱིར་བཅོས་པ་ལ་ཞུགས་པ༌[^1797]ནི་འདོན་པར་བྱེད་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྔར་དེ་དག་ནི༌[^1798]བྱེད་པ་པོ་ཉིད་མ་ཡིན་ནོ་ཞེས་སྨོས་པ་དེའི་དམིགས་ཀྱིས་བསལ་བ་ཡིན་ཏེ། དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་ཕྱིར་འཆོས་པ་ལ་ཞུགས་པ་སྤོ་བ་ལ་སོགས་པ་དང་། དབྱུང་བ་ལ་སོགས་པས་གསོ་བར༌[^1799]ཞུགས་པའི་གང་ཟག་གིས་ནི་སོ་སོར་ཐར་པའི་མདོ་འདོན་དུ་རུང་བ་ཉིད་ཡིན་པའོ། །

[Block 2033]
བསྐོ་བ་པོ་གཞན་ཡོད་ན་ཉེས་བྱས་ཙམ་གྱི་མི་འཆགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2034]
དེ་ལས་གཞན༌[^1800]དེ་དག་གིས༌[^1801]ནི་ཐོས་པ་དང་བཅས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་གཞན་ཞེས་བྱ་བ་ནི་ལྷག་མ་དང་བཅས་པ༌[^1802]ཕྱིར་འཆོས་པ་ལ་ཞུགས་པས་སོ། །

[Block 2035]
གཞན་པ་དེ་དག་གིས་ནི་ཞེས་བྱ་བ་ནི་བསྙེན་པར་མ་རྫོགས་པ་ལ་སོགས་པ་རྣམས་ཀྱིས་སོ། །
--- END BLOCKS ---
