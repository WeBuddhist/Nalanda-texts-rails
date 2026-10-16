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
[Block 596]
རེ་བ་བསྐང་བ་ཉི་ཚེར་མ་ཟད་དེ། གཞན་ཡང་མིག་གཉི་ག་ཡང་ངས་སྦྱིན་གྱིས་ཞེས༌[^303]བྱ་བ་ཡིན་ནོ། །

[Block 597]
ཡང་ན་འདིའི་དོན་ནི་མིག་གཅིག་སྦྱིན་པ་ཉིད་ཇི་ལྟར་རེ་བ་བསྐང་བ་ཡིན་ཏེ། རེ་བ་སྐོང་བ༌[^304]ནི་རེ་ཞིག་ཇི་ལྟར་ཡང་མིག་གཉིས་ཐོབ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 598]
འོན་ཀྱང་འདིས་ཡིད་ལ་རེ་བ་བཞིན་དུ་སློང་བར་མི་ནུས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། མི་སྦྱིན་སྙམ་པ་དང་། མིག་གཉིས་བསླངས་ན་རྒྱལ་པོ་ལ་གནོད་པར་འགྱུར་བ་དང་། གཞན་གྱི་སེམས་སྲུང་བར་སྟོན་པ་ཡིན་ཏེ། ཡིད་ལ་རེ་བ་ནི་རེ་ཞིག་མིག་གཉི་ག་ཐོབ་པ་ཉིད་དེ། [^305]དེས་ན་དེ་ཉིད་སྨྲས་པ། ཡིད་ལ་རེ་བ་ཡོངས་སུ་བསྐང་བ་ཞེས་སྨོས་པ་དེ་ཉིད་ནི་མིག་གཉིས་ཀྱང་ནི་ངས་སྦྱིན་གྱིས་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 599]
གཞན་དུ་ཇི་ལྟར་རེ་བ་ཡོངས་སུ་སྐོངས་པར་འགྱུར༌[^306]ཏེ། ངའི་མིག་ནི་ཡ་གཅིག་འདོད་པ་ལ་ཞེས་བྱ་བ་སྟེ། སློང་བ་ལ་གཉིས་སྦྱིན་པའི་དོན་ནི་འདི་ཡིན་ནོ། །

[Block 600]
ཤུགས་ཀྱིས་སྐྲག་པ་ནི་ཤུགས་ཀྱིས་སྐྲག་པ་སྟེ། རྟབས་པ༌[^307]དང་བཅས་པའི་ཤུགས་ཀྱིས་སྐྲག་པའོ། །

[Block 601]
རྟབས་པ༌[^308]དང་བཅས་པ་དང་ཤུགས་ཀྱིས་སྐྲག་པ་དེ་གཉིས་ཀྱིས་གདུངས་པའི་ཡིད་གང་ཡིན་པ་དེ་ནི་རྟབས་པ་དང་བཅས་པའི་ཤུགས་ཀྱིས་སྐྲག་པ༌[^309]དང་བཅས་པ་ཡིན་ནོ། །

[Block 602]
རྟབས་པ༌[^310]ནི་ལུགས་ཀྱི་འགྱུར་བའོ། །

[Block 603]
ཤུགས་ནི་སྐྱོ༌[^311]བའོ། །

[Block 604]
སྐྲག་པ་ནི་སེམས་སོ། །

[Block 605]
མི་རིགས་པ་དང་གནོད་པར་འགྱུར་ཞེས་པ་ནི་གནོད་པ་དང་རྗེས་སུ་འབྲེལ་པའོ། །

[Block 606]
ཡང་ན་དོན་མེད་པ་དང་མི་རིགས་པ་དང་རྗེས་སུ་འབྲེལ་པའོ། །

[Block 607]
སྦྱིན་པ་ལ་དགྱེས་ཆེས་བྱ༌[^312]བ་འདིས་ནི་མིག་སྦྱིན་པ་ལས་ཟློག་པར་བྱེད་པ་སྟེ། མིག་སྦྱིན་པ་མི་རིགས་པ་དང་། གནོད་པར་འདོད་པ་དེ་བསྒྲུབ་པར༌[^313]འདོད་ནས། བྲམ་ཟེ་འདི་ནི་གཅིག་པུའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་སྨོས་པ་ཡིན་ནོ། །

