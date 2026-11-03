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
[Block 5741]
དེ་ལས་གསོད་པར༌[^3665]སྦྱོར་བའི་གནོད་པ་བྱེད་པའི་དབང་དུ་བྱས་ནས། ཤ་ར་བྷ་དང་། རུ་རུ་དང་། སྤྲེའུའི་སྐྱེས་པའི་རབས་སོ། །

[Block 5742]
དེ་ལ་ཤ་ར་བྷའི་སྐྱེས་པའི་རབས་སུ་ནི་བདག་ཉིད་ཀྱིས་མདའ་འཕེན་པ་དང་། གནོད་པ་མ་བྱས་ཏེ། ཕན་བཏགས་ཤིང་རྒྱལ་པོ་ལ་བཟོད་པ་སྟེ། སྦྱོར་བ་བྱེད་པ་ལ་བཟོད་པ་བྱེད་པའི་དབང་དུ་བྱས་པའོ། །

[Block 5743]
རུ་རུ་དང་། སྤྲེའུའི་སྐྱེས་པའི་རབས་སུ་ནི་བྱང་ཆུབ་སེམས་དཔས༌[^3666]དེ་གཉིས་ལ་ཕན་བཏགས་པ་ཡིན་དུ་ཟིན་ཀྱང་གནོད་པ་བྱེད་པར་འཇུག་པ་དེ་གཉིས་ལ་བཟོད་པའི་ཕྱིར་རོ། །

[Block 5744]
འདི་གཉིས་ལ་ཁྱད་པར་ནི་འདི་ཡོད་དེ། རུ་རུའི་སྐྱེས་པའི་རབས་སུ་ནི་རྒྱལ་པོ་བྱང་ཆུབ་སེམས་དཔའ་ལ་གསོད་པར༌[^3667]སྦྱོར་བས་སྦྱོར་དུ་བཅུག་པར་བསྟན་ཏེ། བདག་ཉིད་ཀྱིས་ནི་གསོད་པར༌[^3668]སྦྱོར་བ་མ་བརྩམས་སོ། །

[Block 5745]
སྤྲེའུའི་སྐྱེས་པའི་རབས་སུ་ནི་བྱང་ཆུབ་སེམས་དཔས་ཕན་བཏགས་པ་བྱས་པ་གང་ཡིན་པ་དེ་ལ་བདག་ཉིད་ཀྱིས་གསོད་པར་སྦྱོར་བ་རྩོམ་པའོ། །

[Block 5746]
དེ་ཉིད་ཀྱི་ཕྱིར་རུ་རུའི་སྐྱེས་པའི་རབས་སུ་མཐོང་བའི་ཆོས་ཉིད་ལ་ལག་པ་ཆད་པར་སྟོན་པ་ཡིན་ནོ། །

[Block 5747]
དེ་བཞིན་དུ་སྤྲེའུའི་སྐྱེས་པའི་རབས་སུ་ཡང་བདག་ཉིད་གསོད་པར་རྩོམ་པ༌[^3669]ཡིན་པས་མཛེའི་ནད་ཀྱིས་དེ་མ་ཐག་ཏུ་ཟིལ་གྱིས་མནན་ཏོ། །

[Block 5748]
ད་ནི་བཟོད་པ་སྨྲ་བའི་སྐྱེས་པའི་རབས་སུ་ནི་བདག་ཉིད་གསོད་པར་རྩོམ་པ་ཡིན་པའི་ཕྱིར། དེ་མ་ཐག་ཏུ་རིམས་ནད་མེ་བཞིན་འབར་ཞེས་བྱ་བ་དང་། ས་གས་ནང་དུ་ཞུགས་ཞེས་བྱ་བའོ། །

[Block 5749]
གཙུག་ཕུད་བྱང་ཆུབ་ཀྱི་སྐྱེས་པའི་རབས་སུ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ལ་གནོད་པ་བྱེད་པའི་རྒྱལ་པོ་མཐོང་བའི་ཆོས་ཉིད་ལ་མི་སྡུག་པའི་རྣམ་པར་སྨིན་པ་མ་ཐོབ་པ་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་ལ་ཞེ་སྡང་བ༌[^3670]མེད་པའི་ཕྱིར་དང་། ཁྱིམ་ཐབ༌[^3671]དང་ཆུང་མ་ཕལ་པ༌[^3672]མེད་པའི་ཕྱིར་རོ། །

