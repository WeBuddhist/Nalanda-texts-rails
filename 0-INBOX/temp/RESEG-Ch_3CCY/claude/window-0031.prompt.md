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

[Block 1091]
གལ་ཏེ་དེ་མེད་ན་འབྱུང་བ་ཆེན་པོ་བཞི་དག་རྒྱུར་བྱས་སོ་ཞེས་འབྱུང་བའི་རྒྱུ་ཅན་དུ་སྟོན་པར་མི་འགྱུར་ཏེ། ཡོད་བཞིན་པ་མ་ཡིན་པའི་ནམ་མཁའི་མེ་ཏོག་ལ་འབྱུང་བ་རྒྱུར་བྱས་པ་ཉེ་བར་མ་བསྟན་ལ། དེའི་ཕྱིར་འཇིག་རྟེན་པ་དང་། ལུང་ལས་གྲགས་པའི་ཕྱིར་གཟུགས་ཡོད་དོ་གཟུགས་ཡོད་པར་གྱུར་ན་དེ་ལ་འཛིན་པའི་དབང་པོའི་ཤེས་པ་འབྱུང་བར་འགྱུར་ལ། དེ་ཡོད་ན་ཡང་དེ་བཞིན་ཁོ་ནར་དངོས་པོ་ཐམས་ཅད་གྲུབ་པོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་གཟུགས་ཉིད་ཡོད་ན་གཟུགས་ལ་བརྟེན་ནས༌[^788]དངོས་པོ་ཐམས་ཅད་འགྲུབ་པར་འགྱུར་ན། ཡོད་པ་མ་ཡིན་ལ། ཇི་ལྟར་མེད་པ་ཡང་དེ་ལྟར་སྔར་ཉིད་དུ་རྒྱས་པར་བསྒྲུབས་ལ། གཞན་ཡང་གལ་ཏེ༌[^789]མེད་པས་གཟུགས་མེད་པར་གྲུབ་ཀྱང་། དེ་ལྟ་ན་ཡང་ཤིན་ཏུ་རགས་པ་དང་ཉེ་བ་འདི་དག་མངོན་སུམ་དུ་དམིགས་པ༌[^790]བཞིན་དུ༌[^791]ཆགས་པའི་གནས་སུ་གྱུར་པའི་ཕྱིར། དེས་ན་དེ་སེལ་བའི་སྒོ་ནས་སྐྱེ་མཆེད་ཐམས་ཅད་དགག་པའི་དོན་དུ་སླར་ཡང་བརྟག༌[^792]པ་ཙམ་པའི༌[^793]ཕྱིར་གསུངས་པ།

[Block 1092 [HEADING]]
### ཚིགས་བཅད་ཞེ་ལྔ་པ། ^1-45-0

[Block 1093 [VERSE]]
གལ་ཏེ་འབྱུང་བའི་རང་བཞིན་གཟུགས། །
འབྱུང་ལས་གཟུགས་ནི་འབྱུང་བ་མིན། །
རང་ལས་འབྱུང་མིན་གཞན་ལས་ཀྱང་། །
འབྱུང་མིན་དེ་ཕྱིར་མེད་མིན་ནམ། །

