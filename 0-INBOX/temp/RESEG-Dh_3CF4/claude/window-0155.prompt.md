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
[Block 5426]
དེ་རབ་ཏུ་གྲུབ་པ་ནི་མངོན་སུམ་ལ་སོགས་པའི་རིགས་པའི་ཚད་མ་དག་གིས་སོ། །

[Block 5427]
སྐྱེ་བ་འདི་ལས་གཞན་པའི་སྐྱེ་བ་དེ་ཡང་འཇིག་རྟེན་ཕ་རོལ་ཞེས་བརྗོད་དོ། །

[Block 5428]
དེ་ཡོད་པར་ནི་ལུང་གི་ཚིག་གིས་བསྟན་པ་དང་། [^3453]བརྟག་པའི་རིམ་པ་སྟེ། བརྟག་པའི་རིམ་པ༌[^3454]ནི། རིགས་པས་ཡིད་ཆེས་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5429]
དེ་ལས་མིའི་འཇིག་རྟེན་ལས་གཞན་པའི་འཇིག་རྟེན་ཡོད་པར་བསྟན་པའི་ཕྱིར་ཏེ། [^3455]ཉི་ཟླ་སྐར་མས་བརྒྱན་པའི་ནམ་མཁའ་དང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5430]
ཉི་ཟླ་སྐར་མས་བརྒྱན་པའི་ནམ་མཁའ་དང་། །ཞེས་བྱ་བ་འདིས་ནི་མིའི་འཇིག་རྟེན་འདི་ལས་གཞན་པའི་འཇིག་རྟེན་ཉིད་མངོན་སུམ་གྱི་རིགས་པའི་ཚད་མས་གཟུང་དུ་རུང་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5431]
དུད་འགྲོ༌[^3456]བརྟག་པ་ནི། དུད་འགྲོ་བརྟག་པ་སྟེ། གླང་པོ་ཆེ་དང་།

[Block 5432 [VERSE]]
རྟ་དང་བོང་བུ་རྔ་མོ་དང་། །
བྱ་ལ་སོགས་པའི་མཚན་ཉིད་དོ། །

[Block 5433]
རྣམ་པ་མང་པོ་ཞེས་བྱ་བ་ནི། རིགས་གཅིག་ལ་རྣམ་པ་མང་པོ་མཐའ་ཡས་སོ།[^3457] །འདི་ལྟར་འབུ་སྲིན་ལ་སོགས་པ་གཞན་དག་ཀྱང་། དེ་བཞིན་ཉིད༌[^3458]དུ་སྦྱར་ཏེ། འདིས་ནི་མིའི་འཇིག་རྟེན་ལས་གཞན༌[^3459]དུ་དུད་འགྲོ་མངོན་སུམ་གྱིས་ཡོད་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5434]
མངོན་སུམ་དུ་གསལ་བར་སྣང་བ་ནི་མངོན་སུམ་བཞིན་དུའོ། །

[Block 5435]
འདི་ལ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་ལོ། །

[Block 5436]
སྩོགས་པ་སྨོས་པས་གཟུང་བའི་ལུང་དང་། རྗེས་སུ་དཔག་པ་ནི་འདིར་མི་གཟུང་ངོ་། །འདིར་ད་ལྟར་བྱུང་བ་སྐྱེ་བ་ལ། འདས་པའི་སྐྱེ་བ་ཡོད་པ་ཉིད་དུ་རིགས་པས་བསྟན་པ་ཉིད་དོ། །

[Block 5437]
མིའི་སྐྱེ་བ་ཡོད་པར་སྒྲུབ༌[^3460]པ་ཡིན་ནོ། །

[Block 5438]
ལུང་གི་ཚིག་ནི་ཕྱོགས་གཉི་ག་ལ་ཡང་གྲུབ་པའི་ཕྱིར། ལུང་གི་ཚིག་གཉི་གར་ཡང་ངོ་། །བསམ་གཏན་གོམས་བྱས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་དྲུག་སྨོས་ཏེ། སྐྱེ་བ་འདི་ལས་འདས་པའི་སྐྱེ་བ་རྗེས་སུ་དཔག་པས་ཡོད་པ་ཉིད་དུ་སྒྲུབ་པའི༌[^3461]ཕྱིར། བསམ་གཏན་གོམས་བྱས་ཞེས་བྱ་བའི༌[^3462]ཚིགས་བཅད་འདི་སྨོས་ཏེ། ད་ལྟར་བྱུང་བའི་སྐྱེ་བ་ལས༌[^3463]འདས་པའི་སྐྱེ་བ་དམིགས་ཏེ་དྲན་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 5439]
འཇིག་རྟེན་ཕ་རོལ་ཡོད་དོ་ཞེས་བྱ་བ་ལ། འཇིག་རྟེན་ཕ་རོལ་ཡོད་པ་ཉིད་དུ་སྒྲུབ་པའི་ཕྱིར། འཇིག་རྟེན་ཕ་རོལ་ཡོད་པ་ནི་འདས་པའི་སྐྱེ་བ་ཡོད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5440]
བསམ་གཏན་ལ་གོམས་པ་དང་། དྲན་པ་གསལ་བ་ཉིད་ཀྱིས་ནི་སྐྱེ་བར་སྣང་བའི་ཕྱིར་རོ། །

