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
ཡང་ན་ཚིག་ནི་དོན་གྱིས་སྟོང་པར་བསྒྲུབས་ལ། སྒྲ་ཡང་སྒྲ་གཞན་གྱི་བརྗོད་བྱ་ཡིན་པས་དོན་ཉིད་ལ་དོན་དེ་ཡང་མེད་པ་ཉིད༌[^267]དོ་ཞེས་བྱ་ལ། དོན་མེད་པའི་ཕྱིར་སྒྲ་ཡང་མེད་པར་གཟིགས་ནས་གསུངས་པ་བརྗོད༌[^268]འགའ་མེད་ཅེས༌[^269]སོ། །

[Block 317]
བརྗོད་པ༌[^270]མེད་པར་གྱུར་ན་ཡང་བརྗོད་བྱའི་དོན་གྲུབ་པ་མེད་དོ་ཞེས་གནས་སོ། །

[Block 318]
འདིར་སྨྲས་པ། གལ་ཏེ་རྗོད༌[^271]བྱེད་ཀྱིས་བརྗོད་པའི་དོན་ཀྱང་མེད་ན། དེའི་ཚེ་ཅི་ཞིག་ཡོད། སྨྲས་པ། ཁོ་བོས་སྒྱུ་མའི་ནོར་གྱིས་ཕྱུག་པོར་བྱེད་པའམ་སྨིག་རྒྱུའི་ཆུས་ཁྱོད་ཀྱི་ཆུའི་གདུང་བ་སེལ་བར་བྱེད་པའམ། སྒྱུ་མའི་རི་དགས་ཀྱི་ཤས་བཀྲེས་པ་ཉེ་བར་ཞི་བར་བྱེད་པར་མི་ནུས་སོ། །

[Block 319]
འོ་ན་འདིར༌[^272]ཁོ་ན་ཉིད་གང་ཡིན་པ་དེ་ཉིད་གཟུང་བར་བྱ་བར་འགྱུར་ལ། སླར་ཡང་འདིར་དེ་ཁོ་ན་ཉིད་དེ་ཅི་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་ཁྱོད་དེ་ཁོ་ན་ཉིད་ལ་ཕྱིན་ཅི་ལོག་ཏུ་གོ་བ་དང་སྤོང་བ་དག་གིས་ལོག་པར་སྒྲུབ་པར་མི་བྱེད་ཅིང་ཆོས་ཉིད་ཟབ་མོ་ལ་གུས་པ་ཡང་སྐྱེད་ན་དེའི་ཚེ་ཁྱོད་ཀྱི།

[Block 320 [VERSE]]
བརྗོད་བྱ་མྱ་ངན་འདས་དང་མཚུངས། །
དངོས་པོ་ཀུན་གྱི་རང་བཞིན་སྟོང་། །

[Block 321]
རང་བཞིན་དང་ངོ་བོ་ཉིད་དང་དེ་ཁོ་ན་ཉིད་ཅེས༌[^273]པ་རྣམ་གྲངས་སོ། །

[Block 322]
རང་བཞིན་གྱིས་སྟོང་པ་ནི་རང་བཞིན་དང་བྲལ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 323]
མྱ་ངན་ལས༌[^274]འདས་པ་ནི་རྟག་པ༌[^275]མ་ལུས་པ་སྐྱེ་བ་མེད་པའི་རང་བཞིན་རང་གི་མཚན་ཉིད་ཅུང་ཟད་ཀྱང་མེད་པ་སྟེ། ཇི་སྐད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་གང་ངེས་པར་འདི་ནི་སྡུག་བསྔལ་མ་ལུས་པ་སྤོངས་པ། བོར་བ་བྱང་བར༌[^276]གྱུར་པ་ཟད་པ་འདོད་ཆགས་དང་བྲལ་བ་འགོག་པ་ཉེ་བར་ཞི་བ་ནུབ་པར་འགྱུར་བ་སྡུག་བསྔལ་གཞན་དུ་ཉིང་མཚམས་མི་སྦྱོར་བ། འདི་ནི་ཉེ་བར་ལེན་པ་མེད་པའོ། །

[Block 324]
འདི་ནི་ཞི་བ་གྱ་ནོམ་པའོ། །

