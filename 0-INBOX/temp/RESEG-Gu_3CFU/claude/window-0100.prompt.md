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
[Block 3501]
ཞེ་སྡང་བས་མ་གཏོགས་ཞེས་བྱ་བ་འདི་དང་འོག་ཏུ་བརྗོད་པ་དེའི་ཡན་ལག་ཉིད་ནི་མ་ཡིན་ཏེ། སྐུར་བ་འདེབས་པ་ལ་འདིར་སྐྱོན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3502]
བརྗོད་པ་ཡོད་པར་གྱུར་ཅིག་ཅེས་བྱ་བ་ཡང་ཀུན་ནས་རྒོལ་བའམ་རྣམ་པ་གཞན་གྱིས་སྐུར་བ་འདེབས་པ་དང་། སྐུར་བ་འདེབས་པ་ཉིད་ཀྱིས་ཅི་སྟེ་འཇུག་པའི་རྒྱུ་རྗེས་སུ་འགྲོ་བ་ཙམ་འདི་དཔེ་ཉིད་ཀྱིས༌[^2413]ཕལ་ཆེ་བ་ཉིད་ལ་བརྟེན་ནས་ཕལ་ཆེར་སྐུར་བ་འདེབས་པ་འཇུག་པ་ལ་ཞེ་སྡང་གི་རྒྱུ་སྐྱེས་པའི་དབང་གིས་འདིར་གསུངས་པ་ཡིན་གྱི་ཡན་ལག་ཉིད་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 3503]
གཞི་མེད་པའི་དགེ་འདུན་ལྷག་མའོ།། །།

[Block 3504]
ད༌[^2414]ནི་གཞན་གྱི་ཆ་དང་མཐུན་པའི་དགེ་འདུན་ལྷག་མ་ལ་འདི་ཉིད་ཆོ་ག་མ་ལུས་པ་ཁས་བླངས་ནས་བརྫུན་དུ་སྨྲ་བས་སོ་ཞེས་སྨོས་པའི་གནས་སུ་འདི་འཐོབ་པས་དེའི་བྱེ་བྲག་འགའ་ཞིག་འདིར་བརྗོད་པར་བྱ་སྟེ། བརྗོད་པར་བྱ་བ་གཞན་ལ་གནས་པའི་ཚིག་གིས་བརྫུན་ནའོ་ཞེས་བྱ་བ་འདི་ཕམ་པར་འགྱུར་བའི་ལས་འདིས་ལྷག་པར་སྤྱོད་པ་ཞེས་བྱ་བ་བརྗོད་པར་བྱ་བ་འདིས༌[^2415]ལས་གཞན་དུ་དེའི་ཡན་ལག་ཏུ་གྱུར་པའི་རྣམ་པར་བྲལ་བ་བརྗོད་པར་བྱ་བ་ལ་གནས་པ་གང་ལ་ཡོད་པ་དེ་ནི་བརྗོད་པར་བྱ་བ་གཞན་ལ་གནས་པའི་ཚིག་གོ། །

[Block 3505]
འདི་ལྟ་སྟེ་དཔེར་ན་ཁོ་བོ་ཅག་གིས་ཚེ་དང་ལྡན་པ་གྱད་བུ་ནོར་མཐོང་ངོ་། །དགེ་སློང་མ་ཨུཏྤ་ལའི་མདོག་ཅན་མཐོང་ངོ་། །མི་ཚངས་པར་སྤྱོད་པ་འཁྲིག་པའི་ཆོས་བསྟེན་པ༌[^2416]མཐོང་ངོ་ཞེས་གང་གི་ཕྱིར་སྒྲ་དེ་གསུམ་གཅིག་ལ་གཅིག་སྦྱར་བ་དེ་བཞིན་དུ་འདི་རྣམས་ཀྱིས་བརྗོད་པར་བྱ་བའི་དོན་རྣམ་པར་བྲལ་བ་དེའི་ཆར་གྱུར་པའི་ཕམ་པའི་ལས་འདིས་ལྷག་པར་སྤྱོད་པ་དེ་བས་ན་དེ་ལྟར་དེའི་ཆ་དང་རྣམ་པར་བྲལ་བ་སོ་སོར་གྱུར་པ་འདིས༌[^2417]ཞེས་བྱ་བ་བྱས་ནས་སོ། །