[Block 5441]
ང༌[^3464]བདག་ལས་ཀྱང་མངོན་པར་མི་འགྱུར་རམ། །ཞེས་བྱ་བ་ནི། བདག་ཉིད་དཔེ་ཉིད་དུ་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5442]
བསམ་གཏན་གོམས་བྱས་ཞེས་བྱ་བ་ནི་བསམ་གཏན་ལ་བརྟེན་ནས། སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པའི་ཤེས་པའི་མངོན་པར་ཤེས་པ་སྟོན་ཏོ། །

[Block 5443]
དྲན་པ་གསལ་བ་ཞེས་བྱ་བ་ནི་བསམ་གཏན་ཐོབ་ན། ཚེ་རབས་དྲན་པའི་རྒྱུ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5444]
དེ་ལས་ཞེས་བྱ་བ་ནི་ཚེ་རབས་དྲན་པར་སྣང་བ་དང་། ཚེ་རབས་དྲན་པའི་ཕྱིར་རོ། །

[Block 5445]
ལྷག་མ་ཐམས་ཅད་ཀྱང་འཇིག་རྟེན་ཕ་རོལ་ཡོད་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་ཚིགས་བཅད་ལྔ་སྨོས་སོ། །

[Block 5446]
བློ་གཞན་སོང་བ་ལས་བློ་གཞན་སྐྱེ་བ་ཡིན་ཏེ། དེ་བས་ན་འཇིག་རྟེན་ཕ་རོལ་ཡོད་དོ་ཞེས་སྒྲུབ་པའི་ཕྱིར། སྔ་མའི་བློ་ལས་ཕྱི་མའི་བློ་འགྲུབ་ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། མངལ་ན་འདུག་པའི་སྔོན་རོལ་བློ། །ཞེས་བྱ་བ་ནི་བློ་སྔོན་དུ་བྱས་པ་ལས༌[^3465]ཐམས་ཅད་འགྱུར་ཏེ། བློ་སྔོན་དུ་འགྲོ་བར་སྣང་བས། དཔེར་ན་ད་ལྟར་བྱུང་བའི་མངལ་གྱི་སྔ་རོལ་དུ་བློ་འབྱུང་བ་ནི་སྔ་མའི་བློ་ཡིན་ཏེ། དེ་ནི་འཇིག་རྟེན་ཕ་རོལ་ལོ། །

[Block 5447]
དེ་བས་ན༌[^3466]འཇིག་རྟེན་ཕ་རོལ་ཡོད་པ་ཉིད་དོ། །

[Block 5448]
དང་པོའི་བློ་ནི་ཡུལ་ཡོད་པར་གྱུར་པའི་ཕྱིར། འཇིག་རྟེན་ཕ་རོལ་ཡོད་པ་ཡིན་ནོ་ཞེས་སྒྲུབ་པའི་ཕྱིར། ཤེས་བྱ་རྟོགས་པར་བྱེད་པ་བློ་ཡིན་ཟེར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5449]
དང་པོའི་སྐྱེ་བའི་བློ་ནི་ཡུལ་ཡོད་པ་ཉིད་དོ། །

[Block 5450]
[^3467]ཡུལ་མེད་པར་ནི་བདག་ཉིད་ཀྱིས་རྟོགས་པར་མི་སྣང་བའི་ཕྱིར་ཏེ། ད་ལྟར་བྱུང་བའི་བློ་ལྟ་བུར་རོ། །

[Block 5451]
དང་པོའི༌[^3468]བློའི་ཡུལ་དུ་གྱུར་པ་དེ་ནི་འཇིག་རྟེན་ཕ་རོལ་ཏེ། དེ་བས་ན་འཇིག་རྟེན་ཕ་རོལ་ཡོད་དོ། །

