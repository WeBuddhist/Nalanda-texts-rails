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
[Block 981 [HEADING]]
###### གང་ལ་བརྟེན་པར་བྱ་བ། ^4-2-10-1-3-0

[Block 982]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་པ་ནས་འཇིག་རྟེན་དུ་བྱུང་སྟེ་ཞེས་པའི་བར་དུ་ནི་གང་ལ་བརྟེན་པར་བྱ་བའི་དོན་སྟོན་ཏེ། དེ་ཡང་བྱ་བ་གཅིག་པ་དེ་སྔར་གླེང་བ་དང་ཕྱིས་དགྲོལ་བ་ལ་འདི་ནི་དང་པོའོ། །

[Block 983 [HEADING]]
###### **གླེང་བ།** ^4-2-10-1-3-1-0

[Block 984]
གང་ལ་བརྟེན་པར་བྱ་བ་ནི་བཅོམ་ལྡན་འདས་ཉག་གཅིག་གིས་མཁྱེན་པའི་ཆོས་ཏེ་ཤེས་པར་དཀའ་བའི་དོན་ཏོ། །

[Block 985]
དོན་དེ་སེམས་ཅན་རྣམས་ལ་ཕན་གདགས་པའི་ཕྱིར་སོ་སོའི༌[^1001]དབང་པོ་དང་སྦྱོར་ཞིང་ཆོས་སྟོན་པ་མཛད་དོ། །

[Block 986 [HEADING]]
###### **བསྟན་པར་བྱ་བའི་ཆོས་རྒྱས་པར་དགྲོལ་བ།** ^4-2-10-1-3-2-0

[Block 987]
མདོ་ལས་དེ་ལྟར་ན་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་ཡེ་ཤེས་མཐོང་བའི་ལམ་དུ་འཇུག་གོ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་བསྟན་པར་བྱ་བའི་ཆོས་རྒྱས་པར་དགྲོལ་བ་སྟེ། དོན་ཆེན་པོ་བྱ་བ་གཅིག་པ་ཞེས་པ་ནི། དེ་བཞིན་གཤེགས་པའི་མཁྱེན་པ༌[^1002]གཟིགས་པ་སྟེ་དེ་ཡང་དབྱེ་བ་དང་བསྟན་པ་དང་། ཆུད་པར་བྱ་བ་དང་། འཇུག་པ་དང་འདི་བཞི་སྟོན་ཏོ། །

[Block 988]
རྣམ་པ་འདི་བཞིས༌[^1003]དེ་བཞིན་གཤེགས་པའི་མཁྱེན་པ༌[^1004]གཟིགས་པ་རྟོགས་པར༌[^1005]བྱེད་དོ། །

[Block 989]
ཡེ་ཤེས་དེའི་བྱེད་པ་དང་། རང་བཞིན་གཉིས་ཀ་ལ་མཁྱེན་པ༌[^1006]གཟིགས་པ་ཞེས་བྱ་སྟེ། དོན་དམ་པ་དང་ཀུན་རྫོབ་གཉི་གའི་སྤྱོད་ཡུལ་ལ་འཇུག་པའོ། །

[Block 990]
དེ་ལ་དབྱེ་བ་ལ་ནི་བླ་ན་མེད་པའི་དོན་བསྟན་པ་ནི་མཐུན་པའི་དོན་ནི་རྟོགས༌[^1007]པར་བྱ་བ་ནི་མི་ཤེས་པ་ཤེས་པར་བྱ་བའི་དོན་ལ༌[^1008]འཇུག་པ་ནི་ཕྱིར་མི་ལྡོག་པའི་སར༌[^1009]འཇུག་ཅིང་ཡེ་ཤེས་ཀྱི་ལས་ཚད་མེད་པར་སྟོན་པའོ། །

[Block 991]
བླ་ན་མེད་པའི་བྱང་ཆུབ་དང་མྱ་ངན་ལས་འདས་པ་གཉིས་ཀ་གཞན་ལས་འཕགས་པའི་ཕྱིར་བླ་ན་མེད་པ་ཞེས་གདགས་སོ། །

