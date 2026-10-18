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
[Block 2941]
ལམ་ཞེས་བྱ་བ་ནི་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་སྟེ་ཞེས་བྱ་བ་ལ། འཕགས་པ་རྣམས་ཡེ་ཤེས་གང་གིས་བླ་ན་མེད་པའི་བྱང་ཆུབ་འགྲུབ་པའི་ཡེ་ཤེས་དེ་ལ་ལམ་ཞེས་བྱའོ། །

[Block 2942]
ལྟ་བ་ལ་སོགས་པ་བརྒྱད་པོ་དེ་རྣམས་ལམ་གྱི་ཡེ་ཤེས་དེའི་གྲོགས་སུ་གྱུར་པའི་ཕྱིར༌[^2571]ཡན་ལག་ཅེས་བྱ་སྟེ། འཇིག་རྟེན་པའི་ལོག་པར་ལྟ་བ་ལས་བཟློག༌[^2572]པས་ན༌[^2573]ཡང་དག་པའོ། །

[Block 2943 [HEADING]]
#### རྣམ་པར་མི་རྟོག་པ། ^8-7-1-0

[Block 2944]
རྣམ་པར་མི་རྟོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་བསྒོམ་པའི༌[^2574]ལམ་ན་ཡང་དག་པའི་ལྟ་བ་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས་ཡང་དག་པའི་ལྟ་བ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2945]
གང་འདི་འཕགས་པ་འཇིག་རྟེན་ལས་འདས་པ་ཞེས་བྱ་བ་ལ། ཟག་པ་མེད་པ་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ནི་ཡང་དག་པའི་ལྟ་བའོ། །

[Block 2946]
དེ་ཉིད༌[^2575]གང༌[^2576]ཡིན་པ་རྒྱས་པར་བསྟན་པའི་ཕྱིར། བདག་ཏུ་ལྟ་བ་ལ༌[^2577]ཀུན་ནས་ལངས་པ་མ་ཡིན་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བདག་ཏུ་ལྟ་བ་ལས་བྱུང་ཞིང་སྐྱེས་པ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2947]
དགེ་བ་དང་མི་དགེ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་དགེ་བ་དང་མི་དགེ་བ་ལ་སོགས་པའི་ལས་དང་ལས་ཀྱི་འབྲས་བུ་ཡོད་པར་ལྟ་བ་ཡང་མཚན་མར་ལྟ་བ་ཡིན་པས༌[^2578]འཇིག་རྟེན་ལས་འདས་པའི་ཡང་དག་པའི་ལྟ་བ་མ་ཡིན་ཏེ། དེ་དག་ཡོད་པར་ལྟ་བ་ལས་ཀྱང་བྱུང་བ་མ་ཡིན་པའོ། །

[Block 2948]
འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཇི་ཙམ་དུ་མཚན་མར་ལྟ་བ་དེ་ཐམས་ཅད་ལས་བྱུང་བ་མ་ཡིན་པར་སྟོན་ཏེ། མྱ་ངན་ལས་འདས་པ་ལ་ཡང་ཡོད་པར་ལྟ་ན། དངོས་པོར་ལྟ་བ་ཡིན་པས༌[^2579]ཡང་དག་པའི་ལྟ་བར་མི་འགྱུར་རོ། །

[Block 2949 [HEADING]]
#### ཤིན་ཏུ་རྣམ་པར་རྟོག་པ། ^8-7-2-0

[Block 2950]
ཤིན་ཏུ་རྣམ་པར་རྟོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་བསྒོམ་པའི༌[^2580]ལམ་ན་ཡང་དག་པའི་རྟོག་པ་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས་དེ་ལ་ཡང་དག་པའི༌[^2581]རྟོག་པ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2951]
དེ་ལ་མི་རྟོག་ཅེས་བྱ་བ་ནི་ཉོན་མོངས་པ་སྐྱེ་བའི་ཡུལ་དེ་དག་ལ་མི་རྟོག་པ་འམ། ཉོན་མོངས་པ་སྐྱེ་བའི་ཀུན་དུ་རྟོག་པ་མི་སྐྱེད་པའོ། །

