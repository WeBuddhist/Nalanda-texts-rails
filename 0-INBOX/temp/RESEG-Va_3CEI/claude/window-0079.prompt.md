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
[Block 2766]
བརྒྱད་པ་ཡན་ཆད་ནི་ཆེར་བངས་པའོ། །

[Block 2767]
དེ་ཡང་ས་དང་པོ་མན་ཆད་ནི་གཅིག་ཏུ་ཟག་པ་དང་བཅས་པའི་བསྒྲུབ་པའོ། །

[Block 2768]
ས་བདུན་པ་མན་ཆད་ནི་ཟག་པ༌[^2359]མེད་པ་གཉིས་ཀའི་བསྒྲུབ༌[^2360]པའོ། །

[Block 2769]
ས་བརྒྱད་པ་ཡན་ཆད་ནི་གཅིག་ཏུ་ཟག་པ༌[^2361]མེད་པའི་བསྒྲུབ་པའོ། །

[Block 2770]
ཡང་ན་ས་དང་པོ་མན་ཆད་ནི་ཆུང་ངུ་བངས་པ། ས་དང་པོ་ཡན་ཆད་ནི་མི་ལྡོག་པའི་ས་སྟེ་ཆེར་བངས་པའོ། །

[Block 2771]
མདོ་ལས་དེ་བཞིན་དུ་མེ་ཏོག་དང་ཞེས་པ་ནས་མིང་ཐོབ་བོ་ཞེས་པའི་བར་དུ་ནི་ལུང་དང་འབྲས་བུ་སོ་སོར་བསྟན་པ་སྟེ། བསྟན་པ་གཅིག་ལས་འབྲས་བུ་མི་མཐུན་པར་གྲུབ༌[^2362]ཅེས་པའི་དོན་ཏོ། །

[Block 2772]
ཆར་པ་གཅིག་གིས་བརླན་པ་ལས་མེ་ཏོག་དང་འབྲས་བུ་སོ་སོར་སྐྱེ་བ་བཞིན་ཏེ།

[Block 2773]
དང་པོ་ཐོས་པ་དང་བསམས་པའི༌[^2363]ཤེས་རབ་ནི་མེ་ཏོག་ལྟ་བུར་བལྟའོ།[^2364] །བསྒྲུབ་ན་འབྲས་བུ་ཐོབ་པའི་དཔེ་འདི་ནི་འབྲས་བུའི་དཔེའོ། །

[Block 2774]
ཆར་པ་རོ་གཅིག་གིས་ཞེས་པ་ནི་གསུང་རབ་གཅིག་གིས་ཞེས་པའི་དོན་ཏོ། །

[Block 2775]
ལྷག་པའི་ཚུལ་ཁྲིམས་དང་། ཤེས་རབ་དང་། ཏིང་ངེ་འཛིན་ཀྱང་སོ་སོའི་དབང་པོའི༌[^2365]ལས་ས༌[^2366]ཐེག་པ་ཆེ་ཆུང་གིས༌[^2367]སོ་སོར་མཐོང་བའང་དེ་དང་འདྲའོ། །

[Block 2776 [HEADING]]
###### **བརླན་པར་མི་སེམས་པའི་དཔེ།** ^4-5-4-2-2-4-0

[Block 2777]
མདོ་ལས་ས་གཅིག་ལ་གནས་པའི་སྨན་མང་པོ་དང་ཞེས་པ་ནས་བངས་པ་དེ་བཞིན་དུ་ཞེས་པའི་བར་དུ་ནི་སོ་སོ་ནས་དེ་ལྟར་བྱས་པར་མི་སེམས་པའི༌[^2368]དཔེ་སྟེ། ཐེག་པ་རྣམ་གསུམ་གྱི་རིགས་ཀྱང་ཡང་དག་པའི་གཞུང་གཅིག་ལ་བརྟེན་པ་ནི། ས་གཅིག་ལ་གནས་པ་དང་འདྲ། དེ་བཞིན་གཤེགས་པ༌[^2369]གཅིག་གིས་བསྟན་པ་ལས་གོ་བ་ནི་ཆར་པའི་རོ་གཅིག་གིས༌[^2370]བངས་པ་བཞིན་ཏེ། འབྲས་བུ་སོ་སོར་སྨིན་པ་དང་། ཤིང་རྩི་སྣ་ཚོགས་སུ་འགྱུར་བ་ཡང་མི་སེམས་མི་ཤེས་སོ། །

