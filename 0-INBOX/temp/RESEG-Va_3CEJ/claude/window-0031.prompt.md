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
[Block 1086]
དྲུག་གང་ཞེ་ན། མིག་དང་རྣ་བ་དང་སྣ་དང་ལྕེ་དང་ལུས་དང་སྲོག་གི་དབང་པོ་རྣམས་སོ། །

[Block 1087]
བདུན་ནམ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་མཚན་གཅིག་པ་ཞིག་ཡིན་ན་སྟེ། འདི་ལྟར་ལྷ་ལ་སོགས་པ་དག་ནའོ། །

[Block 1088]
བརྒྱད་ཅེས་བྱ་བ་ནི་གལ་ཏེ་མཚན་གཉིས་པ་ཞིག་ཡིན་ནའོ། །

[Block 1089]
ཅི་རྫུས་ཏེ་སྐྱེ་བ་ཡང་མཚན་གཉིས་པ༌[^478]ཡོད་དམ་ཞེ་ན། ངན་སོང་དག་ན་ཡོད་དོ། །

[Block 1090]
རེ་ཞིག་འདོད་པའི་ཁམས་ན་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 1091]
འོ་ན་གཟུགས་ཀྱི་ཁམས་དང་། གཟུགས་མེད་པའི་ཁམས་ན་ཇི་ལྟ་བུ་ཡིན༌[^479]ཞེ་ན། གཟུགས་ན་དྲུག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདོད་པའི་ཁམས་ནི་འདོད་པ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་འདོད་པ་རྣམ༌[^480]ཞེས་བསྟན་ལ། གཟུགས་ཀྱི་ཁམས་ནི་གཟུགས་གཙོ་བོ་ཡིན་པའི་ཕྱིར་གཟུགས་རྣམས་ཞེས་བསྟན་ཏེ། མདོ་ལས་ཀྱང་། གང་ཡང་གཟུགས་མེད་པའི་རྣམ་པར་ཐར་པ་ཞི་བ་གང་དག་གཟུགས་རྣམས་ལས་འདས་ཏེ་ཞེས་གསུངས་སོ། །

[Block 1092]
གཟུགས་ཀྱི་ཁམས་དེ་ན་ནི་དང་པོ་ཉིད་དུ་དབང་པོ་དྲུག་རྣམ་པར་སྨིན་པ་འཐོབ་སྟེ། འདོད་པའི་ཁམས་ན་རྫུས་ཏེ་སྐྱེ་བ་མཚན་མ༌[^481]མེད་པ་དག་གིས་རྙེད་པ་གང་དག་ཡིན་པ་དེ་དག་ཉིད་དོ། །

[Block 1093]
གོང་མར་གཅིག །གཟུགས་ཀྱི་ཁམས་པས་ནི་གཟུགས་མེད་པའི་ཁམས༌[^482]སྙོམས་པར་འཇུག་པས་རིང་བའི༌[^483]ཕྱིར་དང་། སྐྱེ་བས་ཆེས་མཆོག་ཡིན་པའི་ཕྱིར་གོང་མ་སྟེ། དེར་ནི་དང་པོ་ཉིད་དུ་སྲོག་གི་དབང་པོ་གཅིག་ཁོ་ན་རྣམ་པར་སྨིན་པ་ཐོབ་སྟེ། གཞན་ནི་མ་ཡིན་ནོ། །

[Block 1094]
རྙེད་པ་བཤད་ཟིན་ཏོ། །

[Block 1095 [HEADING]]
#### གཏོང་བ། ^2-1-6-0

[Block 1096]
ད་ནི་གཏོང་བ༌[^484]བརྗོད་པར་བྱ་སྟེ། ཁམས་གང་དུ་འཆི་བ་ན་དབང་པོ༌[^485]ཞིག་ཐམས་ཅད་ཀྱི་ཐ་མར་གཏོང་ཞེ་ན།

[Block 1097 [VERSE]]
གཟུགས་མེད་དག་ཏུ་འཆི་བ་ནི། །
སྲོག་དང་ཡིད་དང་བཏང་སྙོམས་ཉིད། །
འགག་པར་འགྱུར་རོ་གཟུགས་ན་བརྒྱད། །

[Block 1098]
གཟུགས་ཀྱི་ཁམས་སུ་འཆི་ན་ཕུང་པོ་དེ་དག་དང་། མིག་ལ་སོགས་པ་ལྔ་དང་། དབང་པོ་བརྒྱད་འགག་སྟེ། བརྫུས་ཏེ་སྐྱེ་བ་ཐམས་ཅད་ནི་དབང་པོ་རྣམས་ཚང་བར་སྐྱེ་ཞིང་འཆིའོ། །

