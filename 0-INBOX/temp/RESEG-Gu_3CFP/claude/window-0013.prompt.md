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
གཉིས་དག་གམ་ཤེས་པ་རྣམ་པ་གསུམ་ཡང་རུང་སྟེ། ཉོན་མོངས་པའི་སྒྲིབ་པ་རྣམ་པར་དག་པའི་ཤེས་པའི་སྤྱོད་ཡུལ་ནི་དེ་ཁོ་ན་ཉིད་ཅེས་བརྗོད་དོ་ཞེས་བྱ་བའོ། །

[Block 457]
རབ་ཏུ་རྣམ་པར་འབྱེད་པ་ཞེས་བྱ་བ་ནི་ཟག་པ་མེད་པ་ཐོབ་པར༌[^292]བྱེད་པའི་ཤེས་པ༌[^293]གོང་དུ་བསྟན་པ་དེས་སོ། །

[Block 458]
མངོན་པར་རྟོགས་པར་འགྱུར་བ་དང་ཞེས་བྱ་བ་ནི། ཟག་པ་མེད་པའི་ཤེས་པ་སྟེ། གང་མངོན་པར་རྟོགས་པའི་ཤེས་པའོ། །

[Block 459]
མངོན་པར་རྟོགས་པར་འགྱུར་བའི་ཤེས་པ་ཞེས་བྱ་བ་ནི། གང་ཟག་པ༌[^294]མེད་པའི་རྗེས་ལས་ཐོབ་པའི་ཤེས་པའོ། །ཤེས་བྱ་ལ་ཤེས་པའི་གེགས་བྱེད་པ་ཞེས་བྱ་བ་ལ། ཤེས་བྱ་ལ་ཤེས་པའི་གེགས་བྱེད་ཅིང་གང་དང་ལྡན་པས་ཤེས་པར་བྱ་བ་མི་ཤེས་པ་དེ་ནི་ཤེས་བྱའི་སྒྲིབ་པ་ཞེས་བརྗོད་དེ། [^295]བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཆོས་བདག་མེད་པའི་རྗེས་ལ་འཇུག་པ་དང་། སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ཆོས་བདག་མེད་པ་ལ་རབ་ཏུ་ཞུགས་པའི་ཡེ་ཤེས་ཤིན་ཏུ་རྣམ་པར་དག་པ་སྟེ།[^296] བརྟགས་པ་བརྗོད་པའི་ངོ་བོ་ཉིད་ཀྱིས་རྣམ་པར་མི་རྟོག་པ་ནི་དེ་ལ་རྟོག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 460]
དེ་ལྟར་བརྟགས་པ༌[^297]བརྗོད་པའི་ངོ་བོ་ཉིད་རྣམ་པར་མི་རྟོག་པ་གཉིས་པོ་དེས་ཤེས་བྱ༌[^298]དང་། ཤེས་པ་ནི་མཉམ་པས་མཉམ་པའི་ཡེ་ཤེས་དེའི་སྤྱོད་ཡུལ་ཏེ། ཡེ་ཤེས་དེའི་ཤེས་པར་བྱ་བའི་ཡུལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 461]
ལྡོག་པར་འགྱུར་བ་སྟེ། རབ་ཏུ་ལྡོག་པར་འགྱུར་བའོ། །

[Block 462]
འདའ་བར་མི་འགྱུར་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་འདའ་བར་མི་འགྱུར་བའོ། །

[Block 463]
འཇིག་རྟེན་གྱི་མངོན་པར་ཞེན་པར་བྱས་ཞེས་བྱ་བ་ནི། མངོན་པར་ཞེན་པས་བཟུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 464]
རྣམ་པར་རྟོག་པ་དང་སྤྲོས་པ་ཐམས་ཅད་ཀྱི་རྩ་བས༌[^299]ཞེས་བྱ་བ་ལ། རྣམ་པར་རྟོག་པ་ཐམས་ཅད་ནི་འཆད་པར་འགྱུར་བ་རྣམ་པ་བརྒྱད་དེ། རྟོག་པ༌[^300]དང་། མི་རྟག་པ་ལ་སོགས་པ་དག་གི༌[^301]རྣམ་པའི་རྣམ་པར་རྟོག་པས་རྣམ་པར་བརྟགས་པའི༌[^302]ཐ་སྙད་དོ། །

