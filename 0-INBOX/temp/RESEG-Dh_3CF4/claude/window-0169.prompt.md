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
[Block 5916]
བསྟན་བཅོས་ཀྱི་རིམ་པ་བཞིན་དུ་ཚིག་ལ་མཁས་པར་གྱུར་པའི་དབང་དུ་བྱས་ནས། དུལ་ཞིང་རབ་ཏུ་གསལ་བའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5917]
དུལ་བ་དང་རབ་ཏུ་གསལ་བ་ནི་དུལ་ཞིང་རབ་ཏུ་གསལ་བའོ། །

[Block 5918]
དུལ་ཞིང་རབ་ཏུ་གསལ་བ་དེས་སྤོབས་པ་ནི་དུལ་ཞིང་རབ་ཏུ་གསལ་བའི་སྤོབས་པའོ། །

[Block 5919]
དེ་གཉིས་འབར་བ་དེ་ནི་དུལ་ཞིང་རབ་ཏུ་གསལ་བའི་སྤོབས་པ་སྐྱེ་བའོ། །

[Block 5920]
དུལ་བ་ནི་ཉོན་མོངས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 5921]
རབ་ཏུ་གསལ་བ་ནི་གནོད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 5922]
འཕྲལ་དུ་ཞེས་བྱ་བ་ནི་ཟིལ་གྱིས་གནོན་པའོ། །

[Block 5923]
སྨྲ་བ་ལེགས་པ་ནི་ལྕེ་བདེ་བར་གྱུར་པ་སྟེ་ངག་བཟང་པོའོ། །

[Block 5924]
དེ་ལ་གོམས་པ་ནི་ལྡན་པའོ། །

[Block 5925]
ཐོས་པ་ཉིད་དཔལ་ཡིན་པས་ཐོས་པའི་དཔལ་ལོ། །

[Block 5926]
དོན་གསལ་བར་རྟོགས་པར་གྱུར་པ་གང་ལ་ཡོད་པ་དེ་ནི་དོན་གསལ་བར༌[^3782]རྟོགས་པར་འགྱུར་བའོ། །

[Block 5927]
དེ་ཉིད་ཐོས་པའི་དཔལ་ཡིན་པས་དོན་གསལ་རྟོགས་འགྱུར་ཐོས་པའི་དཔལ་ལོ། །

[Block 5928]
བསྒྲུབ་པའི༌[^3783]རྒྱུའི་དབང་དུ་བྱས་ནས། ཐོས་དང་ལྡན་ན་འགལ་བ་མེད་པའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5929]
[^3784]འགལ་བའི་དངོས་པོ་ཡིན་པས་འགལ་ལོ། །

[Block 5930]
འགལ་བ་ཡིན་ལ་ཉེས་པ་ཡང་ཡིན་པས་འགལ་བའི་ཉེས་པའོ། །

[Block 5931]
དེ་སྤངས་པ་ནི་འགལ་བའི་ཉེས་པ་མེད་པའོ། །

[Block 5932]
འཁོར་གསུམ་ལམ་ལ་ཞེས་བྱ་བ་ནི་མངོན་པར་མཐོ་བ་བདེ་འགྲོའོ། །

[Block 5933]
སྒྲུབ་པའི་རྒྱུ་ལ་རབ་ཏུ་གནས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཇི་ལྟར་རབ་ཏུ་གནས་པ་ཡིན་ཞེ་ན། ཐོས་པའི་རྗེས་སུ་འཇུག་པས་བསྒྲུབ་པ་ཡིན་པས་ཐོས་པའི་རྗེས་སྒྲུབ་པའོ། །

[Block 5934]
དེ་སྙིང་པོར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་ཐོས་པའི་རྗེས་འཇུག་སྒྲུབ་པ་སྙིང་པོར་བྱེད་པའོ། །

