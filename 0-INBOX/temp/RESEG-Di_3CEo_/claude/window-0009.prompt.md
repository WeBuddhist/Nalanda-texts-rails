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
[Block 316 [HEADING]]
#### འདོད་པའི་ཁམས་སུ་གཏོགས་པ། ^1-18-4-0

[Block 317]
འདོད་པའི་ཁམས་སུ་གཏོགས་པ་དག་ནི་དུ་ཞེ་ན། འདོད་ཁམས་གཏོགས་པ་ཐམས་ཅད་དོ། །

[Block 318]
གཏོགས་པ་ནི་མ་བྲལ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 319 [VERSE]]
གཟུགས་ཀྱི་ཁམས་ན་བཅུ་བཞི་སྟེ། །
དྲི་དང་རོ་དང་སྣ་དང་ནི། །
ལྕེ་ཡི་རྣམ་ཤེས་ཁམས་མ་གཏོགས། །

[Block 320]
དེ་ན་དྲི་དང་རོ་དག་མེད་དེ། [^119]གཉིས་ནི་ཁམས་ཀྱི་ཟས་ཡིན་པའི་ཕྱིར་ཡིན་ལ། དེ་ལ་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ཀྱང་དེར་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 321]
དེ་ལྟ་བས་ན་དམིགས་པ་མེད་པའི་ཕྱིར་སྣ་དང་ལྕེའི་རྣམ་པར་ཤེས་པ་དག་ཀྱང་མེད་དོ། །

[Block 322 [VERSE]]
གཟུགས་མེད་རྟོགས་པ༌[^120]ཡིད་དང་ནི། །
ཆོས་དང་ཡིད་ཀྱི་རྣམ་ཤེས་ཁམས། །

[Block 323]
གཟུགས་ཀྱི་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་དེར་སྐྱེས་ཏེ། དེའི་ཕྱིར་གཟུགས་ཀྱི་རང་བཞིན་གྱི་ཁམས་བཅུ་དང་། དེ་དག་ལ་བརྟེན་པ་དང་། དམིགས་པ་རྣམ་པར་ཤེས་པའི་ཁམས་ལྔ་ཡང་མེད་དོ། །

[Block 324 [HEADING]]
#### ཟག་པ་དང་བཅས་པ། ^1-18-5-0

[Block 325]
ཟག་པ་དང་བཅས་པ་རྣམས་ནི་དུ། ཟག་པ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། །ཡིད་དང་ཆོས་དང་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཆོས་གང་དག་བཤད་པ། དེ་གསུམ་ཟག་བཅས་ཟག་པ་མེད། །གང་དག་ལམ་གྱི་བདེན་པ་དང་འདུས་མ་བྱས་ཀྱིས་བསྡུས་པ་དེ་དག་ནི་ཟག་པ་མེད་པ་ཡིན་ནོ། །

[Block 326]
ལྷག་མ་དག་ནི་ཟག་བཅས་སོ། །

[Block 327 [HEADING]]
#### རྟོག་པ་དང་བཅས་དཔྱོད་པ་དང་བཅས་པ། ^1-18-6-0

[Block 328]
རྟོག་པ་དང་བཅས་དཔྱོད་པ་དང་བཅས་པ་རྣམས་ནི་དུ། རྟོག་པ་མེད་ལ་དཔྱོད་པ་ཙམ་དག་ནི་དུ། རྟོག་པ༌[^121]ཡང་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན།

[Block 329 [VERSE]]
རྟོག་དང་དཔྱོད་དང་བཅས་པ་ནི། །
རྣམ་པར་ཤེས་པའི་ཁམས་ལྔ་ཡིན། །

[Block 330]
འདི་དག་ནི་ཁམས་རྟག་ཏུ་རྟོག་པ་དང་དཔྱོད་པ་དག་དང་མཚུངས་པར་ལྡན་པ་ཡིན་ཏེ། ཐ་མ་གསུམ་ནི་རྣམ་གསུམ་མོ། །

