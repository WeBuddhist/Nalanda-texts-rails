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
ལེའུ་དང་པོ་ལས་ཀྱང་། རང་གི་གཟུགས་བརྙན་བུད་མེད་ཀྱི་གཟུགས་བརྙན་དུ་སྤྲུལ་ཞེས་གསུངས་སོ། །

[Block 387]
དེའི་ཕྱིར་ཐབས་དང་ཤེས་རབ་ཀྱི་ཏིང་ངེ་འཛིན་ལས་དབྱེར་མེད་པའི་ལྷ་མོ་རྣམས་ཀྱིས༌[^264]བསྟོད་དེ་ཐལ་ཆེས་པས་ཆོག་གོ། །

[Block 388 [HEADING]]
##### བཞེངས་པ་ལ་དེ་བཞིན་གཤེགས་པ་ལྔས་བསྟོད་པ། ^1-1-3-6-0

[Block 389]
དེའི་རྗེས་སུ་སྔ་མ་བཞིན་དུ་བཅོམ་ལྡན་འདས་ཞལ་དང་ཕྱག་མཚན་ཇི་ལྟ་བ་བཞིན་དུ་ཡེ་ཤེས་ཀྱི་ཕྱག་རྒྱས་འཁྱུད་པ་བཞེངས་པར་མཐོང་ནས་དེ་བཞིན་གཤེགས་པ་ལྔའི་སྒོ་ནས་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པས་བསྟོད་པར་འགྱུར་ཏེ།

[Block 390 [VERSE]]
མི་བསྐྱོད་རྡོ་རྗེ་ཡེ་ཤེས་ཆེ། །
རྡོ་རྗེ་དབྱིངས་ནི་མཁའ་ཆེན་པོ། །
རྡོ་རྗེ་གསུམ་མཆོག་དཀྱིལ་འཁོར་གསུམ། །
རྡོ་རྗེ་གསུམ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 391 [VERSE]]
རྣམ་པར་སྣང་མཛད་དགའ་ཆེན་པོ། །
རྡོ་རྗེ་ཞི་བ་དགའ་བ་ཆེ། །
རང་བཞིན་འོད་གསལ་མཆོག་གི་མཆོག །
སྟོན་པ་རྡོ་རྗེ་ཕྱག་འཚལ་བསྟོད། །

[Block 392 [VERSE]]
རིན་ཆེན་རྒྱལ་པོ་ཤིན་ཏུ་ཟབ། །
རྡོ་རྗེ་ནམ་མཁའ་དྲི་མ་མེད། །
རང་བཞིན་གྱིས་དག་གོས་པ་མེད། །
རྡོ་རྗེ་སྐུ༌[^265]ལ་ཕྱག་འཚལ་བསྟོད། །

[Block 393 [VERSE]]
རྡོ་རྗེ་འཆི་མེད་རྒྱལ་ཆེན་པོ། །
རྟོག་མེད་ནམ་མཁའ་རྡོ་རྗེ་འཛིན། །
འདོད་ཆགས་ཕ་རོལ་ཕྱིན་ཐོབ་པ། །
རྡོ་རྗེ་གསུང་ལ༌[^266]ཕྱག་འཚལ་བསྟོད། །

[Block 394 [VERSE]]
དོན་ཡོད་རྡོ་རྗེ་རྫོགས་སངས་རྒྱས། །
བསམ་པ་ཐམས་ཅད་ཡོངས་རྫོགས་པ། །
རྣམ་དག་ངོ་བོ་ལས་བྱུང་བ། །
རྡོ་རྗེ་སེམས་ལ་ཕྱག་འཚལ་ལོ། །

[Block 395 [HEADING]]
##### ཚིམ་པར་བྱེད་པའི་ཆོ་ག། ^1-1-3-8-0

[Block 396 [HEADING]]
###### ཚིམ་པར་བྱེད་པའི་ཆོ་ག་གཅིག། ^1-1-3-8-1-0

