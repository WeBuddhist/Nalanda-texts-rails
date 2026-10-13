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
ཆུ་ནི་བཾ་ལས་གྱུར་པས་དཀར་པོ་ཟླུམ་པོ་བུམ་པས་མཚན་པ་སྟེ། ལྷ་ནི་རླུང་ལ་བཤད་ཀྱང་སྔ་མ་བཞིན་ཏེ་སངས་རྒྱས་སྤྱན་ལ་སོགས་པའོ། །

[Block 1297 [HEADING]]
#### རྣམ་པར་ཤེས་པའི་ཁམས་བསྟན་པ། ^1-8-2-0

[Block 1298]
གཞི་འབྱུང་བ་ནམ་མཁའ་རྐྱེན་གྱི་འབྱུང་བ་བཞི་བསྟན་ནས་རྣམ་པར་ཤེས་པའི་ཁམས༌[^627]བསྟན་པའི་ཕྱིར་ཇི་ལྟར་ནི་གཞི་དང་རྐྱེན་དེ་ལྟར་ཡིན་ན། རྒྱུ་ཇི་ལྟར་ཞེས་དྲིས་པའོ། །

[Block 1299]
སྒོམ་པ་པོ་ནི་ཚོགས་གཉིས་ཀྱིས་སྦྱངས་པའི་རྣལ་འབྱོར་པའི་སེམས་སོ། །

[Block 1300]
འབྱུང་བ་ནི་བར་དོར་འཇུག་པའི་རང་བཞིན་ཏེ་ཁྱབ་པའོ། །

[Block 1301 [HEADING]]
#### གཞི་ནམ་མཁའ་བསྟན་པ། ^1-8-1-0

[Block 1302]
ད༌[^628]ནི་གཞི༌[^629]ནམ་མཁའ་བསྟན་པའི་ཕྱིར་ཚིག༌[^630]ཟོར་ཡང་དུ་བསྟན་པར་འདོད་ནས་ཐོག་མ་དང་ཐ་མར་སྦྱར་ཏེ། ཆོས་འབྱུང་ལས་སྐྱེས་ཞེས་པ་ཆོས་འབྱུང་ནི་ནམ་མཁའ་སྟེ། འཛམ་བུའི་གླིང་དང་སྐྱེ་གནས་དང་མཐུན་པའོ། །

[Block 1303]
ལས་སྐྱེས་ནི་ལྔ་པ་ཡིན་ཡང་བདུན་པར་སྦྱར་ཏེ་དེ་ལ་གནས་སོ། །

[Block 1304]
ཡང་སྐྱེ་གནས་སུ་བྱ་བའི་ཚེ་ན་ལྔ་པའི་དོན་ཉིད་དོ། །

[Block 1305]
འཁོར་ལོ་ཉིད་ནི་བསྐྱེད་པའི་ཁང་པ་ཉིད་དོ། །

[Block 1306]
འཕར་མ་གཉིས་དག་ནི་རིམ་པ་སྟེ་ཁྱད་པར་གྱི་མཚན་ཉིད་དོ། །

[Block 1307]
སྐྱོན་མེད་པ་ནི་གྲུ་བཞི་པ་ལ་སོགས་པ་སྟེ་སྤྱིའི་མཚན་ཉིད་བསྟན་པའོ། །

[Block 1308 [HEADING]]
#### བཤད་པ། ^1-8-3-0

[Block 1309]
ད༌[^631]ནི་བཤད་པའི་ཕྱིར། ཟེ་འབྲུ་ལས་ནི་གཅིག་གྱུར༌[^632]ཏེ། །ཞེས་པ་ནི་ལྟེ་བ་ནས་ཟེ་འབྲུ་དང་བཅས་པ་ནི་པདྨའི་ནང་གི་གནྡྷོ་ལི་སྟེ་གཙང་ཁང་ནི་ནང་གི་འཕར་མའོ། །

[Block 1310]
གྲུ་གསུམ་གྱི་ནི་ཕྱི་ནས་བརྗོད། །ཅེས་པ་ནི་གྲུ་གསུམ་ནས་ཚུར་མཚོན་པའི་རྩིག་པ་སྟེ་བསྐོར་བའི་ལྷའི་སྣམ་བུས་སོ། །

[Block 1311]
གནས་ཀྱི་ཁྱད་པར་ནི་ཚིག་རྐང་གཉིས་ཏེ་གདན་རོ་དང་ཉི་མའི་གདན་བཅོ་ལྔའོ། །

