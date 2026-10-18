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
[Block 106]
དེ་བཞིན་གཤེགས་པས་བསོད་ནམས་ཆེ་བའི༌[^175]རིམ་པ་བསྟན་ཀྱང་སེམས་ཅན་མོས་པ་ཆུང་བ་རྣམས་དོགས་པ་སྐྱེ་བ་ཡང་ཡོད་དེ། དེ་བསླུ་བ་མ་ཡིན་པའི་གཏན་ཚིགས་སུ་དེ་བཞིན་གཤེགས་པའི་རྫུ་འཕྲུལ་མངོན་པར་འདུ་བྱེད་པའི་ལེའུ་བཞག་གོ། །

[Block 107]
སྨན་གྱི་རྒྱལ་པོ་སྔོན༌[^176]དམ་པའི་ཆོས་འདི་ཚོལ་བ༌[^177]ལ་ལུས་དང་སྲོག་ལ༌[^178]མི་ཕངས་པས༌[^179]བརྩོན་པར་ཚོལ་བ་སྔོན་གྱི་ཚུལ་བསྟན་པའི་ཕྱིར་དེའི་འོག་ཏུ་སྨན་གྱི་རྒྱལ་པོ་བྱང་ཆུབ་སེམས་དཔའི་ལེའུ་བཞག་གོ། །

[Block 108]
ཡང་དག་པའི་ཆོས་སྤྱོད་པ་འཇིག་རྟེན་འདི་དང་ཁམས་གཞན་དག་ཏུ༌[^180]རྒྱས་པར་བསྒྲགས་པའི་ཕྱིར་དབྱངས་དམ་པ་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་སྒྲོགས་སུ་གཞུག་པའི་ཕྱིར་དེའི་འོག་ཏུ་སང་སང་པོའི་དབྱངས་ཀྱི་ལེའུ་བཞག་གོ། །

[Block 109]
སེམས་ཅན་རྣམས་མདོ་འདི༌[^181]འཛིན་པ་ལ་བགེགས་དང་བར་ཆད་ཆེ་བས་ཐུགས་རྗེ་ཆེན་པོ་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་འཕགས་པ་སྤྱན་རས་གཟིགས་ལ་བརྟེན་པའི་ཀུན་གྱི་སྒོའི་ལེའུ་བཞག་གོ། །

[Block 110]
བགེགས་དང་བར་ཆད་ཞི་བར་བྱ་བའི་ཕྱིར་གཟུངས་ཀྱི་ལེའུ་བཞག་གོ། །

[Block 111]
སྔོན་གྱི་གཏན་ཚིགས་དང་གླེང་གཞི་ལ་བརྟེན་པའི་ཕྱིར་དེའི་འོག་ཏུ་དགེ་བའི་རྒྱན་གྱི་སྔོན་གྱི་ཚུལ་གྱི་ལེའུ་བཞག་གོ། །

[Block 112]
ཡུལ་ཁམས་ཐམས་ཅད་དུ་རྒྱས་པར་བསྟན་པའི་ཕྱིར་དེའི་འོག་ཏུ་བྱང་ཆུབ་སེམས་དཔའ་ཀུན་ཏུ་བཟང་པོའི་ལེའུ་བཞག་གོ། །

[Block 113]
མདོ་སྡེ་འདི་བཤད་པའི་གཞུང་རྫོགས་ཤིང་མཐར་ཕྱིན་པས་དེའི་འོག་ཏུ་གདམས་ཤིང་གཏད་པར་འོས་པའི་ཕྱིར་དེའི་འོག་ཏུ་ཡོངས་སུ་གཏད་པའི༌[^182]ལེའུ་བཞག་གོ། །

[Block 114 [HEADING]]
## མདོ་སྡེའི་གཞུང་འགྲེལ་པ། ^4-0

[Block 115 [HEADING]]
### གླེང་གཞིའི་ལེའུ། ^4-1-0

[Block 116 [HEADING]]
#### འདི་སྐད་བདག་གིས་ཐོས་པ། ^4-1-1-0

[Block 117]
དེ་ལ་མདོ་སྡེའི་གཞུང་འགྲེལ་པ་ནི་འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་པ་ལ་དོན་རྣམ་པ་གསུམ་སྟེ། དེའི༌[^183]ཕྱིར་བཤད་པ་དང་དེ་ཅིར་དགོངས་པ༌[^184]དང་། དེའི་གཞུང་དགྲོལ་བ་དང་རྣམ་པ་གསུམ་མོ། །

[Block 118 [HEADING]]
##### ཅིའི་ཕྱིར་བཤད་པ། ^4-1-1-1-0

