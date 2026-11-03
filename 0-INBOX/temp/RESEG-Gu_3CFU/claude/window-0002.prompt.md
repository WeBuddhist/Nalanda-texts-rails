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
[^42]

[Block 72]
དེ་ནི་ད་ལྟར་བྱུང་བའི་ཆོ་ག་བརྗོད་པར་བྱ་སྟེ། རབ་ཏུ་འབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་དེའི་ཕྱིར་དགེ་སློང་འགའ་ཞིག་ལ་མཁན་པོ་ཉིད་དུ་གནས་པ་ལའོ་ཞེས་བྱ་བ་སྟེ། དགེ་སློང་འགའ་ཞིག་ལ་ཞེས་བྱ་བ་ནི་གདོན་མི་ཟ་བར་འགའ་ཞིག་ལ་བརྟེན་ནས་རབ་ཏུ་འབྱུང་བ་ཉིད་དེ་ལ༌[^43]བསྙེན་པར་རྫོགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་རབ་ཏུ་བསྟན་པའི་དོན་དུ་འགའ་ཞིག་ཅེས་བྱ་བའི་ཚིག་གོ། །ཇི་ལྟར་བརྟེན་ནས་ཤེ༌[^44]ན། སྨྲས་པ། མཁན་པོ་ཉིད་དུའོ། །ཅིའི་དོན་དུ་བརྟེན་པ་ལ་ཞེས་བྱ་ཞེ་ན། སྨྲས་པ། དེའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ། རབ་ཏུ་འབྱུང་བ༌[^45]ཉིད་དང་བསྙེན་པར་རྫོགས་པ་ལ་ལྟོས་པ༌[^46]ལའོ། །

[Block 73]
འདིའི་རྒྱུ་མཚན་གྱི་བདུན་པ་སྟེ། འདི་རྣམས་ལ་རབ་ཏུ་འབྱུང་བ༌[^47]ཉིད་དང་བསྙེན་པར་རྫོགས་པའི་རྒྱུ་མཚན་གྱིས༌[^48]མཁན་པོ་ཉིད་ཀྱིས་དགེ་སློང་འགའ་ཞིག་ལ་བརྟེན་པ་ལས༌[^49]རབ་ཏུ་འབྱུང་བ༌[^50]ཉིད་དང་བསྙེན་པར་རྫོགས་པ་དག་ཏུ༌[^51]འགྱུར་གྱི། ཇི་ལྟར་སྔོན་གྱི་ཆོ་ག་ལྟར་འགའ་ཞིག་ལ་མ་བརྟེན་པ་ཉིད་ཀྱིས་ནི་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 74]
འདིར༌[^52]སླར་རབ་ཏུ་བྱུང་བ་ཉིད་ནི་གང་ཞིག་དེ་ལ་འོས་པའི་ཚུལ་ཁྲིམས་དགེ་ཚུལ་གྱི༌[^53]སྡོམ་པ་དེས་རྗེས་སུ་ཆགས་པར་རིག་པར་བྱའོ། །

[Block 75]
རབ་ཏུ་འབྱུང་བ༌[^54]ཉིད་དང་དགེ་ཚུལ་གྱི་སྡོམ་པ་དག་གཉིས་པོ་འདི་ཡང་བརྟེན་པ་ལའོ། །

[Block 76]
སླར་འདིར་ཁྱད་པར་ཡིན་ཏེ། མཁན་པོ་ཉིད་ལས་རབ་ཏུ་བྱུང་བ་སྟེ་སྡོམ་པ་ནི་གཞན་ལས་ཞེས་བྱའོ། །

[Block 77]
རྟེན་ལ་བརྟེན་པ་ཡོངས་སུ་འཛིན་པ་ལ་ཆོ་ག་ནི་དང་པོའི་མཁན་པོ་ཉིད་ཀྱིས༌[^55]བར་ཆད་དྲིས་ནས། །ཡོངས་སུ་དག་པ་ལ་སྐབས་དབྱེའོ་ཞེས་བྱ་བ་སྨྲས་ཏེ། རབ་ཏུ་བྱུང་བ་ཉིད་ལ་གང་ཞིག་བར་ཆད་བྱེད་པ་མ་བསད་པ་ལ་སོགས་པ་དེ་ནི་འདིར་བར་ཆད་དུ་མངོན་པར་འདོད་དོ། །

[Block 78]
དེ་བས་ན་རྟེན༌[^56]གང་ཞིག་རབ་ཏུ་འབྱུང་བ༌[^57]ཉིད་ལ་ལྟོས་པའི༌[^58]བར་ཆད་དྲིས་ནས་གལ་ཏེ་འདི་ལ་ཆོས་དེ་རྣམས་ཡོད་པ་མ་ཡིན་ན། [^59]དེའི་ཕྱིར་ཡོངས་སུ་དག་པ་འདི་ལ་དང་པོའི་མཁན་པོ་ཉིད་ཀྱིས་དགེ་ཚུལ་གྱི་མཁན་པོ་ཉིད་ཀྱིས་བདག་གིས་ཁྱོད་རབ་ཏུ་དབྱུང་ངོ་ཞེས་སྐབས་དབྱེ་བ་ནི་བྱ་བའོ། །

