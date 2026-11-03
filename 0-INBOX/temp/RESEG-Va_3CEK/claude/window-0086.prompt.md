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
[Block 3011]
དེ་ལ་འཇིག་རྟེན་པའི་བྲལ་བའི༌[^2077]ཐོབ་པ་མེད་དུ་ཟིན་ཀྱང་དེ་དག་དང་ལྡན་པར་མི་འགྱུར་ཏེ། དཔེར་ན་སྲིད་པའི་རྩེ་མོའི་རྣམ་པ་ཕྱེད༌[^2078]ལ་རྣམ་པར་གྲོལ་བ་ལ་དེའི་བྲལ་བའི་འཐོབ་པ༌[^2079]འཇིག་རྟེན་པ་ཡང་མེད་ལ། དབང་པོ་འཕོ་བས་འཇིག་རྟེན་ལས༌[^2080]འདས་པ་ཡང༌[^2081]བཏང་བཞིན་དུ་ཉོན་མོངས་པ་དེ་དག་དང༌[^2082]ལྡན་པར་མི་འགྱུར་བ་དང་། ཡང་དཔེར་ན་སོ་སོའི་སྐྱེ་བོ་བསམ་གཏན་དང་པོ༌[^2083]ཡན་ཆད་དུ་སྐྱེས་པ༌[^2084]འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པའི་བྲལ་བའི་ཐོབ་པ་བཏང་བས་ཡང་དེ་དག་དང༌[^2085]ལྡན་པར་མི་འགྱུར་བ་བཞིན་པས་འདི་ནི་ཤེས་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 3012 [HEADING]]
##### ས་གང་གིས་གང་ལས་འདོད་ཆགས་དང་བྲལ་བ། ^3-2-9-2-0

[Block 3013]
ས་གང་ཞིག་གིས་གང་ལས་འདོད་ཆགས་དང་བྲལ་བར་འགྱུར་ཞེ་ན། ཟག་མེད་མི་ལྕོགས་མེད་པ་ཡིས།[^2086] །ཐམས་ཅད་ལས༌[^2087]ནི་འདོད་ཆགས་བྲལ།[^2088] །སྲིད་པའི་རྩེ་མོའི་བར་ལས་སོ། །

[Block 3014 [HEADING]]
##### རྣམ་པར་གྲོལ་བའི་ལམ་ཐ་མ། ^3-2-9-3-0

[Block 3015]
ཡང་གང་ཞིག་ཉེར་བསྡོགས་ལ་བརྟེན་ཏེ་ས་འོག་མ་ལས་འདོད་ཆགས་དང་བྲལ་བ་འཐོབ་ན། ཅིའི་ཕྱིར༌[^2089]རྣམ་པར་གྲོལ་བའི་ལམ་ཐམས་ཅད་བར་ཆད་མེད་པའི་ལམ་བཞིན་དུ་ཉེར་བསྡོགས་ལས་སྐྱེའམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 3016]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 3017 [VERSE]]
ས་གསུམ་རྒྱལ་ལ་བསམ་གཏན་ནམ། །
ཉེར་བསྡོགས་ལས་མཐའི༌[^2090]རྣམ་གྲོལ་ལམ། །

[Block 3018]
སྐྱེ་བའི་ས་ནི་ཐམས་ཅད་དུ་དགུ་སྟེ། འདོད་པའི་ཁམས་དང་བསམ་གཏན་དང་གཟུགས་མེད་པ་བརྒྱད་དོ། །

[Block 3019]
དེ་ལ་བསམ་གཏན་གཉིས་ཀྱི་བར་ལས་འདོད་ཆགས་དང་བྲལ་བ་ས་གསུམ་ལས་རྒྱལ་བ་དེ་ལ་ནི་རྣམ་པར་གྲོལ་བའི་ལམ་ཐ་མ་ཉེར་བསྡོགས་སམ་བསམ་གཏན་དངོས་གཞི་ལས་སྐྱེའོ། །

[Block 3020]
གོང་མའི་ཉེ་བར༌[^2091]བསྡོགས་ལས་མིན། །ས་གསུམ་ལས་རྒྱལ་བ་ཡན་ཆད་ནི་བཏང་སྙོམས་ཀྱི་དབང་པོ་ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་དངོས་གཞི་ཁོ་ན་ལས་སྐྱེའི་ཉེར་བསྡོགས་ལས་ནི་མ་ཡིན་ནོ། །

