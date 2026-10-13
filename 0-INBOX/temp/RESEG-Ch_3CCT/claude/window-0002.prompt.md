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
དེ་ལྟར་ཡང་གསུངས་པ།

[Block 72 [VERSE]]
བླ་མ་ཡི་ནི་ཐོད་རློན་ལ། །
རྣམ་ཤེས་ལྔ་ནི་སངས་རྒྱས་ཏེ། །
ཀླད་པ་བྱང་ཆུབ་སེམས་ཀྱི་ཆུ། །
དབང་པོ་ལྔ་དང་རྟེན་ལྔ་ནི། །

[Block 73 [VERSE]]
གང་དུ་སྨན་དང་འབྲུ༌[^25]ཞེས་བཤད། །
ཀླད་པའི་སྤྲིས་མ་རས་ཀྱིས༌[^26]དཀྲིས། །
སྐྲ་ནི་བུམ་པའི་ཁ་རྒྱན་ནོ། །
དེ་ཡི་ཁ་ནས་ཆུ་བྱུང་བ། །

[Block 74 [VERSE]]
ཡེ་ཤེས་བདུད་རྩི་དྲི་མ་མེད། །
ལུས་ཀྱི་སྡིག་པ་དག་པར་བྱེད། །
ཅེས་གསུངས་པ་དང་གཞན་ཡང་། །
ཤེས་རབ་ལུས་ཀྱི་བུམ་པ་ནི། །

[Block 75 [VERSE]]
བྱང་ཆུབ་སེམས་ཀྱི་ཆུས་བཀང་ནས། །
གསང་བའི་པདྨར་དབབ་བྱས་ཏེ། །
ཐབས་ཀྱི་རྡོ་རྗེ་དག་པར་བྱེད། །

[Block 76]
ཅེས་འབྱུང་བ་ལྟ་བུའོ། །

[Block 77]
དེའི་རྣམ་གྲངས་བཤད་པ།

[Block 78 [VERSE]]
ཕྱི་དང་བུམ་པ་རིག་པའི་དབང་། །
ཐུན་མོང་དག་ནི་རྣམ་གྲངས་སོ། །

[Block 79]
ཞེས་པ་ནི་ཕྱིའི་དབང་དང་ཐུན་མོང་གི་དབང་དང་། བུམ་པའི་དབང་དང་། རིག་པའི་དབང་དང་། ཐུན་མོང་གི་ནུས་པ་ནི་རྣམ་གྲངས་ཏེ། བསྟན་དུ་ཡོད་པ་ཉིད་དང་། ཀུན་ལ་བྱ་བ་ཉིད་དང་། འཁྲུ་བར་བྱེད་པ་ཉིད་དང་། །སྐལ་བར་དབང་བ༌[^27]ཉིད་དང་། ཐུན་མོང་གི་དངོས་གྲུབ་འགྲུབ་པ་ཉིད་ཀྱི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 80]
དེའང་ཆོས་དུ་དང་ལྡན་པ་ཡིན་ཞེ་ན།

[Block 81 [VERSE]]
སྤྱི་བོར་བསྐུར༌[^28]དང་ལུས་འཁྲུ༌[^29]དང་། །
ཆུ་ཡིས་འཁྲུ་བར་བྱེད་པ་དང་། །
གཞན་དང་ཐུན་མོང་གྲུབ་པ་དང་། །
ཀུན་ལ་བྱ་བས་དེ་སྐད་དོ། །

[Block 82]
བུམ་པའི་དབང་ནི་དང་པོ་སྤྱི་བོར་བསྐུར་བ་དང་། །དེ་ནས་ལུས་ཀྱི་དྲི་མ་འཁྲུ་བ་དང་། ཕལ་ཆེར་ཆུས་འཁྲུ་བ་དང་ཐུན་མོང་གི་དངོས་གྲུབ་འགྲུབ་པར༌[^30]བྱེད་པ་དང་། ཚོགས་ལ་སོགས་པ་དང་ཐུན་མོང་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 83]
དེ་དག་ལས་གཅིག་གམ་གཉིས་ཀྱིས་ཀྱང་དེ་མ་ཡིན་ནོ། །

