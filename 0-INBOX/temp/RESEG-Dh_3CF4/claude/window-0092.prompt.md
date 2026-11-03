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
[Block 3221]
དེ་ལྟར་ཚིགས་བཅད་དྲུག་གི་གོ་རིམས་ཀྱི་རྒྱུ་འདི་དག་གོ། །

[Block 3222]
དེ་ལྟར་ཚིགས་བཅད་བཅུ་གསུམ་པོ་འདི་རྣམས་ཀྱི༌[^2050]དོན་བསྡུས་པའི་ཚིགས་བཅད་གཅིག་སྟེ། མི་ཡི་བདག་པོ་ཆང་འདི་དེ་འདྲ་ཡང་། །ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 3223]
ད་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཉེས་དམིགས་ཀྱི་དབང་དུ་བྱས་ནས། །གང་ཞིག་བསྟེན༌[^2051]ན་ངན་པ་སྤྱོད་པར་འགྱུར། །ཞེས་བྱ་བ་དང་། ཆང་དེ་ཉུང་ངུ་འཐུངས་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ཏེ། གང་ཞིག་བསྟེན་ན་རབ་ཏུ་འཇིགས་པར་ལྟུང་། །ཞེས་བྱ་བ་ནི་གང༌[^2052]སྔར་བསྟན་མ་ཐག་པའི་གང་ཞིག་བློ་ནི་རབ་ཏུ་ཉམས་གྱུར་ནས། ཞེས་བྱ་བའི་ཚིགས་བཅད་དེའི་མཚམས་མེད་པའི་ལས་ཀྱིས་ངན་སོང་གི་འགྲོ་བར་འཇུག་པ་ཡིན་ཏེ། ལས་དེ་བྱས་ནས་དམྱལ་བ་ལ་སོགས་པའི་ངན་སོང་རྣམ་པ་གསུམ་དུ་འགྲོ་བར༌[^2053]འགྱུར་ཏེ། དེ་ལྟར་འགྲོ་བའི་ལས་ཀྱང་ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོའི་དབྱེ་བས་སོ། །

[Block 3224]
བསྟེན་པ་ཞེས་བྱ་བ་ནི་ཆང་བསྟེན་པའོ། །

[Block 3225]
ངན་པ་སྤྱོད་པར་འགྱུར་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ལས་ལ་སོགས་པ་རྣམ་པ་གསུམ་ངན་པར་སྤྱོད་པར་འགྱུར་བའོ། །

[Block 3226]
ཡང་ན། གང་ཞིག་བསྟེན་ན་ངན་པར༌[^2054]སྤྱོད་པར་འགྱུར། །ཞེས་བྱ་བ་ནི་ཆང་འཐུང་བ་ཉིད༌[^2055]ངན་པ་སྤྱོད་པར་འགྱུར་བ་ཉིད་དེ། དེ་ཉིད་ཤས་ཆེ་བ་ལ་སོགས་པ་བསྟན་པ་འདིས་ན་ཆང་འཐུང་བ་ཉིད་ཀྱིས་ངན་སོང་གསུམ་དུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 3227]
ཡི་དྭགས་དབུལ་བར་འགྱུར་ཞེས་བྱ་བ་ལ། དབུལ་བ་ཞེས་སྨོས་པ་ནི་ཡི་དགས་རྫུ་འཕྲུལ་ཆེ་བ་དག་མ་ཡིན་པའི་དོན་ཏེ། གང་གི་ཕྱིར་དེ་ནི་ལྷའི་འབྱོར་པ་ལྟ་བུར༌[^2056]རྗེས་སུ་མྱོང་བ་ཡིན་ཏེ། ཆང་འཐུང་བ་ནི་ཉེས་པ་ཆེ་བ་ཡིན་པས་གཅིག་ཏུ་མི་འདོད་པའི་འབྲས་བུ་བསྐྱེད་པ་ཡིན་པའི་ཕྱིར་ཡི་དགས་རྫུ་འཕྲུལ་ཆེ་བ་དག་ཏུ་སྐྱེ་བ་ནི་མི་རིགས་སོ། །ཇི་ལྟར་ཆང་འཐུང་བ་ངན་པ་ལ་སྤྱོད་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སློབ་དཔོན་བཙུན་པ་གཞན་ལ་ཕན་པའི་དབྱངས་ཀྱིས་བཤད་པ།

