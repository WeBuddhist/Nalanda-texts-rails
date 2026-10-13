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
[Block 1821 [HEADING]]
### འདོད་རྒྱལ་བ་ལ་དོན་དབྱེ་བ། ^5-18-0

[Block 1822]
གལ་ཏེ་རེ་ཞིག་རྒྱུ་མཚན་ཅན་གྱི་སྒྲ་རྣམས་ལ་ལྟ་དོན་གང་དག་བསལ་བའི༌[^1449]སྒོ་ནས་དོན་མངོན་པར་བརྗོད་པ་རིགས་གྲངས་ན་འདོད་རྒྱལ་བ་རྣམས་ལ་ཇི་ལྟར་ཞེ་ན། འདོད་རྒྱལ་བ་ལ་དོན༌[^1450]དབྱེ་བས། །འདོད་རྒྱལ་བ་ལ་ཤིང་ཏོག་དིད་ཐཱ་ལ་སོགས་པའི་སྒྲ་སྤྱི་བརྗོད་པ་ཡིན་ཞིང་སྤྱི་དེའི་དབྱེ་བས་རྗོད་པར་བྱེད་དོ། །

[Block 1823 [HEADING]]
### རིགས་དང་མཐུན་པའི་འདུས་པ་སྒྲ། ^5-19-0

[Block 1824]
གལ་ཏེ་རིགས་དང་མཐུན་པའི་འདུས་པ་སྒྲ་དག་ལ་བྱེ་བྲག་ཅི་ཡོད་ཅེ་ན། ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 1825]
རིགས་ཀྱི་སྒྲ་ཡང་གྲགས་པའི་དབང་གིས། ཁ་ཅིག་ཏུ་ཡན་ལག་སོ་སོ་ལ་འདོགས་པར་འདོད་དེ། དཔེར་ན་གྲོང་གི་ཕག་པ་བཟའ་བྱ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1826]
ལ་ལར་དངོས་སུ་རྗོད་པར་བྱེད་དེ་དཔེར་ན།

[Block 1827 [VERSE]]
གྲངས་དང་མཚན༌[^1451]ཉིད་དང་ནི་དབྱིབས། །
ལྟོས་པ་མེད་པར་རབ་ཏུ་འཇུག །
ཆུ་ལ་སོགས་པའི་ཐིགས་པ་དང་། །
འདུས་པ་ལ་ཡང་རྗོད་པར་བྱེད། །

[Block 1828]
ལ་ལར་ཡན་ལག་འབའ་ཞིག་ལ་འཇུག་པ་མ་ཡིན་ཏེ། དཔེར་ན།

[Block 1829 [VERSE]]
དབྱིབས་དང་ཁ་དོག་ཆ་ཤས་ཀྱིས། །
ཁྱད་པར༌[^1452]བྱས་ནས་འཇུག་པ་ཡིན།[^1453] །
སྒྲ་ཡིས་དེ་ཡི་ཆ་ཤས་ལ། །
རབ་ཏུ་འཇུག་པ་དམིགས་མ་ཡིན། །

[Block 1830]
དབྱིབས་ཀྱི་ཁྱད་པར་ལ་འཁོར་ལོ་དང་། ཟླུམ་པོ་དང་། རིང་པོ་དང་། གྲུ་བཞི་པ་ཞེས་བྱ་བ་ལྟ་བུ་ཡན་ལག་ཙམ་གྱིས་བརྗོད་པ༌[^1454]མ་ཡིན་ནོ། །

[Block 1831]
དེ་བཞིན་དུ་ཁུ་ཚུར་དང་། མདུད་པ་དང་། ཕྲེང་བ་དང་། རྣ་རྒྱན་ལ་སོགས་པ་རྣམས་ལ་ཡང་ངོ་། །ཁ་དོག་གི་ཁྱད་པར་ལ་ཁྲ་བོ་དང་། ཁྲེ་རྩེ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 1832]
ཡན་ལག་ཅན་གྱི་ཁྱད་པར་ལ་བརྒྱ་དང་། སྟོང་བྲེ་དང་ཁལ་དང་། ཟླ་བ་དང་། ལོ་དང་། སྲང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུ་ཡན་ལག་རྣམས་ལ་འཇུག་པ་མ་ཡིན་ནོ། །

[Block 1833]
འདུས་པའི་སྒྲ་ཡང་ཁ༌[^1455]ཅིག་སོ་སོ་བ་ལ་རྫོགས་པར་འཇུག་སྟེ། དཔེར་ན་གྲོང་འོངས་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1834]
ཁ་ཅིག་ནི་བརྟགས༌[^1456]ནས་ཏེ། དཔེར་ན་ལུས་ཀྱི་ལས༌[^1457]ཀྱིས་བདག་གི་ལས་ཆད་པར་བྱེད་པ་ལྟ་བུའོ། །

