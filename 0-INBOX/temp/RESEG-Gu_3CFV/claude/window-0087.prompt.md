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
[Block 3046]
མ་མཐོང་བ་གནས་པའི་སྐྱེས་པ་ཡོད་པ་དང་། མེད་པ་ཉིད་ཤེས་པར་བྱ་བའི་ཕྱིར་བརྟགས་པ་འདིའོ། །

[Block 3047]
དེ་ལྟ་བས་ན་སྐྱབས་ཡོད་པ་ལ་སོ་སོར་བརྟག་པར་བྱ་བ་མ་བྱས་པར་མཚན་མོ་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3048]
གང་ལ་བསླབ་པའི་གཞི་གསུམ་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གནས་ཁང་དུ་དགེ་སློང་མ་གཞན་མེད་པར་མཚན་མོ་འདའ་བར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཚན་མོ་གནས་ཁང་དུ་དགེ་སློང་མ་གཞན་མེད་པར་གཅིག་པུ་ཉལ་ཞིང་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3049]
འདིར་གནས་ཁང་ཞེས་སྨོས་པ་ནི་དཔེ་ཙམ་དུ་ཟད་ཀྱི། གཡོགས་པའི་ཕྱོགས་ཀྱི་གནས་ཁང་གཞན་ཡང་བསྡུས་པ་ཡིན་ནོ། །

[Block 3050]
དུས་འདེབས་པ་དང་སྐྱེས་པས་གནོད་པར་འགྱུར་བའི་གཞན་དང་ལྷན་ཅིག་ཉེས་དམིགས་མཉམ་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3051]
ཇི་ལྟར་འོས་པས་རྗེས་སུ་འགྲོ་བར་གྱུར་ཅིག་ཅེས་བྱ་བས་དེའི་གནས་ཁང་ཞེས་སྨོས་སོ། །

[Block 3052]
མཚན་མོ་གསུམ་པའི༌[^1954]ཆ་གསུམ་པ་ལ་ལྟུང་བྱེད་དོ། །

[Block 3053]
མདུན་རོལ་དུ་ནི་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3054]
ཉིན་མཚན་གྱི་དང་པོ་མ་ཡིན་པ་ལ་མཚན་མོ་མཐའི་སྐད་ཅིག་ལ་ནི་ཡོད་པ་ཉིད་དང་སྦྱར་བ༌[^1955]ཙམ་ཉིད་བདེན་པ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 3055]
དེ་ཤི་བ་ལ་སོགས་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི། དགེ་སློང་མ་གཞན་དེ་ནི༌[^1956]ཤི་བའམ། བབས་སམ། ཡུལ་གཞན་ལ་སོགས་པར་སོང་ངམ། རྐྱེན་གཞན་གྱིས་མེད་པར་གྱུར་ན་གཅིག་པུ་གནས་ཁང་དུ་མཚན་མོ་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བ་མེད་པ་ཡིན་ཏེ། དེས་ནི་མི་འདོད་བཞིན་དུ་བྲལ་བར་བསྟན་ཏོ། །

[Block 3056]
གནོད་པར་འགྱུར་བའི་སྒོ་སྤང་བའི་ལྟུང་བྱེད་གསུམ་མོ། །

[Block 3057]
གང་ལ་མལ་གཅིག་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མ་དང་ཁྲི་གཅིག་ལ་སྟན་གཅིག་རེག་པ་དང་བཅས་ཤིང་མཚན་མོ་ཉལ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་དགེ་སློང་མ་ཞེས་བྱ་བ༌[^1957]ནི་བུད་མེད་དུ་གྱུར་པ་ལ་དཔེ་ཙམ་དུ་ཟད་དེ་བུད་མེད་གཞན་ལ་ནི་ཤིན་ཏུ་སྐྱོན་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3058]
རེག་པ་དང་བཅས་ཤིང་ཞེས་བྱ་བ་ནི་རེག་པ་དང་བཅས་ཤིང་འཇུག་པ་ལ་རེག་པ་དང་བཅས་ཤིང་ཞེས་བྱ་བའི་བསྡུ་བའོ། །

[Block 3059]
མ་རེག་པར་ཉལ་བ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་སྨོས་པའི་ཕྱིར་འདིར་རེག་པ་ལ་ནི་ཁ་ན་མ་ཐོ་བ་རྫོགས་པའོ། །

[Block 3060]
དེ་དང་ངམ་དུ་མ་དང་ལྷན་ཅིག་ཀྱང་རུང་སྟེ། གཏུར་བུ་ལ་སོགས་པས་བར་དུ་བཅད་ཅིང་དྲན་པ་ཉེ་བར་གཞག༌[^1958]སྟེ། ལུས་ཀྱི་རེག་པའི་རོ་མྱང་བ་མེད་པར་ཁྲི་མི་འཁྲུལ་བ་ཐ་མལ་པའམ་སྟན་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ལ། དེ་དང་ངམ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མས་སོ། །

