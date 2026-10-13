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
[Block 211 [HEADING]]
###### **བསླབ་པ་ཤེས་པར་བྱ་བ།** ^1-1-5-2-1-2-1-1-0

[Block 212]
བསླབ་པ་ཤེས་པར་བྱ་བ་ལ་གཉིས་ཏེ། དེ་ཁོ་ན་ཉིད་བཤད་པ་དང་།

[Block 213 [HEADING]]
###### **དེ་ཁོ་ན་ཉིད་བཤད་པ།** ^1-1-5-2-1-2-1-1-1-0

[Block 214 [HEADING]]
###### **ཡེ་ཤེས།** ^1-1-5-2-1-2-1-1-1-1-0

[Block 215]
རྣམ་པར་གཞག་པའི་ཆ་དབྱེ་བའོ། །དེ་ཁོ་ན་ཉིད་ལ་གཉིས་ཏེ།ཡེ་ཤེས་དང་ཆོས་ཉིད་དོ། །ཡེ་ཤེས་ལ་ཡང་གཉིས་ཏེ།

[Block 216 [HEADING]]
###### **རྟེན་བསྟན་པ།** ^1-1-5-2-1-2-1-1-1-1-1-0

[Block 217]
ལུས་ལ་ཡེ་ཤེས་ཆེན་པོ་གནས། །ཞེས་པ་རྟེན་བསྟན་པ་དང་།

[Block 218 [HEADING]]
###### **ཚུལ་ལམ་མཚན་ཉིད་རང་འབྱུང་ཡེ་ཤེས་སུ་བསྟན་པ།** ^1-1-5-2-1-2-1-1-1-1-2-0

[Block 219]
ལུས་གནས་ལུས་ལས་མ་སྐྱེས་པ། །ཞེས་པ་ཚུལ་ལམ་མཚན་ཉིད་རང་འབྱུང་ཡེ་ཤེས་སུ་བསྟན་པའོ། །

[Block 220 [HEADING]]
###### **ཆོས་ཉིད།** ^1-1-5-2-1-2-1-1-1-2-0

[Block 221 [HEADING]]
###### **རྟེན་བསྟན་པ།** ^1-1-5-2-1-2-1-1-1-2-1-0

[Block 222]
ཆོས་ཉིད་ལ་གཉིས་ཏེ། དངོས་པོ་ཀུན་ལ་ཁྱབ་ཅེས་པས་རྟེན་བསྟན་པ་དང་།

[Block 223 [HEADING]]
###### **ཚུལ་ལམ་མཚན་ཉིད་འདུས་མ་བྱས་ཏེ་དེ་བཞིན་ཉིད་བསྟན་པ།** ^1-1-5-2-1-2-1-1-1-2-2-0

[Block 224]
རྟོག་པ་ཐམས་ཅད་ཡང་དག་སྤངས། །ཞེས་པ་ཚུལ་ལམ་མཚན་ཉིད་འདུས་མ་བྱས་ཏེ་དེ་བཞིན་ཉིད་བསྟན་པའོ། །

[Block 225 [HEADING]]
###### **རྣམ་པར་གཞག་པའི་ཆ་དབྱེ་བ།** ^1-1-5-2-1-2-1-1-2-0

[Block 226 [HEADING]]
###### **རྟེན་བསྟན་པ།** ^1-1-5-2-1-2-1-1-2-1-0

[Block 227]
རྣམ་པར་གཞག་པའི་ཆ་དབྱེ་བ་ལ་བཞི་སྟེ། ཚིག་དང་པོས་རྟེན་བསྟན་པ་དང་།

[Block 228 [HEADING]]
###### **མཚན་ཉིད།** ^1-1-5-2-1-2-1-1-2-2-0

[Block 229]
རྟོག་པ་གཉིས༌[^141]པས་མཚན་ཉིད་དང་།

[Block 230 [HEADING]]
###### **ཡོན་ཏན།** ^1-1-5-2-1-2-1-1-2-3-0

[Block 231]
གསུམ་པས་ཡོན་ཏན་དང་།

[Block 232 [HEADING]]
###### **དེ་ཁོ་ན་ཉིད་ཀྱི་རང་བཞིན་སྐྱེ་མེད་དུ་བསྟན་པ།** ^1-1-5-2-1-2-1-1-2-4-0

[Block 233]
བཞི་པས་དེ་ཁོ་ན་ཉིད་ཀྱི་རང་བཞིན་སྐྱེ་མེད་དུ་བསྟན་པའོ། །

[Block 234 [HEADING]]
###### **བསྒོམ་པ་ཉམས་སུ་ལེན་པ།** ^1-1-5-2-1-2-1-2-0