[Block 608]
གཅེས་པ་དང་། མི་གཅེས༌[^314]པ་བློས་བརྟགས་ཤིང་སྦྱིན་པ་དང་མི་སྦྱིན༌[^315]པར་བྱ་བ་སྟེ། གཅིག་པུ་དང་མང་པོ་ལ་གཅེས་པ་དང་མི་གཅེས་པ་བརྟགས༌[^316]པའི་རིགས་ཏེ། བདག་ཅག་ཐམས་ཅད་ཅེས་བྱ་བ་འདི་ནི་མང་པོ་ཉིད་དེ། བྱིས་པ་དང་། བར་མ་དང་། རྒན་པོ་དང་བཅས་པའི་བྲམ་ཟེ་དང་། རྒྱལ་རིགས་དང་རྗེའུ་རིགས་ལ་སོགས་པ་ཅིའི་ཕྱིར་དོར་ཞེས་པའོ། །

[Block 609]
ཐམས་ཅད་ལ་གནོད་པར་འགྱུར་བའི་ཕྱིར་འདི་ཉིད་ཀྱིས་ནི་རེ་ཞིག་མིག་བཏང་བ་རིགས་པ་མ་ཡིན་པར་བསྟན་ཏོ། །

[Block 610]
གནོད་པར་འགྱུར་བ་ནི།

[Block 611 [VERSE]]
སྐྱེ་དགུ་བདེ་བར་བསྐྱེད་པ་རྣམས། །
མྱ་ངན་ཞུགས་ཀྱིས༌[^317]མི་བསྲེགས༌[^318]གསོལ། །

[Block 612]
ཞེས་བྱ་བ་ཡིན་ཏེ། སྐྱེ་དགུ་བདེ་བས་རྒྱལ་པོ་བདེ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 613]
ད་ནི་སྤྱན་སྩལ༌[^319]མི་རིགས་སོ། །ཞེས་བྱ་བ་དེ་མི་རིགས་པར་སྒྲུབ་པ་སྟེ། སྤྱན་སྩལ་བར་མི་རུང་བའི་དམིགས་ཀྱིས་དབྱེ་བ་ནི་གཞན་ནི་སྩལ་བར་རིགས་ཏེ༌[^320]ཞེས་སྟོན་པ་ཡིན་ཏེ། གཞན་ཡང་གང་དག་ཡིན་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར། དཔལ་ཆེན་སྐྱེད་པར་འགྱུར་བའི་ཞེས་བྱ་བ་ལ་སོགས༌[^321]པའི་ཚིགས་བཅད་གཉིས་སྨོས་པ་ཡིན་ནོ། །

[Block 614]
དཔལ་ཆེན་བསྐྱེད་པའི་ནོར་ཞེས་བྱ་བ་ཉིད་ཀྱིས་ནི་འདིའི༌[^322]ནང་དུ་སྦྱིན་པའི་དངོས་པོ་ཐམས་ཅད་འདུས་པ་ཡིན་ཏེ། སྤྱད་པར་བྱ་བ་དང་། ཡིད་དགའ་བར་བྱེད་པ་དང་། བཀྲེས་པ་དང་། སྐོམ་པའི་སྡུག་བསྔལ་ཟློག་པར་བྱེད་པ་དང་། འཁྲིག་པའི་འདོད་པ་ཉེ་བར་སྤྱོད་པའི་བདེ་བ་དང་། ཡོ་བྱད་ནི་ནོར་ལ་སོགས་པ་ཡིན་པས་དེ་ལྟར་སྨོས་པ་ཡིན་ནོ། །

[Block 615]
རྩོད་པ་ཟློག༌[^323]པར་བྱེད་པ་ཡིན་པས་ནོར་ལ་སོགས་པ་འདིའི་ཐ་སྙད་དོ། །

[Block 616]
རིན་ཆེན་ཞེས་བྱ་བ་ནི་ཡིད་དགའ་བར་བྱེད་པས་སོ། །

[Block 617]
ཤིང་རྟ་དང་གླང་པོ་སྨོས་པས་ནི་ངལ་བ་ལས་གྱུར་པའི་སྡུག་བསྔལ་སེལ་བར་བྱེད་པའོ། །

