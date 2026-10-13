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
ཟས་དང་ལེགས་པར་བྱ་བ་དང་། ཏིང་ངེ་འཛིན་གྱི་ཁྱད་པར་དག་གིས་རྒྱས་པར་བྱས་པ་རྣམས་ནི་རྒྱས་པ་ལས་བྱུང་བ་དག་གོ། །

[Block 387]
སྒྲ་ནི་རྒྱས་པ་ལས་བྱུང་བ་དང་། རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་ཡོད་ཀྱི།

[Block 388 [VERSE]]
[^141]སྒྲ་ནི་རྣམ་སྨིན་ལས་སྐྱེས་མིན། །
རང་གི་འདོད་དགུར་འབྱུང་བའི་ཕྱིར། །
[^142]རྒྱུ་མཐུན༌[^143]ལས་བྱུང༌[^144]རྣམ་སྨིན་སྐྱེས། །

[Block 389]
ཐོགས་པ་མེད་པ༌[^145]བརྒྱད། སེམས་ཀྱི་ཁམས་བདུན་པོ་དག་དང་ཆོས་ཀྱི་ཁམས་ཏེ་སྐལ་པ་མཉམ་པ་དང་། ཀུན་དུ་འགྲོ་བའི་རྒྱུས་བསྐྱེད་པ་རྣམས་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དག་གོ། །

[Block 390]
རྣམ་པར་སྨིན་པའི་རྒྱུས་བསྐྱེད་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དག་གོ། །

[Block 391]
གཞན་རྣམ་གསུམ། ལྷག་མ་གཟུགས་དང་། དྲི་དང་། རོ་དང་། རེག་བྱའི་ཁམས་དག་སྟེ། དེ་དག་ནི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དང་། རྒྱས་པ་ལས་བྱུང་བ་དང་། རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དག་ཀྱང་ཡིན་ནོ། །

[Block 392]
རྫས་དང་ལྷན་ཅིག་འདུས་མ་བྱས་ནི་བརྟན་པའི་ཕྱིར་རྫས་སོ། །

[Block 393]
དེ་ཡང་ཆོས་ཀྱི་ཁམས་ལ་ཡོད་པས་ཆོས་ཀྱི་ཁམས་གཅིག་པུ་རྫས་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 394]
ཐ་མ་གསུམ། སྐད་ཅིག་མ་སྟེ། ཐ་མ་དེ་དག་ཡིད་ཀྱི་ཁམས་ལ་སོགས་པ་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པའི་ཚོགས་ལ་སྐད་ཅིག་མ་གཅིག་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་མ་ཡིན་པར་འགྱུར་ཏེ། དེའི་ཕྱིར་སྐད་ཅིག་མ་ཞེས་བྱའོ། །

[Block 395]
དེ་ལ་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་དང་མཚུངས་པར་ལྡན་པའི་སེམས་ནི་ཡིད་ཀྱི་ཁམས་དང་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་ཡིན་ནོ། །

[Block 396]
ལྷག་མ་དེ་དག་དང་ལྷན་ཅིག་འབྱུང་བ་རྣམས་ནི་ཆོས་ཀྱི་ཁམས་སོ། །

[Block 397 [HEADING]]
#### ལྡན་པ་ཐོབ་པ། ^1-18-13-0

[Block 398]
འདི་དཔྱད་པར་བྱ་སྟེ་གང་མིག་གི་ཁམས་དང་མི་ལྡན་པ་ལས་ལྡན་པ་ཐོབ་པ་དེ་མིག་གི་རྣམ་པར་ཤེས་པ་དང་ཡང་ཡིན་ནམ། གང་མིག་གི་རྣམ་པར་ཤེས་པ་དང་ཡིན་པ་དེ་མིག་གི་ཁམས་དང་ཡང་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ། མིག་དང་ནི། རྣམ་ཤེས་ཁམས་དག་སོ་སོ་དང་། ལྷན་ཅིག་ཏུ་ཡང་ཐོབ་པ་ཡོད། །རེ་ཞིག་སོ་སོ་ནི་མིག་གི་ཁམས་དང་ཡིན་ལ་མིག་གི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་མ་ཡིན་པ་ཡང་ཡོད་དེ། འདོད་པའི་ཁམས་ན་རིམ་གྱིས༌[^146]མིག་གི་དབང་པོ་ཐོབ་པའོ། །

