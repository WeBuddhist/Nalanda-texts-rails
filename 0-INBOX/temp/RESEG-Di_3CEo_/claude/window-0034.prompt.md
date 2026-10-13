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
[Block 1191 [VERSE]]
འདིར་གང་སྐྱེ་དང་འཆི་བ་ཡི། །
སྲིད་པའི་བར་དུ་འབྱུང་བའོ། །

[Block 1192]
འགྲོ་བའི་བར་མ་ཡིན་པའི་ཕྱིར་སྲིད་པའི་བར་མའོ། །

[Block 1193]
ཇི་ལྟར་ན་འདི་སྐྱེས་པ་ཡང་ཡིན་ལ། འབྱུང་བ༌[^438]ཡང་མ་ཡིན་ཞེ་ན།

[Block 1194 [VERSE]]
བགྲོད་པའི་ཡུལ་དུ་མ་ཕྱིན་ཕྱིར། །
སྲིད་པ་བར་མ་བྱུང་བ་མིན། །

[Block 1195]
སོན་པ་ནི་བྱུང་བ་ཡིན་ན་འདི་ཡང༌[^439]བགྲོད་པར་བྱ་བའི་ཡུལ་དུ་སོན་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་བྱུང་བ་མ་ཡིན་ནོ། །

[Block 1196]
འཆི་བའི་སྲིད་པ་ཆད་པ་ཁོ་ན་ལས་སྐྱེ་བའི་སྲིད་པ་འབྱུང་ངོ་ཞེས་ཁ་ཅིག་གིའོ།[^440] །

[Block 1197]
དེ་ཡང་།

[Block 1198 [VERSE]]
འབྲུ་ཡི་རྒྱུན་དང་ཆོས་མཐུན་ཕྱིར། །
སྲིད་པ་ཆད་ལས་འབྱུང་བ་མིན། །

[Block 1199]
རྒྱུན་གྱིས༌[^441]འཇུག་པའི་ཆོས་རྣམས་ནི་རྒྱུན་མི་ཆད་པར༌[^442]ཡུལ་གཞན་དག་ཏུ་འབྱུང་བར་མཐོང་སྟེ། དཔེར་ན་འབྲུའི༌[^443]རྒྱུན་ལྟ་བུའོ། །

[Block 1200]
ཆད་ནས་འབྱུང་བ་ཡང་མཐོང་སྟེ། དཔེར་ན་མེ་ལོང་ལ་སོགས་པ་དག་གི་ནང་དུ་གཟུགས་ལས་གཟུགས་བརྙན་ལྟ་བུའོ་ཞེས་ཟེར་རོ། །

[Block 1201 [VERSE]]
གཟུགས་བརྙན་མ་གྲུབ་ཕྱིར་བ་དང་། །
མི་འདྲའི་ཕྱིར་ན་དཔེ་མ་ཡིན། །

[Block 1202]
གཟུགས་བརྙན་ཞེས་བྱ་བ་གཞན་ཁོ་ན་ཞིག་འབྱུང་ངོ་ཞེས་བྱ་བ་དེ་ནི་མ་གྲུབ་སྟེ། གྲུབ་ཏུ་ཟིན་ཡང་མི་འདྲ་བའི་ཕྱིར་དཔེ་མ་ཡིན་ནོ། །

[Block 1203]
འོ་ན་ཇི་ལྟར་མ་གྲུབ་ཅེ་ན། གཅིག་ན་ལྷན་ཅིག་གཉིས་མེད་ཕྱིར། །ཡུལ་དེ་ཉིད་ན་མེ་ལོང་གི་གཟུགས་ཀྱང་སྣང་གཟུགས་བརྙན་ཀྱང་སྣང་།[^444] རྟེན་གྱི་འབྱུང་བ་ཐ་དད་པའི་ཕྱིར་ཡུལ་གཅིག་ཏུ་གཟུགས་གཉིས་ལྷན་ཅིག་འབྱུང་བ་ནི་མེད་དེ། [^445]རེ་ཞིག་མ་གྲུབ་པའི་ཕྱིར་ཏེ། དེ་ལྟ་བུ་ཡིན་ནོ། །ཇི་ལྟར་མི་འདྲ་ཞེ་ན། རྒྱུན་མིན་ཕྱིར། ཇི་ལྟར༌[^446]འཆི་བའི་སྲིད་པའི་སྐྱེ་བའི་སྲིད་པ་ལྟ་བུར་གཟུགས་བརྙན་ནི་གཟུགས་ཀྱི་རྒྱུན་དུ་གྱུར་པ་མ་ཡིན་ཏེ། མེ་ལོང་གི་རྒྱུད་དང་འབྲེལ་པའི་ཕྱིར་དང་། ལྷན་ཅིག༌[^447]འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1204]
རྒྱུན་ལ་རྒྱུན་མི་འཆད་པར་འབྱུང་བར་བརྗོད་པའི་ཕྱིར་དཔེ་མི་འདྲ་བ་ཡིན་ནོ། །