[Block 84]
དེ་ཉིད་ནི་གཞན་སེལ་བའང་ཡིན་ཏེ། སྤྱི་བོར༌[^31]འཁྲུ་བ་ལ་སོགས་པས། གཞན་པའི་ཡུལ་དུ་འགྱུར་བ་སེལ། །ཞེས་པ་འཁྲུ་བ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མེད་པའི་ཕྱིར་གསང་བ་ལ་སོགས་པ་ལ་ཐལ་བར་འགྱུར་བས་དེའི་གཉེན་པོར་སྤྱི་བོར་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 85]
དེ་བས་ན་འདི་ནི་སྤྱི་བོའང་ཡིན་ལ་དེར་འཁྲུ་བ་ཡང་ཡིན་པས་ན༌[^32]འདི་ནི་བུམ་པ་ཁོ་ནའོ་ཞེས་བསྙད་དོ། །

[Block 86]
སྤྱི་བོར་འཁྲུ་བའང་ཡིན་ལ་ལུས་ཀྱི་དྲི་མ་འཁྲུ་བའང་ཡིན་པས་འདི་ནི་བུམ་པའི་དབང་ཡིན་པ་ཁོ་ནའོ་ཞེས་བསྙད་དོ། །

[Block 87]
འོ་ན་བུམ་པའི་དབང་གི་རྒྱུ་གང་ཡིན་སྙམ་པ་ལ་དེའི་ཕྱིར། ཏིང་འཛིན༌[^33]ཤེས་རབ་ཁྱད་པར་ཅན། །ཞེས་པ་ཤེས་རབ་ཁྱད་པར་ཅན་དང་། ཏིང་ངེ་འཛིན་ཁྱད་པར་ཅན་གང་ཡིན་པ་དེ་ནི༌[^34]བུམ་པའི་དབང་གི་རྒྱུ་ཡིན་ནོ། །

[Block 88]
དེ་ཉིད་རྒྱུ་ཡིན་པ་ཅིའི་ཕྱིར་ཞེ་ན། གང་ཞིག་མེད་ན་གང་མི་འབྱུང་བ་དེ་ནི་མེད་པའི་ཕྱིར་རྒྱུ་མེད་པ་ཡིན་ལ། གང་ཞིག་ཡོད་ན་གང་འབྱུང་བ་དེ་ནི་དེའི་རྒྱུ་ཡིན་ཏེ། དཔེར་ན་ས་བོན་དང་འབྲས་བུ་ལྟ་བུའོ། །

[Block 89]
ཤེས་རབ་ཀྱིས་ཀྱང་བུམ་པ་ལ་སོགས་པའི་མཚན་ཉིད༌[^35]ཤེས་ནས་ཕྱིས་དེ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་ཏེ་འདི་གཉིས་མེད་ན་བུམ་པའི་དབང་བསྐུར་བ་ནམ་ཡང་ནུས་པ་མ་ཡིན་ནོ། །

[Block 90]
དེ་བས་ན་འདི་ནི་རྒྱུའོ། །

[Block 91]
འོ་ན་བུམ་པའི་དབང་འདིའི་གླེང་གཞིའང་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 92 [VERSE]]
ཤཱཀྱ་སེང་གེ་སྐྱོབ་པ་ལ། །
ཇི་ལྟར་དབང་བསྐུར་གླེང་གཞི་ཡིན། །

[Block 93]
ཞེས་པ་ཤཱཀྱ་ཐུབ་པ་སྐུ་བལྟམས་པའི་དུས་སུ་ཀླུའི་རྒྱལ་པོ་རྣམས་ཀྱིས་དབང་བསྐུར་བ་དང་མངོན་པར་སངས་རྒྱས་པའི་དུས་སུ་སའི་ལྷ་མོས་དབང་བསྐུར་བ་ལ་སོགས་པ་སྔོན་བྱུང་བ་དེ་དག་ནི་བུམ་པའི་དབང་གི་གླེང་གཞིར་བཤད་དོ། །

[Block 94]
གནས་གང་དང་གང་དུ་སྒྲུབ་ཅེ་ན།

[Block 95 [VERSE]]
རི་དང་ཡུལ་ཁམས་དགོན་པ་རུ། །
བུམ་པའི་ཆོ་ག་བྱ་བར་གསུངས། །

