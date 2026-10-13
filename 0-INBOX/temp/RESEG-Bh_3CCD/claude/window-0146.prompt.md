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
[Block 5111 [VERSE]]
ཚིག་ཏུ་བརྗོད་པ་སྤངས་པ་སྟེ། །
བརྗོད་པ་ཀུན་གྱི་རྒྱུ་ཡི་མཆོག །

[Block 5112]
ཚིག་ཀུན་རབ་ཏུ་གསལ་བར་བྱེད། ཅེས་འབྱུང་ངོ་། །མི་ཤིགས་པ་ལ་ངེས་པར་འབྱུང་བའོ་ཞེས་པ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་འཁོར་ལོ་རྩིབས་བརྒྱད་པའི་ཡི་གེ་ཨ་ལས་འབྱུང་ཞིང་དེའི་སྤྲུལ་པ་ལས་བསྐྱེད་པའོ། །

[Block 5113]
ཆུའི་དཀྱིལ་འཁོར་ཏེ་མི་བསྐྱོད་པའི་ངོ་བོ་ཉིད་ཁ་དོག་དཀར་བ་ནི་ཞེས་པ་ལ་སྙིང་གར་གནས་པའི་ཕྱིར་དང་། ཆུའི་ཁམས་ཁ་དོག་དཀར་བའི་ཕྱིར་དང་། ཞི་བའི་ལས་ལ་བརྩོན་པའི་ཕྱིར་རོ། །

[Block 5114]
དལ་བར་རྒྱུ་བའི་ཕྱིར་རོ་ཞེས་པ་ནི་རླུང་གི་དཀྱིལ་འཁོར་བཞིན་དུ་ཆུ་ནི་དྲག་པར་རྒྱུ་བ་མ་ཡིན་ཏེ། འོན་ཀྱང་རང་བཞིན་གྱི་ཆུའི་ཁམས་དལ་བར་རྒྱུ་བ་སྟེ། སྟེང་དང་འོག་གི་གནས་ཀྱི་འབྲེལ་པས་དེ་རྣམས་ཀྱི་མྱུར་བ་དང་དམན་པ་དང་བར་མ་རྒྱུ་བ་ཡིན་ཏེ། ཆུ་བོ་དང་རྒྱ་མཚོ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 5115]
མེའི་དཀྱིལ་འཁོར་ཁ་དོག་དམར་པོའོ་ཞེས་པ་ལ་དེ་ཉིད་ཀྱི་རང་བཞིན་ལས་བྱུང་བ༌[^3023]གྲུ་གསུམ་པ་ལྐོག་མར་གནས་པའོ། །

[Block 5116]
གཡས་ནས་འབྱུང་བ་ཞེས་པ་ནི་སྣ་ཁུང་གཡས་པ་ལས་འབྱུང་བའོ། །

[Block 5117]
མེའི་དཀྱིལ་འཁོར་གྱི་རང་གི་ཁ་དོག་ནི་དམར་པོ་ཉིད་དོ། །

[Block 5118]
དབང་ཆེན་གྱི་དཀྱིལ་འཁོར་ཞེས་པ་ནི་སའི་དཀྱིལ་འཁོར་ཏེ། །དེ་ཉིད་ཀྱང་ཡི་གེ་ལཾ་ལས་བྱུང་བ༌[^3024]གསང་བའི་གནས་སུ་གྲུ་བཞི་པར་གནས་པའོ། །

[Block 5119]
གཉི་ག་ལས་འབྱུང་བར་ཞེས་པ་ནི་སྣ་ཁུང་གཉི་ག་ལས་འབྱུང་ངོ་།[^3025] །སའི་དཀྱིལ་འཁོར་ཁ་དོག་སེར་པོ་སྟེ་གསེར་གྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5120]
དེ་ཡང་དལ་བུས་དམན་པར་རྒྱུ་བ་ཡིན་ཏེ་ས་གཞི་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་ཡིན་པས་བརྟན་པའི༌[^3026]ཕྱིར་རོ། །

[Block 5121]
རླུང་གི་དཀྱིལ་འཁོར་ཏེ་ཞེས་པ་ནི་དེ་ཉིད་ཀྱི་ཡི་གེ་ཡཾ་ལས་བྱུང་བ་གཞུའི་དབྱིབས་ཅན་ལྟེ་བར་གནས་པའོ། །

