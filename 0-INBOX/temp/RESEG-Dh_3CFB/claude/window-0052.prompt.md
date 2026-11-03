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
[Block 1821]
ཐོག་མའི་བསྐལ་པ་པ་རྣམས་ལ་མཐོང་བ་ཉིད་མེད་པར་ཐ་སྙད་རྣམས་ལ་ཕྱིས་འཇུག་པར་འགྱུར་བར་འདོད་པ་མ་ཡིན་ནམ་མ་ཡིན་ཏེ། ལེགས་པར་བྱས་པ་གཞན་གྱིས་བསྒོས་པས་དེ་དག་གིས༌[^1327]ནི་རྐྱེན་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་སད་པའི་ཕྱིར་རོ། །

[Block 1822]
གལ་ཏེ་ཐམས་ཅད་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་འགྱུར་རོ་ཞེ་ན།

[Block 1823 [VERSE]]
དེ་འདྲའི་སྐྱེས་བུས་མ་བྱས་ཉིད། །
གྲུབ་ནའང་ཡོན་ཏན་ཅི་ཞིག་འགྱུར། །

[Block 1824]
རྣམ་པ་གང་གིས་མི་སླུ་བའི་ཕྱིར། སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་འདོད་ན་དེ་ནི་ཐོག་མ་མེད་པ་ཉིད་ཅན་དུ༌[^1328]ཡིན་པའི་ཕྱིར། སླུ་བར་བྱེད་པ་ལ་ལ༌[^1329]དག་ལ་ཡང་ཡོད་པས་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་ཀྱིས་ཅི་ཞིག་བྱ། རིག་བྱེད་ཀྱི་ངག་དག་ཁོ་ན་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་ན་ཡང་། དོན་ནི་འདུས་བྱས་ཁྱད་པར་རྣམས། །མཐོང་ཕྱིར་ཐེ་ཚོམ་དག་ཀྱང་ཡིན། གལ་ཏེ་སྐྱེས་བུས་བྱས༌[^1330]མ་བྱས་པ་ཉིད་ཡིན༌[^1331]ཡང་དེའི་དོན་གྱིས༌[^1332]སྤོབས་པ་སོ་སོར་ངེས་པ་བསྐྱེད་པར་འགྱུར་བ་ན་ཡིད་ཆེས་པར་འགྱུར་རོ། །

[Block 1825]
ཇི་ལྟར་འདོད་པ་བཞིན་དུ་སྒྲོ་འདོགས་པ་དང་སྐུར་པ་འདེབས་པ་དག་གིས་ངེས་པར་བརྗོད་པ་དང་དཔྱོད་པ་པ་ལ་སོགས་པ་དག་གིས་རིག་བྱེད་ཀྱི་ངག་རྣམས་ཐ་དད་པར་བྱེད་པར་མཐོང་ངོ་། །དོན་དེ་རྣམས་དེ་དག་མི་འཐད་པར་འགྱུར་བ་མ་ཡིན་ཏེ། དོན་ལ་འཇུག་པ་བརྡ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་དང་། ངག་གཅིག་ལ་ཡང་རྣམ་པར་རྟོག་པ་དུ་མ་སྲིད་པའི་ཕྱིར་དང་། རང་བཞིན་དང་རྐྱེན་རྣམས་ཀྱི་དོན་དུ་མར་བརྗོད་པའི་ཕྱིར་དང་། གྲོགས༌[^1333]སུ་ཟིན་ཀྱང་གཅིག་ཉིད་དུ་ཁས་མི་ལེན་པའི་ཕྱིར་དང་། མ་གྲགས་པའི་མང་བ་ཉིད༌[^1334]ཕྱིར་དང་། དེའི་དོན༌[^1335]སྐྱེས་བུས་བསྟན་པ་ལ་རག་ལུས་པའི་ཕྱིར་དང་། དེས་བསྟན་པ༌[^1336]ནི་དེའི་འདོད་པའི་རྗེས་སུ་འཇུག་པའི་ཕྱིར། རིག་བྱེད་ཀྱི་ངག་གི་དོན་རྣམས་ངེས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1826]
གཞན་ཡང་འདི་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་བསྒྲུབས༌[^1337]ན་ཡི་གེ་རྣམས་སམ་ངག་སྒྲུབ་པར་བྱེད་པར་འགྱུར་གྲང༌[^1338]ན། དེ་ལ།

