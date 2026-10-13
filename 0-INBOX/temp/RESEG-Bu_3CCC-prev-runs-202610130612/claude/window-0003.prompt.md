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
གལ་ཏེ་ཡོད་པར་གྱུར་ན་རྟག་ཏུ་ཐམས་ཅད་ལས་ཐམས་ཅད་སྐྱེ་བར་འགྱུར་རོ། །

[Block 107]
དེ་ལྟ་ཡིན་ན་རྩོམ་པ་ཐམས་ཅད་དོན་མེད་པ་ཉིད་དུ་འགྱུར་བས་དེ་ཡང་མི་འདོད་དེ། དེའི་ཕྱིར་རྐྱེན་དང་མི་ལྡན་པའི་བྱ་བ་ཡང༌[^76]མི་འཐད་དོ། །

[Block 108]
འདིར་སྨྲས་པ།

[Block 109 [VERSE]]
རེ་ཞིག་རྐྱེན་རྣམས་ནི་ཡོད་དོ། །
དེ་དག་ཡོད་པས་དངོས་པོ༌[^77]འགྲུབ་པོ། །
དེ་གྲུབ་པས་སྐྱེ་བ་འགྲུབ་པོ། །

[Block 110]
བཤད་པ། བྱ་བ་མི་ལྡན་རྐྱེན་མ་ཡིན། །གང་དག་ལ་བྱ་བ་མེད་པ་དེ་དག་ནི་རྐྱེན་མ་ཡིན་ནོ། །ཇི་ལྟར་ཞེ་ན། མིག་ལ་སོགས་པ་ནི་སྐྱེ་བའི་བྱ་བ་སྒྲུབ་པར༌[^78]བྱེད་པས་རྣམ་པར་ཤེས་པའི་རྐྱེན་དུ་འགྱུར་ན། སྐྱེ་བའི་བྱ་བ་དེ་མི་འཐད་པར་ནི་སྔར་རབ་ཏུ་བསྟན་ཟིན་ཏོ། །

[Block 111]
དེ་མེད་པའི་ཕྱིར་དེ་སྒྲུབ་པར་བྱེད་པ་ཡོད་པར་ག་ལ་འགྱུར། དེ་སྒྲུབ་པར་བྱེད་པ་མེད་པའི་ཕྱིར་མིག་ལ་སོགས་པ་སྐྱེ་བར༌[^79]བྱ་བའི་རྐྱེན་མ་ཡིན་ནོ། །

[Block 112]
སྐྱེ་བར༌[^80]བྱ་བའི་རྐྱེན་མ་ཡིན་ན་ཇི་ལྟར་རྐྱེན་དུ་འགྱུར། ཅི་སྟེ་འགྱུར་ན་ནི་ཐམས་ཅད་ཀྱང་ཐམས་ཅད་ཀྱི་རྐྱེན་དུ་འགྱུར་རོ། །

[Block 113]
དེ་ལྟ་ཡིན་ན་ཐམས་ཅད་ལས་ཐམས་ཅད་སྐྱེ་བར་འགྱུར་བ་ཞིག་ན། དེ་ལྟར་ཡང་མི་འགྱུར་ཏེ། དེའི་ཕྱིར༌[^81]བྱ་བ་དང་མི་ལྡན་པ་རྣམས་རྐྱེན་མ་ཡིན་ནོ། །

[Block 114]
སྨྲས་པ། ཅི་ཁོ་བོ་རྐྱེན་རྣམས་བྱ་བ་དང་མི་ལྡན་ནོ་ཞེས་སྨྲའམ། འདི་ལྟར་རྐྱེན་རྣམས་ནི་བྱ་བ་དང་ལྡན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 115]
བཤད་པ། བྱ་བ་ལྡན་ནམ་འོན་ཏེ་ན་མ་ཡིན་ཞེས་བྱ་བའི་སྐབས་དེ་དང་སྦྱར་ཏེ་རྐྱེན་རྣམས་བྱ་བ་དང་ལྡན་པ་མ་ཡིན་ནོ། །

[Block 116]
བྱ་བ་རྐྱེན་དང་ལྡན་པ་མ་ཡིན་པ་དང་རྐྱེན་དང་མི་ལྡན་པ་མེད་པ་དེ་ནི་སྔར་རབ་ཏུ་བསྟན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 117]
བྱ་བ་མེད་ན་ཇི་ལྟར་རྐྱེན་རྣམས་བྱ་བ་དང་ལྡན་པར་འགྱུར། དེ་ལྟར་ན་གང་གི༌[^82]ཕྱིར་བྱ་བ་དང་མི་ལྡན་པའི་རྐྱེན་ཀྱང་མི་འཐད་ལ། བྱ་བ་དང་ལྡན་པ་ཡང་མེད་པས་དེའི་ཕྱིར་རྐྱེན་དུ་རྣམ་པར་བརྟག་པ༌[^83]ནི་དོན་མེད་པ་ཉིད་དོ། །

