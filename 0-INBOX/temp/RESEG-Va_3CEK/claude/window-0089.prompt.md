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
[Block 3116]
འདི་དག་ནི་དུས་ལ་ལྟོས་པ་ཡང་ཡིན་ལ་རྣམ་པར་གྲོལ་བ་ཡང་ཡིན་པས༌[^2152]དུས་ཀྱི༌[^2153]རྣམ་པར་གྲོལ་བ་དག་སྟེ། བར་གྱི་ཚིག་མི་མངོན་པར་བྱས་པའི་ཕྱིར་མར་གྱི་བུམ་པ་བཞིན་ནོ། །

[Block 3117]
འདི་དག་གི་ཏིང་ངེ་འཛིན་མངོན་སུམ་དུ་གྱུར་པ༌[^2154]ནི་ཡོ་བྱད་དང་ནད་མེད་པ་དང་ཡུལ་གྱི་བྱེ་བྲག་ལ་ལྟོས་པའི་ཕྱིར་དུས་ལ་ལྟོས་པ་ཡིན་ནོ། །

[Block 3118]
མི་གཡོའི་ཆོས་ཅན་མི་གཡོ་བ། །མི་གཡོ་བའི་ཆོས་ཅན་གྱི་རྣམ་པར་གྲོལ་བ་ནི་ཡོངས་སུ་མི་ཉམས་པའི་སྒོ་ནས་གཡོ་བར་མི་ནུས་པའི་ཕྱིར་མི་གཡོ་བ་ཡིན་ནོ། །

[Block 3119]
དེའི་ཕྱིར་དེ་དུས་མི་སྦྱོར་གྲོལ། །དེ་ཉིད་ཀྱི་ཕྱིར་དེ་ནི་དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ་ཞེས་བྱ་བ་སྟེ། དེ་ནི་འདོད་དགུར་ཏིང་ངེ་འཛིན་མངོན༌[^2155]སུམ་དུ་གྱུར་པའི་ཕྱིར་དུས་ལ་མི་ལྟོས་པར་རྣམ་པར་གྲོལ་བ་ཡིན་ནོ། །

[Block 3120]
ཡང་ན་ཡོངས་སུ་ཉམས་པ་སྲིད་པ་དང་། མི་སྲིད་པའི་སྒོ་ནས་དུས་གཞན་གྱི་བར་དང་། གཏན་དུ་རྣམ་པར་གྲོལ་བའི་ཕྱིར་དུས་ཀྱི༌[^2156]རྣམ་པར་གྲོལ་བ་དང་། དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ་ཉིད་ཡིན་ནོ། །

[Block 3121]
དེ་ནི་མཐོང་ཐོབ་རྒྱུ་ལས་བྱུང་། །མི་གཡོ་བའི་ཆོས་ཅན་དེ་ནི་མཐོང་བས་ཐོབ་པ་སྔོན་དུ་འགྲོ་བ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3122 [HEADING]]
##### དང་པོ་ནས་དེའི་རིགས་དང་སྦྱངས་པ་ལས་གྱུར་པ། ^3-2-12-2-0

[Block 3123]
ཅི་དགྲ་བཅོམ་པ་དྲུག་པོ་འདི་དག་དང་པོ་ཁོ་ན་ནས་དེའི་རིགས་ཅན་ཁོ་ན་དག་ཅིག་ཡིན་ནམ།

[Block 3124 [VERSE]]
འོན་ཏེ་ཕྱིས་ཡིན་ཞེ་ན། །
ཁ་ཅིག་དང་པོ་ནས་དེའི་རིགས། །
ཁ་ཅིག་སྦྱངས་པ་ལས་གྱུར་ཏོ། །

[Block 3125]
ཁ་ཅིག་ནི་དང་པོ་ཉིད་ནས་འཆི་བར་སེམས་པའི་ཆོས་ཅན་གྱི་རིགས་ཅན་ཡིན་ལ་ཁ་ཅིག་ནི་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་དུ་གྱུར་པ་ལས་དབང་པོ་རྣམས་སྦྱངས་པས་འཆི་བར་སེམས་པའི་ཆོས་ཅན་དུ་གྱུར་པ་ཡིན་ཏེ། མི་གཡོ་བའི་ཆོས་ཅན་དུ་གྱུར་བའི་བར་དུ་ཡང་དེ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 3126]
དེ་ལ་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ནི་ཡོངས་སུ་ཉམས་པར་འགྱུར་བའི་སྐལ་བ་དང་ལྡན་གྱི་འཆི་བར༌[^2157]སེམས་པ་ལ་སོགས་པའི་ཆོས་ཅན་ནི་མ་ཡིན་པ་གང་ཡིན་པའོ། །

