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
[Block 71]
མཐུན་པ་ནི་འགྲུས་སྐྱོང་གི་ཚོགས་ཀྱིས་བཤད་དེ། ཚངས་པར་སྤྱོད་པ་དང་མཐུན་པའི་ཕྱིར་ཏེ། དཔེར་ན་གསུང་གི་ཡན་ལག་ལྔ་བསྟན་པ་ལ་སྔ་མ་ཕྱི་མས་བསྟན་ཏེ། ཟབ་པ་འབྲུག་སྒྲས་བཤད་པ་དང་། སྙན་ཅིང་འཇེབས་པ་རྣམ་པར་སྙན་པས་བཤད་པ་དང་། ཡིད་དུ་འོང་བ་དགའ་བར་བྱེད་པས་བཤད་པ་དང་། རྣམ་པར་རིག་པར་བྱ་བ་རྣམ་པར་གསལ་བས་བཤད་པ་དང་། མཉན་པར་འོས་པ་མི་མཐུན་པ་མེད་པས་བཤད་པ་བཞིན་ནོ། །

[Block 72]
ཚིག་བཞི་པོ་ཚིག་ཕྱི་མས་བཤད་པ་དང་བཅས་པ་འདི་དག་གིས་ནི་དྲི་བ་ཐམས་ཅད་ལ་ཡོན་ཏན་བཞི་དང་ལྡན་པའི་ལན་གདབ་པར་བསྟན་པར་འགྱུར༌[^51]ཏེ། སྔ་ཕྱི་མི་འགལ་བ་དང་། ཆོས་ཉིད་དང་མི་འགལ་བ་དང་། འདུལ་བ་དང་མི་འགལ་བ་དང་། དོན་གྱི་མཆོག་དང་འབྲེལ་བའོ། །

[Block 73]
ལུང་ལས་ནི་ཡོན་ཏན་བརྒྱད་དང་ལྡན་པའི་ལན་གདབ་པར༌[^52]ནི་ཚིག་བརྒྱད་ཀྱིས་ཡོངས་སུ་བསྟན་ཏོ་ཞེས་འབྱུང་སྟེ། ཡོན་ཏན་བརྒྱད་ནི་དོན་ལ་སྦྱོར་བས་འབྱུང་བ་དང་། འཇིག་རྟེན་ལ་གྲགས་པའི་ཚིག་འབྲུ་དང་འབྲེལ་པ་དང་། རྒོལ་བ་དང་འགལ་བ་དང་མཐུན་པ་དང་། ཟབ་མོའི་ཚིག་ངེས་པའི་དོན་དང་ཉན་པ་ལ་ཕན་གདགས་པའི་ཚིག་འབྲུ་རྣམ་པར་མི་གཡེང་བའི་གཞིའི་གནས་དང་། འདུལ་བའི་བསམ་པ་དང་མོས་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་རྣམ་པར་འབྱེད་པ་དང་། ལུང་ནོད་པ་དང་། ཁ་ཏོན་དང་། འཛིན་པ་དང་། སེམས་པ་དང་། སྒོམ་པ་མི་གཏོང་བ་དང་། སྒྲ་ཅི་བཞིན༌[^53]དུ་མངོན་པར་ཞེན་པ་མེད་པར་སྟོན་པའོ། །

[Block 74]
བྱ་བ་རྣམས་ལ་ཇི་ལྟ་བ་བཞིན་དུ་སྡུག་བསྔལ་བ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་བརྗོད་པར་བྱའོ། །

[Block 75 [HEADING]]
### འཇིགས་པ་རྣམས་ཀྱི་དོན་གྱི་མདོ། ^2-4-0

[Block 76]
འཇིགས་པ་རྣམས་ཀྱི་དོན་གྱི་མདོ་ནི་འཇིགས་པ་དྲུག་བསྟན་པ་ཡིན་ཏེ། མདོར་བསྡུ་ན་ཐང་ལ་གནས་པའི་དུད་འགྲོའི་འཇིགས་པ་དང་། ཆུའི་འཇིགས་པ་དང་། ཆུ་ན་གནས་པའི་དུད་འགྲོའི་འཇིགས་པ་དང་། མིའི་འཇིགས་པ་དང་། ལུས་དང་ངག་དང་། ཡིད་ཀྱིས་མྱོང་བའི་གནས་གསུམ་དང་། མི་མ་ཡིན་པ་ལས་གྱུར་པ་ལས་རྣམ་པ་གཉིས་སོ། །

[Block 77]
དེ་ལ་མིའི་འཇིགས་པ་ནི་ཐུན་མོང་དང་། ཐུན་མོང་མ་ཡིན་པའི་བྱེ་བྲག་གིས༌[^54]རྣམ་པ་བཞིའོ། །

