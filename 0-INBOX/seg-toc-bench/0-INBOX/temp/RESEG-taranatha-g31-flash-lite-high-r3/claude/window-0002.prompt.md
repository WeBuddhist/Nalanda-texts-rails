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
འདི་ནི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་གི་འབྲས་བུ་ཀུན་ཏུ་འོད་ལ་སོགས་པའི་ས་བཅུ་གཉིས་སོ། །

[Block 72 [HEADING]]
### ཕྱག་འཚལ་དགུ་པ། ^1-9-0

[Block 73 [HEADING]]
#### ཚིག་འགྲེལ། ^1-9-1-0

[Block 74]
ཚིགས་བཅད་དགུ་པ་ཕྱག་འཚལ་དཀོན་མཆོག་སོགས་ལ། དཀོན་མཆོག་གསུམ་མཚོན་པར་བྱེད་པ་ཨུཏྤ་ལའི་ཕྱག་རྒྱ་ནི་སྒྲོལ་མའི་དམ་ཚིག་གི་ཕྱག་རྒྱ་སྟེ། སྙིམས་པ་ཁ་སྦྱར་གྱི་གུང་མོ་སྦྱར་ཞིང་མཛུབ་མོས་བརྟེན་ནས་མཐེ་བོང་གཤིབས་ཏེ་རྩེ་བར་བཀོད་པ་ཐུགས་ཀར་གཏོང་པས་རྣམ་པར་བརྒྱན་པ་ནི། རྗེས་འཇུག་རྣམས་ཀྱིས་ཀྱང་དམ་ཚིག་གི་ཕྱག་རྒྱ་དེ་ལྟ་བུ་ཆོག་བཞིན་དུ་བཅིངས་ན། རིག་སྔགས་ཀྱི་ལྷས་བྱིན་གྱིས་བརླབ་པའི་དོན་སྔོན་བྱུང་ལ་བཅོམ་ལྡན་འདས་མ་ཉིད་ཕྱག་རྒྱ་དེ་ལྟ་བུ་འཆིང་བའི་སྐུའི་རྣམ་འགྱུར་དང་། ཕྱོགས་ཀྱི་འཁོར་ལོ་སྟེ་ཕྱོགས་བཅུའི་ཞིང་ཁམས་མ་ལུས་པ། རང་གི་སྐུ་ལས་བྱུང་བའི་འོད་ཟེར་གྱི་ཚོགས་རབ་ཏུ་འཁྲུགས་ཤིང་འཕྲོས་པས་ཁབ་ཅིང་བརྒྱན་པར་མཛད་པའོ། །

[Block 75]
དེ་ཉིད་རྗེས་འཇུག་ལ་ནི། ཕྱག་རྒྱ་དེས་སྤྱན་དྲངས་ན་ཕྱོགས་བཅུའི་ཞིང་ནས་འོད་ཟེར་འཕོ་ཞིང་དངོས་སུ་འབྱོན་པའོ། །

[Block 76 [HEADING]]
#### སྦས་དོན། ^1-9-2-0

[Block 77]
སྦས་དོན་ནི། དཀོན་མཆོག་གསུམ་མཚོན་ནི་ཁུ་རྡུལ་རླུང་གསུམ་སྟེ། གཅིག་ཏུ་འདུས་པས་སོར་མོ་གསུམ་གྱི་ཕྱག་རྒྱ་ལྟ་བུ་དེ་རྣམས་རྩ་འཁོར་ལོ་སོ་སོའི་ཐུགས་ཀ་སྟེ་དབུས་ཀྱི་ལྟེ་བའི་ཐིག་ལེར་ཡོངས་སུ་བཅིངས་པས་ཡེ་ཤེས་ཀྱི་སྐུ་གཏུམ་མོའི་འོད་ཟེར་ལས་གྲུབ་པ་ཕྱོགས་ཀུན་དུ་ཁྱབ་པས་ཐོབ་པར་འགྱུར་བའི་དོན་ཏེ། འཛིན་པའི་སྟོབས་ལས་རྗེས་དྲན་འབྱུང་བའོ། །

[Block 78 [HEADING]]
### ཕྱག་འཚལ་བཅུ་པ། ^1-10-0

[Block 79 [HEADING]]
#### ཚིག་འགྲེལ། ^1-10-1-0

