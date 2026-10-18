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
[Block 3046]
མདོ་ལས།

[Block 3047]
འདིས་སྡིག་པ་མི་དགེ་བའི་ཆོས་ཞེས་བྱ་བ་ནས་རྒྱས་པར་རྒ་ཤིར་འགྱུར་བའི་བར་རྣམ་པ་དུ་མ་ཞི་བར་བྱས་པ་ཡིན་པས། དེའི་ཕྱིར་དགེ་སྦྱོང་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3048]
སོ་སོའི་སྐྱེ་བོ་ནི༌[^2110]གཏན་དུ་ཞི་བར་མི་བྱེད་པའི་ཕྱིར་དོན་དམ་པའི་དགེ་སྦྱོང་མ་ཡིན་ནོ། །

[Block 3049 [HEADING]]
##### དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་འདུས་བྱས་དང་འདུས་མ་བྱས། ^3-2-11-2-0

[Block 3050]
དགེ་སྦྱོང་གི་ཚུལ་དེའི་འབྲས་བུ་འདུས་བྱས་འདུས་མ་བྱས། དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་རྣམས་ཡིན་ནོ།[^2111] དེ་དག་ཀྱང་མདོ་ལས་རྣམ་པ་བཞིར་གསུངས་སོ། །

[Block 3051]
གཞན་ཡང་དེ་དག་བརྒྱད་ཅུ་རྩ་དགུའོ། །

[Block 3052 [VERSE]]
དེ་དག་ཀྱང་གང་ཞེ་ན། །
གྲོལ་ལམ་ཟད་པ་རྣམས་དང་བཅས། །

[Block 3053]
མཐོང་བས་སྤང་བར་བྱ་བ་སྤོང་བར་བྱེད་པའི༌[^2112]བར་ཆད་མེད་པའི་ལམ་བརྒྱད་དང་། རྣམ་པར་གྲོལ་བའི་ལམ་བརྒྱད་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བ་སྤོང་བར་བྱེད་པ་ས་དགུ་པོ་རེ་རེ་ཞིང་ཡང༌[^2113]ཉོན་མོངས་པ་རྣམ་པ་དགུ་དགུ་སྤོང་བར་བྱེད་པ་དེ་སྙེད་ཁོ་ནའི་བར་ཆད་མེད་པའི་ལམ་དང་རྣམ་པར་གྲོལ་བའི་ལམ་དག་གོ། །

[Block 3054]
དེ་ལ་བར་ཆད་མེད་པའི་ལམ་རྣམས་ནི་དགེ་སྦྱོང་གི་ཚུལ་ཡིན་ནོ། །

[Block 3055]
རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་ནི་དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་འདུས་བྱས་དག་ཡིན་ཏེ། དེའི་རྒྱུ་མཐུན་པ་དང་། སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3056]
ཉོན་མོངས་པ་དེ་དག་གི་སྤངས་པ་ནི་དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་འདུས་མ་བྱས་དག་ཡིན་ཏེ། དེ་ལྟར༌[^2114]བརྒྱད་ཅུ་རྩ་དགུ་ཡིན་ནོ། །

[Block 3057]
དེ་ལྟར་ན་འོ་ན་ནི་སངས་རྒྱས་ཀྱིས་གསུངས་པ་ཁ་བསྐང་བར༌[^2115]བྱ་དགོས་པར་འགྱུར་རོ༌[^2116]ཞེ་ན། བྱ་མི་དགོས་ཏེ། གལ་ཏེ་ཡང་འབྲས་བུ་རྣམས་མང་མོད་ཀྱི།

[Block 3058 [HEADING]]
##### འབྲས་བུ་བཞི་རྣམ་པར་གཞག་པའི་རྒྱུ་ལྔ། ^3-2-11-3-0

[Block 3059 [VERSE]]
འབྲས་བུ་བཞི༌[^2117]རྣམ་གཞག་པ་ནི། །
རྒྱུ་ལྔ་དག་ནི་སྲིད་ཕྱིར་རོ། །