[Block 1827 [VERSE]]
ཡིག་རྣམས་གཞན་ལ་ཁྱད་མེད་ཕྱིར། །
སྒྲུབ་པར་བྱེད་པར་འབྲས་ཅིར༌[^1339]འགྱུར། །

[Block 1828]
འཇིག་རྟེན་པ་དང་རིག་བྱེད་པ་དག་གི་ངག་གི༌[^1340]ཡི་གེ་ཐ་དད་པ་མ་ཡིན་ནོ། །

[Block 1829]
ཐ་དད་ན༌[^1341]ཡང་ངོ་ཤེས་པ་ལ་ཁྱད་པར་མེད་པའི་ཕྱིར། །དེ་ལས་གཅིག་ཉིད་མ་གྲུབ་པར་ཐལ་བར༌[^1342]འགྱུར་བའི་ཕྱིར་དང་། ཁྱད་པར་རྟོགས་པ་མེད་པའི་ཕྱིར་དང་། རིག་བྱེད་པའི་ཡི་གེ་དག་མ་འགྲུབ་པའི༌[^1343]ཕྱིར་དང་། ངོ་ཤེས་པ་ལས་རྟོགས་པ་མེད་པའི་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དང་། ཁས་མི་ལེན་པའི་ཕྱིར་རོ། །

[Block 1830]
དེ་དག་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་བསྒྲུབས་པ༌[^1344]ན་དེ་ཐམས་ཅད་ལ་མཚུངས་པའི་ཕྱིར། འདིས་ལྷག་པ་ཅི་ཞིག་བྱས། དེ་ལྟར་ཐ་སྙད་ཐམས་ཅད་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་ན་ཐམས་ཅད་བདེན་པ་མ་ཡིན་པའི་ཕྱིར། ཡོངས་སུ་ངལ་བ༌[^1345]དོན་མེད་པ་ཡིན་ནོ།། །།

[Block 1831]
བམ་པོ་བརྒྱད་པ། ཅི་སྟེ་ངག་རྣམས་སྐྱེས་བུས་མ་བྱས་པར་འདོད་ན་ནི།

[Block 1832 [VERSE]]
ངག་ནི་ཡི་གེ་ལས་ཐ་དད། །
པར་ཡོད་མིན་ཏེ་མི་དམིགས་ཕྱིར། །

[Block 1833]
ཁོ་བོ་ཅག་གི་བློ་ལ་ལྷ་སྦྱིན་ལ་སོགས་པའི་ཚིག་དང་ངག་རྣམས་ཀྱི་ཡི་གེ་ད་ལ་སོགས་པ་སྣང་བ་མ་གཏོགས་པར་ཡི་གེ་གཉིས་པ་སྣང་བ་དང་འདྲ་བར། སྣང་བ་གཞན་ནི་མ་མཐོང་ངོ་། །འཛིན་པ་ལ་སྣང་བར་གྱུར་པ་མེད་ན་གཟུང་བར་འདོད་པ་ཡོད་པའམ། གཞན་ཞེས་ངེས་པར་ནུས་པ་མ་ཡིན་ཏེ་རྣམ་པ་གཞན་བཞིན་ནོ། །

[Block 1834]
གལ་ཏེ་གཞན་ལ་མི་སྲིད་པ་ཅན་གྱི་འབྲས་བུ་གོ་བར་བྱེད་པ་ཡིན་ནོ་ཞེ་ན། ཡིན་ན་གལ་ཏེ་ཡི་གེ་ཡོད་པ་དེ་དག་ལ་ཡང་འབྲས་བུ་དེ་མེད་པར་འགྱུར་རོ། །

[Block 1835]
གལ་ཏེ་ཚིག་དང་ངག་གཞན་ལ་དེ་དག་ཁྱད་པར་མེད་པ་ཡིན་ན་ཡང་། མེད་པའི་ཕྱིར་འགྱུར་བ་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་དག་ནི་ཁྱད་པར་མེད་པ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1836]
གལ་ཏེ་ངོ་ཤེས་པ་ལས་ཁྱད་པར་གྲུབ་པ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ནི་འཁྲུལ་པའི་ཕྱིར་དང་། དཔེ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1837]
ཡི་གེ་ཁྱད་པར་མེད་པ་ཡིན་ན་ཡང་ངག་གི༌[^1346]ཁྱད་པར་ལས༌[^1347]དོན་རྟོགས་པའི་ཁྱད་པར་ནི་འབྲས་བུའི་ཁྱད་པར་ཡིན་པར་འགྱུར་ལ་དེ་ཡང་ངག་ལས་འགྱུར་རོ། །