[Block 325]
འདི་ལྟར་ཕུང་པོ་ཐམས་ཅད་སྤངས་པ་སྲེད་པ་ཟད་པ་འདོད་ཆགས་དང་བྲལ་བ་འགོག་པ་ནི་མྱ་ངན་ལས་འདས་པའོ་ཞེས་སོ། །

[Block 326]
འདི་ལྟར་མྱ་ངན་ལས་འདས་པའི༌[^277]རང་བཞིན་ཅི་ཡང་མེད་པ་དེ་ལྟར་ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་ཅི་ཡང་མེད་པས་དེའི་ཕྱིར་ཆོས་རྣམས་ཀྱི་དེ་ཁོ་ན་ཉིད་ཕྱིན་ཅི་མ་ལོག་པར་བསྟེན་པ། གང་ཞིག་ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་མྱ་ངན་ལས་འདས་པ་དང་མཚུངས་པར་བརྗོད་པར་བྱའོ། །

[Block 327]
དེ་ལྟར་ན་ཆོས་རྣམས་ཀྱི་དེ་ཁོ་ན་ཉིད་ཕྱིན་ཅི་མ་ལོག་པར་བརྟེན་པར༌[^278]འགྱུར་གྱི་གཞན་དུ་མ་ཡིན་ནོ། །

[Block 328]
འདིར་སྨྲས་པ། རེ་ཞིག་མྱ་ངན་ལས་འདས་པ་སྡུག་བསྔལ་དང་བྲལ་བ་ཙམ་ལ་རང་བཞིན་མེད་པ་ནི་རུང་གི །ཕྱི་དང་ནང་གི་ཆོས་འདུ་བྱེད་དང་མྱུ་གུ་ལ་སོགས་པ་དང་། མ་རིག་པ་དང་ས་བོན་ལ་སོགས་པ་རྒྱུ་དང་རྐྱེན་གྱིས་ཉེ་བར་བསྐྱེད་པའི་བདག་ཉིད་དུ་ཡོད་པ་རྣམས་ཇི་ལྟ་བར་རང་དང་སྤྱི་དང་ཐུན་མོང་དུ་ཉམས་སུ་མྱོང་བའི་རང་གི་མཚན་ཉིད་མྱ་ངན་ལས་འདས་པ་ལས་ཤིན་ཏུ་བསྐལ་པའི་མཚན་ཉིད་རྣམས་ཇི་ལྟར་རང་བཞིན་གྱིས་སྟོང་པ་ཉིད་དུ་བསྒྲུབ་པར་ནུས། དེའི་ཕྱིར་གང་ཆོས་ཐམས་ཅད་མྱ་ངན་ལས་འདས་པའི་རང་བཞིན་མ་ཡིན་ནོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་མ་རིག་པས་ཕྱིན་ཅི་ལོག་པའི་རྣམ་པར་ཤེས་པ་ལ་ཉམས་སུ་མྱོང་བ་རྣམས་ཚད་མར་འགྱུར་ན། དེའི་ཚེ་འཕགས་པ་དང་འཕགས་པའི་ལམ་གྱིས་ཅི་དགོས་པར་འགྱུར། བྱིས་པའི་སྐྱེ་བོས་ཉམས་སུ་མྱོང་བ་ཉིད་ཚད་མ་ལ། ཚད་མས་ཡང་དག་པར་མཐོང་བའི་ཕྱིར་མ་བཙལ་བར་དེ་རྣམས་གྲོལ་བར་གྱུར༌[^279]ཏེ། དེ་ལྟ་བུ་ཡང་མེད་པས་དེ་རྣམས་ཀྱིས༌[^280]ཉམས་སུ་མྱོང་བ་ནི་ཚད་མ་མ་ཡིན་ནོ། །

[Block 329]
ཇི་ལྟར་འཕགས་པའི་ལམ་གྱིས་མངོན་དུ་བྱས་པའི་འཕགས་པས་ཆོས་རྣམས་ཀྱི༌[^281]ཆོས་ཉིད་གཟིགས་པར་གྱུར་པ་དེ་ལ་རང་བཞིན་ནོ་ཞེས་རིགས་ཏེ། གང་ཞིག༌[^282]མ་མཐོང་བ་ལས་བྱིས་པ་རྣམས་ཉོན་མོངས་ལ། གང་ཞིག་མཐོང་བ་ལས་འཕགས་པ་རྣམས་རྣམ་པར་གྲོལ་ལོ། །

