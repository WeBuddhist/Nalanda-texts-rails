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
[Block 106]
བདག་ཉིད་ལ་ང་དང་ང་ཡིར་འཛིན་པ་མེད་ཀྱང་ང་དང་ང་ཡི༌[^89]ཞེས་པ་གསུངས་པས་འཇིག་རྟེན་པས་རྟོགས་པའི་ཐབས་སུ་འགྱུར་བའི་ཕྱིར་འཇིག་རྟེན་པ་ལ་ལྟོས་ནས་ང༌[^90]དང་ང་ཡི་ཞེས་གསུངས་ལ། འདི་ལྟར་གཙུག་ན་ནོར་བུའི་རྟོགས་པ་བརྗོད་པ་ལ་སོགས་པར་བྱ་དཀའ་བ་བརྒྱ་ཕྲག་གསུངས་པ་དེ་གང་ཞིག་དེའི་ཚེ་ལོང་བ་ཆེན་པོར་གྱུར་པ་དང་གང་དུ་འདི་ལྟར་བྱ་དཀའ་བ་བརྒྱ་ཕྲག་གསུངས་ཤེ་ན། དེ་དག་གོ་བར་འདོད་པའི་འཇིག་རྟེན་པ་ལ་གལ་ཏེ་ང་ཉིད་དེའི་ཚེ་ན་ཞེས་མ་གསུངས་ན་འཇིག་རྟེན་པས་རྟོགས་པར་འདོད་པའི་དོན་མི་རྟོགས་པར་འགྱུར་བའམ།[^91] དེ་བཞིན་གཤེགས་པའི་སྤྱོད་པ་ལ་ངོ་མཚར་བར་ཡང་མི་འགྱུར་རོ། །

[Block 107]
དེ་བཞིན་དུ་ང་ཡིར་འཛིན་པ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 108]
གང་ཡང་འདི་ལྟར་ང་དང་ང་ཡིར་འཛིན་པ་མེད་ཀྱང་འཇིག་རྟེན་པའི་ངོར་འཇུག་ཏུ༌[^92]ང་དང་ང་ཡིར་འཛིན་པ་ཡོད་པ་ལྟ་བུར་མཚོན་ནོ། །

[Block 109]
དེ་བཞིན་དུ་དངོས་པོར་གྱུར་པ་གཞན་གསུང་བ་ན་ཡང་དངོས་པོ་དེའི་རང་བཞིན་ལྟ་བུར་མཚོན་པར་ཁས་བླང་བར༌[^93]བྱའོ། །

[Block 110]
དེའི་ཕྱིར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱིས་གསུངས་པས་དངོས་པོ་ཡོད་པ་མ་ཡིན་པ་ཉིད་དེ་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་རྗེས་སུ་འཇུག་པས་གསུངས་པའོ༌[^94]ཞེས་ཤེས་པར་བྱའོ། །

[Block 111]
ང་དང་ང་ཡིར་འཛིན་པ་བཞིན་བརྗོད་བྱས་སྟོང་པའི་ཕྱིར་ན། བརྗོད་བྱ་མེད་པར་རབ་ཏུ་བྱེད་པ་རྫོགས་ཀྱི་བར་གྱིས་སྟོན་པར་འགྱུར་རོ། །

[Block 112]
དེའི་ཕྱིར་གནས་པ་ལ་སོགས་པ་འདི་དག་གི་རྗོད་བྱེད་ནི་བརྗོད་བྱ་མེད་པ་སྟེ། ཐ་སྙད་ཀྱི་དབང་གིས་བརྗོད་པ་འགའ་ཞིག༌[^95]ཏུ་གྲུབ་ཀྱི་དོན་དམ་པའི་དབང་གིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 113]
གལ་ཏེ་གསུངས་པ་ཐམས་ཅད་དངོས༌[^96]མེད་པ་ཚིག་ཙམ་ཁོ་ན་ཡིན་ན། གང་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་དུ།

[Block 114 [VERSE]]
བདག་ཉིད་ལ་ནི་བདག་ཉིད་མགོན། །
རྗེས་སུ་མགོན་བྱེད་གཞན་སུ་ཞིག །
བདག་ཉིད་ལེགས་པར་དུལ་གྱུར་ན། །
མཁས་པས་མཐོ་རིས་ཐོབ་པར་འགྱུར། །