[Block 3061]
དུ་མ་དང་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་གཅིག་པུ་ཉིད་དུ་མ་ཟད་ཀྱི། འོན་ཀྱང་གཉིས་ལ་སོགས་པས་ཀྱང་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅི་དེ་ཙམ་ཉིད་ཀྱིས་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་བར་དུ་བཅད་ཅིང་ཞེས་བྱ་བ༌[^1959]སྨོས་སོ། །

[Block 3062]
གང་གིས་ཤེ་ན་དེའི་ཕྱིར་གཏུར་བུ་ལ་སོགས་པས་ཞེས་བྱ་བ་སྨོས་ཏེ། གཏུར་བུ་དང་ལྷུང་བཟེད་དང་འདྲ་བ༌[^1960]ལ་སོགས་པས་བར་དུ་བཅད་པ་བྱས་པར་འགྱུར་བ་ལའོ། །

[Block 3063]
དྲན་པ་ཉེ་བར་གཞག་སྟེ་ཞེས་བྱ་བ་ཀུན་དུ་ལོངས་འཆོས་པར་གཏོགས་པའི་ཉེ་བའི་ཉོན་མོངས་པའི་སྐྱོན་ཉེ་བར་བསལ་བའི་ཕྱིར་བསླབ་པའི་གཞི་འདིའོ། །

[Block 3064]
དེ་བས་ན་དྲན་པའི་རྣམ་པ་ལྟ་བུར༌[^1961]ལོངས་འཆོས་པར་གཏོགས་པའི་ཉེ་བའི་ཉོན་མོངས་པ་དེའི་ཆ་ཅན་ལ་ཉེ་བར་ལྟུང་བ་བསལ་བར་ནུས་པའི་དྲན་པ་དེ་ལྟ་བུས་དྲན་པ་ཉེ་བར་གཞག་གོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3065]
ལུས་ཀྱི་རེག་པའི་རོ་མྱང་བ་མེད་པར་ཞེས་བྱ་བ་ནི། ལུས་ཀྱི་རེག་པ་ཡོངས་སུ་བསལ་བ་ནི་བར་དུ་གཅོད་པའི་དོན་ཏོ། །

[Block 3066]
དེའི་ཕྱིར་བར་དུ་གཅོད་པ་ལས་ཡང་རྐྱེན་གྱི་དབང་གིས་བརྒྱ་ལ༌[^1962]ལུས་རེག་པར་འགྱུར་ན་ལུས་རེག་པ་དེའི་རོ་མྱང་བ་མེད་པར་བྱེད་པའོ། །གང་དུ་འདི་དང་ལྷན་ཅིག་ལྟུང་བར་མི་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཁྲི་མི་འཁྲུལ་བའམ། ཐ་མལ་པའམ། སྟན་ཞེས་བྱ་སྟེ། འདི་རྣམས་ལ་ལྷན་ཅིག་ཉལ་བ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 3067]
འདིར་གཞུང་ནི་ཁྲི་མི་འགུལ་བ་ལ་གཏུར་བུ་ལ་སོགས་པས་བར་དུ་བཅད་ཅིང་དྲན་པ་ཉེ་བར་གཞག་སྟེ། ལུས་ཀྱི་རེག་པའི་རོ་མྱང་བ་མེད་པ་དང་། ཁྲི་ཐ་མལ་པ་དང་དེ་བཞིན་དུ་སྟན་ལ་ཡང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3068]
ཡོད་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི། མལ་སོ་སོར་བྱ་བའི་སྐབས་ཡོད་ན་བར་དུ་བཅད་པ་ལ་སོགས་པས་ཀྱང་ལྷན་ཅིག་ཉལ་བ་ལ་ནི་ཉེས་བྱས་ཀྱི་ཁ་ན་མ་ཐོ་བར་འགྱུར་རོ། །

[Block 3069]
ལོངས་སྤྱོད་ཅིང་གནས་པ་བཏང་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 3070]
[^1963]

