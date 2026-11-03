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
[Block 1751]
འདིར་གཞུང་ནི། ཇི་ལྟར་ཡང་བཙོ་བླག་མཁན་གྱིས་གོས་རྣམས་བཏིང་བ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1752]
བདག་ཏུ་བྱས་པ་ཉིད་ལ་ཡང་གཞན་གྱིས་མ་བྲལ་བ་ཉིད་ཀྱི་བསམ་པར༌[^1220]བདག་པོ་ཉིད་དུ་མ་བཏང་བ་དག་ཏུ་བྱས་པ་རྗེས་སུ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 1753]
དེ་དང་མ་བྲལ་བ་ཉིད་དང༌[^1221]བདག་ལ༌[^1222]བྱས་པ་ལ་དེ་བསལ་བ་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 1754]
དེ་ལྟར་ན་རྒྱལ་པོའི་ཕོ་བྲང་དུ་རྐུན་པོ་རྣམས་གཏད་ཅིང་བཟློག་པ་ལ་རྐུ་བ་ཉིད་བསྐྱེད་པ་མི་སྲིད་པའོ། །

[Block 1755]
ཕྱེད༌[^1223]རིན་རྣམ་པར་སྦྱོར་བ༌[^1224]གང་ཞིག་དངོས་པོ་དེ་ལས་བདག་གིས༌[^1225]བྱེད་པ་སོ་སོར་མ་ལོག་པ་འདི་ནི་འདིར་བསམ་པས་མ་བཏང་བར་ཤེས་པར་བྱའོ། །

[Block 1756]
ཐ་སྙད་མི་ཤེས་པའི་ནི་ཞལ་ཏ་བྱེད་པ་བདག་པོ་ཉིད༌[^1226]ཡིན་ནོ་ཞེས་བྱ་བ་ལ་ཐ་སྙད་ཤེས་པ་ནི་འཇིག་རྟེན་གྱི་ཐ་སྙད་སྨྲ་ནུས་པ་སྟེ། དེའི་རྒྱུད་དུ་གཏོགས་པའི་རྫས་ནི་ཐ་སྙད་ཤེས་པའོ།[^1227] །ཐ་སྙད་མི་ཤེས་པའི་ནི་ཐ་སྙད་ཤེས་པ་མ་ཡིན་པ༌[^1228]སྟེ། དཔེར་ན་བྱ་རྣམས་ཀྱི་རྒྱན་བཞིན་ནོ། །

[Block 1757]
དེ་ལ་ཐ་སྙད་མི་ཤེས་པའི་རྒྱུད་དུ་གཏོགས་པ་ཡོད་ཀྱང་དེའི་ཞལ་ཏ་བྱེད་པ་ང་ཡིར༌[^1229]འཛིན་པར་བྱས་པ་གང་ཡིན་པ་དེ་བདག་པོ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1758]
འདིར་བདག་པོ་མེད་པ་དང་འདྲ་སྟེ་དེ་བས་ན་ཞལ་ཏ་བྱེད་པ་པོའི་འདིར་ངར་འཛིན་པ་དངོས་པོ་ཅན་ལ་ཡང་དག་པར་གནས་པ་སྟེ་འདིར་བདག་ཏུ་བྱས་པ་ནི་བྱ་དེ་རྣམས་ཀྱི་བྱའི་རྒྱན་བཞིན་དུ་དེ་བས་ན་བྱ་རྣམས་ལ་ཡང་འདིར་བདག་པོ་ཉིད་དོ། །

[Block 1759]
གཉིས་ཀ་བདག་པོ་ཉིད་ཡིན་ན་ནི་འདུ་ཤེས་ཀྱི་དབང་གིས་ལྟུང་བ་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་རིག་པར་བྱའོ། །

[Block 1760]
དེ་ལྟར་འདིར་གཞུང་ནི། གལ་ཏེ་དེ་འདི་སྙམ་དུ་མི་ལས་བརྐུ་བར་བྱའི་བྱ་རྣམས་ལས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དང་། མི་ལས་རིན་ཐང་བརྩི་བར་བྱ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 1761]
མིའི་བདག་པོ་ཉིད་མེད་པར་ཕམ་པར་སྦྱོར་བ་མ་ཡིན་ནོ། །

[Block 1762]
བཟའ་བཏུང་གི་ཕྱིར་བྱིན་པ་ལ་ནི་བསམ་པ་དང་འབྲེལ་པ་མེད་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དགོན་པའི་ལམ་དུ་ཆུའི་སྐལ་བ་དུད་འགྲོ་རྣམས་ལ་སྦྱིན་པ་ལ་གང་གི་ཕྱིར་འདུ་ཤེས་ཀྱིས་རྣམ་པར་གཞག་པ་མ་བྱས་པ་དེ་རྒྱུར་བརྗོད་པ་ཡིན་ནོ། །

