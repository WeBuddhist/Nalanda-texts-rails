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
འོ་ན་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་ཞེས་བྱ་བ་འདི་ཡང་ཆོས་དུ་དང་ལྡན་པ་ཡིན་ཞེ་ན།

[Block 317 [VERSE]]
ཤེས་རབ་ལ་བརྟེན་ཡེ་ཤེས་སྐྱེ། །
ཏིང་ངེ༌[^166]འཛིན་དམིགས་བདག་གིས་འཇུག །
བྱང་ཆུབ་སེམས་སྤྱོད་ཉེ་བའི་རྒྱུ། །

[Block 318]
ཞེས་པ་ཤེས་རབ་དམ་པ་བསྐྱེད་པ་ཉིད་དང་། ཡེ་ཤེས་དམ་པ་དང་། ཏིང་ངེ་འཛིན་དམ་པ་ལ་དམིགས་པ་ཉིད་དང་ཐབས་བདེན་པའི་རྣལ་འབྱོར་པ་བདག་ཉིད་ཀྱི་འཇུག་པ་དང་། ཞུ་བ་བྱང་ཆུབ་སེམས་ལ་སྤྱོད་པ་དང་། [^167]དེའང་ཉེ་བའི་རྒྱུར་འདུག་པ༌[^168]སྟེ། འདི་ལྟར་དྲུག་དང་ལྡན་པ་ཁོ་ན་ཡིན་ནོ་ཞེའོ། །

[Block 319]
འོ་ན་དེ་སྨོས་པས་ཅི་བྱེད་ན།

[Block 320 [VERSE]]
བུམ་པ་དང་ནི་གསང་བ་དང་། །
ཐོབ་བྱ་བཞི་པ་སེལ་བར་བྱེད། །

[Block 321]
ཅེས་པ་ཤེས་རབ་མ་མ་སྨོས་ན་ནི་ཕྱི་དང་ནང་གི་བུམ་པ་ལའང་ཐལ་བར་འགྱུར་ལ། ཏིང་ངེ་འཛིན་མ་སྨོས་ན་ནི་སོ་སོ་སྐྱེ་བོ་ལའང་ཐལ་བར་འགྱུར་རོ། །

[Block 322]
དེའང་བདག་ཉིད་ཀྱིས་འཇུག་པ་ཞེས་མ་སྨོས་ན། གསང་བ་ལའང་ཐལ་བར་འགྱུར་རོ། །

[Block 323]
བྱང་ཆུབ་སེམས་ལ་སྤྱོད་པ་མ་སྨོས་ན་བཞི་པ་དང་གཡོན་གྱི་ཡུམ་བསྐྱེད་པའི་རིམ་པ་ལའང་ཐལ་བར་འགྱུར་རོ། །

[Block 324]
ཉེ་བའི༌[^169]རྒྱུ་ཞེས་པ་མ་སྨོས་ན་འགྲུབ་པ་མ་ཡིན་པའི་ལོག་པར་རྟོག་པའང་ལྡོག་པར་མི་འགྱུར་རོ། །

[Block 325]
འོ་ན་དབང་གསུམ་པའི་རྒྱུ་གང་ཡིན་ཞེ་ན། ཤེས་རབ་ཏིང་འཛིན་དམིགས་པ་ཡིས།[^170] །བྱེ་བྲག་དང་བཅས་དེ་ཡི་རྒྱུ། །ཞེས་པ་བཤད་ཟིན་ཏོ། །

[Block 326]
འོ་ན་དུས་གང་གི་ཚེ་བསྐུར༌[^171]ཞེ་ན།

[Block 327 [VERSE]]
དབང་གཉིས་རྫོགས་དང་གང་མ༌[^172]རྣམས། །
གསུམ་པའི་དབང་གིས་དུས་ཞེས་བཤད། །

[Block 328]
ཅེས་པ་དང་པོར་བུམ་པའི་དབང་ཐོབ་པའི་སྟེང་ལ༌[^173]ཕྱི་ནས་གསང་བའི་དབང་ཐོབ་པ་བླ་མ་གཉིས་ཀྱིས༌[^174]གནང་བ་དང་། བྱང་ཆུབ་སེམས་གཉིས༌[^175]རྒྱས་པ་དང་། མཆོག་འདོད་པའི་དུས་ནའོ། །

