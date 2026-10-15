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
རང་དང་བརྙ་བ་དང་ཡིད་གཅུགས༌[^1246]པའི་སེམས་དང་གཞན་ལ་གོ་བར་བྱས་པ་རྣམས་ལས་རྣམ་པ་གཞན་གྱིས་ཀྱང་རྐུ་བའི་སེམས་མེད་པར་ལེན་པ་ལ་ལྟུང་བ་མེད་ཅེས་བསྟན་པའི་ཕྱིར། །རྐུ་སེམས་མེད་པ་གཞན་གྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1787]
རྣམ་པ་གཞན་གྱིས་ཀྱང་ཇི་ལྟར་ཉེས་པ་མེད་ཅེ་ན།

[Block 1788]
ཉེ་བ་འཁོར་གྱིས་ཞུས་པ་ལས།

[Block 1789]
དགེ་སློང་གིས་དགེ་སློང་ལ་འདི་སྐད་ཅེས་སྨྲས་ཏེ། ཁྱོད་ཀྱིས་དགེ་སློང་ཆེ་གེ་མོའི་ཡོ་བྱད་དེ་དང་དེ་དག་ཤེས༌[^1247]སམ་ཤེས་སོ། །

[Block 1790]
འོ་ན་སོང་ལ་དེ་དག༌[^1248]རྐུས༌[^1249]ཤིག །དེ་དག་ཕྲོགས་ཤིག །དེ་དག་གནས་ནས་ཡང་གཞན་དུ་སྤོགས་ཤིག་ཅེས་བསྒོ་ནས་ཞེས་བྱ་བའོ། །

[Block 1791]
རྐུ་བའི་སེམས་ཀྱིས༌[^1250]རྐུ་ཞེས་བྱ་བ་འདི་ལ་དོན་གཉིས་དང་ལྡན་པ་ཉིད་དོ། །

[Block 1792]
རྐུ་བར་བྱེད་ཁར་འཇུག་པར་བྱེད་ཅེས་བྱ་བར་མངོན་པར་འདོད་དོ། །

[Block 1793]
འོན་ཏེ་དེ་འདི་སྙམ་དུ་འདི་ནི་ཞེས་བྱ་བ་འདི་ལ་བདག་པོ་ཉིད་ཀྱིས་འདི་ཞེས་བྱ་བ་དོན་གྱིས་ཀུན་དུ་སྤྱོད་པར་གྱུར་པ་རྐུ་བ་མངོན་པར་འདོད་ཅེས་བྱ་བ་དོན་འདི་ཡིན་ནོ། །

[Block 1794]
སྙིང་རྗེས༌[^1251]རྫུ་འཕྲུལ་གྱིས་ཕྲོགས་ནའོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བར་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 1795]
སེམས་ཀྱིས་རིགས་ཉིད་དེ་འདྲ་བ་འདི་ཡིན་གྱི། གང་ཞིག་འདིར་ལྟུང་བ་མི་སྐྱེད༌[^1252]ཅེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 1796]
སྙིང་རྗེའི་སེམས་ཀྱིས་གཞན་ནོར་དང་བྲལ་བ་ལ་ལྟུང་བ་མི་སྐྱེད༌[^1253]པའོ། །

[Block 1797]
དེ་ལྟར་ན་ཡང་འཆད་པར་འགྱུར་བ་སྟེ་སྙིང་རྗེའི་སེམས་ཀྱིས་ནི་ཉེས་བྱས་ཞེས་བྱ་བའོ། །

[Block 1798]
དེ་བས་ན་རྣམ་པ་གསུམ་ཞེས་བྱ་བ་ཁྱད་པར་རོ། །

[Block 1799]
ཐམས་ཅད་དུ་སྦྱོར་བ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་ཐམས་ཅད་ལ་ཡང་སྦྱོར་བ་གང་ཡིན་པ་དེ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 1800]
[^1254]དེ་ནི་སྤྱིར་བཏང་བ་སྟེ། དེའི་དམིགས་ཀྱིས་བསལ་བ་བསྟན་པའི་ཕྱིར། སྡེ་ཚན་དེ་ལ་གལ་ཏེ་དངོས་གཞིའི་ཡིན་ན་སྦོམ་པོའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་དེ་ལ་ཞེས་བྱ་བ་ནི་ཕམ་པ་ལའོ། །

[Block 1801]
སྡེ་ཚན་ལ་སྦོམ་པོ་ནི་སྦྱོར་བའོ། །

[Block 1802]
གལ་ཏེ་དངོས་གཞིའི་ཡིན་ན་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་དེའོ།[^1255] །ཇི་སྟེ་སྦྱོར་བའི་སྦྱོར་བ་ཡིན་ན་དེ་ལ་ནི་ཉེས་བྱས་ཁོ་ནའོ། །

