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
ཇི་ལྟར་ན་འདྲོན༌[^1272]པོས་བཏང་བའི་མེ་ཡང་འཁྲུལ་པ་ཡིན་ཏེ། མེ་ལས་བྱུང་བའི་ནུས་པ་ལ་བརྟེན་ནས་མེའི་རྒྱུ་གཞན་སྤོང་བར་བྱེད་དོ། །

[Block 1752]
གལ་ཏེ་མེ་མེད་པར་ཡང་འགྱུར་ན་ནི་གཞན་དག་ལ་ཡང་འགྱུར་རོ་ཞེ་ན། དེ་ལ་མེ་ཉིད་དང་ཅིག་ཤོས་ལས་བྱུང་བ་དག་ལ་གནོད་པར་བྱ་བ་དང་གནོད་པར་བྱེད༌[^1273]པ་མེད་པས༌[^1274]མེ་ལས་བྱུང་བ་ཉིད་ནི་གཞན་དག་ལ་ཡང་འགྱུར་བ། དེ་ལྟར་ན་ཆོས་གཉིས་དག་དོན་གཅིག་ལ་སྲིད་པའི་ཕྱིར། འདྲོན་པོས༌[^1275]བཏང་བའི་མེའམ། དོན་གཞན་ནི་གཅིག་ལ། སོ་སོར་ངེས་པར་འགྱུར་བ་མེད་པས་ན་འཁྲུལ་པར་དོགས་པ་ཡིན་ནོ། །

[Block 1753]
ཕན་ཚུན་ཐ་དད་པ་ཅན་གྱི་ཆོས་གཉིས༌[^1276]འཇུག་པ་དེ་ཡང་ཕྱིའི༌[^1277]དངོས་པོ་ལ་འགལ་བ་མེད་དོ། །ཞེས་བརྗོད་པར་བྱ་བའི་གནས་སྐབས་ཐ་དད་པ་ཅན་གྱི་ཁྱད་པར་ནི་མ་ཡིན་ཏེ། ཆ་མེད་པའི་བདག་ཉིད་ལས༌[^1278]དེ་ཉིད་དང་དེ་ཉིད་མ་ཡིན་པ་འགལ་བའི་ཕྱིར་རོ། །

[Block 1754]
འདྲོན་པོས༌[^1279]བཏང་བའི་མེ་ལ་མེ་དང་ཅིག་ཤོས་ཀྱིས་བསྐྱེད་པ་ནི་གནོད་བྱ་དང་གནོད་བྱེད༌[^1280]མ་ཡིན་ཏེ། དེ་ནི་མེས་བསྐྱེད་པ་མེད་པར་མི་སྲིད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1755]
དེ་ལྟ་བུར་གྱུར་པའི་འདྲོན༌[^1281]པོས་བཏང་བའི་མེ་མེ་ལས་བྱུང་བ་ཞེས་བྱ་བར་ནི་འགྱུར་གྱི། ཐམས་ཅད་ནི་མ་ཡིན་ཏེ། དེ་ལ་ཁྱད་པར་སྤོང་བར་བྱེད་པར་མི་ནུས་པའི་ཕྱིར་དང་། ཁྱད་པར་ཡོད་པ་ཅན་གྱི་དེའི་གནས་སྐབས་ཅན་ཉིད་ལ་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1756]
གལ་ཏེ་མེ་མེད་པར་ཡང་འགྱུར་ན་ནི་གཞན་དག་ལ་ཡང་འགྱུར་རོ། །ཞེས་བྱ་བ་གལ་ཏེ་ཚོགས་པ་གང་གིས་དེར་འགྱུར་བ་ན་དེ་འགྱུར་ཞིང་འགྱུར་བ་ཉིད་ཡིན་ནོ། །

[Block 1757]
དེ་ཡོད་པས༌[^1282]བསྟན་ནས་དེ་མེད་པར་བསྟན་པར༌[^1283]འགྱུར་བའམ་དེ་ལ་མེའམ༌[^1284]དེ་མེད་པར་སྟོན་ན་དེར་འགྱུར་རོ། །

