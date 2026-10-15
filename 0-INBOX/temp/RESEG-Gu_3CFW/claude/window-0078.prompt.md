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
[Block 2731]
དེ་བས་ན་གནས་ནས་དབྱུང་བ་ཉིད་ལ་སྡོམ་པ་འདི་བྱ་བ་ཉིད་ཤེས་པ་འདིའོ། །

[Block 2732]
ནན་ཏུར་གྱི་རྒྱུ་གཞན་ལ་དེའི་དོན་དུ་བསམ་པ༌[^2548]གཞན་བྱེད་པ་ནི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་ནན་ཏུར་གྱི་རྒྱུ་གཞན་ཡོད་པ་ལ་དེའི་དོན་དུ་བསམ་པ་ཞེས་བྱ་བ་ནི་གང་གི་རྒྱུ་དེ་ཉེ་བར་གནས་པ་དེའི་བདག་ཉིད་རང་གི་ངོ་བོར་གྱུར་པའི་དོན་གང་ཡིན་པ་དེ་ནི་ནན་ཏུར་གཞན་གྱི་མིང་གིས་བསམ་པ་གང་ཡིན་པ་དེ་ནི་དེའི་དོན་དུ་བསམས་པ༌[^2549]སྟེ། ནན་ཏུར་གྱི་རྒྱུ་ཉེ་བར་གནས་པ་དེའི་དོན་ཏོ། །

[Block 2733]
གལ་ཏེ་བསྡིགས་པའི་ནན་ཏུར་གྱི་རྒྱུ་ཉེ་བར་གྱུར་པ་དེའི༌[^2550]དོན་དུ་བསམས་པས༌[^2551]བསྐྲད་པ་ལ་སོགས་པའི་མིང་གི་ནན་ཏུར་གྱི་ལས་བྱེད་ན་དེ་ལྟར་ན་ཡང་བསྡིགས་པའི་ནན་ཏུར་གྱི་ལས་ཉིད་འཆགས་པར་འགྱུར་རོ། །

[Block 2734]
གཞན་དུ་ན་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་དེའི་མིང་གི༌[^2552]དོན་འདོད་པ་ཉིད་དུ་མི་སེམས་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2735]
འཐབ་ཀྲོལ་བྱེད་པ་ཉིད་ལ་སྐྲོད་པར་བྱེད་པའི་ལས་བྱེད་པ་ལ་གལ་ཏེ་འཐབ་ཀྲོལ་བྱེད་པ་ཉིད་སྐྲོད་པར་བྱེད་པའི་ཡིད༌[^2553]ཅན་གྱི་དོན་ལ་དགོངས་ནས་སྐྲོད་པར་བྱེད༌[^2554]ན་བསྐྲད༌[^2555]པར་བྱ་བ་དེ་འབྱུང་ངོ་། །གལ་ཏེ་ཁྱིམ་སུན་འབྱིན་པ་ཉིད་ཀྱི་དོན་ལ་དོགས་ནས་འཐབ་ཀྲོལ་བྱེད་པའི་རྒྱུ་ཡོད་པ་ལ་སྐྲོད་པའི་ལས་བྱེད་ན། དེས་ན་ལས་དེ་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 2736]
དེ་བས་ན་དེ་ལ་འདི་སྐད་བརྗོད་དོ། །

[Block 2737]
གཞན་ལས་ཉམས་སོ་ཞེས་བྱ་བ་ནི་ནན་ཏུར་གཞན་བྱས་པ་ལ་སྔ་མ་ཉམས་པ་ཡིན་ཏེ། གཞན་མི་འཆགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2738]
སྤྱིར་ནན་ཏུར་བྱེད་པ་རྣམས་ལ་དེ་བསྐྲད་པའི་རྣམ་པ་ཉིད་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 2739]
ནན་ཏུར་གཞན་བྱས་ན་ནན་ཏུར་སྔར་བྱས་པ་ཉམས་སོ། །

[Block 2740]
འདིར་གཞུང་ནི་དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 2741]
བཙུན་པ་རེ་ཞིག་བསྡིགས་པའི་ལས་བགྱིས་པ་ལ་སྨད་པའི་ལས་བརྗོད་པར་བགྱིའམ། [^2556]བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བྱས་པར༌[^2557]བརྗོད་པར་བྱ་སྟེ། བསྡིགས་པའི་ལས་ནི་བག་ཡངས་སུ་གྱུར་ཏོ། །

