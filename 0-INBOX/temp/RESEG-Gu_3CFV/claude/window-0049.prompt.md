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
[Block 1716]
ག་ག་ཚིལ་བྱེད་པ་འདི་ནི་མཚོན་པ་ཙམ་ཡིན་ཏེ། འབྲེལ་པ་བྱེད་པའི་རྣམ་པ་ལའོ། །

[Block 1717]
བཟོད་པ་དང་ཀུན་ནས་བཟོད་པ་དང་རེག་པ་ལ་ཡང་ཀུན་དུ་ཆགས་པ་མེད་པའི་སེམས་ཀྱིས་གལ་ཏེ་དེ་དང་འབྲེལ་པར་བྱེད་པའི་དེ་ལ་ཡང་འདིས་འཕངས་པའོ། །

[Block 1718]
བག་འཁུམས་པར་མི་བྱེད་པའི་རྣམ་པས་ཀུན་དུ་ཆགས་པ་མེད་པའི་སེམས་ཀྱིས་རེག་པ་ལ་ལྟུང་བ་མེད་པར་རིག་པར་བྱའོ། །ཅི་བསམ་པ་གང་ཡང་རུང་བས་རེག་ན་འམ་ཞེ་ན། དེའི་ཕྱིར་སྐྱི་གཡའ་བར་བྱ་བའི་སེམས་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་སྐྱི་གཡའ་ཞེས་བྱ་བ་ནི་བག་འཁུམས་པར་རིག་པར་བྱའོ། །

[Block 1719]
འདིར་ཀུན་དུ་འདོད་ཆགས་པ་དང་ལྡན་པའི་སེམས་ཀྱིས༌[^1096]རེག་པ་ལ་ནི་དགེ་འདུན་ལྷག་མར་གཏོགས་པའི་ཁ་ན་མ་ཐོ་བའི་ཆོ་ག་དམིགས་ཀྱིས་བསལ་བའོ། །

[Block 1720]
སྐྱི་གཡའ་བ་དང་ལྷན་ཅིག་འབྲེལ་པ་ལ་གསོད་པ་དང་རྡེག་པར་བྱེད་པའི་ལྟུང་བྱེད་དོ། །

[Block 1721]
འདི་ལས་གཞན་པའི་སེམས་ལ་སྐྱི་གཡའ་བར་བྱ་བའི་སེམས་ཀྱི་སྒྲས་རྣམ་པར་གཞག་པའོ། །

[Block 1722]
དེའི་ཕྱིར་རྨ་དང་སྦྲང་བུ་དང་འབྲུམ་བུ་དང་སྨེ་བ་དང་སྤུའི་ཚུམས་བསྟན་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། གང་གི་ཕྱིར་སྐྱི་གཡའ་བའི་སེམས་ཀྱིས་རེག་པ་ལ་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་བ་དེའི་ཕྱིར་འདི་དག་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1723]
རེག་བྱེད་གཅིག་གམ་དུ་མ་ཉིད་ལའོ་ཞེས་བྱ་བ་ནི། འདིར་རྡེག་པར་བྱེད་པ་བཞིན་དུ་གསོད་པར་བྱེད་པ་རེ་རེ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 1724]
འོན་ཀྱང་གསོད་བྱེད་དུ་མ་ཉིད་ལ་ཡང་ལྟུང་བ་གཅིག་ཁོ་ན༌[^1097]བསྐྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1725]
ལོངས་སྤྱོད་དུ་གྱུར་པའི་རྣམ་པར་གྱུར་པ་ཅན་གྱི་འཇུག་པ་ལ་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་ཏེ། ལོངས་སྤྱོད་ལ་ཡང་གསོད་པར་བྱེད་པ་རེ་རེ་ལ་ཐ་དད་པར་དབྱེ་བ་ནི་མེད་དེ་གནོད་པ་ཇི་ལྟ་བར་ཞེས་བྱ་བ་འདིས་ཤེས་པའོ། །

[Block 1726]
འདིར་གཞུང་ནི་དགེ་སློང་གིས༌[^1098]སོར་མོ་གཅིག་གིས་ག་ག་ཚིལ་བྱེད་ན་ལྟུང་བྱེད་དོ། །

[Block 1727]
དེ་བཞིན་དུ་གཉིས་སམ་གསུམ་མམ་བཞི་འམ་ལྔ་རྣམས་ཀྱིས་ཀྱང་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1728]
གཞན་དུ་ཡང་སོར་མོ་གཅིག་གིས་ག་ག་ཚིལ་བྱེད་ན་ལྟུང་བྱེད་ཉིད་དུ་འགྱུར་རོ། །

