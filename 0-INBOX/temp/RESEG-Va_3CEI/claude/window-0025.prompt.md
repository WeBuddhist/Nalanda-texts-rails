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
[Block 876]
དེ་ཡང་རྣམ་པ་གསུམ་དུ་དབྱེ་སྟེ།

[Block 877]
དང་པོ་ཚིགས་བཅད་བཞིས་ནི་ཉན་ཐོས་དང་ཐུན་མོང་མ་ཡིན་པ་བསྟན། ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་རང་སངས་རྒྱས་དང་ཐུན་མོང་མ་ཡིན་པ་བསྟན། ཚིགས་བཅད་ཕྱེད་དང་བཞིས་ནི་བྱང་ཆུབ་སེམས་དཔའ་དང་ཐུན་མོང་མ་ཡིན་པར་བསྟན་ཏོ། །

[Block 878]
ཚིག་རྐྱང་པ་ལས་ནི་ཐེག་པ་རྣམ་པ༌[^872]གཉིས་དང་ཐུན་མོང་མ་ཡིན་པ་ཉི་ཚེ་བསྟན། ཚིགས་སུ་བཅད་པ་ལས་ནི་བྱང་ཆུབ་སེམས་དཔའ་དང་ཐུན་མོང་མ༌[^873]ཡིན་པའང་སྟོན་ཏོ། །

[Block 879 [HEADING]]
###### **ཉན་ཐོས་དང་ཐུན་མོང་མ་ཡིན་པ།** ^4-2-4-2-1-2-5-1-0

[Block 880]
ཉན་ཐོས་དང་ཐུན་མོང་མ་ཡིན་པའང་དབང་པོ་རྣོན་པོ་ཤཱ་རིའི་བུ་ལྟ་བུ༌[^874]དང་ཐུན་མོང་མ་ཡིན་པ་དང་། འཁོར་གཞན་དང་ཡང་ཐུན་མོང་མ་ཡིན་པ་བསྟན་པ་ལས་འདི་ནི་དང་པོ་དང་སྦྱར་རོ། །

[Block 881]
ཟག་པ་ཟད་པ་འཕགས་པ་དགྲ་བཅོམ་པའི་ལུས་ཐོབ་པའི་ཡེ་ཤེས་ཀྱིས་ཀྱང་མི་སྐྲུན༌[^875]ཅེས་པའོ། །

[Block 882]
མདོ་ལས་གལ་ཏེ་འཇིག་རྟེན་འདི་དག་ཐམས་ཅད་དུ་ཞེས་པ་ནས་དེའི་བདེ༌[^876]གཤེགས་ཡེ་ཤེས༌[^877]མི་ནུས་ཞེས་པའི་བར་དུ་འདིས༌[^878]ནི་དབང་པོ་རྣོན་པོ་འཕགས་པ་ཤཱ་རིའི་བུའི་ཡེ་ཤེས་ཀྱིས་ཀྱང་ཤེས་པར་མི་ནུས་པས་དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ཤེས་པ་དང་ཆུད་པར་དཀའ་བ་བསྟན་ཏོ།

[Block 883]
མདོ་ལས།

[Block 884]
གལ་ཏེ་ཁྱོད་འདྲར་མཁས་པ་རྣམས་ཀྱིས་སུ། །ཞེས་པ་ནས། ཐམས་ཅད་འདུས་པར་ཤེས་པར་མི་ནུས་ཏེ། །ཞེས་པའི་བར་དུ་ནི་ཕྱོགས་བཅུའི་གང་ཤེས་རབ་རྣོན་པོར༌[^879]གྱུར་པ་འཕགས་པ༌[^880]ཤཱ་རིའི་བུ་ལྟ་བུ་དང་། གཞན་ཡང་དབང་པོ་རྣོ་བ་རྣམས་ཀྱི༌[^881]ཡེ་ཤེས་གཅིག་ཏུ་བསྡུས་པའི་ཤེས་རབ་ཀྱིས་ཀྱང་ཤེས་པར་མི་ནུས་ཞེས་བསྟན་ཏོ། །

[Block 885]
མདོ་ལས།

[Block 886 [HEADING]]
###### **རང་སངས་རྒྱས་དང་ཐུན་མོང་མ་ཡིན་པ།** ^4-2-4-2-1-2-5-2-0

[Block 887]
ཇི་ཙམ་ཚད་མེད་ཡེ་ཤེས་ངས་ཤེས་པ། །ཞེས་པ་ནས། དེ་ཡི་ཡང་དག་དོན་ནི་ཡོངས་མི་ཤེས། །ཞེས་པའི་བར་དུ་ནི་རང་སངས་རྒྱས་དང་ཐུན་མོང་མ་ཡིན་པ་བསྟན་ཏེ། རང་སངས་རྒྱས་ལ་ཡང་བསེ་རུ་བཞིན་དུ༌[^882]གཅིག་པུར་གནས་པ་དང་། མང་པོ་ཁྱུས་ལྡིང་བ་སྟེ་ཆོས་རྣམ་པར་འབྱེད་པ་ལ་མ་ཞུགས་པ་ནི་གཅིག་པུ་གནས་པས་སྒྲུབ་པའོ། །

