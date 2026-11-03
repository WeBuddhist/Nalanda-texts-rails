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
[Block 1226 [HEADING]]
##### སྦྱིན་པ་ཐམས་ཅད་ཀྱི་ནང་ན་མཆོག། ^1-71-1-5-0

[Block 1227 [VERSE]]
སྦྱིན་པ་ཐམས་ཅད་ཀྱི་ནང་ན། །
མཆོག་ནི་གྲོལ་བས་གྲོལ་བ་ལའང་། །

[Block 1228]
འདོད་ཆགས་དང་བྲལ་བས་འདོད་ཆགས་དང་བྲལ་བ་ལ་བྱིན་པའི་སྦྱིན་པ་གང་ཡིན་པ་དེ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཟང་ཟིང་གི་སྦྱིན་པ་རྣམས་ཀྱི་ནང་ནས་མཆོག་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 1229]
བྱང་ཆུབ་སེམས་དཔའ་ཡིས། ཡང་ན་བྱང་ཆུབ་སེམས་དཔས༌[^884]སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པར་བྱ་བའི་ཕྱིར་སྦྱིན་པ་སྦྱིན་པར་བྱེད་པའི་སྦྱིན༌[^885]པ་གང་ཡིན་པ་དེ་ནི་གྲོལ་བ་མ་ཡིན་པས་མ་གྲོལ་བ་རྣམས་ལ་ཡང་བྱིན་ན༌[^886]མཆོག་ཡིན་ནོ། །

[Block 1230]
དེ་མ་གཏོགས་པ་བཅོམ་ལྡན་འདས་ཀྱིས༌[^887]གང་དག་སྦྱིན་པ་བརྒྱད་གསུངས་པ་དེ་དག་གི་ནང་ན་ནི་བརྒྱད་པ་མཆོག་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1231]
བརྒྱད་གང་ཞེ་ན། ཉེ་བ་ལ་སྦྱིན་པ་དང་། འཇིགས་པས་སྦྱིན་པ་དང་། བདག་ལ་བྱིན་པས་སྦྱིན་པ་དང་། བདག་ལ་སྦྱིན་པར་འགྱུར་བས་སྦྱིན་པ་དང་། སྔོན་བདག་གི་ཕ་དང་མེས་པོ་དག་གིས་སྦྱིན་པ་བྱིན་པས་སྦྱིན་པ་བྱིན་པ་དང་། མཐོ་རིས་ཀྱི་དོན་དུ་སྦྱིན་པ་དང་། གྲགས་པའི་དོན་དུ་སྦྱིན་པ་དང་། སེམས་ཀྱི་རྒྱན་གྱི་དོན་དང་། སེམས་ཀྱི་ཡོ་བྱད་ཀྱི་དོན་དང་། རྣལ་འབྱོར་གྱི་ཚོགས་ཀྱི་དོན་དང་། དོན་གྱི་མཆོག་ཐོབ་པར་བྱ་བའི་ཕྱིར་སྦྱིན་པ་བྱིན༌[^888]པའོ། །

[Block 1232]
དེ་ལ་ཉེ་བ་ལ་སྦྱིན་པ་ནི་སྔ་མ་དག་ན་རེ་ནམ་ཉེ་བར་གྱུར་ཅིང་ཉེ་བར་ལྷགས་པ་དག་ལ་སྦྱིན་པར་བྱེད༌[^889]པའོ་ཞེས་ཟེར་རོ། །

[Block 1233]
འཇིགས་པས་སྦྱིན་པ་ནི་མེད་པར་བྱེད་པ་མངོན་སུམ་དུ་མཐོང་ནས་དམ་པ་སྦྱིན་ནོ་ཞེས་སྦྱིན་པར་བྱེད་པ་གང་ཡིན་པའོ། །

[Block 1234]
ལྷག་མ་ནི་གོ་སླ་བས་རྣམ་པར་མ་ཕྱེའོ། །

[Block 1235 [HEADING]]
##### ཡོན་གཞལ་དུ་མེད་པ། ^1-71-1-6-0

[Block 1236]
མདོ་ལས་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་ཞུགས་པ་ལ་སྦྱིན་པ་བྱིན་ན་རྣམ་པར་སྨིན་པ་གཞལ་དུ་མེད་དོ། །

