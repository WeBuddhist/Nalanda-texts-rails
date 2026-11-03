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
[Block 3606]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཤཱཀྱ་ཐུབ་པས་ཞེས་པ་ནས་ནམ་མཁའ་བར་སྣང་ལ་བཞུགས་སོ་ཞེས་པའི་བར་དུ་ནི་མཆོད་རྟེན་དབྱེ་བར་དགོངས་པ་སྟེ། དེ་ཡང་དོན་གྲུབ༌[^3002]ནས་ནམ་མཁའ་ལ་བཞུགས་པ་དང་། འཁོར་བཞི་པོ་ལངས་ནས་ཞལ་དུ་བལྟ་བ༌[^3003]དང་། མཆོད་རྟེན་མངོན་པར་ཕྱེ་བའོ། །

[Block 3607 [HEADING]]
###### **འཁོར་བཞི་པོ་ལངས་ནས་ཞལ་དུ་བལྟ་བ།** ^4-11-4-2-4-2-2-0

[Block 3608]
མདོ་ལས་འཁོར་བཞི་པོ་དེ་དག་སྟན་ལས་ལངས་ནས་ཐལ་མོ་སྦྱར་ཏེ། བཅོམ་ལྡན་འདས་ལགས་སུ་བལྟ་ཞིང་འཁོད་དོ་ཞེས་པ་ནི༌[^3004]འཁོར་ལངས་པ་བསྟན་པའོ། །

[Block 3609 [HEADING]]
###### **མཆོད་རྟེན་མངོན་པར་ཕྱེ་བ།** ^4-11-4-2-4-2-3-0

[Block 3610]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱི༌[^3005]ཞེས་པ་ནས། ས་ལེར་བྱས་སོ་ཞེས་པའི་བར་དུ་ཕྱག་གཡས་པ་ཞེས་པ་ནི་བཀྲ་ཤིས་པར་བྱ་བའོ།[^3006] །མདོ་ལས་དེ་བཞིན་གཤེགས་པའི་ཞེས་པ་ནས་ཁོ་བོ་འདིར་འོངས་སོ་ཞེས་པའི་བར་དུ་ནི་མཆོད་རྟེན་ཕྱེ་བས་འཆད་པ་དང་། ཉན་པ་རྣམས་སྤྲོ་བར་བྱ་བའི་གཏན་ཚིགས་བསྟན་ཏེ། སྐུ་མངོན་པར་སྟོན་ཅིང་གསུང་སྨྲ་བ་དང་། མེ་ཏོག་འཐོར་བ༌[^3007]གཉིས་ལས༌[^3008]འདི་ནི་དང་པོའོ། །

[Block 3611]
མདོ་ལས་དེ་ནས་འཁོར་བཞི་པོ་དེ་དག་གི་ཞེས་པ་ནས། རིན་པོ་ཆེའི་ཕུང་པོས་གཏོར་ཏོ་ཞེས་པའི་བར་དུ་ནི་མེ་ཏོག་འཐོར་བ་བསྟན་ཏོ། །

[Block 3612]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་རིན་ཆེན་མང་ཞེས་པ་ནས་འདིར་བཞུགས་ཏེ་དེ་སྐད་གསུང་ངོ་ཞེས་པའི་བར་དུ་ནི་འཁོར་མང་པོ་ལ་མཆོད་ཅིང་ཡོངས་སུ་གཏད་པ་སྟོན་པའོ། །

[Block 3613]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཤཱཀྱ་ཐུབ་པ་ཞེས་པ་ནས་བཞུགས་པར་སྣང་ངོ་ཞེས་པའི་བར་དུ༌[^3009]སྐུ་གསུམ་དོན་ཆེན་པོ་མཛད་པར་འདྲ་བར་བསྟན་པའི་ཕྱིར་སངས་རྒྱས་དེ་གཉིས༌[^3010]གདན་གཅིག་ལ་བཞུགས་པ་དང་ཐེག་པ་གཅིག་ལ་འདུ་བར་བསྟན་པའི་ཕྱིར་གདན་གཅིག་ལ་བཞུགས་པའོ། །

[Block 3614]
མདོ་ལས་དེ་ན་འཁོར་བཞི་པོ་དེ་དག་ཅེས་པ་ནས་བར་སྣང་ལ་འཕགས་པར་བྱའོ་སྙམ་དུ་སེམས་སོ་ཞེས་པའི་བར་དུ་ནི་ཐམས་ཅད་སྟོང་པའི་མཚན་ཉིད༌[^3011]གནས་པར་བྱ་བ༌[^3012]བསྟན་ཏོ། །

[Block 3615]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས། བར་སྣང་ལ་བཀོད༌[^3013]དོ་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེན་པོ་ཐོས་པས་བླ་ན་མེད་པའི་འབྲས་བུ་འགྲུབ་པ༌[^3014]བསྟན་ཏོ། །

