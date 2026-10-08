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

[Block 1091]
གཉིས་ཀྱིས་ལེགས་པར་འོངས་པ་ཡིན། །ཞེས་པ་ནི་དེ་ལྟ་མོད་ཀྱིས༌[^507]གསང་བའི་དབང་ལ་ཡང་རེག་པ་ཡིན་ཞེས་པའི་ཕྱག་རྒྱའི་ལན་ནོ། །

[Block 1092]
ཡང་ཅུང་ཟད་གོ་བསྣུར་ཏེ། གང་གི་སྲིན་ལག་སྟོན་པ་ལ། །ཞེས་པ་ནི་མཐེ་བོང་དང་བཅས་པ་སྟེ། གསང་བའི་དབང་དྲིས་པའོ། །

[Block 1093 [VERSE]]
དེ་ཡིས་མགྲིན༌[^508]པ་རབ་ཏུ་བསྟན། །
ཞེས་པ་ནི་ལོངས་སྤྱོད་པ་སྟེ།
གསང་བའི་དབང་ཐོབ་པའི་ལེན༌[^509]ནོ། །
གང་ཞིག་སྲིན་ལག་སྟེར་བ་ལ། །

[Block 1094]
ཞེས་པ་ནི་ཤེས་རབ་ཡེ་ཤེས་དྲིས་པའོ། །

[Block 1095]
སོར་མོ་གསུམ་པས། དབང་གསུམ་བརྡ་ཡིས་བསྟན་པའོ། །

[Block 1096]
དེ་ཡི་མཐེའུ་ཆུང་རྣམ་པར་སྨིན།[^510] །ཞེས་པ་ནི་དེ་ལྟ་མོད་ཀྱི་བཞི་པ་ལ་རེག་གོ་ཞེས་བྱ་བའི་དོན་ནོ། །

[Block 1097]
གང་གིས༌[^511]གུང་མོ་སྟོན་པ་ལ། །ཞེས་པ་ནི་བཞི་པའི་དོན་དབུ་མ་དྲིས་པའོ། །

[Block 1098]
དེ་ཡི་མཛུབ་མོ་རྣམ་པར་སྨིན།[^512] ། ཞེས་པ་ཚིག་དབང་རིན་པོ་ཆེ་ཉེ་བར་དགྲོལ༌[^513]ལོ། །ཞེས་པའི་ལན་ནོ། །

[Block 1099 [VERSE]]
ད་ནི་རྩའི་མན་ངག་བསྟན་པའི་ཕྱིར། །
གང་གིས༌[^514]སོ་ནི་སྟོན་པ་ལ། །

[Block 1100]
ཞེས་པ་ནི་བདེ་བ་ཆེན་པོའི་འཁོར་ལོའི་རྩའི་དབྱིབས་བ་ཏི་སྟེ།

[Block 1101 [VERSE]]
[^515] ཐོད་ལྟ་བུར་གནས་པ་དྲིས་པའོ། །
དེ་ཡིས་རྩེ་གསུམ་རྣམ་པར་བསྟན། །

[Block 1102]
ཞེས་པ་ནི་དེ་ཡང་རྩ་གསུམ་ལས་གྱུར་པ་དང་རྩ་གསུམ་ལས་འབེབས༌[^516]པའི་ལན་ནོ། །

[Block 1103]
རྩ་ལ་བརྟེན་པའི་བྱང་ཆུབ་སེམས་ཇི་ལྟ་བུ་ཞེས་པ་ནི་ཀུན་རྫོབ་ལྷན་ཅིག་སྐྱེས་པའི་མན་ངག་བསྟན་པའི་ཕྱིར། གང་ཞིག་ནུ་མ་སྟོན་པ་ལ། །ཞེས་པ་ནི་ཀུནྡ་ལྟ་བུ་གང་ན་གནས་ཞེས་དྲིས་པ་ལ། དེ་ཡིས་མཚམས་ནི་རབ་ཏུ་བསྟན། །ཞེས་པ་སྟེ་མཚམས་ནི་སིམ་སྟེ་སིར་ཞེས་པས་མཚོག༌[^517]མ་ན་གནས་ཞེས་པའི་དོན་ཏོ། །

