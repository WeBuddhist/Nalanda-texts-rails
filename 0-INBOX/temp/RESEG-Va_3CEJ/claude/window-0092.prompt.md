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
[Block 3221 [HEADING]]
###### **གཟུགས་མེད་པ་དང་ལྡན་པ།** ^3-1-11-13-2-3-0

[Block 3222]
ད་ནི་གཟུགས་མེད་པ་དང་ལྡན་པ་བརྗོད་པར་བྱ་སྟེ། གཟུགས་མེད་ཉེ་བར༌[^1836]བསྡོགས་ན་བཞི། །གཟུགས་མེད་པའི་ཉེ་བར༌[^1837]བསྡོགས་ནི་འདིར་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ཀྱི་ཉེ་བར་བསྡོགས་པ༌[^1838]ཡིན་ཏེ། དེ་ན་ནི་གཟུགས་དང་སྒྲ་དང་རེག་བྱ་དང་ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་བཞིའོ། །

[Block 3223]
དེ་དག་ཀྱང་། གཟུགས་སྒྲའོ།[^1839] །དེ་དག་གི་དམིགས་པ་ནི་བསམ་གཏན་བཞི་པ་ཡིན་ཏེ། གང་དག་གི་ལྟར་ན་དེ་རྣམ་པར་ཆད་པ་ལ་དམིགས་པ་ཡོད་པ་ཡིན་ནོ། །

[Block 3224]
གང་དག་གི་ལྟར་ན་ནི་དེ་དག༌[^1840]བཟླུམས་ཏེ་དམིགས་པ་དེ༌[^1841]དག་གི་ལྟར་ན་ནི་དེ་ན་ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་འདྲེས་པ་ལ་དམིགས་པ་གཅིག་ཁོ་ན་ཡོད་དོ། །

[Block 3225]
གོང་མར་འགྲོ་བ་གཅིག །དེ་ན་གཟུགས་མེད་པའི་ཁམས་ལ་དམིགས་པ་ནི་གཅིག་ཁོ་ན་སྟེ། ཆོས་ལ་ཉེ་བར་རྒྱུ་བའོ། །

[Block 3226]
དངོས་གཞི་ན་གཅིག །གཟུགས་མེད་པའི་དངོས་གཞི་ན་ནི་ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་གཅིག་ཁོ་ན་ཡོད་ཀྱི་གཞན་ནི་མེད་དོ། །

[Block 3227]
དེ་ཡང་། རང་ཡུལ་ཅན། གཟུགས་མེད་པའི་ཁམས་ཁོ་ན་ལ་དམིགས་པ་ཡིན་ཏེ། གཟུགས་མེད་པའི་དངོས་གཞི་རྣམས་ཀྱི་དམིགས་པ་ནི་ཁ་ཅིག༌[^1842]མ་ཡིན་ནོ་ཞེས་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 3228]
ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་དེ་དག་ཀྱང་། བཅོ་བརྒྱད་ཐམས་ཅད་ཟག་དང་བཅས། །ཟག་པ་མེད་པ་ནི་འགའ་ཡང་མེད་དོ། །

[Block 3229]
གང་ཞིག་དུ་དག་དང་ལྡན་ཞེ་ན། འདོད་པའི་ཁམས་སུ་སྐྱེས་པ་གཟུགས་ན་སྤྱོད་པའི་དགེ་བའི་སེམས་མ་ཐོབ་པ་ནི་འདོད་པ་ན་སྤྱོད་པ་ཐམས་ཅད་དང་ལྡན་ནོ། །

[Block 3230]
བསམ་གཏན་དང་པོ་དང་གཉིས་པའི་ས་པ་ནི་དྲི་དང་རོ་ལ་དམིགས་པ་མ་གཏོགས་པ་ཉོན་མོངས་པ་ཅན༌[^1843]བརྒྱད་བརྒྱད་དང་ལྡན་ནོ། །

[Block 3231]
བསམ་གཏན་གསུམ་པ་དང་བཞི་པའི་ས་པ་ནི་བཞི་བཞི་དང་ལྡན་ནོ། །

[Block 3232]
གཟུགས་མེད་པ་ན་སྤྱོད་པ་ནི་ཉོན་མོངས་པ་ཅན་གཅིག་ཁོ་ན་དང་ལྡན་ནོ། །

[Block 3233]
གཟུགས་ན་སྤྱོད་པའི་དགེ་བའི་སེམས་ཐོབ་པ་འདོད་ཆགས་དང་མ་བྲལ་བ་ནི་འདོད་པ་ན་སྤྱོད་པ་ཐམས་ཅད་དང་ལྡན་ནོ། །

[Block 3234]
བསམ་གཏན་དང་པོའི་ས་པ་ནི་བཅུ་དང་ལྡན་ཏེ། ཡིད་བདེ་བའི་ཉེ་བར་རྒྱུ་བ་དྲི་དང་རོ་ལ་དམིགས་པ་མ་གཏོགས་པ་ཉོན་མོངས་པ་ཅན་བཞི་དང་། མི་ལྕོགས་པ་མེད་པའི་ས་པའི་བཏང་སྙོམས་ཀྱི་ཉེ་བར་རྒྱུ་བ་དྲུག་དང་ལྡན་ནོ། །

