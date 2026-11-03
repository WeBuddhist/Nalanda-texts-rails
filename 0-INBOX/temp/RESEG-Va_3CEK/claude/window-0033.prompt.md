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
དེ་བཞིན་གཤེགས་པ་རྣམ་པར་གཟིགས་ཀྱི་ཚེ་ནི་གསུམ་པ་རྫོགས་སོ། །

[Block 1157]
དེ་དག༌[^842]ཐམས་ཅད་ཀྱི་དང་པོ་ཤཱཀྱ་ཐུབ་པ་ཡིན། སྔོན་ཤཱཀྱ་ཐུབ་པ་ཞེས་བྱ་བ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་གང་ལ་བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔར་གྱུར་པའི་ཚེ་བདག་ཀྱང་འདི་འདྲ་བའི་རྣམ་པ་ཁོ་ནར་སངས་རྒྱས་པར་ཤོག་ཤིག༌[^843]ཅེས་དང་པོར་སྨོན་ལམ་བཏབ་པ་བྱུང་སྟེ། དེ་ཡང་འདི་བཞིན་དུ་རྩོད་པའི་དུས་ཁོ་ན་ལ་བྱུང་ལ། དེའི་བསྟན་པ་ཡང་ལོ་སྟོང་གི་མཐའི་བར་དུ་གནས་པར་གྱུར་ཏོ། །

[Block 1158 [HEADING]]
### ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པ། ^1-70-0

[Block 1159]
ཡང་བྱང་ཆུབ་སེམས་དཔའ་གནས་སྐབས་གང་དག་ཏུ༌[^844]ཕ་རོལ་ཏུ་ཕྱིན་པ་གང་ཡོངས་སུ་རྫོགས་པར་བྱེད་ཅེ་ན།

[Block 1160 [VERSE]]
ཀུན་ལ་ཐམས་ཅད་སྙིང་རྗེ་ཡིས། །
སྦྱིན་པར་བྱེད་པས་སྦྱིན་པ་རྫོགས། །

[Block 1161]
གང་གི་ཚེ་གང་ལ་ཀུན་ལ་ནི་མིག་གི་བར་དང་རྐང་གི་བར་ཐམས་ཅད་མངོན་པར་མཐོ་བའི་ཁྱད་པར་ལ༌[^845]མི་རེ་བར་སྙིང་རྗེས་སྦྱིན་པར་བྱེད་ན་དེ་ཙམ་གྱིས་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པ་ཡིན་ནོ། །

[Block 1162 [VERSE]]
ཆགས་བཅས་ཡན་ལག་བཅད་ཀྱང་ནི། །
མི་འཁྲུག་བཟོད་དང་ཚུལ་ཁྲིམས་ཀྱི། །

[Block 1163]
གང་གི་ཚེ་འདོད་ཆགས་དང་མ་བྲལ་བཞིན་དུ་ཡན་ལག་བཅད་ཀྱང་ཅུང་ཟད་ཀྱང་མི་འཁྲུག་པ་དེའི་ཚེ་འདིའི་ཚུལ་ཁྲིམས་དང་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དག་ཡོངས་སུ་རྫོགས་པ་ཡིན་ནོ། །