[Block 5122]
ཁ་དོག་ནག་པོ་ཞེས་པ་རླུང༌[^3027]ནི༌[^3028]ངོ་བོ་ཉིད་ཀྱིས་ཁ་དོག་སྔོ་བ་ཡིན་པས་སོ། །

[Block 5123]
གཡོན་ནས༌[^3029]རྒྱུ་བ་ཡིན་པར་ཞེས་པ་ནི་སྣ་ཁུང་གཡོན་པ་ལས་རྒྱུ་བའོ། །

[Block 5124]
ཡིན་པར་ཤེས་པར་བྱ་སྟེ་ཞེས་པ་ནི་བསམ་པར་བྱའོ། །

[Block 5125]
དེ་རྣམས་ནི་དེ་བཞིན་གཤེགས་པའི་ངོ་བོ་ཉིད་འོད་ཟེར་བཞིའི་རབ་ཏུ་རྒྱུ་བ་ཞེས་པ་ནི་མི་བསྐྱོད་པ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 5126]
དེ་ནི་ཉེ་བར་མཚོན་པ་ཙམ་ཡིན་ཏེ། གོས་དཀར་མོ་ལ་སོགས་པ་ལྷ་མོ་བཞིའི་རང་བཞིན་དང་། ས་ལ་སོགས་པའི་ཁམས་བཞི་དང་། ཞི་བ་ལ་སོགས་པ་ཕྲིན་ལས་བཞི་དང་། དཀར་པོ་ལ་སོགས་པ་འོད་ཟེར་འབྱུང་བ། གཡས་དང་གཡོན་དང་གཉི་ག་དང་དལ་བུས་རྒྱུ་བ་དང་། ཝ་ལ་སོགས་པའི་ཡི་གེ་ལས་བྱུང་བ་དང་གྲུ་གསུམ་དང་ཟླུམ་པོ་དང་གཞུའི་དབྱིབས་དང་གྲུ་བཞི་དང་ཁ་དོག་དམར་པོ་ལ་སོགས་པ་དང་ལྡན་པར་ཤེས་པར་བྱའོ། །

[Block 5127]
བཤད་པ་ཡིན་ནོ་ཞེས་པ་ནི་སྡུད་པ་པོས་བཤད་པའོ། །

[Block 5128]
སྐུ་ལ་སོགས་པ་བསྐྱེད་པས་ན། །ཞེས་པ་ནི་འཇིག་རྟེན་ལས་འདས་པའི་ཡེ་ཤེས་ཀྱི་སྐུའི་རང་བཞིན་གྱི་སྐུ་གསུང་ཐུགས་རྫོགས་པར་བྱེད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 5129]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར་འོད་གསལ་བ་ལས་བཞེངས་ཏེ་ཞེས་སྨོས་ཏེ། རིམ་པ་བཞི་པས་ཐོབ་པའི་དེ་ཁོ་ན་ཉིད་ལས་འབྱུང་བའོ། །

[Block 5130]
བདེན་པ་གཉིས་ཀྱི་བདག་ཉིད་ཅན་གྱི་ཞེས་པ་ནི་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ཀྱི་རང་བཞིན་ནོ། །

[Block 5131]
ལྷའི་དཀྱིལ་འཁོར་ཡིན་པར་ཤེས་པར་བྱའོ་ཞེས་པ་ནི་མི་བསྐྱོད་པ་ལ་སོགས་པ་དེ་བཞིན་གཤེགས་པའི་ཚོགས་བསྒོམ་པར༌[^3030]བྱའོ། །

[Block 5132]
ཐམས་ཅད་མཁྱེན་པའི་གོ་འཕང་ཐོབ་པར་འདོད་པའི་ཞེས་པ་ནི་རྣལ་འབྱོར་པས་ཞེས་ཚིག་ལྷག་མའོ། །

[Block 5133]
དེ་ནི་བྱེད་པའི་དྲུག་པ་ཡིན་ནོ། །

