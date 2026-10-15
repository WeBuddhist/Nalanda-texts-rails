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
[Block 2136]
མཆོད་པར་འོས་པ་ཞེས་བྱ་བ་ནི་གང་སྦྱིན་པ་དང་བསྙེན་བཀུར་བ་ལ་སོགས་པའི་མཆོད་པས་གང་ཞིག་ལ་དུས་དུས་སུ་བསྙེན་བཀུར་བར་བྱ་བ་དེ་ནི་མཆོད་པར་བྱ་བའོ། །

[Block 2137]
བསྟོད་པར་འོས་པ་ཞེས་བྱ་བ་ནི་གང་གང་ལ་དུས་དུས་སུ་ཉེ་བར་གནས་ནས་ཚུལ་ཁྲིམས་དང་ཐོས་པ་དང་གཏོང་བ་ལ་སོགས་པའི་ཡིད་བཟུང་བ་ཉིད་ཀྱིས་ཡང་དག་པར་མཐོང་བ་དེ་ནི་བསྟོད་པར་བྱ་བའོ། །

[Block 2138]
བླངས་ན་དགའ་བ་ཞེས་བྱ་བ་ནི་བདག་གིས་བཟུང་བ་ལ་དགའ་བའི་ཕྱིར་གང་དུ་ཡིད་ཆེས་པ་འདི་སྐྱེས་པའོ། །

[Block 2139]
ལག་སྤོད༌[^1495]ཀྱི་ལས་ཀྱིས་ལས་བྱ༌[^1496]ཞིང་བསོད་ནམས་ཀྱི་བློས་ཀྱང་སྟེ་གླ་རྔན་གྱིས་ནི་མ་ཡིན་ནོ། །

[Block 2140]
ཡུལ་གྱི་ངེས་པའི་ཚིག་ནི་འདྲིད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཡང་རྣམ་པར་འབྱེད་པ་ལས་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་མའི་གནས་སུ་ཁྱོད་ཀྱིས་ཅི་ཞིག་བྱས་ཞེས་བྱ༌[^1497]བ་གང་བརྗོད་པ་ཅིའི་ཐ་ཚིག་ཅེས་སྨྲས་པ་དང་། གསོལ་བ་བཙུན་པ་འཇིག་རྟེན་ན་ལྟུང་ངོ་ཞེས་བྱ་བ་གང་ལགས་པའི་ཐ་ཚིག་གོ། །

[Block 2141]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་དག་ཡུལ་གྱི་ངེས་པའི་ཚིག་གིས་ལྟུང་བར་མི་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2142]
འདི་ལྟར་བརྗོད་པར་གྱུར་པ་འདི་སྡུག་བསྔལ་དུ་རྟོགས་པར་བྱ་བ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ༌[^1498]འདི་བསྟན་པའོ། །

[Block 2143]
ལྟུང་བ་བླངས་པ་ཡུན་རིང་དུ་མི་བསྲེལ་ལོ་ཞེས་བྱ་བ་ནི་དུས་ཇི་སྲིད་ཀྱིས་ན་འདིས༌[^1499]བཅབས་སོ་སྙམ་དུ་དོགས་པ་སྐྱེ་བའི་དུས་དེ་སྲིད་ན་འདིར་ཡུན་ཤིན་ཏུ་རིང་བ་ཉིད་དུ་རིག་པར་བྱས་ཏེ་དེ་སྲིད་དུ་བསྲེལ་བར་མི༌[^1500]བྱའོ། །

[Block 2144]
དེ་དགེ་སྐོས་ལ་གཏད་པ་ཉིད་དུ་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་བླངས་པ་ལའོ། །

[Block 2145]
དེས་རབ་ཏུ་བྱུང་བ་ཡིན་པར་དོགས་ན་དགེ་འདུན་ལ་བསྟན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སྐོས་དེ་རབ་ཏུ་བྱུང་བ་ལ་འདི་དང་འབྲེལ་པ་ལ་ཞེས་བྱ་བ་དོགས་པ་འདི་ཡོད་པ་ལ་དེའི་ཚེ་རྫས་དེའི་བདག་པོ་ངེས་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་དགེ་འདུན་ལ་བསྟན་པར་བྱའོ། །

