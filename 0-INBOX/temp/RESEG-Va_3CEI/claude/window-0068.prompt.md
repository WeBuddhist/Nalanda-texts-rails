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
[Block 2381]
མདོ་ལས་སྔོན་གྱི་དེ་བཞིན་གཤེགས་པ་དེས་མཐོང་ཞེས་པ་ནས། སངས་རྒྱས་ཀྱི་ས་འདི་མི་ཤེས༌[^1993]པའི་བར་དུ་དེ་དག་གིས་ནི་སྔོན་དེ་བཞིན་གཤེགས་པའི་བསྟན་པ་ལ་ཞུགས་ཤིང་ཐོས་པའི་རྒྱུས་འདི་ལ་འཇུག་ནུས་པར་བསྟན་པ་དང་། མདོ་འདི་ལ་དད་ཅིང་འཇུག་པ་ནི་དེས་ང་དང་ངའི་དགེ་འདུན་མཐོང་ཞེས་པ་ཡང་དཀོན་མཆོག་གསུམ་ཐ་མི་དད་པའི་མཚན་ཉིད་བསྟན་པའོ། །ཤེས་པ་ཆུང་བ་དང་དགེ་བའི་རྩ་བ་ཞན་པ་རྣམས་ཀྱིས་འཇུག་པར་མི་ནུས་པའི་ཕྱིར་བྱིས་པ་མྱོས་གྱུར་པ་ཞེས་གསུངས་སོ། །

[Block 2382]
ཐེག་པ་རྣམ་གཉིས་སུ་རིགས་ངེས་པ་རྣམས་ཀྱིས་ཀྱང་འཇུག༌[^1994]པའི་ཕྱིར་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་ས་མ་ཡིན་ཞེས་གསུངས་སོ། །

[Block 2383]
མདོ་ལས།

[Block 2384]
ཤཱ་རིའི་བུ་ཁྱོད་ང་དང་འབྲང༌[^1995]ན་ཞེས་པ་ནས། འདི་དག་རང་རིག་ཡེ་ཤེས་མེད། །ཅེས་པའི་བར་དུ་ནི་རིགས་མ་ངེས་པའི་ཉན་ཐོས་རྣམས་ཀྱང་ངའི་གསུང་འདི་ཐོས་ནས་གདོད་དད་པ་སྐྱེ་ཞིང་རྗེས་སུ་འབྲང་བར་འགྱུར་ན་གཞན་ལྟ་ཅི་སྨོས་ཞེས་བསྟན་པའོ། །

[Block 2385 [HEADING]]
###### **བསྟན་དུ་མི་རུང་བ།** ^4-3-5-4-2-2-2-2-0

[Block 2386]
མདོ་ལས།

[Block 2387]
ཁྱེད་ཀྱི༌[^1996]ཁེངས་པ་དང་ནི་ང་རྒྱལ་ཅན། མི་རིགས་ཞུགས་པ་དག་ལ་འདི་མ་བསྟན། །ཞེས་པ་ནི་ཚིགས་སུ་བཅད་པ༌[^1997]སུམ་ཅུ་རྩ་དྲུག་གིས་མི་ཤེས་པ་དད་པ་མེད་པ་སྡིག་པ་ཅན་བཞི་དང་། བདུན་དག་ལ་བསྟན་དུ་མི་རུང་བར་གསུངས་པ་སྟེ། དེ་ལ་སྡིག་པ༌[^1998]ཅན་བཞི་ནི་ཁེངས་པ། ང་རྒྱལ་ཅན། ལེ་ལོ་ཅན། བདག་ཏུ་ལྟ་བའི་མུ་སྟེགས་ཅན་རྣམས་སོ། །

[Block 2388]
མདོ་ལས།

