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

[Block 2421]
དེ་དག་འདི་འདྲ་སྡིག་གི་འབྲས་བུ་ནི། །ཞེས་པ་ནས། ནམ་ཡང་དེ་ཡི་ནད་རྣམས་མཐར་མི་སོས། །ཞེས་པའི་བར་དུ་ནི་མདོ་སྡེ་འདི་ལ་སྐུར་པ་བཏབ་པས༌[^2014]བསོད་ནམས་ཆུང་བར་བསྟན་པའོ། །

[Block 2422]
མདོ་ལས།

[Block 2423]
གཞན་གྱི༌[^2015]རྐུན་པོ་བྱས་པར་གྱུར་པ་ཡང་། །ཞེས་པ་ནས། སྡིག་པའི་ལས་ཅན་དེ་ལ་འདུ་ཤེས་འབབ། །ཞེས་པའི༌[^2016]བར་དུ་ནི་མདོ་སྡེ་འདི་ལ་སྐུར༌[^2017]པས་ཉེས་པ་གློ་བུར་འོང་ཞེས་པའི་དོན་ཏོ། །

[Block 2424]
མདོ་ལས།

[Block 2425]
[^2018] དེས་ཀྱང་འཇིག་རྟེན་མགོན་པོ་ཡང༌[^2019]མི་མཐོང་། །ཞེས་པ་ནས། །དེ་དག་སེམས་མི་དྲན་ཞིང་འོན་པར་གྱུར། །ཞེས་པའི་བར་དུ་ནི་མདོ་སྡེ་འདི་སྤངས་པས་ནམ་དུ་ཡང་སངས་རྒྱས་མི་མཐོང་བ་དང་། ཆོས་མི་ཐོས་པ་དང་། དབང་པོ་ཉམས་པར་འགྱུར་བ་ལ་འདི་ནི་དང་པོ་གཉིས་དང་སྦྱར་རོ། །

[Block 2426]
མདོ་ལས།

[Block 2427]
བྱང་ཆུབ་འདི་འདྲ་བ་འདི་སྤངས་པས་ན། །ཞེས་པ་ནས། བླུན་ཞིང་ཡན་ལག་དག་ནི་ཚང་མི་འགྱུར། །ཞེས་པའི་བར་དུ་འདིས་ནི་དབང་པོ་ཉམས་པར༌[^2020]བསྟན་ཏོ། །

[Block 2428 [HEADING]]
###### **འགྲོ་བ་བཞིར་རྣམ་པར་སྨིན་པ།** ^4-3-5-4-2-2-2-2-2-1-2-0

[Block 2429]
མདོ་ལས།

[Block 2430]
དེས༌[^2021]ནི་མདོ་སྡེ་འདི་སྤངས་སྡིག་གི་འབྲས། །ཞེས་པ་ནས། དེ་ན་དེ་དག་རྟག་ཏུ་དེ་གནས་འགྱུར།[^2022] །ཞེས་པའི་བར་དུ་ནི་དེས་ངན་སོང་བཞི་མྱོང་བར་བསྟན་པ་སྟེ། སེམས་ཅན་དམྱལ་བ་དང་། ཡི་དགས་དང་། བྱོལ་སོང་དང་། མི་མ་རབས་སུ་འགྱུར་བ་རིམ་བཞིན་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 2431]
མདོ་ལས།

[Block 2432]
དེ་དག་མི་ཡི༌[^2023]ལུས་སུ༌[^2024]གྱུར་ན་ཡང་། །ཞེས་པ་ནས། དེ་ཚེ་དེ་ཡི་རྒྱན་ནི་དེ་དག་སྟེ། །ཞེས་པའི་བར་དུ་ནི་མི་མ་རབས་སུ་གྱུར་པ༌[^2025]རྣམ་པར་སྨིན་པ་བསྟན་ཏེ། རྒྱན་ངན་པས་བརྒྱན་པ་དང་། རྟེན་ངན་པ་དང་བརྟེན་པ་དང་། མི་མཛེས་པར་གྱུར་པ་དང་། སྤྱོད་པ་ངན་པར་གྱུར་པ་སྟེ། འོག་ནས་འབྱུང་བ་དང་སྦྱར་རོ། །

