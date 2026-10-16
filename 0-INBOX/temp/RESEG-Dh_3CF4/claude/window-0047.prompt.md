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
[Block 1646]
བུ་ཡུག་གིས་ཀུན་ཏུ་འདྲེས་པའི་རླུང་ནི་བུ་ཡུག་རླུང་ངོ་། །བུ་ཡུག་རླུང་གིས་རྙིས་པར་བྱས་པ་ནི་བུ་ཡུག་རླུང་གིས་རྙིས་པ༌[^933]སྟེ། དེ་ལྟ་བུའི་པདྨ་ནི་བུ་ཡུག་རླུང་གིས་རྙིས་པའི༌[^934]པདྨའོ། །

[Block 1647]
བརྟན་ཞིང་རྒྱས་པ་ཞེས་བྱ་བ་ལ་བརྟན་པ་དང་རྒྱས་པ་ནི་བརྟན་ཞིང་རྒྱས་པའོ། །

[Block 1648]
བརྟན་པའི་ཁྱད་པར་ནི་རྒྱས་པ་སྟེ་རྣམ་པ་གཉིས་སོ། །

[Block 1649]
ནད་ལ་སོགས་པས་རྒྱས་པར་གྱུར་པ་ནི་དེ་ལྟ་བུ་མ་ཡིན་ནོ། །

[Block 1650]
བདག་རང་ཤི་བ་ཞེས་བྱ་བ་ནི་མངོན་པར་འདོད་པའི་སྦྱིན་པ་མ་ཡིན་པའོ། །

[Block 1651]
གསོན་པའི༌[^935]ཤ་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་མངོན་པར་འདོད་པའི་སྦྱིན་པའི་དངོས་པོ་གཞན་ལ་མེད་པའོ། །

[Block 1652]
འདི་དག་བདག་གི་ཐ་དད་དུ། །ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་མི་སྦྱིན་པ་ནི་རྗེས་སུ་མཐུན་པ་མ༌[^936]ཡིན་པ་སྟེ། སྐྱོན་གསུམ་པོ་འདི་སྤངས་པའི༌[^937]ཐབས་བསྟན་པར་འདོད་པས་སོ། །

[Block 1653]
དེ་བས་ན་འདི་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྩམས་སོ། །

[Block 1654]
གདུངས་པའི་རྨ་འདྲ་བ་ཞེས་བྱ་བ་ནི་འདི་ལྟ་བུའི་མཚན་ཉིད་དེ་རྟག་ཏུ་ན་བ་འདི་ལྟ་བུའི་ལུས་ཏེ། རྟག་ཏུ་ན་བ་ནི་ལུས་ནད་དང་བྲལ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1655]
རྟག་ཏུ་ན་བའོ་ཞེས་བསྟན་པ་ལ། ཇི་ལྟར་རྟག་ཏུ་ན་བ་ཉིད་ཡིན་ཞེ་ན་ནད་ཀྱི་འབྱུང་ཁུང་ཞེས་སྨོས་ཏེ། ནད་ནི་གནོད་པ་བྱེད་པ་སྟེ། དེ་ནི་ཚོར་བར་བྱེད་པའི་ཕྱིར་གདུངས་པའི་རྨ་ལ་སོགས་པའི་ནད་ཀྱི་ཡང་འབྱུང་གནས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1656]
ཡང་ན་ནད་ཀྱི་འབྱུང་ཁུང་ཞེས་བྱ་བ་ནི་ནད་ཀྱི་ཚོར་བ་སྟེ། དེའི་འབྱུང༌[^938]གནས་ཡིན་པའི་ཕྱིར་ཏེ། གང་ཅུང་ཟད་ཚོར་བ་དེ་ནི་སྡུག་བསྔལ་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 1657]
དགོས་པ༌[^939]ཁྱད་པར་ཅན་དུ་སྤྱད་པ་ཡིས། །ཞེས་བྱ་བ་ནི་འབྲས་བུ་དང་བྲལ་བ་ནི༌[^940]སྡུག་བསྔལ་ཉེ་བར་ཞི་བ་སྟེ། དེ་ཉིད་ཀྱི་ཁྱད་པར་ནི་སྔར་བསྟན་པའི་རྣམ་པ་སྟེ། སྡུག་བསྔལ་གྱི་སྡུག་བསྔལ་ལ་སྡུག་བསྔལ་གྱིས་ཉེ་བར་སྤྱད་པ་ནི་དགོས་པ་ཁྱད་པར་ཅན་དུ་སྤྱོད་པའོ། །

