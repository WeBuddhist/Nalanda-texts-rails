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
[Block 2801]
དེ་དག་ཐམས་ཅད་ཀྱང་རྒྱལ་བ་རིགས་ལྔ་ལས་མི་འདའ་སྟེ། རྒྱུ་སེམས་ཅན་གྱི་གནས་སྐབས་ནས་སྦྱང་གཞི་རྣམ་པ་ལྔ་ཡོད་པས་དེ་སྤྱོད་བྱེད་ཀྱང་རིགས་ལྔ་སྟེ། དེ་སྐད་དུ་ཡང་།

[Block 2802 [VERSE]]
ཞི་བ་ཡི་ནི་དཀྱིལ་འཁོར་རོ། །
ཁྲོ་བོ་ཡི་ནི་དཀྱིལ་འཁོར་ཏེ། །
རྗེས་སུ་གཟུང་བ་བྱ་ཕྱིར་རམ། །
གཞན་དག་ཚར་གཅད་བྱ་ཕྱིར་བཤད། །

[Block 2803]
ཡང་ལྷ་དང་ལྷ་མོ་ཐ་དད་པ་དང་དེའི་རིགས་འབྱུང་སྟེ་དེ་མེད་ཀྱང་ནི་དེ་ཡོད་ནི། འགྲོ་བའི་དོན་དུ་བསྟན་པ་ཡིན། །ཞེས་གསུངས་སོ། །

[Block 2804]
དེ་རྣམས་ཀྱི་རྒྱུ་མཚན་ནི་འོག་ནས་འཆད་དོ། །

[Block 2805]
ཡང་རྣལ་འབྱོར་མ་རྣམས་ཀྱི་ས་བོན་ནི་ཨཱ་ལི་དང་པོ་ལ་སོགས་པ་སྟེ་དེ་བཞིན་ནོ། །

[Block 2806]
ད་ནི་རྩའི་གྲངས་ལས་རྣལ་འབྱོར་མའི་གང༌[^1184]བསྟན་པའི་ཕྱིར། རིགས་ཀྱི་ལེའུ་ལས་རྩ་རྣམས་གང་ཞེས་པ་ནི་ལེའུ་དང་པོ་ལས་སོ། །

[Block 2807]
བཅུ་དྲུག་གཉིས་གསུངས་པ་ནི་སྔོན་དུ་དྲིས་པ་སྟེ། བདེན་ཏེ་ཞེས་པ་ནི་ལྷག་མའོ། །

[Block 2808]
ཇི་ལྟ་བུ་ཞེ་ན་རྩ་ནི༌[^1185]གཉིས་གཉིས་ཞེས་པ་ནི་ཐབས་དང་ཤེས་རབ་ཀྱི་རྩ་གཉིས་སྡོམ་པའོ།[^1186] །རྣལ་འབྱོར་མ་རེ་རེ་ཞེས་པ་ནི་རྡོ་རྗེ་རྣལ་འབྱོར་མ་ལ་སོགས་པའོ། །

[Block 2809]
གསུམ་དུ་བརྗོད་ཅེས་པ་ནི་བརྐྱང༌[^1187]མ་ལ་སོགས་པའོ། །

[Block 2810]
བདག་མེད་རྣལ་འབྱོར་ཞེས་པ་ནི་རྩ་གསུམ་སྐུ་གསུང་ཐུགས་ཀྱི་རང་བཞིན་དུ་གཅིག་པའོ། །

[Block 2811]
འོ་ན་རྣལ་འབྱོར་མ་རྣམས་ཀྱི་ས་བོན་ཐ་མ་ལྷག་པ༌[^1188]དང་རྩ་རྣམས་ཀྱི་ཐ་མ་ལྷག་པ་ཅི་བྱེད་ཅེ་ན། དེའི་ཕྱིར་གང་ཕྱིར་བཅུ་དྲུག་ཆ་མེད་ཅེས་པ་ནི་དབྱངས་ཡིག་བཅུ་དྲུག་པ་མེད་པའོ། །