[Block 1164]
སྐར་རྒྱལ་བསྟོད་པས་བརྩོན་འགྲུས་ཀྱི། །བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔར་གྱུར་པའི་ཚེ་དེ་བཞིན་གཤེགས་པ་སྐར་རྒྱལ་རིའི་ཕུག་ཅིག་ན་མེའི་ཁམས་ལ་སྙོམས་པར་ཞུགས་པ་མཐོང་ནས་རྐང་པ་གཅིག་གིས་འགྲེངས་ཏེ༌[^846]ཞག་བདུན་གྱི་བར་དུ། སྐྱེས་བུ་ཁྱུ་མཆོག་ཁྱོད་འདྲིའི་དགེ་སྦྱོང་ཆེན་པོ་གཞན་དག་ལྷ་ཡུལ་པ༌[^847]ལ་མེད། །འཇིག་རྟེན་འདི་ནའང་ཡོད་པ་མ་ཡིན་རྣམ་ཐོས་བུ་ཡི་གནས་ནའང་ཡོད་མ་ཡིན། །ལྷ་ཡི་ཕོ་བྲང་གནས་མཆོག་དག་ནའང་ཡོད་མིན་ཕྱོགས་སམ་ཕྱོགས༌[^848]མཚམས་དག་ནའང་མེད། །རི་དང་ནགས་སུ་བཅས་པའི་ས་སྟེང་རྒྱས་པར་ཀུན་ཏུ༌[^849]ཡུལ་གཅིག་ག་ལ་ཡོད། །ཅེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་གཅིག་གིས་བསྟོད་པ་དེའི་ཚེ་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་ཡོངས་སུ་རྫོགས་ལ། བསྐལ་པ་དགུ་ཡང་བསྡུམས་སོ་ཞེས་གྲག་གོ། །

[Block 1165]
དེ་མ་ཐག་ལ་ཏིང་ངེ་འཛིན་བློའི་བྱང་ཆུབ་པའི༌[^850]སྔོན་རོལ་གྱི་དེ་མ་ཐག་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་ཚེ་བསམ་གཏན་དང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དག་ཡོངས་སུ་རྫོགས་ཏེ། རང་རང་གི་ཕུན་སུམ་ཚོགས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཕྱིར་ཕ་རོལ་ཏུ་ཕྱིན་པ་དག་ཡིན་ནོ། །

[Block 1166 [HEADING]]
### བསོད་ནམས་བྱ་བའི་གཞི་གསུམ། ^1-71-0

[Block 1167]
མདོ་ལས་སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་གཞི་དང་། ཚུལ་ཁྲིམས་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་གཞི་དང་། བསྒོམ་པ་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་གཞི་དང་བསོད་ནམས་བྱ་བའི་གཞི་གསུམ་གསུངས་པ། ཇི་ལྟར་ན་གསུམ་པོ་འདི་དག་བསོད་ནམས་བྱ་བའི་གཞི་ཡིན་ཞེ་ན།

[Block 1168 [VERSE]]
གསུམ་པོ་བསོད་ནམས་བྱ་བ་དང་། །
དེའི་གཞི་དཔེར་ན་ལས་ལམ་བཞིན། །

[Block 1169]
གསུམ་པོ་འདི་དག་ནི་ཅི་རིགས་པར་བསོད་ནམས་ཀྱང་ཡིན། བྱ་བ་ཡང་ཡིན།[^851] གཞི་ཡང་ཡིན་པས་བསོད་ནམས་བྱ་བའི་གཞི་སྟེ། དཔེར་ན་དེ་དག་ནི་ལས་ཀྱང་ཡིན་ལ་ལས་ཀྱི་ལམ་ཡང་ཡིན་པ་དང་། ལས་ཀྱི༌[^852]ལམ་ཁོ་ན་ཡིན་པས་ལས་ཀྱི་ལམ་མོ་ཞེས་བཤད་པ་བཞིན་ནོ། །

[Block 1170]
དེ་ལ་རེ་ཞིག་སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་གཞི་ལ་ལུས་དང་ངག་གི་ལས་ནི་རྣམ་པ་གསུམ་ཆར་ཡིན་ནོ། །

[Block 1171]
དེ་ཀུན་ནས་སློང་བར་བྱེད་པའི་སེམས་པ་ནི་བསོད་ནམས་ཀྱང་ཡིན་ལ་བྱ་བ་ཡང་ཡིན་ནོ། །

[Block 1172]
དེ་དང་ལྷན་ཅིག་འབྱུང་བའི་ཆོས་རྣམས་ནི་བསོད་ནམས་ཁོ་ན་ཡིན་ནོ། །

