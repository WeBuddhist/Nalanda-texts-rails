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
[Block 141]
འདིར་གཞུང་ནི་དེ་རྣམས་སློང་བར་བྱེད་ན་ཉེས་དམིགས་དེ་ཉིད་དུ་འགྱུར་རོ། །

[Block 142]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། མགོའམ་མཇུག་བཟློག་པ་སློང་བར༌[^96]བྱས་ཏེ། འགྲོ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 143]
གོས་དག་བསྐམ་པའི་ཕྱིར་རྩྭ་གདིང་བ་ཡང་དོར་བར་བྱ་བ་ཉིད་དོ། །

[Block 144]
སློང་བ་ལ་དོར་བ་ཁས་ལེན་ན་སྦྱིན་ནོ་ཞེས་བྱ་བ་ལ། སྦྱིན་པ་ཞེས་བྱ་བ་ནི་གནང་བའི་རྩྭ༌[^97]རྣམས་སོ། །

[Block 145]
འཆག་ས་དག་ཏུ་རྐང་མཐིལ་གཉིས་ལ་རྩུབ་ན་རྩྭ༌[^98]དག་གདིང་བར་བྱའོ། །

[Block 146]
དེ་དག་ཀྱང་དོར་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གནང་བའི་རྩྭ་རྣམས་སོ། །

[Block 147]
གཏོང་ན་དོར་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་དུ་མ་གྱུར་པ་དོར་བར་བྱའོ་ཞེས་བྱ་བ་ལ། གཏོང་ན་ཞེས་བྱ་བ་ནི་འཆག་པ་གཏོང་བའི་དུས་ལ་དོར་བར་བྱ་བ་དོར་བའོ། །

[Block 148]
ཅི་གནས་སྐབས་ཐམས་ཅད་དུ་ཡིན་ནམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་དོར་བར་བྱ་བ་མ་ཡིན་པ་ཉིད་དུ་མ་གྱུར་པ་ལ་ཞེས་བྱ་བ་སྨོས་ཏེ། གྱུར་པ་ལ་ནི་གྱུར་པ་ཉིད་ཁོ་ན་བྱས་པ་ཉིད་དོར་བ་ཞེས་བྱ་བ་དོན་གྱིས་ཐོབ་བོ། །

[Block 149]
གཞན་གྱི་ཚེ་ནི་དུས་སུ་སོ་སོར་བརྟག་པ་དང་བསྒྱུར་ལོག་བྱའོ་ཞེས་བྱ་བ་ལ། གཞན་གྱི་ཚེ་ཞེས་བྱ་བ་ནི་གཏོང་བའི༌[^99]དུས་ལས་སོ། །

[Block 150]
ས་སྣུམ་པ་དང་མངར་བ་ནི་ཉིན་རེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་སྲིལ་ལ་སོགས་པ་ལས་བྱུང་བའི་ཉེས་པ་སྤང་བའི་ཕྱིར་ཉི་མ་རེ་རེར་བསྒྱུར་བཟློག་བྱ་བའོ། །

[Block 151]
ཡུལ་གང་ནས་ས་སྣུམ་པ་དང་མངར་བ་ནི་སྲིལ་རྣམས་ལ་སྡུག་བསྔལ་འབྱུང་བས་ཏེ། དེའི་ཕྱིར་ན་སྣུམ་པའི་ཚིག་གོ། །

[Block 152]
དེ་ལྟར་ཡང་ཡུལ་འདི་ནི་སྣུམ་པ་དང་འཇམ་པའི་ས་དང་ལྡན་པ་ཞེས་བྱ་བས༌[^100]ནི་སྣུམ་པ་བརྗོད་པའོ། །

[Block 153]
གཞན་དུ་ཟླ་བ་ཕྱེད་ཕྱེད་ཅིང་ངོ་ཞེས་བྱ་བ་ནི་ས་སྣུམ་པ་དང་མངར་བ་ལས་གཞན་པའི་ཡུལ་དུ་ནི༌[^101]ཟླ་བ་ཕྱེད་ཕྱེད་ཅིང་ལན་རེ་བསྒྱུར་བཟློག་བྱའོ། །

[Block 154]
འདིར་གཞུང་ནི་གལ་ཏེ་ས་ཕྱོགས་སྣུམ་པ་དང་མངར་བ་ཡིན་ན་བཏིང་བ་ཉིན་རེ་ཞིང་བསྒྱུར་བཟློག་བྱའོ། །

[Block 155]
གལ་ཏེ་ས་ཕྱོགས་སྣུམ་པ་དང་མངར་བ་མ་ཡིན་ན་ནི་ཟླ་བ་ཕྱེད་ཅིང་བསྒྱུར་བཟློག་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 156]
འཆག་ས་དག་ཏུ་རྩྭའི༌[^102]ཆུན་པོ་དག༌[^103]ཐག་པས་བཅིངས་ཏེ་ཤིང་ལ་གཞག་པར་བྱའོ། །

