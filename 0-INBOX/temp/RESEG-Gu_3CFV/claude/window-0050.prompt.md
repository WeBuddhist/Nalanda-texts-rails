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
རེངས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་བར་བྱེད་དུ་བཅུག་པ་ལ་ཡང་ལྟུང་བྱེད་དོ། །

[Block 1752]
ཉེས་བྱས་སུ་གྱུར་པ་ལ་ནི་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1753]
བསྙེན་པར་རྫོགས་པས་བྱེད་དུ་བཅུག་ན་བྱེད་དུ་བཅུག་པ་དང་བྱེད་པ་པོ་གཉིས་ཀ་ལ་ཁ་ན་མ་ཐོ་བ་དང་འདྲ་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1754]
དེ་བས་ན་སྐྱེས་པར་རིག་པར་བྱའོ། །

[Block 1755]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 1756]
རེངས་པའི་བསམ་པ་ལ་ཇི་ལྟ་བ་བཞིན་དུ་རེངས་སུ་བཅུག་པའི་བསམ་པ་ལ་ཡང་དེ་བཞིན་ནོ། །

[Block 1757]
རྩེ་བའི་བསམ་པ་ལ་ཇི་ལྟ་བ་བཞིན་དུ་རྩེར་འཇུག་པའི་བསམ་པ་ལ་ཡང་དེ་བཞིན་ནོ། །

[Block 1758]
དགའ་བའི་བསམ་པ་ལ་ཇི་ལྟ་བ་བཞིན་དུ་དགར་འཇུག་པའི་བསམ་པ་ལ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 1759]
ཇི་བསམ་པ་གང་ཡང་རུང་བས་དེ་ལས་གཞན་པའི་ཡུལ་ལས་སྐྱེས་པའི་བྱ་བ་རྣམས་རྗེས་སུ་བསྒྲུབ་པ་ལ་ཁ་ན་མ་ཐོ་བ་འདི་རྣམས་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་དགོད་པས༌[^1115]དགའ་བ་ཉམས་སུ་མྱོང་བར་བྱ་བའི་འདུན་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་སྲིད་དུ་དགའ་བའི་ངོ་བོ་མེད་པར་འདུན་པ་འདི་མི་འགྲུབ་པས་དེ་སྲིད་དུ་འདིར་འདི་ནི་མཐར་རོ། །

[Block 1760]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་དགེ་སློང་གིས་བུམ་པའི་སྦྱོར་བས་ཆུས་འཐོར་ན་ཐམས་ཅད་དུ་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1761]
དེའི་ཕྱིར་སིམ་པར་འདོད་པས་རྒལ་བ་ལ་སོགས་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ནུབ་པ་དང་མ་ནུབ་པ༌[^1116]དག་ལ་སོགས་པའི་སྒྲས་འཕངས་པའོ། །

[Block 1762]
རྐྱལ་སློབ་པ༌[^1117]ཐད་ཀའམ་ལྟག་འོག་ཏུ་རྩོལ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ལྟག༌[^1118]འོག་ཏུ་ཞེས་བྱ་བ་ནི་སྲིད་དུའོ། །

[Block 1763]
ཐད་ཀར་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1764]
གྲང་བར་འདོད་པས་ཚ་བ་དག་ལ་རི་མོ་འདོད་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གྲང་ཞིང༌[^1119]ངད་ལས༌[^1120]པར་འདོད་པས་ནི་ཉི་མ་ལ་སོགས་ཚ་བར་གྱུར་པའི་ཆུ་དག་ལ་རི་མོ་འདོད་པར་བྱེད་པ་ལྟུང་བ་མེད་དོ། །

[Block 1765]
ཆུ་ལ་རྩེ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1766]
ཅི་ཞིག་བྱས་ནས་འཇུག་པ་གང་བུད་མེད་དང་ལྷན་ཅིག་ཉལ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བུད་མེད་དང་ལྷན་ཅིག་གནས་གཅིག་ཏུ་གཉིད་ལོག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྷན་ཅིག་ཅེས་བྱ་བ་ནི་གཉིས་ཀ་དག་ཀྱང་ལྷན་ཅིག་གཉིད་ལོག་པ་ལས་འདའ་བར་བྱེད་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1767]
དུས་གང་གི་ཚེ་གཉིད་ལོག་པ་ན་ཞེ་ན། དེའི་ཕྱིར་མཚན་མོའོ་ཞེས་སྨོས་སོ། །