[Block 888]
ཆོས་རྣམ་པར་འབྱེད་པ་ལ་ཞུགས་པ་ནི་ཁྱུས་ལྡིང་བ༌[^883]འགྲུབ་པ་སྟེ། རྣམ་པར་གྲོལ་བའི་ཆ་མ་སྐྱེས་པ་དང་རྣམ་པར་གྲོལ་བའི་ཆ་སྐྱེས་པའི་བྱེ་བྲག་གིས་དབྱེའོ། །

[Block 889]
མདོ་ལས།

[Block 890 [HEADING]]
###### **བྱང་ཆུབ་སེམས་དཔའ་དང་ཐུན་མོང་མ་ཡིན་པ།** ^4-2-4-2-1-2-5-3-0

[Block 891]
བྱང་ཆུབ་སེམས་དཔའ༌[^884]ཐེག་པ༌[^885]གསར་ཞུགས་རྣམས། །ཞེས་པ་ནས། །འདི་ལ་དེ་དག་གི་ཡང་ཡུལ་མེད་དོ། །ཞེས་པའི་བར་དུ་ནི་བྱང་ཆུབ་སེམས་དཔའ་དང་ཐུན་མོང་མ་ཡིན་པ་བསྟན་པ་སྟེ། བྱང་ཆུབ་ཀྱང་བྱང་ཆུབ་སེམས་དཔས་མི་དཔོགས༌[^886]པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོས་མི་དཔོགས་པ་དང་གཉིས་ཏེ། འདི་ནི་དང་པོའོ། །

[Block 892 [HEADING]]
###### **བྱང་ཆུབ་སེམས་དཔས་མི་དཔོགས་པ།** ^4-2-4-2-1-2-5-3-1-0

[Block 893]
སེམས་གསར་དུ་བསྐྱེད་ཅེས་པ་ནི་ཡོན་ཏན་དྲུག་དང་ལྡན་པ་སྟེ། བསྙེན་བཀུར་བྱེད་པ། དོན་རྟོགས་པ་འཆད་མཁས་པ་འཁོར་མང་བ་སེམས་གཅིག་ཏུ་གྱུར་པ་རྣམས་ཀྱིས་ཀྱང་མི་དཔོགས་ཞེས་པའོ། །

[Block 894]
མདོ་ལས།

[Block 895 [HEADING]]
###### **བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོས་མི་དཔོགས་པ།** ^4-2-4-2-1-2-5-3-2-0

[Block 896]
ཕྱིར་མི་ལྡོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་གང་། །ཞེས་པ་ནས། །འདི་ལ་དེ་དག་གི་ཡང་ཡུལ་མེད་དོ། །ཞེས་པའི་བར་དུ་ནི་དབང་པོ་རྣོན་པོའི༌[^887]བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱིས་ཀྱང་མི་རིག་པར༌[^888]སྟོན་ཏེ། ཕྱིར་མི་ལྡོག་པའི༌[^889]ས་བརྒྱད་པ་ཡན་ཆད་དོ། །

[Block 897]
མདོ་ལས།

[Block 898 [HEADING]]
###### དད་པའི་སེམས་སྐྱེ་བ་དང་ཡང་དག་པའི་དོན་སྟོན་པ། ^4-2-4-2-2-0

[Block 899 [HEADING]]
###### **ཤཱ་རིའི་བུ་ལ་མཆོག་གི་དོན་བསྟན་ཏེ་བསྐུལ་བ།** ^4-2-4-2-2-1-0

[Block 900]
ཟབ་ཅིང་ཤིན་ཏུ་ཕྲ་བའི་ཆོས་ཤེས་པ། །ཞེས་པ་ནས། །ཡུན་རིང་བཤད་ཀྱང་མཆོག་གི་དོན་ཡིན་ནོ། །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་སུ་བཅད་པ་ཕྱེད་དང་བཞིས་དད་པའི་སེམས་བསྐྱེད་པར་བསྐུལ་བ་སྟེ། དེ་ཡང་ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་ཤཱ་རིའི་བུ་ལ་མཆོག་གི་དོན་བསྟན་ཏེ་བསྐུལ། འོག་མ་ཚིགས་བཅད་གཉིས་ཀྱིས་ནི་ཐེག་པ་རྣམ་གཉིས་ཀྱིས༌[^890]འཁོར་མང་པོ་ལ་ཐབས་ཀྱིས་བསྐུལ་བ་བསྟན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱི་བསྟན་པ་འདི་ལ་དད་པ་བསྐྱེད༌[^891]ཅིག་པའོ། །

