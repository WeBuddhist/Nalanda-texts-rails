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
[Block 2556]
དེ་ལྟར་ཡང་རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ༌[^2377]རྫོགས༌[^2378]པ་དག་གིས་དགེ་འདུན་ལ་དགག་དབྱེ་བྱའོ་ཞེས་གསུངས་པ་ལས་ཤེས་སོ། །

[Block 2557]
ཆོས་འདི་པ་ལ་དེ་བྱས་ན་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། ཆོས་འདི་བ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པ༌[^2379]མཚན་མི་མཐུན་པ་དང་། རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ་རྫོགས་པ་དང་། ཁྱིམ་པ་དེ་བཞིན་གཤེགས་པའི་ཆོས་ཀྱི་ལྟ་བ་ཅན་ཐམས་ཅད་བསྡུས་ཏེ། ཆོས་འདི་པ་དེ་དག་ལ་ལྟུང་བ་རིག་པར་བྱ་བ་དེ་བྱས་ནས༌[^2380]ཡང་བྱས་པ་ཉིད་དེ། དེ་རིག་པར་བྱས་ན་བཅབས་པར་མི་འགྱུར་རོ། །

[Block 2558]
དེ་ལ་འདིར་བྱ་བ་ནི་དགེ་འདུན་གྱི་ཡུལ་ལ་མ་གུས་པ་སྤང་བའི་ཕྱིར་ཏེ། མི༌[^2381]རིགས་པ་སྤངས་པར་གསུངས་སོ། །

[Block 2559]
འོ་ན་མདོ་འདི་ཅིའི་ཕྱིར་བྱས་ཤེ་ན། མ་བརྗོད་པ་བརྗོད་པར་བྱ་བའི་ཕྱིར་ཏེ། དེ་བས་ན་མཚན་མི་མཐུན་པ་བསྙེན་པར་རྫོགས་པ་དག་ལ་རིག་པར་བྱེད་ན་ཡང་བཅབས་པར་མི་འགྱུར་ལ། །རིག་པར་བྱེད་པ་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 2560]
འདིར་གཞུང་ནི་ཉེ་བ༌[^2382]འཁོར་གྱིས་ཞུས༌[^2383]པའི་གང་དག་གི༌[^2384]གཞི་ལས།

[Block 2561]
དགེ་སློང་ལ་བརྗོད་ན་བརྗོད་ཅེས་བྱ་བའམ། ཉེ་བ༌[^2385]འཁོར་བརྗོད་ཅེས་བྱའོ། །

[Block 2562]
དེ་བཞིན་དུ་དགེ་སློང་མ་དང་བསླབ་པ་བྱིན་པ་དང་། དགེ་སློབ༌[^2386]མ་དང་དགེ་ཚུལ་དང་དགེ་བསྙེན་དང་དགེ་བསྙེན་མ་ལ་བརྗོད་ན་བརྗོད་ཅེས་བགྱིའམ། ཉེ་བ༌[^2387]འཁོར་བརྗོད་ཅེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2563]
འདོན་པ་གཞན་མ་ལས་ཀྱང་དེ་བཞིན་དུ་ཁས་བླངས་པས་ཁས་མ་བླངས་པ་ལ་རྗོད་པར༌[^2388]བྱེད་ཅིང་ཁས་མ་བླངས་པ་ལ་རྗོད་པར་བྱེད་ན་བརྗོད་ཅེས་བགྱིའམ། ཉེ་བ༌[^2389]འཁོར་བརྗོད་ཅེས་བྱ་སྟེ། ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2564]
མཚམས་གཞན་ན་གནས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་རིག་པར༌[^2390]བྱས་ན་བྱས་པ་ཉིད་ཡིན་པ་སྟེ་འདི་ནི་མཚམས་གཞན་ན་གནས་པ་གང་གི་ཡན་ལག་ཀྱང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེའི་དམིགས་ཀྱིས་བསལ་བ་ཡིན་ནོ། །

