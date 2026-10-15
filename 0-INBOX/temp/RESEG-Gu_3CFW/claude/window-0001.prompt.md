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
[Block 36]
གཅིག་ཅིག་བྱིན་གྱིས་བརླབས་པ༌[^38]ལ་གསུམ་ཆར་གྱིས་དབྱུང་བ་ཡང་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 37]
དེ་ལྟར་ཡང༌[^39]འདིར་གཞུང་ནི་བཙུན་པ། གང་ཟག་གི་སྣམ༌[^40]སྦྱར་གྱི་གཏན་ལ༌[^41]གདིང་དུ་རུང་ངམ། ཉེ་བ༌[^42]འཁོར་མི་རུང་ངོ་། །གལ་ཏེ་དགེ་འདུན་ལ་ཕུལ་ན་ནི་རུང་ངོ་། །བླ་གོས་དང་མཐང་གོས་ཀྱང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། བླ་གོས་དང་མཐང༌[^43]གོས་གཉིས་ཀྱང་ངོ་། །གཅིག་གིས་གདིང་བ་ཡོད་པར་གྱུར་པ་ལ༌[^44]འདི་རིགས་པར་གྱུར་པ་མཐོང་བ་ཡིན་ནོ། །

[Block 38]
གང་ཡང་གདིང་བར་བྱ་ཞེས་བྱ༌[^45]བ་གཅིག་གིས་ཚིག་དེ་ལ་ནི་དེ་ལྟར་གནོད་པ་མ་ཡིན་ཏེ། འདིར་དགེ་འདུན་རྒྱས་པ་བསྒྲུབ་པ་ཅན་གྱི་སྲ་བརྐྱང་གི་སྒྲས་ཆོས་གོས་བརྗོད༌[^46]པའི་ཕྱིར་དང་། [^47]གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 39]
ཆོས་གོས་ཐམས་ཅད་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་རྒྱས་པར་སྒྲུབ་པ་ཉིད་ལ་གནས་པ༌[^48]མེད་དོ། །

[Block 40]
དེ་ལྟ་བས་ན་བྱིན་གྱིས་བརླབ་པ༌[^49]ཐམས་ཅད་ལ་འདི་ཐམས་ཅད་སྟོན་པའོ། །

[Block 41]
དེ་ལྟ་བས་ན་དགེ་སློང་མ་རྣམས་ཀྱིས་ཆོས་གོས་ལྔ་ཆར་གཏན་པ་ཉིད་དུ་གདིང་བར་བཏིང་བ༌[^50]འདིས་བསྟན་པ་ཡིན་ནོ། །

[Block 42]
དགེ་འདུན་གྱིའོ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་གསུམ་མོ། །

[Block 43]
ཆོས་གོས་གཞན་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་དེ་ཉིད་ཡིན་ཏེ། ཁས་བླང་བར་མ་བྱས་པར་བྱིན་གྱིས་བརླབ་པ་མེད་དོ། །

[Block 44]
དེའི་ཕྱིར་དགེ་འདུན་གྱིལ་བྱིན་པ་དེ་ལ་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 45]
ཆོས་གོས་གང་གདིང་བར་འོས་པ་དེ་བསྟན་པའི་བཤད་གདབ་མ་བྱས་པ་དང་། ཡ་ཡོར་མ་གྱུར་པ་དང་མ༌[^51]མུགས་པ་དང་མ་ཟེགས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་བཀྲུ་བ་ལ་བཤད་གདབ་མ་བྱས་ཀྱི་བར་དེ་སྲིད་དུ་བཀྲུས་པ་མི་འགྲུབ་པས་དེ་སྲིད་དུ་འདིར་བཀྲུ་བ་ལ་བཤད་གདབ་ཏུ་འདོད་དོ། །

[Block 46]
དེ་ལས་གང་ཞིག་ལབ་བཞིན་དུ་བཤད་གདབ་བྱས་པ་དང་རྡུང་བ༌[^52]དེ་ནི་བཤད་གདབ་བོ། །