[Block 1763]
གང་གི་ཕྱིར་བཟའ་བཏུང་གི་དོན་དུ་དུད་འགྲོ་ཁྱུ༌[^1230]ལ་སོགས་པ་དེ་ལ་ནི་ཆུ་ལ་སོགས་པ་གང་ཞིག་སྟེར་བའི༌[^1231]སྦྱིན་པར་བྱེད་པ་འདི༌[^1232]བདག་གིའོ་སྙམ་པའི་བསམ་པས་འབྲེལ་པ་གང་ཡིན་པ་དང་ལྟོས་པ་གང་ཡིན་པ་དེ་མེད་པ་ཉིད་ནི་དངོས་པོ་མེད་པའོ། །

[Block 1764]
དེ་བས་ན་དུད་འགྲོ་རྣམས་ཁོ་ན་བདག་པོ་ཉིད་ཅེས་བྱའོ། །

[Block 1765]
འདིར་གཞུང༌[^1233]ནི། གནས་སྐབས་དེ་ལ་དུད་འགྲོ་རྣམས་ཀྱི་སྐལ་བའི་ཆུའི་རིན་ཐང་དེ་རྣམས་ཀྱིས་བརྩི་བར་བྱ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་ལས་མ་བྱིན་པར་ལེན་པ་བསྐྱེད་དོ། །

[Block 1766]
ནགས་མེས་བཏང་བ་ལ་སོགས་དག་གིས་གཟུང་བའི་ཕྱིར་རི་དགས་དང་བྱ་དང་སྡིག་སྦྲུལ་ལིངས་བཏབ་པ་རྣམས་ལ་ནི་ལིངས་པ་མ་ཡིན་པ་བདག་པོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། རྔོན་པ༌[^1234]ལ་སོགས་པ་རྣམས་ཀྱིས༌[^1235]རི་དགས་ལ་སོགས་པ་རྣམས་ལ་ནགས་མེས་བཏང་བ་ལ་སོགས་པའི་ཐབས་རྣམས་ཀྱིས་བཟུང་བའི་ཕྱིར་མངོན་པར་བརྩོན་པ་རྣམས་ལ་གང་ཞིག་དེ་རྣམས་ཀྱི་ནང༌[^1236]མངོན་པར་མི་བརྩོན་པ་དེ་ལ་མངོན་པར་བརྩོན་པ་ཉིད་ནི་བདག་པོ་ཉིད་དུ་དེར་གྱུར་ཏེ་མངོན་པར་མི་བརྩོན་པ་ནི་མ་ཡིན་ནོ། །

[Block 1767]
རྐུ་སེམས་ཀྱིས་འཛིན་པ་ལ་རྐུན་མའི་དངོས་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1768]
རི་དགས་ལ་སོགས་པ་སྨོས་པ་ནི་འདིར་དཔེ་ཡིན་ཏེ། མི་དང་ཕྱུགས་དག་ལ་ཡང་ཆོ་ག་འདི་སྦྱར་བའོ། །

[Block 1769]
བདག་དང་བདག་གི་དག་ལ་ཡང་ཡོད་པ་ཉིད་ཀྱི་ཕྱིར་བདག་པོ་སྐྱེས་པ་ལ་བདག་པོ་དང་བཅས་པར་སྦྱར་བའོ། །

[Block 1770]
བྱེ་བྲག་མ་ཕྱེད་པ་ལ་ནི་གཞི་ལས་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་ནི་བདག་པོ་དང་བཅས་པ་ཞིག་གམ་འོན་ཏེ་མ་ཡིན་ཞེས་བྱེ་བྲག་མ་ཕྱེད་པ་གང་ཞིག་དེ་ཡོད་མོད་ཅེས་བྱ་བ་གང་དུ་གཏེར་རམ། རྫས་གཞན་འཛིན་པ་དངོས་པོ༌[^1237]དེ་ལ་ནི་འདུ་ཤེས་ལས་རྣམ་པར་གཞག་པའོ། །

[Block 1771]
གལ་ཏེ་རྫས་དེ་བདག་པོ་དང་བཅས་པ་ཡིན་ན་བདག་པོ་དང་བཅས་པའི་སྐྱོན་ནོ། །

[Block 1772]
གལ་ཏེ་མིན་ན་བདག་པོ་མ་ཡིན་པ་ལ་སོགས་པ་ལྡང་བའི་སྐྱོན་ནོ། །

[Block 1773]
རིན་ཐང་ནི་བརྐུས་པའི་གནས་དང་དུས་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་རིན་ཐང་གི་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་འཇུག་གོ། །

[Block 1774]
བརྐུས་པའི་གནས་དང་དུས་གང་ཡིན་པ་དེས་རིན་ཐང་གི་རྣམ་པར་གཞག་པ་གང་དུ་བྱེད་པ་དང་། གང་གི་ཚེ་ན་དེར་དེའི་ཚེ་རིན་ཐང་དེས་དེར་ལྟུང་བྱེད་ཅེས་བྱ་བའི་དོན་དེ་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་འཇུག་གོ། །

