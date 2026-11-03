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
བསམ་གཏན་སོགས། དབང་པོ་མོས་དང་ཁམས་ལ་ནི། དགུའོ། །

[Block 3852]
བསམ་གཏན་དང་། རྣམ་པར་ཐར་པ་དང་། ཏིང་ངེ་འཛིན་དང་། སྙོམས་པར་འཇུག་པ་མཁྱེན་པའི་སྟོབས་ནི་ཤེས་པ་དགུ་ཡིན་ཏེ། འགོག་པ་ཤེས་པ་མ་གཏོགས་སོ། །

[Block 3853]
དབང་པོ་མཆོག་དང་མཆོག་མ་ཡིན་པ་མཁྱེན་པའི་སྟོབས་དང་། མོས་པ་སྣ་ཚོགས་མཁྱེན་པའི་སྟོབས་དང་། ཁམས་སྣ་ཚོགས་མཁྱེན་པའི་སྟོབས་ཀྱང་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 3854]
ལམ་དག་ལ་བཅུའམ། འམ་ཞེས་བྱ་བའི་སྒྲ་ནི་དགུ་འམ་ཞེས་ལུགས་ཐ་དད་པའི་དོན་ཏེ། གལ་ཏེ་ལམ་དེ༌[^2717]འབྲས་བུ་དང་བཅས་པར་གཟུང༌[^2718]ན་ནི་ཐམས་ཅད་དུ་འགྲོ་བའི་ལམ་མཁྱེན་པའི་སྟོབས་ཤེས་པ་བཅུའོ།[^2719] །གལ་ཏེ་མ་ཡིན་ན་ནི་དགུ་སྟེ།

[Block 3855 [VERSE]]
འགོག་པ་ཤེས་པ་མ་གཏོགས་སོ། །
གཉིས་ནི་ཀུན་རྫོབ་ཤེས་པ་ཡིན། །

[Block 3856]
སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་མཁྱེན་པའི་སྟོབས་དང་། ཤི་འཕོ་བ་དང་། སྐྱེ་བ་མཁྱེན་པའི་སྟོབས་ནི་ཀུན་རྫོབ་ཤེས་པ་ཡིན་ནོ། །

[Block 3857]
ཟད་པ་དྲུག་གམ་བཅུ་ཡིན་ནོ། །

[Block 3858]
གལ་ཏེ་ཟག་པ་ཟད་པ་ཤེས་པ་འགོག་པ་ཤེས་པ༌[^2720]ཁོ་ན་ཞིག་ཡིན་ན་ནི༌[^2721]ཟག་པ་ཟད་པ་མཁྱེན་པའི་སྟོབས་ཤེས་པ་དྲུག་ཡིན་ཏེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། འགོག་པ་ཤེས་པ་དང་། ཟད་པ་ཤེས་པ་དང་། མི་སྐྱེ་བ་ཤེས་པ་དང་། ཀུན་རྫོབ་ཤེས་པ་རྣམས་སོ། །

[Block 3859]
འོན་ཏེ་ཟད་པ་ཤེས་པ་ཟག་པ་ཟད་པའི་རྒྱུད་ལ༌[^2722]ཡོད་པའི་ཤེས་པ་ཡིན་ན་ནི། དེས་ན་ཤེས་པ་བཅུ་ཡིན་ནོ། །

[Block 3860]
རང་བཞིན་བཤད་ཟིན་ཏོ། །

[Block 3861 [HEADING]]
##### ས། ^4-12-1-2-0

[Block 3862]
ད་ནི་ས་བརྗོད་པར་བྱ་སྟེ། སྔོན༌[^2723]གནས་ཤི་འཕོ་སྐྱེ་བའི༌[^2724]སྟོབས། །བསམ་གཏན་དག་ན། འཆི་འཕོ་བ་ནི་འཆི་འཕོ་བ་ཁོ་ན་སྟེ། སྔོན་གྱི་གནས་དང་། ཤི་འཕོ་དང༌[^2725]སྐྱེ་བ་མཁྱེན་པའི་སྟོབས་ནི་བསམ་གཏན་བཞིའི་ས་པ་ཡིན་ནོ། །

