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
གལ་ཏེ། ཤེས་རབ་ངན་པོའི༌[^500]མིན་ལྟ་ཕྱིར། །སྨད་པའི་ཤེས་རབ་ནི་ཉོན་མོངས་པ་ཅན་ཡིན་ན་དེ་ལྟ་ན་ཡང་ལྟ་བའི་རང་བཞིན་ཡིན་པས་མ་རིག་པར་མི་རུང་ངོ་། །འོ་ན་ནི་གང་ལྟ་བའི་རང་བཞིན་མ་ཡིན་པ་དེ་དེ་ཡིན་པར་འགྱུར་རོ། །

[Block 1332]
དེ་ཡང་ཡིན་པར་མི་འོས་སོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ལྟ་བ་དེ་དང་མཚུངས་ལྡན་ཕྱིར། །གལ་ཏེ་མ་རིག་པ་ཤེས་རབ་ཡིན་པར་འགྱུར་ན། ཤེས་རབ་ཀྱི་རྫས་གཉིས་མཚུངས་པར་མི་ལྡན་པའི་ཕྱིར་ལྟ་བ་དེ་དང་མཚུངས་པར་ལྡན་པར་མི་འགྱུར་རོ། །ཤེས་རབ་ཉོན་མོངས་བསྟན་ཕྱིར་རོ། །ཞེས་བྱ་བ་འདི་ལས་ཀྱང་འགྲུབ་སྟེ། འདོད་ཆགས་ཀྱིས་ཉེ་བར་ཉོན་མོངས་པ༌[^501]ཅན་དུ་གྱུར་པའི་སེམས་ནི་རྣམ་པར་མི་འགྲོལ་ལོ། །

[Block 1333]
མ་རིག་པས་ཉེ་བར་ཉོན་མོངས་པ་ཅན་དུ་གྱུར་པའི་ཤེས་རབ་ནི་རྣམ་པར་མི་འདག་གོ་ཞེས་གསུངས་ཏེ། ཤེས་རབ་དེ་ཉིད་ཤེས་རབ་དེའི་ཉེ་བར་ཉོན་མོངས་པ་ཅན་དུ་ཡང་མི་རིགས་སོ། །

[Block 1334]
ཡང་མིང་དང་གཟུགས་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། གཟུགས་ནི་རྒྱ་ཆེར་བཤད་པ་ཇི་ལྟ་བ་བཞིན་དུའོ། །

[Block 1335 [VERSE]]
མིང་ནི་གཟུགས་ཅན་མིན་ཕུང་པོ། །
ཚོར་བ་ལ་སོགས་པ་བཞིའོ། །
སྐྱེ་མཆེད་དྲུག་ནི་བཤད་ཟིན་ནས། །

[Block 1336]
ད་ནི་རེག་པ་བརྗོད་པར་བྱ་སྟེ། རེག༌[^502]དྲུག །མིག་གི་འདུས་ཏེ་རེག་པ་ནས་ཡིད་ཀྱི་འདུས་ཏེ་རེག་པའི་བར་རོ། །

[Block 1337]
དེ་དག་ཀྱང་། འདུས་ཏེ་བྱུང་བ༌[^503]ཡིན། དབང་པོ་དང་ཡུལ་དང་རྣམ་པར་ཤེས་པ་རྣམས་འདུས་པ་ལས་སྐྱེའོ། །

[Block 1338]
དྲུག་པོ་དེ་དག་ལས།

[Block 1339 [VERSE]]
ལྔ་ནི་ཐོགས་པའི་རེག་པ་ཡིན། །
དྲུག་པ་བླ་དགས་ཚིག་ཅེས་བྱ། །

[Block 1340]
མིག་ལ་སོགས་པའི་རེག་པ་རྣམས་ནི་ཐོགས་པ་དང་བཅས་པའི་དབང་པོ་ལ་བརྟེན་པའི༌[^504]ཕྱིར་ཐོགས་པའི་རེག་པ་རྣམས་སོ། །

[Block 1341]
ཡིད་ཀྱི་འདུས་ཏེ་རེག་པ་ནི་ཚིག་བླ་དགས་ཀྱི་རེག་པ་ཞེས་བྱ་སྟེ།