[Block 2812]
ཆ་མེད་ཅེས་པ་ནི་རྩ་སུམ་ཅུ་རྩ་གཉིས་པ་མེད་པའམ་བདག་མེད་མ་བཞིན་དུ་མཁའ་སྤྱོད་མ་གསུམ་འདུས་པའོ། །

[Block 2813]
འབད་པ་ནི་བླ་མ་ལས་རྙེད་པའི་མན་ངག་གིས་ཏེ་དབྱངས་ཡིག་བཅོ་ལྔ་པ་ལས་བཅུ་དྲུག་པ་ཐིག་ལེ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་རང་བཞིན་ལ་མེད་པ་དང་། དྲི་བ་དང་བརྗོད་པ་ཙམ་དུ་ནི་ཡོད་དོ། །

[Block 2814]
རྩ་བདུད་འདྲལ་མ༌[^1189]ཡང་བྱང་ཆུབ་ཀྱི་སེམས་གནས་པ་ཙམ་ལས་འཕེལ་བ་དང་འགྲིབ་པའི་བྱ་བ་མི་བྱེད་དོ། །

[Block 2815]
དེའི་ཕྱིར་སྤང་བའོ། །

[Block 2816]
དཔེར་ན་ཕྱིའི་ཟླ་བ་དཀར་པོ་དང་ནག་པོའི་ཕྱོགས་འཕེལ་བ་དང་འགྲིབ་པ་བཅོ་ལྔ་ལས་མེད་པའི་ཕྱིར་རོ། །

[Block 2817]
འོ་ན་ཕྱིའི་ཟླ་བ་མེད་པས་བཅུ་དྲུག་པ་དང་སུམ་ཅུ་རྩ་གཉིས་པ་ལས་ཅི་གནོད་ཅེ་ན་དེའི་ཕྱིར།

[Block 2818 [VERSE]]
བཅོ་ལྔའི་ཆ་ཡི་བདག་ཉིད་ཀྱི། །
ཟླ་བ་བྱང་ཆུབ་སེམས་སུ་འགྱུར། །

[Block 2819]
ཞེས་པ་སྟེ་ལུས་ལ་རྩ་གཉིས་ལ་བྱང་ཆུབ་ཀྱི་སེམས་གཡོན་ནས་འཕེལ་བ་བཅོ་ལྔ་དང་། གཡས་ནས་འགྲིབ་པ་བཅོ་ལྔ་རྒྱུ་བའི་ཕྱིར་རོ། །

[Block 2820]
དེ་དང་ས་བོན་ཡི་གེ་དག་དང་ཅི་འབྲེལ་ཞེ་ན། དེའི་ཕྱིར་བདེ་བ་ཆེན་པོ་ནི་རྟེན་ཏེ་ཞུ་བའོ། །

[Block 2821]
ཨཱ་ལི་གཟུགས་ནི་ཞུ་བའི་གནས་བཅོ་ལྔ་ལས་ཨ་ལ་སོགས་པ་བཅོ་ལྔར་འགྱུར་བ་སྟེ། དེའི་རྩ་རྣམས་ཀྱང་དེ་རྣམས་ཡིན་པའི་ཕྱིར་རྣལ་འབྱོར་མ་རྣམས་ཞེས་པ་ནི་བདག་མེད་མ་ལ་སོགས་པ་བཅོ་ལྔའོ། །

[Block 2822]
དེའི་ཆ་ནི་རྟེན་ཞུ་བ་དེ་ཡང་རྟེན་རྩའི་ཆས༌[^1190]སོ། །

[Block 2823]
ད་ནི་སྔར་གྱི་རྣམ་དག་དྲིས་པའི་ལན་དུ་བྱང་ཆུབ་ཀྱི་སེམས་བསྟན་པའི་ཕྱིར་རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པའོ། །

[Block 2824]
ག་པུར་ངེས་པར་ཅིས་མི་སྤངས། །ཞེས་པ་ནི་ཀུན་རྫོབ་མི་སྤང་བའི་ཐབས་ཏེ་དོན་དམ་ཡང་ཤུག༌[^1191]ཀྱིས་དྲིས་པའོ། །

