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
[Block 4411]
དེ་བས་ན་གཟུང་བ་དང་འཛིན་པ་རྣམ་པར་སྤངས་པའོ། །

[Block 4412]
དེས་ནི་གང་ཟག་ལ་བདག་མེད་པ་དང་ཆོས་ལ་བདག་མེད་པ་ཉིད་བསྟན་ཏོ། །

[Block 4413]
དེས་ནི་རྣལ་འབྱོར་སྤྱོད་པ་རྣམས་ཀྱི་རྣམ་པ་དང་བཅས་པ་དང་། རྣམ་པ་མེད་པའི་རྣམ་རིག་ཙམ་གྱི་ཕྱོགས་སེལ་ཏོ། །

[Block 4414]
གཉིས་ཀ་ལ་བདག་མེད་པའི་མཚན་ཉིད་ཅན་གྱི་ཐེག་པ་ཆེན་པོའི༌[^2684]ཕྱོགས་བསྟན་པར་བྱ་བའི་ཕྱིར། ཆོས་བདག་མེད་པ་ནི་རང་བཞིན་གྱིས་འོད་གསལ་བ་སྟེ་ཞེས་པ་ལ། །ཆོས་ཐམས་ཅད་ནི་ཕུང་པོ་ལ་སོགས་པ་དང་རྣམ་རིག་ཙམ་སྟེ། དེ་དག་རང་བཞིན་གྱིས་བདག་མེད་པ་སྟེ་སྟོང་པའོ། །

[Block 4415]
སྒོམ་པ་ནི༌[^2685]འདི་ལ་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་ཡན་ལག་ཡིན་ཏེ། དེ་ལ་ཆོས་ཐམས་ཅད་སྟོང་པ་ཡིན་ཏེ། གཅིག་དང་དུ་མ་དང་བྲལ་བའི་ཕྱིར་ཏེ་གཟུགས་བརྙན༌[^2686]བཞིན་ནོ། །

[Block 4416]
དབང་ཕྱུག་ལ་སོགས་པའི་རྒྱུ་བྱས་པ་ཡང་མ་ཡིན་ཏེ། རྒྱུ་རྣམས་མེད་པའི་ཕྱིར་རོ། །

[Block 4417]
སྨོན་པའི་འབྲས་བུ་ཡང་མ་ཡིན་ཏེ། སྨོན་ལམ་ལ་སོགས་པ་དམིགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4418 [VERSE]]
དེ་ལྟར་འོད་གསལ་བ་ཞེས་ཉེ་བར་བསྡུས་པའོ། །
གང་གི་རང་བཞིན་ངོ་བོ་ཡོད་མ་ཡིན། །
ངོ་བོ་མེད་དེ་གཞན་གྱི་ཇི་ལྟར་རྒྱུ། །
ངོ་བོ་མེད་པས་ཇི་ལྟར་འབྲས་བུ་སྐྱེ། །

[Block 4419]
བདེ་བར་གཤེགས་པས་གཏན་ཚིགས་ཇི་ལྟར་གསུངས། །

[Block 4420]
དེ་བཞིན་དུ། ཡི་གེ་ཨ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་སྒོ་ཡིན་ཏེ། །གཟོད་མ་ནས་མ་སྐྱེས་པའི་ཕྱིར་རོ། །

[Block 4421]
ཡི་གེ་ཙ་ནི་ཆོས་ཐམས་ཅད་ཀྱི་སྒོ་ཡིན་ཏེ། འཆི་འཕོ་བ་དང་སྐྱེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 4422]
ཡི་གེ་ཤ་ཆོས་ཐམས་ཅད་ཀྱི་སྒོ་ཡིན་ཏེ། ཞི་བའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4423]
ཡི་གེ་ཧ་ཆོས་ཐམས་ཅད་ཀྱི་སྒོ་ཡིན་ཏེ། དགའ་བ་དང་མྱ་ངན་ལས་འདས་པའི་ཕྱིར་རོ། །

[Block 4424]
དེ་ལ་སོགས་པ་ཆོས་ཀྱི་ཡི་གེ་ངེས་པའི་ཚིག་གི་སྒོ་ནས་བདག་མེད་པ་ཉིད་བསྟན་ཏོ། །

[Block 4425]
དེ་ལྟར་ཆོས་བདག་མེད་པ་ཉིད་ནི་འོད་གསལ་བ་སྟེ། གཟུང་བ་དང་འཛིན་པ་དང་བྲལ་བ། ཆགས་བྲལ་དང་ཆགས་པ་དང་ཆགས་པ་བར་མའི་རིམ་གྱིས་རྣམ་པར་སྦྱངས་པའི་དེ་ཁོ་ན་ཉིད་བཞི་པའོ། །

[Block 4426]
དེ་དང་མཉམ་པ་ཉིད་ནི་གཉིས་སུ་མེད་པ་ཡིན་པར་དགོངས་སོ་ཞེས་པ་ནི་ཇི་ལྟར་བདག་ཉིད་ཀྱིས་འོད་གསལ་བ་ཉམས་སུ་མྱོང་བ་དེ་བཞིན་དུ་ཏིང་ངེ་འཛིན་དེ་ཉིད་ཀྱིས་ཁམས་གསུམ་པ་ཡང་འོད་གསལ་བའི་རང་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 4427]
དཔེར་ན་རིལ་པོར་འཛིན་པའི་ཏིང་ངེ་འཛིན་གྱིས་བདག་ཉིད་འོད་གསལ་བར་བྱས་ནས་ཁམས་གསུམ་པ་ཡང་དེ་བཞིན་དུ་བྱ་བ་ནི་རྗེས་སུ་གཞིག་པའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 4428]
རབ་ཏུ་བྱེད་པ་ལས།

