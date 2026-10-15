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
[Block 2486]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 2487]
གང་གི་ཕྱིར་འདི་རྒྱུ་གཉིས་ཀྱིས་མི་རིགས་ཏེ། སྐབས་མི་འབྱེད་པའི་གང་ཟག་ལ་གླེང་བ་ཉིད་ཀྱང་མི་བྱ་ན་ཁས་ལེན་པ་ལྟ་ག་ལ་ཡོད་དེ། དེའི་ཕྱིར་རྒྱུ་གཅིག་གིས་ཀྱང་མི་རིགས་ལ། གང་སྐབས་མི་འབྱེད་པར་བྱེད་པ་དེ་ལ་ཇི་ལྟར་བྱས་ཀྱང་སྐབས་རྙེད་ཅིང་གླེང་བ་ལ༌[^2282]ཁས་བླང་ངོ་སྙམ་དུ་སེམས་པར་མི་འགྱུར་བས་དེའི་ཕྱིར་རྒྱུ་གཉིས་པ་དེས་ཀྱང་མི་རིགས་སོ། །

[Block 2488]
གླེང་བ་པོས་རང་མ་ལངས་ན་བསྐོ་བས་བསླང་བར༌[^2283]བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གླེང་བ་པོ་རང་ལངས་ནས༌[^2284]སྤྲོ་བར་བྱ་སྟེ། དགེ་འདུན་མཐུན་པར་བསླང་བར༌[^2285]བྱའོ། །

[Block 2489]
རྒྱུ་གང་གིས་ནན་ཏུར་གྱི་ལས་བྱ་བ་དེ་སྤྱིར་བསྟན་པས་ནན་ཏུར་བྱས་པ་ཇི་ལྟར་གྱུར་པ༌[^2286]ལ་བཟོད་པར་བྱ་བ་དེ་བསྟན་པའི་ཕྱིར། གཤེ་བ་དང་ཁྲོ་བ་དང་སྤྱོ་བ་ཉིད་དང་། དགེ་འདུན་གྱི་རྙེད་པ་མེད་པ་དང་། གནས་མེད་པར་བྱ་བར་སེམས་པ་ཉིད་དང་། བླའི་གྲྭ་དང་འོག་ཟུར་དང་། ཉེ་དུའི་གང་ཟག་རྟེན་ཉིད་དང་། དགེ་འདུན་རྟེན་མ༌[^2287]ཡིན་པ་ཉིད་དུ་མི་འཛིན་པ་དང་། ཁྱིམ་པ་དང་མུ་སྟེགས་ཀྱི༌[^2288]རྒྱལ་མཚན་འཆང་བ་དང་། མུ་སྟེགས་ཅན་ལ་བརྟེན་པ་དང་། ཆོ་ག་མ་ཡིན་པར༌[^2289]སྤྱོད་པ་དང་དགེ་སློང་གི་བསླབ་པ་དག་ལ༌[^2290]སློབ་པར་མི་བྱེད་པ་དང་། སྐྲ་འགྲང་བར༌[^2291]གྱུར་པ་དང་། སྐྲ་འཕྱར་བར་གྱུར་པ་དང་། དགེ་འདུན་ལ་སྤུ་སྙོལ་བར་བྱེད་པ་དང་། འབྱུང་བར་བསྐྱོད་པ་དང་མཚུངས་པར་ཉེ་བར་སྟོན་པ་དང་། རྒྱུན་ལས༌[^2292]ཕྱིར་བཟློག་པར༌[^2293]བཟོད་པར་གསོལ་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མི་འཛིན་པ་ཞེས་བྱ་བ་ནི་ཚིག་གོང་མ་བཞི༌[^2294]དང་སོ་སོར་སྦྱར་ཏེ། ཁྱིམ་པ་དང་རབ་ཏུ་བྱུང་བ་དག་ལ་གཤེ་བ་དང་ཁྲོ་བ་དང་། སྤྱོ་བ་ཉིད་དུ་མི་འཛིན་པའོ། །