[Block 1803]
འོག་མ་དག་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་སྡེ་ཚན་དེ་ལ་འོག་མ་སྦོམ་པོ་བརྗོད་པ༌[^1256]དངོས་གཞིའི་ཡིན་ན་སྦྱོར་བ་དེ་ལ་ཞེས་བྱ་བ་ནི༌[^1257]འོག་མའི་སྡེ་ཚན༌[^1258]ལ་དགེ་འདུན་ལྷག་མ་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 1804]
འདིར་ཡང་དངོས་གཞིའི་སྦྱོར་བ་ཡིན་ན་སྦོམ་པོའོ། །

[Block 1805]
སྦྱོར་བའི་སྦྱོར་བ་ཡིན་ན་ནི་ཉེས་བྱས་སོ། །

[Block 1806]
མ་ཆོག་པ༌[^1259]བརྐུས་ནའོ་ཞེས་བྱ་བ་སྦོམ་པོའོ་ཞེས་བྱ་བའི་དབང་དུ་བྱ་སྟེ། འདི་མན་ཆད་འོག་ནས་སྙིང་རྗེ་དང་ལྡན་པའི་སེམས་ཀྱིས་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནས་མ་ཤ་ཀ་ལྔར་མ་ཆོག་པ་བརྐུས་ན་གང་ཅུང་ཟད་མ་ཚང་བར་བརྗོད་པ་དེ་ཐམས་ཅད་ནི་དངོས་གཞིའི༌[^1260]ཆོ་ག་ལའོ། །

[Block 1807]
དེ་བས་ན་འདིར་ཇི་ཙམ་དུ་དངོས་གཞིའི་ཆོ་ག་ལ་བརྟེན་པའི་རྣམ་འགྱུར་དུ་གྱུར་པའོ། །

[Block 1808]
དེ་ལས་གཞན་པའི་དངོས་གཞིའི་ཆོ་ག་བརྟེན་པ་དེ་ལ་རྗེས་སུ་སྦྱོར་བའོ། །

[Block 1809]
དཔེར་ན་རྐུ་བ་དང་རྐུར་བཅུག་པ་དང་མངགས་པ་དང༌[^1261]མ་བྱིན་པ་དང་། རྐུ་སེམས་ཀྱིས་མིའི་རྒྱུད་ཀྱིས་ཡོངས་སུ་བཟུང་བར་འདུ་ཤེས་པ་དང་ཞེས་བྱ་བ་འདི་རྣམས་དངོས་གཞིའི་ཆོ་ག་ལ་གཏོགས་པའི་ཡན་ལག་རྣམས་མདོ་འདི་ལ་རྗེས་སུ་སྦྱར་བའོ། །

[Block 1810]
དེ་བས་ན་ཁྱད་པར་འདི་དང་ལྡན་པའི་ཆོ་ག་འདི་ལ་སྦོམ་པོ་འདི་རིག་པར་བྱའོ།[^1262] །གཞན་དུ་ཡང་དེ་དང་རྗེས་སུ་འབྲང་བས་རྟོགས་པར་བྱའོ། །

[Block 1811]
མི་མ་ཡིན་པའི་འགྲོ་བ་དང་འབྲེལ་པ་ལ་དེའི་འདུ་ཤེས་དང་མིའི་འགྲོ་བ་ལ་བརྟེན་པའི་འདུ་ཤེས་ཀྱིས་མ་ཆོག་པ་བརྐུས་པ་ལ་སྦོམ་པོའི་ལྟུང་བ་བྱུང་བ་ལ་དམན་པ་ཉིད་ཀྱི་ཕྱིར་ཉེས་བྱས་སོ། །

[Block 1812]
གང་དེའི་བདག་པོ་ཉིད་ཡོངས་སུ་བཟུང་བ་དང་མ་ཆོག་པ་དང་མིའི་འགྲོ་བ་པ་ཡོངས་སུ་འཛིན་པ་ཉིད་ཀྱི་ཕྱིར་འདུ་ཤེས་ལ་ཉེས་བྱས་ཉིད་དོ། །

[Block 1813]
རྐུ་བའི་སེམས་མེད་ན་ཐམས་ཅད་དུ་ལྟུང་བ་མེད་དོ། །

[Block 1814]
གང་གི་ཕྱིར་འདིར་རྐུ་བའི་སེམས་ནི་ལྟུང་བ་བྱས་པ་སྟེ། ཡན་ལག་གཞན་རྣམས་ལ་ནི་དེའི༌[^1263]ཁྱད་པར་དུ༌[^1264]བྱས་པ་ཉིད་དོ། །

[Block 1815]
བདག་པོ་མེད་པའི་གཏེར་རོ་ཞེས་བྱ་བ་ནི་མ་བྱས་པ་ལ་འདིར་བདག་པོ་ཉིད་ཅི་འདྲ་བ་སྟེ། གང་ཞིག་དོན་རྟོགས་པའི་བདག་པོས་ཡིན་གྱི་དོན་མ་རྟོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1816]
ཡུལ་གྱི་བདག་པོའམ་དེའི་རིགས་དང་ལྡན་པས་མ་རྟོགས་པར་གྱུར་པ་ལ་གང་དང་བཅས་པས་དེའི་རིག༌[^1265]ཆད་པ་དེ་རྒྱལ་པོས་མ་ཤེས་པ་དང་མ་བྱས་པ༌[^1266]ལ་སྦོམ་པོའི་ལྟུང་བའོ། །

