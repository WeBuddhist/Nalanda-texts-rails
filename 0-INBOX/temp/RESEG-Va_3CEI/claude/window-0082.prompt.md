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
མདོ་ལས།

[Block 2872]
བདེ་བར་གཤེགས་པའི་སྲས་པོ་གང་བཞུགས༌[^2451]པ། །ཞེས་པ་ནས། དེ་ལྟ་བུ་ཡི་དཔེ་དག་བསྟན་པ་ཡིས། །ཞེས་པའི་བར་དུ་ནི་རིགས་ཅན་གྱི་ས་ནས་ཐེག་པ་ཆེན་པོའི་འབྲས་བུ་ཐོབ་པ་དང་། མྱ་ངན་ལས་འདས་པའི་བར་དུ་འབྲས་བུ་ཆེ་ཆུང་ཐོབ་པ་དང་། གྲུབ་པའི་དཔེ་བསྟན་པ་ཡིན་ནོ། །

[Block 2873]
མདོ་ལས།

[Block 2874]
དེ་བཞིན་གཤེགས་པའི་ཐབས་རྣམས་ཤེས་པར་གྱིས།[^2452] །ཞེས་པ་ནས། ཕྱོགས་བཅུ་ཀུན་ན་ཇི་ལྟར་མཛེས་པ་བཞིན། །ཞེས་པའི་བར་དུ༌[^2453]ནི་འབྲས་བུ་སོ་སོར་སྨིན་ཅིང་ཐོབ་པ་ཁྱད་པར་དུ་གྱུར་པ་དང་དཔེ༌[^2454]དོན་དུ་སྦྱར་ཏེ་རྒྱས་པར་བསྟན་པའོ། །

[Block 2875]
མདོ་ལས།

[Block 2876]
འདི་ན་རྟག་ཏུ་འཇིག་རྟེན་ཕན་པའི་ཆོས། །ཞེས་པ་ནས། ངོམས་པར་བྱེད་ཅེས་པའི་བར་དུ་ནི་ལྷ་དང་མི་རྣམས་ལ་ཕན་པའི་དོན་བྱས་པའོ། །

[Block 2877]
མདོ་ལས་འཇིག་རྟེན་ཐམས་ཅད་ངོམས་པར་བྱས་ནས་ནི་ཞེས་པ་ནས་སྡོང་པོ་ཆེན་པོ་ཞེས་པ༌[^2455]ནི་དེ་དག་བྱ་ཞེས་པའི་བར་དུ་ནི་འབྲས་བུ་ཆེ་ཆུང་ལས་ཐེག་པ་ཆེ་ཆུང་གི་རིམ་པ་བསྟན་པའོ། །

[Block 2878 [HEADING]]
#### དོན་གྱི་མདོ་བསྡུས་ཏེ་ལུང་བསྟན་པ། ^4-5-5-0

[Block 2879]
མདོ་ལས།

[Block 2880]
འོད་སྲུངས་འདི་ལྟ་བུ་ཡི་ཆོས་བཤད་པ། །ཞེས་པ་ནས། ང་ཡི་ཉན་ཐོས་ཐམས་ཅད་སངས་རྒྱས་འགྱུར། །ཞེས་པའི་བར་དུ་ནི༌[^2456]དོན་བསྡུ་བ་སྟེ། སྔར་བཀྲི་བའི་དོན་བསྟན། ཕྱིས་ངེས་པའི་དོན་བསྟན་པ་དང་། འབྲས་བུ་ཐོབ་པའི་ཕྱིར་ལུང་བསྟན་པ་སྟེ། འཕགས་པ་ཉན་ཐོས་པ་རྣམས་ཀྱི་སྤྱོད་པས་སངས་རྒྱས་སུ་འགྱུར་བར༌[^2457]ལུང་བསྟན་པའང་འགྲུབ་པ་ལ་དགོངས་ཏེ་ལུང་བསྟན་པ་ཡིན་ནོ། །

[Block 2881]
བྱང་ཆུབ་སེམས་དཔའི་སྤྱད་པ་སྤྱོད་པ་དང་། བྱང་ཆུབ་ཀྱི་སྤྱོད་པ་ལས་ཉམས་པའང་།[^2458] ཕྱིས་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་ཅིང་། དགེ་བའི་རྩ་བ་མ་ཉམས་ན་བླ་ན་མེད་པའི་འབྲས་བུ་ཐོབ་ཅེས་བསྟན་ཏོ།། །།

[Block 2882 [HEADING]]
### ལུང་བསྟན་པའི་ལེའུ། ^4-6-0

