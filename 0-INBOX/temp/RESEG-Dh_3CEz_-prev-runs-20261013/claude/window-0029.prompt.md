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
[Block 1016 [VERSE]]
དུར་ཁྲོད་ནི་བྱ་རོག་གི་གདོང་ཅན་ནོ། །
མ་མོའི་ཁྱིམ་ནི་རྩ་གཞན་དག་གོ། །
དུས་མཚན་མོ་ནི་འཁོར་ལོ་གསུམ་མོ། །

[Block 1017]
དབེན་པའམ་བས་མཐའ་ནི་བདེ་བ་ཆེན་པོའི་འཁོར་ལོའོ། །

[Block 1018]
དེ་དག་ཅིའི་ཕྱིར་ཞེ་ན། དེ་ཉིད་དུ་འདུ་ཞིང་དེ་ལས་བྱུང་བ་དང་རང་གིས་བསྐུལ་བ་གཡོ་བ་དང་བྲལ་བ་དང་དེ་དག་ཏུ་བྱང་ཆུབ་སེམས་འཆར་བ་དང་གནས་གསུམ་དུ་ངལ་སོ་ཞིང་ནུབ་པ་དང་ཆགས་པ་དང་ཆགས་བྲལ་གྱི་སྐྱོན་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 1019]
གཉིས་སུ་མེད་པ་ཕྱག་རྒྱ་ཆེན་པོ་ནི། ཤིང་གཅིག་སྟེ༌[^453]ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པའོ། །

[Block 1020]
དུར་ཁྲོད་ནི་ལུས་སོ། །

[Block 1021]
མ་མོའི་ཁྱིམ་ནི་དབང་པོ་ལྔའི་གྲོང་ཁྱེར་རོ། །

[Block 1022]
མཚན་མོ་ནི་ཡོད༌[^454]དོ། །

[Block 1023]
དབེན་པ་དང་།[^455] བས་མཐའ་ནི་དེ་དག་གི༌[^456]ཐབས་སོ། །

[Block 1024]
དེ་དག་ཅིའི་ཕྱིར་ཞེ་ན། ཀུན་ཕྱག་རྒྱ་ཆེན་པོ་ལས་སྐྱེས་པ་དང་། འདི་དག་གི་ཁོང་ན་མི་གསལ་ལ༌[^457]གཟུགས་སུ་གནས་པ་དང་། འདི་དང་མ་བྲལ་བ་བཞིན་དུ་རྗེས་སུ་འབྲང་བ་དང་སྤྱིའི་རྣམ་པར༌[^458]མི་གསལ་བ༌[^459]འབའ་ཞིག་ལ་དམིགས་པ་དང་ཡིད་དང་བས་དབང་པོ་དང་ལ། །

[Block 1025 [VERSE]]
དེས་ཡེ་ཤེས་རང་འབར་བའི་ཕྱིར་རོ། །
བསྒོམ་པ་བཟང་བར་བརྗོད་པར་བྱ། །

[Block 1026]
ཞེས་པ་ནི་དེ་ལྟ་བུ་དག་གིས་ནི་ལྷན་ཅིག་སྐྱེས་པའི་གདོན༌[^460]མི་ཟ་བར་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1027]
དེ་ཡང་བསྐྱེད་རིམ་དང་ཐུན་མོང་དུ་ཤིང་གཅིག་ལ་སོགས་པའི་ཕྱི་རོལ་གྱི་གནས་སུ་བཤད་པའི་ཚེ་གསང་བའི་སྤྱོད་པ༌[^461]ཐུན་མོང་མ་ཡིན་པ་ཡིན༌[^462]ལ་བཤད་ཚུལ་སོ་སོར་སྦྱར་བ་ཐུན་མོང་དག་ཏུ་ཡང་གནས་སོ། །

[Block 1028]
འདི་རྣམས་ཀྱི་ཆོ་ག་ཁ་བསྐང་བ་ནི་སྔ་མ་དང་འདྲའོ། །

[Block 1029]
ད་ནི་དུས་བསྟན་པའི་ཕྱིར། ཅུང་ཟད་དྲོད་ནི་ཐོབ་པ་ན། །ཞེས་པ་སྟེ།[^463] དེ་ཡང་ཕྱག་རྒྱ་ཆེན་པོའི་མན་ངག་ཉམས་སུ་ལེན་པས་ནི། གསང་བའི་སྤྱོད་པའི་དྲོད་དོ། །

[Block 1030]
དབང་པོ་རབ་སྣང་གི་དྲོད་མན་ངག་གི་ཅུང་ཟད་སྨྱོན་པའི་དྲོད་དོ། །

