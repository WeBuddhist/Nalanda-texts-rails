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
[Block 5146]
དེ་ལྟར་ཡང་གཞུང་ནི་འདི༌[^3533]རྣམ་པར་འབྱེད་པ་ལས་དགེ་སློང་གིས་ཇི་ཙམ་དུ་གཞན་འདྲི་བ་ལ་ལན་འདེབས་ན་ཐམས་ཅད་དུ་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5147]
གཞན་འདྲི་བ་ལ་དོན་གཞན་བརྗོད་པ་ནི་གཞན་བརྗོད་པའོ། །

[Block 5148]
རྟོག་པ༌[^3534]ཡོད་པ་ལ་དོན་གཞན་གྱིས་ནི་དངོས་ཏེ།

[Block 5149]
དེ་ལྟར་ཡང་གཞུང་ནི་ཞུ་བ་ལས།

[Block 5150]
དབུས་པའི་ཚིག་གིས་མཐའ་འཁོབ་པ་ལ་འམ། མཐའ་འཁོབ་པའི་ཚིག་གིས་དབུས་པ་ལ་མཐའ་གཞན་དང་གཞན༌[^3535]བརྗོད་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5151]
ཅང་མི་སྨྲ་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཅང་མི་སྨྲ་བས་དགེ་སློང་གིས་བསྒོས་པ༌[^3536]རྣ་ལ་གཟོན་ལ༌[^3537]ཉེས་བྱས་སོ། །

[Block 5152]
མི་དྲན་ནོ་ཞེ་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བརྗོད་པ་འདི་ཉིད་དེ༌[^3538]དང་འབྲེལ་པ་ཉིད་ཡིན་ཏེ། གཞན་དོན་ལ་ནི་མ་ཡིན་ཏེ་དེ་བས་འདི༌[^3539]ན་སྨད་པའོ། །

[Block 5153]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་མི་དྲན་ནོ་ཞེས་ཟེར་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 5154]
གལ་ཏེ་བརྗོད་པར་བྱ་བ་སྡུག་བསྔལ་བར་གྱུར་པ་ཡིན་ན་མེད་དོ་ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་བར་གྱུར་པའི་རྒྱུ་ཡིན་ན་གཞན་བརྗོད་ཀྱང་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་གི་ཕྱིར་དེ༌[^3540]འདི་ལྟར་ཡིན་ན།[^3541] དེའི་ཕྱིར་གསད་པར༌[^3542]བྱ་བ་མཐོང་ངམ་ཞེས་འདྲི་བ་ལ་རེ་ཞིག་མེ་འདེ་ཤིག༌[^3543]སྐོམ་འཐུངས་ཤིག༌[^3544]ངལ་སོས༌[^3545]ཤིག །ནམ་མཁའ་མཐོང་ངོ་སེན་མོ་མཐོང་ངོ་། །དོན་དམ་པར་ན་སེམས་ཅན་ནམ་གསད་པར༌[^3546]བྱ་བ་མ་མཐོང་ངོ་ཞེས་བྱ་བ་སྨྲས་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའོ། །

[Block 5155]
གང་དུ་ཆེ་བཞི་ཉིད་བྱ་དགོས་པར་འགྱུར་བའི་གནས་དེར་བསྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གླེང་གཞི་དག་ལས་ཆོ་ག་གཉིས་པ༌[^3547]འདི་དེ་ལྟ་བུའི་འདྲི་བའི་ཕྱོགས་ཀྱི་ཕྱིར་འདིར་ཡང་དག་པར་ཞུགས་པའོ། །

[Block 5156]
གནོད་པའི་སྒོ་མ་བཅད་པས་ཆེ་བཞིའི༌[^3548]དབྱེ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཆང་བ་ལ་སོགས་པ་གནོད་པར་སྒོ༌[^3549]མ་བཅད་པ་གང་གིས་ཞེས་བྱ་བ་འདིར་བསྡུ་བའོ། །

[Block 5157]
གསད་པ༌[^3550]དང་བཅིང་བ་ལ་སོགས་པ་དག་གིས་གཞན་ལ་གནོད་པ་དག་གི༌[^3551]སྒོ་ནི་སྒོ་སྟེ། སྒོ་གང་གིས་གནོད་པ་དེའི་བཅད་པ་ནི་བཅད་པ་མ་བྱས་པར་ཆེ་བཞིའི༌[^3552]དབྱེ་བར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5158]
བསྒོ་བ༌[^3553]རྣ་ལ་གཟོན་པའི་ལྟུང་བྱེད་དོ།། །།
--- END BLOCKS ---