[Block 2883]
འདི་མན་ཆད་ལུང་བསྟན་པའི་ལེའུ་སྟེ། དེ་ཅིའི་ཕྱིར་ལུང་བསྟན་པ་ཞེས་གདགས་པ་དང་། མིང་བཤད་པ་དང་རྣམ་པ་གཉིས་སོ། །

[Block 2884 [HEADING]]
#### ཅིའི་ཕྱིར་ལུང་བསྟན་པ་ཞེས་གདགས་པ། ^4-6-1-0

[Block 2885]
[^2459]དེ་ལ་གཏན་ཚིགས་ནི་འཕགས་པ་ཤཱ་རིའི་བུ་དབང་པོ་རྣོན་པོ་ཡིན་པས་ཆོས་ཐོས་པ་ཙམ་གྱིས་གོ་བའི་ཕྱིར་ལུང་བསྟན་པ་དང་། གཞན་དབང་པོ་བར་མ༌[^2460]རྣམས་དོན་དཔེས་མཚོན་ཏེ་བསྟན་པས་གོ་བའི་ཕྱིར་ལུང་བསྟན་པའོ། །

[Block 2886]
ཡང་ན་ང་རྒྱལ་ཅན་རྣམས་སྤ་བཀོང་བའི་ཕྱིར་ཐེག་པ་ཐམས་ཅད་གཅིག་སྟེ། ཆེ་ཆུང་མེད་པའི་ཕྱིར་ལུང་བསྟན་པའོ། །

[Block 2887]
དེ་ཡང་ལུང་བསྟན་པའི་ཆོས་རྣམ་པ་གསུམ་སྟེ། རང་བཞིན་ཡོད་པའི་ཕྱིར་ལུང་བསྟན་པ་དང་། ཁྱད་པར་ཡོད་པའི་ཕྱིར་འབྲས་བུ་ཡོད་པས་ལུང་བསྟན་པ་དང་། ཆེ་བའི་བདག་ཉིད་ཅན་རྣམས་ལ་ཆེ་བའི་གཞུང་འོས་པ་དང་། རྒྱུ་ཆེ་བ་རྣམས་ལ་འབྲས་བུ་ཆེན་པོར་འོས་པས་ལུང་བསྟན་པ་དང་གསུམ་མོ། །

[Block 2888]
རང་བཞིན་གྱིས་ཡོད་པ༌[^2461]ཡང་ལུང་བསྟན་པར་འོས་པ་དང་། ལུང་བསྟན་པར་མི་འོས་པ་ནི་མ་རིག་པ་ལ་ཐོག་མ་ཡོད་དམ་མེད་ཅེས་འདྲི་བ་ལ་ལུང་མི་བསྟན་པ་ལྟ་བུའོ། །

[Block 2889]
རྒྱུ་ཁྱད་པར་ཅན་རྣམས་ནི་ལུང་བསྟན་པར་འོས་པའོ། །

[Block 2890]
རྒྱུ་ཆེ་བ་དང་། འབྲས་བུ་ཆེ་བ་ཡང་ལུང་བསྟན་པར་འོས་པའོ། །

[Block 2891]
རྒྱུ་ཆུང་བ་དང་འབྲས་བུ་ཆུང་བ་རྣམས་ནི་ལུང་བསྟན་པར་མི་འོས་པའོ། །

[Block 2892]
དགེ་བའི་རྩ་བ་སྨིན་པ་རྣམས་མྱུར་དུ་ལུང་བསྟན་པ་དང་། མ་སྨིན་པ་རྣམས་ཕྱིས་ལུང་བསྟན་པ་དང་། འཁོར་བ་སྤོང་ཞིང་འབྲས་བུ་མྱུར་དུ་ཐོབ་པར་འདོད་པ་རྣམས་ལ་མྱུར་དུ་ལུང་བསྟན་པ་དང་། ཐུགས་རྗེ་ཆེ་བས་འཁོར་བར་སྦྱོར་བ་རྣམས་བགས་ཀྱིས༌[^2462]ལུང་བསྟན་པའོ། །

[Block 2893]
ཡང་སྤྱིར་ལུང་བསྟན་པ་དང་། སོ་སོར་ཕྱེ་སྟེ་ལུང་བསྟན་པའོ། །

[Block 2894 [HEADING]]
#### མིང་བཤད་པ། ^4-6-2-0

[Block 2895]
མིང་དགྲོལ་བ་ནི་རྒྱུ་ཅི་བྱེད་པ་འབྲས་བུ་དེ་ཐོབ༌[^2463]སྟེ། དེ་སོ་སོར་སྟོན་པའི་ཕྱིར་ལུང་སྟོན་པ་ཞེས་བྱའོ། །

