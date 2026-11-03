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
ཡོན་ཏན་ལ་དགྱེས་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་གཏམ་གྱིས་སོ། །

[Block 4202]
ཆོས་ལ་མངོན་འཚལ་ནས་ཞེས་བྱ་བ་ནི་ཆོས་ལ་མངོན་པར་ཕྱོགས་པ༌[^2701]སྟེ་རྗེས་སུ་དགའ་ཞིང་འདོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4203]
བརླག་པར་བགྱི་བའི་སླད་དུ་གཡོ་དང་བཅས་པའི་ཚིག་འཇམ་པོར་སྨྲ་ཞིང་སྤྱོད་པ་གང་ཡིན་པ་དེ་ནི་བརླག་པར་བགྱི་བའི་སླད་དུ་གཡོ་དང་བཅས་པའི་ཚིག་འཇམ་པོར་སྨྲ་ཞིང་སྤྱོད་པའོ། །

[Block 4204]
བརླག་པ་ཞེས་བྱ་བ་ནི་དཔལ་གང་ཡིན་པ་དེ་ཉམས་པར་བྱེད་པ་སྟེ། ཆོས་ནན་ཏན་དུ་བྱེད་ཀྱང་རྒྱལ་པོ་ནི་རླག་པར༌[^2702]བྱེད་པ་ཉིད་ཡིན་ཏེ། རྒྱལ་པོའི་ཆོས་དང་འགལ་བའི་ཕྱིར་བརླག་པ་ཞེས་བརྗོད་དོ། །

[Block 4205]
ཉམས༌[^2703]དྲོད་ནི་སྤྱོད་པ་ལ་འཇུག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4206]
དེའི་རྟེན་དུ་གྱུར་པས་ན་ཉམས༌[^2704]དྲོད་འཛིན་པ་ལགས་ཏེ། ཞེས་བྱ་བའོ། །

[Block 4207]
བྱ་མ་རྟ་ཞེས་བྱ་བ་ནི་ཉན་རྣ་བའོ། །

[Block 4208]
བྱ་མ་རྟ་ཉིད་བཏང་བ་ཡིན་པས་བྱ་མ་རྟ་བཏང་བའོ། །

[Block 4209]
ཐུགས་རྗེ་ཆེ་བ་ཞེས་བྱ་བ་ལ་ཐུགས་རྗེ་ནི་གཞན་སྡུག་བསྔལ་དང་བྲལ་བའི་དོན་དུ་གཉེར་བའོ། །

[Block 4210]
ངོ་ཚ་མཁྱེན་པ་ཉིད་ཀྱི༌[^2705]འཇམ་དེས་ཅན་དུ་གྱུར་ཏེ། དེས་ལས་ལ་སོགས་པ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 4211]
སྲིད་དང་འདོད་པ་དང་མི་མཐུན་པའི་ཚུལ་གང་ལ་ཡོད་པ་དེ་ནི་སྲིད་པ་དང་འདོད་པ་དང་མི་མཐུན་པའོ། །

[Block 4212]
དེ་ཡང་སྙིང་རྗེ་དང་ལྡན་པར་བགྱི་བའི་ཆེད་དུ་བགྱིད་པ༌[^2706]སྟེ། དེ་གཞན་གྱི་བྲན་བཞིན་དུ་བྱེད་པས་དོན་དུ་སྒྲུབ་ཅིང་གང་གཞན་གྱིས་བརྙས་པར་འོས་པ་དེ་བྱེད་པ་ནི་དོན་སྒྲུབ་པ་ཉིད་དུ༌[^2707]ཡིན་ནོ། །

[Block 4213 [VERSE]]
ཆེད་ཆེར་བགྱིས་ནས་ཐབས་ཀྱིས་བག་འབེབས་སོ། །
ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་བ་དང་།
ཡིད་མི་བདེ་བ་མེད་པའི་ཐབས་ཀྱིས་སོ། །

[Block 4214]
བཤེས་ཤིང་འདྲུལ་ལ་ཞེས་བྱ་བ་ནི་མཛའ་བར་འབྲེལ་པའོ། །

[Block 4215]
ཡིད་མི་ཆེས་པ་དང་། བརྩེ་བ་ཆུང་བ་གཉིས་ཀྱིས༌[^2708]སེམས་སྔོན་དང་མི་འདྲ་བར༌[^2709]གྱུར་པ་གང་ཡིན་པ་དེ་ནི་ཡིད་མི་ཆེས་པར་གྱུར་ཏེ། བྱམས་པ་དང་བཀུར་སྟི་ཆུང་ཞེས༌[^2710]སེམས་སྔོན་དང་མི་འདྲ་བར་གྱུར་པའོ། །

[Block 4216]
དབྱེན་གྱི་རྡོ་རྗེ་ཉིད་སེར་བ་ཡིན་ཏེ། དེ་ལྟུང་བ་ནི་དབྱེན་གྱི་སེར་བ་རྡོ་རྗེ་འབབ་པའོ། །

[Block 4217]
མཛའ་བ་བརྟན༌[^2711]པ་ཞེས་བྱ་བ་ནི་བརྟན་པར་གྱུར་པའི་མཛའ་བ་དེ་ལ་ཕན་པ་མི་འདོད་པས་སྨྲས་པའི་དབྱེན་གྱི་ཚིག་ཡིན་ཏེ།

