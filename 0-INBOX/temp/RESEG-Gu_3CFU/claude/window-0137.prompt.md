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
[Block 4796]
དེ་ལྟ་བས་ན་འདིར་སྨོས་པ་ནི་དཔེ་ཙམ་དུ་ཟད་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་འདི་རྣམ་པར་གཞག་པ་འདི་རྟོགས་པར་བྱའོ། །གང་ཞེ་ན། དེའི་ཕྱིར་བཟའ་བར་བྱ་བ་རུང་བ་མ་ཡིན་པ་ཉིན་མཚན་འདས་པ་ནི་འདིར་ཟོས་པ་དང་འདྲ་བར་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཟའ་བར་བྱ་བ་ཟོས་པ་ལྟར་ཞེས་བྱ་བ་འདིར་རྣམ་པར་གཞག་པའོ། །

[Block 4797]
རུང་བ་མ་ཡིན་པ་ཉིན་མཚན་འདའ་བར་བྱེད་ན་ལྟུང་བ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྐྱ་རེངས༌[^3283]

[Block 4798]
བརྒྱད་པ་ཤར་ནའོ་ཞེས་བྱ་བ་ནི་འདིར་དོན་ཏོ། །

[Block 4799]
འདིར་ཉིན་ཞག་ལ་ཉིན་མཚན་ཞེས་བྱ་བ་བརྗོད་པ་ཡིན་ནོ། །

[Block 4800]
ཉིན་མཚན་འདའ་བར་བྱེད་པ་ནི་ནང་དུ་ཞག་ལོན་པ་དང་ནང་དུ་བཙོས་པ་ལ་སོགས་པ་རུང་བའི་བཟའ་བ་ཇི་ལྟ་བུ་ཐོས་པ་ལ་ཁ་ན་མ་ཐོ་བ་དེ་ལྟ་བུ་འདིར་འཆང་བ་ལ་རིགས་པ་ཡིན་གྱི་ལྷག་པ་ནི་མ་ཡིན་ནོ། །

[Block 4801]
གང་གི་ཕྱིར་མི་རིགས་པར་གྱུར་པ་ཟ་བར་བྱེད་པ་ལ་ནང་དུ་ཞག་ལོན་པ་དང་ནང་དུ་བཙོས་པ་ལ་སོགས་པ་རྣམས་ལ་ཉེས་བྱས་ཏེ་འཆང་བ་ལ་ནི་སྤང་བའོ་ཞེས་གསུངས་སོ། །

[Block 4802]
དེ་བས་ན་འདིར་ཟོས་པ་ལྟར་ཞེས་བྱ་བ་བསྟེན༌[^3284]པའོ། །

[Block 4803]
དེ་དོན་གང་གི་ཕྱིར་བརྟགས་པ་དེའི་ཕྱིར་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་བཟའ་བའི་དོན་ལས་དོན་གཞན་གང་ཞིག་ལ་ཞག་བདུན་པ་བརྟག་པ་དོན་དེའི་ཕྱིར་འཆང་བ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 4804]
དོན་མ་བཅད་པར་འཆང་བ་བཟའ་བའི་དོན་ཉིད་ལ་ཁོངས་སུ་གཏོགས་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 4805]
དེ་བས་ན་དེར་ཉེས་པ་མེད་པ་འམ་ན་སྨད་པ་མེད༌[^3285]པའོ། །

[Block 4806]
བག་མེད་པ་དང་དྲན་པ་བརྗེད༌[^3286]ངས་པས་འཆང་བ་ནི་འཆང་བ་མ་ཡིན་པའོ། །

[Block 4807]
དེ་བས་ན་འདིར་ཡང་ཡིད་ཀྱིས་མ་བསྡུས་པ་ཉིད་ལ་རུང་བ་མ་ཡིན་པའི་དོན་ལས་འདིའི་སྒོ་ནས་འདའ་བར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 4808]
རུང་བ་མ་ཡིན་པའི་དོན་ལས་བསྡུས་ཏེ། དངོས་པོ་ལ་མ་བརྟེན་པར་རུང་བ་མ་ཡིན་པའི་དོན་ལ་འདི་ཙམ་ཉིད་དུ་དོན་མེད་པར་ཉེས་བྱས་སུ་རྣམ་པར་གནས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4809]
སྣར་བླུགས་པ་དང་བསྐུ་མཉེ་བྱས་པ་དག་ནི་གསོག་འཇོག་བྱས་ཀྱང་རུང་ངོ་ཞེས་བྱ་བ་ནི་ཞག་བདུན་པའི་དབང་དུ་བྱེད་པ་ན་མཚུངས་པ་ཉིད་ཀྱི་ཕྱིར་འདི་རྟོགས་པའོ། །

[Block 4810]
ཞག་བདུན་པའི་སྤང་བའོ། །

[Block 4811]
སྤང་བ་རྣམས་རྫོགས་སོ།། །།

[Block 4812 [HEADING]]
## དགེ་སློང་གི་ལྟུང་བྱེད་འབའ་ཞིག་ཏུ་གྱུར་པ་རྣམས། ^8-0

