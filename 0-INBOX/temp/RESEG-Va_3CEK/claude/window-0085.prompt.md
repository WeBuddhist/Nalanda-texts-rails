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
[Block 2976]
ནམ་མཁའ་དང་རྣམ་ཤེས་མཐའ་ཡས་དང་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ཀྱིས༌[^2054]བསྡུས་པ་རྣམས་ནི་གྲངས་བཞིན་དུ་ཉི་ཤུ་རྩ་བརྒྱད་དང་ཉི་ཤུ་རྩ་བཞི་དང་ཉི་ཤུ་ཡིན་ཏེ། དེ་དག་ནི༌[^2055]ཆོས་ཤེས་པ་དང་རྗེས་སུ་ཤེས་པས་ས༌[^2056]འོག་མའི་འགོག་པ་ལ་དམིགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2977]
ས་འོག་མིའི༌[^2057]གཉེན་པོ་ལ་དམིགས་པ་ནི་ཡོད་དེ།[^2058] དེ་ནི་ཕན་ཚུན་དུ་རྒྱུ་བའི་ཕྱིར་རོ། །

[Block 2978]
གང་དག་ལམ་ལ་རྗེས་སུ་ཤེས་པ་ཡང་ས་རེ་རེའི་གཉེན་པོ་ལ་དམིགས་པ་ཡིན་པར་འདོད་པ་དེ་དག་གི་ལྟར་ན་ཉི་ཤུ་རྩ་བརྒྱད་ལྷག་པར་བསྣན་ནས་མི་ལྕོགས་པ་མེད་པས་བསྡུས་པ་རྡོ་རྗེ་ལྟ་བུ་ནི་བརྒྱད་ཅུ་ཡིན་ཏེ། བསམ་གཏན་བཞི་པས་བསྡུས་པའི་བར་དུ་ཡང་དེ་དང་འདྲའོ། །

[Block 2979]
ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ་སོགས་པ་དག་ནི་གོ་རིམས་བཞིན་དུ་བཞི་བཅུ་དང་། སུམ་ཅུ་རྩ་གཉིས་དང་། ཉི་ཤུ་རྩ་བཞི་ཡིན་ནོ། །

[Block 2980]
ཡང་རིགས་དང་དབང་པོའི་བྱེ་བྲག་གིས་ནི་ཆེས་མང་བ་ཡིན་ནོ། །

[Block 2981 [HEADING]]
##### མི་སློབ་པ་དགྲ་བཅོམ་པ། ^3-2-8-10-0

[Block 2982]
གང་སྲིད་པའི་རྩེ་མོའི༌[^2059]རྣམ་པ་དགུ་པར༌[^2060]བཤད་པ་རྡོ་རྗེ་ལྟ་བུས་སྤངས་པ་གང་ཡིན་པ། དེ་ཟད་ཐོབ་དང་ཟད་པ་ཤེས། །རྣམ་པ་དགུ་པ་དེ་ཟད་པའི་ཐོབ་པ་དང་ལྷན་ཅིག་ཏུ་ཟད་པ་ཤེས་པ་སྐྱེ་སྟེ། རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི༌[^2061]མཇུག་ཐོགས་སུ་རྣམ་པར་གྲོལ་བའི་ལམ་ཐ་མ་སྐྱེ་བ་ཡིན་ནོ། །

[Block 2983]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་ནི་དང་པོ་ཉིད་དུ་ཟག་པ་ཐམས་ཅད་ཟད་པའི་ཐོབ་པ་དང་ལྷན་ཅིག་སྐྱེ་བའི་ཕྱིར་ཟད་པ་ཤེས་པ་ཡིན་ནོ། །

[Block 2984]
དེ་ཚེ་དེ་མི་སློབ་དགྲ་བཅོམ། །ཡང་དགྲ་བཅོམ་པ་ཉིད་ལ་ཞུགས་པ་དེ་ཟད་པ་ཤེས་པ་སྐྱེ༌[^2062]ནས་མི་སློབ་པ་དང་དགྲ་བཅོམ་པ་ཉིད་ཀྱི༌[^2063]འབྲས་བུ་ཐོབ་པ་ཡིན་ཏེ། འབྲས་བུ་གཞན་གྱི་ཕྱིར་སློབ་པར་བྱ་བ་མེད་པའི་ཕྱིར་མི་སློབ་པ་ཡིན་ནོ། །

[Block 2985]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་ནི་གཞན་གྱི་དོན་བྱེད་པར་འོས་པའི་ཕྱིར་དང་། འདོད་ཆགས་དང་བཅས་པ་ཐམས་ཅད་ཀྱིས་མཆོད་པར་འོས་པའི་ཕྱིར་དགྲ་བཅོམ་པ་ཡིན་ནོ། །

[Block 2986 [HEADING]]
##### སློབ་པ། ^3-2-8-11-0

