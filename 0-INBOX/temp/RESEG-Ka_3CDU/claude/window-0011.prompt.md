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
རྐུ་སེམས་མེད་ན་བསྡམ་པར་བྱ་བའི་ཉེས་བྱས་གཅིག །གཞན་གྱི༌[^287]མཐུ་དང་འཇབ་བུས་བརྐུས་ན་ཚུལ་ཁྲིམས་ཞིག་པར་འགྱུར་ཏེ། བདག་ཉིད་ཀྱིས་ནི་མ་ཡིན་གྱིས་དགེ་སློང་གྲོགས་པོ་ཞིག་ལ་རྐུར་བཅུག་པ་ལས་དེས་མཐུ་དང་འཇབ་བུས་བརྐུས་ཏེ། ནོར་བདག་ཅག་སོ་སོར་བགོས་རིན་ཐང་ཚང་ན་ཕས་ཕམ་པར་འགྱུར་རོ། །

[Block 387]
རིན་ཐང་མ་ཚང་ན་ཉེས་བྱས་སྦོམ་པོ་རེ་རེ་བརྐུས་ན་བརྐུས་ཤས་ཀྱི༌[^288]སྐལ་བ་བླངས་ན་ཉེས་པ་སྦོམ་པོ་གཅིག །འཁྲུལ་པ་མེད་པར་མི་གཞན་གྱི་ཞེས་བྱ་བ་ལ་འཁྲུལ་པ་ནི་རྨོངས་པ་དང་མི་དྲན་པ་ཡིན་ལ་དེ་མེད་པ་ནི་སེམས་རང་བཞིན་དུ་གནས་པའོ། །

[Block 388]
ཡང་བརྐུ་བར་བྱ་བའི་རྫས་གང་ཡིན་པ་དེ་ཉིད་མངོན་པར་ཐོབ་པ་ལ་བྱ་སྟེ། བརྐུ་བར་བྱ་བའི་རྫས་ཉིད་ནི་མ་ཐོབ་ཀྱི་བར་དུ་རྫས་གཞན་གྱིས་ཐོབ་པ་ལས་འཁྲུལ་ཞེས་བྱ་སྟེ་དེ་ནི་རིན་ཐང་ཚང་ཡང་ཕས་ཕམ་པར་མི་བྱ་སྟེ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 389]
མི་གཞན་ཞེས་བྱ་བ་ནི་བདག་གི་ནོར་དགར་བའི་ཚིག་སྟེ། མི་གཞན་གྱི་ནོར་བརྐུས་ན་ཕས་ཕམ་པར་འགྱུར་རོ།[^289] །བདག་གི་ནོར་བརྐུས་ན་རིན་ཐང་ཚང་ཡང་སྦོམ་པོར་མི་འགྱུར་རོ། །

[Block 390]
གནས་ནས་མ་ཤ་ལྔ་ཙམ་ཞེས་བྱ་བ་ལ་གནས་ནི་ནོར་རྫས་གནས་ནས་སྤགས་ཏེ་བར་དུ་ཆོད་རིན་ཐང་ཚང་བ་ལས་ཕམ་པའོ། །

[Block 391]
དེ་ཡང་གནས་གཅིག་སྟེ་གཞི་མ་ཉམས་པ་ལ་ཚོན་ལ་སོགས་པ་མ་གྲོགས་པ་དང་། ས་སྒར་སྒུར་མེད་ན་གཞི་གཅིག་པ་ཞེས་བྱ་བ་སྟེ་ནམ་ཐ་དད་པ་གཅིག༌[^290]གིས་མ་ཆོད་ཀྱི་བར་དུ་ཕམ་པར་མི་གཞག༌[^291]གོ། །

[Block 392]
མ་ཤ་ལྔ་ཙམ་ཞེས་བྱ་བ་ནི་རྒྱ་གར་གྱི་རིན་ཐང་གཞལ་ན་དངུལ་ཞོ་གཅིག་ཙམ་བརྐུས་ན་ཕམ་པར་བརྩིའོ། །

[Block 393]
ཡང་ཁ་ཅིག༌[^292]གིས་ནི་ཞོའི་བརྒྱད་ཆ་གཅིག་ལ་བྱས་ཏེ་དེ་ཙམ་གྱིས་ནི་རིན་ཐང་ཚང་བར་བརྩིའོ། །

