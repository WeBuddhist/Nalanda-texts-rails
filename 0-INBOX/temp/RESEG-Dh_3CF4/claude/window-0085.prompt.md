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
[Block 2976]
དེ་བས་ན་ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པར་བྱའོ་ཞེས་བྱ་བ་ཡིན་ཏེ། སྲོག་གཅོད་པ་ལས་ལྡོག་པའི་མཚན་ཉིད་ཀྱི་ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པར་བྱའོ་ཞེས་པའོ། །

[Block 2977]
རང་བཞིན་གྱིས་ཤེས་རབ་རྣོ་བས་ཞེས་བྱ་བ་ནི་ཤེས་རབ་དང་སྙིང་རྗེ་རབ་ཏུ་བསྒོམས་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ནི་རིགས་ཀྱིས་ཤེས་རབ་ཤས་ཆེ་བ་ཡིན་པས་ཤེས་རབ་རྣོ་བ་ཞེས་སྨོས་སོ། །

[Block 2978]
རང་བཞིན་དང་རིགས་དང་། རྒྱུ་དང་ས་བོན་ཞེས་བྱ་བ་རྣམ་གྲངས་སོ། །

[Block 2979]
རང་བཞིན་གྱིས་ཤེས་རབ་རྣོ་བ་ནི་རིགས་ཀྱིས་གྲུབ་པའི་ཤེས་རབ་རྣོ་བའོ། །

[Block 2980]
གཙུག་ལག་ཁྱད་པར་ཅན་གང་དང་གང་། སྒྱུ་རྩལ་ཁྱད་པར་ཅན་གང་དང་གང་ཞེས་བྱ་བ་ལ། ཁྱད་པར་ཅན་སྨོས་པ་ནི་གཙུག་ལག་དང་སྒྱུ་རྩལ་གྱིས་སེམས་ཅན་རྗེས་སུ་བཟུང་བར༌[^1899]བྱེད་པ་ཡིན་ཏེ། སློབ་པར་འདོད་པ་དེ་ཡང་དག་པར་བསྟན་པའི་ཕྱིར་དེ་དང་དེ་དག་ལ་ཞེས་བྱ་བ་ཡིན་ཏེ། སྐྱེ་བོ་གཞན་པས་ལྷག་པར་འགྱུར། །ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་དྲི་མའི༌[^1900]ཤེས་རབ་ལས་ཀྱང་ལྷག་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏེ། ཤེས་རབ་རྣོ་ཞིང་སྐྱེ་བོ༌[^1901]གཞན་པས་ཞེས་བྱ་བས་ནི་ལྷན་ཅིག་སྐྱེས་པའི་ཤེས་རབ་ཀྱིས་ཀྱང་ལྷག་པར་འགྱུར་བ་ཡིན་ཏེ། གཞན་དག་གི་ཤེས་རབ་ནི་འབད་པ་ལས་བྱུང་བའི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2981]
ནར་མ་དང་གློ་བུར་ནི་ནར་མ་དང་གློ་བུར་རོ། །

[Block 2982]
འབྱུང་བར་འགྱུར་བའི་ལྟས་ནི་འབྱུང་བར་འགྱུར་བའི་ལྟས་སོ། །

[Block 2983]
འབྱུང་བའི་ལྟས་དང་མཚན་མ་ནི་འབྱུང་བའི་ལྟས་དང་མཚན་མ་སྟེ། ནར་མ་དང་གློ་བུར་དུ་འབྱུང་བའི་ལྟས་དང་མཚན་མ་གང་གིས་ཤེས་པ་ནི་ནར་མ་དང་གློ་བུར་དུ་འབྱུང་བའི་ལྟས་དང་མཚན་མ་ཤེས་པའོ། །

[Block 2984]
བདག་ཉིད་ཆེན་པོ་དེ་སྐར་མ་རྒྱུ་བ་ལ་མཁས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཇི་སྲིད་དུ་རྒྱ་མཚོའི་ཕྱོགས་ནི་ལེགས་པར་རྟོགས་ཞེས་བྱ་བས་ནི་ཤེས་རབ་ཀྱི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 2985]
དྲན་པ་དང་ལྡན་ཞིང་ལེ་ལོ་དང་གཉིད་ནི་ཆུང་ཞེས་བྱ་བས་ནི་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྟགས་བསྟན་ཏོ། །

[Block 2986]
གྲང་བ་དང་ཚ་བ་དང་ཆར་ལ་སོགས་པ་ལ་ཇི་མི་སྙམ་ཞེས་བྱ་བ་འདིས་ནི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྟགས་བསྟན་ཏོ། །

