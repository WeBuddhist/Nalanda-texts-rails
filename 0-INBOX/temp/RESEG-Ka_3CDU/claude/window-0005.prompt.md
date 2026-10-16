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
[Block 176 [VERSE]]
སྟན་ཆུ་ས་དང་སོ་ཤིང་དང་། །
འདག་པའི་ཆལ་ཡང་སྟ་གོན་བྱ། །

[Block 177]
ཞེས་བྱ་བ་སྨོས་ཏེ། མཁན་པོ་དང་སློབ་དཔོན་གྱི་ལས་སུ་བྱ་བ་ནི་ནང་པར་མཁན་པོ་དང་སློབ་དཔོན་གང་དུ་ཁ་གདོང་བཀྲུ་བའི་གནས་སུ་གདན་གདིང་བ་དང་། བཀྲུ་བའི་ཆུ་དང་སོ་ཤིང་དང་། འདག་པའི་ཆལ་ལ་སོགས་པ་སྟ་གོན་བྱ་སྟེ། གཤེགས་པ་དང་། བཤང་གཅི་བྱེད་པའི་གནས་སུ་ས་དང་འདབ་མ་དག་ཀྱང་སྟ་གོན་བྱས་ཏེ་བཞག་གོ། །

[Block 178]
དེ་ཙམ་ཞིག་བྱས་པས་ཆོག་གམ་ཞེ་ན། མི་ཆོག་པར་བསྟན་པའི་ཕྱིར། ལྷུང་བཟེད་བཀྲུ་ལ་སོགས་པ་དང་། །ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་མཁན་པོ་དང་སློབ་དཔོན་གྱི་ལྷུང་བཟེད་བཀྲུའོ། །

[Block 179]
སོགས་པའི༌[^103]སྒྲས་ནི་ཆོས་གོས་བཀྲུ་ཞིང་བཙེམ་པ་དང་གནས་བྱི་དོར་བྱ་བ་ལ་སོགས་པ་ལས་སུ་བྱ་བ་ཐམས་ཅད་བྱའོ། །

[Block 180 [HEADING]]
### ཞུ་བ། ^3-6-0

[Block 181 [VERSE]]
དེ་ནས་དུས་རིག་ཕྱག་བྱ་སྟེ། །
དེ་བཞིན་གུས་པར་ཐལ་སྦྱར་ནས། །
ཟས་བཟའ་བྱ་ཞེས་བླ་མ་ལ། །
བརྟུལ༌[^104]ཞུགས་ཅན་གྱིས་དེ་ལྟར་ཞུ། །

[Block 182]
ཞེས་བྱ་བས་ཞུས་ནས་ཟས་བཟའ་བ་བསྟན་ཏེ། དེ་ནས་ཞེས་བྱ་བས་ནི་བླ་མའི་དགོས་པ་ཐམས་ཅད་བྱས་པའི་འོག་ཏུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 183]
དུས་རིག་ཕྱག་བྱས་ལ་དགེ་སློང་རྣམས་ཀྱི་ཟས་བཟའ་བའོ། །

[Block 184]
དུས་ནི་སྐྱ་རེངས༌[^105]ཤར་བ་ནས་བརྩམས་ཏེ། འཛམ་བུའི་གླིང་གི་ཉི་མ་དྲོས་མན་ཆད་དེ། དེའི་བར་དུ་ཟས་བཟའ་བར་གནང་བའི་དུས་རིག་ནས་ཞེས་བྱའོ། །

[Block 185]
ཕྱག་བྱས་ཏེ། དེ་བཞིན་གུས་པས༌[^106]ཐལ་སྦྱར་ནས། །ཞེས་བྱ་བ་ལ་མཁན་པོའམ་སློབ་དཔོན་ལ་ཕྱག་བྱས་ཏེ། དེ་བཞིན་ནང་པར་སྔར་ཞུས་པ༌[^107]བཞིན་དུ་ལུས་ཀྱིས༌[^108]མ་གུས་པ་རྐང་པ་བརྐྱང་བ་དང་། ལག་པ་བརྐྱང་བ་ལ་སོགས་པ་བྱེད་པ་དང་། ངག་གིས༌[^109]མ་གུས་པ་རྟ་གད་བྱེད་པ་ལ་སོགས་པ་བཏང་ལ། ལུས་དང་ངག་ཞི་བ་དང་དུལ་བར་བྱ་སྟེ། ཐལ་མོ་སྦྱར་ལ་འཚལ་མ་འཚལ། །ཞེས་བླ་མ་མཁན་པོ་དང་སློབ་དཔོན་ལ་བརྟུལ་ཞུགས་ཅན་དེ་དགེ་སློང༌[^110]གིས་དེ་ལྟར་ཞུའོ། །

