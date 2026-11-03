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
[Block 2976]
འདིར་གཞུང་ནི་ཞུ་བ༌[^2037]ལས་བཙུན་པ་དགེ་སློང་གིས་རེ་ཞིག་འཛམ་བུའི་གླིང་གི་བུད་མེད་ལ་བྱང་གི་སྒྲ་མི་སྙན་པ་དང་ལྷན་ཅིག་ཆོས་སྟོན་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ། །

[Block 2977]
དེ་བཞིན་དུ་གླིང་གཞན་པ་རྣམས་དང་ལྷན་ཅིག་ཆོས་སྟོན་པ་ལ་ཡང་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2978]
བཅོམ་ལྡན་འདས་ཀྱིས་རིག་པའི་སྐྱེས་པ་མེད་པར་བུད་མེད་ལ་ཆོས་བསྟན་པར་མི་བྱའོ་ཞེས་གང་གསུངས་པ་དེ་ལ་རིག་པའི་སྐྱེས་པ་ཇི་ལྟ་བུ་ཞིག་དང་ལྷན་ཅིག་ཏུ་བུད་མེད་ལ་ཆོས་བསྟན་པར་བྱ་ཞེ་ན། རུང་བ་གང་ཡིན་པའོ། །

[Block 2979]
རུང་བ་ཇི་ལྟ་བུ་ཞེ་ན། སྨྲས་པ། ཁྱིམ་པ་ཡང་རུང་རབ་ཏུ་བྱུང་བ་ཡང་རུང་སྟེ། འགྱུར་བ་བསྟེན་པར་མི་བྱེད་པ་གང་ཡིན་པའོ། །

[Block 2980]
རྣམ་པར་འགྱུར་བའི་སྒོ་འབྲེལ་བའི་དོན་དུ་འདིར་རིག་པའི་སྐྱེས་པ་ལ་བརྟེན་པའོ། །

[Block 2981]
འདིར་འདི་དག་ལ་བདག་པོ་ཉིད་ཡོངས་སུ༌[^2038]རྫོགས་པ་མ་ཡིན་ཏེ། གླིང་གཞན་ནས་སྐྱེས་པ་ལ་སྐྱེ་བ་འདི་སུ་ཞིག་ཅེས་བྱ་བ་ཡིན་ལ་བརྟེན་པ་ཉིད་ཀྱི་གུས་པ༌[^2039]མེད་པས། དེ་བས་ན་འདི་ལྷག་པར་ཤེས་པར་འགྱུར་ཏེ། འདི་དག་ལ་རྩོམ་པ་དང་འདུན་པ་ལ་སོགས་པ་མ་གྲུབ་པའོ། །

[Block 2982]
དེ་བས་ན་འདིར༌[^2040]ལམ་དུ་འགྲོ་བ་ཡིན་གྱི་རྣམ་པར་ཤེས་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2983]
དེ་ནི་བརྡ་ཕྲད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དཔེར་ན་གོ་བར་བྱ་བ་གཞན་ལ་གོ་བར་གྲུབ་པ་ཁོ་ནར་འགྱུར་གྱི་མ་གྲུབ་ན་ནི་ཕྱེད་ཉིད་ཡིན་པ་དེ་བཞིན་དུ་རིག་པའི་སྐྱེས་པ་ཡོད་པ་འདི་ལ་བརྡ་ཕྲད་ནའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2984]
ཆོམ་རྐུན་དང་ཀླ་ཀློ་ལ་སོགས་པ་ཉིད་ཀྱིས་སྐད་མ་གོ་བ་དང་གཉིད་ལོག་པ་དང་། སྨྱོས་པ་དང་། བག་མེད་པར་གྱུར་པ་དང་། སྙོམས་པར་ཞུགས་པ་དང་། གླེན་པ་དང་འོན་པར་གྱུར་པ་རྣམས་ལ་སྟོན་པ་ལ་རིག་པའི་སྐྱེས་པ་དེ་ལ་ཉེས་བྱས་དེ་ལ་འདི་བྱེད་པའོ། །

