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
[Block 2871]
དེ་ཉིད་ཀྱི་དོན་གང་ཡིན་པ་བསྟན་པའི་ཕྱིར་གང་དང་གང་། ཇི་ལྟ་ཇི་ལྟ་བུར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཆོས་གང་དང་གང་། གང་གི་ཆ་དང་ཕྱོགས་སུ་གཏོགས་པ་ཇི་ལྟ་ཇི་ལྟ་བུར་དེའི་ཟླ་དང་ཕྱོགས་སུ་བསླན་ཞིང་། དབྱེ་བར་བྱ་བའི་ཆོས་དེ༌[^2523]དང་དེ་དག་ལ་འདི་ནི་འདིའི༌[^2524]ཕྱོགས་སུ་གཏོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་། [^2525]གང་དང་གང་གི་ཟླ་ལ་གཏོགས་པ་ཤེས་ཤིང་། ཆ་ཆར་སོ་སོར་རྣམ་པར་འབྱེད་པ་ཤེས་པའོ། །

[Block 2872]
བརྡ་དང་རྣམ་པར་ངེས་པ་ནི་ཐ་སྙད་དང་གཏན་ལ་ཕབ་པའི་དོན་ལ་བྱ་སྟེ། ངེས་པའི་དོན་ནས་རྣམ་པར་ངེས་པའི་བར་གྱི་ཆོས་གང་དང་གང་གསུངས་པ་དེ་དག་ཀྱང་དེ་དག་སོ་སོའི་སྡེ་ཚན་དུ་གཏོགས་པར་ཤེས་པའོ།[^2526] །

[Block 2873 [HEADING]]
#### བརྩོན་འགྲུས་ཤིན་ཏུ་འབྲེལ་པ། ^8-6-3-0

[Block 2874]
བརྩོན་འགྲུས་ཤིན་ཏུ་འབྲེལ་པ་ནི་བརྩོན་འགྲུས་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ལ་རབ་ཏུ་ཞུགས་ཏེ། དེ་བསྟན་པའི་དབང་དུ་བྱས་ནས། དེ་ལ་བརྩོན་འགྲུས་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་གང་ཞེ་ན༌[^2527]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2875]
འདི་ཞེས་བྱ་བའི་ཚིག་གོང་དུ་བསྟན་པ་ཆོས་རྣམ་པར་འབྱེད་པ་ལ་སོགས་པ་སྙེགས༌[^2528]སོ། །

[Block 2876]
རབ་ཏུ་འཛིན་པ་ནི་ཆོས་དེ་དག་སེམས་ལ་མི་བརྗེད་པར་འཛིན་པ་སྟེ། [^2529]ཕྱིར་ཞེས་བྱ་བའི་སྒྲ་ཐམས་ཅད་དང་སྦྱར་རོ། །

[Block 2877]
སྤྲོ་བ་ནི་ཆོས་དེ་དག་སྒྲུབ་པར༌[^2530]འདོད་པའོ། །

[Block 2878]
སྟོབས་ནི་ལེ་ལོའི་དབང་དུ་མི་འགྱུར་བའོ། །

[Block 2879]
བརྟུལ་བ༌[^2531]ནི་ཉོན་མོངས་པ་གཞན་གྱིས་མི་ཚུགས་པའོ། །

[Block 2880]
ཕྱིར་མི་ལྡོག་པ་ནི་དགེ་བ་བསྒྲུབ་པ་མི་འདོར་བའོ། །

[Block 2881]
འདུན་པ་ནི་ཆོས་དེ་དག་ལ་དེ་བཞིན་དུ་ཡིད་ཆེས་ནས་བྱེད་པའོ། །

[Block 2882]
མཐུ་ནི་བདུད་ལ་སོགས་པས་མི་ཟློགས་པའོ། །

[Block 2883]
བརྩོན་འགྲུས་མི་གཏོང་བ་ནི་བསྒོམ་པ་རྒྱུན་དུ་བྱ་བ་མི་གཏོང་བའོ། །

