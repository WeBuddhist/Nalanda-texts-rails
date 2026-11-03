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
དེའི་འོག་ཏུ་དེ་ནི་གཟུགས་ཡོངས་སུ་གཟུང་བ༌[^572]དང་མེད་པར་བྱ་བའི་ཕྱིར་མི་སློབ་པོ་ཞེས་བྱ་བ་ནི་གང་ལ་དེ་ལྟར་འཕེལ་བར་བྱ་བ་དང་། འགྲིབ་པར་བྱ་བའི་ཆོས་རྣམས་མེད་པ་དེ་ལ་ཁྱད་པར་དུ་འཕགས་པའི་ཆོས་རྣམས་ཡོངས་སུ་བཟུང་ཞིང་ཆོས་ངན་པ་རྣམས་ཆུད་གསན་པར་བྱ་བ་མེད་པར་སྟོན༌[^573]ཏོ། །

[Block 842]
དེ་སྐད་སྨྲས་པ་དང་། ཚེ་དང་ལྡན་པ་རབ་འབྱོར་ཅིའི་ཕྱིར་དེ༌[^574]ཡོངས་སུ་འཛིན་པ་དང་མེད་པར་བྱ་བའི་ཕྱིར་མི་སློབ་ཅེས་གསུངས་པ་ནི་གནས་བརྟན་ཤཱ་རིའི་བུས་དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་ཆོས་ངན་པ་རྣམས་ཡོངས་སུ་སྤོང་ཞིང་ཁྱད་པར་དུ་འཕགས་པའི་ཆོས་རྣམས་ཐོབ་པར༌[^575]བྱེད་ན་དེ་ལ་ཅིའི་ཕྱིར་ཡོངས་སུ་འཛིན་པ་དང་། མེད་པར་བྱ་བ་མེད་ཅེས་འདྲི་བའོ། །

[Block 843]
དེ་སྐད་ཅེས་སྨྲས་པ་དང་། གནས་བརྟན་རབ་འབྱོར་གྱིས་གཟུགས་ལ་གཟུགས་ཡོངས་སུ་མི་འཛིན་ཏོ་ཞེས་བྱ་བ་གསུངས་ཏེ། གཟུང་བ་དང་འཛིན་པ་རྣམས་མེད་པར་སྟོན་ཏོ། །

[Block 844]
དེའི་གཏན་ཚིགས་སུ་སྟོང་པ་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 845]
གཟུགས་ཀྱི་སྐྱེ་བ་ཡང་དག་པར་རྗེས་སུ་མི་མཐོང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གློ་བུར་ལ་ནི་སྐྱེ་བ་མེད་དོ། །

[Block 846]
གནས་པ་ནི་མི་འགྱུར་བའི་ངོ་བོ་ཉིད་ཡིན་པས་འགག་པ་མེད་དོ། །

[Block 847]
དེ་བཞིན་ཉིད་ལ་སྐྱེ་བ་མེད་པའི་སྔོན་མ་བྱུང་བ་བླང་བ་མེད་དོ། །

[Block 848]
འགག་པ་མེད་པས་བཟུང་བ་ལས་དོར་བ་མེད་དོ། །

[Block 849]
གཟུང་བར་བྱ་བ་མེད་པས་སྔོན་མ་བྱུང་བའི་རྣམ་པར་བྱང་བ་མེད་དོ། །

[Block 850]
དོར་བར་བྱ་བ་མེད་པས་སྤང་བར་བྱ་བའི་ཀུན་ནས་ཉོན་མོངས་པ་མེད་དོ། །

[Block 851]
རྣམ་པར་བྱང་བ་མེད་པས་འཕེལ་བ་མེད་དོ། །

[Block 852]
ཀུན་ནས་ཉོན་མོངས་པ་མེད་པས་འགྲིབ་པ་མེད་དོ། །

[Block 853]
བཙུན་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གང་ནས་བཙལ་བར་བྱ་ཞེས་བྱ་བ་ནི་འདིར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཉིད་ལས་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་བསྟན་པའི་ཕྱིར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲིས་སོ། །

[Block 854]
རབ་འབྱོར་གྱི་ལེའུ་ལས་ཞེས་བྱ་བ་ནི་གང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་འབྲིང་དུ་བཤད་པ་དེ་དག་ཐམས་ཅད་ནི་རབ་འབྱོར་གྱི་ལེའུ་ཞེས་བྱའོ། །

[Block 855]
རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་བརྩམས་ཏེ་བྱུང་བའི་ཕྱིར། དེ་བཤད་པ་ཡང་དེ་ནི་དེ༌[^576]ལས་གཟུང་བར་བྱའོ་ཞེས་བསྟན་ཏོ། །

