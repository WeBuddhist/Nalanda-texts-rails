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

[Block 1791]
དེ་སྤངས་ཀྱང་དེ་ལ་དམིགས་པ་ཀུན་དུ་འགྲོ་བ་ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་ཀྱིས་ལྡན་ནོ། །

[Block 1792]
བསྒོམ་པས་སྤང་བར་བྱ་བའི་རིས་ལ་ཡང་རྣམ་པ་དགུ་ལས་དང་པོའི་རྣམ་པ་སྤངས་ན་དེ་སྤངས་ཀྱང་དེ་ལ་དམིགས་པའི་ཉོན་མོངས་པ་ལྷག་མ་རྣམས་ཀྱིས་ལྷག་པར་རིག་པར་བྱའོ། །

[Block 1793 [HEADING]]
### དངོས་པོ་གང་ལ་ཕྲ་རྒྱས་དུ་ཞིག་རྒྱས་པར་འགྱུར་བ། ^2-24-0

[Block 1794]
དངོས་པོ་གང་ལ་ཕྲ་རྒྱས་དུ་ཞིག་རྒྱས་པར་འགྱུར་ཞེས་བྱ་བའི་ཚིག་འདི་རེ་རེ་ནས་བཤད་ན་ནི་བརྗོད་པར་བྱ་བ་མང་པོར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་ཅི་ནས་ཀྱང་འབད་པ་ཆུང་ངུ་ཆུང་ངུས་འདྲི་བའི༌[^1324]ཚོགས་མང་པོ་གོ་བར་འགྱུར་བར་བསྡུས་ཏེ་རྣམ་པར་འཆད་པར་བྱེད་དོ། །

[Block 1795 [HEADING]]
#### སེམས་བཅུ་དྲུག་གི་དམིགས་པ་ཆོས་བཅུ་དྲུག། ^2-24-1-0

[Block 1796]
མདོར་བསྡུ་ན་ཆོས་ནི་བཅུ་དྲུག་པོ་འདི་ལྟ་སྟེ། འདོད་པ་དང་། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམ་པ་ལྔ་ལྔ་དང་། ཟག་པ་མེད་པའོ། །

[Block 1797]
སེམས་ཀྱང་བཅུ་དྲུག་སྟེ། དེ་དག་ཉིད་དོ། །

[Block 1798]
དེ་ལ་ཆོས་གང་ཞིག་སེམས་གང་གི་དམིགས་པ་ཡིན་པ་ཤེས་པར་བྱས་ནས་འདི་ལ་ནི་ཕྲ་རྒྱས་འདི་དེ༌[^1325]སྙེད་ཅིག་རྒྱས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདི་ནི་རྟག༌[^1326]པར་བྱའོ། །

[Block 1799]
དེ་ལ་རེ་ཞིག །

[Block 1800 [VERSE]]
སྡུག་བསྔལ་རྒྱུ་མཐོང་གོམས་པ་ཡིས། །
སྤང་བྱ་འདོད་ཁམས་ལས་སྐྱེས་པ། །
རང་གི་གསུམ་དང་གཟུགས་གཏོགས་གཅིག །
དྲི་མེད་རྣམ་ཤེས་སྤྱོད་ཡུལ་ལོ། །

[Block 1801]
དེ་དག་ནི་རང་གི་ཡང་ཡིན་ལ་གསུམ་ཡང་ཡིན་པས་རང་གི་གསུམ་མོ། །

[Block 1802]
དེ་ནི་གཅིག་ཀྱང་ཡིན་ལ་གཟུགས་སུ་གཏོགས་པ་ཡང་ཡིན་པས་གཟུགས་གཏོགས་གཅིག་སྟེ། དེ་ནི་ཚིག་རྣམ་པར་སྦྱར་བའི་རྣམ་པ་ཡིན་ནོ། །