[Block 1031]
སྤྱོད་ལམ་དང་བསྲེ་བའི་མན་ངག་ནི་ཕྱི་རོལ་གྱི་དངོས་པོས་མི་འགྱུར་བ་ནི་སྨྱོན་པའི་བརྟུལ་ཞུགས་ཆེན་པོའི་དྲོད་དོ། །

[Block 1032]
དེ་དག་ནི་ནུས་པའི་ཚད་ཀྱི་དུས་ཡིན་ལ། ད་ནི་རྒྱུ་མཚན་གྱི་དུས་བསྟན་པའི་ཕྱིར། གང་ཚེ་སྤྱོད་པ་བྱེད་འདོད་ན། །ཞེས་པ་སྟེ། གཞན་གྱི་དོན་དུའོ། །

[Block 1033 [VERSE]]
གང་ཚེ་འགྲུབ་འགྱུར་འདོད་ཡོད་ན། །
ཞེས་པ་ནི་རང་གི་དོན་དུའོ། །
[^464]འདིས་ནི་སྤྱོད་པ་སྤྱད་པ་ཉིད། །

[Block 1034]
ཅེས་པ་ནི་དེ་གསུམ་གྱི་ཚེ་སྤྱོད་པ་བྱ་བ་ཁོ་ནའོ། །

[Block 1035]
དེ་ནི་གསང་བ་ལ་སོགས་པའི་ཐུན་མོང་ངོ་། །ཤིན་ཏུ་བཞིན་བཟངས་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཉིས་ཀྱིས་ནི་གྲོགས་བསྟན་ཏོ། །

[Block 1036]
གསང་བའི་སྤྱོད་པ་ཐུན་མོང་མ་ཡིན་པའོ། །

[Block 1037]
ཤིང་གཅིག་པ་ལ་སོགས་པ་ཡང་གྲོགས་བསྟན་པ་དང༌[^465]མི་འགལ་ལམ་ཞེ་ན། མ་ཡིན་ཏེ་དེར༌[^466]ནི་བཤད་པའི་ཚུལ་སྦྱར་བ་ཡིན་ལ། འདིར་ནི་དངོས་སུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 1038]
གང་ཚེ་དགའ་བ་ལ་སོགས་པ་ནི་གླུ་དང་གར་ལ་སོགས་པ་ནི་སྤྱོད་པའི་ངོ་བོས་བསྟན་ཏེ་གོ་སླའོ། །

[Block 1039]
དེ་ལ་ཕྱག་རྒྱའི་རྣམ་དག་དང་བཟའ་བཏུང་གི་ཡོན་ཏན་ནི་རང་དང་འབྲེལ་བར་ཤེས་པར་བྱའོ། །

[Block 1040 [HEADING]]
##### རང་ལུས་ཐབས་ལ་བརྟེན་པ་ཅུང་ཟད་སྨྱོན་པ་བརྟུལ་ཞུགས་ཀྱི་སྤྱོད་པ། ^1-6-1-2-0

[Block 1041]
ད་ནི་ཅུང་ཟད་སྨྱོན་པའི་བརྟུལ་ཞུགས་ཀྱི་སྤྱོད་པ་བསྟན་པའི་ཕྱིར། རྐུན་མའི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། འདིའི་ཆ་བྱད་གཞན་ནི། སྨད་གཡོགས་ཁ་དོག་སྣ་ཚོགས་དང་། །ཞེས་པ་ལ་སོགས་པ་བསྟན་པ༌[^467]ཕྱི་མར་བསྟན། འདི་ནི་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་གསུམ་གྱིས་ཆ་བྱད་བསྟན་ཏེ་གོ་སླའོ། །

[Block 1042]
རང་ལུས་ཐབས་དང་ལྡན་པ་དེས་གླུ་དང་གར་གྱི་སྙོམས་པར་འཇུག་པ་དེས་སྤྱོད་པ་མ་ཡིན་ཏེ། དེས་ན། ཅང་ཏེའུའི༌[^468]སྒྲ་ནི་བླངས་པ་སྟེ། །

[Block 1043 [VERSE]]
ཞེས་པ་ནི་གླུ་དང་འདྲ་བའི་སྤྱོད་པའོ། །
ཁ་ཊྭཱཾ་ག་སྒོམ༌[^469]ཤེས་རབ་ནི་གར་དང་འདྲའོ། །

[Block 1044]
རྡོ་རྗེ༌[^470]སྤྱོད་པ་ཡིས་ཞེས་པ་ནི་སྙོམས་པར་འཇུག་པ་ལྟ་བུའོ། །