[Block 330]
ཇི་ལྟར་ན་འདི་རྣམས་མྱ་ངན་ལས་འདས་པ་དང་མཚུངས་ན་རང་བཞིན་གྱིས་སྟོང་པའོ། །

[Block 331]
འོ་ན་དེ་ཁོ་བོ་ལ་མངོན་སུམ་མ་ཡིན་ན། དེ་ཇི་ལྟར་ཁོ་བོ་ཅག་གིས་འདི་རྟོགས་པར་ནུས་ཤེ་ན། སྨྲས་པ། མོས་པ་མེད་པ་དད་པ་མེད་པ་སྡིག་པའི་གྲོགས་པོ་དང་འབྲེལ་པ་ཐོས་པ་ཆུང་བ་ལེ་ལོ་ཅན་རྨོངས་པ་ལ་སོགས་པ་དང་ལྡན་པས་དེ་རྟོགས་པར་འགལ་བས་དེས་འདི་མི་མཐོང་སྟེ། ཉོན་མོངས་པའི་གོ་སྐབས་སུ་འགྱུར་བས། སྦྱིན་པ་དང་སྤྲོ་བ་དང་ཐོས་པ་མང་བ་དགེ་བའི་བཤེས་གཉེན་བརྟེན་པ༌[^283]དད་པ་དང་མོས་པ་ལ་སོགས་པ་སོ་སོར་བརྟེན་པར༌[^284]བྱའོ་ཞེས་བྱ་སྟེ། འདི་དག་དང་ལྡན་པས་འཕགས་པས་བསྟན་པའི་རིགས་པ་དང་དཔེ་ཡང་འདིར་ཁས་བླང་བར་བྱའོ། །

[Block 332]
དེ་ལྟར་ཐབས་དང་བཅས་གང་རིགས་པས་ངེས་པར༌[^285]ཡོད་ན་ཆོས་རྣམས་ཀྱི་རང་བཞིན་མངོན་སུམ་ཉིད་དུ་འགྱུར་རོ། །

[Block 333]
སླར་ཡང་ཅི་ཞིག་འདིར་འཕགས་པས་བསྟན་པའི་རིགས་པ་གང་གིས་ཆོས་རྣམས་ཀྱི་ཆོས་ཉིད་མྱ་ངན་ལས་འདས་པ་དང་མཚུངས་པར་རིགས༌[^286]པས་མངོན་སུམ་དུ་འགྱུར་ཞེ་ན། འཕགས་པས་ཉེ་བར་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 334 [HEADING]]
### ཚིགས་བཅད་གསུམ་པ། ^1-3-0

[Block 335 [VERSE]]
གང་ཞིག་དངོས་ཀུན་རང་བཞིན་ནི། །
རྒྱུ་རྐྱེན་ཚོགས་པའམ་སོ་སོའི་དངོས། །
ཀུན་ལ་ཡོད་མིན་དེ་ཕྱིར་སྟོང་། །

[Block 336]
ཞེས་པ་ལ་དེ་ལ་རྒྱུ་ནི་འབྲས་བུ་རྫོགས་པར་བྱེད་པ་ལ་འདྲ་བའི་འབྲས་བུ་རྫོགས་པར་བྱེད་པའི༌[^287]ཐུན་མོང་མ་ཡིན་པའོ། །

[Block 337]
འདི་ལྟ་སྟེ་སཱ་ལུའི་མྱུ་གུས་སཱ་ལུའི་ས་བོན་ནོ། །

[Block 338]
རྐྱེན་ནི་ཐུན་མོང་བ་སྟེ། འདི་ལྟ་སྟེ་སཱ་ལུའི་མྱུ་གུ་དེ་ཉིད་ཀྱི་ས་ལ་སོགས་པའོ། །

[Block 339]
དེ་ཡང་ཇི་ལྟར་སཱ་ལུའི་མྱུ་གུ་སྐྱེད་པའི་ཡན་ལག་གི་དངོས་པོར༌[^288]གྱུར་པ་དེ་བཞིན་ནས་ཀྱི་མྱུ་གུ་ལ་སོགས་པ༌[^289]ཡང་ངོ་། །