[Block 157]
ལྕི་བ་གྱོ་མོར་གཞག་པར་བྱའོ། །

[Block 158]
གནས་ནས་འཕགས་པར་འགྱུར་བ་ན་ཞེས་བྱ་བ་ཡན་ཆད་སྔར་ཐལ་བའོ་ཞེས་བྱ་བ་ནི། སྔར་མདོ་ལས་གནས་ནས་འཕགས་པར་འགྱུར་བ་ན་སྔར་གྱི་བསླབ་པའི་གཞི་དེ་དང་འབྲེལ་པ་གང་ཡིན་པ་དེ་འདིར་རྟོགས་པར་བྱའོ། །

[Block 159]
འདིར་གཞུང་ནི་དགེ་སློང་འཁོད་པ་ལ་ཡང་མ་བཅོལ་ན་གཞན་ལ་དེ་འདྲ་བའི་རྐྱེན་མ་གཏོགས་ཏེ་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པའི་ལྟུང་བ་བསྟན་པའི་གཞུང་རྒྱ་ཆེར་འབྱུང་བ་དེ་དག་གནས་མལ་ལྟུང་བའི་ལམ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 160]
དེ་བཞིན་དུ་འདིར་ཁ་ཅིག་ནི་འདིར་གཞན་དེ་འདྲ་བའི་རྐྱེན་ལས་ཞེས་བྱ་བ་འདི་ཉམ་ང་བ་དང་ཕྲད་པར་མི་འགྱུར་བ་ལྟ་ན་ཞེས་བྱ་བ་ནི་མ་ཡིན་པ་དགག་པ་སྟེ་འབྲེལ་པ་མང་པོ་ཉིད་དུ་བྱ་བ་མི་འཇུག་པ་ཡིན་ནོ། །

[Block 161]
དེའི་ཕྱིར་འདི་མེད་པར་རྟོགས་པར་བྱ་སྟེ། བསླབ་པའི་གཞི་འདི་དག་ལ་རྣམ་པ་གཅིག་ཏུ་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 162]
དེ་བས་ན་མ་བརྗོད་པའི་དོན་ལ་ཡང་འདིར་སྔ་མའི་རྗེས་སུ་འབྲང་བས་ཐོབ་པའོ། །

[Block 163]
གཞན་དག་ནི་ཆར་པས་ཕན་ཕུན༌[^104]དུ་གྱུར་པས་འདིར་མི་འཇུད་དོ་ཞེས་ཟེར་ན་དེ་ཡང་མི་རིགས་ཏེ། འདིར་འདིས་ཀྱང་ས་གཞི་ཆུད་ཟོས་པའི་ཕྱིར་རོ། །

[Block 164]
རེག་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་ལ་ནི་མི་འགྱུར་རོ་ཞེས་བྱ་བ་འདི་ལ་འདིར་དོན་མི་སྣང་བས་ལོག་པའོ། །

[Block 165]
གནས་མལ་འདི་སྡུས༌[^105]ཤིག་ཅེས་བྱ་བ་འདིར༌[^106]འདི་ལ་གནས་མལ་གྱི་གནས་སུ་གདིང་བ་གཏོགས་པར་དོན་གྱིས་གྲུབ་བོ། །

[Block 166]
དེ་བས་ན་དེའི་འོག་ཏུ་ཐམས་ཅད་ལ་དམིགས་ཀྱིས་བསལ་བའོ། །

[Block 167]
ཅིག་ཅར་སྤྱོད་པ་ནི་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ཐམས་ཅད་ལ་ཁྱབ་པ་དང་ལྡན་པ་ཡིན་གྱིས་ལངས་པ་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 168]
དགེ་འདུན་གྱི༌[^107]མ་ཡིན་པར་ནི་གནས་པའི་བདག་པོ་རྣམས་ལ་ཡང་དྲི་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཡང་གི་སྒྲས་ནི་དགེ་སློང་ལ་ཡང་ཞེས་བྱ་བ་དགེ་འདུན་གྱི་གནས་མ་ཡིན་པར་གནང་བའི་གདིང་བ་ལ་གནས་དེའི་བདག་པོ་རྣམས་ལ་དྲི་བར་བྱ་ཞིང་དོར་བར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 169]
རྣམས་ལ་ཞེས་མང་པོའི་ཚིག་ཏུ་བསྟན་པ་ནི་འདིར་བུ་དང་ཆུང་མ་ལ་སོགས་པ་དག་ཀྱང་དེའི་དངོས་པོ་ལ་བདག་པོར་གྱུར་པ་ལ་ཁོངས་སུ༌[^108]བསྡུ་བའི་དོན་ཏོ། །

