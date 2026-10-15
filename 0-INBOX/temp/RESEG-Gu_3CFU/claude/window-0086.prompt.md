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
[Block 3011]
འདིར་རེག་པའི་དགེ་འདུན་གྱི་ལྷག་མ་ལ་ལན་བུ་ལས་གཞན་པའི་བུད་མེད་ཀྱི་མཚན་མ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པ་མ་ཡིན་ནོ། །

[Block 3012]
ཇི་ལྟར་བུད་མེད་ཀྱི་ལུས་ལ་རེག་པ་ལ་དངོས་གཞིའོ། །

[Block 3013]
དེ་བཞིན་དུ་ལན་བུ་ལ་རེག་པ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3014]
སླར་ལུས་མེད་པ་ཉིད་ཡོད་པར་གྱུར་པ་ལ་ཅིའི་ཕྱིར་ལན་བུ་ལ་དངོས་གཞི་བྱེད་པ་ཉིད་དུ་ཤེས་པ་ཡིན། ལུས་ལ་རེག་པ་ལྟར་འདིར་རེག་པ་ལ་རོ་ལ་སོ་སོར་ཉེ་བར་གནས་པའི་ཕྱིར་རོ། །

[Block 3015]
དེ་དང་འབྲེལ་བའི་གོས་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ལན་བུ་དང་འབྲེལ་པ་སྐུད་པ་ལ་སོགས་པ་ལ་ལན་བུའི་ཡན་ལག་ཏུ་གྱུར་པ་ནི་དེ་ལ་ལུས་དང་ལྡན་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3016]
འདིར་རྣམ་པར་སྤྱོད་པར་བྱེད་པ་རྣམས་ལ་སྐྱེད་པའི༌[^2052]སྡོང་བུ་ལས་རེག་པའི་སྐྲ་བཞིན་དུ་ཅོད་པན་དང་ཁ་ཆུ་ལ་སོགས་པ་ལ་རེག་པ་ནི་དཔེར་ན་སེན་མོ་དང་འདྲ་བར་སྦོམ་པོའོ། །

[Block 3017]
ནོམ་པ་དང་ཉུག་པ་དང་། སྤྲོད་པ་དང་འཛིན་པ་དང་། འདྲེན་པ་དང་ཡོངས་སུ་འདྲེན་པ་དང་། འོག་ནས་འཁྱུད་པ་དང་། སྟེང་ནས་འཁྱུད་པ་དང་། དམ་དུ་སྦྱོར་བ་རྣམས་ལ་ནི་བྱེ་ཕྲག༌[^2053]མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། སྤྲོད་པ་ནི་རེག་པ་ཙམ་མོ། །

[Block 3018]
འདིར༌[^2054]རེག་པ་དང་ལྡན་པ་གང་ཞིག་ལ་བྱེ་བྲག་ཏུ་སྙེགས་པ༌[^2055]ནི་མ་ཡིན་ནོ། །

[Block 3019]
དེ་བས་ན་ཇི་ལྟར་རྣམ་པ་གང་གིས་རེག་པ་བསྒྲུབ་པ་ལ་ཡང་དགེ་འདུན་གྱི་ལྷག་མ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3020]
བྱ་བའི་ཁྱད་པར་འགའ་ཞིག༌[^2056]ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3021]
དེ་ལ་ནོམ་པ་ཞེས་བྱ་བ་ནི་དང་པོར་ལན་ཅིག་ལུས་ལ་སྦྱོར་བ་ཉིད་དོ། །

[Block 3022]
ཉུག་པ་ཞེས་བྱ་བ་ནི་ཡང་དང་ཡང་དུ་ལུས་ལ་སྦྱོར་བའོ། །

[Block 3023]
སྤྱོད་པ༌[^2057]ཞེས་བྱ་བ་ནི་མཐར་སྦྱར་བའི་བསམ་པས་རང་གི་ལུས་བུད་མེད་ཀྱི་ལུས་དང་བར་དུ་མ་བཅད་པར་སྤྲོད་པའོ། །

[Block 3024]
འཛིན་པ་ཞེས་བྱ་བ་ནི་ལག་པ་ལ་སོགས་པ་འཆང་བའོ། །

[Block 3025]
འདྲེན་པས་ཞེས་བྱ་བ་ནི་ཐག་རིང་པོ་ནས་ལག་པ༌[^2058]སོགས་པ་ནས་བཟུང་སྟེ། ཐག་རིང་པོ་རྣམས་ནས་འོངས་པའོ། །

[Block 3026]
རིང་པོ་ནས་དྲངས་པ་ན་འདྲེན་པ་ཞེས་བྱ་བ་བྱས་ནས་སོ། །

[Block 3027]
ཡོངས་སུ་འདྲེན་པ་ཞེས་བྱ་བ་ནི་ཐག་ཉེ་བ་ནས་ཁོར་ཡུག་ཏུ་བསྐོར་བའོ། །

