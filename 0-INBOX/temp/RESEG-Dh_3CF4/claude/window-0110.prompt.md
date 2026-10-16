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
[Block 3851]
བདེ་བའི་ཡོ་བྱད་དགག་པ་མེད་པ་ཞེས་བྱ་བ་ལ། དགག་པ་མེད་པ་ནི་བྱ་བ་ཐམས་ཅད་ཀྱི་ཐུན་མོང་དུ་གྱུར་པའི་ཕྱིར་ཏེ།[^2500] བདེ་བའི་ཡོ་བྱད་དང་།

[Block 3852 [VERSE]]
མི་འཇིགས་པ་བྱིན་པས་སོ། །
རྒྱལ་པོས་བྱ་རྣམས་ཀུན་ལ་བྱིན། །

[Block 3853]
ཞེས་བྱ་བ་འདིས་ནི་དགག་པ་མེད་པ་ཉིད་བསྟན་ཏོ། །

[Block 3854]
མི་འཇིགས་ཡོན་དང་བཅས་པའི་ཡིད་བཞིན་གྱི་མཚོ་གང་ཡིན་པ་དེ་ནི་མི་འཇིགས་ཡོན་དང་བཅས་པ་སྟེ། འདིས་ནི་བདེ་བའི་ཡོ་བྱད་ཉིད་བསྟན་ཏོ། །

[Block 3855]
སྤྲིན་གྱིས་བྱས་པའི་མུན་པ་ནི་སྤྲིན་གྱི་མུན་པའོ། །

[Block 3856]
སྤྲིན་གྱིས་བསྒྲིབས་པ་ཉིད་ཡོལ་བ་ཡིན་པས༌[^2501]སྤྲིན་གྱི་མུན་པ་ཡོལ་བ་དག་གོ། །

[Block 3857]
སྦྲིན་གྱི་མུན་པ་ཡོལ་བ་ལྟ་བུས་བསྒྲིབས་པ་གང་ཡིན་པ་དེས་ན༌[^2502]ཕྱོགས་རྣམས་ཏེ། མུན་པ་ཡོལ་བ་ལྟར་བསྒྲིབས་པ་མེད་པའི་ཕྱོགས་རྣམས་སོ། །

[Block 3858]
ཁ་བྱེ་བར་གྱུར་པའི་མེ་ཏོག་པདྨ་ནི་མེ་ཏོག་པདྨ་མང་པོ་ཁ་བྱེ་བའོ། །

[Block 3859]
དེས་མཛེས་པར་བྱས་པ་གང་ཡིན་པའི་མཚོ་དེ་ནི་མེ་ཏོག་པདྨ་མང་པོ་ཁ་བྱེ་བས་མཛེས་པར་གྱུར་པའོ། །

[Block 3860]
ཆུ་རྣམས་རབ་ཏུ་དང་ཞིང་ཡིད་དུ་འོང་བར་གྱུར་པ་ནི་ཆུ་རྣམས་རབ་ཏུ་དང་ཞིང་ཡིད་དུ་འོང་བའོ། །

[Block 3861]
རབ་ཏུ་འཕེལ་བར་ནུས་པ་དང་། རབ་ཏུ་ཚོགས་པ་དང་། རྒྱས་པར་གྱུར་པའི་འོད་ཟེར་རབ་ཏུ་འཕེལ་བའོ། །

[Block 3862]
རྣམ་པ་སྣ་ཚོགས་པའི་མེ་ཏོག་ནི་མེ་ཏོག་རྣམ་པ་མང་པོའོ། །

[Block 3863]
མེ་ཏོག་དང་རྣམ་པ་སྣ་ཚོགས་གཉིས་ཀྱི་ཕུན་སུམ་ཚོགས་པ་ནི་མེ་ཏོག་རྣམ་པ་མང་པོ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3864]
མེ་ཏོག་རྣམ་པ་མང་པོ་ཕུན་སུམ་ཚོགས་པ་ཉིད་རྒྱན་ཡིན་པས་མེ་ཏོག་རྣམ་པ་མང་པོ་ཕུན་སུམ་ཚོགས་པས་བརྒྱན་པ་དང་ལྡན་པའོ། །

