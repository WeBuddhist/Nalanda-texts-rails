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
[Block 1786]
དང་པོ་ཉིད་དུ་རྗེས་སུ་འདོད་པ་ནི་འདི་ཉིད་དུ༌[^1037]ཡིན་པས་སོ། །

[Block 1787]
ཆོས་ཀྱི་གྲོགས་ཀྱང༌[^1038]བྱ་བ་དང་། །ཞེས་བྱ་བ་ནི། སློང་བ་རྣམས་ཀྱི༌[^1039]བྱང་ཆུབ་སེམས་དཔའ་དགེ༌[^1040]བའི་བཤེས་གཉེན་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 1788]
འདི་ནི་རེ་ཞིག་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཕན་ཡོན་ནོ། །

[Block 1789]
ང་ཡང་རབ་ཏུ་དགའ་བར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཕན་ཡོན་ནོ། །

[Block 1790]
ཆོས་དགའ་བ་དེ་གཉིས་ཀྱི་དངོས་པོས་ནི་འཛིན་པའི་འཇིག་པ༌[^1041]ལས་ལྡོག་པ་སྟེ། དེའི་ཕན་ཡོན་རྣམ་པ་གཉིས་བསྟན་ཏོ། །

[Block 1791]
སྙིམ་པ༌[^1042]བཟེད་དེ་ཞེས་བྱ་བ་སྨོས་པས་ནི་སྣོད་དང་འབྲིམ༌[^1043]པས་དུས་ལས་འདས་ཀྱིས་དོགས་པའོ། །

[Block 1792]
འདིར་ཁྱད་པར་བསྟན་པའི་ཕྱིར། ཙནྡན་དམར་པོའི་ཁུ་བ་འདྲ་བ་ཞེས་སྨོས་ཏེ། དམར་བའི་ཁྱད་པར་ནི་རྒྱལ་པོ་དེའི༌[^1044]མཚན་ཉིད་དང༌[^1045]ལྡན་པའོ། །

[Block 1793]
ཁྲག་གི་མཚན་ཉིད་ཀྱི་ཁྱད་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 1794]
མཚམས་དུས་ཀྱི་ཆར་སྤྲིན་ལྟ་བུ་ནི་ཁྲག་གོ། །

[Block 1795]
ཁྲག་དང་འབྲེལ་པ་དེ་ནི་གནོད་སྦྱིན་ནོ། །

[Block 1796]
དགའ་བ་མཆོག་དང་ལྡན་པས་ལུས་ཀྱང་མ་ཉམས་པ་ནི་བརྟན་པ༌[^1046]དང་ལྡན་པའོ། །

[Block 1797]
སེམས་ཀྱང་བརྒྱལ་བ་མེད་པ་ནི་ལུས་ཀྱི་ཡོན་ཏན་དང་ལྡན་པ་སྟེ། ཁྲག་གི་རྒྱུན་ཀྱང་ཟད་པར་ཡོང༌[^1047]མ་གྱུར་ཏོ། །

[Block 1798]
ད་ནི་འདིས་འཚལ་ཏེ་ཞེས་བྱ་བ་ནི་ཁྲག་དེ་དགག་པ་སྟེ། གང་གཞན་སྔར་བསླངས་པར་གྱུར་པ་དེ་ནི་བྱིན་པར་གྱུར་ཏོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 1799]
སྡུག་བསྔལ་མང་པོ་འབྱུང་བའི་གནས། །ཞེས་བྱ་བ་འདིས་ནི་སྡུག་བསྔལ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1800]
བྱས་པ་མི་གཟོ་ཞེས་བྱ་བ་འདིས་ནི་མི་གཙང་བ་ཉིད་དེ། གཙང་བའི་རྫས་ཀྱིས་བསྐྱེད་ཀྱང་ཡང་མི་གཙང་བ་ཉིད་ཡོངས་སུ་མི་འདོར་བས་སོ། །

