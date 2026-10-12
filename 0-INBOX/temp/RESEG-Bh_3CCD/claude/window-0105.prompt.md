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
[Block 3676]
དེ་རྣམས་སྐྲག་པར༌[^2311]མཛད་པ་ནི་དགུག་པ་དང་ཕུར་བུས་གདབ་པ་དང་། བརྡུང་བའི་མཚན་ཉིད་དོ། །

[Block 3677]
ཡང་ན་ཞེས་བྱ་བ་འདིས་ཕྱོགས་གཞན་བཤད་པ་ཡིན་ཏེ། འཇིག་རྟེན་པའི་མཁའ་འགྲོ་མ་རྣམས་ནི། ཨུ་མ་དང་། བདེ་ཕྱོགས་མ་དང་། དཔལ་མོ་དང་། གྲགས་པ་མ་ལ་སོགས་པའོ། །

[Block 3678]
དེ་རྣམས་སྐྲག་པར་མཛད་པ་ནི་ནན༌[^2312]གྱིས་ཕྲོགས་ཏེ་ལོངས་སྤྱོད་པའོ། །

[Block 3679]
ཁྲོ་བོའི་གཟུགས་ཀྱིས་དེ་དག་གདུལ་བའི་ཕྱིར་རོ། །

[Block 3680]
ཇི་སྐད་དུ།

[Block 3681]
བདེ་མཆོག་ལས།

[Block 3682 [VERSE]]
སངས་རྒྱས་ཐམས་ཅད་ལྷག་མོས་པས། །
སྡིག་མེད་སྟོབས་ཀྱིས་མནན་ནས་ཀྱང་། །
གནོད་དང་ཟིལ་གྱིས་གནོན་པ་ཡིས།[^2313] །
འཇིག་རྟེན་ཐམས་ཅད་རབ་འཇོམས་བྱེད། །

[Block 3683 [VERSE]]
ཤིན་དུ་གདུག་པ་དྲག་པོ་མཆོག །
སེམས་ཅན་ཁམས་ནི་དུ་མ་རྣམས། །
བྱི་ཤོར་རྒུ་བ༌[^2314]བཅིངས་པ་ཡིས། །
སེམས་ཅན་ཁམས་ནི་སྦྱོར་བར༌[^2315]མཛད། །

[Block 3684 [VERSE]]
ནན་གྱིས་སྒྱུ་མའི༌[^2316]སྦྱོར་བ་ཡིས། །
སྡིག་མེད་སྟོབས་ཀྱིས་བཀུག་བྱས་ནས། །
མཚོན་ཆ༌[^2317]ལྔ་ཡི་གོ་བགོ་ཞིང་། །
འཇིག་རྟེན་ཀུན་ལས་རྒྱལ་བར་འགྱུར། །

[Block 3685 [VERSE]]
འགྲོ་བ་བརྟན་དང་གཡོ་བ་དག །
འགྲུབ་པ་ཐམས་ཅད་ལས་རྒྱལ་ཞིང་། །
སྣ་ཚོགས་གདུལ་བའི་ཐབས་ཀྱིས་ནི། །
རང་གི་རྒྱལ་སྲིད་སྐྱོང་བར་མཛད། །

[Block 3686 [VERSE]]
འདོད་ལྡན་མ་ལ་འདོད་འགྱུར་ཞིང་། །
དྲག་པོ་རྣམས་ལ་དྲག་པོ་མཆོག །
ཞི་བ་རྣམས་ལ་ཞི་བ་མཆོག །
གནོད་བྱེད་རྣམས་ལ་གནོད་བྱེད་མཛད། །

[Block 3687 [VERSE]]
དབང་ཕྱུག་དམ་པ་དགུག༌[^2318]བྱས་ནས། །
སྡིག་མེད་སྟོབས་ཀྱི་ནུས་པ་ཡིས། །
ལྷ་མོ་འཇིགས་མ་དགུག༌[^2319]བྱས་ནས། །
རང་གི་ལོངས་སྤྱོད་ཀྱིས་ནི་སྤྱོད། །

[Block 3688 [VERSE]]
ཁྱབ་འཇུག་དག་ནི་བཀུག་ནས་ཀྱང་། །
སྡིག་མེད་ནུས་པའི་སྟོབས་ཀྱིས་ནི། །
ལྷ་མོ་དཔལ་མོ་བཀུག་བྱས་ནས། །
རང་གི་ལོངས་སྤྱོད་ཀྱིས་དེ་སྤྱད། །