[Block 1729]
གཉིས་སམ་གསུམ་མམ་བཞི་འམ་ལྔ་དག་གིས་ག་ག་ཚིལ་བྱེད་ན་ལྟུང་བ་ལྔའི་ལྟུང༌[^1099]བར་འགྱུར་རོ་ཞེས་བྱ་བ་འདིར་གཞུང་མཐོང་བ་ཡིན་ནོ། །

[Block 1730]
བརྡེག་པའི་བསླབ་པའི་གཞིའི་རྗེས་སུ་འབྲངས་ནས་དེའི་རྣམ་པར་རྟོག་པར་བྱས་སོ་སྙམ་དུ་བདག་ཅག་སེམས་སོ། །

[Block 1731]
ག་ག་ཚིལ་བྱེད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1732]
ཅི་ཞིག་བྱས་ན་ཆུ་ལ་རྩེ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཆུའི་ཡུལ་ལ་རྩེ་བ་རྗེས་སུ་བསྒྲུབ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གང་དུ་ཁ་ན་མ་ཐོ་བ་ཇི་ལྟ་བུ་འདི་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཞུགས་ཤིང་ནུབ་པ་དང་འབྱུང་བ་དང་ངོགས་གཞན་དུ་རྒལ་བ་དང་རྒྱུན་ཕྱོགས་དང་རྒྱུན་ལས་བཟློག་ཕྱོགས་སུ་རྩོལ་བ་དང་ཆུ་ལ་རྔ་བོ་ཆེ་དང་། རྫ་རྔ་ཁ་གཅིག་པའི་སྒྲ་འབྱིན་པ་དང་གསེག་མ་འཁྲབ་པ་དང་འཕེན་པ་དང་འཁོར་ཡུག་དང་རྡོ་རྗེ་དང་ཁྲོན་པ་དང་རྦ་ཀློང་དང་ཆུ་སྲུབས་འདྲེན་པར་བྱེད་ན་དངོས་གཞིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྔ་བོ་ཆེ་ལ་སོགས་པ་ནས་ཆུ་སྲུབས་འདྲེན་པའི་མཐར་སོ་སོར་ཆུའི་སྒྲ་དང་འབྲེལ་པའོ། །

[Block 1733]
རྒྱུན་ཕྱོགས་ཀྱི་སྒྲས་ཀྱང༌[^1100]འབྱིན་པ་དང་སོ་སོར་འབྲེལ་པའོ། །

[Block 1734]
བེམ་ཏོལ༌[^1101]གྱིས་རྡེག༌[^1102]ན་ཉེས་བྱས་སོ། །

[Block 1735]
བུམ་པ་དང་ཕྲུ་བ་དང་རིལ་བ་དང་ཁམ་ཕོར་དང་། བུ་རམ་གྱི་ཁུ་བ་འཛག་པ་དང་སྲན་ཚོད་དང་འུ་ཤ་དང་ཐང་ཚ་བ་ཉིད་ཡོད་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འཇུག་ཏུ་རུང་བའི་གནས་དེར་ཞུགས་ཏེ་ནུབ་པ་ལ་སོགས་པ་རྗེས་སུ་བསྒྲུབ་པ་ལ་ནི་ལྟུང་བྱེད་དུ་འགྱུར་ལ། བེམ་ཏོལ༌[^1103]གྱིས་རྡེག་པ༌[^1104]ནི་རིལ་བ་ལ་སོགས་པ་འཇུག་པའི་ཡུལ་གང་ལ་གང་དུ་འཇུག་ཏུ་རུང་བ་དེར་ཆུའི་ཡུལ་གྱི་ལས་རྗེས་སུ་བསྒྲུབ་པ་ལ་ཉེས་བྱས་ཏེ་བེམ་ཏོལ༌[^1105]གྱིས་རྡེག་པ༌[^1106]ལ་ནི་ཉེས་བྱས་སོ། །

[Block 1736]
འུ་ཤ་ལ་སོགས་པ་ཚ་བ་ཉིད་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བར་ཤེས་པར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བར་ཤེས་པར་བྱ་བའི་དོན་ཏོ། །

[Block 1737]
མ་ཞུགས་པ་དང་ཞུགས་པའི་ཡུལ་བེམ་ཏོལ༌[^1107]གྱིས་རྡེག་པ་ཞེས་བྱ་བ་འདི་ལ་ཉེས་བྱས་སུ་གཏོགས་པར༌[^1108]བྱའོ། །

[Block 1738]
ལྟེ་བ་ཙམ་ལ་ཞུགས་པའི་བློ་ནི་དེ་ལྟ༌[^1109]ན་ཡང་ཁྲུས་བྱེད་པ་ལ་འདི་ནི་མཐར་གསུངས་སོ། །

