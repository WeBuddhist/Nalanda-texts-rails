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
མདོ་ལས། །

[Block 737]
གང་སྔོན་བདེ་བར་གཤེགས་པ་དེ་ཡི་སྲས། །ཞེས་པ་ནས། །ཕྱོགས༌[^730]རྣམ་པར་གྲགས་ཞེས་པའི་བར་དུ་ནི་འཁོར་རྣམས་ལ་དགོངས་པ་བསྟན་ཏེ། ཚིགས་བཅད་ཕྱེད༌[^731]དང་གསུམ་གྱིས་ཉོན་མོངས་པའི་རྒྱུ་བསྟན། ཡང་ཚིགས་བཅད་ཕྱེད༌[^732]དང་གསུམ་གྱིས་ནི་དག་པའི་རྒྱུ་བསྟན་ཏེ། འདི་ནི་དང་པོ་དང་སྦྱར་རོ། །

[Block 738]
ཁེ་དང་གྲགས་པ་དང་ཆོ་རིགས་ལ་ཆགས་པ༌[^733]ཐོས་པར་རྩོལ་བའི་ཆགས་པ་དེ༌[^734]དག་གྲགས་པར་འདོད་པའོ། །

[Block 739]
མདོ་ལས།

[Block 740]
དེ་ཡང་དགེ་བ་རྣམས་ཀྱིས༌[^735]ལས་དེ་དག །ཅེས་པ་ནས། །སྲོག་ཆགས་སྟོང་ཕྲག་བྱེ་བ་འདུལ་བར་འགྱུར། །ཞེས་པའི་བར་གྱིས་ནི་རྣམ་པར་དག་པའི་རྒྱུ་བསྟན་ཏོ། །

[Block 741]
མདོ་ལས། །

[Block 742]
དེའི་ཚེ་ལེ་ལོ་ཅན་དུ་གང་གྱུར་པ། །ཞེས་པ་ནས། །ཆོས་སྨྲ་བ་ནི་ཁོ་བོ་ཡིན།[^736] །ཞེས་པའི་བར་དུ་ནི་དོན་གཞན་ལས་གླེང་བ༌[^737]རྣམས་བསྟན་ནས་སྔོན་གྱི་ལུགས་དང་སྦྱར་བ་བསྟན་པ་སྟེ། ཚིགས་བཅད་དང་པོས་ནི་གང་ཟག་བསྟན། །དེའི་འོག་མས་ནི་ཆོས་བསྟན། དེའི་འོག་མས་ནི་བསྡུ་བ་སྟེ་འདི་ནི་དང་པོའོ། །

[Block 743 [HEADING]]
##### འོག་མ་ཉན་པ་རྣམས་ལ་གདམས་པ། ^4-1-10-3-0

[Block 744]
མདོ་ལས།

[Block 745]
ཡེ་ཤེས་འདི་ཡི་ལྟས་སྣང་འགྱུར། །ཞེས་པ་ནས་བྱང་ཆུབ་གང་འདིར་ཞུགས་ཞེས་པའི་བར་དུ་ནི་ཆོས་བསྟན་པ་དང་། ལྟས་བསྟན་ནས་གཟེངས་བསྟོད་པ་དང་། ཆོས་ཟབ་མོ་ལ་སེམས་སུ་གཞུག་པའི་ཕྱིར་ལྷའི་འོད་ཀྱིས་བསྟན་པ༌[^738]དང་། ཆོས་ཀྱི་ཆར་པ་ཕབ་པས་དགེ་བའི་མྱུ་གུ་བསྐྱེད་པ༌[^739]དང་། བྱང་ཆུབ་ཚོལ་བ༌[^740]རྣམས་ཐེ་ཚོམ་བཅད་པའོ།། །།

[Block 746]
དམ་པའི་ཆོས་པུཎྜ་རཱི་ཀའི་འགྲེལ་པ། [^741]བམ་པོ་གསུམ་པ།

[Block 747 [HEADING]]
### ཐབས་མཁས་པའི་ལེའུ། ^4-2-0

[Block 748]
འདི་མན་ཆད་ཐབས་མཁས་པའི་ལེའུ་སྟོན་ཏེ། དེ་ཡང་གདགས་པའི་གཏན་ཚིགས་དང་མིང་དགྲོལ་བ་དང་། རང་བཞིན་བསྟན་པའོ། །

[Block 749 [HEADING]]
#### གདགས་པའི་གཏན་ཚིགས། ^4-2-1-0

