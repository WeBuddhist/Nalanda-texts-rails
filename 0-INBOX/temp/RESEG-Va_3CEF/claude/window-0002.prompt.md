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
[Block 151]
དེ་ལ་ཟ་བ་སྟོང་པ་ཉིད་ནི་ནང་གི་སྐྱེ་མཆེད་རྣམས་ལས༌[^53]བརྩམས་སོ། །

[Block 152]
བཟའ་བ་སྟོང་པ་ཉིད་ནི་ཕྱི་རོལ་གྱི་རྣམས་སོ། །

[Block 153]
དེའི་ལུས་ནི་ཟ་བ་དང་བཟའ་བ་དེ་གཉིས་ཀྱི་གནས་གང་ཡིན་པ་སྟེ་ཁོག་པའོ། །

[Block 154]
དེའི་སྟོང་པ་ཉིད་ནི་ཕྱི་ནང་སྟོང་པ་ཉིད་ཅེས་བྱའོ། །

[Block 155]
གནས་ཀྱི་གཞི་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་ཏེ། དེ་རྒྱ་ཆེ་བའི་ཕྱིར་དེའི་སྟོང་པ་ཉིད་ནི་ཆེན་པོ་སྟོང་པ་ཉིད་ཅེས་བྱའོ། །

[Block 156]
ནང་གི་སྐྱེ་མཆེད་ལ་སོགས་པ་དེ་ཡང་གང་གིས༌[^54]སྟོང་པར་མཐོང་ཞེ་ན། སྟོང་པ་ཉིད་ཤེས་པས་ཏེ། དེའི་སྟོང་པ་ཉིད་ནི་སྟོང་པ་ཉིད་སྟོང་པ་ཉིད༌[^55]དོ། །

[Block 157]
ཇི་ལྟར་དོན་དམ་པའི་རྣམ་པར་མཐོང་བ་དེའི་སྟོང་པ་ཉིད་ནི་དོན་དམ་པ་སྟོང་པ་ཉིད་དོ། །

[Block 158]
གང་གི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་སྒྲུབ་པར་བྱེད་པ་དེ་ཡང་སྟོང་པ་ཉིད་དོ། །ཅིའི་ཕྱིར་སྒྲུབ་པར་བྱེད་ཅེ༌[^56]ན། དགེ་གཉིས་ཐོབ་པར་བྱ་བའི་ཕྱིར། །ཞེས་བྱ་བ་སྟེ། དགེ་བ་གཉིས་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་སོ། །

[Block 159]
རྟག་ཏུ་སེམས་ཅན་ཕན་བྱའི་ཕྱིར། །ཞེས་བྱ་བ་ནི་སེམས་ཅན་ལ་གཏན་དུ་ཕན་པར་བྱ་བའི་ཕྱིར༌[^57]རོ། །

[Block 160]
འཁོར་བ་གཏང་བར༌[^58]མི་བྱའི་ཕྱིར། །ཞེས་བྱ་བ་ནི་འཁོར་བ་ཐོག་མ་དང་ཐ་མ་མེད་པ་སྟོང་པ་ཉིད་དུ་མ་མཐོང་ན་སྐྱོ༌[^59]སྟེ་འཁོར་བ་ཡོངས་སུ་གཏོང་ངོ་། །དགེ་བ་མི་ཟད་བྱ་བའི་ཕྱིར། ། ཞེས་བྱ་བ་ནི་ཕུང་པོ་ལྷག་མ་མེད་པའི་མྱ་ངན་ལས་འདས་པ་ན་ཡང་མི་གཏོང་ཞིང་མི་འདོར་བ་གང་ཡིན་པའོ། །

