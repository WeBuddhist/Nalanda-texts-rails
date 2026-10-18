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
གཉིས་པའི་ནི་རྣམ་པར་ཟོས་པ་དང་། རྣམ་པར་འཐོར་བ་ལ་དམིགས་པའོ། །

[Block 2417]
གསུམ་པའི་ནི་རྣམ་པར་འབུས་གཞིགས་པ་དང་། རྒྱུས་པས་བྲང་བྲེང་དུ་སྦྲེལ་བའི་ཀེང་རུས་ལ་དམིགས་པའོ། །

[Block 2418]
བཞི་པའི་ནི་ཤི་བའི་རོ་གཡོ་བ་མེད་པ་ལ་དམིགས་པའོ། །

[Block 2419]
བྱེ་བྲག་མེད་པར་ནི། ཀེང་རུས་ཆགས་བཅས་ཐམས་ཅད་ལ། །ཤིས་ཏེ། རུས་པའི་ཀེང་རུས་ལ་ནི་ཆགས་པའི་གཞི༌[^1744]རྣམ་པ་བཞི་པོ་འདི་དག༌[^1745]ཐམས་ཅད་མེད་དོ། །

[Block 2420]
མོས་པ་དང་ཉི་ཚེ་བ་ཡིད་ལ་བྱེད་པ་ཡིན་པའི་ཕྱིར་མི་སྡུག་པས་ཉོན་མོངས་པ་སྤོང་བ་ནི་མ་ཡིན་གྱི་རྣམ་པར་གནོན་པ་ནི་ཡིན་ནོ། །

[Block 2421 [HEADING]]
###### **མི་སྡུག་པ་བསྒོམ་པའི་རྣལ་འབྱོར་སྤྱོད་པ་རྣམ་པ་གསུམ།** ^3-1-3-4-1-2-0

[Block 2422]
མི་སྡུག་པ་བསྒོམ་པའི༌[^1746]རྣལ་འབྱོར་སྤྱོད་པ་དེ་ནི་རྣམ་པ་གསུམ་དུ་བརྗོད་དེ། ལས་དང་པོ་པ་དང་། ཡོངས་སུ་སྦྱང་བ་བྱས་པ་དང་། ཡིད་ལ་བྱེད་པ་རྫོགས་པའོ། །

[Block 2423 [HEADING]]
###### **ལས་དང་པོ་པ།** ^3-1-3-4-1-2-1-0

[Block 2424]
དེ་ལ་རུས་པ་རྒྱ་མཚོའི་བར་དུ་ནི། །སྤྲོ་ཞིང་སྡུད་པ་ལས་དང་པོ། །མི་སྡུག་པ་བསྒོམ་པར༌[^1747]འདོད་པའི་རྣལ་འབྱོར་སྤྱོད་པ་ནི་དང་པོ་ཉིད་དུ་རང་གི་ལུས་ཀྱི་ཡན་ལག་རྐང་པའི་མཐེ་བོའམ། དཔྲལ་བའི་དབྱེས་སམ། ཡང་ན་དེ་གར་དགའ་བར་སེམས་གཏོད་པར་བྱེད་ཅིང་། དེས་དེར་ཤ་མྱགས་ཤིང་ཟག་པར་མོས་པས༌[^1748]རིམ་གྱིས་རུས་པ་རྣམ་པར་སྦྱོང་བར་བྱེད་པ་ན་ཐམས་ཅད་རུས་པའི་ཀེང་རུས་སུ་ལྟ་ཞིང་། དེ་བཞིན་དུ་མོས་པ་བསྐྱེད་པའི་ཕྱིར་གཉིས་པ་ལ་མོས་པར་བྱེད་པ་ནས་གཙུག་ལག་ཁང་དང་། ཀུན་དགའི་ར་བ་དང་། གྲོང་དང་། ཞིང་དང་རིམ་གྱིས་རྒྱ་མཚོའི་མཐས་ཀླས་པའི་བར་གྱི་ས་གཞི་རུས་པའི་ཀེང་རུས་ཀྱིས་གང་བར་མོས་པར་བྱེད་དོ། །

