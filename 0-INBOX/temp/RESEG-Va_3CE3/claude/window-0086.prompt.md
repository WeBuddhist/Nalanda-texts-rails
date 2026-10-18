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
[Block 3011 [HEADING]]
#### རྣམ་པར་བརྟགས་པའི་གཟུགས། ^2-2-2-0

[Block 3012]
དེའི་འོག་ཏུ་རྣམ་པ་གཉིས་ནི་འདུ་བྱེད་ཀྱི་མཚན་མའི་དངོས་པོ་དེ་རྣམ་པར་རྟོག་པ་ཙམ་གྱི་ཆོས་ཉིད་ལ་གནས་པའི་རྣམ་པར་རྟོག༌[^2225]པ་ལ་བརྟེན་ནས་མངོན་པར་བརྗོད་དེ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྟོན་ཏེ། བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱི་སེམས་ཉོན་མོངས་པ་དང་། ལས་དང༌[^2226]རྣམ་པར་སྨིན་པ་ལ་སོགས་པའི་རྒྱུ་དང་རྐྱེན་གྱིས་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པ་རྣམས་ལ་དངོས་པོའི་རྣམ་པར་བློ་སྐྱེ་ཞིང་སྣང་བ་ནི༌[^2227]རྣམ་པར་བརྟགས་པའི་གཟུགས་ཞེས་བྱའོ། །

[Block 3013]
འདུ་བྱེད་ཀྱི་མཚན་མའི་དངོས་པོ་དེ་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་སྟོན་ཏེ། རྣམ་པར་རྟོག་པ་ཙམ་གྱི་ཆོས་ཉིད༌[^2228]ལ་གནས་པ་ཞེས་བྱ་བ་ནི་བློས༌[^2229]རྣམ་པར་བརྟགས་པའི་རྣམ་པ་མ་གཏོགས༌[^2230]པར་ངོ་བོ་ཉིད་གཞན་མེད་དེ། དེ་བས་ན་དངོས་པོ་དེ་རྣམ་པར་བརྟགས་པ་ཙམ་གྱི་ངོ་བོ་ཉིད་ལ་གནས་ཏེ། དེ་ལ་གནས་པ་དེ་ཉིད་ལ་རྣམ་པར་རྟོག་པ་ཞེས་བྱའོ། །

[Block 3014]
དེ་ལྟར་བློས་རྣམ་པར་བརྟགས་པའི་རྣམ་པ་ཙམ་གྱི་ངོ་བོ་ཉིད་ལ་གནས་པ་རྣམ་པར་རྟོག་པ་དེ་ཉིད་ལ་བརྟེན་ཏེ་ཉེ་བར་བཟུང་ནས། གང་མངོན་པར་བརྗོད་པ་དང་འབྲེལ་པ་དངོས་པོའི་བདག་ཉིད་དུ་ཀུན་ཏུ་གཡེངས་པའི་རྣམ་པ་ལ་མངོན་པར་བརྗོད་པ་ཞེས་བྱ་སྟེ། དེ་ལྟར་བློས་རྣམ་པར་བརྟགས་པའི་རྣམ་པའི་ངོ་བོ་ཉིད་དུ་གནས་པ་ཞེས་བྱ་བའི་རྣམ་པ་ལ་བརྟེན་ནས་བློ་ལ་དངོས་པོའི་བདག་ཉིད་དུ་སྣང་བ་ནི་རྣམ་པར་བརྟགས་པའི་གཟུགས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3015]
དེ་བཞིན་དུ་ཚོར་བ་ལ་སོགས་པ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 3016 [HEADING]]
#### ཆོས་ཉིད་ཀྱི་གཟུགས། ^2-2-3-0

