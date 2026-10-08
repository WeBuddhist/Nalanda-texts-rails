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
[Block 281]
དགྱེས་པའི་རྡོ་རྗེ་མིང་བསྡུས་པས་ནི་དོན་གྱི་སྟེ་སྟོན་པ་དང་། བསྟན་པ་བསྡུས་པའོ། །

[Block 282]
སྟོན་པ་མིང་བསྡུས་པ་ནི་སྐུ་རྡོ་རྗེ་ལ་སོགས་པ་བཛྲིའི་མིང་གོང༌[^119]མ་ལྟར་གྱུར་པས་བསྡུས་པའོ། །

[Block 283]
དོན་བསྡུས་པ་ནི་ཡེ་ཤེས་རྣམས་སེམས་སུ་བསྡུས་ལ་དེ་ཡང་ལྷན་སྐྱེས་བདེ་ཆེན་དུ་འདུས་སོ། །

[Block 284]
འོ་ན་སྔ་མ་ལས་ཁྱད་པར་ཅི་ཡོད་ཅེ་ན། འདིར་ཁྲོ་བ་དང་ཆགས་པས་འདུལ་བའི་དོན་དུའམ། ཡང་ན་དེ་བཞིན་གཤེགས་པའི་སའི་སྐད་ཅིག་མ་གཉིས་ལ་སོགས་པ་ཡིན་ཏེ་གཞན་དོན་རྫོགས་པའོ། །

[Block 285]
སྔར་གྱི་ནི་དེ་ལྟར་མ་ཡིན་ནོ། །

[Block 286]
བསྟན་པ་མིང་བསྡུས་པ་ནི༌[^120]ལྷན་སྐྱེས་གཏན་ལ་ཕབ་པའམ་སེམས་དཔའ་གསུམ་ནི་ཧེ་དང་བཛྲ་དང་གཉིས༌[^121]བསྡུས་པར་སོ་སོར་གསལ་བར་བཤད་དོ། །

[Block 287]
སྔར་གྱི་སེམས་དཔའ་གསུམ་གྱི་ཡོན་ཏན་ཀུན་ལྡན་པར་ཤེས་པར་བྱའོ། །

[Block 288]
སྟོན་པ་དང་བསྟན་པ་ཡང་འཁོར་མ་འོངས་པའི་གདུལ་བྱ་ལ་དགོངས་ནས་རྣམ་གཞག་ཐ་དད་དུ་བྱ་བའི་དོན་དེ་ཁོ་ན་ཉིད་ལ་ནི་ཁྱད་པར་མེད་དོ། །

[Block 289]
ཡང་ན་མིང་དག་ཏུ་གོང་མ་བསྡུས་ཏེ། ཧེ་ནི་ཕྱི་སེམས་ཅན་གྱི་དོན་སྡུག་བསྔལ་དམིགས་ནས༌[^122]སྐྱེ་བའོ། །

[Block 290]
ཆེན་པོ་ནི་ནང་གི་ལྷན་ཅིག་སྐྱེས་པའི་རོས་ཕུལ་དུ་བྱུང་བའི་སྙིང་རྗེ༌[^123]རང་དབང་མེད་པར་ཟག་པ་དང་བཅས་པར་རྣལ་འབྱོར་པ་ལ་ངང་གིས་སྐྱེ་བའོ། །

[Block 291]
ཧེ་ནི་སྙིང་རྗེ་ཆེན་པོ་སྟེ། ཡེ་ཤེས་ཆེན་པོའི་རང་བཞིན་བདེ་བ་ཆེན་པོ་ཐབས་ཀྱི་སྒོ་ནས་བསྡུས་པའོ། །

[Block 292]
བཛྲ་ནི་ཤེས་རབ་སྟེ་སྟོང་པ་ཉིད་རེག་པའི་ཤེས་རབ་ཆེན་པོའི་ལྟ་བས་བསྡུས་པའོ། །

[Block 293]
དབྱེར་མེད་ནི་བདག་ཉིད་ཀྱི་རྒྱུད་དེ་དམ་ཚིག་སྤྱོད་པས་བསྡུས་སོ། །

[Block 294]
དེས༌[^124]ན་ཤེས་རབ་ཀྱི་རིགས་པ་དང་ཐབས་ཀྱི་རིགས་པ་དང་དབྱེར་མེད་ཀྱི་རིགས་པས་དགྱེས་པའི་རྡོ་རྗེ་བསྟན་ཏོ། །

[Block 295]
མིང་བསྡུས་པའི་ཚུལ་ཡང་མིང་གིས་བསྡུས་པ་ཏེ། ཧེ་ནི་སྙིང་རྗེ་སྟེ་རྟག་ཏུ་དམ་ཚིག་སྤྱོད་པ་བསྡུས་སོ། །

[Block 296]
ཆེན་པོ་ཉིད་ཀྱིས་ཡེ་ཤེས་ཆེན་པོ༌[^125]རོས་གང༌[^126]བསྡུས་པའོ། །

[Block 297]
བཛྲ་ཤེས་རབ་ཀྱིས་ནི་མི་ཕྱེད་པ་དང་སྲིད་པ་གསུམ་གཅིག་ཏུ་བསྡུས་སོ། །

[Block 298]
ཐབས་དང་ཤེས་རབ་བདག་ཉིད་རྒྱུད་ནི་རང་བཞིན་པ་དང་བཏགས་པའོ། །

[Block 299]
རང་བཞིན་གྱི།