[Block 2884]
ལམ་མངོན་པར་རྟོགས་པར་བྱ་བ་ནི་འཕགས་པའི་ལམ་གྱི་ཡན་ལག་བརྒྱད་དང་། ས་བཅུའི་ལམ་རྟོགས་པར་བྱ་བའོ།[^2532] །ཕྱིར་ནི་དེ་དག་གི་དོན་དུའམ། ཆེད༌[^2533]དུའོ། །

[Block 2885]
བརྩོན་པ་འདི་ནི་ཞེས་བྱ་བ་ནི་འབད་པ་འདི་ནི་ཞེས་བྱ་བའི༌[^2534]ཐ་ཚིག་གོ། །

[Block 2886 [HEADING]]
#### དགའ་བ་ཤིན་ཏུ་འབྲེལ་པ། ^8-6-4-0

[Block 2887]
དགའ་བ་ཤིན་ཏུ་འབྲེལ་པ་ནི་དགའ་བ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་དགའ་བ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་གང་ཞེ་ན༌[^2535]ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2888]
དེ་ཡང་དགའ་བ་ཇི་ལྟ་བུ་གང་གིས༌[^2536]གང་བསྒྲུབས་ཤིང་། དེའི༌[^2537]མཐུན་པ་སྤངས་པ་ནི་དགའ་བ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཅེས་བྱའོ། །

[Block 2889 [HEADING]]
##### དུས་གསུམ་གྱི་ཆོས་ཐོབ་པར་དགའ་བ། ^8-6-4-1-0

[Block 2890]
དེ་ལ་དགའ་བ་ཇི་ལྟ་བུས་ནི། དུས་གསུམ་གྱི་ཆོས་ཐོབ་པར་དགའ་བའི་དགའ་བ་སྟེ། ཆོས་ལ་རབ་ཏུ་དགའ༌[^2538]ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིག་གསུམ་གྱིས་བསྟན་ཏོ། །

[Block 2891]
དེ་ལ་འདས་པའི་ཆོས་རྣམས་ལ་དམིགས་ནས། སེམས་ལ་མོས་པ་སྐྱེས་པ་ནི་ཆོས་ལ་དགའ་བའོ། །

[Block 2892]
མ་འོངས་པའི་ཆོས་ལ་དམིགས་ནས། སེམས་ལ་མོས་པ་སྐྱེས་པ༌[^2539]ནི་ཆོས་ལ་མོས་པའོ། །

[Block 2893]
ད་ལྟར་གྱི་ཆོས་ལ་དམིགས་ནས། སེམས་ལ་མོས་པ་སྐྱེས་པ་ནི་ཆོས་ལ་མཆོག་ཏུ་དགའ་བའོ། །

[Block 2894]
དགའ་བ་གང་ཡིན་པ་དེ་ཉིད་ཀྱིས་རྒྱུ་བྱས་ནས་སེམས་ཞུམ་པ་དང་སྤྲོས་པར་གྱུར་པ་སྟེ། སེམས་མ་གོང་བ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིག་གཉིས་ཀྱིས་བསྟན༌[^2540]ཏོ། །

[Block 2895]
སེམས་མ་གོང་བ་ནི་མི་ནུས་སོ་སྙམ་དུ་སེམས་ཞུམ་ཞིང་དགའ་བ་སྲོ་ཤི་བར་མ་གྱུར་པའོ། །

[Block 2896]
དད་ཅིང་འདུན་པ་ནི་དགའ་བ་ཁྱད་པར་དུ་འཕགས་པ༌[^2541]སྐྱེས་ཤིང་ལྷག་པར་འཇུག་པར་སེམས་མོས་པའོ། །

[Block 2897 [HEADING]]
##### ལུས་དང་སེམས་ལས་སུ་རུང་བ་བསྒྲུབས་པ། ^8-6-4-2-0

