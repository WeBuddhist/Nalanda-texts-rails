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
[Block 946]
ཤི་བ་ཙམ་ཉིད་དང་ནི་རྣམ་པར་བྲལ་བ་ཉིད་ཆོས་མཐུན་པ་ཉིད་དུ་འདོད་དོ། །

[Block 947]
ཕུན་སུམ་ཚོགས་པ་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའོ། །

[Block 948]
ཐེ་ཚོམ་ཐམས་ཅད་ཐེ་ཚོམ་མེད་པར་གཟུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་མི༌[^644]གང་ཐེག་པ་ཆེན་པོའི་ཆོས་ཀྱི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ལ་བརྩམས་ནས་ངོ་བོ་ཉིད་གསུམ་སྟོན་པ་སྟེ། འདི་ལྟ་སྟེ། ཆོས་ཐམས་ཅད༌[^645]ངོ་བོ་ཉིད་མེད་པ། མ་སྐྱེས་པ། མ་འགགས་པ། གདོད་མ༌[^646]ནས་ཞི་བའོ། །

[Block 949]
ཆོས་ཐམས་ཅད་ནི་རང་བཞིན་གྱིས་མྱ་ངན་ལས་འདས་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་མེད་པའི་རྣམ༌[^647]གྲངས་ཀྱིས་ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་ཉེ་བར་གཟུང་བར༌[^648]བྱའོ། །

[Block 950]
སྒྱུ་མ་དང་། སྨིག་རྒྱུ་དང་། རྨི་ལམ་དང་། མིག་ཡོར་དང་། གཟུགས་བརྙན་དང་། ཆུ་ཟླ་དང་། སྤྲུལ་པ་བསྟན་པས་ནི་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉེ་བར་གཟུང་བར༌[^649]བྱའོ། །

[Block 951]
དེ་བཞིན་ཉིད་དང་། ཡང་དག་པའི་མཐའ་དང་། མཚན་མ་མེད་པ་དང་། དོན་དམ་པ་དང་། ཆོས་ཀྱི༌[^650]དབྱིངས་དང་། སྟོང་པ་ཉིད་ལ་སོགས་པའི་རྣམ་གྲངས་བསྟན་པས་ནི་ཡོངས་སུ་གྲུབ་པའི་ངོ་བོ་ཉིད་ཉེ་བར་གཟུང་བ༌[^651]ཉིད་དེ། འདི་ལ་བློ་གྲོས་ངན་པ་ཐམས་ཅད་ཀྱི་སོམ་ཉི་འཇུག་པར་མི་འགྱུར་རོ། །

[Block 952]
ཐོས་པ་དང་བསམ་པའི༌[^652]ཆོས་ལ་ངར་འཛིན་པ་དང་ང་ཡིར་འཛིན་པའི་མངོན་པར་ཞེན་པ་ཡོངས་སུ་སྤོང་བ་ཞེས་བྱ་བ་ནི་ཆོས་ལ་མངོན་པར་ཞེན་པ་ཙམ་སྤོང་བར་བཞེད་པའོ། །

[Block 953]
རྣམ་པར་རྟོག་པ་སྤངས་པས་མདུན་ན་གནས་པ་དང་བཞག་པའི་མཚན་མ་ཐམས་ཅད་ཡིད་ལ་མི་བྱེད་ཅིང་རྣམ་པར་མི་རྟོག་པ་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་ལས་བྱུང་བའི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ལ་གནས་པའི་དགེ་བའི་རྩ་བའི་སྟོབས་ལས་བྱུང་བའི་སེམས་སྦྱོང་བ་རྣམ་པ་གསུམ་ལ་བརྟེན༌[^653]ནས་འདི་ལྟར་རྟག་ཏུ་གུས་པ་དང་བཅས་པས་བག་ཡོད་པར་འབྱུང་བའི༌[^654]ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པའི་གནས་སྐབས་ལ་གནས་པ་ཐམས་ཅད་དུ་མཉམ་པར་གཞག་པའི་སེམས་རྗེས་སུ་མཐུན་པའི་བཟོད་པ་རྣོན་པོ་ལ་གནས་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 954]
ལྟན་ཅིག་ཏུ་སྣ་ཚོགས་ཀྱི་རྣམ་པའི་དོན་སྣང་བ་འབྱུང་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་མིང་དང་ཚིག་དང་ཡི་གེའི་ཚོགས་སྣ་ཚོགས་ཀྱི་རྣམ་པ་སྣང་བ་འབྱུང་བའི་ཕྱིར་དང་། དེ་ལ་བརྟེན་པའི་དོན་སྣ་ཚོགས་ཀྱི་རྣམ་པ་སྣང་བ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 955]
ཚིགས་སུ་བཅད་པ་ནི།

