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
དེ་སྦྱང་བ༌[^777]ནི་ཡོངས་སུ་དག་པར༌[^778]བྱ་བའི་ཕྱིར་རོ། །

[Block 1472]
ཞེ་སྡང་ཞེས་པའི་བཤད་པ་ཐུགས་རྗེ་ཆེན་པོའི་ཐབས་ཀྱི་ཁྲོ་བ༌[^779]ནི་ཐུགས༌[^780]རྗེ་ཆེན་པོས་སྤྲུལ་པའོ། །

[Block 1473]
དེ་ཡང་རབ་ཏུ་ཁྲོས་པའི༌[^781]ཆོས་དང་ལྡན་པས་ནི་ཞེ་སྡང་སྟེ། གང་ལ་ཞེ་སྡང་དང་འདྲ་བའི་ཆོས་ཡོད་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1474]
དེའི་རིགས༌[^782]ནི་དེའི་རིགས་སུ་སྐྱེད་པའོ། །

[Block 1475]
འདོད་པའི་འབྲས་བུ་སྐྱེད་པ་ནི་སྔགས་དང་མཐུན༌[^783]པའི་ལུས་སྐྱེད་པའོ། །

[Block 1476]
ཇི་ལྟར་སྐྱེ་ཞེ་ན། སྐུ་དང་ཞེས་བྱ་བ་ལ་སོགས་པའི་བཤད་པ་སྙོམས་པར་ཞུགས་པ་ཞེས་པ་ནི་ཡབ་ཡུམ་སྦྱོར་བ་ལས་ཏེ་མངལ་ནས་སྐྱེས་པའི་ཚུལ་ཅན་ནོ། །

[Block 1477]
བཛྲ་དྷྲིཀ་ཅེས་པས་ནི་དབྱུང་བའི་སྔགས་བསྟན་ཏོ། །

[Block 1478]
དེའི་དོན་ཅི་ཞེ་ན་རྡོ་རྗེ་འཆང་ཞེས་པའོ། །

[Block 1479]
དེ་ཉིད་བཤད་པ།[^784] མངོན་པར་བྱང་ཆུབ་པ་ནི་བསྐྱེད་པའི༌[^785]རིམ་པའི་ས་བོན་ལ་སོགས་པའོ། །

[Block 1480]
དེ་མཚོན་པའི་རྡོ་རྗེ་རྩེ་ལྔ་པ་གང་གིས་འཛིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1481]
བདེན་པ་གཉིས་ནི་དོན༌[^786]དམ་པ་དང་ཀུན་རྫོབ་སྟེ་གཉིས་སུ་མེད་པ་ནི་སྤྲོས་པ་ཐམས་ཅད་དང་བྲལ་བའོ། །

[Block 1482]
དེ་ཉིད༌[^787]རྡོ་རྗེ་སྟེ་རྣམ་པར་རྟོག་པའི་རི་བོ་གཅོད་པ་སྟེ། དེ་གང་དང་ལྡན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1483]
དེ་སྤྲོས་ནས་ཕྱི་རོལ་གྱི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཞེ་སྡང་རྣམ་པར་སྦྱངས་ཏེ། སླར་ལོག་ནས་གཙོ་བོའི་མདུན་དུ་བཞུགས་སོ་ཞེས་བྱའོ། །ཇི་ལྟ་བུའི་རྣམ་པར་བཞུགས་ཤེ་ན། མི་བསྐྱོད་པའི་ཕྱག་རྒྱ་ཆེན་པོའི་ངོ་བོར་བཞུགས་སོ་ཞེའོ། །

[Block 1484]
དེ་ལྟར་སྦྱོར་བ་དང་པོ་ནི་ཏིང་ངེ་འཛིན་དང་པོ་ཉིད་དོ། །

[Block 1485]
སེམས་ཅན་རྨོངས་པ་ནི་རྒྱུ་དང་འབྲས་བུ་དང་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་མི་ཤེས་པའོ། །

[Block 1486]
དེ་སྦྱང་བ༌[^788]ནི་དེའི་ཉེས་པ་སེལ་བའོ། །

[Block 1487]
གཞན་ནི་གོ་སླའོ། །

[Block 1488]
དབྱུང་བའི་སྔགས་ནི་ཛི་ན་ཛིཀ་ཅེས་པའོ། །

[Block 1489]
རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ནི་སྐད་ཅིག་མ་གཅིག་གིས་སྒྲིབ་པ་ཐམས་ཅད་དང་བྲལ་བར་བྱེད་པའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 1490]
ཀུན་རྫོབ་ཀྱི་བྱང་ཆུབ༌[^789]སེམས་ནི་བཤད་ཟིན་ཏོ། །

