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
[Block 3116]
འདིར་སྦྱིན་པ་པོ་དང་མནོད་པ༌[^3021]པོས་ཀྱང་གཞན་དུ་བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་ལྟུང་བ་དང་ལྡན་པར༌[^3022]རིག་པར་བྱའོ། །

[Block 3117]
དགེ་འདུན་ཐམས་ཅད་ཀྱིས་གྲོས་བྱས་སམ་ལས༌[^3023]སུ་སྩལ༌[^3024]ཏེ་དེར་གནས་ཁང་སྦྱིན་པར་བྱེད་ན་ཡང་ཐམས་ཅད་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 3118]
འདིར་གནས་ཀྱི་གཞི་གཡོགས་པ་ནི་གཙུག་ལག་ཁང་ངོ་། །ཆོས་དང་འདུལ་བ་ལ་གལ་ཏེ་དེ་དང་ལྡན་པར་ཤེས་ནས་ཆོས་མ་ཡིན་པ་ལ་མངོན་པར་ཞེན་པ་ལ་དགེ་འདུན་མཐུན་པ་མེད་དོ་ཞེས་བྱ་བ་ལ་ཆོས་དང་ཞེས་བྱ་བ་ནི་དངོས་པོར་གཏོགས་པ་དང་སྤྱོད་པར་གཏོགས་པའི་ཆོ་གའོ། །

[Block 3119]
འདུལ་བ་ཞེས་བྱ་བ་ནི་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པ་དག་ལ་བྱས་པ་དང་མ་བྱས་པ་ཉིད་དོ། །

[Block 3120]
དེ་དང་ལྡན་པར་ཞེས་བྱ་བ་ནི་དེ་ལྟར་ཆོས་དང་འདུལ་བའི་རྣམ་པ་ལ་མི་མཐུན་པ་ཉིད་དང་ལྡན་པའོ། །

[Block 3121]
གལ་ཏེ་ཤེས་ནས་ཆོས་མ་ཡིན་པ་ལ་ཞེས་བྱ་བ་ནི།[^3025] ཆོས་མ་ཡིན་པ་ལ་མངོན་པར་ཞེན་པར་བྱེད་པ་དེ་ལ་དགེ་འདུན་མཐུན་པ་མེད་དོ། །

[Block 3122]
གང་གི་ཕྱིར་ཆོས་དང་འདུལ་བའི་ཕྱིར་དགེ་འདུན་མི་མཐུན་པ༌[^3026]ཡིན་གྱི། དོན་གཞན་གྱི་ཕྱིར་ནི་མ་ཡིན་པས་དེའི་ཕྱིར༌[^3027]མི་མཐུན་པ་ལ་ནི་དགེ་འདུན་མི་མཐུན་པ་བྱེད་པར་མི་རིགས་སོ། །

[Block 3123]
དེའི་ཕྱིར་དེ་ལས་གཞན་པ་དག་དང་ཚོགས་ཏེ་ལས་བྱས་ན་ཡང་མི་འཆགས༌[^3028]ལ་ཕན་ཚུན་མི་མཐུན་པ་ཉིད་དུ་ཡང་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་དགེ་འདུན་མཐུན་པ་མེད་པ་དེའི༌[^3029]ཕྱིར་ཆོས་མ་ཡིན་པ་ལ་མངོན་པར་ཞེན་པ་དེ་དག་དང་དེ་ལས་གཞན་པ་ཆོས་ཀྱི་ཕྱོགས་དང་མཐུན་པ་གཞན་དག་ལ་ཡང་བསྡུས་ཏེ་བྱས་པ་ལ་ལས་བྱས་ན་ཡང་མི་འཆགས་པ་དང་ཕན་ཚུན་མི་མཐུན་པའི་དངོས་པོར་མི་འགྱུར་རོ། །