[Block 5935]
སྐྱེ་བའི་རྫོང་ལས་ཚེགས་ཆུང་ཐར་བར་འགྱུར། །ཞེས་བྱ་བ་ནི་ངེས་པར་ལེགས་པའི་དབང་དུ་བྱས་པ་སྟེ། ཐོས་པའི་རྗེས་འཇུག་སྒྲུབ་པ༌[^3785]སྙིང་པོར་བྱེད་པ་དེ་ཉིད་ཀྱིས་ཐར་བའོ། །

[Block 5936]
ཡོན་ཏན་དུ་མ་ཅན་ཞེས་བྱ་བ་ནི་གོང་དུ་བསྟན་པའི་ཡོན་ཏན་ལས་གཞན་དག་ཀྱང་གཟུང་སྟེ་བདག་གིས་ནུས་བཞིན་དུ་ཇི་ལྟར་ཐོས་པ༌[^3786]དེ་ལ་མཆོད་པ་མི་བྱ་བའོ། །

[Block 5937]
ཁྱོད་ཀྱི་བཀའ་ཡང་ཅི་ཕྱིར་བཅག༌[^3787]པར་འགྱུར། །ཞེས་བྱ་བ་འདི་ཡིན་ཏེ། ལེགས་པར་སྨྲ་བ་སྟོན་པ་ལ་ཡང་མཆོད་པ་བྱ་བ་མཆོག་ཏུ་ཚད་མ་ཡིན་ཏེ། དེ་ལས་མཆོག་ཏུ་གྱུར་པ་མེད་པའི་ཕྱིར་དོགས་པ༌[^3788]མེད་པའི༌[^3789]ཡོན་ཏན་ཉམས་པར་འགྱུར། སྐྱོན་གྱི་ལམ་དུ་ཞུགས་པས་འཐོབ་འགྱུར་བའི། རྒྱལ་སྲིད་སྤྱོད་པ་ཡིན་ཏེ། དེ་བས་ན་རྒྱལ་སྲིད་སྤྱོད་པ་བདག་ལ་དགོས་པ་མེད་པའོ། །

[Block 5938]
སུ་དཱ་སའི་བུའི་དྲུང་དུ་འགྲོ་ཞེས་བསྟན་པ་དེ་རྒྱུ་གཉིས་ཀྱིས་བསྟན་པ་ཡིན་ནོ། །

[Block 5939]
[^3790]ལེགས་པར་བཤད་པ་ལ་མཆོད་པའི་ཚད་ཀྱི་ཚིག་དང་། བདག་ཉིད་འབྱོར་བའི་དོན་ལས་ལྡོག་པའོ། །

[Block 5940]
མི་དགའ་བ་ལས་བརྩལ་བའི་ཕྱིར། ཅི་སྟེ་བདེན་པ་བསྲུང་བའི་ཕྱིར། བདག་ཉིད་ལ་མི་དགའ་བ་མི་བྱ་བའི་དབང་དུ་བྱས་ནས་བུ་ཁྱོད་ཉིད་ལ་ཕན་པའི་ཕྱིར་ཞས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 5941]
བདེན་པ་བསྲུང་བའི༌[^3791]དབང་དུ་བྱས་ནས། འོན་ཏེ་དེའི༌[^3792]དྲུང་དུ་འགྲོ་བར་ཁྱོད་ཀྱིས་ཁས་བླངས་ཏེ། །ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 5942]
གཞུང་ལུགས་ཀྱི་ཆོས་དང་འགལ་བ་ཞེས་བྱ་བ་ནི༌[^3793]དྲང་སྲོང་གི་ཆོས་ཡིན་པས་གཞུང་ལུགས་ཀྱི་ཆོས་སོ། །

[Block 5943]
དེ་དང་འགལ་བའི་ཆོས་གང་ལ་ཡོད་པ་དེ་ནི་གཞུང་ལུགས་ཀྱི་ཆོས་དང་འགལ་བའོ། །

