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
[Block 981 [VERSE]]
བདག་དང་གཞན་སྨྲས་དངོས་འདི་དག །
ཡང་དག་དོན་དུ་རང་བཞིན་མེད། །
གཅིག་དང་དུ་མར་བྲལ་བའི་ཕྱིར། །
རང་བཞིན་མེད་དེ་གཟུགས་བརྙན་བཞིན། །

[Block 982]
ཞེས་གསུངས་པ་དང་། སློབ་དཔོན་དཔལ་སྦས་ཀྱིས་ཀྱང་།

[Block 983 [VERSE]]
ཕྱི་དང་ནང་ན་གནས་འདི་ཀུན། །
ཡང་དག་དོན་དུ་རང་བཞིན་མེད། །
གཅིག་པ་ཉིད་དང་དུ་མ་དང་། །
བྲལ་བའི་ཕྱིར་ན་གཟུགས་བརྙན་བཞིན། །

[Block 984]
ཞེས་གསུངས་སོ། །

[Block 985]
དེ་དག༌[^534]གི་དོན་རྒྱས་པར་གཞུང་དེ་དག་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 986 [HEADING]]
### རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་གཏན་ཚིགས། ^8-4-0

[Block 987]
སྟོང་ཉིད་བདུན་ཅུའི་རིགས་པ་དང་། དབུ་མ་རྩ་བ་ལ༌[^535]སོགས་ལས་ཀྱང་།

[Block 988 [VERSE]]
དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ནི། །
སྟོང་པ་ཉིད་དུ་གྲུབ་བཤད་པ། །

[Block 989]
ཞེས་བྱ་བ་འདིས་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་གཏན་ཚིགས་བསྟན་ཏེ། འདིའི་དོན་ཡང་གཞུང་དེ་དག་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 990]
གྲུབ་བཤད་པ་ནི་སྔོན་གྱི་སློབ་དཔོན་ཆེན་པོ་རྣམས་ཀྱིས༌[^536]དངོས་པོ་ཐམས་ཅད་སྐྱེ་བ་མེད་པར་བསྒྲུབས་པ༌[^537]བསྟན། དེ་ལྟ་བུའི་གཏན་ཚིགས་ཆེན་པོ་བཞིས་དངོས་པོ་མ་ལུས་པ་སྐྱེ་བ་མེད་པ། རབ་ཏུ་མི་གནས་པ། རང་བཞིན་གྱིས༌[^538]མྱ་ངན་ལས་འདས་པ། གདོད་ནས་རྣམ་པར་དག་པ། རྩ་བ་མེད་པ། གཞི་མེད་པ། ཆོས་གང་ཡང་གྲུབ་པ་མེད་པར་སྔོན་གྱི་མཁས་པ་ཆེན་པོ༌[^539]དག་གིས་ལེགས་པར་བསྒྲུབས་ཟིན་ཏོ།། །།

[Block 991]
འཛམ་བུའི་གླིང་ན་མཁས་པ་དག་ནི་འདི་སྐད་དུ། འཕགས་པ་ཐོགས་མེད་ཀྱིས༌[^540]བསྟན་པའི་རྣམ་གྲངས་བཤད་པ། དེས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དོན་རྣམ་པར་རིག་པ་ཙམ་དུ་གསུངས་ཤིང་། ད་ལྟར་བླ་མ་སུ་ཝརྞྞ་དྭཱི་པ་དང་། བླ་མ་ཤཱན་ཏི་པ་ཡང་དེ་ལྟར་དགོངས་སོ། །

[Block 992]
སློབ་དཔོན་ཀླུ་སྒྲུབ་ཀྱིས་ནི་བསྟན་པའི་སྙིང་པོ་བཤད་དེ། དེས་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དོན་ཡོད་པ་དང་མེད་པ་ལས་འདས་པའི་དབུ་མ་ཆེན་པོའི་དོན་ཐུགས་སུ་ཆུད་ཅིང་། མཁས་པ་གཞན་གྱི་རྒྱུད་ལ་ཡང་དེ་ལྟར་གསུངས་སོ། །

[Block 993]
དེ་ལྟར་བླ་མ་བྱང་ཆུབ་བཟང་པོ་དང་། རྗེ་བཙུན་ཀུ་སུ་ལུ་པ་ཡང་དེ་ལྟར་དགོངས་སོ། །

[Block 994 [VERSE]]
འཕགས་པ་ཀླུ་སྒྲུབ་ཞལ་གྱི་བདུད་རྩི་དེས། །
ཨཱརྱ་དེ་བ་ཟླ་གྲགས་བྷ་བྱ་དང་། །
ཞི་བའི་ལྷ་དང་བྱང་ཆུབ་བཟང་པོའི་བར། །
ཚིམ་པར་གྱུར་པ་བདག་ལའང་ཅུང་ཞིག་འཐོར། །

