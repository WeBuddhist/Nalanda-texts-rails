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
ཁྱིའི་མདུན་དུ་གཅི་བར་མི་བྱའོ། །

[Block 1717]
གང་དུ་སྲོག་གི་བར་ཆད་འབྱུང་བའི་དགོན་པ་དེར་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། མིའམ་ཅི་མོའི་དབང་བའི༌[^1203]གླེང་གཞིར་གྱུར་པའི་བསླབ་པའི་གཞི་ལ་དེ་བསྡུ་བ་ཡིན་ནོ། །

[Block 1718]
འདིར་གཞུང་ནི། ཡང་དགེ་སློང་གིས་གང་ན་ཉེས་དམིགས་དེ་ལྟ་བུ་ཡོད་པའི་དགོན་པ་དེ་ལྟ་བུར་ལྷག་པར་གནས་པར་མི་བྱ་སྟེ། གང་ན་འདི་ལྟ་བུའི་འཇིགས་པའི་ངོ་བོ་ཡོད་པར་གྱུར་པའི་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1719]
གང་ན་ཡན་ལག་གི་རྣམ་པ་འཛིན་པའི་འཇིགས་པ་ཡོད་པའི་ཆུ་ཀླུང་དེར་སྒྲེན་མོར་རྒལ་བར༌[^1204]མི་བྱའོ། །

[Block 1720]
དེར་ཤེས་བཞིན་དུ་གྲུ་རྒལ་བར༌[^1205]བྱའོ་ཞེས་བྱ་བ་ནི་བུད་མེད་ལ་རེག་པ་ཡོངས་སུ་སྤང་བའི་ཕྱིར་ཤེས་བཞིན་དུ་འགྲོ་བར༌[^1206]བྱ་བ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1721]
བ་གླང་གི་ནང་དུ་ཡང་ཤེས་བཞིན་དུ་འགྲོ་བར་བྱའོ། །

[Block 1722]
ཁྲོན་པ་ཡང་བརྟག་པར་བྱའོ། །

[Block 1723]
བསོད་སྙོམས་པ༌[^1207]ལ་ཡང་གྲོང་དུ་རྒྱུ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། གསུམ་པོ་དག་ལ་ཡང་ཞེས་བྱ་བའི་སྒྲ་སྨོས་པ་ནི་ཤེས་བཞིན་ཞེས་བྱ་བའི་རྗེས་སུ་འཇུག་པའི་དོན་དུའོ། །

[Block 1724]
ལེགས་པར་སོ་སོར་བརྟག་པར་བྱས་ནས་རབ་ཏུ་དབྱུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་བྱེ་བྲག་ཏུ་འབད་པར་བྱ་ཞེས་བྱ་བ་འདི་ལ་འདི་འགྲུབ་པ༌[^1208]ཡིན་ཏེ། [^1209]འགའ་ཞིག་ཏུ་ཡང་ལྷོད་པའི་སྦྱོར་བ་མི་བྱའོ། །

[Block 1725]
དེ་བས་ན་འདི་ནི་དཔེ་ཡིན་ཏེ། ཆོ་ག་འདི་ནི་བསླབ་པ་ཐམས་ཅད་ལ་སྦྱོར་བ་ལྷོད་ན་ཉེས་བྱས་ཡིན་ཏེ། དེའི་ཕྱིར་འདི་བསྟན་པའོ། །

[Block 1726]
གཅིག་པུ་བླ་གབ་མེད་པར་གློས་མི་དབབ་པོ་ཞེས་བྱ་བ་ནི་གཉིད་ཀྱིས་ལོག་པ་དེའི་ཤམ་ཐབས་བུད་པ་ན་བུད་མེད་ཀྱིས་བརྩལ་བས་འདི་གསུངས་པ་ཡིན་ནོ། །

[Block 1727]
རྩ་བའི་ལྟུང་བའི་རྒྱུར་འགྱུར་བ་ནི་སྐྱེ་བོ་མེད་པའི་ཕྱོགས་ལ་ཉིན་མོའམ་མཚན་མོ་གཉིད་མ་ལོག་པ་ན་ཡང་དེར་གློས་དབབ་པར་མི་བྱའོ། །

[Block 1728]
དེ་བས་ན་འདི་མི་བྱའོ་ཞེས་བྱ་བ་འདིར་བརྗོད་པ་ཡིན་ནོ། །

[Block 1729]
དགོན་པ་དང་བླ་གབ་མེད་པ་ལ་གཅིག་པུ་ཉིད་དུ་གྱུར་པ་ལ་ཉེས་པ་དང་ལྡན་པ་ཡང་ཡིན་ཏེ། དེ་བས་ན་འདི་རིག་པར་བྱའོ། །

[Block 1730]
དགེ་སློང་མས་གནས་ཁང་སྒོ་མ་བཅད་པར་སྙོམས་པར་འཇུག་པ་ཡང་མི་བྱའོ་ཞེས་བྱ་བ༌[^1210]ལ། ཡང་གི་སྒྲ་ནི་གློས༌[^1211]དབབ་པར་མི་བྱའོ་ཞེས་བྱ་བའི་རྗེས་སུ་དྲང་བའི་དོན་དུའོ། །

