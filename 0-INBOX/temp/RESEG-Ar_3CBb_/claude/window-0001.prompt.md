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
[Block 36]
ཕྱོགས་ཕྱི་མ་ལྟར་ན་ནི་རང་གི་ཚིག་གིས་གནོད་པའི་ཕྱིར་རོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ཚིག་གི་བླང་དོར་མེད་པའི་བྱང་ཆུབ་སྒྲུབ་པའམ། བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱིས་འགྲུབ་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 37]
ཐམས་ཅད་གསང་བ་མཆོག་ལ་གནས། །ཞེས་བྱ་བ༌[^21]དང་། རང་གི་ལམ་ལ་གནས་ཞེས་པ་ཡང་གཅིག་གིས་གཅིག་སྤངས་པའི་ཕྱིར་རོ། །

[Block 38]
དེ་བས་ན་འདི་ནི་བླང་བར་བྱ་བ་ཉིད་དོ་ཞེ་ན་མ་ཡིན་ཏེ། ས་ལ་གནས་པ་རྣམས་ནི་ཐམས་ཅད་ཀྱང་བསྐྱེད་པའི་རིམ་པ་ཉམས་སུ་ལེན་པའི་ཕྱིར་དང་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་ཆེན་པོར་ལུང་བསྟན་པའི་ཕྱིར་རོ། །

[Block 39]
དེ་ལྟ་ན་ནི་ཐེག་པའི་བྱེ་བྲག་མེད་པར་འགྱུར་རོ་ཞེ་ན་མ་ཡིན་ཏེ་གཉིས་པ༌[^22]ཡོད་པའི་ཕྱིར་རོ། །

[Block 40]
གཉིས་ཞེས་བྱ་བ་འདི་ཡང་གསུམ་དང་གཉིས་ཀྱི་བྱེ་བྲག་གིས་ཡིན་ནོ། །

[Block 41]
ཐེག་པ་ཆེན་པོ་མདོ་སྡེའི་རྗེས་སུ་ཞུགས་པ་རྣམས་ནི་དོན་དམ་པ་ཆོས་ཉིད་མངོན་དུ་གྱུར་ནས་སྣང་བ་སྒྱུ་མ་ཙམ་དང་། རྩོལ་བ་དང་བཅས་པ་ལྷ་དང་ལྷ་མོའི་དཀྱིལ་འཁོར་དུ་བསལ༌[^23]བའོ། །

[Block 42]
གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་ལ་གནས་པ་རྣམས་ནི་དོན་དམ་པའི་བདེན་པ་དང་། ཡང་དག་པའི་ཀུན་རྫོབ་འབའ་ཞིག་ལ་ཉེ་བར་ལོངས་སྤྱོད་པའི་ཕྱིར་རོ། །

[Block 43]
དངོས་པོར་སྣང་བ་སྒྱུ་མ་ཙམ་འདི་ཅི་ཡང་དག་པའི་ཀུན་རྫོབ་པ་འམ། ལོག་པའི་ཀུན་རྫོབ་ཅེས་རྟོག་གྲང་ན། རེ་ཞིག་ཡང་དག་པའི་ཀུན་རྫོབ་ནི་མ་ཡིན་ཏེ། ཟླས་གསལ་བའི་ཕྱིར་རོ། །

[Block 44]
ལོག་པའི་ཀུན་རྫོབ་པ་ནི་མ་ཡིན་ཏེ། ཐམས་ཅད་ལས་མཐུན་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 45]
དངོས་པོ་ལྷའི་དཀྱིལ་འཁོར་དུ་སྣང་བ་ཞེས་བྱ་བ་འདི་ཡང་ལོག་པའི་ཀུན་རྫོབ་ནི་མ་ཡིན་ཏེ་ཁས་མ་བླངས་པའི་ཕྱིར་རོ། །

[Block 46]
ཡང་དག་པའི་ཀུན་རྫོབ་ཀྱང་མ་ཡིན་ཏེ། ཐམས་ཅད་ལ་མཐུན་པར་སྣང་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 47]
དེ་བས་འདི༌[^24]བླང་བར་བྱ་བ་མ༌[^25]ཡིན་ནོ་ཞེ་ན་མ་ཡིན་ཏེ། དངོས་པོར་སྣང་བ་སྒྱུ་མ་ཙམ་འདི༌[^26]དམན་པ་ལ་ཡང་དག་པའི་ཀུན་རྫོབ་ཏུ་སྣང་ན་ནི་མི་འདོད་པ་མེད་དོ་ཐམས་ཅད་ལ་ཡང་དག་པའི་ཀུན་རྫོབ་ཏུ་སྣང་ཞེས་བྱ་བའི་ངེས་པ་ཅི་ཞིག་ཡོད། ལོག་པའི་ཀུན་རྫོབ་ཅེས་བྱ་བ་ནི་འཁྲུལ་པ་ཉིད་དོ། །

