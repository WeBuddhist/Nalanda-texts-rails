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
[Block 3361]
གཉིས་ན་དེ་གཉིས་མ་གཏོགས་པ། བསམ་གཏན་གསུམ་པ་དང་བཞི་པ་དག་ན་ནི་དགའ་བ་དང་རྟོག་པ་དག་མ་གཏོགས་པ་སུམ་ཅུ་རྩ་ལྔ་ཡོད་དོ། །

[Block 3362]
བསམ་གཏན་བར་ནའང་། དེ་གཉིས་ཉིད་མ་གཏོགས་པ་སུམ་ཅུ་རྩ་ལྔ་ཁོ་ན་ཡོད་དོ། །

[Block 3363]
གཟུགས་མེད་པ། གསུམ་ནའང་དེ་དང་མཚུངས་ཡན་ལག །མ་གཏོགས་ཞེས་བྱ་བར་སྦྱར་ཏེ། གཟུགས་མེད་པ་དག་ན་ནི་ཡང་དག་པའི་ངག་དང་། ལས་ཀྱི་མཐའ་དང་། འཚོ་བ་རྣམས་དང་། དགའ་བ་དང་། རྟོག་པ་དག་མ་གཏོགས་པ་སུམ་ཅུ་རྩ་གཉིས་ཡོད་དོ། །

[Block 3364 [VERSE]]
བྱང་ཆུབ་དང་ནི་ལམ་ཡན་ལག །
མ་གཏོགས་འདོད་ཁམས་སྲིད་རྩེ་ན། །

[Block 3365]
དེ་གཉིས་ནི༌[^2347]ཟག་པ་མེད་པའི་ལམ་མེད་པའི་ཕྱིར་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་ཉི་ཤུ་རྩ་གཉིས་ཡོད་དོ། །

[Block 3366 [HEADING]]
#### ཤེས་ནས་དད་པ། ^3-2-18-0

[Block 3367]
བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་རྣམས་ལ་གནས་པ་གནས་སྐབས་གང་དུ་ཤེས་ནས་དད་པ་འཐོབ་པར༌[^2348]རིག་པར་བྱ་ཞེ་ན།

[Block 3368 [VERSE]]
བདེན་གསུམ་མཐོང་ན་ཚུལ་ཁྲིམས་དང་། །
ཆོས་ལ་ཤེས་ནས་དད་པ་འཐོབ། །
ལམ་མངོན་རྟོགས༌[^2349]ན་སངས་རྒྱས་དང་། །
དེ་ཡི་དགེ་འདུན་དག་ལ་ཡང་། །

[Block 3369]
སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ་དང་འགོག་པའི་བདེན་པ་རྣམས་མངོན་པར་རྟོགས༌[^2350]ན་ཆོས་ལ་ཤེས་ནས་དད་པ་དང་། འཕགས་པ་དགྱེས་པའི་ཚུལ་ཁྲིམས་རྣམས་འཐོབ་བོ། །

[Block 3370]
ལམ་གྱི་བདེན་པ་མངོན་པར་རྟོགས༌[^2351]ན་སངས་རྒྱས་དང་། དེའི་ཉན་ཐོས་ཀྱི་དགེ་འདུན་ལ་ཤེས་ནས་དད་པ་འཐོབ་སྟེ། གང་ཞིག་དེ་གཉིས་ལ་དད་པ་དེ་ནི་སངས་རྒྱས་སུ་བྱེད་པའི་ཆོས་མི་སློབ་པ་རྣམས་དང་། དགེ་འདུན་དུ་བྱེད་པའི་ཆོས་སློབ་པ་དང་། མི་སློབ་པ་རྣམས་ལ་དད་པ་ཡིན་ནོ། །

[Block 3371]
ཡང་ཞེས་བྱ་བའི་སྒྲས་ནི་ཚུལ་ཁྲིམས་དང་ཆོས་ལ་ཤེས་ནས་དད་པ་དག་ཀྱང་འཐོབ་པར་སྟོན་ཏོ། །

[Block 3372]
འདིར་གང་ལ་ཆོས་སུ་དགོངས་པ་ཡིན་ཞེ་ན།

[Block 3373 [VERSE]]
ཆོས་བདེན་གསུམ་དང་རང་སངས་རྒྱས། །
བྱང་ཆུབ་སེམས་དཔའི་ལམ་ཡིན་ནོ། །

[Block 3374]
དེའི་ཕྱིར་བདེན་པ་བཞི་ཆར་ཡང་མངོན་པར་རྟོགས་ན་ཆོས་ལ་ཤེས་ནས་དད་པ་འཐོབ༌[^2352]པོ། །དེ་དག་ནི་དད་པའི་གཞིའི༌[^2353]བྱེ་བྲག་ལས་མིང་གི་སྒོ་ནས་ཤེས་ནས༌[^2354]དད་པ་བཞི་ཞེས་བྱ་བའོ། །

