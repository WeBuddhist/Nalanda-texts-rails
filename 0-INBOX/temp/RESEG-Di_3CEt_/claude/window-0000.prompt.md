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
[Block 1 [HEADING]]
## ༄༅། །དམིགས་པ་བརྟག་པའི་འགྲེལ་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅། །རྒྱ་གར་སྐད་དུ། ཨཱ་ལཾ་བ་ན་པ་རཱིཀྵ་བྲྀཏྟི། བོད་སྐད་དུ། དམིགས་པ་བརྟག་པའི་འགྲེལ་པ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [HEADING]]
## གཞུང་དངོས། ^1-0

[Block 5 [HEADING]]
### ཚིགས་བཅད་དང་པོ། ^1-1-0

[Block 6]
གང་དག་མིག་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པའི་དམིགས་པ་ཕྱི་རོལ་གྱི་དོན་ཡིན་པར་འདོད་པ་དེ་དག་ནི་དེའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རྡུལ་ཕྲ་རབ་དག་ཡིན་པའམ་དེར་སྣང་བའི་ཤེས་པ་སྐྱེ་བའི་ཕྱིར་དེ་འདུས་པ་ཡིན་པར་རྟོག་གྲང་ན། དེ་ལ་རེ་ཞིག །

[Block 7 [VERSE]]
དབང་པོ་རྣམ་པར་རིག་པའི་རྒྱུ། །
ཕྲ་རབ་རྡུལ་དག་ཡིན་མོད་ཀྱི། །
དེར་མི་སྣང་ཕྱིར་དེ༌[^1]ཡུལ་ནི། །
རྡུལ་ཕྲན་མ་ཡིན་དབང་པོ་བཞིན། །

[Block 8]
ཡུལ་ཞེས་བྱ་བ་ནི་ཤེས་པས་གང་གིས༌[^2]རང་གི་ངོ་བོ་ངེས་པར་འཛིན་པ་ཡིན་ཏེ་དེའི་རྣམ་པར་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 9]
རྡུལ་ཕྲ་མོ་དག་གི༌[^3]ནི་དེའི་རྒྱུ་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་དེ་ལྟ་མ་ཡིན་ཏེ་དབང་པོ་བཞིན་ནོ། །

[Block 10]
དེ་ལྟར་ན་རེ་ཞིག་རྡུལ་ཕྲ་མོ་དག་དམིགས་པ་མ་ཡིན་ནོ། །

[Block 11 [HEADING]]
### ཚིགས་བཅད་གཉིས་པ། ^1-2-0

[Block 12]
འདུས་པ་ནི་དེར་སྣང་བ་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་། གང་ལྟར་སྣང་དེ་དེ་ལས་མིན། །དོན་གང་ཞིག་རང་སྣང་བའི་རྣམ་པར་རིག་པ་བསྐྱེད་པ་དེ་ནི་དམིགས་པ་ཡིན་པར་རིགས་ཏེ། འདི་ལྟར་དེ་ནི་སྐྱ་བའི་རྐྱེན་ཉིད་དུ་བཤད་པས་སོ། །

[Block 13]
འདུས་པ་ནི་དེ་ལྟ་ཡང་མ་ཡིན་ཏེ། རྫས་སུ་མེད་ཕྱིར་ཟླ་གཉིས་བཞིན། །དབང་པོ་མ་ཚང་བའི་ཕྱིར་ཟླ་བ་གཉིས་མཐོང་བ་ནི་དེར་སྣང་བ་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་དེའི་ཡུལ་མ་ཡིན་ནོ། །

[Block 14]
དེ་བཞིན་དུ་རྫས་སུ་ཡོད་པ་མ་ཡིན་པ་ཉིད་ཀྱིས༌[^4]རྒྱུ་མ་ཡིན་པའི་ཕྱིར་འདུས་པ༌[^5]དམིགས་པ་མ་ཡིན་ནོ། །

[Block 15 [VERSE]]
དེ་ལྟར་ཕྱི་རོལ་གཉིས་ཀར་ཡང་། །
བློ་ཡི༌[^6]ཡུལ་དུ་མི་རུང་ངོ་། །

