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
དཔེ་ནི་ཡང་དག་པའི་དེ་བཞིན་གཤེགས་པ་ཡོད་ལ། དེའི་ཕྱིར་ཡང་དག་པ་ལས༌[^749]ཡང་དག་པ་མ་ཡིན་པའམ། ཡང་དག་པའི་སྤྲུལ་པ་འབྱུང་བར་འགྱུར་རོ་ཞེས་རིགས་སོ། །

[Block 1052]
འདིར་ཡང་དག་པའི་དངོས་པོ་མེད་ན་གང་ཞིག་སྤྲུལ་ནུས་པའི་བྱེད་པ་པོ་འཇུག་པའི་རྒྱུ་མཚན་ཉིད་དུ་རྟོགས་པར༌[^750]བྱེད་དེ། དེའི་ཕྱིར་དཔེ་དང་མི་འདྲའོ། །

[Block 1053]
སྨྲས་པ། གང་འདིར་ཡང་དག་པའི་དེ་བཞིན་གཤེགས་པ་ཡོད་དོ་ཞེས་མངོན་པར་འདོད་ན། དེ་བྱེད་པ་པོར་གྱུར་པའམ༌[^751]ལས་སུ་གྱུར་པའི་ཡང་དག་པ་ཉིད་དུ་ཡོངས་སུ་རྟོགས། [^752]གལ་ཏེ་རེ་ཞིག་བྱེད་པ་པོར་གྱུར་པར་ཡོངས་སུ་རྟོགས༌[^753]ན། དེ་ཡང་། ཡང་དག་པའི་དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་མ་ཡིན་ཏེ། བྱེད་པ་པོའི་ཕྱིར་སྤྲུལ་པའི་བྱེད་པ་པོ་དེ་བཞིན་གཤེགས་པའི༌[^754]སྤྲུལ་པ་བཞིན། ཡང་ན་ལས་སུ་གྱུར་པས་ཡང་དག་པར་ཡོངས་སུ་རྟོགས༌[^755]ན། དེ་ལྟ་ན་ཡང་སྤྲུལ་པ་ནི་སྤྲུལ་པས་སྤྲུལ་པ་བཞིན་འདི་ལ་ཡང་དག་པར་བརྗོད་པར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1054]
ངེས་པར་དེ་བཞིན་གཤེགས་པ་ཡང་མེད་དམ་ཅི་ཞེ་ན། སུ་ཞིག་འདི་སྐད་དུ་ཡོད་པའམ་མེད་དོ་ཞེས་སྨྲ། གང་ཞིག་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བ་རང་བཞིན་དུ་རྟོགས༌[^756]ན་དེ་ནི་དེ་ལ་ཡོད་པའམ་མེད་པར་ཡོངས་སུ་རྟོགས་པར༌[^757]བྱེད་ན། གང་ཡང་རང་བཞིན་མེད་པ་སྟེ་དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་བཞིན་དུ༌[^758]རྟོག་པ་མེད་པ། སྤྲུལ་པ་བཞིན་དུ་རང་བཞིན་གྱིས་ཞི་བ་ངོ་བོ་ཉིད་ཀྱིས་མ་སྐྱེས་པས་དེ་ལ་ཡོད་པའམ་མེད་པར་བརྟག་པར་མི་བྱའོ། །

[Block 1055]
དེ་ན༌[^759]དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་གྲུབ་པ་མེད་པས་དཔེ་དང་མི་འདྲ་བར་རྟོག་པར་ག་ལ་བྱེད། འདིར་སྨྲས་པ། གང་འདི་སྐད་དུ་སྨྲས་པའི་སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་མེད༌[^760]པས། གང་ཅུང་ཟད་ཡོད་པ་རྟོག་པ་ཙམ་ཞེས་པས། སླར་ཡང་ཅིའི་ཕྱིར་ན་འདི་དག་ཀྱང་རང་བཞིན་མེད་པ་དང་རྟོག་པ་ཙམ་དུ་ཡོད་པ་གཉིས་ཁས་ལེན་པར་བྱེད། གལ་ཏེ་སླར་ཡང་རང་བཞིན་ཡོད་པ་ཉིད་པས། རྟོག་པ་ཙམ་གྱི་དངོས་པོར་ཁས་མི་ལེན་ན། དེའི་ཚེ་སྐྱོན་ཅིར་འགྱུར་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་རང་བཞིན་ཡོད་པར་གྱུར་ན། དེའི་ཚེ་མྱ་ངན་ལས་འདས་པ་མེད་པར་འགྱུར་ལ། ཡོད་བཞིན་པ་ལ་བྱེད་པ་པོ་དོན་མེད་པའི་ཕྱིར་དང་། བྱེད་པ་པོ་ཡང་མེད་པར་འགྱུར་རོ། །