[Block 3865]
བྱའི་ཚོགས་ཀྱི་ཅ་ཅོ་ནི༌[^2503]མང་པོའི་སྒྲའོ། །

[Block 3866]
བྱ་མང་པོའི་སྒྲ་སྒྲོགས་པ་ནི་སྒྲ་འབྱིན་པའོ། །

[Block 3867]
རླབས་རྣམས་ཀྱི་ཕྲེང་བ་བཀོད་པ་ནི་རླབས་ཀྱི་ཕྲེང་བ་འཁྲིགས་པའོ། །

[Block 3868]
དེས་བྱས་པ་གང་ཡིན་པ་དེ་ནི་རླབས་ཀྱི་ཕྲེང་བས་བསིལ་བར་བྱས་པ་སྟེ། སེར་བུ་བསིལ༌[^2504]ཞིང་གྲང་བ་ལྡན་པ་གང་ཡིན་པ་དེས་སོ། །

[Block 3869]
དྲི་ཞིམ་པོ་དང་ངད་ལྡན་པ་གང་ཡིན་པ་དེ་ནི་དྲི་ཞིམ་པོའི་ངད་ལྡན་བའོ། །

[Block 3870]
མེ་ཏོག་པདྨ་དང་ཨུཏྤ་ལ་རྣམས་ཀྱི་དྲི་ཞིམ་པོའི་ངད་ལྡང་བ་ནི་མེ་ཏོག་པདྨ་དང་། ཨུཏྤ་ལའི་དྲི་ཞིམ་པོའི་ངད་ལྡང་བའོ། །

[Block 3871]
ཁོ་ར་ཁོར་ཡུག་ཏུ་འཕྲོ་བའི་མེ་ཏོག་པདྨ་དང་། ཨུཏྤ་ལའི་དྲི་ཞིམ་པོའི་ངད་ལྡང་བ་དེ་ནི་ཁོ་ར་ཁོར་ཡུག་ཏུ་མེ་ཏོག་པདྨ་དང་། ཨུཏྤ་ལའི་དྲི་ཞིམ་པོའི་ངད་ལྡང་བའོ། །

[Block 3872]
རང་གི་ངང་པའི་ཚོགས་རྣམས་ཀྱི་རྗེས་སུ་དྲན་པའམ། རང་གི་ངང་པའི་ཚོགས་ལ་རྗེས་སུ་དྲན་པ་ནི་རང་གི་ངང་པའི་ཚོགས་རྣམས་རྗེས་སུ་དྲན་པའོ། །

[Block 3873]
ཇི་ལྟར་ན་རང་གི་ངང་བའི་ཚོགས་རྣམས་རྗེས་སུ་དྲན་པར་གྱུར་ཅེ་ན། སྨྲས་པ། ཨེ་མའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་། འཇིག་རྟེན་པ་ནི་ཕལ་ཆེར་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 3874]
ནམ་ཡང་ཕྱིའི་བདེ་བར་ནི་མི་འགྱུར་མོད་ཀྱི། རྒྱུའི་མིང་འབྲས་བུ་ལ་བཏགས༌[^2505]ནས་བདེ་བའི་རྒྱུ་ནི་ཐུན་མོང་ཡིན་ཏེ། གང་སྐྱེ་པོ་ཐམས་ཅད་ཀྱི་ཐུན་མོང་དུ་ལོངས་སྤྱོད་པའོ། །

[Block 3875]
གལ་ཏེ་སྐྱེ་བོ་ཀུན་གྱི་ཐུན་མོང་གི་བདེ་བའི་རྒྱུ༌[^2506]ཡིན་ན་ནི་སེར་སྣ་འབྱུང་བར་འགྱུར་ཏེ། དངོས་པོ་འདི་ཀུན་དུ་འཛིན་པ་ཡིན་ནོ། །

[Block 3876]
དེ་བས་ན་ཐོག་མར་མཛའ་བཤེས་དྲན་པར༌[^2507]འགྱུར་བ་ཡིན་ཏེ། དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར་སྨྲས་པའོ། །

