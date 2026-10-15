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
[Block 2661]
རྣམ་པ༌[^2482]གཞན་གྱིས་ཀྱང་འདི་ལྟ་སྟེ། སྤོ་བའམ་གཞི་ནས་སྤོ་བ་བྱེད་པས་ལྟུང་བ་རིགས་མཐུན་པ་བྱུང་ནས་འཐབ་ཀྲོལ་བྱེད་པ་འོང་བ་ཕྱིར་སྤོ་བའམ་གཞི་ནས་སྤོ་བ་ལ་སོགས་པ་བཏང་སྟེ་ཡང་ཕྱིར་ལེན་པ་དེས་བཏང་བའི་གནས་སྐབས་སུ་བཅབས་པའི༌[^2483]དུས་རིང་དུ་སྒྲུབ་པར་བྱེད་པའོ། །

[Block 2662]
མནོས་ཏེའོ་ཞེས་སྨོས་ཏེ་དགེ་འདུན་གྱི་སྤོ་བ་དང་མགུ་བར་བྱ་བ་དེ་གཉིས་ཇི་ལྟར་སྦྱིན་པར་བྱ་བ་ནི༌[^2484]བསྟན་པས༌[^2485]དེའི་ཕྱིར། དབྱུང་བ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་ལས་ཀྱིས་སྦྱིན་ནོ་ཞེས་བྱ་བའི་རྗེས་སུ་བསྙེག་པའི༌[^2486]ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 2663]
དེར་བསྡིགས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཁྱོད་ཀྱིས་ལེགས་པར་མ་བྱས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྔགས་ལས་ལྡང་བར་བྱེད་པའོ། །

[Block 2664]
དེར་ཞེས་བྱ་བ་ནི་དབྱུང་བ་དེར་རོ། །

[Block 2665]
བསྡིགས་པ་དེ་ནམ་གྱི་ཚེ་ན་བྱ་ཞེ་ན་དེའི་ཕྱིར་གསོལ་བ་དང་ལས་བརྗོད་པ་དང་པོའི་བར་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གསོལ་བ་བྱས་ནས་དེའི་རྗེས་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2666]
གནས་སྐབས་ཇི་ལྟར་འདུག་པ་ལ་བྱ་ཞེ་ན། དེའི་ཕྱིར་རྩྭ་བཀྲམ་པ་ལྟ་བུར་འགྱེལ་བ་ལའོ། །

[Block 2667]
གཟེངས་བསྟོད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ལ༌[^2487]སྨོས་ཏེ། འདི་ཡང་ཁྱོད་ཀྱིས་ལེགས་པར༌[^2488]བྱས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྔགས་ལས་ལྡང་བར་བྱེད་པ་ལའོ། །

[Block 2668]
འགྱེལ་བ་ལའོ་ཞེས་བྱ་བ་ནི་འདིར་སྦྱར་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2669]
ནམ་གྱི་ཚེ་ན་བྱ་ཞེ་ན། དེའི་ཕྱིར་བརྗོད་མ་ཐག་ཏུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་གྱིས་ཕྱུང་ལགས་ཏེ། འདིར་ཅང་མི་གསུང་བས་དེ་དེ་བཞིན་དུ་འཛིན་ཏོ་ཞེས་བྱ་བའི་ཚིག་བརྗོད་པ་བྱས་མ་ཐག་ཏུའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2670]
ཕྱིར་བཅོས་པའི་གཞིའོ།། །།

[Block 2671]
ཚུལ་ཁྲིམས་འཆལ་པ་བསྐྲད་པར་བྱའོ་ཞེས་བྱ༌[^2489]བ་ནི། འདིར་ཚུལ་ཁྲིམས་འཆལ་པ་ཞེས་བྱ་བ་ནི་ཕམ་པར་གྱུར་པར་ཤེས་པར་བྱའོ། །

[Block 2672]
འདི་ལ་དགེ་འདུན་དབང་བ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་འཆལ་པ་བསྐྲད་པ་ནི་དགེ་འདུན་ལ་རག་ལས་པ་ཡིན་པའི་ཕྱིར་གཙུག་ལག་ཁང་གི་བྱ་བ་ལ་དགེ་འདུན་དབང་བ་ཉིད་ཡིན་པས་གང་ཟག་ལ་ཡང་ནུས་པར༌[^2490]ཡོད་པར་གྱུར་ཀྱང་འདིར་བྱ་བ་ཉིད་དོ། །