[Block 995 [VERSE]]
དེ་ལྟར་གཏན་ཚིགས་ཆེན་པོ་བཞི་དག་གིས། །
ཆོས་རྣམས་ཐམས་ཅད་སྐྱེ་མེད་བསྒྲུབ་བྱས་ཏེ། །
སྔོན་གྱི་སློབ་དཔོན་རྣམས་ཀྱི་རྗེས་འབྲངས༌[^541]ནས། །
དབུ་མ་ཆེན་པོའི་གྲུབ་མཐར་གནས་པར་བྱ། །

[Block 996]
ཡང་ན་འདི་ལྟ་བུ་ཡིན་ཏེ།

[Block 997 [VERSE]]
དེང་སང༌[^542]སེམས་ཅན་དུས་དང་ཉོན་མོངས་དང་། །
ལྟ་བ་ཚེ་ཡི་སྙིགས་མར་གྱུར་པ་སྟེ། །
གཞུང་རྣམས་མཉན་པར་དགོས་པ་མེད་པས་ན། །
སྙིང་པོ་དོན་གྱི་རྣལ་འབྱོར་བསྒོམ་པར༌[^543]བྱ། །

[Block 998 [VERSE]]
དིང་སང་དུས་སུ་གཟིངས་དང་འདྲ་བ་ཡི། །
གཞུང་རྣམས་རྒྱ་ཆེན་མཉན་པའི་དུས་མེད་པས། །
ཡིད་འཁྲུགས༌[^544]བྱེད་པ་ཐམས་ཅད་སྤངས་བྱས་ལ། །
དམ་པའི་ཉེར་བསྟན་འབའ་ཞིག་བསྒོམ་པར་བྱ། །

[Block 999 [VERSE]]
ཚེ་ནི་ཡུན་ཐུང་ཤེས་བྱའི་རྣམ་པ་མང་། །
ཚེ་ཡི་ཚད་ཀྱང་འདི་ཙམ་མི་ཤེས་པས། །
ངང་པས་ཆུ་ལས༌[^545]འོ་མ་ལེན་པ་ལྟར། །
འདོད་པའི་དངོས་པོ་དང་ལས༌[^546]བླང་བར་བྱ། །

[Block 1000]
རྩ་བ་ཉིད་བཤད་པར་བྱ་སྟེ། དབུ་མའི་རྩ་བ་ཞེས་བྱ་བ་ནི་དབུ་མའི་རྩ་བ་ཤེས་རབ་པོ། །སོགས་ཞེས་པས་ནི་ག་ལས༌[^547]འཇིགས་མེད་དང་། རིགས་པ་དྲུག་ཅུ་པ་དང་། རྩོད་པ་བཟློག་པ༌[^548]དང་། སྟོང་པ་ཉིད་བདུན་ཅུ་པ་དང་། རིན་པོ་ཆེའི་ཕྲེང་བ་དང་། ཐེག་པ་ཆེན་པོ་ཉི་ཤུ་པ་དང་། ཚིག་བརྒྱ་པ་དང་། སཱ་ལུ་ལྗང་པའི་འགྲེལ་པ་ལ་སོགས་པའོ། །

[Block 1001]
ཡང་ན་སོགས་ཞེས་པ་ནི་སློབ་དཔོན་འཕགས་པའི་དངོས་ཀྱི་སློབ་མ་རྗེ་བཙུན་ཨཱརྱ་དེ་བ་དང་། སློབ་དཔོན་ཟླ་གྲགས་དང་། སློབ་དཔོན་བྷ་བྱ་སྣང་བྲལ་དང་། སློབ་དཔོན་ཞི་བའི་ལྷ་ལ་སོགས་པས་མཛད་པའི་བསྟན་བཅོས་ཏེ། དེ་ཡང་རྗེ་བཙུན་ཨཱརྱ་དེ་བས་ནི་དབུ་མ་རྣམ་པར་འཐག་པ་ཆེན་པོ་དང་། ལག་པའི་ཚད་དང་། སོར་མོ་ལྟ་བུའི་བཤད་པ་དང་། ཡེ་ཤེས་སྙིང་པོ་ཀུན་ལས་བཏུས་པ་ལ་སོགས་པ་མཛད་དོ། །

[Block 1002]
སློབ་དཔོན་ཟླ་གྲགས་ཀྱིས། དབུ་མ་ལ་འཇུག་པ་དང་། རིགས་པ་དྲུག་ཅུ་པའི་འགྲེལ་པ་དང་། དབུ་མ་ཕུང་པོ་ལྔ་པ་དང་། ཚིག་དོན་གསལ་བ་ལ་སོགས་པ་མཛད་དོ། །