[Block 397]
དེའི་རྗེས་ལ་བསྟོད་པའི་ཚིག་ཐོས་མ་ཐག་ཏུ་ང་རྒྱལ་བརྟན་པར་གྱུར་པས་ཀྱང་གལ་ཏེ་སྐྱོ་བར་གྱུར་ན། དེའི་ཚེ་ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་གྱི་ལུས་ཚིམ་པར་བྱ་བའི་ཕྱིར་ཆོ་ག་འདི་བརྩམ་པར༌[^267]བྱ་སྟེ། མཚོགས༌[^268]མའི་བུག་པ་ནས་མཐོ་གང་ཙམ་གྱི་སྟེང་དུ་ཀུནྡ་དག་པའི་འོད་དང་མཚུངས་པའི་ཡི་གེ་ཨོཾ་རྣམ་པར་དགོད་དེ། དེ་ཡོངས་སུ་གྱུར་པའི་དྲི་མ༌[^269]མེད་པའི་ནམ་མཁའི་ཟླ་བའི་དཀྱིལ་འཁོར་དང་མཚུངས་པའི་ལྷའི་བདུད་རྩིའི་རང་བཞིན་གྱི་གཟུགས་བརྙན་རྣམ་པར་བསྒོམས་ཏེ། དེའི་དབུས་སུ་ཐུར་དུ་འཕྱང་བ་འབར་བའི་ཕྲེང་བ་ཅན་ཨོཾ་རྣམ་པར་དགོད་དེ། དེའི་འོད་ཟེར་གྱིས༌[^270]བཞུ་བར་བྱ་སྟེ། དེའི་བདུད་རྩི་འབབ་ཆུའི་རྒྱུན་གྱིས་རྣམ་པས་མཚོགས༌[^271]མའི་བུ་གའི་ལམ་ནས་འོངས་པ་དེ་རྐན་གྱི་ཕུགས་ལ་གཏད་པའི་ལྕེས་ཀུན་ཏུ་མྱང་བར་བྱས་ལ། རྩ་ཀུན་ཏུ་སྤྱོད་པའི་རིམ་པས་ཡན་ལག་དང་ཉིང་ལག་ཐམས་ཅད་རྒྱས་པར་བྱའོ། །

[Block 398]
དེ་ལྟར་བྱས་པས་བསམ་གཏན་གྱི་ཟས་ཅན་དབང་པོ་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པ། ཁམ་གྱི་ཟས་ལ་ལྟོས་པ༌[^272]མེད་ཅིང་གནས་པར་འགྱུར་རོ་ཞེས་ཚིམ་པར་བྱེད་པའི་ཆོ་ག་གཅིག་གོ། །

[Block 399 [HEADING]]
###### ཆོ་ག་གཉིས་པ། ^1-1-3-8-2-0

[Block 400]
ཆོ་ག་གཉིས་པ་ཡང་ཡོད་དེ། མཆུ་གཉིས་ཀྱི་རྩེ་མོར་ཨོཾ་ཡོངས་སུ་གྱུར་པའི་ཁ་དོག་སེར་པོ་བུམ་པ་བཟང་པོ་བཀོད་དེ། དེའི་ནང་དུ་སཾ་ཡོངས་སུ་གྱུར་པ་ལས་བདུད་རྩིས་ཁའི་བར་དུ་ཡོངས་སུ་བཀང་བ་ལ་དམིགས་ཏེ། ལྕེའི་རྩེ་མོར་ཧཱུྃ་ཕྲ་མོ་ཡོངས་སུ་གྱུར་པའི་རྡོ་རྗེ་ཕྲ་མོས་དེའི་ནང་ནས་བདུད་རྩི་བཀུག་ལ་སྔ་མ་བཞིན་དུ་ཕུང་པོ་ལ་སོགས་པ་ཚིམ་པར་བྱའོ་ཞེས་ཁྱད་པར་རོ། །

[Block 401 [HEADING]]
##### དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ཉེ་བར་བསྡུ་བ། ^1-1-3-7-0