[Block 1768]
ཅི་མཚན་མོ་ཐམས་ཅད་ཀྱི་སྐད་ཅིག་གང༌[^1121]ཡང་རུང་བ་ལའམ་ཞེ་ན། དེའི་ཕྱིར་མཐར་རོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1769]
ཅི་མཚན་མོའི་མཐའི་མདུན་རོལ་དུ་ལྟུང་བ་མེད་དམ་ཞེ་ན། དེའི་མདུན་རོལ་དུ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་འདིར་སྟོབས་དང་མི་ལྡན་པའི་མ་ནིང་ལ་སོགས་པ་དང་། དུད་འགྲོ་ལ་སོགས་པ་རྣམས་ལ་སོ་སོར་སྟོབས་དང་ལྡན་པ་ཉིད་ལ་ཡང་ཉེས་བྱས་ཡིན་ན་ནི་སྤྱི་བོ་ཚོད་གང་ཡང་རུང་བ་དང་ལྡན་པའི་མཐུ་མེད་པ༌[^1122]ལ་སོགས་པ་དེར་ཤེས་པར་བྱ་འམ་ཞེ་ན། དེའི་ཕྱིར་བྱ་གག་གི་ཚད་ནི་དེ་བྱེད་པ་ཉིད་ཀྱི་མཐའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཞན་ཡང་དེ་བྱེད་པ་ཉིད་ནི་ཉེས་བྱས་བྱེད་པ་མཐའོ་ཞེས་བྱ་བ་མཐའ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1770]
བུད་མེད་དང་ལྷན་ཅིག་ཉལ་བའི་ལྟུང་བྱེད།[^1123] །།

[Block 1771]
གང་ལ་སྔངས་པར་བྱེད་པའི་ཁ་ན་མ་ཐོ་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བཞད་གད་བྱ་བའི་བསམ་པས་ཀྱང་རུང་སྟེ། ངང༌[^1124]བར་འདོད་པས་འཇིགས་པའི་རྒྱུ་ཉེ་བར་བསྒྲུབ་པར་སྔོན་དུ་བཏང་བ་འཇིགས་པར་བྱེད་པ་ཆེ་གེ་མོ་ཞིག་ཅེས་དགེ་སློང་ལ་གཞན་གྱིས་ཀྱང་གོ་བར་བྱེད་ན་འཇིགས་པ་མ་སྐྱེས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཤེས་པར་གྱུར་པའི་འཇུག་པ་བྱེད་པ་འདི་ནི་འཇུག་པ་འདི༌[^1125]ཤེས་པ་ཡིན་ཏེ། འདི་ལ་འཇིགས་པ་བསྐྱེད་པ་འདི་ལས་འབྱུང་བ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་བློ་ཡོད་པ་ལ་འཇིགས་པའི་འདུན་པ་ལ་གོ་སྐབས་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1772]
དེ་བས་ན་འཇིགས་པར་འདུན་པས་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་གོ། །

[Block 1773]
འཇིགས་པའི་རྒྱུ་མཚན་ཡིད་དུ་འོང་བ་མ་ཡིན་པའི་ངོ་བོ་ལ་སོགས་པ་ལ་ཉེ་བར་བསྒྲུབ་པ་སྔོན་དུ་འགྲོ་བས་གོ་བར་བྱེད་ན་འཇིགས་པའི་ཁ་ན་མ་ཐོ་བའོ། །

[Block 1774]
འདིར་གཞུང་ནི༌[^1126]ཡིད༌[^1127]དུ་མི་འོང་བའི་གཟུགས་རྣམས་ཉེ་བར་སྒྲུབ་པར་བྱེད་པ་དེ་ནག་པོ་དང་ཁ་དོག་ནག༌[^1128]པོར་སྟོན་པ་དེ་ནག་པོར་སྣང་བའོ། །