[Block 2987]
སོགས་པའི་ཞེས་སྨོས་པས་ནི་བཀྲེས་པ་དང་སྐོམ་པ་ལ་སོགས་པ་ལ་ཇི་མི་སྙམ་པར་གཟུང་ངོ་། །བག་ཆེ་ལ་ཞེས་བྱ་བས་ནི་བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྟགས་བསྟན་ཏོ། །

[Block 2988]
བརྟན་པ་དང་ལྡན༌[^1902]པའི་ཞེས་བྱ་བས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྟགས་བསྟན་ཏོ། །

[Block 2989]
སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཅི་ཡང་མི་བྱེད་པའི་ཕྱིར་རྟགས་སུ་མ་སྨོས་སོ། །

[Block 2990]
དྲང་བ་ལ་མཁས་པ་ནི་སྔོན་དུ་འགྲོ་བ་ལ་མཁས་པའོ། །

[Block 2991]
ལྡོག་པ་ལ་མཁས་པ་ནི་ཕྱིར་ནུར་བ་ལ་མཁས་པའོ། །

[Block 2992]
སོགས་པ་སྨོས་པས་ནི་ཐད་ཀར་འགྲོ་བ་ལ་སོགས་པ་ལ་མཁས་པའོ། །

[Block 2993]
ཡང་དག་པར་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡིན་པས་ལེགས་པར་ཕ་རོལ་ཏུ་ཕྱིན་པར་བྱེད་པ་སྟེ། འདོད་པའི་ཡུལ་དུ་ཕྱིན་པར་བྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2994]
ཡང་ན་དོན་རབ་ཏུ་འགྲུབ་པར་བྱེད་པའོ། །

[Block 2995]
འདོད་པ་ཞེས་བྱ་བ་ནི་གང་ཆས་པར༌[^1903]བརྩམས་པའོ། །

[Block 2996]
རྒས་པའི་དབང་གིས་ལྟ་བ་ཉམས་གྱུར་ཅིང་། །ཞེས་བྱ་བ་འདིས་ནི་གང་གོང་དུ་བསྟན་པའི་བདག་ཉིད་ཆེན་པོ་དེ་སྐར་མ་དང་རྒྱུ་སྐར་ལ་མཁས་པ་ཞེས་བྱ་བ་ནས། རྒྱ་མཚོའི་ཕྱོགས་ནི་ལེགས་པར་རྟོགས། །ཞེས་བྱ་བ་དེའི་ནུས་པ་མེད་པར་བསྟན་ཏོ། །

[Block 2997]
དྲན་པ་རབ་ཏུ་ཉམས་ཞེས་བྱ་བ་འདིས་ནི་གང་བསྟན་པའི་དྲན་པ་དང་ལྡན་ཞེས་བྱ་བ་དེ་མེད་པར་བསྟན་པའོ། །

[Block 2998]
བདག་གི་ལུས་ཀྱི་བྱ་བའང་ཉམ་ཆུང་ན། །ཞེས་བྱ་བ་འདིས་ནི་སྔར་བསྟན་པའི་ལེ་ལོ་དང་གཉིད་ནི་ཆུང་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་མེད་པར་བསྟན་ཏོ། །

[Block 2999]
ཁྱོད་ཀྱི་ལུས་ཀྱི་གནས་སྐབས་དེ་ལྟ་བུའོ། །

[Block 3000]
འཚལ་ཏེ་ཞེས་བྱ་བའི་ཚིག་གིས་ནི་དྲན་པ་དང་བློ་དེའི་གནས་སྐབས་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3001]
བགྲོད་དཀར༌[^1904]ཞེས་བྱ་བ་ནི་ཇི་ལྟ་བུའི་མཚན་ཉིད་ཅན་གྱི་རྒྱ་མཚོ་སྟེ། རབ་ཏུ་ཞེས་བྱ་བ་ནི་ཇི་སྙེད་ཀྱི་མཚན་ཉིད་ཅན་སྟོན་ཏོ། །

[Block 3002]
མཚོ་འཇིང༌[^1905]ནང་དུ་ཞུགས་ཞེས་བྱ་བ་ལ་ཇི་ལྟ་བུར་ཞེ་ན། རྣམ་པ་གསུམ་པའི་མཚན་ཉིད་ཅན་ཏེ། མདོག་དང་། འགྲམ་བལྟར་མི་སྣང་བ་དང་། གཏིང་དཔག་དཀའ་བ་སྟེ། དེ་གསུམ་ཡང་ཨནྡ་རྙིལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་བསྟན་པ་ཡིན་ནོ། །

[Block 3003]
ཉི་མའི་དཀྱིལ་འཁོར་ནི་ཉི་མའི་དཀྱིལ་འཁོར་རོ། །

