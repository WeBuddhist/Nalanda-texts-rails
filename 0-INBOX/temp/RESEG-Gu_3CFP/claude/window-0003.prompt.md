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
[Block 106]
ད་ནི་དགེ་བ་ཆོས་སྡུད་པའི་བརྩོན་འགྲུས་ཀྱི་དབང་དུ་བྱས་ནས་བསྟན་པ་ནི། ཚོགས་ཆེན་པོའི་ནང་དུ་འགྲོ་བའམ། གཞན་དག་དང་འགྱེད་པའམ། ཕྱིར་བརྒལ་བའམ། དེ་ལས་གཞན་པའི༌[^57]ལས་དཀའ་བ་དག་ལ་ཡང་བརྟན་པ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 107]
སེམས་ཅན་གྱི་དོན་བྱ་བའི་བརྩོན་འགྲུས་ཀྱི་རྟགས་ཀྱི་དབང་དུ་བྱས་ནས་བསྟན་པ་ནི། དོན་དང་ལྡན་པའི་བརྩལ་བ༌[^58]ཆེན་པོ་དག་ལ་ཡང་སྐྱོ་བར་མི་བྱེད་ན་ཆུང་ངུ་དག་ལ་ཅི་སྨོས་ཏེ་ཞེས་བྱ་བའོ། །

[Block 108]
བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རིགས་ཀྱི་རྟགས་བསྡུས་པའི་དོན་ནི། ཏིང་ངེ་འཛིན་འདོད་པའི་སློབ་མ་གནས་ལྔ་ལ་ངེས་པར་སྦྱར་བར་བྱ་སྟེ། འདི་ལྟ་སྟེ། སེམས་རྩེ་གཅིག་པ་ཉིད་དང་། རབ་ཏུ་དབེན་པ་དང་། སྒྲིབ་པ་རྣམ་པར་སྦྱང་བ་དང་ཡིད་ལ་བྱེད་པ་གོམས་པར་བྱ་བ་དང་། སྡོམ་པ་སྲུང་ཞིང་སྤེལ་བར་བྱ་བ་སྟེ། དེ་དག་ནི་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རིགས་ཀྱི་རྟགས་ཏེ། འདི་ལ་ཆོས་ཀྱི་དོན་ལ་ངེས་པར་སེམས་པ་ནི། རང་བཞིན་གྱིས་གཡེང་བ་མི་མང་བ་ཡིན་ཞེས་བྱ་བས་ནི་སེམས་རྩེ་གཅིག་པ་ཉིད་ཀྱི་རྟགས་སོ། །

[Block 109]
དགོན་པ་དང་ནགས་ཚལ་གྱི་གནས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་རབ་ཏུ་དབེན་པའི་རྟགས་སོ། །

[Block 110]
རང་བཞིན་གྱིས་ཀྱང་ཉོན་མོངས་པ་ཤས་ཆུང་ཞིང་སྒྲིབ་པ་ཤས་ཆུང་ལ། གནས་ངན་ལེན་ཤས་ཆུང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། སྒྲིབ་པ་རྣམ་པར་སྦྱོང་བའི་རྟགས་སོ། །

[Block 111]
རབ་ཏུ་དབེན་པ་ལ་གནས་ཤིང་ཞེས་བྱ་བ་ནི། ཡིད་ལ་བྱེད་པ་གོམས་པར་བྱེད་པའི་རྟགས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 112]
མི་དགའ་བ་མེད་པ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྡོམ་པ་སྲུང་ཞིང་སྤེལ་བའི་རྟགས་ཏེ། དེ་དག་ནི་བསམ་གཏན་གྱི་ཕ་རོལ་དུ་ཕྱིན་པའི་རིགས་ཀྱི་རྟགས་སོ། །

