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
[Block 36]
དེ་ལ་ཉན་ཐོས་ཀྱི་འཁོར་ཕུན་སུམ་ཚོགས་པ་ནི་མདོ་ལས།

[Block 37]
ཉན་ཐོས་ཀྱི་དགེ་འདུན་ཚད་མེད་པ་ཐམས་ཅད་ཀྱང་ཅང་ཤེས་པ་ཞེས་གསུངས་པས་བསྟན་ཏོ། །

[Block 38]
དེའི་ཕུན་སུམ་ཚོགས་པ་ནི་མདོ་ལས།

[Block 39]
སངས་རྒྱས་ཀྱི་སྲས་ཞེས་བྱ་བ༌[^15]ནས། དེ་བཞིན་གཤེགས་པའི་བཀའ་ལ་ཤིན་ཏུ་ཞུགས་པ་ཤ་སྟག་ཅེས་གསུངས་པའི་བར་གྱི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 40 [HEADING]]
###### **བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ཕུན་སུམ་ཚོགས་པ།** ^1-1-1-2-3-2-0

[Block 41]
བྱང་ཆུབ་སེམས་དཔའི་འཁོར་ཕུན་སུམ་ཚོགས་པ་ནི་མདོ་ལས།

[Block 42]
སངས་རྒྱས་ཀྱི་ཞིང་ཐ་དད་པ་ནས་འདུས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དཔག་ཏུ་མེད་པ་ཐམས་ཅད་ཀྱང་གནས་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ཞེས་བྱ་བས༌[^16]བསྟན་ཏོ། །

[Block 43]
དེའི་ཕུན་སུམ་ཚོགས་པ་ནི་མདོ་ལས།

[Block 44]
ཐེག་པ་ཆེན་པོའི་ཆོས་ཀྱི་ངེས་པར་འབྱུང་བ་ཞེས་བྱ་བ་ནས་སེམས་ཅན་ཐམས་ཅད་ཀྱི༌[^17]གནོད་པ་ཐམས་ཅད་རབ་ཏུ་ཞི་བར་བྱེད་པའི་ས་མངོན་དུ་གྱུར་པ་ཤ་སྟག་ཅེས་གསུངས་པའི་བར་གྱི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 45]
དེ་ནི་མདོ་སྡེ་ཐམས་ཅད་ལ་སྤྱིར་འདྲ་བར་བསྟན་པ་མ་ཡིན་གྱི། འཕགས་པ་དགོངས་པ་ངེས་པར་འགྲེལ་པའི་མདོ་འདི་ལ་སོགས་པ་ཁ་ཅིག་གི་གླེང་གཞིའི་ཁྱད་པར་ཅན་ཡིན་པས་ན། ཐུན་མོང་མ་ཡིན་པའི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་སྟེ། དེ་ནི་རེ་ཞིག་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པས༌[^18]བསྡུས་པའི་དོན་བསྟན་པ་ཡིན་ནོ། །

[Block 46 [HEADING]]
#### མདོ་སྡེའི་ལུས་རྣམ་པར་གཞག་པ། ^1-1-2-0

[Block 47]
དེ་ལ་མདོ་སྡེའི་ལུས་རྣམ་པར་གཞག་པ་ནི། འཕགས་པ་དགོངས་པ་ངེས་པར་འགྲེལ་པའི་མདོ་འདིའི་མདོ་སྡེའི༌[^19]ལུས་རྣམ་པར་གཞག་པ་མཐའ་དག་གི་བདེན་པ་གཉིས་པོ་དོན་དམ་པའི་བདེན་པ་དང་ཀུན་རྫོབ་ཀྱི་བདེན་པའི་མཚན་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བ་བསྟན་པའོ། །

[Block 48]
དེ་ལ་དོན་དམ་པའི་བདེན་པ་ནི་མཚན་ཉིད་ལྔ་དང་ལྡན་པར་ཤེས་པར་བྱ་སྟེ།[^20] བརྗོད་དུ་མེད་པའི་མཚན་ཉིད་དང་། གཉིས་སུ་མེད་པའི་མཚན་ཉིད་དང་། རྟོག་གེའི་སྤྱོད་ཡུལ་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་དང་། ཐ་དད་པ་དང་ཐ་དད་པ་མ་ཡིན་པ་ཉིད་ལས༌[^21]ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་དང་། ཐམས་ཅད་དུ་རོ་གཅིག་པའི་མཚན་ཉིད་དོ། །