[Block 1237]
རྒྱུན་དུ་ཞུགས་པ་ལ་བྱིན་ན་དེ་བས་ཀྱང་ཆེས་གཞལ་དུ་མེད་དོ་ཞེས་བྱ་བ་རྒྱས་པར་གསུངས་མོད་ཀྱི། གཞན་ཡང་།

[Block 1238 [VERSE]]
འཕགས་པ་མིན་ཡང་ཕ་མ་དང་། །
ནད་པ་དང་ནི་ཆོས་སྨྲ་དང་། །
སྐྱེ་མཐའི་བྱང་ཆུབ་སེམས་དཔའ་ལ། །
ཡོན་ནི་གཞལ་དུ་མེད་པ་ཡིན། །

[Block 1239]
ལྔ་པོ་འདི་དག་ལ་ནི་སོ་སོའི་སྐྱེ་བོར་གྱུར་པ་ཡིན་ཡང་འབྲས་བུའི་སྒོ་ནས་ཡོན་གཞལ་དུ་མེད་པ་ཡིན་ནོ། །

[Block 1240]
དེ་ལ་སྐྱེ་བ་ཐ་མ་པའི༌[^890]བྱང་ཆུབ་སེམས་དཔའ་ནི་སྲིད་པ་ཐ་མ་པ་ཡིན་ནོ། །

[Block 1241]
ཆོས་སྨྲ་བ་ཞིང་གི་ཁྱད་པར་རྣམ་པ་བཞི་པོའི་ཕྱོགས་གང་དུ་གཏོགས་པར་བྱ་ཞེ་ན། ཕན་འདོགས་པའི་ཕྱོགས་སུ་གཏོགས་ཏེ། དེ་ནི་སྐྱེ་དགུ་མ་རིག་པས་ལྡོངས་པ་རྣམས་ལ་ཤེས་རབ་ཀྱི་མིག་སྦྱིན་པར་བྱེད་པ་དང་། མཐུན་པ་དང་མི་མཐུན་པ་རབ་ཏུ་སྟོན་པར་བྱེད་པ་དང་། ཆོས་ཀྱི་སྐུ་ཟག་པ་མེད་པ་མངོན་པར་སྒྲུབ་པར་བྱེད་པ་དང་། མདོར་ན་སངས་རྒྱས་ཀྱི་མཛད་པ་ཐམས་ཅད་བྱེད་པ་ཡིན་པས་དགེ་བའི་བཤེས་གཉེན་ཆེན་པོ་ཡིན་ནོ། །

[Block 1242 [HEADING]]
##### ལས་རྣམས་ཀྱི་ལྕི་བ་དང་ཡང་བ། ^1-71-1-7-0

[Block 1243]
ལས་རྣམས་ཀྱི་ལྕི་བ་དང་། ཡང་བ་ཉིད་ཤེས་པར་འདོད་པས་མདོར་ན་རྒྱུ་དྲུག་ཤེས་པར་བྱ་སྟེ། འདི་ལྟ་སྟེ།

[Block 1244 [VERSE]]
མཇུག་དང་ཞིང་དང་གཞི་དང་ནི། །
སྦྱོར་དང་སེམས་པ་བསམ་པ་སྟེ། །

[Block 1245]
དེ་དག་ཆུང་དང་ཆེ་བ་ལས།

[Block 1246]
[^891] །ལས་ཀྱང་ཆུང་དང་ཆེ་བ་ཉིད། །མཇུག་ཅེས་བྱ་བ་ནི་བྱས་པའི་རྗེས་ལ་བྱེད་པ་གང་ཡིན་པའོ། །

[Block 1247]
ཞིང་ཞེས་བྱ་བ་ནི་གང་དུ་ཕན་པ་དང་གནོད་པ་དག་བྱེད་པའོ། །

[Block 1248]
གཞི་ནི་ལས་ཀྱི་ལམ་མོ། །

[Block 1249]
སྦྱོར་བ་ནི་དེའི་དོན་དུ་ལུས་དང་ངག་གིས༌[^892]ལས་བྱེད་པའོ། །

[Block 1250]
སེམས་པ་ནི་གང་གིས་ལས་ཀྱི་ལམ་མཐར་ཕྱིན་པར་བྱེད་པའོ། །

[Block 1251]
བསམ་པ་ནི་དེ་དག་ལ་དེ་དང་འདི་ལྟ་བུ་ཞིག་ནི་བྱའོ། །

