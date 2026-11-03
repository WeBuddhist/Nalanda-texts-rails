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
[Block 316]
སྡོམ་མིན། སྡོམ་པ་མ་ཡིན་པ་ནི་མིའི་འགྲོ་བ་ཁོ་ན་ལ་ཡོད་ཀྱི་གཞན་དག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 317]
དེ་ལ་ཡང་ཟ་མ་དང༌[^237]མ་ནིང་དང་མཚན་གཉིས་པ་དང་བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་ནི་མ་གཏོགས་སོ། །

[Block 318]
སྡོམ་པའང་དེ་བཞིན་ལ། ལྷ་ལའང་། སྡོམ་པ་ཡང་ཇི་སྐད་བཤད་པ་མ་གཏོགས་པ་མི་རྣམས་དང་། ལྷ་རྣམས་ལ་ཡོད་པས་འགྲོ་བ་གཉིས་ན་སྡོམ་པ་ཡོད་དོ། །

[Block 319]
ཟ་མ་ལ་སོགས་པ་ལ་སྡོམ་པ་མེད་དོ་ཞེས་བྱ་བ་ཇི་ལྟར་ཤེས་ཤེ་ན། མདོ་དང་འདུལ་བ་ལས་ཏེ།

[Block 320]
མདོ་ལས།

[Block 321]
མིང་ཆེན་འདི་ལྟར་ཁྱིམ་པ་གོས་དཀར་པོ་གྱོན་པ་སྐྱེས་པ་ཕོའི་དབང་པོ་དང་ལྡན་པ་ཞིག་སངས་རྒྱས་ལ་སྐྱབས་སུ་འགྲོ་བ་ནས་བདག་ལ་དགེ་བསྙེན་དུ་གཟུང་དུ་གསོལ་ཞེས་ཚིག་ཏུ་སྨྲ་བའི་བར་དུ་ཡང་བྱེད་ན་འདི་ཙམ་གྱིས་དགེ་བསྙེན་དུ་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 322]
འདུལ་བ་ལས་ཀྱང༌[^238]དེ་ལྟ་བུ་གསལ་བར༌[^239]བྱའོ་ཞེས་གསུངས་སོ། །ཅིའི་ཕྱིར༌[^240]དེ་དག་ལས་སྡོམ་པ་མེད་ཅེ་ན། རྟེན་གཉི་གའི་ཉོན་མོངས་པ་ཤས་ཆེ་བའི་ཕྱིར་དང་། སོ་སོར་རྟོག་པ་མི་བཟོད་པའི་ཕྱིར་དང་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་ཤས་ཆེན་པོ་མེད་པའི་ཕྱིར་རོ། །

[Block 323]
འོ་ན་སྡོམ་པ་མ་ཡིན་པ་ཅིའི་ཕྱིར་མེད་ཅེ་ན། སྡིག་པ་ལ་ཡང་བསམ་པ་མི་བརྟན་པའི་ཕྱིར་དང་། གང་ལ་སྡོམ་པ་ཡོད་པ་དེ་ལ་སྡོམ་པ་མ་ཡིན་པ་ཡང་ཡོད་དེ། གཉེན་པོར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 324]
བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་ལ་ནི་ཡང་དག་པར་ལེན་པ་དང་ཏིང་ངེ་འཛིན་མེད་པའི་ཕྱིར་དང་། སྡིག་པ་བྱ་བའི་བསམ་པ་མེད་པའི་ཕྱིར་སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་མེད་དོ། །

[Block 325]
ངན་སོང་བ་རྣམས་ལ་ཡང་གང་དང་ལྡན་པ་དང་གང་མེད་པས་སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་དག་ཏུ་འགྱུར་བ་ངོ་ཚ་ཤེས་པ་དང་། ཁྲེལ་ཡོད་པ་ཤས་ཆེན་པོ་མེད་དོ། །

[Block 326]
གཞན་ཡང་ཟ་མ་དང་། མ་ནིང་དང་། མཚན་གཉིས་པ་དང་། ངན་སོང་བ་དེ་དག་གི་ལུས་ཉིད་དུ༌[^241]ལུས་གང་ལ་སྡོམ་པ་ཡང་མི་སྐྱེ་སྡོམ་པ་མ་ཡིན་པ་ཡང་མི་སྐྱེ་བ་ཞིང་ཚ་སྒོ་ཅན་ལྟ་བུར་གྱུར་པ་ཡིན་ཏེ། ཞིང་ཚ་སྒོ༌[^242]ཅན་ལ༌[^243]འབྲུ་ཡང་ཚར༌[^244]ཅིག་མི་སྐྱེ། རྩྭ་ཡང་ཚར༌[^245]ཅིག་མི་སྐྱེ་བ་བཞིན་ནོ། །

[Block 327]
འོ་ན་མདོ་ལས།

[Block 328]
དགེ་སློང་དག་སྒོ་ང་ལས་སྐྱེས་པའི་ཀླུ་ནི་ཟླ་བ་ཕྱེད་ཀྱི་ཚེས་བརྒྱད་ལ་གནས་ནས་བྱུང་ནས་ཡན་ལག་བརྒྱད་དང་ལྡན་པའི་བསྙེན་གནས་ལ་ཉེ་བར་གནས་སོ་ཞེས་གང་གསུངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། དེ་ནི་དེ་དག་གིས་ལེགས་པར་སྤྱད་པ་ཙམ་ཡིན་གྱི་སྡོམ་པ་ནི་མ་ཡིན་ནོ། །

