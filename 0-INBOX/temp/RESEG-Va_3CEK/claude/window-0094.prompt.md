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
[Block 3291]
དེ་ལ། བསམ་གཏན་དག་གི་ལམ་རྣམས་སླ། །བསམ་གཏན་བཞིའི་ལམ་ནི༌[^2287]སླ་བ་ཡིན་ཏེ། ཡན་ལག་གིས་ཡོངས་སུ་ཟིན་པ་དང་། ཞི་གནས་དང་ལྷག་མཐོང་མཉམ་པ་དག་གིས་འབད་མི་དགོས་པར་རང་གི༌[^2288]ངང་གིས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3292]
ས་གཞན་དག་གི་དཀའ་བ་ཡིན། །མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། གཟུགས་མེད་པ་རྣམས་ཀྱི་ལམ་ནི། ཡན་ལག་གིས་ཡོངས་སུ་མ་ཟིན་པའི་ཕྱིར་དང་། ཞི་གནས་དང་ལྷག་མཐོང་ཆུང་བའི་ཕྱིར་ལམ་དཀའ་བ་ཡིན་ཏེ། མི་ལྕོགས་པ་མེད་པ་དང་བསམ་གཏན་ཁྱད་པར་ཅན་ན༌[^2289]ནི་ཞི་གནས་ཆུང་ངོ་། །གཟུགས་མེད་པ་དག༌[^2290]ན་ནི་ལྷག་མཐོང་ཆུང་ངོ་། །ལམ་དེ་ཡང་རྣམ་པ་གཉིས་ཏེ།

[Block 3293 [VERSE]]
བློ་རྟུལ་མངོན་ཤེས་བུལ་བ་སྟེ། །
ཅིག་ཤོས་ཀྱི་ནི་མངོན་ཤེས་མྱུར། །

[Block 3294]
དབང་པོ་རྟུལ་པོ་ནི་ལམ་སླ་བའམ་དཀའ་བ༌[^2291]ཡང་རུང་སྟེ། མངོན་པར་ཤེས་པ་བུལ་བ་ཡིན་ནོ། །

[Block 3295]
དབང་པོ་རྣོན་པོ་ནི་མངོན་པར་ཤེས་པ་མྱུར་བ་ཡིན་ནོ། །

[Block 3296]
ལམ་ཉིད༌[^2292]ལ་མངོན་པར་ཤེས་པ་བུལ་བ་ཡོད་པས་ན་འདི་ནི་མངོན་པར་ཤེས་པ་བུལ་བ་སྟེ། མངོན་པར་ཤེས་པ་མྱུར་བ་ཡང་དེ་དང་འདྲའོ། །

[Block 3297]
ཡང་ན་འདི་གང་ཟག་དབང་པོ༌[^2293]རྟུལ་པོའི་ཡིན་པས་མངོན་པར་ཤེས་པ་བུལ་བ་ཡིན་ལ། ཡིད་རྣོན་པོའི༌[^2294]ཡིན་པས་མངོན་པར་ཤེས་པ་མྱུར་བའོ། །

[Block 3298 [HEADING]]
#### བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ། ^3-2-17-0

[Block 3299]
ལམ་འདི་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་ཞེས་བྱ་བའི་མིང་འཐོབ་སྟེ། བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་སུམ་ཅུ་རྩ་བདུན་ནི་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་དང་། ཡང་དག་པར་སྤོང་བ་བཞི་དང་། རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་དང་། དབང་པོ་ལྔ་དང་། སྟོབས་ལྔ་དང་། བྱང་ཆུབ་ཀྱི་ཡན་ལག་བདུན་དང་། འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་དོ། །

[Block 3300 [HEADING]]
##### བྱང་ཆུབ་གསུམ། ^3-2-17-1-0

[Block 3301]
དེ་ལ་ཟད་དང་མི་སྐྱེ་ཤེས་པ་ནི། །བྱང་ཆུབ་ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་ན༌[^2295]གང་ཟག་གི་བྱེ་བྲག་གིས་ཉན་ཐོས་ཀྱི་བྱང་ཆུབ་དང་། རང་སངས་རྒྱས་ཀྱི་བྱང་ཆུབ་དང་། བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་དང་། བྱང་ཆུབ་གསུམ་ཞེས་བྱ་སྟེ། དེ་གཉིས་ཀྱིས་མ་རིག་པ་མ་ལུས་པར་སྤངས་པའི་ཕྱིར་དང་། རང་གི༌[^2296]དོན་བྱས་པ་དང་། ཡང་བྱར༌[^2297]མེད་པ་ཉིད་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ༌[^2298]རྟོགས་པའི་ཕྱིར་རོ། །

[Block 3302]
དེ་དང་མཐུན་ཉིད་ཕྱིར།

[Block 3303 [VERSE]]
སུམ་ཅུ་རྩ༌[^2299]བདུན་དེའི་ཕྱོགས་མཐུན། །
བྱང་ཆུབ་དང་མཐུན་པའི་ཕྱིར་རོ། །

