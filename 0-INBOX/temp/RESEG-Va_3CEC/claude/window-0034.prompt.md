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
[Block 1191]
ཐག་ཉེ་བ་ནི་ད་ལྟར་གྱི་གཟུགས༌[^1028]སོ། །

[Block 1192]
ཡང་ན་རྒྱང་རིང་པོ་ནི་གཞན་གྱི་རྒྱུད་དུ་གཏོགས་པའི་གཟུགས་སོ། །

[Block 1193]
ཐག་ཉེ་བ་ནི་བདག་གི་རྒྱུད་དུ་གཏོགས་པའི་གཟུགས་སོ། །

[Block 1194]
དེ་དག་ཐམས་ཅད་ནི་གོང་དུ་བཤད་པའི་གཟུགས་དེ་དག་ཐམས་ཅད་དོ། །

[Block 1195]
དེ་དག་གི་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་གི་ལྷའི་མིག་གིས་སོ། །

[Block 1196]
རིག་ཅིང་སྣང་བ་ལ་སོགས་པ་ནི་མཐོང་བའི་རྣམ་གྲངས་ཀྱི་ཚིག་གོ། །

[Block 1197]
ཡང་ན་འདས་པའི་གཟུགས་མཐོང་བ་ནི་རིག་པའོ། །

[Block 1198]
ད་ལྟར་གྱི་གཟུགས་མཐོང་བ་ནི་སྣང་བའོ། །

[Block 1199]
མ་འོངས་པའི་གཟུགས་མཐོང་བ་ནི་ཤིན་ཏུ་རྟོགས་པའོ། །

[Block 1200]
སྦོམ་པོ་རྣམས་མཐོང་བ་ནི་ཤིན་ཏུ་མཐོང་བའོ། །

[Block 1201]
ཡང་ན་མོས་པའི་སྤྱོད་པའི་ཏིང་ངེ་འཛིན་དྲོད་ཀྱི་རྒྱུ་ལས་བྱུང་བས་ན་རིག་པའོ། །

[Block 1202]
སྤྱི་བོའི་རྒྱུ་ལས་བྱུང་བས་ན་སྣང་བའོ། །

[Block 1203]
བཟོད་པའི་རྒྱུ་ལས་བྱུང་བས་ན་རྟོགས་པའོ། །

[Block 1204]
འཇིག་རྟེན་པའི་ཆོས་ཀྱི་མཆོག་གི་རྒྱུ་ལས་བྱུང་བས་ན་ཤིན་ཏུ་རིག་པའོ། །

[Block 1205]
མཐོང་བའི་ལམ་གྱི་རྒྱུ་ལས་བྱུང་བས་ན་ཤིན་ཏུ་མཐོང་བའོ། །

[Block 1206]
འཆི་འཕོ༌[^1029]དང་སྐྱེ་བ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བ་ནི་འཆི་བ་དང་འཕོ་བ་གཉིས་ཀྱང་ཕུང་པོ་འདོར་ཞིང་ལེན་པ་ལ་བྱ་སྟེ། གཟུགས་ཀྱི་ཕུང་པོ་ལེན་ཅིང་འདོར་བ་མིག་གི་སྤྱོད་ཡུལ་ཡིན་པས་ལྷའི་མིག་གིས་ཤེས་པར་བྱའོ། །

[Block 1207]
དེ་དག་གི་ལས་ཀྱི་རྒྱུ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་དེ་དག་གི་ལུས་དང་ངག་གི་སྒོ་ནས་ཅི་སྤྱོད་པ༌[^1030]དེའི་རྒྱུ་བསྟུན་ཇི་སྤྱོད་སྤྱོད་པ་ལས་བྱུང་བ་ཡང་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1208]
ལས་ཀྱི་འབྲས་བུ་ཤེས་པ་ནི་ད་ལྟའི་ལུས་དང་ངག་གི་སྒོ་ནས་ལས་ཅི་བྱས་པའི་འབྲས་བུ་ཕྱིས༌[^1031]ཅིར་འགྱུར་བ་ཤེས་པའོ། །

