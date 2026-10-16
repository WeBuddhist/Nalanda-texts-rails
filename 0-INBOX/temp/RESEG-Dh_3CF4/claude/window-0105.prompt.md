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
གང་སྔར་བསྟན་པའི་ཆས་པ༌[^2367]སེམས་པ་ཞེས་བྱ་བ་དེ་བསྟན་པའི་ཕྱིར། ཁྱིམ་ཡོངས་སུ་མ་བཏང་ཞིང་། འདོད་པ་རྣམས་ལ་ཉེ་བར་ལོངས་སྤྱོད་པ་ལས་ནི་ཆོས་དང་འགལ་བ་ཡིན་ཏེ། འཐབ་མོ༌[^2368]ལ་སོགས་པ་མང་བའི་ཕྱིར་རོ། །

[Block 3677]
དེ་ལྟར་ཆོས་ལ་སེམས་པ་ནི་ཁྱིམ་ན་གནས་པ་ན་དགའ་བར་མ་གྱུར་པའོ། །ཤེས་རབ་དང་ལྡན་པའི་ཕྱིར་ཁྱིམ་ན་གནས་པ་ལ་དགའ་བར་མ་གྱུར་པ་དེ་བསྟན་པའི་ཕྱིར། རྒྱལ་པོ་དང་། རྐུན་པོ་ལ་སོགས་པ་ལྔ་དང་ཐུན་མོང་དུ་གྱུར་པར་ཤེས་པའི་ཕྱིར༌[^2369]དང་། ཆོག་མི་ཤེས་པར་ཡོངས་སུ་ཤེས་པའི་ཕྱིར་དང་། ཉེས་པ་དུ་མའི་གནས་སུ་གྱུར་པར་ཤེས་པའི་ཕྱིར་ཏེ། བློ་དང་ཤེས་རབ་རབ་ཏུ་གསལ་བའི་ཕྱིར། ཁྱིམ་ན་གནས་པ་ལ་དགའ་བར་མ་གྱུར་ཏོ། །

[Block 3678]
ཁྱིམ་པའི་ཆ་ལུགས་བོར་ནས་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་ཁྱིམ་པའི་ཆ་ལུགས་བོར་ཞེ་ན། སྐྲ་དང་ཁ་སྤུ་བཟང་པོ་བྲེགས༌[^2370]པའི་ཕྱིར་དང་། [^2371]གོས་ཁ་དོག་བསྒྱུར་བ་ངུར་སྨིག༌[^2372]བགོས་པའི་ཕྱིར་རོ། །ཇི་ལྟར་རབ་ཏུ་བྱུང་བའི་ཆ་ལུགས་བླངས་ཤེ་ན། རབ་ཏུ་བྱུང་བའི་སྡོམ་པའི་དཔལ་ལ་གནས་པར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3679]
དེ་ཡང་དཀའ་ཐུབ་ཀྱི་ནགས་ཚལ་ན་གནས་མི༌[^2373]ནུས་པར་ཤེས་ནས་སོ། །

[Block 3680]
རབ་ཏུ་དཀའོ་ཞེས་བྱ་བ་ནི་བགྲོད་པར་དཀའ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3681]
དུར་ཁྲོད་དང་། ཁོང༌[^2374]སྟོང་སྨོས་པས་ནི། གནས་མལ་གྲོང་དང་ཉེ་བར་སྟོན་པ་ཡིན་ནོ། །

[Block 3682]
དེ་ཡང་གཉིས་ཏེ། བྱམས་པ་དང་། མི་བྱམས་པའི་བྱེ་བྲག་གིས་སོ། །

[Block 3683]
རི་བོ་དག་ནི་གཅན་གཟན་ཁྲོ་བོས་གང་བའོ། །

[Block 3684]
དེ་གཉིས་སྨོས༌[^2375]པ་ནི་གྲོང་ལས་ཐག་རིང་བར་སྟོན་ཏོ། །

[Block 3685]
དེ་ལྟ་བུའི་གནས་མ་ལ་གྱི་བྱེ་བྲག་མཐུན་པ་དང་། མི་མཐུན་བ་དག་ཏུ་བསམ་གཏན་བྱེད་ཅིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3686]
གྲོགས་མེད་པར༌[^2376]དེས་རབ་ཏུ་དཀའ་བས་བསམ་གཏན་བྱེད་པར་བསྟན་པའི་ཕྱིར། [^2377]འདི་ས་ནི་སྐྱེས་བུ་གཅིག་པུ༌[^2378]གཉིས་སུ་མེད་པར་གནས་པ༌[^2379]བསྟན་ཏོ། །

