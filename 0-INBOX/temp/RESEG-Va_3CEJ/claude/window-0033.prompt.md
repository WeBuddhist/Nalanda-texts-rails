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

[Block 1161]
དད་པ་ལ་སོགས་པ་དང་ལྡན་པ་ནི་ལྔ་པོ༌[^518]དེ་དག་དང་བཏང་སྙོམས་དང་སྲོག་དང་ཡིད་དག་དང་ལྡན་ནོ། །

[Block 1162]
ཀུན་ཤེས་ལྡན་པའི། དབང་པོ་ལྡན་ལ་བཅུ་གཅིག་ལྡན། །ཀུན་ཤེས་པ་ལ་དབང་བྱེད་པས་ན་ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོའོ། །

[Block 1163]
གང་ཞིག་ཀུན་ཤེས་པའི་དབང་པོ་དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་བདེ་བ་དང་ཡིད་བདེ་བ་དང་བཏང་སྙོམས་དང་སྲོག་དང་ཡིད་དང་དད་པ་ལ་སོགས་པ་དག་དང་། ཀུན་ཤེས་པའི་དབང་པོ་དང་བཅུ་གཅིག་དང་ལྡན་ནོ། །

[Block 1164]
དེ་བཞིན་དུ་ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་དང་ལྡན་པ་ཡང་བཅུ་པོ་དེ་དག་ཉིད་དང་། ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་དང་ལྡན་ནོ། །

[Block 1165 [VERSE]]
ཀུན་ཤེས་བྱེད་པའི་དབང་ལྡན་ལ། །
བཅུ་གསུམ་དག་དང་ལྡན་པ་ཡིན། །
བཅུ་གསུམ༌[^519]དག་དང་ལྡན་ཞེ་ན། །

[Block 1166]
ཡིད་དང་སྲོག་དང་ལུས་ཀྱི་དབང་པོ་དག་དང་། ཚོར་བའི་དབང་པོ་བཞི་དག་དང་། དད་པ་ལ་སོགས་པ་དག་དང་། ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་དང་ལྡན་ནོ། །

[Block 1167 [HEADING]]
##### ནང་ན་ཉུང་བ་དག་དང་ལྡན་པ། ^2-1-8-2-0

[Block 1168]
ཡང་གང་ཞིག་ནང་ན་ཉུང་བ་དག་དང་ལྡན་པ་དེ་དབང་པོ་ཇི་སྙེད་ཅིག་དང་ལྡན་ཞེ་ན།

[Block 1169 [VERSE]]
དགེ་མེད་ནང་ན་ཉུང་ལྡན་པ། །
ལུས་ཚོར་སྲོག་ཡིད་བརྒྱད་དང་ལྡན། །

[Block 1170]
དགེ་མེད་ནི་དགེ་བའི་རྩ་བ་ཀུན་ཏུ་ཆད་པ་སྟེ། དེ་ནང་ན་ཉུང་བ་དག་དང་ལྡན་ན་ཚོར་བ་ལྔ་དག་དང་། ལུས་དང་ཡིད་དང་སྲོག་དག་དང་དབང་པོ་བརྒྱད་དང་ལྡན་ནོ། །

[Block 1171]
ཚོར་བར་བྱེད་པ་ནི་ཚོར་བ་སྟེ། མྱོང་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1172]
ཡང་ན་ཚོར་བ་ནི་ཚོར་བ་སྟེ། དཔེར་ན་ཕུན་སུམ་ཚོགས་པ་ལ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1173]
ཇི་ལྟར་དགེ་བ་མེད་པ་ནང་ན་ཉུང་བ་དག་དང་ལྡན་ན་དབང་པོ་བརྒྱད་དག་དང་ལྡན་པ་ལྟར་གཟུགས་མེད་བྱིས་པའང་དེ་བཞིན་ཏེ། བྱིས་པ་ཞེས་བྱ་བ་ནི་སོ་སོའི་སྐྱེ་བོའི་མིང་ངོ་། ། བརྒྱད་གང་དག་དང་ལྡན་ཞེ་ན། བཏང་སྙོམས་སྲོག་ཡིད་དགེ་རྣམས་དང་། །བཏང་སྙོམས་དང་སྲོག་དང་། ཡིད་དང་དད་པ་ལ་སོགས་པ་དང་ལྡན་ནོ། །

[Block 1174]
དགེ་བ་སྨོས་པ༌[^520]ནི་དད་པ་ལ་སོགས་པ་གཟུང་བར་བྱ་སྟེ། གཅིག་ཏུ་དགེ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1175]
ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ལ་སོགས་པ་ཡང་བསྡུས་པར་ཐལ་བར་འགྱུར་རོ་ཞེ་ན་མ་ཡིན་ཏེ། བརྒྱད་ཀྱི་སྐབས་ཡིན་པའི་ཕྱིར་དང་། བྱིས་པའི་སྐབས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1176 [HEADING]]
##### ནང་ན་མང་པོ་དག་དང་ལྡན་པ། ^2-1-8-3-0

[Block 1177]
ཡང་གང་ཞིག་ནང་ན་དབང་པོ་མང་པོ་དག་དང་ལྡན་པ་དེ་ཇི་སྙེད་ཅིག་དང་ལྡན་ཞེ་ན།

[Block 1178 [VERSE]]
མང་པོར་ལྡན་ན་བཅུ་དགུ་སྟེ། །
དྲི་མ་མེད་རྣམས་མ་གཏོགས་སོ། །
ཟག་པ་མེད་པ་གསུམ་མ་གཏོགས་སོ། །

