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
[Block 246 [VERSE]]
ཞེ་སྡང་གཏི་མུག་འདོད་ཆགས་དང་། །
དམ་ཚིག་ནོར་བུའི་རིགས་དེ་བཞིན། །
དེ་དག་རིགས་ནི་ལྔ་ཉིད་དེ། །

[Block 247]
འདོད་དང་གྲོལ་བ་རབ་སྒྲུབ་བྱེད། ཅེས་འབྱུང་ངོ་། །དེའི་རྗེས་ལ་མོ་ཧ་ར་ཏི་ཞེས་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པའི་ཐིག་ལེ་ལས་སངས་རྒྱས་སྤྱན་མ་དེ་ཉིད་དུ་བསྐྱེད་པའི་ཕྱིར་སྤྲོས་ཏེ། བདག་ཏུ་གཏི་མུག་པའི་རྣམ་པར་རྟོག་པ་སྦྱངས་ཏེ༌[^148]སའི་ཁམས་ལ་མངོན་པར་ཞེན་པ་རྣམས་རྣམ་པར་སྣང་མཛད་ཀྱི་ཞིང་ལ་བཀོད་དེ། །སླར་ཡང་གཤེགས་ནས་མེའི་མཚམས་སུ་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་བཞུགས་པར་བསམ་མོ། །

[Block 248]
དེའི་རྗེས་སུ་དྭེ་ཥ་ར་ཏི་ཞེས་བྱ་བའི་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པའི་ཐིག་ལེ་ལས་མཱ་མ་ཀཱི་དེ་ཉིད་དུ་བསྐྱེད་ལ་ཆུའི་ཁམས་ལ་མངོན་པར་ཞེན་པ༌[^149]རྣམས་ཀྱི་བདག་ཏུ་ང་རྒྱལ་བའི་རྣམ་པར་རྟོག་པ་སྦྱངས་ཏེ། རིན་ཆེན་འབྱུང་ལྡན་གྱི་ཞིང་ཁམས་སུ་རྣམ་པར་དགོད༌[^150]དེ་སླར་ཡང་གཤེགས་ཤིང་བདེན་བྲལ་གྱི་མཚམས་སུ་པདྨ་དང་ཉི་མའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་བཞུགས་པར་བསམ་པར་བྱའོ། །

[Block 249]
དེའི་འོག་ཏུ་རཱ་ག་ར་ཏི་ཞེས་བྱ་བའི་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པ་ལས་གོས་དཀར་མོ་དེ་ཉིད་དུ་བསྐྱེད་དེ་ཕྱིར་སྤྲོས་ལ་མེའི་ཁམས་ལ་མངོན་པར་ཞེན་པ་རྣམས་ཀྱི་བདག་ཏུ་ཆགས་པའི་རྣམ་པར་རྟོག་པ་སྦྱངས་ཏེ། སྣང་བ་མཐའ་ཡས་ཀྱི་ཞིང་ཁམས་སུ་བཀོད་པར་བྱས་ལ། སླར་ཡང་གཤེགས་ཏེ་རླུང་གི་མཚམས་སུ་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་ལ་བཞུགས་པར་བསམ་མོ། །

[Block 250]
དེ་ནས་བཛྲ་ར་ཏི་ཞེས་བྱ་བའི་སྔགས་ཀྱི་ཚུལ་དུ་ཡོངས་སུ་གྱུར་པ་ཐིག་ལེ་ལས་ལྷ་མོ་སྒྲོལ་མ་དེ་ཉིད་དུ་བསྐྱེད་དེ་དེ་ཕྱིར་སྤྲོས་ལ་རླུང་གི་ཁམས་ལ་མངོན་པར་ཞེན་པ་རྣམས་ཀྱི་བདག་ཏུ་ལྟ་བའི་རྣམ་པར་རྟོག་པ་འཇོམས་ཤིང་དོན་ཡོད་གྲུབ་པའི་ཞིང་དུ་རྣམ་པར་དགོད༌[^151]དེ་སླར་ཡང་གཤེགས་ནས་དབང་ལྡན་གྱི་མཚམས་སུ་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་དུ་བཞུགས་པར་བསམ་མོ། །

