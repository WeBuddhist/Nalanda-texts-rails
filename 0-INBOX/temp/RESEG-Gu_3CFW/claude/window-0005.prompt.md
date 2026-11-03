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
[Block 176]
ཕྱིར༌[^170]འོངས་ན་ཡང་རྣམ་པར་ཆད་པར༌[^171]འདི་ཞེས་བྱ་བ་དེའི་ཕྱིར་དབྱུང་བས་འགྲུབ་པར་མི་བྱའོ་སྙམ་དུ་འགའ་ཞིག་འདོད་པར་འགྱུར་བ་དེའི་དོན་དུ་མདོ་འདི་ཡིན་ནོ། །

[Block 177]
ཕྱིར་འོངས་པ་ཉིད་ལ་ཡང་བྱེད་པར་འགྱུར་བ་ཉིད་ཆད་ནའོ་ཞེས་གང་སྨོས་པ་དེ་ལ་དབྱུང་བ༌[^172]ཉིད་ཡོད་པར་འགྱུར་རོ། །

[Block 178]
བྱེད་པར་འགྱུར་བའི་མཐར་ཐུག་པ་དང་། བརྩམས་པ་ཞིག་པ་དང་། བསམ་པའི་རྒྱུན་ཆད་པ་གསུམ་ལ་དེ་གནས་སོ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་བྱའོ་སྙམ་དུ་བསམས་པ་གང་ཡིན་པ་དེ་མཐར་ཐུག་པར་འགྱུར་བ་སྟེ། དེའི་རེ་བ་ཆད་པ་དང་། བརྩམས་པ་ཞིག་པར་གྱུར་བ་དང་བསམ་པའི་རྒྱུན་ཆད་པར་གྱུར་པ་ཞེས་བྱ་བ་གསུམ་པོ་དེ་ལ་བྱེད་བཞིན་པ་ཉིད་དུ་དེ་ལ་རྣམ་པར་ཆད་པ་གནས་པའོ། །

[Block 179]
ཡིད་གཉིས་ནི་ངེས་པས་འབྱིན་པར་བྱེད་པ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་ཕྱིར་མི་འོངས་བའི༌[^173]སེམས་ཀྱི་བདག་ཉིད་ཅན་གཏན་པ༌[^174]དབྱུང་བ་སྒྲུབ་པར་བྱེད་པའི་ངེས་པར་སྨོས་པ་དེ་དང་འདྲ་བར་ཡིད་གཉིས་ནི་ཅི་ཞིག་འོང་བར་བྱ་བའམ། འོན་ཏེ་ཕྱིར་འོང་བར་མི་བྱ་སྙམ་པ་དེ་ལྟ་བུའི་སེམས་གཅིག་ཏུ་མ་ངེས་པར་མཚམས་ལས་འདའ་ཞིང་འགྲོ་བ་དང་། མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སོན་པ་ན་དེ་ལྟ་བུའི་སེམས་བསྐྱེད་པས་ཀྱང་རྣམ་པར་ཆད་པ་འགྲུབ་པར་འགྱུར༌[^175]རོ། །

