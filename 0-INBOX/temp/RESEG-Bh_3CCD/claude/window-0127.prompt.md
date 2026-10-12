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
[Block 4446]
རང་བཞིན་གྱིས༌[^2696]འོད་གསལ་བའི་ཕྱིར་རོ་ཞེས་པ་ནི་ཐམས་ཅད་སྟོང་པའམ། གནས་ལ་འཇུག་པས་སོ། །

[Block 4447]
དེ་བས་ན་ཆོས་རྣམས༌[^2697]རེ་ཞིག་མེད་པ་ཁོ་ནའོ་ཞེས་པ་ནི་སྔར་བཤད་པའི་རིགས་པས་རྣམ་པར་ཤེས་པ་གསུམ་སྤོང་བར་འགྱུར་ན་ཡོད་པ་མ་ཡིན་པའི་རྒྱུད་དེ་ལས་སོ། །

[Block 4448]
ཆོས་ཉིད་མེད་པ་སྟེ༌[^2698]ཞེས་པ་ནི་དེ་རྣམས་ཀྱི་ཆོས་ཉིད་ཀྱང་མེད། །རྣམ་པར་ཤེས་པ་གསུམ་མེད་པས་དེ་ལས་བྱུང་བའི་ཤེས་རབ་དང་ཐབས་དང་མ་རིག་པའི་ངོ་བོ། །

[Block 4449]
ཉིན༌[^2699]དང་མཚན་མོ་རང་བཞིན་བརྒྱ་དྲུག་ཅུ་ཡང་མེད་དོ། །

[Block 4450]
ཆོས་རྣམས་མེད་པའི་ཕྱིར་རོ་ཞེས་པ་ནི་སེམས་ཀྱི་རང་བཞིན་རྣམ་པར་ཤེས་པ་གསུམ་མེད་པས་སོ། །

[Block 4451]
རང་བཞིན་གྱི་ཚོགས་ནི་རྣམ་པར་ཤེས་པ་གསུམ་གྱི་རྩ་བ་ཅན་ཡིན་ཏེ། རྣམ་པར་ཤེས་པ་གསུམ་མེད་ན་དེ་ལས་བྱུང་བའི་སེམས་ལས༌[^2700]བྱུང་བའི་རང་བཞིན་རྣམས་ཀྱང་མེད་དེ་རྒྱུ་མེད་པའི་ཕྱིར་རོ། །

[Block 4452]
དེ་བས་ན་འདི་ལྟར་ནམ་མཁའ་ལྟ་བུར་བདག་མེད་པའི་མཚན་ཉིད་ཅན་ཞེས་པ་ནི་དེ་ཉིད་ཐམས་ཅད་སྟོང་པ་ཞེས་བྱ་བའི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་ཀྱི་ཁྱད་པར་རོ། །

[Block 4453]
བྱང་ཆུབ་པའི་ཐབས་སོ་ཞེས་པ་ནི་སེམས་ཀྱི་འོད་གསལ་བ་ལ་འཇུག་པའི་མཚན་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་ཀྱི་ལམ་མོ། །

[Block 4454]
སྙིང་པོ་ཡོད་པ་ཡིན་ནོ་ཞེས་པ་ནི་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་བརྟན་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4455]
དེ་བཞིན་གཤེགས་པ་མི་བསྐྱོད་པས་གསུངས་པ་སྟེ་ཞེས་པ་ནི་རྣམ་པར་ཤེས་པའི་ཕུང་པོ་རྣམ་པར་དག་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4456]
དགོངས་པ་མ་ཡིན་པ་ཞེས་པ་ནི་སེམས་རྣམ་པར་དག་པའི་རིམ་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4457]
བདག་མེད་པ་ནི་དོན་དམ་པའི་བདེན་པའོ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རང་བཞིན་གྱི་རྣམ་པར་ཤེས་པ་གསུམ་རྣམ་པར་དག་པའི་མཚན་ཉིད་ཡིན་པས་འོད་གསལ་བ་ཉིད་དོན་དམ་པའི་བདེན་པ་ཞེས་བཤད་དོ། །

