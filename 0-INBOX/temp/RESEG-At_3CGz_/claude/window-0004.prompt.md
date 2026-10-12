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
[Block 141]
སངས་རྒྱས་སུ་འདུ་ཤེས་པ་ལ་སངས་རྒྱས་མཐོང་བ་མེད་ན། སངས་རྒྱས་ལ་མཆོད་པར་འགྱུར་བ་ལྟ་ཅི་སྨོས་དེ་ནི་གནས་མེད་དོ། །

[Block 142]
དེ་ལ་སངས་རྒྱས་ལ་མཆོད་པ་གང་ཞེ་ན། གང་འདུ་ཤེས་ཀྱི་མཚན་མ་མི་སྐྱེད་པའོ། །

[Block 143]
གང་ལ་སེམས་མེད་པ་དང་། སེམས་ལས་བྱུང་བ་མེད་པ་དང་། སངས་རྒྱས་སུ་འདུ་ཤེས་པ་མེད་པ་དང་། ཆོས་སུ་འདུ་ཤེས་པ་མེད་པ་དང་། དགེ་འདུན་དུ་འདུ་ཤེས་པ་མེད་པ་དང་། གང་ཟག་དང་། བདག་དང་། ཕ་རོལ་པོར་འདུ་ཤེས་པ་མེད་པ་ནི་དེ་བཞིན་གཤེགས་པ་ལ་མཆོད་པ་ཡིན་ནོ་ཞེས་གསུངས་ཏེ། འདིའི་དོན་རྒྱས་པར་མདོ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 144]
དེ་བས་ན་འཕགས་པ་ཐོགས་མེད་ཀྱི༌[^66]ཞལ་སྔ་ནས། སངས་རྒྱས་བཅོམ་ལྡན་འདས་དེ་ནི་སྒྲུབ་པའི་མཆོད་པས་མཉེས་པར་འགྱུར་གྱི། ཟང་ཟིང་གི་མཆོད་པས་ནི་དེ་མཉེས་པར་མི་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡང་ལེགས་པར་དྲངས་པར་འགྱུར་རོ། །

[Block 145]
དེ་བས་ན་སངས་རྒྱས་ནི་ཆོས་ཀྱི་སྐུས་གནས་པ་ཡིན་ཏེ།

[Block 146]
སངས་རྒྱས་ཕལ་པོ་ཆེའི་ལེའུ་ལས།

[Block 147 [VERSE]]
སངས་རྒྱས་རྣམས་ནི་ཆོས་ཀྱི་སྐུ། །
དེ་བཞིན་གཤེགས་པ་སྐྱེ་བ་མེད། །
རྣམ་དག་ནམ་མཁའ་ལྟ་བུ་སྟེ། །

[Block 148]
ཞེས་གསུངས་པ་དང་། འཕགས་པ་ནམ་མཁའ་མཛོད་ཀྱི་མདོ་ལས་ཀྱང་། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ནི་ཆོས་ཉིད་དུ་ཡང་མི་དམིགས་ན། གཟུགས་དང་མཚན་ཉིད་དུ་ལྟ་དམིགས་པར་ག་ལ་འགྱུར་ཞེས་གསུངས་སོ། །

[Block 149]
སློབ་དཔོན་འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་ནས་ཀྱང་།

[Block 150 [VERSE]]
ཆོས་རྣམས༌[^67]ཐམས་ཅད་སྟོང་པ་ལ། །
གང་ལ་བསྟོད་ཅིང་གང་གིས་བསྟོད། །
སྐྱེ་དང་འཇིག་པ་རྣམ་སྤངས་ཤིང་། །
གང་ལ་མཐའ་དང་དབུས་མེད་པ། །

[Block 151]
གཟུང་དང་འཛིན་པ་མི་མངའ་བའི། །འདིར་ནི་ཁྱེད་བསྟོད་ནུས་པ་གང་། །ཞེས་གསུངས་སོ། །

