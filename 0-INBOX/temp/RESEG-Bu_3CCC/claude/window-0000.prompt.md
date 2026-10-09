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
## ༄༅། །དབུ་མ་རྩ་བའི་འགྲེལ་པ་བུདྡྷ་པཱ་ལི་ཏ།

[Block 2]
༄༅༅། །རྒྱ་གར་སྐད་དུ། བུདྡྷ་པཱ་ལི་ཏ་མཱུ་ལ་མ་དྷྱ་མ་ཀ་བྲྀཏྟི། བོད་སྐད་དུ། དབུ་མ་རྩ་བའི་འགྲེལ་པ་བུདྡྷ་པཱ་ལི་ཏ། བམ་པོ་དང་པོ།

[Block 3 [HEADING]]
## མཆོད་བརྗོད། ^I-0

[Block 4]
དཀོན་མཆོག་གསུམ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 5]
འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 6]
སློབ་དཔོན་འཕགས་པ་ཀླུ་སྒྲུབ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 7]
སློབ་དཔོན་བཙུན་པ་བུད་དྷ་པཱ་ལི་ཏ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 8 [HEADING]]
## རྐྱེན་བརྟག་པ། ^1-0

[Block 9]
འདི་ལྟར་སློབ་དཔོན་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྗེས་སུ་སྟོན་པར་བཞེད་པས། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཟབ་མོ་ཉིད་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་གཟིགས་པས་ངོ་མཚར་དུ་གྱུར་པའི་ཐུགས་དང་ལྡན་པ། དད་པ་ལས་བྱུང་བའི་མཆི་མ་དཀྲུག་ཅེས༌[^1]མཛད་པའི་སྤྱན་མངའ་བ། སྐུའི་སྤུ་ཟིང་ཞེས་མཛད་པ་དང་ལྡན་པས་ཐལ་མོ་སྦྱར་བ་དབུར་བཞག་སྟེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་ཆོས་ཀྱི་སྐུའོ་ཞེས་དོན་དམ་པ་སྟོན་པའི་ཚིགས་སུ་བཅད་པ་འདི་བརྗོད་པས་མདུན་དུ༌[^2]འདུག་པ་དང་འདྲ་བར་བཞག་ནས། དེ་བཞིན་གཤེགས་པ་བླ་མ་དམ་པ་ལ།

[Block 10 [VERSE]]
གང་གིས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་། །
འགག་པ་མེད་པ་སྐྱེ་མེད་པ། །
ཆད་པ་མེད་པ་རྟག་མེད་པ། །
འོང་བ་མེད་པ་འགྲོ་མེད་པ། །

[Block 11 [VERSE]]
ཐ་དད་དོན་མིན་དོན་གཅིག་མིན། །
སྤྲོས་པ་ཉེར་ཞི་ཞི་བསྟན་པ། །
རྫོགས་པའི་སངས་རྒྱས་སྨྲ་རྣམས་ཀྱི། །
དམ་པ་དེ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 12]
ཞེས་རྒྱུ་སྔ་ན་ཡོད་པའི་ཕྱག་བཞེས་པ་མཛད་དེ། གང་གིས་དབང་ཕྱུག་དང་དུས་དང་རྡུལ་ཕྲན་དང་རང་བཞིན་དང་ངོ་བོ་ཉིད་ལ་སོགས་པར་སྨྲ་བ་སྤྲོས་པ་ཐིབས་པོར་འཁྱམས་པའི་འཇིག་རྟེན་ལ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་བྱ་བ་དོན་དམ་པའི་བདེན་པ་མཆོག་ཏུ་ཟབ་པ། འགག་པ་མེད་པ་སྐྱེ་བ་མེད་པ། ཆད་པ་མེད་པ་རྟག་པ་མེད་པ། འོང་བ་མེད་པ་འགྲོ་བ་མེད་པ་དོན་ཐ་དད་མ་ཡིན་པ། དོན་གཅིག༌[^3]མ་ཡིན་པ། སྤྲོས་པ་ཐམས་ཅད་ཉེ་བར་ཞི་བ་མྱ་ངན་ལས་འདས་པའི་གྲོང་ཁྱེར་དུ་འགྲོ་བ། ཞི་བ་ལམ་དྲང་པོ་འདི་བསྟན་པ། ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་སྨྲ་བ་རྣམས་ཀྱི་དམ་པ་དེ་ལ་ཕྱག་འཚལ་ལོ། །ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 13]
བཅོམ་ལྡན་འདས་ཀྱིས་ཕྱི་རོལ་པ་ཕས་ཀྱི་རྒོལ་བ་ཐམས་ཅད་བྱིས་པ་བླ་བ༌[^4]འདྲ་བར་ཐུགས་སུ་ཆུད་ནས་འགྲོ་བ་ལོང་བ་ལག་ནོམ་བྱེད་པ་ལྟ་བུ་ལ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་བསྟན་པར་སློབ་དཔོན་གྱིས་ཡང་དག་པར་གཟིགས་པས་སྨྲ་བ་རྣམས་ཀྱི་དམ་པ་ཞེས་གསུངས་སོ། །