[Block 3506]
འདིར་ཡང་འདི་ཉིད་ཀྱི་ཚིག་ལ་གནས་པ་སྟེ། དེས་ན་བརྗོད་པར་བྱ་བ་གཞན་ལ་གནས་པའི་ཚིག་གིས་ཕམ་པ༌[^2418]ལྷག་པར་སྤྱོད་པའི་དགེ་སློང་སུ་ཞིག་ལ་གོ་བར་བྱེད་པ་ལ་དགེ་འདུན་ལྷག་མ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3507]
ཡང་དག་པར་ཤེས་ནས་ཀྱང་སྐུལ་བར་བྱེད་པ་དང་འབྲེལ་བ་ཕམ་པ་ལྷག་པར་སྤྱོད་པར་གྱུར་པ་ཡིན་ཏེ་བརྗོད་པར་བྱ་བ་གཞན་ལ་གནས་པའི་ཚིག་གིས་དེ་སྟོན་པ་སྟེ། དེ་བསལ་བའི་ཕྱིར་བརྫུན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འོག་མ་སྒྲོགས་པར་འདོད་པའི་འདུན་པས་འདྲ་བའི་དོན་བརྗོད་པ་ལ་སྦོམ་པོའོ་ཞེས་བྱ་བ་རྣམ་པ་འདིས་སྦོམ་པོ་ཐོབ་པ་ལ་ཐ་སྙད་འདི་བཏགས་པའོ། །

[Block 3508]
གཞན་གྱི་ཆ་དང་མཐུན་པའི་དགེ་འདུན་ལྷག་མའོ།། །།

[Block 3509]
མི་བསྟེན་པས་སྐུར་པ་འདེབས་ན་སྦོམ་པོའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་ལ་ཕོའི་དབང་པོ་མེད་པ་ནི་དཔེར་ན་མ་ནིང་ཕོས༌[^2419]ལྟ་བུའོ། །

[Block 3510]
དགེ་སློང་ལ་མོའི་དབང་པོ་མེད་པ་ནི་དཔེར་ན་མ་ནིང་མོས་སྐུར་པ་འདེབས་ན་ཡང་སྦོམ་པོའི༌[^2420]ཁ་ན་མ་ཐོ་བའོ། །

[Block 3511]
དེ་ཡང་འདིའི༌[^2421]དབང་དུ་མ་བྱས་ཤིང་ཁ་དང་བཤང་བའི་ལམ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3512]
མིང་མ་སྨོས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཉམས་པར་བྱ་བའི་མིང་མ་སྨོས་པར་སྐུར་པ་འདེབས་ན་ཡང་སྦོམ་པོའོ། །

[Block 3513]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས།

[Block 3514]
དགེ་འདུན་གྱི་དབུས་སུ་ངེས་པ་མེད་པར་འདི་སྐད་ཅེས་མི་ཚངས་པར་སྤྱོད་པ་བྱས་སོ། །

[Block 3515]
མ་ཤ་ཀ་ལྔ་ལས་ལྷག་པ༌[^2422]བརྐུས་སོ། །

[Block 3516]
མི་སྲོག་དང་ཕྲལ༌[^2423]ལོ། །

[Block 3517]
མི་ཆོས་བླ་མ་ཡང་དག་པ་མ་ཡིན་པ་སྨྲས་སོ་ཞེས་ཟེར་ཞིང་། བདག་ནི་ཆེ་གེ་མོས་སོ་ཞེས་མི་ཟེར་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3518]
དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས་ཁྲག་ཕྱུང་བ་དང་དགེ་འདུན་གྱི་དབྱེན་བྱས་པའོ་ཞེས་བྱ་བ་ནི་མཚམས་མེད་པ་འདི་གཉིས་ནི་སྦོམ་པོའོ། །

