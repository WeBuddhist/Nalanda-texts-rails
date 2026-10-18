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
[Block 736]
བསྟན་བཅོས་ལ་འཇུག་པར་བྱ་སྟེ། གང་ཞིག་ལུས་ཀྱི༌[^533]དོན་གཞན་གོ་བར་བྱེད་ན་བརྫུན་དུ་སྨྲ་བར་འགྱུར་རམ་ཞེ་ན། འགྱུར་རོ། །

[Block 737]
དེ་ཉིད་ཀྱི་ཕྱིར། ལུས་ཀྱིས༌[^534]མི་བྱེད་ན་སྲོག་གཅོད་པའི་ཁ་ན་མ་ཐོ་བའི༌[^535]རེག་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན་ཡོད་དོ། །

[Block 738]
ངག་གིས༌[^536]བྱེད་པར་འགྱུར་ནའོ། །

[Block 739]
ངག་གིས་མི་བྱེད་ན་བརྫུན་གྱི༌[^537]ཁ་ན་མ་ཐོ་བས་རེག་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན་ཡོད་དོ། །

[Block 740]
[^538]ལུས་ཀྱིས་བྱེད་པར་འགྱུར་ནའོ། །

[Block 741]
ལུས་ཀྱིས་ཀྱང་མི་བྱེད། ངག་གིས་ཀྱང་མི་བྱེད་ན། ཁ་ན་མ་ཐོ་བ་གཉི་གས་རེག་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན། ཡོད་དེ། འདིར་དྲང་སྲོང་རྣམས་ཡིད་རབ་ཏུ་ཁྲོས་པ་དང་། གསོ་སྦྱོང་དཔེར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 742]
གཉི་གས༌[^539]ཡང་མི་བྱེད་ན་འདོད་པ་ན་སྤྱོད་པའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་རྣམ་པར་རིག་བྱེད་མེད་པ་ཅན་ཡང་མེད་པས་ཇི་ལྟར་ན་དེ་གཉིས་ཀྱིས་ལས་ཀྱི༌[^540]ལམ་དུ་འགྲུབ་སྟེ། འདི་ལ་འབད་པར་བྱའོ། །

[Block 743]
བརྫུན་དུ་སྨྲ་བ་རྫོགས་སོ།། །།

[Block 744 [HEADING]]
#### ཕྲ་མ། ^1-48-5-0

[Block 745 [VERSE]]
ཕྲ་མ་ཕ་རོལ་དབྱེ་བའི་ཕྱིར། །
ཉོན་མོངས་ཅན་གྱི་སེམས་ཀྱི་ཚིག །

[Block 746]
ཕ་རོལ་པོ་དག་དབྱེ་ཞིང་མི་མཛའ་བར་བྱ་བའི་ཕྱིར་སེམས་ཀྱི༌[^541]ཉོན་མོངས་པ་ཅན་གྱི་ཚིག་གང་ཡིན་པ་དེ་ནི་ཕྲ་མ་ཡིན་ཏེ། དོན་མངོན་པར་གོ་བ་དང་།

[Block 747]
མ་ནོར་བ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 748 [HEADING]]
#### ཚིག་རྩུབ་པོ། ^1-48-6-0

[Block 749]
ཚིག་རྩུབ་པོ་ནི་མི་སྙན་པ། །

[Block 750]
སེམས་ཉོན་མོངས་པ་ཅན་གྱི་ཚིག་དང་། དོན་མངོན་པར་གོ་བ་དང་། མ་ནོར་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། སེམས་ཉོན་མོངས་པ་ཅན་གྱིས་ཅིའི༌[^542]ཚིག་མི་སྙན་པ་ཕ་རོལ་པོ་ལ་སྨྲས་ཤིང་དོན་མངོན་པར་གོ་ལ་གང་ལ་སྨྲ་བར་འདོད་པ་དེ་ཉིད་ལ་སྨྲ་བ་གང་ཡིན་པ་དེ་ནི་ཚིག་རྩུབ་པོ་ཡིན་ནོ། །

[Block 751 [HEADING]]
#### ཚིག་ཀྱལ་པ། ^1-48-7-0

[Block 752]
ཉོན་མོངས་ཅན་ཀུན་ཀྱལ་པ་ཉིད། །ཚིག་ཅེས་བྱ་བའི་དབང་དུ་བྱས་པར་སྦྱར་ཏེ། ཉོན་མོངས་པ་ཅན་གྱི་ཚིག་ཐམས་ཅད་ནི་ཚིག་ཀྱལ་པ་ཡིན་ནོ། །