[Block 80]
ཚིགས་བཅད་བཅུ་པ་ཕྱག་འཚལ་རབ་ཏུ་སོགས་ལ། འགྲོ་བ་རྣམས་རབ་ཏུ་དགའ་བ་བསྐྱེད་པའི་སྐུ་དང་། བརྗིད་ཅིང་མཛེས་པས་དབུ་རྒྱན་གྱི་ནོར་བུ་ལས་འོད་ཟེར་གྱི་ཕྲེང་བ་སྤེལ་ཞིང་འཕྲོ་བ་མ་དང་། བཞད་པ་དང་རབ་ཏུ་ཆེར་བཞད་པ་དང་། ཨོཾ་ཏུཏྟཱ་རེ་ལ་སོགས་པའི་སྔགས་ཀྱི་སྒྲས་འཇིག་རྟེན་གཞན་རྣམས་དབང་དུ་བྱེད་པའི་བདུད་ཀྱང་ཁྱོད་ཀྱིས་དབང་དུ་མཛད་ལ། འཇིག་རྟེན་གཞན་ཐམས་ཅད་ཀྱང་ནུས་པས་དབང་དུ་བསྡུས་ནས། ཐར་པ་དང་ཐམས་ཅད་མཁྱེན་པ་ལ་འགོད་དོ། །

[Block 81 [HEADING]]
#### སྦས་དོན། ^1-10-2-0

[Block 82]
སྦས་དོན་ནི། རབ་ཏུ་དགའ་བ་ལྷན་ཅིག་སྐྱེས་པའི་གཟི་བརྗིད་ཀྱི་འོད་ཟེར་གྱི་དབུ་ལ་བརྒྱན་པ་ནི། སྤྱི་བོར་མས་བརྟེན་པའི་ལྷན་སྐྱེས་ཏེ། བཞད་པ་རབ་བཞད་ཀྱང་སྒྲ་དང་བཅས་པའི་གཏུམ་མོའི་མེས་དོན་ནོ། །

[Block 83]
ཏུཏྟཱ་ར་ནི་གདུང་བ་མ་སྟེ་གཏུམ་མོའི་མེས་བདུད་པས། བདུད་ཆགས་རྟོག་དང་། འཇིག་རྟེན་ལུས་ངག་ཡིད་གསུམ་བདེ་བ་ཆེན་པོའི་ཡེ་ཤེས་ཀྱིས་བྱིན་གྱིས་རློབ་ཅིང་དབང་དུ་བྱེད་པ་སྟེ། རྗེས་དྲན་གྱི་ཡན་ལག་གོ །

[Block 84 [HEADING]]
### ཕྱག་འཚལ་བཅུ་གཅིག་པ། ^1-11-0

[Block 85 [HEADING]]
#### ཚིག་འགྲེལ། ^1-11-1-0

[Block 86]
ཚིགས་བཅད་བཅུ་གཅིག་པ་ཕྱག་འཚལ་ས་གཞི་སོགས་ལ་ལྷ་མོ་གང་གི་རིག་སྔགས་ཀྱིས་ས་གཞི་སྐྱོང་བའི་རྒྱལ་པོའི་ཚོགས་སམ། སའི་ལྷ་མོ་ལ་སོགས་པ། ས་འོག་གི་ཀླུ་དང་ལྷ་མ་ཡིན་དང་རིག་པ་འཛིན་པ་དང་། མཁའ་འགྲོ་མའི་ཚོགས་རྣམས་ཐམས་ཅད་འགུགས་ཤིང་དབང་དུ་བྱེད་པའི་ནུས་པ་དང་ལྡན་པ་ཉིད་མའོ། །

[Block 87]
ཁྲོ་གཉེར་གཡོ་བ་སྟེ་ཁྲོ་མོའི་རིག་སྔགས་ཧཱུྃ་གི་ཡི་གེ་དང་བཅས་པའི་མཐུ་ལས།

[Block 88]
འགྲོ་བ་ཕོངས་བ་རྣམས་ཐམས་ཅད་དབུལ་ཞིང་ཕོངས་པའི་སྡུག་བསྔལ་མ་ལུས་པ་ལས་སྒྲོལ་ཞིང་ཞི་བར་མཛད་པ་དང་། ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པ་དང་། གཏེར་ཆེན་པོའི་དངོས་གྲུབ་ལ་སོགས་རྒྱས་པར་བྱེད་པའོ། །

[Block 89 [HEADING]]
#### སྦས་དོན། ^1-11-2-0

