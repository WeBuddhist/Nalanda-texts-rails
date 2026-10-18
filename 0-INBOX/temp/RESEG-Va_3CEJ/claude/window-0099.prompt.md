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
[Block 3466]
འདི་ལ་མི་རིགས་པ༌[^1977]ཅི་ཞིག་ཡོད་ཅེ་ན། དེ་ཉིད་འདི་ཡིན་ལ། འདིས༌[^1978]དེ་ལྟ་བུ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་གི་ལུགས་འདི་ནི་སྔོན་མ་བྱུང་བ་ཡིན་ནོ། །

[Block 3467]
དེ་ལྟར་བྱུང་བའི༌[^1979]གསེར་ལ་སོགས་པ་ལས་ཀྱི་མཐུས་བསྐྱེད་པའི་རླུང་དག་གིས་བསྡུས་ནས་ཕུང་པོར་བྱེད་དེ། དེ་དག་ནི་རི་དག་ཏུའང་འགྱུར་ལ། གླིང་རྣམས་སུ་ཡང་འགྱུར་རོ། །

[Block 3468]
རི་རབ་ལ་སོགས་པ་ཁོར་ཡུག་ལ་ཐུག་པའི་རི་དེ་དག་ནི་ཆུའི་ནང་དུ་བརྒྱད་ཁྲི་དག་ནུབ་བོ། །

[Block 3469]
དེ་དག་གསེར་གྱི་ས་གཞིའི་སྟེང་ན་ཆུ་དཔག་ཚད་བརྒྱད་ཁྲི་ཡོད་པ་དེར་ནུབ་བོ། །

[Block 3470]
ཆུའི་སྟེང༌[^1980]དུ་ཡང་། དཔག་ཚད་དག་ནི་བརྒྱད་ཁྲིའོ། །

[Block 3471]
དེ་ལྟར་ན་རི་རབ་ནི་འཕང་དུ་དཔག་ཚད་འབུམ་དྲུག་ཁྲིའོ། །

[Block 3472]
བརྒྱད་པོའི་འཕང་དུ་ཕྱེད་ཕྱེད༌[^1981]དབྲི། །རི་རབ་ཆུའི་སྟེང་དུ་ཇི་ཙམ་འཕགས་པ་དེའི་ཕྱེད་ནི་གཉའ་ཤིང་འཛིན་ཏེ། དཔག་ཚད་བཞི་ཁྲི་ཡིན་ལ། དེའི་ཕྱེད་ནི་གཤོལ་མདའ་འཛིན་ཏོ་ཞེས་བྱ་བས།[^1982] དེ་བཞིན་དུ་གཞན་དག་ལ་ཡང་མུ་ཁྱུད་འཛིན་གྱི་ཕྱེད་ནི་ཁོར་ཡུག་སྟེ། འཕང་དུ་དཔག་ཚད་སུམ་བརྒྱ༌[^1983]ཕྱེད་དང་བཅུ་གསུམ་ཡིན་ནོ་ཞེས་བྱ་བའི་བར་དུ་ཕྱེད་ཕྱེད་ཀྱིས་དབྲི་བར་རིག་པར་བྱའོ། །

[Block 3473]
དེ་དག་རྔམས་སུ༌[^1984]འཕང་དང་མཉམ། །དེ་དག་ཆུ་ལས་ཇི་ཙམ༌[^1985]གྱེན་དུ༌[^1986]འཕགས་པ་རྔམས་སུ་ཡང་དེ་ཙམ་སྟེ།

[Block 3474]
རྒྱར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3475 [HEADING]]
##### རོལ་མཚོ་བདུན། ^3-2-1-4-0

[Block 3476]
དེ་དག་བར་བདུན་རོལ་མཚོ་ཡིན། །

