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
བསྟི་སྟང་དུ་བྱས་པས་མ་ཐོས་པར༌[^938]སེམས་པ་དང་། བསྟི་སྟང་དུ༌[^939]མ་བྱས་པས་དམས་པར་སེམས་པ་ནི་ཉོན་མོངས་པ་སྟེ། བསྟི་སྟང་དུ་བྱས་ཀྱང་མཐོས་པར་མི་སེམས་ལ་བསྟི་སྟང་དུ་མ་བྱས་ཀྱང་དམས་པར་མི་སེམས་པ་ནི་ཉོན་མོངས་པ་ལ་བཏང་སྙོམས་པ་སྟེ། ལྷག་མ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 1087]
རྙེད་པ་རློམ་སེམས་མེད་ཅེས་བྱ་བ་ནི་ཆོས་གོས་དང་ལྷུང་བཟེད་ལ་སོགས་པ་རྙེད་ཀྱང་རྙེད་དོ་ཞེས་རློམ་སེམས་མེད་པའོ། །

[Block 1088]
སྙན་པ་ནི་བདག་གི་ཡོན་ཏན་ནོ། །

[Block 1089]
མི་སྙན་པ་ནི་སྐྱོན་བརྗོད་པའོ། །

[Block 1090]
བསྔགས་པ་ལ་ཆོས་ཉིད་རབ་ཏུ་གནས་ཞེས༌[^940]བྱ་བ་ལ། བསྔགས་པ་ནི་ཡོན་ཏན་དངོས་སུ་བརྗོད་པའོ། །

[Block 1091]
ཆོས་ཉིད་རབ་ཏུ་གནས་ཞེས་བྱ་བ་ནི་རང་བཞིན་མི་འགྱུར་བར་འདུག་ཅེས་བྱའོ། །

[Block 1092]
སྡུག་བསྔལ་དག་ལ་སོ་སོར་རྟོག་པའི༌[^941]སྟོབས་ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་བར་འགྱུར་བའི་དངོས་པོ་རྣམས་ཤེས་རབ་ཀྱིས༌[^942]དངོས་པོ༌[^943]མེད་པར་རྟོགས་པས༌[^944]དེ་ལ་ཇི་མི་སྙམ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1093]
བདེ་བ་དག་ལ་མི་རྟག་པ་དང་སྡུག་བསྔལ་བར༌[^945]རྟོག་པའི་སྟོབས་ཞེས་བྱ་བ་ནི་བདེ་བ་ཉིད་དུ་འགྱུར་ཞིང་མི་གནས་ཏེ། མཐར་སྡུག་བསྔལ་དུ་འགྱུར་བར་རྟོགས་པའི༌[^946]མཐུས་བདེ་བ་ལ་ཆགས་ཤིང་དྲེགས་པ་མེད་པའོ། །

[Block 1094]
རྗེས་སུ་ཆགས་པ་འདོར་ཞེས་པ་ལ་སོགས་པ་ལ། རྗེས་སུ་ཆགས་པ་དང་ཁོང་ཁྲོ་བའི་སེམས་ནི་ཉོན་མོངས་པ་སྟེ། དེ་གཉིས་ནི་མཛའ་བ༌[^947]དང་མི་མཛའ་བ༌[^948]ལས་འབྱུང་ན། དེ་གཉི་ག་ལ་འདྲ་བར་སེམས་མཉམ་པ་ནི་ཉོན་མོངས་པ་ལ་སེམས་བཏང་སྙོམས་པའོ། །

[Block 1095]
བློ་མཉམ་པ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་དང་ལྡན་པ་དང་ཚུལ་ཁྲིམས་འཆལ་བ་གཉིས་ལ་བསྟོད་པ་དང་སྨད་པའི་བསམ་པ་མེད་པ་དང་། བྱམས་པ་དང་ཁོང་ཁྲོ་བའི་བསམ་པ་མེད་པའོ། །