[Block 152]
དེ་ལྟ་བུའི་མཆོད་པའི་བྱེ་བྲག་ནི་བྱང་ཆུབ་སེམས་དཔའ་དབང་པོ་རྟུལ་པོ་དང་རྣོན་པོའི་བྱེ་བྲག་གིས་དེ་དང་དེ་ཤེས་པར་བྱའོ། །

[Block 153]
རྩ་བ་ཉིད་ལ་འཇུག་པར་བྱ་སྟེ།

[Block 154 [VERSE]]
བྱང་ཆུབ་སྙིང་པོའི་མཐར་ཐུག་པར། །
མི་ལྡོག་པ་ཡི་སེམས་ཀྱིས༌[^68]སུ། །

[Block 155]
ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། བྱང་ཆུབ་སྙིང་པོ་ནི་དྲང་བའི་དོན་དུ་དཔལ་རྡོ་རྗེའི་གདན་བྱང་ཆུབ་ཆེན་པོའི་གནས་དང་། འོག་མིན་གྱི་གནས་དཔལ་སྟུག་པོ་བཀོད་པའི་ཞིང་ངོ་། །དེ་དག་ཏུ་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་བརྙེས་པས་ན་སྙིང་པོའོ། །

[Block 156]
ངེས་པའི་དོན་དུ་ཏིང་ངེ་འཛིན་དེ་བརྙེས་པའི་གནས་འདི་ཡིན་བྱ་བ་མེད་དེ། དོན་དམ་པར་ཆོས་ཐམས་ཅད་ཀྱི་དབྱིངས་ཉིད་ཡིན་པས་སོ། །

[Block 157]
འཕགས་པ་ནམ་མཁའ་མཛོད་ཀྱི་མདོ་ལས།

[Block 158]
བྱང་ཆུབ་སྙིང་པོ་ནམ་མཁའ་སྟེ། །བྱང་ཆུབ་ནམ་མཁའི་མཚན་ཉིད་ཡིན།[^69] །

[Block 159]
ཞེས་གསུངས་སོ། །

[Block 160]
མི་ལྡོག་པ་ཡི་སེམས་ཀྱིས༌[^70]སུ། ། ཞེས་བྱ་བ་ནི་འདིར་ཕྱིར་མི་ལྡོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་རྣམ་པ་གསུམ་སྟེ། སྦྱོར་བའི་ལམ་ནས་མི་ལྡོག་པ་དང་། བདེན་པ་མཐོང་བ་ནས་མི་ལྡོག་པ་དང་། ས་བརྒྱད་པ་ནས་མི་ལྡོག་པའོ། །

[Block 161]
འདིའི་དོན་ནི་འཕགས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་མན་ངག་གི་བསྟན་བཅོས་མངོན་པར་རྟོགས་པའི་རྒྱན་ལས་རྒྱས་པར་བལྟ་བར་བྱའོ། །

[Block 162]
གཞན་ཡང་སོ་སོའི༌[^71]སྐྱེ་བོ་ཉིད་ནས་ཕྱིར་མི་ལྡོག་པ་དང་། བདེན་པ་མཐོང་བ་ནས་ཕྱིར་མི་ལྡོག་པ་དང་། ས་བདུན་པ་ནས་ཕྱིར་མི་ལྡོག་པའོ། །

[Block 163]
འདིའི༌[^72]དོན་སློབ་དཔོན་དཔལ་ཡེ་ཤེས་གྲགས་པས་མཛད་པའི་དེ་ཁོ་ན་ཉིད་ལ་འཇུག་པའི་བསྟན་བཅོས་ཆེན་པོར་གསལ་བར་མཛད་པ་དེར་བལྟ་བར་བྱའོ། །

[Block 164]
ཡང་ན་ཕྱིར་མི་ལྡོག་པ་ནི་བཞི་སྟེ། སེམས་བསྐྱེད་པ་ནས་ཕྱིར་མི་ལྡོག་པ་དང་གསང་སྟེ་ཕྱིར་མི་ལྡོག་པ་དང་། བཟོད་པ་ཐོབ་ནས༌[^73]ཕྱིར་མི་ལྡོག་པའོ། །