[Block 2825]
རྣལ་འབྱོར་མ་ཀུན་ལས༌[^1192]ཞེས་པ་ནི་འཆད་པར་འགྱུར་བའི་ཤིན་ཏུ་བཞིན་བཟངས་ལ་སོགས་པ་ལས་བྱུང་བའོ། །

[Block 2826]
ལྷན་སྐྱེས་རང་བཞིན་ནི་ཀུན་རྫོབ་བོ། །

[Block 2827]
ཟག་མེད་དང་འགྲིབ་མེད་ནི་གཟུང་བའི་ཐབས་ཀྱི་མི་འབྲལ་བའོ། །

[Block 2828]
བཏུང་མཆོག་ནི་བདུད་རྩི་ཡིན་པས་སོ། །

[Block 2829]
དེས་ནི་འདི་སྐད་སྟོན་ཏེ་ཀུན་རྫོབ་ལྷན་ཅིག་སྐྱེས་པའི་ཚུལ་ནི་རྟེན་རྣལ་འབྱོར་མ་ལས་བྱུང་། གནས་པའི་ཚུལ་གཟུང་བའི་མན་ངག་བྱས་ལ་ཡོན་ཏན་བཏུང་མཆོག་སྟེ་ལུས་རྒུད་པ་ལ་སོགས་སེལ་བས་སོ། །

[Block 2830]
དེ་ལྟར་ལགས་སམ་ཞེས་ཞུས་པའོ། །

[Block 2831]
ཡང་རྣལ་འབྱོར་མ་ཀུན་ལས་བྱུང་ན་སྟོང་པ་ཤེས་རབ་ཀྱི་རང་བཞིན་ལས་སོ། །

[Block 2832]
ལྷན་ཅིག་སྐྱེས་དགའ་ནི་བདེ་བ་ཐམས་ཅད་ཀྱི་རང་བཞིན་ཏེ། དེ་ནམ་མཁའ་ཉིད་དུ་འབྲེལ་ཏེ་ནམ་མཁའི་རང་བཞིན་གཉིས་སུ་མེད་ཅིང་བདག་མེད་པའོ། །

[Block 2833]
དེས་ཀྱང་འདི་སྐད་དུ་སྟོན་ཏེ་རྣལ་འབྱོར་མ་ཀུན་ལས་བྱུང་བའི་ཆོས་ཀྱི་སྐུ་ལྷན་ཅིག་སྐྱེས་དགའ་ལོངས་སྐུ་འཁྱུད་ནས། ནམ་མཁའ་དབྱེར་མེད་བདེ་ཆེན་གྱི་སྐུ་ལགས་སམ་ཞེས་ཞུས་པའོ། །

[Block 2834]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་ཞེས་པ་ནི་ཡིན་པར་ཞུས་སོ། །

[Block 2835]
ཇི་སྐད་སྨྲས་པ་དེ་བཞིན་ཞེས་པ་ནི། བདུད་རྩི་དང་བདེ་ཆེན་གྱི་སྐུར་བྱས་པ་སྟེ་བསྟན་པའོ། །

[Block 2836]
དེ་བཤད་པ་ཡང་རྡོ་རྗེ་སྙིང་པོས་གསོལ་ཞེས་པ་ནི་བདག་གི་ཡིན་ཡང་དེ་ལས་རྒྱས་པར་རོ། །

[Block 2837]
ཐབས་གང་གིས་བསྐྱེད་ལགས་ཞེས་པ་ནི་ལམ་རིམ་པ་གཉིས་དྲིས་པའོ། །

[Block 2838]
མ་བསྐྱེད་ན་བསོད་ནམས་མེད་ཅིང༌[^1193]སྡིག་པ་མེད་པས་བསྐྱེད་དེ་མི་སྤང་བར་ཞུས་པ་ཡང་བཀའ་སྩལ་ཞིང་རིམ་གཉིས་སུའོ། །

[Block 2839]
དཀྱིལ་འཁོར་ནི་རྟེན་གྱི༌[^1194]རྣལ་འབྱོར་རོ། །

[Block 2840]
འཁོར་ལོ་ནི་བརྟེན་པའོ། །
--- END BLOCKS ---
