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
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་དང་པོའི་དཀའ་བ་བཏུས་ཏེ་བཤད་པའོ།།།།

[Block 72 [HEADING]]
## ལེའུ་གཉིས་པ། ^2-0

[Block 73]
རྒྱུ་དང་འབྲས་བུའི་ཉེ་བར་གདགས་པ་ཞེས་བྱ་བའི་སྐུ་དང་གསུང་དང་ཐུགས་རྣམས་ཀྱི་རང་གི་ངོ་བོ་དབྱེར་མི་ཕྱེད་པའི་བྱང་ཆུབ་ཀྱི་སེམས་གང་ཡིན་པ་དེ་ནི༌[^24]རྒྱུ་ཡིན་ལ། དེས་རྡོ་རྗེ་འཛིན་པ་མཆོག་ལ་ཉེ་བར་སྤྱོད་པ་ནི་འབྲས་བུའོ།།

[Block 74]
སྲོག༌[^25]ལས་ཞེས་བྱ་བ་ནི་རླུང་ལས་ཞོན་པའི་རྣམ་པར་ཤེས་པ་རྨི་ལམ་ལྟ་བུར་སྣང་བའོ།།

[Block 75]
ཁམས་གསུམ་གྱི་རྣམ་པར་གནས་པ་ནི། ཁམས་གསུམ་པ་དེ་ཉིད་རླུང་རྨི་ལམ་ལྟ་བུར་གནས་པ་སྟེ། གནས་པ་ཞེས་པ༌[^26]འདི་ཉིད་ཀྱང་ཁམས་གསུམ་པར་སྐྱེས་པའོ།།

[Block 76]
མཆོག་ཅེས་བྱ་བ་ནི་དམ་པ་སྟེ་སྲིད་པ་བར་མ་དོའི་མཚན་ཉིད་དང་འདྲ་བའོ།།

[Block 77]
གཅིག་ཏུ་ཞེས་པ་ནི་རླུང་དང་རྣམ་པར་ཤེས་པ་གཅིག་ཏུ་འདུས་པའོ།།

[Block 78]
མྱུར་དུ་ཞེས་པ་ནི་སེམས་ཙམ་དུའོ།།

[Block 79]
མཐོང་བ་ནི༌[^27]དེར་མཐོང་བའོ།།

[Block 80]
བདག་ཉིད་ཅེས་པ་ནི་རྣལ་འབྱོར་པར་བལྟའོ།།

[Block 81]
དེ་དག་ཉིད་ནི་རང་བྱིན་གྱིས་བརླབ༌[^28]པའི་གནས་ཏེ། གཟུགས་ལ་སོགས་པ་ནས་ཡིད་ཀྱི་མཐར་ཐུག་པ༌[^29]དེ་བཞིན་གཤེགས་པ་དྲུག་པོར་བྱིན་གྱིས་བརླབ་པ་ལ་སོགས་པ་བསྟན་ཏེ།།བརྟན་པ་དང་གཡོ་བ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་སྟོང་པ༌[^30]ཉིད་ཁོ་ནར་བསྒོམ་པའི༌[^31]མུ་སྟེགས་ཅན་ལ་སོགས་པའི་ཚུལ་འགེགས་པ་ཡིན་ནོ།།

[Block 82]
དེ་ཡང་།

[Block 83 [VERSE]]
བསྒོམ་པར་བྱ་བ་བསྒོམ་པ༌[^32]མེད། །
ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 84]
དེ་གང་ཡོད་པར་བསྒོམ་ཞེས་བྱ་བའི་རྣམ་པ༌[^33]དེ་ལྟ་བུ་ཉིད་ཀྱིས་ཡོད་དང་མེད་པར་བསྒོམ་པ་དག་མ་ཡིན་པར་དཔྱད་པའོ།།

[Block 85]
སྟེང་འོག་ཅེས་པ་ལ་སོགས་པ་ལས་ནི་ཉན་ཐོས་བྱེ་བྲག་ཏུ་སྨྲ་བའི་བསྒོམ་པ་འགེགས་པ་སྟེ། དེ་ཡང་གཞན་ལས་སྨྲས་པ།

[Block 86 [VERSE]]
ནམ་མཁའ་གཉིས་པོ་འགེགས་པ༌[^34]དང་། །
དུས་གསུམ་རྟག་པ་འདུས་མ་བྱས། །

[Block 87]
ཞེས་པའི་ཚུལ་ལོ།།

[Block 88]
གང་ཡང་རྒྱུ་དང་འབྲས་བུ་ཞེས་པ༌[^35]ལ་སོགས་པས་ནི་མདོ་སྡེ་པའི་སྤྱིའི་དོན་བསྒོམ་པ་འགེགས་པ་ཡིན་ནོ།།

[Block 89]
ཕུང་པོ་ལ་སོགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་རྣམ་པར་ཤེས་པ་ཙམ་དུ་སྨྲ་བའི་གཞུང་གི་བསྒོམ་ལུགས་འགེགས་པ་ཡིན་ནོ།།

[Block 90]
ཀུན་རྫོབ་ཀྱི་བདེན་པ་བཟློག་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཀུན་རྫོབ་ཏུ་སྣང་བ་དེར་བསྒོམ་པ་འགེགས་པ་ཡིན་ནོ།།

[Block 91]
བདེན་པ་གཉིས་ལྟ་བུར་ཞེས་པ་ལ་སོགས་པས་ནི་དོན་དམ་པའི་བདེན་པ་དང་། ཀུན་རྫོབ་ཀྱི་བདེན་པ་ལ་མངོན་པར་ཞེན་ནས་བསྒོམ་པ་འགེགས་པར་བྱེད་པ་ཡིན་ནོ།།

