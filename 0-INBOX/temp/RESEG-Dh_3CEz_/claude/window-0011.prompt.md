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
[Block 386]
བསྒོམ་པ་ཉམས་སུ་ལེན་པ་ལ་གཉིས་ཏེ། མངོན་རྟོགས་ལམ་དུ་བྱས་པ་དང་། འབྲས་བུ་ལམ་དུ་བྱས་པའོ། །

[Block 387 [HEADING]]
###### **མངོན་རྟོགས་ལམ་དུ་བྱས་པ།** ^1-1-5-2-1-2-1-2-1-0

[Block 388 [VERSE]]
མངོན་རྟོགས་ལམ་དུ་བྱས་པ་ལ་གསུམ་སྟེ།
ཆགས་ཅན་དང་ཆགས་བྲལ་དང་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 389 [HEADING]]
###### **ཆགས་ཅན།** ^1-1-5-2-1-2-1-2-1-1-0

[Block 390]
དེ་ལ་ཆགས་ཅན་ནི་གཞན་ལུས་ཤེས་རབ་ལས་ཀྱི་ཕྱག་རྒྱ་ལ་བརྟེན་པ་སྟེ། དེ་ཡང་ལུས་ལ་ཞེས་པ་ནི་མཚོན་བྱེད་དབྱེར་མེད་དུ་རང་གི༌[^142]ཉམས་སུ་མྱོང་བ་སྟེ། དེ་རྟོག་པར་རང་ཤུགས་སུ་གཅོད་ཅིང་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པའོ། །

[Block 391]
དངོས་པོ་ཀུན་ལ་ཁྱབ་པ་པོ་ནི་མཚོན་བྱ་ལྷན་སྐྱེས་དོན་དམ་བདེ་བ་ལ་མི་རྟོག་པ་དང་ཀུན་རྫོབ་ཞུ་བ་དང་དབྱེར་མེད་རང་ཡང་དག་པར་རིག་པའོ། །

[Block 392]
ལུས་གནས་ལུས་ལས་མ་སྐྱེས་པ།[^143] །ཞེས་པ་ནི་མཚན་བྱ་ལྷན་སྐྱེས་ལ་འཇུག་ཚུལ་གསལ་བྱེད་ཀྱི་རྒྱུས་འཇུག་གི།[^144] འདུས་བྱས་ཀྱི་སྐྱེད་པར་བྱེད་པའི་རྒྱུས་ནི་མ་ཡིན་ནོ། །

[Block 393 [HEADING]]
###### **ཆགས་བྲལ།** ^1-1-5-2-1-2-1-2-1-2-0

[Block 394]
ཆགས་བྲལ་ནི་རང་ལུས་ཐབས་ལྡན་དམ་ཚིག༌[^145]ཕྱག་རྒྱ་སྟེ། དེ་ཡང་ལུས་ལ་ཞེས་པ་ནི་ལྟེ་བར་རྩ་གསུམ་འདུས་པ་གྲུ་གསུམ་སྐྱེ་གནས་སུའོ། །

[Block 395 [VERSE]]
ཡེ་ཤེས་ནི་དོན་དམ་མཚོན་བྱེད་བདེ་བའོ། །
གནས་ཞེས་པ་ནི་ཀུན་རྫོབ་མཚོན་བྱེད་ཞུ་བའོ། །

[Block 396]
ཡང་ན་ཡེ་ཤེས་ནི༌[^146]བདེ་བའོ། །

[Block 397]
ཆེན་པོ་ནི་སྤྱི་བོ་བདེ་ཆེན་གྱི་གནས་སོ། །

[Block 398]
གནས་ཞེས་པ་ཞུ་བ་བདེ་བ་དང་བཅས་པས༌[^147]འབབ་སྟེ་ལྟེ་བར་གནས་པའོ། །

[Block 399]
རྟོག་པ་ཐམས་ཅད་ཡང་དག་སྤངས། ། ཞེས་པ་ནི་མཚོན་བྱེད་དབྱེར་མེད་དེ། རྟོག་པ་རང་ཤུགས་སུ་སྤྱོད༌[^148]ཅིང་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པའོ། །