[Block 180]
ཇི་ལྟར་འབྲེལ་བ་མེད་པ་ལ་རབ་ཏུ་དབྱེ་བར་གྱུར་པར༌[^176]འདི་ལ་ཆོས་གོས་བྱའོ་སྙམ་པའི་ངེས་པ་གང་ཡིན་པ་འབྲེལ་བ་མེད་པར་དབྱུང་བ་འགྲུབ་པར་བྱེད་པ་མ་གསུངས་པ་དེ་བཞིན་དུ། འདི་ལྟ་བུའི་བློ་ཅི་ཆོས་གོས་བྱ་བའམ་འོན་ཏེ་ཆོས་གོས་མི་བྱ་སྙམ་དུ་དེ་ལྟ་བུའི་སེམས་གཅིག་ཏུ་མ་ངེས་པས་མཚམས་ལས་འདའ་ཞིང་འགྲོ་བ་དང་། མཚམས་ཀྱི་ཕྱི་རོལ་དུ་སོན་པ་ན་དེ་ལྟ་བུའི་སེམས་སྐྱེས་པས་ཀྱང་ཆོས་གོས་བྱ་བའི་བསམ་པས་འབྲེལ་བ་མེད་པར་འགྲུབ་པར་འགྱུར་རོ༌[^177]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 181]
འདིར་གཞུང་ནི། མཚམས་ཀྱི་ཕྱི་རོལ་དུ་འགྲོ་བ་ན་དེ་འདི་སྙམ་དུ་ཅིའི་ཕྱིར་ཕྱིར༌[^178]འོང་བར༌[^179]བྱ་ཞིང་ཆོས་གོས་བྱ་བ་འམ།[^180] འོན་ཏེ་མི་འོང་བར་མི་བྱ་སྙམ་དུ་སེམས་པས་མཚམས་ལས་འདས་པར་བྱེད་ན། དེའི་གཏན་པ་དབྱུང་བ་འབྱུང་བ་རང་འཇུག་པ་དང་བྲལ་བ་ནི། མཚམས་ལས་འདས་པའི་མཐའ་ལས་བྱུང་བ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 182]
གལ་ཏེ་ཡང་འོང་བའི་ཕྱིར་ཡིད་གཉིས་ཀྱིས་འདི་ལ་སླར་འོང་བའི་སེམས་དང་ལྡན་པ་ཉིད་ནི་ཡིད་གཉིས་སུ་བྱེད་པའི་ཕྱིར། འབྲེལ་བ་མེད་པར་ལྡན་པ་ཉིད་དེ་དེ་བཞིན་དུ་འདིར་མཚམས་ལས་འདའ་བར་བྱེད་པ་ལ་གཏན་པ་དབྱུང་བ་འགྲུབ་པ་སྦྱོར་བ་ལས་ཏེ། གཞན་དུ་ནི་མ་ཡིན་ཏེ་དེ་ནི་སོང་ཟིན་ཏེ། ད་ནི་དབྱུང་བ༌[^181]དྲུག་པོ༌[^182]དེ་རྣམས་འདིར་བཤད་པར་བྱ་སྟེ། བྱེད་པའི་བསམ་པ་མེད་པར་ཕྱིར་མི་འོང་བའི་སེམས་ཀྱིས་མཚམས་ལས་འདའ་བར༌[^183]བྱེད་ན་འགྲོ་བའི་མཐའ་ཅན་གཏན་པ་དབྱུང་པར་བྱའོ། །

[Block 183]
ཡིད་གཉིས་ཀྱིས་བྱེད་པའི་ཕྱིར་ཕྱིར་མི་འོང་བའི༌[^184]སེམས་དང་ཐེ་ཚོམ་གྱི༌[^185]སེམས་སམ་མཚམས་ལས་འདའ་ཞིང་བྱེད་དུ་འཇུག་པའི་བསམ་པ་མེད་པར་ཕྱིར་འོང་བ་ལ་ཐེ་ཚོ༌[^186]ཟ་བའི་སེམས་ཀྱིས༌[^187]མཚམས་ཀྱི་མཐར་འདས་པ་དང་། མཚམས་ཀྱི་ཕྱིར་རོལ་དུ་སོན་པ་ན་ཕྱིར་མི་འོང་བའི་སེམས་བསྐྱེད་པའམ། ཕྱིར་འོང་བ་ལ་ཐེ་ཚོམ་ཟ་བའི་སེམས་བསྐྱེད་པ་ལ་བསམ་པས་རྗེས་སུ་འབྲེལ་བ་མི་སྐྱེད༌[^188]ཅིང་མཐར་ཐུག་པར་གྱུར་པའི་མཐའ་དང་། ངེས་པར་ཁས་བླངས་པ་མཐར་ཐུག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 184]
རྗེས་སུ་འབྲེལ་བ་ཡོད་ཅིང་ཕྱིར་མི་འོང་བའི་སེམས་སམ་ཐེ་ཚོམ་ཟ་བའི་སེམས་ཀྱིས་འདའ་བ་དང་། མཚམས་ཀྱི་ཕྱི་རོལ་དུ་འདི་དག་སྐྱེད་པ༌[^189]ལ་གལ་ཏེ་བསམ་པའི་རྒྱུན་ཆད་པས་བྱེད་པར་གྱུར་པ་ཉིད་ལས་བསམ་པ་རྒྱུན་ཆད་པ་ལ་རྣམ་པར་ཆད་པར་འགྱུར་རོ། །

[Block 185]
འོ་ན་བརྩམས་པ་ཞིག་པའི་མ་གང༌[^190]ཞེ་ན། བརྩམས་པ་ཞིག་པའི་མཐའ་ཅན་ནོ། །

