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
[Block 3396]
དེས་བསྐྱེད་པའི་ས་བོན་གྱི་ཡི་གེ་སྟེ། །ཞེས་པ་ནི་བཛྲ་དྷྲྀཀ་ཅེས་བྱ་བ་ལ་སོགས་པ་ཕྱུང་བའི་སྔགས་ཀྱི་ཡི་གེ་རྣམས་སོ། །

[Block 3397]
དེ་རྣམས་ཀྱིས་བྱིན་གྱིས་བརླབས་པར༌[^2187]མཛད་ནས་ཞེས་བྱ་བའི་བར་རོ། །

[Block 3398]
སྤྱིའི་དོན་ནི་བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པའི་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3399]
དབང་པོ་གཉིས་ཀྱིས༌[^2188]སྙོམས་པར་འཇུག་པ་ཞེས་པ་ནི་གསང་བའི་རྡོ་རྗེ་དང་ཆུ་སྐྱེས་ཕྲད་པའོ། །

[Block 3400]
རྡོ་རྗེའི་དམ་ཚིག་ཅེས་པ་ནི་རྡོ་རྗེ་དང་དམ་ཚིག་གོ། །

[Block 3401]
རྡོ་རྗེ་དང་དམ་ཚིག་སྟེ་ཟླས་དབྱེ་བའི་བསྡུ་བའི་དོན་གཅིག་པའོ། །

[Block 3402]
ཡང་ན་རྡོ་རྗེ་ནི་དེ་བཞིན་གཤེགས་པའམ་རྣལ་འབྱོར་པ་རྣམས་ཀྱིའོ། །

[Block 3403]
དམ་ཚིག་ནི་དབང་པོ་གཉིས་སྙོམས་པར་ཞུགས་པ་ཁོ་ནའོ། །

[Block 3404]
བྱང་ཆུབ་སེམས་ཀྱི་ཐིག་ལེ་ཞེས་པ་ནི་སྙོམས་པར་ཞུགས་པའི་སྒྲས་ནམ་མཁའི་དབྱིངས་མ་ལུས་པ་ན་གནས་པའི་དེ་བཞིན་གཤེགས་པ་འཇུག་པས་ཡོངས་སུ་གྱུར་པའི་ཤུ་ཀྲའི་ཐིག་ལེ་རྣམས་སོ། །

[Block 3405]
དབང་བསྐུར་བར་བྱ་བ་སྟེ་ཞེས་པ་ནི་ཆོས་འབྱུང༌[^2189]ནང་དུ་ཐིག་ལེ་རྣམས་ཀྱིས༌[^2190]གསང་བའི་དབང་བྱིན་ནས་སོ། །

[Block 3406]
སྦས་པ་ནི་འདོད་ཆགས་ཀྱི་ཆོས་བསྟན་པས་སོ། །

[Block 3407]
འོད་གསལ་བ་ནི་ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་གྱི་རིམ་པས་ཐོབ་པར་བྱ་བའི་དེ་ཁོ་ན་ཉིད་བཞི་པའོ། །

[Block 3408]
ཆེན་པོ་སྟོང་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཆགས་པ་བར་མ་དང་ཆགས་པ་དང་། ཆགས་པ་དང་བྲལ་བའོ། །

[Block 3409]
དེས་བྱིན་གྱིས་རློབ་པ༌[^2191]ནི་ཆགས་པ་བར་པ་ལ་སོགས་པ་བཀག་ནས་སོ། །

[Block 3410]
གདུལ་བྱའི་སྐྱེ་བོའི་རྒྱུད་ལ་ནི་འཁོར་གྱི་སེམས་ཀྱི་རྒྱུད་རྣམས་སུའོ། །

[Block 3411]
ལྷའི་སྐུ་རྣམ་པ་གཉིས་གསལ་བར་མཛད་ནས་ཞེས་པ་ནི་སྔགས་ཀྱི་སྐུ་དང་ཡེ་ཤེས་ཀྱི་སྐུ་དབྱེར་མེད་པར་བྱས་ནས་སོ། །