[Block 2389]
བུས་པ་འདོད་ལས་རྟག་ཏུ་རབ་མོས་ཤིང་། ཆོས་བསྟན་མི་ཤེས་པས་ན་སྤོང་བར་བྱེད། །ཅེས་པ་ནི་སྡིག་ཅན་གསུམ་ལ་མི༌[^1999]བཤད་པ་སྟེ། ཤེས་པ་ཆུང་བ་ལོག་པའི་ཤེས་རབ་ཅན་དང་། འདོད་པ་རྣམ་ལྔས་མྱོས་ཤིང་ཉོན་མོངས་པ་སྟུག་པ༌[^2000]རྣམས་དང་། རིགས་མེད་པའི་སེམས་ཅན་ཐོས་ཀྱང་འཇུག་པར་མི་ནུས་པ་རྣམས་སོ། །

[Block 2390]
མདོ་ལས།

[Block 2391 [VERSE]]
ང་ཡི་ཐར་པ་འདི་ནི་སྤོང་བ་ནི། །
འཇིག་རྟེན་རྟག་ནས་སངས་རྒྱས་ཚུལ་ཡང་སྤང་། །

[Block 2392]
ཞེས་པའི་དོན་ཏེ། དེ་ཡང་མ་དད་པས་སྡིག་པ་མི་དགེ་བའི་རྒྱུ་བསྐྱེད་པ༌[^2001]དང་། སྡུག་བསྔལ་བའི་འབྲས་བུ་ལེན་པའོ། །

[Block 2393]
ཟག་པ་མེད་པའི་རྒྱུ་སྤོང་བ་ནི་སངས་རྒྱས་ཀྱི་རིགས་གཅོད་པའོ། །

[Block 2394]
ཟག་པ་དང་བཅས་པའི་རྒྱུ་སྤོང་བ་ནི་འཇིག་རྟེན་གྱི་དགེ་བས་མཐོ་རིས་སྤོང་བ་སྟེ། མདོ་སྡེ་འདི་ལ་མ་དད་པས་དེ་གཉིས་སྤངས་ཞེས་པའི་དོན་ཏོ། །

[Block 2395 [HEADING]]
###### **སྡིག་པ་མི་དགེ་བའི་རྒྱུ་བསྐྱེད་པ།** ^4-3-5-4-2-2-2-2-1-0

[Block 2396]
མདོ་ལས།

[Block 2397]
ཁྲོ་གཉེར་བྱས་ཤིང་ཐེག་པ་སྤངས་པ་ཡི། །ཞེས་པ་ནས། དེ་དག་རྣམ་སྨིན་མི་བཟད་ང་ལ༌[^2002]ཉོན། ། ཞེས་པའི་བར་དུ་ནི་མདོ་སྡེ་འདི་ལ་མ་དད་པས་སྡིག་པ་སྐྱེ་བར་བསྟན་པ་སྟེ། ཁྲོ་གཉེར་བྱས་ཞེས་པ་ནི་ལུས་དང་སེམས་མ་དད་པའི་ཚུལ་སྟོན་པའོ། །

[Block 2398]
མདོ་སྡེ་འདི་འདྲ་བ་ཀློག་པའི་དགེ་སློང་ལ་ངན་བྱས་ན་ཞེས་པ་ནི་ཆོས་སྤྱོད་པ་རྣམ་པ་བཅུའི་བར་ཆད་བྱས་པའོ། །

[Block 2399]
ངན་བྱས་པ་ནི་བརྙས་པ་སྨད་པ་ཕྲག་དོག་བྱས་པ་ཁོན་དུ་གཟུང༌[^2003]བའོ། །

[Block 2400 [HEADING]]
###### **སྡུག་བསྔལ་བའི་འབྲས་བུ་ལེན་པ།** ^4-3-5-4-2-2-2-2-2-0

[Block 2401]
མདོ་ལས།

[Block 2402 [HEADING]]
###### **མ་དད་པ་རྣམས་ཀྱི་འབྲས་བུ།** ^4-3-5-4-2-2-2-2-2-1-0

