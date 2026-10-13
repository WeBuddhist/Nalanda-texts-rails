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
ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་ཀུན་དུ་སྦྱོར་བ། ཐ་མའི་ཆ་དང་མཐུན་རྣམ་ལྔ། །གསུངས་ཏེ། ཅིའི་ཕྱིར་རྣམ་པ་ལྔ་ཁོ་ན་ཡིན་ཞེ་ན། འདི་ལྟར།

[Block 2942 [VERSE]]
གཉིས་ཀྱིས་འདོད་ལས་མི༌[^1164]འདའ་ལ། །
གསུམ་པོ་ཡིས་ནི་ཕྱིར་ཟློག་བྱེད། །

[Block 2943]
འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་དག་གིས་ནི་འདོད་པའི་ཁམས་ལས་མི་འདའོ། །

[Block 2944]
འཇིག་ཚོགས་ལ་ལྟ་བ་ལ་སོགས་པ་དག་གིས་ནི་འདས་ཀྱང་ཕྱིར་ཟློག་པར་བྱེད་དོ། །

[Block 2945]
འདིར་ཡང་གསུངས་པ། སྒོ་དང་རྩ་བས་བསྡུས་ཕྱིར་གསུམ། །ཁོ་ནར་གསུངས་སོ། །

[Block 2946]
སྔར་མཐོང་བས་སྤང་བར་བྱ་བ་སྤངས་ན་ཡང་སྒོ་དང་རྩ་བ་བསྡུས་པས་ཉོན་མོངས་པ་རྣམས་ནི་རྣམ་པ་གསུམ་དུ་གསུངས་ཏེ། རྣམ་པ་གཅིག་པ་དང་། རྣམ་པ་གཉིས་པ་དང་། རྣམ་པ་བཞི་པ་དག་གོ། །

[Block 2947]
དེ་དག་གི་སྒོ་ནི་འདི་གསུམ་གྱིས་བསྡུས་སོ། །

[Block 2948]
གཞན་ཡང་མཐར་འཛིན་པར་ལྟ་བ་ནི་འཇིག་ཚོགས་ལ་ལྟ་བས་རབ་ཏུ་བཅུག་ལ། ལྟ་བ་མཆོག་ཏུ་འཛིན་པའི༌[^1165]ཚུལ་ཁྲིམས་དང་། བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པས་རབ་ཏུ་བཅུག །ལོག་པར་ལྟ་བ་ནི་ཐེ་ཚོམ་གྱིས་རབ་ཏུ་བཅུག་སྟེ། དེའི་ཕྱིར་རྩ་བ་བསྡུས་སོ་ཞེའོ། །

[Block 2949]
གཞན་དག་ན་རེ།

[Block 2950 [VERSE]]
འགྲོ་མི་འདོད་དང་ལམ་ནོར་དང་། །
ལམ་ལ་ཐེ་ཚོམ་དེ་རྙེད་ཅིག །
ཐར་པ་བགྲོད་ལ་གེགས་བྱེད་ཡིན། །
དེ་ཡི་ཕྱིར་ན་གསུམ་བསྟན་ཏོ། །

[Block 2951]
འཇིག་ཚོགས་ལ་ལྟ་བས་ནི་ཐར་པ་ལ་སྐྲག་པར་འགྱུར་བས་འགྲོ་མི་འདོད་པར་འགྱུར་རོ། །

[Block 2952]
ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པས་ནི་ལམ་གཞན་ལ་ཡང་དག་པར་བསྟན་པའི༌[^1166]ཕྱིར་ལམ་ནོར་བར་འགྱུར་རོ། །

[Block 2953]
ཐེ་ཚོམ་གྱིས་ནི༌[^1167]ལམ་ལ་སོམ་ཉི༌[^1168]ཟ་བར་འགྱུར་ཏེ། དེའི་ཕྱིར་འདི་གསུམ་ཁོ་ན་སྤང་བར་བསྟན་ཏོ། །

[Block 2954]
ཇི་ལྟར་ཀུན་དུ་སྦྱོར་བ་ཐ་མའི་ཆ་དང་མཐུན་པ་ལྔ་བཤད་པ་དེ་བཞིན་དུ་ཡང་།

[Block 2955 [VERSE]]
གོང་མིའི༌[^1169]ཆ་དང་མཐུན་ལྔ་ཉིད། །
གཟུགས་དང་གཟུགས་མེད་ལས་སྐྱེས་པའི། །
འདོད་ཆགས་གཉིད༌[^1170]རྒོད༌[^1171]ང་རྒྱལ་རྨོངས། །

[Block 2956]
འདི་དག་མ་སྤངས་པར་ཁམས་གོང་མ་ལས་མི་འདའ་བའི་ཕྱིར་རོ། །

