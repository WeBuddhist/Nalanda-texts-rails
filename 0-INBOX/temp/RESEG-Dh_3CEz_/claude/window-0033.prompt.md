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
ཡང་སྔར་ནི་ཕྱག་རྒྱའི་ངེས་པ་བསྒྲུབ་པ་ལས་མཁའ་སྤྱོད་མ་ལ་སོགས་པ་རིགས་གསུམ་དུ་བྱ་བ་དང་རིགས་ཀྱི་དབྱེ་བ་གོ་སླའོ། །ལེའུ་བཞི་པའོ།། །།
### ལེའུ་ལྔ་པ། ^2-5-0

[Block 1157]
ད་ནི་ཧེ་རུ་ཀ་ཕྱག་བཅུ་དྲུག་པ་ལས༌[^1247]གསུངས་པ།[^1248] དེའི་སྒྲུབ་ཐབས་བཤད་པར་ཞུས་པ་ནི། ཕྱག་ནི་བཅུ་དྲུག་ཞལ་བརྒྱད་པ། །ཞེས་པ་ནི་རྡོ་རྗེ་འཆང་ལ་བདག་མེད་མས་གསོལ་བ་གདབ་པའོ། །དཔའ་བོ་ཐོད་པའི་ཕྲེང་བ་ཅན་ནི་མི༌[^1249]མགོ་ལྔ་བཅུའི་ཕྲེང་བ་འཕྱང་སྟེ་འདུ་བྱེད་ལྔ་བཅུ་དག་པའོ། །གཞན་དག་ནི་རྣམ་པར་དག་པ་སྔར་བཤད་ཟིན་ཏོ། །བཅོ་ལྔས༌[^1250]ཡོངས་སུ་བསྐོར་བའི་བདག་གི་འཁོར་ལོ་ཁྱེད་ཀྱིས་བཤད་ནི་ལེའུ་བརྒྱད་པར་གསུངས་པའོ། །ཁྱོད་ཀྱི་དཀྱིལ་འཁོར་ཇི་ལྟར་ལགས། །ཞེས་དྲིས་པའོ། །བདག་མེད་མ་ལ་འོ་མཛད་ནས། །ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཞེ་སྡང་ཅན་དང་ཆགས་པ་ཅན་འདུལ་བའི་དོན་ཏོ། །

[Block 1158]
འཁོར་ལོ་ཇི་ལྟར་སྔར་གསུངས་པ། །ཞེས་པའི་དོན་འདིར་སྒྲུབ་པའི་ཐབས་ནི་སྒྲུབ་པ་པོས་གནས་གང་ཡང་རུང་བར་བྱ་བ་དང་། ཚོགས་བསགས་པ་དང་། སྲུང་བ་མཚམས་དང་ཆོས་ཀྱི་འབྱུང་གནས་བསྒོམ་པ་སྔ་མ་ལྟར་བྱས་ལ།

[Block 1159 [VERSE]]
འཁོར་ལོ་ས་དང་ཆུ་ནི་སྔོན། །
ཇི་ལྟར་རིགས་པར༌[^1251]བྱིན་ཟ་ཡི། །

[Block 1160]
ཞེས་ལེའུ་བརྒྱད་པ་ལྟར་བསྒོམས་ལ། ཁྱད་པར་ནི་འཕར་མ་གཅིག་པ་ལ་སོགས་པ་དང་ལྡན་པའི་རྗེས་ལ། ཚངས་པ་དབང་པོ་ཉེ་དབང་དྲག །ལ་སོགས་པ་སྦྱར་ལ། དུར་ཁྲོད་བརྒྱད་དང་བཅས་པའི་དབུས་སུ༌[^1252]བདུད་བཞི་བསྣོལ་མར་བསྒོམས་ནས་ཨ་ལ་བཛྲ་ཞེས་པའི་སྔགས་བརྗོད་དོ། །

[Block 1161]
དེ་སྐད་དུ་ཡང་།

[Block 1162 [VERSE]]
མི་མཉམ་མེད་པས་གྲུ་བཞི་སྟེ། །
དྲན་པས་དབང་པོ་སྒོ་བཞི་ཡིན། །
རྣམ་ཐར་བརྒྱད་ཀྱི་ཀ་བ་སྟེ། །
ཏིང་འཛིན་བཞི་ཡི་ཁ་ཁྱེར་ཏེ། །