[Block 1096]
གཉིས་སུ་མི་བྱེད་པ་ཞེས་བྱ་བ་ནི་ལེགས་པར་བྱས་པ་དང་ཉེས་པར་བྱས་པ་གཉིས་ལ་འདིས་ནི་ཕན་བཏགས། [^949]འདིས་ནི་གནོད་པར་བྱས་སོ་ཞེས་ཐ་དད་པར་མི་སེམས་པའོ། །

[Block 1097]
སྡུག་པ་དང་མི་སྡུག་པར་མི་ལྟ་ཞེས་བྱ་བ་ནི་ཆགས་པར་འགྱུར་བའི་ཡུལ་དང་། ཆགས་པར་མི་འགྱུར་བའི་ཡུལ་གཉིས་ལ་སྡུག་པ་དང་མི་སྡུག་པར་མི་ལྟ་བ༌[^950]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1098]
ལེགས་པ་ཐོས་པ་དང་ཉེས་པར༌[^951]ཐོས་པ་ཞེས་སྨོས་པ་དང་། ལེགས་པར་སྨྲས་པ་དང་ཉེས་པར་སྨྲས་པ་ཞེས་སྨོས་པ་གཉིས་ལ། ཐོས་པ་ནི་ཉིད་ནས་བརྒྱུད༌[^952]དེ་སྤྱོས་ཤིང་བསྟོད་པ་ཐོས་པའོ། །

[Block 1099]
སྨྲས་པ་ནི་མངོན་སུམ་དུ་སྤྱོས་ཤིང་བསྟོད་པའོ། །

[Block 1100]
མི་བརྗེད་པ་དང་བག་ལ་ཉལ་བར་བྱེད་པ་གཉིས་དོན་གཅིག་སྟེ། དེ་གཉི་ག་ལ་ཡང་ཇི་སྙམ་དུ་འདོར་བའོ། །

[Block 1101]
ཁ་གཅིག༌[^953]ལས་བག་ལ་ཉལ་མེད་ཅེས་འབྱུང་སྟེ། དེའི་དོན་ཀྱང་དགའ་བར་འཛིན་པ་དང་། ཁོན་དུ་འཛིན་པ་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1102]
རོ་མྱང་བའི་ཉེས་དམིགས་རྣམས་ལ་མཚུངས་པར་ཡོངས་སུ་འཇལ་ཞེས་བྱ་བ་ནི་རོ་མྱང་བའི༌[^954]བདེ་བ་དང་། དེ་དང་བྲལ་བའི་ཚེ་ཉེས་དམིགས་མི་དམིགས་མི་བདེ་བ་གཉི་ག་ལ་མཚུངས་པར་རྟོག་པའོ། །

[Block 1103]
སེམས་ཅན་ཐམས་ཅད་ལ་བསམ་པ་མཉམ་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་འདྲ་བར་སེམས་པའོ། །

[Block 1104]
ལུས་དང་སྲོག་ལ་མི་ལྟ་ཞེས་བྱ་བ་ནི་ལུས་དང་སྲོག་ལ་ཕངས་སུ་བཟུང་ན་དེའི་རྐྱེན་གྱིས༌[^955]ཆགས་པ་དང་ཞེ་སྡང་བའི་ཉོན་མོངས་པ་འབྱུང་བས་ལུས་དང༌[^956]སྲོག་ལ་ཕངས་པར་མི་འཛིན་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1105]
རབ་དང་འབྲིང་དང་ཐ་མ་རྣམས་ལ་འོད་ཟེར་མཉམ་ཞེས་བྱ་བ་ནི་ཐེག་པ་གསུམ་གྱི་སེམས་ཅན་ལ་ཡང་རབ་འབྲིང་དུ་མི་ལྟ་བའི་འདྲ་བར་ལྟ་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1106]
བསྔགས་པ༌[^957]དང་བསྔགས་པ་མ་ཡིན་པ་རྣམས་ལ་སེམས་མཉམ་ཞེས་བྱ་བ་ནི་བསྟོད་པ་དང་སྨད་པ༌[^958]གཉི་ག་ལ་ཡང་དགའ་བ༌[^959]དང་མི་དགའ་བར༌[^960]འཛིན་པའོ། །