[Block 115]
ཞེས་གསུངས་པ་དེ་ལ་བདག་ལ་སོགས་པ་ཡོད་པ་མིན་ན་མགོན་ལ་སོགས་པ་ཇི་ལྟར་རིགས་པར༌[^97]འགྱུར། དེའི་ཕྱིར་བདག་ཡོད་དོ་ཞེ་ན། གལ་ཏེ་ཡང་ཁྱོད་ནི་རང་ཉིད་ཀྱིས་ཡོངས་སུ་སྤངས་ནས་རྩོད་པའི་སྐབས་ཚོལ་བར་བྱེད་ལ་དེ་ལྟ་ན་ཡང་སྨྲས་པ།

[Block 116 [HEADING]]
### ཚིགས་བཅད་གཉིས་པ། ^1-2-0

[Block 117 [VERSE]]
བདག་མིན་བདག་མེད་མིན་བདག་དང་། །
བདག་མེད་མིན་པས་རྗོད་འགའ་འང་མེད། །
བརྗོད་བྱ་མྱ་ངན་འདས་དང་མཚུངས། །
དངོས་པོ་ཀུན་གྱིས༌[^98]རང་བཞིན་སྟོང་། །

[Block 118]
དེ་ལ་བདག་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཚིག་གི་ལྷག་མའོ། །

[Block 119]
འདིར་བསྒོམ་པ་ལས་བྱུང་བའི་ངོར༌[^99]རློམ་སེམས་པ་ནི་བདག་ཅེས་བྱའོ། །

[Block 120]
དེ་ཉིད་སྲེད་པའི་དངོས་པོར་གྱུར་པས་སྲེད་པའི༌[^100]སྙིང་སྟོབས་ཀྱི་ཕྱིར་སེམས་ཅན་ནོ། །

[Block 121]
སྲོག་གི་དབང་པོ་དང་འབྲེལ་པས་འཚོ་བས་ན་སྲོག་གོ། །

[Block 122]
ལས་དང་ཉོན་མོངས་པས་སྐྱེ་བ་གཞན་དུ་སྐྱེ་བར་བྱེད་པས་སྐྱེ་བ་པོའོ། །

[Block 123]
ཡིད་གཙོ་བོར་གྱུར་པ་ལས་སྐྱེས་པས་ཤེད་ལས་སྐྱེས་སོ། །

[Block 124]
ཡིད་ཤས་ཆེ་བར་གྱུར་པའི་ཕྱིར་ཤེད་ཅན་ནོ། །

[Block 125]
དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པའི་ལས་བྱེད་དུ་འཇུག་པའི་ཕྱིར་བྱེད་པ་པོའོ། །

[Block 126]
དེའི་འབྲས་བུ་མྱོང་བར་བྱེད་པའི་ཕྱིར་རིག་པ༌[^101]པོའོ། །

[Block 127]
ཡུལ་ཡོངས་སུ་དཔྱོད་པའི༌[^102]ཕྱིར་ཤེས་པ་པོའོ། །

[Block 128]
དཔྱོད་པར་བྱེད་པའི་ཕྱིར་མཐོང་བ་པོའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་དེའི་མིང་གི་ཁྱད་པར་རོ། །

[Block 129]
བདག་དེ་ཡང་རྩ་བའི་རབ་བྱེད་བཅུ་པར། །

[Block 130 [VERSE]]
རེ་ཞིག་ཤིང་ལ་མེ་མིན་ཞིང་། །
ཤིང་ལས་གཞན་དུ་མེ་མ་ཡིན། །
མེ་ནི་ཤིང་དང་ལྡན་མིན་ལ། །
མེ་ལ༌[^103]ཤིང་མེད་དེར༌[^104]དེ་མེད། །

[Block 131]
མེ་དང་བུད་ཤིང་བཤད་པ་ཡིས། ། བདག་དང་ཉེ་བར་ལེན་རིམ༌[^105]བཞིན། །ཞེས་པའི་ཚིག་གིས་ཉེ་བར་ལེན་པ་ལས་དེ་ཉིད་དང་གཞན་པ་རྣམ་པ་ལྔས་དཔྱད་ན་མི་སྲིད་པས་བདག་མེད་དོ་ཞེས་བྱའོ། །

