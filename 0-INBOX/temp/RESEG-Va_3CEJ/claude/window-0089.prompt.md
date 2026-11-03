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
གང་དེ༌[^1781]དག་རེག་པ་ནི་འདུས་པ་ལས་གཞན་ནོ་ཞེས་ཟེར་བ་དེའི༌[^1782]ཆོས་གསུམ་པོ་འདི་དག་འབྲེལ་ཞིང་འདུས་ལ་ཚོགས་པ་གང་ཡིན་པ་དེ་ནི་རེག་པ་ཡིན་ནོ་ཞེས་གསུངས་པའི་མདོ་འདི་ལ་ཇི་ལྟར་ལན་འདེབས་ཤེ་ན། དེ་སྐད་དུ་མི་འདོན་ཏོ། །

[Block 3117]
ཡང་ན་ནི་འདི་རྒྱུ་ལ་འབྲས་བུ་བཏགས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3118]
བརྗོད་པ་འདི་རྒྱ་ཆེ་བའི་རྣམ་པ་ཧ་ཅང་མང་པོར་འཕྲོ་བ་ཡིན་པས་ཞར་ལ་འོངས་པས་ཆོག་གོ། །

[Block 3119]
ཆོས་མངོན་པ༌[^1783]རྣམས་ན་རེ་རེག་པ་གཞན་ཁོ་ན་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3120 [VERSE]]
རེག་པ་དྲུག་པོ་དེ་དག་ལས། །
ལྔ་ནི་ཐོགས་པའི་རེག་པ་ཡིན། །
དྲུག་པ་བླ་དགས་ཚིག་ཅེས་བྱ། །

[Block 3121]
མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་ཀྱི་འདུས་ཏེ་རེག་པ་ལྔ་ནི་ཐོགས་པ་དང་བཅས་པའི་དབང་པོ་ལ་བརྟེན་པའི་ཕྱིར་ཐོགས་པའི་རེག་པ་ཞེས་བྱའོ། །

[Block 3122]
དྲུག་པ་ཡིད་ཀྱི་འདུས་ཏེ་རེག་པ་ནི་ཚིག་བླ་དགས་ཀྱི་རེག་པ་ཞེས་བྱའོ། །ཅིའི་ཕྱིར་ཞེ་ན། ཚིགས་བླ་དགས་ཞེས་བྱ་བ་ནི་མིང་ཡིན་ནོ། །

[Block 3123]
དེ་ལྷག་པར་འདིའི་དམིགས་པ་ཡིན་པས། དེའི་ཕྱིར་ཚིག་བླ་དགས་ཀྱི་འདུས་ཏེ་རེག་པ་ཞེས་བྱའོ་ཞེས་གྲག་སྟེ། ཇི་སྐད་དུ་མིག་གི་རྣམ་པར་ཤེས་པས་ནི་སྔོན་པོ་རྣམ་པར་ཤེས་ཀྱི་སྔོན་པོའོ་ཞེས་བྱ་བར་ནི་རྣམ་པར་མི་ཤེས་སོ། །

[Block 3124]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས་ནི་སྔོན་པོ་ཡང་རྣམ་པར་ཤེས་ལ་སྔོན་པོའོ་ཞེས་བྱ་བར་ཡང་རྣམ་པར་ཤེས་སོ་ཞེས་གསུངས་པ་ལྟ་བུ་སྟེ། གཅིག་ནི་རྟེན་གྱིས་རབ་ཏུ་ཕྱེ་བ་ཡིན་ནོ། །

[Block 3125]
གཉིས་པ་ནི་དམིགས་པས་རབ་ཏུ་ཕྱེ་བ་ཡིན་ནོ། །

[Block 3126]
གཞན་དག་ན་རེ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ནི་ཚིག་གི་དབང་དུ་བྱས་ནས་དོན་རྣམས་ལ་འཇུག༌[^1784]གི་ལྔ་པོ་དག་ནི་མ་ཡིན་ཏེ། དེའི་ཕྱིར་དེ་ནི་ཚིག་བླ་དྭགས་ཡིན་ནོ། །

[Block 3127]
དེ་དང་མཚུངས་པར་ལྡན་པའི་རེག་པ་ནི་ཚིག་བླ་དགས་ཀྱི་རེག་པ་ཞེས་བྱ་བས་གཅིག་ནི་རྟེན་གྱིས་རབ་ཏུ་ཕྱེ་བ་ཡིན་ནོ། །

[Block 3128]
གཉིས་པ་ནི་མཚུངས་པར་ལྡན་པས༌[^1785]རབ་ཏུ་ཕྱེ་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3129]
ཡང་རེག་པ་དྲུག་པོ་དེ་དག་ཉིད་གསུམ་དུ་འགྱུར་ཏེ། རིག་དང་མ་རིག་དང་གཞན་རེག །རིག་པའི་རེག་པ་དང་། མ་རིག་པའི་རེག་པ་དང་། དེ་གཉིས་ལས་གཞན་པ་རིག་པ་ཡང་མ་ཡིན་མ་རིག་པ་ཡང་མ་ཡིན་པའི་རེག་པའོ། །