[Block 1758]
དེ་བས་ན་གཅིག་གིས་འདོན་པར་བྱེད་པ་གཞན་སྔོན་དུ་སོང་བ་ཅན་ཡིན་པ་དེ་ལྟ་བུའི་ངོ་བོར་ཐམས་ཅད་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་ཏེ། དེ་ལ་རྣམ་པ་གཞན༌[^1285]དུ་མི་སྲིད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1759]
དེ་བྱེད་པའི་སྤོབས་པ་དང་བྲལ་བ་དེ་ལྟ་བུའི་རྣམ་པ་ལ་ནི་དེ་ལྟར་འགྱུར་བའི་ཕྱིར་དེ་ལྟ་བུར་གྱུར་པ་ཁོ་ན་བརྗོད་པར་བྱ་བར་འགྱུར་ལ། བྱེ་བྲག་མེད་པར་ཁྱད་པར་སྲིད་པ་ཅན་དེ་བརྗོད་ན་ནི་མཛེས་པར༌[^1286]ཐོབ་པ་མ་ཡིན་ནོ། །ཇི་ལྟར་ཁྱད་པར་སྲིད་པ་ཡིན། །གང་གི་ཚེ་སྐྱེས་བུས་དེ་དག་ཀྱང་ནུས་པ་མེད་པ་ཁོ་ན་ཡིན་ཏེ། ད་ལྟར་བའི་སྐྱེས་བུ་འདྲའོ། །

[Block 1760]
ནུས་པ་དག་ལ་འགལ་བ་ཅུང་ཟད་ཀྱང་མཐོང་བ་མེད་པའི་ཕྱིར་དང་། མི་འགལ་བ་སྒྲུབ་པ་ཅན་མི་དམིགས་པའི་སྦྱོར་བ་ནི་གོ་བར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1761]
དབང་པོ་ལས་འདས་པ་དག་ལ་ནི་འགལ་བ་རྟོགས་པ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 1762]
སྦྱོར་བ་འདི་ཡང་སྦྱོར་བ་སྔ་མ་ལས་ཐ་དད་པ་མ་ཡིན་ནོ། །

[Block 1763]
གལ་ཏེ་སྐྱེས་བུས་ནུས་པར་འགྱུར་ན་ད་ལྟར་བས་ཀྱང་ཡིན་ནོ་ཞེ་ན། ཁྱད་པར་མེད་པ་ཡིན་ན་དེར་འགྱུར་ན། དེ་ཡང་བསྒྲུབ་པར་དཀའ་བ་ཡིན་ནོ། །

[Block 1764]
གང་ལ་གཅིག་ནུས་པ་མེད་པ་དེ་ལས་སྐྱེས་བུས་ཐམས་ཅད་ཀྱང་ཞེས་བྱ་བ་ཡང་སྔ་མ་བཞིན་དུ་འཁྲུལ་པ་ཡིན་ཏེ། བྷ་ར་ཏ་ལ་སོགས་པ་ད་ལྟར་བ་རྣམས་ལ་ཡང་ནུས་པ་མེད་པ་ཡིན་ན་ཡང་འགའ་ཞིག་ལ་ནུས་པ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1765]
དེ་བས་ན་རྒྱུ་རྣམ་པར་འབྱེད་པར་བྱེད་པས། དེ་ལས་བྱུང་བ་ཅན་དང་དེ་ལས་བྱུང་བ་ཅན་མ་ཡིན་པའི་དོན་རྣམས་ཀྱི་ཡང་རང་བཞིན་གྱི་ཁྱད་པར་བསྟན་པར་བྱའོ། །

[Block 1766]
དེ་མེད་ན་ཐམས་ཅད་དེའི་བདག་ཉིད་ཅན་ནམ་འགའ་ཞིག་ཀྱང་མ་ཡིན་ནོ། །

[Block 1767]
འདི་ལ་འཇིག་རྟེན་པ་དང་རིག་བྱེད་པ་དག་གི་རང་བཞིན་གྱི་ཁྱད་པར་མཐོང་བ་མེད་དོ། །

[Block 1768]
དེ་ཡོད་པ་མ་ཡིན་པ་དེ་དག་མཚུངས་པ་ཉིད་དུ་མཐོང་བའི་ཕྱིར། གཅིག་གི་ཆོས་འགའ་ཞིག་རྣམ་པར་འབྱེད་པའི་དེའི་རང་བཞིན་སྲིད་པ་དེས་འཁྲུལ་པར་དོགས་པའི་བརྗོད་པ་ཅན་དུ་འབྱེད་དོ། །

[Block 1769]
[^1287]རིག་བྱེད་དེ༌[^1288]རིག་བྱེད་མ་ཡིན་པ་དག་ལ་དེ་ཉིད་ཀྱི་མཚན་ཉིད་ཅན་གྱི་ཁྱད་པར་ཡོད་པ་མ་ཡིན་ནམ། །ཡོད་པ་བདེན་ཏེ་དེ་དག་འབའ་ཞིག་ཁོ་ན་ལ་མ་ཡིན་ཏེ། འོན་ཀྱང་ཁ་བྱའི༌[^1289]མནའ་གཏམ་དང་ཅིག་ཤོས་དག་ལ་ཡང་ཡིན་ནོ། །

