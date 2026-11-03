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
དེ་ཐོབ་པར་བྱེད་པའི་ལམ་ནི་རྣམ་པར་ཐར་པའི་ལམ་མོ། །

[Block 737]
བཅིང་བའི༌[^643]སྒྲ་འཛིན་པས་བཅིངས་པ༌[^644]དང་། ཉོན་མོངས་པས་བཅིངས་པ་ཞེས་ཚིག་གཉི་ག་དང་སྦྱར་ཏེ། འཛིན་པ་ཉིད་བཅིངས་པ་དང་ཉོན་མོངས་པ༌[^645]ཉིད་བཅིངས་པ་ཡིན་པས་འཛིན་པ་དང་ཉོན་མོངས་པ་བཅིངས་པའོ། །

[Block 738]
དེ་ལ་འཛིན་པ་ནི་གཟུང་བ༌[^646]དང་འཛིན་པ་ལ༌[^647]མངོན་པར་ཆགས་པ་དང་བདག་ཏུ་འཛིན་པ་དང་། སེམས་ཅན་དུ་འཛིན་པ་ལ་སོགས་པའོ། །

[Block 739]
ཉོན་མོངས་པ་ནི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་ལ་སོགས་པའོ། །

[Block 740]
བཅིངས་པ་དེ་དག་ཤེས་རབ་ཀྱིས་གཅོད་དེ། བཅིངས་པ་བཅད་ན་མྱ་ངན་ལས་འདས་པར་འགྱུར་བས། ཤེས་རབ་ནི་རྣམ་པར་ཐར་པའི་ལམ་མོ། །ཤེས་རབ་ནི་ཉོན་མོངས་པ་ཐམས་ཅད་དང་མ་འདྲེས་པའོ་ཞེས་བྱ་བ་ལ་འདོད་ཆགས་ལ་སོགས་པའི་ཉོན་མོངས་པ་ཐམས་ཅད་དང་མ་འདྲེས་ཤིང་དེ་དག་དང་མི་འགྲོགས་པའི་ཕྱིར་རོ། །ཤེས་རབ་ནི་འགྲོགས་པ་དང་སྒྲིབ་པ་དང་སྒྲིབ་པར་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པ་ལས་ལྷན་ཅིག་མི་གནས་པ་ནི་ཆོས་དེ་རྣམས་དང་མི་འགྲོགས་ཤིང་མ་འདྲེས་པའོ། །

[Block 741]
འགྲོགས་པ་ནི་འགྲོགས་པ་བཅུ་དྲུག་ཅེས་གོང་དུ་བཤད་པར་ཟད་དོ་ཞེས་སྒྲིབ་པ་དང་སྒྲིབ་པར་འགྱུར་བ་ཡང་རྣམ་པ་བཅོ་བརྒྱད་དོ་ཞེས་གོང་དུ་བཤད་དེ། དུས་གསུམ་གྱི་དབྱེ་བས་ན། སྒྲིབ་པ་ལ་སྒྲིབ་པ་དང་། [^648]སྒྲིབ་པར་འགྱུར་བ་ཞེས་རྣམ་པ་གཉིས་སུ་དབྱེའོ། །

[Block 742]
དེ་ལ་ད་ལྟར་གྱི་དུས་ཀྱི་དགེ་བ་ལ་བར་དུ་གཅོད་པ་ནི་སྒྲིབ་པའོ། །

[Block 743]
མ་འོངས་པའི་དུས་ན་དགེ་བ་ལ་བར་དུ་གཅོད་པ་ནི་སྒྲིབ་པར་འགྱུར་བའོ། །

[Block 744]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ཀྱི་སྤྱོད་པ་ཇི་སྙེད་པར་ཤེས་རབ་དང་ཡེ་ཤེས་ཀྱི་ལས་ཀྱང༌[^649]དེ་སྙེད་དོ་ཞེས་བྱ་བ་ལ། སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ཇི་སྙེད་པ་དང་། སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྤྱོད་པ་ཇི་སྙེད་པར་ཞེས་དེ་སྙེད་ཀྱི་སྒྲ་ཚིག་རེ་རེ་དང་སྦྱར་རོ། །