[Block 399]
མིག་གི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་ཡིན་ལ། མིག་གི་ཁམས་དང་མ་ཡིན་པ་ཡང༌[^147]ཡོད་དེ། བསམ་གཏན་གཉིས་པ་ལ་སོགས་པར་སྐྱེས་པས་གཟུགས་ལྟ་ཞིང་མིག་གི་རྣམ་པར་ཤེས་པ་མངོན་དུ་བྱེད་པ་ནའོ། །

[Block 400]
ལྷན་ཅིག་ཏུ་ཡང་ནི་གཉིས་ཀ་དང་ལྡན་པ་འཐོབ་པ་ཡང་ཡོད་དེ། གཟུགས་མེད་པའི་ཁམས་ནས་ཤི་འཕོས་ནས་འདོད་པའི་ཁམས་དང་ཚངས་པའི་འཇིག་རྟེན་དུ་སྐྱེས་པ་ནའོ། །

[Block 401]
གཉིས་ཀ་དང་མ་ཡིན་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 402 [HEADING]]
#### ནང་གི་ཁམས། ^1-18-14-0

[Block 403]
ནང་གི་ཁམས་དག་ནི་དུ། ཕྱིའི་དག་ནི་དུ་ཞེ་ན། ནང་གི་བཅུ་གཉིས་གཟུགས་ལ་སོགས་མ་གཏོགས་པ༌[^148]རྣམ་པར་ཤེས་པ་དྲུག་དང་རྟེན་དྲུག་གོ། །

[Block 404]
མིག་ལ་སོགས་པ་ནི་སེམས་ཀྱི་རྟེན་ཉིད་དུ་ཉེ་བ་ཉིད་ཀྱི་ཕྱིར་ནང་གིའོ། །

[Block 405]
སེམས་ནི་ངར་འཛིན་པའི་རྟེན་ཡིན་པའི་ཕྱིར་བདག་ཏུ་ཉེ་བར་འདོགས་པའོ། །

[Block 406]
གཟུགས་ལ་སོགས་པ༌[^149]ཡུལ་གྱི་ཁམས་དྲུག་པོ་དག་ནི་ཕྱིའི་ཡིན་ནོ། །

[Block 407 [HEADING]]
#### རྟེན་པ་དང་བཅས་པ། ^1-18-15-0

[Block 408]
རྟེན་པ་དང་བཅས་པའི་ཁམས་རྣམས་ནི་དུ། དེ་དག་དང་མཚུངས་པ་རྣམས་ནི་དུ་ཞེ་ན། རེ་ཞིག་མཐའ་གཅིག་ཏུ། ཆོས་ཞེས་བྱ་བ་ནི་རྟེན་པ༌[^150]དང་བཅས། རྟེན་དང་བརྟེན་པར་དམིགས་པ་གང་རང་གི་ལས་བྱེད་པ་དེ་ནི་རྟེན་པ༌[^151]དང་བཅས་པའོ། །

[Block 409]
གང་ལ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་མཐའ་ཡས་པ་མ་སྐྱེས་པའམ། སྐྱེ་བར་མི་འགྱུར་བའི་ཆོས་ཀྱི་ཁམས་གང་ཡིན་པ་དེ་དག་ནི་འགའ་ཡང་མེད་དེ། དེ་ལྟ་བས་ན༌[^152]ཆོས་ཀྱི་ཁམས་ནི་རྟག་ཏུ་བརྟེན་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 410]
ལྷག་མ་ནི་དེ་དག༌[^153]མཚུངས་པ་དག་ཀྱང་ཡིན། །ཀྱང་ཞེས་བྱ་བའི་སྒྲ་བརྟེན་པ༌[^154]དང་བཅས་པ་དག་ཀྱང་ཡིན་པའོ། །

[Block 411]
དེ་དག་མཚུངས་པ་ཞེས་བྱ་བ་ནི༌[^155]འདི་ཅི་ཞིག་ཅེ་ན། གང་ཞིག་རང་གི་ལས་མི་བྱེད། །གང་རང་གི་ལས་མི༌[^156]བྱེད་པ་དེ༌[^157]ནི་བརྟེན་པ་དང་བཅས་པའོ་ཞེས་བཤད་པར་འགྱུར་རོ། །