[Block 161]
རིགས་ཀྱང་རྣམ་པར་དག་བྱའི་ཕྱིར། །ཞེས་བྱ་བ་ལ། རིགས་ནི་རང་བཞིན་ཏེ་ངོ་བོ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 162]
མཚན་དང་དཔེ་བྱད་ཐོབ་བྱའི་ཕྱིར། །ཞེས་བྱ་བ་ནི། སྐྱེས་བུ་ཆེན་པོའི་མཚན་རྣམས་དང་། དཔེ་བྱད་བཟང་པོ་རྣམས་དང་བཅས་པ་ཐོབ་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 163 [VERSE]]
སངས་རྒྱས་ཆོས་རྣམས་དག་བྱའི་ཕྱིར། །
བྱང་ཆུབ་སེམས་དཔའ་སྒྲུབ་པར་བྱེད། །

[Block 164]
ཅེས་བྱ་བ་ནི་སྟོབས་དང་མི་འཇིགས་པ་དང་མ་འདྲེས་པ་ལ་སོགས་པའོ། །

[Block 165]
དེ་ལྟར་རེ་ཞིག་སྟོང་པ་ཉིད་བཅུ་བཞི་རྣམ་པར་གཞག་པར༌[^60]ཤེས་པར་བྱའོ། །

[Block 166]
འདི་ལ་སྟོང་པ་ཉིད་གང་ཡིན་ཞེ་ན།

[Block 167 [VERSE]]
གང་ཟག་དང་ནི་ཆོས་རྣམས་ཀྱི། །
དངོས་པོ་མེད་འདིར་སྟོང་པ་ཉིད། །

[Block 168]
དེ་དངོས་མེད་པའི་དངོས་ཡོད་པ།[^61] །དེ་ནི་དེ་ལས་སྟོང་ཉིད་གཞན། །ཞེས་བྱ་བའོ།

[Block 169]
[^62] །གང་ཟག་དང་ཆོས་ཀྱི་དངོས་པོ་མེད་པ་ནི་སྟོང་པ་ཉིད་དོ། །

[Block 170]
དངོས་པོ་མེད་པ༌[^63]དེའི་དངོས་པོ་ཡོད་པ་ཡང་ཡིན་ནོ། །

[Block 171]
[^64]ཟ་བ་ལ་སོགས་པ་སྟོང་པ་ཉིད་ཅེས་གོང་དུ་ཇི་སྐད་སྨོས་པ་དེར་སྟོང་པ་ཉིད་ཀྱི་མཚན་ཉིད་བསྟན་པའི་ཕྱིར། དངོས་པོ་མེད་པ་སྟོང་པ་ཉིད་དང་། དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་སྟོང་པ་ཉིད་དང་། སྟོང་པ་ཉིད་རྣམ་པ་གཉིས་ཐ་མར་རྣམ་པར་འཇོག་སྟེ། གང་ཟག་དང་ཆོས་སུ་སྒྲོ་འདོགས་པ་དང་། དེའི་སྟོང་པ་ཉིད་ལ་སྐུར་པ་འདེབས་པ་བསལ་བའི་ཕྱིར་གོ་རིམས་བཞིན་ནོ། །

[Block 172]
དེ་ལྟར་སྟོང་པ་ཉིད་ཀྱི༌[^65]རབ་ཏུ་དབྱེ་བ་ཤེས་པར་བྱའོ། །

[Block 173 [HEADING]]
#### སྒྲུབ་པ། ^1-2-5-0

[Block 174]
སྒྲུབ་པ་ཇི་ལྟར་ཤེས་པར་བྱ་ཞེ་ན།

[Block 175 [VERSE]]
གལ་ཏེ་ཉོན་མོངས་དེ་མ་གྱུར། །
ལུས་ཅན་ཐམས་ཅད་གྲོལ་བར་འགྱུར། །
གལ་ཏེ་རྣམ་དག་དེ་མ་གྱུར། །
འབད་པ་འབྲས་བུ་མེད་པར་འགྱུར། །

