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
[Block 1856]
[^1298]འདིར་གཉིས་ཀ་རྣམ་པར་བྲལ་བར་བྱེད་པ་ལས་ཡོངས་སུ་བཟུང་བ་དང་བཅས་པའི་འདུ་ཤེས་ཡོད་པ་ལ་རྣམ་པར་ལྡང་བ་སྟེ། གསོད་པའི་བློ་དང་སྙིང་རྗེའི་སེམས་ཀྱིས་ཞེས་བྱ་བའོ། །

[Block 1857]
དེ་ལ་སྙིང་རྗེའི་སེམས་ཀྱིས་འདི་བྱེད་པ་ལ་ཉེས་བྱས་ཏེ་ཞེས་བྱ་བར་འཆད་པར་འགྱུར་རོ། །

[Block 1858]
ལྷག་མ་གསོད་པའི་བློས་ཆོ་ག་འདི་བྱེད་པ་ལ་རྣམ་པར་ཞུགས་པར་རིག་པར་བྱའོ། །

[Block 1859]
སྙིང་རྗེ་དང་ལྡན་པའི་སེམས་ཀྱིས་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ལ། ཡོངས་སུ་བཟུང་བ་དང་བཅས་པའི་འདུ་ཤེས་ཡོད༌[^1299]པ་ལ་བཟུང་བ་བཏང་བ་ལ་སོགས་པས་གཞན་གྱི་དོན་དང་བྲལ་བར་བྱེད་པ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 1860]
སྔར་བྱས་ན་ཕྱིར་བཅོས་མ་བྱས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་དེ་ན་བུད་མེད་ནི་མང་སྐྱེས་པ་ནི་ཉུང་ངོ་ཞེས་སྔར་སྦྲན་པའི་ལོ༌[^1300]རྒྱུས་དབུལ་བའི་ཕྱིར་བཅོས་པ་སྟེ། གང་དུ་ཕྱིར་བཅོས་པ་རྐུན་པོ་རྣམས་ཕྱིར་བཟློག་པ་ལ་སོགས་པ་བྱེད་པ་དེ་ལ་དང་པོ་ནི་རྩོམ་པ་བྱས་པ་མེད་པར་མི་འགྱུར་རོ། །

[Block 1861]
དེ་བས་ན་དེར་སྦོམ་པོའི་ལྟུང་བ་ལས་མེད་པར་ཤེས་པར་རིག་པར་བྱའོ། །

[Block 1862]
ནོམ་པའི་སྔ་རོལ་ནི་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་བསམ་པའི་དབྱེ་བས་བྱ་བ་ནི་དབྱེ་བའོ། །

[Block 1863]
བྱ་བའི་དབྱེ་བས་ལྟུང་བ་དབྱེ་བའོ་ཞེས་བྱ་བ་ངེས་པར་བསམ་པའི་དབྱེ་བས་བྱ་བའི༌[^1301]དབྱེ་བ་ངེས་པར་བྱའོ། །

[Block 1864]
དེ་ལ་ཇི་ལྟར་དངོས་གཞིའི་སྦྱོར་བ་ལ་བྱ་བ་གཞན་ཉིད་ངེས་པར་བྱས་ནས་ལྟུང་བ་གཞན་དང་རྣམ་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 1865]
དེ་བཞིན་དུ་ནོམ་པའི་སྔ་རོལ་དུ་བསམ་པའི་དབྱེ་བ་ཡོད་པ་ཡིན་ཞེས་བྱ་བ་བྱ་བ༌[^1302]གཞན་ཉིད་ངེས་པར་བྱས་ནས་ལྟུང་བ་གཞན་དང་དམན་པར་རིག་པར་བྱའོ། །

[Block 1866]
འདིར་གཞུང་ནི། ཇི་སྲིད་དུ་ནོམ་པར་མི་བྱེད། མཆོག་ཏུ་ནོམ་པར་མི་བྱེད་པ་དེ་སྲིད་དུ་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 1867]
ཀུན་ནས་ནོམ་པར་བྱེད་མཆོག་ཏུ་ནོམ་པར་བྱེད་ཅིང་ཇི་སྲིད་དུ་གནས་ནས་གནས་སུ་སྦེད་པར་མི་བྱེད་པ་དེ་སྲིད་དུ་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1868]
ཐ་མ་གཏོང་བར་གྱུར་པ་གང་ཡིན་པ་དེ་ལ་རྩོམ་པ་ནི་དེ་ནས་བྱ་བ་གཞན་ཉིད་རྣམ་པར་གཞག་གོ། །

[Block 1869]
གང་ཞིག་ལ་གཏོང་བར་གྱུར་པ་མ་ཡིན་ན་ནི་དཔེར་ན་ནོམ་ཞིང་ཉུག་ན་དོན་གྱི་དབང་དུ་སུ་ཞིག་གིས་སླར་མནན་པ་ཞེས་བྱ་བར་ཤེས་པར་རིག་པར་བྱའོ། །

