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
[Block 281]
གཉིས་མེད་ཕྱག་རྒྱ་ཆེན་པོ་ལ་གཉིས་ཏེ། བརྟེན་པ་ཆོས་ལ་འཇུག་པ་དང་། རྟེན་ནང་ནས་འཇུག་པའོ། །

[Block 282 [HEADING]]
###### **བརྟེན་པ་ཆོས་ལ་འཇུག་པ།** ^1-1-5-2-1-2-2-2-2-3-1-0

[Block 283]
བརྟེན་པ་ཆོས་ལ་འཇུག་པ་ནི་ཤེས་རབ་དང་ཐབས་དབྱེར་མེད་པའོ། །དེ་ལ་ཤེས་རབ་ནི་སྲིད་གསུམ་སྟེ་ཁམས་གསུམ་མོ། །ཡོངས་གྱུར་ནི་གཅིག་དང་དུ་མ་དང་བྲལ་བའི་སྦྱོར་བས་རང་བཞིན་མེད་པས་ཐམས་ཅད་ཡོངས་སུ་གྱུར་པའོ། །དེ་ལ་ཤེས་རབ་ཀྱི་ཇི་ལྟར་བལྟ་ཞེ་ན། དེའི་ཕྱིར། གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤང་། །ཞེས་གསུངས་སོ། །དེ་ལ་ཐབས་ཀྱི་ཇི་ལྟར་བལྟ་ཞེ་ན། ཕ་རོལ་ཕྱིན་པའི་ཐེག་པ་ལྟར་གཅིག་དང་དུ་བྲལ་ལ་སོགས་པ་སྦྱོར་བ་ལ་མི་ལྟོས་པས་ཨ་ཐ་བ་སྟེ། རྣམ་གྲངས་སམ་ཐབས་སྣང་བའི་བདག་ཉིད་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ཚད་མེད་པ་ལ་སོགས་པའི་དངོས་པོའི་མཚན་ཉིད་དུ་བརྟག་པའོ། །

[Block 284 [HEADING]]
###### **རྟེན་ནང་ནས་འཇུག་པ།** ^1-1-5-2-1-2-2-2-2-3-2-0

[Block 285]
ཡང་ན། སྲིད་གསུམ་ཡོངས་གྱུར་ཐམས་ཅད་ནི། །ཞེས་པ་ནི་ལུས་ངག་ཡིད་གསུམ་གྱི་ཁམས་གཉུག་མའི་ཨ་ཝ་དྷཱུ་ཏཱི་དེས་བསྡུས་པའོ། །གཟུང་དང་འཛིན་པ་རྣམ་པར་སྤང་།[^167] །ཞེས་པ༌[^168]ནི་དེར་སྐྱེས་པའི་ཡེ་ཤེས་ཀྱི་རྟོག་པ་གཅོད་ཅིང་མི་རྟོག་པ་སྐྱེ་བའོ། །ཐབས་ནི་ཞེས་པ་ནི་བདེ་བའི་རོར་རང་སྣང་བས་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པའོ། །ཐམས་ཅད་ཀྱི་ཞེས་པ་ནི་ཐབས་དང་ཤེས་རབ་དབྱེར་མེད་དོ། །དེ་ལྟ་བུའི་ཡེ་ཤེས་ཆེན་པོ་དེ་གང་དུ་གནས་ཤིང་བརྟེན་ཞེ་ན། དེའི་ཕྱིར། དངོས་པོའི་མཚན་ཉིད་དུ་ནི་བརྟག །ཅེས་པ་སྟེ། དངོས་པོ་ནི་བསྟན་དུ་མེད་ལ་ཐོགས་པ་མེད་པའི་གཟུགས་གཉུག་མའི་དབང་པོའོ། །མཚན་ཉིད་ནི་དེར་གནས་པའི་ཡེ་ཤེས་ཆེན་པོའོ། །དུ་ནི་བརྟག་ཅེས་པ་སྟེ་དབང་པོ་རང་སྣང་བ་དང་ཡེ་ཤེས་རང་འབར་བའི་མན་ངག་གོ། །དེ་རྣམས་ལ་ཆོ་ག་ཁ་བསྐང་བ་སྔ་མ་དང་འདྲའོ། །