[Block 753]
དེ་ཉིད་ན་ནི༌[^543]ཀྱལ་པ་ཉིད་ཡིན་ཏེ། དེ་དང་ལྡན་པ་ནི་ཚིག་ཀྱལ་པ་ཅན་ཡིན་ནོ། །

[Block 754]
གཞན་ནི་དེ་ལས་གཞན་ཉོན་མོངས། །གཞན་དག་ན་རེ་ངག་གི་ལས་བརྫུན་དུ་སྨྲ་བ་ལ་སོགས་པ་དེ་དག་ལས་གཞན་པ་ཉོན་མོངས་པ་ཅན་གྱི་ཚིག་གང་ཡིན་པ་དེ་ནི་ཚིག་ཀྱལ་པ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། ཁ་གསག་གླུ་དང་ཟློས་གར་བཞིན། །བསྟན་བཅོས་ངན་བཞིན།[^544] དཔེར་ན་དགེ་སློང་ལོག་པས་འཚོ་བ་ཅན་ཁ་གསག་བྱེད་པ་དང་། ཆགས་པས་ཁ་ཅིག་གླུ་ལེན་པ་དང་། ཟློས་གར་མཁན་རྣམས་ཟློས་གར་གྱི་ཚེ་གཞན་དག་མགུ་བར་བྱ་བའི་ཕྱིར་འཁྱལ་པ་དང་། དེའི་ལྟ་བར་གྱུར་ནས་བསྟན་བཅོས་ངན་པ་དག་གདོན་པ༌[^545]དང་། དེ་བཞིན་དུ་སྨྲེ་སྔགས་འདོན་པ་དང་། འདུ་འཛིའི་གཏམ་ལ་སོགས་པ༌[^546]བརྫུན་དུ་སྨྲ་བ་ལ་སོགས་པ་ལས་གཞན་པ་ཉོན་མོངས་པ་ཅན་གྱི་ཚིག་གང་ཡིན་པ་དེ་ཡང་ཚིག་ཀྱལ་པ་ཡིན་ནོ། །

[Block 755]
ཇི་ལྟར་ན་འཁོར་ལོས་སྒྱུར་བའི་ཚེ་གླུ་ཡང་ཡོད་ལ་ཚིག་ཀྱལ་པ་ཡང་མ་ཡིན་ཞེ་ན། དེའི་ཚེ་ངེས་པར་འབྱུང་བ་དང་ལྡན་པའི་གླུ་དག་བླངས་ཀྱི་སྟེགས་སྔགས་དང་ལྡན་པ་དག་ནི་མ་ཡིན་ནོ། །

[Block 756]
གཞན་དག་ན་རེ་དེའི་ཚེ་ཡང་བག་མ་ལེན་པ་དང་། བག་མ༌[^547]གཏོང་བ་ལ་སོགས་པའི་མངོན་པར་བརྗོད་པ་ཡོད་པས་ཚིག་ཀྱལ་པ་ནི་ཡོད་མོད་ཀྱི་ལས་ཀྱི་ལམ་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 757 [HEADING]]
#### བརྣབ་སེམས། ^1-48-8-0

[Block 758]
བརྣབ་སེམས་ནི། ལོག་པས་གཞན་གྱི་ནོར་ལ་ཆགས། ། ཕ་རོལ་པོ་དག་གི་གང་ཡིན་པ་དེ་བདག་གི་ཡིན་པར་གྱུར་ཀྱང་ཅི་མ་རུང་སྙམ་ནས་གཞན་གྱི༌[^548]ནོར་དག་ལ་མཐུའམ་འཇབ་བུ་འང་རུང་ལོག་པར༌[^549]མི་རིགས་པས༌[^550]བདག་གིར༌[^551]བྱེད་འདོད་པ༌[^552]གང་ཡིན་པ་དེ་ནི་བརྣབ་སེམས་ཀྱི་ལས་ཀྱི་ལམ་ཡིན་ནོ། །

[Block 759]
གཞན་དག་ན་རེ་འདོད་པ་ན་སྤྱོད་པའི་སྲེད་པ་ཐམས་ཅད་བརྣབ་སེམས་ཡིན༌[^553]ཏེ། འདི་ལྟར་སྒྲིབ་པའི་སྐབས་སུ་འདོད་པ་ལ་འདུན་པའི་དབང་དུ་མཛད་ནས་མདོ་ལས་དེ་འཇིག་རྟེན་ན་བརྣབ་སེམས་སྤངས་ཏེ་ཞེས་བྱ་བ་དེ་ལ་སོགས་པ་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 760]
གཞན་དག་ན་རེ་འཁོར་ལོས་སྒྱུར་བ་རྣམས་དང་། བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་ལ་ཡང་བརྣབ་སེམས་ཀྱི་ལས་ཀྱི་ལམ་ཡོད་པར་འགྱུར་དུ་འོང་བས། གལ་ཏེ་ཐམས་ཅད་བརྣབ་སེམས་ཡིན་ན་ཡང་ཐམས་ཅད་ལས་ཀྱི་ལམ་ནི་མ་ཡིན་ཏེ། ཉེས་པར་སྤྱད་པ་ཆེ་ལོང་བསྡུས་པའི་ཕྱིར༌[^554]ཞེས་ཟེར་རོ། །