[Block 3689 [VERSE]]
སྐྱེ་དགུའི་བདག་པོ་བཀུག་ནས་ཀྱང་། །
སྡིག་མེད་ནུས་པའི་སྟོབས་ཀྱིས་ནི། །
ནུས་པའི་ལྷ་མོ་ཕྲོགས་བྱས་ནས། །
རང་གི་ལོངས་སྤྱོད་ཀྱིས་དེ་སྤྱད། །

[Block 3690 [VERSE]]
འདོད་པའི་ལྷ་ནི་དགུག་བྱས་ནས། །
སྡིག་མེད་ནུས་པའི་སྟོབས་ཀྱིས་ནི། །
དགའ་མ༌[^2320]ཆགས་མ་དབྲོག་བྱས་ནས། །
རང་གི་ལོངས་སྤྱོད་ཀྱིས་དེ་སྤྱད། །

[Block 3691 [VERSE]]
དེ་ལ་སོགས་ཏེ་མཐའ་ཡས་མཆོག །
ཆོས་ཀྱི་དབྱིངས་དང་མཉམ་མི་མཉམ། །
ནམ་མཁའི་མཐའ་ཡི་མཐར་ཐུག་པ། །
རྡོ་རྗེ་ཆོས་མཆོག་དཔའ་བོ་རྣམས།[^2321] །

[Block 3692]
ཞེས་འབྱུང་བས་སོ། །

[Block 3693]
སྒྲ་ཇི་བཞིན་པ་ནི་དྲག་པོའི་སྤྱོད་པ་སོ་སོར་བསྟན་པས་སོ། །

[Block 3694]
དེ་ཉིད་འབྱུང་ནས་ནི་རིགས་སུ་གྱུར་པ་ཞེས་པ་ལ། རྟ་མགྲིན་ནི་འོད་དཔག་ཏུ་མེད་པའི་རིགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3695]
དྲང་བའི་དོན་ནི་བསྐྱེད་པའི་རིམ་པ་ཙམ་བསྟན་པས་སོ། །

[Block 3696]
འོད་གསལ་བ་ཞེས་པ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་སྙིང་པོར་གྱུར་པས་རིན་ཐང་མེད་པའོ། །

[Block 3697]
དེ་ཉིད་འབྱུང་གནས་ནི་བདག་བྱིན་གྱིས་རློབ་པའི་རིམ་པས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3698]
ངེས་པའི་དོན་ནི་སྒྱུ་མ་ལྟ་བུའི༌[^2322]ཏིང་ངེ་འཛིན་བསྟན་པས་སོ། །

[Block 3699]
ཉོན་མོངས་པ་རྣམས་ཀྱིས་མ་གོས་ཤིང་ཞེས་པ་ནི་དེའི་དབུས་སུ་གནས་པ་དང་དེ་རྣམས་བསྙེན་ཅིང་སོ་སོར་སྡུད་པ་དང་། བསམ་གཏན་གྱི་རིམ་པས་དེའི་སྐྱོན་གྱིས༌[^2323]མི་གོས་པའོ། །

[Block 3700]
གང་གི་ཕྱིར་འདོད་ཆགས་ལ་སོགས་པའི་ཉེས་པ་རྣམས་ཀྱིས་སོ་སོའི་སྐྱེ་བོ་འཇིག་པར་གྱུར་པ་དེ་རྣམས་ཁོ་ན་ཐབས་ཀྱིས༌[^2324]བསྟེན་པར་གྱུར་པ་ན་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་དེ་ཁོ་ན་ཉིད་ཀྱི་འབྲས་བུ་སྟེར་བར༌[^2325]འགྱུར་ཏེ་ཐབས་ལ་མཁས་པའི་ཕྱིར་རོ། །

[Block 3701 [VERSE]]
དོན་ཡོད་གྲུབ་པའི་རྒྱུད་ལས་ཀྱང་། །
རྨོངས་པ་གང་གིས་འཆིང་འགྱུར་བ། །
མཁས་པ་དེ་ཉིད་ཀྱིས་གྲོལ་འགྱུར། །
དེ་ལྟར་བྱང་ཆུབ་བསྒོམ་དོན་དུ། །

[Block 3702]
འདི་དག་ཕྱིན་ཅི་ལོག་པ་ཡིན། །ཞེས་འབྱུང་ངོ་། །