[Block 3863]
ལྷག་མ་ནི་ས་རྣམས་ཀུན་ན།[^2726] །སྟོབས་ལྷག་མ་ནི་ས་ཐམས་ཅད་ཀྱིས་བསྡུས་པ་ཡིན་ཏེ། དེ་དག་ཀྱང་འདོད་པའི་ཁམས་དང་། མི་ལྕོགས་པ༌[^2727]མེད་པ་དང་། བསམ་གཏན༌[^2728]ཁྱད་པར་ཅན་དང་། བསམ་གཏན་དང་། གཟུགས་མེད་པའོ། །

[Block 3864]
ཐམས་ཅད་ཀྱང་འཛམ་བུའི་གླིང་གི་སྐྱེས་པའི་རྟེན་ཅན་ཡིན་ཏེ། གཞན་དུ་སངས་རྒྱས་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3865 [HEADING]]
##### ཐུགས་ཀྱི་སྟོབས། ^4-12-1-3-0

[Block 3866]
ཤེས་པ་རྣམ་པ་བཅུ་པོ་འདི་ཉིད་གཞན་གྱི༌[^2729]ནི་སྟོབས་ཞེས་མི་བྱའི། སངས་རྒྱས་ཁོ་ནའི་སྟོབས་ཞེས་བྱའོ། །

[Block 3867]
ཅིའི་ཕྱིར། འདིའི་སྟོབས་གང་ཕྱིར་ཐོགས་མི་མངའ། །གང་གི༌[^2730]ཕྱིར་འདིའི་མཁྱེན་པ་ཤེས༌[^2731]བྱ་ཐམས་ཅད་ལ་ཐོགས་པ་མི་མངའ་བར་འཇུག་པ་དེའི་ཕྱིར་སྟོབས་ཡིན་ནོ། །

[Block 3868]
གཞན་དག་གི༌[^2732]ཤེས་པ་ནི་ལ་ལར་འདོད་ཀྱང་མི་འཇུག་པའི་ཕྱིར། ཐོགས་པ་ཡིན་པས་དེ་ནི་སྟོབས་ཞེས་བྱ་བའི་མིང་ཐོབ་པར༌[^2733]འོས་པ་མ་ཡིན་ཏེ། འདིར་དཔེ་ནི་གནས་བརྟན་ཤཱ་རིའི་བུས་རབ་ཏུ་འབྱུང་བར་འདོད་པའི་མི་ཕྱིར་བཏང་བ་དང་། བྱ་ཞིག་ཁྲས་གཙེས་པ་སྐྱེ་བ་ལ་སོགས་པའི་མཐའ་མ༌[^2734]ཤེས་པ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3869]
རེ་ཞིག་དེ་ལྟར་ན་མཁྱེན་པ་ལ་ཐོགས་པ་མི་མངའ་བའི་ཕྱིར། སངས་རྒྱས་རྣམས་ཀྱི་ཐུགས་ཀྱི་སྟོབས་ནི་ཤེས༌[^2735]བཞིན་དུ་མཐའ་ཡས་པ་ཡིན་ནོ། །

[Block 3870 [HEADING]]
##### སྐུའི་སྟོབས། ^4-12-1-4-0

[Block 3871]
སྐུ་ལ་སྲེད་མེད་བུ་ཡི་སྟོབས། །སངས་རྒྱས་ཀྱི་སྐུ་ལ་ནི་སྲེད་མེད་བུའི་སྟོབས་མངའོ་ཞེས་བརྗོད་དོ། །

[Block 3872]
གཞན་དག་ཚིགས་ན། གཞན་དག་ན་རེ་ཚིགས༌[^2736]དང་ཚིགས༌[^2737]ན་སྲེད་མེད་ཀྱི་བུའི་སྟོབས་མངའོ་ཞེས་ཟེར་རོ། །

[Block 3873]
བཙུན་པ་ན་རེ་སྐུའི་སྟོབས་ཀྱང་ཐུགས་ཀྱི་སྟོབས་བཞིན་དུ་མཐའ་ཡས་པ་ཡིན་ནོ། །

[Block 3874]
དེ་ལྟ་མ་ཡིན་ན་མཁྱེན་པའི་སྟོབས་མཐའ་ཡས་པས༌[^2738]བཟོད་པར་མི་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 3875]
སངས་རྒྱས་དང་རང་སངས་རྒྱས་དང་འཁོར་ལོས་སྒྱུར་བ་རྣམས་ཀྱི་ཚིགས་ཀྱི༌[^2739]མདུད་པ་དང་། ལུ་གུ་བརྒྱུད་དང་། གཟར༌[^2740]བུས་བཏབ་པ་ལྟ་བུ་དག་ཡིན་ནོ། །

