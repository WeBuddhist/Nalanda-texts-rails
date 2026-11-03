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

[Block 1126]
དགུ་པ་ནི་ཀུན་ཤེས་པའི་དབང་པོ་ཡིན་ནོ། །

[Block 1127 [HEADING]]
##### བཅུ་གཅིག་དག་གིས་དགྲ་བཅོམ་ཉིད། ^2-1-7-3-0

[Block 1128]
འོ་ན་ཆོས་མངོན་པ་ལས་དབང་པོ་དུ་ཞིག་གིས་དགྲ་བཅོམ་པ་ཉིད་འཐོབ་ཅེ་ན། སྨྲས་པ། བཅུ་གཅིག་གིས་འཐོབ་བོ་ཞེས་བཤད་པ་གང་ཡིན་པ་དེ་ཇི་ལྟར་དགུ་དག་གིས་འཐོབ་ཅེས་བཤད་ཅེ་ན། དེ་ནི་དགུ་ཁོ་ནས་འཐོབ་སྟེ།

[Block 1129 [VERSE]]
བཅུ་གཅིག་དག་གིས་དགྲ་བཅོམ་ཉིད། །
འགའ་ཞིག་སྲིད་ཕྱིར་བཤད་པ་ཡིན། །

[Block 1130]
གང་ཟག་གཅིག༌[^496]འགའ་ཞིག་ཡོངས་སུ་ཉམས་ཤིང་ཡོངས་སུ་ཉམས་ནས་བདེ་བ་དང་། ཡིད་བདེ་བ་དང༌[^497]བཏང་སྙོམས་ཀྱི་དབང་པོ་དག་གིས་དགྲ་བཅོམ་པ་ཉིད་འཐོབ་པ་སྲིད་པ་ཡོད་པས་དེའི་ཕྱིར་བཅུ་གཅིག་གིས་ཞེས་བཤད་ཀྱི། བདེ་བ་ལ་སོགས་པ་དུས་གཅིག་ཏུ་སྲིད་པ་ནི་མེད་དོ། །

[Block 1131]
འདི་ཕྱིར་མི་འོང་བ་ལ་ཡང་ཇི་ལྟར་ཐལ་བར་མི་འགྱུར་ཞེ་ན། འདི་ནི་ཡོངས་སུ་ཉམས་ཕན་ཆད་ནམ་ཡང་བདེ་བའི་དབང་པོས་འཐོབ་པ་མེད་དོ། །

[Block 1132]
འདོད་ཆགས་དང་བྲལ་བ་སྔོན་དུ་འགྲོ་བ་ལ་ནི་ཡོངས་སུ་ཉམས་པར་འགྱུར་བ་ཡང་མེད་དེ། དེའི་འདོད་ཆགས་དང་བྲལ་བ་ནི་ལམ་གཉིས་ཀྱིས་འཐོབ་པའི་ཕྱིར་རོ། །

[Block 1133 [HEADING]]
#### དབང་པོ་དག་དང་ལྡན་པ། ^2-1-8-0

[Block 1134 [HEADING]]
##### གདོན་མི་ཟ་བར་ལྡན་པ། ^2-1-8-1-0

[Block 1135]
དབང་པོ་གང་ཞིག་དང་ལྡན་ན་གདོན་མི་ཟ་བར་དབང་པོ༌[^498]དག་དང་ལྡན་པ་དག་ཡིན་ཞེས་བྱ་བ་འདི་དཔྱད་པར་བྱ་སྟེ། དེ་ལ་བཏང་སྙོམས་དང་ནི་སྲོག་དང་ནི། །ཡིད་དང་ལྡན་ལ་ངེས་གསུམ་ལྡན། །གང་ཞིག་བཏང་སྙོམས་ལ་སོགས་པ་འདི་དག་ལས་གང་ཡང་རུང་བ་ཞིག་དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་དབང་པོ་གསུམ་དག་དང་ལྡན་པ་ཡིན་ཏེ། དེ་དག༌[^499]ཉིད་དང་ངོ་། །འདི་དག་ནི་ཕན་ཚུན་མེད་ན་མི་ལྡན་པ་ཡིན་གྱི་ལྷག་མ་རྣམས་དང་ནི་མ་ངེས་ཏེ། ལྡན་པ་ཡང་ཡོད་མི་ལྡན་པ་ཡང་ཡོད་དོ། །