[Block 1342 [VERSE]]
མིང་བླ་དགས་ལ་དམིགས་པའི་ཕྱིར་རོ། །
ཡང་དེ་ཉིད་གསུམ་དུ་འགྱུར་ཏེ།
རིག་དང་མ་རིག་དང་གཞན་རེག །

[Block 1343]
[^505]དེ་དག་ཀྱང་། དྲི་མེད་ཉོན་མོངས་ཅན་ལྷག་མ། །རིག་པའི་རེག་པ་ནི་ཟག་པ་མེད་པའི་རེག་པའོ། །

[Block 1344]
མ་རིག་པའི་རེག་པ་ནི་ཉོན་མོངས་པ་ཅན་གྱི་རེག་པ་སྟེ། རིག་པ་དང་མ་རིག་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1345]
ལྷག་མ་ནི་གཉིས་ཀ་དང་མཚུངས་པར་མི་ལྡན་པའི་ཕྱིར་རིག་པ་ཡང་མ་ཡིན་མ་རིག་པ་ཡང་མ་ཡིན་པའི་རེག་པའོ། །

[Block 1346]
དེ་ཡང་ནི་དགེ་བ་ཟག་པ་དང་བཅས་པ་དང་། མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའོ། །

[Block 1347]
ཡང་མ་རིག་པའི་རེག་པའི་ཕྱོགས་གཅིག་སྨོས་པས། གནོད་སེམས་རྗེས་སུ་ཆགས་པའི་རེག །གནོད་སེམས༌[^506]རྗེས་སུ་ཆགས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1348]
ཡང་ཐམས་ཅད་བསྡུ་ན། བདེ་བར་མྱོང་འགྱུར་ལ་སོགས་གསུམ། །བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པ་དང་། སྡུག་བསྔལ་མྱོང་བར་འགྱུར་བ་དང་། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ་ཡང༌[^507]མ་ཡིན་པ་ཡང་མྱོང་བར་འགྱུར་བ་སྟེ་རེག་པ་བཤད་ཟིན་ཏོ། །

[Block 1349]
ཚོར་བ་བཤད་པར་བྱ་སྟེ། དེ་ལ་རེག་པ་རྣམ་པ་དྲུག་སྔར་བཤད་ཟིན་པ། དེ་ལས་བྱུང་བའི་ཚོར་བ་དྲུག་མིག་གི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བ་ནས་ཡིད་ཀྱི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་བར་རོ། །

[Block 1350]
དེ་དག་ལས།

[Block 1351]
ལྔ་ནི་ལུས་ཀྱིའོ། །

[Block 1352]
སེམས་ཀྱི་གཞན། ལུས་ཀྱི་ལྔ་སྟེ། དབང་པོ་གཟུགས་ཅན་ལ་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 1353]
སེམས་ཀྱི་ནི་དྲུག་པ་སྟེ།

[Block 1354 [VERSE]]
དེ་སེམས་ཙམ་ལ་བརྟེན་པའི་ཕྱིར་རོ། །
དེ་ཡིད་ཉེ་བར་རྒྱུ་བ་ལས། །
རྣམ་པ་དག་ནི་ཡང་བཅོ་བརྒྱད། །

[Block 1355]
ཡང་སེམས་ལས་བྱུང་བའི་ཚོར་བ་དེ་ཉིད་ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་བཅོ་བརྒྱད་རྣམ་པར་གཞག་པ་ལས་རྣམ་པ་བཅོ་བརྒྱད་དུ་དབྱེའོ། །

[Block 1356]
དེ་ལ་ཡིད་བདེ་བའི་ཉེ་བར་རྒྱུ་བ་དྲུག་དང་། [^508]བཏང་སྙོམས་ཀྱི་ཉེ་བར་རྒྱུ་བ་དྲུག་གོ་ཞེས་བྱ་བ་རྣམ་པ་བཅོ་བརྒྱད་དུ་འགྱུར་རོ། །

[Block 1357]
དེ་དག་ལས་བཅོ་ལྔ་ནི་གཟུགས་ལ་སོགས་པ་ལ་ཉེ་བར་རྒྱུ་བ་ཡིན་ཏེ། གཟུགས་ལ་སོགས་པ་སོ་སོར་ངེས་པ་ལ་དམིགས་པའི་ཕྱིར་མ་འདྲེས་པ་ལ་དམིགས་པ་ཡིན་ནོ། །

