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

[Block 3296]
མ་ཁེངས་པ་ཞེས་བྱ་བས་ནི་མཉན་པར་འོས་པ་བསྟན་ཏེ། མཉན་པའི་དོན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3297]
མ་ཁེངས་པ་དང་། རྙེད་པ་ལ་རེ་བའི་བརྐམ་པ་དང་ཞུམ་པ་མེད་པ་ཞེས་བྱ་བ་འདིས་ནི་མི་གནས་པ་བསྟན་ཏེ། རྙེད་པ་ལ་སོགས་པའི་འདོད་པ་དང་བྲལ་བས་དེ་མི་གནས་པའོ། །

[Block 3298]
དེས་དེ་ཉིད་རྙེད་པ་ལ་སོགས་པ་མེད་པའོ། །

[Block 3299]
དུལ་ཞིང་གཟི་བྱིན་ཆེ་བ་དང་། །ཇི་ལྟར་རིགས་པར་འཇམ་པོར་སྨྲ་ཞིང་གསལ་བ་ཞེས་བྱ་བ་འདི་གཉིས་ཀྱིས་ནི་མི༌[^2096]མཐུན་པ་མེད་པར་བསྟན་ཏེ། ཇི་ལྟར་གཡོག་འཁོར་འཇུག་པ་དེས་དུལ་ཞིང་གཟི་བྱིན་ཆེ་བ་ཡང་དེས་འཇུག་སྟེ། ཇི་ལྟར་རིགས་པར་འཇམ་པོར་སྨྲ་ཞིང་གསལ་བའི་ཕྱིར་སྙན་པའི་སྐྱེ་བོ་རྣམས་ལ་མི་མཐུན་པ་མེད་པ་ཡིན་ནོ། །

[Block 3300]
དེ་བས་ན་ཇི་ལྟར་གཡོག་འཁོར་གྱི་འཇུག་པ་དེས་ཆོས་དང་ཆོས་མ་ཡིན་པ་རབ་ཏུ་འབྱེད་པ་མཁས་པ་ཞེས་བྱ་བ་ཡིན་ཏེ། འདིས་ནི་མི་གསལ་བ་མེད་པ༌[^2097]བསྟན་ཏེ། དཔག་ཏུ་མེད་པའི་སྤོབས་པ་དང་ལྡན་པའི་ཕྱིར་མི་གསལ་བ༌[^2098]མེད་པ་ཡིན་ཏེ། དེས་ན་ཡང་ཆོས་དང་ཆོས་མ་ཡིན་པ་རབ་ཏུ་འབྱེད་པ་ལ་མཁས་པ་ཉིད་དོ། །

[Block 3301]
དེ་ལྟར་མདོའི་ཚིག་གི་རྗེས་སུ་འབྲང་བ་ཡིན་ཏེ། ཚིག་བརྒྱད་པོ་འདིའི་གོ་རིམས་ཀྱིས་ཡང་དག་པར་བསྟན་ཏེ། འདིས་ནི་ངག་གི་ལས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 3302]
རབ་ཏུ་བྱུང་བའི་སྤྱོད་ཚུལ་བཟང་པོ་དང་། ཡ་རབས་རྣམས་དགའ་བའི་སྤྱོད་པས༌[^2099]ཞེས་བྱ་བ་འདིས༌[^2100]ལུས་ཀྱི་ལས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 3303]
ཆོ་རིགས་བཙུན་པ་ལས་རབ་ཏུ་བྱུང་བར་ཤེས་ནས་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྔར་བསྟན་པའི་རྒྱལ་རིགས་ཕྱུག༌[^2101]པོའི་རིགས་ཞེས་བྱ་བ་ལ་སོགས་པའི་རིགས་ཀྱི་ཁྱད་པར་གྱིས་སོ། །

[Block 3304]
རབ་ཏུ་བྱུང་བར་ཤེས་ནས་ཞེས་བྱ་བ་དེ་ཡང་སྔར་བསྟན་པ་ཡིན་ཏེ། དེའི་ཕ་མ་གཉིས་ཚེ་འདས་པས༌[^2102]ཞེས་བྱ་བ་ལ་སོགས་པའི་རིམ་པས་རབ་ཏུ་བྱུང་བར་ཤེས་པར་བྱའོ། །

