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
[Block 841]
ཕུང་པོ་ལྔ་དང་བྲལ་བ་ནི་སྐྱེ་བ་མེད་པ་ལ་སོགས་པའོ། །

[Block 842]
ཡང་བཤད་པ་གསུམ་ནི་ཚིག་དེ་ལྔ་ལས་དང་པོའི་གཉིས་ནི་གོང་དུ་བཤད་པ་དག་དང་འདྲ། ཆོས་དེ་དག་ཅི་འདྲ་ཞེས་པ་ནི་རང་བཞིན༌[^837]མེད་པ་སྟེ་རྟེན་ཅིང་འབྲེལ་ཏེ་འབྱུང་བའི༌[^838]ཆོས་སོ། །

[Block 843]
མཚན་ཉིད་ཇི་ལྟ་བུ་ཡིན་པ་ནི་བལྟར༌[^839]རུང་བའི་མཚན་ཉིད་ཀྱི་ཆོས་རྣམས་སོ། །

[Block 844]
ངོ་བོ་ཉིད་ཇི་ལྟ་བུ་ཡིན་པ་ནི་ཕུང་པོ་ལྔ་གཟུང་བ་དང་འཛིན་པའི་ཆོས་ཏེ། ཀུན་འབྱུང་གི་ངོ་བོ་ཉིད་དམ་ལམ་གྱི་བདེན་པས་གཟུང༌[^840]བའོ། །

[Block 845]
ཡང་ཆོས་དེ་དག་ལ་བཤད་པ་བཞི་སྟེ། ཆོས་སྟོན་པའི་བྱེད་པ་ལ༌[^841]བརྟེན་ཏེ་བཤད་པ་ནི༌[^842]ཆོས་དེ་དག་གང་ཡིན་ཞེས་པ་ནི་མིང་དང་ཚིག་དང་འབྱུང་བའི་ཚོགས་ཀྱི༌[^843]བཤད་པའི་ཆོས་སོ། །

[Block 846]
ཆོས་དེ་དག་ཇི་ལྟ་བུ་ཡིན་པ་ནི་དེ་བཞིན་གཤེགས༌[^844]པའི་ཆོས་རྣམས་ལ༌[^845]བརྟེན་ཏེ་བཤད་པའི་ཆོས་རྣམས་སོ། །

[Block 847]
ཆོས་དེ་དག་ཅི་འདྲ་བ་ཞེས་པ་ནི་འདུལ་བ་གདུལ་བར་བྱ་བའི་སེམས་ཅན་རྣམས་སོ། །

[Block 848]
མཚན་ཉིད་ཇི་ལྟ་བུ་ཡིན་པ་ནི་ཚིག་གི་སྒྲ་ལ་བརྟེན་ནས་ཆུད་པར་བྱེད་པ་སྟེ། ཚིག་གི་སྒྲ་ལ་འཇུག་པའི་མཚན་ཉིད་དོ། །

[Block 849]
ངོ་བོ་ཉིད་ཅི་ཡིན་པ་ནི་ངོ་བོ་ཙམ་ལ་བརྟེན་ནས་ཆོས་ཡང་དག་པ་ལ༌[^846]འཇུག་པ་ངེས་པ་མ་ཡིན་ཏེ། དེ་ལ་ཆགས་ཤིང་ཞེན་པ་ཡང་ཡོད་དེ། ཆོས་ཀྱི་ངོ་བོ་ཉིད་ཚིག་གི་ཐ་སྙད་དང་བྲལ་བའི་ངོ་བོ་ཉིད་དུ་རྟོགས་པས༌[^847]འཇུག་པ་བསྟན་པའོ། །

[Block 850 [HEADING]]
##### ཚིགས་སུ་བཅད་པས་བསྡུས་ཏེ་བསྟན་པ། ^4-2-4-2-0

[Block 851]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེ་ཉིད་ཀྱི་དོན་རྒྱ་ཆེར་བསྟན་པ་ཞེས་པ་ནས་སུས་ཀྱང་ཤེས་པར་མི་ནུས་སོ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་སུ་བཅད་པ་ཉི་ཤུ་རྩ་གཅིག་ལ་རྣམ་པ་གཉིས་སུ་ཕྱེ་སྟེ། ཚིགས་བཅད་ཕྱེད་དང་བཅོ་བརྒྱད་ཀྱིས་ནི་གོང་གི་དམ་པ་གཉིས་བསྟན། དེའི་འོག་མ་ཚིགས་བཅད་ཕྱེད༌[^848]དང་བཞིས་ནི་དད་པའི་སེམས་སྐྱེ་བ་དང་ཡང་དག་པའི་དོན་སྟོན་པ་བཤད་དོ། །

[Block 852 [HEADING]]
###### གོང་གི་དམ་པ་གཉིས། ^4-2-4-2-1-0

