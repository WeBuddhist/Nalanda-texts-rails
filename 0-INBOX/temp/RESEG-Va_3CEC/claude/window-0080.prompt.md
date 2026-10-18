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
[Block 2801]
ལྷར་བཅས་པའི་འཇིག་རྟེན་ཞེས་བྱ་བ་ནི་ལྷ་དང་ལྷ་ལས་གཞན་པའི་འཇིག་རྟེན་གྱིས་ཀྱང་རུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2802 [HEADING]]
#### དྲན་པ་མི་ཚུགས་པ། ^8-5-3-0

[Block 2803]
དྲན་པ་མི་ཚུགས་པ་ནི་གང་དྲན་པའི་སྟོབས་ལ༌[^2440]རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་དྲན་པའི་སྟོབས་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2804]
དེ་ཞེས་བྱ་བ་ནི་དྲན་པའི་སྟོབས་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེའོ། །

[Block 2805]
ཆོས་ནི་ཕུང་པོ་དང་ཁམས་ལ་སོགས་པ་གང་ཡང་རུང་པའོ། །

[Block 2806]
དྲན་པའི་གནས་གང་དང་གང་ལ་ཞེས་བྱ་བ་ནི་དྲན་པས་དམིགས་པར་བྱ་བའི་ཡུལ་གང་དང་གང་ལ་ཞེས་བྱ་བའི༌[^2441]དོན་ཏོ། །

[Block 2807]
སེམས་འཇོག་པ༌[^2442]ནི་དེ་ལ་དམིགས་ཤིང་མི་བརྗེད་པར་བྱེད་པའོ། །

[Block 2808]
དེ་ལ་ཞེས་བྱ་བ་ནི་ཆོས་ལ་དམིགས་ཤིང་མི་བརྗེད་པར་བྱེད་པའི་དྲན་པ་དེ་ལས་སོ། །

[Block 2809]
ཉོན་མོངས་པ་གང་ཡང་རུང་བས་སྟོང་པར་མི་ནུས་ཞེས་བྱ་བ་ནི་དྲན་པ་ཉམས་པ་དང་། གཉིད་དང་། རྨུགས་པ་དང་། འདོད་ཆགས་དང་ཞེ་སྡང་ལ་སོགས་པ་ཉོན་མོངས་པ་གང་ཡང་རུང་བས་མེད་པར་བྱ་ཞིང་བར་དུ་གཅོད་པར་མི་ནུས་པའོ། །

[Block 2810]
དེའི་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེའི་འོ། །

[Block 2811]
དྲན་པའི་སྟོབས་སྐྱེད་པ༌[^2443]ནི་དྲན་པའི་མཐུ་དང་ལྡན་པའོ། །

[Block 2812]
འཇོམས་པ་ནི་ཉོན་མོངས་པ་སྤོང་བའོ། །

[Block 2813]
མི་བརྫི་བ༌[^2444]ནི་ཉོན་མོངས་པའི་དབང་དུ་མི་འགྱུར་བའོ། །

[Block 2814 [HEADING]]
#### ཏིང་ངེ་འཛིན་མི་ཚུགས་པ། ^8-5-4-0

[Block 2815]
ཏིང་ངེ་འཛིན་མི་ཚུགས་པ་ནི་ཏིང་ངེ་འཛིན་གྱི་སྟོབས་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཏིང་ངེ་འཛིན་གྱི་སྟོབས་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2816]
གང༌[^2445]ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་གྱི་སྟོབས་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ལ་སྙེགས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་དེ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2817]
འདུ་འཛི༌[^2446]ཐམས་ཅད་ལས་དབེན་པར་གནས་ཤིང་ཞེས་བྱ་བ་ནི་འགྲོ་བ་མང་བའི༌[^2447]ནང་ན༌[^2448]གནས་པ་སྤངས་ནས་ཏིང་ངེ་འཛིན་ལ་སེམས་རྩེ་གཅིག་ཏུ་འཇོག་པ་སྟེ། འདིར་ཡང་དེ་ལྟ་མོད་ཀྱི། ཏིང་ངེ་འཛིན་གྱི་མཐུ་དང་ལྡན་པ༌[^2449]ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2818]
དེའི་སྒྲ་དང་ཚིག་གི་ལམ་ཐམས་ཅད་ཀྱིས༌[^2450]ཞེས་བྱ་བ་ནི། བསམ་གཏན་དང་པོ་ལ་སྒྲ་ཅ་ཅོ་རྣམས་བར་དུ་གཅོད་པར་མི་འགྱུར་ཏེ། བྱང་ཆུབ་སེམས་དཔའི༌[^2451]ཏིང་ངེ་འཛིན་གྱི་མཐུ་དང་ལྡན་པས་བསམ༌[^2452]གཏན་དང་པོ་ལ་ཞུགས་པའི་ཚེ། དེའི་བར་དུ་གཅོད་པའི་སྒྲ་ཅ་ཅོ་རྣམས་འདོན་ཀྱང་། དེ་དག་བསམ་གཏན་དེ་ལ་བར་དུ་གཅོད་ཅིང་སྒྲིབ་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2819]
དེ་ལྟར་མི་མཐུན་པའི་ཕྱོགས་དག༌[^2453]ཡོད་ཀྱང་། དེ་དག་གིས་མི་ཚུགས་པའི༌[^2454]མཐུ་དང་ལྡན་པའི་ཕྱིར་སྟོབས་ཞེས༌[^2455]བྱའོ། །

