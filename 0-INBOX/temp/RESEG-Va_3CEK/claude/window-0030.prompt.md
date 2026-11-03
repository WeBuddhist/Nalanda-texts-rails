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
དགེ་སློང་གིས་འབྱེད་ཀྱི་ཁྱིམ་པ་ཡང་མ་ཡིན་ལ། དགེ་སློང་མ་ལ་སོགས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1052]
དེ་ཡང་ལྟ་བ་སྤྱོད་པ་ཁོ་ནས་འབྱེད་ཀྱི་སྲེད་པ་སྤྱོད་པས་ནི་མ་ཡིན་ནོ། །

[Block 1053]
ཚུལ་དང་ལྡན་པས་འབྱེད་ཀྱི་ཚུལ་ཉམས་པས་ནི་མ་ཡིན་ཏེ། དེའི་ཚིག་མི་བཙན་པའི་ཕྱིར་རོ། །གང་དུ་འབྱེད་ཅེ་ན།

[Block 1054]
གང་ན་བཅོམ་ལྡན་འདས་མངོན་སུམ་དུ་བཞུགས་པ་དེ་ལས།

[Block 1055]
གཞན་དུའོ། །

[Block 1056]
དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་བཟོད་པར་དཀའ་བའི་ཕྱིར་དང་། བཀའ་སྩལ་པའི༌[^761]ཕྱིར་སྟོན་པ་མངོན་སུམ་དུ་བཞུགས་པ་ཉིད་དུ་དབྱེ་བར་མི་ནུས་སོ། །སུ་དག་ཅིག་འབྱེད་ཅེ་ན། བྱིས་པ་རྣམས། བྱིས་པ་རྣམས་ཁོ་ན་ཡིན་གྱི་འཕགས་པ་རྣམས་ནི་མ་ཡིན་ཏེ། ཆོས་མངོན་སུམ་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1057]
ཁ་ཅིག་ན་རེ་དེ་དག་ལས་ཀྱང་བཟོད་པ་ཐོབ་པ༌[^762]རྣམས་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །ཇི་ཙམ་གྱིས་ན་དགེ་འདུན་བྱེ་བ་ཡིན་ཞེ་ན། སྟོན་དང་ལམ་གཞན་ལ་བཟོད་པ། །བྱེ་བའོ།[^763] །གང་གི་ཚེ་དེ་དག་གིས་དེ་བཞིན་གཤེགས་པ་ལས་གཞན་པའི་སྟོན་པ་དང་དེས་བསྟན་པའི་ལམ་ལས་གཞན་པའི་ལམ་ལ་བཟོད་ན་དེ་ཙམ་གྱིས་དགེ་འདུན་བྱེ་བ་ཞེས་བརྗོད་དོ། །

[Block 1058]
བྱེ་ནས་དུས་ཇི་སྲིད་དུ་ཅིག་ཏུ༌[^764]འདུག་ཅེ་ན། དེ་ཉིད་ཀྱི་ནུབ་གཅིག་ཏུ་དེ་ནི་མི་གནས་སོ། །

[Block 1059]
དགེ་འདུན་དབྱེ༌[^765]ན་གདོན་མི་ཟ་བར་ནམ་མ༌[^766]ལངས་པ་ཉིད་དུ་དགེ་འདུན་སླར་འདུམ་པར་འགྱུར་རོ། །

[Block 1060]
དགེ་འདུན་གྱི་དབྱེན་དུ་བཤད་པ་གང་ཡིན་པ། དེ་ནི་འཁོར་ལོའི་དབྱེན་དུ་འདོད། །དེའི་ཚེ་ལམ་དུ༌[^767]འཇུག་པའི་བགེགས༌[^768]སུ་གྱུར་པའི་ཕྱིར་དེའི་ཚེ་བཅོམ་ལྡན་འདས་ཀྱི་ཆོས་ཀྱི་འཁོར་ལོ་ཡང་ཕྱེ་བ་ཡིན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་འཁོར་ལོའི༌[^769]དབྱེན་ཞེས་ཀྱང་བྱ་ལ། དགེ་འདུན་གྱི་དབྱེན་ཞེས་ཀྱང་བྱའོ། །

[Block 1061]
འཁོར་ལོའི་དབྱེན་ཡང་གང་ན་ཡོད་ཅེ་ན། འཛམ་བུའི་གླིང་ནའོ། །

[Block 1062]
གླིང་གཞན་དག་ན་ནི་མེད་དོ། །

[Block 1063]
དགེ་སློང་དུ་ཞིག་གིས་ཤེ་ན། དགུ་སོགས་ཀྱིས་དགུ་ལ་སོགས་པ་སྨོས་པས་ཡན་ཆད་ནི་མ་ངེས་སོ། །

[Block 1064]
དགེ་སློང་བརྒྱད་ནི་དགེ་འདུན་ཡིན་ནོ། །

[Block 1065]
དགུ་པ་ནི་འབྱེད་པ་པོ་ཡིན་ཏེ། གདོན་མི་ཟ་བར་དགེ་འདུན་ཕྱོགས་གཉིས་སུ་གནས་པར་འགྱུར་བ་དེ་ལྟ་བུ་ནི༌[^770]བྱེ་བ་ཡིན་ནོ། །

