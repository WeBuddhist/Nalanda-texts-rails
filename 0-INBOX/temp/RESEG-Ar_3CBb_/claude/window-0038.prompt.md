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

[Block 1336]
བྷ་ནི་སྤྱོད་པའོ། །

[Block 1337]
གེ་ནི་དགོས༌[^707]པའོ། །

[Block 1338]
ཥུ་ནི་མཐོར་བའོ། །

[Block 1339]
བི་ནི་འབྱུང་བའོ། །

[Block 1340]
ཛ་ནི་འཕྲུལ་པའོ། །

[Block 1341]
ཧ་ནི་སྤྱོད་པའོ། །

[Block 1342]
ར་ནི་མེད་པའོ། །

[Block 1343]
འདི་དག་ཀྱང་སྒྲའི་རྣམ་པ་ལ་མ་རྨོངས་པས་གང་གི་དུས་སུ་སྒྲ་གཏན་ལ་ཕབ་ནས་ཕྱིས་དོན་གཞན་དུ་གཏན་ལ་འབེབས༌[^708]པའི་དུས་སུ་གང་གང་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^709]དེ་དེ་ལ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^710]ཀུན་དུ་གཏན་ལ་དབབ་པར་བྱའོ། །

[Block 1344]
འདི་དག་གིས་ནི་སྦས་པའི་དོན་བསྟན་ཏོ། །

[Block 1345]
ཡང་ལུང་གིས༌[^711]བཤད་པ་ཞེས་པ་ནི་མཐར་ཐུག་པའི་དོན་བཤད་པར་འདོད་པས་སོ།[^712] །དེ་ཅིའི་ཕྱིར་ཞེ་ན། གང་གིས་གང་དུ་བརྟག་པར་བྱ་བ་དང་བྲལ་བར་བྱ་བའི་ཕྱིར། རྒྱུད་ནི་འདི་སྐད་བདག་གིས་ཐོས། །ཞེས་པ་ནི་སྤྲོས་པ་ཐམས་ཅད་དང་བྲལ་བའི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 1346]
གསལ་བ་འགའ་ཞིག༌[^713]དུས་ཡིན་ཏེ། །ཞེས་པ་ནི་གང་གིས་གང་ཞིག་ཡོངས་སུ་གསལ་བར་གྱུར་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1347]
རྡོ་རྗེ་གསང་བ་ནི་སེམས་གསུམ་ཉིད་དེ། སློབ་མའི་ལུགས་སུ་འབྱུང་བའོ། །

[Block 1348]
རྡོ་རྗེ་དམ་ཚིག་ནི་གསང་བ་གསུམ་ལུགས་ལས་བཟློག་པ་དང་ལྡན་པ་ཉིད་དེ། ཡེ་ཤེས་ཉིད་དེ་དེ་བཞིན་གཤེགས་པས་ན་ཡེ་ཤེས་དེ་བཞིན་གཤེགས་པའོ། །

[Block 1349]
ཡེ་ཤེས་ཕུན་ཚོགས་བསམ་མི་ཁྱབ། །ཅེས་པ༌[^714]ནི་སངས་རྒྱས་ཀྱི་ཡོན་ཏན་དཔག་ཏུ་མེད་པའོ། །

[Block 1350]
ཡོད་མེད་གཉི་ག༌[^715]ལས་འདས་པ། །ཞེས་པ་ནི་གང་གིས་གང་ཞིག་སྤངས་པར་གྱུར་པ༌[^716]དེའི་ཕྱིར་དེ་ལ་རག་ལས་པར་གྱུར་པའི་ཆོས་དེ་ཡང་ཡོངས་སུ་སྤངས་པའོ། །

[Block 1351]
དེ་ལ་གནས་མེད་གནས་པ་ནི་གནས་དང་གནས་པའི་རྟོག་པ་དང་བྲལ་བའོ། །

[Block 1352]
ནམ་མཁའི་རང་བཞིན་ནི་འདུས་མ་བྱས་པ་སྟེ་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་དོ། །

[Block 1353]
ཐམས་ཅད་མཁྱེན་པ་ནི་སངས་རྒྱས་ཏེ་དེའི་ཡེ་ཤེས་ནི་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་སོ། །