[Block 113]
དེ་ལ་ཁྱད་པར་ནི་འདི་ཡིན་ཏེ། གོ་རིམ་བཞིན་དུ་མ་བསྟན་ཏེ་དེའི་ཏིང་ངེ་འཛིན་གྱི་སྡོམ་པ་བསྲུང་བ་དང་། སྤེལ་པ་དང་སེམས་རྩེ་གཅིག་པ་དང་། སྒྲིབ་པ་རྣམ་པར་སྦྱང་བ་དང་། ཡིད་ལ་བྱེད་པ་གོམས་པར་བྱེད་པ་ཞེས་བྱ་བ་དེ་ལྟ་བུའི་དོན་ནི་བྱང་ཆུབ་སེམས་དཔའི་དབང་དུ་བྱས་ནས་དེའི་རྗེས་སུ་འབྲངས༌[^59]ནས་བསྟན་པར་རིག་པར་བྱའོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རིགས་ཀྱི་རྟགས་རྣམས་བསྡུས་པའི་དོན་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ལེའུ་ལས་བྱང་ཆུབ་སེམས་དཔའི་ཤེས་རབ་ཀྱི་ངོ་བོ་ཉིད་བསྟན་པའོ། །ཤེས་བྱ་ཐམས་ཅད་ལ་འཇུག་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི། ཤེས་བྱ་ཐམས་ཅད་ལ་རྗེས་སུ་འཇུག་པ་དང་། གང་ཆོས་རྣམས་ལ་སོ་སོར་རྟོག་པ་སྟེ། རིག་པའི་གནས་ལྔ་ལ་དམིགས་ནས་འཇུག་པ་ཉིད་དོ། །

[Block 114]
དེའི་རྟགས་ནི་རིག་པའི༌[^60]གནས་ཐམས་ཅད་ལ་ཤེས་པ་འཇུག་པས། ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་དང་ལྡན་པའི་ཕྱིར་ཡིད་མི་རྟུལ་བ༌[^61]ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། དེ་དག་ནི་ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་དེའི་ཁྱད་པར་རྣམས་སོ། །

[Block 115]
རང་བཞིན་གྱིས་དེ་ལྟར་ཡོན་ཏན་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི། རང་བཞིན་གྱིས་ཡོན་ཏན་དང་ལྡན་པས་ཕྱིན་ཅི་ལོག་གི་ཡིད་ལ་བྱེད་པའི་སེམས་མ་དག་པ་སྤོང་བར་བྱེད་པའོ། །ཇི་ལྟ་བུ༌[^62]ཞེ་ན། སྨྲས་པ། བཟང་ལ་སྟེ། ཅང་ཤེས་ལྟ་བུར་བཟང་བའོ། །

[Block 116]
དགེ་བ་ནི་གསེར་བཟང་པོ་ལྟ་བུ་སྟེ། ཇི་ལྟར་དགེ་བ་ཞེ་ན། དཀར་པོའི་ཆོས་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 117]
བསྐྱེད་པར་དཀའ་བ་ཞེས་བྱ་བ་ནི་ཐོབ་པར་དཀའ་བའོ། །

[Block 118]
གཙོ་བོར་གྱུར་པ་ཞེས་བྱ་བ་ནི། ཐམས་ཅད་ལས་ཤིན་ཏུ་ཁྱད་པར་དུ་འཕགས་པའོ། །

[Block 119]
བསམ་གྱིས་མི་ཁྱབ་པ་ཞེས་བྱ་བ་ནི་སོ་སོ་རང་གིས་རིག་པའོ། །

[Block 120]
མི་གཡོ་བ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་ཉམས་པ་མེད་པའོ། །

[Block 121]
བླ་ན་མེད་པ་ཞེས་བྱ་བ་ནི་འདི་ལས་གཞན་པའི་གོང་མར་གྱུར་པ་མེད་པའོ། །

[Block 122]
དེ་ལས་གཞན་པའི་སེམས་ཅན་ངན་སོང་དུ་སྐྱེས་པ་རྣམས་ལས་རྒྱུའི་ཁྱད་པར་གྱིས་ཁྱད་པར༌[^63]དུ་འཕགས་པ་སྟེ། མི་དགེ་བའི་ལས་མང་དུ་མ་བྱས་པ༌[^64]དེས་ན་མྱུར་དུ་ལྡོག་པའོ། །

[Block 123]
སེམས་ཅན་རྣམས་ལ་ཚོར་བ་དྲག་པོ་བདག་གིས་མི་བསྐྱེད༌[^65]ལ། གཞན་གྱིས་བྱས་པའི་ཚོར་པས་སེམས་ཅན་རྣམས་སྡུག་བསྔལ་བ་མཐོང་ན་སྐྱོ་བ་སྐྱེད་པ་དང་། སྙིང་རྗེའི་སེམས་བསྐྱེད་པ༌[^66]སྟེ། དེ་དག་ཐམས་ཅད་ནི་རིགས་ཀྱིས་བྱས་པ་ཉིད་དོ། །