[Block 329]
གསུམ་པའི་གླེང་གཞིའང་གང་ཞེ་ན།

[Block 330 [VERSE]]
རྒྱལ་བ་ཡུམ་དང་མཉམ་སྦྱར༌[^176]ཚེ། །
འཁོར་རྣམས་དུས་སོགས་གླེང་གཞི་ཡིན། །

[Block 331]
ཞེས་གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་དུ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཡུམ་དང་གཉིས་སུ་མེད་པར་སྙོམས་པར་ཞུགས་པ་དང་གཉིས་སུ་མེད་པའི་བདེ་བ་ཆེན་པོ་རྒྱས་པར་གྱུར་པ་གང་ཡིན་པ་དེའི་དུས་སུ། འཁོར་ན་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དང་ཉན་ཐོས་འདོད་ཆགས་དང་བྲལ་བ་ཐམས་ཅད་གསང་བའི་སྤྱོད་པའི་ཚུལ་དེ་མཐོང་ནས་དངངས་པ༌[^177]དང་། ངུས་པ་དང་། བརྒྱལ་བ་དང་། དེ་ལས་བསླང་བ་ལ་སོགས་པའི་སྦྱོར་བ་འདི་ནི་གསུམ་པའི་དབང་གི་གླེང་གཞི་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 332 [VERSE]]
དེའང་གནས་གང་དུ་བསྐུར་ཞེ་ན། །
ས་ཕུག་རིམ་པ་གསུམ་པའམ། །
པདྨའི་ནང་དུ་བསྐུར་བ་ཡིན། །

[Block 333]
ཞེས་པ་ས་ཕུག་རིམ་པ་གསུམ་པ་ནི་ཕྱི་སྟེ་ཐུན་མོང་གི་གནས་སོ། །

[Block 334]
དེའི་ཁྱད་པར་གྱི༌[^178]གནས་ནི་ཤེས་རབ་མའི་པདྨའི་ནང་དུ་བསྐུར་བ་འདི་ནི་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་གནས་སོ། །

[Block 335]
སློབ་དཔོན་ཡང་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། །བླ་མ་རིག་མ་དམ་པ་སྟེ། །ཞེས་གང་རིག་མ་དམ་པ་དེ་ནི་ཡང་དག་པའི་བླ་མ་སྟེ་མཆོག་སྟེར་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 336 [VERSE]]
ཡང་ན་རང་སེམས་བྱང་ཆུབ་སེམས། །
ཐབས་ཀྱི་རྡོ་རྗེ་གསང་བའི་རྩ། །
ཐོས་པ་ཀུན་གོམས་ཡོན་ཏན་ལྡན། །

[Block 337]
ཞེས་པ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པའོ། །

[Block 338 [VERSE]]
དེས་སློབ་མ་གང་ལ་བསྐུར་ཞེ་ན། །
དབང་གཉིས་རྫོགས་ཤིང་ཡོན་ཏན་ལྡན། །
དེ་ལ་མཁས་པས་གསུམ་པ་སྦྱིན། །

[Block 339]
ཞེས་པ་ནི་གོ་སླའོ། །

[Block 340]
འོ་ན་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་རྒྱུའང་གང་ཞིག་ཡིན་ཞེ་ན། །ཤེས་རབ་ཏིང༌[^179]འཛིན་འདི༌[^180]ཁོ་ན། །ཞེས༌[^181]བཤད་ཟིན་ཏོ། །

[Block 341]
དེའི་འང་དུས་གང་ཞིག་ཡིན་ཞེ་ན། སློབ་དཔོན་ཡོན་ཏན་ལྡན་པས་གནང་། །བླ་མ་དང་མཐུན་ཁུ་བ་འབབ། ཅེས་པ། གང་ཞིག་ཤེས་རབ་ཡེ་ཤེས་ཀྱི་དབང་ཐོབ་པར་འདོད་པས་དང་པོར་དེའི་སྦྱོར་བ་བཤད་ཟིན་ཏོ། །

