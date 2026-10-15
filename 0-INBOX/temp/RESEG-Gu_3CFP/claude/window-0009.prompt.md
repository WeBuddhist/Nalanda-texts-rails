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
གཞི་དེས་ཞེས་བྱ་བ་ནི། ཡིད་བརྟན་དུ་རུང་བ་ཉིད་དང་། ཡིད་ཆེས་པ་ཉིད་ཀྱི་གཞི་དེས་ཚིག་གཟུང་བར་འོས་པར་འགྱུར་རོ། །

[Block 317]
གྲགས་པ་ཆེན་པོ་ནི་གྲགས་པར་འགྱུར་བ་སྟེ། ཅི་ལྟ་བུ་ཞེ་ན།

[Block 318 [VERSE]]
དཔའ་བ་ལ་སོགས་པ་དྲུག་གོ། །
སྙན་པ་ཇི་ལྟ་བུ་ཞེ་ན།
འཇིག་རྟེན་འདིར་གྲགས་པར་འགྱུར་བའོ། །

[Block 319]
ཇི་ལྟ་བུ་ཞེ་ན། བཟོ་དང་ལས་ཀྱི་གནས་རྣམ་པ་སྣ་ཚོགས་ལྷག་པར་རབ་དང་ཕུལ་དང༌[^182]ཞེས་བྱ་བ་ནས་བརྩམས་པའོ། །

[Block 320]
གཞི་དེས་བྱ་བ་ནི་གྲགས་པ་ཆེན་པོ་དང་སྙན་པས་འཇིག་རྟེན་དུ་ཤེས་པ་ཉིད་ཀྱི་གཞིའོ། །

[Block 321]
ཕོའི་དངོས་པོ་ཞེས་བྱ་བ་ནི། གང་དང་ལྡན་པས་སྐྱེས་པ་ཞེས་བརྗོད་པའོ། །དེ་ཡང་གང་གིས་འགྱུར་ཞེ་ན། ཕོའི་དབང་པོ་དང་ལྡན་པས་ཏེ། དེ་ནི་མི་ཉིད་དོ། །

[Block 322]
གནོད་པ་ཆུང་བ་ནི་གློ་བུར་བའི་ནད་ཉུང་བའོ། །

[Block 323]
ནད་མེད་པའི་རང་བཞིན་ཅན་ནི། ལུས་ལ་གནས་པའི་ནད་མེད་པ་སྟེ། འདི་དག་གིས་ནི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་ཟིལ་གྱིས་མི་ནོན་པར་བསྟན་ཏོ། །

[Block 324]
སྤྲོ་བ་ཆེ་བ་ཡིན་ཞེས་བྱ་བ་ནི། བྱ་བ་བྱེད་པ་ཐམས་ཅད་ལ་ནུས་པ་དང་ལྡན་པ་ཞེས་བྱ་བའི་དོན་ཏེ། [^183]འདིས་ནི་གཉེན་པོའི་ཕྱོགས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 325]
མི་འཚེ་བའི་མཚན་ཉིད་གང་ཞེ་ན། སེམས་ཅན་རྣམས་ལ་མི་འཚེ་བ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏེ། སེམས་ཅན་རྣམས་ལ་མི་འཚེ་བའི་བསམ་པ་ནི། རྗེས་སུ་བརྩེ་བའི་བསམ་པའམ། དེ་ནི་སྙིང༌[^184]རྗེ་ཆེ་བའི་བསམ་པའོ། །

[Block 326]
སྣང་བའི་སྦྱིན་པ་ཇི་ལྟར་ཁ་དོག་ཕུན་སུམ་ཚོགས་པའི་རྒྱུ་ཡིན་ཞེ་ན་ཁ་དོག་གསལ་བར་བྱེད་པ་ལ་གཙོ་བོ་སྣང་བ་ཡིན་པས་སོ། །

[Block 327]
གོས་གཙང་མ་སྦྱིན་པ་ནི་ཁ་དོག་ཕུན་སུམ་ཚོགས་ཏེ། གོས་ཀྱི་སྦྱིན་པ་ནི་དེའི་ཁ་དོག་ཕུན་སུམ་ཚོགས་པའི་རྒྱུའི་ཕྱིར་རོ། །

[Block 328]
ང་རྒྱལ་ངེས་པར་བཅོམ་པ་ཞེས་བྱ་བ་ནི། ང་རྒྱལ་ངེས་པར་བཅོམ་པའི་ཕྱིར་ཕྱག་ལ་སོགས་པ་བྱ་བར་འོས་པ་རྣམས་ལ། ཕྱག་ལ་སོགས་པ་བྱེད་པས་དེ་ལ་འོས་པའི་རིགས་སུ་སྐྱེ་བའོ། །