[Block 1094]
གལ་ཏེ་འདི་སྙམ་དུ་སེམས་ན། གང་ལས་འབྱུང་བ་ཆེན་པོ་བཞི་ལ་བརྟེན་ནས་གཟུགས་ཉེ་བར་བསྟན་པས། དེའི་ཕྱིར་གཟུགས་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། དེ་ཉིད་ཀྱིས་ན་གཟུགས་རང་བཞིན་མེད་པའོ་ཞེས་གསལ་བར་བཅོམ་ལྡན་འདས་ཀྱིས་བསྟན་པ་མ་ཡིན་ནམ། ཇི་ལྟར་བྱས་ན་གང་ལས་འཇིག་རྟེན་འདིར་རྒྱུ་དང་འདྲ་བའི་འབྲས་བུ་འཇུག་བཞིན་པ་ཉེ་བར་དམིགས་ཏེ། འདི་ལྟ་སྟེ། སཱ་ལུ་ལས་སཱ་ལུ་དང་། གྲོ་ལས་གྲོ་དང་། བ་ལང་ལས་བ་ལང་དང་། བ་མེན་ལས་བ་མེན་ནོ་ཞེས་དེ་བཞིན་དུ་གཟུགས་ཀྱང་འབྱུང་བ་ལས་ཀྱང༌[^794]གྱུར་པས་ན་འབྱུང་བའི་རང་བཞིན་ཁོ་ནར་འཇུག་པར་འགྱུར་ལ་རག་ན། གཟུགས་ཀྱང་འབྱུང་བའི་རང་བཞིན་མ་ཡིན་ཏེ། སྲ་བ་ལ་སོགས་པ་མ་ཡིན་པའི་ངོ་བོའི་ཕྱིར་དང་། འབྱུང་བ་རྣམས་ལུས་ཀྱི་དབང་པོའི་གཟུང་བྱའི་ཕྱིར་དང་། གཟུགས་ནི་མིག་གི་དབང་པོའི་གཟུང་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1095]
བཅོམ་ལྡན་འདས་ཀྱིས་འབྱུང་བ་རྒྱུར་བྱས་ནས་གཟུགས་འབྱུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡང་། གཟུགས་ལ་རིགས་པ་དང་འགལ་བར་གསུངས་པའོ་ཞེས་མཚོན་པས་འཇིག་རྟེན་པ་རྣམས་ཀྱིས་དེ་མི་བདེན་པར་ཁོང་དུ་ཆུད་པར་བྱ་བའི་དོན་དུའོ། །

[Block 1096]
དེའི་ཕྱིར་ལུང་ནི་གཟུགས་ཡོད་པ་ཉིད་ཀྱི་སྒྲུབ་བྱེད་མ་ཡིན་ལ། འོན་ཀྱང་གཟུགས་མེད་པའི་སྒྲུབ་བྱེད་དོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 1097]
གལ་ཏེ་འབྱུང་བའི་རང་བཞིན་གཟུགས། །འབྱུང་ལས་གཟུགས་ནི་འབྱུང་བ་མིན། །

[Block 1098]
འབྱུང་བའི་རང་བཞིན་ཞེས་པ་འདི་ནི་རྒྱུ་ལ་རང་བཞིན་དུའོ། །

[Block 1099]
ཁ་ཟས་ཀྱི་རང་བཞིན་སྲོ་ག་ལ། རྩྭའི་རང་བཞིན་བ་ལང་ཞེས་པའོ། །

[Block 1100]
ཇི་ལྟར་གལ་ཏེ་འབྱུང་བའི་རང་བཞིན་ཏེ། འབྱུང་བའི་རྒྱུ་ཅན་གྱི་གཟུགས་སུ་སྐྱེས་པ་དེ་ནི་འབྱུང་བ་ལས་མི་འབྱུང་སྟེ། འབྱུང་བའི་རང་བཞིན་གྱིས་ཡོད་པ་མ་ཡིན་པས། དེ་ལྟར་གྱུར་ན་རྒྱུ་དང་མི་འདྲ་བའི་འབྲས་བུ་སྐྱེ་བ་མི་སྲིད་པས་དེ་ནི་གཟུགས་ཀྱི་རང་བཞིན་མ་ཡིན་པ་མ་ཡིན་ཞེས་བྱ་སྟེ་གོ་སླའོ། །

[Block 1101]
གལ་ཏེ་དེ་ལྟར་རྒྱུ་དང་འབྲས་བུ་དག་མཚན་ཉིད་ཐ་དད་པའི་ཕྱིར་གཟུགས་ཀྱི་རང་བཞིན་ལས་མ་ཡིན་ཡང་། དེ་ལྟ་ན་ཡང་གཞན་དངོས་ལས་འབྱུང༌[^795]ངོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་གཟུགས་ནི་རང་དངོས་ལས་འབྱུང་མིན། །ཞེས་གནས་ལ། དེའི་ཚེ་དེ་མེད་པ་སྟེ། རང་གི་དངོས་ལས་གཞན་ལས་མ་ཡིན་ནོ་ཞེས་གསལ་བར་ངེས་སོ། །