[Block 1803]
རེ་ཞིག་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ༌[^1327]མཐོང་བས་སྤང་བར་བྱ་བ་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཆོས་འདོད་པ་ན་སྤྱོད་པ་རྣམས་ནི་སེམས་ལྔའི་དམིགས་པ་ཡིན་ཏེ། རང་གི་ཁམས་པ༌[^1328]གསུམ་སྟེ། དེ་དག་ཉིད་དང་། གཟུགས་ན་སྤྱོད་པ་གཅིག་སྟེ། བསྒོམ་པས་སྤང་བར་བྱ་བ་ཁོ་ན་དང་།

[Block 1804 [VERSE]]
ཟག་པ་མེད་པའི་དམིགས་པ་ཡིན་ནོ། །
གཟུགས་ཁམས་ལས་སྐྱེས་རང་གི་དང་། །
འོག་གསུམ་གོང་གཅིག་དྲི་མེད་ཀྱི། །

[Block 1805]
ཆོས་རྣམ་པ་གསུམ་པོ་དེ་དག་ཉིད་གཟུགས་ན་སྤྱོད་པ་ནི་སེམས་བརྒྱད་ཀྱི་དམིགས་པ་ཡིན་ཏེ། རང་གི་ཁམས་པ་གསུམ་སྟེ། དེ་དག་ཉིད་དང་། ཁམས་འོག་མ་པ་གསུམ་སྟེ། དེ་དག་ཉིད་དང་། ཁམས་གོང་མ་པ་གཅིག་སྟེ། [^1329]བསྒོམ་པས་སྤང་བར་བྱ་བ་ཁོ་ན་དང་།

[Block 1806 [VERSE]]
ཟག་པ་མེད་པའི་དམིགས་པ་ཡིན་ནོ། །
གཟུགས་མེད་ལས་སྐྱེས་ཁམས་གསུམ་གཏོགས། །
གསུམ་དང་ཟག་མེད་སྤྱོད་ཡུལ་ལོ། །

[Block 1807]
ཆོས་རྣམ་པ་གསུམ་པོ་དེ་དག་ཉིད་གཟུགས་མེད་པ་ན་སྤྱོད་པའི༌[^1330]སེམས་བཅུའི་དམིགས་པ་ཡིན་ཏེ། ཁམས་གསུམ་པ་རྣམ་པ་གསུམ་གསུམ་སྟེ། དེ་དག་ཉིད་དང་། ཟག་པ་མེད་པའི་དམིགས་པ་ཡིན་ནོ། །

[Block 1808]
སྡུག་བསྔལ་དང་ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བ་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཆོས་ཁམས་གསུམ་པ་དག་བཤད་ཟིན་ཏོ། །

[Block 1809 [VERSE]]
འགོག་དང་ལམ་མཐོང་སྤང་བྱ་ཀུན། །
རང་གིས་གླགས་པའི་སྤྱོད་ཡུལ་ལོ། །

[Block 1810]
འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བའི་ཆོས་རྣམས་ཀྱི་རང་གི་སེམས་ནི་འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ཁོ་ན་ཡིན་ཏེ། ཆོས་དེ་དག་ནི་དེས་གླགས་པའི་སྤྱོད་ཡུལ་ཡིན་པར་ཤེས་པར་བྱ་སྟེ། ཇི་ལྟར་བྱས་པས་ཤེ་ན། འགོག་པ་མཐོང་བས་སྤང་བར་བྱ་བའི་ཆོས་འདོད་པ་ན་སྤྱོད་པ་རྣམས་ནི་རྣམ་པར་ཤེས་པ་དྲུག་གི་དམིགས་པ་ཡིན་ཏེ། སྔར་བཤད་པ་ལྔ་དང་། འགོག་པ་མཐོང་བས་སྤང་བར་བྱ་བ་གླགས་པ་དེ་ཉིད་ཀྱི་དམིགས་པ་ཡིན་ནོ། །

[Block 1811]
ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་ཀྱང་དེ་དང་འདྲ་སྟེ། སྔར་བཤད་པ་ལྔ་དང་། ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་གླགས་པ་དེ་ཉིད་ཀྱི་དམིགས་པ་ཡིན་ཏེ། དེ་བཞིན་དུ་འགོག་པ་དང་། ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམས་ཀྱང་འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བའི་སེམས་གླགས་པ་དེའི་དམིགས་པ་ཡིན་པས་སེམས་དགུ་དང་། བཅུ་གཅིག་གི་དམིགས་པ་ཡིན་ནོ། །

