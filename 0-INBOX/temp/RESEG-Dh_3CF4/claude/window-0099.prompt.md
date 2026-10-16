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
[Block 3466]
འབྲིང་གི་དབང་དུ་བྱས་པ་ནི།

[Block 3467 [VERSE]]
གང་གིས་མཛའ་བོ་རྣམས་དང་མྱུར་དུ་འཁོན༌[^2226]འབྱུང་འགྱུར། །
ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་འོག་མ་ཡིན་ནོ། །
འདི་དང་ཕ་རོལ་དུ་ཡང་འདོད་པས་གསོད་པར༌[^2227]བྱེད། །

[Block 3468]
ཅེས་བྱ་བ་ནི། གྲགས་པ་ཉམས་ཤིང་ཕྱི་མ་ལ་ཡང་སྡུག་བསྔལ་མྱོང་། །ཞེས་བྱ་བ་ཚིགས་བཅད་དེའི་དབང་དུ་བྱས་པ་སྟེ། གྲགས་པ་ཉམས་པ་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཉེས་དམིགས་སོ། །

[Block 3469]
སྡུག་བསྔལ་མྱོང་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཉེས་དམིགས་སོ། །

[Block 3470]
བདག་ལ་ཕན་འདོད་སྦྲུལ་གདུག་ཁྲོས་པ་བཞིན། །ཞེས་བྱ་བ་ནི་དུས་རྟག་ཏུ་ཕུང་ཁྲོལ་གྱི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3471]
བདག་གིས་འདིར་པདྨའི་རྩ་བ་སྦས་པ་ཞེས་བྱ་བ་ཅིའི་ཕྱིར་ཞེ་ན༌[^2228]སྨྲས་པ་བརྟག་པའི༌[^2229]ཕྱིར་རོ། །ཅིའི་ཕྱིར་བརྟག་ཅེ་ན། སྨྲས་པ། ཡོན་ཏན་རྣམས་རེ་བ་བཞིན་པ་རྟོགས༌[^2230]པར་འགྱུར་བའོ། །

[Block 3472]
སྤྱོད་པ་རྣམ་པར་དག་པ་ནི་གང་གི་ཡིད་འཁྲུགས་པ༌[^2231]མ་ཡིན་ཞིང་དོན་གཞན་དུ་མ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3473]
བརྟན་པའི་སྤྱོད་པ་ནི་བདེ་བ་དང་སྡུག་བསྔལ་ལྡོག་པ་དང་འཇུག་པ་གཉིས་ལ་ཡང་བརྟན་པའི་ཁྱད་པར་གྱིས་གཞན་དུ་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 3474]
ངེད་ཅག་ཁྱོད་ཀྱི་གཉེན་དང་གྲོགས་མ་ཡིན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་རྩེད་མོའི་ལམ་འབྱུང་བའི་རྒྱུ་ནི་རྣམ་པ་བཞི་སྟེ། དེའི་དབང་དུ་བྱས་ནས། ངེད་ཅག་ཁྱེད་ཀྱི་གཉེན་དང་ཞེས་བྱ་བ་ནི་གང་གིས་ལྷན་ཅིག་སྐྱེས་པའི་སྤུན་ཟླའོ། །

[Block 3475]
གྲོགས་ནེའུ་ལྡངས་ཏེ། འདི་གཉིས་ཀྱིས་ནི་རང་གི་སྐྱེ་བོ་ཡིན་པའི་ཕྱིར་དང་། ན་ཚོད་མཉམ་པའི་ཕྱིར་རྩེད་མོའི་ལམ་བཞིན་དུ་བྱ་བར་རིགས་པ་ཡིན་ནོ། །

[Block 3476]
གར་མཁན་ནི་འདྲ་བར་བྱེད་པ་ཡིན་ཏེ། གར་མཁན་དང་འཕྱས་གདགས་པ་ནི་གཅིག་ལ་གཅིག་རྩེད་མོའི་ལམ་རིགས་པ་ཡིན་ཏེ། དེས་ཀུན་དུ་འཚོ་བའི་ཕྱིར་རོ། །

