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
[Block 36]
རྣམ་པར་རོལ་ཞེས་བྱ་བ་ནི་རྣམ་པར་སྤྲུལ་བར་བྱའོ།།

[Block 37]
རྣམ་པར་འཕྲུལ་ཞེས་བྱ་བ་ནི་སྤྲུལ་བར་བྱེད་པའོ།།

[Block 38]
རྡོ་རྗེ་གསུམ་པོ་དམ་ཚིག་མཆོག།

[Block 39]
ཅེས་བྱ་བ་ནི་བྷ་གའོ། །

[Block 40]
ཡེ་ཤེས་དེ་བཞིན་གཤེགས་པ་ཀུན།།ཞེས་བྱ་བ་ནས། འགྲོ་སྙིང་རྣམ་དག་ཅེས་བྱ་བ་ནི་བྷ་གའི་ཁྱད་པར་རོ།།

[Block 41]
ནམ་མཁའི་སྐབས་འདི་ཉིད་ཅེས་བྱ་བ་ནི་ཆོས་ཀྱི་འབྱུང་གནས་ཏེ། རང་བཞིན་རྣམས༌[^9]རང་བཞིན་མེད་པ་གནས་གཞིར་གྱུར་པ་ཤེས་རབ་ཀྱི་བྷ་གའོ།།

[Block 42]
སེམས་ཅན་ཐམས་ཅད་དཔལ་རྡོ་རྗེ་སེམས་དཔའ་བཞུགས་པས་བཅུག་ནས་རྡོ་རྗེ་སེམས་དཔའ་ཉིད་ཐོབ་པའོ་ཞེས་བྱ་བ་ལ། སེམས་ཅན་ཐམས་ཅད་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་དོ།།

[Block 43]
དཔལ་རྡོ་རྗེ་སེམས་དཔའ་བཞུགས༌[^10]ཞེས་བྱ་བ་ནི་དབང་བསྐུར་བའི་ཡེ་ཤེས་བྱིན་པས་སོ།།

[Block 44]
བཅུག་པས་ཞེས་བྱ་བ་ནི་གཉིས་སུ་མེད་པའི་སེམས་སུ་འཇུག་པས་བདེ་བ་དང་ཡིད་བདེ་བ་ཐོབ་པར་གྱུར་པའོ།།

[Block 45]
ཐབས་ཀྱི་ཡེ་ཤེས་ཤར་བས་སོ།།

[Block 46]
ཞེས་བྱ་བ་ནི་སྣང་བའི་ཡེ་ཤེས་ཤར་བས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ།།

[Block 47]
སེམས་དཔའ་གསུམ་གྱི་མཐར་ཐུག་པ་ཞེས་བྱ་བ་ནི་དམ་ཚིག་སེམས་དཔའ་དང་། ཡེ་ཤེས་སེམས་དཔའ་དང་། ཏིང་ངེ་འཛིན་སེམས་དཔའི་མཐར་ཐུག་པའོ།།

[Block 48]
ཉོན་མོངས་པ་ལྔ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་དང་། ཞེ་སྡང་དང་། གཏི་མུག་དང་། ང་རྒྱལ་དང་། ཕྲག་དོག་གོ།།

[Block 49]
རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ནི་ཟུང་དུ་འཇུག་པའོ།།

[Block 50]
ཁམས་ཕྲ་བ་ནི་རླུང་གི་ཁམས་སོ།།

[Block 51]
དེས་ཐབས་ཀྱི་ཡེ་ཤེས་གཞོམ་དུ་མེད་པའི་ཐིག་ལེ་དྲངས་པའི་གླེང་གཞི་དང་པོའོ།།

[Block 52]
བཙུན་མོ་དང་འཁོར་གྱི་ནང་ནས་ངེས་པར་བྱུང་བར་གྱུར་པ་ནི་གླེང་གཞི་གཉིས་པའོ།།

[Block 53]
རབ་ཏུ་བྱུང་བ་ནི་གླེང་གཞི་གསུམ་པའོ།།

[Block 54]
རྡོ་རྗེའི་གདན་ལ་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན༌[^11]གྱིས་ཞུགས་པ༌[^12]ནི་གླེང་གཞི་བཞི་པའོ།།

[Block 55]
དེ་ནི་གླེང་གཞིའི་དབྱེ་བ་རྣམས་སོ།།