[Block 2565]
འདིར་གཞུང་ནི་དེ་བཞིན་དུ་དོག་ས༌[^2391]ལ་མཆིས་པ་ལ་ནམ་མཁའ་ལ་མཆིས་པས་སམ། ནམ་མཁའ་ལ་མཆིས་པ་ལ་དོག་ས་ལ༌[^2392]མཆིས་པས་བརྗོད་ན་བརྗོད་ཅེས་བགྱིའམ། ཉེ་བ༌[^2393]འཁོར་བརྗོད་ཅེས་བྱ་སྟེ། བརྗོད་པ་ལ་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2566]
བསྒོ་བ་ལས་བྱུང་བ་རྣམས་ནི་དགེ་འདུན་ཐམས་ཅད་ལའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལྷག་མ་ཐུན་མོང་བ་བཞི་པོ་དགེ་འདུན་འབྱེད་པ་དང་དེའི་རྗེས་སུ་ཕྱོགས་པ་ལ་སོགས་པ་དང་། དཀོན་མཆོག་གཏོང་བ་དང་འཐབ་ཀྲོལ་བྱེད་པ་ལ་སོགས་པ་བཞི་པོ་ནི་དགེ་སློང་མ་རྣམས་ཀྱིའོ། །

[Block 2567]
ལྟུང་བྱེད་ཐུན་མོང་བ༌[^2394]ལྟ་བའི་རྣམ་པ་མི་གཏོང་བ་དག་གི་བསྒོ་བ་ལས་བྱུང་བའི་ལྟུང་བ་རྣམས་ནི་ཕྱིར་བཅོས་ཤིང་བཤགས་པ་དང་། དེ་དག་རིག་པར་བྱ་བ་ཉིད་དང་དགེ་འདུན་ཐམས་ཅད་ལ་བྱ་བ་ཡིན་ནོ། །

[Block 2568]
འདིར་ལུང་ནི་དགེ་སློང་སྟན་དེ་ཉིད་ལ་འདུག་ནས་དེས་ཚེ་དང་ལྡན་པ་དག་བདག་ལ་དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་བྱུང་ངོ་ཞེས་བརྗོད་པར་བྱ་སྟེ། གལ་ཏེ་རྗོད་པར་བྱེད་ན་དེ་ལྟར་ན་ལེགས་གལ་ཏེ་མི་བརྗོད་ན་དེ་ལ་ཉི་མ་དེ་ཉིད་ནས་བརྩམས་ཏེ་འཆབ་པ་འབྱུང་ངོ་། །དགེ་སློང་དེས་ཚེ་དང་ལྡན་པ་དག་བདག་ལ་ལྟུང་བ་བྱུང་ངོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 2569]
སོ་སོར་བཤགས་པར་བྱ་བ་ནི་གནས་དེར་ཚོགས་པ་ལའོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ལ་ཞེས་བྱ་བར༌[^2395]སྦྱར་ཏེ། གནས་དེར་རིག་པར་བྱ་བའི་དུས་སུ་གང་དག་གི་ཉེ་བར་གནས་པ་ཉིད་དེར་གཏོགས་པ་ཐམས་ཅད་ལ་གདོན་མི་ཟ་བར་ཉེ་བར་བསྡུ་བར་བྱ་བ་ཉིད་ཡིན་གྱི་དགེ་འདུན་དུ་གཏོགས་པ་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2570]
དེ་ལྟར་ཡང་གཞུང་ནི་གནས་ཀྱི་ནང་དུ་སོང་བས་དགེ་སློང་གང་དག་མཐོང་བ་དེ་དག་གི་དྲུང་དུ་ཅི་ནས་ཀྱང་གནས་ཁང་ལ་སོགས་པ་ན་འཁོད་པ་དག་ལ་ཡང་གྲག་པར༌[^2396]འགྱུར་བ་དེ་ལྟར་ཐོས་པ་དང་བཅས་པར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2571]
དེ་ལྟར་བྱས་ན་གལ་ཏེ་ཁ་ཅིག་ལ་གཉིད་ལོག་པ་དང་བྲེལ་བ་ལ་སོགས་པའི་དབང་གིས༌[^2397]གྲག་པར་མ་གྱུར་ན་ཡང་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་འདི་ལ་ཆོ་ག་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2572]
འདིར་གནས་ཀྱི་གཞི་སྨོས་པའི་ནི་འདུ་བའི་གནས་ཀྱི་དཔེ་ཡིན་ཏེ། ཕྱོགས་གང་དུ་དགེ་སློང་དག་འདུ་བ་དེར་ཅི་ནས་ཀྱང་དགེ་ཚུལ་ལ་སོགས་པ་ཐོས་པར་བྱ་བ་མ་ཡིན་པ་དག་གིས་ཐོབ་པར༌[^2398]མི་འགྱུར་བ་དེ་ལྟར་བྱའོ། །