[Block 4458]
སྣང་བ་ལ་སོགས་པའི་རྣམ་པར་དག་པའི་ངོ་བོ་ཐམས་ཅད་སྟོང་པའི་གོ་འཕང་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4459]
དེ་ཉིད་རྡོ་རྗེ་ཞེས་པ་ནི་ས་བཅུ་པ་ལ་ཡེ་ཤེས་ཀྱི་དབང་ཐོབ་པ་དང་ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ་རྣམས་སོ་ཞེས་པ་ནི་དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པའི་ཆོས་དང་ལྡན་པ་རྣམ་པར་ཤེས་པ་གསུམ་མོ། །

[Block 4460]
མཚན་མ་མེད་པའི་ཕྱིར་རོ་ཞེས་པ་ནི་རྣམ་པར་ཤེས་པ་གསུམ་གྱི་རྒྱུ་མེད་པས་སོ། །

[Block 4461]
ཆོས་ཀྱི་མཚན་ཉིད་རྣམ་སྤངས་པ། །ཞེས་བྱ་བ་ནི་ཆོས་ནི་རྣམ་པར་ཤེས་པ་གསུམ་སྟེ། དེ་རྣམས་ཀྱི་མཚན་ཉིད་ནི་གང་གི་མཚོན་པར་འགྱུར་བའི་མཚན་ཉིད་དེ། དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པའི་རང་བཞིན་རྣམས་སོ། །

[Block 4462]
རྣམ་པར་སྤང༌[^2701]བྱ་བ་ནི་དེ་མེད་པའི་འོད་གསལ་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4463]
འདི་ཉིད་དུ་ནི་རིགས་པ་བསྟན་པའི་ཕྱིར། །རེ་ཞིག་ཆོས་རྣམས་ཉིད་མ་གྲུབ་ན་ཞེས་པ་ནི་རྣམ་པར་ཤེས་པ་གསུམ་ཉིད་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་སྤོང་བར་འགྱུར་ན་ནང༌[^2702]མེད་པ་ཁོ་ནའོ། །

[Block 4464]
དེ་རྣམས་ཀྱི༌[^2703]མཚན་ཉིད་ག་ལ་ཡོད་དེ་ཞེས་པ་ནི་རྣམ་པར་ཤེས་པ་དེ་རྣམས་ཀྱི་སེམས་ལས་འབྱུང་བའི་རང་བཞིན་རྣམས་ག༌[^2704]ལས་ཡོད། མོ་གཤམ་གྱི་བུ་ཞེས་བྱ་བ་ལ་སོགས་པས་དཔེ་བསྟན་ཏོ། །

[Block 4465]
འོ་ན་ཇི་ལྟར་ལྷའི་སྐུ་བསྐྱེད་ཅེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་གི་ཚེ་འོད་གསལ་བ་མངོན་དུ་གྱུར་ན། དེའི་ཚེ་སེམས་ཅན་གྱི་དོན་མ་ཡིན་ནོ་ཞེས་དེ་བསྒྲུབ་པར་བྱ་བའི་ཕྱིར་ལྷའི་སྐུ་བསྐྱེད་པ་བསྟན་ཏེ། འོད་གསལ་བ་ལས་ཅིག་ཅར་རམ༌[^2705]སྣང་བ་ཉེ་བར་ཐོབ་པ་ལ་སོགས་པའི་རིམ་པས་ཡེ་ཤེས་ཀྱི་སྐུ་སྤྲོ་བ་ནི་ལྷའི་སྐུ་བསྐྱེད་པའོ། །

[Block 4466]
དོན་དམ་པའི་བདེན་པ་སྟེ་ཞེས་པ་ནི་ཐམས་ཅད་སྟོང་པའོ། །

