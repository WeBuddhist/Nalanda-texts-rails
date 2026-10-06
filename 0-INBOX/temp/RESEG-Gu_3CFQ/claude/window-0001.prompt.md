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
རྟོག་པ༌[^23]རྣམ་པར་དག་པ་གང་ཞེ་ན། འདོད་པའི་རྟོག་པ་ལ་སོགས་པའི་གཉེན་པོ་མི་སྡུག་པ་ལ་སོགས་པའི་རྟོག་པ༌[^24]དེ་ནི་རྣམ་པར་དག་པ་སྟེ། དེ་མེད་པས་ན༌[^25]རྟོག་པ་ཡོངས་སུ་དག་པའོ། །

[Block 37]
བདག་ལ་ཁྱད་དུ་གསོད་པ་ལས་ནི་བརྟུན་པའི་བརྩོན་འགྲུས་ཀྱིས་བསླབ་པའི་གཞི་རྣམས་ལ༌[^26]ལེགས་པར་ནན་ཏན་མི་བྱེད་དེ། དེའི་གཉེན་པོ་བདག་ལ་ཁྱད་དུ་མི་གསོད་པ་ལས་ནི་ས་ཆེན་པོ་ལ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པའི་གཞི་དཀའ་བ་ཐོབ་པས་སེམས་ཞུམ་པ་མེད་དོ།[^27] །བརྟུན་པའི་བརྩོན་འགྲུས་ཀྱིས་ནན་ཏན་བྱེད་དོ། །

[Block 38]
འཁོར་ཡོངས་སུ་མི་འཛིན་ཞེས་བྱ་བ་ལ་འདིར་ཚུལ་ཁྲིམས་ཀྱི་འཁོར་ནི་བཟོད་པ་སྟེ། དེ་མེད་ན་བསྡམས་སུ་ཟིན་ཀྱང་ལེགས་པར་བསྡམས་པ་མ་ཡིན་ཏེ། ཉེས་པའི་གནས་རྒྱང་མ་བསྲིངས་པའི་ཕྱིར་རོ། །

[Block 39]
ཉེས་པ༌[^28]བྱུང་བ་ལ་རྣམ་པ་ཐམས་ཅད་དུ་ཆོས་བཞིན་དུ་ཕྱིར་འཆོས་པ་མེད་པ་ཇི་ལྟ་བུ་ཞེ་ན། སྔ་ནས་བྱ་བ་དང་ལྷན་ཅིག་རྗེས་སུ་སྤྱོད་པའི༌[^29]བག་ཡོད་པ་དང་། སྔོན་གྱི་མཐའ་དང་ལྡན་པ་དང་། ཕྱི་མའི་མཐའ་དང་ལྡན་པ་དང་། དབུས་ཀྱི་མཐའ་དང་ལྡན་པའི་བག་ཡོད་པ་དང་མི་ལྡན་པའི་ཕྱིར་བསྡམས་སུ་ཟིན་ཀྱང་ལེགས་པར་བསྡམས་པ་མ་ཡིན་ནོ། །

[Block 40]
ཆོ་ག་དང་འཚོ་བ་མ་དག་པ་ནི་རྣམ་པ་ལྔ་ལྔ་པོ་དག་གི༌[^30]རྣམ་པ་རིལ་གྱིས་མེད་པའི་ཕྱིར་དེ་གཉིས༌[^31]བསྡམས་སུ་ཟིན་ཀྱང་ལེགས་པར་བསྡམས་པ་མ་ཡིན་ནོ། །

[Block 41]
ལུས་ལ་ལྟ་བ་དང་། ལོངས་སྤྱོད་ལ་ལྟ་བ་ནི་སྦྱིན་པའི་མི་མཐུན་པའི་ཕྱོགས་ཡིན་ཏེ། དེའི་ཆུང་ངུ་ཡང་དང་ཡང༌[^32]དུ་ལེན་པར་མི་བྱེད་པ་ནི་སྦྱིན་པའི་ཉེར་གནས་ཡིན་ཏེ། ཉེར་གནས་ནི་རྒྱུའི་དོན་ཏོ། །

[Block 42]
སློང་བ་ལ་ལྟ་བ་ནི་སྦྱིན་པ་སྒྲུབ་པ་ཡིན་ཏེ། གཞན་ལ་ཡང་དེ་བཞིན་དུ་བརྗོད་པར་བྱའོ། །

