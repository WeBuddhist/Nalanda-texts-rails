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
[Block 5181]
ཕྱི་མ་ལ་ཡང་བདེ་བ་འཐོབ་མི་འགྱུར། །ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་དུ་སྟེ། འཇིག་རྟེན་འདིའི་བདེ་བའི་རྒྱུས་ཏེ། བདེ་བ་ནི་དགེ་བ་ལ་སོགས་པ་ཡིན་པས་སོ། །

[Block 5182]
རབ་ཏུ་སྦྱིན་དང་ཚུལ་ཁྲིམས་ལ་སོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པས་ནི་བཟོད་པ་དང་། བརྩོན་འགྲུས་ཀྱང་གཟུང༌[^3326]ངོ་། །དགེ་བ་དེ་ནི་ཐམས་ཅད་ཀྱི་རྒྱུ་ཡིན་པའི་ཕྱིར། འདི་ལས་བྱུང་ཞེས་བྱ་བས་བསྟན་པ་ཡིན་ནོ། །

[Block 5183]
ད་ནི་འབྲས་བུ་དེ་མེད་པར་ཡང་སྦྱིན་པ་ལ་སོགས་པ་དང་ལྡན་ན་འབྲས་བུ་སྐྱེ་བའི་དབང་དུ་བྱས་ནས། དེ་མེད་ཀྱང་དེའི་དངོས་པོའི་རྒྱུ་མཚན་ཉིད་བསྟན་པའི་ཕྱིར་སྨྲས་པ། རིགས་ལ་སོགས་པ་དམན་ཡང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5184]
སྡིག་པ་ལ་མ་ཆགས་ཤིང་ཞེས་བྱ་བས་ནི། སྡིག་པ་ལས་ལྡོག་པར་སྟོན་ཏེ། མི་དགེ་བའི་ལས་ཀྱི་ལམ་ལས་ལྡོག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5185]
རབ་ཏུ་སྦྱིན་དང་ཚུལ་ཁྲིམས་ལ་སོགས་ཡོན་ཏན་ལྡན། །ཞེས༌[^3327]བྱ་བ་ནི། སྦྱིན་པ༌[^3328]དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པ་དང་། བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་ལྡན་པའོ། །

[Block 5186]
ཕྱི་མའི་ཚེ་ལའང་བདེ་བ་ཞེས་བྱ་བ་ནི། འཇིག་རྟེན་ཕ་རོལ་དུ་ཡང་བདེ་བའི་རྒྱུ་དགེ་བ་ལ་སོགས་པའོ། །

[Block 5187]
ཚུལ་ཁྲིམས་ལ་སོགས་པའི་འབྲས་བུ་ཇི་ལྟ་བུ་ཞེ་ན། དབྱར་གྱི་དུས་ན་འབབ་ཆུས་རྒྱ་མཚོ་གང་བ་བཞིན། །ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 5188]
འཇིག་རྟེན༌[^3329]དུ་བདེ་བ་རྒྱས་པར་འགྱུར་བར་མ་ཟད་དེ། མཐོང་བའི་ཆོས་འདི་ལ་ཡང་ཚུལ་ཁྲིམས་ཀྱི་ཕན་ཡོན་རིགས་ལ་སོགས་པའི་རྒྱན་དུ་ཡང་འགྱུར་ཏེ། ཚུལ་ཁྲིམས་ལ་སོགས་པ་དང་ལྡན་པ་དེ་བསྟན་པའི་ཕྱིར། རིགས་དང་གཟུགས་དང་ལུས་ཀྱི་ཡོན་ཏན་རྣམས་ཀྱང་རུང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5189]
འདིའི་བསྡུས་པའི་དོན་ནི་ཚུལ་ཁྲིམས་དང་། བཟོད་པ་དང་། སྦྱིན་པའི་འབྲས་བུ་བདག་ཉིད་ཆེ་བ་དང་། འབྱོར་པ་དང་། གཡོག་འཁོར་ཕུན་སུམ་ཚོགས་པ་ལ་གནས་པའོ། །

[Block 5190]
དེ་ལྟར་བྱུང་བའི་བདག་ཉིད་ཆེ་བ་དང་། གཡོག་འཁོར་འབྱོར་པའི་རྒྱུ་དེ་བས་ཁྱད་པར་དུ་གྱུར་ཅིང་། དེ་དག་གི་རྒྱན་དུ་གྱུར་པ་ཡིན་ཏེ། ཇི་ལྟར་ཤིང་དང་། ཆར་སྤྲིན་དང་། མཚོ་དག་ལ་མེ་ཏོག་དང་། གློག་ཕྲན་འགྱུ་བ་དང་། བུང་བ་མྱོས་པ་འདུ་བའི་པདྨ་ལྟ་བུ་སྟེ། དེ་ལ་ཤིང་ལྟ་བུ་ནི་ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུ་སྟེ། ད་ལྟར༌[^3330]བྱུང་བའི་བདག་ཉིད་ཆེན་པོའི་མཐོ་བ་ཉིད་དེ་ལ་རྒྱན་དུ་གྱུར་བར་བྱེད་དེ། དེ་ལས༌[^3331]ཀྱང་ཁྱད་པར་དུ་གྱུར་པའི་མཐོ་བ་ཕུན་སུམ་ཚོགས་པའི་རྒྱུ་ད་ལྟར་བྱུང་བའི་ཚུལ་ཁྲིམས་ཏེ། ཇི་ལྟར་ཤིང་རྣམས་མཐོ་བ་ཉིད་ལ་གཞན་མེ་ཏོག་གིས་བརྒྱན་པའི༌[^3332]རྒྱུས་སོ། །

