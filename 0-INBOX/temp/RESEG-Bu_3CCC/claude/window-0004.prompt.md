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
[Block 141]
འདི་ལ་ཆོས་གང་རྒྱུས་སྒྲུབ་པར་གྱུར་ན་དེ་ཡོད་པའམ་མེད་པའམ་ཡོད་མེད་ཅིག་སྒྲུབ་པར་འགྱུར་གྲང་ན། རྣམ་པ་ཐམས་ཅད་མི་འཐད་དོ། །

[Block 142]
དེ་ལ་རེ་ཞིག་ཡོད་པ་ནི་སྒྲུབ་པར་མི་བྱེད་དེ། སྐྱེས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 143]
འདི་ལྟར་སྐྱེས་པ་ལ་ཡང་སྐྱེ་བས་ཅི་བྱ་སྟེ། [^113]ཅི་སྟེ་ཡོད་ཀྱང་ཡང་སྐྱེ་བ་ནི༌[^114]ནམ་ཡང་མི་སྐྱེ་བར་མི་འགྱུར་བས་དེ་ཡང་མི་འདོད་དོ། །

[Block 144]
རྒྱུར་བསྟན་དུ་ཡང་མི་འཐད་དེ། འདི་ལྟར་ཡོད་པ་ལ་རྒྱུས་ཅི་བྱ། འདི་ལྟར༌[^115]རེ་ཞིག་ཡོད་པ་ནི་སྒྲུབ་པར་མི་བྱེད་དོ། །

[Block 145]
ད་ནི་མེད་པ་ཡང་སྒྲུབ་པར་མི་བྱེད་དེ་མེད་པའི་ཕྱིར་རོ། །

[Block 146]
ཅི་སྟེ་མེད་ཀྱང་སྐྱེ་ན༌[^116]ནི་རི་བོང་གི་རྭ་ཡང་སྐྱེ་བར་འགྱུར་རོ། །

[Block 147]
གལ་ཏེ་དངོས་པོ་ནི་རྒྱུ་ལས་སྐྱེའོ་ཞེ་ན། མི་རུང་སྟེ། རྒྱུ་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 148]
འདི་ལྟར་དངོས་པོ་མེད་ན་གང་གི་རྒྱུར་ཅི་འགྱུར། ཡང་ན་ཅི་ཞིག་བྱས་ན་རྒྱུའི་རྒྱུ་ཉིད་དུ་འགྱུར། འདི་ལྟར་ཐམས་ཅད་དུ་དངོས་པོ་མེད།[^117] དེ་ལ་འདི་ནི་རྒྱུའོ། །

[Block 149]
འདི་ནི་མ་ཡིན་ནོ་ཞེས་བྱེ་བྲག་བསྟན་པ་དེ་ཡོད་པར་ག་ལ་འགྱུར། དེ་ལྟ་བས་ན་མེད་པ་ཡང་སྒྲུབ་པར་མི་བྱེད་དོ། །

[Block 150]
ད་ནི་ཡོད་མེད་ཀྱང་སྒྲུབ་པར་མི་བྱེད་དེ། ཡོད་པ་དང་མེད་པ་གཉིས་ལྷན་ཅིག་འབྱུང་བ་འགལ་བའི་ཕྱིར་དང་། སྐྱོན་སྔ༌[^118]མར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 151]
དེ་ལྟར་ན་ཡོད་མེད་ཀྱང་སྒྲུབ་པར་མི་བྱེད་དོ། །

[Block 152]
དེའི་ཕྱིར་དེ་ལྟར་བརྟགས་ན་གང་གི་ཚེ་དངོས་པོ་གྲུབ་པ་ཇི་ལྟར་ཡང་མི་འཐད་པ་དེའི་ཚེ།

[Block 153 [VERSE]]
ཇི་ལྟར་སྒྲུབ་བྱེད་རྒྱུ་ཞེས་བྱ། །
དེ་ལྟར་ཡིན་ན་མི་རིགས་སོ། །

[Block 154]
དེ་ལྟར་ཡིན་ན་སྒྲུབ་པར་བྱེད༌[^119]རྒྱུ་ཞེས་བྱ་བ་དེ་མི་རིགས་སོ། །

[Block 155]
འདིར་སྨྲས་པ། དམིགས་པ་ནི་ཡོད་དེ། རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་གནས་སུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 156]
བཤད་པ།

[Block 157 [VERSE]]
ཡིན་པའི་ཆོས་ནི་དམིགས་པ་ནི། །
མེད་པ་ཁོ་ནར་ཉེ་བར་བསྟན། །

[Block 158]
འདི་ལ་དམིགས་པ་དང་བཅས་པར་ཞེས་བྱ་བའི༌[^120]ཚིག་གི་ལྷག་མའོ། །

[Block 159]
ཡིན་པའི་ཆོས་འདི་དམིགས་པ་ཁོ་ན་ལས་དམིགས་པ་དང་བཅས་པར་ཉེ་བར་བསྟན་ཏོ། །

[Block 160]
ཡིན་པའི་ཆོས་འདི་དམིགས་པ་མེད་པ་ཁོ་ན་ལས་ཁྱོད་ཀྱིས་རང་གི་བློ༌[^121]དམིགས་པ་དང་བཅས་པ་ཞེས་བརྗོད་དོ། །

