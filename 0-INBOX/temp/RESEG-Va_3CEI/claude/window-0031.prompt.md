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
ཚེའི་རྙོག་པའི་གཉེན་པོ་ནི་དབང་པོ་སོ་སོའི་གྲུབ་པའི་མཐའོ། །

[Block 1087]
ཉོན་མོངས་པའི་རྙོག་པ་དང་། ལྟ་བའི་རྙོག་པའི་གཉེན་པོ་ནི་གཉེན་པོའི་གྲུབ་པའི་མཐའོ། །

[Block 1088]
གྲུབ་པའི་མཐའ༌[^1092]གསུམ་གྱིས༌[^1093]རྙོག་པ་ལྔ་བཅོམ་ནས་དོན་དམ་པར་ཞུགས་ཏེ་ཡང་དག་པ་ཉིད་ནི་རིག་པའོ། །

[Block 1089 [HEADING]]
###### **གཟུགས་པ་དང་གཞིག་པ།** ^4-2-10-2-1-1-4-0

[Block 1090]
དེ་ལ་གཟུགས་པ་དང་གཞིག་པ་ནི་དྲིས་པ། ཅིའི་ཕྱིར་རྙོག་པ་ལྔ་ལས་མི་མང་མི་ཉུང་ཞེ་ན། ལན་བཏབ་པ། སེམས་ཅན་ལ་རྣམ་པ་གཉིས་ཏེ། སྡིག་པ་སྤྱོད་པ་ཁྱིམ་པ་སྐྱེ་བོ༌[^1094]དང་ལོག་པར་ལྟ་བ་སྟེ་རབ་ཏུ་བྱུང་བའི་མུ་སྟེགས་ཅན་ནོ། །

[Block 1091]
ཁྱིམ་པ་ཤིས་པ༌[^1095]མེད་པ་ཉོན་མོངས་པ་བསྐྱེད་པ་ནི་ཉོན་མོངས་པའི་རྙོག་པ་ཞེས་བྱའོ། །

[Block 1092]
མུ་སྟེགས་ཅན་ལ༌[^1096]ལོག་པར་ལྟ་བ་དོན་མེད་པ་ཚོལ་བ་ནི་ལྟ་བའི་རྙོག་པ་ཞེས་བྱའོ། །

[Block 1093]
གཞན་ཡང་དབང་པོ་རྟུལ་པོ༌[^1097]ནི་ཉོན་མོངས་པའི་རྙོག་པ་ཞེས་བྱ། དབང་པོ་རྣོན་པོ་ནི་ལྟ་བའི་རྙོག་པ་ཞེས་བྱ་སྟེ། རྒྱུ་རྣམ་པ་གཉིས་ཀྱིས་མ་འོངས་པའི་འབྲས་བུ་ཐོབ་པའི་ཚེ་བསྡུ་བ་དང་དབྱེ་བ་མི་མཐུན་པས༌[^1098]རྙོག་པ་རྣམ་གཉིས་སུ་ཕྱེ་སྟེ་ནང་གི་འབྲས་བུ་གཉིས་དང་སྤྱིར་བསྡུ་བ་ནི་སེམས་ཅན་གྱི་རྙོག་པ་ཞེས་བྱའོ། །

[Block 1094]
སེམས་ཅན་སྡིག་པ་ཕྱིའི་འབྲས་བུ་གཉིས་དང་སྤྱིར་བསྡུས་པ་ནི་བསྐལ་པའི་རྙོག་པ་ཞེས་བྱའོ། །

