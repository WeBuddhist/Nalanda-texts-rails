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
སེམས་ཅན་དུ་སྟོན་པ་ཁོ་ནའི་རྟེན་ཅིང་འབྲེལ་པ་ཆ་གསུམ་གསུངས་པ་ཡང་།

[Block 1297 [VERSE]]
སྔོན་དང་ཕྱི་མཐའ་བར་དག་ལ། །
རྨོངས་པ་རྣམ་པར་བཟློག་ཕྱིར་རོ། །

[Block 1298]
ཇི་ལྟར་སྔོན་གྱི་མཐའ་ལས་བར་མ་འབྱུང་བ་དང་། བར་མ་ལས་ཕྱི་མའི་མཐའ་ཞེས་བྱ་བ་རྨོངས་པ་འདི་རྣམ་པར་བཟློག་པའི་ཕྱིར་ཆ་གསུམ་པ་དང་སེམས་ཅན་དུ་སྟོན་པ་གསུངས་སོ། །

[Block 1299]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དེ་ཡང་འདིར་ཉོན་མོངས་པ་དང་། ལས་དང་། གཞིའི་རང་བཞིན་ཏེ། དེ་ལ། ཉོན་མོངས་གསུམ་མོ། །

[Block 1300]
མ་རིག་པ་དང་། སྲེད་པ་དང་། ལེན་པ༌[^481]རྣམས་སོ། །

[Block 1301]
ལས་གཉིས་སོ། །

[Block 1302]
འདུ་བྱེད་དག་དང་། སྲིད་པའོ། །

[Block 1303]
གཞི་བདུན། ལྷག་མ་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་ཡན་ལག་ནི་གཞིའི་རང་བཞིན་ཡིན་ཏེ། ལས་དང་ཉོན་མོངས་པའི་རྟེན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1304]
ཇི་ལྟར་གཞི་ཡིན་པ། དེ་བཞིན་འབྲས་བུ་ཡིན། ཡན་ལག་བདུན་པོ་ཉིད་འབྲས་བུའོ། །

[Block 1305]
ལྷག་མ་ལྔ་ནི་རྒྱུའོ། །

[Block 1306]
བར་མ་ཁོ་ན་རྒྱུ་དང་འབྲས་བུ་རྒྱས་པར་བཤད་དེ།

[Block 1307 [VERSE]]
གཉིས་ཀྱི་རྒྱུ་འབྲས་མདོར་བསྡུས་པ། །
བར་མའི་རྗེས་སུ་དཔག་པ་ལས། །

[Block 1308]
བར་མ་ཁོ་ན་ལས་སྔོན་གྱི༌[^482]མཐའ་དང་ཕྱི་མའི་མཐའ་དག་གིས་རྒྱུ་དང་འབྲས་བུ་རྒྱས་པར་རྗེས་སུ་དཔག་པར་ནུས་པས་མ་བཤད་དོ། །

[Block 1309]
གལ་ཏེ་ཡང་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཡན་ལག་བཅུ་གཉིས་ཁོ་ན་ཡིན་ན། དེ་ལྟར་ན་གོ་མ༌[^483]རིག་པའི་རྒྱུ་མ་བསྟན་པའི་ཕྱིར་འཁོར་བ་ཐོག་མ་ཅན་དུ་ཡང་འགྱུར་ལ། རྒ་ཤིའི་འབྲས་བུ་མ་བསྟན་པའི་ཕྱིར་མཐའ་དང་ལྡན་པར་འགྱུར་བའམ། ཡང་ན་ནི༌[^484]གཞན་གྱིས་ཁ་བསྐང༌[^485]དགོས་སོ། །

[Block 1310]
དེ་ལ་ཡང༌[^486]གཞན་ཞིག་ཡོད་ན་ནི་ཐུག་པ་མེད་པར་འགྱུར་རོ་ཞེ་ན། ཁ་བསྐང་བར་བྱ་མི་དགོས་ཏེ། འདི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 1311 [VERSE]]
ཉོན་མོངས་པ་ལས་ཉོན་མོངས་དང་། །
བྱ་བ་ཉིད་དོ་དེ་ལས་གཞན།[^487] །
དེ་ལས་གཞི་དང་ཉོན་མོངས་སྐྱེ། །
འདིར་ནི་སྲིད་པའི་ཡན་ལག་ལུགས། །

[Block 1312]
ཞེས་བསྟན་ཟིན་ཏོ། །

[Block 1313]
ཉོན་མོངས་པ་ལས་ཉོན་མོངས་པ་སྐྱེ་སྟེ། སྲིད་པ་ལས་ལེན་པའོ། །

[Block 1314]
ཉོན་མོངས་པ་ལས་ལས་ཏེ། ལེན་པ་ལས་སྲིད་པ་དང་། མ་རིག་པ་ལས་འདུ་བྱེད་རྣམས་སོ། །

[Block 1315]
ལས་ལས་གཞི་སྟེ། འདུ་བྱེད་རྣམས་ལས་རྣམ་པར་ཤེས་པ་དང་། སྲིད་པ་ལས་སྐྱེ་བའོ། །

[Block 1316]
གཞི་ལས་གཞི་སྟེ། རྣམ་པར་ཤེས་པ་ལས་མིང་དང་གཟུགས་ནས། རེག་པ་ནས་ཚོར་བའི་བར་དང་། སྐྱེ་བ་ལས་རྒ་ཤིའོ། །

