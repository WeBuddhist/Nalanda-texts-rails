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
[Block 3361]
བདག་བློ་ཞན་པས་ཞེས་བྱ་བ་ནི་བདག་གི་ཤེས་རབ་དང་ཡེ་ཤེས་ཆུང་བས༌[^2908]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3362]
འགོག་པ་ལ་ཡང་འཁྲུལ་པ་མེད་ཅེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་དུ་སྟོན་པ་ལ་ཡང་འཁྲུལ་བ་མེད་པའོ། །

[Block 3363]
རྟོགས་པ་ཁོང་དུ་ཆུད་ཅིང་ཞེས༌[^2909]བྱ་བ་ནི་ཕྱིན་ཅི་མ་ལོག་པར་ཁོང་དུ་ཆུད་པའོ། །

[Block 3364]
ཡང་དག་པའི་དོན་རྣམ་པར་ངེས་པ་ཐོབ་པ་ཡིན་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་ཕྱིན་ཅི་མ་ལོག་པ་དང་། གཏན་ལ་ཕབ་པར་ཁོང་དུ་ཆུད་ཅིང་སྟོན་ནུས་པ་ཐོབ་པ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3365]
དམ་པ་ནི་ཉན་ཐོས་ལ་སོགས་པ་སོ་སོ་ཡང་དག་པར་རིག་པ་ལས༌[^2910]ཁྱད་པར་དུ་འཕགས་པའོ། །

[Block 3366]
མཆོག་ཐོབ་པ་ནི་སོ་སོ་ཡང་དག་པར་རིག་པ་ཐོབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་གཞན་པས་ཀྱང་མཆོག་ཏུ་གྱུར་པའོ། །

[Block 3367]
མིང་ཅི་ལགས༌[^2911]ཞེས་པ་ནི་བདག་གི་དོན་དུ་བྲིས་པ༌[^2912]སྟེ། བདག་གི་མིང་ཇི་ལྟར་འཚལ་བར་བགྱི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3368]
ཇི་ལྟ་བུར༌[^2913]གཟུང་བར་བགྱི་ཞེས་བྱ་བ་ནི་གཞན་གྱི༌[^2914]དོན་དུ་དྲིས་པ་སྟེ། བདག་གིས༌[^2915]བཟུང་ནས་གཞན་ལ༌[^2916]འཆད་ཅིང་ཐ་སྙད་དུ་བགྱིད་པའི་ཚེ་ན་ཡང་། ཇི་ལྟར་འཛིན་དུ་སྩལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3369]
[^2917]འཕགས་པ་བློ་གྲོས་མི་ཟད་པའི་མདོ་རིམ་གྱིས་མི་ཟད་པ་རྣམས་ཀྱི་ལུས་རྣམ་པར་གཞག་པ་ནི་རྣལ་འབྱོར་སྤྱོད་པའི་ས་ལས་བསྟན་ཏེ་དེར་བལྟ་བར་བྱའོ། །

[Block 3370 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 3371 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 3372]
འཕགས་པ་བློ་གྲོས་མི་ཟད་པས་བསྟན་པའི་བཤད་པ་རྫོགས་སོ།། །།

[Block 3373]
[^2918]
--- END BLOCKS ---