[Block 90]
སྦས་དོན་ནི། ས་གཞི་སྐྱོང་བ་ས་འོག་གི་བདག་པོའི་སྒྲས། རྡུལ་གྱི་དངས་མ། གཙུག་ཏོར་ནས་ནོར་བུའི་བར་དུ་བརྟེན་པའི་ཚུལ་གྱིས་འགུགས་པ་དང་། ཁྲོ་གཉེར་གཡོ་བ་དང་ཧཱུྃ་གི་སྒྲས། རི་བོང་ཅན་གྱི་དངས་མ་ཁྲོ་གཉེར་ཏེ། སྨིན་མཚམས་ཀྱི་ཐིག་ལེ་བརྒྱུད་དེ། གཙུག་ཏོར་གྱི་བར་དུ་བརྟན་པ་ནི། ནམ་མཁའི་མཛོད་ལ་སོགས་པའི་ཏིང་ངེ་འཛིན་སྒྲུབ་པའི་ཕྱིར་ཕོངས་པ་ལས་གྲོལ་བའོ། །

[Block 91]
འདི་ནི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་གི་ཁྱད་ཆོས་དཀར་དམར་གྱི་འགྲོད་པ་སྟེང་འོག་ཏུ་འགག་ཚུལ་ལོ། །

[Block 92 [HEADING]]
### ཕྱག་འཚལ་བཅུ་གཉིས་པ། ^1-12-0

[Block 93 [HEADING]]
#### ཚིག་འགྲེལ། ^1-12-1-0

[Block 94]
ཚིགས་བཅད་བཅུ་གཉིས་པ་ཕྱག་འཚལ་ཟླ་བའི་སོགས་ལ། ཟླ་བའི་དུམ་བུ་ནི་ཟླ་བ་ཕྱེད་པས་དབུ་བརྒྱན་ལ་བརྒྱན་པ་ལས་དང་། གཞན་ཡང་རྒྱན་གྱིས་བརྒྱན་པ་ཐམས་ཅད་ལས་འོད་ཟེར་རབ་ཏུ་འབར་བས། ཕྱུག་བདག་ཆེན་པོ་བྱེ་བ་ཕྲག་བརྒྱའི་དྲེགས་པ་འཇོམས་པ་མོ། ལན་འགའ་དཀའ་ཐུབ་ཅན་གྱི་སྐུར་བསྟན་ནས།

[Block 95]
རལ་པའི་ཐོར་ཚུགས་འཆར་བའི་ཁྲོད་ན་དེ་བཞིན་གཤེགས་པ་འོད་དཔག་ཏུ་མེད་པ་བཞུགས་ཤིང་གནས་པའི་སྐུ་ལས།

[Block 96]
རྟག་ཏུ་རྒྱུན་མི་འཆད་པར་ཤིན་ཏུ་འོད་རབ་བྱེད་མ་སྟེ། འོད་ཀྱི་སྣང་བས་གསལ་བར་བྱེད་པའོ། །

[Block 97 [HEADING]]
#### སྦས་དོན། ^1-12-2-0

[Block 98]
སྦས་དོན་ནི། གོང་སྔ་མའི་འཕྲོས་དེ་ཉིད་ལ་སྦྱར་ཏེ། ཟླ་བའི་དུམ་བུའི་དབུ་རྒྱན་ནི་བྱང་ཆུབ་ཀྱི་སེམས་སྤྱི་བོར་བརྟན་པའོ། །

[Block 99]
རལ་པའི་ཁྲོད་གནས་ནི་གྲིབ་མའི་ཚུལ་དུ་སྤྱི་བོར་བརྟན་པ། འོད་དཔག་མེད་ནི་དམར་ཆའི་དངས་མ། དེ་གཉིས་དཀར་ལ་འོད་ཟེར་རབ་ཏུ་འཕྲོ་པ་ནི། དཀར་དམར་དེ་རྣམས་སྟོང་གཟུགས་ཕྱག་རྒྱ་ཆེན་པོའི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་མཐའ་ཡས་པར་གྱུར་པའོ། །

[Block 100 [HEADING]]
### ཕྱག་འཚལ་བཅུ་གསུམ་པ། ^1-13-0

[Block 101 [HEADING]]
#### ཚིག་འགྲེལ། ^1-13-1-0

