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
བསོད་ནམས་ཀྱི་ཡོན་ཏན་ཞེས་བྱ་བ་ལ་སོགས་པས་ཀྱང་བསྐྱེད་པའི་གནས་ཡིན་པའི་ཕྱིར་དྲི་བ་ཡིན་ནོ། །

[Block 912]
གང་གིས་ཐོབ་པའི་མཚན་མ་དེས་ན་ཟན་ཆང་གཅིག་ཅེས་བྱ་བའི་སྐལ་པ་སྒོམ་པའོ། །

[Block 913]
ཐུབ་པ་ནི་རབ་ཏུ་བྱུང་བ་ལའོ། །

[Block 914]
གུས་པར་ཕུལ་བ་ཞེས་བྱ་བ་ནི་སྲི་ཞུས་བྱིན་པའོ། །

[Block 915]
དེ་ཚེ་གཉིད་ཀྱིས་ལོག་ལས་ཞེས་བྱ་བས་ནི་སྔ་མའི་ལུས་ཡང་དག་པར་རྟོགས་པའོ། །

[Block 916]
འཆི་བའི་སེམས་ལས་སད་པ་བཞིན། །ཞེས་བྱ་བ་ཡིན་ཏེ། ཉིང་མཚམས་སྦྱོར་བར་གྱུར་པས་སོ།[^498] །མགོན་ཁྱོད་ཅེས་བྱ་བ་ནི་གང་གི་མགོན་གང་ཡིན་པ་དེ་ནི་མགོན་པོ་སྟེ། དེར་གྱུར་པ་དེ་ནི་མགོན་ཁྱོད་གྱུར་པའོ། །

[Block 917]
ས་དང་བཅས་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སའི་མགོན་དུ༌[^499]གྱུར་པ་ཞེས་བྱ་བ༌[^500]ཡིན་ཏེ། དེས་ན་བདག་ཀྱང་ཁྱོད་དང་འདྲ་བར་གྱུར་ཞེས་བྱ་བ་བསྟན་པའི་དོན་ཏོ། །

[Block 918]
ཇི་ལྟར་ཐུབ་པས་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་ཏེ། ཇི་ལྟར་བསོད་ནམས་ཀྱི་འབྲས་བུ་བསྟན་པ་བཞིན་དུ་རྒྱལ་པོས་ཀྱང་བསོད་ནམས་ཀྱི་འབྲས་བུ་བསྟན་པ༌[^501]སྟེ། དེ་བས་ན་བསོད་ནམས་ལ་གུས་པ་བསྐྱེད་པ་ཞེས་བྱ་བ་ནི་བསོད་ནམས་དེ་ཉིད་ཆུང་ངུ་ཡིན་ཡང་རྣམ་པར་སྨིན་པ་ཆེ་བ་ཡིན་པས་བསོད་ནམས་ལ་སེམས་མངོན་པར་དང་བ་སྟེ། བསོད་ནམས་ཀྱི་བྱ་བ་བསྐྱེད་པ་དག་པ༌[^502]དང་། སེམས་མངོན་པར་དང་བར་འགྱུར༌[^503]ཞིང་ལས་ཀྱི་འབྲས་བུ་ལ་ཡིད་ཆེས་པས་སེམས་རྙོག་པ་དང་བྲལ་བ་ཡིན་ཏེ། ཆུ་དངས་པ༌[^504]བཞིན་ནོ། །

[Block 919]
ཡ་མཚན་ལ་རྩེ་གཅིག་ཏུ་གྱུར་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པ་དག་གིས་ཡ་མཚན་དུ་གྱུར་པ་དེ་ལ་ཡང༌[^505]དག་པར་བསྟན་པའོ། །

[Block 920]
ད་ནི་དགེ་བ་མི་ཆེ་བས་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་ལྔས་ནི་ཡང་དག་པར་ལེན་པའི༌[^506]དབང་དུ་བྱས་པ་སྟེ། དེ་ལ་དགེ་བ་མི་ཆེ་བས་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་དོན་ནི་འདི་ཡིན་ཏེ། དགེ་བ་ཞེས་བྱ་བ་ནི༌[^507]ཚུལ་ཁྲིམས་དང་སྦྱིན་པ་ལ་སོགས་པའོ། །

