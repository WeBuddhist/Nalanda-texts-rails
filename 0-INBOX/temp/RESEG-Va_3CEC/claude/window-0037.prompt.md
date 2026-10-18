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
རྒྱུ་དང་འབྲས་བུ་མི་མཐུན་པར་ཤེས་པ་བཤད་ཟིན་ཏོ། །

[Block 1297 [HEADING]]
#### གཉིས་ཀའི་ཆ་ལ་ཉོན་མོངས་པ་མེད་པ། ^3-2-6-0

[Block 1298]
འཕགས་པའི་སྒྲ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་། དེ་བཞིན་གཤེགས་པ་རྣམས་གསུངས་པ་དང་། ཆོས་འཆད་པའི་སྒྲའོ། །

[Block 1299]
འཕགས་པ་མ་ཡིན་པའི་སྒྲ་ནི་སོ་སོའི་སྐྱེ་བོ་རྣམས་འོང་བ༌[^1099]དང་འགྲོ་བ་ལ་སོགས་པ་ཐ་སྙད་སྣ་ཚོགས་ཀྱི་སྒྲ་འབྱིན་པའོ།[^1100] །འཕགས་པའི་སྒྲ་ལ་བྱམས་པ་ཆེན་པོ་འཐོབ་ཅིང་ཞེས་བྱ་བ་ནི་འཕགས་པ་རྣམས་ཀྱི་སྒྲ་ཐོས་ནས་ཆོས་བཤད་པའི་སྒྲ་འདིས་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་བཏགས་སོ་ཞེས་སྒྲ་དེ་ལ་བདག་ཉིད་བྱམས་པ་ཆེན་པོའི་སེམས་བསྐྱེད༌[^1101]པའོ། །

[Block 1300]
འཕགས་པ་མ་ཡིན་པའི་སྒྲ་ལ་སྙིང་རྗེ་ཆེན་པོ་འཐོབ་ཅེས་བྱ་བ་ནི་སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱི་སྨྲ་བའི༌[^1102]སྒྲ་ནི་འདོད་ཆགས་དང་ཞེ་སྡང་ལ་སོགས་པའི་རྒྱུ་ལས་བྱུང་བས་ན་སྡུག་བསྔལ་སྣ་ཚོགས་བསྐྱེད༌[^1103]པའི་རྒྱུ༌[^1104]ཡིན་ནོ་ཞེས་སྙིང་རྗེ་ཆེན་པོའི་སེམས་སྐྱེའོ། །

[Block 1301]
གཉི་གའི་ཆ་ལ་ཉོན་མོངས་པ་མེད་པ་བཤད་ཟིན་ཏོ། །

[Block 1302 [HEADING]]
#### དུས་གསུམ་མ་འདྲེས་པ་ཤེས་པ། ^3-2-7-0

[Block 1303]
སྒྲ་ཐམས་ཅད་ལ་ཡང་སྔོན་གྱི་མཐའ་དང་ཕྱི་མའི་མཐའ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི༌[^1105]འདས་པའི་སྒྲ་དང་མ་འོངས་པའི་སྒྲ་གང་ཡིན་པ་བྱེ་བྲག་ཕྱེད་པར་ཤེས་པ་ནི་སྔོན་གྱི་མཐའ་དང་ཕྱི་མའི་བར་བྱེ་བྲག་འབྱེད་པ༌[^1106]ཤེས་པ་ཞེས་བྱ་སྟེ། ཤེས་པ་དེས་སྒྲ་འདི་དག་ནི་འདས་པའི་ཚིག་ཡིན་ནོ་ཞེས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་སོ། །

[Block 1304]
དེ་ལྟར་དུས་གཉིས་ཀྱི་སྒྲ་བྱེ་བྲག་ཕྱེད་པར་ཤེས་ན། ད་ལྟར་བྱུང་བའི་དུས་ཀྱི༌[^1107]ཚིག་ཀྱང་ཤེས་པར་མངོན་པའི༌[^1108]ཕྱིར་མདོ་ལས་མ་གསུངས་ཏེ། དུས་གསུམ་འདྲེས་པ་བཤད་ཟིན་ཏོ། །

[Block 1305 [HEADING]]
#### ལས། ^3-2-8-0

