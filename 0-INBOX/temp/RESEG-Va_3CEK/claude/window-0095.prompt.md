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

[Block 3331]
ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་བའི་དགེ་བའི་རྩ་བ་ལ་འཇུག་པའི་ཕྱིར་རྩེ་མོ་དག་ནི་རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་སོ། །

[Block 3332]
ཡང་ཡོངས་སུ་ཉམས་པར་མི་འགྱུར་བའི་སྒོ་ནས་དབང་པོ༌[^2321]ཐོབ་པའི་ཕྱིར༌[^2322]བཟོད་པ་དག་ལ་ནི་དབང་པོ་རྣམས་སོ། །

[Block 3333]
ཉོན་མོངས་པ་རྣམས་ཀྱིས་མི་བརྫི་བའི༌[^2323]ཕྱིར་རམ། འཇིག་རྟེན་པའི་ཆོས་ཅན༌[^2324]གཞན་དག་གིས་མི་བརྫི་བའི༌[^2325]ཕྱིར་ཆོས་ཀྱི་མཆོག་དག་ལ་ནི་སྟོབས་རྣམས་སོ། །

[Block 3334]
བྱང་ཆུབ་དང་ཉེ་བའི་ཕྱིར་བསྒོམ་པའི་ལམ་དག་ལ་ནི་བྱང་ཆུབ་ཀྱི་ཡན་ལག་རྣམས་སོ། །

[Block 3335]
འགྲོ་བས་རབ་ཏུ་ཕྱེ་བའི་ཕྱིར་མཐོང་བའི་ལམ་ལ་ནི་ལམ་གྱི་ཡན་ལག་རྣམས་ཏེ། དེ་ནི་མྱུར་བར་འགྲོ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3336]
གྲངས་ཀྱི་རིམ༌[^2326]པ་བཞིན་དུ་བྱ་བའི་ཕྱིར་སྔར་བདུན་བཤད་ལ་ཕྱིས་བརྒྱད་བཤད་དོ། །

[Block 3337]
དེ་ལ་ཆོས་རྣམ་པར་འབྱེད་པ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ནི་བྱང་ཆུབ་ཀྱང༌[^2327]ཡིན་ལ་བྱང་ཆུབ་ཀྱི་ཡན་ལག་ཀྱང་ཡིན་ནོ། །

[Block 3338]
ཡང་དག་པའི་ལྟ་བ་ནི་ལམ་ཡང་ཡིན་ལ་ལམ་གྱི་ཡན་ལག་ཀྱང་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3339]
གཞན་དག་ནི་གོ་རིམས་མ་ཉམས་པ་ཁོ་ནར་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་རྣམས་གོ་རིམས་བཞིན་དུ་བརྗོད་དོ། །

[Block 3340]
རེ་ཞིག་དང་པོ་ཁོ་ནར་ཡུལ་རྣམ་པ་མང་པོ་ལ་གཡེང་བར་འཕྲོ༌[^2328]བའི་བློ་རྣམས་ཚར་བཅད་པའི་ཕྱིར་དྲན་པ་ཉེ་བར་གཞག་པ་རྣམས་སོ། །

[Block 3341]
དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་པོ་འདི་དག་ནི་དེའི་སེམས་ཀྱི་ཉེ་བར་འདོགས་པ་ཡིན་ཏེ། མདོ་ལས་འདི་ལྟ་སྟེ། ཞེན་པ་ལ་བརྟེན་པའི་དྲན་པའི་ཀུན་དུ་རྟོག་པ་རྣམས་བསལ་བར༌[^2329]བྱ་བའི་ཕྱིར་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3342]
དེའི་སྟོབས་ཀྱིས༌[^2330]བརྩོན་འགྲུས་ཡང་དག་པར་འཕེལ་བས་དགོས་པ༌[^2331]རྣམ་པ་བཞི་བསྒྲུབ་པའི་ཕྱིར་སེམས་ཡང་དག་པར་རབ་ཏུ་འཇོག་པས་ན་ཡང་དག་པར་རབ་ཏུ་འཇོག་པ་རྣམས་སོ། །

[Block 3343]
དེའི་འོག་ཏུ་ཏིང་ངེ་འཛིན་རྣམ་པར་སྦྱོང་བའི་ཕྱིར༌[^2332]རྫུ་འཕྲུལ་གྱི་རྐང་པ་རྣམས་སོ། །

[Block 3344]
ཏིང་ངེ་འཛིན་ལ་ཡང་དག་པར་བརྟེན་ནས་འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་རྣམས་ཀྱི་བདག་པོར་འགྱུར་བའི༌[^2333]ཕྱིར་དད་པ་ལ་སོགས་པ་ནི་དབང་པོ་རྣམས་སོ། །