[Block 176]
གལ་ཏེ་གཉེན་པོ་མ་སྐྱེས་པར་ཡང་ཆོས་རྣམས་ཀྱི་སྟོང་པ་ཉིད་ཀྱིས༌[^66]གློ་བུར་གྱི་ཉེ་བའི༌[^67]ཉོན་མོངས་པ་རྣམས་ཀྱིས་ཀུན་ནས་ཉོན་མོངས་པར་མི་འགྱུར་ན་ནི་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པས་འབད་པ་མེད་པར་སེམས་ཅན་ཐམས་ཅད་གྲོལ་བར་འགྱུར་རོ། །

[Block 177]
ཅི་སྟེ་གཉེན་པོ་སྐྱེས་ཀྱང་རྣམ་པར་དག་པར་མི་འགྱུར་ན་ནི་ཐར་པར་བྱ་བའི་ཕྱིར་རྩོམ་པ་འབྲས་བུ་མེད་པར་འགྱུར་རོ། །

[Block 178]
དེ་ལྟར༌[^68]ན།

[Block 179 [VERSE]]
ཉོན་མོངས་མ་ཡིན་མི་མོངས༌[^69]མིན། །
དེ་ནི་དག་དང་མ་དག་མིན། །

[Block 180]
ཇི་ལྟར་ཉོན་མོངས་པར་གྱུར་པ་མ་ཡིན་ལ་མ་དག་པ་ཡང་མ་ཡིན་ཞེ་ན་སེམས་རང་བཞིན་གྱིས༌[^70]འོད་གསལ་བའི་ཕྱིར་རོ། །

[Block 181]
ཇི་ལྟར་ཉོན་མོངས་པར་གྱུར་པ་མ་ཡིན་པ་ཡང་མ་ཡིན་ལ་དག་པ་ཡང་མ་ཡིན་ཞེ་ན། གློ་བུར་གྱི༌[^71]ཉོན་མོངས་པའི་ཕྱིར་རོ། །

[Block 182]
དེ་ལྟར་སྟོང་པ་ཉིད་ཀྱི་རབ་ཏུ་དབྱེ་བ་བསྟན་པ་བསྒྲུབས་པ༌[^72]ཡིན་ནོ། །

[Block 183]
དེ་ཡང་སྟོང་པ་ཉིད་ཀྱི་དོན་བསྡུས་པ་ནི་མཚན་ཉིད་རྣམ་པར་གཞག་པར་རིག་པར་བྱའོ། །

[Block 184]
དེ་ལ་མཚན་ཉིད་ནི་དངོས་པོ་མེད་པའི་མཚན་ཉིད་དང་། དངོས་པོའི་མཚན་ཉིད་དོ། །

[Block 185]
དངོས་པོའི་མཚན་ཉིད་ཀྱང་དངོས་པོ་ཡོད་པ་དང་དངོས་པོ་མེད་པ་ལས་རྣམ་པར་གྲོལ་བའི་མཚན་ཉིད་དང་། དེ་ཉིད་དང་གཞན་ལས་རྣམ་པར་གྲོལ་བའི་མཚན་ཉིད་དོ། །

[Block 186]
རྣམ་པར་གཞག་པ་ནི་རྣམ་གྲངས་ལ་སོགས་པས༌[^73]རྣམ་པར་གཞག་པར་རིག་པར་བྱའོ། །

[Block 187]
དེ་ལ༌[^74]རྣམ་པ་བཞི་པོ་འདི་དག་བསྟན་པས་ནི་རྣམ་པར་རྟོག་པ་དང་། སྐྲག་པ་དང་། ལེ་ལོ་དང་། ཐེ་ཚོམ་ཉེ་བར་ཞི་བར་བྱ་བའི་ཕྱིར་སྟོང་པ་ཉིད་རང་གི་མཚན་ཉིད་དང་། ལས་ཀྱི་མཚན་ཉིད་དང་། ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བའི་མཚན་ཉིད་དང་། རིགས་པའི་མཚན་ཉིད་བརྗོད་པ་ཡིན་ནོ། །

[Block 188]
[^75]བསྟན་བཅོས་དབུས་དང་མཐའ་རྣམ་པར་འབྱེད་པ་ལས་མཚན་ཉིད་ཀྱི་ལེའུར་བཅད་པ་ཞེས་བྱ་བ་སྟེ༌[^76]དང་པོའི་འགྲེལ་པའོ།། །།

