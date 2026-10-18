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
[Block 3011]
མདོ་ལས་འདི་ལྟར༌[^2548]སྔོན་དེའི་ཚེ་དེའི་དུས་ཞེས་པ་ནས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་སོ་ཞེས་པའི་བར་དུ་ནི་དངོས་སུ་བསྟན་པའོ། །

[Block 3012 [HEADING]]
###### དྲིས་པའི་ལན། ^4-7-4-1-2-0

[Block 3013]
མདོ་ལས་དགེ་སློང་དག་དེ་བཞིན་གཤེགས་པ་དེ་བྱུང་ནས་ཞེས་པ་ནས་སའི་ཁམས་དེ་ཐམས་ཅད་བཏགས༌[^2549]ན་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་དྲིས་པ་དང་། ལན་གདབ་པ་སྟེ། འདི་ནི་དྲིས༌[^2550]པའོ། །

[Block 3014]
མདོ་ལས་དགེ་སློང་རྣམས་དེ་ཡིད་ལ་ཇི་སྙམ་ཞེས་པ་ནས་བཅོམ་ལྡན་འདས་དེ་མ་ལགས་སོ་ཞེས་པའི་བར་དུ་ནི་དྲིས་པའི་ལན་བཏབ་པའོ། །

[Block 3015]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཀྱི༌[^2551]ཞེས་པ་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་བཞིན་ནོ་ཞེས་པའི་བར་དུ་ནི་འདིས་ནི་མངོན་པར་ཤེས་པ་ཆེན་པོ་སྟོན་ཏེ། ཡེ་ཤེས་ཀྱི་གཟིགས་པས་མཁྱེན་ཞེས་པའོ། །

[Block 3016]
ཡང་དེ་དགོངས་ཤིང་མཁྱེན་པ་ཡང་དགོངས་པ་རྣམ་བཞིའི་ཚུལ་གྱིས་མཁྱེན་ཏེ། མཉམ་པ་ལ་དགོངས་པ་དང་། དུས་ཐ་དད་པ་ལ་དགོངས་པ་དང་། དོན་ཐ་དད་པ་ལ་དགོངས་པ་དང་། སེམས་ཅན་གྱི་མོས་པ་ལ་དགོངས་པའོ། །

[Block 3017 [HEADING]]
##### ཚིགས་བཅད་ཀྱིས་བསྡུ་བ། ^4-7-4-2-0

[Block 3018 [HEADING]]
###### དུས་ཀྱི་མཐའ་བསྟན་པ། ^4-7-4-2-1-0

[Block 3019]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱི༌[^2552]ཞེས་པ་ནས། མངོན་ཤེས་ཡེ་ཤེས་ཟིལ་གནོན་ཐུབ་ཆེན་པོ། །ཞེས་པའི་བར་དུ་ནི། དུས་ཀྱི་མཐའ་བསྟན་པ་དང་། མཁྱེན་གཟིགས་བསྟན་པ་སྟེ། དེ་ལ་ཡང་སྔར་ནི་སྒོ། །ཕྱིས་ནི་བསྐལ་པའི་གྲངས་བསྟན་པ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 3020]
མདོ་ལས།

[Block 3021]
དེའི་ཚེ༌[^2553]བླ་མེད་རྒྱལ་བར་གྱུར། །ཞེས་པ་ནས། བསྐལ་པ་མང་པོ་དེ་སྙེད༌[^2554]ཟད་པར་གྱུར། །ཞེས་པའི་བར་དུ་ནི་བསྐལ་པའི་གྲངས་བསྟན་པའོ། །

[Block 3022 [HEADING]]
###### མཁྱེན་གཟིགས་བསྟན་པ། ^4-7-4-2-2-0

[Block 3023]
མདོ་ལས།

[Block 3024]
དེ་ལྟར་འདྲེན་པ་མྱ་ངན་ལས་འདས་པ།[^2555] །ཡུན་རིང་ཞེས་པ་ནས། དྲན་པ་ཕྲ་ཞིང་ཟག་པ་མེད་པ་པོ། །ཞེས་པའི་བར་དུ་ནི་མཁྱེན་གཟིགས་བསྟན་ཏོ། །

[Block 3025 [HEADING]]
#### དྲིས་པའི་དོན། ^4-7-5-0

[Block 3026]
མདོ་ལས་དགེ་སློང་འདི་ལྟར་ཡང་མངོན་པར་ཤེས་པ་ཆེན་པོའི་ཡེ་ཤེས་ཀྱི༌[^2556]ཟིལ་གྱིས་གནོན་པ་ཞེས་པ་ནས་ལྔ་བཅུ་རྩ་བཞིར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་དྲིས་པའི་དོན་ཉིད་འོག་ནས་སྟོན་ཏོ། །

[Block 3027 [HEADING]]
##### དེ་བཞིན་གཤེགས་པའི་ཚེའི་ཚད། ^4-7-5-1-0