[Block 3021]
བསམ་གཏན་གསུམ་ན་ནི་ཉེར་བསྡོགས་དང་དངོས་གཞི་གཉིས་ཀྱི་དབང་པོ་ཐ་དད་པའི་ཕྱིར་ལ་ལ༌[^2092]བསམ་གཏན་དང༌[^2093]དངོས་གཞི་ལ་འཇུག་མི་ནུས་ཏེ། དབང་པོའི་འཕོ་བ་ནི་དཀའ་བའི་ཕྱིར་རོ། །

[Block 3022]
དེ་ལྟ་བས་ན་ས་གསུམ་ལས་འདོད་ཆགས་དང་བྲལ་བ་ལ་ནི༌[^2094]རྣམ་པར་གྲོལ་བའི་ལམ་ཐ་མ་ཉེར་བསྡོགས་ལས་ཀྱང༌[^2095]སྐྱེའོ། །

[Block 3023]
ཟག་མེད་མི་ལྕོགས༌[^2096]མེད་པ་ཡིས། །ཐམས་ཅད་ལས་ནི་འདོད་ཆགས་བྲལ།[^2097] །ཞེས་བཤད་ཀྱི་གཞན་དག་གིས་ནི་མ་བཤད་པས་དེའི་ཕྱིར། འཕགས། བརྒྱད་ཀྱིས་རང་གོང་ས་ལས་རྒྱལ། །ཞེས་བྱ་བ་སྨོས་ཏེ། ཟག་པ༌[^2098]མེད་པའི་བསམ་གཏན་དང་བསམ་གཏན་ཁྱད་པར་ཅན་དང་གཟུགས་མེད་པ༌[^2099]བརྒྱད་ཀྱིས་ནི་རང་གི་ས་དང་ས་གོང༌[^2100]མ་ལས་འདོད་ཆགས་དང་བྲལ་བར་འགྱུར་རོ། །

[Block 3024]
འོག་མ་ལས་ནི་མ་ཡིན་ཏེ། འདོད་ཆགས་དང་བྲལ་ཟིན་པའི་ཕྱིར་རོ། །

[Block 3025]
དེ་ལ་འཇིག་རྟེན་ལས་འདས་པའི་བར་ཆད་མེད་པ་དང་རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་ནི་བདེན་པ་ལ་དམིགས་པའི་ཕྱིར་བདེན༌[^2101]པའི་རྣམ་པར་ཞུགས་པ་དག་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པོ། །

[Block 3026 [HEADING]]
##### འཇིག་རྟེན་པའི་རྣམ་གྲོལ་དང་བར་ཆད་མེད་པའི་ལམ་གྱི་རྣམ་པ། ^3-2-9-4-0

[Block 3027 [VERSE]]
འཇིག་རྟེན་པ་ཡི་རྣམ་གྲོལ་དང་། །
བར་ཆད་མེད་ལམ་གོ་རིམས་བཞིན། །
ཞི་སོགས་རགས༌[^2102]སོགས་རྣམ་པ་ཅན། །

[Block 3028]
རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་ནི་ཞི་བ་ལ་སོགས་པའི་རྣམ་པ་ཅན་དག་ཡིན་ལ། བར་ཆད་མེད་པའི་ལམ་རྣམས་ནི་རགས་པ་ལ་སོགས་པའི་རྣམ་པ་ཅན་དག་ཡིན་ནོ། །

[Block 3029]
དེ་དག་ཀྱང་གོ་རིམས་བཞིན་དུ། གོང་དང་འོག་མའི་སྤྱོད་ཡུལ་ཅན། །རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་ནི་ཅི་རིགས་པར་ས༌[^2103]གོང་མ་ལ་ཞི་བ་དང་། གྱ་ནོམ་པ་དང་། ངེས་པར་འབྱུང་བའི་རྣམ་པར་བལྟའོ། །

[Block 3030]
བར་ཆད་མེད་པའི་ལམ་རྣམས་ནི་ས་འོག་མ་ལ་རགས་པ་དང་། ཐ་མ༌[^2104]ངན་པ་དང་། རྩིག་པ་སྟུག་པོ་ལྟ་བུར་བལྟ་སྟེ། མངོན་པར་འདུ་བྱེད་པ་ཤིན་ཏུ་ཆེ་བ་ཉིད་ཀྱིས་མ་ཞི་བའི་ཕྱིར་རགས་པར་བལྟའོ། །