[Block 3304]
མིང་གི་སྒོ་ནས། བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་སུམ་ཅུ་རྩ་བདུན་ཞེས་བྱའོ། །

[Block 3305 [HEADING]]
##### རྫས་སུ་བཅུ། ^3-2-17-2-0

[Block 3306]
རྫས་སུ་བཅུ། བྱང་ཆུབ་ཀྱི༌[^2300]ཕྱོགས་དང་མཐུན་པ་ཐམས་ཅད་ནི་རྫས་སུ་བཅུ་སྟེ། བཅུ་གང་ཞེ་ན།

[Block 3307 [VERSE]]
དད་དང་བརྩོན་འགྲུས་དྲན་པ་དང་། །
ཤེས་རབ་ཏིང་འཛིན་བཏང་སྙོམས་དགའ། །
རྟོག་དང་ཚུལ་ཁྲིམས་ཤིན་ཏུ་སྦྱངས། །

[Block 3308]
དེ་ལྟར་བྱས་ན་དེ་དག་ནི་རྫས་སུ་བཅུའོ། །ཇི་ལྟར་བྱས་པས་ཤེ་ན།

[Block 3309 [VERSE]]
དྲན་པ་ཉེར༌[^2301]གཞག་ཤེས་རབ་སྟེ། །
བརྩོན་འགྲུས་ཡང་དག་འཇོག་ཅེས་བྱ། །
རྫུ་འཕྲུལ་རྐང་པ་ཏིང་འཛིན༌[^2302]ཏོ། །

[Block 3310]
དྲན་པ་ཉེ་བར་གཞག་པ་དང་ཡང་དག་པར་རབ་ཏུ་འཇོག་པ་དང་། རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་ནི་ཤེས་རབ་དང་། བརྩོན་འགྲུས་དང་། ཏིང་ངེ་འཛིན་གྱི༌[^2303]རང་བཞིན་དག་ཡིན་ནོ། །

[Block 3311]
དེའི་ཕྱིར་རེ་ཞིག་དབང་པོ་དང་སྟོབས་རྣམས་ནི་མིང་གིས་སྨོས་པ་དད་པ་དང་བརྩོན་འགྲུས་དང་དྲན་པ་དང་ཏིང་ངེ་འཛིན་དང་ཤེས་རབ་ཀྱི་རྫས་ལྔ་ཡིན་ཏེ། དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་དང་། ཆོས་རྣམ་པར་འབྱེད་པ༌[^2304]ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། ཡང་དག་པའི་ལྟ་བ་ནི་ཤེས་རབ་ཁོ་ན་ཡིན་ནོ། །

[Block 3312]
ཡང་དག་པར་རབ་ཏུ་འཇོག་པ་རྣམས་དང་། བརྩོན་འགྲུས་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། ཡང་དག་པའི་རྩོལ་བ་ནི་བརྩོན་འགྲུས་ཁོ་ན་ཡིན་ནོ། །

[Block 3313]
རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་དང་། ཏིང་ངེ་འཛིན་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། ཡང་དག་པའི་ཏིང་ངེ་འཛིན་ནི་ཏིང་ངེ་འཛིན་ཁོ་ན་ཡིན་ནོ། །

[Block 3314]
དྲན་པ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། ཡང་དག་པའི་དྲན་པ་ནི་དྲན་པ་ཁོ་ན་ཡིན་ནོ། །ཅི་ཞིག་ལུས་ཤེ་ན། དགའ་བ་དང་། ཤིན་ཏུ་སྦྱངས་པ་དང་། བཏང་སྙོམས་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། ཡང་དག་པའི་རྟོག་པ་དང་། ཚུལ་ཁྲིམས་ཀྱི་ཡན་ལག་རྣམས་དང་རྫས་དེ༌[^2305]ལྔ་སྟེ། དེ་ལྟར་ན་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་དེ་དག་ནི་རྫས་བཅུ་ཡིན་ནོ། །

[Block 3315]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ཀྱི་ལྟར་ན་ལུས་དང་ངག་གི་ལས་དག་ཐ་དད་ཅིང་རིགས་མི་མཐུན༌[^2306]པའི་ཕྱིར་ཚུལ་ཁྲིམས་ཀྱི་ཡན་ལག་རྣམས་རྫས་གཉིས་ཡིན་པས་རྫས་བཅུ་གཅིག་ཡིན་ནོ། །

[Block 3316]
འདི་སྐད་དུ་དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པ་ནི་ཤེས་རབ་དང་བརྩོན་འགྲུས་དང་། ཏིང་འཛིན༌[^2307]གྱི་རང་བཞིན་དག་ཡིན་ནོ་ཞེས་བཤད་པ་གང་ཡིན་པ་དེར་ནི། གཙོ་བོ་སྨོས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3317]
[^2308]དེ་དག་ནི། སྦྱོར་བྱུང་ཡོན་ཏན་ཀུན་ཀྱང་ཡིན། །གཙོ་བོ་སྨོས་པས་དེ་སྐད་བཤད་ཀྱི། དྲན་པ་ཉེ་བར་གཞག་པ་དང་། ཡང་དག་པར་རབ་ཏུ་འཇོག་པ་དང་། རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་ནི་སྦྱོར་བ་ལས་བྱུང་བའི་ཡོན་ཏན་ཐམས་ཅད་ཀྱང་ཡིན་ནོ། །