[Block 402]
དེའི་རྗེས་སུ་ཕྱིའི་དཀྱིལ་འཁོར་ལུས་ཀྱི་དཀྱིལ་འཁོར་ལ་རབ་ཏུ་འཇུག་ཅིང་བདུད་རྩི་མྱང་བར་བྱ་སྟེ། ཡེ་ཤེས་སེམས་དཔའི་ཐུགས་ཀའི་ས་བོན་ལས་བྱུང་བའི་འོད་ཟེར་གྱི་ཚོགས་ལྕགས་ཀྱུའི་རྣམ་པས་ཕུང་པོ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་དེ་བཞིན་གཤེགས་པ་དང་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་། ཁྲོ་བོའི་འཁོར་ལོ་སྔ་མ་བཞིན་དུ་བཀུག་ལ། ཡན་ལག་དང་ཚིགས་ཐམས་ཅད་དུ་ངེས་པར་དགོད་དེ། དེ་ལས་ཀྱང་སྐུའི་རྡོ་རྗེ་འཛིན་པའི༌[^273]ངོ་བོ་ཉིད་ལྷའི་འཁོར་ལོ་སྤྱི་བོར་ཨོཾ་ལ་བསྡུ་བ་དང་། གསུང་གི་རྡོ་རྗེའི་ངོ་བོ་ཉིད་ལྷའི་འཁོར་ལོ་མགྲིན་པར་ཡི་གེ་ཨཱཿལ་བསྡུ་བ་དང་། ཐུགས་ཀྱི་རྡོ་རྗེ་འཛིན་པའི་ངོ་བོ་ཉིད་ཀྱི་ལྷའི་འཁོར་ལོ་ཐུགས་ཀ་ན་གནས་པའི་ཡི་གེ་ཧཱུྃ་ལ་བསྡུ་བར་བྱའོ། །

[Block 403]
དེའི་རྗེས་ལ་ཡི་གེ་ཨོཾ་ཨཱཿལ་ཐིམ་པ་དང་ཨཱཿཡི་གེ་ཧཱུཾ་ལ་ཐིམ་པ་དང་། ཧཱུྃ་དེ་ཉིད་ལ་ཡང་ཡེ་ཤེས་ཀྱི་ཕྱག་རྒྱ་དང་སྙོམས་པར་ཞུགས་པའི་རང་གི་ལྷའི་གཟུགས་བརྙན་བསྡུས་ཏེ།

[Block 404]
སླར་ཡང་ཧཱུཾ་དེ་ཉིད་ལ་ཁམས་གསུམ་མ་ལུས་པ༌[^274]བསྡུས་ཏེ། །དེ་ཉིད་ཡོངས་སུ་གྱུར་པ་ལས།

[Block 405]
སླར་ཡང་བདེ་བ་ཆེན་པོའི་རང་བཞིན་ཅན། རྡོ་རྗེ་འཆང་ཆེན་པོའི་གཟུགས་བརྙན་བསྒོམ་པར་བྱའོ། །ཞེས་དཔའ་བོ་གཅིག་ཏུ་བསྒོམ་པའི་བདག་ཉིད་ཅན་གྱི་འཁོར་ལོ་ཉེ་བར་བསྡུ་བའི་བསྒོམ་པའི་ཆོ་གའོ། །

[Block 406 [HEADING]]
##### ནང་གི་སྦྱིན་སྲེག་གི་ཆོ་ག། ^1-1-3-9-0

[Block 407]
དེའི་རྗེས་ལ་ཁ་དོག་སྔོན་པོ་ཡི་གེ་ཡཾ་ཡོངས་སུ་གྱུར་པ་ལས།

