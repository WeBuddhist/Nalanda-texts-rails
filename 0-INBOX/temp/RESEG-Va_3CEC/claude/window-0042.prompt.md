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
[Block 1471]
འབྱུང་བ་མངོན་སུམ་དུ་གྱུར་པ་ནི་ཟག་པ་ཟད་པ་མངོན་སུམ་དུ་བྱས་པ་སྟེ། སློབ་དཔོན་ཐོགས་མེད་ཀྱིས་མངོན་སུམ་དུ་གྱུར་པ་དྲུག་ཡོད་པའི་ཕྱིར་བསྡུས་པའི་དོན་གྱི་ནང་དུ་སྨོས་མོད་ཀྱིས།[^1274] དེ་བཞིན་གཤེགས་པ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས༌[^1275]ཟག་པ་ཟད་པ་མངོན་སུམ་དུ་མ་བྱས་པས་ན་མདོ་ལས་ནི་མ་གསུངས་སོ། །

[Block 1472]
[^1276]

[Block 1473 [HEADING]]
## ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ། ^4-0

[Block 1474]
ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^1277]ཏིའི་བུ་གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་བསྡུ་བའི་དངོས་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བསྡུ་བའི་དངོས་པོ་ནི་དགའ་བའི་དངོས་པོ་འམ། ཕན་པར་བྱེད་པའི་དངོས་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1475]
དེ་མི་ཟད་པ་ཡང་དེས་བསྡུ་བར་བྱ་བའི་སེམས་ཅན་མི་ཟད་པས་སྡུད་པར་བྱེད་པའི་དངོས་པོ་ཡང་མི་ཟད་པའོ། །

[Block 1476]
འདིར་ཡང་བསྟན་པ་དང་། བཤད་པའི་ཚུལ་དུ་རིག་པར་བྱ་སྟེ། བཞི་གང་ཞེ་ན། འདི་ལྟ་སྟེ་སྦྱིན་པ༌[^1278]དང་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་བསྟན་པའི་ཚུལ་བཤད་དོ། །

[Block 1477]
ལྷག་མ་རྣམས་ཀྱིས་ནི་བཤད་པའི་ཚུལ་བཤད་དོ།[^1279] །ཡོངས་སུ་སྨིན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡང་རྣམ་པ་བཞི་སྟེ། རྗེས་སུ་ཕན་འདོགས་པ་དང་། ཕན་འདོགས་པར་བྱེད་པ་དང་། འཇུག་པ་དང་། རྗེས་སུ་འཇུག་པར་བྱེད་པའོ། །

[Block 1478]
བསྡུ་བའི་དངོས་པོ་བཞིས་ནི་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱེད་པས། དེ་དག་ཉིད་ཀྱིས་སའི་དོན་ཡོངས་སུ་སྨིན་པར་བྱེད་པའི་མཐུ་བསྟན་ཏོ། །

[Block 1479 [HEADING]]
### རྗེས་སུ་ཕན་འདོགས་པ། ^4-1-0

[Block 1480]
རྗེས་སུ་ཕན་འདོགས་པ༌[^1280]བསྟན་པའི་ཕྱིར། དེ་ལ་སྦྱིན་པ་ནི་ཟང་ཟིང་སྦྱིན་པ་དང་ཆོས་སྦྱིན་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། ནོར་དང་། འབྲུ་ལ་སོགས་པ་སྦྱིན་པ་ནི་ཟང་ཟིང་སྦྱིན་པའོ། །

[Block 1481]
ཟང་ཟིང་མེད་པའི་བསམ་པས་གསུང༌[^1281]རབ་ཡན་ལག་བཅུ་གཉིས་ཐོས་པ་གཞན་ལ་སྟོན་པ་ནི་ཆོས་ཀྱི་སྦྱིན་པ་སྟེ། དེ་གཉིས་སྦྱིན་པ་ལ་སྦྱིན་པ་ཞེས་བྱའོ། །

[Block 1482 [HEADING]]
### ཕན་འདོགས་པར་བྱེད་པ། ^4-2-0

