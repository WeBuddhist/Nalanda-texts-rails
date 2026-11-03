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
[Block 911]
ཐེ་ཙོམ་གྱི་དོན་ནི་ཐེག་པ་རྣམ་གསུམ་གྱིས༌[^906]རྣམ་པར་གྲོལ་བ་སོ་སོའི་བྱེ་བྲག་དང་། ཁྱད་པར་ཡོད་པ་ཡང་བསྟན།

[Block 912 [VERSE]]
ཐེག་པ་རྣམ་གསུམ་རྣམ་པར་གྲོལ་གཅིག་སྟེ། །
རྣམ་པར་གྲོལ་བའི་ཁྲི་གཅིག་ལ་བཞུགས་སོ། །

[Block 913]
ཞེས་ཀྱང་བསྟན་པ་དེ་ཉིད་རྒྱུ་ལ་ཐེ་ཙོམ་དུ་གྱུར་ཏོ། །

[Block 914]
དེ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡེ་ཤེས་ཀྱི་མཚན་ཉིད་དང་། ཆོས་ཀྱི་སྐུ་གཉིས་སུ་མེད་པ་ལས་དགོངས་པ་དང་། མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ལས་རྣམ་པ་གསུམ་བསྟན་པ་བཞིན་ཅི་རིགས་པར༌[^907]ཆུད་པར་བྱའོ། །

[Block 915]
ཅིའི་རྒྱུ་ཞེས་པ་ནི་དོན་ཅི་ལས་གླེངས་པའོ། །

[Block 916]
ཅིའི་ཕྱིར་ཞེས་པ་ནི་དངོས་པོའོ། །

[Block 917]
དངོས་པོ༌[^908]གང་ལས་དྲིས་ཞེས་པའི་དོན་ཏོ། །

[Block 918 [HEADING]]
##### ཚིགས་སུ་བཅད་པས་བསྡུས་ཏེ་གསོལ་བ། ^4-2-5-2-0

[Block 919]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་ཞེས་པ་ནས། དེ་དག་ཚད་མེད་ངས་ཐོབ་དང་། །ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པ་བཅུ་གཅིག་ལ་རྣམ་པ་བཞིར་དབྱེ་སྟེ།

[Block 920]
དང་པོ་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་བཞིས་ནི་བཅོམ་ལྡན་འདས་ལ་ཐབས་མཁས་ཤིང་ཤིན་ཏུ་ཟབ་པའི་སྒོ་ནས་བསྟོད་པ༌[^909]དང་། ཡང་ཚིགས་སུ་བཅད་པ་གསུམ་གྱིས་ནི༌[^910]འཁོར་བཞི་པོ༌[^911]རྣམས་ཀྱི་ཐེ་ཚོམ་གླེངས་པ༌[^912]དང་། ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས༌[^913]ཐེ་ཚོམ་དེ་ལྟ་བུ་སྔོན་མ་ཐོས་པ་གླེངས་པ༌[^914]དང་། ཡང་ཚིགས་བཅད་གསུམ་གྱིས་བཅོམ་ལྡན་འདས་ལ་ཡང་དོན་དེ་བཤད་པར་གསོལ་བའོ། །

[Block 921]
དེ་དག་ལ་ཡང་དེ་བཞིན་གཤེགས་པ་ཉིད་ཀྱིས་དགོངས་ཤིང་མཁྱེན་པ་ཟབ་ཅིང་རྒྱ་ཆེ་བ་དང་། ཐོགས་པ༌[^915]མེད་པར་འཇུག་པ་བསྟན་ཏོ། །

[Block 922]
ཉི་མ་ཞེས་པ་ནི་བཅོམ་ལྡན་འདས་ཀྱི་ཡོན་ཏན་གྱི་དཔེ་སྟེ། ཉི་མ་དེས༌[^916]མུན་པ་སེལ་བ་དང་། བྱ་བ་ལ་འཇུག་པ་སློང་བ་དང་། བྱ་མང་པོ་སྐད་འབྱིན་པ་དང་། གདུང་བ་བསྐྱེད་པ་བཞིན་བཅོམ་ལྡན་འདས་འཇིག་རྟེན་དུ་བྱུང་བ༌[^917]བས་ཀྱང་མ་རིག་པའི་མུན་པ་སེལ་བ་དང་། བསོད་ནམས་ཀྱི་བྱ་བ་བྱེད་པ་སྟོན་པ་དང་། འཁོར་མང་པོ་ལ་ཆོས་སྒྲོག་པ་དང་། བདུད་དང་མུ་སྟེགས་གདུང་བ་བསྐྱེད་པའོ། །

[Block 923]
མདོ་ལས།

