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
[Block 526]
རྟག་ཏུ་སྦྱོར་བས་ནི་བསོད་ནམས་ཀྱི་ལས་རྒྱུ་མཐུན་པའི་འབྲས་བུ་སྦྱོར་བ་ཡིན་ཏེ། རྟག་པར་བྱེད་པའི་བག་ཆགས་ཀྱིས་ཕྱིས་ཀྱང་བསོད་ནམས་ཀྱི་བྱ་བ་མངོན་པར་བསྒྲུབ་པ༌[^239]ཡིན་པའི་ཕྱིར་རོ། །

[Block 527]
གུས་པར་བྱ་བའི་སྦྱོར་བས་ནི་བསོད་ནམས་ཀྱི་ལས་རྒྱ་ཆེར་སོགས་ཤིང་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་སྦྱིན་པའི་ངེས་པར་འབྱུང་བར་འགྱུར་རོ། །

[Block 528]
དེ་ཡང་བསོད་ནམས་ཀྱི་ལས་གོམས་ཤིང་འདྲིས་པར་བྱས་པ་སྟེ། དཔག་ཏུ་མེད་པའི་དུས་ནས་གོམས་པར་བྱས་པས༌[^240]སོ། །

[Block 529]
བསོད་ནམས་ཞེས་སྨོས་པས༌[^241]ནི་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཟུང་ངོ་། །དེ་བས་ན་དེ་ཉིད་ཀྱིས༌[^242]རྒྱལ་པོ་ཉིད་དུ་གྱུར་པ་ཡིན་ཏེ། བསོད་ནམས་ཀྱི་འབྲས་བུའི་སྟོབས་ཀྱིས་སོ། །

[Block 530]
རྒྱལ་པོ་དག༌[^243]གི་བུ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་རང་གི་སྐྱེ་བོ་བཞིན་དུ་སྐྱེ་དགུ་སྐྱོང་བར་གྱུར་པའོ། །

[Block 531]
ཡོན་ཏན་ཅི་དང་ལྡན་པས་ཡོངས་སུ་སྐྱོང་ཞེ་ན། དེ་ཉིད་སྨྲས་པ། བྱིས་པ་ནས་རྒན་པོ་ལ་བསྙེན་བཀུར་བྱེད་པ་ཞེས་བྱ་བའི་ཡོན་ཏན་དང་ལྡན་པ་ཉིད་ཀྱིས་སོ། །

[Block 532]
གང་དག་སྐྱོང་བར་གྱུར་ཞེ་ན། རང་གི་ཚོགས་དང་གཞན་གྱི་ཚོགས་གཉིས་ཏེ། རང་གི་ཚོགས་ཀྱི་སྐྱེ་བོ་སྐྱོང་བར་བྱེད་པ་ནི་རྒན་པ་ལ་སོགས་པ་ལ་བསྙེན་བཀུར་བྱ་བ་ལ་དགའ་བ་དང་། རྗེ་བློན་བྱམས་པ་དང་། ཡིད་གཞུངས་པ་སྟེ། འདིས་ནི་རིགས་པ༌[^244]རྟོགས་ཤིང་བློ་དྲི་མ་མེད་པར་གྱུར་པའོ། །

[Block 533]
གཞན་གྱི་ཚོགས་ཀྱི་སྐྱེ་བོ་སྐྱོང་བར༌[^245]བྱེད་པ་ནི་ནུས་པ་གསུམ་དང་ལྡན་པ་དང་། སྐལ་བ་ཕུན་སུམ་ཚོགས་པ་དང་།[^246] དེས་ན་དེ་ཉིད་ཀྱི་ཚིག་གིས་ནི་ལུགས་ཀྱི་བསྟན་བཅོས༌[^247]དང་གཉིས་སུ་དབྱེར་མེད༌[^248]པ་ཡིན་ནོ། །

