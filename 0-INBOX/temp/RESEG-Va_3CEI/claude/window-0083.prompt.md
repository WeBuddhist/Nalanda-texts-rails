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

[Block 2911]
དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་བྱེ་བ་སྟོང་། །ཞེས་བྱ་བ་ནས།

[Block 2912 [VERSE]]
བསྐལ་པ་འབུམ༌[^2487]གྱི་ཡེ་ཤེས་ཀྱི་གྲངས༌[^2488]ཀྱང་། །
ཞེས་པའི་བར་དུ་ནི་འཁོར་རྣམས་སྟོན་ཏེ།
བྱང་ཆུབ་སེམས་དཔའ་དང་འཁོར་རྣམས་ཀྱི་དོན་ཏོ། །

[Block 2913]
མདོ་ལས།

[Block 2914]
དེ་ནི་བར་གྱི་བསྐལ་པ་བཅུ་གཉིས་གནས།[^2489] །ཞེས་པ་ནས། འོད་ཟེར་བར་སྣང་དེ་ཡི་རྒྱན༌[^2490]འདི་འདྲ། །ཞེས་པའི་བར་དུ་ནི། ཚིགས་བཅད་ཕྱེད་ཀྱིས་ནི་ཚེ་ཚད་བསྟན། ཕྱི་མས་ནི་བསྡུས་པའོ། །

[Block 2915 [HEADING]]
#### ཉན་ཐོས་ཆེན་པོ་གསུམ་ལུང་བསྟན་པ། ^4-6-4-0

[Block 2916 [HEADING]]
##### ལུང་བསྟན་པར་གསོལ་བ། ^4-6-4-1-0

[Block 2917]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་གནས་བརྟེན༌[^2491]མཽད་གལ་གྱི་བུ་ཆེན་པོ་དང་ཞེས་པ་ནས་འདི་སྐད་གསོལ་ཏོ་ཞེས་པའི་བར་དུ་ནི་འདིས་འཕགས་པ་ཉན་ཐོས་ཆེན་པོ་གསུམ་གྱིས་ལུང་བསྟན་པར་གསོལ་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་དངོས་སུ་ལུང་བསྟན་པའོ། །

[Block 2918]
ལུས་འདར་ཞིང་མིག་མི་འཛུམས་པར༌[^2492]བལྟ༌[^2493]ཞིང་ཞེས་པ་ནི་གཅིག་ཏུ་འདུན་པའི་སེམས་སོ། །

[Block 2919 [HEADING]]
###### བསྟོད་དེ་གསོལ་བ། ^4-6-4-1-1-0

[Block 2920]
མདོ་ལས།

[Block 2921]
དགྲ་བཅོམ་ཞིང་ནི་ཆེར་དཔའ་བ། །ཞེས་པ་ནས། རྒྱལ་བས་བདག་ཅག་ལུང་སྟོན་ཅིག །ཞེས་པའི༌[^2494]བར་དུ་ནི་ཚིག་དེ་དག་ལ་བསྟོད་དེ་གསོལ་བ་དང་དཔེ་ལས་གླེངས་ཏེ༌[^2495]གསོལ་བ་དང་། གསོལ་བའི་མདོ་བསྡུས་པ་དང་གསུམ་སྟེ། འདི་ནི་བཅོམ་ལྡན་འདས་ལ་ཡོན༌[^2496]ཆེན་པོའི་སྒོ་ནས་བསྟོད་དེ་གསོལ་བའོ། །

[Block 2922 [HEADING]]
###### དཔེ་ལས་གླེངས་ཏེ་གསོལ་བ། ^4-6-4-1-2-0

[Block 2923]
མདོ་ལས་མུ་གེ་བྱུང་ཚེ་ལ་ལའི་ཞེས་པ་ནས་ཐུབ་པ་ཆེན་པོ་མཐར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི། མུ་ག་བྱུང་ཚེ་ཞེས་པ་ནི་དཔེ་ལས་གླེངས་ཏེ་གསོལ་བ་སྟེ། ཉན་ཐོས་པ་རྣམས་ཐེག་པ་ཆེན་པོའི་ཆོས་ཀྱིས་བཀྲེས་པའི་ཕྱིར་མུ་གེ་ཞེས་པའོ། །

[Block 2924]
བཅོམ་ལྡན་འདས་ཀྱིས་ལུང་བསྒོ་བ༌[^2497]ལ། ལྟོས་ཤིང༌[^2498]ཐེག་པ་ཆེན་པོ་འཇུག་པ་ལ་མི་སྤོབས་པ་ཡང་དཔེ་དེ་དང་འདྲའོ། །

[Block 2925 [HEADING]]
###### གསོལ་བའི་མདོ་བསྡུས་པ། ^4-6-4-1-3-0

