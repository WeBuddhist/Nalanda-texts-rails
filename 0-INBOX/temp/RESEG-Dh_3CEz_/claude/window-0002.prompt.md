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
གླེང་གཞི་ནི་འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་བྱ་བས་ནི་སྡུད་པ་པོ་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏོ།[^35] །

[Block 72]
སྔར་བསྟན་པའི་ཡོན་ཏན་དང་ལྡན་པའི་ས་བཅུའི་བྱང་ཆུབ་སེམས་དཔའ་རྡོ་རྗེ་སྙིང་པོའོ། །

[Block 73]
དུས་གཅིག་ནི༌[^36]ཕུན་སུམ་ཚོགས་པ་སྟེ། སྟོན་པ་གནས་དང་འཁོར་ལ་སོགས།[^37] །འདུས་པ་དུས་ཞེས་བཤད་པ་ཡིན། །ཞེས་པ་མདོ་ལ་སོགས་པ་ལྟར་དཔྱིད་ཟླ་ར་བ་ལ་སོགས་པ་བསྟན་པ་བཞིའི་དུས་སོ། །

[Block 74]
སྟོན་པ་ནི་བྷ་ག་ཝཱན་ཏེ་གོང་མ་ལྟར་སྤངས་པ་དང་། ཡེ་ཤེས་ཏེ་དེ་དང་ལྡན་པའི་རྒྱུའི་རྡོ་རྗེ་འཆང་རིགས་བདུན་པ་སྟེ་དེ་ཡང་འོག་ཏུ་འཆད་དེ།

[Block 75 [VERSE]]
ཞལ་བརྒྱད་ཕྱག་ནི་བཅུ་དྲུག་སྟེ། །
དཔའ་བོ་ཐོད་པའི་ཕྲེང་བ་ཅན། །
ཕྱག་རྒྱ་ལྔ་ནི་འཛིན་ལྷ་ལ། །
བདག་མེད་མ་ནི་ཉིད་ཀྱིས་ཞུས། །

[Block 76]
གསུངས་པས་དེའི་དགོངས་པ་ཡང་རྒྱུའི་རྡོ་རྗེ་འཆང་འཆད་པ་པོར་འདོད་དོ། །

[Block 77]
གནས་ཕུན་སུམ་ཚོགས་པ་ནི་སརྦ་ཏ་ཐཱ་ག་ཏ་ནས་བྷ་ག་ག་ལའི་བར་ཏེ་ཁྲོ་བ་དང་ཆགས་པས་འདུལ་བ་ལ་ཕྱི་ཆོས་འབྱུང༌[^38]བ་དེར་ཐོས་སོ། །

[Block 78]
འཁོར་ཕུན་སུམ་ཚོགས་པ་ནི་རྣལ་འབྱོར་གྱི་དབང་ཕྱུག་བྱེ་བྲག་བརྒྱད་ཅུ་སྟེ། རིགས་ལྔ་དང་བྱང་ཆུབ་སེམས་དཔའ་ས་བཅུ་ལ་གནས་པ་རྣམས༌[^39]དང་། རྡོ་རྗེ་བདག་མེད་མ་དང་སྤྱན་ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་སྤྲུལ་པ་རྡོ་རྗེ་མཁའ་འགྲོ་མ་རི་རབ་ཀྱི་རྡུལ་ཕྲ་རབ་དང་མཉམ་པ་རྣམས་ཏེ། དེ་ཡང་འོག་ལྡན་མ་དང་སྟེང་ཞལ་མ་ལ་སོགས་པས་འཆད་དོ། །

[Block 79 [HEADING]]
###### **ཉམས་སུ་ལེན་པའི་ཐབས་བསྟན་པ།** ^1-1-1-2-1-1-2-0

[Block 80]
དེ་ལྟ་བུར་བདག་གིས་ཐོབ་པར་བྱ་སྙམ་དུ་འདོད་པར་བྱ་ཞེས་བསྐྱེད་རིམ་གྱིས་དམིགས་པར་བྱས་ལ་དེ་ཉིད་ཉམས་སུ་ལེན་པ་ནི་སྒྲུབ་པ་པོ་ཐུན་མོང་དང་ཁྱད་པར་གྱི་ཡོན་ཏན་དང་ལྡན་པས། གནས་ཕུན་སུམ་ཚོགས་པ་བགེགས་དང་འཚེ་བ་མེད་པར་བྱ་བ་ལ་འཇུག་པ་སྔར་ལངས་ལ་ལྷའི་ང་རྒྱལ་གྱིས་འཆགས་ཡོད་པར༌[^40]ཕྱིན་ཏེ། བསམ་གཏན་གྱི་བར་ཆད་བསལ་ལ། འཆགས་ཆུང་ངུ་ཕྱིའི་ཁྲུས་ཙནྡན་ལ་སོགས་པ་སྦྱར་བའི་ཆུས་དབང་བསྐུར་བར་མོས་ཏེ་ཁྲུས་བྱའོ། །