[Block 43]
ཕན་ཡོན་མཐོང་བ་ནི་བདེ་བའི༌[^33]རྒྱུ་ཡོངས་སུ་ཚོལ་བའི་མཚན་ཉིད་ཀྱི་ཤེས་རབ་ཀྱི་རྒྱུ་ཡིན་ནོ། །

[Block 44]
ཕན་ཡོན་མཐོང་བ་ནི་ཤེས་རབ་ཉིད་དོ། །

[Block 45]
གནས་ལྔ་དག་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡོངས་སུ་ཤེས་པ་ཡང་ཤེས༌[^34]རབ་ཉིད་དོ། །

[Block 46 [HEADING]]
### གྲོགས་སུ་འགྲོ་བ་རྣམས་ཀྱི་དོན། ^2-1-0

[Block 47]
གྲོགས་སུ་འགྲོ་བ་རྣམས་ཀྱི་དོན༌[^35]ལོངས་སྤྱོད་ཀྱི་བྱ་བའི་གྲོགས་སོ། །

[Block 48]
དེ་ལ་ལོངས་སྤྱོད་ཀྱི་བྱ་བའི་གྲོགས་ནི་རྣམ་པ་བཞི་སྟེ། མ་ཐོབ་པ་ཐོབ་པར་བྱ་བའི་དོན་དང་། འཕེལ་བར་བྱ་བའི་དོན་དང་། ལོངས་སྤྱོད་རྣམས་བསྲུང་བའི་དོན་དང་། ཡོན་གནས་སུ་གྱུར་པ་ལ་དབུལ་བའི་དོན་ཏོ། །

[Block 49]
སེམས་ཅན་གྱི་བྱ་བ་སྒྲུབ་པ་ནི་རྣམ་པ་གཅིག་པུར་ཟད་དེ། བྱེ་བ་ལས་བསྡུམ་པ༌[^36]ཁོ་ནའོ། །

[Block 50]
དེ་ལ་བྱ་བ་སེམས་པ་ཞེས་བྱ་བ་ནི་འདི་ཇི་ལྟར་བྱ་སྙོམ༌[^37]པའོ། །

[Block 51]
བྱ་བ་གཏན་ལ་འབེབས་པ་ནི་འདི་བྱའོ་ཞེའམ། འདི་མི་བྱའོ་ཞེས་བྱ་བའོ། །

[Block 52]
ལམ་དུ་འགྲོ་ཞིང་འོང་བ་ཞེས་བྱ་བ་ནི་འགྲོ་བར་བྱ་བ་དང་དེ་བཞིན་དུ་ཕྱིར་འོང་བ་ལ་སོགས་པའོ། །

[Block 53]
ཡང་དག་པའི་ལས་ཀྱི་མཐའ་ལ་སྦྱོར་བ་ཞེས་བྱ་བ་ནི་གྲུའི་ལས་ཀྱི་མཐའ་དང་། ཞིང་ལས་ལ་སོགས་པའི་ལས་ཀྱི་མཐའ་ལ་སྦྱོར་བ་སྟེ། རྣམ་པ་གསུམ་པོ་འདི་དག་ཀྱང་ལོངས་སྤྱོད་རྣམས་མ་ཐོབ་པ་ཐོབ་པར་བྱ་བའི་ཕྱིར་དང་། ཐོབ་པ་རྣམས་ཡོངས་སུ་བསྲུང་བའི་ཕྱིར་རོ། །

[Block 54]
ཡང་ན་གྲོགས་སུ་འགྲོ་བ་དང་པོ་གཉིས་ནི་མ་ཐོབ་པ་ཐོབ་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 55]
ལས་ཀྱི་མཐའ་ལ་སྦྱོར་བ་ལོངས་སྤྱོད་རྣམས་སྤེལ་བ་དང་སྲུང་བ༌[^38]ནི་རང་གི༌[^39]སྒྲས་བསྟན་ཏོ། །

[Block 56]
འཕེལ་ཟིན་པ་ལ་ནི་ཡོན་གནས་ལ་དབུལ་བའི་ཕྱིར་དང༌[^40]དགའ་སྟོན་དང་བསོད་ནམས་བྱ་བ་ལ་གྲོགས་སུ་འགྲོའོ། །

[Block 57 [HEADING]]
### སྡུག་བསྔལ་བ་རྣམས་ཀྱི་གྲོགས་སུ་དོན་གྱི་མདོ། ^2-2-0

