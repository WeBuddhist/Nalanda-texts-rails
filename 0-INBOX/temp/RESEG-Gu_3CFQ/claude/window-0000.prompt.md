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
[Block 1 [HEADING]]
### ༄། །བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་ཀྱི་ལེའུའི་འགྲེལ་པ་བཞུགས་སོ། །

[Block 2]
༄༅༅། །བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་ཀྱི་ལེའུ་བཤད་པ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །

[Block 3 [HEADING]]
## ཚུལ་ཁྲིམས་ཀྱི་རང་བཞིན་ཡོན་ཏན་བཞི་དང་ལྡན་པ། ^1-0

[Block 4]
ཚུལ་ཁྲིམས་ཀྱི་རང་བཞིན་ཡོན་ཏན་བཞི་དང་ལྡན་པ་དེ་ནི་དགེ་བར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ཇི་ལྟ་བུ་ཞེ་ན། དེ་ལས་བརྩམས་ཏེ། བདག་ལ་ཕན་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 5]
དེ་ལ་ཕན་པ༌[^1]ཞེས་བྱ་བ་ནི་དགེ་བ་སྤྱོད་པའོ། །

[Block 6]
བདེ་བ་ནི་གནོད་པ་མེད་པའོ། །

[Block 7]
སྙིང་བརྩེ་བ༌[^2]ནི་འདི་ལྟར་ལ་ལ་སྤྱོད་པ་དགེ་བ་དང་གནོད་པ་མེད་པས་ཕ་རོལ་རྣམས་ལ་སྙིང་བརྩེ་བར་བྱེད་པ་ལྟ་བུའོ། །

[Block 8]
དོན་ཅེས་བྱ་བ་ནི་དོན་དུ་གཉེར་བ་དང་དོན་དང་ལྡན༌[^3]པ་སྟེ། འདོད་པ་དང་ཁ་ན་མ་ཐོ་བ་མེད་པ་གང་ཡིན་པའོ། །

[Block 9]
ཕན་པ་དང་བདེ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྤྱོད་པ་དགེ་བ་དང་། གནོད་པ་མེད་པ༌[^4]ལ་གནས་པའོ། །

[Block 10]
མི་ཞེས་བྱ་བ་ནི་རྒྱལ་རིགས་ལ་སོགས་པ་སྟེ། དེ་དག་ཕལ་ཆེར་ལ་སངས་རྒྱས་འབྱུང་བ༌[^5]དང་། ཆོས་ལེགས་པར་གསུངས་པ་དང་། དགེ་འདུན་ལེགས་པར་སྒྲུབ་པ་རྣམས་ཀྱིས་ཤས་ཆེར་ཕན་པ་དང་། བདེ་བར་འགྱུར་ལ། དེ་དག་ཀྱང་བདག་ཉིད་ལ་ཕན་པ་དང་བདེ་བར་བྱས་ནས། འཇིག་རྟེན་ལ་སྙིང་བརྩེ་བ༌[^6]སྟེ། དེ་དག་གཞན་དག་ལ་འདི་སྙམ་དུ་ཕན་པ་དང་བདེ་བ་དང་ལྡན་པར་གྱུར་ཀྱང་ཅི་མ་རུང་སྙམ་དུ་སེམས་སོ། །

[Block 11]
གཞན་དག་ཀྱང་འདི་སྙམ་དུ་བདག་ཅག༌[^7]ཀྱང་དེ་ལྟར༌[^8]གྱུར་ཀྱང་ཅི་མ་རུང་སྙམ་དུ་སེམས་ཏེ། དེ་ལྟ༌[^9]བས་ན་དོན་དང་ཕན་པ་དང་བདེ་བའི་ཕྱིར་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 12]
ལྷ་དང་མི་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི་དེ་དག་གི་དོན་རྟོགས་པར་བྱ་བ་དང་བསྒྲུབ་པར༌[^10]མི་ནུས་པའི་ཕྱིར་ཏེ། བདག་ལ་ཕན་པ་དང་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྣམས་ཀྱི་དོན་ནི་དེ་དག་ཡིན་ནོ། །

[Block 13]
དེ་ཡང་ཁྱིམ་པ་དང་རབ་ཏུ་བྱུང་བའི་ཕྱོགས་ལ་ཅི་རིགས་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། ཁྱིམ་པའི་ཕྱོགས་ནི་དགེ་བསྙེན་གྱི་ཚུལ་ཁྲིམས་དང་། དགེ་བསྙེན་མའི་ཚུལ་ཁྲིམས་སོ། །