[Block 2673]
དེ་ལྟར་ཡང་འཕགས་པ་མཽད་གལ་གྱི་བུ་གཅིག་པུས་གང་ཟག་ལ་སྡུག་བསྔལ་དེ་བྱས་པས་ན། འདིར་གང་ཟག་མི་དབང་བ་ཡིན་པས། དེ་བས་ན་དགེ་འདུན་ཉིད་ཀྱིས་བྱ་བར་གསུངས་སོ། །

[Block 2674]
འདིར་གཞུང་ནི། བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་ཚུལ་ཁྲིམས་འཆལ་པ་བསྐྲད་པར་བྱའོ་ཞེས་བཀའ་སྩལ་ན།[^2491] གང་གིས༌[^2492]བསྐྲད་པར་བགྱི། དགེ་འདུན་གྱིས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2675]
དེས་དེ་ཡལ་བར་མི་དོར་རོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱིས་སོ། །

[Block 2676]
དེ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་འཆལ་པ་བསྐྲད་པ་དེའོ། །

[Block 2677]
ཡལ་བར་མི་དོར༌[^2493]ཞེས་བྱ་བ་ནི་དེས་དེ་ལ་འབད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ནོ། །

[Block 2678]
བསྙིལ་བ་ལ་བཟོད་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དགེ་ཚུལ་བསྙིལ་བའི་ལས་བྱས་པ་ལ་ཇི་ལྟར་ནན་ཏུར་བྱས་པ་གཞན་དག་ལ་བཟོད་པར་བྱ་བ་དེ་བཞིན་དུ་དེ་ལ་ཡང་བཟོད་པར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 2679]
བསྙིལ་བ་ཉིད་ཀྱི་ཕྱིར་འདི་ལ་བཟོད་པར་མི་འོས་སོ་སྙམ་པའི་དོགས་པ་བཟློག་པའི་ཕྱིར་མདོ་འདི་ཡིན་ནོ། །

[Block 2680]
འདིར་གཞུང་ནི་དགེ་ཚུལ་བསྙིལ་བ་སྡུད་པའི་ལྟུང་བྱེད་ཀྱི་ཞུ་བ་ཁ་ཅིག་ལས།

[Block 2681]
དགེ་འདུན་གྱིས་དགེ་ཚུལ་བསྙིལ་བའི་ལས་ཀྱིས་བསྙིལ་བར་གྱུར་ཅིང་དེ་ཡང་འབྱུང་བ་སྐྱོད༌[^2494]ན་བཟོད་པར་བགྱིའམ་བཟོད་པར་མི་བགྱི། བཟོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2682]
ནན་ཏུར་བྱེད་པ་དག་གིས་མ་བསྐོས༌[^2495]ན་ནན་ཏུར་བྱས་པ་ལ་བཟོད་པ་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་མ་བསྐོས༌[^2496]པར་གྱུར་པ་ལ་ནན་ཏུར་བྱེད་པའི་དགེ་སློང་རྣམས་ཀྱིས་ནན་ཏུར་བྱས་ན་བཟོད་པ་མི་འཆགས་ཏེ། [^2497]གལ་ཏེ་དགེ་སློང་གཞན་དག་ནན་ཏུར་བྱས་པ་དེ་ལ་བཟོད་པར་བྱེད་འདོད་ན་ཅི་ནས་ཀྱང་ནན་ཏུར་བྱེད་པ་དེ་དག་གིས་དེར་བསྐོས་པ་ཉིད་དུ་འགྱུར་བ་དེ་ལྟར་བྱ་ཞིང་ཇི་ལྟར་ནན་ཏུར་བྱེད་པ་རྣམས་ལ་དེར་བསྐོས་པ་ཉིད་དུ་གྱུར་ཏེ། དེ་ལྟ་བས་ན་དེ་བསྟན་པའོ། །

[Block 2683]
བསྐྲད་པས༌[^2498]སུན་ཕྱུང་བའི་གནས་སུ་གནས་པར་མི་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་སུན་འབྱིན་པ་བསྐྲད་པ་ཉིད་ཀྱིས་གནས་ཁང༌[^2499]ཕྱུང་བར་གྱུར་པའི་སྤྱོད་ཡུལ་གྱི་གནས་དེར་གནས་པ་ཉིད་དོ། །