[Block 186 [HEADING]]
### ཟས་བཟའ་བ། ^3-7-0

[Block 187 [VERSE]]
ལག་པ་བཀྲུས་ནས་ཚུལ་བཞིན་དུ། །
དེ་ནི་མི་སྨྲ་ཚོད་རིག་བྱ། །

[Block 188]
ཞེས་བྱ་བས་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ལག་པ་བཀྲུས་ནས་ཞེས་བྱ་བ་ནི་ལག་པ་དང་ལྷུང་བཟེད་གཉིས་ཀ་བཀྲུས༌[^111]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 189]
ཚུལ་བཞིན་དུ་ཞེས་བྱ་བས་ནི་ཟས་བཟའ་བའི་ཚེ་གཡས་གཡོན་དུ་མི་བལྟའོ། །

[Block 190 [VERSE]]
ཁ་ཟས་འབྲིམ་པ་ལ་མི་བལྟའོ། །
ཧ་ཅང་ཁམ་ཆེར་མི་ཟའོ། །
དེ་ནི༌[^112]མི་སྨྲ་ཚོད་རིག་བྱ། །

[Block 191]
ཞེས་བྱ་བ་ནི་ཟས་ཟ་བའི་ཚེ་གད་མོ་མི་བགད༌[^113]དོ། །

[Block 192]
གཏམ་མི་བྱའོ། །

[Block 193]
རྐན་སྒྲ་མི་གཏོག༌[^114]གོ། །

[Block 194]
ཅག་ཅག་མི་བྱའོ། །

[Block 195]
ཚོད་རིག་ཅེས་བྱ་བ་ནི་ཧ་ཅང་མང་དུ༌[^115]མི་བཟའ་ལ། ཧ་ཅང་ཉུང་དུ་ཟོས་ན་ཡང་དགེ་བ་བྱེད་མི་ནུས་པས་ཅི་ཙམ་གྱི་དགེ་བ་བྱེད་པ་དེ་ཙམ་གྱི་ཚོད་དེ་ཙམ་ཞིག་བཟའོ།[^116] །

[Block 196 [VERSE]]
བྲུ་བའི་ནད་ལས་བཟློག་པའི་ཕྱིར། །
བཟའོ་སྙམ་པའི་སེམས་ཀྱིས་བཟའ། །

[Block 197]
ཞེས་བྱ་བས་བསམ་པ་ཕུན་སུམ་ཚོགས་པས་བཟའ་བར་བྱ་བ་བསྟན་ཏེ། འདི་ལྟར་ཟས་ཟ་བའི་ཚེ་སྟོབས་ཆེ་བ་དང་གཟུགས་མཛེས་པར་འདོད་པའི་བསམ་པས་ཟོས་ན་ནི་ཟས་ཟོས་པ་དེ་ཉིད་མི་དགེ་བར་འགྱུར་རོ། །

[Block 198]
ཟས་མ་ཟོས་ན་ལུས་ཉམ་ཆུང་བས་དགེ་བ་བྱེད་མི་ནུས་པའི་ཕྱིར་དགེ་བ་བྱེད་པའི་དོན་དུ་ཟས་བཟའོ་སྙམ་པའི་སེམས་ཀྱིས་ཟས་ཟོས་ན་ཟས་ཟོས་པ་དེ་ཉིད་དགེ་བར་འགྱུར་རོ། །

[Block 199]
དེ་གཉིས་གང་དུ་ཡང་མ་གཏོགས་པར་ཁ་ཟས་བཟའོ༌[^117]སྙམ་སྟེ་ཟས་ཟོས་པ་དེ་ཉིད༌[^118]ལུང་མ་བསྟན་དུ་འགྱུར་རོ། །

[Block 200]
དེ་བས་ན་ཟས་ཟ་བའི་ཚེ་ཡང་ཟས་མ་ཟོས་ན་བཀྲེས་པའི་ནད་ཀྱིས་འདེབས་སོ། །

[Block 201]
བཀྲེས་པའི་ནད་ཀྱིས་བཏབ་ན་དགེ་བ་བྱེད་མི་ནུས་པས། ཁ་ཟས་ཟོས་ལ་བཀྲེས་པའི་ནད་བཟློག་ལ་དགེ་བ་བྱའོ་སྙམ་པའི་བསམ་བས་ཟས་བཟའ་བར་བྱ་སྟེ། དེ་ལྟ་བུའི་བསམ་པ་བཟང་པོས་ཟོས་ན་ཁ་ཟས་ཟོས་པ་དེ་དགེ་བར་འགྱུར་རོ། །