[Block 750]
འདི་ལ༌[^742]ཡང་ལེའུ་བརྒྱད་གཞུང་ཡང་དག་པར་འགྲེལ་པ་སྟེ། པདྨ་ཆུ་ལས་སྐྱེས་པ་དང་ཁ་འབྱེད་པའི༌[^743]དོན་གྱིས་དམ་པའི་ཆོས་ཀྱི་འབྲས་བུ་རྟོགས་པར༌[^744]སྟོན་ཏེ་ཐེག་པ་གཅིག་པོ་སྟོན་པ་ཡང་ཐེག་པ་རྣམ་པ་གཉིས་བསྩལ༌[^745]ནས་དབང་པོ་རྣམ་གསུམ་ལུང་བསྟན་པ་དང་ཐེ་ཚོམ་བསྩལ་བའི༌[^746]ཕྱིར་དཔེ་དང་ཐབས་རྣམ་པ་སྣ་ཚོགས་སྟོན་པས་ཐབས་མཁས་པའི་ལེའུ་སྟོན་པར་དགོངས་པ་དང་། ཡང་ན་ལེའུ་བཅུ་དགུ་པ་ཡང་དག་པའི་གཞུང་ཉིད་སྟོན་པ་ལ་ཐབས་མཁས་པའི་ལེའུ་འདི་མན་ཆད་ལེའུ་བཅུ་གཉིས་ཀྱིས་ཐེག་པ་གཅིག་པོ༌[^747]སྟོན་པའི་དམིགས་པ་སྟོན་པ་དང་། བདེ་བ་ལ་གནས་པ་དང་སའི༌[^748]རུམ་ནས་འཐོན་པའི་ལེའུ་གཉིས་ཀྱིས༌[^749]ཐེག་པ་གཅིག་པོའི་སྤྱོད་པ་བསྟན་པ་དང་། དེ་བཞིན་གཤེགས་པའི་ཚེའི་ཚད་ཀྱི་ལེའུ་དང་། རྟག་ཏུ་མི་བརྙས་པའི་ལེའུ་དང་། སྤྱིར་ལེའུ་ལྔས་ཐེག་པ་གཅིག་པོའི་འབྲས་བུ་བསྟན་པ་སྟེ། དམིགས་པ་བསྟན་པས་ནི་ཐེག་པ་འདིའི་དྲང་བ་དང་ངེས་པའི་དོན་མཚོན་ནས་ཉན་ཐོས་པ་རྣམས་དེ་རྟོགས་པ༌[^750]ལུང་བསྟན་པའོ། །

[Block 751]
དེ་ལ་ཡང་དང་པོའི་ལེའུ་བརྒྱད་ཀྱིས་ནི་དྲང་བ་དང་ངེས་པའི་དོན་དངོས་པོ་བསྟན་པས་དབང་པོ་རྣམ༌[^751]གསུམ་ལུང་བསྟན་པས་ཐོབ་པ་དང་། ལེའུ་གསུམ་གྱིས་ཆོས་དང་གང་ཟག་ལ་བསྟོད་ཅིང་མདོ་འདི་ལ་གཟུད་པ་དང་ལེའུ་གཅིག་གིས་བཀྲི་བའི༌[^752]དོན་སྤངས༌[^753]ཏེ་ངེས་པའི་དོན་ལ་འཇུག་པའོ། །

[Block 752]
འགྲེལ་པ་ལས་འདི་མན་ཆད་རྒྱུ་དང་འབྲས་བུའི་མཚན་ཉིད་སྟོན་ཏེ། གླེང་གཞིའི་ལེའུ་བཤད་པའི་རྗེས་ལ་གཞུང་ཉིད་བསྟན་པའི་ཕྱིར་རྒྱུ་དང་འབྲས་བུ་སྟོན་པའི་མཚན་ཉིད་རྣམ་པ་གསུམ་སྟེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་ཡེ་ཤེས་བླ་ན་མེད་པའི་འབྲས་བུའོ། །

[Block 753]
ཡེ་ཤེས་ཀྱི་འབྲས་བུ་ནི་མཚོན་པར་བྱེད་པའི་རྒྱུའོ། །

[Block 754]
ཕུགས་སུ་འགྲོ་བ་སྒོ་ནས་འཇུག་པ་བཞིན་བསྟན་པའི་ལུང་འདི་ལ་གནས་ཏེ་ཡང་དག་པའི་འབྲས་བུ་ལེན་པར་བྱེད་པ་ཞེས་པའི་དོན་ཏོ། །