[Block 1003]
སློབ་དཔོན་བྷ་བྱ་སྣང་བྲལ་གྱིས༌[^549]དབུ་མ་རྟོག་གེ་འབར་བ་དང་། ཤེས་རབ་སྒྲོན་མ༌[^550]ལ་སོགས་པ་མཛད་དོ། །

[Block 1004]
དེ་ལ་དབུ་མའི་རྩ་བ་ཤེས་རབ་ལ་འགྲེལ་པ་བརྒྱད་ཡོད་དེ། སློབ་དཔོན་ཉིད་ཀྱིས་མཛད་པའི་ག་ལས༌[^551]འཇིགས་མེད་དང་། སློབ་དཔོན་ཟླ་གྲགས་ཀྱིས་མཛད་པའི་ཚིག་དོན་གསལ་བ་དང་། སློབ་དཔོན་བྷ་བྱ་སྣང་བྲལ་གྱིས་མཛད་པའི་ཤེས་རབ་སྒྲོན་མ་དང་། གནས་བརྟན་བུདྡྷ་པཱ་ལི་ཏས་མཛད་པའི་བུདྡྷ་པཱ་ལི་ཏ་དང་། སློབ་དཔོན་བློ་བརྟན་གྱིས་མཛད་པ་དང་། སློབ་དཔོན་གུ་ཎ་མ་ཏི་དང་། སློབ་དཔོན་གུ་ཎ་ཤྲཱི་དང་། ཨཱ་ཙཱརྱ་གུ་ཎ་ད་ཏས་མཛད་པ་རྣམས་སོ། །

[Block 1005]
དེ་ལ་ཤེས་རབ་སྒྲོན་མ་ལ་ཊཱི་ཀ་ཆེན་པོ་གཉིས་ཡོད་དེ། ཨཱ་ཙཱརྱ་སྤྱན་རས་གཟིགས་བརྟུལ༌[^552]ཞུགས་ཀྱིས་མཛད་པ་དང་། ཨཱ་ཙཱརྱ་དེ་བ་ཤརྨས་མཛད་པའི་དབུ་མ་དཀར་པོ་འཆར་བའོ། །

[Block 1006]
གཞན་ཡང་འཛམ་བུའི་གླིང་ན་སློབ་དཔོན་འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་དགོངས་པ་འཆད་པ་མཁས་པ་ཆེན་པོ་བདག་དང་གཞན་གྱི༌[^553]གྲུབ་པའི་མཐའ་རྒྱ་མཚོ་ལྟ་བུ་ཐུགས་སུ་ཆུད་པ་རྣམས་ཀྱིས༌[^554]མཛད་པའི་གཞུང་གི་གཏན་ཚིགས་དག་གིས།

[Block 1007 [VERSE]]
དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་གྱི། །
སྟོང་པ་ཉིད་ནི་གྲུབ་བཤད་པ། །

[Block 1008]
ཞེས་ཏེ་དེ་དང་དེར་ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་དུ་རྒྱས་པར་བསྒྲུབས་ཟིན་ལ། གལ་ཏེ་བདག་གིས༌[^555]གཏན་ཚིགས་ཆེན་པོ་བཞིས་གཞན་དག་གི་ལོག་པར་རྟོགས་པ་བསལ་བར༌[^556]གྱུར་ན་ནི་གཞུང་ཤིན་ཏུ་མངས་པར༌[^557]འགྱུར་བས་ན། དེ་ཕྱིར་བདག་གིས་འདིར་ཉུང་ངུན༌[^558]དུ་བྱས་ཤིང་མ་སྤྲོས་པ་ཡིན་ནོ། །

[Block 1009]
འདིར་བདག་ཅག་དབུ་མ་ཆེན་པོའི་གྲུབ་པའི་མཐའ་ནི་འདི་ལྟར་ཡིན་ནོ་ཞེས་སྨོས་པ༌[^559]ཙམ་དུ་ཟད་ཀྱི། གྲུབ་པའི་མཐའ་རྒྱས་པར་ནི་མ་བྲིས་ཏེ། རྣལ་འབྱོར་པ་ཉམས་སུ་ལེན་འདོད་པ་དག་ལ་ཉུང་ངུན༌[^560]དུ་བསྡུས་ནས་བསྟན་པ་ཡིན་པས། བསྒོམ་པའི་དོན་དུ་རབ་ཏུ་བཤད། །ཅེས་བྱ་བ་དེ་ཡིན་ནོ། །

