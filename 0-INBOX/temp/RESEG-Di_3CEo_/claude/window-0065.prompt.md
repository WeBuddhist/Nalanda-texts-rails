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
[Block 2276]
དོན་སྨྲ་བ་གང་ཡིན་པ་དེ་ལས་འདུ་ཤེས་གཞན་དུ་བསྒྱུར་ལ། དེས་གང་གི་དབང་དུ་བྱས་ནས་སྨྲས་པའི་ཚིག་དེའི་དོན་ཡང་གོ་ན་ཚིག་དེའི་བརྫུན་དུ་སྨྲ་བ་ཡིན་ནོ། །

[Block 2277]
མདོ་ལས་ཐ་དད༌[^906]བཅུ་དྲུག་གསུངས་པ་དེ་ནི་མ་མཐོང་བ་ལ་མཐོང་ཞེས་སྨྲ་བ་ནས་མི་ཤེས་པར་ཤེས་སོ་ཞེས་པའི་བར་ལ་སོགས་པའོ། །

[Block 2278]
མཐོང་བ་དང་། ཐོས་པ་དང་། རྟོགས་པ་དང་། རྣམ་པར་ཤེས་པ་དག་གི་མཚན་ཉིད་ཅི་ཞེ་ན། མིག་རྣ་ཡིད་ཀྱི་རྣམ་ཤེས་དང་།

[Block 2279 [VERSE]]
གསུམ་གྱིས༌[^907]ཉམས་སུ་མྱོང་གང་དེ། །
མཐོང་ཐོས་རྣམ་པར་ཤེས་པ་དང་། །
རྟོགས་པ་ཡིན་ཏེ་རིམ་བཞིན་བཤད། །

[Block 2280]
མིག་གི་རྣམ་པར་ཤེས་པས་ཉམས་སུ༌[^908]མྱོང་བ་དེ་ནི་མཐོང་བ་དང་། རྣ་བའི་རྣམ་པར་ཤེས་པས་མྱོང་བ་དེ་ནི་ཐོས་པ་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས༌[^909]མྱོང་བ་དེ་ནི་རྣམ་པར་ཤེས་པ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་ཀྱི་རྣམ་པར་ཤེས་པས་མྱོང་བ་ནི་རྟོགས་པ་ཞེས་བཤད་དོ། །

[Block 2281 [VERSE]]
ཕྲ་མ་ཕ་རོལ་དབྱེ་བའི་ཕྱིར། །
ཉོན་མོངས་ཅན་གྱི་སེམས་ཀྱི་ཚིག །

[Block 2282]
ཕ་རོལ་དབྱེ་ཞིང་མི་མཛའ་བར༌[^910]བྱ་བའི་ཕྱིར་སེམས་ཉོན་མོངས་པ་ཅན་གྱི་ཚིག་ནི་ཕྲ་མ་སྟེ། དོན་མངོན་པར་གོ་བ་དང་། མ་ནོར་བ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2283]
ཚིག་རྩུབ་པོ་ནི་མི༌[^911]སྙན་པ། སེམས་ཉན་མོངས་པ་ཅན་གྱི་ཚིག་ཅེས་པ་དང་ཡང་སྦྱར་ཏེ། སེམས་ཉོན་མོངས་པ་ཅན་གྱི་ཚིག་མི་སྙན་པ་ཕ་རོལ་པོ་ལ་སྨྲས༌[^912]ཤིང་དོན་མངོན་པར་གོ་ལ། གང་ལ་སྨྲ་བར་འདོད་པ་དེ་ཉིད་ལ་སྨྲས་པ་གང་ཡིན་པ་དེ་ནི་ཚིག་རྩུབ་པོ་ཡིན་ནོ། །

[Block 2284]
ཉོན་མོངས་ཅན་ཀུན་ཀྱལ་པ་ཉིད། །ཉོན་མོངས་པ་ཅན་གྱི་ཚིག་ཐམས་ཅད་ནི་ཚིག་ཀྱལ་པ་ཡིན་ནོ། །

