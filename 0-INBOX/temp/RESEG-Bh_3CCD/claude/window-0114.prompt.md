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
[Block 3991]
སྐུ་གསུང་ཐུགས་ཀྱི་རྡོ་རྗེ་འཆང་གི་སྐུ་རྣམས་བསྒོམས་ནས་ཡང་རྡོ་རྗེ་ཕྲེང་བ་ལས་གསུངས་པའི་དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི་རིམ་པས་སྟོང་པ་ཉིད་དུ་གྱུར་པར་རྣམ་པར་བསམ་པར་བྱ་བ་དང་། ཨོཾ་ཤཱུ་ནྱ་ཏཱ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྔགས་ཀྱང་བརྗོད་དོ། །

[Block 3992]
དྲང་བའི་དོན་ནི་བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པ་དང་པོ་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་ཕྱོགས་གཅིག་པའི་རྣལ་འབྱོར་ཞེས་བྱ་བའི་ཡན་ལག་དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི་རང་བཞིན་སྟོང་པ་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་རབ་ཏུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3993]
རྫོགས་པའི་རིམ་པ་བསྟན་པའི་ཕྱིར་ཡིད་ཀྱི་རང་བཞིན་གྱི་ལུས་གཅིག་པ་ཞེས་བསྟན་ཏོ། །

[Block 3994]
སེམས་གསུམ་པོ་ཞེས་བྱ་བ༌[^2469]ལ། ཀུན་གཞི་ལ་སོགས་པ་རྣམ་པར་ཤེས་པ་གསུམ་པའོ། །

[Block 3995]
ཁམས་ཕྲ་བ་ནི་འོད་གསལ་བ་དང་ལྷན་ཅིག་ཏུའོ། །

[Block 3996]
ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་སྣང་བ་ཉེ་བར་ཐོབ་པ་ལ་སོགས་པའི་རིམ་པའམ་ཅིག་ཅར་གྱིས་རྫོགས་པའི་སྒྱུ་མ་ལྟ་བུའི་སྐུའོ། །

[Block 3997]
ལུས་གང་བསྐྱེད་པ་ཞེས་པ་ནི་འོད་གསལ་བ་ལས་ཅིག་ཅར་རམ། རིམ་གྱིས་ཡེ་ཤེས་ཀྱི་སྐུ་སྤྲོ་བའོ། །

[Block 3998]
དེ་ནི་སེམས་ཉིད་ཡིན་ནོ་ཞེས་པ་ལ། སེམས་ལ་རྣམ་པར་དག་པའི་རིམ་པས་ཐོབ་པར་བྱ་བའི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་ལས་ཡེ་ཤེས་ཀྱི་སྐུ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 3999]
ཚིག་ཏུ་བརྗོད་པ་གང་ཡིན་པ་དེ་དང་དེའི་ངོ་བོར་སེམས་ཉིད་སྐྱེད་ཅིག་པའོ་ཞེས་པ་ནི་ཚིག་ཏུ་བརྗོད་པ་ནི་ཡི་གེ་གསུམ་པོ་འཇུག་པ་ལ་སོགས་པའི་རིམ་པས་བཟླ་བའོ། །

[Block 4000]
དེ་གང་གི་ཚེ་འོད་གསལ་བའི་མཚན་ཉིད་སེམས་ལ་བརྟེན་ཏེ་འཇུག་པ་དེའི་ཚེ་ཚིག་ཏུ་བརྗོད་པ་ཉིད་སེམས་ཡིན་ནོ་ཞེས་རྡོ་རྗེ་བཟླས་པ་དང་སེམས་རྣམ་པར་དག་པ་དང་བདག་ལ་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 4001]
སྐུ་དང་ཞེས་བྱ་བ་ལ་སོགས་པས་བཞི་པ་དང་ལྔ་པའི༌[^2470]རིམ་པ་སྟོན་པར་བྱེད་དེ། དེ་ལྟར་བསྐྱེད་པའི་ཞེས་པ་ནི་རིམ་པ་གསུམ་བསྒོམ་པས་སོ། །

[Block 4002]
ནམ་མཁའི་ངོ་བོ་ཉིད་ཀྱིས་ཡང་དག་པར་སྦྱོར་ཞིང་ཞེས་པ་ལ། སྒྱུ་མའི་རང་བཞིན་གྱི་ལུས་ཀྱང༌[^2471]འོད་གསལ་བའི་རང་བཞིན་དེ་ཁོ་ན་ཉིད་ཀྱི་རྣམ་པར་སྦྱངས་ནས་སོ། །

