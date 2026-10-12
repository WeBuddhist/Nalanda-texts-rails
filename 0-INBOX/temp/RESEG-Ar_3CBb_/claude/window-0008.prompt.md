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
གང་ཞིག་ཡིན་ཞེ་ན། རྡོ་རྗེ་སེམས་དཔའ་ཡིན་ཞེས་སྦྱར་རོ། །

[Block 282]
འདི་དག་གིས་ནི་འདི་སྐད་དུ་སྟོན་པར་འགྱུར་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ༌[^153]གསུང་བ་པོ་རྡོ་རྗེ་འཆང་ཡིན་ཞེས་སྦྱར་རོ། །

[Block 283]
འདིའི་ཚད་གང་ཡིན་ཞེས་པའི་ལན་དུ།

[Block 284 [VERSE]]
ཚད་དག་ཀྱང་ནི་བཤད་བྱ་སྟེ། །
ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ།
ལེའུ་དང་དེ་བཞིན་ཆོ་ག་དང་། །

[Block 285]
ཞེས་པ་ལེའུ་བཅུ་བདུན་ཡོད་ཅེས་པ་ནི་ལེའུའི་ཚད་དོ། །

[Block 286]
ལེའུ་ལ་ཇི་ལྟ་བ་བཞིན་དུ་ཆོ་ག་ལ་ཡང་ཡོད་དོ། །

[Block 287]
འདི་ལྟར་སྨིན་པར་བྱེད་པའི་ལམ་གྱི་དབང་དུ་བྱས་པ་ནི་ཆོ་ག་ཉི་ཤུའོ། །

[Block 288]
ཆོ་ག་ལ་ཚད་ཡོད་པ་དེ་བཞིན་དུ་དུམ་བུ་ལ་ཡང་ཚད་ཡོད་དེ། [^154]དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུའི་དུམ་བུ་ལ་སོགས་པ་བཅུ་བདུན་ནོ། །

[Block 289]
དུམ་བུ་ལ་ཇི་ལྟ་བ་བཞིན་དུ་རིམ་པར་ཕྱེ་བ་ལ་ཚད་ཡོད་དེ། འདི་ལྟར་ཐུན་མོང་གི་དབང་དུ་བྱས་ན་རིམ་པ་གཉིས་སོ། །

[Block 290]
ཁྱད་པར་གྱི་དབང་དུ་བྱས་པ་ནི་རིམ་པ་ལྔ་པ་སྟེ་རྡོ་རྗེའི་བཟླས་པ་ལ་སོགས་པའོ། །

[Block 291]
ཚད་ཀྱང་ཡིན་ལ་བཞི་ཡང་ཡིན་པས། དེ་ནི་རྣམ་པ་བཞིར་འགྱུར་ཏེ། །ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱད་པར་གྱི་དབང༌[^155]དུ་ལེའུའི་ཚད་དང་ཆོ་གའི་ཚད་དང་། དུམ་བུའི་ཚད་དང་། རིམ་པའི་ཚད་དོ། །

[Block 292]
འདི་དག་གི་ཐུན་མོང་གི་ཚད་ཀྱང་གང་ཞེ་ན། རྣམ་པ་གསུམ་སྟེ། བསྡུས་པའི་ཚད་དང་། རྒྱས་པའི་ཚད་དང་། ཤིན་ཏུ་རྒྱས་པའི་ཚད་དོ། །

[Block 293]
བསྡུས་པའི་ཚད་ནི་རྣམ་པ་བཞི་སྟེ། རྟེན་གྱི་གང་ཟག་ལ་སོགས་པའོ། །

[Block 294]
རྒྱས་པའི་ཚད་ནི་རྣམ་པ་ལྔ་སྟེ། བསྒྲུབ་པར་བྱ་བ་དང་། སྒྲུབ་པར་བྱེད་པ་དང་། ཐབས་དང་། དགོས་པ་དང་སྐྱོན་ནོ། །

[Block 295]
ཤིན་ཏུ་རྒྱས་པའི་དབང་དུ་ནི་རྣམ་པ་བདུན་ཏེ། དཀྱིལ་འཁོར་དང་། སྒྲུབ་པ་དང་། དབང་དང་། དམ་ཚིག་དང་། ཕྲིན་ལས་དང་། དེ་ཁོ་ན་ཉིད་དང་གྲོགས་སོ། །

[Block 296]
དགོས་པའང་གང་ཞིག་ཡིན་ཞེས་པའི་ལན་དུ་དགོས་པ་ཡང་ནི་བཤད་བྱ་སྟེ། །ཞེས་བྱ་བ་སྨོས་ཏེ། ཞི་སོགས་བྱ་བའི༌[^156]ཆོ་ག་དང་། །ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་འདིས་ཞི་བའི་ལས་དང་། རྒྱས་པ་ལ་སོགས་པ་རྡོ་རྗེ༌[^157]བཞིན་དུ་འགྲུབ་པར་དགོངས་སོ། །