[Block 5134]
དགོངས་པ་ནི་འདི་ཡིན་ཏེ། རེ་ཞིག་དང་པོའི་རྣལ་འབྱོར་པས་ཅིག་ཅར་དུ་ཡེ་ཤེས་ཀྱི་སྐུ་དམིགས་ལ། ལྟེ་བའི་ཕྱོགས་སུ་རྩིབས་བརྒྱད་པའི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་འཁོར་ལོའི་ཡི་གེ་ལས་ཡ་ར་ལ་ཝ་སྤྲུལ་ཏེ། དེ་དག་ཡོངས་སུ་གྱུར་པ་ལས་ལྐོག་མ་ལ་སོགས་པའི་གནས་བཞི་ལས༌[^3031]གྲུ་གསུམ་དང་ཟླུམ་པོ་དང་ཟླ་གམ་དང་གྲུ་བཞི་པའི་མེ་དང་ཆུ་དང་རླུང་དང་སའི་དཀྱིལ་འཁོར་རྣམས་བསྒོམས་ལ། དེ་རྣམས་རེ་རེ་ལ་ཡི་གེ་གསུམ་དམིགས་པ་སྔོན་དུ་འགྲོ་བར་འཇུག་པ་ལ་སོགས་པ་གསུམ་གྱི་རིམ་པས་བཟླས་པར་བྱ་སྟེ། དེ་ལས་བྱུང་བའི་འོད་ཟེར་གྱི་འཁོར་ལོས་ཕྲ་མོའི་རྣལ་འབྱོར་བསླབ་པར་བྱའོ། །

[Block 5135]
དེའི་རིམ་པ་ནི་མེའི་དཀྱིལ་འཁོར་ལ་ཁ་དོག་དམར་པོ་འོད་ཟེར་སྣ་ཁུང་གཡས་པ་ལས་འབྱུང་ཞིང་གདོང་གི་སྣ་རྩེར༌[^3032]ཐུན་ཕྱེད་ཕྱེད་ཀྱི་དུས་སུ་ཟིན་ན་དེའི་ཚེ་རྣལ་འབྱོར་པས་འབད་རྩོལ་མེད་པར་དབང་གི་ལས་འགྲུབ་པར་འགྱུར་རོ། །

[Block 5136]
དེ་བཞིན་དུ་རླུང་གི་དཀྱིལ་འཁོར་ལས་ཁ་དོག་ལྗང་སེར་སྣ་བུག་གཡོན་པ་ནས་འབྱུང་ཞིང་གདོང་གི་སྣ་རྩེར་ཐུན་ཕྱེད་ཕྱེད་ཀྱི་དུས་སུ་ཟིན་ན་དེའི་ཚེ༌[^3033]རྣལ་འབྱོར་པས་འབད་རྩོལ་མེད་པར་དགུག་པ་དང་མངོན་སྤྱོད་དག་གྲུབ༌[^3034]བོ། །

[Block 5137]
དེ་བཞིན་དུ་སའི་དཀྱིལ་འཁོར་ཁ་དོག་སེར་པོ་སྣ་ཁུང་གཉིས་ཀ་ལས་འབྱུང་ཞིང་གདོང་གི་སྣ་རྩེར་ཐུན་ཕྱེད་ཕྱེད་ཀྱི་དུས་སུ་ཟིན་ན། དེའི་ཚེ་རྣལ་འབྱོར་པས་འབད་རྩོལ་མེད་པར་རྒྱས་པའི་ལས་གྲུབ་བོ། །

[Block 5138]
དེ་བཞིན་དུ་ཆུའི་དཀྱིལ་འཁོར་ལས་གཉི་ག༌[^3035]ལས་བྱུང་བའི་ཁ་དོག་དཀར་པོ་འོད་ཟེར་འབྱུང་ཞིང་གདོང་གི་སྣ་རྩེར་ཐུན་ཕྱེད་ཕྱེད་ཀྱི་དུས་སུ་ཟིན་ན། དེའི་ཚེ་རྣལ་འབྱོར་པས་འབད་རྩོལ་མེད་པར་ཞི་བའི་ལས་གྲུབ་བོ། །