[Block 924]
སྙིང་པོ་བྱང་ཆུབ་བརྗོད་མཛད་པ། །ཞེས་པ་ནས། །མ་དྲིས་པར༌[^918]ཡང་གསུང་མཛད་པ། །ཞེས་པའི་བར་དུ་ནི་ཚིགས་བཅད་གོང་མ་གཉིས་ཀྱིས་ནི་མངོན་པར་བྱང་ཆུབ་པ་དང་། མྱ་ངན་ལས་འདས་པ༌[^919]ཤེས་པ༌[^920]བསྟན། འོག་མ་གཉིས་ཀྱིས་ནི་གོང་མ་དེ་ཉིད་ཐེག་པ་རྣམ་གཉིས་ཀྱིས་ནི་མི་ཤེས་ཏེ། ཡེ་ཤེས་ཟབ་མོའི་སྤྱོད་ཡུལ་དུ་བསྟན་པའོ། །

[Block 925]
མདོ་ལས།

[Block 926]
ཉིད་ཀྱི་སྤྱོད་པ་ཀུན་ཀྱང་བརྗོད། །ཞེས༌[^921]པ་ནས། ཐུབ་པ་ཆེན་པོ་ལུང་བསྟན་གསོལ། །ཞེས་པའི་བར་དུ་ནི་དེ་ལ་དང་པོའི་ཚིགས་བཅད་གཅིག་གིས་ནི་བཅོམ་ལྡན་འདས་ཏིང་ངེ་འཛིན་ལས་བཞེངས་ཤིང་ཆོས་ཉིད་ཀྱིས་བསྒྲགས་པ་དང་། དེའི་འོག་མས་ནི་འཁོར་བཞི་རྣམས་ཀྱི་ཐེ་ཚོམ་གླེང་ཞིང་དགྲོལ་བར་གསོལ་བའོ། །

[Block 927]
མདོ་ལས།

[Block 928]
ཇི་སྙེད་འཁོད་པའི་ཉན་ཐོས་ནི། །ཞེས་པ་ནས། འོན་ཏེ་བདག་ལ་སྤྱོད་བསྟན་ཏམ། །ཞེས་པའི་བར་དུ་ནི་འབྲས་བུ་ཐོབ་པ་དེ་འབྲས་བུ་ཉིད་མངོན་དུ་གྱུར་པའམ། རྒྱུ་མངོན་དུ་གྱུར་པ་ཡིན། འབྲས་བུ་མངོན་དུ་གྱུར་པ་ཡིན་ན་ནི་མངོན་པར་བསྟོད་ཀྱང་ཅི་དགོས། རྒྱུ་མངོན་དུ་གྱུར་པ་ཡིན་ན་ནི་རྒྱུ་བསྒྲུབས་པས༌[^922]གཟོད༌[^923]འབྲས་བུ་རྩོམ་པ་ཡིན་པའི་ཕྱིར་འཁོར་རྣམས་ཀྱིས༌[^924]ཐོབ་པར་ངེས་པའི་སེམས་བསྐྱེད་དེ། དེ་ངེས་པའི་དོན་མེད་པས་ཤཱ་རིའི་བུ་ཐེ་ཙོམ་དུ་གྱུར་པ་བསྟན་ཏོ། །

[Block 929]
མདོ་ལས། །

[Block 930]
རྔ་མཆོག་དབྱངས་ཀྱིས༌[^925]རབ་ཏུ་སྒྲ་ཕྱུང་སྟེ། །ཞེས་པ་ནས། ཀྱེ་མ་ཇི་ལྟར་སྤྱོད་རྫོགས་བྱས། །ཞེས་པའི་བར་དུ་ནི་འཕགས་པ་ཉན་ཐོས་པའི་འཁོར་རྣམས་ཀྱིས༌[^926]ཆོས་བཤད་པར་གསོལ་བ་དང་། ཕྱིའི་འཁོར་རྣམས་ཀྱིས་ཆོས་བཤད་པར་གསོལ་བའོ། །

[Block 931]
དེ་བཞིན་གཤེགས་པས་བསྟན་པའི་ཐུགས་ལས་སྐྱེས་པའི༌[^927]སྲས་པོས། མངལ་ནས་སྐྱེ་བ་ལ་སོགས་པ་གསོལ་བའོ། །

[Block 932 [HEADING]]
#### མི་བཤད་པར་དགག་པ། ^4-2-6-0

[Block 933]
མདོ་ལས་དེ་སྐད་ཅེས་གསོལ་པ་དང་ཞེས་པ་ནས་སྡང་བར་འགྱུར༌[^928]ཞེས་པའི་བར་དུ་ནི་འདི་ལ་དུམ་བུ་གཉིས་སུ་དབྱེ་སྟེ། སྔར་དགག་པ་དང་ཕྱིས་གསོལ་བ་སྟེ། འདི་ནི་མི་བཤད་པར་དགག་པའོ། །

