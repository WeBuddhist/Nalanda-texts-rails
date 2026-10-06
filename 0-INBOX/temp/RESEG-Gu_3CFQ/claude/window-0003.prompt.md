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
[Block 106 [VERSE]]
ཕན་མིན་བསླབ་པ་མ་གཏོགས་པར། །
གང་གིས་ཕ་རོལ་སྡུག་བསྔལ་བ། །
དེ་དང་གཞན་དང་བདག་ལ་ཡང་།
དངོས་པོ་དེ་ནི་དེ་མི་སྤྱོད། །

[Block 107]
ཅེས་བྱའོ། །

[Block 108]
སེམས་ཅན་གང་དག་ལ་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་བ་ཞེས་བྱ་བ་དེ་ནས་བཟུང་སྟེ། གཞན་ཁྲོ་བའི་ཀུན་ནས་དཀྲིས་པས་ཀུན་ནས་དཀྲིས་པ་ལ་ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་ནི་རང་བཞིན་ཤེས་ནས་སེམས་ཅན་གང་དག་དང་ཇི་ལྟར་ལྷན་ཅིག་གནས་པར་བྱ་བ་དང་སེམས་ཅན་གང་དག་ལ་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་བ༌[^75]ཞེས་བྱ་བའི་དབང་དུ་བྱས་པ་ཡིན་ཏེ། གཞུང་འདིའི་དོན་གྱི་མདོ་ནི་ཡིད་ཀྱི་ལས་བསྒྲུབ་པ༌[^76]དང་། ངག་གི་ལས་བསྒྲུབ་པ་དང་། ལུས་ཀྱི་ལས་བསྒྲུབ༌[^77]པའོ། །

[Block 109]
དེ་ལ་ཡིད་ཀྱི་ལས་སྒྲུབ་པའི་དབང་དུ་བྱས་ཏེ་ཁྲོ་བའི་ཀུན་ནས་དཀྲིས་པས་ཀུན་ནས་དཀྲིས༌[^78]པ་ལ་ཞེས་བྱ་བ་ནས། བདག་ཉིད་མཐོང་བར༌[^79]མི་སྟོན་ཏོ་ཞེས་བྱ་བའི་བར་དུ་སྨོས་སོ། །

[Block 110]
ཡིད་ཀྱི་ལས་བསྒྲུབ་པ༌[^80]ཡང་གཉི་ག་དང་ཅི་རིགས་པར་སྦྱར་བར་བྱ་སྟེ། ཇི་ལྟར་བྱ་ཞེ་ན། ཁྲོ་བའི་ཀུན་ནས་དཀྲིས་པ་ཞེས་བྱ་བ་སེམས་སྒྲུབ་པའི་གནས་སྐབས་ཀྱིས་འདུལ་བ་དེ་ལ་རང་གི་སེམས་སྒྲུབ་ཅིང་འཁྲུག་ཀྱང་མི་འཁྲུག་ལ༌[^81]སྨ་ཡང་འབེབས་པར་བྱེད་དེ། དེ་བཞིན་དུ་གཞན་ལ་ཡང་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 111]
ལུས་ཀྱི་ལས་སྒྲུབ་པ་ལས་བརྩམས་ཏེ་གཞན་དག་ལ་མི་རྟེན༌[^82]པར་ཡང་མི་བྱེད་ཧ་ཅང་རྟེན་པར༌[^83]ཡང་མི་བྱེད་དོ། །

[Block 112]
ངག་གི་ལས་སྒྲུབ་པ་ལས་བརྩམས་ཏེ་མདུན་དུ་མཛའ་བོ་ལས༌[^84]སྨོད་པར་ཡང༌[^85]མི་བྱེད་ཅེས་བྱ་བ་ནས་ཆོས་དང་མཐུན་པར་བཤད་ཀྱི༌[^86]བྱང་བར་བྱེད་དོ། །

[Block 113 [HEADING]]
### ཡང་དག་པར་ཡོན་ཏན་གྱིས་ཡང་དག་པར་དགའ་བར་བྱེད་པའི་དོན་གྱི་མདོ། ^2-9-0

[Block 114]
ཡང་དག་པར༌[^87]ཡོན་ཏན་གྱིས་ཡང་དག་པར་དགའ་བར་བྱེད་པའི༌[^88]དོན་གྱི་མདོ་ནི་དད་པ་ལ་སོགས་པ་དེ་དག་ཁོ་ནར་ཟད་དེ། དད་པ་ལ་སོགས་པ་ལྔ་པོ་ཁོ་ན་སྡུད་པའི་རྒྱུ་ཡིན་པར་འོག་ནས་སྟོན་ཏོ། །

[Block 115 [HEADING]]
### ཚར་བཅད་པའི་དོན་གྱི་མདོ། ^2-10-0