[Block 1801]
ཡང་ན་སྡུག་བསྔལ་མང་པོ་འབྱུང་བའི་གནས་དེ་ཉིད་ཀྱི་ཁྱད་པར་གྱི་དོན་ཏོ། །

[Block 1802]
སྡུག་བསྔལ་གསོ་བའི་གཞིའི་དོན་ཏོ། །

[Block 1803]
སློང་བ་རྣམས་ཀྱི་བསྙེན་བཀུར་ནི་སློང་བ་རྣམས་ལ་སྦྱིན་པའོ། །

[Block 1804]
དེའི་གྲུབ་པ༌[^1048]ནི་སློང་བ་དག་ལ་སྦྱིན་པ་དེའི༌[^1049]དོན་གྲུབ་སྟེ། སློང་བ་དག་ལ་སྦྱིན་པའི་དོན་གྲུབ་པའོ། །

[Block 1805]
རབ་ཏུ་དགའ་དང་རྗེས་སུ་མཐུན། །ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་མང་པོའི་འབྱུང་གནས་ཡིན་ཡང་བཟུང་བར་གྱུར་པ་བདེ་བའི་རྒྱུར་གྱུར་པ་སྟེ། སྦྱིན་པ་པོ་རང་གི་བདེ་བའི་རྒྱུར་གྱུར་པས་སོ། །

[Block 1806]
བདེ་བ་ཞེས་སྨོས་པ་ནི། བྱས་པ་མི་གཟོ་བ་ཉིད་ཡིན་ནོ་ཞེས་གཞན་དག་ཏུ་བསྟན་པ་ནི་ལན་དུ་ཕན་འདོགས་པར་བཟུང་བའི༌[^1050]ཕྱིར་རོ། །

[Block 1807]
རབ་ཏུ་དགའ་བ་དང་། རབ་ཏུ་ཚིམ་པ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་དགའ་བ་དང་རྗེས་སུ་མཐུན་པར་གྱུར་པ་ཞེས་བྱ་བ་བསྟན་མ་ཐག་པ་འདིའི་རྒྱུས་སོ། །

[Block 1808]
ཨུཏྤ་ལའི་འདབ་མ་ལྟར་མདོག་སྔོ་ཞིང་མཐིང་ག་གང་ཡིན་པ་དེ་ནི་ཨུཏྤ་ལ་མཐིང་ག་ལྟར་མདོག་སྔོ་བའོ། །

[Block 1809]
རྡོ་རྗེ་རིན་པོ་ཆེས་སྤྲས་པའི་རལ་གྲི༌[^1051]སྔོན་པོའི་འོད་ཀྱིས༌[^1052]མཛེས་པ་གང་ཡིན་པ་དེ་ནི་རལ་གྲི༌[^1053]རྣོན་པོ་རྡོ་རྗེ་རིན་པོ་ཆེས་སྤྲས་པའི་འོད་ཀྱིས་མཛེས་པའོ། །

[Block 1810]
སྐབས་ནི་མེད་པར་བྱས་པས༌[^1054]ན། །ཞེས་བྱ་བ་ནི་སྲན་ཐུབ་པ་མེད་པའི་སྐབས་མེད་པར་བྱས་པའོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྦྱིན་པ་ལ་དགའ་བས་སོ། །

[Block 1811]
དྲངས་པས་ན་ཞེས་བྱ་བ་ནི་འདྲེན་པར་བྱེད་པ་སྟེ། ཅི་ལྟར་འདི་བསྟན་མ་ཐག་པས་དྲངས་པ་སྟེ། དེ་བས་ན་དེ་ནི་ཚིགས༌[^1055]བཅད་ཀྱིས་སོ། །

[Block 1812]
དེ་ལྟར་བྱས་པས་ཞེས་བྱ་བ་ནི་གྲགས་པའི་སེམས་ཀྱི༌[^1056]ཚིག་གིས་སོ། །