[Block 124]
དཀར་པོའི་ཆོས་དང་མི་མཐུན་པའི་ཉེ་བའི་ཉོན་མོངས་པ༌[^67]བཞི་པོའི་བསྡུས་པའི་དོན་ནི། རྒྱུ་ལས་གྱུར་པ་དང་། རྐྱེན་གྱི་མཚན་ཉིད་ཅེས་བྱ་བ་སྟེ། རྒྱུ་ལས་གྱུར་པ་ནི་གཅིག་གོ། །

[Block 125]
གསུམ་ནི་རྐྱེན་ལས་གྱུར་པའོ། །

[Block 126]
རྐྱེན་ཡང་རྣམ་པ་གཉིས་ཏེ། ཕྱིའི་དང་། ནང་གིའོ། །

[Block 127]
ཕྱི་ཡང་རྣམ་པ་གཉིས་ཏེ། བྱང་ཆུབ་འཐོབ་པ༌[^68]ལ་མི་ཕན་པ་དང་། དེ་འཐོབ་པ་ལ་བར་དུ་གཅོད་པའོ། །

[Block 128]
ནང་གི་ནི་འཚོ་བ་ལ་ལྟོས་པའི་མཚན་ཉིད་ཀྱིས་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་དང་། རིགས་ཕུན་སུམ་ཚོགས་ན་ཡང་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི༌[^69]བྱང་ཆུབ་པར་མི་ནུས་པའོ།[^70] །རྒྱུ་བཞིའི་བསྡུས་པའི་དོན་ནི། རྒྱུ་རྣམས་ལས་དང་པོ་གསུམ་ནི་རྐྱེན་ནོ། །

[Block 129]
ཐ་མའི་བཞི་པ་ནི༌[^71]རྒྱུ་སྟེ། དད་པ་དང་འདུན་པ་དང་སྐྱེད་པའི་རྐྱེན་དང་བྲལ་བ་དང་། བདག་ཉིད་ཐབས་མ་ཡིན་པ་ལ་སྦྱོར་བ་དང་། བརྩོན་འགྲུས་གཡེལ་བའོ། །

[Block 130]
རིགས་ཀྱི་ལེའུའི་བསྡུས་པའི་དོན་ནི། རིགས་ནི༌[^72]བྱང་ཆུབ་འཐོབ་པའི་རྒྱུའི་གཙོ་བོ་ཉིད་དུ་བསྒྲུབ་པ་དང་། རིགས་ཀྱི་རྣམ་གྲངས་དང་། རིགས་ཀྱི་མཚན་ཉིད་དང་། རིགས་ཀྱི་དབྱེ་བ་དང་། རིགས་གཞན་ལས་བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཁྱད་པར་དུ་འཕགས་པ་ཉིད་དང་། དེ་ཁྱད་པར་དུ་འཕགས་པའི་རྒྱུའི་ཁྱད་པར་དང་། དེའི་རྟགས་རྣམ་པར་གཞག་པ་དང་། ངན་སོང་དུ་སྐྱེས་པར་མཚུངས་ན་ཡང་དེ་ལས་གཞན་པའི་རིགས༌[^73]ལས་བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཀྱི་ཁྱད་པར་དུ་འཕགས་པ་དང་། དཀར་པོའི་ཆོས་དང་འགལ་བའི་ཉེ་བའི་ཉོན་མོངས་པ་དང་། རིགས་ཕུན་སུམ་ཚོགས་པ༌[^74]ན་ཡང་བྱང་ཆུབ་མི་ཐོབ་པའི་རྒྱུ་ཞེས་བྱ་བ་སྟེ།

[Block 131]
དང་པོ་བཞི་ནི་རིགས་གསུམ་གྱི་ཐུན་མོང་ཡིན་ནོ། །

[Block 132]
གཞན་རྣམས་ནི་བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཀྱི་ཁྱད་པར་སྟོན་པའོ།[^75] །

[Block 133]
དང་པོ་བཞི་ནི་རིགས་གཞན་ལ་ཡང་ཡོད་པས་ཐུན་མོང་གི་དོན་ཏོ། །

[Block 134]
གཉིས་པ་ནི་བསྟན་པ་འདི་ལ་དེ་ཡོད་པར་རབ་ཏུ་བསྟན་པའི་དོན་ཏོ། །

[Block 135]
རིགས་ཀྱི་མཚན་ཉིད་དང་། རིགས་ཀྱི་དབྱེ་བ་ནི་ཤེས་པར་བྱ་བའི་དོན་དུའོ། །

