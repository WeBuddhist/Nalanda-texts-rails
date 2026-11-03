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
[Block 6126]
དེ་རྣམས་ཕྱག་འཚལ་བ་ནི་རྒྱལ་ཕྲན་དྲེགས་པ་རྣམས་ཕྱག་འཚལ་བའོ། །

[Block 6127]
འདིས་ནི་ཡུལ་གཞན་དུ་གྱུར་བའི་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 6128]
དུལ་བ་ལ་དགའ་བས་ཞེས་བྱ་བས༌[^3927]མ་འོངས་པའི་འབྲས་བུ༌[^3928]རྒྱུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 6129]
རྒྱལ་པོའི་རིགས་དེ་དང་དེ་དག་བདེ་བ་དང་སྡུག་བསྔལ༌[^3929]འདྲ་བར་འགྱུར་བ༌[^3930]སྟེ། དེའི་བདེ་བ་སྡུག་བསྔལ་མཉམ་པའོ། །

[Block 6130]
སྦྱིན་པ༌[^3931]ཐོབ་པས་བྲམ་ཟེ་མགུ་ཞིང་གཡེངས། །[^3932]ཞེས་བྱ་བ་ནི་ཕོངས་པའི༌[^3933]སྐྱེ་བོ་མགུ་བ་ཕུན་སུམ་ཚོགས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 6131]
འབངས་རྣམས་དྲེགས་པས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། གླུ་སྒྲ་སྙན་པ་དགོད་པས་ཞེས་བྱ་བའི་བར་གྱིས་ནི་ཉེ་བར་ལོངས་སྤྱོད་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 6132]
གཅིག་ལ་གཅིག་འཇུས་དགའ་བ་རྣམས་པར༌[^3934]འཕེལ། །ཞེས་བྱ་བ་ནི་སྡུག་པ་དང་ཕྲད་པའི་བདེ་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 6133]
གཏམ་སྙན་སྐྱེལ་བ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འོག་མ་ཕྱེད་འདིས་ནི་གང་འདོད་པ་བཙལ་ཏེ་མ་རྙེད་པ་དེ་ཡང་སྡུག་བསྔལ་བའོ་ཞེས་བྱ་བ་དེའི་གཉེན་པོ་བདེ་བའི་ཕྱོགས་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 6134]
སྒོ་རྣམས་ཕྱེ་ཞིང་བཙོན་དུ་བཟུང་བ་མེད། །ཅེས་བྱ་བས་ནི་བདེ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6135]
སྲང་གི་བཞི་མདོ་རྒྱལ་མཚན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ནི་གྲོང་ཁྱེར་གྱི་རྒྱན་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 6136]
ཁང་པ་ཆེན་པོའི་སྟེང༌[^3935]ནས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་སྐྱེ་བོ་སྦྱིན་པ་པོའི་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 6137]
སྙིང་སྟོབས་དང་ལྡན་པ་དང་། བསོད་ནམས་བསགས་པའི་ཁྱད་པར་འདི་གཉིས་ཀྱིས་ནི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། ཡེ་ཤེས་དང་། བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་རྒྱུ་ཡོངས་སུ་གཟུང་བའི༌[^3936]ཕྱིར། བསྲུང་བ་ལེགས་པར་བྱས་པས་ཞེས་བྱ་བ༌[^3937]ཡིན་ཏེ། ཡོངས་སུ་གཟུང་བའི༌[^3938]ཕྱིར་རེ། །རབ་ཏུ་ཞི་བ་ཞེས་བྱ་བ་ནི་ལུས་དང་ངག་གི་རབ་ཏུ་ཞི་བའོ། །

[Block 6138]
དུལ་བ་ནི་བྱ་བ་མ་ཡིན་པ་ལས་ལྡོག་པའོ། །

