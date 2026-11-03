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
འདིས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་སྟོན་པ་ཡིན་ནོ། །

[Block 37]
རང་གི་སྙན་ངག་ཡིན་པས་བདག་གི་སྙན་ངག་གོ། །

[Block 38]
བདག་གི་སྙན་ངག་ཉིད་མེ་ཏོག་ཡིན་པས་བདག་གི་སྙན་ངག་མེ་ཏོག་གོ། །

[Block 39]
མེ་ཏོག་བཞིན་དུ་མེ་ཏོག་གི་མཆོད་པའི་ཡོ་བྱད༌[^19]ཆོས་མཐུན་པ་ཡིན་པའི་ཕྱིར་ཇི་ལྟར་དེ་མེ་ཏོག་ལ་སོགས་པའི་སྙིམ་པ་སྟེ། བདག་གི་སྙན་ངག་མེ་ཏོག་སྙིམ་པའོ། །

[Block 40]
སྙིམ་པ་ནི་ལག་པ་གཉིས་སྦྱར༌[^20]བའོ། །

[Block 41]
ཡང་ན་མེ་ཏོག་གི་སྙིམ་པ་ཡིན་པས་མེ་ཏོག་སྙིམ་པའོ། །

[Block 42]
རང་གི་སྙན་ངག་ཉིད་མེ་ཏོག་སྙིམ་པ་ཡིན་པས་ན་བདག་གི་སྙན་ངག་མེ་ཏོག་སྙིམ་པའོ། །

[Block 43]
དེས་ན་བདག་གི་སྙན་ངག་གི་མེ་ཏོག་སྙིམ་པ་ཞེས་བྱ་བ་འདིས་ནི་མཆོད་པའི་ཡོ་བྱད་ཅུང་ཟད་ཙམ་དུ་བསྟན་ཏེ། མེ་ཏོག་གི་གནས་དག་ལ་སྙན་ངག་ཉེ་བར་བསྟན་པ་ཡིན་ནོ། །

[Block 44]
དེ་ལྟར་ན༌[^21]འདིས་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བཤད་པ་ཡིན་ནོ། །

[Block 45]
གྲགས་པའི་མཚན་མར་གྱུར་པ་འདི་རྣམས་ཀྱིས་ཞེས་བྱ་བ་དང་། འཇིག་རྟེན་དོན་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་གཉིས་ནི་སྙན་ངག་བརྩམས་པའི་དགོས་པ༌[^22]བསྟན་པ་ཡིན་ཏེ། དགོས་པ་དང་དགོས་པ་བྱེད་པ་གཉིས་ཀྱིས་བསྡུས་པའི་དོན་ཏེ། ཚིགས་བཅད༌[^23]འདི་གཉིས་ནི༌[^24]བདག་དང་གཞན་གྱི་དོན་མཐའ་དག་འདི་ལས་འབྱུང་བར་བསྟན་ཏོ། །

[Block 46]
དེ་ལ་གཞན་གྱི་དོན་མཐའ་དག་ལས་བརྩམས༌[^25]ཏེ། གྲགས་པའི་མཚན་མར་གྱུར་པ་ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་བསྟན༌[^26]ཏེ། འདི་རྣམས་ཀྱི༌[^27]ཞེས་བྱ་བ་ནི་སྔར་བཤད་པའི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱིས་ཡོངས་སུ་བཟུང་བ་དེས་ན་གྲགས་པ་ཞེས་བྱ་བར་གྲགས་པར༌[^28]བྱེད་པ་ཡིན་ཏེ་རབ་ཏུ་བསྔགས་པའོ། །

[Block 47]
ཇི་ལྟར་གྲགས་པ་ཡིན་ཞེ་ན་སྨྲས་པ། མངོན་སྣང་མཚན་མར་གྱུར་པ་ཞེས་སྨོས་ཏེ། སེམས་ཅན་རྣམས་ཀྱི་མངོན་པར་སྣང་བའི་མཚན་མར་གྱུར་པ་སྟེ། འདིས་ནི་གནས་ཀྱི་ཁྱད་པར་གྱི༌[^29]སྤྱོད་པའི་ཁྱད་པར་བཤད་པ་ཡིན་ནོ། །

[Block 48]
ཡང་ན་མངོན་པར་སྣང་བ་ཡང་ཡིན་ལ། མཚན་མར་གྱུར་པ༌[^30]ཡིན་པས་མངོན་སྣང་མཚན་མར་གྱུར་པའོ། །

[Block 49]
འདིས་ནི་དེའི་སྤྱོད་པ་དག་གིས་སྐྱེ་བོ་ཀུན་ལ་ཕན་པར་སྟོན་པར་བཤད་དེ་བསྡུས་པའི་དོན་ཏོ། །

[Block 50]
གྲགས་པ་ཞེས་བྱ་བ་ནི་དགེ་ཤིས༌[^31]སོ། །

[Block 51]
འདི་རྣམས་ཀྱིས་ཞེས་བྱ་བ༌[^32]ནི་སྤྱོད་པ་སྟེ་མངོན་སྣང་མཚན་མར་བྱས་པའོ། །

[Block 52]
དེ་གང་གི་ཞེ་ན། སངས་རྒྱས་ཉིད་ཀྱིའོ། །

[Block 53]
མཚན་མར་གྱུར་པ་ནི་རྟགས་སུ་གྱུར་པ་དང་། མཚོན་པར་གྱུར་པའོ། །