[Block 81]
ནང་གི་ཁྲུས་བདུད་རྩིའི་བྱུག་པ་ལ་སོགས་པ་བྱ་བའོ།[^41] །དེ་ནས་ནང་དུ་མཎྜལ་དང་མཆོད་པ་བཤམས་ལ༌[^42]ཐང་ཀ་དང་འབུར་སྐུ་རྣམས་བཞུགས་པ༌[^43]བདག་དང་རྣལ་འབྱོར་ལ་སོགས་བསྲུང་བར༌[^44]བྱའོ། །

[Block 82]
དེ་ནས་མཆོད་པ་བྱིན་གྱིས་བརླབ་སྟེ། རང་རང་གི་ཕྱག་རྒྱ་དང་སྔགས་ཀྱི་རྫས་སུ་བྱིན་གྱིས་བརླབ་བོ། །

[Block 83]
དེ་ནས་བསོད་ནམས་ཀྱི་ཚོགས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་ལ། རེ་ཕ༌[^45]སྔོན་དུ་ཞེས་པས་ར་བ་དྲ་བ་བསྒོམས་པའི་ནང་དུ་ཨེ་ཆོས་འབྱུང་བ་ཤྲཱི་དང་ནཱའི་གནས་ལྟ་བུར་བསམ་སྟེ་དོན་ལེའུ་བརྒྱད་པར་འཆད་དོ། །

[Block 84]
ཝཾ་གཞལ་ཡས་ཁང་འབྱུང་བས༌[^46]ཆུ་མེ་རླུང་རྣམས་ཞུ་བ་ལས་བྱུང་བ་དེ་ཡང་འོག་ནས་འཆད་དོ། །

[Block 85]
ཟེའུ་འབྲུ་དང་བཅས་པར་ཐིག་ལེ་བྱང་ཆུབ་སེམས་ལས་མ༌[^47]ཡཱ་དཀྱིལ་འཁོར་གྱི་བདག་པོ་བསྒོམ་སྟེ།

[Block 86 [VERSE]]
དེ་ཡང་ཟླ་བ་མེ་ལོང་ཡེ་ཤེས་ལྡན། །
བདུན་གྱི་བདུན་པ་མཉམ་པ་ཉིད། །
རང་ལྷའི་ས་བོན་ཕྱག་མཚན་ནི། །
སོ་སོར་རྟོག་པ་ཡིན་ཞེས་ཟེར། །

[Block 87 [VERSE]]
དེ་རྣམས་གཅིག་གྱུར་བྱ་ནན་ཏན། །
རྫོགས་པ་ཆོས་དབྱིངས་དག་པའོ། །

[Block 88]
ཞེས་བྱ་བས་མངོན་པར་བྱང་ཆུབ་པ་ལྔས་རྒྱུའི་རྡོ་རྗེ་འཆང་དུ་སྤྲུལ་ལོ། །

[Block 89]
ཤྲུ་ཏ་ནི་རིག་མ་དང་བཅས་པ་བཞུགས་པ༌[^48]ལས་བྱུང་བ་དེ་ཡང་། བར་དོར་བཞུགས༌[^49]ནས་བསྲུབ་དང་བསྲུབས་པས་གཙོ་བོ་ཞུ་རིག་མ་དང་བཅས་ཏེ་ཞུ་བའོ། །

[Block 90]
དུས་གཅིག་ནི་ཞུ་བ་དང་ལྡན་པའི་རིག་མ་དང་དུས་གཅིག་པའོ། །

[Block 91]
བཅོམ་ལྡན་འདས་ནི་གླུའི་ངོར་འབྲས་བུ་ཧེ་རུ་ཀར༌[^50]ལངས་ཏེ། ཐིག་ལེ་བཞི་ཆད་ནས་རྐྱེན་གླུས་བསྐུལ་ནས་ཡུད་ཙམ་གྱིས་མངོན་པར་བྱང་ཆུབ་པ་ལྔས་བསྐྱེད་པའོ། །

[Block 92]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་ཉན་པའི་འཁོར་རྫོགས་པ་སྟེ། རང་བཞིན་སངས་རྒྱས་རྣམ་པ་རྡོ་རྗེ༌[^51]བཙུན་མོ་སྟེ། རྣལ་འབྱོར་མའི་འཁོར་རྗེས་སུ་མཐུན་པའི་བྱང་ཆུབ་པ་ལྔས་བསྐྱེད་པའོ། །

[Block 93]
དེ་ནས་ཉམས་དགའ་བའི་གྲོང་ཁྱེར་ཡིན་པས་བྷ་ག་སྟེ། ཉོན་མོངས་པ་རྣམ་པར་འཇོམས་པ་དག་པའི་ཡེ་ཤེས་དང་ལྡན་པས་སོ། །