[Block 1066]
དགེ་འདུན་གྱི་དབྱེན་གཞན་ནི་ལས་ཀྱི་དབྱེན་ལས་འགྱུར་ཏེ། གལ་ཏེ་མཚམས་གཅིག་གི་ནང་དུ་མི་མཐུན་པས་ལས་དག་བྱེད་ནའོ། །

[Block 1067]
ལས་ཀྱི་དབྱེན་ནི་གླིང་གསུམ་ན༌[^771]ཡོད་དེ། གང་དག་ན་བསྟན་པ་ཡོད་པ་ཁོ་ན་ནའོ། །

[Block 1068]
དགེ་སློང་དུ་ཞིག་གིས་ཤེ་ན། དེ་ནི་བརྒྱད་དག་ཡན་ཆད་ཀྱིས་འཁོར་ལོའི་དབྱེན་ནི་དུས་དྲུག་དག་ཏུ་མི་འབྱུང་སྟེ། གང་དག་ཏུ་ཞེ་ན།

[Block 1069 [VERSE]]
དང་པོ་མཐའ་སྐྱོན་ཟུང་གཅིག་གི། །
སྔ་རོལ་ཐུབ་པ་ནོངས་པ་དང་། །
མཚམས་མ་བཅད་པ་དག་ཏུ་ཡང་། །
འཁོར་ལོའི་དབྱེན་ནི་མི་འབྱུང་ངོ་། །

[Block 1070]
དང་པོ་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་ནས་རིང་པོ་མ་ལོན་པ་དང་། ཐ་མ་བཅོམ་ལྡན་འདས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཚེ་དང་། གནས་སྐབས་དེ་གཉིས་སུ་ནི་དགེ་འདུན་ཤ་གཅིག་མ༌[^772]ཡིན་ནོ། །

[Block 1071]
བར་དུ་ཡང་སྐྱོན་མ་བྱུང་བའི་སྔོན་རོལ་དུ་འབྱེད་པར༌[^773]མི་འགྱུར་ཏེ། ཇི་སྲིད་དུ་བསྟན་པ་ལ་ཚུལ་ཁྲིམས་ཀྱི་སྐྱོན་དང་། ལྟ་བའི་སྐྱོན་མ་བྱུང་གི་བར་དུའོ། །

[Block 1072]
ཟུང་གཅིག་མ་བྱུང་བའི་སྔོན་རོལ་དུ་ཡང་དབྱེ་བར་མི་འགྱུར་ཏེ། ཇི་སྲིད་དུ་ཉན་ཐོས་ཀྱི་མཆོག་ཟུང་གཅིག་མ་བྱུང་གི་བར་དུ་སྟེ། བྱེ་བ་ཡོངས་སུ་མི་གནས་པའི་ཕྱིར་དང་། དེས་ཕྱིར་སྡུམ་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1073]
ཐུབ་པ་ནོངས་ན་ཡང་མི་འབྱུང་སྟེ། སྟོན་པ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ན་འགྲན་ཟླ་མེད་པའི་ཕྱིར་རོ། །

[Block 1074]
མཚམས་མ་བཅད་པ་དག་ཏུ་ཡང་སྟེ། ཇི་སྲིད་དུ་མཚམས་མ་བཅད་པར་མི་འབྱུང་སྟེ། མཚམས་གཅིག་གི་ནང་དུ་ཕྱོགས་གཉིས་སུ་གནས་པའི་ཕྱིར་བྱེ་བ་ཞེས་བྱའོ། །

[Block 1075]
དེ་ལྟར་ན་དུས་དྲུག་པོ་དེ་དག་ཏུ་འཁོར་ལོའི་དབྱེན་མི་འབྱུང་ངོ་། །ལས་ལ་རག་ལུས་པའི་ཕྱིར་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་འཁོར་ལོ་ལ་ཡང་དབྱེན་མི་འབྱུང་ངོ་། །

[Block 1076 [HEADING]]
### མ་བསད་པ་ལ་སོགས་པ་མཚམས་མེད་པ་ཡིན་པ། ^1-62-0

[Block 1077]
ཅིའི་ཕྱིར་མ་བསད་པ་ལ་སོགས་པ་མཚམས་མེད་པ་ཡིན་ལ་གཞན་ནི་མ་ཡིན་ཞེ་ན།

[Block 1078 [VERSE]]
ཕན་འདོགས་པ་དང་ཡོན་ཏན་ཞིང་། །
སྤངས་དང་མེད་པར་བྱས་ཕྱིར་རོ། །

[Block 1079]
རེ་ཞིག་ཕ་མ་གསད་པ༌[^774]ནི་ཕན་འདོགས་པ་མེད་པར་བྱས་པའི་ཕྱིར་རོ། །ཇི་ལྟར་དེ་གཉིས་ཕན་འདོགས་པ་ཡིན་ཞེ་ན། དེ་དག་ལས༌[^775]ལུས་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 1080]
དེ་དག་སྤངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། ཡོངས་སུ་བོར་བའོ། །

