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
[Block 2241]
མ་གནང་བ་ལ་བསྲི་བ་མེད་པ་ཉེ་བར་ལོངས་སྤྱོད་པ་ནི་ཤིན་ཏུ་ལྕི་བ་ཉིད་དེ་དེ་བས་ན་འདིར་ཡང་འདིས་སྦོམ་པོའི་ལྟུང་བ་བྱས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2242]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས༌[^1554]ཁྱིམ་བདག་གི་གོས་བརྙན་པ༌[^1555]བཏགས་ཏེ་རྐུ་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2243]
ཅི་སྟེ་ཁྱིམ་བདག་འདི་སྐད་ཅེས་འཕགས་པ་བདག་ཉིད༌[^1556]འདི་ཁྱོད་ལ་བརྙན་ནོ་ཞེས་ཟེར་ན་དགེ་སློང་དེ་ལ་བསྲི་བ་མེད་པའི་འདུ་ཤེས་ཅན་དེ་ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པར་བྱེད་ན་སྦོམ་པོའི་ལྟུང་བར་འགྱུར་ཞེས་བྱ་བ་འདིའི་འདི་བསྡུས་པའོ། །

[Block 2244]
འདི་ལས་སྔ་རོལ་གྱི་གཞུང་ལས་རུང་བ་ཞེས་བྱ་བའི་མདོ་འདི་བསྡུས་པའོ། །

[Block 2245]
གསང་སྔགས་དང་སྨན་དག་གིས་འབུལ་དུ་བཅུག་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་བཞིན་ནོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 2246]
དེ་ནི་ཆད་པས་བཅད་པའི༌[^1557]རྣམ་པ་ཡིན་པ་སྟེ། དེ་བས་ན་འདིར་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2247]
འདིར་གཞུང་ནི་ཇི་སྟེ་དེས་གསང་སྔགས་ཀྱིས་སམ། མེ་ཏོག་དང་འབྲས་བུ་རྣམས་ཀྱིས་སྩལ༌[^1558]ནས་ཁྱིམ་བདག་དེས་འདི་སྐད་ཅེས་འཕགས་པ་བདག་གིས་འདི་ཁྱོད་ལ་བརྙས་པ༌[^1559]བརྙན་ནོ་ཞེས་ཟེར་ནས། དགེ་སློང་དེ་ལ༌[^1560]ཡང་བསྲི་བ་མེད་པའི་འདུ་ཤེས་ཅན་དང་། ངེས་པར་བྱིན་པ་ཉིད་ཀྱི་འདུ་ཤེས་ཀྱིས་ཉེ་བར་སྤྱད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2248]
ངེས་པར་བྱིན་པའི་འདུ་ཤེས་ཅན་ཞེས་བྱ་བ་ནི་དེ་ལྟར་རྙེད་པ་ལ་བདག་ཏུ་བྱ་བ་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 2249]
ཡོངས་སུ་ཚིམ་པར་བྱ་བའི་ཕྱིར་མེ་ཏོག་དང་འབྲས་བུ་སྦྱིན་པ་གང་ཡིན་པ་ནི་མ་གཏོགས་པ་སྟེ། དེ་ནི་ལོག་པའི་འཚོ་བ་ལ་མཚན་མ་རྙེད་པ་དང་བླངས་པས་བསམ་པ་བྲལ་བར་གྱུར་པ་རྐུ་བ་ལ་བརྟེན་པའི་སྐྱོན་མི་སྐྱེད་པ༌[^1561]ཉིད་དོ། །

[Block 2250]
དེ་བས་ན་དབང་དུ་བྱ་བ་ལ་མཁས་པར་གྱུར་པའི་མེ་ཏོག་དང་འབྲས་བུ་རྣམས་ལ་མ་བཟུང་བ་འདི་རྣམ་པར་ཤེས་པའོ། །

[Block 2251]
གཞན་གྱི་དོན་ཉིད་དུ་ན་ཡང་དངོས་གཞིའི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དོན་ལ་བདག་གི༌[^1562]བྱ་བ་མ་སྐྱེས་པར༌[^1563]གང་རྐུ་བར་བྱེད་ན་ཡང་དེ་ལ་དངོས་གཞིའི་རྣམ་པའོ་ཞེས་བྱ་བ་དངོས་གཞིའི་སྦྱོར་བ་སྟེ། དངོས་གཞིའི་ཁ་ན་མ་ཐོ་བ་མ་ཚང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2252]
ཕམ་པར་འགྱུར་བའི་སྦྱོར་བ་ལ་དགོངས་ནས་དངོས་གཞིའི་རྣམ་པ་ཞེས་བརྗོད་དོ། །

