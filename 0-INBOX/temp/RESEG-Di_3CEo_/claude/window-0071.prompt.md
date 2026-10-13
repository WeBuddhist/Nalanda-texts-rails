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
[Block 2486]
གཞན་ནི་ལས་ཀྱི་དབྱེན་ལས་འགྱུར་ཏེ། གལ་ཏེ་མཚམས་གཅིག་གི་ནང་དུ་མི་མཐུན་པས་ལས་དག་བྱེད་ནའོ། །

[Block 2487]
དེ་ཡང་ནི།

[Block 2488 [VERSE]]
ལས་ཀྱི༌[^989]དབྱེན་ནི་གླིང་གསུམ་ནའོ། །
སྒྲ་མི་སྙན་མ་གཏོགས་སོ། །
དེ་ནི་བརྒྱད་དག་ཡན་ཆད་ཀྱིས། །

[Block 2489]
འཁོར་ལོའི་དབྱེན་དུས་དྲུག་ཏུ་མི་འབྱུང་ངོ་། །འདི་ལྟ་སྟེ།

[Block 2490]
དང་པོ་མཐའ་སྐྱོན་ཟུང་གཅིག་གི །

[Block 2491 [VERSE]]
སྔ་རོལ་ཐུབ་པ་ནོངས་པ་དང་། །
མཚམས་མ་བཅད་པ་དག་ཏུ་ཡང་། །
འཁོར་ལོའི་དབྱེན་ནི་མི་འབྱུང་ངོ་། །

[Block 2492]
དང་པོ་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་ནས་རིང་པོ་མ་ལོན་པ་དང་། ཐ་མ་བཅོམ་ལྡན་འདས་མྱ་ངན་ལས་འདའ་བའི་ཚེ་དང་། ཆུ་བུར་གྱི་སྔོན་རོལ་དུ་སྟེ།[^990] ཇི་སྲིད་དུ་ཚུལ་ཁྲིམས་ཀྱི་སྐྱོན་དང་། ལྟ་བའི་སྐྱོན་མ་བྱུང་གི་བར་དང་། ཟུང༌[^991]གཅིག་གི་སྔོན་རོལ་ཏེ། ཇི་སྲིད་དུ་ཉན་ཐོས་ཀྱི་མཆོག་ཟུང་གཅིག་མ་བྱུང་གི་བར་ཏེ། དེས་ཕྱིར་སྡུམ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2493]
ཐུབ་པ་ནོངས་པ་ནི་སྟོན་པ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ན་མི་འབྱུང་སྟེ། འགྲེན་ཟླ་མེད་པའི་ཕྱིར་རོ། །

[Block 2494]
མཚམས་མ་བཅད་ན་ཡང་མཚམས་གཅིག་གི་ནང་དུ་ཕྱོགས་གཉིས་སུ་གནས་པས་བྱེ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2495]
ཅིའི་ཕྱིར་ཕ་མ་བསད་པ་ལ་སོགས་པ་མཚམས་མེད་པ་ཡིན་ལ། གཞན་ནི་མ་ཡིན་ཞེ་ན།

[Block 2496 [VERSE]]
ཕན་འདོགས་པ་དང་ཡོན་ཏན་ཞིང་། །
སྤངས་དང་མེད་པར་བྱས་ཕྱིར་རོ། །

[Block 2497]
རེ་ཞིག་ཕ་མ་བསད་པ་ནི་ཕན་འདོགས་པ་མེད་པར་བྱས་པའི་ཕྱིར་དང་། ཡོན་ཏན་གྱི་ཞིང་མིན་པའི༌[^992]ཕྱིར་དགྲ་བཅོམ་པ་བསད་པ་ལ་སོགས་པ་ཡང་མཚམས་མེད་པ་ཡིན་ནོ། །

[Block 2498]
གལ་ཏེ་ཕའམ་མ༌[^993]མཚན་གྱུར་པ་ཡང་ལུས་གཅིག་པ་དེ་ལས་ནི།

[Block 2499 [VERSE]]
མཚན་ནི་གཞན་དུ་གྱུར་ཀྱང་འགྱུར། །
དེ་ལ་ཡང༌[^994]མཚམས་མེད་པར་འགྱུར་རོ། །

