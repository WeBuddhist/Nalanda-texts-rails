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
[Block 2346]
དགེ་བ་དང་མི་དགེ་བའི་ལས་ཀྱི་ལམ་བཅུ་པོ་འདི་དག་ནི།

[Block 2347 [VERSE]]
ཐམས་ཅད་བདག་པོ་རྒྱུ་མཐུན་དང་། །
རྣམ་སྨིན་འབྲས་བུ་འབྱིན་པར་འདོད། །

[Block 2348]
རེ་ཞིག་མི་དགེ་བ་ཐམས་ཅད་ཀྱི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་ནི་དམྱལ་བར་སྐྱེ་བའོ། །

[Block 2349]
མི་རྣམས་སུ་སྲོག་གཅོད་པའི་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ནི་ཚེ་ཐུང་བའོ། །

[Block 2350]
མ་བྱིན་པར་ལེན་པ༌[^941]ནི་ལོངས་སྤྱོད་ཀྱིས་ཕོངས༌[^942]པའོ། །

[Block 2351]
འདོད་པས་ལོག་པར་གཡེམ་པས་ནི་དགྲ་དང་བཅས་པའི་ཆུང་མ་ཅན་དུའོ། །

[Block 2352]
བརྫུན་དུ་སྨྲ་བ༌[^943]ནི་སྐུར་པ་མང་བའོ། །

[Block 2353]
ཕྲ་མས་ནི་མཛའ་བོ་དབྱེའོ།[^944] །

[Block 2354]
ཚིག་རྩུབ་པོ༌[^945]ནི་ཡིད་དུ་མི་འོང་བའི་སྒྲ་ཐོས་སོ། །

[Block 2355]
ཚིག་ཀྱལ་པས་ནི་ཚིག་གཟུང་བར་མི་འོས་པའོ། །

[Block 2356]
བརྣབ་སེམས་ཀྱིས་ནི་འདོད་ཆགས་ཆེ་བར་རོ། །

[Block 2357]
གནོད་སེམས་ཀྱིས་ནི་ཞེ་སྡང་ཆེ་བར་རོ། །

[Block 2358]
ལོག་པར་ལྟ་བས་ནི་གཏི་མུག་ཆེ་བར་འགྱུར་རོ།[^946] །

[Block 2359]
སྲོག་གཅོད་པའི་བདག་པོའི་འབྲས་བུ་ནི་ཕྱིའི་དངོས་པོ་རྣམས་གཟི་མཐུ༌[^947]ཆུང་བར་འགྱུར་རོ། །

[Block 2360]
མ་བྱིན་པར་ལེན་པས་ནི་སེར་བ་དང་ཆར་པ་མང་བར་འགྱུར་རོ། །

[Block 2361]
འདོད་པས་ལོག་པར་གཡེམ་པས་ནི་རྡུལ༌[^948]གྱིས་འཁྲིགས་པའོ། །

[Block 2362]
བརྫུན་དུ་སྨྲ་བས་ནི་དྲི་ང་བར་རོ།[^949] །

[Block 2363]
ཕྲ་མས་ནི་མཐོ་དམན་ཅན་དུའོ། །

[Block 2364]
ཚིག་རྩུབ་པོས་ནི་ཚ་སྒོ་ཅན་དང་། དགོན་དུང་ཅན་དུའོ། །

[Block 2365]
ཚིག་ཀྱལ་པས་ནི་དུས་ལོག་པ་ཅན་དུའོ། །

[Block 2366]
བརྣབ་སེམས་ཀྱིས་ནི་འབྲས་བུ་ཕྲ་མོར་རོ། །

[Block 2367]
གནོད་སེམས་ཀྱིས་ནི་འབྲས་བུ་ཁ་བར་རོ། །

[Block 2368]
ལོག་པར་ལྟ་བས་ནི་འབྲས་བུ་ཆུང་ངུའམ་མེད་པར་འགྱུར༌[^950]རོ། །

[Block 2369]
འདི་ཡང་།

[Block 2370 [VERSE]]
སྡུག་བསྔལ་ཕྱིར་དང་བསང་ཕྱིར་དང་། །
གཟི་བྱིན་མེད་ཕྱིར་འབྲས་རྣམ༌[^951]གསུམ། །