[Block 992]
བསྟན་པ་མཐུན༌[^1010]པའི་དོན་ནི་ཐེག་པ་རྣམ་གསུམ་ཀུན་ལས་ཆོས་ཀྱི་སྐུས་འདྲ་བར་ཁྱབ་པའི་ཕྱིར་མཐུན་པ་ཞེས་གདགས་སོ། །

[Block 993]
རྟོགས་པར་བྱ་བ་ནི་ཐེག་པ་རྣམ་གཉིས་པ་དག༌[^1011]ཡང་དག་པའི་ངོ་བོ་མི་ཤེས་ཤིང་ཐེག་པ་རྣམ་གཅིག་གི་དོན་ལ་མི་གནས་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པས་མི་ཤེས་པ༌[^1012]ཤེས་པར་བྱ་བའི་ཕྱིར་འདི་བསྟན་པ་དང་། འཇུག་པར་བྱ་བ་ནི༌[^1013]མཚན་ཉིད་གསུམ་པོ་གང་དུ་བསྟན་པ་དེ་ལ་འཇུག་པ་དང་། ཐོབ་པར་བྱ་བའི་ཐབས་བསྟན་ཏོ། །

[Block 994]
དེ་བཞིན་གཤེགས་པ་འཇིག་རྟེན་དུ་བྱུང་སྟེ༌[^1014]ཆོས་སྟོན་པ་ཡང་རིམ་དང་ཅིག་ཅར་དང་ཆེ་ཆུང་གི་རྣམ་པ་མི་མཐུན་གྱིས་ཀྱང་སེམས་ཅན་ཐམས་ཅད་ཡེ་ཤེས་དེ་མཐོང་བ་དང་འཇུག་པར་བྱ་བ་ལས་གཞན༌[^1015]མི་སྟོན་ཏོ། །

[Block 995]
ཡེ་ཤེས་མཐོང་བ་དང་འཇུག་པ་ལ་མཐོང་བ་ནི་མངོན་དུ་རྟོགས་པ༌[^1016]ཤེས་པ་ནི་རྣམ་པར་ཤེས་པ་ལྔ་དང་ལྡན་པ་སྟེ། ཆོས་མངོན་པ་ལས་ཀྱང་མཁྱེན་ལ་མི་གཟིགས་པ་དང་། གཟིགས་ལ་མི་མཁྱེན་པ་དང་། མཁྱེན་ཀྱང་མཁྱེན་ལ་གཟིགས་ཀྱང་གཟིགས་པ་སྟེ་རྣམ་པ་གསུམ་མོ། །

[Block 996]
མཁྱེན་ལ་མི་གཟིགས་པ་ནི་ཟད་པའི་ཡེ་ཤེས་དང་། མི་སྐྱེ་པའི་ཡེ་ཤེས་སོ། །

[Block 997]
གཟིགས་ལ་མི་མཁྱེན་པ་ནི་བཟོད་པ་བརྒྱད་དང་འཇིག་རྟེན་པའི་ཡང་དག་པར་ལྟ༌[^1017]བའོ། །

[Block 998]
མཁྱེན་ཀྱང་མཁྱེན་ལ་གཟིགས་ཀྱང་གཟིགས་པ་ནི་ཡེ་ཤེས་ལྷག་མ་གཞན་དག་གོ། །

[Block 999]
རྣ་བས༌[^1018]ཐོས་པ་ལྟ་བུ་ནི་མཁྱེན་པ་དང་སྦྱར་རོ། །

[Block 1000]
མིག་གིས་མངོན་དུ་མཐོང་བ་ནི་གཟིགས་པ་དང་སྦྱར་རོ། །

[Block 1001]
ཡང་དོན་ཆེན་པོ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པའི་རང་བཞིན་བསྟན་པ་སྟེ། མ་རིག་པའི་སྒྲིབ་པས་བསྒྲིབས་པའི་སེམས་ཅན་རྣམས་ལ་ཡང་དག་པའི་རང་བཞིན་མཚོན་པ་ནི་དབྱེ་བའོ། །