[Block 1102]
རང་བཞིན་ནི་རང་བཞིན་གཞན་ལ་ལྟོས་ནས་གཞན་ཉིད་དུ་འགྱུར་ལ། རང་བཞིན་དེ་ཡང་མེད་པས་རང་བཞིན་གཞན་ལས་ཀྱང་སྐྱེས་པ༌[^796]མེད་དོ།། །།

[Block 1103]
གཞན་ཡང་གལ་ཏེ་འབྱུང་བ་ཆེན་པོ་བཞི་ལ་བརྟེན་ནས་གཟུགས་ཀྱི་སྐྱེ་མཆེད་འབྱུང་ངོ་ཞེས་པ་དེ་ལྟར་གྱུར་ན་གཟུགས་ཀྱི་སྐྱེ་མཆེད་གཅིག་པུ་ལ་རྣམ་པ་བཞིར་ཐོབ་པར་འགྱུར་ཏེ། གཅིག་ལ་ཕན་ཚུན་མཚན་ཉིད་ཐ་དད་པའི་བདག་ཉིད་བཞི་བརྟེན་པར་མི་འཐད་དེ། དེའི་ཕྱིར་གཟུགས་ནི་རྣམ་པ་བཞིར་ཁས་བླང་བར༌[^797]བྱ་བའམ། གལ་ཏེ་སྐྱེ་མཆེད་གཅིག་གི་རྟེན་གྱི་དངོས་པོར་རྟོག་ན་ཡང་འབྱུང་བ་རྣམས་གཅིག་ཉིད་དུ་ཁས་བླང་བར་བྱའོ། །

[Block 1104]
འདི་དག་ཀྱང་དེ་ལྟར་མེད་དོ་ཞེས་བསྒྲུབ་པའི་ཕྱིར་གསུངས་པ།

[Block 1105 [HEADING]]
### ཚིགས་བཅད་ཞེ་དྲུག་པ། ^1-46-0

[Block 1106 [VERSE]]
གཅིག་ལ་བཞི་ནི་ཡོད་མ་ཡིན། །
བཞི་གང༌[^798]གཅིག་ཏུ་མ་ཡིན་པས། །
གཟུགས་ནི་འབྱུང་བ་ཆེན་པོ་བཞི། །
རྒྱུར་བྱས་ནས་གྲུབ་ཇི་ལྟར་ཡོད། །

[Block 1107]
གལ་ཏེ་འབྱུང་བ་ཆེན་པོ་བཞི་ཡོད་བཞིན་པ་ལ་གཟུགས་བརྟེན་པར་གྱུར་ན། དེའི་ཚེ་གཟུགས་གཅིག་ཀྱང་བཞིར་འགྱུར་ཏེ། བརྟེན་པ་ནི་རྟེན་གྱི་དབྱེ་བའི་རྗེས་སུ་འབྲེལ་བའི་ཕྱིར་རོ། །