[Block 3412]
མཐར་ཐུག་པ་ནི་འོད་གསལ་བ་ལ་འཇུག་པ་དང་ཟུང་དུ་འཇུག་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3413]
དེ་ལྟར་གསོལ་བ་བཏབ་པ་དང་། ཞེས་བྱ་བ་ལ་སོགས་པས་རང་གི་སྙིང་ག་ནས་སྤྲོས་པའི་དེ་བཞིན་གཤེགས་པ་རྣམས༌[^2192]གསོལ་བ་བཏབ་པ་ཐོས་མ་ཐག་ཏུ་དེ་རྣམས་ལ་དབང་བསྐུར་བས་ཆོས་བསྟན་པ་ལ་དབང་བ་ཡིན་པས་དེ་དང་འབྲེལ་པའི༌[^2193]ཡེ་ཤེས་ཀྱི་དཀྱིལ་འཁོར་སྤྲུལ་པར་མཛད་དོ་ཞེས་བསྟན་ཏོ། །

[Block 3414]
ཡེ་ཤེས་ཀྱི་དཀྱིལ༌[^2194]འཁོར༌[^2195]ནི་ལེགས་པར་སྦྱངས་པའི་ཡན་ལག་དང་ཉིང་ལག་དང་ལྡན་པའི་དམ་ཚིག་གི་ཕྱག་རྒྱ་པདྨའི་ནང་དུ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེ་ལས་སྤྲུལ་པའི་དམ་ཚིག་གི་དཀྱིལ་འཁོར་རོ། །

[Block 3415]
དེའི་སྤྲུལ་པ༌[^2196]དང་རྗེས་སུ་མཐུན་པའི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་པ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། ཡེ་ཤེས་ཉིད་སྒྲོན་མ་ཡིན་པས་ན་ཞེས་སྨོས་ཏོ། །

[Block 3416]
ཡེ་ཤེས་ནི་དཀྱིལ་འཁོར་སྤྲུལ་པའི་ཕྱིར་སེམས་རྩེ་གཅིག་པ་ཉིད་དོ། །

[Block 3417]
སྒྲོན་མ་ནི་སྤྲུལ་པའི་དཀྱིལ་འཁོར་རབ་ཏུ་བསྟན་པས་སོ། །

[Block 3418]
ཡི་གེའི་དོན་ནི་དེ་ཙམ་བར་དུ༌[^2197]བསྟན་པས་སོ། །

[Block 3419]
སེམས་ཅན་རྣམས་ཀྱི་རྒྱུད་ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གདུལ་བྱའི་རྒྱུད་ལའོ། །

[Block 3420]
ཡེ་ཤེས་ནི་ཤིན་ཏུ་རྣམ་པར་དག་པའི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་སོ། །

[Block 3421]
དེ་ཉིད་ཀྱིས་རབ་ཏུ་སྣང་བ་མཛད་པས་ན་ཡེ་ཤེས་ཀྱི་སྒྲོན་མ་སྟེ་མི་བསྐྱོད་པའོ། །

[Block 3422]
སྤྱིའི་དོན་ནི་མདོ་སྡེ་ལ་སོགས་པ་རྣམས་ཀྱི་འགྱོད་པ་བཟློག་པས་སོ། །

[Block 3423]
རྣམ་པར་ཤེས་པ་གསུམ་གྱི་སྣང་བས་ཞེས་པ་ནི། རྣམ་པར་ཤེས་པ་གསུམ་རྣམ་པར་དག་པའི་ངོ་བོ་ཡེ་ཤེས་གསུམ་རྣམ་པར་དག་པ་སེམས་ལ་དམིགས་པ་ཐོབ་པའོ། །

[Block 3424]
ཕྱོགས་བཅུར་སྣང་བར༌[^2198]མཛད་པས་ཞེས་པ་ནི་གཏན་ཚིགས་སོ། །

