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

[Block 286]
སྨྲས་པ། སྤྲོས་པ་འདིས་ཅི་བྱ། གང་ལ་ལྟོས་ནས་འགྲོའོ། །ཞེས་བྱ་བ་དེ་འགྲོ་བ་ཡིན་ནོ། །

[Block 287]
འདིར་བཤད་པ། གལ་ཏེ་འགྲོ་པོ་ཞེས་བྱ་བ་དེ་ཉིད་རབ་ཏུ་གྲུབ་པར་གྱུར་ན་ནི་དེས་ན་འགྲོ་བ་ཡང་རབ་ཏུ་འགྲུབ་པར་འགྱུར་གྲང་ན། དེ་རབ་ཏུ་མི་འགྲུབ་པས་འགྲོ་བ་རབ་ཏུ་འགྲུབ་པར་ག་ལ་འགྱུར། ཇི་ལྟར་ཞེ་ན། འདི་ལ་འགྲོ་བ་ཞིག་ཡོད་ན་འགྲོ་བ་པོའམ། འགྲོ་བ་པོ་མ་ཡིན་པ་འགྲོ་གྲང་ན། འདིར་བཤད་པ།

[Block 288 [VERSE]]
རེ་ཞིག་འགྲོ་པོ་མི་འགྲོ་སྟེ། །
འགྲོ་བ་པོ་མིན་འགྲོ་པོ་མིན། །
འགྲོ་པོ་འགྲོ་པོ་མིན་ལས་གཞན། །
གསུམ་པ་གང་ཞིག་འགྲོ་བར་འགྱུར། །

[Block 289]
དེ་བས་ན་འགྲོའོ་ཞེས་བྱ་བ་ཉིད་མི་འགྲུབ་པོ། །ཅིའི་ཕྱིར་ཞེ་ན། མི་འཐད་པའི་ཕྱིར་རོ། །ཇི་ལྟར་ཞེ་ན།

[Block 290 [VERSE]]
རེ་ཞིག་འགྲོ་པོ་འགྲོའོ་ཞེས། །
ཇི་ལྟར་འཐད་པ་ཉིད་དུ་འགྱུར། །
འགྲོ་བ་མེད་ན་འགྲོ་བ་པོ། །
ནམ་ཡང་འཐད་པར་མི་འགྱུར་རོ། །

[Block 291]
འདི་ལ་འགྲོ་བ་པོ་འགྲོའོ། །ཞེས་བྱ་བ་ལ། འགྲོ་བའི་བྱ་བ་གཅིག་པུ་ཞིག་ཡོད་པ་དེ་ནི་འགྲོ༌[^199]ཞེས་བྱ་བ་དེ་ལ་ཉེ་བར་སྦྱར་བས་དེས་ན་འགྲོ་བ་པོ་ནི་འགྲོ་བ་དང་བྲལ་ཏེ། གུབ་ཏ་དང་ཙཻ་ཏྲ་བཞིན་དུ་མིང་ཙམ་དུ་གྱུར་པར་ཐལ་བར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དོ། །

[Block 292]
དེའི་ཚེ༌[^200]གང་གི་ཚེ་འགྲོ་བ་མེད་ན་འགྲོ་བ་པོ་ནམ་ཡང་འཐད་པར་མི་འགྱུར་བ་དེའི་ཚེ་འགྲོ་བ་པོ་འགྲོའོ་ཞེས་བྱ་བ་དེ་ཇི་ལྟར་འཐད་པ་ཉིད་དུ་འགྱུར། ཡང་གཞན་ཡང་བཤད་པ།

[Block 293 [VERSE]]
གང་གི་ཕྱོགས་ལ་འགྲོ་བ་པོ། །
འགྲོ་བ་དེ་ལ་འགྲོ་མེད་པའི། །
འགྲོ་པོ་ཡིན་པར་ཐལ་འགྱུར་ཏེ། །
འགྲོ་པོ་འགྲོ་བར་འདོད་ཕྱིར་རོ། །