[Block 1658]
ཤིན་ཏུ་བཟང་པོར་བྱ་བ་ཞེས་བྱ་བ་ནི་གཅིག་ཏུ་ནད་གཏན་དུ་ཉེ་བར་ཞི་བར་བྱེད་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་དང་།[^941] ཤིན་ཏུ་བཟང་པོ་ནི་གཞན་ལ་ཕན་འདོགས་པ་མཆོག་ཏུ་བྱེད་པའི་ཕྱིར་ཏེ། ཉན་ཐོས་ལ་སོགས་པ་ཡང་རྩ་འབིགས་ཤིང་གསོ་བ་སྟོན་པར་བྱེད་དེ། [^942]འདིར་བཅོས་པ་གཉིས་ཀྱི་ཁྱད་པར་ནི་གདུངས་པའི་རྨའི་རྩ་བཀྲོལ༌[^943]ཏེ། འདི་དག་ལ་ནི་དགོས་པ་ཁྱད་པར་ཅན་དུ་སྤྱད་པ་མེད་དེ། དེ་བས་ན་འདི་ནི་ཤིན་ཏུ་བཟང་པོ་མ་ཡིན་ནོ། །

[Block 1659]
དེ་རབ་ཏུ་དགའ་བར༌[^944]གྱུར་པས་མིག་རྩ་དང་། གདོང་གི་མདངས་བཟང་པོ་གང་ཡིན་པ་དེ་ནི་རབ་ཏུ་དགའ་བར་གྱུར་པས་མིག་རྩ་དང་གདོང་གི་མདངས་བཟང་པོའོ། །

[Block 1660]
བདག་གི་ཤ་ནི་ཁྲག་དང་བཅས་པ་འདི། །ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པའི་དངོས་པོ་དོན་དུ་གཉེར་བའི་མཚན་ཉིད་དང་ལྡན་པ་ཉིད་དུ༌[^945]བསྟན་ཏོ། །

[Block 1661]
འཇིག་རྟེན་རྣམས་ལ་ཕན་པའི་ཕྱིར། །ཞེས་བྱ་བ་འདིས་ནི་ཁྱེད་ཅག་གི་དོན་དུ་འདི་བཟུང་བ༌[^946]ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་གིས་ཡོངས་སུ་གཏོང་བ་དེ༌[^947]ཡོངས་སུ་གཏོང་བ་ནི་སྔར་ཡོངས་སུ་བཏང་བའོ་ཞེས་གཞན་གྱི་ངོར་བྱེད་པ་བཞིན་ཏེ། ལེན་པར་མི་འགྱུར་བའི་རྒྱུ་མེད་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 1662]
མགྲོན་དུ་བྱར་རུང་ན༌[^948]ཞེས་བྱ་བ་ནི་མགྲོན་ཉིད་དུ་རུང་བ་ནི་མགྲོན་བྱར་རུང་བའོ། །

[Block 1663]
ཆེན་པོ་འབྱུང་བར་འགྱུར་བ་ནི་འབྲས་བུ་ཆེན་པོ་སྟེ། འཇིག་རྟེན་ཐམས་ཅད་ལ་ཕན་པའི་ཕྱིར་རོ། །

