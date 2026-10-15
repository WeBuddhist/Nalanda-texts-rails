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
[Block 2486]
དེས་འགྱོད་པ་སྐྱེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཕམ་པའི་ལྟུང་བར་ནི་མི་འགྱུར་ཏེ། ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2487]
འདིར་མི་སྣང་བ་ཉིད་ལས་གཞན་དུ་ལྟུང་བའི་ཚིག་ལ་རྒྱུ་མཐོང་བ་ཡིན་ཏེ། སྦྱོར་བ་ཉིད་ཀྱི་ཕྱིར་འདིར་ཉེས་པ་སྦོམ་པོར་བརྗོད་པ་ཞེས་བྱ་བ་འདིར་ནི་ཤེས་པ་ཡིན་ནོ། །

[Block 2488]
མི་མཐུས༌[^1697]རྐུ་བ་ནི་དབང་དུ་བྱས་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་ནི་ནན་གྱིས་ལེན་པ་ལ་མི་ལ་བག་ཕེབས་ཤིང་དབང་དུ་བྱས་པ་ཉིད་ན༌[^1698]བརྐུས་པ་ཡིན་ནོ། །

[Block 2489]
འདིར་མི་ཞེས་སྨོས་པའི་སྒྲ་འདི་ནི་རིགས་ལ་བསྙགས་པ་དེས་ན་སྐྱེས་པ་འབའ་ཞིག་ཏུ་མ་ཟད་དེ་བུད་མེད་ལ་སོགས་པ་ལ་ཡང་ཡོད་པར་རིག་པར་བྱའོ། །

[Block 2490]
གཞན་དང་ལྷན་ཅིག་ཏུ་གཙུག་ལག་ཁང་ལ་སོགས་པ་ལས་རྐུ་བ་ནས་དབང་དུ་བྱས་པ་ལས་གྲོལ་བ༌[^1699]གང་ཡིན་པ་དེའི་དོན་དུ་ཡང་འདི་དེ་ལྟར་བླང་བར་བྱས་པ་ལ་གྲོལ་བ་ན་རྐུ་བ་སྐྱེས་པ༌[^1700]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2491]
དེ་བདག་ཉིད་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གཞན་རྣམས་ཀྱིས༌[^1701]བདག་ཉིད་དབང་དུ་བྱ་བ་ལ། སྐབས་གྲོལ་བ་གང་ཡིན་པ་འདི་ནི་རྐུ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2492]
འདིར་གཞུང་ནི་བདག་ཉིད་ལ་བརྐུས་པ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2493]
གང་བསམས་པ་དེ་དང་འབྲེལ་བས་མ་བསམས་པ་བླངས་པ་བརྐུས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 2494]
འདི་ལྟར་མ་བསམས་པ་ནི་རྐུ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2495]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་རས་སྦྱར་མ་མ་བྱིན་པར་བླངས་ནས་དེ་བརྐུས་ཏེ་བར་ཕྱེ་བ་དང་དེའི་བར་ནས་དར་རིན་ཐང་ཆེན་པོ་བྱུང་ནས་དེ་འགྱོད་པ་སྐྱེས་པ༌[^1702]དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རས་སྦྱར་མའི་རིན་ཐང་བརྩི་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2496]
འདིར་དར་རིན་ཐང་ཆེན་པོ་ནི་རྐུ་བར་བསམས་པ་མ་ཡིན་པས་དེ་བས་ན་ལྟུང་བར་མི་འགྱུར། སྦོམ་པོ་ནི་གང་གི་གང་ལེན་པ་དེ་དེའི་རྣམ་པར་གཞག་པ་ལ་གཞན་གྱིར་རྐུ་བའོ་ཞེས་བྱ་བ་ལ། སྦོམ་པོ་ནི་ཞེས་བྱ་བའི་ཚིག་དེ་དང་པོར་སྨོས་པ་ནི་དབང་དུ་བྱས་པ་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 2497]
གང་ཞིག་གང་ལེན་པ་དེའི་དེ་ཞེས་བྱ་བ་འདིའི་རྣམ་པར་གཞག་པ་ལ་བསྡུས་ནས་འཇུག་པ་རྣམས་ལ་གཞན་གྱི་ནོར་རྐུ་བ་ལ་གང་ཞིག་གྲོགས་ཀྱི་ཕྱིར་འགྲོ་བ་སྟེ། བདག་གི་དོན་དུ་ན་མ་བྱིན་པར་ལེན་པར་འདོད་པ་ནི་ཉེས་པ་སྦོམ་པོར་རོ། །