[Block 3060]
བཅོམ་ལྡན་འདས་ཀྱིས་སྤོང་བའི་ལམ་གྱི༌[^2118]གནས་སྐབས་གང་ལ་རྒྱུ་ལྔ་སྲིད་པ་དེ་ལ་འབྲས་བུ༌[^2119]རྣམ་པར་གཞག་གོ་ཞེས་གྲག་གོ། །

[Block 3061]
ལྔ་གང་ཞེ་ན། །

[Block 3062 [VERSE]]
འབྲས་ལ་སྔོན་ལམ་བཏང་བ་དང་། །
གཞན་ཐོབ་པ་དང་ཟད་བསྡོམས་དང་།
ཤེས་པ་བརྒྱད་ཚན༌[^2120]ཐོབ་པ་དང་། །

[Block 3063]
རྣམ་པ་བཅུ་དྲུག་ཐོབ་པའོ།[^2121] །ལམ་སྔ༌[^2122]མ་བཏང་བ་དང་སྔོན་མེད་པའི་ལམ་ཐོབ་པ་ནི་ཞུགས་པ་དང་འབྲས་བུའི་ལམ་བཏང་བ་དང་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 3064]
སྤངས་པ་བསྡོམས་པ་ནི་ཐམས་ཅད་ཀྱིས༌[^2123]ཐོབ་པ་ཅིག་རྙེད་པའི་ཕྱིར་རོ། །ཤེས་པ་བརྒྱད་ཅིག་ཅར་དུ་འཐོབ་པ་ནི་ཆོས་དང་རྗེས་སུ་ཤེས་པ་རྣམ་པ་བཞིའོ། །

[Block 3065]
རྣམ་པ་བཅུ་དྲུག་ཐོབ་པ་ནི་མི་རྟག་པའི་རྣམ་པ་ལ་སོགས་པ་སྟེ། རྒྱུ་ལྔ་པོ་དེ་དག་ནི་འབྲས་བུ་རེ་རེ་ལ་ཡོད་དོ། །

[Block 3066 [HEADING]]
##### འཇིག་རྟེན་པས་ཐོབ་པའི་འབྲས་བུ། ^3-2-11-4-0

[Block 3067]
གལ་ཏེ་ཟག་པ་མེད་པའི་ལམ་ཁོ་ན་དགེ་སྦྱོང་གི་ཚུལ་ཡིན་ན་འཇིག་རྟེན་པའི་ལམ་གྱིས་ཐོབ་པའི་འབྲས་བུ་གཉིས་ཇི་ལྟར་དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུར་རུང་ཞེ་ན།

[Block 3068 [VERSE]]
འཇིག་རྟེན་པ་ཡིས་ཐོབ་འབྲས་ནི། །
བསྲེས་དང་ཟག་མེད་ཐོབ་འཛིན་ཕྱིར། །

[Block 3069]
དེ་ལ་ནི་ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་འམ་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་འཇིག་རྟེན་པའི་ལམ་གྱིས་འབྲས་བུ་སྤངས་པ་ཁོ་ན་ཡང་མ་ཡིན་ནོ། །

[Block 3070]
འོ་ན་ཅི་ཞེ་ན། མཐོང་བའི་ལམ་གྱིས་འབྲས་བུ་སྤངས་པ་ཡང་དེར་བསྲེ་བར་བྱ་སྟེ། ཐམས་ཅད་ཀྱི་ཐོབ་པ་དེའི་འབྲས་བུར་བསྡུས་པ༌[^2124]ཅིག་རྙེད་པའི་ཕྱིར་རོ། །

[Block 3071]
དེ་ཉིད་ཀྱི་ཕྱིར་མདོ་ལས།

