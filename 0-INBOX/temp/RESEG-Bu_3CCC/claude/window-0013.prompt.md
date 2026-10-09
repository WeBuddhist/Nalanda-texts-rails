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
[Block 456 [VERSE]]
མ་སྤངས་ལྟ་པོ་ཡོད་མིན་ཏེ། །
ལྟ་བ་སྤངས་པར་གྱུར་ཀྱང་ངོ་། །
ལྟ་པོ་མེད་ན་བལྟ་བྱ་དང་།

[Block 457]
[^300] །ལྟ་བ་དེ་དག༌[^301]ག་ལ་ཡོད། །འདི་ལ་ལྟ་བ་ཉིད་ན་ལྟ་བ་པོ་ཡིན་གྱི་མི་ལྟ་ན་མ་ཡིན་ནོ། །ཞེས་སྔར་བསྟན་པ་དེས་ན་ལྟ་བ་དང་ལྡན་པའི་ཕྱིར་ལྟ་བ་པོ་ཡིན་པས་ལྟ་བ་པོ་ལྟ་བར་བྱེད་དོ། །ཞེས་བྱ་བ་དེ་མི་འཐད་དོ། །

[Block 458]
ལྟ་བའི་བྱ་བ་གཉིས་ལ༌[^302]མེད་པའི་ཕྱིར་རོ། །

[Block 459]
དེ་ལྟར་རེ་ཞིག་ལྟ་བ་མ་སྤངས་ན་ལྟ་བ་པོ་མ་ཡིན་པས་ལྟ་བ་པོ་མེད་དོ། །

[Block 460]
ད་ནི་ལྟ་བ་པོ་མ་ཡིན་པ་ཡང་ལྟ་བར་མི་བྱེད་པ་ཉིད་དེ། ལྟ་བའི་བྱ་བ་དང་བྲལ་བའི་ཕྱིར་རོ་ཞེས་བསྟན་པ་དེ་བཞིན་དུ་ལྟ་བ་སྤངས་པར་གྱུར་ན་ཡང་ལྟ་བ་པོ་མེད་དོ། །

[Block 461]
དེ་ལ་ལྟ་བ་སྤངས་ཀྱང་རུང་མ་སྤངས༌[^303]ཀྱང་རུང་སྟེ་ལྟ་བ་པོ་མེད་ན་ཁྱོད་ཀྱི་བལྟ་བར༌[^304]བྱ་བ་དང་ལྟ་བ་ཡོད་པར་ག་ལ་འགྱུར། འདི་ལྟར་གང་གིས་ལྟ་བར་བྱེད་པས་བལྟ་བར༌[^305]བྱ་བ་ཡིན་ན་གང་གིས་ལྟ་བར་བྱེད་པས༌[^306]དེ་ནི་མེད་དོ། །

[Block 462]
དེ་མེད་ན་གང་གིས་ལྟ་བར་འགྱུར། མི་ལྟ་ན་བལྟ་བར༌[^307]བྱ་བར་ཇི་ལྟར་འགྱུར། འགའ་ཞིག་གིས་གང་གིས་ལྟ་བར་བྱེད་པ་དེ་ནི་དེའི་ལྟ་བ་ཡིན་ན་གང་གིས་ལྟ་བར་བྱེད་པ་དེ་ནི་མེད་དོ། །

[Block 463]
དེ་མེད་ན་གང་གིས༌[^308]ལྟ་བར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་ལྟ་བ་པོ་མེད་ན་བལྟ་བར༌[^309]བྱ་བ་དང་ལྟ་བ་མི་འཐད་པ་ཉིད་དོ། །

[Block 464]
དེའི་ཕྱིར་སྐྱེ་མཆེད་རྣམས་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 465]
སྨྲས་པ། སྐྱེ་མཆེད་རྣམས་ནི་ཡོད་པ་ཉིད་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། རྣམ་པར་ཤེས་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 466]
འདི་ལྟར་རྣམ་པར་ཤེས་པ་དངོས་པོ་རྣམས་དམིགས་པར་བྱེད་པ་ནི་ཡོད་དོ། །

[Block 467]
དེ་ཡོད་པའི་ཕྱིར་སྐྱེ་མཆེད་རྣམས་ཀྱང་ཡོད་དོ། །

[Block 468]
བཤད་པ།