[Block 1163 [VERSE]]
བསམ་གཏན་བཞི་ཡི་རྟ་བབས་ཅན། །
འདོད་པའི་ཡོན་ཏན་ལྔ་ཡིས་སྤྲས། །
ཉོན་མོངས་ཆེ་ཆུང་རྣམ་དག་པའི། །
དྲ་བ་དང་ནི་དྲ་བ་ཕྱེད། །

[Block 1164 [VERSE]]
ཁམས་གསུམ་བདག་ནི་མེད་པ་ཡི། །
དུར་ཁྲོད་བརྒྱད་ཀྱིས༌[^1253]ཉེ་བར་མཛེས། །
ཚངས་པ་ལ་སོགས་མནན་པ་ནི། །
ཐ་མལ་རྣམ་སྦྱོང་གཞལ་ཡས་ཁང་། །

[Block 1165]
རྟེན་གྱི་རྣལ་འབྱོར་དྲོད་གཤེར་ལས་སྐྱེས་པ་དང་མཐུན་པ་རྣམ་པར་སྣང་མཛད་ཀྱི་རྣམ་པར༌[^1254]དག་པའོ། །

[Block 1166]
དེ་ནས་འདོད་ཆགས་ཆེན་པོ་རྗེས་ཆགས་ཞེས་བྱ་བ་ཤློ་ཀ་གཅིག་སྦྱར་ཏེ། དེ་ལ་དབུས་སུ་ང་ཡོད་ཅེས་བྱ་བ་ནི་རྡོ་རྗེ་འཆང་བསྐྱེད་པ་སྟེ།

[Block 1167 [VERSE]]
ཨཱ་ལི་ཟླ་བ་ཀཱ་ལི་ཉི། །
ས་བོན་ནང་དུ་སོན་གྱུར་པ། །
དེ་ཉིད༌[^1255]སེམས་དཔའ་ཞེས་བྱར་བརྗོད། །
ནམ་མཁའི་དཀྱིལ་འཁོར་ཁྱབ་པ་ནི།[^1256] །

[Block 1168 [VERSE]]
རང་གི་ལུས་མཚུངས་རྣམ་པར་སྤྲོ། །
བསྡུས་ནས་སྙིང་གར་དགུག་པ་ནི། །
ཡོ་གི་ཞེ་སྡང་བདག་ཉིད་ཅེས། །
མངོན་པར་བྱང་ཆུབ་ལྔ་སྦྱར་ཏེ། །

[Block 1169 [VERSE]]
ཟླ་བ་མེ་ལོང་ཡེ་ཤེས་ལྡན། །
བདུན་གྱི་བདུན་པ་མཉམ་ཉིད་ལྡན། །
རང་ལྷའི་ས་བོན་ཕྱག་མཚན་ནི། །
སོ་སོར་རྟོག་པ་ཡིན་ཞེས་ཟེར། །

[Block 1170 [VERSE]]
དེ་རྣམས་གཅིག་གྱུར་བྱ་ནན་ཏན། །
རྫོགས་པ་ཆོས་དབྱིངས་དག་པའོ། །

[Block 1171]
ཞེས་པ་རྡོ་རྗེ་འཆང་སྐུ་མདོག་དཀར་པོ་གོང་དུ་གསུངས་པ་དང་། འོག་ནས་འཆད་པའི་ཕྱག་མཚན་ལ་སོགས་པ་དང་ལྡན་བར་བསྐྱེད་ལ། རྡོ་རྗེ་དང་པདྨ་བྱིན་གྱིས་བརླབས་ལ་རྗེས་སུ་ཆགས་པའི་སྔགས་བརྗོད་པ་ནི་རྗེས་སུ་ཆགས་པའི་ཡན་ལག་སྟེ་སྒོང་སྐྱེས་དང་ཆོས་མཐུན་པའོ། །

[Block 1172]
དེའི་རྗེས་ལ།

[Block 1173 [VERSE]]
གྲོང་ཁྱེར་ཉམས་དགར་ཁྱོད་དང་ང་། །
དགའ་བས་ཤིན་ཏུ་རོལ་པ་ལས། །

