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
[Block 5881]
མཐོང་བའི་ཆོས་ལ་ཕན་འདོགས་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཕོངས་པ་ལས་བཟློག་པའི༌[^3765]ཕན་འདོགས་པ་དང་།

[Block 5882 [VERSE]]
ཕན་ཡོན་སྐྱེད་པར་བྱེད་པའི་ཕན་འདོགས་པའོ། །
ཕོངས་པར་གྱུར་ཀྱང་མི་འགྱུར་མཛའ་བོ་ཡིན། །

[Block 5883]
ཞེས་བྱ་བ་ནི། བཅིང་པ་ལ་སོགས་པའི་ཕོངས་པ་སེལ་བའི་ཕྱིར་རོ། །

[Block 5884]
སེམས་ཀྱི་ནད་མྱ་ངན་གྱི་མཚན་ཉིད་ལ་ཐོས་པ་ནི་སྨན་ཡིན་ཏེ། མྱ་ངན་སེལ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 5885]
ཐོས་པ་ནི་དཔུང་ཡིན་ཏེ་སོ་སོར་བརྟགས་ཏེ་ཡང་དག་པར་བླངས་ནས་འདོད་ཆགས་ལ་སོགས་པ་ཉེས་པ་རྣམས་ཀྱི་དཔུང་འཇིག་པར་བྱེད་པའི་རྒྱུར་གྱུར་པ་སྟེ། དེ་ཡང་འདོད་ཆགས་ལ་སོགས་པའི་ཉེས་པ་སོ་སོར་བརྟགས༌[^3766]པའི་སྟོབས་ཀྱི༌[^3767]ཟིལ་གྱིས་མནན་པ་ཡིན་པའི་ཕྱིར་ཉེས་པ་འཇོམས་པས་དཔུང་གི་མཆོག་གོ། །

[Block 5886]
ཐོས་པ་ནི་གྲགས་པ་དང་དཔལ་གྱི་གཏེར་གྱི་མཆོག་ཀྱང་ཡིན་ཏེ། ཐོས་པ་ལ་ཉེ་བར་གནས་པས་ན་མི་བཟད་པའི་གྲགས་པ་དང་དཔལ་ཐོབ་པ་ཡིན་ནོ། །

[Block 5887]
ད་ནི་ཐོས་པ་སྨྲ་བར་བྱེད་པ་རྣམས་ཀྱི་ཕན་གདགས་པ་ཆེན་པོ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། ཡ་རབས་རྣམས་དང་ཕྲད་ན༌[^3768]སྐྱེས་ཀྱི་མཆོག །ཅེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5888]
དེ་ལ་སྨྲ་བ་རྣམས་ལ་ཐོས་པ༌[^3769]ཕན་འདོགས་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། ཡ་རབས་རྣམས་དང་ཕྲད་ན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་བཞི་སྨོས་སོ། །

[Block 5889]
དེ་ལ་ཚིག་བཟང་པོར་གྱུར་པ་ནི་རྣམ་པ་བཞི་སྟེ། རང་གི་ཕྱོགས་གནས་པར་བྱེད་པ་ཉིད་དུ་སྨྲ་བའི་ཚིག་ལ་མཁས་པར་འགྱུར་བ་དང་། ལེགས་པར་བཤད་པའི་སྙན་དངགས༌[^3770]བྱེད་པའི་ཚིག་ལ་མཁས་པར་འགྱུར་བ་དང་། ཆོས་སྟོན་པའི་ཚིག་ལ་མཁས་པར་འགྱུར་བ་དང་། བསྟན་བཅོས་ཀྱི་རིམ་པ་བཞིན་དུ་ཤེས་པ་སྟེ། ཚིགས་བཅད་བཞི་དང་གོ་རིམས་བཞིན་དུ་སྦྱར་རོ། །

[Block 5890]
ཡ་རབས་རྣམས་དང་ཕྲད་ན༌[^3771]ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་རང་གི་ཕྱོགས་གནས་པར་བྱེད་པ་སྨྲ་བའི་ཚིག་ལ་མཁས་པར་གྱུར་པའི་དབང་དུ་བྱས་པ་སྟེ། གང་གི་ཕྱིར་དེའི་ཚིག་ནི་ཡ་རབས་རྣམས་དང་ཕྲད་ན་སྐྱེས་བཞིན་དུ་འགྱུར་ཏེ། ཡན་ལག་སྐྱོན་མེད་པ་དེས་འདོད་པའི་དོན་སྒྲུབ་ནུས་པའི་ཕྱིར་རོ། །