[Block 3235]
བསམ་གཏན་གཉིས་པ་དང་།

[Block 3236]
གསུམ་པ་དང་།

[Block 3237]
བཞི་པ་དང་། གཟུགས་མེད་པ་ལས་སྐྱེས་པ་རྣམས་དང་ནི་སྔ་མ་བཞིན་ཏེ། སྲོལ་འདིས་ལྷག་མ་ཡང་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 3238]
བསམ་གཏན་དུ་སྐྱེས་པ་ནི་འདོད་པ་ན་སྤྱོད་པའི་བཏང་སྙོམས་ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་སྤྲུལ་པའི་སེམས་དང་མཚུངས་པར་ལྡན་པ་གཅིག་དང་ལྡན་པར་རིག་པར་བྱའོ། །

[Block 3239]
གཞན་དག་ན་རེ་ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་རྣམས་ཀྱི་དོན་བྱེ་བྲག་ཏུ་སྨྲ་བ་ལྟ་བུ་འདི་ཡང་ཡོད་མོད་ཀྱི་མདོའི་དོན་ནི་གཞན་དུ་སྣང་ངོ་། །གང་ཞིག་གང་ལས་འདོད་ཆགས་དང་བྲལ་བ་དེ་ནི་དམིགས་པ་དེ་ལ་ཉེ་བར་རྒྱུ་བར་རིག་པ༌[^1844]མ་ཡིན་ནོ། །

[Block 3240]
དེ་ལྟ་བས་ན་ཡིད་བདེ་བ༌[^1845]ལ་སོགས་པ་ཟག་པ་དང་བཅས་པ་དག་ཀྱང་ཐམས་ཅད་ནི་ཉེ་བར་རྒྱུ་བ་མ་ཡིན་ནོ། །

[Block 3241]
འོ་ན་ཅི་ཞེ་ན། ཀུན་ནས་ཉོན་མོངས་པ་རྣམས་ཡིན་ཏེ། དེ་དག་གིས་ཡིད་ཡུལ་རྣམས་ལ་ཉེ་བར་རྒྱུ་བར་བྱེད་པའོ། །ཇི་ལྟར་ཉེ་བར་རྒྱུ་བར་བྱེད་ཅེ་ན། རྗེས་སུ་ཆགས་པར༌[^1846]བྱེད། སོ་སོར་མ་བརྟགས་པ་ཡང༌[^1847]བཏང་སྙོམས་སུ༌[^1848]བྱེད་པ་སྟེ། གང་དག་གི་གཉེན་པོར་རྟག་ཏུ་ཡོད་པ་དྲུག་གནས་པ་ཡིན་པ་སྟེ། མིག་གིས༌[^1849]གཟུགས་རྣམས་མཐོང་ནས་ཡིད་བདེ་བར་ཡང་མི་འགྱུར་ཞིང་། ཡིད་མི་བདེ་བར་ཡང་མི་འགྱུར་ལ། དྲན་པ་དང་ལྡན་ཞིང་ཤེས་བཞིན་དུ་བཏང་སྙོམས་སུ་གནས་སོ་ཞེས་བྱ་བ་ནས། དེ་བཞིན་དུ་ཡིད་ཀྱིས་ཆོས་རྣམས་ཤེས་ནས་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ལྟ་བུའོ། །

[Block 3242]
དགྲ་བཅོམ་པ་ལ་ཡང་འཇིག་རྟེན་པའི་དགེ་བའི་ཆོས་ལ་དམིགས་པའི་ཡིད་བདེ་བ་མེད་པ་མ་ཡིན་པས་འདི་ནི་ཀུན་ནས་ཉོན་མོངས་པའི༌[^1850]ཡིད་ཉེ་བར་རྒྱུ་བ་དེ་དགག་པ་མ༌[^1851]ཡིན་པར་བདེ་བར༌[^1852]མངོན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3243 [HEADING]]
###### སྟོན་པའི་བཀའ་སུམ་ཅུ་རྩ་དྲུག། ^3-1-11-13-3-0

[Block 3244]
ཡང་ཡིད་བདེ་བ་ལ་སོགས་པ་དེ་དག་ཉིད་ཞེན་པ་ལ་བརྟེན་པ་དང་། ངེས་པར་འབྱུང་བ་ཉིད་ལ་བརྟེན་པའི་བྱེ་བྲག་གིས་སྟོན་པའི་བཀའ་སུམ་ཅུ་རྩ་དྲུག་ཏུ་འགྱུར་ཏེ། དེ་དག་གི་བྱེ་བྲག་སྟོན་པས་བཀའ་སྩལ་པའི་ཕྱིར་རོ། །

[Block 3245]
དེ་ལ་ཞེན་པ་ལ་བརྟེན་པ༌[^1853]རྣམས་ནི་ཉོན་མོངས་པ་ཅན་དག་གོ། །