[Block 1664]
མངོན་པར་མཐོ་བ་འབྱུང་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་ཏེ། ཁྱད་པར་ཅན་གྱི་མངོན་པར་མཐོ་བ་སངས་རྒྱས་ཉིད་ལ་མངོན་པར་མཐོ་བ་ཞེས་བརྗོད་དོ། །

[Block 1665]
ཡིད་མ་ཆེས་ནས་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཡིད་ཆེས་ན་ནི་བརྟན་པ་ཡིན་ཏེ། ཅུང་ཟད་དེ་ལ་མི་བརྟན་པ་ཡོད་པས་གང་གི་ཕྱིར་བྱིན་ཅིག་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨྲ་བས་མི་བརྗོད་དེ། དེ་བས་ན་ཡིད་མི་ཆེས་པའོ་ཞེས་རྟོགས་པ་ཡིན་ནོ། །

[Block 1666]
བདག་གི་སྡུག་བསྔལ་དག་ཅེས་བྱ་བ་ནི་བཀྲེས་པའི་སྡུག་བསྔལ་ལོ། །

[Block 1667]
སློང་བ་ཉིད་དམན་པ་ཡིན་པས་སློང་ཞིང་དམན་པའོ། །

[Block 1668]
དེ་ལས་དུས་ལ་བབ་པ་ཞེས་བྱ་བ་ནི་སྦྱིན་པར་བྱ་བ་བཏུང་བར་བྱ་བ་སྟེ། རང་གི་ཁྲག་དང་ཤའོ། །

[Block 1669]
སྦྱིན་པ་ལ་རྩོལ་བ་ནི་སྦྱིན་པར་སྩོལ་བ༌[^949]སྟེ། རང་གི་ཤ་ཁྲག་སྟེ་སྦྱིན་པར་སྩོལ༌[^950]བའོ། །

[Block 1670]
རྟབ་རྟབ་པོར་གྱུར་ཏེ༌[^951]མི་བཟོད་ཅིང་སེམས་འཁྲུགས་ནས་ཞེས་བྱ་བ་ལ། རྟབ་རྟབ་པོར་གྱུར་པ་ནི་རང་གི་ཤ་དང་ཁྲག་སྦྱིན་པར་བྱེད་པས་སོ། །

[Block 1671]
དེའི་སྡུག་བསྔལ་དེས་མི་བཟོད་ཅིང་སྦྱིན་པར་བྱ་བ་མ་ཡིན་པ་སྦྱིན་པ་སྟེ། དེ་གཉིས་ཀྱིས་སེམས་འཁྲུགས་པར་གྱུར་པའོ། །

[Block 1672]
སྦྱིན་པ་ལ་ཧ་ཅང་དགྱེས༌[^952]ཆེས་པས་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་བྱས་པའི་དགྱེས་པ་ནི་སྦྱིན་པ་ལ་དགྱེས་པའོ། །

[Block 1673]
དེ་ལ་ཧ་ཅང་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་རོ་ཚོར་བ་སྟེ། སྦྱིན་བ་ལ་ཧ་ཅང་དགྱེས་པའོ། །

[Block 1674]
དེ་བས་ན་ཕན་པ་དང་གནོད་པ་ཞེས་བྱ་བ་ལ། ཕན་པ་དང་གནོད་པའི་རིམ་པ་ནི་ཕན་པ་དང་གནོད་པར་གྱུར་པ་སྟེ། རིམ་པ་དང་གང་གིས་ཕན་པ་དང་གནོད་པའོ། །

[Block 1675]
དེ་ཉིད་ནི་འོག་ནས་འབྱུང་བ་བཞིན་དུ་རྟོགས་པར་བྱའོ། །

[Block 1676]
མི་མཁྱེན་པ་ཡང་མ་ལགས་ཏེ། ཞེས་བྱ་བ་ནི་མཁྱེན་པ་ཉིད་དེ། སྐྱེས་བུ༌[^953]རྣམས་ལ་གནོད་པར་འབྱུང་བ་ནི་སྐྱེ་དགུ་རྣམས་ལ་གནོད་པ་སྟེ། ཕན་པ་མ་ཡིན་པ་བསྐྱེད༌[^954]པའོ། །