[Block 3028]
སྟེང་ནས་འཁྱུད་པ་ཞེས་བྱ་བ་ནི་སྟེང་ན་འདུག་པ་ལུས་ཀྱི་འོག་ཏུ་འཇོག་ཅིང་འཁྱུད་པར་བྱེད་པའོ། །

[Block 3029]
འོག་ནས་འཁྱུད་པ་ཞེས་བྱ་བ་ནི་དེ་ནས་ཕབ་སྟེ་འོག་ཏུ་འཇུག་ཅིང་འཁྱུད་པར་བྱེད༌[^2059]པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3030]
དམ་དུ་སྦྱོར་བ་ནི་མཐང་དམ་དུ་སྦྱོར་བ་ལ་སོགས་པའོ། །

[Block 3031]
བསྟེན་པར་བྱ་བས་བྱས་པ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་བསྟེན་པར་བྱ་བའི་སྒྲ་ནི་བཟུང་བ་ཡིན་གྱི་བུད་མེད་ཀྱི་སྒྲ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3032]
ན་སྨད་པ་བྱས་པ་ཐམས་ཅད་ལ་ཡང་ཁོངས་སུ་བསྡུ་བ་སྒྲུབ་པའི༌[^2060]དོན་དུ་གང་ཞིག་ནོམ་པ་ལ་སོགས་པ་འདི་ལ་ཁྱད་པར་ཅན་དང་ཁྱད་པར་ཅན་མ་ཡིན་པའི་རེག་པ་ལ་བསྟེན་པར༌[^2061]བྱ་བ་དང་ལྷན་ཅིག་ཏུ་བུད་མེད་དང་སྐྱེས་པ་ལ་སོགས་པ་རྣམས་ལ་བྱས་པ་ཉིད་དེ་ཁྱད་པར་མེད་པ་ཉིད་དོ།[^2062] །དེ་ལ་རང་དང་བཅས་པས་དེ་ལ་ཡང་ཀུན་དུ་འདོད་ཆགས་པའི་སེམས་ཀྱིས་བདག་གིར་བྱེད་ན་ལྟུང་བ་དེ་ཉིད་གང་ཞིག་རང་དང་བཅས་པ་ཉིད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3033]
གོས་ཀྱིས་བར་དུ་ཆོད་པ་ལ་ནི་འོག་མར་རོ་ཞེས་བྱ་བ་ནི་གོས་ཀྱིས༌[^2063]བར་དུ་ཆོད་པ་ཉིད་ལ་བསྟེན་པར་བྱ་བ་ལ་རེག་པ་ལ་འོག་མའི་ཚིག་གིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3034]
ཁྱད་པར་མ་བཟུང་བའི་ཕྱིར་མི་སྲིད་པ་ལ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 3035]
བར་དུ་ཆོད་པ་ཞེས་བྱ་བའི་སྒྲ་ནི་བར་དུ་ཆོད་པའི་རྣམ་གྲངས་སུ་གྱུར་པར་ཤེས་པར་བྱའོ། །

[Block 3036]
ཉེས་བྱས་ཀྱི༌[^2064]ན་སྨད་པ་ནི་གཞན་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ལྟུང་བ་གཞན་ལ་ན་སྨད་པར་གསུངས་པ་ལ་ལྟུང་བ་གཞན་དུ་རྣམ་པར་གཞག་པ་ཡིན་པ་དེ་བཞིན་དུ་འདིར་མ་ཡིན་ནོ། །

[Block 3037]
འོན་ཀྱང་ཉེས་བྱས་ཀྱི་ན་སྨད་པ་ལ་བྱ་དཀའ་བ་ཉིད་ཀྱི་ཕྱིར་གཞན་ཉིད་མ་ཡིན་ཏེ། ཉེས་བྱས་ཉིད་དེ་ཉེས་བྱས་ཕྲ་མོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3038]
དགེ་སློང་མ་ལ་རེག་པར་མི་བྱའོ། །

[Block 3039]
བུད་མེད་ལ་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཡང་རེག་པར༌[^2065]མི་བྱའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 3040]
རྗེས་སུ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་བསམ་པའི་ཉེས་པ་མེད་དུ་ཟིན་ཀྱང་བཀག་པར་རིག་པར་བྱ་སྟེ། ཀུན་ནས་ལྷག་མ་ཉིད་ཀྱི་ཕྱིར་བསྒྲུབ་པའོ། །

[Block 3041]
འདིར་གཉིས་ཀ་ལ་རེག་ན་ཉེས་བྱས་སོ། །