[Block 2490]
འདིར་གཤེ་བ་ལ་སོགས་པ་ལ་འཇུག་པར་གྱུར་པ་ཉིད་གཟུང་བར༌[^2295]རིག་པར་མི་བྱ་བར་མི་བྱའོ།[^2296] །ཞི་བ་མ་ཡིན་པར་འཇུག་པ་ལ་ཡང་འདིར་བཟོད་པ་གསོལ་བ་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 2491]
བཟོད་པ་གསོལ་བ་དང༌[^2297]འཇུག་པར་འགྱུར་བ་ལ་ཡང་སྔོན་གྱི་གནས་སྐབས་སུ་གྱུར་པའི་གཤེ་བ་ལ་སོགས་པ་ཡང་འདིར་བསྡུས་པར༌[^2298]རིག་པར་བྱའོ། །

[Block 2492]
རྙེད་པ༌[^2299]དང་གནས༌[^2300]པ་དག་གིས་དགེ་འདུན་ལ་སེམས་པར་བྱེད་པ་ཉིད་མི་འཛིན་པའོ། །

[Block 2493]
གལ་ཏེ་དགེ་འདུན་ལ་མ་རྙེད་པའི་ཕྱིར་སེམས་པར་མི་བྱེད་པ་དང་མི་གནས་པའི་ཕྱིར་སེམས་པར་མི་བྱེད་པ་ཞེས་བྱ་བའོ།

[Block 2494]
[^2301] །འདིར་དགེ་འདུན་ཞེས་སྨོས་པ་ནི་དཔེ་ཙམ་དུ་ཟད༌[^2302]དེ་དགེ་སློང་བསྡུས་པའམ། རེ་རེ་ལ་དེ་ལྟར་རྙེད་པ་མ་ཡིན་པ་དང་གནས་མེད་པ་དག་གིས་དེ་ལྟར་སེམས་པ་ཉིད་མི་འཛིན་པ་སྟེ། བཟོད་པར་གསོལ་བ༌[^2303]རིགས་པ་ཉིད་དོ། །

[Block 2495]
ནན་ཏུར་གྱི་ལས་ཀྱི་རྒྱུ་བྱ་བ་ཡོད་པའི་ཕྱིར། བླའི་གྲྭ་དང་འོག་ཟུར་དང་། ཉེ་དུའི་གང་ཟག་རྟེན་ཉིད་དུ་མི་འཛིན་པའོ། །

[Block 2496]
བླའི་གྲྭ་དང་འོག་ཟུར་དང་།[^2304] ཉེ་དུའི་གང་ཟག་ཁྱིམ་པ་དང་རབ་ཏུ་བྱུང་བའི་གང་ཟག་རྟེན་ཉིད་དུ་མི་འཛིན་པ༌[^2305]སྟེ། དེ་དག་རྟེན༌[^2306]ཉིད་དུ་མི་འཛིན་ཅིང་བཟོད་པ་གསོལ་བ་ལ་དགེ་འདུན་གྱིས་བཟོད་པའི་ལས་བྱའོ། །

[Block 2497]
གལ་ཏེ་དེ་ལྟར༌[^2307]དགེ་འདུན་རྟེན་པར་བྱེད་ན་ཁྱིམ་པ་དང་མུ་སྟེགས་ཅན་གྱི་རྒྱལ་མཚན་འཛིན་པར་མི་བྱེད་ཅིང་མུ་སྟེགས་ཅན་ལ་བརྟེན་པ་དང་། ཆོ་ག་མ་ཡིན་པར་སྤྱོད་པར༌[^2308]མི་བྱེད་པ་ཞེས་བྱ་བ་ནི་འདིར་གང་དག་དང་འབྲེལ་པས་འདིར་ཆོ་ག་མ་ཡིན་པ་དག་སྤྱོད་པ་དག་པ་མི་བྱེད་པ་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 2498]
ཁྱིམ་པའི་རྒྱལ་མཚན་འཆང་བ་དང་། མུ་སྟེགས་ཅན་གྱི་རྒྱལ་མཚན་འཆང་བ་དང་། མུ་སྟེགས་ཅན་ལ་བརྟེན་པ་དང་། ཆོ་ག་མ་ཡིན་པར་སྤྱོད་པར་མི་བྱེད་པ་ཞེས་བྱ་བ་དེ་རྣམས་མི་བྱེད་ཅིང་ཞེས་བྱ་བའོ། །