[Block 1136]
དེ་ལ་རེ་ཞིག་མིག་དང་རྣ་བ་དང་སྣ་དང་ལྕེའི་དབང་པོ་དག༌[^500]ནི་གཟུགས་མེད་པར་སྐྱེས་པ་དང་མི་ལྡན་ནོ། །

[Block 1137]
འདོད་པའི་ཁམས་ན་ནི་གང་གིས་མ་ཐོབ་པ་དང་རྣམ་པར་ཉམས་པ་དག་དང་མི་ལྡན་ནོ། །

[Block 1138]
ལུས་ཀྱི་དབང་པོ༌[^501]ནི་གཟུགས་མེད་པར་སྐྱེས་པ་དང་མི་ལྡན་ནོ། །

[Block 1139]
མོའི་དབང་པོ་དང་ནི་གཟུགས་དང་གཟུགས་མེད་པར་སྐྱེས་པ་དང་མི་ལྡན་ནོ། །

[Block 1140]
འདོད་པའི་ཁམས་ན་ནི་གང་གིས་མ་ཐོབ་པ་དང་། རྣམ་པར་ཉམས་པ་དང་མི་ལྡན་ཏེ། ཕོའི་དབང་པོ་ཡང་དེ་བཞིན་ནོ། །

[Block 1141]
བདེ་བའི་དབང་པོ་དང་ནི་བསམ་གཏན་བཞི་པ་དང་གཟུགས་མེད་པར་སྐྱེས་པའི་སོ་སོའི་སྐྱེ་བོ་དང་མི་ལྡན་ནོ། །

[Block 1142]
ཡིད་བདེ་བའི་དབང་པོ་དང་ནི་བསམ་གཏན༌[^502]

[Block 1143]
གསུམ་པ་དང་།

[Block 1144]
བཞི་པ་དང་། གཟུགས་མེད་པར་སྐྱེས་པའི་སོ་སོའི་སྐྱེ་བོ་ཁོ་ན་དང་མི་ལྡན་ནོ། །

[Block 1145]
སྡུག་བསྔལ་གྱི་དབང་པོ་དང་ནི་གཟུགས་དང་གཟུགས་མེད་པར་སྐྱེས་པ་མི་ལྡན་ནོ། །

[Block 1146]
ཡིད་མི་བདེ་བ་དང་ནི་འདོད་པའི་འདོད༌[^503]ཆགས་དང་བྲལ་བ་མི་ལྡན་ནོ། །

[Block 1147]
དད་པ་ལ་སོགས་པ་དང་ནི་དགེ་བའི་རྩ་བ་ཀུན་ཏུ་ཆད་པར༌[^504]མི་ལྡན་ནོ། །

[Block 1148]
ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་དང་ནི་སོ་སོའི་སྐྱེ་བོ་དང་། འབྲས་བུ་ལ་གནས་པ་དག་དང༌[^505]མི་ལྡན་ནོ། །

[Block 1149]
ཀུན་ཤེས་པའི་དབང་པོ་དང་ནི་སོ་སོའི་སྐྱེ་བོ་དང་། མཐོང་བ་དང་མི་སློབ་པའི་ལམ་ལ་གནས་པ་རྣམས་ནི༌[^506]མི་ལྡན་ནོ། །

[Block 1150]
ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་དང་ནི༌[^507]སོ་སོའི་སྐྱེ་བོ་དང་སློབ་པ་དག་དང༌[^508]མི་ལྡན་ནོ། །

