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
བདག་བྱིན༌[^2028]གྱིས་རློབ་པའི་རིམ་པའི་རྣལ་འབྱོར་པས་བར་བར་དུ་སེམས་རྣམ་པར་དག་པ་ཡང་མངོན་དུ་བྱ་བའི་ཕྱིར། ཥྱ། འདི་ལ་སྣང་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་གསུམ་པོ་མཚམས་ལ་སོགས་པའི་སྒྲས་ཐ་སྙད་དུ་བྱའོ། །

[Block 3117]
འཇིག་རྟེན་ན་མཚམས་ལ་སོགས་པ་གཞན་མེད་དེ་ཡེ་ཤེས་གསུམ་དུ་མཐོང་བའི་ཕྱིར་རོ་ཞེས་པ་ལ། འཇུག་པའི༌[^2029]རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་བཟློག་པས་སྤངས་པའི་ཕྱིར་རོ། །

[Block 3118]
དེ་དང་དེའི་རྗེས་སུ་མཐུན་པ་སྣང་བ་གསུམ་བཞིན་དུ་ཕྱིའི་མཚམས་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པ་བརྫུན་པ་ཉིད་དོ། །

[Block 3119]
འདས་པ་ལ་སོགས་པ་ཡང་ཡེ་ཤེས་གསུམ་གྱི་རྣམ་པར་དག་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཝི། སྣ་ཚོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། སྣ་ཚོགས་པ་ཡི་ཐ་སྙད་ནི། །ལུས་དང་ངག་དང་ཡིད་ཀྱི་བྱ་བ་སྟེ། སྤྱོད་ལམ་བཞིའི་མཚན་ཉིད་ཅན་དེ་དག་ཆགས་པ་དང་བྲལ་བ་ལ་སོགས་པའི་རང་བཞིན་གྱི་དབྱེ་བས་སྣ་ཚོགས་ཅན་ཏེ། དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་ཞེས་བྱ་བའི་བར་རོ། །

[Block 3120]
འཇིག་རྟེན་པས་ནི་ཡོངས་བརྟགས་པ། །ཞེས་པས་ནི་སོ་སོའི་སྐྱེ་བོས་བརྟགས་པ༌[^2030]གང་ཡིན་པ་དེ་དག་དུས་གསུམ་གྱི་དབྱེ་བས་ནི། ཡེ་ཤེས་རྣམ་པ་གསུམ་ལས་འབྱུང་། །ཞེས་རིག་པར་བྱའོ། །

[Block 3121]
དེ་ལྟར་ཡིན་ན། ཡེ་ཤེས་གསུམ་ལྟར་སྤང་བར་བྱ། །ཞེས་ཐ་ཚིག་གོ། །

[Block 3122]
སྐྱེ་བ་ལ་སོགས་པ་ཡང་དེའི་ངོ་བོ་ཡིན་ཞེས་བསྟན་པར་བྱ་བའི་ཕྱིར། ཛ། སྐྱེ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདུས་བྱས་པའི་མཚན་ཉིད་གསུམ་སྟེ། སྐྱེ་བ་དང་གནས་པ་དང་འཇིག༌[^2031]པའོ། །

[Block 3123]
དེ་བཞིན་དུ་ཡང་སྲིད་པ་བར་མ་ན་གང༌[^2032]དུ་བསྟན་ཏོ། །

[Block 3124]
ཇི་སྙེད་འཇིག་རྟེན་གྱིས་བརྟགས་པ། །ཞེས་པ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡང༌[^2033]ཡན་ལག་བཅུ་གཉིས་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པའོ། །

[Block 3125]
སེམས་ཀྱི་རླུང་གི་རྣམ་འཕྲུལ་ལོ།[^2034] །

[Block 3126]
ཞེས་པ་ནི་དེ་དག་ཐམས་ཅད་རྣམ་པར་ཤེས་པའི་རླུང་གི་རྒྱུ་ལས་ཀུན་དུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3127]
དེ་ལྟར་ཤེས་ནས་དེ་དག་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་འབད་པར་བྱའོ། །

[Block 3128]
སླར་ཡང་བདག་བྱིན་གྱིས་རློབ་པར་བྱ་བའི་ཕྱིར། ཧ། དགོད་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དགོད་པ་ནི་སྒེག་པའི་རོའི་བྱེ་བྲག་གོ། །

[Block 3129]
རྩེད་མོ་ནི་གར་དང་གླུ་དང་རོལ་མོ་ལ་སོགས་པའོ། །

[Block 3130]
དེ་བཞིན་དུ་ཡང་གར་གྱི་རོ་དགུ་ཞེས་པ་ནི་སྔོན་དུ་བཤད་པའོ། །

