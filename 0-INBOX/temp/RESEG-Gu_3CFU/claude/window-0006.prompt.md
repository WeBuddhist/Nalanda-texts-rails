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
དེ་ཡང་འདི་ལ་དེ་མ་ཐག་པ་དང་བཅས་པར་བྱེད་པ་ཚིག་གང་ལ་འདི་ནི་འཇུག་པ་ལོག་པ་ཞེས་བྱ་བའི་བློའོ། །

[Block 212]
དགེ་ཚུལ་ཉིད་དུ་ཉེ་བར་སྒྲུབ་པའི་ཆོ་གའོ།། །།

[Block 213]
དགེ་འདུན་ལས་བསྙེན་པར་རྫོགས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རབ་ཏུ་འབྱུང་བ་དང་དགེ་ཚུལ་ཉིད་དུ་ཁས་ལེན་པ་ལྟར་གང་ཟག་ལས་ནི་མ་ཡིན་ཏེ། [^160]འོན་ཀྱང་དགེ་འདུན་ལས་བསྙེན་པར་རྫོགས་པར་བྱའོ། །

[Block 214]
མཁན་པོ་ཉིད་དུ་ཕྱོགས་པར་གྱུར་པས་ལས་བྱེད་པ་དང་གསང་སྟེ་སྟོན་པའི་དགེ་སློང་ལ་གསོལ་བ་གདབ་པར་བྱའོ་ཞེས་བྱ་བ་སྟེ། མཁན་པོ་ཉིད་དུ་ཕྱོགས་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པ་ལ་མཁན་པོ་ཉིད་ཀྱིས་སོ་སོར་ཉེ་བར་གནས་པའོ། །

[Block 215]
གསོལ་བ་གདབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གསོལ་བ་གདབ་པའོ། །

[Block 216]
གསང་སྟེ་སྟོན་པ་ལ་ཡང་གསོལ་བ་གདབ་པར་བྱའོ། །

[Block 217]
དགེ་སློང་ལ་ཞེས་བྱ་བ་ནི་གསང་སྟེ་སྟོན་པའི་དོན་དུ་དགེ་སློང་གི་ཚིག་སྟེ། ལས་བྱེད་པའི་དོན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 218]
ལས་བྱེད་པ་ལ་ནི་གང་ཞིག་ལས་ཀྱི་ཆོ་ག་གསུངས་པ་དེ་ཉིད་ལས་དེ་ལ་དགེ་སློང་ཉིད་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 219]
མཁན་པོར་གསོལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་དབུས་སུ་བསྙེན་པར་རྫོགས་པར་བྱ་བས༌[^161]སོ། །

[Block 220]
དེ་རང་གིས་དེ་ལ་ཆོས་གོས་གསུམ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་སྟེ། དེ་ཞེས་བྱ་བ་ནི་མཁན་པོའོ། །

[Block 221]
རང་གིས་ཞེས་བྱ་བ་ནི་འདིར་དབུགས་དབྱུང་བའི་ཆོ་ག་བྲེགས་པ༌[^162]ལ་སོགས་པ་བཞིན་དུ་ཅི་ནས་ཀྱང་མ་ཡིན་ཏེ། རང་གིས་འདི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 222]
དེ་ལ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པར་བྱ་བ་ལའོ། །

[Block 223]
ཚོགས་པ་ཡོད་པ་ལ་དྲས་ཤིང་དྲུབ་པས༌[^163]བྱིན་གྱིས་བརླབས་པས་ཀྱང་ངོ་། །མེད་པ་ལ་གཞན་ཞེས་བྱ་བ་གོས་ཀྱི༌[^164]གཞི་ལས་རྟོགས་པར་བྱའོ། །

[Block 224]
བྱིན་གྱིས་བརླབ་པ་ནི་ཆ་ལུགས་ཀྱི་དོན་ཉིད་ཀྱི་ཕྱིར་བྱིན་གྱིས་བརླབས་པའི་དོན༌[^165]དེ་མ་ཐག་ཏུ་འདི་རྣམས་བགོ་བར་བྱ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 225]
ལྷུང་བཟེད་ཀྱང་མི་ཆུང་ངམ་མི་ཆེ་འམ་མི་སྐྱ་འམ་ཞེས་དགེ་འདུན་ལ་བསྟན་ནས་སོ་ཞེས་བྱ་བ་སྟེ། བསྟན་ནས་ཞེས་བྱ་བ་དགེ་འདུན་ལ་ཞེས་བྱ་བ་འདི་དང་འདི་ལ་འབྲེལ་ཏོ། །ཅིའི་ཕྱིར་བསྟན་ཞེ་ན། མི་ཆུང་ངམ་མི་ཆེ་འམ་མི་སྐྱ་འམ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྐྱོན་འདི་ཡོངས་སུ་སྤང་བའི་དོན་དུ་རྣམ་པ་འདི་ལྟ་བུ་ལ་བྱིན་གྱིས་བརླབས་པ༌[^166]རིགས་པ་མ་ཡིན་ནོ། །