[Block 14]
འགག་པ་མེད་པ་ཞེས་བྱ་བ་ནི་འདི་ལ་འགག་པ་ཡོད་པ་མ་ཡིན་པའོ། །

[Block 15]
ཚིག༌[^5]ལྷག་མ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 16]
ཚིགས་སུ་བཅད་པ་དེ་ནི་མདོ་ལྟ་བུ་སྟེ། བསྟན་བཅོས་ལྷག་མས་དེ་རྣམ་པར་བཤད་པ༌[^6]བྱེད་པར་འགྱུར་རོ། །

[Block 17]
དེ་ཡང་བརྗོད་པ་ལ་མངོན་པར་ཞེན་པའི་དབང་གིས༌[^7]སྒོ་དེ་དང་དེས་བྱེད་པར་འགྱུར་གྱི་གོ་རིམས་ཇི་ལྟ་བ་བཞིན་དུ་ནི་མི་བྱེད་དོ། །

[Block 18]
ཅི་སྟེ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྗེས་སུ་བསྟན་པ་ལ་དགོས་པ་ཅི་ཡོད་ཅེ་ན། བཤད་པ། སློབ་དཔོན་ཐུགས་རྗེའི་བདག་ཉིད་ཅན་གྱིས༌[^8]སེམས་ཅན་རྣམས་སྡུག་བསྔལ་སྣ་ཚོགས་ཀྱིས་ཉེན་པར་གཟིགས་ནས་དེ་དག་རྣམ་པར་གྲོལ་བར་བྱ་བའི་ཕྱིར་དངོས་པོ་རྣམས་ཀྱི་ཡང་དག་པ་ཇི་ལྟ་བ་ཉིད་རབ་ཏུ་བསྟན་པར་བཞེད་པས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྗེས་སུ་བསྟན་པ་བརྩམས་ཏེ།

[Block 19]
ཡང་དག་མ་ཡིན་མཐོང་བ་འཆིང་། །ཡང་དག་མཐོང་བ་རྣམ་པར་གྲོལ། །ཞེས་གསུངས་པའི་ཕྱིར་རོ།[^9] །དངོས་པོ་རྣམས་ཀྱི་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན༌[^10]ཉིད་གང་ཡིན། བཤད་པ། ངོ་བོ་ཉིད་མེད་པ་ཉིད་དེ། མི་མཁས་པ་གཏི་མུག་གི་མུན་པས་བློ་གྲོས་ཀྱི་མིག་བསྒྲིབས་པ་ནི་དངོས་པོ་རྣམས་ལ་ངོ་བོ་ཉིད་དུ་རྣམ་པར་རྟོག༌[^11]ན་དེ་དག་ལ་འདོད་ཆགས་དང་ཞེ་སྡང་དག་སྐྱེད་པར༌[^12]བྱེད་དོ། །

[Block 20]
གང་གི་ཚེ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཤེས་པའི་སྣང་བས་གཏི་མུག་གི་མུན་པ་བསལ་ཅིང་། ཤེས་རབ་ཀྱི་མིག་གིས་དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པ་ཉིད་མཐོང་བ་དེའི་ཚེ་ན་གནས་མེད་པ་ལ་དེའི་འདོད་ཆགས་དང་ཞེ་སྡང་དག་མི་སྐྱེའོ། །

[Block 21]
འདི་ལྟ་སྟེ་དཔེར་ན་ལ་ལ་ཞིག་གཟུགས་བརྙན་གྱི་བུད་མེད་ལ་བུད་མེད་དོ་སྙམ་པའི་བློ་གྲོས་སྐྱེས་ནས་ཀུན་ཏུ་འདོད་ཆགས་སྐྱེད་དེ༌[^13]དེ་དང་འབྲེལ་པའི་ཡིད་ཀྱིས་དེ་ལ་རྣམ་པར་རྟོག་པར་བྱེད་དོ། །

