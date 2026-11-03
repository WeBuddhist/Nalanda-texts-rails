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
[Block 71]
གང་ལ་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་ལའོ། །

[Block 72]
མེད་ན་དགེ་ཚུལ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མེད་ན་དགེ་ཚུལ་ལ་དེ་བཅོལ་བར་བྱའོ། །

[Block 73]
དེ་ཡང་མེད་ན་ཁྱིམ་བདག་ལའོ་ཞེས་བྱ་བ་ནི་དགེ་ཚུལ་དེ་ཡང་མེད་ན་ཁྱིམ་བདག་ལ་དེ་བཅོལ་བར་བྱའོ། །

[Block 74]
ཐམས་ཅད་མེད་ན་ཕྱོགས་བཞིར་རྣམ་པར་བལྟས་ཏེ་ལྡེ་མིག་སྦས་ནས་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་བཅོལ་བར་བྱ་བ༌[^57]ཐམས་ཅད་མེད་ནའོ། །

[Block 75]
གལ་ཏེ་ལམ་ཁར་དགེ་སློང་མཐོང་ན་ཕྱོགས་དེ་དེ་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་དུ་ལྡེ་མིག་སྦས་པའོ། །

[Block 76]
གལ་ཏེ་འོང་བ་ནི༌[^58]ཁྱིམ་གཞན་དུ་མགྲོན་དུ་བོས་ཤིང་སྒོ་བཅད་པར་གྱུར་ན་རྩིག་དྲུང་ངམ་ཤིང་ལྗོན་པའི་དྲུང་དུ་སྟན་བཞག་སྟེ་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་སྒོ་ལ་ཞེས༌[^59]བྱ་བ་འདི་ལ་བཅད་པར་གྱུར་ན་ཞེས་བྱ་བ་འདི་དང་འབྲེལ་ཏོ། །

[Block 77]
འདིར་རྩིག་དྲུང་ངམ་ཤིང་ལྗོན་པའི་དྲུང་དུ་ཞེས་སྨོས་པ་ནི་ཉི་ཚན་བསྐྱབ་པའི་དཔེ་ཙམ་དུ་ཟད་དོ། །

[Block 78]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་ཞུ་བའི་ཡི་གེ་ཁ་ཅིག་ལས་རྩིག་དྲུང་ངམ་ཤིང་ལྗོན་པའི་དྲུང་ངམ་ཉི་མས་ཆུད་ཟོས་པར་མི་འགྱུར་ན་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 79]
དེར་སྟན་དག་གཡར་པོར་སྦྱིན་ནོ་ཞེས་བྱ་བ་ལ་དེར་ཞེས་བྱ་བ་ནི་ཁྱིམ་གྱི་ནང་དུའོ། །

[Block 80]
རང་གིས་བསྐུར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་གྱི་ནང་ནས་དགེ་སློང་གི་གནས་མལ་ལོ། །

[Block 81]
དེ་ནི་ཁྱིམ་པ་དང་དགེ་ཚུལ་དག་གིའོ་ཞེས་བྱ་བ་ནི་སྟན་བསྐུར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 82]
མེད་ན་བསྐྱལ་བའི་ཕྱིར་ཁྱིམ་པ་ལ་བཅོལ་ཏེ་འདོང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་མེད་ན་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་དང་དགེ་ཚུལ་དག་གོ། །

[Block 83]
འདིར་གཞུང་ནི་དགེ་སློང་ཟན་ཟོས་ནས་སྟན་རང་གི་མཆན་ཁུང་གིས་བླངས་ཏེ་འགྲོ་བ་ན་བྲམ་ཟེ་དང་ཁྱིམ་བདག་དག་ཅི་འཕགས་པ་དག་རོལ་མོ་ལྟར་འདོང་ངམ་ཞེས་ཅོ་འདྲི་བར་བྱེད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རང་གིས་སྟན་བསྐུར་བར་མི་བྱ་བར་ཁྱིམ་པ་དང༌[^60]དགེ་ཚུལ་དག་གིས་བསྐུར་བར་བྱའོ། །