[Block 2778 [HEADING]]
##### དཔེ་དོན་དུ་སྦྱར་བ། ^4-5-4-3-0

[Block 2779 [HEADING]]
###### དོན་བསྟན་པ། ^4-5-4-3-1-0

[Block 2780]
མདོ་ལས་འོད་སྲུངས་དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནས་གསུང་གཅིག་གིས་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་ཁེབས་པ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་དུ་དཔེ་དོན་དུ་སྦྱར་བ་སྟེ། མདོ་ལས་འབྱུང་བ་བཞིན་དུ་གོ་བར་གྱིས༌[^2371]ཤིག །མདོ་ལས་འོད་སྲུངས་དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནས་ཡང་དག་པར་རྫོགས་པའི༌[^2372]སངས་རྒྱས་ཞེས་པའི་བར་དུ་ནི་འབྲས་བུ་བརླན་པ༌[^2373]མི་མཐུན་པའི་དཔེ་སྟེ། སྔར་ནི་དོན་བསྟན། ཕྱིས་ནི་མི་མཐུན་པའི་དཔེ་དང་སྦྱར་བའོ། །

[Block 2781 [HEADING]]
###### **ཡོན་ཏན་གྱི་མཚན་ལས་གླེང་པ།** ^4-5-4-3-1-1-0

[Block 2782]
དང་པོའང་དེ་བཞིན་གཤེགས་པ་ཉིད་ལས་གླེང་པ་སྟེ། དོན་རྣམ་པ་གསུམ་མོ། །

[Block 2783]
ཡོན་ཏན་གྱི་མཚན་ལས་གླེང་པ་དང་། དོན་མཛད་པ་ལས་གླེང་པ་དང་། མཁྱེན་གཟིགས་པ་ལས་གླེང་པ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 2784 [HEADING]]
###### **དོན་མཛད་པ་ལས་གླེང་པ།** ^4-5-4-3-1-2-0

[Block 2785]
མདོ་ལས་མ་རྒལ་བ་བསྒྲལ་ལོ་ཞེས་པ་ནས་མྱ་ངན་ལས་བཟླའོ་ཞེས་པའི་བར་དུ་ནི་དོན་མཛད་པ་ལས་གླེང་པ་སྟེ། སྨོན་པ་བཞི་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའོ། །

[Block 2786]
སྡུག་བསྔལ་ལས་བསྒྲལ་བ་དང་། སྡིག་པ་མི་དགེ་བའི་ལས་ལས་དགྲོལ་བ་དང་། བདེ་བ་མ་ཐོབ་པ་རྣམས་བདེ་བ་ལ་བཞག་པ་དང་། མྱ་ངན་ལས་འདས་པ་མ་ཐོབ་པ་ཐོབ་པར་བྱ་བ་སྟེ། སྡུག་བསྔལ་ཤེས་པ་དང་། ཀུན་འབྱུང༌[^2374]སྤངས་པ་དང་། ལམ་བསྒོམ་པ༌[^2375]དང་། འགོག་པ་མངོན་དུ་བྱ་བ་སྟེ། རིམ་པ་བཞིན་ནོ།[^2376] །

[Block 2787 [HEADING]]
###### **མཁྱེན་གཟིགས་པ་ལས་གླེང་པ།** ^4-5-4-3-1-3-0

[Block 2788]
མདོ་ལས་ང་ནི་ད་ལྟར་གྱི་འཇིག་རྟེན་འདི་དང་ཞེས༌[^2377]པ་ནས་ལམ་བསྒོམ་པ་ལ༌[^2378]མཁས་པའོ་ཞེས་པའི་བར་དུ་ནི་ཐམས་ཅད་མཁྱེན་པ་དང་། ཐམས་ཅད་གཟིགས་པ་སྟོན་ཏེ། དེ་ཡང་རིག་པ་གསུམ་དང་། ཡེ་ཤེས་གཉིས་དང་། ཆོས་ཤེས་པ་དག༌[^2379]གསུམ་སྟོན་ཏོ། །

[Block 2789]
རིག་པ་གསུམ་ནི་དུས་གསུམ་རིག་པའོ། །

