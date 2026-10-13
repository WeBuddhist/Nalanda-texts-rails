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
[Block 106]
ལྔ་པ་རིམས་ནད་སེལ་བའི་སྒྲོལ་མའི་འཕྲིན་ལས་ནི། ཕྱག་འཚལ་ཉི་མ་ཟླ་བ་རྒྱས་པ་ལྟ་བུའི་སྤྱན་གཡས་པ། ཟླ་བ་རྒྱས་པ་ལྟ་བུའི་སྤྱན་གཡོན་པ་(ཅེས་,ཞེས་)གསུང་ཡང་། ཉི་མ་རྒྱས་པ་ལྟ་བུའི་ཁྲོ་མོའི་སྤྱན། ཟླ་བ་རྒྱས་པ་ལྟ་བུའི་ཞི་བའི་སྤྱན་གཉིས་པོ་ལ་འོད་རབ་ཏུ་གསལ་བ་འཕྲོ་བ་དང་། ངག་ཏུ་ཁྲོ་མོའི་སྔགས་ཧ་ར་གཉིས་བརྗོད། ཞི་བའི་སྔགས་ཏུ་ཏྟཱ་ར་ཡི་སྔགས་བརྗོད་པ་ཡིས་ཤིན་ཏུ་དྲག་པོའི་རིམས་ནད་སེལ་མ་ཉིད་དོ། འདི་ལ་དངོས་གྲུབ་འབྱུང་གནས་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 107 [HEADING]]
##### དྲུག་པ་གདོན་དང་རོ་ལངས་འཇོམས་པའི་འཕྲིན་ལས། ^2-2-3-6-0

[Block 108]
དྲུག་པ་གདོན་དང་རོ་ལངས་འཇོམས་པའི་འཕྲིན་ལས་ནི། ཕྱག་འཚལ་དེ་ཉིད་གསུམ་རྣམས་བཀོད་པའི། །ཞེས་པ་སྐུ་གསུང་ཐུགས་ཀྱི་དེ་ཉིད་དེ། སྐུའི་དེ་ཉིད་སྤྱི་བོར་ཨོཾ། གསུང་གི་དེ་ཉིད་མགྲིན་པར་ཨཱཿ ཐུགས་ཀྱི་དེ་ཉིད་ཐུགས་ཀར་ཧཱུཾ་རྣམས་བཀོད་པའི་མཐུ་བརྟན་པའི། དྲུག་ཉོན་མོངས་ཞི་བའི་མཐུ་དང་ཡང་ལྡན་མ། གཡོ་བའི་དུག་གདོན་དང་རོ་ལངས་གནོད་སྦྱིན་ཚོགས་རྣམས་འཇོམས་པ་ལ། རབ་མཆོག་ནི། ཏུ་རེ་སྒྲོལ་མ་ཉིད་ཡིན་ནོ། །

[Block 109]
འདི་ལ་ཡོངས་སུ་རྫོགས་བྱེད་སྒྲོལ་མ་ཞེས་འབྱུང་ངོ་། །

[Block 110 [HEADING]]
### གསུམ་པ་ཕན་ཡོན་བསྟན་པ། ^2-3-0

[Block 111 [HEADING]]
#### དང་པོ་ཕན་ཡོན་བསམ་པའི་ཁྱད་པར། ^2-3-1-0

[Block 112]
གསུམ་པ་ལ་ཕན་ཡོན་བསམ་པའི་ཁྱད་པར། དུས་ཀྱི་ཁྱད་པར། ཕན་ཡོན་དངོས་བཤད་པ། གྲངས་ཀྱི་སྒོ་ནས་ཕན་ཡོན་བསྡུས་ཏེ་བསྟན་པ་དང་བཞི། དང་པོ་ནི། ཞི་བ་དང་ཁྲོ་མོའི་རྩ་བའི་སྔགས་ཀྱི་བསྟོད་པ་ཉེར་གཅིག་པོ་འདི་དང་། སྒོ་གསུམ་གུས་པས་ཕྱག་འཚལ་བ་ནི་ཉི་ཤུ་རྩ་གཅིག ། ལྷ་མོ་སྒྲོལ་མ་ལ་གུས་པ་དང་ཡང་དག་པར་ལྡན་པས་ཏེ། ཁ་ཙམ་ཚིག་ཙམ་མིན་པར། རྩེ་གཅིག་པ་ཉིད་ཀྱི་བློ་ཤེས་རབ་དང་ལྡན་པ་གང་གིས་རབ་ཏུ་དད་པས་བརྗོད་པས།

[Block 113 [HEADING]]
#### གཉིས་པ་དུས། ^2-3-2-0

