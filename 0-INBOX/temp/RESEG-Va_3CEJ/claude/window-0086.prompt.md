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
[Block 3011]
གནས་སྐབས་གང་ཞིག་སྐྱེ་ཞེ་ན། སྐྱེ་བ་ལ་མངོན་དུ་ཕྱོགས་པའི་མ་འོངས་པ་སྟེ། གནས་སྐབས་དེ་ཁོ་ན་རྐྱེན་དང་ཕྲད་ནས་ཞེས་བྱའོ། །

[Block 3012]
སྒྲ་པའི་འདི་ལྟ་སྟེ། བྱེད་པ་པོ་དང་བྱ་བ་རྣམ་པར་འཇོག་པ་འདི་ཡང་གྲུབ་པ་མ་ཡིན་ཏེ། སྐྱེའོ༌[^1710]ཞེས་བྱ་བ་འདི་ནི་བྱེད་པ་པོ་ཡིན་ལ། སྐྱེ་ཞེས་བྱ་བ་འདི་ནི་བྱ་བ་ཡིན་ན་འདི་ལ༌[^1711]སྐྱེའོ་ཞེས་བྱ་བའི་དོན་ལས་བྱ་བ་གཞན་ཡང་མ་མཐོང་ངོ་། །དེ་ལྟ་བས་ན་ཐ་སྙད་དག་ལ་ཀླན་ཀ་མེད་དོ། །

[Block 3013]
ཚིག་གི་དོན་ནི་འདི་ཡོད་ན་འདི་འབྱུང་། འདི་སྐྱེས་པས་འདི་སྐྱེ་ཞེས་བྱ་བའི་དོན་གང་ཡིན་པ་དེ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དོན་ཏོ་ཞེས་བྱ་བ་འདི་ཡིན་ནོ། །

[Block 3014]
འདིར་བཤད་པ།

[Block 3015 [VERSE]]
ཇི་ལྟར་མེད་པ་སྐྱེ་བ་ལྟར། །
མེད་པ་ཕྲད་པའང་དེ་དང་འདྲ། །
སྐྱེས་པ་སྐྱེ་ན་མཐར༌[^1712]ཐུག་མེད། །
འོན་ཏེ་སྔ་ན་ཡོད་ནའང་རུང་། །

[Block 3016 [VERSE]]
ལྷན་ཅིག་པ་ལ་འང་དེ་ཡོད་དེ། །
མར་མེ་བྱུང་ནས་མུན་པ་མེད། །
ཁ་གདངས་ཉལ་བཞིན་གལ་ཏེ་ཕྱིས། །
བཙུམས་པ་ལ་ཡང་ཅི་ཕྱིར་མིན། །

[Block 3017]
གཞན་དག་ནི་ཀླན་ཀ་འདི་ཡོངས་སུ་སྤང་བར་བྱ་བའི་ཕྱིར་དོན་གཞན་དུ་ཡོངས་སུ་རྟོག་པར་བྱེད་དོ། །

[Block 3018]
རྟེན་ཅིང་འབྲེལ་པ་ནི་ཟློས་པའི་དོན་ཡིན་ནོ། །

[Block 3019]
སམ་ནི་འདུ་བའི་དོན་ཡིན་ནོ། །

[Block 3020]
ཨཱི་ཏྱ་ནི་འགྲོ་བར་རུང་བ་སྟེ་མི་སྡོད་པའོ། །

[Block 3021]
ཨུད་གོང་ན་ཡོད་པའི་པ་ད་ནི་འབྱུང་བའི་དོན་ཏེ། འདི་སྐད་དུ་ཚོགས་པ་དེ་དང་དེ་ན་འགྲོ་བར་རུང་བ་རྣམས་འདུས་ནས་སྐྱེ་བ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའོ་ཞེས་བཤད་པ་ཡིན་ནོ། །

[Block 3022]
རྟོགས་པ༌[^1713]འདི་ནི་འདི་ཁོ་ན་ལ་རབ་ཏུ་བརྟག་ཏུ་རུང་གི་མིག་དང་གཟུགས་རྣམས་ལ་བརྟེན་ནས་མིག་གི་རྣམ་པར་ཤེས་པ་སྐྱེའོ་ཞེས་བྱ་བ་འདི་ལ་ཇི་ལྟར་རུང་།

