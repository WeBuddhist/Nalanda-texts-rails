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
[Block 3081 [VERSE]]
གཉེན་པོ་སྐྱེ༌[^1217]དང་འབྲས༌[^1218]ཐོབ་དང་། །
དབང་པོ་རྣམ་པར་འཕེལ་རྣམས་སུ། །

[Block 3082]
གཉེན་པོ་ནི་རྣམ་པར་གྲོལ་བའི་ལམ་མོ། །

[Block 3083 [VERSE]]
འབྲས་བུ་དག་ནི་དགེ་སྦྱོང་གི་འབྲས་བུ་དག་གོ། །
དབང་པོ་རྣམ་པར་འཕེལ་བ་ནི་དབང་པོ་འཕོ་བའོ། །
དུས་དེ་དག་ཏུ་ཉོན་མོངས་པ་བྲལ་བ་ཐོབ་པོ། །

[Block 3084]
བྲལ་བ་དེ་ཡང་ནི་གནས་སྐབས་དེ་དང་དེ་དག་ཏུ་ཡོངས་སུ་ཤེས་པ་ཞེས་བྱ་བའི་མིང་འཐོབ་བོ། །

[Block 3085 [HEADING]]
### ཡོངས་སུ་ཤེས་པ་དགུ། ^5-18-0

[Block 3086]
དེ་དག་ཀྱང་། ཡོངས་སུ་ཤེས་དགུ། དེ་ལ་རེ་ཞིག་འདོད་པ་ན།

[Block 3087]
དང་པོ་རྣམ་གཉིས་ཟད༌[^1219]ལ་གཅིག །འདོད་པའི་ཁམས་ན་དང་པོའི་རྣམ་པ་གཉིས་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བ་སྤངས་པ་ནི་ཡོངས་སུ་ཤེས་པར་བྱ་བ་གཅིག་གོ། །

[Block 3088]
གཉིས་ཟད་པ་ནི་དེ་གཉིས་སོ། །

[Block 3089]
འདོད་པའི་ཁམས་ཁོ་ན་ན༌[^1220]འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བའི་རྣམ་པ་སྤངས་པ་ནི་ཡོངས་སུ་ཤེས་པ་གཉིས་སོ། །

[Block 3090]
ཇི་ལྟར་འདོད་པ་ན་སྤྱོད་པ་ཇི་ལྟ་བ་བཞིན་དུ། དེ་བཞིན་གོང་མ་དེ་གསུམ་ཉིད། །དེ་ལྟར་ན་ཁམས་གསུམ་པའི་མཐོང་བས་སྤང་བར་བྱ་བ་སྤངས་པ་ནི་ཡོངས་སུ་ཤེས་པ་དྲུག་ཡིན་ནོ། །

[Block 3091 [VERSE]]
ཡོངས་སུ་ཤེས་པ༌[^1221]གཞན་གསུམ་སྟེ། །
ཐ་མའི་ཆ་དང་མཐུན་གཟུགས་དང་། །

[Block 3092]
ཟག་པ་ཀུན་ཟད། འདོད་པའི་ཟག་པ་སྤོང་བའི་ཡོངས་སུ་ཤེས་པ་དང་། གཟུགས་ཀྱི་ཟག་པ་སྤོང་བའི་ཡོངས་སུ་ཤེས་པ་དང་། ཟག་པ་ཐམས་ཅད་སྤོང་བའི་ཡོངས་སུ་ཤེས་པ་འདི་དག་བསྒོམ་པས་སྤང་བར་བྱ་བ་སྤངས་པའི་ཡོངས་སུ་ཤེས་པ་གསུམ་སྟེ། སྔར་གྱི་དྲུག་དང་དགུར་འགྱུར་རོ། །

[Block 3093]
དེ་དག་ལས་ཀྱང་། དྲུག་བཟོད་འབྲས། སྔ་མ་དག་གོ། །