[Block 1045]
འདི་དག་བཟླས་པ༌[^471]དང་སྒོམ་པ༌[^472]ཡིན་ཞེས་པ་ནི་ཆེ་བའི་བདག་ཉིད་དེ། བཟླས་སྒོམ༌[^473]དང་ལྡན་པའི་སྙོམས་འཇུག་གི་སྤྱོད་པའོ། །

[Block 1046]
བརྐམ་དང་རྨོངས་ལ་སོགས་པའི་ཚིགས་བཅད་གཅིག་གིས་ནི་བསམ་པའི་ཁྱད་པར་ཏེ༌[^474]གོ་སླའོ། །

[Block 1047]
སྤྱིར་སྤྱོད་པ་མ་བྱས་པས་སངས་མི་རྒྱའམ་ཞེ་ན། མི་རྒྱ་སྟེ་སྤྱོད་པ་བྱེད་པ་ཁོ་ན་སྟེ། དཔེར་ན་མི་འགའ་ཞིག་སྦལ་པས༌[^475]འཇིགས་ལ།[^476] འདི་ལ་ཅིའི་ཕྱིར་འཇིགས་གནོད་པའི་རྩལ་ཡང་མེད་ན། འགུགས༌[^477]པའི་མཆུ་ཡང་མེད། གཅོད་པའི༌[^478]སོ་ཡང་མེད་པའི་ཕྱིར་འཇིགས་པར་མི་བྱའོ་ཞེས་བརྗོད་ཀྱང་ད་དུང༌[^479]བག་ཚ་བ་དང་ལྡན་ཏེ། དེས་རེག་པ་དང་གནོད་པའི་སྦྱོར་བ་བྱེད་པས། དེས་སྔ་མའི་དོན་དེ་ཁོང་དུ་ཆུད་ནས་འཇིགས་པ་མེད་པ་ཐོབ་བོ། །

[Block 1048]
དེ་བཞིན་དུ་དངོས་པོ་ལ་མངོན་པར་ཞེན་པ་ལྟ་བས་རང་བཞིན་མེད་པར་རྟོགས། སྒོམ་པས་ཀྱང་དེ་ལྟར་བསྒོམས་ཀྱང་དངོས་པོ་ལ་མངོན་པར་ཞེན་པ་ད་དུང་སྐྱེ་བས། སྤྱོད་པ་བྱ་དགོས་ཏེ་གཙང་བ་དང་མི་གཙང་བ་དང་། སྡུག་པ་དང་མི་སྡུག་པ་དང་། ཞེ་སྡང་བ་དང་མི་སྡང་བ་དང་། བསྟོད་པ་དང་སྨད་པ་ལ་སོགས་པ་དངོས་པོ་ལ་མངོན་པར་ཞེན་པ༌[^480]སྐྱེ་བས་རོ་མཉམ་པའི་སྤྱོད་པ་བྱ་དགོས་སོ། །

[Block 1049]
ཡང་སྤྱོད་པ་འདི་གསུམ་མཐར་ཆགས་སུ་བྱ་དགོས་སམ་མི་དགོས་ཞེ་ན། ལ་ལ་དག་ལ༌[^481]ནི་མཐར་ཆགས་སུ་ཡང་བྱ། ལ་ལ་དག་ནི་ཐོད་རྒལ་དུ་ཡང་སྤྱོད་དེ། སྤྱོད་པ་སྤྱོད་པ༌[^482]ལམ་དུ་བྱ། སྤྱོད་ལམ་དབང་པོ༌[^483]རང་སྣང་ཕྱག་རྒྱ་ཆེན་པོར་སྦྱར་ལ། དེ་ནས་རྟགས་གསུམ་པོ་ལས་བར་པ༌[^484]ལ་བྱེད་པ་ཡང་སྲིད་ཐ་མ་ལ་བྱེད་པ་ཡང་སྲིད་དོ། །

[Block 1050]
བཤད་པའི་རྒྱུད་ནས་ནི་སྤྱོད་པ་བཞི་རུ་བརྟགས་ཏེ། རྒྱལ་ཚབ་ཀྱི་སྤྱོད་པ་དང་། རིགས་པ་བརྟུལ་ཞུགས་ཀྱི་སྤྱོད་པ་དང་། ཕྱོགས་ལས་རྣམ་པར་རྒྱལ་བའི་སྤྱོད་པ་དང་། ཨ་ཝ་དྷཱུ་ཏཱིའི་སྤྱོད་པའོ། །

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
--- END BLOCKS ---