[Block 22]
གང་གི་ཚེ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རྟོགས་པ་དེའི་ཚེ་ན་བུད་མེད་ཀྱི་བློ་གྲོས་མེད་པར་གྱུར་ཅིང་འདོད་ཆགས་དང་བྲལ་ནས་ཤིན་ཏུ་ངོ་ཚ་བ་སྐྱེས་ཏེ། རང་བཞིན་གྱི༌[^14]སེམས་གནས་མེད་པ་ལ་འདོད་ཆགས་སྐྱེ་བ་ལ་འཕྱ་བ་དེ་དང་འདྲ་སྟེ་དེ་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་དགེ་སློང་དག་བུད་མེད་ལ་ནང་གི་བུད་མེད་ཀྱི་དབང་པོ་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་སྟེ། དགེ་སློང་དག་གལ་ཏེ་བུད་མེད་ཡིན་ན་ནང་གི་བུད་མེད་ཀྱི་དབང་པོ་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་ངོ་། །ཞེས་རྒྱ་ཆེར་བཀའ་སྩལ་ཏོ། །

[Block 23]
དེའི་ཕྱིར་སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 24 [VERSE]]
སྲིད་པའི་ས་བོན་རྣམ་ཤེས་ཏེ། །
ཡུལ་རྣམས་དེ་ཡི་སྤྱོད་ཡུལ་ལོ། །
ཡུལ་ལ་བདག་མེད་མཐོང་ན་ནི། །
སྲིད་པའི་ས་བོན་འགག་པར༌[^15]འགྱུར། །

[Block 25]
ཞེས་གསུངས་སོ། །

[Block 26]
དེ་ལྟ་བས་ན་སློབ་དཔོན་གྱིས་དངོས་པོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པ་ཉིད་རབ་ཏུ་བསྟན་པའི་ཕྱིར་འདི་བརྩམ་མོ།[^16] །འདིར་སྨྲས་པ། གང་གི་ཚེ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་མཁྱེན་པ་ཐམས་ཅད་གཟིགས་པ་ཐུགས་རྗེ་ཆེན་པོ་མངའ་བ་ཉིད་ཀྱིས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དེ་དང་དེར་དེ་ལྟ་དེ་ལྟར་བཤད་ཅིང་རབ་ཏུ་བསྟན་ཟིན་ན། ཡང་དེ་རྗེས་སུ་རབ་ཏུ་བསྟན་པ་ལ་དགོས་པ་ཅི་ཡོད། བཤད་པ། དེ་བཞིན་གཤེགས་པ་ཉིད་ཀྱིས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་བཤད་ཅིང་རབ་ཏུ་བསྟན་པ་བདེན་མོད་ཀྱི། འོན་ཀྱང་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་གིས་སྐྱེ་བ་ལ་སོགས་པའི་བརྗོད་པ་དག་གིས་བཤད་ཅིང་རབ་ཏུ་བསྟན་པས། དེ་ལ་ད་ལྟར༌[^17]ཉིད་ཀྱང་བརྗོད་པ་ཙམ་ལ་མངོན་པར་ཞེན་པའི་བློ་ཅན་ཁ་ཅིག་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མཆོག་ཏུ་ཟབ་པ་མ་རྟོགས་པ་ན། དངོས་པོ་རྣམས་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ཏེ། གང་གི་ཕྱིར་དེ་དག་གི་སྐྱེ་བ་དང་འགག་པ་དང་འགྲོ་བ་དང་འོང་བ་དག་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 27]
གང་ཞིག་ཡོད་པ་ལས་རྟག་པ་དང་ཆད་པ་དང་དེ་ཉིད་དང་གཞན་ཉིད་དུ་སེམས་པ་དག་བྱེད་ཀྱི། རི་བོང་གི་རྭ་ལ་སོགས་པ་མེད་པ་དག་ལ་དེ་དག་མི་འབྱུང་ངོ་སྙམ་དུ་སེམས་པ་དེ་དག་ལ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ངོ་བོ་ཉིད་རབ་ཏུ་བསྟན་པའི་ཕྱིར་སློབ་དཔོན་གྱིས་རིགས་པ་དང་ལུང་སྔོན་དུ་བཏང་བ་འདི་བརྩམས་སོ། །

[Block 28]
གཞན་ཡང་གང་ཁོ་ནའི་ཕྱིར་དེ་བཞིན་གཤེགས་པས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་བཤད་ཅིང་རབ་ཏུ་བསྟན་པ་དེ་ཁོ་ནའི་ཕྱིར་སློབ་དཔོན་གྱིས་རྗེས་སུ་རབ་ཏུ་བསྟན་པར་འཐད་ཀྱི། མ་བཤད་ཅིང་རབ་ཏུ་མ་བསྟན་པར་རྗེས་སུ་རབ་ཏུ་སྟོན་པར་འོས་པ་དེ་གང་ཞིག་ཡིན། འདི་ལྟར་འཇིག་རྟེན་པའི་བསྟན་བཅོས་དག་ཀྱང་སྔོན་གྱི་སློབ་དཔོན་རྣམས་ཀྱིས་བཤད་ཅིང་རབ་ཏུ་བསྟན་པས་ད་ལྟར་ཉིད་ཀྱང་དེ་རྣམས་ཀྱི་སློབ་མ་དག་རྗེས་སུ་སྨྲ་བར་བྱེད་དོ། །