[Block 2425]
ཡང་སྡུད་པ་ན་སེམས་བསྡུ་བའི་ཕྱིར་བདག་གཅིག་པུ་ཁོ་ན་ལ་རུས་པའི་ཀེང་རུས་སུ་མོས་པའི་བར་དུ་སྡུད་དེ། འདི་ཙམ་གྱིས་ན་མི་སྡུག་པ་ཡོངས་སུ་རྫོགས་པ་ཡིན་ནོ་ཞེས་གྲག་སྟེ། འདི་ནི་ལས་དང་པོ་པའི་རྣལ་འབྱོར་སྤྱོད་པ་ཡིན་ནོ། །

[Block 2426 [HEADING]]
###### **ཡོངས་སུ་སྦྱང་བ་བྱས་པ།** ^3-1-3-4-1-2-2-0

[Block 2427 [VERSE]]
རྐང་རུས་ནས་ནི་ཐོད་ཕྱེད་པར། །
བཏང་བས་སྦྱང་བ་བྱས་པར་བཤད། །

[Block 2428]
དེ་སེམས་བསྡུ་བ་ཁྱད་པར་ཅན་དུ་བྱ་བའི་ཕྱིར་རུས་པའི་ཀེང་རུས་དེ་ལས་རྐང་པའི་རུས་པ་རྣམས་བོར་ནས་ལྷག་མ་ཡིད་ལ་བྱེད་ཅིང་། དེ་བཞིན་དུ་ཐོད་པའི་བྱེད༌[^1749]བོར་ནས་ཐོད་པ་ཕྱེད་ཀྱི་བར་ཡིད་ལ་བྱེད་པ་འདི་ནི་ཡོངས་སུ་སྦྱང་བ་བྱས་པ་ཡིན་ནོ། །

[Block 2429 [HEADING]]
###### **ཡིད་ལ་བྱེད་པ་རྫོགས་པ།** ^3-1-3-4-1-2-3-0

[Block 2430]
སྨིན་མའི་བར་དུ་སེམས་འཛིན་པས། ཡིད་ལ་བྱེད་པ་རྫོགས་པ་ཡིན། དེ་ཐོད་པའི་ཕྱེད་ཀྱང་བོར་ནས་སྨིན་མ་གཉིས་ཀྱི་བར་དུ་སེམས་འཛིན་པར་བྱེད་པ་འདི་ནི་མི་སྡུག་པ་ཡིད་ལ་བྱེད་པ་རྫོགས་པའི་རྣལ་འབྱོར་སྤྱོད་པ་ཡིན་ནོ་ཞེས་གྲག་གོ། །

[Block 2431]
དམིགས་པ་ཆུང་བས་ཆུང་ལ་དབང་ཆུང་བས་མ་ཡིན་པས་ཡང་མི་སྡུག་པ་ཡང་ཡོད་དེ་ཞེས་བྱ་བ་མུ་བཞི་སྟེ། ཡིད་ལ་བྱེད་པ་སྦྱང་བ་བྱས་པ་དང་། སྦྱང་བ་མ་བྱས་པ་དག་དང་། ཡིད་ལ་བྱེད་པ་སྦྱང་བ་མ་བྱས་པ་དང་། སྦྱང་བ་བྱས་པ་དག་རང་གི་ལུས་དང་རྒྱ་མཚོའི་མཐའ་ཀླས་པ་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 2432 [HEADING]]
###### **མི་སྡུག་པའི་རང་བཞིན་ལ་སོགས་པ།** ^3-1-3-4-1-3-0

[Block 2433]
ཡང་མི་སྡུག་པ་འདིའི་རང་བཞིན་ཅི་ཞིག་ཡིན། ས་ནི་དུ་ཞིག་ཡིན། དམིགས་པ་ནི་ཅི་ཞིག་ཡིན། གང་དུ༌[^1750]སྐྱེད་པར་བྱེད་ཅེ་ན། གོ་རིམས་བཞིན་དུ། མི་སྡུག་མ་ཆགས་ས་བཅུ་དང་། དམིགས་པ་འདོད་སྣང་མིས་སྐྱེད༌[^1751]དོ། །

[Block 2434]
རང་བཞིན་ནི་མ་ཆགས་པའོ། །

[Block 2435]
ས་ནི་བཅུ་པ༌[^1752]སྟེ། བསམ་གཏན་བཞི་ཉེར་བསྡོགས་དང་བསམ་གཏན་ཁྱད་པར་ཅན་དང་བཅས་པ་དང་། འདོད་པའི་ཁམས་ན་ཡོད་དོ། །

[Block 2436]
དམིགས་པ་ནི་འདོད་པ་ན་སྤྱོད་པའི་སྣང་བ་ཡིན་ནོ། །

