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
[Block 246 [VERSE]]
ཚེ་དང་ལྡན་པ་ཁྱོད་ཉོན་ཅིག །
འདི་ནི་ཁྱོད་ཀྱི་བདེན་པའི་དུས། །

[Block 247]
འདི་ནི་ཁྱོད་ཀྱི་འབྱུང་བའི་དུས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྔགས་ཀྱིས༌[^180]བར་ཆད་ཡོངས་སུ་དྲི་བའོ། །

[Block 248]
བསྙེན་པར་རྫོགས་པ་ཉེ་བར་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གསོལ་བ་དང་བཞིའི་ལས་ཀྱིས་ཏེ། ལས་བྱེད་པ་པོ་ལ་སྐབས་དོན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 249]
དེ་མ་ཐག་ཏུ་གྲིབ་ཚོད་རིག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པ་ཉེ་བར་བསྒྲུབས་པའི་རྗེས་སུ་གྲིབ་ཚོད་བསྙེན་པར་རྫོགས་པ་ལ་རིག་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 250]
དེ་མ་ཐག་ཏུ་ནི་ཐོགས་པ་མེད་པའོ། །

[Block 251]
ཇི་ལྟར་རིགས་པར༌[^181]བྱ་བ་ནི་ཆ་ལྷག་མའི་བྱ་བའི་ཚད་བྱ་བ་ལ་གཏན་འཇུག་པ་མི་རིགས་པས་ལས་བྱེད་པ༌[^182]ལས་གཞན་གྱིས་ཚད་འདི་ལ་སྦྱར་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཡང་ཚད་མ༌[^183]འདི་ལ་རྐང་པ་ལ་སོགས་པ་རྣམས་ལ་གང་ཞིག་ཅེ་ན། དེ་ནི་ཐུར་མ་སོར་བཞི་པས་བཟང་ངོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 252]
དེ་ནི་ཞེས་བྱ་བ་ནི་ཚད་དེ་རིང་བ་ཉིད་མེད་པའི་ཕྱིར་ཐུར་མ་སོར་བཞི་པས་ཚད་མཛེས་པའོ། །

[Block 253]
དེའི༌[^184]སྐྱེས་བུ་ཉིད་ཅེས་ཐ་སྙད་དུ་བྱའོ་ཞེས་བྱ་བ་ནི་བཟང་ཞེས་སྦྱར་བར་རོ། །

[Block 254]
དེ་ནི་ཞེས་བྱ་བ་ནི་ཐུར་མ་སོར་བཞི་པ་ལ་ཇི་ཙམ་པའི་ཐུར་མ་རྣམས་དེ་ཙམ་དུ་སྐྱེས་བུ་གྲིབ་མ་བརྗོད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 255]
ཉིན་མཚན་གྱི་ཆ་སྔ་དྲོ་ལ་སོགས་པ་དང་ཞེས་བྱ་བ་ནི་རིག་པར༌[^185]བྱ་ཞེས་བྱ་བ་རྗེས་སུ་འཇུག་གོ། །

[Block 256]
སྔ་དྲོ་དང་གུང་གི་ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་གིས་གསུངས་སོ། །

[Block 257]
དུས་ཚོད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་རིག་པར་བྱའོ། །

[Block 258]
དེ་དག་ལྔའོ་ཞེས་བྱ་བ་ནི་དུས་ཚོད་རྣམས་ཏེ། དགུན་གྱི༌[^186]དུས་དང་། དཔྱིད་ཀྱི་དུས་དང་། དབྱར་གྱི་དུས་དང་། དབྱར་ཐུང་ངུའི་དུས་དང་། དབྱར་རིང་པོའི་དུས་སོ། །

[Block 259]
འདི་རྣམས་ཀྱི་ཚད་བརྗོད་པ་ཡིན་ནོ། །

[Block 260]
དང་པོ་གཉིས་ནི་ཟླ་བ་བཞི་བཞིའོ་ཞེས་བྱ་བ་ནི་དགུན་གྱི་དུས་དང་དཔྱིད་ཀྱི་དུས་སོ། །

[Block 261]
འོག་མ་ནི་ཟླ་བ་གཅིག་གོ་ཞེས་བྱ་བ་ནི་དབྱར་གྱི་དུས་སོ། །

[Block 262]
དེའི་འོག་མ་ནི་ཉིན་ཞག་གཅིག་གོ་ཞེས་བྱ་བ་ནི་དེ་ནི་དབྱར་གྱི་དུས་ལས་འོག་མ་ནི་དབྱར༌[^187]ཐུང་ངུའི་དུས་ཏེ་ཉིན་ཞག་གཅིག་གོ། །

