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
[Block 246]
འདི་ལ་གལ་ཏེ་འགྲོ་བ་ཞིག་ཡོད་པར་གྱུར་ན། དེ་སོང་བ་ལའམ། མ་སོང་བ་ལ་ཡོད་པར་འགྱུར་གྲང་ན། དེ་ལ་རེ་ཞིག་སོང་བ་ལ་ནི་འགྲོ་བ་མེད་དོ། །

[Block 247 [VERSE]]
འགྲོ་བའི་བྱ་བ་འདས་ཟིན་པའི་ཕྱིར་རོ། །
མ་སོང་བ་ལ་ཡང་འགྲོ་བ་མེད་དེ།
འགྲོ་བའི་བྱ་བ་མ་བརྩམས་པའི་ཕྱིར་རོ། །

[Block 248]
སྨྲས་པ། དེ་ནི་དེ་བཞིན་ཏེ། སོང་བ་དང་མ་སོང་བ་ལ་འགྲོ་བ་མེད་མོད་ཀྱི། འོན་ཀྱང་བགོམ་པ་ལ་འགྲོ་བ་ཡོད་དོ། །

[Block 249]
བཤད་པ།

[Block 250 [VERSE]]
སོང་དང་མ་སོང་མ་གཏོགས་པར། །
བགོམ་པ་ཤེས་པར་མི་འགྱུར་རོ། །

[Block 251]
སོང་བ་དང་མ་སོང་བ་མ་གཏོགས་པར་བགོམ་པ་ཅི་ཞིག༌[^180]ཡོད་དོ། །ཤེས་པར་མི་འགྱུར་རོ། །ཇི་ལྟར་ཞེ་ན། འདི་ལྟར། ཤེས་པར་མི་འགྱུར་རོ། །ཞེས་བྱ་བ་ནི། གཟུང་དུ་མེད་པས་ཏེ་མི་འཐད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 252]
དེ་ལྟར་གང་གི་ཕྱིར་སོང་བ་དང་མ་སོང་བ་མ་གཏོགས་པར་བགོམ་པ་གཟུང་དུ་མེད་པ་ཁོ་ན་སྟེ༌[^181]མི་འཐད་པ་དེའི་ཕྱིར་མེད་པ་ཁོ་ན་ཡིན་པས་འགྲོ་བ་མེད་དོ། །

[Block 253]
སྨྲས་པ། བགོམ་པ་ཁོ་ན་ཡིན་ཏེ། དེ་ལ་འགྲོ་བ་ཡོད་དོ། །ཇི་ལྟར་ཞེ་ན།

[Block 254 [VERSE]]
གང་ན་གཡོ་བ་དེ་ན་འགྲོ། །
དེ་ཡང་གང་གི་བགོམ་པ་ལ། །
གཡོ་བ་སོང་མིན་མ་སོང་མིན། །
དེ་ཕྱིར་བགོམ་ལ་འགྲོ་བ་ཡོད། །

[Block 255]
འདི་ལ་ཁྱོད་ཀྱི་འགྲོ་བ་མེད་པའི་གཏན་ཚིགས་སུ་འགྲོ་བའི་བྱ་བ་འདས་ཟིན་པ་དང་མ་བརྩམས་པ་བསྟན་པ་དེའི་ཕྱིར། གང་ན་གཡོ་བ་དེ་ན་འགྲོ། །ཞེས་བྱ་བ་འདི་འབྱུང་བར་འགྱུར་ཏེ། དེ་ཡང་གང་གི་བགོམ་པ་ལ་གཡོ་བ་དེ༌[^182]དམིགས་པ་ནའོ། །

[Block 256]
གང་གི་ཞེས་བྱ་བ་ནི་འགྲོ་བ་པོའི་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 257]
དེ་ལྟར་གང་གི་ཕྱིར་གཡོ་བ་ནི་སོང་བ་ལ༌[^183]མེད། མ་སོང་བ་ལ་ཡང་མེད་ཀྱི་བགོམ་པ་ལ་ཡོད་པ་དེའི་ཕྱིར་གང་ན་གཡོ་བ་ཡོད་པ་དེ་ན་འགྲོ་བ་ཡོད་དོ། །

[Block 258]
དེ་ལྟར་འགྲོ་བ་ཡོད་པས་བགོམ་པ་ལ་འགྲོ་བ་ཡོད་དོ། །

[Block 259]
བཤད་པ།

[Block 260 [VERSE]]
བགོམ་ལ་འགྲོ་བ་ཡོད་པར་ནི། །
ཇི་ལྟ༌[^184]བུར་ན་འཐད་པར་འགྱུར། །
གང་ཚེ་འགྲོ་བ་མེད་པ་ཡི། །
བགོམ་པ་འཐད་པ་མེད་ཕྱིར་རོ། །