[Block 118]
འདིར་སྨྲས་པ། ཅིའི་རྐྱེན་རྣམས་བྱ་བ་དང་མི་ལྡན་ནོ་ཞེའམ། བྱ་བ་དང་ལྡན་ནོ་ཞེས་བྱ་བ་མི་དགོས་པ་བསམ་པ་འདིས་ཅི་བྱ། གང་གི་ཕྱིར་རྣམ་པ་ཐམས་ཅད་དུ་རྒྱུ་ལ་སོགས་པའི༌[^84]རྐྱེན་བཞི་པོ་དེ་དག་ལ༌[^85]བརྟེན་ནས་དངོས་པོ་རྣམས་སྐྱེ་བས་དེའི་ཕྱིར་དེ་དག་དངོས་པོའི་རྐྱེན་ཡིན་ནོ། །

[Block 119]
བཤད་པ། ཅི་ཁྱོད་ནམ་མཁའ་ལ་ཁུ་ཚུར་དག་གིས་བརྡེག་གམ། གང་གི་ཚེ་སྐྱེ་བའི་བྱ་བ་མེད་པ་ཁོ་ན་སྟེ༌[^86]དེ་མེད་པའི་ཕྱིར་རྐྱེན་རྣམས་མི་འཐད་དོ་ཞེས་སྔར་བསྟན་པའི་ཚེ་དེ་དག་ལ་བརྟེན་ནས་དངོས་པོ་རྣམས་སྐྱེ་བ༌[^87]ཞེས་བྱ་བ་དེ་ཇི་ལྟར་སྨྲ་བར་འཐད། ཡང་གཞན་ཡང་། འདི་དག་ལ་བརྟེན་སྐྱེ་བས་ན། །དེ༌[^88]ཕྱིར་འདི་དག་རྐྱེན་ཞེས་གྲགས།[^89] །

[Block 120 [VERSE]]
ཇི་སྲིད་མི་སྐྱེ་དེ་སྲིད་དུ། །
འདི་དག་རྐྱེན་མིན་ཇི་ལྟར་མིན། །

[Block 121]
གལ་ཏེ་འདི་དག་ལ༌[^90]བརྟེན་ནས་སྐྱེ་བས་རྐྱེན་ཡིན་ནོ་ཞེས་དེ་ལྟར་རྟོག་ན། ཇི་སྲིད་དུ་མི་སྐྱེ་བ་དེ་སྲིད་དུ་རྐྱེན་མ་ཡིན་ནོ་ཞེས་བྱ་བར་ཡང་ཅིའི་ཕྱིར་མི་བརྟག །ཅི་སྟེ་སྔར་རྐྱེན་དུ་མ་གྱུར་པ་ཕྱིས་རྐྱེན་དུ་འགྱུར་བར་སེམས་ན། དེ་ཡང་མི་འཐད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། ཐམས་ཅད་ཀྱི་རྐྱེན་དུ༌[^91]ཐལ་བར་འགྱུར་བའི་ཕྱིར་དེ་ཡང་མི་འདོད་དོ། །

[Block 122]
ཅི་སྟེ་རྐྱེན་མ་ཡིན་པ་དག་ཀྱང་གཞན་འགའ་ཞིག་ལ་ལྟོས་ནས་རྐྱེན་དུ་འགྱུར་ཏེ། དེས་ན་ཐམས་ཅད་ཀྱི་རྐྱེན༌[^92]དུ་ཐམས་ཅད་ཐལ་བར་མི་འགྱུར་བར་སེམས་ན། དེ་ལ་ཡང་དེ་ཉིད༌[^93]དོ། །

[Block 123]
གང་ཡང་རུང་བ་ལ་ལྟོས་ནས་རྐྱེན་མ་ཡིན་པ་ཡང་རྐྱེན་ཉིད་དུ་འགྱུར་ན། རྐྱེན་ཉིད་དེ་ལ་ཡང་རྐྱེན་ཡོད་པར་འགྱུར་ཞིང་། དེ་ལ་ཡང་དེ་ལྟར་བསམ་དགོས་སོ། །

[Block 124]
ཐུག་པ་མེད་པའི་སྐྱོན་དུ་ཡང་འགྱུར་ཏོ།[^94] །གལ་ཏེ་གཞན་ཡང་གཞན་འགའ་ཞིག་ལ་ལྟོས་ནས་རྐྱེན་ཉིད་དུ་འགྱུར་ན། དེ་ཡང་གཞན་ལ་ལྟོས་ལ་དེ་ཡང་གཞན་ལ་ལྟོས་པས་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དོ། །