[Block 2684]
དེས་དེ་དག་གི་མ་དད་པ་ཡོངས་སུ་སྤང་བའི་ཕྱིར་གཞན་དུ་འགྲོ་བར་བྱའོ། །

[Block 2685]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་དག་ལས།

[Block 2686]
ཚེ་དང་ལྡན་པ་དག་ཁྱོད་གནས་འདི་ནས་སོང་ཤིག་དང་ཞེས༌[^2500]བྱ་བ་དང་། དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས་ཀྱང་བསྐྲད་པ་ཞེས་བྱ་བའི་དོན་ཅི་ལགས། ཉེ་བ༌[^2501]འཁོར་ལས་དེའི་མིང་ཡིན་ཏེ། འོན་ཀྱང་བསྐྲད་པར་བྱ་བ་ནི་དགེ་སློང་སུན་འབྱིན་པ་གང་ཡིན་པ་དེ་ལ་བྱ་སྟེ། དེ་འདིར་གནས་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2687]
གནས་ནས་ཕྱུང་བ་ཐམས་ཅད་ལ་གནས་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་དང་ལོངས་སྤྱད༌[^2502]པར་བྱ་བ་མ་ཡིན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ལྷན་ཅིག་གནས་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་དང་། ལྷན་ཅིག་ལོངས་སྤྱོད་པ་མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བ་དེ་གཉིས་ནི་གནས་ནས་ཕྱུང་བ་ཐམས་ཅད་ལ་རིག་པར་བྱ་བའི་ལྟ་བའི་རྣམ་པ་མི་གཏོང་བ་ཉིད་ཀྱིས་གནས་ནས་ཕྱུང་བ་འབའ་ཞིག་ལ་དེ་གཉིས་རིག་པར་བྱ་བར་མ་ཟད་དོ། །

[Block 2688]
དེ་ཡང་བསྐྲད་པར་བྱ་བ་ཉིད་ཅེས་བྱ་བ་ཉིད༌[^2503]དེ་འདིར་བརྗོད་པས་འདི་ལ་འདི་གནས་པར་རིག་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2689]
འདིར་གཞུང་ནི་དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས་གནས་ནས་ཕྱུང་བ་གྲོགས་དང་བཅས་པར་བརྗོད་པར་བགྱི་འམ། གྲོགས་མ་མཆིས་པར་བརྗོད་པར་བགྱི། གནས་ནས་ཕྱུང་བ་ཐམས་ཅད་གཅིག་པུ་གྲོགས་གཉིས༌[^2504]མེད་པར་བརྗོད་པར་བྱའོ། །

