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
ཡིད་དུ་འོང་བ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཡིད་དུ་འོང་བའི་རྒྱུ་ཉེ་བར་བསྒྲུབ་པ་སྒྲོགས་ན་ཉེས་བྱས་སོ། །

[Block 1787]
གང་གི་ཕྱིར་འདི་ལ་འཇིགས་པའི་རྒྱུ་ཡོངས་སུ་རྫོགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་འདི་ལ་ཤིན་ཏུ་ཡིད་འབྱུང་བར་བྱེད་པ་ཉིད་མ་ཡིན་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1788]
འདིར་ཡིད་དུ་འོང་བ་དཔེ༌[^1138]བསྟན་པའི་ཕྱིར། འདི་ལྟ་སྟེ་དཔེར་ན་ལྷ་དང་ཀླུ་དང་དྲི་ཟ་དང་གནོད་སྦྱིན་དང་མིའམ་ཅི་དང༌[^1139]ལྟོ་འཕྱེ་ཆེན་པོ་གཟུགས་ནོར་ཅན་དང་ཚོང་དཔོན་དང་དེད་དཔོན་ལ་སོགས་པ་ལྟ་བུ། པི་ཝང་ལ་སོགས་པའི་སྒྲ་ལྟ་བུའོ་ཞེས་བྱ་བ་ལ། འདིར་སོགས་པའི་སྒྲས་ནི་གླིང་བུ་དང་བ་ལ་རི་དང་མ་ཧཱ་ཏི་དང་སུ་གོ་ཥ་ལྟ་བུ་རྣམས་ཀྱང་བསྡུའོ། །

[Block 1789]
ཨ་ཀ་རུ་དང་ཙན་དན་དང་གུར་གུམ་དང་། ཏ་མ་ལའི་ལོ་མའི་དྲི་ལྟ་བུ་དང་། དར་དང་རས་ཡུག་ཆེན༌[^1140]དང་བེའུ་རས་དང་དར་ལ༌[^1141]དང་དུ་ཀུ་ལའི་རས་དང་། ཀོ་ཏམ་པའི་རས་ཀྱི་རེག་པ་ལྟ་བུ་རྣམས་ཉིད་སྒྲོགས་པའོ་ཞེས་བྱ་བ་ནི་ཇི་སྲིད་ལྷ་ལ་སོགས་པ་འདི་ན་ཡོད་དོ་ཞེས་སྒྲོགས་ཤིང་ཞེས་བྱ་བ་འདི་ལ་འདིར༌[^1142]ཐམས་ཅད་དུ་སྦྱར་བར་རིག་པར་བྱའོ། །

[Block 1790]
འདིར་ལྷ་ལ་སོགས་པ༌[^1143]སྨོས་པ་ནི་མཚོན་པ་ཙམ་ཡིན་ཏེ་ཤིན་ཏུ་ཆེ་བའི་ཡི་དགས་ལ་སོགས་པ་རྣམས་ཀྱང་འདིར་བསྡུས་པའོ། །

[Block 1791]
ཅི་འདིར་འཇུག་པ་ཐམས་ཅད་ལ་ཁ་ན་མ་ཐོ་བ་འདི་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་སྐྱོ་བར་བྱ་བའི་ཆེད་ཉིད་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འཇུག་པ་འདི་ལ་རྣམ་པ་འདི་ལྟ་བུ་དག་མ་གཏོགས་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1792]
གང་གི་ཕྱིར་འཇུག་པ་འདི་ལས་འཇུག་པ་གཞན་ནི་ཁ་ན་མ་ཐོ་བ་དེ་བས་ན་དེའི་ཕྱིར་སྐྱོ་བར་བྱ་བའི་ཆེད་དུ་སེམས་ཅན་དམྱལ་བ༌[^1144]དང་དུད་འགྲོ་དང་། ཡི་དགས་ཀྱི་གཏམ་ལ་སོགས་པ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1793]
སྔངས་པར་བྱེད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1794]
ཅི་ཞིག་བྱས་ན་སྦེད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རབ་ཏུ་བྱུང་བ་འདི་པ་དབང་བའི་ལྷུང་བཟེད་དང་། ཆོས་གོས་དང་དྲ་བ་དང་ཕོར་བུ་དང་སྐེ་རགས༌[^1145]ལ་སོགས་པ་དགེ་སློང་གི་འཚོ་བའི་ཡོ༌[^1146]བྱད་སྦེད་དུ་བཅུག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སངས་རྒྱས་ཀྱིས་གསུངས་པའི་རབ་ཏུ་བྱུང་བ་འདི་པ་དབང་བའི་ལྷུང་བཟེད་ལ་སོགས་པ་དེ་དག་དགེ་སློང་གི་འཚོ་བའི་ཡོ་བྱད་ཚད་དང་ལྡན་པ་རུང་བ་རང་གིས༌[^1147]སྦེད་དམ་སྦེད་དུ་འཇུག་ན་ཞེས་བྱ་བའི༌[^1148]དོན་ཏོ། །