[Block 1209]
དབང་པོའི་རིམ་པ་ཤེས་པ་ནི་མིག་ལ་སོགས་པའི་དབང་པོ་རྣམས་དང་། དད་པ་ལ་སོགས་པའི་དབང་པོ་རྣོ་རྟུལ༌[^1032]གྱི་རིམ་པ་ཤེས་པ་སྟེ། ལས་ཀྱི་རྒྱུ་དང་འབྲས་བུ་དང་དད་པ་ལ་སོགས་པའི་དབང་པོ་འདི་དག་གཟུགས་ཀྱི་རྒྱུ་ལས་བྱུང་བའི་ཕྱིར་ལྷའི་མིག་གི་སྤྱོད་ཡུལ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1210]
སངས་རྒྱས་ཀྱི་ཞིང་གི་ཡོན་ཏན་བཀོད་པ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་ཞིང་ས་གཞི་བཻ་ཌཱུརྱའི་ཁ་དོག་དང་དཔག་བསམ་གྱི་ཤིང་གི་ཕྲེང་བ་དང་བདུད་རྩིའི་རྫིང་ལ་སོགས་པ་དང་ལྡན་པའོ། །

[Block 1211]
རང་གི་ཚུལ་ཁྲིམས་ཡོངས་སུ་དག་པས་རང་གི་ཞིང་གི་ཡོན་ཏན་བཀོད་པ་ཡོངས་སུ་དག་པར་བྱ་བའི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་བསགས་པ་རྣམས་ཡོངས་སུ་བསྔོ༌[^1033]སྟེ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ཞིང་གི་ཡོན་ཏན་མཐོང་ནས་བདག་ཀྱང་ནམ་སངས་རྒྱས་སུ་འགྱུར་བའི་ཚེ་ཞིང་གི་ཡོན་ཏན་དེ་ལྟ་བུ་དང་ལྡན་པར་གྱུར་ཅིག་ཅེས༌[^1034]བདག་གི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཅི་བསགས་པ་རྣམས་ཚུལ་ཁྲིམས་ཡོངས་སུ་དག་པའི་མཐུས་བསྔོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1212]
ཚུལ་ཁྲིམས་ཀྱི་མཐུས་བསྔོས་པས༌[^1035]ཇི་བཞིན་འགྲུབ་པར་འགྱུར༌[^1036]རམ་སྙམ་པ་ལ། ཚུལ་ཁྲིམས་ཀྱི་ཡོན་ཏན་ལ་གནས་པ་དེ་དག་གི་བསྔོ་བ་ཡོངས་སུ་འགྲུབ་པར་འགྱུར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆོས་ཉིད་ཀྱི་ཚུལ་ཁྲིམས་དང་ལྡན་པ་རྣམས་ཅི་བསམས༌[^1037]པའམ། སྨོན་པ་བཞིན་དུ་འགྲུབ་པས་ཇི་ལྟར་བསྔོས་པ་བཞིན་དུ་ཡོངས་སུ་འགྲུབ་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1213]
ཆོ་ག་དང་ཞེས་བྱ་བ་ལ། བྱ་བ་དང་མི་བྱ་བ་རྣམས་ནི་ཆོ་གའོ། །

[Block 1214]
ཆོས་གོས་བགོ་བ་དང་། ལྷུང་བཟེད་བཟུང་བ་ལ་སོགས་པ་ཆོས་བཞིན་དུ་བྱེད་པ་ནི་སྤྱོད་པའོ། །

[Block 1215]
ཆང་འཚོང༌[^1038]དང་སྨད་འཚོང་ལ་སོགས་པ་སྤྱོད་ཡུལ་ལྔར་མི་འཇུག་པ་ནི་སྤྱོད་ཡུལ་ལོ། །