[Block 3031]
གྱ་ནོམ་པ་མ་ཡིན་པའི་ཕྱིར་ཐ་བ་ངན་པར་བལྟ་སྟེ། གནས་ངན་ལེན་རབ་ཏུ་མང་བ་ཉིད་ཀྱིས་མི་མཐུན་པར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3032]
རྩིག་པ་ལས་ངེས་པར་མི་འབྱུང་བ༌[^2105]བཞིན་དུ་དེ་ཉིད་ཀྱིས་ས་དེ་ལས་ངེས་པར་མི་འབྱུང་བའི་ཕྱིར༌[^2106]རྩིག་པ་སྟུག་པོ་ལྟ་བུར་བལྟའོ། །

[Block 3033]
དེ་དག་ལས་བཟློག་པ་ནི་ཞི་བ་དང་། གྱ་ནོམ་པ་དང་། ངེས་པར་འབྱུང་བའི་རྣམ་པ་ཅན་དག་ཡིན་ནོ། །

[Block 3034]
ཞར་ལ་འོངས་པ་རྫོགས་སོ།། །།

[Block 3035 [HEADING]]
#### ཟད་པ་ཤེས་པའི་མཇུག་ཐོགས་སུ་སྐྱེ་བ། ^3-2-10-0

[Block 3036]
དཀྱུས་མ་ཁོ་ན་བརྗོད་པར་བྱ་སྟེ། ཡང་ཟད་པ་ཤེས་པའི་མཇུག་ཐོགས་སུ་ཅི་ཞིག་སྐྱེ་ཞེ་ན། གལ་ཏེ་མི་གཡོ་ཟད་ཤེས་ལས། །

[Block 3037]
མི་སྐྱེའི་བློ་གྲོས། གལ་ཏེ་དགྲ་བཅོམ་པ་མི་གཡོ་བའི་ཆོས་ཅན་ཞིག་ཡིན་ན་དེ་ལ་ཟད་པ་ཤེས་པའི་དེ༌[^2107]མ་ཐག་ཏུ་མི་སྐྱེ་བའི་ཤེས་པ་སྐྱེའོ། །

[Block 3038]
གལ་ཏེ་མིན། ཟད་པ་ཤེས་སམ་མི་སློབ་ལྟ། གལ་ཏེ་མི་གཡོ་བའི་ཆོས་ཅན་མ་ཡིན་ན་ནི་ཟད་པ་ཤེས་པ་ལས་ཟད་པ་ཤེས་པ་ཁོ་ནའམ། མི་སློབ་པའི་ཡང་དག་པའི་ལྟ་བ་སྐྱེའོ། །

[Block 3039]
ཡོངས་སུ་ཉམས་པ་སྲིད་པའི་ཕྱིར་མི་སྐྱེ་བ་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 3040]
ཅི་མི་གཡོ་བའི་ཆོས་ཅན་ལ་དེ་མི་སྐྱེ་བ་ཁོ་ན་ཡིན་ནམ་ཞེ་ན། དེ་ནི་དགྲ་བཅོམ་ཐམས་ཅད་ལ། །མི་གཡོ་བའི་ཆོས་ཅན་ལ་ཡང་རེས་འགའ་མི་སྐྱེ་བ་ཤེས་པ་ལས་མི་སྐྱེ་བ་ཤེས་པ་ཁོ་ན་སྐྱེ་ལ། རེས་འགའ་ནི་མི་སློབ་པའི་ཡང་དག་པའི་ལྟ་བ་སྐྱེའོ། །

[Block 3041 [HEADING]]
#### དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ། ^3-2-11-0

[Block 3042]
གང་དག་འབྲས་བུ་བཞིར་བཤད་པ་དེ་དག་གང་གི་འབྲས་བུ་དག༌[^2108]ཡིན་ཞེ་ན་དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ༌[^2109]ཡིན་ནོ། །

[Block 3043 [HEADING]]
##### དགེ་སྦྱོང་གི་ཚུལ། ^3-2-11-1-0

[Block 3044]
དགེ་སྦྱོང་གི་ཚུལ་ཞེས་བྱ་བ་འདི་ཅི་ཞིག་ཅེ་ན། དགེ་སྦྱོང་ཚུལ་ནི་དྲི་མེད་ལམ། །དགེ་སྦྱོང་གི་ཚུལ་ནི་ཟག་པ་མེད་པའི་ལམ་ཡིན་ནོ། །

[Block 3045]
དེས་ཉོན་མོངས་པ་ཡང་དག་པར་ཞི་བར་བྱེད་པའི་སྒོ་ནས་དགེ་སྦྱོང་དུ་འགྱུར་ཏེ།

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
--- END BLOCKS ---