[Block 2573]
འདི་ནི་གནས་བརྟན་ལ་སོགས་པའི་དུས་ཅུང་ཞིག་གནས་པ་ལའང་དེ་ཤེས་པར་བྱའོ། །

[Block 2574]
དེར་འདི་ཇི་ལྟར་རིག་པར་བྱ་བ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཚེ་དང་ལྡན་པ་དག་བདག་ལ་སྨད་པའི་གནས་སུ་གྱུར་པ་མི་རིགས་པ་སོ་སོར་བཤགས་པར་བྱ་བ་བྱུང་གི་ཆོས་དེ་སོ་སོར་འཆགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྤྱད་པ་དེ་ངེས་པར་དམན་པ་ཉིད་དང་ཟས་འདུ་བ་ཉིད་ཡིན་པའི་ཕྱིར་སྨད་པ་ཡིན་ཏེ། འདི་ལྟར་ཟང་ཟིང་མེད་པའི་ཆོས་སྒྲུབ་པའི་ཕྱིར་ཞུགས་པ་རྣམས་ལ་སྨད་པའི་གནས་དེ་ཉིད་ལ་རྒྱུག་པ་ནི་སྒྲུབ་པ་པོ་ལ་མི་རིགས་པ་ཡིན་ནོ། །

[Block 2575]
འདི་ནི་སྨྲེ་སྔགས་འདོན་པའི་རྣམ་པར་བརྗོད་པར་སོ་སོར་བཤགས་པའི་བྱ་བ་ཉིད་དུ་གསུངས་པ་ཡིན་གྱི། བཤགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2576]
བཤགས་པ༌[^2399]ཇི་ལྟར་ལྟུང་བྱེད་ཀྱི་ལྟུང་བ་བྱུང༌[^2400]བས་གཅིག་གི་མདུན་དུ་བཤགས་པར་བྱ་བར་གསུངས་པ་དང་འདྲ་བ་ཡིན་ནོ། །

[Block 2577]
དེ་ནི་སྔགས་དང་འདྲ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རིག་པར་བྱ་བ་དེ་ནི་རང་གི་དོན་དུ་སྔགས་ལན་གསུམ་བརྗོད་པ་དང་འདྲ་བ་མ་ཡིན་ཏེ། ལན་ཅིག་བརྗོད་པས་ཆོག་གོ། །

[Block 2578]
གང་གི་ཕྱིར་སྔགས་ནི་གཞན་གང་ལ་ལན་གསུམ་པར་བྱ་བ་དེའི་མདུན་དུ་ཙོག་པུར་འདུག་སྟེ། ཐལ་མོ་སྦྱར་བར་བྱ་བ་ཡིན་ཏེ་ངེས་པ་དེ་ལ་འདི་བཀག་པའོ། །

[Block 2579]
ཡིད་ཀྱིས་དེ་ལས་ནི་བསྡམ་པར་བྱས་ན་ལྡང་ངོ་ཞེས་བྱ་བ་ནི་ཅང་མི་སྨྲ་བའི་དངོས་པོས་མ་དག་པ་བསྟན་པ་ལ་དམིགས་པ་ནོར་གྱི་ཕྱིར་གཞན་ཤི་བར་འདོད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་ལས་ནི་ཡིད་ཀྱི་ཉེས་བྱས་བསྡམ་པར་བྱ་བ་དོན་གྱི་ཕྱིར་ཡང་མི་བྱའོ་སྙམ་དུ་བསྡམས་པ༌[^2401]ལས་ཕྱིར་བཟློག་པའི་བསམ་པ་བྱས་པ་ལྟུང་བ་ལས་བསྡམ་པར༌[^2402]འགྱུར་བའོ། །

[Block 2580]
འདིར་ཉེ་བ༌[^2403]འཁོར་གྱིས་ཞུས་པའི་གཞུང་ཁ་ཅིག་ལས།