[Block 2498]
དེར་གཞན་གྱི་དོན་ཉིད་དུ་ན་ཡང་དངོས་གཞིའི་རྣམ་པའོ་ཞེས་སྨོས་པ་ནི་མདོ་འདི་སྤྲོས་པའོ། །

[Block 2499]
ཡོངས་སུ་འཛིན་པ་དང་བཅས་པའི་དུར་ཁྲོད་ནས་ལེན་པ་པོ་ཞེས་བྱ་བ་ནི་འདིར་ལེན་པའི་བདག་ཉིད་ཅན༌[^1703]ཡོངས་སུ་འཛིན་པ་དང་བཅས་པ་ཉིད་ལ་ཕམ་པར་བྱས་པ་ཉིད་དོ། །

[Block 2500]
དེ་བས་ན་མ་བྱུང་བ་དང་འབྱུང་བར་འགྱུར་བ་ཉིད་ཀྱིས་བདག་གིར་བྱ་བ་ལ་སོགས་པའི་དབང་གིས་གང་ཞིག་རྣམ་པར་གནས་པ་ཉིད་འདིར་ཡོངས་སུ་བཟུང་བ་དང་བཅས་པ་ཉིད་འདི་རིག་པར་བྱའོ། །

[Block 2501]
གང་རྣམས་ཀྱིས༌[^1704]དུར་ཁྲོད་ཀྱི་དངོས་པོ་དེ་མ་བྱུང་བར་འགྱུར་བ་དེ་རྣམས་དང་དེ་ལ་ཡོངས་སུ་འཛིན་པ་དང་བཅས་པ་ཉིད་དོ། །

[Block 2502]
ཅི་སྟེ་ཤོ་གམ་བཞིན་འདིར་ཕམ་པ་ཡོད་པར་འགྱུར་རོ་ཞེ་ན། འདི་ནི་ཡོད་པ་མ་ཡིན་ཏེ་སྐྱིན་པོ་བཞིན་དུ་ཤོ་གམ་ལ་སྦྱིན་པ་ཉིད་དོ། །

[Block 2503]
འདི་ལྟར་དུར་ཁྲོད་ཀྱི་རྫས་དེ་དག་ལ་ཕོངས་པ༌[^1705]ཉིད་ཀྱིས་བླངས་པ་ཉིད་དོ། །

[Block 2504]
བརྩེ་བ་མེད་པ་ཉིད་ཀྱིས་འདིའི་དོན་དུ་བསྲིས་ལ་སོགས་པ་ཉིད་ཀྱི་རྒྱུའོ། །

[Block 2505]
དེ་བས་ན་མ་བྱུང་བ་དང་འབྱུང་བར་མ་གྱུར་པ་ཉིད་ཡོད་ཀྱང་འདིར་མ་བྱུང་བ་རྣམས་ལ་ལོག་པར་མ་གྱུར་པ་དེའི་དངོས་པོ་ལ་བདག་གིར་བྱ་བའི་བློ་ཡང་དག་པར་གནས་པའོ། །

[Block 2506]
དེ་བས་ན་འདིར་ཕམ་པ་མི་སྐྱེད་པ་ནི་རྐུ་བའི་རྣམ་པ་འདི་ཡོངས་སུ་བཟུང་བ་དང་བཅས་པའི་འདུ་ཤེས་ཀྱིས་བཟུང་བ༌[^1706]ཞེས་བྱ་བ་འདིར་ནི་ཉེས་པ་སྦོམ་པོར་ཤེས་པའོ། །

