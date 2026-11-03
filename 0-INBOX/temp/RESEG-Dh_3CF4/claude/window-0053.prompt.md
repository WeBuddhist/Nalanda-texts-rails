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
[Block 1856]
འདི་ལྟ་བུའི་བརྩལ་བ༌[^1082]ཞེས་བྱ་བ་ནི། སངས་རྒྱས་ཉིད་དོན་དུ་གཉེར་བའི་བརྩལ་བ༌[^1083]གང་ཡིན་པ་སྟེ། བྱང་ཆུབ་ཀྱི་སེམས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1857]
ལས་འདི་ཞེས་བྱ་བ་ནི། རང་གི་ཤ་དང་ཁྲག་སྦྱིན་པའི་ལས་སོ། །

[Block 1858]
ཁྱོད་ལྟ་བུ་ཞེས་བྱ་བ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སོ། །

[Block 1859]
འཇིག་རྟེན་ཕན་པའི་ཕྱིར་ལགས་ཀྱང་། །ཞེས་བྱ་བ་ནི་འགྲོ་བ་མཐའ་དག་ཡོངས་སུ་བསྐྱབ་པའི་ཕྱིར་ཏེ། ཐམས་ཅད་ཀྱི་ནོར་བུར་ཁྱོད་གྱུར་པས་བདག་ཀྱང་འགྲོ་བའི་ཁོངས་སུ་གཏོགས་པར་གྱུར་པ་སྟེ། དེ་བས་ན་ཇི་ལྟར་ཡང་དོན་དུ་གཉེར་པར་བྱའོ། །

[Block 1860]
བདག་ཅག་རང་ལ་ཕན་འཚལ་བ། །ཞེས་སྨོས་ཏེ། ཡང་འབྱོར་པ་དོན་དུ་གཉེར་བའོ་ཞེས་བྱ་བ་སངས་རྒྱས་ཉིད་ཐོབ་པའོ། །

[Block 1861]
མ་འཚལ་བ་ནི་ཞེས་བྱ་བ་ནི། འདིའི་དོན་དམ་པ་ལ་འཇུག་པའོ། །

[Block 1862]
བདག་གི་དོན་ཡང་ཞེས་བྱ་བ་ནི། མ་འོངས་པའི་མཐའི་དུས་ཀྱི་ངན་སོང་གི་སྡུག་བསྔལ་གྱི་རྒྱུར་གྱུར་པའི་ལས༌[^1084]ཀྱང་ངོ་། །རྗེས་སུ་གཟུང་བའི་རྒྱུར་གྱུར་བ། །ཞེས་བྱ་བ་ནི་རྗེས་སུ་བཟུང་བར༌[^1085]བྱེད་པའི་ལམ་དུ་གྱུར་པ་སྟེ། མི་ཤེས་པ་དེའི་རྗེས་སུ་གཟུང་བར༌[^1086]འགྲོ་བ་སྟེ། དེ་བས་ན་རྗེས་སུ་བཟུང་བའི༌[^1087]རྒྱུར་གྱུར་པ་ཞེས་བརྗོད་དོ། །

[Block 1863]
[^1088]མི་ཤེས་པས་བདག་རྗེས་སུ་གཟུང་བར་འགྱུར་བའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1864]
རྣམ་པར་ཐར་པའི་ཆོས་ཀྱི་བདུད་རྩི་ལས།

[Block 1865]
ཐོག་མར་བགོ་བར་བྱ་ཞེས་བྱ་བ་ལ། རྣམ་པར་གྲོལ་བ་ནི་རྣམ་པར་ཐར་པ་སྟེ། ཉོན་མོངས་པ་སྤངས་པའོ། །

[Block 1866]
རྣམ་པར་ཐར་པ་ཉིད་ཆོས་ཡིན་པས་རྣམ་པར་ཐར་པའི་ཆོས་སོ། །

[Block 1867]
འདིས་ནི་ཉན་ཐོས་ཀྱི་ཐེག་པས་མྱ་ངན་ལས་འདས་པའི་རྣམ་པར་གྲོལ་བའོ། །

