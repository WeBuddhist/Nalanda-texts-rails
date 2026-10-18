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
[Block 1751]
འོན་ཏེ་མེད་དོ་ཞེ་ན་ནི། མེད་པ་ཡང་དམིགས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པ་ཡིན་ནོ། །

[Block 1752]
གལ་ཏེ་མེད་པ་ཡང་དམིགས་པ་ཡིན་ན་སྐྱེ་མཆེད་བཅུ་གསུམ་པ་ཡང་དམིགས་པ་ཡིན་པར་འགྱུར་རོ། །

[Block 1753]
འོ་ན་སྐྱེ་མཆེད་བཅུ་གསུམ་པ་མེད་དོ་སྙམ་པའི་རྣམ་པར་ཤེས་པ་འདིའི་དམིགས་པ་ཅི་ཞིག་ཡིན། མིང་དེ་ཉིད་དམིགས་པ་ཡིན་ནོ། །

[Block 1754]
དེ་ལྟ༌[^1297]ནི་འོ་ན་མིང་དེ༌[^1298]ཉིད་མེད་དོ་ཞེས་བྱ་བར་རྟོགས་པར་འགྱུར་རོ། །

[Block 1755]
གང་ཞིག་སྒྲའི་སྔ་ན་མེད་པ་ལ་དམིགས་པ་དེའི་དམིགས་པ་ཡང་ཅི་ཞིག་ཡིན། སྒྲ་ཁོ་ན་ཡིན་ནོ། །

[Block 1756]
དེ་ལྟ་ན་ནི་འོ་ན་གང་ཞིག་སྒྲ་མེད་པ་དོན་དུ་གཉེར་བ་དེ་ལ་སྒྲ་དབྱུང་དགོས་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 1757]
གལ་ཏེ་མ་འོངས་པའི་གནས་སྐབས་ཡིན་ནོ་ཞེ་ན་ནི་ཡོད་ན་ཇི་ལྟར་ན་མེད་པའི་བློར་འགྱུར། གལ་ཏེ་ད་ལྟར་མེད་པ་ཡིན་ནོ་ཞེ་ན་ནི་མ་ཡིན་ཏེ། གཅིག་པའི་ཕྱིར་རོ། །

[Block 1758]
ཡང་ན་དེའི་བྱེ་བྲག་གང་ཡིན་པ་དེ་མ་བྱུང་བ་ལས་འབྱུང་བར་འགྲུབ་སྟེ། དེ་ལྟ་བས་ན་རྣམ་པར་ཤེས་པའི་དམིགས་པ་ནི་ཡོད་པ་དང་མེད་པ་དེ༌[^1299]གཉི་ག་ཡིན་ནོ། །

[Block 1759]
འོ་ན་བྱང་ཆུབ་སེམས་དཔའ༌[^1300]འཇིག་རྟེན་ན་མེད་པ་གང་ཡིན་པ་དེ་དག༌[^1301]གིས་ཤེས་པའམ་མཐོང་བ་འདི་ནི་གནས་མེད་དོ་ཞེས་གང་སྨྲས་པ་དེ༌[^1302]ཇི་ལྟ་བུ། འདིར་བསམ་པ་ནི་མངོན་པའི་ང་རྒྱལ་ཅན་གཞན་དག་སྣང་བ་མེད་བཞིན་དུ་ཡོད་པར་ལྟའི་བདག་ནི་ཡོད་པ་ཁོ་ན་ལ་ཡོད་དོ་ཞེས་བྱ་བར་ལྟའོ་ཞེས་བྱ་བ་འདི་ཡིན་ནོ། །

[Block 1760]
དེ་ལྟ་མ་ཡིན་ཏེ། བློ་ཐམས་ཅད་ཀྱི་དམིགས་པ་ཡོད་པ་ཉིད་ཡིན་ན་འདི་རྟོག་པར་ཡང༌[^1303]ག་ལ་འགྱུར། ཡང་ན་ཁྱད་པར་ཡང༌[^1304]ཅི་ཞིག་ཡོད། དེ་ནི་གདོན་མི་ཟ་བར་དེ་ལྟ་བུ་ཡིན་པར་ཤེས་པར་བྱ་སྟེ། འདི་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་གཞན་དུ་ངའི་ཉན་ཐོས་ཀྱི་དགེ་སློང་ཚུར་ཤོག་ཅེས་བྱ་བ་ནས་དེ་ངས་ནང་གཏམས་ན་ནུབ་ཁྱད་པར་དུ་འགྲོ། ནུབ་གཏམས་ན་ནང་ཁྱད་པར་དུ་འགྲོ་སྟེ། ཡོད་པ་ལ༌[^1305]ཡོད་པར་ཤེས་ལ། མེད་པ་ལ་ཡང་མེད་པར་ཤེས་སོ། །

