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
འདི་ལ་སྐྱེ་བའི་ཆོས་ཉིད་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བུའི་རྟགས་ཅན་ནི་བསྙིལ་བར་བྱའོ་ཞེས་བྱ༌[^341]བའོ། །

[Block 492]
དེ་བཞིན་དུ་མ་ནིང་ལ་སོགས་པ་གཞན་དག་ལ་ཡང་སྦྱར་བར་བྱའོ།[^342] །མ་ནིང་ངོ་། །དེ་ནི་རྣམ་པ་ལྔའོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་མ་ནིང་ལས་སོ། །

[Block 493]
ལྔ་པོ་གང་ཞེ་ན། སྐྱེས་ནས་དང་། ཟླ་བ་ཕྱེད་པ་དང་། འཁྱུད་ནས་ལྡང་བ་དང་། ཕྲག་དོག་ཅན་དང་། ཉམས་པའོ་ཞེས་བྱ་བ་ལ། སྐྱེས་ནས་མ་ནིང་ནི་གང་ཞིག་སྐྱེ་བ་ཉིད་ཀྱིས་བུད་མེད་ཀྱང་མ་ཡིན་སྐྱེས་པ་ཡང་མ་ཡིན་པའོ། །

[Block 494]
ཟླ་བ་ཕྱེད་པ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ཟླ་བ་ཕྱེད་ལ་བུད་མེད་ཟླ་བ་ཕྱེད་ལ་སྐྱེས་པ་དེ་ནི་ཟླ་བ་ཕྱེད་པའི་མ་ནིང་ངོ་། །ཟླ་བ་ཕྱེད་པ་ནི་ཟླ་བ་ཕྱེད་དོ། །

[Block 495]
འཁྱུད་ནས་ལྡང་བ་ཞེས་བྱ་བ་ནི་གང་ཞིག་གཞན་གྱིས་འོངས་པ་ལ་འབྱུང་བར་འགྱུར་བ་དེ་ནི་འཁྱུད༌[^343]ནས་ལྡང་བའི་མ་ནིང་ངོ་། །ཕྲག་དོག་ཅན་དང་ཞེས་བྱ་བ་ནི་གང་ཞིག་གཞན་དག་གིས་ཉེ་བར་འོངས་པའི་བུད་མེད་མཐོང་ནས་བརྩལ་བར་མ༌[^344]གྱུར་པ་དེ་ནི་ཕྲག་དོག་ཅན་གྱི་མ་ནིང་ངོ་། །ཉམས་པའོ་ཞེས་བྱ་བ་ལ། ཉམས་པའི་མ་ནིང་ནི་གང་གི་ཕོའི་དབང་པོ་བཅད་པ་ལ་སོགས་པས་ཉམས་པར་གྱུར་པ་སྟེ། དེ་ནི་ཉམས་པའི་མ་ནིང་ངོ་། །འདི་ལས་ཐ་མ་ནི་ཉེས་པ་བསྟེན་ན་བསྙིལ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། ཐ་མ་ཞེས་བྱ་བ་ནི་ཉམས་པའི་མ་ནིང་ངོ་། །སྐད་ཅིག་དེ་ལ་མ་ནིང་གི་སྐྱོན་ལ་བརྟེན་པ་དེ་ལས་བསྙིལ་བར་བྱའི་གཞན་དུ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 496]
རྐུ་ཐབས་སུ་གནས་པའོ་ཞེས་བྱ་བ་འདིའི་མཚན་ཉིད་ནི་གང་ཞེ་ན། བསྙེན་པར་རྫོགས་པའི་ཆོ་ག་མ་བྱས་པ་ཉིད་དམ་མ་ཆགས་པ་ཉིད་དུ་ཤེས་ལ་ལན་གཉིས་སུ་དགེ་འདུན་དང་ལྷན་ཅིག་ལས༌[^345]ཉམས་སུ་མྱོང་བར་གྱུར་པ་ཉིད་ན་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྙེན་པར་རྫོགས་པ་ལ་འདྲེན་པའི་གང་ཞིག་གསོལ་བ་ལ་སོགས་པ་དེ་མ་བྱས་པ་ཉིད་དུ་ཤེས་ཤིང་བྱས་པ་ཉིད་དུ་ཡང་མ་ཆགས་པ་ཉིད་དུ་ཤེས་ཤིང་། གལ་ཏེ་ཡང་ཆོ་ག་བྱས་པ་བསྙེན་པར་རྫོགས་པ་ནི་ཆགས་པ་མ་ཡིན་ཏེ། ལོ་བཅུ་དགུ་ལོན་པ་ལ་སོགས་པའི་སྐྱོན་གྱིས་དེའི་ཕྱིར་དགེ་འདུན་དང་ལྷན་ཅིག་ལས་གཉིས་པ་ཉམས་སུ༌[^346]མྱོང་བ་ལ་དེ་ཉིད༌[^347]ཅེས་བྱ་བ་ནི་རྐུ་ཐབས་སུ་གནས་པ་ཉིད་དོ། །