[Block 534]
ཡང་ན་འཁོར་གསུམ་དང་རྗེས་སུ་མཐུན་པའི་ཡོན་ཏན་གྱི་ཚོགས་ཞེས་བྱ་བ་དེ་བསྟན་པའི་ཕྱིར་རྒན་པ་ལ་བསྙེན་བཀུར་བྱེད་པ་ལ་སོགས་པའི་ཡོན་ཏན་འདི་དག་བསྟན་ཏེ། ཆོས་ཀྱི་ཡོན་ཏན་དང་ནུས་པ་གསུམ་གྱི་ཡོན་ཏན་དང་། དོན་གྱི་ཡོན་ཏན་དང་། སྐལ་བ་ཕུན་སུམ་ཚོགས་པའི་ཡོན་ཏན་དང་། དད་པའི་ཡོན་ཏན་ནོ། །

[Block 535]
ཕན་ཚུན༌[^249]འགྲན་པ་བཞིན་དུ་གནས་པར་གྱུར་ཅེས་བྱ་བ་འདིས་ནི་ཇི་ལྟར་ཡོད་པའི་ཡོན་ཏན་དང་ལྡན་པ་དེ་དག་ཀྱང་ལྷན་ཅིག་ཏུ་གནས་པར་གྱུར་པ་ཡིན་པར་བསྟན་ཏོ། །

[Block 536]
དངོས་པོ་ཐམས་ཅད་ནི་དངོས་པོ་ཇི་སྲིད་པས་མ༌[^250]ལུས་པའི་ཡོན་ཏན་ཡོད་པར་གྱུར་པ་སྟེ། ཆོས་དང་དོན་དང་འདོད་པ་ཕན་ཚུན་འགལ་བ་ཡིན་ཡང་དེའི་ཡོན་ཏན་འགལ་ཞིང་འཁྲུག་པས༌[^251]གཙེས་པ༌[^252]མེད་པར༌[^253]གྱུར། ཞེས་པའི་དོན་ཏོ། །

[Block 537]
མ་དུལ་འཕྱར་བ་ཞེས་བྱ་བའི་ཚིགས༌[^254]བཅད་འདིས་ནི་ཞེ་སྡང་དང་། གཏི་མུག་དང་། འདོད་ཆགས་ཀྱི་ཉེས་པས་མ་རུངས་པར་བྱས་པས་མ་དུལ་བ་ལ་སོགས་པའོ། །

[Block 538]
གསུམ་དུ་གྱུར་པའི་ཉེས་པས་གསུམ་པ༌[^255]མེད་པ་སྟེ་ཉེས་པ་དེ་གསུམ་གྱི་གཉེན་པོར་གྱུར་པ་བྱམས་པ་དང་། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་དང་། མི་སྡུག་པ་བསྒོམ་པ༌[^256]དང་ལྡན་པ་སྟེ། དཔལ་དེ་དེ་ལ་མིང་ནི་དོན་བཞིན་དུ་གྱུར་ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་མཚན་ཉིད་དང་མཚན་དུ་གྱུར་པའོ། །

[Block 539]
རང་བཞིན་རྒྱ་ཆེ་ཞེས་བྱ་བ་འདིའི་ལུས་ནི་བསམ་པ་དང་། སྦྱིན་པའི་དངོས་པོ་དང་། སློང་བའི་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 540]
རང་བཞིན་རྒྱ་ཆེ་བ་དང་། སྙིང་རྗེའི་ཡོན་ཏན་ཞེས་བྱ་བ་འདིས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 541]
རྒྱ་ཆེ་བས་ནི་རང་གི་བདེ་བ་ལ་མི་ཆགས་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 542]
སྙིང་རྗེའི་ཡོན་ཏན་གྱིས་ནི་གཞན་གྱི་སྡུག་བསྔལ་སེལ་བར་མངོན་པར་འདོད་པ་ཡིན་ནོ། །

[Block 543]
ཡང་ན་བདག་གི་ལོངས་སྤྱོད་ལ་མི་ལྟོས་པ༌[^257]དང་། སེམས་ཅན་ལ་ལྟོས་པ༌[^258]དང་གཉིས་སྟོན་པ༌[^259]ཡིན་ནོ། །

[Block 544]
ཡང་ན་འབྲས་བུ་ལ་མི་ལྟོས་པ༌[^260]དང་། སེམས་ཅན་ལ་ལྟོས་པ༌[^261]ཡིན་པར་བསྟན་ཏོ། །