[Block 2146]
བདག་པོ་མ་བྱུང་ན་གཟར་ཐག་ལ་བཏགས་ཏེ་གཞག་གོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དེ་ལྟར་ན་འདི་ཉེ་བར་བསྟན་པ༌[^1501]རབ་ཏུ་བྱུང་བའམ་གཞན་འགའ་ཞིག་བདག་པོ་བྱུང་སྟེ། འདི་ནི་བདག་གི་ཡིན་ཞེས་བྱ་བ་བདག་ཉིད་ཉེ་བར་བསྟན་པར་བྱེད་པ་དེའི་ཆེད་ནི་རྫས་དེ་གཟར་ཐག་ལ་ཉེ་བར་བཏགས་པ་ཉིད་དོ། །

[Block 2147]
འདི་ལ་གོས་རྣམས་གཟར་ཐག་ཏུ་བྱ་བས་ན་གཟར་ཐག་སྟེ་ཀ་བ་ལ་སོགས་པ་ལ་བཅིངས་པ་དགེ་སློང་ཐམས་ཅད་ལ་གསལ་བར་གྱུར་པ་འདི་འདིར་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་གོ་བར་བྱའོ། །

[Block 2148]
ཉེ་བར་བཏགས་པ་ནི་ལྟུང་བའི་དོན་དུའམ་སླར་མི་སྟོར་བའི་དོན་དུའམ། མ་བྱིན་པར་ལེན་པར་ཡང་མི་རིགས་པ་བཟུང་བ་མ་གྲུབ་པའི་དོན་དུའོ། །

[Block 2149]
ནད་པས་མ་གནང་བ་དེ་ལ་སྨན་མི་བླང་ངོ་ཞེས་བྱ་བ་ནི་འདི་ལས་སྨན་ལོང་ཤིག༌[^1502]ཅེས་བྱ་བ་ནད་པས་དེ་ལྟར་གནང་བ་མ་ཐོབ་པ་གང་ཡིན་པ་དེ་ལས་སྨན་དེ་ནད་པའི་ནད་གཡོག་གམ་གཞན་གྱིས་ཀྱང་བླང་བར་མི་བྱའོ། །

[Block 2150]
མ་བྱིན་པར་ལེན་པའི་ཕམ་པར་འགྱུར་བ་རྣམ་པར་འབྱེད་པའོ་ཞེས་བྱ་བ་མ་བྱིན་པར་ལེན་པའི་ཕམ་པར་གྱུར་པའི་སྐབས་རྣམ་པར་འབྱེད་པ་ལས་འབྱུང་བ་རྫོགས་སོ།། །།

[Block 2151]
ཡོངས་སུ་བཟུང་བ་དང་བཅས་པ་གནང་བ་ལས་གཞན་པའི་ཐབས་ཀྱིས་བདག་གིར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཆོམ་རྐུན་དག་གིས༌[^1503]འགྲོན་པོ་བཅོམ་པ་དང་། དུར་ཁྲོད་དང་ལྷའི་ཆུའི་རྡོ་སྣོད་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་སོང་བ་ཡོངས་སུ་འཛིན་པ་དང་བཅས་པའི་རྫས་དེ་གནང་བ་ལས་གཞན་པའི་ཐབས་ཀྱིས་འདི་ཕྱག་དར་ཁྲོད་དོ་ཞེས་བཤད་པ་ཡིན་ནོ། །

[Block 2152]
བདག་གིས་བཙུགས་པའི་ལྷའི་ཆུའི་རྡོ་སྣོད་ལ་འབྱོར་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་ངའི་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཐབས་ཀྱིས་བདག་གིར་མི་བྱ་སྟེ། བདག་ཉིད་དུ་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2153]
བདག་གིར་བྱས་པ་དགུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་རང་གི་མ་ཡིན་པའི་ནོར་རང་གི་མིང་གིས་བྱས་པ་རྐུ་བའམ་བཏང་བ་ལྷག་པར་གནས་པས་བདག་ཏུ་བྱས་པ་གང་ཡིན་པ་དེ་ནི་སོ་སོར་ལེན་པ་དང་། འཚོང་བ་དག་གི་ལས་ཀྱིས་རྙེད་པ་དེར་བདག་ཏུ་བྱས་པ་མ་ཡིན་པ་ཞེས་བྱ་བ་འདི་གྲགས་པ་ཡིན་ནོ། །