[Block 1174]
ཞེས་སྦྱར་ཏེ། དེ་ཡང་།

[Block 1175 [VERSE]]
དང་པོ་སྐྱེས་བུ་བསམ་དེ་ནས། །
མཁའ་འགྲོ་མ་ཡི་འཁོར་ལོ་སྤྲོ། །

[Block 1176]
ཞེས་གསུངས་ཏེ་འཁོར་རྗེས་སུ་མཐུན་པའི་བྱང་ཆུབ་པ་ལྔས༌[^1257]མངལ་སྐྱེས་ཀྱི་སྒོང་སྐྱེས་དང་འདྲ་བར་བསྐྱེད་དེ། གཾ་ཙཾ་ལ་སོགས་པ་ཚིག་གཉིས་སྦྱར་རོ། །

[Block 1177]
དེའི༌[^1258]དོན་ནི་སྙིང་ག་ནས་འོད་འཕྲོས་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་བཀུག་ནས་ཞལ་དུ་ཞུགས། སྙིང་གར་ཞུ། སྲོག་དག་པའི་ལམ་ནས་བྱུང་སྟེ། ཡུམ་གྱི་པདྨར་ཐིག་ལེ་དེ་ལས་ས་བོན་བརྒྱད་དུ་གྱུར་པ་དང་། མདུན་གྱི་ཚངས་པའི་གདན་སྟེང་དུ་ཨཱ་ལི་ལས་ཟླ་བ་ཀཱ་ལི་ལས་ཉི་མ་དེའི་བར་ན༌[^1259]གཾ །དེ་ལས་གྲི་གུག །[^1260]དེ་སྤྲོ་བསྡུ་བྱས་ནས་ཞུ་བ་ལས་གཽ་རཱི་བསྐྱེད་དེ།

[Block 1178 [VERSE]]
དཀར་མོ་དབང་པོའི་ཕྱོགས་ཕྱུང་ནས། །
ཞེས་བྱ་བ་ལ་སོགས་པ་སྦྱར་རོ། །
རླུང་གི་མཚམས་སུ་གཡུང་མོ་ནི། །

[Block 1179]
ཞེས་པའི་མཐར་ཏེ། རླུང་མཚམས་ནི༌[^1261]ཉི་མའི་སྟེང༌[^1262]ན་ཐགས༌[^1263]བཟངས་རིས་མནན་པའི་སྟེང་དུ་ཨཱ་ལི་ལས༌[^1264]ཟླ་བ་ཀཱ་ལི་ལས་ཉི་མ། དེ་གཉིས་བར་དུ་ཌཾ་དེ་ལས་རྡོ་རྗེ་ལ་ཌཾ་གིས་མཚན་པ་དེ་སྤྲོས་བསྡུས་ནས་ཞུ་བ་ལ་གཡུང་མོ་བསྐྱེད་དོ། །

[Block 1180]
གཞན་ལ་ཡང་དེ་བཞིན་སྦྱར་རོ། །

[Block 1181]
དེ་སྐད་དུ།

[Block 1182 [VERSE]]
ཟླ་བ་ཉི་མའི་རབ་དབྱེ་བས། །
དཀར་མོ་ལ་སོགས་རབ་ཏུ་གྲགས། །

[Block 1183]
ཞེས་གསུངས་སོ། །

[Block 1184]
དེ་ལྟར་འཁོར་བསྐྱེད་ནས་གཙོ་བོ་འགྱུར་བ་ནི། དེ་ནས་རྡོ་རྗེ་ཆགས་ཆེན་ལས། །

[Block 1185]
རིག་མ་བཅས་པར་ཞུ་བར་འགྱུར།[^1265] །ཞེས་པ་སྟེ། རྒྱུའི་འགྱུར་བ་ནི་སྔར་གྱི་ཐིག་ལེ་བྱང་ཆུབ་སེམས་དཔའ་འབྲུ་ལྔར་གྱུར་པ་དེ་གཙོ་བོའི་ཞལ་དུ་ཞུགས་པས་གཙོ་བོ་དང་རིག་མར་བཅས་པ་ཞུའོ། །

[Block 1186 [VERSE]]
དེ་ནས་རྐྱེན་གྱིས་འགྱུར་བ་ནི། །
སྣ་ཚོགས་གླུ་ཡི་མཆོད་པ་ལས། །
དེ་ནས་ལྷ་མོ་རྣམས་ཀྱིས་བསྐུལ། །

