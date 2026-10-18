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
[Block 3886 [HEADING]]
##### བར་གྱི་བསྐལ་པ། ^3-2-5-3-0

[Block 3887 [VERSE]]
བར་གྱི་བསྐལ་པ་དཔག་མེད་ནས། །
ཚེ་ལོ་བཅུ་པའི་བར་དུའོ། །

[Block 3888]
འཇིག་རྟེན་ཆགས་པ༌[^2216]ན་མི་རྣམས་ཀྱི་ཚེ་དཔག་ཏུ་མེད་པ་ལ་བར་གྱི་བསྐལ་པ་བཅུ་དགུར་འདའ་བར་འགྱུར་རོ། །

[Block 3889]
ཚེ་དཔག་ཏུ་མེད་པ་ནས་འགྲིབ་པ་ན་ཚེ་ལོ་བཅུ་པའི་བར་དུ་འགྱུར་ཏེ། འདི་ནི་ཆགས་ནས་གནས་པ་རྣམས་ཀྱི་བར་གྱི་བསྐལ་པ་དང་པོ་ཡིན་ནོ། །

[Block 3890 [VERSE]]
དེ་ནས་ཡར་སྐྱེ་མར་འབྲི་བའི། །
བསྐལ་པ་གཞན་ནི་བཅོ་བརྒྱད་དང་། །

[Block 3891]
དེ་ནས་ཡར་སྐྱེ་བ་དང་མར་འབྲི་བ་གཞན་བཅོ་བརྒྱད་དེ། བར་གྱི་བསྐལ་པ་གཞན༌[^2217]བཅོ་བརྒྱད་དུ་འགྱུར་རོ། །ཇི་ལྟ་ཞེ་ན། ཚེ་ལོ་བཅུ་པ་དེ་དག་ཀྱང༌[^2218]ཡར་སྐྱེ་བར་འགྱུར་བ་ན་རིམ་གྱིས་ཚེ་ལོ་བརྒྱད་ཁྲིའི༌[^2219]བར་འགྱུར། [^2220]ཡང་མར་འབྲི་བར་འགྱུར་བ་ན་ཚེ་ལོ་བཅུ་པར་འགྱུར་བ་འདི་ནི་བར་གྱི་བསྐལ་པ་གཉིས་པ་ཡིན་ཏེ། དེ་ལྟ་བུ་བཅོ་བརྒྱད་ཀྱི་བར་དང་། ཡར་སྐྱེ་བ་ནི་གཅིག་ཡིན་ཏེ། བར་གྱི་བསྐལ་པ་ཉི་ཤུ་པ་གཅིག་ནི་ཡར་སྐྱེ་བ་ཁོ་ན་ཡིན་གྱི་མར་འགྲིབ་པ༌[^2221]ནི་མ་ཡིན་ནོ། །

[Block 3892]
མི་རྣམས་ཀྱི་ཚེ་ལོ་བཅུ་པ་དག་ལས་ཚེ་ལོ་བརྒྱད་ཁྲི་པའི་བར་དུ༌[^2222]འགྱུར་རོ། །

[Block 3893]
ཡང་མར༌[^2223]སྐྱེ་བ་དེ་དག་ཇི་ཙམ་དུ་ཡང༌[^2224]སྐྱེ་བར་འགྱུར་ཞེ་ན། དེ་དག་ཚེ་ནི་བརྒྱད་ཁྲིའི་བར།[^2225] །དེ་ལས་ཡར་ནི་མི་སྐྱེའོ། །

[Block 3894]
བར་གྱི་བསྐལ་པ་གཞན་རྣམས་ཀྱི་ཡར་སྐྱེ་བ་དང་མར་འགྲིབ་པའི་དུས་ཇི་སྲིད་པར་བར་གྱི་བསྐལ་པ་དང་པོའི་མར་འགྲིབ་པ་དང་ཐ་མའི་ཡར་སྐྱེ་བའི་དུས་ཀྱང་དེ་སྲིད་པས་ཐམས་ཅད་དུས་མཉམ་པ་ཡིན་ནོ། །

[Block 3895 [VERSE]]
དེ་ལྟར་འཇིག་རྟེན་ཆགས་པ་འདི། །
བར་གྱི་བསྐལ་པ་ཉི་ཤུར་གནས། །

[Block 3896]
དེ་ལྟར་ན་བར་གྱི་བསྐལ་པའི་ཚུལ་འདིས་འཇིག་རྟེན་འདི་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་ཆགས་ནས་གནས་སོ། །

[Block 3897]
དུས་ཇི་སྲིད་དུ་ཆགས་ནས་གནས་པའི་དུས་དེ་སྲིད་ཁོ་ནར།

[Block 3898 [VERSE]]
འཆགས་པ་དང་ནི་འཇིག་པ་དང་། །
ཞིག་ནས་འདུག་པ༌[^2226]དག་མཉམ་མོ། །

[Block 3899]
བར་གྱི་བསྐལ་པ་ཉི་ཤུ་ཁོ་ནར་འཆགས་སོ། །