[Block 1095]
རྩ་བ་བསྟན་པའམ། ནང་གི་མི་དགེ་བའི་འབྲས་བུ་ནི་ཚེའི་རྙོག་པ་ཞེས་བྱ། ཕྱི་རོལ་གྱི་མི་དགེ་བའི་འབྲས་བུ་ནི་བསྐལ་པའི་རྙོག་པ་ཞེས་བྱ། སྡིག་པའི་རྒྱུ་དང་འབྲས་བུ་སེམས་ཅན་སྡིག་པ་ལས་ཡོད་པར༌[^1099]འགྱུར་བས་སེམས་ཅན་གྱི་རྙོག་པ་ཞེས་བྱ་སྟེ་དེ་བས་ན་རྙོག་པ་ལྔའི་མཚན་ཉིད་བསྟན་པས་དེ་ལ་སྐྱོ་བར་བྱ་བའི་ཕྱིར་རྙོག་པ་ལྔ་བཤད་དོ། །

[Block 1096 [HEADING]]
###### **གཅིག་གིས་གཅིག་བསྡུ་བ།** ^4-2-10-2-1-1-5-0

[Block 1097]
དེ་ལ་གཅིག་གིས་གཅིག་བསྡུ་བ་ནི་མདོ་དག་ལས་རྙོག་པ་བཅུ་གཉིས་གསུངས་ཏེ། བསྐལ་པའི་རྙོག་པ་བསྟན་པ་དང་། དུས་ཀྱི་རྙོག་པ་བསྟན་པ་དང་། སེམས་ཅན་གྱི་རྙོག་པ་བསྟན་པ་དང་། ཉོན་མོངས་པའི་རྙོག་པ་བསྟན་པ་དང་། ཚེའི་རྙོག་པ་བསྟན་པ་དང་། ཐེག་པ་གསུམ་གྱི་ཁྱད་པར་གྱི་རྙོག་པ་བསྟན་པ་དང་། ཡོངས་སུ་མ་དག་པའི་ཞིང་གི་རྙོག་པ་བསྟན་པ་དང་། སེམས་ཅན་གདུལ་དཀའ་བའི་རྙོག་པ་བསྟན་པ་དང་། ཉོན་མོངས་པ་སྣ་ཚོགས་བསྟན་པའི་རྙོག་པ་བསྟན་པ་དང་། མུ་སྟེགས་ཅན་འཁྲུག་པའི་རྙོག་པ་བསྟན་པ་དང་། བདུད་ཀྱི་རྙོག་པ་བསྟན་པ་དང་། བདུད་ཀྱི་ལས་ཀྱི་རྙོག་པ་བསྟན་པ་དང་བཅུ་གཉིས་སོ། །

[Block 1098]
རྙོག་པ་བཅུ་གཉིས་པོ་འདི་སྤྲུལ་པའི་སངས་རྒྱས་ཀྱི་ཞིང་ན་ཐེག་པ་ཆེན་པོ་པ་འབའ་ཞིག་ལ་ཡོད་དོ། །

[Block 1099]
རྙོག་པ་ལྔའི་ཡོངས་སུ་མ་དག་པའི་ཞིང་ན་ཐེག་པ་ཆེ་ཆུང་གཉི་ག་ལ་ཡོད་དོ། །

[Block 1100]
བསྐལ་པ་དང་དུས་ནི་བསྐལ་པའི་རྙོག་པ་སེམས་ཅན་དང་གདུལ་དཀའ་བའི་སེམས་ཅན་ནི་སེམས་ཅན་གྱི་རྙོག་པ་ཉོན་མོངས་པ་དང་ཉོན་མོངས་པ་སྣ་ཚོགས་པ༌[^1100]ནི་ཉོན་མོངས་པའི་རྙོག་པ། ཚེ་ནི་ཚེའི་རྙོག་པ། མུ་སྟེགས་ཅན་འཁྲུག་པ་ནི་ལྟ་བའི་རྙོག་པ་སྟེ། བརྒྱད་པོ་འདི་ནི་རྙོག་པ་རྣམ་པ་ལྔའོ། །

[Block 1101]
ལྷག་མ་བཞི་པོ་ནི་ཐེག་པ་གསུམ་གྱི་ཁྱད་པར་དུ་བསྟན་ཏོ། །