[Block 261]
འདི༌[^185]ལ་ཁྱོད་འགྲོ་བ་དང་ལྡན་པས་བགོམ་པར་འདོད་ལ་དེ་ལ་འགྲོ་བ་ཡོད་དོ་ཞེས་ཟེར་ན་འདི་ལ་འགྲོ་བའི་བྱ་བ་ནི་གཅིག་ཏུ་ཟད་ལ། དེ་ནི་བགོམ་པ་ཞེས་བྱ་བ་དེ་ལ་ཉེ་བར་སྦྱར་བས་དེའི་ཕྱིར་འགྲོ་བ་ཞེས་བྱ་བ་དེ་ནི་འགྲོ་བའི་བྱ་བ་དང་བྲལ་བས་འགྲོ་བ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 262]
དེ་ཡང་མི་འཐད་དེ། འདི་ལྟར་འགྲོ་བ་མེད་པར་ཇི་ལྟར་འགྲོ་བར་འགྱུར། དེ་ལ་གང་གི་ཚེ་འགྲོ་བ་ཞེས་བྱ་བ་དེ་འགྲོ་བའི་བྱ་བ་དང་བྲལ་བས་མི་འཐད་པས༌[^186]དེའི་ཚེ་བགོམ་པ་ལ་འགྲོ་བ་ཡོད་པར་ཇི་ལྟར་འཐད་པར་འགྱུར།

[Block 263]
ཡང་གཞན་ཡང་། བཤད་པ།

[Block 264 [VERSE]]
གང་གི་བགོམ་ལ་འགྲོ་ཡོད་པ། །
དེ་ཡི་བགོམ་ལ༌[^187]འགྲོ་མེད་པར། །
ཐལ་བར་འགྱུར་ཏེ་གང་གི་ཕྱིར།

[Block 265]
[^188] །བགོམ་པ་ཁོང་དུ་ཆུད་ཕྱིར་རོ། །

[Block 266]
གང་གི་བློ་ལ་སྐྱོན་དེར་གྱུར་ན་མི་རུང་ངོ་སྙམ་པས་འགྲོ་བ་ཞེས་བྱ་བ་དེ་འགྲོ་བ་དང་ལྡན་པས་འགྲོ་བར་སེམས་པ་དེའི་ཡང་འགྲོ་བ་འགྲོ་བ་ཞེས་བྱ་བ་དེ་ལ་ཉེ་བར་སྦྱར་བ་བྱས་པས་བགོམ་པ་ནི་འགྲོ་བ་མེད་པ་འགྲོ་བ་དང་བྲལ་བ་གྲོང་དང་གྲོང་ཁྱེར་ལྟ་བུར་ཐལ་བར་འགྱུར་ཏེ། དཔེར་ན་གྲོང་འགྲོ་ཞེས་བྱ་བ་དེ་བཞིན་དུ་བགོམ་པ་ཡང་ཐལ་བར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དེ། དེའི་ཕྱིར་བགོམ་པ་ལ་འགྲོ་བ་ཡོད་དོ། །ཞེས་བྱ་བ་དེ་ཇི་ལྟར་ཡང་མི་འཐད་དོ། །

[Block 267]
ཅི་སྟེ་སྐྱོན་དེར་གྱུར་ན་མི་རུང་ངོ་སྙམ་པས་འགྲོ་ཞེས་བྱ་བ་དེ་དང་བགོམ་པ་ཞེས་བྱ་བ་དེ་གཉིས་ཀ༌[^189]ཡང་འགྲོ་བ་དང་ལྡན་པར་སེམས་ན། དེ་ལ་སྐྱོན་འདི་ཡོད་དེ། བཤད་པ།

[Block 268 [VERSE]]
བགོམ་ལ་འགྲོ་བ་ཡོད་ན་ནི། །
འགྲོ་བ་གཉིས་སུ་ཐལ༌[^190]འགྱུར་ཏེ། །
གང་གིས་བགོམ་པ་དེ་དང་ནི། །
དེ་ལ་འགྲོ་བ་གང་ཡིན་པའོ། །

[Block 269]
བགོམ་པ་འགྲོ་བ་དང་ལྡན་པ་ལ་འགྲོ་བར་བརྟགས༌[^191]ན། འགྲོ་བ་གཉིས་སུ་ཐལ་བར་འགྱུར་ཏེ། འགྲོ་བ་དང་ལྡན་པས་བགོམ་པ་ཞེས་བྱ་བར་འགྱུར་བ་དང་། དེ་ལ་འགྲོ་བ་ཞེས་བྱ་བའི་འགྲོ་བ་གཉིས་པར་བརྟག་པའོ། །

[Block 270]
འགྲོ་བ་གཉིས་སུ་ནི་མི་འདོད་པས་དེའི་ཕྱིར་དེ་ཡང་མི་འཐད་དོ། །

[Block 271]
དེ་ལ་སྐྱོན་གཞན་འདི་ཡང་ཡོད་དོ།[^192] །

[Block 272]
བཤད་པ།

[Block 273 [VERSE]]
འགྲོ་བ་གཉིས་སུ་ཐལ་འགྱུར༌[^193]ན། །
འགྲོ་བ་པོ་ཡང་གཉིས་སུ་འགྱུར། །
གང་ཕྱིར་འགྲོ་པོ་མེད་པར་ནི། །
འགྲོ་བ་འཐད་པར་མི་འགྱུར་ཕྱིར། །

