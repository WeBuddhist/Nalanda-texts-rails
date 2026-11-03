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
དེ་བས་ན་དབྲོག་པ་མ་ཡིན་ནོ། །

[Block 457]
བཀོལ་བ་བྲན་ནོ་ཞེས་བྱ་བ་ནི་བཀོལ་བ་ཞེས་བྱ་བའི་མིང་འདིས་ཁྱོད་བྲན་མ་ཡིན་ནམ་ཞེས་བྱ་བ་ལ་སོགས་པའི་མིང་ཅན་བྲན་དང་འབྲེལ་བ་ལ་སོ་སོར་ཉེ་བར་གཞག་པའོ། །

[Block 458]
དེ་བས་ན་མིང་བསྟན་པ་འདི་ལ་གང་ཞིག་ལྡན་པ་ཁས་ལེན་པར་བྱེད་པ་དེ་དོན་ཇི་ལྟར་ཡོངས་སུ་གྱུར་ཀྱང་གནས་ཇི་ལྟ་བར་ཡང་དག་པར་གནས་པ་ཡིན་ནོ། །

[Block 459]
འདིར་ནི་ངག་ཀྱང་འདི་བསྐྱེད་པ༌[^318]ཡིན་ཏེ། ཁྱོད་ནི་བྲན་མ་ཡིན་ནམ་ཞེས་བྱ་བར༌[^319]རབ་ཏུ་འབྱུང་བའི༌[^320]དོན་དུ་ཉེ་བར་འོངས་པ་ལ་དྲི་བར་བྱའོ། །

[Block 460]
བསྙེན་པར་རྫོགས་པར་བྱེད་པ་རྣམས་ཀྱང་བྲན་ལས་རབ་ཏུ་དབྱུང་བ་མ་ཡིན་པ་དང་བསྙེན་པར་རྫོགས་པར་བྱ་བ་མ་ཡིན་པ་ཞེས་བྱ་བའོ། །

[Block 461]
ཡིན་ནམ་བཏང་ལ་ཁྱོད་ལ་ལ་ལའི་བུ་ལོན་མང་ཡང་རུང་ཉུང་ཡང་རུང་ཅུང་ཟད་ཆགས་པ་མེད་དམ་ཞེས་བྱ་བ་ཁྱོད་རྣམ་པར་བཏང་བ་ནི་ཡིན་ནམ་ཞེས་བྱ་བ༌[^321]བཏང་སྟེ། ཁྱོད་ཀྱི་སྒྲ་དང་བྲལ་བ༌[^322]ནི་བཀོལ་བ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 462]
ཁྱོད་ཅེས་བྱ་བའི་གནས་འདི་ལ་ཁྱོད་ལ་ཞེས་བྱ་བ་བརྗོད་པར་བྱ་སྟེ། དེ་བས་ན་ངག་ནི་འདི་ཡིན་ཏེ། ཁྱོད་ལ་ལ་ལའི་བུ་ལོན་མང་ཡང་རུང་ཉུང་ཡང་རུང་ཅུང་ཟད་ཆགས་པ་མེད་དམ་ཞེས་བྱ་བ་རབ་ཏུ་འབྱུང་བའི༌[^323]དོན་དུ་ཉེ་བར་འོངས་པ་ལ་དྲི་བར་བྱའོ། །

[Block 463]
བསྙེན་པར་རྫོགས་པར་བྱེད་པ་པོ་རྣམས་ཀྱང་བུ་ལོན་ཆགས་པ་དང་ལྡན་པ་རབ་ཏུ་དབྱུང་བར་མི་བྱ། བསྙེན་པར་རྫོགས་པར་མི་བྱ་ཞེས་བྱ་བའི་སྔགས་ཀྱིས་སོ། །

[Block 464]
འདིའི་སྔགས་ལས་རབ་ཏུ་དབྱུང་དུ་བཅུག་ནས་བསྙེན་པར་རྫོགས་པར་བྱ་སྟེ། སྦྱིན་པར་ནུས་པར་འགྱུར་བ་སོ་སོར་ཤེས་པར་བྱ་ཞིང་བུ་ལོན་ཆགས་པ་མ་གཏོགས་པར་ཞེས་བྱ་བའི་གྲངས་བྱེ་བྲག་སོ་སོར་བསྒྲུབ་པར་བྱའོ། །

[Block 465]
རབ་ཏུ་འབྱུང་བར༌[^324]འདོད་པ་ཕ་མ་གསོན་ཞིང་དེ་གཉིས་ཀྱིས་མ་གནང་བ་ཡུལ་ཐག་མི་རིང་བ་ནི་ཞག་བདུན་བསྲེལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཕ་མ་དག་གསོན་བཞིན་པ་དང་གང་ལ་ཡོད་པ་དེ་ནི་ཕ་མ་གསོན་བཞིན་པ་ཅན་ནོ། །