[Block 5750]
ངང་པའི་སྐྱེས་པའི་རབས་སུ་ཡང་སྡིག་པའི་བསམ་པ་མེད་པའི་ཕྱིར་དང་། བྱང་ཆུབ་སེམས་དཔའི་ཡོན་ཏན་བརྗོད་པས་ཕྲད་པར་འདོད་པ་དེས་བྱང་ཆུབ་སེམས་དཔའ་ལ་གནོད་པ་བྱས་ཀྱང་མི་འདོད་པའི་འབྲས་བུ་མ་ཐོབ་པའོ། །

[Block 5751]
བྱང་ཆུབ་ཆེན་པོའི་སྐྱེས་པའི་རབས་སུ་ནི་རྒྱལ་པོ་ལ་སྡིག་པའི་བསམ་པ་མེད་པའི་ཕྱིར༌[^3673]དང་། མ་གུས་པའི༌[^3674]ཉི་ཚེ་ཙམ་དུ་ཟད་པའི་ཕྱིར་དང་། [^3675]མི་འདོད་པའི་འབྲས་བུ་མེད་དོ། །

[Block 5752]
ཤ་ར་བྷའི་སྐྱེས་པའི་རབས་སུ་ཡང་རྒྱལ་པོ་ལ་སྡིག་པའི་བསམ་པ་མེད་པ་དང་། གནོད་པའི་སྦྱོར་བ་ཉི་ཚེ་ཙམ་ཡོད་པའི་ཕྱིར་དང་། བྱང་ཆུབ་སེམས་དཔའ་ལ་གནོད་པ་བྱེད་པར་སྦྱོར་བ་ཡང་བྱང་ཆུབ་སེམས་དཔའ་ཡིན་པར་སྔར་མ་ཤེས་པ་དང་། རྒྱལ་པོས་གནོད་པ་མ་བྱས་པའི་ཕྱིར་མི་འདོད་པའི་འབྲས་བུ་མེད་དོ། །

[Block 5753]
དེ་ཉིད་ཀྱིས་འདི་དག་ནི་བཟོད་པ་ཆུང་བ་ཡིན་པའི་ཕྱིར་དང་པོར་སྨོས་པ་ཡིན་ནོ། །

[Block 5754]
སྐྱེས་པའི་རབས་འདི་དག་ལས་གཞན་རུ་རུ་དང་། སྤྲེའུ་དང་། བཟོད་པ་སྨྲ་བ༌[^3676]སྐྱེས་པའི་རབས་ཕྱིས་བཀོད་པ་ནི་གོ་རིམས་བཞིན་དུ་ཁྱད་པར་དུ་གྱུར་པའི་ཕྱིར་ཏེ། བྱང་ཆུབ་སེམས་དཔའ༌[^3677]ཕན་བཏགས་པ་ལ་གནོད་པ༌[^3678]བྱེད་པ་ལ་ཕྱི་མ་གསུམ་ཡིན་ཏེ། མི་འདོད་པའི་འབྲས་བུ་རྣམ་པར༌[^3679]སྨིན་པ་ཡིན་ཏེ། སེམས་ཀྱི༌[^3680]གོ་སྐབས་མེད་པ་ཉིད་དོ། །

[Block 5755]
བྱང་ཆུབ་སེམས་དཔའ་ལ་ནི་གནོད་པ་མེད་པའི་ཕྱིར་དང་། བསམ་པ་ངན་པ་མེད་པས༌[^3681]སྤྲེའུའི་ཚོགས་དེ་དག་གིས་བྱང་ཆུབ་སེམས་དཔའ་ལ་བརྫིས་པ་ཡིན་ན་ཡང་བྱང་ཆུབ་སེམས་དཔས་གནང་བ་ཉིད་ཡིན་གྱི། གཞན་དུ་མ་ཡིན་པས་མི་འདོད་པའི་འབྲས་བུ་མེད་པ་ཉིད་དོ། །