[Block 1081]
ཡོན་ཏན་གྱི་ཞིང་ཡིན་པའི་ཕྱིར་དགྲ་བཅོམ་པ་གསད་པ༌[^776]ལ་སོགས་པ་ཡང་མཚམས་མེད་པ་ཡིན་ནོ། །

[Block 1082]
གལ་ཏེ་ཕའམ་མ་མཚན་གྱུར་པ༌[^777]ན་ཡང་ལུས་གཅིག་པ་དེ་ལ་ནི། མཚན་ནི་གཞན་དུ་གྱུར་ཀྱང་འགྱུར། །དེ་ཉིད་ཀྱི་ཕྱིར་ཕ་ཡང་མ་ཡིན་དགྲ་བཅོམ་པ་ཡང་མ་ཡིན་པའི་སྐྱེས་པ་ཞིག་བསད་ན་མཚམས་མེད་པའི་ཁ་ན་མ་ཐོ་བས་རེག་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན། ཡོད་དེ། མ་མཚན་གྱུར་པས༌[^778]བསད་ན་མཚམས་མེད་པའི་ཁ་ན་མ་ཐོ་བས་རེག་པར་འགྱུར་རོ། །

[Block 1083]
མ་ཡང་མ་ཡིན་དགྲ་བཅོམ་པ་ཡང་མ་ཡིན་པའི་བུད་མེད་གཅིག་བསད་ན་མཚམས་མེད་པའི་ཁ་ན་མ་ཐོ་བས་རེག་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན། ཡོད་དེ། ཕ་མཚན་གྱུར་པས༌[^779]བསད་ན་མཚམས་མེད་པའི་ཁ་ན་མ་ཐོ་བས་རེག་པར་འགྱུར་རོ་ཞེས་བཤད་དོ། །

[Block 1084]
བུད་མེད་གཞན་ལས༌[^780]ནུར་ནུར་པོ་ཟགས་ནས་བུད་མེད་གཞན་གྱི་མངལ་དུ་བླུགས་ན་གང་ཞིག་བསད་ན་མཚམས་མེད་པར་འགྱུར་བ་དེའི་མ་གང་ཡིན་ཞེ་ན། གང་གི་ཟླ་མཚན་ལས་བྱུང་མ། །སེམས་ཅན་དེ་གང༌[^781]གི་ཟླ་མཚན་ལས་བྱུང་བ་དེ་ནི་དེའི་མ་ཡིན་ནོ། །

[Block 1085]
གཉིས་པ་ཡང་བྱ་བ་ཐམས་ཅད་ཁུ་བར༌[^782]བྱ་བ་ཡིན་ཏེ། དེ་ནི་ནུ་ཞོ་ལྡུད་པར་བྱེད༌[^783]པ་དང་། གསོ་བར་བྱེད་པ་དང་། སྐྱེད་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1086]
གལ་ཏེ་མ་ལ་སྦྱོར་བ་བྱས་ནས་གཞན་བསད་ན་ཡང་མཚམས་མེད་པར་མི་འགྱུར་ལ་མ་མ་ཡིན་པ་ལ་སྦྱོར་བ་བྱས་ནས་མ་བསད་ན་ཡང་མཚམས་མེད་པར༌[^784]འགྱུར་ཏེ། མ་ཁྲིའུའི་འོག་ན་འདུག་པ་བསད་པ་དང་། ཁྲུས་པའི་བུས་སྦྲང་བུ་ལ་སྦྱོར་བ་བྱས་པས་ཕ་བསད་པ་དཔེར་བྱའོ། །

[Block 1087]
མཚོན་ཐབས་གཅིག་གིས་མ་དང་གཞན་ཞིག་ཀྱང༌[^785]བསད་ན་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ནི་གཉིས་ཡིན་ལ། རྣམ་པར་རིག་བྱེད་ནི་མཚམས་མེད་པ་ཁོ་ན་ཡིན་ཏེ། ལས་དེ་སྟོབས་ཆེ་བའི་ཕྱིར་རོ། །

[Block 1088]
བཙུན་པ་དབྱངས་སྒྲོགས་ན་རེ་རྡུལ་ཕྲ་རབ་བསགས་པ་ཡིན་པའི་ཕྱིར་རྣམ་པར་རིག་བྱེད་ཀྱང་རྣམ་པ་གཉིས་སོ་ཞེས་ཟེར་རོ། །

[Block 1089]
དགྲ་བཅོམ་པ་མ་ཡིན་པའི་འདུ་ཤེས་ཀྱིས་དགྲ་བཅོམ་པ་བསད་ན་ཡང་མཚམས་མེད་པར་འགྱུར་ཏེ། འདི་གསད༌[^786]དོ་སྙམ་དུ་རྟེན་ངེས་པར་བཟུང་བའི་ཕྱིར་རོ། །

[Block 1090]
གང་ཞིག་གིས་ཕ་དགྲ་བཅོམ་པ་བསད་ན་ཡང་དེ་ལ་མཚམས་མེད་པ་ནི་གཅིག་ཁོ་ནར་འགྱུར་ཏེ། རྟེན་གཅིག་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