[Block 116]
ཚར་བཅད་པའི་དོན་གྱི་མདོ་ནི་ཉེས་པ་དང་། འགལ་བ་རྣམ་པ་གསུམ་ཡོད་པ་ལས་ཉེས་པ་ཇི་ལྟ་བ་བཞིན་དུ་སྨ་དབབ་པ་དང་ཆད་པ་རྣམ་པ་གསུམ་མོ། །

[Block 117]
སྤང་བ་ལ་ནི་རྣམ་པ་གཉིས་ཏེ། དེ་དག་ཉིད་ཕྱིར་དགུག་པར་བྱ་བ་དང་། འགྲོགས་པར་མི་བྱ་བའོ། །

[Block 118]
དེ་ལ་ཉེས་པ་ནི་བྱ་བའི་རིགས་པ་མི་བྱེད་པའོ། །

[Block 119]
འགལ་བ་ནི་བྱ་བ་མི་རིགས་པ༌[^89]བྱེད་པའོ། །

[Block 120 [HEADING]]
### རྫུ་འཕྲུལ་གྱི་དོན་གྱི་མདོ། ^2-11-0

[Block 121]
རྫུ་འཕྲུལ་གྱི་དོན་གྱི་མདོ་ནི་སྐྲག་པར་བྱ་བ་དང་། འདུན་པར་བྱ་བའོ། །

[Block 122 [HEADING]]
## ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་རྣམ་པ་གསུམ། ^3-0

[Block 123]
ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་རྣམ་པ་གསུམ་ཞེས་བྱ་བ་འདིས་ནི་ཚུལ་ཁྲིམས་མང་བར་བསྟན་ཏོ། །

[Block 124]
བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་ལ་ཞེས་བྱ་བ་འདིས་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་གང་ལ་སློབ་པ་དེ་བསྟན་ཏོ། །

[Block 125]
གང་གིས༌[^90]རྣམ་པར་རིག་བྱེད་ཀྱི་དོན་འཛིན་པ་དང་། གོ་བར་ནུས་པ་ལ་ཐུགས་བརྩེ་བའི་སླད་དུ་ཅུང་ཟད་ཅིག་གསན་ཅིང་ཐུགས་བརྩེ་བའི་སླད་དུ་སྩལ་བའི་རིགས་སོ་ཞེས༌[^91]སྦྱར་བར་བྱའོ། །

[Block 126]
ཡེ་ཤེས་དང་མཐུ་ཆེན་པོ་ཐོབ་པ་རྣམས་ལ་ཞེས་བྱ་བ་ནི་ཟབ་པ་དང་རྒྱ་ཆེ་བ་དང་ལྡན་པར་བསྟན་ཏོ། །

[Block 127]
མཆོད་པ་བྱས་པ་ནི་མེ་ཏོག་དང་། བདུག་པ་དང་སྤོས་ལ་སོགས་པ་དང་། བསྟོད་པ་བརྗོད་པ་དང་། ཕྱག་བྱ་བ་ལ་སོགས་པས་མཆོད་པའོ། །

[Block 128]
ཅི་ནུས་པ་དང་རྒྱུའི་སྟོབས་ཅི་ཡོད་པས་ཞེས་བྱ་བ་ནི་སེམས༌[^92]བསྐྱེད་པ་དེ་ད་ལྟར་བྱུང་བའི་སྐྱེས་བུའི་རྩལ་དང་། འདས་པའི་ཚེ་རབས་ན་བྱས་པའི་རྒྱུའི་འབྲས་བུར་བསྟན་པའོ། །

[Block 129]
གལ་ཏེ་འབོགས་པ༌[^93]ནི་ཆོས་མཚུངས་པ་ཁྱིམ་པ་ཞིག་ཡིན་ན་ནི་རིགས་ཀྱི་བུ་ཞེས་བྱ་བའོ། །

[Block 130]
ཡང་ན་རབ་ཏུ་བྱུང་བ༌[^94]ན་ཡང་གལ་ཏེ༌[^95]གཞོན་ནུ་ཞིག་ཡིན་ན་ཚེ་དང་ལྡན་པ་ཞེས་བྱ་བའོ།

[Block 131]
[^96] །ཅི་སྟེ་རྒན་པ་ཞིག་ཡིན༌[^97]ན་ནི་བཙུན་པ་ཞེས་བྱ་སྟེ། འདིས་ཅི༌[^98]བསྟན་ཞེ་ན། རབ་ཏུ་བྱུང་བ་འབའ་ཞིག་དང་། རྒན་པ་ཉི་ཚེ་ལས་གནོད་པར་བྱ་བར་ངེས་པ་མེད་པར་བསྟན་པའི་དོན་ཏོ། །

[Block 132]
བསླབ་པའི་གཞི་གང་ཡིན་པ་རྣམས་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་རྣམ་པ་གསུམ་པོ་རེ་རེ་ལ་བསླབ་པའི་གཞི་སོ་སོ་བ་གང་དག་ཡོད་པ་དེ་དག་གོ། །

[Block 133]
ཚུལ་ཁྲིམས་གང་ཡིན་པ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་རྣམ་པ་གསུམ་མོ། །

