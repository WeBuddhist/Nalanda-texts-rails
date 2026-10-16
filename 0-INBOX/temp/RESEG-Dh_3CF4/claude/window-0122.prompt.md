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
[Block 4271]
འགྲོ་བ་འདི་དག༌[^2740]ངོ་བོ་ཉིད་ཀྱིས་ངེས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ཕྱི་དང་ནང་གི་དངོས་པོ་རྣམས་ལ་བྱེད་པ་པོ་མེད་པར་ཡང་སྣ་ཚོགས་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 4272]
རྒྱུ་མེད་པར་འབྱུང་བར༌[^2741]མི་རིགས་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་ཀྱིས་མེད་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4273]
གཅིག་གཅིག༌[^2742]ཡོད་ཅེས་བྱ་བ་ནི་རང་དགས་སྤྲུལ་པར༌[^2743]བྱེད་པ་སྟེ། འཇིག་རྟེན་སྣ་ཚོགས་སོ། །

[Block 4274]
ཕྱིས་ཀྱང་མཉམ་དུ་མེད་པར་བྱེད། །ཅེས་བྱ་བ་ནི། ཅིའི་ཕྱིར་ཞེ་ན། བྱེད་པ་པོ་རང་དགའི་ཁྱད་པར་གྱིས་ཤིང་རྟ་ལ་སོགས་པ་རྣམ་པ་སྣ་ཚོགས་པའི་དངོས་པོ་འབྱིན་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 4275]
[^2744]དེའི་ཡང་རང་དགའི་དབང་གིས་མི་སྣང་བར་བྱེད་པ་ལྟ་བུའོ། །

[Block 4276]
འདི་དག་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པ་དག་གོ། །

[Block 4277]
སྔོན་གྱི་ལས་ཀྱིས་བྱས་ཞེས་བྱ་བ་ལ། སྔོན་གྱི་ལས་ཀྱིས་བྱས་པ་ཡིན་པས་ནི་སྔོན་གྱི་ལས་ཀྱིས་བྱས་པ་སྟེ། སྔོན་གྱི་ལས་ལས་བྱས་པའི་རྒྱུས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4278]
བདེ་བ་དང་མི་བདེ་བ་ཞེས་བྱ་བ་ནི་བདེ་བ་དང༌[^2745]སྡུག་བསྔལ་ཡིན་ཏེ། སྔོན་གྱི་ལས་ཀྱིས༌[^2746]བྱས་པས་ཞེས་བསྟན་ནས་དེའི་འོག་ཏུ་བདེ་བ་དང་མི་བདེ་བ་གཟུང་ངོ་། །སྐྱེ་བ་སྔ་མར་བྱས་པའི་ལས་ཉིད་ཀྱིས་ནི་སངས་རྒྱས་པ་དང་ཡང་འདྲ་བ་ཉིད་དུ་སྟོན་ཀྱང་གང་བྱས་པ་དེ་ངེས་པར་སྔ་མའི་ལས་ཀྱིས༌[^2747]བྱས་པ་ཉིད་དུ་སྟོན་པ་ཡིན་པས་དེ་བསྟན་པའི་ཕྱིར། འབད་པའི་མཐུས་བྱས་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་པ་ཡིན་ཏེ། འདིས་ནི་དེ་ལྟར༌[^2748]བྱུང་བའི་སྐྱེས་བུ་བྱེད་པའི་རྐྱེན་འགོག་པ་ཡིན་ནོ། །

[Block 4279]
བདེ་བ་དང་སྡུག་བསྔལ་གྱི་བྱེད་པའི་འགྲོ་བ་རྣམས་ཀྱི་བྱེད་པ་པོ་གཅིག་ཏུ་མི་རིགས་པ་ཉིད་དེ། ཅིའི་ཕྱིར་ཞེ་ན། དུས་གཅིག་ཏུ་གནས་པ་མང་པོ་དུ་མ་སྟེ། མཐའ་ཡས་པའི་དངོས་པོ་བྱེད་པར་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 4280]
བདེ་བར་བྱེད་པ་ལ་མཁས་པ་ནི་བདེ་བར་བྱེད་པ་ལ་མཁས་པ་སྟེ། དེ་ཡང་སྡུག་བསྔལ་བར་མཐོང་བའི་ཕྱིར་ཏེ། དེ་བས་ཐམས་ཅད་སྔོན་གྱི་ལས་ལས་གྱུར་པ་ཉིད་དུ་གཟུང་ངོ་། །སྔར་བསྟན་པའི་སྐྱོན་དང་། དབང་ཕྱུག་རྒྱུར་བྱེད་པའི་སྐྱོན་བསྟན་པ་ཡིན་ཏེ། སྣ་ཚོགས་པའི་ཕྱིར་ལས་ཀྱི་བྱེད་པ་པོ་ལས་དངོས་པོ་སྐྱེ་བའི་རྒྱུ་ཉིད་དུ་ནི་རུང་སྟེ། དུས་གཅིག་ཏུ་སོ་སོར་གནས་པ་མང་པོ་དཔག་ཏུ་མེད་པའི་དངོས་པོ་སྐྱེ་བ་ནི་རིགས་པ་ཉིད་དོ། །