[Block 58]
སྡུག་བསྔལ་བ༌[^41]རྣམས་ཀྱི་གྲོགས་སུ༌[^42]དོན་གྱི་མདོ་ནི་སྡུག་བསྔལ་བ་རྣམ་པ་གཉིས་ཏེ། ལུས་ཀྱི་ལས་དང་སེམས་ཀྱིའོ། །

[Block 59]
ལུས་ཀྱི་ཡང་རྣམ་པ་གསུམ་སྟེ། ནད་ཀྱི་སྡུག་བསྔལ་དང་། དབང་པོ་མ་ཚང་བའི་སྡུག་བསྔལ་དང་།

[Block 60 [VERSE]]
ཡན་ལག་མ་ཚང་བའི་སྡུག་བསྔལ་བའོ། །
ཡིད་ཀྱི་སྡུག་བསྔལ་བ་ནི་རྣམ་པ་གཉིས་ཏེ།
སྒྲིབ་པའི་སྡུག་བསྔལ་དང་རྟོག་པའི་སྡུག་བསྔལ་བའོ། །

[Block 61]
གསུམ་པ་ནི་ངལ་བ་ལས་གྱུར་པའི་སྡུག་བསྔལ་བ་སྟེ། དེར་གྲོགས་སུ་འགྲོ་བའོ། །

[Block 62 [HEADING]]
### ཚིག་འབྲུ་འབྱོར་པ་རྣམས་ཀྱིས་ཆོས་སྟོན། ^2-3-0

[Block 63]
ཚིག་འབྲུ་འབྱོར་པ་རྣམས་དང་། འབྲེལ་བ་རྣམས་དང་། རྗེས་སུ་མཐུན་པ་རྣམས་དང་། རྗེས་སུ་འཕྲོད་པ་རྣམས་དང་། [^43]ཐབས་དང་ལྡན་པ་རྣམས་དང་། མཚན་མ་རྣམས་དང་། མཐུན་པ་རྣམས་དང་། འགྲུས་སྐྱོང་གི་ཡན་ལག་གི་ཚོགས་རྣམས་ཀྱིས་ཆོས་སྟོན་ཏོ་ཞེས་བྱ་བ་དེ་ལ་ཚིག་འདི༌[^44]དག་གིས༌[^45]དྲི་བ་རྣམ་པ་གསུམ་གྱི་ལན་ཡོན་ཏན་བརྒྱད་དང་ལྡན་པ་བསྟན་ཏེ། དོན་དང་མཚམས་སྦྱོར་བའི༌[^46]དབང་དུ་བྱས་ནས་མི་ཤེས་ཏེ་འདྲི་བ་ལ་ནི་ཕྱིན་ཅི་མ་ལོག་པའི་དོན་དང་། མཚམས་སྦྱོར་བའི་ཚིག་གིས་བསྟན༌[^47]ཏོ། །

[Block 64]
ཆོས་ཉིད་དང་སྔ་ཕྱིའི་དབང་དུ་བྱས་ནས་འགལ་བ་འདྲི་བ་ལ་ནི་ཆོས་ཉིད༌[^48]དང་མཐུན་པ་དང་དགོངས་པ་བརྗོད་པའི་ཚིག་གིས་བསྟན༌[^49]ཏོ། །

[Block 65]
འདྲི་བ་གཉིས་ཀ་ལ་ནི་བརྡ་ཕྲད་དུ་རུང་བ་དང་། འདུལ་བ་ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་པས་སྟོན་ཏོ། །

[Block 66]
རྟོགས་པའི་དབང་དུ་བྱས་ནས་གདམས་ངག་འདྲི་བ་ལ་ནི་འཇིག་རྟེན་པའི་ཡོན་ཏན་སྒྲུབ་པ་དང་མཐུན་པས་སྟོན་ཏོ།[^50] །འགྲུས་སྐྱོང་ནི་འཕགས་པའི་ལམ་གྱི་ཡན་ལག་གི་ཚོགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 67]
འགྲུས་སྐྱོང་ནི་རྟག་པ་པ་དང་སྒྲིམ་པར་སྐྱོང་བ་སྟེ། རྒྱུན་དུ་གུས་པར་ཟག་པ་རྣམས་ལས་སེམས་བསྲུང་བའི་ཕྱིར་རོ། །