[Block 125]
དེའི་ཕྱིར་རྐྱེན་རྣམས་མི་འཐད་པ་ཁོ་ནའོ། །

[Block 126]
ཡང་གཞན་ཡང་། མེད་དམ་ཡོད་པའི་དོན་ལ་ཡང་། །རྐྱེན་ནི་རུང་བ་མ་ཡིན་ནོ།[^95] །

[Block 127 [VERSE]]
མེད་ན་གང་གི་རྐྱེན་དུ་འགྱུར། །
ཡོད་ན་རྐྱེན་གྱིས་ཅི་ཞིག་བྱ། །

[Block 128]
འདི་ལ་བརྟེན༌[^96]ནས་འདི་སྐྱེའོ་ཞེས་པའི༌[^97]འབྲེལ་པ་འདིས་དོན་འདིའི་རྐྱེན་འདིའོ་ཞེས་ཟེར་ན། འདིའོ་འདིའོ་ཞེས་བྱ་བའི་འབྲེལ་པ་དེ་ཡང་དོན་མེད་པའམ་ཡོད་པའི་རྐྱེན་ཉིད་དུ་བརྟག་གྲང་ན། དོན་མེད་པ་དང་ཡོད་པའི་རྐྱེན་འདིའོ་ཞེས་བྱ་བར་མི་རུང་ངོ་། །ཇི་ལྟར་ཞེ་ན།

[Block 129 [VERSE]]
མེད་ན་གང་གི་རྐྱེན་དུ་འགྱུར། །
ཡོད་ན་རྐྱེན་གྱིས་ཅི་ཞིག་བྱ། །

[Block 130]
དངོས་པོ་མེད་པའི་རྐྱེན་དུ་བརྟགས༌[^98]ན་རྐྱེན་འདི་གང་གི་ཞེས་ཟེར་བ་ལ་ཇི་སྐད་བརྗོད་པར་བྱ། འདི་ལྟར་སྣམ་བུ་མེད་པའི་རྐྱེན་རྒྱུ་སྤུན་དག་ཡིན་ནོ་ཞེས་བསྟན་པར་མི༌[^99]རིགས་སོ། །

[Block 131]
སྨྲས་པ། རྒྱུ་སྤུན་དག་ལས་སྣམ་བུ་འབྱུང་བས་ཕྱིས་འབྱུང་བའི་ཚུལ་གྱིས་རྒྱུ་སྤུན་དག་སྣམ་བུའི་རྐྱེན་ཡིན་པར་བསྟན་དུ་རུང་ངོ་། །བཤད་པ། ཅི་ཁྱོད་བུ་མ་འབྱུང་བའི་ནོར་གྱིས་བུའི་མ༌[^100]ཁ་དྲངས་པར༌[^101]འདོད་དམ། དངོས་པོ་མེད་པའི་རྐྱེན་མི་འཐད་དོ་ཞེས་སྨྲས་ཏེ། རྐྱེན་མི་འཐད་པས་དངོས་པོ་སྐྱེ་བ་བཀག་བཞིན་དུ་ཁྱོད་མ་འོངས་པའི་དངོས་པོ་སྐྱེ་བས་རྐྱེན་ཉིད་བསྒྲུབ་པར༌[^102]འདོད་དོ།[^103] །གང་གི་ཚེ་གང་དུ་དུས་ལ་ལར་ཡང་།

[Block 132 [VERSE]]
དངོས་པོ་སྐྱེ་བ་མེད་པ་ལ། །
མེད་ན་གང་གི༌[^104]རྐྱེན་དུ་འགྱུར། །

[Block 133]
ཞེས་བྱ་བ་འདི་ཉེ་བར་གནས་པ་དེའི་ཚེ་དངོས་པོ་ཕྱིས་སྐྱེ་བར་འགྱུར་བ་དེ་ལ་ལྟོས་ནས་ཁྱེད་ཀྱི་རྐྱེན་འགྲུབ་པར་འགྱུར་བ་གང་ལ༌[^105]ཡོད། དེ་ལྟ་བས་ན་དེ་ནི་གྱི་ནའོ། །

[Block 134]
དེ་ལ་འདི་སྙམ་དུ་ཡོད་པའི་རྐྱེན་དུ་འགྱུར་སེམས་ན། བཤད་པ། ཡོད་ན་རྐྱེན་གྱིས་ཅི་ཞིག་བྱ། །དངོས་པོ་ཡོད་པ་ལ་རྐྱེན་མི་འཐད་དོ། །

