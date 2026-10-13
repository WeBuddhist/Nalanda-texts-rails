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
ཡང་ན་ཤེས་རབ་ནི་ཟླ་བ་དང་འདྲ་བའི་སྣང་བའོ། །

[Block 3362]
ཐབས་ནི་ཉི་མ་དང་འདྲ་བའི་སྣང་བ་མཆེད་པའོ། །

[Block 3363]
[^2171]ཡང་དག་པར་སྦྱོར་བ་ནི་མཚམས་ཀྱི་སྣང་བ་དང་འདྲ་བ་ཐོབ་པའོ།[^2172] །

[Block 3364]
དེ་ཡོངས་སུ་གྱུར་པ་ལས་ཡང་དག་པར་སྐྱེས་པའི་སྒྱུ་མ་ལྟ་བུའི་ཡེ་ཤེས་ཀྱི་སྐུ་སྟེ། འདུས་པའོ་ཞེས་ཀུན་རྫོབ་ཀྱི་བདེན་པ་རྟོགས་པའི༌[^2173]མཚན་ཉིད་ཅན་བདག་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 3365]
ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདེན་པ་དག་ཏུ་འདུས་པ་ནི་ཞེས་པ་ལ་ཉེ་བར་མཚོན་པ་འདི་ཡིན་པས་ཡོད་པ་དང་མེད་པ་དང་། དངོས་པོ་དང་དངོས་པོ་མེད་པ་དང་། རྣམ་པ་དང་། རྣམ་པ་མེད་པ་དང་། རྟག་པ་དང་། ཆད་པ་དང་། གཅིག་པུ་དང་། དུ་མ་དང་། ཐབས་དང་ཤེས་རབ་ལ་སོགས་པ་གཉིས༌[^2174]པོ་གཅིག་ཏུ་འདུས་པའི་རང་བཞིན་ནོ། །

[Block 3366]
གསལ་བ་ཞེས་པ་ནི་འོད་གསལ་བ་སྟེ་རིམ་པ་བཞི་པས་ཐོབ་པར་བྱ་བ་དེ་ཁོ༌[^2175]ཉིད་དོ། །

[Block 3367]
དེ་ལས་བྱུང་བ་ནི་ཞེས་པ་ལ་མྱུར་བའི་རྣམ་པས་སོ་ཞེས་ཚིག་གི༌[^2176]ལྷག་མའོ། །

[Block 3368]
གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ཀྱི་བདག་ཉིད་ཅན་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བའི་བར་དུ་སྟེ་ཞེས་པ་ལ། ཟུང་དུ་འཇུག་པའི་རིམ་པར༌[^2177]ཐོབ་པར་བྱ་བ་ཕྱག་རྒྱ་ཆེན་པོའི་གཟུགས་ཀྱི་མཚན་ཉིད་ཡེ་ཤེས་སོ། །

[Block 3369]
མཐར་ཐུག་པ་ནི་རིམ་པ་བཞི་པ་དང་ལྔ་པའི་རིམ་པས་སོ་སོར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3370]
དེ་ལྟར་གསང་བ་འདུས་པའི་དོན་བཤད་པས་རིམ་པ་གཉིས་གསལ་བར་བསྟན་ཏོ། །

[Block 3371]
གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་ཞེས་པ་ལ། རྡོ་རྗེ་འཆང་ཆེན་པོ་ནས་བརྩམས་ཏེ་དེ་བཞིན་གཤེགས་པ་ལ་སོགས་པ་འབྲེལ་པ་དྲུག་གཙོར་གྱུར་པའོ། །

[Block 3372]
སྦ་བར་བྱའོ་ཞེས་པ་ལ་བྱ་བ་དང་སྤྱོད་པའི་ཚུལ་ལ་གནས་པ་རྣམས་ལ་བསྟན་པར་བྱ་བ་མ་ཡིན་པའོ། །

