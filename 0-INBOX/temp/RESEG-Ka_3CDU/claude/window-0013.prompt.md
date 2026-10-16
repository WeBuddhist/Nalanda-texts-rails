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
[Block 456 [HEADING]]
### བརྫུན་དུ་སྨྲ་བའི་ཕས་ཕམ་པ། ^5-4-0

[Block 457]
ཕས་ཕམ་པ་བཞི་པ་བརྫུན་གྱི་གླེང་གཞི་ནི། བཅོམ་ལྡན་འདས་ཡུལ་ཡངས་པ་ཅན་གྱི་སྤྲེའུ་རྫིང་གི་འགྲམ་ན་བཞུགས་སོ། །

[Block 458]
དེའི་ཚེ་མུ་གེ་ཆེན་པོ་བྱུང་ནས་ཁ་ཟས་ཀྱིས་ཤིན་ཏུ་བྲེལ་ཏེ༌[^350]ཕ་མ་ཡང་བུ་ལ་ཁ་ཟས་མི་སྟེར་བ་ཙམ་དུ་དཀོན་པའི་ཚེ། དགེ་སློང་རྫུ་འཕྲུལ་ཅན་དང་གནས་བརྟན་རྣམས་ནི་བྱང་གི་སྒྲ་མི་སྙན་ལ་སོགས་པ་ཡུལ་གཞན་འབྱོར་ཅིང་རྒྱས་པ་དག་ཏུ་དོང་ཞིང་བདག་ཉིད་ཀྱང་ཟ། གང་ཟག་གཞན་ལ་ཡང་སྟོབས་སོ། །

[Block 459]
དེ་ལ་ཉ་པ་ལས་རབ་ཏུ་བྱུང་བའི་དགེ་སློང་ལྔ་བརྒྱ་ལ་སོགས་པ་དག་གིས་ཀྱང་དགེ་སློང་དེ་དག་ལྟར་བྱ་ཞིང་དབྱར་ཚུལ་དུ་འཇུག་ཏུ་ནི་རྫུ་འཕྲུལ་ཡང་མ་ཐོབ་ཅིང་ཐོས་པ་དག་ཀྱང་ཉུང་ཞིང་དེ་ལྟར་མི་ནུས་ཀྱིས་བདག་ཅག་གིས་ཡུལ་ཉིད་དུ་དབྱར་ཚུལ་དུ་ཞུགས་ལ་བདག་ཅག༌[^351]སོ་སོའི་ཡོན་ཏན་བསྒྲགས་ཏེ་རྙེད་པ་བསྒྲུབ་པོ་སྙམ་ནས་ཚུལ་དུ་ཞུགས་སོ། །

[Block 460]
དེ་ནས་ལྔ་བརྒྱ་པོ་དེ་དག་གིས་གཅིག་གིས་གཅིག་གི་ཡོན་ཏན་བརྗོད་པ་ལ་ཞུགས་སོ། །

[Block 461]
འདིས་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ཐོབ་བོ། །

[Block 462]
འདིས་ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་ཐོབ་བོ། །

[Block 463]
འདིས་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ཐོབ་བོ། །

[Block 464]
འདིས་ནི་དགྲ་བཅོམ་པའི་འབྲས་བུ་ཐོབ་བོ། །

[Block 465]
འདིས༌[^352]ནི་འཇིག་རྟེན་པའི་ལམ་གྱིས་གྲུབ་བོ། །

[Block 466]
འདི་ནི་སྡེ་སྣོད་གསུམ་སྨྲ་བའོ་ཞེས་སོ་སོའི་ཡོན་ཏན་བརྗོད་པས་ཁ་ཟས་ལ་སོགས་པ༌[^353]མང་པོ་དུ་མ་རྙེད་དེ་ཤ་ཁྲག་གི་ལུས་ཤིན་ཏུ་རྟས་པས༌[^354]གནས་སོ། །

[Block 467]
དེ་ནས་དབྱར་འདས་ནས་ཚུལ་ནས་བྱུང་སྟེ། བཅོམ་ལྡན་འདས་ཀྱི་ཞབས་ལ་ཕྱག་འཚལ་དུ་ཕྱིན་ཏོ། །