[Block 3318]
ཅིའི་ཕྱིར་བརྩོན་འགྲུས་ལ་ཡང་དག་པར་རབ་ཏུ་འཇོག་པ་ཞེས་བཤད་ཅེ་ན། དེས་ལུས་དང་ངག་དང་ཡིད་ཡང་དག་པར་འཇོག་པས་སོ། །

[Block 3319]
ཅིའི་ཕྱིར་ཏིང་ངེ་འཛིན་ལ་རྫུ་འཕྲུལ་གྱི་རྐང་པ་ཞེས་བཤད་ཅེ་ན། དེ་ནི་ཡོན་ཏན་ཐམས་ཅད་སྦྱོར་བའི་རྟེན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3320]
གང་དག་རྫུ་འཕྲུལ་ནི་ཏིང་ངེ་འཛིན་ཁོ་ན་ཡིན་ལ། འདུན་པ་ལ་སོགས་པ་ནི་རྐང་པ་ཡིན་ནོ་ཞེས་ཟེར་བ་དེ་དག་གི་ལྟར་ན་ནི༌[^2309]འདུན་པ་དང་སེམས་དག་ལྷག་པའི་ཕྱིར་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་རྫས༌[^2310]བཅུ་གསུམ་དུ་འགྱུར༌[^2311]ལ། དགེ་སློང་དག་རྫུ་འཕྲུལ་ཡང་བཤད་ལ་རྫུ་འཕྲུལ་གྱི༌[^2312]རྐང་པ་རྣམས་ཀྱང་བཤད་དོ་ཞེས་བྱ་བ་ནས། རྫུ་འཕྲུལ་གང་ཞེ་ན། འདི་ན་དགེ་སློང༌[^2313]རྫུ་འཕྲུལ་གྱི་ཡུལ་རྣམ་པ་དུ་མ་ཉམས་སུ་མྱོང་བར་བྱེད་ཅིང་། གཅིག་ཏུ་གྱུར་ནས་མང་པོར་འགྱུར་ཞེས་བྱ་བའི་བར་རྒྱས་པར་གསུངས་པའི་མདོ་དང་ཡང་འགལ་ལོ། །

[Block 3321]
ཅིའི་ཕྱིར་དབང་པོ་རྣམས་ཁོ་ན་ཡང་སྟོབས་རྣམས་སུ་བཤད་ཅེ་ན། ཆུང་ངུ་དང་ཆེན་པོའི་བྱེ་བྲག་གིས༌[^2314]རྫི་བ་དང་རྫི་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 3322]
དབང་པོ་རྣམས་ཀྱི་གོ་རིམས་ཅིས་བྱས་ཤེ་ན། དད་པར་གྱུར་པ་ནི༌[^2315]འབྲས་བུའི་དོན་དུ་བརྩོན་འགྲུས་རྩོམ་པར་བྱེད་དོ། །

[Block 3323]
བརྩོན་འགྲུས་བརྩམས༌[^2316]ན་དྲན་པ་ཉེ་བར་གནས་པར་འགྱུར་རོ། །

[Block 3324]
དྲན་པ་ཉེ་བར་གནས་ན་རྣམ་པར་མི་གཡེང་བའི་ཕྱིར་སེམས་མཉམ་པར་འཇོག་གོ། །

[Block 3325]
སེམས་མཉམ་པར་གཞག་ན་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན༌[^2317]རབ་ཏུ་ཤེས་པར་འགྱུར་རོ། །

[Block 3326 [HEADING]]
##### གནས་སྐབས་གང་དུ་རབ་ཏུ་འབྱེད་པ། ^3-2-17-3-0

[Block 3327]
གནས་སྐབས་གང་དུ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་གང་ཞིག་རབ་ཏུ་འབྱེད་ཅེ་ན་བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ།

[Block 3328 [VERSE]]
སྡེ་ཚན་བདུན་ནི་གོ་རིགས་བཞིན། །
ལས་ནི་དང་པོ་པ་དག་དང་། །
ངེས་འབྱེད་ཆ་མཐུན་རྣམས་དང་ནི། །
བསྒོམ་དང་མཐོང་ལ་རབ་ཏུ་ཕྱེ། །

[Block 3329]
ལས་དང་པོ་པའི་གནས་སྐབས་སུ་ནི་ལུས་ལ་སོགས་པ་ལ་ཉེ་བར་བརྟག་པའི༌[^2318]ཕྱིར་དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་སོ། །

[Block 3330]
ཁྱད་པར་ཐོབ་པས༌[^2319]བརྩོན་འགྲུས་ཡང་དག་པར་སྤེལ་བའི་ཕྱིར་དྲོ་བར་གྱུར་པ་དག་ལ་ནི་ཡང་དག་པར་རབ་ཏུ་འཇོག་པ༌[^2320]རྣམས་སོ། །
--- END BLOCKS ---