[Block 497]
འོ་ན་གང་གི་ཕྱིར་ཉེ་བར་འཁོར་རང་བཞིན་དུ་གནས་པའི་དགེ་སློང་རྣམས་དང་ལྷན་ཅིག་ཏུ་གསོ་སྦྱོང་གི་ལས་ལན་གཉིས་ལན་གསུམ་ཉམས་སུ་མྱོང་བར་གྱུར་པ་དེ་ཙམ་གྱིས་ནི་རྐུ་ཐབས་སུ་གནས་པ་ཡིན་ནོ་ཞེས་གསུངས་ན། གསུམ་ཞེས་བྱ་བ་དེ་ཅིའི་ཕྱིར་མདོར་མ་བྲིས་ཤེ་ན། གང་གི་ཕྱིར་ངེས་པར་བྱེད་པའི་ཚིག་ནི་འདི་མ་ཡིན་ཏེ། འོན་ཀྱང་རྒྱུན་ལ་འདི་རབ་ཏུ་བསྟན་པའོ། །

[Block 498]
རྒྱུན་ལ་རྩོམ་པར་གྱུར་པ་ན་ཉམས་པར་འགྱུར་ཞེས་བྱ་བ་སྟེ། གཞན་དུ་ན་གཉིས་ཞེས་བྱ་བས་འདི་རྣམ་པར་གཞག་པ་ལ། གསུམ་ཞེས་བྱ་བ་འདི༌[^348]དབུགས་དབྱུང་བ༌[^349]རྣམ་པར་ཤེས་པར་འགྱུར་རོ། །

[Block 499]
དེ་ལྟར་ན་འདི་ནི་རྩོམ་པ་སྟེ་ཐ་སྙད་དུ་བྱ་བ་ཆོས་ཉིད་ཀྱི་རྣམ་པར་གཞག་པ་མ་ཡིན་པ་ཞེས་བྱ་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 500]
འདིར་ལུང་ཡང་ཡོད་དེ།

[Block 501]
གཏམ་གྱི་གཞི་ལས།

[Block 502]
གང་གིས༌[^350]རྐུ་ཐབས་སུ་གནས་པ་རབ་ཏུ་དབྱུང་བར་མི་བགྱིད།[^351] བསྙེན་པར་རྫོགས་པར་མི་བགྱི་བའི་གཞི་དེ་ཉིད་ཀྱིས་རབ་ཏུ་དབྱུང་བར་བགྱི་བ་དང་། བསྙེན་པར་རྫོགས་པར་བགྱི་བ་མ་མཆིས་སམ་ཞེ་ན། བཀའ་སྩལ་པ་ཡོད་དེ། གང་གིས་ལན་གཉིས་ལན་གསུམ་དུ་གསོ་སྦྱོང་ཉམས་སུ་མྱོང་བར་འགྱུར་བ༌[^352]དེ་རབ་ཏུ་དབྱུང་བར་མི་བྱ། བསྙེན་པར་རྫོགས་པར་མི་བྱའི། གང་གིས་ལན་ཅིག་གསོ་སྦྱོང་ཉམས་སུ་མྱོང་བར་གྱུར་པ་དེ་ནི་རབ་ཏུ་དབྱུང་བར་བྱ། བསྙེན་པར་རྫོགས་པར་བྱའོ་ཞེས་བྱ་བའོ།