[Block 545]
སྦྱིན་པའི་དངོས་པོ་ནི་ནོར་གྱི་རྒྱལ་པོས་མི་ལེན་ཅིང་། སེམས་ཅན་གྱི་སྡུག་བསྔལ་སེལ་བར་འདོད་པ་ཡིན་པས། ལོངས་སྤྱོད་སེམས་ཅན་རྣམས་ལ་སྦྱིན་པའི་དངོས་པོ་སྒྲུབ་པ་ཡིན་ནོ། །

[Block 546]
ནོར་ལ་དབང་ཡོད་ཕྱིར་ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 547]
འདོད་པའི་དོན་གྲུབ་ཅེས་བྱ་བ་སྨོས༌[^262]པ་ནི་སྦྱིན་པའི་དངོས་པོ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ཏེ། ཇི་ལྟ་བུ་འདོད་པ་དང་། ཇི་སྙེད་འདོད་པ་དང་། གང་འདོད་པ་དེ་དག་ཡང་དག་པར་སྒྲུབ་པའོ། །

[Block 548]
འདོད་པའི་དོན་གྲུབ་པས་ཕོངས་པ་དག་ངོ་ཟུམ་མི་གནག་བཞིན་བཟངས་མཐོང་བས་དགའ་བ་སྟེ། དེ་ལྟར་སློང་མོ་པ་རྣམས༌[^263]ཕུན་སུམ་ཚོགས་པའོ། །

[Block 549]
དེའི་ཕུན་སུམ་ཚོགས་པ་གང་ཞེ་ན། སྦྱིན་པའི་དངོས་པོ་རྣམ་པ་ཐམས་ཅད་བསླངས་པ་སྟེ། འདོད་པ་ཞེས་སྨོས་པས་ཐོབ་པ་ཡིན་ཏེ། དེས་དུས་ཕྱི་ཞིག་ན་མིང་དང་གཟུགས་ཀྱི་ལུས་དགའ་བ་དང་མཛེས་པར་བྱེད་དོ། །

[Block 550]
སྦྱིན་པ་ལ་དགའ་བས་ཞེས་བྱ་བས༌[^264]ནི་སྔར་སྨོས་པ་བཞིན་དུ་རྒྱུ་མཐུན་པའི་འབྲས་བུ་སྟོན་པ་ཡིན་ཏེ། རྒྱུ་མཐུན་པ་ནི༌[^265]རྒྱུ་དང་འདྲ་བ་སྟེ་དེའི་ཚིག་གིས་སྔོན་གྱི་སྦྱིན་པ་བྱས་པས་སྦྱིན་པ་ལ་མངོན་པར་དགའ་བ་སྐྱེ་བར་འགྱུར༌[^266]ཏེ། རྒྱུ་མཐུན་པའི་འབྲས་བུ་སྦྱིན་པ་ལ་དགའ་བ་ཉིད་དོ། །

[Block 551]
ཡོ་བྱད་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ལ། ཡོ་བྱད་ནི་ནོར་དང་འབྲུ་ཞེས་སྨོས་པ་སྟེ། ཉེ་བར་སྤྱད་པ་དང་། ལོངས་སྤྱད་པའི་བྱེ་བྲག་གིས་གསུམ་གྱི་ནང་དུ་འདུས་པ་ཡིན་ནོ། །

[Block 552]
གང་དག་མ་སྨོས་པའི་སྦྱིན་པའི་དངོས་པོ་དེ་ཡང་འདིའི་ནང་དུ་ཆུད་པ་ཡིན་ཏེ། དེ་དག་ཀྱང་དེའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 553]
བདག་གི་བདག་ཉིད་ཆེ་བ་དང་རྗེས་སུ་མཐུན་པས་ཞེས་བྱ་བས་ནི་སྦྱིན་པའི་དངོས་པོ་མང་དུ་ཡོད་པ་བསྟན་ཏོ། །

[Block 554]
རེ་བ་ཇི་ལྟ་བ་བཞིན་ཞེས་བྱ་བས་ནི་གང་དང་གང་འདོད་པ་དེ་དེ་རེ་བ་ཇི་ལྟ་བ་བཞིན་དུའོ། །

[Block 555]
འདིས་ནི་དངོས་པོ་སྣ་ཚོགས་སྦྱིན་པར་བསྟན་པའོ། །

