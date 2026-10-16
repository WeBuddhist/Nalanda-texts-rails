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
[Block 3256]
དེ་ཡང་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་དང་། འཇིག་རྟེན་ཕ་རོལ་གྱི་བདེ་བ་ཡིན་ནོ། །

[Block 3257]
དེ་ཉིད་སྨྲས་པ། ངའི་ལུང༌[^2077]ལ་ཞེས་བྱ་བ༌[^2078]ནི་མཐོ་རིས་སུ་འགྲོ་བར་བྱེད་པ་སྟེ། འཇིག་རྟེན་ཕ་རོལ་གྱི་བདེ་བ་ཐོབ་པར་བྱེད་པའོ། །

[Block 3258]
ཡང་ན་བདེ་བ་དེ་ཡང་འཐོབ། །ཅེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཉིད་ཀྱི་ཡིན་ནོ། །

[Block 3259]
ང་ཡི་ལུང་ལ་བརྟེན་ཞེས་བྱ་བ་འདི་ནི་འཇིག་རྟེན་ཕ་རོལ་ལ་བདེ་བ་འཐོབ་པའི་ཚིག་གོ །སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་བུམ་པའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 3260 [HEADING]]
## རྒྱལ་རིགས་ཕྱུག་པོའི་སྐྱེས་པའི་རབས། ^19-0

[Block 3261]
ཚུལ་ཁྲིམས་ཀྱི་གཉེན་པོར་འགྱུར་ཞིང་གནོད་པ་ཞེས་བྱ་བ་ལ་འདིར་གཉེན་པོར་ཞེས༌[^2079]སྨོས་པ་ནི་ཚུལ་ཁྲིམས་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་སུ་གཟུང་སྟེ། ཚུལ་ཁྲིམས་ཀྱི་མི་མཐུན་པ་ཡིན་པས་དེས་ན་གནོད་པ་ཡང་ཡིན་ནོ། །

[Block 3262]
ཕྱུག་པོའི་རིགས་འཚོ་བའི་ཚུལ་དང་སྤྱོད་པ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་འདིས་ནི་བདག་གི་སྐྱེ་བ་ཆོ་རིགས་ཕུན་སུམ་ཚོགས་པར་བསྟན་ཏོ། །

[Block 3263]
ཆོ་རིགས་མཐོན་པོ་ལ་དགའ་བ་རྣམས་ཀྱིས་གཉེན་བྱ་བར་གསོལ་བ་བཏབ་པ༌[^2080]ཞེས་བྱ་བ་འདི༌[^2081]ནི་འདས་པའི་དུས་ཀྱི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུའོ། །

[Block 3264]
དགེ་སྦྱོང་དང་བྲམ་ཟེ་རྣམས་ཀྱི་རེ་བའི་གནས་སུ་གྱུར་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་བཞིས་ནི་མ་འོངས་པའི་ལོངས་སྤྱོད་ཆེན་པོའི་འབྲས་བུའི་རྒྱུར་གྱུར་པ་སྟེ། སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 3265]
མ་འོངས་པའི་སྐྱེ་བར་གཡོག་འཁོར་མང་བའི་འབྲས་བུར་གྱུར་པ་སྟེ། སློང་བ་རྣམས་ཀྱིས་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བསྟན་ཏོ། །

[Block 3266]
དཔལ་གྱི་གཞིར་གྱུར་པ་ཞེས་བྱ་བས་ནི་འདས་པའི་ཚེ་རབས་ཀྱི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 3267]
རྒྱལ་པོས་བཀུར་སྟི་བྱ་ཞིང་ཕན་འདོགས་པའི་འོས་སུ་གྱུར་པ་ཞེས་བྱ་བ་ལ། ཕན་བཏགས་པ་ཞེས་བྱ་བ་ནི་གཡོག་འཁོར་གྱི་སྦྱིན་པ་ལ་སོགས་པའོ། །

[Block 3268]
བཀུར་སྟི་ནི་གདུགས་ལ་སོགས་པ་སྦྱིན་པའོ། །

[Block 3269]
འཇིག་རྟེན་པས་མངོན་པར་བཀུར་བ་ཞེས་བྱ་བ་དང་དེ་གཉིས་ཀྱིས་ནི་འདས་པའི་སྐྱེ་བའི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 3270]
དེ་བཞིན་དུ་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པའི་མཚན་ཉིད་དོ། །