[Block 78]
ཐུན་མོང་བ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཚར་གཅད་པ་དང་། ཕན་གདགས་པའི་ལས་ཐམས་ཅད་ལ་མཐུ་ཡོད་པའི་རྒྱལ་པོ་སེམས་ཅན་ཐམས་ཅད་ཐུན་མོང་དུ་དེས་འཇིགས་པ་དང་། ནོར་བདོག་པ་ཐམས་ཅད་ཆོམ་རྐུན་གྱིས་འཇིགས་པ་ཐུན་མོང་བའོ། །

[Block 79]
གནོད་པའི་རྒྱུའི་འཇིགས་པ་ཕྱིར༌[^55]རྒོལ་བ་རྣམས་དང་། ཕ་རོལ་པོ་དག་དང་། མཐུ་མེད་པ་དག་དང་། མཐུ་ཡོད་པ་དག་དང་། རྗེ་བོ་ཐུན་མོང་མ་ཡིན་པ་རྣམས་ལས་བྱུང་བ་ནི་ཐུན་མོང་མ་ཡིན་པའོ། །

[Block 80]
མི་མ་ཡིན་པ་ནི་རྣམ་པ་གཉིས་ཏེ། རིག་སྔགས་ཀྱིས་བསླང་བ་རྣམས་དང་། དེ་མ་ཡིན་པས་བསླང་བ་རྣམས་སོ། །

[Block 81 [HEADING]]
### མྱ་ངན་སེལ་བའི་མྱ་ངན་གྱི་བསྡུས་པའི་དོན། ^2-5-0

[Block 82]
མྱ་ངན་སེལ་བའི་མྱ་ངན་གྱི༌[^56]བསྡུས་པའི་དོན་ནི་མདོར་བསྡུ༌[^57]ན་རྣམ་པ་གཉིས་ཏེ། གཉེན་བཤེས་ཀྱི་སྡུག་བསྔལ་ལས་གྱུར་པ་དང་ལོངས་སྤྱོད་ཀྱི་སྡུག་བསྔལ་ལས་གྱུར་པའོ། །

[Block 83]
[^58]དེ་ལ་གཉེན་བཤེས་ཀྱི་སྡུག་བསྔལ་ནི་རྣམ་པ་ལྔ་སྟེ། གཉེན་བཤེས་རྒུད་པ་ལས་གྱུར་པ་དང་། སྐྱེད་པའི་རྒྱུར་གྱུར་པའི་གཉེན་ཕ་མ་རྣམས་དང་། ཡོངས་སུ་བཟུང་བ༌[^59]དང་། འབྲས་བུ་བུ་དང་ཆུང༌[^60]མ་རྣམས་དང་ངག་ཉན་པའི་བྲན༌[^61]དང་། བྲན་མོ་ལ་སོགས་པ་དང་། ཕན་འདོགས་པ་དང་བྱམས་པའི་གཉེན་མཛའ་བོ་དང་། གྲོགས་པོ་རྣམས་དང་ཕན་པ་སྟོན་པའི་གཉེན་སློབ་དཔོན་ལ་སོགས་པའོ། །

[Block 84]
ལོངས་སྤྱོད་ཀྱི༌[^62]སྡུག་བསྔལ་གྱི་མདོ་ནི་ལོངས་སྤྱོད༌[^63]ལས་གྱུར་པའི་སྡུག་བསྔལ་གང་ཡིན་པ་དེའི་བྱེ་བྲག་ལས་ལོངས་སྤྱོད་ཀྱི་སྡུག་བསྔལ་གྱི་བྱེ་བྲག་ཏུ་འགྱུར་རོ། །

[Block 85]
ལོངས་སྤྱོད་ཀྱི་སྡུག་བསྔལ་གྱི་རྒྱུ་ནི་རྣམ་པ་གཉིས་ཏེ། འཇིག་རྟེན་ཐམས་ཅད་ཀྱི་སྡུག་བསྔལ་གྱི་རྒྱུ་རྣམས་དང་། ཁ་ཅིག་གི་ཐུན་མོང་མ་ཡིན་པ་རྣམས་སོ། །

[Block 86]
ཐམས་ཅད་དང་ཐུན་མོང་བ་ནི་མིའི་ཆོམ་རྐུན་རྣམས་དང་མེ་དང་ཆུའོ། །

[Block 87]
ཐུན་མོང་མ་ཡིན་པ་ནི་རྣམ་པ་གཉིས་ཏེ། བདག་གིས་ཚུལ་མ་ཡིན་པ་དང་། གཞན་ལས་གྱུར་པའོ། །

[Block 88]
བདག་གིས་ཚུལ་མ་ཡིན་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། ལོངས་སྤྱོད་སྲུང་བ་དང་། སྒྲུབ་པའོ། །

[Block 89]
གཞན་ལས་གྱུར་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། བགོ་སྐལ་ལ་སྤྱོད་པ་རྣམས་དང་། རང་གི་ཁྱིམ་ནས་བྱུང་བ་རྣམས་ཀྱི་སྡུག་བསྔལ་ཅན་རྣམས་སོ། །

