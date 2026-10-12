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
འདོད་ཆགས་དང་བྲལ་བའི་སྐུ་སྤངས་ནས་ཞེས་པ་ནི་སྙིགས་མ་ལྔའི་དུས་སུ་སྒེག་པའི་ཉམས་གཙོར་གྱུར་པས་སྒེག་ཅིང་གཟུགས་བསྟན་ཏོ། །

[Block 3222]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3223]
སེམས་ཅན་རྣམས་སྨིན་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་ངོ་བོ་ནི་སྙིང་རྗེ་ཆེན་པོའི་བདག་ཉིད་ཀྱི་རྒྱུ་ཅན་ཡིན་ཞེས་བསྟན་ཏོ། །

[Block 3224]
དེ་བས་ན་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་བསྒོམ་པས་གང་གི་ཚེ་འགྲོ་བའི་དོན་བྱེད་ན་དེའི་ཚེ་དེ་རྫོགས་པར་བྱ་བའི་ཕྱིར་དེ་དང་རྗེས་སུ་མཐུན་པའི་ཏིང་ངེ་འཛིན་ལ་དཔལ་རྡོ་རྗེ་འཆང་ཆེན་པོས་དམིགས་པར་མཛད་ཅེས་རྒྱུད་ཐམས་ཅད་ཀྱི་གཞུང་ལུགས་སོ། །

[Block 3225]
དཀྱིལ་འཁོར་པ་རྣམས་ཞེས་པ་ནི་འཁོར་རྣམས་སོ། །

[Block 3226]
རང་གི་ས་བོན་ཞེས་བྱ་བ་ལ་སོགས་པས་ཡེ་ཤེས་སེམས་དཔའི་ཐུགས་ཀ་ན་གནས་པ་པདྨ་དང་ཟླ་བ་དང་རྡོ་རྗེ་ལ་གནས་པ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ས་བོན་གྱི་འོད་ཟེར་གྱི་ལྕགས་ཀྱུས་ནམ་མཁའི་དབྱིངས་ན་བཞུགས་པའི་དེ་བཞིན་གཤེགས་པ་ལ་སོགས་པའི་ཚོགས་བཀུག་ལ་འཇུག་པར་མཛད་དོ། །

[Block 3227]
དེ་ནས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཅེས་བྱ་བ་ལ་སོགས་པས་སྔར་ཉེ་བར་བསྡུས་པ་གང་ཡིན་པ་དེ་རྣམས་ཀྱིས་དགའ་བ་བསྐྱེད་པར་བྱ་བའི་ཕྱིར་བུད་མེད་མཆོག་གི་གཟུགས་སུ་བཅོམ་ལྡན་འདས་ཀྱི་སྤྲོས་པ་མཛད་དོ། །

[Block 3228]
དེ་ནི་དོན་དམ་པར་བུད་མེད་དང་སྐྱེས་པའི་བྱེ་བྲག་གང་ཡང་མེད་དོ་ཞེས་བསྟན་ཏོ། །

[Block 3229]
གདུལ་བྱ་རྣམས་འཇུག་པར་བྱ་བའི་ཕྱིར་སངས་རྒྱས་ཀྱི་རོལ་སྟོན་གྱི་སྤྲོས་པ་རྨད༌[^2077]དུ་བྱུང་བར༌[^2078]བསྟན༌[^2079]ཏོ། །

[Block 3230]
དེ་ལ་བཅོམ་ལྡན་འདས་མཆོག་ཏུ་དགའ་བའི་བདེ་བས། ཞེས་པ་ནི་མཆོག་ཏུ་དགའ་བ་ལས་ཕྱི་མའི་དགའ་བ་ནི་མཆོག་ཏུ་དགའ་བ་སྟེ། འོད་གསལ་བ་བཞི་པ་ལ་འཇུག་གོ། །

[Block 3231]
ཡང་ན་མཆོག་ནི་ཐམས་ཅད་ཀྱི་ཕུལ་དུ་བྱུང་བ་སྟེ་དགའ་བ་བཞི་པ་ཁོ་ནའོ། །

[Block 3232]
རྣལ་འབྱོར་པ་ལ་གྲགས་པའི་རིགས་པས་མཆོག་ཏུ་དགའ་བའི་སྒྲས་ཀྱང་བཞི་པ་བརྗོད་དོ། །