[Block 3246]
ངེས་པར་འབྱུང་བ་ལ་བརྟེན་པ་རྣམས་ནི་དགེ་བ་དག་ཡིན་ནོ། །

[Block 3247]
དེ་ལྟར་ན་ཚོར་བ་དག་ཅེས༌[^1854]བྱ་བར༌[^1855]སྲེད་པའི་ཡན་ལག་འདིའི་རབ་ཏུ་དབྱེ་བ་ནི་དུ་མ་ཡོད་པར་རིག་པར་བྱའོ། །

[Block 3248 [HEADING]]
##### ཡན་ལག་ལྷག་མ། ^3-1-11-14-0

[Block 3249]
ཡན་ལག་ལྷག་མ་རྣམས་ནི་ཡང་མི་བརྗོད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། བཤད་དང་འཆད་པར་འགྱུར་བ་གཞན། །འདིར་ཡན་ལག་ཁ་ཅིག་ནི་བཤད་ཟིན། ཁ་ཅིག་ནི་འོག་ནས་འཆད་དེ། དེ༌[^1856]ལ་རེ་ཞིག་རྣམ་པར་ཤེས་པ་ནི། རྣམ་པར་ཤེས་པ༌[^1857]སོ་སོར་རྣམ་རིག་པ། ཡིད་ཀྱི་སྐྱེ་མཆེད་ཀྱང་དེ་ཡིན་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 3250]
སྐྱེ་མཆེད་དྲུག་ཀྱང་། དེ་དག་རྣམས་ཀྱི་རྣམ་ཤེས་རྟེན་མིག་ལ་སོགས་པ་གཟུགས་དང་བ་རྣམས་ཞེས༌[^1858]བཤད་ཟིན་ཏོ། །

[Block 3251]
འདུ་བྱེད་དང་སྲིད་པ་ནི་ལས་ཀྱི་མཛོད་ཀྱི་གནས་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 3252]
སྲེད་པ་དང་ལེན་པ་རྣམས་ནི་ཉོན་མོངས་པའི་གནས་ཀྱི༌[^1859]མཛོད་ཀྱི༌[^1860]གནས་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 3253 [HEADING]]
##### ཉོན་མོངས་པ་དང་ལས་དང་གཞི་ས་བོན་ལ་སོགས་པ་དང་ཆོས་མཐུན་པ། ^3-1-11-15-0

[Block 3254]
སྔར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དེ་ཡང་མདོར་བསྡུ་ན་ཉོན་མོངས་པ་དང་། ལས་དང་། གཞི་རྣམས་སོ་ཞེས་བསྟན་པ།

[Block 3255 [HEADING]]
###### ཉོན་མོངས་པ་ས་བོན་ལ་སོགས་པ་དང་འདྲ་བ། ^3-1-11-15-1-0

[Block 3256 [VERSE]]
འདིར་ནི་ཉོན་མོངས་ས་བོན་བཞིན། །
ཀླུ་བཞིན་རྩྭ་བཞིན་ལྗོན་ཤིང་བཞིན། །
དེ་བཞིན་ཤུན་པ་བཞིན་དུ་འདོད། །

[Block 3257]
འདིའི་ས་བོན་ལ་སོགས་པ་དང་ཆོས་མཐུན་པ་གང་ཞིག་ཡིན་ཞེ་ན། དཔེར་ན་ས་བོན་ལས་སྡོང་བུ་དང་། ལོ་མ་ལ་སོགས་པ་སྐྱེ་བར་འགྱུར་བ་དེ་བཞིན་དུ། ཉོན་མོངས་པ་ལས་ཀྱང་ཉོན་མོངས་པ་དང་ལས་དང་གཞི་རྣམས་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3258]
དཔེར་ན་ཀླུ་གནས་པའི་མཚོ་ནི་སྐམ་པར་མི་འགྱུར་བ་ལྟར། ཉོན་མོངས་པའི་ཀླན་ཀ༌[^1861]གནས་པའི་སྐྱེ་བའི་མཚོ་ཡང་དེ་དང་འདྲའོ། །

[Block 3259]
དཔེར་ན་ནགས་ཚལ་རྩ་བ་ནས་མ་ཕྱུང་བ་རྣམས་ནི་བཅད༌[^1862]ཀྱང་སླར་སྐྱེ་བར་འགྱུར་བ་ལྟར། ཉོན་མོངས་པ་རྩ་བ་ནས་མ་བཏོན་པའི་འགྲོ་བ་རྣམས་ཀྱང་དེ་དང་འདྲའོ། །

[Block 3260]
དཔེར་ན་ཤིང་ལྗོན་པ་རྣམས་དུས་དུས་སུ་མེ་ཏོག་དང་འབྲས་བུ་རྣམས་སྐྱེད་པར་བྱེད་པ་དེ་བཞིན་དུ། ཉོན་མོངས་པ་རྣམས་ཀྱང་ལན་ཅིག་མ་ཡིན་པར་ཉོན་མོངས་པ་དང་ལས་དང་གཞི་རྣམས་ཀྱི་རྒྱུ་ཡིན་ནོ། །
--- END BLOCKS ---