[Block 956 [VERSE]]
ཆོས་དང་གང་ཟག་ཆོས་དང་དོན། །
བསྡུས་པ་དང་ནི་རྒྱས་དང་རིགས། །
མ་དག་པ་དང་དག་དང་མཐའ། །
རབ་ཏུ་དབྱེ་བས་མིང་གི་ཡུལ། །

[Block 957]
མདོར་བསྡུ༌[^655]ན་བྱང་ཆུབ་སེམས་དཔའི་མིང་ལ་དམིགས་པ་ནི་རྣམ་པ་བཅུ་སྟེ། འདི་ལྟ་སྟེ་ཆོས་ཀྱི་མིང་ནི་མིག་ལ་སོགས་པའོ། །

[Block 958]
གང་ཟག་གི་མིང་ནི་བདག་དང་སེམས་ཅན་ལ་སོགས་པའོ། །

[Block 959]
ཆོས༌[^656]ནི་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་སུ་གཏོགས་པའོ། །

[Block 960]
དོན་ནི་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་པོ་དེའི་དོན་གང་ཡིན་པའོ། །

[Block 961]
མིང་བསྡུས་པ་ནི་ཆོས་ཐམས་ཅད་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 962]
མིང་རྒྱས་པ་ནི་གཟུགས་དང་། ཚོར་བ་ལ་སོགས་པ་དང་ནམ་མཁའ་ལ་སོགས་པའོ། །

[Block 963]
རིགས་ཀྱི་མིང་ནི་དང་པོ་ཡི་གེ་ཨ་ནས༌[^657]ཧའི་མཐར་ཐུག་པའི་བར་རོ། །

[Block 964]
མ་དག་པའི་མིང་ནི་དོན་དང་བཅས་པའི་སོ་སོའི་སྐྱེ་བོའོ། །

[Block 965]
དག་པའི་མིང་ནི་བདེན་པ་མཐོང་བ་རྣམས་ཀྱིའོ། །

[Block 966]
མཐར་ཐུག་པའི་མིང་ནི་གང་མ་འདྲེས་པའི་ཆོས་ལ་དམིགས་པའི་འཇིག་རྟེན་ལས་འདས་པ་དང་། དེའི་རྗེས་ལས་ཐོབ་པའི་ཡེ་ཤེས་གཉིས་ཀྱི༌[^658]དམིགས་པའོ། །

[Block 967]
དེ་བཞིན་གཤེགས་པའི་རིགས་སུ་སྐྱེས་པ་ཡིན། །ཞེས་བྱ་བ་ནི་རྣམ་པ་སྣ་ཚོགས་ཀྱི་ཆོས་ཐམས་ཅད་ལ་བརྟེན་ནས་སོ། །

[Block 968]
སེམས་ཅན་ཐམས་ཅད་ལ་སེམས་མཉམ་པ་ཉིད་ནི་བདག་དང་གཞན་མཉམ་པ་ཉིད་དུ་རྟོགས་པས་བདག་ལ་ཇི་ལྟ་བ་བཞིན་དུ་དེ་དག་ལ༌[^659]ཡང་སྡུག་བསྔལ་ཟད་པར་འདོད་པའོ། །

[Block 969]
བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་དང་སེམས་མཉམ་པ་ཉིད་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་དང་སྦྱོར་བའི་བསམ་པ་མཉམ་པའོ། །

[Block 970]
སངས་རྒྱས་ཐམས་ཅད་དང་སེམས་མཉམ་པ་ཐོབ་པ་ནི་དེ་དག་དང་ཆོས་ཀྱི་དབྱིངས་ཀྱི་བདག་ཉིད་ཐ་མི་དད་པར་མཐོང་བའོ། །

[Block 971]
ཡོངས་སུ་ཚོལ་བ་ནི༌[^660]བཞི་པོ་དག་གི་བསྲབས་པས༌[^661]དོན་མེད་པར་བཟོད་པ་ཆུང་ངུའི་ཚེ་སྣང་བ་ཐོབ་པའི་ཏིང་ངེ་འཛིན་ཞེས་བྱ་བ་ལ། བསྲབས་པ་ནི་དོན་མེད་པར་འདོད་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། དོན་མེད་པར་ཤེས་པ་ནི་སྣང་བ་ཐོབ་པ་ཞེས་བྱ་བའི་སྒྲས་བསྟན་ཏོ། །

[Block 972]
སྣང་བ་ཐོབ་པའི་ཏིང་ངེ་འཛིན་ཞེས་བྱ་བ་ནི་དོན་མེད་པ་ལ་ཡང་དག་པར་བརྟེན་པའི་ཏིང་ངེ་འཛིན་གྱིས་མཐོང་བའོ། །

[Block 973]
དོན་མེད་པར་བཟོད་པ་ཆེན་པོའི་ཚེ་ཞེས་བྱ་བ་ལ། དེ་ལ་བཟོད་པ་ནི་འདོད་པ་སྟེ། མངོན་པར་འདོད་པའོ། །