[Block 466]
དེ་གཉིས་ཀྱིས་མ་གནང་བ་ཞེས་བྱ་བ་ནི་ཕ་མ་དག་ལས་སོ། །

[Block 467]
དེ་གཉིས་ཀྱི་སྒྲས་ནི་ཕ་མ་དག་འདིར་ཕ་མའི་སྒྲ་ཞེས་བྱ་བས་ཤེས་པར་བྱའོ། །

[Block 468]
དེ་ཡུལ་ཐག་རིང་ན་ཡང་དགེ་འདུན་ལ་མ་ཞུས་པར་རབ་ཏུ་དབྱུང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་ཕ་མ་གསོན་བཞིན་པས་མ༌[^325]གནང་བའོ། །

[Block 469]
དེ་གཉིས་ཀྱི་ནང་ནས་ཕ་མ་གསོན་བཞིན་ཕ་མ་ཡིན་པའམ་ཕ་མ་དག་གིས་གནང་བ་མ་ཞུས་པ་ཡང་སྐྱོན་དང་བྲལ་བ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 470]
དེ་ལྟར༌[^326]ན་ཡང་ཕ་མ་གསོན་བཞིན་པ་ལ་དྲི་བའི་ཀློག་པ་སྟེ། བཙུན་པ་རེ་ཞིག་གང་ལ་ཕ་མ་དག་དུས་འདས་པར་གྱུར་པའམ། དུད་འགྲོའི་སྐྱེ་གནས་སུ་གྱུར་པ་ནི་དེ་སྐྲ་བྲེག་པའི་ཕྱིར་དགེ་འདུན་ཐམས་ཅད་ལ་ཞུ་བར་བགྱི་འམ། ཉེ་བ་འཁོར་མི་བྱའོ་ཞེས་གསུངས་པའོ། །

[Block 471]
ཡུལ་ཐག་རིང་པོའི་ཚིག་ནི་ཅིའི་དོན་དུ་བྱས་ཤེ་ན། གང་གི་ཕྱིར་ཁྱིམ་བདག་གི་ཆུང་མ་འགའ་ཞིག༌[^327]གི༌[^328]བུ་རབ་ཏུ་བྱུང་བ༌[^329]ལ་འོངས་ཏེ་སྨྲས་པ། ཁྱོད་ནི་ཤཱཀྱའི་སྲས་ཆོམ་རྐུན་འདི་རྣམས་ཀྱི་ནང་དུ་ཅིའི་ཕྱིར་རབ་ཏུ་བྱུང་སྟེ། ཚུར་ཤོག་འགྲོ་བར་བགྱིའོ་ཞེས་སྨྲས་ཏེ། དེས་འདི་བཟུང་ནས་ཁྱིམ་དུ་ཁྲིད་དོ། །

[Block 472]
དེ་ལྟར་ནི་ཆོམ་རྐུན་ཉིད་དུ་སྐུར་པ་འདེབས་པ་ནི་འདིར་ཉེས་དམིགས་ཏེ། ཡུལ་ཐག་རིང་བ་ལ་ནི་ཉེས་པ་མེད་དོ། །

[Block 473]
རང་གི་གནས་ལ་གནས་པ་དག་ལ་ཡང་ཐོས་ནས་བྱས་པ་ལ་ཉེས་དམིགས་སུ་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་འོངས་ནས་ཀྱང་ཉེས་དམིགས་བྱེད་པ་སྲིད་པ་ཉིད་ཀྱི་ཕྱིར་དེ་བས་ན་ཡུལ་ཐག་རིང་བ་ལ་ཡང༌[^330]ཞེས་བྱ་བ་མདོར་བྱས་པ་ཡིན་ནོ། །

[Block 474]
རབ་ཏུ་འབྱུང་བར་འདོད་པའི་ཟན་ནི་དགེ་འདུན་གྱིས་བྱིན་ན་རུང་ངོ་ཞེས་བྱ་བ་ལ། རུང་བ་ཞེས་བྱ་བ་ནི་འདི་ངེས་པ་མ་ཡིན་ཏེ། དགེ་སློང་དེ་རྣམས་ལ་སྨོས་པ་འཇུག་པའི་ཕྱིར་ཞེས་བྱ་བ་སྟོན་པར་བྱེད་དོ། །

