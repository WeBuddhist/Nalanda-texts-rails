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
ཅི་གང་གི་ཕྱིར་གཉིས་ལ་བརྟེན་ནས། སྐྱེས་པའི༌[^23]རྣམ་པར་ཤེས་པའི་དབང་པོ་ལ་བརྟེན་པའོ་ཞེས་བརྗོད་ཀྱི་ཡུལ་ལ་བརྟེན་པ་མ༌[^24]ཡིན་ཞེ་ན།

[Block 37 [VERSE]]
ཐུན་མོང་མིན་པའི༌[^25]རྒྱུའི་ཕྱིར། །
དེ་ཡི་ཐ་སྙད་དབང་པོ་ལས། །

[Block 38]
ཡུལ་གཟུགས་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 39]
འདི་ལྟར་ཡུལ་ནི་རྒྱུད་གཞན་གྱི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་ཡང་ཐུན་མོང་ཡིན་ནོ། །

[Block 40]
ཐུན་མོང་མ་ཡིན་པ་ལ་ཐ་སྙད་བྱེད་པ་ཡང་མཐོང་སྟེ། དཔེར་ན་རྔའི་སྒྲ་ནས་ཀྱི་མྱུ་གུ་ཞེས་པ་བཞིན་ནོ། །

[Block 41]
དེ་ལྟ་བས་ན་མངོན་སུམ་རྟོག་པ་དང་བྲལ་བར་འཐད་པ་ཡིན་ནོ། །

[Block 42]
ཆོས་མངོན་པ་ལས་ཀྱང་། མིག་གི་རྣམ་པར་ཤེས་པ་དང་ལྡན་པས་སྔོན་པོ་ཤེས་ཀྱི་སྔོན་པོའོ་སྙམ་དུ་ནི་མ་ཡིན་ནོ། །

[Block 43]
དོན་ལ་དོན་དུ་འདུ་ཤེས་ཀྱི་དོན་ལ་ཆོས་སུ་འདུ་ཤེས་པ་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 44]
གལ་ཏེ༌[^26]གཅིག་ཏུ་མི་རྟོག་ན་རྣམ་པར་ཤེས་པ་ལྔ་པོ་དེ་འདུས་པ་ལ་དམིགས་པ་ཇི་ལྟར་ཡིན། གང་ཡང་སྐྱེ་མཆེད་ཀྱི་རང་གི་མཚན་ཉིད་ལ་སོ་སོ་རང་གི་མཚན་ཉིད་ཀྱི་ཡུལ་ཅན་ཡིན་གྱི། རྫས་ཀྱི་རང་གི་མཚན་ཉིད་ལ་ནི་མ་ཡིན་ནོ་ཞེས་ཀྱང་ཇི་ལྟར་གསུངས་ཤེ་ན།

[Block 45 [VERSE]]
དེར་དོན་དུ་མས་བསྐྱེད་པའི་ཕྱིར། །
རང་དོན་སྤྱི་ཡི་སྤྱོད་ཡུལ་ཅན། །

[Block 46]
དེ་རྫས་དུ་མས་བསྐྱེད་པར་བྱ་བའི་ཕྱིར་ན་རང་གི་སྐྱེ་མཆེད་ལ་སྤྱིའི་སྤྱོད་ཡུལ་ཅན་ཞེས་བརྗོད་ཀྱི། ཐ་དད་པ་ལ་ཐ་མི་དད་པར་རྟོགས་པ་ལས་ནི་མ་ཡིན་ནོ། །

[Block 47]
དོན་འདི་ཉིད་སྨྲས་པ།

[Block 48 [VERSE]]
དུ་མའི་ངོ་བོའི་ཆོས་ཅན་ནོ།[^27] །
དབང་པོ་ལས་རྟོགས་སྲིད་མ་ཡིན། །
རང་རང་རིག་བྱ་ཐ་སྙད་ཀྱིས། །
བསྟན་བྱ་མིན་ན་དབང་པོའི་ཡུལ། །