[Block 1838]
དེ་ཡང་དབང་པོ་ལས་འདས་པ་ཡིན་པའི་ཕྱིར་གང་ལས་འགྱུར། ཐག་ཉེ་བ་ཙམ་གྱིས་བསྐྱེད་པ་ཡིན་ན༌[^1348]མ་བྱང་བར་ཡང་འགྱུར་རོ། །

[Block 1839]
དེ་བས་ངག་ཅེས་བྱ་བ་ཡི་གེ་དག་ལས་དོན་གཞན་དུ་གྱུར་པ་ཅུང་ཞིག་ཀྱང་མེད་ན་གང་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་བསྒྲུབ་པར༌[^1349]འགྱུར། དེ་མེད་པའི་ཕྱིར་རིག་བྱེད་ཀྱི་ཁྱད་པར་དུ་མ་བྱས་པའི་ཡི་གེ་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་ཀྱི་ཕྱོགས་དང་པོའི་ཡང་ལན་བཏབ་པ་ཡིན་ནོ། །

[Block 1840]
གཞན་ཡང་དོན་གཞན་དུ་གྱུར་པའི་ངག་ཡོད་པ་ནི་བླ་སྟེ། དེ་ཡན་ལག་དུ་མའི་བདག་ཉིད་ཅན་ནམ། ཡན་ལག་མེད་པ་ཅན་དུ་འགྱུར་གྲང༌[^1350]ན།

[Block 1841 [VERSE]]
ཡན་ལག་དུ་མའི་བདག་ཉིད་ཡིན། །
དེ་རྣམས་ཐ་དད་དོན་མེད་ཉིད། །

[Block 1842]
གལ་ཏེ་དེའི་ཡན་ལག་དེ་དག་ཀྱང་དུ་མ་ཡིན་ན། ཐ་དད་པའི་རང་བཞིན་དོན་མེད་པ་ཅན་ཡིན་ནོ། །

[Block 1843 [VERSE]]
དེ་དངོས་ཅན་མིན་དེ་དངོས་ཅན། །
བརྟགས་པ༌[^1351]སེང་གེ་ཉིད་སོགས་བཞིན། །

[Block 1844]
དོན་དང་ལྡན་པའི་བདག་ཉིད་ཁོ་ན་ངག་ཡིན་ནོ། །

[Block 1845]
ཡན་ལག་དེ་དག་ཀྱང་བདག་ཉིད་དོན་མེད་པ་ཡིན་ཏེ། དེ་དག་བདག་ཉིད་དེས་རྟོགས་པས་སྒྲོ་བཏགས་པར་འགྱུར་རོ། །

[Block 1846]
བྲམ་ཟེའི་ཁྱེའུ་ལ་སོགས་པ་ལ་སེང་གེ་ཉིད་ལ་སོགས་པའི་དང་འདྲ་བ་ཡིན་པའི་ཕྱིར། སྐྱེས་བུས་བྱས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1847]
ཅི་སྟེ་གལ་ཏེ་སྐྱོན་དེར་མ་གྱུར་ཅིག་སྙམ་པས་ཡན་ལག་དེ་དག་སོ་སོ་དོན་དང་བཅས་པར་འདོད་ན།

[Block 1848 [VERSE]]
རེ་རེ་དོན་བཅས་ཉིད་ཡིན་ནའང་། །
དུ་མ་ཉིད་རྟོགས༌[^1352]ལོག་པ་ཡིན། །
ཡན་ལག་གཅིག་ནི་རྟོགས་པས་ཀྱང་། །
ངག་གི་དོན་དག་རྟོགས་པར་འགྱུར།

[Block 1849]
[^1353] །དོན་ཡོངས་སུ་རྫོགས་པ་ཅན་གྱི་སྒྲའི་ངོ་བོ་ནི་ངག་ཡིན་ནོ། །

[Block 1850]
ཡན་ལག་དེ་དག་ཀྱང་སོ་སོ་སོ་སོར་དེ་ལྟ་བུའི་རྣམ་པ་ཡིན་པའི་ཕྱིར། སོ་སོ་དེ་དག་ངག་ཡིན་ནོ། །