[Block 2742]
བཙུན་པ་གནས་ནས་ཕྱུང་བ་ལ་བསྡིགས་པའི་ལས་བགྱིས་ན་བགྱིད་པར་བརྗོད་པར་བགྱིའམ། ཉེ་བ༌[^2558]འཁོར་མི་བྱ་སྟེ། དེ་ཅིའི༌[^2559]ཕྱིར་ཞེ་ན། དེ་ནི་ལོངས་མི་སྤྱད་པའི་ཕྱིར༌[^2560]སོང་བའི་ཕྱིར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2743]
གནས་ནས་ཕྱུང་བ་ལ་ནི་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་གནས༌[^2561]ནས་ཕྱུང་བ་བདག་ཉིད་ཀྱིས་ནན་ཏུར་བྱས་པ་ལ་ནི་ཕྱི་མ་མི་འཆགས་ཏེ་སྔ་མ་ཉམས་པར་ཡང་མི་འགྱུར་ཏེ། དེ་ལོངས་མི་སྤྱད་པའི་ཕྱིར་སོང་བ་ཉིད་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་འདིར་རྒྱུ་སྨོས་ཏེ། ལོངས་མི་སྤྱད་པར་སོང་བ་མ་ཡིན་ཏེ་འདིར་དགེ་འདུན་ལ་ཞེས་བྱ་བའི་དོན་དེ་རིག་པར༌[^2562]བྱའོ། །ཤེས་པ་དང་། བསོད་ནམས་ཆེན་པོ་དང་། མདོ་སྡེ་དང་འདུལ་བ་དང་། མ་མོ་འཛིན་པ་དང་། ཐོས་པ་མང་བ་དང་། ཕྱོགས་མང་བ་དང་། འཁོར་མང་བ་དག་ལ་ནི་སྦོམ་པོའོ་ཞེས་བྱ་བ་ཤེས་པ་དང་། བསོད་ནམས་ཆེན་པོ་དང་། མདོ་སྡེ་འཛིན་པ་དང་། འདུལ་བ་འཛིན་པ་དང་། མ་མོ་འཛིན་པ་དང་། ཐོས་པ་མང་བ་དང་། ཕྱོགས་མང་བ་དང་། འཁོར་མང་བ་ཆོས་ཀྱི༌[^2563]གནས་ནས་འབྱིན་ན་དབྱིན་གྱི་སྐབས་སུ་གཏོགས་པའི་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2744]
དབྱེ་བར་འདོད་པས་དེས་རྒྱས་པར་གྱུར་པ་དང་། གཞན༌[^2564]ཆོས་དང་ལྡན་པ་ཡང་མངོན་པར་འདོད་པས་གང་ཟག་ལྔ་པོ་ལ༌[^2565]ནན་ཏུར་བྱེད་པ་ནི་ཉེས༌[^2566]བྱས་སོ། །

[Block 2745]
ཕྱི་རོལ་པའི༌[^2567]རྟོག་གེ་དང་། སྒྲ་དང་སྤྱོད་པ་ལ་སོགས་པའི་ཐོས་པ་མང་བ་དང་ལྡན་པའི་མདོ་སྡེ་ལ་སོགས་པའི་དོན་ལ་ཐོས་པ་མང་བས་ཞེས་སྨོས་པས་སོ། །

[Block 2746]
ཁྱིམ་པ་ནི་དཔེའོ། །

[Block 2747]
དགེ་སློང་ལ་སོགས་པ་ལྔ་པོ་དག་ལ་བརྙས་ཐབས་བྱེད་པ་དག་ལ་ཡང་ཕྱིར་འགྱེད་པ་བྱའོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་ལ་བརྙས་ཐབས་བྱེད་པ་ལ་ཕྱིར་འགྱེད་པའི་ལས་བགྱིའམ། ཉེ་བ༌[^2568]འཁོར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 2748]
ཕྱིར་འགྱེད་པའི་ལས་བྱའོ་ཞེས་གང་གསུངས་པ་དེ་ནི་དཔེ་ཙམ་དུ་ཟད་དེ་དེ༌[^2569]དང་ཁྱིམ་པ༌[^2570]རིག་པར་བྱའོ། །

