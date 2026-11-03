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
[Block 2696]
[^2368]བཏང་སྙོམས་ནི་སྡིག་པ་མི་དགེ་བའི་ཆོས་དང་མཐུན་པ་དག་ལ་སྤྱོད་པའི་སེམས་ཀུན་ནས་ཉོན་མོངས་པ་མེད་ཅིང༌[^2369]མཉམ་པ་ཉིད་དུ་བྱེད་པའོ། །

[Block 2697]
དེ་ལ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་མངོན་པར་སྒྲུབ་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའ་དེ་ལ་འདུན་པ་ལ་སོགས་པ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་སྒྲུབ་པ་རྣམས་ཀྱིས༌[^2370]རྫུ་འཕྲུལ་ཡང་དག་པར་སྒྲུབ་པར་བྱེད་དེ། དེ་བས་ན་འདུན་པ་ལ་སོགས་པ་ལ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་ཞེས་བྱའོ། །

[Block 2698]
དེ་ལ་འདུན་པ་དང་རྫུ་འཕྲུལ་གྱི་རྐང་པས་ནི་རྫུ་འཕྲུལ་སྒྲུབ༌[^2371]པའོ། །

[Block 2699]
བརྩོན་འགྲུས་རྫུ་འཕྲུལ་གྱི༌[^2372]རྐང་པས་ནི་རྫུ་འཕྲུལ་མཐར་འབྱིན་པར་བྱེད་དོ། །

[Block 2700]
སེམས་རྫུ་འཕྲུལ་གྱི་རྐང་པས་ནི་མཐར་དབྱུང་བའི་རྫུ་འཕྲུལ་རྣམས་མི་ཉམས་པར་བྱེད་དོ། །

[Block 2701]
དཔྱོད་པ་རྫུ་འཕྲུལ་གྱི་རྐང་པས་ནི་རྫུ་འཕྲུལ་དེ་དག་གཏན་ལ་འབེབས་ཤིང་གང་དང་གང་བྱ་བ་མངོན་པར་བྱེད་པའོ། །

[Block 2702]
མོས་པ་ལས་བྱུང་བ༌[^2373]མངོན་པར་འདུ་བྱེད་པ་མེད་པ་ཞེས་བྱ་བ་ལས་དང་པོ་པའི་རྫུ་འཕྲུལ་རྣམས་ནི་དེ་ཁོ་ན་མ་རྟོགས་པས༌[^2374]དངོས་པོ་འདི་ལྟར་གྱུར་ཅིག་ཅེས། མངོན་སུམ་དུ་མ་གྱུར་པ་ལ་སེམས་ཀྱིས་མོས་པ་བསྐྱེད་ནས་བརྩལ་བ༌[^2375]ལས་འབྱུང་གི །བྱང་ཆུབ་སེམས་དཔའ་ཡོངས་སུ་སྦྱང་བ༌[^2376]བྱས་པ་རྣམས་གདོད་སྨོན་ཅིང་འབད་པ་དང་བརྩལ༌[^2377]མི་དགོས་པར་བསམས་པ༌[^2378]ཙམ་གྱིས་ལྷུན་གྱིས་གྲུབ་པ་ཉིད་དུ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་རྫོགས་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2703]
དེ་བས་ན་རང་གི་སེམས་པ་སྐྱེད་པས་དབང་བྱེད་པ་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་འགྲོ་ཞེས་བྱ་བ་གསུངས་ཏེ། ཏིང་ངེ་འཛིན་མཉམ་པར་གཞག་པ་ལ་སོགས་པ་རྒྱུ་རྐྱེན་གཞན་ལ་མི་ལྟོས་པར༌[^2379]དངོས་པོ་འདི་འདི་ལྟར་བྱའོ་སྙམ་དུ་རང་གི་སེམས་བསྐྱེད་པ་ཙམ་གྱིས་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་དབང་དུ་འགྱུར་བའོ། །

[Block 2704]
ཡོངས་སུ་སྦྱང་བ་ལེགས་པར་བྱས་པས༌[^2380]ནི་མཐར་ཕྱུང་ཞིང་ལས་སུ་རུང་བར་བྱས་པའོ། །