[Block 263]
ཐ་མ་ནི་དེས་ཟླ་བ་གསུམ་དུ་མ་ཆོག་པའོ་ཞེས་བྱ་བ་ནི་ཉིན་ཞག་གཅིག་པོ་དེས་མ་ཆོག་པའི་ཟླ་བ་གསུམ་ནི་ཐ་མའི་དུས་ཏེ་དབྱར་རིང་པོའི་དུས་སོ། །

[Block 264]
དུས་ཚོད་བརྗོད་པའི་དེ་མ་ཐག་ཏུ་བསྙེན་པར་རྫོགས་པར་བྱས་པ་ཙམ་ལ་ལས་བྱེད་པ་པོས་གནས་རྣམས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཕྱག་དར་ཁྲོད་པ་ལ་སོགས་པ་བཞི་པོ་དེ་རྣམས་སོ། །

[Block 265]
ལྟུང་བར་འགྱུར་བའི་ཆོས་རྣམས་དང་། དགེ་སྦྱོང་དུ་བྱེད་པའི་ཆོས་རྣམས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྟེ། ཁྲོ་བ་ལ་སླར་མི་ཁྲོ་བ་ལ་སོགས་པ་རྣམས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བར་འབྲེལ་ཏོ། །

[Block 266]
མཆོག་ཏུ་འདོད་པར་བྱ་བ་ཡང་དག༌[^188]པ་ཉིད་ཀྱིས་རྫོགས་པ་ཉིད་བརྗོད་ནས། ཚུལ་ཁྲིམས་ཀྱིས་མཉམ་པར་གྱུར་པ་ཉིད་བསྒྲུབ་པ་ལ་ངེས་པར་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་ནི་མཆོག་ཏུ་འདོད་པར་བྱ་བས་ན་མཆོག་ཏུ་འདོད་པར་བྱ་བ་ཡིན་ཏེ། གང་ཞིག་ཁྱེད་ལ་སྔོན་བྱུང་བ་སྟོན་པར་བྱེད་པའོ། །

[Block 267]
བདག་གིས༌[^189]ཅི་ཞིག་ཐོབ་པར་འགྱུར་རམ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་ནི་དེའི༌[^190]འདོད་པའོ། །

[Block 268]
དེའི་རྫོགས་པ་ཉིད་ནི་ཡོད་པ་ཉིད་གཟུང་ནས་སུ་འདི་ལ་རབ་ཏུ་བྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 269]
སླར་རྫོགས་པ་ཉིད་ལ་མཐུན་པའི་མཁན་པོས་ཞེས་བྱ་བ་ལ་སོགས་པས་ཡང་དག་པ་ཉིད་བརྗོད་པའོ། །

[Block 270]
རྫོགས་པ་ཉིད་བརྗོད་ནས་ཅི་ཞིག་བྱ་ཞེ་ན། ཚུལ་ཁྲིམས་ཀྱིས་མཉམ་པར་གྱུར་པ་ཉིད་བསྒྲུབས་པ༌[^191]ལ་ངེས་པར་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་དུ་བསྙེན་པར་རྫོགས་ནས་ལོ་བརྒྱ་ལོན་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚུལ་ཁྲིམས་ཀྱིས་མཉམ་པར་གྱུར་པ་ཉིད་ནི་ཚུལ་ཁྲིམས་ཀྱིས་མཉམ་པར་གྱུར་པ་ཉིད་དོ། །

[Block 271]
བསྒྲུབ་པ་ནི་སྟེན་པར༌[^192]བྱེད་པའོ། །

[Block 272]
ཚུལ་དང་འབྲེལ་བའི་གཟུགས་བརྙན་དང་ཞེས་བྱ་བ་ནི་ངེས་པར་སྦྱར་བར་བྱ་ཞེས་པ་ཐམས་ཅད་དུ་དབང་དུ་བྱེད་པར་རིག་པར་བྱའོ། །

[Block 273]
ཚུལ་དང་འབྲེལ་པ་ནི་ཕ་མ་ལྟ་བུར་འབྲེལ་པའོ། །

[Block 274]
དེའི་གཟུགས་བརྙན་ནི་དེ་ཕྱིན་ཆད་ནས་མཆོག་ཏུ་ཁྱོད་ཀྱིས་མཁན་པོ་ལ་ཕའི་འདུ་ཤེས་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 275]
དེ་ལྟར་ན་ཁྱོད་ཀྱིས་ཁྱིམ་པའི་འབྲེལ་བ་དེ་གོམས་པ་སོ་སོར་སྤང་བར་བྱ་ཞེས་བྱ་བའོ། །

