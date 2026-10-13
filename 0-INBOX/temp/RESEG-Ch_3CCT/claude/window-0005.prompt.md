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
[Block 176]
དབབ་པ་ནི་འདར་བ་དང་འཕར་བ་དང་། སྨྲ་བ་ལ་བརྟག་པའོ། །

[Block 177]
དྲི་བ་ནི་དཀར་པོ་ལ་སོགས་པ་བརྟག་པའོ། །

[Block 178]
མེ་ཏོག་ནི་སྐུའི་སྟོད་དང་སྨད་དང་གཙོ་བོ་དང་འཁོར་ལ་ཕོག་པ༌[^72]དང་མ་ཕོག་པ༌[^73]བརྟག་པའོ། །

[Block 179]
བརྡ་ཡང་གང་ཡིན་ཞེ་ན།

[Block 180 [VERSE]]
བུམ་པའི་དབང་དང་ལྡན་རྣམས་ཀྱིས། །
ལྔ་བསྡུས་ཕྱག་རྒྱ་བསྟན་པར་བྱ། །

[Block 181]
ཞེས་པ་ནི་བུམ་པའི་དབང་ཐོབ་པ་རྣམས་ཀྱིས་ཉན་ཐོས་དང་མུ་སྟེགས་ལ་སོགས་པ་འདྲི་བ་ལ་གཡོན་གྱི་སོར་མོ་བསྡུས་པའི་སྟེང་དུ་གཡས་ཀྱི་སྲིན་ལག་གམ་གུང་མོ་བཞག་པའམ་ཡང་ན་དེའི་སྟེང་དུ་ལྔ་བཞག་པ་འདི་ནི་བུམ་པའི་དབང་གི་བརྡ་ཡིན་ནོ། །ཞེས་གསུངས་སོ། །

[Block 182]
བསམ་གཏན་ཡང་ཇི་ལྟར་བྱ་ཞེ་ན།

[Block 183 [VERSE]]
བྱང་ཆུབ་སེམས་ཀྱིས༌[^74]རྒྱས་པ་དང་། །
ལྷ་མོས༌[^75]རྫས་སྟེར་ལ་སོགས་པ། །
ཇི་ལྟར་བསྒོམས་པ༌[^76]བསམ་གཏན་ཏེ། །
དམ་པ་རྣམས་ཀྱིས་དེ་བཞིན་བཤད། །

[Block 184]
ཅེས་པ་ནི་ནམ་མཁའ་ལས་ལྷ་མོ་བྱུང་བ་དང་། སློབ་དཔོན་གྱིས་བསྐུལ་བ་དང་། ལུས་ལ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་རྒྱས་པ་དང་། གནས་གང་དུ་རྫས་གང་གིས་དབང་བསྐུར༌[^77]བ་དང་། དྲི་མ་ཐོན་པ་དང་། རིགས་ལྔའི་སྐུར་ལངས་པ་ལ་སོགས་པ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་འདི་ནི་བསམ་གཏན་ནོ། །

[Block 185]
དེས་ཀྱང་ནུས་པ་ཅི་ཡོད་ཅེ་ན།

[Block 186 [VERSE]]
བག་ཆགས་སྦྱོང་བར་བྱེད་པ་དང་། །
དྲི་མ་འཁྲུ་བར་བྱེད་པའོ། །

[Block 187]
ཞེས་པ་འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་དང་ང་རྒྱལ་དང་། ཕྲག་དོག་གི་དྲི་མ་འཁྲུ་ཞིང་དེའི༌[^78]བག་ཆགས་སྦྱོང་བར་བྱེད་པ་སྟེ། ཡང་ན་རེ་རེ་ལ་རིམ་པ་བཞིན་དུ་སྦྱར་རོ། །

[Block 188]
དེ་ལ་བུམ་པའི་དབང་བསྐུར་ནས་དེ་དང་འབྲེལ་པའི་མན་ངག་ཀྱང་གང་བསྟན་ཞེ་ན།