[Block 475]
བཀོལ་བ་ཕ་མས་ཁྱོད་གནང་ངམ་འཇུག་ཏུ་ཡུལ་ཐག་རིང་པོ་ནི་མ་གཏོགས༌[^331]སོ་ཞེས་བྱ་བ་ལ། ཁྱོད་གནང་ངམ་ཞེས་བྱ་བ་ནི་ཁྱོད་མ་ཡིན་ནམ་ཞེས་བྱ་བ་འདིའི་གནས་པ༌[^332]འདི་ཡིན་ཏེ། བཀོལ་བ་ཞེས་བྱ་བ་འདིའི༌[^333]བརྗོད་པའི་ཐ་མ་ལ་ཡུལ་ཐག་རིང་པོ༌[^334]ནི་མ་གཏོགས་པ་ཞེས་བྱ་བའི་སྒྲས་འདི་ལྷག་པར་བརྗོད་པར་བྱའོ། །

[Block 476]
དེ་ལྟར་ན་ངག་ནི་འདི་ཡིན་ཏེ། ཁྱོད་ཕ་མ་དག་གིས་གནང་ངམ་ཞེས་བྱ་བའོ། །

[Block 477]
རབ་ཏུ་འབྱུང་བའི་དོན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནས་ཇི་སྲིད་དུ་ཕ་མ་དག་གིས་མ་གནང་བ་རབ་ཏུ་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་མི་བྱ་སྟེ། ཡུལ་ཐག་རིང་བ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བའོ། །

[Block 478]
ཉེ་བར་འོངས་པ་ལ་ཁྱོད་ནད་པ་མ་ཡིན་ནམ་ཞེས་དྲི་བར་བྱའོ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བའི་དོན་དུ་སྟེ་ཞེས་བྱ་བ་སྐབས་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 479]
ཁྱོད་ལ་ནད་གང་ཡང་རུང་བ་མེད་དམ་ཞེས་བྱ་བར་ཡང་རུང་ངོ་ཞེས་བྱ་བ་ནི་འདོན་པའི་རྟོག་པ་ལ་འདིར་ཉེ་བར་འབྲེལ་པའོ། །

[Block 480]
གཉིས་པོ་དག་ལས་གང་ཡང་རུང་བ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་བསྟན་པར་བྱེད་དོ། །

[Block 481]
བསྙེན་པར་རྫོགས་པར་བྱེད་པ་དག་གི་བྱེ་བྲག་ཏུ་འོ་ཞེས་བྱ་བ༌[^335]ནི་དྲི་བར་བྱའོ་ཞེས༌[^336]བྱ་བ་འདི༌[^337]ཡོངས་སུ་གྱུར་པ་ལ་དྲི་བར་བྱའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 482]
སྐྱེས་པ་རྣམས་ཀྱི༌[^338]ལུས་ལ་འདི་རྣམས་འདི་ལྟ་བུའི་ངོ་བོ་ཉིད་ལུས་ཀྱི་གནོད་པ་འབྱུང་བ་འདི་ལྟ་སྟེ། མཛེ་དང་འབྲས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་བྱེ་བྲག་དང་ལྡན་པ་སྟེ། ཁྱོད་ནི་འདི་ཙམ་དུ་ནད་པ་མ་ཡིན་ནམ་ཞེས་བྱ་བའོ། །

[Block 483]
ནད་པ་རབ་ཏུ་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཞུ་བ་བྱེད་པ་པོ་དང་། རབ་ཏུ་འབྱིན་པར་བྱེད་པ་དང་དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་ཁྲིད་པའི་དགེ་འདུན་མང་པོ་རྣམས་ཀྱི་བྱ་བ་སྟེ། དེ་བས་ན་མང་པོའི་ཚིག་གོ། །

[Block 484]
བཀོལ་བ་ཆད་པ་ཡན་ཆད་དོ་ཞེས་བྱ་བ་ནི་རྒྱུ་ལས་བཟློག་པའི་ཆད་པ་ཁས་མི་ལེན་པ་དག་ལ་ཞེས་བྱ་བ་འདི་ཡན་ཆད་ལས་ཅི་ཙམ༌[^339]བསྟན་པ་ཐམས་ཅད་དུ་བཀོལ་བ་ཞེས་བྱ་བའི་དབང་དུ༌[^340]བྱས་ནས་རིག་པར་བྱ་སྟེ། དེ་རྣམས་ཐམས་ཅད་བཀོལ་བ་དང་འབྲེལ་པ་རྣམས་སོ། །

[Block 485]
འདི་ལ་སྐྱེ་བའི་ཆོས་ཉིད་མེད་པར་ཡང་འདྲའོ་ཞེས་བྱ་བ་ནི་འདིར་གང་ཞིག་སྤྲུལ་པ་ལ་སོགས་པ་འགག་པར་འགྱུར་བ་དེ་ལ་ཡང་གི་སྒྲ་ནི་ཡན་ཆད་པ་ཞེས་བྱ་བ་ལས་འབྲེལ་བའི་དོན་དུའོ། །

