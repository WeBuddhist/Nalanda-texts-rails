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
[Block 71]
དེ་ནས་ཁྱད་པར་གྱི་སྐྱབས་འགྲོ་ལ་བརྟེན་ནས་བྱང་ཆུབ་ཀྱི་སེམས་བརྟན་དུ་གཞུག །དེ་ནས་འཇུག་པའི་སྡོམ་པ་ལེགས་པར་བྱིན་ལ་དབང་བཞིའི་སྒོ་ནས་ལྟ་སྤྱོད་སྒོམ་གསུམ་གྱི་རྟོགས་པ་བསྒྲུབ༌[^41]པོ། །དེ་ནས་རྟོག་པ༌[^42]དང་མཐུན་པའི་ལམ་ལ་སྦྱར་ཏེ། དེ་ཡང༌[^43]བསྐྱེད་པའི་རིམ་པའི་དུས་སུ་བླ་མ་དང་ལྷ་ཐ་མི་དད་པ་ལ་ཚོགས་བསགས།[^44] ལྟུང་བ་དང་པོའི་རྒྱུ་སྤངས། གོ་རིམས༌[^45]དེ་རྣམས་དབང་པོ་རབ་ཀྱིས༌[^46]ཆོས་ཐམས་ཅད་ཟུང་འཇུག་ཏུ་རྟོགས་པ་སྒྲུབ་པའི་ཐབས་སུ་ཤེས་པར་བྱའོ། །

[Block 72]
འབྲིང་དང་ཐ་མས་ཐ་མལ་པའི་རྟོག་པ་ཟློག༌[^47]པའི་ཐབས་སུ་ཤེས་པར་བྱ་བའི་ཕྱིར་ཕྱིན་ཅི་མ་ལོག་པས་ལྟུང་བ་གཉིས་པ་དང་བདུན་པ་དང་བརྒྱད་པ་དང་དྲུག་པ་དང་བཅུ་གཉིས་པའི་རྒྱུ་སྤངས། ཐུན་མོང་གི་ལམ་བྱམས་པ་དང་སྙིང་རྗེ་བྱང་ཆུབ་ཀྱི་སེམས་དང་ལྡན་པ་དང་། ཐུན་མོང་མ་ཡིན་པའི་ལམ་རྣལ་འབྱོར་དང་བདག་དང་གནས་བསྲུང་བས་ལྟུང་བ་གསུམ་པ་དང་བཞི་པ་དང་ལྔ་པ་དང་དགུ་པ་དང་བཅུ་པའི་རྒྱུ་སྤངས། དེ་ནས་རྫོགས་པའི་རིམ་པ་ལ་བརྟེན་ནས་ཆོས་ཐམས་ཅད་འོད་གསལ་དུ་རྟོགས་པ་བསྒྲུབས་ནས། བདུད་རྩི་ལྔ་ལ་སོགས་པའི་དམ་ཚིག་བརྟེན་པས་བཅུ་གསུམ་པ་དང་བཅུ་བཞི་པ་དང་བཅུ་གཅིག་པའི་རྒྱུ་སྤངས། ཡང་ན་ལྷ་ལ་གསང་བ་དང་ཤེས་རབ་དང་བཞི་པ་བླངས་པས༌[^48]བཅུ་བཞི་པ་དང་བཅུ་གསུམ་པའི་རྒྱུ་སྤངས། དེ་ལྟར་ན་བཅུ་བཞི་པོ་རྣམས་མཉམ་གཞག་གི༌[^49]ལས་ཀྱི་རིམ་པ་ལས༌[^50]འདུས་པས་རྗེས་ཀྱིས་ཀྱང་དེའི་བདག་ཉིད་དུ་བྱ་དགོས་པའི་ངེས་པ་བསྐྱེད་ཅིང་བརྟན་པར་བྱའོ། །

[Block 73 [HEADING]]
## དངོས་གཞིའི་དབང་དུ་བྱས་ནས་ལྟུང་བ་རེ་རེ། ^2-0

[Block 74]
དངོས་གཞིའི༌[^51]དབང་དུ་བྱས་ནས་ལྟུང་བ་རེ་རེ་ལ་ལྟུང་བའི་ངོས་འཛིན་དང་རྐྱེན་གང་གིས་བྱུང་བ་དང་། ཉེས་པ་དང་། ཚུལ་ཇི་ལྟར་མི་འབྱིན་པའི་ཐབས་སོ། །

