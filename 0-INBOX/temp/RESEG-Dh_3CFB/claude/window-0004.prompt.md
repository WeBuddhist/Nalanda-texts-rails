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
དེའི་ལྡོག་པ་དེ་ནི་མ་ངེས་པས་མི་མཐུན་པའི་ཕྱོགས་ལ་འཇུག་པར་ཐེ་ཚོམ་ཟ་བར་འགྱུར་ཏེ། ལྡོག་པ་སྒྲུབ་པ་མ་མཐོང་བ་ཙམ་ནི་ཐེ་ཚོམ་གྱི༌[^84]རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 142]
མི་དམིགས་པ་ཐམས་ཅད་ནི་རྟོགས་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 143]
དེའི་ཕྱིར་གཅིག་ལོག་པས་གཞན་ལྡོག་པར་འདོད་པས་ནི་དེ་གཉིས་རང་བཞིན་འབྲེལ་པ་འགའ་ཞིག་ཀྱང་འདོད་པར་བྱ་དགོས་སོ། །

[Block 144]
དེ་ལྟ་མ་ཡིན་ན་གཏན་ཚིགས་གོ་བར་བྱེད་པ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 145 [VERSE]]
གཏན་ཚིགས་ཀྱི་ནི་ཚུལ་གསུམ་ལའང་། །
དེ་ཡིས༌[^85]མ་གྲུབ་བཟློག་དོན་དང་། །
འཁྲུལ་པ་ཅན༌[^86]གྱི་གཉེན་པོར་ནི། །
ངེས་པ་བརྗོད་པར་མཛད་པ་ཡིན། །

[Block 146]
འབྲེལ་པ་མེད་པར་ནི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་ངེས་པ་མེད་དེ། དེས་ན་དེ་ཉིད་སྟོན་པར་མཛད་པ་ནི་ངེས་པ་བཤད་པ་ཡིན་ནོ། །

[Block 147]
དེ་ལ་རྗེས་སུ་འགྲོ་བ་ངེས་པས་ནི་འགལ་བ་དང་དེའི་ཕྱོགས་དང་མཐུན་པ་རྣམས་བསལ༌[^87]ལོ། །

[Block 148]
ལྡོག་པས༌[^88]ནི་མ་ངེས་པ་དང་དེའི་ཕྱོགས་དང་མཐུན་པ་ལྷག་མ་དང་ལྡན་པ་ལ་སོགས་པའོ། །

[Block 149]
གཉི་ག་ལ་ཞེས་བྱ་བ་ནི་གཅིག་ལ་གྲུབ་པ་དགག་པ་ཡིན་ནོ། །

[Block 150]
རབ་ཏུ་གྲུབ་པ་ཞེས་སྨོས་པས༌[^89]མཐུན་པའི་ཕྱོགས་དང་། མི་མཐུན་པའི་ཕྱོགས་དག་ལ་ལྷག་མ་དང་ལྡན་པ་དང་། ཐུན་མོང་མ་ཡིན་པའི་ཐེ་ཚོམ་ཟ་བ་དག་ཀྱང་ངོ་། །

[Block 151]
དེ་ལྟ་མ་ཡིན་ཏེ་འབྲེལ་པ་མེད་པར་མ་མཐོང་བ་ཙམ་གྱིས་ལྡོག་ན་ནི།

[Block 152 [VERSE]]
འཁྲུལ་པ་ཅན་གྱི་གཉེན་པོར་ནི། །
མི་མཐུན་ཆོས་བརྗོད་གང་ཡིན་པ། །

[Block 153]
རེ་ཞིག་འགལ་བ་དང་མ་ངེས་པའི་གཉེན་པོར་གཉི་ག་བརྗོད་པར་བྱ་བ་གང་ཡིན་པ་འདི་ནི་རིགས་སོ་ཞེས་བཤད་པ་གང་ཡིན་པ་སྟེ། ཆོས་མི་མཐུན་པ་སྨོས་པ་ནི་མ༌[^90]ངེས་པའི་གཉེན་པོར་རོ། །

[Block 154]
གལ་ཏེ་མ་མཐོང་འབྲས་ཅན་ཏེ། གལ་ཏེ་དེས༌[^91]མི་མཐུན་པའི་ཆོས་ལ་མ་མཐོང་བ་སྟོན་པར་བྱེད་ན། དེ་མ་སྨོས་ཀྱང་རྟོགས་པར་འགྱུར། །དེ་ལ་སྔོན་བརྗོད་པས་ལོག་པར་འགྱུར་བ་མཐོང་བའི་འཁྲུལ་པ་གང་ཡིན་པ་ནི༌[^92]མེད་དོ། །

[Block 155]
གལ་ཏེ་ཚིག་གིས་མ་མཐོང་བ་ལ་དྲན་པར་བྱེད་དོ་ཞེ་ན། མཐོང་བ༌[^93]མ་རྟོགས་པ་ནི་ཡན་ལག་མ་ཡིན་པས་དེ་ལ་ནི་དྲན་པ་གཞག༌[^94]པར་རིགས་ན། མ་མཐོང་བ་ནི་མཐོང་བ་མེད་པ་ཡིན་ཏེ། དེ་ལ་ནི་མཐོང་བས་གནོད་པར་འགྱུར་རོ། །