[Block 1775]
འདི་ལྟ་སྟེ་དཔེར་ན་ཡི་དགས་དང་ཤ་ཟ་དང་གྲུམ་བུམ༌[^1129]དང་ལུས་སྲུལ་པོའི་གཟུགས་ཅན་དེ་ལྟ་བུ་དེ་རྣམས་ཀྱིས༌[^1130]ནི་རུང་བ་དང་། དེ་རྣམས་ཀྱིས༌[^1131]ནི་གསོད་པར་གྱུར་པ་དང་། དེ་རྣམས་ཀྱིས་ནི་སྲོག་གཅོད་པར་འགྱུར་ཏེ། དེ་ལྟ་བུར་གྱུར་པའི་རྣམ་གྲངས་གཞན་ཡང་ཤེས་པར་བྱའོ། །

[Block 1776]
འདིར་ཡང་དེ་ལྟ་བུའི་གཟུགས་ཅན་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1777]
ལྷག་མ་འཇིགས་པའི་རྒྱུ་ཉེ་བར་བསྒྲུབ་པར་བྱའོ། །

[Block 1778]
སྔོན་དུ་འགྲོ་བ་ཞེས་བྱ་བ་འདི་ལ་གོ་བར་བྱེད་པ་ན་རྣམ་པ་གཉིས་ཏེ། དོན་དང་གོ་བར་བྱ་བ་ལའོ། །

[Block 1779]
དེ་ལ་དོན་གོ་བར་བྱེད་པ་གང་ལ་ཞེས་བྱ་བ་འདི་ལ་འཇིགས་པར་བྱེད་པ་ཞེས་སྨོས་པ་ཡིན་ནོ། །ཇི་ལྟར་འཇིགས་པར་གོ་བར་བྱེད་པ་གོ་བར་བྱེད་ཅེ་ན། དེའི་ཕྱིར་ཆེ་གེ་མོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1780]
གང་ལ་གོ་བར་བྱེད་ཅེས་བྱ་བའི་དྲི་བ་འདི་ལ་དགེ་སློང་ལ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1781]
ཅི་བདག་ཉིད་ཀྱིས་དེ་ལྟ་བུ་གོ་བར་བྱེད་པ་ལ་འཇིགས་པའི་ཁ་ན་མ་ཐོ་བ་ཞེས་བྱ་བ་འདི་ལ་གཞན་གྱིས་ཀྱང་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1782]
ཅི་མ་སྐྱེས་པ་ལ་ཡང་གོ་བར་བྱ་ཞེས་བྱ་བའི་འཇིགས་པ་ལ་ཁ་ན་མ་ཐོ་བ་འདི་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འཇིགས་པ་མ་སྐྱེས་ཀྱང་ངོ་ཞེས་བྱ་བ་སྨོས༌[^1132]སོ། །

[Block 1783]
འཇིགས་པའི་རྒྱུ་ཅི་འདྲ་བ་ཞིག་ཉེ་བར་བསྒྲུབ་པ་ལ་ཁ་ན་མ་ཐོ་བ་ཅི་འདྲ་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཡིད་དུ་མི་འོང་བ་ལ་ནི་དངོས་གཞིའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1784]
འདིར་ཡིད་དུ་མི་འོང་བ་དཔེས་བསྟན་པའི་ཕྱིར། འདི་ལྟ་སྟེ་དཔེར་ན་ཡི་དགས་དང་ཤ་ཟ་དང་གྲུམ་བུམ༌[^1133]དང་ལུས་སྲུལ་པོའི་གཟུགས་ལ་བ་ནག་པོ་དང་སོལ་བ་དང་ཀ་བ་ཚིག་པ་ལྟ་བུ་དང་། སེང་གེ་དང་སྟག་དང་གུང་དང་། མཚའ་དང་གཟིག་དང་ཝའི་སྐད་ལྟ་བུ་བཤང་བ་དང་གཅི་བ་དང་རྭ་དང་དེའི་ཟེ་བའི་དྲི་ལྟ་བུ་སེག་དང་རེ་ལྡེ་དང་ཕྱར་བའི་རེག་པ་ལྟ་བུ་བདག་ཉིད་སྒྲོགས་པའོ༌[^1134]ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཐམས་ཅད་དུ་སྒྲ་དང་དྲི་དང་རེག་བྱ་རྣམས་ལ་ཡི་དགས་དང་། ཤ་ཟ་དང་གྲུམ་བུམ༌[^1135]དང་ལུས་སྲུལ་པོ་ཡོད་དོ་ཞེས་སྒྲོགས་ཤིང་གོ་བར༌[^1136]བྱེད་པ་འདི་ལ་འདིར་སོ་སོར་རྗེས་སུ་སྦྱར་བར༌[^1137]རིག་པར་བྱའོ། །