[Block 556]
གུས་པ་དང་བཅས་པར་ཞེས་བྱ་བ་ནི་བསྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པར་བསྟན་ཏོ། །

[Block 557]
དུས་བཞིན་དུ་འབྱོར་པས་ཡིད་དུ་འོང་བ་ནི༌[^267]དུས་གང་གི་ཚེ་གང་འདོད་པ་བཞིན་དུ་སྟེ། རྫོགས་ལྡན་གྱི་སྤྲིན་དང་འདྲ་བར་བདག་གི་བདག་ཉིད་ཆེ་བ་དང་རྗེས་སུ་མཐུན་པར་རེ་བ་ཇི་ལྟ་བར་དུས་བཞིན་དུ་འབྱོར་པ་སྒྲུབ་པའི་ཆོས་དང་མཐུན་པ་ཡིན་ནོ། །

[Block 558]
འདིས་ནི་རེ་བ་ཇི་ལྟ་བ་བཞིན་དུ་ཞེས་བྱ་བ་འདིའི་ཁྱད་པར་བསྟན་པ་སྟེ། ཟས་འདོད་པ་ལ་སོགས་པ་སྨོས་པས་ནི་གང་དང་གང་འདོད་པར་གྱུར་པ༌[^268]དེ་དང་དེ་སྒྲུབ་པ་ཡིན་ནོ། །

[Block 559]
ཡང་ན་ཡོ་བྱད་ཐམས་ཅད་དེ། [^269]ནོར་དང་འབྲུ་ལ་སོགས་པ་གང་གོང་དུ་བསྟན་པ་དེས་ཟས་འདོད་པ་རྣམས་ལ་ནི་ཟས། བཏུང་བ་འདོད་པ་རྣམས་ལ་ནི་བཏུང་བ་སྟེ། གང་གོང་དུ་བཤད་པ་དེ་སྦྱིན་པའོ། །

[Block 560]
མལ་ཆ་དང་། སྟན་དང་། གོས་དང་། བཟའ་བ་དང་། བྱུག་སྤོས་དང་། ཕྲེང་བ་དང་། དངུལ་ལ་སོགས་པའི་ནོར་སྒྲུབ་པས་སྙིང་དགའ་བར་བྱེད་དེ། བདག་གི་བདག་ཉིད་ཆེན་པོ་དང་རྗེས་སུ་མཐུན་པས་སོ། །

[Block 561]
སྦྱིན་པ་དེས་དགའ་བར་འགྱུར༌[^270]ཏེ་ཞེས་བྱ་བ་ནི་རེ་བ་ཇི་ལྟ་བ་བཞིན་དུ་བསྒྲུབ་པ༌[^271]ལ་སོགས་པ་གསུམ་གྱིས་སོ། །

[Block 562]
ཕྱོགས་ཐ་དད་པའི་ཡུལ་ན་གནས་པ་དེ་ནི་ཕྱོགས་ཐ་དད་པའི་ཡུལ་ན་གནས་པའོ།[^272] །ཡང་ན་ཕྱོགས་ཐ་དད་པའི་གནས་པས་མཚོན་པའི་ཚུལ་གང་ལ་ཡོད་པ་དེ་དག་གོ། །

[Block 563]
ཕྱོགས་ཐ་དད་པ་ཞེས་སྨོས་པས་ནི་ཐག་རིང་པོ་ནས་འོང་བར་སྟོན་པ་མངོན་པར་མཚོན་པའོ། །

[Block 564]
ཡུལ་ན་གནས་པ་ཞེས་སྨོས་པས་ནི་ཡུལ་ན་གནས་པ་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏོ། །

[Block 565]
གཞན་དག་ན་རེ་རེ་བ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་མེད་དམ། ཅིའི་ཕྱིར་ཐག་རིང་པོ་ནས་ལྷགས་ཤིང་འོངས་ཤེ་ན། དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། མི་ཡུལ་ཀུན་ཏུ༌[^273]ཡིད་ཀྱིས༌[^274]བརྟགས་ན་ཡང་། །ཞེས་བྱ་བའི་ཚིགས༌[^275]བཅད་འདི་སྨོས་སོ། །
--- END BLOCKS ---