[Block 2437]
སྣང་བ་ཞེས་བྱ་བ་ཅི་ཞེ་ན། ཁ་དོག་དང་། དབྱིབས་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་དོན་ལ་དམིགས་པ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 2438]
མི་རྣམས་ཀྱི་ནང་ཁོ་ནར་སྐྱེད་ཀྱི་འགྲོ་བ་གཞན་དུ་ཡང་མ་ཡིན་ན་ཁམས་གཞན་དུ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། དེར་ཡང་བྱང་གི་སྒྲ་མི་སྙན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 2439]
མི་ཉིད་ཀྱིས་མི་སྡུག་པའི་རྣམ་པ་ཞེས་བྱ་བར༌[^1753]གྲུབ་པོ། །དུས་གང༌[^1754]ཡིན་པ་དེའི་དུས་ལ་དམིགས་སོ། །

[Block 2440]
མི་སྐྱེ་བའི་ཆོས་ཅན་གྱི་ཡུལ་ནི་དུས་གསུམ་ཡིན་ནོ། །

[Block 2441]
མོས་པ་ཡིད་ལ་བྱེད་པ་ཡིན་པའི་ཕྱིར་ཟག་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 2442]
འདྲིས་པ་དང་མ་འདྲིས་པ་ཡིན་པའི་ཕྱིར་འདོད་ཆགས་དང་བྲལ་བས་ཐོབ་པ་དང་སྦྱོར་བ་ལས་བྱུང་བ་ཡིན་ནོ། །

[Block 2443]
མི་སྡུག་པའི་མཚན་ཉིད་རབ་ཏུ་དབྱེ་བ་དང་བཅས་ཏེ་བཤད་ཟིན་ཏོ། །

[Block 2444 [HEADING]]
###### དབུགས་རྔུབ་པ་དང་འབྱུང་བ་དྲན་པ། ^3-1-3-4-2-0

[Block 2445 [VERSE]]
དབུགས་རྔུབ་དབུགས་འབྱུང་དྲན་པ་ནི། །
ཤེས་རབ་ས་ལྔ་སྤྱོད་ཡུལ་རླུང་། །

[Block 2446]
འདོད་རྟེན། དབུགས་རྔུབ་པ་ནི༌[^1755]དབུགས་རྔུབ་པ་སྟེ་རླུང་འཇུག་པ་གང་ཡིན་པའོ། །

[Block 2447]
དབུགས་འབྱུང་བ་ནི་དབུགས་འབྱིན་པ་སྟེ་རླུང་འབྱུང་བ་གང་ཡིན་པའོ། །

[Block 2448]
དེ་གཉིས་དྲན་པ་ནི་དབུགས་རྔུབ་པ་དང་དབུགས༌[^1756]འབྱུང་བ་དྲན་པ་སྟེ། དེ་ནི་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་ནོ། །

[Block 2449]
དྲན་པ་ཞེས་སྨོས་པ་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་སྟེ། དེའི་སྟོབས་བསྐྱེད་པས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 2450]
ས་ལྔ་པོ་ཉེར་བསྡོགས་གསུམ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། འདོད་པའི་ཁམས་ན་ཡོད་དོ། །

[Block 2451]
[^1757]བཏང་སྙོམས་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2452]
བདེ་བ་དང་སྡུག་བསྔལ་དག་ནི་རྣམ་པར་རྟོག་པ་དང་མཐུན་པའི་ཕྱིར་དེའི་གཉེན་པོ་ནི་དེ་དག་དང་མཚུངས་པར་མི་ལྡན་ནོ། །

[Block 2453]
བདེ་བ་དང་ཡིད་བདེ་བ་དག་ཀྱང་གཏོད་པ་ལ་བར་ཆད་བྱེད་པའི་ཕྱིར་ལ། དེ་ཡང་གཏད་པས་བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་གྲག་གོ། །

[Block 2454]
གང་དག་བསམ་གཏན་དངོས་གཞི་དག་ན་ཡང་སྙོམས་པར་ཞུགས་པ་ལ་བཏང་སྙོམས་ཀྱི་དབང་པོ་ཡོད་པར་འདོད་པ་དེ་དག་གི་ལྟར་ན་ས་བརྒྱད་པ་ཡིན་ནོ། །

[Block 2455]
ཡན་ཆད་ནི་དབུགས་རྔུབ་པ་དང་དབུགས་འབྱུང་བའི་ས་མ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