[Block 2154]
དགུག་པར་མི་བྱ་བ་ཞེས་བྱ་བ་འདིས་ཉོ་བ་དགག་པ་མ་ཡིན་པ་དང་མཛའ་བོས་སྦྱིན་དུ་བཅུག་པ་དགག་པ་མ་ཡིན་པ་དང་། བྱིན་ལེན་ལ་དགག་པ་མ་ཡིན་པའོ། །

[Block 2155]
དེ་བས་ན་སྟོབས༌[^1504]ཀྱིས་བྱ་བས་ཞེས་བྱ་བ་ཡིད་ཆེས་པ་ཡིན་ནོ། །

[Block 2156]
འདིར་ནི་རང་གི་འདུ་ཤེས་ཀྱིས་འཇུག་པ་ལ་ཆོ་ག་ནི་འདི་ཡིན་ཏེ། ཁ་ན་མ་ཐོ་བ་མེད་པ་ལ་གཞན་དུ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2157]
འདིར་གཞུང་ན་སླར་དགེ་སློང་གིས་བདག་ཏུ་བྱས་པ་དགུག་པར་བྱ་བ་ཡང་མ་ཡིན་ཏེ། དེ་ནི་གང་གིས་ཕྲོགས་པ་དེའི་ཡིན་པའི་ཕྱིར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2158]
འདིའི་དོན་ནི་གང་ཞིག་རྐུ་བ་དེའི་དེ་མ་ཡིན་པ་དེ་ནི་དེ་ལ་དེ་རང་ཉིད་མི་འབྱུང་སྟེ། མི་འདོད་པ་ནི་གཞན་ལ་སྦྱིན་པ་ཞེས་བྱ་བ་རིགས་པ་ཡིན་ཏེ། དེ་བས་ན་འདི་མི་བྱ་བ་ཞེས་བྱ་བའོ། །

[Block 2159]
འདིར་སླར་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར། དེ་ནི་ཆོས་བཤད་པས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ནི་ཞེས་བྱ་བ་ནི༌[^1505]བརྐུས་པའི་ནོར་རོ། །

[Block 2160]
རིན་ཕྱེད་དུ་ཉེ་བས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་བླང་བར་བྱ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2161]
ལྷུང་བཟེད་དང་ཆོས་གོས་ནི་རིན་ཆེན་པོས་བླུས་ཀྱང་རུང་ངོ་ཞེས་བྱ་བ་ལ། རུང་ངོ་ཞེས་བྱ་བ་ནི་རྙེད་པར་བྱ་བ་མ་ཡིན་པ་དང་བརྐུས་པ་ལའོ། །

[Block 2162]
བླུས་ཀྱང་ཞེས་བྱ་བ་ནི་རིན་ཐང་ཡོངས་སུ་རྫོགས་པས་ཀྱང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2163]
མི་སྙན་པ༌[^1506]འབྱུང་བར་འགྱུར་བ་ནི་ཕྱིར་བོར་བའོ་ཞེས་སྐྱེ་བོ་ཕལ་པོ་ཆེའི་མངོན་སུམ་དུ་མ་བབ་པར་བསྐུར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དངོས་པོ་གང་ལས་འདི་ཉིད་ཀྱིས་འདི་བསད་དོ། །

[Block 2164]
འདི་ཉིད་ཀྱིས་འདི་བརྐུས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་མི་སྙན་པ་མི་མཛེས་པ་འབྱུང་བར་འགྱུར་བ་ནི་དེ་བདེན་དུ་བོར་བ་ཉིད་ཡིན་ན་དེ་བདེན་དུ་བོར་བ་ཉིད་ཡིན་ནོ། །