[Block 408]
མདུན་དུ་གཞུའི་དབྱིབས་ཅན་རླུང་གི་དཀྱིལ་འཁོར་རྣམ་པར་བསམས་ཏེ། དེའི་སྟེང་དུ་ཡི་གེ་རཾ་ཡོངས་སུ་གྱུར་པ་ལས་མེའི་དཀྱིལ་འཁོར་ཟུར་གསུམ་པ་མེའི་ཕྲེང་བས་དཀྲུགས་པར་བསམས་ལ། [^275]དེའི་སྟེང་དུ་ཡི་གེ་ཨ་དམར་པོ༌[^276]ཡོངས་སུ་གྱུར་པ་ལས་དུམ་བུ་གཅིག་པ་པདྨའི་སྣོད་བསམས་ཏེ།[^277] དེའི་དབུས་སུ་མ་ར་བི༌[^278]ཤུ་མུའི༌[^279]ས་བོན་དང་གོ་ཀུ་ད་ཧ་ན་ཞེས་བྱ་བའི་ས་བོན་ལྔ་བཀོད་དེ། ཡི་གེ་བཅུ་འདྲེས་པར་གྱུར་པས་ལྔ་རུ་སོང་བར་རྣམ་པར་བསམས་ཏེ། དེ་དག་ཡོངས་སུ་གྱུར་པ་ལས་རྟག་པ་ལ་སོགས་པའི་རང་བཞིན་ཅན་གྱི་རྫས་རྣམ་པ་ལྔ་པོ་དེའི་སྟེང་དུ་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་དེ་བཞིན་གཤེགས་པ་ལྔའི་ས་བོན་ཨོཾ་ལ་སོགས་པ་རྣམ་པར་དགོད་དེ། སྤྲོ་བ་དང་བསྡུ་བའི་རིམ་པས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རང་བཞིན་དུ་བསྒྲུབས༌[^280]ལ། ས་བོན་དང་རྫས་ཡོངས་སུ་གྱུར་པ་ལས་དེ་བཞིན་གཤེགས་པ་ལྔ་ཞལ་གསུམ་པ༌[^281]ལ་སོགས་པའི་རྣམ་པ་ཅན། སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་རང་རང་གི་ཕྱག་རྒྱ་དང་སྙོམས་པར་ཞུགས་པ་སྣ་ཚོགས་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་ལ་བཞུགས་པ་འོད་གསལ་བའི་རང་བཞིན་ཅན་བསྒོམ་པར་བྱའོ། །

[Block 409]
དེ་ནས་རྡོ་རྗེ་དང་པདྨ་སྙོམས་པར་འཇུག་པའི་དུས་སུ་དེ་རྣམས་ཀྱི་རྗེས་སུ་ཆགས་པའི་སྒྲ་དམ་པས་བཀུག་པ་དེ་བཞིན་གཤེགས་པ་རྣམས་ནང་དུ་ཞུགས་པར་བསམ༌[^282]ལ་ཞུགས་པའི་དེ་མ་ཐག་ཏུ་དེ་དག་ཞུ་ཞིང་བྱང་ཆུབ་ཀྱི༌[^283]སེམས་ཀྱི་གཟུགས་འོ་མ་ཅན་གྱི་རྒྱ་མཚོ་ལྟ་བུ་བདུད་རྩི་དེ་ཉིད་དུ་གནས་པར་བལྟ་བར་བྱའོ། །

[Block 410]
དེ་ལ་བལྟས་ཏེ་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཀྱི་རང་བཞིན་ཡི་གེ་ཧཱུཾ་གིས་སྦྱངས་པས་ཐ་མལ་པའི་རྣམ་པར་རྟོག་པ༌[^284]བཟློག་པར་བྱའོ། །

[Block 411]
ཡི་གེ་ཨཱཿསོ་སོར་རྟོག་པའི་ཡེ་ཤེས་ཀྱི༌[^285]རང་བཞིན་གྱིས་སད་པར༌[^286]བྱ་བ་གཡས་དང་གཡོན་དུ་འཁོར་བར་བསམ་པར་བྱའོ། །

[Block 412]
ཡི་གེ་ཨོཾ་མེ་ལོང་ལྟ་བུའི་ཡེ་ཤེས་ཀྱི་རང་བཞིན་གྱིས་སྦར་ཞིང་འོད་ཀྱི་ཚོགས་སྤྲོ་བར་གྱུར་པར་བསམ་མོ་ཞེས་བདུད་རྩི་སྦྱང་བ་ལ་སོགས་པའི་རིམ་པའོ། །