[Block 1795]
རབ་ཏུ་བྱུང་བ་འདི་པ་ཞེས་བྱ་བ་སྨོས་པ་ནི་དགེ་སློང་དང་དགེ་སློང་མ་དང་དགེ་སློབ་མ་དང་དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་དང་ཞེས་བྱ་བ་ཐམས་ཅད་ནི་རབ་ཏུ་བྱུང་བ་འདི་པའི་གང་ཟག་རྣམས་ཉེ་བར་བསྡུ་བའི་དོན་དུའོ། །

[Block 1796]
ཅི་དུས་གང་ཡང་རུང་བ་ལ་མ་བྱས་པ་འདི་དག་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཕན་པར་འདོད་པས་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིས༌[^1149]ལྟུང་བ་མེད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1797]
སྦེད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1798]
གང་ལ་བྱིན་པས་ཉེ་བར་འཚོ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་ལ་གོས་བླངས་པ༌[^1150]མེད་པར་བྱིན་པ་དེས་གནང་བ་མེད་པར་སྤྱོད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐམས་ཅད་ཀྱང་ཐམས་ཅད་དུ་བྱིན་པའི་དགེ་སློང་གིས༌[^1151]གོས་གང་ལ་སྦྱིན་པ་དེ་རྗེས་སུ་གནང་བ་མེད་པར་ཡོངས་སུ་ལོངས་སྤྱོད་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1799]
རང་གི་བློས་ཉེ་བར་འཚོ་བ་ལ་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་རོ། །

[Block 1800]
གཞན་གྱི་བློས་ནི་སྦོམ་པོ་སྟེ། འདིར་མ་བྱིན་པར་ལེན་པ་ཉེ་བར་འབྲེལ་པའོ། །

[Block 1801]
དེ་བས་ན་མ་བྱིན་པ་ལ་ཁ་ན་མ་ཐོ་བ་འདི་བསྐྱེད་པའོ། །

[Block 1802]
འདི་རང་གི་བློ་ལ་ཉེས་པ་མེད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1803]
གཞན་གྱི་ལ་འདི་ནི་བདག་གི་ཡིན་ནོ་སྙམ་དུ་འཁྲུལ་པར་འགྱུར་བའི་གོ་བ་གྲུབ་པའོ། །

[Block 1804]
རང་གི་བློ་འཁྲུལ་པར་གྱུར་པས་འདི་དང་གཞན་ལ་ཡང་ཉེ་བར་སྦྱོར་བ་ལ་ཉེས་པ་མེད་དོ། །

[Block 1805]
གོས་དང་ཡོ་བྱད་ལྷག་མ་རྣམས་ལ་ཡང་ཐོག་མ་ཉིད་དུ་འདིར་ཁ་ན་མ་ཐོ་བ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1806]
ལྷུང་བཟེད་ལ་ནི་ཡོངས་སུ་རྫོགས་པ་སྟེ། ལྷུང་བཟེད་ཆུང་བ་ལ་ནི་ན་སྨད་པར་རིག་པར་བྱའོ། །

[Block 1807]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས།

[Block 1808]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་ལ་ལྷུང་བཟེད་དང་ཆོས་གོས་སྦྱིན་པར་བྱ་སྟེ། དེའི་འོག་ཏུ་སླར་འཕྲོག་པར་བྱེད་ཅིང་ལོངས་སྤྱོད་པར་བྱེད་ན་ལྟུང་བ་ཅིར་འགྱུར། ལྟུང་བྱེད་དོ། །

[Block 1809]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་ལྷུང་བཟེད་དམ༌[^1152]ཆོས་གོས་དགེ་སློང༌[^1153]གཞན་དང་གཞན་ལ་འཚོ་བའི་ཡོ་བྱད་དུ༌[^1154]བྱིན་ནས་འཕྲོག་པར་བྱེད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1810]
འདིར་སྔ་མ་ལ་ལྷུང་བཟེད་དང་ཆོས་གོས་ལས་གཞན་མ་བཟུང༌[^1155]བའོ། །