[Block 1205]
གཟུགས་བརྙན་ནི་གཉིས་ལས་འབྱུང་ཕྱིར། གཟུགས་བརྙན་གྱི་གཟུགས་དང་མེ་ལོང་གཉིས་ལས་འབྱུང་བར་འགྱུར་ཏེ། སྐྱེ་བའི་སྲིད་པ་ཡང་འཆི་བའི་སྲིད་པ་དང་གཞན་ལ་ནི་མི་འབྱུང་བས་མི་འདྲའོ། །

[Block 1206]
དེ་བས་ན་སྲིད་པ་བར་མ་ནི་ཡོད་དོ། །

[Block 1207]
མགུར་ནས་གསུངས་ཕྱིར་ཡོད་དོ།[^448] །

[Block 1208]
མདོ་ལས་སྲིད་པ་ནི་བདུན་ཏེ། དམྱལ་བའི་སྲིད་པ་དང་། དུད་འགྲོའི་སྲིད་པ་དང་། ཡི་དགས་ཀྱི་སྲིད་པ་དང་། ལྷའི་སྲིད་པ་དང་། མི་ཡི་སྲིད་པ་དང་། ལས་ཀྱི་སྲིད་པ་དང་། སྲིད་པ་བར་མའོ་ཞེས་གསུངས་སོ། །

[Block 1209]
དྲི་ཟ་གནས་གསུམ་མངོན་དུ་གྱུར་པས་མའི་མངལ་དུ་བུ་ཆགས་པར་འགྱུར་ཏེ། མ་རུང་ཞིང་ཟླ་མཚན་དང་ལྡན་པ་དང་། ཕ་མ་ལ་ཆགས་པར་གྱུར་ཅིང་ཕྲད་པ་དང་། དྲི་ཟ་ཡང་ཉེ་བར་གནས་པར་གྱུར་ནའོ། །

[Block 1210]
སྲིད་པ་བར་མ་མ་གཏོགས་པ༌[^449]དྲི་ཟ་གང་ཞིག་ཡིན། དེའི་ཕྱིར་བར་མའི་སྲིད་པ་ནི་ཡོད་དོ། །

[Block 1211]
ལྔར༌[^450]གསུངས་པ། བར༌[^451]མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་ལ་སོགས་པ་ཕྱིར་མི་འོང་བ་ལྔར༌[^452]གསུངས་ལ། སྲིད་པ་བར་མ་མེད་ན་ཇི་ལྟར་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་འབྱུང་།

[Block 1212]
[^453]འདི་ལས་ཀྱང་འགྲོ་བའི་མདོ་སྡེ་ལས།

[Block 1213]
སྐྱེས་བུ་དམ་པའི་འགྲོ་བ་བདུན། །ཞེས་བྱ་བའི་མདོ་ལས་དུས་དང་ཡུལ་གྱི་ཁྱད་པར་གྱི་བྱེ་བྲག་བར་མ་དོར་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་གསུམ་དུ་བཤད་དེ། དཔེར་ན་ལྕགས་ཀྱི་ཚ་ཚ་བཞིན་ནོ་ཞེས་བྱ་བ་དེའི་ཕྱིར་ཡང་ཡོད་དོ། །

[Block 1214]
ཡང་འགྲོ་བ་གང་དུ་འགྲོ་བར་འགྱུར་བའི་སྲིད་པ་བར་མའི་ཤ་ཚུགས་ཇི་ལྟ་བུ་ཞིག་མངོན་པར་འགྲུབ་ཅེ་ན།