[Block 745]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་སེམས་ནི་སེམས་ཅན་རྣམས་ཀྱི་འདས་པ་དང་། མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བའི་སེམས་དང་སེམས་ལས་བྱུང་བ་སྐྱེས་ཤིང་བྱུང་བ་ཇི་སྙེད་པའོ། །

[Block 746]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྤྱོད་པ་ཇི་སྙེད་པ་ནི་སེམས་ཅན་འདོད་ཆགས་ལ་སྤྱོད་པ་ཉི་ཁྲི་ཆིག་སྟོང་། ཞེ་སྡང་ལ་སྤྱོད་པ་ཉི་ཁྲི་ཆིག་སྟོང་། གཏི་མུག་ལ་སྤྱོད་པ་ཉི་ཁྲི་ཆིག་སྟོང་། ཆ་མཉམ་པ་ལ་སྤྱོད་པ་ཉི་ཁྲི་ཆིག་སྟོང་དག་གོ། །

[Block 747]
སེམས་ཅན་རྣམས་ཀྱི་སེམས་དང་སྤྱོད་པ་ཇི་སྙེད་པ་དེ་དག་ཐམས་ཅད་ཤེས་རབ་ཀྱིས༌[^650]ཤེས་པར་བྱ་བ་ཡིན་པས། ཤེས་རབ་དང་ཡེ་ཤེས་ཀྱི་ལས་ཀྱང་དེ་སྙེད་དོ། །

[Block 748]
དེ་ནི་འདི་སྐད་དུ། སེམས་ཅན་ཉིད་ཀྱང་ནམ་མཁའ་བཞིན་དུ་མཐའ་ཡས་པས་ན༌[^651]དེ་དག་གི་སེམས་དང་སྤྱོད་པ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཏེ། མཐའ་ཡས་པས་དེ་ལ་དམིགས་པར་བྱེད་པའི་ཤེས་རབ་དང་ཡེ་ཤེས་ཀྱང་མཐའ་ཡས་སོ་ཞེས་བྱ་བར་འདོད་དོ། །

[Block 749]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཉོན་མོངས་པ༌[^652]དང་བག་ལ་ཉལ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཤེས་རབ་ཀྱིས༌[^653]ཉོན་མོངས་པ་བསལ་ནས་འབྲས་བུ་ཡེ་ཤེས་ཐོབ་པ་ནི་ཤེས་རབ་ཀྱི༌[^654]སྤྱོད་པའི་ཡེ་ཤེས་ཏེ། ཤེས་རབ་ཀྱི་རྒྱུ་ལས་བྱུང་བའི་ཡེ་ཤེས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 750]
ཉོན་མོངས་པ་ནི་འདོད་ཆགས་ལ་སོགས་པའོ། །

[Block 751]
བག་ལ་ཉལ་བ༌[^655]ནི་ཉོན་མོངས་པ་དེ་དག་གི་ས་བོན་ནོ། །

[Block 752]
སེམས་ཅན་གྱི་ཉོན་མོངས་པ་དང་བག་ལ་ཉལ་བ༌[^656]ཇི་སྙེད་པ་དེ་དག་ཐམས་ཅད་ཤེས་རབ་ཀྱིས་སྤང༌[^657]དགོས་པས་དེ་དག་སྤངས་པའི་ཡེ་ཤེས་ཀྱང༌[^658]དེ་སྙེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 753]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཉོན་མོངས་པའི་སྒོ་ཇི་སྙེད་པ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་རྣམས་ཀྱི་ཉོན་མོངས་པའི་རྒྱུ་ཇི་སྙེད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །ཤེས་རབ་ལ་འཇུག་པའི་སྒོའང་དེ་སྙེད་དོ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པའི་སྒོ་ཇི་སྙེད་ཡོད་པ་དེ་དག་རེ་རེ་བཞིན་ཡང་ཤེས་པར་བྱེད་པའི་ཤེས་རབ་སྐྱེད་པར་བྱེད་པའི་སྒོའང་དེ་སྙེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 754]
ཉན་ཐོས་དང་། རང་སངས་རྒྱས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་མིང་གིས་སྨོས་པའི་འཕགས་པ་དེ་རྣམས་ཀྱི་ཤེས་རབ་ཀྱང་འཕགས་པ་དེ་དག་གི་ཡེ་ཤེས་ཀྱི་གཞི་ལ་གནས་པས་འཕགས་པ་དེ་དག་གི་ཤེས་རབ་ཇི་སྙེད་པར་འཕགས་པ་དེ་དག་གི་ཡེ་ཤེས་དང་རྟེན་དང༌[^659]དེ་སྙེད་དོ་ཞེས་བྱའོ། །

