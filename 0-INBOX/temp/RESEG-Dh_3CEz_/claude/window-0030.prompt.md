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
[Block 1051 [VERSE]]
དེ་དག་དང་འདི་དག་ཅི་རིགས་སུ་བསྡུ།
[^485] ཕན་ཚུན་དགོངས་པ་ཤེས་པར་བྱའོ། །

[Block 1052 [HEADING]]
##### ཕྱག་རྒྱ་ཆེན་པོ་ལ་བརྟེན་པ་སྨྱོན་པའི་བརྟུལ་ཞུགས་མཆོག་ཏུ་གསང་བའི་སྤྱོད་པ། ^1-6-1-3-0

[Block 1053]
ད་ནི་སྨྱོན་པའི་བརྟུལ་ཞུགས་ཀྱི་སྤྱོད་པ་བསྟན་པའི་ཕྱིར་ཚིགས་སུ་བཅད་པ་གསུམ་གསུངས་ཏེ། འདི་རྣམ་པ་གཞན་བསྟན་པའི་ཕྱིར། བརྟག་པ་ཕྱི་མ་ལས་བཟའ་བཏུང་ཇི་ལྟར་རྙེད་པ་ལྟར་བཟའ་ཞེས་པ་ལ་སོགས་པ་བསྟན་ཏོ། །

[Block 1054 [VERSE]]
ལུས་ཀྱི་སྦྱིན་པ་བྱིན་ནས་ནི། །
ཞེས་པ་ནི་ལུས་དང་སྲོག་ལ་མི་ལྟའོ། །
ཕྱི་ནས་སྤྱོད་པ་ཡང་དག་སྤྱད། །
ཅེས་པ་ནི་དེ་ལྟ་བུ་དང་ལྡན་པའོ། །

[Block 1055]
ལུས་ཀྱི་སྦྱིན་པ༌[^486]ཇི་ལྟ་བུ་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར་སྐལ་དང་སྐལ་མེད་རྣམ་དཔྱད་ནས། །ཞེས་པ་སྟེ། སྦྱིན་པའི་གནས་ཡིན་པ་དང་མ་ཡིན་པ་སྤྱད་ནས༌[^487]སྦྱིན་པ་བྱེད་པ་དང་མི་བྱེད་པར་རོ། །

[Block 1056]
དེའི་ཕྱིར་སྦྱིན་པ་སྦྱིན་མི་བྱ། །ཞེས་པ་ནི་དེ་ལྟར་བརྟགས་ཤིང་དཔྱད་ནས་སྦྱིན་པར་བྱ་བ་མ་ཡིན་པའོ། །

[Block 1057]
སྤྱོད་པ་ནི་གླུ་དང་ལྡན་པའི་སྙོམས་པར་འཇུག་པ་ཙརྱ་པ་ཡིན་ན། འདིར་ཇི་ལྟར་བྱེད་ཅེ་ན། འདིར་ནི་ཕྱག་རྒྱ་ཆེན་པོ་རང་སྣང་བའི་མན་ངག་གླུ་གར་དང་སྙོམས་འཇུག་ཡོངས་སུ་རྫོགས་པ་སྟེ། དེ་ཡང་བཟའ་བཅའ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཉིས་ཀྱིས་བསྟན་ཏེ། བླ་མ་དམ་པའི་ཞལ་ལས་ཤེས་པར་བྱའོ། །

[Block 1058]
ད་ནི་སྤྱོད་པ་ལ་འཇུག་པའི་ཚུལ་སྤྱིར་ཤེས་པར་བྱ་བའི་ཚུལ། དངོས་གྲུབ་རྙེད་པའི་སློབ་མ་གང་། །ཞེས་པ་ནི་སློབ་མ་གང་གིས་དངོས་གྲུབ་ཐོབ་པའོ། །

[Block 1059]
ཡང་དེ་དང་ངོ་། ། ཡང་དག་ཡེ་ཤེས་སྣང་བའོ།[^488] །

[Block 1060 [VERSE]]
ཞེས་པ་ནི་དེ་ཉིད་དངོས་གྲུབ་ཡིན་པའོ། །
ཡང་ན་དེ་ཡིས་ཀྱང་ངོ་། །

