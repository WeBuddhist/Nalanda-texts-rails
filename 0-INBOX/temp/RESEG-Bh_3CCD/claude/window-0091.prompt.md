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
[Block 3186]
བྱང་ཆུབ་སེམས་དཔའི་སྒྲ་ནི་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་དང་སྤྲུལ་པའི་སྐུ་དབྱེར་མེད་པའི་ཕྱིར་རོ། །

[Block 3187]
དབྱེར་མེད་པ་ཡང་བྱ་བ་གཅིག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3188]
དེ་ལྟར་སྐུ་རྡོ་རྗེ་ལ་སོགས་པ་སྔ་མ་བཞིན་ནོ། །

[Block 3189]
ཏིང་ངེ་འཛིན་རྡོ་རྗེ་ནི་ནམ་མཁའི་སྙིང་པོ་ཞེས་པ་ལ། རིན་ཆེན་འབྱུང་ལྡན་གྱི་རིགས་ནམ་མཁའ་མཛོད་ཀྱི་ཏིང་ངེ་འཛིན་གཙོ་བོར༌[^2061]གྱུར་པའི་ཕྱིར་རོ། །

[Block 3190]
རྒྱལ་བ་རྡོ་རྗེ་ནི་བྱམས་པ་ཞེས་པ་ལ། །མ་འོངས་པའི་དུས་སུ་ཆོས་ཀྱི་རྒྱལ་སྲིད་ལ་མངའ་མཛད་པའི་ཕྱིར་རོ། །

[Block 3191]
ས་རྡོ་རྗེ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཁམས་བཞིའི་རྣམ་པར་དག་པའི་ངོ་བོ་སྤྱན་ལ་སོགས་པ་བསྟན་ཏོ། །

[Block 3192]
དམ་ཚིག་སྒྲོལ་མ་ཞེས་པ་ནི་དོན་ཡོད་གྲུབ་པའི་རིགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3193]
གང་གི་ཕྱིར་སྒྲོལ་མ་ནི་གཉིས་ཏེ། དམ་ཚིག་གི་སྒྲོལ་མ་དང་། དབང་གི་སྒྲོལ་མའོ། །

[Block 3194]
དབང་གི་སྒྲོལ་མ་ནི་འོད་དཔག་ཏུ་མེད་པའི་རིགས་ཅན་ནོ། །

[Block 3195]
དམ་ཚིག་སྒྲོལ་མ་ནི་དེ་ཉིད་ཀྱི་སྐུའི་བྱེ་བྲག་གོ། །

[Block 3196]
ནམ་མཁའ་རྡོ་རྗེ་ནི་འཇམ་དཔལ་ཞེས་པ་ལ་རྟག་ཏུ་དྲི་མ་མེད་ཅིང་ཟག་པ་མེད་པའི་ཤེས་རབ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 3197]
གཟུགས་རྡོ་རྗེ་ཞེས་བྱ་བ་ལ་སོགས་པས་གཟུགས་ལ་སོགས་པ་རྣམ་པར་དག་པའི་མཚན་ཉིད་ཅན་མཆོད་པའི་ལྷ་མོ་དང་དབུས་ཀྱི་གཙོ་མོ་ཡང་བསྟན་ཏོ། །

[Block 3198]
ཆོས་ཀྱི་དབྱིངས་ཀྱི་རྡོ་རྗེ་ནི་ཀུན་ཏུ་བཟང་པོ་ཞེས་པ་ནི་ཆོས་ནི་བྱ་བ༌[^2062]གྲུབ་པའི་ཡེ་ཤེས་ཀྱི་རང་བཞིན་ཅན་འཛིན་པ་དང་། མི་ཕྱེད་པའི་ཕྱིར་རྡོ་རྗེ་སྟེ། ཆོས་ཀྱི་དབྱིངས་ཀྱི་རྡོ་རྗེ་དམ་ཚིག་གི་རིགས་ཅན་ནོ། །

[Block 3199]
བྱང་ཆུབ་སེམས་དཔའི་ཚོགས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནམ་མཁའི་དབྱིངས་དང་མཚུངས་པ། ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའི་ངོ་བོ་ཉིད་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་གསུངས་སོ། །

[Block 3200]
དེ་དག་ཅེས་བྱ་བ་ལ་སོགས་པས་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་ལྔ་བཟུང༌[^2063]སྟེ། དེ་དང་འདྲ་བའི་དེ་བཞིན་གཤེགས་པ་གཞན་རྣམས་ཀྱང་བསྟན་ཏོ། །