[Block 1179]
དེ་ཡང་མཚན་གཉིས། མཚན་གཉིས་པ་དབང་པོ་ཚང་བ་གང་ཡིན་པ་དེ་ནི་བཅུ་དགུ་དང་ལྡན་ནོ། །

[Block 1180]
གཞན་ཡང་གང་ཞིག་ཅེ་ན། འཕགས་པ་ཆགས་བཅས་ཏེ། སློབ་པ་འདོད༌[^521]ཆགས་དང་མ་བྲལ་བ་ཡང་ནང་ན་མང་པོ༌[^522]དང་ལྡན་ན་བཅུ་དགུ་དང་ལྡན་ཏེ། མཚན་གཅིག་དྲི་མེད་གཉིས་མ་གཏོགས། །མཚན་གཅིག་དང་ཟག་པ་མེད་པ་གཉིས་ཏེ། ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་དང་། གཉིས་པོ་ལས་གང་ཡང་རུང་བ་ཞིག་མ་གཏོགས་སོ། །

[Block 1181]
ཁམས་རབ་ཏུ་དབྱེ་བའི་ཞར་ལ་འོངས་པ་དབང་པོ་རྣམས་ཀྱི་རབ་ཏུ་དབྱེ་བ་རྒྱས་པར་བཤད་ཟིན་ཏོ། །

[Block 1182 [HEADING]]
### ངེས་པར་ལྷན་ཅིག་སྐྱེ་བ། ^2-2-0

[Block 1183]
ད་ནི་འདི་དཔྱད་པར་བྱ་སྟེ། ཅི་འདུས་བྱས་ཀྱི་ཆོས་འདི་དག་ཅི་ལྟར༌[^523]མཚན་ཉིད་ཐ་དད་པ་དེ་བཞིན་དུ་ཐ་དད་པར་སྐྱེ་བ་ཞིག་ཡིན་ནམ། འོན་ཏེ་ཁ་ཅིག་ངེས་པར་ལྷན་ཅིག་སྐྱེ་བའང་ཡོད་ཅེ་ན། སྨྲས་པ་ཡོད་དེ། ཆོས་འདི་དག་ཐམས་ཅད་ནི་གཟུགས་དང་སེམས་དང་། སེམས་ལས་བྱུང་བ་དག་དང་། སེམས་དང་ལྡན་པ་མ་ཡིན་པ་དག་དང་། འདུས་མ་བྱས་དང་ལྔར་འགྱུར་རོ། །

[Block 1184]
དེ་ལ་འདུས་མ་བྱས་ལ་ནི་སྐྱེ་བ་མེད་པ་ཉིད་དོ། །

[Block 1185 [HEADING]]
#### གཟུགས་ཅན་རྣམས་ཀྱི་ངེས་པར་ལྷན་ཅིག་སྐྱེ་བ། ^2-2-1-0

[Block 1186]
ཆོས་གཟུགས་ཅན་རྣམས་ཀྱི་ངེས་པ་ནི་འདི་ཡིན་ཏེ།

[Block 1187 [VERSE]]
འདོད་ན་དབང་པོ་མེད་པ་དང་། །
སྒྲ་མེད་ཕྲ་རབ་རྡུལ་རྫས་བརྒྱད། །

[Block 1188]
ཐམས་ཅད་ལས་ཕྲ་བའི་གཟུགས་ནི་བསགས་པའི་རྡུལ་ཕྲ་རབ་ཅེས་བྱ་སྟེ། དེ་ལས་ཆེས་ཆུང་བ་ནི་མི་མངོན་ནོ། །

[Block 1189]
དེ་འདོད་པའི་ཁམས་ན་སྒྲ་ཡང་མེད་དབང་པོ་ཡང་མེད་པ་ཞིག་ཡིན་ན་ནི་རྫས་བརྒྱད་དང་ལྡན་པར་སྐྱེ་སྟེ། གང་ཡང་རུང་བ་ཞིག་མེད་པར་ནི་མ་ཡིན་ནོ། །

[Block 1190]
རྫས་བརྒྱད་ནི་འབྱུང་བ་ཆེན་པོ་བཞི་དག་དང་། རྒྱུར་བྱས་པའི་གཟུགས་བཞི་སྟེ། གཟུགས་དང་། དྲི་དང་། རོ་དང་། རེག་བྱ་རྣམས་སོ། །

[Block 1191]
རྡུལ་ཕྲ་རབ་དབང་པོ་དང་བཅས་ལ་སྒྲ་མེད་པ་ཞིག་ཡིན་ན་ནི་རྫས་དགུ་འམ། རྫས་བཅུ་དང་ལྡན་པར་སྐྱེ་སྟེ། དེ་ལ་རེ་ཞིག །ལུས་དབང་ལྡན་ལ་རྫས་དགུའོ། །

[Block 1192]
འདི་ལ་ལུས་ཀྱི་དབང་པོ་ཡོད་པས་ན་འདི་ནི་ལུས་དབང་ལྡན་ནོ། །

[Block 1193]
དེ་ལ་རྫས་དགུ་ནི་བརྒྱད་པོ་དག་དང་ལུས་ཀྱི་དབང་པོའོ། །

[Block 1194]
དབང་པོ་གཞན༌[^524]རྫས་བཅུའོ། །

[Block 1195]
དབང་པོ་གཞན་གྱི་རྡུལ་ཕྲ་རབ་གང་ལ་ཡོད་པ་དེ་ལ་རྫས་བཅུ་སྟེ། དགུ་པོ་དེ་དག་ཉིད་དང་། མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེའི་དབང་པོ་རྣམས་ལས་གང་ཡང་རུང་བ་ཞིག་གོ། །
--- END BLOCKS ---