[Block 75]
བདེ་གཤེགས་བཀའ་ནི་འཁོར་བའི་ཉེས་པ་ནས་བྱས་ཞེས་དང་། བྱས་གཟོ་དང་། བྱམས༌[^52]སྙིང་རྗེ་དང་འཇུག་པའི་སྡོམ་པའི་བར་དུ༌[^53]བརྟན་པར་བྱ་བ་དང་། ཁྱད་པར་ཅན་དབང་རྣམ་པ༌[^54]བཞིས་སྣོད་དུ་བསྒྲུབས་ནས་ལྟ་བ་ལ་སོགས་པའི་མན་ངག་ནི་བདེ་གཤེགས་ཀྱི་བཀའོ། །

[Block 76]
འདས་པ་ནི་མ་གུས་པ་དང་། བག་མེད་པ་དང་། མི་ཤེས་པ་དང་། ཉོན་མོངས་པ་མང་བའི་དབང་གིས་སོ། །

[Block 77]
དེས་ན་བླ་མའི་སྤྱན་སྔར་དམ་བཅས་པ་བརྟན་པར་མི་བྱེད་པར་ཉིན་མཚན་གྱི་ཆ་འདས་པ་ནི་ལྟུང་བའོ། །

[Block 78]
རྐྱེན་ནི་མ་དད་པ་ལ་སོགས་པ་བཞིའོ། །

[Block 79]
ཉེས་པ་ནི་སྔར་ཡམས་དང་ཞེས་པའི་ཚིགས་སུ་བཅད་པ་བཞི་སྟེ། བླ་མའི་སྐབས་སུ་བཀའ་ལས་འདས་པ་དང་ཤེས་རབ་སྨོད་པ་ཞེས་རེ་རེ་ལ་སྦྱར་རོ། །

[Block 80]
མི་འབྱུང་བའི་ཐབས་ནི་བླ་མས་བསྟན་པའི་ལམ་དྲན་པ་དང་ཤེས་བཞིན་གྱིས༌[^55]མར་མེ་དང་ཆུའི་རྒྱུན་ལྟར་ཡིད་ལ་བྱའོ། །

[Block 81]
སྤུན་ནི་སྦྱོར་བ་གཅིག་པ་དང་། དེ་ལས་གཞན་པ་དང་སེམས་ཅན་མཐའ་དག་གོ། །

[Block 82]
ཉེས་པ་བརྗོད་པའི་ཡུལ་ལ་བརྡ་ཕྲད་ཅིང་ཉིན་མཚན་གྱི་སུམ་ཆ་འདས་ན་ལྟུང་བའོ། །

[Block 83]
རྐྱེན་ནི་ཡུལ་གསུམ་པོ་གང་ཡང་རུང་བས་སེམས་དང་མཐུན་པར་མ་བྱས་པ་དང་། མི་བྱེད་པའི་དབང་གིས་ཞེ་སྡང་དང་ཕྲག་དོག་གམ་ཉོན་མོངས་པ་གང་ཡང་རུང་བ་དང་མཚུངས་པར་ཁྲོ་བའོ། །

[Block 84]
མི་འབྱིན་པའི་ཐབས་ནི་ཁྲོ་བའི་རྐྱེན་ཉེ་བར་གནས་པའི་ཚེ་བྱས་པ་ཤེས་པ་ལ་སོགས་པ་བྱམས་པ་ཡིད་ལ་བྱ་བ་དང་། ཡང་ན་ཆོས་ཐམས་ཅད་སྐྱེ་མེད་དུ་ཡིད་ལ་བྱ་བའོ། །

[Block 85]
བྱམས་པ་ནི་བྱས་པ་ཤེས་པའི་སྒོ་ནས་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པར་འདོད་པའོ། །

[Block 86]
སྤོང་བ་ནི་ཕན་པ་མ་ཡིན་པར་བསྒྲུབས་པས་ཉིན་མཚན་གྱི་ཆ་འདས་ན་ལྟུང་བའོ། །

[Block 87]
རྐྱེན་ནི་གོང་མ་ལྟར་ཡུལ་གསུམ་ལ་བརྟེན་ནས་བདག་གི་བསམ་པ་དང་མཐུན་པར་མི་བྱེད་པ་དང་། མ་བྱས་པའི་དབང་གིས་ཕན་པ་མ་ཡིན་པ་བསྒྲུབ༌[^56]ཅིང་སྤོང་བའོ། །

[Block 88]
མི་འབྱུང་བའི་ཐབས་ནི་རྐྱེན་ཉེ་བར་གནས་པའི་དུས་སུ་དེ་ལ་ཆེད་དུ་གཏད་པའི་ཚུལ་གྱིས་བྱམས་པ་ཡིད་ལ་བྱ་བའམ་ཟུང་འཇུག་ཏུ༌[^57]ཤེས་པར་བྱའོ། །

[Block 89]
བྱང་ཆུབ་ཀྱི་སེམས་ནི་སེམས་ཅན་གྱི་དོན་དུ་རྡོ་རྗེ་འཆང་འདོད་པའོ། །