[Block 165]
དང་པོར་སྐྱབས་འགྲོ་ལན་གསུམ་བྱ་ཞེས་བྱ་བ་ནི་དཀོན་མཆོག་གསུམ་རེ་རེ་ལ་ལན་གསུམ་གསུམ་བྱ་བའོ།[^74] །

[Block 166 [HEADING]]
## སྐྱབས་སུ་འགྲོ་བའི་དོན་བསྡུས། ^2-0

[Block 167]
སྐྱབས་སུ་འགྲོ་བའི་དོན་བསྡུས་ནས་སྨྲས་པ།

[Block 168 [VERSE]]
གནས་དང་རྟེན་དང་བསམ་པ་དུས། །
བསླབ་པ་རང་བཞིན་ཚད་དང་ཚུལ། །
བྱ་བ་དབྱེ་བ༌[^75]ངེས་ཚིག་དབྱེ། །
ཉེས་དམིགས་དགོས་པ་ཕན་ཡོན་ཡིན། །

[Block 169 [HEADING]]
### གནས། ^2-1-0

[Block 170]
འདིར་སྐྱབས་སུ་འགྲོ་བའི་ཚུལ་བརྗོད་པར་བྱ་སྟེ། སྐྱེས་བུ་འགའ་ཞིག་འཁོར་བའི་སྡུག་བསྔལ་ལས་ཡིད་ངེས་པར་བྱུང་བ། རྟག་ཏུ་འཆི་བ་རྗེས་སུ་དྲན་པ། རང་བཞིན་གྱིས༌[^76]སྙིང་རྗེ་དང་ཤེས་རབ་ཆེ་བ། སོ་སོར་ཐར་པའི་རིས་བདུན་པོ་ལས་གང་ཡང་རུང་བའི་ཚུལ་ཁྲིམས་ལ་སྐྱོན་མེད་པར་གནས་པ་དེ་གལ་ཏེ་ཁྱིམ་པ་ཞིག་ཡིན་ན་ནི་དགེ་བསྙེན་གྱི་བསླབ་པར་གྱུར་པ་བསླབ་པའི་གཞི་ལྔ་དང་། དེའི་ཕྱོགས་སུ་གཏོགས་པ་བསླབ་པ་བཞི་བཅུ་རྩ་ལྔ་དང་ལྡན་པ་དང་། དེ་རབ་ཏུ་བྱུང་བ༌[^77]ཞིག་ཡིན་ན་ནི་རང་གི༌[^78]བསླབ་པའི་ཚུལ་དང་། ཇི་ལྟར་ཉན་ཐོས་ཀྱི་སར་བཤད་པའི་དགེ་སྦྱོང་གི་རྒྱན་དང་། སྦྱངས་པའི་ཡོན་ཏན་དང་། གཞན་ཡང་རྟེན་བཞི་དང་། ཚུལ་བཞི་ལ་སོགས་པ་དང་། གཞན་ཡང་ཆོ་ག་དང་། སྤྱོད་ལམ་དང་། འཚོ་བ་དང་། ཚུལ་ཁྲིམས་དང་། ལྟ་བ་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པ་དང་། གཞན་ཡང་ནམ་གྱི་ཆ་སྟོད་དང་ཆ་སྨད་ལ་མི་ཉལ་བར་རྣལ་འབྱོར་ལ་བརྩོན་པ་དང་། ཟས་ཀྱི་ཚོད་རིག་པ་དང་། དབང་པོ་རྣམས་ཀྱི་སྒོ་བསྡམས་པ༌[^79]དང་། ཁ་ན་མ་ཐོ་བ་ཕྲ་རབ་ཙམ་ལ་ཡང་འཇིགས་པར་ལྟ་བའི་སྐྱེས་བུ་དེ་འདི་སྙམ་དུ་མ་ལ་སོ་སོར་ཐར་པའི་ཚུལ་ཁྲིམས་འདི་ཙམ་གྱིས༌[^80]ནི་བདག་དང་གཞན་གྱི་དོན་མཐར་ཕྱིན་པར་མི་འགྱུར་ན། ཇི་ལྟར་ན་བདག་དང་གཞན་གྱི་དོན་མཐར་ཕྱིན་པར་འགྱུར་ཞིག་གུ། འདི་ལྟར་ཐེག་པ་ཆེན་པོ་ཞེས་བྱ་བ་བདག་དང་གཞན་གྱི་དོན་མཐར་ཕྱིན་པར་བྱེད་པ་ཞིག་ཡོད་ཅེས་གྲག་གི །[^81]དགེ་བའི་བཤེས་གཉེན་དམ་པ་ཅིག་ལས་བཙལ་བར་བྱའོ་ཞེས་བསམས་ནས་བླ་མར་འོས་པའི་དམ་པ་དེ་ཡུན་རིང་དུ་ཡོངས་སུ་མཉེས་པར་བྱས་ཏེ། དེ་མཉེས་པར་གྱུར་ནས་དེའི་ཞབས་གཉིས་ལ་མགོ་བོས་གཏུགས་ཏེ་འདི་སྐད་དུ་སྐྱེས་བུ་དམ་པ་ཁྱོད་བདག་ལ་ཐུགས༌[^82]བརྩེ་བར་མཛད་དུ་གསོལ། བདག་ལ་བདག་དང་གཞན་གྱི་དོན་མཐར་ཕྱིན་པར་བྱེད་པའི་ཐབས་ཐེག་པ་ཆེན་པོའི་ལམ་དེ་སྩལ་དུ་གསོལ་ཞེས་གཡོ་སྒྱུ་དང་བྲལ་བའི་སེམས་ཀྱིས༌[^83]ཞུ་བར་བྱའོ། །