[Block 1835]
ཁ་ཅིག་ནི་འཇུག་པར་མི་བྱེད་དེ། དཔེར་ན་ཆུ༌[^1458]ཞེས་བྱ་བ་དང་། ནགས་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1836 [HEADING]]
### འབྲེལ་པས་མ་བྱས་པ་སྒྲའི་དོན་སྟོན་པ། ^5-20-0

[Block 1837]
གལ་ཏེ་འདི་ལྟར་འབྲེལ་པས་མ་བྱས་པ་སྒྲའི་དོན་སྟོན་པར་བྱེད་པ་སྟེ། དཔེར་ན༌[^1459]ཤིང་ཏོག་པ་ན་སའོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 1838]
[^1460]དེ་ལ་ཇི་ལྟར་རྗེས་སུ་དཔག་པར་བྱ་ཞེ་ན། དེར་ཤིང་ཏོག་པ་ན་སའི་སྒྲའི་དོན་གྱིས་རྟོགས་པ་བསྐྱེད་པ་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། རྟོགས་པའི་དོན་ནི་བསྟན་ཕྱིར་རོ། །

[Block 1839]
འདི༌[^1461]ཞེས་པའི་སྒྲ་དང་ལག་པའི་བརྡའམ། གྲགས་པ་རྙིང་པ་དང་འབྲེལ་པས་རབ་ཏུ་རྟོགས་པ་ཡིན་གྱི། ཤིང་ཏོག་པ་ན་སའི་སྒྲ་དོན་རྟོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1840]
འདི་ལྟར་བརྡ༌[^1462]གསལ་བར་བྱེད་པའི་འབྲེལ་པ་བསྟན་པའི་དོན་དེར་བརྡའི་དོན་དང་འདི་ཞེས་པའི་སྒྲ་གཞི༌[^1463]མཐུན་པ་ཡིན་ནོ། །

[Block 1841]
གཉིས་ཀ་བརྗོད་པར་བྱ་བ་ཡིན་ནོ་ཞེས་བྱས་ནས་དེའི་དོན་དུ་བརྡའི་དོན་བྱས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1842]
ཤིང་ཏོག་པ་ན་སའི་སྒྲ་དེ་ཉིད་དང་འབྲེལ་པ་ལྟར་སྒྲའི་གཞལ་བར་བྱ་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1843]
འབྲེལ་པ་མ་ཡིན་བརྟག་པའི༌[^1464]ཕྱིར། །འབྲེལ་པ་ནི་ཤིང་ཏོག་པ་ན་སའི་དོན་དང་སྒྲ་དག་ཚད་མ་གཞན་གྱིས་དམིགས་ནས་འདི་འདིའི་ཡིན་ནོ་ཞེས་ཤིང་ཏོག་པ་ན་ས་དང་འབྲེལ་པར་རྟོགས་པ་ཡིན་ལ། གཞལ་བར་བྱ་བ་དང་འབྲེལ་པའི་ཕྱིར་རྗེས་སུ་དཔག་པ་ཡིན་ནོ། །

[Block 1844]
དེའི་ཕྱིར་སྒྲ་ལས་བྱུང་བའི་ཚད་མ་གཞན་མ་ཡིན་ནོ། །

[Block 1845 [HEADING]]
### ཉེ་བར་གཞལ་བ་ལ་སོགས་པ་ལྷག་མ་རྣམས། ^5-21-0

[Block 1846]
ཅི་སྟེ་ཉེ་བར་གཞལ་བ༌[^1465]ལ་སོགས་པ་ལྷག་མ་རྣམས་ཇི་ལྟར༌[^1466]གཞན་མ་ཡིན་ཞེ་ན། ཕྱོགས་འདིས་ལྷག་མ་རྣམས་ལའང་བརྗོད། །རེ་ཞིག་ཉེ་བར་གཞལ་བ་ནི་བ་ལང་དང་བ་མེན་ལ་སོགས་པ་དེ་དང་འདྲ་བར་རྟོགས་པར་བྱ་བའི་དོན་དུ་དེར་གཞན་ལས་ཐོས་པ་དང་། རྟོགས་པ་དག་གིས༌[^1467]སྒྲའི་རང་གི་དོན་གཉིས་ཚད་མ་གཞན་གྱི༌[^1468]ཁོངས་སུ་ཆུད་པ་དེ་དང་འདྲ་བར་རྟོགས་པ་སྟེ་དེ་ནི་ཚད་མ་གཞན་མ་ཡིན་ནོ། །