[Block 3519]
མི་གསོད་པ་དང་དགེ་འདུན་གྱི་དབྱེན་གྱི་ལྷག་མ་དབྱེ་བར་བརྟུལ་བ་ནི་སྤོང་བའི་ཕྱོགས་ལ།[^2424] འདི་དག་ལ་གོ་རིམས༌[^2425]ཇི་བཞིན་དུ་སྦོམ་པོའི་ལྟུང་བ་ཡིན་གྱི་སྐུར་པ་འདེབས་པའི་ཕྱོགས་པ་ནི་མ་ཡིན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3520]
དེ་གཉིས་ཀྱིས་སྐུར་པ་འདེབས་ན་ཉེས་བྱས་སུ༌[^2426]རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3521]
བསམས་ཏེ་སྨྲས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པས་གཞོགས་སྨོས་བྱེད་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་འདིར་སོགས་པ་ཞེས་བྱ་བའི་སྒྲ་ནི་རྣམ་པ་གཞན་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3522]
བསམས་ཏེ་སྨྲས་སོ་ཞེས་བྱ་བ་ནི་འདི་ལྟ་བུའི་རྣམ་པ་མཚོན་པར་བྱེད་པ་ལ་ཉེས་བྱས་སོ། །

[Block 3523]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་གི་གཞུང་ལས་དགེ་སློང་སྟན་ལས་ལངས་ཏེ་བདག་གིས་བསམས་ཏེ་སྨྲས་སོ་ཞེས་ཟེར་ཞིང་སྐྱེ་བོ་ཐམས་ཅད་ལ་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 3524]
བག་ཙམ་ལ་ཡང་རྣམ་པ་དེ་དག་ཤེས་པར་བྱས་ཏེ།[^2427] བདག་གིས་དགེ་སློང་མ་ཆེ་གེ་མོ་ཞེས་བྱ་བ་མ་ནིང་ཕོ་དང་མི་ཚངས་པར་སྤྱོད་པ་འཁྲིག་པའི་ཆོས་བསྟེན་པ་མཐོང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 3525]
གཞི་མེད་པའི་དང་བག་ཙམ་གྱི་ཞུ་བའོ།། །།

[Block 3526]
གཞན་གྱི་འཁོར་ཁ་འདྲེན་ན་སྦོམ་པོའོ་ཞེས་བྱ་བ་ནི་ཕྲན་ཚེགས་རྣམས་ལས་འདི་འབྱུང་ངོ་། །དགེ་འདུན་གྱི་དབྱེན་ལ་སོགས་པའི་དགེ་འདུན་ལྷག་མ་བསྒོ་བ་ལས་བྱུང་བ་བཞི་པོ་རྣམས་ཀྱི་ཐུན་མོང་གི་རྣམ་པ་བརྗོད་པར་བྱ་སྟེ། བཟློག་པའི་ཚུལ་གྱིས་མི་གཏོང་བར་རྗེས་སུ་བསྒྲུབ་པའི་རང་བཞིན་ནི་རྗེས་སུ་མཐུན་ནོ་ཞེས་བྱ་བ་ནི་འཆད་པར་འགྱུར་བ་དག་ལས་དགེ་འདུན་གྱི་དབྱེན་བྱེད་པ་ལ་འཇུག་པས་ཞེས་བྱ་བ་འདི་ལྟ་བུ་ལ་སོགས་པ་མི་གཏོང་བའི་བདག་ཉིད་ཅན་རྗེས་སུ་བསྒྲུབ་པ་ལ་གང་ཞིག་གི་ངོ་བོ་ལུས་ངག་གིས་གོ་བར་གྱུར་པ་ལའང་ཅང་མི་སྨྲ་བའི་ངོ་བོས་རྗེས་སུ་མཐུན་པར་གྱུར་པའམ། གཉིས་ཀའི་བདག་ཉིད་ཅན་བཟློག་པའི་ཚུལ་གྱིས་དེ་རྗེས་སུ་འགྲོ་བའོ། །

[Block 3527]
གང་གི་ཕྱིར་བཟློག་པ་དང་འབྲེལ་བའི་སོ་སོར་ཉེ་བར་གནས་པ་ཞེས་བྱ་བ་འདི་ལ་མི་གཏོང་བར་རྗེས་སུ་བསྒྲུབ་པའི་རང་བཞིན་ནོ། །

