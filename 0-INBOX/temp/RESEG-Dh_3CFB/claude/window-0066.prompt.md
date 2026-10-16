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
[Block 2311]
དེ་བས་ན་ངོ་བོ་བདག་མེད་པ་ཡིན་གྱི་བདག་ལྡོག་པ་ཙམ་ནི་མ་ཡིན་ནོ། །

[Block 2312]
དེ་ལྟ་མ་ཡིན་ན་ཉེ་བར་བརྗོད་པ་མེད་པ་ལ་བྱས་པ་ཉིད་ལ་སོགས་པ་མི་རུང་བའི་ཕྱིར། དེ་ལས་བདག་མེད་པ་འགྲུབ་པར་མི་འགྱུར་རོ། །

[Block 2313]
གལ་ཏེ་བདག་རྣམ་པར་གཅད༌[^1607]ནས་བདག་མེད་པའི་ངོ་བོ་རྗོད་པར་བྱེད་པའི་ཕྱིར་སྐྱོན་ཡོད་པ་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་པས་དངོས་པོ་ལ་རེག་པའི་ཕྱིར། དངོས་པོའི་ངོ་བོ་དེ་ཉིད་བདག་མེད་པ་ཐོབ་པོ། །གང་གི་རྣམ་པར་བཅད་པ༌[^1608]དངོས་པོ་མེད་པའི་ངོ་བོ་མ་ཡིན་གྱི་དེའི་རྣམ་པར་གཅོད་པ་དངོས་པོའི་ངོ་བོ་ཡིན་ན་ཡང་དངོས་པོ་གྲུབ་པར་མི་འགྱུར་བའི་ཕྱིར། རྗེས་སུ་འགྲོ་བ་འཕངས་པ་མ་ཡིན་ནོ། །

[Block 2314]
དེ་ལྟར་ན་བདག་མེད་པ་ཡིན་ན་ཡང་དངོས་པོར་འགྲུབ་པར་མི་འགྱུར་ཏེ། དཔེར་ན་གསོན་པོའི་ལུས་འདི་ནི་བདག་མེད་པ་མ་ཡིན་ཏེ། སྲོག་ལ་སོགས་པ་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2315]
མི་མཐུན་པའི་ཕྱོགས་དག༌[^1609]གི་ཁྱབ་པར་བྱ་བ་དང་ཁྱབ་པར་བྱེད་པ་དཔྱོད་པ་ན་སྲོག་ལ་སོགས་པ་དང་མི་ལྡན་པ་ཉིད་ལ་བདག་མེད་པ་ཉིད་མཐོང་བ་དང་དེ་མེད་ན་མེད་པའི་ཕྱིར། བདག་མེད་པ་དག་ཉིད་མེད་དུ་ཟིན་ཀྱང་། སྲོག་ལ་སོགས་པ་དག་ནི་བདག་ལ་གྲུབ་པར་འཇོག་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 2316]
དེ་ལྟར་ན་བསྒྲུབ་པར་བྱ་བ་ལ་ཡང་སྲོག་ལ་སོགས་པ་དག་གིས་འབའ་ཞིག་བསལ་བར་འགྱུར་རོ། །

[Block 2317]
བདག་མེད་པ་ཉིད་ལ་མེད་པའི་ཕྱིར། སྲོག་ལ་སོགས་པས་དེ་བསལ་བ་ཡིན་གྱི། བདག་ཉེ་བར་འཇོག་པ་ནི་མ་ཡིན་ཏེ། དེ་ལ་ཡོད་པ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2318]
བདག་མེད་པ་ལ་ལོག་པས་ཀྱང་བདག་གྲུབ་པ་མ་ཡིན་ཏེ། མི་མཐུན༌[^1610]ཕྱོགས་ལ་ལྡོག་པ་མཐོང་བ་ན་ཡང་མཐུན་པའི་ཕྱོགས་ལ་ཡང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2319]
དེ་བས་ན་ལྡོག་པ་མ་གྲུབ་པ༌[^1611]ན་བཟློག་པའི་ཁྱབ་པ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་གྲུབ་པ་ཉིད་ཀྱིས་ཀྱང་རྗེས་སུ་འགྲོ་བ་གྲུབ་པའམ། མ་གྲུབ་པ་ནི་ལྡོག་པ་བཟློག་པ་གྲུབ་ཏུ་ཟིན་ཀྱང་དེ་མ་གྲུབ་པའི་ཕྱིར་བསྒྲུབ་པར༌[^1612]བྱ་བ་ལ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 2320]
དེ་བས་ན་ལྡོག་པའི་ཁྱབ་པ་ལ་རྗེས་སུ་འགྲོ་བ་མེད་པ་མ་ཡིན་ནོ། །