[Block 4467]
དེ་ལས་རང་ལ་བྱིན་གྱིས་བརླབ་པ་ཞེས་བྱ་བའི་རིམ་པ་ནི་རིམ་པ་གསུམ་པས་སོ། །

[Block 4468]
ཀུན་འབྱུང་བས་ན་ཞེས་པ་ལ་ཅིག་ཅར་རམ་རིམ་གྱིས༌[^2706]སྒྱུ་མ་ལྟ་བུ་དེ༌[^2707]ཉིད་དུ་སྐྱེས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4469]
འོ་ན་འོད་གསལ་བ་ནི་བག་ཆགས་ཀྱི་དྲི་མ་ཐམས་ཅད་དང་བྲལ་བས༌[^2708]རྣམ་པར་མི་རྟོག་པ་ཡིན་ན་དེ་ལས་ལྷའི་སྐུ་ཇི་ལྟར་བསྐྱེད་ཅེ་ན། སྨྲས་པ། སྔོན་གྱི་འཕེན་པའི་ཤུགས་ཀྱིས༌[^2709]འབྱུང་བའི་ཞེས་པ་ནི་སྔར་བསགས་པའི་ཐུགས་རྗེ་ཆེན་པོ་དང་སྨོན་ལམ་གྱི་ཤུགས་ཀྱིས་ཞེས༌[^2710]བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4470]
སྐྱོན་རྣམས་ཐམས་ཅད་སྐྱེད་བྱེད་འཇིག་ཚོགས་ལྟ་བུའི་བུད་ཤིང་རྣམ་སྲེག༌[^2711]པ། །རང་དང་གཞན་གྱི་བྱེ་བྲག་ཡུལ་རྣམ་གཉིས་སྤངས་དེ་ཡི་སྐྱོན་འབྱུང་མེད། །ཉེས་པ་མེད་ཀྱང་སྒྱུ་མའི་སྐྱེས་བུ་ལས་ལ་ཐུགས་རྗེས་རིག་བཞིན་བསྐུལ། །སྔོན་གྱི༌[^2712]སྨོན་ལམ་གྱིས་ནི་བློ་བཟང་འཇུག་སྟེ། རྫ་མཁན་འཁོར་ལོ༌[^2713]ཤུགས་བཞིན་འཕེན། །ཞེས་འབྱུང་ངོ་། །

[Block 4471]
དེ་བས་ན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ནི་འོད་གསལ་བའི་ཏིང་ངེ་འཛིན་ལ་བཞུགས་པས་ཀྱང་སེམས་ཅན་གྱི་དོན་མཛད་དེ།

[Block 4472 [VERSE]]
སྐྱེས་བུ་ཡིད་བཞིན་ནོར་བུ་བཞིན། །
དེ་ཡི་གནས་པ་ཙམ་གྱིས་ནི། །
རྩིག་པ་ལ་སོགས་རྣམས་ལས་ཀྱང་། །
ཇི་བཞིན་བསྟན་པ་རྣམས་འབྱུང་ངོ་། །

[Block 4473]
ཞེས་འབྱུང་ངོ་། །དགོངས་པ་མ་ཡིན་ཞེས་པ་ནི་སེམས་རྣམ་པར་དག་པ་དང་བདག་བྱིན་གྱིས་བརླབ་པ་གཉིས་འཆད་པའི་ཕྱིར་རོ། །

[Block 4474]
ཡེ་ཤེས་ཀྱི་འོད་ཟེར་ཞེས་བྱ་བ་ལ་སོགས་པས་འདྲིའོ། །

[Block 4475]
འོད་གསལ་བའི་སྣང་བ་ཞེས་བྱ་བ་ནི་ལན་ནོ། །

[Block 4476]
འོད་གསལ་བ་ནི་དེ་ཁོ་ན་ཉིད་བཞི་པའོ། །

[Block 4477]
སྣང་བ་ནི་གསལ་བ་སྟེ་བདེ་བ་ཆེན་པོས་སོ་སོར་སྣང་བའོ། །