[Block 251]
རིགས་ཀྱི་བཙུན་མོ་བཞི་པོ་དེ་དག་ཞལ་དང་ཕྱག་དང་མཚོན་ཆ་དང་སྐུ་མདོག་དང་གནས་སྟབས༌[^152]གཙོ་བོ་བཞིན་དུ་འཛིན་པ། ལྷའི་གཟུགས་ཅན་རྒྱན་ཐམས་ཅད་ཀྱིས་བརྒྱན་པ་འདོད་ཀྱང་། ཁྱད་པར་དུ་ནི་མཱ་མ་ཀཱིའི་ཕྱག་མཚན་ནི་རྡོ་རྗེས་མཚན་པའི་ཨུཏྤ་ལའོ། །

[Block 252]
ལྷ་མོ་སྒྲོལ་མའི་ཨུཏྤལ་སེར་པོའོ། །

[Block 253]
དེ་དག་ཀྱང་སྟོང་པ་ཉིད་རྣམ་པར་ཐར་པ་བཞི་དང་། ཚད་མེད་པ་བཞི་དང་། ཕྲིན་ལས༌[^153]བཞི་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་བཞི་དང་། བསྡུ་བའི་དངོས་པོ་བཞིའི་ངོ་བོ་ཉིད་དུ་ཤེས་པར་བྱའོ་ཞེས་ནང་གི་ཕོ་བྲང་གཅིག་གོ། །

[Block 254]
དེའི་ཕྱི་རོལ་ཏུ་གྲུ་བཞི་པ་དེའི་ཟུར་བཞིའི་ནང་དུ། ཛཿཧཱུཾ་བཾ་ཧོཿ །ཞེས་བྱ་བའི་སྔགས་ཀྱི་ཚུལ་དུ་ཐིག་ལེ་ཡོངས་སུ་གྱུར་པ་ལས་གཟུགས་རྡོ་རྗེ་མ་ལ་སོགས་པའི་མཆོད་པའི་ལྷ་མོ་བཞི་དེ་ཉིད་དུ་བསྐྱེད་ལ། ཕྱི་རོལ་དུ་སྤྲོས་ཏེ་གཟུགས་ལ་སོགས་པའི་མངོན་པར་ཞེན་པ་རྣམས་ལ་འདོད་པའི་ཡོན་ཏན་སྦྱངས་ཏེ། རང་གི་རིགས་ཀྱི་བདག་པོའི་ཞིང་ཁམས་སུ་བཀོད་པར་བྱས་ལ། སླར་ཡང་གཤེགས་ཏེ་སྔ་མ་བཞིན་དུ་ཟུར་བཞིར་ཟླ་བ་རྣམས་ལ་བཞུགས་པར་བསམ་མོ། །

[Block 255]
དེ་རྣམས་ཀྱི་རྩ་བའི་ཕྱག་གཡས་པའི་དང་པོ་རྣམས་ལ་མེ་ལོང་དང་རྒྱུད་མངས་དང་དྲིའི་དུང་ཆོས་དང་བདུད་རྩི་ལྔས་གང་བའི་སྣོད་བསྒོམ་པར་བྱའོ། །

[Block 256]
ལྷག་མ་ནི་སངས་རྒྱས་སྤྱན་ལ་སོགས་པ་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 257]
དེ་རྣམས་ཐླིཾ་མམ་ས་བོན་ལས་ཡོངས་སུ་རྫོགས་པ་སའི་སྙིང་པོ་དང་བྱམས་པ་དག་གིས་ཐིག་ལེའི་གཟུགས་ལས་དེ་ཉིད་དུ་སྤྲོས་ཏེ་དེའི་ཕྱི་རོལ་དུ་གཤེགས་ནས་སེམས་ཅན་ཐམས་ཅད་ཀྱི་མིག་ལ་སོགས་པའི༌[^154]དབང་པོ་ལྷའི་མིག་ཏུ་བྱས་པ་དང་། [^155]རྩ་རྒྱུས་ཀྱི་དྲ་བ་ཡང་སངས་རྒྱས་ཀྱི་སྐུ་དང་འདྲ་བར་བསྐྱེད་དེ། རང་གི་རིགས་ཀྱི་བདག་པོའི་ཞིང་ཁམས་སུ་རབ་ཏུ་བཀོད་ཅིང་སླར་ཡང་གཤེགས་ནས་ཤར་གྱི་སྣམ་བུ་ལ་ཟླ་བའི་དཀྱིལ་འཁོར་བདག་པོ་ལ་འདུད་པར་བྱེད་ཅིང་གནས་པར་བསྒོམ་མོ། །