[Block 329]
སློང་བ་རྣམས་ལ་ཞེས་བྱ་བ་ནི། བདག་ཉིད་གང་སློང་བའོ། །

[Block 330]
ཡོ་བྱད་མི་བདོག་པ་རྣམས་ལ་ཞེས་བྱ་བ་ནི་མི་སློང་ན་ཡང་དེ་ལ་བདག་ཉིད་སོང་ནས་སྟེར་བ་ཉིད་དོ། །

[Block 331]
དེ་ལྟར་སྦྱིན་པ་རྣམ་པ་གཉིས་པོ་སློང་བ་དང་མི་སློང་ན་ཡང་སྦྱིན་པ་ནི་དབང་ཕྱུག་ཕུན་སུམ་ཚོགས་པའི་རྒྱུའོ། །

[Block 332]
དཀོན་མཆོག་གསུམ་ལ་མཆོད་པ་ཉིད་ཀྱིས་ནི་གྲགས་པ་ཆེན་པོ་རྒྱས་པར་འགྱུར་རོ། །

[Block 333]
བླ་མ་མཆོད་པས་ཀྱང་སྙན་པར་གྲགས་པར་འགྱུར་རོ། །

[Block 334]
རྒྱུ་གཉིས་ཀྱིས་ཞེས་བྱ་བ་ལ། བུད་མེད་ཀྱི་དངོས་པོ་ལ་མི་དགའ་བ་དང་། གཞན་དག་ལ་སྐྱེས་པ་ཉིད་སྒྲུབ་པའི་རྒྱུ་གཉིས་པོ་དེ་དག་གིས་འགྱུར་ཏེ། དེ་ལ་བུད་མེད་ཀྱི་དངོས་པོ་ལ་མི་དགའ་བ་ནི་འདུན་པ་བཟློག་པའོ། ། གང་ལས་འདུན་པ་བཟློག་ཅེ་ན། བུད་མེད་ཀྱི་དངོས་པོ་ཉིད་ལས་སོ། །

[Block 335]
གང་དག་འདུན་པ་བཟློག་ཅེ་ན། བུད་མེད་རྣམས་སོ། །

[Block 336]
མཚན་ཉིད་གང་ལས་ཤེ་ན། བུད་མེད་ཀྱི་དངོས་པོ་ལ་དགའ་བ་རྣམས་ལས༌[^185]སོ། །

[Block 337]
གཞན་དག་ལ་སྐྱེས་པ་ཉིད་སྒྲུབ་པ་ཇི་ལྟ་བུ་ཞེ་ན། ངེས་པར་རྣམ་པར་ཐར་པར་བྱེད་པའོ། །

[Block 338]
གང་དག་ངེས་པར་རྣམ་པར་ཐར་པར་བྱེད་ཅེ་ན། སྐྱེས་པ་རྣམས་སོ། །ཇི་ལྟ་བུའི་གནས་སྐབས་དག་གི་ཞེ་ན། བཟུང༌[^186]སྟེ་ཁྲིད་པ་རྣམས་ཏེ། གཉིས་ཀྱིས་ནི་ངེས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 339]
གང༌[^187]གི་དོན་དུ་ཞེ་ན། ཕོའི་དབང་པོ་གཅད་པའི༌[^188]ཕྱིར་རོ། །ཇི་ལྟར་ཐར་པར་བྱེད་ཅེ་ན། ཆོས་ཀྱིས༌[^189]ཏེ། དེ་ལ་ཆོས་ནི་གང་སྤྱད་པར༌[^190]བྱ་བ་སྐྱེས་པ་ཕོའི་དབང་པོ་གཅད་པའི༌[^191]ཕྱིར་སྲིད་པ༌[^192]དང་བརྗེ་བའི་རྫས་རྗེས་སུ་མཐུན་པ་སྦྱིན་པ་སྟེ། དེས་ཉེ་བར་འཚོ་བའམ་གཞན་པ་ཡང་རུང་བ་ལ། དེའི་འདོད་པས༌[^193]བྱེད་ཀྱི་གནོད་པས་ནི་མ་ཡིན་ནོ། །