[Block 114]
(གཉིས་པ་) དུས་ནི། སྲོད་དང་ཐོ་རངས་མལ་ནས་ལངས་པར་བྱས་ནས། དྲན་པ་(ཅེས་,ཞེས་)པ། སྤྱིར་སྐུ་དང་། གསུང་སྔགས་དང་། བསྟོད་པ་དང་། ཁྱད་པར་སྲོད་ཀྱི་དུས་སུ་ཁྲོ་མོའི་ངང་། ཐོ་རངས་དུས་སུ་ཞི་བའི་སྐུ་སོགས་དྲན་པ་ཙམ་གྱིས་ཚེ་འདིའི་ནད་གདོན་དང་། དུས་མིན་འཆི་བ་ལ་སོགས་པ་བར་ཆད་ཀྱི་མི་འཇིགས་པ་ཐམས་ཅད་རབ་ཏུ་སྟེར་བ། ཕྱི་མར་ངན་འགྲོའི་རྒྱུ་སྡིག་པ་ཐམས་ཅད་རབ་ཏུ་ཞི་བས་ན། འབྲས་བུ་ངན་འགྲོ་ཐམས་ཅད་འཇོམས་པ་ཉིད་དོ། །

[Block 115 [HEADING]]
#### གསུམ་པ་ཕན་ཡོན། ^2-3-3-0

[Block 116]
(གསུམ་པ) ཕན་ཡོན་ནི། རྒྱལ་བ་བྱེ་བ་ཕྲག་བདུན་རྣམས་ཀྱིས་མྱུར་དུ་སྟེ། ཚེ་དེ་ཉིད་ལ་དབང་ནི། རིམ་པར་བསྐུལ་བར་འགྱུར་ལ། ཚེ་འདི་ལ་མི་དང་མི་མ་ཡིན་དབང་དུ་འདུ་བ་ལ་སོགས་པའི་ཐུན་མོང་གི་ཆེ་བའི་དངོས་གྲུབ་ཐོབ་ཅིང་། མཆོག་གི་དངོས་གྲུབ་སངས་རྒྱས་ཀྱི་གོ་འཕང་མཐར་ཐུག་དེར་འགྲོ། སངས་རྒྱས་ཀྱི་གོ་འཕང་དེའི་བར་དུ་(བཅོད་,གཅོད་)པའི་དུག་ནི་(དྭག་,དྭགས་)པོ་ཆེན་པོ་ལོག་ལྟ་ཉིད་དོ། །

[Block 117]
དེ་མཐར་ཕྱིན་པར་བྱེད་ཅིང་གཏན་ནས་གནས་པར་བྱེད་པ་ནི། གཏི་མུག་གི་ཆོས་ཀྱིས་ཆོས་ཀྱི་གནས་ལུགས་ལ་སྐུར་བ་བཏབ་པ་ཙམ། ཞེ་སྡང་དྲག་པོས་ཆོས་དང་ཆོས་སྨྲ་བ་ལ་ཞེ་སྡང་བའི་ལས་རྣམས་འཇོམས་ཞེས་པ་བརྟན་པའི་དུག་རྣམས་སེལ་བའོ། །

[Block 118]
གཞན་ཡང་གཡོ་བའི་དུག་འགྲོ་བ་ཁྱི་དྲུག་དང་། སྦྲུལ་དྲུག་གིས་ཟིན་པ་དང་། ཟོས་པ་དང་ནི་འཐུངས་པ་སྟེ། ཟས་(སྒོམ་,སྐོམ་)གྱི་དུག་ཉིད་ཀྱང་། ལྷ་མོའི་སྐུ་སོགས་དྲན་པ་ཙམ་གྱིས་རབ་ཏུ་སེལ་བ་ཉིད་ཐོབ་པ། སྡུག་བསྔལ་གྱི་རྒྱུ་སེལ་བའོ། །

[Block 119]
འབྲས་བུ་སྡུག་བསྔལ་དྲག་པོ་སེལ་བ་ནི། གདོན་དང་རིམས་དང་དུག་གིས་གཟིར་བ་སྟེ་སྐྱེ་བའི་སྡུག་བསྔལ་ཚོགས་ནི་རྣམ་པར་སྤོ་སྟེ། ཞེས་པ་རང་དོན་ཏོ། །

[Block 120]
གཞན་དོན་ནི། སེམས་ཅན་གཞན་པ་རྣམས་ལ་ཡང་ངོ་། །ཞེས་གཞན་གྱི་དོན་དུ་ཡང་གུས་པ་དང་ལྡན་པས་སྲོད་དང་ཐོ་རངས་ལངས་པར་བྱས་ཏེ། སྐུ་སོགས་ཡིད་ལ་དྲན་བཞིན་དུ་བརྗོད་ན་ཕན་ཡོན་གོང་བཞིན་དུ་ཐོབ་ཅེས་པའོ། །