[Block 189 [HEADING]]
## སྒྲིབ་པ། ^2-0

[Block 190]
སྒྲིབ་པའི་དབང་དུ་མཛད་དེ།

[Block 191 [VERSE]]
ཁྱབ་དང་ཉི་ཚེ་ལྷག་པ་དང་། །
མཉམ་དང་ལེན་དང་སྤོང་བ་ནི། །
གཉིས་ཀྱི་སྒྲིབ་པར་བསྟན་པ་ཡིན། །

[Block 192]
ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 193]
དེ་ལ་ཁྱབ་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཅན་རྣམས་ཀྱི་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་སྟེ། མཐའ་དག་ལ་སྒྲིབ་པའི་ཕྱིར་རོ། །

[Block 194]
ཉི་ཚེ་བ་ནི་ཉན་ཐོས་ལ་སོགས་པའི་རིགས་ཅན་རྣམས་ཀྱི་ཉོན་མོངས་པའི་སྒྲིབ་པའོ། །

[Block 195]
ལྷག་མ་ནི་དེ་དག་ཉིད་ཀྱི་སྒྲིབ་པ་སྟེ། འདོད་ཆགས་ལ་སོགས་པའི་སྤྱོད་པ་རྣམས་ཀྱི་སྒྲིབ་པའོ། །

[Block 196]
མཉམ་པ་ནི་ཆ་མཚུངས་པར་སྤྱོད་པ་རྣམས་ཀྱི་སྒྲིབ་པའོ། །

[Block 197]
འཁོར་བ་ལེན་པ་དང་སྤོང་བའི་སྒྲིབ་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཅན་རྣམས་ཀྱི་སྒྲིབ་པ་སྟེ། མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་ལ་སྒྲིབ་པའི་ཕྱིར་རོ། །

[Block 198]
དེ་ལྟར་འདི་དག་ནི་ཅི་རིགས་པར་བྱང་ཆུབ་སེམས་དཔའི་རིགས་ཅན་རྣམས་དང་། ཉན་ཐོས་ལ་སོགས་པའི་རིགས་ཅན་རྣམས་དང་གཉི་གའི་སྒྲིབ་པར་བསྟན་ཏོ། །

[Block 199]
ཡང་།

[Block 200 [VERSE]]
ཉོན་མོངས་མཚན་ཉིད་རྣམ་དགུའོ། །
ཀུན་ཏུ་སྦྱོར་རྣམས་སྒྲིབ་པ་ཡིན། །

[Block 201]
ཀུན་ཏུ་སྦྱོར་བ་དགུ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པའོ། །

[Block 202]
དེ་དག་གང་ལ་གང་སྒྲིབ་ཅེ་ན།

[Block 203 [VERSE]]
སྐྱོ་བ་དང་ནི་བཏང་སྙོམས་དང་། །
དེ་ཁོ་ན་ནི་མཐོང་བ་དང་། །

[Block 204]
རྗེས་སུ་ཆགས་པའི་ཀུན་ཏུ་སྦྱོར་བ་ནི་ཀུན་ཏུ་སྐྱོ་བ་ལ་སྒྲིབ་པའོ། །

[Block 205]
ཁོང་ཁྲོ་བའི་ཀུན་ཏུ་སྦྱོར་བ་ནི་བཏང་སྙོམས་ལ་སྒྲིབ་སྟེ། དེས་ནི་མི་མཐུན་པ་ལ་ཁོང་ཁྲོ་བའི་གཞི་ལ་བཏང་སྙོམས་སུ་བྱེད༌[^77]མི་ནུས་སོ། །

[Block 206]
ལྷག་མ་རྣམས་ནི་དེ་ཁོ་ན་མཐོང་བ་ལ། ཇི་ལྟ༌[^78]ཞེ་ན། དེ་དག་ནི་གོ་རིམས་བཞིན་དུ།

