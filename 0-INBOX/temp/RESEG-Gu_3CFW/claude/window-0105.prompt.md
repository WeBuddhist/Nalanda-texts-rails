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
[Block 3676]
དེ་དག་གི་སྟེང་དུ་སྤང་ལེབ་དག་གོ། །

[Block 3677]
དེ་དག་གི་སྟེང་དུ་སོ་ཕག་དགྲམ་མོ། །

[Block 3678]
དེ་དག་གི་སྟེང་དུ་སོ་ཕག་གི་ཕྱེ་མའི་འཇིམ་པའོ་ཞེས་བྱ་བ་ནི་དེ་དག་གི་སྟེང་དུ་སོ་ཕག་གི་ཕྱེ་མའི་འཇིམ་པ་གླན་པར་བྱ་བའོ།[^3783] །མི་ལྟུང་བར་བྱ་བའི་ཕྱིར་ལན་ཀན་བྱའོ། །

[Block 3679]
མི་འགུལ་བར་བྱ་བའི་ཕྱིར་ཤར་བ་གཞུག་གོ། །

[Block 3680]
དེ་ལྕགས་ཀྱི་གཟེར་བུ་དག་གིས་སྦྱར་རོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་དེ༌[^3784]ཤར་བ་དེའོ། །

[Block 3681]
འཛེག་པའི༌[^3785]ཕྱིར་ཐེམ་སྐས་བྱའོ། །

[Block 3682]
འོག་ཏུ་རྡོ་ལས་བྱས་པ་བར་དུ་ས་ལས་བྱས་པ།[^3786] སྟེང་དུ་ཤིང་ལས་བྱས་པའོ། །

[Block 3683]
ཡ་གད་ལས་འཛེག་པར༌[^3787]བྱའོ། །

[Block 3684]
ཤིང་དང་སྨྱིག༌[^3788]མ་དང༌[^3789]ཐག་པ་ལས་བྱས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཤིང་ལས་བྱས་པ་དང་སྨྱིག་མ་ལས་བྱས་པ་དང་ཐག་པ་ལས་བྱས་པ་རྣམས་སོ། །

[Block 3685]
རྫིང་བུ་དང་སྒོ་ཁང་དུ་རྫབ་མི་འབྱུང་བར་བྱ་བའི་ཕྱིར་སོ་ཕག་གི་གཅལ་གཞུག་གོ། །

[Block 3686]
དེའི་སྟེང༌[^3790]སོ་ཕག་གི་ཕྱེ་མའི༌[^3791]འཇིམ་པའོ་ཞེས་བྱ་བ་ནི་སོ་ཕག་གི་གཅལ་དེའི་སྟེང་དུའོ། །

[Block 3687]
དེའི་སྟེང་དུ་རྡོ༌[^3792]ཐལ་གྱིས་སོ་ཞེས་བྱ་བ་ནི་སོ་ཕག་གི་སྟེང་མའི་འཇིམ་པ་དེའི་སྟེང་དུ་རྡོ༌[^3793]ཐལ་གྱི་སྐྱང་ནུལ་གྱིས་བསྐུ་བར་བྱ་བའོ།[^3794] །མེད་ན་རྐང་པ་བསྐྱབ་པའི་ཕྱིར་ཤིང་གི་སྤང་ལེབ་སོ༌[^3795]ཞེས་བྱ་བ་ནི་གཅལ་ཇི་ལྟར༌[^3796]བསྟན་པའི་རྫས་དེ་དག་མེད་ན་རྐང་པ་བསྐྱབ་པའི་ཕྱིར་སྤང་ལེབ་གཞུག་པར་བྱའོ། །

[Block 3688]
ཡང་ན་བར་བར་དུ་སོ་ཕག་གོ་ཞེས་བྱ་བ་ནི་རྐང་པ་བསྐྱབ་པའི་ཕྱིར་གཞུག་པའོ། །

[Block 3689]
མཆོད་རྟེན་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་རྫབ་མི་འབྱུང་བར་བྱ་བའི་ཕྱིར༌[^3797]སོ་ཕག་གི་གཅལ་གཞུག་གོ་ཞེས་བྱ་བ་ནས་སོ་ཕག་དག་གོ་ཞེས་བྱ་བའི་བར་དེ་དག་དེ་བཞིན་དུ་གཞུག་པའོ། །

[Block 3690]
འདི་ལ་དེ་འདོམ་གང་ཙམ་བྱས་པ་ཉིད་ན་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི་གཅལ་དེའོ། །

[Block 3691]
འདི་ལ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་ལའོ། །

[Block 3692]
སེང་གེའི་ཁྲི་གྲུ་བཞི་བྱའོ། །

[Block 3693]
རྐང་པ་དག་ལ་སེང་གེའི་གདོང་ཉིད་དོ། །

[Block 3694]
སྤོ་བའི་ཕྱིར་གཟུང་བའི༌[^3798]དོན་དུ་བཞི་པོ་དེ་དག་ལ་ལྕགས་ཀྱི་ཡང་མིག་དག་གདགས་སོ་ཞེས་བྱ་བ་ལ་དེ་དག་ལ་ཞེས་བྱ་བ་ནི་རྐང་པ་བཞི་པོ་དག་ལའོ། །

[Block 3695]
ཐག་གུ་དག་གིས༌[^3799]གདགས་སོ། །

[Block 3696]
དེར་སྟན་ནང་ཚངས་ཅན་གཞག་གོ། །