[Block 3131]
ལྡན་པ་ནི་དེའི་ཡན་ལག་ཏུ་གྱུར་པའི་ཐ་སྙད་དོ། །

[Block 3132]
དེ་བཞིན་དུ་ཕྱག་རྒྱ་ནི་ལག་པ་དང་རྐང་པ་དང་རྐེད་པ་དང་མགྲིན་པ་ལ་སོགས་པའི་ཡན་ལག་གི་ཁྱད་པར་གྱི་བྱ་བའི་མཚན༌[^2035]ཉིད་དོ། །

[Block 3133]
སྔགས་ནི་ཞི་བ་དང་ཁྲོ་བ༌[^2036]དང་གཉི་ག་མ་ཡིན་པའི་ངག་གིས་བརྗོད་པར་གྱུར་པའོ། །

[Block 3134]
རྣམ་པར་རྟོག་པ་ནི་སེམས་ལས་བྱུང་བ་རྩེ་གཅིག་པ་ལ་སོགས་པའོ། །

[Block 3135]
རྡོ་རྗེ་སེམས་དཔའི་རྣམ་འཕྲུལ་ཞེས་པ་ནི་དེ་དག་ཐམས་ཅད་སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ལས་རྣམ་པར་འཕྲུལ་པ་སྟེ། འབྱུང་ངོ༌[^2037]ཞེས་རྣལ་འབྱོར་པས་ཤེས་པར་བྱའོ། །

[Block 3136]
དེ་ལྟར་ཤེས་པས་ཏིང་ངེ་འཛིན་དེ་ལ་ལེགས་པར་གནས་པར་འགྱུར་རོ། །

[Block 3137]
ཉེ་བར་སྡུད་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། ར། [^2038]བདག་བྱིན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། བདག་བྱིན་གྱིས་རློབ་པའི་རིམ་པ་སྤངས་ཏེ། རིན་པོ་ཆེ་གཞན་ནི་འགྲོ་བ་ཐམས་ཅད་ཀྱི་རེ་བ་རྫོགས་པར་བྱེད་པ་ཡོད་པ་མ་ཡིན་ཏེ། གང་གི༌[^2039]ཕྱིར་བསྐྱེད་པའི་རིམ་པའི་སྔགས་ཀྱི་སྐུས་རེ་བ་རྫོགས་པར་བྱེད༌[^2040]མི་ནུས་ཏེ། བརྟགས་པ༌[^2041]བ་ཡིན་པའི༌[^2042]ཕྱིར་རོ། །

[Block 3138]
རྫོགས་པའི་རིམ་པའི་སེམས་རྣམ་པར་དག་པ་དང་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་དག་གིས་འགྲོ་བའི་དོན་ཡང་མི་འགྲུབ་སྟེ། འོད་གསལ་བ་ཙམ་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3139]
རྡོ་རྗེ་བཟླས་པའི་རིམ་པས་ཀྱང་སེམས་ཅན་གྱི་དོན་མེད་དེ། རླུང་ལ་དབང་བ་ཙམ༌[^2043]ཐོབ་པས་སོ། །

[Block 3140]
དེའི་ཕྱིར་འགྲོ་བའི་དོན་ལ་བདག་བྱིན་གྱིས་རློབ་པ་ཁོ་ན་མཆོག་ཡིན་ནོ། །

[Block 3141]
སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ལ་མངོན་པར་ཞེན་པ་བརྒྱལ་སྲིད་པས་དེ་དགག་པར་བྱ་བའི་ཕྱིར། རིམ་པ་བཞི་བསྒོམ་པར་བྱ་བ་ཡིན་ཞེས་ཟུར་གྱིས་མཐར་ཐུག་པའི་ཕྱོགས་གཅིག་པ་འོད་གསལ་བ་ལ་འཇུག་པར་བྱ་བའི་ཕྱིར། །མེས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། རིམ་པ་བཞི་པས་ཐོབ་པའི་འོད་གསལ་བས་གལ་ཏེ་བདག་བྱིན་གྱིས་རློབ་པའི་སྐུ་དག་པར་འགྱུར་ན། དེའི་ཚེ་མེས་སྦྱངས་པའི་གསེར་བཞིན་དུ་རྣམ་པར་དག་པ་དྲི་མ་མེད་ཅིང་སྤྲོས་པ་མེད་པར་འགྱུར་རོ། །

[Block 3142]
དེའི་ཕྱིར་རིམ་པ་བཞི་པ༌[^2044]ཡང་། སྒོམ་པར་བྱེད་པར་རིག་པ་ཁོ་ནའོ། །