[Block 3124]
དེ་དག་དེའི་མི་མཐུན་པའི་ཕྱོགས་དང་འཐབ་པར་གྱུར་པ་ཉིད་ན་ཆོས་འདི་པ་དག་གིས༌[^3030]ཕྱག་མི་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དེ་དག་ཅེས་བྱ་བ་ནི་ཆོས་མ་ཡིན་པ་ལ་མངོན་པར་ཞེན་པ་དེ་རྣམས་ལ་དེའི་མི་མཐུན་པའི་ཕྱོགས་ཆོས་དང་མཐུན་པའི༌[^3031]ཕྱོགས་སུ་གཏོགས་པ་དང་ལྷན་ཅིག་འཐབ་པར་འགྱུར་བ་ཉིད་ན་དེ་དག་ལ་ཆོས་འདི་པ་དགེ་སློང་དང་དགེ་སློང་མ་དང་དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་དང་དགེ་སློབ༌[^3032]མ་དང་དགེ་བསྙེན་དང་དགེ་བསྙེན་མ་རྣམས་ཀྱིས་ཕྱག་མི་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 3125]
མངོན་དུ་ལྡང་བ་དང་སྟན་ལ་བོད་པ་དང་། གཏམ་འདྲེ་བ་དང་། ཕེབས་པར་སྨྲ་བ་དང་། ཀུན་དགའ་བར་འགྱུར་བ་དང་རྣམ་པར་ལྟ་བ་དང་ཅུང་ཟད་ལྟ་བ་དག་ཀྱང་མི་བྱའོ། །

[Block 3126]
ལག་པའི་ཐ་སྙད་ཀྱིས་གནས་མལ་ངན་པ་རྗེས་སུ་སྦྱིན་ནོ། །

[Block 3127]
ཁ་ཅིག་ལས་ནི་ཚིག་གིས་ཐོས་པ་དང་བཅས་པར་གཞན་ལའོ་ཞེས་བྱ་བ་ནི་གཞུང་ཁ་ཅིག་ལས་ནི་ཆོས་མ་ཡིན་པ་ལ་མངོན་པར་ཞེན་པ་དེ་དག་འོངས་ན༌[^3033]ཚིག་གིས་ཅི་ནས་ཀྱང་དེ་དག་གིས་ཐོས་པ་དང་བཅས་པར་གང་ཟག་གཞན་ལ་བརྟེན༌[^3034]ཏེ་དེ་དག་འདི་ཙམ་ཐོབ་པོ་ཞེས་བྱ་བའི་ཚིག་གིས་གནས་མལ་ངན་པ་རྗེས་སུ་སྦྱིན་པར་བྱའོ་ཞེས་འབྱུང་ངོ་། །གཙུག་ལག་ཁང་འཇུག༌[^3035]ཏུའོ་ཞེས་བྱ་བ་ནི་སྦྱིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3128]
ཁོ་བོ་ཅག་རྒན་ནོ་ཞེས་ཟེར་ན་ཁྱེད་ཅག་ཀྱང་བདག་ཅག་ཤཱཀྱའི་སྲས་ཀྱི་དགེ་སློང་དག་ཡིན་ནོ་སྙམ་དུ་བདག་ཉིད་ཁས་འཆེའམ། [^3036]ཁྱེད་ཅག་གང༌[^3037]དག་གི་སྤྱོད་ཚུལ༌[^3038]འདི་ལྟ་བུ་དང་གཏམ་འདི་ལྟ་བུ༌[^3039]འདི་ཡང་མི་ཐོབ་པ་ཡིན་ན། ཁྱེད་ཀྱི་སྟོན་པ་ཐུགས་རྗེ༌[^3040]དང་ལྡན་པ་དེས་ན་འདི་རྗེས་སུ་གནང་ངོ༌[^3041]ཞེས་གཞན་ལ་ལན་གདབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི། དེ་དག་ལ་དངོས་སུ་ལན་མི་གདབ་པར་གང་ཟག་གཞན་ལ་བརྟེན་ཏེ་ལན་འདི་སྐད་གདབ་པར་བྱའོ༌[^3042]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3129]
སྤྱོད་ཚུལ་འདི་ལྟ་བུ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དེ་རྣམས་ཀྱིས༌[^3043]སྤྱད་པའི་སྤྱོད་པ་ལ་སོགས་པ་དེ་དག་བརྗོད་པར་བྱའོ། །