[Block 132]
ཡང་ན་འདིར་ཕྱོགས་སྔ་མ་གཞན་ཏེ། གལ་ཏེ་ཡང་སངས་རྒྱས་རྣམས་ངར་འཛིན་པ་དང་། ང་ཡིར་འཛིན་པ་སྤངས་པའི་ཕྱིར། ང་དང་ང་ཡིར་འཛིན་པའི་གསུང་དངོས་པོ་མེད་ལ། ངར་འཛིན་པ་དང་ང་ཡིར་འཛིན་པ་མ་སྤངས་པའི་འཇིག་རྟེན་པའི་ང་དང་ང་ཡིར་འཛིན་པའི་བརྗོད་པ་དོན་དང་བཅས་པར་འགྱུར་རོ་ཞེ་ན། སྨྲས་པ། འཇིག་རྟེན་པའི་ང་དང་ང་ཡིར་འཛིན་པའི་ཚིག་དོན་དང་བཅས་པ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། གང་གི་ཕྱིར་བདག་མིན་ཅེས་བདག་དགག་པ༌[^106]སྔར་བཞིན་ནོ། །

[Block 133]
བདག་མ་གྲུབ་པས་ཀྱང་འཇིག་རྟེན་གྱི་ང་དང་ང་ཡིར་འཛིན་པའི་རྗོད་བྱེད་ཀྱང་བརྗོད་བྱས་སྟོང་པའོ། །

[Block 134]
འདིར་སྨྲས་པ། གལ་ཏེ་བདག་མེད་ན་ཡང་དེ་ལྟ་ན་ཡང་ངར་འཛིན་པ་སེམས་ལས་བྱུང་བའི་ཆོས་རང་རིག་པར་ཡོད་པས་དེའི་རྗོད་བྱེད་ཚིག་ཙམ་མ་ཡིན་ནོ་ཞེ་ན།[^107] སླར་ཡང་ངར་འཛིན་པ་དེའི་དམིགས་པ་ཅི་ཞེ་ན། བདག་གོ། །

[Block 135]
གལ་ཏེ་དེ་ལྟ་ན་བདག་མེད་ན་དམིགས་པ་ལས་གཞན་དུ་ངར་འཛིན་ཇི་ལྟར་འབྱུང་བར་འགྱུར། དམིགས་པ་མེད་པར་སེམས་དང་སེམས་ལས་བྱུང་བ་སྐྱེ་བ་ནི་མེད་དོ། །

[Block 136]
ཁ་ཅིག་ནི་ཕྱི་རོལ་གྱི་དམིགས་པ་ལ་ལྟོས་པ་མེད་པར་སེམས་དང་སེམས་ལས་བྱུང་བ་སྐྱེ་སྟེ། དཔེར་ན་རྨི་ལམ་ལ་སོགས་པའོ་ཞེ་ན། དཔེ་འདི་ནི་གཉི་ག་ལ་མ་གྲུབ་པས་རྣམ་པར་རིག་པར་སྨྲ་བའི་འདོད་པའི་དོན་གྲུབ་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 137]
ཁྱོད་ལ་ཡང་དཔེ་མེད་པས་འདོད་པའི་དོན་མི་འགྲུབ་བོ༌[^108]ཞེ་ན། སླར་ཡང་ཁོ་བོའི་འདོད་པ་ཅི་ཞེ་ན། རྣམ་པར་ཤེས་པའི༌[^109]ཕྱི་རོལ་ལ་དམིགས་པར་བྱེད་པ་ཉིད་དོ། །

[Block 138]
སླར་ཡང་དེ་ཇི་ལྟར་མ་གྲུབ་ཅེ་ན། ཁོ་བོས་སུན་ཕྱུང་བའི་ཕྱིར་རོ། །

[Block 139]
གལ་ཏེ་ཁྱོད་ཀྱི༌[^110]སྐྱོན་བརྗོད་པ་ནུས་པ་དང་ལྡན་པར་གྱུར་ན། དེ་ལྟར་འགྱུར་ལ་རག་ན་གཉི་ག་ལ་གྲགས་པའི་དཔེ་བརྗོད་པ་མེད་པས་ནུས་པ་མེད་དོ། །