[Block 1731]
གཉིས་ཀ་ཡང་འདིར་དགེ་སློང་མས་གནས་ཁང་སྒོ་མ་བཅད་པར་མི་བྱའོ། །

[Block 1732]
གྲོགས་དང་བཅས་པས་ཀྱང་བྱ་བར་འགྱུར་གྱི། འདིར་གྲོགས་ཡོད་པ་ལ་ཡང་འདི་ཟིལ་གྱིས་མནན་ནས་སྩོལ་བའི༌[^1212]ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 1733]
མི་ཚངས་པར་སྤྱོད་པའི་ཕམ་པར་འགྱུར་བ་རྫོགས་སོ་ཞེས་བྱ་བ་དངོས་གཞི་དང་པོ་མི་ཚངས་པར་སྤྱོད་པའི་ཕམ་པར་འགྱུར་བ་རྫོགས་སོ།། །།

[Block 1734 [HEADING]]
## མ་བྱིན་པར་ལེན་པའི་ཕམ་པར་འགྱུར་བ། ^3-0

[Block 1735]
གང་བྱས་ན་མ་བྱིན་པར་ལེན་པའི༌[^1213]ཕམ་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རྐུ་བའམ་རྐུར་བཅུག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྐུ་བ་ནི་རང་གིས༌[^1214]བྱ་བའོ། །

[Block 1736]
རྐུར་བཅུག་པ་ནི་གཞན་ལ་བཅོལ་ནས་འཕྲོག་ཏུ་བཅུག་པའོ། །

[Block 1737]
རང་གི་ལུས་ངག་འབའ་ཞིག་ཏུ་ཡང་མ་ཟད་ཀྱི། མངགས་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕོ་ཉས་ཀྱང་བྱེད་པར་འགྱུར་བས་རྐུ་འམ་རྐུར་བཅུག་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1738]
རྐུ་བ་ནི་མངགས་པ་སྟེ་གང་དུ་མངགས་པ་རང་གི་ལུས་ཀྱིས་བྱེད་པའོ། །

[Block 1739]
རྐུར་བཅུག་པ་ནི་གང་ལ་མངགས་པས་བཅོལ་ནས་གཞན་ལ་འདི་སྐད་ཅེས་སོ། །

[Block 1740]
[^1215]རང་གིས་རྐུས་ཤིག །སོང་ལ་རྐུར་ཆུག་ཤིག༌[^1216]ཅེས་བྱེད་དུ་བཅུག་པའོ། །

[Block 1741]
བྱེ་བྲག་ཏུ་བཅོལ་བའི་དབང་གིས་དེ་ལྟར་རྣམ་པར་གཞག་སྟེ། མངགས་པའི་མངགས་པས་གཞན་གྱིས་རྐུར་བཅུག་པ་ཡིན་ཏེ། དེས་མངགས་པ་ལ་སོགས་པས་སམ། དེ་ལ་ཡང་རང་གིས་མངགས་པ་ཉིད་ཀྱིས་ཞེས་བྱ་བའི་ཁྱད་པར་ཡོངས་སུ་མ་བཟུང་བའི་ཕྱིར་འདིར་མངགས་པ་ཉིད་རིག་པར་བྱའོ། །གང་གི་ཞེ་ན། དེའི་ཕྱིར་མ་བྱིན་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱིན་པ་ལ་ཡང་རྐུ་སེམས་ཀྱིས་ལེན་པ་སྲིད་པས་དེའི་ཕྱིར་ཁྱད་པར་འདིའོ། །

[Block 1742]
འདིར་ལུང་ནི། དེ་ལ་བུད་མེད་དམ་སྐྱེས་པའམ་མ་ནིང་དག་གིས་ཀྱང་མ་བྱིན་པ་ཞེས་གསུངས་པ་དེ་ཡིན་ནོ། །

[Block 1743]
ཚད་ཇི་ཙམ་ཞེ་ན། དེའི་ཕྱིར་མ་ཤ་ཀ་ལྔ་ལ་སོགས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི། མ་ཤ་ཀ་ལྔའམ་མ་ཤ་ཀ་ལྔ་ལས་ལྷག་པས་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1744]
སེམས་ཇི་ལྟ་བུས་ཤེ་ན། དེའི་ཕྱིར། རྐུ་སེམས་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ལྟར་ཡིད་གཅུགས་པའི༌[^1217]སེམས་ལ་སོགས་པ་རྣམས་ཀྱིས་ནི་ལྟུང་བ་མེད་དོ་ཞེས་འོག་ནས་འབྱུང་ངོ་། །ཅི་མི་མ་ཡིན་པའི་རྒྱུད་ཀྱིས་ཡོངས་སུ་བཟུང་བའམ་ཞེ་ན། མ་ཡིན་ཏེ། །དེའི་ཕྱིར་མིའི་རྒྱུད་ཀྱིས་ཡོངས་སུ་བཟུང་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མིས་ཡོངས་སུ་བཟུང་བ་མ་ཡིན་པ་ལ་ན་སྨད་པ་ཉིད་དུ་གསུངས་པའི་ཕྱིར་འགྲོ་བ་གཞན་དང་འབྲེལ་པའི་འདུ་ཤེས་ཀྱིས་ཅི་ཞིག་དེ་ལྟ་ཉིད་དུ་འགྱུར་རམ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་ཕྱིར་དེར་འདུ་ཤེས་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མིའི་འགྲོ་བ་པས་ཡོངས་སུ་བཟུང་བ་ཡིན་པར་འདུ་ཤེས་པས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1745]
གལ་ཏེ་མིའི་བདག་གིས་རྐུའོ་སྙམ་དུ་འདུ་ཤེས་པར་གྱུར་ན་དེས་ཕམ་པ་ཡིན་ནོ། །

