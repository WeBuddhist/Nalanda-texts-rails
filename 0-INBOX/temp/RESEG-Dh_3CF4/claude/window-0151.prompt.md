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

[Block 5291]
མྱ་ངན་ནི་བཤུགས༌[^3394]པར་མ་ནུས་པའོ། །

[Block 5292]
དེ་གཉིས་ཀྱིས་གདུངས་བའི་ཡིད་གང་ཡིན་པ་དེ་ནི་ཡིད་མི་དགའ་ཞིང་མྱ་ངན་གྱིས་གདུངས་པའོ། །

[Block 5293]
འཇིགས་པ་ནི་རྒྱལ་པོའི་ཆད་པས་སོ། །

[Block 5294]
སྐྲག་པ་ནི་དེ་བཅོས་བའི་ཐབས་ལ་མ་ཤེས་པས་སོ། །

[Block 5295]
དེ་གཉིས་ཀྱིས་གཡེན་སྤྱོ་བ་ནི། འཇིགས་ཤིང་སྐྲག་པས་འཁྲུགས་པའོ། །

[Block 5296]
དྲང་སྲོང་མཆོག་དེའི་མྱ་ངན་བྱེད་ཅིང་ཞེས་བྱ་བ་ལ། ཅིའི་རྒྱུས་མྱ་ངན་བྱེད་བ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ། བདག་ཅག་རྣམས་ཀྱི་དོན་ནི་བདག་ཅག་རྣམས་ཀྱི༌[^3395]ཕྱིར་རོ། །

[Block 5297]
ཉེས་པ་ཡོད་མེད་པར༌[^3396]ཞེས་བྱ་བ་ནི་གང་ལ་རྒྱལ་པོ་ཉེས་པར་བྱས་པས༌[^3397]དོགས་པའི་ཉེས་པ་དེ༌[^3398]མེད་ཅིང་མ་ཡིན་པས་སོ། །

[Block 5298]
དུལ་བ་ཞེས་བྱ་བ་ནི་ལུས་དང་ངག་གི་དུལ་བ་དག་གོ། །

[Block 5299]
དཀའ་ཐུབ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་བའོ། །

[Block 5300]
ཡོན་ཏན་གྲགས་པ་ཞེས་བྱ་བ་ནི། ཡོན་ཏན་འཇིག་རྟེན་གྱིས་བརྗོད་པའོ། །

[Block 5301]
ལམ་དུ་ཞུགས་ཞེས་བྱ་བ་ནི་མངོན་པར་འགྲོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5302]
བྱེད་པ་ནི་ལུས་དང་། ངག་གི་འགྱུར་བའོ། །

[Block 5303]
ཅི་ཞིག་གྱུར་ནས་སུ་ཞེས་བྱ་བ་ནི་བརྡེག་པ་དང་། བཅིངས་པ་ལ་སོགས༌[^3399]པའི་ལས་ཀྱི་ལམ་གྱིས༌[^3400]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5304]
གྲགས་པ་ཐོབ་པ་ཞེས་བྱ་བ་ནི་ཐུབ་པའི་ལུས་བཅད་པས། རང་གི་ཆོས་ཀྱི་ལུས་བཅད་ཅིང་འཆི་བ་ལ་སོགས་པས་སོ། །

[Block 5305]
ཨ་ཛིན་དང་དབྱིག་པ་གང་ཡིན་པ་དེ་ནི་ཨ་ཛིན་དང་དབྱིག་པའོ། །

[Block 5306]
དེ་ཡོད་པ་ནི་ཨ་ཛིན་དང་དབྱིག་པ་ཐོགས་པའོ། །

[Block 5307]
གཡོ་སྒྱུ་ནི་སླུ༌[^3401]བའོ། །

[Block 5308]
གཡོ་སྒྱུ་ཉིད་བརྗིད་བག་ཏུ་འཆོས་པ་ཡིན་པས་གཡོ་སྒྱུ་བརྗིད་བག་འཆོས་པའོ། །

[Block 5309]
ཁྲོས་པ་དང་། རྔམ་པ་ཞེས་བྱ་བ་ལ། ཁྲོས་པ་ནི་ཞེ་སྡང་ངོ་། །རྔམ་པ་ནི་དེ་ལ་མངོན་པར་འཇུག་པའོ། །

[Block 5310]
དེ་གཉིས་ཀྱི་སྤྱོད་པའི་ཚུལ་མི་སྡུག་བར་གྱུར་པ་དེ་ནི་དེའོ། །

