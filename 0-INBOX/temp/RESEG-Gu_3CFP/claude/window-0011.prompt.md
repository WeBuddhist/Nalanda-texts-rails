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
[Block 386]
དེ་ལྟ་བུའི་བསོད་ནམས་དང་ཡེ་ཤེས་དེ་ཡང་མདོར་བསྡུ་ན་རྣམ་པ་དྲུག་ཏུ་འགྱུར་རོ་ཞེས་བྱ་བ་ནི། ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གི་མཚན་ཉིད་དོ། །

[Block 387]
ཡང་ན་བསོད་ནམས་དང་བསོད་ནམས་ཀྱི་ཕྱོགས་དང་། བརྩོན་འགྲུས་དང་། བསམ་གཏན་དང་། ཡེ་ཤེས་དང་ཡེ་ཤེས་ཀྱི་ཕྱོགས་དང་། བརྩོན་འགྲུས་དང་བསམ་གཏན་ཞེས་བྱ་བའོ། །

[Block 388]
བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་འབྲས་བུ་ནི་མདོར་བསྡུ་ན་ཅི་རིགས་པར་རྣམ་པ་བཞིར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། བསོད་ནམས་ཀྱི་འབྲས་བུ་རྣམ་པ་གཉིས་ནི་གནོད་པ་མེད་པར་འཁོར་བ་ན་འཁོར་ཞིང་སྡུག་བསྔལ་པ་དག་གིས་ཤིན་ཏུ་གཟིར་བ་མེད་པ་དང་། ཇི་ལྟར་དགའ་བར་སེམས་ཅན་གྱི་དོན་དང་ཕན་འདོགས་པར་ནུས་པ་ཞེས་བྱ་བའོ། །

[Block 389]
ཡེ་ཤེས་ཀྱི་འབྲས་བུ་རྣམ་པ་གཉིས་ནི་ཡེ་ཤེས་ལ་བརྟེན་ནས་ཡང་དག་པར་བསོད་ནམས་ཡོངས་སུ་འཛིན་པ་དང་། མཁས་པར་བྱ་བ་རྣམ་པ་སྣ་ཚོགས་དཔག་ཏུ་མེད་པ་དག་གིས་ཀྱང་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བའི་བར་དུའོ། །

[Block 390]
གང་རྣམ་པར་སྨིན་པ་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ནི་བསོད་ནམས་ལ་བརྟེན་པའོ། །

[Block 391]
རྣམ་པར་སྨིན་པའི་འབྲས་བུ་གང་ཡིན་པ་ནི་བསོད་ནམས་ལས་བྱུང་བ་ཡིན་ནོ། །

[Block 392]
བསོད་ནམས་ཀྱང་ཡེ་ཤེས་ལ་བརྟེན་ཅེས་བྱ་བ་ནི། ཡེ་ཤེས་ལ་བརྟེན་ནས་འབྱུང་བའོ། །

[Block 393]
ཡེ་ཤེས་ལས་བྱུང་བ་ཡིན་ཞེས་བྱ་བ་ནི། ཡེ་ཤེས་ཉིད་ལས་འབྱུང་བའོ། །

[Block 394]
རིག་པའི་བཟོ་དང་ལས་ཀྱི་གནས་ཞེས་བྱ་བ་ནི། རིག་པ༌[^232]ཉིད་དང་ལྡན་པའི་བཟོ་དང་ལས་ཀྱི་གནས་སྐྱེས་བུའི་བྱེད་པ་སྟེ། གང་དེ་ནི་ལུང་དུ་མ་བསྟན་པ་ཉིད་ཀྱིས་ཕ་རོལ་གྱི་ནི༌[^233]མ་ཡིན་ནོ། །

[Block 395]
ལོངས་སྤྱོད་བསྒྲུབས་པ་སྟེ། བཟའ་བ་དང་། བཏུང་བ་དང་བགོ་བ་ལ་སོགས་པ་ལོངས་སྤྱད་པར་བྱ་བ་བཟུང་བ་རྣམས་སོ། །

[Block 396]
ཚོད་མ་ཟིན་པར་ལོངས་སྤྱོད་པས་ནི་ཕ་རོལ་དུ་ཡང་འབྲས་བུ་མི་འདོད་པར་འགྱུར༌[^234]ལ། མཐོང་བའི་ཆོས་ལ་ཡང་ཚོད་མ་ཟིན་པར་ལོངས་སྤྱོད་པས་ནད་ལ་སོགས་པ་འབྱུང་བ་དང་མཐོང་བའི་ཆོས་ཀྱི་དོན་ཡང་ཉམས་པར་འགྱུར་བའོ། །