[Block 853]
དང་པོ་ལ་ཡང་རྣམ་པ་གཉིས་སུ་དབྱེ་སྟེ། གོང་མ་གཉིས་ཀྱིས་ནི་དམ་པ༌[^849]གཉིས་བསྟན། དེའི་འོག་མ་ཚིགས་བཅད་ཕྱེད༌[^850]དང་བཅུ་དྲུག་གིས་ནི་དམ་པ་གཉིས་ཀྱི་དབྱེ་བ་བསྟན༌[^851]ཏེ་འདི་དང་པོའོ། །

[Block 854 [HEADING]]
###### **དམ་པ་གཉིས་བསྟན་པ།** ^4-2-4-2-1-1-0

[Block 855]
ཚིགས་བཅད་དང་པོས་ནི་སྟོན་པའི་ཡོན་ཏན་བསྟན། དེའི་འོག་མ༌[^852]གཅིག་གིས་ནི་ཆོས་ཀྱི་བསྔགས་པ་བསྟན་ཏོ། །

[Block 856]
མདོ་ལས།

[Block 857 [HEADING]]
###### **དམ་པ་གཉིས་ཀྱི་དབྱེ་བ།** ^4-2-4-2-1-2-0

[Block 858]
སྔོན་ཆད་བསྙན༌[^853]ཅིང་སྤྱད་པ༌[^854]ནི། །ཞེས་པ་ནས། ཤེས་དཀའ་ཤིན་ཏུ་ལྟ་བར༌[^855]དཀའ། །ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་བཅོ་ལྔས་དམ་པ་གཉིས་ཀྱི་དབྱེ་བ་སྟོན་ཏེ། དེ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 859]
ཚིགས་བཅད་བཅུ་བཞིས་ནི་ཆོས་དམ་པར་བསྔགས། དེའི་འོག་མ་གཅིག་གིས་ནི་ཆོས་སྨྲ་བ་དམ་པར་བསྔགས་པའོ། །

[Block 860 [HEADING]]
###### **ཀློག་ཅིང་འདོན་པ་དང་གྲུབ་ཅིང་སྤྱོད་པའི་ཤིན་ཏུ་ཟབ་པ།** ^4-2-4-2-1-2-1-0

[Block 861]
དེའི་དང་པོ་ལ་ཡང་རྣམ་པ་ལྔར་དབྱེ་སྟེ། ཚིགས་བཅད་དང་པོ་གཅིག་གིས་ནི་ཀློག་ཅིང་འདོན་པ་དང་གྲུབ་ཅིང་སྤྱོད་པའི་ཤིན་ཏུ་ཟབ་པ་གཉིས་བསྟན། དེའི་འོག་མ༌[^856]ཚིགས་བཅད་གཅིག་གིས་ནི་འབྲས་བུ་སྤྱོད་ཅིང་ཡོན་ཏན་རྣམ་པར་འཕེལ་བས་སེམས་བདེ་བའི་དམ་པ་ཐོབ་སྟེ་ཤིན་ཏུ་ཟབ་པ་གསུམ་བསྟན། ཡང་ཚིགས་བཅད་གཅིག་གིས་ནི་བླ་ན་མེད་པའི་ཟབ་པ་བསྟན། ཡང་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་འཇུག་པ་ཤིན་ཏུ་ཟབ་པ་བསྟན། ཡང་ཚིགས་བཅད་ཕྱེད་དང་དགུས་ནི་ཐེག་པ་རྣམ་པ༌[^857]གཉིས་དང་ཐུན་མོང་མ་ཡིན་པར་འཛིན་པ་ཤིན་ཏུ་ཟབ་པ་བསྟན་ཏེ་འདི་ནི་དང་པོའོ། །

[Block 862]
མདོ་ལས།

[Block 863 [HEADING]]
###### **འབྲས་བུ་སྤྱོད་པས་བསོད་ནམས་རྣམ་པར་འཕེལ་བ།** ^4-2-4-2-1-2-2-0

[Block 864]
དེ་ལྟར་སྤྱད་པ་སྤྱོད་པ་ནི། །ཞེས་པ་ནས། དེ་ནི་ཅི་འདྲ་བ་ཡང་མཐོང་། །ཞེས་པའི་བར་དུ་ནི་ཚིགས་བཅད་འདི་གཅིག་གིས་ནི་འབྲས་བུ་སྤྱོད་པས་བསོད་ནམས་རྣམ་པར་འཕེལ་བ་སྟོན་ཏེ། སེམས་དགའ་བའི་དམ་པ་ཐོབ་པ་ཡང་བརྩོན་འགྲུས་བསྐལ་པ་གྲངས་མེད་པར་སྤྱད་པས་འབྲས་བུ་དམ་པ་ཐོབ༌[^858]སྟེ། ཅི་ཡང་མཁྱེན་ཅིང་གཟིགས་པའི་དམ་པ་ཐོབ་པའོ། །

