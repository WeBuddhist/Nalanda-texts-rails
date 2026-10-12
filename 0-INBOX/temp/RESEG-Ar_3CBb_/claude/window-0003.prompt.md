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
[Block 106]
དེ་ཉིད་ཀྱིས་གསུངས་པ་འདི་ཉིད་ནི་རྒྱུད་ཀྱི་རྒྱལ་པོ་ཡིན་ཞེས་སྦྱར་རོ། །

[Block 107]
ཡང་ན་དཔལ་ལྡན་ཡང་ཡིན་རྒྱུད་ཀྱང་ཡིན་པས་ན་དཔལ་ལྡན་རྒྱུད་རྒྱལ་ཏེ། གང་ལ་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཐོབ་པར་བྱེད་པའི་ཐབས་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 108]
དེ་ཉིད་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་ཀྱིས་ཤིན་ཏུ་གསལ་བར་རྣམ་ཕྱེ་སྟེ། གང་ལ་ཏིང་ངེ་འཛིན་གཙོ་བོར༌[^58]སྟོན་པར་བྱེད་པའི་རྒྱུད་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་དོ། །གང་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ལ་བྱམས་པ་ལ་སོགས་པས་ཞུས་པའི་རྒྱུད་ཡེ་ཤེས་རྡོ་རྗེ་ཀུན་ལས་བཏུས་པ་ལ་སོགས་པའོ། །

[Block 109]
དེས་གསལ་བར་བྱེད་པ་ནི་དེས་གསལ་བར་བཤད་པ་སྟེ། སྒྲ་དང་དོན་ཐམས་ཅད་རྒྱས་པར་བྱས་ཤེའོ།[^59] །དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་ལ་རྣལ་འབྱོར་གྱི་རྒྱུད་ཀྱིས་རྒྱས་པར་བྱེད་པ་ཅིའི་ཕྱིར་ཞེ་ན། མཐའ་དྲུག་གི་ནི་འཆིང་བས་བཅིངས། །ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་མཐའ་དྲུག་གི་འཆིང་བ་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 110]
གལ་ཏེ་མཐའ་དྲུག་གི་འཆིང་བས་བཅིངས་ཀྱང་ཉེ་བར་གདགས་པ་མི་བྱའོ་ཞེ་ན། བློ་དམན་པ་རྣམས་ཀྱིས་རྟོགས་པར་བྱེད་པར་འགྱུར་ཏེ། དེའི་ཕྱིར་རྒྱལ་སྲས་ཡུལ་གྱུར་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 111]
རྒྱལ་བའི་ཡུལ་དུ་གྱུར་ཞེས་པས་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པས་རྟོགས་པར་བྱ་བ་ཡིན་པར་བསྟན་ཏོ། །

[Block 112]
རྒྱལ་བའི་སྲས་ཀྱི་ཡུལ་དུ་གྱུར། །ཞེས་པས་ནི་བྱམས་པ་ལ་སོགས་པ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་རྟོགས་པར་བྱ་བ་ཡིན་པར་བསྟན་ཏོ། །

[Block 113]
རྒྱས་སྲས༌[^60]ཡུལ་གྱུར་ཞེས་བྱ་བ་འདི་ནི་རྒྱལ་སྲས་གྱི་ཡུལ་དུ་གྱུར་པ་ཁོ་ནའོ་ཞེས་བྱ་བ་ནི་མ་ཡིན་གྱི། རྒྱལ་བའི་སྲས་ཁོ་ནའི་ཡུལ་དུ་གྱུར་ཞེས་པའོ། །

[Block 114]
འདིས་ནི་གཞན་དང་ལྡན་པ་རྣམ་པར་བཅད་པའོ། །

[Block 115]
མཐའ་དྲུག་གི་ནི་འཆིང་བས་བཅིངས། །ཞེས་བྱ་བ་འདི་ནི་ཉེ་བར་མཚོན་པའི་ཚིག་སྟེ། བཤད་པ་བཞི་ཡི་འཆིང་བས་བཅིངས། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཡང་ཤེས་པར་བྱའོ། །