[Block 340]
མྱུ་གུ་ལ་སོགས་པའི་རྒྱུ་ལས་སྐྱེས་པའི་འབྲས་བུ་ས་ལ་སོགས་པའི་རྣམ་པ་དང་རྗེས་སུ་འབྲེལ་པ་མ་ཡིན་ལ་སཱ་ལུའི་ས་བོན་གྱི་རྣམ་པ་དང་རྗེས་སུ་འབྲེལ་ཏོ་ཞེས་བྱའོ། །

[Block 341]
རྒྱུའི་དངོས་པོ་འབའ་ཞིག་ཙམ་དུ་ཉེ་བར་འགྲོ་བས་འདི་ལ་རྐྱེན་ཉིད་དུ་རྣམ་པར་འཇོག་གོ། །

[Block 342]
རེ་ཞིག་གང་འདིའི་རྒྱུ་དང་རྐྱེན་དུ་འགྱུར་ན་རྫོགས་པར་བྱེད་པ་ནི་རྒྱུའི་དངོས་པོར་གནས་ལ། གང་དུ་རྐྱེན་ནི་འདིའི་ངེས་པའི་རྒྱུ་མ་ཡིན་ཏེ། འདི་ལྟ་སྟེ་རྣམ་པར་ཤེས་པའི་དམིགས་པའི་རྐྱེན་ནོ། །

[Block 343]
དེ་ཉིད་ཀྱིས་ན༌[^290]རྒྱུ་གཉིས་དང་རྐྱེན་གཉིས་སོ་ཞེས་སོ།

[Block 344]
[^291] །ཡུལ་གཅིག་ལ་རྒྱུ་རྐྱེན་གྱི་སྒྲའི་སྦྱོར་བ་བཅོམ་ལྡན་འདས་ཀྱིས་མཛད་དོ།[^292] །ཚོགས་པ་ནི་དངོས་པོ་དེ་དག་མ་ཚང་བ་མེད་པར་ཉེ་བར་གནས་པ་ལས་སྐྱེའི་གཞན་དེ་མ་ཐག་པ་ཉེ་བར་གནས་པ་ལས་མ་ཡིན་པས་རྒྱུ་རྐྱེན་ཚོགས་པར་འདིར་རྟོགས་པར་བྱའོ། །

[Block 345]
སོ་སོའི་དངོས་པོ༌[^293]ནི་དེ་རྣམས་ཐ་དད་པ་སྟེ། རྒྱུ་དང་རྐྱེན་ཚོགས་པ་མ་ཡིན་པའི་སོ་སོའི་དངོས་པོའི༌[^294]རྒྱུ་དང་རྐྱེན་ཚོགས་པ་མ་ཡིན་པས་སོ་སོའི་དངོས་པོ་དེ་ཐམས་ཅད་ལ་འབྲས་བུའི་དངོས་པོ་ཐམས་ཅད་ཀྱི་རང་བཞིན་མེད་དོ། །

[Block 346]
དེའི་ཕྱིར་དེས་སྟོང་པས་རང་བཞིན་དང་བྲལ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 347]
གལ་ཏེ་འདིར་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་འགའ་ཞིག་ཡོད་ན་དེ་ངེས་པར་འདུས་བྱས་སམ་འདུས་མ་བྱས་སུ་ཡོད་པར་འགྱུར། དེ་ལ་རེ་ཞིག་འདུས་མ་བྱས་ནི་རྒྱུ་མེད་པ་བདག་ཉིད་ཀྱི་དངོས་པོ་མ་སྐྱེས་པ་ལ་རང་བཞིན་གྱིས་བརྗོད་པའི་སྐལ་བ་དང་ལྡན་པ་མི་རིགས་སོ། །

[Block 348]
འདུས་བྱས་ལ་ཡང་རང་བཞིན་མི་འཐད་དེ། ཅིའི་ཕྱིར་ན་གལ་ཏེ་འདུས་བྱས་ཀྱི་རང་བཞིན་དུ་གྱུར་ལ། འདུས་བྱས་རྣམས་ནི་རྒྱུ་དང་རྐྱེན་ལས་སྐྱེ་བའི་ཕྱིར་ན་སྐྱེ་བ་རྒྱུ་དང་རྐྱེན་ལ་རག་ལས་པར་འགྱུར་ལ། རྒྱུ་དང་རྐྱེན་ལ་རག་ལས་ནས་སྐྱེ་བ་ནི་བྱས་པ་སྟེ། རང་བཞིན་དུ་མི་འཐད་དོ། །