[Block 1770]
རང་ཉིད་ཀྱི་ལོ་རྒྱུས་ཀྱི་བྱེ་བྲག་གསལ་བར་བྱེད་པའི་མིང་གི༌[^1290]ཁྱད་པར་གྱིས་སྐྱེས་བུས་བྱས་པ་ལ་གནོད་པ༌[^1291]མ་ཡིན་ཏེ། གཞན་དག་ལ་ཡང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1771]
གལ་ཏེ་དེ་འདྲ་བའི་སྦྱོར་བ་སྐྱེས་བུས་བྱེད་པར་མི་ནུས་པར་འགྱུར་བའམ། བྱས་པ་ལམ་བྱས་པའི་བརྡས་རྣམ་པར་འབྱེད་པས༌[^1292]འགྱུར་བ་ན། རིག་བྱེད་སྐྱེས་བུས་མ་བྱས་པར་གསལ་བ༌[^1293]ཡིན་ནོ། །

[Block 1772]
སྐྱེས་བུ་དག་གི་སྔགས་བྱེད་པའི་ནུས་པ་དང་མི་ལྡན་པ་ཁོ་ན་མ་ཡིན་ནམ། དེ་ནི་འོག་ནས་རྣམ་པར་དཔྱད་པར་བྱའོ། །

[Block 1773]
གཞན་ཡང་སྔགས་ཞེས་བྱ་བ་གཞན་ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1774]
འོ་ན་ཅི་ཡིན་ཞེ་ན། བདེན་པ་དང་དཀའ་ཐུབ་ཀྱི་མཐུ་དང་ལྡན་པའི་འདོད་པའི་དོན་སྒྲུབ་པར་བྱེད་པའི་ཚིག་ཡིན་ཏེ། [^1294]དེ་ནི་ད་ལྟར་ཉིད་ཀྱང་སྐྱེས་བུ་རྣམས་ལ་སྣང་བ་ཁོ་ན་ཡིན་ཏེ། བདག་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་བདེན་པའི་བྱིན་གྱི་རླབས༌[^1295]ཀྱི་སྟོབས་ལས་དུག་དང་མེ་ལ་སོགས་པ་ཀུན་ནས་རེངས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1775]
ད་ལྟར་ཡང་རི་ཁྲོད་འགའ་ཞིག་སྔགས་བྱེད་པའི་ཕྱིར་དང་། རིག་བྱེད་མ་ཡིན་པའི༌[^1296]སངས་རྒྱས་ལ་སོགས་པའི་སྔགས་དང་རྟོགས་པ༌[^1297]དག་མཐོང་བའི་ཕྱིར་རོ། །

[Block 1776]
དེ་དག་ཀྱང་སྐྱེས་བུས༌[^1298]མ་བྱས་པ་ཉིད་ཡིན་ན་ད༌[^1299]སྐྱེས་བུས་མ་བྱས་པ་བདེན་པ་ཡིན་ཏེ། འདི་ལྟར་སངས་རྒྱས་པ་དང་ཅིག་ཤོས་དག་གི་སྔགས་དང་རྟོགས་པ༌[^1300]དག་ལ་འཚེ་བ་དང་། འཁྲིག་པ་དང་བདག་ཏུ་ལྟ་བ་ལ་སོགས་པ་མངོན་པར་མཐོ་བ་མ་ཡིན་པའི་རྒྱུ་དང་རྣམ་པ་གཞན་དུ་བརྗོད་དོ། །

[Block 1777]
དེ་ཇི་ལྟར་ན་གཅིག་ལ་འགལ་བ་བརྗོད་ན་གཉིས་བདེན་པར་འགྱུར། དེ་ལ་དོན་གཞན་དུ་རྟོགས་པ༌[^1301]ན་དེ་ནི་གཞན༌[^1302]ལ་ཡང་མཚུངས་པ་དེ་ལྟར་ན་དོན་ལ་ངེས་པའི་ཕྱིར། འགའ་ཞིག་ཀྱང་རྟོགས་པར་མི་འགྱུར་རོ། །

[Block 1778]
དེ་ལྟར་ན་ཡང་སྐྱེས་བུས་མ་བྱས་པ༌[^1303]ཡིན་དུ་ཟིན་ཀྱང་ཉེ་བར་མཁོ་བ་མ་ཡིན་ནོ། །

[Block 1779]
སངས་རྒྱས་པ་ལ་སོགས་པ་དག་གི་སྔགས་ཉིད་མ་ཡིན་ན་དེ་ལས་གཞན་པ་ལ་ཡང་མནའ༌[^1304]ཆུ་བཏུང་དགོས་པར་འགྱུར་རོ། །