[Block 755]
དེ་ཡང་མདོ་སྡེ་འདི་ཉིད་ཀྱི་གཞུང་དང་ལུགས་སུ་བསྟན་པ༌[^754]ཡང་དག་པའི་ཡེ་ཤེས་ཀྱི་སྒོ་དབྱེ་བ་དང་། དེ་བསྟན་པ་དང་དེ་རྟོགས་པ༌[^755]དང་། དེ་ཆུད་པ་སྟེ། དེ་ཉིད་རྒྱུ་དང་འབྲས་བུར་བལྟའོ། །

[Block 756]
ཐེག་པ་རྣམ་པ་གསུམ་གྱི་གཞུང་ཐོས། ཐེག་པ་རྣམ་པ་གཅིག་གི་ཚུལ་ལ་ཞུགས་པ༌[^756]དེ་ཉིད་ཀྱི་འབྲས་བུ་ཐོབ་པ་ནི་ཆོས་ཀྱི་པདྨོ་ཞེས་པའི་དོན་ཏོ། །

[Block 757 [HEADING]]
#### མིང་དགྲོལ་བ། ^4-2-2-0

[Block 758]
འདི་མིང་བཤད་པ་ནི་དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ལ༌[^757]རྣམ་པ་གཉིས་ཏེ། ཡང་དག་པའི་ཡེ་ཤེས་དང་སྦྱོར་བའི་ཡེ་ཤེས་སོ། །

[Block 759]
ཡང་དག་པའི་ཡེ་ཤེས་ཀྱང་འདུས་བྱས་དང༌[^758]འདུས་མ་བྱས་ཀྱི་ཡེ་ཤེས་དང་གཉིས་སུ་དབྱེ་བ་ལ། འདིར༌[^759]ནི་ཟག་པ་མེད་པའི་ཡེ་ཤེས་རྩ་བ་དང་རྒྱབ་ནས་ཐོབ་པའི་ཡེ་ཤེས་གཉིས་དང་སྦྱར་རོ། །

[Block 760]
སྦྱོར་བ་ནི་ཡང་དག་པའི་ཡེ་ཤེས་ལ་སྦྱོར་ཞིང་འཇུག་པའི་ཕྱིར་ཀུན་རྫོབ་ཀྱི་ཡེ་ཤེས་ཏེ་ཐབས་ཉིད་དོ། །

[Block 761]
ཐབས་དེ་ཡང་བདག་དང་གཞན་གྱི་དོན་སྒྲུབ་པ་ལ་སྦྱོར་བ། སྒྲུབ་པ་ལ་མཁས་པ་དེ་ཐབས་ཞེས་གདགས་སོ། །

[Block 762]
དེ་ཡང་འོག་མ་འདྲེས་པ་དང་། བླ་མ་ལ་སྦྱར་བའོ། །

[Block 763]
ཇི་ལྟར་མདོ་ལས་སྣོད་མི་གཙང་བ་འཛིན་ཅིང་གོས་མི་གཙང་བ་གྱོན་པས་མངོན་པར་བྱང་ཆུབ་པ་ནི་ལུས་ཀྱི་ཐབས་སོ། །

[Block 764]
བདེན་པ་བཞི་ལ་སོགས་པ་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་དང་། ཐེག་པ་ཆེན་པོ་ལ་འཇུག་པའི་མདོ་སྟོན་པ་ནི། ངག་གི་ཐབས་མཁས་པའོ། །

[Block 765]
སྔོན་གྱི༌[^760]དེ་བཞིན་གཤེགས་པས་མཛད་པ་དང་འདྲ་བར་ཐབས་མཁས་པ་རྣམ་པ་སྣ་ཚོགས་དགོངས་པ་ནི་ཡིད་ཀྱི་ཐབས་མཁས་པའོ། །

[Block 766]
ཡང་ན་འདྲེན་པའི་ཐབས་མཁས་པ་སྟེ་ཕྱི་རོལ་གྱི་དྲུག་སྤྱོད་པའོ། །

[Block 767]
བསྔོ་བ་ལ་ཐབས་མཁས་པ་སྟེ་ནང་དུ་དྲུག་སྤྱོད་པའོ། །

[Block 768 [HEADING]]
#### རང་བཞིན་བསྟན་པ། ^4-2-3-0

[Block 769]
འདི་རང་བཞིན་ནི་ཤེས་རབ་ཀྱི་རང་བཞིན་ཏེ། རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་སོ། །

[Block 770]
ཡང་ན་ཕྱིས་ཐོབ་པའི་ཡེ་ཤེས་ཏེ་གཞན་ལ་ཕན་འདོགས་པའི་ཕྱིར་སྤྱོད་པ་དམ་པ་དང་ལྡན་པའི་ཕྱིར་ཞེས་ཀྱང་འཆད་དོ། །