[Block 413]
ཨོཾ་སྭ་བྷཱ་བ་ཤུདྡྷ་སརྦ་དྷ་རྨཱ་སྭ་བྷཱ་བ་ཤུད་དྷོ྅ཧཾ། ཞེས་སྔགས་སམ་ཡང་ན། ཨོཾ་བཛྲ་དྷྲྀཀ་ཅེས་བྱ་བའི་སྔགས་ཀྱིས་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 414]
དེའི་རྗེས་ལ་ཡང་ཡེ་ཤེས་སེམས་དཔའི་ཐུགས་ཀར་ཏིང་ངེ་འཛིན་སེམས་དཔའི་མེ་ལྕེ་བདུན་དང་ལྡན་པ་ལྟ་བུར་བསམས་ཏེ།[^287] མགྲིན་པར་ཡི་གེ་ཨཱཿཡོངས་སུ་གྱུར་པ་ལས་པདྨ་འདབ་མ་བརྒྱད་པ་དམར་པོ་དེའི་འདབ་མ་གཅིག་ལྕེ་རུ་བསམས་ལ། དེ་ལ་ཡང་ས་བོན་ཧཱུཾ་ཡོངས་སུ་གྱུར་པའི་རྡོ་རྗེ་དཀར་པོ་ཕྲ་མོ་དེའི་དབུས་ཀྱི་རྩེ་ལ་ཡི་གེ་ཨོཾ་གྱིས་བྱིན་གྱིས་བརླབ་པར་བྱ་སྟེ། སྔ་མ་བཞིན་དུ་དེ་བཞིན་གཤེགས་པ་དང་ཡུམ་གྱིས་བྱིན་གྱིས་བརླབས་ལ་དགང་གཟར་དང་བླུགས་གཟར་དུ་ལག་པ་གཉིས་བསམས་ཏེ། དེ་དག་གིས༌[^288]བདུད་རྩིའི་སྣོད་ཕྱག་འཚལ་བ༌[^289]སྔོན་དུ་འགྲོ་བར་བླངས་ཏེ། དབྱེ་བ་རྣམ་པར་སྤངས་པའི་བློས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་འདུས་པའི་ངོ་བོ་ཉིད་ཨོཾ་བཛྲ་ཨ་མྲྀ་ཏེ་ས་མཱ་དྷི་དྷཱ་ན་པྲྀ་ཎ་ནི༌[^290]སྭཱ་ཧཱ། ཞེས་བྱ་བའི་སྔགས་འདིས་ཁའི་ཐབ་ཁུང་གི་ལམ་ནས༌[^291]ཡེ་ཤེས་ཀྱི་མེ་ལ་བསྲེག་པར་བྱའོ། །

[Block 415]
འདིའི་ཕན་ཡོན་ནི་ལྷ་མོ་བཞིས་ཞུས་པའི་རྒྱུད་ལས།

[Block 416 [VERSE]]
རྒ་བ་མེད་ཅིང་ནད་མེད་དང་། །
འཆི་བ་མེད་ཅིང་དུག་སོགས་མེད། །
དེ་ནི་དུས་མིན་འཆི་བ་མེད། །
གནོད་པ་ཐམས་ཅད་འཇོམས་པར་བྱེད། །

[Block 417]
ཅེས་འབྱུང་ངོ་། །ཟླ་གསང་ཐིག་ལེ་ལས་ཀྱང་།

[Block 418 [VERSE]]
དུས་དེ་བརྩམས་ནས་དེ་ནི་རྟོག་མེད་དེ། །
དེ་ཡི་ཁ་དོག་དབྱིབས་དང་མཚན་མ་འཛིན། །
བསམ་མི་ཁྱབ་པའི་ངོ་བོ་རྣམ་སྨིན་སྐུ། །
སྡོམ་པ་དེ་ལས་བྱ་བ་བྱས་པས་བསྒོམ། །