[Block 5191]
ཆར་སྤྲིན་ལྟ་བུ་ནི་ད་ལྟར་བྱུང་བའི་སྦྱིན་པའི་འབྲས་བུ་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 5192]
ཆར་གྱི་རྟགས་གློག་ཕྲན་འགྱུ་བ་ལྟ་བུ་ནི་སྦྱིན་པ་པོའི་རྟགས་མ་འོངས་པ་ན་ཁྱད་པར་དུ་གྱུར་པའི་བདག་ཉིད་ཀྱི་ཕུན་སུམ་ཚོགས་པ་མཐོང་བ། སྦྱིན་པའི་འབྲས་བུ་ད་ལྟར་བྱུང་བ་ལ་བྱས་པ་ནི་ཆར་གྱི་རྟགས་གློག་ཕྲན་འགྱུ་བ་དང་འདྲ་བར་སྦྱིན་པ་པོའི་རྟགས་མ་འོངས་པ་ན།[^3333] དེ་ལས་ཁྱད་པར་དུ་གྱུར་པའི་ལོངས་སྤྱོད་ཀྱི་རྒྱུ་དག༌[^3334]གིས་བརྒྱན་པར་གྱུར་པ་ཡིན་ནོ། །

[Block 5193]
མཚོ་ལྟ་བུ་ནི་ད་ལྟར་བྱུང་བའི་བཟོད་པའི་འབྲས་བུ་བཀུར་སྟི་དང་། གཡོག་འཁོར་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 5194]
བུང་བ་མྱོས་པའི་པདྨ་ལྟ་བུ་ནི་གཞན་དེ་ལས་ཁྱད༌[^3335]དུ་གྱུར་པའི་གཡོག་འཁོར་ཕུན་སུམ་ཚོགས་པའི་རྒྱུ་བཟོད་པ་ད་ལྟར་བྱུང་བའི་རྒྱན་དུ་གྱུར་བ་ཡིན་ནོ། །

[Block 5195]
ཡོན་ཏན་ཁྱད་པར༌[^3336]འཕགས་པ་ལུས་ཅན་དག་གི་རྒྱན། །ཞེས་བྱ་བ་ལ། ཚུལ་ཁྲིམས་དང་། སྦྱིན་པ་དང་། བཟོད་པ་རྣམས་ཀྱི་ཁྱད་བར་དུ་གྱུར་པའི་དབང་དུ་བྱས་པ་ནི་དེ་ལས་ཁྱད་པར་དུ་གྱུར་པ་རྣམས་ཀྱིས་སོ། །

[Block 5196]
ཚུལ་ཁྲིམས་ལ་སོགས་པས་རིགས་ལ་སོགས་པ་འཐོབ་པར་འགྱུར་ཞིང་། གཞན་དུ་མི་འགྱུར་བར་ཇི་ལྟར་ཤེས་པར་བྱ་ཞེ་ན། དེ་བསྒྲུབ་པའི་ཕྱིར། ནད་མེད་ཚེ་རིང་ནོར་དང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5197]
ནད་མེད་པ་དང་། ཚེ་རིང་བ་དང་། རིགས་ནི་ཚུལ་ཁྲིམས་ཀྱིའོ། །

[Block 5198]
ནོར་ནི་སྦྱིན་པའི་འོ། །

[Block 5199]
གཟུགས་ནི་བཟོད་པའོ།[^3337] །རབ་དང་། འབྲིང་དང་། ཐ་མ་ནི་རབ་འབྲིང་ཐ་མའོ། །

[Block 5200]
དེ་ཉིད་ཀྱི་བྱེ་བྲག་དག་ནི་རབ་འབྲིང་ཐ་མའི་བྱེ་བྲག་གོ། །

[Block 5201]
དེ་དག་སྣ་ཚོགས་པ༌[^3338]ནི་རབ་འབྲིང་ཐ་མའི་བྱེ་བྲག་སྣ་ཚོགས་པའོ། །

[Block 5202]
ཡང་ན་རབ་འབྲིང་ཐ་མ་དག་ནི་བྱེ་བྲག་སྟེ། ལྷག་མ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 5203]
ངོ་བོ་ཉིད་ལས་གྱུར་པ་ནི་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། རྒྱུ་མེད་པ་ཉིད་ཀྱི་བྱེ་བྲག་ལས་བྱུང་བའི་དངོས་པོ་མེད་དེ། འདིས་ནི་རྒྱུ་མེད་པར་སྨྲ་བ་བསལ་ཏོ། །