[Block 2749]
དགེ་སློང་དང་དགེ་སློང་མ་དང་། དགེ་སློབ་མ་དང་། དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་དག་ལ་བརྙས་ཐབས་བྱེད་པ་ལ་ཡང་ཕྱིར་འགྱེད་པའི་ལས་བྱ་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 2750]
འདིར་གཞུང་ནི་གླེང་གཞི་དག་ལས།

[Block 2751]
བཙུན་པ་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་ཁྱིམ་པ་ལ་བརྙས་ཐབས་བགྱིད་པ་ལ་ཕྱིར་འགྱེད་པའི་ལས་བྱའོ་ཞེས་གསུངས་ན། བཙུན་པ་དགེ་སློང་ལ་བརྙས་ཐབས་བགྱིད་པར་གྱུར་ན་དེ་ཡང་ཕྱིར་འགྱེད་པའི་ལས་བགྱི་འམ། ཉེ་བ༌[^2571]འཁོར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 2752]
ཁྲོ་བ་ནི་བརྙས་ཐབས་མ་ཡིན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི།

[Block 2753]
འདིར་གཞུང་ཁ་ཅིག་ལས།

[Block 2754]
ཁྲོ་བ་ནི་བརྙས་ཐབས་བྱེད་པ་ཡིན་པས་དེ་ལ་ཡང་ཕྱིར་འགྱེད་པའི་ལས་བྱ་བ་ཡིན་ནོ། །

[Block 2755]
ཁྲོ་བ་ལ་ཡང་འདི་རྣམས་ཀྱི༌[^2572]ཕྱིར་འགྱེད་པར་བྱ་བ་ཉིད་དོ། །

[Block 2756]
ནན་ཏུར་གྱི་ལས་དག་ལ་ཐུན་མོང་བ༌[^2573]མ་ཡིན་པར་དོགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ནི་དགེ་སློང་མ་རྣམས་ཀྱི་ཆོ་ག་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2757]
རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ༌[^2574]རྫོགས་པ་ལ༌[^2575]ཡང་དེ་དག་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་དག་བྱ་བ་ཉིད་ནི་ནན་ཏུར་གྱི་ལས་དག་དང་། བསྙིལ་བའི་ཆོ་ག་འདི་ལ་དམིགས་ཀྱིས་བསལ་བར་རིག་པར་བྱའོ། །

[Block 2758]
ཁྱིམ་པ་ལ་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཁྱིམ་པ་ལ་ནན་ཏུར་གྱི་ལས་དག་མི་བྱ་བ་སྟེ། དེ་ལ་དགེ་སློང་མི་དབང་བའི་ཕྱིར་རོ། །

[Block 2759]
དགེ་སློང་ལ་ཕམ་པར་འགྱུར་བ་ཡང་དག་པ་མ་ཡིན་པས་སྐུར་པ་དང༌[^2576]གཤེ་བ་དང་སྤྱོ་བ་ལ་ལྷུང་བཟེད་ཁ་སྦུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི། གསོལ་བ་འབའ་ཞིག་གི་ལས་ཀྱིས་ལྷུང་བཟེད་ཁ༌[^2577]སྦུབ་པར་བྱའོ་ཞེས་བྱ་བར༌[^2578]སྦྱར་རོ། །སུ་ལ་ཁས་སྦུབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཡང་དག་པ་མ༌[^2579]ཡིན་པས་སྐུར༌[^2580]པའི་ཁྱིམ་པ་ལའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2760]
སྐུར་པ་འདེབས་པ་པོ༌[^2581]གང་གི་ཕྱིར་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་ལ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆོས་འདི་པའི་རབ་ཏུ་བྱུང་བ་ནི་དཔེ་ཙམ་ཡིན་ནོ། །