[Block 156]
དེ་མེད་ན་གྲུབ་པ་ཁོ་ན་ཡིན་པས་དེ་གྲུབ་པར་བྱ་བའི་ཕྱིར་བརྗོད་པ་དོན་མེད་དོ། །

[Block 157]
གལ་ཏེ་མི༌[^95]དམིགས་པའི་ཚེ་དེ་ཙམ་གྱིས་མེད་དོ་ཞེས་བྱ་བ་མ་ཡིན༌[^96]པས་དེའི་ཕྱིར་བརྗོད་དོ་ཞེ་ན།

[Block 158 [VERSE]]
མེད་ཅེས་བྱ་བའི་ཚིག་གིས་ཀྱང་། །
དེ་མེད་ཁོ་ན་མིན་གལ་ཏེ། །
ཇི་ལྟར་མེད་རིགས་དེ་བརྗོད་ན། །
དེ་ཚེ་མེད་ཅེས་བྱ་བར་རྟོགས། །

[Block 159]
གལ་ཏེ་མ་དམིགས་པས་མེད་དོ༌[^97]ཅེས་བྱ་བར་མི་རྟོགས་ན་བརྗོད་པས་ཀྱང་མི་རྟོགས་པ་ཁོ་ནར་འགྱུར་ཏེ། དེ་ཡང་མི༌[^98]དམིགས་པ་ཁོ་ན་བརྗོད་པར༌[^99]བྱེད་པ་ཡིན་ནོ། །

[Block 160]
གཅིག་མ༌[^100]དམིགས་པས་ནི༌[^101]གཞན་མེད་པ་སྒྲུབ་པར་བྱེད་པ་ཡང་མ་ཡིན་ཏེ། ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 161]
དེས་མེད་དོ་ཞེས་བརྗོད་པས་ཀྱང་དེ་ལྟར་འགྱུར་བ་མ་ཡིན་ཏེ། ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 162]
དེ་བས་ན་ཇི་ལྟར་ཆོས་མི་མཐུན་པ་སྨོས་པས་མ་ངེས་པ་སྤངས་པ་ཡིན། དེ་ལྟ་བས་ན་ལྡོག་པར་འདོད་པས་དེ་ལ་གང་གིས་ན་འདི་ལ་ལྡོག་པ་ཞེས་བྱ་བར་འགྱུར་བའི༌[^102]རིགས་པ་བརྗོད་དགོས་སོ། །

[Block 163]
དེ་མེད་པ་ལ་མི་དམིགས་པས་ལྡོག་པ་གྲུབ་པ་མ་ཡིན་ནམ་ཞེ་ན།

[Block 164 [VERSE]]
གལ་ཏེ་མ་མཐོང་བས་ལྡོག་འགྱུར། །
ཅི་སྟེ་ལྷག་ལྡན་འཁྲུལ་ཅན་ཡིན། །

[Block 165]
དཔེར་ན་འབྲས་བུ་འདི་དག་ནི་སྨིན་པའམ་རོ་འདི་བྲོ་བ་ཡིན་ཏེ། གཟུགས་ཁྱད་པར་མེད་པའི་ཕྱིར་རམ། གཅིག་ལས་སྐྱེས་པའི་ཕྱིར། ཟོས་པ་དང་འདྲའོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 166]
འདི་ལ་ཡང་བརྗོད་པར་འདོད་པ་མ་ལུས་པ་ཕྱོགས་སུ་བྱས་ན་བསྒྲུབ་པར་བྱ་བ་མེད་པ་ལ་གཏན་ཚིགས་མི་དམིགས་པ་ཡོད་པས་ཇི་ལྟར་འཁྲུལ་པ་ཡིན་ཁ་ཅིག་ན་རེ་མངོན་སུམ་གྱིས་གནོད་པར་དོགས་པའི་འཁྲུལ་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 167]
མ་ཡིན་ཏེ་ཕྱོགས་སུ་བྱས་པའི་ཡུལ་ལ་མེད་པའི་ཕྱིར་རོ། །ཅི་སྟེ་གལ་ཏེ་ན༌[^103]འགྱུར་རོ་ཞེ་ན། དེ་ལྟ་བུས་དགོས་ན་ཧ་ཅང་ཐལ་བར་འགྱུར་ཏེ། གཞན་ལ་ཡང་མེད་པར་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 168]
ཚད་མ་ཞུགས་པ་གནོད་པར་བྱེད་པ་ཡིན་གྱི། མ་ཞུགས་པར་གནོད་ན་ནི་ཐམས་ཅད་ལ་ཡིད་བརྟན་དུ་མེད་དོ། །