[Block 186]
ཡང་ན་རྫོགས་ཤིང་ཟིན་པའི་མཐར་ཐུག་ཅེས༌[^191]བྱ་བ་རང་འཇུག་པ་དང་བྲལ་བ་སྲ་བརྐྱང་དབྱུང་བ་རྣམ་པར་དབྱེ་བར་བྱས་སོ། །

[Block 187]
ད་ནི་བཅོས་མ་བརྗོད་པར་བྱ་སྟེ། གང་ཡང་རུང་བའི་རྣམ་པར་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ངེས་པར་མ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རྣམ་པར་ངེས་པ༌[^192]བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་ལས་ལས་གཞན་པའི་བྱ་བ་རྗེས་སུ་བསྒྲུབ་པར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་སླར་རྣམ་པ་གཞན་འདི་ཟློག་པ༌[^193]སྒྲུབ་པར༌[^194]བྱེད་པ་གང་གི་ཕྱིར་གཞན་བྱེད་པ་རྣམས་ལ་གཞན་སྨོས་ཏེ། ལས་ལ་རྣམ་པ༌[^195]གཞན་གྱིས་འདི་བསྐྱེད་པ་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 188]
འདི་ལྟར་སེམས་བསྐྱེད་པ་བརྟན༌[^196]པོས་ཀྱང་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 189]
སླར་གང་ཞིག་དབྱུང་བའི་ལས་འདི་ལ་དུས་ནམ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེའི་དུས་ནི་དཔྱིད་ཟླ་ར་བའི་ཉ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ།

[Block 190]
དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 191]
དུས་མ་ཡིན་པར་གཏན་པ་དབྱུང་བར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 192]
གཏན་པ་དབྱུང་བའི་དུས་མ་ཡིན་པ་གང་ཞེ་ན་སྟོན་ཟླ་འབྲིང་པོའི་ཉ་ནས་དཔྱིད་ཟླ་ར་བའི་ཉའི་བར་དུ་གཏན་པ་དབྱུང་བར་ཆོས་གོས་གཏན་པ་གདིང་བའི་དུས་མ་ཡིན་པ་འདིའོ། །

[Block 193]
དེ་མན་ཆད་ནི་དུས་ཏེ། དུས་སུ་གཏན་པ་དབྱུང་བར་བྱ་བ་སྨོས་ན་སྲ་བརྐྱང་དབྱུང་བའི་དུས་གང་ཞེ་ན། དེའི་ཕྱིར་དཔྱིད་ཟླ་ར་བའི་ཉ་ལའོ་ཞེས་བྱ་བ་མངོན་པར་བརྟེན་པའོ། །

[Block 194]
དེའི་རྗེས་ལ་སྔ་མའི་ཚེས་བཅུ་བཞིའི་མཐའ་ཅན་དཔྱིད་ཟླ་ར་བའི་མཐའ་ཅན་ཉིད་ཀྱིས་སོ། །

[Block 195]
མོད་ལའོ་ཞེས་བྱ་བ་ནི་ལོ་གཉིས་པ་ལ་སོགས་པ་དང་འབྲེལ་བའི་དཔྱིད་ཟླ་ར་བའི་ཉ་ཐལ་བར་གྱུར་པ་བསལ་བའི་ཕྱིར་ཚིག་འདི་སྨོས་ཏེ། དབྱར་དེ་ཉིད་ཀྱིས་བར་དུ་མཆོད་པའི་མོད་ལ་སྟེ། དབྱར་གཞན་ནི༌[^197]ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 196]
འདིར་སྔགས་ནི་མིང་དེ་ལས་དུས་ཐམས་ཅད་པ་དུས་ཀྱི་གཞུང་འདིར་དགེ་འདུན་གྱིས༌[^198]གསན་པ་མཛོད་ཅིག །འདི་ལྟར་གནས་འདིར་དགེ་སློང་གི་དགེ་འདུན་གྱིས་གཏན་པ་བཏིང་བ་ལས་དེའི་རྗེས་སུ་འཇུག་པའི་དུས་ཚེས་བཅོ་ལྔ་ལགས་ཏེ། གལ་ཏེ་དགེ་འདུན་གྱི༌[^199]དུས་ལ་བབ་ཅིང་བཟོད་ན་དགེ་འདུན་གྱིས་གནང་བར༌[^200]མཛོད་ཅིག་དང་། གང་གི་ཕྱིར་དགེ་འདུན་གྱིས༌[^201]གཏན་པ་འབྱིན་པར་མཛད་དོ། །

