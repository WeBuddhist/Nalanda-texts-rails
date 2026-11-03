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

[Block 3541]
མཇུག་སྡུད་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱིས་བཟོད་ཅིང་གནང་ནས་ཞེས་བྱ་བ་ལ་སོགས་པའི་མཇུག་སྡུད་པ་ལ་སོ་སོ་ཉིད་མ་ཡིན་ནོ། །

[Block 3542]
བྱས་པ་ནི་གོ་བར་བྱ་བ་ཙམ་ཉིད་ཀྱི་ཕྱིར་ལྷག་མ་ལྟར་དངོས་གཞིའི་དུས་ཀྱི་ཐ་མ་རྒྱུན་ལས་འདི་ལ་སྔོན་དུ་ཞུགས་པ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3543]
སྔར་སྔོན་དུ་འདི་ལ་ཞུགས་པ་གང་དུ་རིགས་པ་མ་ཡིན་ཏེ་ཕྱི་མ་བསྒྲུབ་པ་ལ་རིགས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འཇུག་པ་ཉིད་ནི་སྦྱོར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་དབྱེན་བྱ་བ་ལ་བརྩམས་པ་ལ་སོགས་པའི་འཇུག་པ་ནི་སྦྱོར་བ་ཉིད་དེ། དུས་གང་ཞིག་ལ་འཇུག་པ་གང་ཡིན་པ་ཞེས་བྱ་བ་འདིར་ཁྱད་པར་མ་བརྗོད་པས༌[^2433]སྔར་ཡང་བཞམས་ཏེ་བསྒོ་བ་ལ་སོགས་པའི་འོག་ཏུ་འམ་གསོལ་པ་ལ་སོགས་པའི་བར་དུ་ཡང་ཞེས་བྱ་བ་ཤེས་པར་བྱའོ། །

[Block 3544]
མ་གཏད་པའི་ཕྱིར་ཤིན་ཏུ་དམན་པ་འཇུག་པ་འདི་ཡིན་ཏེ། དེ་བས་ན་འདིས་དེ་མ་ཐག་པའི་མི་གཏོང་བ་ལ་སྦྱོར་བ་ཉིད་དུ་གྲགས་པར་འགྱུར་རོ། །

[Block 3545]
བསྐྲད་པའི་ལས་མ་བགྱིས་པར་ཡང་འདུན་པས་འགྲོ་བ་ལ་སོགས་པ་ཉིད་ཀྱིས་འགྲོ་བར་བྱེད་པ་ལ་འདི་ལས་སྦྱོར་བ་ཉིད་ཐལ་བ་དང་། བསྐྲད་པ་དང་གླེང་བ་དང་དྲན་པར་བྱེད་དུ་འཇུག་པ་ལ་ཡང་བརྩམ་པར༌[^2434]བྱ་བ་ཉིད་གོ་བར་བྱེད་པས་དེ་བསལ་བར་བྱ་སྟེ། བསྐྲད་པ་དང་གླེང་བ་དང་དྲན་པར་མ་བྱས་པར་དེའི་འོ་ཞེས་བྱ་བ་ནི་གནས་འདི་ལ་སྦྱོར་བ་འཇུག་པའི་ཕྱིར་རོ།[^2435] །སྦྱོར་བ་ཉིད་དེ་དངོས་གཞིའི་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3546]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 3547]
བསྐྲད་པའི་ལས་མ་བགྱིས་པར༌[^2436]དེ་འདུན་པས་མཆིའོ་ཞེས་བགྱི་བ་དང་། ཞེ་སྡང་གིས་མཆི་བ་དང་། གཏི་མུག་གིས་མཆི་བ་དང་། འཇིགས་པས་མཆིའོ་ཞེས་བགྱི་བའི་བར་དུ་མཆི་ན། ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 3548]
བསྒོ་བར་བགྱི་འམ་འོན་ཏེ་བསྒོ་བར་མི་བགྱི། བཀའ་སྩལ་པ། བསྒོ་བར་མི་བྱའོ། །

[Block 3549]
བསྒོ་བ་འཆགས༌[^2437]སམ་མི་འཆགས། བཀའ་སྩལ་པ། མི་འཆགས་སོ། །

[Block 3550]
གླེང་བར་མ་བགྱིས་དྲན་པར་མ་བགྱིས་པར་བདག་ཉིད་ངག་མི་ཉན་པ་ཉིད་དུ་འཇོག་པར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 3551]
བསྒོ་བར་བགྱི་འམ་འོན་ཏེ་བསྒོ་བར་མི་བགྱིད། [^2438]བཀའ་སྩལ་པ་བསྒོ་བར་མི་བྱའོ། །