[Block 3375]
རྫས་སུ་གཉིས་ཏེ་དད་པ་དང་། ཚུལ་ཁྲིམས། སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན་ལ་ཤེས་ནས་དད་པ་རྣམས་ནི་དད་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 3376]
འཕགས་པ་དགྱེས་པའི་ཚུལ་ཁྲིམས་རྣམས་ནི་ཚུལ་ཁྲིམས་ཡིན་པས་རྫས་གཉིས་སོ། །

[Block 3377]
ཅི་འདི་དག་ཟག་པ་དང་བཅས་པ་དག་ཅིག༌[^2355]གམ་ཟག་པ་མེད་པ་དག་ཅིག་ཡིན་ཞེ་ན། ཤེས་ནས་དད་པ་རྣམས་ནི་གཅིག་ཏུ། དྲི་མ་མེད་པ་ཡིན། ཤེས་ནས་དད་པ་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། བདེན་པ་རྣམས་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་རྟོགས་ནས་ཡིད་ཆེས་པ་ནི་ཤེས་ནས་དད་པ༌[^2356]ཡིན་ནོ། །

[Block 3378]
འདི་དག་གི་རིམ་པ་ནི་ལངས་ནས་ཇི་ལྟར་མངོན་སུམ་དུ་བྱེད་པ་དེ་བཞིན་དུ་བཀོད་དོ། །

[Block 3379]
ལངས་ནས་ཇི་ལྟར་མངོན་སུམ༌[^2357]བྱེད་ཅེ་ན། ཀྱེ་མ་བཅོམ་ལྡན་འདས་ནི་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཡིན་ནོ། །

[Block 3380]
དེའི་ཆོས་འདུལ་བ་ནི་ལེགས་པར་གསུངས་པ་ཡིན་ནོ། །

[Block 3381]
དེའི་ཉན་ཐོས་ཀྱི་དགེ་འདུན་ནི་ལེགས་པར་ཞུགས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་མངོན་སུམ་དུ་བྱེད་དེ། སྨན་པ་དང་སྨན་དང་ནད་གཡོག་ལྟ་བུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3382]
སེམས་རབ་ཏུ་དང་བས་བྱས་པའི༌[^2358]ཚུལ་ཁྲིམས་ཀྱང་རབ་ཏུ་དང་བ་ཡིན་པས་ཐ་མར་བཞི་པ་བཤད་དེ། འདི་ནི་དེ་ལྟར་རབ་ཏུ་དང་བར་གྱུར་པའི་སྒྲུབ༌[^2359]པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3383]
ཡང་ན་ནད་མེད་པ་ལྟ་བུར་གྱུར་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3384]
ཡང་ན་སྟོན་པར་བྱེད་པ་དང་། ལམ་དང་། ལམ་གྲོགས་དང་། བཞོན་པ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3385 [HEADING]]
#### སློབ་པ་དང་མི་སློབ་པའི་ཡན་ལག། ^3-2-19-0

[Block 3386]
མདོ་ལས་སློབ་པ་ནི་ཡན་ལག་བརྒྱད་དང་ལྡན་ནོ། །

[Block 3387]
མི་སློབ་པ་ནི་ཡན་ལག་བཅུ་དང་ལྡན་ནོ་ཞེས་གསུངས་པ། ཅིའི་ཕྱིར་སློབ་པ་ལ་ཡང་དག་པའི་རྣམ་པར་གྲོལ་བ་དང་། ཡང་དག་པའི་ཤེས་པ་མ༌[^2360]བཤད་ཅེ་ན། བཅིངས་ཕྱིར་སློབ་པའི་ཡན་ལག་ཏུ། །རྣམ་གྲོལ་མ་བཤད། སློབ་པ་ནི་ད་དུང་ཉོན་མོངས་པའི་འཆིང་བ་རྣམས་ཀྱིས༌[^2361]བཅིངས་པ་ཡིན་པས་བཅིངས་བཞིན་དུ་ཇི་ལྟར་རྣམ་པར་གྲོལ་བར་རྣམ་པར་གཞག༌[^2362]སྟེ་འཆིང་བའི་ཕྱོགས་གཅིག་ལས་གྲོལ་བས༌[^2363]ནི་གྲོལ༌[^2364]ཞེས་མི་བྱའོ། །