[Block 235]
བསྒོམ་པ་ཉམས་སུ་ལེན་པ་ལ་གཉིས་ཏེ། མངོན་རྟོགས་ལམ་དུ་བྱས་པ་དང་། འབྲས་བུ་ལམ་དུ་བྱས་པའོ། །

[Block 236 [HEADING]]
###### **མངོན་རྟོགས་ལམ་དུ་བྱས་པ།** ^1-1-5-2-1-2-1-2-1-0

[Block 237 [VERSE]]
མངོན་རྟོགས་ལམ་དུ་བྱས་པ་ལ་གསུམ་སྟེ།
ཆགས་ཅན་དང་ཆགས་བྲལ་དང་ཕྱག་རྒྱ་ཆེན་པོའོ། །

[Block 238 [HEADING]]
###### **ཆགས་ཅན།** ^1-1-5-2-1-2-1-2-1-1-0

[Block 239]
དེ་ལ་ཆགས་ཅན་ནི་གཞན་ལུས་ཤེས་རབ་ལས་ཀྱི་ཕྱག་རྒྱ་ལ་བརྟེན་པ་སྟེ། དེ་ཡང་ལུས་ལ་ཞེས་པ་ནི་མཚོན་བྱེད་དབྱེར་མེད་དུ་རང་གི༌[^142]ཉམས་སུ་མྱོང་བ་སྟེ། དེ་རྟོག་པར་རང་ཤུགས་སུ་གཅོད་ཅིང་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པའོ། །དངོས་པོ་ཀུན་ལ་ཁྱབ་པ་པོ་ནི་མཚོན་བྱ་ལྷན་སྐྱེས་དོན་དམ་བདེ་བ་ལ་མི་རྟོག་པ་དང་ཀུན་རྫོབ་ཞུ་བ་དང་དབྱེར་མེད་རང་ཡང་དག་པར་རིག་པའོ། །ལུས་གནས་ལུས་ལས་མ་སྐྱེས་པ།[^143] །ཞེས་པ་ནི་མཚན་བྱ་ལྷན་སྐྱེས་ལ་འཇུག་ཚུལ་གསལ་བྱེད་ཀྱི་རྒྱུས་འཇུག་གི།[^144] འདུས་བྱས་ཀྱི་སྐྱེད་པར་བྱེད་པའི་རྒྱུས་ནི་མ་ཡིན་ནོ། །

[Block 240 [HEADING]]
###### **ཆགས་བྲལ།** ^1-1-5-2-1-2-1-2-1-2-0

[Block 241]
ཆགས་བྲལ་ནི་རང་ལུས་ཐབས་ལྡན་དམ་ཚིག༌[^145]ཕྱག་རྒྱ་སྟེ། དེ་ཡང་ལུས་ལ་ཞེས་པ་ནི་ལྟེ་བར་རྩ་གསུམ་འདུས་པ་གྲུ་གསུམ་སྐྱེ་གནས་སུའོ། །ཡེ་ཤེས་ནི་དོན་དམ་མཚོན་བྱེད་བདེ་བའོ། །གནས་ཞེས་པ་ནི་ཀུན་རྫོབ་མཚོན་བྱེད་ཞུ་བའོ། །ཡང་ན་ཡེ་ཤེས་ནི༌[^146]བདེ་བའོ། །ཆེན་པོ་ནི་སྤྱི་བོ་བདེ་ཆེན་གྱི་གནས་སོ། །གནས་ཞེས་པ་ཞུ་བ་བདེ་བ་དང་བཅས་པས༌[^147]འབབ་སྟེ་ལྟེ་བར་གནས་པའོ། །རྟོག་པ་ཐམས་ཅད་ཡང་དག་སྤངས། ། ཞེས་པ་ནི་མཚོན་བྱེད་དབྱེར་མེད་དེ། རྟོག་པ་རང་ཤུགས་སུ་སྤྱོད༌[^148]ཅིང་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པའོ། །དངོས་པོ་ཀུན་ལ་ཁྱབ་པ་པོ། །ཞེས་པ་ནི་མཚོན་བྱ་ལྷན་སྐྱེས་དོན་དམ་བདེ་བ་ལ་མི་རྟོག་པ་དང་། ཀུན་རྫོབ་ཞུ་བ་དང་དབྱེར་མེད་རང་རིག་པའོ། །ལུས་གནས་ལུས་ལས་མ་སྐྱེས་ཞེས་པ་ནི་མཚོན་བྱ་ལྷན་སྐྱེས་ལ་འཇུག་ཚུལ་གསལ་བྱེད་ཀྱི་རྒྱུ་ཡིན་ཏེ། སྐྱེད་བྱེད་ཀྱི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 242 [HEADING]]
###### **ཕྱག་རྒྱ་ཆེན་པོ།** ^1-1-5-2-1-2-1-2-1-3-0

