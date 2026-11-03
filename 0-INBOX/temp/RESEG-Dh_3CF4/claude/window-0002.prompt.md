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
རབ་ཏུ་ཞེས་བྱ་བ་ནི་ལྷག་པར་ཞེས་བྱ་བ་དང་། རབ་ཏུ་ཞེས་བྱ་བའི་དབྱེ་བས་སོ། །

[Block 72]
འགྱུར་ཞེས་བྱ་བ་ནི་འོང་བར་འགྱུར་བའོ། །

[Block 73]
འཇིག་རྟེན་གྱི་དོན་ནི་འཇིག་རྟེན་ལ་ཕན་པའི་ཕྱིར་རོ། །

[Block 74]
མངོན་པར་བརྟགས་ཞེས་བྱ་བ་ནི་བལྟས་ནས་བརྩམས་སོ། །ཞེས་བྱ་བའི་ཚིག་གི༌[^46]དོན་ནོ། །

[Block 75]
འབར་ཞེས་བྱ་བ་ནི་ཀུན་ལ་སྦྱར་བར་བྱའོ། །

[Block 76]
ཐོས་པ་དང་གཙུག་ལག་དང་རིགས་པ་ནི་ཐོས་པ༌[^47]དང་གཙུག་ལག་རིགས་པ་དག་སྟེ། ཐོས་པ་ནི་ཉན་པའོ། །

[Block 77]
གཙུག་ལག་ནི་སངས་རྒྱས་ཀྱིས་གསུངས༌[^48]པའོ། །

[Block 78]
རིགས་པ༌[^49]ནི་རིགས་པའི༌[^50]བསྟན་བཅོས་སོ། །

[Block 79]
ཡང་ན་རིགས་པ༌[^51]ནི་ཚད་མའོ། །

[Block 80]
མི་འགལ་བ་ནི་སྐྱོན་དང་བྲལ་བའི་ལམ་དག་གིས་སོ། །

[Block 81]
འབད་པ་ནི་མངོན་པར་སྤྲོ་བས་སོ།[^52] །འཇིག་རྟེན་མཆོག་གི་སྤྱོད་པ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ནི་སྐྱེ་དགུའོ། །

[Block 82]
མཆོག་ནི་གཙོ་བོའོ། །

[Block 83]
སྤྱོད་པ་ནི་སྤྱོད་པའོ། །

[Block 84]
དམ་པ་ཞེས་བྱ་བ་ནི་ལྷག་པའོ། །

[Block 85]
ཕྱོགས་ཙམ་ཞེས་བྱ་བ་ནི་ཕྱོགས་གཅིག་གོ། །

[Block 86]
མཉན་པར་རུང་བ་ནི་མཉན་དུ་རུང་བའོ། །ཤེས་པར་འགྱུར་བ་ཡིན་པས་ན་ཤེས་པར་རུང་བ་སྟེ། སྙན་ངག་གོ། །

[Block 87]
རྟོགས་པ་ནི་ཉེ་བར་འདུལ་བའི་དོན་དུའོ། །

[Block 88]
མཉན་པ༌[^53]ནི་རྣ་བའི་དབང་པོས་སོ། །

[Block 89]
རུང་བར་བྱ་བ་ནི་དགའ་བར་བྱ་བའོ།[^54] །རང་དོན་བརྩོན་པས་ཞེས་བྱ་བ་ལ་རང་གི་དོན་ནི་རང་ལ་ཕན་པའོ། །

[Block 90]
བརྩོན་པ་ནི་མངོན་པར་བརྩོན་པའོ། །

[Block 91]
ཡང་གི་སྒྲ་ནི་སྲིད་པའི་ཚུལ་ལོ། །

[Block 92]
གཞན་དོན་བརྩོན་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དོན་ལ་སྤྱོད་པ་ཡིན་པས་གཞན་དོན་བརྩོན་པའོ། །

[Block 93]
ཡོན་ཏན་སྒྲུབ་པ་བཟང་པོ་ཞེས་བྱ་བ་ལ་སྒྲུབ་པ་ནི་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 94]
བཟང་པོ་ནི་བཟང་པོར་གྱུར་པས་སོ། །

[Block 95]
རྗེས་སུ་མཐུན་མ་གྱུར་ཞེས་བྱ་བ་ནི། དེའི་རྗེས་སུ་མ་གྱུར་ཅེས་བྱའོ།[^55] །

[Block 96]
ཡང་ན་རང་དོན་བརྩོན་པ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཏེ། དེས་ཀྱང་རྗེས་སུ་མཐུན་པར་མ་གྱུར་པ་སྟེ། དེ་བཞིན་གཤེགས་པའི་ཡོན་ཏན་ལ་ཡོངས་སུ་སྤྱོད༌[^56]པའམ། །སྐྱེད་པར་མི་ནུས་ན་སྐྱེ་བོ༌[^57]གཞན་དག་གིས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའོ། །

[Block 97]
ཐམས་ཅད་མཁྱེན་པ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཐུགས་སུ་ཆུད་པའི་ཕྱིར་ཐམས་ཅད་མཁྱེན་པའོ། །

[Block 98]
འདི་ལྟར་མ་ནོར་བ་ནི་ཕྱིན་ཅི་མ་ལོག་པའོ། །

[Block 99]
གསལ་བ་ནི་སྣང་བར་གྱུར་པའོ། །

[Block 100]
གྲགས་པ་ནི་སྙན་པའོ། །

[Block 101]
ཆོས་དང་དགེ་འདུན་དང་བཅས་པ་ནི་ཆོས་དང་དགེ་འདུན་དང་ལྷན་ཅིག་པའོ། །

[Block 102]
སྤྱི་བོ་ནི་མགོ་བོའི་གཙུག་གིས་སོ། །

[Block 103]
འདུད་ཅེས་བྱ་བ་ནི་དེས་ཕྱག་འཚལ་བར་བྱེད་པའོ། །

[Block 104 [HEADING]]
## སྟག་མོའི་སྐྱེས་པའི་རབས། ^1-0

[Block 105]
བཅོམ་ལྡན་འདས་དེ་སེམས་ཅན་ཐམས་ཅད་ལ་རྒྱུ་མེད་པར་བྱམས་པའི་ངོ་བོ་ཉིད་ཡིན་ཞེས་བྱ་བ་ནི་ཕྱོགས་སོ། །

[Block 106]
འབྱུང་པོ་ཀུན་ལ་དགའ་བཞིན་དུ་གྱུར་པ་ཞེས་བྱ་བ་ནི་གཏན་ཚིགས་སོ། །

[Block 107]
འདི་སྐད་ཐོས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་བ་ནི་དཔེའོ། །

[Block 108]
སེམས་ཅན་ཞེས་བྱ་བ་ནི་སྐྱེ་དགུའོ། །

[Block 109]
ཐམས་ཅད་ནི་ལུས་པ་མེད་པའོ། །

[Block 110]
རྒྱུ་མེད་པར་ཞེས་བྱ་བ༌[^58]ནི་དགོས་པ་མེད་པར་རོ། །
--- END BLOCKS ---