[Block 3305]
རིགས་དང་གཟུགས་ཀྱི་ཡོན་ཏན་ལས། །ཞེས་བྱ༌[^2103]བ་ལ། རིགས་ཀྱི་ཡོན་ཏན་རྣམས་ནི་སྔར་བཤད་པ་དག་གོ། །

[Block 3306]
གཟུགས་ཀྱི་ཡོན་ཏན་ཡང་སྔར་བཞིན་བཤད་པ་ཡིན་ཏེ། ལུས་བྱད་བཟང་པོ་སྐྱེ་བོའི་མིག་ཏུ་སྡུག །ཅེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 3307]
ས་གཞི་བཟང་པོ་ཞེས་བྱ་བ་ནི་ཡང་ཐོག་གི་རྩིག་པ་དཀར་གྱིས་བསྐུས་པ་ལ་ཟླ་བའི་འོད་ཟེར་བབ་པ་བཞིན་ནོ། །

[Block 3308]
ན་ཚོད་འདི་ཙམ་ལ་ཆོ་རིགས་ལ་ཡང་མི་ལྟ་བར་འདི་ལྟར་རབ་ཏུ་བྱུང་ཞེས་བྱ་བ་ནི་བུ་སྐྱེད༌[^2104]ནས་ན་ཚོད་རྒུད་པ་ལ་རབ་ཏུ་འབྱུང་བར་བྱ་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3309]
སོང་ཞེས་བྱ་བ་ནི་འགྲོ་བས་འགྱུར་བ་སྟེ། དེས་ན་འདི་ཉིད་ལས་ཆོས་བརྙེས༌[^2105]པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 3310]
ཅིའི་ཕྱིར་ཞེས་བྱ་བ་ནི་རྒྱུ་གཞན་གྱི་ཕྱིར་རོ། །

[Block 3311]
གཞན་གྱི་དྲིང་ལ་ལྟོས༌[^2106]ཤིང་སློང༌[^2107]མོ་སྤྱོད། །ཅེས་བྱ་བ་དང་། གོས་ངན་པ་གྱོན་པ་དང་། བས་མཐའི་ས་ན་ལུས་ནི་བསྒྱུར་ཏེ་བོར། །ཞེས་བྱ་བ་འདི་དག་གིས་ཟས་བསོད་སྙོམས་དང་གནས་མལ་དང་བྲལ་བར་སྟོན་ཏེ། འདིས་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་མེད་པར་བྱས་པའི་ཕྱིར་རོ། །

[Block 3312]
དབུལ་པོའི་ལུས་ཞེས་བྱ་བ་དང་། ངན་པ་བཞིན་དུ་སྐྱེ་བོ་ཀུན་གྱིས༌[^2108]སྨད། །ཅེས་བྱ་བ་འདིས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ༌[^2109]རིགས་ལ་སོགས་པ་ཕུན་སུམ་ཚོགས་པར་འབྱོར་ཀྱང་སྨད་པ་ཉིད་དུ་གྱུར་པ་སྟེ། གསུམ་པོ་འདི་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 3313]
གཉེན་གྱི་སྐྱེ་བོ་དང་བྲལ་བ༌[^2110]དང་། གཉེན་བཤེས་རྣམས་དང་བྲལ་བ་ཞེས་བྱ་བ་འདིས་ནི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་གཡོག་འཁོར་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 3314]
བུ་མཆོག་ཡིད་ལ་བསམ་པ༌[^2111]གྲུབ་པར་གྱིས། །ཞེས་བྱ་བ་ནི་དེ༌[^2112]སུའི་ཡིད་ལ་བསམ་པ་འགྲུབ་པ༌[^2113]ཡིན་ཞེ་ན། དབུལ་པོའི་ལུས་སུ་གྱུར་པ་ཉིད་ཀྱིས་ཏེ། རེ་གནས་བཞིན་དུ་བདེ་བ་ཉིད་དེ། རེ་གནས་ནི་སྟེགས་སོ། །

[Block 3315]
དབེན་པས་བྱས་པ་ནི་དབེན་པའི་བདེ་བའོ། །

[Block 3316]
དབེན་པ་ནི་རྣམ་པ་གཉིས་ཏེ། ལུས་དབེན་པ་དང་། སེམས་དབེན་པའོ། །