[Block 3233]
དེ་ལྟ་ན་རང་གཟུགས་སུ་དེ་ཉིད་ཅིའི་ཕྱིར་མ༌[^2080]གཟུང་ཞེ་ན། སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3234]
བཞི་པ་ནི་བླང་བར་བྱ་བ་ཡིན་ཏེ། རྟོག་པ་མེད་པ་ཉིད་ཀྱིས་རྟག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3235]
དེ་བས་ན་ཚིམ་པར་བྱ་བའི་ཕྱིར་ཞེས་སྨོས་པ་ལ། དེ་ཉིད་ཀྱིས་ཚིམ་པར་བྱ་བར་རིགས་ཏེ། འཁྲུལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3236]
སྣང་བ་ལ་སོགས་པའི་ཡེ་ཤེས་གསུམ་གྱི་བདེ་བ་ནི་འཁྲུལ་པ་དང་བཅས་པ་ཡིན་ཏེ། དེ་མ་ཡིན་པ་ལ་དེ་ཉིད་དུ་གཟུང་བའི་ཕྱིར་རོ། །

[Block 3237]
རང་བཞིན་གྱིས་དག་པ་ལ་ནི་འཁྲུལ་པ་མེད་དེ། ཆོས་ཉིད་ནི་འཁྲུལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 3238]
གནས་སྐབས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་འོག་ནས་འཆད་པར་འགྱུར་བའི་ལྷ་མོ་དགུ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་དང་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་ཁྲོ་བོ་རྣམས་ཀྱི་ངོ་བོ་ཉིད་ཡིན་ནོ་ཞེས་རབ་ཏུ་བསྟན་ཏོ། །

[Block 3239]
གཞི་དང་གཞི་ཅན་ཐམས་ཅད་ཀྱི་དཀྱིལ་འཁོར་ཉེ་བར་བསྡུས་པའི་བྱང་ཆུབ་ཀྱི་སེམས་ལས་འབྱུང་བ་ཡིན་པས་དེའི་རྒྱུ་མཐུན་པར་གྱུར་པ་བདེ་བ་ཆེན་པོའི་ངོ་བོ་ཉིད་གསལ་བར་བྱས་པ་ཡིན་ནོ། །

[Block 3240]
སའི་ཁམས་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས་རིགས་ཀྱི་བཙུན་མོ་བཞི་བསྟན་ཏོ། །

[Block 3241]
ཡང་རྣམ་པར་སྣང་མཛད་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་རིགས་ལས་འབྱུང་བའི་ལྷ་མོ་ལྔ་བསྟན་ཏོ། །

[Block 3242]
དྲང་བའི་དོན་ཞེས་པ་ནི་སྤྲོ་བ་དང་བསྡུ་བ་ཙམ་བརྗོད་པའི་ཕྱིར་རོ། །

[Block 3243]
དེས་ནི་བཅོམ་ལྡན་འདས་ནམ་མཁའི་དབྱིངས་ཐམས་ཅད་དུ་བཞུགས་པའི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཉེ་བར་བསྡུས་པས་ལྷ་མོ་དགུར་སྤྲོས་ཏེ། དེའི་དབུས་སུ་འདོད་པ་སྣ་ཚོགས་ཀྱི་དབང་ཕྱུག་ཉིད་དུ་བཞུགས་སོ། །

[Block 3244]
དེའི་འོག་ཏུ་འདི་ལྟར་བྱ་བ་ཉིད་བསྟན་པར་བྱ་སྟེ། འདོད་ཆགས་ཀྱང་ཡིན་ལ་ཆེན་པོ་ཡང་ཡིན་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་འདོད་ཆགས་ཆེན་པོའི༌[^2081]ཆོས་ཞེས་ནང༌[^2082]དུ་སོང་བའི་དངོས་པོའི་རྐྱེན་ཉིད་ཀྱིས་འདོད་ཆགས་ཆེན་པོའི་ཆོས་ཉིད་ཀྱིས་བརྗོད་པར་བྱ་བ་ནི་འོད་གསལ་བ་ཉིད་བསྟན་ཏོ། །

[Block 3245]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། འདོད་ཆགས་དང་འདོད་ཆགས་བྲལ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྣང་བ་མཆེད་པ་ལ་སོགས་པའི་ཡེ་ཤེས་གསུམ་གྱི་རྣམ་གྲངས་ཡིན་ཞེས་བྱ་བའི༌[^2083]ཐ་ཚིག་གོ། །

[Block 3246]
རྣམ་པར་དག་པ་ནི་མངོན་དུ་བྱ་བ་སྟེ། འོད་གསལ་བ་ཐོབ་པའོ། །

[Block 3247]
ཐབས་ནི་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པའི་མཚན་ཉིད་ཀྱིས་ནི་སེམས་རྣམ་པར་དག་པའོ། །