[Block 135]
འདི་ལྟར་ཡོད་པ་ལ་ཡང་རྐྱེན་གྱིས་ཅི་ཞིག་བྱ་སྟེ། སྣམ་བུ་གྲུབ་ཅིང་ཡོད་པའི་རྐྱེན་རྒྱུ་སྤུན་དག་ཡིན་ནོ། །ཞེས་བསྟན་པར་མི་རིགས་སོ། །

[Block 136]
སྨྲས་པ། ཁོ་བོ་སྐྱེས་པ་ལ་ཡང༌[^106]རྐྱེན་གྱི་བྱ་བ་ཡོད་དོ་ཞེས་མི་སྨྲ་སྟེ་འོན་ཀྱང་སྣམ་བུ་ཡོད་པའི་རྐྱེན་རྒྱུ་སྤུན་ཡིན་པར་ཐ༌[^107]སྙད་འདོགས་པར་བྱེད་པས༌[^108]སྣམ་བུ༌[^109]དེའི་རྐྱེན་རྒྱུ་སྤུན་དག་ཡིན་ནོ། །

[Block 137]
བཤད་པ། ཅི་ཁྱོད་རང་གི་ཆུང་མ་མ་བླངས་པར་བུའི་ཆུང་མ་བླང་བར་སེམས་སམ། དངོས་པོ་ཡོད་པ་སྐྱེ་བའི༌[^110]རྐྱེན་མི་འཐད་པས་དངོས་པོ་སྐྱེ་བ་བཀག་བཞིན་དུ་ཁྱོད་སྣམ་བུ་སྐྱེས་པའི་རྐྱེན་སྟོན་པར་བྱེད་འདོད་ཀོ །འོ་ན་ནི་དངོས་པོ་སྐྱེ་བ་སྒྲུབ་པའི་ཕྱིར་ཇེ་སྒྲིམས་ཤིག་དང་དེའི་འོག་ཏུ་འདིའི་རྐྱེན་འདིའོ། །ཞེས་བྱ་བ་དེ་འཐད་པར་འགྱུར་རོ། །

[Block 138]
དེ་ལྟ་བས་ན་དེ་ཡང་གྱི་ནའོ། །

[Block 139]
འདིར་སྨྲས་པ། འདི་ལ་དངོས་པོ་རྣམས་ནི་མཚན་ཉིད་ལ༌[^111]འགྲུབ་ལ། རྒྱུ་ནི་སྒྲུབ་པར་བྱེད་པའོ། །ཞེས་རྒྱུའི་མཚན་ཉིད་ཀྱང་བསྟན་པས་དེ་ལྟར་མཚན་ཉིད་ཡོད་པའི་རྒྱུ་ཡོད་དེ། བཤད་པ། གང་ཚེ་ཆོས་ནི་ཡོད་པ་དང་། །མེད་དང་ཡོད་མེད་མི་འགྲུབ་པས།[^112] །

[Block 140 [VERSE]]
ཇི་ལྟར་སྒྲུབ་བྱེད་རྒྱུ་ཞེས་བྱ། །
དེ་ལྟར་ཡིན་ན་མི་རིགས་སོ། །

[Block 141]
འདི་ལ་ཆོས་གང་རྒྱུས་སྒྲུབ་པར་གྱུར་ན་དེ་ཡོད་པའམ་མེད་པའམ་ཡོད་མེད་ཅིག་སྒྲུབ་པར་འགྱུར་གྲང་ན། རྣམ་པ་ཐམས་ཅད་མི་འཐད་དོ། །

[Block 142]
དེ་ལ་རེ་ཞིག་ཡོད་པ་ནི་སྒྲུབ་པར་མི་བྱེད་དེ། སྐྱེས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 143]
འདི་ལྟར་སྐྱེས་པ་ལ་ཡང་སྐྱེ་བས་ཅི་བྱ་སྟེ། [^113]ཅི་སྟེ་ཡོད་ཀྱང་ཡང་སྐྱེ་བ་ནི༌[^114]ནམ་ཡང་མི་སྐྱེ་བར་མི་འགྱུར་བས་དེ་ཡང་མི་འདོད་དོ། །

[Block 144]
རྒྱུར་བསྟན་དུ་ཡང་མི་འཐད་དེ། འདི་ལྟར་ཡོད་པ་ལ་རྒྱུས་ཅི་བྱ། འདི་ལྟར༌[^115]རེ་ཞིག་ཡོད་པ་ནི་སྒྲུབ་པར་མི་བྱེད་དོ། །

[Block 145]
ད་ནི་མེད་པ་ཡང་སྒྲུབ་པར་མི་བྱེད་དེ་མེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