[Block 921]
རྒྱ་ཆེན་ཞེས༌[^508]བྱ་བས༌[^509]ནི་བདག་ཉིད་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏོ། །

[Block 922]
སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་ཀྱི་བྱ་བས་རྣམ་པ་ཐམས་ཅད་ཀྱིས༌[^510]མངོན་པར་མཐོ་བ་ལ་འཇུག་པ་དང་ལྡན་པར་བསྟན་པས༌[^511]རྣམ་པ་ཐམས་ཅད་ཀྱིས༌[^512]དགེ་བ་བྱ་བ་དང་ལྡན་པར་བསྟན་པའོ། །

[Block 923]
དེ་རྣམ་པ་ཐམས་ཅད་ཀྱིས་ནུས་པ་ཡིན་ན་ཡང་བྱ་བ་གཞན་བསྟན་པ༌[^513]ཡིན་ནོ། །

[Block 924]
དེ་ལྟར་མི་རུང་ཞེས་བྱ་བའི་དོན་བསྟན་པ་ནི་དེ་ལྟར་ཡང་མི་བཟོད་དོ་ཞེས་བྱ་བ་སྟེ། འདི་ནི་དེ་བས་ན་སྐྱེ་བ་གཞན་དག་ཏུ་མེད་པར་བསྟན་པ་ཡིན་ཏེ། ཇི་ལྟར་ཞེ་ན། ནོར་གྱིས་ཆོག་པར་ཡོད་ཀྱང་ཞེས་བྱ་བ་སྨོས་པ་སྟེ། སྦྱིན་པའི་དངོས་པོ་ལ་ཡང་ངན་ཅིང་ཞེན་པའི་ཕྱིར་སྦྱིན་པ་ཆུང་བ་སྟེ། བདག་ཉིད་ལ་ཆགས་པ་དང་ལྡན་པས་དེ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ཡང་སྦྱིན་པ་མི་ནུས་པར་སྟོན་ཏོ། །

[Block 925]
དེ་ལྟར་མི་རུང་ཞེས་བྱ་བ་ལ་རུང་བ་ནི་བཟོད་པར་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 926]
ད་ནི་དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར་བློ་བསྒྲིབས་ནས་ཞེས་སྨོས་ཏེ། མུན་པ་བཞིན་དུ་བློ་བསྒྲིབས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 927]
གྲགས་པ་ཞེས་སྨོས་པ་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་འབྲས་བུ་ནི་རེ་ཞིག་གཞག༌[^514]གི། འཇིག་རྟེན་འདིའི་འབྲས་བུ་མངོན་སུམ་དུ་འདོད་པའི་ཕྱིར་ཡང་སྦྱིན་པ་སྦྱིན་པར་བྱ་བ་སྟེ། གྲགས་པའི་དོན་དུ་ཡང་ངོ་། །སེར་སྣའི་མུན་པས་ཞེས་བྱ་བ་ནི་སེར་སྣའི་མུན་པས་བློ༌[^515]རབ་ཏུ་གཡོགས་པའི་ཕྱིར་རོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 928]
དེ་ཉིད་བསྒྲུབ་པའི༌[^516]ཕྱིར། དབང་མེད་པར་ནི་གང་ཞིག་ཅེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས༌[^517]བཅད་བརྩམས་པ་ཡིན་ཏེ། དབང་མེད་པར་ནི་གང་ཞིག་བཏང་དགོས་ཞེས་བྱ་བ་ནི་རྐུན་པོ་དང་། ཆུ་ལ་སོགས་པ་རྣམས་ཀྱིས་ཀྱང་ནོར་འཇིག་པར་འགྱུར་ལ། ཐ་མར་ཡང་བདག་ཉིད་འཆི་བས་མི་རྟག་པ་སྟེ། དེས་ན༌[^518]ནོར་ནི༌[^519]བཏང་དགོས་པ་ཡིན་ནོ། །