[Block 49]
ཀུན་རྫོབ་ཀྱི་བདེན་པ་ནི་མཚན་ཉིད་དྲུག་དང་ལྡན་པར་ཤེས་པར་བྱ་སྟེ། སེམས་ཀྱི་མཚན་ཉིད་དང་། ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་དང་། ཆོས་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པའི་མཚན་ཉིད་དང་། ཆོས་གདགས་པ་རྣམ་པར་གཞག་པ་ལས་བརྩམས་ནས་རྣལ་འབྱོར་གྱིས་ཡོངས་སུ་བསྡུས་པའི་ཞི་གནས་དང་ལྷག་མཐོང་གི་ལམ་གྱིས་རབ་ཏུ་དབྱེ་བ་དང་ཐེག་པ་རྣམ་པར་གཞག་པ་ལས་བརྩམས་ནས་ཐེག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རྣམ་པར་དབྱེ་བ་བསྟན་པ་དང་། ཐེག་པ་གདགས་པ་རྣམ་པར་གཞག་པ་ཁོ་ན་ལས་བརྩམས་ནས་དེ་བཞིན་གཤེགས་པའི་བྱ་བ་སྒྲུབ་པའི་རབ་ཏུ་དབྱེ་བས་བསྟན་པ་སྟེ།

[Block 50]
མཚན་ཉིད་བཅུ་གཅིག་པོ་དེ་དག་ནི་མདོ་ལས།

[Block 51]
དེ་ནས་བྱང་ཆུབ་སེམས་དཔའ་ཚུལ་བཞིན་ཀུན་འདྲིས་ཀྱིས་བརྗོད་དུ་མེད་པ་དང་། གཉིས་སུ་མེད་པའི་མཚན་ཉིད་དོན་དམ་པ་ལས་བརྩམས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་དོན་ཟབ་དགོངས་པ་ངེས་པར་འགྲེལ་པ་ལ་དྲི་བ་དྲིས་པ་ཞེས་གསུངས་པ་ལ་སོགས་པ་མདོ་སྡེའི་ལུས་རྣམ་པར་གཞག་པའི་ལེའུ་བཅུ་འབྱུང་བ་ལས་དོན་དམ་པའི་མཚན་ཉིད་དང་པོ་གཉིས་ནི་ལེའུ་དང་པོ་སྦྱར་རོ། །

[Block 52]
མཚན་ཉིད་ལྷག་མ་དགུ་ནི་ལེའུ་ལྷག་མ་དགུ་དང་གོ་རིམ༌[^22]བཞིན་དུ་འོག་ནས་རྒྱ་ཆེར་སྟོན་ཏེ། དེ་ནི་མདོ་སྡེའི་ལུས༌[^23]རྣམ་པར་གཞག་པས་བསྡུས་པའི་དོན་བསྟན་པ་ཡིན་ནོ། །

[Block 53 [HEADING]]
### དགོས་པ། ^1-2-0

[Block 54]
དེ་ལ་དགོས་པ་ནི་འཕགས་པ་དགོངས་པ་ངེས་པར་འགྲེལ་པའི་མདོ་བསྟན་པ་འདིས་དེ་བཞིན་གཤེགས་པའི་དགོངས་པ་ངེས་པར་དགྲོལ་བ༌[^24]དང་བདེན་པ༌[^25]གཉིས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པར་བྱ་བ་དང་། ཚོགས་གཉིས་རྫོགས་པར་བྱ་བ་དང་། བདག་མེད་པ་གཉིས་ཆུད་པར་བྱ་བ་དང་། སྒྲིབ་པ་གཉིས་སྤོང་བ་དང་། འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་གཉིས་ཐོབ་པར་འགྱུར་བ་སྟེ། དེས་ནི་དགོངས་པའི༌[^26]ངོ་བོ་ཉིད་དང་། རྒྱུ་དང་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 55 [HEADING]]
### ཚིག་གི་དོན། ^1-3-0

[Block 56]
དེ་ལ་ཚིག་གི་དོན་ནི་འདི་སྐད་བདག་གིས་ཐོས་པ་དུས་གཅིག་ན་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^27]མདོ་སྡེའི་ལུས༌[^28]མཐའ་དག་གི་མིང་དང་ཚིག་དང་ཡི་གེའི་ཚོགས་རྣམས་ཀྱི་ཚིག་གི་དོན་སོ་སོར་སྟོན་པའོ། །