[Block 1483]
ཕན་འདོགས་པར་བྱེད་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་སྙན་པར་སྨྲ་བ་ནི་གང་སློང་བ་དང་ཆོས་ཉན་པ་རྣམས་ཚིག་འཇམ་ཞིང་སྙན་པར་སྨྲ་བའོ༌[^1282]ཞེས་གསུངས་ཏེ།[^1283] འདིར་ཡང་ཟང་ཟིང་སློང་བ་རྣམས་ལ་ཚིག་འཇམ་ཞིང་སྙན་པར་སྨྲ་བ་དང་ཆོས་ཉན་པ་རྣམས་ལ་ཚིག་འཇམ་ཞིང་སྙན་པར་སྨྲ་བའོ། །

[Block 1484]
དེ་ལ་ཚིག་འཇམ་པ་ནི་མིག་བཟློག་པ་དང་། གཉེར་མ་བསྡུས་པ་ལ་སོགས་པ་མེད་པར་བྱ་སྟེ། བདེ་བར་འོངས་པ་དང་འདིར་འོངས་པ་ལ་ལེགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨྲ་བའོ། །

[Block 1485]
སྙན་པར་སྨྲ་བ་ནི་ཕྱིས་འོངས་ནའང་དེ་བཞིན་དུ་སྦྱིན་པར་བྱའོ་ཞེས་སྨྲ་བའོ། །

[Block 1486]
ཡང་ན་སློང་བ་དང་ཆོས་ཉན་པའི་སྐྱོན་མི་གླེང་བ་ནི་ཚིག་འཇམ་པའོ། །

[Block 1487]
དེ་དག་གི༌[^1284]ཡོན་ཏན་བརྗོད་པ་ནི་སྙན་པར་སྨྲ་བ་སྟེ། འདི་ནི་སྙན་པར་སྨྲ་བ་ཞེས་བྱའོ། །

[Block 1488 [HEADING]]
### འཇུག་པ། ^4-3-0

[Block 1489]
འཇུག་པ་བསྟན༌[^1285]པའི་ཕྱིར་དེ་ལ་དོན་སྤྱོད་པ་ནི་གང་བདག་དང་གཞན་གྱི་དོན་བསམས་པ་བཞིན་དུ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའོ་ཞེས་བྱ་བ་གསུངས་ཏེ། གང་བདག་གི་དོན༌[^1286]བསམས་པ་བཞིན་རྫོགས་པར་བྱེད་པ་དང་། གཞན་གྱི་དོན་བསམས་པ་བཞིན་དུ་རྫོགས་པར་བྱེད་པ་ནི་དོན་སྤྱོད་པའོ། །

[Block 1490]
དེ་ལ་བསམས་པ༌[^1287]བཞིན་དུ་རྫོགས་པར་བྱེད་པ་ནི་བདག་ཉིད་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པར་བྱ་བའི༌[^1288]ཕྱིར་ཟང་ཟིང་དང་ཆོས་གཏོང་བར་འདོད་པ་ལས།

[Block 1491]
ཇི་ལྟར་འདོད་པ་བཞིན་དུ་ཟང་ཟིང་སློང་ཞིང་ཆོས་ཉན་པ་དང་ཕྲད་ནས་དེ་དག་ལས༌[^1289]ཟང་ཟིང་བཏང་ཞིང་ཆོས་བཤད་པའོ། །

[Block 1492]
དེ་ལ་སེམས་ཅན་ཡང་ཚེ་འདིར་ལོངས་སྤྱོད་འདོད་པ་དང་། ཚེ་རབས་གཞན་དུ་རྣམ་པར་གྲོལ་བ་འདོད་པ་རྣམ་པ་གཉིས་ཏེ། སློང་བ་རྣམས་ལ་ཡང་ཟང་ཟིང་བཏང་ནས་ཇི་ལྟར་བསམས་པ་བཞིན་དུ་བསམ་པ་རྫོགས་པར་བྱེད་པའོ། །