[Block 294]
གང་གི་ཕྱོགས་ལ་སྐྱོན་དེར་གྱུར་ན་མི་རུང་ངོ་སྙམ་པས་འགྲོ་བ་པོ་འགྲོ་བ་དང་ལྡན་པས་འགྲོ་པོ༌[^201]སྙམ་པ་དེ་ལ་ཡང་འགྲོ་བ་པོ་ཞེས་བྱ་བ་དེ་ལ་འགྲོ་བའི་བྱ་བ་ཉེ་བར་སྦྱར་བ་བྱས་པས་འགྲོ་བ་མེད་པའི་འགྲོ་བ་པོ་ཡིན་པར་ཐལ་བར་འགྱུར་བ་སྟེ། འགྲོ་བ་པོ་འགྲོ་བར་འདོད་པའི་ཕྱིར་འགྲོ་བ་མེད་པར་འགྲོའོ་ཞེས་བྱ་བ་དེར་ཐལ་བར་འགྱུར་རོ། །ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 295]
དེ་ནི་མི་འཐད་དེ། འགྲོའོ་ཞེས་བྱ་བ་དེ། འགྲོ་བ་མེད་པར་ཇི་ལྟར་འགྱུར་རོ།[^202] །

[Block 296]
ཅི་སྟེ་སྐྱོན་དེར་གྱུར་ན་མི་རུང་ངོ་སྙམ་པས་འགྲོ་བ་པོ་ཞེས་བྱ་བ་དང་། འགྲོ་བ་པོ་ཞེས་བྱ་བ༌[^203]དེ་གཉི་ག་ཡང་འགྲོ་བ་དང་ལྡན་ནོ་ཞེ་ན། དེ་ལ་ཡང་སྐྱོན་འདི་ཡོད་དེ། བཤད་པ།

[Block 297 [VERSE]]
གལ་ཏེ་འགྲོ་པོ་འགྲོ་འགྱུར༌[^204]ན། །
འགྲོ་བ་གཉིས་སུ་ཐལ་འགྱུར་ཏེ། །
གང་གིས་འགྲོ་པོར་མངོན་པ་དང་། །
འགྲོ་པོར་གྱུར་ནས་གང་འགྲོ་བའོ། །

[Block 298]
འགྲོ་བ་པོ་འགྲོ་བ་དང་ལྡན་པ་ལ་འགྲོ་བར་བརྟགས༌[^205]ན་འགྲོ་བ་གཉིས་སུ་ཐལ་བར་འགྱུར་ཏེ། འགྲོ་བ་གང་དག་ལྡན་པས་འགྲོ་བ་པོ་ཞེས་བྱ་བར་མངོན་པ་དང་། དེ་འགྲོ་བ་གང་ལ་ལྟོས་ནས་འགྲོའོ་ཞེས་བྱ་བར་འགྱུར་བའོ། །

[Block 299]
འགྲོ་བ་གཉིས་སུ་ནི་མི་འཐད༌[^206]དེ། འགྲོ་བ་གཉིས་སུ་ཐལ་བར་གྱུར་ན་སྔ་མ་བཞིན་དུ་འགྲོ་བ་པོ་ཡང་གཉིས་སུ་ཐལ་བར་འགྱུར་བས་དེ་ཡང་མི་འདོད་དེ་དེ་ལྟ་བས་འགྲོ་བ་པོ་འགྲོའོ་ཞེས་བྱ་བ་དེ་མི་འཐད་དོ། །

[Block 300]
ད་ནི་འགྲོ་བ་པོ་མ་ཡིན་པ་ཡང་མི་འགྲོ་སྟེ། གང་གི་ཚེ་འགྲོ་བ་པོ་འགྲོ་པོ༌[^207]ཞེས་བྱ་བ་དེ་མི་འཐད་པ་དེ༌[^208]ཚེ་འགྲོ་བ་པོ་མ་ཡིན་པ་འགྲོ་བ་དང་བྲལ་བའང་འགྲོ་བའོ། །ཞེས་བྱ་བ་དེ་ཇི་ལྟར་འཐད་པ་ཉིད་དུ་འགྱུར། དེ་ལྟ་བས་ན་འགྲོ་བ་པོ་མ་ཡིན་པ་ཡང་མི་འགྲོའོ། །

[Block 301]
དེ་ལ་འདི་སྙམ་དུ་འགྲོ་བ་པོ་ཡིན་པ་དང་འགྲོ་བ་པོ་མ་ཡིན་པ་འགྲོ་བར་སེམས་ན། བཤད་པ།

[Block 302 [VERSE]]
འགྲོ་པོ་འགྲོ་པོ་མིན་ལས་གཞན། །
གསུམ་པོ༌[^209]གང་ཞིག་འགྲོ་བར་འགྱུར། །