[Block 1775]
མ་བསམས་པ༌[^1238]ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ལ། རྫས་གང་ཞིག་རྐུ་བ་ཉིད་ཀྱིས་མངོན་པར་མི་འདོད་པ་དེ་ལྟ་བུའམ་འོན་ཏེ་ཆེ་གེ་མོའི་ཡིན་ན་ཡང་བདག་གིས་རྐུའོ་སྙམ་སྟེ། འཁྲུལ་པས་བརྐུས་པར་གྱུར་པ་དེ་ལས་ལྟུང་བར་མི་འགྱུར་རོ། །

[Block 1776]
དེ་ལྟར་ན༌[^1239]ཡང་ཉེ་བ་འཁོར་གྱིས་ཞུས་པ་ལས།

[Block 1777]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་རྐུ་སེམས་ཀྱིས་ཆོས་གོས་ཀྱི་གདང་བུ་བརྐུས་པ་ལ་གལ་ཏེ་དེར་ཆོས་གོས་དག་ཀྱང་ཞར་ལ་མཆིས་ན་ལྟུང་བ་ཅིར་འགྱུར་ཆོས་གོས་ཀྱི་གདང་བུའི་རིན་ཐང་བརྩི་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེ་ལ་ཆོས་གོས་རྣམས་ནི་མངོན་པར་འདོད་པ་མ་ཡིན་ཏེ། དེ་བས་ན་དེ་ལ་བརྟེན་པའི་གྲངས་གསུངས་པ་མ་ཡིན་ནོ། །

[Block 1778]
རང་དང་བརྙ་བ་དང་ཡིད་གཅུགས༌[^1240]པའི་སེམས་དག་གིས་གཞན་ལ་གོ་བར་བྱ་སྟེ། བླངས་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་རྐུ་སེམས་མེད་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་དང་འབྲེལ་ལོ། །

[Block 1779]
རང་གི་སེམས་དང་བརྙ་བའི་སེམས་དང་ཡིད་གཅུགས་པའི་སེམས་ནི་རང་དང་བརྙ་བ་དང་ཡིད་གཅུག་པའི་སེམས་སོ། །

[Block 1780]
དེ་རྣམས་ཀྱིས་བཟུང་བ་ལ་རྐུ་སེམས་མེད་པས་ལྟུང་བ་མེད་དོ། །

[Block 1781]
དེ་ལྟར་ཡང་དགེ་སློང་གིས་རང་གི༌[^1241]ལྷུང་བཟེད་དང་ཆོས་གོས་ཀྱང་རྐུ་སེམས་ཀྱིས་ལེན་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 1782]
སེམས་འདི་རྣམས་ཀྱིས་ཀྱང་ལེན་པར་བྱེད་ན་གཞན་གྱིས་རྐུ་བའི་གླགས་བཟློག་པའི་དོན་དུ་དངོས་པོ་འདི་གཞན་ལ་གོ་བར་བྱ་བ་འདིར་རིགས༌[^1242]པ་ཡིན་ནོ། །

[Block 1783]
དེ་ལྟར་ན་ཡང་གཞན་ལ་གོ་བར་བྱའོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1784]
དོགས་པ༌[^1243]དང་བྲལ་བར༌[^1244]བྱ་བའི་ཕྱིར་བསྟན་པ་འདི་ཡིན་ཏེ། དོགས་པ༌[^1245]མེད་པར་དོན་དུ་གཉེར་བའི་ཕྱིར་འདི་བྱའོ། །

[Block 1785]
དེ་ལྟར་བྱས་ན་འགྱོད་པའི་གླགས་རྙེད་པར་མི་འགྱུར་བ་ཞེས་བྱ་བའོ། །

[Block 1786]
རང་དང་བརྙ་བ་དང་ཡིད་གཅུགས༌[^1246]པའི་སེམས་དང་གཞན་ལ་གོ་བར་བྱས་པ་རྣམས་ལས་རྣམ་པ་གཞན་གྱིས་ཀྱང་རྐུ་བའི་སེམས་མེད་པར་ལེན་པ་ལ་ལྟུང་བ་མེད་ཅེས་བསྟན་པའི་ཕྱིར། །རྐུ་སེམས་མེད་པ་གཞན་གྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1787]
རྣམ་པ་གཞན་གྱིས་ཀྱང་ཇི་ལྟར་ཉེས་པ་མེད་ཅེ་ན།

[Block 1788]
ཉེ་བ་འཁོར་གྱིས་ཞུས་པ་ལས།

[Block 1789]
དགེ་སློང་གིས་དགེ་སློང་ལ་འདི་སྐད་ཅེས་སྨྲས་ཏེ། ཁྱོད་ཀྱིས་དགེ་སློང་ཆེ་གེ་མོའི་ཡོ་བྱད་དེ་དང་དེ་དག་ཤེས༌[^1247]སམ་ཤེས་སོ། །

[Block 1790]
འོ་ན་སོང་ལ་དེ་དག༌[^1248]རྐུས༌[^1249]ཤིག །དེ་དག་ཕྲོགས་ཤིག །དེ་དག་གནས་ནས་ཡང་གཞན་དུ་སྤོགས་ཤིག་ཅེས་བསྒོ་ནས་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
