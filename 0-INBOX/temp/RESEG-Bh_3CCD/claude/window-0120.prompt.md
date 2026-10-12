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
[Block 4201]
ཇི་སྐད་དུ།

[Block 4202 [VERSE]]
ཡང་དག་མ་ཡིན་ཀུན་རྟོག་ཡོད། །
དེ་ལ་གཉིས་པོ་ཡོད་མ་ཡིན། །
དེ་ལ་སྟོང་པ་ཉིད་ཡོད་དེ། །
དེ་ལ་ཡོད་ན༌[^2593]དེ་ཡོད་དོ། །

[Block 4203 [VERSE]]
ཡོད་དང་མེད་དང་ཡོད་པའི་ཕྱིར། །
དེ་ཡང་དབུ་མའི་ལམ་ཡིན་ནོ། །

[Block 4204]
ཞེས་འབྱུང་ངོ་། །དེ་བས་ན་ཕྱི་རོལ་གྱི་དངོས་པོ་ལྟ་བུར་བསྒོམ་པ་དམིགས་སུ་མེད་ཅིང་ཡོད་པ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་རྣམ་པར་ཤེས་པའི་རྣམ་པ་དངོས་པོ་སོ་སོར་སྣང་བའི་རྟོག་པ་ནི་མེད་དོ། །

[Block 4205]
སེམས་ཀྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །ཞེས་པ་ནི་སེམས་ཉིད་སོ་སོར་སྣང་བའི་ཕྱིར་རོ། །

[Block 4206 [VERSE]]
དོན་དང་སེམས་ཅན་བདག་རྣམ༌[^2594]རིག །
སོ་སོར་སྣང་བ་རབ་སྐྱེས་པ། །
རྣམ་པར་ཤེས་པ་དེ་དོན་མེད། །
དེ་མེད་པས་ཀྱང་དེ་ཡང་མེད། །

[Block 4207 [VERSE]]
གཅིག་ནི་རྐྱེན་གྱི༌[^2595]རྣམ་པར་ཤེས། །
གཉིས་པ་ཉེ་བར་ལོངས་སྤྱོད་པ། །
སྤྱོད་དང་གཅོད་དང་སྐུལ་བྱེད་ནི། །
དེ་ལ་སེམས་ལས་འབྱུང་བ་ཡིན། །

[Block 4208]
ཞེས་འབྱུང་ངོ་། །སྤྱིའི་དོན་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་ལ་སོགས་པའི་འགྱོད་པ་སེལ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 4209]
གང་གི་ཕྱིར་མདོ་སྡེ་པ་ལ་སོགས་པ་རྣམས་ཀྱི་ཕྱོགས་ནི་ཕྱི་རོལ་གྱི་དོན་མེད་པ་དང་རྣམ་པར་རིག་པ་ཙམ་ཡོད༌[^2596]པའོ། །

[Block 4210]
གང་ཕུང་པོ་ལ་སོགས་པ་ཞེས་པ་ལ། ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་རྣམས་སོ། །

[Block 4211]
དེ་རྣམས་མེད་པ་ནི་གཅིག་དང་དུ་མ་དང་བྲལ་བའི་ཕྱིར་མེད་པའོ། །

[Block 4212]
དེ་བས་ན༌[^2597]ཕྱི་རོལ་ཏུ་གྱུར་པ་ཕུང་པོ་ལ་སོགས་པ་མེད་པས་རྣམ་པར་ཤེས་པ་ཙམ་འབའ་ཞིག་ཏུ་ཡོད་པ་ཞེས་རྣལ་འབྱོར་སྤྱོད་པ་པ་རྣམས་ཀྱི་ཕྱོགས་སོ། །

[Block 4213]
དེ་ཉིད་ཀྱི་ཕྱིར་བསྒོམ་པར་བྱ་བར་གྱུར་པ་ཕུང་པོ་ལ་སོགས་པ་མེད་པས་འབའ་ཞིག་དྲི་མ་མེད་པ་མཐའ་ཡས་པ་ནམ་མཁའ་དང་མཚུངས་པ། སེམས་ཙམ་གང་ཡིན་པ་ནི༌[^2598]ཞེས་པ་ནི་རྣམ་པར་རིག་པ་ཙམ་མོ། །

