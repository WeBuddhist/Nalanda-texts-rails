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
[Block 3886]
དེ་བས་ན་ལྟུང་བ་ལས་ལྷག་པའི་དོན་ཉིད་ཀྱིས༌[^2667]འདི་ལྟར་བརྗོད་པ་ལ་སྐྱེས་པ་ཉིད་ཀྱིས་དེ་བཞིན་དུ་རིམ་པ་དུ་མ་བྱའོ་སྙམ་པའི་བསམ་པས་མཚམས་སྦྱར་བ་ལ་ཇི་སྲིད་དུ་རིམ་པ་རིགས་པ་ཉིད་བྱེད་པ་མངོན་པར་འདོད་པ་དེ་ཙམ་གྱི་རིམ་པ་ཉིད་ཀྱིས་ཞུགས་ལ་ཚད་གང་ཡིན་པ་དེ་ནི་དེ་ལས་ལྷག་པར་བྱེད་ན་ཡང་སྤང་བར་འགྱུར་བ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 3887]
རིམ་པ་དུ་མ་བྱའོ་སྙམ་པའི་བསམ་པ་མེད་དེ་རིམ་པ་གཅིག་པའོ༌[^2668]སྙམ་པ་ལས་གང་ཞིག་ཚད་འདི་ལས་ལྷག་པར་བྱེད་དམ། དྲས་ཏེ་བྱའོ་སྙམ་པའི་བསམ་པ་ཡོད་པས་གཞག་པར་བྱ་བ་ལ་འདི་ནི་ཚད་དོ། །

[Block 3888]
དེ་ལས་ལྷག་པ་མེད་པ་མ་བཅད་པའི་ངོ་བོ་ཉིད་ཀྱིས་ཚད་འདི་གང་ཡིན་པ་དེ་ལས་ལྷག་པར་བྱེད་ན་སྤང་བར་འགྱུར་བར་རིག་པར་བྱའོ། །

[Block 3889]
ངོས་ཇི་ཙམ་པ་དེ་ཙམ་གྱི་བསམ་པས་འཇུག་པ་དེ་ཙམ་ལ་དེའི་དོན་ཉིད་ཀྱིས༌[^2669]ཉེས་པར་གྱུར་པ་ཉིད་མེད་དོ། །

[Block 3890]
གང་གི་ཕྱིར་མངོན་པར་བརྟེན་པ་དང་རིག་པ་ལས་མ་འདས་པའི་དོན་ལ་ལྷག་པར་གྱུར་པ་ཉིད་མ་ཡིན་པའོ། །

[Block 3891]
གཞན་ཐམས་ཅད་ལ་ལྷག་པའི་དོན་ཉིད་ཐམས་ཅད་ལ་སོགས་པ་ལ་གནས་པས་ན་ཆོས་གོས་ཐམས་ཅད་ཀྱི་ཚད་ལ་མངོན་པར་གནས་པ་ཉིད་དོ། །

[Block 3892]
དེ་བས་ན་ཆེ་བ་དང་བར་མ་ཉིད་བྱེད་པའི་ལྷག་པར་གྱུར་པ་ལ་ཞེང་ངམ་ཆུར་ཉེས་པ་མི་བསྐྱེད་པའོ། །

[Block 3893]
ཞེང་ངམ་ཆུ་དག་ལས་གང་ཡང་རུང་བར་ལྷག་ན་བཅད་དེ་ལྔ་པོ་འཕགས་པ་ཉིད་ཀྱིས་མངོན་པར་འདོད་པའོ། །

[Block 3894]
རིགས་པ༌[^2670]ལས་མ་འདས་པའི་གོས་ཀྱི་ཕྱོགས་གཅིག་ཉིད་ཀྱི་མངོན་པར་བརྟེན་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 3895]
ཆུང་ངུ་དག་ནི་གཉིས་ཀ་དག་ལས་ཁྲུ་ཕྱེད་ཕྱེད་ཕྲི་བའོ་ཞེས་བྱ་བའི་ཁྲུ་གསུམ་མམ་ལྔ་ལས་གཉིས་ཀ་ལས་ཀྱང་ཁྲུ་ཕྱེད་ཕྱེད་དོར་ནས་ཆུང་བ་ཆོས་གོས༌[^2671]གསུམ་པོ་ལ་ཡང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3896]
འབྲིང་རྣམས་ཀྱི་ཚད་ནི་བར་མའོ་ཞེས་བྱ་བ་ནི་ཁྲུ་གསུམ་དང་ལྔ་དང་ཕྱེད་དང་གསུམ་དང་ཕྱེད་དང་ལྔ་གང་ཡིན་པ་དེའི་བར་མ་ནི་འབྲིང་པོ་སྟེ་དེ་ནི་འབྲིང་པོ་རྣམས་ཀྱི་ཚད་དོ། །

[Block 3897]
མཐང་གོས་ནི་དོ་དང་ལྔ་ཡང༌[^2672]ཡིན། དོ་དང་བཞི་ཡང་ཡིན་ནོ་འཁོར་གསུམ་ཁེབས་པ་ཡན་ཆད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དོ་དང་བཞི་མན་ཆད་ནས་བརྩམས་ཏེ་ཇི༌[^2673]སྲིད་འཁོར་གསུམ་ཁེབས་པ་ཉིད་ཡན་ཆད་ཀྱི་བར་རོ། །