[Block 329]
དེ་ལྟ་བས་ན་སྡོམ་པ་ནི་ལྷ་དང་མི་རྣམས་ཁོ་ན་ལ་ཡོད་དོ། །

[Block 330]
དེ་ལ་ཡང་མི་རྣམས་ལ་གསུམ་མོ། །

[Block 331]
མི་རྣམས་ལ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ལ་སོགས་པ་ཐམས་ཅད་ཡོད་དོ། །

[Block 332]
འདོད་དང་གཟུགས་སྐྱེས་ལྷ་རྣམས་ལ། །བསམ་གཏན་སྐྱེས་ཡོད། བསམ་གཏན་གྱི་སྡོམ་པ་ནི་འདོད་པ་དང༌[^246]གཟུགས་ཀྱི་ཁམས་སུ་སྐྱེས་པའི་ལྷ༌[^247]རྣམས་ལ་ཡོད་ཀྱི་གོང་ན་ནི་མེད་དོ། །

[Block 333]
ཟག་མེད་ནི།

[Block 334 [VERSE]]
བསམ་གཏན་ཁྱད་པར་འདུ་ཤེས་མེད། །
སེམས་ཅན་མ་གཏོགས་གཟུགས་མེད་ནའང་། །

[Block 335]
ཟག་པ་མེད་པའི་སྡོམ་པ་ནི་འདོད་པའི་ཁམས་སུ་སྐྱེས་པ་རྣམས་ལ་ཡང་ཡོད༌[^248]ལ་བསམ་གཏན་ཁྱད་པར་ཅན་དང་འདུ་ཤེས་མེད་པའི་སེམས་ཅན་དུ་སྐྱེས་པ་རྣམས་མ་གཏོགས་པ་གཟུགས་མེད་པའི་ཁམས་སུ་སྐྱེས་པ་རྣམས་ལ་ཡང༌ཡོད་དེ། དེ་དག་གིས༌[^249]ནི་ལྡན་པའི་སྒོ་ནས་ཡོད་ཀྱི་མངོན་སུམ་དུ༌[^250]གྱུར་པ་ལས་ནི་མ་ཡིན་ནོ། །

[Block 336 [HEADING]]
### ལས་དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ། ^1-22-0

[Block 337]
ལས་བསྟན་པའི་དབང་དུ་བྱས་པ་ཡིན་པས་འདི་མན་ཆད་ནི་མདོ་ལས་བསྟན་པའི་ལས་རྣམས་བཤད་པར་བརྩམ་མོ། །

[Block 338]
ལས་ནི་གསུམ་སྟེ། ལས་དགེ་བ་དང་ལས༌[^251]མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་ཞེས་འབྱུང་བ་དེ་ལ།

[Block 339 [VERSE]]
ལས་བདེ་མི་བདེ་དང་གཞན་ནི། །
དགེ་དང་མི་དགེ་ནི༌[^252]གཞན་ཡིན། །

[Block 340]
འདི་ནི་དགེ་བ་ལ་སོགས་པའི་མཚན་ཉིད་ཡིན་ཏེ། ལས་བདེ་བ་ནི་དུས་རེ་ཞིག་དང་། གཏན་དུ་སྡུག་བསྔལ་ལས་ཡོངས་སུ་སྐྱོབ་པའི་ཕྱིར་དགེ་བ་ཡིན་ཏེ། འབྲས་བུ་ཡིད་དུ་འོང་བ་དང་མྱ་ངན་ལས་འདས་པ་འཐོབ་པར༌[^253]བྱེད་པ་ཡིན་ནོ། །

[Block 341]
མི་དགེ་བ་ནི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་མི་དགེ་བ་ཡིན་ཏེ། གང་གིས༌[^254]རྣམ་པར་སྨིན་པ་ཡིད་དུ་མི་འོང་བའོ། །

[Block 342]
དེ་ཉིད༌[^255]ལས་གཞན་པ་བདེ་བ་ཡང་མ་ཡིན་མི་བདེ་བ་ཡང་མ་ཡིན་པ་གང་ཡིན་པ་དེ་ནི་དགེ་བ་དང་མི་དགེ་བ་ལས་གཞན་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། ལུང་དུ་མ་བསྟན་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 343 [HEADING]]
### བསོད་ནམས་དང་བསོད་ནམས་མ་ཡིན་པ་དང་མི་གཡོ་བ། ^1-23-0

[Block 344]
ཡང་།

[Block 345 [VERSE]]
བསོད་ནམས་བསོད་ནམས་མིན་མི་གཡོ། །
བདེ་བ་མྱོང་འགྱུར་ལ་སོགས་གསུམ། །

[Block 346]
ལས་ནི་གསུམ་སྟེ། བསོད་ནམས་དང་། བསོད་ནམས་མ་ཡིན་པ་དང་། མི་གཡོ་བའོ། །

[Block 347]
ཡང་གསུམ་སྟེ། བདེ་བ་མྱོང་བར་འགྱུར་བའི་ལས་དང་། སྡུག་བསྔལ་མྱོང་བར་འགྱུར་བའི་ལས་དང་། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ༌[^256]ཡང་མ་ཡིན་པ་མྱོང་བར་འགྱུར་བའོ། །

[Block 348]
དེ་ལ་རེ་ཞིག །

[Block 349 [VERSE]]
བསོད་ནམས་འདོད་ཁམས༌[^257]དགེ་བའི་ལས། །
མི་གཡོ་གོང་མ་ལས་སྐྱེས་པའི། །

[Block 350]
དགེ་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ལས་དགེ་བ་ནི་མི་གཡོ་བ་ཡིན་ནོ། །

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
--- END BLOCKS ---