[Block 1108]
དེ་ལྟར་ཡོད་པ་ཡང་མ་ཡིན་པས་གཟུགས་ནི་འབྱུང་བ་ཆེན་པོ་བཞི་རྒྱུར་བྱས་ནས་གྲུབ་པར་ཅི་ལྟར༌[^799]ཡོད། ཡང་ན་རྟེན་ཐ་དད་ཀྱི་རྗེས་སུ་མཐུན་པ་བརྟེན་པའི༌[^800]གཟུགས་མ་ཡིན་ན། དེ་ལྟར་ན་རྟེན་དུ་གྱུར་པ་རྣམས་བརྟེན་པ་གཅིག་གི་རྗེས་སུ་འཇུག་པར་བྱོས་ཤིག །དེ་དག་ཀྱང་མི་སྲིད་ལ། དེའི་ཕྱིར་གར་གྱི་སྐྱེས་བུ་བཞིན་དུ་ཕན་ཚུན་མི་བདེན་པ་རྣམས་ངེས་པར་འདི་དག་གི་ཡོད་པ་ཉིད་ཉམས་སོ་ཞེས་བྱ་སྟེ། གཟུགས་ནི་འབྱུང་བ་ཆེན་པོ་བཞི་རྒྱུར་བྱས་ནས་གྲུབ་པ་ཇི་ལྟར་ཡོད། འདིར་སྨྲས་པ། གཟུགས་ནི་ཡོད་པ་ཉིད་དེ། འཛིན་བཞིན་པའི་ཕྱིར། འདིར་མིག་གི་རྣམ་པར་ཤེས་པ་དེའི་སྔོན་པོའི་རྣམ་པར་སྐྱེས་པས་འཛིན་ལ། དེ་ལ་གལ་ཏེ་སྔོན་པོ་མེད་ན་དེའི་འཛིན་པ་མི་འབྱུང་ལ། འཛིན་པ་ཡང་ཡོད་པས་དེའི་ཕྱིར་གཟུགས་ཡོད་དོ་ཞེ་ན། སྨྲས་པ། གལ་ཏེ་དེའི་འཛིན་པ་ཡོད་ན་གཟུགས་ཡོད་ལ། འདི་ལ་འཛིན་པ་མི་སྲིད་དོ། །

[Block 1109]
དེའི་ཕྱིར་ཤིན་ཏུ་ཡང་འཛིན་པ་མེད་པས། གཟུགས་ནི་ཇི་ལྟར་ཞེས་པ་འདིར་འབྲེལ་ཏོ། །

[Block 1110 [HEADING]]
### ཚིགས་བཅད་ཞེ་བདུན་པ། ^1-47-0

[Block 1111]
འདི་དག་གི་ཤིན་ཏུ་མི་འཛིན་པ་ཡང་རྒྱས་པར་བསྒྲུབ་པར་བྱ་སྟེ། འདིར་སྨྲས་པ། གཟུགས་ལ་འཛིན་པ་ནི་ཡོད་པ་ཉིད་དོ།[^801] །རྟགས་ཅི་ལས་ཤེ་ན། གལ་ཏེ་གཟུགས་འཛིན་པར་མི་འགྱུར་ན་འདི་ནི་གཟུགས་སོ་ཞེས་པའི་བློ་མི་འབྱུང་ལ། འདིའི་བློ་ཡང་ཡོད་པས་ཤེས་བྱ་སྟེ། རྟགས་དེས་ན་འཛིན་པ་ཡོད་དོ་ཞེས་བྱའོ། །

[Block 1112]
སྨྲས་པ། རྟགས་ལས་ཤེ་ན་དེའི་རྟགས་ཀྱང་མེད་དེ། རྒྱུ་དང་རྐྱེན་ལས་སྐྱེས་པའི་ཕྱིར་མེད་པ་ཉིད་དོ། །

[Block 1113]
གཞན་ཡང་གཟུགས་ཡོད་ན་གཟུགས་ཀྱི་བློ་འཐད་ཀྱི་མེད་པ་ལ་མ་ཡིན་ནོ། །

[Block 1114]
གང་གི་ཚེ་འདི་དག་དེ་ལྟ་ན་དེའི་ཚེ་ཡོད་པའི༌[^802]གཟུགས་ཀྱི་གཟུགས་ཀྱིས༌[^803]བློ་སྐྱེད་པར་བྱེད་ན་གཟུགས་ཡོད་པར་རུང་ན། གཟུགས་ཀྱི་བློ་མེད་ན་ཇི་ལྟར་གཟུགས་ཡོད་པའི་རྟགས་སུ་འགྱུར་ཞེས༌[^804]གསུངས་པ། ཡོད་ན་ཡང་རྟགས་དེ༌[^805]མེད་ན་མི་འཐད་པས་ཞེས༌[^806]བྱ་སྟེ། དེ་ཉིད་ཤིན་ཏུ་མི་འཛིན་པའི་ཕྱིར་རོ། །