[Block 394]
རང་གི་ཡུལ་ནས་བྱུང་བ་གང་ཞེས་བྱ་བ་ནི་རིན་ཐང་ཚང་བ་ཡང་བརྐུས་བའི་དུས་དེ་ཉིད་ན་རིན་ཐང་ཚང་མ་ཚང་བརྩིའོ། །

[Block 395]
ཁ་ཅིག༌[^293]བརྐུས་པའི་དུས་དེ་ཉིད་ན་རིན་ཐང་མ་ཚང་ལ་དཀོན་མོད་དང་སྦྱར་ཏེ། དུས་ཕྱི་ཞིག་ན་རིན༌[^294]ཐང་ཚང་བ་ལྟ་བུ་ནི་ཕམ་པར་མི་གཞག༌[^295]སྦོམ་པོའོ། །

[Block 396]
ཀཱརྵཱ་པ་ཎའི་བཞི་ཆ་བརྐུས། །ཞེས་བྱ་བ་ནི་གོང་དུ་མ་ཤ་ལྔ་བཤད་པ་དང་འདྲའོ། །

[Block 397]
སྦྱོར་བའི་ཚེ་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་དང་པོ་བརྐུ་བར༌[^296]བསམས་ཏེ་སྟན་དང་ཁྲི་ལས་ལངས་པའི་དུས་ཉིད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 398]
རྡོ་ཁུ་རྩ་བ་འབྲས་བུ་ཤིང་། །ཞེས་བྱ་བ་ལ་རྩ་བ་ནི་བླ་སྒང༌[^297]དང་བོང་ང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 399]
འབྲས་བུ་ནི་ཤིང་ཐོག་ལ་སོགས་པའོ། །

[Block 400]
ཤིང་ནི་སྐྱེད་ཤིང་རྣམ་པ་སྣ་ཚོགས་ཏེ། དེ་དག་བརྐུས་ཏེ་རིན་ཐང་ཚང་ན་ཕམ་པ་མ་ཚང་ན་སྦོམ་པོའོ། །

[Block 401]
སྡོང་བུ་ལོ་མ་ཤུན་པ་ཆུ། །ཞེས་བྱ་བ་ལ། སྡོང་བུ་ནི་མར་དང་སྨན་ཁྲིལ་བུའི་རིགས་སུ་གཏོགས་པའོ། །

[Block 402]
ལོ་མ་ནི་ཤིང་ལོ་ལྡུམ༌[^298]ལོངས་སྤྱད་པར་འོས་པར་རུང་བའོ། །

[Block 403]
ཤུན་པ་ནི་གྲོ་ག་ལ་སོགས་པའོ། །

[Block 404]
ཆུ་ནི་ཁྲུས་ཆུ་དང་བཏུང་ཆུ་ལྟ་བུ་སྟེ་རྒྱ་མཚོར་ཞུགས་པ་དང་མྱ་ངམ་ལྟ་བུར་འགྲོ་བ་སྟེ་ཆུ་ཤིན་དུ་དཀོན་པའི་དུས་ན་བརྐུ་བའོ། །

[Block 405]
མེ་ཏོག་ཆུ་སྐྱེས་ཐང་སྐྱེས་དང་། །ཞེས་བྱ་བ་ནི་མེ་ཏོག་ཆུ་ནས༌[^299]སྐྱེས་པ་པདྨ་དང་ཨུཏྤལ་ལ་སོགས་པའོ། །

[Block 406]
ཐང་ལས་སྐྱེས་པ་སྟེ་ནཱ་ག་གེ་སར་ལ་སོགས་པའོ། །

[Block 407]
ཞིང་དང་ལོ་ཐོག་ས་གཞི་དང་། །ཞེས་བྱ་བ་ལ་ཞིང་གི་མུ་རྐུ་བ་སྟེ། ཡུལ་གྱི་རྒྱལ་པོའི་བཀའ་ཁྲིམས་ལས་བྱུང་བ་བཞིན་རིན་ཐང་བརྩིའོ། །

