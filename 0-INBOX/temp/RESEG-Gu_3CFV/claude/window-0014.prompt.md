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
[Block 491]
སོང་ཤིག་ཅེས་བྱ་བ་ཡང་ངོ་། །འཚལ་ལགས་སོ་ཞེས་བྱ་བས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལས་བཟློག་པ་ནི་ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲ་ནི་སྔར་ཡང་ངོ་ཞེས་བྱ་བའི་རྗེས་བསྙགས་པའི་ཕྱིར་རོ། །

[Block 492]
རེ་ཞིག་ཅེས་བྱ་བའི་སྒྲ་ཉེ་བར་སྦྱར་ན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདི་གསུམ་རེ་ཞིག་སྒྲ་ལ་ཉེ་བར་མཚམས་སྦྱར་བ་ལ་བཟློག་པར་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 493]
ཆོག་གོ་ཞེས་བྱ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལ་ཡང་རེ་ཞིག་ཅེས་བྱ་བའི་སྒྲ་ཉེ་བར་སྦྱར་ན་སྤངས་པ་མ་ཡིན་ན་སླར་གཞན་དག་ལ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 494]
ཐུག་པ་ལས་ཀྱང་ཞེས་བྱ་བ་གང་ཞིག་བརྗོད་པ་དེ་ལ་སླར་བརྗོད་པར་འདོད་ནས༌[^293]ཁ་གཟར་གྱེན་དུ་འགྲེང་དུ་མི་བཏུབ་པ་ཉིད་ཀྱི་ཐུག་པ་དག་ནི་ཐུག་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁ་གཟར་གྱེན་དུ་གནས་པ་གང་ཡིན་པ་དེ་གལ་ཏེ་ཐུག་པ་ལ་གྱེན་དུ་འགྲེང༌[^294]དུ་མི་བཏུབ་ན་དེ་ལྟར་ན་འདི་ལ་ནི་ཐུག་པ་ཉིད་དོ། །

[Block 495]
སོར་མོ་ལྔ་མི་མངོན་པ་ནི་སྐྱོ་མའོ་ཞེས་བྱ་བ་ནི་ཐུག་པ་ཉིད་ལེན་དུ་བཅུག་པ་ལ་ཞེས་བྱ་བ་འདི་དང་འབྲེལ་པ་བརྗོད་པར་བྱའོ། །

[Block 496]
ཐོ་འཚམས༌[^295]པ་ནི་བྱིན་ལེན་སྟོབས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ནི་ཐོ་འཚམས༌[^296]པར་ཤེས་པ་ཉིད་ལ་འདི་ལྟར་བྱིན་ལེན་དུ་འཇུག་པ་མ་ཡིན་ནོ། །

[Block 497]
འདི་ནི་བྱིན་ལེན་བྱེད་དུ་འཇུག་པའི་ཀུན་དུ་སྤྱོད་པ་ལ་རྗེས་སུ་མཐུན་པ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 498]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 499]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་སྔར་ཐོ་འཚམས༌[^297]པར་རྟོགས་པ་ཅན་གྱིས་བྱིན་ལེན་བསྟབས་པར་གྱུར་ལ། དེས་སླད་ཀྱི་ཐ་མལ་པའི་གནས་སྐབས་སུ་བྱིན་ལེན་བསྟབས་པ་དེ་འཚལ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེ་བ་འཁོར་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 500]
ཐོ་འཚམས༌[^298]པའི་རྟོག་པ༌[^299]ཅན་ཞེས་བྱ་བ་ནི་འདི་ལ་ཐོ༌[^300]འཚམ་མོ་སྙམ་པའི་རྟོག་པ་གང་ལ་ཡོད་པར་གྱུར་པ་ཞེས་བྱ་བ་འདི༌[^301]དོན་རིག་པར་བྱའོ། །

[Block 501]
སྤང་བ་བསྟན་ཟིན་ཏོ།། །།

[Block 502]
ད་ནི་ལྷག་བོར་བྱ་བ་བསྟན་པར་བྱ་སྟེ། མཚམས་ཀྱི་ཕྱི་རོལ་དང་མི་འཐོབ་པའི་ཕྱོགས་དང་མདུན་མ༌[^302]ཡིན་པ་ན་འདུག་པ་ལས་ལྷག་བོར་བྱ་བ་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་མཚམས་ཀྱི་ཕྱི་རོལ་ན་གནས་པ་དང་། མི་འཐོབ་པའི་ཕྱོགས་ན་གནས་པ་དང་། མདུན་མ་ཡིན་པ་ན་འདུག་པ་ལས་ཞེས་བྱ་བའི་བསྡུ་བའོ། །

[Block 503]
གཉིས་དང་ལྡན་པ་ལ་གཅིག་པའི་དངོས་པོ་འདི་རྣམས་ལས་ལྷག་བོར་བྱ་བ་མི་འབྱུང་སྟེ། མཚམས་གཞན་ན་གནས་པ་ན་གང་ཞིག་ལ་ཡང་ཡན་ལག་ཉིད༌[^303]དོ། །