[Block 1061]
མནར་མེད་སྤང༌[^489]བའི་རྒྱུ་ཡི་ཕྱིར། །ཞེས་པ་ནི་ཡོན་ཏན་དེ་ཡིས་མི་བསྐྱོད་པ་སྟེ་བླ་མ་ལས་བྱུང་བ་གཙོ་བོ་ཡིན་པའི་ཕྱིར། འོ་ན་ཇི་ལྟར་བྱ་ཞེ་ན་གོང་མ་ལྟ་བུ་གྲུབ་པས་ཀྱང་བླ་མ་ལ་ཕྱག་བཙལ་བའོ། །

[Block 1062]
ད་ནི་སྤྱོད་པའི་རང་བཞིན་དམ་ཚིག་དང་སྡོམ་པ་བསྟན་པའི་ཕྱིར་ཚིགས་སུ་བཅད་པ་གཉིས་སྟོན་ཏོ། །

[Block 1063]
དེ་ཡང་གོ་རིམས་བཟློག་སྟེ་བསྟན་པ་དང་བཤད་པར་གནས་པའོ། །

[Block 1064]
དེ་ཡང་ཞབས་ཀྱི་ཚིག་རྐང་གཉིས་དང་དམ་ཚིག་སྡོམ་པ་རྣམ་པར་གྲོལ་ཞེས་པ་ནི་དམ་ཚིག་གི་བྱ་བའི་ཚུལ་ལོ། །

[Block 1065 [VERSE]]
སྡོམ་པ་ནི་བསྲུང་བའི་ཚུལ་ནས་སོ། །
རྣལ་འབྱོར་ལྡན་པས་སྤྱོད་པ་བྱེད། །

[Block 1066]
ཅེས་པ་ནི་མི་བྱེད་པ་དང་། སྤྱོད་པ་གཉིས་ཀ་དོན་གཅིག་སྟེ་མཉམ་པའི་དོན་དང་ལྡན་པས་སོ། །

[Block 1067]
དེ་དག་བཤད་པ་ནི། བསླབ་དང་ཆོ་ག་རྣམ་པར་གྲོལ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། སྲོག་གཅོད་པ་སྤོང་བ་དང་། གོས་གསུམ་བརྗེ་བ་དང་། ཁྲུས་བཞི་ལ་སོགས་པ་སྡོམ་པ་མི་བྱེད་པ་དང་སྦྱིན་སྲེག་མཆོད་སྦྱིན་ཞེས་དཀྱིལ་འཁོར་པ་དང་བསམ་གཏན་དང་སྔགས་དང་ཕྱག་རྒྱ་དང་ཕྲིན་ལས༌[^490]སོགས་པ་བྱ་བ་ཐམས་ཅད་ཀྱང་མི་བྱེད་དེ། དེ་དག་ཐམས་ཅད་ཀྱང་རོ་མཉམ་པའི་ཕྱིར་གཉིས་ཀ་མཚུངས་སོ། །

[Block 1068]
ད་ནི་སྤྱོད་པའི་རྣམ་པའི་ཚུལ་སྤྱིར་བསྟན་པའི་ཕྱིར་ངེས་པར་སྔོན་དུ་ཞེས་པ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་གཅིག་གིས་བསྟན་ཏེ། གོ་སླའོ། །

[Block 1069]
དེ་ཡང་བླ་མ་པུ་ལ༌[^491]ཧ་རི་བའི་ལུགས་ཀྱིས་སྨྱོན་པའི་བརྟུལ་ཞུགས་ཆེན་པོའི་རྣམ་པའམ་ངོ་བོ༌[^492]ཡིན་པར་འཆད་དོ། །

[Block 1070]
ད་ནི་སྤྱོད་པའི་རྒྱུ་མཚན༌[^493]སྤྱིར་བསྟན་པའི་ཕྱིར། སེམས་ཅན་ཀུན་གྱི་དོན་གྱི་ཕྱིར། །རྟག་ཏུ་སྙིང་རྗེ་ཞེས་པ་སྟེ་གཞན་གྱི་དོན་དུའོ། །

[Block 1071]
བཏུང་བར་བྱ། རྣལ་འབྱོར་བཏུང་དགའ་ཞེས་པ་ནི་བདག་གི་དོན་དུ་སྟེ། དེ་ཡང་སཾ་བ་ལའི་སྒྲས་ཡང་དག་པའི་རྒྱགས༌[^494]ཞེས་བྱའོ། །

[Block 1072 [VERSE]]
སཾ་ནི་མཉམ་པའམ་ཡང་དག་པའོ། །
བ་ལ་ནི་སྟོབས་ཏེ་བདེ་བའོ། །

