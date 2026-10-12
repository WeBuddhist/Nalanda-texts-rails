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
[Block 1156]
དེ་ནས་སེམས་དེ་ཉིད་སྐྱེ་མཆེད་ཀྱི་ངོ་བོར་ཡང་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་པའི་ཕྱིར། ཡིད་ཀྱི་སྐྱེ་མཆེད་ཉིད་དང་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ་ཆོས་ལ་དམིགས་པ་དང་། བདག་དང་གཞན་གྱི་ཡུལ་རིག་པ༌[^575]དང་། སྤྱི་དང་བྱེ་བྲག་ལ་སོགས་པ་རིག་པར་བྱེད་པ་ནི་ཡིད་ཀྱི་སྐྱེ་མཆེད་དེ་དུས་གཅིག་པ་ཉིད་དོ། །

[Block 1157]
མིག་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཡུལ་གཅིག་པ་ཉིད་དེ་རང་གི་ཡུལ་ལ་དམིགས་པ་དང་། རང་གི་མཚན་ཉིད་རིག་པ་ལ་སོགས་པའོ། །

[Block 1158]
དེའི་སེམས་ལ་དམིགས་པ་ནི་གནས་པའི་རླུང་ལ་དབང་ཐོབ་ནས་འབྱུང་ངོ་། །གང་གིས་གནས་པ་ནི་གང་ཞིག་གང་དུ་བྱས་པ་དེ་ལ་རག་ལས་པར་འགྱུར་རོ་ཞེས་བསྟན་པའི་ཕྱིར།

[Block 1159 [VERSE]]
གང་ཡང་ཁམས་གསུམ་སེམས་ཅན་རྣམས། །
ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ།
ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་ནོ། །

[Block 1160]
སྲོག་དང་རྩོལ་བ་ནི་སྲོག་དང་རྩོལ་བ༌[^576]སྟེ་རྩ་བ་དང་ཡན་ལག་གི་རླུང་ངོ་། །

[Block 1161]
འདི་ལ་བརྟེན༌[^577]ནས་ཅི་བྱེད་ཅེ་ན། གསང་སྔགས་རྒྱལ་པོ་སྟེ། རྡོ་རྗེ༌[^578]བཟླས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1162]
འདི་དག་ནི་འོག་ནས། །སྣ་ཡི་རྩེ་མོར་ཡུངས་ཀར་བསམ། །ཞེས་བྱ་བ་ལ་སོགས་པས་ཀྱང་སྟོན་ལ། འདི་དག་རྒྱས་པར༌[^579]ནི་བཤད་པའི་རྒྱུད་ལས་གསུངས་ཏེ།

[Block 1163 [VERSE]]
སངས་རྒྱས་ལྔ་ཡི་རིགས་གནས་པ། །
སྣ་རྩེའི་བུ་ག་ལས་བྱུང་ཞིང་། །
རླུང་ལྔ་སྟེང་དུ་ཡང་དག་རྒྱུ། །
ལུས་ལ་རྟག་ཏུ་སྤྱོད་པར་འགྱུར། །

[Block 1164 [VERSE]]
ཀུན་རྫོབ་སྣར་ནི་སྤྱོད་པར་ནི། །
སྒོ་དེ་ལས་ནི་རྣམ་པར་འབྱུང་། །
གཡོན་དང་གཡས་དང་གཉི་ག་དང་། །
དལ་བར་རྒྱུ་དང་རྣམ་པ་བཞི། །

[Block 1165]
ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ་འདི་དག་གིས་རྒྱས་པར་ཤེས་པར་བྱའོ། །

[Block 1166]
འོག་ནས་སོ་སོར་སྡུད་དང་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྐབས་སུ་ཡང་འཆད་པར་འགྱུར་རོ། །

[Block 1167]
མི་ཤེས་བསམ་གཏན་ཀློག་པ་སྤངས། །ཞེས་པ་འདིས༌[^580]ནི་སློང་མོ་ཟ་ཞིང་མི་བཟླས་ཏེ་ཞེས༌[^581]བྱ་བ་ལ་སོགས་པ་བསྟན་ཏོ། །

[Block 1168]
འདིར་ནི་སྒོམ་པའི་རྟེན་དང་ཐབས༌[^582]སྤང་བར་བྱ་བ་ཙམ་ཞིག་དངོས་སུ་བསྟན་ལ། ཡོན་ཏན་དང་ལས་དང་འབྲས་བུ་ཤུགས་ཉིད་ཀྱིས་བསྟན་པས་དེ་ལས་གཞན་གྱི་སྤྲོས་པ་དང་བཅས་པའི་བཤད་པ་ཐམས་ཅད་ནི་ཤུགས་ཀྱིས༌[^583]འདིར་ཤེས་པར་བྱའོ། །

