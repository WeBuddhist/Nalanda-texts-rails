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
[Block 211]
ཁ་ཅིག་ནི་གཟུགས་ཁོ་ན་ལའོ། །

[Block 212]
ཁ་ཅིག་ནི་གཟུགས་དང་སེམས་དག་ལའོ། །

[Block 213]
དབང་པོ་དག་ཀྱང་རྣམ་པ་གསུམ་སྟེ། དབང་པོ་རྣོན་པོ་དང་། འབྲིང༌[^75]དང་། རྟུལ༌[^76]པོའི་ཕྱིར་རོ། །

[Block 214]
འདོད་པ་ཡང་རྣམ་པ༌[^77]གསུམ་སྟེ། བསྡུས་པ་དང་། བར་མ་དང་། རྒྱ་ཆེན་པོ་འདོད་པའི་ཕྱིར་ཏེ། དེ་དག་ལ་གོ་རིམས་བཞིན་དུ་ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་གསུམ་བསྟན་ཏེ༌[^78]ཞེས་གྲག་གོ། །

[Block 215 [HEADING]]
### ཚོར་བ་དང་འདུ་ཤེས་ལོགས་ཤིག་ཕུང་པོར་གཞག་པ། ^1-11-0

[Block 216]
ཡང་ཅིའི་ཕྱིར་ན་སེམས་ལས་བྱུང་བ་གཞན་རྣམས་ནི་འདུ་བྱེད་ཀྱི་ཕུང་པོ་གཅིག་ཏུ་བསྡུས་ལ་འདུ་ཤེས་དང་ཚོར་བ་དག་ནི་ལོགས་ཤིག་ཏུ་ཕུང་པོར་བྱས་ཤེ་ན། སྨྲས་པ།

[Block 217 [VERSE]]
རྩོད་པའི་རྩ་བར་གྱུར་པ་དང་། །
འཁོར་བའི་རྒྱུ་ཕྱིར་རིམ་རྒྱུའི་ཕྱིར།
སེམས་བྱུང་རྣམས་ལས་ཚོར་བ་དང་། །
འདུ་ཤེས་ལོགས་ཤིག༌[^79]ཕུང་པོར་གཞག །

[Block 218]
རྩོད་པའི་རྩ་བ་དག་ནི་གཉིས་ཏེ་འདོད་པ་ལ་ལྷག་པར་ཞེན་པ་དང་། ལྟ་བ་ལ་ལྷག་པར་ཞེན་པའོ། །

[Block 219]
དེ་གཉིས་ཀྱི་རྒྱུའི་གཙོ་བོ་ནི་གོ་རིམས་བཞིན་དུ་ཚོར་བ་དང་། འདུ་ཤེས་དག་སྟེ། ཚོར་བའི་རོ་མྱངས་པའི་དབང་གིས་ནི་འདོད་པ་རྣམས་ལ་མངོན་པར་ཞེན་ལ། འདུ་ཤེས་ཕྱིན་ཅི་ལོག་གི༌[^80]དབང་གིས་ནི་ལྟ་བ་རྣམས་ལ་སྟེ། དེ་གཉིས་ནི་འཁོར་བའི་རྒྱུའི་གཙོ་བོ་ཡིན་ཏེ། ཚོར་བ་ལ་ཞེན་ཅིང་འདུ་ཤེས་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་ནི་འཁོར་རོ། །

[Block 220]
གང་ཡང་ཕུང་པོའི་གོ་རིམས་ཀྱི་རྒྱུ་སྟོན་པར་འགྱུར་བའི་གོ་རིམས་ཀྱི་རྒྱུ་དེའི་ཕྱིར་ཡང་འདི་གཉིས་ལོགས་ཤིག་ཏུ་ཕུང་པོར་བྱས་པར་རིག་པར༌[^81]བྱའོ། །

[Block 221 [HEADING]]
### ཕུང་པོ་དག་ཏུ་འདུས་མ་བྱས་མ་བཤད་པ། ^1-12-0

[Block 222]
འོ་ན་ཅིའི་ཕྱིར་སྐྱེ་མཆེད་དང་ཁམས་དག་ཏུ་ནི་འདུས་མ་བྱས་བཤད་ལ། [^82]ཕུང་པོ་དག་ཏུ་ནི་མ་ཡིན་ཞེ་ན།