[Block 1104]
གང་ཞིག་ས་ནི་སྟོན་པ་ལ། །ཞེས་པ་ནི་ཀུནྡ་སྐྱེས་པའི་ཤེས་རབ་མ་དྲིས་པའོ། །

[Block 1105 [VERSE]]
དེ་ཡིས་ཁ་ནི་རབ་ཏུ་བསྟན། །
ཞེས་པ་ནི་ཉེ་བའི༌[^518]ལོངས་སྤྱོད་ཅེས་པའོ། །

[Block 1106]
གླེགས་བམ་ལ་ལར་འཁོར་ལོ་བསྟན་པ་ནི་ཤེས་རབ་མལ་སྤྱི་བོས་བཏུད་པའོ། །

[Block 1107]
གང་གིས་ཁྲོ་གཉེར་བསྟན་པ་ལ། །ཞེས་པ་ནི་འདོད་ཆགས་ཀྱིས་འཆིང་བར་མི་འགྱུར་རམ་ཞེ་ན་དྲིས་པའོ། །

[Block 1108]
གཙུག་ཕུད་དགྲོལ་བར་བརྗོད་པར་བྱ། །ཞེས་པས་ནི་ལྷན་ཅིག་སྐྱེས་པའི་རོ་ལ་ལོངས་སྤྱོད་པའོ། །

[Block 1109]
ཀུན་རྫོབ་དེ་ལ་བརྟེན་པའི་སེམས་ཇི་ལྟ་བུ་ཞེ་ན། ད་ནི་དོན་དམ་ལྷན་ཅིག་སྐྱེས་པ་བསྟན་པའི་ཕྱིར། གང་ཞིག་དཔྲལ་བ་སྟོན་པ་ལ། །ཞེས་པས་ཧ་ཛའི་ཡེ་ཤེས་དེ་མངོན་དུ་བྱར་ཡོད་དམ༌[^519]དྲིས་པའོ། །

[Block 1110]
དེ་ཡི་རྒྱབ་ནི་རབ་ཏུ་བསྟན། །ཞེས་པ་ནི་མངོན་དུ་བྱས་པ་སྤོང་བའི་ལན་ནོ། །

[Block 1111]
གང་ཞིག་རྐང་མཐིལ་སྟོན་པ་ལ། །ཞེས་པ་ནི་མངོན་དུ་རྟོག་པ་མེད་ན་ལྟུང་བར་མི་འགྱུར་རམ༌[^520]ཞེས་དྲིས་པའོ། །

[Block 1112]
དགའ་བས༌[^521]རྣམ་པར་རོལ་པར་བྱ། །ཞེས་པ་བསྟན་པའི་ཕྱིར། གང༌[^522]ལྷན་ཅིག་སྐྱེས་པའི་རོ་ལ་ལོངས་སྤྱོད་པའོ། །

[Block 1113]
ཡང་གླེགས་བམ་ལ་ལར། ལྟོ་ཡིས་རྣམ་པར་རྩེ་བར་བྱ། །ཞེས་པ་ནི་དར་གྱི་ཕོ་ལོང་ལ་གདབ་པ་དང་འདྲ་བར་ལྷན་ཅིག་ལྟུང་ཡང༌[^523]ཉོན་མོངས་པས་མི༌[^524]གོས་པར་ཞེན་པ་མེད་པའི་ཐ་ཚིག་གོ། །

[Block 1114 [VERSE]]
ཕྱག་རྒྱ་ཕྱག་རྒྱའི་ལན་གྱིས་ནི། །
ཞེས་པ་ནི་དྲིས་པ་དང་ལན་ནོ། །
དམ་ཚིག་ཅན་གྱི་རྣམ་པར་དབྱེ། །
ཞེས་པ་ནི་དེ་ལྟར་བྱའོ། །