[Block 90]
དེ་སྤོང་བ་ནི་ཡུལ་གྱི་དབང་གིས་གསུམ་སྟེ། བླ་མ་དང་རྡོ་རྗེ་སྤུན་དང་སེམས་ཅན་ལ་གཡོ་སྒྱུ་སྤྱོད་པས་ཡོན་ཏན་ཐོབ་པར་བྱ་སྙམ་པ་དང་། དོན་དོར་བར་ཉིན་མཚན་གྱི་ཆ་འདས་པའོ། །

[Block 91]
རྐྱེན་ནི་སྔ་མ་ལྟར་རོ། །

[Block 92]
མི་འབྱིན་པའི་ཐབས་ནི་མི་མཐུན་པའི་རྐྱེན་ཉེ་བར་གནས་པའི་དུས་སུ་ཕན་ཡོན་དང་ཉེས་དམིགས་ཤེས་པས་བྱང་ཆུབ་ཀྱི་སེམས་བསྒོམ་པར་བྱའོ། །

[Block 93]
ཡང་ན་སྐྱེ་བ་མེད་པ་ཡིད་ལ་བྱའོ། །

[Block 94]
རང་གི་གྲུབ་པའི་མཐའ་ནི་ཐེག་པ་ཆེན་པོ་རྣམ་པ་གཉིས་སོ། །

[Block 95]
གཞན་གྱི་ནི་ཉན་ཐོས་དང་བསེ་རུའོ། །

[Block 96]
ཧེ་བཛྲ་འདུས་པའི་ལེའུ་ལྟར་རིམ་གྱིས་མི་སྦྱོང་བར་སྨོད་པས་ཉིན་མཚན་འདས་པའོ། །

[Block 97]
རྐྱེན་ནི་བླ་མ་དམ་ཚིག་ཉམས་པ༌[^58]དང་བྲལ་བ་རྣམས་དང་ཕྲད་པས་ལམ་རིམ་གྱིས་སྦྱང་བ༌[^59]རྣམས་ལ་སྨོད་ཅིང་ཁྲོ་བའོ། །

[Block 98]
མི་འབྱིན་པའི་ཐབས་ནི་བློ་རིམ་གྱིས་བསླབས་པས༌[^60]ཐེག་པ་གཅིག་ཏུ་ཤེས་པར་བྱའོ། །

[Block 99]
ཡོངས་སུ་མ་སྨིན་པ་ནི་ལམ་རིམ༌[^61]གྱིས་མ་སྦྱངས་པའོ། །

[Block 100]
གསང་བ་ནི་གྲུབ་པ་གནས་པའི་དོན་ནམ་མཁའ་དང་འདྲ་བར་ལྟ་བ་གཉིས་སོ། །

[Block 101]
སྒྲོགས་པ་ནི་ལུས༌[^62]ངག་གི་སྦྱོར་བས་ཉིན་མཚན་འདས་ནའོ། །

[Block 102]
རྐྱེན་ནི་མ་སྦྱངས་པ་དང་ཕྲད་པའི་དབང་གིས་སོ། །

[Block 103]
མི་འབྱིན་པའི་ཐབས་ནི་ཡུལ་དེ་ལྟ་བུ་དང་ཕྲད་པ་ན་བློའི་བྱེ་བྲག་དྲིས་ནས་དེ་དང་མཐུན་པར་བྱའོ། །

[Block 104]
ཕུང་པོ་སྨོད་པ་ནི་བསྐྱེད་པའི་གོ་རིམས༌[^63]མཐའ་དག་གཟུང་ངོ་། །སྨོད་པ་ནི་དེ་མ་བསྒོམས༌[^64]པར་ཉིན་མཚན་འདས་ནའོ། །

[Block 105]
རྐྱེན་ནི་ཟབ་མོ་སྟོན་པའི་ལུང་དང་ཡོངས་སུ་འཛིན་པ་ངན་པ་ལགས༌[^65]སོ། །

[Block 106]
མི་འབྱིན་པའི་ཐབས་ནི་ལྷ་སྒོམ་པའོ། །

[Block 107]
རང་བཞིན་དག་པ་ནི་ལྟ་བ་གཉིས་སོ། །

[Block 108]
སོམ་ཉི་ཟ་བ་ནི་དེ་གཉིས་ཀྱི་རྟོག་པ༌[^66]མ་སྐྱེས་པའོ། །

[Block 109]
དེའི་བདག་ཉིད་དུ་རྟོག་པ༌[^67]མེད་པར་ཉིན་མཚན་འདས་ནའོ། །

[Block 110]
རྐྱེན་བླ་མ་དམ་པ་དང་བྲལ་བས་དངོས་པོར་ལྟ་བའི་དབང་གིས་སོ། །
--- END BLOCKS ---