[Block 349]
ཡང་འདི་སྙམ་དུ་སེམས་ཏེ། རྒྱུ་དང་རྐྱེན་གྱིས་བསྐྱེད་པའི་དངོས་པོ་རྣམས་ཁོ་ན་རང་བཞིན་ནོ་ཞེ་ན། ངེས་པར་འདི་སྐད་བརྗོད་པར་བྱ་སྟེ་རྒྱུ་དང་རྐྱེན་གང་ལས༌[^295]རང་བཞིན་གང་ཞིག་སྐྱེ་ན་དེ་ཅི་དེ་རྣམས་ལ༌[^296]ཡོད་པ་ལས་དེ་སྐྱེ་བར་འགྱུར་གྱི། གང་ཞིག་གང་ལ་མེད་པར་དེ་དེ་ལས་མི་སྐྱེ་སྟེ། འདི་ལྟ་སྟེ་འཇིམ་པ་ལས་སྣམ་བུའམ་སྐུད་པ་ལས་བུམ་པ་ཞེས་སོ། །

[Block 350]
འདི་ནི་རྒྱུ་ལ་སོགས་པ་ལས་སྐྱེ་བར་འདོད་ན་ངེས་པར་རྒྱུ་ལ་སོགས་པ་ལ་རང་བཞིན་ཡོད་པ་ཉིད་དུ་ཁས་བླང་བར་བྱ་ན། འདི་ནི་ཁས་བླང་བར༌[^297]མི་ནུས་ཏེ། ཡོད་བཞིན་པ་ན་དམིགས་པར་ཐལ་བ་དང་། སྐྱེ་བ་དོན་མེད་པ་དང་། ཐུག་པ་མེད་པའི་སྐྱོན་དང་། རྒྱུ་མེད་པ་ཡོད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 351]
གལ་ཏེ་ཡང་རྒྱུ་ལ་སོགས་པ་ལ་འབྲས་བུའི་རང་བཞིན་ཡོད་ན། དེ་དག་ལ་ཐམས་ཅད་ཀྱི་བདག་ཉིད་ཀྱིས་ཡོད་དམ་ཆ་ཤས་ཀྱིས་སོ། །

[Block 352]
དེ་ལ་རེ་ཞིག་གལ་ཏེ་ཐམས་ཅད་ཀྱིས༌[^298]བདག་ཏུ་རྟོག་ན་རྒྱུ་དང་རྐྱེན་རྣམས་མང་པོའི་ཕྱིར་འབྲས་བུ་དུ་མས་འཇུག་ལ། དེའི་ཕྱིར་རྒྱུ་ལ་སོགས་པ་སོ་སོ་ལ་འབྲས་བུ་མེད་ལ་རྒྱུ་དུ་མས་འབྲས་བུ་གཅིག་སྒྲུབ་པ་མ་ཡིན་ཞིང་། རྒྱུ་གཅིག་གིས་བསྒྲུབ་པར་བྱ་བ་ཉིད་དུ་འགྱུར་རོ། །

[Block 353]
དེའི་ཕྱིར་གང་ལ་གནས་པ་དེ་ཉིད་ལ༌[^299]འཇུག་པའི་ཕྱིར་དེ་ལྟར་རེ་ཞིག་ཐམས་ཅད་ཀྱི་བདག་ཉིད་ཀྱི་རྒྱུ་ལ་སོགས་པ་ལ་འབྲས་བུ་མི་གནས་སོ། །

[Block 354]
ད་ནི་ཆ་ཤས་ཀྱིས་ཀྱང་མི་གནས་ཏེ། འབྲས་བུ་གཅིག་དུམ་བུར་སྐྱེ་བར་ཐལ་བར་འགྱུར་ལ། རྒྱུ་ཐ་དད་པ་ན༌[^300]ཡང་རྒྱུ་དུ་མས་འབྲས་བུ་སྐྱེད་པར་ཐལ་ལོ། །

[Block 355]
གང་ཡང་རྒྱུ་ལ་སོགས་པ་ལ་མི་གནས་ན། དེ་རྒྱུ་ལ་སོགས་པ་ལས་མི་སྐྱེ་ལ་རྩ་བའི་རབ་བྱེད་དང་པོར་ཡང་ན་དེ་རྐྱེན་ལ་སོགས་པ་ལ་མེད་ཀྱང་དེ་རྣམས་ལས་འབྱུང་ན།
--- END BLOCKS ---
