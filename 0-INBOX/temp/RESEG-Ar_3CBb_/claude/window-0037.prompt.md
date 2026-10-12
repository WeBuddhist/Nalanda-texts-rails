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
[Block 1296]
ཞེས་པ་སྟེ་གང་གི་མཚམས་ལ་སོགས་པར་རང་གི་ཡེ་ཤེས་སྐྱེ་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1297 [VERSE]]
སྣ་ཚོགས་པ་ཡི་ཐ་སྙད་དག །
འཇིག་རྟེན་པས་ནི་ཡོངས་བརྟགས༌[^690]པ། །

[Block 1298]
ཞེས་པ་ནི་བདག་ལ་སོགས་པ་དང་ས་ལ་སོགས་པར༌[^691]བརྟགས་པའོ། །

[Block 1299 [VERSE]]
ལམ་གསུམ་གྱི་ནི་དབྱེ་བ་ཡིས། །
ཡེ་ཤེས་གསུམ་དུ་རབ་ཏུ་འགྱུར། །

[Block 1300]
ཞེས་པ་ནི་གང་གིས་ལམ་གསུམ་ལ་བརྟེན་པས་འགག་པ་དང་སྐྱེ་བར་འགྱུར་ཞེས་པའོ། །

[Block 1301]
སྐྱེ་དང་གནས་དང་ཞེས་བྱ་བའི་དོན་ནི་བཤད་ཟིན་ཏོ། །

[Block 1302]
དགོད༌[^692]དང་རྩེད་མོ་བྱེད་པ་དང་། །ཞེས་བྱ་བ་ལ་སོགས་པ༌[^693]འདི་དག་ཀྱང་སྤྲོས་པ་དང་བཅས་པ་ལ་སོགས་པའི་སྤྱོད་པ་སྟེ་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་སངས་རྒྱས་ཐམས་ཅད་དང་མཉམ་པར་སྦྱོར་བ་ཞེས་པ༌[^694]ལས་ཇི་སྐད་དུ་གསུངས་པ་བཞིན་ནོ། །

[Block 1303]
བདག་བྱིན་བརླབ༌[^695]ཆེན་མ་གཏོགས༌[^696]པ། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་འདི་དག་གི་དོན་ཡང་བདག་བྱིན་གྱིས་བརླབ་པ༌[^697]མེད་ན་ནམ་ཡང་འབྲས་བུ་དམ་པ་མི་འཐོབ༌[^698]ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1304]
གཞན་ཡང་ཨེ། ཞེས་བྱ་བ་ནི་བདག༌[^699]གོ། །

[Block 1305]
བཾ་ནི་བསྐྱེད་པའོ། །

[Block 1306]
མ་ནི་རྩ་བོ། །

[Block 1307]
ཡ་ནི་དང་པོའོ།[^700] །ཤྲུ་ནི་རྩ་བོ། །

[Block 1308]
ཏཾ་ནི་གནས་པའོ། །

[Block 1309]
ཨེ་ནི་འགྲོ་བའོ། །

[Block 1310]
ཀ་ནི་སྐྱེ་བའོ། །

[Block 1311]
སྨིན་ནི་འབྱུང་བའོ། །

[Block 1312]
ས་ནི་དེ་ཉིད་དེ་རིག་པའོ། །

[Block 1313]
མ་ནི་འབྱུང་བའོ། །

[Block 1314]
ཡེ་ནི་སྤོང་བའོ། །

[Block 1315]
བྷ་ནི་འབྱུང་བའོ། །

[Block 1316]
ག་ནི་འགྲོ༌[^701]བའོ། །

[Block 1317]
བཱན་ནི་སྟེར་བའོ། །

[Block 1318]
ས་ནི་བཏབ་པའོ། །

[Block 1319]
རྦ་ནི་རྟག༌[^702]པའོ། །

[Block 1320]
ཏ་ནི་སྟོན་པའོ། །

[Block 1321]
[^703]ཐཱ་ནི་གཞག་པའོ། །

[Block 1322]
ག་ནི་ལྷག་མ་འགོག་པའོ། །

[Block 1323]
ཏ་ནི་འབུལ༌[^704]བའོ། །

[Block 1324]
ཀཱ་ནི་གྱུར་པའོ། །

[Block 1325]
ཡ་ནི་དག་པའོ། །

[Block 1326]
བཱ་ཀ་ནི་སྣང་བའོ། །

[Block 1327]
ཙི་ཏ་ནི་བརྗོད་པའོ། །

[Block 1328]
ཏ་ནི་ཐོབ་པའོ། །

[Block 1329]
ཧྲྀ་ནི་སྤྱོད་པའོ། །

[Block 1330]
ད་ནི་སྟེར་བའོ། །

[Block 1331]
ཡ་ནི་གཞག༌[^705]པའོ། །

[Block 1332]
བ་ནི་གནས་པའོ། །

[Block 1333]
ཛྲེ་ནི་རོལ་པའོ། །

[Block 1334]
ཡོ་ནི་འགྱུར་བའོ། །

[Block 1335]
ཥི་ཏ༌[^706]ནི་མི་འགྱུར་བའོ། །
--- END BLOCKS ---