[Block 4281]
ཁ་དོག་ནི་སྔོན་པོ་ལ་སོགས་པའོ། །

[Block 4282]
ཡོན་ཏན་ནི་དྲི་དང་། རོ་དང་། རེག་བྱ་ལ་སོགས་པའི་མཚན་ཉིད་དོ། །

[Block 4283]
ལྡན་པ་ནི་དབྱིབས་ཀྱི་ཁྱད་པར་དང་། ཁ་དོག་དག༌[^2749]དང་། ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 4284]
རྣམ་པ་སྣ་ཚོགས་པའི་ཁ་དོག་དང་། ཡོན་ཏན་དང་ལྡན་པ་གང་ཡིན་པ་དེ་ནི་རྣམ་པ་སྣ་ཚོགས་ཁ་དོག་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 4285]
འགྲོ་བ་རྣམས་ཀྱི་ལས་ཀྱི་རྒྱུ་མེད་པར་བསྟན་ཏེ། དུས་གཅིག་ཏུ་འབྱུང་ཞེས་བྱ་བས༌[^2750]བསྟན་པ་ནི་དུས་གཅིག་ཏུ་སོ་སོར་གནས་པ་མཐའ་ཡས་པ་མང་པོ་རྣམས་དཔག་ཏུ་མེད་པའི་དངོས་པོར་སྐྱེ་བར་མཐོང་བའི་ཕྱིར་ལས་གང་ཡིན་པ་དེ་ནི་མེད་དེ། དེ་ལ་དུས་གཅིག་ཏུ་དངོས་པོ་མཐའ་ཡས་པ་དཔག་ཏུ་མེད་པའི་དངོས་པོ་སྐྱེ་བ་མེད་པར་འགྱུར་ན་ནི་ཤིང་རྣམ་པ་སྣ་ཚོགས་པའི་ཁ་དོག་དང་ལྡན་པ་སྣང་བས་དེ་རྣམས་ཀྱི་ལས་ནི་མེད་དོ། །

[Block 4286]
དེ་བས་ན་རྒྱུ་མེད་པ༌[^2751]ཉིད་དེ་རང་གི་ས་བོན་གྱི་རྒྱུས་སོ། །

[Block 4287]
རྐྱེན་ཡང་མེད་དེ་དབང་ཕྱུག་བྱེད་པ་པོས་འདོད་པ་དེའི་ཉེས་པར་ཐལ་བའི་ཕྱིར་རོ། །

[Block 4288]
སྔོན་གྱི་ལས་གྱུར༌[^2752]འདོད་པ་ཡང་མ་ཡིན་ཏེ། ལས་མེད་པར་ཁ་དོག་དང་ཡོན་ཏན་ལ་སོགས་པ་རྣམ་པ་སྣ་ཚོགས་པའི་དངོས་པོ་སྐྱེ་བར་སྣང༌[^2753]བའི་ཕྱིར་རོ། །

[Block 4289]
འཇིག་རྟེན་ཕ་རོལ་ཡང་མེད་དེ། ཤིང་དེ་དག་ཉིད་ཞིག་པར་གྱུར་ན་ཕྱིས་ཡང་སྐྱེ་བར་མ་མཐོང་བའི་ཕྱིར་ཏེ། དེ་བས་ན་དེ་བཞིན་དུ་འགྲོ་བ་འདི་དག་ཐམས་ཅད་གནས་པར་འདོད་དོ། །

[Block 4290]
རྒྱལ་རིགས་ཀྱི་གཙུག་ལག་ལས་འབྱུང་བ་ཞེས་བྱ་བ་ནི། ལུགས་ཀྱི་བསྟན་བཅོས་ལས་འབྱུང་བའོ། །

[Block 4291]
ལུགས་ཀྱི་བསྟན་བཅོས་ཉིད་གཡོ་བ་དང་དགྲ་ཐབས་ཡིན་པས། ལུགས་ཀྱི་བསྟན་བཅོས་ཀྱི་གཡོ་བ་དང་དགྲ་ཐབས་ཡིན་ནོ། །

[Block 4292]
གཡོ་བ་དང་དགྲ་ཐབས་བསྟེན་པ་ནི་གཡོ་བ་དང་དགྲ་ཐབས་འབྲེལ་པའོ། །