[Block 331]
དེ་ལ་ཡིད་ཀྱི་ཁམས་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་། རྟོག་པ་དང་དཔྱོད་པ་དག་ལས་གཞན་པ་ཆོས་ཀྱི་ཁམས་མཚུངས་པར་ལྡན་པ་དག་འདོད་པའི་ཁམས་དང་བསམ་གཏན་དང་པོ་ན་ནི་རྟོག་པ་དང་བཅས་དཔྱོད་པ་དང་བཅས་པ་དག་ཡིན་ནོ། །

[Block 332]
བསམ་གཏན་ཁྱད་པར་ཅན་ན་ནི་རྟོག་པ་མེད་ཅིང་དཔྱོད་པ་ཙམ་དག་ཡིན་ནོ། །

[Block 333]
བསམ་གཏན་གཉིས་པ་ནས་བཟུང་སྟེ་སྲིད་པའི་རྩེ་མོའི་བར་གྱི་དང་། ཆོས་ཀྱི་ཁམས་མཚུངས་པར་ལྡན་པ་མ་ཡིན་པ་ཐམས་ཅད་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་གྱི་དཔྱོད་པ་ནི་རྟོག་པ་ཡང་མེད་དཔྱོད་པ་ཡང་མེད་པ་དག་ཡིན་ནོ། །

[Block 334]
རྟོག་པ་ནི་རྟོག་པ་གཉིས་པ་ཡང་མེད་པའི་ཕྱིར་དང་། དཔྱོད་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རྟོག༌[^122]ཏུ་རྟོག་པ་མེད་ཅིང་དཔྱོད་པ་ཙམ་ཡིན་ནོ། །

[Block 335]
ལྷག་མ་རྣམས་ནི་གཉིས་ཀ་སྤངས། །ལྷག་མ་ནི་གཟུགས་ཅན་གྱི་ཁམས་བཅུ་པོ་དག་སྟེ། དེ་དག་ནི་མཚུངས་པར་ལྡན་པ་མ་ཡིན་པའི་ཕྱིར་རྟག་ཏུ་རྟོག་པ་ཡང་མེད་ལ་དཔྱོད་པ་ཡང་མེད་པ་དག་ཡིན་ནོ། །

[Block 336]
གལ་ཏེ་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་པོ་རྣམས་རྟོག་པ་དང་དཔྱོད་པ་དང་བཅས་པ་དག་ཡིན་ན། ཇི་ལྟར་ན་རྣམ་པར་རྟོག་པ་མེད་པ་དག་ཅེས་བྱ་ཞེ་ན།

[Block 337 [VERSE]]
ངེས་པར་རྟོག་དང་རྗེས་དྲན་པའི། །
རྣམ་པར་རྟོག་པས༌[^123]རྣམ་མི་རྟོག །

[Block 338]
རྣམ་པར་རྟོག་པ་ནི་རྣམ་པ་གསུམ་མོ་ཞེས་གྲག་སྟེ། ངོ་བོ་ཉིད་དང་ངེས་པར་རྟོག་པ་དང་རྗེས་སུ་དྲན་པའི་རྣམ་པར་རྟོག་པའོ། །

[Block 339]
དེ་བས་ན་དེ་དག་ལ་ངོ་བོ་ཉིད་ཀྱིས་རྟོག་པ་ནི་ཡོད་ཀྱི་གཞན་དག་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་རྣམ་པར་རྟོག་པ་མེད་པ་དག་ཅེས་བྱ་སྟེ། དཔེར་ན་རྟ་རྐང་པ་གཅིག་པ་ལ་རྐང་མེད་ཅེས་བྱ་བ་བཞིན་ནོ། །

[Block 340]
ཡང་སེམས་ཀྱི་རང་བཞིན་ངོ་བོ་ཉིད་དང་།