[Block 1099]
འདོད་པར་བཅུ་འམ་དགུ་འམ་བརྒྱད་འདོད་པའི་ཁམས་སུ་འཆི་ན་མཚན་གཉིས་པ་ཞིག་ཡིན་ན་ནི་བརྒྱད་པོ་དེ་དག་དང་། ཕོ་དང་མོའི་དབང་པོ་དང་དབང་པོ་བཅུ་འགག་པར་འགྱུར་རོ། །

[Block 1100]
མཚན་གཅིག་པ་ཞིག་ན་ནི་དགུའོ། །

[Block 1101]
མཚན་མེད་པ་ཞིག་ཡིན༌[^486]ན་ནི་བརྒྱད་དེ། ཅིག་ཅར་འཆི་བ་ལ་ནི་ཚུལ་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 1102]
རིམ་གྱིས་འཆི་བ་དག་ལ་བཞི། རིམ་གྱིས་འཆི་ན་ལུས་དང་སྲོག་དང་ཡིད་དང་བཏང་སྙོམས་ཀྱི་དབང་པོ་དག་དང་དབང་པོ་བཞི་འགག་སྟེ། དེ་རྣམས་ལ་ནི་སོ་སོར་འགག་པ་མེད་དོ། །

[Block 1103]
ཉོན་མོངས་པ་ཅན་དང་ལུང་དུ་མ་བསྟན་པའི་སེམས་ཀྱིས་འཆི་བ་ལ་ནི་ཚུལ་དེ་ལྟ་བུ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1104]
གང་གི་ཚེ་དགེ་བའི་སེམས་ལ་གནས་ཏེ་འཆི་བ་དེའི་ཚེ་ནི། དགེ་བ་ཐམས་ཅད་དག་ཏུ་ལྔ། །དགེ་བའི་སེམས་ལ་གནས་ཏེ་འཆི་ན་ཐམས་ཅད་དུ་ཇི་སྐད་བཤད་པའི་དབང་པོ་རྣམས་དང་། ལྷག་པར་དད་པ་ལ་སོགས་པ་ལྔ་འགག་སྟེ། དེ་རྣམས་ནི་དགེ་བའི་སེམས་ལ་གདོན་མི་ཟ་བར་ཡོད་དོ། །

[Block 1105]
དེ་ལྟར་ན་གཟུགས་མེད་པ་ན་ནི་བརྒྱད་འགག་པར་འགྱུར་རོ། །

[Block 1106]
གཟུགས་ན་ནི་བཅུ་གསུམ་མོ་ཞེས་རྒྱས་པར་བརྩི་བར་བྱའོ། །

[Block 1107 [HEADING]]
#### དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་འཐོབ་པ། ^2-1-7-0

[Block 1108 [HEADING]]
##### འབྲས་བུ་ཐ་མ་གཉིས། ^2-1-7-1-0

[Block 1109]
དབང་པོའི་སྐབས་སུ་དབང་པོའི་ཆོས་ཐམས་ཅད་དཔྱད་པར་བྱ་སྟེ། དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་གང་ཞིག་དབང་པོ་དུ་དག་གིས་འཐོབ་ཅེ་ན།[^487] འབྲས་བུ་ཐ་མ་གཉིས་ནི་དབང་པོ་དགུས་འཐོབ་བོ། །

[Block 1110]
ཡང་ཐ་མ་གང་དག་ཡིན་ཞེ་ན། རྒྱུན་དུ་ཞུགས་པ་དང་། དགྲ་བཅོམ་པ་ཉིད་ཀྱི་འབྲས་བུའོ། །

[Block 1111]
བར་མ་གང་དག་ཡིན་ཞེ་ན། ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་དང་། ཕྱིར་མི་འོང་བའི་འབྲས་བུའོ།[^488] །དེ་ལ་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ནི་དད་པ་ལ་སོགས་པ་དང་། [^489]ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་མ་གཏོགས་པ་དག་དང་། ཡིད་དང་། བཏང་སྙོམས་ཀྱི་དབང་པོ་དག་དང་དགུས་འཐོབ་སྟེ། ཀུན་ཤེས༌[^490]པར་བྱེད་པའི་དབང་པོ་ནི་བར་ཆད་མེད་པའི་ལམ་ལ་རིག་པར་བྱའོ། །

[Block 1112]
ཀུན་ཤེས་པའི་དབང་པོ་ནི་རྣམ་པར་གྲོལ་བའི་ལམ་ལ་རིག་པར་བྱའོ། །

[Block 1113]
གཉི་གས་ཀྱང་དེ་འཐོབ་སྟེ། གོ་རིམས་བཞིན་དུ་བྲལ་བའི་འཐོབ༌[^491]པ་འདྲེན་པར་བྱེད་པ་དང་། རྟེན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1114]
དགྲ་བཅོམ་པ་ཉིད་ནི་དད་པ་ལ་སོགས་པ་དང་། ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་མ་གཏོགས་པ་དག་དང་། ཡིད་ཀྱི་དབང་པོ་དང་། བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་ཀྱི་དབང་པོ་རྣམས་ལས་གང་ཡང་རུང་བ་ཞིག་དང་དགུས་འཐོབ་བོ། །