[Block 2987]
གང་ཟག་སྔར་བཤད་པ་གཞན་བདུན་ནི་སློབ་པ་དག་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པོ། །ཅིའི་ཕྱིར་དེ་དག་སློབ་པ་ཡིན་ཞེ་ན། ཟག་པ་ཟད་པར་བྱ་བའི་ཕྱིར་བསླབ་པ༌[^2064]གསུམ་པོ་ལྷག་པའི་ཚུལ་ཁྲིམས་དང་ལྷག་པའི་སེམས་དང་ལྷག་པའི་ཤེས་རབ་ལ་རྟག་ཏུ་སློབ་པའི་ངང་ཚུལ་ཅན་ཡིན་པའི་ཕྱིར་ཏོ། །

[Block 2988]
[^2065]དེ་དག་ནི་ཚུལ་ཁྲིམས་དང་ཏིང་ངེ་འཛིན་དང་ཤེས་རབ་ཀྱི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 2989]
སོ་སོའི་སྐྱེ་བོ་ཡང་སློབ་པ་ཡིན་པར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། བདེན་པ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་མི་ཤེས་པའི་ཕྱིར་དང་། ཡང་སློབ་པ་གཏོང༌[^2066]བའི་ཕྱིར་རོ། །

[Block 2990]
དེ་ཉིད་ཀྱི་ཕྱིར་ཅི་ནས་ཀྱང་གང་ཞིག་སློབ་པ་དེ༌[^2067]ཁོ་ན་སློབ་པ་ཡིན་གྱི་སློབ་པ་འདོར་བ་ནི་མ་ཡིན་ནོ་ཞེས་དམིགས་ཀྱིས་བསལ་བ་ཤེས་པར་བྱ་བའི་ཕྱིར་མདོ་ལས།

[Block 2991]
ཞི་བྱེད་བསླབ་པ་ལ་སློབ་ཅིང་། །བསླབ་པ་ལ་སློབ༌[^2068]པས་ནི༌[^2069]དེའི་ཕྱིར་སློབ་པ་ཞེས་བྱའོ་ཞེས་ལན་གཉིས་སུ་གསུངས་སོ། །

[Block 2992]
འཕགས་པ་རང་བཞིན་དུ་གནས་པ་ཇི་ལྟར༌[^2070]སློབ་པའི་ངང་ཚུལ་ཅན་ཡིན་ཞེ་ན། བསམ་པའི་སྒོ་ནས་ཏེ། ལམ་དུ་འགྲོ་བ་གནས་པ་བཞིན་ནོ། །

[Block 2993]
ཐོབ་པ་དང་རྗེས་སུ་འབྲེལ་བའི་ཡང་ཕྱིར་རོ། །

[Block 2994]
ཡང་སློབ་པའི་ཆོས་རྣམས་གང་ཞེ་ན། སློབ་པའི་ཟག་པ་མེད་པ་རྣམས་སོ། །

[Block 2995]
མི་སློབ་པ་རྣམས་གང་ཞེ་ན། མི་སློབ་པའི་ཟག་པ་མེད་པ་རྣམས་སོ། །ཅིའི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་སློབ་པ་མ་ཡིན་ཞེ་ན། མི་སློབ་པ་དང་སོ་སོའི་སྐྱེ་བོ་གཉི་ག་ཡང་དེ་དང་ལྡན་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་མི་སློབ་པ་མ་ཡིན་ཞེ་ན། སློབ་པ་དང་སོ་སོའི་སྐྱེ་བོ་གཉི་ག་ཡང་དེ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2996 [HEADING]]
##### ཞུགས་པ་བཞི་དང་འབྲས་བུ་ལ་གནས་པ་བཞི། ^3-2-8-12-0

[Block 2997]
དེ་དག་ཐམས་ཅད་ནི་ཞུགས་པ་བཞི་དང་འབྲས་བུ་ལ་གནས་པ་བཞི་དང་། འཕགས་པའི་གང་ཟག་བརྒྱད་ཁོ་ན་ཡིན་ཏེ། འདི་ལྟ་སྟེ་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་མངོན་སུམ་དུ་བྱ་བའི་ཕྱིར་ཞུགས་པ་དང་། རྒྱུན་དུ་ཞུགས་པ་ནས་དེ་བཞིན་དུ་དགྲ་བཅོམ་པ་ཉིད་ཀྱི་འབྲས་བུ་མངོན་སུམ་དུ་བྱ་བའི་ཕྱིར་ཞུགས་པ་དང་། དགྲ་བཅོམ་པའི་བར་ཡིན་ནོ། །

[Block 2998]
མིང་གི་སྒོ་ནས་ནི་བརྒྱད་ཡིན་ནོ། །

[Block 2999]
རྫས་སུ་ནི་ལྔ་ཡིན་ཏེ། ཞུགས་པ་དང་པོ་དང་འབྲས་བུ་ལ་གནས་པ་བཞིའོ། །

[Block 3000]
ཞུགས་པ་ལྷག་མ་རྣམས་ནི་འབྲས་བུ་ལ་གནས་པ་གསུམ་ལས་ཐ་མི་དད་པའི་ཕྱིར་རོ། །

