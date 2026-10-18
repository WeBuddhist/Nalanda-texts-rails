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
[Block 351]
བཅོམ་ལྡན་འདས་ཀྱིས། འདི་ལ་རྣམ་པར་བརྟགས་པ་དང་རྣམ་པར་དཔྱད་པ་གང་ཡིན་པ་འདི་ནི་འདིར་འཕགས་པ་རྣམས་ཀྱིས་གཡོ་བའོ་ཞེས་གསུངས་སོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་བསམ་གཏན་གསུམ་པོ་གཡོ་བ་དང་བཅས་པར་གསུངས་པ་མ་ཡིན་ནམ་ཞེ་ན། དེ་དག་གི་ཏིང་ངེ་འཛིན་སྐྱོན་དང་བཅས་པ་ལས་དགོངས་ནས་དེ་སྐད་དུ༌[^258]གསུངས་པར་ཟད་ཀྱི། དེ་དག་ནི་མི༌[^259]གཡོ་བའི་མདོ་ལས་མི་གཡོ་བ་དང་མཐུན་པར་འགྲོ་བའི་ལམ་ལས་བརྩམས་ཏེ་མི་གཡོ་བར་གསུངས་སོ། །

[Block 352]
ཡང་ཅིའི་ཕྱིར་གཡོ་བ་དང་བཅས་པ་ཁོ་ན་གཞན༌[^260]དུ་མི་གཡོ་བར་གསུངས་ཤེ་ན།

[Block 353 [VERSE]]
གང་ཕྱིར་ས་ནི་དེ་དག་ཏུ། །
ལས་རྣམས་སྨིན་ཕྱིར་མི་གཡོའི་ཕྱིར། །

[Block 354]
འདོད་པ་ན་སྤྱོད་པའི་ལས་ནི་རྣམ་པར་སྨིན་པའི་ཕྱིར་གཡོ་བ་ཡིན་ནོ། །

[Block 355]
ཇི་ལྟར་གཡོ་ཞེ་ན་རྣམ་པར་མི་གནས་པའི་ཕྱིར་འགྲོ་བ་གཞན་ཡང་འགྲོ་བ་གཞན་དུ་རྣམ་པར་སྨིན་པར་འགྱུར་ལ། ལྷའི་རིས་གཞན་པ་ཡང་ལྷའི་རིས་གཞན་དུ་རྣམ་པར་སྨིན་པར་འགྱུར་ཏེ། བོང་ཚོད་དང་སྟོབས་དང༌[^261]ཁ་དོག་དང་བདེ་བ་དང་ལོངས་སྤྱོད་ལ་སོགས་པར་འགྱུར་བའི་ལས་ལྷ་དག་གི་ནང་དུ་རྣམ་པར་སྨིན་པར་འགྱུར་བ་གང་ཡིན་པ་དེ་ཉིད་རེས་འགའ་རྐྱེན་གཞན་གྱི་དབང་གིས་མི་དང་དུད་འགྲོ་དང་ཡི་དགས་ཀྱི་ནང་དུ་རྣམ་པར་སྨིན་པར་འགྱུར་རོ། །

[Block 356]
གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ལས་ནི་ས་གཞན་ལས་གཞན་དུ་རྣམ་པར་སྨིན་པར་ནམ་ཡང་མི་ནུས་སོ། །

[Block 357]
དེ་ལྟ་བས་ན་རྣམ་པར་སྨིན་པ་རྣམ་པར་གནས་པའི་ཕྱིར་མི་གཡོ་བ་ཞེས་བྱའོ། །

[Block 358]
བསོད་ནམས་མ་ཡིན་པའི་ལས་ནི་མི་དགེ་བའོ་ཞེས་འཇིག་རྟེན་ན་གྲགས་བས་འཇིག་རྟེན་ལས༌[^262]གྲགས་པ་གང་ཡིན་པ་དེ་ལ་འབད་པས་ཅི་ཞིག་བྱ། བསོད་ནམས་ལ་སོགས་པའི་ལས་བསྟན་ཟིན་ཏོ། །

