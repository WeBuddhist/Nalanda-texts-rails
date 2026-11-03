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
[Block 5251 [VERSE]]
ཆུ་ཡིས་མ་བཀྲུས་པར་ཡང་དག་པར་འགྱུར། །
ཞེས་བྱ་བ་འདིའི༌[^3364]རྗེས་སུ་བསྟན་པ་ནི།
མཐུ་དང་ལྡན་པ་རྣམས་ཀྱི་རྒྱན་ཡང་ཡིན། །

[Block 5252]
ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས༌[^3365]བསྟན་ཏེ། [^3366]གང་དག་འདི་རྣམ་པར་དག་པར་བྱེད་པ་ཡིན་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར་ཚིགས་བཅད་འདི་སྨོས་ཏེ། ཁྱིམ་པ་དང་། རབ་ཏུ་བྱུང་བ་རྣམས་ཀྱིའོ། །

[Block 5253]
ཁྱིམ་པ་རྣམས་ཀྱི་ནི། [^3367]མཐུ་དང་ལྡན་པ་རྣམས་ཀྱི་རྒྱན་ཡང་ཡིན། །ཞེས་བྱ་བ་ཡིན་ཏེ། གནོད་སེམས་ཀྱིས༌[^3368]དགོན་པའི་མེ་ལ་ཆུ་རྒྱུན་འབེབས་པའོ། །

[Block 5254]
དཀའ་ཐུབ་ཅན་གྱི་སྟོབས་མཆོག་ཕུན་སུམ་ཚོགས་པ་ཡོད་ན་ནི། གནོད་སེམས་དགོན་པའི་མེ་ལ་ཆུའི་རྒྱུན༌[^3369]འབེབས་པ་ཡིན་ཏེ། གནོད་སེམས་ཀྱི་དགོན་པའི་མེ་ལ་ཆུའི་རྒྱུན་འབེབས་ཞེས་བྱ་བ་ཡིན་ཏེ། གནོད་སེམས་ཀྱི་དགོན་པའི་མེ་ལ་ཆུའི་རྒྱུན་དང་འདྲ་བར་དེ་ཉེ་བར་ཞི་བ་སྟེ། དེ་བས་ན་གནོད་སེམས་དགོན་པའི་མེ་ལ་ཆུ་རྒྱུན་འབེབས་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 5255]
དེའི་ཕྱིར། གཉི་གའི་ཚེ་ལ་དོན་མེད་ཞི་བར་བྱེད། །ཅེས་བྱ་བ་སྨོས་ཏེ། དེ་བས་ན་ཆུ་ཡིས་མ་བཀྲུས་པར་ཡང་དག་པར་བྱེད་དེ། དོན་མེད་པར་ཉེ་བར་ཞི་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 5256 [VERSE]]
ཡོན་ཏན་དེ་དང་དེ་དག་ཕུན་སུམ་ཚོགས། །
ཞེས་བྱ་བ༌[^3370]དེའི་རྗེས་སུ་བསྟན་པ་ནི།
དམ་པ་རྣམས་ཀྱི༌[^3371]གོ་ཆ་བཟོད་པ་ཡིན། །

[Block 5257]
ཞེས་བྱ་བའི་ཚིགས་བཅད་དེ་བསྔགས་པའི༌[^3372]མེ་ཏོག་གི་རྒྱུར་གྱུར་པའི་ཕྱིར། བཟོད་པའི་ཡོན་ཏན་གྱི་ཚོགས་རྗེས་སུ་འཕེལ་བར་འགྱུར་རོ། །

[Block 5258]
དེ་ལྟ་བུ་ལ་སྦྱར་བའི་ཕྱིར། ཆོས་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་རྣམས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་སྨོས་པ་ཡིན་ནོ། །

[Block 5259]
ཆོས་ཀྱི་བགེགས་མི་མཐུན་པའི་ཕྱོགས་ནི་མི་མཐུན་པའི་ཕྱོགས་སོ། །

[Block 5260]
ཆོས་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་ཀྱང་ཡིན་ལ། བཟོད་པ་ཡང་ཡིན་པས་ཆོས་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་རྣམས་བཟོད་པའོ། །

[Block 5261]
དེས་འཇོམས་པ་ཡིན་པས་གང་དེས་སྨྲས་པའོ། །