[Block 1056]
གལ་ཏེ༌[^761]རྟོག་པ་ཙམ་ཡང་མེད་པར་འགྱུར་ན། དེའི་ཚེ་ལས་ཀྱི་འབྲས་བུ་མེད་པས་ལོག་ལྟར་འགྱུར་ལ། དེས་ན་རང་བཞིན་ཁས་བླང་བར་མི་བྱ་ཞིང་། རྟོག་པ༌[^762]ཁས་མི་བླང་བར་ཡང་མི་བྱའོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1057 [HEADING]]
### ཚིགས་བཅད་ཞེ་གསུམ་པ། ^1-43-0

[Block 1058]
ལས་ཀྱི་རང་བཞིན་ཡོད་ཅེ་ན།

[Block 1059 [VERSE]]
མྱང་འདས་བྱེད་པོ་ལས་ཀྱང་མེད། །
གལ་ཏེ་མེད་ན་ལས་བསྐྱེད་པའི། །
འབྲས་བུ་སྡུག་དང་མི་སྡུག་མེད། །

[Block 1060]
གལ་ཏེ་ལས་ཀྱི་རང་བཞིན་ཡོད་ན། དེའི་ཚེ་དེ་རང་བཞིན་གྱིས་ཡོད་བཞིན་པའི་ཕྱིར་སླར་ཡང་གཞན་དུ་འགྱུར་བ་མེད་དོ་ཞེས་བྱའོ། །

[Block 1061]
གང་འདི་ལྟར་མྱ་ངན་ལས་འདས་པ་ལས་དང་ཉོན་མོངས་པ་ཟད་པ་ལས་རྣམ་པར་གཞག་ལ། དེ་མི་འབྱུང་བར་འགྱུར་བ་དང་། ལས་དེ་ཡང་བྱེད་པ་པོ་ལ་མི་ལྟོས་པར་འགྱུར་ལ། དེ་ལྟ་ན༌[^763]རྒྱུ་མེད་པའི་ཕྱིར་འདི་ནི་ཡོད་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 1062]
རེ་ཞིག་ལས་ལ་རང་བཞིན་ཡོད་པར་གྱུར་ན། སྐྱོན་འདི་དག་སྟེ་དེའི་ཕྱིར་ལས་ལ་རང་བཞིན་མེད་པའོ། །

[Block 1063]
གལ་ཏེ་གང་ཅི་ཡང་རུང་བ་རྟོག་པ་ཙམ་དུ་མི་འགྱུར་ན། དེའི་ཚེ་ལས་ཀྱིས་བསྐྱེད་པའི་སྡུག་པའམ་མི་སྡུག་པར་མི་འགྱུར་ལ། དགེ་བ་དང་མི་དགེ་བ་དག་གི་ལས་ཀྱིས༌[^764]སྡུག་པ་དང་མི་སྡུག་པ་དག་ཀྱང་ཡོད་པས། དེའི་ཕྱིར་འདི་དག་གང་ཅི་ཡང་རུང་རྟོག་པ་ཙམ་དུ་ཡོད་དོ་ཞེས་གནས་སོ། །

[Block 1064]
གང་ཡང་འདི་ལས་ཀྱི་རང་བཞིན་ནི་མེད་ལ་གང་ཅུང་ཟད་རྟོག་པ་ཙམ་ཡོད་པས། དེ་ཉིད་ཀྱིས༌[^765]ཤིན་ཏུ་ཐ་དད་པའི་སྤྱོད་པའི་འདུས་བྱས༌[^766]སྐྱེ་བོའི་རྗེས་སུ་འབྲང་བའི་བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པས། ཉོན་མོངས་པ་དང་རྗེས་སུ་མཐུན་པའི་གཉེན་པོའི་དངོས་པོར་འཇུག་པ་ཕན་ཚུན་དུ་འགལ་བས། བརྗོད་པའི་ཚིག་ཀྱང་ཆོས་ཉིད་དང་མི་འགལ་བར་གནས་སོ། །