[Block 618]
རྐང་གདུབ་འཁྲོལ་བའི་སྒྲ་རྣམས་གྲག༌[^324]པ་ཡི། །ཞེས་བྱ་བ་ནི་འཁྲིག་པའི་འདོད་པ་ཉེ་བར་སྤྱོད་པའི་ཡོ་བྱད་དོ། །

[Block 619]
ཁང་པ་དུས་རྣམས་ཀུན་ཏུ་བདེ་ལྡན་པ། །ཞེས་བྱ་བ་འདིས་ནི་རྩོད་པ་མེད་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 620]
སྤྱན་རྩལ་བ༌[^325]མི་རིགས་པ་དེ་དམིགས་ཀྱིས༌[^326]དབྱེ་བ་ནི་གཞན་གྱི་མིག་གིས་གཞན་ལ་ཇི་ལྟར་སྦྱར་དུ་རུང་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གཉིས་ཏེ། རྒྱུ་དེ་གཉིས་ཀས་སྤྱན་སྩལ་བ་དེ་མི་རིགས་ཏེ། ཉིད་ཀྱི་སྤྱན་སྩལ་ཀྱང་དེའི་མིག་སྐྱེ་བར་མི་འགྱུར་བའི་ཕྱིར་དང་། གལ་ཏེ་འབྱུང་བར་གྱུར་ན་ནི་ཁྱོད་ཀྱི་སྤྱན་མ་བྱིན་པར་ཡང་ཡོད་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 621]
གཞན་དག་གི་མིག་གིས་ཞེས་བྱ་བ༌[^327]འདིས་ནི་མིག་འབྱིན་པར་མི་རིགས་པའོ། །

[Block 622]
མིག་ཡོད་ཀྱང་ནོར་གྱི་ཕུན་སུམ་ཚོགས་པ་མེད་པ་དང་། གོང་དུ་བཤད་པའི༌[^328]ནོར་དང་ལྡན་པ་གང་གཅེས༌[^329]པ་ཡིན་ཏེ། མིག་གཅེས་པ༌[^330]ཡིན་ནམ། འོན་ཏེ་ནོར་དང་ལྡན་པས་གཅེས་པ་ཡིན་ཅེས་བསམས་ན་ནོར་ཉིད་གཙོ་བོ་ཡིན་ཏེ། མིག་དང་ལྡན་པ་ནོར་མེད་པར་ནི་ཉམས་པ་ཉིད་དུ་འགྱུར་ཏེ། མིག་ཡོད་ཀྱང་ནོར་གྱི་ཕུན་སུམ་ཚོགས་པ་མེད་པ་དང་། ནོར་དང་ལྡན་ཞིང་མིག་མེད་དེ་ལོང་བ་ནི་བླའི། ཕོངས་པ་ནི་མ་ཡིན་ཏེ། ཕོངས་ཤིང་མིག་དང་ལྡན་པར་གྱུར་ན་གཞན་གྱི་འབྱོར་པ་མཐོང་ན་ཡིད་གདུངས་པར་འགྱུར་རོ། །

[Block 623]
འབྱོར་པ་ཕུན་སུམ་ཚོགས་པ་ནི་ལོང་ན་ཡང་དབང་པོ་གཞན་གྱིས་ཉེ་བར་ལོངས་སྤྱོད་པའི་ཕྱིར་རོ། །

[Block 624]
དེ་བས་དཀོར་ལས་སྩལ་དུ་གསོལ། །ཞེས་བྱ་བ་ཡིན་ཏེ། ནོར་ཉིད་སྦྱིན་པར་བྱའི་སྤྱན་ནི་སྩལ་བར་བྱ་བ་མ་ཡིན་ཞེས་པའོ། །

[Block 625]
འདིར་ཡང་སྤྱན་སྩལ་བར་མི་རིགས་པ་དམིགས་ཀྱིས་འབྱེད་པས་གཞན་ཉིད་སྔར་བཤད་པ་སྟེ། ནོར་གཞན་དག་ནི་སྩལ་བར་རིགས་སོ། །

[Block 626]
གཅིག་གི་ཕྱིར་ནི་ཞེས་བྱ་བའི་དབང་དུ་བྱས་ནས་དཔལ་བསྐྱེད་པའི་ནོར་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གཉིས་ཀྱིས་བསྟན་པ་ཡིན་ནོ། །