[Block 3094]
ལྷག་མ་དག་ནི་ཤེས་པ་ཡིན། །ཕྱི་མ་གསུམ་མོ། །

[Block 3095 [VERSE]]
མི་ལྕོགས་མེད་འབྲས་ཐམས་ཅད་དོ། །
བསམ་གཏན་རྣམས་ཀྱི་ལྔ་འམ་བརྒྱད། །

[Block 3096]
བྱེ་བྲག་ཏུ་སྨྲ་བའི་ལུགས་ཀྱིས་ནི་བསམ་གཏན་གྱི་འབྲས་བུ་ཡོངས་སུ་ཤེས་པ་ལྔ་སྟེ། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་སྤངས་པའི་རང་བཞིན་ནོ། །

[Block 3097]
བཙུན་པ་དབྱངས་སྒྲོགས་ཀྱི་ལུགས་ཀྱིས་བརྒྱད་དེ། དེ་ནི༌[^1222]འདོད་ཆགས་དང་བྲལ་བས་འདོད་པ་ན་སྤྱོད་པའི་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ཡང་བྲལ་བའི་ཐོབ་པ་ཟག་པ་མེད་པ་རྙེད་པའི་ཕྱིར། མཐོང་བའི་ལམ་གྱི་འབྲས་བུར་འདོད་དོ། །

[Block 3098]
ཐ་མའི་ཆ་དང་མཐུན་པ་སྤངས་པའི་ཡོངས་སུ་ཤེས་པ་ནི་མི་ལྕོགས་པ་མེད་པའི་འབྲས་བུ་ཁོ་ན་ཡིན་ནོ། །

[Block 3099]
བསམ་གཏན་ཁྱད་པར་ཅན་ཡང་བསམ་གཏན་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 3100]
གཟུགས་མེད་པ་རྣམས་ཀྱི་ནི། ཉེ་བར་བསྡོགས་པའི་གཅིག་ཡིན་ཏེ། །གཟུགས་ཀྱི་འདོད་ཆགས་ཟད་པའི་ཡོངས་སུ་ཤེས་པའོ། །

[Block 3101]
གཟུགས་མེད་དངོས་གཞི་གསུམ་གྱི་ཡང་། །གཅིག་ཁོ་ན་སྟེ། ཀུན་དུ་སྦྱོར་བ་ཐམས་ཅད་ཡོངས་སུ་གཏུགས་པའི་ཡོངས་སུ་ཤེས་པའང་འབྲས་བུའོ། །

[Block 3102]
ཐམས་ཅད་འཕགས་པའི་ལམ་གྱི་ཡིན། །འཇིག་རྟེན་པའི། འབྲས་བུ་ནི་ཐ་མའི་ཆ་དང་མཐུན་པ་དང་། གཟུགས་ཀྱི་འདོད་ཆགས་ཟད་པའི་ཡོངས་སུ་ཤེས་པ་དག་གོ། །

[Block 3103]
གཉིས་རྗེས་ཀྱི་འང་། [^1223]རྗེས་སུ་ཤེས་པའི་འབྲས་བུ་ཡང་ཡོངས་སུ་ཤེས་པ་གཉིས་ཏེ། ཐ་མ་དག་གོ། །

[Block 3104]
ཆོས་ཤེས་པའི་ནི་གསུམ་ཡིན་ནོ། །

[Block 3105]
ཐ་མ་དག་ཁོ་ནའོ། །

[Block 3106]
དེའི་ཕྱོགས་མཐུན་གྱི་དྲུག་དང་ལྔ། ཆོས་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པའི་འབྲས་བུ་ནི་ཡོངས་སུ་ཤེས་པ་དྲུག་སྟེ། ཆོས་ཀྱི་བཟོད་པ་དང་ཤེས་པ་རྣམས་ཀྱི་འབྲས་བུ་གང་དག་ཡིན་པ་ཁོ་ནའོ། །