[Block 1065]
འདི་ལྟར་ལས་ཡོད་དོ་ཞེས་བྱ་བའི་ཚིག་མེད་དོ་ཞེས་བྱ་བའི་ཚིག་དང་འགལ་བ་མེད་དོ་ཞེས་བྱ་བའི་ཚིག་ཡོད་དོ་ཞེས་བྱ་བའི་ཚིག་དང་འགལ་བ་དང་། དེ་བཞིན་དུ་གཉི་གར་བརྗོད་པ་ཡང་གཉི་ག་དང་འགལ་ལོ། །

[Block 1066]
ཚིག་འདི་དག་ཐམས་ཅད་ཀྱང་ལས་སྟོང་པ་ཉིད་འཇུག་པའི་ཐབས་ཀྱི་ཕྱིར། ཆོས་ཉིད་དང་མི་འགལ་ལོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1067 [HEADING]]
### ཚིགས་བཅད་ཞེ་བཞི་པ། ^1-44-0

[Block 1068 [VERSE]]
ཡོད་ཅེས་པ་ཡོད་མེད་ཅེས་ཡོད། །
མེད་དང་ཡོད་ཅེས་དེ་ཡང་ཡོད། །
སངས་རྒྱས་རྣམས་ཀྱི༌[^767]དགོངས་པ་ཡིས། །
གསུངས་པ་རྟོགས༌[^768]པར་སླ་མ༌[^769]ཡིན། །

[Block 1069]
དེ་ལ་གཅིག་ཏུ་ངེས་པར་གཟུང་བར་མི་ནུས་པས་ལས་ངོ་བོ་ཉིད་ཀྱིས་ཡོད་པར་འཇིག་རྟེན་པས་ཡང་དག་པར་མཐོང་ནས་མངོན་པར་ཞེན་པའི་ཡོད་པ་ཡང་གང་ཅི་ཡང་རུང་བ་རྟག་པ་ཙམ་སྟེ། དྲི་ཟའི་གྲོང་ཁྱེར་ལ་སོགས་པའི་རྣམ་པ་ལ་མེད་དོ་ཞེས་བྱ་བར་རྟོགས་པ་ཁོང་དུ་ཆུད་པས་ལོག་པར་ལྟ་བས། གང་ཞིག་དམྱལ་བ་ཆེན་པོར་ལྟུང་བ་ལ་མངོན་པར་ཕྱོགས་པས་སྡིག་པ་ཆེན་པོ་དང་ལྡན་པར་གྱུར་པས། དེ་དག་མེད་པར་ལྟ་བ་ལས་བཟློག་པའི་དོན་དུ་ལས་ཡོད་དོ། །

[Block 1070]
ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཡོད་དོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་ལ། གང་ཞིག་དེ་གང་ཅི་ཡང་རུང་བ་རྟོག་པ་ཙམ་བྱིས་པའི་སྐྱེ་བོས་ཡོངས་སུ་བརྟགས་པའི༌[^770]དྲི་ཟའི་གྲོང་ཁྱེར་ལ་སོགས་པར་ཡོད་པ་དེ་ཐུགས་ལ་བཞག་པའོ། །

[Block 1071]
གང་ཡང་ལས་དང༌[^771]འབྲས་བུ་ལ་འདི་དག་བདེན་ནོ་ཞེས་མངོན་པར་ཞེན་ལ། མངོན་པར་ཞེན་པ་དེས་དེ་དག་འཁོར་བ་ལས་མི་གྲོལ་བས། རང་བཞིན་གྱིས་མ་སྐྱེས་པ་ཐུགས་ལ་བཞག་ནས་གསུངས་པ། གང་ལ་ལས་མེད་ཅིང་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་མེད་པ་དེ་ནི་འཕགས་པ་རྣམས་ཀྱི་རིགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1072]
གཉི་ག་ཡང་ཐུགས་ལ་བཞག་ནས་འགའ་ཞིག་ཏུ་ཡོད་པ་དང་མེད་པ་གཉི༌[^772]གའོ་ཞེས་སོ། །

[Block 1073]
དེ་ལྟར་ཇི་སྐད་སྨོས་པའི༌[^773]རིགས་པས་བདེན་པ་གཉིས་སུ་རྣམ་པར་གཞག་པ་མ་བྱས་ན།

[Block 1074 [VERSE]]
སངས་རྒྱས་རྣམས་ཀྱི༌[^774]དགོངས་པ་ཡིས། །
གསུངས་པ་རྟོགས་པར་སླ་མ་ཡིན། །

