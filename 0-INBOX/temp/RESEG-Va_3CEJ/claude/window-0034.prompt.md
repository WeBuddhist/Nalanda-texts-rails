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
རྡུལ་ཕྲ་རབ་དབང་པོ་དང་བཅས་ལ་སྒྲ་མེད་པ་ཞིག་ཡིན་ན་ནི་རྫས་དགུ་འམ། རྫས་བཅུ་དང་ལྡན་པར་སྐྱེ་སྟེ། དེ་ལ་རེ་ཞིག །ལུས་དབང་ལྡན་ལ་རྫས་དགུའོ། །

[Block 1192]
འདི་ལ་ལུས་ཀྱི་དབང་པོ་ཡོད་པས་ན་འདི་ནི་ལུས་དབང་ལྡན་ནོ། །

[Block 1193]
དེ་ལ་རྫས་དགུ་ནི་བརྒྱད་པོ་དག་དང་ལུས་ཀྱི་དབང་པོའོ། །

[Block 1194]
དབང་པོ་གཞན༌[^524]རྫས་བཅུའོ། །

[Block 1195]
དབང་པོ་གཞན་གྱི་རྡུལ་ཕྲ་རབ་གང་ལ་ཡོད་པ་དེ་ལ་རྫས་བཅུ་སྟེ། དགུ་པོ་དེ་དག་ཉིད་དང་། མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེའི་དབང་པོ་རྣམས་ལས་གང་ཡང་རུང་བ་ཞིག་གོ། །

[Block 1196]
རྡུལ་ཕྲ་རབ་དེ་དག་སྒྲ་དང་བཅས་པ་ཞིག་ཏུ་སྐྱེ་ན་ནི་གོ་རིམས་བཞིན་དུ་རྫས་དགུ་དང་། བཅུ་དང་བཅུ་གཅིག་དང་ལྡན་པར་སྐྱེ་བ་ན་སྐྱེའོ། །

[Block 1197]
དབང་པོ་དང་ཐ་མི་དད་པའི་སྒྲ་ཡང་ཡོད་དེ། ཟིན་པའི་འབྱུང་བ་ཆེན་པོའི་རྒྱུ་ལས་བྱུང་བ་གང་ཡིན་པའོ། །

[Block 1198]
ཇི་ལྟར་ན་འབྱུང་བ་རྣམས་ཐ་མི་དད་པ་ལས་འདི་ན་འདུས་པ་ཁ་ཅིག་ཁོ་ན་ནི་སྲ་བར་དམིགས། ཁ་ཅིག་ཁོ་ན་ནི་གཤེར་བའམ་དྲོ་བ་འམ་གཡོ་བར་དམིགས་ཤེ་ན། གང་ཞིག་གང་ན་ཆེས་གསལ་ཞིང་མཐུའི་སྒོ་ནས་ཤས་ཆེ་བ་དེ་ནི་དེ་ན་དམིགས་ཏེ། དཔེར་ན་ཁ་བ་དང་སྡོང་བུའི་ཚོགས་ལ་རེག་པ་ལྟ་བུ་དང་། ཕྱེ་དང་ལན་ཚྭའི་ཕྱེ་མའི་རོ་བཞིན་ནོ། །

[Block 1199]
ཡང་ཇི་ལྟར་དེ་དག་ན་ལྷག་མ་རྣམས་ཡོད་པར་ཁོང་དུ་ཆུད་པར་བྱ་ཞེ་ན། ལས་ཀྱི་སྒོ་ནས་ཏེ། སྡུད་པ་དང་འཛིན་པ་དང་། སྨིན་པ་དང་། གཡོ་བའི་ཕྱིར་རོ། །

[Block 1200]
རྐྱེན་དང་ཕྲད་ན་སྲ་བ་ལ་སོགས་པ་ཡང་གཤེར་བ་ལ་སོགས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1201]
གཞན་དག་ན་རེ་ཆུ་དག་ལ་གྲང་བའི་ཁྱད་པར་གྱི་སྒོ་ནས་དྲོ་བ་ཡོད་པར་ཁོང་དུ་ཆུད་དོ་ཞེས་ཟེར་རོ། །

[Block 1202]
མ་འདྲེས་ཀྱང་ཁྱད་པར་ཡོད་པར་འགྱུར་ཏེ། སྒྲ་དང་ཚོར་བའི་ཁྱད་པར་བཞིན་ནོ། །

[Block 1203]
གཞན་དག་ན་རེ་དེ་དག་ལས་དེ་དག་ས་བོན་གྱི་སྒོ་ནས་ཡོད་ཀྱི་རང་གི་ངོ་བོར་ནི་མ་ཡིན་ཏེ། ཤིང་གི་ཕུང་པོ་འདི་ལ༌[^525]ཁམས་རྣམ་པ་སྣ་ཚོགས་ཡོད་དོ་ཞེས་གསུངས་པའི་ཕྱིར༌[^526]ཞེས་ཟེར་རོ། །

