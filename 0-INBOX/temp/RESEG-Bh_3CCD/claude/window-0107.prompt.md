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
[Block 3746]
ཞེས་འབྱུང་ངོ་། །

[Block 3747 [VERSE]]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་། །
འདིར་ནི་ཁ་ཅིག་མི་སྐྱེ་ཞིང་། །
ཁ་ཅིག་ཀྱང་ནི་འཆི་མི་འགྱུར། །
སེམས་ཀྱི་ངོ་བོར་རྣམ་གནས་པའི། །

[Block 3748]
འཁོར་བ་ཉིད་དུ་ཤེས་པར་བྱ། །ཞེས་འབྱུང་ངོ་། །

[Block 3749 [VERSE]]
སྲིད་པ་འཕོ་བའི་མདོ་ལས་ཀྱང་། །
དངོས་པོ་ལས་ཀྱང་དངོས་མི་སྐྱེ། །
དངོས་མེད་ལས་ཀྱང་སྐྱེ་མི་འགྱུར། །
དངོས་པོ་རྟག་ཏུ་སྐྱེ་བ་ནི། །

[Block 3750]
འཁྲུལ་པས་ནམ་མཁའི་མེ་ཏོག་བཞིན། །ཞེས་འབྱུང་ངོ་། །

[Block 3751 [VERSE]]
ཀམྤ་ལའི་ཞལ་སྔ་ནས་ཀྱིས་ཀྱང་། །
དེ་ཉིད་ཡང་དག་མཐའ་ཡིན་ཏེ། །
དེ་ཉིད་དེ་བཞིན་དེ་སྟོང་ཉིད། །
དེ་ཉིད་མཉམ་ཉིད་དེ་གྲོལ་བ། །

[Block 3752 [VERSE]]
དེ་ཉིད་རྣམ་རིག༌[^2349]ཙམ་ཉིད་དེ། །
ཆོས་ཀུན་ནང་དུ་ཆུད་པའི་ཕྱིར། །
རིང་པོར་མ་ཡིན་གམ་དུ་མིན། །
དེ་ཉིད་རྟོགས་པར༌[^2350]དཀའ་བའི་ཕྱིར། །

[Block 3753]
དེ་ཡི་ངོ་བོ་སྤྱོད་མི་འགྱུར། །ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3754]
དེ་བས་ན་དང་པོ་མ་སྐྱེས་པའི་རང་བཞིན་གྱི་དེ་ཁོ་ན་ཉིད་ཐབས་ཀྱི་དབང་གིས་ཇི་ལྟར་སྐྱེ་བར་འགྱུར་ཞེ་ན། འདིར་སྨྲས་པ། དེ་ཁོ་ན་ཉིད་ནི་ཐབས་གང་གིས་ཀྱང་སྐྱེ་བར་མི་འགྱུར་ཏེ། རང་བཞིན་གྱིས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 3755]
འོན་ཀྱང་དེ་རང་བཞིན་གྱིས་གྲུབ་ཀྱང་དེའི་དབང་པོ་གཉིས་སྙོམས་པར་ཞུགས་པ་གསལ་བར་བྱེད་པའི་རྒྱུ་ཡིན་གྱི་སྐྱེད་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 3756]
གང་གི་ཕྱིར་རྒྱུ་ནི་རྣམ་པ་བཅུ་ཡང་ཡིན་ཏེ།

[Block 3757 [VERSE]]
སྐྱེ་དང་གནས་དང་གསལ་བྱེད་དང་། །
འགྱུར་བ་རྐྱེན་དང་ཐོབ་པ་དང་། །
སྦྱོར་དང་གཞན་དང་རྟེན་དང་ནི། །
རྒྱུ༌[^2351]ནི་རྣམ་པ་བཅུ་རུ་བཤད། །

[Block 3758]
ཅེས་འབྱུང་ངོ་། །དེ་ཉིད་ཀྱི་ཕྱིར་གསལ་བ་ཙམ་རྒྱུ༌[^2352]ཡིན་ན། དེ་ཁོ་ན་ཉིད་ལ་སྐྱེད་པའི་སྐྱོན་དུ་ཐལ་བར་མི་འགྱུར་རོ། །

