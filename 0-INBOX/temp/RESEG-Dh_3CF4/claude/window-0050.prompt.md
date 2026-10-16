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
[Block 1751]
ཁྱེད་ཀྱི་གནོད་པ་བདག་གིས་ག་ལ་བཟོད། །[^1010]ཅེས་བྱ་བ་ནི་འདི་ལྟར་བྱམས་ཤིང་ཡིད་གཅུགས༌[^1011]པའི་དངོས་པོ་དག་ལ་སྟེ། །དེས་ན་ཁྱེད་ལ་ཡང་གནོད་པ་བཏང་སྙོམས་སུ་བྱ་ཞིང་། གང་འདི་དག་ཁྱེད་ལ་སློང་ན་དེ་ལ་སྦྱིན་པའི་རྗེས་སུ་ཡི༌[^1012]རང་བར་བྱས་ཏེ། འདི་ལྟར་ངའི་སྦྱིན་པ་ལ་ཁྱེད་ཅག་གིས་རྗེས་སུ་ཡི་རང་བ་དེ་ལྟར་བྱའོ།[^1013] །ཇི་ལྟར་འོག་ནས་བརྗོད་པ་ཞེས་བྱ་བ་ནི་མདུན་ནས་སོ། །

[Block 1752]
དེ་ལྟར་རེ་ཞིག་སྦྱིན་པའི་བྱ་བ་རིགས་པ་ཉིད་དུ་བསྟན་ནས། སྔར་བཤད་པའི་དབྱེ་བས་དབྱེ་བ་བསྟན་པའི་ཕྱིར། དེ་བས་ན་ང་ལ༌[^1014]རབ་ཏུ་བྱམས་པའི༌[^1015]ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 1753]
ཆོས་ཀྱི་བགེགས་ལ་འཛེམ་པ་མེད་པ་ཞེས་བྱ་བས་ནི་དེ༌[^1016]དག་ཆོས་མ་ཡིན་པ་ཉིད་དུ་བསྟན་པས་འཛེམ་པ་བསྐྱེད་པའི༌[^1017]མཚན་ཉིད་ཀྱི་དབྱེ་བ་བསྟན་ཏོ། །

[Block 1754]
ཇི་ལྟར་དབྱེ་བ་དེ་ཡང་ཆོས་མ་ཡིན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1755]
ད་ནི་ལོག་པ་ཉིད་དུ་བསྟན་པར་འདོད་པས། ངའི་དོན་དུ་ཁྱོད་ཅི་སྤྱོད་པ་འདི་ལྟ་བུ་བྱ་བ་མི་རིགས་ཏེ་ཞེས་བྱ་བ་འདི་བརྩམས་སོ། །

[Block 1756]
ངེད་ཅག་གི་དོན་ནི་ངའི་དོན་ཏེ་ངེད་ཅག་གི་དོན་དུའོ། །

[Block 1757]
ཁྱེད་ཅག་གིས༌[^1018]ནམ་ཡང་ངའི་དོན་དུ་སྦྱིན་པའི་བགེགས་ནི་བྱ་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1758]
བདག་གི་དོན་དུ་བཟའ་བ་ལ་སོགས་པ་ཞེས་བྱ་བ་ལ༌[^1019]བདག་ཉིད་ཀྱི་ཡིན་པས་བདག་སྟེ། མངོན་པར་མཐོ་བ་དང་ངེས་པར་ལེགས་པ་འཐོབ་པའི་ཕྱིར་རོ། །

[Block 1759]
ཕྱི་རོལ་གྱི་དངོས་པོ་ནི་བཟའ་བ་དང་བཏུང་བ་ལ་སོགས་པའོ། །

[Block 1760]
སོགས་པ་སྨོས་པས་ནི་སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པ་ཉིད་དོ། །

[Block 1761]
དེ་ལྟར་བྱེད་པ་ཅི་འདྲར་འགྱུར། །ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་དུ་ནང་གི་སྦྱིན་པ་ནི་སྔོན་གང་གིས་མ་སྦྱིན༌[^1020]ཏེ་བྱང་ཆུབ་སེམས་དཔའ༌[^1021]དག་གིས་སོ། །