[Block 1204]
རླུང་ལ་ཁ་དོག་ཇི་ལྟར་ཡོད་ཅེ་ན། དོན་འདི་ནི་དད་པར་བྱ་བ་ཡིན་གྱི་རྗེས་སུ་དཔག་པར་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 1205]
ཡང་ན་འདྲེས་པར་དྲི་འཛིན་པའི་ཕྱིར་ཏེ། དེ་ལ་ནི་ཁ་དོག་འཁྲུལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1206]
གཟུགས་ཀྱི་ཁམས་ན་ནི་དྲི་དང་རོ་དག་མེད་པར་བཤད་པས་དེས་ན་ཡོད་པའི་རྡུལ་ཕྲ་རབ་རྣམས་ནི་རྫས་དྲུག་དང་། བདུན་དང་བརྒྱད་དང་ལྡན་པ་ཞེས་བཤད་ཟིན་པ་དང་འདྲ་བའི་ཕྱིར༌[^527]མི་བཤད་དོ། །

[Block 1207]
ཡང་ཅི་འདིར་རྫས་ཁོ་ན་ལ་རྫས་སུ་གཟུང༌[^528]ངམ། འོན་ཏེ་སྐྱེ་མཆེད་ཀྱི་རྫས་ལ་རྫས་སུ་གཟུང་། དེས་ན༌[^529]ཅིར་འགྱུར། གལ་ཏེ་རྫས་ཁོ་ན་ལ་རྫས་སུ་གཟུང༌[^530]ནས་ནི་རྫས་བརྒྱད་དང་ལྡན་པ་དང་རྫས་དགུ་དང་བཅུ་དང་ལྡན་པ་ཞེས་བྱ་བ་འདི་ཧ་ཅང་ཉུངས་པར་སྨྲས་པ་ཡིན་ཏེ། དེ་ཡང་རྡུལ་ཕྲ་རབ་བསགས་པ་ཡིན་པའི་ཕྱིར་གདོན་མི་ཟ་བར་དེ་ལ་དབྱིབས་ཀྱང་ཡོད་དོ། །

[Block 1208]
ལྕི་བ་ཉིད་དང་ཡང་བ་ཉིད་དག་ལས་གང་ཡང་རུང་བ་ཞིག་དང་། འཇམ་པ་ཉིད་དང་རྩུབ་པ་ཉིད་དག་ལས་གང་ཡང་རུང་བ་ཞིག་ཀྱང་ཡོད་དོ། །

[Block 1209]
ཁ་ཅིག་ལ་ནི་གྲང་བ༌[^531]ཡང་ཡོད་ལ། བཀྲེས་པ་དང་སྐོམ་པ་ཡང་ཡོད་དོ། །

[Block 1210]
འོན་ཏེ་སྐྱེ་མཆེད་ལ་རྫས་སུ་གཟུང༌[^532]ན་ནི་རྫས་བརྒྱད་དང་ལྡན་པ་ཞེས་བྱ་བ་འདི་ཧ་ཅང་མངས་པར་སྨྲས་པ་ཡིན་ཏེ། རྫས་བཞི་དང་ལྡན་པ་ཞེས་བྱ་བ༌[^533]བརྗོད་པར་བྱ་སྟེ། འབྱུང་བ་ཇི་སྙེད་པ་དག་ཀྱང་རེག་བྱའི་སྐྱེ་མཆེད་ཡིན་ནོ། །

[Block 1211]
འདིར་ཅུང་ཟད་ཅིག་ནི་རྫས་ཁོ་ན་ལ་རྫས་སུ་གཟུང་སྟེ། རྟེན་དུ་གྱུར་པ་གང་ཡིན་པའོ། །

[Block 1212]
འདིར་ཅུང་ཟད་ཅིག་ནི་སྐྱེ་མཆེད་ཀྱི་རྫས་ལ་རྫས་སུ་གཟུང་སྟེ་རྟེན་ཅན་དུ་གྱུར་པ་གང་ཡིན་པའོ། །

[Block 1213]
དེ་ལྟ་ན་ཡང་འབྱུང་བའི་རྫས་རྣམས་མང་པོར་འགྱུར་ཏེ། རྒྱུར་བྱས་པའི་གཟུགས་རྣམས་རེ་རེ་ཞིང་འབྱུང་བ་བཞི་ཚན་ལ་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 1214]
འདིར་ནི་རིགས་ལ་རྫས་སུ་གཟུང་སྟེ། འབྱུང་བ་བཞི་པོ་གཞན་དག་ཀྱང་རིགས་ལས་མི་འདའ་བའི་ཕྱིར་རོ། །

[Block 1215]
དེ་ལྟར་འབད་དེ་བྱེ་བྲག་ཏུ་བཤད་ཅི་དགོས། ཚིག་ནི་འདུན་པའི་སྒོ་ནས་འཇུག་པ་ཡིན་པས་དོན་ལ་བརྟག་པར་བྱའོ། །