[Block 161]
ཇི་ལྟ༌[^122]ཞེ་ན་འདི་ལ་དམིགས་པ་དང་བཅས་པ་ཞེས་བྱ་བ་ནི་དམིགས་པ་ཡོད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 162]
ཆོས་ཡོད་པ་ནི་དམིགས་པ་དང་བཅས་པར་འགྱུར་གྱི་མེད་པ་ནི་མི་འགྱུར་རོ། །

[Block 163]
དམིགས་པ་དང་བཅས་པའི་སྔོན་རོལ་ན་དམིགས་པ་མེད་པས་དེ་ནི་དམིགས་པ་མེད་པ་ཡིན་ནོ། །

[Block 164]
འདི་ལྟ་སྟེ། དཔེར་ན་ནོར་ཡོད་པ་ནི་ནོར་དང་བཅས་པ་སྟེ་ནོར་ཅན་ཞེས་བྱའོ། །

[Block 165]
འགའ་ཞིག་ཡོད་ན་ནོར་དང་བཅས་པར་འགྱུར་གྱི། མེད་ན་མི་འགྱུར་རོ། །

[Block 166]
ནོར་དང་བཅས་པའི་སྔོན་རོལ་ན་ནོར་མེད་པས་དེ་ནི་ནོར་མེད་པ་ཡིན་པ་བཞིན་ནོ། །

[Block 167]
དེའི་ཕྱིར་དམིགས་པ་མེད་པ་ཁོ་ན་ཡིན་པའི་ཆོས་འདི་ལ་ཁྱེད་རང་གི་རྣམ་པར་རྟོག་པས་དམིགས་པ་དང་བཅས་པར་རྟོག་པར་བྱེད་དོ། །

[Block 168]
དེ་ལ་ཁོ་བོས་བཤད་པར་བྱ་སྟེ།

[Block 169 [VERSE]]
དེ་ལྟར་ཆོས་ནི་དམིགས་མེད་ན། །
དམིགས་པ་ཡོད་པར་ག་ལ་འགྱུར། །

[Block 170]
དེ་ལྟར་ཞེས་བྱ་བའི་སྒྲ་ནི་དྲི་བའོ། །

[Block 171]
ག་ལ་འགྱུར་ཞེས་བྱ་བ༌[^123]གཏན་ཚིགས་བསྟན་པ་སྟེ། དེ་ལྟར་ཆོས་དམིགས་པ་མེད་པར་གྲུབ་ན་ཅིའི་ཕྱིར་དོན་མེད་པའི་དམིགས་པ་ལ་རྟོག་པར་བྱེད།

[Block 172]
སྨྲས་པ། ཁྱོད་ཉིད་གཞུང་ལུགས་ཁོང་དུ་མ་ཆུད་པ་ཁོ་ནས་ལོག་པར་རྟོག་གི །ཁོ་བོ་ནི་དམིགས་པ་ཡོད་པ་ནི་དམིགས་པ་དང་བཅས་པ་སྟེ་ནོར་དང་བཅས་པ་བཞིན་ནོ་ཞེས་མི་སྨྲའོ། །

[Block 173]
དེའི་དོན་ནི་འདི་ཡིན་ཏེ་ཆོས་གྲུབ་པ་ནི༌[^124]གཞི་གང་གིས་སྒྲུབ་པར་བྱེད་པ་དེ་ནི་དེའི་དམིགས་པ་ཡིན་ཏེ། དེས་ན་དེ་དམིགས་པ་དང་བཅས་པ་ཞེས་ཉེ་བར་སྟོན་ཏོ། །

[Block 174]
བཤད་པ། དེ་མི་འཐད་དེ།

[Block 175 [VERSE]]
དེ་ལ་ཡང་བཤད་པར་བྱའོ། །
དེ་ལྟར་ཆོས་ནི་དམིགས་མེད་ན། །
དམིགས་པ་ཡོད་པར་ག་ལ་འགྱུར། །

[Block 176]
དེ་ལྟར་ཆོས་དམིགས་པ་མེད་དེ་ཡོད་པ་མ་ཡིན་ཞིང་མངོན་པར་མ་གྲུབ་ན་དམིགས་པ་ཡོད་པར་འཐད་པར་ག་ལ་འགྱུར། ཆོས་ཀྱི་དམིགས་པ་ཞེས་བྱ་བ་དེ་ཡང་མངོན་པར་མ་གྲུབ་པ་ཁོ་ནའོ། །

[Block 177]
མངོན་པར་མ་གྲུབ་ཅིང་མེད་པ་དེ་ལ་དམིགས་པ་ཡོད་པར་ག་ལ་འགྱུར། དམིགས་པ་མེད་ན་ཇི་ལྟར་དམིགས་པས་ཆོས་སྒྲུབ་པར་བྱེད། དེའི་ཕྱིར་དམིགས་པ་ཡང་ཡོད་པ་མ་ཡིན་ལ། ཆོས་ཀྱང་དམིགས་པ་དང་བཅས་པ་མ་ཡིན་པ་ཁོ་ནའོ། །

[Block 178]
འདིར་སྨྲས་པ། དངོས་པོ་གཞན་འགགས་མ་ཐག་པ༌[^125]ནི་དངོས་པོ་གཞན་སྐྱེ་བའི་རྐྱེན་ཡིན་ནོ། །

[Block 179]
དེ་ནི་དེ་མ༌[^126]ཐག་པ་ཞེས་བྱ་བ་སྟེ་དེ་ཡོད་དོ། །

[Block 180]
བཤད་པ།
--- END BLOCKS ---