[Block 2321]
ལོག་པའི་དོན་ཅན་དག་ནི་སྐྱེས་བུས་བྱས་པ་ཉིད་ཀྱིས་ཁྱབ་པས་སྐྱེས་བུས་མ་བྱས་པ་ལས་ལོག་པ་ཡིན་དུ་ཟིན་ཀྱང་། བདེན་པའི་དོན་ཅན་ཉིད་མ་ཡིན་ཏེ། རྣམ་པ་གཞན་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2322]
སྒྲ་རྣམས་ལ་ཕུང་པོ་གཉིས་ཡོད་ན་ནི་དེ་ལྟར་འགྱུར་ཏེ། གཅིག་ལོག་པ་ན་རྣམ་པ་གཞན་མེད་པའི་ཕྱིར་རོ། །

[Block 2323]
དེ་དག་དོན་མེད་པ་ཅན་དུ་འགྱུར་བ་དེ་ལྟར་ན་འདོད་པའི་དོན་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 2324]
གལ་ཏེ་དོན་རྟོགས་པའི་ཕྱིར། དོན་མེད་པ་ཅན་མ་ཡིན་ནོ་ཞེ་ན། དེ་དག་གི་སྐྱེས་བུའི་བྱ་བས་འགྱུར་ཏེ། དོན་གཞན་ལ་རྣམ་པར་རྟོག་པ་བཞིན་ནོ། །

[Block 2325]
དཔེར་ན་བྷ་ར་ཏ་ལ་སོགས་པའི་ལུགས་ལ་སོགས་པ༌[^1613]ནི་དེའི་དོན་ཅན་མ་ཡིན་དུ་ཟིན་ཀྱང་དོན་གཞན་དག་གི་རྣམ་པ་གཞན་དུ་བཤད་པ་དེའི་རྗེས་སུ་འབྲངས་ནས་གཞན་གྱིས་ཀྱང་དེ་ལྟར་རྟོགས་པར་འགྱུར་བ་ལྟ་བུའོ། །

[Block 2326]
སྐྱེས་བུས་བསྟན་པ་ལ་རག་ལས་པའི་ཕྱིར། དོན་མེད་པ་ཅན་དག་ལ་དོན་དུ་རྣམ་པར་རྟོག་པ་འདི་ནི་སྐྱེས་བུས་བྱས་པར་འགྱུར་བ་ཡིན་གྱི། སྒྲའི་རང་བཞིན་གྱིས་བྱས་པ་ནི་མ་ཡིན་ཏེ། དོན་གཞན་ཉིད་བཞིན་ནོ། །

[Block 2327]
ངོ་བོ་ཉིད་ཀྱིས་མེ་ལ་སོགས་པ་གསལ་བར་བྱེད་པ་དེ་ལ་ལྟོས་པ་མ་ཡིན་ཏེ། སྐྱེས་བུས་བདག་ཉིད་ཀྱི༌[^1614]བརྡའི་བྱ་བ་བརྗོད་པ་ན་སྟོན་པར་བྱེད་པ་ཞེས་བྱ་བ་ནི་རིགས་པ་ཡིན་ནོ། །

[Block 2328]
སྐྱེས་བུས་བརྡར་བྱས་པ་དང་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པའི་དོན་དག་ནི་བསྟན་པ་ལ་རག་ལུས་པར་ཁྱད་པར་མེད་པའི་ཕྱིར་དང་། ཁྱད་པར་གཞན་མེད་པའི་ཕྱིར་གཅིག་ནི་ངོ་བོ་ཉིད་ཀྱིས་གྲུབ་པ་ཡིན་ལ། གཞན་ནི་སྐྱེས་བུས་བྱས་པ་ཡིན་ནོ་ཞེས་ངེས་པར་དཀའ་བ་ཡིན་ནོ། །

[Block 2329]
གལ་ཏེ་ཚད་མས་མི་སླུ་བའི༌[^1615]བྱེ་བྲག་ཡོད་དོ་ཞེ་ན། དེ་ནི་འོག་ནས་ཤིན་ཏུ་ལྐོག་ཏུ་གྱུར་པའི་དོན་ལ་ཚད་མ་གཞན་འཇུག་པ་མེད་དོ་ཞེས་བྱ་བས་འགོག་པར་འགྱུར་རོ། །

