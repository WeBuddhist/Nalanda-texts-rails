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
ཁྲོ་བ་ནི༌[^1177]གནོད་སེམས་དང་རྣམ་པར་འཚེ་བ་མ་གཏོགས་པ་སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པ་ལ་ཀུན་ནས་མནར་སེམས་པ་གང་ཡིན་པའོ། །

[Block 2977]
འཆབ་པ་ནི་ཁ་ན་མ་ཐོ་བ་མཁྱུད་པའོ། །

[Block 2978]
ཉེ་བའི་ཉོན་མོངས་པ་ཁ་ཅིག་སྔར་བཤད་པས་འདིར་རྣམ་པར་མ་ཕྱེའོ། །

[Block 2979]
ཀུན་ནས་དཀྲིས་པ་དེ་རྣམས་ལས།

[Block 2980]
འདོད་ཆགས་ཀྱིས། ངོ་ཚ་མེད་རྒོད་སེར་སྣ་བསླང་། །གསུམ་པོ་འདི་དག་ནི༌[^1178]འདོད་ཆགས་ཀྱི་རྒྱུ་མཐུན་པ་ཡིན་ནོ། །

[Block 2981]
འཆབ་པ་རྩོད་དོ། །

[Block 2982]
ཁ་ཅིག་ན་རེ་སྲེད་པའི་རྒྱུ་མཐུན་པའོ་ཞེའོ། །

[Block 2983]
གཞན་ན་རེ་མ་རིག་པའི་རྒྱུ་མཐུན་པའོ་ཞེའོ། །

[Block 2984]
གཞན་དག་ན་རེ་དེ༌[^1179]གཉིས་ཀ་ཡིན་ཏེ་ཤེས་པ་དང་མི་ཤེས་པ་རྣམས་ཀྱི་ཡིན་ནོ་ཞེས་སོ། །

[Block 2985]
མ་རིག་ལས།

[Block 2986]
རྨུགས་དང་གཉིད་དང་ཁྲེལ་མེད་དོ། །

[Block 2987]
གསུམ་པོ་འདི་ནི་མ་རིག་པའི་རྒྱུ་མཐུན་པའོ། །

[Block 2988 [VERSE]]
ཐེ་ཚོམ་ལས་འགྱོད་ཁྲོ་བ་དང་། །
ཕྲག་དོག་ཁོང་ཁྲོའི་རྒྱུ་ལས་བྱུང་། །

[Block 2989]
ཁོང་ཁྲོ་བ་ཀུན་ནས་བསླང་བ་དག་ཡིན་ཏེ། དེ་ལྟར་ན་ཉེ་བའི་ཉོན་མོངས་པ་བཅུ་པོ་དེ་དག་ནི་ཉོན་མོངས་པའི་རྒྱུ་མཐུན་པ་དག་ཡིན་ནོ། །

[Block 2990 [VERSE]]
གཞན་ཡང་ཉོན་མོངས་དྲི་མ་དྲུག །
སྒྱུ་དང་གཡོ་དང་རྒྱགས་པ་དང་། །
དེ་བཞིན་འཚིག༌[^1180]དང་ཁོན་འཛིན་དང་། །
རྣམ་འཚེ་སྒྱུ་ནི་གཞན་འདྲིད་པའོ། །

[Block 2991]
གཡོ་ནི་སེམས་གྱ་གྱུ་བའོ། །

[Block 2992]
རྒྱགས་པ་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 2993]
འཚིག་པ་ནི་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པའི་དངོས་པོ་ལ་དམ་དུ་འཛིན་པའོ། །

[Block 2994]
ཁོན་དུ་འཛིན་པ་ནི་ཀུན་ནས་མནར་སེམས་ཀྱི་དངོས་པོ་ལ༌[^1181]ལན་མང་དུ་བྱེད་པའོ། །

[Block 2995]
རྣམ་པར་འཚེ་བ་ནི་རྣམ་པར་ཐོ་འཚམས༌[^1182]པའོ། །

[Block 2996]
ཉོན་མོངས་པའི་དྲི་མ་དྲུག་པོ་དེ་དག་ལས།

[Block 2997]
སྒྱུ་དང་རྒྱགས་པ་ནི། །

[Block 2998 [VERSE]]
འདོད་ཆགས་ལས་སྐྱེས་ཁོན་འཛིན་དང་། །
རྣམ་འཚེ་ཁོང་ཁྲོ་ལས་སྐྱེས་སོ། །
འཚིག་པ་ལྟ་བ་མཆོག་འཛིན་ལས། །
གཡོ་ནི་ལྟ་བས་ཀུན་ནས་བསླང་། །

[Block 2999]
རྒྱུ་མཐུན་བཤད་ནས་ཅི་ཞིག་གིས་སྤང་བར་བྱ་བ་བཤད་པར་བྱ་སྟེ།