[Block 1812]
ཁམས་གསུམ་པའི་ཆོས་རྣམ་པ༌[^1331]ལྔ་བཤད་ཟིན་ཏོ། །

[Block 1813 [VERSE]]
ཟག་མེད་ཁམས་གསུམ་མཐའ་གསུམ་དང་། །
ཟག་པ་མེད་པའི་སྤྱོད་ཡུལ་ལོ། །

[Block 1814]
ཆོས་ཟག་པ་མེད་པ་རྣམས་ནི་སེམས་བཅུའི་དམིགས་པ་ཡིན་ཏེ། ཁམས་གསུམ་པའི་ཐ་མ་གསུམ་སྟེ། འགོག་པ་དང་ལམ་མཐོང་བས༌[^1332]སྤང་བར་བྱ་བ་དང་། ཟག་པ་མེད་པའི་དམིགས་པ་ཡིན་ནོ། །

[Block 1815]
ཡང་དོན་དེ་ཉིད་ཚིགས་སུ་བཅད་པ་ཕྱེད་པ༌[^1333]དང་གཉིས་ཀྱིས་བསྡུས་པ་ཡིན་ཏེ།

[Block 1816 [VERSE]]
ཁམས་གསུམ་སྡུག་བསྔལ་རྒྱུ་མཐོང་དང་། །
བསྒོམ་པས༌[^1334]སྤང་བྱ་ཟག་པ་མེད། །
རྣམ་ཤེས་ལྔ་བརྒྱད་བཅུ་དང་ནི། །
རྣམ་ཤེས་བཅུ་ཡི་སྤྱོད་ཡུལ་ཏེ། །

[Block 1817 [VERSE]]
འགོག་དང་ལམ་མཐོང་སྤང་བྱ་ཀུན། །
རང་གིས་གླགས་པའི༌[^1335]སྤྱོད་ཡུལ་ལོ། །

[Block 1818 [HEADING]]
#### ཕྲ་རྒྱས་རྒྱས་པར་འགྱུར་བ། ^2-24-2-0

[Block 1819]
དེ་ལྟར་སེམས་བཅུ་དྲུག་པོ་དེ་དག་གི་དམིགས་པར་ཆོས་བཅུ་དྲུག་པོ༌[^1336]རྣམ་པར་གཞག་པར་རིག་ནས། ཇི་ལྟར་ན་ཕྲ་རྒྱས་ཀྱི་དགོས་པ་ཡིན་པ་སྦྱར་བར་བྱ་སྟེ། ཕྱོགས་ཙམ་ཞིག་བསྟན་པར་བྱ་སྟེ། [^1337]བདེ་བའི་དབང་པོ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་ལ་ཕྲ་རྒྱས་དུ་ཞིག་རྒྱས་པར་འགྱུར་ཞེས་བྱ་བའི་དྲི་བ་འོངས་པ་ལ་དཔྱད་པར་བྱ་སྟེ། བདེ་བའི་དབང་པོ་ནི་རྣམ་པ་བདུན་ཏེ། འདོད་པ་ན་སྤྱོད་པ་བསྒོམ་པས་སྤང་བར་བྱ་བ་དང་། གཟུགས་ན་སྤྱོད་པ་རྣམ་པ་ལྔ་དང་། ཟག་པ་མེད་པའོ། །