[Block 1813]
ཆོས་ལ་དགའ་ཞིང་ཞེས་བྱ་བ་ནི་མངོན་པར་མཐོ་བ་འདོད་པའི་ཕྱིར་རམ། བདག་ཐར་པ་འདོད་པའི་ཕྱིར་རོ། །

[Block 1814]
སྙིང་རྗེའི་དབང་དུ་གྱུར་ཏེ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གཞན་ལ་ཕན་པའི་དོན་ཏོ། །

[Block 1815]
མདོག་གསལ་བར་བྱས་པ་ནི་མདོག་གསལ་བར་བྱས་པའོ། །

[Block 1816]
བཞིན་མདངས་མ་གྱུར༌[^1057]ཅིང་རབ་ཏུ་དང་བ་ཞེས་བྱ་བ་ནི་བཞིན་མདངས་གསལ་བ་གཟུང༌[^1058]སྟེ། དགའ་བ་ཡིན་པས་རྗེས་སུ་དཔག་གོ། །

[Block 1817]
མི་གཡོ་བར་དེ་བཞིན་འདུག་པ་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ཚོར་བ་ལ་སོགས་པས་སོ། །

[Block 1818]
རབ་ཏུ་དང་བ་ཆེར་གྱུར་ཏོ། །ཞེས་བྱ་བ་ནི། བཞིན་མདངས་མ་གྱུར༌[^1059]ཅིང་གསལ་བའི་ཕྱིར་རོ། །

[Block 1819]
ངོ་མཚར་ཆེར་གྱུར་ཏོ་ཞེས་བྱ་བ་ནི་མི་གཡོ་ཞིང་དེ་བཞིན་དུ་འདུག་པའི་ཕྱིར་ཏེ། ཤ་གཅོད་པ་དང་བཅས་པའི་སྡུག་བསྔལ་གྱིས་སོ། །

[Block 1820]
ངོ་མཚར་ནི་སྙིང་རྗེས་གཞན་ལ་བདེ་བ༌[^1060]འདོད་པ་སྟེ། སེམས་ཅན་ལ་དགའ་བ་ཤས་ཆེ་བའི་ཕྱིར་རོ། །

[Block 1821]
རྨད་དུ་བྱུང་བ་ནི་མི་གཡོ་བར་དེ་བཞིན་འདུག་པ་སྟེ། ཤ་ཆོད་པ་དང་བཅད་པའི་ཚོར་བའི་སྡུག་བསྔལ་ཟིལ་གྱིས་ནོན་པའི༌[^1061]ཕྱིར་རོ། །

[Block 1822]
བདེན་ནམ་བརྫུན་ཞེས་དཔྱོད་ཅིང་ངོ་མཚར་སྐྱེས་ཞེས་བྱ་བ་ནི་ངོ་མཚར༌[^1062]རྨད་དུ་བྱུང་བ་སྐྱེས་པས༌[^1063]སོ། །

[Block 1823]
དེ་ལ་བསྟོད་ཅིང་ཕྱག་ཀྱང་འཚལ་བར་གྱུར། །ཞེས་བྱ་བ་ནི་དེ་ལ་བསྟོད་པ་དང་ཕྱག་འཚལ་བར་གྱུར་པ་སྟེ། དེ་ལ་བསྟོད་པ་དང་འདུད་པ་ནི།[^1064] ཁྲག་དང་ཤ་སྦྱིན་པས་ཕྱག་འཚལ་བའོ། །

[Block 1824]
གུས་པའི་དབང་གིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་གསང་ཚིག་དང་། གཙོ་བོ་དང་། སྤྲོ་བའི་ནུས་པ་བསྟན་ཏོ། །

[Block 1825]
དང་པོའི་རྐང་པས་ནི་གསང་ཚིག་གི་ནུས་པ་བསྟན་ཏེ། [^1065]གུས་པ་དང་གྲགས་པས་ནི་གསང་ཚིག་གི་ནུས་པ་བསྐྱེད་པས་སོ། །
--- END BLOCKS ---