[Block 4813]
དགེ་འདུན་འདུས་པ་ལ་ཤེས་བཞིན་དུ་ཆོས་མ་ཡིན་པ་ཆོས་སུ་དང་། ཆོས་ཆོས་མ་ཡིན་པར་བསྟན་པ་ནི་ཉེས་པ་སྦོམ་པོའོ་ཞེས་བྱ་བ་ལ། ཤེས་བཞིན་དུ་ཞེས་བྱ་བ་ནི་ཆོས་དང་ཆོས་མ་ཡིན་པ་ཉིད་དོ། །

[Block 4814]
དགེ་འདུན་འདུས་པ་ལ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་དབྱེ་བའི་ཕྱིར་འགྲོ་བ་ལ་དེའི་སྦོམ་པོའི་ལྟུང་བ་བསྐྱེད་པའོ། །

[Block 4815]
དེ་བས་ན་གཞན་དུ་ནི་འདི་མེད་པའོ། །

[Block 4816]
གསོ་སྦྱོང་ལ་ཅི་འདི་ལ་ཁྱེད་ཡོངས་སུ་དག་གམ་ཞེས་ལན་གསུམ་གྱི་བར་དུ་དྲིས་པ་ལས་མ་དག་པར་ཤེས་བཞིན་དུ་ཅང་མི་སྨྲ་བས་འདའ་བར་བྱེད་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་འདིར་ཚིག་ལ་ནི་ཡན་ལག་ཉིད་ཀྱི་ཕྱིར་ན་འདིར་ནི་ན་སྨད་པ་ཉིད་དོ། །

[Block 4817]
ཅང་མི་སྨྲ་བས༌[^3287]འདའ་བར་བྱེད་པ་འདི་ནི་དཔེ་ཡིན་ཏེ། ཚིག་ལས་གཞན་པ་ཐམས་ཅད་ལ་འདིས་གོ་བར་བྱེད་པ་ལ་འཕངས་པར་རིག་པར་བྱའོ། །གང་དུ་བརྫུན་དུ་སྨྲ་བའི་ལྟུང་བྱེད་ཅེ་ན། དེའི་ཕྱིར་དེ་གཉིས་དང༌[^3288]ཕམ་པར་འགྱུར་བ་དང་དགེ་འདུན་ལྷག་མར་གྱུར་པ་གཉིས་ལས་གཞན་པའི་བརྫུན་དུ་སྨྲ་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདུ་ཤེས་རྣམ་པར་བཞག་ནས་ཞེས་བྱ་བ་ནི་འདིར་ཕམ་པར་རྒྱས་པར་བཤད་པའི་རྗེས་སུ་འབྲངས་ནས་རྟོགས་པར་བྱའོ། །

[Block 4818]
དེ་གཉིས་དང་ཞེས་བྱ་བ་ནི་བསྟན་མ་ཐག་པའི་ཉེས་པ་སྦོམ་པོར་འགྱུར་བ་དང་། ཉེས་བྱས་སུ་འགྱུར་བའི་བརྫུན་དུ་སྨྲ་བ་གཉིས་སོ། །

[Block 4819]
བརྫུན་དུ་སྨྲ་བ་རྣམ་པ་བཞི་པོ་དེ་དག་ལས་གཞན་པའི་ལྟུང་བ་འདིར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4820]
སྨྲ་བར༌[^3289]འདོད་པ་ཉིད་ལ་འདུ་ཤེས་རྙེད་པ་ལ་བརྫུན་དུ་སྨྲ་བ་ཞེས་བྱ་བ་འདི་ཐེ་ཚོམ་མེད་པར་སྨྲ་བར་གྱུར་པ་ཉིད་ལ་འདུ་ཤེས་ཐོབ་པ་ལ་བརྫུན་དུ་སྨྲ་བ་ཡོད་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་གང་ཞིག་ལ་དོགས་པར་གྱུར་ན། དེ་བཟློག་པའི་དོན་དུ་བརྗོད་པར་བྱ་སྟེ། སྨྲ་བའི་ཚེ་ཉིད་ན་ཡང་འདུ་ཤེས་བྱུང་ན་དེ་ཀུན་ནས་སློང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། འདུ་ཤེས་བྱུང་ན་ཞེས་བྱ་བ་ནི་གཞན་དུ་སྨྲ་བར་གྱུར་པ་ལ་ཞེས་བྱ་བའི་དོན་གྱིས་ཤེས་པར་བྱའོ། །

[Block 4821]
དེ་ཞེས་བྱ་བ་ནི་བརྫུན་དུ་སྨྲ་བའོ། །