[Block 84]
གལ་ཏེ་ཁྱིམ་པ་དང་དགེ་ཚུལ་དག་མེད་པར་གྱུར་ན་ཁྱིམ་བདག་དེ་ཉིད་ལ་བཅོལ་ཏེ་འདོང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 85]
བདག་ཅག་གིས་བསྐྱལ་ལོ་ཞེས་ཟེར་ན་བཞག་སྟེ་འདོང་བར་བྱའོ། །

[Block 86]
དེ་དག་གིས་མ་བསྐྱལ་ན་གནས་པར་བྱེད་པ་དག་གིས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་ནི་ཁྱིམ་པ་རྣམས་ཀྱིས་སོ། །

[Block 87]
དེ་ལྟར་ཁས་མ་བླངས་ནས་མ་བསྐྱལ་ན་གནས་པར་བྱེད་པ་རྣམས་ཀྱིས་བླང་བར་བྱའོ། །

[Block 88]
མེད་ན་རང་གིས་སོ༌[^61]ཞེས་བྱ་བ་ནི། གནས་པར་བྱེད་པ་དག་ཀྱང་མེད་ན་རང་གིས་བླང་བར་བྱའོ། །

[Block 89]
ཐམས་ཅད་ཀྱིས༌[^62]ན་གཎྜཱི་བརྡུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་དགེ་སློང་ཐམས་ཅད་ཀྱིས་བླང་བར་བྱ་དགོས་པ་ཞིག་ཡོད་ན་ཐམས་ཅད་འདུས་ཏེ་གཎྜཱི་བརྡུངས་ཏེ་བླང་བར་བྱའོ། །

[Block 90]
ཡོན་བདག་གིས་གཙུག་ལག་ཁང་དུ་རང་གི་དོན་དུ་སྟན་དག་གཡར་པོར་བྱེད་ན་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^63]གང་རྣམས་ཀྱིས༌[^64]སྤྱན་འདྲེན་ལ་སྦྱིན་པ་དེ་རྣམས་གལ་ཏེ་གཙུག་ལག་ཁང་དུ་རང་གི་དོན་དུ་གདན་ཆ་དག་གཡར་པོར་བྱེད་ན་དེ་རྣམས་ལ་གཡར་པོ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 91]
དེ་དག་བསྲུང་བའི་ཕྱིར་དགེ་སློང་ཡང་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གདན་རྣམས་ལའོ། །

[Block 92]
དེས་ཕྱོགས་གཅིག་ཏུ་བསྡད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བཞག་པའི་དགེ་སློང་གིས་སོ། །

[Block 93]
རང་གི་ལས་བྱའོ་ཞེས་བྱ་བ་ནི་བསམ་གཏན་དང་ཁ་ཏོན་བྱེད་པའོ། །

[Block 94]
སེམས་གཏད་པ་ལ་ཡང་ངོ༌[^65]ཞེས་བྱ་བ་ནི་གདན་རྣམས་ལ་སེམས་གཏད་པར་བྱེད་ཅིང་གནས་པར་བྱའོ། །

[Block 95]
དོང་ནས་བརྟུལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་སྤྱན་འདྲེན་པར་བྱེད་པ་རྣམས་དོང་ནས་གདན་ཆ་དེ་རྣམས་བརྟུལ་བར་བྱའོ། །

[Block 96]
མ་རུང་བ༌[^66]དག་བྱི་དོར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་གིས་མ་རུང་བ༌[^67]བྱས་པའི་བྱི་དོར་གང་གིས་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཆང་གིས་ན་ཆུ་དག་གིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆང་གི༌[^68]སྙིགས་མས༌[^69]མ་རུང་བར༌[^70]བྱས་པ་རྣམས་ནི་ཆུ་འབའ་ཞིག་གིས་བཀྲུ་ཞིང་བྱི་དོར་བྱའོ། །