[Block 96]
ཞེས་པ་བུམ་པའི་དབང་བསྐུར་བའི་གནས་ཀྱང་བཀྲ་ཤིས་པ་དང་བྱིན་ཆེ་བ་དང་། མི་ལ་སོགས་པས་དབེན་པ་དང་། ཤར་བདལ་བ་འདྲ་བ་དང་། ལྷོ་བྲེས་པ་ལྟ་བུ་དང་། ནུབ་མཐོ་བ་ལྟ་བུ་དང་། བྱང་སྐྱོབ་པ་ལྟ་བུ་དང་། མདུན་ན་མེ་ཏོག་གི་གཅལ་བར༌[^36]ཡོད་པ་ལྟ་བུ་དང་། གཟུགས་དང་སྒྲ་ལ་སོགས་པ་ཡོན་ཏན་ཐམས་ཅད་དང་ལྡན་པ་དང་། ཁྱད་པར་དུ་སློབ་མའི་ལས་དང་རྗེས་སུ་མཐུན་པ་ཁ་དོག་དང་དབྱིབས་དང་ནུས་པ་ཕུན་སུམ་ཚོགས་པ༌[^37]དང་། མཚན་ཉིད་དང་ཚད་ལ་སོགས་པ་དང་ལྡན་པའི་གནས་སོ། །

[Block 97]
གནས་དེར་བུམ་པའི་དབང་བྱ་བ་ཡང༌[^38]དུས་གང་གི་ཚེ་བྱ་སྙམ་པ་ལ།

[Block 98 [VERSE]]
དུས་ནི་དམ་ཆོས་འབྱུང་བ་དང་། །
སློབ་མ་དད་དང་སློབ་དཔོན་གནང་། །
ཐུན་མོང་སྒྲུབ་དང་མཆོག་སྒྲུབ་པའོ། །

[Block 99]
ཞེས་པ་ནི། གང་གི་ཚེ་དམ་པའི་ཆོས་འཆད་པ་དང་ཉན་པའི་དུས་སུ་དབང་མ་བསྐུར་ན་རུང་བར་མི་འགྱུར་བས་དེའི་དུས་དང་། ཡང་ན་སློབ་མ་དད་པ་དང་ལྡན་པ་དམ་ཚིག་དང་ཤེས་རབ་ལ་སོགས་པ་དང་ལྡན་པ་དང་བླ་མ་དམ་པ་རྣམས་ཀྱིས་གནང་བ་དང་། ཐུན་མོང་གི་དངོས་གྲུབ་སྒྲུབ་པའི་དུས་སུའང་དབང་མེད་ན་མན་ངག་མེད་པ་དང་། མཆོག་སྒྲུབ་པའི་དུས་ན་གསང་བ་དང་ཤེས་རབ་ཡེ་ཤེས་ལ་བརྟེན་པ་དེའང་བུམ་པའི་དབང་མ་བསྐུར་ན་མི་འབྱུང་བས་དེའི་ཕྱིར་བུམ་པའི་དབང་གི་དུས་བསྟན་ཏོ། །

[Block 100]
གཞན་ཡང་།

[Block 101 [VERSE]]
ཚོགས་དང་གཏོར་མའི་འཁོར་ལོ་དང་། །
སྦྱིན་སྲེག་སཱཙྪ་བྱེད་པ་དང་། །
ཞི་སོགས་ཆོ་གའི༌[^39]ལས་བྱེད་པ། །
བུམ་པའི་དབང་ནི་བསྐུར་བ་ཡིན། །

[Block 102 [VERSE]]
གསང་བ་ལ་སོགས་དབང་དག་གིས། །
འབྲས་བུ་བསྐྱེད་པར་འགྱུར་བ་ལ། །
འདི་ནི་སྔོན་དུ་འགྲོ་བ་ཡིན། །

[Block 103]
ཞེས་འབྱུང་བ༌[^40]ལྟ་བུའོ། །

[Block 104]
དུས་དེར་སློབ་དཔོན་ཡང་ཇི་ལྟ་བུ་ཞིག་གིས་བསྐུར་ཞེ་ན། དེའི་ཕྱིར།

[Block 105 [VERSE]]
ལྟ་སྤྱོད་དབང་དང་དམ་ཚིག་ལྡན། །
ཉོན་མོངས་ཉེ་བའི་ཉོན་མོངས་མེད། །
གཟུགས་བཟང་རིགས་མཐོ་སྙན་པར་གྲགས། །
དགེ་བའི་ཆོས་ཀྱིས་རྣམ་པར་བརྒྱན། །

[Block 106 [VERSE]]
ས་ནོན་སྤྱོད་དང་ལས་ལ་མཁས། །
ཡོན་ཏན་མཆོག་དང་ལྡན་པའོ། །

