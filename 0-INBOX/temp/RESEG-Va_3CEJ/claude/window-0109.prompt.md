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
[Block 3816 [HEADING]]
##### དཔག་ཚད་ཀྱི་ཚད། ^3-2-4-2-0

[Block 3817 [VERSE]]
དེ་ལ་ཕྲ་རབ་རྡུལ་དང་ནི། །
རྡུལ་ཕྲན་དང་ནི་དེ་བཞིན་དུ། །
ལྕགས་ཆུ་རི་བོང་ལུག་དང་གླང་། །
ཉི་ཟེར་རྡུལ་དང་སྲོ་མ་དང་། །

[Block 3818 [VERSE]]
དེ་ལས་བྱུང་དང་དེ་བཞིན་དུ། །
སོར་ཚིགས་ཞེས་བྱ་གོང་བདུན་འགྱུར། །

[Block 3819]
རྡུལ་ཕྲ་རབ་ལ་སོགས་པ་འདི་དག་ནི་གོང་ནས་གོང་དུ་བདུན་འགྱུར་དུ་རིག་པར་བྱ་སྟེ། རྡུལ་ཕྲ་རབ་བདུན་ལ་ནི་རྡུལ་ཕྲན་ནོ། །

[Block 3820]
རྡུལ་ཕྲན་བདུན་ལ་ནི་ལྕགས་རྡུལ་ལོ། །

[Block 3821]
དེ་དག་བདུན་ལ་ནི་ཆུ་རྡུལ་ལོ། །

[Block 3822]
དེ་དག་བདུན་ལ་ནི་རི་བོང་གི༌[^2186]རྡུལ་ལོ། །

[Block 3823]
དེ་དག་བདུན་ལ་ནི་ལུག་རྡུལ་ལོ། །

[Block 3824]
དེ་དག་བདུན་ལ་ནི་གླང་རྡུལ་ལོ། །

[Block 3825]
དེ་དག་བདུན་ལ་ནི་ཉི་ཟེར་རྡུལ་ལོ། །

[Block 3826]
དེ་དག་བདུན་ལ་ནི༌[^2187]སྲོ་མའོ། །

[Block 3827]
སྲོ་མ་བདུན་ལ་ནི་དེ་ལས་བྱུང་བ་སྟེ། སྲོ་མ་ལས་བྱུང་བ་ནི་ཤིག་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3828]
ཤིག་བདུན་ལ་ནི་ནས་སོ། །

[Block 3829]
ནས་བདུན་ལ་ནི་སོར་མོའི་ཚིགས་སོ། །

[Block 3830]
སོར་མོའི་ཚིགས་གསུམ་ལ་ནི་སོར་མོ་ཞེས་བྱ་བར་གྲགས་པ་ཉིད་པས་མ་བཤད་དོ། །

[Block 3831]
ངོས་སུ་བྱ་བ༌[^2188]ནི།

[Block 3832 [VERSE]]
སོར་ནི་ཉི་ཤུ་བཞི་ལ་ཁྲུ། །
ཁྲུ་བཞི་ལ་ནི༌[^2189]གཞུ་གང་ངོ་། །

[Block 3833]
འདོམ་གང་ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3834 [VERSE]]
དེ་དག་ལྔ་བརྒྱ་རྣམས་ལ་ནི། །
རྒྱང་གྲགས་དེ་ལ་དགོན་པར་འདོད། །

[Block 3835]
གཞུ་ལྔ་བརྒྱ་ལ་ནི་རྒྱང་གྲགས་ཏེ། གྲོང་ནས་རྒྱང་གྲགས་ཙམ་གྱི་ཐག་ལ་ནི་དགོན་པ་ཡིན་པར་འདོད་དོ། །

[Block 3836]
དེ་བརྒྱད་དཔག་ཚད་ཅེས་བྱའོ། །

[Block 3837]
རྒྱང་གྲགས་དེ་དག་བརྒྱད་ལ་དཔག་ཚད་ཅེས་བྱའོ། །

[Block 3838]
དཔག་ཚད་ཀྱི་ཚད་ནི་བཤད་ཟིན་ཏོ། །

[Block 3839 [HEADING]]
##### ལོའི་ཚད། ^3-2-4-3-0