[Block 1847]
དེ་བཞིན་དུ་སྙམ་དུ་སེམས་པ་ཡང་དེ་དང་འདྲ་བར་འཇལ་བར་བྱེད་པ་ཡིན་པས་ཚད་མ་གཞན་མ་ཡིན༌[^1469]པར་ཁོང་དུ་ཆུད་པར་བྱ་སྟེ། རྗེས་སུ་དཔག་པའི་རྣམ་པར་རྟོག་པ་ལས་ཕྱི་རོལ་དུ་གྱུར་པ་ཡིན་པའི་གསལ་བར༌[^1470]བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 1848]
ཚད་མ་ཀུན་ལས་བཏུས་པ་ལས་གཞན་སེལ་བ་བརྟག་པའི་ལེའུ་སྟེ་ལྔ་པའོ།། །།

[Block 1849 [HEADING]]
## ལྟག་གཅོད་བརྟག་པའི་ལེའུ། ^6-0

[Block 1850]
ཚད་མ་ནི་གཉིས་སུ་གནས་ན་ཅི་སྟེ་ཚད་མ་བརྗོད་པར་བྱ་བ་ལ་ཅིའི་དོན་དུ་དེ་ལྟར་སྣང་བ་མ་ཚང་བ་ལ་སོགས་པ་རྣམས་ཀྱང་རྗོད་པར་བྱེད་ཅེ་ན།

[Block 1851 [VERSE]]
ཚད་སྣང་བརྗོད་པར་འདོད་རྣམས་ལ། །
རིག་པའི་ཆ་ཤས་སྨྲ་པོ་བཞིན། །
ཕྱོགས་གྲུབ༌[^1471]མཚུངས་པ་མ་ཡིན་ཞེས། །
བསྟན་ཕྱིར་མ་ཚང་ལ་སོགས་བརྗོད། །

[Block 1852]
ཁ་ཅིག་ངག་ཙམ་ལ་མཁས་པར་འཛིན་པ་ནི་ཡོད་པ་ཉིད་དེ། ཇི་སྐད་དུ་ཕྱོགས་གྲུབ་པའི་སྒྲུབ་བྱེད་ཡིན་བཞིན་དུ་ཡང་གྲུབ་པ་ལྟར་སྣང་བར་འདོད་ཅེས་བརྗོད་པ་དེ་དག་གི་སྒྲུབ་བྱེད་མ་ཡིན་པ་གཞན་ཉིད་དོ་ཞེས༌[^1472]ཕྱོགས་གྲུབ་པ་དགག་པའི་ཕྱིར་མ་ཚང་བ་ཉིད་ལ་སོགས་པ་གྲུབ་པའི་སྐྱོན་བརྗོད་དོ། །

[Block 1853 [VERSE]]
དེ་ཉིད་རབ་ཏུ་བསྟན་ཕྱིར་དང་། །
དེ་ལྟར་སྣང་བ་བརྗོད་པའི་ཕྱིར། །
ལན་འདི་བརྗོད་པར་རིགས་པ་ཡིན། །
ལྟག་སྤྱོད༌[^1473]ལ་ནི་རྗེས་མཐུན་ལན། །

[Block 1854]
གང་གི་ཕྱིར་འདིས་ཕྱོགས་སྔ་མ་གྲུབ་པོ་ཞེས་བརྗོད་པ་འདི་ལ་ལན་དུ༌[^1474]ཚང་བ་ལ་སོགས་པ་བརྗོད་པར་རིགས་སོ། །

[Block 1855]
མ་ཚང་བ་ལ་སོགས་པ་བསྟན་པར་བྱ་བའི་ཕྱིར་ཡང་བརྗོད་པར་རིགས་སོ། །

[Block 1856]
ལྟག་སྤྱོད་རྣམས་ལ་ནི༌[^1475]སྐྱོན་ལན་དུའོ། །

[Block 1857]
འདིས་ཕྱོགས་སྔ་མ་དག་སྒྲུབ་བྱེད་མ་ཡིན་པ་ཉིད་དུ་ཤེས་པར་མི་ནུས་སོ། །

[Block 1858]
དེ་ལ།

[Block 1859 [HEADING]]
### ཕྲད་པ་དང་མ་ཕྲད་པར་མཚུངས་པ། ^6-1-0

[Block 1860 [VERSE]]
ཕྲད་དང་མ་ཕྲད་དག་དང་དུས། །
གསུམ་ལ་རྟགས་སུ་བརྗོད་འདོད་མིན། །
ཕྲད་དང་མ་ཕྲད་རྟགས་བརྗོད་དེས།[^1476] །
མ་ཚང་གཏན་ཚིགས་རྗེས་མཐུན་ཡིན། །
--- END BLOCKS ---
