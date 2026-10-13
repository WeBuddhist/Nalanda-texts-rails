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
[Block 3151]
བདེན་པ་མཐོང་བ་ལས་ཞེས་བརྗོད་དེ། དེ་དག་ཀྱང་། བདེན་པ་དག་ནི་བཞིར་བཤད་དོ། །གང་དུ་བཤད་ཅེ་ན།

[Block 3152]
ཆོས་ཟག་པ་དང་བཅས་པ་དང་། །ཟག་པ་མེད་པ༌[^1237]བསྟན་པར་རོ། །

[Block 3153]
དེར་གང་བཤད་པའི་རིམ་པ་ཅི་དེ་ཁོ་ན་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ་འོན་ཀྱང་།

[Block 3154 [VERSE]]
སྡུག་བསྔལ་ཀུན་འབྱུང་དེ་བཞིན་དུ། །
འགོག་དང་ལམ་སྟེ་དེ་ལྟར་ན། །

[Block 3155]
དེ་དག་གི་རིམ་པ་ནི་འདི་ཡིན་ཏེ། རང་གི་ངོ་བོ་ནི་སྔར་ཇི་སྐད་བཤད་པ་ཁོ་ན་བཞིན་ནོ། །

[Block 3156]
འདི་ཡང་། དེ་དག་ཇི་ལྟར་མངོན་རྟོགས་ཀྱིས།[^1238] །བདེན་པ་གང་ཞིག་སྔར་མངོན་པར་རྟོགས་པ༌[^1239]དེ་སྔར་བསྟན་ཏོ། །

[Block 3157]
གང་གི་ཚེ་ཚོར་བའི་ཕྱོགས་གཅིག་སྡུག་བསྔལ་གྱི་རང་བཞིན་ཡིན་པ་དེའི་ཚེ་ཇི་ལྟར་ན་འདུ་བྱེད་ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་སྡུག་བསྔལ་ཞེས་བརྗོད་ཅེ་ན།

[Block 3158 [VERSE]]
ཡིད་འོང་ཡིད་དུ་མི་འོང་དང་། །
དེ་ལས་གཞན་ཟག་བཅས་རྣམས་ཉིད། །
སྡུག་བསྔལ་ཉིད་གསུམ་ལྡན་པའི་ཕྱིར། །
ཅི་རིགས་མ༌[^1240]ལུས་སྡུག་བསྔལ་ལོ། །

[Block 3159]
དེ་ལ་ཡིད་དུ་འོང་བ་དག་ནི་འགྱུར་བའི་སྡུག་བསྔལ་གྱིས་སྡུག་བསྔལ་ལོ། །

[Block 3160]
ཡིད་དུ་མི་འོང་བ་དག་ནི་སྡུག་བསྔལ་གྱི་སྡུག་བསྔལ་གྱིས་སོ། །

[Block 3161]
དེ་དག་ལས་གཞན་རྣམས་ནི་འདུ་བྱེད་ཀྱི་སྡུག་བསྔལ་གྱིས་སྡུག་བསྔལ་ལོ། །

[Block 3162 [HEADING]]
#### ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདེན་པ། ^6-1-2-0

[Block 3163]
བཅོམ་ལྡན་འདས་ཀྱིས་བདེན་པ་བཞིར་གསུངས་པ་ལས།

[Block 3164]
བདེན་པ་གཉིས་ཀྱང་སྟེ། ཀུན་རྫོབ་དང་། དོན་དམ་པའི་བདེན་པ་སྟེ། དེ་དག་གི་མཚན་ཉིད་ཅི་ཞེ་ན།

[Block 3165 [VERSE]]
གང་ལ༌[^1241]བཅོམ༌[^1242]དང་བློ་ཡིས་གཞན། །
བསལ་ན་དེ་བློ་མི་འཇུག་པ། །
བུམ་ཆུ་བཞིན་དུ་ཀུན་རྫོབ་ཏུ། །
ཡོད་དེ་དོན་དམ་ཡོད་གཞན་ནོ། །

[Block 3166]
གང་ལ་ཆ་ཤས་སུ་བཅོམ་ན་དེའི་བློ་མི་འཇུག་པ་དེ་ནི་ཀུན་རྫོབ་ཏུ་ཡོད་པ་སྟེ། དཔེར་ན་བུམ་པ་ལྟ་བུའོ། །

[Block 3167]
གང་ལ་བློས་ཆོས་གཞན་བསལ་ན་དེའི་བློ་མི་འཇུག་པ་དེ་ཡང་ཀུན་རྫོབ་ཏུ་ཡོད་དེ། དཔེར་ན་ཆུ་ལྟ་བུའོ། །

[Block 3168]
དེ་ལས་གཞན་ནི་དོན་དམ་པར་ཡོད་དེ། གང་ལ་བཅོམ་པའམ་བློས་ཆོས་གཞན་བསལ་ཡང་དེའི་བློ་འཇུག་པ་ཉིད་ནི་དཔེར་ན་གཟུགས་ལྟ་བུའོ། །

[Block 3169]
དེ་ལ་ནི་རྡུལ་ཕྲ་རབ་ཏུ་བཅོམ་ཡང་རུང་། བློས་རོ་ལ་སོགས་པའི་ཆོས་བསལ་ཡང་རུང་། གཟུགས་ཀྱི་རང་བཞིན་གྱི་བློ་འཇུག་པ་ཉིད་དོ། །

[Block 3170 [HEADING]]
#### དང་པོ་འཇུག་པ། ^6-1-3-0