[Block 3840]
ད་ནི་ལོའི་ཚད༌[^2190]བརྗོད་པར་བྱ་སྟེ། སྐད་ཅིག་མ་བརྒྱ་ཉི་ཤུ་ལ། དེ་ཡི་སྐད་ཅིག །སྐད་ཅིག་མ་བརྒྱ་ཉི་ཤུ་ལ་དེའི༌[^2191]སྐད་ཅིག་གོ། །

[Block 3841]
དེ་དག་ཀྱང་། དྲུག་ཅུ་ལ་ནི་ཐང་ཅིག་གོ། །

[Block 3842]
དེའི་སྐད་ཅིག་དྲུག་ཅུ་ལ་ནི་ཐང་ཅིག་ཅེས་བྱའོ། །

[Block 3843 [VERSE]]
ཡུད་ཙམ་ཉིན་ཞག་ཟླ་གསུམ་ནི། །
གོང་ནས་གོང་དུ་སུམ་ཅུར༌[^2192]འགྱུར། །
ཐང་ཅིག་སུམ་ཅུ་ལ་ཡུད་ཙམ་མོ། །

[Block 3844]
ཡུད་ཙམ་སུམ་ཅུ་ལ་ནི༌[^2193]ཉིན་ཞག་གཅིག་གོ། །

[Block 3845]
རེས་འགའ་ནི་མཚན་མོ་རིང་ངོ་། །རེས་འགའ་ནི་ཐུང་ངོ་། ། རེས་འགའ་ནི་མཉམ་མོ། །

[Block 3846]
ཉིན་ཞག་སུམ་ཅུ་ལ་ནི་ཟླ་བ་གཅིག་གོ། །

[Block 3847]
ཞག་མི་ཐུབ་དང་བཅས་པ་ཡི། །ཟླ་བ་བཅུ་གཉིས་ལ་ལོ་གཅིག་གོ།[^2194] །དགུན་རྣམས་ཀྱི་ཟླ་བ་བཞི་དང་། དཔྱིད་རྣམས་ཀྱི་ཟླ་བ་བཞི་དང་། དབྱར་རྣམས་ཀྱི་ཟླ་བ་བཞི་སྟེ། དེ་དག༌[^2195]ཟླ་བ་བཅུ་གཉིས་པོ་དེ་དག་ཞག་མི་ཐུབ་དང་བཅས་པ་ལ་ལོ་གཅིག་གོ། །

[Block 3848]
ལོ་ལ་ནི་ཞག་གཅིག༌[^2196]གི་ཤོལ་དྲུག་དོར་ཏེ། ཇི་ལྟ༌[^2197]ཞེ་ན།

[Block 3849 [VERSE]]
དགུན་དང་དཔྱིད་དང་དབྱར་རྣམས་ཀྱི། །
ཟླ་བ་ཕྱེད་དང་གཉིས་འདས་ནས། །
ཟླ་བ་ཕྱེད་ནི་ལུས་པ་ན། །
མཁས་པས་ཞག་མི་ཐུབ་པ༌[^2198]དོར། །

[Block 3850]
ལོའི་ཚད་བཤད་ཟིན་ཏོ། །

[Block 3851 [HEADING]]
#### བསྐལ་པ། ^3-2-5-0

[Block 3852]
ད་ནི་བསྐལ་པ༌[^2199]བརྗོད་པར་བྱ་སྟེ། བསྐལ་པ་རྣམ་པ་མང་བཤད་པ། །བར་གྱི་བསྐལ་པ་དང་། འཇིག་པའི་བསྐལ་པ་དང་། འཆགས་པའི་བསྐལ་པ་དང་། བསྐལ་པ་ཆེན་པོའོ། །

[Block 3853]
དེ་ལ་རེ་ཞིག །

[Block 3854 [HEADING]]
##### འཇིག་པའི་བསྐལ་པ། ^3-2-5-1-0

[Block 3855 [VERSE]]
འཇིག་པའི་བསྐལ་པ་དམྱལ་བ་ཡི། །
སྲིད་པ་མེད་ནས་སྣོད་ཟད་པ། །
--- END BLOCKS ---