[Block 397]
སྔོན་གྱི་ལས་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། འབྲས་བུ་འདོད་པའི་ལས་བཟུང་བས་མི་འདོད་པའི་འབྲས་བུ་མེད་པ་ཉིད་དོ། །

[Block 398]
འབྲས་བུ་ཚེ་འདི་ལ་ལོངས་སྤྱོད་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི། སྦྱིན་པ་མི་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་ཕ་རོལ་གྱི་དོན་མེད་པར་འདིའི་དོན་དུ་སྟེ། གཞན་གྱི་དོན་སྒྲུབ་པའི་དོན་ནི་ཕ་རོལ་གྱི་དོན་ཡིན་པས་དེའི་ངོ་བོ་བསྟན་པའི་དོན་དུའོ། །

[Block 399]
དེ་བཞིན་གཤེགས་པར་འགྱུར་བ་ཞེས་བྱ་བའི་ཚིག་ནི། བྱང་ཆུབ་སེམས་དཔའ་འདི་ཉིད་དུ་མྱ་ངན་ལས་འདའ་བ་བརྩལ་བའི༌[^235]དོན་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་དེ་ལྟ་བུའི་ཚུལ་གྱིས༌[^236]ཕ་རོལ་དུ་ཡང་གོང་ནས་གོང་དུ་སྐྱེ་བའི་ཁྱད་པར་ཐོབ་པའོ། །

[Block 400]
ཆོས་འདུས་བས༌[^237]ཞེས་བྱ་བ་ནི། ལམ་ཡང་གཟིངས་དང༌[^238]འདྲ་བའི་ཕྱིར་ཡོངས་སུ་གཏང་བར༌[^239]བྱ་བ་ཉིད་ཡིན་ལ། འདུས་མ་བྱས་ནི་ཕ་རོལ་དུ་ཡང་ཡིན་པས་བྱང་ཆུབ་སེམས་དཔའ་ཇི་ལྟ་བ་བཞིན་དུ་གཞན་གྱི་ཡང་ཡིན་ལ། ཇི་ལྟར་བཤད་པའི་མཚན་ཉིད་ཅན་གྱིས༌[^240]མཐོང་བའི་ཆོས་ཅན་ཉིད་ནི་རང་གི་དོན་ཏོ། །

[Block 401]
དེ་བཞིན་དུ་གཞན་ཡང༌[^241]བྱང་ཆུབ་སེམས་དཔས་བཏུལ་བ༌[^242]རྣམས༌[^243]གཞན་གྱི་དོན་ཡང་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། ཅི་ཐམས་ཅད་ཀྱང་དེ་ལྟར་རམ་ཞེ་ན། སྨྲས་པ། གང་དག་བྱང་ཆུབ་སེམས་དཔས་བཏུལ་བ་སྟེ། གང་བྱང་ཆུབ་སེམས་དཔས་བཏུལ་བ་དེ་རྣམས་ཉིད་དེ། དེ་ལ་ལྟོས་ནས་དེ་དག་ཉིད་ལས༌[^244]གཞན་ཞེས་བརྗོད་ཀྱི་གཞན་ཐམས་ཅད་ཀྱི་ནི་མ་ཡིན་ནོ། །

[Block 402]
དེ་ལ་ཕྱི་མ་ལ་འདོད་པའི་ཁམས་སུ་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པར་འགྱུར་བ་ཞེས་བྱ་བ་ལ། འདིར་འདོད་པའི་ཁམས་སུ༌[^245]སྨོས་པ་ནི། འདོད་པའི་ཁམས་ལས་གཞན་པ་ན། ཕྱི་མ་ལ་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པ་མེད་དོ།[^246] །ལོངས་སྤྱོད་ཀྱི་ས་ལས་ཤིན་ཏུ་འདས་པས་སོ། །

[Block 403]
ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པའི་ཚིག་ནི་ཕུན་སུམ་ཚོགས་པ་གཞན་ནི་རྣམ་པར་སྨིན་པ་མ་ཡིན་པ་ཉིད་དེ། ལུས་ཕུན་སུམ་ཚོགས་པ་འཆད་པར་འགྱུར་བའི་བར་དུའོ། །