[Block 1811]
འདི་ལ་ནི་ཉེས་པ་མེད་པས་མ་བཟུང་བ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1812]
ཕྱི་མ་ནི་བཟུང་བས་འདི་ལ་ནི་ཉེས་བྱས་སུ་འགྱུར་བ་ཞེས་བྱ་བ་ནི་ཤེས་བྱེད་དོ། །

[Block 1813]
ཕྱི་མ་ལ་ལྷུང་བཟེད་དམ་ཆོས་གོས་ཞེས་བྱ་བ་འདི་ལྷུང་བཟེད་དམ་ཆོས་གོས་ལས་གཞན་པ་ཞེས་བྱ་བ་ཉམས་པའོ། །

[Block 1814]
དེའི་རྗེས་སུ་གནང་བ་མེད་པ་ཞེས་བྱ་བ་ནི་གང་ལ་བྱིན་པ་དེའི་རྗེས་སུ་གནང་བ་སོ་སོར་བཟུང་ནས་ཞེས་བྱ་བ་ནི་བསྡུ་བའོ། །ཅི་བསམ་པ་གང་ཡང་རུང་བས་སྤྱོད་པ་ལ་འམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་གཞི་དེས་དེ་དག་དགའ་བར་མི་འགྱུར་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཞེས་བྱ་བ་ནི་གང་ལ་བྱིན་པ་དེས་ཡིད་ཆེས་པས་ལོངས་སྤྱོད་པ་ལ་ལྟུང་བ་མེད་ཅེས་བྱའོ། །

[Block 1815]
བྱིན་པས་ཉེ་བར་འཚོ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1816]
ཅི་ཞིག་བྱས་ན་སྐུར་པ་འདེབས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྐུར་པ་འདེབས་པར་འདོད་པས་དགེ་སློང་ལ་འདུ་ཤེས་བསྒྱུར་ཏེ། དགེ་འདུན་ལྷག་མས་སྐུར་པ་བརྗོད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་ལྷག་མའི་ལྟུང་བས་སྐུར་པ་འདེབས་པར་འདོད་པས་སྐུར་པ་འདེབས་པ་གང་ཡིན་པ་དེའི་འདུན་པས་ཤེས་པར་རིག་པར་བྱའོ། །ཅི་དངོས་སུ་སྐུར་པ་འདེབས་པ་ཁོ་ན་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་བག་ཙམ་གྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ།

[Block 1817]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 1818]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་བསླབ་པ་སྩལ་བ་ཙམ་གྱིས་དགེ་འདུན་ལྷག་མས་སྐུར་པ་འདེབས་པར་བྱེད་ན་ལྟུང་བ་ཅིར་འགྱུར། ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1819]
སྐུར་པ་འདེབས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1820]
སྔར་ལམ་དུ་འགྲོ་བ་ལ་བུད་མེད་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 1821]
གང་ཞེས་སྨོས་པ་དེ་ཅི་གཞན་གང་ཡང་རུང་བ་ལ་དེ་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་འདོད་པས་ལམ་དུ་འགྲོ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་དགར་ལམ་དུ་འགྲོ་ན་སྟེ། གཞན་དབང་གིས་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1822]
ལམ་ཇི་སྲིད་དུ་འགྲོ་བ་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རྒྱང་གྲགས་རེ་རེར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྟུང་བྱེད་ཉིད་ལ་འདིར་བྱེད་པ་པོ་ཉིད་ནི་འདི་ཡིན་ནོ་ཞེས་བྱ་བ་བྱེ་བྲག་མ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རྟོགས་པའོ། །

[Block 1823]
དེའི་ཕྱེད་རེ་རེ་ཉིད་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་རྒྱང་གྲགས་ཀྱི་ཕྱེད་རེ་རེར་ནི་བུད་མེད་ཀྱི་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 1824]
རྒྱང་གྲགས་རེ་རེར་རིག་པའི་སྐྱེས་པ་མེད་པར་བུད་མེད་དང་ལྷན་ཅིག་ཏུ༌[^1156]རང་དགར་ལམ་དུ་འགྲོ་བ་ལ་སྤྲོས་པ་ནི་ཤེས་པར་བྱའོ། །

[Block 1825]
ཅི་བུད་མེད་ཀྱི་གནས་སྐབས་ཐམས་ཅད་དགེ་སློང་གི༌[^1157]གནས་སྐབས་རྣམས་ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་བསེལ་བྱེད་པ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ༌[^1158]སྨོས་ཏེ། དགེ་སློང་དེ༌[^1159]ཉིད་ཅེས་བྱ་བ་འདི་ལ་འདིར་ཉེ་བར་གནས་པ་ཉིད་ཀྱི་ཕྱིར་རྟོགས་པར་བྱའོ། །
--- END BLOCKS ---