[Block 465]
སྤྲོས་པ་ནི་གཟུགས་ལ་སོགས་པ་ཕུང་པོ་ལྔ་དང་། དབང་པོ་དྲུག་དང་། འབྱུང་བ་ཆེན་པོ་བཞི་དང་། འབྱུང་བ་ཆེན་པོ་ལས་བྱུང་བའི་གཟུགས་ཞེས་བྱ་བ་སྟེ་ཐམས་ཅད་ཀྱང་ངོ་བོ་ཉིད་ཀྱི༌[^303]རྣམ་པར་རྟོག་པའོ། །

[Block 466]
དགེ་བ་ལ་སོགས་པ་ཞེས་བྱ་བ་ནི། ཁྱད་པར་གྱི་རྣམ་པར་རྟོག་པ་སྟེ། དགེ་བ་དང་། མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པའི་ཁྱད་པར་དུ་རྣམ་པར་རྟོག་པའི་ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བ་དང་། གཉི་ག་མ་ཡིན་པ་ཉིད་དང་། འདུས་བྱས་ཀྱི་མཚན་ཉིད་དོ། །

[Block 467]
སྐྱེ་བ་ལ་སོགས་པ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་བྱ་བ་ནི། འཇུག་པ་དང་ལྡོག་པ་ཉིད་དོ། །

[Block 468]
འདས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དུས་ཉིད་དུའོ། །

[Block 469]
འདུས་བྱས་དང་འདུས་མ་བྱས་ཞེས༌[^304]བྱ་བའི༌[^305]རྐྱེན་ལས་བྱུང་བ་དང་མ་བྱུང་བ་ཉིད་དོ། །

[Block 470]
འཇིག་རྟེན་འདི་དང་འཇིག་རྟེན་ཕ་རོལ་ཞེས་བྱ་བ་ནི། མཐོང་བའི་ཆོས་དང་ཕྱི་མའི་བྱེ་བྲག་གོ། །

[Block 471]
ཉི་མ་དང་ཟླ་བ་འདི་གཉིས་ཞེས་བྱ་བ་ནི། མཚན་མོ་དང་ཉིན་པར་གྱི་བྱེ་བྲག་གི་ཁྱད་པར་དུ་བྱས་པ་ཉིད་དེ། ཐ་སྙད་རྣམ་པ་བརྒྱད་ཀྱི་ཁྱད་པར་ཉིད་དོ། །

[Block 472]
མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བའི་བར་དུ་ཞེས་བྱ་བ་ནི། རྣམ་པར་གྲོལ་བ་ཉིད་དོ། །

[Block 473]
ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་མེད་པ་ཞེས་བྱ་བ་ནི། བརྗོད་དུ་མེད་པའི་ངོ་བོ་ཡིན་པས་འཇིག་རྟེན་ལས་འདས་པའི་ཡེ་ཤེས་ཡིན་ན་ཡང་ངོ་། །དངོས་པོ་ཙམ་མམ། དེ་བཞིན་ཉིད་ཙམ་དུ་འཛིན་པ་ཞེས་བྱ་བས་ནི་བཏགས་པ༌[^306]བརྗོད་པའི་རྫས་མེད་པ་དང་། མཚན་མ་མེད་པ་ཉིད་དག་འགེགས་པར༌[^307]བྱེད་དོ། །

[Block 474]
ཇི་ལྟ་བུར་ཡང་རྣམ་པར་རྟོག་པར་མི་བྱེད་དོ་ཞེས་བྱ་བ་ནི། རྫས་ཙམ་མམ་འདི་ལྟ་བུའི་དེ་བཞིན་ཉིད་ཙམ་ཞེས་བྱ་བའི་ངོ་བོར་གང་བཏགས་པ༌[^308]བརྗོད་པའི་རང་བཞིན་དུ་རྣམ་པར་གཞག་པ་དེ་འགོག་པར་བྱེད་དོ། །

[Block 475]
དེ་བཞིན་ཉིད་དེ་དང་མཚུངས་པ༌[^309]མཉམ་པར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་རབ་ཀྱིས་མཐོང་སྟེ་ཞེས་བྱ་བ་ནི། བརྗོད་དུ་མེད་པའི་ངོ་བོར་ཁྱད་པར༌[^310]མེད་དེ། ཀུན་ཏུ་བརྟགས་པའི་དངོས་པོའི་ངོ་བོ་མེད་པ་ཉིད་དོ། །