[Block 197]
འདི་ནི་གསོལ་བའོ། །

[Block 198]
དགེ་འདུན་བཙུན་པ་རྣམས་གསན་དུ་གསོལ། ཇི་སྲིད་གནས་འདི་དགེ་སློང་གི་དགེ་འདུན་གྱིས༌[^202]གཏན་པ་བཏིང་བ་ལས་དེའི་རྗེས་སུ་འཇུག་པའི་དུས་ཚེས་བཅོ་ལྔ་ལགས་ཏེ། དེའི་སླད་དུ་དགེ་སློང་གིས་གཏན༌[^203]པ་འབྱིན་ནོ།[^204] །གཏན་པ་འབྱིན་པར་ཚེ་དང་ལྡན་པ་གང་དག་བཟོད་པ་དེ་དག་ནི༌[^205]ཅང་མ་གསུང་ཤིག༌[^206]གང་དག་མི་བཟོད་པ་དེ་དག་ནི་གསུངས་ཤིག་ཅེས་ལན་གསུམ་བཟླས་པས་དགེ་འདུན་གྱིས་བཟོད་ཅིང་གནང་ནས་དགེ་འདུན་གྱིས་གཏན་པ་ཕྱུང་ལགས་ཏེ། འདི་ལྟར་ཅང་མི་གསུང་བས་དེ་དེ་བཞིན་དུ་འཛིན་ཏོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 199]
བཅོམ་པའི་དོན་ཉིད་དུ་ནི་སྔར་ཡང་ངོ་ཞེས་བྱ་བ་ན། དེ་དུས་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཉི་མ་དེ་ཉིད་ལ་ཞེས་བྱ་བའི་ཚིག་གིས་གསོ་སྦྱོང་གི་ཉི་མའི་བདག་ཉིད་ཅན་ནི་སྔར་གྱི་དུས་ཀྱི་དེ་ཡིན་ཏེ། སྔར་ནི་སྔོན་དུ་བྱ་བའོ། །

[Block 200]
དེར་ཉམས་སུ་མ་མྱོང་བ་དང་ལྡན་པ་ལ་ནི་མ་ཐོས་ཀྱི་བར་དུ་ཕན་ཡོན་རྗེས་སུ་འཇུག་གོ་ཞེས་བྱ་བ་ལ་མ་ཐོས་ཀྱི་བར་དུ་ཞེས་བྱ་བ་ནི་མཚམས་ཀྱི༌[^207]ནང་ངམ་ཕྱི་རོལ་དུ་འདུག་པས་སོ། །

[Block 201]
དེ་ནི་འདིར་གཏན་པ་དབྱུང་བ་ཐོས་པའི་མཐའ་ལས་བྱུང་བ་སྔར་གྱི་དུས་སོ། །

[Block 202]
གཙུག་ལག་ལས།

[Block 203]
གང་གིས་དེ་ཉམས་སུ་མྱོང་བར་མ་གྱུར་པ་དེ་སྲིད་དུ་འདི་མ་ཐོས་ཀྱི་བར་དུ་འཇུག་གི༌[^208]ཐོས་ན་ནི་ལྡོག་གོ། །

[Block 204]
ཅི་གནས་སྐབས་ཐམས་ཅད་དུ་མ་ཐོས་ཀྱི་བར་དུ་ཕན་ཡོན་དེ་རྗེས་སུ་འཇུག་གམ་ཞེ་ན། དེའི་ཕྱིར་རྗེས་སུ་འབྲེལ་བ་མེད་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 205]
གཞན་དུ་ཇི་སྲིད་ཕན་ཡོན་རྗེས་སུ་འཇུག་ཅེ་ན། དེའི་ཕྱིར་ཡོད་ན་མ༌[^209]ཆད་ཀྱི་བར་དུ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྗེས་སུ་འབྲེལ་བ་ཡོད་པ་ཉིད་མ་ཆད་ཀྱི་བར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 206]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་གཏན་པ་དབྱུང་བ་ཐོས་པའི་མཐའ་ལས་བྱུང་བ་གང་ཞེ་ན། གང་ཞིག་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་ཤན་མེད་པའི་རྒྱུད་ཀྱི་ཐོས་པ་དང་། གོས་ལ་རེ་བ་ཆད་པ་དང་། ཤན་ཡོད་པས་གོས་ཟིན་པར་གྱུར་པ་དང་། གལ་ཏེ་གོས་ལ་རེ་བ་ཡོད་པ་དང་། གོས་ཀྱང་རུང་སྟེ་བརྩམས་པ་ནི་ཤན་གྱི་རྒྱུན་ཡོངས་སུ་ཡང༌[^210]དག་པས༌[^211]བརྗོད་པར་བྱ་བ༌[^212]སྟེ། དེ་བཞིན་དུ་དེ་འཇུག་གོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 207]
དངོས་པོ་བསྡུས་བ༌[^213]ནི་བརྡ་བཤད་ཀྱིས་ཆོག་སྟེ་ཞེས་བྱ་བ་དེའི་རྙེད་པ་འབྱུང་བ་མཐོང་བ་ཡོད་ཀྱང་རྙེད་པ་བརྩམས་པ༌[^214]ཉིད་ལ་ཡང་གོས་གནང་བཞིན་པ་ཉིད་ལ་འདི་ནི་མཐར་ཐུག་པའོ། །