[Block 503]
[^353] །གང་གི་ཕྱིར་གཞན་དུ་ན་ཁ་ཅིག་གིས་ལན་གཉིས་སོ་སོར་ཉམས་སུ་མྱོང་བ་ལ་འོས་པ་ཉིད་མ་ཡིན་ཏེ། སླར་རིགས་པ་ནི་གང་གི་ཕྱིར་འདིར་ཐོག་མར་རབ་ཏུ་འཇུག་པ་ན་དོགས་པ་དང་བཅས་པར་འགྱུར་རོ། །

[Block 504]
དེ་ལས་བརྫུན་པ༌[^354]ཉིད་ཀྱི༌[^355]རང་བཞིན་ཉིད་ནི་འགྲོ་བར་མི་འགྱུར་ཏེ། རྒྱུན་དུ་བྱེད་ཅིང་དེའི་རང་བཞིན་ཉིད་ཐོབ་པ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 505]
འོ་ན་འདིར་གསོ་སྦྱོང་བཟུང་བར་མི༌[^356]བྱ་བ་སྟེ། དེ་བས་ན་འདིར་ཅིའི་ཕྱིར་ཁྱད་པར་མེད་པར་ལས་ཐམས་ཅད་སོ་སོར་ཉམས་སུ་མྱོང་བ་གང༌[^357]ཞེ་ན། བརྗོད་པར་བྱ་སྟེ། དགེ་འདུན་ལ་ཡང་དག་པར་བརྟེན་པའི་བྱ་བ་ལ་འདིའི་ཁོངས་སུ་བསྡུས་པའོ། །

[Block 506]
གང་ཞིག་གསོ་སྦྱོང་ལ་མཚུངས་པའམ་ལས་གཞན་རྣམས་ལ་ཡང་དགེ་འདུན་གྱི༌[^358]གནས་པ་ཉིད་དོ། །

[Block 507]
དེ་བས་ན་དཔེ་ཉིད་ཀྱིས་འདིར་གསོ་སྦྱོང་གཟུང་བ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 508]
བསྙེན་པར་རྫོགས་པར༌[^359]མ་ཚང་བའི་ལྟུང་བྱེད་དྲི་བ་ལས་འདི་ལ་ལུང་ཡང་ཡོད་དེ། གང་ཞིག་གསོལ་བ་དང་། བཞིའི་ལས་ཀྱིས་བསྙེན་པར་མ་རྫོགས་པར་དགེ་འདུན་གྱི་ལས་གསོ་སྦྱོང་ངམ། དགག་དབྱེ་འམ། གང་ཟག་བཅུ་གཉིས་བསྐོ་བ་དག་ཉམས་སུ་མྱོང་བར་གྱུར་པ་དེ་ཡང་དེ་ཙམ་གྱིས་ནི༌[^360]རྐུ་ཐབས་སུ་གནས་པ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 509]
ཇི་སྲིད་དུ་བསྙེན་པར་མ་རྫོགས་པས་བྱ་བ་མ་ཡིན་པ་རྗེས་སུ་མཚོན་པར་གྱུར་པ་དགེ་འདུན་གྱི་ལས༌[^361]རབ་ཏུ་འབྱུང་བ་ཞུ་བ་ལ་སོགས་པ་དེ་ཐམས་ཅད་དགེ་འདུན་ལ་རག་ལས་པའི་ཕྱིར་ལས་ཀྱི༌[^362]ཕྱོགས་པ་ཉིད་དོ། །

[Block 510]
དེ་བས་ན་ལས་ཀྱི་ཚིག་ཀྱང་འདིར་དཔེར་རྟོགས་པར་བྱའོ། །