[Block 107]
ཞེས་པ་དུས་དེར་སློབ་དཔོན་ལྟ་བ་དང་སྤྱོད་པ་དང་དབང་དང་དམ་ཚིག་དང་ལྡན་པ། ཉོན་མོངས་པ་མེད་པ། ཤིན་ཏུ་ཉོན་མོངས་པ་མེད་པ། གཟུགས་མཆོག་ཏུ་བཟང་བ། རིགས་མཐོ་བ། སྐད་སྙན་པ། སྙན་པར་གྲགས་པ། ཐམས་ཅད་ཀྱིས་བསྟོད་པ། ཡང་དག་པའི་ཚོར་བ་དང་། དྲན་པ་དང་། དད་པ་དང་། ངོ་ཚ་ཤེས་པ་དང་། ཁྲེལ་ཡོད་པ་དང་། མ་ཆགས་པ་དང་། ཞེ་སྡང་མེད་པ་དང་། གཏི་མུག་མེད་པ་དང་། རྣམ་པར་མི་འཚེ་བ་དང་། ཤིན་ཏུ་སྦྱངས་པ་དང་། བག་ཡོད་པ་དང་། བརྩོན་འགྲུས་ལ་སོགས་པ་དང་ལྡན་པ་དང་། མོས་པའི་ས་དང་། དྲོད་དང་། རྩེ་མོ་དང་། བཟོད་པ་དང་། ཆོས་ཀྱི་མཆོག་བཅུ་གཉིས་ལ་གནས་པ་དང་རབ་ཏུ་དགའ་བ་དང་། དྲི་མ་མེད་པ་དང་། འོད་འཕྲོ་བ་དང་། འོད་བྱེད་པ་ནས། ཀུན་ཏུ་འོད་ཀྱི་བར་ལ་གནས་པ། བརྡ་དང་བརྡའི་ལན༌[^41]ལ་མཁས་པ། གར་དང་ཕྱག་རྒྱ་དང་། མཆོད་པ་དང་། གཡབ་མོ་དང་། གླུ་དང་གླུའི་ལན་ལ་མཁས་པ། ཞི་བ་དང་། རྒྱས་པ་དང་། དབང་དང་། རེངས་པ་དང་། བཅུག་པ༌[^42]དང་། བསད་པ་དང་། དབྱེ་བ་དང་། གསོ་བ་དང་། དགུག་པ་དང་། སྲེག་པ་དང་། འབར་བ་དང་། སྟེག་པ་དང་། འཁྱུད་པ་དང་། འཇིབ་པ་དང་། དེ་ལ་སོགས་པ་འདོད་ཆགས་ཀྱི་སྤྱོད་པ་དང་། འདོད་ཆགས་དང་བྲལ་བའི་སྤྱོད་པ་ལ་མཁས་པ། རིག་པའི་གནས་དང་གསོ་བའི་ཆོ་ག་ལ་མཁས་པའོ། །

[Block 108]
སློབ་དཔོན་དེས་སློབ་མ་ཅི་འདྲ་བ་ཅིག༌[^43]ལ་བསྐུར་བ༌[^44]མི་ཤེས་ནས་དྲིས་པ་དང་། ལན་དུ། སློབ་མའང་དགེ་བས་བརྒྱན་པ་དང་།

[Block 109 [VERSE]]
གསང་བ་འཇིགས་མེད་ཚོད་རིག་ཅིང་། །
བླ་མའི་ཡིད་དུ་འོང་བ་དང་། །
ཐེག་ཆེན་སྣོད་དུ་རུང་བའོ། །

[Block 110]
ཞེས་པ༌[^45]བུམ་པའི་དབང་བསྐུར་བའི༌[^46]སློབ་མའང་དད་པ་དང་དམ་ཚིག་དང་མོས་པ་དང་དྲན་པ་ལ་སོགས་པས་བརྒྱན་པ་གསང་བ་ལ་འཇིགས་པ་མེད་ཅིང་མཆོག་ཏུ་དེ་ལ་དད་པ་དང་། སྦྱོར་བ་ལ་སོགས་པ༌[^47]ཚོད་རིག་པ། བླ་མ་ལ་ཚུལ་མ་ཡིན་པའི་སྤྱོད་པ་མི་བྱེད་པ་ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་ཡིན་པ། གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་དུ་དབང་བསྐུར་བའི་སྐལ་བ་དང་ལྡན་པ་སྟེ། མཚན་ཉིད་མདོར་བསྡུས་པ་འདི་རྣམས་དང་ལྡན་པ་ལ་སློབ་དཔོན་གྱིས་དབང་བསྐུར་བར་གསུངས་སོ། །
--- END BLOCKS ---
