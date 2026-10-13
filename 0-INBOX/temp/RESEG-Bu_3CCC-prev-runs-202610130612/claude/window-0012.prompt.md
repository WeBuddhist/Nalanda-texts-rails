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
[Block 421]
ཅི་སྟེ་གཞན་པ་ཉིད་མ་ཡིན་དུ་ཟིན་ཀྱང་བུད་ཤིང་ནི་བསྲེག་པར༌[^280]བྱ་བའོ། །

[Block 422]
མེ་ནི་སྲེག་པར་བྱེད་པའོ་ཞེས་རྟོག་ན། ཁོ་བོས་ཀྱང་བུད་ཤིང་ནི་སྲེག་པར་བྱེད་པའོ། །

[Block 423]
མེ་ནི་བསྲེག་པར་བྱ་བའོ། །ཞེས་སྨྲ་ལ་རག་གོ། །

[Block 424]
ཡང་ན་ཁྱད་པར་གྱི་གཏན་ཚིགས་བསྟན་པ་བརྗོད་དགོས་སོ། །

[Block 425]
སློབ་དཔོན་འཕགས་པ་ལྷས་ཀྱང་།

[Block 426 [VERSE]]
མེས་ནི་ཚ་བ་ཉིད་བསྲེག་སྟེ། །
ཚ་བ་ལ་ཡིན་ཇི་ལྟར་བསྲེག །
དེས་ན་བུད་ཤིང་ཞེས་བྱ་མེད། །
དེ་མ་གཏོགས་པར་མེ་ཡང་མེད། །

[Block 427]
ཅེས་གསུངས་སོ། །

[Block 428]
དེ་ལྟ་བས་ན་མེའི་དཔེས་ནུས་པ་མ་ཡིན་ནོ། །

[Block 429]
འདི་ལ་ཁ་ཅིག་མེ་ནི་རང་གཞན་གྱི་བདག་ཉིད་དག་སྣང་བར་བྱེད་དོ་སྙམ་དུ་སེམས་པ༌[^281]དེས་ཀྱང་ནུས་པ་མ་ཡིན་ཏེ། མེ་ནི་ཇི་ལྟར་རང་དང་གཞན་གྱི་བདག་ཉིད་དག་སྣང་བར་བྱེད་པ་དེ་བཞིན་དུ་རང་གཞན་གྱི་བདག་ཉིད་དག་སྲེག་པར་ཡང༌[^282]བྱེད་པའི་རིགས་སོ། །

[Block 430]
འོན་ཀྱང་གཞན་དག་སྲེག་པར་བྱེད་པ་ཉིད་ཡིན་གྱི་རང་གི་བདག་ཉིད་སྲེག་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟར་ན་ཡང་མེས་ཇི་ལྟར་གཞན་དག་སྲེག་པར་བྱེད་ཀྱི། རང་གི་བདག་ཉིད་སྲེག་པར་མི་བྱེད་པ་དེ་བཞིན་དུ་ལྟ་བ་ཡང་གཞན་དག་ལ་ལྟ་བར་བྱེད་ཀྱི། རང་གི་བདག་ཉིད་ལ་ལྟ་བར་མི་བྱེད་དོ་ཞེས་བྱ་བ་དེ་ཇི་ལྟར༌[^283]རུང་སྟེ། མེ་ཇི་ལྟར་རང་དང་གཞན་གྱི་བདག་ཉིད་དག་སྣང་བར་བྱེད་པ་དེ་བཞིན་དུ་ལྟ་བ་ཡང་ནི་གལ་ཏེ་ལྟ་བ་ཡིན་ན། རང་དང་གཞན་གྱི་བདག་ཉིད་དག་ལ་ལྟ་བར་བྱེད་དོ། །ཞེས་བྱ་བ་དེ་ལྟ་བུར་ཡང་ཅིའི་ཕྱིར་མི་འགྱུར། བདག་ཉིད་བདག་ཉིད་ལ་ལྟའོ་ཞེས་ཀྱང་ཟེར་ལ། དེ་བཞིན་དུ་འཇིག་རྟེན་ན་སྨྲ་བ་པོ་དག་བདག་ཉིད་ཀྱིས་བདག་ཉིད་འཛིན་ཏོ་ཞེས་ཀྱང་ཟེར་བས། དེའི་ཕྱིར་རང་གི་བདག་ཉིད་ལ་འཇུག་པའི་ཚིག་གིས་ན། ལྟ་བ་རབ་ཏུ་བསྒྲུབ་པའི་ཕྱིར་མེའི་དཔེས་ནུས་པ་མ་ཡིན་ནོ། །