[Block 54]
བདེ་བར་གཤེགས་འགྱུར་ལམ་ཞེས་བྱ་བ་ནི་བདེ་བར་གཤེགས་པར་འགྱུར་བ་ཡིན་པས་བདེ་བར་གཤེགས་འགྱུར་རོ། །

[Block 55]
མཛེས་པར་གཤེགས་པས་ན༌[^33]བདེ་བར་གཤེགས་པའོ། །

[Block 56]
དེ་ཁོ་ན་ཉིད་ནི་ཕྱིན་ཅི་མ་ལོག་པའོ། །

[Block 57]
ལམ་རྣམས་ཞེས་བྱ་བ་ནི་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པའོ། །

[Block 58]
གང་ཡིན་ཞེས་བྱ་བ་ནི༌[^34]གང་གི་ཕྱིར་རོ། །

[Block 59]
བསྟན་པ་ནི་བཤད་པ་སྟེ་རབ་ཏུ་སྟོན་པ་ཡིན་ནོ། །

[Block 60]
ཡིད་ལ་དད་པ་མེད་པ་རྣམས་ཀྱང་ཞེས་བྱ་བ་ལ། འདིར་ཡང་ཞེས་བྱ་བ་ནི་དེ་ཡང་དེ་ལྟར་འགྱུར༌[^35]ཞེས་པ་སྟེ། ཀྱང་གི་སྒྲ་ནི་སྲིད་པའི་ཚུལ་ལོ། །

[Block 61]
ཡང་ན་ཡིད་ལ་དད་པ་མེད་པ་རྣམས་ཀྱང་དེ་བཞིན་དུ་འགྱུར་བ་སྟེ་གཞན་དག་གི་ཡང་ངོ་། །འདིར་ཀྱང་གི་སྒྲ་ཡང་སྲིད་པའི་ཚུལ་ཉིད་དོ། །

[Block 62]
ཆོས་དང་ལྡན་པའི་གཏམ་གྱིས་རབ་ཏུ་དགའ་བ་ཞེས་བྱ་བ་ནི་གྲགས་པའི་སྤྱོད་པ་འདི་རྣམས་ཀྱིས་རབ་ཏུ་དགའ་བར་གྱུར་པའི༌[^36]ཕྱིར་རོ། །ཇི་ལྟར་ཞེ་ན། འདིར་ཉན་པ་ཐ་མལ་པ་རྣམས་གང་གི་ཕྱིར་རབ་ཏུ་དགའ་བར་འགྱུར་བ་ཡིན་པས་སོ། །

[Block 63]
དེས་ན་ཡང་སྐྱེ་བོ་ཐ་མལ་པ་ལ་མངོན་པར་བརྟགས་ནས་འབད་དེ༌[^37]བརྩམ་མོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 64]
དེ་ལ་སྐྱེ་བོའི་བྱེ་བྲག་ཀྱང་རྣམ་པ་གསུམ་སྟེ། དད་པ་དང་ལྡན་པ་དང་། དད་པ་ཉམས་པ་དང་། ཐ་མལ་པའོ། །

[Block 65]
སྐྱེ་བོ་དེ་གསུམ་ཐ་མལ་པ་ལ༌[^38]མངོན་པར་བརྟགས་ཤིང་འབད་ནས་བྱའོ་ཞེས་པ༌[^39]ནི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ཏོ། །

[Block 66]
དེ༌[^40]སྐྱེ་བོ་དད་པ་དང་ལྡན་པའི་དབང་དུ་བྱས་ནས། བསྟན་པར་འགྱུར་བ༌[^41]ནི་བདེ་བར་གཤེགས་འགྱུར་ལམ་རྣམས་གང་ཡིན་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 67]
དད་པ་ཉམས་པའི་དབང་དུ་བྱས་པ་ནི་ཡིད་ལ་དད་པ་མེད་པ་རྣམས་ཀྱང་དད་པར་འགྱུར་ཞེས་བྱའོ། །

[Block 68]
ཐ་མལ་པའི་དབང་དུ་བྱས་པ་ནི་ཆོས་དང༌[^42]ལྡན་པའི་གཏམ་གྱིས་རབ་ཏུ༌[^43]དགའ་བར་འགྱུར་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 69]
དེ་ལ་ཆོས་ནི་ཡན་ལག༌[^44]བཅུ་གཉིས་བརྗོད་པའི་རྣམ་པའོ། །

[Block 70]
གཏམ་ཡིན་པས་ན་གཏམ་སྟེ༌[^45]རབ་ཏུ་དགའ་བའོ། །

[Block 71]
རབ་ཏུ་ཞེས་བྱ་བ་ནི་ལྷག་པར་ཞེས་བྱ་བ་དང་། རབ་ཏུ་ཞེས་བྱ་བའི་དབྱེ་བས་སོ། །

[Block 72]
འགྱུར་ཞེས་བྱ་བ་ནི་འོང་བར་འགྱུར་བའོ། །

[Block 73]
འཇིག་རྟེན་གྱི་དོན་ནི་འཇིག་རྟེན་ལ་ཕན་པའི་ཕྱིར་རོ། །

[Block 74]
མངོན་པར་བརྟགས་ཞེས་བྱ་བ་ནི་བལྟས་ནས་བརྩམས་སོ། །ཞེས་བྱ་བའི་ཚིག་གི༌[^46]དོན་ནོ། །

[Block 75]
འབར་ཞེས་བྱ་བ་ནི་ཀུན་ལ་སྦྱར་བར་བྱའོ། །
--- END BLOCKS ---