[Block 1306]
དྲན་པ་ནི་ཐོས་པའི་ཆོས་རྣམས་ཀྱི་ཚིག་དང་དོན་མ་བརྗེད་པའོ། །ཤེས་བཞིན་ནི་ཆོས་དེ་རྣམས་ཀྱི་རང་དང་སྤྱིའི་མཚན་ཉིད་བྱེ་བྲག་ཕྱེད་པའོ། །

[Block 1307]
དེ་གཉིས་མི་བརྗེད་པ་དང་བྱེ་བྲག་ཕྱེད་པར་བྱེད་པས་ན་དྲན་པ་དང་ཤེས་བཞིན་གཉིས་ལ་མི་བརྗེད་པའི་ཆོས་ཉིད་ཅེས་བྱའོ། །

[Block 1308]
སེམས་ཅན་རྣམས་ལ་དྲན་པར་བྱེད་ཅེས་བྱ་བ་ནི་ཐོས་པའི་ཆོས་དེ་དག་སེམས་ཅན་ལ་སྟོན་ཅིང་སེམས་ཅན་རྣམས་ཀྱང་མི་བརྗེད་པའི་ཆོས་ཉིད་ལ་འཇོག་པར་བྱེད་པའོ་ཞེས༌[^1109]བྱ་བའི་དོན་ཏོ། །

[Block 1309]
སྙིང་པོ་དང་སྙིང་པོ་མ་ཡིན་པའི་ཆོས་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། དོན་དམ་པ་བསྟན་པའི་ཆོས་རྣམས་ནི་སྙིང་པོའི་ཆོས་སོ། །

[Block 1310]
ཀུན་རྫོབ་ཏུ་ཆོས་བསྟན་པ་ཐམས་ཅད་ནི་སྙིང་པོ་མ་ཡིན་པའི་ཆོས་ཏེ། སེམས་ཅན་རྣམས་མི་བརྗེད་པའི་ཆོས་ཉིད་ལ་བཀོད་པས། སྙིང་པོ་དང་སྙིང་པོ་མ་ཡིན་པའི་ཆོས་རྣམས་ཀྱང་སེམས་ཅན་དེ་དག་གིས་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1311]
གང་དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན༌[^1110]པའི་སྒྲ་གང་དག་ཐོས་པ་དེ་དག་ཀྱང་དྲན་པ་དང་ཤེས་བཞིན་གྱིས་དུས་དུས་སུ་བརྗོད་དོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེ་སྔོན་གཞན་ལས་དགེ་བའི་སྒྲ་ཐོས་པ་དང་། མི་དགེ་བའི་སྒྲ་ཐོས་པ་དང་། ལུང་དུ་མ་བསྟན་པའི་སྒྲ་ཐོས་པ་རྣམས་ཀྱང་སྨྲ་བར་བྱ་བའི་སྣོད་དང་དུས་སུ་སྦྱར་ཏེ་སྒྲའོ༌[^1111]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1312]
སྣོད་དང་སྦྱར་བ་ནི་གལ་ཏེ་སེམས་ཅན་དེ་དག་ཆོས་བཤད་པའི་སྣོད་ཡིན་ན་ནི་སྨྲའི། [^1112]མ་ཡིན་ན་ནི༌[^1113]མི་སྨྲའོ། །

[Block 1313]
དུས་སུ་སྦྱར་བ་ནི་ཆོས་བཤད་པའི་དུས༌[^1114]ལ་བབ་ན་ནི༌[^1115]སྨྲའི། དུས༌[^1116]ལ་མ་བབ་ན་ནི༌[^1117]མི་སྨྲའོ། །

[Block 1314]
དེ་ཉིད་ཀྱི་དོན་གལ་ཏེ་འཁོར་གྱི་དུས་ཡིན་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིག་འོག་མ་རྣམས་ཀྱིས་གསལ་བར་བཤད་དེ། འཁོར་རྣམས་ཚོགས་སུ་ཟིན་ཀྱང་ཆོས་བཤད་པའི་དུས་དང་སྐབས་སུ་མ་བབ་ན་ཆོས་ཐོས་པ་རྣམས་ཀྱང་མི་སྟོན་པར་འཇོག་གོ། །