[Block 3373]
དེ་རྣམས་ཀྱི་གཅིག་ཏུ་གྱུར་པའི་མཚན་ཉིད་ཅན་ནི་ཞེས་པ་ལ། རིགས་བརྒྱའི་དབྱེ་བ་ལ་བརྟེན་ཏེ་བསྡུས་པས་སྐུ་དང་གསུང་དང་ཐུགས་ཀྱི་ངོ་བོར་བསྡུས་པའི་ཕྱིར་རོ། །

[Block 3374]
ཇི་ལྟ་བ་བཞིན་དུ་འབྱུང་བ་ཞེས་པ་ནི་རིམ་པ་གཉིས་བརྗོད་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3375]
དེས་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་ཞུས་པའོ། །

[Block 3376]
དེ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པ་ནས་བརྡ་སྤྲོད་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་བར་དུ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོས་ལེགས་སོ་ལེགས་སོ་སྦྱིན་པ་སྔོན་དུ་འགྲོ་བ་རིན་པོ་ཆེ་ལྟ་བུ་དབང་པོ་རྣོ་བ་རྣམས་ཀྱང་སྤྱོད་ཡུལ་མ་ཡིན་ན། ཙནྡན་ལ་སོགས་པ་དབང་པོ་དམན་པ་རྣམས་ཀྱི༌[^2178]ག་ལས་འགྱུར་རོ་ཞེས་པས་དྲི་བ་ལ་ལན་མི་རྩོལ་ཞེས་བསྟན་ཏོ། །

[Block 3377]
དེ་ལྷར་བྱ་བ་ནས་བརྩམས་ཏེ་སྟོན་པ་ཡིན་ཏེ་ཞེས་པའི་བར་དུ་ནི་དབང་པོ་རྣོ་བ་དང་དམན་པ་དག་གིས་ཡུལ་མ་ཡིན་པ་ཉིད་ཀྱིས་དཔལ་གསང་བ་འདུས་པའི་རྒྱུད་མི་གསུང་བའི་ཕྱིར་ངོ་མཚར་དང་རྨད་དུ་བྱུང་བའི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་རིན་པོ་ཆེ་ལྟ་བུའི་གང་ཟག་གི་ངོ་བོ་བདག་ཅག་རྣམས་འཁོར་འདི་ཡིན་པས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩོལ་ཅིག་ཅེས་གསོལ་བ་བཏབ་པར་གྱུར་ཏོ་ཞེས་བསྟན་ཏོ། །

[Block 3378]
དགོངས་པས་བཤད་པ་ནི་དེ་བཞིན་གཤེགས་པའི་སྒྲ་ནི་རིན་པོ་ཆེ་ལྟ་བུ་གང་ཟག་གི་རྣམ་གྲངས་དང་བྱང་ཆུབ་སེམས་དཔའི་སྒྲ་ཡང་ཙནྡན་ལ་སོགས་པ་རྗོད་པར་བྱེད་པ་ཡིན་པས་འགལ་བའི་ཚིག་གི་སྦྱོར་བ་དང་། གསང་བ་འདུས་པའི་དེ་ཁོ་ན་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3379]
ད་ནི་སྣོད་དུ་རུང་བར་བྱ་བ་སྔོན་དུ་འགྲོ་བས་དཔལ་གསང་བ་འདུས་པ་རབ་ཏུ་སྟོན་ཅིག་ཅེས་སླར་ཡང་གསོལ་བ་གདབ་པར་བྱ་བའི་ཕྱིར་དམ་ཚིག་དང་སྡོམ་པ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་ལ་དམ་ཚིག་ནི་བསྲུང་བར༌[^2179]བྱ་བ་དང་བཟའ་བར་བྱ་བའོ། །

[Block 3380]
དེ་ལ་བསྲུང་བར་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པ་རིགས་ལྔའི་དམ་ཚིག་སྟེ་དཀོན་མཆོག་གསུམ་ལ་སྐྱབས་སུ་འགྲོ་བ་ལ་སོགས་པ་དང༌[^2180]སྲོག་གཅོད་པ་ལ་སོགས་པ་ལས་ལོག་པའོ། །