[Block 2285]
གཞན་ནི་དེ་ལས་གཞན་ཉོན་མོངས། །གཞན་དག་ན་རེ་ངག་གི་ལས་བརྫུན་གྱི་ཚིག་སྨྲ་བ་ལ་སོགས་པ་དེ་དག་ལས་གཞན་པ་ཉོན་མོངས་ཅན་གྱི་ཚིག་གང་ཡིན་པ་དེ་ནི་ཚིག་ཀྱལ་པ༌[^913]ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2286]
ཁ་གསག་གླུ་དང་ཟློས་གར་བཞིན། །བསྟན་བཅོས་ངན་བཞིན། དཔེར་ན་དགེ་སློང་ལོག་པས་འཚོ་བ་ཁ་གསག་བྱེད་པ་དང་། ཆགས་པས་ཁ་ཅིག་གླུ་ལེན་པ་དང་། ཟློས་གར་མཁན་རྣམས་ཟློས༌[^914]གར་གྱི་ཚེ་གཞན་དག་མགུ་བར་བྱ་བའི་ཕྱིར་འཁྱལ་པ་དང་། དེའི་ལྟ་བར་གྱུར་ནས་བསྟན་བཅོས་ངན་པ་དག་འདོན་པ་དང་། དེ་བཞིན་དུ་བརྫུན་དུ་སྨྲ་བ་ལས་གཞན་པ་ཉོན་མོངས་པ་ཅན་གྱི་ངག་གི་ལས་གང་ཡིན་པ་དེ་ཡང་ཚིག་ཀྱལ་པ་ཡིན་ནོ། །

[Block 2287]
བརྣབ་སེམས་ནི། ལོག་པས་གཞན་གྱི་ནོར་ལ་ཆགས། །ཕ་རོལ་པོ་དག་གི་གང་ཡིན་པ་བདག༌[^915]གི་ཡིན་པར་གྱུར་ཀྱང་ཅི་མ་རུང་སྙམ་ནས་གཞན་གྱི་ནོར་དག་ལ་མཐུའམ་འཇབ་བུ་ཡང་རུང་ལོག་པ་མི་རིགས་པས་བདག་གིར་བྱེད་པར་འདོད་པ་གང་ཡིན་པ་དེ་ནི་བརྣབ་སེམས་སོ། །

[Block 2288]
གནོད་སེམས་སེམས་ཅན་ལ་སྡང༌[^916]བ། །ཕ་རོལ་ལ་གནོད་པའི་རྣམ་པར་ཞུགས་པའོ། །

[Block 2289]
དགེ་དང་མི་དགེ་མེད་ལྟ་བ། །ལོག་པར་ལྟ་བ་ཡིན། ལས་དགེ་བ་དང་མི་དགེ་བ་མེད་དོ་ཞེས་ལྟ་བ་དེ་ནི་ལོག་པར་ལྟ་བའོ། །

[Block 2290]
ལས་ཀྱི་ལམ་བཅུར་བཤད་པའི་ལས་ཀྱི་ལམ་ཞེས་བྱ་བའི་དོན་ནི༌[^917]ཅི་ཡིན་ཞེ་ན། འདི་ལ། གསུམ་ལམ་བདུན་ནི་ལས་ཀྱང་ཡིན། །བརྣབ་སེམས་ལ་སོགས་པ༌[^918]འཇུག་པའི་ལས་ཀྱི་ལམ་ཡིན་པས་ལས་ཀྱི་ལམ་མོ། །

[Block 2291]
སྲོག་གཅོད་པ་ལ་སོགས་པ་བདུན་ནི་ལས་ཀྱང་ཡིན་ལས་ཀྱི་ལམ་ཡང་ཡིན་པ་ལས་ཀྱི་ལམ་མོ། །

[Block 2292 [HEADING]]
##### དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པ། ^4-3-9-4-0

[Block 2293]
མི་དགེ་བའི་ལས་ཀྱི་ལམ་བཅུ་པོ་གང་དག་ཡིན་པ་དེ་དག་ཐམས་ཅད་དགེ་བའི་ཆོས་རྣམས་ཀུན་དུ་སྤྱོད་པ་དང་འགལ་བ་ཡིན་ལ། མེད་པར་ལྟ་བས་རྩ་བ་གཅོད། །དགེ་བའི་རྩ་བ༌[^919]གཅོད་པ་ནི་ལོག་པར་ལྟ་བ་ཆེན་པོ་ཡོངས་སུ་རྫོགས་པས་སོ། །