[Block 16]
ཡན་ལག་གཅིག་མ་ཚང་བའི་ཕྱིར་ཕྱི་རོལ་གྱི་རྡུལ་ཕྲ་མོ་དང་ཚོགས་པ་ཞེས་བྱ་བའི་དོན་ནི་དམིགས་པ་མ་ཡིན་ནོ། །

[Block 17]
འདི་ལ་ནི།

[Block 18 [HEADING]]
### ཚིགས་བཅད་གསུམ་པ། ^1-3-0

[Block 19 [VERSE]]
ཁ་ཅིག་འདུས་པའི་རྣམ་པ་དག །
སྒྲུབ་པ་ཡིན་པར་འདོད་པར་བྱེད། །

[Block 20]
དོན་ཐམས་ཅད་ནི་རྣམ་པ་དུ་མ་ཅན༌[^7]ཡིན་པས་དེ་ལ་རྣམ་པ་འགའ་ཞིག་གིས་མངོན་སུམ་ཉིད་དུ་འདོད་དོ། །

[Block 21]
རྡུལ་ཕྲ་རབ་རྣམས་ལ་ཡང་འདུས་པར་སྣང་བའི་ཤེས་པ་སྐྱེད་པའི༌[^8]རྒྱུ༌[^9]ཡོད་དོ། །

[Block 22]
རྡུལ་ཕྲན་རྣམ་པར་རྣམ་རིག་གི །དོན་མིན་སྲ་ཉིད་ལ་སོགས་བཞིན། །ཇི་ལྟར་སྲ༌[^10]ཉིད་ལ་སོགས་པ་ནི་ཡོད་བཞིན་དུ་ཡང་མིག་གི་བློའི་ཡུལ་མ་ཡིན་པ་ལྟར་རྡུལ་ཕྲ་མོ་ཉིད་ཀྱང་དེ་དང༌[^11]འདྲའོ། །

[Block 23 [HEADING]]
### ཚིགས་བཅད་བཞི་པ། ^1-4-0

[Block 24]
དེ་དག་ལྟར་ན་བུམ་པ་དང་ཁམ་ཕོར་སོགས་བློ་མཚུངས་པར་འགྱུར། བུམ་པ་དང་ཁམ་ཕོར་ལ་སོགས་པའི་རྡུལ་ཕྲ་མོ་རྣམས་ལ་ནི་མང་དུ་ཟིན་ཀྱང་ཁྱད་པར་འགའ་ཡང་མེད་དོ། །

[Block 25]
གལ་ཏེ་རྣམ་པའི་དབྱེ་བས་དབྱེ། །གལ་ཏེ་འདི་སྙམ་དུ་མགྲིན་པ་ལ་སོགས་པའི་རྣམ་པའི་ཁྱད་པར་ལས་གང་གིས་ནི༌[^12]བློའི་ཁྱད་པར་དུ་འགྱུར་བའི་ཁྱད་པར་ཡོད་དོ་སྙམ་དུ་སེམས་ན་ཁྱད་པར་འདི་ནི་བུམ་པ་ལ་སོགས་པ་ལ་ཡོད་ཀྱི།

[Block 26 [HEADING]]
### ཚིགས་བཅད་ལྔ་པ། ^1-5-0

[Block 27 [VERSE]]
དེ་ནི་རྡུལ་ཕྲན་རྫས་ཡོད་ལ། །
མེད་དེ་ཚད་དབྱེ་མེད་ཕྱིར་རོ། །

[Block 28]
རྡུལ་ཕྲ་རབ་རྣམས་ནི་རྫས་གཞན་ཡིན་དུ་ཟིན་ཀྱང་ཟླུམ་པོ་ལ་ནི་དབྱེ་བ་མེད་དོ། །