[Block 359 [HEADING]]
### བདེ་བ་མྱོང་བར་འགྱུར་བ་ལ་སོགས་པ། ^1-24-0

[Block 360]
བདེ་བ་མྱོང་བར་འགྱུར་བ་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ་དེ་ཙམ༌[^263]མོ། །

[Block 361]
བསམ་གཏན་གསུམ་པའི་བར་དགེ་བ། །བདེ་བ་མྱོང་འགྱུར། བསམ་གཏན་གསུམ་པའི་བར་གྱིས༌[^264]ལས་དགེ་བ་ནི་བདེ་བ་མྱོང་བར་འགྱུར་བ་ཡིན་པས་བདེ་བའི་ཚོར་བའི་ས་ནི་འདི་ཡིན་ཏེ། འདི་ལྟ་སྟེ། འདོད་པའི་ཁམས་དང་བསམ་གཏན་གསུམ་མོ། །

[Block 362]
དེ་ཡན་ཆད། སྡུག་མིན་བདེ་མིན་མྱོང་འགྱུར་བ། །བདེ་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། བསམ་གཏན་གསུམ་པ་ཡན་ཆད་ཀྱི་ལས་དགེ་བ་ནི་བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ༌[^265]ཡང་མ་ཡིན་པ་མྱོང་བར་འགྱུར་བ་ཡིན་ཏེ། དེ་ན་བདེ་བ་དང་སྡུག་བསྔལ་གྱི་ཚོར་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 363]
སྡུག་བསྔལ་མྱོང་འགྱུར་འདིའི་མི་དགེ །ལས་མི་དགེ་བ་ནི་སྡུག་བསྔལ་མྱོང་བར་འགྱུར་བའོ། །

[Block 364]
འདིའི་ཞེས་སྨོས་པ་ནི་འདོད་པའི་ཁམས་ཁོ་ན་ན་དེ་ཡོད་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 365]
འདི་དག་གི་འབྲས་བུ་ཚོར་བ་འབའ་ཞིག་ཏུ་ནི་མ་ཟད་དོ། །

[Block 366]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 367 [VERSE]]
ཚོགས་དང་བཅས་པ་ཡིན་ནོ། །
འོག་ནའང་བར་མ་ཡོད་དོ་ཞེས། །

[Block 368]
ཁ་ཅིག་ཟེར་ཏེ། གཞན་དག་ན་རེ་བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་ཡང་མ་ཡིན་པ་མྱོང་བར་འགྱུར་བའི་ལས་སུ་བཤད་པ་གང་ཡིན་པ་དེ་ནི་བསམ་གཏན་བཞི་པ་མན་ཆད་ན་ཡང་ཡོད་དོ་ཞེས་ཟེར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། གང་གི་ཕྱིར། བསམ་གཏན་ཁྱད་པར་རྣམ་སྨིན་ལས། །

[Block 369]
དེ་ལྟར༌[^266]མ་ཡིན་ན་བསམ་གཏན་ཁྱད་པར་ཅན་གྱི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་མེད་པའམ། ལས་གང་གིས་ཀྱང་བསམ་གཏན་ཁྱད་པར་ཅན་དུ་རྣམ་པར་སྨིན་པར་མི་འགྱུར་ཏེ། དེ་ན་བདེ་བ་དང་སྡུག་བསྔལ་དག་མེད་པའི་ཕྱིར་རོ། །

[Block 370]
ཁ་ཅིག་ན་རེ་བསམ་གཏན་ཁྱད་པར་ཅན་གྱིས༌[^267]ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ནི་བསམ་གཏན་གྱི་བདེ་བའི་དབང་པོ་ཁོ་ན་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 371]
གཞན་དག་ན་རེ་དེའི་རྣམ་པར་སྨིན་པ་ཚོར་བ་མེད་པ་ཉིད་དོ་ཞེས་ཟེར་རོ། །