[Block 3017]
དེའི་འོག་ཏུ་ཆོས་ཉིད་ཀྱི་གཟུགས་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་བྱུང་ཡང་རུང་མ་བྱུང་ཡང་རུང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་བཞིན་གཤེགས་པ་རྣམས༌[^2231]བྱུང་ཡང་རུང་ཞེས་བྱ་བ༌[^2232]འདིས་ཆོས་ཉིད་དེ་ངོ་བོ་ཉིད་ཡིན་གྱི་མི་རྟག་པ་ནི་མ་ཡིན་ནོ་ཞེས་བསྟན་པ་དེ།[^2233] གང་ཀུན་བརྟགས་པའི་གཟུགས་དེས་རྣམ་པར་བརྟགས་པའི་གཟུགས་དེ༌[^2234]རྟག་པ་རྟག་པའི་དུས་དང་། ཐེར་ཟུག་ཐེར་ཟུག་གི་དུས་སུ་ངོ་བོ་ཉིད་མེད་པ་ཁོ་ན་ཞེས་བྱ་བ་དེ་ལ། ཆོས་ཉིད་ཀྱི་གཟུགས་ཞེས་བྱ་བ་ནི་གང་གི་ཚེ་རྣམ་པར་མི་རྟོག་པའི༌[^2235]བློ་ལ་སྣང་བའི་རྣམ་པ་དེ་ཉིད་སྔར་སྨོས་པའི་ཀུན་བརྟགས་པ་བརྗོད་པར་བྱ་བ་དང་། བརྗོད་པར༌[^2236]བྱེད་པའི་རྣམ་པས་འདུ་ཤེས་དང་། གདགས་པར་འོས་པའི་བདག་ཉིད་དང་བྲལ་བར་གྱུར་པ་དེའི་ཚེ། བདག་ཉིད་ཀྱི༌[^2237]བརྗོད་དུ་མེད་པ་རྣམ་པར་མི་རྟོག་པའི་བདག་ཉིད་དུ་གནས་པའི་རྣམ་པ་དེ་ལ་ཆོས་ཉིད་ཀྱི་གཟུགས་ཞེས་བྱའོ། །

[Block 3018]
ངོ་བོ་ཉིད་མེད་པ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པའི་ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 3019]
ཆོས་ལ་བདག་མེད་པ་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་བདག་ཉིད་ཀྱི་རྣམ་པ་མེད་པའོ། །

[Block 3020]
དེ་བཞིན་ཉིད་ཅེས་བྱ་བ་ནི་ཕྱིན་ཅི་མ་ལོག་པའི་རྣམ་པའོ། །

[Block 3021]
ཡང་དག་པའི་མཐའ་ཞེས་བྱ་བ་ནི་རྣམ་པ་དེ་ལྟ་བུའི་མཐར་ཐུག་པའོ། །

[Block 3022]
དེ་བཞིན་དུ་ཚོར་བ་ལ་སོགས་པ་ལ་ཡང༌[^2238]སྦྱར་བར་བྱའོ། །

[Block 3023]
བྱམས་པ་གང་ཀུན་བརྟགས་པའི་གཟུགས་ནི་རྫས་སུ་མེད་པར་བལྟ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་མེད་པའི་ཕྱིར་རོ། །

[Block 3024]
རྣམ་པར་བརྟགས་པའི་གཟུགས་གང་ཡིན་པ་དེ་ནི་རྣམ་པར་རྟོག་པ༌[^2239]རྫས་སུ་ཡོད་པའི་ཕྱིར་རྫས་སུ་ཡོད་པར་བལྟ་བར་བྱ་ཞེས་བྱ་བ་ནི་ཀུན་རྫོབ་ཏུ་ཡོད་པའི་ཕྱིར་དེ་ཡོད་པའོ། །