[Block 1173]
ཚུལ་ཁྲིམས་ལས་བྱུང་བ་ནི་ལུས་དང་ངག་གི་ལས་ཁོ་ན་ཡིན་པས་རྣམ་པ་གསུམ་ཆར་ཡིན་ནོ། །

[Block 1174]
བསྒོམ་པ༌[^853]ལས༌[^854]བྱུང་བ་ལ་བྱས་པ་ནི་བསོད་ནམས་ཀྱང་ཡིན་ལ་བསོད་ནམས་བྱ་བའི་གཞི་ཡང་ཡིན་ཏེ། བྱམས་པའི་སྒོ་ནས་དེ་དང་མཚུངས་པར་ལྡན་པའི་སེམས་པ་མངོན་པར་འདུ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1175]
དེ་དང་ལྷན་ཅིག་འབྱུང་བའི་སེམས་པ་དང་། ཚུལ་ཁྲིམས་ནི་བསོད་ནམས་ཀྱང་ཡིན་ལ་བྱ་བ་ཡང་ཡིན་ནོ། །

[Block 1176]
དེ་དང་ལྷན་ཅིག་འབྱུང་བ་གཞན་ནི་བསོད་ནམས་ཁོ་ན་ཡིན་ནོ། །

[Block 1177]
ཡང་ན་བསོད་ནམས་བྱེད་པ་ནི་བསོད་ནམས་བྱ་བ་སྟེ། སྦྱོར་བའོ། །

[Block 1178]
འདི་དག་སྒྲུབ་པའི་ཆེད་དུ་བསོད་ནམས་ཀྱི་འབྱོར་པ་རྩོམ་པའི་ཕྱིར་གསུམ་པོ་འདི་དག་ནི་དེའི་གཞི་ཡིན་ནོ། །

[Block 1179]
གཞན་དག་ན་རེ་བསོད་ནམས་བྱ་བ་ནི་དོན་དམ་པར་ན་སེམས་པ་དགེ་བ་ཡིན་ལ། འདི་དག་ནི་དེའི་གཞི་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1180 [HEADING]]
#### སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་གཞི། ^1-71-1-0

[Block 1181 [HEADING]]
##### གང་གིས་སྦྱིན་བྱེད་དེ་སྦྱིན་པ། ^1-71-1-1-0

[Block 1182]
སྦྱིན་པ་ཞེས་བྱ་བ་འདི་ཅི་ཡིན་ཞེ་ན། གང་སྦྱིན་པར་བྱ་བ་དེ་ཡང་སྦྱིན་པ་ཡིན་མོད་ཀྱི་འདིར་ནི། གང་གིས་སྦྱིན་བྱེད་དེ་སྦྱིན་པ། །འཇིགས་པ་དང་། ལན་ལ་རེ་བ་དང་། འདོད་ཆགས་པ་ལ་སོགས་པས་ཀྱང་སྦྱིན་པར་བྱེད་མོད་ཀྱི། དེ་ནི་འདིར་མི་འདོད་པས་དེའི་ཕྱིར་ཁྱད་པར་དུ་བྱ་བའི་ཕྱིར། མཆོད་དང་ཕན་གདགས་འདོད་པ་ཡིས། །ཞེས་བྱ་བ་སྨོས་ཏེ། གང་གིས་གཞན་དག་ལ་མཆོད་པ་དང་། ཕན་གདགས་པར་འདོད་པ་དག་གིས་སྦྱིན་པར་བྱེད་པའོ། །གང་གིས་སྦྱིན་པར་བྱེད་པ་དེ་ཡང་གང་ཞིག་ཅེ་ན།

[Block 1183 [VERSE]]
ལུས་དང་ངག་ལ༌[^855]སློང་དང་བཅས། །
སློང་བ་ཡང་གང་ཞིག་ཅེ་ན།
ཚོགས༌[^856]གང་གིས་དེ་སློང་བར་བྱེད་པའོ། །

[Block 1184]
འདིར་སྨྲས་པ།