[Block 3477]
མུ་ཁྱུད་འཛིན་ལ་ཐུག་པའི་རི་དེ་དག་གི་བར་བདུན་ནི་རོལ་མཚོ་བདུན་ཞེས་བྱ་སྟེ། ཡན་ལག་བརྒྱད་དང་ལྡན་པའི་ཆུས་གང་ངོ་། །ཆུ་དེ་ནི་བསིལ་བ་དང་། ཞིམ་པ་དང་། ཡང་བ་དང་། འཇམ་པ་དང་། དངས་པ༌[^1987]དང་། དྲི་ང་བ་མེད་པ་དང་། འཐུང༌[^1988]ན་མགྲིན་པ་ལ་མི་གནོད་པ་དང་། འཐུངས༌[^1989]ན་ལྟོ་ལ་མི་གནོད་པའོ། །

[Block 3478]
ཡང་དེ་དག་ལས། དང་པོ་སྟོང་ཕྲག་བརྒྱད་ཅུའོ། །

[Block 3479]
རི་རབ་དང་གཉའ་ཤིང་འཛིན་གྱི་བར་གྱི་རོལ་མཚོ་དང་པོ་ནི་ཁ་ཚོན་དཔག་ཚད་བརྒྱད་ཁྲིའོ། །

[Block 3480]
དེ་ནི་ནང་གི་རྒྱ་མཚོ་ཡིན། །རྒྱ་མཚོ་ནི་གཉིས་ཏེ། ནང་གི་དང་ཕྱིའིའོ། །

[Block 3481]
རོལ་མཚོ་དེ་ནི་ནང་གི་རྒྱ་མཚོ་ཡིན་ནོ། །

[Block 3482]
དེའི་ངོས་ལ་སུམ་འགྱུར་རོ། །

[Block 3483]
ཁ་ཚོན་ནི་དཔག་ཚད་བརྒྱད་ཁྲི༌[^1990]བཤད་དོ། །

[Block 3484]
ངོས་ལ་ནི་གཉའ་ཤིང་འཛིན་གྱི་འགྲམ་ནས་བགྲངས་ན་སུམ་འགྱུར་ཏེ། དཔག་ཚད་ཉིས་འབུམ་བཞི་ཁྲིའོ། །

[Block 3485]
རོལ་མཚོ་གཞན་ནི་ཕྱེད་ཕྱེད་དོ། །

[Block 3486]
[^1991]གཉའ་ཤིང་འཛིན་ནས་གཤོལ་མདའ་འཛིན་གྱི་བར་གྱི་རོལ་མཚོ་གཉིས་པ་ནི་དང་པོའི་ཕྱེད་དེ། དཔག་ཚད་བཞི་ཁྲི་ཡིན་ལ།

[Block 3487]
གསུམ་པ་ནི་དེའི་ཕྱེད་དོ་ཞེས་བྱ་བ་ནས། དེ་བཞིན་དུ་རོལ་མཚོ་བདུན་པ་ནི། དཔག་ཚད་སྟོང་ཉིས་བརྒྱ་ལྔ་བཅུའོ༌[^1992]ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 3488]
[^1993]རོལ་མཚོ་གཞན་རྣམས་ཕྱེད་ཕྱེད་ཀྱིས་དབྲིའོ། །

[Block 3489]
དེ་དག་གི་སྲིད་དུ་ནི་ཧ་ཅང་འབྱམས༌[^1994]ཀླས་པའི་ཕྱིར་མ་བགྲངས་སོ། །

[Block 3490 [HEADING]]
##### ཕྱིའི་མཚོ་ཆེན། ^3-2-1-5-0

[Block 3491]
ལྷག་མ་ཕྱིའི་མཚོ་ཆེན་ཡིན། །ལྷག་མ་གང་ཞིག་ཅེ་ན་མུ་ཁྱུད་འཛིན་དང་ཁོར་ཡུག་གི་བར་དེའི་ནི་ཕྱིའི་རྒྱ་མཚོ་ཆེན་པོ་ཡིན་ཏེ། ཚྭ་སྒོའི༌[^1995]ཚྭ་ཆུས་གང་ངོ་། །དེ་ཡང་ཁ་ཚོན་དུ༌[^1996]དཔག་ཚད་འབུམ་ཕྲག་གསུམ་དང་སྟོང་ཕྲག་ནི་ཉི་ཤུ་གཉིས་སོ། །