[Block 856]
ཆོས་ཟབ་མོ་བཤད་པ་ནི་དེ་བཞིན་གཤེགས་པའི་སྤྱོད་ཡུལ་ཡིན་ན་རབ་འབྱོར་སྨོས་པ་ལྷའི་དབང་པོས་མ་བཟོད་ནས་འཕགས་པ་རབ་འབྱོར་འདི་ལྟར་བཤད་པའི་སྐབས་ཕྱེ་བ་དེ་ཁྱོད་ཀྱི་བྱིན་གྱི་རླབས་སམ།[^577] དེ་ཁྱོད་ཀྱི་མཐུའམ་ཞེས་དྲིས་སོ། །

[Block 857]
དེ་སྐད་སྨྲས་པ་དང་། གནས་བརྟན་རབ་འབྱོར་གྱིས། དང་པོར་ཀུན་རྫོབ་ཀྱི་ཚུལ་གྱིས་འདི་དག་དེ་བཞིན་གཤེགས་པའི་བྱིན་གྱི་རླབས༌[^578]ཡིན་ཏེ་དེ་བཞིན་གཤེགས་པའི་བྱིན་གྱི་རླབས༌[^579]ཀྱིས་དགྲ་བཅོམ་པ་དག་ཆོས་འཆད་དོ་ཞེས་བསྟན་ཏོ། །

[Block 858]
དེ་ནས་བརྒྱ་བྱིན་གྱིས་དེ་ཡང་མ་བཟོད་ནས། བཙུན་པ་རབ་འབྱོར་ཆོས་ཐམས་ཅད་ནི༌[^580]བྱིན་གྱི་རླབས༌[^581]མེད་ན་ཅིའི་ཕྱིར་དེ་སྐད་དུ་འདི༌[^582]ནི་དེ་བཞིན་གཤེགས་པའི་མཐུའོ། །

[Block 859]
འདི་ནི་དེ་བཞིན་གཤེགས་པའི་བྱིན་གྱི་རླབས༌[^583]སོ་ཞེས་སྨྲ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 860]
དེ་ནས་གནས་བརྟན་གྱིས་ཚིག་དེ་ལ་རྗེས་སུ་ཡི་རང་ནས། དོན་དམ་པའི་ཚུལ་དུ་ན་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བ་དེ་བཞིན་ཉིད་ལ་བྱ་བ་བསྟན་པའི་ཕྱིར་བྱིན་གྱི་རླབས༌[^584]མེད་པའི་ཆོས་ཉིད་ལ་དེ་བཞིན་གཤེགས་པ་མི་དམིགས་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་བཞིན་གཤེགས་པ་ཞེས་བྱ་བའི་ཆོས་གང་ཡང༌[^585]མེད་དོ་ཞེས་སྟོན་ཏོ། །

[Block 861]
ཆོས་ཉིད་ལ་ཀུན་བརྟགས་པའི་ཆོས་མེད་པའི་ཕྱིར་བྱིན་གྱི་རླབས༌[^586]མེད་པའི་ཆོས་ཐམས་ཅད་ཀྱི་ཆོས་ཉིད༌[^587]གང་ཡིན་པ་དེ་ལ་དེ་བཞིན་གཤེགས་པ་མེད་དོ། །

[Block 862]
ཆོས་ཉིད་ལས༌[^588]མ་གཏོགས་པའི༌[^589]ཆོས་རྣམས་མེད་པའི་ཕྱིར་བྱིན་གྱི་རླབས༌[^590]མེད་པའི་ཆོས་ཉིད་ལས་གུད་ན་ཡང་དེ་བཞིན་གཤེགས་པ་མི་དམིགས་སོ། །

[Block 863]
ཀུན་བརྟགས་པ་ལ་ཆོས་ཉིད་མི་གནས་པའི་ཕྱིར། དེ་བཞིན་གཤེགས་པ་ལ་ཡང༌[^591]བྱིན་གྱི་རླབས༌[^592]མེད་པའི་ཆོས་མི་དམིགས་སོ། །

[Block 864]
ཆོས་ལས་གུད་ན་ཆོས་ཉིད་མེད་པའི་ཕྱིར། དེ་བཞིན་གཤེགས་པ་ལས་གུད་ན་ཡང་བྱིན་གྱི་རླབས༌[^593]མེད་པའི་ཆོས་ཉིད་མི་དམིགས་སོ། །

[Block 865]
དེ་བཞིན་དུ་དེ་བཞིན་ཉིད་ཀྱི་འགྲེས་ལ་ཡང་སྦྱར་རོ། །

[Block 866]
དེ་བཞིན་དུ་གཟུགས་ལ་སོགས་པ་ནས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་མཐར་ཐུག་པའི་ཆོས་ཉིད་དང་། དེ་བཞིན་ཉིད་ཀྱི་འགྲེས་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 867]
དེ་བཞིན་གཤེགས་པའི་ཆོས་ཉིད་གང་ཡིན་པ་དེ་ནི་གཟུགས་ཀྱི་ཆོས་ཉིད་དང་ལྡན་པ་ཡང་མ་ཡིན། བྲལ་བ་ཡང་མ་ཡིན་ནོ། །