[Block 476]
སེམས་སྙོམས་པས་མཉམ་པ་ཉིད་ཀྱི་བཏང་སྙོམས་རབ་ཏུ་འཐོབ་པ་སྟེ། ཐམས་ཅད་ཁྱད་པར་མེད་པ་ཉིད་དོ། །

[Block 477]
ཁྱད་པར་ཡོད་ན་ནི་དངོས་པོ་རྣམས་མི༌[^311]མཉམ་པར་མཐོང་བར་འགྱུར་རོ། །

[Block 478]
དེ་ལྟར་ཕན་པ༌[^312]མང་པོ་དང་ལྡན་པ་ནི་བདག་ཉིད་ཀྱང་སངས་རྒྱས་ཀྱི་ཆོས་ཡོངས་སུ་སྨིན་པར་བྱ་བ་དང་། གཞན་དག་ཀྱང་ཐེག་པ་གསུམ་གྱི་ཆོས་ལ་ཡོངས་སུ་སྨིན་པར་བྱ་བའི་ཕྱིར་ཡང་དག་པར་རབ་ཏུ་ཞུགས་པ་ཡིན་ཏེ། བདག་ཉིད་ཀྱི་སངས་རྒྱས་ཀྱི་ཆོས་ཡོངས་སུ་སྨིན་པར་བྱ་བའི་ཕྱིར་ནི། ལོངས་སྤྱོད་རྣམས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནས་བརྩམས་པ་སྟེ། བདག་ཉིད་ཀྱི་སངས་རྒྱས་ཀྱི་ཆོས༌[^313]ཡོངས་སུ་སྨིན་པ་ཡིན་ནོ། །

[Block 479]
སེམས་ཅན་ནི་རྣམ་པ་བཞི་སྟེ། ཡོན་ཏན་དང་ལྡན་པ་དང་། སྐྱོན་དང་ལྡན་པ་དང་། བདག་ལ་གནོད་པ་བྱེད་པ་དང་། ཕན་པ་བྱེད་པ་ཞེས་བྱ་བ་སྟེ། དེ་དག་ལ་ཇི་ལྟར་འོས་པར་སྒྲུབ་པ་ནི་ཡང་དག་པར༌[^314]སྦྱོར་བ་ཡིན་ནོ། །

[Block 480]
ངོ་བོ་ཉིད་ཀྱང་མ་ཡིན་ལ་ཞེས་བྱ་བ་ནས། དངོས་པོ་གཅིག་པུ་ལ་མང་པོ་དག་གིས་ཞེས་བྱ་བ་ནི་གང་བརྗོད་པར་བྱ་བའོ།[^315] །དེ་ལས་གཞན་པ་ཞེས་བྱ་བ་ནི་གཟུགས་ལ་སོགས་པ་དག་ལས་གཞན་པའོ། །

[Block 481]
ཆོས་གང་དག་དང་དངོས་པོ་གང་དག་ལ་ཞེས་བྱ་བ་ནི། ཆོས་ནི་གཟུགས་མེད་པ། དངོས་པོ་ནི་གཟུགས་ཅན་ནོ། །

[Block 482]
ཡང་ན་ཆོས་དེ་དག་ཅེས་བྱ་བ་ནི། ཆོས་ནི་མང་པོ་འདུས་པའི་བརྗོད་པ་དང་སྦྱར་རོ།[^316] །དངོས་པོ་རེ་རེ་ལ་ཡང་རྣམ་པ་སྣ་ཚོགས་ཞེས་བྱ་བ་ནི་རྣམ་པའི་བྱེ་བྲག་གོ། །

[Block 483]
མང་པོར་ཞེས་བྱ་བ་དང་། རྣམ་པ་སྣ་ཚོགས་མང་པོ་ཞེས་བྱ་བ་ནི། གང་བརྗོད་པ་དང་སྦྱར་རོ། །

[Block 484]
བཏགས་ཏེ་ཞེས་བྱ་བ་ནི། གང་བརྗོད་པ༌[^317]ཉེ་བར་འདོགས་པ་ཞེས་བྱ་བ་སྟེ།[^318] དེ་ནི་དེ་ལྟར་གཞན་དང་གཞན་པའི་ཐ་སྙད་དོ། །