[Block 1102]
ཡོངས་སུ་མ་དག་པའི་ཞིང་ན་བདུད་དང་བདུད་ཀྱི་ལས་ནི་རྙོག་པ་ལྔར་མི་བསྡུའོ། །

[Block 1103]
འགྲེལ་པ་ལས་རྣམ་པར་དག་པ་ནི་རྙོག་པ་མ་ཡིན་པའི་དོན་ཏེ། རྙོག་པ་ལ་ཡང་རྣམ་པ་དྲུག་སྟེ། རྙོག་པ་འདི་དང་བྲལ་ན་རྣམ་པར་དག་པ་ཞེས་བྱའོ། །

[Block 1104]
དྲུག་གང་ཞེ་ན་ཆགས་པའི་རྙོག་པ་དང་། སྤྱོད་ལམ་གྱི་རྙོག་པ་དང་། སྒྲིབ་པའི་རྙོག་པ་དང་། མཚན་མ་ཐ་དད་པའི་རྙོག་པ་དང་། ཡོན་ཏན་དང་མི་ལྡན་པའི་རྙོག་པ་དང་། གཏི་མུག་གི་རྙོག་པ་དང་དྲུག་གོ། །

[Block 1105]
གཉེན་པོའི་ཕྱིར་ལེ་ལོ་སྤང་བའི་ཕྱིར་དག་པའི་ཕྱིར་བསྟན་པའི་ཕྱིར་བསོད་ནམས་དང་ལྡན་པའི་ཕྱིར། ཡེ་ཤེས་དང་ལྡན་པའི་ཕྱིར་གཉེན་པོ་འདི་དྲུག་དང་ཟག་པ་དྲུག་གོ་རིམས་སུ་སྦྱར་རོ། །

[Block 1106]
ཆོས་ཉིད་སངས་རྒྱས་ནི་རྙོག་པ་ལྔའི་ཚེ་འཇིག་རྟེན་དུ་གཤེགས་ཏེ་དེ་བས་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ནི་རྙོག་པ་ལྔའི་དུས་སུ་འཇིག་རྟེན་དུ་གཤེགས་སོ། །

[Block 1107]
ཅིའི་ཕྱིར་བྱམས་པ་ནི་ཚེ་ལོ་བརྒྱད་ཁྲིའི་དུས་སུ་གཤེགས་ལ་ཤཱཀྱ་ཐུབ་པ་ནི་ཚེ་ལོ་བརྒྱའི་དུས་སུ་གཤེགས་པར་གྱུར།[^1101] སྨྲས་པ། སྨོན་ལམ་ནི་ཐ་དད་ཀྱི་གཉི་ག་ཡང་རྙོག་པ་ལྔའི་དུས་སུ་གཤེགས་པར་འདྲ་བར་སྔར་ཐེག་པ་གསུམ་ཐབས་ཙམ་དུ་བསྟན་ནས་ཕྱིས་ཡང་དག་པ༌[^1102]བསྟན་ཏེ། །སྤྲུལ་པའི་སྐུ་ལ༌[^1103]འདྲའོ། །

[Block 1108]
གལ་ཏེ་བསོད་ནམས་ཀྱི་སྐུ་དང་། སྤྲུལ་པའི་སྐུ་ལ༌[^1104]ཐེག་པ་གཉིས་པོ་ལ་འདུལ་བ་མི་མཛད་ན་ངེས་པར་རྙོག་པ་མ་ཡིན་པའི་དུས་སུ་གཤེགས་ནས་ཐེག་པ་གཉིས་པོ་ལ་གདུལ་བར་མཛད་པས་ངེས་པར༌[^1105]རྙོག་པའི་དུས་སུ་གཤེགས་སོ། །

[Block 1109]
རྙོག་པ་ཞེས་བྱ་བ་ནི་འགྲིབ་པའི་བསྐལ་བ་ལས་འཇུག་སྟེ་རྙོག་པ་ལྔ་ཁད་ཀྱིས༌[^1106]སྐྱེ་བས་དེ་ལ་རྙོག་པ་ཞེས་བྱའོ། །