[Block 226]
དགེ་འདུན་ལ་བསྟན་ནས་སོ་ཞེས་བྱ་བ་ནི་ལྷག་པར་གནས་པར་བྱའོ་ཞེས་བྱ་བའི་རྗེས་སུ་འཇུག་གོ། །

[Block 227]
ཐམས་ཅད་ཀྱིས་དེ་ལྟ་བུ་ཉིད་མ་ཡིན་ཏེ་ལྷུང་བཟེད་བཟང་ངོ་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་དགེ་སློང་རྣམས་འདུས་པས་སོ། །

[Block 228]
དེ་ལྟ་བུའི་དངོས་པོ་ནི་དེ་ལྟ་བུ་ཉིད་དེ་ཆུང་བ་ལ་སོགས་པའི་སྐྱོན་དང་ལྡན་པ་ཉིད་དོ། །

[Block 229]
དེ་ལྟ་བུ་ཉིད་མ་ཡིན་པ༌[^167]ནི་དེ་ལྟ་བུ་ཉིད་མ་ཡིན་པ་སྟེ། སྐྱོན་འདི་རྣམས་དང་བྲལ་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 230]
བཀར་ནས་ལས་བྱེད་པས་གསང་སྟེ་སྟོན་པ་ལ་གང་ཡིན་ཞེས་བྱ་བས་སྨྲར་བཅུག་སྟེ་སྤྲོ་བར་བྱས་ནས་དེ་དགེ་འདུན་ལ་གསོལ་བའོ་ཞེས་བྱ་བ་སྟེ། བཀར་ནས་ཞེས་བྱ་བ་ནི་དཀྱིལ་འཁོར་གྱི་གནས་ནས་གཞན་དུ་སྟོན་པའི་ཉེ་བར་གནས་པར་བྱ་བ་ལ༌[^168]གསང་སྟེ་སྟོན་པ་ལ༌[^169]གནས་པའི་ལས་ཐོས་པའི་ཉེ༌[^170]འཁོར་མ་ཡིན་པ་ནི་འདིར་བཀར་བའི་དོན་ཏེ་གཞན་མཐོང་བ་མ་ཡིན་ནོ། །

[Block 231]
དེ་བས་ན་གང་དུ་གནས་པ་འདི་ལ་ཐོས་པའི་ཉེ་འཁོར་མ་ཡིན་པར་འགྲོ་བ་དེར་ཞེས་བྱ་བ་ལས་ཀྱི་ཆོ་ག་རྟོགས་པར་བྱའོ། །

[Block 232]
མཐོང་བ་ཉེ་བར་སྤྱད་པ་ལ་འདི་འཆད་པར་འགྱུར་ཏེ། ཚོགས་པ་ལ་མངོན་པར་ཕྱོགས་ཤིང་ཐལ་མོ༌[^171]སྦྱར་བ་འདི་བཀར་ནས་གཞག་པར་བྱ་ཞེས་བྱའོ།[^172] །སུ་ཞིག་ཅེ་ན། བཀར་ནས་ཞེས་བྱ་བ་སྟེ། མིང་འདི་ཞེས་བྱ་བ་སུ་ཞིག༌[^173]གསོལ་བ་བཏབ་པར་གྱུར་པ་གསང་སྟེ་སྟོན་པ་ཞེས་བྱ་བའི་སྔགས་འདིས་བདག་མིང་འདི་ཞེས་བགྱི་བ་གསང་སྟེ་སྟོན་པ་བཙལ་ནས་ཞེས་བྱའོ།[^174] །སྤྲོ་བར་བྱས་ནས་ཞེས་བྱ་བ་ནི་ཁྱོད་སྤྲོའམ་ཞེས་བྱ་བ་ལ་སོགས་པས་གསང་སྟེ་སྟོན་པ་དེ་ཉིད་ལའོ། །

[Block 233]
དེ་ཞེས་བྱ་བ་ནི་གསང་སྟེ་སྟོན་པའོ། །

[Block 234]
གསོལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིའི་དོན་དུ་ལས་བྱེད་པ་པོས་གསོལ་བར་བྱའོ། །

[Block 235]
ཁ་ཅིག་ནི་འདིར་སོན་པའི་སྔགས་ལ་དགེ་འདུན་གྱིས་མིང་འདི་ཞེས་བགྱི་བའི་གསང་སྟེ་སྟོན་པ་ལ་ཡང་དག་པར་བསམས་པ་ཞེས་བྱ་བ་གང་ཞིག་འདོན་པར་བྱེད་པ་དེ་ནི་རིགས་པ་མ་ཡིན་ཏེ། ལས་བརྗོད་པ་ལ་ཡང་བྱ་བ་ཉིད་དུ་ཐལ་བའི་ཕྱིར་དང་། འདི་རྣམས་ལ་བློ་མཐུན་པར་གསོལ་བར་བྱ་བ་འདི་ཞེས་བྱ་བ་རྣམ་པར་གཞག་པའོ། །