[Block 5262]
བཟོད་པ་ཕན་པར་འགྱུར་ཞེས་བྱ་བ་ལ་བཟོད་པའི་ཕན་པ་ནི། བཟོད་པ་ཕན་པར་འགྱུར་བ་སྟེ། ཕན་པ་དང་མཐུན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5263]
འདོད་ཆགས་ཀྱང་ཡིན་ལ། ལྷག་མ་ལུས་པ༌[^3373]ཡང་ཡིན་པས། འདོད་ཆགས་ཀྱི་ལྷག་མ་ལུས་པའོ། །

[Block 5264]
དེས་ལྕི་བར་གྱུར་བའི་མིག་གང་ཡིན་པ་དེ་ནི། འདོད་ཆགས་ཀྱི་ལྷག་མ་ལུས་པས་མིག་ལྕི་བར་གྱུར་པའོ། །

[Block 5265]
བཙུན་མོ་རྣམས་ཀྱི༌[^3374]སྤོབས་པས་བསྲུང་བ་དང་བྲལ་བའི་བག་ཡངས་སུ༌[^3375]དགོད་ཅིང་། རྩེ་བ་དང་། ལྟ་འདོད་པ་གང་ཡིན་པ་དེ་ནི་བཙུན་མོ་རྣམས་ཀྱི་སྤོབས་པས་བསྲུང་བ་དང་བྲལ་བའི་བག་ཡངས་སུ་དགོད་ཅིང་། རྩེ་བ་དང་། ལྟ་འདོད་པའོ། །

[Block 5266]
མེ་ཏོག་དང་། ལོ་མ་སྣ་ཚོགས་ཀྱིས་གཏོར་བ་གང་ཡིན་པ་དེ་ནི། མེ་ཏོག་དང་། ལོ་མ་རྣམས་ཀྱིས་གཏོར་བའོ། །

[Block 5267]
མེ་ཏོག་དང་ལོ་མ་སྣ་ཚོགས༌[^3376]ཀྱིས་གཏོར་བའི་ནགས་ཀྱི་ལམ་ནི་ལམ་སྟེ། མེ་ཏོག་དང་ལོ་མ་སྣ་ཚོགས་ཀྱིས་གཏོར་བའོ། །

[Block 5268]
ཡང་ན་ལམ་མེ་ཏོག་དང་། ལོ་མ་སྣ་ཚོགས་ཀྱིས་གཏོར་བ་དང་ལྡན་པའོ། །

[Block 5269]
འཁོན་སྙིང༌[^3377]ཡོད་པ་ཞེས་བྱ་བ་ནི། དེའི་ཁྲོ་བའི་རྒྱུས་བྱས་བ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5270]
འདོད་ཆགས་ཀྱིས་དྲན་པ་ཉམས་ཞེས་བྱ་བ་ནི་ད་ལྟར་བྱུང་བའི་དྲན་པ་འཇིག༌[^3378]པའི་རྒྱུ་ཡིན་ཏེ། འདིས་ནི་ཁྲོ་བའི་གཉེན་པོ་མེད་པར་བསྟན་ཏོ། །

[Block 5271]
ཕྲག་དོག་གིས་ཟིལ་གྱིས་ནོན་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་ཀུན་དུ་སྤྱོད་པས་ད་ལྟར་བྱུང་བའི་རྐྱེན་དུ་བསྟན་ཏོ། །

[Block 5272]
དུལ་བ་དང་། དེས་པ་ནི་དུལ་བ་དང་དེས་པའོ། །

[Block 5273]
དེ་གཉིས་ཀྱི་སྤྱོད་པ་ནི་དུལ་བ་དང་། དེས་པར་སྤྱོད་པའོ། །

[Block 5274]
ཉམས་པའི་དུལ་བ་དང་། དེས་པ༌[^3379]སྤྱོད་པ་གང་ཡིན་པ་དེ་ནི། དུལ་བ་དང་། དེས་པར་སྤྱོད་པ༌[^3380]ཉམས་པའོ། །

[Block 5275]
འཐབ་མོ༌[^3381]དང་། རྒོལ་བར་འདོད་པ་དེའི་ཤུགས་ནི་འཐབ་མོ༌[^3382]རྒོལ་བར་འདོད་པའི་ཤུགས་ཏེ་དེ་ལས་སོ། །