[Block 4822]
ཡང་ཞེས་བྱ་བའི་སྒྲ་ནི་སྨྲ་བར་འདོད་པ་ཉིད་ལ་ཡང་ངོ་། །འདིར་གཞུང་ནི་བརྫུན་དུ་སྨྲ་བ་རྣམ་པ་གཉིས་པོ་གང་ཞེ་ན། ཤེས་བཞིན་དུ་བརྫུན་གྱི་ཚིག་སྨྲ་བ་ནི་འདི་སྙམ་དུ་བརྫུན་གྱི་ཚིག་སྨྲའོ་སྙམ་པ་དང་། སྨྲས་པའི་འོག་ཏུ་འདི་སྙམ་དུ་བདག་གིས་བརྫུན་གྱི་ཚིག་སྨྲས་སོ་སྙམ་པ་སྟེ། དེ་བས་ན་འདིར་བརྫུན་དུ་སྨྲ་བ་གཅིག་པུ་ཉིད་ལ་རྣམ་པ་གཉིས་ཡིན་ཏེ། རྣམ་པ་གཉིས་འདི་ལ་ཡོད་པའི་ཕྱིར་རྣམ་པ་གཉིས་དང་ལྡན་པ་ཉིད་ཀྱིས་བརྗོད་པའོ། །

[Block 4823]
གཅིག་པུ་གཅིག་གིས་ནི་མ་ཡིན་ནོ། །

[Block 4824]
དེ་བས་ན་རྣམ་པ་གཉིས་དང་ལྡན་པའི་བརྫུན་དུ་སྨྲ་བ་ཉིད་བསྟན་ཏེ། དེ་ལྟར་ཡང་རྣམ་པ་གཅིག་པ་འབའ་ཞིག་གིས་བརྫུན་དུ་སྨྲ་བ་ནི་ཡོད་པ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 4825]
ངེས་པར་སྨྲ་བར་གྱུར་པ་ཉིད་ཀྱི་འདུ་ཤེས་ཅན་གྱི་སྨྲ་བ་ཉིད་ལ་ཡང་འདི་བསྒྲུབ་པ༌[^3290]ཞེས་བྱ་བ་འདིའི་ཚིག་སྟེ། སྨྲ་བ་ཉིད་ཀྱི་འདུ་ཤེས་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4826]
འདུ་ཤེས་ལ་སྨྲ་བར་གྱུར་པ་ཉིད་ལ་ཡང་མ་གྲུབ་པ་ཞེས་བྱའོ། །

[Block 4827]
འདུ་ཤེས་སྔ་མ་ལ་ནི་ཕྱི་མ་གནས་པའི་ངོ་བོ་སྟེ། ཕྱི་མ་ལ་ནི་སྔ་མས་མ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 4828]
མནའ་དོར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཕྲེན་ཚེགས་རྣམས་ལས་བཏུས་པ་ཡིན་ཏེ། ཐམས་ཅད་བདག་ལ་བདེན་པ་ལ་འཇུག་པ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་འདི་ལ་འདི་བསྟན་པ་སྟེ། གང་ཞིག་མནའ་མེད་པའོ། །

[Block 4829]
དེ་བས་ན་བརྫུན་དུ་སྨྲ་བའི་ཕྱོགས་ཉིད་ཀྱི་ཕྱིར་འདི་ལ་འདིར་སྤོང་བའོ། །

[Block 4830]
དེ་ལྟར་ཡང་དགེ་སློང་རྣམས་ནི་བདེན་པར་སྨྲ་བར་འདོད་པ་ཡིན་ཏེ། རབ་ཏུ་བྱུང་བ་ཉིད་ལ་ཞེས་བྱ་བར་བརྗོད་ནས་དེ་བས་ན་དགེ་སློང་གིས་མནའ་དོར་བར་མི་བྱ་བའི་ཚིག་འདིའོ། །

[Block 4831]
བརྫུན་དུ་སྨྲ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 4832]
རུང་བ་མ་ཡིན་པར་བསམ་པས༌[^3291]གང་ཡང་རུང་བའི་སྐྱོན་ནས་སྨྲ་བར་འདོད་ནས་སྐྱོན་ནས་སྨྲ་བའི་ལྟུང་བྱེད་ཅེས་བྱ་བ་འཆད་པར་འགྱུར་རོ། །

[Block 4833]
དེ་ལ་ཅི་ཞིག་བསྙེན་པར་མ་རྫོགས་པ་ལ་ཡང་རུང་བ་མ་ཡིན་པར་བསམ་པ་བརྗོད་པ་ཡང་འདི་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་གིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་དགེ་སློང་ནི་ཡུལ་དུ་རྟོགས་པར་བྱ་སྟེ། དགེ་སློང་གི་ཡུལ་བརྗོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4834]
འོག་མ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཕྲ་མ་བྱེད་པའི་ལྟུང་བྱེད་ལ་ཡུལ་དགེ་སློང་ཉིད་དུ་རྟོགས་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4835]
སྨྲས་ན་ཞེས་བྱ་བ་ནི་བསླབ་པའི་གཞི་གཉིས་ཀ་ཡང་དགེ་སློང་གི་ཡུལ་ཁོ་ན་ལ༌[^3292]རིག་པར་བྱ་སྟེ། དགེ་སློང་ལ་བརྗོད་པ་ལ་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