[Block 79]
དེ་ལྟར་ན་ཡང་གཞུང་ལས་གང་སུ་དག་ལས་རབ་ཏུ་བྱུང་བ་ལ་ལྟོས་པ་ཉེ་བར་འགྲོ་བར་བྱེད་པ་དེ་དེས་བར་ཆད་ཀྱི་ཆོས་རྣམས་དྲིས་ཏེ་གཟུང་བར༌[^60]བྱ་ཞེས་བྱའོ། །

[Block 80]
སྡོམ་པ་རྣམས་ཀྱི་གོ་རིམས་བསྟན་པར་བྱ་བའི་ཕྱིར། དགེ་བསྙེན་ཉིད་དང་དགེ་ཚུལ་ཉིད་དང་དགེ་སློང་ཉིད་དག་གི༌[^61]སྔ་མ་བསྙེན་པར་མ་རྫོགས་པ་ལ་ཕྱི་མ་མི་བྱའོ་ཞེས་སྨྲས་ཏེ། དགེ་བསྙེན་ཉིད་ལ་སོགས་པ་འདི་རྣམས་ཀྱི༌[^62]སྔ་མ་སྔ་མ་ནི་སྔ་མ་བསྙེན་པར་མ་རྫོགས་པ་ལ་དེའི་བདག་ཉིད་དུ་ཉེ་བར་སོང་བས་ཁས་མ་བླངས་པ་ལ་གང་ཞིག་ཕྱི་མ་ཕྱི་མ་དེ་ནི་བྱ་བ་མ་ཡིན་ཏེ། འདི་ནི་རྣམ་པར་གཞག་པ་བསྟན་པའོ། །

[Block 81]
བར་ཆད་དྲིས་ནས་རབ་ཏུ་བྱུང་བ་གཟུང་བ༌[^63]ལ་ལྟོས་པ་དང་པོ་དགེ་བསྙེན་ཉིད་འཛིན་དུ་གཞུག་གོ། །

[Block 82]
དེ་ནས་དགེ་ཚུལ་ཉིད་དང་། དེ་ནས་དགེ་སློང་ཉིད་འབྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ཤེས་པར་བྱ་བའི་དོན་དུ་སྟེ། འདིའི་དོན་ནི་མ་ཡིན་ཏེ། སྔ་མ་མ་བཟུང་བ་ལ་ཕྱི་མ་སྐྱེ་བ༌[^64]འབྱུང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 83]
དགེ་སློང་གི་སྡོམ་པའི་སྔོན་དུ་སྡོམ་པ་གཞན་སྐྱེ་བ་ལ་ཡང་ཁུངས་ཀྱི་ཚིག་གཙོ་བོ་ཡོད་པ་ཉིད་དེ། དགེ་ཚུལ་གྱི་སྡོམ་པ་ལ་ནི་དགེ་བསྙེན་གྱི་སྡོམ་པ་མེད་པར་སྐྱེ་བ་འབྱུང་བ་ཡིན་ནོ། །

[Block 84]
དགེ་སློང་གི་སྡོམ་པ་ལ་ནི་ཁུངས་ཀྱི་ཚིག་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 85]
སྐྱབས་སུ་འགྲོ་བ་སྔོན་དུ་འགྲོ་བས་སྡོམ་པ་བླང་ངོ་ཞེས༌[^65]བསྟན་པའི་ཕྱིར། སྐྱབས་སུ་འགྲོ་བ་ཁས་བླངས་པའི༌[^66]ཚིག་རྩོམ་པ་དང་། དགེ་བསྙེན་ཉིད་དང་དགེ་ཚུལ་ཉིད་དུ་ཁས་བླངས་པའི་ཚིག་བྱའོ་ཞེས་སྨྲས་ཏེ། འགྲོ་བ་ནི་འགྲོ་བ་སྟེ་སྐྱབས་སུ་འགྲོ་བ་ཁས་ལེན་པའོ། །

[Block 86]
སངས་རྒྱས་ལ་སྐྱབས་སུ་མཆིའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་རྗོད་པར༌[^67]བྱེད་པའི་ཚིག་སྐྱབས་སུ་འགྲོ་བ་ཁས་བླངས༌[^68]པའི་ཚིག་ནི་དེའི་ཚིག་གོ། །

[Block 87]
རྩོམ་པ་ནི་བརྩམས་པའོ། །