[Block 3425]
སྦས་པ་ནི་ཡེ་ཤེས་གསུམ་བརྟག་པའི༌[^2199]མཚན་ཉིད་ཅན་གྱི་དོན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3426]
ཛྙཱ་ན་རྟོག་པའི་དོན་ཏོ། །ཞེས་བྱ་བ་ནི་འདོད་ཆགས་དང་བྲལ་བ་ལ་སོགས་པ་ཡོངས་སུ་ཤེས་པའི་མཚན་ཉིད་ནི་ཡེ་ཤེས་ཏེ་ཛྙཱའོ། །

[Block 3427]
ན་ནི་དགག་པ་ལ་འཇུག་པ༌[^2200]སྟེ་ཞེས་བྱ་བ་ནི་ཨ་མ་ནོ་ན་དགག་པའི་དོན་ཞེས་འབྱུང་བས་སོ། །

[Block 3428]
དེ་གང་ཡིན་ཞེས་པ་ནི་འདོད་ཆགས་ལ་སོགས་པ༌[^2201]འགོག་པའི་མཚན་ཉིད་ཅན་འོད་གསལ་བའི་རྣམ་གྲངས་དེ་ཁོ་ན་ཉིད་བཞི་པ་གཟི་བརྗིད་མ་ལུས་པའི་ཟིལ་གྱིས་གནོན་པ་མི་ཕྱེད་པའི་ཏིང་ངེ་འཛིན་ཞེས་བསྟན་ཏོ། །

[Block 3429]
མཐར་ཐུག་པ་ནི་མན་ངག་བཞི་པ་བརྗོད་པར་འདོད་པས་སོ། །