[Block 755 [HEADING]]
### ཤེས་རབ་ཀྱི་འབྲས་བུ། ^1-3-0

[Block 756]
གོང་དུ་ཤེས་རབ་མི་ཟད་པ་རྒྱ་ཆེར་བསྟན་པའི་དོན་རྣམས་བསྡུ་ཞིང་དེའི་འབྲས་བུ་ཡང་བསྟན་པའི༌[^660]ཕྱིར། བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཤེས་རབ་མི་ཟད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་ནི་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པ་ལ་སྙེགས་སོ། །ཤེས་རབ་མི་ཟད་པ་འདིས་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་གོང་དུ་སྨོས་པའི་ཤེས་རབ་ཀྱི་རྒྱུ་འདིས་སོ། །

[Block 757]
དེ་བས་ན་འབྲས་བུ་ཡེ་ཤེས་མི་ཟད་པ་ཐོབ་པར་འགྱུར་ཏེ། གཟུང་བ་དང་འཛིན་པ་གཉིས་སྤངས་པ། གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ནི་ཡེ་ཤེས༌[^661]མི་ཟད་པའོ། །

[Block 758 [HEADING]]
### བསྟན་པའི་བདག་ཉིད་ཆེན་པོ། ^1-4-0

[Block 759]
བསྟན་པའི་བདག་ཉིད་ཆེན་པོ་བསྟན་པའི་ཕྱིར། ཤེས་རབ་མི་ཟད་པ་བསྟན་པའི་ཆོས་ཀྱི་ལེའུ་འདི་བཤད་པ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་ཡང་དུས་དང་གྲངས་དང་ཡོན་ཏན་གྱིས་བསྟན་ཏོ། །

[Block 760 [HEADING]]
#### དུས། ^1-4-1-0

[Block 761]
བྱང་ཆུབ་སེམས་དཔའ༌[^662]སྔོན་ཡོངས་སུ་སྦྱང་བ་བྱས་པ་ཞེས་བྱ་བས་དུས་བསྟན་ཏོ།[^663] །མོས་པས་སྤྱད་པའི་སར་མཉན་པ་དང་བསྒོམ་པ་ལ་སོགས་པའི་སྒོ་ནས་ལུས་དང་སེམས་ལས་སུ་རུང་བ་བྱས་པ་ནི་སྔོན་ཡོངས་སུ་སྦྱང་བ་བྱས་པའོ། །

[Block 762 [HEADING]]
#### གྲངས། ^1-4-2-0

[Block 763]
སུམ་ཁྲི་ཉིས་སྟོང་ཞེས་བྱ་བས་གྲངས་བསྟན་ཏོ། །

[Block 764 [HEADING]]
#### ཡོན་ཏན། ^1-4-3-0