[Block 171]
དེ་ནས་དགེ་བའི་བཤེས་གཉེན་དེས་སློབ་མ་དེ་བརྟག་པ་གསུམ་གྱིས་བརྟགས་ཏེ། [^84]འདི་ལྟར་སྤྱོད་ལམ་དང་། རྨི་ལམ་དང་། འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་ལྷའི་པྲ་དབབ་པས་བརྟགས་ལ་དེ་སྣོད་དུ་འདུག་པར་ཤེས་ནས་བླ་མ་དེ་ཡིད་དགའ་བ་དང་། བཞིན་འཛུམ་པ་དང་། ཟང་ཟིང་དང་། རྙེད་པ་དང་། བཀུར་སྟི་དང་བྲལ་བའི་སེམས་དང་སློབ་མ་དེ་ལ་སྙིང་བརྩེ་བའི་སེམས་ཀྱིས་སྡིག་པ་ཅན་གྱི་སྐྱེ་བོས་དབེན་པའི་ས་ཕྱོགས་སུ་ས་གཞི་ལེགས་པར་འཐས་པར་བྱས་ལ་གཙང་བ་དེར་བའི་རྣམ་ལྔས་སྐྱང༌[^85]ནུལ་དང་བྱུག་པ་བྱས་ལ། ཙནྡན་ལ་སོགས་པའི་དྲི་ཕུལ་དུ་བྱུང་བས་ཀྱང་བྱུགས་ཤིང༌[^86]དེར་དྲི་ཞིམ་པོའི་མེ་ཏོག་སིལ་མས༌[^87]གཏོར་བར་བྱའོ། །

[Block 172 [HEADING]]
### རྟེན། ^2-2-0

[Block 173]
དེར་དཀོན་མཆོག་གསུམ་གྱི་གཟུགས་བརྙན་ལུགས་མ་ལ་སོགས་པ་དང་། པོ་ཏི་ལ་སོགས་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཁྲིའམ་སྟེགས་བུ་ལ་བཞུགས་པར་བྱའོ། །

[Block 174]
དེར་བླ་རེ་ལ་སོགས་པ་དང་། མེ་ཏོག་ལ་སོགས་པའི་མཆོད་པའི་ཡོ་བྱད་ཇི་ལྟར་འབྱོར་པ་དང་། རོལ་མོའི་བྱེ་བྲག་དང་། ཞལ་ཟས་དང་། རྒྱན་ཆ་ལ་སོགས་པ་སྟ་གོན་བྱེད་དུ་བཅུག་ལ། དེ་ནས་སློབ་མ་དེས་གདན་ཁྲི་མེ་ཏོག་གིས་བརྒྱན་པའི་སྟེང་དུ་དགེ་བའི་བཤེས་གཉེན་བཞུགས་སུ་གསོལ་ལ།