[Block 1868]
རྣམ་པར་ཐར་པའི་ཆོས་ཉིད་བདུད་རྩི་ཡིན་པས་རྣམ་པར་ཐར་པའི་ཆོས་ཀྱི་བདུད་རྩིའོ། །

[Block 1869]
དེ་ཡང་དག་པར་འགྱེད་པ༌[^1089]ནི་རྣམ་པར་ཐར་པའི་ཆོས་ཀྱི་བདུད་རྩི་བགོ་བར་བྱ་བའོ། །

[Block 1870]
ཀུན་ཏུ་ཤེས་པ་སྦྱིན་པའི་དབང་དུ་བྱས་ནས། ང་ནི་དེ་ལ་དགའ་བ་ལ༌[^1090]ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་སྨོས་ཏེ། །གཞན་ནོར་ཆུང་མ་དག་ལ་ཆགས་པ་དང་། །ཞེས་བྱ་བ་ལ། གཞན་ནོར་ཞེས་བྱ་བ་སྨོས་པས་ནི་མ་བྱིན་པར་ལེན་པ་ལས་ལྡོག་པ་དང་། ཆུང་མ་དག་ཅེས་བྱ་བས་ནི་གཞན་གྱིས༌[^1091]ཡོངས་སུ་བཟུང་བའི༌[^1092]ཆུང་མ་ནི།[^1093] འདོད་པས་ལོག་པར་གཡེམ་པ་ལས་ལྡོག་པའོ། །

[Block 1871]
བརྫུན་དུ་སྨྲ་བ་ཞེས་བྱ་བས༌[^1094]ནི་སྨད་པའི་ངག་ལས་ལྡོག་པ་སྟེ། དེ་ལྟར་ཡང་བསླབ་པའི་གཞི་ལྔ་དག་འཛིན་དུ་བཅུག་པའོ། །

[Block 1872]
དེ་དག་ཅེས་བྱ་བ་ནི་མེ་ཏོག་གོ། །

[Block 1873]
རྫིས་བསྐྱོད་ཅེས་བྱ་བའི་སྒྲས་ནི་འདིར་ཤིང་དང་མེ་ཏོག་དང་སྦྱར་བར་བྱའོ། །

[Block 1874]
འགུལ་བར་གྱུར་ཅེས་བྱ་བ་ནི་ས་འགུལ་བའོ། །

[Block 1875]
རྒྱ་མཚོ་ཆེན་པོ་ཤིན་ཏུ་བདོ་བ་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་ཡང་ས་འགུལ་བས་ཞེས་བྱ་བའི་དབང་དུ་བྱ་བ་རྗེས་སུ་འབྲང་ངོ་། །ཡང་ན་རྒྱ་མཚོ་ཆེན་པོ་ཤིན་ཏུ་བདོ་བ་ཞེས་བྱ་བ་འདིས༌[^1095]ནི་དོན་བྱས་པ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 1876]
རང་བཞིན་ལས་ནི་ལྷག་པའི་ཤུགས་དང་སྒྲས། །ཞེས་བྱ་བའི་རང་བཞིན་དེ་ལས་ལྷག་པའི་ཤུགས་དང་ལྡན་པའི་སྒྲ་དང་སྐད་གང་ལ་ཡོད་པའི་ཆུ་དེ་ནི་རང་བཞིན་ལས་ལྷག་པའི་ཤུགས་དང་སྒྲའོ། །

[Block 1877]
སྲ་ཡམ་ཀྲ་མ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་དང་། འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་དང་། སེམས་ཅན་གྱི་དོན་བྱ་བའི་ཕུན་སུམ་ཚོགས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 1878]
རྒྱུ་ཕུན་སུམ་ཚོགས་པའི་དབང་དུ་བྱས་པ་ནི། སྐྱེ་བོ་དམ་པའི་ཆོས་རེ་བཟང་ཞེས་བྱ་བ་སྟེ། སྐྱེ་བོ་བཟང་པོ་ནི་བྱང་ཆུབ་སེམས་དཔའ་སྟེ། རང་གི་སྲོག་ལ་ཆགས་པ་མེད་པས་སོ། །