[Block 2985]
རྣམ་པ་དེ་ལྟ་བུ་ཉིད་ལ་མཚན་ཅིག་ཤོས་དོན་མེད་དོ་ཞེས་བྱ་བ་ལ། རྣམ་པ་དེ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་རྣམ་པ་གཉིས་ཉིད་ཡོད་པར་གྱུར་པ་ལའོ། །

[Block 2986]
དོན་མེད་པ་ནི་འབྲས་བུ་མེད་པ་ཅུང་ཟད་ཀྱང་མི་བྱེད་པའོ། །

[Block 2987]
བུད་མེད་ཉིད་ཉམས་པ་ལ་བུད་མེད་ཀྱི་མཚན་ལས་གཞན་ནི་སྐྱེས་པའི་མཚན་མ་སྟེ། སྐྱེས་པའི་རྣམ་པ་ཉིད་ཀྱང་ཡོད་པར་གྱུར་པ་ལ་སྐྱེས་པ་ཉིད་ནི་དོན་མེད་པ་སྟེ་སྐྱེས་པའི་མཚན་ཉམས་པ་ལས་གཞན་པ་ནི་བུད་མེད་ཀྱི་མཚན་མའོ། །

[Block 2988]
དེ་བས་ན་འཇུག་པ་འདི་རྣམས་ལ་དགེ་སློང་ལ་བུད་མེད་ཀྱི་རྣམ་པའི་མཚན་མ་བྱེད་དོ། །

[Block 2989]
སྐྱེས་པའི་རྣམ་པ་ལ་ཡང་ལ་ལར་ནི་ན་སྨད་པའོ། །

[Block 2990]
འདིར་གཞུང་ནི་མཚན་གཉིས་པ་ལ་རེག་ན་གལ་ཏེ་བུད་མེད་ཀྱི་དབང་དུ་གྱུར་པ་ཡིན་ན་དེའི་ཚེ་ན་ནི་དགེ་འདུན་གྱི་ལྷག་མའི་ལྟུང་བར་འགྱུར་རོ། །

[Block 2991]
གལ་ཏེ་སྐྱེས་པའི་དབང་དུ་གྱུར་པ་ཡིན་ན་ནི་དེའི་ཚེ་ཉེས་པ་སྦོམ་པོའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2992]
གང་ཞིག་ཁྱད་པར་མེད་པར་མཚན་གཉིས་པར་གྱུར་ན་སྦོམ་པོའི་ལྟུང་བར་གློག་པར་གྱུར་ན་དེའི་ཉམས་པར་རིག་པར་བྱའོ། །

[Block 2993]
འདིར་ཕྱེད་ཉིད་བྱེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མཚན་ཅིག་ཤོས་མོའི་མཚན་གྱི་སྐབས་འདིར་རིག་པའི་སྐྱེས་པ་ཉིད་ཀྱི་སྐྱེས་པ་དང་བུད་མེད་དང་ལྷན་ཅིག་ཏུ་ལམ་དུ་འགྲོ་བ་དང་བུད་མེད་ལ་ཆོས་སྟོན་པ་ནི་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2994]
འོག་མ་གསུམ་ལ་ལེགས་པར་སྨྲས་པ་དང་ཉེས་པར་སྨྲས་པ་དག་གིས་དོན་ཀུན་ཤེས་པ༌[^2041]དང་། གཞན་ལ་འཁྲིག་པ་བསྟེན་པར་བྱ་བའི་མཐུ་ཡོད་པ་ཉིད་ཡིན་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་ནི་འདི་ལས་འོག་མ་བསླབ་པའི་གཞི་གཉིས་པོ་དང་སྟོན་པ་གང་ཡིན་པ་གསུམ་པོ་འདི་འདོན་པའི་རིམ་པ་ལས་ཐ་མར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་ཐ་མར་བྱུང་བའོ། །