[Block 901]
མདོ་ལས།

[Block 902 [HEADING]]
###### **ཐེག་པ་རྣམ་གཉིས་ཀྱིས་འཁོར་མང་པོ་ལ་ཐབས་ཀྱིས་བསྐུལ་བ།** ^4-2-4-2-2-2-0

[Block 903]
[^892] བསྒོའོ་ཉན་ཐོས་འདི་དག་ཐམས་ཅད་དང་། །ཞེས་པ་ནས། ཐེག་པ་གསུམ་རྣམས་ཉེ་བར་བསྟན་པ་ནི། །ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པ༌[^893]གཉིས་ཀྱིས་ཐེག་པ་གཉིས་པའི་འཁོར་ལ་ཐེག་པ་ཆེན་པོ་བསྟན་ཞིང༌[^894]བླ་ན་མེད་པར་གཏང་བའི་ཕྱིར་ཐེག་པ་གསུམ་པ་བསྟན་ཏོ། །

[Block 904 [HEADING]]
#### ཐེ་ཚོམ་གླེངས་པ། ^4-2-5-0

[Block 905]
མདོ་ལས་དེ་ནས་འཁོར་དེ་ན༌[^895]ཞེས་པ་ནས་དེ་དག་ཐམས་ཅད་འདི་སྙམ་དུ་སེམས་སོ་ཞེས་པའི་བར་དུ་ནི་འཁོར་བཞི་པོ་རྣམས་ཀྱི་ཐེ་ཙོམ་དུ་གྱུར་པ་ཆེད་དུ་གླེངས་ཏེ༌[^896]བཅོམ་ལྡན་འདས་ལ་དོན་དེ་དགྲོལ་བར་ཡིད་ཀྱིས་བསམས༌[^897]པའོ། །

[Block 906]
མདོ༌[^898]ལས་ཀྱེ་མ་གང་གི་རྒྱུ་ཅིའི་ཕྱིར་ཞེས་པ་ནས་ཤེས་པར་དཀའོ་ཞེས་པའི་བར་དུ་ནི་ཐེ་ཙོམ་གྱི་དོན་ཉིད་གླེངས་ཏེ།[^899] ཐེག་པ་རྣམ་པ༌[^900]གཉིས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་ཤེས་པར་དཀའ་བའི་དོན་དེ་དངོས་སུ་གང་ཡིན་ཞེས་པའོ། །

[Block 907]
མདོ་ལས་དེ་ལྟར་བཅོམ་ལྡན་འདས་ཀྱིས་རྣམ་པར་གྲོལ་བ༌[^901]གཅིག་གོ་ཞེས་བཀའ་སྩལ་པ་ཞེས་པ་ནས་མ་རིག་གོ་སྙམ་པའི་བར་དུ་ནི་འདི་ཉིད་ཐེ་ཙོམ་གྱི་དོན་ངེས་པ་སྟེ། མྱ་ངན་ལས་འདས་པ༌[^902]ཐོབ་པ་ཡན་ཆད་ནི་བསམ་གཏན་གྱི་དོན་ལ་ཐེ་ཚོམ་ཟ་བ། འཕགས་པ་ཉན་ཐོས་པ་རྣམས་ལྟ་བ་ཟབ་མོ་ལ་གཟུད་པ་དང་། མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ལ་བརྟེན་པའི་ཕྱིར་ཤེས་པ་དང་ཆུད་པར་དཀའ་བའི་དོན་ཞེས་སྨོས་སོ། །

[Block 908 [HEADING]]
##### ཚིག་རྐྱང་པས་གསོལ་བ། ^4-2-5-1-0

[Block 909]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུས་ཞེས་པ་ནས་ཡང་དང་ཡང་གསུངས་པ་དེ་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་བར་བཤད་དུ་གསོལ་ཞེས་པའི་བར་དུ་ནི་འཕགས་པ་ཤཱ་རིའི་བུས་ཐེ་ཚོམ་གླེངས་པ༌[^903]སྔར་ནི་ཚིག༌[^904]རྐྱང་པས་གསོལ། དེའི་འོག་ཏུ་ནི་ཚིགས་སུ་བཅད་པས་བསྡུས་ཏེ་གསོལ་པའོ། །

[Block 910]
དེ་ཡང་སྔར་ནི་ཐེ་ཚོམ་གྱི་དོན་གླེངས། དེའི་འོག་ཏུ་ནི་ཐེ་ཚོམ་བཅད་པར༌[^905]གསོལ་བའོ། །

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
--- END BLOCKS ---