[Block 4429 [VERSE]]
མགོ་བོ་ནས་ནི་རྐང་པའི་བར། །
ཇི་སྲིད་སྙིང་གར་ཕྱིན་གྱི་བར། །
རྣལ་འབྱོར་ཡང་དག་མཐའ་ལ་འཇུག །
རིལ་པོར་འཛིན་པ་དེ་བཤད་དོ། །

[Block 4430 [VERSE]]
བརྟན་པ༌[^2687]དང་ནི་གཡོ་བ་དག །
སྔོན་དུ་འོད་གསལ་བར་བྱས་ཏེ། །
ཕྱི་ནས་དེ་བཞིན་བདག་བྱས་པའི། །
རྗེས་སུ་འཇིག་པའི༌[^2688]རིམ་འདི་ཡིན། །

[Block 4431]
ཞེས་འབྱུང་ངོ་། །ཆོས་བདག་མེད་པ་སྟེ་དེ་རྣམས་དང་མཉམ་པ་ཉིད་ཡིན་པས། ཤེས་པ་ནི་རང་དང་གཞན་གྱི་རྒྱུད་ལ་གནས་པའི་དངོས་པོའི་ཚོགས་ངོ་བོ་མེད་པ་འོད་གསལ་བ་དང་མཚུངས་པས༌[^2689]སོ། །

[Block 4432]
རང་གི་སེམས་ཞེས་པ་ནི་རང་དང་གཞན་གྱི་རྒྱུད་ལ་གནས་པའི་སེམས་སོ། །

[Block 4433]
ཡེ་ནས་མ་སྐྱེས་པ་ཞེས་པ་ནི་འོད་གསལ་བའི་རང་བཞིན་ནོ། །

[Block 4434]
རྡོ་རྗེ་གསུམ་མི་ཕྱེད་པའི་ལུས་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུའི་རང་བཞིན་གང་ལ་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 4435]
དེ་ཉིད་ཀྱི་ཕྱིར། སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་སྟེ། །ཞེས་པ་ནི་ལྷན་ཅིག་སྐྱེས་པའི་དགའ་བའི་མིང་གི་རྣམ་གྲངས་ཅན་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཀྱི་ངོ་བོ་འོད་གསལ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4436]
མིག་གི་སྤྱོད་ཡུལ་མ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་པ་ལ་ཉེ་བར་མཚོན་པ་ཡིན་ཏེ། དབང་པོ་ཀུན་ལས་འདས་པ་ཡང་ཡིན་པར་ཤེས་པར་བྱ་སྟེ། འདུས་མ་བྱས་པའི་ཕྱིར་རོ། །

[Block 4437]
དགོངས་པ་མ་ཡིན་པ་ནི་རིམ་པ་བཞི་པས་མངོན་པར་བྱང་ཆུབ་པ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 4438]
མི་བསྐྱོད་པའི་ཚིགས་སུ་བཅད་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། མི་ཟད་པ་ཞེས་བྱ་བ་ནི་མི་ཟད་ཅིང་འཇིག་པར་མི་འགྱུར་བས་ན༌[^2690]མི་ཟད་པ་ནི་དོན་དམ་པའི་བདེན་པ་སྟེ། སྐྱེ་བ་དང་འཇིག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4439 [VERSE]]
བརྟན་ཞིང་སྙིང་པོ་ཁོང་སྟོང་མེད། །
གཅོད་མེད་དབྱེར་མེད་མཚན་ཉིད་མེད། །
སྲེད་པ༌[^2691]མེད་ཅིང་འཇིག་མེད་པ། །
སྟོང་པ་ཉིད་ནི་རྡོ་རྗེར༌[^2692]བཤད། །

[Block 4440]
ཅེས་རྡོ་རྗེ་རྩེ་མོ་ལས་འབྱུང་ངོ་། །ཡང་དག་པའི་མཐའ་ཞེས་པ་ནི་དེ་བཞིན་ཉིད་དེ་སེམས་རྣམ་པར་དག་པའི་རིམ་པས་ཐོབ་པར་བྱ་བའི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 4441]
དེ་ཉིད་རྡོ་རྗེ་སྟེ་ཞེས་པ་ནི་བདུད་ཐམས་ཅད་ཀྱིས༌[^2693]དབྱེར་མི་ཕྱེད་པའི་ཕྱིར་རོ། །

[Block 4442]
དེ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་ཞེས་པ་ནི་སྔགས་དང༌[^2694]ཕྱག་རྒྱའི་རིམ་པའི་མཚན་ཉིད་ཅན་གྱི་སེམས་རྩེ་གཅིག་པ་ཉིད་དོ། །

[Block 4443]
དེ་ལ་སྙོམས་པར་ཞུགས་ནས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4444]
ཕྱི་དང་ནང་གི་བདག་ཉིད་ཅན་གྱི་དངོས་པོ་འདི་རྣམས་ཞེས་པ་ནི། སྣོད་ཀྱི་འཇིག་རྟེན་དང་བཅུད་ཀྱི༌[^2695]འཇིག་རྟེན་གྱི་རང་བཞིན་གྱིས་སྣང་བའི་རྣམ་པར་ཤེས་པ་གསུམ་མོ། །

[Block 4445]
དེ་དག་མ་སྐྱེས་པ་སྟེ་ཞེས་པ་ནི། སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་སྤོང་བར་འགྱུར་ན་རང་བཞིན་མེད་པ་དེ་ཉིད་དོ། །

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
--- END BLOCKS ---