[Block 3345]
དེ་དག་ཉིད་མི་མཐུན་པའི་ཕྱོགས་ཀུན་ཏུ་སྤྱོད་པ་ལས་ངེས་པར་རྒྱལ་བ་ནི་སྟོབས་རྣམས༌[^2334]སོ། །

[Block 3346]
མཐོང་བའི་ལམ་ལ་ནི་བྱང་ཆུབ་ཀྱི་ཡན་ལག་རྣམས་ཏེ།

[Block 3347]
དང་པོ་ཉིད་དུ་ཆོས་ཀྱི་དེ་ཁོ་ན་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 3348]
གཉི་ག་ལ་ནི་ལམ་གྱི་ཡན་ལག་རྣམས་ཏེ། འདི་ལྟར་འཕགས་པའི་ལམ་ཡན་ལག༌[^2335]

[Block 3349]
བརྒྱད་པ་བསྒོམ་པ་ཡོངས་སུ་རྫོགས་པར་གྱུར༌[^2336]ན། དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་བསྒོམ་པ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་བ་རྣམས༌[^2337]བྱང་ཆུབ་ཀྱི་ཡན་ལག་བདུན་གྱི་བར་དུ་བསྒོམ་པ༌[^2338]ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 3350]
ཡང་དགེ་སློང་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་གྱི་ཚིག་བརྗོད་པ་ཞེས་བྱ་བ་འདི་ནི་འཕགས་པའི་བདེན་པ་བཞིའི་ཚིག་བླ་དགས་ཡིན་ནོ། །

[Block 3351]
དགེ་སློང་ཇི་ལྟར་རྟོགས་པའི་ལམ་གྱིས༌[^2339]འཇུག་ཅེས་བྱ་བ་འདི་ནི་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་ཀྱི་ཚིག་བླ་དགས་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 3352]
དེ་ལྟ་བས་ན་གཉི་ག་ལ་འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་འདོད་པར་བྱ་དགོས་པས་གོ་རིམས་གྲུབ་པ་ཡིན་ནོ། །

[Block 3353 [HEADING]]
##### ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ། ^3-2-17-4-0

[Block 3354]
བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་དུ་ཞིག་ནི་ཟག་པ་དང་བཅས་པ་དག་ཡིན། དུ་ཞིག་ནི་ཟག་པ་མེད་པ་དག་ཡིན་ཞེས་བྱ་བ་འདི་བརྗོད་པར་བྱ་སྟེ། བྱང་ཆུབ་ཡན་ལག་ལམ་ཡན་ལག །ཟག་པ་མེད། དེ་གཉིས་ནི་བསྒོམ་པའི་ལམ༌[^2340]དང་མཐོང་བའི་ལམ་ལ་རྣམ་པར་གཞག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3355]
འཇིག་རྟེན་པའི་ཡང་དག་པའི་ལྟ་བ་ལ་སོགས་པ་ཡང་ཡོད་མོད་ཀྱི། དེ་དག་ནི་འཕགས་པའི་ལམ་ཞེས་བྱ་བའི་སྒྲ་མི་འཐོབ་པོ། །གཞན་རྣམ༌[^2341]གཉིས་སོ། །

[Block 3356]
བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་གཞན་དག་ནི་ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ་ཡང༌[^2342]ཡིན་ནོ། །

[Block 3357 [HEADING]]
##### ས་གང་ན་དུ་ཞིག་ཡོད་པ། ^3-2-17-5-0

[Block 3358]
ས་གང་ན་བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་མཐུན་པ་དུ་ཞིག་ཡོད་ཅེ་ན་བསམ་གཏན་དང་པོ་ན་ཐམས་ཅད། བསམ་གཏན་དང་པོ་ན་སུམ་ཅུ་རྩ་བདུན་པོ་ཐམས་ཅད་ཡོད༌[^2343]དོ། །

[Block 3359]
མི་ལྕོགས་མེད་ན་དགའ་མ་གཏོགས། །ཅིའི་ཕྱིར་མི་ལྕོགས་པ་མེད་པ་ན་དགའ་བ་མེད་ཅེ་ན། ཉེར་བསྡོགས་རྣམས་ནི་སྟོབས་ཀྱིས་དྲང་དགོས་པའི་ཕྱིར་དང་། ས་འོག་མའི་དོགས་པ༌[^2344]དང་བཅས་པའི་ཕྱིར་རོ། །

[Block 3360]
གཉིས་པ་ན་ནི་རྟོག་མ་གཏོགས། །བསམ་གཏན་གཉིས་པ་ན་ནི་ཡང་དག་པའི་རྟོག་པ༌[^2345]མ་གཏོགས་པ་སུམ་ཅུ་རྩ་དྲུག་ཁོ་ན་ཡོད་དེ། [^2346]དེ་ན་རྟོག་པ་མེད་པའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