[Block 48]
འདི་ལྟར་འཁྲུལ་པ་ཞེས་བྱ་བ་ཡང་། རྟོག་པ་དང་དབང་པོ་མེད་པ་ནི་ཡང་དག་པར་ཡང་སྣང་ངོ་། །དངོས་པོ་ལྷའི་སར༌[^27]སྣང་བ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། མ་འཁྲུལ་པའི་དངོས་པོ༌[^28]ཡོད་པའི་ཕྱིར་དང་། རྟོག་པའི༌[^29]དུས་ན་དེར་སྣང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 49]
གང་གིས་གང་ལ་གནས་པ་དེ་ཉིད་དོན་ལ་མི་སླུ་བར༌[^30]བྱེད་པ་ནི་ཡང་དག་པའི་ཀུན་རྫོབ་སྟེ། དཔེར་ན་དུ་བ་ལས་མེ་དཔོག་པ་བཞིན་ནོ། །

[Block 50]
ལོག་པའི་ཀུན་རྫོབ་ནི་རྟོག་པའི༌[^31]དུས་ན་མི་གནས་པའི་ཕྱིར་དོན་ལ་སླུ་བར༌[^32]བྱེད་པ་སྟེ་ཐག་པ་ལ་སྦྲུལ་བཞིན་ནོ། །

[Block 51]
བསྐྱེད་པའི་རིམ་པ་འདི་ཡང་ཕྲད་པར་བྱེད་པའི་ཕྱིར་དང་། མི་སླུ་བར༌[^33]བྱེད་པའི་ཕྱིར་ཡང་དག་པའི་ཀུན་རྫོབ་ཏུ་འགྱུར་རོ་འཁྲུལ་པའི་ཤེས་པ་དང་། མ་འཁྲུལ་པའི་ཤེས་པ་ནི་སླུ་བར་བྱེད་པ་དང་མི་བྱེད་པས་གཅིག་གིས་གཅིག་སྤངས་པའི་ཕྱིར་འགལ་བར་གནས་པའོ། །

[Block 52]
དེ་བས་ན་མདོ་སྡེའི་རྗེས་སུ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་དོན་དམ་པའི་བདེན་པ་དང་། ཡང་དག་པའི་ཀུན་རྫོབ་དང་ལོག་པའི་ཀུན་རྫོབ་གསུམ་ལ་ཉེ་བར་གནས་པའོ། །

[Block 53]
སྔགས་ཀྱི་སྒོར་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི། དོན་དམ་པའི་བདེན་པ་དང་། ཡང་དག་པའི་ཀུན་རྫོབ་འབའ་ཞིག་ལ་ཉེ་བར་སྤྱོད་པའི་ཕྱིར། དེ་བས་ན་ཐེག་པ་གཉིས་སུ་ཡང་འགྱུར་རོ།[^34] །དུས་ཀྱིས་གསལ་བ་ཡང་མ་ཡིན་ཏེ། སློབ་པ་དང་མི་སློབ་པའི་བྱེ་བྲག་གིས་ཡིན་ནོ། །

[Block 54]
རང་གི༌[^35]ཚིག་གིས་གསལ་བ་ཡང་མ་ཡིན་ཏེ། གཉིས་ཉིད་ཡོད་པའི་ཕྱིར་རོ། །

[Block 55]
དེ་བས་ན་འདི་ནི་བླང་བར་བྱ་བ་ཉིད་དོ། །

[Block 56]
དགོས་པ་མེད་པ་ཡང་མ་ཡིན་ཏེ། སེམས་ཅན་འདོད་ཆགས་ཅན་ལ་སོགས་པ་འདུལ་བར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 57]
སེམས་ཅན་འདོད་ཆགས་ཅན་རྣམས་ནི་འདོད་ཆགས་ཆེན་པོའི་ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་འདོད་ཆགས་ཀྱི་སྒོ་ནས་ཆོས་སྟོན་ཏོ། །

[Block 58]
སེམས་ཅན་ཞེ་སྡང་ཅན་རྣམས་ནི་ཞེ་སྡང་ཆེན་པོའི་ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་ཞེ་སྡང་གི་སྒོ་ནས་ཆོས་སྟོན་ཏོ། །

[Block 59]
སེམས་ཅན་གཏི་མུག་ཅན་རྣམས་ནི་གཏི་མུག་ཆེན་པོའི་ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་གཏི་མུག་ཆེན་པོའི་སྒོ་ནས་ཆོས་སྟོན་ཏོ། །

[Block 60]
སེམས་ཅན་ང་རྒྱལ་ཅན་རྣམས་ནི་ང་རྒྱལ་ཆེན་པོའི་ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས༌[^36]ང་རྒྱལ་གྱི་སྒོ་ནས་ཆོས་སྟོན་ཏོ། །