[Block 1762]
ལེགས་སམ་ག་ལ་ཏེ་མ་ལེགས་ཀྱང་། །ཞེས་བྱ་བ་ནི། ཇི་ལྟར་ལེགས་པ་ཉིད་མ་ཡིན་ནོ། །ཞེས་བརྗོད་པར་བྱ་སྟེ། འདིས་ཀྱང་ཆོས་མ་ཡིན་པ་དང་བདེན་པ་མ་ཡིན་པ་ཉིད་བསྟན་ཏེ་སྦྱིན་པའི་གེགས༌[^1022]སོ། །

[Block 1763]
དེ་ཞེས་བྱ་བ་ནི་ནང་གི་དངོས་པོ་གཏོང་བ་འགོག་པར་བྱེད་པ་སྟེ། འདི་ལྟར་ལེགས་པ་མ་ཡིན་པར་འགྱུར་ཞིང་ཆོས་མ་ཡིན་པ་དང་ལྡན་པ་སྟེ། ཁྱེད་ཅག་ནམ་ཡང་དེ་ལྟ་བུ་མ་བྱེད་ཅིག་པའོ། །

[Block 1764]
ནང་གི་དངོས་པོ་གཏོང་བའི་དགག་པ་གང་ཡིན་པ་དེ་ནི་ལེགས་པ་མ་ཡིན་ལ། དགག་པ་མ་ཡིན་པ་དེ་ནི་ལེགས་པ་ཉིད་དོ། །

[Block 1765]
ཁྱེད་ཀྱི་ནི་སྲོག་གཅོད་པ་ལ་རྗེས་སུ་ཡི་རང་བར་བྱའོ་ཞེས་བྱ་བ་ལྟ་བུ་ཡིན་ཏེ། དེས་ན་ངའི་རྗེས་སུ་འགྲོ་བར་བྱ་བ་ནི༌[^1023]རིགས་པས་དཔྱད་པར་བྱའོ་ཞེས་བྱ་བ་འདི་བརྩམས་སོ། །

[Block 1766]
ངའི་གྲོགས་རྗེས་སུ་མཐུན་པ་ཞེས་བྱ་བ་བསྟན་པ་ལ། གྲོགས་ཀྱི་ངོ་བོ་ནི་གོགས༌[^1024]ཏེ་བཀའ་ལ་གཏོགས་ཏེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1767]
ངེད་ཅག་བྱང་ཆུབ་སེམས་དཔའི་གྲོགས་དེ་དང་མཐུན་པ་ནི་ངའི་གྲོགས་མཐུན་པ་སྟེ། འདི༌[^1025]ནི་གཞན་མི་མཐུན་པའི་ཞེས་བསྟན་པའི་ཚུལ་དུ་འགྱུར་ཏེ། དེ་གང་ཡིན་ཞེ་ན། ལམ་ལོག་པར་འགྲོ་བ་ལས་བཟློག་པའི་སྟེ། ལམ་ལོག་པ་ལས་བཟློག་པ་ཡིན་པས་ལོག་པར་འགྲོ་བ་དེ་ལས་བཟློག་པའོ། །

[Block 1768]
དེ་གང་ཞེན་ཡིད་དོ། །