[Block 297]
དེ་བཞིན་གྲུབ་པ་བརྒྱད་དང་ནི། །ཞེས་པ་ས་འོག་གི་དངོས་གྲུབ་ལ་སོགས་པ་འདིའི་གྲུབ་པར་དགོངས་སོ། །

[Block 298]
འདི་དག་གིས་ནི་ཐུན་མོང་གི་དངོས་གྲུབ་བསྟན་ཏེ། ཐུན་མོང་གི་དངོས་གྲུབ་ཅེས་བྱ་བ་ཡང་གང་ཞིག་ཅིའི་ཕྱིར་བསྟན་ཞེ་ན།

[Block 299]
དང་པོ་ནི་བཤད་ཟིན་ཏོ། །

[Block 300]
གཉིས་པ་ལའང༌[^158]ལྷ་ཐུན་མོང་བ་ཉིད་དང་། རྫས་ཐུན་མོང་བ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^159]བརྟག་གྲང་ན། ལྷ་ཐུན་མོང་བ༌[^160]ནི་མ་ཡིན་ཏེ། ལྷ་རེ་རེའི་ཁྱད་པར་གྱི་ལས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 301]
ཁྱད་པར་གྱི་ལས་ཞེས་བྱ་བ་འདི་ཡང་འདི་ལྟར་ཞི་བའི་ལས་ལ་ནི་རྣམ་པར་སྣང་མཛད་ཀྱི་སྦྱོར་བས་སོ། །

[Block 302]
རྒྱས་པའི་ལས་ལ་ནི་རིན་ཆེན་འབྱུང་ལྡན་གྱི༌[^161]སྦྱོར་བས་སོ། །

[Block 303]
དབང་གི་ལས་ལ་ནི་སྣང་བ་མཐའ་ཡས་ཀྱི༌[^162]སྦྱོར་བས་སོ། །

[Block 304]
དྲག་པོའི་ལས་ལ་ནི་དོན་ཡོད་གྲུབ་པའི་སྦྱོར་བས་སོ། །

[Block 305]
ལས་ཐམས་ཅད་ལ་ནི་རྡོ་རྗེ་སེམས་དཔའི་སྦྱོར་བས་སོ། །

[Block 306]
དེའི་ཕྱིར་ལྷ་ཐུན་མོང་བ་མ་ཡིན་ནོ། །

[Block 307]
རྫས་ཐུན་མོང་བ་ཡང་མ་ཡིན་ཏེ། རེ་ཞིག་ཞི་བའི་རྫས་ནི་འོ་མ་དང་། མེ་ཏོག་དཀར་པོ་ལ་སོགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 308]
རྒྱས་པའི་རྫས་ནི་བ་བླ་དང་། ལྡོང་རོས་དང་། མེ་ཏོག་སེར་པོ་ལ་སོགས་པ་ཡིན་པའི༌[^163]ཕྱིར་རོ། །

[Block 309]
དབང་གི་རྫས་ནི་ཁྲག་དང་། མཚལ་དང་མེ་ཏོག་དམར་པོ་ལ་སོགས་པའི་སྦྱོར་བས་སོ། །

[Block 310]
དྲག་པོའི་ལས་ནི་དུག་དང་། སོལ་བ་ཆེན་པོ་དང་། གྲིར་ཤི་བའི་ཤ་ཁྲག་ལ་སོགས་པའི་སྦྱོར་བས་སོ། །

[Block 311]
དེ་བས་ན་རྫས་ཐུན་མོང་བ་མ་ཡིན་ནོ། །

[Block 312]
སྔགས་ཐུན་མོང་བ༌[^164]ཡང་མ་ཡིན་ཏེ། [^165]ཞི་བ་ལ་ནི་ཤཱནྟིཾ་ཀུ་རུ་ཞེས་པའི་མཐའ་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 313]
རྒྱས་པ་ལ་ནི་པུཥྚིཾ་ཀུ་རུ་ཞེས་པའི་མཐའ་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 314]
དབང་ལ་ནི་བ་ཤཾ་ཀུ་རུ་ཞེས་པའི་མཐའ་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 315]
དྲག་པོ་ལ་ནི་མཱ་ར་ཡ་ཞེས་པའི་སྔགས་མཐའ་དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 316]
དེ་བས་ན་སྔགས་ཐུན་མོང་མ་ཡིན་ནོ། །

[Block 317]
ཡིད་ལ་བྱེད་པའི་ཁྱད་པར་ཐུན་མོང་བ་ཡང་མ་ཡིན་ཏེ། ཞི་བ་ལ་ནི་བྱམས་པ་ཡིད་ལ་བྱེད་དོ། །

[Block 318]
རྒྱས་པ་ལ་ནི་སྙིང་རྗེ་ཡིད་ལ་བྱེད་དོ། །

[Block 319]
དབང་ལ་ནི་དགའ་བ་ཡིད་ལ་བྱེད་དོ། །

[Block 320]
དྲག་པོ་ལ་ནི་བཏང་སྙོམས་ཡིད་ལ་བྱེད་དོ། །
--- END BLOCKS ---