[Block 1010]
འདིར་དོན་དམ་པའི་བྱང་ཆུབ་ཀྱི་སེམས་བསྒོམ་པས། ཉམས་སུ་བླང་བའི་ཐབས་ནི་བདག་གིས་མ་བྲིས། བླ་མ་ཡོངས་སུ་མཉེས་པར་བྱས་ནས་བླ་མ་ལ༌[^561]ཞུ་བར་བྱའོ། །

[Block 1011]
དེ་བས་ཆོས་རྣམས་མ་ལུས་པ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། དེ་དག་ནི་དཀྱུས་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 1012]
གང་གི་རང་བཞིན་མ་མཐོང༌[^562]ཞེས་པ་ནི་ཆོས་གང་ཡང་མཐོང་བ་མེད་པ༌[^563]ཉིད་དེ་ཁོ་ན་ཉིད་མཆོག་མཐོང་བའོ་ཞེས་མདོ་སྡེ་དུ་མར་གསུངས་པ་ཡིན་ནོ། །

[Block 1013]
འདིའི་དོན་ལ་སློབ་དཔོན་ཨཱརྱ་དེ་བས་མཛད་པའི་དབུ་མ་འཁྲུལ་པ་འཇོམས་པར་བལྟ་བར་བྱའོ། །

[Block 1014]
རྟོག་གེ་འབར་བ་དང་། དབུ་མ་ལ་འཇུག་པ་དང་། སྤྱན་རས་གཟིགས་བརྟུལ་ཞུགས་དག་ཏུ་ཡང་བལྟ་བར་བྱའོ། །

[Block 1015]
ཆོས་གཞན་ཐམས་ཅད་ལྟ་ཡོངས་སུ་གྲུབ་པ་མེད་ན་རང་གི་སེམས་འདི་ཡོད་དམ་ཞེ་ན། ཤེས་རབ་དེ་ཉིད་རིགས༌[^564]བཤད་པ། །ཞེས་སྨྲས་ཏེ། སོ་སོར་རྟོག་པའི༌[^565]ཤེས་རབ་དེ་ཉིད་ག་ལ་ཡོད་དེ་མེད་དོ། །ཇི་ལྟར་མེད་པ་ཡིན་ཞེ་ན། རིགས་བཤད་པ་ཞེས་ཏེ། དེ་ཉིད་ཀྱང་གཏན་ཚིགས༌[^566]ཆེན་པོ་བཞིས་བཤད་ཅིང་གཞིགས༌[^567]ན་གྲུབ་པར་མི་འགྱུར་ཏེ། དོན་འདི་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་འཕགས་པ་བདེན་པ་གཉིས་བསྟན་པའི་མདོ་ལས་གསལ་བར་གསུངས་ཏེ། ཇི་སྐད་དུ་དོན་དམ་པར་ནི་ཆོས་ཐམས་ཅད་ཀྱི་ཤེས་རབ་རྣམ་པར་དཔྱད་ནས་བཙལ་ཡང་ཤིན་ཏུ་མེད་ཅིང་མི་དམིགས་པའོ། །ཤེས་རབ་དེ་ཡང་དོན་དམ་པར༌[^568]ནི་ཤིན་ཏུ་མེད་ཅིང་མི་དམིགས་པས་ན་ཀུན་རྫོབ་ཏུ་ཤེས་རབ་ཅན་ཞེས་བྱ་བ་སྟེ། ཤེས་རབ་དེ་ཡང་དོན་དམ་པར་ན་ཤིན་ཏུ་མ་སྐྱེས་ཤིང་མེད་པ་ཡིན་ནོ། །

[Block 1016]
འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ༌[^569]ནས་ཀྱང་དོན་འདི་ལ་དགོངས་ནས།

[Block 1017 [VERSE]]
སེམས་ནི་སངས་རྒྱས་ཐམས་ཅད་ཀྱིས། །
མ་གཟིགས་གཟིགས་པ་མ་ཡིན་ཏེ། །
རང་བཞིན་མེད་པའི་ངོ་བོ་ལ། །
ཇི་ལྟ་བུ་ཞིག་གཟིགས་པར་འགྱུར། །

[Block 1018]
ཞེས་གསུངས་སོ། །

[Block 1019]
སློབ་དཔོན་འཕགས་པ་ལྷའི་ཞལ་ནས་ཀྱང་།

[Block 1020 [VERSE]]
རྣམ་ཤེས་དེ་ཡང་དོན་དམ་པར། །
དེ་ནི་མཁས་རྣམས་མི་བཞེད་དེ། །
གཅིག་དང་དུ་མ་བྲལ་བའི་ཕྱིར། །
ནམ་མཁའི་པདྨ་ཉིད་དང་མཚུངས། །
--- END BLOCKS ---