[Block 372]
འདི་ནི་བསྟན་བཅོས་དང་འགལ་བ་ཡིན་ཏེ། བསྟན་བཅོས་ལས་ནི། ལས་ཀྱི་རྣམ་པར་སྨིན་པ་སེམས་ཀྱི་ཚོར་བ་ཁོ་ན་རྣམ་པར་སྨིན་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན།[^268] ཡོད་དོ། །

[Block 373]
རྟོག་པ་མེད་པའི་ལས་དགེ་བ་ཡིན་ནོ་ཞེས་འབྱུང་ངོ་། །སྔ་ཕྱི་མེད་གསུམ་སྨིན་འདོད་ཕྱིར། །ཇི་ལྟར་ལས་གསུམ་པོ་རྣམས་ཀྱི་རྣམ་པར་སྨིན་པ་སྔ་ཕྱི་མེད་པར་སྨིན་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན། ཡོད་དེ། བདེ་བ་མྱོང་བར་འགྱུར་བ་ནི་གཟུགས་སོ། །

[Block 374]
སྡུག་བསྔལ་མྱོང་བར་འགྱུར་བ་ནི་སེམས་དང་སེམས་ལས་བྱུང་བའི་ཆོས་རྣམས་སོ། །

[Block 375]
བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ་ཡང་མ་ཡིན་པ་མྱོང་བར་འགྱུར་བའི་ལས༌[^269]ནི་སེམས་དང་ལྡན་པ་མ་ཡིན་པའི་འདུ་བྱེད་རྣམས་སོ་ཞེས་འབྱུང་སྟེ། འདིའི་ཕྱིར་ཡང་འོག་ན་བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ༌[^270]ཡང་མ་ཡིན་པ་མྱོང་བར་འགྱུར་བའི་ལས་ཡོད་དེ། འདོད་པའི་ཁམས་ལས་གཞན་ན༌[^271]ནི་ལས་གསུམ་གྱི་རྣམ་པར་སྨིན་པ་དང་ཅིག་ཅར་དུ་ལྡན་པ་མེད་དོ། །

[Block 376]
ད་ནི་ཅི་ལས་དེ་དགེ་བ་ཡིན་ནམ། འོན་ཏེ་མི་དགེ་བ་ཡིན་ཞེ་ན། དགེ་བ་སྟེ་སྟོབས་ཆུང་ངུ་ནི་མ༌[^272]ཡིན་ནོ། །

[Block 377]
དེ་ལྟ་ན་ནི་འོ་ན། བསམ་གཏན་གསུམ་པའི་བར་དགེ་བ། །བདེ་བ་མྱོང་འགྱུར་ཞེས་བྱ་བ༌[^273]དང་། རྣམ་པར་སྨིན་པ་ཡིད་དུ་འོང་བ་ནི་དགེ་བ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་དང་འགལ་ལོ། །

[Block 378]
དེ་ནི་ཕལ་ཆེ་བ་བསྟན་པ་ཡིན་པར་བལྟ་བར༌[^274]བྱའོ། །

[Block 379]
ཇི་ལྟར་ན་ཚོར་བའི་རང་བཞིན་མ་ཡིན་པའི་ལས་བདེ་བ་མྱོང་བར་འགྱུར་བ་ཞེས་བྱ་ཞེ་ན། བདེ་བ་མྱོང་བར་འགྱུར་བ་དང་མཐུན་པའམ། འདིའི་བདེ་བ་མྱོང་བར་བྱ་བ་ཡིན་པས་ན་བདེ་བ་མྱོང་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 380]
མྱོང་བར་འགྱུར༌[^275]བ་ཡང་གང་ཞིག་ཡིན་ཞེ་ན། རྣམ་པར་སྨིན་པ་སྟེ། དེ་མྱོང་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 381]
ཡང་ན་བདེ་བ་མྱོང་བར་འགྱུར་བ་ཡིན་པས་བདེ་བ་མྱོང་བར་འགྱུར་བ་སྟེ། གང་གི༌[^276]བདེ་བ་མྱོང་བར་འགྱུར་བ་ནི། འཁྲུ་བར་བྱེད་པའི་འདག་པའི་ཆལ་བཞིན་ནོ། །