[Block 1073]
རྣལ་འབྱོར་བཏུང་བ༌[^495]གཞན་གྱིས་བཟི་བ་མེད་ཅེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པའི་དགའ་བའི་རྒྱགས༌[^496]ཡིན་པས་ཚིམ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1074]
སྤྱོད་པ་འོག་མ་གཉིས་ཀ་ལ་གོང་དུ་བསྟན་པའི་དངོས་པོ༌[^497]བཤད་པ་སྤྱིར་འགྲོ་བ་ནི་གཉིས་ཀ་ལ་སྦྱར་རོ། །

[Block 1075]
སྤྱོད་པའི་ལེའུ་སྟེ་དྲུག་པའོ།། །།

[Block 1076 [HEADING]]
### བདུན་པ་འབྲས་བུའི་ཡོན་ཏན་ནམ་དེའི་ཡན་ལག། ^1-7-0

[Block 1077]
དེ་ནས་ཞེས་པ་ནི་རྗེས་ལ་སྟེ་སྤྱོད་པའི་ཡན་ལག་ཏུའོ། །

[Block 1078]
བརྡ་ནི་ཙྪོ་མ་སྟེ། སྦས་པའི་དོན་སྟོན་པའམ། སཾ་ཁི་ཏ་སྟེ་དོན་ཟུར་གྱིས་སྟོན་པས་ན་ལུས་ཀྱི་བརྡའོ། །

[Block 1079]
ངག་གི་སཾ་གཱི་ཏའམ།

[Block 1080 [VERSE]]
སཾ་ཏི་པ་ཤེ༌[^498]སྟེ་དགོས་པའི་སྐད་དམ་ཚིག་གི་བརྡའོ། །
མི་ལ་ཙ༌[^499]ཀླ་ཀློའི་སྐད་དུ་ཞེས་བྱ་སྟེ།

[Block 1081]
འཇིག་རྟེན་པ་ལ་གསང་བའི་དགོངས་པའོ། །

[Block 1082]
དེ་ཡང་བརྟག་པ་ཕྱི་མ་ལས་སྟོན་ཏོ།[^500] །ལེའུ་བཤད་པར་བྱའོ་ཞེས་པ་ནི་སྡུད་པ་པོ་ཁས་ལེན་པ་སྟེ། བརྡ་དང་དེའི་ཡན་ལག་གནས་ལ་སོགས་པ་ཡང་སྟོན་ཏོ། །

[Block 1083]
ད་ནི་བརྡའི་དགོངས་པ་བསྟན་པའི་ཕྱིར།

[Block 1084 [VERSE]]
གང་གི༌[^501]སྤུན་དང་སྲིང་མོར་ཡང་། །
ཞེས་པ་ནི་རྣལ་འབྱོར་པ་དང་མའོ། །

[Block 1085]
ཐེ་ཚོམ་མེད་པར་ཤེས་པར་བྱ་བ་ནི་ཚོགས་ཀྱི་སྤྱོད་པའི་སྐལ་བ་དང་ལྡན་པར་རོ། །

[Block 1086]
ད་ནི་དབང་གི་བརྡ་ཤེས་པར་བྱ་བའི་ཕྱིར་ཅུང་ཟད་གོ་བསྣུར་ཏེ། གཡོན་གྱི་མཐེ་བོང་བཅངས་པ༌[^502]ལས། །ཞེས་པ་ནི་ཕལ་བ་ལས་ཁྱད༌[^503]དུ་བྱ་བའི་ཕྱིར་གཉིས་ཀས་ཀྱང་ལག་པ་གཡོན་པ་དག་གིས༌[^504]བྱའོ། །

[Block 1087]
མཐེ་བོང་བཅངས་པས་ཕྱག་ཅེས་དྲིས་པ་དང་། ཕྱག་རྒྱའི་ལན་དུ།

[Block 1088]
གཡོན་གྱི་མཐེ་བོང་བཅངས་པ་ལས།

[Block 1089]
བསྙུན་གྱི་ཕྱག་རྒྱར་རྣམ་པར་ཤེས། །ཞེས་བྱའོ། །

[Block 1090]
གང་གིས༌[^505]སོར་མོ་གཅིག་སྟོན་པ། །ཞེས་པ་ནི་སོར་མོ་ཚོགས་པ་གཅིག་པ་སྟེ། བུམ་པའི་དབང་དྲིའི༌[^506]ཕྱག་རྒྱའོ། །
--- END BLOCKS ---
