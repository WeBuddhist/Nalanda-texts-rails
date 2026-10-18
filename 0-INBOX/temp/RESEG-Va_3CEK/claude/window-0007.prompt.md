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
[Block 246]
ད་ནི་གཏོང་བ་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག །

[Block 247 [HEADING]]
#### སོ་སོར་ཐར་པའི་འདུལ་བ་གཏོང་བ། ^1-20-1-0

[Block 248 [VERSE]]
བསླབ་པ་ཕུལ་དང་ཤི་འཕོས་དང་། །
མཚན་ཉིད༌[^185]དག་ནི་བྱུང་བ་དང་། །
རྩ་བ་ཆད་དང་མཚན་འདས་ལས། །
སོ་སོར་ཐར་པའི་འདུལ་བ་གཏོང་། །

[Block 249]
འདིས་འདུལ་བར་བྱེད་པས་ན༌[^186]འདུལ་བ་སྟེ། དེས་དབང་པོ་འདུལ་བར་བྱེད་པའི་ཕྱིར་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཡིན་པར་དགོངས་པའོ། །

[Block 250]
བསྙེན་གནས་མ་གཏོགས་པའི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ནི་རྒྱུ་རྣམ་པ་བཞིས་གཏོང་བར༌[^187]འགྱུར་ཏེ། མི་བརྡ་ཕྲད་པའི་དྲུང་དུ་བསླབ་པའི་གཞི་རྣམས་བསམ་པ་ཐག་པ་ནས་སླར་ཕུལ་བ་དང་། རིས་མཐུན་པ་བཏང་བ་དང་། མཚན་ཉིད༌[^188]ཅིག་ཅར་དུ་འབྱུང་བ་དང་། དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པ་ལས་སོ། །

[Block 251]
བསྙེན་གནས་ཀྱི་སྡོམ་པ་ནི་རྒྱུ་དེ་དག་དང་། མཚན་མོ་འདས་པ་ལས་ཏེ། དེ་དག་ནི་མདོར་བསྡུ་ན་གཏོང་བའི་རྒྱུ་ལྔ་ཡིན་ནོ། །ཅིའི་ཕྱིར་རྒྱུ་དེ་དག་གིས་གཏོང་བར་གྱུར༌[^189]ཞེ་ན། ཡང་དག་པར་བླངས་པ་དང་འགལ་བའི་རྣམ་པར་རིག་བྱེད་སྐྱེད་པ༌[^190]དང་། རྟེན་བོར་བ་དང་། རྟེན་ཉམས་པ་དང་། གཞི་ཆད་པ་དང་། དེ་སྲིད་དུ་འཕངས་པའི་ཕྱིར་རོ། །

[Block 252]
ཁ་ཅིག་ལྟུང་བར་འགྱུར་བ༌[^191]ལས་སྨྲ། གཞན་དག་ན་རེ་ལྟུང་བར་འགྱུར་བ་བཞི་ལས་གང་ཡང་རུང་བ་ཞིག་གིས་དགེ་སློང་དང་དགེ་སྦྱོང་གི་སྡོམ་པ་གཏོང་ངོ་ཞེས་ཟེར་རོ། །

[Block 253]
གཞན་དག་དམ་ཆོས་ནུབ་པ་ལས། །

[Block 254]
གཞན་དག་ན་རེ་དམ་པའི་ཆོས་ནུབ་པ་ལས་ཏེ། འདི་ལྟར་དམ་པའི་ཆོས་ནུབ་ན་བསླབ་པའི་མཚམས་ཐམས་ཅད་དང་། ལས་ཀྱི་མཐའ་རྣམས་མེད་པར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 255 [VERSE]]
ཁ་ཆེ་རྣམས་ནི་བྱུང་བ་ལ། །
བུ་ལོན་ནོར་བཞིན་གཉིས་སུ་འདོད། །

[Block 256]
ཁ་ཆེ་བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་འདི་ལྟར་འདོད་དེ། རྩ་བའི་ལྟུང་བ་བྱུང་བ་ལ་ཡང་སྡོམ་པ་གཏོང་བ་མེད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། ཕྱོགས་གཅིག་ཉམས་པས་སྡོམ་པ་ཟད་པར་གཏོང་བ་ནི་མི་རིགས་སོ། །