[Block 1312 [HEADING]]
#### བརྟེན་པ་ལྷའི་རྣལ་འབྱོར་བསྟན་པ། ^1-8-4-0

[Block 1313]
ད་ནི་བརྟེན་པ་ལྷའི་རྣལ་འབྱོར་བསྟན་པའི་ཕྱིར། དེ་ཡི་སྟེང་དུ་ཟླ་བ་ཡིན། །ཞེས་པ་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་པའི་སེམས་སྣང་བའོ། །

[Block 1314 [VERSE]]
ཟླ་བའི་སྟེང་དུ་ས་བོན་ཉིད། །
ཅེས་པ་ནི་སྒོམ་པ་པོའི་སེམས་ཉིད་དོ། །
ཕྱི་ནས་བདུད་ལས་རྒྱལ་བས་མནན། །
ཞེས་པ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱིའོ། །

[Block 1315]
དེ་དག་ཀྱང༌[^633]གཅིག་ནི་རྒྱུ་ས་བོན་ཧཱུཾ་ཡིག་གཉིས་ནི༌[^634]རྐྱེན་གྱི༌[^635]ཟླ་ཡིན་ནོ། །

[Block 1316]
དེ་གཉིས་འདུས་པ་ལ་དེའི་ཕྱིར་འབྲས་བུ་བདེ་བ་ཆེན་པོ་སྟེ་རྒྱུའི་རྡོ་རྗེ་འཆང་གི་རང་བཞིན་བདག་མེད་པའོ། །

[Block 1317]
གཉིས་ནི་རྐྱེན་གཉིས་སོ། །

[Block 1318 [VERSE]]
འདུས་པ་ནི་རྒྱུ་ས་བོན་བསྐུལ་བའོ། །
དེ་དག་ནི་གཙོ་མོ་བསྐྱེད་པ་མདོར་བསྟན་པའོ། །

[Block 1319]
ད་ནི་འཁོར་བསྟན་པའི་ཕྱིར་ཚིགས་སུ་བཅད་པ་གཅིག་སྟེ། འཁོར་རྣམས་ཀྱང་མངོན་པར་བྱང་ཆུབ་པ་རྣམ་པ་ལྔ་ཡིས་རྐང་ཐོན་དུ་བསྐྱེད་པར་བྱའོ། །

[Block 1320]
སྤྱིར་འཁོར་བསྐྱེད་ལུགས་ལ་གཉིས་ཏེ་བྱང་ཆུབ་སེམས་ཀྱི་ཆ་ལས་བསྐྱེད་པ་དང་། བྱང་ཆུབ་སེམས་ཀྱི་སྣང་བའི་ཚུལ་དུ་བསྐྱེད་པའོ། །

[Block 1321]
འོ་ན་གཙོ་མོ་དང་འཁོར་དུ་མི་འོང་ངོ་ཞེ་ན་རྣམ་པར་དག་པ་བཙན་པར་བྱ་བའི་ཕྱིར་གཙོ༌[^636]འཁོར་དུ་བསྟན་ཏེ། འོག་ནས།

[Block 1322 [VERSE]]
རྣམ་ཤེས་ཕུང་པོའི་རང་བཞིན་གྱིས། །
དེས་ན་བདག་མེད་མ་དབུས་སྐྱེས། །

[Block 1323]
ཞེས་གསུངས་པས་རྣམ་པར་ཤེས་པ་གཙོ་བོ་ཡིན་ནོ། །

[Block 1324]
ད་ནི་གཙོ་མོ་རྒྱས་པར་བསྟན་པའི་ཕྱིར། ཟླ་བ་མེ་ལོང་ལ་སོགས་པ༌[^637]ཚིགས་སུ་བཅད་པ་གཉིས་ཏེ། གདན་དབུས༌[^638]མའི་སྟེང་དུ་གཙོ་མོ༌[^639]མངོན་པར་བྱང་ཆུབ་པ་རྣམ་པ་ལྔས་བསྐྱེད་དེ། ཟླ་བ་མེ་ལོང་ཡེ་ཤེས་ལྡན། །ཞེས་པ་ནི་ཨཱ་ལི་བཅུ་དྲུག་ཉིས་འགྱུར་ལས་བྱུང་བའི་ཟླ་བ་ནི་མེ་ལོང་ལྟ་བུའི་ཡེ་ཤེས་ལས་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 1325]
བདུན་གྱི་བདུན་པ་མཉམ་པ༌[^640]ཉིད་ནི་ཀཱ་ལི་ཡི་གེ་སུམ་ཅུ་རྩ་བཞིའི་སྟེང་དུ་ཌ་ཌྷ་ཡ་ར་ལ་ཝ་དྲུག༌[^641]བསྣན་པས་བཞི་བཅུ་ཐམ་པ་ཉིས་འགྱུར་ལས་བྱུང་བ་ནི་མཉམ་པ་ཉིད་ཀྱི་ཡེ་ཤེས་ལས་མངོན་པར་བྱང་ཆུབ་པ་སྟེ། གསང་སྔགས་ལས་ཉི་མ་ལ་རྟ་བདུན་པའོ་ཞེས་གྲགས་སོ། །