[Block 400]
དངོས་པོ་ཀུན་ལ་ཁྱབ་པ་པོ། །ཞེས་པ་ནི་མཚོན་བྱ་ལྷན་སྐྱེས་དོན་དམ་བདེ་བ་ལ་མི་རྟོག་པ་དང་། ཀུན་རྫོབ་ཞུ་བ་དང་དབྱེར་མེད་རང་རིག་པའོ། །

[Block 401]
ལུས་གནས་ལུས་ལས་མ་སྐྱེས་ཞེས་པ་ནི་མཚོན་བྱ་ལྷན་སྐྱེས་ལ་འཇུག་ཚུལ་གསལ་བྱེད་ཀྱི་རྒྱུ་ཡིན་ཏེ། སྐྱེད་བྱེད་ཀྱི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 402 [HEADING]]
###### **ཕྱག་རྒྱ་ཆེན་པོ།** ^1-1-5-2-1-2-1-2-1-3-0

[Block 403]
ཕྱག་རྒྱ་ཆེན་པོ་ལ་གཉིས་ཏེ་ཆགས་བྲལ་ལྟ་བུ་དང་། ཆགས་ཅན་ལྟ་བུའོ། །

[Block 404 [HEADING]]
###### **ཆགས་བྲལ་ལྟ་བུ།** ^1-1-5-2-1-2-1-2-1-3-1-0

[Block 405]
དེ་ལ་ཆགས་བྲལ་ལྟ་བུ་དེ་ཉིད་མཆོག་གི་རྣམ་འཕྲུལ་ནི། དེ་ཡང་།

[Block 406 [VERSE]]
དངོས་པོ་ཀུན་ལ་ཁྱབ་པ་པོ། །
ཞེས་པ་ནི་དོན་སྐྱེ་མེད་ཀྱིས་ཁྱབ་པའོ། །
ལུས་ལ་ཡེ་ཤེས་ཆེན་པོ་གནས། །

[Block 407]
ཞེས་པ་ནི་ཤེས་བྱེད་ཀྱི་དོན་ཡང་དོན་དམ་པའི་ཡེ་ཤེས་སོ།[^149] །རྟོག་པ་ཐམས་ཅད་ཡང་དག་སྤངས། །ཞེས་པ་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་སྐྱེ་མེད་དུ་གོ་བའོ། །

[Block 408]
ལུས་གནས་ལུས་ལས་མ་སྐྱེས་ཞེས་པ་ནི་ཤེས་བྱ་ཡེ་ཤེས་དེ་ཉིད་ཀྱང་སྐྱེ་མེད་དུ་གཅིག་པར་གྱུར་པའོ། །

[Block 409 [HEADING]]
###### **ཆགས་ཅན་ལྟ་བུ།** ^1-1-5-2-1-2-1-2-1-3-2-0

[Block 410]
དེ་ལ་ཆགས་ཅན་ལྟ་བུ་ནི་གཉུག་མའི་ལུས་ཏེ་དེ་ཡང་ལུས་ཞེས་པ་ནི་གཉུག་མ་དེ་ཉིད་ལའོ། །

[Block 411]
ཡེ་ཤེས་ཆེན་པོ་ནི་ཟག་པ་མེད་པའི་ཡེ་ཤེས་སོ། །

[Block 412]
གནས་ཞེས་པ་ནི་ཞུ་བ་བསྡུས་པས་རྟག་པ་མི་འགྱུར་བར་གནས་པ་ཉིད་དོ། །

[Block 413]
རྟོག་པ་ཐམས་ཅད་ཡང་དག་སྤངས། །ཞེས་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོ་མཚོན་བྱེད་རང་རིག༌[^150]སྟེ། རྟོག་པ་རང་ཤུགས་སུ་གཅོད་པ་དང་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པའོ། །

