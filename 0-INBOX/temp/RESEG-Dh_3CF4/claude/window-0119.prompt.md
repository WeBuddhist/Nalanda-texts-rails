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
[Block 4166]
བསོད་ནམས་ཀྱི་གཞི་ལས་ཐོབ་ཅིང་འབར་བ་གང་ཡིན་པ་དེ་ནི་བསོད་ནམས་ཀྱི་གཞི་ལས་འབར་བའོ། །

[Block 4167]
བསོད་ནམས་ཞེས་སྨོས་པས་ནི་གང་སྔར་བསྟན་པའི་བསོད་ནམས་དང་ལྡན་པའི་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་ཏོ། །

[Block 4168]
ནན་ཏན་སྒྲུབ་པའི་བྱིན་གྱིས་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་བདག་གི་སྒྲུབ་པ་སྟེ། ནན་ཏན་ཆེ་བའི་ཡོན་ཏན་ཞེས་བྱ་བ་དང་། གཞན་གྱི་སྒྲུབ་པ་སྟེ་འཇིག་རྟེན་གྱི་ཚུལ་ལ་མཁས་པ་ཞེས་བྱ་བ་དེ་གཉི་ག་ནི་ནན་ཏན༌[^2681]སྒྲུབ་པའི་བྱིན་གྱིས་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4169]
ཡང་ན་ཡོན་ཏན་ཞེས་སྨོས་པས་ནི་འཇིག་རྟེན་གྱི་སྤྱོད་ཡུལ་ལ་མཁས་པ་ཞེས་བྱ་བ་དེ་གཟུང༌[^2682]ངོ་། །ཡོན་ཏན་སྒྲུབ་པའི་བྱིན་གྱིས་ཞེས་བྱ་བ༌[^2683]ནི་སྔར་བསྟན་པའི་ནན་ཏན་ཆེ་བ་ཡིན་པར་བསྟན༌[^2684]ཏོ། །

[Block 4170]
དགྲ་ཡང་རང་གི་གྲགས་པ་བསྲུང་བའི༌[^2685]ཕྱིར། །ཞེས་བྱ་བ་ནི་ཡོན་ཏན་དང་ལྡན་པ་ལ་བསྙེན་བཀུར་བྱེད་པས་སོ། །

[Block 4171]
ཡོན་ཏན་ཅན་ལ་སྡང་བ་དེ། །ཞེས་པ་ནི་རང་གི་གྲགས་པ་འཇིག་པར་བྱེད་པའི་ཕྱིར། ཡོན་ཏན་ཅན་ལ་བསྙེན་བཀུར་བྱེད། ། ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4172]
རྒྱ་ཆེ་བ་དང་མཐུ་ནི་རྒྱ་ཆེ་བ་དང༌[^2686]མཐུའོ། །

[Block 4173]
ཡོན་ཏན་རྣམས་ཀྱི་མཐུ་ཆེ་བ་ཐོས་པ༌[^2687]ནི་ཡོན་ཏན་གྱི་མཐུ་ཆེ་བ་དེས་ཐོས་པའོ། །

[Block 4174]
ཡོན་ཏན་འདི་རྣམས་ཇི་སྲིད་དུ་ལྡན་པ་དང་། ཇི་ལྟར་ལྡན་པ་བསྟན་ཏེ། བསུ་བ་ལ་སོགས་པའི་བཀུར་སྟི་ཆེར་བྱས་ཏེ། ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པས་ནི་མངོན་པར་སྨྲ་བ་ལ་སོགས་པ་གཟུང་ངོ་། །རིམ་གྲོ་ནི་མཉེས་པའི༌[^2688]ལས་ལ་སོགས་པའོ། །

[Block 4175]
བཀུར་སྟི་ནི་ཉེ་བར་འགྲོ་བ་ལ་སོགས་པའོ། །

[Block 4176]
ཉེ་བར་ལོངས་སྤྱོད་པར་བྱ་བ་ཡིན་པས་ན་ལོངས་སྤྱོད་དོ། །

