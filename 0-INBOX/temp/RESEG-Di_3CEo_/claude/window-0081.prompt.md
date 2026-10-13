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
[Block 2836]
གཞན་ནི་རྣམ་པར་ཕྱེ་སྟེ་སྨྲ་བ་ཡིན་ནོ། །

[Block 2837]
ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་དེ་དག་ཀྱང་དུ་ཞིག་ཅེ་ན། སྨྲས་པ། དེ་དག །

[Block 2838 [VERSE]]
རྣམ་བཞི་དངོས་དང་མཚན་ཉིད་དང་། །
གནས་སྐབས་གཞན་གཞན་འགྱུར་ཞེས་བྱ། །

[Block 2839]
དངོས་པོ་གཞན་དུ་འགྱུར་བ་ནི་བཙུན་པ་ཆོས་སྐྱོབ་ཡིན་ཏེ། དེ་ན་རེ་ཆོས་དུས་རྣམས་སུ་འཇུག་པ་ན་དངོས་པོ་གཞན་དུ་འགྱུར་གྱི་རྫས་གཞན་དུ་འགྱུར་བ་ནི་མ་ཡིན་ཏེ། དཔེར་ན་གསེར་གྱི་སྣོད་བཅོམ་ནས་གཞན་དུ་བྱེད་པ་ནི་དབྱིབས་གཞན་དུ་འགྱུར་བ་བཞིན་ནོ། །

[Block 2840]
མཚན་ཉིད་གཞན་དུ་འགྱུར་བ་ནི་བཙུན་པ་དབྱངས་སྒྲོགས་ཡིན་ཏེ། དེ་ན་རེ་ཆོས་དུས་རྣམས་སུ་འཇུག་པ་ན་འདས་པའི་མཚན་ཉིད་དང་ལྡན་ལ་གཉིས་དང་ནི་མི་ལྡན་པ་མ་ཡིན་ནོ། །

[Block 2841]
དེ་བཞིན་དུ་གཞན་ཡང་ངོ་། །གནས་སྐབས་གཞན་དུ་འགྱུར་བ་ནི་བཙུན་པ་དབྱིག་བཤེས༌[^1134]ཡིན་ཏེ། དེ་ན་རེ་ཆོས་དུས་རྣམས་སུ་འཇུག་པ་ན་འདས་པ་ལ་སོགས་པའི་གནས་སྐབས་སུ་ཕྱིན་ནས་གཞན་དང་གཞན་ཞེས་སྟོན་ཏོ། །

[Block 2842]
གཞན་དང་གཞན་དུ་འགྱུར་བ་ནི་བཙུན་པ་སངས་རྒྱས་ལྷ་ཡིན་ཏེ། ཆོས་དུས་རྣམས་སུ་འཇུག་པ་ན་སྔ་མ་དང་ཕྱི་མ་ལ་ལྟོས༌[^1135]ནས་གཞན་ཞེས་བརྗོད་དོ། །

[Block 2843]
དེ་དག་ལས།

[Block 2844]
གསུམ་པ་བཟང་སྟེ། གནས་སྐབས་གཞན་དུ་འགྱུར་བ་གང་ཡིན་པའོ། །

[Block 2845]
དེའི་ནི། བྱ་བ་ཡིས། དུས་རྣམས་རྣམ་གཞག །གང་གི་ཚེ་ཆོས་དེ་བྱ་བ་མི་བྱེད་པ་དེའི་ཚེ་ནི་མ་འོངས་པ་ཡིན་ལ། གང་གི་ཚེ་བྱ་བ་བྱེད་པ་དེའི་ཚེ་ནི་ད་ལྟར་བྱུང་བ་ཡིན་ཞིང་། གང་གིས་བྱས་ནས་འགགས་པ་དེའི་ཚེ་འདས་པ་ཡིན་ནོ། །