[Block 761 [HEADING]]
#### གནོད་སེམས། ^1-48-9-0

[Block 762]
གནོད་སེམས་སེམས་ཅན་ལ་སྡང་བ། །སེམས་ཅན་དག་ལ་ཞེ་སྡང་བ་ཕ་རོལ་ལ་གནོད་པའི་རྣམ་པར་ཞུགས་པ་ནི་གནོད་སེམས་ཡིན་ནོ། །

[Block 763 [HEADING]]
#### ལོག་པར་ལྟ་བ། ^1-48-10-0

[Block 764]
དགེ་དང་མི་དགེ་མེད་ལྟ་བ། །ལོག་པར་ལྟ་བ་ཡིན། ལས་དགེ་བ་དང་མི་དགེ་བ་མེད་དོ་ཞེས་ལྟ་བ་དེ་ནི་ལོག་པར་ལྟ་བ་ཡིན་ཏེ། འདི་ལྟ་སྟེ་སྦྱིན་པ་མེད་དོ། །

[Block 765]
མཆོད་སྦྱིན་མེད་དོ། །

[Block 766]
སྦྱིན་སྲེག་མེད་དོ། །

[Block 767]
ལེགས་པར་སྤྱད་པ༌[^555]མེད་དོ། །

[Block 768]
ཉེས་པར་སྤྱད་པ་མེད་དོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་ནས་འཇིག་རྟེན་ན་དགྲ་བཅོམ་པ་མེད་དོ་ཞེས་བྱ་བའི་བར་ལས་དང་འབྲས་བུ་དང་འཕགས་པ་ལ་སྐུར་པ་འདེབས་པ་ནི་རིལ༌[^556]གྱིས་ལོག་པར་ལྟ་བ་ཡིན་ནོ། །

[Block 769]
ཚིགས་སུ་བཅད་པར་ནི་དང་པོ་ཙམ་ཞིག་བསྟན་པར་ཟད་དོ། །

[Block 770]
ལས་ཀྱི་ལམ་བཅུ་པོ་དེ་དག་གི་མཚན་ཉིད་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 771 [HEADING]]
### ལས་ཀྱི་ལམ་ཞེས་བྱ་བའི་དོན། ^1-49-0

[Block 772]
ལས་ཀྱི་ལམ་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། འདི་ལ། གསུམ་མམ་བདུན་ནི་ལས་ཀྱང་ཡིན། །བརྣབ་སེམས་ལ་སོགས་པ་གསུམ་ནི་ལས་ཀྱི་ལམ་ཡིན་པས་ལས་ཀྱི་ལམ༌[^557]དག་ཡིན་ནོ། །

[Block 773]
དེ་དག་དང་མཚུངས་པར་ལྡན་པ་ཅན་གྱི་སེམས་པ་ནི་དེ་དག་གི་རྒྱུ་བས་རྒྱུ་སྟེ། དེ་དག་གི་དབང་གིས་དེ་བཞིན་དུ་མངོན་པར་འདུ་བྱེད་པའི་ཕྱིར་དེ་དག་གི་འགྲོས་ཀྱིས་འགྲོའོ། །

[Block 774]
སྲོག་གཅོད་པ་ལ་སོགས་པ་བདུན་ནི་ལུས་དང་ངག་གི་ལས་ཡིན་པའི་ཕྱིར་ལས་ཀྱང་ཡིན་ལ༌[^558]ལས་ཀྱི་ལམ་ཡིན་པས་ལས་ཀྱི་ལམ་ཡང་ཡིན་ཏེ། དེ་དག་ཀུན་ནས་སློང་བའི་སེམས་པ་ནི་དེ་དག་ལ་བརྟེན་ནས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 775]
དེ་ལྟར་ན་ལས་ཀྱི་ལམ་དང་། ལས་དང་ལས་ཀྱི་ལམ་ཡིན་པས་ན་ལས་ཀྱི་ལམ་སྟེ། མི་འདྲ་བ་རྣམས་ལ་ཡང་གཅིག་བསྡུས་པར༌[^559]འགྲུབ་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