[Block 3023 [HEADING]]
##### འདི་ཡོད་ན་འདི་འབྱུང་ཞེས་རྣམ་གྲངས་གཉིས་གསུངས་པ། ^3-1-11-8-0

[Block 3024]
ཡང་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་ཡོད་ན་འདི་འབྱུང་། འདི་སྐྱེ་བས་འདི་སྐྱེའོ་ཞེས་རྣམ་གྲངས་གཉིས་གསུངས་ཤེ་ན། ངེས་པར་གཟུང་བའི་དོན་ཏེ། དཔེར་ན་གཞན་ལས་མ་རིག་པ་ཡོད་ན་འདུ་བྱེད་རྣམས་འབྱུང་གི །མ་རིག་པའི་རྐྱེན་མེད་པར་འདུ་བྱེད་རྣམས་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ལྟ་བུའོ། །

[Block 3025]
ཡང་ན་ཡན་ལག་འདི་ཡོད་ན་འདི་འབྱུང་ངོ་། །ཡན་ལག་འདི་སྐྱེས་པས་ཡན་ལག་གཞན༌[^1714]སྐྱེའོ་ཞེས་ཡན་ལག་བརྒྱད་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3026]
ཡང་ན་སྔོན་གྱི་མཐའ་ཡོད་ན་ད་ལྟར་གྱི་མཐའ་འབྱུང་ངོ་། །ད་ལྟར་གྱི་མཐའ་སྐྱེས་པས་ཕྱི་མའི་མཐའ་སྐྱེའོ་ཞེས་ཚེ་བརྒྱུད་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3027]
ཡང་ན་རེས་འགའ་ནི་འདུ་བྱེད་རྣམས་མ་རིག་པའི་མཇུག་ཐོགས་སུ་འབྱུང་ངོ་། །རེས་འགའ་ནི་བརྒྱུད༌[^1715]ནས་སོ་ཞེས་མངོན་སུམ་དང་བརྒྱུད་ནས་རྐྱེན་གྱི་ངོ་བོར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3028]
གཞན་དག་ན་རེ་རྒྱུ་མེད་ན་དངོས་པོ་མི་འབྱུང་ལ། རང་བཞིན་དང་སྐྱེས་བུ་ལ་སོགས་པ་སྐྱེ་བ་མེད་པ་དང་ལྡན་པ་རྟག་པ་ལས་ཀྱང་ཅུང་ཟད་ཀྱང་མི་སྐྱེའོ་ཞེས་རྒྱུ་མེད་པ་དང་། རྒྱུ་རྟག་པར་སྨྲ་བ་དགག་པའི་ཕྱིར་རོ་ཞེས་ཟེར་ཏེ། རྟོག་པ་འདི་ལ་ནི་ཚིག་སྔ་མ་སྨོས་པ་དོན་མེད་པར་འགྱུར་ཏེ། འདི་སྐྱེས་པས་འདི་སྐྱེའོ་ཞེས་བྱ་བ་འདི་ཁོ་ནས་སྨྲས་པ༌[^1716]གཉི་ག་དགག་པ་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 3029]
འོ་ན་ནི་གང་ལགས༌[^1717]བདག་རྟེན་དུ་གྱུར་པ་ཡོད་པས་འདུ་བྱེད་ལ་སོགས་པ་རྣམས་འབྱུང་ངོ་། །མ་རིག་པ་ལ་སོགས་པ་སྐྱེས་པས་དེ་དག་སྐྱེ་བར་རྟོག་པར་བྱེད་པ་ཡོད་པས་དེའི་ཕྱིར་རྟོག་པ་དེ་བསལ་བར༌[^1718]བྱས་པའི༌[^1719]ཕྱིར་གང་ཞིག་སྐྱེས་པས་གང་སྐྱེ་བ་ནི་དེ་ཉིད་ཡོད་པས་དེ་འབྱུང་གི །གཞན་ལས་ནི་མ་ཡིན་ནོ་ཞེས་འདི༌[^1720]ངེས་པར་གཟུང་བ་མཛད་པ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད་རྣམས་དང་། སྡུག་བསྔལ་གྱི་ཕུང་པོ་ཆེན་པོ་འདི་འབའ་ཞིག་ཡང་དག་པར་འབྱུང་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་བར་ཡིན་ནོ། །

