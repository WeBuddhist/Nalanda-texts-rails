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
དང་པོ་ཚིག་གཅིག་གིས་ནི་བསྒོ་བ་བསྟན། དེའི་འོག་མ་བཅུ་གཅིག་གིས་ནི་དངོས་སུ་བསྟན་པ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 2942 [HEADING]]
###### **དངོས་སུ་བསྟན་པ།** ^4-6-4-2-1-2-2-0

[Block 2943]
མདོ་ལས།

[Block 2944 [HEADING]]
###### **རྒྱུ་དང་འབྲས་བུ་སྦྱར་ཏེ་བསྟན་པ།** ^4-6-4-2-1-2-2-1-0

[Block 2945]
ང་ཡི༌[^2502]ཉན་ཐོས་གནས་བརྟན་རབ་འབྱོར་འདི། །ཞེས་པ་ནས། དྲང་སྲོང་ཆེན་པོ་གསེར་གྱི་སྡོང་པོ་འདྲ། །ཞེས་པའི་བར་དུ་ནི་འདིས༌[^2503]དངོས་སུ་བསྒོ་བ་སྟེ། རྒྱུ་དང་འབྲས་བུ་སྦྱར་ཏེ་བསྟན་པ་དང་། ངོ་མཚར་བདུན་དང་། འཁོར་དང་ཚེའི་ཚད་ལ་སོགས་པ་སྟོན་ཏེ། འདི་ནི་དང་པོའོ། །

[Block 2946 [HEADING]]
###### **ངོ་མཚར་བདུན།** ^4-6-4-2-1-2-2-2-0

[Block 2947]
མདོ་ལས།

[Block 2948]
འཇིག་རྟེན་རྣམས༌[^2504]ལ་ཕན་ཞིང་ཐུགས་བརྩེར༌[^2505]འགྱུར། །ཞེས་པ་ནས། སྲོག༌[^2506]ཆགས་བྱེ་བ་ཁྲག་ཁྲིག་སྒྲོལ་བཞིན་དུ། །ཞེས་པའི་བར་དུ་ནི་ངོ་མཚར་བའི་མཚན་འདི་བསྟན་པའོ། །

[Block 2949 [HEADING]]
###### **འཁོར།** ^4-6-4-2-1-2-2-3-0

[Block 2950]
མདོ་ལས།

[Block 2951]
དེ་ནས་བྱང་ཆུབ་སེམས་དཔའ་མཐུ་ཆེན༌[^2507]མང་།[^2508] །ཞེས་པ་ནས། རྫུ་འཕྲུལ་སྟོབས་ནི་བསམ་གྱིས་མི་ཁྱབ་འགྱུར།[^2509] །ཞེས་པའི་བར་དུ་ནི་འཁོར་རྣམས་སྟོན་ཏེ། །བྱང་ཆུབ་སེམས་དཔའི་འཁོར་དང་། ཉན་ཐོས་པའི་འཁོར་རྣམས་ཅི་རིགས་པར༌[^2510]སྦྱར་རོ། །

[Block 2952]
མདོ་ལས།

[Block 2953]
བྱང་ཆུབ་མཆོག་དེར་རབ་ཏུ་བཤད་པ་ན།[^2511] །ཞེས་པ་ནས། དེ་ལ་རྟག་ཏུ་ཐལ་མོ་སྦྱར་བར་འགྱུར། །ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པས་སྤྲུལ་པ་དང་ཆོས་ཉན་པའི་འཁོར་རྣམས་བསྟན༌[^2512]ཏོ། །

[Block 2954 [HEADING]]
###### **ཚེའི་ཚད།** ^4-6-4-2-1-2-2-4-0

[Block 2955]
མདོ་ལས།

[Block 2956]
དེ་ན་པར་གྱི་བསྐལ་པ་བཅུ་གཅིག༌[^2513]གནས། །ཞེས་པ་ནས། རྐང་གཉིས་མཆོག་གིའོ་ཞེས་པའི་བར་དུ་ནི་ཚེའི་ཚད་བསྟན་པའོ། །