[Block 47]
དེ་ལྟར་མ་བྱས་པ་གང་ཡིན་པ་དེ་ནི་བཤད་གདབ་མ་བྱས་པའོ། །

[Block 48]
ཡ་ཡོར་ལ་སོགས་ཞེས་བྱ་བ་ནི་སྒམ་བུ་ལ་སོགས་པ་གཞག་པ་ནི་ཡ་ཡོར་རོ། །

[Block 49]
གང་ཞིག་གྲྭ་དག༌[^53]འཕྱང་བར་འདུག་པ་ནི་མི་མཉམ་པར་འདུག་པའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 50]
འཐག་པའི་ཚེ་བར་བར་དུ་རྒྱུ་སྤུན་མ་བཅུག་ཅིང་སེང་སེར་པོར༌[^54]གྱུར་པའོ་ཞེས་ཀྱང་གཞན་དག་ཟེར་ཏེ། འདི་ལ་དོན་དེ་ཁས་ལེན་པའོ། །

[Block 51]
དེའི་འདོད་པ་འདིར་ཡ་ཡོ༌[^55]ནི་སེང་སེང་པོར་གྱུར་པའོ། །

[Block 52]
དེ་ལས་བཟློག་པ་གང་ཡིན་པ་དེ་ནི་ཡ་ཡོར་མ་གྱུར་པའོ། །

[Block 53]
མ་མུགས་པ་ཞེས་བྱ་བ་ལ་མུགས་པ་ཞེས་བྱ་བ་ནི་སྲིལ་རྣམས་དང་བྱི་བ་ལ་སོགས་པའི་མཆུས་མུགས་པ་སྟེ། དེ་ལྟར་མ་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་གཞན་ནོ། །

[Block 54]
མ་ཟེགས་པ་ཞེས་བྱ་བ་ལ། ཟེགས་པ་ཞེས་བྱ་བ་ནི་ཤས་སྲབ་པ༌[^56]སྟེ། དེ་ལྟར་མ་གྱུར་པ་ནི་མ་ཟེགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 55]
ཁ་བསྒྱུར་བའོ་ཞེས་བྱ་བ་ནི་འདིར་བཀྲུ་བཤལ་འབའ་ཞིག་ལ་སོགས་པས་ཁ་བསྒྱུར་བར་བྱས་པའོ། །

[Block 56]
ཁ་བསྒྱུར་བ་དེས་ཀུན་ནས་སྦྱར་བ་ནི་ཁ་བསྒྱུར་བའོ། །

[Block 57]
ཆོས་གོས་མ་བསྡམས་པ༌[^57]རུང་བ་ཞེས་གསུངས་པ་དེ་ཉིད་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 58]
འདིར་གཞུང་ནི།

[Block 59]
བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 60]
ཆོས་གོས་མ་བསྡམས་པ༌[^58]རུང་བ་གང་ཞེ་ན། མ་བསྡམས་པ༌[^59]ནི་མ་བཅགས་པའོ།[^60] །དོན་དེ་ཉིད་རུང་བ་གང་ཡིན་པས་མ་བསྡམས་པ༌[^61]རུང་བའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 61]
སྨྲས་པ༌[^62]ཆོས་གོས་རུང་བ་གང་ཡིན་ཞེ་ན། ཆོས་གོས་ཁ་བསྒྱུར་བ༌[^63]གང་ཡིན་པ་དེ་ཡང་དེ་ཡིན་པས་ཁ་བསྒྱུར་བ་ཞེས་བྱ་བ་དེ་འདི་ཡིན་ཏེ། [^64]མི་གདིང་བར་མི་བྱའོ། །