[Block 2403]
མི་ལས་ཤི་འཕོས་བསྟིར་མེད་པ་དེ་ཡི། །ཞེས་པ་ནས། བུས་པ་ཤི་ཤིང༌[^2004]འཕོས་ནས་དེར་ཡང་ལྟུང་། །ཞེས་པའི་བར་དུ་ནི། མདོ་སྡེ་འདི་ལ་མ་དད་པ་རྣམས་སྡུག་བསྔལ་མྱོང་བའི་འབྲས་བུ་བསྟན་པ་སྟེ། ཚིག་དང་པོ་ཉི་ཤུ་བརྒྱད་ཀྱིས་ནི་མ་དད་པ་རྣམས་ཀྱི༌[^2005]འབྲས་བུ་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས༌[^2006]ནི་བསྡུ་བ་བསྟན་ཏེ། འདི་ནི་དང་པོའོ། །

[Block 2404 [HEADING]]
###### **ངན་སོང་རྒྱུད་གསུམ་གཅིག་ནས་གཅིག་ཏུ་འཕོ་བ་རྣམ་པར་སྨིན་པ།** ^4-3-5-4-2-2-2-2-2-1-1-0

[Block 2405 [HEADING]]
###### **སེམས་ཅན་དམྱལ་བ།** ^4-3-5-4-2-2-2-2-2-1-1-1-0

[Block 2406]
དེ་ལ་ཡང་ཚིག་ཉི་ཤུ་གཉིས་ཀྱིས་ནི་ངན་སོང་རྒྱུད་གསུམ་གཅིག་ནས་གཅིག་ཏུ་འཕོ་བ་རྣམ་པར་སྨིན་པ་བསྟན། ཚིག་དྲུག་གིས་ནི་འགྲོ་བ་བཞིར་རྣམ་པར་སྨིན་པ་བསྟན། དེ་ལ་ཚིག་དང་པོ་གཅིག་གིས་ནི་སེམས་ཅན་དམྱལ་བ་མྱོང་བ་བསྟན། ཚིག་བཅུས་ནི་བྱོལ་སོང་གི་འབྲས་བུ་མྱོང་བ་བསྟན། དེའི་འོག་མ་ཚིག་བཅུས་ནི་མིའི་ནང་ན་ཐ་མར་སྐྱེ་བ་བསྟན། འདིར་ཡི་དགས་མ་སྨོས་པ་ནི་ཡི་དགས་སྲེད་པའི་དབང་གིས་སྐྱེ་བའི་ཕྱིར་འདིར༌[^2007]མ་སྨོས་སོ། །

[Block 2407]
དེ་དག་ཀྱང་རྣམ་པ་དྲུག་གིས་དབྱེ་བར་བྱ་སྟེ། དེའི་མིང་དང་། དེའི་ལུས་དང་། དེ་བསྡུ་བ་དང་། དེའི་གནས་དང་། དེའི་འབྲས་བུ་དང་། དེའི་ཚེའི་ཚད་དེ། གྲང་བ་བརྒྱད་དང་ཚ་བ་བརྒྱད་ལ་སོགས་པ་གཞན་དག་ལས་འབྱུང་བ་བཞིན༌[^2008]ཤེས་པར་གྱིས་ཤིག

[Block 2408 [HEADING]]
###### **བྱོལ་སོང།** ^4-3-5-4-2-2-2-2-2-1-1-2-0

[Block 2409]
།མདོ་ལས།

[Block 2410]
སེམས་ཅན་དམྱལ༌[^2009]ལས་ནམ་ཞིག་འཕོས་ན་ཡང་། །ཞེས་པ་ནས། འདི་འདྲ་བ་ཡི་མདོ་སྡེ་འདིས་སྤངས་པ། །ཞེས་པའི་བར་དུ་ནི་བྱོལ་སོང་དུ་གྱུར་པ་རྣམས་ཀྱི་སྡུག་བསྔལ་སྣ་ཚོགས་མྱོང་བར་བསྟན་པའོ། །