[Block 1002]
དེ་ཉིད་རྣམ་པར་ཕྱེ་སྟེ་དགྲོལ་བ་ནི་བསྟན་པའོ། །

[Block 1003]
ཡང་ན་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་མ་གཏོགས་པར༌[^1019]དོན་གཞན་མེད་དོ་ཞེས་གསུངས་ཏེ་ཐམས་ཅད་མཁྱེན་པ་ནི་ཆོས་དང་གང་ཟག་ལ་བདག་མེད་པར་མཁྱེན་པའོ། །

[Block 1004]
ཡེ་ཤེས་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཏེ། དེ་གཉིས་ལས་འདའ་བའི་ཆོས་གཞན་མེད་པའི་ཕྱིར་བླ་ན་མེད་པའོ། །

[Block 1005]
དེ་ལ་དབྱེ་བ་དང་བསྟན་པ་དང་རྟོགས་པ་འདི་གསུམ་གྱིས་ནི་བླ་ན་མེད་པའི་འབྲས་བུ་བསྟན། འཇུག་པར་བྱ་བས་ནི་སྒྲུབ་པའི༌[^1020]རྒྱུ་བསྟན་ཏོ། །

[Block 1006]
མདོ་ལས་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་ཡེ་ཤེས་མཐོང་བའི་ལམ་དུ་འཇུག་གོ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པའི་མཁྱེན་པ་དང་། གཟིགས་པས༌[^1021]སེམས་ཅན་རྣམས་ལ་སྟོན་པ་སྟེ། ཐེག་པ་རྣམ་པ་གཉིས་པ་དག་བླ་ན་མེད་པའི་སྐལ་བ་མེད་པ་ཙམ་དུ་སེམས་པ་དེ་དག་འབྲས་བུ་དེ་ལ་གཟུད་པའི་ཕྱིར་རྣམ་པ་དེ་བཞིན༌[^1022]བསྟན་ཏོ། །

[Block 1007 [HEADING]]
###### ཐེག་པ་གཅིག་པོ་ལ་གནས་པར་བྱ་བ། ^4-2-10-1-4-0

[Block 1008]
མདོ་ལས་ཤཱ་རིའི་བུ་ང་ནི་ཐེག་པ་གཅིག་ལས༌[^1023]བརྩམས་ཏེ་ཞེས་པ་ནས་གཉིས་སམ་གསུམ་ཞེས་བྱ་བ་ཆུང་ཟད༌[^1024]ཀྱང་མེད་ཅེས་པའི་བར་དུ་ནི་ལུང་བསྟན་པའི་ནང་ནི༌[^1025]ཐེག་པ་གཅིག་བརྩམས་པ་ལ་གནས་པ་སྟེ། ཐེག་པ་གཅིག་བརྩམས་པ་འདི༌[^1026]སེམས་ཅན་རྣམས་ལ་ཆོས་སྟོན་གྱི་རང་སངས་རྒྱས༌[^1027]ཐེག་པ་གཉིས་པའམ། ཉན་ཐོས་ཞེས་ཐེག་པ་གསུམ་པའི་ཁྱད་པར་རིམ་པར་བཀོད་པ་མེད་དེ། དེ་ལ་ཟབ་པའམ་མི་ཟབ་པའམ་དཀའ་བའམ་སླ་བ༌[^1028]ལས་རིམ་པར་བཀོད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1009]
སྐབས་འདིར་ཐེག་པ་གཉིས་བསལ་ཏེ་ཐེག་པ་ཆེན་པོ་གཅིག་བསྟན་པའི་དོན་སྟོན་ཏོ། །

[Block 1010 [HEADING]]
###### **ཕྱོགས་བཅུའི་སངས་རྒྱས་ཀྱི་ཆོས་ལུགས།** ^4-2-10-1-4-1-0