[Block 4293]
སྙིང་རྗེ་མེད་ཅིང་སྐྱོན་དང་བཅས་པ། ཆོས་དང་འགལ་བ་ལ་ཞེས་བྱ་བ་ནི་སྲོག་གཅོད་པ་ལ་སོགས་པ་དང་བཅས་པའོ། །

[Block 4294]
གྲིབ་མ་རྣམས་ཀྱི་ཤིང་ཡིན་པས་གྲིབ་མའི་ལྗོན་ཤིང་ངོ་། །གྲིབ་མའི་ལྗོན་ཤིང་དག་ལ་བརྟེན་པ་གང་ཡིན་པ་དེ་ནི་གྲིབ་མའི་ལྗོན་ཤིང་ལ་བརྟེན་པའོ། །

[Block 4295]
བྱས་པ་གཟོ་བའི་སྤྱོད་པ༌[^2754]གང་ཡིན་པ་དེ་བྱས་པ་གཟོ་བའོ། །

[Block 4296]
དེས་བསྲུང་བ་ནི་འཐོབ་པར་འདོད་པའོ། །

[Block 4297]
བསྲུང་བ་དེ་ཉིད་སྨྲས་པ། དེ་དག་ཇི་སྲིད་དགོས་པའི་དུས་ལ་མ་བབ་པ་དེ་སྲིད་དུ་རང་གི་གྲགས་པ་བསྲུང་བའོ། །

[Block 4298]
དགོས་པ་བྱུང་ན་ཞེས་བྱ་བ་ནི་དགོས་པའི་དུས་ལ་བབ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4299]
དེ་ལྟ་བ༌[^2755]ལྔ་པོ་འདི་དག་བྱས་པ་འདིའི་བསྡུས་པའི་དོན་ནི་རང་བཞིན་གྱི་དབང་དུ་བྱས་ནས་ལྟ་བ་རྣམ་པ་གཉིས་ཏེ། རྒྱུ་མེད་པར་སྨྲ་བ་དང་། མི་མཐུན་པའི་རྒྱུར་སྨྲ་བའོ། །

[Block 4300]
རྒྱུ་མེད་པར་སྨྲ་བའི་དབང་དུ་བྱས་པ་ནི་ལྟ་བའི་རྣམ་པ་དང་པོའོ། །

[Block 4301]
དབང་ཕྱུག་རྒྱུར་སྨྲ་བ་ནི་མི་མཐུན་པ་རྒྱུར་སྨྲ་བའོ། །

[Block 4302]
ཐམས་ཅད་སྔོན་གྱི་ལས་ཀྱིས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ད་ལྟར་བྱུང་བའི་ལས་རྣམ་པར་གཅོད་པའོ། །

[Block 4303]
དེ་བཞིན་དུ་མཐོང་བའི་ཆོས་ལ་མྱ་ངན་ལས་འདས་པར་འདོད་པ་ཆད་པར་ལྟ་བ་སྟེ། འཇིག་རྟེན་ཕ་རོལ་རྣམ་པར་གཅོད་པའོ། རྒྱལ་རིགས་ཀྱི་ཆོས་ཀྱི༌[^2756]གཙུག་ལག་ལས་འབྱུང་བར་སྨྲ་བ་ནི་མངོན་པར་མཐོ་བའི་རྒྱུ་མི་མཐུན་པར་སྨྲ་བའོ། །

[Block 4304]
ལྟ་བའི་རྣམ་པ་འདི་དག་ལས་དང་པོ་ལས༌[^2757]བརྩམས་པ་ནི་གཉིས་སོ། །

[Block 4305]
བར་མ་ལས་བརྩམས་པ༌[^2758]ནི་གཅིག་པའོ། །

[Block 4306]
དེ་ལས་གཞན་པ་ལས་བརྩམས་པ་ནི་གཉིས་ཏེ། དེ་ལྟ་བས་ན་ལྟ་བ་འདི་དག་གི་གོ་རིམས་ནི་འདི་ཡིན་ནོ། །

[Block 4307]
སྐྱེ་བོ་སྡིག་པ་ཅན་རྣམས་དང་བསྟེན་པ༌[^2759]ཞེས་བྱ་བ་འདིས་ནི་རྐྱེན་བསྟན་ཏོ། །

[Block 4308]
བློ་གཞན་གྱི་དྲིང་ལ་འཇོག་པས་ཞེས་བྱ་བ་འདིས་ནི་རྒྱུ་བསྟན་ཏོ། །

[Block 4309]
ལྟ་བས་བྱས་པ་ཉིད་གཡང་སར་ལྷུང་བ་ཉིད་ཡིན་པས་ལྟ་བ་ངན་པའི་གཡང་སར་ལྟུང་བ་ཞེས་བརྗོད་དོ། །

[Block 4310]
[^2760]ངན་སོང་གི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