[Block 1115 [HEADING]]
##### ལན་ཅིག་ཕྱིར་འོང་བ་དང་ཕྱིར་མི་འོང་བའི་འབྲས་བུ། ^2-1-7-2-0

[Block 1116]
གཉིས་ནི་བདུན་དང་བརྒྱད་དང་དགུས། །ལན་ཅིག་ཕྱིར་འོང་བ་དང་ཕྱིར༌[^492]མི་འོང་བའི་འབྲས་བུ་དག་ནི་རེ་རེ་ཞིང་དབང་པོ་བདུན་ནམ༌[^493]བརྒྱད་དམ་དགུ་དག་གིས་འཐོབ་སྟེ། ཇི་ལྟ་ཞེ་ན། རེ་ཞིག་གལ་ཏེ་ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་མཐར་གྱིས་འཐོབ་ལ་དེ་ཡང་འཇིག་རྟེན་པའི་ལམ་གྱིས་འཐོབ་ན་ནི་དེ་དད་པ་ལ་སོགས་པ་ལྔ་དང་། བཏང་སྙོམས་དང་ཡིད་ཀྱི་དབང་པོ་དང་དབང་པོ་བདུན་དག་གིས་འཐོབ་པོ། །འོན་ཏེ་འཇིག་རྟེན་ལས་འདས་པའི་ལམ་གྱིས་འཐོབ་ན་ནི་དེས༌[^494]དབང་པོ་བརྒྱད་དག་གིས་འཐོབ་སྟེ།

[Block 1117]
བརྒྱད་པ་ནི་ཀུན་ཤེས་པའི་དབང་པོ་ཡིན་ནོ། །

[Block 1118]
ཅི་སྟེ་ཕལ་ཆེར་ལ་འདོད་ཆགས་དང་བྲལ་བ་ཞིག་གིས་འཐོབ་ན་ནི་དེ་དགུས་འཐོབ་སྟེ། གང་དག་ཁོ་ནས་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་འཐོབ་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1119]
གལ་ཏེ་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་མཐར་གྱིས་འཐོབ་ལ་དེ་ཡང་འཇིག་རྟེན་པའི་ལམ་གྱིས་འཐོབ་ན་ནི་དེ་དབང་པོ་བདུན་གྱིས་འཐོབ་སྟེ། ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུའི་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 1120]
འོན་ཏེ་འཇིག་རྟེན་ལས་འདས་པའི་ལམ་གྱིས་འཐོབ་ན་ནི་དེ་དབང་པོ༌[^495]བརྒྱད་ཀྱིས་འཐོབ་སྟེ། དེ་དང་འདྲའོ། །

[Block 1121]
ཅི་སྟེ་འདོད་ཆགས་དང་བྲལ་བ་ཞིག་གིས་འཐོབ་ན་ནི་དེ་དགུས་འཐོབ་སྟེ། རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུའི་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 1122]
འདི་ནི་ཁྱད་པར་ཡིན་ཏེ། རྟེན་གྱི་བྱེ་བྲག་ལས་བདེ་བ་དང་ཡིད་བདེ་བ་དང་བཏང་སྙོམས་ཀྱི་དབང་པོ་རྣམས་ལས་གང་ཡང་རུང་བ་ཞིག་ཡིན་ནོ། །

[Block 1123]
གང་གི་ཚེ་འདི་མཐར་གྱིས་པ་ཞིག་ཡིན་ལ། རྣམ་པར་གྲོལ་བའི་ལམ་དགུ་པ་ལ་འཇིག་རྟེན་པའི་ལམ་གྱིས་བསམ་གཏན་ལ་འཇུག་པ་དེའི་ཚེ་ཡང་དབང་པོ་བརྒྱད་ཀྱིས་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་འཐོབ་སྟེ། དེ་ལ་རྣམ་པར་གྲོལ་བའི་ལམ་དགུ་པ་ལ་ནི་ཡིད་བདེ་བའི་དབང་པོ་བརྒྱད་པ་ཡིན་ནོ། །

[Block 1124]
བར་ཆད་མེད་པའི་ལམ་ལ་ནི་རྟག་ཏུ་བཏང་སྙོམས་ཀྱི་དབང་པོ་ཁོ་ན་སྟེ། དེ་ནི་གཉི་གས་ཀྱང་འཐོབ་བོ། །

[Block 1125]
འོན་ཏེ་འཇིག་རྟེན་ལས་འདས་པས་འཇུག་ན་ནི་དེ་དབང་པོ་དགུས་འཐོབ་སྟེ།
--- END BLOCKS ---