[Block 3898]
ཁྲུའི་དོན་ནི་ལུས་ཀྱི་ཆ་བདུན་ལས་གཉིས་སོ་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ཁྲུའི་སྒྲའི་དོན་དུ་རིག་པར་བྱའོ། །

[Block 3899]
ལུས་དང་གྲུ་མོ་ནས་གུང་མོའི་རྩེ་མོའི་བར་ཡོད་པ་དེའི་ཚད་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3900]
གང་དུ་ལུས་ལ་ཁྲུའི་ཚད་ཐུང་བ་འམ་རིང་བ་ཉིད་དེ་དང་འབྲེལ་པ་ཉིད་ནི་ཆོ་ག་འདིའོ། །

[Block 3901]
མི་ཡོག་ན་རལ་ག་དཔུང་ཆད་བྱའོ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཡང༌[^2674]གང་གིས་ལུས་མི་ཁེབས་ན་རལ་ག་དཔུང་ཆད་བྱ་སྟེ་ཁེབས་པར་བསྒྲུབ་པར་བྱའོ། །

[Block 3902]
འདི་ནི་གཙོ་བོའི་ཐབས་ཏེ་དེ་བས་ན་འདིའི་འདི་བརྗོད་པར་བྱའོ། །

[Block 3903]
ཟླ་བས་སྤང་བ་རྣམ་པར་འབྱེད་པའོ།། །།

[Block 3904]
དེ་བས་དམན་པ་ནི་ཆུང་བ་དང་འདྲ་སྟེ་ཉེས་བྱས་སུ་འགྱུར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མཉམ་པ་ཀུན་ལས་འོག་ཏུ་གོས་གང་ཞིག་དུམ་བུར་གྱུར་པ་འམ་དུམ་བུར་མ་གྱུར་པ་ཆུང་བ་འཇོག་པ་ཟླ་བ་དང་འདྲ་བར་དེ་ལ་ཉེས་བྱས་སུ་གྱུར་པ་ཉིད་དོ། །

[Block 3905]
རེ་བ་ཡོད་པ་ལ་བྱིན་གྱིས་རློབ་པར༌[^2675]བྱེད་པ་མེད་པ་ཉིད་ལ་ཟླ་བ་གཅིག་འདས་ན་ཤིན་ཏུ་དམན་པ༌[^2676]འཆང་བ་ལ་ཉེས་བྱས་སོ། །

[Block 3906]
རེ་བ་མེད་པ་ལ་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་ཡོད༌[^2677]ལ་ཞག་བཅུ་འདའ་བར༌[^2678]བྱེད་ན་ཞེས་བྱ་བའི་དོན་དུའོ། །

[Block 3907]
འཁོར་གྱི་ཕྱེད་གཡོགས་པ་གང་ཞིག་དམན་པ་དེར་ཆོ་ག་འདི་ཞུགས་པའོ། །

[Block 3908]
འདི་ལས་འོག་མ་གང་ཡིན་པ་དེ་ལ་ཆོ་ག་བརྗོད་པར་བྱ་སྟེ། འཁོར་གྱི་ཕྱེད་མི་ཁེབས་པ་ནི་རེ་བ་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདིར་ལྟེ་བའི་རི་མོ་ལ་སོགས་པ་ནས་པུས་མོའི་ལྷ་ངའི་མཐར་ཐུག་པ་གང་ཡིན་པ་དེ་ནི་ཀན༌[^2679]ཐ་འཁོར་རོ། །

[Block 3909]
འདིའི་ཞེང་ལས་གང་གིས་ཕྱེད་མི་ཁེབས་པ་དེ་ལ་རེ་བ་མེད་པ་ཉིད་དོ། །

[Block 3910]
ཆ་གཅིག་པས་ཞག་བཅུའི་ཕྱོགས་ཉིད་དོ། །

[Block 3911]
ཞག་བཅུ་ལས་འདས་པར་བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3912]
འདིར་རེ་བ་ཤིན་ཏུ་ཆེ་བ་ཡང་དག་པར་གནས་པ་མ་ཡིན་ཏེ། དལ་གྱིས་འགྲོ་བས་ཡུལ་གཞན་དུ་ཕྱིན་པ་དང་འདྲ་བ་ཞེས་བྱ་བ་འདིས་ཤེས་པའོ། །

[Block 3913]
རུང་བ་མ་ཡིན་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་རེ་བ་མེད་པ་ཉིད་ཅེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 3914]
འདིར་གཞུང་ནི་གོས་ཇི་ལྟ་བུ་ཅིག་གཞག་པར་བགྱི། [^2680]རུང་བ་གང་ཡིན་པའོ། །