[Block 2790]
ཡེ་ཤེས་གཉིས་ནི་དོན་དམ་པའི་ཡེ་ཤེས་དང་། ཀུན་རྫོབ་ཀྱི་ཡེ་ཤེས་སོ། །

[Block 2791]
ཡུལ་རབ་ཏུ་ཤེས་པ་སྤྱོད་པ་རབ་ཏུ་འཆད༌[^2380]པ། འབྲས་བུ་རབ་ཏུ་རིག་པའོ། །ཤེས་པ་ནི་ཡང་དག་པ་དང་། ཡང་དག་པ་མ་ཡིན་པ་ཤེས་པ། འཆད་པ་ནི་དགེ་བ་དང་མི་དགེ་བ་འཆད་པ། མཁས་པ་ནི་བསྒོམ་པ་དང་བསྒྲུབ་པ་ལ་མཁས་པའོ། །

[Block 2792]
ཡང་ན་ཐེག་པ་རྣམ་གསུམ་རིམ༌[^2381]བཞིན་དུ་སྦྱར་རོ། །

[Block 2793]
མདོ་ལས་དེ་ལྟར་འོད་སྲུངས་སྲོག་ཆགས་མང་པོ་ཞེས་པ་ནས་མཐུ་ཇི་ལྟ་བ་བཞིན་དུ་འཇུག་གོ་ཞེས་པའི་བར་དུ། དབང་པོ་དང་ཞེས་པ་ནི་དབང་པོ་རྣོན་པོའི་ཆེད་དུ་ཐེག་པ་ཆེན་པོ་བསྟན། དབང་པོ་རྟུལ་པོ་ལ་ནི་ཐེག་པ་རྣམ་གཉིས་བསྟན། དབང་པོ་རྣོན་པོའི་ཆེད་དུ་སྡོང་བུའི་སྨན་ཆེན་པོ་བསྟན། དབང་པོ་རྟུལ་པོ་ལ་ནི་སྨན་ཆུང་ངུ་བསྟན། བརྩོན་འགྲུས་ཅན་ལ་ནི་སྒྲུབ་པའི་སྤྱོད་པ་བསྟན། ལེ་ལོ་ཅན་ལ༌[^2382]ནི་སངས་རྒྱས་རྗེས་སུ་དྲན་པ་སྟོན་ཏོ། །

[Block 2794]
སེམས་ཅན་རྣམས་ཚེ་འདི་ལ་བདེ་བར་གྱུར་ཅིང་མཐར་གྱིས་ཐམས་ཅད་མཁྱེན་པའི་ཆོས་ལ་སྟོབས་དང་མཐུ་ཇི་ལྟ་བ་བཞིན་དུ་འཇུག༌[^2383]གོ་ཞེས་པ་ནི་སེམས་ཅན་རྣམས་ཆོས་ཐོས་པ་ཙམ་གྱིས་བདེ་བ་ཐོབ་སྟེ། དེ་ཡང་འཇིག་རྟེན་གྱི་བདེ་བ་དང་། འཇིག་རྟེན་ལས་འདས་པའི་བདེ་བའོ། །

[Block 2795]
འཇིག་རྟེན་གྱི་བདེ་བ་ནི་ཚེ་འདི་ལ་སྤྱོད་པ་ཡིད་དུ་འོང་བ་དང་ལྡན་ཞིང་དགེ་བའི་སྤྱོད་པ་བསྒྲུབས་པས་བདེ་བའི་འབྲས་བུ་ཐོབ་པའོ། །

[Block 2796]
འཇིག་རྟེན་ལས་འདས་པའི་བདེ་བ་ནི་སྒྲིབ་པ་བྱང་བས་ཆོས་ཉིད་ལ་ཞུགས་ཏེ། བྱང་ཆུབ་སེམས་དཔའི་ལམ་མོ། །

[Block 2797]
དེ་ཡང་ལྷག་པའི་མོས་པས་བསྐྱེད་པའི༌[^2384]ལམ་དང་། ངེས་པའི་ལམ་སྟེ་སྒྲིབ་པ་རྣམ་པ༌[^2385]གཉིས་སྤངས་པ་ལ་རིམ༌[^2386]པ་བཞིན་དུ་འཇུག་གོ། །