[Block 414]
དངོས་པོ་ཀུན་ལ་ཁྱབ་ཅེས་པ་ནི་དབང་པོ་རང་སྣང་ལ་སྦྱར་བའམ། མཚོན་བྱ་ལྷན་སྐྱེས་སོ། །

[Block 415]
ལུས་གནས་ལུས་ལས་མ་སྐྱེས་པ་ནི་གཉུག་མའི་ལུས་ལ་གནས་ཀྱང་ཐ་མལ་གྱི་ལུས་ལས༌[^151]མ་སྐྱེས་པའམ།[^152] གསལ་བྱེད་ཀྱི་རྒྱུ་ཡིན་གྱི་སྐྱེད་བྱེད་ཀྱི་རྒྱུ་མ་ཡིན་པའོ། །

[Block 416 [HEADING]]
###### **འབྲས་བུ་ལམ་དུ་བྱས་པ།** ^1-1-5-2-1-2-1-2-2-0

[Block 417]
འབྲས་བུ༌[^153]ལམ་དུ་བྱས་པ་ནི་སྐུ་བཞི་སྟེ། ཚིག་དང་པོ་ལོངས་སྐུའོ། །

[Block 418]
ཚིག་གཉིས་པ་ནི་ཆོས་སྐུའོ། །

[Block 419]
གསུམ་པ་སྤྲུལ་སྐུའོ། །

[Block 420]
བཞི་པ་ནི་བདེ་བ་ཆེན་པོའི་སྐུའོ། །

[Block 421 [HEADING]]
###### **རྟེན་རྡོ་རྗེའི་ལུས་ལམ་དུ་བྱེད་པ།** ^1-1-5-2-1-2-2-0

[Block 422]
རྟེན་རྡོ་རྗེའི་ལུས་བསྟན་པ་ནི་ལུས་ལ་ཞེས་པ་ལ་སོགས་པ་སྟེ། རྡོ་རྗེ་སྙིང་པོས་གསོལ་པ་ཞེས་པ། ཀྱེ༌[^154]རྡོ་རྗེའི་ལུས་ལ་རྩ་དུ་ལགས། ཞེས་པ་ནི་དགྱེས་པའི་རྡོ་རྗེར་འབྲེལ་ལོ། །

[Block 423]
ཀུན་བརྟགས་ཀྱི་ལུས་ལ་ཀུན་བརྟགས་ཀྱི་རྩ་དུ་མཆིས་པ་དང་། གཞན་དབང་གི་ལུས་ལ་གཞན་དབང་གི་རྩ་དུ་མཆིས་པ་དང་། ཡོངས་གྲུབ་ཀྱི་ལུས་ལ་ཡོངས་གྲུབ་ཀྱི་རྩ་དུ་མཆིས་ཞེས་དགོངས་པའོ། །

[Block 424]
ལན་དུ་རྩ་སུམ་ཅུ་རྩ་གཉིས་ཏེ་ཕྱིར་ལེན༌[^155]བཏབ་སྟེ་ཀུན་བརྟགས་ཀྱི་ལུས་ལ་རྩ་སུམ་ཅུ་རྩ་གཉིས་གང་ཞེ་ན། མི་ཕྱེད་མ༌[^156]ཞེས་བྱ་བ་ལ་སོགས་པ་བྱང་ཆུབ་ཀྱི་སེམས་སུམ་ཅུ་རྩ་གཉིས་འབབ་པའོ་ཞེས་བྱ་བར་སྦྱར་ཏེ་རྣལ་འབྱོར་གྱི་ཀུན་རྫོབ་བོ། །

[Block 425]
ཀུན་བརྟགས་ཀྱི་ལུས་ལ་ཡང་སུམ་ཅུ་རྩ་གཉིས་ཏེ། ཡང་མི་ཕྱེད་མ་དང་ཕྲ་གཟུགས་མ༌[^157]ལ་སོགས་པ་སྟེ། ཁམས་དང་ཉེ་བའི་ཁམས་བསྐྱེད་པའོ། །
--- END BLOCKS ---
