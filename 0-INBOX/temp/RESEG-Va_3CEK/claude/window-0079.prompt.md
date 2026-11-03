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
[Block 2766 [HEADING]]
#### མཐར་གྱིས་འཇུག་པ། ^3-2-8-0

[Block 2767]
མཐར་གྱིས་འཇུག་པ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་རེ་ཞིག་འདི་རྣམ་པར་གཞག་པར་བྱའོ། །

[Block 2768 [HEADING]]
##### ས་དང་ས་ན་ཉེས་པ་རྣམ་པ་དགུ། ^3-2-8-1-0

[Block 2769]
ཇི་ལྟར་འདོད་པའི་ཁམས་ཀྱི་ཉོན་མོངས་པ་རྣམ་པ་དགུ་པོ་དེ་དག་བསྟན་པ་དེ་བཞིན་དུ།

[Block 2770 [VERSE]]
ས་དང་ས་ན་ཉེས་རྣམ་དགུ། །
སྲིད་པའི་རྩེ་མོའི་བར་དུའོ། །

[Block 2771]
ཉེས་པ་རྣམས་ཇི་ལྟ་བ་དེ་བཞིན་དུ་ཡང༌[^1903]ཡོན་ཏན་རྣམས་ས༌[^1904]དང་ས་ན་དེའི་གཉེན་པོ་བར་ཆད་མེད་པའི་ལམ་དང་རྣམ་པར་གྲོལ་བའི་ལམ་ཞེས་བྱ་བ༌[^1905]ཡོན་ཏན་ཡང་རྣམ་པ་དགུ་དགུ་ཁོ་ན་ཡོད་དོ། ། ཇི་ལྟར་བྱས་པས་ཤེ་ན།

[Block 2772 [VERSE]]
ཆུང་དང་འབྲིང་དང་ཆེ་རྣམས་ཀྱི། །
ཆུང་ངུ་ལ་སོགས་ཐ་དད་ཕྱིར། །
རྩ་བའི་རྣམ་པ་གསུམ་སྟེ།
ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོའོ། །

[Block 2773]
དེ་དག་རེ་རེ་ཞིང་ཡང་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོ་ཉིད་ཀྱིས༌[^1906]རྣམ་པ་གསུམ་ཡིན་པའི་ཕྱིར་དགུར་རྣམ་པར་གཞག་སྟེ། ཆུང་ངུའི་ཆུང་ངུའི་རྣམ་པ་དང་། ཆུང་ངུའི༌[^1907]འབྲིང་དང་། ཆུང་ངུའི་ཆེན་པོ་དང་། འབྲིང་གི་ཆུང་ངུ་དང་། འབྲིང་གི་འབྲིང་དང་། འབྲིང་གི་ཆེན་པོ་དང་། ཆེན་པོའི་ཆུང་ངུ་དང་། ཆེན་པོའི་འབྲིང་དང་། ཆེན་པོའི་ཆེན་པོའོ། །

[Block 2774]
དེ་ལ་ལམ་ཆུང་ངུའི་ཆུང་ངུས་ནི་ཉོན་མོངས་པ་ཆེན་པོའི་ཆེན་པོ་སྤོང་ལ། དེ་བཞིན་དུ་ལམ་ཆེན་པོའི་ཆེན་པོས་ནི་ཉོན་མོངས་པ་ཆུང་ངུའི་ཆུང་ངུའི་བར་དུ་སྤོང་སྟེ།

[Block 2775]
དང་པོ་ཁོ་ནར་ལམ་ཆེན་པོ་མི་སྲིད་པའི་ཕྱིར་དང་། ལམ་ཆེན་པོ་སྐྱེས༌[^1908]པ་ལ་ཉོན་མོངས་པ་ཆེན་པོ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2776]
གོས་ལ་དྲི་མ་ཆེ་ལོང་ནི་སྔར་འཁྲུ་ལ༌[^1909]ཕྲ་མོ་ནི་ཕྱིས་འཁྲུ་བ་དང་། མུན་པ་ཆེ་ལོང་ནི་སྣང་བ་ཆུང་ངུས་འཇོམས་ལ་ཕྲ་མོ་ནི་ཆེན་པོས་སེལ་ཞེས་བྱ་བ་འདི་ནི་དཔེའི་རྣམ་པ་ཡིན་ནོ། །