[Block 469 [VERSE]]
བལྟ༌[^310]བྱ་ལྟ་བ་མེད་པའི་ཕྱིར། །
རྣམ་པར་ཤེས་ལ་སོགས་པ་བཞི། །
ཡོད་མིན་ཉེ་བར་ལེན་ལ་སོགས། །
ཇི་ལྟ་བུར་ན་ཡོད་པར་འགྱུར། །

[Block 470]
གང་གི་ཚེ་ལྟ་བ་པོ་མེད་ན་བལྟ་བར་བྱ་བ་དང་ལྟ་བ་མི་འཐད་དོ། །ཞེས་བཤད་པ་དེའི་ཚེ་གནས་མེད་པར་རྣམ་པར་ཤེས་པ་ཇི་ལྟར་ཡོད་པར་འགྱུར་ཏེ། འདི་ལྟར་བལྟ་བར༌[^311]བྱ་བ་ལས་གཞན་ཅི་ཞིག་རྣམ་པར་ཤེས་པར་འགྱུར། ལྟ་བ་མེད་ན་རྣམ་པར་ཤེས་པ་ལྟོས་པ་མེད་པར་ཇི་ལྟར་ཡོད་པར་འགྱུར། ཅི་སྟེ་འགྱུར་ན་ནི་ལོང་བ་ལ་ཡོད་པར་འགྱུར་བ་ཞིག་ན་མི་འགྱུར་རོ། །

[Block 471]
དེ་ལྟ་བས་ན་བལྟ་བར༌[^312]བྱ་བ་དང་ལྟ་བ་མེད་ན་གནས་མེད་པར་རྣམ་པར་ཤེས་པ་ཡོད་པར་མི་འཐད་དོ། །

[Block 472]
རྣམ་པར་ཤེས་པ་མེད་ན་རེག་པ་ག་ལ་ཡོད།

[Block 473]
རེག་པ་མེད་ན་ཚོར་བ་ག་ལ་ཡོད། །ཚོར་བ་མེད་ན་སྲེད་པ་ག་ལ་ཡོད། །

[Block 474]
དེ་བཞིན་དུ་ཉེ་བར་ལེན་པ་དང་སྲིད་པ་དང་། སྐྱེ་བ་དང་རྒ་ཤི་དག་ཀྱང་ཡོད་པར་ག་ལ་འགྱུར་ཏེ། དེ་བས་ན་སྐྱེ་མཆེད་རྣམས་ནི་ཡོད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 475]
དེ་སྐད་དུ། བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་། དེ་ལ་འཕགས་པ་ཉན་ཐོས་ནི་མིག་གི་རྣམ་པར་ཤེས་པར་བྱ་བའི་གཟུགས་གང་དག་འདས་པ་དང་། མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བ་འདི་དག་ལ་རྟག་པ་ཉིད་དམ་བརྟན་པ་ཉིད་དམ། དེ་བཞིན་ཉིད་དམ་གཞན་མ་ཡིན་པ་དེ་བཞིན་ཉིད་དམ། མ་ནོར་བ་དེ་བཞིན་ཉིད་ནི་འགའ་ཡང་མེད་ཀྱི་སྒྱུ་མ་དེ་ནི་ཡོད་དོ། །

[Block 476]
སྒྱུ་མར་བྱས་པ་དེ་ནི་ཡོད་དོ། །

[Block 477]
སེམས་རྨོངས་པར་བྱེད་པ་དེ་ནི་ཡོད་དེ། དེ་ནི་གྱི་ན་ཞིག་ཡོད་དོ། །

[Block 478]
སྙམ་དུ་དེ་ལྟར་སོ་སོར་རྟོག་པར་བྱེད་དོ། །ཞེས་གསུངས་སོ། །

[Block 479]
སྨྲས་པ། ཁྱོད་ཀྱིས་རེ་ཞིག༌[^313]ལྟ་བ་ནི་བཀག་ན་ཉན་པ་ལ་སོགས་པ་ནི་མ་བཀག་པས༌[^314]དེས་ན་ཉན་པ་ལ་སོགས་པ་ཡོད་པའི་ཕྱིར་དངོས་པོ་རྣམས་ཡོད་དོ། །

[Block 480]
བཤད་པ།