[Block 116]
དེ་དག་གིས་བཅིངས་པ་ཡང་གང་ཡིན༌[^61]ཞེ་ན། རྒྱལ་བའི་འདུས་གང་ཡིན་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་མཐའ་དྲུག་གི་འཆིང་བས་བཅིངས་ཞེས་སྦྱར་རོ། །

[Block 117]
རྒྱལ་བའི་འདུས་པ་ཡང་སྒྲའི་རྣམ་པ་བཅིངས་སམ། དོན་གྱི་རྣམ་པ་བཅིངས་ཞེས་རྟོག༌[^62]གྲང་ན། སྒྲའི་རྣམ་པ་མ་ཡིན་པའི་ཕྱིར། རིམ་གཉིས་གནས་ཀྱིས་རྒྱས་བཏབ་དེ་ནི་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྐྱེད་པའི་རིམ་པ་དང་། རྫོགས་པའི་རིམ་པ་གཉིས་ཀྱིས་རྒྱས་བཏབ་ཅེའོ། །

[Block 118]
དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་རྒྱས་བཏབ་ཅེས་པ་ཡང་མི་གདུག༌[^63]སེམས་དང་བཅས་པ་འམ། སྙོམ༌[^64]ལས་དང་བཅས་པ༌[^65]ཡིན་ཞེས་རྟོག་གྲང་ན། ཕྱོགས་གཉི་ག་ནི་བླང་བར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རེ་ཞིག་བསལ་ལོ། །

[Block 119]
དེ་ཉིད་ཐམས་ཅད་ཀྱིས་རྟོགས་པ་མ་ཡིན་ནོ་ཞེ་ན། ཀླུ་སྒྲུབ་ལས་རྙེད་པ་ཞེས་སྨོས་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་གང་ཡིན་པ་དེ་སུས་ཀྱང་རྙེད་པར༌[^66]མ་གྱུར་པ་སློབ་དཔོན་ཀླུ་སྒྲུབ་ལས་རྙེད་ཅེས་སྦྱར་རོ། །

[Block 120]
འདི་དག་གི་དོན་ནི་འདི་སྐད་དུ་སྟོན་པར་འགྱུར་ཏེ། སྣོད་དང་སྣོད་མ་ཡིན་པ་རྣམ་པར་ཕྱེ་ནས་སྣོད་མ་ཡིན་པ་ལ་གསང༌[^67]བའི་དོན་དུ༌[^68]མཐའ་དྲུག་གི་འཆིང་བས་བཅིངས་པའོ། །

[Block 121]
གང་མཐའ་དྲུག་གི་འཆིང་བས་བཅིངས་པ་དེ་ནི་རྒྱལ་བའི་སྲས་ཀྱི་ཡུལ་དུ་འགྱུར་རོ། །

[Block 122]
གང་རྒྱལ་བའི་སྲས་ཀྱི་ཡུལ་དུ་གྱུར་པ་དེ་ནི་ཚོགས་དང་སློབ་མའི་གང་ཟག་གིས་རྙེད་པ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 123]
གང་ཚོགས་དང་སློབ་མས་རྙེད་པར་མ་གྱུར་པ་དེ་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་དང་། བྱང་ཆུབ་སེམས་དཔའི་སྤྲུལ་པ་ལས་རྙེད་པར་འགྱུར་རོ། །

[Block 124]
གང་རྣལ་འབྱོར་གྱི་རྒྱུད་དང་། བྱང་ཆུབ་སེམས་དཔའ༌[^69]སྤྲུལ་པ་ལས་རྙེད་པ་དེ་ནི་ཀུན་དང་ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 125]
ཀུན་དང་ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་རིགས་དབྱེ་བར་འགྱུར་རོ། །

[Block 126]
རྣལ་འབྱོར་གྱི་རྒྱུད་ཀྱང་ཇི་ལྟར་བཤད་ཅེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་ཕྱི་དང༌[^70]ནང་གི་མངོན་པར་བྱང་ཆུབ་པའི་སྒོ་ནས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པས་དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པ་ལས་ཀྱང་མངོན་པར་བྱང་ཆུབ་པ་སྟོན་པར་འགྱུར་རོ། །