[Block 303]
འགྲོ་བ་པོ་དང་འགྲོ་བ་པོ་མ་ཡིན་པ་ལས་གཞན་པ་གསུམ་པ། འགྲོ་བ་པོ་ཡིན་པ་དང་འགྲོ་བ་པོ་མ་ཡིན་པ་གང་འགྲོའོ་ཞེས་བྱ་བར་འཐད་པ་ཞིག་གང་ཞིག་ཡིན། དེ་ལྟ༌[^210]བས་ན་མེད་པའི༌[^211]ཁོ་ནའི་ཕྱིར་འགྲོ་བ་པོ་མ༌[^212]ཡིན་པ་དང་འགྲོ་བ་པོ་མ་ཡིན་པ་ཡང་མི་འགྲོའོ། །

[Block 304]
དེ་ལྟར་གང་གི་ཕྱིར་འགྲོ་བ་པོ་དང་། འགྲོ་བ་པོ་མ་ཡིན་པ་དང་། འགྲོ་བ་པོ་ཡིན་པ་དང་། འགྲོ་བ་པོ་མ་ཡིན་པ་འགྲོའོ། །ཞེས་བྱ་བ་དེ་མི་འཐད་པ་དེའི་ཕྱིར། འགྲོའོ་ཞེས་བྱ་བ་དེ་རབ་ཏུ་མི་འགྲུབ་བོ། །

[Block 305]
འགྲོའོ་ཞེས་བྱ་བ་དེ་མེད་ན་འགྲོ་བ་རབ་ཏུ་འགྲུབ་པར་ག་ལ་འགྱུར།

[Block 306]
འདིར་སྨྲས་པ། འགྲོ་བ་པོ་དང་། འགྲོ་བ་པོ༌[^213]ཡིན་པ་དང་།[^214] འགྲོ་བ་པོ་མ་ཡིན་པ་འགྲོའོ། །ཞེས་བྱ་བ་མི་འཐད་དུ་ཟིན་ཀྱང་། གུབ་ཏ་འགྲོའོ། །

[Block 307]
ཙཻ་ཏྲ་འགྲོའོ་ཞེས་བྱ་བ་དེ་ལ་འགྲོའོ་ཞེས་བྱ་བ་འཐད་དོ། །

[Block 308]
བཤད་པ། དེས་ནི་ཅི་ཡང་སྨྲས་པ་མ་ཡིན་ཏེ། གུབ་ཏ་ལ་བརྟེན་ན་ཅི་གུབ་ཏ་འགྲོ་བ་པོར་གྱུར་ནས་འགྲོའམ། འོན་ཏེ་འགྲོ་བ་པོ་མ་ཡིན་འགྲོའམ། འོན་ཏེ་འགྲོ་བ་པོ་ཡིན་པ་དང་། འགྲོ་བ་པོ་མ་ཡིན་པ་ཞིག་འགྲོ་ཞེས་བྱ་བ་འདི་གསལ་བ༌[^215]མ་བྱས་སམ། དེ་ལྟ་བས་ན་འདི་ནི་གྱི་ནའོ། །

[Block 309]
འདིར་སྨྲས་པ། འགྲོ་བ་ནི་ཡོད་པ་ཁོ་ནའོ། །ཅིའི་ཕྱིར་ཞེ་ན། འགྲོ་བའི་བྱ་བ་རྩོམ་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 310]
འདི་ལ་སོང་བ་དང་མ་སོང་བ་དང་བགོམ་པ་ལ་འགྲོ་བ༌[^216]ཡོད་དོ། །ཞེས་བྱ་བ་དེ་བརྗོད་པར་མི་ནུས་སུ་ཟིན་ཀྱང་། གང་གི་ཚེ་སྡོད་པ་ལས་འགྲོ་བ་དེའི་ཚེ་ན་སྡོད་པའི་བྱས་པ༌[^217]འདས་མ་ཐག་ཏུ་འགྲོ་བའི་བྱ་བ་འཇུག་པར་འགྱུར་བས་དེ་ལྟ་བས་ན་བྱ་བ་རྩོམ་པ་ཡོད་པས་འགྲོ་བ་ཡོད་པ་ཁོ་ནའོ། །