[Block 2165]
སྐྱེ་བོ་ཕལ་པོ་ཆེ་སུའི་ཡང་མངོན་སུམ་དུ་མ་བབ་པར་བསྐུར་བར་མི་བྱ་བླང་བར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2166]
སྐྱེ་བོ་ཕལ་པོ་ཆེའི་མངོན་སུམ་དུ་དམ་པ་མ་ཡིན་པའི་ཡང་དག་པར་འབྱུང་བ་ལ་སྐབས་མེད་པའོ། །

[Block 2167]
འདིར་གཞུང་ནི་ཕག་གི་མགོ་བཅད་པ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 2168]
རོའི་རྫས་མི་མ་ཡིན་པས་བླངས་པ་ཉིད་ནི་ཡོངས་སུ་མ་བཟུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རོའི་རྒྱུད་དུ་གཏོགས་པའི་རྫས་གང་ཡིན་པ་དེ༌[^1507]གལ་ཏེ་མི་མ་ཡིན་པས་བླངས་པར་གྱུར་ན་དེ་ཡོངས་སུ་མ་བཟུང་བའོ་སྙམ་དུ་ཤེས་པར་མི་བྱ་སྟེ། དེ་བརྐུས་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་བ་ཉིད་ལ་འདི་བརྗོད་པའོ། །

[Block 2169]
རབ་ཏུ་གཏུམ་པ་དེའི་ཕྱི་བཞིན་དུ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་མི་མ་ཡིན་པ་དེས་གནོད་པར་བྱེད་པ་སྤང་བའི་ཕྱིར་རབ་ཏུ་གཏུམ་པ་དེའི་ཕྱི་བཞིན་དུ་འགྲོ་བར་བྱའོ། །

[Block 2170]
ཁས་བུབ་ཏུ་བསྙལ་བ་ལ་རྐང་པའི་མཐའ་ནས་བརྩམས་ཏེ་གཡོགས༌[^1508]པར་བྱའོ་ཞེས་བྱ་བ་ལ་བསྙལ་བ་ཞེས་བྱ་བ་ནི་རོ་ལའོ། །

[Block 2171]
འདི་ཡང་རབ་ཏུ་འགྲོ་བ་ཡོངས་སུ་སྤང་བའི་དོན་དུ་རོ་མ་རྨས་པ་ལས༌[^1509]གོས་བླང་བར་མི་བྱའོ། །

[Block 2172]
རང་གིས་རྨས་པ་དང་རྨས་པར་བྱེད་དུ་གཞུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་རོ་ཞེས་བྱ་བ་མཐའ་གཉིས་ཀར་སྦྱར་རོ། །

[Block 2173]
ཐམས་ཅད་དུ་བསྟི་གནས་དང་སོ་ཤིང་དང་ཆུ་དང་འདག་རྫས་དང་ལྕི་བ་དང་ས་ཅི་བདེར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་བྱུག་པ་ལ་སོགས་པའི་དོན་དུ་བ་ལང་གི་ལྕི་བ་བཟུང་བ་ཡིན་ཏེ། འདག་རྫས་སུ་གྱུར་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2174]
འདིར་གཞུང་ནི་དགེ་སློང་གང་དུ་བསྟི་བ་དེར་རྣམ་པ་ལྔ་པོ་ཅི་བདེར་བརྗོད་པར་བྱ་སྟེ། སོ་ཤིང་དང་ཆུ་དང་འདག་རྫས་དང་ལྕི་བ་དང་སའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2175]
དགེ་སློང་དང་དགེ་ཚུལ་མི་འདོད་བཞིན་དུ་འབྲེལ་བས་ཁྲིད་པ་ན་གཟུང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། འབྲེལ་བས་ཞེས་བྱ་བ་ནི་ཕུ་ནུ་དང་བུ་སྲིང་དང་ཆུང་མ་ལ་སོགས་པས་མི་འདོད་བཞིན་དུ་ཁྲིད་པར་གྱུར་ན་དགེ་སློང་གིས་གཟུང་བར་བྱའོ། །
--- END BLOCKS ---