[Block 1358]
ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་གསུམ་ནི་རྣམ་པ་གཉིས་ཀ་ཡིན་ནོ། །

[Block 1359]
ཡིད་ཉེ་བར་རྒྱུ་བ་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། ཡིད་ལ་བརྟེན་ནས་ཡིད༌[^509]བདེ་བ་ལ་སོགས་པ་དེ་དག་ཡུལ་ལ་ཉེ་བར་རྒྱུ་བའི་ཕྱིར་རོ་ཞེས་གྲག་གོ། །

[Block 1360]
གཞན་དག་ན་རེ། ཡུལ་དག་ལ་ཉེ་བར་རྒྱུ་བར་བྱེད་པའི་ཕྱིར་ཏེ། ཚོར་བའི་དབང་གིས་ཡིད་ཡུལ་དག་ལ་ཡང་དང་ཡང་དུ་རྣམ་པར་རྒྱུ་བའི་ཕྱིར་རོ། །

[Block 1361]
ཡང་ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་འདི་དག་ལས་དུ་ཞིག་འདོད་པའི་ཁམས་དང་ལྡན་པ་ཡིན། དེ་དག་ལས་ཀྱང་དུ་ཞིག་གི་དམིགས་པ་ཅི་ཞིག་ཡིན། དེ་བཞིན་དུ་གཟུགས་དང་གཟུགས་མེད་པ་དང་ལྡན་པའི་བར་དུ་བརྗོད་པར་བྱའོ་ཞེ་ན། འདོད་ན་ཐམས་ཅད་རང་དམིགས་ཅན། །འདོད་པའི་ཁམས་ན་ནི་བཅོ་བརྒྱད་པོ་ཐམས་ཅད་ཡོད་ལ། དེ་དག་ཐམས་ཅད་ཀྱི་དམིགས་པ་ཡང་དེ་ཡིན་ནོ། །

[Block 1362]
དེ་དག་ཉིད་ཀྱི། སྤྱོད་ཡུལ་གཟུགས་ཅན་བཅུ་གཉིས་སོ། །

[Block 1363]
གཟུགས་ཀྱི་ཁམས་ནི་བཅུ་གཉིས་ཀྱི་དམིགས་པ་ཡིན་ནོ། །

[Block 1364]
དྲི་དང་རོ་ལ་ཉེ་བར་རྒྱུ་བ་དྲུག་མ་གཏོགས་པའོ། །

[Block 1365]
གོང་མ་གསུམ་གྱི། སྤྱོད་ཡུལ་ཞེས་བྱ་བར་སྦྱར་ཏེ། གཟུགས་མེད་པ་ནི་ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་གསུམ་གྱི་དམིགས་པ་ཡིན་ནོ། །

[Block 1366]
འདོད་པ་དང་ལྡན་པ་བཤད་ཟིན་ཏོ། །

[Block 1367]
བསམ་གཏན་ནི། གཉིས་ན༌[^510]བཅུ་གཉིས། ཡིད་མི་བདེ་བའི་ཉེ་བར་རྒྱུ་བ་རྣམས་མ་གཏོགས་སོ། །

[Block 1368]
བཅུ་གཉིས་པོ་དེ་དག་ཀྱང་། འདོད་འགྲོ་རྣམས། འདོད་པའི་ཁམས་ནི་དེ་དག་གི་དམིགས་པའོ། །

[Block 1369]
རང་ལ་དམིགས་བརྒྱད། གཟུགས་ཀྱི་ཁམས་དེ་ཉིད་ནི་དེ་དག་གི་རང་བཞིན་ཡིན་ཏེ། དེ་ནི་ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་བརྒྱད་ཀྱི་དམིགས་པ་ཡིན་ཏེ། དྲི་དང་རོ་ལ་ཉེ་བར་རྒྱུ་བ་བཞི་མ་གཏོགས་སོ། །

[Block 1370]
གཟུགས་མེད་པ་གཉིས་ཀྱིའོ། །
--- END BLOCKS ---