[Block 258]
དེ་དག་རིམ་པ་བཞིན་དུ་དཀར་པོ་དང་སེར་པོར༌[^156]སྐུ་མདོག་ཤེས་པར་བྱའོ། །

[Block 259]
རྩ་བའི་ཕྱག་དང་པོའི་ཕྱག༌[^157]མཚན་ནི་རང་རང་གི་རིགས་ཀྱི་བདག་པོའི༌[^158]བཞིན་ནོ། །

[Block 260]
འོན་ཀྱང་བྱམས་པའི་ཕྱག་དུ་ནཱ་ག་གེ་སར་གྱི་ཤིང་གི་ཡལ་གའོ། །

[Block 261]
དེའི་རྗེས་སུ་ཨོཾ་གཉིས་ཐིག་ལེའི་གཟུགས་སུ་ཡོངས་སུ་གྱུར་པ་ལས་ཕྱག་ན་རྡོ་རྗེ་དང་ནམ་མཁའི་སྙིང་པོ་དེ་ཉིད་དུ་སྤྲོས་ཏེ། ཕྱི་རོལ་དུ་གཤེགས་ནས་སེམས་ཅན་ཐམས་ཅད་ཀྱི་རྣ་བ་དང་སྣའི་དབང་པོ་སྦྱངས་ཏེ་ལྷའི་དབང་པོར་བྱས་ལ། རང་གི་རིགས་ཀྱི་བདག་པོའི་ཞིང་ཁམས་སུ་གནས་པར་མཛད་ཅིང་སླར་ཡང་གཤེགས་ཏེ་ལྷའི་སྣམ་བུ་ལ་ཟླ་བའི་དཀྱིལ་འཁོར་དུ་བདག་པོ་ལ་འདུད་པ་སྔོན་དུ་འགྲོ་བར་བཞུགས༌[^159]པར་བསམ་མོ། །

[Block 262]
འདི་དག་གི་ཞལ་ལ་སོགས་པ་ནི་ལྷག་པའི་ལྷའི༌[^160]བདག་པོ་བཞིན་ནོ། །

[Block 263]
འོན་ཀྱང་ཕྱག་ན་རྡོ་རྗེ་ནག་པོ་དང་། ནམ་མཁའི་སྙིང་པོ་སེར་པོའོ། །

[Block 264]
དེའི་རྗེས་སུ༌[^161]ཧཱུཾ་དང་ཨོཾ་ས་བོན་ལས་ཐིག་ལེའི་གཟུགས་དེ་དག་ལས་བྱུང་བ༌[^162]འཇམ་དཔལ་དང་སྤྱན་རས་གཟིགས་ཀྱི་དབང་ཕྱུག་དེ་ཉིད་དུ་སྤྲོས་ཏེ་ཕྱི་རོལ་དུ་གཤེགས་ནས་སེམས་ཅན་གྱི་ལྕེ་དང་ཡིད་ཀྱི་དབང་པོ་དག་ལྷའི་རང་བཞིན་དུ་བྱས་ནས་རང་གི་རིགས་ཀྱི་བདག་པོའི་ཞིང་ཁམས་སུ་རབ་ཏུ་བཀོད་དེ། སླར་ཡང་གཤེགས་ནས་ནུབ་ཀྱི་སྣམ་བུ་ལ་ཟླ་བའི་དཀྱིལ་འཁོར་གཉིས་ཀྱི་སྟེང་དུ་རང་གི་བདག་པོ་ལ་འདུད་པ་སྔོན་དུ་འགྲོ་བར་བཞུགས་སོ། །

[Block 265]
སྐུ་མདོག་ནི་དམར་པོ་དང་དཀར་པོ་སྟེ་ལྷག་མ་ནི་བདག་པོ་བཞིན་ནོ། །