[Block 1761]
བླ་ན་ཡོད་པ་ལ་ཡང་བླ་ན་ཡོད་པར་ཤེས་ལ། བླ་ན་མེད་པ་ལ་ཡང་བླ་ན་མེད་པར་ཤེས་སོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་ཏེ། དེ་ལྟ་བས་ན་རྣམ་པར་ཤེས་པ་ནི་ཡོད་པ་ལ་དམིགས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་དེ་ཡང་གཏན་ཚིགས་སུ་མི་རུང་ངོ་། །གང་ཡང་འབྲས་ཕྱིར་ཞེས་སྨྲས་པ། མདོ་སྡེ་པ་རྣམས་ནི་ལས་དང༌[^1306]འདས་པ་ལས་འབྲས་བུ་འབྱུང་བར་མི་བརྗོད་པ་ཁོ་ནའོ། །

[Block 1762]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། དེ་སྔོན་དུ་འགྲོ་བའི་རྒྱུད་ཀྱི་ཁྱད་པར་ལས་ཏེ། བདག་ཏུ་སྨྲ་བ་དགག་པ༌[^1307]ནས་བཤད་པར་བྱའོ། །

[Block 1763 [HEADING]]
#### ལས་ཀྱི་ནུས་པ། ^2-22-8-0

[Block 1764]
གང་གི་འདས་པ་དང་མ་འོངས་པ་རྫས་སུ་ཡོད་པ་དེའི་འབྲས་བུ་རྟག་ཏུ་ཡོད་པ་ཁོ་ན་བས་དེ་ལ་ལས་ཀྱི་ནུས་པ་ཅི་ཞིག་ཡོད། བསྐྱེད་པར་ནུས་སོ། །

[Block 1765]
འོ་ན་ནི་སྐྱེ་བ་མ་བྱུང་བ་ལས་དང༌[^1308]འབྱུང་བ་ཞེས་བྱ་བར་གྲུབ་པ་ཡིན་ནོ། །

[Block 1766]
ཡང་ཐམས་ཅད་ཡོད་པ་ཁོ་ན་ཡིན་ན་ད་ནི་གང་ལ་གང་ཞིག་འདུས༌[^1309]ཏེ། དེ་ལྟ་ན་ལོ་རྩིས་པ༌[^1310]རྣམས་ཀྱི་རྩོད་པ་སྐད་དུ་གང་ཡོད་པ་དེ༌[^1311]ནི་ཡོད་པ་ཁོ་ནའོ། །

[Block 1767]
གང་མེད་པ་དེ་ནི་མེད་པ་ཁོ་ནའོ། །

[Block 1768]
མེད་པ་ལ་ནི་སྐྱེ་བ་ཡང་མེད་དོ། །

[Block 1769]
ཡོད་པ་ལ་ནི་འཇིག་པ་ཡང་མེད་དོ་ཞེས་བརྗོད་པ་ཡིན་ནོ། །

[Block 1770]
འོ་ན་ད་ལྟར་དུ་བྱེད་པ༌[^1312]ནུས་པ་ཡིན་ནོ། །

[Block 1771]
ད་ལྟར་དུ་བྱེད་པ་ཞེས་བྱ་བ་འདི་ཅི་ཡིན། གལ་ཏེ་ཡུལ་གཞན་དུ་འདྲེན་པ་ཡིན་ནོ་ཞེ་ན་ནི་རྟག་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1772]
གཟུགས་ཅན་མ་ཡིན་པ་རྣམས་ལ་ཡང༌[^1313]དེ་ཇི་ལྟ་བུ། དེ་འདྲེན་པ་གང་ཡིན་པ་དེ་ཡང་མ་བྱུང་བ་ལས་བྱུང་བ་ཡིན་ནོ། །

[Block 1773]
གལ་ཏེ་རང་གི་ངོ་བོའི་ཁྱད་པར་ཞིག་ཡིན་ནོ་ཞེ་ན་ནི་མ་བྱུང་བ་ལས་འབྱུང་བ་གྲུབ་པ་ཡིན་ནོ། །

[Block 1774]
དེ་ལྟ་བས་ན་འདི་སྐད་དུ། གང་འདས་པ་དང་མ་འོངས་པའི༌[^1314]རྫས་སུ་ཡོད་པར་སྨྲ་བའི་ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་ནི༌[^1315]བསྟན་པ་ལ་ལེགས་པ་མ་ཡིན་གྱི། ཇི་སྐད་དུ་མདོ་ལས་ཐམས་ཅད་ཡོད་དོ་ཞེས་གསུངས་པ་དེ་བཞིན་དུ་སྨྲ་བ་དེ་དག༌[^1316]ནི་ལེགས་པ་ཡིན་ནོ། །