[Block 412]
དེ་ལ་མིག་ལ་སོགས་པ་དག་ནི་གང་གཅིག་གི་བརྟེན་པ་དང་བཅས་པ༌[^158]དེ་ནི་ཐམས་ཅད་ཀྱི་ཡིན་ལ། གཟུགས་ལ་སོགས་པ་དག་ནི་གང་ཁོ་ནའི་དམིགས་པར་གྱུར་པ་དེ་ཁོ་ནའི་བརྟེན་པ་དང་བཅས་པ་དག་གོ། །

[Block 413]
བརྟེན་པ་དང་བཅས་པ་ནི་དངོས་པོའི་བྱེད་པ་ལ༌[^159]བརྟེན་པ་སྟེ། དེ་འདི་དག་ལ་ཡོད་པས་བརྟེན་པ་དང་བཅས་པ་རྣམས་སམ། འབྲས་བུ་ལ་རེག་པའི་ཕྱིར་བརྟེན་པ་དང་བཅས་པ་དག་གོ། །

[Block 414]
ཡང་གང་དག་བརྟེན་པ་དང་བཅས་པས༌[^160]མ་ཡིན་པ་དེ་དག་ནི་རིགས་མཐུན་པར་འདྲ་བའི་ཕྱིར་དེ་དང་མཚུངས་པ་དག་གོ། །

[Block 415 [HEADING]]
#### མཐོང་བས་སྤང་བར་བྱ་བ། ^1-18-16-0

[Block 416]
མཐོང་བས༌[^161]སྤང་བར་བྱ་བའི་ཁམས་རྣམས་ནི་དུ། བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཁམས་རྣམས་ནི་དུ། སྤང་བར་བྱ་བ་མ་ཡིན་པ་རྣམས་ནི་དུ་ཞེ་ན། རེ་ཞིག་གཟུགས་ཅན་བཅུ་ནི་བསྒོམ་པས་སྤང་བྱ་ཡིན། ལྔ་ཡང་ཡིན་ཏེ། རྣམ་པར་ཤེས་པའི་ཁམས་ལྔ་པོ་དག་གོ། །

[Block 417]
ཐ་མ་གསུམ་རྣམ་གསུམ། ཕྲ་རྒྱས་བརྒྱད་ཅུ་རྩ་བརྒྱད་དང་། །དེ་དག་དང་ལྷན་ཅིག་འབྱུང་བ་དང་། དེ་དག་གི་ཐོབ་པ་རྗེས་སུ་འབྲང་བ་དང་བཅས་པ་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 418]
ཟག་པ་དང་བཅས་པ་ལྷག་མ་དག་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 419]
ཟག་པ་མེད་པ་ནི་སྤང་བྱ་མ་ཡིན་པའོ། །

[Block 420]
སོ་སོའི་སྐྱེ་བོ་ཉིད་དང་། ངན་སོང་བའི་ལུས་དང་། ངག་གི་ལས་དག་ཀྱང་འཕགས་པའི་ལམ་དང་འགལ་བའི་ཕྱིར་མཐོང་བས་སྤང་བར་བྱ་བ་གཞན་ཡང་ཡོད་པ་མ་ཡིན་ནམ་ཞེ་ན། དེ་དག་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་མ་ཡིན་ཏེ།

[Block 421 [VERSE]]
མདོར་བསྡུ་བ་ནི་འདི་ཡིན་ནོ། །
ཉོན་མོངས་ཅན་མིན་མཐོང་སྤང་མིན། །
གཟུགས་མིན་དྲུག་པ་མིན༌[^162]སྐྱེས་མིན།[^163] །

[Block 422]
ཉོན་མོངས་པ༌[^164]ཅན་མ་ཡིན་པ་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་ཅུང་ཟད་ཀྱང་མེད་ལ། གཟུགས་ཀྱང་མ་ཡིན་ནོ། །

[Block 423]
སོ་སོའི་སྐྱེ་བོ་ཉིད་ནི་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་ལུང་དུ་མ་བསྟན་པ་ཡིན་ཏེ། དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པ་དང་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ཀྱང་དེ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 424]
ལུས་དང་ངག་གི་ལས་ནི་གཟུགས་ཡིན་ནོ། །

[Block 425]
དེ་ལྟ་བས་ན་དེ་དག་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་མ་ཡིན་ཏེ། བདེན་པ་དག་ལ་ལོག་པར་མི་རྟོག་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