[Block 62]
སྨྲས་པ་བདག་ཉིད་འདི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 63]
ཡོངས་སུ་མ་སྤྱད་པའོ་ཞེས་བྱ་བ་ནི། འདིར་གཞུང་འདི་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས་ཆོས་གོས་དེངས་པ་འཆང་བ་ལས་དགེ་སློང་རྣམས་ཀྱིས་ཡོངས་སུ་ལོངས་སྤྱོད་པ་ཉིད་ཀྱི་དོན་དུ་གསུངས་སོ། །

[Block 64]
ཇི་སྐད་དུ་ཆོས་གོས་རྙིང་པ་འཆང་བས་སྲ་བརྐྱང་གདིང་བར་མི་བྱའོ། །ཅི་ཇི་ཙམ་གྱིས་ན་རྙིང་པ་བཅང་བར་བགྱི་ཞེ་ན། དགེ་སློང་གིས་སྤྱད་པའི་ཆོས་གོས་གསུམ་གང་ཡིན་པའོ༌[^65]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 65]
དགེ་སློང་གིས་སྤྱད་པའི༌[^66]མི་འོས་པ་ཉིད་ལ་བདེ་བླག་ཏུ་དེ་ལས་གཞན་པ༌[^67]ཡོངས་སུ་ལོངས་སྤྱོད་པ་ཞེས་བྱ་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 66]
དེ་ལྟ་བས་ན་ཡོངས་སུ་ལོངས་སྤྱོད་པ་ཐམས་ཅད་ལས་དེངས་པ་བསལ་བ་དང་འབྲེལ་ལོ། །

[Block 67]
སྲ་བའོ་ཞེས་བྱ་བ་འདིས་ནི་ཆོས་གོས་དེངས་པ་བསལ་བ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 68]
བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 69]
དེའི་དོན་ནི་ལོངས་སྤྱོད་མི་བཟོད་པ་ཞེས་གསུངས་སོ། །

[Block 70]
ཆོས་གོས་དེངས་པ་གང་ཞེ་ན། ཆོས་གོས་གང་དག་སློང་གི་ལུས་ལས་དེངས་པའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེངས་པ་ནི་ཟད་པ་ལས་ཏེ་ཞེས་བྱ་བ་འདིར་གཟུགས་པ་འདི་ཡིན་ཏེ། དེངས་པ་ནི་ཟད་པ༌[^68]ཡིན་པས་དེ་ལྟར་མ་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 71]
མཐུད་མ་ཅན་དང་ལྷན༌[^69]རིངས་ཅན་དང༌[^70]ལྷན་པ་ཅན་དང་ཆག་ཅན་དང་ཟུངས་ཅན༌[^71]མ་ཡིན་པའོ། །

[Block 72]
བྱ་བ་འདིར་མ་ཡིན་པའོ་ཞེས་བྱ་བའི་སྒྲ༌[^72]འདི་ལྔ་ཆར་དང་སོ་སོར་སྦྱར་ཏེ། ཟུངས་ཅན་མ་ཡིན་ཏེའོ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 73]
དེ་ལྟར་ཡང་ཐམས་ཅད་ལ་ཐུང་བ་ཉིད་དུ་བྱས་པ་ཉིད་དོ། །

[Block 74]
མཐུད་མ་ཅན་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། ཚད་དུ་མཆོག་པ་དགེ་སློང་མང་པོ་དག་ལ་མཚམས་སྦྱར་བར་བྱེད་ཅིང་སྲ་བརྐྱང་འདིང་བར༌[^73]བྱེད་ན་བཏིང་ཞེས་བརྗོད་པར་བགྱིའམ། བཀའ་སྩལ་པ། མ་བཏིང་ཞེས༌[^74]བརྗོད་པར་བགྱིའོ་ཞེས་བྱ་བ་ལ་དེ་ལས་འདིར་གདིང་བར་བྱ་བ་བཀག་པའོ། །

[Block 75]
གདིང་བར་བྱ་བ་ནི་གང་ཞིག་དུམ་བུར་བྱ་སྟེ། བཙེམས་པར་མ་ཡིན་པ་དེའོ། །
--- END BLOCKS ---