[Block 2330]
ཆོས་མཐུན་པ་ཅན་གྱི་དོན་དག་ལས་ཚད་མས་མི་སླུ་བ༌[^1616]ཙམ་གྱི༌[^1617]ཁྱད་པར་གཅིག་ལ་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་དུ་འདོད་ན། ད་ནི་ཆེས་ཤིན་ཏུ་མང་པོ་སྐྱེས་བུས་བྱས་པ་མ་ཡིན་པ་དེ་ལྟར་ན། སྐྱེས་བུས་བྱས་པའི་དག་འགའ་ཞིག་ཀྱང་དེ་ལྟ་བུའི་རྣམ་པ་ཡིན་པའི་ཕྱིར་དེ་དག་ལ་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 2331]
དེ་དང་འདྲ་བར་དེ་དག་གི་མངོན་བར་འདོད་པའི་དོན་དང་ལྡན་པ་ཉིད་ཀྱང་སྐྱེས་བུས་བྱས་པ་དང་ཚད་མའི་རྗེས་སུ་བྱེད་པ་ཅན་དུ་ཡང་འགྱུར་རོ། །

[Block 2332]
གཞན་ཡང་སྔགས་དང་སྐྱེས་བུས་བྱས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་གནོད་པ་ཡང༌[^1618]མཐོང་ངོ་། །དེ་ལྟར་ནི། ལ་ལ་བརྡར་བྱས་ཉིད་ཡིན་ན། །སྔགས་རྣམས་འབྲས་བུ་སྒྲུབ་བྱེད་ཡིན་པར་རིགས་སོ། །

[Block 2333]
གལ་ཏེ་སྔགས་དེ་དག་འདི་ལྟར་ཁོ་བོས་མངོན་པར་འདོད་པའི་རྒྱུ་ཅན་གྱི་ངག་བྱས་པ་དེ་ཉིད་ལ་དེ་ལྟར་སྦྱར་བར་བྱེད་པ་ན་དོན་འདིས་སྦྱར་བར་བྱའོ་སྙམ་པས་གཞན་གྱི་དོན་གཙོ་བོར་གྱུར་པའི་ངོར་བྱས་པའམ། གཞན་འགའ་ཞིག་གིས་ལ་ལར༌[^1619]བརྡར་བྱས་པར་འགྱུར་བ་དེའི་ཚེ་སྔགས་ཀྱི་སྦྱོར་བ་ལས་འགའ་ཞིག་གི་ཚེ་དོན་གྲུབ་པར་རིགས་པ་ཡིན་ཏེ། འདོན་པར་བྱེད་པ་དག་གི་སྙན་དངགས་མཁན་གྱི་བརྡ༌[^1620]བྱས་པ་ལས་དོན་གྲུབ་པ་བཞིན་ནོ། །

[Block 2334 [VERSE]]
ཅི་སྟེའང་དངོས་པོའི་ནུས་ཡིན་ན། །
ཁྱད་པར་མེད་ཕྱིར་གཞན་ལ་འང་འགྱུར། །

[Block 2335]
སྐྱེས་བུའི་བརྡ་ལས་སྔགས་རྣམས་ཀྱིས་དོན་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 2336]
འོ་ན་ཅི་ཞེ་ན། འདི་རྣམ་པ་འགའ་ཞིག་ལྟར་ངེས་པར་སྦྱར་བ་ན། འབྲས་བུ་འབྱིན་པ་གང་ཡིན་པ་དེ་དག་ནི་དངོས་པོའི་རང་བཞིན་ནོ། །

[Block 2337]
འོ་ན་ནི༌[^1621]ཡི་གེ་རྣམས་ཀྱི་ངོ་བོ་དེ་ཐམས་ཅད་ཁྱད་པར་མེད་པའི་ཕྱིར། ཇི་ལྟར་རྣམ་པ་འགའ་ཞིག་ལྟར་སྦྱར་བ་ལས་ཀྱང་འབྲས་བུར་འགྱུར་རོ། །

[Block 2338]
ཡི་གེ་ཁོ་ན་སྔགས་ཡིན་གྱི་གཞན་ཅུང་ཟད་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2339]
གལ་ཏེ་དེའི་བཀོད་པ་ཡང་སྔགས་ཡིན་ནོ་ཞེ་ན།

[Block 2340 [VERSE]]
དོན་གཞན་ཉིད་དུ་གྱུར་པ་ཡི། །
བཀོད་པའང་སྔར་ནི་བསལ་བ་ཡིན། །

[Block 2341]
ཡི་གེ་དག་ལས་ཐ་དད་པ་བཀོད་པ་གཞན་ནི་མེད་དོ་ཞེས་དེ་བསྟན་ཟིན་ཏོ། །

[Block 2342]
ཐ་དད་པ་མེད་ན་ཡང་ཡི་གེ་ཉིད་སྔགས་ཡིན་ལ། དེ་དག་ཀྱང་ཐམས་ཅད་དུ་ཁྱད་པར་མེད་པའི་ཕྱིར། ཐམས་ཅད་ཀྱི་ཚེ་འབྲས་བུ་འབྱིན་པར་འགྱུར་རོ། །