[Block 2820]
དེ་དགེ་བ་རྟོག་པ༌[^2456]དང་དཔྱོད་པར་སྤྱོད་ཀྱང་དེའི་བསམ་གཏན་གཉིས་པ་ལ་སྒྲིབ་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ལ། རྟོག་པ༌[^2457]དང་དཔྱོད་པ་གཉིས་ནི་བསམ་གཏན་གཉིས་པའི་མི་མཐུན་པའི་ཕྱོགས་ཏེ། དེ་བས་ན་བསམ་གཏན་གཉིས་པ་ལ་རྟོག་པ༌[^2458]དང་དཔྱོད་པ་གཉིས་སྤངས་ཏེ་མེད་པར་བྱེད་དོ། །

[Block 2821]
བྱང་ཆུབ་སེམས་དཔའི་ཏིང་ངེ་འཛིན་གྱི་སྟོབས་དང་ལྡན་པ་ནི་བསམ་གཏན་གཉིས་པ་ལ་ཡང་དག་པར་ཞུགས་ལ། རྟོག༌[^2459]དཔྱོད་གཉིས་སྤྱོད་ཀྱང་དེ་དེ་ལ་སྒྲིབ་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2822]
དེ་དག༌[^2460]དགའ་བ་དང་མགུ་བ་ཡང་སྐྱེས་པ་ཡིན་ལ། དེའི་བསམ་གཏན་གསུམ་པ་ལ་སྒྲིབ་པར་ཡང་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ལ། དགའ་བ་དང་མགུ་བ་ལ་ཆགས་པ་ནི་བསམ་གཏན་གསུམ་པའི་སྒྲིབ་པ་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་ཏིང་ངེ་འཛིན་གྱི་མཐུ་དང་ལྡན་པས་བསམ་གཏན་གསུམ་པ་ལ་ཡང་དག་པར་ཞུགས་ལ། ཆོས་ལ་དགའ་ཞིང་མགུ་བ་ལ་ཡང་སྤྱོད་མོད་ཀྱི། དགའ་ཞིང་མགུ་བ་དེ་བསམ་གཏན་དེ་ལ་སྒྲིབ་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2823]
དེ་སེམས་ཅན་ཐམས་ཅད་སྨིན་པར་བྱ་བ་དང་། དམ་པའི་ཆོས་ཡོངས་སུ་གཟུང་བའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། བཏང་སྙོམས་སུ་མི༌[^2461]འཇོག་པར་དཔྱོད་པ༌[^2462]དང་བྱ་བ་ལ༌[^2463]ཞུགས་པ་ནི་བསམ་གཏན་བཞི་པའི་སྒྲིབ་པ་སྟེ། བྱང་ཆུབ་སེམས་དཔའི་ཏིང་ངེ་འཛིན་གྱི་མཐུ་དང་ལྡན་པས༌[^2464]བསམ་གཏན་བཞི་པ་ལ་ཡང་ཞུགས༌[^2465]ལ། སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱ་བ་དང་། དམ་པའི་ཆོས་གཟུང་བ་ལ་སོགས་པ་སྤྱོད་པ་རྣམ་པ༌[^2466]སྣ་ཚོགས་བྱེད་ཀྱང་དེ་དེ་ལ་སྒྲིབ་པར༌[^2467]མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2824]
དེ་བསམ་གཏན་བཞི་པོ་དེ་དག་གི་གནས་ཏེ། བསམ་གཏན་དང་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་ཆོས་རྣམས་ཀྱིས་ཀྱང་ཐུལ་བར་མི་ནུས་སོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེ་ཏིང་ངེ་འཛིན་གྱི༌[^2468]སྟོབས་དང་ལྡན༌[^2469]པས་བསམ་གཏན་དང་པོ་ལ་སོགས་པ་བཞི་པོ་རྣམས་ཀྱི༌[^2470]གནས་ལ། བསམ་གཏན་དེ་དག་གི་མི་མཐུན་པའི་ཕྱོགས་སྒྲ་ཅ་ཅོ་དང་། རྟོག་དཔྱོད་དང་། དགའ་ཞིང་མགུ་བ་དང་། བཏང༌[^2471]སྙོམས་མ་ཡིན་པ་རྣམས་ཀྱིས་ཀྱང་བར་དུ་གཅོད་པར་མི་ནུས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2825]
དེ་ལ་མཉམ་པར་གཞག་པའི༌[^2472]གནས་ཀྱང་མི་གཏོང་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི། བསམ་གཏན་དང་པོ་ལ་སོགས་པའི་མཉམ་པར་བཞག་པ༌[^2473]རྣམས་ལ་རྒྱུན་དུ་སྤྱོད་ཀྱང་བསམ་གཏན་དེ་དག་གི་དབང་དུ་གྱུར་ནས། གཟུགས་ཀྱི་ཁམས་འབའ་ཞིག་ཏུ་ཡང་མི་སྐྱེ་སྟེ་སྨོན་ལམ་གྱི་དབང་གིས། སེམས་ཅན་གྱི་དོན་དུ་ས་འོག་མ་རྣམས་སུ་ཡང་བསམས་བཞིན༌[^2474]ནི་སྐྱེའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2826 [HEADING]]
#### ཤེས་རབ་མི་ཚུགས་པ། ^8-5-5-0