[Block 3492 [HEADING]]
##### གླིང་བཞི། ^3-2-1-6-0

[Block 3493 [HEADING]]
###### འཛམ་བུའི་གླིང། ^3-2-1-6-1-0

[Block 3494]
དེ་ལ་རི་རབ་ཀྱི་ངོས་བཞི་ནི༌[^1997]གླིང་བཞི་སྟེ། དེ་ལ་ནི་འཛམ་བུའི་གླིང་སྟེ་ངོས་གསུམ་ལ། སྟོང་ཕྲག་གཉིས་པོ༌[^1998]ཤིང་རྟའི་དབྱིབས། །དེའི་ངོས་གསུམ་ལ་དཔག་ཚད་ཉིས་སྟོང་ཉིས་སྟོང་ཡོད་ལ། དེའི་དབྱིབས༌[^1999]ཀྱང་ཤིང་རྟ་དང་འདྲའོ། །

[Block 3495]
དེའི་དབུས་སུ་གསེར་གྱི་རང་བཞིན་གྱི་ས་གཞི་ལ་གང་དུ་བྱང་ཆུབ་སེམས་དཔའ་བཞུགས་ནས་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་སྐྱེད་པར༌[^2000]མཛད་པ་རྡོ་རྗེའི་གདན་མངོན་པར་འགྲུབ་སྟེ། དེ་ནི་ལུས་སམ་ས་ཕྱོག་གཞན་གྱིས་བཟོད་པར་མི་ནུས་སོ། །

[Block 3496]
གཅིག་ལ་དཔག་ཚད་ཕྱེད་དང་བཞིའོ། །

[Block 3497]
[^2001]དེའི་ངོས་བཞི་པ་དག༌[^2002]ལ་ནི་དཔག་ཚད་ཕྱེད་དང་བཞི་སྟེ། དེ་ཉིད་ཀྱི་ཕྱིར་འདི་ནི་ཤིང་རྟ་ཆེན་པོའི༌[^2003]དབྱིབས་ལྟ་བུ་ཡིན་ནོ། །

[Block 3498 [HEADING]]
###### ཤར་གྱི་ལུས་འཕགས། ^3-2-1-6-2-0

[Block 3499]
ཤར་གྱི་ལུས་འཕགས་ཟླ་གམ་འདྲ། །འདི་ནས་ཤར་ཕྱོགས་ཀྱི་རི་རབ་ཀྱི་ངོས་རོལ་ན་ཤར་གྱི་ལུས་འཕགས་ཀྱི་གླིང་ཡོད་དེ། དེ་ནི་ཟླ་བ་ཁམ་པ༌[^2004]ལྟ་བུར་མངོན་པར་གྲུབ་བོ། །

[Block 3500]
རྒྱར་ནི་ངོས་གསུམ་འདི་དང་འདྲའོ། །

[Block 3501]
[^2005]ཇི་ལྟར་འཛམ་བུའི་གླིང་ལ་དཔག་ཚད་ཉིས་སྟོང་ཉིས་སྟོང་ཡོད་པ་བཞིན་ནོ། །

[Block 3502]
གཅིག་ལ་དཔག་ཚད་སུམ་བརྒྱ་ལྔ་བཅུའོ། །

[Block 3503]
ངོས་བཞི་པ་ལ་ནི་དཔག་ཚད་སུམ་བརྒྱ་ལྔ་བཅུའོ། །

[Block 3504 [HEADING]]
###### བ་ལང་སྤྱོད་གླིང། ^3-2-1-6-3-0

[Block 3505 [VERSE]]
བ་ལང་སྤྱོད་གླིང་ཟླུམ་པོ་སྟེ། །
སྟོང་ཕྲག་ཕྱེད་དང་བརྒྱད་ཡིན་ནོ། །
--- END BLOCKS ---