[Block 382]
སྡུག་བསྔལ་མྱོང་བར་འགྱུར་བ་དང་། སྡུག་བསྔལ་ཡང་མ་ཡིན་བདེ་བ་ཡང་མ་ཡིན་པ་མྱོང་བར་འགྱུར་བ་ལ་ཡང་དེ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 383 [HEADING]]
### མྱོང་འགྱུར་རྣམ་པ་ལྔ། ^1-25-0

[Block 384]
གཞན་ཡང་།

[Block 385 [VERSE]]
ངོ་བོ་ཉིད་དང་མཚུངས་ལྡན་དང་། །
དམིགས་པ་དང་ནི་རྣམ་སྨིན་དང་། །
མངོན་སུམ་དུ་ནི་གྱུར་པ་ལས། །
མྱོང་འགྱུར་རྣམ་པ་ལྔ་ཡིན་ནོ། །

[Block 386]
ངོ་བོ་ཉིད་ཀྱིས་མྱོང་བར་འགྱུར་བ་ནི་ཚོར་བ་རྣམས་སོ། །

[Block 387]
མཚུངས་པར་ལྡན་པས་མྱོང་བར་འགྱུར་བ་ནི་རེག་པ་སྟེ། བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པ་ཞེས་བྱ་བའོ། །

[Block 388]
དམིགས་པ་མྱོང་བར་འགྱུར་བ་ནི་ཡུལ་རྣམས་ཏེ། ཇི་སྐད་དུ། མིག༌[^277]གིས་གཟུགས་རྣམས་མཐོང་ནས་གཟུགས་སོ་སོར་ཡང་དག་པར་མྱོང་བར་འགྱུར་གྱི་གཟུགས་ལ་འདོད་ཆགས་སོ་སོར་ཡང་དག་པར་མྱོང་བ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་གསུངས་པ་སྟེ། དམིགས་པ་ན༌[^278]ཚོར་བས་དེ་དག་སོ་སོར་ཡང་དག་པར་མྱོང་བར་བྱེད་དོ། །

[Block 389]
རྣམ་པར་སྨིན་པ་མྱོང་བར་འགྱུར་བ་ནི་ལས་ཡིན་ཏེ། མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཞེས་བྱ་བ་རྒྱས་པར་འབྱུང༌[^279]བའོ། །

[Block 390]
མངོན་སུམ་དུ་གྱུར་པ་མྱོང་བར་འགྱུར་བ་ནི་ཇི་སྐད་དུ། གང་གི་ཚེ་བདེ་བའི་ཚོར་བ་མྱོང་བར་བྱེད་པ་དེའི་ཚེ༌[^280]ཚོར་བ་གཉིས་འགག་པར་འགྱུར་རོ༌[^281]ཞེས་གསུངས་པ་སྟེ། གང་གི༌[^282]ཚེ་བདེ་བའི་ཚོར་བ་འཇུག་པ་དེའི་ཚེ་གང་གིས་ན་དེ་མྱོང་བར་འགྱུར་བ༌[^283]གཞན་ནི་མེད་ཀྱི་དེས་མངོན་སུམ་དུ་བྱེད་ན་ནི་དེ་མྱོང་བར་འགྱུར་ཞེས་བྱ་སྟེ། དེའི་ཕྱིར་རྣམ་པར་སྨིན་པ་མྱོང་བར་འགྱུར་བ་ཡིན་པའི་ཕྱིར་ལས་ཀྱང་བདེ་བ་མྱོང་བར་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^284]བརྗོད་དོ། །
--- END BLOCKS ---