[Block 2433]
མདོ་ལས།

[Block 2434]
ནད་རྣམས་དེ་ཡི་ལུས་ལ༌[^2026]བྱེ་བ་ཁྲག་ཁྲིག་རྨ། །ཞེས་པ་ནས། དེ་ནི་བྱོལ་སོང༌[^2027]སྐྱེ་གནས་དེ༌[^2028]རྟག་དགའ། །ཞེས་པའི་བར་དུ་ནི་འདིས་མི་མཛེས་པར་གྱུར་བ་དང་། སྤྱོད་ལམ་ངན་པར་གྱུར་པ་བསྟན་ཏོ། །

[Block 2435 [HEADING]]
###### **བསྡུ་བ།** ^4-3-5-4-2-2-2-2-2-2-0

[Block 2436]
མདོ་ལས།

[Block 2437]
དེ་རིང་གལ་ཏེ་ངས་དེང་ཤཱ་རིའི་བུ། །ཞེས་པ་ནས། འདི་འདྲའི་མདོ་སྡེ་མ་བཤད་ཅིག་ཅེས་བསྒོ། །ཞེས་པའི་བར་དུ་ནི་མདོ་སྡེ་འདི་ལ་མ་དད་པའི་རྣམ་པར་སྨིན་པ་མདོར་བསྡུས༌[^2029]ཏེ་བཤད་པའོ། །

[Block 2438 [HEADING]]
###### **བཤད་པར་འོས་པ་རྣམས་ཀྱི་མཚན་ཉིད།** ^4-3-5-4-2-2-2-3-0

[Block 2439]
མདོ་ལས།

[Block 2440 [HEADING]]
###### **དེ་བཞིན་གཤེགས་པའི་རིགས་ཅན།** ^4-3-5-4-2-2-2-3-1-0

[Block 2441]
འདི་ལྟར་གང་དག་གསལ་ཞིང་མང་ཐོས་དང་། །ཞེས་པ་ནས། དེ་ལ་ཁྱོད་ཀྱིས་དོན་དམ་འདིར༌[^2030]དེར་སྒྲོགས། །ཞེས་པའི་བར་དུ་ཚིག་བཅུ་དགུ་པོ་འདིས་ནི་བཤད་པར་འོས་པ་རྣམས་ཀྱི༌[^2031]མཚན་ཉིད་བསྟན་ཏེ། སྔོན་བྱང་ཆུབ་ཏུ་སེམས༌[^2032]བསྐྱེད་དུ་ཟིན་གྱིས༌[^2033]དེ་བཞིན་གཤེགས་པའི་རིགས་ཅན་བཤད་པར་འོས་པ་དང་། བྱང་ཆུབ་ཏུ་སེམས་ཀྱང་བསྐྱེད་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་སྤྱོད་སྤྱོད་པའི་བག་ཆགས་ཅན་འོག་ནས་འབྱུང་བ་རྣམས་ལ་བཤད་པར་འོས་པ་སྟེ། དེ་བཞིན་གཤེགས་པའི་རིགས་ཀྱི་རྟགས་ཡོད་པ་ནི་དབང་པོ་རྣོ་བ། ཤེས་རབ་ཅན་ལེགས་ཉེས་རྟོགས་པ། མི་རྨོངས་པའི་རང་བཞིན་ཅན་མང་དུ་ཐོས་པ། སེམས་གསལ༌[^2034]ཞིང་རྟུལ་ཕོད༌[^2035]པ། དམ་པའི་ཆོས་འདི་ཉན་པར་དགའ་ཞིང་ཐོས་པ་གཞན་མི་ཚོལ་བ༌[^2036]ནི་དེ་བཞིན་གཤེགས་པའི་རིགས་སུ་ངེས་པ་སྟེ། བཤད་པར་འོས་པའོ། །

[Block 2442 [HEADING]]
###### **ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གི་བག་ཆགས་ཅན།** ^4-3-5-4-2-2-2-3-2-0

[Block 2443]
མདོ་ལས།