[Block 2507]
དངོས་པོ་ཚང་བ་ནི་སྦོམ་པོ་འདི་རྟོགས་པར་བྱའོ། །

[Block 2508]
རྩ་བའི་ལྡུམ་ཞིང་དང་སྡོང་བུ་དང་ལོ་མ་དང་མེ་ཏོག་དང་འབྲས་བུའི་ཀུན་དགའ་ར་བ་ལ་སོགས་པ་གསང་སྔགས་དག་གིས་སྐེམས༌[^1707]པར་བྱེད་པའོ་ཞེས་བྱ་བ་ནི་གསང་སྔགས་དག་གིས་ཆུད་གཟོན་པས་ཆུད་གསོན་པ་དེ་བསྟན་པའི་ཕྱིར་མདོ་འདི་བསྟན་པ་ཡིན་ནོ། །

[Block 2509]
ཆས་ཀྱིས་རྡོ་བས༌[^1708]རྟ་བཀྲི་བ་དང་ཞོན་ཏེ་འདི་བརྐུ་བར་བྱའོ་སྙམ་ནས་ལུས་འགྱུར་བའོ་ཞེས་བྱ་བ་ནི་ཆས་སྦྱིན་པས་རྟ་ཁྱེར་བ་དེ་ལྟར་རྣམ་པ་དེས་རྟ་འདི་བརྐུ་བར་བྱའོ་སྙམ་དུ་ལུས་འགྱུར་བ་ལ་ཉེས་པ་སྦོམ་པོའོ། །

[Block 2510]
དེ་བཞིན་དུ་ཞོན་ཏེ་རྟ་འདི་བརྐུ་བར་བྱའོ་སྙམས༌[^1709]ནས་དེ་ལྟར་སེམས་ཤིང་ལུས་གཡོ་བ་ལ་སོགས་པས་ལུས་འགྱུར་བ་ཡང་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2511]
གྲུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གྲུ་འདིར་ཞུགས་ཏེ་འདི་རྐུ་བར༌[^1710]བྱའོ་སྙམ་དུ་སེམས་ཤིང་ལུས་འགྱུར་བར་བྱེད་ན་ཞེས་བྱ་བ་ནི་སྦོམ་པོར་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 2512]
འདི་ལས་འདི་ལྟར་སྙམ་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སྔར་འདི་ཞེས་བྱ་བ་སྨོས་པའི་ཚིག་གི་གནས་སུ་འདིར་རྟ་འདི་ལས་གྲུ་འདི་ལྟར་བརྐུ་བར་བྱའོ་སྙམ་ནས་ལུས་འགྱུར་བ་ཡང་སྦོམ་པོའོ། །

[Block 2513]
འདིར་འདི་ནི་མི་བསལ་བ་མ་ཡིན་ནོ། །

[Block 2514]
འདིར་གཞུང་ནི་དགེ་སློང་གྲུ་རིན་པོ་ཆེས་བཀང་བ་རྒལ་བར་བྱེད་པ་དེས་འདི་ལས་འདི་ལྟར་བརྐུ་བར་བྱའོ་སྙམ་ན༌[^1711]དེར་ལུས་འགྱུར་བར་བྱས་ནས་དེས་འགྱོད་པ་སྐྱེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཕམ་པར་མི་འགྱུར་ཏེ་ཉེས་པོ༌[^1712]སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2515]
ཇི་སྟེ་སྦྱོར་བའི་རྣམ་པ༌[^1713]འདི་ཡིན་གྱི་སྦྱོར་བ་ནི་མ་ཡིན་ནོ། །

[Block 2516]
དེ་བས་ན་ཉེས་བྱས་ཀྱིས་འདིར་འབྱུང་བར་འགྱུར་རོ། །

