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

━━━ TOPIC SHIFT vs CONTINUATION (from the editors' corrections) ━━━

The editors' blocks are large (median ≈ 55 syllables; whole explanations of
100–250 syllables are normal). A sentence end is NOT a boundary. Inside one
explanation they cut only where the commentary turns to something new:
  START a new block at   "ཡང་ན་ …" (an alternative explanation)
                         "ཁ་ཅིག་ …", "གཞན་དག་ …" (another party's view)
                         "འོ་ན་ …" (the reply to an objection)
                         "དེ་སྐད་དུ་ …", "ཇི་སྐད་དུ་ …" (introducing a supporting quotation)
                         "དེ་ནས་ …" when it opens the next step of a procedure
                         "དཔེ་ …" / "དཔེར་ན་ …" when an example section begins
KEEP WITH the block before (merge into it):
                         "ད་ནི་ …" — a transitional "now …" line is not a new unit
                         (no heading or verse between them)
                         "ལེའུ་ … པའོ། །" — a chapter-closing line stays with the
                         explanation it closes
                         "ཞེས་ / ཅེས་ …" — the quotative closing the words just before it

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
[Block 456]
དེ་བས་ན་འདི་ནི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱི་ཐེག་པ་ཆེན་པོ་ཞེས་བྱའོ་ཞེས་བྱ་བ་ནི་ཆེན་པོ་རྣམས་ཀྱི་ཐེག་པ་ཡིན་པས་ཐེག་པ་ཆེན་པོ་ཞེས་བྱ་བར་ངེས་པའི་ཚིག་གིས་བསྟན་ཏོ། །

[Block 457 [HEADING]]
#### གཏན་ལ་དབབ་པའི་ཚིག་བཅུ་གཉིས། ^1-1-7-0

[Block 458]
བཅོམ་ལྡན་འདས་གནས་བརྟན་རབ་འབྱོར་འདི་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སླད་དུ་བསྒོ་བ་མཛད་པས་འདི་ནི་ཐེག་པ་ཆེན་པོ་བསྟན་པར་སེམས་སོ་ཞེས་བྱ་བ་ནི་གནས་བརྟན་གང་པོས་འོག་ནས་བཤད་པའི་སྐབས་དབྱེ་བའི་ཕྱིར་གསོལ་པའོ། །

[Block 459]
སྔར་གདམས་པ་དང་། རྗེས་སུ་བསྟན་པ་བཤད་པ་རྩོམ་པ༌[^290]ལས་བཅོམ་ལྡན་འདས་ཀྱིས་རབ་འབྱོར་ཁྱོད་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་བརྩམས༌[^291]ཏེ། ཅི་ནས་ཀྱང༌[^292]བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ངེས་པར་འབྱུང་བར་འགྱུར་བར་སྤོབས་པར་གྱིས་ཤིག་ཅེས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཕྱིར་བསྐོས་ལ། ད་ལྟར་ནི༌[^293]ཐེག་པ་ཆེན་པོ་བཤད་པ་བྱས་པ་ལས་ཞུས་པ་ནི་དེའི་སྒོ་ནས་འོག་ནས་བཤད་པའི་ལམ་འདོད་དོ། །

[Block 460]
བཅོམ་ལྡན་འདས་བདག་གིས༌[^294]ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་འགལ་བར་ཐེག་པ་ཆེན་པོ་བསྟན་པའམ་གཅིག་ཏུ་མ་གྱུར་ལགས་གྲང་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ཐེག་པ་ཆེན་པོ་གཉིས་ཐ་མི་དད་པའི་ཕྱིར། ཐེག་པ་ཆེན་པོ་བསྟན་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་བསྟན་པ་ཡིན་པར་དགོངས་པ་སྟེ། ཐེག་པ་ཆེན་པོ་བསྟན་པས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པར་འགྱུར་རོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པས་ཐེག་པ་ཆེན་པོ་བསྟན་པར་འགྱུར་རོ་ཞེས་ཐ་མའི༌[^295]ཚིག༌[^296]བསྟན་ཏོ། །

[Block 461 [HEADING]]
##### ས་བོན་གྱི་ཚིག། ^1-1-7-1-0

[Block 462]
བཅོམ་ལྡན་འདས་འདི་ལྟར་ཡང་བྱང་ཆུབ་སེམས་དཔའ་ནི་སྔོན་གྱི་མཐར་མི་དམིགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིག་བཅུས། འོག་ནས་བཤད་པའི་ས་བོན་གྱི་ཚིག་རྣམས་བསྟན་ཏོ། །

[Block 463]
དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་ནི་སྔོན་གྱི་མཐར་མི་དམིགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་བྱང་ཆུབ་སེམས་དཔའ་སྔོན་བྱུང་བ་དང་། ཕྱིས་འབྱུང་བ་དང་། ད་ལྟར་ཡང་ཡོད་དོ་ཞེས་དུས་གསུམ་ལ་བྱང་ཆུབ་སེམས་དཔའ་མི་དམིགས་པར་བསྟན་ཏོ། །

[Block 464]
གང་གི་ཕྱིར་མཐའ་གསུམ་པོ་འདི་དག་ལ་བྱང་ཆུབ་སེམས་དཔའ་མི་དམིགས་པ་དེའི་ཕྱིར་མཐའ་མེད་པས་བྱང་ཆུབ་སེམས་དཔའ་ལ་མཐའ་ཐུག་པ་མེད་པར་བསྟན་ནས། དེའི་འོག་ཏུ་བཅོམ་ལྡན་འདས་གཟུགས་ཀུན་དུ་མཐའ་ཡས་པའི་སླད་དུ་བྱང་ཆུབ་སེམས་དཔའ་ཀུན་དུ་མཐའ་ཡས་པར་རིག་པར་བགྱིའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། གཟུགས་ལ་སོགས་པའི༌[^297]ཆོས་ཐམས་ཅད་ལ་མཐའ་གསུམ་མེད་པས་ཀུན་དུ་མཐའ་ཡས་པ་ཉིད་དེ། དེ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་ཡང་ཀུན་དུ་མཐའ་ཡས་པར་རིག་པར་བྱའོ། །ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 465]
གལ་ཏེ་གཟུགས་ལ་སོགས་པ་ཀུན་དུ་མཐའ་ཡས་པར༌[^298]བྱང་ཆུབ་སེམས་དཔའ་ཀུན་དུ་མཐའ་ཡས་པ་ཞེས་བྱ་ན། འོ་ན་ནི་གཟུགས་ལ་སོགས་པ་བྱང་ཆུབ་སེམས་དཔར་འགྱུར་རོ་སྙམ་པ་ལ། གཟུགས་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བགྱི་བ་དེ་ལྟ་བུ་ཡང་མ་མཆིས། མི་དམིགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 466]
དེ་ལྟར་དུས་གསུམ་ལ་བྱང་ཆུབ་སེམས་དཔའ་མི་དམིགས་པས་གཟུགས་ལ་སོགས་པ་ལ་ཡང་བྱང་ཆུབ་སེམས་དཔའ་ངོ་བོར་མི་དམིགས་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་དམིགས་སུ་མེད་དོ། །