[Block 2898]
གང་བསྒྲུབ་པ་ནི་དགའ་བ་དེས་ལུས་དང་སེམས་ལས་སུ་རུང་བ་བསྒྲུབས་པ་སྟེ། དེ་ཡང་ལུས་དང་སེམས་ཤིན་ཏུ་སྦྱངས་པར་འགྱུར་བ་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 2899]
ལུས་ལས་སུ་རུང་བ་ནི་གཟུགས་ཀྱི་ཕུང་པོ་རྟེན་དུ་གྱུར་པས་ཉོན་མོངས་པ་སྐྱེ་བའི་རྒྱུ་མི་བྱེད་ཅིང་། ཉོན་མོངས་པ་སྐྱེ་བ་དང་རྗེས་སུ་མི་མཐུན་པར་གནས་པའོ། །

[Block 2900]
སེམས་ལས་སུ་རུང་བ་ནི་ཞུམ་པ་དང་། རྒོད་པའི་དབང་དུ༌[^2542]མ་གྱུར་ལ། ཞི་གནས་དང་ལྷག་མཐོང་ཟུང་དུ་འབྲེལ་པས་དོན་རྟོགས་ཤིང་རྩེ་གཅིག་ཏུ་གནས་པར་ནུས་པའོ། །

[Block 2901 [HEADING]]
##### མི་མཐུན་པའི་ཕྱོགས་སྤོང་བ། ^8-6-4-3-0

[Block 2902]
དེ་མི་མཐུན་པའི་ཕྱོགས་སྤོང་བ༌[^2543]ནི་དགའ་བའི་མི་མཐུན་པའི་ཕྱོགས་སམ། མཐོང་བའི༌[^2544]ལམ་ལ་བར་དུ་གཅོད་པའི་མི༌[^2545]མཐུན་པའི་ཕྱོགས་སྤོང་བ་སྟེ། དེ༌[^2546]ཡང་ཉོན་མོངས་པ་རྣམས་སེལ་བ་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 2903 [HEADING]]
#### ཤིན་ཏུ་སྦྱངས་པའི་ཤིན་ཏུ་འབྲེལ་པ། ^8-6-5-0

[Block 2904]
ཤིན་ཏུ་སྦྱངས་པའི་ཤིན་ཏུ་འབྲེལ་པ་ནི། གང་ཤིན་ཏུ་སྦྱངས་པ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཤིན་ཏུ་སྦྱངས་པ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2905]
དེ་ཡང་གང་གིས་གང་སྤངས་ནས། དམིགས་པའི་ཡུལ་ལ་རྩེ་གཅིག་ཏུ་གནས་པར་ནུས་པ་ནི་ཤིན་ཏུ་སྦྱངས་པ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཅེས་བྱའོ། །གང་གིས་སྤངས་ཤེ་ན། གང་ལུས་ཤིན་ཏུ་སྦྱངས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། གོང་དུ་བཤད་པའི་ལུས་དང་སེམས་ལས་སུ་རུང་བས་སྤངས་སོ། །

[Block 2906]
གང་སྤངས་པ་ནི་ཉོན་མོངས་པ་ལ་སོགས་པ༌[^2547]སྤངས་སོ། །

[Block 2907]
དམིགས་པའི་ཡུལ་ལ་རྩེ་གཅིག་ཏུ་གནས་པར་ནུས་པ་ནི། ཞི་གནས་ལ་འཇུག་པའི་དམིགས་པ་ལ་སེམས་རྩེ་གཅིག་ཏུ་འཇུག་པར་ནུས་པའོ། །

[Block 2908]
ཞི་གནས་ཀྱི༌[^2548]དམིགས་པའི་དམིགས་པ་ནི། ཞི་གནས་ལ་དམིགས་པའི་དམིགས་པ་ཞེས་བྱའོ། །

[Block 2909 [HEADING]]
#### ཏིང་ངེ་འཛིན་ཤིན་ཏུ་འབྲེལ་པ། ^8-6-6-0

[Block 2910]
ཏིང་ངེ་འཛིན་ཤིན་ཏུ་འབྲེལ་པ་ནི། གང་ཏིང་ངེ་འཛིན་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ལ༌[^2549]རབ་ཏུ་ཞུགས་པ་སྟེ། དེའི་དབང་དུ་བྱས་ནས། དེ་ལ་ཏིང་ངེ་འཛིན་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །
--- END BLOCKS ---