[Block 765]
མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པར་གྱུར་ཏོ་ཞེས་བྱ་བས་ཡོན་ཏན་བསྟན་ཏེ། འཇིག་རྟེན་པའི་ཆོས་ཀྱི་མཆོག་ལས་འདས་ནས་དེ་མ་ཐག་ཏུ་ཆོས་ཀྱི་དབྱིངས་ཐམས་ཅད་དུ་འགྲོ་བའི་མཚན་ཉིད་རྟོགས་ཏེ། མཐོང་བས་སྤང་བར༌[^664]བྱ་བའི་ཉོན་མོངས་པ་རྣམས་སྤངས་ནས་ས་རབ་ཏུ་དགའ་བ་ཐོབ་པ་ནི་མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པ་ཞེས་བྱ་སྟེ། དོན་དུ་ན་ཤེས་རབ་མི་ཟད་པའི་ལེའུ་འདི་བསྟན་པའི་ཚེ་མོས་པས་སྤྱོད་པའི་ས་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་སུམ་ཁྲི་ཉིས་སྟོང་གིས༌[^665]ས་དང་པོ་རབ་ཏུ་དགའ་བ་ཐོབ་པར་གྱུར་ཏོ་ཞེས༌[^666]བའི་ཐ་ཚིག་གོ། །ཤེས་རབ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 766 [HEADING]]
## སྙིང་རྗེ་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ། ^2-0

[Block 767]
ཚད་མེད་པ་བཞི་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་སྙིང་རྗེ་བྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་བྱ་སྟེ། དེ་ཡང་རྣམ་པ་བཞི་སྟེ། བཞི་གང་ཞེ་ན་བདེ་བ་འདོད་པ་དང་། སྡུག་བསྔལ་གྱིས་གདུངས་པ་དང་། བདེ་བ་ལ་རྗེས་སུ་ཡི་རང་བ་དང་། མཉམ་པར་གནས་པའོ། །

[Block 768]
ཚད་མེད་པ་བཞི་ནི་སེམས་ཅན་རྣམས་ཀྱི་དོན་བྱེད་པས་ན་དེ་དག་ཉིད་ཀྱིས་བསྡུས་པའི་དོན་སྙིང་བརྩེ་བ་བསྟན་ཏོ། །

[Block 769 [HEADING]]
### བདེ་བ་འདོད་པ། ^2-1-0

[Block 770]
དེ་ལ་བདེ་བ་འདོད་པའི་དབང་དུ་བྱས་ནས་དེ་ནས་བྱང་ཆུབ་སེམས་དཔའ་བློ་གྲོས་མི་ཟད་པས་ཚེ་དང་ལྡན་པ་ཤ་ར་དྭ་ཏིའི་བུ་ལ་འདི་སྐད་ཅེས་སྨྲས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 771]
དེའང་རྣམ་པ་དྲུག་སྟེ། དམིགས་པར་བྱ་བ་ཚད་མེད་པས་དམིགས་པར་བྱེད་པ༌[^667]ཚད་མེད་པ་དང་། ལས་དང་འབྲས་བུ་དང་། རང་བཞིན་དང་ཁྱད་པར་དང་། རབ་ཏུ་དབྱེ་བ་བསྟན་ཏོ། །

[Block 772]
བཙུན་པ་ཤ་ར་དྭ༌[^668]ཏིའི་བུ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བྱམས་པ་ཡང་མི་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། དེ་དག་ཀྱང་བྱམས་པ་མི་ཟད་པར་འཕགས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་དམིགས་པ་ཚད་མེད་པས་དམིགས་པར་བྱེད་པ་ཚད་མེད་པ་བསྟན་ཏོ། །

[Block 773]
བློ་གྲོས་མི་ཟད་པས་སྨྲས་པ། བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་བྱམས་པ་ནི་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཚུལ་འཆོས་པ་དང་། ཁ་གསག་དང་། ཐོབ་ཀྱིས་འཇལ་བ་ཐམས་ཅད་དང་བྲལ་བ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^669]བསྟན་ཏོ། །

[Block 774]
རྙེད་པ་དང་བཀུར་སྟི་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ངན་སོང་ཐམས་ཅད་དང་མི་ཁོམ་པ་བརྒྱད་ལས་འདས་པ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་འབྲས་བུ་བསྟན་ཏོ། །

[Block 775]
ཆོས་ཀྱི་ཀུན་དགའ་ལ་དགའ༌[^670]མོས་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བག་ཆགས་དང་མཚམས༌[^671]སྦྱོར་བ་དང་ཉོན་མོངས་པའི་དྲི་ང་བ་སྦྱོང་བ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་རང་བཞིན་བསྟན་ཏོ། །
--- END BLOCKS ---