[Block 467]
དེ་མི་དམིགས་པས་གདམས་པ་དང་། རྗེས་སུ་བསྟན་པ་གཉིས་ཀྱང་མེད་དོ། །

[Block 468]
བཅོམ་ལྡན་འདས་དེ་ལྟར་བདག་གིས་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་རྣམ་པ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་མ་དམིགས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་སྔར་བསྟན་པའི་དོན་ཉིད་བསྟན་ཏོ། །

[Block 469]
བཅོམ་ལྡན་འདས་འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བགྱི་བ་འདི་ནི་མིང་ཙམ་དུ་བས་སོ༌[^299]ཞེས་བྱ་བས་ནི་དེ་ལྟར་དམིགས་སུ་མེད་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ཀུན་བརྟགས་པ་ཙམ་དུ་ཟད་པར་སྟོན་ཏོ། །

[Block 470]
དེ་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་དོན་དམ་པར་མེད་པར་བསྟན་ནས་དཔེ་བསྟན་པའི་ཕྱིར། བཅོམ་ལྡན་འདས་འདི་ལྟ་སྟེ་དཔེར་ན་བདག་བདག་ཅེས་བགྱི་བ༌[^300]ཡང་། བདག་ནི་ཤིན་ཏུ་མངོན་པར་གྲུབ་པ་མ་མཆིས་པའོ་ཞེས་གསུངས་སོ། །

[Block 471]
དེ་ལྟར་བསྟན་ནས་དེའི་འོག་ཏུ་གཟུགས་ལ་སོགས་པ་མངོན་པར་འགྲུབ་པའི་མཚན་ཉིད་དང་། མངོན་པར་འགྲུབ་པ་མེད་པའི་མཚན་ཉིད་དེ་གཉི་ག་ཡང་མེད་པར་བསྟན་ཏེ།[^301] དེ་ལ་མངོན་པར་འགྲུབ་པའི་མཚན་ཉིད་མེད་པ་ནི་བཅོམ་ལྡན་འདས་དེ་ལྟར་རང་བཞིན་དངོས་པོ༌[^302]མ་མཆིས་པའི་ཆོས་རྣམས་ལ་གང་མངོན་པར་འགྲུབ་པའི་གཟུགས་དེ་གང་ལགས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་སྟེ། གཟུགས་ལ་སོགས་པ་ནི་སྒྱུ་མ་ལྟ་བུ་ཡིན་པས་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་དང་། མ་སྐྱེས་པའི་ཕྱིར་མངོན་པར་འགྲུབ་པའི༌[^303]མཚན་ཉིད་མེད་དོ། །