[Block 771 [HEADING]]
#### དམ་པའི་ཆོས་ཀྱི་དོན་དེ་བཞིན་གཤེགས་པ་ཉག་གཅིག་གིས་མཁྱེན་པ། ^4-2-4-0

[Block 772 [HEADING]]
##### ཚིག་རྐྱང་པས་རྒྱས་པར་བཤད་པ། ^4-2-4-1-0

[Block 773]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་དགོངས་པ་དང་ལྡན་ཞིང༌[^761]ཞེས་པ་ནས་རང་སངས་རྒྱས་ཐམས་ཅད་ཀྱིས༌[^762]ཤེས་པར་དཀའོ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིག་རྐྱང་པས་རྒྱས་པར་བཤད་པ་དང་། ཚིགས་སུ་བཅད་པས་བསྡུས་ཏེ་བསྟན་པའི་དོན་ནི་དམ་པའི་ཆོས་ཀྱི་དོན་ཆུད་པར་བྱ་བ་དེ་བཞིན་གཤེགས་པ་ཉག་གཅིག་གིས་མཁྱེན་པ་དེ་སྟོན་ཏེ། བཅོམ་ལྡན་འདས་དགོངས་པ་དང་མཁྱེན་བཞིན་དུ་ལྡན་ཞེས་པ་ནི་ཡང་དག་པའི༌[^763]ཡེ་ཤེས་ཀྱིས་གཟིགས་ཤིང་ཏིང་ངེ་འཛིན་ལས་བཞེངས་པའོ། །

[Block 774]
ཏིང་ངེ་འཛིན་དེ་ལས༌[^764]བཞེངས་པ་ཡང་ཆོས་ལ་མངའ་བརྙེས་པའི་དོན་དང་། བཅོམ་ལྡན་འདས་ཏིང་ངེ་འཛིན་དུ་བཞུགས་པ་ལ་གཞན་གྱིས་བཞེངས་པར་བསྐུལ་མི་ནུས་ཀྱི་བཅོམ་ལྡན་འདས་ཉིད་དེ་ལས་བཞེངས་ཤིང་འབྱུང་བ་དང་འཇུག་པ་ལ་མངའ་བརྙེས་པ་སྟོན་ཏོ། །

[Block 775]
དེ་ལས་བཞེངས་ནས་ཡང་དག་པའི་དོན་དེ་བཞིན༌[^765]ལ་བཀའ་མི་སྩོལ་གྱི། [^766]ཤཱ་རིའི་བུ་ཞེས་བོས་ཏེ་བཀའ་སྩལ་པ་ནི་ཤེས་རབ་མཆོག་ཏུ་རྣོ་བས་ཆོས་དམ་པའི་མཆོག༌[^767]སྣོད་དུ་འགྱུར་བ་དང་འཕགས་པ་ཉན་ཐོས་པ༌[^768]རྣམས་གཟེངས་བསྟོད་ཅིང་དམ་པའི་ཆོས་འདི་འཕགས་པ༌[^769]ཉན་ཐོས་པ༌[^770]རྣམས་ཀྱི་ཆེད་དུ་གསུངས་པ་དང་ཉན་ཐོས་པ༌[^771]རྣམས་བྱང་ཆུབ་ཆེན་པོ་ལ་གཞོལ་ཞིང་འབྲས་བུ་བླ་ན་མེད་པ་ལ་གཟུད་པ༌[^772]དང་འཕགས་པ་ཉན་ཐོས་པ༌[^773]རྣམས་སྙིང་རྗེ་ཞན་པ་ཡིན་པས་བྱང་ཆུབ་སེམས་དཔའ་ལ་བཀའ་སྩལ་ནས༌[^774]ཆོས་འདི་ལ་ཉན་ཐོས་པ༌[^775]རྣམས་སྐལ་བ༌[^776]མེད་པ་དང་དོན་དུ་མ་བཤད་ཅེས་འཇུག་ཏུ་མི་བཏུབ་པའི་ཕྱིར་ཤཱ་རིའི་བུ་ལ་བཀའ་སྩལ་ནས༌[^777]འཕགས་པ་ཉན་ཐོས་པ་གཞན་ཡང་མདོ་འདི་ལ་འཇུག་པར་སེམས་བསྐྱེད་པ༌[^778]དང་བལྟ་བ་དང་། རྟོགས་པར༌[^779]དཀའ་བ་ནི་ཡེ་ཤེས་དང་ཡེ་ཤེས་ཀྱི་སྒོའོ། །
--- END BLOCKS ---