[Block 3127]
འཆི་བར་སེམས་པའི་ཆོས་ཅན་ནི་འཆི་བར་སེམས་པར་འགྱུར་བའི་སྐལ་བ་ཅན་གང་ཡིན་པའོ། །

[Block 3128]
རྗེས་སུ་སྲུང་བའི་ཆོས་ཅན་ནི་རྗེས་སུ་སྲུང་བར་འགྱུར་བའི་སྐལ་བ་ཅན་གང་ཡིན་པའོ། །

[Block 3129]
གནས་པ་ལས་མི་བསྐྱོད་པ་ནི་ཡོངས་སུ་ཉམས་པར་འགྱུར་བའི་རྐྱེན་སྟོབས་དང་ལྡན་པ་མེད་ན་རྗེས་སུ་མ་བསྲུངས་ཀྱང་གནས་པར་འགྱུར་བའི་སྐལ་བ་ཅན་ཡིན་ཞིང་ཉམས་པར་མི་འགྱུར་བ་དང་མངོན་པར་བརྩོན་པ་མེད་ན་འཕེལ་བར་ཡང་མི་འགྱུར་བའི་སྐལ་བ་ཅན་གང་ཡིན་པའོ། །

[Block 3130]
རྟོགས་པའི་སྐལ་པ་ཅན་ནི་མི་གཡོ་བ་རྟོགས་པར་འགྱུར་བའི་སྐལ་པ་ཅན་གང་ཡིན་པའོ། །

[Block 3131]
མི་གཡོ་བའི་ཆོས་ཅན་ནི་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་བའི་སྐལ་བ་ཅན་གང་ཡིན་པ་དེ་ཁོ་ནའོ། །

[Block 3132]
དང་པོ་གཉིས་ནི་སྔོན་སློབ་པའི་གནས་སྐབས་ཁོ་ན་ན་རྒྱུན་དུ་སྦྱོར་བ་དང་གུས་པར་སྦྱོར་བ་མེད་པ་ཡིན་ནོ། །

[Block 3133]
གསུམ་པ་ནི་རྒྱུན་དུ་སྦྱོར་བ༌[^2158]ཡིན་ནོ། །

[Block 3134]
བཞི་པ་ནི་གུས་པར་སྦྱོར་བ༌[^2159]ཡིན་ནོ། །

[Block 3135]
ལྔ་པ་ནི་གཉི་གར༌[^2160]སྦྱོར་བ་པ་ནི་ཡིན་ལ་དབང་པོ་རྟུལ་པོ་ཡིན་ནོ། །

[Block 3136]
དྲུག་པ་ནི་གཉི་གར་སྦྱོར་བ༌[^2161]དང་དབང་པོ་རྣོན་པོ་ཡིན་ནོ། །

[Block 3137]
ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ཡང་གདོན་མི་ཟ་བར་ཡོངས་སུ་ཉམས་པར་འགྱུར་བ་མ་ཡིན་ལ། རྟོགས་པའི་སྐལ་བ་ཅན་གྱི་བར་དུ་ཡང་རྟོགས་པར་འགྱུར་བ་མ་ཡིན་གྱི་སྲིད་པའི་ཕྱིར་དེ་སྐད་ཅེས་བཤད་དོ། །

[Block 3138]
དེ་ལྟར་བྱས་ན་ཁམས་གསུམ་ཆར་ན་ཡང་དགྲ་བཅོམ་པ་དྲུག་ཡོད་པར་རུང་ངོ་། །གང་དག་གི་གདོན་མི་ཟ་བར་ཡོངས་སུ་ཉམས་པར་འགྱུར་བ་ནས་མངོན་པར་རྟོགས་པའི་བར་དུ་འགྱུར་བ་དེ་དག་གི༌[^2162]ལྟར་ན་འདོད་པའི་ཁམས་ན་ནི་དྲུག་གོ། །