[Block 3477]
ཅིའི་ཕྱིར་ཁྱད་དུ་བསད་ནས་ཞེས་བྱ་བ་ནི་གཟི་བྱིན་གྱིས་ནོན་པའི་ཚིག་སྟེ། རྩེད་མོའི༌[^2232]ལས་ཞེས་བྱ་བའི་ཚིག་གིས་ནི་སྤྱོད་པ་གླང་པོས་སྤྱོས་སོ༌[^2233]ཞེས་བྱ་བའོ།

[Block 3478]
[^2234] །སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་པདྨའི་རྩ་བའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 3479 [HEADING]]
## ཚོང་དཔོན་གྱི་སྐྱེས་པའི་རབས། ^21-0

[Block 3480]
ཐོས་པ་དང་། དུལ་བ་དང་། ཆོ་རིགས་བཙུན་པ་ཞེས་བྱ་བ་ལ་ཐོས་པ་ནི་ད་ལྟར་བྱུང་བའི་ཤེས་རབ་ཀྱི་ཚོགས་སོ། །

[Block 3481]
དུལ་བ་དང་། ཆོ་རིགས་བཙུན་པ་ནི་འདས་པའི་སྐྱེ་བའི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་སྟེ། རྣམ་པར་སྨིན་པ་དང་། རྒྱུ་མཐུན་པའི་འབྲས་བུ་འོ། །

[Block 3482]
མ་འཇུངས་ཤིང་ཁོང་བཟོ་བ་ཞེས་བྱ་བ་ནི་འདས་པའི་སྐྱེ་བའི་ཤེས་རབ་ཀྱི་ཚོགས་དེའི་འབྲས་བུའོ། །

[Block 3483]
འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་བྱ་བ་ལ་འགལ་བ་མེད་པ་ཞེས་བྱ་བ་ནི་ད་ལྟར་བྱུང་བའི་དུས་ཀྱི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 3484]
གཙུག་ལག་མང་པོ་ལ་གོམས་པས་ཚིག་ལ་མཁས་པར་གྲགས་པ་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་ཐོས་པ་གསལ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 3485]
སྙིང་རྗེ་དང་ལྡན་ཞེས་བྱ་བ་ལ་སོགས་པའི༌[^2235]ཚིག་གིས་ནི་ད་ལྟར་བྱུང་བའི་སྐྱེ་བའི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 3486]
རབ་ཏུ་ཕྱུག་པས༌[^2236]ཞེས་བྱ་བ་ནི་ཚེ་སྔ་མའི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་བའི་འབྲས་བུའོ། །

[Block 3487]
དེ་ལྟར་འདི་དག་ཐམས་ཅད་ཀྱི༌[^2237]བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་རྒྱུ་དང་འབྲས་བུ་ལ་འཇུག་པ་བསྟན་པའོ། །

[Block 3488]
དེ་ནི་རང་བཞིན་ཆོས་ཀྱི་བདག །ཅེས་བྱ་བ་འདིས༌[^2238]ནི་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 3489]
ཐོས་ལ་སོགས་པའི་ཡོན་ཏན་བརྒྱན། །ཅེས་བྱ་བ་འདིས་ནི་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གནས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 3490]
ཚོགས་གཉིས་ཀྱི་གནས་ཉིད་དུ་གྱུར་པས་བཀུར་སྟི་བྱ་བའི་གཞིར་གྱུར་པ་ཡིན་ནོ། །

[Block 3491]
ཕྲད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་བལྟ་བའི་ཕྱིར་རོ། །

[Block 3492]
དེའི་ཁྱིམ་དུ་ཞེས་བྱ་བ་ནི་སེམས་དཔའ་ཆེན་པོའོ། །

[Block 3493]
མགྲོན་འོངས་པའི་བཀུར་སྟིའི་བྱ་བ་བྱས་པ་གང་ཡིན་པ་དེ་ནི་མགྲོན་འོངས་པའི་བཀུར་སྟིའི་བྱ་བ་བྱས་པའོ། །

[Block 3494]
གཏམ་སྨྲ་བའི་སྐབས་ལ་བབ་པ་ནི་སྐབས་ལ་བབ་པའི༌[^2239]གཏམ་གླེང་བའོ། །

[Block 3495]
དེ་ལས་འཕྲོས་པའི་གླེང་ལངས་པའོ། །