[Block 2896 [HEADING]]
#### འཕགས་པ་འོད་སྲུངས་ལུང་བསྟན་པ། ^4-6-3-0

[Block 2897 [HEADING]]
##### ཚིག་རྐྱང་པས་བསྟན་པ། ^4-6-3-1-0

[Block 2898]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཚིགས་སུ་བཅད་པ་འདི་གསུངས་ནས་ཞེས་པ་ནས་ངན༌[^2464]པའི་ཆོས་འཛིན་པར་འགྱུར་ཞེས་པའི་བར་དུ་ནི་འཕགས་པ་ཉན་ཐོས་བཞི་མངོན་དུ་ལུང་བསྟན་པ་ལ་སྔར་ནི་ཚིག་བརྒྱད་པས༌[^2465]བསྟན། འོག་ཏུ་ནི་ཚིགས་སུ་བཅད་པས་བསྡུས་ཏེ་བསྟན། དེ་ཡང་འཕགས་པ་འོད་སྲུངས་དང་པོར་ལུང་བསྟན། འཕགས་པ་གཞན་དེའི་འོག་ཏུ་ལུང་བསྟན་ཏོ། །

[Block 2899]
དེ་དག་ཀྱང་སོ་སོའི་དབང་པོ་ལས་ཁ་ཅིག་སྔར་འཕགས་པའི་འབྲས་བུ་ཐོབ་ལ། སངས་རྒྱས་སུ་ཕྱིས་གྲུབ་པ༌[^2466]ཡང་ཡོད་དེ། ཇི་ལྟར་དགེ་སློང་ལྔ་བརྒྱ་ཁྱད་པར་མེད་པ་ལས་སངས་རྒྱས་སུ་སྔ་ཕྱིར་གྲུབ་སྟེ། གཅིག་གིས་གཅིག་ལུང་བསྟན་པ་ལྟ་བུ་དང་།

[Block 2900]
ཐེག་པ་ཆེན་པོ་ལས་ཀྱང་སློབ་པ་དང་མི་སློབ་པ་རྣམས་ཁྱད་པར་ཡོད་པ་ལས།

[Block 2901]
དུས་གཅིག་ཏུ་སངས་རྒྱས་སུ་གྲུབ་པ༌[^2467]དང་། ཁ་ཅིག་སྔར་འཕགས་པ་ཐོབ་ལ་ཕྱིས་དེ་བས་ཕྱི་པ༌[^2468]རྣམས་སངས་རྒྱས་སུ་འགྲུབ་པ་ལྟ་བུ་སྟེ། འཕགས་པ་འོད་སྲུངས་ཆེན་པོས་སངས་རྒྱས་ཁྲི་ཕྲག་སུམ་བརྒྱ་ལ་བསྙེན་བཀུར་བྱས། འཕགས་པ་རབ་འབྱོར་གྱིས་སངས་རྒྱས་བྱེ་བ་ཁྲག་ཁྲིག་སུམ་བརྒྱ་ལ་བསྙེན་བཀུར་བྱས། འཕགས་པ་ཀཱ་ཏྱཱ་ཡ་ནས༌[^2469]སངས་རྒྱས་བྱེ་བ༌[^2470]ཁྲག་ཁྲིག་བརྒྱ་ལ་བསྙེན་བཀུར་བྱས། ཕྱིས་ཁྲག་ཁྲིག་གཉིས་ལ་བསྙེན་བཀུར་བྱས། འཕགས་པ་མཽད་གལ་ཆེན་པོས་སྔར་སངས་རྒྱས་བརྒྱད༌[^2471]སྟོང་ལ་བསྙེན་བཀུར་བྱས། ཕྱིས་ཁྲག་ཁྲིག་ཉིས་བརྒྱ༌[^2472]ལ་བསྙེན་བཀུར་བྱས་ཏེ། སངས་རྒྱས་སུ་ལུང་བསྟན་པ་ཡང་སངས་རྒྱས་ལ་བསྙེན་བཀུར་བྱས་པ་ལན་མང་དུ་ཡོད་མོད་ཀྱི་སྤྱོད་པ་རྒྱ་ཆེན་པོ་ལྡོག་པ་རྣམས་དྲང་བའི་ཕྱིར་བསྟན་ཏེ། སོ་སོར༌[^2473]དབང་པོ་རྣོ་རྟུལ༌[^2474]ལས་སྔ་ཕྱིར་ལུང་བསྟན་པ་ཡིན་ནོ། །