[Block 1677]
དེ་ལ་ཕན་པ་མ་ཡིན་པ་འབྱུང་བ་ལ་ཅིའི་ཕྱིར་དེ་དགའ་བ་ཡིན་ཞེ་ན། གཞན་ལ་གནོད་པས་འཚོ་ཞིང་དགའ་བ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1678]
གཞན་ལ་གནོད་པར་བྱེད་པ་ནི་གཞན་ལ་གནོད་པ་སྟེ། དེས་འཚོ་ཞིང་དགའ་བ་གང་ཡིན་པ་དེ་དག་ནི་གཞན་ལ་གནོད་པས་འཚོ་ཞིང་དགའ་བ་སྐྱེ་བའོ། །

[Block 1679]
དེ་བས་ན་དེ་དག་ནི་དེས་དགའ་བ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར་རང་བཞིན་དེ་ལྟར་ལགས་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིས་ནི་ཆོས་ཉིད་ཀྱི་རིགས་པས་རིགས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1680]
ད་ནི་ཕན་པའི་རིམ་པ་ལ་མི་གཟིགས་པའི་དབང་དུ་བྱས་ཏེ། འདི་སྐད་སྟོན་ཏེ། སྦྱིན་པ་ལ་ནི་རྣམ་པ་འདི་གསུམ་བསམ་པར༌[^955]བྱ་སྟེ། ལེན་པ་པོ་དང་། སྦྱིན་པ་པོ་དང་། སྦྱིན་པར་བྱ་བ་སྟེ།

[Block 1681]
གསུམ་པ་ནི༌[^956]ཕུན་སུམ་ཚོགས་པ་ཡིན་ན་ནི་སྦྱིན་པ་ཕུན་སུམ་ཚོགས་པར་འགྱུར༌[^957]ཏེ། དེ་ལ་ལེན་པ་པོ་ཡོན་ཏན་མེད་པའི་དབང་དུ་བྱས་ནས། སྐྱེ་དགུ་རྣམས་ལ་གནོད་པ་གང་དང་གང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 1682]
སྦྱིན་པ་པོ་དང་སྦྱིན་པའི་དབང་དུ་བྱས་ནས། རྒྱལ་སྲིད་དཔལ་འདི་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 1683]
དེ་ལས་སྐྱེ་དགུ་ལ་ཕན་པའི་དབང་དུ་བྱས་ནས། རྒྱལ་སྲིད་དཔལ་འདི་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་དང་པོའོ། །

[Block 1684]
དེ་བས་བདག་གི་ཤ་སྦྱིན་སྩོལ་བའི་ཞེས་བྱ་བ་ནི་སྦྱིན་བའི༌[^958]དངོས་པོའི་དབང་དུ་བྱས་པ་སྟེ། བདག་གི་ཤ་སྦྱིན་པར་སྩོལ་བ་ཐོང་ཤིག་ཅེས་བྱ་བ་ནི་རང་གི་ཤ་སྦྱིན་པ་ལ་སྩོལ་བ༌[^959]ནི་རང་གི་ཤ་སྦྱིན་པ་ལ་སྩོལ་བའོ།[^960] །བདག་གི༌[^961]ཤ་སྦྱིན་པར་སྩོལ་བ་ཉིད་ནི་བདག་གི་ཤ་སྦྱིན་པར་སྩོལ་བ་སྟེ། ངེས་པར་བཟུང་བ༌[^962]ནི་སྩོལ་བ་དང་གཏོང་བ་དང༌[^963]སྦྱིན་པ་རབ་ཏུ་དགག་པ་སྟེ། རང་གི་ཤ་སྦྱིན་པ་ནི་ངེས་པར་བཟུང༌[^964]བའོ། །

[Block 1685]
གཞན་གྱི་ཤ་སྦྱིན་པ་ནི་དགག་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