[Block 934]
ཡང་འཆད་ཅིང་ལུང་སྟོན་པ་ཡང་རྣམ་པ་བཞི་སྟེ། ངེས་པར་ལུང་བསྟན་པ་ལ་སོགས་པའོ། །

[Block 935]
ཡང་ལུང་བསྟན་པ་ཡང་རྣམ་པ་གསུམ་སྟེ་སྔོན་འདས་པའི་དུས་ན་འཁོར་རྣམས་ཀྱིས༌[^929]ལེགས་ཉེས་ཅི་བྱས་པ་སྟོན་པ་དང་། སྐྱེས་བུ་ཆེན་པོ་སངས་རྒྱས་སུ་ལུང་སྟོན་པ་དང་། ལྡེམ་པོ་ངག་གི་དོན་ངེས་པར་སྟོན་པའོ། །

[Block 936]
ཡང་འགྲེལ་པ་ལས་དོན་རྣམ་པ་བཞི་ལ་བརྟེན་ཏེ། སེམས་ངེས་པ་དང་། ལུང་སྟོན་པའི་རྒྱུ་དང་ལུང་ནོད་པ་དང་། ལུང་དཔོག་པར་གསོལ་བ་སྟེ། སེམས་ངེས་པ་ལ་ནི་དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་ངེས་པར་ཡོད་པ་ལས་དགོངས་ཏེ་མི་བཤད་པར་དག༌[^930]པའོ། །

[Block 937]
སྡང་བ་ལ་རྣམ་པ་ལྔ་སྟེ། སྐུར་བས་སྡང་བ་དང་སྒྲུབ་དཀའ་བའི་ཕྱིར་སྡང་བ་དང་། ཕྱིན་ཅི་ལོག་དུ་སྡང་བ་དང་། འགྱོད་པས་སྡང་བ་དང་། [^931]དོགས་པས་སྡང་བའོ། །

[Block 938]
སྐུར་པས་སྡང་བ་ནི་ཐོས་པའི་སྒྲས་སྡང་བ་སྟེ་ཉན་ཐོས་ཀྱི་མྱ་ངན་ལས་འདའ་བ་ཉིད་ཡང་དག་པའི་མཐའ་ཡིན་པར་སེམས་པ་ལ་ཐེག་པ་ཆེན་པོའི་མྱ་ངན་ལས་འདའ་བ་ཐོས་པས་གཉིས་ཀ་ལ་སྐུར་ཅིང་སྡང་བ་དང་། སྒྲུབ་དཀའ་བའི་ཕྱིར་སྡང་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་བསྐལ་པ་གྲངས་མེད་པར་བསྒྲུབས་པས༌[^932]གདོད་འགྲུབ་པ་ལས་སེམས་ནུར་ཞིང་སྡང་བ་དང་། ཕྱིན་ཅི་ལོག་གིས་སྡང་བ་ནི་དབང་པོ་མ་སྨིན་པའི་སེམས་ཅན་མ་རབས༌[^933]ཀྱི་རིགས་ཅན་ཉོན་མོངས་པ་སྟུག་པ་བདག་དང་བདག་གིར་འཛིན་པ་ལ་ཞེན་པ་ལ་ཆོས་ཟབ་མོ་བསྟན་ན་ཕྱིན་ཅི་ལོག་ཏུ་འཛིན་ཅིང་སྡང་བ་དང་། འགྱོད་པའི་སྡང་བ་ནི་འཕགས་པ་ཤཱ་རིའི་བུ་ལྟ་བུ་ཐེག་པ་ཆུང་ངུ་ལ་གནས་པའི་སེམས་ལ་འགྱོད་ཅིང་དངང༌[^934]བས་ཐེག་པ་ཆེན་པོ་ལ་འཇུག་པ་ལྟ་བུའོ། །

[Block 939]
དོགས་པས༌[^935]དངང་བ༌[^936]ནི་ལྷག་པའི་ང་རྒྱལ་ཅན་ཏེ། དེ་ཡང་ཉན་ཐོས་ཀྱི་རིགས་ལ་ནི་རིགས་ངེས་པ་དང་མ་ངེས་པ་གཉིས་སོ། །

[Block 940]
སེམས་ཅན་མ་རབས་ལ་ནི་མ་ཐོབ་པ་ཐོབ་པར་སེམས་པ་དང་། ཉོན་མོངས་པ་སྟུག་པོ༌[^937]དང་ལྡན་པའོ། །