[Block 3107]
རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པ་ནི་ལྔ་སྟེ། རྗེས་ཀྱི་བཟོད་པ་དང་ཤེས་པ་རྣམས་ཀྱི་འབྲས་བུ་གང་དག་ཡིན་པ་ཁོ་ནའོ། །

[Block 3108]
ཅིའི་ཕྱིར་སྤངས་པ་རེ་རེ་ཡོངས་སུ་ཤེས་པར་རྣམ་པར་མི་གཞག་ཅེ་ན། འདི་ལྟར་རེ་ཞིག་བཟོད་པའི་འབྲས་བུ་བྲལ་བ་ནི།

[Block 3109 [VERSE]]
བྲལ་བའི་ཐོབ་པ་ཟག་མེད་དང་། །
སྲིད་རྩེ་ཉམས་པར་བྱེད་པ་དང་། །
རྒྱུ་གཉིས་ཀུན་དུ་བཅོམ་པའི་ཕྱིར། །

[Block 3110]
ཡོངས་ཤེས། སུ་རྣམ་པར་གཞག་གོ། །

[Block 3111]
རེ་ཞིག་སོ་སོའི་སྐྱེ་བོ་ལ་ནི་བྲལ་བའི་ཐོབ་པ་ཟག་པ་མེད་པ་དང་། སྲིད་པའི་རྩེ་མོ་ཉམས་པར་བྱེད་པ་མེད་དོ། །

[Block 3112]
འཕགས་པ་ལ་ཡང་། ཇི་སྲིད་དུ་སྡུག་བསྔལ་ལ༌[^1224]རྗེས་སུ་ཤེས་པའི་བཟོད་པ་ལ་གནས་པ་དེ་སྲིད་དུ་བྲལ་བའི་ཐོབ་པ་ཟག་པ་མེད་པ་ཡོད་ལ། སྲིད་པའི་རྩེ་མོ་ཉམས་པར་བྱས་པ་མེད་དོ། །

[Block 3113]
སྡུག་བསྔལ་ལ་རྗེས་སུ་ཤེས་པ་ལ་གཉིས་ཀ་ཡོད་དོ། །

[Block 3114]
རྒྱུ་གཉིས་ཀུན་དུ་བཅོམ་པ་ནི་མ་ཡིན་ཏེ། ཆོས་དང་རྗེས་སུ་ཤེས་པ་གཞན་ལ་གསུམ་པོ་ཐམས་ཅད་ཡོད་པས་དེའི་ཕྱིར་གནས་སྐབས་དེ་དང་དེ་དག་ཏུ་སྤངས་པའི་ཡོངས་སུ་ཤེས་པའི་མིང་འཐོབ་པོ།[^1225] །ཤེས་པའི་འབྲས་བུ་ནི་སྤངས་པ་སྟེ། རྒྱུ་གསུམ་པོ་དེ་དང་བཞི་པ།

[Block 3115]
ཁམས་ལས་འདས་པ་ལས།

[Block 3116]
གང་གི་ཚེ་ཁམས་ལས་ཡང་དག་པར་འདས་པ་དེའི་ཚེ་ཡོངས་སུ་ཤེས་པའི་མིང་འཐོབ་པོ། །

[Block 3117 [HEADING]]
#### ཡོངས་སུ་ཤེས་པ་དུ་མ་དང་ལྡན་པ། ^5-18-1-0

[Block 3118]
གང་ཞིག་ཡོངས་སུ་ཤེས་པ་དུ་མ༌[^1226]དང་ལྡན་ཞེ་ན།

[Block 3119 [VERSE]]
གཅིག་མིན་མཐོང་ལ་གནས་པ་ནི། །
ལྔ་ཡི་བར་དང་ཡང་དག་ལྡན། །

[Block 3120]
རེ་ཞིག་སོ་སོའི་སྐྱེ་བོ་ནི་མི་ལྡན་པ་ཁོ་ནའོ། །
--- END BLOCKS ---