[Block 14]
གཞན་ནི་རབ་ཏུ་བྱུང་བའི་ཕྱོགས་ལ་བརྟེན་པའོ། །

[Block 15]
འདི་ལ་བྱང་ཆུབ་སེམས་དཔའི་ཚུལ་ཁྲིམས་ལ་བརྟེན་ཅིང་ཞེས་བྱ་བ་མན་ཆད། དགེ་བའི་ཆོས་རྣམས་བསྒྲུབ་པ༌[^11]དང་སྲུང་བ་དང་རྣམ་པར་འཕེལ་བར་བྱེད་པའི་ཞེས་བྱ་བ་ཡན་ཆད་ནི་ལུས་དང་ངག་དང་ཡིད་གསུམ་ཆར་དང་། གཉིས་ཀྱིས་ཀྱང་བྱེད་དེ་ཅི་རིགས་པར་བྱའོ། །

[Block 16 [HEADING]]
## སེམས་ཅན་གྱི་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་རྣམ་པ་བཅུ་གཅིག། ^2-0

[Block 17]
སེམས་ཅན་གྱི་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་རྣམ་པ་བཅུ་གཅིག་ནི་མདོར་དོན་དུ་ན་སེམས་ཅན་རྣམ་པ་གསུམ་སྟེ། ཐ་མལ་པར་གནས་པ་རྣམས་དང་། ཞུགས་པ་རྣམས་དང་། ཞེ་འགྲས་པ་རྣམས་སོ། །

[Block 18]
དེ་ལ་ཐ་མལ་པ་གནས་པ་རྣམས༌[^12]ལས་བརྩམས་ཏེ་རང་གི་དོན་བྱེད་པ་རྣམ་པ་བདུན་ཡོད་པ་ལ་ཕན་འདོགས་པ་ལན་དུ་ཕན་འདོགས་པར་འདོད་པ་རྣམས་རྣམ་པ་གསུམ་སྟེ། ལུས་འཇིག་ཏུ་དོགས་པས་འཇིགས་པ་རྣམས་དང་། སྡུག་བསྔལ་ལ་གནས་པ་རྣམས་དང་། ཡོ་བྱད་མེད་པ་རྣམས་སོ། །

[Block 19]
ཞུགས་པ་དག་ནི་བརྟེན༌[^13]ཏེ་གནས་པ་རྣམས་དང་། ཆོས་མཐུན་པ་གཞན་རྣམས་དང་། ཡང་དག་པར་ཞུགས་པ་རྣམས་དང་ལོག་པར་ཞུགས་པ་རྣམས་སོ། །

[Block 20]
ཞེ་འགྲས་པ་དག་ནི་ཐ་མ་རྣམས་སོ། །

[Block 21]
དཔེར་ན་རྩྭའམ་མི་གཙང་བ་ལ་ཇི་ལྟ་བ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་འདོད་པ་ལ་རྣམ་པ་གཉིས་ཡོད་དེ། དངོས་པོའི་འདོད་པ་རྣམས་དང་། ཉོན་མོངས་པའི་འདོད་པ་རྣམས་སོ། །

[Block 22]
དེ་ལ་དངོས་པོའི་འདོད་པ་རྣམས་ནི་འདོད་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 23]
ཉོན་མོངས་པའི་འདོད་པ་རྣམས་ནི་འདོད་པའི་ཕྱིར་འདོད་པ་ཞེས་བྱ་སྟེ། འདིར་ནི༌[^14]དངོས་པོའི་འདོད་པ་རྣམས་ལ་བྱའོ། །

[Block 24]
དེ་དག་ཀྱང་རྣམ་པ་གཉིས་ཏེ། འཁྲིག་པའི་དངོས་པོའི་འདོད་པ་རྣམས་དང་། དེ་མ་ཡིན་པའི་དངོས་པོའི་འདོད་པ་རྣམས་ཏེ། དེ་མ་ཡིན་པའི་དངོས་པོའི་འདོད་པ་རྣམས་ལ་ནི་དཔེར་ན་རྩྭ་ལ་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 25]
དངོས་པོའི་འདོད་པ་རྣམས་ལ་ནི་དཔེར་ན་མི་གཙང་བ་ལ་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 26]
ཐ་ཆད་རྣམས་ཞེས་བྱ་བ་ནི་དངོས་པོ་བཞིན་དུ་རྣམ་པ་གཉིས་སོ། །