[Block 121 [HEADING]]
#### བཞི་པ་གྲངས་ཀྱི་སྒོ་ནས་ཕན་ཡོན་བསྡུས་པ། ^2-3-4-0

[Block 122]
བཞི་པ་གྲངས་ཀྱི་སྒོ་ནས་ཕན་ཡོན་བསྡུས་པ་ནི། གཉིས་གསུམ་བདུན་དུ་མངོན་པར་བརྗོད་ན། ཞེས་པ། གྲགས་པའི་མཎྜལ་བཞི་མ་ལྟར་ཏེ། དེའི་དོན་ལ་སྙན་ངག་པ་འགའ་ཞིག །གཉིས་སུ་བརྗོད་ན་བུ་འདོད་པས་ནི་བུ་ཐོབ་འགྱུར་ཞིང་། གསུམ་དུ་བརྗོད་ན་ནོར་འདོད་པས་ནི་ནོར་རྣམས་ཉིད་ཐོབ། བདུན་དུ་བརྗོད་ན་འདོད་པ་ཐམས་ཅད་ཐོབ་པར་འགྱུར་ཏེ་ཞེས་ཟེར། སྤང་ལོས་ནི། གཉིས་གསུམ་ཞེས་པ་ལ། གཉིས་ནི། སྒྲུབ་པ་པོ་རྟེན་གྱི་གང་ཟག་གི་ཁྱད་པར་ཏེ། བློ་ལྡན་གང་གིས་ཞེས་པས། དབང་རྣོན་ཆོས་ཀྱི་རྗེས་འབྲངས་དང་། རབ་དད་ཅེས་པས་དབང་རྟུལ་དད་པའི་རྗེས་འབྲངས་བསྟན་ལ། གསུམ་ཞེས་པས་དུས་ཀྱི་ཁྱད་པར་བསྟན་ཏེ། སྲོད་དང་ཐོ་རངས་ལངས་པར་བྱས་ནས་ཞེས་པ་ནམ་ལངས་ནས་སྲོད་ཐུན་གྱི་བར་རོ། །

[Block 123]
བདུན་དུ་མངོན་པར་བརྗོད་ན། ཞེས་པ་གྲངས་ཀྱི་ཁྱད་པར་ཏེ། དུས་གསུམ་པོ་དེ་ལ་བདུན་བདུན་ཏེ། བདུན་གསུམ་ཉི་ཤུ་རྩ་གཅིག་བརྗོད་ན། མི་འཇིགས་པ་ཐམས་ཅད་སྟེར་བ་ལ་སོགས་པ་འདོད་པ་ཐམས་ཅད་ཐོབ་པར་འགྱུར་ཏེ། དེ་ཐོབ་པ་ལ་ཡང་བར་ཆད་བྱེད་པར་མ་ནུས་པས། བགེགས་རྣམས་མེད་ཅིང་དེའི་གཉེན་པོ་རེ་རེས་སྤང་བྱ་རེ་རེ་འཇོམས་པར་འགྱུར་ཅེས་གསུངས་སོ། །

[Block 124]
རིན་པོ་ཆེ་བུ་སྟོན་གྱིས་ནི། གཉིས་ཞེས་བྱ་བ་ཉིན་མཚན་གྱི་ཆ་གཉིས། གསུམ་ཞེས་པ་དེ་རེ་རེ་ལ་ཐུན་གསུམ་གསུམ་སྟེ། ཉིན་མོ་ལ་སྔ་དྲོ། ཉིན་གུང་རྒོངས་ཐུན་གསུམ། མཚན་མོ་ལ་སྲོད་གུང་ཐུན། ཐོ་རངས་ཏེ་ཐུན་དྲུག་པོ་འདི་ལ། བདུན་བདུན་ཏེ་བཞི་བཅུ་རྩ་གཉིས་ཉིན་མཚན་ཕྲུགས་གཅིག་ལ་བརྗོད་ན། ཕན་ཡོན་དེ་རྣམས་འབྱུང་བ་ཡིན་གསུང་།

[Block 125 [HEADING]]
## མཇུག་བྱང། ^a-0

[Block 126 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 127]
རྗེ་བཙུན་མ་འཕགས་མ་སྒྲོལ་མ་ལ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་རྣམ་པར་སྣང་མཛད་ཀྱིས་བསྟོད་པ་རྣམ་པར་དབྱེ་བ་རྫོགས་སོ།། ༎
--- END BLOCKS ---