[Block 1769]
རིགས་པས་དཔྱད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་ལ་ལ་སེམས་ཅན་རྣམས་ཀྱི་དོན་དུ་བདག་ཉིད་ཡོངས་སུ་གཏོང་བར་བྱེད་པ་སྟེ། གཞན་གང་ཞིག་རྗེས་སུ་ཡི་རང་བར་མི་བྱེད་པ་དེ་ནི་རྗེས་སུ་ཡི་རང་བ་སྲོག་གཅོད་པའི་ཁ་ན་མ་ཐོ་བ་དང་ལྡན་པར་འགྱུར་རོ་ཞེས་འདིར་ཡང་ཁ་ཅིག་ཞུགས་པར་འགྱུར་ཞེས་འདིར་ཡང་ཁ་ཅིག་ཞུགས་པའོ། །ཅི་སྟེ་རིགས་སམ་མི་རིགས་ཤེ་ན། སྐྱེས་པའི་རབས་ཐོས་པས་ཀྱང་བསོད་ནམས་མེད་པར་འགྱུར་ཏེ། དེ་ན་ནི་བྱང་ཆུབ་སེམས་དཔའ༌[^1026]ནང་གི་དངོས་པོ་ཡོངས་སུ་གཏོང་བ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1770]
དེ་ལ་རྗེས་སུ་ཡི་རང་བར་བྱེད་པ་དང་། རྗེས་སུ་ཡི་རང་བ་ཡང་བསོད་ནམས་མ་ཡིན་པར་འགྱུར་ཏེ། གལ་ཏེ་འདས་མ་ཐག་པ་དེ་ལྟར་རིགས་པས་དཔྱད་པར་བྱས་པ་དེ་བས་ན་བསོད་ནམས་མ་ཡིན་པ་གང་ཡིན་བ་དེ་ཉིད་ལོག་པའི་ལམ་དེ་ལས་བཟློག་པར་བྱས་པ་དེ་ལ་རྗེས་སུ་ཡི་རང་བ་དང་མཐུན་པའི་ཚིག་གང་ཡིན་པ་དེ་ནི་རྗེས་སུ་ཡི་རང་བ་དང་མཐུན་པའི་ཚིག་གོ། །

[Block 1771]
བཟང་ངོ་ཞེས་བྱ་བ་ཉིད༌[^1027]ནི་བཟང་བ་ཉིད་དོ། །

[Block 1772]
[^1028]དེ་ལྟར་བྱེད་པ་ཅི༌[^1029]འདྲ་བར་འགྱུར་བ་ལྟ་ཅི་སྨོས། དེ་ལྟར་བྱ་བའི་ཁྱད་པར་བསྟན་པའི་ཕྱིར། ནོར་ནི་གཅིག་པུས་སྤྱད་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་སྨོས་སོ། །

[Block 1773]
བྱ་བ་དེའི་ཁྱད་པར་རྣམ་པ་གཉིས་སུ་བསྟན་པ་སྟེ།[^1030] སློང་བ་ཉིད་དུ་རྙེད་དཀའ་བའི་ཕྱིར་དང་། སྦྱིན་པའི་དངོས་པོ་ཤེས་པས་མ་རུང་བ་ཡོངས་སུ་གཏོང་བ༌[^1031]ལེགས་པའི་ཕྱིར་རོ། །

[Block 1774]
དེ་ལས་ནང་གི་དངོས་པོ་གཏོང་བ་རྙེད་དཀའ་བའི་དབང་དུ་བྱས་ནས། ནོར་ནི་གཅིག་པུས་སྤྱད་པ་མ་ཡིན་ལ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 1775]
གཅིག་པུས་མ་ཡིན་ལ་ཞེས་བྱ་བ་ནི་ནོར་འདི་དག་གཅིག་པུས་སྤྱད་པ་གང་ཡིན་པ་དེ་ནི་དེ་སྟེ། ནོར་གཅིག་པུས་སྤྱད་པར་བྱ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1776]
ནོར་ཞེས་སྨོས་པས་ནི་བཟའ་བ་དང་། བཏུང་བ་དང་། གོས་ལ་སོགས་པ་བྱེ་བྲག་མེད་པར་གཟུང་ངོ་། །ཉིན་རེ་མ་ཡིན་ལ་ཞེས་བྱ་བ་ནི། ཉི་མ་རེ་རེ་ཞིང་མ་ཡིན་པ་སྟེ། དུས་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1777]
མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་རྙེད་དཀའ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1778]
སློང་བ་འདི་ལྟ་བུ་དང་ཞེས་བྱ་བ་ནི་ནང་གི་དངོས་པོ་ལོངས་སྤྱོད་ཅིང་སློང་བའི་སྐྱེ་བོ་ནི་ཉུང་བས་སོ། །