[Block 175 [HEADING]]
### བསམ་པ། ^2-3-0

[Block 176]
འདི་སྙམ་དུ་འདི་ནི་འགྲོ་བ་མ་ལུས་པའི་སྐྱབས་དང་དཔུང་གཉེན་ཡིན་ནོ་སྙམ་དུ་བླ་མ་ལ་སྟོན་པའི་འདུ་ཤེས་བསྐྱེད་ལ། ཁྲུས་བྱས་ཏེ་གོས་གཙང་མ་བགོས་ལ་བསམ་པ་བཟང་པོ་དང་ལྡན་པས་འདི་སྐད་དུ་རིགས་ཀྱི་བུ་ཁྱོད་མཁྱེན་པར་མཛད་དུ་གསོལ། བདག་འཁོར་བའི་གནས་འདིར་ཐོག་མ་མེད་པའི་དུས་ནས་སྡུག་བསྔལ་དུ་མས་གཙེས་ཤིང་ཤིན་ཏུ་ཉམ་ཐག་པར་གྱུར་ཏེ། མགོན་མ་མཆིས་པ། སྐྱབས་མ་མཆིས་པ། དཔུང་གཉེན་མ་མཆིས་པ། བདག་གི༌[^88]མགོན་དང་སྐྱབས་དང་དཔུང་གཉེན་མཛད་དུ་གསོལ་ཞེས་ལན་གསུམ་དུ་བྱའོ། །

[Block 177]
དེ་ནས་བླ་མ་དེས་འདི་སྐད་དུ་སྐྱེས་བུ་ཁྱོད་འཁོར་བ་ལས་སྐྱོ་ཞིང་ཡིད་བྱུང་བས་ཤིང་རྟ་ཆེན་པོའི་ལམ་ལ་འཇུག་པར་འདོད་པ་ཤིན་ཏུ་ལེགས་སོ། །

[Block 178]
འདི་ལྟར་ཤེས་པར་གྱིས་ཤིག །དཀོན་མཆོག་གསུམ་ཞེས་བྱ་བ་མགོན་མེད་པ་དང་། སྐྱབས་མེད་པ་དང་། དཔུང་གཉེན་མེད་པ་དག་གི༌[^89]མགོན་དང་། སྐྱབས་དང་དཔུང་གཉེན་དུ་གྱུར་པ་ཡོད་ཀྱི།[^90] ཁྱོད་དང་བའི་ཡིད་དང་། ཤིན་ཏུ་སྤྲོ་བའི་ཡིད་ཀྱིས་འགྲོ་བ་མཐའ་དག་ཡུལ་དུ་བྱས་ཏེ། དེ་ལས་སྐྱབས་སུ་འགྲོ་བ་གྱིས་ཤིག །དེ་ལ་སྲི༌[^91]ཞུ་དང་། བསྙེན་བཀུར་ཚུལ་བཞིན་དུ་བྱ་བའི་ཕྱིར་མཆོད་པའི་ཡོ་བྱད་འབྱོར་པ་ཅི་ཡོད་པས་ཚོགས་པར་གྱིས་ཤིག་ཅེས་བརྗོད་པར་བྱའོ། །

[Block 179]
དེ་ནས་སློབ་མ་དེས་པུས་མོ་གཉིས་ས་ལ་བཙུགས་ཤིང་ཐལ་མོ་སྦྱར་ནས་མེ་ཏོག་ཕུལ་ཏེ། འདི་སྐད་དུ།

[Block 180 [VERSE]]
སྐྱེས་བུ་གཙོ་བོ་དགོངས་སུ་གསོལ། །
ཐོག་མ་མེད་ནས་འདི་བར་དུ། །
བདག་ནི་འཁོར་བར་འཁོར་གྱུར་ཏེ། །
སྡུག་བསྔལ་རྣམས་ཀྱིས༌[^92]ཤིན་ཏུ་དུབ། །
--- END BLOCKS ---