[Block 1746]
འདིར་གཞུང་ནི། འདི་ལྟ་སྟེ། དགེ་སློང་གིས་འདི་ལྟར་ཡོ་བྱད་ལྕི་བ་འདི་རྣམས་ནི་གཞན་སྐྱེས་པའམ་བུད་མེད་དམ་མ་ནིང་རྣམས་ཀྱིས་ཡོངས་སུ་བཟུང་བར་འདུ་ཤེས་པས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1747]
དེ་ལྟར་མ་བྱིན་པར་ལེན་པའི་ཕས་ཕམ་པ་བསྐྱེད་པ་ལ་ཡན་ལག་ལྔ་སྟེ། མ་བྱིན་པ་ཉིད་དང་། མ་ཤ་ཀ་ལྔ་ལ་སོགས་པ་ཉིད་དང་། རྐུ་སེམས་ཉིད་དང་། མིའི་རྒྱུད་ཀྱིས་ཡོངས་སུ་བཟུང་བ༌[^1218]ཉིད་དང་། དེར་འདུ་ཤེས་པ་ཉིད་དོ། །

[Block 1748]
ཡན་ལག་གང་ཡང་རུང་བ་མ་ཚང་བ་ལ་ནི་ཕམ་པར་འགྱུར་བ་མེད་དེ་ན་སྨད་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 1749]
མིའི་རྒྱུད་ཀྱིས་ཡོངས་སུ་བཟུང་བ་ཞེས་སྨོས་སོ། །

[Block 1750]
ཁྱེར་བ་ཉིད་ནི༌[^1219]བསམ་པས་མ་བཏང་བ་ནི་བདག་པོ་ཉིད་དང་མ་བྲལ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རླུང་དང་རྐུན་པོ་ལ་སོགས་པ་རྣམས་ཀྱིས་གོས་ལ་སོགས་པའི་རྫས་ཁྱེར་བ་ཉིད་ནི་གང་གིས་དེ་དང་འབྲེལ་པར་ཇི་སྲིད་བསམ་པ་དེ་དང་ལྡན་པས་མ་བཏང་བར་གྱུར་པ་ནི་ཡོངས་སུ་གཏོང་བར་མི་འགྱུར་བ་འདི་ལ་རེ་བ་མེད་པ་ཉིད་མ་སྐྱེས་པ་དེ་སྲིད་དུ་རྫས་ཀྱི་ཡུལ་དེ་ལ་གང་ཞིག་བདག་པོ་ཉིད་དང་མ་བྲལ་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1751]
འདིར་གཞུང་ནི། ཇི་ལྟར་ཡང་བཙོ་བླག་མཁན་གྱིས་གོས་རྣམས་བཏིང་བ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1752]
བདག་ཏུ་བྱས་པ་ཉིད་ལ་ཡང་གཞན་གྱིས་མ་བྲལ་བ་ཉིད་ཀྱི་བསམ་པར༌[^1220]བདག་པོ་ཉིད་དུ་མ་བཏང་བ་དག་ཏུ་བྱས་པ་རྗེས་སུ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 1753]
དེ་དང་མ་བྲལ་བ་ཉིད་དང༌[^1221]བདག་ལ༌[^1222]བྱས་པ་ལ་དེ་བསལ་བ་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 1754]
དེ་ལྟར་ན་རྒྱལ་པོའི་ཕོ་བྲང་དུ་རྐུན་པོ་རྣམས་གཏད་ཅིང་བཟློག་པ་ལ་རྐུ་བ་ཉིད་བསྐྱེད་པ་མི་སྲིད་པའོ། །

[Block 1755]
ཕྱེད༌[^1223]རིན་རྣམ་པར་སྦྱོར་བ༌[^1224]གང་ཞིག་དངོས་པོ་དེ་ལས་བདག་གིས༌[^1225]བྱེད་པ་སོ་སོར་མ་ལོག་པ་འདི་ནི་འདིར་བསམ་པས་མ་བཏང་བར་ཤེས་པར་བྱའོ། །
--- END BLOCKS ---