[Block 2957 [HEADING]]
###### འཕགས་པ་ཀཱ་ཏྱཱ་ཡ་ན་ལུང་བསྟན་པ། ^4-6-4-2-2-0

[Block 2958 [HEADING]]
###### **ཚིག་རྐྱང་པས་སྤྲོ་བ།** ^4-6-4-2-2-1-0

[Block 2959]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་གི་དགེ་འདུན་ཐམས་ཅད་ལ་བཀའ་སྩལ་པ་ཞེས་པ་ནས་གསོ་བ༌[^2514]བྱེད་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་འཕགས་པ་ཀཱ་ཏྱཱ་ཡ་ན་ལུང་བསྟན་པ་སྟེ་དབྱེ་བ་དང་ས་བཅད་པ་གོང་མ་དག་འདྲ་བར་སྦྱར་རོ། །

[Block 2960]
མདོ་ལས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་དེ་དག་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ནས་ཡང་ཞེས་པ་ནས་ལྷ་དང་མིའི་མཁན་པོ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་དེ་ཞེས་པའི་བར་དུ་ནི་འཕགས་པ་ཀཱ་ཏྱཱ་ཡ་ན་དེས་སྔོན་གྱི་དུས་དེ་བཞིན་གཤེགས་པ་མང་པོ་ལ་དངོས་སུ་བསྙེན་བཀུར་བགྱིས་པ་དང་། དེ་མྱ་ངན་ལས་འདས་པའི་འོག་ཏུ་ཡང་རིན་པོ་ཆེའི་མཆོད་རྟེན་བྱས་པ་དང་། མཆོད་རྟེན་དེ་ལ་མཆོད་པ་སྣ་ཚོགས་བྱས་པ་སྟེ། བྱང་ཆུབ་སེམས་དཔའི༌[^2515]སྤྱོད་པ་མང་དུ་བྱས་ཏེ༌[^2516]འདིར་ལུང་བསྟན་ཏེ། འཕགས་པ་དེ་ཉིད་སྔོན་དགེ་འདུན་གྱི་གནས་ཁང་ཕྱག་དར་བྱས་པ་ལས་ཚེ་རབས་ཐམས་ཅད་དུ་ལུས་གསེར་གྱི་ཁ་དོག་ཅན་དུ་གྱུར་ཏེ་སྤྱོད་ལམ་མཛེས་པ་འོད་དང་ལྡན་པར་གྱུར་པ་ལས་འདི་སངས་རྒྱས་སུ་གྲུབ་པ་ལུང་བསྟན་པའོ། །

[Block 2961]
མདོ་ལས་སངས་རྒྱས་དེའི་ཞིང་ཡོངས་སུ་དག་པ་ཞེས་པ་ནས་མེ་ཏོག་གིས་ཆལ་པར་བཀང༌[^2517]ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པའི་ཞིང་གི་རྒྱན་སྣ་ཚོགས་བསྟན་པའོ། །

[Block 2962]
མདོ་ལས་སེམས་ཅན་དམྱལ་བ་དང་ཞེས་པ་ནས་ཆོས་ཀྱི་གཟུགས་བརྙན་གནས་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་ཞིང་དེ་ན་ངན་སོང་གསུམ་མེད་པ། ལྷ༌[^2518]དང་མི་མང་བ་དང་། ཕྱི་ནང་གི་འཁོར་མང་དུ་འདུས་པ་དང་། སྐུ་ཚེའི་ཚད་བསྟན་པའོ། །

[Block 2963 [HEADING]]
###### **ཚིགས་སུ་བཅད་པས་བསྡུ་བ།** ^4-6-4-2-2-2-0

[Block 2964 [HEADING]]
###### **བསྒོ་བ།** ^4-6-4-2-2-2-1-0

