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
མི་སློབ་པ་ལས་ནི་ལྔ་སྟེ། སློབ་པའི་གཅིག་པུ་མ་གཏོགས་པ་སློབ་པའི་མཇུག་ཐོགས་སུ་ལྔ་པོ་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 1087]
དེ་ཡང་དེ་གཉིས༌[^408]ལས།

[Block 1088]
མི་སློབ་པ་ནི༌[^409]ལྔ་ཁོ་ན་ལས་ཏེ། སྦྱོར་བ་ལས་བྱུང་བ་གསུམ་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །

[Block 1089]
ཅིའི་ཕྱིར་སྦྱོར་བ་ལས་བྱུང་བའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་ནི་རྣམ་པར༌[^410]སྨིན་པ་ལས་སྐྱེས་པ་དང་། སྤྱོད་ལམ་པ་དང་། བཟོའི་གནས་པའི་སེམས་དག་འབྱུང་ལ། སྦྱོར་བ་ལས་བྱུང་བ་ནི་དེ་དག་ལས་མ་ཡིན་ཞེ་ན།

[Block 1090 [VERSE]]
མངོན་པར་འདུ་བྱེད་ཞུགས་པའི་ཕྱིར། །
སྟོབས་ཆུང་ཕྱིར་དང་འབད་མེད་ཕྱིར། །
སྦྱོར་བ་ལས་བྱུང་རྗེས་མཐུན་མིན། །
དེའི་ཕྱིར་དེ་ཡི་མཇུག་ཐོགས་མིན། །

[Block 1091]
དེ་ལ་གསུམ་སྟེ། འབྱུང་བའི་སེམས་ཀྱང་མངོན་པར་འདུ་བྱ་བ་མེད་པས་སྦྱོར་བ་ལས་བྱུང་བའི་མཇུག་ཐོགས་སུ་དངོས་པོའི་དོན་དུ་རབ་ཏུ་སྐྱེའོ། །

[Block 1092]
དེ་ལྟ་ན་འོ་ན་ནི་ཉོན་མོངས་པ་ཅན་དག་ལས་ཀྱང་སྦྱོར་བ་ལས་བྱུང་བ་འབྱུང༌[^411]བར་མི་འགྱུར་ཏེ། མི་མཐུན་པའི་ཕྱིར་རོ། །

[Block 1093 [VERSE]]
ཉོན་མོངས༌[^412]ཅན་ལས་མི་མཐུན་ཀྱང་། །
ཉོན་མོངས་ཀུན་འབྱུང་ཡོངས་ཤེས་ཕྱིར། །
སྦྱོར་བ་ལས་བྱུང་ཀུན་དུ་འབྱུང་། །
མངོན་པར་སྦྱོར་བ་ལ་རིགས་སོ། །

[Block 1094]
དེ་ལ་ཡང་།

[Block 1095 [VERSE]]
སློབ་དང་མི་སློབ་སྦྱོར་བྱུང་དང་། །
གཟུགས་གཏོགས་ལས་ནི་འདོད་སྤྱོད་པ། །
དེ་ལས་དེ་ནི་འབད་མེད་མིན། །
གཟུགས་མེད་སྤྱོད་པའི་ཉོན་མོངས་ལས། །

[Block 1096 [VERSE]]
གཟུགས་སྤྱོད་སྐྱེས་ནས་ཐོབ་མི་འགྱུར། །
གཟུགས་སྤྱོད་ཉོན་མོངས་ཅན་ལས་ནི། །
འདོད་གཏོགས་མི་གསལ་གསལ་ཕྱིར་རོ། །

[Block 1097]
ཚིག་ལེའུར་བྱས་པ་འདི་དག་ཀྱང་འགྲེལ་པ་ཁོ་ན་བསྡུས་པ་ཡིན་པས་རྣམ་པར་ཕྱེའོ། །

[Block 1098 [HEADING]]
#### སེམས་གང་ལ་དུ་ཞིག་རྙེད་པ། ^2-4-3-0

[Block 1099]
གང་དག་སེམས་བཅུ་གཉིས་བཤད་པ་དེ་དག་ལས།

[Block 1100]
སེམས་གང་ལ་དུ་ཞིག་རྙེད་ཅེ་ན།

[Block 1101 [VERSE]]
ཁམས་གསུམ་པ་ཡི་ཉོན་མོངས་ཅན། །
དྲུག་དང་དྲུག་དང་གཉིས་རྙེད་དོ། །

[Block 1102]
འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་གྱི་སེམས་མངོན་དུ་གྱུར་ན་སེམས་དྲུག་རྙེད་དེ། [^413]ཐེ་ཚོམ་གྱིས་དགེ་བའི་རྩ་བའི་ཉིང་མཚམས་སྦྱོར་བ་དང་། ཁམས་སུ་སླར་ལྡོག་པའི་ཕྱིར་རོ། །

[Block 1103]
ཁམས་སུ་སླར་ལྡོག་པ་དང་། དངོས་སུ་ཉམས་པ་ལས་མི་དགེ་བ་དང་། བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་དང་། གཟུགས་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དང་། ཡོངས་སུ་ཉམས་ན་གཟུགས་མེད་ན་སྤྱོད་པའི་ཉོན་མོངས་པ༌[^414]ཅན་དང་། སློབ་པའོ། །