[Block 3130]
དེ་དག་ཀྱང་གོ་རིམས་བཞིན་དུ། དྲི་མེད་ཉོན་མོངས་ཅན་ལྷག་མ། །ཡིན་པར་རིག་པར་བྱ་སྟེ། རིག་པའི་རེག་པ་ནི་ཟག་པ་མེད་པའི་རེག་པའོ། །

[Block 3131]
མ་རིག་པའི་རེག་པ་ནི་ཉོན་མོངས་པ་ཅན་གྱི་རེག་པ་སྟེ། རིག་པ་དང་མ་རིག་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རོ། །

[Block 3132]
ལྷག་མ་ནི་གཉིས་ཀ་དང་མཚུངས་པར་མི་ལྡན་པའི་ཕྱིར་རིག་པ་ཡང་མ་ཡིན་མ་རིག་པ་ཡང་མ་ཡིན་པའི་རེག་པའོ། །

[Block 3133]
ལྷག་མ་ཡང་གང་ཞིག་ཅེ་ན། དགེ་བ་ཟག་པ་དང་བཅས་པ་དང་། མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའོ། །

[Block 3134]
མ་རིག་པའི་རེག་པ་ཡང་དང་ཡང་དུ་ཀུན་ཏུ་འབྱུང་བའི་ཕྱོགས་གཅིག་སྨོས་པས་རེག་པ་གཉིས་སུ་འགྱུར་ཏེ། གནོད་སེམས་རྗེས་སུ་ཆགས་པའི་རེག །གནོད་སེམས་དང་། རྗེས་སུ་ཆགས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རོ། །

[Block 3135]
ཡང་ཐམས་ཅད་བསྡུ་ན། བདེ་བ་མྱོང་འགྱུར་ལ་སོགས་གསུམ། །བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པ་དང་། སྡུག་བསྔལ་མྱོང་བར་འགྱུར་བ་དང་། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ༌[^1786]ཡང་མ་ཡིན་པ་མྱོང་བར་འགྱུར་བ་སྟེ། བདེ་བ་མྱོང་བར་འགྱུར་བ་ལ་སོགས་པ་དང་རྒྱུ༌[^1787]མཐུན་པའི་ཕྱིར་རོ། །

[Block 3136]
ཡང་ན་དེ་མྱོང་བར་བྱ་བའམ། མྱོང་བར་ནུས་པའི་ཕྱིར་མྱོང་བར་འགྱུར་བ་སྟེ། དེ་གང་ཞེ་ན། ཚོར་བ་ཡིན་ནོ། །

[Block 3137]
འདི་ལ་བདེ་བ་མྱོང་བར་འགྱུར་བ་ཡོད་པས་ན་བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པ་སྟེ། གང་ལ་བདེ་བའི་ཚོར་བ་ཡོད་པའོ། །

[Block 3138]
དེ་བཞིན་དུ་སྡུག་བསྔལ་བ་དང་། བདེ་བ་ཡང་མ་ཡིན་པའི༌[^1788]སྡུག་བསྔལ་བ༌[^1789]ཡང་མ་ཡིན་པ་མྱོང་བར་འགྱུར་བ་དག་ལ་ཡང་སྦྱར་བར་བྱ་སྟེ། དེ་དག་ནི་རེག་པ་བཅུ་དྲུག་ཡིན་ནོ། །

[Block 3139]
རེག་པ་བཤད་ཟིན་ཏོ། །

[Block 3140 [HEADING]]
##### ཚོར་བ། ^3-1-11-13-0

[Block 3141 [HEADING]]
###### ཚོར་བ་མདོར་བཤད་པ། ^3-1-11-13-1-0

[Block 3142]
ཚོར་བ་བཤད་པར་བྱ་སྟེ། དེ་ལ་རེག་པ་རྣམ་པ་དྲུག་སྔར་བཤད་པ་གང་ཡིན་པ། དེ་ལས་བྱུང་བའི་ཚོར་བ་དྲུག །མིག་གི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བ་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་དང་། ཡིད་ཀྱི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བའོ། །

[Block 3143]
དེ་དག་ལས།

[Block 3144]
ལྔ་ནི་ལུས་ཀྱིའོ་སེམས་ཀྱི་གཞན། །མིག་དང་། རྣ་བ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་ཀྱི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བ་ལྔ་ནི་དབང་པོ་གཟུགས་ཅན་ལ་བརྟེན་པའི་ཕྱིར་ལུས་ཀྱི་ཚོར་བ་ཞེས་བྱའོ། །

[Block 3145]
ཡིད་ཀྱི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བ་ནི་སེམས་ཙམ་ལ་བརྟེན་པའི་ཕྱིར་སེམས་ཀྱི་ཞེས་བྱའོ། །