[Block 2500]
གང་གི་ཚེ་བུད་མེད་གཞན་ལས་ནུར་ནུར་པོ་ཟགས༌[^995]ནས་བུད་མེད་གཞན་གྱི་མངལ་དུ་བླུགས་ན་དེའི་ཚེ་གང་ཞིག་བསད་པ༌[^996]ན་མཚམས་མེད་པར་འགྱུར་བ་དེའི་མ་གང་ཡིན་ཞེ་ན། གང་གི་ཟླ་མཚན་ལས་བྱུང་ངམ། །གང་གི་ཟླ་མཚན་ལས་བྱུང་བ་ནི་དེའི་མ་ཡིན་ནོ། །

[Block 2501]
ཅི་དེ་བཞིན་གཤེགས་པ་ལ་ངན་སེམས་ཀྱིས༌[^997]ཁྲག་བྱུང་བས༌[^998]གདོན་མི་ཟ་བར་མཚམས་མེད་པར་འགྱུར་རམ་ཞེ་ན། བགྲོངས་པར༌[^999]སེམས་པ་ལ་ནི་འགྱུར་གྱི། སངས་རྒྱས་བརྡེག༌[^1000]པར་སེམས་ལ་མིན། །གལ་ཏེ་བརྡེག༌[^1001]པའི་བསམ་པས་འབྱིན་པར་བྱེད་ན་མཚམས་མེད་པར་མི་འགྱུར་རོ། །

[Block 2502]
གལ་ཏེ་དགྲ་མ་ཆོམས་པའི་ཚེ་བསྣུན་ལ་བསྣུན་པའི་འོག་ཏུ་དགྲ་བཅོམ་པར་འགྱུར༌[^1002]ན། བསྣུན་འོག་དགྲ་བཅོམ་པ་ལ་མིན། །དེས་ནི་དགྲ་བཅོམ་པ་ལ་སྦྱོར་བ་མ་བྱས་པའི་ཕྱིར་རོ། །

[Block 2503]
ཅི་མཚམས་མེད་པའི་སྦྱོར་བ་བྱས་ཏེ། དེ་ཡང་མ་བཟློག་པར༌[^1003]འདོད་ཆགས་དང་བྲལ་བའམ་འབྲས་བུ་ཐོབ་པར་འགྱུར་རམ་ཞེ་ན།

[Block 2504 [VERSE]]
མཚམས་མེད་སྦྱོར་བ་བྱས་པ་ལ། །
འདོད་ཆགས་བྲལ་འབྲས་མི་སྲིད་དོ། །

[Block 2505]
གཞན་གྱི་ལས་ཀྱི་ལམ་གྱི་སྦྱོར་བ་བྱས་ནས་འཕགས་པའི་ལམ་བསྐྱེད་པ་ལ་དགག་པ༌[^1004]མེད་དོ། །

[Block 2506]
མཚམས་མེད་པ་འདི་དག་གི་ནང་ནས་ཁ་ན་མ་ཐོ་བ་དང་བཅས་པ་ཆེན་པོ་གང་ཡིན་ཞེ་ན།

[Block 2507 [VERSE]]
དགེ་འདུན་དབྱེ་ཕྱིར་བརྫུན་སྨྲ་བ། །
ཁ་ན་མ་ཐོ་རབ་ཆེར་འདོད། །

[Block 2508]
དེའི་ནི་རྣམ་པར་སྨིན་པ་བསྐལ་པ་གཅིག་ཏུ་མནར་མེད་པར་སྐྱེ་བ་ཡིན་ལ། ལྷག་མ་རྣམས་ལ་ནི་མ་ངེས་སོ། །

[Block 2509]
ལེགས་པར་སྤྱད་པ་གང་ཞིག་འབྲས་བུ་ཆེ་ཞེ་ན།

[Block 2510 [VERSE]]
འཇིག་རྟེན་པ་ཡི་དགེ་བ་ལ། །
སྲིད་རྩེའི་སེམས་པ་འབྲས་རབ་ཆེ། །

[Block 2511]
དེའི་རྣམ་པར་སྨིན་པ་ནི་བསྐལ་པ་བརྒྱད་ཁྲིའི་བར་དུ་ཞི་བ་ཡིན་ནོ། །

[Block 2512 [HEADING]]
##### མཚམས་མེད་པ་དང་ཆ་འདྲ་བ། ^4-3-12-2-0

[Block 2513]
ཅི༌[^1005]མཚམས་མེད་པ་རྣམས་ཁོ་ནས་དམྱལ་བ་དག་ཏུ༌[^1006]གདོན་མི་ཟ་བར་སྐྱེའམ་ཞེ་ན། མཚམས༌[^1007]མེད་པ་དང་ཆ་འདྲ་བས་ཀྱང་གདོན་མི་ཟ་བར་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2514]
དེ་དག་གང་ཡིན་ཞེ་ན། སྨྲས་པ།