[Block 5944]
སྡུག་བསྔལ་གྱི་འདམ་དུ་བྱིང་བ་ཞེས་བྱ་བ་ནི། མིའི་ཤ་ཟ་བའི་སྡུག་བསྔལ་བ༌[^3794]ཉིད་དུ་བྱིང་བའོ། །

[Block 5945]
སེམས་ཅན་དམྱལ་བ་ལ་མངོན་དུ་ཕྱོགས་པ་ཞེས་བྱ་བ་ནི། དམྱལ་བར་སྐྱེ་བ་ལ་མངོན་དུ་ཕྱོགས་པ་སྟེ། དེ་བས་ན། དེ་ཉིད་ཀྱིས༌[^3795]སྡུག་བསྔལ་གྱི་འདམ་དུ་བྱིང་བའི་ཕྱིར་ཏེ། དེ་ལྟར་འདི་གཉིས༌[^3796]ཀྱིས་སྡུག་བསྔལ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5946]
མཛའ་བོ་དང་གཉེན་བཤེས་ཀྱིས་ཡོངས་སུ་སྤངས་པ་ཞེས་བྱ་བ་ནི། བཟོད་པའི་འབྲས་བུ་གཡོག་འཁོར་གྱིས༌[^3797]ཡོངས་སུ་སྤངས་པའོ། །

[Block 5947]
མགོན་མ་མཆིས་པ་ཞེས་བྱ་བ་ནི་གཞན་ཡང་སྔར༌[^3798]མ་མཐོང་བའི་སྐྱེ་བོ་རྣམས་ཀྱིས་ཡོངས་སུ་སྤངས་པ་སྟེ་དོན་མེད་པའི་ཕྱིར་རོ། །

[Block 5948]
དེའི་དྲིན་གྱིས་ཞེས་བྱ་བ་ནི་བཏང་བའི་རྒྱུས་སོ། །

[Block 5949]
ཡུན་རིང༌[^3799]དུ་གོམས་པ་དེས་སེམས་ཤིན་ཏུ་རྩུབ་ཅིང་དྲི་མ་ཤས་ཆེར་ཡོག་པ་གང་ལ་ཡོད་པ་དེ་ནི་སེམས་རྩུབ་པ་ཡུན་རིང་དུ་གོམས་པའི་དྲི་མས་ཤས་ཆེར་ཡོག་པའོ། །

[Block 5950]
འཇིགས་པ་དང་སྐྲག་པ་ཅུང་ཟད་ཀྱང་མེད་པའི་ཕྱིར་བརྟན་པས་བདག་རང་འདིར་འོངས་པ་ཡིན་ཏེ། དེ་བས་ན་བདེན་པ་སྨྲ་ཞིང་དགེ་བའོ། །

[Block 5951]
བདེན་པ་སྨྲ་ཞེས་གྲགས་པ་དེ༌[^3800]ཇི་ལྟ་བུའི་བདེན་པ་ལ་གནས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ།

[Block 5952 [VERSE]]
འདི་ལྟར་བདེན་པ་བསྲུང་བའི་ཕྱིར། །
སྲོག་དང་རྒྱལ་སྲིད་གང་གཏོང་བ། །

[Block 5953]
ཞེས་བྱ་བ་སྨོས་ཏེ། གཟི་བྱིན་རབ་ཏུ་ཉམས་ཞེས་བྱ་བ་འདིས་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་སྡུག་བསྔལ་གྱི་འབྲས་བུ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5954]
འཕྲལ་གྱི་བདེན་པ་མི་འགྲུབ་པ། །ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་བདེན་པ་ཡང་མི་འགྲུབ་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5955]
འོན་ཀྱང་ཁྱོད་ནི་འཇིག་རྟེན་གཉི་ག་ལ་ཕན་པ་སྒྲུབ་པ་མ་ཡིན་ཏེ། གཞུང་ལུགས་ཀྱི་ཚུལ་ལ་ནི་ང་ཉིད་མཁས་སོ། །
--- END BLOCKS ---
