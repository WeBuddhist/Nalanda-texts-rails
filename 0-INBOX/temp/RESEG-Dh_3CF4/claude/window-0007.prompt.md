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
[Block 246]
ཏིང་ངེ་འཛིན་ནི་བསམ་གཏན་ནོ། །

[Block 247]
ཅི་ནུས་ཞེས༌[^121]བྱ་བ་ནི་གང་གང་ལ་ཅི་ནུས་པ་སྟེ་ཇི་ལྟར་ནུས་པའོ། །

[Block 248]
དང་པོ་ཚུལ་ཁྲིམས་ལ་གཞག་པར་སྟོན་ཏོ། །

[Block 249]
ཚུལ་ཁྲིམས་ལ་གནས་ནས་དབང་པོའི་སྒོ་སྡོམ་པའོ། །

[Block 250]
དེ་ལ་སོགས་པའི་རིམ་པ་ཇི་ལྟར་འཚམ་བ་བཞིན་དུ་ཅི་ནུས་པ་སྟེ། སྟོབས་ཇི་ལྟ་བ་བཞིན་དུ་རྗེས་སུ་སྟོན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 251]
སློབ་མ་དེ་གང་ཡིན་ཞེ་ན། དེ་ནས་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་པའོ། །

[Block 252]
བདག་ཉིད་ཆེན་པོ་ཞེས་བྱ་བ་ལ། བདག་ཉིད་ཆེན་པོ་གང་ལ་ཡོད་པ་དེ་ལ་བདག་ཉིད་ཆེན་པོ་སྟེ། ཚུལ་ཁྲིམས་ལ་སོགས་པ་ཡོད་པའོ། །

[Block 253]
དེ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 254]
རེ་ཞིག་ཅེས་བྱ་བ་ནི་དུས་གང་གི་ཚེ་ནའོ། །

[Block 255]
སློབ་མའི་ཚོགས་ཞེས་བྱ་བ་ནི་སློབ་མ་འདུས་པ་རྣམས་སོ། །

[Block 256]
ཕལ་ཆེར་ཞེས་བྱ་བ་ནི་མང་དུའོ། །

[Block 257]
ཡོངས་སུ་རྫོགས་པ་ནི་བྱ་བ་རྣམས་མཐར་ཕྱིན་པའོ། །

[Block 258]
རྒྱ་ཆེ་བ་ནི་ཡངས་པར་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 259]
དགེ་བ་ནི་དེས་དག༌[^122]པའོ། །

[Block 260]
ལས༌[^123]ནི་ལམ་སྟེ། འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པའོ། །

[Block 261]
རབ་ཏུ་བཀོད་པ་ནི་རྣམ་པར་གཞག༌[^124]པའོ། །

[Block 262]
འཇིག་རྟེན་པ་རྣམས་ཞེས་བྱ་བ་ནི་སློབ་མའི་མཆོག་ཏུ་བཟུང་བ་ཡིན་ནོ། །

[Block 263]
ཡང་ན་འཇིག་རྟེན་པ༌[^125]ཐ་མལ་པའོ། །

[Block 264]
ངེས་པ་ནི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 265]
ངེས་བའི་ལམ་ནི་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་དེ་ཉིད་སྦྱར་བར་བྱའོ། །

[Block 266]
བཙུད་པ་ནི་ཡང་དག་པར་ཞུགས་པར་བྱས་པས་སོ། །

[Block 267]
ངན་སོང་ནི་དམྱལ་བ་དང་། དུད་འགྲོ་དང་། ཡི་དགས་ལ་སོགས་པའོ། །

[Block 268]
སྒོ་ནི་འཇུག་པར་བྱེད་པ་སྟེ། བཅད་པ་ནི་བཀག་པའོ། །

[Block 269]
བདེ༌[^126]འགྲོ་ཞེས་བྱ་བ་ནི་མཛེས་པར་འགྲོ་བས་བདེ་འགྲོའོ། །

[Block 270]
ཡང་ན་ལྷ་དང་མིའི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 271]
ལམ་པོ་ཆེ་སྟེ་རྒྱལ་པོའི་ལམ་སྲང་བཞིན་དུ་ཞེས་བྱ་བ་ནི་དཔེས་ཉེ་བར་འཇལ་བ་སྟེ། ཇི་ལྟར་བྲམ་ཟེའི་ཁྱེའུ་སེང་གེ་ལྟ་བུའོ། །

[Block 272]
བྱས་ནས་ཞེས་བྱ་བ་ནི་བྱས་པར་གྱུར་ནས་ཞེས་པ་ཡིན་ནོ། །

[Block 273]
ཚེ་འདི་ལ་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ལའོ། །

[Block 274]
བདེ་བ༌[^127]སྤྱད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཚངས་པའི་གནས་པ༌[^128]བཞི་སྟེ། དེ་ཡང་གཅིག་ཏུ་བདེ་བ་ཡིན་པས་དེས་གནས་པའི་ཕྱིར་སྤྱོད་པའོ། །

[Block 275]
དེའི་ཚེ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གདུལ་བྱ༌[^129]རྣམས་འདུལ་བའི་ཚེའོ། །

[Block 276]
ཡང་ན་དེའི་ཚེ་ཞེས་པ་ནི་སློབ་མ་སྨིན་པའི་ཚེ་ནའོ། །

[Block 277]
སློབ་མའི་ངང༌[^130]ཚུལ་ཅན་ཡིན་པས་ན་སློབ་མའོ། །

[Block 278]
མ་ཕམ་པ༌[^131]ནི་བྱམས་པ་འདིའོ། །

[Block 279]
རྗེས་སུ་མཐུན་པ་ཞེས་བྱ་བ་ནི༌[^132]རྗེས་སུ་འགྲོ་བའོ། །

[Block 280]
རྣལ་འབྱོར་དང་མཐུན་པ་ནི་ཞི་གནས་དང་ལྷག་མཐོང་དང་རྗེས་སུ་མཐུན་པའི་གནས་སོ། །

[Block 281]
རི་སུལ་ནི་རིའི་སྨན་ལྗོངས་དང་། ཕུག་དང་ཚང་ཚིང་དང་བཅས་པའོ།[^133] །གནས་ཤིང་སྤྱོད་པ་ནི་སྤྱོད་ཅིང་འདུག་པའོ། །

[Block 282]
དེ་ནས་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་པའོ། །

[Block 283]
རིའི་ཁྲོད་ནི་རིའི་ཁྲོད་དེ་སུལ་དག་གོ། །

[Block 284]
དེ་ན་ནི་ཞེས་བྱ་བ་ནི་དེའི་ཚེ་ནའོ། །

[Block 285]
སྟག་མོ་ནི་སྟག་མོ་ཉིད་དོ། །
--- END BLOCKS ---