[Block 2690]
གནས་ནས་ཕྱུང་བ་ལ་ལོངས་སྤྱོད་དང་བཅས་པར་བརྗོད་པར་བགྱིའམ། ལོངས་སྤྱོད་མ་མཆིས་པར་བགྱི། གནས་ནས་ཕྱུང་བ་ཐམས་ཅད་ལ་ལོངས་སྤྱོད་མེད་པར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2691]
འདི་ལ་འདུ་ཤེས་ཀྱིས་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་ནི་གནས་ནས་ཕྱུང་བ་སྤང་བ་འདི་ལ་འདུ་ཤེས་ཀྱིས༌[^2505]རྣམ་པར་གཞག་པ་སྟེ། གང་གིས་འདི་གནས་ནས་བྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བར་ཤེས་ལ། དེ་མི་སྤོང་བ་དེ་ལ་ཉེས་པ་འདིར་འགྱུར་གྱི༌[^2506]མི་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2692]
འདིར་གཞུང་ནི་གང་གིས་གནས་ནས་ཕྱུང་བར་ཤེས་པ་དེས་ལྷན་ཅིག་གནས་པ་དང་། ལྷན་ཅིག་ལོངས་སྤྱད༌[^2507]པར་མི་བྱའི་གང་གིས་གནས་ནས་ཕྱུང་བར་མི་ཤེས་པ་དེས་ལྷན་ཅིག་གནས་པ་དང་། ལྷན་ཅིག་ལོང་སྤྱོད་པ༌[^2508]ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2693]
ཡོངས་སུ་སྤང་བར་བྱ་བ་ཐམས་ཅད་ཡོངས་སུ་སྤངས་པ་དག་ལ་ཡང་འདིའི་རྗེས་སུ་འབྲང་བའི་རྣམ་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2694]
བྱེ་བ་ཉིད་ནི༌[^2509]དེ་གཉིས་ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་། ཅིག་ཤོས་སུ་ཡིན་གྱི་ཅིག་ཤོས་དང་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། ལས་བྱེ་བ༌[^2510]དང་འཁོར་ལོ་བྱེ་བ་དག་ལས་གང་ཡང་རུང་བ་བྱེ་བ་དེ་ཉིད་ན་གནས་པ་བྱ་བ་མ་ཡིན་པ་ཉིད་དང་། ལོངས་སྤྱད༌[^2511]པར་བྱ་བ་མ་ཡིན་པ་ཉིད་དེ་དེ༌[^2512]གཉིས་ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་། ཅིག་ཤོས་ཀྱི་ཕྱོགས་སུ་ལྷན་ཅིག་མི་བྱ་བ་ཡིན་གྱི་ཆོས་ཀྱི་ཕྱོགས་ཅིག་ཤོས་དང་ཆོས་མ་ཡིན་པའི་ཕྱོགས་སུ་ལྷན་ཅིག་བྱར་མི་རུང་བ་ནི་མ་ཡིན་ཏེ། ཆོས་ཀྱི་ཕྱོགས་ལ་ནི་ཉེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2695]
འདིར་གཞུང་ནི་ཁས་བླངས་པ་དག་ནི་ཁས་མ་བླངས་པ་དག་དང་ལྷན་ཅིག་ལོང་སྤྱོད་པར་བྱེད་ན་ཉེས་བྱས་སོ། །

[Block 2696]
ཁས་མ་བླངས་པ་དག་ཁས་བླངས་པ་དག་དང་ལྷན་ཅིག་ལོངས་སྤྱོད་པར་བྱེད་པ་དག་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2697]
འཁོར་ལོ་བྱེ་བ་དག་ལས་ཐ་དད་པ་དག་ལ་ཡང་ཆོ་ག་འདི་རྣམ་པར་གཞག་པ་དེ་བས་ན་བྱེ་བྲག་མེད་པར་མདོར་བྱས་པ་སྟེ། ཐམས་ཅད་ཀྱི་དབང་དུ་བྱས་ནས་བསྟན་པའོ། །

[Block 2698]
ནན་ཏུར་བྱས་པ་གཞན་དག་ལ་དེ་གཉིས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་ནས་ཕྱུང་བ་ལས་གཞན་པའི་ནན་ཏུར་བྱས་པ་བསྡིགས་པ་དང་། སྨད་པ་དང་། བསྐྲད་པ་དང་། [^2513]ཕྱིར་འགྱེད་པ་བྱས་པའི་ཡུལ་དག་ལ་ལྷན་ཅིག་གནས་པར་མི་བྱ་བ་ཉིད་དང་ལྷན་ཅིག་ལོངས་སྤྱོད་པར་མི་བྱ་བ་ཉིད་དེ་གཉིས་མི་བྱའོ།[^2514] །འདིར་གཞུང་ནི་བསྡིགས་པའི་ལས་བགྱིས་པ་ལ་སྨད་པའི་ལས་བགྱིས༌[^2515]ན་བགྱིས་པར་བརྗོད་པར་བགྱིའམ། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བྱས་པར་བརྗོད་པར་བྱ་སྟེ།

[Block 2699]
བསྡིགས་པའི་ལས་ནི་བག་ཡངས་སུ་གྱུར་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པས་གནས་ནས་ཕྱུང་བ་ལས།

[Block 2700]
གཞན་པའི་ནན་ཏུར་བྱས་པ་དག་ལ་ནན་ཏུར་གཞན་འཆགས་པར་གསུངས་ནས། གནས་ནས་ཕྱུང་བ་ལ་བསྡིགས་པའི་ལས་བགྱིས་ན་བགྱིས་པར་བརྗོད་པར་བགྱིའམ། ཉེ་བ༌[^2516]འཁོར་མི་བྱ་སྟེ། [^2517]ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་ལོངས་མི་སྤྱོད་པར་བྱ་བའི་ཕྱིར་སོང་བ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