[Block 468]
དང་པོར་ཀུན་དགའ་བོ་དང་ཕྲད་པ་དང་སྨྲས་པ། མུ་གེ་ཆེན་པོ་བྱུང་བའི་དུས་ན་དགེ་སློང་གཞན་རྣམས་ནི་རྨྱ་སྟེ་ལྷགས་ན། ཁྱོད་ནི་ཤིན་ཏུ་ཚོ་སྟེ་བྱུང་ན་དེ་ཅིའི་རྒྱུ་ཞེས་སྨྲས་པ་དང་། བདག་ཅག་སོ་སོའི་ཡོན་ཏན་བརྗོད་པས་རྙེད་པ་མང་པོ་བྱུང་སྟེ་ལུས་རྟས་སོ་ཞེས་སྨྲས་སོ། །

[Block 469]
ཁྱེད་ལ་ཡོན་ཏན་ཡོད་དེ་བརྗོད་དམ་མེད་དེ་བརྗོད། བདག་ཅག་ལ་ཡོན་ཏན་མེད་པར་བརྗོད་དོ་ཞེས་སྨྲས་པ་དང་། ཟང་ཟིང་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་མིའི་ཆོས་ལས་བླ་མར་གྱུར་པ་མེད་པ་ལ་ཡོད་པ་གཞན་བཞིན་དུ་སྨྲ་བ་ཤིན་ཏུ་མི་རིགས་སོ་ཞེས་ཀུན་དགའ་བོ་ལ་སོགས་པ་རྣམས་ཀྱིས་སྨྲས་སོ། །

[Block 470]
དེ་ལྟར་གྱུར་པ་བཅོམ་ལྡན་འདས་ཀྱིས་གསན་ཏོ། །

[Block 471]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^355]རྣམ་པ་དུ་མས་སྨད་ནས་འདུལ་བ་ལ༌[^356]བསླབ་པའི་གནས་བཅས་སོ། །

[Block 472 [VERSE]]
ལྷ་དག་མཐོང་ཞེས་དེ་ཡི་སྒྲ། །
ཐོས་པར་གྱུར་དང་ཀུན་སྨྲ་དང་། །

[Block 473]
ཞེས་བྱ་བ་ལ། དགེ་སྦྱོང་གིས༌[^357]བདག་གིས༌[^358]ལྷ་མཐོང་ངོ་། །ལྷའི་སྒྲ་ཐོས་སོ། །

[Block 474]
ལྷ་རྣམས་དང་བདག་ཏུ་སྨྲ་ཞིང་ཀུན་དུ་སྨྲ་བར་བྱེད་དོ་ཞེས་ཟེར་ན་གསུམ་ཆར་ལ་ཡང་ཕམ་པ་རེ་རེར་འགྱུར་རོ། །

[Block 475 [VERSE]]
གང་ན་བདག་འདུག་ལྷ་འོང་ཞིང་། །
བདག་ཀྱང་དེ་ཡི་གནས་འགྲོ་དང་། །

[Block 476]
ཞེས་བྱ་བ་ལ། དགེ་སྦྱོང་གིས༌[^359]བདག་གང་ན་འདུག་པའི་གནས་སུ་ལྷ་དག་འོང་ངོ་། །བདག་ལྷ་གང་ན་གནས་པའི་གནས་དེ་དག་ཏུ་འགྲོའོ་ཞེ་ན༌[^360]ཡང་ཕམ་པ། ཇི་ལྟར་ལྷ་མཐོང་ཞིང་སྒྲ་ཐོས་ཟེར་བ་དང་། ལྷ་དང་སྨྲ་ཞིང་ཀུན་དུ་སྨྲའོ། །

[Block 477]
བདག་འདུག་པའི་གནས་སུ་འོང་ངོ་ཞེས་སྨྲའོ།[^361] །

[Block 478 [VERSE]]
དེ་བཞིན་དྲི་ཟ་གྲུལ་བུམ་ཀླུ། །
གནོད་སྦྱིན་ལྟོ་འཕྱེ་ཆེན་པོ་དང་། །
ཤ་ཟ་ཡི་དགས་མི་འམ་ཅི། །
མཐོང་ངོ་ཞེས་ལ་སོགས་སྨྲའམ། །

[Block 479]
ཞེས་བྱ་བ་རྣམས་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 480]
བསམ་གཏན་མངོན་ཤེས་ཚད་མེད་དང་།[^362] །

[Block 481 [VERSE]]
རྒྱུན་ཞུགས་ལ་སོགས་འབྲས་བུ་དང་། །
ལམ་ལ་རབ་ཏུ་ཞུགས་པའང་རུང་། །
བདག་གིས་ཐོབ་ཅེས་སྨྲས༌[^363]ན་ནི། །
དོན་རིག་པ་ལས་བརྫུན་པའི་ཚིག །

