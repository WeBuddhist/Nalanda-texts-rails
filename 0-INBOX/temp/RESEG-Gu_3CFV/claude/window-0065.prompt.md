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
[Block 2276]
བཤགས་པར་བྱ་བ་གཉིས་པ་ལ་བྱེད་པ་པོ༌[^1435]གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེའམ་དགེ་སློང་གཞན་དག་ལ་བཟའ་བའམ་བཏུང་བ་འམ་སྲན་ཚོད་དམ། བཅའ་བའམ་ཡང་བྱིན་ཅིག་ཅེས་བྱ་བ་ལ་སོགས་པས་བསྐོ་ཤམ་བྱེད་པ་ལ་ཞུགས་པའི་དགེ་སློང་མ་འདུག་པ་ནི་བྱེད་པ་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སོགས་པ་ཞེས་བྱ་བའི་སྒྲས་ནི་ཟས་ལྷག་མ་དག་སྟོབས་པ་ཡང་བསྡུས༌[^1436]པའི་ཕྱིར་རོ། །

[Block 2277]
བསྐོ་ཤམ་བྱེད་པ་ཞེས་བྱ་བ་འདིས་འདི་ལ་འབྲེལ་པ་ཡིན་ཏེ། དེའི་འདི་ངོ་བོ་ཉིད་བརྗོད་པ་ཡིན་ནོ། །

[Block 2278]
བསྐོ་ཤམ་བྱེད་པ་ལ་ཞུགས་པའི་དགེ་སློང་མ་འདུག་པ་ལ་ནི་དེ་བས་ན་ཚིག་འདིའོ། །

[Block 2279]
དེའམ༌[^1437]དགེ་སློང་གཞན་ལ་ཞེས་བྱ་བ་ལ། དེའམ༌[^1438]ཞེས་བྱ་བ་ལྟུང་བ་འབྱིན་པ་པོ་ཉིད་ལ་མངོན་པར་བརྟེན་པའི་དགེ་སློང་གཟུང་བའོ། །

[Block 2280]
ཅི་དགེ་སློང་མ་དེ་ལྟ་བུར་གྱུར་པ་ཐམས་ཅད་ཀྱི་འདུག་པ་དེ་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་དེའི་ཚིག་གིས་སམ། དེའི་ཉེ་དུས་མགྲོན་དུ་བོས་པ་མ་ཡིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་བསྐོ་ཤམ་བྱེད་པ་ལ་ཞུགས་པའི་དགེ་སློང་མ་དེ་ལ་ཉེ་དུས་མགྲོན་དུ་བོས་པ་མ་ཡིན་ནའོ། །

[Block 2281]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས།

[Block 2282]
དེའི་ཚིག་གིས་ཉེ་དུའི་གནས་ནས་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2283]
བསྐོ་ཤམ་བྱེད་པ་ལ༌[^1439]སྤྱིར་གཏང་བ༌[^1440]བསྟན་ནས་དམིགས་ཀྱིས་བསལ་བ་བསྟན་པའི་ཕྱིར་བྱུག་རིས་སྟོན་པ་དང་། མ་བྱིན་པ་ལ་བྱིན་དུ་འཇུག་པ་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རེ་ཞིག་འདིར་བྲིམས་ཤིག་ཅེས་བྱ་བ་ལ་སོགས་པས་གྲལ་རིམས་བཞིན་དུ་མདུན་དུ་བྱུག་རིས་སྟོན་པར་བྱེད་པའོ། །