[Block 236]
དེ་བས་ན་མིང་འདི་ཞེས་བགྱི་བའི་གསང་སྟེ་སྟོན་པ་མིང་འདི་ཞེས་བགྱི་བའི༌[^175]ལྐོག་ཏུ་སྟོན་པར་བྱེད་པ་ཞེས་བྱ་བ་འདི་ལ་གདོན་པར་རིགས་པ་ཡིན་ཏེ། དེ་བས་ན་གསོལ་བར་བྱ་བ་ནི་འདི་ལྟར་མདོར་བྱས་པ་ཡིན་ཏེ་བློ་མཐུན་པ་ནི་མ་ཡིན་ནོ། །

[Block 237]
ཁྱོད་ཉོན་ཅིག་ཅེས་བྱ་བས་ལྐོག་ཏུ་རྗེས་སུ་བསྟན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གསང་སྟེ་སྟོན་པ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རིག་པར་བྱའོ། །

[Block 238]
ཚེ་དང་ལྡན་པ་ཁྱོད་ཉོན་ཅིག །ཁྱོད་ཀྱིས༌[^176]འདི་ནི་བདེན་པའི་དུས་ཡིན་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྔགས་ལ་ཁྱོད་ཉོན་ཅིག་ཅེས་བྱ་བའི་ཚིག་འདི་དང་འབྲེལ་པའོ། །

[Block 239]
མ་བོས་ཀྱི་བར་དུ་མ་འོང་བར་སྡོད་ཅིག་ཅེས་སྨྲས་ནས་རྗེས་སུ་བསྟན་ན་ཞེས་བྱ་བས་དགེ་འདུན་ལ་ཡོངས་སུ་དག་པ་གོ་བར་བྱ་སྟེ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་བཙུན་པ་རྣམས་གསན་དུ་གསོལ། ། མིང་འདི་ཞེས་བྱ་བས་བདག་གི་དགེ་འདུན་ལ་རྗེས་སུ་བསྟན་པས་ཞེས་བྱ་བའི་སྔགས་ཀྱིས་སོ། །

[Block 240]
ཅི་མཆི་ཞིག་གམ་ཞེས་བྱ་བས་དགེ་འདུན་ལ་འོང་བ༌[^177]ཞུ་བར་བྱའོ། །

[Block 241]
ཐམས་ཅད་ཀྱིས་གལ་ཏེ་ཡོངས་སུ་དག་ནའོ་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་རྣམས་ཀྱིས་བསྙེན་པར་རྫོགས་པ་ཅིག༌[^178]གོ། །

[Block 242]
ཁ་ཅིག་ནི་འདི་དང་སྔ་མ་ལ་རབ་ཏུ་བྱུང་བའི་དོན་དུ་ཞུ་བའི་ཚིག་ལ་ལེན་བརྗོད་པ་ཡིན་ཏེ། གལ་ཏེ་ཡོངས་སུ་དག་ནའོ་ཞེས་དགེ་འདུན་ཐམས་ཅད་ཀྱིས་བརྗོད་པར་བྱའོ། །

[Block 243]
དེས་ན་ཡོངས་སུ་དག་གོ་ཞེས་བྱ་བ་བརྗོད་པར་བྱ་བ་དེ་ནི་མི་འཐད་དེ། གང་གི་ཕྱིར་བརྗོད་པ་པོ་ལ་ཁུར་བཀལ་བ་འདི་མིན༌[^179]ཏེ། གསང་སྟེ་སྟོན་པས་དང་པོ་ཉིད་དུ་བརྗོད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 244]
ལས་བྱེད་པས་བསྙེན་པར་རྫོགས་པ་གསོལ་དུ་གཞུག་གོ་ཞེས་བྱ་བ་སྟེ། བསྙེན་པར་རྫོགས་པ་ལ་ལྟོས་པའོ། །

[Block 245]
དགེ་འདུན་ལ་གསོལ་ནས་བར་ཆད་དྲི་བར་བྱའོ་ཞེས་བྱ་བ་ནི། བར་ཆད་ཡོངས་སུ་དྲི་བའི་དོན་དུ་གསོལ་བ་བྱས་ནས་སོ། །

[Block 246 [VERSE]]
ཚེ་དང་ལྡན་པ་ཁྱོད་ཉོན་ཅིག །
འདི་ནི་ཁྱོད་ཀྱི་བདེན་པའི་དུས། །

[Block 247]
འདི་ནི་ཁྱོད་ཀྱི་འབྱུང་བའི་དུས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྔགས་ཀྱིས༌[^180]བར་ཆད་ཡོངས་སུ་དྲི་བའོ། །

[Block 248]
བསྙེན་པར་རྫོགས་པ་ཉེ་བར་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གསོལ་བ་དང་བཞིའི་ལས་ཀྱིས་ཏེ། ལས་བྱེད་པ་པོ་ལ་སྐབས་དོན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 249]
དེ་མ་ཐག་ཏུ་གྲིབ་ཚོད་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པ་ཉེ་བར་བསྒྲུབས་པའི་རྗེས་སུ་གྲིབ་ཚོད་བསྙེན་པར་རྫོགས་པ་ལ་རིག་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 250]
དེ་མ་ཐག་ཏུ་ནི་ཐོགས་པ་མེད་པའོ། །
--- END BLOCKS ---
