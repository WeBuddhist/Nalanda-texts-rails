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
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། ས་གཞི་ཆེན་པོ་འདི་སྐྱོང་བའི་ས་ཡི་ལྷ་མོ་དང༌། ཀླུ་རྒྱལ་དགའ་བོ་སོགས་དང༌། དེ་བཞིན་གནོད་སྦྱིན་གྱི་རྒྱལ་པོ། ལྷ་དབང་བརྒྱ་བྱིན་སོགས་ཀྱི་ཚོགས་རྣམས་ཐམས་ཅད༌ཁྱེད་ཀྱི་ཕྲིན་ལས་སྒྲུབ་པའི་བྲན་དུ་འགུགས་པར་ནུས་པའི་འཕགས་མ་ཁྱེད་ཉིད་མ། ཁྲོ་གཉེར་གཡོ་བའི་ཐུགས་ཀའི་ཡི་གེ་ཧཱུཾ་གི་འོད་ཟེར་གྱིས་ལྷ་ཀླུ་མི་སོགས་ཀྱི་དཔལ་འབྱོར་ལོངས་སྤྱོད་མ་ལུས་པ་བཀུག་ནས་འདོད་དགུ་ཆར་དུབབས་པས་འགྲོ་བ་དབུལ་ཞིང་ཕོངས་པ་ཐམས་ཅད་ལས་རྣམ་པར་སྒྲོལ་བར་མཛད་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 72 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-12-2-0

[Block 73]
གསལ་འདེབས་ཚུལ་ནི། དབུལ་ཕོངས་སེལ་བའི་ནོར་སྟེར་སྒྲོལ་མ་འདི་ཉིད་སྐུ་མདོག་དམར་གསེར་བརྗིད་ཅིང་ཆགས་པའི་ཞི་མ་ཁྲོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་དུ། གཏེར་གྱི་བུམ་པ་ལས་འོད་འཕྲོས་ལྷ་ཀླུའི་ལོངས་སྤྱོད་དཔལ་འབྱོར་ཐམས་ཅད་ཆར་བཞིན་བབས་པས་ཕྱོགས་ཀུན་གང་བར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 74 [HEADING]]
### ཕྱག་འཚལ་བཅུ་གཉིས་པ། ^1-13-0

[Block 75 [HEADING]]
#### ཚིག་འགྲེལ། ^1-13-1-0

[Block 76 [VERSE]]
ཕྱག་འཚལ་ཟླ་བའི་དུམ་བུས་དབུ་རྒྱན། །
བརྒྱན་པ་ཐམས་ཅད་ཤིན་ཏུ་འབར་མ།
རལ་པའི་ཁྲོད་ན་འོད་དཔག་མེད་ལས། །
རྟག་པར་ཤིན་ཏུ་འོད་རབ་མཛད་མ། །

[Block 77]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། ཟླ་བའི་དུམ་བུ་ནི་ཟླ་བ་ཕྱེད་པ་སྟེ་དེས་དབུ་ཡི་རྒྱན་དུ་རབ་ཏུ་མཛེས་པར་བརྒྱན་པ་དང་། སྐུ་ལའང་རིན་པོ་ཆེ་སྣ་ཚོགས་ལས་བརྒྱན་པ་དེ་ཐམས་ཅད་ལས་སྡུག་བསྔལ་གྱི་ཚོགས་རྣམས་སེལ་བའི་འོད་ཟེར་དཀར་པོ་ཤིན་ཏུ་འབར་ཞིང་འཕྲོ་བས། འཇིག་རྟེན་ན་ཆེ་བར་གྲགས་པའི་ཕྱག་བདག་ཡོངས་ཀྱི་ང་རྒྱལ་དང་དྲེགས་པ་འཇོམས་མ།

[Block 78]
དབུ་སྐྲ་བུང་བ་ལྟར་གནག་པའི་རལ་པའི་ཁྲོད་ན་བདེ་ལྡན་ཞིང་མགོན་འོད་དཔག་ཏུ་མེད་པ་བཞུགས་པ་ལས།