[Block 1187]
ཞེས་པ་སྟེ་མཚམས་ཀྱི་ལྷ་མོས་བསྐུལ་ཏེ་ཆོས་ཅན་རྣམ་པར་དག་པ་འབྱུང་བ་བཞིས་འབྲས་བུ་བསྐྱེད་པ་དང་། ངོ་བོ་ཚད་མེད་པ་བཞེས༌[^1266]སེམས་ཅན་གྱི་དོན་བྱེད་པ་དང་ལས་སོ་སོར་ངེས་པ་སྟེ། མཚམས་མས་སློང་བའི་ལས་དང་། སྒོ་མས་ཡེ་ཤེས་ཀྱི་འཁོར་ལོ་དགུག་པ༌[^1267]ལ་སོགས་པའོ། །

[Block 1188]
རྗེ་བཙུན་ཞེས་བྱམས་པ་ཆེན་པོ་པུཀྐ་སཱིའི་གླུ་སྟེ་སྲི་ཞུས་བོད་པའོ། །སྙིང་རྗེའི་ཡིད་ཀྱིས་བཞེངས་ཤིག་པ་སྟེ་ཐིག་ལེ་ལས་བསྐུལ་བའོ། །པུཀྐ་སཱི་ནི་བདག་ལ་སྐྱོབས༌[^1268]ནི་སེམས་ཅན་གྱི་དོན་མཛོད་ཅིག་པའོ། །སྟོང་པའི་རང་བཞིན་ཉིད་སྤོངས་ལ་ནི་ཐིག་ལེ་སྟོང་པ་དང་འདྲ་སྟེ་གཞན་དོན་མི་ནུས་པའོ། །བདག་ལ་བདེ་ཆེན་སྦྱོར༌[^1269]ནི་གཞན་དོན་ལ་བསྐུལ་བ་སྟེ་གཞན་བདེ་བས་བདག་བདེ་བའོ། །ཁྱོད་མེད་ན་ནི་བདག་འགུམ་པས། །ཞེས་པ་སྙིང་རྗེ་ཆེན་པོ་ཤ་བ་རཱིའི་གླུ་སྟེ་བདག་གི་སྲོག་སྙིང་རྗེས་གཞན་དོན་མེད་ན་སྙིང་རྗེ་མེད་པ་བདག་འགུམ་པ་ཞེས་པའོ། །

[Block 1189]
ཀྱེའི་རྡོ་རྗེ་ཞེས་བོད་པའོ། །སྟོང་པ་སྔ་མ་དང་འདྲའོ། །རི་ཁྲོད་མ་འབྲས་བསྒྲུབ་པ་ནི་གཞན་དོན་མཛོད་ཅིག་པའོ། དགའ་གཙོ་ཞེས་པ་ནི་དང་བའི་དགའ་བའི་གླུ་སྟེ། ཁྱེད་དང་པོ་སེམས་བསྐྱེད་ཙམ་ན་སེམས་ཅན་མགྲོན་དུ་བོས་ནས་ད་སྟོང་པ་ལ་ཅིའི་ཕྱིར་བཞུགས་ཞེས་བྱའོ། །

[Block 1190]
འོ་ན་རང་གིས་གཞན་དོན་བྱས་མོད་ཅེ་ན། ཁྱོད་མེད་ན་ནི་ཕྱོགས་མི་ཁུམས། །ཞེས་པ་སྟེ་བདག་གི་དོན་མི་ཤེས་པར་དགོངས་པའོ། །དེའི་ཕྱིར་བདག་ཞུ་བར་བགྱིད་པའོ། །མིག་འཕྲུལ་ལྟ་བུར་ཞེས་བྱ་བ་ཤློ་ཀ་གཅིག་སྦྱར་ཏེ། བཏང་སྙོམས་གཡུང་མོའི་གླུ་སྟེ། ཁྱེད་སྤྲུལ་པ་ལྟ་བུ་སྒྱུ་མ་ལྟ་བུ་མངའ་བ་སྟེ་དེ་ཅིའི་ཕྱིར་ཞེ་ན། བདག་གིས་ཁྱེད་ཀྱི་ཐུགས་འཚལ་ཞེས་པའོ། །དེའི་འཐད་པ་གཡུང་མོ་བདག་ཉིད་དྲན་ཉམས་ནི་གྲོང་ཁྱེར་ཆེན་པོའི་མི་ཞེས་བྱ་སྟེ། སྙིང་རྗེ་རྒྱུན་ཆད་མ་མཛད་ནི་ཐིག་ལེ་སྤོངས་ཞེས་བྱའོ། །