[Block 169]
ལྡོག་པ་ནི་གྲུབ་པ་ཁོ་ན་བསྒྲུབ་པ༌[^104]ཡིན་ཏེ། དེའི་ཕྱིར་དེ་ལྟ་བུའི་ངོ་བོ་ནི་ངེས་པ་ལ་ལྟོས་སོ། །

[Block 170]
མི་དམིགས་པའི་སྒོ་ནས་ནི་འགའ་ཞིག་ལ་མེད་པ་གྲུབ་ཏུ་ཟིན་ཀྱང་འབྲེལ་པ་མེད་པ་ནི་དེ་མེད་ཀྱང་ཐམས་ཅད་ལ་མེད་པ་མི་གྲུབ༌[^105]པས། ཐེ་ཚོམ་ཟ་བའི་ཕྱིར་ལྡོག་པ་མེད་པ་ནི་ལྷག་མ་དང་ལྡན་པའི་འཁྲུལ་པ་ཡིན་ནོ། །

[Block 171]
གཞན་ཡང་། ལྡོག་པ་ཅན་ཡང་གཏན་ཚིགས་འགྱུར། །གསོན་པོའི་ལུས་འདི་ནི་བདག་མེད་པ་མ་ཡིན་ཏེ། སྲོག་ལ་སོགས་པ་དང་ལྡན་པ་དང་ལྡན་པ༌[^106]མ་ཡིན་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 172]
བདག་མེད་པ་བུམ་པ་ལ་སོགས་པ་མཐོང་བ་དང་མ་མཐོང་བ་དག་ལ་སྲོག་ལ་སོགས༌[^107]པ་མ་མཐོང་བའི་ཕྱིར་རོ།[^108] །དེ་ལས་ལྡོག་པས་བདག་ཡོད་པར་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 173]
བལྟར་མི་རུང་བ་མི་དམིགས་པས་མེད་པ་མ་གྲུབ་ན། བུམ་པ་ལ་སོགས་པ་བདག་མེད་པར་མ་གྲུབ་པའི་ཕྱིར་སྲོག་ལ་སོགས་པ་ལྡོག་པ་མེད་དོ། །

[Block 174]
གལ་ཏེ་ཁས་བླངས་པའི་ཕྱིར་འགྲུབ་པོ་ཞེ་ན། ད་ནི་ཇི་ལྟར་ན་བདག་འགྲུབ། གཞན་བདག་མེད་པ་ཚད་མ་མ་ཡིན་པ་ཡང་ཇི་ལྟར་འགྲུབ་པར་འགྱུར། ཁས་བླངས་པས་ནི་བདག་དང་བཅས་པ་དང་། བདག་མེད་པ་དག་རྣམ་པར་ཕྱེ་ནས་དེ་ལ་མེད་པས་རྟོགས་པར་བྱེད་པ་ཉིད་ཡིན་པར་རྗོད་པར༌[^109]བྱེད་པས་ཀྱང་། བདག་ལུང་ལས་བྱུང་བ་ཉིད་དུ་ཁས་བླངས་པར་འགྱུར་གྱི། རྗེས་སུ་དཔག་པར་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 175]
དེ་ལྟ་བས་ན་མ་མཐོང་དུ་ཟིན་ཀྱང་བདག་ལྡོག་པ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 176]
འགའ་ཞིག་ལ་དེ་ལོག་སྟེ།[^110] སྲོག་ལ་སོགས་པ་ལོག་ཀྱང་འབྲེལ་པ་མེད་པའི་ཕྱིར། ཐམས་ཅད་ལས༌[^111]ལྡོག་པ༌[^112]མི་འགྲུབ་པས་རྟོགས་པར་བྱེད་པ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 177]
གང་ཡང་མ་གྲུབ་པའི་སྦྱོར་བ་དེ་བཞིན་དུ་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་དང་། མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ཡང་ཅི་རིགས་པར་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ། མ་གྲུབ་སྦྱར་བ༌[^113]དེ་ཡང་བརྗོད་བྱ་མིན། །མི་དམིགས་པ་ཁོ་ནར་ཟད་ན་ཐེ་ཚོམ་ཟ་བའི་ཕྱིར་ཏེ། དམིགས་ན་དེ༌[^114]མེད་པའི་ཕྱིར་རོ། །

[Block 178]
མི་དམིགས་པའི་ཕྱིར་ལྡོག་གོ་ཞེས་བྱས་ན་ཐེ་ཚོམ་དུ་གྱུར་པ་ཡང་མ་བཟློག་པར་འགྱུར་རོ། །

[Block 179]
གལ་ཏེ་ཅི་རིགས་པར་ཞེས་སྨོས་པ་ཕྱིར་མ་ལྡོག་པ༌[^115]ཁོ་ན་ཡིན་ནོ། །

[Block 180]
ཞེ་ན། ཅི༌[^116]ཡིན་ཏེ། བརྗོད་པ་གང་ཞིག་གཉི་ག་ལ་ངེས་པ་ཁོ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་འབྱུང་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