[Block 1870]
ཕྲི་བའི་གོམ་པ་རེ་རེ་ལ་དེ་ཐ་དད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གོམ་པ་ཕྲི་བ་ལ་རྫས་བཟུང་བའི་དགེ་སློང་གིས༌[^1303]དེའི་བདག་པོའི་དྲུང་ནས་རྐུ་བའི་དོན་དུ་ཕྲི་བའི་གོམ་པ་རེ་རེ་ལ་དེ་ཐ་དད་པ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 1871]
གང་ནས་མི་སྣང་བར་འགྲོ་བའི་རྐང་པ་བཏེག་པའི་རྐང་པ་དེ་ནི་སྦྱོར་བ་ཉིད་ཡིན་ནོ། །

[Block 1872]
གཞན་རྣམས་ལ་ནི་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་དང་སྣ་ཚོགས་པ་ཉིད་དེ་གཅིག་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིའི་བྱེད་པའོ། །

[Block 1873]
ཐ་མའི་རྐང་པ་བཏེག་པ་ལ་སྦོམ་པོ་སྟེ། གཞན་རྣམས་ལ་ནི་སོ་སོར་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་ཐོབ་པའི་དོན་དུ་སོ་སོར་བཏེག༌[^1304]པར་འདིར་རྩོམ་པར་གྱུར་པ་ཉིད་དེ་འགའ་ཞིག༌[^1305]ཏུ་ནི་རྫོགས་པར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 1874]
དེ་བས་ན་གོམ་པ་རེ་རེར༌[^1306]འདིར་ཐ་དད་པའོ། །

[Block 1875]
དེའི་གཞི་ལ་ནི་སེམས་ཅན་སོ་སོ་ལའོ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གྱི་གཞི་སེམས་ཅན་གྱི་རྟེན་ལ་བརྐུས་པ་དང་གསོད་པ་དང་མཚོན་བྱིན་པ་དང་སྦ་བ་ལ་སོགས་པ་ལ་སེམས་ཅན་སོ་སོ་ལ་དངོས་གཞི་དང་སྦྱོར་བའི་བདག་ཉིད་ཅན་གྱི་ལྟུང་བ་ཐ་དད་དོ། །

[Block 1876]
ཕུར་པ་ལས་བཀྲོལ་བ་ལ་ནི་གྲུ་ལ་རེག་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཐག་པ་གྲུ་དང་འབྲེལ་པ་ཉིད་ཀྱི་ཕྱིར་དེ་ལ་རེག་པས་གྲུ་ལ་རེག་པ་ཉིད་ཅེས་བྱ་བའི་དོགས་པ་བསལ་བའི་ཕྱིར་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་དོ། །

[Block 1877]
འདིར་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་ནི་ཉེས་བྱས་ཡིན་ཏེ། འདིར་སྦོམ་པོ་མ་ཡིན་ཏེ། འདི་ལ་བྱེད་པའོ། །

[Block 1878]
འདིར་གཞུང་ནི། དགེ་སློང་གིས་རྐུ་སེམས་ཀྱིས་གྲུ་ཕུར་པ་ལ་བཏགས་པ་སྐྱོད་པར་བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1879]
དེ་བྱས་ནས་རྐུ་བ་ལ་ནི་ཁུར་བརྐུས་པ་ནའོ་ཞེས་བྱ་བ་ལ། དེ་བྱས་ནས་ཞེས་བྱ་བ་ནི་ཁུར་བུ་བྱས་ནས༌[^1307]རྐུ་བ་ནི་གང་དུ་ཁུར་བུ་བྱས་ཏེ་རྐུ་བའོ། །

[Block 1880]
དཔེར་ན་གོས་རྣམས་རླུང་གིས༌[^1308]སྣ་ཚོགས་པའི་ཕྱོགས་རྣམས་སུ་རྣམ་པར་འཕེན་པར་བྱེད་པ་དེར་ཁུར་བུ་འཕྲོག་པ་ཡིན་གྱི༌[^1309]རྫས་རེ་རེ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1881]
མ་ཤ་ཀ་ལྔ་ལ་སོགས་པའི་རིན་ཐང་གི་ཚད་ནི་གོས་ལ་སོགས་པ་དག་ཁུར་དྲགས་པའི་སྔ་རོལ་དུ་གནས་སྤོ་བར་བྱེད་ཀྱང་དེ་ལྟར་ན་ཡང་ཕམ་པར་མི་འགྱུར་ཏེ། དེའི་ཚེ་ན་དེ་ལ་བསྡུའོ་སྙམ་པའི་བློ་ཡོད་ཀྱི་རྐུའོ་སྙམ་པའི་བློ་མེད་པའི་ཕྱིར་རོ། །