[Block 2846]
དེའི་ཡང་ཆོས་དེའི་བདག་ཉིད་དེ་ཁོ་ནར་ཡོད་ལ་རྟག་ཏུ་བྱ་བ་བྱེད་པ་ལ་གེགས་སུ་བྱེད། གང་གིས་ན་རེས་འགའ་ནི་བྱ་བ་བྱེད་ལ༌[^1136]རེས་འགའ་ནི་མ་ཡིན། བྱ་བ་འདས་པ་དང་། མ་འོངས་པ་དང་། ད་ལྟར་བྱུང་བ་ཞེས་བྱ་བ་གང་ཡིན་པ། དེ་ཡང་ཇི་ལྟར། ཅི་བྱ་བ་ལ་ཡང་བྱ་བ་གཞན་ཞིག་ཡོད་དམ། གལ་ཏེ་ཆོས་ལས་བྱ་བ་གཞན་ཞིག་ཡིན་ན་སྐྱོན་དེར་ཡང་འགྱུར་བ་ཞིག་ཡིན་ན་དེ་ནི་གཞན་མ་ཡིན། དེའི་ཕྱིར་སྐྱོན་དེར་མི་འགྱུར་རོ། དེ་ལྟ༌[^1137]ན་འོ་ན་ནི། དེ་ཉིད་དུས་སུ་མི་རུང་། གང་གི་ཚེ་ཆོས་ཡོད་པ་དེའི་ཚེ་ཁོ་ནར་བྱ་བ་ཡང་ཡོད་པར་འགྱུར་རོ། །

[Block 2847]
གལ་ཏེ་ཇི་ལྟར་ད་ལྟར་རྫས་སུ་ཡོད་པ་དེ་བཞིན་དུ་འདས་པ་དང་མ་འོངས་པ་ཡང་ཡོད་ན། དེ་བཞིན་དུ། ཡོད་ན་ཅི་ཕྱིར་མ་སྐྱེས་ཞིག །ཆོས་དེའི་རང་གི་ངོ་བོ་ཁོ་ནར་ཡོད་ན་ཇི་ལྟར་ན་མ་སྐྱེས་པ་ཞེས་བྱ་བའམ་ཞིག་པ་ཞེས་བྱ་བ་འདི་འགྲུབ་པར་འགྱུར་རོ། །

[Block 2848]
བྱེ་བྲག་ཏུ་སྨྲ་བ་ན་རེ་འདས་པ་དང་མ་འོངས་པའི༌[^1138]རྫས་སུ་ཡོད་པ་ཁོ་ནའོ། །

[Block 2849]
གང་ཞིག་བྲང་བར༌[^1139]མི་ནུས་པ་དེ་ལ་ནི་བདག་ལ་ཕན་པར་འདོད་པས་འདི་ལྟར་རིག་པར་བྱ་སྟེ། ཆོས་ཉིད་དག་ནི་ཟབ་པ་ཡིན། །དེ་གདོན་མི་ཟ་བར་རྟོགས་པས༌[^1140]བསྒྲུབས་པ༌[^1141]མ་ཡིན་ནོ། །

[Block 2850 [HEADING]]
#### སྤངས་ལ་དངོས་པོ་དེ་དང་བྲལ་བ། ^5-9-2-0

[Block 2851]
དངོས་པོ་གང་ཞིག་སྤངས་ན་དངོས་པོ་དེ་དང་བྲལ་བ་ཡིན་པ་འདི་དཔྱད་པར༌[^1142]བྱ་སྟེ། སྤངས་ལ་དངོས་པོ་དེ་དང་བྲལ་བ་ཡང་མ་ཡིན་ནོ། །

[Block 2852]
འདི་ལྟ་སྟེ།

[Block 2853 [VERSE]]
སྡུག་བསྔལ་མཐོང༌[^1143]སྤང་བྱ་སྤངས་ཀྱང་། །
ཀུན་འགྲོ་ལྷག་མ་རྣམས་ཀྱིས་ལྡན། །
དང་པོའི་རྣམ་པ་སྤངས་ཀྱང་དེའི། །
ཡུལ་ཅན་དྲི་མ་ལྷག་རྣམས་ཀྱིས། །

[Block 2854]
སྡུག་བསྔལ་ཤེས་པ་ནི་མ་སྐྱེས་པའི་ཚེ་སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བའི་རིས་སྤངས་པ་ཡིན་ནོ། །

[Block 2855]
དེ་སྤངས་ཀྱང་དེ་ལ་དམིགས་པ་ཀུན་དུ་འགྲོ་བ་ཀུན་འབྱུང་མཐོང་པས་སྤང་བར་བྱ་བ་རྣམས་ཀྱིས༌[^1144]ལྡན་ནོ། །