[Block 3130]
གཏམ་འདི་ལྟ་བུ་ལ་ཞེས་བྱ་བ་ནི་གང་ཞིག་སྤྱོད་ཚུལ་དེ་ལ་ཉེས་དམིགས་གང་བྱུང་བ་སྟེ། སྟོན་པ་གུང་དུ་གཤེགས་པ་ལ་སོགས་པ་གང་ཡིན་པ་དེ་དག་བརྗོད་པར་བྱའོ། །

[Block 3131]
དགེ་སློང་མ་ལ༌[^3044]སྟན་ལས་ལྡང་བ་དབྲི་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འཐབ་ཀྲོལ་བྱེད་པ་རྣམས་ལའོ། །

[Block 3132]
དགེ་བསྙེན་གྱིས༌[^3045]བསོད་སྙོམས་དབུལ་བར་བྱའོ། །

[Block 3133]
བཟོད་པར༌[^3046]བྱས་པ་དེ་དག་ལ་མཐུན་པ་ཐོབ་པ་མེད་པར་མཐུན་པ་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ལ་དེ་དག་ལ་ཞེས་བྱ་བ་ནི་ཆོས་མ་ཡིན་པ་ལ་མངོན་པར་ཞེན་པ་དེ་དག་ལའོ། །

[Block 3134]
བཟོད་པར་བྱས་པ་རྣམས་ལ་ཡང་བཟོད་པ་བྱས་སུ་ཟིན་ཀྱང་མཐུན་པ་སྦྱིན་པ་ཐོབ་པ༌[^3047]མེད་པར་མཐུན་པ་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 3135]
གསོ་སྦྱོང་མེད་པར་རང་བཞིན་དུ་གནས་པ་ཉིད་མི་ཐོབ་བོ་ཞེས་བྱ་བ་ནི་མཐུན་པ་ཐོབ་ཏུ་ཟིན་ཀྱང་ཇི་སྲིད་དུ་དགེ་འདུན་ལས་མཐུན་པའི་གསོ་སྦྱོང་མ་གསོལ་ཞིང་མཐུན་པའི་གསོ་སྦྱོང་མ་ཐོབ་ཀྱི་བར་དུ་རང་བཞིན་དུ་གནས་པ་ཉིད་མི་འཐོབ་སྟེ། ཆོས་དང་ཟང་ཟིང་གི་ལོངས་སྤྱོད་གཉིས་ཀྱི༌[^3048]འོས་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3136]
མཐུན་པའི་གསོ་སྦྱོང་ཞེས་བྱ་བའི་དོན་དང་མཐུན་པ༌[^3049]ཡིན་ཏེ། [^3050]གསོ་སྦྱོང་ཞེས་བྱ་བའི་དོན་ནི་གང་ཞིག་འདི་ལ་འཐབ་ཀྲོལ་ལ་མངོན་པར་སྤྱོད་པ་ཉིད་ཀྱི་ཕྱིར་ངེས་པར་སྤྱོད་པ༌[^3051]ལ་མངོན་པར་གནས་པ་སྤང་བར་བྱ་བ་ཉིད་དོ། །

[Block 3137]
ཐ་དད་པའི་དངོས་པོ་ལ་ཡང་ཐ་དད་པའི་བློ་ལ་མངོན་པར་ཞེན་པར་གནས་པས་རང་བཞིན་དུ་མི་གནས་པ་ཉིད་དོ། །

[Block 3138]
དེ་ལྟ་བས་ན་མཐུན་པ་རྙེད་པ་དང་མཐུན་པའི་གསོ་སྦྱོང་དག་མེད་པར་ཡང་མི་བྱ་བ་ཉིད་ལ། རང་བཞིན་དུ་གནས་པ་དག་དང་དེ་མི་འགྲུབ་པས་དེའི་ཕྱིར་དེ་བརྟེན༌[^3052]པའོ། །