[Block 1785]
སེང་གེ་ལ་སོགས་པའི་སྒྲ་ལ་སོགས་པ་རྣམས་ལ་ཡི་དགས་ལ་སོགས་པར་གྲགས་པས་གོ་བར་བྱེད་ན་དངོས་གཞི་སྟེ་གཞན་རྣམས་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1786]
ཡིད་དུ་འོང་བ་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་ཡིད་དུ་འོང་བའི་རྒྱུ་ཉེ་བར་བསྒྲུབ་པ་སྒྲོགས་ན་ཉེས་བྱས་སོ། །

[Block 1787]
གང་གི་ཕྱིར་འདི་ལ་འཇིགས་པའི་རྒྱུ་ཡོངས་སུ་རྫོགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་འདི་ལ་ཤིན་ཏུ་ཡིད་འབྱུང་བར་བྱེད་པ་ཉིད་མ་ཡིན་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1788]
འདིར་ཡིད་དུ་འོང་བ་དཔེ༌[^1138]བསྟན་པའི་ཕྱིར། འདི་ལྟ་སྟེ་དཔེར་ན་ལྷ་དང་ཀླུ་དང་དྲི་ཟ་དང་གནོད་སྦྱིན་དང་མིའམ་ཅི་དང༌[^1139]ལྟོ་འཕྱེ་ཆེན་པོ་གཟུགས་ནོར་ཅན་དང་ཚོང་དཔོན་དང་དེད་དཔོན་ལ་སོགས་པ་ལྟ་བུ། པི་ཝང་ལ་སོགས་པའི་སྒྲ་ལྟ་བུའོ་ཞེས་བྱ་བ་ལ། འདིར་སོགས་པའི་སྒྲས་ནི་གླིང་བུ་དང་བ་ལ་རི་དང་མ་ཧཱ་ཏི་དང་སུ་གོ་ཥ་ལྟ་བུ་རྣམས་ཀྱང་བསྡུའོ། །

[Block 1789]
ཨ་ཀ་རུ་དང་ཙན་དན་དང་གུར་གུམ་དང་། ཏ་མ་ལའི་ལོ་མའི་དྲི་ལྟ་བུ་དང་། དར་དང་རས་ཡུག་ཆེན༌[^1140]དང་བེའུ་རས་དང་དར་ལ༌[^1141]དང་དུ་ཀུ་ལའི་རས་དང་། ཀོ་ཏམ་པའི་རས་ཀྱི་རེག་པ་ལྟ་བུ་རྣམས་ཉིད་སྒྲོགས་པའོ་ཞེས་བྱ་བ་ནི་ཇི་སྲིད་ལྷ་ལ་སོགས་པ་འདི་ན་ཡོད་དོ་ཞེས་སྒྲོགས་ཤིང་ཞེས་བྱ་བ་འདི་ལ་འདིར༌[^1142]ཐམས་ཅད་དུ་སྦྱར་བར་རིག་པར་བྱའོ། །

[Block 1790]
འདིར་ལྷ་ལ་སོགས་པ༌[^1143]སྨོས་པ་ནི་མཚོན་པ་ཙམ་ཡིན་ཏེ་ཤིན་ཏུ་ཆེ་བའི་ཡི་དགས་ལ་སོགས་པ་རྣམས་ཀྱང་འདིར་བསྡུས་པའོ། །
--- END BLOCKS ---