[Block 170]
གཅིག་གི་ཚིག་གིས༌[^109]ཁྱིམ་བདག་གཅིག་ཁོ་ན་ལ་བཟུང་བར་ཤེས་པར་འགྱུར་རོ། །

[Block 171]
འདིར་ཡན་ལག་གང་རྣམས་ལ་ལྟུང་བའི་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་ཉིད་དང་རྡོ་བ་དང་ཕྱེ་མའི་གཞི་ཉིད་ལ་སོགས་པའི་བདག་ཉིད་མ་ཡིན་པ་ཉིད་དང་དེ་ལྟ་བུའི་ཉེས་དམིགས༌[^110]ཡོད་པ་ཉིད་ཀྱིས་གཞིར་རང་དང་བསྐོས་པས་གདིང་བ་བྱ་བ་ཉིད་ལྟ་བུ་ནི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྡོ་བ་དང་ཞེས་བྱ་བ་ནི་རུང་བ་ཉིད་ལ་འདི་བསྟན་པ་སྟེ། དེ་ལྟ་བུའི་བདག་ཉིད་རུང་བ་ཉིད་ཅེས་བྱ་བའོ། །

[Block 172]
སོགས་པའི་སྒྲས་ནི་རྡོ་བ་ལ་སོགས་པས་མ༌[^111]ཡིན་པར་འགྱུར་བ་བཟུང་ངོ་། །རྡོ་བ་དང་བྱེ་མ་ལ་སོགས་པ་ས་གང་ལ་ཡོད་པ་མ་ཡིན་པ་དེ་ནི་རྡོ་བ་དང་བྱེ་མའི་གཞིའོ། །

[Block 173]
དེའི་དངོས་པོ་དང་རྡོ་བ་དང་བྱེ་མའི་གཞི་ཉིད་དེ་རྣམས་ཀྱི་བདག་ཉིད་དོ། །

[Block 174]
དེ་ལྟ་བུའི་ཉེས༌[^112]དམིགས་ཡོད་པ་ཉིད་ཀྱིས་རུང་བ་ཉིད་ཅེས་བྱ་བ་ནི་སྲིལ་ལ་སོགས་པའི་ཉེ་བར་འཚེ་བ་རུང་བ་ཉིད་དོ། །

[Block 175]
རང་དང་བསྐོས་པས་གདིང་བ་བྱས་པ་ཉིད་ལྟ་བུ་ནི་བྱེད་པ་པོ་དག་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། སྔར་ཐལ་བའོ་ཞེས་བྱ་བ་འདི་ལས་དངོས་གཞིའི་མཐའ་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིར་རྟོགས་པར་བྱའོ། །

[Block 176]
གདིང་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 177]
སྐྲོད་པའི་ལྟུང་བྱེད་ལ་བྱེད་པ་པོ་ཉིད་གང་ཡིན་ཞེ་ན་དེའི་ཕྱིར་དགེ་སློང་ཉིད་དང་དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་ཉིད་དག་ནི་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 178]
ཅི་བསམ་པ་ཐམས་ཅད་ཀྱིས་དེ་ཉིད་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན་དེའི་ཕྱིར། གལ་ཏེ་དེ་ལ་གནོད་པ་དང་དགེ་འདུན་འཁྲུག་པ་སྐྱེ་བ་ཉེ་བར་ཞི་བར་མི་འགྱུར་བའི་གཉེན་པོར་འདོད་པ་མ་ཡིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་ཉིད་གང༌[^113]ལ་བྱེད་པ་པོ་ཉིད་དུ་བརྗོད་པ་དེ་ལ་སྲོག་གཏོང་བ་ལ་སོགས་པས་གནོད་པ་ནི་དེ་ལ་གནོད་པའོ། །

[Block 179]
དེ་ལ་གནོད་པ་དང་དགེ་འདུན༌[^114]འཁྲུག་པ་དག༌[^115]ལ་སྐྱེ་བ་དང་སྐྲོད་པ་གཉིས་ལ་ཉེ་བར་ཞི་བར་མི་འགྱུར་བར་དོགས་པ་ཡོད་པ་ལས་བསམ་པ་གཞན་ལ་འདི་དག་ལས་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 180]
དེ་གཉིས་གང་ལ་བྱེད་པ་པོ་ཉིད༌[^116]ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྐྲོད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །སུས་ཤེ༌[^117]ན། དེའི་ཕྱིར་གཞན་གྱིས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། [^118]རང་ཉིད་གཅིག་པུ་ནི༌[^119]མ་ཡིན་ནོ། །
--- END BLOCKS ---