[Block 136]
རིགས་གཞན་ལས་ཁྱད་པར་དུ་འཕགས་པ་ཉིད་དུ་བསྟན་པས་ནི་བྱང་ཆུབ་སེམས་དཔའ༌[^76]འཇིག་རྟེན་ཐམས་ཅད་ལས་ཤིན་ཏུ་ཁྱད་པར་དུ་འཕགས་པའི་ཡོན་ཏན༌[^77]ཉིད་དུ་བསྟན་པའི་དོན་ཏོ། །

[Block 137]
དེ་ཁྱད་པར་དུ་འཕགས་པའི་རྒྱུའི་ཁྱད་པར་ནི་རྣམ་པ་བཞི་སྟེ། རྣམ་པར་གྲོལ་བ་ལས་གྱུར་པ་དང་། ཐོག་མ་དང་བར་མ༌[^78]དང་ཐ་མ་ལས་གྱུར་པ་དང་། བདེ་འགྲོར་སྐྱེས་པ་དང་། ངན་འགྲོར་སྐྱེས་པའི་ཁྱད་པར་རོ། །

[Block 138]
དེ་ལ་རྣམ་པར་གྲོལ་བ་ལས་གྱུར་པ་ནི། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་རིགས་ལས་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 139]
ཐོག་མ་དང་། བར་མ་དང་ཐ་མ་ལས་གྱུར་པ་ནི་རྣམ་པ་བཞི་སྟེ། དབང་པོ་ལས་གྱུར་པ་དང་། བསྒྲུབ་པ༌[^79]ལས་གྱུར་པ་དང་། མཁས་པ་ལས་གྱུར་པ་དང་། འབྲས་བུ་ལས་གྱུར་པའོ། །

[Block 140]
དེ་ལ་དང་པོ་ནི་དབང་པོའིའོ། །

[Block 141]
བར་མ་ནི་བསྒྲུབ༌[^80]པའིའོ། །

[Block 142]
མཁས་པ་དང་འབྲས་བུ་ནི་ཐ་མའིའོ། །

[Block 143]
བདེ་འགྲོར་སྐྱེས་པ་ལས་གྱུར་པ་ནི་ཁྱད་པར་གྱི་དབང་དུ་བྱས་པའི་རྟགས་སོ། །

[Block 144]
ངན་འགྲོར་སྐྱེས་པ་ལས་གྱུར་པའི་ཁྱད་པར་གྱི་དབང་དུ་བྱས་པ་ནི། འདི་ལ་བྱང་ཆུབ་སེམས་དཔའ་ནི་ཡུན་རིང་པོ༌[^81]ཞིག་ན་ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་ཡིན་ནོ། །

[Block 145]
དཀར་པོའི་ཆོས་དང་མི་མཐུན་པ་དང་མི་ཐོབ་པའི་རྒྱུ་ལ་རྒོལ་བ་དང་། ལན་གདབ་པ་ལས་བརྩམས་ནས། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་རང་བཞིན་གྱིས་ཡོན་ཏན་དང་ལྡན་ཞིང་དཀར་པོའི་ཆོས་དང་ལྡན་ན་གང་གིས་ན་དུས་རྟག་ཏུ་དཀར་པོའི་ཆོས་དང་མི་ལྡན་ཞེ་ན། དེ་ལྟ་བུའི་རྒོལ་བའི་ལན་གདབ་པར་གསུངས་པ། ཇི་སྲིད་དཀར་པོའི་ཕྱོགས་ཀྱི་ཆོས་དང་མི་མཐུན་པ་ཉེ་བའི་ཉོན་མོངས་པ་བཞི་ལས་མ་ལུས་པའམ་འགས་ཀྱང་ཉོན་མོངས་པར་མ་གྱུར་ན་སྐྱེད་པར་དཀའ་བ་གཙོ་བོར་གྱུར་པ་བསམ་གྱིས་མི་ཁྱབ་པ་མི་གཡོ་བ་བླ་ན་མེད་པ་དེ་བཞིན་གཤེགས་པའི་གོ་འཕང་ཐོབ་པ་ཉིད་དེ། རྒྱུའི་ངོ་བོ་དང་ལྡན་པ་ནི༌[^82]ཡིན་གྱི། གཞན་དང་ལྡན་ན་ནི༌[^83]མ་ཡིན་པས་སོ། །
--- END BLOCKS ---