[Block 3072]
ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་གང་ཞེ་ན། ཀུན་དུ་སྦྱོར་བ་གསུམ་སྤངས་པ་དང་། འདོད་ཆགས་དང་ཞེ་སྡང་དང་གཏི་མུག་རྣམས་བསྲབས་པ་གང་ཡིན་པ་དེ་ཡིན་ན། །[^2125]ཕྱིར་མི་འོང་བའི་འབྲས་བུ་གང་ཞེ་ན། ཀུན་དུ་སྦྱོར་བ་ཐ་མའི་ཆ་དང་མཐུན་པ་ལྔ་སྤངས་པ་གང་ཡིན་པ་དེ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 3073]
དེའི་སྟོབས་ཀྱིས་ཡོངས་སུ་ཉམས་པ་མི་འཆི་བའི་ཕྱིར་བྲལ་བའི་ཐོབ་པ་ཟག་པ་མེད་པས་སྤངས་པ་དེ་འཛིན་པར་ཡང་བྱེད་དེ། [^2126]འདིའི་ཕྱིར་ཡང་འདི༌[^2127]དགེ་སྦྱོང་གི་འབྲས་བུ་ཉིད་དུ་རིགས་སོ། །

[Block 3074 [HEADING]]
##### ཚངས་པའི་ཚུལ་དང་ཚངས་པའི་འཁོར་ལོ། ^3-2-11-5-0

[Block 3075]
དགེ་སྦྱོང་གི་ཚུལ་དུ་བཤད་པ་གང་ཡིན་པ། དེ་ཉིད་ཚངས་ཚུལ་ཚངས་པ་ཡི། །འཁོར་ལོ། །

[Block 3076]
ཉོན་མོངས་པ་རྣམས་སྤོང་བའི་ཕྱིར་ཚངས་པའི་ཚུལ་ལོ། །

[Block 3077]
ཚངས་པའི་འཁོར་ལོ་ནི། ཚངས་པས་བསྐོར་ཕྱིར་རོ། །

[Block 3078]
བཅོམ་ལྡན་འདས་ནི་ཚངས་པའི་ཚུལ་བླ་ན་མེད་པ་དང་ལྡན་པའི་ཕྱིར་ཚངས་པ་ཡིན་ཏེ།

[Block 3079]
མདོ་ལས།

[Block 3080]
བཅོམ་ལྡན་འདས་དེ་ནི་ཚངས་པ་ཞེས་ཀྱང་བྱ། ཞི་བ་དང་བསིལ་བར་གྱུར་པ་ཞེས་ཀྱང་བྱ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3081]
འཁོར་ལོ་འདི་ནི་དེའི་ཡིན་པས་ན་ཚངས་པའི་འཁོར་ལོ༌[^2128]སྟེ། དེས་བསྐོར་བའི་ཕྱིར་རོ། །

[Block 3082 [HEADING]]
##### ཆོས་ཀྱི་འཁོར་ལོ། ^3-2-11-6-0

[Block 3083]
ཆོས་ཀྱི་འཁོར་ལོ་མཐོང་བའི་ལམ། རྒྱུ་བས་ན་འཁོར་ལོའོ། །

[Block 3084]
དེ་དང་ཆོས་མཐུན་པའི་ཕྱིར་མཐོང་བའི་ལམ་ནི་ཆོས་ཀྱི་འཁོར་ལོ་ཡིན་ནོ། །

[Block 3085]
འདིའི་ཆོས་མཐུན་པ་ཇི་ལྟ་བུ་ཞེ་ན། མྱུར་བར་འགྲོ་སོགས་རྩིབས་སོགས་ཀྱིས། མྱུར་དུ་འགྲོ་བའི་ཕྱིར་དང་། འདོར་བ་དང་འཇུག་པའི་ཕྱིར་དང་། མ་རྒྱལ་བ་རྒྱལ་བར་བྱེད་པ་དང་རྒྱལ་བ་རྣལ་དུ་དགོད་པའི༌[^2129]ཕྱིར་དང་། འཕར་བ་དང་འབབ་པའི་ཕྱིར་ཏེ། མྱུར་བར་འགྲོ་བ་ལ་སོགས་པ༌[^2130]ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །
--- END BLOCKS ---