[Block 3876]
སྲེད་མེད་ཀྱི་བུའི་སྟོབས་ཀྱི་ཚད་ཇི་ཙམ་ཞེ་ན། གླང་ཆེན་སོགས་བདུན་ཅུས་གླགས་པའི་སྟོབས་ཡིན་ནོ། །

[Block 3877]
གླང་པོ་ཆེ་ཕལ་པ་བཅུའི་སྟོབས་གང་ཡིན་པ་དེ་ནི་སྤོས་ཀྱི་གླང་པོ་ཆེ་གཅིག་གི་སྟོབས་ཡིན་ནོ། །

[Block 3878]
དེ་བཞིན་དུ་ཚན་པོ་ཆེ་ཆེན་པོ་དང་། རབ་གནོན་དང་། ཡན་ལག་མཆོག་དང་། སྟོབས་མཆོག་དང་། སྲེད་མེད་ཀྱི་བུ་རྣམས་གོང་ནས་གོང་དུ་བཅུ་འགྱུར་དུ་བསྐྱེད་དེ༌[^2741]བརྗོད་པར་བྱའོ། །

[Block 3879]
གཞན་དག་ན་རེ་གླང་པོ་ཆེ་ཕལ་པ་དང་། སྤོས་ཀྱི་གླང་པོ་ཆེ༌[^2742]དང་། ཚན་པོ་ཆེ་ཆེན་པོ་དང་། རབ་གནོན་དང་། ཡན་ལག་མཆོག་དང་། སྟོབས་མཆོག་རྣམས་གོང་ནས་གོང་དུ་བཅུ་འགྱུར་དུ་བསྐྱེད་པ༌[^2743]ནི་སྲེད་མེད་ཀྱི་བུའི་སྟོབས་ཀྱི་ཕྱེད་ཡིན་ལ། དེ་གཉིས་སུ་བསྒྱུར་བ་ནི་སྲེད་མེད་ཀྱི་བུའི་སྟོབས་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། ཇི་ལྟར་ཆེས་ཆེ་བ་དེ་ལྟར་རུང་ངོ་། །དེ་ནི་རེག་བྱའི་སྐྱེ་མཆེད་དོ། །

[Block 3880]
ལུས་ཀྱི་སྟོབས་དེ་ནི་ཐམས་ཅད་ཀྱང་རེག་བྱའི་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་འབྱུང་བ་ཆེན་པོའི་ཁྱད་པར་ཁོ་ན་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3881]
གཞན་དག་ན་རེ་བདུན་ལས་དོན་གཞན་དུ་གྱུར་པ་རྒྱུར་བྱས་པའི༌[^2744]གཟུགས་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3882]
སྟོབས་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 3883 [HEADING]]
#### མི་འཇིགས་པ་བཞི། ^4-12-2-0

[Block 3884 [VERSE]]
མི་འཇིགས་པ༌[^2745]ནི་རྣམ་པ་བཞི། །
མདོ་ལས་ཇི་སྐད༌[^2746]འབྱུང་བ༌[^2747]བཞིན་ནོ། །

[Block 3885]
མི་འཇིགས་པ༌[^2748]བཞི་པོ་དེ་དག་ཀྱང་། ཇི་ལྟར་སྟོབས་ནི་དང་པོ་དང་བཅུ་པ་གཉིས་པ༌[^2749]

[Block 3886]
བདུན་པ་བཞིན་ནོ། །

[Block 3887 [HEADING]]
##### མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པ། ^4-12-2-1-0

[Block 3888]
[^2750]གནས་དང་གནས་མ་ཡིན་པ་མཁྱེན་པའི་སྟོབས་ཇི་ལྟ༌[^2751]བར། ཀྱེ་མ་ང་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པར་གྱུར་པ་ལ་ཞེས་བྱ་བའི་མི་འཇིགས་པ༌[^2752]འདི་ཡང་དེ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 3889 [HEADING]]
##### ཟག་པ་ཟད་པ། ^4-12-2-2-0

[Block 3890]
ཟག་པ་ཟད་པ་མཁྱེན་པའི་སྟོབས་ཇི་ལྟ་བར༌[^2753]ཀྱེ་མ་ང༌[^2754]ཟག་པ་ཟད་པར་གྱུར་པ་ལ་ཞེས་བྱ་བའི་མི་འཇིགས་པ་འདི་ཡང་དེ་དང་འདྲའོ། །
--- END BLOCKS ---