[Block 1252]
དེ་དང་འདི་ལྟ་བུ་ཞིག་ནི་ཕྱིས་བྱའོ་སྙམ་དུ་སེམས་པ་སྟེ། ལ་ལའི་མཇུག་ཡོངས་སུ་བཟུང་བ་ཁོ་ན༌[^893]ལས་དེ་ལྕི་བར་འགྱུར་ཏེ། རྣམ་པར་སྨིན་པར༌[^894]ངེས་པར་གནས་པའི་ཕྱིར་རོ། །

[Block 1253]
ལ་ལའི་ནི་ཞིང་གི་དབང་ཁོ་ནས་སོ། །

[Block 1254]
ཞིང་དེ་ཉིད་ལ་གཞིའི་དབང་གིས་ལྕི་བར་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ཏེ། ཇི་ལྟར་ཕ་དང་མ་ལ་སྲོག་གཅད་པས༌[^895]ལྕི་བར་འགྱུར་བ་ལྟར་མ་བྱིན་པར་བླངས་པ་ལ་སོགས་པས་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 1255]
དེ་བཞིན་དུ་གཞན་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 1256]
གང་གི་ཐམས་ཅད་ཆེ་བ་ཡིན་པ་དེ་ནི་ལས་ཀྱང་ཤིན་ཏུ་ཆེས་ལྕི་བ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1257]
གང་གི་ཆུང་ངུ་ཡིན་པ་དེ་ནི་ཤིན་ཏུ་ཆུང་བ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1258 [HEADING]]
##### བསགས་པའི་ལས། ^1-71-1-8-0

[Block 1259]
ལས་བྱས་པ་དང་བསགས་པ་ཞེས་བྱ་བ་ཇི་ལྟར་ན་ལས་བསགས་པ་ཡིན་ཞེ་ན།

[Block 1260 [VERSE]]
བསམས་བཞིན་པ་དང་རྫོགས་པ་དང་། །
མི་འགྱོད་གཉེན་པོ་མེད་པ་དང་། །
འཁོར་དང་རྣམ་པར་སྨིན་པ་ལས། །
བསགས་པའི་ལས་ཞེས་བྱ་བ་བཞིན། །

[Block 1261]
བསམས་བཞིན་པ༌[^896]ལས་ཇི་ལྟ་བུ་ཞེ་ན། ཆེད་དུ་བསམས་ནས་བྱས་པ་ཡིན་གྱི་བློ་སྔོན་དུ་མ་བཏང་བ་ཡང་མ་ཡིན་ལ་བབ་ཅོལ་དུ་བྱས་པ་ཡང་མ་ཡིན་པའོ། །

[Block 1262]
རྫོགས་པས་ཇི་ལྟ་བུ་ཞེ་ན། ཁ་ཅིག་ནི་ཉེས་པར་སྤྱད་པ་གཅིག་གིས་ངན་སོང་དུ་འགྲོ་ལ། ཁ་ཅིག་ནི་གསུམ་གྱི་བར་གྱིས་འགྲོ་བ་དང་། ཁ་ཅིག་ནི་ལས་ཀྱི་ལམ་གཅིག་གིས་ངན་སོང་དུ་འགྲོ་ལ། ཁ་ཅིག་ནི་བཅུའི་བར་གྱིས་འགྲོ་བ་དེ༌[^897]གང་ཞིག་གིས་ཇི་ཙམ་གྱིས་དེར་འགྲོ་བར་འགྱུར་བ་རྫོགས་པར་མ་བྱས་ན་ཡང་ལས་དེ་བྱས་པ་ཡིན་གྱི་བསགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1263]
རྫོགས་ན་ནི་བསགས་པ་ཡིན་ནོ། །

[Block 1264]
མི་འགྱོད་པ་དང་། གཉེན་པོ་མེད་པས་ཇི་ལྟ་བུ་ཞེ་ན། ལས་དེ་ལ་ཡིད་ལ་གཅགས་པ་མེད་པ་དང་། གཉེན་པོ་མེད་པ་ཡིན་ནོ། །

[Block 1265]
འཁོར་ལས་ཇི་ལྟ་བུ་ཞེ་ན། མི་དགེ་བ་ལ་འཁོར་ཡང་མི་དགེ་བ་མ༌[^898]ཡིན་ནོ། །
--- END BLOCKS ---