[Block 1110]
སངས་རྒྱས་བྱམས་པ་གཤེགས་པའི་ཚེ་ལོ་བརྒྱད་ཁྲི་ལས་ཁད་ཀྱིས༌[^1107]བྲི་བས་དེ་ལ་ཡང་རྙོག་པའི་དུས་ཞེས་བྱ་བའི་ཚེ་ལོ་བཅུའམ་ཉི་ཤུ་ལས་མི་ཐུབ་པའི༌[^1108]བསྐལ་པ་ཆུང་ངུ་འབྱུང་བ་འབའ་ཞིག་ལ་རྙོག་པ་ཞེས་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1111]
དེ་བས་ན་བསྐལ་པ་འགྲིབ་པའི་ཚེ་སངས་རྒྱས་འཇིག་རྟེན་དུ་གཤེགས༌[^1109]ལ་བསྐལ་པ་སྐྱེ་བའི་ཚེ་འཁོར་ལོས་སྒྱུར་བའི༌[^1110]རྒྱལ་པོ་འབྱུང་ངོ་། །དེ་ལྟར་བསྐལ་པ་འགྲིབ་པའི་ཚེ་སངས་རྒྱས་གཤེགས་ལ་བསྐལ་པ་སྐྱེ་བའི་ཚེ་འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་འབྱུང༌[^1111]ན་ཅིའི་ཕྱིར་རྒྱལ་པོ་དུང་ཞེས་བྱ་བ་སངས་རྒྱས་བྱམས་པ་དང་ཅིག་ཅར་བྱུང་ལ་གལ་ཏེ་རབ་ཏུ་མ་བྱུང་ན་འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོར་འགྱུར་ཞིང་སངས་རྒྱས་མར་མེ་མཛད་ཀྱི་སྲས་བརྒྱད་ཅར་གླིང་བཞི་ལ་དབང་བར་འགྱུར་ཞེས་གསུངས།

[Block 1112]
ལན་བཏབ་པ་རྒྱལ་པོ་དུང་ཞེས་བྱ་བ་བསྐལ་པ་སྐྱེ་བའི་ཚེ་བྱུང་བ་ནི་བདེན་ན་ཚེ་རིང་བས་བྱམས་པ་དང་ཕྲད་པར་ཟད་ཀྱི་སངས་རྒྱས་བྱམས་པ་བསྐལ་པ་འགྲིབ་པའི་དུས་མ་ཡིན་པར་གཤེགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1113]
སངས་རྒྱས་རབ་ཏུ་བྱུང་ནས་འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོར་འགྱུར་ཞེས་བསྟན་པ་ཡང་ངེས་པར་ལུང་བསྟན་པ་མ་ཡིན་ནོ། །

[Block 1114]
སངས་རྒྱས་མར་མེ་མཛད་ཀྱི་སྲས་བརྒྱད་ཀྱང་སྔ་མ་དང་འདྲ་སྟེ། བསོད་ནམས་ཀྱི་སྐུ་ཡིན་པས་དེ་འདྲའི་སྐྱོན་མེད༌[^1112]དུ་ངེས་སོ། །

[Block 1115]
གསེར་གྱི་འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་ནི་བསྐལ་པ་ཡར༌[^1113]སྐྱེ་བའི་ཚེ་འཇིག་རྟེན་དུ་ངེས་པར་འབྱུང་གི །དངུལ་དང་ཟངས་དང་ལྕགས་ཀྱི་འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་འབྱུང་བའི་དུས་སུ༌[^1114]ནི་ངེས་པ་མེད་དེ། དེ་བས་ན་རྒྱལ་པོ་དྷརྨཱ་ཨ་ཤོ་ཀ་སངས་རྒྱས་མྱ་ངན་ལས་འདས་ནས་ལོ་བརྒྱ་ལོན་པའི་འོག་ཏུ་འབྱུང་ངོ་།། །།