[Block 286 [HEADING]]
###### **རྟགས།** ^1-1-5-2-1-2-2-3-0

[Block 287]
དེ་རྣམས་ཀྱི་རྟགས་ནི་གསུམ་སྟེ།

[Block 288 [VERSE]]
མི་འགྱུར་བ་ནི་ལྟ་བའི་རྟགས་སོ། །
དངོས་པོ་ཀུན་ལ་ཆགས་མེད་དྲོད། །
འཇིག་རྟེན་ཆོས་བརྒྱད་སྤངས་པ་ནི། །
སྤྱོད་པའི་རྟགས་སུ་ཤེས་པར་བྱ། །

[Block 289]
ཞེས་པའོ། །

[Block 290 [HEADING]]
###### **སྡོམ་པའི་དབྱེ་བ།** ^1-1-5-2-1-2-3-0

[Block 291]
སྡོམ་པའི་དབྱེ་བ་ལ་དོན་གཉིས་ཏེ། བཤད་ཚུལ་སྦྱར་བ་དང་བརྟག་པ༌[^169]ཕྱི་མའི་རྒྱུ་མཚན་བཏུ་བའོ། །

[Block 292 [HEADING]]
###### **བཤད་ཚུལ་སྦྱར་བ།** ^1-1-5-2-1-2-3-1-0

[Block 293]
བཤད་ཚུལ་སྦྱར་བ་ལ་ཡང་དོན་གསུམ་སྟེ། ངེས་པའི་ཚིག་དང་བཤད་ཚུལ་དབྱེ་བ་དང་མངོན་པར་རྟོགས་པའོ། །

[Block 294 [HEADING]]
###### **ངེས་པའི་ཚིག།** ^1-1-5-2-1-2-3-1-1-0

[Block 295]
ངེས་པའི་ཚིག་ལ་གསུམ་སྟེ། མང་བ་ཉུང་བར་སྡོམ་པ་དང་། ཕྱི་རོལ་ལུས་ལ་སྡོམ་པ་དང་། བདེ་བ་ཆེན་པོའི༌[^170]མཆོག་ཏུ་བསྟིམ་པའོ། །ཡང་གང་གིས་སྡོམ་པ༌[^171]དང་གང་དུ་སྡོམ་པ་དང་ཡང་དག་པར་སྡོམ་པའོ། །

[Block 296 [HEADING]]
###### **མང་བ་ལ་ཉུང་བར་སྡོམ་པ།** ^1-1-5-2-1-2-3-1-1-1-0

[Block 297]
དེ་ལ་མང་བ་ལ་ཉུང་བར་སྡོམ་པ་ནི་ཐབས་དང་ཤེས་རབ་ལ་སྡོམ་པ་དང་། ལུས་ངག་ཡིད་གསུམ་ལ་སྡོམ་པའོ། །

[Block 298 [HEADING]]
###### **ཕྱི་རོལ་ལུས་ལ་སྡོམ་པ།** ^1-1-5-2-1-2-3-1-1-2-0

[Block 299]
ཕྱི་རོལ་ལུས་ལ་སྡོམ་པ་ནི་འཁོར་ལོ་བཞི་ལ་སྡོམ་པའོ། །

[Block 300 [HEADING]]
###### **བདེ་བ་མཆོག་ཏུ་སྡོམ་པ།** ^1-1-5-2-1-2-3-1-1-3-0

[Block 301]
བདེ་བ་མཆོག་ཏུ་སྡོམ་པ་ནི་དགའ་བ་དང་སྐད་ཅིག་གོ།[^172] །

[Block 302 [HEADING]]
###### **བཤད་ཚུལ་དབྱེ་བ།** ^1-1-5-2-1-2-3-1-2-0

[Block 303]
བཤད་ཚུལ་དབྱེ་བ་ལ་གཉིས་ཏེ།