[Block 1491]
འདི་ནི་གཞན་དུ་ཡང་སྟེ། གང་གི་ཏིང་ངེ་འཛིན་གྱིས་གང་ཤེས་པའི་ཏིང་ངེ་འཛིན་གྱིས་དེ་ཡང་ཤེས་པ་ཉིད་དོ། །

[Block 1492]
ཡང་དག་པའི་མཐའ་ནི་དེ་བཞིན་ཉིད་དེ་དེ༌[^790]ཡེ་ཤེས་གང་གིས་ཡུལ་དུ་བྱས་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1493]
ནོར་གྱིས༌[^791]དྲེགས་པ་ནི་ནོར་ལ་དགའ་བར་བྱེད་པའོ། །

[Block 1494]
ཁེངས་པ་ནི༌[^792]ང་རྒྱལ་ཆེན་པོ་ཉིད་དང་ལྡན་པར་གྱུར་པ་ཉིད་དོ། །

[Block 1495]
སྦྱིན་པས་འདུལ་བ་ནི་ནོར་བུ་རིན་པོ་ཆེའི་སྤྲིན་གྱིས་ང་རྒྱལ་རབ་ཏུ་ཞི་བར་བྱེད་པའོ། །

[Block 1496]
ང་རྒྱལ་རྣམ་པར་དག་པའི་གནས་ལ་ཡང་དག་གཞག་པ་ནི་དེས་ང་རྒྱལ་གྱི་རང་བཞིན་དང་བྲལ་བའི་དོན་དམ་པའོ། །

[Block 1497]
གཞན་ནི་གོ་སླའོ། །

[Block 1498]
འདོད་ཆགས་ནི་འཁྲིག་པ་དང་ཡུལ་ལ་ཆགས་པའོ། །

[Block 1499]
དེ་ཡང་གང་གིས་སྤོང་ཞེ་ན་བཅོམ་ལྡན་འདས་འོད་དཔག་ཏུ་མེད་པའི་རྣལ་འབྱོར་ཏེ། ཏིང་ངེ་འཛིན་གང་གིས་དེ་ཡུལ་དུ་བྱས་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1500]
གང་གིས་དེ༌[^793]ལྟ་བུའི་རང་བཞིན་ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཕྱིར་གསུངས་སོ་ཞེས་སྦྱར་རོ། །

[Block 1501]
འདོད་ཆགས་ཆེན་པོ་ཡང་གང་ཡིན་ཞེ་ན། མཆོག་ཏུ་དགའ་བས་ཏེ།[^794] དྲི་མ་མེད་པའི་དགའ་བའོ། །

[Block 1502]
དེའི་རྒྱུ་ནི་དེ་འཕེལ་བར་བྱེད་པའི་རྒྱུ་སྟེ་ཁུ་བ་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 1503]
དེ་ལས་བྱུང་བ་ནི་རྒྱུ་དེ་ལས་སྐྱེས་པ་སྟེ། འོད་དཔག་ཏུ་མེད་པའོ། །

[Block 1504]
ངེས་པའི་དོན་དུ་གང་ཡིན་ཞེ་ན་འོད་གསལ་བ་སྟེ་སྟོང་པ་ཉིད་དོ། །

[Block 1505]
དེ་ལས་བྱུང་བ་ནི་སེམས་ཅན་དེ་ལྟ་བུ་གདུལ་བའི༌[^795]དོན་དུ་དེའི་སྐུར་སྤྲུལ་པའོ།[^796] །སོ་སོར་རྟོག་པའི༌[^797]ཡེ་ཤེས་ནི་ཆོས་ཐམས་ཅད་མ་འདྲེས་པར་མཁྱེན་པ་གང་ལ་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1506]
དེ་ལ་ཆགས་པ་ནི་དེ་ཡང་དག་པར་ངེས་པའི་ཚུལ་དུ་འཛིན་པའོ། །

[Block 1507]
འཁོར་བ་མ་ལུས་པར་འཇོམས་པ་ནི་གང་གིས་འཁོར་བ་མ་ལུས་པའི༌[^798]རྟོག་པ་འཇོམས་པའོ། །

[Block 1508]
གཞན་ཡང་དེ་བཞིན་ནོ། །

[Block 1509]
དོན་ཡོད་པ་གྲུབ་པ་ནི༌[^799]ཅིའི་ཕྱིར་ཞེ་ན་བྱ་བ་གྲུབ་པའི་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^800]བསྟན་ཏོ། །

[Block 1510]
འོད་གསལ་བ་ལ་ཅིའི༌[^801]ཕྱིར་ཞེ་ན་མཚན་མ༌[^802]མེད་པའི་འབྲས་བུ་སྟེར་བ་སྟེ་དེ་ལ་དམིགས་པས་དེ་འགྲུབ་པའི༌[^803]ཕྱིར་རོ། །
--- END BLOCKS ---