[Block 5276]
རྡུལ་དང་། མདོག་འགྱུར་བ་དང་། འདར་བ་ནི༌[^3383]རྡུལ་དང་། མདོག་འགྱུར་བ་དང་། འདར་བ་དག་གོ། །

[Block 5277]
རྡུལ་དང་། མདོག་འགྱུར་བ་དང་། ལུས་འདར་བ་འབྱུང་བ་གང་ཡིན་པ་དེ་ནི། རྡུལ་དང་། མདོག་འགྱུར་བ་དང་། ལུས་འདར་བར་གྱུར་པའོ། །

[Block 5278]
སྨིན་མ་བཙུམས་པས་མིག་རྩ་དམར་པོ་བགྲད་པ༌[^3384]གང་ཡིན་པ་དེ་ནི། ཚུལ་འཆོས་ཞེས་བྱ་བའི་བྱ་བ་པའོ། །

[Block 5279]
ཚུལ་འཆོས་ཀྱི་གཡོ་སྒྱུའི་རང་བཞིན་གང་ཡིན་པ་དེ་ནི་དེའོ།[^3385] །དེ་དག་གི་སྤྱོད་ཚུལ་དང་། མཛེས་པ་དང་། དུལ་བ་ནི༌[^3386]སྤྱོད་ཚུལ་མཛེས་པ་དུལ་བའོ། །

[Block 5280]
དེ་དག་གི་གུས་པ་དང་། མཁས་པའི་སྤྱོད་ཚུལ་མཛེས་པ་དང་། དུལ་བ་ནི་གུས་ཤིང་འོས་པ་མཁས་པའོ། །

[Block 5281]
རབ་ཏུ་ཁྲོས་ཤིང་བཞིན༌[^3387]གྱུར་ལ། །ཞེས་བྱ་བ་འདི༌[^3388]ནི། སོ་སོར་བརྟགས་ཏེ་བརྣག་པའི༌[^3389]མཐུ་ཆུང་བས། །[^3390]ཞེས་བྱ་བ་ལ་སོགས་པ་སྟོན་པ་ཡིན་ནོ། །

[Block 5282]
ཡང་ན་འཐབ་མོ༌[^3391]རྒོལ་འདོད་པའི་ཤུགས་ལས་རྡུལ་ནི་བྱུང་ལུས་འདར་བ་ཞེས་བྱ་བ་དེ་ཉིད་སྟོན་ཏོ། །

[Block 5283]
སྤྱོད་པ་ཉམས་ཤིང་རྩུབ་པར་མངོན་ལ་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི། ང་ཡི་གཟི་བརྗིད་ཟིལ་མནན་ནས། །ཞེས་བྱ་བ་དེ་སྟོན་པ་ཡིན་ནོ། །

[Block 5284]
མཚོན་ཆ་ཐོགས་ཏེ་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་གསོལ་ཀ་བའི་ལག་ན་རལ་གྲི་འདུག་པ་བླངས་ཏེ་ཞེས་བྱ་བ་དེ་ཉིད་སྟོན་ཏོ། །

[Block 5285]
དེས་མགུ་བར་བྱས་ཟིན་ཏོ་ཞེས་བྱ་བ་ནི་སེམས་དབང་དུ་བྱས་པའོ། །

[Block 5286]
དེ་ཡང་ཉམས་སུ་མི་ལེན་ཏེ། དེ་ཅིའི༌[^3392]ཕྱིར་ཞེ་ན། བུད་མེད་བསྟན༌[^3393]པར་སྣང་བ་ལས་བཟོད་པ་མེད་དོ། །

[Block 5287]
འཆོས་པའི་ཚུལ་ཡིན་པས་འཆོས་པའི་ཚུལ་ལོ། །

[Block 5288]
འཆོས་པའི་ཚུལ་ཉིད་འདྲིད་པ་ཡིན་པས་ཚུལ་འཆོས་འདྲིད་པའོ། །

[Block 5289]
དེས་བརྟན་པ་འདུག་པའི་ཚུལ་ནི་བཟོད་པ་སྨྲ་བ་ཡིན་ནོ། །ཞེས་བྱ་བའི་སྒྲ་སྨྲ་ཞིང་འདུག་པའོ། །

[Block 5290]
ཡིད་མི་དགའ་བ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ནོངས་ཀྱིས་དོགས་པའོ། །
--- END BLOCKS ---