[Block 482]
ཅེས་བྱ་བ་ལ། དགེ་སྦྱོང་གི་འདུ་ཤེས་སྦས་ནས། གཟུགས་ཀྱི་ཁམས་ཀྱི་བསམ་གཏན་དང་པོ་ཐོབ་བོ་ཞེའམ།

[Block 483]
གཉིས་པ་ཐོབ་པོ་ཞེའམ།

[Block 484]
གསུམ་པ་དང་བཞི་པ་ཐོབ་བོ་ཞེས་སྨྲ་ན་ཡང་ཕམ་པ། དེ་བཞིན་དུ་མངོན་པར་ཤེས་པ་ལྔ་ལས་གང་ཡང་རུང་བ་ཞིག་ཐོབ་པོ་ཞེས་སྨྲ་ན་ཡང་ཕམ་པའོ། །

[Block 485]
ཡང་འདུ་ཤེས་སྦས་ནས་ཚད་མེད་པ་བཞི་གང་ཡང་རུང་བ་ཞིག་གྲུབ་པོ་ཞེས་ཟེར་བ་དང་། དགེ་སྦྱོང་གི་འདུ་ཤེས་སྦས་ནས་འབྲས་བུ་བཞི་ལས་བདག་གིས་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ཐོབ་བོ་ཞེའམ། ལན་ཅིག་ཕྱིར་འོང་བ་དང་། ཕྱིར་མི་འོང་བ་དང་། དགྲ་བཅོམ་པའི་འབྲས་བུ་ཐོབ་པོ་ཞེས་སྨྲས་ཏེ། གཞན་གྱིས༌[^364]དོན་གོ་བས་དོན་རིག་སྟེ་གོ་ན་བརྫུན༌[^365]གྱི་ཚིག་སྟེ་ཕམ་པར་འགྱུར་རོ། །

[Block 486]
ལམ་ལ་རབ་ཏུ་ཞུགས་པ་ནི་དགེ་སྦྱོང་གིས༌[^366]འདུ་ཤེས་སྦས་ཏེ་འཇིག་རྟེན་ལས་འདས་པའི་ལམ་བདག་གིས་ཐོབ་བོ་ཞེས་སྨྲས༌[^367]ན་ཕམ་པའོ། །

[Block 487]
འཇིག་རྟེན་པའི་ལམ་གྱི་ཞི་གནས་ཀྱི་མཚན་མ་འགའ་ཞིག་ལ་བརྟེན་ཏེ་འདོད་ཆགས་དང་གནོད་སེམས་ལ་མི་སྤྱོད་དོ་ཞེས་ཟེར་ན་སྦོམ་པོར་འགྱུར་རོ། །

[Block 488]
ཁྱད་པར་ཐོབ་པའི་བདག་ཉིད་ཅན། །མ་ཉམས་ཞེས་བྱ་བ་ལ། དགེ་སྦྱོང་བདག་གིས༌[^368]སེམས་མ་སྨྱོས་པ་ནད་ཀྱིས་གཟིར་བར་མ་གྱུར་ཏེ་རང་བཞིན་དུ་གནས། གོང་དུ་བསྟན་པའི་ཡོན་ཏན་ཁྱད་པར་ཅན་ཐོབ་ཅིང་མཐོང་ཞེས་སྨྲས༌[^369]ན་ཕས་ཕམ་པར་འགྱུར་གྱི། སེམས་སྨྱོས་པ་དང་ནད་ཀྱིས༌[^370]གཟིར་བ་རྣམས་ནི་ཕམ་པར་མི་འགྱུར་གྱི་སྦོམ་པོར་གཞག༌[^371]གོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 489]
ང་རྒྱལ་མེད་བཞིན་དུ། སྨྲས་ན་བརྟུལ༌[^372]ཞུགས་ཉམས་པར་འགྱུར། །ཞེས་བྱ་བ་ལ། སྔོན་དགེ་སྦྱོང་ཞིག་དགོན་པ་ན་གནས་པས་འཇིག་རྟེན་པའི་ལམ་གྱིས་ཉོན་མོངས་པ་བཅོམ་སྟེ། མི་འབྱུང་བར་བྱས་ནས་ཡུན་རིང་མོ་ཞིག་ལོན་པ་ན། ཉོན་མོངས་པ་མི་འབྱུང་བའི་གནས་རྣམས་ལ་བརྟགས་ན་ཉོན་མོངས་པ༌[^373]མི་སྐྱེ་བས་བདག་ཅག་གིས་ཉོན་མོངས་པ་སྤངས་སོ་ཞེས་བསམས་ཤིང༌[^374]བརྗོད་ནས་སླར་གྲོང་དུ་ལྷགས་པ་ལས་འཇིག་རྟེན་པའི་ལམ་གྱིས་ཉོན་མོངས་པ་རྩད་ནས་མ་ཕྱིན་པའི་ཕྱིར་ཉོན་མོངས་པ་སྐྱེ་བའི་ཡུལ་བུད་མེད་དང་དགྲ་ལ་སོགས་པ་མངོན་དུ་གྱུར་པ་དང་ཉོན་མོངས་པ་སླར་སྐྱེས་ནས་དགེ་སློང་དེ་དག་བདག་ཅག་གིས༌[^375]ཉོན་མོངས་པ་མ་སྤངས་པར་སྤངས་སོ་ཞེས་སྨྲས་ཏེ་མིའི་ཆོས་ལས་བླ་མར་གྱུར་པའི་ཕམ་པར་མ་གྱུར་གྲང་ཞེས་བཅོམ་ལྡན་འདས་ལ་ཞུས་པ་དང་། མངོན་པའི་ང་རྒྱལ་ཅན་དེ་ལྟ་བུ༌[^376]མ་གཏོགས་ཏེ་སླན་ཆད་དེ་ལྟ་བུའི་ཁྱད་པར་ཞིག་ཐོབ་ན་ཡང་སྨྲ་བར་མི་བྱའོ་ཞེས་གསུངས་པ་ལྟ་བུ་སྟེ། དེ་ལྟ་བུ་ནི་ཕམ་པར་མི་གཞག༌[^377]གོ། །

