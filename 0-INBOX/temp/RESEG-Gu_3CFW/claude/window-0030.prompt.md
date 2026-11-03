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
[Block 1051]
གཞན་པ་གཅིག་ཏུ་གནས་པ་ཁས་བླངས་པ་ལ་ནི་ཡུན་རིང་བ་ཉིད་ཀྱིས༌[^898]རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་ལ། གཞན་པ་གཅིག་ཏུ་གནས་པར་ཁས་བླངས་པ་ལ་ཞེས་བྱ་བ་ནི་མནན་པའི་རྫས་མེད་པར་ཁས་བླངས་པ་ཞེས་གཞན་ལ་ཐ་དད་པར་ཁས་བླངས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1052]
དེ་དུས་ཡུན་རིང་དུ་གནས་པ་ཉིད་ཀྱིས་རྣམ་པར་གཞག་གོ།[^899] །གང་དུ་ཡུན་རིང་བར་གནས་པ་དེ་ཉིད་ལ་རྙེད་པ་འདི་སྦྱིན་པར་བྱའི་གཞན་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1053]
འདིར་གཞུང་ནི་གནས་མལ་གྱི་གཞི་ལས།

[Block 1054]
ཚེ་དང་ལྡན་པ་ཉེ་དགས་རྙེད་པ་འདོད་པས་གཙུག་ལག་ཁང་གཉིས་སུ་ཚུལ་ཤིང་དང་གནས་མལ་བླངས་ཏེ། གནས་མལ་ཁས་བླངས་པ་ན་དེས་གནས་གཙུག་ལག་ཁང་གཅིག་ནས་ཆོས་གོས་ཀྱི་རིན་ཐོབ་ལ། ཅིག་ཤོས་ནས་མ་ཐོབ་ནས།[^900] དེ་ནས་རྙེད་པ་སྒྲུབ་པ༌[^901]ན། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གང་དུ་གང་གསོ་སྦྱོང་ལན་མང་དུ་བྱས་པ་དེ་ནས་རྙེད་པ་བླང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1055]
དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་ནི་རྙེད་པ་ལ་སུམ་ཆ་དབྲི་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། སུམ་ཆ་དབྲི་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སུམ་ཆ་དེ་ཆ་ཉིད་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1056]
ཟས་ལ་ནི༌[^902]མཉམ་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། མཉམ་པ་ཉིད་ནི་འདིར་ཆ་ཐོབ་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1057]
ཟང་ཟིང་གི་རྙེད་པ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་གྲགས་སོ། །

[Block 1058]
དེ་བས་ན་འདིར་མཉམ་པ་ཉིད་ཐོབ་པ་ལ་གསལ་བར་བྱ་བའི་ཕྱིར་མཉམ་པ་ཞེས་སྨོས་པར་རིག་པར་བྱའོ། །

[Block 1059]
བསྙེན་པར་རྫོགས་པར་འདོད་པ་དང་དགེ་སློང་མ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ་ནི་རྣམ་པ༌[^903]ཉིད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1060]
བསྙེན་པར་རྫོགས་པར་འདོད་པ་ཞེས་བྱ་བ་སྨོས་པ་ནི་དགེ་ཚུལ་ཡང་བསྡུས་པའོ། །

[Block 1061]
དེ་མེད་ན་དགེ་ཚུལ་མ་ལ་བསྙེན་པར་རྫོགས་པར་བྱར་མེད་པའི་ཕྱིར་རོ། །

[Block 1062]
འདི་ནི་ཐམས་ཅད་ཀྱི་དོན་དུ་ཡིན་གྱི། ཡང་འདོད་པའི་དོན་དུ་ནི་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 1063]
འདིར་གཞུང་ནི་སིལ་བུ་དག་ལས།

[Block 1064]
དགེ་སློང་དང་དགེ་སློང་མ་དག་གིས་སྐལ་བ༌[^904]མཉམ་པར་སྦྱིན་ནོ། །

[Block 1065]
དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་དག་ལ་ནི་སུམ་གཉིས་སྦྱིན་ནོ། །

[Block 1066]
བསྙེན་པར་རྫོགས་པར་འདོད་པ་དང་། དགེ་སློང་མ་དག་ཀྱང་མཉམ་པར་སྦྱིན་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1067]
དགེ་སློང་དང་དགེ་སློང་མ་རྣམས་ཀྱི༌[^905]སྐལ་བ་བགོ་བ་ནི་གང་ཟག་ལས་ནི་ཡིན་གྱི་དགེ་འདུན་ལས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཟག་འདི་སྙེད་ནི་དགེ་སློང་གི་དགེ་འདུན་ལ་དབུལ་ལོ། །