[Block 3759]
འོན་ཏེ་སྐད་ཀྱི་དབྱིངས་དོན་དུ་མ་ཡིན་པས་མཛད་པའི་སྒྲ་ནི་གསལ་བར་བྱེད་པ་ཙམ་ལ་འཇུག་གི་བྱེད་པ་པོའི་ནུས་པ་ལ་མ་ཡིན་ནོ་ཞེས་ཤིན་ཏུ་རྒྱས་པས་ཆོག་གོ། །

[Block 3760]
ད་ནི་རྣལ་མ་དཔྱད་པར་བྱ་སྟེ། །སྒྲ་ཇི་བཞིན་པ་ནི་ཁྲོ་བོའི་རྒྱལ་པོ་དབྱིངས་ཙམ་བསྟན་པས་སོ། །

[Block 3761]
དོན་ཡོད་པར་གྲུབ་པ་ནི། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་ལ་སོགས་པའི་ནང་དུ་འདུས་པའི་ཕྱིར་རོ། །

[Block 3762]
དོན་ཡོད་གྲུབ་པ་ནི་ཕྲག་དོག་རྣམ་པར་དག་པའི་ངོ་བོ་ཕྲག་དོག་ཡང་ཞེ་སྡང་ལས་བྱུང་བ་སྟེ། ཞེ་སྡང་གི་ངོ་བོ་ཉིད་ཐུགས་རྡོ་རྗེ་འཛིན་པའི་རིགས་སུ་འདུས་པར་འགྱུར་རོ། །

[Block 3763]
ཡང་ན་འདོད་ཆགས་ལས་བྱུང་བ་ཡིན་ན།[^2353] སྣང་བ་མཐའ་ཡས་ཀྱི་རིགས་སུ་འདུས་པར་འགྱུར་རོ། །

[Block 3764]
དེ་ཉིད་རྡོ་རྗེ་ཞེས་པ་ནི་རིགས་སམ་རྒྱས་བཏབ་པས་སོ། །

[Block 3765]
དྲང་བའི་དོན་ཞེས་བྱ་བ་འཕགས་པ་བདུད་རྩི་འཁྱིལ་པ་ཁྲོ་བོ་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3766]
རྣམ་པར་དག་པའི་གནས་ནི་འོད་གསལ་བ་སྟེ། སེམས་རྣམ་པར་དག་པའི་རིམ་པས་ཐོབ་པར་བྱ་བའི་སེམས་ཀྱི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 3767]
ངེས་པའི་དོན་ཞེས་བྱ་བ་ནི་སེམས་རྣམ་པར་དག་པའི་རིམ་པས་སོ་སོར་བསྟན་པས་སོ། །

[Block 3768]
བགེགས་རྣམས་མཐར་མཛད་ཅིང་འཇིགས་པར༌[^2354]མཛད་པས་ན་ཞེས་པ་ནི་དེ་ལ་བགེགས་ནི་བདུད་བཞི་སྟེ། དེ་རྣམས་ལ་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱིས་མཐར་བྱེད་པས་ན་བགེགས་མཐར་བྱེད་དོ། །

[Block 3769]
དྲང་བའི་དོན་ནི་བདུད་འཇོམས་པ་རྣམ་པར་བསྟན་པས་སོ། །

[Block 3770]
ཁམས་བཞི་པོ་སྟེ་ཞེས་པ་ནི་ས་ལ་སོགས་པའོ། །

[Block 3771]
འཕེལ་བ་དང་འགྲིབ་པ་ཞེས་པ་ནི་སྐྱེ་བ་དང་འཇིག་པ་དག་གིས་སོ། །

[Block 3772]
ལུས་གཟིར་བས་ན་ཞེས་པ་ནི་ལུས་ཀྱིས་ཉེ་བར་མཚོན་པའི་སེམས་གཟིར་བས་སོ། །

[Block 3773]
དེ་རྣམས་ཐབས་ཀྱི༌[^2355]ཡེ་ཤེས་ཤར་བས་ན། །ཞེས་པ་ནི་སྣང་བ་མཆེད་པའི་ཡེ་ཤེས་ཡང་དག་པར་འབྱུང་བས་སོ། །

