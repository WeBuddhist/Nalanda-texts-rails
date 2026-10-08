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
[Block 1191]
ལན་བདུན་པ་ནི་སྐྱེ་བ་བདུན་པའི་ཤ་སྟེ་འོག་ནས་དེ་ཉིད་བརྟགས༌[^574]པའི་ཐབས་འཆད་དོ། །

[Block 1192]
བསྒྲུབ་པ༌[^575]ནི་ཡུལ་དང་བསམ་པ་སྦྱོར་བས་གནང་བ་སྟེ། དེ་བསད་པའི་ཤ་སྟེ་བརྟག་པ་ཕྱི་མར་འཆད་དོ། །

[Block 1193]
ལྷན་ཅིག་སྐྱེས་པ་གྲུབ་པ་དེའི་ཚེ་རྒྱལ་མཚན་ནི་ཁམས་དང་བཅས་པ་སྟེ་བྱ་རོག་གི་གདོང་ཅན་ནོ། །

[Block 1194]
མཚོན་བསྣུན་ནི་རིན་ཆེན་ཟེ་འབྲུ་དང་བྱ་རོག་གི་གདོང་ཕྲད་པའོ། །

[Block 1195]
ལན་བདུན་པ་ཡང་བཟའ་བར་བྱ། །ཞེས་པ་ནི་ཟླ་བ་དང་མི་འབྲལ་བར་ཉི་མ་དང༌[^576]ལོངས་སྤྱོད་པའོ། །

[Block 1196]
འབད་པས་སྙིང་རྗེ་བསྐྱེད་པ་ཡིས། །ཞེས་པ་ནི་བླ་མ་ལ་འབད་པའི་མན་ངག་གིས་སོ། །

[Block 1197]
གསད་པར་བྱ་བ་བརྗོད་པ་ཉིད། །ཅེས་པ་ནི་ཉོན་མོངས་པ་དང་རྟོག་པའི་ཚོགས་བཀག་ནས་བདེ་བར་སློང་བའོ། །

[Block 1198 [VERSE]]
སྙིང་རྗེ་མེད་པས་མི་འགྲུབ་པས། །
ཞེས་པ་ནི་མན་ངག་དང་མི་ལྡན་ནའོ། །
དེ་ཕྱིར་སྙིང་རྗེ་བསྐྱེད་པ་ཉིད། །
ཅེས་པ་ནི་མན་ངག་ཉིད་དོ། །

[Block 1199]
ཆོ་གའི་གཙོ་བོ་ནི་ལས་ཀྱི་ཕྱག་རྒྱ་ལུས་ཀྱི༌[^577]འཁྲུལ་འཁོར་དང་། རྩའི་འཁྲུལ་འཁོར་དང་རླུང་གི་འཁྲུལ་འཁོར་ཏེ་མན་ངག་གིས་འགེགས་པ་ནི་དེས་རྟོག་པ་འགེགས་པའོ། །

[Block 1200]
རང་ལུས་ནི་རྒྱལ་མཚན་ཞེས་པ་སྤྱིའོ།[^578] །མཚོན་བསྣུན་ནི་ལྟེ་བ་ནས་ཕར་འོད་ཟེར་གྱིས་བསྲེགས་པས་ལན་བདུན་པ་ནི་མཚོན་པ་ཡང་དང་ཡང་དུ༌[^579]རྩ་གཉིས་ནས་ལམ་མཚོན་པའོ། །

[Block 1201]
འབད་པ་ནི་ལུས་ངག་གིས་སོ།[^580] །སྙིང་རྗེ་ནི་ནང་གི་བསྒོམ་པའོ། །

[Block 1202]
བསད་པ་ནི་རྟོག་པའོ། །

[Block 1203]
སྙིང་རྗེ་མེད་ནི་ནང་གི་ཉམས་མེད་པའོ། །

[Block 1204]
གདུག་པ་ནི་རྟོག་པའོ། །

[Block 1205]
ཆོ་གའི་གཙོ་བོ་ནི་གཏུམ་མོ་སྦར་བའོ། །

[Block 1206]
དབྱེར་མེད་ཕྱག་རྒྱ་ཆེན་པོ་ནི་བརྟེན་པ་ཆོས་ནས་འཇུག་པའི་རྒྱལ་མཚན་ནི་སྣང་བའོ། །

[Block 1207]
མཚོན་བསྣུན་ནི་ཤེས་རབ་ཀྱི་བདག་མེད་པའོ། །

[Block 1208]
ལན་བདུན་པ་ནི༌[^581]སྣང་བ་སྟོང་པ་དབྱེར་མེད་པ༌[^582]ཡང་དང་ཡང་དུ་སྒོམ་པ༌[^583]རང་གི་རྩོལ་བས་སོ། །

[Block 1209 [VERSE]]
སྙིང་རྗེ་ནི་ཐབས་ཏེ་སེམས་ཅན་ལ་བསྐྱེད་པའོ། །
གདུག་པ་གཞུག་པ་ནི་དངོས་པོར་ཞེན་པ༌[^584]སྣང་བའོ། །

[Block 1210]
ཆོ་གའི་གཙོ་བོ་ནི་མན་ངག་གི་སྟོབས་ཀྱིས༌[^585]དངོས་པོའི་ཆོས་ལ་བརྟེན་ནས་རང་ལ་ཆོས་ཉིད་འཆར་བའོ། །