[Block 311]
བཤད་པ། ཅི་ཁྱོད་མིང་གཞན་དུ་བསྒྱུར་བས་སེམས་རྨོངས་ནས་རང་གི་བུ་ངོ་མི་ཤེས་སམ། ཁྱོད་དོན་དེ་ཉིད་ལ་བློ་ཕྱི་མས་བརྗོད་པ་གཞན་གྱིས་བརྗོད་ཀོ་འགྲོ་བའི་བྱ་བ་རྩོམ་པ་ཡོད་པར་ཡོངས་སུ་བརྟག་པ་གང་ཡིན་པ་དེ་ཡང་སོང་བའམ་མ་སོང་བའམ། བགོམ་པ་ལ་ཡོད་གྲང་ན། དེ་ལ་གཏན་ཚིགས་སྔར་བསྟན་པ་དག་ཉིད་ཀྱིས་བཤད་པ། སོང་ལ་འགྲོ་བའི་རྩོམ་མེད་དེ། །ཅིའི་ཕྱིར་ཞེ་ན། འགྲོ་བའི་བྱ་བ་འདས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 312]
མ་སོང་བ་ལའང་འགྲོ་རྩོམ་མེད། །ཅིའི་ཕྱིར་ཞེ་ན། འགྲོ་བའི་བྱ་བ༌[^218]མ་བརྩམས་པའི་ཕྱིར་རོ། །

[Block 313]
བགོམ་ལ་རྩོམ་པ༌[^219]ཡོད་མིན་ན། །ཅིའི་ཕྱིར་ཞེ་ན། བགོམ་པ་མེད་པའི་ཕྱིར་དང་། འགྲོ་བ་གཉིས་སུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དང་། འགྲོ་བ་པོ་གཉིས་སུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 314]
གང་དུ་འགྲོ་བ་རྩོམ་པར་བྱེད། །ཅེས་བྱ་བའི་ལན་དེ་ད་སྨྲོས་ཤིག །དེ་ལྟ་བས་ན་འགྲོ་བའི་རྩོམ་པ་མེད་དོ། །

[Block 315]
རྩོམ་པ་མེད་ན་འགྲོ་བ་ཡོད་པར་ག་ལ་འགྱུར།

[Block 316]
འདིར་སྨྲས་པ། འགྲོ་བ་ནི་ཡོད་པ་ཁོ་ནའོ། །ཅིའི་ཕྱིར་ཞེ་ན། བགོམ་པ་དང་སོང་བ་དང་མ་སོང་བ་ཡོད་པའི་ཕྱིར་ཏེ། གང་གི་ཕྱིར་འགྲོ་བ་དང་ལྡན་པའི་ཕྱིར་བགོམ་པ་ཞེས་བྱ་བ་ཡིན་ལ། འགྲོ་བ་མཐར་ཕྱིན་པ་ནི་སོང་བ་ཞེས་བྱ་བ་ཡིན། འགྲོ་བའི་བྱ་བ་མ་སོང་བ་ལ་ལྟོས་ནས་མ་སོང་བ་ཞེས་བྱ་བ་ཡིན་པས་ན་དེ་ལྟ་བས་ན་བགོམ་པ་དང་སོང་བ་དང་། མ་སོང་བ་ཡོད་པའི་ཕྱིར་འགྲོ་བ་ཡོད་དོ། །

[Block 317]
བཤད་པ། ཅི་ཁྱེད་ནམ་མཁའ་འདི་ལ་ལྡང་བར་བསྐྱོད་དམ། གང་གི་ཚེ།

[Block 318 [VERSE]]
འགྲོ་བ་རྩོམ་པའི་སྔ་རོལ་ན། །
གང་དུ་འགྲོ་བ་རྩོམ་འགྱུར་བ། །
བགོམ་པ་མེད་ཅིང་སོང་བ་མེད། །

[Block 319]
འདི་ལ་འགྲོ་བ་རྩོམ་པའི་སྔ་རོལ་སྡོད་པར་གྱུར་པ་ན་གང་དུ་འགྲོ་བ་རྩོམ་པར་འགྱུར་བའི་བགོམ་པ་ཡང་མེད་ཅིང་། སོང་བ་ཡང་མེད་དོ། །

[Block 320]
འགྲོ་བ་རྩོམ་པ་མེད་ན་བགོམ་པ་འགྲོ་བ་དང་ལྡན་པར་ག་ལ་འགྱུར། འགྲོ་བ་དང་ལྡན་པ་མེད་ན་འགྲོ་བ་མཐར་ཕྱིན་པ་ཡོད་པར་ཡང་ག་ལ་འགྱུར། འདིར་སྨྲས་པ། མ་སོང་བ་ནི་ཡོད་དེ། དེར་འགྲོ་བ་རྩོམ་པར་འགྱུར་རོ། །
--- END BLOCKS ---