[Block 3430]
རང་བཞིན་གྱིས་འོད་གསལ་བའི་ཏིང་ངེ་འཛིན་ལས་བཞེངས་ནས་ཞེས་བྱ་བ་ལ་སོགས་པའི་དོན་ནི་འདི་ཡིན་ཏེ། དང་པོའི་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་རྗེས་སུ་ཨུཏྤ་ལ་སྔོན་པོའི་འདབ་མ་དང་འདྲ་བའི༌[^2202]ལོ་བཅུ་གཉིས་པ་སྨེ་ཤ་ཅན་གྱི་བུ་མོ་ཕྱག་རྒྱ་རྙེད་ནས་སྔོན་དུ་བཤད་པའི་རིམ་པས་དེའི་ཐ་མལ་པའི་ལུས༌[^2203]བསྲེགས་ཏེ། དེའི་རྣམ་པར་ཤེས་པ་ནི་འཁྱུད་པའི་ཡེ་ཤེས་ཀྱི་ཕྱག་རྒྱའི་ཆོས་འབྱུང་བའི་ནང་དུ་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་ལ་ཞལ་གསུམ་པ་ཕྱག་དྲུག་པ་སྐུ་མདོག་ནག་པོ་དང་མཐིང་ག་དང་དཀར་བ་དང་དམར་པོ་སྟེ་ཞལ་གསུམ་པ། རྡོ་རྗེ་དང་འཁོར་ལོ་དང་པདྨ་དང་དྲིལ་བུ་དང་རིན་པོ་ཆེ་དང་རལ་གྲི་གཡས་པ༌[^2204]དང་གཡོན་པའི་ཕྱག་ན་བསྣམས་པ། རྡོ་རྗེ་སྐྱིལ་མོ་ཀྲུང་གིས་བཞུགས་པ་སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་ཅན་རེག་བྱ་རྡོ་རྗེ་མ་རྣམ་པར་སྤྲོས་ཏེ་རྣལ་འབྱོར་དང་རྗེས་སུ་རྣལ་འབྱོར་བྱས་ནས། དེ་ནས་ཀྱང་ཕྱི་རོལ་དུ་སྤྲོས་ཏེ་དེ་དང་ལྷན་ཅིག་ཏུ་རོ་གཅིག་པར་བྱས་ཏེ་སྤྱི་བོ་ལ་སོགས་པའི་གནས་ལྔ་ལ་རིགས་ལྔས་ཁྱབ་པར་བྱས་ཏེ་མིག་ལ་སོགས་པ་རྣམས་སུ་སའི་སྙིང་པོ་ལ་སོགས་པ་དང་། སྙོམས་པར་ཞུགས་པའི་གཟུགས་རྡོ་རྗེ་མ་ལ་སོགས་པའི་ལྷ་མོའི་ཚོགས་རྣམས༌[^2205]རྣམ་པར་བཀོད་ལ། སའི་ཁམས་ཀྱི་ངོ་བོ་ཡི་གེ་ལཾ་ཡོངས་སུ་གྱུར་པའི་སངས་རྒྱས་སྤྱན་ལས་སྐྱེས་པའི་དེའི་ནུ་མ་དང་། ཡི་གེ་མཾ་ཆུའི༌[^2206]ཁམས་ཀྱི་ངོ་བོ་ཡོངས་སུ་གྱུར་པ་ལས་མཱ་མ་ཀཱི་དེའི་རང་བཞིན་ཆུ༌[^2207]དང་། བཾ་གྱི་ས་བོན་ལས་མེའི་ཁམས་ཀྱི་ངོ་བོ་ཡོངས་སུ་གྱུར་པ་ལས་གོས་དཀར་མོའི་རང་བཞིན་དེའི་པདྨ་དང་། ཡི་གེ་ཏཾ་ལས་རླུང་གི་ཁམས་ཀྱི་རང་བཞིན་སྒྲོལ་མ་ཡོངས་སུ་གྱུར་པའི་པདྨའི་ནང་དུ་ཁོང་སྟོང་བསམས་ལ། གསང་བ་ལ་སོགས་པའི་གནས་བཅུ་ལ་རྡོ་རྗེ་རོ་ལངས་མ་ལ་སོགས་པ་ཁྲོ་བོའི༌[^2208]རྒྱལ་པོ་རྣམས་ཀྱི་བཙུན་མོ་བཅུ་རྣམ་པར་བཀོད་ལ་སྐུ་གསུང་ཐུགས་ཀྱང་བྱིན་གྱིས་བརླབ་པར༌[^2209]བྱ་སྟེ། དེའི་པདྨ་ཡང་སྟོང་པ་ཉིད་བསྒོམ་པ་སྔོན་དུ་སོང་བ་ཡི་གེ་ཨ་ཡོངས་སུ་གྱུར་པའི་པདྨ་འདབ་མ་བརྒྱད་པའི་རྣམ་པར་བྱས་ལ། དེའི་ལྟེ་བ་ལ་ཨོཾ་གྱི་བྱིན་གྱིས་བརླབ་པར་བྱས་ལ། བདག་ཉིད་ཀྱི་གསང་བའི་རྡོ་རྗེ་ཡང་སྔ་མ་བཞིན་ཧཱུྃ་ཡོངས་སུ་གྱུར་པ་ལས་རྡོ་རྗེ་རྩེ་ལྔ་པ་བསྒོམ་པར་བྱ་སྟེ། དེའི་ཆང་ཟུངས་ཡང་ཡི་གེ་ཨོཾ་གྱི་བྱིན་གྱིས་བརླབ་པར༌[^2210]བྱས་ལ།