[Block 4003]
རྡོ་རྗེ་འཆང་ཆེན་པོར་བདག་ཉིད་བསྐྱེད་པར་བྱ་བ་སྟེ་ཞེས་པ་ལ་བདེན་པ་གཉིས་གཉིས་སུ་མེད་པའི་མཚན་ཉིད་ཅན་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ལས་རྫོགས་པའི་རྡོ་རྗེའི་སྐུ་རྫོགས་པར་བྱའོ་ཞེས་པ་འདིས་མངོན་པར་བྱང་ཆུབ་པ་དང་ཟུང་དུ་འཇུག་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 4004]
དེ་ལ་མདོར་བསྡུས་པ་ནི་རིགས་བརྒྱའི་དབྱེ་བའི་འོག་ཏུ་རྫོགས་པའི་རྣལ་འབྱོར་པས་ཡི་གེ་གསུམ་པོ་འཇུག་པ་དང་། གནས་པ་དང་། ལྡང་བའི༌[^2472]རིམ་པས་རྣམ་པ་བཅུ་གཅིག་ཡན་ལག་མ་ཉམས་པའི་བཟླས་པ་བྱ་སྟེ། ངག་སྦྱང༌[^2473]བའི་འོག་ཏུ་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་རྣམ་ཤེས་གསུམ་པོ་གནས་གྱུར་པའི་མཚན་ཉིད་སྣང་བ་གསུམ་རྣམ་པར་དག་པས་སེམས་ལ་དམིགས་པ་ཐོབ་ནས་དེ་ལ་ཅིག་ཅར་རམ་སྣང་བ་ཉེ་བར་ཐོབ་པ་ལ་སོགས་པའི་རིམ་གྱིས་སེམས་ཅན་གྱི་དོན་དུ་བླངས་ལ། སྒྱུ་མའི་སྐུ་ཡང་ཆགས་པ་དང་ཆགས་བྲལ་དང་། ཆགས་པ་བར་མའི་རིམ་པས་སྦྱང་ཞིང་འོད་གསལ་བའི་རང་བཞིན་དུ་བྱས་ཏེ། དེ་ལས་ཀྱང་ཅིག་ཅར་དུ་རྣམ་པ་ཐམས་ཅད་ཀྱི་མཆོག་དང་ལྡན་པའི༌[^2474]མཚན་དང་དཔེ་བྱད་ཀྱིས་རྣམ་པར་མཛེས་པ་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ཀྱི་ངོ་བོ་རྡོ་རྗེའི་སྐུའི་རྣམ་གྲངས་ཅན་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་གྱིས་ཐོབ་པར་བྱ་བ་རྡོ་རྗེ་འཆང་གི་ཕྱག་རྒྱ་ཆེན་པོའི་སྐུ་བསྒོམ་པར་བྱའོ། །

[Block 4005]
དཔལ་རྡོ་རྗེ་ཕྲེང་བ་ཞེས་བྱ་བ་ལ་སོགས་པས་ལུང་ཚད་མ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4006]
སྙིང་པོར་གྱུར་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ཁམས་གསུམ་འདི་ལ་སྙིང་པོར་གྱུར་པ་ནི་རང་གི་སྲོག་སྟེ། རྣམ་པར་ཤེས་པ་གསུམ་མོ། །

[Block 4007]
དེ་ལ་གཞན༌[^2475]མེད་པ་ནི་རྣམ་པར་ཤེས་པའི་སྣ་ཚོགས་པ༌[^2476]ཉིད་རྣམ་པ་དེ་དང་དེར་སྣང་བའི་ཕྱིར་རོ། །

[Block 4008]
དེ་ཉིད་སེམས་རྣམ་པར་དག་པའི་རིམ་པས་རྣམ་པར༌[^2477]སྦྱངས་ནས་སེམས་ཀྱི་འོད་གསལ་བ་ཉིད་ཐོབ་པར་འགྱུར་རོ། །

[Block 4009]
དེས་ནི་སེམས་རྣམ་པར་དག་པའི་རིམ་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 4010]
སྐྱེས་བུ་ཞེས་པ་ནི་རྣལ་འབྱོར་པས་སོ། །