[Block 97]
སྣུམ་གྱིས་ན་ཆལ་གྱིས་སོ་ཞེས་བྱ་བ་ནི་སྣུམ་གྱིས་མ་རུང་བར༌[^71]གྱུར་པ་རྣམས་ནི་འདག་པའི་ཆལ་གྱིས་བྱི་དོར་བྱའོ། །

[Block 98]
མི་གཙང་བས་ན་སའམ་ལྕི་སྐམ་མམ་ལྕི་བས་སོ་ཞེས་བྱ་བ་ནི། གདན་ཆ་རྣམས་མི་གཙང་བས་མ་རུང་བར༌[^72]གྱུར་ནས་སའམ་ལྕི་སྐམ་མམ་ལྕི་བ་རྣམས་ཀྱིས་བྱི་དོར་བྱ་བའོ། །

[Block 99]
འདིར་གཞུང་ནི་གཞན་དུ་ས་ཙམ་ལ་འདིར་བཟུང་བ་ཞེས་གསུངས་ཏེ། དེ་ནི་མཚོན་པ་ཙམ་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 100]
དེ་དང་འདི་འགལ་བར་ཤེས་པར་མི་བྱའོ། །

[Block 101]
ཐགས་མ་མ་དག་ན་གཅད་པར༌[^73]བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་གལ་ཏེ་རེ་ཞིག་སྦྱང་བར་ནུས་ན་དེ་ལྟ་ན་ལེགས། གལ་ཏེ་མི་ནུས་ན་འབྲེང་བ༌[^74]བཅད་དེ་དོར་བར་བྱ་ཞིང་འབྲེང་བུ་གསར་པ་རྣམས་ཀྱིས་ཀྱང་སླར་གསོ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 102]
ཁྱིམ་པ་འདུག་འདུག་པའི་སྟན་མ༌[^75]བསྡུས་པ་མཐོང་ན་བསྡུ་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གང་དག་གིས་དེ་དག་མཐོང་བ་ཉིད་ཀྱིས་དེ་དག་བསྡུ་བར་བྱའོ། །

[Block 103]
གལ་ཏེ་རྒས་པ་དང་ན་བ་ཡིན་ན་དགེ་སྐོས་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་མཐོང་བ་པོ་རྒས་པའམ་ན་བ་ཡིན་ན་དགེ་སྐོས་ཀྱིས་བསྡུ་བར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 104]
དེས་སྦྲན་པར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྒན་པོའམ་ནད་པ་མཐོང་བ་པོ་དེས་སྦྲན་པར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 105]
གང་ལ་སྦྲན་པར༌[^76]བྱ་སྙམ་དུ་དོགས་པ་ལ་འདིར་བསྐོས་པ་ལ་ཞེས་བྱ་བ་དོན་གྱིས་དང་དབང་དུ་བྱས་པ་ཤེས་པར་བྱའོ། །

[Block 106]
ཐམས་ཅད་ཀྱི་ནད་པ་བལྟ་བར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^77]དེའི་ཁང་བུའི་གནས་སུ་ཉེ་བར་འགྲོ་བ་ན་གསར་བུའམ་རྒན་པོ་འགའ་ཞིག་གིས་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 107]
ཅི་འགྲེང་སྟེ་བལྟ་བར་བྱ་བ་འམ་ཞེ་ན་མ་ཡིན་ཏེ་དེའི་ཕྱིར་འདུག་སྟེའོ། །

[Block 108]
དེར་སྟན་ཐོགས་ཏེ་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེར་ཞེས་བྱ་བ་ནི་ནད་པ་ལྟ་བ་ལའོ། །

[Block 109]
ནད་པའི་ནད་གཡོག་གིས༌[^78]དེར་སྟན་དག་བཤམ་པར་བྱའོ། །

[Block 110]
མཁན་པོའམ་སློབ་དཔོན་དགེ་བའི་ཕྱོགས་ལ་འགྲོ་ན་གལ་ཏེ་གཞན་གྱིས༌[^79]དགེ་བའི་ཕྱོགས་མི་འཕེལ་ན་ཕྱི་བཞིན་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^80]གལ་ཏེ་མ་ཡིན་ན་གཞན་དུ་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