[Block 276]
དུལ་བར༌[^193]གནས་པ་ཉིད་དང་ཞེས་བྱ་བ་ནི་དེང༌[^194]ཕྱིན་ཆད་ཁྱོད་ཀྱིས་གུས་པ་དང་བཅས་པར༌[^195]ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 277]
དགོས་པ༌[^196]རྗེས་སུ་བསྒྲུབ་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེང་ཕྱིན་ཆད་མཆོག་ཏུ་ཁྱོད་ལ་བསྟན་པར་བྱ་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 278]
མ་བརྗོད་པ་ཡང་དག་པར་བླངས་པ་ཡོངས་སུ་ཤེས་པའི་བསྒྲུབ་པར་འགྱུར་བ་ཉིད་ཀྱང་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཁྱོད་ལ་འདི་དང་འདི་རྣམས་བདག་གིས་རྒྱ་ཆེར་ཞེས་བྱ་བ་འདི་ལྟ་བུ་ལ་སོགས་པས་སོ། །

[Block 279]
དེ་ནི་མ་བརྗོད་པར་ཡང་དག་པར་བླངས་པའི་ཚུལ་ཁྲིམས་ལ་གནས་པ་ལ་ཡོངས་སུ་ཤེས་པ་དེ་ལྟར་བསྒྲུབ་པར་འགྱུར་ཞེས་བྱ་བའོ། །

[Block 280]
གུས་པ་ལས༌[^197]ཡང་ངེས་པར་སྦྱར་བར༌[^198]བྱའོ་ཞེས་བྱ་བ་ནི། ཁྱོད་ནི་བསྙེན་པར་རྫོགས་པར་གྱུར། །ཞེས་བྱ་བའི༌[^199]ཚིགས་སུ་བཅད་པ་དག་གིས་དང་། སྐྱེད་པ༌[^200]ཞེས་བྱ་བ་འདིས་དལ་འབྱོར་ཕུན་སུམ་ཚོགས་པ་རྙེད་པར་དཀའ་བ་ཉིད་བསྟན་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་མི་ཁོམ་པ་གཞན་མེད་པས་ཀྱང་ཐོབ་པར་བྱ་བ་རྙེད་པ་ལ་ཡང་ཐུགས་བརྩེ་བ་དང་ལྡན་པ་རྣམས་ཀྱིས་དལ་འབྱོར་ཕུན་སུམ་ཚོགས་པའི་མིའི་ལུས་ཉིད་འདི་ལ་རྣམ་པར་མ་དག་པའི་གྲངས་མང་པོ་ནི་བར་ཆད་རྣམས་དང་གཟུགས་ངན་པ་ཉིད་དེ། [^201]དེ་བས་ན་འདི་རྙེད་པར་དཀའ་བའོ། །

[Block 281]
བསྒྲུབ་པར་བྱ་བ་ཐབས་བརྗོད་པ་དང་བཅས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བརྗོད་པ་དང་ལྷན་ཅིག་ཏུ་ནི་བརྗོད་པ་དང་བཅས་པའོ། །

[Block 282]
གང་གི༌[^202]དོན་དུ་རབ་ཏུ་བྱུང་བ་ཉིད༌[^203]དང་བསྙེན་པར་རྫོགས་པ་དེ་བསྒྲུབ་པར་བྱ་བ་ལ་ཚེ་དང་ལྡན་པ་ཁྱོད་བསྙེན་པར་རྫོགས་ཟིན་གྱིས་བག་ཡོད་པར་སྒྲུབས༌[^204]ཤིག་ཅེས་བྱ་བ་འདིས་ངེས་པར་སྦྱར་བར་བྱའོ། །

[Block 283]
འདི་ལྟ་སྟེ་ཁྱོད་ནི་གནས་འདི་རྗེས་སུ་ཐོབ་པ་སྟེ། ད་ནི་འདིར་ཁྱོད་ཀྱིས་མངོན་པར་དགའ་བར་བྱ་ཞེས་བྱ་བའོ།

[Block 284]
[^205] །

[Block 285]
དང་པོ་ཕྱག་ལན་གསུམ་བྱས་ནས་དགེ་འདུན་འདུས་པའི་ནང་དུ་རྗེས་སུ་བསྟན་པ་ལ་ཙོག་ཙོག་པོར་འདུག་པའི་མདུན་དུ་སོ་ཕག་བཏིང་བ་དག་གིས་གསང་སྟེ་སྟོན་པ་ལ་བསྙེན་པར་རྫོགས་པ་ལ་གནས་པའི་ལག་པ་གཡོན་པར་ལྷུང་བཟེད་བཞག་སྟེ། ལག་པ་གཡས་པས་བཀབ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལས་ཀྱི་གཞིར་འཆད་པར་འགྱུར་བ་ཉིད་ཀྱི་ཕྱིར་འདིར་རྗེས་སུ་འབྲེལ་པ་མ་བྱས་སོ། །
--- END BLOCKS ---