[Block 1115]
[^525]མཇུག་བསྡུས་པའོ། །

[Block 1116]
ད་ནི་སྤྱོད་པའི་བརྡ་བསྟན་པའི་ཕྱིར། དེ་ལ་རྣལ་འབྱོར་མས་སྨྲས་ཞེས་པ་སྔོན་བྱུང༌[^526]དུ་བདག་མེད་མ་ལ་སོགས་པ་ཟབ་པའི་ཁྱད་པར་བསྟན་པའོ། །

[Block 1117]
ཨེ་མ་བུ་ནི་སྙིང་རྗེ་ཆེ་ཞེས་པ་ནི་རྡོ་རྗེ་སྙིང་པོ་སྲི་ཞུར་བོས་པའོ། །

[Block 1118]
གལ་ཏེ་ཕྲེང་བའི་ལག་སྟོན་ན། །ཞེས་པ་ནི་མ་འོངས་པའི་དུས་སུ་རྣལ་འབྱོར་མ་རྣམས་ཕྲེང་བ་སྟོན་པ་ན་ཞེས་པའོ། །

[Block 1119]
འདུ་བར་བྱ་ཞེས་སྨྲས་པ༌[^527]ཡིན། །ཞེས་པ་ནི་སྙོམས་འཇུག་ལ་མངོན་པར་ཕྱོགས་པའམ། ཕྲེང་བ་མངོན་པར་གཏད་བྱས༌[^528]ན། །ཞེས་པ་ནི་མ་འོངས་པའི་དུས་སུ་སྟེར་བའོ། །

[Block 1120 [HEADING]]
#### འདིའི་དོན། ^1-7-1-0

[Block 1121 [HEADING]]
##### སྔོན་བྱུང། ^1-7-1-1-0

[Block 1122]
འདིའི་དོན་ནི་སྔོན་བྱུང་དང་རྗེས་འཇུག་རྣམ་པ་གཉིས་ཏེ། སྔོན་བྱུང་ནི་རྡོ་རྗེ་འཆང་གི་འཁོར་ན་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་དང་རྡོ་རྗེ་མཁའ་འགྲོ་མ་རྣམས་འདུ་བའི་དུས་སུ་ལུས་ཀྱི་བརྡ་རྣམས་དང༌[^529]འོག་ནས་འབྱུང་བའི་ངག་གི་བརྡ་རྣམས་བརྡ་དང་བརྡའི་ལན་དུ་བསྟན་ཏེ།

[Block 1123 [HEADING]]
##### རྗེས་འཇུག། ^1-7-1-2-0

[Block 1124]
རྡོ་རྗེ་སྙིང་པོ་ལ་སོགས་པ་མ་འོངས་པའི་དུས་སུ༌[^530]བརྡ་དང་ངག་གི་བརྡ་རྣམས་ཀྱིས། རྣལ་འབྱོར་ཕ་དང་རྣལ་འབྱོར་མ་རྣམས་སོ་སོར་འདུ་བའི་བརྡ་དང་མན་ངག་མཚོན་པའི་བརྡ་སྟེ། འཇིག་རྟེན་པ་ལས་བཟློག་པས་ནི༌[^531]དྲི་བ་ཡང་གཡོན་པས་བྱས༌[^532]ལ། ལན་ཀྱང་གཡོན་པས་གདབ་པོ། །སྔར་གྱི་ཚེ་ལ་བརྡ་རྐྱང་པའི་ལན་དུ་ཀུན་ལ་སྦྱར་བར་བྱའོ། །

[Block 1125]
བརྟུལ་ཞུགས་དམ་ཚིག་ཤིན་ཏུ་ནོས། །ཞེས་པ་ནི་སྙོམས་འཇུག་གི་སྤྱོད་པ་ལ་གནས་པའོ། །
--- END BLOCKS ---
