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
བཟློག་པ་དེ་ཡི༌[^1734]གཉེན་པོ་དག །ཆོག་མི་ཤེས་པ་དང་། འདོད་ཆེན་ཅན་ལས་བཟློག་པ་ནི་དེ་དག་གི་གཉེན་པོ་ཆོག་ཤེས་པ་དང་། འདོད་ཆེན་ཆུང་བ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2382]
དེ་གཉིས་ཁམས་གསུམ་གཏོགས་དྲི་མེད། །དེའི་གཉེན་པོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཁམས་གསུམ་པ་དག་དང་། མི་ལྡན་པ་དག་ཀྱང་ཡིན་ནོ། །

[Block 2383]
ཆོག་མི་ཤེས་པ་དང་། འདོད་ཆེན་ཅན་ནི་འདོད་པ་ན་སྤྱོད་པ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 2384]
འདོད་ཆེན་ཆུང་བ་དང་ཆོག་ཤེས་པ་འདི་གཉིས་ཀྱི་རང་བཞིན་ཅི་ཞེ་ན། མ་ཆགས་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་དག་ནི་མ་ཆགས་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 2385 [HEADING]]
###### འཕགས་པའི་རིགས་བཞི། ^3-1-3-3-2-0

[Block 2386]
འཕགས་རིགས་མ་ཆགས་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདི་དག་ལས་འཕགས་པ་རྣམས་སྐྱེ་བས་ན་འཕགས་པའི་རིགས་བཞི་སྟེ། དེ་དག་ཀྱང་མ་ཆགས་པའི་རང་བཞིན༌[^1735]ནོ། །

[Block 2387]
དེ་དག་ལས་གསུམ་ནི་ཆོག་ཤེས་བདག་ཉིད་དོ། །

[Block 2388]
དང་པོ་གསུམ་པོ་ཆོས་གོས་དང་། བསོད་སྙོམས་དང་། མལ་ཆ་དང་སྟན་གྱིས་ཆོག་ཤེས་པ་རྣམས་ནི་ཆོག་ཤེས་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 2389]
འཕགས་པའི་རིགས་བཞི་པ་ནི་སྤོང་བ་དང་བསྒོམ་པ་དག༌[^1736]ལ་དགའ་བ་ཉིད་ཡིན་ནོ། །ཇི་ལྟར་ན་མ་ཆགས་པའི་རང་བཞིན་ཡིན་ཞེ་ན། སྲིད་པ་དང་འདོད་པའི་འདོད་ཆགས་ལ་རྒྱབ་ཀྱིས་ཕྱོགས་པའི་ཕྱིར་རོ། །

[Block 2390]
ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་འཕགས་པའི་རིགས་བཞིས་ཅི་ཞིག་བསྟན་ཅེ་ན། གསུམ་གྱིས༌[^1737]ཚུལ་བསྟན་ཐམས་ཅད༌[^1738]ལས། །

[Block 2391]
ཆོས་ཀྱི་རྗེ་བཅོམ་ལྡན་འདས་ཀྱིས། རང་གི་ཚུལ་དང་ལས་ཀྱི་མཐའ་ཡོངས་སུ་སྤངས་ཤིང༌[^1739]ཐར་པ་དོན་དུ་གཉེར་བར་ཁས་འཆེ་བའི༌[^1740]སློབ་མ་རྣམས་ལ་ཚུལ་དང་ལས་གཉིས་བཅས་ཏེ། འཕགས་པའི་རིགས་གསུམ་གྱིས་ནི་ཚུལ་བཅས་སོ། །

[Block 2392]
བཞི་པས་ནི་ལས་བཅས་ཏེ། ཁྱེད་ཚུལ་འདིས་ལས་འདི་བྱེད་ན་རིང་པོར༌[^1741]མི་ཐོགས་པར་ཐར་པ་ཐོབ་པར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 2393]
ཅིའི་ཕྱིར་ཚུལ་འདི་ལྟ་བུ་དང་། ལས་འདི་ལྟ་བུ་བཅས་ཤེ་ན། སྲེད་པ་སྐྱེ་བའི་གཉེན་པོའི་ཕྱིར། མདོ་ལས་སྲེད་པ་སྐྱེ་བ་བཞི་གསུངས་ཏེ། དགེ་སློང་སྲེད་པ་སྐྱེ་བ་ན་ཆོས་གོས་ཀྱི་ཕྱིར་དང་། བསོད་སྙོམས་ཀྱི་ཕྱིར་དང་། མལ་ཆ་དང་སྟན་གྱི་ཕྱིར་སྐྱེའོ། །

[Block 2394]
གནས་པ་ན་གནས་སོ། །

[Block 2395]
མངོན་པར་ཞེན་པ་ན་མངོན་པར་ཞེན་ཏོ། །

[Block 2396]
དགེ་སློང་སྲེད་པ་སྐྱེ་བ་ན་འབྱུང་བ་དང་འཇིག་པ་དེ་ལྟ་བུའི་ཕྱིར་སྐྱེའོ་ཞེས་རྒྱས་པར་གསུངས་ཏེ། དེ་དག་གི་གཉེན་པོར་འཕགས་པའི་རིགས་བཞི་བསྟན་ཏོ། །