[Block 92]
མཐར་ཐུག་པའི་དོན་གྱིས༌[^36]ནི་བསྒོམ་པ༌[^37]མ་ནོར་བ་ཡིན་པར་བསྟན་ཏེ། རང་བཞིན་དགའ་བ་དང་རང་བཞིན་གྱིས༌[^38]འོད་གསལ་བར་རབ་ཏུ་གནས་པ་ཡིན་ནོ།།

[Block 93]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་ལེའུ་གཉིས་པའི་དཀའ་བ་བཏུས་ཏེ་བཤད་པའོ།།།།

[Block 94 [HEADING]]
## ལེའུ་གསུམ་པ། ^3-0

[Block 95]
གནས་ཇི་ལྟ་བ་བཞིན་དུ་ཞེས་པ་ནི་དབུས་དང་ཤར་ལ་སོགས་པའི་གནས་རྣམས་སོ།།

[Block 96]
སྐུ་གསུང་ཐུགས་ཀྱིས༌[^39]མཚན་པ་ཞེས་པ་ནི་སྐུ་རྡོ་རྗེ་རྣམ་པར་སྣང་མཛད་ཀྱིས༌[^40]དཀྱིལ་འཁོར་བ་རྣམས་ལ་ཡང་མཚན་པ་སྟེ། གཙོར་བྱས་པའི་རང་བཞིན་འདིས་ནི་ཐུགས་དང་གསུང་རྣམས་ལ་ཡང་གོ་བར་བྱའོ།།

[Block 97]
རྡོ་རྗེ་གསུམ་པོ་རྣམ༌[^41]པ༌[^42]རེ་རེ་ལ་ཡང་ནང་ཕན་ཚུན་དུ་ལྡན་པར་གསལ་བར་བསྟན་པའི་ཕྱིར་རོ།།

[Block 98 [VERSE]]
རྣམ་པར་སྣང་མཛད་ཐུགས་རྗེ་ཆེ། །
སྐུ་གསུང་ཐུགས་ཀྱི་མཚན་མ་འམ། །

[Block 99]
ཞེས་གསུངས་པ་ལ། ཨོཾ་ཤཱུ་ནྱ་ཏཱ་ཛྙཱ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་རིགས་དྲུག་དང་། རིགས་གསུམ་དང་།

[Block 100 [VERSE]]
མཐར་རིགས་གཅིག་ཏུ་ཐུག་པར་བསྟན་ཏོ། །
བཞི་བཞི་ཡི་ནི་སྦྱོར་བ་ཡིས། །

[Block 101]
ཞེས་པ་ལ་སོགས་པ་ནི་དཀྱིལ་འཁོར་རེ་རེ་ཞིང་ཡང་དཀྱིལ་འཁོར་བཞི་བཞིའི་རང་བཞིན་ཡིན་པ་ལ་བྱའོ།།

[Block 102]
གོས་དཀར་ལ་སོགས་པའི་རང་བཞིན་དེ་ནི་ལྷ་སྟེ་རྣམ་པར་ཤེས་པའོ།།

[Block 103]
སྒྲོན་མ་གསལ་བར་བྱེད་པ་ཞེས་བྱ་བའི་ལེའུ་གསུམ་པའི་དཀའ་བ་བཏུས་པའི་བཤད་པའོ།།།།

[Block 104 [HEADING]]
## ལེའུ་བཞི་པ། ^4-0

[Block 105]
ཆོ་ག་ཞེས་པ་ལ་སོགས་པ་ནི་གཏོར་མ་དང་སྦྱིན་སྲེག་ལ་སོགས་པའི་ཆོ་ག་ཉི་ཤུ་པོ་རྣམས་སོ།།

[Block 106]
འདི་ནི་དགུག་པའི་བདག་ཉིད་མཆོག །ཅེས་བྱ་བ་ནི་ཕུང་པོ་ལྔ་དང་འབྱུང་བ་བཞིའི་བདག་ཉིད་དེ། [^43]དེ་ལྟ་བུའི་ཐིག་སྐུད་ཀྱིས་ལུས་ཀྱི་དཀྱིལ་འཁོར་རྣམས་ཀྱི་གནས་ཇི་ལྟ་བ་བཞིན་དུ་ཡང་དག་པར་བལྟ་བར་བྱའོ།།

[Block 107]
རྣམ་པ་ལྔའི་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཡེ་ཤེས་ལྔ་རྣམས་ཀྱི་རང་བཞིན་གྱིས་མི་བསྐྱོད་པ་ལ་སོགས་པ་དབུས་ལ་སོགས་པར་བཀོད་པ༌[^44]ཡིན་པར་སྟོན་ནོ།།

[Block 108]
དབྱིབས་ཀྱི་མཆོད་པ་ཞེས་པ་དང་། རྣམ་པ་གསུམ་ཞེས་པ་ནི་འཇུག་པ་དང་ལྡང་བ་དང་། གནས་པའི་རིམ་གྱིས་སོ།།

[Block 109]
སྐད་ཅིག་ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་སྣང་བ་རྣམས་ཀྱི་རང་བཞིན་གྱི་སྐད་ཅིག་གི་དུས་ལས་སྟོང་པ་བཅུ་དྲུག་ཏུ་ཕྱེ་བའོ།།

[Block 110]
ཞི་བའི་ཆོས་ནི་ཤིན་ཏུ་ཕྲ་བའི་ཁམས་སེམས་ཅན་གྱི་ཡོངས་སུ་ཤེས་པར་བྱས་པ༌[^45]རྣམ་པར་ཤེས་པའི་རང་བཞིན་སྙིང་རྗེ་ཆེན་པོའི་བདག་ཉིད་དེ་ཞི་བར་ངེས་པར་སྦྱངས་པའོ།།
--- END BLOCKS ---