[Block 5139]
འོད་ཟེར་གྱི་ཐིག་ལེ་དེ་ལས་སྔ་མ་བཞིན་དུ་བརྟན་པའི་རྟགས་མཐོང་བ་སྔོན་དུ་འགྲོ་བར་འོད་ཟེར་དང་ཕྱག་མཚན་དང་དེ་བཞིན་གཤེགས་པའི་ཕྱག་རྒྱ་ཆེན་པོ་སྤྲོ་ཞིང་སླར་ཡང་དཀྱིལ་འཁོར་དེ་ཉིད་དུ་འཇུག་པ་ནི། གཏི་མུག་གི་རིགས་ཅན་གྱི་རྣལ་འབྱོར་པའི་ཕྲ་མོའི་རྣལ་འབྱོར་བསྒོམ་པའོ། །

[Block 5140]
འདི་དང་སྔ་མ་གཉིས་བསྡུས་ཏེ་རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་པའི་སྐུ་རྡོ་རྗེ་ལ་སོགས་པའི་དབྱེ་བས་ཕྲ་མོའི་རྣལ་འབྱོར་རྣམ་པ་གསུམ་བསྟན་ཏོ། །

[Block 5141]
རིན་ཆེན་འབྱུང་ལྡན་དང་དོན་ཡོད་གྲུབ་པའི་རྣལ་འབྱོར་པ་དག་གིས་ཀྱང་། སྨིན་མཚམས་དང་ལྟེ་བའི་དབུས་སུ་ཐིག་ལེ་ཙམ་བསྒོམ་པར་བྱའོ། །

[Block 5142]
དེ་ལ་གསང་བའི་གནས་ཀྱི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེ་གང་ཡིན་པ་དེ་ཉིད་ཐུར་དུ་སེལ་བའི་རླུང་བཟློག་ནས་གྱེན་དུ་འདྲེན་པར་བསྒོམ་པར་བྱའོ་ཞེས་བླ་མའི་མན་ངག་གོ། །

[Block 5143]
ཡང་ན་སྐུའི་རིགས་ལ་སོགས་པ་ལ་བསྡུས་པའི་ཕྱིར་ལོགས་སུ་བསྒོམ་པར་མི་བྱ་སྟེ། གང་གི་ཕྱིར་རིན་ཆེན་འབྱུང་ལྡན་ནི་ང་རྒྱལ་གྱི་རང་བཞིན་ནོ། །

[Block 5144]
ང་རྒྱལ་ཡང་གཏི་མུག་ལས་འབྱུང་བའམ་ཞེ་སྡང་ལས་བྱུང་བའོ། །

[Block 5145]
དེ་ལ་གཏི་མུག་ལས་འབྱུང་ན་རྣམ་པར་སྣང་མཛད་ཀྱི་རིགས་ལ་བསྡུའོ། །

[Block 5146]
ཞེ་སྡང་ལས་འབྱུང་ན་མི་བསྐྱོད་པའི་རིགས་ལ་བསྡུའོ། །

[Block 5147]
དོན་ཡོད་གྲུབ་པ་ཡང་ཕྲག་དོག་གི་རང་བཞིན་ཏེ་ཕྲག་དོག་ཀྱང་ཞེ་སྡང་ལས་འབྱུང་བས་ན་ཐུགས་རྡོ་རྗེའི་རིགས་ཀྱི་ནང་དུ་བསྡུའོ། །

[Block 5148]
དེའི་ཕྱིར་རྣམ་པར་སྣང་མཛད་དང་མི་བསྐྱོད་པ་དག་གི་ཕྲ་མོའི་རྣལ་འབྱོར་གྱི་བསྒོམ་པ༌[^3036]གང་ཡིན་པ་དེ་དག་ནི་དེ་ཉིད་རིན་པོ་ཆེ་དང་དོན་ཡོད་གྲུབ་པའི་རྣལ་འབྱོར་པས་བསྒོམ་པར་བྱ་ཞེས་གུད་ནས་བཤད་པར༌[^3037]མི་བྱའོ། །

[Block 5149]
དེ་ཉིད་ཀྱི་ཕྱིར་རྒྱུད་ཕྱི་མ་ལས་ཀྱང་།

[Block 5150 [VERSE]]
སྐུ་གསུང་ཐུགས་ནི་རྣམ་པ་གསུམ། །
གསང་བ་ཞེས་བྱ་མངོན་པར་བཤད། །
རིགས་ནི་རྣམ་པ་བརྒྱར༌[^3038]བཤད་དེ། །
མདོར་བསྡུས༌[^3039]པས་ནི་རྣམ་པ་ལྔ། །
--- END BLOCKS ---