[Block 3004]
དེའི་འོད་ནི་ཉི་མའི་དཀྱིལ་འཁོར་གྱི་འོད་དོ། །

[Block 3005]
ཆུང་ངུ་གྱུར་པ་ནི་ཉི་མའི་དཀྱིལ་འཁོར་གྱི་འོད་དེ། གང་དེ་ཆུང་ངུ་གྱུར་པ་དེ་ནི་ཉི་མའི་དཀྱིལ་འཁོར་གྱི་འོད་ཆུང་ངུ་གྱུར་པའོ། །

[Block 3006]
དེ་ལ་ལྟས་ངན་ཆེན་པོ་ཞེས་བྱ་བ་ནི་ལྟས་འབྱུང་བ་སྟེ། ཤིན་ཏུ་ཆེ་བ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། རླབས་ནི་རྣམ་པར་འཁྲུག་ཅིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། རྒྱུ་གསུམ་གྱི་ལྟས་ངན་ཆེན་པོ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 3007]
མདོག་དང་། སྒྲ་དང་། དབྱིབས་སོ། །

[Block 3008]
དེ་ཡང་དབྱིབས་ནི།

[Block 3009 [VERSE]]
ཆུ་ཀུན་ཐ་མལ་འདུག་ལས་རབ་ཏུ་གཡོས། །
ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱིས་བསྟན་ཏོ། །
ཆུ་ཀུན་ཐ་མལ་འདུག་ལས་རབ་ཏུ་གཡོས། །

[Block 3010]
ཞེས་བྱ་བ་ཉིད་བསྟན་པའི་ཕྱིར། ལྟས་ངན་གློ་བུར་ལངས་པའི་རླུང་གིས་ཞེས་བྱ་བའི་ཚིགས་བཅད༌[^1906]སྨོས་ཏེ། ཆུ་ཐ་མལ་པར་འདུག་པ་ལས་རབ་ཏུ་བསྐྱེད་པ༌[^1907]ཉིད་ནི་སྒྲ་སྒྲོགས་པ་དང་། ཚད་དང་། ཤུགས་དང་། འགྲོས་ཀྱིས་བསྟན་པ་ཡིན་ཏེ། དཀྲུགས་པ༌[^1908]ནི་འགྲོས་ཏེ། སྣ་ཚོགས་སུ་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 3011]
འཇིང༌[^1909]ནི་རབ་ཏུ་འཇིགས་སུ་རུང་བ་སྟེ། དེའི་རབ་ཏུ་འཇིགས་སུ་རུང་བ་ནི། གློག་ཕྲན་འགྱུ་བའི་འོད་འབར་ལྕེ་གཡོ་བ། །ཞེས་བྱ་བའི་ཚིགས༌[^1910]བཅད་གསུམ་གྱིས་བསྟན་ཏེ། དེའི་རབ་ཏུ་འཇིགས་སུ་རུང་བ་ནི་སྤྲིན་དང་བ་དང་། སྣང་བ་ནུབ་པ་དང་། དེའི་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་ལྟས་ངན་འབྱུང་བ་སྟོན་པས་སོ། །

[Block 3012]
གློག་ཕྲན་འགྱུ་བ་ཞེས་བྱ་བ་འདིའི་བསྡུས་པའི་དོན་ནི་མདོག་དང་ཚད་དང་། སྒྲ་དང་།[^1911] སྤྲིན་གྱི་ཁྱད་པར་ཏེ། གློག་ཕྲན་འགྱུ་བ་འོད་འབར་ལྕེ་གཡོ་བ། །ཞེས་བྱ་བ་དང་།

[Block 3013 [VERSE]]
སྔོ་བ་ཞེས་བྱ་བས་ནི་མདོག་བསྟན་ཏོ། །
སྤྲིན་གྱིས་ཉི་མའི་ལམ་ཡང་བསྒྲིབས་པར་འགྱུར། །

[Block 3014]
ཞེས་བྱ་བ་འདིས་ནི་ཚད་བསྟན་ཏོ། །

[Block 3015]
སེམས་སྟོབས་ཡོན་ཏན་བསམ་པ་སྟོན༌[^1912]ཞེས་བྱ་བ་ནི་སྙིང་སྟོབས་ཉིད་ཀྱི་ཡོན་ཏན་གང་ཡིན་པ་དེ་ནི་སེམས་སྟོབས་ཡོན་ཏན་ཏེ། སེམས་སྟོབས་ཀྱི་ཡོན་ཏན་ཇི་ལྟ་བ་བཞིན་དུ་བསམ་པ་ནི་འདོད་པ་སྟེ་སྟོན་ཅིང་སྨྲ་བའོ། །
--- END BLOCKS ---