[Block 3025]
འདུས་བྱས་ཀྱི་ཚུལ་གྱི༌[^2240]འཇིག་པ་དང་། གཟུགས་སུ་ཡོད་པའི་ཕྱིར་རྫས་ཡིན་ཏེ། དེ་བས༌[^2241]རྣམ་པར་བརྟགས་པར་ཡོད་པ་ཉིད༌[^2242]དང་། རྫས་ཡིན་པའི་ཕྱིར་བཤད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3026]
རང་དབང་དུ་འཇུག་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དབང་གི༌[^2243]ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་དེ་སྐད་གསུངས་ཏེ། ཆོས་ཉིད་ཀྱི་གཟུགས་གང་ཡིན་པ་དེ་ནི་རྫས་སུ་མེད་པ་ཡང་མ་ཡིན་ལ། རྫས་སུ་ཡོད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 3027]
དོན་དམ་པས་རབ་ཏུ་བྱེ་བ༌[^2244]ཞེས་བྱ་བ་ནི་ཆོས་ཉིད༌[^2245]གཟུགས་སོ། །

[Block 3028]
དེ་བརྗོད་དུ་མེད་པའི་བདག་ཉིད་དུ་ཡོད་པའི་ཕྱིར་མེད་དོ་ཞེས་བརྗོད་དུ་མི་རུང་སྟེ། དེ་བས་ན་རྫས་སུ་མེད་པའང་མ་ཡིན་ནོ། །

[Block 3029]
རྣམ་པར་བརྟགས་པའི་དངོས་པོའི་རྣམ་པར་ཡོད་པའི་ཕྱིར་ཡོད་དོ་ཞེས་བརྗོད་དུ་ཡང་མི་རུང་སྟེ། དེ་བས་ན་རྫས་སུ་ཡོད་པ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་མཐའ་གཉིས་སྤངས་ནས་དབུ་མའི་ལམ་བསྟན་པ་ཡིན་ནོ། །

[Block 3030]
དོན་དམ་པས་རབ་ཏུ་ཕྱེ་བ་ཞེས་བྱ་བ་ནི་དོན་དམ་པའི་ངོ་བོ་ཉིད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3031]
རབ་ཏུ་ཕྱེ་ཞེས་བྱ་བའི་སྒྲ་ནི་ངོ་བོ་ཉིད་ཀྱི་དོན་ཏོ། །

[Block 3032]
དེ་བཞིན་དུ་སངས་རྒྱས་ཀྱི་ཆོས་ཀྱི་མཐའི་བར༌[^2246]ཡང་སྦྱར་བར་བྱའོ། །

[Block 3033 [HEADING]]
### གཉིས་སུ་མེད་པའི་མཚན་ཉིད། ^2-3-0

[Block 3034]
དེ་ལྟར་ངོ་བོ་ཉིད་གསུམ་གྱི་དབང་གིས་མཚན་ཉིད་གསུམ་སྨོས་ནས། ཡང་གཉིས་སུ་མེད་པའི་མཚན་ཉིད་བསྟན་པའི་སྐབས་དབྱེ་བའི་ཕྱིར་འཕགས་པ་བྱམས་པས་གསོལ་པ། སྔར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མདོར་བསྡུས་པ་གཏན་ལ་ཕབ་པའི་སྐབས་སུ་ཞུ་བ་རྣམ་པ་ཉི་ཤུ་རྩ་བརྒྱད་བསྟན་པ་འདི་ལྟ་སྟེ། གཟུགས་ཞེས་བྱ་བ་འདི༌[^2247]ནི་གཉིས་སུ་མེད་པའི་གྲངས་སུ་བྱས་པའོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2248]བཀའ་སྩལ་པ་དེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསོལ་ཏོ། །

[Block 3035 [HEADING]]
#### གཟུགས་དང་གཟུགས་མ་ཡིན་པ་ལས་རྣམ་པར་གྲོལ་བའི་མཚན་ཉིད། ^2-3-1-0

[Block 3036 [HEADING]]
##### ཀུན་བརྟགས་པའི་གཟུགས། ^2-3-1-1-0