[Block 6139]
ཡིད་གཞུངས་པའི༌[^3939]ཡོན་ཏན་ནི་ཤེས་རབ་ཀྱི་ཡོན་ཏན་ཏེ། སྲི་ཞུ་ཆེ་བ་དང་། མཉན་པ་ཟིན་པ་དང་། འཛིན་པ་དང་། རྣམ་པར་ཤེས་པ་དང་། རྟོག་པ་དང་། སེལ་ནུས་པས་མངོན་པར་འཇུག་པའི་མཚན་ཉིད་དོ། །

[Block 6140]
རབ་ཏུ་ཞི་བ་དང་། དུལ་བ་དང་། ཤེས་རབ་ཀྱི་ཡོན་ཏན་དེ་དག་དང་ལྡན་པ་ནི་རབ་ཏུ་ཞི་བ་དང་། དུལ་བ་དང་། ཤེས་རབ་ཀྱི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 6141]
མ་དྲིས་པ་ནི་མ་ཤེས་པའོ། །

[Block 6142]
གཉེན་དུ་མ་འབྲེལ་པའི་ཞེས་བྱ་བ་ནི་གང་དེ་ལ་རིགས་ལ་སོགས་པའི་མཚན་ཉིད་ཀྱིས་ན༌[^3940]གཉེན་དུ་འབྲེལ་བ་སྟེ། གཉེན་དུ་འབྲེལ་པ་དེ་མེད་པའི་ཕྱིར་རོ། །

[Block 6143]
དམ་པའི༌[^3941]རིང་དུ་གནས་གྱུར་ཀྱང་། །ཞེས་བྱ་བ་ནི་རབ་ཏུ་བསྐལ་པའོ། །

[Block 6144]
རྒྱུ་གསུམ་གྱིས་ནི་བྱམས་པར་འགྱུར་ཏེ། ཡོངས་སུ་འདྲིས་པ་དང་། གཉེན་དུ་འབྲེལ་བ་དང་། ཉེ་བ་ན༌[^3942]གནས་པ་སྟེ། གསུམ་པོ་འདིའི་དབང་དུ་བྱས་པའོ། །

[Block 6145]
སྡུག་པ་དང་བྲལ་བས་སྡུག་བསྔལ་ཉིད་ཀྱི་ཕྱིར་ཏེ། དར་བ་ཞེས་བྱ་བ་ནི་བདག་གི་ཡོ་བྱད་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 6146]
རྒུད་པ་ཞེས་བྱ་བ་ནི་འཇིག་ཅིང་གཞན་དུ་འགྱུར་བས་དེ་མི་རྟག་པའོ། །

[Block 6147]
བདག་ལ་ཕན་པ་བགྱི་བར་འཚལ། །ཞེས་བྱ་བ་ནི་དེར་གནས་ནའོ། །

[Block 6148]
ཐུགས་དཔག་མཛད་དུ་གསོལ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་གཟུང་བར་གསོལ་བའོ། །

[Block 6149]
གླང་པོ་ཆེ་མདའ་དུག་ཅན་གྱིས་ཚབས་ཆེར་ཕོག་པ་བཞིན་དུ་དེའི་མྱ་ངན་གྱིས༌[^3943]སེམས་གདུངས་པ་དང་། རྒྱ་མཚོ་རབ་ཏུ་ཟབ་པ་རླུང་གིས་སློངས་པ༌[^3944]བཞིན་དུ་འཁམས་ཏེ་འདར་བར་གྱུར་པ་ཞེས་དེ་ལྟར་སྦྱར་རོ། །

[Block 6150]
བདག་ཉིད་བུང་བར༌[^3945]བྱེད་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད༌[^3946]པོ་འདིས་ནི་སུས་དེ་ལྟར་གནོད་པ་བྱས་ཞེས་པའོ། །

[Block 6151]
སུ་ཡིས༌[^3947]ང་ཡི༌[^3948]མི་ཞེས་བྱ་བ་ཕྱེད་འོག་མས་ནི།

[Block 6152 [VERSE]]
སུ་ཞིག་གསད་པར་བྱ་ཞེས་བསྟན་པའོ། །
དང་པོ་མངལ་དུ་ཞུགས་པའི་ནུབ་མོ་ནས། །