[Block 189 [VERSE]]
ཞི་བ་ལ་སོགས་ལས་རྣམས་དང་། །
བསྐྱེད་པ་དང་ནི་དེ་མཐུན་གཞན། །

[Block 190]
ཞེས༌[^79]བྱ་བར་སྦྱར་རོ། །

[Block 191]
དེའི་དོན་ཡང་བསྐྱེད་པའི་རིམ་པས་སེམས་གཟུང་བ་དང་། བཅས་པ་དང་། དེའི་སྒོ་ནས་ཞི་བ་ལ་སོགས་པའི་ཆོ་གས་ས་འོག་དང་རི་ལུ༌[^80]ལ་སོགས་པའི་དངོས་གྲུབ་གང་འགྲུབ་པའི་ཐབས་དང་། གཞན་ཡང་བུམ་པ་ལ་སོགས་པའི༌[^81]དབང་བསྐུར་བའི་དཀྱིལ་འཁོར་གྱི༌[^82]ཆོ་ག་ལ་སོགས་པ་རྒྱས་པ༌[^83]ཐམས་ཅད་བསྟན་པར་བྱའོ། །

[Block 192]
དེའང་ཚོགས་གང་དང་འབྲེལ་ཞེ་ན།

[Block 193 [VERSE]]
ཐུན་མོང་ཚོགས་དང་དེ་བཞིན་དུ། །
ཞི་ལ་སོགས་པའི་སྦྱོར་བའོ། །

[Block 194]
ཞེས་པ་ཐུན་མོང་གི་ཚོགས་དང་། རེངས་པ་དང་བཀུག་པ༌[^84]དང་། རྨོངས་པ་ལ་སོགས་པའི་ཚོགས་ཀྱི་འཁོར་ལོ་དང་། །མཆོད་པ་དང་འབྲེལ་པར་ཤེས་པར་བྱའོ། །

[Block 195]
འོ་ན་དངོས་གྲུབ་ཀྱང་གང་དང་འབྲེལ་ཞེ་ན།

[Block 196 [VERSE]]
གང་ཞིག་བུམ་པའི་དབང་ཐོབ་ནས། །
ཅི་སྲིད་ཐུན་མོང་དངོས་གྲུབ་འགྱུར། །

[Block 197]
ཞེས་པ་གང་ཞིག་གིས་གང༌[^85]ལ་བུམ་པའི་དབང་བསྐུར་ནས་གང་གིས་ཐོབ་པ་དེས་ནི་ཞི་བ་ལ་སོགས་པའི་དངོས་གྲུབ་གང་ཡང་ཐོགས་པ་མེད་པར་འགྱུར་རོ། །

[Block 198]
འོ་ན་འབྲས་བུའང་གང་ཞིག་ཐོབ་པར་འགྱུར་ཞེ་ན།

[Block 199 [VERSE]]
བདེ་གཤེགས་སྐུ་ཡི་དངོས་གྲུབ་ནི། །
གང་ཚེ་འདི་ཡིས་ཐོབ༌[^86]པར་འགྱུར། །

[Block 200]
ཞེས་པ༌[^87]གང་ཞིག་གི་གང༌[^88]ལ་གང་ཐོབ་པར་འགྱུར་བ་དེས་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་རྡོ་རྗེའི་དངོས་གྲུབ་རྡོ་རྗེ་བཞིན་ཐོགས་པ་མེད་པར་འགྱུར་རོ། །

[Block 201]
འོ་ན་རྒྱུད་གང་དང་འབྲེལ་པ་ཡིན་ཞེ་ན། ཐུན་མོང་མན་ངག་སྟོན་པ་ཡི། །རྒྱུད་དང་འབྲེལ་ལོ་ཞེས་པ་གང་ལ་ཐུན་མོང་གི་སྦྱོར་བ་སྟོན་པའི་རྒྱུད་དང་འབྲེལ་པར་བྱའོ། །

[Block 202]
འོ་ན་རྣལ་འབྱོར་གང་དང་འབྲེལ་པ་ཡིན་ཞེ་ན།