[Block 431]
ཡང་གཞན་ཡང་།

[Block 432 [VERSE]]
སོང་དང་མ་སོང་བགོམ་པ་ཡིས། །
དེ་ནི་ལྟར་བཅས་ལན་བཏབ་པོ། །

[Block 433]
ལྟར་བཅས་ཞེས་བྱ་བ་ནི་ལྟ་བ་དང་བཅས་པའོ། །གང་ཞེ་ན། མེའི་དཔེ་སྟེ།[^284] དཔེ་དང་ལྟ་བ་དེ་གཉི་ག་མཚུངས་པར་ལན་བཏབ་ཟིན་ཏོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །གང་གིས་ལན་བཏབ་ཅེ་ན། སོང་བ་དང་། མ་སོང་བ་དང་། བགོམ་པ་དག་གིས་ཏེ། ཇི་ལྟར་སོང་བ་དང་། མ་སོང་བ་དང་། བགོམ་པ་བརྟག་པར་སོང་བ་ལ་ཡང་འགྲོ་བ་མེད། མ་སོང་བ་ལ་ཡང་མེད། བགོམ་པ་ལ་ཡང་འགྲོ་བ་མེད་དོ། །ཞེས་བཤད་པ་དེ་བཞིན་དུ་མེས་ཀྱང་བསྲེགས་པ་ཡང་སྲེག་པར་མི་བྱེད། མ་བསྲེགས་པ་ཡང་སྲེག་པར་མི་བྱེད།[^285] ལྟ་བ་ཡང་བལྟས་པ་ལ་ཡང་ལྟ་བར་མི་བྱེད། མ་བལྟས་པ་ལ་ཡང་ལྟ་བར་མི་བྱེད། ལྟ་བ་ལ་ཡང་ལྟ་བར་མི་བྱེད་དོ། །

[Block 434]
དེ་ལྟར་མེ་ཡང་སྲེག་པར་མི་བྱེད་ལ། ལྟ་བ་ཡང་ལྟ་བར་མི་བྱེད་ན་ཅི་ཞིག་གང་གི་དཔེར་འགྱུར། དེའི་ཕྱིར་ཡང་ལྟ་བ་རབ་ཏུ་བསྒྲུབ་པའི་ཕྱིར་མེའི་དཔེས་ནུས་པ་མ་ཡིན་ནོ། །

[Block 435]
ཡང་གཞན་ཡང་།

[Block 436 [VERSE]]
གང་ཚེ་ཅུང་ཟད་མི་ལྟ་བ། །
ལྟ་བར་བྱེད་པ་མ་ཡིན་ནོ། །
ལྟ་བས་ལྟ་བར་བྱེད་ཅེས་བྱར།

[Block 437]
[^286] ། དེ་ནི་ཇི་ལྟར་རིགས་པར་འགྱུར། །འདི་ལྟར་ཁྱོད་ཀྱིས་གཟུགས་ལ་ལྟ་བར་བྱེད་པས་ལྟ་བའོ་ཞེས་སྨྲས་པ་ནི་བྱེད་པ་པོ་ལ་བྱ་བའི་རྐྱེན་བརྗོད་ནས་ལྟ་བར་བྱེད་པས་ལྟ་བ་ཡིན་ནོ། །

[Block 438]
དེའི་ཕྱིར་ལྟ་བ་ཉིད་ན་ལྟ་བ་ཡིན་གྱི་མི་ལྟ་བ་ནི་མ༌[^287]ཡིན་ནོ། །