[Block 1191]
དེའི་རྗེས་སུ། ཨཾ་དང་ཧཱུཾ་གིས་རྡོ་རྗེ་ཆེ། ཞེས་བྱ་བ་ཤློ་ཀ་གཅིག་སྦྱར་ཏེ་འབྲས་བུ་ཧེ་རུ་ཀར་བཞེངས་པ་ནི་རྫུས༌[^1270]སྐྱེས་དང་མཐུན་པ། ཡུད་ཙམ་གྱིས༌[^1271]མངོན་པར་བྱང་ཆུབ་པ་བསྐྱེད་དེ། བདག་པོ་ས་བོན་དག་གིས་ནི་ཚིག་གཉིས་སྦྱར་ཏེ། ཐིག་ལེ་དེ་ཆ་གཉིས་ལས་འོག་ཟླ་བ་མེ་ལོང་ལྟ་བུ་སྟེང་ཉི་མ་མཉམ་པ་ཉིད་དེ། བར་དུ་ཡི་གེ་ཨཾ་དང་ཧཱུཾ་ལས་རྡོ་རྗེ་ཆེན་པོ་སྟེ། གྲི་གུག་དེ་ལས་ས་བོན་གྱིས་མཚན་མ་ནི་སོ་སོར་རྟོག་པའི་ཡེ་ཤེས་དེ་ལས་སྤྲོ་བ་དང་བསྡུས་ནས་ཞུ་བ་ནི་བྱ་བ་ནན་ཏན་ནོ། །

[Block 1192]
དེ་ལས་སྐུར་བཞེངས་པ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་སོ། །དེའི་མོད་ལ་ཞབས་རྣམས་ས་ལ་བརྡབས་པ་ལ་སོགས་པར་གྱུར་ཏོ། །འདིར་ཐིག་ལེ་གཉིས་བྱས་ལ་ཡུམ་ཡང་འགྲན་ཐུབ་ཏུ་བསྐྱེད་དེ་བདག་མེད་མ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །ཞལ་བརྒྱད་པ་ལ་ཞབས་བཞི་ཞེས་སྦྱར་ཏེ་རྣམ་དག་ཕལ་ཆེར་སྔར་བཤད་དོ། །སྣ་ཚོགས་རྡོ་རྗེ་ནི་མི་བསྐྱོད་པའི་རིགས་མཚོན་པའོ། །ཐལ་བས་ལུས་ལ་བྱུགས་པ་ནི་དྲུག་པ་རྡོ་རྗེ་འཆང་གི་དག༌[^1272]པའོ། །དབའ་རླབས་མེད་པའི་བདེ་བ་ཞེས་པ་ལྷན་ཅིག་སྐྱེས་པའི་ངོ་བོའོ། །

[Block 1193]
དེའི་རྗེས་ལ་གླང་པོ་རྟ་བོང་ཞེས་སྦྱར་ཏེ།

[Block 1194 [VERSE]]
གློ་དང་དབུགས་དང་དེ་བཞིན་སྨྱོ། །
ཁྲག་སྐྱུག༌[^1273]མཛེ་དང་བིརྫི༌[^1274]ཀ །
མཆེར་པ་མཆིན་པར༌[^1275]རང་གཟུགས་ནི། །
གོ་རིམས་བཞིན་དུ་སྤོང་ཕྱིར་རོ། །

[Block 1195 [VERSE]]
ཕྲ་བ་ཡང་བ་མཆོད་པར་བསྟན། །
བདག་པོར་གྱུར་པར་བདག་ལྡན་པ། །
གང་ཡང་ཕྱིན་ཅིང་འདོད་དགུར་ལྡན། །
དགའ་མགུར་སྤྱོད་པ་བདེ་བས་སོ། །
--- END BLOCKS ---