[Block 119]
དེ་ལ་ཅིའི་ཕྱིར་བཤད་པ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདའ་ཀར་འཕགས་པ་དགའ་བོས་དོན་རྣམ་པ་བཞི་ཞིག་དྲིས་པ། བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདས་པའི་འོག་ཏུ་དགེ་སློང་རྣམས་ཇི་ལྟར་བཅོམ་ལྡན་འདས་ལ་གནས་འཆའ་བ་བཞིན་མ་འོངས་པ་ན་སུ་ལ་བརྟེན་པར་བགྱི། ཅི་ལ་གནས་པར་བགྱི། དགེ་སློང་མ་རུངས་པ་ནི་ཇི་ལྟར་གདུལ་བར་བགྱི། མདོ་སྡེ་ཐམས་ཅད་ཀྱི་ཀླད་ལ་ནི་ཚིག༌[^185]ཇི་སྐད་དུ་སྨོས་ཞེས་དྲིས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། [^186]མྱ་ངན་ལས་འདས་པའི་འོག་ཏུ་སོ་སོར་ཐར་པ་ལ་སྟོན་པར་ཟུང་ཤིག །[^187]ཚུལ་ཁྲིམས་ལ་གནས་ཤིང་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་ལ་གནས་འཆའ་བར༌[^188]གྱིས་ཤིག །དགེ་སློང་མ་རུངས་པ་རྣམས་མི་སྨྲ་བས༌[^189]ཐུལ་ཅིག །མདོ་སྡེ་ཐམས་ཅད་ཀྱི་ཀླད་ལ་འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་བྲིས༌[^190]ཤིག་ཅེས་གསུངས་པས་དེའི་ཕྱིར་འདིར་ཡང་འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་སྨོས་སོ། །

[Block 120 [HEADING]]
##### ཅིར་དགོངས་པ། ^4-1-1-2-0

[Block 121]
དེ་སྐད་སྨོས་པ་དེ་ཅིར་དགོངས་པ༌[^191]བསྟན་པའི་ཕྱིར་དད་པ༌[^192]ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། གཞུང་ལས་ཀྱང་འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་སྨོས་པས་དད་པ་སྐྱེ་བར་གྱུར་ཏོ། །

[Block 122]
མངོན་པར་དགའ་ཞེས་སྨོས་པས་ཡེ་ཤེས་སྐྱེ་བར་འགྱུར་རོ་ཞེས་འབྱུང་སྟེ། དད་པས་ནི་འཇུག་ནུས་པར་འགྱུར། ཡེ་ཤེས་ཀྱིས་ནི་འབྱུང་ནུས་པར་འགྱུར་ཏེ། དད་པ་ནི་དགེ་བའི་ཆོས་ཐམས་ཅད་ཀྱི་རྩ་བ། ཡེ་ཤེས་ནི་ཟབ་མོ་རྟོགས་པར༌[^193]འགྱུར་བའི་མཐའོ། །

[Block 123 [HEADING]]
##### གཞུང་དགྲོལ་བ། ^4-1-1-3-0

[Block 124]
ཡང་སློབ་དཔོན་གཞན་གྱིས་བཤད་པ་ལས་ཀྱང་འདི་སྐད་ཅེས་བྱ་བ་དོན་རྣམ་པ་བཞི་སྟེ། རྣམ་ཐོས་བུ་བཞིན་ཕྱུག་པའི་ཕྱིར་དཔེ་དེ་ཁོ་ན་བཞིན་ཞེས་བྱ་བ་དང་། ཇི་སྐད་དུ་བསྒོ་བ༌[^194]དེ་བཞིན་ཉིད་དུ་མཉན་པའི༌[^195]ཕྱིར་དེ་བཞིན་ཞེས་བྱ་བ་དང་། ཇི་སྐད་དུ་དྲིས་པ་དེ་བཞིན་དུ་ལན་བཏབ་པའི་ཕྱིར་འདི་སྐད་ཅེས་བྱ་བ་དང་། གཞན་གྱིས་སྨྲས་པ་དེ་ལྷག་ཆད་མེད་པར་ཟློས༌[^196]པ་དེ་ལ༌[^197]ཡང་འདི་སྐད་ཅེས་བྱ་སྟེ། མདོ་སྡེ་པའི༌[^198]བྱང་ཆུབ་སེམས་དཔས༌[^199]སྔོན་བཅོམ་ལྡན་འདས་ཀྱིས་ཇི་སྐད་དུ་བཤད་པ་དེ་བཞིན་དུ་ཟློས་པའི་ཕྱིར་འདི་སྐད་ཅེས་བྱའོ། །

[Block 125]
ཡང་འདུལ་བ་ཕྲན་ཚེགས་ཀྱི་ནང་ནས་འཕགས་པ་དགའ་བོ་འཁོར་མང་པོ་ལ་ཆོས་སྟོན་པ་ན་འཁོར་རྣམས་ཐེ་ཚོམ་དུ་གྱུར་པ། འདི་གསུམ་བསལ་བའི་ཕྱིར༌[^200]དགའ་བོས་འདི་སྐད་ཅེས་སྨྲས༌[^201]ཏེ།