[Block 3248]
ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་གྱི་རིམ་པའི་མཚན་ཉིད་ཅན་གྱི་རིམ་པ་ནི་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 3249]
ཕྱི་རོལ་གྱི་དེ་བཞིན་གཤེགས་པའི་འཁོར་དེ་དག་ཏུ་དམིགས་པའི་མངོན༌[^2084]པར་ཞེན་པ་སྤངས་ནས་ཞེས་པ་ནི་བདག་ནི་འདི་ཡིན་པ་དང་འདི༌[^2085]རྣམས་དེ་བཞིན་གཤེགས་པ་ཡིན་ཞེས་དེ་དག་གིས༌[^2086]ནི་སེམས་རྣམ་པར་དག་པ་དང་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་དག་ལ་མེད་པའི་ཕྱིར་རོ། །

[Block 3250]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་ཡོངས་སུ་བསྒྲུབས་པའི༌[^2087]སྐུ་ནི་བདག་ཡིན་ནོ་ཞེས་བྱ་བ་འདིས་གཉིས་པའི་རིམ་པ་ལས་མྱུར་དུ་ལྷའི་གཟུགས་བདག་བྱིན་གྱིས་རློབ་པའི་རིམ་པས་སྤྲོ་བའམ། ཡང་ན་བཞི་པ་ལས་ཟུང་དུ་འཇུག་པའི་རིམ་པས་རྡོ་རྗེ་ལྟ་བུའི་སྐུ་བྱིན་གྱིས་བརླབ་པར་མཛད་དོ། །

[Block 3251]
བདག་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པས་ལུང་གི་ཚད་མ་ཉིད་བཤད་དོ། །

[Block 3252]
སྔ་མ་བཞིན་ཞེས་བྱ་བ་ནི་སྤྲོ་བ་ཙམ་གྱི་དཔེ་ཡིན་གྱི་ཐམས་ཅད་ཀྱི་ནི་མ་ཡིན་ནོ། །

[Block 3253]
གང་གི་ཕྱིར་སྔོན་དུ་ནི་རྟོག་པའི་རྣལ་འབྱོར་གྱིས་སྤྲོས་པའི་ཕྱིར་རོ། །

[Block 3254]
འདིར་ནི་སྒྱུ་མ་ལྟ་བུ་ཉིད་ཀྱིས་སོ། །

[Block 3255]
ངེས་པའི་དོན་ཞེས་པ་ནི་སེམས་རྣམ་པར་དག་པ་དང་བདག༌[^2088]བྱིན་གྱིས་རློབ་པ༌[^2089]དང་། མངོན་པར་བྱང་ཆུབ་པ་དང་ཟུང་དུ་འཇུག་པ་རྣམས་འཆད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3256]
དེ་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི༌[^2090]འདོད་པའི་དབང་ཕྱུག་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར་ལྷ་མོ་དགུའི་བདག་ཉིད་གཟུངས་ཀྱི་དཀྱིལ་འཁོར་བསྟན་ཏོ། །

[Block 3257]
སེམས་གཙོ་བོ་ནི་ངག་དང་ལུས་ཀྱི་ནང་ནས་སེམས་ཁོ་ན་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3258]
མི་བསྐྱོད་པའི་བསྡུས་པའི་དཀྱིལ་འཁོར་སྤྲུལ་པའི་བྱ་བ་ཞེས་པ་ནི༌[^2091]རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་རྗེས་སུ་ཞུགས་པས་བསྐྱེད་པའི༌[^2092]ཐུགས་ཀྱི་རྡོ་རྗེའི་གཞི་དང་། གཞི་ཅན་གྱི་མཚན་ཉིད་ཀྱི་དཀྱིལ་འཁོར་གྱི་སྤྲུལ་པ་མཛད་ཅེས་ཐ་ཚིག་གོ། །

[Block 3259]
སྔ་མ་བཞིན་ཏེ་ཤེས་རབ་ཀྱི་གནས། །ཞེས་པ་ནི་བགེགས་བསྐྲད་པ་དང་སྟོང་པ་ཉིད་བསྒོམ་པའི་རྗེས་སུ་ཧཱུཾ་ལས་བྱུང་བའི་ཆོས་འབྱུང་བའི་ཕྱག་རྒྱ་ལའོ། །

[Block 3260]
དེར་ཆུད་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཡེ་ཤེས་ཀྱི་ས་གཞི་དང་རི་རབ་ལ་སོགས་པ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི་གྲུ་བཞི་པ་ལ་སོགས་པའི་ཡོན་ཏན་དང་ལྡན་པའི་གཞིའི་དཀྱིལ་འཁོར་ཞེས་བྱ་བའི་བར་རོ། །
--- END BLOCKS ---