[Block 3030]
སློབ་དཔོན་དག་ན་རེ། མ་རིག་པ་མ་སྤངས་ན་འདུ་བྱེད་རྣམས་མི་སྤོང༌[^1721]ལ་དེ་ཉིད་སྐྱེས་པས༌[^1722]སྐྱེ་བར་འགྱུར་རོ་ཞེས་མ་སྤངས་པ་དང་སྐྱེ་བར་འགྱུར་བ་རྒྱས་པར་བསྟན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 3031]
གཞན་དག་ན་རེ་རྒྱུའི་རྒྱུན་ཇི་སྲིད་པ་དེ་སྲིད་དུ་འབྲས་བུའི་རྒྱུན་འབྱུང་བར་འགྱུར་རོ། །

[Block 3032]
རྒྱུ་ཉིད་སྐྱེས་པས་འབྲས་བུ་སྐྱེ་བར་འགྱུར་རོ་ཞེས་གནས་པ་དང་སྐྱེ་བ་ཡང་དག་པར་བསྟན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་ཏེ། འབྱུང་བའི་དབང་དུ་མཛད་པ་ཡིན་ན་གནས་པའི་ཚིག་ཏུ་ཐལ་བ་ཅི་ཞིག་ཡོད། བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ཅིའི་ཕྱིར་རིམ་པ་མི་མཐུན་པར་སྔར་ནི་གནས་པ་དང་ཕྱིས་ནི་སྐྱེ་བ་གསུངས་པར་འགྱུར། ཡང་སྨྲས་པ། འདི་ཡོད་ན་འདི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི་འབྲས་བུ་ཡོད་ན་རྒྱུ་འཇིག་པར༌[^1723]འབྱུང་བ་ཡིན་ནོ། །

[Block 3033]
འོ་ན་ནི་རྒྱུ་མེད་པ་ལས་འབྲས་བུ་འབྱུང་ངོ་སྙམ་དུ་སེམས་པར་འགྱུར་བས་སྨྲས་པ། དེའི་ཕྱིར་རྒྱུ་མེད་པ་ལས་འབྱུང་བ༌[^1724]མ་ཡིན་ཏེ། འདི་ལྟར་ན༌[^1725]འདི་སྐྱེས་པས་འདི་སྐྱེའོ་ཞེས་བཀའ་སྩལ་ཏོ། །

[Block 3034]
གལ་ཏེ་མདོའི་དོན་དེ་ཡིན་པར་གྱུར་ན་ནི་འདི་ཡོད་པས་འདི་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ཁོ་ནར་བཀའ་སྩལ་པར་འགྱུར་ལ། རེ་ཞིག་སྔར་ནི་འབྲས་བུ་སྐྱེ་བ་ཁོ་ན་ཡིན་ལ། ཕྱིས་ནི་འདི་ཡོད་ན་འདི་མི་འབྱུང་བར་འགྱུར་རོ་ཞེས་བཀའ་སྩལ་པར་འགྱུར་ཏེ། དེ་ལྟར༌[^1726]ན་གོ་རིམས་ལེགས་པ་ཡིན་ནོ། །

[Block 3035]
གཞན་དུ་ན་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་གང་ཞེ་ན་ཞེས་བྱ་བའི་སྐབས་སུ་འཇིག་པ་ཞེས་བྱ་བའི་རིག་པ༌[^1727]གང་ཞིག་ཡིན། དེ་ལྟ་བས་ན་དེ་ནི་མདོའི་དོན་མ་ཡིན་ནོ། །

[Block 3036 [HEADING]]
##### མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད་ལ་སོགས་པའི་འབྲེལ་པ། ^3-1-11-9-0

[Block 3037]
ཡང་ཇི་ལྟར་ན་མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད་རྣམས་ཡིན་པ་ནས་སྐྱེ་བའི་རྐྱེན་གྱིས་རྒ་ཤིའི་བར་དག་ཡིན་ཞེ་ན། འབྲེལ་པ་ཙམ་ཞིག་བསྟན་པར་བྱ་སྟེ། བྱིས་པ་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་འདུ་བྱེད་ཙམ་འདི་མི་ཤེས་པས་བདག་ཏུ་ལྟ་བ་དང་། ངའོ་སྙམ་པའི་ང་རྒྱལ་ལ་མངོན་པར་ཞེན་ཅིང་བདག་ཉིད་བདེ་བའི་དོན་ཏམ། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་ཡང་མ་ཡིན་པའི་དོན་དུ་ལུས་ལ་སོགས་པ་དག་གིས་ལས་རྣམ་པ་གསུམ་རྩོམ་སྟེ། ཚེ་ཕྱི་མ་ལ་བདེ་བའི་དོན་དུ༌[^1728]བསོད་ནམས་བདེ་བ་དང་། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ་ཡང་མ་ཡིན་པའི་དོན་དུ་ནི་མི་གཡོ་བ། ཚེ་འདི་ལ་བདེ་བའི་དོན་དུ༌[^1729]བསོད་ནམས་མ་ཡིན་པ་རྩོམ་སྟེ། དེ་དག་ནི་འདིའི་མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད་དག་ཡིན་ནོ། །