[Block 3496]
ཁྱོད་ལ་བྱམས་སམ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་བརྩེ་འམ་ཞེས་དྲི་བ་ཡིན་ཏེ། བུད་མེད་གཞན་ལ་ཆགས་པ་མེད་དམ་ཞེས་དྲི་བ་འོ། །

[Block 3497]
ཁྱོད་ཀྱིས་ནི༌[^2240]བཀུར་སྟི་བྱས་པའི་ཡོན་ཏན་དྲིན་དུ་གཟོ་འམ་མི་གཟོ་ཞེས་བྱ་བ་ནི་གསོ༌[^2241]ཞིང་བསྐྱེད་པ་ལ་སོགས་པ་སྟེ། གནོད་པ་མ་བྱས་པ་ཉིད་དང་། བཀུར་སྟི་བྱས་པའི་ཡོན་ཏན་ཡོངས་སུ་ཤེས་པར་གྱུར་པའོ། །

[Block 3498]
མི་བདེ་བ་ལྟ་ཡོད་དམ་མེད་ཅེས་བྱ་བའི་ཚིགས་བཅད་ལ་སོགས་པ་རྣམ་པ་གཉིས་ཏེ། འདི་གསུམ་གྱིས་ནི་བདག་ཉིད་དང་མཉམ་པར་ལོངས་སྤྱོད་དང་ཉེ་བར་སྤྱོད་པས་རྗེས་སུ་འཛིན་པ་ཡིན་ཏེ། མི་བདེ་བ་མེད་པ་ནི་ཉེ་བར་འཚེ་བ་མེད་པར་བསྟན་ཏོ། །

[Block 3499]
དེ་ལྟར་རེ་ཞིག་བུད་མེད་རྣམས་གཞན་ལ་རག་ལུས་པའི་ཚུལ་ཡིན་པས་འདྲི་བར་བྱེད་པའོ། །

[Block 3500]
དེ་ངོ་ཚ་བས་མགོ་སྨད་དེ་མི་སྤོབས་བཞིན་དུ་ཞེས་བྱ་བས་ནི་གནས་མ་ཡིན་པར་དྲིས་པས་དེ་ངོ་ཚ་སྟེ་མགོ་སྨད་པའོ། །

[Block 3501]
སྤོབས་པ་ནི་དེའི་ལན་དེ་མི་སྤོབས༌[^2242]བཞིན་དུའོ། །

[Block 3502]
དར་ལ་བབ་ཅིང་བྱད་གཟུགས་བཟང་། །ཞེས་བྱ་བའི་དོན་ནི་བདག་གི་དབང་ངམ་གཞན་གྱི་དབང་གིས་རབ་ཏུ་བྱུང་བར་བྱེད་པའི་རྒྱུ་ཡིན་ན་རབ་ཏུ་བྱུང་བའི་རྒྱུ་དེ་གཉི་ག་མེད་པར་སྟོན་ཏོ། །

[Block 3503]
[^2243]བདག་གི་དབང་ཡང་རྣམ་པ་གཉིས་ཀྱིས་རབ་ཏུ་བྱུང་བ་ཡིན་ཏེ། ལོངས་སྤྱོད་སྤྱོད་པར་མི་ནུས་པ་དང་། དཀའ་ཐུབ་ཀྱི་ནགས་སུ་གནས་པར་འོས་པ་སྟེ་གཉིས་སོ། །

[Block 3504]
དེ་གཉི་ག་ཡང་མེད་པར་བསྟན་པའི་ཕྱིར་དང་པོའི་ཕྱེད་ཀྱིས་བསྟན་པ་ཡིན་ཏེ། དར་ལ་བབ་ཅིང་བྱད་གཟུགས་བཟང་། །ཞེས་བྱ་བ་འདི་གཉིས་ཀྱིས་ནི་ཉེ་བར་ལོངས་སྤྱོད་པར་རིགས་པར་བསྟན་ཏེ། དར་ལ་བབ་པས་ནི་རང་ཉིད་ཀྱིས་ལོངས་སྤྱོད་པར་ནུས་པ་དེས་སོ། །

[Block 3505]
བྱད་གཟུགས་བཟང་ཞེས་བྱ་བས་ནི༌[^2244]བུད་མེད་རྣམས་ཀྱིས་ཀྱང་འདོད་པར་བྱ་བ་དེས་སོ། །
--- END BLOCKS ---