[Block 90 [HEADING]]
### ཡོ་བྱད་ཉེ་བར་སྒྲུབ་པའི་དོན་གྱི་མདོ། ^2-6-0

[Block 91]
ཡོ་བྱད་ཉེ་བར་སྒྲུབ་པའི་དོན་གྱི་མདོ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 92 [HEADING]]
### ཡང་དག་པའི་གནས་སྦྱིན་པའི་དོན་གྱི་མདོ། ^2-7-0

[Block 93]
ཡང་དག་པའི་གནས་སྦྱིན་པའི་དོན་གྱི་མདོ་ནི་བསམ་པ་གང་གིས་ཡོངས་སུ་སྡུད་པ་དང་། སྦྱོར་བ་གང་གིས་ཡོངས་སུ་སྡུད་པའོ། །

[Block 94]
དེ་ལ་བསམ་པ་གང་གིས་ཡོངས་སུ་སྡུད་ཅེ་ན།

[Block 95 [VERSE]]
ཟང་ཟིང་མེད་པའི་སེམས་ཀྱིས་སོ། །
སྦྱོར་བ་གང་གིས་ཡོངས་སུ་སྡུད་ཅེ་ན།
ཆོས་དང་ཟང་ཟིང་གཉིས་ཀྱིས་སོ། །

[Block 96]
དེ་ལ་ཟང༌[^64]ཟིང་གིས་ཡོངས་སུ་བསྡུ་བ་ནི་རྣམ་པ་གཉིས་ཏེ། ཕ་རོལ་ལས་བཙལ་བ་དང་། བདག་གི་ཡོ་བྱད་ཐུན་མོང་དུ་བྱེད་པའོ། །

[Block 97]
ཆོས་ཀྱིས༌[^65]ཡོངས་སུ་བསྡུ་བ་ཡང་རྣམ་པ་གཉིས་ཏེ། གདམས་ངག་སྦྱིན་པ་དང་། རྗེས་སུ་བསྟན་པའོ།[^66] །

[Block 98 [HEADING]]
### གཞན་གྱི་སེམས་དང་རྗེས་སུ་མཐུན་པར་བྱེད་པའི་དོན་གྱི་མདོ། ^2-8-0

[Block 99]
གཞན་གྱི་སེམས་དང་རྗེས་སུ་མཐུན༌[^67]པར་བྱེད་པའི་དོན་གྱི་མདོ་ལས༌[^68]སེམས་དང་མཐུན་པར་བྱེད་པ་ནི་རྒྱས་པ་དང་རབ་ཏུ་དབྱེ་བའོ། །

[Block 100]
དེ་ལ་དོན་གྱི་མདོ་ལས༌[^69]ནི་བསམ་པ་དང་། རང༌[^70]བཞིན་ཡོངས་སུ་ཤེས་ནས་སེམས་ཅན་གང་དག་གིས༌[^71]ཇི་ལྟར་ལྷན་ཅིག་གནས་པར་བྱ་བ་དེ་ལྟར་དེ་དག་དང་གནས་སོ། །

[Block 101]
སེམས་ཅན་གང་དག་ལ་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་བ་དེ་ལྟར་དེ་དག་ལ་སྒྲུབ་པར་བྱེད་དོ་ཞེས་བྱ་བ་དེ་ལ། བསམ་པ་ནི་ད་ལྟར་བྱུང་བའི་རྐྱེན་གྱིས་བསྐྱེད་པའི་སེམས་སོ། །

[Block 102]
རང་བཞིན་ནི་ཚེ་སྔ་མའི་རྒྱུ་ལས་བྱུང་བའི་ངོ་བོ་ཉིད་དོ། །

[Block 103]
ཡང་ན་བསམ་པ་ནི་སེམས་ཅན་རྣམས་ཀྱི༌[^72]སེམས་ཅན་སོ་སོའི་རང་བཞིན་ཐ་དད་པའོ། །

[Block 104]
རང་བཞིན་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་འཇུག་པ་ཐུན་མོང་བ་སྟེ། བསམ་པ་དང་རང་བཞིན་ཤེས་ནས་ལྷན་ཅིག་འགྲོགས་པར་བྱ་ཞིང་། བསམ་པ་དང༌[^73]རང་བཞིན་ཤེས་ནས་སེམས་ཅན་རྣམས་ལ་བསྒྲུབ་པར་བྱའོ།[^74] །དེ་ལ་བསམ་པ་ཤེས་ནས་གནས་པ་དང་། སྒྲུབ་པའི་དབང་དུ་བྱས་ནས་སེམས་ཅན་གང་གིས་ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་བརྩམས་སོ། །

[Block 105]
གཞུང་གི་དོན་གྱི་མདོ་ནི།

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
--- END BLOCKS ---