[Block 207 [VERSE]]
འཇིག་ཚོགས་ལྟ་དང་དེའི༌[^79]གཞི་དང་། །
འགོག་དང་ལམ་དང་དཀོན་མཆོག་དང་། །
རྙེད་པ་དང་ནི་བཀུར་སྟི་དང་། །
ཡོ་བྱད་བསྙུངས་པ་ཡོངས་ཤེས་ལ། །

[Block 208]
སྒྲིབ་པ་ཡིན་ནོ། །

[Block 209]
ང་རྒྱལ་གྱི་ཀུན་ཏུ་སྦྱོར་བ་ནི་འཇིག༌[^80]ཚོགས་ལ་ལྟ་བ་ཡོངས་སུ་ཤེས་པ་ལ་སྒྲིབ་པ་སྟེ། མངོན་པར་རྟོགས་པའི་དུས་ན་ངའོ་སྙམ་པའི་ང་རྒྱལ་བར་ཆད་དང་བཅས་པ་དང་བར་ཆད་མེད་པར་ཀུན་ཏུ་འབྱུང་བའི་དབང་གིས་དེ་མ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 210]
མ་རིག་པའི་ཀུན་ཏུ་སྦྱོར་བ་ནི་འཇིག་ཚོགས་ལ༌[^81]ལྟ་བའི་གཞི་ཡོངས་སུ་ཤེས་པ་ལ་སྒྲིབ་སྟེ། དེས་ཉེ་བར་ལེན་པའི་ཕུང་པོ་རྣམས་ཡོངས་སུ་མི་ཤེས་པའི་ཕྱིར་རོ། །

[Block 211]
ལྟ་བའི་ཀུན་ཏུ་སྦྱོར་བ་ནི་འགོག་པའི་བདེན་པ་ཡོངས་སུ་ཤེས་པ་ལ་སྒྲིབ་སྟེ། འཇིག་ཚོགས་དང༌[^82]མཐར་འཛིན་པར་ལྟ་བ་གཉིས་ཀྱིས་དེ་ལ་སྐྲག་པ་དང་། ལོག་པར་ལྟ་བས་དེ་ལ་སྐུར་པ་འདེབས་པའི་ཕྱིར་རོ། །

[Block 212]
མཆོག་ཏུ་འཛིན་པའི་ཀུན་ཏུ་སྦྱོར་བ་ནི་ལམ་གྱི་བདེན་པ་ཡོངས་སུ་ཤེས་པ་ལ་སྒྲིབ་སྟེ། རྣམ་པ་གཞན་གྱིས་མཆོག་གི་དག་པར་མཆོག་ཏུ་འཛིན་པའི་ཕྱིར་རོ། །

[Block 213]
ཐེ་ཚོམ་གྱི༌[^83]ཀུན་ཏུ་སྦྱོར་བ་ནི་དཀོན་མཆོག་གསུམ་ཡོངས་སུ་ཤེས་པ་ལ་སྒྲིབ་སྟེ། དེའི་ཡོན་ཏན་ལ་མངོན་པར་ཡིད་མི་ཆེས་པའི་ཕྱིར་རོ། །

[Block 214]
ཕྲག་དོག་གི་ཀུན་ཏུ་སྦྱོར་བ་ནི་རྙེད་པ་དང་། བཀུར་སྟི་ཡོངས་སུ་ཤེས་པ་ལ་སྒྲིབ་སྟེ། དེའི་ཉེས་པ་མི་མཐོང་བའི་ཕྱིར་རོ། །

[Block 215]
སེར་སྣའི་ཀུན་ཏུ་སྦྱོར་བ་ནི་ཡོ་བྱད་བསྙུངས་པ་ཡོངས་སུ་ཤེས་པ་ལ་སྒྲིབ་སྟེ། ཡོ་བྱད་ལ་ལྷག་པར་ཞེན་པའི་ཕྱིར་རོ། །