[Block 1169]
རྒྱས་པར་ནི་འོག་ནས་ཤེས་པར་བྱའོ། །

[Block 1170]
དེ་ནས་དགེ་བ་དང་མི་དགེ་བའི་ལས་དང་འབྲས་བུ་སེམས་ལས་འབྱུང་ངོ་ཞེས་བསྟན་པའི་ཕྱིར། འབྱུང་བ་འདི་ལས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ་འབྱུང་བ༌[^584]ནི་སྣང་བ་གསུམ༌[^585]རྐྱེན་དང་བཅས་པའོ། །

[Block 1171]
རང་བཞིན་ནི་བཤད་ཟིན་ཏོ། །

[Block 1172]
དགེ་དང་མི་དགེ་བའི་ལས་ཞེས་པ་ནི་འདི་ལས་དགེ་བ་དང་མི་དགེ་བའི་ལས་བྱུང་ཞེའོ། །

[Block 1173]
དེ་ལས་སྐྱེ་བ་འབྱུང་བ་ཡིན། ཞེས་བྱ་བ་ནི་བཟང་པོ་དང་ངན་པ་དང་འདོད་པ་དང༌[^586]མི་འདོད་པ་ལ་སོགས་པ་འབྱུང་བར་འགྱུར་ཞེས་པའོ། །

[Block 1174]
འདི་དག་རྒྱས་པར་ནི་བཅོམ་ལྡན་འདས་ཀྱིས༌[^587]རྡོ་རྗེ་གཙུག་ཏོར་གྱི་རྒྱུད་ལས་གསུངས་ཏེ་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་གསང་བའི་བདག་པོ་ཉོན་ཅིག །ལུས་ཀྱི་ཉེས་པར་སྤྱོད་པ་ནི་རྣམ་པ་གསུམ་མོ། །

[Block 1175]
ངག་གི་ཉེས་པར་སྤྱོད་པ་ནི་རྣམ་པ་བཞིའོ། །

[Block 1176]
ཡིད་ཀྱི་ཉེས་པར་སྤྱོད་པ་ནི་རྣམ་པ་གསུམ་སྟེ་དེ་དག་གིས་སེམས་ཅན་དམྱལ་བར་ལྟུང་བར་འགྱུར་རོ། །

[Block 1177]
ཕྱག་ན་རྡོ་རྗེས་གསོལ་བ་ལུས་ཀྱི་ཉེས་པར་སྤྱོད་པ་དང་ངག་གི་ཉེས་པར་སྤྱོད་པ་དང་། ཡིད་ཀྱི་ཉེས་པར་སྤྱོད་པ་ནི་དུ་ཞིག་མཆིས།

[Block 1178]
བཅོམ་ལྡན་འདས་ཀྱིས་བཤད་དུ་གསོལ། །བདེ་བར་གཤེགས་པས་བཤད་དུ་གསོལ། །

[Block 1179]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གསང་བའི་བདག་པོ་ཉེས་པར་སྤྱོད་པ་དེ་ཉིད་ནི་ཐ་མལ་པ་རྣམས་ཏེ། དེ་ལ་ཕ་མ་དང་བླ་མར་གྱུར་པ་ལ་སོགས་པ་གསོད་པ་དང་། བརྡེག་པར་སྤྱོད་པ་ནི་ཉེས་པར་སྤྱོད་པ་ལྕི་བའོ། །

[Block 1180]
སྲོག་གཅོད་པ་ལ་སོགས་པ་མི་དགེ་བའི་ལས་ཀྱི་ལམ་རྣམས་ནི་ཉེས་པར་སྤྱོད་པ་ཐ་མལ་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་གསུངས་སོ། །

[Block 1181]
དེ་ནས་ཕུང་པོ་ལྔ་ནི་ཡོངས་སུ་དག་པའི་རིགས་ལྔར་བསྐྱེད་པའི་རིམ་པར་འགྱུར་ལ། དེ་དག་སྒྱུ་མའི་དཔེ་བཅུ་གཉིས་ཀྱིས་ཉེ་བར་མཚོན་པས་སྒྱུ་མ་ལྟ་བུའི་སྐུར་འགྱུར་རོ་ཞེས་བསྟན་པའི་ཕྱིར། འགྲོ་བར་འབྱུང་བའི༌[^588]ཕུང་པོ་ཡང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། །འགྲོ་བར་འབྱུང་བའི༌[^589]ཕུང་པོ་ནི་གཟུགས་ལ་སོགས་པའོ། །

[Block 1182]
སངས་རྒྱས་ལྔ་ཡི་བདག་ཉིད་དེ། །ཞེས་བྱ་བ༌[^590]ནི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་རང་བཞིན་ཏེ། མདོར་ན་ཕུང་པོ་ལྔ་རྣམས་ནི། །ཞེས་བྱ་བ་ལ་སོགས་པས་རྒྱས་པར་བསྟན་ཏོ། །