[Block 2444]
གང་གིས་སངས་རྒྱས་བྱེ་བ་མང་པོ་མཐོང་། །ཞེས་པ་ནས། དེ་ལ་ཁྱོད་ཀྱིས༌[^2037]དོན་དམ་འདི་སྒྲོགས་ཤིག །ཞེས་པའི༌[^2038]བར་དུ་ནི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་གི་བག་ཆགས་ཅན་ནི་འདི་དག་སྟེ་འདི་ནི་སངས་རྒྱས་མང་པོ་མཐོང་ཞིང་སྦྱིན་པ་རྒྱ་ཆེན་པོ་བྱས་ཤིང་དགེ་བའི་རྩ་བ་བསྐྱེད་པ་སྟེ། སྦྱིན་པའི་བག་ཆགས་ཅན་དང་སྦྱར་རོ། །

[Block 2445]
མདོ་ལས།

[Block 2446]
གང་རྣམས་བརྩོན་འགྲུས་གང་ལྡན་རྟག་བྱམས་སེམས། ། ཞེས་པ་ནས། དེ་དག་ལ་ནི་མདོ་སྡེ་འདི༌[^2039]མངོན་ཤོད། །ཅེས་པའི་བར་དུ་བརྩོན་འགྲུས་དང་བསམ་གཏན་དུ་སྦྱར་རོ། །

[Block 2447]
མདོ་ལས།

[Block 2448]
ཕན་ཚུན་རྟོག་ཅིང་རིམ་གྲོ་བཅས་པ་ཅན། །ཞེས་པ་ནས། དེ་མདུན་མདོ་སྡེ་བཟང་པོ་འདི་སྨྲོས༌[^2040]ཤིག །ཅེས་པའི་བར་དུ་ནི་ཤེས་རབ་དང་ཚུལ་ཁྲིམས་ཀྱི་བག་ཆགས་རིམ་པ་བཞིན་དུ་སྦྱར་རོ། །

[Block 2449]
མདོ་ལས།

[Block 2450]
རྟག་ཏུ་ཁྲོ་བ་མེད་ཅིང་གང་དྲན་པ། །ཞེས་པ་ནས། དེ་ཡི་མདུན་དུ་མདོ་སྡེ་མཆོག༌[^2041]འདི་སྨྲོས།[^2042] །ཞེས་པའི་བར་དུ་ནི་བཟོད་པའི་བག་ཆགས་དང་སྦྱོར༌[^2043]རོ། །

[Block 2451]
མདོ་ལས།

[Block 2452]
གང་དག་འཁོར་གྱི་དབུས་སུ་ཆོས་སྟོན་ཅིང་། །ཞེས་པ་ནས། དེ་ལ་ཁྱོད་ཀྱིས་མདོ་སྡེ་འདི༌[^2044]རབ༌[^2045]སྒྲོགས། །ཞེས་པའི་བར་དུ་ནི་མདོ་སྡེ་འདི་ཚོལ་བ་དང་རིམ་གྲོར་བྱེད་པ་རྣམ་པ༌[^2046]གཉིས་ལ་གཞན་གྱི༌[^2047]བསྟན་པ་ཐམས་ཅད་སྤངས་ཏེ། ཐེག་པ་ཆེན་པོའི་མདོ་སྡེ་འབའ་ཞིག་ཚོལ་བའི་ཕྱིར་ཚོལ་བ་བསྟན་ཏོ། །

[Block 2453]
མདོ་ལས།

[Block 2454]
ཇི་ལྟར་དེ་བཞིན་གཤེགས་པའི་གདུང་འཛིན་པ། །ཞེས་པ་ནས། དེ་དག་མདུན་དུ་མདོ་སྡེ་མཆོག་འདི་སྨྲོས།[^2048] །ཞེས་པའི༌[^2049]བར་དུ་ནི་མདོ་སྡེ་འདི་ལ་རིམ་གྲོ་བསྐྱེད་པ་དང་། བཤད་པར་འོས་པ་རྣམས་ཀྱི་མཚན་ཉིད་ཀྱི་བསྡུ་བ་བསྟན་ཏོ།། །།

[Block 2455 [HEADING]]
### དད་པའི་ལེའུ། ^4-4-0
--- END BLOCKS ---