[Block 208]
དེ་གཉིས་ནི་མཐར་ཐུག་པའི་མཐའ་ལས་བྱུང་བ་དང་། རེ་བ༌[^215]ཆད་པའི་མཐའ་ལས་བྱུང་བ་འདིས་རྣམ་པ་གཞན་གཉིས་ཡིན་ནོ། །

[Block 209]
ཞིག་པར་འགྱུར་བ༌[^216]མཐའ་ལས་བྱུང་བའི་རྣམ་པ་གཞན་ཡང་འདིར་འབྱུང་བར་རིག་པར་བྱའོ། །

[Block 210]
མ་བྱུང་ན་ཐམས་ཅད་ཀྱིས་དེའི་དུས་ཀྱི་རྙེད་པ་བགོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་གཏན་པའི་ཆོས་གོས་དེ་མ་བྱུང༌[^217]ན་སྟེ། དངོས་པོ༌[^218]ཞུགས་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 211]
ཆོས་གོས་དེ་ནི་གཞན་དག་གི་ལ་གཏེར་གྱི་གནས་ལྟ་བུ་ཡིན་པས། གང་གི་ཚེ་འདིང་བར༌[^219]བྱེད་པ་ཐམས་ཅད་ཀྱིས༌[^220]དེ་ཕྱུང་བར་འགྱུར་བ༌[^221]དེའི་ཚེ་ན་གཏན་པ་བཏིང་བའི་དུས་ལས་བྱུང་བའི་རྙེད་པར་བགོ་བར་བྱའི། དེ་མ་ཕྱུང་བའི་སྔོན་རོལ་དུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིར་སྟོན་ཏོ། །

[Block 212]
གཞིར་གཏོགས་པའི་སྲ་བརྐྱང་གི་གཞིའོ། །

[Block 213]
སྟོན་ཟླ་འབྲིང་པོའི་ཞེས་སྨོས་པས་སྟོན་ཟླ་འབྲིང་པོའི་ཚེས་བཅུ་དྲུག་ལ་གཏན་པ་བཏིང་བའི་དུས་ཡིན་ན་ཤོལ་གྱི་ཟླ་བ་ནི༌[^222]རྒྱལ་པོའི་རྗེས་སུ་འབྲང་བར་བྱའོ་ཞེས་སྨོས་པས་དེའི་རྗེས་སུ་འབྲང་བ་ལ་མངོན་པར་བརྟེན་པར་ཐལ་བའི་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དགག་དབྱེ་བ༌[^223]ཇི་ལྟ་བ་བཞིན་དུ་གདིང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་དགག་དབྱེའི་སྒྲས་ནི་དུས་ཉེ་བར་མཚོན་པར་བྱེད་པར་རིག་པར་བྱའོ། །

[Block 214]
ཇི་ལྟར་དགག་དབྱེའི་དུས་སུ་ཞེས་བྱ་བའོ། །

[Block 215]
དེ་ལྟ་བས་ན་རྩོད་པར་བྱེད་པའི་དབང་གིས་སྔོན་དུ་དགག་དབྱེ་བྱེད་པ་ལ་དེའི་འོག་ཏུ་གཏན་པ་བཏིང་བ་འདིས་བྱ་བ་ཉིད་དུ་སྟོན་པའོ། །
--- END BLOCKS ---