[Block 3228 [VERSE]]
མི་འཚེ་མི་རྐུ་འཁྲིག་པ་མི་སྤྱོད་པ། །
ལུས་ཀྱི་དགེ་བ་བྱས་པ༌[^2057]གསུམ་ཡིན་ནོ། །
འབྲེལ་མེད་ཕྲ་མ་བརྫུན༌[^2058]དང་ཚིག་རྩུབ་སྤོང་། །
ངག་གི་དགེ་བ་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 3229 [VERSE]]
ཆང་འཐུང་སྤོང་བ་འདི་ནི་སྡོམ་པ་བརྒྱད་པ་སྟེ། །
གང་ཚེ་ཀུན་དུ་འཚོ་བ་དགེ་བ་ལྡན་གྱུར་པ། །
དེ་ཚེ་ཚུལ་ཁྲིམས་ཆོ་ག་གནས་པར་གྱུར་པ་ཡིན། །

[Block 3230]
དེ་ལས༌[^2059]ཚུལ་ཁྲིམས་འཆལ་པར་མཁས་པས་བཤད། །དེ་བས་ན་ཆང་འཐུང་བ༌[^2060]ནི་ངན་པར་སྤྱོད་པ་ཉིད་དོ། །

[Block 3231]
དེ་ལྟར་རེ་ཞིག་འཐུང་བས༌[^2061]ནི་ངན་སོང་གསུམ་དུ་འགྲོ་བའི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་བཤད་ནས། ད་ནི་རྒྱུ་མཐུན༌[^2062]པའི་འབྲས་བུའི་དབང་དུ་བྱས་ནས། ཆང་དེ་ཉུང་ངུ་འཐུངས་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། ཉུང་ངུ་ཞེས་བྱ་བ་ནི་ཆུང་ངུ་དང་འབྲིང་དང་ཤས་ཆེ་བས་ཆང་འཐུང་བ་གསུམ་གྱི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་སྟེ། ཤས་ཆེར༌[^2063]འཐུངས་པའི་རྣམ་པར་སྨིན་པས་ནི་སེམས་ཅན་དམྱལ་བར་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3232]
འབྲིང་དུ་འཐུངས་པས་ནི་དུད་འགྲོའོ། །

[Block 3233]
ཆུང་ངུ་འཐུངས་པས་ནི་ཡི་དྭགས་སུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3234]
དེ་ཉུང་ངུ་འཐུངས་པའི་རྣམ་པར་སྨིན་པས་མིའི་ནང་དུ་སྐྱེས་ཀྱང་ཞེས་བྱ་བས་ནི་ཆུང་ངུ་འཐུངས་པའི་རྣམ་པར་སྨིན་པས་ཡི་དགས་ཀྱི་འབྲས་བུ་རྗེས་སུ་མྱོང་ནས༌[^2064]གལ་ཏེ་མི་རྣམས་ཀྱི་ནང་དུ་སྐལ་བ་མཉམ་པར༌[^2065]སྐྱེས་ན་ཡང་ཚུལ་ཁྲིམས་ལྟ་བ་ཉམས་ཞེས་སྨོས་པ་ཡིན་ཏེ། ཚུལ་ཁྲིམས་ཀྱིས་ཕོངས་པ་དང་། ལྟ་བས་ཕོངས་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 3235]
རྒྱུ་མཐུན་རྒྱུ་དང་འདྲ་བའོ་ཞེས་བྱ་བའི་ཚིག་གིས་ཆང་འཐུངས་པ་ནའོ། །