[Block 3038]
ལས་ཀྱི་འཕེན་པའི་དབང་གིས་རྣམ་པར་ཤེས་པའི་རྒྱུན་སྲིད་པ་བར་མ་དང་འབྲེལ་པའི་ཕྱིར་མེ་འབར་བ་འགྲོ་བའི་ཚུལ་དུ་འགྲོ་བ་དེ་དང་དེར་འགྲོ་བར་འགྱུར་ཏེ། དེ་ནི་འདིའི་འདུ་བྱེད་ཀྱི་རྐྱེན་གྱིས་རྣམ་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 3039]
དེ་ལྟར་བཤད་ན་རྣམ་པར་ཤེས་པའི་ཡན་ལག་བསྟན་པ་ལས།

[Block 3040]
རྣམ་པར་ཤེས་པ་གང་ཞེ་ན། རྣམ་པར་ཤེས་པའི༌[^1730]ཚོགས་དྲུག་གོ་ཞེས་བཤད་པ་དེ་འཐད་པ་ཡིན་ནོ། །

[Block 3041]
ཡང་རྣམ་པར་ཤེས་པ་སྔོན་དུ་འགྲོ་བའི་མིང་དང་གཟུགས་ཕུང་པོ་ལྔ་པོ་འགྲོ་བ་དེ་དང་དེར་སྐྱེ་བར་འགྱུར་ཏེ། རྣམ་པར་འབྱེད་པ་ལས་དེ་སྐད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3042]
དེའི་འོག་ཏུ་མིང་དང་གཟུགས་ཡོངས་སུ་སྨིན་པའི་རིམ་གྱིས་སྐྱེ་མཆེད་དྲུག་གོ། །

[Block 3043]
དེའི་འོག་ཏུ་ཡུལ་དང་ཕྲད་ན་རྣམ་པར་ཤེས་པ་སྐྱེ་བས་གསུམ་འདུས་པ་ལས་བདེ་བ་ལ་སོགས་པ་མྱོང་བར་འགྱུར་བའི་རེག་པའོ། །

[Block 3044]
དེའི་འོག་ཏུ་ཚོར་བ་རྣམ་པ་གསུམ་མོ། །

[Block 3045]
དེའི་འོག་ཏུ་སྲེད་པ་སྟེ། སྡུག་བསྔལ་གྱིས་གཟིར་བའི་ཚོར་བ་བདེ་བ་ལ་ནི་འདོད་པའི་སྲེད་པའོ། །

[Block 3046]
བདེ་བ་དང་། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་ཡང་མ་ཡིན་པ་ལ་ནི་གཟུགས་ཀྱི་སྲེད་པའོ། །

[Block 3047]
བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་ཡང་མ་ཡིན་པ་ལ་ནི་གཟུགས་མེད་པའི་སྲེད་པའོ། །

[Block 3048]
དེའི་འོག་ཏུ་ཚོར་བ་ཡིད་དུ་འོང་བ་ལ་སྲེད་པ་ལས་འདོད་པ་ལ་སོགས་པ་ཉེ་བར་ལེན་ཏེ། དེ་ལ་འདོད་པ་རྣམས་ནི་འདོད་པའི་ཡོན་ཏན་ལྔ་དག་གོ། །

[Block 3049]
ལྟ་བ་དག་ནི་དྲུག་ཅུ་རྩ་གཉིས་ཏེ། ཚངས་པའི་དྲ་བ་ལས་ཇི་སྐད་འབྱུང་བ་བཞིན་ནོ། །

[Block 3050]
ཚུལ་ཁྲིམས་ནི་འཆལ་པའི་ཚུལ་ཁྲིམས་སྤོང་བའོ། །
--- END BLOCKS ---