[Block 3703]
དཀོན་མཆོག་བརྩེགས་པ་ལས་ཀྱང་། འདི་ལྟ་སྟེ། འོད་སྲུངས༌[^2326]བུ་རམ་གྱི་ཞིང་ངམ། འབྲས་ཀྱི་ཞིང་དང་འདམ་བུའི་ཞིང་ལ་ལུད་ཀྱི་ཕུང་པོས་ཕན་པར་འགྱུར་ཏེ། དེ་བཞིན་དུ་ཡང་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོའི་ཉོན་མོངས་པ་ཁོ་ན་ཕན་པར་འགྱུར་ཏེ། འདི་ལྟ་སྟེ། འོད་སྲུངས་ཀི༌[^2327]ཏ་ཀིའི་མེ་ཏོག་སྤོས་ཀྱི་གླང་པོས་ཟོས་པར་གྱུར་ན་གླརྩིའི༌[^2328]དངོས་པོར་འགྱུར་རོ། །

[Block 3704]
དེ་ཉིད་གཞན་དག་གིས་ཟོས་པ་ན་མི་གཙང་བའི་གཟུགས་སུ༌[^2329]འགྱུར་རོ། །

[Block 3705]
དཔལ་མཆོག་དང་པོ་ལས་ཀྱང་།

[Block 3706 [VERSE]]
འདོད་ཆགས་ཞེ་སྡང་གཏི་མུག་ནི། །
འཇིག་རྟེན་ན་ནི་དུག་ཆེན་གསུམ། །
དུག་ཉིད་དུ་ནི་བསྟེན་པ་ན།[^2330] །
དུག་ཉིད་དུ་ནི་ཉེ་བར་འགྲོ། །

[Block 3707 [VERSE]]
བདུད་རྩི་རིམ་པས་བསྟེན་པ་ན།[^2331] །
དེ་བཞིན་བདུད་རྩི་ཉིད་དུ་འགྱུར། །

[Block 3708]
ཞེས་འབྱུང་ངོ་། །རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་།

[Block 3709 [VERSE]]
སེམས་གང་གིས་ནི་བྱིས་པ་རྣམས། །
འཁོར་བར་འཆིང་བ་ཉིད་དུ་འགྱུར། །
སེམས་དེ་ཉིད་ཀྱིས༌[^2332]རྣལ་འབྱོར་པ། །
བདེ་བར་གཤེགས་པའི་གནས་སུ་འགྲོ། །

[Block 3710]
ཞེས་སོ། །

[Block 3711]
སྦྱོར་བ་ནི་གང་དང་གང་ཁྱད་པར་ཅན༌[^2333]གྱི་བུད་ཤིང་སྐམ་པོའི་རྒྱུ༌[^2334]ལས་མེ་ལ་སོགས་པ་དེ་དང་དེ་རྣམས་སྲེག་པ༌[^2335]དང་། འཚོད་པ་ལ་སོགས་པའི་བྱ་བ་བྱེད་པར་མཐོང་ངོ་།[^2336] །བསམ་པ་བཟང་པོས་ཉེ་བར་སྤྱོད་པའི་འདོད་པའི་ཡོན་ཏན་ལྔ་ཁྱད་པར་ཅན་གྱི་ཐར་པའི་མཚན་ཉིད་ཅན་གྱི་འབྲས་བུ་སྟེར་བར་འགྱུར་ཞེས་མཐུན་པའི་དཔེའོ། །

[Block 3712]
གང་རྒྱུ་ཁྱད་པར་ཅན་ལས་མ་སྐྱེས་པ་མེ་ལ་སོགས་པ་དེ་དག་དོན་གྱི་བྱ་བ་སྒྲུབ་པར་བྱེད་པར་མི་ནུས་ཏེ། ཁྱད་པར་མ་ཡིན་པའི་བསམ་པས་གཟུགས་ལ་སོགས་པའི་ཡུལ་རྣམས་སྤྱད་པར་གྱུར་པ་ན་ཁྱད་པར་ཅན་གྱི་འབྲས་བུ་སྟེར་བར་བྱེད་པར་མི་འགྱུར་ཞེས་མི་མཐུན་པའི་དཔེའོ། །

[Block 3713]
རྒྱུ་ཁྱད་པར་ཅན་གྱི་བསམ་པས་གཟུགས་ལ་སོགས་པ་རང་བཞིན་གྱི་གཏན་ཚིགས་སོ། །

[Block 3714]
དེ་བས་ན་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཐབས་ལ་མཁས་པ་ཉིད་གང་གིས་ཡུལ་རྣམས་སྤྱད་པ་ན་ཡང་དེ་ཞེན་པ་ལས་བྱུང་བའི་སྐྱོན་རྣམས་ཀྱིས་གོས་པར་མི་འགྱུར་ཏེ་པདྨ་བཞིན་ནོ་ཞེས་དཔེའོ། །

[Block 3715]
རིགས་པ༌[^2337]འདིས་དེ་ཉིད་འཇིགས་པར་མཛད་པ་ན་ཞེས་གསུངས་སོ། །
--- END BLOCKS ---