[Block 4214]
དེ་ནི་དངོས་པོ་མེད་དེ་ཞེས་པ་ལ། །མ་དག་པ་ཡིན་པས་གྲོལ་བ༌[^2599]ཐོབ་པར་མི་འགྱུར་རོ་ཞེས་བཤད་དོ། །

[Block 4215]
རྟག་ཏུ་མེད་པ་ཡིན་པའི་ཕྱིར། །ཞེས་པ་ནི། ཤེས་བྱ་མེད་པས་ཤེས་པ་རྣམས་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 4216]
ཇི་སྐད་དུ།

[Block 4217 [VERSE]]
ཤེས་བྱའི་སྔོན་དུ་ཤེས་པ་ན། །
ཅི་ལ་དམིགས་ཏེ་དེ་འབྱུང་འགྱུར། །
ཤེས་བྱ་འཇིག་ནས་ཤེས་པ་ན། །
ཅི་ལ་དམིགས་ཏེ་དེ་འབྱུང༌[^2600]འགྱུར། །

[Block 4218 [VERSE]]
ཤེས༌[^2601]དང་ཤེས་བྱ་ལྷན་ཅིག་ན། །
ཅི་ལ་དམིགས་ཏེ་དེ་འབྱུང་འགྱུར། །

[Block 4219]
ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 4220]
ཡང་ན་རྟག་ཏུ་མེད་པ་མ༌[^2602]ཡིན་པའི་ཕྱིར་རོ་ཞེས་པ་ནི། །རྟག་ཏུ་ནི་དུས་ཐམས་ཅད་དེ་དུས་གསུམ་ལ་ཡང་སེམས་ནི་མེད་དོ། །

[Block 4221]
གང་གི་ཕྱིར་འདས་པའི་སེམས་གང་ཡིན་པ་དེ་ནི་འཇིག་པའི་ཕྱིར༌[^2603]ཞེས་བྱ་བ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 4222]
མ་འོངས་པའི་སེམས་ཀྱང་མ་ཕྲད་པའི་ཕྱིར་རོ།[^2604] །

[Block 4223]
རྣམ་པར་ཤེས་པ་ཞེས་མ་གྲགས་སོ། །

[Block 4224]
ད་ལྟར་བྱུང་བ་ཡང་འདས་པ་དང་མ་འོངས་པའི་སྐད་ཅིག་མ་དང་ལྡན་པའི་ཕྱིར་སྔ་མ་བཞིན་ནོ་ཞེས་དུས་གསུམ་གྱི་རང་བཞིན་སེམས་མེད་དོ། །

[Block 4225 [VERSE]]
གང་འདས་པ་ནི་དེ་འཇིག་པ། །
མ་འོངས་པ་ནི་མ་ཐོབ་སྟེ། །
སྐད་ཅིག་གཉིས་ཀ་ལྡན་པའི་ཕྱིར། །
ད་ལྟར་བྱུང་བ་གང་ལ་གནས། །

[Block 4226]
ཞེས་འབྱུང་ངོ་། །དེ་བས་ན་རིགས་པ་འདིས། །སེམས་རྣམ་པར་དཔྱད་པ་རྣམ་པར་ཤེས་པ་གསུམ་གྱི་རང་བཞིན་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་འོད་གསལ་བར་བྱའོ། །

[Block 4227]
དེས་ནི་ཡེ་ཤེས་གསུམ་དཔྱོད་པའི་མཚན་ཉིད་སྦས་པའི་དོན་བསྟན་པ་ཡིན་ནོ། །

[Block 4228]
གང་ཀུན་རྫོབ་ཀྱི་བདེན་པའི་བདག་ཉིད་ཅན་ཞེས་པ་ལ། འོད་གསལ་བ་ལས་མྱུར་དུ་འམ༌[^2605]སྣང་བ་ཐོབ་པ་ལ་སོགས་པའི་རིམ་པས་བརྒྱ་བྱིན་གྱི་གཞུང༌[^2606]དང་འདྲ་བའི་ཡེ་ཤེས་ཀྱི་སྐུ་གང་སྤྲོས་པ་སྒྱུ་མ་ལྟ་བུའི་ལྷའི་སྐུ་བསྒོམ་པ་ནི་སྒྱུ་མའི་དཔེ་བཅུ་གཉིས་ཀྱིས་ཉེ་བར་མཚོན་པའོ། །