[Block 439]
དེའི་ཕྱིར་གང་གི་ཚེ་ན་ལྟ་བ་ཉིད་ན་ལྟ་བ་ཡིན་གྱི་མི་ལྟ་བ༌[^288]ན་མ་ཡིན་པ་དེའི་ཚེ་ལྟ་བར་བྱེད་པས་ལྟ་བའོ་ཞེས་བྱ་བ་དེ་སྨྲ་བ་ཇི་ལྟར་རིགས་པར༌[^289]འགྱུར་ཏེ། འདི་ལ་གང་གིས་ལྟ་བར་བྱེད་དོ། །ཞེས་བྱ་བ་དེ་རིགས་པར་འགྱུར་བ་ལྟ་བའི་བྱ་བ་གཉིས་པ་དེ་ག་ལ་ཡོད། ཅི་སྟེ་འདི་ལ་ལྟ་བའི་བྱ་བ་གཉིས་པ་མེད་བཞིན་དུ་ཡང་རབ་ཏུ་རྟོག་ན། དེ་ལྟ་བས༌[^290]ན་ཡང་ལྟ་བ་གཉིས་སུ་ཐལ་བ་དང་། ལྟ་བ་པོ་ཡང་གཉིས་སུ་ཐལ་བར་འགྱུར་བས་དེ་ནི་མི་འདོད་དོ། །

[Block 440]
དེ་ལྟ་བས་ན་གཟུགས་ལ་ལྟ་བར་བྱེད་པས་ལྟ་བའོ། །ཞེས་བྱ་བ་དེ་མི་འཐད་དོ། །

[Block 441]
ཅི་སྟེ་ཐལ་བའི་བྱ་བ་གཉིས་སུ་ཐལ་བར་འགྱུར་བའི་སྐྱོན་དེར་གྱུར་ན་མི་རུང་ངོ་། །སྙམ་ནས་ལྟ་བ་ཉིད་ལྟ་བའི་བྱ་བ་དང་ལྡན་པའི་ཕྱིར་ལྟ་བར་བྱེད་པས་ལྟ་བའོ་ཞེ་ན། དེ་ལ་བཤད་པ།

[Block 442 [VERSE]]
ལྟ་བ་ལྟ་ཉིད་མ་ཡིན་ཏེ། །
ལྟ་བ་ལྟ་བར་བྱེད་པ་ཉིད་དོ། །

[Block 443]
ཞེས་དེ་ལྟར་རྟོག་ན་དེ་ཡང་མི་རིགས་པ་མ་ཡིན་ཏེ་ལྟ་བར་བྱེད་དོ། །ཞེས་བྱ་བ་དེ་ལ་ལྟ་བའི་བྱ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 444]
དེ་དེ་ལ་འདི་སྙམ་དུ་སྐྱོན་དེར་གྱུར་ན་མི་རུང་བས་ལྟ་བར་བྱེད་དོ། །ཞེས་བྱ་བ་དེ་ཉིད་ལྟ་བའི་བྱ་བ་དང༌[^291]ལྡན་པར་སེམས་ན། དེ་ལྟ༌[^292]བཤད་པ། ལྟ་བ་མིན་པ་མི་ལྟ་ཉིད། །དེ་ལྟ་ན་ཡང་ལྟ་བའི་བྱ་བ་དང་བྲལ་བའི་ལྟ་བ་ནི་ལྟ་བ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 445]
དེ་ལ་ལྟ་བ་མ་ཡིན་པ་ཇི་ལྟར༌[^293]ལྟ་བར་བྱེད་དོ། །ཞེས་བྱར་ནི་མི་རུང་སྟེ། འདི་ལྟར་ལྟ་བ་མ་ཡིན་པ་ཇི་ལྟར་ལྟ་བར་འགྱུར། ཅི་སྟེ་ལྟ་ན་ནི་སོར་མོའི་རྩེ་མོ་ཡང་ལྟ་བར་འགྱུར་བ་ཞིག་ན་མི་ལྟ་སྟེ། དེ་ལྟ་བས་ན་ལྟ་བ་མ་ཡིན་པ་ལྟ་བར་བྱེད་དོ་ཞེས་བྱ་བ་དེ་ཡང་མི་རུང་ངོ་། །