[Block 1354]
དེས་འདི་ཡུལ་དུ་བྱེད་པ་ནི་སྒོམ་པའོ། །

[Block 1355]
བཞུགས་པ་ཞེས་བྱ་བ་ཡང་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། འགྲོ་སྙིང་རྣམ་དག་སྟེ་ཆོས་ཐམས་ཅད་ཀྱི་དེ་བཞིན་ཉིད་ལ་བཞུགས་པ་ནི་གནས་པར་མཛད་པའོ། །

[Block 1356]
དེ་བས་ན༌[^717]བཞུགས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཐ་སྙད་ཐམས་ཅད་ཀྱང་དོན་དམ་པ་ལ་འཇུག་པར་བྱ་བ་ཡིན་གྱི༌[^718]དོན་དམ་པར་བརྗོད་པའི་ཕྱིར་ནི་མ་ཡིན་ནོ་ཞེས་བཤད་དོ། །

[Block 1357]
གཞན་གོང༌[^719]དུ་བཤད་པའོ། །

[Block 1358]
དེ་ལྟར་ཞེས་བྱ་བ་ནི་དེའི་ཕྱིར་ཏེ། འདི་སྐད་ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་གང་གིས་ཇི་ལྟར་ཡོངས་སུ་བསྟན་པའི་ཕྱིར་ཞེས་པའོ། །

[Block 1359]
ཞུགས་པའི༌[^720]ཚིག་ཉིད་ཀྱིས་ཞེས་བྱ་བ་ནི་ཐ་མ་སྨོས་པ་ཉིད་དོ། །

[Block 1360]
རྒྱུད་མ་ལུས་པའི་དགོངས་པ་བསྟན་པ་ནི་རྒྱུད་མ་ལུས་པའི་དོན་བསྟན་པས་ཏེ་འདིས་མཇུག་བསྡུ་བ་བསྟན་ཏོ། །

[Block 1361]
དེའི་འོག་ཏུ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་འདི་ཉིད་ཀྱི་ཡན་ལག་བསྟན་པར་བྱའོ། །

[Block 1362]
འཁོར་ཕུན་སུམ་ཚོགས་པ་ཡང་གྲངས་ཇི་ལྟ་ཙམ་ཞེ་ན། བརྗོད་ཀྱིས༌[^721]མི་ལང་བ༌[^722]ཞེས་བྱའོ། །

[Block 1363]
དེ་བཤད་པ་བགྲང་བ་ལས་འདས་པ་ནི་བགྲང་དུ་མེད་པའོ། །

[Block 1364]
གང་ཞིག་ཀུན་དུ་བསམ་གྱིས་མི་ཁྱབ་པར་གྱུར་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1365]
འོ་ན་ལན་གཉིས་སྨོས་པས་ཅི་ཞིག་བྱེད་ཅེ་ན། གཟུགས༌[^723]དང་ཡོན་ཏན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ་འདི་དག་དཔག་ཏུ་མེད་པའོ། །

[Block 1366]
དེས་ནི༌[^724]བྱེད་ཅེ་ན། གང་གིས་གང་ཞིག་ཀུན་དུ་སྣང་བར་གྱུར་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1367]
གཞན་ནི་གོ་སླའོ། །

[Block 1368]
དེ་ནས་གང་གིས་གང་ཞིག་ཡོངས་སུ་རྫོགས་པར་བསྟན་པ་ནི། གང་གིས་ལྷའི་འཁོར་ལོ་ཡོངས་སུ་རྫོགས་པ་སྟེ་དེ་ཉིད་དོ། །

[Block 1369]
དམ་ཚིག་རྡོ་རྗེ་ཞེས་བྱ་བ་གང་ཞིག་ཡིན་ཞེ་ན་དོན་ཡོད་པར་གྲུབ་པའོ་ཞེས་གང་ཞིག་ཡོངས་སུ་གྲུབ་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1370]
འོ་ན་སྒྲིབ་པ་རྣམ་པར་སེལ་བ་ལ་ཅིའི་ཕྱིར་དམ་ཚིག་རྡོ་རྗེའི་སྒྲར་བརྗོད་ཅེ་ན། འདིར་དེའི་རིགས་དང་ལྡན་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདིར་དོན་ཡོད་གྲུབ་པའི་རིགས་དང་ལྡན་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །
--- END BLOCKS ---