[Block 404]
ཕྱི་མ་ཞེས་སྨོས་པ་ནི། འདི༌[^247]ནི་ཕ་རོལ་གྱི་མ་ཡིན་པ་ཉིད་དེ། དེ་ལྟར་འདི་ལུས་ཕུན་སུམ་ཚོགས་པར་ནི་འདོད་པའི་ཁམས་དང་། གཞན་པ་དག་ཁྱད་པར་མེད་པར་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 405]
དེའི་ཕྱི་མ་ལ་ལོངས་སྤྱོད་དང་ལུས་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་ནི། འདོད་པའི་ཁམས་ཀྱི་སྔར་བསྟན་པའི་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 406]
ཚེ་འདི་ལ་སྡུག་བསྔལ་དང་བཅས་ཡིད་མི་བདེ་བ་དང་བཅས་ཞེས་བྱ་བ་ནི། བདེ་བ་དང་ཡིད༌[^248]བདེ་བ་དང་མཚུངས་པར་ལྡན་པའི་རྒྱུ་མཐོང་བའི་ཆོས་ཉིད་ལ་བརྟེན་པའོ། །

[Block 407]
སོ་སོར་བརྟགས༌[^249]ཤིང་ཞེས་བརྗོད་པ་ནི། གང་གིས་སྡུག་བསྔལ་དང་བཅས་པ་དང་ཡིད་མི་བདེ་བ་དང་བཅས་པ་དེས་མ་འོངས་པ་ནི་འབྲས་བུ་འདོད་པ་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་དེ་ལ་བརྟེན་པར་སོ་སོར་བརྟགས་ཤིང་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 408]
གང་ཡང་ཚེ་འདི་ལ་བདེ་བ་དང་བཅས་པ་དང་ཡིད༌[^250]བདེ་བ་དང་བཅས་པས་ལོངས་སྤྱོད་དང་ལུས་ཕུན་སུམ་ཚོགས་པར་འགྱུར་བའི༌[^251]རྒྱུ་ལ་བརྟེན་པ་ཞེས་བྱ་བ་དེ་ལ། འདོད་པའི་ཁམས་ལས་གཞན་པ་མ་ཡིན་པ་དེའི་ཕྱིར་འདོད་པའི་ཁམས་བྱེ་བྲག་ཏུ་བརྗོད་པར་བྱའོ། །

[Block 409]
གང་འདིར་ཉམས་པར་འགྱུར་བའི་ཆ་དང་མཐུན་པ་མ་ཡིན་པའི་བསམ་གཏན་དང་། གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པ་ཞེས་བྱ་བ་དེ་ལ། འདིར་ཞེས་སྨོས་པའི༌[^252]འདོད་པའི་ཁམས་བཟུང་བའི་དོན་ཏེ། གཞན་དག་ན་བསམ་གཏན་དང་གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པ་ཕྱི་མ་ལ་མེད་པས་སོ། །

[Block 410]
ཉམས་པར་འགྱུར་བའི་ཆ་དང་མཐུན་པ་མ་ཡིན་པ་སྨོས་པ་ནི་ཉམས་པར༌[^253]འགྱུར་བའི་ཆ་དང་མཐུན་པ་མ་ཡིན་པའི་ཕྱིར་བསམ་གཏན་དང་གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པ་ནི་མ་འོངས་པའི་ཉིད་དེ། དེས༌[^254]དེ་ལ་འབྲས་བུ་སྟེར་བས་སོ། །

[Block 411]
བསམ་གཏན་དང་གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པ་སྨོས་པ་ནི། དེ་ལས་གཞན་པའི་སྙོམས་པར་འཇུག་པ་རྣམས་ལ་ཕྱི་མ་ལ་ཕན་པ་མེད་པ་ཉིད་དེ་སྲིད་པ་སྒྲུབ་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 412]
སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱི་འཇིག་རྟེན་པའི་དག་པ་ཞེས་བྱ་བ་ལ། འདིར་སོ་སོའི་སྐྱེ་བོ་སྨོས་པ་ནི་འཇིག་རྟེན་པའོ། །

[Block 413]
འཕགས་པ་རྣམས་ཀྱི་དག་པ་ནི་གཏན་དུ་བ་ཉིད་དེ། བདེན་པ་མཐོང་བ་བསྒོམས་པས༌[^255]སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་སྤངས་པ༌[^256]ནི། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ལམ་དག་གིས་ཡིན་པས་སོ། །

[Block 414]
ཉོན་མོངས་པ་ཐམས་ཅད་གཏན་སྤངས་པ་ཞེས་བྱ་བ་ལ། འདིར་ཐམས་ཅད་གཏན་ཞེས་སྨོས་པ༌[^257]ནི་འཇིག་རྟེན་པའི་ལམ་གྱིས༌[^258]ནི་ཉོན་མོངས་པ་མགོ་མནན༌[^259]པ་ཙམ་དུ་སྤོང་གི༌[^260]གཏན་དུ་ནི་མ་ཡིན་པ་ཉིད་དེ། འདི་ལྟར་དེས་སྤངས་པའི་ཉོན་མོངས་པ་རྣམས་ཐམས་ཅད་དུ་སྤངས་པ་མ་ཡིན་ཏེ། འཇིག་རྟེན་པའི་ལམ་གྱིས༌[^261]སྲིད་པའི་རྩེ་མོ་པའི་ཉོན་མོངས་པ་མི་སྤོང་བས་ཉོན་མོངས་པ་གཏན་སྤངས་པ་མ་ཡིན་ཏེ། བག་ལ་ཉལ་མ་སྤངས་པས་སོ། །