[Block 446]
སྨྲས་པ། བྱ་བའི་རྐྱེན་འདི་ནི་བྱེད་པ་ལ་བརྗོད་པ་ཡིན་གྱི་བྱེད་པ་པོ་ལ་མ་ཡིན་པས། འདིས་ལྟ་བར་བྱེད་པས་ལྟ་བ་སྟེ། གང་ཞིག་ལྟ་བར་བྱེད་ཅེ་ན། ལྟ་བ་པོའོ། །

[Block 447]
བཤད་པ།

[Block 448 [VERSE]]
ལྟ་བ་ཉིད་ཀྱིས་ལྟ་བ་པོའང་། །
རྣམ་པར་བཤད་པར་ཤེས་པར་བྱ། །

[Block 449]
འདི་ལ། ལྟ་བ་རང་གི་བདག་ཉིད་ནི།[^294] །

[Block 450 [VERSE]]
དེ་ནི་དེ་ལ་མི་ལྟ་ཉིད། །
གང་ཞིག་བདག་ལ་མི་ལྟ་བར། །

[Block 451]
དེ་གཞན་དག་ལ་ཇི་ལྟར་ལྟ།[^295] །ཞེས་བྱ་བ་ལ་སོགས་པ་དག་གིས་ལྟ་བས་ལྟ་བར་བྱེད་དོ་ཞེས་བྱ་བ་དེ་བསལ་ཟིན་ཏེ། ལྟ་བས༌[^296]བསལ་བ་དེ་ཉིད་ཀྱིས་ལྟ་བ་པོ་ཡང་བསལ་བ་ཉིད་དུ་ཤེས་པར་བྱའོ། །ཅིའི་ཕྱིར་ཞེ་ན། འདིར་དོན་གཞན་ཅུང་ཟད་མ་སྨྲས་པ་སྟེ།[^297] མིག་ལྟ་བ་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་བཏང་སྟེ་བདག་ལྟ་བ་པོ་ཡིན་ནོ་ཞེས་སྨྲས་པ་འབའ་ཞིག་ཏུ་ཟད་པའི་ཕྱིར་རོ། །

[Block 452]
དེ་ལ་ལྟ་བ་ལ་ལྟ་བ་པོར་རྟོག་གམ་བདག་ལ་ལྟ་བ་པོར་རྟོག་ཀྱང་རུང་སྟེ་བསལ་བའི་གཏན་ཚིགས་དག་ནི་མཚུངས་སོ། །

[Block 453]
འདིར་སྐྱོན་གཞན་འདི་ཡང་ཡོད་དེ། ལྟ་བ་པོས་ལྟ་བས་ལྟ་བར་བྱེད་ན་ལྟ་བ་གསུམ་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 454]
སྨྲས་པ། ལྟ་བས་ལྟ་བར་བྱེད་ཞེའམ་ལྟ་བ་པོས་ལྟ་བར་བྱེད་དོ་ཞེས་བྱ་བ་འདིས་ཁོ་བོ་ལ་ཅི་བྱ། ཡོང་ནི་བལྟ་བར༌[^298]བྱ་བ་བུམ་པ་དང་སྣམ་བུ་ལ་སོགས་པ་དག་ཡོད་པ་ལ་གང་གིས་ལྟ་བར་བྱེད་པའི་ལྟ་བ་དེ་ནི་ཡོད་དོ། །

[Block 455]
བཤད་པ། ཅི་ཁྱོད་ས་མཁན་མེད་པར་འབྲོག་དགོན་པར་འཐོམ་མམ། ཁྱོད་ལྟ་བ་པོ་མེད་པར་བལྟ་བར༌[^299]བྱ་བ་དང་ལྟ་བ་ཡོད་པར་འདོད་ཀོ། །

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
--- END BLOCKS ---