[Block 3271]
བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ཡང་རྣམ་པ་གསུམ་ལས་ལོངས་སྤྱོད་ཆེན་པོའི་བདག་ཉིད་དང་། འཁོར་བར་གཡོག་འཁོར་ཕུན་སུམ་ཚོགས་པའི་མཚན་ཉིད་ནི་རྒྱལ་པོའི་རིགས་དང་། ཕྱུག་པོའི་རིགས་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 3272]
འཇིག་རྟེན་པས༌[^2082]བསྔགས་པའི་རིག་པའི་གནས་རྣམས་ལ་ནི་བསླབས། སྒྱུ་རྩལ་གྱི་ཐབས་རྣམ་པ་སྣ་ཚོགས་ལ་ནི་བློ་གསལ་བར་གྱུར་ཞེས་བྱ་བ་འདིས་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 3273]
ལུས་བྱད་བཟང་པོ་སྐྱེ་བོའི་མིག་ཏུ་སྡུག །ཅེས་བྱ་བ་འདིས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 3274]
ཆོས་དང་མི་འགལ་བར་འཇིག་རྟེན་གྱི་ཚུལ་ལ་མཁས་པས༌[^2083]ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པ་དང་། བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་འཇུག་པའོ། །

[Block 3275]
འཇིག་རྟེན་པ་རྣམས་ཀྱི་ནང་མི་བཞིན་དུ༌[^2084]སྙིང་ལ་ཆགས་པར་གྱུར་ཏོ་ཞེས་བྱ་བ་འདིས་ནི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུའོ། །

[Block 3276]
གཞན་བསོད་ནམས་ཀྱི་ཚོགས་ཐམས་ཅད་ནི་ཆོ་རིགས་མཐོ་བའི་ཁྱད་པར་ཉིད་ཀྱིས་བསྟན་ཏེ་ཡང་མི་བརྗོད་དོ། །

[Block 3277]
[^2085]སྐྱོན་དང་ཡོན་ཏན་གཉིས་བརྟག་པ་ནི་སྐྱོན་དང་ཡོན་ཏན་ལ་བརྟགས་པ་སྟེ། སྐྱོན་དང་ཡོན་ཏན་ལ་བརྟེན་པ་དང་། སྐྱོན་དང་ཡོན་ཏན་ལ་སྨྲ་བའོ། །

[Block 3278]
སྐྱོན་དང་ཡོན་ཏན་ལ་བརྟགས་ནས་ནང་མིའམ་ཕྱི་མི་རྣམས་ཀྱིས་བཀུར་སྟིའམ་སྨད་པར་བྱ་བ་ཡིན་ཏེ། སྐྱོན་ལ་བརྟགས་ནས་ནི་ནང་མི་འམ་ཕྱི་མི་གང་ཡང་རུང་བས་བཀུར་བ་མ་ཡིན་པའི་གནས་སུ་འགྱུར་རོ། །

[Block 3279]
དེ་སྔོན་རབ་ཏུ་བྱུང་བ་ལ་གོམས་པར་བྱས་པས་ཞེས་བྱ་བ་ནི་ཚེ་རབས་སྔ་མ་ལ་འདྲིས་པར་བྱས་པའི༌[^2086]ཕྱིར་རོ། །

[Block 3280]
རབ་ཏུ་བྱུང་བ་ལ་གོམས་པར་བྱས་པས་ཞེས་བྱ་བ་འདིས་ནི་རྒྱུའི༌[^2087]འབྲས་བུ་སྟོན་ཏོ། །

[Block 3281]
ཚོལ་བ་ཞེས་བྱ་བ་འདིས་ནི་རྐྱེན་གྱི་འབྲས་བུ་ལས་བརྩམས་པ་ཡིན་ཏེ། ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པའི་རྐྱེན་གྱིས་ཏེ། གཙོ་གཞན་གྱི་སྒྲའི་རྐྱེན་གྱིས་བདག་ཉིད་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 3282]
ཚོལ་བའི་སྡུག་བསྔལ་ཞེས་བྱ་བ་འདིས་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཉེས་དམིགས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 3283]
ཆོས་དང་འགལ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཡིན་ཏེ། ལོག་པའི་འཚོ་བ་སྟེ། ཁྱིམ་ན་གནས་ཤིང་མི་དགེ་བའི་ལས་ཀྱིས་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 3284]
བདེ་འབྱུང་གནས་ཞེས་བྱ་བ་ནི། འཇིག་རྟེན་གཉི་གར་བདེ་བ་འབྱུང་བ་ཉིད་ཡིན་ཏེ། དཀའ་ཐུབ་ཀྱི་ནགས་ཚལ་ན་ནི་ཚོལ་བ་དང་ཆོས་དང༌[^2088]འགལ་བའི་སྒྲུབ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3285]
ཁྱིམ་རྫས་དང་དབྱིག་བརྒྱ་སྟོང་དུ་མ་ཡོད་པ་དེ་ཡང་བཤེས་གཉེན་དང་། དགེ་སྦྱོང་དང་། བྲམ་ཟེ་དང་། ཕོངས་པ་དང་། སློང་བ་རྣམས་ལ་ཇི་ལྟར་རིགས་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་འོས་པར་བཏང་ཞིང་རབ་ཏུ་བྱུང་བ་སྟེ། ཚིག་འདིས་ནི་ཅི་ཞིག་སྟོན་པ་ཡིན་ཞེ་ན། ཐེག་པ་ཆེན་པོའི་ཡན་ལག་ཉིད་དུ་བསྟན་པ་སྟེ། གང་གི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ལོག་པར་སྤྱོད་པ་རྣམས་ལ་ཆགས་པ་མེད་པའི་ཕྱིར་ཏེ། དེ་བས་ན་སྦྱིན་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཐེག་པ་ཆེན་པོ་ཉིད་དོ། །