[Block 2705]
རྩ་བ་ལ་ཤིན་ཏུ་གནས་པ་ནི་དད་པ་ལ་སོགས་པའམ། བྱམས་པ་ལ་སོགས་པའི་ཚད་མེད་པ་བཞིའི་རྩ་བ་ལ༌[^2381]གནས་པའོ། །

[Block 2706]
ཐམས་ཅད་དུ་རྒྱུ་བ་ནི་ཀུན་དུ་ཁྱབ་པར་བྱེད་ཅིང་སངས་རྒྱས་ཀྱི་ཞིང་ཐམས་ཅད་དུ་འགྲོ་བའོ། །

[Block 2707]
རླུང་དམར་བཞིན་དུ་ཐོགས་པ་མེད་པ་ནི་རླུང་དམར་དང་འདྲ་བར་ཐགས༌[^2382]ཐོགས་མེད་པར་འགྲོ་བའོ། །

[Block 2708]
ནམ་མཁའི་མཐར་ཐུག་པ་ནི་ནམ་མཁའ༌[^2383]དང་འདྲ་བར་ཕྱི་མའི་མཐའི་བར་དུ་ཡང་ཉམས་པ་མེད་པའོ། །

[Block 2709]
རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 2710 [HEADING]]
### དབང་པོ་ལྔ་མི་ཟད་པ། ^8-4-0

[Block 2711]
དད་པའི་མཆོག་དང་བརྩོན༌[^2384]འགྲུས་ཀྱི་མཆོག་དང་། དྲན་པའི་མཆོག་དང་། ཏིང་ངེ་འཛིན་གྱི༌[^2385]མཆོག་དང་། ཤེས་རབ་ཀྱི་མཆོག་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ༌[^2386]ཏིའི་བུ། གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་དབང་པོ་ལྔ་མི་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2712]
དེ་དག་མི་ཟད་པ་ཡང་དད་པར་བྱ་བ་ཆོས་དང་དངོས་པོ་མི་ཟད་པའི་ཕྱིར། དེ་ལ་དད་པར་བྱེད་པ་ལ་སོགས་པ་ཡང་མི་ཟད་པའོ། །

[Block 2713]
འདིར་ཡང་བསྟན་པ་དང་བཤད་པའི་ཚུལ་དུ་རིག་པར་བྱ་སྟེ། དེ་ལ་དབང་པོ་ལྔ་གང་ཞེ་ན་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཤེས་རབ་ཀྱི་དབང་པོ་ཞེས་བྱ་བ་ཡན་ཆད་ནི་བསྟན་པའི་ཚུལ་ལོ། །

[Block 2714]
ལྷག་མ་རྣམས་ནི་བཤད་པའི་ཚུལ་ལོ། །

[Block 2715 [HEADING]]
#### དད་པ་མཆོག། ^8-4-1-0

[Block 2716]
དད་པ་མཆོག་གི༌[^2387]བྱང་ཆུབ་སེམས་དཔའ་ནི་དད་པའི་དབང་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་སྟེ། འཇིག་རྟེན་པའི་དད་པའི་ནང་ན་འཇིག་རྟེན་ལས་འདས་པའི་དད་པ་མཆོག་དམ་པ། ཁྱད་ཞུགས་པ། བླ་མར་གྱུར་པ། བླ་ན་མེད་པ་དང་ལྡན་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས་དེ་ལ་དད་པའི་དབང་པོ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2717]
དད་པའི་མཆོག་ལ་ཇི་ལྟ་བ་དེ་བཞིན་དུ་ཤེས་རབ་ཀྱི་མཆོག་གི་བར་དུ་སྦྱར་རོ། །

[Block 2718]
དད་པ་ཉིད་དབང་པོ་ཡིན་པས་ན་དད་པའི་དབང་པོ་སྟེ། དབང་པོའི་དོན་ནི་ཕྱིས་བཤད་དོ། །