[Block 1216]
གཟུགས་ཅན་རྣམས་ཀྱི་ངེས་པར་ལྷན་ཅིག་སྐྱེ་བ་བཤད་ཟིན་ཏོ། །

[Block 1217 [HEADING]]
#### སེམས་དང་སེམས་ལས་བྱུང་བ། ^2-2-2-0

[Block 1218]
ལྷག་མ་རྣམས་ཀྱི་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག །སེམས་དང་སེམས་བྱུང་ངེས་ལྷན་ཅིག །འདི་དག་ནི་ཕན་ཚུན་མེད་ན་འབྱུང་བར་མི་ནུས་སོ། །

[Block 1219]
ཐམས་ཅད་འདུས་བྱས་མཚན་ཉིད་དང་། །ངེས་པར་ལྷན་ཅིག་ཅེས་བྱ་བར་སྦྱར་ཏེ། གཟུགས་སམ། སེམས་སམ། སེམས་ལས་བྱུང་བ་དག་གམ། །ལྡན་པ་མ་ཡིན་པ་དག་ཀྱང་རུང་། གང་ཅུང་ཟད་སྐྱེ་བ་དེ་ཐམས་ཅད་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་རྣམས་དང་ལྷན་ཅིག་སྐྱེའོ། །

[Block 1220]
འཐོབ་པ༌[^534]འམ། ཐོབ་པ་དང་ནི་སེམས་ཅན་དུ་སྟོན་པ་ཁོ་ན་དང་ལྷན་ཅིག་སྐྱེའི་གཞན་དང་ནི་མ་ཡིན་ནོ། །ཞེས་བྱེ་བྲག་ཏུ་བྱ་བའི་ཕྱིར་རམ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 1221 [HEADING]]
##### སེམས་ལས་བྱུང་བ་རྣམ་པ་ལྔ། ^2-2-2-1-0

[Block 1222]
སེམས་ལས་བྱུང་བ་རྣམས་ཞེས་བརྗོད་པ་སེམས་ལས་བྱུང་བ་དེ་དག་གང་ཞེ་ན། སེམས་བྱུང་རྣམ་ལྔ་སྟེ། ས་མང་ལ་སོགས་ཐ་དད་ཕྱིར། ། སེམས་ལས་བྱུང་བ་རྣམས་ནི་རྣམ་པ་ལྔ་སྟེ། ས་མང་པོ་དག་དང་། དགེ་བའི་ས་མང་པོ་པ་རྣམས་དང་། ཉོན་མོངས་པའི་ས་མང་པོ་པ་རྣམས་དང་། མི་དགེ་བའི་ས་མང་པོ་པ་རྣམས་དང་། ཉོན་མོངས་པ༌[^535]ཆུང་ངུའི་ས་པ་རྣམས་སོ། །

[Block 1223]
ས་ཞེས་བྱ་བ་ནི་གོ་སྐབས་ཀྱི་ཡུལ་ཏེ། གང་ཞིག་གང་གི་གོ་སྐབས་ཀྱི་ཡུལ་ཡིན་པ་དེ་ནི་དེའི་ས་ཞེས་བྱའོ། །

[Block 1224 [HEADING]]
###### ས་མང་པོ་པ། ^2-2-2-1-1-0

[Block 1225]
དེ་ལ་འདི་དག་ལ་ས་མང་པོ་པ་ཡོད་པས་ན་ས་མང་པོ་པ་རྣམས་ཏེ། གང་དག་སེམས་ཐམས་ཅད་ལ་འབྱུང་བའོ། །

[Block 1226]
གང་དག་སེམས་ཐམས་ཅད་ལ་འབྱུང་བ་དེ་དག་ཀྱང༌[^536]གང་ཞེ་ན།

[Block 1227 [VERSE]]
ཚོར་དང་སེམས་པ་འདུ་ཤེས་དང་། །
འདུན་དང་རེག་དང་བློ་གྲོས་དྲན། །
ཡིད་ལ་བྱེད་དང་མོས་པ་དང་། །
ཏིང་ངེ་འཛིན་སེམས་ཐམས་ཅད་ལ། །

[Block 1228]
ཆོས་བཅུ་པོ་འདི་དག་ནི་སེམས་ཀྱི་སྐད་ཅིག་མ་ཐམས་ཅད་ལ་ཚོགས་པར་འབྱུང་ངོ་ཞེས་གྲག་གོ་ལོ།[^537] །དེ་ལ་ཚོར་བ་ནི་མྱོང་བ་རྣམ་པ་གསུམ་སྟེ། བདེ་བ་དང་། སྡུག་བསྔལ་དང་། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ༌[^538]ཡང་མ་ཡིན་པའོ། །

[Block 1229]
སེམས་པ་ནི་སེམས་མངོན་པར་འདུ་བྱེད་པའོ། །

[Block 1230]
འདུ་ཤེས་ནི་འདུས་ནས་ཤེས་པ་སྟེ། ཡུལ་ལ་མཚན་མར་འཛིན་པའོ། །
--- END BLOCKS ---