[Block 3236]
ཚུལ་ཁྲིམས་ཉམས་པར་འགྱུར་བ་དང་། བློ་ཡང་རྣམ་པར་རྨོངས་པ་ཡིན་ཏེ། དེ་བས་ན་མིར་སྐྱེས་ན་ཡང་ཚུལ་ཁྲིམས་དང་ལྟ་བ་གཉིས་ཀྱིས་ཕོངས་པ་ཡིན་ཏེ། རྒྱུ་དང་འདྲ་བ་ཡིན་པའི༌[^2066]ཕྱིར་འབྲས་བུ་ཡང་ཚུལ་ཁྲིམས་དང་ལྟ་བ་ཉམས་པར་འགྱུར་བ་ཡིན་ཏེ། ཕྱིས་ཀྱང་གསུམ་པོ་གང་ཡང་རུང་བ་དག་ཏུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3237]
ད་ནི་ཐམས་ཅད་ཀྱིས་བསྡུས་པའི་དོན་གྱི་ཚིགས་བཅད་ཚུལ་ཁྲིམས་ཉམས་པར་འགྱུར་ཞིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་བསྟན་པ་ཡིན་ཏེ། ཚུལ་ཁྲིམས་ཉམས་པས་ནི་ངན་འགྲོ་དག་ཏུ་ཤིན་ཏུ་ཡུན་རིང་པོར་སྡུག་བསྔལ་བར་འགྱུར་བ་ཡིན་ཏེ། འདིས་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཉེས་དམིགས་བསྟན་ཏོ། །

[Block 3238]
གཏམ་ངན་ཞེས་བྱ་བ་འདིས་ནི༌[^2067]མཐོང་བའི་ཆོས་ཀྱི་ཉེས་དམིགས་ཡིན་ཏེ། གང་གི་ཕྱིར་གྲགས་པ་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཕུན་སུམ་ཚོགས་པ་ཡིན་ཏེ། གཞན་དང་འབྲེལ་པའི་ཕྱིར་རོ། །

[Block 3239]
འཇིག་རྟེན་འདིའི་ཕུན་སུམ་ཚོགས་པ་ཐམས་ཅད་ཀྱི་རྒྱུ་ནི་གྲགས་པ་ཡིན་ཏེ། མེད་ན་ནི་རྒྱུ་མེད་པའི་ཕྱིར་རོ། །

[Block 3240]
ངོ་ཚ་མེད་ཅིང་བློ་གྲོས་དྲི་མ་ཅན་དུ་འགྱུར། །ཞེས་བྱ་བ་ལ། ངོ་ཚ་ཞེས་སྨོས་པས་ནི་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་གཉིས་གཟུང་ངོ་། །བློ་གྲོས་དྲི་མ་ཅན་དུ་འགྱུར། །ཞེས་བྱ་བ་ནི་ལྟ་བས༌[^2068]ཕོངས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 3241]
འདི་གཉིས་ཀྱིས་ཀྱང་ཚུལ་ཁྲིམས་གྲགས་པ་ཉམས་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 3242]
རྒྱུ་བཞི་པོ་འདི་དག་གིས་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཕུན་སུམ་ཚོགས་པའི་རྒྱུ་ཉམས་པར་བསྟན་ཏེ། བཞི་པོ་འདིའི་ནང་དུ་ཉེས་པ་ཐམས་ཅད་འདུས་པའི་ཕྱིར་ཡོན་ཏན་ཐམས་ཅད་ཉམས་པར་བསྟན་ཏེ།

[Block 3243 [VERSE]]
དེ་ཉིད་ཀྱི་ཕྱིར་སྨྲས་པ། །
ཡོན་ཏན་དེ་དང་དེ་དག་ཉམས། །

[Block 3244]
ཞེས་སྨོས་སོ། །

[Block 3245]
དེ་བས་ན༌[^2069]ཞེས་བྱ་བ་ནི་ཆང་འཐུང་བ་ཉིད་སྐྱོན་ཆེན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3246]
ཆང་འཐུངས་པའི༌[^2070]ཉེས་པ་ཁོང་དུ་ཆུད་པར་བྱས་པ་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་དེ་ལ་སྐྱོན་དུ་ཡང༌[^2071]མི་ལྟ་བར་གྱུར་ལ་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་པ་ཡིན་ཏེ། སྐྱོན་དུ་མི་ལྟ་བ་ཞེས་བྱ་བ་ནི་ཆང་འཐུང་བ་ལ་ཆགས་པའི་སྐྱོན་ཡོངས་སུ་མ་ཤེས་པའི་ཕྱིར་རོ། །