[Block 2284]
མ་བྱིན་པ་ལ་སྦྱིན་དུ་འཇུག་པ་ནི། མ་བྱིན་པ་ལ་སྦྱིན་དུ་འཇུག་པའོ། །ཅི་ཞིག་བྱས་ན་དེ་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེ་ལ་དགེ་སློང་གང་ཡང་རུང་བས་ལྷན་ཅིག་མི་ཟ་བས་ཀྱང་རུང་བས་སྲིང་མོ་ཁྱོད་དགེ་སློང་རྣམས་ཟན་ཟོས་ཀྱི་བར་དུ་རེ་ཞིག་སྡོད་ཅིག་ཅེས་མ་བསྒོ་བར་དགེ་སློང་གསུམ་ལ་སོགས་པ་མགྲོན་དུ་བོས་པས་ཟོས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྡོད་ཅིག་ཅེས་བྱ་བ་ནི་འདི་ནི་བཟློག་པའི་དོན་ལ་མཚོན་པ་ཡིན་ཏེ། སུས་མ་བསྒོ་བར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་གིས་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་ལྟུང་བ་འབྱིན་པར་བྱེད་པ་ཁོ་ནས་སམ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་ཕྱིར་གང་ཡང་རུང་བས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2285]
སྔར་ལངས་པ་དེས་བསྒོ་བ་བྱས་ན་ཡང་དེ་ལ་བསྒོ་བ་ཉིད་ཡིན་པས་དེའི་ཕྱིར་ལྷན་ཅིག་མི་ཟ་བས་ཀྱང་རུང་བས་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་དགེ་སློང་གཞན་དག་ཟོས་ཏེ་འབྱུང་ཞིང་གཞན་དག་འཇུག་པས་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2286]
ཐམས་ཅད་ལངས་པར་གྱུར་ཟིན་ཅིང་གཞན་དག་འཁོད་པར་གྱུར་ན་འདུག་པའི་མདུན་རོལ་དུ་ཞུགས་པ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་འདིར་ཟན་གཅིག་པ༌[^1441]ཉིད་མི་འཐད་པའོ། །

[Block 2287]
དེ་བས་ན་ཟ་བ་པོ་ཐམས་ཅད་མ་ལངས་པ་ཉིད་ལ་སུ་ཞིག་གིས་ལངས་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2288]
འདིར་ཟན་གཅིག་པའི་དབང་དུ་བྱས་ཏེ་འདི་བརྗོད་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2289]
དགེ་སློང་གསུམ་ལ་སོགས་པ་མགྲོན་དུ་བོས་ནའོ་ཞེས་བྱ་བ་ནི། དེ་ཟོས་པ་ལའོ། །

[Block 2290]
ཅི་མགྲོན་དུ་བོས་པ་གང་ཡང་རུང་བ༌[^1442]ཟོས་པ་ལའམ༌[^1443]ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་བྲམ་ཟེ་དང་ཁྱིམ་བདག་གི་ཁྱིམ་དུ་མགྲོན་དུ་བོས་པ་དེས་སོ། །

[Block 2291]
ཁྱིམ་ཉིད་དུ་ཟོས་ན་སྟེ་གཞན་དུ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2292]
གང་ཞིག་དགོན་པ་དང་གཙུག་ལག་ཁང་ལ་སོགས་པ་སྦྱིན་བདག་ཁྱིམ་གྱི་མི་ཐམས་ཅད་འདུས་པའམ་དེས་བསྐོས་པ་ལ་སོགས་པ་ཉེ་བར་གནས་པས་ཟ་བས་ཏེ། དེའི་ཁྱིམ་དུ་ནི་མ་ཡིན་ཞེས་ཤེས༌[^1444]པར་བྱའོ། །

[Block 2293]
ཁྱིམ་ཞེས་སྨོས་པས་ནི་དེས་ཁོངས་སུ་བསྡུ་བ་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 2294]
འདིར་རང་གི་ཚོགས་རྣམས་ལས་དམན་པ་བདག༌[^1445]ཉིད་གནས་པས་མ་མོའི་ཚོགས་ཀྱི་ཆོས་སོ། །