[Block 2581]
ཕྱིན་ཆད་སྡོམ་མམ། སྡོམ་མོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2582]
ལས་གཞན་ལས་ནི་དེ་དང་བཅས་པའི་བཤགས་པའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ཡིད་ཀྱིས་ལྟུང་བ་དེ་ལས་གཞན་ལས་ནི་བསྡམ་པར་བྱ་བ་དེ་དང་བཅས་པའི་བཤགས་པ་བྱས་ན་ལྡང་བ༌[^2404]སྟེ། དག་པ་དང་མ་དག་པ་དག་ནི་བསམ་པའི་གཞི་ལས་བྱུང་བ་ཡིན་པས། བསྡམ་པར་བྱ་བ་མེད་ན་འདིར་བཤགས་པས་ཅིར་ཡང་མི་འགྱུར་རོ། །

[Block 2583]
འདིར་གཞུང་ནི་ཕྱིན་ཆད་སྡོམ་མམ། སྡོམ་མོ་ཞེས་བྱ་བས་སྡོམ་པ་ལྟུང་བ་ལས་ལྡང་བའི་དོན་དུ་ཚིག་ཏུ་བརྗོད་པ་བསྔགས་པ་ཡིན་ནོ། །

[Block 2584]
དེ་ལྟར་ཡང་བསམ་པས་ལྟུང་བ་ལས༌[^2405]ལྡང་བར་སྨྲའི་ཆད་པའི་ལས་ཀྱིས་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2585]
ལུས་མི་མཐུན་པའི་གཉེན་པོ་ནི་འདི་ཡིན་ཏེ། གང་ཞིག་ཀུན་དུ་སྤྱོད་པའི་ཚུལ་ལ་ཕྱིར་བཅོས་པ་དང་སྡུག་བསྔལ་ཡིན་ནོ། །

[Block 2586]
ལུས་པ༌[^2406]རྣམ་པར་འགྱུར་བ་ལ་གཞན་དབང་ཉིད་མེད་པར་སྡོམ་མོ་ཞེས་བྱ་བས་གང་ཞིག་བཤགས་པ་ཁས་ལེན་པའོ། །གང་ལ་བཤགས་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དེ་གཅིག་པུ་ལྟ་བ་ཐ་མི་དད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཞེས་བྱ་བའི་སྒྲས་ནི་རང་བཞིན་དུ་གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྔར་བསྟན་པའི་བྱེ་བྲག་དང་ལྟ་བ་ཐ་མི་དད་པ་བསྟན་ཏོ། །

[Block 2587]
གཅིག་པུ་ཞེས་སྨོས་པའི་སྒྲས་ནི་མང་པོ་དག་བསལ་ཏེ། འདི་ལྟར་གང་ཟག་གཅིག་ལ་བཤགས་པ་འགྲུབ་པར་བསྟན་ཏེ། གང་ཞིག་རང་བཞིན་དུ་གནས་པ་བསྙེན་པར་རྫོགས་པ་དང་བཅས་པ་མཚན་མཐུན་པ་ལྟ་བ་ཐ་མི་དད་པ་ཞེས་གསུངས་པ་དེ་ལྟ་བུ་གཅིག་ལ༌[^2407]བཤགས་པར་བྱའོ། །ཅི་འདིར་ཐམས་ཅད་ལའམ་ཞེ་ན། དེའི་ཕྱིར་ཁ་ན་མ་ཐོ་བ་མི་མཐུན་པ་ལའོ་ཞེས༌[^2408]བྱ་བ་སྨོས་ཏེ། ལྟུང་བ་མི་འདྲ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཇི་ལྟར་ཁ་ན་མ་ཐོ་བ་མི་མཐུན་པ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྡེ་ཚན་ལས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་གླེང་གཞི་དག་ལས་བཙུན་པ་ལྟུང་བ་རིགས་མཐུན་པ་ཞེས་ཀྱང་བགྱི། བཙུན་པ་ལྟུང་བ་རིགས་མི་མཐུན་པ་ཞེས་ཀྱང་བགྱི་ན། བཙུན་པ་ལྟུང་བ་རིགས་མཐུན་པ་ནི་གང་ལགས། ལྟུང་བ་རིགས་མི་མཐུན་པ་ནི་གང་ལགས། ཉེ་བ༌[^2409]འཁོར་ཕམ་པར་གྱུར་པ་གང་ཡིན་པ་ཕམ་པར་གྱུར་པ་དང་རིགས་མཐུན་པ་ཡིན་ལ། དེ་ལས་གཞན་པ་དག༌[^2410]རིགས་མི་མཐུན་པ་ཡིན་ནོ། །