[Block 1739]
དེ་ལྟ་བས་ན་དེ་དག་ལ་སོགས་པ་ལ་འཇུག་པ་ཉིད་ཀྱིས་ཡང་དག་པར་བརྟེན་པ་ཉིད་ཡིན་གྱི་དབང་བསྐུར་བ་ལ་ཆུ་དང་འབྲེལ་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 1740]
དེ་བས་ན་འདིའི་དབང་གིས་དངོས་གཞིའི་བྱེད་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 1741]
ཆོལ་ཟངས་ལ་སོགས་པར་མི་ནུབ་པ་ནི་མི་ནུབ༌[^1110]པའོ། །

[Block 1742]
འདིར་ཆུ་ལ་རྩེ་བའི་བློ་ཡོད་པས༌[^1111]ཡིན་ཏེ། དེ་བས་ན་འདིའི་དབང་གིས་དངོས་གཞི་མ་ཡིན་པ་ནི་མ་ཡིན་ནོ། །

[Block 1743]
གང་ཡང་རུང་བ་ཉིད་ཀྱིས་ལྟེ་བ་ནུབ་པ་ཙམ་དུ་ཆུ་ལ་ཞུགས་པ་ཉིད་ནི་ཆུ་ལ་རྩེ་བའི་བློ་ཡོངས་སུ་རྫོགས་པ་སྟེ། དེ་བས་ན་འདུག་པ་ལྟེ་བ་ཙམ་དུ་སོན་པ་ལ་དངོས་གཞིའི༌[^1112]བྱེད་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 1744]
ཆུ་མ་ཡིན་པ་ལ་རྩེ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བའི་རྗེས་བསྙེག་པའི་ཕྱིར་ཏེ། ཆུ་ལས་གཞན་པ་ལ་ཡང༌[^1113]རྩེ་བའོ། །

[Block 1745]
རྩེ་བར་གྱུར་པའི་འཛག་པ་ནི་རྩེ་བར་བྱེད་པའོ། །

[Block 1746]
ལུས་ཀྱི་རྩེད་མོར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་དེའི་གར་གྱི་བདག་ཉིད་ཡིན་ཞེས་བྱ་བ་ཉིད་དུ་དགག་པ་ཉིད་ཀྱི་ཕྱིར་འདིར་ཞུགས་པ་མ་ཡིན་ནོ། །

[Block 1747]
གར་གྱི་བདག་ཉིད་མ་ཡིན་པའི་གཞན་ཐམས་ཅད་ནི་བོང་བ་ལ་སོགས་པ་འཕེན་པ་དང་། ལུས་ཀྱི་རྩེད་མོར་གྱུར་པ་གཡོ་བའི་རྩེད་མོ་གཞན་ཐམས་ཅད་ལ་ཡོངས་སུ་བཟུང་བ་འདིར་རིག་པར་བྱའོ། །

[Block 1748]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 1749]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་ཆབ་མ་ལགས་པ་དངོས་པོ་ལྡེག་མ་ལ༌[^1114]རྩེ་བར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1750]
དེ་ལྟ་བུ་ལ་བྱེད་དུ་བཅུག་པ་ནི་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་གང་དུ་འདིར་ཆར་པར་གྱུར་པ་ལ་ཆུ་ལས་གཞན་པའི་རྫས་ལ་ཁ་ན་མ་ཐོ་བར་སྨོས་པ་དེ་ལྟ་བུར་གྱུར་པའི་ཆུ་དང་། དེ་ལས་གཞན་པའི་རྫས་དག་ལ་འཛག་ཏུ་འཇུག་པའི་རྒྱུ་དེ་དང་འདྲ་བར་རང་གིས་བྱས་པ་ལྟར་བལྟ་བར་བྱའོ། །

[Block 1751]
རེངས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་བར་བྱེད་དུ་བཅུག་པ་ལ་ཡང་ལྟུང་བྱེད་དོ། །

[Block 1752]
ཉེས་བྱས་སུ་གྱུར་པ་ལ་ནི་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1753]
བསྙེན་པར་རྫོགས་པས་བྱེད་དུ་བཅུག་ན་བྱེད་དུ་བཅུག་པ་དང་བྱེད་པ་པོ་གཉིས་ཀ་ལ་ཁ་ན་མ་ཐོ་བ་དང་འདྲ་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1754]
དེ་བས་ན་སྐྱེས་པར་རིག་པར་བྱའོ། །

[Block 1755]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།
--- END BLOCKS ---