[Block 2777]
འཕགས་པའི་ལམ་སྐད་ཅིག་མ་ཆུང་ངུས་ཀྱང་འཁོར་བ་ཐོག་མ་མེད་པ་ནས༌[^1910]བརྒྱུད་པས་སྤེལ་བའི་ཉོན་མོངས་པ་ཆེན་པོ་རྣམས་རྩ་བ་ནས་མེད་པར་བྱེད་པའི་ཕྱིར་ཆོས་དཀར་པོ་རྣམས་ནི་སྟོབས་དང་ལྡན་པ་ཡིན་ལ། ནག་པོ་རྣམས་ནི་སྟོབས་ཆུང་བ་ཡིན་ཏེ། ཡུན་རིང་པོ་ནས་བསགས་པའི་སྐྱོན་རྣམས་སྨན་ཏྲི་བྱིད༌[^1911]ཐུན་གཅིག་གིས་འབྱིན་པ་ལྟ་བུ་དང་། མར་མེ་སྐད་ཅིག་མ་ཆུང་ངུས་མུན་པ་ཆེན་པོ་འཇོམས་པ་བཞིན་ནོ། །

[Block 2778 [HEADING]]
##### མཆོག་ཏུ་ཐོགས་ན་ལན་བདུན་པ། ^3-2-8-2-0

[Block 2779]
དེ་ལྟར་ཉོན་མོངས་པ་རྣམས་པ༌[^1912]དགུ་པོ་དེ་དག་ཐམས་ཅད་དུ།

[Block 2780 [VERSE]]
འབྲས་གནས་བསྒོམ་སྤང་བྱ་མ་ཟད། །
རེ་ལྟར་ཐོགས་ན་ལན་བདུན་པ། །

[Block 2781]
འབྲས་བུ་ལ་གནས་པ་གང་ཞིག་གིས། བསྒོམ་པས༌[^1913]སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་གཅིག་ཀྱང་མ་སྤངས་པ་དེ་ནི་རྒྱུན་དུ་ཞུགས་པ་ཡིན་ལ། ཚེ་བདུན་གྱི་བར་དུ་སྐྱེ་བས་ན་རེ་ལྟར་ཐོགས་ན་ལན་བདུན་པའོ། །

[Block 2782]
ཐམས་ཅད་དུ་ནི་ལན་བདུན་པ་མ་ཡིན་པས་རེ་ལྟར་ཐོགས་ན་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་ཀྱི་ཐ་ཤལ་བའོ། །

[Block 2783]
མདོ་ལས།

[Block 2784]
མཆོག་ཏུ་ཐོགས་ན་ལན་བདུན་པ་ཞེས་འབྱུང་བ་ནི་དེ༌[^1914]མཆོག་ཏུ་ཐོགས་ན་སྐྱེ་བ་ལན་བདུན་པ༌[^1915]ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། མཆོག་ཅེས་བྱ་བའི་སྒྲ་ནི་རབ་ཏུའོ། །

[Block 2785]
མྱ་ངན་ལས་འདས་པའི་རྒྱུན་ནི་ལམ་སྟེ། དེས་ན་དེར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 2786]
འདི་ནི་དེར་ཞུགས་ཤིང་ཕྱིན་ལ་སོན་པས་ན་རྒྱུན་དུ་ཞུགས་པ་ཡིན་ནོ། །ཇི་ལྟར་ན་ཞུགས་པ་ཡིན། གལ་ཏེ་ལམ་དང་པོ་ཐོབ་པའི་ཕྱིར་རོ་ཞེ་ན་ནི་བརྒྱད་པ་ཡང་ཡིན་པར་འགྱུར་རོ། །

[Block 2787]
གལ་ཏེ་འབྲས་བུ་དང་པོ་ཐོབ་པའི་ཕྱིར་རོ་ཞེ་ན་ནི་ཕལ་ཆེར་ལས་འདོད་ཆགས་དང་བྲལ་བ་ཡང་ཡིན་པར་འགྱུར་ལ། འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་ཡང་ཡིན་པར་འགྱུར་རོ། །