[Block 2411]
ཁྱིར་གྱུར་པ༌[^2010]ནི་རྣམ་པར་སྨིན་པ་བཅུ་སྟེ། སྐམ་པ།[^2011] རིད་པ། མདོག་ཉམས་པ། རྔོས་ཉེན་པ། གཞན་གྱིས་གཙེ་བ། ཤེས་པ་མེད་པ། བཀྲེས་པ། སྐོམ་པས་ཉེན་པ། བརྡེག་པ་དང་། གཞུ་བའི་གནས་སུ་གྱུར་པའོ། །

[Block 2412]
རྔ་མོའི་རྣམ་པར་སྨིན་པ་ནི་ཁུར་ལྕི་བས་མནན་པ། ཟས་ཀྱིས་གདུངས་པ། གཞུ་བརྡེག་གི་གནས་སུ་གྱུར་པ། ཤེས་པའི་བློ་མེད་པའོ། །

[Block 2413]
ཝར་གྱུར་བའི་རྣམ་པར་སྨིན་པ་ནི་རྔོས་འཁོངས་པ་མིག་ཞར་བ། བརྡེག་པའི་གནས་སུ་གྱུར་པའོ། །

[Block 2414]
སྦྲུལ་དུ་གྱུར་པའི་སྡུག་བསྔལ་ནི་ལུས་ཧ་ཅང་ཆེ་བ་རྣ་བ་འོན་པ། ཤེས་པ་མེད་པའོ། །

[Block 2415 [HEADING]]
###### **མིའི་ནང་ན་ཐ་མར་སྐྱེ་བ།** ^4-3-5-4-2-2-2-2-2-1-1-3-0

[Block 2416]
མདོ་ལས།

[Block 2417]
ནམ་ཞིག་མི་ཡི་ལུས་ཐོབ་གྱུར་ཀྱང་ནི། །ཞེས་པ་ནས། མགོན་མེད་གྱུར་ཅིང་འཇིག་རྟེན་དག་ན་རྒྱུ། །ཞེས་པའི་བར་དུ་ནི་མདོ་སྡེ་འདི་སྤོང་བའི་རྣམ་པར་སྨིན་པས་མི་ཞིག་ཏུ་སྐྱེས་ན་ཡང་། མ་རབས་དབང་པོ་མ་ཚང་བ་སྐྱོན་སྣ་ཚོགས་ཀྱིས་མནར་བར་སྐྱེ་སྟེ། ལུས་ཀྱི་སྐྱོན་ནི་དབང་པོ་རྟུལ་བ། ཧ་ཅང་ཐུང་བ། མཚན་དུ་མི་སྡུག་པ། ཞ་བོར་གྱུར་པ། གྲུམ་པོར༌[^2012]གྱུར་པ། ལོང་བ་འོན་པ་སྒུར་པོར་གྱུར་པ། ཚིག་སྨྲས་པ་མིས་ཡིད་མི་ཆེས་པར་གྱུར་པ། ཁ་ནས་རུལ་བའི་དྲི་མནམ་པ་འདྲེ་གདོན་གྱིས་གཙེ་བ། དབུལ་བ། དམན་པ། གཞན་གྱིས་བཀོལ་བ། ནད་མང་བ། རེག་པར་གྱུར་པ་སྟེ། ལུས་དང་། ངག་དང་། ཡིད་དང་། གསུམ་གྱི་སྒོ་ནས་སྡིག་པ་བྱས་པའི་རྣམ་པར་སྨིན་པ་ཡིན་པར་སྦྱར་རོ། །

[Block 2418]
མདོ་ལས།

[Block 2419]
དེ་ན་གང་ལ་དེ་ཡིས་ཉེར་བསྙེན༌[^2013]ཀྱང་། །ཞེས་པ་ནས། བྱིན་ན་ཡང་ནི་མྱུར་དུ་མི་ཟ་སྟེ། །ཞེས་པའི་བར་དུ་ནི་མདོ་སྡེ་འདི་ལ་མ་དད་པའི་ཕྱིར་གཞན་ལ་བརྟེན་ཀྱང་དེས་སྐྱབས་མི་བྱེད་ཅེས་པའི་དོན་ཏོ། །

[Block 2420]
མདོ་ལས།
--- END BLOCKS ---