[Block 2499]
འདི་པའི་ཆ་བྱད་གྲུབ་པས་བཟོད་པ་གསོལ་བར་བྱ་བ་ཉིད་དོ། །

[Block 2500]
ཇི་ལྟར་བསྙེན་པར་རྫོགས་པ་ལ་དེ་ཡང་ཁྱིམ་པ་དང་། མུ་སྟེགས་ཅན་གྱི་རྒྱལ་མཚན་འཆང་བས་མི་རིགས་པ་སྟེ།[^2309] ལྟ་བ་ཕུན་སུམ་ཚོགས་པ་དང་ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པར་གྱུར་པས་བསྙེན་པར་རྫོགས་པར་ལྟ་བར༌[^2310]བཟོད་པ༌[^2311]གསོལ་བའོ། །

[Block 2501]
དེ་ཡང་མུ་སྟེགས་ཅན་ལ་བརྟེན་པ་དང་། ཆོ་ག་མ་ཡིན་པ་ལ་སྤྱོད་པ་ལ་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཕུན་སུམ་ཚོགས་པ་གཉིས་མ་ཚང་བས༌[^2312]མི་རིགས་པའོ།[^2313] །དགེ་སློང་གི་བསླབ་པ་དག་ལ་མི་སློབ་པར་མི་བྱེད་པ་ཞེས་བྱ་བ་ནི་སྤོང་བས་བསྡུས་པའི་བསླབ་པ་དག་ལ་སློབ་པར་བྱེད་པ་ཁོ་ནར༌[^2314]བྱེད་པའོ། །

[Block 2502]
སྐྲ་འགྲེང་བར་གྱུར་པ་ཞེས་བྱ་བ་ནི་སྐྲ་དག་གྱེན་དུ་རྣམ་པར་འགྲེང་བར་གྱུར་པ་ཉིད་དོ། །

[Block 2503]
སྐྲ་འཕྱར་བར་གྱུར་པ་ཞེས་བྱ་བ༌[^2315]སྐྲ་དག་ཐད་ཀར་རྣམ་པར་འཕྱར་བར་གྱུར་པ་ཉིད་དོ། །

[Block 2504]
དེ་གཉིས་ཀྱིས་ནི་སྨ༌[^2316]དབབ་པ་ཉིད་དུ་བསྟན་པ་ཡིན་ཏེ། འདི་ལྟར་ན་སྨ་དབབ་པ༌[^2317]ནི་སྐྲ་འགྲེང་བར་གྱུར་པ་དང་། སྐྲ་འཕྱར་བར་གྱུར་པ་ཡིན་ནོ་ཞེས་གྲགས་པའི་ཕྱིར་ཏེ། དེ་ལྟར་གྱུར་ཅིང་བཟོད་པ་ཡང་གསོལ་བ་ལ་དགེ་འདུན་གྱིས༌[^2318]བཟོད་པའི་ལས་བྱའོ། །

[Block 2505]
སྤུ་སྙོལ་བར་བྱེད་པ་ཞེས་བྱ་བ་ནི། སྤུ་འཁུམས་པར་བྱེད་པ་སྟེ། དེས་ནི་རྒྱགས་པ་མེད་པར༌[^2319]བསྟན་ཏེ། འདི་ལྟར་རྒྱགས་པ་དང་བཅས་པའི་སྤུ་དག་སྟེ། དང་པོར་ཤིན་ཏུ་སྤུངས་པར་སྟོན་པས་དེས་ན་འདི་ནི་རྒྱགས་པ་མེད་པ་ཉིད་དུ་བྱེད་པ་བསྟན་ཏེ། དེ་ལྟར་བྱེད་ཅིང་བཟོད་པ་གསོལ་བ་ལ་དགེ་འདུན་གྱིས་བཟོད་པའི་ལས་བྱའོ། །