[Block 5891]
ཚོགས་ཀྱི་ནང་ན་མཁས་པ་དགའ་བར་འགྱུར། །ཞེས་བྱ་བ་ནི་བརྗོད་པ་དང་བརྗོད་པར་བྱ་བའི་དོན་རིགས་པར་ལྡན་པ་དེས་སོ། །

[Block 5892]
ཕས་ཀྱི་རྒོལ་བ་ཉིད་འོད་ཡིན་པས་ཕས་ཀྱི་རྒོལ་བ་འོད་དོ། །

[Block 5893]
དེ་རྣམས་ཀྱི་ཇི་ལྟར་ཉི་མ་ལྟ་བུ་ཡིན་ཏེ། ཉི་མས་ནི་ཟླ་བ་ལ་སོགས་པའི་འོད་ཟེར་ཟིལ་གྱིས་གནོན་པ་བཞིན་དུ་རང་གི་ཕྱོགས་གནས་པར་བྱེད་པའི་ཚིག་ལ་མཁས་པ་ཡིན་ཏེ། རང་གི་ཕྱོགས་གནས༌[^3772]པ་ཉིད་ཀྱིས་ཕས་ཀྱི༌[^3773]རྒོལ་བའི་འོད་ཟིལ་གྱིས་མནན་པར༌[^3774]འགྱུར་རོ། །

[Block 5894]
འགྲན་པ་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི་གང་དག་དེ་ལ་འགྲན་ཞིང་རྒོལ་བར་འདོད་པའོ། །

[Block 5895]
དེ་རྣམས་ཀྱི་གྲགས་པ་དང་། དྲེགས་པ༌[^3775]སེལ་བ་ཡིན་ཏེ། འགྲན་པ་རྣམས་ཀྱིས་འདོད་པའི་དོན་སྒྲུབ་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 5896]
མིག་དང་བཞིན་མདངས་རབ་ཏུ་གསལ་གྱུར་ཅིང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་ལེགས་པར་བཤད་པའི་ཚིག༌[^3776]ལ་མཁས་པར་འགྱུར་བའི་དབང་དུ་བྱས་པ་སྟེ། མིག་དང་བཞིན་ནི་མིག་དང་བཞིན་ནོ། །

[Block 5897]
མདངས་དང་རབ་ཏུ་གསལ་བ་ནི་མདངས་དང་རབ་ཏུ་གསལ་བར་གྱུར་པའོ། །

[Block 5898]
མིག་དང་བཞིན་མདངས་རབ་ཏུ་གསལ་བར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་མིག་དང་བཞིན་མདངས་རབ་ཏུ་གསལ་བར་གྱུར་པའོ། །

[Block 5899]
མིག་དང་བཞིན་མདངས་རབ་ཏུ་གསལ་བ་དང་། མདངས་རབ་ཏུ་གསལ་བར་གྱུར་པ་དེས་རབ་ཏུ་དགའ་བ་ནི་རབ་ཏུ་དགའ༌[^3777]བར་གྱུར་ནས་སོ། །

[Block 5900]
ཡང་ན་མིག་དང་བཞིན་ནི་མིག་དང་བཞིན་ནོ། །

[Block 5901]
མདངས་ཉིད་རབ་ཏུ་གསལ་བ་ཡིན་པས་མདངས་རབ་ཏུ་གསལ་བ་སྟེ། མིག་དང་བཞིན་མདངས༌[^3778]ཀྱང་ཡིན་ལ་རབ་ཏུ་གསལ་བ་ཡང་ཡིན་པས་རབ་ཏུ་གསལ་བར་གྱུར་པའོ། །

[Block 5902]
ལྷག་པར་ཚིམ་པ་ཡིན་པས་ལྷག་པར་དགའ་བ་སྟེ། རབ་ཏུ་དགའ་བར་གྱུར་པའོ། །