[Block 1317]
གཞི་ལས་ཉོན་མོངས་པ་སྟེ། ཚོར་བ་ལས་སྲིད་པའོ། །

[Block 1318]
གང་གི་ཕྱིར་སྲིད་པའི་ཡན་ལག་རྣམས་ཀྱི་ལུགས་དེ་ལྟར་རྣམ་པར་གཞག་པ་དེའི་ཕྱིར་མ་རིག་པ་ཉོན་མོངས་པའི་རང་བཞིན་ཡང་གཞིའམ་ཉོན་མོངས་པ་ལས་སྐྱེ་བར་འགྱུར་རོ་ཞེས་བསྟན་པ་ཡིན་ལ། རྒ་ཤི་དང་ཚོར་བ་ལ་ཐུག་པའི་གཞི་ལས་ཀྱང་ཉོན་མོངས་པ༌[^488]འབྱུང་ངོ་ཞེས་བསྟན་པ་ཡིན་པས་ཡང་འདི་ལ་ཁ་བསྐང་བར་བྱ་བ་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 1319]
ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དང་། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི༌[^489]ཆོས་དག་ལ་ཁྱད་པར་ཅི་ཞེ་ན། རེ་ཞིག་བསྟན་བཅོས་ལས་ནི་ཁྱད་པར་ཅུང་ཟད་ཀྱང་མེད་དེ། [^490]གཉིས་ཀ་ཡང་འདུས་བྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཡིན་པར་གསུངས་སོ། །

[Block 1320]
མདོའི་དགོངས་པ་ནི།

[Block 1321 [VERSE]]
འདིར་ནི་འབྱུང་བ་རྒྱུ་ཡིན་ཏེ། །
བྱུང་བ་འབྲས་བུ་ཡིན་པར་འདོད། །

[Block 1322]
ཅེས་གསུངས་ཏེ། རྒྱུར་གྱུར་པའི་ཡན་ལག་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡིན་ཏེ། འདི་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1323]
འབྲས་བུར་གྱུར་པའི་ཡན་ལག་ནི༌[^491]རྟེན་ཅིང་འབྲེལ་བར་བྱུང་བ་སྟེ། དེ་ལྟར་ན་ཡན་ལག་ཐམས་ཅད་ཀྱང་གཉིས་ཀར་གྲུབ་བོ། །

[Block 1324]
ཡང་མ་རིག་པ་ཞེས་བྱ་བའི་དོན་གང་ཞེ་ན།

[Block 1325 [VERSE]]
རིག་པའི༌[^492]མི་མཐུན་ཕྱོགས་ཆོས་གཞན། །
མ་རིག་མི་མཛའ་བརྫུན་སོགས་བཞིན། །
ཇི་ལྟར་མཛའ་བོ་ལས་བཟློག་ན། །

[Block 1326]
དེའི་མི་མཐུན་པའི་ཕྱོགས་སུ་གྱུར་པའི་མི་མཛའ་བ་འགའ་ཞིག་ཡོད་ཀྱི། མཛའ་བོ་ལས་གཞན་པ་གང་ཡིན་པ་ཡང་མ་ཡིན་ལ། མཛའ་བོ་མེད་པ་ཡང་མ་ཡིན་པ་དང་། བདེན་པ་ཞེས་བྱ་བ་ནི་མི་སླུ་བ༌[^493]སྟེ། དེའི་མི་མཐུན་པའི་ཕྱོགས་སུ་གྱུར་པ་དག་ནི་མི་བདེན་པ་ཡིན་པ་དང་། ཆོས་མ་ཡིན་པ་དང་། དོན་མ་ཡིན་པ་དང་། བྱ་བ་མ་ཡིན་པ་ལ་སོགས་པ་ཡང་ཆོས་ལ་སོགས་པའི་མི་མཐུན་པར་གྱུར་པ་དེ་བཞིན་དུ་མ་རིག་པ་ཡང་རིག་པའི་མི་མཐུན་པར་གྱུར་པ་ཆོས་གཞན་ཞིག་ཏུ་བལྟ་བར་བྱའོ། །

[Block 1327]
འདི་ལ་གང་ཞེ་ན། ཀུན་སྦྱོར་སོགས་ཚིག༌[^494]ཕྱིར།

[Block 1328]
མདོ་དག་ལས།

[Block 1329]
མ་རིག་པ་ནི་ཀུན་དུ་སྦྱོར་བ་དང་། འཆིང་བ༌[^495]དང་། ཕྲ་རྒྱས་ལ་སོགས་པ་ཉིད་དུ་གསུངས་ཏེ། མེད་པ་ཙམ་ནི་དེ་ལྟ་བུ༌[^496]ཡིན་པར་འོས་པ༌[^497]ཡང་མ་ཡིན་ནོ། །

[Block 1330]
འོ་ན་ནི་དཔེར་ན་ཆུང་མ་ངན་མ་ལ་ཆུང་མ་མ༌[^498]ཡིན་ཞེས་བྱ་བ་དང་། བུ་ངན་པ༌[^499]ལ་བུ་མ་ཡིན་ཞེས་བྱ་བ་ལྟར་མ་རིག་པ་ཡང་དེ་དང་འདྲའོ། །

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
--- END BLOCKS ---