[Block 504]
དེ་བས་ན་ཕྱི་རོལ་གྱི་མཚམས་ལ་གནས་པ་དོར་བའོ། །

[Block 505]
ལྷག་བོར་ཞེས་བྱ་བ་ནི་མཐར་ཐུག་པར་གྱུར་པའི་བོར་བ་ནི་དོར་བ་སྟེ༌[^304]ལྷག་བོར༌[^305]རོ། །

[Block 506]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 507]
ལྷག་མར་མ་བྱས་ཤིང་མ་བོར་ཡོངས་སུ་མ་བཏང་བ་ནི་ལྷག་བོར་མ་བྱས་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 508]
བྱ་བ་ལག་ཏུ་མ་བླངས་པ་ལ་ཡང་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་ལྷག་བོར་བྱ་བའི་དངོས་པོ་གང་ཡིན་པ་དེ་ལག་ཏུ་མ་བླངས་པ་ལ་ཡང་ལྷག་བོར་མི་འབྱུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 509]
འདིར་གཞུང་ནི་དགེ་སློང་དེས་ལག་པ་གཉིས་བསྙལ་ཏེ་བྱིན་ལེན་བྱས་པ་ལས༌[^306]ཞེས་གང་གསུངས་པ་ཡིན་ནོ། །

[Block 510]
ནམ་མཁའ་ལ་ཡང་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་དེ་ནི་མཚམས་ཀྱི་ཕྱི་རོལ་ཞེས་བྱ་བ་འདིའི་ཁོངས་སུ་གཏོགས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 511]
རུང་བ་མ་ཡིན་པ་དང་དེ་དང་འདྲེ་བ་ལ་ནི་མི་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རུང་བ་ལ་མི་རུང་བ་འདྲེས་པས་ལྷག་བོར་གྱི་དངོས་པོ་དོར་བ་ཉིད་ཀྱིས་མི་བྱ་བ་ཉིད་དོ། །

[Block 512]
གང་གི་ལྷག་བོར་དུ་བྱ་བ་དང་གང་གི་འདིར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གནས༌[^307]མ་བཏང་བས་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཟ་བའི་གནས་ནི་གནས་ཤེས་པར་དོན་གྱིས་ཤེས་པར་བྱའོ། །ཅི་ཆོག་པར་མ་བྱས་པ་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་མི་ཟ་བར་བརྟག་པར༌[^308]བྱས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་མ་གསོལ་བས་ཀྱང་བྱའམ་ཞེ་ན། དེའི་ཕྱིར་གསོལ་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 513]
འདིའི་བྱ་བ་ཅི་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཁྱོད་ཀྱིར་གྱུར་གྱི༌[^309]བཞུད་ཅིག་ཅེས་བྱ་བའི་ཚིག་གིས་བྱའོ། །

[Block 514]
ཁ་ཅིག་ནི་ཅི་བདེར་གསོལ་ཅིག་ཅེས་ཀྱང་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདོད་པ་གཞན་ལ་འདི་བསྟན་པའོ། །

[Block 515]
གཞན་དག་གི་ཚིག་འདི་འདིར་བྱ་བ་ཉིད་ཀྱིས་ཤེས་ཀྱང་ཟེར་ཏེ། འདིར་དོན་གཙོ་ཆེ་བ་ཡིན་གྱི་ཚིག་ནི་མ་ཡིན་ནོ། །

[Block 516]
དེ་བས་ན་འདི་གཉིས་ཀ་འདིའི་བྱ་བ་ཡིན་ནོ། །

[Block 517]
གཞན་ཡང་འདི་ལྟ་བུའི་རིགས་ཅན་ཀྱི་ཚིག་ཅེས་བྱ་བ་རྟོགས་པར་བྱའོ། །ཅི་ཚིག་ཙམ་ཁོ་ནས་ལྷག་བོར་བྱ་བ་ཟད་དམ་ཞེ་ན། དེའི་ཕྱིར་ཁམ་གཉིས་སམ་གསུམ་ཟོས་ནས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་གི་ཡང་མ་ཟོས་པ་ལ་ཀུན་དུ་རྟོག་པར༌[^310]བྱ་བའི་ལྷག་བོར་འདུ༌[^311]བྱེད་པ་དེས་ཀྱང་ཁམ་གཉིས་སམ་གསུམ་ཟོས་ནས་བྱ་བ་ཞེས་སྨོས་པ་ནི་བྱ་བ་བཏང་བས་ནི་བཟའ་བར་མི་བྱའོ་ཞེས་བྱ་བ་སྟེ། མ་ཟོས་པ་ལ་ཀུན་དུ་རྟོག་པ༌[^312]བྱེད་བཞིན་པ་ལ་ཡང་གང་ཟག་བརྗོད་པ་གང་ཡིན་པ་དེ་ལ་དེས་ནི་བཟའ་བར་མི་བྱ་བར་ཁྱོད་ཀྱིར་གྱུར་གྱི༌[^313]བཞུད་ཅིག་ཅེས་བྱ་བའི་ཚིག་ཙམ་ཉིད་དུ་བྱ་བ་འདིས་བསྟན་པར་ཤེས་པར་བྱའོ། །