[Block 1185 [VERSE]]
གང་ཚེ་སྐྱེས་བུ་དགེ་ཡིད་ཀྱིས། །
རང་གི་རྫས་དག་སྦྱིན་བྱེད་པ། །
དེ་ཚེ་དགེ་བའི་ཕུང་པོ་རྣམས། །
སྦྱིན་པ་ཞེས་ནི་བརྗོད་པ་ཡིན། །

[Block 1186]
ཞེས་བྱ་བའོ། །

[Block 1187 [HEADING]]
##### འབྲས་བུ་ལོངས་སྤྱོད་ཆེན་པོ། ^1-71-1-2-0

[Block 1188]
དེ་འབྲས་ལོངས་སྤྱོད་ཆེན་པོ་ཅན། །སྦྱིན་པ་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་གཞི་གང་ཡིན་པ་དེ་ནི་འབྲས་བུ་ལོངས་སྤྱོད་ཆེན་པོ༌[^857]ཡིན་ནོ། །

[Block 1189]
འབྱུང་བ༌[^858]ཞེས་བྱ་བ་འདི་ནི་རང་བཞིན་ཡིན་པར་རིག་པར་བྱ་སྟེ། དཔེར་ན་རྩྭ༌[^859]ལས་བྱུང་བའི་ཁྱིམ་དང་། ལོ་མ་ལས་བྱུང་བའི་སྣོད་ཅེས་བྱ་བ་བཞིན་ནོ། །

[Block 1190 [HEADING]]
##### བདག་གཞན་དོན་ཕྱིར་སྦྱིན་པ། ^1-71-1-3-0

[Block 1191]
ཡང་སྦྱིན་པ་དེ་ནི།

[Block 1192 [VERSE]]
བདག་གཞན་དོན་ཕྱིར་གཉིས་དོན་ཕྱིར། །
གཉི་གའི་དོན་དུ་མིན་ཕྱིར་སྦྱིན། །

[Block 1193]
དེ་ལ་འདོད་ཆགས་དང་མ་བྲལ་བའམ། སོ་སོའི་སྐྱེ་བོ་འདོད་ཆགས་དང་མ༌[^860]བྲལ་བས་མཆོད་རྟེན་ལ་སྦྱིན་པ་སྦྱིན༌[^861]པར་བྱེད་པ་གང་ཡིན་པ༌[^862]དེས་ཕ་རོལ་པོ་དག་ལ་ཕན་འདོགས་པ་མེད་པའི་ཕྱིར་དེའི་བདག་ཉིད་ཁོ་ནའི་དོན་གྱི་ཕྱིར་སྦྱིན་པ་ཡིན་ནོ། །

[Block 1194]
འཕགས་པ་འདོད་ཆགས་དང་བྲལ་བས་སེམས་ཅན་ཕ་རོལ་པོ་དག་ལ་སྦྱིན་པར་བྱེད་པའི་སྦྱིན་པ་གང་ཡིན་པ༌[^863]དེ་ནི་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བ་མ་གཏོགས་པར་དེས་དེ་དག་ལ་ཕན་བཏགས་པའི་ཕྱིར་གཞན་གྱི་དོན་གྱི་ཕྱིར་ཡིན་གྱི་བདག་གི་དོན་གྱི་ཕྱིར་ནི་མ་ཡིན་ཏེ། དེའི་རྣམ་པར་སྨིན་པའི་ས་ལས་ཤིན་ཏུ་ཡང་དག་པར་འདས་པའི་ཕྱིར་རོ། །

[Block 1195]
འདོད་ཆགས་དང་མ་བྲལ་བའམ། སོ་སོའི་སྐྱེ་བོའི་འདོད་ཆགས་དང་བྲལ་བས་སེམས་ཅན༌[^864]ཕ་རོལ་པོ༌[^865]དག་ལ་སྦྱིན་པར་བྱེད་པའི་སྦྱིན་པ་གང་ཡིན་པ་དེ་ནི་གཉི་གའི་དོན་གྱི་ཕྱིར་ཡིན་ནོ། །
--- END BLOCKS ---