[Block 2827]
ཤེས་རབ་མི་ཚུགས་པ་ནི་གང་ཤེས་རབ་ཀྱི་སྟོབས་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཤེས་རབ་ཀྱི་སྟོབས་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2828]
འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་ལ་མི་མཐུན་པར་ཤེས་པ་ཞེས་བྱ་བ་ལ། འཇིག་རྟེན་པའི་ཆོས་ནི་རིག་པའི་གནས་བཞིའོ། །

[Block 2829]
བཟོ་དང་། གསོ༌[^2475]བ་དང་། གཏན་ཚིགས་དང་། སྒྲ་རིག་པ་རྣམས་སོ། །

[Block 2830]
འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་ནི་ནང་རིག་པ་སྟེ། གསུང་རབ༌[^2476]ཡན་ལག་བཅུ་གཉིས་སོ། །

[Block 2831]
མི་ཐུལ་བར་ཤེས་རབ་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་རྣམས་ཀྱིས་སྒྲིབ་ཅིང་བར་དུ་གཅོད་མི་ནུས་པར་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་རྣམས་ཤེས་པའོ། །

[Block 2832]
ཆོས་དེ་རྣམས་ལ་མི་ཐུལ་བར་ཤེས་པ་རྒྱས་པར་བསྟན་པའི་ཕྱིར། ཚེ་རབས་ཚེ་རབས་སུ་ཡང༌[^2477]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་ལ་མངོན་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་ཡན་ཆད་ནི་འཇིག་རྟེན་པའི་ཆོས་ལ་མི་ཐུལ་བར་ཤེས་པ་བསྟན་ཏོ། །

[Block 2833]
གང་ཡང་འཇིག་རྟེན་ལས་འདས་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། རྗེས་སུ་རྟོགས་ཏེ་ཞེས་བྱ་བ་ཡན་ཆད་ནི་འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་ལ་མི་ཐུལ་བར་ཤེས་པ༌[^2478]བསྟན་ཏོ། །

[Block 2834 [HEADING]]
##### འཇིག་རྟེན་པའི་ཆོས་ལ་མི་ཐུལ་བར་ཤེས་པ། ^8-5-5-1-0

[Block 2835]
ཚེ་རབས་ཚེ་རབས་སུ༌[^2479]ཞེས་བྱ་བ་ནི་ལྷ་དང་མིའི་གནས་དེ་དག་ཏུ་བདག་གི་ཕུང་པོ་སྐྱེས་ཤིང་ཚེ་བླངས་པའོ། །

[Block 2836 [VERSE]]
དེ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེའོ། །
བཟོའི་ལས་ནི་དྲ་བ་བཙེམ༌[^2480]པ་ལ་སོགས་ཏེ།
[^2481] བཟོ་རིག་པ་རང་གི་མིང་གིས་བསྟན་ཏོ། །

[Block 2837]
རིག་པ་ཞེས་སྨོས་པ་ནི་རིག་པའི་གནས་ལྷག་མ་གསུམ་བསྟན་ཏོ། །

[Block 2838]
སྔགས་ནི་གཞན་གྱི་དམག་གི་སྡེ་མནན་པ་དང་། སྦྲུལ་ལ་སོགས་པའི་དུག་མེད་པར་བྱ་བའི་ཐབས་སོ། །

[Block 2839]
སྟོབས་ནི་མཚོན་ཆ་འཕང་བ༌[^2482]དང་། གླང་པོ་ཆེ་འདེགས་པ་ལ་སོགས་པའི་རྩལ་ལོ། །

[Block 2840]
མངོན་དུ་འགྱུར་བ་ནི་ཤེས་པར་གྱུར་པའོ། །
--- END BLOCKS ---