[Block 5452]
དང་པོའི་བློ་ནི་འདས་པའི་ཡུལ་གྱི་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། མིག་ལ་སོགས་པའི་དབང་པོ་ལྔ་དག་མེད་ཅིང་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཡང་མིག༌[^3469]ལ་སོགས་པའི་དབང་པོ་གང་ལ་བརྟེན་ནས་སྐྱེ་བ་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 5453]
ཁ་ཅིག་འདི་སྐད་བརྗོད་དེ། ཇི་ལྟར་ཤིང་ལ་སོགས་པ་སེམས་ཅན་མ་ཡིན་པ་སྟོན་པ་རྣམས་རང་གི་ས་བོན་གྱི་བྱེ་བྲག་གིས་སྣ་ཚོགས་པའི་ངོ་བོ་ཡང་ཡོད་དེ། དེ་དག་ལ་འཇིག་རྟེན་ཕ་རོལ་མེད་པ་དེ་བཞིན་དུ་སེམས་ཅན་དུ་བསྟན་པའི་དངོས་པོ་རྣམས་ཀྱང་ཕ་མའི་ཁུ་ཁྲག་གི་ས་བོན་གྱི་བྱེ་བྲག་གིས་དེ་དེ་དང་མཐུན་པར་སྣ་ཚོགས་པའི་ངོ་བོ་ཉིད་ཡོད་དེ། འཇིག་རྟེན་ཕ་རོལ་ན་ནི་མེད་དོ་ཞེས་དེ་ལྟར་སྨྲས་པ་དེའི་དབང་དུ་བྱས་ནས། སྐྱེ་དགུའི་ཚུལ་ཁྲིམས་ལ་སོགས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5454]
ཕ་མ་གཉིས་ཀྱི་ཡིན་པས་ཕ་མ་གཉིས་ཀྱིའོ། །

[Block 5455]
དེའི་རང་བཞིན་དག་དང་མི་མཐུན་པ་ནི་འདས་པའམ་ཐ་དད་པའོ། །

[Block 5456]
ཚུལ་ཁྲིམས་ལ་སོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པས་ནི་གཟུགས་བཟང་བ་དང་། གཟུགས་ངན་པ་དང་། ཕྱུག་པོ་དང་། དབུལ་པོ་ལ་སོགས་པའི་མཚན་ཉིད་ཀྱི་དབྱེ་བའོ། །

[Block 5457]
གློ་བུར༌[^3470]དུ་གྱུར་པ་མེད་དེ་ཞེས་བྱ་བས་ནི། རྒྱུ་མེད་པའི་སྨྲ༌[^3471]བའི་རྒྱུ་མེད་པའི་དབྱེ་བའི་སྦྱོར་བས་སོ། །

[Block 5458]
ཡང་ན་རྒྱུ་མེད་པའི་གང་ཡང་འབྱུང་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 5459]
གལ་ཏེ་དེ་ལྟ་ཡིན་ན་ནི་ཕ་མ་ལ་སོགས་པའི་ས་བོན་གྱི་བྱེ་བྲག་ལས་སེམས་ཅན་རྣམས་ཀྱི་ཁྱད་པར་དེ་ལྟར་འཇུག་པ་མེད་དམ་ཞེ་ན། མེད་དེ་ཅིའི་ཕྱིར་ཞེ་ན། ཚུལ་ཁྲིམས་ལ་སོགས་པའི་བྱེ་བྲག་ཕ་མའི་རང་བཞིན་དག་དང་མི་མཐུན་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 5460]
འཇིག་རྟེན་རྒྱང་ཕན་པ༌[^3472]ལ་སོགས་པ་ཁ་ཅིག་འདི་སྐད་དུ་གློ་བུར༌[^3473]དུ་སྒྲུབ་པ་ཡིན་ནོ་ཞེས་སྨྲས་ཏེ། གློ་བུར༌[^3474]འབྱུང་བ་ནི་ཞེས༌[^3475]མི་སྣང་བའི་ཕྱིར། འཇིག་རྟེན་ཕ་རོལ་ནི་ཡོད་དེ། ཐམས་ཅད་ཀྱང་རྒྱུ་དང་བཅས་པས་སྣང་བའི་ཕྱིར་རོ། །

[Block 5461]
འདི་ལྟར་བུམ་པ་ལ་སོགས་པ་ལ་གློ་བུར༌[^3476]གྱི་དབྱེ་བ་མ་མཐོང་བའི་ཕྱིར། ཇི་ལྟར་ནམ་མཁའ་ལྟ་བུའོ། །

[Block 5462]
འོན་ཀྱང་ལྷག་མ་ནི་སྐྱེ་བ་གཞན་ལ་གོམས་པའི་ཁྱད་པར་ཡིན་ཏེ། དེ་བས་ན་འཇིག་རྟེན་ཕ་རོལ་ཡོད་དོ། །

[Block 5463]
སྐྱེས་མ་ཐག་ཏུ་སེམས་ཅན་གྱི་སྐྱེ་བའི་རྒྱུ་སྲེད་པས་བྱས་པའི་བྱ་བ་ལ་འཇུག་པར་སྣང་བ་ལས་བརྩམས་ཏེ། བློའི་མཐུ་སྟོབས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5464]
བློའི་མཐུ་སྟོབས་ཞེས༌[^3477]བྱ་བ་ནི། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 5465]
བླུན་པའི་དབང་པོ་རྣམས་ཀྱང་ཞེས་བྱ་བ་ནི་དབང་པོ་ལྔའི་རྣམ་པར་ཤེས་པའོ། །
--- END BLOCKS ---
