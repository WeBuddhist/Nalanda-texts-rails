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
ཁ་ཏོན་བྱས་པའི་བསོད་ནམས་སེམས་ཅན་ཀུན་གྱི་དོན་དུ་བསྔོ་བའོ།། །།

[Block 107 [HEADING]]
### དེ་བཞིན་གཤེགས་པ་ལ་ཕྱག་འཚལ་བ། ^3-2-0

[Block 108 [VERSE]]
གདོང་དང་སོ་ཡི་དྲི་བཀྲུས་ནས། །
རྫོགས་སངས་རྒྱས་ལ་གུས་ཕྱག་བྱ། །

[Block 109]
ཞེས་བྱ་བས་དེ་བཞིན་གཤེགས་པ་ལ་ཕྱག་བྱ་བ་བསྟན་ཏེ། ལངས་ནས་ཆུ་དང་སོ་ཤིང་ལ་སོགས་པས་སོ་དང་གདོང་གི་དྲི་མ་བཀྲུས་ནས་རྫོགས་སངས་རྒྱས་ཏེ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ལ་གུས་པས་ཕྱག་བྱའོ། །

[Block 110]
དེ་ལ་ཆོས་ཐམས་ཅད་ཐུགས་སུ་ཆུད་ཅིང་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་མ་ལུས་པར་བརྙེས་པས༌[^48]ན་རྫོགས་པ་ཞེས་བྱའོ། །

[Block 111]
སྐྱེས་བུ་གཉིད་ལས་སངས་པ་བཞིན་དུ་མ་རིག་པ་སྤངས་ནས། མ་རིག་པའི་གཉིད་ལས་སངས་པས་ན་སངས་རྒྱས་ཞེས་བྱའོ། །

[Block 112]
གུས་ཕྱག་བྱ་ཞེས་བྱ་བས་གུས་པར་ཕྱག་བྱ་བ་ལ༌[^49]ཡང་རྣམ་པ་གསུམ་སྟེ། ལུས་ཀྱིས་གུས་པར་ཕྱག་བྱ་བ་དང་། ངག་གིས་གུས་པར་ཕྱག་བྱ་བ་དང་། ཡིད་ཀྱིས་གུས་པར་ཕྱག་བྱ་བའོ། །

[Block 113]
དེ་ལ་ལུས་སྨད༌[^50]ལྔ་ས་ལ་གཏུགས་ཏེ་ཞི་བའི་ཚུལ་གྱིས་ཕྱག་བྱ་བ་ནི་ལུས་ཀྱིས་གུས་པར་ཕྱག་བྱ་བའོ། །

[Block 114]
མི་དྲག་མི་ངལ་བའི་དབྱངས་ཀྱིས་དེ་བཞིན་གཤེགས་པ་ལ་བསྟོད་པ་ནི་ངག་གིས་གུས་པར་ཕྱག་བྱ་བའོ། །

[Block 115]
ལུས་ཀྱིས་གུས་པར་ཕྱག་བྱ་བའི་སྔོན་རོལ་དུ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ནི་ཉེས་པ་ཐམས་ཅད་སྤངས་པས༌[^51]ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པ་ཐུགས་རྗེ་ཆེན་པོ་ཅན་ཞེས་སེམས་ཅན་ཐམས་ཅད་ཀྱི་མགོན་དང་སྐྱབས་སུ་གྱུར་པ། འགྲོ་བ་ཐམས་ཅད་ཀྱི་བསོད་ནམས་ཀྱི་གཞི་ཡིན་པས་ཕྱག་བྱ་བའི་གནས་ཡིན་ནོ་སྙམ་དུ་སེམས་པ་ནི་ཡིད་ཀྱིས༌[^52]གུས་པར་ཕྱག་བྱ་བ་སྟེ། དེ་ལྟ་བུའི་སེམས་སྔར་བསྐྱེད་ལ་དེ་ནས་གདོད་ལུས་ངག་གིས་ཕྱག་བྱ་བས་ཕྱག་བྱའོ།། །།

[Block 116 [HEADING]]
### མཁན་པོ་དང་སློབ་དཔོན་ལ་སྙུན་གསོལ་ནས་ལས་སུ་བྱ་བ་ཞུ་བ། ^3-3-0

[Block 117 [VERSE]]
བླ་མ་གནས་པའི་སྒོ་གླེགས་ལ། །
ལག་པས་དལ་གྱིས༌[^53]བརྡུང་བར་བྱ། །
ནང་ཞུགས་གུས་པར་བླ་མ་ལ། །
ཁམས་བདེ་མི་བདེ་ལ་སོགས་དྲི། །

[Block 118 [VERSE]]
འདི་དག་བྱ་ཞེས་དྲིས་ནས་ནི། །
དཀྱིལ་འཁོར་ལ་སོགས་རྣམ་བྱའི་ཕྱིར། །