[Block 29]
དེའི་ཕྱིར་སློབ་དཔོན་གྱིས་རྗེས་སུ་རབ་ཏུ་བསྟན་པར་རིགས་སོ། །

[Block 30]
འདིར་སྨྲས་པ། ཅིའི་ཕྱིར་འགག་པ་ལ་སོགས་པ་བརྒྱད་པོ་དེ་དག་འགོག་པར་བྱེད།

[Block 31 [VERSE]]
འགག་པ་མེད་པ་སྐྱེ་མེད་པ། །
ཆད་པ་མེད་པ་རྟག་མེད་པ། །

[Block 32]
ཞེས་བྱ་བ་དེ་ཙམ་ཞིག་བྱས་པས་མི་ཆོག་གམ། བཤད་པ། དངོས་པོའི་ངོ་བོ་ཉིད་སྨྲ་བ་དག་ཕལ་ཆེར་ཐ་སྙད་ཀྱི་དབང་གིས་བསྟན་པ་འགག་པ་ལ་སོགས་པ་བརྗོད་པ་བརྒྱད་པོ་དེ་དག་གིས་དངོས་པོ་ཡོད་པ་ཉིད་དུ་སྟོན་པར་བྱེད་པས་དེའི་ཕྱིར་འགག་པ་ལ་སོགས་པ་བརྒྱད་པོ་དེ་དག་ཉིད་དགག་པ་མཛད་དོ། །

[Block 33]
དེ་བཞིན་དུ་དེ་ཁོ་ན་སེམས་པར་བྱེད་པའམ། འགྱེད་པ་རྩོམ་པར་བྱེད་པ་གང་དག་ཅི་ཡང་རུང་བ་དེ་དག་ཀྱང་འགག་པ་ལ་སོགས་པའི་དོན་དེ་དག་ལ་བརྟེན་ནས་སེམས་པ་དང་རྩོམ་པར༌[^18]བྱེད་དེ།[^19] འདི་ལྟ་སྟེ། རེ་ཞིག་ཁ་ཅིག་ན་རེ་དངོས་པོ་ཐམས་ཅད་ནི་སྐྱེ་བ་དང་འགག་པའི་ཆོས་ཅན་སྐད་ཅིག་མ་སྟེ་རྒྱུན་གྱིས་རྒྱུན་དུ་འབྱུང་ངོ་། །ཞེས་ཟེར་རོ། །

[Block 34]
[^20]གཞན་དག་ན་རེ་ས་ལ་སོགས་པ་རྫས་དགུ་པོ་དག་རྟག་ཅེས་ཟེར་རོ། །

[Block 35]
ཡང་གཞན་དག་ནི་ཆོས་དང་ཆོས་མ་ཡིན་པ་དང་། གང་ཟག་ནམ༌[^21]མཁའ་དང་། དུས་དང་གང་ཟག་དང་སྲོག་ཅེས་བྱ་བ་རྫས་དྲུག་པོ་དག་རྟག་ཅེས་བརྗོད་དོ། །

[Block 36]
དེ་བཞིན་དུ་ཕལ་ཆེར་སྲོག་དང་ལུས་གཉིས། མེ་དང་བུད་ཤིང་གཉིས། རྒྱུ་དང་འབྲས་བུ་གཉིས། ཡོན་ཏན་དང་ཡོན་ཅན་གཉིས། ཡན་ལག་དང་ཡན་ལག་ཅན་གཉིས་ནི་དེ་ཉིད་དང་གཞན་ཉིད་ཅེས༌[^22]འགྱེད་པར་བྱེད་དོ། །

[Block 37]
དེ་བཞིན་དུ་ཁ་ཅིག་ན་རེ་ཡོན་ཏན་བྱ་བ་དང་ལྡན་པ་རྣམས་དང་རྟག༌[^23]འཁོར་ལོ༌[^24]ཞེས་ཟེར་རོ། །

[Block 38]
གཞན་དག་ན་རེ་རྡུལ་ཕྲན་དང་ཡིད་གཉིས་ནི་མི་འགྲོའོ་ཞེས་ཟེར་རོ། །

[Block 39]
གཞན་དག་ནི་སྲོག་དང་གང་ཟག་གཉིས་འགྲོ་བ་དང་ལྡན༌[^25]ཞེས་བརྗོད་དོ། །

[Block 40]
གྲུབ་ནས་གང་དུ་འགྲོ་བར་ཡང་འདོད་དོ། །
--- END BLOCKS ---