[Block 3381]
རྫོགས་པའི་རིམ་པའི་ཕྱོགས་སུ་སྲོག་གཅོད་པ་ལ་སོགས་པ་ཁོ་ནའོ། །

[Block 3382]
བཟའ་བར་བྱ་བ་ནི་བདུད་རྩི་དང་ལྕགས་ཀྱུ་ལ་སོགས་པ་མྱང་བར་བྱ་བ་ཁོ་ནའོ། །

[Block 3383]
སོགས་པའི་སྒྲས་ནི་ཚད་མེད་པ་བཞི་བསྒོམ་པ་ལ་སོགས་པའོ། །

[Block 3384]
རིགས་གསུམ་ཡོངས་སུ་གྱུར་པ་སྟེ་ཞེས་པ་ནི་དམ་ཚིག་ལ་སོགས་པ་བླངས་ནས་བསྐྱེད་པའི་རིམ་པ་ལས༌[^2181]ལུས་དང་ངག་དང་ཡིད་སྦྱང་བར་བྱ་བའི་ཕྱིར་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་རིགས་གསུམ་གྱི་གཟུགས་སུ༌[^2182]བདག་ཉིད་ཡོངས་སུ་གྱུར་ནས་ལྷའི་ང་རྒྱལ་གྱིས་གནས་པའོ། །

[Block 3385]
ཡི་གེའི་དོན་ནི་དམ་ཚིག་ལ་སོགས་པ་ཙམ་སོ་སོར་བསྟན་པས་སོ། །

[Block 3386]
ཡི་གེ་གསུམ་སྟེ་ཞེས་པ༌[^2183]ནི་ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་བུའི༌[^2184]ལྷའི་སྐུའོ། །

[Block 3387]
སྤྱིའི་དོན་ནི་བསྐྱེད་པའི་རིམ་པ་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3388]
ཡེ་ཤེས་གསུམ་ནི་རྣམ་པར་ཤེས་པ་གསུམ་གྱི་གཉེན་པོར་གྱུར་པའོ། །

[Block 3389]
རང་བཞིན་གྱིས་སྣང་བ་རླུང་གི་བཞོན་པ་དང་ལྡན་པ་སྟེ། ཞེས་པ་སྟེ་འདོད་ཆགས་དང་བྲལ་བ་ལ་སོགས་པ་རང་བཞིན་གྱི༌[^2185]ཚོགས་དང་བཅས་པ་འཇུག་པའི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་གསུམ་པོ་ནི་མི་མཐུན་པའི༌[^2186]ཕྱོགས་སོ། །

[Block 3390]
དེ་ལྟར་མི་མཐུན་པ་དང་གཉེན་པོའི་སྒོ་ནས་སེམས་རྣམ་པར་དག་པར་འགྱུར་རོ། །

[Block 3391]
སྦས་པ་ནི་ཡེ་ཤེས་གསུམ་པོ་བརྟགས་པའི་མཚན་ཉིད་ཅན་གྱི་སེམས་རྣམ་པར་དག་པའི་རིམ་པ་སོ་སོར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3392]
ཡེ་ཤེས་ཀྱི་རང་བཞིན་གྱི་སྐུ་སྟེ་ཞེས་པ་ནི་ཡེ་ཤེས་ནི་བཞི་པའོ། །

[Block 3393]
དེ་ལས་བྱུང་བའི་སྐུ་ནི་ཡེ་ཤེས་ཀྱི་སྐུའོ། །

[Block 3394]
མཐར་ཐུག་པ་ནི་འོད་གསལ་བ་དང་ཟུང་དུ་འཇུག་པ་བསྟན་པས་སོ། །

[Block 3395]
སྐུ་ལ་སོགས་པ་བཞུགས་པ་སྟེ་དེ་མཛད་པ་ཞེས་བྱ་བ་ནི་ལུས་ལ་སོགས་པ་སྣོད་དུ་རུང་བར་བྱ་བའི་ཕྱིར་པདྨའི་ནང་དུ་དམ་ཚིག་གི་དཀྱིལ་འཁོར་སྤྲོ་བར་མཛད་ནས་སོ། །

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
--- END BLOCKS ---