[Block 119]
ཞེས་བྱ་བས་མཁན་པོ་དང་སློབ་དཔོན་ལ་སྙུན༌[^54]གསོལ་ནས་ལས་སུ་བྱ་བ་ཞུ་བ་བསྟན་ཏེ།

[Block 120 [VERSE]]
བླ་མ་གནས་པའི་སྒོ་གླེགས་ལ། །
ལག་པས་དལ་གྱིས་བརྡུང་བར་བྱ། །

[Block 121]
ཞེས་བྱ་བ་ལ་དེ་ལྟར་སངས་རྒྱས་ལ་ཕྱག་བྱས་པའི་འོག་ཏུ་བླ་མ་སྟེ་མཁན་པོ་དང་སློབ་དཔོན་གྱི་གནས་སུ་སོང་ལ་སྒོ་འཕར་ལ་ལག་པས་དལ་གྱིས་བརྡུང་བའམ། སེ་གོལ་གཏོགས་ཏེ་ནང་དུ་ཤོག་ཅིག་ཅེས་ཟེར་ན་ནང་དུ་འགྲོ་བར་བྱའོ། །

[Block 122]
དེ་ལྟར་སྒྲ་མ་བྱུང་ན་ཡང་ལན་གཉིས་ཀྱི་བར་དུ་དེ་བཞིན་དུ་བྱའོ། །

[Block 123]
དེ་སྟེ་སྒྲ་མ་བྱུང་ན་ཡང་ལན་གཉིས་ལན་གསུམ་གྱི་བར་དུ་དེ་བཞིན་དུ་བྱའོ། །

[Block 124]
དེ་ནས་ནང་དུ་ཤོག་ཅིག་ན་གདོད་ནང་དུ་འགྲོ་བར་བྱའོ། །

[Block 125]
ཐུག༌[^55]ཐུབ་ཏུ་མི་བྱ་བར་ཚུལ་འདི་ལྟར་བྱ་བ་ནི་དགེ་སྦྱོང་གི་ཚུལ་ཞི་བ་དང་དུལ་བའི་རང་བཞིན་ཡིན་པའི་ཚུལ་བསྟན་པར་བྱ་བ་དང་། ཐུག༌[^56]ཐུབ་ཏུ་ཞུགས་ན་བླ་མ་རྣམས་ཀྱིས༌[^57]དགེ་བའི་བར་ཆད་དུ་གྱུར༌[^58]ཞིང་སེམས་འཁྲུག་པར་འགྱུར་བས་བླ་མའི་སེམས་མི་འཁྲུག་པར་བྱ་བའི་ཕྱིར་ཚུལ་དེ་ལྟར་བྱའོ། །

[Block 126]
དེ་ནས་བླ་མས་ནང་དུ་ཤོག་ཅིག་ཅེས་སྨྲས་ཏེ་ནང་དུ་ཞུགས་ནས་ཅི་བྱ་ཞེ་ན། དེའི་ཕྱིར།

[Block 127 [VERSE]]
ནང་ཞུགས་གུས་པས་བླ་མ་ལ། །
ཁམས་བདེ་མི་བདེ་ལ་སོགས་དྲི། །

[Block 128]
ཞེས་བྱ་བ་སྨོས་ཏེ། ཁམས་ཀྱི་སྒྲས་ནི་ས་དང་ཆུ་དང་མེ་དང་རླུང་དང་འབྱུང་བ་ཆེན་པོ་བཞི་ལ་བྱ་སྟེ། འབྱུང་བ་ཆེན་པོ་བཞི་ཤས་ཆེ་ཆུང་དུ་གྱུར་པ་ལས་ནད་དུ་འགྱུར་རོ། །

[Block 129]
དེ་ལ་སའི་ཁམས་ཤས་ཆེ་ན་ནི་ཁ་ཟས་མི་འཇུ་ཞིང་ལུས་ལྕིའོ། །

[Block 130]
ཆུའི་ཁམས་ཤས་ཆེ་ན་ནི་བད་ཀན་ཤས་ཆེའོ། །

[Block 131]
མེའི་ཁམས་ཤས་ཆེ་ན་ནི་མཁྲིས་པ་ཅན་དུ་འགྱུར་རོ། །

[Block 132]
རླུང་གི་ཁམས་ཤས་ཆེ་ན༌[^59]ནི་རླུང་ནད་ཅན་དུ་འགྱུར་རོ། །

[Block 133]
དེ་ལྟར་ནང་དུ་ཞུགས་ནས་ཞི་བ་དང་དུ་ལ་བ་དང་སྲིད༌[^60]ཞུའི་ཚུལ་གྱིས་ཕྱག་བྱ་སྟེ། ཁམས་བཞི་མ༌[^61]སྙོམས་པ་ལས་སྙུན༌[^62]དུ་གྱུར་པ་མཆིས་སམ་མ་མཆིས་སྙུན༌[^63]གསོལ་ལོ། །