[Block 274]
འགྲོ་བ་གཉིས་སུ་ཐལ་བར་འགྱུར༌[^194]ན་འགྲོ་བ་པོ་ཡང་གཉིས་སུ་ཐལ་བར་འགྱུར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན།

[Block 275 [VERSE]]
གང་ཕྱིར་འགྲོ་པོ་མེད་པར་ནི། །
འགྲོ་བ་འཐད་པར་མི་འགྱུར་ཕྱིར། །

[Block 276]
གང་གི་ཕྱིར་འགྲོ་བ་པོ་ཡོད་ན་འགྲོ་བ་ཡང་ཡོད་ཀྱི། འགྲོ་བ་པོ་སྤངས་ན་འགྲོ་བ་མེད་པ་དེའི་ཕྱིར་འགྲོ་བ་གཉིས་སུ་ཐལ་བར་འགྱུར༌[^195]ན་འགྲོ་བ་པོ་ཡང་གཉིས་སུ་ཐལ་བར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དེ། དེའི་ཕྱིར་དེ་ལྟར་སྐྱོན་དུ་མ་ཡོད་པས་བགོམ་པ་ལ་འགྲོ་བ་མེད་པ་ཉིད་དོ། །

[Block 277]
གང་གི་ཕྱིར་སོང་བ་དང་མ་སོང་བ་དང་བགོམ་པ་ལ་འགྲོ་བ་མི་འཐད་པ་དེའི་ཕྱིར་འགྲོ་བ་མེད་པ་ཁོ་ནའོ། །

[Block 278]
འདིར་སྨྲས་པ། སོང་བ་དང་མ་སོང་བ་དང་བགོམ་པ་ལ་འགྲོ་བ་མི་འཐད་དུ་ཟིན་ཀྱང་། འགྲོ་བ་པོ་ལ་བརྟེན་པའི་འགྲོ་བ་ཡོད་པ་ཉིད་དེ། འདི་ལྟར་འགྲོ་བ་པོ་ལ་འགྲོ་བ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 279]
བཤད་པ།

[Block 280 [VERSE]]
གལ་ཏེ་འགྲོ་པོ་མེད་གྱུར་ན། །
འགྲོ་བ་འཐད་པར་མི་འགྱུར་ཏེ། །

[Block 281]
འགྲོ་པོ་མེད་པར་གྱུར་ན་འགྲོ་བ་འཐད་པར་མི་འགྱུར་བར་ནི་སྔར་བསྟན་ཟིན་ཏོ། །

[Block 282]
གལ་ཏེ་འགྲོ་བ་པོ་མེད་པར་གྱུར་ན་འགྲོ་བ་འཐད་པར་མི་འགྱུར་ན་གང་འགྲོ་བ་པོ་ལ་བརྟེན༌[^196]ཅིང་འགྲོ་བ་པོ་ལ་འཇུག་པའི་འགྲོ་བ་དེ་གང་ཡིན། སྨྲས་པ། གང་འགྲོ་བ་པོ་ལ་འཇུག་པའི་འགྲོ་བ་གཞན་འགྲོ་བ་པོ་ལས་ཐ་དད་དུ་གྱུར་པ་ཡོད་དོ་ཞེས་ནི་མི་སྨྲའོ།[^197] །འདི་ལྟར་འགྲོ་བ་གང་དང་ལྡན་པས་འགྲོ་བ་པོ་ཞེས་བྱ་བར་འགྱུར་བ་དེ་ཡོད་དོ་ཞེས་སྨྲའོ། །

[Block 283]
འདིར་བཤད་པ།

[Block 284 [VERSE]]
འགྲོ་བ་མེད་ན་འགྲོ་བ་པོ། །
ཡོད་པ་ཉིད་དུ་ག་ལ་འགྱུར། །

[Block 285]
གལ་ཏེ་རྟེན་ཅུང་ཟད་ཀྱང་མེད་པའི་འགྲོ་བ་ཞིག་རབ་ཏུ་གྲུབ་པར་གྱུར་ན་ནི་དེ་དང་འགྲོ་བ་པོའམ། འགྲོ་བ་པོ་མ་ཡིན་པ་ལྡན་པར་ཡང་འགྱུར་གྲང་ན། ཐ་དད་པར་གྱུར་པ་རྟེན་མེད་པའི་འགྲོ་བ་ནི་འགའ་ཡང་མེད་དེ། དེས་ན་ཐ་དད་པར་གྲུབ་པའི་འགྲོ་བ་མེད་པར་ཁྱོད་ཀྱིས༌[^198]འགྲོ་བ་ལྡན་པས་འགྲོ་བ་པོར་འགྱུར་བ་ཡོད་པ་ཉིད་དུ་ག་ལ་འགྱུར་འགྲོ་བ་པོ་མེད་ན་ཡང་སུ་ཡི་འགྲོ་བར་འགྱུར་ཏེ། དེ་བས་ན་འགྲོ་བ་མེད་དོ། །
--- END BLOCKS ---