[Block 5204]
སེམས་ཅན་སྣ་ཚོགས་པ་ནི་གཞན་གྱིས༌[^3339]བསྐྱེད་པ་མ་ཡིན་ཏེ། དབང་ཕྱུག་ལ་སོགས་པས་སོ། །

[Block 5205]
གལ་ཏེ་རྒྱུ་གཅིག་གིས་བསྐྱེད་པ་ཡིན་ན། འགྲོ་བ་རྣམས་བྱེ་བྲག་མེད་པར་འགྱུར་ཏེ། འདིས་ནི༌[^3340]མི་མཐུན་པ་རྒྱུར་སྨྲ་བ་བསལ་ཏེ། [^3341]དེ་ལྟ་མོད་ཀྱི་རབ་ལ་སོགས་པའི་བྱེ་བྲག་ནི་སེམས་ལས་བྱུང་བ་ཡིན་ཏེ། དེའི་ཕྱིར་སྨྲས་པ། ལས་ནི་རྣམ་པ་གསུམ་ལས་གྱུར། །ཅེས་བྱ་བ་སྟེ། རྣམ་པ་གསུམ་ནི་ལུས་དང་། ངག་དང་། ཡིད་རྣམ་པ་གསུམ་གྱི་དབྱེ་བའོ། །

[Block 5206]
དེ་ནི་སོ་སོའི་དབང་གིས་མཐའ་ཡས་པ་སྟེ༌[^3342]འགྲོ་བ་སྣ་ཚོགས་ཀྱི་དབྱེ་བ་མཐའ་ཡས་པར་རིགས་པ་ཉིད་དོ། །

[Block 5207]
འདི་དག་ལས་རྣམ་པ་གསུམ་ལས་གྱུར་པར་ཤེས་པ་ཡིན་པའི་ཕྱིར། འདི་ལྟར་འཇུག་པར་བྱ་སྟེ། མི་བརྟན་པ་ཞེས་བྱ་བ་ནི་སྐད་ཅིག་གིས་འཇིག་པ༌[^3343]སྟེ། མི་རྟག་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5208]
འཆི་བ་དང་ཉེ་བ་ཞེས་བྱ་བ་སྐལ་བ་མཐུན་པའི་རིས་ལས་མི་རྟག་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5209]
སྡིག་པ་སྤང་བར་གྱིས་ཞེས་བྱ་བ་ནི་མི་དགེ་བའི་ལས་ཀྱི་ལམ་མོ། །

[Block 5210]
དགེ་བའི་ཕྱོགས་ལ་བརྟེན་པ་ནི། སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པ་དང་། བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་བརྟེན་པའོ། །ཅིའི་ཕྱིར་ག་ལས་ཤེ་ན། ལམ་ནི་འདི་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ། དགེ་བའི་ཕྱོགས་ལ་བརྟེན་པ་དང་། སྡིག་པ་སྤང་བའོ། །

[Block 5211]
གྲགས་པ་ནི་ཚེ་འདིའི་ཕན་ཡོན་བསྟན་པ་ཡིན་ནོ། །

[Block 5212]
བདེ་བ་འཐོབ་པ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཡིན་ཏེ། བདེ་བ་འདོད་པ་དག་ཏུ་བདེ་བ་འཐོབ་པའོ། །

[Block 5213]
འགྲོ་བ་དག་ལ་འདས་པའི་དུས་ཀྱི་བཟོད་པ་ནི་མ་བསྟན་ཏེ། བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་མཚན་ཉིད་དང་། བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུའི་དབང་དུ་བྱས་ནས་ཐ་དད་པར་རྗེས་སུ་བསྟན་པའོ། །

[Block 5214]
དེས་ན་ད་ནི་བཟོད་པ་ལས་བརྩམས་ནས། ཡིད་ལ་ཞེ་སྡང་ཡོད་ན་ཡང་། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་བརྒྱད་ཀྱིས་བསྟན་ཏེ། ཡིད་ལ་ཞེ་སྡང་ཡོད་ན་ཡང་། །ཞེས་བྱ་བ་ནི། བཟོད་པ་མེད་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5215]
[^3344]

[Block 5216]
གཞན་ལ་ཕན་པ་མ་ཡིན་པས་མི་བཟོད་པར་བྱེད་པ་སྟེ། གཞན་མི་འདོད་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 5217]
བདག་ལ་ཡང་སྐྱེ་བ་གཞན་ལ་ཕན་པར་འགྱུར་བ་མེད་ཅིང་། རབ་ཏུ་སྡིག་པར་བྱེད་དེ། བདག་དང་གཞན་གྱི་ངན་སོང་གི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 5218]
དེ་དག་གིས་ཞེས་བྱ་བ་ནི་ཡིད་ལ༌[^3345]ཞེ་སྡང་ཡོད་པའོ། །

[Block 5219]
སྡིག་ལ་འཛེམ་པ་ནི་མི་འདོད་པའི་འབྲས་བུ་ལ་འཇིགས་པས་སོ། །

[Block 5220]
གཉེན་པོ་རྣམས་ལ༌[^3346]བརྟེན་ནས་ཞེས་བྱ་བ་ནི། བཟོད་པ་ལ་བརྟེན་པའོ། །
--- END BLOCKS ---