[Block 134]
ཡེ་ཤེས་གཟིགས་པ་ཞེས་བྱ་བ་ལ།

[Block 135]
ཡེ་ཤེས་ནི་ལྐོག་ཏུ་གྱུར་པ་འཛིན་པའོ། །གཟིགས་པ་ནི་དངོས་པོ་མངོན་སུམ༌[^99]དུ་གྱུར་པ་འཛིན་པའོ། །

[Block 136]
ཕམ་པའི་གནས་ལྟ་བུའི་ཆོས་བཞི་ཞེས་བྱ་བ་འདིས་ཅི་བསྟན་ཞེ་ན། འདི་ལ་གནས་པས་ན་གནས་ཞེས་བྱ་སྟེ།

[Block 137 [VERSE]]
ཕམ་པ་རྣམས་ཀྱི་གནས་ནི་ཕམ་པའི་གནས་སོ། །
ཕམ་པ་རྣམས་ཀྱི་གནས་དེ་གང་ཞེ་ན།
གང་ལ༌[^100]བརྟེན་ན་ཕམ་པའི་ཆོས་རྣམས་འབྱུང་བར་འགྱུར་བའོ། །

[Block 138]
གང་ལ༌[^101]བརྟེན་ཏེ་འབྱུང་བར་འགྱུར་ཞེ་ན། འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་ལ་བརྟེན་ཏེ་འབྱུང་ངོ་། །ཆོས་བཞི་ཇི་ལྟར་གསུམ་ལ༌[^102]བརྟེན་ཏེ་འབྱུང་ཞེ་ན། འདོད་ཆགས་ལ་རྣམ་པ་གཉིས་ཡོད་པའི་ཕྱིར་ཏེ། འདོད་ཆགས་རྣམ་པ་གཉིས་ནི་འཁྲིག་པའི་དངོས་པོ་ལ་འདོད་ཆགས་དང་། དངོས་པོ་གཞན་ལ་འདོད་ཆགས་སོ། །

[Block 139]
དེ་ལ་འཁྲིག་པའི་དངོས་པོ་ལ་འདོད་ཆགས་ལ་བརྟེན་པ་ལས་ནི་ཕམ་པའི་བསླབ་པའི་གཞི་དང་པོའོ། །

[Block 140]
དངོས་པོ་གཞན་ལ་འདོད་ཆགས་ལ་བརྟེན་པ་ལས་ནི་གཉིས་པའོ། །

[Block 141]
རྣམ་པ་གཅིག་ཏུ་ན་ཕམ་པ་རྣམས་ཀྱི་གནས་ཡིན་ཏེ། ཕམ་པའི་ཆོས༌[^103]གང་ལ་གནས་པ་བསླབ་པའི་གཞི་བཅས་པ་ཆེན་པོ་ལ་གནས་སོ། །

[Block 142]
དེ་དང་མཐུན་པ༌[^104]རྣམས་ནི་ཕམ་པའི་གནས་ལྟ་བུ་རྣམས་ཏེ། དེ་དག་གི་གནས་ལྟ་བུ་ཉིད་ཆེན་པོའི་གནས་ནི་འདི་དག་གི་ཡང་ཡིན་ནོ། །

[Block 143]
དེ་ལྟ་བས་ན་ཆོས་བཞི་པོ་འདི་དག་ནི་ཕམ་པའི་གནས་ལྟ་བུ་ཞེས་བྱ་སྟེ། དཔེར་ན་སྡོམ་པའི་ཚུལ་ཁྲིམས་ཆེན་པོའི་ཆོས་རྣམས་ཇི་ལྟ་བ་བཞིན་དུ་འདི་དག་ཀྱང་དེ་དང་འདྲ་བའི་ཕྱིར་ཕམ་པའི་གནས་ལྟ་བུ་ཞེས་བྱའི༌[^105]རྣམ་པ་ཐམས་ཅད་དུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་སྟེ། དེ་ནི༌[^106]འོག་ནས་བསྟན་ཏོ། །

[Block 144]
ཉན་ཐོས་ཀྱི་ཐེག་པ་པ་བསྙེན་པར་རྫོགས་པས་བསླབ་པ་མ་ཕུལ་བར་འཁྲིག་པའི་ཆོས་བསྟེན་པས་ཉེས་པ་ཐོབ་པ་གང་ཡིན་པ་དེ་ནི། རྙེད་པ་དང་བཀུར་སྟི་ལ་ལྷག་པར་ཞེན་ཏེ། [^107]བདག་ལ་སྟོད་པ༌[^108]དང་གཞན་ལ་སྨོད་པས་ཐོབ་པར་འགྱུར་ཏེ། གཞན་དག་ལ་ཡང་དེ་བཞིན་དུ་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 145]
སྡུག་བསྔལ་བ་ཞེས་བྱ་བ་ནི་སྙིང་རྗེའི་གཞིར་བསྟན་ཏོ། །
--- END BLOCKS ---