[Block 27]
མིའི་འདོད་པ་ཐམས་ཅད་ཀྱི་མཆོག་འཁོར་ལོས་སྒྱུར་བའི༌[^15]འདོད་པ་རྣམས་ལ་མི་ལྟ་བ་ནི་ཚེ་འདི་ལའོ། །

[Block 28]
མངོན་པར་དགའ་བ་མ་ཡིན་པ་ནི་མ་འོངས་པ་རྣམས་ལ་སྟེ། མ་འོངས་པ་ནི་ཚེ་ཕྱི་མ་ལ། མ་འོངས་པ་དག་ན་ཡང་བདུད་ཀྱི་གནས་སུ་གཏོགས་པའི་འདོད་པ་རྣམས་ལའོ། །

[Block 29]
དེ་དག་གི་དོན་དུ་སྨོན་ལམ་བཏབ་ནས་ཚངས་པར་སྤྱད་པ་སྤྱོད་པར་མི་བྱེད་པ་ཅིའི་ཕྱིར་ཞེ་ན། ཆེན་པོ་སྣ་ཚོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 30]
ཁ་ཟས་ཀྱི་སྐྱུགས་པ་འདྲ་བར་ཡང་དག་པར་ཤེས་རབ་ཀྱིས་མཐོང་བ༌[^16]སྟེ་ཞེས་བྱ་བ་ནི་ཁ་ཟས་ཀྱི་སྐྱུགས་པ་དང་འདོད་པ་གཉིས་སྔར་ཡོངས་སུ་སྤངས་པར་འདྲ་བའི་ཕྱིར་རོ། །

[Block 31]
སྡོམ་པའི་ཚུལ་ཁྲིམས་ལ་གནས་པ་ཞེས་བྱ་བ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ལ་གནས་པར་སྟོན་ཏེ། དེ་ལྟར་ན་བསྡམས་པའི་ཚུལ་ཁྲིམས་ཅན༌[^17]ནོ། །

[Block 32]
དེ་ལ་ལེགས་པར་བསྡམས་པའི་ཚུལ་ཁྲིམས་ཅན་ཇི་ལྟ་བུ་ཞེ་ན། བསྡམས་སུ་ཟིན་ཀྱང་རྒྱུ་རྣམ་པ༌[^18]དྲུག་གིས་ལེགས་པར་བསྡམས་པ་མ་ཡིན་ཏེ། དེ་ཙམ་གྱིས་ཆོག་པར་འཛིན་པ་དང་། ཀུན་ནས་སློང་བ་དང་བཅས་པའི་ངག་ཡོངས་སུ་མ་དག་པ་དང༌[^19]བདག་ལ་ཁྱད་དུ་གསོད་པ་དང་། འཁོར་ཡོངས་སུ་མི་འཛིན་པ་དང་། ཉེས་པ་བྱུང་བ་ལ་རྣམ་པ་ཐམས་ཅད་དུ་ཆོས་བཞིན་དུ་ཕྱིར་འཆོས་པ་མེད་པ་དང་། ཆོ་ག་དང༌[^20]འཚོ་བ་ཡོངས་སུ་མ་དག་པའོ། །

[Block 33]
དེ་ལ་རྒྱུ་གཉིས་ཀྱིས་ན་དེ་ཙམ་གྱིས༌[^21]ཆོག་པར་འཛིན་པར་འགྱུར་ཏེ། ངག་དང་ལུས་གཉིས་བསྡམས་པ་ཡོད་དུ་ཟིན་ཀྱང་དུས་གསུམ་གྱིས་འདོད་པ་རྣམས་ལ་སེམས་མ་བསྡམས་པའི་ཕྱིར་དང་། དེ་བསྡམས་སུ་ཟིན་ཀྱང་ཚུལ་ཁྲིམས་ལ་གནས་ནས་ཏིང་ངེ་འཛིན་སྒྲུབ་མི་འདོད་པའི་ཕྱིར་ཏེ། དེ་ལྟར་ན་རྒྱུ་གཉིས་ཀྱིས་དེ་ཙམ་གྱིས་ཆོག་པར་འཛིན་པ་ཡིན་ནོ། །