[Block 3201]
རིགས་ལྔས་བསྡུས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་རྣམས་ཁོ་ན་བསྟན་ཏོ། །

[Block 3202]
དེ་ལྟར་ན༌[^2064]གང་གིས་ལྷའི་འཁོར་ལོ་ཡོངས་སུ་རྫོགས་པ་དེ་ཙམ་ཉིད་ཀྱི་དཔེ་བསྟེན་པའི༌[^2065]ཕྱིར་དེ་བས་ན་སུམ་ཅུ་རྩ་གཉིས་དགོད་པར་རིགས་ན་ཅིའི་ཕྱིར་ཁྲོ་བོ་རྣམས་མ་བསྟན་ཞེ་ན། དེ་ནི་བདེན་ཏེ། འོན་ཀྱང་འགྲེལ་པ་མཁན་གྱིས་འཆད་པར་འགྱུར་ཏེ།

[Block 3203]
དཔེར་ན་སྐུའི་དཀྱིལ་འཁོར་ཉིད་དུ་ལྷ་དགོད་པ་ཇི་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པས་བཤད་པའི་རྒྱུད་ཀྱི་ཁུངས་ལས།

[Block 3204]
སྐུའི་དཀྱིལ་འཁོར་བཞིན་དུ་འབྱིན་པའི་དཀྱིལ་འཁོར་ལ༌[^2066]ཡང་ཡོད་པར་རིགས་སོ། །

[Block 3205]
འདིར་མ་གསུངས་པ་ནི་རང་གིས་གླེགས་བམ་ལྟ་བ་རྣམས་ལ་འཁྲུལ་པ་བསྐྱེད་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 3206]
འབྱིན་པའི་དཀྱིལ་འཁོར་གྱི་སྐབས་སུ་ལེའུ་དང་པོ་ལས་བཞི་པོ་གསུངས་ཏེ་ལྷག་མ་རྣམས་ལེའུ་བཅུ་གསུམ་པོ༌[^2067]ལས་གསུངས་པ་རྣམས་མདོ་བསྲེས་ཏེ་ཤེས་པར་བྱའོ། །

[Block 3207]
ཀློག་པའི་རིམ་པ་ལས་དོན་གྱི་རིམ་པ་སྟོབས་དང་ལྡན་པ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 3208]
དེའི་ཕྱིར་གང་གིས་ལྷའི་འཁོར་ལོ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་བ་གང་གསུངས་པ་དེ་ནི་རིགས་པ་ཁོ་ནའོ། །

[Block 3209]
ནམ་མཁའི་དབྱིངས་ཐམས་ཅད་དང་མཉམ་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་གཞལ་ཡས་ཁང་པའི་ཕྱི་རོལ་ཏུ་བར་སྣང་ལ་བཞུགས་སོ་ཞེས་པའི་བར་དུའོ། །

[Block 3210]
འདི་ལྟ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཏིལ་གྱི་གང་བུའི་དཔེས་དེ་བཞིན་གཤེགས་པ་མཐའ་ཡས་པ་རྣམས་ཀྱི་གནས་པ་མི་འགལ་བ་བསྟན་པའོ། །

[Block 3211]
དྲང་བའི་དོན་ཞེས་པ་ནི་ཡོད་པ་ཙམ་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3212]
བརྗོད་ཀྱིས་མི་ལང་བ་ཞེས་བྱ་བ་ལ་སོགས་པས་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་མ་ལུས་པ་ཉེ་བར་བསྡུས་ནས་ཀྱང་ལྷ་ཐམས་ཅད་ཀྱི་ངོ་བོ་རྡོ་རྗེ་འཆང་ཆེན་པོས་སེམས་ཅན་རྗེས་སུ་གཟུང་བར་བྱ་བའི་ཕྱིར་གཞལ་ཡས་ཁང་པ་དང་དཀྱིལ་འཁོར་པ་རྣམས་སྤྲུལ་ཏེ་རྒྱུད་གསུང༌[^2068]ཞེས་བྱ་བ་འདིས་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 3213]
ངེས་པའི་དོན་ཞེས་པ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཉིད་གཞི་དང་གཞི་ཅན་གྱི་དཀྱིལ་འཁོར་གྱི་དེ་ཁོ་ན་ཉིད་ཀྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3214]
དེ་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པས་གླེང་གཞི་སྡུད་པར་བྱེད་དོ། །