[Block 4478]
དེ་ཉིད་རྡོ་རྗེ་སྟེ་ཞེས་པ་ནི་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4479]
འདུས་བྱས་པ་དང་འདུས་མ་བྱས་པ་རྣམས་ལའོ་ཞེས་པ་ནི་ཆགས་པ་དང་བྲལ་བ་དང་ཆགས་པ་དང་ཆགས་པ་བར་མ་སྤོང་བར་འགྱུར་བ་དང་། །རིལ་པོར་འཛིན་པ་དང་རྗེས་སུ་འཇིག་པའི་ཏིང་ངེ་འཛིན་དག་ཀྱང་སྤང་བར་བྱའོ། །

[Block 4480]
བསྒོམ་པར་བྱ་བ་མེད་པའོ་ཞེས་པ༌[^2714]ནི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་ཐོབ་ན་དེ་རྣམས་བསྒོམ་པར་བྱ་བར་མི་རིགས་ཏེ། འབྲས་བུ་ཐོབ་པས་ཐབས་དོར་བར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4481]
འབྲས་བུ་ཐོབ་པས་གང་འདོར་བ༌[^2715]དེ་ནི་ཐབས་ཞེས་བཤད་པ་ཡིན།

[Block 4482 [VERSE]]
དེ་ལྟར་ཁ་ཅིག་མེ་སྒྲོན་མས། །
ལམ་ལ་མཐོང་སྟེ་དེ་ཉིད་བོར། །
ཤེས་པས་ཤེས་བྱ་གཟིགས་ནས་ནི། །
དེ་བཞིན་གཤེགས་པ་འདོར་བར་བྱ། །

[Block 4483]
ཞེས་འབྱུང་ངོ་། །ཡང་ན་བསྒོམ་པར་བྱ་བ་མེད་པའོ་ཞེས་པ་ནི་འོད་གསལ་བའི་ཡུལ་དུ་ཉིན་མོ་དང་མཚན་མོ་མཚམས་དང་ཆགས༌[^2716]དང་ཆགས་བྲལ་དང་ཆགས་པ་བར་མ་རྣམས་ནི་བསྒོམ་པར་བྱ་བ་མ་ཡིན་ཏེ། འདུས་བྱས་པ་དང་འདུས་མ་བྱས་པ་དག་འགལ་བའི་ཕྱིར་རོ། །

[Block 4484]
མཚན་མོ་སྣང་བའི་ཆ་སྟེ་ཉི་མའི་འོད་ཟེར་འགྱེད་པ་སྣང་བ་མཆེད་པ་ཡིན། །མཚམས་ནི་སྣང་བ་མཆེད་པ་རང་གི་རང་བཞིན་ལྷན་ཅིག་མིན་དང་སྦྱར། །མཚན་མོ་མ་ཡིན་མཚམས་མིན་ཉིན་མིན་རང་བཞིན་གང་དག་པ། །དེ་ནི་བྱང་ཆུབ་སྐད་ཅིག་བླ་མ་མཆོག་བཤད་རྣལ་འབྱོར་པ་ཉིད་ཡུལ། །ཞེས་འབྱུང་ངོ་། །བསྒོམ་པ་ཡང་མེད་དེ་ཞེས་བྱ་བ་ནི་དེ་ཐོབ་པར་བྱ་བའི་ཕྱིར་སེམས་རྩེ་གཅིག་པ་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་གྱི་ཁྱད་པར་ཡང་མེད་དོ། །

[Block 4485]
བསྒོམ་པར་བྱ་བ་མེད་པའི་ཕྱིར་རོ་ཞེས་པ་ལ་བསྒོམ་པར་བྱ་བ་ནི་འོད་གསལ་བ་སྟེ། དེ་མེད་པ་ནི་འདུས་བྱས༌[^2717]པའི་ཚུལ་དུ་མེད་པ་དང་། ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་དང་། བསྒོམ་པ་ནི་གློ་བུར་གྱི་དྲི་མ་སེལ་བའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