[Block 408]
ལོ་ཏོག་ནི༌[^300]ཐན་པ་ཆེན་པོའི་ཚེ་གཞན་གྱི་ཞིང་ལ་ཆུ་གཏོང་བ་གཅོད་ཅིང་བདག་གི་ཞིང་ལ་ཆུ་གཏོང་བ་དང་། ཆར་པ་ཆེ་བའི་དུས་ན་བདག་གི་ཞིང་ལ་ཆུ་བཅད་ནས་གཞན་གྱི་ཞིང་ལ་བཏང་སྟེ་བདག་གི་ལོ་ལེགས་ལ་གཞན་གྱི་ལོ་ཉེས་ན་རིན་ཐང་ཚང་ན་ཕམ་པ། མ་ཚང་ན་སྦོམ་པོའོ། །

[Block 409]
ལོ་ཏོག་གཉིས་ཀ་ལ་མ་ཕན་ཡང་བླ་སྙམ་པས་ཞིང་རྐུ༌[^301]སེམས་དེ་ལྟར་བཏང་སྟེ་ཕ་རོལ་པོ་ལ་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 410]
ཞིང་རྐུ་བ་ལ་རྣམ་པ་གཉིས་ཏེ། ཤགས་བཀར༌[^302]གཏོང་བ་དང་ར་བས་བསྐོར་བའོ། །

[Block 411]
དགེ་སྦྱོང་གིས༌[^303]ཞལ་ཆེ་བའམ་ཡུལ་དཔོན་གྱི་མདུན་དུ་ཤགས་བཀྱེ་ལ་དགེ་སྦྱོང་རྒྱལ་བར་བཅད་ལ་ཁྱིམ་པས་ཀྱང་སྦྱོར་བའི་བསམ་པ་བཏང་ན་ཕམ་པ། སྦྱོར་བའི་བསམ་པ་མ་བཏང་ན་སྦོམ་པོའོ། །

[Block 412]
རྒྱལ་པོས༌[^304]རྒྱལ་བར་བཅད་ན་ཡུལ་གྱི་གཙོ་བོས༌[^305]རྒྱལ་བར་གྱུར་པར་གཅད༌[^306]མ་ཐག་ཏུ་ཕམ་པའོ། །

[Block 413]
བསྐོར་བས་བརྐུ་བ༌[^307]ནི་ཞིང་ལ་ར་བ་དང་འོབས་ལྟ་བུས་སྐོར་བར༌[^308]བྱེད་པ་ན་ནམ་ལངས༌[^309]ཀྱི་སྣ་མ་ཕྲད་ཀྱི་བར་དུ་སྦོམ་པོའོ། །

[Block 414]
ཕྲད་ན་ཕམ་པར་གཞག༌[^310]གོ། །

[Block 415]
ས་གཞི་ནི་ཁངས་དང་ཚོང་དུས༌[^311]ལྟ་བུ་སྟེ། དགེ་སྦྱོང་གིས༌[^312]མི་དབང་བཞིན་བརྐུས་ན་རིན་ཐང་ཚང་ན་ཕམ་པའོ། །

[Block 416 [VERSE]]
མ་ཚང་ན་སྦོམ་པོར་བཞག་གོ། །
གྲུ་དང་ཤིང་དང་ཤོ་གམ་དང་། །

[Block 417]
ཞེས་བྱ་བ་ལ་དགེ་སློང་གིས་གྲུ་རྐུ་བར༌[^313]བསམས་ཏེ་ཆུ་རྒྱུན་ལས་གྱེན་དུ་བཟློག་དེ༌[^314]གྲུ་ཚུགས་ལས་གྲུ་འཇུག༌[^315]ཐལ་ན་ཕམ་པ། ཆུ་རྒྱུན་ཐོག་ཐག་ཁྱེར་ཏེ་སྒུར་དང་གད་པ་དང་སྣེའུ་ཆོད་ན་སྦོམ་པོའོ། །

[Block 418]
དེ་མི་སྣང་ན་ཕམ་པ། ཐད་ཀར་རྐུ་ན་ཕ་རོལ་གྱི་འགྲམ་སྐམ་ས་ལ་ཕྱིན་ན་ཕམ་པ། དེ་ཉིད་རྫབ་དང་སའི་འོག་ཏུ་སྦས་ན་གྲུ་མི་སྣང་བར་གྱུར་ཙམ་ན་ཕམ་པའོ། །