[Block 3139]
དེ་བྱིན་ནས་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བྱ་ནི་གསོ་སྦྱོང་སྟེ། དེ་བཞིན་མི་བྱ་བར་འོན་ཀྱང་བྱིན་ནས་བཟོད་པར་བྱའོ། །

[Block 3140]
དེ་ནི་ལས་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་གསོ་སྦྱོང་བྱིན་པ་དེ་ནི་ལས་ཀྱིས་ཏེ། དེ་ཐམས་ཅད་ཉིད་ཀྱིས་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3141]
སྔ་མ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མཐུན་པ་སྦྱིན་པ་ཞེས་བྱ་བ་བསྟན་པ་དེ༌[^3053]ཡང་ལས་ཀྱིས་ཏེ་དེ་བཞིན་དུ་མཐུན་པ་སྦྱིན་པ་དང་མཐུན་པའི་གསོ་སྦྱོང་སྦྱིན་པ་དེ་དག་ལ་ལས་ཀྱིས་སྦྱིན་པ་དང་། གསོལ་བའི་ལས་ཀྱིས༌[^3054]སྦྱིན་པ་དང་རྣམ་པར་གཞག་པ་ལས་གསོལ་བའི་ལས་སྔོན་དུ་འགྲོ་བ་ཉིད་དུ་ཤེས་པར་བྱའོ། །

[Block 3142]
མཐུན་པ་དང་བཀྲ་ཤིས་དང་གནོད་པ་བྱུང་བའི་དོན་དུ་གསོ་སྦྱོང་བྱར་རུང་ངོ་ཞེས་བྱ་བ་ནི་གཞན་འདི་རྣམས་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པ་སྦྱིན་པའི་རྒྱུད་ཀྱིས་གསོ་སྦྱོང་ཞེས་བྱ་བ་འདི་ལས་སུ་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་པས་སོ། །

[Block 3143]
བྱ་བ་རྣམས་ཀྱི་མཐུན་པ་སྒྲུབ་པའི་ཕྱིར་མཐུན་པའི་གསོ་སྦྱོང་བྱར་རུང་བ་ཡིན་ཏེ། བཀྲ་ཤིས་ཀྱི་དོན་དང་ཆོས་དང་འདུལ་བའི་སྐབས་སམ་དགེ་འདུན་བདེ་བའི་སྐབས་སུ་ཅུང་ཟད་བཀྲ་མི་ཤིས་པ༌[^3055]ཉེ་བར་ཞི་བ་མཐོང་ནས་གསོལ་བ་བསྒྲུབ་པའི༌[^3056]དོན་དུ་འདི༌[^3057]བྱེད་པའོ། །

[Block 3144]
གནོད་པ་ཡང་དག་པར་བསྡུམ་པར་བྱ་བའམ་དོགས་པར་གྱུར་པ་ལ་དེ་དག་ཉེ་བར་ཞི་བར་བྱ་བའི༌[^3058]དོན་དུ་གྲོང་ཁྱེར་ཡངས་པ་ཅན་དུ་གང་དག་སྡུད་པར་བྱེད་པ་ན། གསོ་སྦྱོང་བྱས་པ་གང་ཡིན་པ་དེ་ནི་མི་རུང་བའི་གཞི་བཅུ་བྱུང་བ་དེ་དག་ཉེ་བར་ཞི་བར་བྱ་བའི་ཕྱིར་ཏེ། ཆོས་དང་འདུལ་བ་ཀུན་ནས་འཁྲུག་པ་མཐོང་བས་ཞེས་བྱ་བར༌[^3059]རིག་པར་བྱའོ། །

[Block 3145]
བཀྲ་མི་ཤིས་པ་ཉེ་བར་ཞི་བར་བྱ་བའི་དོན་དུ་འདི་བྱེད་པ་རིགས་པ༌[^3060]ཡིན་ཏེ། ཉེ་བར་འཚེ་བ་མ་ཞི་བ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3146]
དེ་ལྟར་ཡང་གྲོང་ཁྱེར་ཡངས་པ་ཅན་དུ་བྱས་པའོ། །