[Block 2798 [HEADING]]
###### མི་མཐུན་པའི་དཔེ་དང་སྦྱར་བ། ^4-5-4-3-2-0

[Block 2799]
མདོ་ལས་འདི་ལྟ་སྟེ། འོད་སྲུངས་དཔེར་ན་ཞེས་པ་ནས་བདག་བདག་གི་རིགས་དང་ཚད་དུ་སྐྱེའོ་ཞེས་པའི་བར་དུ་ནི་དཔེ་དང་དོན་དུ་སྦྱར་ཏེ། འབྲས་བུ་མི་མཐུན་པར་གྱུར་པའོ། །

[Block 2800]
མདོ་ལས་འོད་སྲུངས་དེ་བཞིན༌[^2387]གཤེགས་པ་ཞེས་པ་ནས་བདག་གིས༌[^2388]བདག་ཤེས་པའམ་རིག་པའམ། རྟོགས་པ་མེད་དོ་ཞེས་པའི་བར་དུ་ནི་དཔེ་ཕྱི་མ་དང་དོན་དུ་སྦྱར་བ་སྟེ། རོ་གཅིག་ཅེས་པ་ནི་མཚན་མ་མེད་པར་རོ་གཅིག་པ། མཚན་མ་མེད་པའི་རོ་དང་། ཟག་པ་མེད་པའི་རོ་དང་། རྣམ་པར་གྲོལ་བའི་རོ་གཅིག་པའོ། །

[Block 2801]
དེ་ལྟར་རོ་གཅིག་གིས་སོ་སོར་སྨིན་པ་དང་། ཤིང་དང་འབྲས་བུ་སོ་སོར་བརླན་པ་ཡང༌[^2389]བདག༌[^2390]སོ་སོ་ནས་སེམས་པ༌[^2391]མེད་དོ། །

[Block 2802]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེ་ན། འོད་སྲུངས་ཞེས་པ་ནས་ཇི་ལྟ་བ་བཞིན་དུ་གཟིགས་སོ་ཞེས་པའི་བར་དུ་ནི་དེ་ལའང་སེམས་ཅན་གྱི་སྤྱོད་པ་སྤྱིར་མཁྱེན་པ་དང་། སོ་སོར་མཁྱེན་པ་དང་། མཁྱེན་པ་དེ་གཉིས་བསྡུ་བའོ། །

[Block 2803]
སེམས་ཅན་དེ་དག་ཅི་ལྟ་བ་བཞིན་དུ་མཁྱེན་པ་ནི་འདུས་བྱས་སམ། འདུས་མ་བྱས་ཀྱི་ཚུལ་དུའམ། སྤྱོད་པའམ། སེམས་ཀྱི་སྒོ་ནས་ཇི་ལྟ་བ་བཞིན་དུ་མཁྱེན་པའོ། །

[Block 2804]
ཅི་ལ་སེམས་ཞེས་པ་དག་ནི་མཁྱེན་པ་སོ་སོར་སྨོས་པ་སྟེ། ཤེས་རབ་རྣམ་གསུམ་གྱི་སྒོ་ནས་རང་བཞིན་མཁྱེན་པ་དང་། སྤྱོད་པ་དང་། དངོས་པོ་མཁྱེན་པ་དང་། སྤྱོད་པ་གང་གིས་འབྲས་བུ་ཅི་འཐོབ་པ༌[^2392]དང་། ལུང་གང་གིས་འབྲས་བུ༌[^2393]ཅི་སྒྲུབ་པ་སྟེ། ཆོས་དེ་བཞིའི་རིམ་པ་བཅོམ་ལྡན་འདས་ཀྱིས་མཁྱེན་ཞེས་པའོ། །

[Block 2805]
མངོན་སུམ་དུ་གཟིགས་པ་དང་། ཇི་ལྟ་བ་བཞིན་དུ་གཟིགས་པ་ནི་མཁྱེན་པ་དེ་དག་བསྡུ་བ་སྟེ། སེམས་ཅན་གྱི་གཞི་དང་། སེམས་ཀྱི༌[^2394]སྤྱོད་པ་མཚན་མ་དང་། དངོས་པོ་དང་། རང་བཞིན་མ་ལུས་པར་གཟིགས་པའི་ཕྱིར་གཟིགས་པའོ། །
--- END BLOCKS ---