[Block 223 [VERSE]]
ཕུང་པོ་དག༌[^83]ཏུ་འདུས་མ་བྱས། །
དོན་དུ་མི་རུང་ཕྱིར་མ་བཤད། །

[Block 224]
དེ་ནི་ཕུང་པོ་དག་གི་ནང་དུ་བརྗོད་པ་ན་དེ་ནི་གཟུགས་མ༌[^84]ཡིན་ཞིང་། རྣམ་པར་ཤེས་པའི་བར་དུ་ཡང་མ་ཡིན་པས་དོན་དུ་མི་རུང་བའི་ཕྱིར་རེ་ཞིག་དེ་དག་ཉིད༌[^85]ཀྱི་ནང་དུ་བསྡུ་བར་ནི་མི་ནུས་སོ། །

[Block 225]
ཕུང་པོ་དྲུག་པར་བརྗོད་པར་ཡང་མི་ནུས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། དོན་དུ་མི་རུང་བའི་ཕྱིར་ཏེ། སྤུངས་པའི་དོན་ནི་ཕུང་པོའི་དོན་ཏོ་ཞེས་བཤད་ན་འདུས་མ་བྱས་ནི་གཟུགས་བཞིན་དུ་འདི་ལྟར་དེ་དག་ཐམས་ཅད་གཅིག་ཏུ་བསྡུས་ནས་འདུས་མ་བྱས་ཀྱི་ཕུང་པོ་ཞེས་བྱ་བའི་གྲངས་སུ་འགྲོ་བར་འགྱུར་བ་འདས་པ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་ཐ་དད་པ་མ་ཡིན་ནོ། །

[Block 226 [HEADING]]
### ཕུང་པོའི་གོ་རིམས། ^1-13-0

[Block 227 [VERSE]]
རིམ༌[^86]ནི་རགས་དང་ཀུན་ཉོན་མོངས། །
གནོད༌[^87]སོགས་དོན་ཁམས་ཇི་བཞིན་ནོ། །

[Block 228]
གཟུགས་ནི་ཐོགས་པ་དང་བཅས་ཕྱིར༌[^88]རགས་སོ། །

[Block 229]
གཟུགས་ཅན་མ་ཡིན་པ་རྣམས་ཀྱི་ནང་ན་ཡང་ཚོར་བའི་རྒྱུ་བ་རགས་པའི་ཕྱིར་ཏེ། འདི་ལྟར་ངའི་ལག་པ་ལ་ཚོར་རོ། །

[Block 230]
དེའི་རྐང་པ་ལ་ཚོར་རོ་ཞེས་ཐ་སྙད་འདོགས་སོ། །

[Block 231]
འདུ་ཤེས་ནི་གཉིས་པས་ཆེས་རགས་སོ། །

[Block 232]
རྣམ་པར་ཤེས་པ་བས་ནི་འདུ་བྱེད་དེ། དེའི་ཕྱིར་གང་ཆེས༌[^89]རགས་པ་དེ་སྔར་བཤད་དོ། །

[Block 233]
ཡང་ན་ཐོག་མ་མེད་པ་ཅན་འཁོར་བ་ན་ཕོ་དང་མོ་དག་ཕན་ཚུན་གཟུགས་ལ་མངོན་པར་དགའ་སྟེ། དེ་དག་ཀྱང་ཚོར་བའི་རོ་མྱང་བ་ལ་ཆགས་པའི་ཕྱིར་རོ། །

[Block 234]
དེ་ལ་ཆགས་པ་ཡང་འདུ་ཤེས་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 235]
ཕྱིན་ཅི་ལོག་དེ་ཡང་ཀུན་ནས་ཉོན་མོངས་པ་དག་གིས་སོ། །

[Block 236]
སེམས་ཀྱང་དེ་དག་གིས་ཀུན་ནས་ཉོན་མོངས་པ་ཅན་དུ་བྱས་པས་དེའི་ཕྱིར་ཀུན་ནས་ཉོན་མོངས་པའི་གོ་རིམས་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 237]
ཡང་ན་སྣོད་ལ་སོགས་པའི་དོན་གྱིས་ཏེ། གཟུགས་ལ་སོགས་པའི་ཕུང་པོ་ནི་སྣོད་དང་། ཟས་དང་། ཚོད་མ་དང་། བྱན་པོ་དང་། ཟ་བ་པོ་ལྟ་བུའོ། །