[Block 94]
བཞུགས་སོ་ཞེས་བྱ་བས་ནི་སེམས་དཔའ་སུམ་བརྩེགས་དང་ཡེ་ཤེས་ཀྱི་འཁོར་ལོ་དགུག་པ་དང་། སྐྱེ་མཆེད་བྱིན་གྱིས་བརླབ་པ་ནི་གཙོ་བོ་ལ་བསྐྱེད་ཚུལ༌[^52]དུ་བསྒོམ་མོ། །

[Block 95]
སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་བརླབ་པ་དང་དབང་བསྐུར་བ་དང་། མཆོད་པ་དང་བསྟོད་པ་དང་བདུད་རྩི་མྱང་བ་དང་རྫོགས་པའི་རིམ་པ་ཉུང་ལྡན་དུ་བསྒོམ་མོ། །

[Block 96]
དག་པ་རྗེས་སུ་དྲན་པ་དང་སྔགས་བཟླས་པ་དང་གཏོར་མ་དང་ཡེ་ཤེས་པ་གཤེགས་པ་དང་དམ་ཚིག་པ་བསྡུ་བ་དང་བཅས་པ༌[^53]བཞུགས་སོ། །

[Block 97 [HEADING]]
###### **ཐུན་བཞིའི་རིམ་པ།** ^1-1-1-2-1-1-2-1-0

[Block 98]
དོ་ལ་མཉམ་གཞག་དང་རྗེས་ཐོབ་ཀྱི་རྟགས་འབྱུང་སྟེ། ཐུན་བཞིའི་རིམ་པར་ཞག༌[^54]གཉིས་དང་དེ་བཞིན་ཏེ་བརྟེན་པ་ཆོས་ནས་འཇུག་པ་དང་རྟེན་དང་པོ་ནང་ནས་འཇུག་པའོ། །

[Block 99 [HEADING]]
###### **དང་པོ་བརྟེན་པ་ཆོས་ནས་འཇུག་པ།** ^1-1-1-2-1-1-2-1-1-0

[Block 100]
དང་པོ་ནི་ཨེ་སྟེ་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་དང་བ༌[^55]སྟེ་ཐབས་སྣང་བ་དང་། ང་སྟེ་དབྱེར་མེད་བདག་གིས་ནི་བདག་ཉིད་དུ་ཐོས་ཤིང་གསལ་བའོ། །

[Block 101]
ཤྲུ་ཏ་སྟེ་བདེ་བ་གོང་ནས་གོང་དུ་འཕེལ་བའམ་ཡང་གསལ་རིག་གི་ཆ་མ་འགགས་པའོ། །

[Block 102]
དུས་ནི་དེ་ཉིད་སྣང་བ་དང་སྟོང་པ་དབྱེར་མེད་པའི་སྒོམ་པ་སྟེ། དེ་ཡང་ཕ་རོལ༌[^56]ཕྱིན་པ་ནི་ལུང་དང་རྒྱ་མཚོ་རིགས་པས་དཔྱད་དེ་བསྒོམས་ལ། འདིར་ནི་མན་ངག་གི་སྟོབས་ཀྱིས་ཆོས་རྣམས་ལས་ཡེ་ཤེས་སྐྱེ་བའི༌[^57]ཚུལ་དུ་བསྒོམ་མོ། །

[Block 103]
བཅོམ་ལྡན་འདས་ནི་དེས་མི་མཐུན་པ་འཇོམས་པ་དང་ཡེ་ཤེས་དང་ལྡན་པའོ། །

[Block 104]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད༌[^58]ནི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་སོགས་པའོ། །

[Block 105 [VERSE]]
སྐུ་གསུང་ཐུགས་ནི་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་མོ། །
ཧྲྀ་ད་ཡ་ནི་སྙིང་པོ་སྟེ་བསྡུས་པའམ་དཀྱིལ་ལོ། །

[Block 106]
བཙུན་མོ་ནི་ཡུམ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟེ་ཡོན་ཏན་བསྐྱེད་པའོ་ཞེས༌[^59]བཞུགས་སོ་ཞེས་པ་ནི་ཆོས་ཉིད་ཀྱིས་ཆོས་ཐམས་ཅད་ལ་ཁྱབ་པ་སྟེ། ཏིལ་ཅན་ནི་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་སོགས།

[Block 107 [VERSE]]
[^60]ཏིལ་ལ་ཏིལ་མར་ཇི་བཞིན་དུ། །
བུ་རམ་ཤིང་ལ་བུ་རམ་བཞིན། །

[Block 108]
ཞེས་པའོ། །

[Block 109 [HEADING]]
###### **རྟེན་དང་པོ་ནང་ནས་འཇུག་པ།** ^1-1-1-2-1-1-2-1-2-0

[Block 110]
རྟེན་དང་པོ་ནང་ནས་འཇུག་པ་ནི་ཨེ་སྟེ་ཤེས་རབ་ལྷ་མོ་བླ་ན་མེད་པའོ། །
--- END BLOCKS ---
