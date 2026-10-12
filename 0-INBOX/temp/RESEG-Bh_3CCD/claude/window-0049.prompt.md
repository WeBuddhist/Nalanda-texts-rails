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
དེ་ནས་བཅོམ་ལྡན་འདས་ཡེ་ཤེས་སྒྲོན་མ་རྡོ་རྗེ་ཞེས་བྱ་བའི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་ཏེ་ཞེས་བྱ་བ་དེའི་བཤད་པ་རྣམ་པ་བཞིའི་རིགས་པས་བསྐྱེད་པའི་རིམ་པ་དང་། རྡོ་རྗེ་བཟླས་པ་དང་། སེམས་རྣམ་པར་དག་པ་དང་། བདག་ལ་བྱིན་གྱིས་བརླབ་པ་དང་། འོད་གསལ་བ་དང་། ཟུང་དུ་འཇུག་པའི་རིམ་པ་རྣམས་མཚོན་ཏོ། །

[Block 1717]
དེ་བཞིན་དུ།

[Block 1718 [VERSE]]
དངོས་པོ་ཐམས་ཅད་དང་བྲལ་བ། །
ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་དང་། །
གཟུང་དང་འཛིན་པ་རྣམ་སྤངས་པ། །
ཆོས་བདག་མེད་པ་མཉམ་ཉིད་པས། །

[Block 1719 [VERSE]]
རང་སེམས་གཟོད་ནས་མ་སྐྱེས་པ། །
སྟོང་པ་ཉིད་ཀྱི༌[^1230]རང་བཞིན་ནོ། །

[Block 1720]
ཞེས་བྱ་བས་རང་གི་སེམས་ལ་དམ་བཅའ་བ་དང་། གཏན་ཚིགས་དག་ཉིད་ཀྱིས་གསུངས་སོ། །

[Block 1721]
དེ་དག་གཟུང་བས་བསྒྲུབ་བྱ་བསྒྲུབ་པར་བྱ་བའི༌[^1231]ཕྱིར་རོ། །

[Block 1722]
དཔེ་མེད་པའི་སྒྲུབ་པར་བྱེད་པས་སྒྲུབ་མི་ནུས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནས།

[Block 1723 [VERSE]]
ཇི་ལྟར་སྒྱུ་མའི་རྨི་ལམ་བཞིན། །
ཇི་ལྟར་སྲིད་པ་བར་མ་དོ། །

[Block 1724]
ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱུད་གཞན་ནས་གསུངས་པའི་དཔེ་རྣམས་སྟོན་པས་ན་མདོར་ཤེས་པར་བྱའོ། །

[Block 1725]
ཡང་ན་གཡེང་བ་གཞན་ཉེ་བར་སྡུད་པའི་དགེ་སློང་རྩེ༌[^1232]གཅིག་པའི་བློ་ནི་ཚིག་དེ་དང་དེ་དག་ཏུ་སྤེལ་བར་བྱེད་པས་ན་མདོའོ། །

[Block 1726]
[^1233]འདི་ལྟ་སྟེ།

[Block 1727]
ཐུགས་ཀྱི་དཀྱིལ་འཁོར་གྱི་ལེའུ་བཞི་པ་ལས།

[Block 1728 [VERSE]]
དེ་ནས་ལས་ཀྱི་ཆོ་ག་ནི། །
མཐོང་བས་ཕྱག་རྒྱ་དགོད་པར་བྱ། །

[Block 1729]
ཞེས་སྨོས་པ་ལས་ལས་ཀྱི༌[^1234]ཆོ་ག་མཐོང་བའི་རྡོ་རྗེ་སློབ་དཔོན་གྱིས་ལྷ་དང་དཀྱིལ་འཁོར་དང་ཐིག་གདབ་པ་ལ་སོགས་པའི་རྣམ་པ་དཀྱིལ་འཁོར་གྱི་ཆོ་གའི་སྤྲོས་པ་གང་ཡིན་པ་དེ་དག་ཐམས་ཅད་རྒྱུད་གཞན་ལས་འདིར་མཚོན་པའོ། །