[Block 1011]
མདོ་ལས་ཤཱ་རིའི་བུ་ཕྱོགས་བཅུའི་འཇིག་རྟེན་ཐམས་ཅད་ཀྱི་དོན་ཡང་དེའོ་ཞེས་པ་ནི་ཆོས་ལ་གནས་པ་སྟེ། ད་ལྟར་བཞུགས་པའི་སངས་རྒྱས་ཤཱཀྱ་ཐུབ་པ་ཡང་སངས་རྒྱས་ཐམས་ཅད་ཀྱི་ཆོས་ལུགས་ལ་བརྟེན་ཏེ་འགྲོ་བ་མང་པོ་ལ་དད་པ་བསྐྱེད་ཅིང་བདག་དང་འདྲ་བར་བྱ་བའི་ཕྱིར་སྔར་ཐབས་ཙམ་བསྟན་ནས་ཕྱིས་ཡང་དག་པ་གང་ཡིན་པ་སྟོན་ཏེ། སྔར་ནི་ཕྱོགས་བཅུའི་སངས་རྒྱས་ཀྱི་ཆོས་ལུགས་ཀྱང་འདིའོ། །

[Block 1012]
དུས་གསུམ་གྱི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི་ཆོས་ལུགས་ཀྱང་འདིའོ། །

[Block 1013]
ད་ལྟར་ངས་བསྟན་པའི་ཆོས་ལུགས་ཀྱང་འདིའོ་ཞེས་བསྟན་པ་སྟེ། འདི་ནི་ཕྱོགས་བཅུའི་སངས་རྒྱས་ཀྱི་ཆོས་ལུགས་བསྟན་པའོ། །

[Block 1014]
དུས་གསུམ་ལས་ཕྱོགས་བཅུ༌[^1029]ཞེས་བྱ་བ་གཞན་པ་མེད་ལ་ཕྱོགས་བཅུ་ལས་དུས་གསུམ་ཞེས་བྱ་བ་གཞན་ཡང་མེད་མོད་ཀྱི་ཆུ་ཞེང་ལས་ཁྱད་པར་དུ་བཤད་དོ། །

[Block 1015 [HEADING]]
###### **དུས་གསུམ་གྱི་སངས་རྒྱས་ཀྱི་ཆོས་ལུགས།** ^4-2-10-1-4-2-0

[Block 1016]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེས་པ་ནས་ཐེག་པ་གཅིག་ལས༌[^1030]བརྩམས་ཏེ་ཆོས་བཤད་པ་དེ་ཡང་ཐམས་ཅད་མཁྱེན་པའི་མཐའི་བར་དུ་ཞེས་པ་ནི་དུས་གསུམ་གྱི་སངས་རྒྱས་ཀྱི་ཆོས་ལུགས་བསྟན་པ་སྟེ་འདི་ལ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 1017 [HEADING]]
###### **འདས་པ།** ^4-2-10-1-4-2-1-0

[Block 1018]
སྔར་དུས་གསུམ་གྱི་ཆོས་སོ་སོར་བསྟན་པ་ཐམས་ཅད་དང་མཐུན་པ་སྟེ་སྔ་མ་ལ༌[^1031]ཡང་རྣམ་པ་གསུམ་སྟེ། འདས་པ་དང་མ་འོངས་པ་དང་ད་ལྟར་དང་གསུམ་མོ། །

[Block 1019 [HEADING]]
###### **ཆོས་ལུགས་མཐུན་པ།** ^4-2-10-1-4-2-1-1-0

[Block 1020]
གསུམ་པོ༌[^1032]ལ་ཡང་གཉིས་གཉིས་ཏེ། སངས་རྒྱས་ཀྱི་ཆོས་བསྟན་པའི་ཆོས་ལུགས་མཐུན་པ་དང་། སེམས་ཅན་གྱི་དོན་བྱས་པའི་འབྲས་བུ༌[^1033]མཐུན་པ་སྟེ། འདི་ནི་འདས་པའི་སངས་རྒྱས་ཀྱི་ཆོས་ལུགས་དང་མཐུན་པར་བསྟན་པའོ། །
--- END BLOCKS ---