[Block 140]
ཁྱོད་ལ་ཡང་ཁོ་བོ་ལ་ལྟོས་ནས་གཉི་ག་ལ་གྲུབ་པའི་དཔེ་ནུས་པ་མེད་པས་འདོད་པའི་དོན་མི་འགྲུབ༌[^111]བོ། །

[Block 141]
སླར་ཡང་ཅི་ཁོ་བོའི་འདོད་པ་རྣམ་པར་ཤེས་པ་ཕྱི་རོལ་ལ་དམིགས་པ་ཡིན་ལ། རྣམ་པར་ཤེས་པ་ཉིད་ཁོ་བོ༌[^112]མི་འདོད་ན། ཅིའི་ཕྱིར་ཕྱི་རོལ་ལ་དམིགས་པར་བྱེད་པ་པོ་ཉིད་ཁོ་བོའི་འདོད་པ་ཡིན། འཇིག་རྟེན་པའི་ཐ་སྙད་ཁོ་བོས་ཁས་བླངས་ལ་དེའི་ཡུལ་དང་རྣམ་པར་ཤེས་པ་ཡང་འཇིག་རྟེན་པས་ཤེས་ཀྱི་ཁོ་བོས་ནི་མ་ཡིན་ནོ། །

[Block 142]
ཁྱོད་ཀྱིས་ཀྱང་ཁོ་བོ་ཅག་དང་འབྲེལ་བའི་འཇིག་རྟེན་པའི་དོན་འདི་སེལ་བར་མི་ནུས་སོ། །

[Block 143]
དེ་ལ་ཅི་འཇིག་རྟེན་པ་ལ་སེམས་དང་སེམས་ལས་བྱུང་བ་དམིགས་པ་དང་བཅས་པ་མ་གྲུབ་པས། དེ་ལས་དམིགས་པས་བསྐྱེད་པའི༌[^113]སེམས་དང་སེམས་ལས་བྱུང་བ་དམིགས་པ་མེད་ན་དེ་མེད་པས་བདག་མེད་ན་ངར་འཛིན་པ་མེད་པར་གྲུབ་བོ། །

[Block 144]
ཁོ་བོས་དེ་ལྟར་ཁས་མ་བླངས་སོ་ཞེ་ན། སླར་ཡང་ཅི་དངོས་པོ་འདི་དག་འཇིག་རྟེན་པ་ལ་མ་གྲུབ་པས་གང་ཞིག་ཁྱོད་ཀྱང་ཁས་མི་ལེན་ནམ། འདི་དག་ནི་འཇིག་རྟེན་པ་ལ་གྲུབ་ལ། འོན་ཀྱང་འཇིག་རྟེན་རྨོངས་པས་ཕྱིན་ཅི་ལོག་ཇི་ལྟ་བ་དེ་ལྟ་བར་འཇུག་པར་འགྱུར་རོ་ཞེས་ཁོ་བོ་སྨྲའོ། །

[Block 145]
དེའི་ཕྱིར་འཇིག་རྟེན་པའི་འདི་དག་ཀྱང་ཁོ་བོས༌[^114]ཁས་མི་ལེན་ནོ་ཞེ་ན། སྨྲས་པ། འདིར་དོན་རྟོགས་པ་པོ་རྣམས་ཀྱི་དོན་རྟོགས་པ་འཛིན་པ༌[^115]ལས་སམ་བསྟན་བཅོས་ལས་འགྱུར་གྲང་། དེ་ལ་རེ་ཞིག་འཇིག་རྟེན་པ་ཁྱོད་ལ་ཚད་མ་མ་ཡིན་ལ། བསྟན་བཅོས་ལས་ཁས༌[^116]བླངས་པའི་དོན་ཀྱང་གཞན་ལ་བསྒྲུབ་པར་ནུས་པ་མེད་ལ། དེའི་ཕྱིར་ཁྱོད་དང་མཚུངས་པའི་སྐྱེ་བོའི་སྒྲའི་རྗེས་སུ་ཁྱོད་འཇུག་པའི༌[^117]རིགས་ཀྱི་མཁས་པ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