[Block 415]
བདག་དང་གཞན་གྱི་དོན་རིམ་པར་ཕྱེ་བ་འདིའི་བསྡུས་པའི་དོན་གྱི་རིམ་པ་མ་བསྟན་པ་ནི། བསྟན་པའི་དོན་གྱི་ཚིགས་སུ་བཅད་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 416]
འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་ཞེས་བྱ་བ་ལ། དེ་ནི་གཏན་དུ་བ་ཡིན་པའི་ཕྱིར་ཡོངས་སུ་མི་ཉམས་པ་ཉིད་དོ། །

[Block 417]
དེ་ལ་བརྟེན་ནས་ཞེས་བྱ་བ་ནི། འཇིག་རྟེན་ལས་འདས་པའི་ལམ་ལ་བརྟེན་ནས་སོ། །

[Block 418]
བདག་དང་གཞན་གྱི་དོན་རྣམ་པ་བཅུའི་བསྡུས་པའི་དོན་ནི། རྒྱུན་ཉིད་དང་། རྗེས་སུ་འབྲེལ་པ་ཉིད་དང་། རྒྱུ་དང་འབྲས་བུ་ཉིད་དང་། མཐོང་བའི་ཆོས་དང་། ཕ་རོལ་གྱི་བྱེ་བྲག་ཉིད་དང་། རྟག་པ་དང་མི་རྟག་པ་ཉིད་དང་། གཏན་དུ་བ་དང་གཏན་དུ་བ་མ་ཡིན་པ་ཉིད་དང་། ཇི་སྙེད་ཡོད་པ་ཉིད་དང་། ཅིག་ཤོས་ཇི་ལྟར་ཡོད་པ་ཉིད་དང་།

[Block 419]
བདག་དང་གཞན་གྱི་དོན་བཅུ་པོ་གོང་དུ་བསྟན་པ་རྣམས་ཀྱི་བསྡུས་པའི་དོན་ནི་དེ་ལྟར་འབྱུང་ངོ་། །བྱང་ཆུབ་སེམས་དཔའི་སའི་གཞིའི༌[^262]རྣལ་འབྱོར་གྱི་གནས་ལས།

[Block 420]
བདག་དང་གཞན་གྱི་དོན་རིམ་པར་ཕྱེ་བ་སྟེ་གསུམ་པའོ།། །།

[Block 421]
དེའི་ངོ་བོ་ནི་དེ་ཁོ་ན་ཉིད་དེ། དེ་ཁོ་ན་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 422]
གང་ཇི་ལྟ་བ་བཞིན་ཡོད༌[^263]པའི་ངང་ཚུལ་ཅན་དེ་ནི་ཇི་ལྟར་ཡོད་པ་སྟེ། ཇི་ལྟ་བ་བཞིན་ཡོད་པས་ཇི་ལྟར་ཡོད་པས་སོ།[^264] །དེའི་ངོ་བོ་ནི་ཇི་ལྟར་ཡོད་པ་ཉིད་དོ། །

[Block 423]
དེ་བཞིན་དུ་ཇི་སྙེད་ཡོད་པ་ལ་ཡང་རིག་པར་བྱ་བའོ།[^265] །དེ་ཁོ་ནའི་དོན་དེ་ཡང་ཞེས་བྱ་བ་ནི། བསྟན་པའི་མཚན་ཉིད་ཅན་གྱི་དེ་ཁོ་ནའི་དོན་རྣམ་པ་གཉིས་སོ། །

[Block 424]
རབ་ཏུ་དབྱེ་ན༌[^266]རྣམ་པ་བཞིར་རིག་པར་བྱ་སྟེ་ཞེས་བྱ་བ་ལ། རྣམ་པ་གཉིས་པོ་དེ་ཉིད་ལས་སོ། །

[Block 425]
འཇིག་རྟེན་གྱི་གྲགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། འཇིག་རྟེན་ལ་གྲགས་པ་ནི་འཇིག་རྟེན་གྱི་གྲགས་པའོ། །
--- END BLOCKS ---