[Block 2295]
རིགས་འདི་གང་གིས་འདི་ཉེས་པར་སྤྱོད་པ་དེ་བས་ན་ཤིན་ཏུ་དམན་པར་ཁས་ལེན་པར་གྱུར་པ་འདིའི་ཟང་ཟིང་འཕྲོག་པ་ཉིད་རྟེན་དུ་གྱུར་པ་ཟང་ཟིང་གི་གཙོ་བོ་ཉིད་དུ་རྗེས་སུ་འགྲོ་བར་གྱུར་པ༌[^1446]གང་ཞིག་བདག་པོར་མ་གྱུར་ཀྱང་བདག་པོ་བཞིན་དུ༌[^1447]རང་གི་ཚོགས་ཀྱི་ཁོངས་སུ་བསྡུས་པ་མ་མོའི་ཚོགས་ཟང་ཟིང་ལ་འཇུག་པར་གྱུར་པ་ལྷག་པར་གནས་ཏེ་ཟང་ཟིང་དེ་ལ་ཉེ་བར་ལོངས་སྤྱོད་པ་དེ་བས་ན་འདི་ནི་ཁ་ན་མ་ཐོ་བའོ། །

[Block 2296]
མང་པོར་གྱུར་པ་རྣམས་ལ་དེ་ལྟར་མི་བརྟེན་པ་འདིར་ཡོངས་སུ་གྱུར་པ་ཁྱིམ་གྱི་ཟས་ལས་གཞན་པས༌[^1448]འདིར་ཤིན་ཏུ་དཀའ་བ་ཉིད་ཀྱི་ཕྱིར་ཉེ་བར་གནས་པ་ལ་ཡང་ཁྱིམ་གྱི་སྐྱེ་བོ་ལ་འདིར་ཤིན་ཏུ་རྫོགས་པར་གྱུར་པ་ཉིད་ཀྱིས་གསོལ་བ་ཉམས་པའོ། །

[Block 2297]
དེ་བས་ན་འདི་རྣམས་ལ་འདིར་ཁྱད་པར་རྣམས་བརྟེན་པའོ། །

[Block 2298]
ཁྱིམ་གྱི་ཟན་ལས་གཞན་པ་གཙུག་ལག་ཁང་ལ་སོགས་པའི་ཟན་ལ་གཅིག་གམ་གཉིས་ཟ་བར་བྱེད་ན་རྗེས་སུ་འབྲངས་པས་རྟོགས་པར་བྱའོ། །

[Block 2299]
འདིར་དགེ་སློང་མ་ཐག་ཇི་སྲིད་ན་འདུག་པར་གྱུར་པ་ན་ཁ་ན་མ་ཐོ་བ་ཇི་ལྟ་བུའི་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་ཚིག་དེ་ཉེ་བར་གདགས་སུ་རུང་བ་ན་དངོས་གཞིའོ། །

[Block 2300]
གལ་ཏེ་མི་རུང་ན་ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་སྲིང་མོ་ཁྱོད་སྡོད་ཅིག་ཅེས་བྱ་བ་སྨོས་ན་གལ་ཏེ་དགེ་སློང་མ་འདི་ཉེ་བར་སྤྱོད་པ་ཐོབ་པར་འགྱུར་ཏེ། གང་དུ་སྨྲ་བར་ནུས་ན་ལྟུང་བ་དངོས་གཞིའི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 2301]
གལ་ཏེ་ཉེ་བར་མ་གདམས་ཤིང་མ་བསྒོ་ན་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2302]
སྔ་མ་དག་གི་སོ་སོར་བཤགས་པར་བྱ་བ་ལ་འདིར་ཉེས་བྱས་ཀྱི་གཞུང་ནི་གང་དག་བར་མའི་ས་ལ་ཟ་བར་བྱེད་པ་དེ་རྣམས་ཀྱིས་དྲི་བར༌[^1449]བྱའོ། །

[Block 2303]
དགེ་སློང་མ་དེ་ལ་བསྒོའམ་ཞེས་དྲི༌[^1450]བར་བྱ་སྟེ། མ་དྲིས་པར་ཟ་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 2304]
གང་དག་སྒོ་ཁང་ན་ཟ་བ་དེ་དག་གིས་དགེ་སློང་མ་དེ་ལ་བསྒོའམ་ཞེས་དྲི་བར༌[^1451]བྱ་སྟེ། མ་དྲིས་པར་ཟ་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2305]
འདིར་དངོས་གཞིའི༌[^1452]གཞུང་ནི་དགེ་སློང་དག་ཁ་ཅིག་ནི་ཁང་ཐོག་ན་ཟ་བར་བྱེད་ལ། ཁ་ཅིག་ནི་བར་ཁང་ན་ཟ་བར་བྱེད་ལ། དེ་ལ་གལ་ཏེ་དགེ་སློང་མ་བསྐོ་ཤམ་བྱེད་ཅིང་འདུག་པར་གྱུར་ན་དགེ་སློང་དེ་རྣམས་ཀྱིས་དགེ་སློང་མ་དེ་ལ་བསྒོ་བར་བྱའོ། །