[Block 3146]
ཡང་ཅི་ཚོར་བ་རེག་པའི་འོག་ཏུ་འབྱུང་ངམ། འོན་ཏེ་དུས་མཉམ་དུ་འབྱུང་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ཕན་ཚུན་དུ་ལྷན་ཅིག་ཏུ༌[^1790]འབྱུང་བའི་རྒྱུ་ཡིན་པའི་ཕྱིར་དུས་མཉམ་མོ་ཞེས་ཟེར་རོ། །

[Block 3147]
ཇི་ལྟར་ན་ལྷན་ཅིག་འབྱུང་བ་གཉིས་སྐྱེད་པར་བྱེད་པ་དང་བསྐྱེད་པར་བྱ་བའི་དངོས་པོར་འགྲུབ། ཇི་ལྟར་མི་འགྲུབ་མཐུ་མེད་པའི་ཕྱིར་ཏེ། ཆོས་སྐྱེས་ཟིན་པ་ལ་ནི་ཆོས་ཀྱི་ནུས་པ་མེད་དོ། །

[Block 3148]
ལྷན་ཅིག་འབྱུང་བ་ཉིད༌[^1791]སྐྱེད་པར་བྱེད་པ་དང་བསྐྱེད་པར་བྱ་བའི་དངོས་པོ་མེད་དོ་ཞེས་བྱ་བ་གང་ཡིན་པ་དེ་ཉིད་ཆོས་སྐྱེས་ཟིན་པ་ལ་ནི་ཆོས་ཀྱི་ནུས་པ་མེད་དོ་ཞེས་བྱ་བ་ཡིན་པས་དམ་བཅས་པ་དང་བྱེ་བྲག་ཏུ༌[^1792]མེད་པ་ཡིན་ནོ། །

[Block 3149]
འོ་ན་ནི་ཕན་ཚུན་དུ་སྐྱེས༌[^1793]པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 3150]
འདོད་པའི་ཕྱིར་ཉེས་པ་མེད་དེ། ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ལ་ཕན་ཚུན་གྱི་འབྲས་བུ་ཉིད་དུ་མི་འདོད་པ་ཁོ་ནའོ། །

[Block 3151]
འདི་ནི་འདོད་མོད་ཀྱི་རེག་པ་དང་ཚོར་བ་དག་ཕན་ཚུན་ནམ༌[^1794]འབྲས་བུ་ཉིད་དུ་འདོད་པ་འདི་ནི་མདོ་ལས་མི་བཞེད་དེ། མིག་གི་འདུས་ཏེ་རེག་པ་ལ་བརྟེན་ནས་མིག་གི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི༌[^1795]ཚོར་བ་སྐྱེའོ། །

[Block 3152]
[^1796]མིག་གི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བ་ལ་བརྟེན་ནས་མིག་གི༌[^1797]འདུས་ཏེ་རེག་པ་སྐྱེ་བ་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3153]
སྐྱེད་པར་བྱེད་པའི་ཆོས་དང་འགལ་བའི་ཕྱིར་ཡང་རིགས་པ་མ་ཡིན་ཏེ། ཆོས་གང་ཞིག་ཆོས་གང་གི་སྐྱེད་པར་བྱེད་པར་གནས་པ་དེ་ནི་དེ་དང་དུས་ཐ་དད་པར་གྲགས་ཏེ། དཔེར་ན་ས་བོན་སྔ་ལ་མྱུ་གུ་འཕྱི་བ་དང་། འོ་མ་སྔ་ལ་ཞོ་འཕྱི་བ་དང་། བསྣུན་པ་སྔ་ལ་སྒྲ་འཕྱི་བ་དང་། ཡིད་སྔ་ལ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་འཕྱི་བ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 3154]
རྒྱུ་དང་འབྲས་བུ་དག་སྔ་ཕྱིའི་དངོས་པོར་མ་གྲུབ་པ་ཡང་མ་ཡིན་མོད་ཀྱི་ལྷན་ཅིག་པའི་དངོས་པོར༌[^1798]ཡང་འགྲུབ་སྟེ། དཔེར་ན་མིག་གི༌[^1799]རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་རྣམས་དང་། མིག་དང་གཟུགས་དག་དང་། འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པ་རྣམས་ལྟ་བུའོ། །

[Block 3155]
དེ་ལ་ཡང་དབང་པོ་དང་དོན་དག༌[^1800]སྔ་ལ༌[^1801]རྣམ་པར་ཤེས་པ་འཕྱི་བ་དང་། འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པ་རྒྱུ་ཚོགས་པ་སྔ་མ་ལས་ཕྱི་མ་འབྱུང་ངོ་ཞེས་བྱ་བར་འདོད་ན་དགག་པ་ཅི་ཞིག་ཡོད། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་འོ་ན་ནི་མྱུ་གུ་དང་གྲིབ་མ་དག་ཇི་ལྟ་བར་རེག་པ་དང་ཚོར་བ་དག་ཀྱང་དེ་དང་འདྲའོ་ཞེས་ཟེར་རོ། །
--- END BLOCKS ---