[Block 1075]
འདིར་ཚིག་ཁ་ཅིག་ནི་དོན་གྱི་རྗེས་སུ་འབྲངས༌[^775]ནས་འཇུག་ལ། འགའ་ཞིག་དགོངས་པའི་རྗེས་སུ་འབྲངས་ནས་འཇུག་གོ། །

[Block 1076]
[^776]རེ་ཞིག་གང་དོན་གྱི་རྗེས་སུ་འབྲངས་ནས་འཇུག་པ་དེ་ནི་ངེས་པའི་དོན་ཏེ་དགོངས་པ་མ་ཡིན་པས་ན། ཇི་སྐད་གསུངས་པའི་དོན་ཡོད་བཞིན་པའི་ཕྱིར་ན། འདི་ལྟ་སྟེ་ཆོས་རྣམས་རང་བཞིན་མེད་པའོ། །

[Block 1077]
དེ་ཡང་ཇི་སྐད༌[^777]དུ་སྨོས་པའི་རིགས་པ་དང་ལུང་གིས་དཔྱད་པ་ན་དེ་བཞིན་ཁོ་ནར་འགྱུར་གྱི༌[^778]གཞན་དུ་མ་ཡིན་ནོ། །

[Block 1078]
གང་དུ་དགོངས་པའི་རྗེས་སུ་འབྲངས་ནས་འཇུག་པ་དེ་ནི་དྲི་བའི་དོན་ཏེ་དགོངས་པ་དང་བཅས་པའོ། །

[Block 1079]
འདི་ལྟ་སྟེ་གཟུགས་ཡོད་དོ་ཚོར་བ་ཡོད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་འདི་དག་ཀྱང་དོན་གྱི་ཁྱད་པར་ཅུང་ཟད་ཙམ་ཐུགས་ལ་བཞག་ནས་གསུངས་སོ་ཞེས་ངེས་ཏེ། ཇི་སྐད་དུ་ཐོས་པའི་དོན་དང་མི་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1080 [VERSE]]
དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ནི། །
རྒྱུ་རྐྱེན་ཚོགས་པའམ་སོ་སོ་ཡི། །
དངོས་ལ་རྣམས་ཀུན༌[^779]ཡོད་མིན་པའི། །
རང་བཞིན་གང་ཞིག་དེས་ན་སྟོང་། །

[Block 1081 [VERSE]]
ཡོད་པ་ཡོད་ཕྱིར་མི་སྐྱེ་ལ། །
མེད་པ་མེད་ཕྱིར་མི་སྐྱེ་ཞིང་། །
ཆོས་མི་མཐུན་ཕྱིར་ཡོད་མེད་མིན། །
སྐྱེ་བ་མེད་པས་གནས་འགག་མེད། །

[Block 1082]
ཞེས་བྱ་བ་ལ་སོགས་པའི་རིགས་པ་དང་། དགེ་སློང་དག་འདི་དག་ནི་དོན་དམ་པའི་བདེན་པ་གཅིག་པུ་སྟེ། འདི་ལྟར་ཞི་བའི་ཆོས་ཅན་མྱ་ངན་ལས་འདས་པའོ། །

[Block 1083]
འདུ་བྱེད་ཐམས་ཅད་ནི་བརྫུན་ཞིང་སླུ་བའི༌[^780]ཆོས་ཅན་ཏེ། གཟུགས་ནི་དབུ་བ་རྡོས་པ༌[^781]ལྟ་བུ། ཚོར་བ་ནི་ཆུའི་ཆུ་བུར་ལྟ་བུ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ལུང་གིས་ཀྱང་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པའི༌[^782]ཡོད་པ་ཉིད་དུ་གནས་པར་མི་ནུས་ཏེ། དེའི་ཕྱིར་དེ་ལྟ་བུ་ལ་སོགས་པའི་ཚིག་གིས་ཇི་ལྟར་ཐོས་བཞིན་པའི་དོན་དང་མི་ལྡན་པའི་ཕྱིར་དགོངས་པ་ཉིད་དུ་ངེས་ཏེ། རང་བཞིན་མེད་པ་གསལ་བར་བྱེད་པའི་ཚིག་བཞིན་དུ་འདི་དག་ནི་དོན་དང་རྗེས་སུ་མཐུན་པའི་ཚིག་མ་ཡིན་ནོ། །