[Block 304 [HEADING]]
###### **བསྐྱེད་པ་ལྟར་སྦྱར་བ།** ^1-1-5-2-1-2-3-1-2-1-0

[Block 305]
བསྐྱེད་པ་ལྟར༌[^173]སྦྱར་བ་དང་རྫོགས་རིམ་མོ། །བསྐྱེད་པ་ལྷ་ལ་གཉིས་ཏེ།ལམ་ཆོ་ག་དང་འབྲས་བུའོ། །

[Block 306 [HEADING]]
###### **ལམ་ཆོ་ག།** ^1-1-5-2-1-2-3-1-2-1-1-0

[Block 307]
དེ་ལ་ལམ་ནི་ཨཱ་ལི་ཀཱ་ལི་ཡོངས་སུ་གྱུར་པ་ལས་ཟླ་བ་དང་ཉི་མའོ། །ཤེས་རབ་དང་ཐབས་སོ། །དེས་ནི་ཆོས་ཀུན་བསྡུས་ཤིང་དབྱེ་བས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 308 [HEADING]]
###### **འབྲས་བུ།** ^1-1-5-2-1-2-3-1-2-1-2-0

[Block 309]
འབྲས་བུ་ཡང་སྐུ་གསུམ་དང་རྡོ་རྗེ་གསུམ་མོ། །དེར༌[^174]ལྷ་ཀུན་གྱི་འབྲས་བུ་འདུས་པས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 310 [HEADING]]
###### **རྫོགས་རིམ།** ^1-1-5-2-1-2-3-1-2-2-0

[Block 311]
རྫོགས་པའི་རིམ་པ་ལ་གསུམ་སྟེ། གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ་དང་རང་ལུས་ཐབས་དང་ལྡན་པ་དང་དེ་ཁོ་ན་ཉིད་དང་སྦྱར་བའོ། །

[Block 312 [HEADING]]
###### **གཞན་ལུས་ཤེས་རབ་ལ་བརྟེན་པ།** ^1-1-5-2-1-2-3-1-2-2-1-0

[Block 313]
དེ་ཡང་གཞན་ལུས་ཤེས་རབ་ལ་སྦྱར་བ་ནི་ཨེ་ཝཾ་མ་ཡཱ་ལྷ་མོ་བཞི་སྟེ། དེ་ཉིད་ཕྱག་རྒྱ་བཞིའམ་ལྷན་སྐྱེས་ལ་སོགས་པའི་རྣལ་འབྱོར་མ་བཞིའོ། །དེས་ན་རྟེན་ཐམས་ཅད་དེར་འདུས་པས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 314 [HEADING]]
###### **རང་ལུས་ཐབས་དང་ལྡན་པ།** ^1-1-5-2-1-2-3-1-2-2-2-0

[Block 315]
རང་ལུས་དང་ཐབས་དང་ལྡན་པ་ནི་འཁོར་ལོ་བཞིའི་འདབ་མའི་གྲངས་དང་རྣམ་པ་སྟེ། དེར་ལུས་ཀུན་འདུས་པས་སྡོམ་པའི་དབྱེ་བའོ། །

[Block 316 [HEADING]]
###### **དེ་ཁོ་ན་ཉིད་དང་སྦྱར་བ།** ^1-1-5-2-1-2-3-1-2-2-3-0

[Block 317]
དེ་ཁོ་ན་ཉིད་དང་སྦྱར་བ་ལ་ཡང་ཐུན་མོང་དང་ཁྱད་པར་རོ། །

[Block 318 [HEADING]]
###### **ཐུན་མོང།** ^1-1-5-2-1-2-3-1-2-2-3-1-0

[Block 319]
ཐུན་མོང་ནི་བདེན་པ་བཞི་དང་སྡེ་པ་བཞི་སྟེ་སྡེ་པ་མཆོག་ཏུ་སྡོམ་པའོ། །

[Block 320 [HEADING]]
###### **ཁྱད་པར།** ^1-1-5-2-1-2-3-1-2-2-3-2-0
--- END BLOCKS ---