[Block 6153]
ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི། སྐད་ཅིག་མས་འཇིག་ཅིང་མི་རྟག་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6154]
ཡང་ན་སྐྱེ་བ་དང་གནས་པ་བསྟན་ཏོ། །

[Block 6155]
དང་པོ་མངལ་དུ་ཞུགས་པའི་ནུབ་མོ་ཞེས་བྱ་བ་འདིས་ནི་སྐྱེ་བའོ། །

[Block 6156]
དེ་ནས་བརྩམས་ཏེ་གཞན་དུ་མ་གོལ་བར། །ཞེས་བྱ་བ་འདིས་ནི་གནས་པ་བསྟན་ཏོ། །

[Block 6157]
གནས་པ་ཞེས་བྱ་བ་ནི་སྐྱེ་བའི་གནས་ཏེ། སྐད་ཅིག་མའི༌[^3949]རེ་རེས་འཆི་བདག་གི་དྲུང་དུ་ཉེ་བར་འགྲོ་བའོ། །

[Block 6158]
ཐབས་དང་རབ་ཏུ་ལྡན་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི། རྒ་བ་དང་། མི་རྟག་པ་ཉིད་བསྟན་ཏེ། ཐབས་དང་ལྡན་ཡང་སུ་ཡང་ཐར་པ་མེད། །ཅེས་བྱ་བས་ནི་མཛངས་པས༌[^3950]ཀྱང་དགའ་བ༌[^3951]དང་། འཆི་བ་བཟློག་པར་མི་ནུས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6159]
མཐུ་ཡོད་ཀྱང་ཞེས་བྱ་བ་འདིས་ནི་གཟུགས་ཀྱི་ལུས་ཀྱི་སྟོབས་ཀྱིས་བཟློག་པར་མི་ནུས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6160]
དེ་ལྟར་ཚིགས་བཅད་དེ་གཉིས་ཀྱིས་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་བཞི་དང་ལྡན་པའི་ཕྱིར། འདུས་བྱས་རྣམས་ཡོངས་སུ་དོར་བ་ཉིད་དུ་སྟོན༌[^3952]ཏོ། །

[Block 6161]
འདུས་བྱས་ཀྱི་མཚན་ཉིད་བཞི་ནི་སྐྱེ་བ་དང་། གནས་པ་དང་། རྒ་བ་དང་མི་རྟག་པའོ། །

[Block 6162]
མི་རྟ་གླང་ཆེན་ཤིང་རྟ་མང་པོ་ཞེས་བྱ་བ་ནས་བརྩམས་པའི་ཚིགས་བཅད་ཐམས་ཅད་ཀྱིས་ནི་འཆི་བ་མི་ཟློགས་པ་ཉིད་ལས་བརྩམས་ནས་སོ། །

[Block 6163]
ཚིགས་བཅད་འདི་དག་གི་དོན་ནི་འདི་ཡིན་ཏེ། མི་དང་། དུད་འགྲོ་དང་། ལྷ་དང་། ལྷ་མ་ཡིན་གྱི་འགྲོ་བ་ལ་གནས་པས་ཀྱང་འཆི་བ་ལས་མི་ཟློགས་པ༌[^3953]ཉིད་དུ་བསྟན་ཏོ། །

[Block 6164]
དམྱལ་བ་རྣམས་སུ་ནི་དེའི་བསམ་པའི་སྐབས་མེད་པའི་ཕྱིར། དམྱལ་བ་འདིར་མ་སྨོས་སོ། །

[Block 6165]
དེ་ལྟར་རེ་ཞིག་ཚིགས་བཅད་འདི་དག་གི་ཁྱད་པར་ནི་འདི་ལྟར་སྣང་སྟེ། ཁྱད་པར་གཞན་ནི་གང་ཡང་མེད་དོ། །
--- END BLOCKS ---