[Block 340]
བྱ་བ་ལ་འཇུག་པའི་ངོ་བོ་ནི་ཞལ་ཏ་བྱེད་པ་སྟེ། དེའི་བྱེད་པ་ནི་སེམས་ཅན་རྣམས་ཀྱི་བྱ་བ་བྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏེ། བྱ་བའི་གྲོགས་བྱེད་ཅིང་བྱ་བ་བྱེད་པར་འདོད་པས་བརྩམས་པ་དེའི་དེ་ལྟ་བུའི་བྱ་བ་དེ་ལ་གྲོགས་བྱེད་པའོ། །

[Block 341]
ཅི་ནུས་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱི་ནུས་པ་དང་རྗེས་སུ་མཐུན་པར་རོ། །

[Block 342]
ཅི་ལྕོགས་ཞེས་བྱ་བ་ནི། དེའི་བྱ་བ་ལ་ནུས་པ་དང་སྟོབས་ལ༌[^194]ལྟོས་པས་སོ། །

[Block 343]
ཆོས་དང་མཐུན་པ༌[^195]ཞེས་བྱ་བ་ནི། བྱ་བ་དེ་ཆོས་དང་མཐུན་པ་ཉིད་ལ་ལྟོས་ནས་ཞལ་ཏ་བྱེད་པ་སྟེ། གྲོགས་བྱེད་པ་མེད་པ་ལ་གྲོགས་བྱེད་པའོ། །

[Block 344]
དེ་ལྟ་བུ་ནི་རེ་ཞིག་གནོད་པ་ཉུང་བ་དང་། ནད་མེད་པའི་རང་བཞིན་ཅན་གྱི༌[^196]རྣམ་པར་སྨིན་པའི་རྒྱུའོ། །

[Block 345]
ལྟ་བར་འགྱུར་བའི་ཟས་དང་སྐོམ་བསྒྲུབ་པ་ནི་སྤྲོ་བ་ཆེན་པོ་ཉིད་ཀྱི་རྒྱུའོ། །

[Block 346]
སེམས་རྣམ་པར་དག་པ་བཞིའི་བསྡུས་པའི་དོན་ནི། གང་ལ་བསམ་པ་དང་། ཇི་ལྟ་བུར་བསམ་པ་དང་། རྣམ་པ་ཅི་ལྟ༌[^197]བུས་བསམ་པའོ། །

[Block 347]
གང་ལ་བསམ་པ་ཞེས་བྱ་བ་ལ། །བྱང་ཆུབ་ཏུ་ཆོས་མཐུན་པ་དང་མཚུངས་པར་རོ། །

[Block 348]
ཇི་ལྟ་བུར༌[^198]ཞེས་བྱ་བ་ལ་དྲག་ཏུའོ། །

[Block 349]
རྣམ་པ་ཇི་ལྟ་བུས་ཞེས་བྱ་བ་ལ་ཉིན་གཅིག་བཞིན་དུ་སྐད་ཅིག་རེ་རེ་ལ་དེ་དང་མཐུན་པའི་ཆོས་ཁོ་ན་ལ་ལན་མང་དུ་རྟོག་ཅིང་དཔྱོད་པས་སོ། །

[Block 350]
དང་པོ་གསུམ་ནི་ཇི་ལྟར་ཡོད་པའི་མཚན་ཉིད་དོ། །

[Block 351]
ཐ་མ་ནི་ཇི་སྙེད་ཡོད་པའི་མཚན༌[^199]ཉིད་དོ། །

[Block 352]
ཡུན་རིང་པོ༌[^200]ཞེས་བྱ་བ་ནི། སྦྱོར་བ་དེ་ཇི་སྙེད་པས་རྒྱུན་མི་འཆད་པར་གྲིམས་པར་བྱེད་པ་དག་གོ། །

[Block 353]
ཇི་ལྟར་འབྱུང་བར༌[^201]སྦྱོར་བས་ནི་བག་མེད་པ་རྣམས་ཡང་དག་པར་ལེན་དུ་གཞུག་པའི་ཕྱིར་བསྔགས་པ་བརྗོད་པ་ཉིད་དོ། །

[Block 354]
ཡང་དག་པར་བླངས་པ་རྣམས་ལ་ཡང་ཞེས་བྱ་བ་ལ། ཡང་དག་པར་ཞུགས་པ་དང་། ཞུམ་པ་རྣམས་ངེས་པར་གཞུག་པ་དང་། རབ་ཏུ་དགོད༌[^202]པའོ། །

[Block 355]
སྦྱོར་བ་འདིའི་བསྡུས་པའི་དོན་ནི། རྣམ་པ་ཇི་ལྟ་བུས་དང་། གང་ལ་སྦྱོར་བས་སོ། །
--- END BLOCKS ---