[Block 342]
དེའི་རྫས་གང་ཞིག་ཡིན་ཞེ་ན། དཀར་དམར་བྱང་ཆུབ་སེམས་དག་དང་། ཏིང་འཛིན་སྦྱོར་བ༌[^182]བསྐྱེད་ཕྱིར་རྒྱུ། །ཞེས་པ་གང་གིས་གང་ལ་ཕན་པ་ཡོད་པ་དེ་ནི་རྫས་ཏེ། བྱང་ཆུབ་སེམས་དཀར་དམར་དང་མ༌[^183]མཆུའི་རོ་མྱོང༌[^184]བ་ལ་སོགས་པ་འདི་ཡང་ངོ་། །འདིའི་རིམ་པ་ཡང་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 343 [VERSE]]
དཀར་དམར་སྤེལ་དང་འཁྲུ་བ་དང་། །
དངོས་པོ་འབྱུང་དང་མི་འགྱུར་ཞིང་། །
རེག་པར་བྱེད་དང་གང་ཞིག་བསྟབས། །
འདི་ཡི་སྦྱོར་བས་འབྱུང་བ་ཡིན། །

[Block 344]
ཞེས་པ་དཀར་དམར་སྤེལ་བ་ནི་ཕྲེང་བའི་དབང་ངོ་། །འཁྲུ་བ་ནི་བྱང་ཆུབ་སེམས་ཀྱི༌[^185]ཆུའི་དབང་ངོ་། །ལྟེ་བ་ལ་རེག་པ་ནི་དབུ་རྒྱན་གྱི་དབང་ངོ་། །གཞན་འཇོམས་པ་ནི༌[^186]རྡོ་རྗེའི་དབང་ངོ་། །གང་ཞིག་ཁ་གོང་མ༌[^187]ལ་སྒྲ་འབྱུང་བ་ནི་མིང་གིའོ། །

[Block 345]
འོག་གི་སྒྲ་ནི་དྲིལ་བུའོ། །

[Block 346]
ཡང་ན་ཧཱུཾ་གི་སྒྲ་ནི་དྲིལ་བུའོ། །

[Block 347]
ཧ་ཧ་ཞེས་པ་ནི་མིང་གི་དབང་དུ་ཤེས་པར་བྱའོ། །

[Block 348]
དེའི་ཐབས་ཀྱང་གང་ཡིན་ཞེ་ན།

[Block 349 [VERSE]]
དབབ་དང་བཟློག་དང་རོལ་མོའི་ཚོགས། །
འདི་ནི་ཐབས་ཀྱི་དམ་པར་འདོད། །

[Block 350]
ཅེས་པ་བསྐྱོད་པའི་སྟོབས་ཀྱིས་དབབ་པ་དང་རླུང་གི་སྦྱོར་བས་བཟློག་པ་ལ་སོགས་པ་འདི་དང་གཞན་ཡང་རོལ་མོ་དང་། པི་ཝང་ལ་སོགས་པའི་སྦྱོར་བ་འདི་ཡང་ཐབས་ཀྱི་དམ་པའོ། །

[Block 351]
དཀྱིལ་འཁོར་ཡང་གང་དུ་ཞེ་ན།

[Block 352 [VERSE]]
དཀྱིལ་འཁོར་ལུས་དང་བྷ་གར་སྦྱོར། །
རྒྱལ་བའི་ཡུམ་གྱི་ཚུལ་འཆང་བའོ། །

[Block 353]
ཞེས་པ་དཀྱིལ་འཁོར་ལུས་སུ་བྱས་པ་ནི། །གསང་བའི་དབང་བཞིན་ནོ། །

[Block 354]
བྷ་ག་ལ་ནི་རྩ་དང་བྱང་ཆུབ་སེམས་རྟེན་དང་བརྟེན་པའི་ཚུལ་དུ་དཀྱིལ་འཁོར་རོ། །

[Block 355]
དེར་འཇུག་པའི་རིམ་པ་ཡང་།
--- END BLOCKS ---