[Block 2515 [VERSE]]
མ་དགྲ་བཅོམ་མ་སུན་བྱས་དང་། །
བྱང་ཆུབ་སེམས་དཔའ་ངེས་གནས་དང་། །
སློབ་པ་གསོད་དང་དགེ་འདུན་གྱི། །
འདུ་བའི་སྒོ་ནི་འཕྲོག་པ་དག །
མཚམས་མེད་པ་དང་ཆ་འདྲ་སྟེ། །
ལྔ་པ་མཆོད་རྟེན་འཇིག་པ་ཡིན། །

[Block 2516]
གལ་ཏེ་མི་ཚངས་པར་སྤྱད་པས་མ་དགྲ་བཅོམ་མ་སུན་པར་བྱེད་པ་དང་། ངེས་པར་གཏོགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་གསོད་པ་དང་། སློབ་པ་གསོད་པ་དང་། དགེ་འདུན་གྱི་ཞལ་དུ་འདུ་བའི་སྒོ་འཕྲོག་པ་དང་། མཆོད་རྟེན་འཇིག་པར་བྱེད་པ་དང་ལྔ་པོ་འདི་དག་ནི་མཚམས་མེད་པ་ལྔ་དང་ཆ་འདྲ་བ་ཡིན་ནོ། །

[Block 2517]
རྣམ་པར་སྨིན་པ་དང་བཅས་པའི་ལས་གཞན་ཡང་དུས་གསུམ་པོ་དག་ཏུ་ཤིན་ཏུ་གེགས་བྱེད་དེ། གསུམ་པོ་གང་དག་ཏུ་ཞེ་ན།

[Block 2518 [VERSE]]
བཟོད་དང་ཕྱིར་མི་འོང་དགྲ་བཅོམ། །
འཐོབ་ལ་ལས་གེགས་ཤིན་ཏུ་བྱེད། །

[Block 2519]
རྩེ་མོ་ལས་བཟོད་པ་འཐོབ་པ་ལ་ནི་དེའི་རྣམ་པར་སྨིན་པའི་ས༌[^1008]ལས་འདའ་བའི་ཕྱིར་ངན་སོང་བའི་ལས་རྣམས་གེགས་བྱ་བའི་ཕྱིར་ཉེ་བར་གནས་སོ། །

[Block 2520]
ཕྱིར་མི་འོང་བའི་འབྲས་བུ་འཐོབ་པ་ལ་ནི་འདོད་པ་ན་སྤྱོད་པའི་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བ་མ་ཡིན་པའི་ལས་རྣམས་གེགས་བྱ་བའི་ཕྱིར་ཉེ་བར་གནས་སོ། །

[Block 2521]
དགྲ་བཅོམ་པ་འཐོབ་པ་ལ་ནི་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ལས་དག་གོ། །

[Block 2522 [HEADING]]
#### བྱང་ཆུབ་སེམས་དཔའ། ^4-3-13-0

[Block 2523]
བྱང་ཆུབ་སེམས་དཔའ་བསད་པ༌[^1009]ཞེས་བཤད་པ་གང་ཡིན་པ། གང་ནས་བྱང་ཆུབ་སེམས་དཔའ་ཡིན། །གང་ནས་བཟུང་སྟེ་ངེས་པར་གཏོགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བརྗོད་པར་བྱ། གང་ནས་མཚན་གྱི་ལས་བྱེད་པ། །གང་ཕན་ཆད་ནས་མཚན་རྣམ་པར་སྨིན་པར་འགྱུར་བའི་ལས་རྣམས་བྱེད་པར་རྩོམ་པའོ། །

[Block 2524]
དེ་ནི་དུས་དེ་ཕན་ཆད་རྟག་ཏུ། བདེ་འགྲོར་རིགས་མཐོང་སྐྱེ་དབང་ཚང་། །ཕོར་གྱུར་ཚེ་རབས་དྲན་མི་ལྡོག་པ་ཡིན་ནོ། །

[Block 2525]
དེའི་འགྲོ་བ་རབ་ཏུ་བསྔགས་པ༌[^1010]ནི་ལྷ་དང་མི་ཡིན་ནོ། །
--- END BLOCKS ---