[Block 2294]
དགེ་བའི་རྩ་བ་གང་ཞིག་གཅོད་ཅེ་ན། འདོད་གཏོགས་སྐྱེས་ནས་ཐོབ་པ་རྣམས། །འདོད་པ་ན་སྤྱོད་པ་རྣམས་ཀྱི་གཅོད་དེ། གཟུགས་དང་གཟུགས་མེད་པ་དག་དང་མི་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2295]
སྐྱེས་ནས་འཐོབ་པ་དག་ཁོ་ན་ཀུན་དུ་འཆད་པར་འགྱུར་ཏེ། སྦྱོར་བ་ལས་བྱུང་བ་དག་ནི་སྔར་ཡོངས་སུ་ཉམས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 2296]
ཅི་ལ་དམིགས་པའི་ལོག་པར་ལྟ་བས་ཀུན་དུ་གཅོད་པར་བྱེད་ཅེ་ན། རྒྱུ་དང་འབྲས་ལ་སྐུར་བ༌[^920]འདེབས་པས། །ལེགས་པར་སྤྱད་པ་མེད་དོ། །

[Block 2297]
ཉེས་པར་སྤྱད་པ་མེད་དོ་ཞེས་རྒྱུ་ལ་སྐུར་པ་འདེབས་པ་གང་དག་ཡིན་པ་དང་། ལེགས་པར་སྤྱད་པ་དང་ཉེས་པར་སྤྱད་པ་རྣམས་ཀྱི་འབྲས་བུ་རྣམ་པར་སྨིན་པ་མེད་དོ་ཞེས་འབྲས་བུ་ལ་སྐུར་པ་འདེབས་པ་གང་དག་ཡིན་པའོ། །

[Block 2298]
དེ་ལ་ཡང་ཟག་པ་དང་བཅས་པ་ཁོ་ནས་ཞེས་ཁ་ཅིག་ཟེར་རོ། །

[Block 2299]
འདི་སྐད་དུ་བརྗོད་དེ། ཀུན་གྱིས། གཏན་ནས་ཅིག་ཅར་གཅོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 2300]
རིམ་གྱིས་བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་བཞིན་དུ་ཆེན་པོའི་ཆེན་པོས་ཆུང་ངུའི་ཆུང་ངུ་གཅོད་པར་བྱེད་པའི་བར་དུ་ལོག་པར་ལྟ་བ་དགུས་དགེ་བའི་རྩ་བ་རྣམ་པ་དགུ་གཅོད་པར་བྱེད་དོ། །གང་དུ་དགེ་བའི་རྩ་བ་རྣམས་ཀུན་དུ་གཅོད་ཅེ་ན། མིའི་ནང་དུ། ངན་སོང་དག་ན་ནི་མ་ཡིན་ཏེ། ཤེས་རབ་ཉོན་མོངས་པ་ཅན་དང་། ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་དག་མི་བརྟན་པའི༌[^921]ཕྱིར་རོ། །

[Block 2301]
ལྷ་དག་གི་ནང་ན་ཡང་མེད་དེ། ལས་ཀྱི་འབྲས་བུ་མངོན་སུམ་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 2302]
གླིང་གསུམ་དག་ན་ཡོད་ཀྱི་བྱང་གི་སྒྲ་མི་སྙན་ན་མེད་དེ། སྡིག་པའི་བསམ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2303]
དེ་དག་ཀྱང་། སྐྱེས་པ་བུད་མེད་ཀྱིས༌[^922]གཅོད་དོ། །

[Block 2304]
དེ་དག་ལས་ཀྱང་། ལྟ་སྤྱད་སྡིག་པའི་བསམ་པ་བསྟན་པ༌[^923]དང་། མཁྱུད་པ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2305]
དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པའི་རང་བཞིན་ཇི་ལྟ་བུ་ཞིག་ཡིན་ཞེ་ན། དེ་ནི་མི་ལྡན་པའོ། །