[Block 4177]
ལོངས་སྤྱོད་ཉིད་ཡོན་ཏན་ཡིན་པས་ན་ལོངས་སྤྱོད་ཡོན་ཏན་ནོ། །

[Block 4178]
ཡོན་ཏན་ཅན་ལ་དགའ་བ་ཉིད་ཀྱིས་ཕན་འདོགས་པར་བྱེད་པའི་རྒྱུ་རབ་ཏུ་ནུས་པ་སྟེ་བསམ་པའི་ཆོ་ག་བསྟན་ཏོ། །

[Block 4179]
གུས་པ་མེད་པ་གང་ཡིན་པ་དེ་དག་ནི་གུས་པ་མེད་པ་རྣམས་སོ། །གང་ལ་ཞེ་ན། ཆོས་དང་ཆོས་སྨྲ་བ་རྣམས་ལའོ། །

[Block 4180]
ཆོས་ལ་གུས་པ་མེད་པ་ལ༌[^2689]ཅིའི་ཕྱིར་ཆོས་སྟོན་པར་བྱེད་ཅེ་ན། ཆོས་ལ་དགའ་བའི་ཕྱིར་རོ། །

[Block 4181]
ཆོས་སྟོན་པ་ལ་མི་གུས་པ་ལ་ཡང་ཅིའི་ཕྱིར་བསྟན་པར་འདོད་ཅེ་ན། གཞན་ལ་སྙིང་བརྩེ་བའི་ཕྱིར་རོ། །

[Block 4182 [VERSE]]
ཕན་པར་འདོད་ཅིང་ཡོན་ཏན་དགའ་བ་ཡིན། །
སྐྱེ་བོ་གནོད༌[^2690]གཙང་འདྲ་ལ་སྨོས་ཅི་དགོས། །

[Block 4183]
ཞེས་བྱ་བ༌[^2691]སྨོས་ཏེ། འདི་གསུམ་གྱིས་ནི་ཕྱི་རོལ་གྱི་སྣོད་དང་འདྲ་བར་ཆོས་ཉན་པ་རྣམས་ཀྱི་ཉེས་པ་གསུམ་མེད་པར་སྟོན་ཏེ། གང་གི་ཕྱིར་སྣོད་འདི་གསུམ་ལ་ཆར་བབ་ཀྱང་དོན་མེད་པ་ཉིད་དེ། བསིལ་བ༌[^2692]དང་ཕན་པ་ཡིན་ཡང་ཆུ་མི་འཇུག་པ་དང་། གང་དུ་ཆུ༌[^2693]འཇུག་ཀྱང་མི་གཙང་བས་མ་རུང་བར་འགྱུར་བ་དང་། གང་དུ་ཆུ་ཞུགས་ཀྱང་སྣོད་རྡོལ་བས༌[^2694]མི་གནས་པ་སྟེ། དེ་ལྟར་ཉན་པའི༌[^2695]སྐྱེ་བོ་རྣམ་པ་གསུམ་པ༌[^2696]ལ་ནི་ཆོས་བསྟན་ཀྱང་དོན་མེད་ཅིང་ཆུད་ཟོས་པ་ཉིད་ཡིན་ཏེ། གང་དུ་ཐོས་པ་བྱ་བ་གཡེང་བ་དང་། རྨུགས་པ་རྣམ་པ་གཉིས་ཀྱིས་མི་འཇུག་པ་དང་། གང་དུ་འཇུག་ཏུ་ཟིན་ཀྱང་ཚུལ་བཞིན་དུ་ཡིད་ལ་མི་བྱེད་པས་མ་རུང་བར་འགྱུར་བ་དང་། གང་དུ་ཡང་དྲན་པ་མེད་པས་མི་གནས་པའོ། །

[Block 4184]
གང་ཡོན་ཏན་འདོད་པའི་སྐྱེ་བོ་ཞེས་སྨོས་ཏེ། འདིས་ནི་གང་དུ་ཐོས་པ་མི་འཇུག་སྟེ། གཡེང་བ་དང་། རྨུགས་པ་རྣམ་པ་གཉིས་ཀྱི་སྐྱོན་མེད་པར་སྟོན་ཏོ། །