[Block 1879]
ཆོས་ནི་གནས་པའོ། །

[Block 1880]
ཡང་ན་འདུག་པ་ཡིན་པས་གནས་པ་སྟེ། རང་གི་སྲོག་ལ་ལྟོས་པ༌[^1096]མེད་པ་ནི། བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་གནས་པའོ། །

[Block 1881]
ཡང་ན་ཆོས་ནི་སེམས་བསྐྱེད་པའོ། །

[Block 1882]
དེས་ཁྱད་པར་དུ་གྱུར་པ་ནི་སའི་ཕྱོགས་ལ་སོགས་པ་སྟེ། ལྷག་པའི་བསམ་པའི་ས་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སོ། །

[Block 1883]
རང་གི་སྦྱིན་པ་ནི་མོས་པས༌[^1097]སྤྱོད་པའི་ས་ལ༌[^1098]གནས་པ་མེད་དོ། །

[Block 1884]
འདིས་ནི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 1885]
ཡོན་ཏན་བསྒོམས་པ་ཞེས་བྱ་བ་ནི་ཡོན་ཏན༌[^1099]དག་ལ་གོམས་པ་ཡིན་པས་ཡོན་ཏན་གནས༌[^1100]པའོ། །

[Block 1886]
ཡོན་ཏན་གོམས་པ་ཉིད་དེའི་བྱ་བ་ཡིན་པས༌[^1101]དེའི་ཡོན་ཏན་གོམས་པར་བྱ་བའོ།[^1102] ། དེ་ལ་འདིས་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཡོན་ཏན་བྱས་པ་སྟེ། གང་གི་ཕྱིར་སྔོན་གྱི་ཕྱི་རོལ་གྱི་དངོས་པོ་ཡོངས་སུ་གཏོང་བ་ལ་གོམས་པ་དེའི་དབང་གིས་ནང་གི་དངོས་པོ་ཡོངས་སུ་གཏོང་བ་ཡིན་ནོ་ཞེས་བསྟན་པ་སྟེ།[^1103] ཅི་རིགས་པར་སྔོན་གྱི་དུས་སུ་གོས་དང་། བཟའ་བ་དང་།

[Block 1887 [VERSE]]
བཏུང་བ༌[^1104]དང་མལ་སྟན་སྦྱིན་པ་སྟེ། །
ཕོངས་པའི་ལུས་དང་མཐུན་བཞིན་དུ། །

[Block 1888]
བྱང་ཆུབ་སེམས་དཔའ་གང་དུ་ཡོན་ཏན་ལ་གོམས་པས་གཏོང་བ་ཉིད་དོ། །

[Block 1889]
འདིས་ནི་སྦྱོར་བ་ཁྱད་པར་ཅན་ཐོབ་པ་སྟེ། སྦྱོར་བ་ལ་སོགས་པས༌[^1105]འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་ཉིད་དེ། སྦྱོར་བ་ཁྱད༌[^1106]པར་ཅན་གྱིས་ཏེ།

[Block 1890 [VERSE]]
སངས་རྒྱས་ཉིད་དུ་འདིར་དགོངས་སོ། །
གཞན་ལ༌[^1107]ཕན་པའི་བློ་རེ་དེས། །

[Block 1891]
ཞེས་བྱ་བ་འདིས་ནི་སེམས་ཅན་གྱི་དོན་བྱ་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 1892]
མཐུན་པ་དང་གུས་པ་དང་ཡོ་བྱད་ཀྱིས་ཞེས་བྱ་བ་ལ། མཐུན་པ་ཞེས་བྱ་བ་ནི་དེས་པའོ། །

[Block 1893]
ཡང་ན་དམན་པའི་ཚུལ་ཉིད་དོ། །

[Block 1894]
ཡང་ན་བྱས་པ་གཟོ་བ་ཉིད་དོ། །

[Block 1895]
གུས་པ་ནི་དུལ་བའོ། །
--- END BLOCKS ---