[Block 481 [VERSE]]
ལྟ་བས་ཉན་དང་སྣོམ་པ་དང་། །
མྱོང་བར་བྱེད་དང་རེག་བྱེད་ཡིད། །
ཉན་པ་པོ་དང་མཉན་ལ་སོགས། །
རྣམ་པར་བཤད་པར་ཤེས་པར་བྱ། །

[Block 482]
ཉན་པ་ལ་སོགས་པ་དེ་དག་ནི་རྣམ་པར་བཤད་པ༌[^315]ཉིད་དུ་ཤེས་པར་བྱའོ། །གང་གིས་རྣམ་པར་བཤད་ཅེ་ན། ལྟ་བ་ཉིད་ཀྱིས་ཏེ། ཇི་ལྟར་ལྟ་བ་རྣམ་པ་ཐམས་ཅད་དུ་བརྟགས་ན་མི་འཐད་པ་དེ་བཞིན་དུ་ཉན་པ་ལ་སོགས་པ་དག་ཀྱང་ཤེས་པར་བྱའོ། །

[Block 483]
ཇི་ལྟར་ལྟ་བ་པོ་མི་འཐད་པ་དེ་བཞིན་དུ་ཉན་པ་པོ་ལ་སོགས་པ་དག་ཀྱང་ཤེས་པར་བྱའོ། །

[Block 484]
ཇི་ལྟར་བལྟ་བར༌[^316]བྱ་བ་བསལ་བ་དེ་བཞིན་དུ་མཉན་པར་བྱ་བ་ལ་སོགས་པ་དག་ཀྱང་ཤེས་པར་བྱའོ། །

[Block 485]
དེ་ལྟ་བས་ན་སྐྱེ་མཆེད་རྣམས་ཀྱང་སྟོང་པ་ཉིད་དུ་གྲུབ་པར་ཤེས་པར་བྱའོ། །

[Block 486]
སྐྱེ་མཆེད་བརྟག་པ་ཞེས་བྱ་བ་སྟེ་རབ་ཏུ་བྱེད་པ་གསུམ་པའོ།། །།

[Block 487 [HEADING]]
## ཕུང་པོ་བརྟག་པ། ^4-0

[Block 488]
འདིར་སྨྲས་པ། འདི་ལ་གཟུགས་ལ་སོགས་པ་ཕུང་པོ་ལྔ་པོ་དག་བསྟན་ཏོ། །

[Block 489]
དེ་དག་སྡུག་བསྔལ་ལོ་ཞེས་གསུངས་ཏེ། སྡུག་བསྔལ་འཕགས་པའི་བདེན་པར་གསུངས་སོ། །

[Block 490]
འཕགས་པའི་བདེན་པ་གང་ཡིན་པ་དེ་ནི་མེད་པར་ཇི་ལྟར་འགྱུར་ཏེ། དེ་བས་ན་ཕུང་པོ་རྣམས་ནི་ཡོད་དོ། །

[Block 491]
བཤད་པ།

[Block 492 [VERSE]]
གཟུགས་ཀྱི་རྒྱུ་ནི་མ་གཏོགས་པར། །
གཟུགས་ནི་དམིགས་པར་མི་འགྱུར་རོ། །

[Block 493]
འདི་ལ༌[^317]འབྱུང་བ་ཆེན་པོ་བཞི་པོ་དག་ནི་གཟུགས་ཀྱི་རྒྱུར་བསྟན། གཟུགས་ནི་དེ་དག་གི་འབྲས་བུར་བསྟན་ན། འབྱུང་བ་ཆེན་པོ་བཞི་པོ་དག་མ་གཏོགས་པར་འབྱུང་བ་ཆེན་པོ་བཞི་པོ་དེ་དག་ལས་དོན་གཞན་དུ་གྱུར་པ་གཟུགས་ཞེས་བྱ་བར་འབྲས་བུ་ནི་ཅི་ཡང་མེད་དེ། དེ་ལྟ་བས་ན་གཟུགས་ནི་མི་འཐད་དོ། །

[Block 494]
སྨྲས་པ། རེ་ཞིག་འབྱུང་བ་དག་ནི་ཡོད་དེ། དེ་ལ་རྒྱུ་ཡོད་པའི་ཕྱིར་འབྲས་བུ་ཡང་ཡོད་པས༌[^318]གཟུགས་ཀྱང་རབ་ཏུ་གྲུབ་པ་ཉིད་དོ། །

[Block 495]
བཤད་པ།
--- END BLOCKS ---