[Block 57 [HEADING]]
### མཚམས་སྦྱར་བ། ^1-4-0

[Block 58]
དེ་ལ་མཚམས་སྦྱར་བ་ནི་ཚིག་གི་དོན་དེ་དག་གི་སྔ་མ་དང་སྦྱོར་བ་དང་། ཚིག་ཕྱི་མ་དང་སྦྱོར་བའི་གོ་རིམ༌[^29]སྔ་ཕྱི་མི་འགལ་བར་མཚམས་སྦྱོར་བའོ། །

[Block 59 [HEADING]]
### བརྒལ་བའི་ལན། ^1-5-0

[Block 60]
བརྒལ་བའི་ལན་ནི་རིགས་པ་དང་མི་འགལ་བར་བསྟན་པའི་ཕྱིར༌[^30]གཞན་གྱིས་དྲིས་པའི་ལན་གདབ་པ་དང་། ཉིད་ཀྱི༌[^31]དོགས་པ་བསུ་ཞིང་གཏན་ཚིགས་ཀྱིས་དགྲོལ་བ་ལ་སོགས་པས་ཐེ་ཚོམ་གྱི་རྣམ་པ་ཐམས་ཅད་གཅོད་པ་སྟེ། དེ་ལྟར་ན་དགོས་པ་དང་། ཚིག་གི་དོན་དང་། མཚམས་སྦྱར་བ་དང་། བརྒལ་བའི་ལན༌[^32]དེ་དག་ནི་མདོ་སྡེའི་མགོ་འཇུག༌[^33]གི་ལུས་མཐའ་དག་དང་སྤྱིར་མཐུན་མཐུན་དུ་སྦྱར་ཏེ་བསྟན་པ་ཡིན་གྱི་གནས་སྐབས་སོ་སོར་དབྱེ་བ་ནི་མེད་དོ། །

[Block 61]
དེ་ལ་དང་པོར་བསྡུས་པའི་དོན་མ་བསྟན་ན་མདོ་སྡེའི་དོན་བདེ་བླག་ཏུ་ཁོང་དུ་ཆུད་པར་མི་འགྱུར་བས་དེའི་ཕྱིར་དེ་རྣམ་པར་བསལ་བའི་ཕྱིར་དང་པོར་བསྡུས་པའི་དོན་བསྟན་ཏོ། །

[Block 62]
དེའི་འོག་ཏུ་དགོས་པ་མ་བསྟན་ན་ཉན་པ་པོ་རྟོག་པ་སྔོན་དུ་གཏོང་བ་དག་ནན་ཏན་གྱིས་ཉན་པ་པོ་ལ་སོགས་པར་ཁས་མི་ལེན་པས་དེའི་ཕྱིར་དེ་རྣམ་པར་བསལ་བའི་ཕྱིར་དེའི་འོག་ཏུ་དགོས་པ་བསྟན་ཏོ། །

[Block 63]
དེའི་འོག་ཏུ་ཚིག་དོན་མ་བསྟན་ན་ཉན་པ་པོ༌[^34]ཤེས་རབ་རྟུལ་པོ་དེ་དག་ལ་རྨོངས་པར་འགྱུར་བས་དེའི་ཕྱིར་དེ་རྣམ་པར་བསལ་བའི༌[^35]ཕྱིར་དེའི་འོག་ཏུ་ཚིག་གི་དོན་བསྟན་ཏོ། །

[Block 64]
དེའི་འོག་ཏུ་མཚམས་སྦྱར་བ་མ་བསྟན་ན་སྨྱོན་ཚིག་ལྟར་སྔ་ཕྱི་འབྲེལ་བ་མེད་པར་འགྱུར་བས་དེའི་ཕྱིར་དེ་རྣམ་པར་བསལ་བའི་ཕྱིར་དེའི་འོག་ཏུ་མཚམས་སྦྱར་བ་བསྟན་ཏོ། །