[Block 3028]
འདི་ནི་དེ་བཞིན་གཤེགས་པའི་ཚེའི་ཚད་དང་། ཆོས་རྙེད་པར་དཀའ་བ་དང་། ཆོས་མངོན་དུ་རྙེད་པ་དང་གསུམ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 3029 [HEADING]]
##### ཆོས་རྙེད་པར་དཀའ་བ། ^4-7-5-2-0

[Block 3030]
མདོ་ལས་བཅོམ་ལྡན་འདས་དེ་བླ་ན་མེད་པ་ཞེས་པ་ནས་དེས་ཆོས་མངོན་དུ་ནི་མ་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་འདིས་ཆོས་རྙེད་པར་དཀའ་བ་བསྟན་པ་སྟེ། དེ་མངོན་དུ་བྱ་བར་སྟོན་པ་དང་། འདུག་ཏུ་བཅུག་པ་དང་། མེ་ཏོག་གིས་གཏོར་བ་དང་། མངོན་དུ་དགའ་བ་བསྟན་པའོ། །

[Block 3031]
འགྲེལ་པ་ལས་ཀྱང་འདིས་བྱང་ཆུབ་ཐོབ་པར་དཀའ་བ་བསྟན་པ༌[^2557]སྟེ། མདོ་དག་ལས་དོན་རྣམ་པ་བཅུས་བྱང་ཆུབ་ཀྱི་སྙིང་པོ་ལ་གནས་པར་འགྱུར་ཞེས་གསུངས་ཏེ། ས་ཐམས་ཅད་གཡོ་བར་མཛད་པ་ནས་སེམས་ཅན་ཐམས་ཅད་བསྡུ་བར་མཛད༌[^2558]ནས་གདོད་བྱང་ཆུབ་ཀྱི་སྙིང་པོ་ལ་བཞུགས་སོ། །

[Block 3032]
བདུད་བཏུལ་བ་ཡང་སངས་རྒྱས་ཤཱཀྱ་ཐུབ་པ་ནི་སྔར་མངོན་པར་བྱང་ཆུབ་སྟེ། ཕྱིས་བདུད་བཏུལ་ཞེས་ཀྱང་འབྱུང་། མདོ་གཞན་དག་ལས་སྔར་བདུད་བཏུལ་ཏེ་ཕྱིས་མངོན་པར་བྱང་ཆུབ་ཅེས་ཀྱང་འབྱུང་། སངས་རྒྱས་བྱམས་པ་ནི་ནམ་རབ་ཏུ་བྱུང་བའི་ཉིན་པར་བྱང་ཆུབ་ཀྱི་སྙིང་པོ་ལ་རེག་པར་འགྱུར། སངས་རྒྱས་ཤཱཀྱ་ཐུབ་པ་ནི་ལོ་དྲུག་གི་བར་དུ་ནི་དཀའ་བ་སྤྱད་ནས་གཟོད༌[^2559]སངས་རྒྱས་བཅོམ་ལྡན་འདས་འདི༌[^2560]བསྐལ་པ་བཅུའི་བར་དུ་གཞེས་ཤིང་ཆོས་མངོན་དུ་མ༌[^2561]གྱུར་ཏེ༌[^2562]ཞེས་གསུངས་སོ། །

[Block 3033]
མདོ་ལས་འདི་ལྟར་ཡང་དགེ་སློང་བཅོམ་ལྡན་འདས་དེ་ཞེས་པ་ནས་སེང་གེའི་ཁྲི་ཆེན་པོ་འཕང་དུ་དཔག་ཚད་བརྒྱ་པ་བཤམས་ཞེས་པའི་བར་དུ་ནི་བཞུགས་པ་བསྟན་ཏེ། ལྷ་ཐམས་ཅད་ཀྱིས༌[^2563]བཅོམ་ལྡན་འདས་ཀྱི་གདན་བཤམས༌[^2564]ཞེས་པའི་དོན་ཏོ། །

[Block 3034]
མདོ་ལས་བཅོམ་ལྡན་འདས་དེ་བྱང་ཆུབ་ཀྱི་སྙིང་པོར་བཞུགས་མ་ཐག་ཏུ་ཞེས་པ་ནས་བཅོམ་ལྡན་འདས་དེ་ལ་མངོན་པར་བབ་པོ༌[^2565]ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་དེ་ལ་མེ་ཏོག་གི་ཕུང་པོ་རི་རབ་ཙམ་སྤུངས་ཏེ་མཆོད་པ་དང་སྦྱར་ན་ལོངས་སྤྱོད་པའི་སྐུ་ཡིན་པར་མངོན་ནོ། །