[Block 1104]
གཟུགས་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་ལ་ཡང་དྲུག་རྙེད་དེ། ཁམས་སུ་སླར་ལྡོག་པ་ལས་གཟུགས་ན་སྤྱོད་པ་གསུམ་དང་། འདོད་པ་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དང་། ཡོངས་སུ་ཉམས་པ་ལས་གཟུགས་མེད་པའི་ཉོན་མོངས་པ་ཅན་དང་། སློབ་པའོ། །

[Block 1105]
གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་ལ་ནི་གཉིས་རྙེད་དེ། ཡོངས་སུ་ཉམས་པ་ལས་ཉོན་མོངས་པ་ཅན་དེ་ཉིད་དང་། སློབ་པའོ། །

[Block 1106]
གཟུགས་སྐྱེས་དགེ་ལ་གསུམ་དག་གོ། །

[Block 1107]
དགེ་བ་དེ་ཉིད་དང་། འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་གོ། །

[Block 1108]
སློབ་པ་ལ་བཞི། སློབ་པ་དེ་ཉིད་དང་། འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་དང་། གཟུགས་མེད་པའི་དགེ་བའོ། །

[Block 1109]
འཕགས་པའི་ལམ་གྱིས་འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་ལས་འདོད་ཆགས་དང་བྲལ་བར་བྱེད་པ་ནའོ། །

[Block 1110]
ལྷག་ལ་དེ། སེམས་གང་ལ་རྙེད་པ་མ་བཤད་པ་དེ་ལ་ནི་དེ་ཉིད་རྙེད་པར་བལྟ་བར་བྱའོ། །

[Block 1111]
བསྡུ་བའི་ཚིགས་སུ་བཅད་པ་ནི།

[Block 1112 [VERSE]]
སྐྱེ་དང་སྙོམས་པར་འཇུག་པ་དང་། །
འདོད་ཆགས་བྲལ་དང་ཡོངས་ཉམས་དང་། །
དགེ་བའི་ཉིང་མཚམས་སྦྱོར་བའི་ཚེ། །
སེམས་དེ་ལྡན་པ་མིན་ལས་རྙེད།[^415] །

[Block 1113]
ཅེས་བྱའོ། །

[Block 1114]
དབང་པོ་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་གཉིས་པའོ།། །།

[Block 1115 [HEADING]]
## འཇིག་རྟེན་བསྟན་པ། ^3-0

[Block 1116 [HEADING]]
### སེམས་ཅན་གྱི་འཇིག་རྟེན། ^3-1-0

[Block 1117 [HEADING]]
#### ཁམས་གསུམ། ^3-1-1-0

[Block 1118]
ཁམས་གསུམ་གྱི་དབྱེ་བས་སེམས་ལ་སོགས་པ་རྣམས་ཀྱི་དབྱེ་བ་བཤད་ནས། དེ་ཉིད་མ་བཤད་པས་དེ་བརྗོད་པར་བྱ་སྟེ།

[Block 1119 [VERSE]]
དམྱལ་བ་ཡི་དགས་དུད་འགྲོ་དང་། །
མི་རྣམས་དང་ནི་ལྷ་དྲུག་དག །

[Block 1120]
འདོད་པའི་ཁམས་ཡིན། འགྲོ་བ་བཞི་དང་། ལྷའི་རིས་དྲུག་པོ་འདི་ལྟ་སྟེ། རྒྱལ་ཆེན་བཞི་པ་རྣམས་དང་། སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས་དང་། འཐབ་བྲལ་བ་རྣམས་དང་། དགའ་ལྡན་པ་རྣམས་དང་། འཕྲུལ་དགའ་བ་རྣམས་དང་། གཞན་འཕྲུལ་དབང་བྱེད་པ་རྣམས་ཏེ། འདི་རྣམས་ནི་འདོད་པའི་ཁམས་ཡིན་ནོ། །

[Block 1121]
དམྱལ་བ་དང་།

[Block 1122 [VERSE]]
གླིང་དབྱེ་བ་ལས་དེ་ཉི་ཤུ། །
གནས་རྣམས་ཞེས་བྱ་བ་ཚིག་ལྷག་མའོ། །

[Block 1123]
དམྱལ་བ་ཆེན་པོ་བརྒྱད་དེ། ཡང་སོས་དང་། ཐིག་ནག་དང་། བསྡུས་འཇོམས་དང་། ངུ་འབོད་དང་། ངུ་འབོད་ཆེན་པོ་དང་། ཚ་བ་དང་། རབ་ཏུ་ཚ་བ་དང་། མནར་མེད་པ་དང་། གླིང་བཞི་དང་། ཡི་དགས་དང་། དུད་འགྲོ་ཞེས་བྱ་བ་གནས་ཉི་ཤུ་པོ་འདི་དག་འདོད་པའི་ཁམས་སོ། །

[Block 1124]
འདོད་པའི་ཁམས་འདིའི་གོང་མའི་གནས་དག་བཅུ་བདུན་ནི། གཟུགས་ཁམས་ཡིན། ཇི་ལྟར་ཡིན་ཞེ་ན། དེར་སོ་སོ་ཡི།

[Block 1125 [VERSE]]
བསམ་གཏན་ས་ནི་གསུམ་པ་ཡིན། །
བཞི་པས་ནི་བརྒྱད་པ་ཡིན། །
--- END BLOCKS ---