[Block 2952 [HEADING]]
#### དུལ་བ། ^8-7-3-0

[Block 2953]
དུལ་བའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་བསྒོམ་པའི༌[^2582]ལམ་ན།[^2583] ཡང་དག་པའི་ངག་གིས་བསྡུས་པ། འཕགས་པ་དགྱེས་པའི་ཚུལ་ཁྲིམས་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཡང་དག་པའི་རྟོག་པ༌[^2584]གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2954]
བདག་ལ་ཡང་ཡོངས་སུ་གདུང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་བདག་དང་གཞན་གྱི་སེམས་ལ་འགྱོད་པ་སྐྱེ་བར་མི་འགྱུར་རོ། །

[Block 2955]
ཀུན་ནས་ཉོན་མོངས་པར་མི་བྱེད་པ་ནི་ཚིག་དེས་བདག་དང་གཞན་འདོད་ཆགས་ཀྱི༌[^2585]ཉོན་མོངས་པ་སྐྱེ་བར་མི་བྱེད་པའོ། །

[Block 2956]
མི་གནོད་པ་ནི་བདག་དང་གཞན་གྱི་སེམས་དང་ལུས་ལ་སྡུག་བསྔལ་སྐྱེད་པར༌[^2586]མི་བྱེད་པའོ། །

[Block 2957]
ལམ་ལ་ལེགས་པར་འཇུག་པ་ནི་ལམ་དང་མཐུན་པའོ། །

[Block 2958]
མཉམ་པར་གཞག་པ༌[^2587]ལ་བརྩོན༌[^2588]པའི་ངག་དེ་དང་ལྡན་ཞེས་བྱ་བ་ནི་གོང་དུ་སྨོས་པ༌[^2589]ལྟ་བུའི་ཚུལ་གྱིས༌[^2590]བདག་དང་གཞན་གཉིས་ཀ་ལ་ཡང་མི་གནོད། འཕགས་པའི་ལམ་དེ་ཐོབ་པར་བྱེད་པའི་རྒྱུར་འགྱུར་བའི་ངག་དེ་ནི། འཁྲུགས་པའམ༌[^2591]མ་སྙོམས་པ་མེད་པས་ན། མཉམ་པར་གཞག་པ་ཞེས་བྱའོ། །

[Block 2959 [HEADING]]
#### ཞི་བ། ^8-7-4-0

[Block 2960]
ཞི་བའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་བསྒོམ་པའི༌[^2592]ལམ་ན་ཡང་དག་པའི་ལས་ཀྱི་མཐའ་བསྡུས་པ། འཕགས་པ་དགྱེས་པའི་ཚུལ་ཁྲིམས་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཡང་དག་པའི་ལས་ཀྱི་མཐའ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2961]
ལས་གནག་པ་ནི་མི་དགེ་བ་བཅུའོ། །

[Block 2962]
ལས་དཀར་བ་ནི་དགེ་བ་བཅུའོ། །

[Block 2963]
ལས་དཀར་གནག་ནི་དགེ་བ་བཅུ་མི་དགེ་བ་དང་འདྲེས་པའོ། །

[Block 2964]
ལས་གང་མི་གནག་མི་དཀར་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི། ཟག་པ་མེད་པ༌[^2593]ལས་འཁོར་བའི་རྒྱུར་མི་འགྱུར་བ་མངོན་པར་འདུ་བྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2965]
ལས་ལ་རྟོན་པ༌[^2594]ཞེས་བྱ་བ་ནི། དེ་ལྟར་ཟག་པ་མེད་པའི་དབྱིངས་ཉིད་དུ་རྟོགས༌[^2595]ཀྱང་། ལས་ཀྱི་རྣམ་པར་སྨིན་པ་མེད་པར་ཡང་མི་རྟོན༌[^2596]ཞེས་བྱ་བའི་དོན༌[^2597]ཏོ། །

[Block 2966 [HEADING]]
#### རབ་ཏུ་ཞི་བ། ^8-7-5-0