[Block 3616]
མདོ་ལས།

[Block 3617]
བཅོམ་ལྡན་འདས་ཤཱཀྱ་ཐུབ་པ༌[^3015]ཞེས་པ་ནས། ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་བཞེད་དོ་ཞེས་པའི་བར་དུ་ནི་ཡོངས་སུ་གཏད་པ་བསྟན་ཏོ། །

[Block 3618 [HEADING]]
#### ཚིགས་བཅད། ^4-11-5-0

[Block 3619]
མདོ་ལས།

[Block 3620]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^3016]དེའི་ཚེ་ན་ཞེས་པ་ནས། ཆོས་ཀྱི་ཕྱིར་དུ་བརྩོན་འགྲུས་མི་སྐྱེད་ཞེས༌[^3017]པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་བཞི་བཅུ་རྩ་བརྒྱད་ལ་གཉིས་སུ་དབྱེ་སྟེ། ཚིགས་བཅད་བཅུ་གཉིས་ཀྱིས་ནི་མཆོད་རྟེན་མངོན་པར་འབྱུང་བ་བསྟན། ཆོས་ཐོས་པའི་གཏན་ཚིགས་ཀྱིས༌[^3018]དམ་པ་བསྟན། དེའི་འོག་གི་ཚིགས་བཅད་སུམ་ཅུ་རྩ་དྲུག་གིས་ནི་འཁོར་རྣམས་མདོ་འདི་ཐོས་པར་མོས་པ་དང་། ཡོངས་སུ་གཏད་པ་བསྟན་ཏོ། །

[Block 3621 [HEADING]]
##### མཆོད་རྟེན་མངོན་པར་འབྱུང་བ། ^4-11-5-1-0

[Block 3622]
མདོ་ལས།

[Block 3623]
ཚིག་དང་པོ་ལ་ཡང་རྣམ་པ་གཉིས་སུ་དབྱེ་སྟེ། ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས་ནི༌[^3019]མཆོད་རྟེན་མངོན་པར་བྱུང་བས་འཁོར་རྣམས་སྤྲོ་བ་བསྐྱེད། དེའི་འོག་གི་ཚིག་ཕྱེད་དང་བཅུ་གཅིག་གིས་ནི་མཆོད་རྟེན་ཕྱེ་སྟེ་འཁོར་ལ་ཆོས་སྟོན་པ་བསྟན་ཏོ། །

[Block 3624]
མདོ་ལས།

[Block 3625]
བསྐལ་པ་བྱེ༌[^3020]མང་མྱ་ངན་ལས་འདས་ཀྱང་། །ཞེས་པ་ནས་ཡོངས་སུ་རྒྱུ་བ་ཕྱོགས་བཅུ་ཐམས་ཅད༌[^3021]ཅེས་པའི་བར་དུ་ནི་མཆོད་རྟེན་ཕྱེ་སྟེ་འཁོར་རྣམས་སྤྲོ་བ་བསྐྱེད་པ་ལ་ཚིག་དང་པོ་གཉིས་ཀྱིས་ནི་གླེང་གཞི་བསྟན། ཕྱི་མ་ཕྱེད་དང་དགུས་ནི་མཆོད་རྟེན་ཕྱེ་སྟེ་མངོན་པར་སྟོན་པ་བསྟན་ཏོ། །

[Block 3626]
མདོ་ལས།

[Block 3627]
འདི་དག་ཐམས་ཅད་ང་ཡི་ལུས༌[^3022]གཟུགས་ཏེ། །ཞེས་པ་ནས། རྫུ་འཕྲུལ་གྱིས་ནི༌[^3023]ཡོངས་སུ་དག་པར་བྱས། །ཞེས་པའི་བར་དུ་ནི། འདི་མན་ཆད་ཞིང་བསྒྱུར་བ་དང་། སངས་རྒྱས་བཞུགས་པ་དང་། སྐུ་ལས༌[^3024]སྤོས་ཀྱི་དྲི་འབྱུང་བ་དང་། སེམས་ཅན་གྱི་དོན་ལ་འཇིག་རྟེན་ན་བཞུགས་པའོ། །

[Block 3628]
མདོ་ལས།

[Block 3629]
འདི་ལྟ་བུར་ནི་འདི་དག་ངས་བཤད་པ། །ཞེས་པ་ནས། མུན་ནག་ཆེན་པོའི་ནང་ན༌[^3025]མེ་བཞིན་ནོ། །ཞེས་པའི་བར་དུ་ནི་སངས་རྒྱས་བཞུགས་པ་བསྟན་ཏོ། །

[Block 3630]
མདོ་ལས།