[Block 3037]
བྱམས་པ་དེ་ཇི་སྙམ་དུ་སེམས་ཀུན་བརྟགས་པའི་གཟུགས་ལ་རྫས་སུ་མེད་པ་ཉིད་གང་ཡིན་པ་དེ། གཟུགས་ཡིན་ནམ་འོན་ཏེ་མ་ཡིན་ཞེས་བྱ་བ་ལ་སོགས་པས་ཇི་སྐད་བསྟན་པ་ཡིན་ཞེ་ན། ཀུན་བརྟགས་པ་དང་། རྣམ་པར་བརྟགས་པ་དང་། ཆོས་ཉིད་ཀྱི་གཟུགས་འདི་གསུམ་ལ་སོ༌[^2249]སོར་གཟུགས་སམ་གཟུགས་མ་ཡིན་ཞེས་བྱ་བ་མེད་པ་དེ༌[^2250]གཉིས་སུ་མེད་པ་དང་། དེ་བཞིན་ཉིད་དང་། ཆོས་ལ་བདག་མེད་པའོ། །

[Block 3038]
དེ་བས་ན་གཟུགས་དང་། ཚོར་བ་ལ་སོགས་པའི་སྒྲས། དེ་བཞིན་ཉིད་གཉིས་སུ་མེད་པའི་གྲངས་སུ་བགྲང་བར༌[^2251]བྱས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། དེ་ཉིད་བསྟན་པར་བཞེད་ནས། གཟུགས་རྣམ་པ་གསུམ་པོ་དེ༌[^2252]དག་རེ་རེ་ལ་ཡང་། གཟུགས་དང་གཟུགས་མ་ཡིན་པ་ལས་རྣམ་པར་གྲོལ་བའི་མཚན་ཉིད་བསྟན་པའི་ཕྱིར་དང་པོར་ཀུན་བརྟགས་པའི་གཟུགས་ལ་བརྩམས་ནས། ཀུན་བརྟགས་པའི་གཟུགས་ལ་རྫས་སུ་མེད་པ་ཉིད་གང་ཡིན་པ་དེ་གཟུགས་ཡིན་ནམ་འོན་ཏེ་མ་ཡིན་ཞེས་བྱ་བ་གསུངས་ཏེ། ཀུན་བརྟགས་པའི་གཟུགས༌[^2253]ནི༌[^2254]གཟུགས་ཀྱི་བདག་ཉིད་དུ་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་དོ་ཞེས་བརྗོད་དུ་མི་རུང་ངོ་། །གཟུགས་ཀྱི་མིང་དང་གཟུགས་སུ་གདགས་པ་དག་དེ་ལ་ཡོད་པའི་ཕྱིར་གཟུགས་ཀྱི་བདག་ཉིད་མ་ཡིན་ནོ་ཞེས་ཀྱང་བརྗོད་དུ་མི་རུང་ངོ་། །

[Block 3039]
དེ་བས་ན་དེ་ལ་གཟུགས་ཞེས་བྱ་བ་མིང་དང་འདུ་ཤེས་དང་། བཏགས་པ་དང་ཐ་སྙད་ཙམ་ཉིད་ཅེས་བྱ་བར་གསུངས་སོ། །

[Block 3040]
ཇི་ག་དེ་ནི་གཟུགས་ཡིན་ནམ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་གཟུགས་སུ་བཏགས་པའི་དབང་གིས་གཟུགས་མེད་པ་ཡང་མ་ཡིན་ལ། གཟུགས་ཀྱི་ངོ་བོ་ཉིད་མེད་པའི་ཕྱིར་གཟུགས་ཀྱང་མ་ཡིན་པས།[^2255] གཉིས་སུ་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3041 [HEADING]]
##### རྣམ་པར་བརྟགས་པའི་གཟུགས། ^2-3-1-2-0