[Block 79]
དུས་རྟག་པར་མཐའ་ཡས་ཀྱི་འགྲོ་བ་རྣམས་ལ་ཤིན་ཏུ་འཁོར་གསུམ་དམིགས་པ་བྲལ་བའི་ཚད་མེད་པའི་སྙིང་རྗེའི་འོད་ཟེར་འཕྲོ་པས་འདོད་དགུའི་ཆར་ཆུ་བབས་ཅིང་། བརྟན་གཡོའི་ཉེས་པ་ཐམས་ཅད་བསལ་ཏེ། དགེ་ལེགས་བཀྲ་ཤིས་པས་སྣོད་བཅུད་ཕུན་ཚོགས་ཀྱི་དཔལ་ལ་རབ་ཏུ་སྦྱར་བར་མཛད་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 80 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-13-2-0

[Block 81]
གསལ་འདེབས་ཚུལ་ནི། སྣོད་བཅུད་དགེ་ལེགས་ཀྱིས་བདེ་བར་བྱེད་པའི་འཕགས་མ་བཀྲ་ཤིས་དོན་གྲུབ་འདི་ཉིད་སྐུ་མདོག་སེར་མོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་དཔལ་བེའུ་འོད་ཟེར་འཕྲོ་བ་ཅན་གྱིས་བཀྲ་ཤིས་པའི་རྫས་ཀྱིས་ཆར་བབས། བརྟན་གཡོ་ཉེས་ཚོགས་ཐམས་ཅད་བཅོམ་སྟེ་དགེ་ལེགས་ཀྱི་ཁྱབ་པར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 82 [HEADING]]
### ཕྱག་འཚལ་བཅུ་གསུམ་པ། ^1-14-0

[Block 83 [HEADING]]
#### ཚིག་འགྲེལ། ^1-14-1-0

[Block 84 [VERSE]]
ཕྱག་འཚལ་བསྐལ་པ་ཐ་མའི་མེ་ལྟར། །
འབར་བའི་ཕྲེང་བའི་དབུས་ན་གནས་མ། །
གཡས་བརྐྱངས་གཡོན་བསྐུམ་ཀུན་ནས་བསྐོར་དགའི། །
དགྲ་ཡི་དཔུང་ནི་རྣམ་པར་འཇོམས་མ། །

[Block 85]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། བསྐལ་པ་འཇིག་པའི་དུས་ཀྱི་མེ་ཆེན་པོ་ལྟར། ངོ་བོ་ཡེ་ཤེས་ལ་རྣམ་པ་མེ་དཔུང་འབར་བའི་ཕྲེང་བའི་དབུས་ན་གནས་ཤིང་བཞུགས་པའི་རྗེ་བཙུན་མ། ཞབས་གཡས་བརྐྱངས་གཡོན་བསྐུམ་པའི་རོལ་སྟབས་ཅིར་ཡང་མ་ངེས་པ་དང་། བདུད་སྡེའི་ཚོགས་བཅོམ་ནས་རྡོ་རྗེའི་རྭ་གུར་གྱིས་ཀུན་ནས་བསྐོར་བར། བདག་གཞན་འགྲོ་བ་རྣམས་མི་འཇིགས་སྐྱབས་ཀྱིས་རྟག་ཏུ་བསྲུང་བས་དགའ་བར་མཛད་པ། བདག་དང་གཞན་དུ་འཛིན་པའི་འཁྲུལ་ཤེས་ཀྱི་རང་གཟུགས་ཕ་རོལ་གཟུགས་ཅན་གཟུགས་མེད་ཀྱི་དགྲ་བོ་ཡི་དཔུང་ཚོགས་རྣམས་ནི་རྣམ་པར་འཇོམས་པར་མཛད་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 86 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-14-2-0