[Block 49]
དེ་ལྟར་ན་རེ་ཞིག་དབང་པོ་ལྔ་ལས་སྐྱེས་པའི་མངོན་སུམ་གྱི་ཤེས་པ་རྟོག་པ་མེད་པ་ཡིན་ཡང་གཞན་གྱི་འདོད་པ་ལ་བརྟེན་ནས་འདིར་ཁྱད་པར་བྱས་པ་སྟེ། དེ་དག་ནི་ཐམས་ཅད་དུ་རྟོག་པ་མེད་པ་འབའ་ཞིག་གོ། །

[Block 50 [HEADING]]
#### ཡིད་ཀྱང་རྟོག་པ་མེད་པ། ^1-3-3-0

[Block 51 [VERSE]]
ཡིད་ཀྱང་དོན་དང་ཆགས་ལ་སོགས། །
རང་རིག་རྟོག་པ་མེད་པ་ཡིན། །

[Block 52]
ཡིད་ཀྱང་ཡུལ་གཟུགས་ལ་སོགས་པ་ལ་དམིགས་ཤིང་ཉམས་སུ་མྱོང་བའི་རྣམ་པས་འཇུག་པ་སྟེ། རྟོག་པ་མེད་པ་འབའ་ཞིག་གོ། །

[Block 53]
འདོད་ཆགས་དང་། ཞེ་སྡང་དང་། གཏི་མུག་དང་། བདེ་བ་དང་སྡུག་བསྔལ་ལ་སོགས་པ་ནི་དབང་པོ་ལ་མི་ལྟོས་པའི༌[^28]ཕྱིར། རང་རིག་པའི་མངོན་སུམ་མོ། །

[Block 54]
དེ་བཞིན་དུ།

[Block 55 [HEADING]]
#### རྣལ་འབྱོར་པ་རྣམས་ཀྱི་མངོན་སུམ། ^1-3-4-0

[Block 56 [VERSE]]
རྣལ་འབྱོར་རྣམས་ཀྱི་བླ་མ་ཡིས། །
བསྟན་དོན་ཐ་དད་ཙམ་ཞིག་མཐོང་། །

[Block 57]
རྣལ་འབྱོར་པ་རྣམས་ཀྱིས་ཀྱང་ལུང་ལས་རྣམ་པར་རྟོག་པ་དང་མ་འདྲེས་པའི་དོན་ཙམ་མཐོང་བ་ནི་མངོན་སུམ་མོ། །

[Block 58 [HEADING]]
#### རྟོག་པའང་རང་རིག། ^1-3-5-0

[Block 59]
རེ་ཞིག་གལ་ཏེ་འདོད་ཆགས་ལ་སོགས་པའི་རང་རིག་པ་མངོན་སུམ་ཡིན་ན་རྟོག་པའི་ཤེས་པ་ཡང་མངོན་སུམ་དུ་འགྱུར་རོ༌[^29]ཞེ་ན། དེ་ནི་བདེན་ཏེ།

[Block 60 [VERSE]]
རྟོག་པའང་རང་རིག་ཉིད་དུ་འདོད། །
དོན་ལ་མ་ཡིན་དེ་རྟོག་ཕྱིར། །

[Block 61]
དེ་ཡུལ་ལ་ནི་འདོད་ཆགས་ལ་སོགས་པ་ཉིད་བཞིན༌[^30]དུ་མངོན་སུམ་མ་ཡིན་ཡང་རང་རིག་གོ་ཞེས་བྱ་བའི་སྐྱོན་ནི་མེད་དོ། །

[Block 62]
དེ་དག་ནི་མངོན་སུམ་མོ། །

[Block 63 [HEADING]]
#### མངོན་སུམ་ལྟར་སྣང་། ^1-3-6-0