[Block 3247]
ཞེན་པ་མེད་པར་འགྱུར་ཞེས༌[^2072]བྱ་བ་ནི་དེ་ལ་ཞེན་པ་མེད་པའི་རྒྱུ་ཡིན་པ་བྱས་ནས་དེའི་ཉེས་པ་བསྟན་པའི་ཕྱིར་བརྩམས་པ་ནི་ཉེས་པ་དེ་བསྒྲུབས་པ༌[^2073]ཡིན་ནོ། །

[Block 3248]
བྱམས་པའི་ཕ་མ་ཞེས་བྱ་བ་འདིའི་བསྡུས་པའི་དོན་ནི་མིའི་འཇིག་རྟེན་གཉེན་བཤེས་ཕན་པར་སྟོན་པ་ནི་གསུམ་ཞིག་ཡོད་དེ། [^2074]བདེ་བར་འདོད་པ་དང་། ཕན་པར་འདོད་པ་དང་། ཐབས་སྟོན་པའོ། །

[Block 3249]
གང་དེ་གསུམ་གྱི་ཡོན་ཏན་དང་ལྡན་པར་སྟོན་པ་ཡིན་ཏེ། བདེ་བར་འདོད་པ་ནི་ཕ་མའོ། །

[Block 3250]
ཕན་པར་འདོད་པ་ནི་བླ་མའོ། །

[Block 3251]
ཐབས་སྟོན་པ་ནི་ཐབས་དང་བསམ་པ་དང་བག་ལ་ཉལ་ཤེས་པ་སྟེ་ཐུབ་པའོ། །

[Block 3252]
གསུམ་པོ་དེ་དང་འདྲ་བར་སྟོན་པའི་ཕྱིར་གསུམ་པོ་དེ་དང་མཉམ་པའོ། །

[Block 3253]
ཡུལ་གྲུ་མཆོག་ལ་སོགས་པའི་ནོར་ནི་ང་མི་འདོད་དེ། དེ་ཅིའི་ཕྱིར་ཞེ་ན། ལྷའི་དབང་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3254]
རྒྱུ་གོང་མ་གཉིས་ཀྱི་ལན་ནི་འདི་ཡིན་ཏེ། ཕན་པར་སྨྲ་ལ་མཆོད་པར༌[^2075]བྱེད། །ཅེས་བྱ་བ་ནི༌[^2076]ཚིགས་བཅད་ཕྱེད་དེས་གྲགས་དང་དཔལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་གཉིས་ཀྱིས་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཕན་ཡོན་བསྟན་ཏོ། །

[Block 3255]
དཔལ་ཞེས་བྱ་བ་ནི་རྙེད་པ་ཡིན་ཏེ་དེའི་བདེ་བའོ། །

[Block 3256]
དེ་ཡང་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་དང་། འཇིག་རྟེན་ཕ་རོལ་གྱི་བདེ་བ་ཡིན་ནོ། །

[Block 3257]
དེ་ཉིད་སྨྲས་པ། ངའི་ལུང༌[^2077]ལ་ཞེས་བྱ་བ༌[^2078]ནི་མཐོ་རིས་སུ་འགྲོ་བར་བྱེད་པ་སྟེ། འཇིག་རྟེན་ཕ་རོལ་གྱི་བདེ་བ་ཐོབ་པར་བྱེད་པའོ། །

[Block 3258]
ཡང་ན་བདེ་བ་དེ་ཡང་འཐོབ། །ཅེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཉིད་ཀྱི་ཡིན་ནོ། །

[Block 3259]
ང་ཡི་ལུང་ལ་བརྟེན་ཞེས་བྱ་བ་འདི་ནི་འཇིག་རྟེན་ཕ་རོལ་ལ་བདེ་བ་འཐོབ་པའི་ཚིག་གོ །སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་བུམ་པའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 3260 [HEADING]]
## རྒྱལ་རིགས་ཕྱུག་པོའི་སྐྱེས་པའི་རབས། ^19-0
--- END BLOCKS ---