[Block 257]
ལྟུང་བ་གཞན་བྱུང་བ་ལ་ཡང་ཚུལ་ཁྲིམས་འཆལ་པ་མེད་དོ། །

[Block 258]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། འདི་ལ་ཚུལ་ཁྲིམས་དང་འཆལ་པའི་ཚུལ་ཁྲིམས་གཉི་ག་ཡང་ཡོད་དེ། དཔེར་ན་མི་འགའ་ཞིག་ལ་ནོར་ཡང་བདོག་བུ་ལོན་ཡང་ཆགས་པ་བཞིན་ནོ། །

[Block 259]
ལྟུང་བ་དེ་བཤགས་ན་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཡིན་གྱི་ཚུལ་ཁྲིམས་འཆལ་པ་ནི་མ་ཡིན་ཏེ། དཔེར་ན་བུ་ལོན་བཙལ་ནས་ནོར་དང་ལྡན་པ་ཡིན་གྱི་བུ་ལོན་ཆགས་པ་མ་ཡིན་པ་བཞིན་ནོ་ཞེས་བྱ་བར་འདོད་དོ། །

[Block 260]
འོ་ན་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་མ་ཡིན་དགེ་སྦྱོང་མ་ཡིན། ཤཱཀྱའི་བུ་མ་ཡིན། དགེ་སྦྱོང་གི་དངོས་པོ་ལས་ཉམས་པར་འགྱུར་ཏེ། དེའི་དགེ་སྦྱོང་གི་ཚུལ་ཞིག་པར་འགྱུར། ཉམས་པ་དང་། བཅོམ་པ་དང་། ལྟུང་བ་དང་། ཕམ་པར་འགྱུར་ཞེས་གང་གསུངས་པ་ཇི་ལྟ་བུ། དེ་ནི་དོན་དམ་པའི་དགེ་སློང་ཉིད་ལས་དགོངས་ཏེ་གསུངས་པ་ཡིན་ནོ། །

[Block 261]
འདི་ནི་ཧ་ཅང་ཐུག༌[^192]ཐུབ་ཆེས་པར་འགྱུར་རོ། །

[Block 262]
འདི་ལ་ཐུག༌[^193]ཐུབ་ཅི་ཞིག་བྱ་ཞེ༌[^194]ན། བཅོམ་ལྡན་འདས་ཀྱིས༌[^195]ངེས་པའི་དོན་གང་ཡིན་པ་གཞན་དུ་འདྲེན་པའོ། །

[Block 263]
ཉོན་མོངས་པ་མང་པོ་རྣམས་ལ་འཆལ་པའི་ཚུལ་ཁྲིམས་སུ་བྱ་བའི་ཕྱིར་རྐྱེན་བྱེད་པ་ཡང་ཡིན་ནོ། །

[Block 264]
དེ་ཇི་ལྟར་ན་ངེས་པའི་དོན་ཡིན་ཞེ་ན། འདུལ་བ་ལས་འདི་སྐད་དུ་དགེ་སློང་ནི་རྣམ་པ་བཞི་སྟེ། མིང་གི་དགེ་སློང་དང་། ཁས་འཆེ་བའི་དགེ་སློང་དང་། [^196]སློང་བས་ན་དགེ་སློང་དང་། ཉོན་མོངས་པ་བཅོམ་པས་ན་དགེ་སློང་ངོ་། །དོན་འདི་ལ་ནི་གསོལ་བ་དང་བཞིའི་ལས་ཀྱིས་བསྙེན་པར་རྫོགས་པའི་དགེ་སློང་ཡིན་ནོ་ཞེས་གསུངས་ཏེ། དེ་སྔོན་དོན་དམ་པའི་དགེ་སློང་དུ་གྱུར་ལ་གང་གིས་ནི། ཕྱིས་དགེ་སློང་མ་ཡིན་པར་འགྱུར་བ་ནི་མ་ཡིན་ནོ། །