[Block 2719]
དད་པ་གང་གིས་ཞེས་བྱ་བ་ནི་དམིགས་པར་གྱུར་པ་སྟེ། སེམས་དང་བ་དང་། ཡིད་ཆེས་པར་གྱུར་པ་གང་གིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2720]
ཆོས་བཞི་ལ་འདོད་པ་སྟེ་ཞེས་བྱ་བ་ནི་དམིགས་པར་བྱ་བ་ལ་བྱ་སྟེ། དེ་དག་ལ་དེ་བཞིན་དུ་ཡིད་ཆེས་པའོ། །

[Block 2721]
འདི་ལྟ་སྟེ་འཁོར་བ་ནས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ།[^2388] སྲོག་གི་ཕྱིར་ཡང་སྡིག་པ་མི་བྱེད་པ་ཡན་ཆད༌[^2389]ཆོས་གཅིག་གོ། །

[Block 2722]
བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་དད་པས་ཏེ་ཞེས་བྱ་བ་ནས། ཐེག་པ་གཞན་ལ༌[^2390]འདོད་པ་མི་སྐྱེད་པ་ཞེས་བྱ་བའི་བར་དུ་ཆོས་གཉིས་སོ། །

[Block 2723]
ཆོས་ཐམས་ཅད་ལ་དོན་དམ་པར༌[^2391]ཞེས་བྱ་བ༌[^2392]ནས། བག་ལ་ཉལ་བར་མི་བྱེད་པ་དང་ཞེས་བྱ་བ་ཡན་ཆད་ཆོས་གསུམ་མོ། །

[Block 2724]
སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པ༌[^2393]ཞེས་བྱ་བ་ནས། ཆོས་དེ་དག་ཡང་དག་པར་སྒྲུབ་པ༌[^2394]སྟེ་ཞེས་བྱ་བ་ཡན་ཆད་ཆོས་བཞིའོ། །

[Block 2725 [HEADING]]
##### འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་ལ་དད་པ། ^8-4-1-1-0

[Block 2726]
འཁོར་བ་ན་ཡོད་པའི་འཇིག་རྟེན་པའི༌[^2395]ཡང་དག་པའི་ལྟ་བ་ལ་དད་པ་སྟེ་ཞེས་བྱ་བ་ནི་འཕགས་པ་མ་ཡིན་པ་སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱི་སྤྱོད་པ་ལས་དང་འབྲས་བུ་དང་། དཀོན་མཆོག་ལ་སོགས་པ་ཡོད་པར་ལྟ་བ་ལ། འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་ཞེས་བྱ་སྟེ། ཡོད་པར་ལྟ་བ་དེ་ལ་དད་པའོ། །

[Block 2727]
དེ་བས་ན་དེ་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ལ་རྟོན་པ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2728]
དེ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་ལ་དད་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེའོ། །

[Block 2729]
ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ལ་རྟོན་པ་ནི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཡོད་པར་ལྟ་བའོ། །

[Block 2730 [HEADING]]
##### བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་དད་པ། ^8-4-1-2-0

[Block 2731]
བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་དད་པ་སྟེ་ཞེས་བྱ་བ་ནི་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ཆོས་དང་། དེ་དག་གི་ཡོན་ཏན་ལ་དད་ཅིང་ཡིད་ཆེས་པའོ། །

[Block 2732]
སྤྱོད་པ་དེ་ལ་ཞུགས་པ་ནི་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྤྱོད་པ་ལ་ཞུགས་པའོ། །

[Block 2733]
ནས༌[^2396]ཀྱང་ཞེས་བྱ་བ་ནི་ཞུགས་ཕན་ཆད༌[^2397]དོ། །

[Block 2734]
ཐེག་པ་གཞན་ལ་འདོད་པ་མི་སྐྱེད་པ་ནི་ཉན་ཐོས་ལ་སོགས་པའི་ཐེག་པ་ལ་མི་སྤྱོད་པའོ། །

[Block 2735 [HEADING]]
##### ཆོས་ཐམས་ཅད་ལ་དོན་དམ་པ། ^8-4-1-3-0
--- END BLOCKS ---