[Block 4011]
རླུང་གི་ཁམས་གསུམ་པ་ཞེས་པ་ལ་རླུང་གི་ཁམས་ཀྱི་རང་བཞིན་གྱི་རང་གི་ལུས་དང་ཁམས་གསུམ་པ་ལ་ཡང་དྲི་མ་མེད་པར་མཐོང་ངོ་། །དེས་ནི་ཡི་གེ་གསུམ་གྱི་རང་བཞིན་འཇུག་པ་ལ་སོགས་པའི་རིམ་པས་ཡན་ལག་མ་ཉམས་པའི་བཟླས་པ་རབ་ཏུ་བསྟན་པ་ཡིན་ནོ། །

[Block 4012]
དེ་ནི་རྡོ་རྗེ་བཟླས་པའི་རིམ་པའོ།[^2478] །

[Block 4013]
ཁམས་གསུམ་བདག་ཉིད་ཅེས་པ་ནི་ཁམས་གསུམ་གྱི་ནང་དུ་གནས་པ་ཁྱབ་འཇུག་དང་དྲག་པོ་དང་དབྱིག་སྙིང་ལ་སོགས་པའི་ནང་ན༌[^2479]མཆོག་ཏུ་གྱུར་པ་ཡེ་ཤེས་ཀྱི་སྐུའི་རྣམ་གྲངས་ཅན་བདག་ལ་བྱིན་གྱིས་རློབ་པའི༌[^2480]རིམ་པའི་མཚན་ཉིད་ཅན་སྒྱུ་མའི་སྐུ་ཐོབ་པར་འགྱུར་རོ། །

[Block 4014]
དེས་ནི་བདག་ལ་བྱིན་གྱིས་བརླབ༌[^2481]པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 4015]
གཅིག་ཏུ་མྱུར་བར་མཐོང་བ་ནི་ཞེས་པ་ལ་ཆགས་པ་དང་ཆགས་བྲལ་དང་། ཆགས་པ་བར་མ་ཡོངས་སུ་སྤངས་ནས་གཅིག་ཏུ་གྱུར་པ༌[^2482]ལྷན་ཅིག་སྐྱེས་པའི་བདེ་བ་ཆེན་པོའི་མཚན་ཉིད་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ངོ་བོ་དེ་ཁོ་ན་ཉིད་བཞི་པའི་མན་ངག་མྱུར་བར་ཕྱི་དང་ནང༌[^2483]གི་ཕྱག་རྒྱའི་དབྱེ་བའམ། ཏིང་ངེ་འཛིན་གྱི་རིམ་པས་མཐོང་བ་ནི་ཐོབ་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདིས་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 4016]
བྱིན་གྱིས་བརླབས་ནས་དེ་བཞིན་ཉིད། །ཅེས་པ་ནི་ཀུན་རྫོབ་དང་དོན་དམ་པ་དང་ཆགས་པ་དང་ཆགས་བྲལ་དང་། ཆགས་པ་བར་མ་དང་། རྟག་པ་དང་། ཆད་པ་དང་། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དང་། ཡོད་པ་དང་མེད་པ་དང་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་དང་། སྲིད་པ་དང་ཞི་བ་དང་འཆིང་བ༌[^2484]དང་གྲོལ་བ༌[^2485]དང་། ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བ་དང་ཡོངས་སུ་དག་པ་དང་། མ་དག་པ་དང་། སྔགས་ཀྱི་སྐུ་དང་། ཡེ་ཤེས་ཀྱི་སྐུ་དང་། སྟོང་པ་ཉིད་དང་། སྙིང་རྗེ་དང་། [^2486]ཤེས་རབ་དང་ཐབས་དང་། རྣམ་པ་དང་བཅས་པ་དང་རྣམ་པ་མེད་པ་དང་། གང་ཟག་ལ་བདག་མེད་པ་དང་། ཆོས་ལ་བདག་མེད་པ་དང་། མ་རིག་པ་དང་རིག་པ་ལ་སོགས་པ་ནི་བྱིན་གྱིས་བརླབ་པ་རྣམས་སོ། །

[Block 4017]
དེ་རྣམས་ཀྱི་གནས་ནི་དབྱེར་མེད་པའི་སྒོ་ནས་གཞིར་གྱུར་པའོ། །