[Block 2506]
འབྱུང་བ་སྤྱོད་པ༌[^2320]དང་ཞེས་བྱ་བ་ལ་འབྱུང་བ་ནི་འབྱུང་བ༌[^2321]སྟེ། རིགས་པ་མ་ཡིན་པ་དག་པ༌[^2322]མ་ཡིན་པ་སྨད་པ་ཞེས་བྱ་བའི་གནས་ཀྱི་བྱེ་བྲག་དེ་ནས་རྣམ་པར་དག་པའི་ལམ་དུ་ཞུགས་ཤིང་འབྱུང་བ་ནི་འབྱུང་བ༌[^2323]ཞེས་བྱའོ། །

[Block 2507]
མཚུངས་པ་ཞེས་བྱ་བ་ནི་ཡང་དག་པ་ཉིད་དུ་གྱུར་པར་འཇུག་སྟེ། དགེ་འདུན་དང་འདྲ་དགེ་འདུན་དང་མཚུངས་པར་འཇུག་པའོ། །

[Block 2508]
དེར་ཉེ་བར་སྟོན་པ་ནི་གང་གིས་འདི་བདག་ཅག་དང་མཚུངས་པར་འགྱུར་ཏེ་ཞེས་བྱ་བས་ཤེས་པར་གྱུར་པས་འདུད་པ་དང་། རྗེས་དང་བཅས་པས་མཉན༌[^2324]ཞིང་རྗེས་སུ་མཐུན་པའི་བྱ་བ་དང་། མཛའ་བར་གྱུར་པའི་སྤྱོད་པ་དང་ལྡན་ཞིང་གུས་པ༌[^2325]དང་རྗེས་གཉིས་ཀྱི་བདག་ཉིད་དུ་གྱུར་པ་ནི་ནང་དུ་གནས་ཤིང་ཞེས་བྱ་བས་ཤེས་པ་ཡིན་ནོ། །

[Block 2509]
རྒྱུ་ལས་ཕྱིར་བཟློག་པ་ཞེས་བྱ་བ་ནི་འཐབ་ཀྲོལ་བྱེད་པ་ཉིད་ལ་སོགས་པའི་རྒྱུ་གང་གིས་དེ་ལ་ནན་ཏུར་གྱི་ལས་བྱས་པར་གྱུར་པའི་རྒྱུ་དེ་ལས་ཕྱིར་བཟློག་པས་ཏེ། དེ་ནས་བསམ་པ་ཞུགས་པ་འགའ་ཞིག་ལ་ཡང་ལམ་རྣམ་པར་དག་པ་ལ་དེ་དང་འབྲེལ་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2510]
ལོག་པའི་ལམ་ལ་གོམས་པས་འདི་ལས་ངེས་པར་འབྱུང་བས་བསྟན་པའི་དོན་དུ་འདི་སྨོས་སོ། །

[Block 2511]
དེ་ལྟ་བུར་གྱུར་པ་ལ་ཡང་གསོལ་བ༌[^2326]མེད་པར་བཟོད་པའི་ལས་མི་བྱའོ། །

[Block 2512]
བཟོད་པ་དེ་གསོལ་ན་བཟོད་པའི་ལས་བྱའོ། །

[Block 2513]
ལས་སྦྱིན་པ་དང་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པར་བྱ་བ་དང་། གཞིག་པ་དང་བསྲང་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ལས་ཀྱི་སྦྱིན་པའམ་ལས་གྱི་བདག་ཉིད་སྦྱིན་པ་འདི་ལྟ་སྟེ། ཁང་པ་དང་གཙུག་ལག་ཁང་བསྟན་པ་ལ་སོགས་པའི་ལས་སྦྱིན་པའོ། །

[Block 2514]
དེ་ཡང་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་དང་ཁྱིམ་གྱི་བསླབ་པ་གཞིག་པ་དང་། ལྷུང་བཟེད་ཁ་སྦུབ་པ་རྣམས་ཀྱི་གསོལ་བ་ཉིད་ཀྱིས་སོ། །