[Block 2856]
བསྒོམ་པས་སྤང་བར་བྱ་བའི་རིས་ལ་ཡང་རྣམ་པ་དགུ་ལས་དང་པོའི་རྣམ་པ་སྤངས་ནས་དེ་སྤངས་ཀྱང་དེ་ལ་དམིགས་པའི་ཉོན་མོངས་པ་ལྷག་མ་རྣམས་ཀྱིས་ལྡན་པར་རིག་པར་བྱའོ། །

[Block 2857 [HEADING]]
### ཆོས་བཅུ་དྲུག་ལ་སེམས་བཅུ་དྲུག་རྒྱས་པ། ^5-10-0

[Block 2858]
དངོས་པོ་གང་ལ་ཕྲ་རྒྱས་དུ་ཞིག་རྒྱས་པར་འགྱུར་ཞེས་བྱ་བའི་ཚིག་འདི་རེ་རེ་ནས་བཤད་ན་ནི་བརྗོད་པར་བྱ་བ་མང་པོར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་མདོར་བསྡུ་ན་ཆོས་ནི་བཅུ་དྲུག་ཏུ་རྣམ་པར་གཞག་པ་དང་། སེམས་བཅུ་དྲུག་ཏུ་རྣམ་པར་བཞག་ནས་ཡུལ་ཅན་གྱི་ངེས་པ་རབ་ཏུ་བསྟན་པར་བྱ་སྟེ།

[Block 2859 [VERSE]]
སྡུག་བསྔལ་རྒྱུ་མཐོང་གོམས་པ་ཡིས། །
སྤང་བྱ་འདོད་ཁམས་ལས་སྐྱེས་པ། །
རང་གི་གསུམ་དང་གཟུགས་གཏོགས་གཅིག །
དྲི་མེད་རྣམ་ཤེས་སྤྱོད་ཡུལ་ལོ། །

[Block 2860]
རེ་ཞིག་སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་བ་མཐོང་བས་སྤང་བར་བྱ་བ་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཆོས་འདོད་པ་ན་སྤྱོད་པ་རྣམས་ཀྱི་ནི་སེམས་ལྔའི་དམིགས་པ་ཡིན་ཏེ། རང་གི་ཁམས་པ་གསུམ་སྟེ། དེ་དག་ཉིད་དང་། གཟུགས་ན་སྤྱོད་པ་སྟེ། བསྒོམ་པས་སྤང་བར་བྱ་བ་ཁོ་ན་དང་།

[Block 2861 [VERSE]]
ཟག་པ་མེད་པའི་དམིགས་པ་ཡིན་ནོ། །
གཟུགས་ཁམས་ལས་སྐྱེས་རང་གི་དང་། །
འོག་གསུམ་གོང་གཅིག་དྲི་མེད་ཀྱིའང་། །

[Block 2862]
ཆོས་རྣམ་པ་གསུམ་པོ་དེ་དག་ཉིད་གཟུགས་ན་སྤྱོད་པ་ན་སེམས་བརྒྱད་ཀྱི་དམིགས་པ་ཡིན་ཏེ། རང་གི་ས་པ་གསུམ་སྟེ། དེ་དག་ཉིད་དང་། ཁམས་འོག་མ་པ་གསུམ་སྟེ། དེ་དག་ཉིད་དང་། ཁམས་གོང་མ་པ་གཅིག་སྟེ། བསྒོམ་པས་སྤང་བར་བྱ་བ་ཁོ་ན་དང་། ཟག་པ་མེད་པའི་དམིགས་པ་ཡིན་ནོ། །

[Block 2863 [VERSE]]
གཟུགས་མེད་ལས་སྐྱེས་ཁམས་གསུམ་གཏོགས། །
གསུམ་དང་ཟག་མེད་སྤྱོད་ཡུལ་ལོ། །

[Block 2864]
ཆོས་རྣམ་པ་གསུམ་པོ་དེ་དག་ཉིད་གཟུགས་མེད་པ་ན་སྤྱོད་པ་ནི་སེམས་བཅུའི་དམིགས་པ་ཡིན་ཏེ། ཁམས་གསུམ་པ་རྣམ་པ་གསུམ་གསུམ༌[^1145]སྟེ། དེ་དག་ཉིད་དང་།