[Block 1084]
འོན་ཀྱང་དོན་གྱི་བདག་ཉིད་ཅུང་ཟད་ཙམ་ཐུགས་ལ་བཞག་ནས་གསུངས་སོ་ཞེས་བྱའོ། །

[Block 1085]
དེ་ལྟར་གཉིས་ཉིད་དུ་རྣམ་པར་གནས་པ་འདི་དག་འདིར་བསམ་པར་བྱ་སྟེ། ཅི་ཡོད་པ་ཉིད་ཀྱི་ཚིག་འདི་དག་སྒྲ་ཇི་བཞིན་པ་ཡིན་ནམ། འོན་ཏེ་དགོངས་པ་དང་བཅས་པ་ཡིན། དེ་ལ་རེ་ཞིག་ཡོད་པ་ཉིད་ཀྱི་ཚིག་འདི་དག་སྒྲ་ཇི་བཞིན་པ་ཡིན་ན། དེའི་ཚེ་ཤིན་ཏུ་དོན་མ་ཡིན་པ་སྐྱེ་བ་ཐོབ་པར་འགྱུར་ལ། མེད་པས༌[^783]མཐོང་བ་ཙམ་ལས་ཐེར་ཟུག་པ་དང་རྒྱུན་ཆད་པའི་མཐའོ། །

[Block 1086]
ཡང་ན་དྲང་དོན་ནི༌[^784]དེའི་ཚེ་ཇི་སྐད་སྨོས་པའི་དོན་དང་མི་ལྡན་པས་འདི་ནི་དོན་དང་རྗེས་སུ་མཐུན་པའི་ཚིག་མ་ཡིན་ནོ། །

[Block 1087]
དེ་ལྟ་ན་ཡང་དོན་གྱི་བདག་ཉིད་ཅུང་ཟད་ཙམ་ཐུགས་ལ་བཞག་ནས་གསུངས་པས་ཞེས་བྱ་སྟེ། རེ་ཞིག་འདི་ཙམ་ཡོངས་སུ་གཅོད་པའོ། །

[Block 1088]
གང་ཡང་དོན་འདི་ནི་བདེན་པ་གཉིས་རྣམ་པར་གཞག་པ་ལ་མི་མཁས་པ་རྣམས་ཀྱིས་འདིར་ལེགས་པར་མི་ཤེས་པའི་ཕྱིར་རོ།[^785] །དེས་ན་ཇི་སྐད་སྨོས་པའི་བདེན་པ་གཉིས་ཀྱི་བློ་དང་ལྡན་པས་མངོན་པར་སྦྱོར་བར་བྱེད་པར་རུང་ངོ་ཞེས་བྱའོ། །

[Block 1089]
འདིར་སྨྲས་པ། གལ་ཏེ་ཡང་ལས་དང་བྱེད་པ་པོ་བཀག་ལ། དེ་ལྟ་ན་ཡང་རེ་ཞིག་ལས་ཀྱི་འབྲས་བུ་གཟུགས་ལ་སོགས་པ་ཡོད་པས་གཟུགས་ལ་སོགས་མེད་དོ་ཞེས་ཀྱང་བརྗོད་པར་མི་ནུས་སོ་ཞེས་བྱ་སྟེ། སྐྱེ་བོ་ཐམས་ཅད་ཀྱི་མངོན་སུམ་དུ་རགས་པ་དང་ཉེ་བར་དམིགས་བཞིན་པའི་གཟུགས་ཡོད་པ་ཉིད་ལས༌[^786]སུ་ཞིག་མེད་དོ་ཞེས་སྨྲ།[^787] གང་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་གསུངས་ཏེ། དགེ་སློང་དག་གཟུགས་ནི་ཕྱི་རོལ་གྱི་སྐྱེ་མཆེད་དེ་འབྱུང་བ་ཆེན་པོ་བཞི་དག་རྒྱུར་བྱས་པའི་གཟུགས་བསྟན་དུ་ཡོད་ལ། ཐོགས་པ་དང་བཅས་པའོ། །

[Block 1090]
དེ་བཞིན་དུ་དགེ་སློང་དག་རེག་བྱ་ནི་ཕྱི་རོལ་གྱི་སྐྱེ་མཆེད་དེ་འབྱུང་བ་ཆེན་པོ་བཞི་རྒྱུར་བྱས་པའི་གཟུགས་ཅན་བསྟན་དུ་ཡོད་ལ་ཐོགས་པ་དང་བཅས་པའོ། །
--- END BLOCKS ---