[Block 3915]
རུང་བ་ཇི་ལྟ་བུ་ལགས། བཅོམ་ལྡན་འདས་ཀྱིས་མ༌[^2681]བཀག་པ་གང་ཡིན་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3916]
གདོང་ཕྱིས་དང་ཆུ་ཚགས་དང་། སྟན་འཇམ་པོ་དང་དྲེའུ་རྔོག༌[^2682]ལ་སོགས་པའི་ཡོ་བྱད་ཀྱི་གོས་བྱིན་གྱིས་མ་བརླབས་པ་དག་གོ་ཞེས་བྱ་བ་ནི་གདོང་ཕྱིས་ལ་སོགས་པ་ཉིད་དུ་བྱིན་གྱིས་མ་བརླབས་པ་དེ་དག་ཀྱང་ཁ་བསྐང་བ་ལ་རེ་བ་མེད་པ་ཉིད་ཡིན་ཏེ། གཞན་རྩེ་གཅིག་པ་རྣམས་ལ༌[^2683]རེ་བ་ཡོད་པ་ཉིད་ལ་ཡང་དག་པར་གནས་པའི་ཕྱིར་གླགས་མི་རྙེད་པ་ཞག་བཅུ་ཉིད་ལ་འདི་བརྗོད་པ་སྟེ་ཡང་དག་པར་འགྱུར་བ་ཉིད་ཀྱང་འདིར་མེད་ན་མི་འབྱུང་བའི་ཕྱིར་གྲགས་པར་རིག་པར་བྱའོ། །

[Block 3917]
འདིར་གཞུང་ནི་ཡི་གེ་ཁ་ཅིག་ལས་ཡོ་བྱད་ཀྱི་གོས་བྱིན་གྱིས་མ་བརླབས་པ་ཞག་བཅུ་ལས་འདས་པ་སྤང་བར་འགྱུར་བ་ཉིད་ནི་གདོང་ཕྱིས་དང་ཆུ་ཚགས་དང་སྟན་འཇམ་དང་དྲེའུ་རྔོག་ལ་སོགས་པའི་ཡོ་བྱད་བྱིན་གྱིས་རློབ་པར༌[^2684]བྱེད་ན་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3918]
ཟླ་བས་སྤང་བ་ཞུ་བའོ།། །།

[Block 3919]
སྦྲུམ་མ་དབེན་པར་གཞག་གོ་ཞེས་བྱ་བ་ལ། སྦྲུམ་མ་ཞེས་བྱ་བ་ནི་མངལ་ན་བུ་ཡོད་པ་སྟེ་རབ་ཏུ་བྱུང་བ། སྦྲུམ་མ་མངལ་ན་བུ་ཡོད་པ་སྟེ་དབེན་པའི་ཕྱོགས་སུ་གཞག་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3920]
དེ་དགེ་སློང་མ་རྣམས་ཀྱིས༌[^2685]ཡལ་བར་མི་དོར་རོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་དབེན་པའི་ས་ཕྱོགས་ན་སྦྲུམ་མའི་གནས་བཅས་པ་དེར་འདི༌[^2686]བསྒྲུབ་ན་དགེ་སློང་མ་གཞན་རྣམས་ཀྱིས་ཡལ་བར་མི་དོར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3921]
དེ་ལ་ཟན་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྦྲུམ་མ་ལ་དགེ་སློང་མ་རྣམས་ཀྱིས་སོ། །

[Block 3922]
ཕ་མ་དག་ནས་བདུན་པ་ཚུན་ཆད་ལས་གང་ཡང་རུང་བ་སྔ་མ་གཅིག༌[^2687]ལས་སྐྱེས་པ་ཡང་ཉེ་དུ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་ཕ་མ་དག་ཅེས་བྱ་བ་ནི་ཕ་དང༌[^2688]མ་ནི་ཕ་མ་དག་གོ། །

[Block 3923]
འདིར་མའི་རྒྱུད་ཕའི་ཡན་ལག་དང་བཅས་པ་ལ་མའི་སྒྲའོ། །

[Block 3924]
ཕའི་སྒྲ་ཡང་མའི་ཡན་ལག་དང་བཅས་པ་ཕའི་རྒྱུད་ལ་ཕྲུགས་བདུན་དུ་གྱུར་པའི་ཕ་མ་དག་གིས་ཇི་སྲིད་དུ་གང་ཡང་རུང་བ་གཅིག༌[^2689]གིས་ཀྱང་ཕ་མ་དེ་དག་ལ་གཉིས་ཀ་དག་ཉིད་ཀྱིས་ནི་མ་ཡིན་ཏེ། གཅིག་སྔ་མ་ལས་སྐྱེས་པ་ཉིད་དང་མ་གཅིག་ལས་སྐྱེས་པ་ཉིད་དང་ཕ་གཅིག་ལས་སྐྱེས་པ་ཉིད་གང་ལ་ཡོད་པ་དེ་ནི་གཉེན་ཞེས་བྱ་བ་འདི་དག་གི་དོན་ཏོ། །

[Block 3925]
འཁྲུར་འཇུག་པའི་སྤང་བའི་བྱེད་པ་པོ་ཉིད་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དོན་མེད་ན་ཡང་འདུ་ཤེས་ནི་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་ཡིན་ཏེ་འདུ་ཤེས་ནི་གཙོ་ཆེར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