[Block 266]
དེའི་འོག་ཏུ་སཾ་དང་ཨོཾ་ས་བོན་དག་ལས་གྲུབ་པ་ཀུན་དུ་བཟང་པོ་དང་སྒྲིབ་པ་ཐམས་ཅད་རྣམ་པར་སེལ་བ་དེ་ཉིད་སྤྲོས་ཏེ། སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཡན་ལག་གི་ཚིགས་དང་། ལུས་ཀྱི་དབང་པོ་རྣམ་པར་སྦྱངས་ཏེ་ལྷའི་གཟུགས་སུ་བསྐྱེད་ལ་རང་གི་རིགས་ཀྱི་བདག་པོའི་ཞིང་ཁམས་སུ་རབ་ཏུ་བཀོད་དེ། སླར་ཡང་གཤེགས་ནས་བྱང་གི་སྣམ་བུར་ཟླ་བའི་སྟེང་དུ་བདག་པོ་ལ་འདུད་པ་མཛད་ཅིང་བཞུགས་སོ། །

[Block 267]
སྐུ་མདོག་ནི་དམར་པོ་དང་ལྗང་གུ་དག་གོ། །

[Block 268]
ལྷག་མ་ནི་བདག་པོ་བཞིན་ནོ། །

[Block 269]
བྱང་ཆུབ་སེམས་དཔའ་བརྒྱད་པོ་དེ་དག་ནི་ལེའུ་བཅུ་གཉིས་པ་ལས་ཕྱག་རྒྱ་ཆེན་པོ་ཡོངས་སུ་གྱུར་པའི་གནས་སྐབས་སུ་གསུངས་པའི་ས་བོན་ལས་ཤེས་པར་བྱའོ། །

[Block 270]
འདིར༌[^163]ཡང་འཆད་པར་འགྱུར་ཏེ། དེ་ལྟར་ལས་ཀྱི་ལམ་རྣམ་པར་དག་པ་སོ་སོར་བསྟན་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 271]
དེའི་རྗེས་སུ་ཡ་མཱནྟ་ཀྲྀཏ་ཅེས་བྱ་བའི་སྔགས་ལས་རྫོགས་པ་གཤིན་རྗེ་གཤེད་པོ་དེ་ཉིད་དུ་སྤྲོས་ཏེ་ཕྱི་རོལ་དུ་གཤེགས་ནས་ཕུང་པོའི་བདུད་དང་ཉོན་མོངས་པའི་སྒྲིབ་པ་དང་འཇིག༌[^164]ཚོགས་ལ་ལྟ་བ་དང་མ་དད་པ་རྣམ་པར་བཅོམ་སྟེ། སེམས་ཅན་ཐམས་ཅད་དད་པའི་དབང་པོ་ལ་ངེས་པར་བཀོད་དེ། སླར་ཡང་གཤེགས་ནས་ཤར་གྱི་སྒོར་པདྨ་དང་ཉི་མའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་བཞུགས་པར་བསམ་མོ། །

[Block 272]
འདིའི་རྩ་བའི་ཕྱག་གཡས་པ་ལ་ཐོ་བའོ། །

[Block 273]
སྐུ་མདོག་ནག་པོ་ལྷག་མ་རྣམས་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 274]
དེའི་འོག་ཏུ་པྲཛྙཱནྟ་ཀྲྀཏ་ཅེས་བྱ་བའི་སྔགས་ལས་རྫོགས་པའི་ཤེས་རབ་མཐར་བྱེད་དེ་ཉིད་དུ་སྤྲོས་ཏེ་ཕྱི་རོལ་དུ་གཤེགས་ནས་འཆི་བདག་གི་བདུད་དང་ཤེས་བྱའི་སྒྲིབ་པ་དང་མཐར་འཛིན་པའི་ལྟ་བ་དང་ལེ་ལོ་རྣམ་པར་འཇོམས་ཤིང་། སེམས་ཅན་ཐམས་ཅད་བརྩོན་འགྲུས་ཀྱི་དབང་པོ་ལ་རྣམ་པར་དཀོད༌[^165]དེ། སླར་ཡང་གཤེགས་ནས་ལྷོའི་སྒོར་པདྨ་དང་ཉི་མའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་བཞུགས་པར་བསམ་མོ། །

[Block 275]
རྩ་བའི་ཕྱག་གཡས་པས་དབྱུག་པ་བསྣམས་པའོ། །

[Block 276]
སྐུ་མདོག་དཀར་པོའོ། །

[Block 277]
ལྷག་མ་སྔ་མ་བཞིན་ནོ། །