[Block 1068]
འདི་སྙེད་ཅིག་ནི་དགེ་སློང་མའི་དགེ་འདུན་ལ་དབུལ་ལོ་ཞེས་བྱ་བ་དེ་ལྟར་བྱེ་བྲག་ཏུ་མ་བྱས་པ་རྙེད་པ་ནི་དགེ་འདུན་གཉིས་ལ་བརྟེན་ནས་ཕུལ་བ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 1069]
འདིར་གཞུང་ན༌[^906]མགོའི་ཤས་ཀྱིས་བགོ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། ཟས་ཀྱི༌[^907]མཇུག་ཐོགས་ཀྱི་རྙེད་པ་བྱེ་བྲག་ཏུ་མ་བཅད་པ་ལ༌[^908]དེ་ལ་དགེ་སློང་མ་ཟོས་པ་ཉིད་དག་ཀྱང་མི་འཇུག་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ཟས་ཀྱི༌[^909]མཇུག་ཐོགས་ཞེས་བྱ་བ་ནི་ཟས་སྔར་བཅུག་པ་དང་ལྷན་ཅིག་རུང་འདི་དགེ་སློང་ཁོ་ན་ལ་འབུལ༌[^910]ལོ་ཞེས་སྦྱིན་བདག་གིས༌[^911]བྱེ་བྲག་ཏུ་མ་བཅད་པའི་ཟས་དེ་ལྟ་བུའི་རྙེད་པ་དེ་དག༌[^912]ལ་ནི་དེར་ཟན་ཟོས་པའི་དགེ་སློང་མ་རྣམས་ཀྱང་མི་དབང་བ་མ་ཡིན་ཏེ་དེ་རྣམས་ལ་ཡང་རྙེད་པ་དབུལ་བར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1070]
འདིར་ལུང་ནི་དགེ་སློང་དྲུག་ཅུ་རྣམས་བཟའ་བའི་ཕྱིར་ཞུགས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་སྟོང་ཉིས་བརྒྱ་ལྔ་བཅུའི་དགེ་སློང་གི་དགེ་འདུན་དང་བཅས་པ་དང་། དགེ་སློང་དྲུག་ཅུ་ཡང་རི་བྲགས་དེ་ཉིད་དུ་ལྷགས་ནས། དེ་དག་ཀྱང་ཟན་ཟོས་ནས་རྙེད་པ་ཐོབ་པ་ཉིད་ཅེས་གསུངས་སོ། །

[Block 1071]
སྟན་དང་ཆུ་དང་བསོད་སྙོམས་དག་ལ་དགེ་སློང་དང༌[^913]དགེ་སློང་མ་དག་པས་གཙོ་བོ་ཉིད་མ་ཡིན་པ་མ་ཡིན་ནོ། །

[Block 1072]
དགེ་སློང་མ་རྣམས་ཀྱི༌[^914]ཚོགས་པ་ནི་རྒན་པའི་མཐར་སྟན༌[^915]དག་གཞག་གོ་ཞེས་བྱ་བ་ལ་འདི་ནི་བརྒྱ་ལམ་ན་དགེ་སློང་འགའ་ཞིག་འོང་སྲིད་པར་འགྱུར་བས་དེའི་ཕྱིར་དེ་མདོར་བྱས་སོ། །

[Block 1073]
དགེ་སློང་དང་བཅས་པ་ཉིད་ནི་དེ་དག་གིས་མི་ནུས་ན་དགེ་སློང་མས་ཡོན་བཤད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དགེ་སློང་དང་བཅས་པ་ཉིད་ན་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་ལ་ཡོན་བཤད་པར་བྱའོ་ཞེས་སྨོས་པར་རིག་པར་བྱའོ། །

[Block 1074]
དེ་དག་གིས་ཞེས་བྱ་བ་ནི་དགེ་སློང་རྣམས་ཀྱིས་སོ། །

[Block 1075]
འདྲིམ༌[^916]པར་བྱེད་པས་སྦྱིན་པའི་ཕྱིར་ཟས་ཉེ་བར་གཞག་པ་ནི་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས༌[^917]དང་པོར་སྙོམས་པར་བྲིམས་ཤིག་ཅེས་བསོ་བར༌[^918]བྱ་བ་ནི་དང་པོར་ཞེས་བྱ་བ་ནི་ཐོག་མར་རོ། །

[Block 1076]
སྦྱིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་བརྩོན་འགྲུས་བརྩམས༌[^919]པའོ། །