[Block 88]
དགེ་བསྙེན་ཉིད་དང་དགེ་ཚུལ་ཉིད་དུ་ཁས་བླངས་པའི་ཚིག་བྱའོ་ཞེས་སྨྲས་ཏེ། དེ༌[^69]སུ་ཞིག་ཅེ་ན། སྒྲུབ་པ་པོའོ། །

[Block 89]
དེ་ནི་འདི་ཡིན་ཏེ། འདི་ལྟར་ལེན་པ་པོས་སྨྲ་བར་བྱ་སྟེ། བཙུན་པ་དགོངས་སུ་གསོལ། བདག་མིང་འདི་ཞེས་བགྱི་བ། སངས་རྒྱས་ལ་སྐྱབས་སུ་མཆིའོ། །

[Block 90]
ཇི་སྲིད་འཚོའི་བར་དུ༌[^70]བཙུན་པས་བདག་དགེ་བསྙེན་དུ་གཟུང་དུ་གསོལ། །བཙུན་པ་དགོངས་སུ་གསོལ། བདག་མིང་འདི་ཞེས་བགྱི་བ་ཇི་སྲིད་འཚོའི་བར་དུ་སངས་རྒྱས་ལ་སྐྱབས་སུ་མཆིའོ། །

[Block 91]
འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ཀྱི་མཆོག་ཆོས༌[^71]ལ་སྐྱབས་སུ་མཆིའོ། །

[Block 92]
ཚོགས་རྣམས་ཀྱི་མཆོག་དགེ་འདུན་ལ་སྐྱབས་སུ་མཆིའོ། །

[Block 93]
ཇི་སྲིད་འཚོའི་བར་དུ་བདག་དགེ་ཚུལ་དུ་སློབ་དཔོན་གྱིས་གཟུང་དུ་གསོལ། འདི་ལྟ་བུར་གྱུར་པ་ཉིད་རྩོམ་པ་ལ༌[^72]ལན་གསུམ་དུ་བརྗོད་པར་བྱའོ། །

[Block 94]
གང་ཁ་ཅིག་དང་པོར་སྐྱབས་སུ་འགྲོ་བ་ལ༌[^73]ལན་གསུམ་དུ་བརྗོད་ནས་དེའི་འོག་ཏུ་བཙུན་པས་བདག་དགེ་བསྙེན་དུ་གཟུང༌[^74]དུ་གསོལ། བདག་དགེ་ཚུལ་དུ༌[^75]སློབ་དཔོན་གྱིས་གཟུང་དུ་གསོལ་ཞེས་བྱ་བ་བརྗོད་པ་འདིས་ནི་མི༌[^76]རིགས་པར་བརྗོད་པར་བྱའོ། །

[Block 95]
གང་གི་ཕྱིར་སྡོམ་པ་ཡང་དག་པར་བླང་བའི་ཚིག་འདི་དག་འདི་ལྟར་ཡོད་པ་ལ་སྐྱབས་སུ་འགྲོ་བའི་ཚིག་ཡན་ལག་གི་ངོ་བོ་སོ་སོར་གྱུར་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 96]
གཞན་ཡང་གང་གི༌[^77]སྔར་ཉིད་དུ་སྐྱབས་སུ་འགྲོ་བ་ཙམ་ཁས་བླངས་པ་དེ་ལ་སྡོམ་པ་ལེན་པའི་དུས་སུ༌[^78]སྐྱབས་སུ་འགྲོ་བ་མི་བརྗོད་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 97]
འདི་ནི་ཅི་ནས་ཀྱང་མྱ་ངན་ལས་འདའ་བའི༌[^79]བསམ་པ་རབ་ཏུ་སྐྱེད་པའི༌[^80]དོན་དུ་དུས་སུ་འདི་ལ་བརྗོད་པར་བྱ་བ༌[^81]སྟེ། གང་གི་ཕྱིར་འདི་ལྟར་སྡོམ་པ་ཡང་དག་པར་བླངས་པའི་ཚིག་དག་གིས་འདི་ནི་ཡན་ལག་ཏུ་གྱུར་པ་ཡིན་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 98]
མྱ་ངན་ལས་འདས་པའི་བསམ་པ་བརྟེན་པོ༌[^82]མེད་པར་སྡོམ་པ་བླང་བ༌[^83]ནི་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་མྱ་ངན་ལས་འདས་པ་ལ་རྗེས་སུ་མཐུན་པ་ནི་སྡོམ་པ་ཡིན་ནོ། །