[Block 65]
དེའི་འོག་ཏུ་བརྒལ་བའི་ལན་མ་བརྗོད་ན་རིགས་པས་མ་གྲོལ་བས་ཐམས་ཅད་ཐེ་ཚོམ་ཟ་བར་འགྱུར་བས་དེའི་ཕྱིར་དེ༌[^36]རྣམ་པར་བསལ་བའི་ཕྱིར་དེའི་འོག་ཏུ་བརྒལ་བའི་ལན་བརྗོད་དེ། དེ་ལྟར་རྣམ་པ་ལྔ་པོ་དེ་དག་ནི་ངེས་པ་ཁོ་ནར་བརྗོད་པར་བྱ་བའི་རྩིས་མགོ་ཡིན་ནོ། །

[Block 66 [HEADING]]
## མདོ་སྡེའི་མིང་བསྟན་པ། ^2-0

[Block 67]
དེ་ལ་མདོ་སྡེ་འདིའི་མིང་འཕགས་པ་དགོངས་པ་ངེས་པར་འགྲེལ་པ་ཞེས་བྱ་བ་ནི་དོན་བཞིན་མདོ་སྡེའི་མིང་དུ་བཏགས་པ་ཡིན་ཏེ། དེ་ཡང་གསུང་རབ་ཏུ་གཏོགས་པའི་མདོ་སྡེ་ཐམས་ཅད་ཀྱི་མིང་མདོར་བསྡུ་ན་གནས་སྐབས་རྣམ་པ་བཞི་ལས་བཏགས༌[^37]པ་ཡིན་ཏེ། ཡུལ་དང་། གང་ཟག་དང་། དཔེ་དང་། དོན་གྱི་གནས་སྐབས་ལས་སོ། །

[Block 68]
[^38]

[Block 69 [HEADING]]
### ཡུལ་གྱི་གནས་སྐབས་ལས་བཏགས་པ། ^2-1-0

[Block 70]
དེ་ལ་ཡུལ་གྱི་གནས་སྐབས་ལས་བཏགས་པ་ནི་ཡུལ་གང་དུ་བཤད་པའི་གནས་སྐབས་ལས་མདོ་སྡེའི་མིང་དུ་བཏགས་པ་སྟེ། དཔེར་ན་ལང་ཀའི་གྲོང་རྡལ་དང་། ག་ཡ༌[^39]མགོའི་རིར་བཤད་པས་འཕགས་པ་ལང་ཀར་གཤེགས་པ་དང་། ག་ཡ༌[^40]མགོའི་རི་ཞེས་མདོ་སྡེའི་མིང་དུ་བཏགས་པ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 71 [HEADING]]
### གང་ཟག་གི་གནས་སྐབས་ལས་བཏགས་པ། ^2-2-0

[Block 72]
གང་ཟག་གི་གནས་སྐབས་ལས་བཏགས་པ་ནི་གང་ཟག་གང་གིས་ཞུས་པ་དང་བསྟན་པའི་གནས་སྐབས་ལས་མདོ་སྡེའི་མིང་དུ་བཏགས་པ་སྟེ། དཔེར་ན་བྱང་ཆུབ་སེམས་དཔའ་གཙུག་ན་རིན་པོ་ཆེས་ཞུས་པ་དང་། དྲི་མ་མེད་པར་གྲགས་པས་བསྟན་པས་འཕགས་པ་གཙུག་ན་རིན་པོ་ཆེས་ཞུས་པ་དང་། དྲི་མ་མེད་པར་གྲགས་པས་བསྟན་པ་ཞེས་མདོ་སྡེའི་མིང་དུ་བཏགས་པ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 73 [HEADING]]
### དཔེའི་གནས་སྐབས་ལས་བཏགས་པ། ^2-3-0

[Block 74]
དཔེའི་གནས་སྐབས་ལས་བཏགས༌[^41]པ་ནི་དཔེ་གང་གིས་དོན་མཚོན་པའི་གནས་སྐབས་ལས་མདོ་སྡེའི་མིང་དུ་བཏགས་པ་སྟེ། དཔེར་ན་སཱ་ལུའི༌[^42]ལྗང་པ་དང་། རྡོ་རྗེ་རྣོན་པོའི་དཔེས་མཚོན་ཏེ་བཤད་པས་འཕགས་པ་སཱ་ལུའི༌[^43]ལྗང་པ་དང་། རྡོ་རྗེ་གཅོད་པ་ཞེས་མདོ་སྡེའི་མིང་དུ་བཏགས་པ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 75 [HEADING]]
### དོན་གྱི་གནས་སྐབས་ལས་བཏགས་པ། ^2-4-0
--- END BLOCKS ---