[Block 485]
དེ་ལྟ་ན་ཡང་བཏགས་པའི་ཚིག་རྣམ་པ་སྣ་ཚོགས་མང་པོ་དག༌[^319]རྣམས་དང་སྦྱར་རོ།[^320] །གལ་ཏེ་ངེས་པ་ཉེ་བར་དམིགས་པར་འགྱུར་བ་དེ་ལྟ་ན་ཡང་ཆོས་དེ་དག་རྣམས་དངོས་པོའི་བདག་ཉིད་དུ་འགྱུར་ན་ནི༌[^321]དམིགས་པ་ཡང་མེད་དོ། །

[Block 486]
གཟུགས་ཀྱི་བདག་ཉིད་ལ་བཏགས་པའི་ཞེས་བྱ་བ་ནི། གཟུགས་ཞེས་བཏགས་པའི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །ཇི་ལྟར་བཏགས་ནས་ཤེ་ན། སྨྲས་པ། བཏགས་པའི་ཚིག་གིས་བསྡུས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 487]
དེ་ལྟ་ན་ནི་ཞེས་བྱ་བ་ནི། སྔ་མ་བཞིན་དུ་བཏགས་པའི་བརྗོད་པས་ཉེ་བར་བཏགས་པས་གཟུགས་ཀྱི་བདག་ཉིད་ཅན་གྱི་དངོས་པོར་གྱུར་པ་དེ་ལྟ་ནའོ། །

[Block 488]
གཟུགས་ཀྱི་བློ་འཇུག་པར་འགྱུར་ཞེས་བྱ་བ་ནི་སྔོན་དུ་བཏགས་པ་ལས་སོ། །

[Block 489]
བཏགས་པའི་ཚིག་མེད་པར་ནི་མ་ཡིན་ཏེ། དེའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 490]
གཟུགས་ལ་སོགས་པའི་ཆོས་རྣམས་ཞེས༌[^322]བྱ་བ་ནི། ལྐོག་ཏུ་གྱུར་པའི་ཆོས་རྣམས་སོ། །

[Block 491]
གཟུགས་ལ་སོགས་པའི་དངོས་པོ་ཞེས་བྱ་བ་ནི། མངོན་སུམ་ཉིད༌[^323]དུ་དམིགས་པའོ། །

[Block 492]
ཡོད་པ་མ་ཡིན་པ་ལ་སྒྲོ་འདོགས་པའི་ཉེས་པ་ཇི་སྙེད་པ་དེ་དག་ནི་ཐོག་མ་ཉིད་དུ་དཔྱད་ཅིང་གསལ་བར་བྱས་ལ་དཀྲོལ༌[^324]ཞིང་བསྟན་ཟིན་ཞེས་བྱ་བ་ནི། དུ་མའི་བདག་ཉིད་དུ་ཇི་ལྟར་འགྱུར་ཏེ། བརྗོད་པའི་སྔ་རོལ་ན་ནི་བདག་མེད་ནའོ། །

[Block 493]
དེ་ལས་བརྗོད་པར་ཇི་ལྟར་འབྱུང་སྟེ། རེ་ཞིག་སྔ་རོལ་ན་ནི་བློ་མེད་དེ། བཏགས་པ་ལ་གནས་པའི་དངོས་པོ་ཙམ་གྱི་ངོ་བོ་མེད་པས་བཏགས་པ་དེ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་མེད་ན། བཏགས་པ་ཡང་ཡོད་དམ་མེད་པ་ཞིག་ཅེ་ན། བཏགས་པ་ཡོད་པ་ཉིད་ན་ནི་བཏགས་པ་ཙམ་གྱི་དངོས་པོར་ཡོད་དོ་ཞེས་སྦྱར་བར་མི་བྱ་སྟེ། དེ༌[^325]ཡོད་པའི་ཕྱིར་རོ། །

[Block 494]
ཡང་ན་བཏགས་པར་ཡོད་པ་དེ་ཡང་མེད་དོ་ཞེས་བྱ༌[^326]ཟེར་ན་ནི་དེ་ཁོ་ན་ཉིད་དང་བཏགས་པ་ཙམ་ལ༌[^327]ཡང་སྐུར་པ་བཏབ་པར་འགྱུར་རོ། །

[Block 495]
བཏགས་པ་དང་དེ་ཁོ་ན་ཉིད་ལ་སྐུར་པ་འདེབས་པ་དེ༌[^328]ནི།
--- END BLOCKS ---