[Block 627]
གཞན་ལ་ཇི་ལྟར་སྦྱར་དུ་རུང་། །ཞེས་བ་ནི་དབྱེ་བའོ། །

[Block 628]
ལྷ་གཞན་ཡང་ཞེས་བྱ་བས་ཅི་ཞིག་སྟོན་པར་འགྱུར་ཞེ་ན་ནོར་དང་མིག་གཉིས་འདོད་པ་དེ་ལ་ནོར་ཉིད་ཆེས་ཕན་པ་ཡིན་གྱི། མིག་སྦྱིན་པ་ནི་མ་ཡིན་ནོ་ཞེས་སྟོན་པ་ཡིན་ནོ། །

[Block 629]
གང་ཞིག་སྦྱིན་ཞེས་སྨྲས་ནས་ནི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་གྱིས་ནི་མིག༌[^331]སྦྱིན་པ་ཉིད་རིགས་པར༌[^332]ཕྱོགས་བླངས་ནས་སྨས་པ་སྟེ། བསམ་པ་ཉམས་པ་དང་། སྦྱོར་བ་ཉམས་པ་ལས་བརྩམས་ཏེ། གཉིས་ཀྱིས་ནི་བསམ་པ་ཉམས་པའོ། །

[Block 630]
གཅིག་གིས་ནི་སྦྱོར་བ་ཉམས་པ་སྟེ། རྒྱུ་གསུམ་གྱིས་སོ། །

[Block 631]
སྦྱིན་པའི་དངོས་པོ་ལ་ཆགས་པའམ། བདག་ཉིད་ལ་ཆགས་ཤིང་ཉམས་པས་འཇིགས་པའམ། ཕོངས་པ་རྣམས་ཀྱི་སྡུག་བསྔལ་ཡལ་བར་འདོར་བས་ནི་ཁས་བླངས་པའི་དངོས་པོ་སྦྱོར་བར་མི་འདོད་པ་ཡིན་ཏེ། སྦྱིན་པའི་དངོས་པོ་ལ་ཆགས་པ་དེ་ཉིད་མི་རིགས་པའི་དབང་དུ་བྱས་ནས། གང་གིས་སྦྱིན་ཞེས་སྨྲས་ན་ནི། ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་ཡིན་ཏེ། སྐྱེ་བོ་རྣམས་ནི་སྦྱིན་པའི་དངོས་པོ་ལ༌[^333]ཆགས་ཤིང་འདོད་པ་ཡིན་པས་སོ། །

[Block 632]
འདོད་པ་གང་ཞེ་ན་སྦྱིན་པ་དང་འགལ་བའི་སེམས་ཀྱིས་ཀུན་ཏུ་འཛིན་པ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 633]
བདག་ལ་ཆགས་ཤིང་ཉམས་པས་འཇིགས་པའི་དབང་དུ་བྱས་ནས་སྦྱིན་ནོ་ཞེས་ནི་ཁས་བླངས་ནས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་ཡིན་ཏེ། གང་ཞིག་ཡིད་ལ་གཞན་སེམས་པ། །ཞེས་བྱ་བ་ནི་མི་སྦྱིན་པར་ཡིད་ལ་སེམས་པའོ། །

[Block 634]
སེར་སྣས་མ་ངེས་བློ་ཅན་ཏེ། །ཞེས་བྱ་བ་ནི་སེར་སྣས་བདག་ཉིད་ལ་ཆགས་ཤིང་སྦྱིན་པ་དང་མི་མཐུན་པ་ཡོད་པས་སོ།[^334] །སེར་སྣས་མ་ངེས་པའི་བློ་གང་ཡིན་པ་དེ་ནི། སེར་སྣས་མ་ངེས་པའི་བློ་ཅན་ཏེའོ། །

[Block 635]
མ་ངེས་པར་གྱུར་པ་དེ་ནི་ཕྱིས་མི་སྦྱིན་པའི་སེམས་ཡིན་ནོ་ཞེས་རྗེས་སུ་ཤེས་པའོ།[^335] ། ཕོངས་པའི་སྐྱེ་བོ་ཡལ་བར་དོར་བའི་དབང་དུ་བྱས་ནས་སྦྱོར་བ། སྦྱིན་ནོ་ཞེས་ནི་ཁས་བླངས་ནས། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