[Block 490]
དགེ་སྦྱོང་གིས་འདུ་ཤེས་སྦས་ཏེ། ལྷ་དང་ཀླུ་དང་གནོད་སྦྱིན་མཐོང་བ་དག་ཡོད་དོ་ཞེས་ནི་སྨྲ་ལ། བདག་ཉིད་ཡིན་ནོ་ཞེས་ནི་མི་སྨྲ་ན་སྦོམ་པོར་འགྱུར་རོ། །

[Block 491]
ཤ་ཟ་རྣམས་མཐོང་བ་ཡོད་དོ་ཞེས་སྨྲ་ལ། བདག་ཉིད་ཡིན་པར་མི་སྨྲ་ན་ནི་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 492]
དགོན་པ་ན་དགེ་སློང་དུ་གནས་པ་དེ་ལ་མི་མ་ཡིན་པ་རྣམས་ཀྱིས་གཙེས་པ་ལས་འཕགས་པ་རྣམས་ལ་མི་གཙེ་སྟེ་བདག་ལ་ཡང་མི་གཙེ་ཟེར་ན་ཕམ་པ། འཕགས་པ་རྣམས་ཀྱི་ཕྱིར་ཁྱིམ་བདག་རྣམས་སྟན་ཁྲ་བོ་འདིངས་ཏེ་བདག་གི་ཕྱིར་ཡང་ཁྱིམ་བདག་སྟན་ཁྲ་བོ་འདིངས་སོ་ཞེས་ཟེར་བ་ཡང་དོན་རིག་ན་ཕམ་པའོ། །

[Block 493]
ཁྱད་པར་ཐོབ་པ་མ་གཏོགས་པར་ཞེས་བྱ་བ་ལ་སོགས་པས་ཉེས་བྱས་སུ་འགྱུར་བ་བསྟན་ཏོ། །

[Block 494 [VERSE]]
དེ་ལས་གཞན་པའི་བརྫུན་ཚིག༌[^378]རྣམས། །
དེ་དག་ཐམས་ཅད་སྡིག་མང་འགྱུར། །

[Block 495]
ཞེས་བྱ་བ༌[^379]ནི་གོང་དུ་ཡོན་ཏན་ཁྱད་པར་ཅན་ཐོབ་བོ་ཞེས་བྱ་བ་ལས་མ་གཏོགས་པར་ཀུ་རེ་དང་ཀྱལ་ཀ་ལ་སོགས་པའི་ཕྱིར། བརྫུན་པའི༌[^380]ཚིག་སྨྲས་ན་སྡིག་པ་མང་དུ་འགྱུར་ཏེ་ཉེས་བྱས་ལྕི་བར་འགྱུར་རོ། །
--- END BLOCKS ---