[Block 1730]
གཞན་ཡང་མདོའི་མཚན་ཉིད་དང་ལྡན་པས་ན་མདོ་སྡེ། མདོའི་མཚན་ཉིད་སློབ་དཔོན་རྣམས་ཀྱིས་ཉེ་བར་བསྟན་པ་གང་ཡིན་པ་དང་། དེ་དང་ལྡན་པས་ན་མདོ་ནི་འདི་ལྟ་སྟེ།

[Block 1731 [VERSE]]
ཚིག་ཉུང་ཐེ་ཚོམ་མེད་པ་དང་། །
སྣ་ཚོགས་སྒོ་དང༌[^1235]སྙིང་པོ་ཅན། །
ཟློས་མེད་ཁ་ན་མ་ཐོ་མེད། །
མདོ་ཤེས་པས་ནི་མདོ་སྡེར་བཤད། །

[Block 1732]
ཟློས་མེད་ཅེས་བྱ་བ་ནི་སྔ་ཕྱི་དག་ལ་ཁྱད་པར་ཡོད་པའོ། །

[Block 1733]
དེ་བཞིན་དུ་ཡང་།

[Block 1734 [VERSE]]
སྤང་བ༌[^1236]དེ་ནི་དོན་མཚོན་པ། །
ཡི་གེ་དང་ནི་ཚིག་ཉུང་བ། །
ཀུན་ཏུ་སྙིང་པོར་གྱུར་པ་སྟེ། །
བློ་དང་ལྡན་པས་མདོ་རུ་བཤད། །

[Block 1735]
དེ་ནས་མདོ་ཞེས་བྱ་བ་ཡན་ལག་དང་པོ་གཙོ་བོ་སྟེ། མདོ་གང༌[^1237]གི་མིང་གིས་རྒྱུད་ཡིན་ཡང་མདོ་སྡེ་ཞེས་བྱ་བར་བསྟན་ཏོ། །

[Block 1736 [HEADING]]
#### ཚད་མ། ^1-6-2-0

[Block 1737]
ཚད་མ་ནི་མངོན་སུམ་དང་རྗེས་སུ་དཔག་པ་གཉིས་ཏེ། དེ་དག་ཀྱང་འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 1738]
དེ་བཞིན་དུ་ཡང་ལེའུ་བཅུ་བདུན་པ་ལས།

[Block 1739]
དེ་ནས་དེ་བཞིན་གཤེགས་པ་ཕྱག་ན་རྡོ་རྗེས་དེ་བཞིན་གཤེགས་པ་དེ་དག་ཐམས་ཅད་ལ༌[^1238]འདི་སྐད་ཅེས་བཀའ་སྩལ་ཏོ། །

[Block 1740]
བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་སངས་རྒྱས་ཐམས་ཅད་ཀྱི༌[^1239]ཆོས་ཀྱི་མཉམ་པ་ཉིད་མཐོང་ངམ། དེ་ནས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་ཕྱག་ན་རྡོ་རྗེ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་བདག་པོ་ལ་འདི་སྐད་ཅེས་གསོལ་ཏོ། །

[Block 1741]
བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རྡོ་རྗེ་ཡེ་ཤེས་ཀྱི་སྤྱོད་པ་མཐོང་ལགས་སོ། །

[Block 1742]
བདེ་བར་གཤེགས་པ་མཐོང་ལགས་སོ་ཞེས་པ་དང་། ལེའུ་དང་པོའི་གླེང་བཞིའི༌[^1240]ཚིག་ལ་ནི་འདི་སྐད་བདག་གིས་ཐོས་པའི་དུས་གཅིག་ན། བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་དང་གསུང་དང་ཐུགས་ཀྱི་སྙིང་པོ་རྡོ་རྗེ་བཙུན་མོའི་བྷ་ག་ལ་བཞུགས་སོ་ཞེས་བྱ་བ་འདིར་མཐོང་བ་དང་ཐོས་པའི་སྒྲ་དག་གིས་མངོན་སུམ་གྱི་ཚད་མར༌[^1241]སོ་སོར་རྟོགས་སོ། །