[Block 3697]
[^3800]སྟེང་དུ་བླ་རེའོ་ཞེས་བྱ་བ་ནི་གདགས་པའོ། །

[Block 3698]
དཔྱང་བ༌[^3801]དག་གོ་ཞེས་བྱ་བ་ནི་ཡང་གདགས་པའོ། །

[Block 3699]
བརྟན་པ་ལ་ནི་སོ་ཕག་ལས་བྱས་པའི་ཐེམ་སྐས་བྱའོ་ཞེས་བྱ་བ་ནི་མི་བསྐྱོད་པའི༌[^3802]ཆོས་ཅན་བརྟན་པ་ལའོ། །

[Block 3700]
སྤོ་བ་ལས་ནི་ཤིང་ལས་བྱས་པའོ། །

[Block 3701]
མ་འབྱོར་ན་ཡ་གད་དོ་ཞེས་བྱ་བ་ནི་ཐེམ་སྐས་མ་འབྱོར་ན་འདི་བྱ་བའོ། །

[Block 3702]
རྐང་རྟེན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གང་དུ་རྐང་པ་གཉིས་མི་འཕྱང་བ་ནི་འདིར་དགོས་པ་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 3703]
དེ་བས་ན་གང་དུ་རྐང་པ་འཕྱང་བ་དེ་རྟོགས་པར༌[^3803]བྱའོ། །

[Block 3704]
མཆོད་པའོ་ཞེས་བྱ་བ་ནི་རྐང་རྟེན་ལའོ་ཞེས་བྱ་བ་དེ་མ་ཐག་པར་ཤེས་པར་བྱའོ། །

[Block 3705]
སྟེང་དུ་ལོ་མའི་ཆུན་པོ་འམ་རྩྭའི་ཆུན་པོ་གཞུག༌[^3804]གོ། །

[Block 3706]
འདི་ནི་རྐང་པ་གཉིས་མི་འཕྱང་བར་བྱ་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལ། འདི་ནི་ཞེས་བྱ་བ་ནི་རྐང་པའི་རྟེན་ལའོ། །

[Block 3707]
འདི་ནི་རྡོས་འགྲུབ་པོ༌[^3805]ཞེས་བྱ་བ་ལ། འདི་ནི་ཞེས་བྱ་བ་ནི་རྐང་པ་གཉིས་མི་འཕྱང་བ་འདིའོ། །

[Block 3708]
ཟན་ཟ་བ་དག་ལ་ཁྲ༌[^3806]དང་བྱེའུ༌[^3807]དང་ཕུག་རོན་དག་གིས་མི་འཚེ་བར༌[^3808]བྱ་བའི་ཕྱིར་བྱ་རྒྱ་བྱའོ་ཞེས་བྱ་བ་ནི་གང་དུ་ཁྭ་ཏ་ལ་སོགས་པ་འབྱུང་བ་དེར་ཞེས་བྱ་བ་ནི་དོན་གྱིས་ཤེས་པའོ། །

[Block 3709]
འདིར་གཞུང་ནི་དགེ་སློང་དག་ཁྱམས་སུ་ཟན་ཟ་བ་ན།[^3809] དེ་དག་ཁྭ་དང་བྱེའུ༌[^3810]དང་ཕུག་རོན་དག་གིས༌[^3811]འཚེ་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བྱ་རྒྱ་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3710]
རྣམ་པ་བཞིའོ་ཞེས་བྱ་བ་ནི་བྱ་རྒྱ་དེའོ། །

[Block 3711]
མུཉྫ་ལས་བྱས་པ་དང་། བལ་བ་ཛ་ལས་བྱས་པ་དང་། ཤ་ན་ལས་བྱས་པ་དང་། རས་བལ་ལས་བྱས་པའོ༌[^3812]ཞེས་བྱ་བ་ནི་གླེང་གཞི་དག་ལས་དེ་གསུངས་པ་དང་། འདིར་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས་ཀྱང་དྲ་བ་ནི་རྣམ་པ་ལྔ་སྟེ། ལྔ་གང་ཞེ་ན། ཤ་ན་ལས་བྱས་པ་དང་། མུཉྫ་ལས་བྱས་པ་དང་། བལ་བ་ཛ་ལས་བྱས་པ་དང་། ཀ་ཤ་ལས་བྱས་པ་དང་། ཀུ་ཤ་ལས་བྱས་པའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ།[^3813] དེ་དག་ནི་འགལ་བར་ཤེས་པར་མི་བྱ་སྟེ། དེ་ནི་གཉིས་ཀ་ལ་ཡང་དཔེ་ཉིད་དུ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 3712]
བལ་བ་ཛ་སྨོས་པས་ནི་སྔར་གྱི་ཀ་ཤ་ལས་བྱས་པ་དང་། ཀུ་ཤ་ལས་བྱས་པ་དག་ཀྱང་འཕངས་པར་ཤེས་པར་བྱའོ། །

[Block 3713]
ཤ་ན་ལས་བྱས་པ་ཞེས་སྨོས་པས་ནི་ཕྱི་མ་རས༌[^3814]བལ་ལས་བྱས་པ་ཡང་འཕངས་སོ། །

[Block 3714]
གྲུ་བཞི་དག་ཏུ་གཟུངས༌[^3815]གཟེར་གདབ་བོ། །

[Block 3715]
དེ་དག་ལ་ཡང་གདགས་སོ་ཞེས་བྱ་བ་ནི་གཟུངས༌[^3816]གཟེར་དེ་དག་ལ་བྱ་རྒྱ་གདགས་སོ། །
--- END BLOCKS ---