[Block 3171]
བདེན་པ་དག་བཤད་ནས་ཇི་ལྟར་ན་དེ་དག་མཐོང་བར་འགྱུར་བ་དང་པོ་འཇུག་པ་ལས་བརྩམས་ཏེ་བརྗོད་པར་བྱའོ། །

[Block 3172 [VERSE]]
ཚུལ་གནས་ཐོས་དང་བསམ་ལྡན་པས། །
བསྒོམ་པ་ལ་ནི་རབ་ཏུ་སྦྱོར། །

[Block 3173]
བདེན་པ་རྣམས་མ་ཐོང་བར་འདོད་པས་དང་པོ་ཁོ་ནར་ཚུལ་ཁྲིམས་སྲུང་བར༌[^1243]བྱེད་དོ། །

[Block 3174]
དེའི་འོག་ཏུ་བདེན་པ༌[^1244]མཐོང་བ་དང་མཐུན་པའི་ཆོས་ཐོས་པ་འཛིན་པའམ་དོན་ཉན་པར་བྱེད་དོ། །

[Block 3175]
ཐོས་པས༌[^1245]ཕྱིན་ཅི་མ་ལོག་པར་སེམས་པར་བྱེད་དོ། །

[Block 3176]
བསམས༌[^1246]ནས་ཏིང་ངེ་འཛིན་བསྒོམ་པ་ལ་རབ་ཏུ་སྦྱོར་བར་བྱེད་དོ། །

[Block 3177]
དེ་དག་ཀྱང་།

[Block 3178 [VERSE]]
ཐེས་སོགས་ལས་བྱུང་བློ་རྣམས་ནི། །
མིང་དང་གཉིས་ཀ་དོན་ཡུལ་ཅན།[^1247] །

[Block 3179]
ཐོས་པ་ལས་བྱུང་པའི་ཤེས་རབ་ནི་མིང་ལ་དམིགས་པ་ཡིན་ལ། བསམས་པ་ལས་བྱུང་བ་ནི་མིང་དང་དོན་ལ་དམིགས་པ་ཡིན་ཏེ། རེས་འགའ་ནི་ཡི་གེས་དོན་འདྲེན་པར༌[^1248]བྱེད་དོ། །

[Block 3180]
རེས་འགའ་ནི་དོན་གྱིས༌[^1249]ཡི་གེ་འདྲེན་པར་བྱེད་དོ། །

[Block 3181]
བསྒོམས་པ་ལས་བྱུང་བའི་ཤེས་རབ་ནི་དོན་ལ་དམིགས་པ་ཁོ་ན་ཡིན་ཏེ། དེ་ནི་ཡི་གེ༌[^1250]ལ་མི་ལྟོས༌[^1251]པར་དོན་ལ་འཇུག་གོ། །

[Block 3182]
དེ་ལྟར་བསྒོམ་པ་ལ་རབ་ཏུ་བརྩོན་པ་དེ་ཇི་ལྟར་ན་བསྒོམ་པ་རྫོགས་པར་འགྱུར་ཞེ་ན། བསྲིངས་གཉིས་ལྡན། གལ་ཏེ་འདུ་འཛི་དང་མི་དགེ་བའི་རྣམ་པར་རྟོག་པ་ཐག་བསྲིངས་པའི་ཕྱིར་ལུས་དང་། སེམས་དག་གིས་བསྲིངས་པ་ཡིན་ན་རྫོགས་པར་འགྱུར་རོ། །

[Block 3183]
འོ་ན་བསྲིངས་པ་དེ་ཉིད་སུ་ལ་སླ་ཞེ་ན། འདོད་པ་ཆུང་བ་དང་། ཆོག་ཤེས་པ་ལ་སླའི། ཆོག་མི་ཤེས་པ་དང་།

[Block 3184 [VERSE]]
འདོད་ཆེན་ཅན་ལ་མ་ཡིན་ནོ། །
ཆོག་མི་ཤེས་པ་ནི་གང་ཞིག་ཡིན། །

[Block 3185]
འདོད་ཆེན་ཅན་ནི་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 3186 [VERSE]]
རྙེད་པ་ལ་སྲེད་ཆོག་མི་ཤེས། །
མ་རྙེད་ལ་འདོད་འདོད་ཆེན་ཅན། །

[Block 3187]
ཆོས་གོས་ལ་སོགས་པ་རྙེད་པ་ལ༌[^1252]ཡང་དང་ཡང་དུ་འདོད་པ་ནི་ཆོག་མི་ཤེས་པ་ཡིན་ལ། མ་རྙེད་པ༌[^1253]དག་ལ་དེ་འདོད་པ་ནི་འདོད་ཆེན་ཅན་ཡིན་ནོ། །

[Block 3188]
བཟློག་པ་དེ་ཡི་གཉེན་པོ་དག །ཆོག་ཤེས་པ་དང་འདོད་པ་ཆུང་བ་དག་གོ། །

[Block 3189]
དེ་གཉིས་ཁམས་གསུམ་གཏོགས་དྲི་མེད། །དེའི་གཉེན་པོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཆོག་མི་ཤེས་པ་དང་། འདོད་ཆེན་ཅན་ནི་འདོད་པ་ན་སྤྱོད་པ་ཁོ་ན་འདོད་ཆེན་ཆུང་བ་དང་། ཆོག་ཤེས་པ་འདི་གཉིས་ཀྱི་རང་བཞིན་ཅི་ཞེ་ན། མ་ཆགས་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་དག་ནི་མ་ཆགས་པའི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 3190]
འཕགས་རིགས། མ་ཆགས་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འདི་དག་ལས་འཕགས་པ་རྣམས་སྐྱེ་བས་ན་འཕགས་པའི་རིགས་བཞིའོ། །
--- END BLOCKS ---