[Block 68]
ཡང་ན་འབྱོར་པ་ནི་འབྲེལ་པས་བཤད་དེ།

[Block 69 [VERSE]]
སྔ་ཕྱི་མ་འབྲེལ་བ་མེད་པའི་ཕྱིར་རོ། །
རྗེས་སུ་མཐུན་པ་ནི་རྗེས་སུ་འཕྲོད་པས་བཤད་དེ།
ཆོས་ཉིད་དང་མི་མཐུན་པ་མེད་པའི་ཕྱིར་རོ། །
ཐབས་དང་ལྡན་པ་ནི་འཚམ་པས་བཤད་དེ།

[Block 70]
འདུལ་བ་དང་འཚམ་པར་སྟོན་པའི་ཕྱིར་རོ། །

[Block 71]
མཐུན་པ་ནི་འགྲུས་སྐྱོང་གི་ཚོགས་ཀྱིས་བཤད་དེ། ཚངས་པར་སྤྱོད་པ་དང་མཐུན་པའི་ཕྱིར་ཏེ། དཔེར་ན་གསུང་གི་ཡན་ལག་ལྔ་བསྟན་པ་ལ་སྔ་མ་ཕྱི་མས་བསྟན་ཏེ། ཟབ་པ་འབྲུག་སྒྲས་བཤད་པ་དང་། སྙན་ཅིང་འཇེབས་པ་རྣམ་པར་སྙན་པས་བཤད་པ་དང་། ཡིད་དུ་འོང་བ་དགའ་བར་བྱེད་པས་བཤད་པ་དང་། རྣམ་པར་རིག་པར་བྱ་བ་རྣམ་པར་གསལ་བས་བཤད་པ་དང་། མཉན་པར་འོས་པ་མི་མཐུན་པ་མེད་པས་བཤད་པ་བཞིན་ནོ། །

[Block 72]
ཚིག་བཞི་པོ་ཚིག་ཕྱི་མས་བཤད་པ་དང་བཅས་པ་འདི་དག་གིས་ནི་དྲི་བ་ཐམས་ཅད་ལ་ཡོན་ཏན་བཞི་དང་ལྡན་པའི་ལན་གདབ་པར་བསྟན་པར་འགྱུར༌[^51]ཏེ། སྔ་ཕྱི་མི་འགལ་བ་དང་། ཆོས་ཉིད་དང་མི་འགལ་བ་དང་། འདུལ་བ་དང་མི་འགལ་བ་དང་། དོན་གྱི་མཆོག་དང་འབྲེལ་བའོ། །

[Block 73]
ལུང་ལས་ནི་ཡོན་ཏན་བརྒྱད་དང་ལྡན་པའི་ལན་གདབ་པར༌[^52]ནི་ཚིག་བརྒྱད་ཀྱིས་ཡོངས་སུ་བསྟན་ཏོ་ཞེས་འབྱུང་སྟེ། ཡོན་ཏན་བརྒྱད་ནི་དོན་ལ་སྦྱོར་བས་འབྱུང་བ་དང་། འཇིག་རྟེན་ལ་གྲགས་པའི་ཚིག་འབྲུ་དང་འབྲེལ་པ་དང་། རྒོལ་བ་དང་འགལ་བ་དང་མཐུན་པ་དང་། ཟབ་མོའི་ཚིག་ངེས་པའི་དོན་དང་ཉན་པ་ལ་ཕན་གདགས་པའི་ཚིག་འབྲུ་རྣམ་པར་མི་གཡེང་བའི་གཞིའི་གནས་དང་། འདུལ་བའི་བསམ་པ་དང་མོས་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་རྣམ་པར་འབྱེད་པ་དང་། ལུང་ནོད་པ་དང་། ཁ་ཏོན་དང་། འཛིན་པ་དང་། སེམས་པ་དང་། སྒོམ་པ་མི་གཏོང་བ་དང་། སྒྲ་ཅི་བཞིན༌[^53]དུ་མངོན་པར་ཞེན་པ་མེད་པར་སྟོན་པའོ། །

[Block 74]
བྱ་བ་རྣམས་ལ་ཇི་ལྟ་བ་བཞིན་དུ་སྡུག་བསྔལ་བ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་བརྗོད་པར་བྱའོ། །

[Block 75 [HEADING]]
### འཇིགས་པ་རྣམས་ཀྱི་དོན་གྱི་མདོ། ^2-4-0
--- END BLOCKS ---