[Block 3774]
སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱིས༌[^2356]རྣམ་པར་རྟོག་པའི་བདག་ཉིད་སེམས༌[^2357]རྣམ་པར་འཇིག་ཅིང་ཉམས་པར་མཛད་དོ། །

[Block 3775]
ངེས་པའི་དོན་ནི་སེམས་རྣམ་པར་དག་པའི༌[^2358]རབ་ཏུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3776]
དཀྱིལ་འཁོར་པ་རྣམས་མཉེས་པར་བྱེད་པའི་ཕྱིར་ཞེས་པ་ནི་དཀྱིལ་འཁོར་གྱི་བདག་པོ་དང་བཅས་པའི་དཀྱིལ་འཁོར་བ་རྣམས་བརྒྱ་བྱིན་ལ་སོགས་པའི་བགེགས་ཀྱི༌[^2359]རྣམ་པར་གཡེང་བ་ལས་བསྲུང་བས་མཉེས་པར་མཛད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3777]
དེ་བས་ན༌[^2360]བགེགས་ཐམས་ཅད་རྣམ་པར་འཇོམས་པའི་ཕྱིར་རོ༌[^2361]ཞེས་པ་ནི་བརྒྱ་བྱིན་ལ་སོགས་པ་ཕྱོགས་སྐྱོང་རྣམས་འཇོམས་པར་མཛད་པས་སོ། །

[Block 3778]
སྒྲ་ཇི་བཞིན་པ་ནི་ཁྲོ་བོའི་རྒྱལ་པོ་དང་འབྲེལ་པའི་སྐུ་ཙམ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 3779]
གཞུང་དེ་ཙམ་གྱིས་ནི་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 3780]
དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ཡོངས་སུ་རྫོགས་པར་བྱ་བའི་ཕྱིར་དཀྱིལ་འཁོར་པ་གཞན་རྣམས་ཀྱི་འབྲེལ་པ་མཁན་གྱིས་ལུང་གི་ཚད་མ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། དེ་ལྟར་སྒོ་རྣམ་པ༌[^2362]བཞིར་བཀོད་ནས་ཞེས་སྨོས་ཏེ། གཤིན་རྗེ་གཤེད་དང་། ཤེས་རབ་མཐར་བྱེད་དང་། པདྨ་མཐར་བྱེད་དང་། བགེགས་མཐར་བྱེད་རྣམས་ནི་ཤར་དང་ལྷོ་དང་ནུབ་དང་བྱང་གི་སྒོ་རྣམས་སུ་དགོད་པར་བྱའོ། །

[Block 3781]
ཤར་གྱི་མཚམས་ནས་བརྩམས་ཏེ་ཞེས་པ་ནི་མེ་དང་། བདེན་བྲལ་དང་རླུང་དང་དབང་ལྡན་གྱི་མཚམས་རྣམས༌[^2363]སུའོ། །

[Block 3782]
མི་གཡོ་བ༌[^2364]ལ་སོགས་པ༌[^2365]དགོད་པར་བྱའོ་ཞེས་པ་ནི༌[^2366]མི་གཡོ་མགོན་དང་འདོད་པའི་རྒྱལ་པོ་དང་དབྱུག་སྔོན་ཅན་དང་སྟོབས་པོ་ཆེ་དགོད་པ་ནི་བསམ་པར་བྱའོ། །

[Block 3783]
ཤར་ཕྱོགས་སུ་ནི་སྣམ་བུ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནང་གི་དཀྱིལ་འཁོར་གྱི་ཕྱི་རོལ་དུ་སྣམ་བུ་བཞི་ལ་ནི་ཤར་དུ་སའི་སྙིང་པོ་དང་བྱམས་པ་དག་གོ། །

[Block 3784]
ལྷོའི་སྣམ་བུ་ལ་ནམ་མཁའི་སྙིང་པོ་དང་ཕྱག་ན་རྡོ་རྗེ་དག་གོ། །

[Block 3785]
ནུབ་ཀྱི་སྣམ་བུ་ལ་འཇམ་དཔལ་དང་འཇིག་རྟེན་དབང་ཕྱུག་གོ། །
--- END BLOCKS ---