[Block 2515]
འོ་ན་བསྙེན་པར་རྫོགས་པ་སྨོས་པ་ཁོ་ན་ཡིན་ན། [^2327]བསྙེན་པར་རྫོགས་པར་གསོལ་བར་བྱའོ་ཞེས་བྱ་བས་མ་ཡིན་ནམ་ཞེ་ན། བརྗོད་པར་བྱ་སྟེ་གཙོ་བོ་མ་ཡིན་པའི་དངོས་པོས་འདིར་གསོལ་བ་འདི་མངོན་པར་བསྟེན༌[^2328]པའོ། །

[Block 2516]
འདིར་ལས་བྱེད་པ་པོའི་བྱ་བ་སྒྲུབ་པར་གྱུར་པ་ལ་ཆོ་ག་འདི་ཐོབ་པའོ། །

[Block 2517]
ཤུགས་ཀྱིས་ཐོབ་པ་ལ་དངོས་སུ་སྨོས་པ་ལ་ཉེས་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2518]
གཞི་མ་ཞི་བར་ཤེས་ནས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནན་ཏུར་གྱི་ལས་ཀྱི་རྒྱུ་ཐུན་མོང་བ་བསྟན་ནས། ད་ནི་རྒྱུ་གང་ལ་ནན་ཏུར་གྱི་ལས་གང་དག་བྱ་བ་དེ་དག་གི་བྱེ་བྲག་བསྟན་པར་བྱ་སྟེ། འཐབ་ཀྲོལ་བྱེད་པ་ལ༌[^2329]ལས་ཀྱིས་བསྡིགས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འཐབ་ཀྲོལ་བྱེད་པ་ལ་ལས་ཀྱིས་བསྡིགས་པར་བྱ་བའི་དོན་ཏོ། །

[Block 2519]
དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་ཕྱིར་མི་འཆོས་པར་རྒྱུན་དུ་བྱེད་པ་ལ་ནི་སྨད་པའོ་ཞེས་བྱ་བ་ནི་ལས་ཀྱིས༌[^2330]ཞེས་བྱ་བ་འདི་དང་འོག་མ་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་ཤེས་པར་བྱའོ། །

[Block 2520]
དགེ་འདུན་ལྷག་མའི་བདག་ཉིད་ཀྱི་ལྟུང་བ་ཡང་དང་ཡང་དུ་འབྱུང་བ་གང་ལ་ཡོད་པ༌[^2331]ནི་ཡང་དང་ཡང་དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་ཅན་ཏེ་དེ་ལའོ། །

[Block 2521]
ཕྱིར་མི་འཆོས་པ༌[^2332]བསྟན་པ༌[^2333]སྨད་པར་བྱ་བའི་ལས་བྱའོ། །

[Block 2522]
ཚར་བཅད་ནས༌[^2334]ནན་ཏུར་གྱི༌[^2335]ལས་རིགས་པ་ཡིན་ཏེ། དག་པ་ལ་འཇུག་པར་གྱུར་པ་ལ༌[^2336]ནི༌[^2337]མ་ཡིན་ནོ་སྙམ་དུ་བྱས་ནས༌[^2338]སོ། །

[Block 2523]
ཁྱིམ་སུན་འབྱིན་པ་ལ་ནི་བསྐྲད་པའོ་ཞེས་བྱ་བ་ནི་གང་གི་ཁྱིམ་སུན་འབྱིན་པ་མ་བཏང་བ་དེ་གནས་དེ་ནས་བསྐྲད་པའི་ལས་བྱའོ། །

[Block 2524]
དེའི་ཕྱིར་འདུ་བ་མི་སྦྱིན་པ་དང་སྐབས་མི་འབྱེད་པ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་དེའི་ཕྱིར་ཞེས་བྱ་བ་ནི་གནས་ནས་བསྐྲད་པའི་ཕྱིར་རོ། །

[Block 2525]
གླེང་བའི་ཕྱིར་ཡོངས་སུ་རྫོགས་པས་དེའི་དོན་ཉིད་དུ་རིག་པར་བྱའོ། །
--- END BLOCKS ---