[Block 2517]
ངེས་པ་ཐོབ་པ་ལ་འབྱུང་བ་མེད་པ་མཐོང་བས་གཅིག་ཏུ་སྤྲོ་བ་ཉམས་པ་ལ་རྣམ་པར་འགྱུར་བ་འདི་ཞེས་བྱ་བ་ཤེས་པར་བྱའོ། །

[Block 2518]
དེ་ལྟར་ན་འདི་ལ་སྦྱོར་བ་ཉིད་སྐྱེས་པར་འགྱུར་རོ། །

[Block 2519]
ཕ་མ་དང་ཕུ་ནུ་དང་བུ་སྲིང་དང་མཁན་པོ་དང་སློབ་དཔོན་དང་མཆོད་རྟེན་དང་དགེ་འདུན་ལ་སོགས་པ་ལ་བསྔོས་པ་ཤོ་གམ་གཞལ་དགོས་པ་བཟླས་པའོ་ཞེས་བྱ་བ་ནི། འདི་ལ་བདག་གི་ཤོ་གམ་གྱི་བྱ་བ་འདི་དག་ཕུལ་བ་ཞེས་བྱ་བའི་བརྣག་པ་བསྐྱེད་ནས་དེ་འདའ་བར་བྱེད་ན་གཞན་དོན་ཉིད་ཀྱི་ཕྱིར་ཉེས་པ་སྦོམ་པོར་ཏེ༌[^1714]ཕམ་པ་ནི་མ་ཡིན་ནོ། །

[Block 2520]
གཞན་གྱི་དོན་ལ་ནི་དངོས་གཞིའི་རྣམ་པ་ཞེས་བྱ་བ་འདི་སྤྲོས་པ་ཡིན་ནོ། །

[Block 2521]
བརྙས་པ་དང་བསྐྱིས་པ་དག་མི་སྦྱིན་པར་སེམས་པའོ་ཞེས་བྱ་བ་ལ། བརྣོགས་པ་ནི་འདིར་བརྐུས་པའོ། །

[Block 2522]
དེ་བས་ན་དེས་སྦྱིན་པར་མི་འགྱུར་བ་ཞེས་བྱ་བ་མི་སྦྱིན་པའི་ཀུན་ཏུ་རྟོག་པ་ལ་སྦྱོར་བ་ཉིད་རིགས་པ་ཡིན་ཏེ། སྣོན་པ་ལ་ཡང་བརྙས་པ་དང་བསྐྱིས་པ་དག་ལ་སྦོམ་པོ་སྟེ། མེ་སྦྱིན་པའི་ཀུན་ཏུ་རྟོག་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་རྣམ་པར་གཞག་པར་བྱའོ། །

[Block 2523]
གཞན་གྱི་དོན་དུ་བྱིན་པ་འགོད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡོན་བདག་གིས་དགེ་འདུན་ལ་མཆོད་རྟེན་ལ་སོགས་པའི་དོན་དུ་རྫས་དགེ་སློང་གི༌[^1715]ལག་ཏུ་བྱིན་པ་དེ་རྣམས་ཀྱིས་འགོད་པ་ལ་སྦོམ་པོ་སྟེ། འདིར་དོན་མི་ཤེས་པ་ཉིད་དགེ་འདུན་གྱི་བདག་ཉིད་ཀྱི་བདག་པོ་ལ་རྒྱུ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཕམ་པ་དང་འདྲ་བའི་སྦོམ་པོའོ། །

[Block 2524]
གང་གི་ཕྱིར་དགེ་སློང་ནད་པས་དགེ་འདུན་ལ་རྫས་ཕུལ་བ་དགེ་འདུན་གྱི༌[^1716]འདི་ཤེས་པ་མ་ཡིན་ནོ། །

[Block 2525]
དགེ་འདུན་ལས་ཀྱང་ཉེ་གནས་དེ་དག་གིས༌[^1717]བརྐུ་བ་འདི་བྱས་པ་སྟེ་སྦྱིན་པ་པོ་ལ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