[Block 5903]
རབ་ཏུ་དགའ་བར་གྱུར་པ་དེ་གང་ཡིན་ཞེ་ན། མིག་དང་བཞིན་མདངས་རབ་ཏུ་གསལ་བར་གྱུར་པའོ། །

[Block 5904]
མི་བཤེས་པ་ནི་མ་འདྲིས་པ་སྟེ་སྔར་མ་མཐོང་བའོ། །

[Block 5905]
ལག་པའི་སེ་གོལ་རྡོབ་པས་མགུ་བར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་ལག་པའི་སེ་གོལ་མགུ་བྱེད་རྡོབ་པའོ། །

[Block 5906]
ཆོས་བསྟན་པའི་ཚིག་ལ་མཁས་པར་འགྱུར་བའི་དབང་དུ་བྱས་ནས། གཏན་ཚིགས་དོན་རྣམས་རབ་ཏུ་གསལ་བར་སྟོན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5907]
གཏན་ཚིགས་ཀྱང་ཡིན་ལ་གསལ་བ་ཡང་ཡིན་པས་གཏན་ཚིགས་གསལ་བའོ། །

[Block 5908]
དེས་དོན་སྟོན་པ་ཞེས་བྱ་བ་ནི་གཏན་ཚིགས་རབ་ཏུ་གསལ་བས་དོན་རབ་ཏུ་སྟོན་པའོ། །

[Block 5909]
གཙུག་ལག་དང་ལུང་རྣམ་པ་སྣ་ཚོགས་པ་ནི་གཙུག་ལག་ལུང་རྣམས་སྣ་ཚོགས་སོ། །

[Block 5910]
ལུང་ནི་མན་ངག་སྟེ། གཙུག་ལག་དང་། ལུང་སྣ་ཚོགས་སྟོན་པ་དང་མཐུན་པའོ། །

[Block 5911]
[^3779]དེ་ལྟར་རེ་ཞིག་ཆོས་སྟོན་པས་དོན་ཕུན་སུམ་ཚོགས་པ་བསྟན༌[^3780]ཏོ། །

[Block 5912]
མཉེན་ཞིང་སྦྱངས་པས་ཡིད་དུ་འོང་བའི་ཕྱིར། །ཞེས་བྱ་བ་ལ། མཉེན་པ་ནི་སྒྲ་སྙན་པའོ། །

[Block 5913]
སྦྱངས་པ་ནི་སྒྲའི་མཚན་ཉིད་དང་ལྡན་པ་སྟེ། སྒྲ་སྙན་པ་དང་།[^3781] ལེགས་པར་སྦྱར་བ་གཉིས་ཀྱིས་ཡིད་དུ་འོང་བ་ནི་མཉེན་ཞིང་སྦྱངས་པ་ཡིད་དུ་འོང་བ་ཉིད་དོ། །

[Block 5914]
དེ་བས་ན་འདིས་ནི་བརྗོད་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 5915]
མེ་ཏོག་ཕྲེང་བ་མ་རྙིས་བཀྲམ་པ་བཞིན། །ཞེས་བྱ་བ་ནི་མེ་ཏོག་མ་རྙིས་ཕུང་པོ་བཞིན་ནོ། །

[Block 5916]
བསྟན་བཅོས་ཀྱི་རིམ་པ་བཞིན་དུ་ཚིག་ལ་མཁས་པར་གྱུར་པའི་དབང་དུ་བྱས་ནས། དུལ་ཞིང་རབ་ཏུ་གསལ་བའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5917]
དུལ་བ་དང་རབ་ཏུ་གསལ་བ་ནི་དུལ་ཞིང་རབ་ཏུ་གསལ་བའོ། །

[Block 5918]
དུལ་ཞིང་རབ་ཏུ་གསལ་བ་དེས་སྤོབས་པ་ནི་དུལ་ཞིང་རབ་ཏུ་གསལ་བའི་སྤོབས་པའོ། །

[Block 5919]
དེ་གཉིས་འབར་བ་དེ་ནི་དུལ་ཞིང་རབ་ཏུ་གསལ་བའི་སྤོབས་པ་སྐྱེ་བའོ། །

[Block 5920]
དུལ་བ་ནི་ཉོན་མོངས་པ་མེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