[Block 126]
དགའ་བོ༌[^202]མཚན་དང་དཔེ་བྱད་དུ་ལྡན་པས་ཆོས་སྟོན་པ་ལ་འཁོར༌[^203]རྣམས་བཅོམ་ལྡན་འདས་ཐུགས་རྗེ་དང་ལྡན་པས་མྱ་ངན་ལས་འདས་པ་ལས།

[Block 127]
སླར་བཞེངས་ཏེ་འཁོར་རྣམས་ལ་ཆོས་སྟོན་པ་ཞིག་གམ་ཕྱོགས་གཞན་གྱི་དེ་བཞིན་གཤེགས་པ་ཞིག་འདིར་ཆོས་སྟོན་ཅིང་བྱོན་པ་ཞིག་གམ། དགའ་བོ༌[^204]འདི་ཉིད་མངོན་པར་སངས་རྒྱས་ཏེ་ཆོས་སྟོན་པ་ཞིག་གམ་སྙམ་པའི་ཐེ་ཚོམ་དེ་བསལ་བའི་ཕྱིར་དགའ་བོས༌[^205]འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་སྨྲས་སོ། །

[Block 128]
ཡང་སློབ་དཔོན་གཞན་ན་རེ་དུས་གསུམ་གྱི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལྷག་ཆད་མེད་པར་མཐུན་པར་སྟོན་པའི་ཕྱིར་དེ་བཞིན་ཞེས་བྱའོ། །

[Block 129]
ཡང་ན་ཆོས་རྣམས་ཀྱི་དེ་ཁོ་ན་ལུགས་གཅིག་པས་མ་ཉམས༌[^206]པ་ཉིད་དེ་བཞིན་ཞེས་བྱ་བ་དང་། ཡང་ན་འཕགས་པ་དགའ་བོས༌[^207]བཅོམ་ལྡན་འདས་ལ༌[^208]ཇི་སྐད་ཐོས་པ་དེ་སྐད་དུ་བཟླས་པའི་ཕྱིར་འདི་སྐད་ཅེས་བྱའོ། །

[Block 130]
བདག་གིས་ཐོས་པ་ནི་ཆོས་འདི་ལྟ་བུ་བདག་ཉིད་ཀྱིས་མངོན་སུམ་དུ་ཐོས་ཀྱི། ཉིད་ནས་ཉིད་དུ་བརྒྱུད་དེ་ཐོས་པ་མ་ཡིན་པའི་ཕྱིར་བདག་གིས་ཐོས་པ་ཞེས་སྨོས་སོ། །

[Block 131]
བདག་ཅེས་བྱ་བ་ནི་ཕུང་པོ་ལྔ་ལ་འཇིག་རྟེན་པའི་ཐ་སྙད་ཙམ་དུ་བཏགས་པ་ལ་བདག་གོ་ཞེས་གདགས་ཀྱི། ཇི་ལྟར་མུ་སྟེགས་ཅན་གྱིས༌[^209]བཏགས་པ་ལྟ་བུ་ནི་མ་ཡིན་གྱི། ལྷ་སྦྱིན༌[^210]དང་མཆོད་སྦྱིན་ཞེས་བཏགས་པ་ལ་བདག་ཅེས་གདགས་པ༌[^211]བཞིན་ནོ། །

[Block 132]
ཡང་འདིར་སུས་ཐོས་པ་མིང་མི་སྨོས་པར་སྤྱིར་བདག་གིས་ཐོས་ཞེས་པ་ཅིའི་ཕྱིར་ཞེས་དྲིས་པ་ལ། དགའ་བོས༌[^212]ཐོས་པ་མང་བ་ཐོས་པ་བསགས་པ། ཐོས་པ་རྒྱ་མཚོ་ཡིན་པས། ཐེག་པ་གསུམ་གྱི་སྡེ་སྣོད་ཀུན་དགའ་བོས༌[^213]བསྡུས་པའི་ཕྱིར་མིང་མ་སྨོས་སོ། །

[Block 133]
ཐོས་པ་ནི་རྣ་བའི་དབང་པོ་དང་རྣམ་པར་ཤེས་པ་གཅིག་ཏུ་བསྡུས་པས་ཐོས་པའི་ང་རྒྱལ་སྐྱེ་བའོ། །