[Block 1107]
བདེ་བ་དང་མི་བདེ་བ་རྣམས༌[^961]ལ་རང་གི་སེམས་ཡོངས་སུ་དགའ་བ་ཞེས་བྱ་བ་ནི་བདག་གི་སེམས་གཡོ་སྒྱུ་མེད་དེ་དེ་དག་ལ་དྲང་པོར་སྨྲས་པ་དང་དྲང་པོར་མ༌[^962]སྨྲས་པ་གཉི་ག་ལ་ཡང་དྲང་པོ་དང་བདེན་པར་སྨྲ་བར༌[^963]འཛིན་པའོ། །

[Block 1108]
ཉོན་མོངས་པ་ལ་བཏང་སྙོམས་པའི་དོན་བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^964]ཏིའི་བུ་དེ་ལྟར་གང་བསྟི་སྟང་དུ་བྱས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། གང་བསྟི་སྟང་དུ་བྱེད་ཅིང་བསྟི༌[^965]སྟང་དུ་བྱས་པས༌[^966]ཀྱང་མཐོས་པར་མི་སེམས། གནོད་པར་བྱེད་ཅིང་གནོད་པར་བྱས་པ༌[^967]ལ་ཡང་དམས་པར་མི་སེམས་ཏེ། བཏང་སྙོམས་པར་འཇོག་པ་ནི་ཉོན་མོངས་པ་ལ་བཏང་སྙོམས་པ་ཞེས་བྱའོ། །

[Block 1109 [HEADING]]
##### བདག་དང་གཞན་བསྲུང་བའི་བཏང་སྙོམས། ^2-4-2-2-0

[Block 1110]
བདག་དང་གཞན་སྲུང་བའི༌[^968]བཏང་སྙོམས་བསྟན་པའི་ཕྱིར། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བདག་དང་གཞན་བསྲུང་བ༌[^969]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 1111]
ཁོང་ཁྲོ་བར་མི་བྱེད་ཅིང་མི༌[^970]ཚོལ་ཏེ་ཞེས་བྱ་བ་ནི་གཞན་གྱིས༌[^971]ཡན་ལག་དང་ཉིང་ལག་ལ་སོགས་པ་གཅད༌[^972]ཀྱང་གཞན་ལ་ཞེ་སྡང་ཡང་མི་སྐྱེ། མི་གཅད་པའི༌[^973]ཐབས་ཚོལ་ཞིང་གསོལ་བ་ཡང་མི་འདེབས་ཏེ།[^974] དེ་ལྟར་ཞེ་སྡང་མ་སྐྱེས་ཤིང་མི་གཅོད་པའི་ཐབས་མི་ཚོལ་བས་བདག་གི་སེམས་མ་འཁྲུགས་པས༌[^975]བདག་སྲུང༌[^976]བའོ། །

[Block 1112]
ཁོང་ཁྲོ་མ་སྐྱེས་ཏེ་གཞན་གྱི་སེམས་མ་འཁྲུགས་པ༌[^977]ནི་གཞན་བསྲུང་བའོ། །

[Block 1113]
ལུས་ཀྱི༌[^978]རྣམ་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་ལུས་ཀྱིས༌[^979]ཉེས་པར་བྱས་པ་ཞེས་བྱ་བའི་ཐ༌[^980]ཚིག་སྟེ། དེ་བཞིན་དུ་ངག་གི་རྣམ་པར་འགྱུར་བའང་རིག་པར་བྱའོ། །