[Block 1315]
ཆོས་བསྟན་པའི་དུས་ལ་བབ་ན་ནི་འཁོར་མང་པོ་མ་ཚོགས་ཀྱང་གདུལ་བྱ་འགའ་ཙམ་ལ་ཡང་ཆོས་སྟོན་ཏོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1316]
དབང་གཅིག་གིས་ཞེས་བྱ་བ་ནི་ཕ་རོལ་པོ་ཉན་པ་གཅིག་པུ་ཞིག་ཡོད་ཀྱང་རུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1317]
བདེན་པར་ལུང་བསྟན་པ་ཡང་གཞན་ལ་གནོད་ན་ལུང་མི་སྟོན་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། བྱང་ཆུབ་སེམས་དཔའ་དགེ་བ་དང་མི་དགེ་བ་ལ་སོགས་པའི་དངོས་པོའི༌[^1118]སྒྲའི་སྒོ་ནས་ཐོས་ཏེ་ལུང་བསྟན་དུ་ཡོད་ཀྱང་སེམས་ཅན་ལ་གནོད་ན་བདེན་ཞིང་ཐོག་ཏུ་བབ་ཀྱང་ལུང་མི་སྟོན་ལ། སེམས་ཅན་ལ་ཕན་ན་མི་བདེན་ཞིང་ཐོག་ཏུ་མ་བབ་ཀྱང་ལུང་སྟོན་ཏེ། ཐབས་མཁས་པ་དང་། བདག་གི་སེམས་ལ་གཡོ་མེད་པའི་སྒོ་ནས་ཡོངས་སུ་དག་པའི་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱ་བ་དང་མི་འགལ་བའི་ཕྱིར་བརྫུན་དུ་སྨྲ་བར་ཡང་མི་འགྱུར་རོ། །

[Block 1318]
སྒྲ་ཇི་ལྟ་བུ་ཉན་པར་འདོད་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི༌[^1119]ཆོས་ཉན་པའི་སེམས་ཅན་རྣམས་ཀྱང་ཆོས་གང་དང་སྒྲ་ཇི་ལྟ་བུ་ཉན་ཅིང་ཐོས་པར༌[^1120]འདོད་པའི་ཆོས་དེ་དང་སྒྲ་དེ་ལྟ་བུ་ཐོས་ཀྱི༌[^1121]སྒྲ་གང་དང་ཆོས་ཉན་པར་མི་འདོད་པའི་སྒྲ་དེ་དང་ཆོས་དེ་ནི་མི་ཐོས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1319]
འཁོར་གང་ན་ཆོས་སྟོན་པ་དེའི་སེམས་ཅན་རྣམས་ཀྱི་རྣ་བའི་གནས་ཀྱི་ཤེས་པ་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་འཁོར༌[^1122]ན་ཆོས་ཉན་པའི་སེམས་ཅན་རྣམས་ཀྱི་རྣ་བའི་དབང་པོས༌[^1123]ཆོས་ཐོས་ནས་གང་ལ་དད་ཅིང་མོས་པའམ། ཅི་དང་ཅིའི་སྣོད་དུ་འགྱུར་བ་ཤེས་ན་དེ་དག་དང་རྗེས་སུ་མཐུན་པའི་ཆོས་རྣམས་སྟོན་ཏེ།[^1124] དེ་ལ་སེམས་ཅན་གང་དག་ཆོས་ཤེས་པར་བྱེད་པ་དེ་དག་གིས་ནི༌[^1125]དེའི་ཆོས་ཐོས་སོ་ཞེས་བྱ་བ་ལ། སྒྲ་ཕར་སྨྲ་བ་ལ་དབང་དུ་གྱུར་པ་སྟོན་ཏོ། །

[Block 1320]
བྱང་ཆུབ་སེམས་དཔའ་དེས་འཁོར་གཅིག་གི་ནང་དུ་ཆོས་བཤད་པ་ལས།

[Block 1321]
འཁོར་དེ་དག་གི་ནང་ན་གང་ཆོས་དེའི་སྣོད་དུ་གྱུར་པའི་ཤེས་པར་ནུས་པ་རྣམས་ལ་ནི་ཆོས་འཆད་པའི་སྒྲ་དེ་དག་གྲག་པར༌[^1126]འགྱུར་གྱི། སྣོད་མ་ཡིན་ཞིང་ཕན་པར་མི་འགྱུར་བ་ལ་ནི་སྒྲ་ཡང་གྲག་པར༌[^1127]མི་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1322]
ལས་བཤད་ཟིན་ཏོ། །