[Block 134]
ཐོས་པ་ཉི་ཚེ་སྨོས་ཀྱི༌[^214]མཐོང་བ་ལ་སོགས་པ་མ་སྨོས་པ་ནི་དོན་ཟབ་མོ་རྟོགས་པ་ལ་ཐོས་པའི་ཤེས་རབ་སྔོན་དུ་འགྲོ་བ་དང་། ཁམས་འདིར་སྒྲས་སངས་རྒྱས་ཀྱི་མཛད་པ་མཛད་པའི་ཕྱིར་ཐོས་པ་ཞེས་སྨོས་སོ། །

[Block 135]
ཡང་བདག་གིས་ཐོས་པ་ཞེས་སྨོས་པས་ཇི་ལྟར་དེ་བཞིན་གཤེགས་པས་བཤད་པ་དེ་ཁོ་ན་བཞིན་སྨྲས་ཏེ། བསྐྱེད་པ་དང་སྐུར་པའི་མཐའ་བསལ་བའི་ཕྱིར་འདི་སྐད་བདག་གིས་ཐོས་ཞེས་སྨོས་སོ། །

[Block 136 [HEADING]]
#### དུས་ཕུན་སུམ་ཚོགས་པ། ^4-1-2-0

[Block 137]
དུས་གཅིག་ན་ཞེས་བྱ་བ་ནི་འདིར་དུས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། དེ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 138]
ཆོས་ཀྱི་རྒྱལ་པོ་ཐུགས་རྗེས་འགྲོ་བའི་དོན་མཛད་པར་དགོངས་པ་དང་། སེམས་ཅན་སྐལ་བ་ཅན་མང་པོ༌[^215]སྨིན་པའི་དུས་དང་མཉམ༌[^216]པ་དང་འཆད་པ་བར་ཆད་མེད་པར་དུས་གཅིག་ཏུ་གྱུར་པའོ། །

[Block 139]
ཡང་དུས་ལ་རྣམ་པ་གཉིས་ཏེ། རིགས་པའི་དུས་དང་། རྣམ་པར་ཤེས་པ་ཙམ་གྱི༌[^217]དུས་སོ། །

[Block 140]
དེ་ལ་རིགས་པའི་དུས་ནི་འཆད་པ་དང་ཉན་པ་རྣམས་འདུ་བྱེད་ཀྱི་ཕུང་པོ་སྐད་ཅིག་ལ་སྐྱེ་ཞིང་འཇིག་པའི་རང་བཞིན་ཅན་སྔ་མ་མ་འདས་པ་དང་། ཕྱི་མས་མ་ཕུལ་བའི་དུས་ཀྱི་ཆ་ཇི་ཙམ་དུ་རྒྱུན་དུ་གནས་པ་དེ་ལྟར༌[^218]གྱི་དུས་དེ་ལ་དུས་གཅིག་ཅེས་གདགས་ཀྱི༌[^219]སྐད་ཅིག་མ་གཅིག་ལ་སྐྱེ་ཞིང་འཇིག་པའི་དུས་ལ་མི་བྱའོ། །

[Block 141]
དེ་ལ་རྣམ་པར་ཤེས་པའི་དུས་ནི་འཆད་པ་དང་ཉན་པ་རྣམས་ཀྱི༌[^220]ཡིད་ལ་དུས་གསུམ་ལྟ་བུར་སྣང་ཞིང་ཡུན་རིང་ཐུང་དང་ཉིན་མཚན་དུ་སྣང་བ་དེའི་དུས་ཏེ། ཇི་ལྟར་རྨི་ལམ་ན་ཡུན་རིང་དུ་ལོན་ཀྱང་སད་ན་དེ་ལྟ་མ་ཡིན་པ་བཞིན་ནོ། །

[Block 142]
ཡང་དུས་གཅིག་ཅེས་སྨོས་པ་ཡང་སྐད་ཅིག་མའི་དུས་དང་། དུས་བཞི་དང་དྲུག་དང་བརྒྱད་ལ་མི་བྱའི། ནམ་ཐུགས་རྗེས་ཕན་འདོགས་པ་དང་། དབང་པོ་སྨིན་པ་དུས་གཅིག་ཏུ་གྱུར་པ་དེ་ལ་དུས་ཤེས་པའོ།[^221] །

[Block 143 [HEADING]]
#### སྟོན་པ་ཕུན་སུམ་ཚོགས་པ། ^4-1-3-0

[Block 144]
བཅོམ་ལྡན་འདས་ཞེས་སྨོས་པ་ནི་སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་སྟེ། དབང༌[^222]ཕུན་སུམ་ཚོགས་པ་ལ་སོགས་པའི་ཡོན་ཏན་དྲུག་དང་ལྡན་པ་ནི་བཅོམ་ལྡན་འདས་ཞེས་བྱའོ། །

[Block 145 [HEADING]]
#### གནས་ཕུན་སུམ་ཚོགས་པ། ^4-1-4-0
--- END BLOCKS ---