[Block 486]
དེ་ལྟ་བུའི་རྟགས་ཅན་ནི་བསྙིལ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལྟ་བུའི་ཞེས་བྱ་བ་ནི་སྐྱེ་བའི་ཆོས་དང་མི་ལྡན་པ་ལའོ། །

[Block 487]
རྟགས་ཅན་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་ངམ་བསྙེན་པར་རྫོགས་པ་ལའོ། །

[Block 488]
ཁྱིམ་ན་གནས་པར་གྱུར་པ་ལ་དགེ་སློང་རྣམས་ཀྱིས་དབུས་སུ་གནས་པ་ལ་འགྲོ་བ་པའི་དགོངས་པའི་དབང་གིས་བསྙིལ་བ་ཡང་ནི་མ་ཡིན་ནོ། །

[Block 489]
ད་ནི་བཀོལ་བ་ལ་སོགས་པ་དང་འབྲེལ་པ་ཅན་བཤད་པར་བྱའོ། །

[Block 490]
སྤྲུལ་པའོ་ཞེས་བྱ་བ་ལ། ཁྱོད་ནི་སྤྲུལ་པ་མ་ཡིན་ནམ་ཞེས་བྱ་བ་རབ་ཏུ་འབྱུང་བའི་དོན་དུ་ཉེ་བར་འོངས་པ་ལ་དྲི་བ་ཡིན་ཏེ། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་དག་གིས་ཀྱང་སྤྲུལ་པ་རབ་ཏུ་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་མི་བྱའོ། །

[Block 491]
འདི་ལ་སྐྱེ་བའི་ཆོས་ཉིད་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བུའི་རྟགས་ཅན་ནི་བསྙིལ་བར་བྱའོ་ཞེས་བྱ༌[^341]བའོ། །

[Block 492]
དེ་བཞིན་དུ་མ་ནིང་ལ་སོགས་པ་གཞན་དག་ལ་ཡང་སྦྱར་བར་བྱའོ།[^342] །མ་ནིང་ངོ་། །དེ་ནི་རྣམ་པ་ལྔའོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་མ་ནིང་ལས་སོ། །

[Block 493]
ལྔ་པོ་གང་ཞེ་ན། སྐྱེས་ནས་དང་། ཟླ་བ་ཕྱེད་པ་དང་། འཁྱུད་ནས་ལྡང་བ་དང་། ཕྲག་དོག་ཅན་དང་། ཉམས་པའོ་ཞེས་བྱ་བ་ལ། སྐྱེས་ནས་མ་ནིང་ནི་གང་ཞིག་སྐྱེ་བ་ཉིད་ཀྱིས་བུད་མེད་ཀྱང་མ་ཡིན་སྐྱེས་པ་ཡང་མ་ཡིན་པའོ། །

[Block 494]
ཟླ་བ་ཕྱེད་པ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ཟླ་བ་ཕྱེད་ལ་བུད་མེད་ཟླ་བ་ཕྱེད་ལ་སྐྱེས་པ་དེ་ནི་ཟླ་བ་ཕྱེད་པའི་མ་ནིང་ངོ་། །ཟླ་བ་ཕྱེད་པ་ནི་ཟླ་བ་ཕྱེད་དོ། །

[Block 495]
འཁྱུད་ནས་ལྡང་བ་ཞེས་བྱ་བ་ནི་གང་ཞིག་གཞན་གྱིས་འོངས་པ་ལ་འབྱུང་བར་འགྱུར་བ་དེ་ནི་འཁྱུད༌[^343]ནས་ལྡང་བའི་མ་ནིང་ངོ་། །ཕྲག་དོག་ཅན་དང་ཞེས་བྱ་བ་ནི་གང་ཞིག་གཞན་དག་གིས་ཉེ་བར་འོངས་པའི་བུད་མེད་མཐོང་ནས་བརྩལ་བར་མ༌[^344]གྱུར་པ་དེ་ནི་ཕྲག་དོག་ཅན་གྱི་མ་ནིང་ངོ་། །ཉམས་པའོ་ཞེས་བྱ་བ་ལ། ཉམས་པའི་མ་ནིང་ནི་གང་གི་ཕོའི་དབང་པོ་བཅད་པ་ལ་སོགས་པས་ཉམས་པར་གྱུར་པ་སྟེ། དེ་ནི་ཉམས་པའི་མ་ནིང་ངོ་། །འདི་ལས་ཐ་མ་ནི་ཉེས་པ་བསྟེན་ན་བསྙིལ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། ཐ་མ་ཞེས་བྱ་བ་ནི་ཉམས་པའི་མ་ནིང་ངོ་། །སྐད་ཅིག་དེ་ལ་མ་ནིང་གི་སྐྱོན་ལ་བརྟེན་པ་དེ་ལས་བསྙིལ་བར་བྱའི་གཞན་དུ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