[Block 3552]
བསྒོ་བ་འཆགས་སམ་མི་འཆགས། བཀའ་སྩལ་པ། མི་འཆགས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3553]
སླར་ཅིའི་ཕྱིར་གནས་སྐབས་འདི་ལ་ནི་ཉེས་བྱས་བསྐྱེད་པ་སྟེ། འདི་ལ་ཤིན་ཏུ་མངོན་པར་ཞེན་པ་གཞན་གནས་པའི་ཕྱིར་ཤིན་ཏུ་སྡིག་པའི་བསམ་པ་ཤས་ཆུང་བ་ལ་ཇི་ལྟར་དྲན་པར་བྱེད་པ་མ་ཚང་བས༌[^2439]མེད་པའོ། །

[Block 3554]
ཁ་ན་མ་ཐོ་བ་མ་ཡིན་པ་དག་ཉིད་ལ་དྲན་པ་རྙེད་པས་ཡིད་ལ་གནས་པའི་ཕྱིར་བརྩོན་པ་ངན་པ་ཉིད་ཀྱིས་དྲན་པར་མི་བྱེད་ཅིང་གླེང་བ་ལ་སྡིག་པ་དང་བཅས་པ་ཉིད་མཐོང་ཤིང་ཚིག་གི༌[^2440]སྒོ་ནས་མཐུ་དང་ལྡན་པ་ཉིད་སྡིག་པའི་བསམ་པ་ཅན་ལ་སོ་སོར་ཉེ་བར་གནས་པར་འགྱུར་རོ། །

[Block 3555]
བརྩོན་པ་བཟང་བ་ཉིད་ཀྱང་བསམས་པར་གྱུར་པ་ལ་གླེང་བ་ལ་གནས་པ་ཉིད་དོ། །

[Block 3556]
གླེང་བར་བྱེད་པ་པོ་ལ་གནས་པ༌[^2441]ཡིན་ཏེ། གླེང་བ་ནི་ཕྱོགས་གཅིག་ཏུ་གྱུར་པའོ། །

[Block 3557]
འདིར་གླེང་བ་ཡོངས་སུ་རྫོགས་པར་གྱུར་པ་དྲན་པར་བྱེད་པ་ལ་འདོད་པ་ཡིན་ནོ། །

[Block 3558]
གང་ཞིག་མེད་པར་བསྟན་པ་བཟུང་བས་རྩོམ་པ༌[^2442]པོའམ། བདག་ཉིད་གླེང་བའི་བསམ་པ་མ་ཡིན་པ་དེ་ནི་འདིར་དྲན་དུ་འཇུག་པར་ཤེས་པར་བྱའོ། །

[Block 3559]
ཚིག་འདི་གཉིས་ཀྱིས་ནི་གླེང་བ་ཡོངས་སུ་རྫོགས་པར་བྱས་པ་ཡིན་ནོ། །

[Block 3560]
དེ་ལྟ་བུའི་གླེང་བ་པོ་ཉིད་མེད་པ་ལ་ཉེས་བྱས་སུ་ཞེས་བྱའོ། །

[Block 3561]
དེ་ལ་ནི་བསྒོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། བསྐྲད་པར་མ་བགྱིས་པ་ལ་གླེང་བ་དང་། དྲན་པར་མ་བྱས་པ་ལ་བྱེ་བྲག་ཡོངས་སུ་མ་བཟུང་བས། བཞམས་ཏེ་བསྒོ་བ་ལས་ཀྱང་སྟེ་ལས་གཅིག་པུས་མ་ཡིན་ནོ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 3562]
དེ་དག་ལ་བཞམས་པ་དང་། ལས་ཀྱིས་མི་བསྒོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་དབྱེན་བྱེད་པ་ལ་རྩོལ་བ་ལ་སོགས་པ། འདི་རྣམས་ལ་གཞམས༌[^2443]ཏེ། བསྒོ་བའི་ལས་ཀྱིས་མི་བསྒོ་བར་མི་བྱའོ། །

[Block 3563]
དགེ་སློང་དག་ཁྱེད་ཀྱིས་བསྒོ་བར་གྱིས་ཤིག་ཅེས་བྱ་བ་ལ་སོགས་པས་བཞམས་ཏེ་བསྒོ་བའི་ལས་ཀྱིས་བྱས་པ་དག་ལ་བསླབ་པའི་གཞི་འདི་རྣམས་ལ་གོ་བར་བྱེད་པ་དག་ལ་བསྡུས་པ༌[^2444]འདི་ཡིན་ནོ། །