[Block 1115]
རྟགས་ལས་ཤེ་ན། རྟགས་དེ་ཡང་མེད་དེ། རྒྱུ་དང་རྐྱེན་ལས་སྐྱེས་པའི་ཕྱིར། ཡོད་ནའང་རྟགས་དེ་མེད་མི་རིགས། །ཞེས་པ་འདིས། ཕ་རོལ་གྱི་རྟགས་ལས་གཟུགས་ཡོད་པ་ཉིད་དུ་ཁས་བླངས་པ་དེ་སེལ་ཏོ། །

[Block 1116]
འདིར་སྨྲས་པ། གང་འདི་སྐད་དུ་ཤིན་ཏུ་མི་འཛིན་པའི་ཕྱིར་ཞེས་སྨོས་པ་དེ་ནི་མི་རིགས་ཏེ། གཟུགས་འཛིན་བཞིན་པའི་ཕྱིར་རོ་ཞེས་བྱའོ། །

[Block 1117]
འདིར་སྨྲས་པ། སླར་ཡང་ཅིས༌[^807]གཟུགས་འཛིན་ན་བློས༌[^808]སོ། །

[Block 1118]
སྨྲས་པ། བློས༌[^809]གཟུགས་ལ་ཇི་ལྟར་འཛིན། དེའི་རྣམ་པར་སྐྱེ་བས་སོ། །

[Block 1119]
སྨྲས་པ། འདི་དག་མི་འཐད་དེ་རྒྱུ་མཚན་ཅིས་ཤེ་ན། གང་གི་ཕྱིར།

[Block 1120 [HEADING]]
### ཚིགས་བཅད་ཞེ་བརྒྱད་པ། ^1-48-0

[Block 1121 [VERSE]]
གལ་ཏེ་བློ་དེས་གཟུགས་འཛིན་ན། །
རང་གི་རང་བཞིན་ལ་འཛིན་འགྱུར། །
རྐྱེན་ལས་སྐྱེས་པས་ཡོད་མིན་ལ། །
ཡང་དག་གཟུགས་མེད་ཇི་ལྟར་འཛིན། །

[Block 1122]
འདིར་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་འཛིན་ན་སྔོན་དུ་རང་གི་བདག་ཉིད་མཐོང་སྟེ། འདི་ལྟ་སྟེ། མེའི་དྲོ་བ་ཉིད་ལྟ་བུ་དེ་དང་ལྡན་པ་ལས་ཕ་རོལ་གྱི་བདག་ཉིད་ཀྱང་ཉེ་བར་དམིགས་པར་བྱེད་དོ།[^810] །ཆུ་ལྟ་བུའོ། །

[Block 1123]
དེ་ལྟར་གལ་ཏེ་བློ་ནི་འཛིན་པའི་རང་བཞིན་དུ་འགྱུར་ན། དེ་ནི་འཛིན་པའི་རང་གི་བདག་ཉིད་ཁོ་ན་ལ་རེ་ཞིག་ཉེ་བར་དམིགས་པར་འགྱུར་ལ། དམིགས་པ་ཡང་མ་ཡིན་ཏེ། བདག་ཉིད་ལ་འཇུག་པ་དང་འགལ་བའི་ཕྱིར་དང་། ལས་དང་བྱེད་པ་པོ་དག་གཅིག་ཉིད་དུ་ཐལ་བ་དང་། དམིགས་པ་མེད་པར་དམིགས་པ་པོ་མི་འཐད་པའི་ཕྱིར་རོ། །

[Block 1124]
གང་གི་ཚེ་འདི་ལྟར་བློ་རང་གི་བདག་ཉིད་ལ་འཛིན་པར་མི་ནུས་པ་དེའི་ཚེ། འདིར་གཟུགས་ཇི་ལྟར་འཛིན་པར་བྱེད། རིགས་པས་ནི་རང་གི་བདག་ཉིད་མི་འཛིན་པའི་ཕྱིར་གཟུགས་ཀྱང་མི་འཛིན་ཏེ། བོང་བ་ལ་སོགས་པ་བཞིན་ནོ་ཞེས་བྱའོ། །

[Block 1125]
གཞན་ཡང་འདིའི་བློ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཕྱིར་ངོ་བོ་ཉིད་ཡོད་པ་མ་ཡིན་པའོ། །
--- END BLOCKS ---