[Block 34]
ཀུན་ནས་སློང་བ་དང་བཅས་པའི་ངག་ཡོངས་སུ་མ་དག་པ་ཇི་ལྟ་བུ་ཞེ་ན། ངག་ཀུན་ནས་སློང་བ་ནི་རྟོག་པ་དང་དཔྱོད་པ་དག་ཡིན་ཏེ། བརྟགས་ཤིང་དཔྱད་ནས་ཚིག་ཏུ་སྨྲ་བའོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 35]
ངག་རྣམ་པར་དག་པ་གང་ཡིན༌[^22]ཞེ་ན། བརྫུན་དུ་སྨྲ་བ་ལ་སོགས་པ་ངག་གི་ཉེས་པའི་གཉེན་པོ་བདེན་པ་ལ་སོགས་པའི་ངག་གི་ལས་ཡོངས་སུ་དག་པ་སྟེ། དེ་མེད་པས་ན་ངག་བསྡམས་སུ་ཟིན་ཀྱང་ལེགས་པར་བསྡམས་པ་མ་ཡིན་ནོ། །

[Block 36]
རྟོག་པ༌[^23]རྣམ་པར་དག་པ་གང་ཞེ་ན། འདོད་པའི་རྟོག་པ་ལ་སོགས་པའི་གཉེན་པོ་མི་སྡུག་པ་ལ་སོགས་པའི་རྟོག་པ༌[^24]དེ་ནི་རྣམ་པར་དག་པ་སྟེ། དེ་མེད་པས་ན༌[^25]རྟོག་པ་ཡོངས་སུ་དག་པའོ། །

[Block 37]
བདག་ལ་ཁྱད་དུ་གསོད་པ་ལས་ནི་བརྟུན་པའི་བརྩོན་འགྲུས་ཀྱིས་བསླབ་པའི་གཞི་རྣམས་ལ༌[^26]ལེགས་པར་ནན་ཏན་མི་བྱེད་དེ། དེའི་གཉེན་པོ་བདག་ལ་ཁྱད་དུ་མི་གསོད་པ་ལས་ནི་ས་ཆེན་པོ་ལ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པའི་གཞི་དཀའ་བ་ཐོབ་པས་སེམས་ཞུམ་པ་མེད་དོ།[^27] །བརྟུན་པའི་བརྩོན་འགྲུས་ཀྱིས་ནན་ཏན་བྱེད་དོ། །

[Block 38]
འཁོར་ཡོངས་སུ་མི་འཛིན་ཞེས་བྱ་བ་ལ་འདིར་ཚུལ་ཁྲིམས་ཀྱི་འཁོར་ནི་བཟོད་པ་སྟེ། དེ་མེད་ན་བསྡམས་སུ་ཟིན་ཀྱང་ལེགས་པར་བསྡམས་པ་མ་ཡིན་ཏེ། ཉེས་པའི་གནས་རྒྱང་མ་བསྲིངས་པའི་ཕྱིར་རོ། །

[Block 39]
ཉེས་པ༌[^28]བྱུང་བ་ལ་རྣམ་པ་ཐམས་ཅད་དུ་ཆོས་བཞིན་དུ་ཕྱིར་འཆོས་པ་མེད་པ་ཇི་ལྟ་བུ་ཞེ་ན། སྔ་ནས་བྱ་བ་དང་ལྷན་ཅིག་རྗེས་སུ་སྤྱོད་པའི༌[^29]བག་ཡོད་པ་དང་། སྔོན་གྱི་མཐའ་དང་ལྡན་པ་དང་། ཕྱི་མའི་མཐའ་དང་ལྡན་པ་དང་། དབུས་ཀྱི་མཐའ་དང་ལྡན་པའི་བག་ཡོད་པ་དང་མི་ལྡན་པའི་ཕྱིར་བསྡམས་སུ་ཟིན་ཀྱང་ལེགས་པར་བསྡམས་པ་མ་ཡིན་ནོ། །

[Block 40]
ཆོ་ག་དང་འཚོ་བ་མ་དག་པ་ནི་རྣམ་པ་ལྔ་ལྔ་པོ་དག་གི༌[^30]རྣམ་པ་རིལ་གྱིས་མེད་པའི་ཕྱིར་དེ་གཉིས༌[^31]བསྡམས་སུ་ཟིན་ཀྱང་ལེགས་པར་བསྡམས་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