[Block 127]
དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པའི་མངོན་པར་བྱང་ཆུབ་པ་དེ་ཉིད༌[^71]ཕྱི་དང་ནང་གི་དབྱེ་བས་རྒྱུའི་མངོན་པར་བྱང་ཆུབ་པ་དང་། ལམ་དང་། འབྲས་བུ་དང་། དཔེ་ལ་སོགས་པའི་ཟབ་པ་དང་རྨད་དུ་བྱུང་བའི་མངོན་པར་བྱང་ཆུབ་པ་ལེགས་པར་བསྟན་པར་བྱ་བའི་ཕྱིར་མངོན་པར་བྱང་ཆུབ་པའི་རྒྱུད་གསུངས་སོ། །

[Block 128]
དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་ངེས་པའི་དོན་དུ་བྱང་ཆུབ་ཀྱི་སེམས་ལ་བརྟེན་ཏེ། སངས་རྒྱས་པས་རྒྱུད་ཀྱི་རྒྱལ་པོ་ལས་ཀྱང་དེ་ཉིད་བསྟོད་པས༌[^72]དེ་ཉིད་གསལ་བར་བསྟན་པར་བྱ་བའི་ཕྱིར་ལྷ་མོ་བཞིས་ཞུས་པ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་རྒྱུད་གསུངས་སོ། །

[Block 129]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་སྤྲུལ་པའི་སྐུ་ལས་མི་འདའ་ལ། སྤྲུལ་པའི་སྐུའི་དེ་ཁོ་ན་ཉིད་དང་ཆོས་འགྲུབ་པར་བྱེད་པའི་ཐབས་སྦྱོར་བ་ཡན་ལག་དྲུག་ནི་གསང་བ་འདུས་པ་ནས་ཉེ་བར་བསྟན་ཏོ། །

[Block 130]
དེ༌[^73]གསལ་བར་སྟོན་པའི་ཕྱིར་བྱམས་པས་ཞུས་པའི་རྒྱུད་ཕྱི་མ་གསུངས་སོ། །

[Block 131]
དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་བཤད་པའི་ཚུལ་རྣམ་པ་བཞི་ལས་མི་འདའ་ལ། དེ་གསལ་བར་བྱ་བའི་དོན་དུ་གསང་བའི་རྒྱུད་རྡོ་རྗེ་ཕྲེང་བ་གསུངས་སོ། །

[Block 132]
དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་ཐུགས་རྗེ་ཆེན་པོའི་སྟོབས་ཀྱིས༌[^74]སེམས་ཅན་ལ་ཆོས་སྟོན་པ་ལས་མི་འདའ་ལ། དེ་གསལ་བར་བྱེད་པའི་རྒྱུད་ནི་དཔལ་ཕྱག་ན་རྡོ་རྗེས་ཞུས་པ་ཡེ་ཤེས་རྡོ་རྗེ་ཀུན་ལས་བཏུས་པའི་རྒྱུད་གསུངས་སོ། །

[Block 133]
དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་རྨད་དུ་བྱུང་བའི་སྤྱོད་པ་ལས་མི་འདའ་ལ། དེ་གསལ་བར་བྱེད་པའི་རྒྱུད་ནི་སྤྱོད་པ་མཆོག་གི་རྒྱུད་གསུངས་སོ། །

[Block 134]
དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་ཐོབ་པ་དང་རྩོལ་བ་དངོས་གྲུབ་རྣམ་པ་གཉིས་ལས་མི་འདའ་ལ། དེ་གསལ་བར་བྱེད་པའི་རྒྱུད་ནི་དངོས་གྲུབ་སྟོན་པར༌[^75]བྱེད་པ་ཞེས་བྱ་བའི་རྒྱུད་གསུངས་སོ། །

[Block 135]
དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་དབང་དང་དམ་ཚིག་ལས་མི་འདའ་ལ། དེ་གསལ་བར་བྱེད་པའི་རྒྱུད་ནི་དམ་ཚིག་གི་དེ་ཁོ་ན་ཉིད་ཉེ་བར་འབྱེད་པའི་རྒྱུད་གསུངས་སོ། །