[Block 300 [VERSE]]
རྒྱུད་ནི་རྒྱུན་དུ་རབ་ཏུ་གྲགས། །
དེ་ཡང་རྣམ་པ་གསུམ་ཡིན་ཏེ། །
རྒྱུ་དང་ཐབས་དང་འབྲས་བུའོ། །

[Block 301]
དེ་ལ་རྒྱུའི་རྒྱུད་སེམས་ཅན་རང་འབྱུང་ཡེ་ཤེས་ངོ་བོར་གནས་པ། ཐབས་ཀྱི་རྒྱུད་སྔགས་དང་ཕྱག་རྒྱ་ལ་སོགས་པ། འབྲས་བུའི་རྒྱུད་ནི་རང༌[^127]ཉིད་མངོན་སུམ་དུ་གྱུར་པའོ། །

[Block 302]
བཏགས་པ་ལ་ནི་འབྲེལ་བ་དང་མ་ཚང་བ་མེད་པ་དང་མ་འཁྲུགས་ཤིང་འབྲེལ་ན་རྒྱུད་དེ་མངོན་རྟོགས་མ་འཁྲུགས་ལ་ཚིག་འབྲེལ་བ་ལྡན་པའོ། །

[Block 303]
དང་པོ་དངོས་པོ་གནས་ལུགས་སྟོན་པ་དང་སྡུད་པ་པོའི་སྣང་བ་གཉིས་པ་ནི་སྒྲུབ་པ་པོ་དང་ཉན་པའི་ཡིད་ཀྱི་ཤེས་པ་སྒྲ་སྤྱི་དང་དོན་སྤྱིར་བསྟན་པའོ། །

[Block 304]
དེ་ནི་ང་ཡིས་བཤད་ཀྱིས་ཉོན་ནི། སྔོན་བྱུང་དང་རྗེས་འཇུག་གཉིས་ཀར་སྦྱར་རོ། །

[Block 305 [HEADING]]
#### རྒྱུད་ཀྱི་དོན་བཤད་པར་བྱ་བའི་ཚུལ། ^1-1-5-0

[Block 306]
དེ་ལྟར་རྗོད་བྱེད་སྟོན་པ་དང་བརྗོད་པར་བྱ་བའི་ཆོས་བསྟན་ནས། དེ་ནས་རྒྱུད་ཀྱི་དོན་བཤད་པར་བྱ་བའི་ཚུལ་ཡང་གསུམ་སྟེ། གདུལ་བྱ་བྲོད་པ་བསྐྱེད་པའི་ཕྱིར་དམིགས་པའི་ཡུལ་དང་ཉམས་སུ་བླང་པའི་ཐབས་དང་འབྲས་བུའོ། །

[Block 307 [HEADING]]
##### དམིགས་པར་བྱ་བའི་ཡུལ། ^1-1-5-1-0

[Block 308]
དམིགས་པར་བྱ་བའི་ཡུལ་ལ་ཡང་གཉིས་ཏེ། བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པའོ། །

[Block 309 [HEADING]]
###### བསྐྱེད་པ། ^1-1-5-1-1-0

[Block 310]
བསྐྱེད་པ་ལ་གཉིས་ཏེ། སོ་སོར་དམིགས་པ་དང་སྤྱིར་དམིགས་པའོ། །

[Block 311 [HEADING]]
###### **སྤྱིར་དམིགས་པ།** ^1-1-5-1-1-2-0

[Block 312]
སྤྱིར་དམིགས་པ་ནི་ལྟ་སྟངས་དང་ཞེས་པ་ནས་རྣམ་མང་བརྗོད་པར་བྱ་བའི་བར་ཏེ་བརྡ་ནི་དམིགས་པ་སྟེ། དབུགས་དང་སྔགས་དང་ལྷའི་རྣལ་འབྱོར་རོ། །

[Block 313]
རེངས་པ་ལ་སོགས་པ་སྟེ། ལས་རྣམ་བཞིའོ། །

[Block 314]
འོ་ན་བདེ་ཆེན་ནི་རྫོགས་རིམ་ཡིན་ན། བསྐྱེད་རིམ་དུ་འཆད་པ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་ལྷའི་རྣལ་འབྱོར་དང་ལྡན་པས་སོ། །

[Block 315]
ཇི་ལྟར་རིགས་པ་རྣལ་འབྱོར་མ་འོག་ནས་ལས་དང་སྔགས་དང་རྣལ་འབྱོར་སོ་སོར་འཆད་དོ། །

[Block 316]
དེ་ཡང་ཅིས་ཐོབ༌[^128]ན།

[Block 317 [VERSE]]
བསྐྱེད་དང་ཞེས་པ་ནི་ཚོགས་བསགས་པའོ། །
གནས་དང་ཞེས་པ་ནི་རྟེན་གྱི་དཀྱིལ་འཁོར་རོ། །
བྱེད་རྒྱུ་ནི་མངོན་པར་བྱང་ཆུབ་པ་ལྔའོ། །

[Block 318 [HEADING]]
###### **སོ་སོར་དམིགས་པ།** ^1-1-5-1-1-1-0

[Block 319]
སོ་སོར་དམིགས་པ་རེངས་པ་ལ་སོགས་པ་ནི་ཇི་ལྟར་རིགས་པ་རྣལ་འབྱོར་རྣམས་ཀྱིས་སོ། །

[Block 320 [HEADING]]
###### རྫོགས་པའི་རིམ་པའི་དམིགས་པ། ^1-1-5-1-2-0
--- END BLOCKS ---