[Block 1882]
འདིར་གཞུང་ནི། འདི་ལྟར་བཙོ་བླག་མཁན་གྱིས་གོས་རྣམས༌[^1310]འཁྲུ་ཞིང་གོས་དག་བཏིང་བ་རླུང་གིས་ཁྱེར་ཞིང་དགེ་སློང་དེ་ལ་སྦྱོར་བས་ཇི་སྲིད་དུ་ནོམ་པར་མི་བྱེད། ཉུག༌[^1311]པར་མི་བྱེད་པ་དེ་སྲིད་དུ་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 1883]
ནོམ་པར་བྱེད། ཉུག་པར་བྱེད། གོས་དག་སྡུད་པར་བྱེད། བམ་པོར་སྦྲེལ་བར་བྱེད་ཅིང་། ཇི་སྲིད་དུ་གནས་ནས་གནས་སུ་སྦེད་པར་མི་བྱེད་པ་དེ་སྲིད་དུ་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 1884]
གནས་ནས་གནས་སུ་སྦེད་པར་བྱེད་ན་བརྐུས༌[^1312]པར་བརྗོད་པར་བྱ་སྟེ། རིན་ཐང་བརྩི་བར་བྱ་ཞིང་དེ་སྲིད་དུ་སྦོམ་པོའི་ལྟུང་བ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 1885]
བཏུས་ནས་ནི་ཕུང་པོ་ནའོ་ཞེས་བྱ་བ་ནི་རྫས་གང་ཞིག་བཏུས་ནས་རྐུ་བར་བྱེད་པ་ནི་མེ་ཏོག་དང་འབྲས་བུ་རྣམས་སོ། །

[Block 1886]
དེའི་ཚེ་ནམ་ཕུང་པོ་བཅེར་བ་ཁོ་ན་བརྐུས་པ་ཡིན་གྱི༌[^1313]རྫས་རེ་རེ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1887]
གང་གི་ཚེ་ན་ཕུང་པོ་དེ་གནས་ནས་འཕོ་བར་གྱུར་ན་དེའི་ཚེ་དངོས་གཞིའི་ལྟུང་བའོ། །

[Block 1888]
གང་གི་ཚེ་མེ་ཏོག་དང་འབྲས་བུ་རེ་རེ་ཡང་རིན་ཐང་མ་ཤ་ཀ་ལྔ་ལ་སོགས་པའི་ཚད་དེ་ལ་བསྡུ་བའོ་སྙམ་པའི་བློ་འདིར་ཡོད་པས་རྐུ་བའི་བློ་ནི་མ་ཡིན་ནོ། །

[Block 1889]
ཕུང་པོ་འདི་ལ་གཞུང་ནི། ཤིང་རྣམས་ནི་གསུམ་ཡིན་ཏེ། མེ་ཏོག་གི་ཤིང་དང་། འབྲས་བུའི་ཤིང་དང་། གྲིབ་མའི་ཤིང་ཞེས་བྱ་བ་སྟེ། དགེ་སློང་ནི་མེ་ཏོག་རྣམས་ཀྱི་ཕྱིར་ཁྲི་ལས་ལྡང་ཞིང་གོས་གྱོན་པར་བྱེད་དེ་འགྲོ་བར་བྱེད། །མེ་ཏོག་གི་ཤིང་ལ་འཛེག་སྟེ་ཇི་སྲིད་དུ་ནོམ་པར་མི་བྱེད། ཉུག་པར་མི་བྱེད་པ་དེ་སྲིད་དུ་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 1890]
ནོམ་པར་བྱེད། ཉུག་པར་བྱེད། [^1314]མེ་ཏོག་རྣམས་འཐོག་པར་བྱེད། ཐུ་བ་འགེངས་པར་བྱེད་ཅིང་ཇི་སྲིད་དུ་གནས་ནས་གནས་གཞན་དུ་འཕོ་བར་མི་བྱེད་པ་དེ་སྲིད་དུ་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1891]
བཏུས་པ་རྣམས་ཀྱི༌[^1315]ཚོགས་ནི་ཕུང་པོའོ། །

[Block 1892]
སྤྱིངས་པ་ལ་ནི་གནས་ཀྱི་སྟེང་ནས་རྫས་ཀྱི་སྟེང་ན༌[^1316]བྱིང་ནའོ་ཞེས་བྱ་བ་ནི་བརྐུ་བར་བྱ་བའི་རྫས་ཀྱི་གནས་ནི་ཆུ་ལ་སོགས་པ་གང་ཡིན་པའོ། །

[Block 1893]
དེའི་སྟེང་ནི་གང་ཞིག་སྟེང་གི་ཡ༌[^1317]མཐའ་ཆའི་སྟེང་རིམ་མོ། །

[Block 1894]
དེའི་སྤྱིངས་པའི་ལྟུང་བ་རྐུ་བཞིན་པའི་རྫས་ལ་ནི་བྱིང་བ་ཉིད་ལ་ནི་སྟེང་གང་ཞིག་ཡ་བླའི་ཆའི་སྟེང་རིམ་དེའི་བྱིང་བ་ལས༌[^1318]འཕོ་བའོ། །

[Block 1895]
གནས་གཞན་དུ་བྱིང་བ་ལ་ནི་འཕོ་བ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