[Block 419]
ཤིང་ནི་བཟའ་ཤིང་དང་མེ་ཏོག་གི་ཤིང་དང་གྲིབ་ཤིང་ལྟ་བུ་སྟེ་རིན་ཐང་ཚང་ན་ཕམ་པའོ། །

[Block 420]
གསེབ་ལམ་དང་ལམ་གྱི་ཤོ་གམ་ལྟ་བུ་བཀའ་ཁྲིམས་གྱིས་མི་སྦྱིན་དུ་མི་རུང་བ་ལས་གཞན་གྱི༌[^316]དགེ་སྦྱོང་གིས་བཟླས་སམ་གང་གིས་གང་ཟག༌[^317]གཞན་ལ་གསངས༌[^318]ཏེ་ཤོ་གམ་མ་བྱིན་ཏེ་རིན་ཐང་བརྩིས་ཏེ་ཚང་ན་ཕམ་པ།

[Block 421 [VERSE]]
དེ་བཞིན་གྲུ་ཡི་བཙས༌[^319]རྣམས་དང་། །
ཞེས་པ་དང་ཡང་སྦྱར་བར་བྱའོ། །
སྲོག་ཆགས་རྐང་པ་མེད་པ་དང་། །
རྐང་མངས༌[^320]རྐང་གཉིས་རྐུ་བ་དང་། །

[Block 422 [VERSE]]
བརྟུལ་ཞུགས་ཅན་གྱིས༌[^321]མི་ཡི་ནོར། །
དབྱིག་ལ་སོགས་པ་གང་ཡང་རུང་། །
རྐུ་བའི༌[^322]སེམས་ཀྱིས་གང་བརྐུས་ཀྱང་། །
རིན་ཐང་ཚང་ན་སྡོམ་པ་ཞིག །

[Block 423]
ཅེས་བྱ་བ་ལ། མིའི་ལོངས་སྤྱོད་དགོས་པར་བྱ་བའི་ཕྱིར་གསོས་ཤིང་བཙལ་བ༌[^323]སྲོག་ཆགས་རྐང་པ་མེད་པ་སྦྲུལ་དང་འབུ་ལྟ་བུ་དང་། རྐང་པ་གཉིས་པ་མི་ལྟ་བུ་དང་། ཕ་རོལ་ལ་གནོད་པར་བྱ་བའི་ཕྱིར་རྐང་མངས་སྡིག་པ་ལ་སོགས་པ་ལྟ་བུ། རང་ཉིད་ཀྱིས་བརྐུས་པ་དང་། རྐུར་བཅུག་པ་དང་། ཡང་གཞན་གྱིས༌[^324]ནོར་གསེར་དངུལ་ལྟ་བུ་རྣམས་རྐུ་བའི་སེམས་ཀྱིས་བརྐུས་ཏེ་རིན་ཐང་ཚང་ན་ཕམ་པའོ། །

[Block 424]
སྩོགས་པའི་སྒྲས་ནི་མིའི་ནོར་རྙི་དང་སྤྲེའུ་དང་བྱ་རྒྱ་དང་བོད་རྒྱ་དང་ཉ་རྒྱ་ལ་སོགས་པ་རྐུ་བ༌[^325]ཡང་བསྡུ་སྟེ། འདིར་དགེ་སྦྱོང་གིས་བདག་གི་ནོར་དུ་རྐུ་སེམས་ཀྱིས་མིང་དུ་སྨོས་པ་འདི་དག་བརྐུས་ཏེ་རིན་ཐང་ཚང་ན་ཕམ་པའོ། །

[Block 425]
བདག་གི་དོན་དུ་མ་ཡིན་གྱི་ཕ་རོལ་ལ་གནོད་པ༌[^326]བྱ་བའི་བསམ་པས་རྐུ་ན་ཕམ་པའོ།[^327] ། གཉིས་ཀ༌[^328]ལ་ཕན་གནོད་མེད་པའི་བསམ་པས་དེ་དག་དྲལ་ཞིང་བསྲེགས་ན་ཡང་སྦོམ་པོའོ། །
--- END BLOCKS ---