[Block 3286]
ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་ཀྱང་ཅི་རིགས་པར་ཐེག་པ་ཆེན་པོར་བརྗོད་དོ། །

[Block 3287]
དོན་རྣམ་པ་གཞན་དུ་ན་ཡུལ་རྣམས་ལ་ཆགས་པ་མེད་པའི་ལམ་ནི་སྦྱིན་པ་སྟེ། གཏོང་བ་ལ་གོམས༌[^2089]པས་ཆགས་པ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 3288]
དེ་ལྟར་སྦྱིན་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ལམ་མོ། །

[Block 3289]
དེ་བཞིན་དུ་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཞན་དག་ཀྱང༌[^2090]ཅི་རིགས་པར་བརྗོད་པར་བྱའོ། །

[Block 3290]
བསམ་གཏན་གྱི་ཡོན་ཏན་ལ་གོམས་པས༌[^2091]ཞེས་བྱ་བ་ནི་བསམ་གཏན་ཉིད་ཡོན་ཏན་ཡིན་ཏེ། ཡོན་ཏན་གཞན་ཐམས་ཅད་ཀྱི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3291]
དེ་བས་ན་དེ་ལ་གོམས་པའོ། །

[Block 3292]
རྣ་བ་དང་སྙིང་ཚིམ་པར་བྱེད་པའི་ཚིག་ཡིན་ཏེ། ཚིག་འདིའི་དོན་ནི་ཆོས་སྟོན་པ་ན་གྲོང་ཁྱེར་པའི་སྐད་དང་། སྙན་ཅིང་འཇེབས་པ་དང་། རྣམ་པར་གསལ་བ་དང་། རྣམ་པར་རིག་པར་བྱ་བ་དང་། མཉན་པར་འོས་པ་དང་། མི་གནས་པ་དང་། མི་མཐུན་པ་མེད་པ་དང་། མི་གསལ་བ་མེད་པ་སྟེ། གང་མདོའི་དོན༌[^2092]དེ་ཉིད་འདིར་ཡང་རྣ་བ་དང་སྙིང་ཚིམ་པར་བྱེད་པ་ཡིན་ཏེ། དེ་ཡང་གསུང་རྒྱ་ཆེ་བས་རྣར༌[^2093]སྙན་པས༌[^2094]ཡོངས་སུ་ཚིམ་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 3293]
རྣ་བ་དང་སྙིང་ཚིམ་པར་བྱེད་པ་ཞེས་བྱ་བ་འདིས་ནི་སྙན་པར་སྟོན་པ་ཡིན་ཏེ། སྐད་སྙན་ཅིང་འཁོར་ཡོངས་སུ་ཚིམ་པར་བྱེད་པས་གྲོང་ཁྱེར་པའི་སྙན་པའི་ཚིག་གིས་བརྗོད་དོ། །

[Block 3294]
དེ་བས་ན་རྣ་བ་དང་སྙིང་ཚིམ་པར་བྱེད་པས་ཞེས་བྱ་བ་འདིས་ནི་འཇེབས་པར་སྟོན་ཏེ། སྙན་ཅིང་འཇེབས་པའོ། །

[Block 3295]
དེས་ན་སྙིང་ཚིམ་པར་བྱེད་པའི་ཚིག་ལ་མཁས་པ་མངོན་པར་སྨྲ་བ་ཡིན་ཏེ། དེས་རྣམ་པར་རིག་པར་བྱ་བ་ཡིན་པར་དེ་བསྟན་ཏེ། གང་གི་ཕྱིར་རྣམ་པར་རིག་པར༌[^2095]བྱ་བ་ནི་བཤད་པའི་དོན་རྣམ་པར་ཤེས་པའི་བྱ་བ་ཡིན་པས་མཁས་པ་ཡིན་པར་མངོན་ནོ། །
--- END BLOCKS ---