[Block 472]
དེའི་འོག་ཏུ་མངོན་པར་འགྲུབ་པ་མེད་པའི་མཚན་ཉིད་མེད་པ་བསྟན་པའི་ཕྱིར། གང་མངོན་པར་གྲུབ་པ་དེ་ནི་གཟུགས་མ་ལགས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། མངོན་པར་འགྲུབ་པ་མེད་པའི་མཚན་ཉིད་ནི་ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་ཡིན་གྱི། ཀུན་བརྟགས་པའི་གཟུགས་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 473]
དེ་ལྟར་ཀུན་བརྟགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་མེད་པའི་ཕྱིར་གདམས་པའི་འོས་མ་ཡིན་པར་བསྟན་ནས། ད་ནི་དོན་དམ་པའི་ཆོས་ཉིད་ཀྱི་བྱང་ཆུབ་སེམས་དཔའི་དབང་དུ་བྱས་ཏེ། བཅོམ་ལྡན་འདས་མངོན་པར་མ་གྲུབ་པ་ལས་གུད་ན༌[^304]བྱང་ཆུབ་ཀྱི་སླད་དུ་སྤྱོད་པར་འགྱུར་བའི་བྱང་ཆུབ་སེམས་དཔའ་དམིགས་སུ་མ་མཆིས་ན། མངོན་པར་མ་གྲུབ་པ་མངོན་པར༌[^305]གྲུབ་པའི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གདམས་ཤིང་རྗེས་སུ་བསྟན་པར་བགྱིའམ་ཞེས་བྱ་བ་གསོལ་ཏེ། དོན་དམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པས་མངོན་པར་མ་གྲུབ་པའི་མཚན་ཉིད་ཡིན་ཏེ། དེ་ཡང་སྤྲོས་པ་ཐམས་ཅད་ལས་འདས་པའི་ཕྱིར་གདམས་པ་དང་རྗེས་སུ་བསྟན་པའི་འོས་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 474]
དེ་ལྟར་དོན་དམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་བསྟན་ནས། གལ་ཏེ་དེ་ལྟར་བསྟན་པའི་ཚེ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་སེམས་ཞུམ་པར་མི་འགྱུར་ན། བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་དེ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྤྱོད་པར་རིག་པར་བགྱིའོ་ཞེས་བྱ་བས་ནི་དོན་དམ་པའི་སྤྱོད་པ་བསྟན་ཏོ། །

[Block 475 [HEADING]]
##### གཏན་ལ་དབབ་པའི་ཚིག་བཅུ་གཉིས་བཤད་པ། ^1-1-7-2-0

[Block 476]
འདི་མན་ཆད་ནི་སྔར་གླེངས་པ་ཉི་ཤུ་རྩ་དགུ་བཞག་པའི་ནང་ནས། རབ་འབྱོར་ཁྱོད་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་རྗེས་སུ་མཐུན་པར་ཐེག་པ་ཆེན་པོ་སྟོན་ཏོ་ཞེས་བྱ་བ་ནས་བཟུང་སྟེ། གཏན་ལ་དབབ་པའི་ཚིག་བཅུ་གཉིས་བཀོད་པ་གང་ཡིན་པ་དེ་དག་ད་བསྟན་པར་བྱའོ། །

[Block 477]
བསྟན་ནས་ཀྱང་བཤད་པར་བྱའོ། །

[Block 478 [HEADING]]
###### བྱང་ཆུབ་སེམས་དཔའ་སྔོན་གྱི་མཐར་མི་དམིགས་པ། ^1-1-7-2-1-0

[Block 479]
ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་སེམས་ཅན་མེད་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་སྔོན་གྱི་མཐའ་དང་། ཕྱི་མའི་མཐའ་དང་། དབུས་ཀྱི་མཐར་མི་དམིགས་སོ་ཞེས་བྱ་བ་ནི་གང་ཟག་ལ་བདག་མེད་པའི་ཕྱིར་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་འདས་པའི་དུས་ན་བྱུང་ངོ་། །བྱང་ཆུབ་སེམས་དཔའ་མ་འོངས་པ་ན་འབྱུང་བར་འགྱུར་རོ། །

[Block 480]
བྱང་ཆུབ་སེམས་དཔའ་ད་ལྟར་བྱུང་བ་ན་ཡོད་དོ་ཞེས་བྱ་བ་དུས་གསུམ་དུ་ཉེ་བར་འགྲོ་བ་མེད་དོ་ཞེས་བྱ༌[^306]བ་བསྟན་ཏོ། །