[Block 868]
གཟུགས་ཀྱི་ཆོས་ཉིད་མ་ཡིན་པ་གཞན་དང་ལྡན་པ་ཡང་མ་ཡིན། བྲལ་བ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཐ་དད་པ་མེད་དེ་གཅིག་པའི་ཕྱིར་དེ་སྐད་བསྟན་ཏོ། །

[Block 869]
གནས་དང་གནས་པའི༌[^594]དངོས་པོ་དང་། གཞན་གྱི་དངོས་པོ་དང་ལྡན་པ་དང་བྲལ་བའི་རྣམ་པར་རྟོག་པ་དག་ནི་ཐ་དད་པ་ཡོད་ན་རིགས་ཀྱི་མེད་ན་མི་རིགས་སོ། །

[Block 870]
དེ་བཞིན་དུ་དེ་བཞིན་ཉིད་ཀྱི་འགྲེས་ལ་ཡང་། ཀཽ་ཤི་ཀ་འདི་ནི་དེ་ལྟར་གང་ཆོས་ཐམས་ཅད་དང་ལྡན་པ་ཡང་མ་ཡིན། བྲལ་བ་ཡང་མ་ཡིན་པ་དེའི་མཐུའོ། །

[Block 871]
འདི་ནི་དེའི་བྱིན་གྱི་རླབས༌[^595]སོ་ཞེས་སྦྱར་བར་བྱ་སྟེ། སྟོང་པ་ཉིད་ཀྱི་མཐུ་དང་སྟོང་པ་ཉིད་ཀྱི་བྱིན་གྱི་རླབས༌[^596]ཏེ། བཤད་པ་དེ་སྟོང་པ་ཉིད་ལས་བརྩམས་ནས་བྱུང་བའི་ཕྱིར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 872]
གཟུགས་ལས་ཀྱང་བཙལ་བར་མི་བྱ་ཞེས་བྱ་བ་ནི་གཟུགས་ལ་སོགས་པ་མེད་པའི་ཕྱིར་དེ་སྐད་བསྟན་ཏོ། །

[Block 873]
གཟུགས་ལས་གཞན་དུ་ཡང་བཙལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡང་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་ཐ་དད་པ་མེད་དོ་ཞེས་ཐ་དད་པ༌[^597]མེད་པར་བསྟན་ཏོ། །

[Block 874]
དེའི་ཕྱིར་ཡོད་པ་མ་ཡིན་ཐ་དད་པ་མ་ཡིན་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 875]
ཆོས་དེ་དག་ཐམས་ཅད་ནི་ལྡན་པ་ཡང་མ་ཡིན། བྲལ་བ་ཡང་མ་ཡིན་ཏེ། འདི་ལྟར་མཚན་ཉིད་མེད་པའོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 876]
གཟུགས་ཀྱང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི་གཟུགས་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཉིས་ཀ་ཡང་ཡོད་པ་མ་ཡིན་པར་བསྟན་པའོ། །

[Block 877]
གཟུགས་ལས་གུད་ན་ཡང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཡོད་པ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་ཐ་དད་པར་བརྗོད་དུ་མི་རུང་ངོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 878]
དེ་བས་ན། ཀཽ་ཤི་ཀ་འདི་ལྟར་ཆོས་འདི་དག་ཐམས་ཅད་ནི་ཡོད་པ་མ་ཡིན་ཏེ་དམིགས་སུ་མེད་དོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 879]
དེ་ནས་ཡང་ཆོས་བཤད་པ་འདི་ངོ་མཚར་དུ་གཟུང་བར༌[^598]བསྟན་པའི་ཕྱིར་བརྒྱ་བྱིན་གྱིས༌[^599]ཚིག་རྣམ་པ་བཞི་བཀོད་དེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་ཆེ་བ་སྟེ་ཞེས་བྱ་བ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་ཚད་མེད་པ་སྟེ་ཞེས་བྱ་བ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་དཔག་ཏུ་མེད་པ་སྟེ་ཞེས་བྱ་བ་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་མཐའ་ཡས་པ་སྟེ་ཞེས་བྱ་བའོ།

[Block 880]
[^600] །གཟུགས་ཀྱི་སྔོན་གྱི་མཐའ་མི་དམིགས་ཞེས་བྱ་བ་ནི་དེའི་ཚེ་བྱུང་ངོ་ཞེས་བྱ་བའམ་མ་བྱུང་ངོ་ཞེས་བྱ་བར་སྦྱར༌[^601]རོ། །
--- END BLOCKS ---