[Block 2306]
གང་གི་ཚེ་དགེ་བའི་རྩ་བ་རྣམས་ཀྱི་ཐོབ་པ་ཆད་དེ་ཡང་མི་སྐྱེ་ལ་མི་ལྡན་པ་དེ་སྐྱེས་ན་དགེ་བའི་རྩ་བ་རྣམས་ཀུན་དུ་ཆད་པ༌[^924]ཞེས་བྱའོ། །

[Block 2307]
ཀུན་དུ་ཆད་པ་དེ་དག་ཀྱང་། མཚམས་ནི་ཐེ་ཚོམ་ཡོད་ལྟ་བས། ནམ་ཞིག་ལ་རྒྱུ་དང་འབྲས་བུ་ལ་ཐེ་ཚོམ་སྐྱེས་པའམ། ཡོད་པར་ལྟ་བ་དེའི་ཚེ་ཡང་དེའི་ཐོབ་པ༌[^925]ཀུན་དུ་སྐྱེས་པའི་ཕྱིར་དགེ་བའི་རྩ་བ་རྣམས་ཉིང་མཚམས་སྦྱོར་བར་འགྱུར་རོ། །

[Block 2308]
ཡང་དེ་དག་གི་ཉིང་མཚམས་སྦྱོར་བ་ནི། མཚམས་མེད་བྱེད་པའི་འདི་ལ་མིན། །གཞན་གྱི་འདི་ཉིད་ལ་འགྱུར་གྱི་མཚམས་མེད་པ་བྱེད་པ༌[^926]ནི་དམྱལ་བར་སྐྱེ་བའམ་འཆི་འཕོ་བར་ཉིང་མཚམས་སྦྱོར་རོ། །

[Block 2309]
འདི་ནི་ལས་ཀྱི་ལམ་གྱི་སྐབས་ཡིན་པས་དེ་ལ་ལས་ཀྱི་ལམ་དུ་ཞིག་དང་སེམས་པ་ལྷན་ཅིག་ཅིག་ཅར་དུ་འབྱུང་བར་འགྱུར་བ་བརྗོད་པར་བྱ་སྟེ།

[Block 2310 [VERSE]]
མི་དགེ་བརྒྱད་ཀྱི་བར་དག་དང་། །
སེམས་པ་ཅིག་ཅར་ལྷན་ཅིག་འབྱུང་།[^927] །

[Block 2311]
རེ་ཞིག་སེམས་པ་གཅིག་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་བརྣབ་སེམས་ལ་སོགས་པ་མངོན་དུ་གྱུར་པའི་ཕྱིར་སེམས་པ་ཉོན་མོངས་པ་མ་ཡིན༌[^928]པ་དེའི་སྦྱོར་བས་གཟུགས་ཅན་རྣམས་ལས་གང་ཡང་རུང་བ་ཞིག་མཐར་ཕྱིན་པར་བྱེད་ནའོ། །

[Block 2312]
གཉིས་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་གནོད་སེམས་སུ་གྱུར་པས་སྲོག་གཅོད་ནའོ། །

[Block 2313]
གསུམ་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་གནོད་སེམས་སུ་གྱུར་པས་གཞན་གྱི་སྲོག་ཆགས་གསད་པས༌[^929]འཕྲོག་ནའོ། །

[Block 2314]
བཞི་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་དབྱེན་བྱ་བའི་བསམ་པ་དང་ལྡན་པས་བརྫུན་གྱི་ཚིག་གམ་ཚིག་རྩུབ་པོ་སྨྲ་ན་སྟེ། དེ་ལ་ཡིད་ཀྱི་གཅིག་ཡིན་ངག་གི་གསུམ༌[^930]ཡིན་ནོ། །

[Block 2315]
ཡང་ན་བརྣབ་སེམས་ལ་སོགས་པར་གྱུར་པ་དེའི་སྦྱོར་བས་གཞན་གསུམ་མཐར་ཕྱིན་པར་བྱེད་ན་སྟེ། ལྔ་དང་དྲུག་དང་བདུན་དང་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །
--- END BLOCKS ---