[Block 278]
དེའི་འོག་ཏུ་པད་མཱནྟ་ཀྲྀཏ་ཅེས་བྱ་བའི་སྔགས་ལས་གྲུབ་པ་པདྨ་མཐར་བྱེད་དེ་ཉིད་དུ་སྤྲོས་ཏེ་ཕྱི་རོལ་དུ་གཤེགས་ནས་ཉོན་མོངས་པའི་བདུད་དང་ལས་ཀྱི་སྒྲིབ་པ་དང་ལྟ་བ་ལོག་པ་དང་བརྗེད་ངས་པ་རྣམ་པར་འཇོམས་ཤིང་། སེམས་ཅན་གྱི་ཁམས་དྲན་པའི་དབང་པོ་ལ་གནས་པར་བྱས་ནས། སླར་ཡང་གཤེགས་ཏེ་ནུབ་ཀྱི་སྒོར་པདྨ་དང་ཉི་མའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་བཞུགས་སོ། །

[Block 279]
རྩ་བའི་ཕྱག་གཡས་པས་པདྨ་བསྣམས་པའོ། །

[Block 280]
སྐུ་མདོག་དམར་པོའོ། །

[Block 281]
ལྷག་མ་ནི་བདག་པོ་བཞིན་ནོ། །

[Block 282]
དེ་ནས་བིགྷྣཱནྟ་ཀྲྀཏ་ཅེས་བྱ་བའི་སྔགས་ལས་སྐྱེས་པ་བགེགས་མཐར་བྱེད་དེ་ཉིད་དུ་སྤྲོས་ནས་ཕྱིར༌[^166]གཤེགས་ཏེ། ལྷའི་བུའི་བདུད་དང་རྣམ་པར་སྨིན་པའི༌[^167]སྒྲིབ་པ་དང་ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་དང་། གཡེང་བ་རྣམས་རྣམ་པར་འཇོམས་ཤིང་ཏིང་ངེ་འཛིན་གྱི་དབང་པོ་ལ༌[^168]སེམས་ཅན་ཐམས་ཅད་རབ་ཏུ་དགོད༌[^169]དེ། སླར་ཡང་གཤེགས་ནས་བྱང་ཕྱོགས་ཀྱི་སྒོར་པདྨ་དང་ཉི་མའི་དཀྱིལ་འཁོར་ལ་བཞུགས་སོ། །

[Block 283]
རྩ་བའི་ཕྱག་གཡས་པས་རྡོ་རྗེ་འཛིན་པ་སྐུ་མདོག་མརྒད་ལྟ་བུ་སྟེ། ལྷག་མ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 284]
ཁྲོ་བོ་དེ་རྣམས་གཡས་བརྐྱང་པ་དང་གཡོན་བརྐྱང་བ་དང༌[^170]མཉམ་པ་དང་མི་མཉམ་པའི་སྟང་སྟབས་ཀྱིས་བཞུགས་པར་བསམ་མོ། །

[Block 285]
དེའི་འོག་ཏུ་སྭཱ་ཧཱ་ཨཱཿཨོཾ་ཧཱུཾ་བྷྲཱུཾ་ས་བོན་དྲུག་ལས་རྫོགས་པ་མི་གཡོ་མགོན་དང་། དབྱུག་སྔོན་ཅན་དང་། འདོད་པའི་རྒྱལ་པོ་དང་། སྟོབས་པོ་ཆེ་དང་། གནོད་མཛེས་ཀྱི་རྒྱལ་པོ་དང་། གཙུག་ཏོར་འཁོར་ལོས་སྒྱུར་བ་སྔ་མ་བཞིན་དུ་སྤྲོས་ནས་ཕྱིར་གཤེགས་ཏེ་མིག་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པ་དྲུག་གི་རྣམ་པར་རྟོག་པའི༌[^171]དྲི་མ་སྦྱངས་ཏེ། སེམས་ཅན་གྱི་ཁམས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་དང་ལྡན་པ་དང་མངོན་པར་ཤེས་པ་དྲུག་ཐོབ་པར་བྱས་ཏེ། སླར་ཡང་གཤེགས་ཏེ་ཤར་ལ་སོགས་པའི་སྒོའི་མཚམས་རྣམས་དང་། སྟེང་དང་འོག་དག་ཏུ་བཞུགས་པར་བསམ་མོ། །
--- END BLOCKS ---