[Block 136]
དེ་བཞིན་གཤེགས་པ་རྣམས༌[^76]ནི་བསྐྱེད་པའི་རིམ་པ་དང་ལྷའི་རྣལ་འབྱོར་གྱི་རྫོགས་པའི་རིམ་པ་ལས་མི་འདའ་ལ། དེ་གསལ་བར་བྱེད་པའི་རྒྱུད་ནི་རྡོ་རྗེ་རྣོན་པོའི་རྒྱུད་གསུངས་སོ། །

[Block 137]
དེ་བས་ན་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་དང་གསུང་དང་ཐུགས་གསང་བ་འདུས་པ་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་རྣམས་ཀྱིས་ཤིན་ཏུ་རྒྱས་བཏབ་པ། ཤིན་ཏུ་ཟབ་པ། ཤིན་ཏུ་རྨད་དུ་བྱུང་བ། ཤིན་ཏུ་རྟོགས་པར་དཀའ་བ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ཀྱིས་ཀྱང་རྙེད་པར་དཀའ་བས་མཆོག་ཏུ་དམ་པར་གྱུར་པ་རྣམས་ཀྱི་སྤྱོད་ཡུལ་དུ་གྱུར་པ་ཡིན་པའི་ཕྱིར་དད་པའི་རྗེས་སུ་འབྲང་བ༌[^77]དང་། ཆོས་ཀྱི་རྗེས་སུ་འབྲང་བ༌[^78]རྣམས་ཀྱིས་རྣལ་འབྱོར་གྱི་རྒྱུད་དང་། བྱང་ཆུབ་སེམས་དཔའ་བྱམས་པའི་ཊཱི་ཀཱ་དང་། བྱང་ཆུབ་སེམས་དཔའ་པདྨའི་མན་ངག་ལ་བརྟེན་ཏེ་རྟོགས་པར་བྱའོ། །

[Block 138]
དེ་ལྟར་བཤད་པར་དམ་བཅའ་བ་བསྟན་ནས། ད་ནི་དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་མདོར་བསྡུས་ཏེ་བསྟན་པར་བྱའོ། །

[Block 139]
དེའི་ཕྱིར། གསང་སྔགས་སྐུ་ནི་རབ་ཏུ་སྒྲུབ་པར༌[^79]བྱེད། །ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། སྐུ་སྒྲུབ་པར་བྱེད་པ་ནི་བསྐྱེད་པའི་རིམ་པ་ཡིན་ལ། སྔགས་སྒྲུབ་པར་བྱེད་པ་ནི་རིམ་པ་དང་པོ་ཡིན་པས་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 140]
རིམ་པ་ཞེས་བྱ་བ༌[^80]ནི་གཉི་ག་ལ་སྦྱར་བར་བྱའོ། །

[Block 141]
འདིས་ནི་བསྐྱེད་པའི་རིམ་པ་ཡང་གཟུང་བར་བྱའོ། །

[Block 142]
རིམ་པ་དང་པོ་ཞེས་སྨོས་པ་མ་ཡིན་ནམ། དེ་ཅིའི་ཕྱིར་གཉི་ག་ལ་དང་པོ་ཞེས་བརྗོད་ཅེ་ན་འདི་ནི་རྫོགས་པའི་རིམ་པ་འབའ་ཞིག་གི་དབང་དུ་བྱས་པ་ཡིན་གྱི། བསྐྱེད་པའི་རིམ་པ་དང་ཐུན་མོང་དུ་ནི་མ་ཡིན་ནོ། །

[Block 143]
རིམ་པ་དང་པོ་ཞེས་བྱ་བ་འདི་ཡང་གང་ཞིག་ཅེ་ན། འདི་ནི་རྡོ་རྗེ་བཟླས་པ་ཉིད་དོ། །

[Block 144]
རིམ་པ་གཉིས་པ་བརྗོད་པའི་ཕྱིར།

[Block 145 [VERSE]]
སེམས་ལ་དམིགས་པ་ཙམ་ཞིག་ནི། །
རིམ་པ་གཉིས་པ་ཞེས་བརྗོད་དོ། །
--- END BLOCKS ---