[Block 3900]
ཉི་ཤུར་འཇིག་གོ། །

[Block 3901]
ཉི་ཤུར་ཞིག་ནས་འདུག་གོ། །

[Block 3902]
གལ་ཏེ་ཡང་དེའི་ཚེ་ཡར་སྐྱེ་བ་དང་མར་འགྲིབ་པ་མི་འཇུག༌[^2227]ཏུ་ཟིན་ཀྱང་དུས་ནི་མཉམ་པར་ཡོངས་སུ་བརྩིའོ། །

[Block 3903]
དེ་ལ་བར་གྱི་བསྐལ་པ་གཅིག་ཏུ་སྣོད་རྣམས༌[^2228]འཆགས་སོ། །

[Block 3904]
བར་གྱི་བསྐལ་པ་བཅུ་དགུར་གནས་པར་བྱེད་དོ། །

[Block 3905]
བར་གྱི་བསྐལ་པ་གཅིག་ཏུ་སྣོད་རྣམས་འཇིག་པར་འགྱུར་རོ། །

[Block 3906]
བཅུ་དགུར་སྟོང་པར༌[^2229]འགྱུར་རོ། །

[Block 3907 [HEADING]]
##### བསྐལ་པ་ཆེན་པོ། ^3-2-5-4-0

[Block 3908]
བར་གྱི་བསྐལ་པ་ཉི་ཤུ་ཕྲག་བཞི་པོ་དེ་དག་ནི་བརྒྱད་ཅུར་འགྱུར་ཏེ། དེ་དག་བརྒྱད་ཅུ་ལ་བསྐལ་ཆེན། །བསྐལ་པ་ཆེན་པོའི་ཚད་ནི་དེ་ཡིན་ནོ། །

[Block 3909]
བསྐལ་པའི་རང་བཞིན་ཅི་ཞེ་ན། ཕུང་པོ་ལྔའི་རང་བཞིན་ནོ། །

[Block 3910 [HEADING]]
##### བསྐལ་པ་གྲངས་མེད་པ་གསུམ། ^3-2-5-5-0

[Block 3911]
བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱིས༌[^2230]སངས་རྒྱས་ཉིད་ཐོབ་པར་འགྱུར་རོ་ཞེས་གང་གསུངས་པ་དེ་བསྐལ་པ་དེ་དག་གང་ཞེ་ན། བསྐལ་པ་ཆེན་པོར་བཤད་པ་གང་ཡིན་པ། དེ་གྲངས་མེད་གསུམ་ལ་སངས་རྒྱས་འབྱུང་ངོ་། །བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱིས་སོ། །

[Block 3912]
གྲངས་མེད་པ་ལ་གྲངས་ཀྱི་མཐའ་མེད་ན་ཇི་ལྟར་གསུམ་ཉིད་དུ་བརྗོད་ཅེ་ན། དེ་ནི་དེ་ལྟར་རིག་པར་མི་བྱའོ། །

[Block 3913]
འོ་ན་ཅི་ཞེ་ན།

[Block 3914]
མདོ་སིལ་བུ་ལས།

[Block 3915]
གྲངས་ནི་གནས་གཞན་དྲུག་ཅུ་དག་གོ་ཞེས་འབྱུང་ངོ་། །དྲུག་ཅུ་གང་ཞེ་ན། གཅིག་སྟེ་གཉིས་པ་མ་ཡིན་པ་ནི་གནས་གཞན་དང་པོ་ཡིན་ནོ། །

[Block 3916]
གཅིག་བཅུ་ནི་གཉིས་པ་ཡིན་ནོ། །

[Block 3917]
བཅུ་ཕྲག་བཅུ་ལ་ནི༌[^2231]བརྒྱ་སྟེ་གསུམ་པ་ཡིན་ནོ། །

[Block 3918]
བརྒྱ་ཕྲག་བཅུ་ལ་ནི་སྟོང་ངོ་། །སྟོང་ཕྲག་བཅུ་ལ་ནི་ཁྲིའོ། །

[Block 3919]
ཁྲི་ཕྲག་བཅུ་ལ་ནི་འབུམ་མོ། །

[Block 3920]
འབུམ་ཕྲག་བཅུ་ལ་ནི་ས་ཡའོ། །

[Block 3921]
ས་ཡ་ཕྲག་བཅུ་ལ་ནི་བྱེ་བའོ། །

[Block 3922]
བྱེ་བ་ཕྲག་བཅུ་ལ་ནི་དུང་ཕྱུར་རོ། །

[Block 3923]
དུང་ཕྱུར་ཕྲག་བཅུ་ལ་ནི་ཐེར་འབུམ་མོ། །

[Block 3924]
ཐེར་འབུམ་ཕྲག་བཅུ་ལ་ནི་ཐེར་འབུམ་ཆེན་པོའོ། །

[Block 3925]
ཐེར་འབུམ་ཆེན་པོ་ཕྲག་བཅུ་ལ་ནི་ཁྲག་ཁྲིག་གོ། །
--- END BLOCKS ---