[Block 2788]
འབྲས་བུ་ཐམས་ཅད་ཐོབ༌[^1916]པའི་དབང་དུ་བྱས་ནས་འབྲས་བུ་དང་པོ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 2789]
[^1917]ཅིའི་ཕྱིར་དེ་ཁོ་ན་ཡིན་ལ་བརྒྱད་པ་ནི་མ་ཡིན་ཞེ་ན། ལམ་ལ་རྗེས་སུ་ཤེས་པ་ལ་ནི་ཞུགས་པ་དང་འབྲས་བུའི་ལམ་ཐོབ་པའི་ཕྱིར་དང་། མཐོང་བ་དང་བསྒོམ་པའི་ལམ་ཐོབ་པའི་ཕྱིར་དང་། རྒྱུན་ཐམས་ཅད་མངོན་པར་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 2790]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་དེ་ནི་དེ་ལས་གཞན་པ་སྐྱེ་བའི་སྲིད་པ་བདུན་དང་སྲིད་པ་བར་མ་བདུན་དུ་མི་རྣམས་ཀྱི་ནང་དུ་ཉིང་མཚམས་སྦྱོར་བར་བྱེད་ལ་དེ་བཞིན་དུ་ལྷ་དག་གི་ནང་དུ་ཡང་ཉིང་མཚམས་སྦྱོར་བར་བྱེད་དོ། །

[Block 2791]
[^1918]དེ་ལྟར་ན་སྲིད་པ་ཉི་ཤུ་རྩ་བརྒྱད་ཀྱི་བར་དུ་ཉིང་མཚམས་སྦྱོར་བར་བྱེད་དོ། །

[Block 2792]
སྲིད་པ་བདུན་ཚན་དུ་འདྲ་བའི་ཕྱིར་མཆོག་ཏུ་ཐོགས་ན་ལན་བདུན་པ་ཞེས་བཤད་དེ། གནས་བདུན་ལ་མཁས་པ་ཞེས་བྱ་བ་དང་། [^1919]འདབ་མ་བདུན་པ་ཞེས་བྱ་བ་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2793]
འོ་ན་གང་མདོ་ལས།

[Block 2794]
གང་ཟག་ལྟ་བ་ཕུན་སུམ་ཚོགས་པ་སྲིད་པ་བརྒྱད་པ་མངོན་པར་འགྲུབ་པ་གང་ཡིན་པ་དེ་ནི་གནས་མ་ཡིན་ཞིང་གོ་སྐབས་མེད་དེ་འདི་ནི་གནས་མེད་དོ་ཞེས་གསུངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། འགྲོ་བ་གཅིག་ཏུ་དགོངས་པ་ཡིན་ནོ། །

[Block 2795]
འོན་ཏེ་སྒྲ་ཇི་བཞིན་དུ་བརྟགས༌[^1920]ན་ནི་སྲིད་པ་བར་མ་ཡང་ཡོད་པར་མི་འགྱུར་རོ། །

[Block 2796]
དེ་ལྟ་ན་ཡང་སྲིད་པའི་རྩེ་མོའི་བར་དུ་གོང་དུ་འཕོ་བ་འགྲོ་བ་གཅིག་ཏུ་སྐྱེ་བའི་སྲིད་པ་བརྒྱད་པར་མི་འགྱུར་རོ་ཞེ་ན། འདོད་པའི་ཁམས་ལས་དགོངས་ཏེ་གསུངས་པའི་ཕྱིར་ཉེས་པ་མེད་དོ། །

[Block 2797]
འདི་ལ་ཤེས་པར་བྱེད་པ་མདོའམ་རིགས་པ་ཅི་ཞིག་ཡོད། ལྷ་དང་མི་དག་གི་ནང་ནས༌[^1921]སོར་ལན་བདུན་སྐྱེའི་གཉི་གའི་ནང་དུ་ལན་བདུན་མ་ཡིན་པ་ཉིད་དོ་ཞེས་བྱ་བ་འདི་ལ་ཡང་ཤེས་པར་བྱེད་པ་ཅི་ཞིག་ཡོད་དེ། འདི་སྐད་དུ་ལྷ་རྣམས་དང་མི་རྣམས་ཀྱི་ནང་དུ༌[^1922]ལན་བདུན་ཞེས་འབྱུང་ངོ་ཞེ་ན། འོད་སྲུངས་པ་རྣམས་ལྷ་རྣམས་སུ་ལན་བདུན། མི་རྣམས་སུ་ལན་བདུན་ཞེས་སོ་སོར་ཡང་འདོན་པས་འདི་ལ་མངོན་པར་ཞེན་པར་མི་བྱའོ། །