[Block 974]
སྣང་བ་མཆེད་པའི་ཏིང་ངེ་འཛིན་ཞེས་བྱ་བ་ནི། དོན་མེད་པར་ཤེས་པ་ཆེན་པོ་ནི་སྣང་བ་མཆེད་པ་ཞེས་བྱ་བའི༌[^662]སྒྲས་བསྟན་ཏོ། །

[Block 975]
ཏིང་ངེ་འཛིན་ཞེས་བྱ་བའི་སྒྲས་ནི་དོན་མེད་པར་ཤེས་པ་དེ་ལ་ཡང་དག་པར་བརྟེན་པ་དེ་བསྟན་ཏོ། །

[Block 976]
དེ་ཁོ་ན་ཉིད་ཀྱི་དོན་གྱི་ཕྱོགས་གཅིག་ལ་ཞུགས་པའི་ཏིང་ངེ་འཛིན་ཞེས་བྱ་བ་ནི་དོན་མེད་པར་ངེས་པར༌[^663]བསྟན་ཏེ། ཏིང་ངེ་འཛིན་གྱི་སྒྲས་ནི་དོན་མེད་པར་ངེས་པར་ཤེས་པ་དེ་ལ་ཡང་དག་པར་བརྟེན་པ་དེ་ནི་ཏིང་ངེ་འཛིན་ཞེས་བསྟན་ཏོ། །

[Block 977]
བདེན་པའི་རྗེས་སུ་མཐུན་པའི་བཟོད་པའི་གནས་ཞེས་བྱ་བ་ལ། ཆོས་བདག་མེད་པ་ནི་བདེན་པ་ཞེས་བྱའོ། །

[Block 978]
དེའི་རྗེས་སུ་མཐུན་པ་གང་ཡིན་པའི་བཟོད་པ་ནི་བདེན་པའི་རྗེས་སུ་མཐུན་པའི་བཟོད་པའོ། །ཇི་ལྟར་བྱས་པས་ཤེ་ན། གཟུང་བར༌[^664]བྱ་བ་མེད་ན་ངེས་པ་ཁོ་ནར་འཛིན་པ་ཡང་མེད་དོ་ཞེས་མོས་པར་འགྱུར་བས་སོ། །

[Block 979 [HEADING]]
### ཤེས་བྱའི་མཚན་ཉིད་ལ་འཇུག་པ་ཞེས་བྱ་བའི་དོན་གཞན། ^3-2-0

[Block 980 [HEADING]]
#### མང་དུ་ཐོས་པས་བསྒོས་པའི་གནས། ^3-2-1-0

[Block 981]
ཤེས་བྱའི་མཚན་ཉིད་ལ་འཇུག་པ་ཞེས་བྱ་བའི་དོན༌[^665]གཞན་ཡང་། མང་དུ་ཐོས་པས་བསྒོས་པའི་གནས། །ཞེས་བྱ་བ་སྟེ། ཐེག་པ་ཆེན་པོ་ཡོངས་སུ་བསྒོམ་པའི༌[^666]བདག་ཉིད་ཀྱི་ངོ་བོའོ།[^667] །ཀུན་གཞི་རྣམ་པར་ཤེས་པས་བསྡུས་པ༌[^668]མ་ཡིན་ལ་ཞེས་བྱ་བ་དང་། ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ལྟར་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པས་བསྡུས་པའི་ས་བོན་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་ཀུན་ནས་ཉོན་མོངས་པའི་ཆོས་རྣམས་ཀྱི་རྒྱུ་ཡིན་པ་དེ་བཞིན་དུ་དེ་རྣམ་པར་བྱང་བའི་ཆོས་རྣམས་ཀྱི༌[^669]རྒྱུར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ།[^670] །

[Block 982]
ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པས་བསྡུས་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ལྟ་བ་དང་བཅས་པའི་ཡིད་ཀྱིས་བརྗོད་པ་རྣམས་ཀྱི་ཡང་སྟེ། ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་ལས་ཆོས་དང་དོན་གྱི་རྣམ་པ་འབྱུང་བར་འགྱུར་བའི༌[^671]རྒྱུ་ཡིན་ནོ། །

[Block 983]
ཚུལ་ཅན་བཟུང་བའི༌[^672]དངོས་པོ་ལྟ་བུ་ཞེས་བྱ་བ་ནི་གཟུགས་སུ་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 984]
ལྟ་བ་དང་བཅས་པའི༌[^673]ཞེས་བྱ་བ་ནི་ལྟ་བར་གྱུར་པ་རྣམས་སོ། །

[Block 985]
དེ་དག་ཉིད་ནི་རྒྱུ་མཚན་དང་ལྟ་བ་དང་བཅས་པའི་རྣམ་པར་ཤེས་པར༌[^674]རྣམ་པར་འཇོག་པར་འགྱུར་རོ། །
--- END BLOCKS ---