[Block 865]
མདོ་ལས།

[Block 866 [HEADING]]
###### **བླ་ན་མེད་པའི་ཤིན་ཏུ་ཟབ་པ།** ^4-2-4-2-1-2-3-0

[Block 867]
དེ་ནི་ང་ཡིས༌[^859]རབ་ཏུ་ཤེས། །ཞེས་པ་ནས། །དེ་ཡི་མཚན་ཉིད་ཅི་འདྲ་བ། །ཞེས་པའི་བར་དུ་ནི་འདིས༌[^860]བླ་ན་མེད་པའི་ཤིན་ཏུ་ཟབ་པ་བསྟན་ཏེ། དེའི་ངོ་བོ་ཉིད་དང་གཞུང་ཅི་འདྲ་བར་དེ་བཞིན་གཤེགས་པས་རབ་ཏུ་མཁྱེན༌[^861]ཅེས་པའོ། །

[Block 868]
མདོ་ལས།

[Block 869 [HEADING]]
###### **འཇུག་པ་ཤིན་ཏུ་ཟབ་པ།** ^4-2-4-2-1-2-4-0

[Block 870]
དེ་ནི་བསྟན་དུ་མི་ནུས་ཏེ། །ཞེས་པ་ནས། །རྣམ་དག་གང་རྣམས་དད་ལ་གནས་པའོ། །ཞེས་པའི་བར་དུ་ནི་འཇུག་པ་ཤིན་ཏུ་ཟབ་པ་བསྟན་ཏེ། དེ་བཞིན་གཤེགས་པའི་ཆོས་སྟོན་པ་མིང་དང་ཚིག་དང༌[^862]ཡིག་འབྲུས་ཆོས་སྟོན་པ་འཇུག་པ་དང་ཤེས་པར་དཀའ་བས་འཇུག་པ་ཤིན་ཏུ་ཟབ་པའོ། །

[Block 871]
ཡང་ན་དེ་བཞིན་གཤེགས་པ་ཉིད་ཟབ་མོ་འདི་ལ་གནས་ཤིང་ཞུགས་པའི་ཕྱིར་མུ་སྟེགས་ཅན་ལས༌[^863]ཁྱད་པར་དུ་བསྟན་ཏེ། མུ་སྟེགས་ཅན་ལྟ་བུ་རང་གི་ཆོས་སྤྱོད་ཀྱང་ཆོས་ཉིད་མ་རྟོགས་པ་ལྟ་བུ་མ་ཡིན་ཏེ། རྟེན་ཅིང་འབྲེལ་པར༌[^864]འབྱུང་བ་ཟབ་མོ་ཚིག་གི་ཐ་སྙད་དང་བྲལ་བ་སེམས་ཅན་རྣམས་ཀྱིས་འཇུག་པར་མི་ནུས་ཀྱི། བྱང་ཆུབ་སེམས་དཔའ་དད་པ་བརྟན་པ༌[^865]ལ་གནས་པ་ཉག་གཅིག་གིས་མཁྱེན་ཅེས་པའོ། །

[Block 872]
བྱང་ཆུབ་སེམས་དཔའ་ས་དང་པོ་ལ་གནས་པ་ཡན་ཆད་ཆོས་བཞི་ལ་དད་པའི་ཕྱིར་མི་ནུར་བ་རྣམས་ཀྱི༌[^866]ཆོས་འདི་ལ་བཟོད་པས་བཤད་པར་འོས་ཀྱི་གཞན་ལ་མ་ཡིན་ཞེས་པའོ། །

[Block 873]
ཆོས་བཞི་ནི་དཀོན་མཆོག་གསུམ་དང་ཚུལ་ཁྲིམས་ལ་ཡིད་ཆེས་ཤིང་ཕྱིར་མི་ནུར་བའོ། །

[Block 874 [HEADING]]
###### **ཐེག་པ་རྣམ་པ་གཉིས་དང་ཐུན་མོང་མ་ཡིན་པ།** ^4-2-4-2-1-2-5-0

[Block 875]
མདོ་ལས་གང་དེ༌[^867]འཇིག་རྟེན་གྱིས༌[^868]མཁྱེན་པའི་ཕྱིར་རྣམ་པར༌[^869]ཤེས་པ་ནས། དེ་དག་ཡུལ་མེད་རྒྱལ་བའི་ཡེ་ཤེས་ལ། །ཞེས་པའི་བར་དུ་ནི༌[^870]འདི་མན༌[^871]ཚིགས་བཅད་ཕྱེད་དང་བཅུས་ཐེག་པ་རྣམ་པ་གཉིས་དང་ཐུན་མོང་མ་ཡིན་པ་སྟོན་ཏེ། གནས་ཤིང་འཛིན་པ་ཤིན་ཏུ་ཟབ་པ་དང་སྦྱར་རོ། །

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
--- END BLOCKS ---