[Block 2957]
ཀུན་དུ་སྦྱོར་བ་བཤད་ཟིན་ཏོ། །

[Block 2958 [HEADING]]
#### འཆིང་བ། ^5-14-2-0

[Block 2959]
འཆིང་བ་ནི་གསུམ་སྟེ། འདོད་ཆགས་དང་། ཞེ་སྡང་དང་། གཏི་མུག་རྣམས་སོ། །

[Block 2960]
འདི་ཡང་། ཚོར་བའི་དབང་གིས་འཆིང་བ་གསུམ། །འདི་ལྟ་སྟེ། བདེ་བའི་ཚོར་བ་ལ་ནི་འདོད་ཆགས་དམིགས་པ་དང་། མཚུངས་པར༌[^1172]ལྡན་པའི་སྒོ་ནས་རྒྱས་པར་འགྱུར་རོ། །

[Block 2961]
སྡུག་བསྔལ་བ་ལས་ནི་ཞེ་སྡང་ངོ་། །བདེ་བ་ཡང་མ་ཡིན། སྡུག་བསྔལ་བ་ཡང་མ་ཡིན་པ་ལ་གཏི་མུག་སྟེ། འདོད་ཆགས་དང་། ཞེ་སྡང་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 2962]
ཡང་ན་རང་གི་རྒྱུད་ལ་ཡོད་པའི་དམིགས་པའི་སྒོ་ནས་ངེས་པ་ཡིན་ནོ། །

[Block 2963]
ཕྲ་རྒྱས་རྣམས་ནི་སྔར་བཤད་པ་ཁོ་ནར་ཟད་དོ། །

[Block 2964 [HEADING]]
#### ཉེ་བའི་ཉོན་མོངས་པ། ^5-14-3-0

[Block 2965]
ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག་གང་དག་ཉོན་མོངས་པ་ཡིན་པ་དེ་དག་ནི་ཉེ་བའི་ཉོན་མོངས་པ་ཡང་ཡིན་ཏེ། སེམས་ཉེ་བར་ཉོན་མོངས་པར་བྱེད༌[^1173]པའི་ཕྱིར་རོ། །

[Block 2966 [VERSE]]
ཉོན་མོངས་ལས་གཞན་ཉོན་མོངས་ཅན། །
སེམས་བྱུང་འདུ་བྱེད་ཕུང་ཞེས་པ། །
གང་དེ་འང་ཉེ་བའི་ཉོན་མོངས་ཏེ། །
དེ་དག་ཉོན་མོངས་ཞེས་མི་བྱ། །

[Block 2967]
དེ་དག་ཀྱང་གཞི་ཕྲན་ཚེགས་ལས་འདོན་པ༌[^1174]གང་ཡིན་པའོ། །

[Block 2968]
འདིར་ནི་ཀུན་ནས་དཀྲིས་པ་དང་ཉོན་མོངས་པའི་དྲི་མས་བསྡུས་པ་ཁོ་ན་བསྟན་པར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག །

[Block 2969 [VERSE]]
ངོ་ཚ་མེད་དང་ཁྲེལ་མེད་དང་། །
ཕྲག་དོག་སེར་སྣ་རྒོད་པ་དང་། །
འགྱོད་དང་རྨུགས་དང་གཉིད་དང་ནི། །
ཀུན་ནས་དཀྲིས་པ་རྣམ་པ་བརྒྱད། །

[Block 2970]
ཡང་ཁ་ཅིག་གིས་བརྒྱད་པོ་དེ༌[^1175]དང་། ཁྲོ་དང་འཆབ་པའོ། །

[Block 2971]
དེ་དག་གིས་བཅུ་སྟེ། དེ་ལ་ཕྲག་དོག་ནི་གཞན་གྱི་ཕུན་སུམ་ཚོགས་པ་ལ་སེམས་ཁོང་ནས་འཁྲུགས༌[^1176]པའོ། །

[Block 2972]
སེར་སྣ་ནི་ཆོས་དང་ཟང་ཟིང་དང་མཁས་པ་རབ་ཏུ་སྦྱིན་པ་དང་། འགལ་བ་ཅན་སེམས་ཀྱི་ཀུན་དུ་འཛིན་པའོ། །

[Block 2973]
རྒོད་པ་ནི་སེམས་རྣམ་པར་མ་ཞི་བའོ། །

[Block 2974]
གཉིད་ནི་ལུས་ཡང་དག་པར་འཛིན་མི་ནུས་པ་སེམས་མངོན་པར་སྡུད་པའོ། །

[Block 2975]
དེ་དང་འགྱོད་པ་ནི་ཉོན་མོངས་པ་ཅན་ཁོ་ན་ཀུན་ནས་དཀྲིས་པ་ཡིན་ནོ། །

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
--- END BLOCKS ---