[Block 61]
སེམས་ཅན་ཕྲག་དོག་ཅན་རྣམས་ནི་ཕྲག་དོག་ཆེན་པོའི་ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་ཕྲག་དོག་གི་སྒོ་ནས་ཆོས་སྟོན་ཏོ། །

[Block 62]
དེ་ལ་སོགས་པ་རྨད་དུ་བྱུང་བའི་སྤྱོད་པ་ཆེན་པོས་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་བྱེད་པའི་ཕྱིར་དགོས་པ་ཆེན་པོ་དང་ལྡན་པས་རྒྱུད་ཆེན་པོའོ། །

[Block 63]
དེ་ལྟ་བུའི་རྨད་དུ་བྱུང་བའི་རྒྱུད་འདི་ནི་སྤྱོད་པ་ཆེན་པོ་དང་། དུས་ཆེན་པོ་ལ་སོགས་པ་དང་ལྡན་པའི་ཕྱིར་རྒྱུད་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 64]
འདིའི་བརྗོད་པར་བྱ་བ་ནི་གང་དགོས་པ་ནི་གང༌[^37]དགོས་པའི་དགོས་པ་ནི་གང་། འབྲེལ་པ་ནི་གང་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་ལམ་འབྲས་བུ་དང་བཅས་པ་ནི་འདི་ནི་བརྗོད་པར་བྱ་བའོ། །

[Block 65]
ལམ་འབྲས་བུ་དང་བཅས་པ་ཇི་ལྟ་བུའི་འབྲས་བུ་རྣམ་པར་རྟོག་པ༌[^38]ནི་དགོས་པའོ། །

[Block 66]
རྗོད་པར༌[^39]བྱེད་པ་དང་དགོས་པ་ནི་གང་ལ་གང་ཞིག་རག་ལས་པར་འགྱུར་བ་དེའི་ཕྱིར་རག་ལས་པའི་འབྲེལ་པར་འགྱུར་རོ། །

[Block 67]
བདག་གི་དོན་དང་གཞན་གྱི་དོན་ཕུན་སུམ་ཚོགས་པར་བྱེད་པ་ནི་དགོས་པའི་དགོས་པའོ། །

[Block 68]
ཡང་ན་ལམ་ལ་གནས་པར༌[^40]བྱེད་པ་ནི་དགོས་པ་ཡིན་ལ། དེས་འབྲས་བུ་ཐོབ་པ་ནི་དགོས་པའི་ཕྱིར་ན༌[^41]དགོས་པའོ། །

[Block 69]
ཡང་ན་ཐུན་མོང་དང་མཆོག་གི་དངོས་གྲུབ་དང་བདག་དང་གཞན་གྱི་དོན་རྣམ་པ་གཉིས་པོ་དགོས་པ་དང་དགོས་པའི༌[^42]དགོས་པར་གོ་རིམས༌[^43]བཞིན་དུ་སྦྱར་རོ། །

[Block 70]
བརྗོད་པར་བྱ་བ་དེ་ཉིད་ལ་སོགས་པ་རྒྱས་པར་བསྟན་པའི་ཕྱིར། དཔལ་ལྡན་རྒྱུད་རྒྱལ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དེ་ལ་དཔལ་ནི་དཔལ་ཏེ། དཔལ་རྡོ་རྗེ་འཆང་ཆེན་པོའོ། །

[Block 71]
དཔལ་དེ་དང་ལྡན་པས་ན༌[^44]དཔལ་ལྡན་ཏེ། དེ་བཞིན་གཤེགས་པ་བཙུན་མོའི་ཚོགས་དང་རྣམ་པར་རོལ་པའོ། །

[Block 72]
དེ་ཉིད་ཐབས་ཤེས་རབ་གཉིས་སུ་མེད་པའི་སྙོམས་པར་ཞུགས་པའི་རྒྱུད་དོ། །

[Block 73]
རྒྱུད་དེ་ཉིད་རྒྱལ་པོ་སྟེ་རྣལ་འབྱོར་རྒྱུད་ཀྱི༌[^45]ཤིན་ཏུ་གསལ་བར་རྣམ་ཕྱེ་ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 74]
སེམས་ཅན་ཐམས་ཅད་ཀྱང་དེ་ལྟ་བུའི་ཆོས་དང་ལྡན་པར་འགྱུར་རོ་ཞེ་ན། མཐའ་དྲུག་གི་ནི་འཆིང་བས་བཅིངས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདིར་མཐའ་རྣམ་པ་དྲུག་ནི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་དང་ང་རྒྱལ་དང་། ལྟ་བ་དང་། ཐེ་ཚོམ་དང་། མ་རིག་པ་དང་རྣམ་པ་དྲུག་གོ། །

[Block 75]
འདི་ནི་མཐའ་སྟེ། འཁོར་བའི་གཡང་ས་དང་ཉེ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །
--- END BLOCKS ---