[Block 3317]
དེ་ལ་ལུས་དབེན་པ་ནི་གཉིས་སུ་མེད་པར་གནས་པའོ། །

[Block 3318]
སེམས་དབེན་པ༌[^2114]ནི་སེམས་ཀྱི་གཡེང་བ་སྤངས་པའོ། །

[Block 3319]
དབེན་པ་ན༌[^2115]གནས་པའི་བདེ་བ་ཉིད་བདུད་རྩིའི་རོ་ཡིན་ཏེ། དེས་ཡོངས་སུ་བསྒོས་པའི༌[^2116]བྱ་བ༌[^2117]གང་ལ་ཡོད་པ་དེ་ནི་དབན་པ་ན་གནས་པའི་བདེ་བའི་བདུད་རྩིའི་རོས་བློ་གོམས་པར་བྱས་པ་སྟེ། དེའི་བདེ་བས༌[^2118]ལུས་དང་སེམས་ཚིམ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3320]
སྙིང་དེ་ལ་གཞོལ་བར་གྱུར་པ་ནི་དབེན་པ་ན་གནས་པའི་བདེ་བ་ལ་གཞོལ་བར་གྱུར་པའོ། །

[Block 3321]
ཁྱིམ་ན་གནས་པ་དང་། ནགས་ན་གནས་པའི་བྱེ་བྲག་ཤེས་པར་གྱུར་པ་ཞེས་བྱ་བས་ནི་ཁྱིམ་ན་གནས་པའི་བདག་ཉིད་ཀྱིས་མངོན་སུམ་དུ་སྐྱོན་མཐོང་བའི་ཕྱིར་རོ། །

[Block 3322]
ནགས་ན་གནས་པ་ཡང་བདག་ཉིད་ཀྱིས་མངོན་སུམ་དུ་ཡོན་ཏན་མཐོང་བའི་ཕྱིར་རོ། །

[Block 3323]
དེ་བས་ན་ནགས་དང་ཁྱིམ་གྱི་ཁྱད་པར༌[^2119]མི་ཤེས་པ་དག༌[^2120]ནི་སྨྲ་བར་མི་རིགས་ཀྱི། དེ་ནི་འདིར་མཉན་པར་ཡང་རིགས་པ་མ་ཡིན་ཏེ། གཉི་ག་ཡང་ངོ་ཤེས་པའི་ཕྱིར་རོ། །

[Block 3324]
བཙོན་ར་འདྲ་བའི་ཁྱིམ་ཞེས་བྱ་བ་ནི་ཁྱིམ་ནི༌[^2121]བཙོན་རར་གྱུར་པ་ཡིན་ཏེ། ངན་སོང་དུ་འགྲོ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3325]
ཕྱུག་པོ་ནི་ཕལ་ཆེར་གཅིག་ཏུ་སྡུག་བསྔལ་བ་ཡིན་ནོ། །

[Block 3326]
ཅིག་ཤོས་དབུལ་བ་ཡང་ངོ་། །དགའ་བ་ཉིད་དུ་ཀུན་དུ་རྨོངས་པ་ནི་དགའ་བས་རྨོངས་པ་སྟེ། སྡུག་བསྔལ་ལ་བདེ་བར༌[^2122]ཕྱིན་ཅི་ལོག་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3327]
སྡིག་པའི་འབྲས་བུ་སྨིན་པ་ཉིད། །ཅེས་བྱ་བ་ནི་སྐྱེ་བ་སྔ་མ་དག་ལ་རང་གི་གོམས་པས་སྡུག་བསྔལ་ལ་བདེ་བར་ཕྱིན་ཅི་ལོག་པའི་འབྲས་བུ་སྨིན་པའོ། །

[Block 3328]
འདིར་བྱར་རུང་ངོ་ཞེས་བྱ་བ་གལ་ཏེ་དེ་ལྟར་ཆོས་བརྙེས་པར་རུང་བ་ཞེས་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 3329]
ཆོས་ཀྱི་གཉེན་པོ་དང་འདོམ་པའི་ཕྱིར་ཏེ་ཆོས་དང་འགལ་བ་དང་།

[Block 3330 [VERSE]]
ཕྱོགས་རྣམ་པར་འཇིག་པའི་ཕྱིར་རོ། །
ལས་སུ་བྱ་བ་མང་ཆེས་པས། །
--- END BLOCKS ---