[Block 3687]
བུད་མེད་དག་ནི་ལྟར་ཡང་མེད་པར་བྱེད། །ཅེས་བྱ་བ༌[^2380]འདིས་ནི། བསམ་གཏན་མི་བྱེད་ཀྱང་བུད་མེད་དང་རེག་པར་གནས་པ་དང་ལྷན་ཅིག་ཏུ་འགྲོགས༌[^2381]པར་མི་རུང་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 3688]
འཆི་བ་ལ་ཕྱོགས་པའི་གནས་དེ་ལྟ་བུ་གཉི་ག་འགྲོ་བའི་འཇིགས་སུ་རུང་བ་དང་། གྲོགས་བྱེད་པ་བསྟན་པའི་སྡུག་བསྔལ་དེས་ནི་བདག་སྡུག་ཅིང་དེས་ཁྱོད་ཀྱང་མི་དགྱེས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3689]
མཆིས་པར་ནུས་པ་ཞེས་བྱ་བ་ནི་འཚོ་བར་རོ། །

[Block 3690]
དཔྱིད༌[^2382]ཀྱི་དུས་ལ་བབ་པའི་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^2383]ནི། མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་ཀྱི༌[^2384]དབང་པོས་ཉེ་བར༌[^2385]སྤྱོད་པ་སྤྱད་དུ་རུང་བའི་ནགས་ཚལ་བསྟན་ཏོ། །

[Block 3691]
ཤིང་ལོ་ལྷག་པར་མཛེས་པ་དང་ནི་ལྡན། །ཞེས་བྱ་བ་འདིས་ནི་མིག་གི་དབང་པོས་ཉེ་བར་ལོངས་སྤྱད་དུ་རུང་བའོ། །

[Block 3692]
བུང་བ་མང་པོ་སྒྲ་དི་རི་རི་ཟེར་ཞེས་པ་ལ་སོགས་པས་ནི་རྣ་བའི་དབང་པོས་ལོངས་སྤྱད་དུ་རུང་བ་བསྟན་ཏོ། །

[Block 3693]
པདྨ་དང་། ཨུཏྤ་ལ་ཁ་བྱེ་བ་ཞེས་བྱ་བ་འདིས་ནི་ལྕེ་དང་། ལུས་ཀྱི་དབང་པོས་ལོངས་སྤྱད་དུ་རུང་བ་བསྟན་ཏོ། །

[Block 3694]
མེ་ཏོག་དྲི་ཞིམ་པོ་སྣ་ཚོགས་ཀྱི་བསུང་གིས་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྣའི་དབང་པོ་དང་། ལུས་ཀྱི་དབང་པོས་ལོངས༌[^2386]སྤྱད་དུ་རུང་བ༌[^2387]བསྟན་ཏོ། །

[Block 3695]
མེ་ཏོག་སྣ་ཚོགས་ཚོམ་བུ་རབ་ཏུ་མཛེས། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་ཚིག་རྐང་གོང་མ་དག་ནི༌[^2388]དོན་ཉིད་བསྟན་ཏོ། །

[Block 3696]
གཡོན་ཅན་དང་ཐུབ་ཆོད་ཅན་རབ་ཏུ་མང་ན་ཞེས་བྱ་བ་ལ། གཡོན་ཅན་ནི་མ་དུལ་བས་བུད་མེད་ལ་སོགས་པ་ཡང་དུལ་བ་མེད་དོ། །

[Block 3697]
ཐུབ་ཆོད་ནི་འཕྲོག་པར་འདོད་པའོ། །

[Block 3698]
དབེན་པ་འདི་ན་ཞེས་བྱ་བ་ནི་རབ་མདའ༌[^2389]བཟློག་ཏུ་མེད་པར་བསྟན་ཏོ། །

[Block 3699]
དཀའ་ཐུབ་ཆུང་བ་ཞེས་བྱ་བ་འདིས་ནི་རང་ཉིད་ནུས་པ་མེད་པར་སྟོན༌[^2390]ཏོ། །

[Block 3700]
ཆོས་དང་བཅས་ཏེ་ཞེས་བྱ་བ་ནི་ཁྱོད་དང་ཁྱོད་ཀྱི་ཆོས་ལ་བརྙས་པ༌[^2391]སྟེ། འདི་དག་གིས་ནི་འཇིག་རྟེན་འདི་དང་། འཇིག༌[^2392]རྟེན་ཕ་རོལ་ལ་འཇིགས་པ་མེད་པའི་རྒྱུ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 3701]
དབེན་པ་འདི་ནི༌[^2393]དཀའ་ཐུབ་ཅེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་ནགས་ན་གནས་པས་བུད་མེད་དེ་ལ་སྟོན་ཏོ། །