[Block 1215 [VERSE]]
དེ་ནི་འཕེན་པ་གཅིག་པའི་ཕྱིར། །
སྔོན་དུས་སྲིད་འབྱུང་ཤ་ཚུགས་ཅན། །

[Block 1216]
ལས་གང་གིས་འགྲོ་བ་འཕེན་པ་དེ་ཉིད་ཀྱིས་དེར་ཕྱིན་པར་བྱ་བའི་ཕྱིར་སྲིད་པ་བར་མ་ཡང་འཕེན་ཏེ། དེའི་ཕྱིར་དེ་ནི་འགྲོ་བ་གང་དུ་འགྲོ་བ༌[^454]དེར་དུས་སྔ་མའི་སྲིད་པ་འབྱུང་བར་འགྱུར་བ་དེའི་ཤ་ཚུགས་ལྟ་བུར་འགྱུར་རོ། །

[Block 1217]
ཡང་སྲིད་པ་སྔ་མ་ཞེས་བྱ་བ་འདི་གང་ཡིན་ཞེ་ན།

[Block 1218 [VERSE]]
དེ་ནི་འཆི་བའི་སྔ་རོལ་ཏེ།
སྐྱེ་བའི་སྐད་ཅིག་ཕན་ཆད་དོ། །

[Block 1219]
སྐྱེ་བའི་སྐད་ཅིག་ཕན་ཆད་ནས་འཆི་བའི་སྐད་ཅིག་མ་གཏོགས་པ་ནི་སྔ་མའི་སྲིད་པ་ཡིན་ནོ། །

[Block 1220]
སྲིད་པ་བར་མ་དེ་ཡང་། རིས་མཐུན་ལྷ་མིག་དག་པས་མཐོང་། །སྲིད་པ་བར་མ་རིས་མཐུན་པ་དག་ཁོ་ནས་མཐོང་ངོ་། །གང་དག་ལ་ལྷའི་མིག་རྣམ་པར་དག་པས༌[^455]མངོན་པར་ཤེས་པ་ལས་བྱུང་བ་དེ་དག་གིས་ཀྱང་འདི་མཐོང་ངོ་། །

[Block 1221 [VERSE]]
ལས་ཀྱི་རྫུ་འཕྲུལ་ཤུགས་དང་ལྡན། །
རྫུ་འཕྲུལ་ནི་ནམ་མཁའ་ལ་འགྲོའོ། །

[Block 1222]
ལས་ཀྱི་རྫུ་འཕྲུལ་བྱེད་པས་ན་ལས་ཀྱི་རྫུ་འཕྲུལ་ལོ། །

[Block 1223]
དེའི་ཤུགས་ནི་ལས་ཀྱི་རྫུ་འཕྲུལ་གྱི་ཤུགས་ཏེ་མགྱོགས་པ་ཉིད་དོ། །

[Block 1224]
དེ་འདི་ལ༌[^456]ཡོད་པས་ན་ལས་ཀྱི་རྫུ་འཕྲུལ་གྱི་ཤུགས་དང་ལྡན་པའོ། །

[Block 1225]
དབང་པོ་ཀུན་ཚང་། དབང་པོ་ལྔ་ཆར་ཚང་བའོ། །

[Block 1226]
ཐོགས་མེད་ལྡན། འདི་ལ་གང་དུ་ཡང་ཐོགས་པ་མེད་པའོ། །

[Block 1227]
མི་ཟློགས། སྲིད་པ་བར་མ་དོར་ནས་ལྷའི་སྲིད་པ་བར་མའམ། གཞན་དུ་འགྱུར་བ་ནི་མི་སྲིད་དོ། །

[Block 1228]
ཁམ་གྱི༌[^457]ཟས་ཀྱིས་གནས་པ་ཡིན་ཡང་རགས་པ་ནི་མི་ཟ་སྟེ། འོན་ཀྱང་དེ་ནི་དྲི་ཟའོ། །

[Block 1229]
དེ་ནི་དྲི་ཟ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1230]
ཡང་འགྲོ་བའི་ཡུལ་དུ་ཕྱིན་པར་བྱ་བའི་ཕྱིར་འབྱུང་བའི་སྲིད་པ་བར་མ་དེ་ནི།
--- END BLOCKS ---