[Block 87]
གསལ་འདེབས་ཚུལ་ནི། གཟུགས་ཅན་གཟུགས་མེད་ཀྱི་གཡུལ་དང་བར་ཆད་ལས་རྒྱལ་བར་བྱེད་མའི་སྒྲོལ་མ་འདི་ཉིད་སྐུ་མདོག་དམར་མོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ་ཞལ་གཅིག་ཕྱག་གཉིས། སྤྱན་གསུམ། ཞལ་ཞི་མ་ཁྲོ་བོའི་ཉམས་ཅན། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང༌། རྡོ་རྗེ་རྭ་གདེངས་པ་ལས་འོད་ཟེར་རྡོ་རྗེའི་ཚྭ་ཚྭ་རབ་ཏུ་འབར་ཞིང་འཕྲོ་བས་ཕ་རོལ་དགྲ་བོའི་དཔུང་རྣམས་ལྷག་མེད་དུ་བཅོམ་ནས། འོད་ཟེར་སླར་ཚུར་འདུས་རྡོ་རྗེའི་རྭ་གུར་ནང་བདག་གཞན་སེམས་ཅན་ཐམས་ཅད་ཚུད་པར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 88 [HEADING]]
### ཕྱག་འཚལ་བཅུ་བཞི་པ། ^1-15-0

[Block 89 [HEADING]]
#### ཚིག་འགྲེལ། ^1-15-1-0

[Block 90 [VERSE]]
ཕྱག་འཚལ་ས་གཞིའི་ངོས་ལ་ཕྱག་གི། །
མཐིལ་གྱིས་བསྣུན་ཅིང་ཞབས་ཀྱིས་བརྡུངས་མ། །
ཁྲོ་གཉེར་ཅན་མཛད་ཡི་གེ་ཧཱུྃ་གིས། །
རིམ་པ་བདུན་པོ་རྣམས་ནི་འགེམས་མ། །

[Block 91]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། རི་རབ་གླིང་བཞི་དང་བཅས་པའི་ས་གཞིའི་ངོས་ལ། ཟིལ་གྱིས་གནོན་པའི་རྒྱ་སྡིག་མཛུབ་ཕྱག་གི་མཐིལ་གྱིས་དྲག་ཏུ་ཡང་ཡང་སྣུན་ཅིང་། ཞབས་ཀྱིས་རྡུངས་པས། འཇིག་རྟེན་གསུམ་གཡོ་ཞིང་འགུལ་བར་མཛད་མ། ཞལ་ཁྲོ་གཉེར་གྱི་ཉམས་ཅན་དང་ལྡན་པར་མཛད་ནས། ཡི་གེ་ཧཱུཾ་གི་སྒྲ་རབ་ཏུ་སྒྲོགས་པས་འོད་ཟེར་རྡོ་རྗེའི་མེ་ཆར་དག་གིས། ས་འོག་རིམ་པ་བདུན་པོ་སྟེ། ༡ མི་མ་ཡིན་གྱི་གཞི། ༢ ལྷག་པའི་གཞི། ༣ གཞི་མེད་པ། ༤ གཞི་ཉིད། ༥ བཅུད་ཀྱི་གཞི། ༦ གཞི་བཟང་པོ། ༧ དག་པའི་གཞི་བཅས་ཡན་གྱི་གདུག་པ་ཅན་དམ་སྲི་རྣམས་ཀྱི་ནི་སྙིང་དང་མགོ་བོ་འགེམ་སྟེ་སྐྱེ་བ་མེད་པ་ཡུམ་ཆེན་མོའི་ངང་དུ་བརྒྱལ་བར་མཛད་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 92 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-15-2-0