[Block 1183]
མངོན་པར་བྱང་ཆུབ་པ་རྣམ་པ་ལྔ་ནི་ས་བོན་ཡོངས་སུ་རྫོགས་པར་འདོད་པས་ཟླ་བ་ལ་སོགས་པ་ཡོངས་སུ་སྒྲུབ་པའོ། །

[Block 1184]
མིང་གིས་བསྐུལ་བ་ནི་མིང་གིས་བསྐུལ་བ་སྟེ་རང་གི་རྐྱེན་གྱིས་བསྐུལ་བའོ། །

[Block 1185]
ཡང་ན་མིང་གིས་བསྐུལ་བ་ནི་སེ་གོལ་གྱི་སྒྲས་བསླངས༌[^591]ཏེ་གང་གིས་དེ་ཁོ་ན་ཉིད་གསལ་བ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་བའོ། །

[Block 1186]
དེ་ནས་ས་ལ་སོགས་པ༌[^592]འབྱུང་བ་ལྔ་པོ་འདི་དག་ནི་སྤྱན་མ་ལ་སོགས་པ་ཡུལ་གྱི་རང་བཞིན་ནོ་ཞེས་བསྟན་པར་བྱ་བའི་ཕྱིར། རླུང་དང་མེ་དང་ཆུ་དང་ས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ་ཕྱི་དང་ནང་གི་སྲ་བའི་དངོས་པོར་གྱུར་པ་དང་། རྟེན་པར་བྱེད་པའི་ས་ནི་སྤྱན་མའི་རང་བཞིན་ནོ། །

[Block 1187]
གཤེར་བ་དང་སྡུད་པར་བྱེད་པའི་ཆུ་ནི་མཱ་མ་ཀཱིའི་རང་བཞིན་ནོ། །

[Block 1188]
ཚ་བ་དང་སྨིན་པར་བྱེད་པའི་རང་བཞིན་མེ་ནི་གོས་དཀར་མོའི་རང་བཞིན་ནོ། །

[Block 1189]
ཡང་ཞིང་གཡོ་བའི་རླུང་ནི་སྒྲོལ་མའི་རང་བཞིན་ནོ། །

[Block 1190]
ཡེ་ཤེས་བདག་ཉིད་སྤྱན༌[^593]གསུམ་ནི། གང་ལ་གང་དུ་ཇི་ལྟར་གནས་པ་དེ་དང་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 1191]
ལྷག་མས་ནི་ཡོན་ཏན་བསྟན་པ་ཉིད་དོ། །

[Block 1192]
དེ་ནས་སྐུ་དང་གསུང་དང་ཐུགས་བྱིན་གྱིས་བརླབ་པ་བསྟན་པར་བྱའོ་ཞེས་བྱ་བ་འབྱུང་བས་དེ་བཤད་པའི་ཕྱིར། ཐམས་ཅད་དེ་བཞིན་གཤེགས་པའི་ལུས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པ་སྟེ། དེའི་ལུས་ཇི་ལྟར་བྱ་ཞེ་ན། ཕྱག་རྒྱ་བཞིས༌[^594]ནི་རྒྱས་བཏབ་ཅིང་། །ཞེས་བྱ་བ་ནི་ཆོས་དང་ལས་དང་དམ་ཚིག་དང་ཕྱག་རྒྱ་ཆེན་པོས་ཐོབ་པར༌[^595]བྱ་བའོ། །

[Block 1193]
མིག་ལ་སོགས་པའི་བདག་ཉིད་དེར། །ཞེས་བྱ་བ༌[^596]ནི་མིག་དང་རྣ་བ་ལ་སོགས་པའི་ནང་ལ་སོགས་པའོ། །

[Block 1194]
ཅི་བྱ་ཞེ་ན་ས་སྙིང་ལ་སོགས་རབ་ཏུ་བརྟག །ཅེས་པ༌[^597]སྟེ་མིག་ལ་སོགས་པར་སའི་སྙིང་པོ་ལ་སོགས་པ་བསྒོམ་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1195]
དེ་ནས་བདུད་ཐམས་ཅད་དང་བར་དུ་གཅོད་པ་ཐམས་ཅད་སྤང་བར་བྱ་བའི་ཕྱིར་ལུས་འདི་ནི་ཁྲོ་བོ་བདུད་ཐམས་ཅད་ངེས་པར་འཇོམས་པའོ་ཞེས་བསྟན་པར་འགྱུར་བས་རོལ་བའི་དགའ་བ་ནི་རོལ་པའི་དགའ་བ་སྟེ་སྙོམས་པར་འཇུག་པའི༌[^598]བདག་ཉིད་ཅན་ནོ། །
--- END BLOCKS ---