[Block 3877]
[^2508]བྱམས་ཤིང་རྗེས་སུ་ཆགས་པའི་ཕྱིར་ཏེ། བྱམས་ཤིང་རྗེས་སུ་ཆགས་པའི་རྒྱུ་དེས་སོ། །

[Block 3878]
སྤྱི་ཡི་བདེ་བ་མྱོང་ནས་ནི། །ཞེས་བྱ་བ་ནི་རྐྱེན་ལས་སྐྱེས་བར་གྱུར་པའི་བད་བ་ནི་སྤྱིའི་ཞེས་བརྗོད་དོ། །

[Block 3879]
ཡང་ན་བདེ་བའི་རྒྱུ་ལ་འབྲས་བུ་བཏགས་པ་སྟེ། རྒྱུ་ལ་འབྲས་བུ་བདེ་བ་བཏགས་ནས་སྤྱི་ཞེས་སྨོས་པས་ནི་བྱེ་བྲག་མེད་པ་སྟེ། ཐམས་ཅད་ཀྱི་ཐུན་མོང་དུ་ལོངས་སྤྱོད་པའི༌[^2509]ཕྱིར་གང་གཅིག་ཉིད་ཀྱི་བདེ་བའི་རྒྱུར་གྱུར་པ་བཞིན་དུ་དེ་ལས༌[^2510]གཞན་དག་གི་ཡང་ངོ་། །བྱམས་པའི་རྗེས་སུ་འགྲོ་བ་ནི་བྱམས་ཤིང༌[^2511]རྗེས་སུ་ཆགས་པའོ། །

[Block 3880]
དེས་ན་བྱམས་པ་སྟེ། གང་ལ་རྗེས་སུ་ཆགས་པ་དེས་བྱམས་ཤིང་རྗེས་སུ་ཆགས་པའི་རྒྱུས་སོ། །

[Block 3881]
དེ་ན་ཞེས་བྱ་བ་ནི་ཡིད་བཞིན་གྱི་མཚོ་ནའོ། །

[Block 3882]
ཇི་སྲིད་འདོད་པ་ཞེས་བྱ་བ་ནི་ཇི་ཙམ་འདོད་པའོ། །

[Block 3883]
འཁོད་ནས་ཞེས་བྱ་བ་ནི་ལོངས་སྤྱད་ནས་སོ། །

[Block 3884]
དབྱར་གྱི་དུས་ལ་བབས་ཞེས་བྱ་བ་ལས་བརྩམས་ཏེ། གློག་རྣམས་གཡོ་བ་ནི་གློག་འགྱུ་བ་དང་། [^2512]གློག་འགྱུ་བའི་མཚོན་ཆ་འདེབས་པ་འདྲ་བ་གང་ཡིན་པ་དེ་ནི་གློག་འགྱུ་བ་མཚོན་ཆ་འདེབས་པ་འདྲ་བའོ། །

[Block 3885]
དེ་ལ་ཡོངས་སུ་རྫོགས་པ་རྨ་བྱའི་མདོངས་ནི་རྨ་བྱའི་མདོངས༌[^2513]རྒྱས་པའོ། །

[Block 3886]
དེས་མཛེས་པ་གང་ཡིན་པ་དེ་ནི་རྨ་བྱའི་མདོངས་མཛེས་པར་གྱུར་པའོ། །

[Block 3887]
དེ་དག་གི་ཅོང་ཅོང་གི་སྒྲ་འབྱིན་པ་ནི་རྨ་བྱའི་སྒྲ་ཅོང་ཅོང་དུ་འབྱིན་པའོ། །

[Block 3888]
དེས་མགུ་བར་བྱེད་པ་ནི་སྒྲ་བསྒྲགས་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3889]
གར་གྱི་བྱེད་པ་ནི་གར་བྱེད་པ་སྟེ། དེ་དག་བྱེད་པའོ། །

[Block 3890]
ཕྲ་མོ་ཉིད་བྱ་ཡིན་པས་བྲན་ནོ། །
--- END BLOCKS ---