[Block 1211]
བརྟེན་པ་ནང་ནས་འཇུག་པའི༌[^586]རྒྱལ་མཚན་ནི་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པ་གཉུག་མའི་དབང་པོའོ། །

[Block 1212]
མཚོན་བསྣུན་ནི་ཡེ་ཤེས་རང་འབར་བ་སྟེ་དེས་བསྐྱེད་པའི་ཡེ་ཤེས་ཀྱི་དངོས་པོ་མཚན་མ་འཇོམས་པ་སྟེ། གཉིས་པོ་དག་ནི་རྣམ་དཔྱད་ན། གཉིས་མེད་ཡེ་ཤེས་རང་འབར་འགྱུར། །ཞེས་པའོ། །

[Block 1213]
ལན་བདུན་པ་དབང་པོ་རང་སྣང་ངོ་། །ཐམས་ཅད་གདུག་པ༌[^587]གཞུག་པ་ནི་ཡིད་ཀྱི་རྒྱུ་བ་ཀུན་ནོ། །

[Block 1214 [VERSE]]
ཆོ་གའི་གཙོ་བོ་ནི་ཕྱག་རྒྱ་ཆེན་པོའོ། །
དགག་པར་བྱ་བ་ནི་ཡིད་དང་བའི་ཐབས་སོ། །

[Block 1215 [VERSE]]
གླེགས་བམ་ལ་ལར་བསྒྲུབ་པར་བྱ། །
ཞེས་པ་ནི་གཉུག་མའི་དབང་དང་པོའི༌[^588]ཐབས་སོ། །

[Block 1216 [HEADING]]
#### ཡོངས་སུ་རྫོགས་པའི་རིམ་པ་སྤྱིའི་དོན། ^1-7-4-0

[Block 1217]
ད་ནི་ཡོངས་སུ་རྫོགས་པའི་རིམ་པ་སྤྱིའི་དོན༌[^589]དུ་ཤེས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1218 [HEADING]]
##### ལྟ་བ་སྟོན་པ། ^1-7-4-1-0

[Block 1219]
དེ་ལ་འདི་ལྟར་ལྟ་བ་ཉིད། །ཅེས་པ་ནི་ཚིག་རྐང་གཉིས་ཀྱིས༌[^590]ལྟ་བ་སྟོན་པར་ཁས་ལེན་པའོ། །

[Block 1220]
ཉིན་མོ་བཅོམ་ལྡན་རྡོ་རྗེ་ཅན། །ཞེས་བྱ་བ་ནི་ཆོས་ཀུན༌[^591]སྣང་བ་བདེ་བ་ཆེན་པོ་ནི་རྡོ་རྗེ་སེམས་དཔར་བལྟའོ།[^592] །མཚན་མོ་ཤེས་རབ་བརྟག་པར་བྱ། །ཞེས་པ་ནི་ཆོས་ཀུན་སྟོང་པ་བདག་མེད་པའོ། །

[Block 1221]
ཉིན་མོ༌[^593]མཚན་མོས༌[^594]མཚོན་ཏེ། དེའི་མཚམས་ཤེས་པ་ནི་སྣང་བ་དང་སྟོང་པ་དབྱེར་མེད་པ་སྐྱེ་བའོ། །

[Block 1222]
ཡང་ཉིན་མོའི༌[^595]འཆར་བ་སྟེ་དགའ་བ་དང་མཆོག་དགའོ། །

[Block 1223]
མཚན་མོ་སྟེ་དགའ་བྲལ་གྱིས་མཚོན་ནས་མཚམས་སུ་ལྷན་ཅིག་སྐྱེས༌[^596]ཞེས་བྱའོ། །

[Block 1224 [HEADING]]
##### སྤྱོད་པ་བསྟན་པ། ^1-7-4-2-0

[Block 1225]
ད་ནི་སྤྱོད་པ་བསྟན་པའི་ཕྱིར།

[Block 1226 [VERSE]]
མི་བྱ་ཅུང་ཟད་ཡོད་མ་ཡིན། །
ཞེས་པ་ནི་བདག་མེད་པས་ནའོ། །
རྟག་ཏུ་མི་བཟའ་ཡོད་མ་ཡིན། །
ཞེས་པ་བཟའ་བ་ནི་སྤྱོད་པ་སྟེ།

[Block 1227 [VERSE]]
དགའ་བ་དེའི་རྣམ་པ་ཡིན་པས་སོ། །
འདི་ལ་མི་བསམ་ཡོད་མ་ཡིན། །

[Block 1228]
ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པ་ལས་ལོག༌[^597]ན་མེད་པའི་ཕྱིར་རོ། །

[Block 1229]
བཟང་ངན་མི་སྨྲ་གང་ཡང་མེད། །

[Block 1230 [VERSE]]
ཅེས་པ་ནི་དོན་གྱིས་སྟོང་ཞིང་བརྫུན་པའི་ཕྱིར་རོ། །
དེ་ཡང་ཉིན་མོའི་ངོས་ནས་ཐམས་ཅད་བྱ་བའོ། །
--- END BLOCKS ---