[Block 2865 [VERSE]]
ཟག་པ་མེད་པའི་དམིགས་པ་ཡིན་ནོ། །
འགོག་དང་ལམ་མཐོང་སྤང་བྱ་ཀུན། །
རང་གིས་གླགས༌[^1146]པའི་སྤྱོད་ཡུལ་ལོ། །

[Block 2866]
འགོག་པ་དང་། ལམ་མཐོང་བས་སྤང་བར་བྱ་བའི་ཆོས་རྣམས་ཀྱི་རང་གི་སེམས་ནི་འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ཁོ་ན་ཡིན་ཏེ། ཆོས་དེ་དག་ནི་དེས་གླགས་པའི་དམིགས་པ་ཡིན་ནོ། །

[Block 2867 [VERSE]]
ཟག་མེད་ཁམས་གསུམ་མཐའ་གསུམ་དང་། །
ཟག་པ་མེད་པའི་སྤྱོད་ཡུལ་ལོ། །

[Block 2868]
ཆོས་ཟག་པ་མེད་པ་རྣམས་ནི་སེམས་བཅུའི་དམིགས་པ་ཡིན་ཏེ། ཁམས་གསུམ་གྱི་རྣམ་པ་གསུམ་སྟེ། འགོག་པ་དང་། ལམ་མཐོང་བ་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བ་དང་། ཟག་པ་མེད་པའི་དམིགས་པ་ཡིན་ནོ། །

[Block 2869]
དེ་ལྟར་སེམས་བཅུ་དྲུག་པོ་དེ་དག་གིས༌[^1147]དམིགས་པ་ཆོས་བཅུ་དྲུག་རྣམ་པར་གཞག་པར་རིག་ནས། གང་ལ་ཇི་ཙམ་དུ་ཕྲ་རྒྱས་དག་རྒྱས་པར་འགྱུར་བ་དེ་དག་མངོན་པར་རིག་པར་བྱའོ། །

[Block 2870]
དེ་ལ་ཡང་།

[Block 2871 [VERSE]]
ཉོན་མོངས་ཕྲ་རྒྱས་བཅས་རྣམས༌[^1148]གཉིས། །
ཉོན་མོངས་ཅན་མིན་རྒྱས་འགྱུར་གྱིས། །

[Block 2872]
སེམས་ཉོན་མོངས་པ་ཅན་ནི་དེ་དང་མཚུངས་པར་ལྡན་པ་དང་། དེ་ལ་དམིགས་པ་མ་སྤངས་པའི་ཕྲ་རྒྱས་རྒྱས་པར་འགྱུར་བ་རྣམས་དང་།དེ་དང༌[^1149]མཚུངས་པར་ལྡན་པ་སྤངས་པ་རྒྱས་པར་མི་འགྱུར་བ་རྣམས་ཀྱི་ཕྲ་རྒྱས་དང་བཅས་པ་ཡིན་ཏེ། དེ་དང་ལྷན་ཅིག་པའི་ཕྱིར་རོ། །

[Block 2873]
སེམས་ཉོན་མོངས་པ༌[^1150]ཅན་མ་ཡིན་པ་ནི་དེ་ལ་དམིགས་པ་མ་སྤངས་པ་རྒྱས་པར་འགྱུར་བ་དག་ཁོ་ནས་ཕྲ་རྒྱས་དང་བཅས་པ་ཡིན་ནོ། །

[Block 2874 [HEADING]]
### ཕྲ་རྒྱས་བཅུ་པོའི་འཇུག་པའི་རིམ་པ། ^5-11-0

[Block 2875]
ཕྲ་རྒྱས་བཅུ་པོའི་འཇུག་པའི་རིམ་པ་བསྟན་པར་བྱ་སྟེ། རེ་ཞིག་དང་པོ་ཁོ་ནར་མ་རིག་པ་དང་ལྡན་པ་ལས་བདེན་པ་རྣམས་ལ་ཀུན་དུ་རྨོངས་པར་འགྱུར་ཏེ། དེའི་ཕྱིར། རྨོངས་ལ་ཐེ་ཚོམ། རྨོངས་པར་གྱུར་པ་ཕྱོགས་གཉིས་ཐོས་ནས་ཐེ་ཚོམ་སྐྱེ་བར་འགྱུར་རོ། །
--- END BLOCKS ---