[Block 4218 [VERSE]]
སེམས་ཀྱི་ལོངས་སྤྱོད་མེད་པའི་ཕྱིར་རོ། །
ཉམས་ཤིང་ཞིག་པར་མི་འགྱུར་སུ་ཞིག་ཡོད། །

[Block 4219]
ཅེས་བྱ་བ་ནི་གཅིག་ཀྱང་མེད་པས་ཐམས་ཅད་ཀྱང་ཉམས་ཤིང་ཞིག་པར་འགྱུར་བ་ཉིད་དོ། །

[Block 4220]
ཡང་ན་མཛའ་བ་བརྟན་པ་ནི་ཡིད་ཆེས་པའོ། །

[Block 4221]
ཉམས་ཤིང་ཞིག་པ་ནི་སྔོན་ཇི་ལྟ་བ་བཞིན་དུ་མཛའ་བ་བརྟན་པའམ༌[^2712]ཡིད་ཆེས་པ་མེད་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 4222]
བཀུར་སྟི་ཆུང་བར་འགྱུར་བ༌[^2713]ཞེས་བྱ་བ་ནི་བརྩེ་བ་དང་གུས་པ་ཆུང་བའི་ཕྱིར་རོ། །

[Block 4223]
བྱ་བ་མང་པོ་ལ་བྲེལ་བ་གང་ཡིན་པ་དེ་ནི་བྱ་བ་མང་པོས་བྲེལ་བའོ། །

[Block 4224]
དེ་ལྟར་གྱུར་པ་ཡིད་ལའང་མི་བྱེད་ན། །ཞེས་བྱ་བ་ནི་རིམ་གྲོ་མི་བྱེད་པར་གྱུར་པའོ། །

[Block 4225]
དེའི་དྲུང་ན་གནས་པ་ནི་དྲུང་ན་འཁོད་པའོ། །

[Block 4226]
དེའི་དྲུང་ན་འཁོད་ཅིང་འཁོར་བའི་ཚུལ་གང་ལ་ཡོད་པ་དེ་ནི་དེའི་འཁོར་ན་འཁོད་པ་རྣམས་སོ། །

[Block 4227]
གུས་པ་དང་རིམ་གྲོ་ནི་གུས་པ་དང་རིམ་གྲོའོ། །

[Block 4228]
དེ་གཉིས་ཀྱི༌[^2714]ལྷོད་པར་གྱུར་པ་ནི་གཡེལ༌[^2715]བའོ། །

[Block 4229]
དེའི་ཕྱིར་བཤད་པ། སྟོན་པ་དང་བྱེད་པ་གཉིས་ཐ་དད་དོ་ཞེས་བྱ་བ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4230]
དོགས་པ་འབྱུང་བའི་གནས་ཡིན་པས་དོགས་པ་འབྱུང་བའི་གཞིའོ། །

[Block 4231]
ནོངས་པར་དོགས་པ་འབྱུང་བའི་གཞི་ཞེས་བྱ་བ་ནི་ཉེས་པ༌[^2716]འབྱུང་བའི་གཞི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4232]
བག་མེད་པ་ཉིད་ཉེས་པ་ཡིན་པས་བག་མེད་ནོངས་པའོ། །

[Block 4233]
ཡང་ན་བག་མེད་པས་ནོངས་པའོ། །

[Block 4234]
འཕྲལ་ལ་འདི་ལྟར་མི་མཆི་བ་ཞེས་བྱ་བ་ནི༌[^2717]རྒྱུ་དང་བཅས་པ་ཉིད་དོ། །

[Block 4235]
བཀུར་སྟི་ཆུང་ཞིང་ཁྲོས་པའི་ཡིད་གང་ཡིན་པ་དེ་ནི་བཀུར་སྟི་ཆུང་བའི༌[^2718]སེམས་ཏེ་དེ་མེད་པའོ། །

[Block 4236]
འོ་ན་རྒྱུ་དེ་གང་ཡིན་ཞེ་ན། སྨྲས་པ། ཁྱོད་ནི་ཆོས་ཀྱི་སྣོད་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 4237]
དེ་ནས་རྒྱལ་པོ་དེའི་ཁྱི་གནང་ཆེན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་ནི་མི་མ་ཡིན་པ་ཁྱི་ཡང་ཟུག༌[^2719]པའི་ཚུལ་གྱིས་རྒྱུ་ཡོད་པ་ཡིན་ཏེ། དབྱེན་གྱི་ཚུལ་ངེས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4238]
བྲི་བར་གྱུར་པ་ནི་ཡལ་བར་བོར་བའོ། །

[Block 4239]
གསུམ་པོ་འདི་ནི་བདག་གི་འགྲོ་བའི་རྒྱུ་ཡིན་ཏེ། གནས་ལ་ལྷག་པར་ཞེན་པ་དང་། གཞན་དུ་འགྲོ་བའི་གནས་མ་མཐོང་བ་དང་། བསྙེན་བཀུར་ཆུང་བར་ཡོངས་སུ་ཤེས་པའོ། །

[Block 4240]
ཕྱིས༌[^2720]བསྐྲད་པར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་སླད་ཀྱིས་བསྐྲད་པར་འགྱུར་བ་སྟེ། རྗེས་སུ་རྒྱལ་པོས་བསྐྲད་པ་དང་། སྤྱུགས་པར་འགྱུར་ཞེས་པའོ། །
--- END BLOCKS ---