[Block 1817]
འདིར་དོན་མ་རྟོགས༌[^1267]པའི་བདག་པོ་རྒྱལ་པོ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་བས་ན་ཅིའི་ཕྱིར་ཕམ་པ་མ་ཡིན་ཏེ། བདག་ཏུ་བྱས་པ་ཉིད་ཀྱི་ཆད་པས་ཡོངས་སུ་མ་རྫོགས་པའི་ཕྱིར་རོ། །

[Block 1818]
དེ་ལྟར་ན་གཞུང་ནི། དེས་ནད་གཡོག་ལ་སྨྲས་པ། ཁུར་བ་སྣ་གསུམ་དང་ཐུག་པ་སྟ་གོན་གྱིས་ཤིག་དང་དགེ་འདུན་ལ་ཡང་དབུལ་རང་ཡང་བཟའ་བཏུང་བྱའོ་ཞེས་ཟེར་ནས་དེས་དེ་དག་ལ་ཟོང་ཕོག་གོ། །

[Block 1819]
དེ་དག་འདི་སྙམ་དུ་བདག་ཅག་ལ་ཁུར་བ་སྣ་གསུམ་པ་དང་ཐུག་པས་ཅི་བྱ། འདི་ལ་ཁུར་བ་སྣ་གསུམ་དང་ཐུག༌[^1268]པ་ཞིག་བྱིན་ལ་ཟོང་བདག་ཅག་གིས་བགོ་བར་བྱའོ་སྙམ་ནས་དེ་དག་གིས་དེ་ལ་ཁུར་བ་སྣ་གསུམ་པ་དང་ཐུག་པ་ཞིག་བྱིན་ཏེ་ཟོང་བགོས་སོ། །

[Block 1820]
དེ་ལ་འགྱོད་པ་སྐྱེས་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཕམ་པར་འགྱུར་བའི་ལྟུང་བ་ནི་མེད་དེ། ཉེས་པ་སྦོམ་པོའི་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། གང་དག་ལ་ཕུལ་བ་དེ་དག་ལ་དེར་བདག་གིར་བྱ་བ་སྐྱེས་པར༌[^1269]མ་གྱུར་པས་དེའི་ཕྱིར་ཕམ་པར་འགྱུར་བའི་རྒྱུ་མེད་པས༌[^1270]སྣང་ངོ་། །འོ་ན་མ་ཆད་པ་ལ་བདག་ཏུ་བྱ་བ་མེད་པ་ལ་ཇི་ལྟར་སྐྱེད་པ༌[^1271]སྟེ། དེར་གཏོགས་པ་ཉིད་ཀྱིས་རྫས་དེ་ལ་གནས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1821]
ཇི་སྟེ་དོན་མ་རྟོགས་པའི་བདག་པོས་ཀྱང་གང་ཞིག་བདག་པོ་མེད་པ་ཉིད་ནི་དཔེར་ན་སུས་ཀྱང་བདག་ཏུ་མ་བྱས་པའི་དགོན་པ་ལ་གནས་པའི་གཏེར་ལ་ཇི་ལྟར་སྒྲུབ་ཅེ་ན། བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་ཀྱི༌[^1272]རྫས་རྐུས་པ༌[^1273]བཞིན་དུ་དེ་ལ་མ་བྱིན་པར་ལེན་པ་མེད་དེ། [^1274]བདག་ཏུ་མ་བྱས་པ་ཉིད་ཀྱི༌[^1275]ཕྱིར་རོ། །

[Block 1822]
ཇི་སྟེ་རྐུ་སེམས་སྐྱེད་པར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 1823]
འདིར་དངོས་གཞིའི་ཆོ་ག་ལ༌[^1276]གཏོགས་པའི་ཡན་ལག་རྣམས་ལ་མིའི་འགྲོ་བ་པ༌[^1277]ཡོངས་སུ་གཟུང་བར་བྱ་བ་འདིས་སྤང་བའི་དོན་དུ་སྦྱར་བའོ། །

[Block 1824]
དེའི་འདུ་ཤེས་ཀྱིས་ཞེས་བྱ་བ་ལ་དེ་ལ་བདག་པོ་མེད་པའི་གཏེར་གྱི་འདུ་ཤེས་ཀྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1825]
བྱེ་བྲག་འདི་དང་ལྡན་པ་རྣམས་ལ་འདི་ནི་སྦོམ་པོ་སྟེ། བདག་པོ་མེད་པའི་གཏེར་ལ་བདག་པོ་དང་བཅས་པའི་འདུ་ཤེས་ཀྱིས་མིར་གྱུར་པའི་བདག་པོས་སམ་གཞན་གྱིས་ཀྱང་སྦོམ་པོ་ཉིད་དོ། །
--- END BLOCKS ---