[Block 2761]
གང་གིས༌[^2582]སྐུར་པ་བཏབ་པ་ལ་ཞེ་ན། དེའི་ཕྱིར་ཡང་དག་པ་མ་ཡིན་པའི་ཕམ་པར་འགྱུར་བས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཕམ་པའི་སྒྲ་ནི་དཔེ་ཡིན་ཏེ། ཚུལ་ཁྲིམས་ལྷུར་བྱ་བ༌[^2583]ཡིན་ནོ། །

[Block 2762]
ལྟུང་བ་ལྷུར་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 2763]
དེ་ན་རབ་ཏུ་བྱུང་ཞིང་བསྙེན་པར་མ༌[^2584]རྫོགས་པ་ལ་སྐུར་པ་འདེབས་པ་ལ་བྱ་བ་རིགས་པར་གྱུར་པ་ཉིད་དུ་ཤེས་པར་བྱའོ། །ཅི་དེ་ཉིད་ལ་བརྟེན་ནས་སམ་ཞེ་ན། དེའི་ཕྱིར་གཤེ་བ་དང་། སྤྱོ་བ་ལ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་འབྱུང་བ་དང་མི་འབྱུང་བ་ཁྱད་པར་མ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་གཉིས་ཀ༌[^2585]ལྟར་ཤེས་པའོ། །

[Block 2764]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་ཆོས་གཉིས་དང་ལྡན་པའི་ཁྱིམ་བདག་ལ་ལྷུང་བཟེད་ཁས༌[^2586]སྦུབ་པར་བྱ་སྟེ། གཉིས་གང་ཞེ་ན། དགེ་སློང་དག་ལ་གཤེ་བ་དང་སྤྱོ་བར་བྱེད་པ་དང་། དགེ་སློང་དག་པ་ལ་གཞི་མེད་པ་ལ་ཕམ་པར་འགྱུར་བའི༌[^2587]ཆོས་ཀྱིས་སྐུར་པ་འདེབས་པ་ལའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2765]
ཅི་ཁས༌[^2588]ཕུབ་ཏུ་གཞག་པས་ཁ་དབུབ་པར་བྱ་བའམ།[^2589] ཇི་སྲིད་དུ་གན་རྐྱལ་དུ་མ་བྱས་པ་དེ་སྲིད་དུ་འདི་ལ་སུས་ཀྱང་ལྷུང་བཟེད་མེད་པར་མི་བྱའོ།[^2590] །འོན་ཏེ་གཞན་གྱིས་ཤེ༌[^2591]ན། དེའི་རྣམ་པར་གཞག་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ལྷུང་བཟེད་བཟེད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ཁྲིམས་སུ་བྱ་བ་རྣམ་པར་གཞག་པར་བྱ་བས༌[^2592]ཡིན་གྱི། ལྷུང་བཟེད་ཀྱི༌[^2593]དབྱིབས་སུ་གྲུབ་པས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2766]
རྣམ་པ་གང་གིས་དེ་རྣམ་པར་གཞག་པར༌[^2594]བྱ་ཞེ་ན། དེའི་ཕྱིར་གསོལ་བས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གསོལ་བ་འབའ་ཞིག་གི་ལས་གྱིའོ། །

[Block 2767]
གང་གི་ཕྱིར་ཁས༌[^2595]སྦུབ་པ་དེའི་དོན་བརྗོད་པར་བྱ་སྟེ། ལྷུང་བཟེད་ཁས༌[^2596]སྦུབ་བའི་ཁྱིམ་དུ་འགྲོ་བར་མི་བྱའོ། །

[Block 2768]
སྟན་ལ་འདུག་པར་མི་བྱའོ། །

[Block 2769]
སྦྱིན་པར༌[^2597]བྱ་བའི་ཆོས་བཤམས་པ་ལས་ཡོངས་སུ་ལོངས་སྤྱོད་པར༌[^2598]མི་བྱའོ་ཞེས་བྱ་བ་ལ་འདིས་ནི་གཙུག་ལག་ཁང་ཡང་སྤང་བར་ཡང་རིག་པར་བྱའོ། །

[Block 2770]
དེ་ལྟར་ཡང་འདིར་གཞུང་ཁ་ཅིག་ལས་སྦྱིན་པར་བྱ་བའི་ཆོས་སྔར་བཤམས་པ་དག་ཡོངས་སུ་ལོངས་སྤྱད་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