[Block 2371]
སྲོག་གཅོད་པར་བྱེད་པས་ནི་གསད་པར༌[^952]བྱ་བ་སྡུག་བསྔལ་བསྐྱེད་པ་དང་། སྲོག་དང་བྲལ་བས་བསད་པ་དང་། གཟི་བྱིན་མེད་པར་བྱས་པ་ཡིན་ཏེ། དེའི་དེ་ལ་དམྱལ་བར་སྐྱེ་བ་ལ་སོགས་པའི་འབྲས་བུ་རྣམ་པ་གསུམ་གསུངས་སོ། །

[Block 2372]
མ་བྱིན་པར་ལེན་པ་ལ་སོགས་པ་དང་། དགེ་བ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 2373 [HEADING]]
##### ལོག་པར་འཚོ་བ། ^4-3-9-6-0

[Block 2374]
ལོག་པའི་ལུས་ངག་གི་ལས་ཀྱི་མཐའ་དག་གིས་ལོག་པར་འཚོ་བ་གང་གསུངས་པ་དེ་ནི་གཞན་མེད་ཀྱི་དེ་ཉིད་ཡིན་ཏེ། ལུས༌[^953]དང་ངག་ལ་ཆགས་ལས་སྐྱེས། །ལོག་འཚོ། ལུས་ངག་གི་ལས་ཀྱི་མཐའ་ནི་ཞེ་སྡང་དང་གཏི་མུག་ལས་སྐྱེས་པ་ཡིན་ཏེ།

[Block 2375]
དེ་ནི་དེ་དག༌[^954]ལས།

[Block 2376]
སྦྱང་དཀའི་ཕྱིར་ལོགས་ཤིག་བསྟན་ཏོ། །

[Block 2377]
ཆགས་པའི་ཆོས་ནི་འཕྲོག་པར་བྱེད་པ་ཡིན་པས་དེས་ཀུན་ནས་བསླང་བའི་ལས་སེམས་བསྲུང་བར་སླ་བ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་འཚོ་བ་སྦྱང་དཀའ་བས་བསྒྲིབ་པར༌[^955]བྱ་བའི་ཕྱིར་ལོགས་ཤིག་ཏུ་བསྟན་ཏོ། །

[Block 2378]
གལ་ཏེ། ཡོ་བྱད་ལ། ཆགས་བསླང་གང་ཞིག་འཚོ་བས་ཡོ་བྱད་ལ་ཆགས་པས་བསླང་བའི་ལུས་དང་ངག་གི་ལས་ཁོ་ན་ལོག་པའི་འཚོ་བ་ཡིན་ལ། གཞན་ནི་མ་ཡིན་ཏེ་ཞེས་འདོད་པ་དེ་ནི། མདོ་དང་འགལ་ཕྱིར་མིན།

[Block 2379]
ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོའི་མདོ་ལས།

[Block 2380]
གླང་པོ་ཆེ་འཐབ་པ་ལ་ལྟ་བ་ལ་སོགས་པ་ཡང་ལོག་པའི་འཚོ་བར་གཞག་སྟེ། ལོག་པའི་ཡུལ་ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་ཕྱིར་རོ། །

[Block 2381]
འདི་ནི་རྫོགས་སོ། །

[Block 2382 [HEADING]]
#### འབྲས་བུ་ལྔ། ^4-3-10-0

[Block 2383]
གོང་དུ་འབྲས་བུ་ལྔ་བཤད་པ་གང་དག་ཡིན་པ་དེ་དག་ལས་ལས་གང་ཞིག་འབྲས་བུ་དུ་ཞིག་གི་འབྲས་བུ་དང་བཅས་པ་ཡིན་ཞེ་ན། དྲིར་བཅས་སྤོང་བའི་ལམ་དག་གི །ལས་ནི་ལྔ་ཡིས་འབྲས་བུར་བཅས། །ལས་དེ་ནི་འབྲས་བུ་ལྔས་འབྲས་བུ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 2384]
དྲི་མེད་བཞི་ཡིས། བར་ཆད་མེད་པའི་ལམ་ཟག་པ་མེད་པའི་ལས་ནི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་མ་གཏོགས་པ་འབྲས་བུ་བཞིས་འབྲས་བུ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 2385]
ཟག་བཅས་གཞན། དགེ་དང་མི་དགེ་གང༌[^956]ཡིན་པའང་། །སྤོང་བའི་ལམ་ལས་གཞན་པའི་ལས་དགེ་བ་ཟག་པ་དང་བཅས་པ་གང་ཡིན་པ་དང་། མི་དགེ་བ་གང་ཡིན་པ་དེ་ཡང་འབྲས་བུ་བཞིས་འབྲས་བུ༌[^957]དང་བཅས་པ་ཡིན་ཏེ།
--- END BLOCKS ---