[Block 3001]
མཐར་གྱིས་འཐོབ་པའི་ཕྱིར་དེ༌[^2071]སྐད་ཅེས་བཤད་ཀྱི། ཕལ་ཆེར་དང་འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་དག་ཅིག་ཡིན་ན་ནི་མཐོང་བའི་ལམ་ལ་ལན་ཅིག་ཕྱིར་འོང་བ་དང་། ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ལ་ཞུགས་པ་དག་ཡིན་གྱི། རྒྱུན་དུ་ཞུགས་པ་དང་། ལན་ཅིག་ཕྱིར་འོང་བ་དག་ནི༌[^2072]མ་ཡིན་ནོ། །

[Block 3002 [HEADING]]
#### གང་གིས་གང་ལས་འདོད་ཆགས་དང་བྲལ་བ་འཐོབ་པ། ^3-2-9-0

[Block 3003]
བསྒོམ་པའི་ལམ་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པ་རྣམ་པ་གཉིས་སུ་བཤད་པ་ལ། སློབ་པ་འདི་གང་གིས་གང་ལས་འདོད་ཆགས་དང་བྲལ་བ་འཐོབ་ཅེ་ན། འཇིག་རྟེན་འདས་ཀྱིས་སྲིད་རྩེ་ལས། །

[Block 3004]
ཆགས་བྲལ་འཇིག་རྟེན་པས་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེའི་གོང་ན་འཇིག་རྟེན་པ་མེད་པའི་ཕྱིར་དང་། རང་གི་ས་པའི་གཉེན་པོ་མ་ཡིན་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་གཉེན་པོ་མ་ཡིན་ཞེ་ན། དེའི་ཉོན་མོངས་པ་རྒྱས་པར་འགྱུར་བའི་ཕྱིར་ཏེ། ཉོན་མོངས་པ་གང་ཞིག་དངོས་པོ་གང་ལ་རྒྱས་པར་འགྱུར་བ་དེ་ནི་དངོས་པོ་དེས་སྤོང་བར་བྱེད་པ་མ་ཡིན་ལ། གང་གི་གཉེན་པོ་གང་ཡིན་པ་དེ་ལ་ནི་ཉོན་མོངས་པ་དེ་རྒྱས་པར་ཡང་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 3005]
གཞན་ལས་རྣམ་པ་གཉིས། །སྲིད་པའི་རྩེ་མོ་ལས་གཞན་པའི་ས་ཐམས་ཅད་ལས་ནི༌[^2073]འཇིག་རྟེན་པའི་ལམ་གྱིས་ཀྱང་འདོད་ཆགས་དང་བྲལ་ལ། འཇིག་རྟེན་ལས་འདས་པས་ཀྱང་འདོད་ཆགས་དང་བྲལ་ལོ། །

[Block 3006 [HEADING]]
##### བྲལ་བའི་ཐོབ་པ་རྣམ་པ་གཉིས། ^3-2-9-1-0

[Block 3007 [VERSE]]
འཇིག་རྟེན་པ་ཡིས་ཆགས་བྲལ་བའི། །
འཕགས་ལ་བྲལ་བའི་ཐོབ་རྣམ་གཉིས། །

[Block 3008]
འཕགས་པ་འཇིག་རྟེན་པའི་ལམ་གྱིས་འདོད་ཆགས་དང་བྲལ་བར་གྱུར་པ་ལ་བྲལ་བའི་ཐོབ་པ་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པ་དང་རྣམ་པ་གཉིས་སྐྱེའོ། །

[Block 3009]
ཁ་ཅིག་འཇིག་རྟེན་འདས་ཀྱིས་ཀྱང་། །གཞན་དག་ན་རེ་འཇིག་རྟེན་ལས་འདས་པས་ཀྱང་དེ་དང་འདྲའོ་ཞེས་ཟེར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། བཏང་ལ་ཉོན་མོངས་མི་ལྡན་ཕྱིར། །གལ་ཏེ་འཕགས་པའི་ལམ་གྱིས་འདོད་ཆགས་དང་བྲལ་བ་འཐོབ་པ་ལ་འཇིག་རྟེན་པའི་བྲལ་བའི་ཐོབ་པ་མི་སྐྱེ༌[^2074]ན། དེ་ལྟ་ན་འཕགས་པའི་ལམ་གྱིས་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ལས་འདོད་ཆགས་དང༌[^2075]བྲལ་བ་བསམ་གཏན་ལ་བརྟེན་ཏེ་དབང་པོ་རྣམས་འཕོ་བར་བྱེད་པ་གང་ཡིན་པ་དེ་ལམ་སྔ་མ་ཟད་པར་བཏང་པའི་ཕྱིར་དང་། འབྲས་བུའི་ལམ་འབའ་ཞིག་ཐོབ་པའི་ཕྱིར་ས་གོང་མ་པའི༌[^2076]ཉོན་མོངས་པའི་བྲལ་བ་དང་མི་ལྡན་པར་ཡང་འགྱུར་ལ། དེ་བཏང་ན་ཡང་ཉོན་མོངས་པ་དེ་དག་དང་ལྡན་པར་ཡང་འགྱུར་རོ། །

[Block 3010 [VERSE]]
སྲིད་རྩེའི་ཕྱེད་ལས་རྣམ་གྲོལ་དང་། །
གོང་དུ་སྐྱེས་པ་བཞིན་མི་ལྡན། །

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
--- END BLOCKS ---