[Block 56]
རྡོ་རྗེ་ལ་སོགས་བཟུང་བ་ནི།།ཞེས་བྱ་བའི་ཆོས་ཀྱི་འཁོར་ལོ་རབ་ཏུ་བསྐོར་བ་ལ་བྱ་བ་ཡིན་ནོ།།

[Block 57]
བྷ་ག་ལ་བཞུགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་དང་པོར་ཕྱི་རོལ་གྱི་དཀྱིལ་འཁོར་གྱི་གཟུགས་ལ་སོགས་པའི་འཁོར་རྣམས་ཉིད་ཀྱི་སྐུ་ལ་རབ་ཏུ་བཅུག་པས་མིག་ལ་སོགས་པ་རྣམས་ལ་ཐིམ་ནས་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུར་གནས་པ་ལས་བྱང་ཆུབ་ཀྱི་སེམས་མཆོག་ཏུ་དགའ་བའི་རང་བཞིན་དུ་གྱུར་ནས། ཡུམ་གྱི་སྐྱེ་གནས་སུ་བྱུང་བ་ནི་བྷ་ག་ལ་བཞུགས་སོ་ཞེས་བྱ་བའི་དོན་ཡིན་ནོ།།

[Block 58]
དེ་ནས་ནི༌[^13]ནུར་ནུར་པོ།།དེ་ནས་མེར་མེར་པོ་ལ་སོགས་པའོ།།

[Block 59]
དེ་ནས་ཟླ་བ་བཅུ་ལ་སོགས་པའི་རིམ་པས་མིག་ལ་སོགས་པའི་དབང་པོ་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ།།

[Block 60]
དེ་ནས་སྐྱེ༌[^14]གནས་ཀྱི་སྒོ་ཁྱད་པར་ཅན་ནས། ཕྱི་རོལ་དུ་གཤེགས་ཏེ་ཡུལ་དང་ཡུལ་ཅན་གྱི་གཟུགས་ལ་སོགས་པར་སྤྲུལ་པ་ནི་འཁོར་ཕུན་སུམ་ཚོགས་པར་གྱུར་པ་ཡིན་ནོ།།

[Block 61]
འདི་ལྟ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའི་དོན་ནི་བཙུན་མོ་དང་ལྡན་པར་བཞུགས་པ་ནི་དམ་ཚིག་གི་ཕྱག་རྒྱའོ།།

[Block 62 [VERSE]]
སྔགས་ཀྱི་ཡི་གེ་ནི་ཆོས་ཀྱི་ཕྱག་རྒྱའོ། །
མཚན་ཐམས་ཅད་དང་ལྡན་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོའོ། །
དེས་འགྲོ་བའི་དོན་བྱེད་པ་ནི་ལས་ཀྱི་ཕྱག་རྒྱའོ། །

[Block 63]
ཆོས་སྟོན་པའི༌[^15]དུས་ན་ཕྱག་རྒྱ་དེ་དག་དང་ལྡན་པ་པོ་ཕྱག་གཉིས་པ་ལ་སོགས་པའི་རིམ་པས་སྲུང་བའི༌[^16]འཁོར་ལོ་མདུན༌[^17]དུ་དྲན་པར་མཛད་པ་དང་། དེ་ནས་ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་བདག་ཉིད་འཁོར་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པར་གྱུར་ནས། བུད་མེད་ཕུན་སུམ་ཚོགས་པ་ལ༌[^18]མཆོད་པ་མཛད་པའི་ཚུལ་གྱིས་གདུལ་བྱ་འདོད་ཆགས་ཅན་རྣམས་ཀྱི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ།།

[Block 64]
ལྷ་དེ་རྣམས་སོ་སོའི་གདན་དང་ལྡན་པའི་གནས་གཞལ་ཡས་ཁང་བརྩེགས་པ་བསྟན་པའི་ཕྱིར། དེ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ།།

[Block 65]
དེ་ནས་དཀྱིལ་འཁོར་པ་རྣམས་ཉིད༌[^19]ཀྱི་སྙིང་ག་ལ་སོགས་པའི་ཕུང་པོ་ལ་སོགས་པའི་ངོ་བོར་ཞུགས་ཏེ་འོད་གསལ་བར་གནས་པ་ལ། ཨོཾ་ཤཱུ་ནྱ་ཏཱ་ཞེས་བྱ་བའི་སྔགས་ཀྱི་བྱིན་གྱིས་བརླབ་པོ།།དེའི་དེ་མ་ཐག་པར་ཉི་མ་དང་། ཟླ་བ་དང་པདྨ་དང་། ཡི་གེ་གསུམ་དང་། དེ་དག་ཞུ་བའི་ཟླ་བ་ལ་སེམས་ཅན་རྣམས་ཞུགས་པ༌[^20]ལ། ཨོཾ་དྷརྨྨཱ་དྷཱ་ཏུ་སྭ་བྷཱ་ཝ་ཞེས་པ་ལ་སོགས་པའི་རིམ་པས་རྡོ་རྗེ་འཛིན་པ་སེམས་དཔའ་གསུམ་གྱི༌[^21]མཐར་ཐུག་པའི་བར་དུ་བསམ་པར་བྱའོ།།