[Block 3042]
དགེ་སློང་མ་ནི་བུད་མེད་ཀྱི་རིགས་ལས་མ་འདས་མོད་ཀྱི་འོན་ཀྱང་དགེ་འདུན་གྱི་ཁོངས་སུ་གཏོགས་པའི་ཕྱིར་དགེ་སློང་མ་ལ་ཞེས་བྱ་བ་གང་ཞིག་ཁས་ལེན་པར་བྱེད་པ་དེའི་འདོད་པ་བཟློག་པའི་དོན་དུ་དགེ་སློང་མ་ལ་རེག་པར་མི་བྱ་ཞེས་བྱ་བའི་མདོ་འདི་བརྩམས་སོ། །

[Block 3043]
ཆུར་ཉམ་ཐག་པ་བསྒྲལ་བའི་ཕྱིར་ནི་རེག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྙིང་བརྩེ་བས་སྡུག་བསྔལ་ལས༌[^2066]ཐར་བར་བྱ་བ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་འདི་ལ་ཕྱོགས་གཅིག་པའི་རྗེས་སུ་བརྗོད་པ་འདི་འོག་མའི་ཆོ་ག་ལ་ཡུལ་བསྟན་པའི་དོན་དུའོ། །ཇི་ལྟར་རིག་པར༌[^2067]བྱ་ཞེ་ན། དེའི་ཕྱིར་མ་དང་སྲིང་མོ་དང་བུ་མོའི་འདུ་ཤེས་ཉེ་བར་བཞག་སྟེ་ལག་པ་འམ་སྐྲ་དག་ལས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3044]
དྲན་པ་རྙེད་པར་བྱ་བའི་ཕྱིར་བྱེ་མ་བདལ་བའི་སྟེང་དུ་ཁ་སྦུབ་ཏུ་གཞག་གོ་ཞེས་བྱ་བ་ནི་དེའི་ཚེ་ན་ཆུ་ཞུགས་པ་འཇག་པར་འགྱུར་ཞིང་དེ་ཟགས་ན་དྲན་པ་ཐོབ་པར་འགྱུར་རོ། །

[Block 3045]
ཁྱེའུ་བཞིན་བསྲུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཁྱིམ་པ་དག་ལ་བྱིན་པའི་ཁྱེའུ་རྣམས་ལ་ཁ་ཏོན་བྱེད་པའམ་ཡིད་ལ་བྱེད་པ་བསྐྱེད་ཅིང་ཕྱོགས་གཅིག་ཏུ་འདུག་སྟེ་སྲུང་བར་བྱེད་པ་དེ་བཞིན་དུ་འདི་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3046]
བ་གླང༌[^2068]རྫིའམ་ཕྱུགས་རྫི་དག་ལ་གཏང་དེ་ཟན་ལ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དུས་དེ་ཙམ་དུ་བ་གླང༌[^2069]རྫི་དང་ཕྱུགས་རྫི་རྣམས་ཀྱིས་ཁས་བླངས་པ་དང་མི་བསྐྱེད་པ་ལ་རང་གིས་བརྩོན་པར་གྱུར་པ་འམ་མགོན་མེད་པ་སླར་གཏད་པ་དང་། མཚན་མོ་ཡང་འོང་བའི་དོན་དུ་འབད་པར་བྱའོ། །

[Block 3047]
འོང་བ་མ་གྲུབ་པ་དང་མི་ནུས་པ་ཉིད་ཀྱིས༌[^2070]འདི་ལ་བདག་ཉིད་བསྲུང་བ་ལ་དེ་ཉིད་དུ་གནས་པ་ཞེས་བྱ་བའི་དོན་གྱིས་ཤེས་པར་བྱའོ། །

[Block 3048]
འཚོ་འམ་འོན་ཏེ་མ་ཡིན་ཞེས་ཡང་དང་ཡང་དུ་བརྟག་པར༌[^2071]བྱའོ་ཞེས་བྱ་བ་ནི་འཇིག་པ་དང་མི་འཇིག་པའི་དོན་འབད་པས་སོ་སོར་བརྟག་པའོ། །

[Block 3049]
སེམས་དག་པས་སྙིང་བརྩེ་བས་བུད་མེད་དེ༌[^2072]ལ་འཁྱུད་པ་ལ་ཉེས་པ༌[^2073]མེད་དོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་སྨན་གྱི་གཞི་ལས་བཅོམ་ལྡན་འདས་ཀྱིས་བུད་མེད་སྐྲ་གྲོལ་བ་ལ་འཁྱུད་པ་གནང་ངོ་ཞེས་འབྱུང་བ༌[^2074]སྟེ། དེ་མདོ་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 3050]
འདིར་དགེ་བའི་སེམས༌[^2075]ཉིད་ཙམ་ནི་དག་པའི་སེམས་ཉིད་དུ་རིག་པར་བྱའི། འདོད་ཆགས་དག་དང་བྲལ་བའི་སེམས་ཉིད་ཁོ་ན་ནི༌[^2076]མ་ཡིན་ནོ། །
--- END BLOCKS ---