[Block 93]
གསལ་འདེབས་ཚུལ་ནི། གདུག་ཅན་དམ་སྲི་བགེགས་རིགས་ཀྱི་གནོད་པ་འཇོམས་པའི་འཕགས་མ་ཁྲོ་གཉེར་ཅན་འདི་ཉིད་སྐུ་མདོག་ནག་མོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་ན། གཏུན་ཤིང་དང་ཧཱུཾ་གི་སྒྲ་ཡིས་རྡོ་རྗེའི་མེ་ཆར་འབེབས་པ། ཕྱག་ཞབས་ས་ལ་བསྣུན་པས། གདུག་ཅན་དམ་སྲི་རྣམས་བཅོམ་ནས་ཆོས་ཉིད་ཀྱི་ཀློང་དུ་གྱུར་པར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 94 [HEADING]]
### ཕྱག་འཚལ་བཅོ་ལྔ་པ། ^1-16-0

[Block 95 [HEADING]]
#### ཚིག་འགྲེལ། ^1-16-1-0

[Block 96 [VERSE]]
ཕྱག་འཚལ་བདེ་མ་དགེ་མ་ཞི་མ། །
མྱ་ངན་འདས་ཞི་སྤྱོད་ཡུལ་ཉི་མ། །
སྭཱ་ཧཱ་ཨོཾ་དང་དང་ཡང་དག་ལྡན་པས། །
སྡིག་པ་ཆེན་པོ་འཇོམས་པ་ཉི་མ། །

[Block 97]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། འབྲས་བུ་སྡུག་བསྔལ་ཟད་པས་བདེ་མ། དེའི་རྒྱུ་ལས་ཉོན་གྱི་ཀུན་འབྱུང་སྤངས་པས་དགེ་མ། དེ་ཡང་ལམ་བདེན་སྟོང་ཉིད་རྟོགས་པའི་ཤེས་རབ་ཀྱིས་བཅོམས་པས་ཞི་མ། སྒྲིབ་གཉིས་བག་ཆགས་མ་ལུས་པ་ཡོངས་སུ་ཟད་པས་འགོག་པ་མྱ་ངན་ལས་འདས་ཤིང་ཞི་བ་ཆོས་སྐུ་ཐོབ་པའོ། །

[Block 98]
ཕྲིན་ལས་ཀྱི་ཆ་ནས་གདུལ་བྱ་རིགས་ཅན་སོ་སོ་དང་འཚམས་པའི་སྤྱོད་ཡུལ་ཅན་ཉིད་དུ་གྱུར་པའི་རྗེ་བཙུན་མ། བཟླས་པའི་མཇུག་ཏུ་སྭཱ་ཧྭ་དང་ༀ་གྱིས་འགོ་བརྩམས་པའི་རྩ་བའི་རིག་སྔགས་བཅུ་དང་ཡང་དག་ལྡན་པ་འདི་བསོད་ནམས་མིན་པ་ཐུ་ཆེ་བ་བསགས་པ་ཅན་རྣམས་ཀྱིས། རབ་ཏུ་འགྱོད་པས་ཆོ་ག་བཞིན་བཟླས་པ་དང་ཐུགས་རྗེའི་སྟོབས་ཀྱིས་སྡིག་པ་ཆེན་པོའི་འབྲས་བུ་སྡུག་བསྔལ་ཆེན་པོའང་འཇོམས་པར་མཛད་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ཡིན། །

[Block 99 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-16-2-0

[Block 100]
གསལ་འདེབས་ཚུལ་ནི། སྡིག་སྒྲིབ་ཞི་བར་མཛད་པའི་སྒྲོལ་མ་འདི་ཉིད་སྐུ་མདོག་དཀར་མོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས། གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་དུ། རིལ་པ་སྤྱི་བླུགས་བདུད་རྩིས་གང་བ་ལས་ཁྲུས་བྱུང་བས་ངན་སོང་དུ་སྐྱེ་བའི་སྡིག་སྒྲིབ་བཀྲུས་པར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 101 [HEADING]]
### ཕྱག་འཚལ་བཅུ་དྲུག་པ། ^1-17-0

[Block 102 [HEADING]]
#### ཚིག་འགྲེལ། ^1-17-1-0