[Block 3147]
འདི་ལ་དུས་ནི་དེ་ཁོ་ནའི་རྒྱུ་ཉིད་དུའོ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་བྱེད་པ་འདི་ལ་དེ་དག་ཚེས་བཅུ་བཞི་པའམ་བཅོ་ལྔའི་དུས་མ་ཡིན་མོད་ཀྱི། འོན་ཀྱང་མཐུན་པ་ལ་སོགས་པ་དེ་དག་གི་དུས་ཡིན་པའི་དུས་དེ་ཁོ་ནའི་རྒྱུ་ཉིད་དུ་བྱ་བ་ཡིན་ནོ། །

[Block 3148]
འདིར་གཞུང་ནི་ཉེ་བ༌[^3061]འཁོར་གསོ་སྦྱོང་ལྔ་པོ་འདི་དག་ཡིན་ཏེ་བཅུ་བཞི་པ༌[^3062]དང་། བཅོ་ལྔ་པ་དང་། བཀྲ་ཤིས་ཀྱི་གསོ་སྦྱོང་དང་། གནོད་པ་བྱུང་བའི་གསོ་སྦྱོང་དང་། མཐུན་པའི་གསོ་སྦྱོང་ངོ་། །དགེ་སློང་གིས་གསོ་སྦྱོང་མ་ཡིན་པར༌[^3063]གསོ་སྦྱོང་མི་བྱའོ། །

[Block 3149]
བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ། །

[Block 3150]
བཀྲ་ཤིས་ཀྱི་གསོ་སྦྱོང་བྱ་བ་དང་གནོད་པ་བྱུང་བའི་གསོ་སྦྱོང་དང་མཐུན་པའི་གསོ་སྦྱོང་ནི་མ་གཏོགས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3151]
ལས་བྱེད་པའི༌[^3064]གཞིའོ།། །།

[Block 3152]
ཆོས་མ་ཡིན་པ་སྨྲ་བ་དག་གིས་དབྱེ་བའི་སེམས་ཀྱིས་མཚམས་ཀྱི་ནང་དུ་ལས་ཐ་དད་པ་བྱས་ན་བྱེ་བ༌[^3065]ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ནང་དུ་བཅས་པ་འདི་རྣམས་བདག་ཅག་ལ་ནི་ཅི་དགོས། འདི་རྣམས་ཁོ་བོ་ཅག་ལས་ཐ་དད་པར་གྱུར་ཅིག་སྙམ་དུ་དབྱེ་བའི་སེམས་ཀྱིས་ཆོས་སྨྲ་བ་རྣམས་ཀྱི༌[^3066]མཚམས་ཀྱི་ནང་དུ་ཆོས་མ་ཡིན་པ་སྨྲ་བ་དག་ལས་ཐ་དད་པའི་ལས་བྱས་པ་ལས་དེ་བྱེ་བ་ནི་ལས་བྱེ་བ་ཞེས་བྱ་བའི་དོན་ནོ། །

[Block 3153]
འདིར་གཞུང་ནི་སིལ་བུ་དག་གིས་ཀཽ་ཤཱམྦཱི་པའི་དགེ་འདུན་ཕྱེ་བར་འགྱུར། [^3067]ཆོས་མ་ཡིན་པ་དག་གིས་མཚམས་ཀྱི་ནང་དུ་གསོ་སྦྱོང་མ་འདྲེས་པར་བྱས་པས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3154]
ཡང་ན༌[^3068]ཆོས་སྨྲ་བ་རྣམས་ཀྱིས་ཆོས་མ་ཡིན་པ་སྨྲ་བའི་ཕྱོགས་དག་ལ༌[^3069]ཐ་དད་པར་བྱས་པ་ནི་མཚམས་ཀྱི་ནང་དུ་ལས་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 3155]
ཆོས་ལས་མི་གཡོ་བ་དེ་རྣམས་ཀྱིས་དེ༌[^3070]བྱས་པས་གནས་ནས་དབྱུང་བ་རྣམ་པ་དེས་ཆོས་མ་ཡིན་པ་སྨྲ་བ་རྣམས་ལ་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