[Block 265]
ཕྱོགས་གཅིག་ཉམས་པས་ཞེས་གང་སྨྲས་པ་དེ་ནི་སྟོན་པ་དེ༌[^197]ཉིད་ཀྱིས། དཔེར་ན་ཤིང་ཏ་ལའི་མགོ་བཅད་ན་སྔོན་པོར་འགྱུར་དུ་མི་བཏུབ་འཕེལ་ཞིང་རྒྱས་པ་དང་ཡངས་པར༌[^198]མི་བཏུབ་པ་བཞིན་ནོ་ཞེས་བྱ་བ་དཔེར༌[^199]མཛད་པས་ལན་བཏབ་པ་ཡིན་ནོ། །

[Block 266]
དཔེའི་དོན་ཡང་ཇི་ལྟ་བུ་ཡིན༌[^200]ཞེ་ན། རྩ་བར་གྱུར་པ་ཕྱོགས་གཅིག་ཆད་པས་ཀྱང་སྡོམ་པ་ལྷག་མ་འཕེལ་དུ་མི་བཏུབ་ཞེས༌[^201]བྱ་བ་ཡིན་ཏེ། དེ་ཡང་དགེ་སློང་གིས༌[^202]དངོས་པོའི་མཚམས༌[^203]འཇིག་པར་བྱེད་པ་རྩ་བའི་ལྟུང་བ་ལྕི་བ་བྱུང་ན་ཁྲེལ་མེད་པ་ཤས་ཆེན་པོ་དང་ལྡན་པའི་ཕྱིར་སྡོམ་པའི་རྩ་བ་འཆད་པས་སྡོམ་པ་ཟད་པས་གཏོང་བར་རིགས་སོ། །

[Block 267]
སྟོན་པས་གང་ལ་དགེ་འདུན་གྱི་ཞལ་ཟས་དང་གཙུག་ལག་ཁང༌[^204]ལ་ཁམ་གཅིག་དང་གོམ་པ་གཅིག༌[^205]འདོར་བའི་ཕྱོགས་ལོངས་སྤྱད་པར་ཡང་མ་གནང་བ་ནི་དགེ་སློང་གི་ལོངས་སྤྱོད་ཐམས་ཅད་ལས་ཀྱང་བཀར་རོ། །

[Block 268]
གང་གི༌[^206]དབང་དུ་མཛད་ནས།

[Block 269 [VERSE]]
དགེ་སློང་མིན་ལ་དགེ་སློང་དུ། །
སྨྲ་བ་སྲེ་ད༌[^207]བསལ་བར་གྱིས། །
ཤིང་རུལ་དག་ནི་སྤང་བར་གྱིས། །
སྙིང་པོ་མེད་པ་དོར་བར་གྱིས། །

[Block 270]
ཞེས་གསུངས་པས་དེའི་དགེ་སློང་གི༌[^208]དངོས་པོ་ཅི་འདྲ་བ་ཞིག་ཡིན་ཅི་འདྲ་ཡང་རུང་དགེ་སློང་གི་དངོས་པོ་ནི་ཡོད་དེ། འདི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་བཙུན་དེ༌[^209]དགེ་སྦྱོང་བཞི་སྟེ་ལྔ་པ་མེད།

[Block 271 [VERSE]]
ལམ་གྱི༌[^210]རྒྱལ་དང་ལམ་སྟོན་དང་། །
ལམ་ཕྱིར་འཚོ་དང་ལམ་སུན་འབྱིན། །

[Block 272]
ཞེས་གསུངས་སོ། །

[Block 273]
དེ་སྐད་དུ་གསུངས་པ་ཡོད་མོད་ཀྱི། དེ་ནི་ཤ་ཚུགས་ཙམ་ལུས་པའི་ཕྱིར་དགེ་སྦྱོང་ཞེས་གསུངས་པར་ཟད་དེ། ཤིང་ཚིག་པ་དང་། མཚེའུ་སྐམས་པ་དང་། ནེ་ཙོའི་མཆུ་དང་། ས་བོན་རུལ་པ་དང་། མགལ་མེའི་འཁོར་ལོ་དང་། སེམས་ཅན་ཤི་བ་བཞིན་ནོ། །

[Block 274]
གལ་ཏེ་འཆལ་པའི་ཚུལ་ཁྲིམས་ལས་དགེ་སློང་མ་ཡིན་པར་འགྱུར་ན་བསླབ་པ་སྦྱིན་པ་པོ༌[^211]མེད་པར་འགྱུར་རོ། །