[Block 1493]
ཚེ་རབས་གཞན་དུ་རྣམ་པར་ཐར་པ་འདོད་པ་ལ་ཡང་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་ལ་སོགས་པའི་ཆོས་བསྟན་ནས་ཇི་ལྟར་བསམས་པ་བཞིན་དུ་བསམ་པ་རྫོགས་པར་བྱེད་པའོ། །

[Block 1494 [HEADING]]
### རྗེས་སུ་འཇུག་པར་བྱེད་པ། ^4-4-0

[Block 1495]
རྗེས་སུ་འཇུག་པར་བྱེད་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་དོན་མཐུན་པ་ནི་གང་ཐེག་པ་གང་ལ་བདག་ཡོན་ཏན་དུ་འདུ་ཤེས་པའི་ཐེག་པ་དེ་ཉིད་ལ་ཆོས་དང་ཟང་ཟིང་ལེན་པ་རྣམས་རབ་ཏུ་འགོད་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞེས་བྱ་བའི་སྒྲ་ནི༌[^1290]བྱང་ཆུབ་སེམས་དཔའ་དང་སྦྱར་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་གང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1496]
ཐེག་པ་གང་ལ་ཞེས་བྱ་བ་ནི་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་མཚན་ཉིད་ཐེག་པ་ཆེན་པོ་གང་ལ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1497]
བདག་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཉིད་དོ། །

[Block 1498]
ཡོན་ཏན་དུ་འདུ་ཤེས་པ་ནི་ཐེག་པ་དེ་ལ་མཆོག་དང་གཙོ་བོར་བལྟ༌[^1291]བའོ། །

[Block 1499]
ཐེག་པ་དེ་ཉིད་ལ་ཞེས་བྱ་བ་ནི་ཐེག་པ་གང་ལ་ཡོན་ཏན་དང་གཙོ་བོར་བལྟས་པའི་ཐེག་པ་དེ་ཉིད་ལའོ། །

[Block 1500]
རབ་ཏུ་དགོད་པ་ནི་བདག་ཞུགས་པ་བཞིན་དུ་གཞན་ཡང་འཛུད་པ་སྟེ། ཐེག་པ་གཅིག་གི་དོན་ལ་བདག་དང་གཞན་གཉིས་ཀར་གནས་པར་བྱེད་པ་འདི་ནི་དོན་མཐུན་པའོ། །

[Block 1501 [HEADING]]
### བསྡུ་བའི་དངོས་པོ་བཞི་རྣམ་གྲངས་གཞན་དུ་བསྟན་པ། ^4-5-0

[Block 1502]
བསྡུ་བའི་དངོས་པོ་བཞི་རྣམ་གྲངས་གཞན་དུ་བསྟན་པའི་ཕྱིར། གཞན་ཡང་སྦྱིན་པ་ནི་གང་སློང་པ་རྣམས་ལ་ཡིད་མགུ་བར་སྦྱིན་པ་ཞེས་གསུངས་ཏེ། གོང་མ་བཞིན་དུ་འདི་མན་ཆད་བསྡུ་བའི་དངོས་པོ་འབྱུང་བ་རྣམས་ལ་ཡང་བསྡུས་པའི་དོན་རེ་རེ་དང་སྦྱར་བའོ། །

[Block 1503]
སློང་བ་རྣམ་པ༌[^1292]གང་ཇི་སྙེད་ཅིག་ཇི་ལྟར་འདོད་པ་བཞིན་སྦྱིན་པ་ནི་སློང་བ་རྣམས་ལ་ཡིད་མགུ་བར་སྦྱིན་པ་སྟེ། གང་སྦྱིན་པ་ནི་དངོས་པོ་གང་འདོད་པ་དེ་སྦྱིན་པའོ། །

[Block 1504]
ཇི་སྙེད་སྦྱིན་པ་ནི་ཕྱི་དང་ནང་གི་དངོས་པོ་ཇི་སྙེད་འདོད་པ་དེ་དག་ཀུན་སྦྱིན་པའོ། །