[Block 2306]
མ་བསྒོ་བར་ཟན་ཟ་ན་སོ་སོར་བཤགས་པར་འགྱུར་རོ།[^1453] །འདིར་གཞུང་དགགས། [^1454]དགེ་སློང་དག་ཁ་ཅིག་ནི་འོག་ཁང་ན༌[^1455]ཟ་བར་བྱེད་ལ། ཁ་ཅིག་ནི་སྒོ་ཁང་ན་ཟ་བར་བྱེད་ལ། དེ་ན་གལ་ཏེ་དགེ་སློང་མ་བསྐོ་ཤམ་བྱེད་ཅིང་འདུག་པར་གྱུར་ན་དགེ་སློང་དེ་དག་གིས་དགེ་སློང་མ་དེ་ལ་བསྒོ་བར་བྱའོ། །

[Block 2307]
མ་བསྒོ་བར་ཟ་ན་སོ་སོར་བཤགས་པར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2308]
གང་ཞིག་འདིར་དྲི་བར༌[^1456]བྱ་བ་ཉིད་ཀྱི་ཚིག་འདུ་ཤེས་པས་བསྒོ་བར་བྱེད་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་དེ་བས་ན་འདི་འདྲི་བར་བྱ་བ་ཉིད་ཅེས་བྱ་བ་དེ་ལ་འདི་སྟོན་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 2309]
དེ་ཉིད་བརྗོད་པར་བྱ་སྟེ་འདི་ལ་བསྒོ་བ་ཉིད་དུ་རྣམ་པར་གནས་པ་ནི་ཤེས་གཙོའོ། །

[Block 2310]
དེའི་ཕྱིར་དྲི་བ་ལ་བརྩོན་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཤེས་གཙོའོ༌[^1457]ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་པའི་ཕྱིར་བསླབ་པའི་གཞི་ལ་བསྒོ་བ་རྣམ་པར་གཞག་པ་ལའོ། །

[Block 2311]
འདི་ལ་རྒན་པ་མི་འཇུག་ན་གསར་བུས་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དྲི་བ་འདི་ལ་རྒན་པས་འཇུག་པར་བྱའོ། །

[Block 2312]
དེ་མི་འཇུག་ན་གསར་བུས་འཇུག་པར་བྱའོ། །

[Block 2313]
གྲལ་རིམས་སུ་མ་ཕེབས་པར་འདྲིམ་དུ་འཇུག་པ་མ་བཟློག་པར༌[^1458]ཟ་བའི་སོ་སོར་བཤགས་པར་བྱ་བ་སྟེ་གཉིས་པའོ།། །།

[Block 2314]
དད་པ་ཅན་གལ་ཏེ་བྱིན་ན་དེ་ཕོངས་པར༌[^1459]འགྱུར་བ་ལྟ་ན་ཁྱིམ་གྱི་བསླབ་པའི་སྡོམ་པ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དད་པ་ཅན་ཞེས་བྱ་བ་ནི་ཁྱིམ་བདག་སྟེ། དེ་ལ་ཁྱིམ་གྱི་བསླབ་པའི་སྡོམ་པ་སྦྱིན་པར༌[^1460]བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2315]
གལ་ཏེ་སྦྱིན་ན་ཕོངས༌[^1461]པར་གྱུར་པ་ལྟ་ན་ཞེས་བྱ་བ་ནི་གལ་ཏེ་སྦྱིན་པ་བྱིན་ན་དད་པ་ཅན་དེ་ཡོ་བྱད་རྣམས་ཀྱིས་ཕོངས་པར་འགྱུར་བ་ལྟ་ན་དེ་ནས་སྡོམ་པ་སྦྱིན་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