[Block 3042]
བྱམས་པ་དེ་ཇི་སྙམ་དུ་སེམས་རྣམ་པར་བརྟགས་པའི་གཟུགས་རྫས་སུ་ཡོད་པ་ཉིད་གང་ཡིན་པ་དེ་ཇི་ག་གཟུགས་མ་ཡིན་པ་ཡིན་ནམ་ཞེས་བྱ་བ་ནི་རྣམ་པར་བརྟགས་པའི་དེའི་གཟུགས་དེ་ཡང་གཟུགས་ཀྱི་བདག་ཉིད་དུ་སྣང་བའི་ཕྱིར་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་མེད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 3043]
དོན་དམ་པར་གཟུགས་ཀྱི༌[^2256]འདུ་ཤེས་དང་བྲལ་བའི་ངོ་བོ་ཉིད་ཡིན་པའི༌[^2257]ཕྱིར་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་ཀྱང་མ་ཡིན་ནོ། །

[Block 3044]
དེ་བས་ན་རྣམ་པར་བརྟགས་པའི་གཟུགས་དེ་ཉིད་ལ་ཀུན་བརྟགས་པའི་གཟུགས་དེས་དེའི་ངོ་བོ་ཉིད་མ༌[^2258]ཡིན་ཞིང་དེའི་མཚན་ཉིད་མ་ཡིན་པ་གང་ཡིན་པ་དེ་གཟུགས་ཡིན་ནམ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 3045]
དེ་ལྟར་རྣམ་པར་བརྟགས་པའི་གཟུགས་དེ་གཟུགས་སུ་འདུ་ཤེས་སུ་རུང་བའི་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་དུ་སྣང་བས་གཟུགས་མེད་པ་ཡང་མ་ཡིན་ལ། དོན་དམ་པར་གཟུགས་ཀྱི་མཚན་ཉིད་མེད་པའི་ཕྱིར་གཟུགས་ཀྱང་མ་ཡིན་པས་གཉིས་སུ་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3046 [HEADING]]
##### ཆོས་ཉིད་ཀྱི་གཟུགས། ^2-3-1-3-0

[Block 3047]
གང་ཆོས་ཉིད་ཀྱི་གཟུགས་བདག་མེད་པས་རབ་ཏུ་ཕྱེ་བ་དེ་ཇི་ག་གཟུགས་ཡིན་ནམ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གྲུབ་པ་ཆོས་ཉིད་ཀྱི༌[^2259]གཟུགས་དེ་མཚན་མ་ཐམས་ཅད་དང་བྲལ་བའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་གཟུགས་ཀྱི་ངོ་བོ་ཉིད་ཀྱང་མ་ཡིན་ནོ། །

[Block 3048]
གཟུགས་ཀྱི་ཆོས་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་གཟུགས་མ་ཡིན་པ་ཡང་མ་ཡིན་ཏེ། དེ་བས་ན་ཆོས་ཉིད་ཀྱི་གཟུགས་དེ༌[^2260]ཉིད་ཀྱི་གཟུགས་ཀྱི་ཆོས་ཉིད་གང་ཡིན་པ་དེ་གཟུགས་མ་ཡིན་པ་ཡིན་ནམ་ཞེས་བྱ་བ་གསུངས་ཏེ། ཆོས་ཉིད་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་གཟུགས་ཀྱང་མ་ཡིན་གཟུགས་ཀྱི་ཆོས་ཉིད་ཡིན་པའི་ཕྱིར་གཟུགས་མ་ཡིན་པ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་ནི་གཉིས་སུ་མེད་པའི་དོན་ཏོ། །

[Block 3049]
དེ་བས་ན་དེ་ནི་གཉིས་སུ་མེད་པའི་གྲངས་སུ་བྱས་པའོ་ཞེས་བྱ་བ་ནི། དེ་བཞིན་ཉིད་ཀྱི་གྲངས་སུ་བྱས་སོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3050]
[^2261]དེ་བཞིན་དུ་སངས་རྒྱས་ཀྱི་ཆོས་ཀྱི་མཐར་ཐུག་གི་བར་དུ་གཉིས་སུ་མེད་པར་སྦྱར་བར༌[^2262]བྱའོ། །
--- END BLOCKS ---