[Block 4229]
དེ་ཡང་མི་རིགས་ཏེ་ཞེས་པ་ནི་དེ་ཁོ་ན་ཉིད་ཀྱི་ངོ་བོ་མ་ཡིན་པས་སོ། །

[Block 4230]
འོད་གསལ་བར་རྣམ་པར་དག་པའི་ཕྱིར་རོ་ཞེས་པ་ནི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་བཞི་པས་དེ་ཡང་སྦྱང་བར༌[^2607]བྱ་བའི་ཕྱིར་རོ། །

[Block 4231]
དེ་ལྟར་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཙམ་གྱི་དངོས་པོ་ནི་ཞེས་པ་ལ་བདག་བྱིན་གྱིས་རློབ་པའི་རིམ་པས་ཐོབ་པར་བྱ་བ་ཡེ་ཤེས་ཀྱི་སྐུའི་མཚན་ཉིད་ལྷའི་སྐུའི་རྣམ་པའོ། །

[Block 4232]
དངོས་པོ་མ་ཡིན་ཏེ་ཞེས་པ་ནི། དོན་དམ་པ་མ་ཡིན་ནོ། །

[Block 4233]
དེ་གཉིས་པ་ལས་མ་འདས་པའི་ཕྱིར་རོ་ཞེས་པ་ནི་གཉིས་སུ་སྣང་བའི་ཕྱིར་རོ། །

[Block 4234]
དེར་ནི་སྒྱུ་མ་ལྟ་བུའི་ལྷའི་རྣམ་པ་དང་། སྒྱུ་མའི་དཔེ་དེ་གཉིས་སོ་སོར་སྣང་བ་ཡོད་པའོ། །

[Block 4235]
གང་དང་གང་དུ་གཉིས་སོ་སོར་སྣང་བ་ཡོད་པ་དེ་དང་དེ་རུ་འཁོར་བ་ཁོ་ན་ཡིན་ཏེ། གཟུང་བ་དང་འཛིན་པ་སོ་སོར་སྣང་བ་བཞིན་ནོ། །

[Block 4236]
དེའི་ཕྱིར་ན་དེ་ཡང་རྣམ་པར་དག་པར་བྱ་བར་རིགས་སོ། །

[Block 4237]
དེ་བས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་རིམ་པ་བཞིའི་འབྲས་བུ་ཟུང་དུ་འཇུག་པའི་རིམ་པའི་ཕན་ཡོན་ཙམ་བསྟན་ཏོ། །

[Block 4238]
བདེན་པ་གཉིས་ལྟ་བུར་བསྒོམ་པ་ནི་ཞེས་པ་ལ་ཀུན་རྫོབ་དང་དོན་དམ་པ་དབྱེར་མེད་པའི་ངོ་བོ་ཉིད་ཟུང་དུ་འཇུག་པའི་རིམ་པ་བསྒོམ་པའོ། །

[Block 4239]
དཀའ་བས༌[^2608]དམིགས་པ་ཡིན་པས་སོ། །ཞེས་པ་ནི་སྔོན་བསགས་པའི་དགེ་བའི་སྟོབས་དང་དགེ་བའི་བཤེས་གཉེན་དང་ཕྲད་པ་དང་རྗེས་སུ་མཐུན་པའི་གནས་སུ་སྐྱེ་བ་དང་བྱང་ཆུབ་སེམས་དཔའི་རིགས་དང་འབྲེལ་པ་དང་། སངས་རྒྱས་ཀྱིས་བྱིན་གྱིས༌[^2609]བརླབས་པས་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4240]
དེས་ནི་ཀུན་རྫོབ་བདེན་པ་ཡང་དག་པར་རྟོགས་པའི་མཚན་ཉིད་ཅན་སྦས་པའི་དོན་བསྟན་ཏོ། །
--- END BLOCKS ---