[Block 5756]
སྐྱེས་པའི་རབས་གཞན་དག་ཀྱང་སེམས་ཀྱི་གོ་སྐབས་མེད་པ་ཉིད་དོ། །

[Block 5757]
གོ་རིམས་དེ་ལྟར་བཀོད་པར་གྱུར་ན་ནི་བཟོད་པ་བསྒོམ་པ༌[^3682]ལ་འཇུག་པ༌[^3683]རྣམས་ཀྱི་བཟོད་པའི་རྣམ་པ་གོ་རིམས་བཞིན་དུ་བསྟན་པར་འགྱུར་ཏེ། དེ་སྒྲུབ་པའི༌[^3684]ཐབས་བསྟན་པར་རིགས་པ་ཡིན་ནོ། །

[Block 5758]
སྐྱེས་པའི་རབས་འདི་དག་གི་གོ་རིམས་འདི་བཞིན་དུ་རིག་པར༌[^3685]བྱ་སྟེ། གལ་ཏེ་ཕྱོགས་སུ་མི་འཛིན་པ་དག་ཡོད་ན་ཡང་འདི་བཞིན་དུ་གླེགས་བམ་དག་ཏུ་བྲི་བར་བྱའོ། །

[Block 5759]
བཟོད་པའི་ཚོམས༌[^3686]ཏེ་སྡེ་ཚན་གསུམ་པ་རྫོགས་སོ།། །།

[Block 5760 [HEADING]]
## བུ་ཟླ་བའི་སྐྱེས་པའི་རབས། ^34-0

[Block 5761]
ཇི་ལྟར་ཕྲད་ཀྱང་རུང་སྟེ་ཞེས་བྱ་བ་ནི་མི་དགེ་བ་མངོན་པར་འདོད་པའམ། དགེ་བ་མངོན་པར་འདོད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5762]
རབ་ཏུ་གྲགས་པའི་རིགས་དང་། དཔལ་དང་ལྡན་པ་ཞེས་བྱ་བ་འདི༌[^3687]གཉིས་ཀྱིས་ནི་གཙོ་བོའི་ནུས་པ་བསྟན་ཏོ། །

[Block 5763]
ཡོན་ཏན་ཡོངས་སུ་འཛིན་པར་བྱེད་པས་འབངས་རྣམས་ནི་གློ་བ་ཉེ་བ་ཞེས་བྱ་བ་འདིས་ནི་གསང་ཚིག་གི་ནུས་པ་བསྟན་ཏོ། །

[Block 5764]
གཟི་བྱིན་ཆེ་བས་རྒྱལ་ཕྲན་དྲེགས་པ་རྣམས་ཕྱག་འཚལ་བར་གྱུར་པ་ཞེས་བྱ་བས་ནི་སྤྲོ་བའི་ནུས་པ་བསྟན་ཏོ། །

[Block 5765]
ཡོན་ཏན་བརྒྱའི་འོད་ཟེར་གྱི་ཕྲེང་བ་ནི་ཡོན་ཏན་བརྒྱའི་འོད་ཟེར་གྱི་ཕྲེང་བའོ། །

[Block 5766]
འོད་ཟེར་བརྒྱ་དང་ལྡན་པ་གང་ལ་ཡོད་པ་དེ་ནི་ཡོན་ཏན་གྱི་འོད་ཟེར་བརྒྱ་དང་ལྡན་པའོ། །

[Block 5767]
ཟླ་བ་བཞིན་དུ་མཐོང་ན་དགའ་བ་གང་ཡིན་པ་དེ་ནི། ཟླ་བ་དང་འདྲ་བར་མཐོང་ན་དགའ་བའོ། །