[Block 2588]
དགེ་འདུན་ལྷག་མ་ནི་དགེ་འདུན་ལྷག་མ་དང་ངོ་། །ལྟུང་བྱེད༌[^2411]ནི་ལྟུང་བྱེད་དང་ངོ་། །སོ་སོར་བཤགས་པར་བྱ་བ་ནི་སོ་སོར་བཤགས༌[^2412]པར་བྱ་བ་དང་ངོ་། །ཉེས་བྱས་ནི་ཉེས་བྱས་དང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2589]
འདིར་ཉེས་བྱས་རང་དབང་ཅན་དག་བསྡུས་པར་རིག་པར་བྱ་སྟེ། ལྟུང་བ་གཞན་པ་དང་འབྲེལ་བའི་ཉེས་པ་གང་ཡིན་པ་དེ་ནི་ལྟུང་བ་དེ་བཤགས་པ་ཉིད་ཀྱིས་དེ་ཡང་བཤགས་པ་བྱས་པར་འགྱུར་རོ། །ཅི་དེ་ལས་འདའ་བར་བྱ་བ་མ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་མེད་ན་ལྟུང་བ་ལས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གི་མདུན་དུ་བཤགས་པར་བྱ་བ་སྡེ་ཚན་ལས་ཁ་ན་མ་ཐོ་བ་མི་མཐུན་པ་མེད་པ་ལྟུང་བ་ལ་ཁ་ན་མ་ཐོ་བ་མི་མཐུན་པའི༌[^2413]མདུན་དུ་བཤགས་པར་བྱའོ་ཞེས་བྱ་བའི༌[^2414]དོན་ཏོ། །

[Block 2590]
འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས་བཙུན་པ་ལྟུང་བ་མཐུན་པའི་མདུན་དུ་ལྟུང་བ་བཤགས་སུ་རུང་ངམ། ཉེ་བ༌[^2415]འཁོར་མི་རུང་ངོ་། །རྐྱེན་དེ་ལྟ་བུ་དག་ཡོད་ན་རིགས༌[^2416]མི་མཐུན་པར་བྱ་སྟེ་རུང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2591]
སྤངས་པ༌[^2417]ལས་ནི་སྤངས་པ་དང་བྲལ་བ་སྔོན་དུ་བཏང་བ་ལས་སོ་ཞེས་བྱ་བ་ནི་ལྟུང་བྱེད་ལས་རྫས་དེ་སྤངས་པ་དང་སྤངས་པ་དག་ཞག་གཅིག༌[^2418]བྲལ་བར་བྱ་བ་དེ་གཉིས་སྔོན་དུ་བཏང་སྟེ། བཤགས་ན་ལྡང་བར་འགྱུར་རོ། །

[Block 2592]
བཏང་བ་ལས་སོ་ཞེས་བྱ་བ་ནི་ནང༌[^2419]མ་བྱས་པ་ལས་སོ། །

[Block 2593]
ཞག་དེ་ལ་ཆོས་གོས་གཞན་བྱིན་གྱིས་མི་རློབ་པར༌[^2420]བྱིན་གྱིས་བརླབ་ཏུ་རུང་བའི་ཆོས་གོས་མེད་པར་གནས་པར་བྱའོ། །

[Block 2594]
དེ་གཉིས་སྔོན་དུ་སོང་བའི་བཤགས་པ་བྱས་ན་སྤང་བའི༌[^2421]ལྟུང་བྱེད་ལས་ལྡང་བར་འགྱུར་རོ། །

[Block 2595]
ཆོས་གོས་གཞན་བྱིན་གྱིས་བརླབས༌[^2422]ན་ནི་བྱིན་གྱིས་བརླབ་ཏུ་རུང་བ་དང་བྲལ་བར་མི་འགྱུར་རོ། །
--- END BLOCKS ---