[Block 134]
སོགས་པའི༌[^64]སྒྲས་ནི་མཚན་མོ་བདེ་བར་མནལ་ལམ་མ་མནལ། དགོངས་པ་ལ་བར་ཆད་དུ་གྱུར་ཏམ་མ་གྱུར་ཞེས་བྱའོ། །

[Block 135]
དེ་ལྟར་སྙུན༌[^65]གསོལ་ནས་ཅི་ཞིག་བྱ་ཞེ་ན། དེའི་ཕྱིར་ན།

[Block 136 [VERSE]]
འདི་དག་བྱ་ཞེས་དྲིས་ནས་ནི། །
དཀྱིལ་འཁོར་ལ་སོགས་རྣམ་བྱའི་ཕྱིར། །

[Block 137]
ཞེས་བྱ་བ་སྨོས་ཏེ། སྙུན༌[^66]གསོལ་བའི་འོག་ཏུ་མཆོད་རྟེན་ལ་ཕྱག་བྱ་ཞིང་བསྐོར་བ་དང་བཤང་གཅི་ཆེ་ཆུང་དུ་འགྲོ་བ་མ་གཏོགས་པར་ནང་པར་སྔ་དྲོའི་བར་དུ་ཅི་དང་ཅི་བྱ་བ་ཐམས་ཅད་ཞུའོ། །

[Block 138]
དེ་ལྟར་ཞུས༌[^67]པའི་འོག་ཏུ་དཀྱིལ་འཁོར་བྱས་ལ་དེ་ནས་གདོད་གཡར་ཚུས་བཟའོ། །

[Block 139]
སོགས་པའི༌[^68]སྒྲས་ནི་མེ་ཏོག་དང་བདུག་པ་ལ་སོགས་པ་མཆོད་པ་ཡང་བསྡུའོ། །

[Block 140 [HEADING]]
### ཆུ་བརྟག་པ། ^3-4-0

[Block 141 [VERSE]]
ཉ་ཕྱིས་ལ་སོགས་ཆུ་བརྟགས་ཏེ། །
སྟེང་དང་བར་གཏིང་རིམ་བཞིན་ནོ། །
ཉ་ཕྱིས་ལ་སོགས་མེད་ན་ཡང་། །
ཁྱོར་བའམ་འདབ་མས་བུམ་པ་དགང་། །

[Block 142 [VERSE]]
ཆུ་ཡི་སྐྱེ་བོ་ཆེ་ཆུང་རྣམས། །
ཡུན་མི་རིང་བར་ནན་ཏན་བརྟག །
སྙིང་རྗེ་ཅན་གྱིས༌[^69]ཁུ་བ་རྣམས། །
རབ་ཏུ་བརྟགས་ཏེ་སྤྱད་པར་བྱ། །

[Block 143 [VERSE]]
སྲོག་ཆགས་ཡོད་ན་ལེགས་པར་བཙག །
སྲོག་ཆགས་རྣམས་ལ་གནོད་མི་བྱ། །
རྩྭ༌[^70]དང་ལྕི་བ་ཤིང་ལ་སོགས། །
དགོས་པ་གང་དང་གང་ཡང་རུང་། །

[Block 144]
དེ་དག་སྲོག་ཆགས་མེད་པར་བྱ། །སྡོམ་པས་སྲོག་ཆགས་གསད་པ༌[^71]སྲུང་།[^72] ། ཞེས་བྱ་བས་ཆུ་ལ་སོགས་པ་བརྟག་པར་བསྟན་ཏེ། དེ་དག༌[^73]དཀྱིལ་འཁོར་བྱས་ནས་གཡར་ཚུས་ཐོབ་པའི་འོག་ཏུ་ཅི་བྱ་ཞེ་ན། དེའི་ཕྱིར། ཉ་ཕྱིས་ལ་སོགས་ཆུ་བརྟགས་ཏེ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དེའི་འོག་ཏུ་ཆུ་ཚགས་ལྔ་འདུལ་བ་ལས་གསུངས་པའི་ཆུ་ཚགས་གང་ཡང་རུང་བ་ཅིག་གིས་ཆུ་བཙག་གོ། །

[Block 145]
དེ་ལ་ཆུ་ཚགས་ལྔ་ནི་རིལ་བ་དང་། གྲུ་གསུམ་པ་དང་། ཡུ་བ་ཅན་དང་། ཆོས་ཅན་ཞེས་བྱ་བ་དང་། གྲོལ་བར་བྱེད་པའི་རས་སོ། །
--- END BLOCKS ---