[Block 275]
ཐམས་ཅད་ལྟུང་བ་བྱུང་བའི་མདོ་ལས་ཕས་ཕམ་པ་པ༌[^212]ཡིན་ནོ་ཞེས་མི་ཟེར་གྱི། གང་ཕས་ཕམ་པ་པ༌[^213]དེ་ནི་གདོན་མི་ཟ་བར་དགེ་སྦྱོང༌[^214]མ་ཡིན་ནོ། །

[Block 276]
ལ་ལ་རྒྱུད་ཀྱི་ཁྱད་པར་ལས་ཕས་ཕམ་པ་པ༌[^215]མ་ཡིན་ཏེ། སེམས་འགས་ཀྱང་མི་འཆབ་པའི་ཕྱིར་དེ་ནི་ཆོས་ཀྱི་རྗེས་སུ༌[^216]རྣམ་པར་གཞག་གོ། །

[Block 277]
གལ་ཏེ་ཕས་ཕམ་པ་པ༌[^217]དགེ་སློང་མ་ཡིན་ན་ཅི་སྟེ་ཡང་རབ་ཏུ་མི་འབྱུང་། རྒྱུད་ཁྲེལ་མེད་པ་ཤས་ཆེན་པོས་ཉམས་པར་བྱས་པས་སྡོམ་པའི་སྐལ་བ་མེད་པའི་ཕྱིར་ཡིན་གྱི། དགེ་སློང་གི་དངོས་པོ་ལ་ལྟོས༌[^218]ཏེ་མ་ཡིན་ཏེ། འདི་ལྟར་དེ་ནི་བསླབ་པ་ཕུལ་ཡང་རབ་ཏུ་མི་འབྱུང་ངོ་། །དོན་མེད་པ་འདི་ལ་ཅི་ཞིག་འབད་དེ། གལ་ཏེ་དེ་ལྟ་བུར་གྱུར་པ་ཡང་དགེ་སློང་ཡིན་ན་དགེ་སློང་ཉིད་དེ་འདྲ་བ་དེ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 278]
དམ་པའི་ཆོས་ནུབ༌[^219]ན་འདུལ་བའི་ལས་མེད་པའི་ཕྱིར་སྔོན་མེད་པའི་འདུལ་བ་འཐོབ་པ་ནི་མེད་ཀྱི་ཐོབ་ཟིན་པ་ནི་གཏོང་བ་མེད་དོ། །

[Block 279 [HEADING]]
#### བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པ་གཏོང་བ། ^1-20-2-0

[Block 280]
ཡང་བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པ་དག་ཇི་ལྟར་གཏོང་ཞེ་ན།

[Block 281 [VERSE]]
བསམ་གཏན་གཏོགས་པའི་དགེ་བ་ནི། །
ས་འཕོས་ཉམས་པ་དག་གིས་གཏོང་། །

[Block 282]
བསམ་གཏན་དུ་གཏོགས་པའི་དགེ་བ་ཐམས་ཅད་ནི་རྒྱུ་གཉིས་ཀྱིས་གཏོང་སྟེ། གོང་མ༌[^220]འོག་ཏུ་སྐྱེ་བ་སྟེ་ས་འཕོས་པ་ལས་སམ། སྙོམས་པར་འཇུག་པ་ལས་ཡོངས་སུ་ཉམས་པ་ལས་སོ། །

[Block 283]
རིས་མཐུན་པ་བཏང་བ་ལས་ཀྱང་ཅུང་ཟད་གཏོང་བར་འགྱུར་རོ། །

[Block 284]
ཇི་ལྟར་གཟུགས་སུ་གཏོགས་པའི་དགེ་བས་འཕོ་བ་དང་། ཡོངས་སུ་ཉམས་པ་དག་གིས་གཏོང་བ་ལྟར། །

[Block 285 [VERSE]]
དེ་བཞིན༌[^221]གཟུགས་མེད་གཏོགས་འཕགས་པ། །
འབྲས་བུ་ཐོབ་སྦྱངས་ཉམས་པ་ལས། །
--- END BLOCKS ---