[Block 202 [HEADING]]
### བསོད་ནམས་བསྔོ་བ། ^3-8-0

[Block 203 [VERSE]]
ཟོས་ཤིང་དེ་བཞིན་འཐུངས་པ་དང་། །
རུང་བའི་ཆུ་ཡིས་དེ་འོག་ཏུ། །
སྦྱིན་པ་ཡང་དག་འཕེལ་བྱའི་ཕྱིར། །
སྦྱིན་པའི་ཚིགས་བཅད་གཉིས་ཤིག་བརྗོད། །

[Block 204]
ཅེས་བྱ་བས་བསོད་ནམས་བསྔོ་བ་བསྟན་ཏེ། ཟོས་ཤིང་ཞེས་བྱ་བས་ནི་བཟའ་བ་ལྔ་ཟོས་ཤིང་བཅའ་བ་ལྔ་འཆོས་སོ། །

[Block 205]
དེ་ལ་བཟའ་བ་ནི་ཁ་ཟས་ལ་བྱའོ། །

[Block 206]
བཅའ་བ་ནི་སྤྱན་གཟིགས་ལ་བྱའོ། །

[Block 207]
དེ་བཞིན་འཐུངས་པ་དང་ཞེས་བྱ་བས་ནི་བཏུང་བར་བྱ་བ་འཐུངས་པའོ། །

[Block 208]
རུང་བའི་ཆུ་ཡིས་ཞེས་བྱ་བ་ནི་བཙགས་ཤིང་བརྟགས༌[^119]པའི་ཆུས་ལག་པ་དང་ཁ་བཀྲུས་ལ། དེའི་འོག་ཏུ་ལྷུང་བཟེད་ཀྱང་དག་པར་བཀྲུ་བར་བྱའོ། །

[Block 209]
དེའི་འོག་ཏུ།

[Block 210 [VERSE]]
སྦྱིན་པ་ཡང་དག་འཕེལ་བྱའི་ཕྱིར། །
སྦྱིན་པའི་ཚིགས་བཅད་གཉིས་ཤིག་བརྗོད། །

[Block 211]
ཅེས་བྱ་བ་ལ། ལག་པ་དང་ལྷུང་བཟེད་བཀྲུས་པའི་འོག་ཏུ་སྦྱིན་པའི་ཡོན་བདག་གི་སྨོན་ལམ་བདག་དང་གཞན་ལ་གནོད་པར་འགྱུར་བ་བཟློག་སྟེ། སྦྱིན་པའི་འབྲས་བུ་ལྷ་དང་མིའི་ལུས་ཐོབ་པའི་ལོངས་སྤྱོད་ཆེན་པོ་ཐོབ་པར་བྱ་བའི་ཕྱིར་སྦྱིན་པའི་ཡོན་བདག་གི་དོན་དུ་ཚིགས་སུ་བཅད་པ་གཅིག་བཀླགས་པ༌[^120]དང་། ཀླུའི་རྒྱལ་པོ་དགའ་བོ་དང་། ཉེ༌[^121]དགའ་བོའི་དོན་དུ་ཚིགས་སུ་བཅད་པ་གཅིག་བཀླགས་ཏེ༌[^122]དེ་ལྟར་ཚིགས་སུ་བཅད་པ་གཉིས་ཤིག་གདོན་ཏོ། །

[Block 212 [HEADING]]
## དགེ་བ་བྱ་བ། ^4-0

[Block 213 [VERSE]]
མན་ངག་ཡོད་ན་བསམ་གཏན་བྱ། །
རབ་ཏུ་འབད་དེ་བཀླག་པར་བྱ། །
སྡོམ་དང་ཆོ་ག་མཁས་པ་དང་། །
བསྒྲུབ་པ་ལ་ནི་བརྩོན་པར་བྱ། །

[Block 214]
ཞེས་བྱ་བས་དགེ་བ་བྱ་བ་བསྟན་ཏེ། དེ་རྣམ་པ་བཞི་ཡོད་དེ་བསམ་གཏན་བྱ་བ་དང་། བཀླག་པ་དང་། ལྟུང་བ་དང་། མི་ལྟུང་བ་ལ་མཁས་པ་དང་།

[Block 215 [HEADING]]
### བསམ་གཏན་བྱ་བ། ^4-1-0
--- END BLOCKS ---