[Block 243]
ཕྱག་རྒྱ་ཆེན་པོ་ལ་གཉིས་ཏེ་ཆགས་བྲལ་ལྟ་བུ་དང་། ཆགས་ཅན་ལྟ་བུའོ། །

[Block 244 [HEADING]]
###### **ཆགས་བྲལ་ལྟ་བུ།** ^1-1-5-2-1-2-1-2-1-3-1-0

[Block 245]
དེ་ལ་ཆགས་བྲལ་ལྟ་བུ་དེ་ཉིད་མཆོག་གི་རྣམ་འཕྲུལ་ནི། དེ་ཡང་། དངོས་པོ་ཀུན་ལ་ཁྱབ་པ་པོ། །ཞེས་པ་ནི་དོན་སྐྱེ་མེད་ཀྱིས་ཁྱབ་པའོ། །ལུས་ལ་ཡེ་ཤེས་ཆེན་པོ་གནས། །ཞེས་པ་ནི་ཤེས་བྱེད་ཀྱི་དོན་ཡང་དོན་དམ་པའི་ཡེ་ཤེས་སོ།[^149] །རྟོག་པ་ཐམས་ཅད་ཡང་དག་སྤངས། །ཞེས་པ་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་སྐྱེ་མེད་དུ་གོ་བའོ། །ལུས་གནས་ལུས་ལས་མ་སྐྱེས་ཞེས་པ་ནི་ཤེས་བྱ་ཡེ་ཤེས་དེ་ཉིད་ཀྱང་སྐྱེ་མེད་དུ་གཅིག་པར་གྱུར་པའོ། །

[Block 246 [HEADING]]
###### **ཆགས་ཅན་ལྟ་བུ།** ^1-1-5-2-1-2-1-2-1-3-2-0

[Block 247]
དེ་ལ་ཆགས་ཅན་ལྟ་བུ་ནི་གཉུག་མའི་ལུས་ཏེ་དེ་ཡང་ལུས་ཞེས་པ་ནི་གཉུག་མ་དེ་ཉིད་ལའོ། །ཡེ་ཤེས་ཆེན་པོ་ནི་ཟག་པ་མེད་པའི་ཡེ་ཤེས་སོ། །གནས་ཞེས་པ་ནི་ཞུ་བ་བསྡུས་པས་རྟག་པ་མི་འགྱུར་བར་གནས་པ་ཉིད་དོ། །རྟོག་པ་ཐམས་ཅད་ཡང་དག་སྤངས། །ཞེས་པ་ནི་ཕྱག་རྒྱ་ཆེན་པོ་མཚོན་བྱེད་རང་རིག༌[^150]སྟེ། རྟོག་པ་རང་ཤུགས་སུ་གཅོད་པ་དང་མི་རྟོག་པ་རང་རྣལ་དུ་འཇུག་པའོ། །དངོས་པོ་ཀུན་ལ་ཁྱབ་ཅེས་པ་ནི་དབང་པོ་རང་སྣང་ལ་སྦྱར་བའམ། མཚོན་བྱ་ལྷན་སྐྱེས་སོ། །ལུས་གནས་ལུས་ལས་མ་སྐྱེས་པ་ནི་གཉུག་མའི་ལུས་ལ་གནས་ཀྱང་ཐ་མལ་གྱི་ལུས་ལས༌[^151]མ་སྐྱེས་པའམ།[^152] གསལ་བྱེད་ཀྱི་རྒྱུ་ཡིན་གྱི་སྐྱེད་བྱེད་ཀྱི་རྒྱུ་མ་ཡིན་པའོ། །

[Block 248 [HEADING]]
###### **འབྲས་བུ་ལམ་དུ་བྱས་པ།** ^1-1-5-2-1-2-1-2-2-0

[Block 249]
འབྲས་བུ༌[^153]ལམ་དུ་བྱས་པ་ནི་སྐུ་བཞི་སྟེ། ཚིག་དང་པོ་ལོངས་སྐུའོ། །ཚིག་གཉིས་པ་ནི་ཆོས་སྐུའོ། །གསུམ་པ་སྤྲུལ་སྐུའོ། །བཞི་པ་ནི་བདེ་བ་ཆེན་པོའི་སྐུའོ། །

[Block 250 [HEADING]]
###### **རྟེན་རྡོ་རྗེའི་ལུས་ལམ་དུ་བྱེད་པ།** ^1-1-5-2-1-2-2-0
--- END BLOCKS ---