[Block 1851]
དེ་ལྟར་ཡན་ལག་དུ་མ་ཅན་ནི་ངག་མ་ཡིན་ནོ། །

[Block 1852]
ཡན་ལག་གཅིག་རྟོགས་པས་ཀྱང་ངག་གི་དོན་རྟོགས་པའི་ཕྱིར།

[Block 1853]
ཡན་ལག་གཞན་ལ་ལྟོས་པ་དང་། །དུས་ལ་སྡོད་པར་མི་འགྱུར་རོ། །

[Block 1854]
ཆ་ཤས་མེད་པའི་བདག་ཉིད་ཅན་དེ་ནི་སྐད་ཅིག་མ་གཅིག་གིས་རྟོགས་པའི་ཕྱིར། ཤེས་པ་གཅིག་སྐྱེས་པ་ན་མ་ལུས་པར་ཁོང་དུ་ཆུད་པའི་ཕྱིར་རོ། །

[Block 1855]
དེ་ལྟ་མ་ཡིན་ན་གཅིག་པ་ཉིད་འགལ་བའི་ཕྱིར་རོ། །

[Block 1856 [VERSE]]
ཐམས་ཅད་ཅིག་ཅར་ཐོས་ན༌[^1354]ཡང་། །
དུས་ཀྱི་ཐ་དད་མི་རུང་ངོ་། །

[Block 1857]
ཡན་ལག་གཞན་ལ་ལྟོས་པ་མེད་པར་ཡང་ཡན་ལག་གཅིག་ཁོ་ན་ལ་ངག་གི་དོན་གྲུབ་པའི་ཕྱིར། ངག་གི་ཡན་ལག་དུ་མ་ཉིད་ཉམས་པར་མ་གྱུར་ཅིག་སྙམ་པས་ཅིག་ཅར་ཡན་ལག་ཐམས་ཅད་ཐོས་པར་འདོད་ན། དེའི་ཚེ་ཡང་དུས་ལ་སྡོད་པ་མི་རིགས་པ་ཁོ་ན་ཡིན་ཏེ། ཡན་ལག་གཅིག་རྟོགས་པའི་དུས་ཉིད་ན་ཐམས་ཅད་ཐོས་པའི་ཕྱིར་རོ། །

[Block 1858]
རིམ༌[^1355]བཞིན་དུ་ཐོས་པ་ཡིན་ན་ཡང་དོན་ཐ་དད་པ་དང་ལྡན་པ་དག་ནི་གཅིག་ཉིད་ལས་དེའི་དོན་གྲུབ་པའི་ཕྱིར། གཞན་ནི་དོན་མེད་པ་ཅན་ཉིད་དུ་འགྱུར་བའི་ཕྱིར་རོ།[^1356] །ཅིག་ཅར་ཐོས་ན་ཡང་དོན་ཐ་དད་པ་དག་ལ་མཐོང་བའི་ནུས་པ་མེད་པ་ཅན་དག་གི་དོན་དང་ལྡན་པ་ཉིད་ཀྱང་མི་འགྲུབ་པོ། །གལ་ཏེ་ཚོགས་པ་རྣམས་ཀྱི་དོན་མཐོང་བའི་ཕྱིར་སྐྱོན་མེད་དོ་ཞེ་ན། མ་ཡིན་ཏེ། ཐ་དད་པ་ལ་ཡོད་པ་མ་ཡིན་པའི་ངོ་བོའི་ཚོགས་པ་ལ་ཡང༌[^1357]མི་སྲིད་པའི་ཕྱིར་དང་། དོན་གཞན་མི་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1859]
རེ་ཞིག་སྒྲ་སྐྱེ་བར་སྨྲ་བ་ལ་སྐྱོན་འདི་ཉིད་ཡོད་པ་མ་ཡིན་ཏེ། སོ་སོར་ནུས་པ་མེད་པའི་ཡན་ལག་རྣམས་ཀྱང་ཕན་འདོགས་པའི་ཁྱད་པར་ལས་ཕུལ་དུ༌[^1358]བྱུང་བ་དང་ལྡན་པའི་འབྲས་བུའི་ཁྱད་པར་ལས་ཉེ་བར་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 1860]
ཡན་ལག་རེ་རེ་ནུས་པ་ཡོད་པ་ཡིན་ན་ཡང་གཞན་དུ་རྟོགས་པ་དོན་མེད་པར་འགྱུར་རོ། །
--- END BLOCKS ---