[Block 2397 [VERSE]]
བདག་གི་བདག་འཛིན་དངོས་འདོད་པ། །
དེ་ཡི་དུས་དང་གཏན་ཞི༌[^1742]ཕྱིར། །

[Block 2398]
དོན་དེ་ཉིད་རྣམ་གྲངས་ཀྱིས་སྟོན་པ་སྟེ། བདག་གིར་འཛིན་པའི་དངོས་པོ་ནི་ཆོས་གོས་ལ་སོགས་པའོ། །

[Block 2399]
བདག་ཏུ་འཛིན་པའི་དངོས་པོ་ནི་ལུས་སོ། །

[Block 2400]
དེ་དག་ལ་འདོད་པ་ནི་སྲེད་པའོ། །

[Block 2401]
དེ་ལ་འཕགས་པའི་རིགས་གསུམ་ནི་བདག་གིར་འཛིན་པའི་དངོས་པོ་འདོད་པ་དེའི་དུས་སུ་ཞི་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 2402]
བཞི་པ་ནི་གཉི་ག་འདོད་པ་གཏན་དུ་ཞི་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 2403]
ཇི་ལྟ་བུའི་བསྒོམ་པ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་བ་འདི་ནི་བཤད་ཟིན་ཏོ། །

[Block 2404 [HEADING]]
##### བསྒོམ་པ་ལ་འཇུག་པའི་སྒོ་གཉིས། ^3-1-3-4-0

[Block 2405]
དེ་ལྟར་སྣོད་དུ་གྱུར་པ་དེ་ཇི་ལྟར་ན་བསྒོམ་པ་དེ་ལ་འཇུག་པ་ཡིན་ཞེ་ན།

[Block 2406 [VERSE]]
དེ་ལ་འཇུག་པ་མི་སྡུག་དང་། །
དབུགས་རྔུབ་འབྱུང་བ་དྲན་པ་ཡིས། །
དྲན་པ་ཉིད་དྲན་པ་ཡིན་ནོ། །
གང་དག་ནི་མི་སྡུག་པས་འཇུག །

[Block 2407]
གང་དག་ནི་དབུགས་རྔུབ་པ་དང་འབྱུང་བ་དྲན་པས་འཇུག་ཅེ་ན། གོ་རིམས་བཞིན་དུ། འདོད་ཆགས་རྣམ་རྟོག་ལྷག་རྣམས་སོ། །

[Block 2408]
འདི་དག་ལ་འདོད་ཆགས་དང་རྣམ་པར་རྟོག་པ་ལྷག་པ་ཡོད་པས། འདི་དག་ནི་འདོད་ཆགས་དང་རྣམ་པར་རྟོག་པ་ལྷག་པ་དག་སྟེ། གང་ཞིག་འདོད་ཆགས་ཉེ་བ་དང་ཤིན་ཏུ་སྤྱད་པ་དེ་ནི་མི་སྡུག་པས་འཇུག་གོ། །

[Block 2409]
གང་ཞིག་རྣམ་པར་རྟོག་པ་སྤྱད་པ་དེ་ནི་དབུགས་རྔུབ་པ་དང་འབྱུང་བ་དྲན་པས་འཇུག་གོ། །

[Block 2410]
ཁ་ཅིག་ན་རེ་འདི་ནི་སྣ་ཚོགས་ལ་མི་དམིགས་པའི་ཕྱིར་རྣམ་པར་རྟོག་པ་གཅོད་པར་བྱེད་པ་ཡིན་གྱི། མི་སྡུག་པ་ནི་ཁ་དོག་དང་དབྱིབས་ཀྱི་བྱེ་བྲག་ལ་དམིགས་པའི་ཕྱིར་རྣམ་པར་རྟོག་པ་འདྲེན་པར་བྱེད་དོ་ཞེས་ཟེར་རོ། །

[Block 2411]
གཞན་དག་ན་རེ་ཁ་ཕྱིར་མ་བལྟས་པའི་ཕྱིར་ཏེ། མི་སྡུག་པ་ནི་མིག་གི་རྣམ་པར་ཤེས་པ་བཞིན་དུ་ཁ་ཕྱིར་བལྟས་པ་ཡིན་ཏེ། དེའི་ཡུལ་ལ་ཉེ་བར་རྟོག་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 2412 [HEADING]]
###### མི་སྡུག་པ། ^3-1-3-4-1-0

[Block 2413 [HEADING]]
###### **འདོད་ཆགས་རྣམ་པ་བཞིའི་གཉེན་པོ།** ^3-1-3-4-1-1-0

[Block 2414]
དེ་ལ༌[^1743]འདོད་ཆགས་ནི་རྣམ་པ་བཞི་སྟེ། ཁ་དོག་གི་འདོད་ཆགས་དང་། དབྱིབས་ཀྱི་འདོད་ཆགས་དང་། རེག་པའི་འདོད་ཆགས་དང་། བསྙེན་བཀུར་གྱི་འདོད་ཆགས་སོ། །

[Block 2415]
དང་པོའི་གཉེན་པོར་ནི་རྣམ་པར་བསྔོས་པ་ལ་སོགས་པ་ལ་དམིགས་པའི་མི་སྡུག་པ་རྗོད་པར་བྱེད་དོ། །

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
--- END BLOCKS ---
