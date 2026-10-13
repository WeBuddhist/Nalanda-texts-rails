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

[Block 1231]
མཚན་མོའི་ངོས་ནས་ཅིར་ཡང་བྱར་མེད་པའོ།[^598] །ཇི་ལྟར་བདག་ཉིད་ནི་རང་སྤྱོད་པའི་ཉམས་སོ། །

[Block 1232]
དེ་ལྟར་གཞན་ནི་ཡུལ་རང་ཤུགས་ཀྱིས་བཀག་པའི་ཕྱིར་བྱ་རོག་ལྡིང་ཆགས༌[^599]ལྟ་བུའོ། །

[Block 1233]
དེ་བཞིན་བདག༌[^600]ནི་ཅི་ཞེས་དྲིས་པ་དང་། ང་མཆོག༌[^601]ཉིད་དེ་ལྷན་ཅིག་སྐྱེས་པའི་རོའོ། །

[Block 1234]
དེ་ཡང་གཞན་ཤེས་པས་བསྒྱུར་ན་ང་དང་གཞན་གཉིས་ཀ་ཡང་བདག་དང་འདྲ་བ་དེ་བཞིན་ནོ། །

[Block 1235 [HEADING]]
##### སྤྱོད་པའི་ཕན་ཡོན་སྔགས་དང་ཕྱག་རྒྱ་བསྟན་པ། ^1-7-4-3-0

[Block 1236]
ད༌[^602]ནི་སྤྱོད་པའི་ཕན་ཡོན་སྔགས་དང་ཕྱག་རྒྱ་བསྟན་པའི་ཕྱིར་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་གཉིས་ཏེ་གོ་སླའོ། །

[Block 1237 [HEADING]]
##### བསྒོམ་པ་བསྟན་པ། ^1-7-4-4-0

[Block 1238]
ད་ནི་བསྒོམ་པ་བསྟན་པའི་ཕྱིར་ཤྲཱི་ནི་གཉིས་མེད་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཅིག་སྟེ། ལྷན་ཅིག་སྐྱེས་པའི་ཡེ་ཤེས་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་དང་ལྡན་པ་སྟེ། །ཧེ་ནི་རྒྱུ་སོགས་སྟོང་པ་ཉིད་ཀྱི་སྒོའོ། །

[Block 1239]
རུ་ནི་ཚོགས་དང་བྲལ་བ་ཉིད་མཚན་མ་མེད་པའི་སྒོའོ། །

[Block 1240]
ཀ་ནི་གང་དུའང་མི་གནས་པ་སྨོན་པ་མེད་པའི་སྒོའོ། །

[Block 1241]
བདེ་བ་དང་སྟོང་པ་དབྱེར་མེད་པར་བསྒོམ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1242 [HEADING]]
##### འབྲས་བུ་བསྟན་པ། ^1-7-4-5-0

[Block 1243 [VERSE]]
ད་ནི་འབྲས་བུ་བསྟན་པའི་ཕྱིར། །
རྡོ་རྗེ་ཐོད་པའི་སྦྱོར་བ་ཡིས། །

[Block 1244]
ཞེས་པ་ནི་དགྱེས་པའི་རྡོ་རྗེ་དང་བདག་མེད་པའི་རྣལ་འབྱོར་རོ། །

[Block 1245]
སྐྱེ་བོ་གང་དང་གང་རྣམས་ཀྱིས། །

[Block 1246 [VERSE]]
ཞེས་པ་ནི་སེམས་ཅན་གང་ཡང་རུང་བ་སྟེ།
[^603]གོ་ཀུ་ད་ཧ་ན་ལ་སོགས་སོ། །

[Block 1247]
མཁས་པས་ཤ་ནི་བཟའ་བར་བྱ། །ཞེས་པ༌[^604]ནི་སྦྱང་བ་དང་སྦར་བ་དང༌[^605]རྟོག་པ་ལ་མཁས་པའོ། །

[Block 1248]
སེམས་ཅན་དེ་དག༌[^606]དབང་དུ་འགྱུར། །ཞེས་པ་ནི་གང་འདོད་པ་དབང་དུ་གྱུར་པ་དངོས་ཀྱི་ཡོན་ཏན་ནོ། །

[Block 1249]
བསྐྱེད་པའི་རིམ་པ་ལྟར་བཤད་པའོ། །

[Block 1250]
ཡང་ཤེས་རབ་ལ་བཤད་པ་ན༌[^607]རྡོ་རྗེ་ནི་ཐབས་ཀྱི་གསང་བའི་གནས་སོ། །

[Block 1251]
ཐོད་པ་ནི་ལས་ཀྱི་ཕྱག་རྒྱའི་གསང་བའི་གནས་སོ། །

[Block 1252 [VERSE]]
སྦྱོར་བ་ནི་སྙོམས་པར༌[^608]འཇུག་གོ། །
སྐྱེ་བོ་ནི་པྲི༌[^609]ཏ་ག་ཛ་ནྲ་སྟེ།
སོ་སོ་སྐྱེས་པས་ཤེས་པ་དུ་མའོ། །

[Block 1253]
ཤ་ནི་བ་ལ་སྟེ་སྟོབས་སམ་ནུས་པ་བདེ་བར༌[^610]བརྟགས་པའོ། །

[Block 1254]
མཁས་པ་ནི་བླ་མའི་མན་ངག་ལའོ། །

[Block 1255]
བཟའ་བ་ནི་ལྷན་ཅིག་སྐྱེས་པའི་རིམ་པའི་རོའོ།[^611] །སེམས་ཅན་དབང་དུ་འགྱུར་བ་ནི་སེམས་རང་གི༌[^612]རིག་པས་ཆོས་ཀུན་དབང་ཐོབ་པའོ། །

[Block 1256 [VERSE]]
དེ་དག་གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པའོ། །
ཡང་རྡོ་རྗེ་ནི་སྐྱེ་གནས་སྟོང་པའི་ཆའོ། །

[Block 1257]
ཐོད་པ་ནི་སྤྱི་བོའོ། །

[Block 1258]
སྦྱོར་བ་ནི་འོག་དང་། སྟེང་དུ་ཐིག་ལེ་འོད་ཟེར་གྱི་ཚུལ་དུའོ། །

[Block 1259 [VERSE]]
སོ་སོ་སྐྱེ་བོ་ནི༌[^613]རྣམས་སོ། །
ཤ་ནི་རྟོག་པར་སྨིན་པའོ། །

[Block 1260]
མཁས་པ་ནི་བསད་པ་དང་གསོ་བའི་མན་ངག་ལའོ། །

[Block 1261]
བཟའ་བ་ནི་བདེ་བར་ལོངས་སྤྱོད་པའོ། །

[Block 1262]
སེམས་ཅན་དེ་དེ་ནི་ཡུལ་ལ་སྣང་བའི་ཤེས་པ་ཐ་དད་དོ། །

[Block 1263]
དབང་དུ་འགྱུར་བ་ནི་དེ་རྣམས་བདེ་བར་འདུ་བའོ། །

[Block 1264 [VERSE]]
དེ་ནི་རང་ལུས་ཐབས་ལ་བརྟེན་པའོ། །
རྡོ་རྗེ་ནི་སྟོང་པ་ཉིད་དོ། །
སྲ་ཞིང་བརྟན་ལ་ཁོང་སྟོང་མིན། །
སྟོང་ཉིད་རྡོ་རྗེ་ཞེས་སུ་བརྗོད། །

[Block 1265]
ཅེས་གསུངས་སོ། །
--- END BLOCKS ---