[Block 203 [VERSE]]
བསྐྱེད་པ་ཡི་ནི་རྣལ་འབྱོར་ལ། །
བུམ་པའི་སྦྱོར་བས་འགྲུབ་པ་ཡིན། །

[Block 204]
ཞེས་པ་གང་ལ་བུམ་པའི་དབང་བསྐུར་བ་དེས་ནི་བསྐྱེད་པའི་རིམ་པའི་ཏིང་ངེ་འཛིན་ལ་གནས་པར་བྱའོ། །

[Block 205]
མན་ངག་དེའང་གང་ཟག་གང་ལ་བསྟན་ཞེ་ན།

[Block 206 [VERSE]]
བུམ་པ་དང་འབྲེལ་མན་ངག་ནི། །
གང་ཟག་གཉི་གའི་ཐུན་མོང་ངོ་། །

[Block 207]
ཞེས་པ་ཐུན་མོང་གི་དངོས་གྲུབ་སྒྲུབ་པའི་ཐབས་དང་བསྐྱེད་པའི་རིམ་པ་ནི་ཚོགས་དང་སློབ་མ་གཉི་གའི་ཐུན་མོང་དུ་གྱུར་པའོ།། །།

[Block 208]
དེ་ལྟར་བུམ་པའི་དབང་བསྐུར་བའི་ཐབས་ལ་སོགས་པ༌[^89]རྒྱས་པར་བཤད་ནས། ད་ནི་སློབ་མའི་དབང་དུ་བྱས་ཏེ། གསང་བའི་དབང་བསྐུར་བཤད་པར་བྱ་སྟེ། དེ་ལ་གསང་བའི་དབང་གི་ངོ་བོའང་གང་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བཤད་པ། གང་ཞིག་གསང་བ་བྱང་ཆུབ་སེམས། །ཞེས་པ་ལ་གསང་བའི་དབང་གི་ངོ་བོ་ནི་ཁྱད་པར་ཅན་གྱི་བྱང་ཆུབ་སེམས་སོ། །

[Block 209]
འོ་ན་བྱང་ཆུབ་སེམས་ཞེས་བྱ་བ་ནི་ཅི་ཞིག །ནུས་པ་ཞེས་བྱ་བ་མ་ཡིན་ནམ་ཞེ་ན།

[Block 210 [VERSE]]
བསམ་གཏན་ལས་བྱུང་བྱང་ཆུབ་སེམས། །
གཞན་གྱིས་ནུས་པ་མ་སྤངས་པའོ། །

[Block 211]
ཞེས་པ་གང་བསམ་གཏན་དང༌[^90]ལྡན་པ་ལས་བྱུང་བའི་བྱང་ཆུབ་སེམས་འཐོར་བ་ལ་སོགས་པའི་ཉེས་པ་དང་བྲལ་བ༌[^91]སྟེ། དེས་ནི་ངག་གི་སྡིག་པ་སྦྱོང་བར་བྱེད་པ་ཉིད་ཀྱི་ནུས་པ་ཡོད་པས་ནུས་པ་ཞེས་བྱ་བ་ནི་འདིར་མ་སྤངས་པའོ། །

[Block 212]
ངེས་པའི་ཚིག་བསྙད་པ་འདི་ཅིའི་ཕྱིར་གསང་བའི་དབང་ཡིན་སྙམ་པ་ལ།

[Block 213 [VERSE]]
གང་ཞིག་གསང་ལ་བྱང་ཆུབ་སེམས། །
ངག་ལ་བསྐུར་བར་བྱེད་ཕྱིར་རོ། །

[Block 214]
ཞེས་པ་ལ་གསང་བར༌[^92]བྱ་བ་ཉིད་དང་། བྱང་ཆུབ་སེམས་ཡིན་པ་ཉིད་དང་། ངག་གི་རྟོག་པ་སྦྱོང་བར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 215]
གསང་བའི་དབང་ཞེས་བྱ་བའང་དུ་ཞིག་ཅེ་ན།
--- END BLOCKS ---