[Block 3564]
སྐྱོན་རབ་ཏུ་ཞི་བའི་དོན་དུ་འདི་བྱས་པའོ། །

[Block 3565]
སྐྱོན་ལ་ལྟོས་པ་ནི་མི་རིགས་པ་སྟེ་ཞེས་བྱ་བ་ངེས་པར་བྱ་བ་ཉིད་ཀྱིས་བསམས༌[^2445]པས་འདི་ཤེས་པའོ། །

[Block 3566]
འདིར་ལས་ཀྱིས་ཞེས་བྱ་བ་ཚིག་གཅིག་གིས་ཀྱང་དོན་འགྲུབ་པའོ། །

[Block 3567]
དགེ་འདུན་བྱེད་པ་པོ་ཉིད་ཀྱི་ཕྱིར་བཞམས་ཏེ་བསྒོ་བ་ཞེས་བྱ་བ་འདིའི་དོན་དུའོ། །

[Block 3568]
མི་བསྒོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་མང་པོའི་ཚིག་བཟུང་བའོ། །

[Block 3569]
འདིར་དགེ་འདུན་གྱི་བྱེད་པ་པོ་ཉིད་མ་ཡིན་ཏེ་གནས་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3570]
དེ་ལྟར་ཡང་འདི་དགེ་སློང་མང་པོ་རྣམས་ཀྱིས་བཞམས་ཏེ་བསྒོ་བས་བསྒོ་བ་དེ་འདིར༌[^2446]དགེ་སློང་མང་པོ་རྣམས་ཀྱིས་བཞམས་ཏེ་བསྒོ་བར༌[^2447]གནང་བར་གྱུར་པ་ན་ཞེས་བྱ་བའི་ཚིག་འདིར་མང་པོར་གྱུར་པ་རྣམས་ཀྱིས་དེར་འཇུག་པར་བྱ་སྟེ། མང་པོ་མ་ཡིན་པ་རྣམས་ཀྱིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་བསྟན་པའི་དོན་དུ་མང་པོའི་ཚིག་ལ་དགོངས་པ་ཉིད་དོ། །

[Block 3571]
གང་དུ་བསྒོ་བ་ལས་གྱུར་པའི་དགེ་འདུན༌[^2448]ལྷག་མ་རྣམས་ཤེ་ན། དེའི་ཕྱིར་དེའི་མཐའ་ལ་མི་གཏོང་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་འདི་ལས་ཀྱི༌[^2449]གལ་ཏེ་ཞེས་བྱ་བ་སྨོས་པ་ལ་བསྒོ་བའི་མཐའ་སྟེ། ཐ་མ་ལ་མི་གཏོང་བ་གང་ཡིན་པ་དེ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3572]
ད་ནི་འདི་བསྒོ་བར་བྱེད་པ་ཐུན་མོང་བ་སྟེ་བསྒོ་བར་བྱེད་པ་ལས་སྐྱེས་པའི་དགེ་འདུན་གྱི་ལྷག་མ་རྣམས་ལ་བརྩམས་ལ༌[^2450]སོ་སོ་དང་འབྲེལ་པ་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་བརྗོད་པར་བྱ་སྟེ། དོན་གང་མི་གཏོང་ན། དགེ་འདུན་གྱི་དབྱེན་བྱེད་པའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བརྟུལ་བར་བྱེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་བརྟུལ་བར་བྱེད་པ་ཉིད་ཅེ་ན་དེའི་ཕྱིར་དབྱེན་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །གང་གི་ཕྱིར་དབྱེན་བྱེད་པ་ལ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་གྱིའོ་ཞེས་སྨོས་ཏེ། དགེ་འདུན་གྱི་དབྱེན་ལའོ། །

[Block 3573]
དབྱེན་བྱེད་པའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 3574]
གང་ཞིག་མི་གཏོང་ན་དེའི་རྗེས་སུ་ཕྱོགས་པ་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དེའི་གྲོགས་ཉིད་རྗེས་སུ་སྒྲུབ་པར་བྱེད་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དང་འབྲེལ་པ་དེར་དགེ་འདུན་གྱི་དབྱེན་དང་འབྲེལ་པའི་གྲོགས༌[^2451]ནི་དེའི་གྲོགས་ཉིད་དོ། །

[Block 3575]
དེ་ལ༌[^2452]རྗེས་སུ་བསྒྲུབ་པ་ཉིད་ནི་ཤིན་ཏུ་དམན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །
--- END BLOCKS ---