[Block 103 [VERSE]]
ཕྱག་འཚལ་ཀུན་ནས་བསྐོར་རབ་དགའ་བའི། །
དགྲ་ཡི་ལུས་ནི་རབ་ཏུ་འགེམས་མ། །
ཡི་གེ་བཅུ་པའི་ངག་ནི་བཀོད་པའི། །
རིག་པ་ཧཱུཾ་ལས་སྒྲོལ་མ་ཉིད་མ། །

[Block 104]
ཞེས་པ་ལ། ཡུལ་གང་ལ་ཕྱག་འཚལ་ན། དྲང་སྲོང་དང་རིག་འཛིན། བྱང་ཆུབ་སེམས་དཔའི་ཚོགས་ཀྱིས་ཀུན་ནས་བསྐོར་བའི་དེ་དག་གི་ཐུགས་རབ་ཏུ་དགའ་བ་དང་ལྡན་པ། འཕགས་མ་ཁྱེད་ཀྱི་མཁྱེན་བརྩེ་ནུས་པའི་འོད་ཀྱིས། ཕ་རོལ་དགྲ་ཡི་ལུས་ནི་རབ་ཏུ་འགེམས་པར་མཛད་མ་ནི་རྗེ་བཙུན་མ་ཁྱེད་ཉིད་དོ། །

[Block 105]
གཞན་ཡང་ཨོཾ་ཏཱ་རེ་ཏུཏྟཱ་རེ་ཏུ་རེ་སྭཱ་ཧྭ་ཞེས་ཡི་གེ་བཅུ་པའི་གསུང་ངག་དེ་ནི། འབྲལ་མེད་བཀོད་པའི་རིག་པ་ཆེན་པོའི་སྔགས་བཟླ་ཞིང་བསྐྱེད་རིམ་གསལ་བའི་སྒོ་ནས་ཐུགས་ཀར་ཧཱུཾ་ལས་བྱུང་བའི་འོད་ཟེར་གྱིས་ཕ་རོལ་པོའི་ངན་སྔགས་བར་ཆད་ཐམས་ཅད་ཀྱི་སྟོབས་གཞོམ་པར་བྱེད་པའི་སྒྲོལ་མ་ཉིད་ཁོ་ན་ཡིན་པས་འཕགས་མ་ཁྱེད་ལའོ། །ཞེས་པ་ནི་ཚིག་འགྲེལ་ལོ། །

[Block 106 [HEADING]]
#### གསལ་འདེབས་ཚུལ། ^1-17-2-0

[Block 107]
གསལ་འདེབས་ཚུལ་ནི། དགྲ་དང་བྱད་མའི་རིག་སྔགས་སྟོབས་གཞོམ་སྒྲོལ་མ་འདི་ཉིད་སྐུ་མདོག་དམར་མོ། པད་ཟླའི་སྟེང་དུ་ཞབས་ཕྱེད་སྐྱིལ། ཞལ་གཅིག་ཕྱག་གཉིས་གཡས་མཆོག་སྦྱིན། གཡོན་ཨུཏྤལ་འཛིན་པའི་སྟེང་། རྡོ་རྗེ་རྒྱ་གྲམ་ལས་འོད་ཟེར་འཕྲོས་པས་དགྲ་བོ་བྱད་མའི་མཐུ་སྟོབས་ངག་ནུས་ཐམས་ཅད་བཤིག་པར་བསྒོམས་པ་ནི་དམིགས་རིམ་ཡིན།

[Block 108 [HEADING]]
### ཕྱག་འཚལ་བཅུ་བདུན་པ། ^1-18-0

[Block 109 [HEADING]]
#### ཚིག་འགྲེལ། ^1-18-1-0

[Block 110 [VERSE]]
ཕྱག་འཚལ་ཏུ་རེའི་ཞབས་ནི་བརྡབས་པས། །
ཧཱུྃ་གི་རྣམ་པའི་ས་བོན་ཉིད་མ། །
རི་རབ་མནྡཱ་ར་དང་འབིགས་བྱེད། །
འཇིག་རྟེན་གསུམ་རྣམས་གཡོ་བ་ཉིད་མ། །
--- END BLOCKS ---