[Block 1326]
རང་ལྷའི་ས་བོན་ཕྱག་མཚན་ནི། །སོ་སོར་རྟོག་པར་བརྗོད་པར་བྱ་བ་ནི་ཟླ༌[^642]ཉི༌[^643]གཉིས་ཀྱི་བར་དུ་ས་བོན་ཧཱུཾ་ཆུད་དེ་དེ་ཞུ་ནས་ཟླ་ཉིའི་སྟེང་དུ་མཚན་མ་རྡོ་རྗེ་ཧཱུཾ་གིས་མཚན་པ་ནི་སོ་སོར་རྟོག་པའི་ཡེ་ཤེས་ལས་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 1327]
ཐམས་ཅད་གཅིག་གྱུར་ནན་ཏན་ནི། ཧཱུཾ་ལས་ལྷ་མོ་རྣམ་པར་སྤྲོ་བསྡུས་ནས་ས་བོན་དང་མཚན་མ་དང་ཉི་མ་དང་ཟླ་བ་ཞུ་བ་ནི་བྱ་བ་ནན་ཏན་གྱི་ཡེ་ཤེས་ལས་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 1328]
རྫོགས་པ་ཆོས་དབྱིངས་དག་པ༌[^644]ནི་རྒྱུའི་རྡོ་རྗེ་འཆང་སྐུ་མདོག་དཀར་པོ་ཞལ་གཅིག་ཕྱག་གཉིས་པའི་རྣམ་པར་བསྐྱེད་པ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ལས་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 1329]
དེ་རྣམས་ལ་རྒྱུ་དང་རྐྱེན་དང་རྣམ་པ་དང་ངོ་བོ་དང་འབྲས་བུ་རྣམས་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 1330 [VERSE]]
མཁས་པས་ཆོ་ག་གསུངས་པ་ཡིས། །
རྣམ་པ་ལྔ་པོ་བསྒོམ་པ་ཉིད། །
ཅེས་པ་ནི་སྔར་གྱི་མཇུག་སྡུད་དོ། །

[Block 1331]
སྐབས་ཁ་ཅིག་ཏུ་ཧེ་རུ་ཀ་རྣམས་ལ་སྦྱར་ཞེས་གསུངས་སོ། །

[Block 1332]
ད་ནི་གཞན་སེལ་བ་བསྟན་པའི་ཕྱིར། ཨཱ་ལི་ཀཱ་ལི་ལ་སོགས་པ་གསུངས་ཏེ།

[Block 1333 [VERSE]]
ཨཱ་ལི་ཀཱ་ལི་ནི་སྔར་གྱི་རྐྱེན་གཉིས་སོ། །
མཉམ་སྦྱོར་བ་ནི་རྒྱུ་ས་བོན་བསྐུལ་བའོ། །

[Block 1334]
རྡོ་རྗེ་སེམས་དཔའ༌[^645]ནི་འབྲས་བུ་བདེ་བ་ཆེན་པོའི་རྒྱུའི་རྡོ་རྗེ་འཆང་བདག་མེད་མའི་རང་བཞིན་དུ་བསྟན་པའོ། །

[Block 1335]
གདན་ཞེས་པ་ནི་རྐྱེན་ཇི་ལྟར་བྱ་ཞེ་ན། ལ་ལ་དག་མ་རྫོགས་པའི་རྡོ་རྗེ་སེམས་དཔར༌[^646]འདོད་དེ། རྡོ་རྗེ་ནི་མཚན་མའོ།[^647] །སེམས་དཔའ་ནི་ས་བོན་ཏེ་གདན་ནི་ཉི་མ་དང་ཟླ་བའོ། །
--- END BLOCKS ---