[Block 481]
དེའི་འོག་ཏུ་གཟུགས་མེད་པའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཆོས་ལ་བདག་མེད་པ་བསྟན་ཏོ། །

[Block 482]
འདི་དག་ཐམས་ཅད་གཉིས་སུ་མེད་དེ་གཉིས་སུ་བྱར་མེད་དོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད༌[^307]ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་དུ་ཐམས་ཅད་གཅིག་པར་དགོངས་པའོ། །

[Block 483]
ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་དེ་བཞིན་ཉིད་མེད་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་སྔོན་གྱི་མཐར་མི་དམིགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དུས་གསུམ་གྱི་དེ་བཞིན་ཉིད་དང་། བྱང་ཆུབ་སེམས་དཔའི་དེ་བཞིན་ཉིད་ཀུན་བརྟགས་པ་ཡིན་པའི་ཕྱིར་མེད་པའོ། །

[Block 484 [HEADING]]
###### བྱང་ཆུབ་སེམས་དཔའ་ཀུན་དུ་མཐའ་ཡས་པ། ^1-1-7-2-2-0

[Block 485]
ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་ཅིའི་ཕྱིར་གཟུགས་ཀུན་དུ་མཐའ་ཡས་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ཀུན་དུ་མཐའ་ཡས་པར་རིག་པར་བྱ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཚིག་གཉིས་པ་བསྟན་ཏེ། ཀུན་དུ་མཐའ་ཡས་པ་དེ་དག་གི་སྔོན་གྱི་མཐའ་ལ་སོགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 486 [HEADING]]
###### གཟུགས་ནི་གཟུགས་ཀྱིས་སྟོང་པ། ^1-1-7-2-3-0

[Block 487]
ཚིག་གསུམ་པ་ལས།

[Block 488]
ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ༌[^308]གཟུགས་ནི་གཟུགས་ཀྱིས་སྟོང་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གྲུབ་པ༌[^309]ཆོས་ཉིད་ཀྱི་གཟུགས་ནི་ཀུན་བརྟགས་པའི་གཟུགས་ཀྱིས་སྟོང་ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 489]
དེ་བས་ན་སྟོང་པ་ཉིད་ལ་གཟུགས་མེད་ཅེས་བྱ་བ་གསུངས་ཏེ། གཟུགས་ཀྱི་སྟོང་པ་ཉིད་ལ་ཀུན་བརྟགས་པའི་གཟུགས་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 490 [HEADING]]
###### གཟུགས་ནི་གཟུགས་ལ་མི་དམིགས་པ། ^1-1-7-2-4-0

[Block 491]
ཚིག་བཞི་པ་ལ། གཟུགས་ནི་གཟུགས་ལ་མི་དམིགས། གཟུགས་ནི་ཚོར་བ་ལ་མི་དམིགས་ཞེས་བྱ་བ་ལ་སོགས་པས་རང་གི་དངོས་པོ་དང་། གཞན་གྱི་དངོས་པོ་ལ་བཙལ་ན་ཆོས་ཐམས་ཅད་མི་དམིགས་པར་བསྟན་པ་སྟེ། འདིས་ནི་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་རྣམ་པ༌[^310]ཐམས་ཅད་དུ་ཞེས་བྱ་བ་བཤད་པ་ཡིན་ནོ། །

[Block 492 [HEADING]]
###### གློ་བུར་དུ་མིང་དུ་བཏགས་པ། ^1-1-7-2-5-0

[Block 493]
ཚིག་ལྔ་པ་ལ་འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བ་འདི་ནི་གློ་བུར་དུ་མིང་དུ་བཏགས་པ་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའ་ནི་དོན་དམ་པ་སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་ཡིན་ན་ཀུན་རྫོབ་ཏུ་དེ་ལ་ཐ་སྙད་དུ་བྱ་བའི་ཕྱིར། བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བའི་མིང་གློ་བུར་དུ་བཏགས་པ་སྟེ། གློ་བུར་ཞེས་པ༌[^311]ནི་ངོ་བོ་ཉིད་དུ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 494]
འདི་ལྟར་ཆོས་ཐམས་ཅད་ཀྱི་མིང་ལྟར༌[^312]ཕྱོགས་བཅུ་གང་ནས་ཀྱང་མི་འོང་གང་དུ་ཡང་མི་འགྲོ་ཞེས་བྱ་བས་ནི་ཡོད་པ་མ་ཡིན་པ་ཉིད་སྟོན་ཏོ། །

[Block 495]
ཡང་དག་པར༌[^313]སྐྱེ་བའི་དུས་ན་ཡང་གང་ནས་ཀྱང་མི་འོང་ལ། འགག་པའི་དུས་ན་ཡང་གང་དུ་ཡང་མི་འགྲོའོ། །
--- END BLOCKS ---