[Block 216]
དགེ་ལ་སོགས་པ་བཅུ་ལ་གཞན། །དགེ་བ་ལ་སོགས་པ་རྣམ་པ་བཅུ་ལ་སྒྲིབ་པ་གཞན་དུ་རིག་པར་བྱའོ། །

[Block 217]
སྒྲིབ་པ་དེ་ནི་གང་། དགེ་བ་ལ་སོགས་པ་ནི་གང་ཞེ་ན།

[Block 218 [VERSE]]
སྦྱོར་བ་མེད་དང་སྐྱེ་མཆེད་མིན། །
རྣལ་འབྱོར་མིན་པས་གང་བསྐྱེད་དང་། །
སྐྱེ་བ་མེད་དང་ཡིད་མི་བྱེད། །
ཚོགས་ནི་རབ་ཏུ་མ་རྫོགས་དང་། །

[Block 219 [VERSE]]
རིགས་དང་བཤེས་གཉེན་མི་ལྡན་དང་། །
སེམས་ནི་ཡོངས་སུ་སྐྱོ་བ་དང་། །
སྒྲུབ་པ་དང་ཡང་མི་ལྡན་དང་། །
སྐྱེ་བོ་ངན་དང་འགྲོགས་པ་དང་། །

[Block 220 [VERSE]]
རང་གི་གནས་ངན་ལེན་གསུམ་ལས། །
ལྷག་མ་ཤེས་རབ་མ་སྨིན་དང་། །
རང་བཞིན་གྱིས་ནི་གནས་ངན་ལེན། །
ལེ་ལོ་དང་ཡང་བག་མེད་དང་། །

[Block 221 [VERSE]]
སྲིད་དང་ལོངས་སྤྱོད་ཆགས་པ་དང་། །
སེམས་ནི་ཞུམ་པར་གྱུར་པ་དང་། །
མ་དད་པ་དང་མ་མོས་དང་། །
སྒྲ་བཞིན་དུ་ནི་དཔྱོད་པ༌[^84]དང་། །

[Block 222 [VERSE]]
དམ་ཆོས་ཆེད་ཆེར་མི་འཛིན་དང་། །
རྙེད་ལ་གདུ༌[^85]དང་སྙིང་རྗེ་མེད། །
ཐོས་པས་ཕོངས་དང་ཉུང་བ་དང་། །
ཏིང་འཛིན་སྦྱངས་པ་མ་བྱས་པའོ། །

[Block 223]
དེ་དག་ནི་སྒྲིབ་པའོ། །

[Block 224]
དགེ་བ་ལ་སོགས་པ་གང་ཞེ་ན།

[Block 225 [VERSE]]
དགེ་དང་བྱང་ཆུབ་ཡང་དག་འཛིན། །
བློ་ལྡན་འཁྲུལ་མེད་སྒྲིབ་པ་མེད། །
བསྔོ་དང་མི་སྐྲག་སེར་སྣ་མེད། །
དབང་ནི་དགེ༌[^86]ལ་སོགས་པའོ། །

[Block 226]
ཞེས་བྱ་བའོ། །

[Block 227]
དགེ་བ་ལ་སོགས་པ་འདི་དག་ལ་གང་གང་ལ་སྒྲིབ་པ་དུ་ཡོད་པར་ཤེས་པར་བྱ་ཞེ་ན།

[Block 228 [VERSE]]
དེ་དག་གི་ནི་སྒྲིབ་པ་རྣམས། །
གསུམ་གསུམ་དག་ཏུ་ཤེས་པར་བྱ། །

[Block 229]
ཞེས་གསུངས་སོ། །

[Block 230]
དགེ་བ་ལ་སྒྲིབ་པ་གསུམ་ནི་སྦྱོར་བ་མེད་པ་དང་། སྐྱེ་མཆེད་མ་ཡིན་པ་ལ་སྦྱོར་བ་དང་། ཚུལ་བཞིན་མ་ཡིན་པ་ལ་སྦྱོར་བའོ། །
--- END BLOCKS ---