[Block 1505]
ཇི་ལྟར་སྦྱིན་པ་ནི་རིམ་གྲོ་དང་བཀུར་སྟི་བྱས་ནས་སྦྱིན་པའོ། །

[Block 1506]
སྙན་པར་སྨྲ་བ་ནི་སློང་བ་རྣམས་ལ་མི་སྨོད་པའོ་ཞེས་བྱ་བ་ལ། ཟང་ཟིང་སློང་བ་པོ་རྣམས་ལ་རིགས་ངན་འདི། དབུལ་པོ་འདི་ཞེས་བྱ་བ་ལ་སོགས་པ་སེམས་གདུང་བར་འགྱུར་བའི་ཚིག་མི་སྨྲ་བ་ནི་སྙན་པར༌[^1293]སྨྲ་བའོ། །

[Block 1507]
དེ་ལ་དོན་སྤྱོད་པ་ནི་གང་སློང་བ་རྣམས་ཀྱི་དོན་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའོ་ཞེས་བྱ་བ་ལ། སློང་བ་རྣམས་ཚེ་འདིར་ཡང་དབུལ་བ་མེད་པར་བྱ་སྟེ། ལོངས་སྤྱོད་ཀྱི་འབྱོར་པ་དང་ལྡན་པར་བྱས་ནས། མི་དགེ་བ་ལ་མི་འཛུད་ཅིང་དགེ་བ་ལ་འཇོག་པ་ནི་དོན་སྤྱོད་པ་ཞེས་བྱའོ། །

[Block 1508]
དེ་ལ་དོན་མཐུན་པ་ནི་གང་ཐེག་པ་དེ་ཉིད་ལ་ཡང་དག་པར་འཛུད་པའོ་ཞེས་བྱ་བ་ལ། གང་ནི་སློང་བ་པོའི་གང་ཟག་གམ་བྱང་ཆུབ་སེམས་དཔའ་གང་ངོ་། །ཐེག་པ་དེ་ཉིད་ལ་ཡང་དག་པར་འཛུད་ཅེས་བྱ་བ་ནི་གང་ཟག་དེ་ཐེག་པ་གང་ལ་དད་པའི་ཐེག་པ་དེ་ཉིད་ལ་གང་ཟག་དེ་འཛུད་པའམ། བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་གང་ལ་གནས་པའི་ཐེག་པ་དེ་ཉིད་ལ་སློང་བ་པོའི༌[^1294]གང་ཟག་དེ་འཇུད་པ་སྟེ། འདི་ནི་དོན༌[^1295]མཐུན་པ་ཞེས་བྱའོ། །

[Block 1509]
རྣམ་གྲངས་གཞན་བསྟན་པར་བཞེད་ནས། གཞན་ཡང་སྦྱིན་པ་ནི་བསམ་པ་ཐག་པ༌[^1296]ནས་སྟོང་པའོ༌[^1297]ཞེས་བྱ་བ་གསུངས་ཏེ། བཟའ་བ་དང་བགོ་བ་ལ་སོགས་པའི་ཟང་ཟིང་རྣམས་ལ་ཅུང་ཟད་ཀྱང་ཆགས་པའི་སེམས་མེད་པར་སྟོང་པ༌[^1298]ནི་སྦྱིན་པའོ། །

[Block 1510]
སྙན་པར་སྨྲ་བ་ནི་གང་སྦྱོར་བ་ལ་ཡོངས་སུ་ཆད་པ་མེད་པའོ་ཞེས་བྱ་བ་ལ། སློང་བ་པོ་རྣམས་ལ་ཕྱིས་ཀྱང་སྦྱིན་པར་བྱ་ཡིས་རྒྱུན་དུ་ཤོག་ཅིག་ཅེས་སྨྲས་ནས་སྦྱིན་པ་གཏོང་བའི་ལས་རྒྱུན་མི་འཆད་པར༌[^1299]བྱེད་པ་ནི་སྙན་པར་སྨྲ་བའོ། །
--- END BLOCKS ---