[Block 99]
འོ་ན་བསྙེན་པར་རྫོགས་པ་ལ་སྐྱབས་སུ་འགྲོ་བའི་ཚིག་མེད་པར་ཇི་ལྟར་སྐྱེ་བ་ཡིན་ཞེ་ན། འདིས་ནི་སྐྱོན་དུ་མི་འགྱུར་ཏེ། བསྙེན་པར་རྫོགས་པའི་སྒྲ་ཉིད་ལས་ནི་དེའི་དོན་བསྒྲུབ་པའི༌[^84]ཕྱིར་དང་། བྱ་བ་མ་ཡིན་པ་ཐམས་ཅད་ལྡོག་པའི་མཚན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 100]
གང་གི་ཕྱིར་རྣམ་པ་ཐམས་ཅད་དུ་མྱ་ངན་ལས་འདས་པར་ཁས་ལེན་པ༌[^85]ནི་བསྙེན་པར་རྫོགས་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་བསྙེན་པར་རྫོགས་པ་ལ་གནས་པ་མྱ་ངན་ལས་འདས་པ་ལ་རྗེས་སུ་མཐུན་པར་རྣམ་པར་གནས་པར་འགྱུར་རོ། །

[Block 101]
བྱའོ་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱི་ཕྱིར་ཚིག་ནི་སྒྲུབ་པ་པོས་འདི་བྱའོ་ཞེས་བྱ་བ་འདིས་ཡང་དག་པར་བསྟན་པའི་དོན་དུའོ། །

[Block 102]
གང་ཞིག་འདིར་གཞན་གྱིས་བརྗོད་པ་དེ་ནི་སློབ་པར་བྱེད་པ་ཞེས་བྱ་བར་ཤེས་པར༌[^86]བྱའི་སྦྱིན་པ་དང་ལེན་པ་ནི་མ་ཡིན་ནོ། །

[Block 103]
བསྙེན་གནས་ལ་ཡང་སྒྲུབ་པ་པོ་ཉིད་ཀྱིས་འདི་བྱ་ཞེས་བྱ་བ་ཤེས་པར་བྱའོ། །

[Block 104]
གང་ཞིག་དེ་སྦྱིན་པ་དང་ལེན་པའི་ཆོས་དེར་ཞེས་བྱ་བ་ནི་ཁ་ཅིག་སྨྲས་ཏེ།[^87] བཟླས་པ་ཉིད་ཀྱི་ཕྱིར་དེ་རྣམས་ལ་འདི་འཁྲུལ་པ་ཞེས་ཤེས་པར་བྱ་སྟེ་ཡང་དག་པར་བླངས་པ་ལ་མཚུངས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 105]
དེའི་འོག་ཏུ་བསླབ་པ་བརྗོད་པ་ཁས་བླངས་པའི༌[^88]ཚུལ་གྱིས་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ཞེས་བྱ་བ་ནི་དགེ་བསྙེན་ཉིད་དང་། དགེ་ཚུལ་ཉིད་དུ་ཁས་བླངས་པའི་ཚིག་གི༌[^89]རྗེས་ལ་དགེ་བསྙེན་དང་དགེ་ཚུལ་གྱིས་བསླབ་པ་དེས་བསླབ་པའི༌[^90]ཚིག་རྣམས་ལ་ཇི་ལྟར་རིགས་པས༌[^91]བརྗོད་པ་སྟེ། ཐོག་མར་ལྔ་རྣམས་ལའོ། །

[Block 106]
ཕྱི་མ་ནི་བཅུ་རྣམས་ལའོ། །

[Block 107]
རྣམ་པ་གང་གིས་ཤེས༌[^92]ཤེ་ན། ཁས་བླངས་པའི་ཚུལ་གྱིས་ཏེ། འདི་དང་འདི་ལས་བཟློག་པར་བགྱིད་ཅེས་བྱ་བ་ཡིན་གྱི། འདི་དང་འདི་ཁྱེད་ཀྱིས་བྱིན་པ་དེ་ནི་བསྲུང་བར་བགྱི་ཞེས་བྱ་བ་དེ་མ་ཡིན་ནོ། །

[Block 108]
རང་གིས་དགེ་བསྙེན་ཉིད་དུ་ཉེ་བར་བསྒྲུབས་ནས་དགེ་འདུན་ལ་ཞུ་བའི་དགེ་སློང་ལ་གཏད་པར་བྱའོ་ཞེས་བྱ་བ་སྟེ། རང་གིས་ཞེས་བྱ་བ་ནི་སྐབས་འདི་ཉིད་ཀྱི་ཕྱིར་མཁན་པོས་སོ། །

[Block 109]
གང་གི་ཕྱིར་དེ་ནི་རབ་ཏུ་འབྱུང་བ་ལ་སྐབས་བྱས་པའོ། །

[Block 110]
དེ་རང་ཉིད་ཀྱིས་དགེ་བསྙེན་དུ་ཉེ་བར་བསྒྲུབས་ནས་ནི་དགེ་བསྙེན་གྱི་སྡོམ་པ་བྱིན་ནས་སོ། །
--- END BLOCKS ---