[Block 3388]
རྣམ་པར་གྲོལ་བ་མེད་པར༌[^2365]ཡང་ཇི་ལྟར་རྣམ་པར་གྲོལ་བའི་ཤེས་པ་རྣམ༌[^2366]པར་གཞག །མི་སློབ་པ་ནི་ཉོན་མོངས་པའི་འཆིང་བ་ཐམས་ཅད་ལས་གཏན་དུ་ངེས་པར་ཐར་པའི་ཕྱིར་རྣམ་པར་གྲོལ་བ་དང་། དེ་སོ་སོ་རང་གི༌[^2367]ཤེས་པ་དག་གིས་རབ་ཏུ་ཕྱེ་བ་ཡིན་པས་དེ་ཁོ་ན་ལ་དེ་སྨོས་པ་རིག་པ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 3389 [HEADING]]
##### ཡང་དག་པའི་རྣམ་པར་གྲོལ་བ། ^3-2-19-1-0

[Block 3390]
རྣམ་པར་གྲོལ༌[^2368]ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན། དེ་རྣམ་གཉིས། འདུས་བྱས་དང་འདུས་མ་བྱས་སོ། །

[Block 3391]
དེ་ལ། ཉོན་མོངས་བཅོམ་པ་འདུས་མ་བྱས། །མོས་པ་འདུས་བྱས་ཉོན་མོངས་པ་སྤངས་པ་ནི་རྣམ་པར་གྲོལ་བ་འདུས་མ་བྱས་ཡིན་ནོ། །

[Block 3392]
མི་སློབ་པའི་མོས་པ་ནི་རྣམ་པར་གྲོལ་བ་འདུས་བྱས་ཡིན་ནོ། །

[Block 3393]
ཡན་ལག་ནི་དེ་ཡིན། རྣམ་པར་གྲོལ་བ་འདུས་བྱས་དེ་ནི་མི་སློབ་པའི་ཡན་ལག་ཏུ་བཤད་དེ།[^2369] ཡན་ལག་རྣམས་ནི་འདུས་བྱས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3394]
དེ་ཉིད་རྣམ་གྲོལ་གཉིས།

[Block 3395]
རྣམ་པར་གྲོལ་བ་འདུས་བྱས་དེ་ཉིད་མདོ་ལས།

[Block 3396]
སེམས་རྣམ་པར་གྲོལ་བ་དང་། ཤེས་རབ་རྣམ་པར་གྲོལ་བ་དང་། རྣམ་པར་གྲོལ་བ་གཉིས་སུ་གསུངས་ཏེ། དེ་ཉིད་རྣམ་པར་གྲོལ་བའི་ཕུང་པོ་ཡིན་པར་ཡང་བལྟའོ། །

[Block 3397]
གཞན་དག་ན་རེ་མདོ་ལས།

[Block 3398]
སྟག་གི་བྱང་ཆུབ་ཀྱི་བུ་དག་རྣམ་པར་གྲོལ་བ་ཡོངས་སུ་དག་པ་གཙོ་བོ་གང་ཡིན་ཞེ་ན། འདི་ན༌[^2370]དགེ་སློང་འདོད་ཆགས་ལས་སེམས་འདོད་ཆགས་དང་བྲལ་ཞིང་རྣམ་པར་གྲོལ་བ་ཡིན། ཞེ་སྡང་དང་གཏི་མུག་ལས་སེམས་འདོད་ཆགས་དང་བྲལ་ཞིང་རྣམ་པར་གྲོལ་བ་ཡིན་ཏེ། འདི་ལྟར་རྣམ་པར་གྲོལ་བའི་ཕུང་པོ་ཡོངས་སུ་མ་རྫོགས་པ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའམ། ཡོངས་སུ་རྫོགས་པ་རྗེས་སུ་འཛིན་པར་བྱེད་པ་འདུན་པ་དང་བརྩོན་འགྲུས་གང་ཡིན་པ་ཞེས་རྒྱས་པར་གང་གསུངས་པ་ཇི་ལྟ་བུ། དེའི་ཕྱིར་རྣམ་པར་གྲོལ་བ་ནི་མོས་པ་ཁོ་ན་ཡིན་པར་མ་ཟད་དོ། །

[Block 3399]
[^2371]འོ་ན་ཅི་ཞེ་ན། དེ་ཁོ་ན་ཤེས་པས་འདོད་ཆགས་ལ་སོགས་པ་སྤངས་ནས་སེམས་དྲི་མ་མེད་པ་ཉིད་རྣམ་པར་གྲོལ་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ།[^2372] །ཡང་དག་པའི་རྣམ་པར་གྲོལ་བ་བཤད་ཟིན་ཏོ། །

[Block 3400 [HEADING]]
##### ཡང་དག་པའི་ཤེས་པ། ^3-2-19-2-0
--- END BLOCKS ---