[Block 2926]
དཔའ་བོ༌[^2499]ཆེན་པོས་ལུང་སྟོན་ཅིག །ཅེས་པ་ནི་གསོལ་བའི་མདོ་བསྡུས་པའོ། །

[Block 2927 [HEADING]]
##### སོ་སོར་ལུང་བསྟན་པ། ^4-6-4-2-0

[Block 2928 [HEADING]]
###### འཕགས་པ་རབ་འབྱོར་ལུང་བསྟན་པ། ^4-6-4-2-1-0

[Block 2929 [HEADING]]
###### **ཚིག་རྐྱང་པས་སྤྲོ་བ།** ^4-6-4-2-1-1-0

[Block 2930]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་བྱང་ཆུབ་བསྒྲུབ་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཉན་ཐོས་ཆེན་པོ་གསུམ་སོ་སོར་ལུང་བསྟན་པ་སྟེ།

[Block 2931]
དང་པོ་ཚིག་རྐྱང་པས་སྤྲོ་བ་དང་། དེའི་འོག་ཏུ་ཚིགས་སུ་བཅད་པས་བསྡུ་བའོ། །

[Block 2932 [HEADING]]
###### **རྒྱུ།** ^4-6-4-2-1-1-1-0

[Block 2933]
ཚིག་རྐྱང་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། སྔར་ནི་རྒྱུ་བསྟན། དེའི་འོག་ཏུ་འབྲས་བུ་བསྟན་ཏེ། འདི་ནི་རྒྱུའོ། །

[Block 2934 [HEADING]]
###### **འབྲས་བུ།** ^4-6-4-2-1-1-2-0

[Block 2935]
མདོ་ལས་དེ་ལྟ་བུའི་ལྷག་པའི་བྱ་བ་བྱས་ཏེ་ལུས་ཐ་མ་ལ་ཞེས་པ་ནས། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཞེས་པའི་བར་དུ་ནི་འབྲས་བུ་བསྟན་པ་སྟེ། ལུང་བསྟན་པའི་མཚན་ཉིད་དགུ་སྟེ། རང་བཞིན་གྱིས་ལུང་བསྟན་པ་ལ་སོགས་པའོ། །

[Block 2936]
མདོ་ལས་སངས་རྒྱས་ཀྱི་ཞིང་ནི་རིན་པོ་ཆེ་འབྱུང་བ་ཞེས་བྱ་བར་འགྱུར་རོ་ཞེས་པ་ནས༌[^2500]ཉན་ཐོས་བརྒྱ་སྟོང་མང་པོ་འདུལ་ལོ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པའི་ཞིང་རྒྱན་སྣ་ཚོགས་ཀྱིས་བརྒྱན་པ་ན་འཁོར་ཕྱི་ནང་རྣམ་གཉིས་དང་བཞུགས་པ༌[^2501]བསྟན་ཏོ། །

[Block 2937 [HEADING]]
###### **ཚིགས་སུ་བཅད་པས་བསྡུ་བ།** ^4-6-4-2-1-2-0

[Block 2938 [HEADING]]
###### **བསྒོ་བ།** ^4-6-4-2-1-2-1-0

[Block 2939]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚེ་ན་ཞེས་པ་ནས་རབ་ཏུ་རིག་པར་བྱའོ། །

[Block 2940]
ང་ལས་ཉོན་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་སུ་བཅད་པ་བཅུ་གཉིས་ལ་གཉིས་སུ་དབྱེ་སྟེ།

[Block 2941]
དང་པོ་ཚིག་གཅིག་གིས་ནི་བསྒོ་བ་བསྟན། དེའི་འོག་མ་བཅུ་གཅིག་གིས་ནི་དངོས་སུ་བསྟན་པ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 2942 [HEADING]]
###### **དངོས་སུ་བསྟན་པ།** ^4-6-4-2-1-2-2-0

[Block 2943]
མདོ་ལས།

[Block 2944 [HEADING]]
###### **རྒྱུ་དང་འབྲས་བུ་སྦྱར་ཏེ་བསྟན་པ།** ^4-6-4-2-1-2-2-1-0

[Block 2945]
ང་ཡི༌[^2502]ཉན་ཐོས་གནས་བརྟན་རབ་འབྱོར་འདི། །ཞེས་པ་ནས། དྲང་སྲོང་ཆེན་པོ་གསེར་གྱི་སྡོང་པོ་འདྲ། །ཞེས་པའི་བར་དུ་ནི་འདིས༌[^2503]དངོས་སུ་བསྒོ་བ་སྟེ། རྒྱུ་དང་འབྲས་བུ་སྦྱར་ཏེ་བསྟན་པ་དང་། ངོ་མཚར་བདུན་དང་། འཁོར་དང་ཚེའི་ཚད་ལ་སོགས་པ་སྟོན་ཏེ། འདི་ནི་དང་པོའོ། །
--- END BLOCKS ---