[Block 66]
དེ་ནས་ནམ་མཁའི་དབྱིངས་ནི་ཐམས་ཅད་ཅེས་བྱ་བ་ལ་སོགས་པས་ནི་རིགས་ལྔ་དང་ལྡན་པའི་ཤེས་རབ་ཀྱི་པདྨར་བྱང་ཆུབ་ཀྱི་སེམས་སྤྲོས་པས་གང་བའོ།།

[Block 67]
སེམས་ཅན་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཏེ། རྡོ་རྗེ་འཛིན་པའི་དཀྱིལ་འཁོར་པ་རྣམས་ཀྱི་དབྱེ་བ༌[^22]དང་ཡིད་བདེ་བ་ཐོབ་པར་གྱུར་པའོ།།

[Block 68]
དེ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཕྱུང་ནས་རྗེས་སུ་ཞུགས་པས་ཞལ་གསུམ་པའི་རྣམ་པ་ལྟ་བུ་ལ་སོགས་པར་རྡོ་རྗེ་འཛིན་པའི་གཟུགས་སུ་སྣང་བར་གྱུར་ཏོ།།

[Block 69]
དེ་ནས་སེམས་ཅན་རྣམས་ཀྱི་སྐལ་བ་ཇི་ལྟ་བ་བཞིན་དུ་མཁྱེན་ནས་སྟོན་པའི་རིམ་པ་ཇི་ལྟ་བུར་བཤད་པ་བཞིན་དུ་སྟོན་པ་ཡིན་ནོ།།

[Block 70]
དེ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་བླ་མ་ལ་སློབ་མ་རྣམས་ཀྱིས་གསོལ་བ་བཏབ་ནས་བླངས་ནས་འབྲས་བུ་ངེས་པས་ན་བསླབ་པ་དེ་ལ་གནས་པར་བྱ་བའི་ཕྱིར། དེ་བཞིན་གཤེགས་པ་རྡོ་རྗེ་འཛིན་པ༌[^23]ཉིད་ལ་ཉིད་གསོལ་བ་འདེབས་པར་བསྟན་པ་ཡིན་ནོ།།

[Block 71]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་དང་པོའི་དཀའ་བ་བཏུས་ཏེ་བཤད་པའོ།།།།

[Block 72 [HEADING]]
## ལེའུ་གཉིས་པ། ^2-0

[Block 73]
རྒྱུ་དང་འབྲས་བུའི་ཉེ་བར་གདགས་པ་ཞེས་བྱ་བའི་སྐུ་དང་གསུང་དང་ཐུགས་རྣམས་ཀྱི་རང་གི་ངོ་བོ་དབྱེར་མི་ཕྱེད་པའི་བྱང་ཆུབ་ཀྱི་སེམས་གང་ཡིན་པ་དེ་ནི༌[^24]རྒྱུ་ཡིན་ལ། དེས་རྡོ་རྗེ་འཛིན་པ་མཆོག་ལ་ཉེ་བར་སྤྱོད་པ་ནི་འབྲས་བུའོ།།

[Block 74]
སྲོག༌[^25]ལས་ཞེས་བྱ་བ་ནི་རླུང་ལས་ཞོན་པའི་རྣམ་པར་ཤེས་པ་རྨི་ལམ་ལྟ་བུར་སྣང་བའོ།།

[Block 75]
ཁམས་གསུམ་གྱི་རྣམ་པར་གནས་པ་ནི། ཁམས་གསུམ་པ་དེ་ཉིད་རླུང་རྨི་ལམ་ལྟ་བུར་གནས་པ་སྟེ། གནས་པ་ཞེས་པ༌[^26]འདི་ཉིད་ཀྱང་ཁམས་གསུམ་པར་སྐྱེས་པའོ།།
--- END BLOCKS ---