[Block 102]
ཚིགས་བཅད་བཅུ་གསུམ་པ་ཕྱག་འཚལ་བསྐལ་པ་སོགས་ལ། བསྐལ་པ་ཐ་མ་སྟེ། འཇིག་དུས་ཀྱི་མེ་ལྟར་འབར་བའི་ཕྲེང་བ་མེ་དཔུང་གི་དབུས་ན་བཞུགས་ཤིང་། ནང་ཟག་མེད་ཀྱི་དགའ་བ་ལས་མ་གཡོས་བཞིན་དུ། གཡས་བརྐྱང་གཡོན་བསྐུམ་སོགས་དྲག་པོའི་སྟངས་སྟབས་ཀུན་ནས་བསྐོར་བ་སྟེ་རོལ་པ་སྣ་ཚོགས་པས་དགའ་བ་དང་། དགྲ་བོ་སྟེ་མི་དང་མི་མ་ཡིན་པའི་གནོད་བྱེད་ཀྱི་དཔུང་གི་ཚོགས་རྣམས་ནི་རབ་ཏུ་འཇོམས་པའོ། །

[Block 103 [HEADING]]
#### སྦས་དོན། ^1-13-2-0

[Block 104]
སྦས་དོན་ནི། གཏུམ་མོ་ཡེ་ཤེས་ཀྱི་མེ་དུས་མཐའི་མེ་འབར་བ་ལྟ་བུ་སྟེ། ལུས་དང་སྣང་བ་ཐམས་ཅད་ལ་ཁྱབ་པར་འབྱུང་བའི་རྒྱུན་ནི། གཡས་བརྐྱང་གཡོན་བསྐུམ་སྟེ། གཡས་གཡོན་རོ་རྐྱང་ངམ། སྟེང་འོག་སྲོག་ཐུར་གྱི་རླུང་ནི་ཀུན་ནས་བསྐོར་བ་སྟེ། རྩ་འཁོར་ལོ་སོ་སོར་རེ་རེ་བཞིན་འབྱུང་བ་ལྔའི་ཐིམ་ཚུལ་སོགས། རྣམ་པར་རོལ་པའི་རྣམ་འགྱུར་དུ་མ་ཀུན་ནས་འབྱུང་བ་སྟེ། དགའ་བ་ཞེས་པས་རླུང་རྣམས་བདེ་བའི་ཐིག་ལེར་གྱུར་པས་བདུད་དང་ཉོན་མོངས་པའི་དགྲ་དཔུང་འཇོམས་པའོ། །

[Block 105 [HEADING]]
### ཕྱག་འཚལ་བཅུ་བཞི་པ། ^1-14-0

[Block 106 [HEADING]]
#### ཚིག་འགྲེལ། ^1-14-1-0

[Block 107]
ཚིགས་བཅད་བཅུ་བཞི་པ་ཕྱག་འཚལ་ས་གཞི་སོགས་ལ། རི་རབ་གླིང་དང་བཅས་པའི་ས་གཞི་ཆེན་པོའི་ངོས་ལ། ཐལ་མོ་བརྡབས་པའི་ཕྱག་གི་མཐིལ་གྱིས་བསྣུན་པའོ། །

[Block 108]
ཞབས་ཀྱིས་རྡུང་མ་ལས་དང་། ཞལ་རས་ཁྲོ་གཉེར་ཅན་དུ་མཛད་ཅིང་ཁྲོ་བའི་ཤུགས་ཀྱིས་ཧཱུྃ་ཞེས་ཤངས་ནས་འཇིགས་པའི་སྒྲ་བསྒྲགས་པས་ས་འོག་རིམ་པ་བདུན་ན་ནས་པའི་ཀླུ་དང་ལྷ་མིན་དང་སྲིན་པོ་དང་ཡི་དྭགས་གདུག་པ་ཅན་རྣམས་ཐམས་ཅད་འགེམས་པ་མོ་སྟེ་དུམ་བུར་འཐོར་པར་མཛད་པའོ། །

[Block 109]
དེ་ལས་འོག་བདུན་ནི། ས་གཞི་ཆེན་པོ་འདི་ཉིད་ལ། འོག་ཏུ་ཐོག་ཕུགས་རིམ་པ་བདུན་བཞིན་དུ་མི་མ་ཡིན་གྱི་ཡུལ་ཆེན་པོ་དག་གནས་པའོ། །

[Block 110]
ཁ་ཅིག་ནི་རི་རབ་ཀྱི་རྩེ་མོའི་ཁོངས་སེང་ནས་ཐུར་དུ་གཞལ་བ་ཡིན་ཟེར་ཡང་མི་ལེགས་པར་མངོན་ནོ། །
--- END BLOCKS ---