[Block 419]
ཞེས་འབྱུང་ངོ་། །བཟའ་བ་དང་བཏུང་བ་ལ་སོགས་པ་གང་ཅི་ཡང་རུང་བ་དེ་དག་ཐམས་ཅད་ཟས་ཀྱི་དུས་སུ་རང་འདོད་པའི་ལྷའི་རྣལ་འབྱོར་པ་དང་ལྡན་པས་བདུད་རྩི་ལྔ་བཞིན་དུ་སྦྱངས་ཏེ་བཟའ་བར་བྱའོ། །

[Block 420]
དེ་ལ་ལྐོག་མ་དང་སྙིང་ག་དང་ལྟེ་བ་དང་གསང་བ་དག་ཏུ་ཁམས་བཞིའི་རང་བཞིན་དཀྱིལ་འཁོར་བཞི་སྟེ། མེ་དང་ཆུ་དང་རླུང་དང་དབང་ཆེན་ནོ། །

[Block 421]
དེ་ལ་མེའི་དཀྱིལ་འཁོར་ནི་རླུང་གི་དཀྱིལ་འཁོར་གྱིས་སྦར་བ་ཡིན་ཏེ། ཆུའི་དཀྱིལ་འཁོར་གྱིས་ཡོངས་སུ་སྨིན་པར་བྱེད་དེ། དབང་ཆེན་གྱི་དཀྱིལ་འཁོར་སྣོད་ཀྱི་འཇིག་རྟེན་གྱི་ངོ་བོར་བསྲེག་བྱ་གནས་པར་གྱུར་ཏེ། དེ་ཉིད་དུ་འཇུག་གོ་འཇུག་པའི་ཐ་མར་བཤང་ལམ་ལས་ཐལ་བར་གྱུར་པ༌[^292]ངེས་པར་འབྱུང་བར་འགྱུར་ཞེས་ནང་གི་སྦྱིན་སྲེག་གི་ཆོ་གའོ། །

[Block 422 [HEADING]]
##### གཤེགས་སུ་གསོལ་བ། ^1-1-3-10-0

[Block 423]
དེའི་རྗེས་སུ་མཆོད་པའི་ཆོ་ག་བརྩམ་པར་བྱ་སྟེ། ཡེ་ཤེས་སེམས་དཔའི་ཐུགས་ཀ་ན་གནས་པའི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་གང་ཡིན་པ་དེ་ཉིད་སྲོག་དང་རྩོལ་བས་བསྐུལ་བ་ན་གཡས་དང་གཡོན་པའི་སྣའི་བུག་པ་ཁ་སྦྱར་གྱི་ནང་ནས་ཕྱིའི་རྡུལ་ཚོན་ལ་སོགས་པའི་དཀྱིལ་འཁོར་དག་ཏུ་རྣམ་པར་སྤྲོ་ཞིང་དགོད་ལ། སྔ་མ་བཞིན་དུ་ཁ་སྦྱར་དུ་བྱས་ཏེ་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ཡོངས་སུ་གསལ་བར་མཐོང་ནས་ཡན་ལག་ལྔས་ཕྱག་འཚལ་བ་བཞི་པོ་བྱའོ། །

[Block 424]
ཨོཾ་སརྦ་ཏ་ཐཱ་ག་ཏ་སྐུའི་རིགས་ཀྱི་དཀྱིལ་འཁོར་པ་རྣམས་ལ་ཀཱ་ཡ་བཱཀ་ཙིཏྟ་པྲ་ན༌[^293]མེ་ན་པཱ་དཱ་བནྡཱ་ནཱཾ་ཀ་རོ་མི། ཞེས་ཤར་ནས་སོ། །

[Block 425]
ཨོཾ་སརྦ་ཏ་ཐཱ་ག་ཏ་རིན་པོ་ཆེའི་རིགས་ཀྱི་དཀྱིལ་འཁོར་པ་རྣམས་ལ་ཀཱ་ཡ་བཱཀ་ཙིཏྟ་པྲ་ན༌[^294]མེ་ན་པཱ་དཱ་བནྡཱ་ནཱཾ་ཀ་རོ་མི། ཞེས་ལྷོ་ནས་བྱའོ། །
--- END BLOCKS ---