[Block 3139]
གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་དག་ན་ནི་གནས་པ་ལས་མི་བསྐྱོད་པ་དང་། མི་གཡོ་བའི་ཆོས་ཅན་དང་གཉིས་ཏེ། དེ་གཉིས་ན་ཡོངས་སུ་ཉམས་པ་དང་། འཆི་བར་སེམས་པ་དང་། དབང་པོ་འཕོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 3140 [HEADING]]
##### འབྲས་བུ་དང་རིགས་ལས་ཡོངས་སུ་ཉམས་པ། ^3-2-12-3-0

[Block 3141]
འདི་དག་ལས་གང་ཞིག་འབྲས་བུ་འམ་རིགས་གང་ལས་ཡོངས་སུ་ཉམས་པར་འགྱུར་རོ་ཞེ་ན། བཞི་ནི་རིགས་ལས་ལྔ་འབྲས་ལས། །

[Block 3142]
ཉམས་འགྱུར། འཆི་བར་སེམས་པའི་ཆོས་ཅན་ལ་སོགས་པ་བཞི་ནི་རིགས་ལས་ཡོངས་སུ་ཉམས་པར་འགྱུར་རོ། །

[Block 3143]
ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ནི་རང་གི་རིགས་ལས་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་རོ། །

[Block 3144]
ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ལ་སོགས་པ་ལྔ་ནི་འབྲས་བུ་ལས་ཀྱང་ཡོངས་སུ་ཉམས་པར་འགྱུར་རོ། །

[Block 3145]
དེ་དག་ཀྱང་།

[Block 3146]
དང་པོ་ལས་མ་ཡིན། གང་གི་རིགས་དང་པོ་གང་ཡིན་པ་དེ་ལས་ནི་དེ་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་ཏེ། སློབ་པ་དང་མི་སློབ་པའི་ལམ་དག་གིས་བརྟན་པོར་བྱས་པའི་ཕྱིར་རོ། །

[Block 3147]
སློབ་པ་ནི་འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་ལམ་དག་གིས་བརྟན་པོར་བྱས་པའི་ཕྱིར་རོ། །

[Block 3148]
ཕྱིས་སྦྱངས་པས་ཐོབ་པ་གང་ཡིན་པ་དེ་ལས་ནི་ཡོངས་སུ་ཉམས་པར་འགྱུར་རོ། །

[Block 3149]
གང་གི༌[^2163]འབྲས་བུ་དང་པོ་གང་ཡིན་པ་དེ་ལས་ཀྱང་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་རོ། །

[Block 3150]
ལྷག་མ་ལས་ནི་ཡོངས་སུ་ཉམས་པར་འགྱུར་རོ། །

[Block 3151]
དེ་ཉིད་ཀྱི་ཕྱིར་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལས་ཡོངས་སུ་ཉམས་པ་མེད་དོ། །

[Block 3152]
དེ་ལྟར་བྱས་ན་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ནི་རྣམ་པ་གསུམ་ཡིན་ཏེ།[^2164] དེའི་སོ་ན་གནས་པ་བཞིན་དུ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ༌[^2165]དང་། དབང་པོ་འཕོ་བའམ།[^2166] ཡོངས་སུ་ཉམས་ནས་སློབ་པ་ཉིད་དུ་འགྱུར་བའོ། །

[Block 3153]
འཆི་བར་སེམས་པའི་ཆོས་ཅན་ནི་བཞི་སྟེ། གསུམ་པོ་དེ་དག་ཉིད་དང་། ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་གྱི་རིགས་སུ་སླར་འོང་བའོ། །

[Block 3154]
དེ་བཞིན་དུ༌[^2167]གསུམ་ལ་ཡང་རེ་རེ་བསྐྱེད་དེ། གོ་རིམས་བཞིན་དུ་རྣམ་པ་ལྔ་དང་དྲུག་དང་བདུན་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3155]
དེ་སློབ་པར་གྱུར་ན་གང་གི་རིགས་དང་པོ་གང་ཡིན་པ་དེ་ཁོ་ན་ལ་གནས་ཀྱི་གཞན་དག༌[^2168]ལ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