[Block 3000 [VERSE]]
དེ་ལས་ངོ་ཚ་མེད་པ་དང་། །
ཁྲེལ་མེད་རྨུགས་གཉིད་རྒོད་རྣམ་གཉིས། །

[Block 3001]
ཆོས་ལྔ་པོ་འདི་དག་ནི་མཐོང་བ་དང་བསྒོམ་པས༌[^1183]སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 3002]
དེ་ལས་གཞན་ནི་བསྒོམ་སྤང་བྱ། །ཕྲག་དོག་དང་། སེར་སྣ་དང་། འགྱོད་པ་དང་། ཁྲོ་བ་དང་། འཆབ་པ་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ༌[^1184]དག་ཡིན་ནོ། །

[Block 3003]
རང་དབང་། མ་རིག་པ་ཙམ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་ཉེ་བའི་ཉོན་མོངས་པ་ལྔ་པོ་རང་དབང་ཅན་དག་ཀྱང་ངོ་། །དེ་བཞིན་དྲི་མ་རྣམས། ཉོན་མོངས་པའི་དྲི་མ་དྲུག་ཀྱང་དེ་དང་འདྲའོ། །

[Block 3004]
ཉེ་བའི་ཉོན་མོངས་པ་ཇི་སྐད་བཤད་པ་དེ་དག་ནི། འདོད་ན་མི་དགེ་གསུམ་རྣམ་གཉིས། །རྨུགས་པ་དང་། རྒོད་པ་དང་། གཉིས༌[^1185]ནི་མི་དགེ་དང་། ལུང་དུ་མ་བསྟན་པ་དག་ཡིན་ནོ། །

[Block 3005]
དེ་ཡན་ཆད་ནི་ལུང་མ་བསྟན། འདོད་པའི་ཁམས་ཡན་ཆད་ན་ཅི་རིགས་པར་རྣམ་པ་གཅིག་གོ། །

[Block 3006]
དེ་དག་ལས་དུ་ཞིག་གང་ན་ཡོད་ཅེ་ན། འདོད་དང་བསམ་གཏན་དང་པོ་ན། །གཡོ་སྒྱུ་འདི་ཉིད་ནི། འདོད་པའི་ཁམས་དང་བསམ་གཏན་དང་པོ་ནའོ། །

[Block 3007]
ཚངས་པའི་འཇིག་རྟེན་ན་སྒྱུ༌[^1186]ཇི་ལྟར་ཡོད་ཅེ་ན་ཚངས་པས་འདྲིད་ཕྱིར་རོ། །

[Block 3008]
ཚངས་པ་ཆེན་པོ་ནི་དེ་ན་བདག་ཉིད་ལོག་པར་ཀུན་དུ་སྟོན་པས་ཚེ་དང་ལྡན་པ་རྟ་ཐུལ་ལ་འདྲིད་པར་ཞུགས་སོ། །

[Block 3009]
རྨུགས་རྒོད་རྒྱགས་པ་ཁམས་གསུམ་ན། །གསུམ་པོ་འདི་དག་ནི་ཁམས་གསུམ་པ༌[^1187]དག་ཡིན་ནོ། །

[Block 3010]
གཞན་དག་འདོད་ཁམས་ལས་སྐྱེས་པ། །ཉེ་བའི་ཉོན་མོངས་པ་བཅུ་གཅིག་ནི་འདོད་པ་ན་སྤྱོད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 3011]
ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 3012 [HEADING]]
### རྣམ་ཤེས་དང་དབང་པོ་དང་མཚུངས་པར་ལྡན་པ། ^5-15-0

[Block 3013]
དེ་དག་ལས་ཀྱང་།

[Block 3014 [VERSE]]
མཐོང་སྤང་བྱ་གཉིད༌[^1188]ང་རྒྱལ་བཅས། །
ཡིད་ཀྱི་རྣམ་ཤེས་ས་པ་ཡིན། །

[Block 3015]
མཐོང་བས་སྤང༌[^1189]བར་བྱ་བ་ཐམས་ཅད་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ས་པ་དག་ཡིན་ཏེ། གཉིད༌[^1190]ང་རྒྱལ་བསྒོམ་པས་སྤང་བར་བྱ་བ༌[^1191]དག་དང་བཅས་པ་ཡང་ངོ་། །ཉེ་བའི་ཉོན་མོངས༌[^1192]རང་དབང་ཡང་། །ཉེ་བའི་ཉོན་མོངས་པ་རང་དབང་ཅན་གང་དག་ཡིན་པ་དེ་དག་ནི་ཡིད་ཀྱི་ས་པ་ཁོ་ན་ཡིན་པར་བལྟ་བར་བྱའོ། །
--- END BLOCKS ---