[Block 2995]
འཁྲིག་པ་ཀུན་ནས་སྨྲས་པ་དང་། བསྙེན་བཀུར་བསྔགས་པ་དང་། སྟོན་པ་རྣམས་ལ་ལེགས་པར་སྨྲས་པ་དང་། ཉེས་པར་སྨྲས་པ་དག་ལ་དོན་ཀུན་ཤེས་པ་དང་། སོ་སོར་སྟོབས་དང་ལྡན་པ་ཉིད་ལ་བུད་མེད་ལ་དངོས་གཞིའི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 2996]
གཞན་དུ་བརྗོད་པའི་གསུམ་ལས་འདིར་རེག་པ་དང་དབེན་པའི་གནས་སུ་སྟན་ལ་འདུག་པ་དང་འགྲེང་བ་གཉིས་དང་ཉལ་པོ༌[^2042]བྱེད་པར་ཤོམ་པ་དང་བཅས་པའི་ཁྱིམ་དུ་འདུག་པ་དང་། འགྲེང་བ་གཉིས་དང་ལྷན་ཅིག་ཏུ་ཉལ་བ་དང་རིག་པའི་སྐྱེས་པ་མེད་པར་བུད་མེད་དང་ལྷན་ཅིག་ལམ་དུ་འགྲོ་བ་ལའོ་ཞེས་བྱ་བ་འདིས་འཁྲིག་པ་དགག་པའི་ཕྱིར་བསྟེན་པར༌[^2043]བྱ་བ་ལ་མཐུ་ཡོད་པ༌[^2044]ཉིད་ལ་བུད་མེད་དངོས་གཞིའི་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བ་འདིར་ངག་གི་དོན་ཏོ། །

[Block 2997]
གཞན་དུ་ན་འོག་མའི་འོ་ཞེས་བྱ་བ་ནི་མཐུ་ཡོད་པར་ཇི་ལྟར་བརྗོད་པའི་དོན་འདི་ལ་འདིར་དབེན་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་འོག་མའི་ཚིག་ལ་བྱེད་པ་པོ་ཉིད་ནི་བུད་མེད་དོ་ཞེས་གང་ཞིག་མཐུ་དང་ལྡན་པ་ལས་དགེ་འདུན་ལྷག་མ་གང་ཡིན་པ༌[^2045]དེ་ལ་མཐུ་མེད་ན་ཉེས་པ་སྦོམ་པོའོ། །

[Block 2998]
གང་ཞིག་ཉེས་པ་སྦོམ་པོ་གང་ཡིན་པ་དེ་ནི་མཐུ་མེད་ན་ཉེས་བྱས་སོ། །

[Block 2999]
གང་ཞིག་མཐུ་ཡོད་པ་ལས་ལྟུང་བ་དེ་ནི་མཐུ་མེད་པ་ལ་ཉེས༌[^2046]བྱས་ཏེ་ཞེས་བྱ་བ་འདི་ལ་འདི་བྱེད་པའོ། །

[Block 3000]
མ་ནིང་མོ་དང་མ་ནིང་ཕོ་དང་སྤྲུལ་པ་མོ་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་མཐུ་མེད་པ་བཞིན་དུའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3001]
གསུམ་པོ་འདི་ལ་སྐྱེས་པའོ། །ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་རེག་པ་དང་། ཀུན་ནས་སྨྲ་བ་དང་། བསྙེན་བཀུར་བསྔགས་པ་རྣམས་ལ་སྐྱེས་པ་ཡང་དག་པར་གྱུར་པ་ལ་སྤྲུལ་པ་ལ་མཐུ་མེད་པ་ལྟར་བལྟ་བར་བྱའོ། །

[Block 3002]
གལ་ཏེ་དེ་དག་གི་བདེ་བ་ཉམས་སུ་མྱོང་བར་བྱ་བའི་འདུན་པ་ཀུན་དུ་འདོད་ཆགས་དང་ལྡན་པས་ཀྱང་ངོ་ཞེས་བྱ་བའི༌[^2047]སྒྲ་ནི་འདི་དང་འདི་ཞེས་བྱ་བའི་ཆོ་ག་ཀུན་ནས་བསྡུས་པའི་དོན་དུའོ། །