[Block 1114]
མིག་གི་རྣམས་ཀྱང་རྨ་མི་ཕྱིན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི། མིག་ལ་སོགས་པའི་དབང་པོ་རྣམས་དང་། གཟུགས་ལ་སོགས་པའི་ཡུལ་རྣམས་ཀྱི་དབང་དུ་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1115]
རྨ་མི་ཕྱིན་ཞིང་ཉམས་པ་མེད་པ་ཞེས་བྱ་བ་ནི་ཞེ་སྡང་གིས༌[^981]མི་ཚུགས་ཤིང་ཞེ་སྡང་གི་དབང་དུ་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1116]
རྨ་ཕྱུང་བ་ལ་རྨ་མི་འབྱིན། །ཞེས་བྱ་བ་ནི་ཕས་གནོད་པར་བྱས་ཀྱང་སླར་གནོད་པ་མི་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1117]
ཕན་པར་བྱེད་པ་དང་གནོད་པར་བྱེད་པ་ལ་མཉམ་ཞེས་བྱ་བ་ནི་ཕན་འདོགས་པར་སེམས་པ་དང་། གནོད་པར་བྱ་བར་སེམས་པ་གཉིས་ལ་བྱམས་པར་བྱ་བ་དང་གནོད་པར་བྱ་བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1118]
བཏང་སྙོམས་ནི་མཆོག་ཏུ་རྩོད་པ་མེད་པ་ཞེས་བྱ་བ་ནི་ཉེས་པར༌[^982]བྱས་ཤིང་མི་སྙན་པར་སྨྲས་པ་ལ་ཇི་མི་སྙམ་སྟེ།[^983] མི་རྩོད་པས་མཆོག་ཏུ་རྩོད་པ་མེད་པའོ། །

[Block 1119]
བཏང་སྙོམས་ནི་རང་གི་སེམས་ལ་ངེས་པར་རྟོག་པའོ་ཞེས་བྱ་བ་ལ་ཆོས་ཐམས་ཅད་སེམས་ལས་བྱུང་བར་ཡང་དག་པར་རྟོགས་ཤིང་གཏན་ལ་འབེབས༌[^984]པས་ཕྱི་རོལ་དུ་མི་འབྲང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1120]
ཡང་ན་རང་གི་སེམས་ལ་ངེས་པར་རྟོག་ཅེས་བྱ་བ་ནི་བདག་གི་སེམས་ཞེ་སྡང་གི་དབང་དུ་མི་གཏོང་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1121]
བཏང་སྙོམས་ནི་གཞན་གྱི་སེམས་སྲུང་བའོ༌[^985]ཞེས་བྱ་བ་ནི་གཞན་གྱི་སེམས་འཁྲུག་པར༌[^986]མི་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1122]
བཏང་སྙོམས་ནི་བདག་ལ་རྟོག་པའོ་ཞེས་བྱ་བ་ནི་གཞན་གྱིས༌[^987]གནོད་པ་བྱས་ཀྱང་བདག་གི་ལས་ལ་རྟོག་གི་གཞན་ལ་ཁོན་དུ་མི་འཛིན་པའོ། །

[Block 1123]
བཏང་སྙོམས་ནི་སེམས་ཅན་གཞན་དག་ལ་གནོད་པ་མེད་པའོ༌[^988]ཞེས་བྱ་བ་ནི་གནོད་པ་ཐམས་ཅད་བདག་གི་ལས་ལས་བྱུང་བར་རྟོགས་པས༌[^989]སེམས་ཅན་གྱིས༌[^990]མ་ཉེས་པར་ཤེས་པའི་ཕྱིར་སེམས་ཅན་གྱིས༌[^991]གནོད་པར་བྱེད་པས་སེམས་ཅན༌[^992]ལ་གནོད་པར༌[^993]མི་བྱེད་པའོ། །

[Block 1124]
བདག་དང་གཞན་བསྲུང་བའི་བཏང་སྙོམས་བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། བཏང་སྙོམས་ནི་བྱང་ཆུབ་སེམས་དཔའི་མཉམ་པར་གཞག༌[^994]པའི་གནས༌[^995]སྐབས་ཡིན་ཏེ་ཞེས་བྱ་བ་གསུངས་ཏེ། མཉམ་པར་གཞག་པ་ནི་ཆགས་པ་དང་ཁོང་ཁྲོ་བ་མེད་པར་བྱའོ། །

[Block 1125]
དེ་ལྟར་མཉམ་པར་གཞག་པའི་གནས་སྐབས་ནི་བཏང་སྙོམས་ཡིན་པས་དེ་བས་ན་བཏང་སྙོམས་ནི་མཉམ་པར་གཞག་པའི་གནས་སྐབས་སོ། །
--- END BLOCKS ---