[Block 2253]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་མ་བསྒོ་བར་གཞན་གྱི་དོན་ལ་རྐུ་བར་བྱེད་ན་ལྟུང་བར༌[^1564]ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2254]
རྟོག་པས༌[^1565]ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དངོས་གཞིའི་རྣམ་པའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 2255]
ཁ་བཅིངས་པ་ཙམ་དུ་གྱུར་པའི་རྟོག་པ་གང་ཡིན་པ་དེ་ལ་མི་སྐྱེད་པ༌[^1566]འགྲིབ་པ་ལ་དངོས་གཞི་ཉིད་དུ་རྣམ་པར་གནས་ཏེ་དངོས་གཞིའི་རྣམ་པ་ནི་མ་ཡིན་ནོ། །

[Block 2256]
དེ་བས་ན་ཡང་དག་པར་ན་སྐྱོན་མེད་པའི་རྣམ་པའི་གནས་དང་རྗེས་སུ་འབྲེལ་པ་དེ་ལས་བཟློག་པ་རྣམས་ལ་རྟོག་པ་འདི་ཅིས་རྟོགས་པར༌[^1567]བྱ་ཞེ་ན། འདི་ལྟ་སྟེ་དཔེར་ན་འདི་ནི་བདག་གི་ཡིན་ནོ་སྙམ་པའམ། ཡོངས་སུ་བཟུང་བ་མ་ཡིན་ནོ་སྙམ་པའམ། དེ་བདག་ལ་སྦྱིན་ནོ་ཞེས་བྱ་བའི་འདུ་ཤེས་སམ། དམིགས་པ་མེད་པའམ། དོགས་པ་དང་བཅས་པའམ། གཡོ་བ་མེད་པའམ། ཅིག་ཤོས་ཀྱི་འདུ་ཤེས་ཀྱི༌[^1568]སྐྱོན་གྱིས་རྗེས་སུ་འབྲེལ་བའོ། །

[Block 2257]
འོ་ན་འདི་ནི་ཐེ་ཚོམ་ཡིན་ན་དེར་འདི་ལ་སྐྱོན་གྱི་འདུ་ཤེས་ཏེ་ཐེ་ཚོམ་ནི་མ་ཡིན་ནོ། །

[Block 2258]
དེ་བས་ན་གཞན་ཉིད་དུ་གྱུར་པ་ལ་ཕམ་པ་འབྱུང་བར་འགྱུར་ཏེ། གང་ཡང་རུང་བའི་འོ་སྙམ་པའི་བསམ་པ་ཡང་དག་པར་གནས་པར་འགྱུར་བ་ལ་འདི་འབྱུང་བར་འགྱུར་བ་ཉིད་དེ། དེ་ལྟ་བུ་ནི་བདག་ཏུ་བྱས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ངེས་པ་ལ་གནས་པའི༌[^1569]འཛིན་པ་ལ་སྦོམ་པོ་འདི་བརྗོད་པར་རིག་པར་བྱའོ། །

[Block 2259]
གདམས་ཏེ་བཟང་པོ་རྐུ་བར་འདོད་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དངོས་གཞིའི་རྣམ་པའོ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ཏོ། །

[Block 2260]
རྐུ་བར་འདོད་པ་ལ་ཞེས་བྱ་བ་འདི་ལྟ་བུའི་འདོད་པ་ཡོད་པ་ལ། གང་ཞིག་གདམས༌[^1570]པ་དངོས་གཞིའི་རྣམ་པ་དེ་ལ་ཁ་ན་མ་ཐོ་བ་མེད་པའོ། །

[Block 2261]
ཇི་ལྟ་བུ་མེ་ཏོག་རྣམས་ཀྱི་གདམས་པ་དེ་ལྟ་བུ་འདིའོ། །

[Block 2262]
འདི་ལྟར་གཞན་དུ་ནི་ནོམ་པའི་སྔ་རོལ་དུ་ཞེས་བྱ་བ་བརྗོད་པས་འདིའི་ནོམ་པ་སྔ་རོལ་དུ་འདིར་དེའི་དངོས་པོ༌[^1571]དེ་བས་ན་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་དོ། །

[Block 2263]
ནོམ་པའི་སྔ་རོལ་དུ་ཞེས་བྱ་བ་ཉེས་བྱས་ཐོབ་པ་ལ་མདོ་འདིའོ། །

[Block 2264]
འདིར་གཞུང་ནི་བཙུན་པ་མི་རྣམས་ཀྱི་གོས་ཀྱི་གདང་ཤིང་ངམ། གོས་ཀྱི་སྣོད་དམ་གོས་ཀྱི་ཟ་མ་ཏོག་གམ་གླང་པོ་ཆེའི་སོ་བཞག་པར་འགྱུར༌[^1572]ཏེ། དེར་དགེ་སློང་རྐུ་བའི་སེམས་རྣམ་པར་ཤེས་ཏེ། གང་འདོད་པར་གྱུར་པ་དེ་རྐུ་བར་བྱེད་ན་ཅི་ལྟུང་བར་འགྱུར་རམ། ཉེས་པ་སྦོམ་པོའི་ལྟུང་བར་འགྱུར་ཞེས་བྱ་བའོ། །