[Block 1780]
སངས་རྒྱས་པ་ལ་སོགས་པ་དག་དུག་གི་ལས༌[^1305]ལ་སོགས་པ་བྱེད་པ་མཐོང་སྟེ། དེ་ལ་ཡང་སྔགས་ཉིད་བཀག་པ་མེད་དོ། །

[Block 1781]
ཕྱག་རྒྱ་དང་དཀྱིལ་འཁོར་དང་བསམ་གཏན་ཡི་གེ་མེད་པ་ཅན་དག་གིས་ཀྱང་ལས་རྣམས་བྱེད་པར་འགྱུར་ཏེ། དེ་དག་ནི་སྐྱེས་བུས་མ་བྱས་པ་དང་རྟག་པར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1782]
དེ་དག་གི་བྱེད་པ་ཡོད་ན་སྐྱེས་བུ་རྣམས་ཡི་གེ་བཀོད་པ་བྱེད་པ་ལ་འགལ་བ་ཅི་ཡོད། དེ་བས་ན༌[^1306]དེ་དག་གི་བྱེད་པ་ནུས་པ་མེད་པ་ན་ཅིར་ཡང་མི་རུང་ངོ་། །ད་ནི་ཇི་ལྟར་ན་བདེན་པ་ལས་བྱུང་བ་ཅན་གྱི་སྔགས་དང་རྟོགས་པ༌[^1307]ཕན་ཚུན་འགལ་བ་དག་ཡིན། དེ་དག་ནི་ཐམས་ཅད་དུ་བདེན་པ་ལས་བྱུང་བ་ཅན་དག་མ་ཡིན་ཏེ། སྐྱེས་བུ་མཐུ་དང་ལྡན་པའི་དམ་བཅས་པའི་མཚན་ཉིད་ཅན་དག་ལ་ཡང་འགྱུར་རོ། །

[Block 1783]
མཐུ་དེ་ནི་འགྲོ་བ་དང་གྲུབ་པའི་ཁྱད་པར་དག་ལས་ཀྱང་འགྱུར་རོ། །

[Block 1784]
གལ་ཏེ་སྔགས་སྐྱེས་བུས་བྱས་པ་ཡིན་ན་སྐྱེས་བུ་ཐམས་ཅད་ཅིའི་ཕྱིར་སྔགས་བྱེད་པ་མ་ཡིན་ནོ་ཞེ་ན། དེ་བྱེད་པའི་སྒྲུབ་པར་བྱེད་པ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1785]
གལ་ཏེ་དེ་འདྲ་བའི་བདེན་པ་དང་དཀའ་ཐུབ་ལ་སོགས་པ་དང་ལྡན་པར་འགྱུར་ན་བྱེད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1786]
གཞན་ཡང་སྐྱེས་བུ་སྙན་དངགས་བྱེད་པའི་ཕྱིར། །སྐྱེས་བུ་ཐམས་ཅད་སྙན་དངགས་བྱེད་པར་འགྱུར་ལ། མི་བྱེད་ན་འགའ་ཞིག་ཀྱང་མི་བྱེད་པ་དེ་དང་འདྲ་བར་དེ་ལྟར་ན་རིག་པ་དེ་དག་ནི་སྔ་ན་མེད་པ་ཡིན་ནོ། །

[Block 1787]
སྔགས་བྱེད་པའི་སྒྲུབ་པར་བྱེད་པ་དང༌[^1308]བྲལ་བ་དག་སྔགས་མི་བྱེད་པ་ནི་བདེན་ན། ཚོགས་པ་དེ་ཡང་འགའ་ཞིག་ལ་ཡང་མ་མཐོང་སྟེ། སྐྱེས་བུ་རྣམས་ནི་ཆོས་མཚུངས་པ་ཅན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1788]
འདིར་སྔགས་ཞེས་བྱ་བ་བདེན་པ་ལ་སོགས་པ་དང་ལྡན་པའི་ཚིག་དང་དམ་བཅས་པ་ལས་གཞན་ཅུང་ཟད་ཀྱང་མེད་དོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 1789]
དེ་དག་ཀྱང་སྐྱེས་བུ་འགའ་ཞིག་ལ་མཐོང་ངོ་། །སྐྱེས་བུ་ཐམས་ཅད་དེ་དང་བྲལ་བ་ཡིན་པ་དེ་ལྟ་ཡང་ངེས་པ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ཡོད་པ་ལ་འགལ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1790]
ལྐོག་ཏུ་གྱུར་པའི་རང་བཞིན་ཅན་དག་ལས་མི་དམིགས་པའི་ངེས་པའི་གཏན་ཚིགས་མ་ཡིན་ནོ། །
--- END BLOCKS ---