[Block 941]
བྱང་ཆུབ་སེམས་དཔའ་ལ་ནི་ཕྱིར་ལྡོག་པ་དང་མི་ལྡོག་པ་ལ་གནས་ཏེ༌[^938]ངེས་པའི་རིགས་ཅན་གྱི་ཉན་ཐོས་ནི་སྐུར་པས་དངང༌[^939]ངོ་། །མ་ངེས་པའི་རིགས་ཅན་ནི་འགྱོད་པས་དངང༌[^940]ངོ་། །མ་ཐོབ་པ་ཐོབ་པར་སེམས་པ་ནི་དོགས་པས་དངང༌[^941]ངོ་། །ཉོན་མོངས་པ་སྟུག་པ་ནི་ཕྱིན་ཅི་ལོག་གིས་དངང༌[^942]ངོ་། །ཕྱིར་ལྡོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་སྒྲུབ་པར་དཀའ་བས་དངང༌[^943]ངོ་། །ཕྱིར་མི་ལྡོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་དངང་བ༌[^944]རྣམས་དང་བྲལ་བ་སྟེ། ཐེག་པ་གཅིག་པོ་བཤད་པར་འོས་པའི་སྣོད་དུ༌[^945]གྱུར་པའོ། །

[Block 942]
ཡང་མི་བཤད་པར་དགག་པ་ནི་གང་ཟག་རྣམ་པ་གཉིས་ཀྱི་དོན་ཏེ། དེ་བཞིན་གཤེགས་པའི་སྙིང་པོ་ལ་ངེས་པའི་སེམས་པ་དང་སྒྲུབ་པར༌[^946]དཀའ་བ་ལས་ལྷག་པར༌[^947]སེམས་པ༌[^948]གཉིས་ཀྱི་ཕྱིར་རོ། །

[Block 943]
ཡང་མི་བཤད་པར་དགག་པ་ནི་ལྷ་དང་མི་ལ་སོགས་པ་དོན་མ༌[^949]རྟོགས་པར་དངང་བ༌[^950]དང་། འཁོར་མང་པོ་དོན་ཟབ་མོ་ཚོལ་དུ་གཞུག་པ་དང་། གུས་ཤིང་རིན་ཆེ་བར་སེམས་སུ་གཞུག་པ༌[^951]དང་། ལྷག་པའི་ང་རྒྱལ་ཅན་རྣམས་གདུལ་བའི༌[^952]ཕྱིར་རོ། །

[Block 944 [HEADING]]
#### ཆོས་བཤད་པར་གསོལ་བ། ^4-2-7-0

[Block 945 [HEADING]]
##### ཚིག་རྐྱང་པས་གསོལ་བ། ^4-2-7-1-0

[Block 946]
མདོ་ལས་ཡང་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུས་ཞེས་པ་ནས་བདེ་བར་གཤེགས་པ༌[^953]བཤད་དུ་གསོལ་ཞེས་པའི་བར་དུ་ནི་འདས་པའི་དེ་བཞིན་གཤེགས་པ་གྲངས་མེད་པ་རྣམས་ཀྱིས༌[^954]སེམས་ཅན་གྱི་དོན་མཛད་པར༌[^955]སྟོན་པ་སྟེ། འདི་ཆོས་བཤད་པར་གསོལ་བ་གཉིས་པ༌[^956]སྔར་ནི་ཚིག་རྐྱང་པས་གསོལ། དེའི་འོག་ཏུ་ནི་ཚིགས་སུ་བཅད་པས་བསྡུས་པ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 947]
མདོ་ལས་དེ་ཅིའི་སླད་དུ་ཞེ་ན་ཞེས་པ་ནས་ཡིད་ཆེས་པ་དང་འཛིན་པ་མཆིས་སོ་ཞེས་པའི་བར་དུ་ནི་འདི་བསྟན་པར་འོས་པའི་རྒྱུ་བསྟན་པ་སྟེ། སྔོན་དེ་བཞིན་གཤེགས་པ་མཐོང་བའི་རྒྱུ་བཟང་པོ་ཡོད་པ་ཤེས་རབ་རྣོ་ཞིང་དབང་པོ་གསལ་བ་དོན་ཟབ་མོ་ལ༌[^957]མཁས་པའི་འཁོར་རྣམས་ཞེས་སྦྱར་རོ། །

[Block 948 [HEADING]]
##### ཚིགས་སུ་བཅད་པས་བསྡུས་པ། ^4-2-7-2-0

[Block 949]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་ཁྱོད་ཀྱིས༌[^958]ཆོས་བསྟན་གང་གིས་འཚལ་བར་འགྱུར་ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པས་བསྡུས་པའོ། །

[Block 950 [HEADING]]
#### དགག་པ། ^4-2-8-0
--- END BLOCKS ---