[Block 1077]
བརྩོན་འགྲུས་དེ་ཉིད་ཀྱང་སྨོས་ན་སྐྱོན་དུ་མི་འགྱུར་བ་ཉིད་དོ། །

[Block 1078]
དང་པོར་མ་སྨྲས་ན་དེའི་འོག་ཏུ་སྨྲ་བར་བྱ་བ་ཉིད་ཡིན་ཏེ་དེའི་ཚེ་ཡང་མ་སྨྲས་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 1079]
འཁོར་ལ་བལྟས་ཏེ་མང་ལ་ཟས་སུ་ཉུང་བ་ཉིད་ཡིན་ནོ།[^920] །དེའི་ཚེ་སྔ་མ་བརྗོད་ཅིང་ཇི་ལྟར་ཁྱེད་པར་བྱའོ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་ཁྱེད་པར་ཞེས་སོ་ཞེས་བྱ་བ་ནི་སྙོམས་པར་བྲིམས་ཤིག་ཅེས་བསྒོ་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1080]
འཁོར་ལ་བལྟས་ཏེ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1081]
གཞན་དག་འོངས་པ་ལ་ནི་འདི་གསུངས་སོ། །

[Block 1082]
གོ་རིམས་བཞིན་དུ་བོས་པ་ལ་དུས་གཞན་དུ་ཡང་འདི་མཐོང་བ་དང་ཐོས་པ་ལ་བཟའ་བའི་ཚད་ཀྱི་བློ་སྐྱེས་པ་ལ་ཟས་ཉུང་བ་ཉིད་དང་ལྷགས་པའི་དོགས་པ་བྱ་བ་ཉིད་རྣམ་པར་གནས་པ་ཡིན་ཞེས་བྱ་བ་བྱེ་བྲག་མེད་པར་སྨོས་སོ། །

[Block 1083]
མང་ལ་ཞེས་བྱ་བ་ནི་འཁོར་གྱི་རྫས་རྣམས་མང་བ་ལའོ། །

[Block 1084]
ཟས་ཉུང་བ་ཉིད་ཡིན་ན་ཞེས་བྱ་བ་ནི་གལ་ཏེ་མཐོང་བའི་ལམ་ན་ཉེ་བར་སྡུད་པའོ། །

[Block 1085]
འདིར་མཐོང་བ་ལས་ཡོངས་སུ་ཚང་བར་འགྲུབ་པའོ།[^921] །གལ་ཏེ་མ་ཡིན་ན་ཐོས་པ་དང་དོགས་པ་དང་བཅས་པ་ལ་སྤྱོད་པའམ། ཡིད་གཉིས་སམ་ཐོས་པ་ལ་ཐེ་ཚོམ་བརྗོད་པ་དང་བཅས་པ་ཉིད་དོ། །

[Block 1086]
དགེ་སློང་དག་མང་ལ་ཟས་ཉུང་གི༌[^922]ཇི་ལྟར་ཁྱེད་པར་བྲིམས་ཤིག་ཅེས་བསྒོ་བར་བྱའོ། །

[Block 1087]
འོན་ཏེ་དགེ་སློང་དག་ཉུང་ལ་ཟས་དག་མང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་བརྗོད་ཅིང་ཅི་འབྱོར་པ་བྲིམས་ཤིག་ཅེས་བསྒོ་བར་བྱའོ། །

[Block 1088]
ཟས་ཉུང་བ་ཉིད་དུ་ངེས་པ་ལས་ཟས་ཉུང་བ་ཉིད་དམ་མང་བ་ཉིད་མ་ཡིན་ན་དེའི་ཚེ་སྔ་མ་བརྗོད་ཅིང་དེའི་འཁོར་གྱི་རྫས་མང་བ་ཉིད་དམ་ཉུང་བ་ཉིད་ནའོ། །

[Block 1089]
དེའི་དོན་ནི་འདི་ཡིན་ཏེ། འཁོར་གྱི་རྫས་མང་བ་ཉིད་དང་ཟས་ཉུང་བ་ཉིད་ཡིན་ན་དེའི་ཚེ་སྔ་མ་བརྗོད་པ་ནི་བྲིམས་ཤིག་ཅེས་བྱ་བ་བསྒོ་བའོ། །

[Block 1090]
ཟས་འགོད་པར་བྱེད་པ་པོ་ཉེ་བར་འགོད་པས་དང་པོར་དགེ་འདུན་གྱི་གནས་བརྟན་པར་གསོལ་བར་བྱའོ། །
--- END BLOCKS ---