[Block 3631]
ཕྱོགས་བཅུ་རྣམས་སུ་ཡིད་དུ་འོང་བའི༌[^3026]དྲི། །ཞེས་པ་ནས། ཆོས་ཀྱི་གཞུང་ཡང་འཛིན་པ་ནི་ཞེས་པའི་བར་དུ་ནི་དྲི་འབྱུང་བ་དང་། སེམས་ཅན་ལ་ཆོས་འཆད་པ་སྟོན་ཏོ། །

[Block 3632 [HEADING]]
##### འཁོར་རྣམས་མདོ་འདི་ཐོས་པར་མོས་པ་དང་ཡོངས་སུ་གཏད་པ། ^4-11-5-2-0

[Block 3633]
མདོ་ལས།

[Block 3634]
མྱུར་དུ་ཚིག་རྣམས་རབ་སྨོས་ཤིག །ཅེས་པ་ནས་འདྲེན་པ་མང་པོ་བྱེ་བ་འདིར་ལྷགས་ཞེས་པའི་བར་དུ་ནི་འཁོར་རྣམས་མདོ་འདི་ཐོས་པར་མོས་པ་དང་། ཡོངས་སུ་གཏད་པའོ། །

[Block 3635 [HEADING]]
###### འཁོར་ཆོས་ཉན་པ་མོས་པ། ^4-11-5-2-1-0

[Block 3636]
དེ་ཡང་གསུམ་དུ་དབྱེ་སྟེ། ཚིགས་བཅད་ཕྱེད་དང་བཅུས་ནི་འཁོར་ཆོས་ཉན་པ་མོས་པ་བསྟན། དེའི་འོག་མ་ཚིག༌[^3027]བཅུ་དགུས་ནི་ཁྱད་པར་བསྟན་ཡང་ཚིག་ཕྱེད་དང་བརྒྱད་ཀྱིས་ནི་སྤྱོད་པ་དམ་པ་བསྡུས་པ༌[^3028]བསྟན།

[Block 3637 [HEADING]]
###### **འཛིན་པ་དང་ཀློག་པ་དང་འདོན་པར་མོས་པ།** ^4-11-5-2-1-1-0

[Block 3638]
དང་པོ་ལ་ཡང༌[^3029]རྣམ་པ་གསུམ་སྟེ། །ཚིག་ཕྱེད་དང་བཞིས་ནི་འཛིན་པ་དང༌[^3030]ཀློག་པ་དང་འདོན་པར་མོས་པ་བསྟན། ཚིག་བཞིས་ནི་ཆོས་བསྲུང༌[^3031]བ་རྣམས་ཡི་དམ་གྱི་མཐར་ཕྱིན་པ་བསྟན། ཡང་ཚིག་གཉིས་ཀྱིས༌[^3032]ནི་ཆོས་འཆད་པར་མོས་པ་རྣམས་བསམ་པ་བཞིན་དུ་གྲུབ་པར༌[^3033]སྟོན་ཏེ༌[^3034]འདི་ནི་དང་པོའོ། །

[Block 3639 [HEADING]]
###### **ཆོས་བསྲུང་བ་རྣམས་ཡི་དམ་གྱི་མཐར་ཕྱིན་པ།** ^4-11-5-2-1-2-0

[Block 3640]
མདོ་ལས།

[Block 3641]
བརྩོན་པ་ཉན་པར་བྱ་བ་རྒྱལ་བའི་བུ། །ཞེས་པ་ནས། དེ་ཡིས༌[^3035]ས་འདི་མཛེས་ཤིང་རྣམ་པར་བཀྲ། །ཞེས་པའི་བར་དུ་ནི་ཆོས་བསྲུང༌[^3036]བར་མོས་པ་རྣམས་ཡི་དམ་གྱི་མཐར་ཕྱིན་པ་བསྟན་པའོ། །

[Block 3642 [HEADING]]
###### **ཆོས་འཆད་པར་མོས་པ་རྣམས་བསམ་པ་བཞིན་དུ་གྲུབ་པ།** ^4-11-5-2-1-3-0

[Block 3643]
མདོ་ལས།

[Block 3644]
དེ་དག་ལ་ཡང་མཆོད་པ་རྒྱ་ཆེ་མཐའ་ཡས་པ། །ཞེས་པ་ནས། སྤྲོ་བ་བྱེད་པ་འདྲེན་པས་སོ། །ཞེས་པའི་བར་དུ་ནི་ཆོས་འཆད་པར་མོས་པ་རྣམས་དེ་བཞིན་གཤེགས་པ་མཐོང་བར་སྟོན༌[^3037]པའོ། །

[Block 3645 [HEADING]]
###### ཀློག་པ་དང་འདོན་པ་དང་འཛིན་པ་ལ་སོགས་པའི་ཁྱད་པར། ^4-11-5-2-2-0
--- END BLOCKS ---