[Block 2343]
བཀོད་པ་ཆེས་ཆུང་བ་ཡང་ཉམས་པ་ལས་འཁྲུལ་པ་ཡང་མཐོང་ངོ་། །འགའ་ཞིག་ནན་ཏན་དུ་བྱས་པ་ལས༌[^1622]ལྷ་ཉིད་ཐག་ཉེ་བའི་ཕྱིར་དང་། ཚོགས་པ་མེད་པས་མཉེས་པར་མ་བྱས་པའི་ཕྱིར་རོ། །

[Block 2344]
ཐམས་ཅད་ཉམས་ན་ནི་བརྡ་འགའ་ཞིག་ཀྱང་ནན་ཏན་དུ་བྱས་པ་མེད་པས་ཐག་ཉེ་བ་ན་མེད་པའི་ཕྱིར། དོན་དང་དོན་མེད་པ་མ་ཡིན་ནོ། །

[Block 2345]
གཞན་ཡང་བཀོད་པ་དོན་གཞན་ཉིད་དམ་དོན་གཞན་ཉིད་མ་ཡིན་ན་སྔགས་ཡི་གེའི་བདག་ཉིད་ཅན་ནམ། དེའི་བཀོད་པའི་བདག་ཉིད་ཅན་དོན་ཅན་གྱི་རྒྱུ་རྟག་པ༌[^1623]ནི་མ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར། རྟག་ཏུ་ཉེ་བ་ཡིན་པ་དེ་ལྟར་ན། རྟག་ཏུ་དེ་ལས་དོན་གྲུབ་འགྱུར། །གང་གི་ཕྱིར་དངོས་པོའི་ནུས་པ་ལས་འབྲས་བུ་བསྐྱེད་ན། དེ་མ་ཚང་བ་མེད་པའི་ཕྱིར་འབྲས་བུ་དང་བྲལ་བར་མི་འགྱུར་རོ། །

[Block 2346]
རྒྱུའི་ཚོགས་པ་ཡོད་ན་འབྲས་བུ་དང་བྲལ་བ་མི་རིགས་ཏེ། རྒྱུ་ཉིད་མ་ཡིན་པར་ཐལ་བའི་ཕྱིར་རོ། །

[Block 2347]
གལ་ཏེ་སྔགས་ཀྱི་སྦྱོར་བ་ཡན་འགར༌[^1624]བ་ལས་འདོད་པ་གྲུབ་པ་མ་ཡིན་ཏེ། དེ་ནི་ཆོ་ག་ལ་ལྟོས་པ་ཉིད་ཀྱི་ཕྱིར་རོ་ཞེ་ན། ལྟོས་པ་ཡིན་ན་དོན་མེད་འགྱུར། །གལ་ཏེ་སྔགས་ཀྱི་ཆོ་ག་ལས་སམ། གཞན་ལས་རང་བཞིན་ཕུལ་དུ་བྱུང་བ་འགའ་ཞིག་ཐོབ་པར་འགྱུར་ན་དེ་ལ་དེའི་ནུས་པ་ལ་ལྟོས་པར་འགྱུར་ཏེ། རྟག་པ་ལ་དེ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2348]
དེ་བས་ན་ནུས་པ་མེད་པ་འདི་ལ་ཅི་ཕྱིར་ལྟོས་པར་འགྱུར། དེ་ལྟར་ན་ལྟོས་པ་མེད་པ་རྟག་ཏུ་བྱེད་པའམ། ཅུང་ཞིག་ཀྱང་བྱེད་པར་མི་འགྱུར་ཏེ།

[Block 2349 [VERSE]]
ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །
གལ་ཏེ་དངོས་ནུས་དེ་འདྲ་ན། །
དེ་དག་ཀུན་གྱི་སྒྲུབ་བྱེད་འགྱུར། །
ལེགས་བྱས་མིན་ནི་བྱེད་པ་པོའི། །
ཁྱད་པར་ལ་ནི་ལྟོས་མི་རུང་། །

[Block 2350]
གལ་ཏེ་དངོས་པོའི་ནུས་པ་ཉིད་ཀྱི་སྔགས་རྣམས་ཀྱིས་གྲུབ་པ་སྟེར་བར་འགྱུར་ན། དེ་དག་གིས་མཆོད་སྦྱིན་བྱེད་པའམ། གཞན་འགའ་ཞིག་ཀྱང་སྤང་བར༌[^1625]མི་འགྱུར་རོ། །
--- END BLOCKS ---