[Block 929]
དེ་བཞིན་སུ་ལའང་ཕན་མི་ཐོགས། །ཞེས་བྱ་བ་ནི་དབང་མེད་པར་ཡོངས་སུ་བཏང་བས་བདག་ཉིད་ཀྱི༌[^520]ཡིན་ཞིང་གཞན་རྣམས་ཀྱི་ནོར༌[^521]ཡིན་པའི་ཕྱིར་རོ། །

[Block 930]
ནོར་དེ་རིགས་པར་ཞེས་བྱ་བའི་ཡོན་ཏན་དེ་ཕན་པ་ཡིན་ཞིང་། གལ་ཏེ་སྦྱིན་པའི་ཞིང་ལ་བྱིན་ན་ནི་ཡོན་ཏན་འགའ་ཞིག་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བ་ཡིན་ཏེ། ཐ་ན་གྲགས་པ་ཡང་ངོ་། །དེ་ལ་ཞེས་བྱ་བ་ནི་ངེས་པར་ཡོངས་སུ་བཏང་བ་ལའོ། །

[Block 931]
སེར་སྣའི་ལམ་ལ་བརྟེན་ཞེས་བྱ་བ༌[^522]ནི་མི་སྟེར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 932]
སྔར་ཤེས་བཞིན་དུ་སྟེ་ཡོན་ཏན་གྱི་ཉམས་སམ། ཡོན་ཏན་གྱི་རོ་ཚོར་བཞིན་དུ་སུ་ཞིག་དེ་ལྟར་མི་སྦྱིན་ཞེས་པའོ། །

[Block 933]
ཡོན་ཏན་དེ་དག་གང་ཡིན་ཞེ་ན། སྨྲས་པ། སྦྱིན་པ་ལས་བྱུང་ཡོན་ཏན་དགའ་ལ་སོགས་པ་ཞེས་སྨོས་ཏེ། ཇི་ལྟར་དགའ་བ་ལ་སོགས་པའི་ཡོན་ཏན་ཡིན་ཞེ་ན། ལྷག་པར༌[^523]རྗེས་སུ་འབྲང་བའི་ཡིད་ཚིམ་པའི་དགའ་བ་སྐྱེས་པས་ལུས་སྦྱངས་པར་འགྱུར་རོ། །

[Block 934]
ལུས་སྦྱངས་པ་ལས་ནི་བདེ་བ་སོ་སོར་མྱོང་བར་འགྱུར་རོ། །

[Block 935]
སེམས་བདེ་བས་ནི་ཏིང་ངེ་འཛིན་ལ་མཉམ་པར་འཇོག་པར་འགྱུར་རོ། །

[Block 936]
སེམས་མཉམ་པར་གཞག་པ༌[^524]ལས་ནི་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་ཤེས་པར་འགྱུར་ཏེ། དེ་ལྟར་དགའ་བ་ལ་སོགས་པའི་ཡོན་ཏན་སྦྱིན་པ་ལས་བྱུང་བའི་གྲགས་པ་དང་ཡང་ལྡན་པར་འགྱུར་རོ། །

[Block 937]
ད༌[^525]ནི་སྦྱིན་པའི་ཆོས་དང་། དོན་དང་། འདོད་པའི་འཁོར་གསུམ་གྱི་རྒྱུ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་འདི་བརྩམས་པ་ཡིན་ཏེ། སྦྱིན་པ་ཞེས་བྱ་གཏེར་ཆེན་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། གཏེར་ཆེན་ཞེས་བྱ་བ་གཏེར་གཞན་ནི། གོད་པ་དང་ཡོངས་སུ་ཟད་པའོ། །

[Block 938]
རྗེས་སུ་འགྲོ་ཞེས་བྱ་བ་ནི་གཏེར་གཞན་ནི་འཇིག་རྟེན་ཕ་རོལ་དུ་མི་འགྲོ་བ་ཡིན་ཏེ། འདི་ནི་འཇིག་རྟེན་ཕ་རོལ་དུ་རྗེས་སུ་འབྲང་བ་ཡིན་ནོ། །