[Block 29]
དེ་ཕྱིར་དེ་རྫས་མེད་ལ་ཡོད། །རྣམ་པའི་དབྱེ་བ་ནི་ཀུན་རྫོབ་ཏུ་ཡོད་པ་དག་ཁོ་ན་ལ་ཡོད་ཀྱི་རྡུལ་ཕྲ་མོ་རྣམས་ལ་མ་ཡིན་ནོ། །

[Block 30]
བུམ་པ་ལ་སོགས་པ་ནི་ཀུན་རྫོབ་ཏུ་ཡོད་པ་ཉིད་དོ།[^13] །

[Block 31 [VERSE]]
རྡུལ་ཕྲན་ཡོངས་སུ་བསལ་ན་ནི། །
དེར་སྣང་ཤེས་པ་ཉམས་འགྱུར་ཕྱིར། །

[Block 32]
རྫས་སུ་ཡོད་པ་རྣམས་ལ་ནི་འབྲེལ་པ་ཅན་བསལ་དུ་ཟིན་ཀྱང་ཁ་དོག་ལ་སོགས་པ་བཞིན་དུ་རང་གི་བློ་འདོར་བར་བྱེད༌[^14]དོ། །

[Block 33]
དེ་ལྟ་བས་ན་དབང་པོའི་བློ་རྣམས་ཀྱི་ཡུལ་ནི་ཕྱི་རོལ་ན་མ་ཡིན་པར་འཐད་དོ། །

[Block 34 [HEADING]]
### ཚིགས་བཅད་དྲུག་པ། ^1-6-0

[Block 35 [VERSE]]
ནང་གི་ཤེས་བྱའི་ངོ་བོ་ནི། །
ཕྱི་རོལ་ལྟར་སྣང་གང་ཡིན་དེ།[^15] །

[Block 36]
དོན་ཡིན་ཕྱི་རོལ་གྱི་དོན་མེད་བཞིན་དུ་ཕྱི་རོལ་ལྟ་བུར་སྣང་བ་ནང་ན་ཡོད་པ་ཁོ་ན་དམིགས་པའི་རྐྱེན་ཡིན་ནོ། །

[Block 37]
རྣམ་ཤེས་ངོ་བོའི་ཕྱིར། །དེ་རྐྱེན་ཉིད་ཀྱང་ཡིན་ཕྱིར་རོ། །

[Block 38]
ནང་གི་རྣམ་པར་ཤེས་པ་ནི་དོན་དུ་སྣང་བ་དང་། དེ་ལས་སྐྱེས་པ་ཡིན་པས། ཆོས་ཉིད་གཉིས་དང་ལྡན་པའི་ཕྱིར་ནང་ན་ཡོད་པ་ཁོ་ན་དམིགས་པའི་རྐྱེན་ཡིན་ནོ། །

[Block 39 [HEADING]]
### ཚིགས་བཅད་བདུན་པ། ^1-7-0

[Block 40]
རེ་ཞིག་དེ་ལྟར་སྣང་བ་ཉིད་ཡིན་ལ་ནི་རག་ལ། [^16]དེའི་ཕྱོགས་གཅིག་པོ་ལྷན་ཅིག་སྐྱེས་པ་གོ་ཇི་ལྟར་རྐྱེན་ཡིན་ཞེ་ན། གཅིག་ནའང་མི་འཁྲུལ་ཕྱིར་ན་རྐྱེན། །ལྷན་ཅིག་པར་གྱུར་དུ་ཟིན་ཀྱང་འཁྲུལ་པ་མེད་པའི་ཕྱིར་གཞན་ལས་སྐྱེ་བའི༌[^17]རྐྱེན་དུ་འགྱུར་ཏེ། འདི་ལྟར་གཏན་ཚིགས་ཡོད་པ་དང་མེད་པ༌[^18]དག་ནི་ཡོད་པ་དང་མེད་པ་དག་གི་དེ་དང་ལྡན་པ་ཉིད་ན༌[^19]རྒྱུ༌[^20]དང་ལྡན་པ་རིམ་གྱིས་སྐྱེ་བ་དག་གི་ཡང་མཚན་ཉིད་ཡིན་པར་སྨྲའོ། །
--- END BLOCKS ---