[Block 2902]
མདོ་ལས་དེ་ལུས་ཐ་མའི་ཚེ་རྒྱན༌[^2475]ཆེན་པོ་ཞེས་བྱ་བའི་བསྐལ་པ་ལ་ཞེས་པ་ནས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཏེ་ཞེས་པའི་བར་དུ་ནི་འབྲས་བུ་ཐོབ་པས་ལུང་བསྟན་པ་སྟེ། ཡང་དག་པའི་ཆོས་མཐོང་བའི་སྣང་བས་མཛེས་པའི་ཕྱིར་འོད་ཟེར་རབ་ཏུ་སྣང་ཞེས་བཏགས༌[^2476]སོ། །

[Block 2903]
མདོ་ལས་དེའི་ཚེ་ཚད་ནི་ཞེས་པ་ནས་མེ་ཏོག་གི་གཏོར་བ་ཞེས་པའི་བར་དུ་ནི་ཞིང་འོད་ཟེར་སྣང་བ་ཐོབ་པའི་ཡོན་ཏན་ལ་བཏགས་པ་དང་། བསྐལ་པ་སྤྱོད་པ་སྣ་ཚོགས་ཀྱིས་བརྒྱན་པའི་རྒྱན་ལས་བཏགས་པ་དང་། ཞིང་གི་རྒྱན༌[^2477]དེ་དག་ཀྱང་རྒྱན༌[^2478]དམ་པ་དང་ལྡན་པ། སྡིག་པ་མི་དགེ་བ་མེད་པ།[^2479] མཉམ་པ་རིན་པོ་ཆེ་བཞི་ལས་གཞི་བྱས་པ། ཤིང་རིན་པོ་ཆེས་བརྒྱན་པའི༌[^2480]ཐིག་གིས་རེའུ༌[^2481]བྲེས་པ། མེ་ཏོག་སྣ་ཚོགས་བཀྲམ་པའི་རྒྱན་དང་ལྡན་པའོ། །

[Block 2904]
མདོ་ལས་དེར་བྱང་ཆུབ་སེམས་དཔའ་བརྒྱད་སྟོང་མང་པོ་འབྱུང་བར་འགྱུར་རོ་ཞེས་པ་ནས་ཆོས་ཀུན་འཛིན་ལ་བརྩོན་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་འཁོར་མང་པོ་ཐམས་ཅད་ཀྱིས་དམ་པའི་ཆོས་བསྲུང་བ་དང་། ཡོངས་སུ་འཛིན་ཞེས་པའོ། །

[Block 2905 [HEADING]]
##### ཚིགས་སུ་བཅད་པས་བསྡུས་ཏེ་བསྟན་པ། ^4-6-3-2-0

[Block 2906]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས། བླ་ན་མེད་པའི་ཡེ་ཤེས་འདི་བསྒྲུབ་སྟེ་ཞེས་པའི་བར་དུ་ནི་ཚིགས་བཅད་དེ་རྣམས་ཀྱི༌[^2482]ནི་དང་པོ་གླེང་སྟེ་སྒོ་བ༌[^2483]དང་། ལུང་མངོན་དུ་བསྟན་པ་དང་བསྡུ་བའོ། །

[Block 2907]
མདོ་ལས།

[Block 2908]
དེ་ནི་ཐ་མའི་ལུས་ཚེ་འཇིག་རྟེན་མགོན། །ཞེས་པ་ནས། མཉམ་ཞིང་བཟང་ལ་བལྟ༌[^2484]ན་སྡུག་པར་གྱུར། །ཞེས་པའི་བར་དུ་ནི་དེ་ལ་ཡང་ཚིགས་བཅད་དང་པོ་ཕྱེད༌[^2485]ཀྱིས་ནི་རང་བཞིན་བསྟན། དེའི་འོག་མ་ཚིགས་བཅད་གསུམ་གྱིས་ནི་ངོ་མཚར༌[^2486]ཉིད་བསྟན། དེའི་འོག་མ་གསུམ་གྱིས་ནི་འཁོར་བསྟན། དེའི་འོག་མ་ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་ཚེའི་ཚད་བསྟན། ངོ་མཚར་གྱི་མཚན་ཉིད་ནི་མི་དགེ་བ་མེད་པ་ལ་སོགས་པ་རྣམ་པར་དག་པའི་ཞིང་རྒྱན་བརྒྱད་དོ། །

[Block 2909]
སྤོས་དྲི་ཡིད་དུ་འོང་བ་འབྱུང་བ་ནི་ཚིག་རྐྱང་པའི་ནང་ནས་མི་འབྱུང་སྟེ། ཚུལ་ཁྲིམས་ཀྱི་དྲི་དམ་པ་དང་སྦྱར་རོ། །

[Block 2910]
མདོ་ལས།
--- END BLOCKS ---