[Block 511]
གལ་ཏེ་དེ་ལྟ་ཡིན་ན་རབ་ཏུ་འབྱུང་བར་ཞུ་བ༌[^363]དང་དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་བསྒྲུབ་པ་དང་གསང་སྟེ་སྟོན་པ་དང་ཡོངས་སུ་དག་པ་དང་བསྡུ་བ་དང་། སྤོ་བ་ལ་སོགས་པ་ཞུ་བ་དང་རྗེས་སུ་ཐོབ་པ་རྣམས་ཀྱང་སོ་སོར་ཉམས་སུ་མྱོང་བ༌[^364]ལ་རྐུ་ཐབས་སུ་གནས་པ་ཉིད་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 512]
མུ་སྟེགས་ཅན་ཞུགས་པའོ་ཞེས་བྱ་བ་ནི་དེའི་རང་གི་ངོ་བོ་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བའི་ཕྱིར། རབ་ཏུ་བྱུང་བ་འདི་ལ༌[^365]ཡང་དག་པར་བླངས་པ་ལྟ་བ་དང་ལྡན་པ་ཆོས་གོས་འདི་བོར་ཏེ། རྒྱལ་མཚན་དེས་དེར་སྐྱ་རེངས༌[^366]ཤར་ན་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་བྱུང་བ་འདི་ལ༌[^367]ཡང་དག་པར་བླངས་པ་འདི་ཡིན་པས་ན་ཡང་དག་པར་བླངས་པའི་རབ་ཏུ་བྱུང་བ་འདིའོ། །

[Block 513]
ལྟ་བ་དེ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་མུ་སྟེགས་ཅན་དེ་རྣམས་ཀྱི་ལྟ་བ་འདི་ལ་ཡོད་པས་ན་དེའི་ལྟ་བ་ཅན་ནོ། །

[Block 514]
ཆོས་གོས་འདི་བོར་ཏེ་ཞེས་བྱ་བ་ནི་བདེ་བར་གཤེགས་པའི་དགེ་སློང་གི་ཆ་བྱད་བོར་བར་བྱས་ནས༌[^368]སོ། །

[Block 515]
རྒྱལ་མཚན་དེས་ཞེས་བྱ་བ་ནི་མུ་སྟེགས་ཅན་གྱི་རྒྱལ་མཚན་གྱིས་སོ། །

[Block 516]
དེར་ཞེས་བྱ་བ་ནི་མུ་སྟེགས་ཅན་གྱི་འདུག་གནས་སུའོ། །

[Block 517]
སྐྱ་རེངས༌[^369]ཤར་ན་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མུ་སྟེགས་ཅན་ཞུགས་པ་ཅན་ཡིན་ནོ། །

[Block 518]
དེ་མ་བྱས་པ་ཡང་རྐུ་ཐབས་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་ཆ་བྱད་མ་བྱས་པར་བོར་ཏེ། མངོན་པར་འདོད་པའི་མུ་སྟེགས་ཅན་གྱི་རྟགས་འདོད་པས་བགོས༌[^370]ནས་དེའི་འདུག་གནས་སུ༌[^371]སྐྱ་རེངས༌[^372]ཤར་བ་ཞེས་བྱ་བ་ནི༌[^373]དེ་བཞིན་གཤེགས་པའི་རྟགས་ཅན་གང་གིས་ཡང་དག་པར་བླངས་པ་སྟེ། མུ་སྟེགས་པའི་ལྟ་བ་ཅན་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 519]
འདི་ནི་དེ་མ་བྱས་པའོ། །

[Block 520]
འོག་མ་འདི་མ་བྱས་པས་གཞན་དུ་ཡང་མུ་སྟེགས་ཅན་དུ་སོང་བ་ཉིད་འབྱུང་བ་ཡིན་ཏེ་ཇི་ལྟར་ཞེ་ན། དཔེར་ན་རྐུ་ཐབས་དང་འདྲའོ། །

[Block 521]
རྐུ་ཐབས་ཀྱི་དེ་ཉིད་བརྗོད་དེ་ལས་ཉམས་སུ་མྱོང་བ་གཉིས་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 522]
རྐུ་ཐབས་ཀྱི་དེ་ཉིད་བརྗོད་ཟིན་ཏོ། །