[Block 341 [VERSE]]
རྗེས་སུ་དྲན་པའི་རྟོག་པ་དག །
དེ་དག་ཡིད་ཀྱི་ཤེས་རབ་གཡེང་། །
ཡིད་ཀྱི་དྲན་པ་ཐམས་ཅད་ཉིད། །

[Block 342]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཤེས་རབ་ནི་ཡིད་ཀྱི་ཞེས་བྱའོ། །

[Block 343]
མཉམ་པར༌[^124]གཞག་པ༌[^125]མ་ཡིན་པ་ནི་གཡེང་བ་ཞེས་བྱ་སྟེ། དེ་ནི་ངེས་པར་རྟོག་པའི་རྣམ་པར་རྟོག་པའོ། །

[Block 344]
ཡིད་ཀྱི་དྲན་པ་ཉིད་མཉམ་པར་གཞག་པ་དང་མཉམ་པར་གཞག་པ་མ་ཡིན་པའི་དྲན་པ་ཐམས་ཅད་ནི་རྗེས་སུ་དྲན་པའི་རྣམ་པར་རྟོག་པ་ཡིན་ནོ། །

[Block 345 [HEADING]]
#### དམིགས་པ་དང་བཅས་པ། ^1-18-7-0

[Block 346]
དམིགས་པ་དང་བཅས་པ་རྣམས་ནི་དུ། དམིགས་པ་མེད་པ་རྣམས་ནི་དུ་ཞེ་ན། དམིགས་བཅས་སེམས་ཀྱི་ཁམས་བདུན་ནོ། །

[Block 347]
སེམས་ཀྱི་ཁམས་བདུན་པོ་དེ་དག་ནི་ཡུལ་འཛིན་པའི་ཕྱིར་དམིགས་པ་དང་བཅས་པ་དག་གོ། །

[Block 348]
ཆོས་ཀྱི་ཕྱེད་ཀྱང་། གང་སེམས་ལས་བྱུང་བའི་རང་བཞིན་ཆོས་ཀྱི་ཁམས་དེ་ནི་དམིགས་པ་དང་བཅས་པའོ། །

[Block 349]
ལྷག་མ་གཟུགས་ཅན་གྱི་ཁམས་བཅུ་པོ་དག་དང་ཆོས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་གཅིག་ལྡན་པ་མ་ཡིན་པ་ནི་དམིགས་པ་མེད་པ་ཞེས་བྱ་བར་གྲུབ་པོ། །

[Block 350 [HEADING]]
#### ཟིན་པ། ^1-18-8-0

[Block 351]
ཟིན་པ་རྣམས་ནི་དུ། མ་ཟིན་པ་རྣམས་ནི་དུ་ཞེ་ན། མ་ཟིན་དགུ། བརྒྱད་པོ་དེ་དག་རྣམས་དང་སྒྲ། །སེམས་ཀྱི་ཁམས་བདུན་དང་ཆོས་ཀྱི་ཁམས་དང་།

[Block 352 [VERSE]]
སྒྲའི་ཁམས་རྣམས་ནི་མ་ཟིན་པའོ།[^126] །
དགུ་པོ་གཞན་ནི་རྣམ་པ་གཉིས། །

[Block 353]
ཟིན་པ་དག་ཀྱང་ཡིན་མ་ཟིན་པ་དག་ཀྱང་ཡིན་ཏེ། དེ་ལ་མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་ད་ལྟར་བྱུང་བ་རྣམས་ནི་ཟིན་པ་ཡིན་ནོ། །

[Block 354]
འདས་པ་དང་མ་འོངས་པ་རྣམས་ནི་མ་ཟིན་པ་ཡིན་ནོ། །

[Block 355]
གཟུགས་དང་། དྲི་དང་། རོ་དང་། རེག་བྱའི་ཁམས་ད་ལྟར་བྱུང་བ་དབང་པོ་དང་ཐ་མི་དད་པ་རྣམས་ནི་ཟིན་པ་ཡིན་ནོ། །
--- END BLOCKS ---