[Block 5768]
དེ་ཉིད་ཀྱི་ཕྱིར། བུ་ཟླ་བ་ཞེས་བྱ་བ་ཡིན་ཏེ། ཟླ་བ་དང་འདྲ་བའི་ཕྱིར་བུ་ཟླ་བ་ཞེས་བཏགས་ཏེ། དེའི་མིང་ཡོན་ཏན་དང་ལྡན་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5769]
ལེགས་པར་ཕན་འདོགས་པ་ཞེས་བྱ་བས་ནི་མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་མི་སྐྱེད་པ་དང་། མི་དགེ་བའི་ཆོས་སྐྱེས་པ༌[^3688]རྣམས་སྤང་བ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5770]
སྡུད་པ་ལ་མཁས་པ་དང་། གུས་པ་ཇེ་ཆེ་ཇེ་ཆེར་གྱུར་པ་དང་། །ཞེས་བྱ་བས་ནི་དགེ་བའི་ཆོས་སྐྱེད་པ༌[^3689]དང་། སྐྱེས་ཟིན་པ་རྣམས་ཕྱིར་ཞིང་བསྒོམས་པ༌[^3690]ཉིད་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 5771]
ཡོངས་སུ་བསྐྱངས་པ་ལ་ངེས་པར་བྱེད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི༌[^3691]དགེ་བའི་ཆོས་རྣམས་བསྒོམ་པར་བྱའོ་ཞེས་བསྟན་ཏོ། །

[Block 5772]
དེ་ཉིད་ཀྱི་ཕྱིར་སྐྱེས་པའི་རབས་འདི་ནི་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་པའི་ཕྱིར་ཡིན་ཏེ། མི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་མི་སྐྱེད་པ་དང་། སྐྱེས་ཟིན་པ་རྣམས་སྤངས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5773]
[^3692]མི་དགེ་བའི་ཆོས་སྤངས་པ་མེད་པར་ནི་དགེ་བའི་ཆོས་སྐྱེད་པ༌[^3693]དང་། འཕེལ་བ་དང་། གནས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 5774]
ཡོན་ཏན་གཉེན་དང་འདྲ་བར་གྱུར་ཏོ་ཞེས་བྱ་བ་བསྟན་པ་ལ། འགྲོ་བ་རྣམས་ཀྱི༌[^3694]གཉེན་དེ་གང་ཡིན་ཞེ་ན། གཉེན་དང་འདྲ་བ་དེ་ཉིད་བསྟན་པའི་ཕྱིར། ཚུལ་ཁྲིམས་ཐོས་དང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5775]
ཡང་ན་གཞན་དང་མངོན་པར་འབྲེལ་པས་ཡོན་ཏན་གྱི་འོད་ཟེར་བརྒྱ་དང་ལྡན་པ་ཞེས་བཤད་པའི་ཡོན་ཏན་གང་དག་ཡིན་ཞེ་ན། ཚུལ་ཁྲིམས་ཐོས་དང་གཏོང་དང་སྙིང་རྗེ་དུལ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5776]
དེ་དང་དེ་དག་ཅེས་བྱ་བ་ནི་ཡོན་ཏན་གཞན་དག༌[^3695]ཡང་ལྡན་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5777]
ཡོན་ཏན་ཡོད་པ་ནི་ཞེས་བྱ་བ་ནི་ཡོན་ཏན་ཉིད་ཡོད་པ་ཡིན་ཏེ།

[Block 5778 [VERSE]]
དེའི་ཡོན་ཏན་མང་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
ལང་ཚོར་གྱུར་པའི་རྒྱན་གྱིས་བརྒྱན་པ་བཞིན། །

[Block 5779]
ཞེས་བྱ་བ་ནི། བྱང་ཆུབ་སེམས་དཔའི་རྒྱན་གྱིས་བརྒྱན་པའི་ལང་ཚོ་བཞིན་དུ་ཞེས་བྱ་བའི་དོན་ཏེ། [^3696]ལང་ཚོ་ནི་ད་ལྟར་བྱུང་བའི་ཡོན་ཏན་གྱིས་མཛེས་པ་ཡིན་ཏེ། དེ་བས་ན་ཡོན་ཏན་ལང་ཚོའི་རྒྱན་གྱིས་བརྒྱན་པ་ཉིད་དོ། །

[Block 5780]
ཡང་ན་ལང་ཚོར་གྱུར་པའི་རྒྱན་གྱིས་བརྒྱན་པ་བཞིན་དུ་ཡོན་ཏན་གསར་པ་དག་གིས་རབ་ཏུ་བརྒྱན་པ་སྟེ། དེ་བས་ན་ལང་ཚོར་གྱུར་པའི་རྒྱན་གྱིས་བརྒྱན་པ་ཞེས་བརྗོད་དོ། །
--- END BLOCKS ---