[Block 3143]
ཡང༌[^2045]ཚད་མ་ཉིད་དུ་བསྟན་པར་བྱ་བའི་ཕྱིར། དཔལ་ལྡན་འདུས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། །རྡོ་རྗེ་ཕྲེང་བ་ཞེས་བྱ་བའི་བཤད་པའི་རྒྱུད་ལས་བཅོམ་ལྡན་འདས་འཇམ་པའི་དབྱངས་ཀྱིས་ཁྲོ་བོའི་རྒྱལ་པོ་གཤིན་རྗེ་གཤེད་ལ་བཞུགས་པའི་ཚིག་དོན་ནི་གླེང་གཞིའི་ཚིག་དོན་བཤད་པ་ཡིན་ཞེས་པ་ནི་དེ་ལྟར་གཏན་ལ་དབབ་པར་བསྟན་པའོ། །

[Block 3144]
སྦས་པ་ཞེས་པ་ནི་བཤད་པའི་ཁྱད་པར་རོ། །

[Block 3145]
དེ་ནས།[^2046] དོན་འདི་ཡིན་ཏེ། འདོད་ཆགས་ཀྱི་ཆོས་བསྟན་པའི་སྒོ་ནས་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་དང་ཡེ་ཤེས་གསུམ་བརྟགས་པའི་སྒོ་ནས་སེམས་ལ་རྣམ་པར་རྟོག་པའི་རིམ་པ་དང་། ཀུན་རྫོབ་ཀྱི་བདེན་པ་རྟོགཔའི༌[^2047]སྒོ་ནས་བདག༌[^2048]བྱིན་གྱིས་རློབ་པའི་རིམ་པ་བསྟེན་ཞེས༌[^2049]སྦས་པས་རིམ་པ་གསུམ་སོ་སོར་བསྟན་ཏོ། །

[Block 3146]
ཡང་ལུང་གིས་བཤད་པ་གསུངས་པ་ཞེས་བྱ་བ་འདིས་རིམ་པ་ཐ་མ་གཉིས་པོ་སྟོན་པར་བྱེད་པ་མཐར་ཐུག་པ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། རྒྱུད་འདི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདི་སྐད་བདག་གིས་ཐོས་ཞེས་སྡུད་པ་པོའི་ཚིག་གསལ་བ་ཁོ་ནའོ། །

[Block 3147]
གསལ་བ་འགའ་ཞིག་དུས་ཡིན་ཏེ། ཞེས་པ་ནི་སྙོམས་པར་ཞུགས་པའི་དུས་སུ་བཅོམ་ལྡན་འདས་ཀྱི་ཁྱད་པར་རོ། །

[Block 3148]
རྡོ་རྗེ་གསང་བ་བཅོམ་ལྡན་འདས་ཞེས་པ་ནི་གསང་བའི་རྡོ་རྗེ་ནི་རྟགས་བསྟན་པའོ། །

[Block 3149]
དེའི་དབང་ཕྱུག་ནི་སྙོམས་པར་ཞུགས་པའི་དབང་གིས་བདེ་བ་ཐོབ་པའོ། །

[Block 3150]
རྡོ་རྗེ་གསུམ་པོ་དམ་ཚིག་མཆོག །ཅེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་གསུང་ཐུགས་ཞེས་འདི་བཤད་པའོ། །

[Block 3151]
དེས་ན་དོན་འདི་ཡིན་ཏེ། རྡོ་རྗེ་གསུམ་ནི་སྐུ་ལ་སོགས་པའོ། །

[Block 3152]
དེ་རྣམས་ཀྱི་དམ་ཚིག་ནི་དབྱེར་མེད་པར་ཡོངས་སུ་ཤེས་པའོ། །

[Block 3153]
དེས་མཆོག་ཅེས་པ་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པ་བཅོམ་ལྡན་འདས་ཀྱི་ཁྱད་པར་རོ། །

[Block 3154]
ཡེ་ཤེས་དེ་བཞིན་གཤེགས་པ་ཀུན། །ཞེས་པ་ནི་རྡོ་རྗེ་གསུམ་ནི་བཙུན་མོའི་བྷ་གའི་ཁྱད་པར་རོ། །

[Block 3155]
དེ་བཞིན་གཤེགས་པ་ཀུན་ནི་ཕུང་པོ་ལྔའི་ཡེ་ཤེས་ཏེ། རོ་གཅིག་པ་ཉིད་དུ་རྟོགས་པ་ནི་འོད་གསལ་བའོ། །
--- END BLOCKS ---