[Block 5311]
འདིས་ནི་མཐོང་བའི་ཆོས་བདག་ཉིད་ཟླ་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5312]
དུལ་བར༌[^3402]སྤྱོད་པའི་དཔལ་ནི་ཉམས། །ཞེས་བྱ་བ་འདིས་ནི། བྱང་ཆུབ་སེམས་དཔའ་ལ་ཟླ་མེད་པའི་འཇུག་པ་བསྟན་ཏོ། །

[Block 5313]
དེ་ལྟར་དེ་གཉིས་ནི་མཐོང་བའི་ཆོས་ལ་བདག་དང་། བྱང་ཆུབ་སེམས་དཔའ་ལ་སྒྲུབ་པ་བསྟན་ཏོ། །

[Block 5314]
བདག་ལ་ཕན་པ་དང་། གནོད་པའི་ལམ་ནི་བརྗེད་པར་གྱུར། །ཅེས་བྱ་བ་འདིས་ནི་སྐྱེ་བ་གཞན་གྱི་མི་འདོད་པའི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 5315]
སྐལ་བ་མེད་ལས་གྱུར་པ་ཞེས་བྱ་བ་འདིས་ནི། སྔར་བྱས་བའི་ལས་ངན་པ་ལས་གྱུར་བའོ། །

[Block 5316]
སེམས་ལ༌[^3403]གཅགས་པ་ནི་ཚིག༌[^3404]ཙམ་གྱིས་ཀྱང་མ་བྱས་ན་གཞན་ལྟ་ཅི་སྨོས་ཞེས་བྱ་བ་ཡིན་ཏེ། འདིས་ནི་སྔར་དྲིས་བའི་རྒྱུའོ། །

[Block 5317]
དམ་པ་མ་ཡིན་པའི་སྤྱོད་པ་ནི་ཉེས་པའི་ལམ་སྟེ། རང་གི་ཆོས་ཀྱི་ལམ་མ་ཡིན་བའོ། །

[Block 5318]
འགྲོ་བའི་དོན་བྱེད་ཅེས་བྱ་བ་ནི་ཉེས་པ༌[^3405]མི་བྱེད་པ་དག་ལ་ཕན་འདོགས་པར་འཇུག་པའོ། །

[Block 5319]
རྣམ་པར་བརྟག་པའི་ལམ་ཞེས་བྱ་བ་ནི་ཡང་དག་པའི་ལམ་མོ། །ཅིའི་ཕྱིར་ལམ་རྣམ་པར་བརྟག་ཅེ་ན། དེའི་ཕྱིར་སྨྲས་པ། ལེགས་པ་དག་ཀྱང་ཅུང་ཟད་མི་རིགས་མཐོང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། མི་རིགས་པ་ཞེས༌[^3406]བྱ་བ་ནི་ཉེས༌[^3407]པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5320]
ལེགས་པ་དག་ཀྱང་ཞེས་བྱ་བ་ནི་ཉེས་པ་མེད་པའོ། །

[Block 5321]
ཁ་ཅིག་ནི་ཉེས་ཀྱང་ལེགས་པར་མཐོང༌[^3408]ཞེས་བྱ་བ༌[^3409]སྟེ། དེས་ན་དེའི་ཕྱིར་མ་བརྟགས་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 5322]
ཡུལ་ཅི་ཞིག་ལ་མ་བརྟགས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ། གཏན་ཚིགས་ཁྱད་པར་ཅན་ལ་སྟེ། ཁྱད་པར་གྱི་གཏན་ཚིགས་དག་ནི་གཏན་ཚིགས་ཁྱད་པར་ཅན་དག་སྟེ་དེ་ལའོ། །

[Block 5323]
དགོས་པའི་དོན་ཉིད་ཅེས་བྱ་བ་ནི། དེའི་དངོས་པོ་ཉིད་ཡིན་པས་དགོས་པའི་དོན་ཉིད་དོ། །

[Block 5324]
དགོས་པའི་དོན་ཡོད་པར་བརྟགས་པ་ཉིད། གཏན་ཚིགས་ཁྱད་པར་གྱིས་ཏེ། དེ་ལྟར་བརྟག་པ་བྱས་ན་ནི། དགོས་པའི་དོན་རྟོགས་པ་ཉིད་དུ་འགྱུར་ཞིང་ཉེས་པ་ཡང་ཉེས་པ་ཉིད་དུ་རྟོགས་སོ། །

[Block 5325]
ལེགས་པར་ཞུགས་ནས་ནི་ཞེས་བྱ་བ་ནི་ཆོས་ཁྲིམས་ལས་བཤད་པ་བཞིན་དུའོ། །
--- END BLOCKS ---