[Block 1151]
མ་བཀག་པའི་གནས་སྐབས་དག་ཏུ་ནི་ཇི་སྐད་བཤད་པ་དང་ལྡན་པར་རིག་པར་བྱའོ། །

[Block 1152]
བདེ་ལུས་ལྡན་ལ་བཞི་དག་དང་། །གང་ཞིག་བདེ་བའི་དབང་པོ་དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་བཏང་སྙོམས་ལ་སོགས་པ་གསུམ་པོ་དེ་དག་དང་། བདེ་བའི་དབང་པོ་དང་དབང་པོ་བཞི་དང་ལྡན་ལ། གང་ཞིག་ལུས་ཀྱི་དབང་པོ་དང་ལྡན་པ་དེ་ཡང་གསུམ་པོ་དེ་དག་དང་།

[Block 1153 [VERSE]]
ལུས་ཀྱི་དབང་པོ༌[^509]བཞི་དང་ལྡན་ནོ། །
མིག་སོགས་ལྡན་ལ་ལྔ་དང་ལྡན། །

[Block 1154]
གང་ཞིག་མིག་གི་དབང་པོ་དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་བཏང་སྙོམས་དང་སྲོག་དང་ཡིད་དང་ལུས་ཀྱི་དབང་པོ་དག་དང་། དེ་དང་དབང་པོ་ལྔ་དང་ལྡན་ཏེ། རྣ་བ་དང་སྣ་དང་ལྕེའི་དབང་པོ་དག་དང་ལྡན་པ་དེ་ཡང་དེ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 1155]
ཡིད་བདེ་ལྡན་ཡང་། གང་ཞིག་ཡིད་བདེ་བའི་དབང་པོ་དང་ལྡན་པ་དེ་ཡང་གདོན་མི་ཟ་བར་བཏང་སྙོམས་དང་སྲོག་དང་ཡིད་དང་བདེ་བ་དང་ཡིད་བདེ་བ་དང་དབང་པོ་ལྔ་དང་ལྡན་ནོ། །

[Block 1156]
བསམ་གཏན་གཉིས་པར་སྐྱེས་པ་བསམ་གཏན་གསུམ་པ་མ༌[^510]ཐོབ་པ་བདེ་བའི་དབང་པོ་གང་དག༌[^511]དང་ལྡན་པ་ཡིན་ཞེ་ན། བསམ་གཏན་གསུམ་པའི་ཉོན་མོངས་པ་ཅན་དང་ལྡན་ནོ། །

[Block 1157]
སྡུག་བསྔལ་ལྡན། བདུན་དང་། གང་ཞིག་སྡུག་བསྔལ་གྱི་དབང་པོ་དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་ལུས་དང་སྲོག་དང་ཡིད་དག་དང་ཚོར་བའི་དབང་པོ་བཞི་དང་བདུན་དང་ལྡན་ནོ། །

[Block 1158]
མོའི་དབང་སོགས་ལྡན། བརྒྱད་དང་། གང་ཞིག་མོའི་དབང་པོ༌[^512]དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་བདུན་པོ་དེ་དག་དང་མོའི་དབང་པོ་དང་བརྒྱད་དང༌[^513]ལྡན་ནོ། །

[Block 1159]
སོགས༌[^514]ཞེས་བྱ་བའི་སྒྲས་ནི་ཕོའི་དབང་པོ་དང་ཡིད་མི་བདེ་བ་དང་དད་པ་ལ་སོགས་པ་གཟུང༌[^515]སྟེ། དེ་དག་དང༌[^516]ལྡན་པ་ནི་རེ་རེ་ཞིང་ཡང་བརྒྱད་དང་ལྡན་པ་ཡིན་ཏེ། བདུན་པོ་དེ་དག་དང་ཕོའི་དབང་པོ་དང་ལྡན་ནོ། །

[Block 1160]
ཡིད་མི་བདེ་བའི་དབང་པོ༌[^517]ཡང་དེ་དང་འདྲའོ། །
--- END BLOCKS ---