[Block 3035]
མདོ་ལས་རྒྱལ་ཆེན་བཞིའི་རིས་ཀྱི་ལྷའི་སྲས་པོ་ཞེས་པ་ནས་རྒྱུན་མི་འཆད་པ་རབ་ཏུ་བསིལ༌[^2566]ཏོ་ཞེས་པའི་བར་དུ་ནི་རོལ་མོས་དགྱེས་པ་བསྐྱེད་ཅིང་མཆོད་པའོ། །

[Block 3036 [HEADING]]
##### ཆོས་མངོན་དུ་རྙེད་པ། ^4-7-5-3-0

[Block 3037]
མདོ་ལས་དེ་ན་དགེ་སློང་རྣམས་ལ་ཞེས་པ་ནས་མངོན་པར་སངས་རྒྱས་སོ་ཞེས་པའི་བར་དུ་ནི་འབྲས་བུ་བརྙེས་པ་བསྟན་ཏོ། །

[Block 3038 [HEADING]]
#### ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ། ^4-7-6-0

[Block 3039 [HEADING]]
##### ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་གསོལ་བ། ^4-7-6-1-0

[Block 3040]
མདོ་ལས་དེ་ལྟར་མངོན་པར་སངས་རྒྱས་མ་ཐག་ཏུ་ཞེས་པ་ནས་ཡེ་ཤེས་འབྱུང་གནས་ཞེས་བྱ་བར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་བསྟན༌[^2567]ཏེ། སྔར་མཆོད་པ་བྱས་ནས་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་གསོལ་བ་དང་། ཕྱིས་ཀྱང་དེ་བཞིན་གཤེགས་པས་ཕྱོགས་བཅུའི་ལྷ་དང་ཚངས་པ་ལ་བཤད་པར་གནང་བ༌[^2568]སྟེ།

[Block 3041 [HEADING]]
###### རྒྱལ་བུ་བཅུ་དྲུག་གིས་མཆོད་དེ་ཆོས་བཤད་པར་གསོལ་བ། ^4-7-6-1-1-0

[Block 3042]
དང་པོ་ལ་ཡང་སྔར་རྒྱལ་བུ་བཅུ་དྲུག་གིས་མཆོད་དེ་ཆོས་བཤད་པར་གསོལ་བ་དང་། ཕྱིས་ལྷ༌[^2569]ཚངས་པས་མཆོད་དེ་གསོལ་བའོ། །

[Block 3043]
དེ་ཡང་གཉེན་རྣམས་མངོན་དུ་གྱུར་པ་དང་། མངོན་དུ་མ་གྱུར་པའོ། །

[Block 3044]
ཆོས་བཤད་པར་གསོལ་བ་ཡང་སྔར་བཅོམ་ལྡན་འདས་ཀྱི་དྲུང་དུ་དོང་བ་དང་། ཕྱིས་བསྟོད་དེ་མངོན་པར་གསོལ་བའོ། །

[Block 3045 [HEADING]]
###### **བཅོམ་ལྡན་འདས་ཀྱི་དྲུང་དུ་དོང་བ།** ^4-7-6-1-1-1-0

[Block 3046]
བཅོམ་ལྡན་འདས་ཀྱི་གན་དུ་འགྲོ་བ་ཡང་སོ་སོའི་འཁོར་དང་གཉེན་དུ་བཅས་ཏེ་དོང་བ་བསྟན་ཏོ། །

[Block 3047]
མདོ་ལས་འདི་ལྟར་དགེ་སློང་རྣམས་རྒྱལ་བུ་གཞོན་ནུ་བཅུ་དྲུག་པོ་དེ་དག་ཅེས་པ་ནས་གང་ན་བ༌[^2570]དེར་དོང་ངོ་ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཀྱི་གན་དུ་ཆས་པ་བསྟན་ཏོ། །

[Block 3048 [HEADING]]
###### **བསྟོད་དེ་མངོན་པར་གསོལ་བ།** ^4-7-6-1-1-2-0

[Block 3049]
མདོ་ལས་བཅོམ་ལྡན་འདས་འདི་ལ་བཀུར་སྟི་བྱས་ཞེས་པ་ནས། ཁྱོད་ནི་རབ་ཞི་ཟག་པ་མེད་ལ་གནས་ནས་ཞེས་པའི་བར་དུ་ནི་ཕྱག་འཚལ་བ་ནི་ལུས་ཀྱིས༌[^2571]ཕྱག་འཚལ་བ་དང་། ངག་གིས་བསྟོད་དེ་ཕྱག་འཚལ་བའོ། །

[Block 3050]
བཅོམ་ལྡན་འདས་ལ་བསྟོད་པ་ཡང་དགོངས་པའི་སྨོན་ལམ་རྫོགས་པའི་སྒོ་ནས་བསྟོད་པ་དང་། སྔོན་མཛད་པའི་ཡོན་ཏན་གྱི་སྒོ་ནས་བསྟོད་པའོ། །
--- END BLOCKS ---