[Block 4018]
དེ་བཞིན་ཉིད་ནི་ཆོས་ཐམས་ཅད་ཀྱི་སྙིང་པོར་གྱུར་པ་མི་སློབ་པའི་ལམ་གྱིས་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 4019]
དངོས་གྲུབ་མྱུར་བ་ཞེས་པ་ནི་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་དངོས་གྲུབ་རྣམས་ཀྱིས་མྱུར་དུ་རྒྱུར་གྱུར་པའོ། །

[Block 4020]
ཐོབ་པར་འགྱུར་ཞེས་པ་ལ་རྣལ་འབྱོར་པས་ཐོབ་པར་འགྱུར༌[^2487]ཞེས་བྱ་བ་འདིས་ཟུང་དུ་འཇུག་པའི་རིམ་པ་རབ་ཏུ་བསྟན་པ་ཡིན་ནོ། །

[Block 4021]
ངེས་པའི་དོན་ཞེས་བྱ་བ་ནི་རིམ་པ་ལྔ་པའི་རང་བཞིན་རྫོགས་པའི་རིམ་པ་གསལ་བར་བཤད་པའི་ཕྱིར་རོ། །

[Block 4022]
རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་པ་ནི་ཐོག་མ་དང་བར་མ་དང་ཐ་མར་ཀུན་ལས་བཟང་པ་གང་ལ་ཡོད་པ་ཞེས་བྱ་བས༌[^2488]སོ། །

[Block 4023]
དེའི་བྱང་ཆུབ་ཀྱི་སེམས་རབ་ཏུ་བརྟན་པ༌[^2489]ནི་ངོ་མཚར་ཆེའོ༌[^2490]ཞེས་པ་ལ་བསྐྱེད་པའི་རིམ་པའི་ཕྱོགས་སུ་སྟོང་པ་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་མངོན་དུ་གྱུར་པའི་མཚན་ཉིད་དང་རྫོགས་པའི་རིམ་པའི་ཕྱོགས་སུ་རིམ་པ་ལྔའི་ངོ་བོ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་རབ་ཏུ་བརྟན་པ༌[^2491]གང་ཡིན་པ་དེ་ནི་ངོ་མཚར་ཆེའོ་ཞེས་པ་ནི་ཚིག་གཅིག༌[^2492]གིས་དེ་རྣམས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4024]
དོན་དམ་པའི་བདེན་པ་ནི་བསྐྱེད་པའི་རིམ་པ་ལ་དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི་ངོ་བོ་སྟོང་པ་ཉིད་མངོན་དུ་བྱའོ། །

[Block 4025]
དེ་ཡིད་ཀྱི་རང་བཞིན་གྱི་ལུས་འཇུག་པ་ནི༌[^2493]ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་རྡོ་རྗེ་ཕྲེང་བ་ལས་གསུངས་པ། གཟུགས་ཕུང་རྟོག་པ་མེ་ལོང་དང་། །ཞེས་བྱ་བ་ལ་སོགས་པས་མི་སྣང་བར་བྱ་བའོ། །

[Block 4026]
འདི་གསལ་བ་ལས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་འོད་གསལ་བ་ལས་བྱུང་བའོ། །

[Block 4027]
ཡོངས་སུ་དག་པའི་ལྷའི་སྐུ་འཛིན་པའི་མཚན་ཉིད་ནི༌[^2494]ཐ་མལ་པའི་ཕུང་པོ་ལ་སོགས་པ་ལྡོག་པའི་མཚན་ཉིད་རྡོ་རྗེ་འཆང་གི་ཕྱག་རྒྱ་ཆེན་པོའི་སྐུ་རྫོགས་པའོ། །

[Block 4028]
བཞེངས་པ་ཞེས་བྱ་བ་ནི་དེ་ཉིད་དཀྱིལ་འཁོར་མ་ལུས་པ་སྤྲུལ་པར་བྱེད་པའོ། །

[Block 4029]
གང་གིས་རབ་ཏུ་སྒྲོགས་ཤིང་བརྗོད་པ་ཞེས་ངོ་མཚར་བའོ། །

[Block 4030]
དགོངས་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པའི་དོན་དམ་པའི་དཀྱིལ་འཁོར་དང་དེ་ལས་བྱུང་བའི་དག་པའི་སྐུ་བསྟན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