[Block 2967]
རབ་ཏུ་ཞི་བའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་བསྒོམ་པའི་ལམ་ན་ཡང་དག་པའི་འཚོ་བས་བསྡུས་པ། འཕགས་པ་དགྱེས་པའི་ཚུལ་ཁྲིམས་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཡང་དག་པའི་འཚོ་བ༌[^2598]གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། གོང་དུ་བཤད་ཟིན་པ་རྣམས་ནི་འདིར་མ་བཤད་པའོ།[^2599] །དགང་སླ་བ་ནི་ཆོས་གོས་དང་བསོད་སྙོམས་ངན་ངོན་གྱིས༌[^2600]མགུ་བའོ། །

[Block 2968]
གསོ་སླ་བ་ནི་ཅུང༌[^2601]ཟད་ཙམ་གྱིས༌[^2602]ཆོག་པའོ། །

[Block 2969]
ཆོ་ག་གང༌[^2603]བཟང་པོའི་ངང་ཚུལ་ཅན་ཞེས་བྱ་བ་ནི་སྤྱོད་པའི་ཆོ་ག་དང་། ཚུལ་ཁྲིམས་བཅོས་པ་མ་ཡིན་གྱི། རང་བཞིན་གྱིས༌[^2604]ཤིན་ཏུ་དག་པའོ། །

[Block 2970]
ཁ་ན་མ་ཐོ་བ་མེད་པ་ནི་ཉེས་པ་ཕྲ་མོ་ཡང་མེད་པའོ། །

[Block 2971]
འཕགས་པས་གནང་བ་ནི་གོང༌[^2605]དུ་བཤད་པ་ལྟ་བུའི་འཚོ་བ་དེ། འཕགས་པས་གནང་བའི་འཚོ་བ་ཡིན་ནོ། །

[Block 2972 [HEADING]]
#### རབ་ཏུ་འབྱུང་བ། ^8-7-6-0

[Block 2973]
རབ་ཏུ་འབྱུང་བའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་བསྒོམ་པའི་ལམ་ན་ཡང་དག་པའི་རྩོལ་བ་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཡང་དག་པའི་རྩོལ་བ༌[^2606]གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2974]
རྩོལ་བ་གང་ཡང་དག་པར་ཞེས་བྱ་བ་ལ། རྩོལ་བ་གང་བྱས་ཤིང་བརྩལ་ན་འཕགས་པའི་ལམ་དང་རྗེས་སུ་མཐུན་ཞིང་བདེན་པ་བཞི་དང་མཐུན་པ་ལ་མྱ་ངན་ལས་འདས་པར་འགྲོ་བའི་ལམ་དུ་གཏོད་པའི་རྩོལ་བ་དེའི་རྗེས་སུ་འགྲོ་བ་དེ་དང་མཐུན་པར་བྱེད་པ་ནི་ཡང་དག་པའི༌[^2607]རྩོལ་བ་ཞེས་བྱའོ། །

[Block 2975 [HEADING]]
#### དགའ་བ་དང་ལྡན་པ། ^8-7-7-0

[Block 2976]
དགའ་བ་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་གང་བསྒོམ་པའི་ལམ་ན་ཚིག་དང་དོན་མི་བརྗེད་པ་ཐོབ་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཡང་དག་པའི་དྲན་པ་གང་ཞེ་ན༌[^2608]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2977]
ཤིན་ཏུ་ཉེ་བར་གཞག་པ་ནི་རྟག་ཏུ་རྩེ་གཅིག་ཏུ་གཞག་པའོ། །

[Block 2978]
མི་སྒུལ་བ་ནི་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས་བསྐྱོད་པར༌[^2609]མི་ནུས་པའོ། །

[Block 2979]
དྲན་པ་ནི༌[^2610]ཡང་དག་པའི༌[^2611]ལྟ་བ་དང་མཐུན་པས་སོ། །

[Block 2980]
གྱ་གྱུ་མེད་པ་ནི་ལོག་པའི་ལྟ་བ་སྤངས་པས་སོ།[^2612] །འཁོར་བའི་སྐྱོན་གྱི༌[^2613]ཉེས་དམིགས་ལ་ལྟ་བ་ནི་ཉོན་མོངས་པ་རྒ་ཤི་ལ་སོགས་པ་ལ་རྟོག་པའོ། །
--- END BLOCKS ---