[Block 3702]
ཁྲོ་བ་སྐྱེད་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི༌[^2394]ཁྱོད་ཉིད་ལ་ཡང་ཕན་པ་མེད་པར་བསྟན་པའི་ཕྱིར་ཏེ། འཇིག་རྟེན་གཉི་ག༌[^2395]ལ་ཡང་ཕན་པ་མེད་པར་ཁྲོ་བ་སྐྱེད་པ་མི་རིགས་སོ། །

[Block 3703]
དེ༌[^2396]ཅིའི་ཕྱིར་ཞེ་ན། ཡིད་འཁྲུགས་པ༌[^2397]ཉིད་ཀྱི་ཕྱིར་འདིས་ནི་ཆོས་དང་འགལ་བར་བསྟན་ཏེ། ཆོས་དང་འགལ་བར་གྱུར་པས་ནི་འཇིག་རྟེན་ཕ་རོལ་ཏུ་ཕན་པ་མེད་པ་ཉིད་དོ། །

[Block 3704]
ཆོས་དང་འགལ་བ་ལས་ནི་གྲགས་པའང་མེད་པར་འགྱུར་ཏེ། འདིས་ནི་འཇིག་རྟེན་འདི་ཉིད་ལ་ཕན་པ་མེད་པ་ཉིད་དོ། །

[Block 3705]
དེས་ན་དེ་དང་ཁྱོད་གཉི་ག་ལ་ཕན་པ་མེད་པའི་ཕྱིར། གྲོང་དུ་ཞེས་བྱ་བ་ནི་སྐྱེ་བོའི་ནང་ཉིད་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3706]
ཅི་སྟེ་སྐྱོན་དེ་གཉི་ག་མེད་ཀྱང་དཀའ་ཐུབ་ཅན་ལ་བུད་མེད་བསྙེན༌[^2398]ཅི་དགོས་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ནི་བདག་ཉིད་དང་རྗེས་སུ་མཐུན་པར་སྟོན་ཏོ།[^2399] །རྒྱགས་པར༌[^2400]བསྙེམས་སམ། གལ་ཏེ་མ་བརྟགས་པར་ཞེས་བྱ་བ་འདི་གཉིས་ཀྱིས་ནི། ཞེ་སྡང་གི་ཤས་ཆེ་བ་དང་དམན་པར་སྟོན་ཏོ། །

[Block 3707]
རྒྱགས་པས་བསྙེམས་པས༌[^2401]ཞེས་བྱ་བ་ནི་བརྟགས་པར་བྱས་ཀྱང་སྤྱོད་པ་ཟིལ་གྱིས་མནོན་པའོ། །

[Block 3708]
མ་བརྟགས་པར་ཞེས་བྱ་བ་ནི་དྲན་པ་ཉམས་པ་ལ་སོགས་པས་སོ། །

[Block 3709]
མི་མཐུན་པའི་ཕྱོགས་མི་བསྟན་པའི༌[^2402]ཕྱིར་དགྲ་ཞེ་སྡང་ལ་ཡང་རྒྱགས་པས་བསྙེམས་པ༌[^2403]དང་། མ་བརྟགས་པ༌[^2404]ཅི་རིགས་པར་བརྗོད་པར་བྱའོ། །

[Block 3710]
དེས་གནོད་པ་བྱས་སུ་ཡང་མི་དོགས་ལ་ཞེས་བྱ་བ་ནི་དེའི་རྒྱུས་གནོད་པས་ན་དེས་གནོད་པ་ནི་དེས་གནོད་པའོ། །

[Block 3711]
དེ་ལ་དོགས་པ་དང་བྲལ་བ་གང་ཡིན་པ་དེ་ནི་དེས་གནོད་པ་བྱས་སུ་མི་དོགས་པའོ། །

[Block 3712]
འདིས་ནི་འཇིག་རྟེན་འདིའི་འཇིགས༌[^2405]པ་མེད་པར་བསྟན་ཏོ། །

[Block 3713]
འདོད་པའི་འདོད་ཆགས་ཀྱི་དབང་དུ་ཡང་གྱུར་པས་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་འཇིགས་པ་མེད་པར་སྟོན་ཏོ། །

[Block 3714]
འདོད་པའི་འདོད་ཆགས་ཀྱིས་ཟིལ་གྱིས་མནན་པ་དེས་ཆོས་ལ་མི་ལྟ་བས་སོ། །

[Block 3715]
འཇིགས་པ་དང་། བག་ཚ་བ་ནི་འཇིགས་པ་དང་བག་ཚ་བ་སྟེ། དེ་གཉིས་ཀྱིས་བཞིན་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་འཇིགས་ཤིང་བག་ཚ་བས་ངོ་འཛུམ་འགྱུར་བའོ། །
--- END BLOCKS ---