[Block 4185]
ཡོན་ཏན་དགའ་བ་ཞེས་བྱ་བ་ལ། ཡོན་ཏན་ལ་དགའ་ཞིང་གཟེངས་བསྟོད་པ་དེ་ནི་ཡོན་ཏན་ལ༌[^2697]དགའ་ཞིང་གཟེངས་བསྟོད་པའོ། །

[Block 4186]
གང་ཟག་གང་གིས་ཡོན་ཏན་ལ་དགའ་བ་དེ་ནི་གཡེང་བ་མེད་པ་ཡིན་ནོ། །

[Block 4187]
ཆོས་ཀྱི་ཡོན་ཏན་ལ་དགའ་བ་དེ་ནི་གཉིད་དང་རྨུགས་པ་མེད་པ་ཡིན་ནོ། །

[Block 4188]
མཁས་པ་རྣམས་ཀྱི་གོ་འཕང་ཡིན་པས་ན་མཁས་པའི་ཐབས་ཏེ། མཁས་པའི་ཐབས་ཐོབ་པ་དེ་དག་དེས་སོ། །

[Block 4189]
ཕྲག་དོག་གི་སེམས་བསྐྱེད་པ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་ཕུན་སུམ་ཚོགས་པ་ལ་ཕྲག་དོག་གི༌[^2698]སེམས་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 4190]
ཡོན་ཏན་གྱི་ཁྱད་པར་ཡིན་པས་ན་ཡོན་ཏན་ཁྱད་པར་རོ། །

[Block 4191]
ཡང་ན་ཡོན་ཏན་ཉིད་ཁྱད་པར་ཡིན་པས་ཡོན་ཏན་ཁྱད་པར་རོ། །

[Block 4192]
བདག་ཉིད་ཀྱི་ཡོན་ཏན་གྱི་ཁྱད་པར་ཡིན་པས་རང་གི་ཡོན་ཏན་ཁྱད་པར་རོ། །

[Block 4193]
ཡང་ན་བདག་གི་ཡོན་ཏན་ཉིད་ཁྱད་པར་ཡིན་པས་རང་གི་ཡོན་ཏན་ཁྱད་པར་རོ། །

[Block 4194]
དེ་དང་ལྡན་པ་ཡིན་པས་རང་གི་ཡོན་ཏན་ཁྱད་པར་ཅན་ནོ། །

[Block 4195]
དེས་འགྲོ་བ་མགུ་བར་ནུས་པའི་མཐུ་སྦྱོར་བ་གང་ཡིན་པ་དེ་ནི་འགྲོ་བ་མགུ་བར་ནུས་པའི་མཐུ་ཅན་ནོ། །

[Block 4196]
ཡོན་ཏན་བཅོས་མས་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་བཅོས་མ་ཉིད་ཀྱིས་ཏེ། དེས་བཀུར་སྟི་ཐོབ་པའོ། །

[Block 4197]
དེ་ལ་ཤིན་ཏུ་འབར་བ་ཉིད་ཡིན་ཏེ་འཕེལ་བ་ཉིད་དོ། །

[Block 4198]
ཕྲག་དོག་གི་མེ་ཞེས་བྱ་བ་ལ། ཕྲག་དོག་ཉིད་མེ་ཡིན་པས་ཕྲག་དོག་གི༌[^2699]མེའོ། །

[Block 4199]
ཕྲག་དོག་གི་མེ་དེས་ནི་མེ༌[^2700]བཞིན་དུ་རང་གི་གནས་སྲེག་པའི་ཕྱིར་རོ། །

[Block 4200]
རྒྱལ་པོ་ཆོས་ལ་བརྟེན་པ་ཞེས་བྱ་བ་ནི་རྒྱལ་པོའི་ཆོས་དང་མི་མཐུན་པའི་ཕྱིར་ཆོས་ལ་བརྟེན་པ་དེའོ། །

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
--- END BLOCKS ---