[Block 1323 [HEADING]]
#### རྒྱུ། ^3-2-9-0

[Block 1324]
དེ་དག་ནི་རྣ་བའི་ཁམས་དེ་ཆོས་ཀྱི་དབྱིངས་ཤིན་ཏུ་རྣམ་པར་དག་པ༌[^1128]ཡིན་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་དབྱིངས་ཤིན་ཏུ་རྣམ་པར་དག་པ་བསྒོམས་པ༌[^1129]ལས་བྱུང་བས་ན་ཆོས་ཀྱི་དབྱིངས་ཤིན་ཏུ༌[^1130]རྣམ་པར་དག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1325]
དེ་དག་གི་རྣ་བའི་ཁམས་དེ་ཡེ་ཤེས་རྣམ་པར་དག་པ་ཡིན་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་རྣམ་པར་དག་པ་ལ་དམིགས་ཤིང་བསྒོམས་པ་ལས་བྱུང་བས་ན་རྣམ༌[^1131]པར་མི་རྟོག་པའི་ཡེ་ཤེས་རྣམ་པར་དག་པ་བཞིན་དུ་དེའི་རྣ་བའི་ཁམས་ཀྱིས༌[^1132]རང་བཞིན་ཡང་དག་པ་ཡིན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1326]
དེ་དག་གི་རྣ་བའི་ཁམས་དེ་བདག་གི་ཁམས་ཤིན་ཏུ་རྣམ་པར་དག་པ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་མུ་སྟེགས་ཅན་གྱིས་བརྟགས་པའི་བདག་དང་སེམས་ཅན་ལ་སོགས་པ་མིང་གིས་སྨོས་ཀྱི་ལྟ་བ་དང་བྲལ་བས་རྣམ་པར་དག་པ་ཞེས་བྱའོ། །

[Block 1327]
དེ་དག་གི་རྣ་བའི་ཁམས་དེ་སྒྲ་དང་ཡི་གེ་དང་ངེས་པའི་ཚིག་ཇི་ལྟ་བ་བཞིན་དུ་ཐོས་པ་ཤིན་ཏུ་བརྟགས་ཞེས་བྱ་བ་ནི་སྒྲ་དང་ཡི་གེ་ལ་སོགས་པ་ཕྱིན་ཅི་མ་ལོག་པར་ཐོས་པས༌[^1133]དེ་དག་གི་མཚན་ཉིད་ཁོང་དུ་ཆུད་པ་ལས་སྐྱེས་པ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1328]
དེ་ལ་སྒྲ་ནི་གདངས༌[^1134]སོ། །

[Block 1329]
ཡི་གེ་ཨ་དང་ཀ་ལ་སོགས་པའོ། །

[Block 1330]
ངེས་པའི་ཚིག༌[^1135]ནི་གཏན་ལ་འབེབས་པའི་ཚིག་སྟེ།[^1136] ཐོགས་པ་དང་བཅས་པས་ན་གཟུགས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1331]
སྐད་ཇི་ལྟ་བ་བཞིན་དུ་འཇུག་པས་ཆོས་སྟོན་ཅེས་བྱ་བ་ནི་སོ་སོའི་སྒྲ་དང་སྐད་ལ་སོགས་པ་དང་མཐུན་པར་བྱས་ནས་ཆོས་སྟོན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1332]
ཐེག་པ་གཞན་མི་ཉན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ཐེག་པ་མི་ཉན་ཞིང་དེར་མི་བསྔོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1333]
ལྷའི་རྣ་བ་མངོན་པར་ཤེས་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ། །

[Block 1334 [HEADING]]
### སེམས་མངོན་སུམ་པ། ^3-3-0

[Block 1335]
སེམས་མངོན་སུམ་པ་བསྟན་པའི་ཕྱིར། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཕ་རོལ་གྱི་སེམས་ཤེས་པའི་མངོན་པར་ཤེས་པ་མི་ཟད་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །
--- END BLOCKS ---