[Block 3071]
འདི་མན་ཆད་ནི་བྱི་དོར་བྱེད་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་བརྒྱད་སྟོན་ཏེ། གང་ལ་དེ་རྣམས་ཀྱི་དང་པོར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རང་གི༌[^1964]ལུས་ཀྱི་དྲིལ་ཕྱིས་དགེ་སློང་མས་བྱེད་དུ་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3072]
བསླབ་པའི་གཞི་གཉིས་པ་ནི། དགེ་སློབ་མ་ལའོ་ཞེས་བྱ་བ་སྟེ། རང་གི་ཡན་ལག་གི་དྲིལ་ཕྱིས་དགེ་སློབ་མ་ལ་བྱེད་དུ་འཇུག་པ་ཞེས་བྱ་བ་ལྔ་པོ་དེ་རྣམས་ལས༌[^1965]ཡང་རིག་པར་བྱའོ། །

[Block 3073]
གསུམ་པ་ནི་དགེ་ཚུལ་མས་སོ། །

[Block 3074]
བཞི་པ་ནི་ཁྱིམ་པ་མོའོ། །

[Block 3075]
ལྔ་པ་ནི་མུ་སྟེགས་ཅན་མའོ༌[^1966]ཞེས་བྱ་བ་ལ། རང་གི༌[^1967]ཡན་ལག་རྣམས་ལ་དྲིལ་ཕྱིས་བྱེད་དུ་འཇུག་ན་ལྟུང་བྱེད་དོ། །ཅིའི་ཕྱིར་སླར་དེ་ཐ་དད་པས་བཅའ་བ་མཛད་ཅེ་ན། འདིར་ལྟུང་བ་ལྔ་པོ་རྣམས་ལ་འཇུག་པའི་ཕྱིར་ཚིག་ཙམ་གྱི་རྗེས་སུ་འཇུག་པ་ཉིད་ཀྱིས་དགེ་སློང་མས་རང་གི་ལུས་ལ་དྲི་མ་ཕྱི་བར་མི་བྱའོ་ཞེས་བྱ་བའི་བཅས་པ་འདི་ཡོད་པ་ལ། དགེ་སློང་མ་ལ་སོགས་པ་རྣམས་ཀྱིས་རང་གི་ལུས་ལ་དྲི་མ་ཕྱིས་པ་ལ་ཉེས་པ་མེད་དོ། །

[Block 3076]
དེ་ལྟར་འཇུག་པར་གྱུར༌[^1968]པ་རྣམས་ལ་ལྔ་པོ་འདི་རྣམས་བཅས་པའོ། །

[Block 3077]
དྲུག་པ་བྱི་དོར་བྱེད་པའི་ལྟུང་བྱེད་ནི་བཀྲུ་བཤལ་བྱེད་དུ་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྟེ། འདིར་བུད་མེད་ཀྱིས་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 3078]
སྐྱེས་པས་བྱེད་དུ་བཅུག་པ་ལ་རེག་པའི་ཁ་ན་མ་ཐོ་བ་ཤིན་ཏུ་ལྕི་བར་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 3079]
རྫས་གཞན་གང་ཡང་རུང་བས་དྲིལ་ཕྱིས་བྱས་པ་ལ་སྔ་མ་ལྔ་པོ་རྣམས་བཅས་པ་ཡིན་ནོ། །

[Block 3080]
འདི་ནི་ཆུ་འབའ་ཞིག་གིས་བཀྲུ་བཤལ་བྱེད་དུ་འཇུག་པ་ལས་བཅས་པ་ཡིན་ཏེ། བྱེ་བྲག་ནི་དེ་ཡིན་ནོ། །

[Block 3081]
དེ་ལྟར་ཡང་བཀྲུ་བཤལ་བྱེད་དུ་འཛུད༌[^1969]ན་ཞེས་གསུངས་པ་དེའི་རྣམ་པར་འབྱེད་པ་ནི་ཆུས་བཀྲུ་བཤལ་བྱེད་ན་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3082]
བསླབ་པའི་གཞི་བདུན་པ་ནི་རྫས་དྲི་ཞིམ་པོས་རང་གི་ལུས་སྐུད་པ་ལའོ་ཞེས་བྱ་བ་ལ། །འདིར་དྲི་དག་གིས་ཞེས་བྱ་བ་ནི། མདོའི་ཚིག་གོ། །

[Block 3083]
རྫས་དྲི་ཞིམ་པོ་དག་གིས་ཞེས་བྱ་བ་ནི་རྣམ་པར་འབྱེད་པའི་ཚིག་གོ། །

[Block 3084]
གང་ལ་ལྟུང་བྱེད་བརྒྱད་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་འབྲུ་མར་གྱི་ཚིགས་མས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གི་ལུས་སྐུད་པ་ལའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3085]
འདིར་རང་གི་བྱེད་པའི་རྫས་དྲི་ཞིམ་པོས་རང་གི་ལུས་ལ་སྐུད་པ་ནི་དྲིལ་ཕྱིས་ཞེས་སྨོས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