[Block 3528]
དེ་བས་ན་བཟློག་པའི་ངོ་བོས་རྗེས་སུ་འགྲོ་བར་རིགས་པ་ཡིན་ནོ། །

[Block 3529]
གཅིག་ཏུ་བཟློག་པ་ལ་དེ་དང་འབྲེལ་པའི་མི་གཏོང་བའི་རྗེས་སུ་བསྒྲུབ་པ་ལ་གཅིག་པ་ཉིད་དང་། གཞན་ལ་ནི་གཞན་ཉིད་དང་། སྦྱོར་བར་གྱུར་པ་ལ་སྦྱོར་བར་འགྱུར་བ་ཉིད་དང་། མཐར་ཐུག་པར་གྱུར་པ་ལ་མཐར་ཐུག་པར་འགྱུར་བ༌[^2428]ཉིད་ཅེས་བྱ་བ་འདི་ལ་འདི་བྱེད་པའོ། །

[Block 3530]
གསོལ་བ་ནི་བཟློག་པ་དང་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདིར་ཡང་མི་གཏོང་བ་ལ་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3531]
བཟློག་པར༌[^2429]བྱ་བ༌[^2430]ཉིད་ལ་འདི་ཁས་ལེན་པ་སྟེ། བཟློག་པ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་རྩོམ་པ་འདིའོ། །

[Block 3532]
བསྒྲུབ་པ་འདི་ནི་བཟློག་པའི་དོན་ཅན་ཉིད་དེ། དེ་བས་ན་བཟློག་པའི་དབང་ཅན་གྱི་ཉེས་པ་བསྐྱེད་པའོ། །

[Block 3533]
ཚིག་གི་སྐད་ཅིག་མ་གཅིག་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཆ་ཤས་རེ་རེ་ལ་ཡང་འདིར་ཆ་རེ་རེ་ནི་སོ་སོར་གཅོད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 3534]
འདིར་ཤིན་ཏུ་རིང་བ་གཅིག་ཉིད་ལ་ཡང་ལྟུང་བ་གཅིག་ཉིད་དོ། །

[Block 3535]
གང་ཞིག་གང་དུ་དངོས་གཞིའི་དུས་དེའི་དུས་ལས་འབྱུང་བའི་རྣམ་པར་རིག་པ་དང་རྣམ་པར་རིག་པ་མ་ཡིན་པ་དག་ལ་ལྟུང་བ་བྱས་པ་ཉིད་དོ། །

[Block 3536]
དེའི་བདག་ཉིད་དུ་གྱུར་པ་གཞན་དག་ལ་རྣམ་པར་འགྱུར་བ་ཉིད་ཀྱི་ཕྱིར་ལྟུང་བ་རྣམ་པར་གཞག་པ་ལ་མཐོང་བའོ། །

[Block 3537]
འདིར་གཞུང་ནི་གསོལ་བ་བྱེད་པ་ན་གཞི་དེ་གཏོང་ན་དེ་ལྟ་ན་ལེགས། གལ་ཏེ་མི་གཏོང་ན་དེ་ལ་བརྗོད་པར་བྱས་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3538]
སྐད་ཅིག་མ་གང་ལ་ཕལ་ཆེར་བྱས་པ་ཉིད་གང་ཡིན་པ༌[^2431]ནི་འདིར་དངོས་གཞིའི་དུས༌[^2432]ཤེས་པར་བྱའོ། །

[Block 3539]
བཟླས་པ་ནི་ཐ་དད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ལས་སོ་སོ་ལ་ཟློག་པར་བྱེད་པ་ནི་ཐ་དད་པའོ། །

[Block 3540]
དང་པོ་འདི་དག་ལ་སོ་སོར་སྦོམ་པོ་སྟེ། ཕྱི་མ་ནི་དངོས་གཞིའོ་ཞེས་བྱ་བ་གང་ཞིག་བརྗོད་པ་དེ་བས་ན་མདོ་འདི་བརྩམས་པའོ། །
--- END BLOCKS ---