[Block 1116]
དམ་པའི་ཆོས་པུཎྜ་རཱི་ཀའི་འགྲེལ་པ། བམ་པོ་བཞི་པ།

[Block 1117 [HEADING]]
###### **ཅིའི་ཕྱིར་བསྟན་པ།** ^4-2-10-2-1-2-0

[Block 1118]
མདོ་ལས་ཤཱ་རིའི་བུ་འདི་ལྟ་སྟེ་ཞེས༌[^1115]པ་ནས་ཐེག་པ་གསུམ་དུ་བཤད་དེ་བསྟན་ཏོ་ཞེས་པའི་བར་དུ་ནི་སངས་རྒྱས་རྙོག་པ་ལྔའི་དུས་སུ་ཅིའི་ཕྱིར་འབྱུང་བ་བསྟན་པའི་ཕྱིར་འདི་ལྟར་བསྐལ་པ་དང་། འཁྲུག་པའི་རྙོག་པ་དང་། དྲི་མ་མང་པོ་དང་བརྐམ་པའི༌[^1116]སེམས་ཅན་དགེ་བའི་རྩ་བ་ཆུང་བདག་ལ་བཅོམ་ལྡན་འདས་ཐབས་མཁས་པ་རྣམ་པ་གསུམ་དུ་སྟོན་ཏོ། །

[Block 1119]
མུ་གེའི་བསྐལ་པ་དང་མཚོན་གྱི་བསྐལ་པ་དང་ནད་ཀྱི་བསྐལ་བ་བྱུང་བའི་ཚེ། སེམས་ཅན་འཁྲུག་པའི་རྙོག་པ་དང་། དྲི་མ་མང་ཞེས་བྱའོ། །

[Block 1120]
དྲི་མ་ནི་རྙོག་པའམ་མི་གཙང་བའི་དོན་མང་པོ་ནི་གཞིག་དཀའ་བའི་དོན་ཏོ།[^1117] །དྲི་མ་ལ་རྣམ་པ་དྲུག་སྟེ། འཚེ་བ་དང་། ཁོན་དུ་འཛིན་པ་དང་། འཁྲུག་པ་དང་། གཡོ་དང་། བརྫུན༌[^1118]དུ་སྨྲ་བ་དང་། ང་རྒྱལ་དང་དྲུག་གོ། །

[Block 1121]
དེ་ལ་གང་། སེམས་ཅན་ལ་གནོད་པར་བྱེད་པ་དགའ་བ་ནི་འཚེ་བ་ཞེས་བྱའོ། །

[Block 1122]
ཁོང་ཁྲོ་བའི་དབང་གིས་ཞེ་ལ་འཛིན་པ་ནི་ཁོན་དུ་འཛིན་པ་ཞེས་བྱའོ། །

[Block 1123]
ཉེས་པས་རྐྱེན་བྱས་ཏེ། སྨྲེ་སྔགས་འདོན་པ་ནི་འཁྲུག་པ་ཞེས་བྱ་སྟེ། འདི་གསུམ་ནི་ཞེ་སྡང་གི་རང་བཞིན་ནོ། །

[Block 1124]
བདག་གི་ཉེས་པ་འཆབ་ཅིང་ཕ་རོལ་པོའི་སྐྱོན་རྟོག་པ༌[^1119]དང་གཞན་གྱི་ཡིད་དང་སྦྱོར་ཏེ་ཚུལ་འཆོས་པ་ནི་གཡོ་ཞེས་བྱའོ། །

[Block 1125]
བཀུར་སྟིའི༌[^1120]ཕྱིར་ཡོན་ཏན་སྒྱུས་སྟོན་པ་ནི་བརྫུན་ཞེས་བྱ་སྟེ་འདི་གཉིས་ནི་འདོད་ཆགས་དང་གཏི་མུག་གི་རང་བཞིན་ནོ། །
--- END BLOCKS ---