[Block 2265]
གང་ཞིག་འདོད་པ་དེ་ནི་བརྐུས་ཏེ་རིན་ཐང་བརྩི་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2266]
སོ་སོར་བྱེད་པར་འགྱུར་བ༌[^1573]ལ་ཡང་གནས་ནས་གདམས་པ་འདི་ནི་ཉེས་པ་སྦོམ་པོར་རིག་པར་བྱའོ། །

[Block 2267]
གཞན་དོན་དང་བཅས་པ་འདྲ་བར་ཡང་དག་པར་འགྲོ་བ་ལ་བསྡུས་པའི་བློ་ལ་དེར་ཡང་དག་པར་གནས་པས་གདམས་ཏེ། འདིར་སྦོམ་པོའི་ལྟུང་བ་གཅིག་གོ། །

[Block 2268]
གདམས་ཏེ་རྐུ་བའི་དོན་དུ་ནོམ་པ་ལ་གཞན་ཞེས་བྱ་བ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2269]
རྒྱན་ལ་དོར་བྱེད་ན་གལ་ཏེ་དེ་རྒྱལ་བ་ཉིད་དུ་མ་གྱུར་པའི་ཚེ་སྦྱོར་བའོ་ཞེས་བྱ་བ་ནི་རྒྱན་ལ་དོར་བྱེད་ན་གལ་ཏེ་དེ༌[^1574]རྒྱལ་བ་ཉིད་དུ༌[^1575]མ་གྱུར་གྱི་བར་དུ༌[^1576]དོར་ཏེ་སྦྱོར་བར་འགྱུར་རོ། །

[Block 2270]
དེ་ལ་དེ་ནི་བརྐུས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་རྒྱན་ལའོ། །

[Block 2271]
དེ་ནི༌[^1577]ཞེས་བྱ་བ་རྒྱལ་བ་ཉིད་ན་བརྐུས་པ་ཡིན་ནོ། །

[Block 2272]
གང་གི་ཕྱིར་འདིར་རྐུ་བ་ཉིད་ནི་དེ་བས་ན་འདི་ལ་བརྟེན་པའི་དོར་བྱེད་པ་ལ་སྦྱོར་བ་ཉིད་དོ། །

[Block 2273]
དངོས་གཞི་ལ་སོ་སོར་དེ་མ་ཐག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2274]
གྲངས་ལ་ནི་དེའིའོ་ཞེས་བྱ་བ་ནི་གྲངས་ནི་རྩིས་ལས་ཏེ། གང་ཞིག་དོར་བྱེད་པ་ནི་རང་གི་སྦྱོར་ལ་དེའི་སྦྱོར་བ་ཉིད་དང་བཅས་པ་དང་། །དངོས་གཞི་ལ་ཉེས་བྱས་མ་ཡིན་པ་ལ། གྲངས་ཀྱི་སྐབས་སུ་དོར་བྱེད་པ་ཉིད་ནི་ཉེས་བྱས་ཡིན་གྱི་སྦོམ་པོར་ནི་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2275]
མཚན་མ་ཕྱིས་པ་དང་བསྣན་པ་གཉིས་གནས་གཞན་དུ་གཞག་པ་ཡང་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མཚན་མ་གང་ཞིག་གཅིག་ལ་སོགས་པ་ཤོད་ཐབས་ཀྱི་མཚན་ཉིད་བྱས་པ་དེ་ཕྱིས་པ་ཞེས་བྱ་བ་ནི་མེད་པར་བྱས་པའོ། །

[Block 2276]
བསྣན་པ༌[^1578]ལ་གང་ཞིག་མཚན་མ་ལ་ཇི་ལྟར་ཐོབ་པའི༌[^1579]གཞན་དུ་གཞག་པ་ཡང་དེ་ཉིད་དོ༌[^1580]ཞེས་བྱ་བ་ནི་དོར་བྱེད་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2277]
ཐམས་ཅད་དུ་དབང་བྱེད་པའི་མདོ་ཡིན་ནོ། །

[Block 2278]
རྒྱན་གྱི་དབང་དུ་བྱེད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2279]
དེ་ལ་གྲུབ་པ་ན་བརྐུས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དེ་ལ་ཞེས་བྱ་བ་ནི་གྲངས་ལའོ། །

[Block 2280]
གྲུབ་པ་ན་ཞེས་བྱ་བ་ནི་ཐོབ་པ་སྟེ་ནོར་ལ་བརྐུས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