[Block 1779]
ལྷ་དག་མཉེས་པར་བྱས་ཀྱང་མི་འགྲུབ་ན། །ཞེས་བྱ་བ་འདིས་ནི་ཤིན་ཏུ་རྙེད་དཀའ་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1780]
སློང་བ་འདི་ལྟ་བུས༌[^1032]ཡང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་ནི་སྦྱིན་པའི་དངོས་པོ་ཉེས་པས༌[^1033]མ་རུང་བར་གྱུར་པའི་སྦྱིན་པ་དང་། སྦྱིན་པ་གཏོང་བ༌[^1034]སླ་བ་ཉིད་དུ་སྟོན་པར་འདོད་པས་བརྩམས་པ་ཡིན་ནོ། །

[Block 1781]
ཅུང་ཟད་ཅེས་བྱ་བ་ནི་འཆི་བའི་ཆོས་ཅན་ཡིན་ལ། ཇི་སྲིད་དུ་འདུག་པ༌[^1035]དེ་སྲིད་དུ་ཡང་མི་བདེ་བའི་གནས་སུ་གྱུར་ཅིང་མི་བདེ་བའི་གཞིར་གྱུར་པ་སྟེ། རྒ་བ་དང་ནད་ལ་སོགས་པའི་སྡུག་བསྔལ་གྱི་གཞིར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 1782]
ཐེ་ཚོམ་ཟ་བའང་ཞེས་བྱ་བ་ནི་སྦྱིན་པར་བྱ་བའམ། སྦྱིན་པར་མི་བྱ་ཞེས་སོ། །

[Block 1783]
རྒྱ་ཆེར་མི་འགྱུར་ན་ཞེས་བྱ་བ་ནི་སློང་བའི་སྐྱེ་བོ་ཉིད་དོ། །

[Block 1784]
འཇུངས་ཤིང་ཞུམ་པ་ཞེས་བྱ་བ་ནི་སྦྱིན་པར་མི་འདོད་པ་ཉིད་དོ། །

[Block 1785]
མུན་པའི་མཆོག་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གཏི་མུག་གི་རབ་མཆོག་སྟེ། དེ་བས་ན༌[^1036]ཐེ་ཚོམ་ཟ་བ་ཡང་མི་རིགས་པ་ཉིད་ན། མི་སྦྱིན་པ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། རང་གི་ལུས་ལ་རྩ་བཀྲོས་ཏེ། གནོད་སྦྱིན་དེ་རྣམས་ལ་ཞེས་བྱ་བ་ནི།

[Block 1786]
དང་པོ་ཉིད་དུ་རྗེས་སུ་འདོད་པ་ནི་འདི་ཉིད་དུ༌[^1037]ཡིན་པས་སོ། །

[Block 1787]
ཆོས་ཀྱི་གྲོགས་ཀྱང༌[^1038]བྱ་བ་དང་། །ཞེས་བྱ་བ་ནི། སློང་བ་རྣམས་ཀྱི༌[^1039]བྱང་ཆུབ་སེམས་དཔའ་དགེ༌[^1040]བའི་བཤེས་གཉེན་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 1788]
འདི་ནི་རེ་ཞིག་འཇིག་རྟེན་ཕ་རོལ་གྱི་ཕན་ཡོན་ནོ། །

[Block 1789]
ང་ཡང་རབ་ཏུ་དགའ་བར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་ཕན་ཡོན་ནོ། །

[Block 1790]
ཆོས་དགའ་བ་དེ་གཉིས་ཀྱི་དངོས་པོས་ནི་འཛིན་པའི་འཇིག་པ༌[^1041]ལས་ལྡོག་པ་སྟེ། དེའི་ཕན་ཡོན་རྣམ་པ་གཉིས་བསྟན་ཏོ། །
--- END BLOCKS ---