[Block 518]
ལྷག་བོར་བྱས་པ་གཞན་གྱིས་བཟའ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གཅིག་ལ་རུང་བ་གང་ཡིན་པ་དེ་གཞན་ལ་ཡང་རུང་ངོ་ཞེས་བྱ་བ་དེ་ལ་འདི་བསྟན་པའོ། །ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྤངས་པ་ཉིད་དང་ལྷག་བོར་མ་བྱས་པ་ཉིད་དག་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྷག་བོར་མ་བྱས་པ་ཉིད་གང་ཡིན་པ་དེ་ལ་དེ་ནི་ལྷག་བོར་ཉིད་དུ་མ་བྱས་པའོ། །

[Block 519]
ཟོས་ནས༌[^314]སྤངས་པ་ཉིད་ལ་ཡང་ལྷག་བོར་དུ་བྱ་བ་མ་བྱས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅི་ཞིག་རྗེས་སུ་བསྒྲུབ་ན་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཟོས་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཅི་ཞིག་ཟོས་ན་ཞེ་ན། དེའི་ཕྱིར་ཟས་ཙམ་མོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཅའ་བར་བྱ་བ་ཙམ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 520]
འདི་སྟན་གཅིག་པའི་ཟས་དང་པོར་བྱས་པས་དེའི་ཕྱིར་དེ་དག་ཐམས་ཅད་ནི་རྣམ་པར་ངེས་པ་མ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 521]
སྦྱངས་པའི་ཡོན་ཏན་ཡང་དག་པར་བླངས་པ་སྤངས་པ་ཉིད་ཡིན་ཡང་རུང་སྤངས་པ་ཉིད་མ་ཡིན་ཡང་རུང་སྟེ། ལྷག་བོར་བྱས་ཀྱང་རུང་ལྷག་བོར་མ་བྱས་ཀྱང་རུང་བཅའ་བར་བྱ་བ་དང་བཟའ་བར་བྱ་བ་དག་ཟོས་བཞིན་པས་བཟའ་བར་མི་བྱ་ཞེས་བྱ་བ་འདིའི་བྱེ་བྲག་རྟོགས་པར་བྱའོ། །

[Block 522]
སྟན་གཅིག་པའི་ཟས་ཀྱི་ལྟུང་བྱེད་དོ།། །།

[Block 523]
འདི་ཡང་ཤེས་གཙོའོ། །

[Block 524]
སྤངས་པ་ཉིད་དང་ལྷག་བོར་མ་བྱས་པ་ཉིད་དག་ལའོ་ཞེས་སྔར་བསྟན་པའི་ཡན་ལག་དེ་དག་ཁས་བླངས་ནས་བསྒྲུབ་པ་གང་ཡིན་ལ་འདུ་ཤེས་པ་འདིའི་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེས་བྱ་བ་འདི་ལ་འདི་སྐད་ཅེས་བརྗོད་པར་བྱ་སྟེ། སྟོབས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟས་ཙམ་ཟོས་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 525]
གང་ལ་སྟོབས་ན་ཞེ་ན་དེའི་ཕྱིར་དགེ་སློང་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐམས་ཅད་དུ་རུང་བ་མ་ཡིན་པའི་ཕྱིར་སྟོབས་པ་ལ་ཉེས་པ་ཞེས་བྱ་བ་འདིའི་རྗེས་སུ་འབྲངས་ནས་རིག་པར་བྱའོ། །

[Block 526]
སྤངས་པ་ལ་སྟོབས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 527]
ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སོ་སོར་ངེས་པའི་ཟས་ཀྱི་གནས་ཅན་དག་ལས་གཞན་པའི་དགེ་སློང་དགེ་འདུན་དུ་གྱུར་པ་མཚམས་ཀྱི་ནང་ན་གནས་པ་དག་ཟན་ལྷན་ཅིག་མ་ཡིན་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་ཁང༌[^315]ན་ཟས་ཐ་དད་པ་ཉིད་དུ་ངེས་པ་དེ་ནི་སོ་སོར་ངེས་པའི་ཟས་སོ། །

[Block 528]
དགེ་སློང་གང་དག་ལ་གནས་དེ་དག་ནི་སོ་སོར་ངེས་པའི་ཟས་ཀྱི་གནས་ཅན་དག་གོ། །

[Block 529]
དེ་རྣམས་ལས་གཞན་དགེ་སློང་མཚམས་ཀྱི་ནང་ན་གནས་པའི་བཞི་ལ་སོགས་པ་དགེ་འདུན་དུ་གྱུར་པའི་དགེ་སློང་རྣམས་དང་ལྷན་ཅིག་མ་ཡིན་པ་ཉིད་ཀྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 530]
འདིར་གཞུང་ནི་ཚོགས་ཤིང་ཟ་བ་བཟུང་བ་ནི་དགེ་འདུན་དུ་གྱུར་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་རིག་པར་བྱའོ། །
--- END BLOCKS ---