[Block 523]
མ་བསད་པ་དང་། ཕ་བསད་པ་དང་། དགྲ་བཅོམ་པ་བསད་པ་དང་། དགེ་འདུན་གྱི་དབྱེན་བྱས་པ་དང་། དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བ་དང་། དགེ་སློང་མ་སུན་ཕྱུང་བ་དང་། ཕམ་པར་གྱུར་པ་བཞི་ལས་ལྟུང་བ་གང་ཡང་རུང་བ་ཞིག་བྱུང་བ་མ་ཡིན་ནམ་ཞེས་སོ། །

[Block 524]
རྒྱུ་ལས་བཟློག་པའི་ཆད་པ་ཁས་མི་ལེན་པ་དག་རབ་ཏུ་བྱུང་བ༌[^374]དང་བསྙེན་པར་རྫོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། རྒྱུ་ལས་བཟློག་པའི་ཞེས་བྱ་བ་ནི་རྒྱུ་གང་གིས་འཐབ་རྩོད་བྱེད་པ་ཉིད་ལ་སོགས་པས་བསྡིགས་པ་ལ་སོགས་པའི་ནན་ཏུར་གྱི་ལས་བྱེད་པར་འགྱུར་བ་དེ་བཟློག་པ་ནི་འཐབ་རྩོད་བྱེད་པ་ཉིད་ལ་སོགས་པ་མ་ཡིན་པའོ། །

[Block 525]
ཆད་པ་ཁས་མི་ལེན་པ་ནི་སྒྲུབ་པར༌[^375]བྱེད་པ༌[^376]བཞིན་པ་མ་ཡིན་པའོ། །

[Block 526]
བསྙེན་པར་རྫོགས་ན་བཟོད་པ་གསོལ་ཟིན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མི་བཟོད་པ་བསྙེན་པར་མ་རྫོགས་པ་རྣམས་བསྙེན་པར་རྫོགས་པ་ཉིད་བཟོད་པ་ཉིད་ཀྱི་ཕྱིར་སླར་བཟོད་པ་གཞན་ནི་བྱ་བ་མ་ཡིན་ནོ། །

[Block 527]
བཟོད་པ་ཞེས་བྱ་བ་ནི་བཟོད་པར་བྱ་བའོ།[^377] །བཙུན་པ་དགེ་སློང་དག་བསྡིགས་པའི་ལས་བགྱིས་ནས་རེ་ཞིག་བསྙེན་པར་རྫོགས་པར་བགྱིད༌[^378]ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱི་འམ། བསྙེན་པར་མ་རྫོགས་ཞེས་བགྱི། ཉེ་བ་འཁོར་བསྙེན་པར་རྫོགས་པ༌[^379]ཞེས་བྱ་སྟེ། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་དག་ལ་ནི་འགལ་ཚབས་ཅན་དུ་འགྱུར་ལ། བཟོད་པ་ནི་གསོལ་ཟིན་པ་ཞེས་བྱ་བའོ་ཞེས་བྱ་བ༌[^380]ནི་གླེང་གཞི་དག་ལས་གསུངས་སོ། །

[Block 528]
གལ་ཏེ་བསྙེན་པར་རྫོགས་ནས་ཁས་མི་ལེན་པ་ནི་ཚོགས་པ་ཡོད་ན་ཡང་ཆད་པས་བཅད་དོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་ནས་ནི༌[^381]འཐབ་ཀྲོལ་མི་བྱེད་པ་ཉིད་ལ་སོགས་པ་རྒྱུ་བཟློག་པ་གལ་ཏེ་ཁས་མི་ལེན་ན་ཚོགས་པ་ཡོད་པ་ན་ཡང་ཆད་པའི་ལས་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 529]
གལ་ཏེ་མ་མཐོང་ངོ་ཞེས་བརྫུན་ཟེར་ན་ལྟུང་བྱེད་དོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་བདག་གིས་མ་མཐོང་ཞེས་བྱ་བ་གལ་ཏེ་བརྫུན་ཟེར་ན་ལྟུང་བར་བྱེད་པ་འདིའི་ལྟུང་བྱེད་དོ། །

[Block 530]
འདི་ལྟ་བུའི་རིགས་ཅན་གྱི་བརྫུན་དུ་སྨྲ་བ་རྣམས་ལ་ལྟུང་བྱེད་མེད་པར་དོགས་པར༌[^382]བྱ་བ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