[Block 3215]
དེ་ནི་འདོད་པའི་ཁམས་ན་གནས་པའི་ཡུལ་ལ་ཆགས་པའི་སེམས་ཅན་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་དཔལ་གསང་བ་འདུས་པ་ལ༌[^2069]བསྟན་པའི་དུས་སུ་དང་པོ་རང་གི་སྐུ་ལ་གྲུབ་པའི་ལྷའི༌[^2070]འཁོར་ལོ་ཕྱི་རོལ་དུ་སྤྲོས་ཏེ། སླར་ཡང་སྐུའི་དཀྱིལ་འཁོར་གྱི་ཚུལ་དུ་བསྡུས་ལ། སླར་ཡང༌[^2071]ལྷ་མོ་དགུར་སྤྲོས་ཏེ། དེ་དག་གཅིག་ཏུ་སོང་བ་དང་ལྷན་ཅིག་ཏུ་བདེ་བ་ཆེན་པོ་མྱོང་ནས་སླར་ཡང་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཉེ་བར་བསྡུས་ཏེ་གཞལ་ཡས་ཁང་པ་སྤྲུལ་ཞིང་དེའི་ནང་དུ་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་བྱིན་གྱིས་བརླབས་ལ། དེ་ཡང་དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི་རིམ་པས་ཉེ་བར་བསྡུས་ཏེ་དབུས་ཀྱི་གཙོ་བོར་གྱུར་ནས་དང་པོའི་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་མཐར་དཀྱིལ་འཁོར་འབྱིན་པའི་མཚན་ཉིད་ཅན་གྱི༌[^2072]དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་རབ་ཏུ་བསྟན་པར་གྱུར་ཏོ། །

[Block 3216]
དེ་ཉིད་སྤྲོས་ཏེ་བསྟན་པར་བྱ་བའི་ཕྱིར། འདོད་པའི་ཡོན་ཏན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ལ། གཟུགས་ལ་སོགས་པ་ལ༌[^2073]ཕྱག་རྒྱ་གཅིག་ལ་གནས་པས་གྲོལ་བར༌[^2074]རབ་ཏུ་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 3217]
དེ་ནས་ཞེས་བྱ་བ་ནི་དེ་མ་ཐག་པའོ་ཞེས་པ་ནི་འཁོར་གྱི་ནང་དུ་གནས་པའི་འོག་ཏུའོ། །

[Block 3218]
ཡོན་ཏན་བརྒྱད་ཀྱི་དབང་ཕྱུག་དང་ལྡན་པ་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 3219]
ཆེན་པོ་ཡང་ཡིན་ལ་རྣམ་པར་སྣང་མཛད་ཀྱང་ཡིན་པས་ན་ཞེས་པ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3220]
འདོད་ཆགས་ཀྱིས་འདོད་ཆགས་རབ་ཏུ་སྤང་བར་བྱ་བའི་ཕྱིར་ཞེས་པ་ནི་ཕྱག་རྒྱ་བསྟན་པའི༌[^2075]ཆགས་པས་འདོད༌[^2076]ཆགས་ཀྱི་ཉོན་མོངས་པ་བཟློག་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 3221]
འདོད་ཆགས་དང་བྲལ་བའི་སྐུ་སྤངས་ནས་ཞེས་པ་ནི་སྙིགས་མ་ལྔའི་དུས་སུ་སྒེག་པའི་ཉམས་གཙོར་གྱུར་པས་སྒེག་ཅིང་གཟུགས་བསྟན་ཏོ། །

[Block 3222]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3223]
སེམས་ཅན་རྣམས་སྨིན་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་ངོ་བོ་ནི་སྙིང་རྗེ་ཆེན་པོའི་བདག་ཉིད་ཀྱི་རྒྱུ་ཅན་ཡིན་ཞེས་བསྟན་ཏོ། །

[Block 3224]
དེ་བས་ན་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་བསྒོམ་པས་གང་གི་ཚེ་འགྲོ་བའི་དོན་བྱེད་ན་དེའི་ཚེ་དེ་རྫོགས་པར་བྱ་བའི་ཕྱིར་དེ་དང་རྗེས་སུ་མཐུན་པའི་ཏིང་ངེ་འཛིན་ལ་དཔལ་རྡོ་རྗེ་འཆང་ཆེན་པོས་དམིགས་པར་མཛད་ཅེས་རྒྱུད་ཐམས་ཅད་ཀྱི་གཞུང་ལུགས་སོ། །

[Block 3225]
དཀྱིལ་འཁོར་པ་རྣམས་ཞེས་པ་ནི་འཁོར་རྣམས་སོ། །
--- END BLOCKS ---