[Block 238]
ཡང་ན་ཁམས་ཀྱིས་ཏེ། འདོད་པའི་ཡོན་ཏན་གཟུགས་ཀྱིས་རབ་ཏུ་ཕྱེ་བ་ནི་འདོད་པའི་ཁམས་སོ། །

[Block 239]
ཚོར་བས་རབ་ཏུ་ཕྱེ་བ་ནི་བསམ་གཏན་རྣམས་སོ། །

[Block 240]
འདུ་ཤེས་ཀྱིས་རབ་ཏུ་ཕྱེ་བ་ནི་གཟུགས་མེད་པ་གསུམ་མོ། །

[Block 241]
འདུ་བྱེད་ཙམ་གྱིས་རབ་ཏུ་ཕྱེ་བ་ནི་སྲིད་པའི་རྩེ་མོ་སྟེ། འདི་དག་ནི་རྣམ་པར་ཤེས་པའི་གནས་པ་ཡིན་ལ་དེ་དག་ལ་རྣམ་པར་ཤེས་པ་གནས་སོ་ཞེས་ཕུང་པོའི་གོ་རིམས་ཞིང་དང་ས་བོན་གྱི་གོ་རིམས་ལྟ་བུར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 242]
དེ་ཉིད་ཀྱི་ཕྱིར་ཕུང་པོ་རྣམས་ནི་ལྔ་སྟེ་མི་ཉུང་མི་མང་ངོ་། །རིམ་པའི་རྒྱུ་དེ་ཉིད་ཀྱི་ཕྱིར་ཚོར་བ་དང་། འདུ་ཤེས་དག་ནི་འདུ་བྱེད་རྣམས་ལས་ལོགས་ཤིག་ཏུ་ཕུང་པོར་བྱས་སོ། །

[Block 243]
གང་གི་ཕྱིར་འདི་དག་ནི་ཆེས༌[^90]རགས་པའོ། །

[Block 244 [HEADING]]
### ཁམས་དང་སྐྱེ་མཆེད་དྲུག་གི་གོ་རིམས། ^1-14-0

[Block 245]
མིག་ལ་སོགས་པའི་ཁམས་དང་སྐྱེ་མཆེད་དྲུག་གི་གོ་རིམས་བརྗོད་པར་བྱ་སྟེ། དེའི་དབང་ཉིད་ཀྱིས་ན་དེའི་ཡུལ་དང་རྣམ་པར་ཤེས་པ་རྣམས་ཀྱི་རིམ༌[^91]པའོ། །

[Block 246]
དྲུག་པོ་དེ་དག་ལས་ཀྱང་། ད་ལྟའི་དོན་ཕྱིར་དང་པོ་ལྔ། །མིག་ལ་སོགས་པ་ལྔའི་ཡུལ་ནི་ད་ལྟར་བ་ཡིན་པའི་ཕྱིར་སྔར་སྨོས་སོ། །

[Block 247 [VERSE]]
འབྱུང་བ་ལས་གྱུར་དོན་ཕྱིར་བཞི། །
དང་པོར་ཞེས་བྱ་བར་སྙེགས་སོ། །

[Block 248]
ལྔ་པོ་རྣམས་ལས་ཀྱང་བཞི་སྔར་སྨོས་པ་ནི་ཡུལ་འབྱུང་བ་ལས་གྱུར་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 249]
ལུས་ཀྱི་ཡུལ་ནི་མ་ངེས་ཏེ། རེས་འགའ་ནི་འབྱུང་བ་དག་ཡིན་ལ། རེས་འགའ་ནི་འབྱུང་བ་ལས་གྱུར་པ༌[^92]དག་ཡིན་ནོ། །

[Block 250 [VERSE]]
རེས་འགའ་ནི་གཉིས་ཀ་ཡིན་ནོ། །
གཞན་ནི་ཆེས་རིང་མྱུར་འཇུག་ཕྱིར། །
--- END BLOCKS ---