[Block 64 [VERSE]]
འཁྲུལ་དང་ཀུན་རྫོབ་ཡིད་ཤེས་དང་། །
རྗེས་དཔག་རྗེས་སུ་དཔག་ལས་བྱུང་། །
དྲན་དང་མངོན་འདོད་ཅེས་བྱ་བ། །
མངོན་སུམ་ལྟར་སྣང་རབ་རིབ་བཅས། །

[Block 65]
རེ་ཞིག་འཁྲུལ་པའི་ཤེས་པ་ནི་སྨིག་རྒྱུ་ལ་སོགས་པ་ལ་ཆུ་ལ་སོགས་པར་རྟོག་པའི་ཕྱིར་མངོན་སུམ་ལྟར་སྣང་བའོ། །

[Block 66]
ཀུན་རྫོབ་ཏུ་ཡོད་པ་ནི་དོན་བཞིན༌[^31]སྒྲོ་འདོགས་པས་ན་དེའི་ངོ་བོར་བརྟགས་ནས་འཇུག་པའི་ཕྱིར་མངོན་སུམ་ལྟར་སྣང་བའོ། །

[Block 67]
རྗེས་སུ་དཔག་པ་དང༌[^32]དེའི་འབྲས་བུ་ལ་སོགས་པའི་ཤེས་པ་ནི་སྔར་ཉམས་སུ་མྱོང་མྱོང་བ་ལ་རྟོག་པའི་ཕྱིར་མངོན་སུམ་མ་ཡིན་ནོ། །

[Block 68]
འདིར་ཡང་།

[Block 69 [HEADING]]
#### ཚད་མའི་འབྲས་བུ། ^1-3-7-0

[Block 70 [VERSE]]
བྱ་དང་བཅས་པར་རྟོགས་པའི་ཕྱིར། །
ཚད་མའི་འབྲས་བུ་ཉིད་དུ་འདོད། །

[Block 71]
འདི་ལ་ཕྱི་རོལ་པ་རྣམས་ཀྱི་བཞིན་དུ་ཚད་མ་ལས་འབྲས་བུ་དོན་གཞན་དུ་འགྱུར་བ་ནི་མེད་ཀྱི། འབྲས་བུར་གྱུར་པའི་ཤེས་པ་དེ་ཉིད་ཡུལ་གྱི་རྣམ་པ་ཅན་དུ་སྐྱེས་པ་དང་བྱ་བ་དང་བཅས་པར་རྟོགས་པ་དེ་ཉེ་བར་བླངས་ནས། ཚད་མ་ཉིད་དུ་འདོགས་པ༌[^33]སྟེ། བྱ་བ་མེད་པའང་མ་ཡིན་ནོ། །

[Block 72]
དཔེར་ན་འབྲས་བུ་རྒྱུ་དང་རྗེས་སུ་མཐུན་པར་སྐྱེས་པ་ལ་རྒྱུའི་གཟུགས་འཛིན་ཞེས་བརྗོད་དོ། །

[Block 73]
བྱ་བ་མེད་པར་ཡང་མ་ཡིན་པ་དེ་བཞིན་དུ་འདིར་ཡང་ཡིན་ནོ། །

[Block 74]
རང་རིག་ལ་ཡང་འདིར་འབྲས་བུ། །ཤེས་པ་ནི་སྣང་བ་གཉིས་ལས་སྐྱེས་ཏེ་རང་གི་སྣང་བ་དང་ཡུལ་གྱི་སྣང་བའོ། །

[Block 75]
སྣང་བ་དེ་གཉིས་ལས་གང་རང༌[^34]རིག་པ་དེ་ནི་འབྲས་བུར་འགྱུར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་ཡི་ངོ་བོ་ལས་དོན་ངེས། གང་གི་ཚེ་ཤེས་པ་དོན་གྱི་ཡུལ་དང་བཅས་པའི༌[^35]དེའི་ཚེ། དེ་དང་རྗེས་སུ་མཐུན་པའི་རང་རིག་པ་འདོད་པའམ་མི་འདོད་པའི་དོན་རྟོགས་པར་བྱེད་དོ། །
--- END BLOCKS ---