[Block 2965]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚེ་ན་ཞེས་པ་ནས་གཞན་དུ་མ་ཡིན་པའི་ཚིག་སྨྲ་ཞེས་པའི་བར་དུ་ནི་འདི་ཡན་ཆད༌[^2519]སྟོན་པས་ལུང་བསྒོ་བའོ། །

[Block 2966 [HEADING]]
###### **དངོས་སུ་བསྟན་པ།** ^4-6-4-2-2-2-2-0

[Block 2967]
མདོ་ལས་ངའི་ཉན་ཐོས་གནས་བརྟན་ཀཱ་ཏྱཱ་ཡ་ན་འདི་ཞེས་པ་ནས་དྲི་དང་མེ་ཏོག་རྣམས་ཀྱིས་མཆོད་པར་འགྱུར་ཞེས་པའི་བར་དུ་ནི་རྒྱུ་ལས་གླེངས་ཏེ་ལུང་བསྟན་པའོ། །

[Block 2968]
མདོ་ལས།

[Block 2969]
དེ་ཡིས་ཐ་མའི༌[^2520]ལུས་ཐོབ་ནས། །ཞེས་པ་ནས། ལྷར་བཅས་འཇིག་རྟེན་རྣམས་ཀྱིས་བཀུར་སྟི་བྱས། །ཞེས་པའི་བར་དུ་ནི་ལུང་བསྟན་པའི་འབྲས་བུ་སྟེ། དེ་ཡང་ཞིང༌[^2521]གི་མཚན་ཉིད་དང་། བསོད་ནམས་ཀྱི་མཚན་ཉིད་དོ། །

[Block 2970]
མདོ་ལས།

[Block 2971]
འོད་བྱེད་གཙོ་བོ་བཅོམ་ལྡན་འདས་འགྱུར་བ། །ཞེས་པ་ནས། ཀུན་ཀྱང་འབྱུང་སྤངས་འབྱུང་བ་མེད་པ་ཡིན། །ཞེས་པའི་བར་དུ་ནི་ཚིག་དང་པོ་གཉིས་ཀྱིས་ནི་རང་བཞིན་བསྟན། ཚིག་ཕྱི་མས་འཁོར་བསྟན་ཏོ། །

[Block 2972 [HEADING]]
###### འཕགས་པ་མཽད་གལ་ལུང་བསྟན་པ། ^4-6-4-2-3-0

[Block 2973 [HEADING]]
###### **ཚིག་རྐྱང་པས་སྤྲོ་བ།** ^4-6-4-2-3-1-0

[Block 2974 [HEADING]]
###### **རྒྱུ།** ^4-6-4-2-3-1-1-0

[Block 2975]
མདོ་ལས་དེ་ནས་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་གི་དགེ་འདུན་ཐམས་ཅད་ལ་བཀའ་སྩལ་པ་ཞེས་པ་ནས་གསོལ་བ་བྱེད་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་འཕགས་པ་མཽད་གལ་ལུང་བསྟན་པ་སྟེ། ཚུལ་དབྱེ་བ་ནི་གོང་མ་དང་འདྲའོ། །

[Block 2976 [HEADING]]
###### **སྔ་མའི་དུས།** ^4-6-4-2-3-1-1-1-0

[Block 2977]
ལུང་བསྟན་པ་ཡང་སྔ་མའི་དུས་དང་ཕྱི་མའི་དུས་སོ། །

[Block 2978 [HEADING]]
###### **སངས་རྒྱས་མངོན་དུ་བཞུགས་པ།** ^4-6-4-2-3-1-1-1-1-0

[Block 2979]
སྔ་མའི་དུས་ལ་ཡང་སངས་རྒྱས་མངོན་དུ་བཞུགས་པ་དང་། མྱ་ངན་ལས་འདས་པ་སྟེ། འདི་ནི་སྔོན་དུ༌[^2522]བཞུགས་པ་དང་སྦྱར་རོ། །

[Block 2980 [HEADING]]
###### **མྱ་ངན་ལས་འདས་པ།** ^4-6-4-2-3-1-1-1-2-0
--- END BLOCKS ---