[Block 1775 [HEADING]]
#### ཐམས་ཅད་ཡོད་ཅེས་གསུངས་པ། ^2-22-9-0

[Block 1776]
མདོ་ལས་ཇི་ལྟ་བུ༌[^1317]ཐམས་ཅད་ཡོད་ཅེས་གསུངས་ཤེ་ན། ཐམས་ཅད་ཡོད་ཅེས་བྱ་བ་ནི་བྲམ་ཟེ་སྐྱེ་མཆེད་བཅུ་གཉིས་ཁོ་ནའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ་ཞེས་གསུངས་སོ། །

[Block 1777]
ཡང་ན་དུས་གསུམ་སྟེ། དེ་ཇི་ལྟར་ཡོད་པ་དེ་བཞིན་དུ་ནི་བཤད་ཟིན་ཏོ། །

[Block 1778]
ཡང་འདས་པ་དང་མ་འོངས་པ་དག་མེད་ན་ཇི་ལྟར་ན༌[^1318]དེས་སམ། དེར་ལྡན་པ་ཡིན་ཞེ་ན། དེ་ལས་སྐྱེས་པ། དེའི་རྒྱུའི་ཕྲ་རྒྱས་ཡོད་པའི་ཕྱིར་ཉོན་མོངས་པ་དེས་ལྡན་ལ། དེ་ལ་དམིགས་པའི་ཉོན་མོངས་པའི་ཕྲ་རྒྱས་ཡོད་པས་དངོས་པོ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 1779]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་འདས་པ་དང་མ་འོངས་པ་ནི་ཡོད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1780]
གང་ཞིག་དྲང་བར་མི་ནུས་པ་དེ་ལ་ནི་འདི་ལྟར། ཆོས་ཉིད་དག་ནི་ཟབ་པ་ཡིན། །དེ་གདོན་མི་ཟ་བར་རྟོགས་པས༌[^1319]སྒྲུབ་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 1781]
གང་སྐྱེས་པ་དེ༌[^1320]འགག་པའི་རྣམ་གྲངས་ཀྱང་ཡོད་དེ། གཟུགས་སྐྱེ་ལ་གཟུགས་འགག་གོ། །

[Block 1782]
གཞན་སྐྱེ་ལ་གཞན་འགག་པའི་རྣམ་གྲངས་ཀྱང་ཡོད་དེ། མ་འོངས་པ་སྐྱེ་ལ་ད་ལྟར་འགག་གོ། །

[Block 1783]
དུས་ཀྱང་སྐྱེ་སྟེ། སྐྱེ་བ་དུས་ཀྱིས་བསྡུས་པའི་ཕྱིར་རོ། །

[Block 1784]
དུས་ལས་ཀྱང་སྐྱེ་སྟེ། མ་འོངས་པའི་དུས་སྐད་ཅིག་མ་དུ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1785]
ཞར་ལ་འོངས་པ་འདི་རྫོགས་སོ།། །།

[Block 1786 [HEADING]]
### སྤངས་པ་དང་བྲལ་བ། ^2-23-0

[Block 1787]
ད་ནི་དངོས་པོ་གང་ཞིག་སྤངས་ན་དེ་དངོས་པོ་དེ་དང་བྲལ་བ་ཡིན་ནམ། གང་དང་བྲལ་ན་དེས༌[^1321]དངོས་པོ་དེ་སྤངས་པ་ཡིན་ཞེས་བྱ་བ་འདི་དཔྱད་པར་བྱ་སྟེ། རེ་ཞིག་གང་དང་བྲལ་ན་དེས་དངོས་པོ་དེ་སྤངས་པ༌[^1322]ཡིན་ནོ། །

[Block 1788]
སྤངས་ལ༌[^1323]དེ་དང་མ་བྲལ་བ་ཡང་ཡོད་དེ། འདི་ལྟ་སྟེ།

[Block 1789 [VERSE]]
སྡུག་བསྔལ་མཐོང་སྤང་བྱ་སྤངས་ཀྱང་། །
ཀུན་འགྲོ་ལྷག་མ་རྣམས་ཀྱིས་ལྡན། །
དང་པོའི་རྣམ་པ་སྤངས་ཀྱང་དེའི། །
ཡུལ་ཅན་དྲི་མ་ལྷག་རྣམས་ཀྱིས། །

[Block 1790]
སྡུག་བསྔལ་ཤེས་པ་ནི་སྐྱེས་ལ། །ཀུན་འབྱུང་ཤེས་པ་ནི་མ་སྐྱེས་པའི་ཚེ་སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བའི་རིས་སྤངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