[Block 939]
གཏེར་གཞན་ནི་རྐུན་པོ་ལ་སོགས་པ་དང་ཐུན་མོང་ཡིན་གྱི།[^526] འདི་ནི་ཐུན་མོང་མ་ཡིན་ཏེ། སྦྱིན་པའི་བདག་ཉིད་ཁྱད་པར་འཕགས་པའི་དོན་གྱི་རྒྱུར་གྱུར་པ་ཡིན་ནོ། །ཇི་ལྟར་ཆོས་ཀྱི་རྒྱུར་འགྱུར༌[^527]ཞེ་ན། ཆོས་ཀྱི་རྒྱུ་དེ་བསྟན་པའི་ཕྱིར་སྨྲས་པ། སྦྱིན་པ་འདོད་དང་སེར་སྣ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྦྱིན་པ་དང་འགལ་བའི་སེམས་ཀྱིས་ཀུན་ཏུ་འཛིན་པ་ནི་སེར་སྣའོ། །

[Block 940]
གཞན་གྱི་ཕུན་སུམ་ཚོགས་པ་ལ་མི་བཟོད་པ་ནི་འདོད་པའོ། །

[Block 941]
སྐྱོན་ནི་དེ་ལས་གཞན་པ་སྟེ། སྲེད་པ་དང་། ཞེ་སྡང་དང་། ང་རྒྱལ་དང་། མ་རིག་པ་ལ་སོགས་པའོ། །

[Block 942]
དེ་ཉིད་རྡུལ་ཡིན་པས་དེའི་རྡུལ་ཏེ། རྡུལ་ནི་སྒྲིབ་པའི་དོན་ཏོ། །

[Block 943]
དེ་བས་ན་སྐྱོན་དེ་རྣམས་སྦྱོང་བར་བྱེད་པས་ཆོས་ཀྱི་རྒྱུར་གྱུར་པའོ། །

[Block 944]
སྦྱིན་པ་འཁོར་བའི་ཞེས་པ་འདིའི་དོན་གྱིས་ནི་འདོད་པའི་རྒྱུར་གྱུར་པ་ཡིན་ཏེ། འཁོར་བ་ཉིད་ལམ་ཡིན་པས་ན་འཁོར་བའི་ལམ་སྟེ།[^528] བགྲོད༌[^529]པར་བྱ་བ་ཡིན་པས་འཁོར་བའི་ལམ་ཞེས་བརྗོད་དོ། །

[Block 945]
འཁོར་བའི་ལམ་དུ་བགྲོད་པས་ངལ་བ་ནི་འཁོར་བའི་ལམ་བགྲོད་པས་ངལ་བ་སྟེ། བཀྲེས་པ་དང་། སྐོམ་པ་ལ་སོགས་པའི་སྡུག་བསྔལ་གྱིས་ངལ་བའོ། །

[Block 946]
སེལ་བ་ཡིན་པས་མེད་པ་སྟེ། དེ་ལ་མེད་པ་ནི་འཁོར་བའི་ལམ་བགྲོད་ངལ་བ་མེད་པའོ། །

[Block 947]
འདིས་ནི་སྡུག་བསྔལ་ལས་ལྡོག་པར་བསྟན་ཏོ། །

[Block 948]
སྡུག་བསྔལ་བསལ༌[^530]ནས་བདེ་བ་བསྒྲུབ་པའི༌[^531]དབང་དུ་བྱས་ནས། སྦྱིན་པ་བདེ་བ་མང་པོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐང་ཡིན་ཏེ། གཅིག་མ་ཡིན་པའི་བདེ་བ་ཡིན་ཏེ། བདེ་བ་མང་པོའོ། །

[Block 949]
དེ་དག་སྒྲུབ་པ་ནི་བདེ་བ་མང་པོ་འགྲུབ་པའོ། །

[Block 950]
གྲོགས་པོ་བཟང་པོ་ཞེས་བྱ་བ་ནི་གྲོགས་པོ་ཡང་ཡིན་ལ་བཟང་པོ་ཡང་ཡིན་པས༌[^532]གྲོགས་པོ་བཟང་པོའོ། །ཇི་ལྟར་གྲོགས་པོ་བཟང་པོ་ཡིན་ཞེ་ན། སྔར་བཤད་པའི་ཚུལ་གྱིས་ཏེ། བདེ་བ་མང་པོ་སྒྲུབ་པར་བྱེད་པས་སོ། །
--- END BLOCKS ---