[Block 2798]
གང་ཞིག་མི་དག་གི་ནང་དུ་རྒྱུན་དུ་ཞུགས་པར་གྱུར་པ་དེ་ནི་དེ་ཁོ་ནར་འོངས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདས༌[^1923]ལ། གང་ཞིག་ལྷ་དག་གི་ནང་དུ་རྒྱུན་དུ་ཞུགས་པར་གྱུར་པ་དེ་ནི་དེ་ཁོ་ནར་འོངས་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའོ། །ཅིའི་ཕྱིར་སྲིད་པ་བརྒྱད་པ་མངོན་པར་མི་འགྲུབ་ཅེ་ན། དུས་དེ་སྲིད་ཀྱིས་གདོན་མི་ཟ་བར་རྒྱུད་ཡོངས་སུ་སྨིན་པའི་ཕྱིར་རོ། །

[Block 2799]
ལམ་དེ་ནི་དེ་འདྲ་སྟེ། སྦྲུལ་གོམ་པ་བདུན་པས་ཟིན་པ་ལྟ་བུ་དང་། རིམས་ཉིན་བཞི་པ་བཞིན་ནོ། །

[Block 2800]
ཀུན་ཏུ་སྦྱོར་བ་བདུན་པོ་ཐ་མའི་ཆ་དང་མཐུན་པ་གཉིས་དང་། གོང་མའི་ཆ་དང་མཐུན་པ་ལྔ་ལུས་པའི་ཡང་ཕྱིར་རོ། །

[Block 2801]
བར་སྐབས་སུ་ཡང་འཕགས་པའི་ལམ་མངོན་དུ་བྱེད་ཅིང་ཡོངས་སུ་མྱ་ངན་ལས་མི་འདའ་སྟེ། དེ་སྲིད་དུ་སྲིད་པ་མྱོང་བར་འགྱུར་བའི་ལས་ཀྱི་སྟོབས་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 2802]
སངས་རྒྱས་འབྱུང་བ་མེད་ན་ཁྱིམ་པ་ཁོ་ནར་དགྲ་བཅོམ་པ་ཉིད་འཐོབ་ན༌[^1924]ཁྱིམ་ན་ནི་མི་གནས་སོ། །

[Block 2803]
ཆོས་ཉིད་ཀྱིས་འཐོབ་པའི་དགེ་སློང་གི་མཚན་མ་ཡང་འཐོབ་བོ། །

[Block 2804]
གཞན་དག་ན་རེ། །དགེ་སྦྱོང་གཞན་གྱི་མཚན་མས་སོ་ཞེས་ཟེར་རོ། །ཅིའི་ཕྱིར་ལོག་པར་ལྟུང་བའི་ཆོས་ཅན་མ་ཡིན་ཞེ་ན། །དེར་འགྲོ་བའི་ལས་མི་སོགས་པའི༌[^1925]ཕྱིར་དང་། བསགས་པ་ཡང་སྦྱོར་བ་དང་བསམ་པ་དག་པའི་སྒོ་ནས་དགེ་བའི་རྩ་བ་སྟོབས་དང་ལྡན་པས་བསྒོས་པའི་ཕྱིར་རྒྱུད་རྣམ་པར་སྨིན་པ་དང་། མི་མཐུན་པ་བྱས་པའི་ཕྱིར་རོ། །

[Block 2805]
ངན་སོང་དུ་ངེས་པའི་ལས་ཡོད་ན་ནི་དེས་བཟོད་པ་ཡང་བསྐྱེད་པར་མི་འགྱུར་རོ། །
--- END BLOCKS ---