[Block 1743]
དེ་བཞིན་དུ་ལེའུ་དགུ་པ་ལས་ཀྱང་། རིགས་ཀྱི་བུ་འདི་ལྟ་སྟེ༌[^1242]དཔེར་ན་གཙུབ་ཤིང་དང་གཙུབ་སྟན༌[^1243]དང་། མིའི་ལག་པ་བསྐྱོད་པའི་རྐྱེན་གྱིས་དུ་བ་རབ་ཏུ་འབྱུང་ཞིང་མེ་འབྱུང་བར་འགྱུར་མོད་ཀྱི་ཞེས་བྱ་བ༌[^1244]ཚོགས་པའི་རྒྱུ་ལ་བརྟེན༌[^1245]ནས། མེ་དང་དུ་བ་དག་གི་རྒྱུ་དང་འབྲས་བུའི་ངོ་བོའི་མཚན་ཉིད་ཅན་རྗེས་སུ་དཔག་པར་བསྟན་ཏོ། །

[Block 1744]
དེ་ལྟར་ཚད་མ་ཞེས་བྱ་བའི་ཡན་ལག་གཉིས་པའོ། །

[Block 1745 [HEADING]]
#### ཡན་ལག། ^1-6-3-0

[Block 1746]
ཡན་ལག་ནི་བཤད་པའི་རྒྱུད་དང་། ཡན་ལག་གི་རྒྱུད་རྣམས་ཏེ་ལྷ་མོ་བཞིས་ཡོངས་སུ་ཞུས་པ་དང་། དགོངས་པ་ལུང་བསྟན་པ་དང་། རྡོ་རྗེ་ཕྲེང་བ་དང་། ཡེ་ཤེས་རྡོ་རྗེ་ཀུན་ལས་བཏུས་པའི་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ལ་སོགས་པ་དེ་རྣམས་ཀྱིས་རྒྱུད་ཀྱི་དོན་ཡོངས་སུ་རྫོགས་པར་འགྱུར་ཏེ། ལག་པ་དང་རྐང་པ་ལ་སོགས་པས་ལུས་བཞིན་ནོ། །

[Block 1747]
དེ་ཡང་དེ་ནས་ལས་ཀྱི་ཆོ་ག་ནི་མཐོང་བས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་རྒྱུད་གཞན་ལས་མཐོང་བའི་ཡན་ལག་རྫོགས་པར༌[^1246]བསྟན་ཏོ། །

[Block 1748]
དེ་ལྟར་ན་ཡན་ལག་ཅེས་བྱ་བ་ཡན་ལག་གསུམ་པའོ། །

[Block 1749 [HEADING]]
#### མ་ཚང་བ་མེད་པ། ^1-6-4-0

[Block 1750]
མ་ཚང་བ་མེད་པ་ནི་ཚིག་གི་དོན་མ་ལུས་པར་གྲུབ་པའོ། །

[Block 1751]
དེ་ལ་ཚིག་གི་དོན་ནི་གཉིས་ཏེ། བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའོ། །

[Block 1752]
དེ་དག་གི༌[^1247]མ་ལུས་པ་དེ་ནི་དང་པོའི་དབྱེ་བ་གསུམ་དང་གཉིས་པའི༌[^1248]ལྔའོ། །

[Block 1753]
དེ་རྣམས་གྲུབ་པ་ནི་བཤད་པའི་རྒྱུད་ཀྱི༌[^1249]ཚིག་གིས་བསྟན་པའོ། །

[Block 1754]
དེ་བཞིན་དུ་ཡང་ལེའུ་བཅོ་བརྒྱད་པ་ལས།

[Block 1755 [VERSE]]
བསྐྱེད་པ་ཡི་ནི་རིམ་པ་དང་། །
རྫོགས་པ་ཡི་ནི་རིམ་པ་སྟེ། །
རིམ་པ་གཉིས་ལ་བརྟེན་ནས་ནི། །
རྡོ་རྗེ་ཅན་རྣམས་ཆོས་བསྟན་པའོ། །
--- END BLOCKS ---