[Block 1820]
དེ་དག་ཀྱང་མདོར་བསྡུ་ན་རྣམ་པར་ཤེས་པ་རྣམ་པ་བཅུ་གཉིས་ཀྱི་དམིགས་པ་ཡིན་ཏེ། འགོག་པ་མཐོང་བས་སྤང་བར་བྱ་བ་མ་གཏོགས་པ་འདོད་པ་ན་སྤྱོད་པ་རྣམ་པ་བཞི་དང་། གཟུགས་ན་སྤྱོད་པ་རྣམ་པ་ལྔ་དང་། [^1338]གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམ་པ་གཉིས་ཏེ། ལམ་མཐོང་བ་དང་བསྒོམ་པས་སྤང་བར་བྱ་བ་དང་། ཟག་པ་མེད་པའི་དམིགས་པ་ཡིན་ཏེ། རྣམ་པ་བཅུ་གཉིས་པོ་འདི་ནི་བདེ་བའི་དབང་པོ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ༌[^1339]ཡིན་ནོ། །

[Block 1821]
དེ་ལ་ཅི་རིགས་པར་ཕྲ་རྒྱས་འདོད་པ་ན་སྤྱོད་པ་རིས་བཞི་དང་། གཟུགས་ན་སྤྱོད་པ་འདུས་བྱས་ལ་དམིགས་པ་རྣམས་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ་རིས་གཉིས་དང་། ཀུན་དུ་འགྲོ་བ་རྣམས་རྒྱས་པར་འགྱུར་བར་ཤེས་པར་བྱའོ། །

[Block 1822]
བདེ་བའི༌[^1340]དབང་པོ་ལ་དམིགས་པའི༌[^1341]རྣམ་པར་ཤེས་པ་ལ་ཕྲ་རྒྱས་དུ་ཞིག་རྒྱས་པར་འགྱུར་ཞེ་ན། བདེ་བའི་དབང་པོ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་རྣམ་པ་བཅུ་གཉིས་པོ་དེ་ནི༌[^1342]རྣམ་པར་ཤེས་པ་གང་གི་དམིགས་པ་ཡིན་ཞེ་ན། རྣམ་པ་བཅུ་གཉིས་པོ་དེ་ཉིད་དང་། ཡང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམ་པ་གཉིས་ཏེ། སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ༌[^1343]མཐོང་བས་སྤང་བར་བྱ་བའི་དམིགས་པ་ཡིན་ཏེ། རྣམ་པ་བཅུ་བཞི་པོ་འདི་ནི་བདེ་བའི་དབང་པོ་ལ་དམིགས་པ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 1823]
དེ་ལ་གཟུགས་མེད་པ་ན་སྤྱོད་པ་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བ་དག་བསྐྱེད༌[^1344]ནས་འདོད་པ་ན༌[^1345]སྤྱོད་པ་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་རིས་བཞི་བཞི་དང་། གཟུགས་ན་སྤྱོད་པ་འདུས་བྱས་ལ་དམིགས་པ་རྣམས་རྒྱས་པར་འགྱུར་རོ་ཞེས་བྱ་བར་ཤེས་པར་བྱ་སྟེ། ལམ་འདིས་གཞན་ཡང་ཁོང་དུ་ཆུད་པར་བྱ་སྟེ།[^1346] ཕྲ་རྒྱས་གང་དག་གི༌[^1347]སེམས་ཕྲ་རྒྱས་དང་བཅས་པའི་ཕྲ་རྒྱས་དེ་དག་སེམས་དེ་ལ་རྒྱས་པར་འགྱུར་རམ་ཞེ་ན། རྒྱས་པར་འགྱུར་བ་དག་ཀྱང་ཡོད་དེ། སེམས་དེ་དང་མཚུངས་པར་ལྡན་པ་ཡང་མ་སྤངས་ལ་དེ༌[^1348]ལ་དམིགས་པ་ཡང་མ་སྤངས་པའི་ཕྲ་རྒྱས་གང་དག་ཡིན་པའོ། །

[Block 1824]
རྒྱས་པར་མི་འགྱུར་བ་དག་ཀྱང་ཡོད་དེ། སེམས་དེ་དང་མཚུངས་པར་ལྡན་པ་སྤངས་པའི་ཕྲ་རྒྱས་གང་དག་ཡིན་པའོ། །

[Block 1825 [HEADING]]
#### སེམས་ཕྲ་རྒྱས་དང་བཅས་པ། ^2-24-3-0
--- END BLOCKS ---