[Block 3003]
འདི་ཡང་གསུམ་པོ་འདི་རྣམས་ལ་རིག་པར་བྱའོ། །

[Block 3004]
འདིར་ལྟུང་བ་རྒྱས་པར་བཤད་པ་འདི་ལ་གསུམ་པོ་གང་ཞིག་འཆད་པར་འགྱུར་བ་ལུས་ཀྱིས་རེག་པ་དང་འཁྲིག་པ་དང་ལྡན་པ་སྨྲ་བ་དང་། བསྙེན་བཀུར་བསྔགས་པ༌[^2048]རྣམས་དེ་ལ་འདིར་དེའི་སྒྲས་བརྗོད་པའོ། །

[Block 3005]
གལ་ཏེ་དེ་དག་གི་བདེ་བ་ཉམས་སུ་མྱོང་བར་བྱ་བའི་འདུན་པ་ཀུན་དུ་འདོད་ཆགས་དང་ལྡན་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་འདུན་པའི་ཁྱད་པར་རོ། །

[Block 3006]
ཡོངས་སུ་གྱུར་པ་ཉིད་དང་བུད་མེད་དེ་ལ་ལྟོས་པ་དང་ལྡན་པ་ཉིད་དང་། ཀུན་ནས་དཀྲིས་པ་ཉིད་དང་། ཀུན་ནས་གནས་པ་ཉིད་ཅེས་བྱ་བ་གཉིས་པོ་འདི་དང་ལྡན་པའི་ཆགས་པ་གང་ཡིན་པ་དེ་ནི་འདིར་ཀུན་དུ་འདོད་ཆགས་པ་ཞེས་བྱ་བར་བརྗོད་དོ། །

[Block 3007]
གང་གི་འདུན་པ་འདི་དང་ཡང་དག་པར་ལྡན་ཏེ་གལ་ཏེ་དེས་རེག་པ་དང་། འཁྲིག་པ་དང་ལྡན་པ་སྨྲ་བ་དང་། བསྙེན་བཀུར་བསྔགས་པ་དེ་བས་ན་དགེ་འདུན་གྱི་ལྷག་མ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3008]
ཐུན་མོང་གི་མཚན་ཉིད་བསྟན་ནས། ད་ནི་རེག་པ་ལ་བསྟན༌[^2049]པ་འབའ་ཞིག་བརྗོད་པར་བྱ་སྟེ། རེག་པ་དང་སྤྲོད་པ་ལ་དགེ་འདུན་གྱི་ལྷག་མ་གང་དུ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ལུས་ཀྱི༌[^2050]རེག་པ་བདག་གིར་བྱེད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་བདག་གིར་བྱེད་པའི་དོན་འདོད་པར་གྱུར་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཡིན་ཏེ། རོ་མྱང་བ་ནི་མ་ཡིན་ནོ། །

[Block 3009]
འདོད་པར་གྱུར་པ་ཉིད་ཀྱང་སེམས་ལ་ཀུན་ནས་ཆགས་པ་ཉིད་ནི་མ་ཡིན་ཏེ། མ་ལ་སོགས་པ་རྣམས་ལ་བརྟེན་པ་ལ་སོགས་པ་ལ་ཡོད་པའི་ཕྱིར་ཏེ། དེ་བས་ན་གལ་ཏེ་དེ་དག་གི་བདེ་བ་ཉམས་སུ་མྱོང་བར་བྱ་བའི་འདུན་པ་ཀུན་དུ་འདོད་ཆགས་དང་ལྡན་པས་ཀྱང་ངོ་ཞེས་བྱ་བའི་ཁྱད་འདི་བྱས་སོ། །

[Block 3010]
འདིར་ལན་བུ༌[^2051]ནི་དེ་དང་ལྡན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། དེ་དང་ལྡན་པ་ཉིད་ནི་ལུས་དང་ལྡན་པ་ཉིད་དོ། །

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
--- END BLOCKS ---