[Block 1216]
ལྟུང་བ་དང་མི་ལྟུང་བ་མ་བརྗེད་པ་ནི་དྲན་པའོ། །

[Block 1217]
ལྟུང་བ་དང་མི་ལྟུང་བ་ཤེས་པ་ནི་ཤེས་བཞིན་ནོ། །

[Block 1218]
འགྲོ་བ་དང་འདུག་པ་དང་ཉལ་བ་དང་འཆག་པ་ལ་སོགས་པ་མཛེས་པ་ནི་སྤྱོད་ལམ་མོ། །

[Block 1219]
གཙུག༌[^1039]ལག་ཁང་དང་རི་དང་བྲག་ཕུག་ལ་སོགས་པ་ནི་གནས་སོ། །

[Block 1220]
མངོན་པར་ཤེས་པ་ལྔ་དང་ལྡན་པ་དང་། བདུད་དང་མུ་སྟེགས་ཅན་གྱིས་མི་ཕྱེད་པ་ནི་མཐུའོ། །

[Block 1221]
བྱང་ཆུབ་སེམས་དཔའི་མདོ་སྡེ་དང་འདུལ་བ་དང་ཆོས་མངོན་པ་ནི་ཆོས་སོ། །

[Block 1222]
མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་ནི་རྣམ་པར་ཐར་པའོ། །

[Block 1223]
མེ་ལོང་ལྟ་བུའི་དང་། མཉམ་པ་ཉིད་དང་། སོ་སོར་ཀུན་དུ་རྟོག་པ༌[^1040]དང་། བྱ་བ་སྒྲུབ་པའི་ཡེ་ཤེས་ནི་ཡེ་ཤེས་སོ། །

[Block 1224]
མཁས་པའི་ཚིག་རེ་རེ་དང་ཡང་སྦྱར་ཏེ། དོན་དང་ཆོས་དང་ཡེ་ཤེས་དང་། ངེས་པའི་དོན་གྱི་མདོ་སྡེ་ལ་རྟོན་པ༌[^1041]ནི་རྟེན་པ༌[^1042]ལ་མཁས་པའོ། །

[Block 1225]
དོན་དང་ཚིག་མི་བརྗེད་པའི་གཟུངས་དང་ལྡན་པ་ནི་གཟུངས་ལ་མཁས་པའོ། །

[Block 1226]
འཁོར་བའི་མཐའི་བར་དུ་ཆོས་བཤད་ཀྱང་སྤོབས་པ་ཟད་པར་མི་འགྱུར་བ་ནི་སྤོབས་པ་ལ་མཁས་པའོ། །

[Block 1227]
རང་དང་སྤྱིའི་མཚན་ཉིད་རྣམ་པར་འབྱེད་པ་ནི་ཤེས་རབ་པོ། ། ཆོས་ཐམས་ཅད་སྟོང་པར༌[^1043]ཁོང་དུ་ཆུད་པ་ནི་ཡེ་ཤེས་སོ། །

[Block 1228]
དགའ་ལྡན་གྱི་ཕོ་བྲང་ནས་འཆི་འཕོ་བ༌[^1044]ལ་སོགས་པ་སྟོན་པ་ནི་ཐབས་ལ་མཁས་པ་ལ་འཇུག་པའོ། །

[Block 1229]
དེ་དག་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་དོ་ཞེས་བྱ་བ་ནི་ལྷའི་མིག་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེས། འཇིག་རྟེན་གྱི་ཁམས་གཞན་གྱི་བྱང་ཆུབ་སེམས་དཔའི་ཡོན་ཏན་དེ་དག་མཐོང་ནས་བདག་ཉིད་ཀྱིས་ཀྱང་དེ་དག་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་དོ། །

[Block 1230]
གཟུགས་ཐམས་ཅད་མཐོང་བ་བཤད་ཟིན་ཏོ།། །།
--- END BLOCKS ---