[Block 3431]
དང་པོ་རྗེས་སུ་ཆགས་པར་བྱ་བའི་ཕྱིར། དེའི་པདྨ་ལ་ཧཱུཾ་གིས་བྱིན་གྱིས་རློབ་པའི༌[^2211]མིག་དང་ལྕགས་ཀྱུ་དང་བ་དན་དང་སྡིགས་མཛུབ་ཀྱི་ཕྱག་རྒྱ་རྣམས་ལས་གང་ཡང་རུང་བ་བཅུག་ལ། གྲང་བ་མ་ཡིན་པའི་རེག་པའི་བར་དུ་བསྐྱེད་པར༌[^2212]བྱས་ལ། བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་རྒྱུན་འབྱུང་བར་འགྱུར་བའི་ཚེ་འདོད་ཆགས་ཆེན་པོའི་དབང་གིས་རང་གི་མགྲིན་པ་ནས་བཟུང་སྟེ་རྣམ་པར་བསམས་ལ། དེ་དང་འཁྱུད་པ་དང་འོ་ལ་སོགས་པ་རྣམ་པ་བརྒྱད་དེའི་སྐད་འཇམ་པོ༌[^2213]དགའ་བའི་རང་བཞིན་ཐོས་ནས། ཨོཾ་སརྦ་ཏ་ཐཱ་ག་ཏ་ཨ་ནུ་རཱ་ག་ན་བཛྲ་སྭ་བྷཱ་ཝ་ཨཱཏྨ་ཀོ྅ཧཾ། ཞེས་འདིས་ནི་རྡོ་རྗེ་དང་པདྨ་ཡང་དག་པར་བཙིར་ལ། ཨོཾ་སརྦ་ཏ་ཐཱ་ག་ཏ་པཱུ་ཛ་བཛྲ་སྭ་བྷཱ་ཝ་ཨཱཏྨ་ཀོ྅་ཧཾ། ཞེས་བྱ་བའི་སྔགས་ཀྱིས་བསྐྱོད་ཅིང་། དམ་པ་དགའ་བའི་སྒྲས་ཕྱོགས་བཅུ་ན་གནས་པའི་དེ་བཞིན་གཤེགས་པ་བཀུག་ལ་ངག་གི་ལམ་དུ་འཇུག་པར་བྱས་ལ། རྩ་དབུ་མ་ནས་རྡོ་རྗེ་ནོར་བུའི་རྩེ་མོར་བྱང་ཆུབ་ཀྱི་སེམས་ཐིག་ལེར་བསམས་ཏེ། འདོད་ཆགས་དང་འདོད་ཆགས་བྲལ་བ་དང་འདོད་ཆགས་བར་མའི༌[^2214]རིམ་གྱིས་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་མྱོང་ནས་འཆད་པར་འགྱུར་བའི་བཛྲ་དྷྀཀ་ཅེས་བྱ་བ་ལ་སོགས་པའི་ཕྱུང་བའི་སྔགས་ཀྱིས་དེ་བཞིན་གཤེགས་པ་ལ་སོགས་པ་སྤྲོ་བར་མཛད་དོ་ཞེས་དགོངས་སོ། །

[Block 3432]
འོད་གསལ་བའི་ཏིང་ངེ་འཛིན་ལས་བཞེངས་ནས་ཞེས་བྱ་བ་ནི་བདེ་བ་ཆེན་པོའི་ཏིང་ངེ་འཛིན་ལས་སོ། །

[Block 3433]
ཉོན་མོངས་པ་ལྔས་ཁྱབ་པའི་སེམས་ཅན་གྱི་ཁམས་ལ༌[^2215]གཟིགས་ནས་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་ལ་སོགས་པའི་སྐྱོན་གྱིས་ཡོངས་སུ་ཁྱབ་པར་རྣམ་པར་གཟིགས་ནས་སོ། །

[Block 3434]
ཉོན་མོངས་པའི་རང་བཞིན་ཡོངས་སུ་ཤེས་པ་ཞེས་པ་ནི་གཟོད༌[^2216]མ་ནས་མ་སྐྱེས་པའི་རང་བཞིན་དེ་ཁོ་ན་ཉིད་ཤེས་པའོ། །

[Block 3435]
བྱང་ཆུབ་ཡིན་ལ་ནི་རྡོ་རྗེ་འཆང་ཉིད་དོ། །
--- END BLOCKS ---
