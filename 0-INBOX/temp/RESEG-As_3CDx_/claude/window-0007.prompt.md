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
[Block 246]
དེ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་ནི་རྣམ་པར་ཐར་པའི་སྒོ་ཆེན་པོ༌[^179]མཚན་མ་མེད་པ་ཞེས་བྱའོ། །

[Block 247]
སྨོན་པ་མེད་པ་ཞེས་བྱ་བ་ལ་སྨོན་པ་ནི་སྨོན་ལམ་སྟེ༌[^180]འདོད་པའོ། །

[Block 248]
དེ་གང་ལ་མེད་པ་ནི་སྨོན་པ་མེད་པ་སྟེ། དེ་ཡང་གང་ཞེ་ན་ཁམས་གསུམ་པ་སྡུག་བསྔལ་བར་མཐོང་ན་དེ་ལ་སྨོན་པར་བྱ་བ་མེད་དོ༌[^181]སྙམ་ནས་དེར་སྨོན་ལམ་མི་འདེབས་པ༌[^182]ནི་སྨོན་པ་མེད་པའོ། །

[Block 249]
དེ་ལ་དམིགས་པའི་ཏིང་ངེ་འཛིན་ནི་རྣམ་པར་ཐར་པའི་སྒོ་ཆེན་པོ་སྨོན་པ་མེད་པ་ཞེས་བྱའོ། །

[Block 250]
ནས་འཇུག་པས་ཞེས༌[^183]བྱ་བ་ནི་སྟོང་པ་ཉིད་ལ་སོགས་པ་རྣམ་པར་ཐར་པའི་སྒོ་ཆེན་པོ་དེ་དག་ནས་དེར་འཇུག་པར་འགྱུར་རོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། དེ་ནི་སྒོ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 251 [HEADING]]
##### རྟེན་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-18-0

[Block 252]
དེ་ལྟར་སྒོ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ནས། སྒོ་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་པ་དེ་གཞལ་མེད་ཁང་གཞན་དག་བཞིན་དུ་གང་ལ་བརྟེན་པའི་རྟེན་ཀྱང་དགོས་པ་དེའི་ཕྱིར་རྟེན་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི༌[^184]དབང་དུ་མཛད་ནས། རིན་པོ་ཆེའི་པདྨའི་རྒྱལ་པོ་ཆེན་པོ་ཡོན་ཏན་མཐའ་ཡས་པས་བརྒྱན་པའི་བཀོད་པ་ལ་བརྟེན་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། དཔེར་ན་ཆུའི་དཀྱིལ་འཁོར་ལ་སོགས་པ་སའི་དཀྱིལ་འཁོར་ལ་སོགས་པ་ལ༌[^185]བརྟེན་པ་དང་། འཇིག་རྟེན་པའི་གཞལ་མེད་ཁང་དག་པ༌[^186]དང་ནམ་མཁའ་ལ་བརྟེན་པ་བཞིན་དུ་གཞལ་མེད་ཁང་འདི་ཡང་རིན་པོ་ཆེའི་པདྨའི་རྒྱལ་པོ་ཆེན་པོ་ཡོན་ཏན་མཐའ་ཡས་པས་བརྒྱན་པའི་བཀོད་པ་ལ་བརྟེན་ཏེ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 253]
དེ་ལ་རིན་པོ་ཆེའི་པདྨ་ཞེས་བྱ་བ་ནི་པདྨ་དེ་ཉིད་རིན་པོ་ཆེ་ཡང་ཡིན་ལ་པདྨ་ཡང་ཡིན་ཏེ། རིན་པོ་ཆེའི་རང་བཞིན་གྱི་པདྨ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 254]
རྒྱལ་པོ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་དེ་ཉིད་རིན་པོ་ཆེའི་རྒྱལ་པོ་ཆེན་པོ་ཡང་ཡིན་ལ་པདྨའི་རྒྱལ་པོ་ཆེན་པོ་ཡང་ཡིན་པའོ། །

[Block 255]
ཡང་ན་རིན་པོ་ཆེའི་པདྨ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^187]བྱིན་གྱི་རླབས༌[^188]ལས་བྱུང་བ་འཁོར་གྱི་པདྨ་དག་ཡིན་ནོ། །

[Block 256]
རྒྱལ་པོ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ལ་སོགས་པ་དེ་དག་གི་བླ་མ་སྟེ། ཆོས་ཀྱི་རྒྱལ་པོ་ཆེན་པོ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱི་དགེ་བའི་རྩ་བ་ལས་བྱུང་བའི་པདྨ་ཆེན་པོ་ཉིད་ཡིན་པར་སྦྱར་རོ། །

[Block 257]
ཡོན་ཏན་མཐའ་ཡས་པས་བརྒྱན་པ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པ་ཆེ་བའི་ཡོན་ཏན་ལས་རྒྱན་སྣ་ཚོགས་སུ་གྲུབ་པའི་རྒྱན་སྣ་ཚོགས་ཀྱིས་བརྒྱན་པའོ། །

[Block 258]
བཀོད་པ་ཞེས་བྱ་བ་ནི་རྒྱན་དེའི་ཁྱད་པར་རོ། །

[Block 259]
ལ་བརྟེན་པ་ཞེས་བྱ་བ་ནི་རྒྱན་དེའི་ཁྱད་པར་གྱི་བཀོད་པ་ཆེན་པོ་དེ་ལ་གཞལ་མེད་ཁང་དེ་བརྟེན་ཅེས་བྱ་བའི་ཐ་ཚིག་སྟེ། དེ་ནི་རྟེན་ཕུན་སུམ་ཚོགས་པ་ཡིན་ནོ། །

[Block 260]
ན་བཞུགས་ཏེ་ཞེས་བྱ་བ་ནི་རྒྱན༌[^189]གྱི་བཀོད་པ་ཆེན་པོ་ལ་བརྟེན་པའི་གཞལ་མེད་ཁང་ཆེན་པོ་དེ་ན་བཅོམ་ལྡན་འདས་བཞུགས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 261]
བཞུགས་ཞེས་བྱ་བ་ནི་སྤྱོད་ལམ་དང་། ལྷ་དང་ཚངས་པ་དང་། འཕགས་པའི་བཞུགས་པ་བླ་ན་མེད་པ་དག་གིས་བཞུགས་པའོ། །

[Block 262]
[^190]གནས་ཕུན་སུམ་ཚོགས་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 263 [HEADING]]
#### ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ། ^3-2-2-0

[Block 264]
ཅི་འདྲ་བ་ཅིག༌[^191]བཞུགས་ཤེ་ན། །ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་སྟེ། དེའི་ཕྱིར་དེའི༌[^192]དབང་དུ་མཛད་ནས་བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 265]
དེ་ལ་བཅོམ་ལྡན་འདས་ཀྱི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་བསྟན་པ་ནི་དེ་ལས་གཞན་པའི་སྟོན་པ་རྣམས་ལས་ཁྱད་པར་དུ་བྱ་བ་དང་། གཞན་དག་ཀྱང་དང་བ་རབ་ཏུ་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 266 [HEADING]]
##### ཡོན་ཏན་གྱི་ཁྱད་པར་རྣམ་པ་ཉི་ཤུ་རྩ་གཅིག། ^3-2-2-1-0

[Block 267]
དེའི་ཕུན་སུམ་ཚོགས་པ་ནི་ཡོན་ཏན་གྱི་ཁྱད་པར་རྣམ་པ་ཉི་ཤུ་རྩ་གཅིག་ཏུ་རིག་པར་བྱ་སྟེ། མངོན་པར་བྱང་ཆུབ་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། སྒྲིབ་པ་མི་མངའ་བའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། འདུལ་བའི་ཐབས་ཀྱི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། འདུལ་བ་ལ་སོ་སོར་རྟོག་པའི༌[^193]ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། སངས་རྒྱས་ཐམས་ཅད་དང་ཕྲིན་ལས་ཀྱི་མཛད་པ་མཐུན་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། མི་མཐུན་པའི་ཕྱོགས་སྤང་བའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། མུ་སྟེགས་ཅན་ཟིལ་གྱིས་གནོན་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། བདུད་ཟིལ་གྱིས་གནོན་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། ཆོས་བསྟན་པ་རྣམ་པར་འཇོག་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། དུས་གསུམ་ལུང་སྟོན་པ་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། དགའ་ལྡན་གྱི་ཕོ་བྲང་ནས་འབབ་པ་ལ་སོགས་པ་ཀུན་དུ་སྟོན་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། ཐེ་ཚོམ་གྱི་རྣམ་པ་ཐམས་ཅད་གཅོད་པའི་ཡོན་ཏན་གྱི༌[^194]ཁྱད་པར་དང་། ཐེག་པ་ཐམས་ཅད་ཀྱིས་འདུལ་བ་དེ་དག་ལ་སྣང་བའི་སྐུ་ཀུན་དུ་སྟོན་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། ཤིན་ཏུ་རྣམ་པར་མཁྱེན་ནས་ཅི་རིགས་པར༌[^195]གདམས་ངག་སྩོལ་བའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། ཀུན་ནས་ཉོན་མོངས་པ་མེད་པའི་སྐུ་ཡོངས་སུ་འཛིན་པའི་ཡོན་ཏན་གྱི༌[^196]ཁྱད་པར་དང་། སངས་རྒྱས་ཀྱི་གདུང་མི་འཆད་པར་སྦྱོར་བའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། སངས་རྒྱས་ཀྱི་རང་བཞིན་གྱི་སྐུ་ལ་བཞུགས་པའི་ཡོན་ཏན༌[^197]གྱི་ཁྱད་པར་དང་། སངས་རྒྱས་ཀྱི་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་ལ་བཞུགས་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། མཚན་ཉིད་ཀྱི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། འབྲས་བུ་ཐོབ་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་དང་། ཡོན་ཏན་མི་ཟད་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་རོ། །

[Block 268]
ཕུན་སུམ་ཚོགས་པ་ཉི་ཤུ་གཅིག༌[^198]པོ་དེ་དག་ནི་མདོ་ལས།

[Block 269]
ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནས། ནམ་མཁའི་ཁམས་ཀྱི་མཐས༌[^199]གཏུགས་པ་དེ་ཞེས་གསུངས་པའི་ཚིག་ཉི་ཤུ་རྩ་གཅིག་དང་གོ་རིམ༌[^200]བཞིན་དུ་སྦྱར་རོ། །

[Block 270 [HEADING]]
###### མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར། ^3-2-2-1-1-0

[Block 271]
དེ་ལ་དང་པོར་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་བསྟན་པའི་དབང་དུ་མཛད་ནས། ལེགས་པར་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཆོས་ཇི་སྙེད་ཡོད་པ་ཉིད་དང་། ཇི་ལྟ་བ་བཞིན་དུ་ཡོད་པ་ཉིད་ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 272]
དེ་ལ་ལེགས་པར་བྱ་བའི་ཚིག་གི་དོན་ནི་རྟོགས་པར་བྱ་བ་ལེགས་པར་རྟོགས་པ་དང་། ཡོངས་སུ་རྫོགས་པར་རྟོགས་པ་དང་། མ་ལུས་པར་རྟོགས་པའི་དོན་ཏོ། །

[Block 273]
ཐུགས་སུ་ཆུད་པའི་བློ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་ཇི་སྙེད་པ་ཉིད་དང་ཇི་ལྟ་བ་བཞིན་དུ་ཡོད་པ་ཉིད་རྟོགས་པར་ཐུགས་སུ་ཆུད་པའི་མཁྱེན་པ་མངའ་བ་སྟེ། དེ་ནི་མངོན་པར་རྫོགས་པའི་བྱང་ཆུབ་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་ཡིན་ནོ། །

[Block 274 [HEADING]]
###### སྒྲིབ་པ་མི་མངའ་བའི་ཡོན་ཏན་གྱི་ཁྱད་པར། ^3-2-2-1-2-0

[Block 275]
དེའི་འོག་ཏུ་སྒྲིབ་པ་མི་མངའ་བའི་ཡོན་ཏན་གྱི་ཁྱད་པར་བསྟན་པའི་དབང་དུ་མཛད་ནས། ཀུན་དུ་སྤྱོད་པ་གཉིས་མི་མངའ་བ་ཞེས་བྱ་བ་གསུངས་ཏེ། བྱིས་པ་དང་ཉན་ཐོས་ཀྱི་སྤྱོད་པ་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་གཉིས་མི་མངའ་བ་ཞེས་བྱ་བར་སྦྱར༌[^201]རོ། །

[Block 276]
དེ་ལ་བྱིས་པའི་ཀུན་དུ་སྤྱོད་པ་ནི་འཁོར་བའི་ཀུན་ནས་ཉོན་མོངས་པ་སྟེ། དེའི་བདག་ཉིད་གནས་པའི་ཕྱིར་རོ། །

[Block 277]
ཉན་ཐོས་ཀྱི་ཀུན་དུ་སྤྱོད་པ་ནི་མྱ་ངན་ལས་འདས་པ་ལ་གཅིག༌[^202]ཏུ་ངེས་པ་སྟེ། གཞན་གྱི་དོན་བྱ་བ་ལ་རྒྱབ་ཀྱིས་ཕྱོགས་པའི་ཕྱིར་རོ། །

[Block 278]
དེ་ལྟར་ན་བྱིས་པའི་ཀུན་དུ་སྤྱོད་པ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པའི་རང་བཞིན་ཡིན་ལ། ཉན་ཐོས་ཀྱི་ཀུན་དུ་སྤྱོད་པ་ནི་ཤེས་བྱའི་སྒྲིབ་པའི་རང་བཞིན་ཡིན་པས་དེ་གཉིས་ནི་སྒྲིབ་པ་མེད་པའི་ཡོན་ཏན་དང་ལྡན་པའི་ཁྱད་པར་དང་ལྡན་པ་མ་ཡིན་གྱི།[^203] བཅོམ་ལྡན་འདས་ནི་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་ལ་བཞུགས་པ་ཡིན་པས་དེ་ལ་ཀུན་དུ་སྤྱོད་པ་དེ་གཉིས་མི་མངའ་སྟེ། དེ་ནི་སྒྲིབ་པ་མི་མངའ་བའི་ཡོན་ཏན་གྱི་ཁྱད་པར་ཡིན་ནོ། །

[Block 279 [HEADING]]
###### འདུལ་བའི་ཐབས་ཀྱི་ཡོན་ཏན་གྱི་ཁྱད་པར། ^3-2-2-1-3-0

[Block 280]
དེའི་འོག་ཏུ་འདུལ་བའི་ཐབས་ཀྱི་ཡོན་ཏན་གྱི་ཁྱད་པར་བསྟན་པའི་དབང་དུ་མཛད་ནས། མཚན་ཉིད་མེད་པའི་ཆོས་ལ་མཆོག་ཏུ་གཞོལ་བར་མཛད་པ་ཞེས་བྱ་བ་གསུངས༌[^204]ཏེ། དེ་ལ་མཚན་ཉིད་མེད་པའི་ཆོས་ཞེས་བྱ་བ་ནི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 281]
མཆོག་ཏུ་གཞོལ་བར་མཛད་པ་ཞེས་བྱ་བ་ནི་སྐལ་བ་ཇི་ལྟ་བ་བཞིན་དུ་ཐེག་པ་གསུམ་གྱིས་སེམས་ཅན་རྣམས་དེར་འདུལ་བའི་ཐབས་ཡོངས་སུ་མཁྱེན་ནས་དེ་བཞིན་དུ་སྟོན་ཅིང་དེ་དག་དེར་གཞོལ་བ་དང་། འབབ་པ་དང་། བབ་པར་མཛད་པ་སྟེ། དེ་ནི་འདུལ་བའི་ཐབས་ཀྱི་ཡོན་ཏན་གྱི་ཁྱད་པར་ཡིན་ནོ། །

[Block 282 [HEADING]]
###### འདུལ་བ་ལས་སོ་སོར་རྟོག་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར། ^3-2-2-1-4-0

[Block 283]
དེའི་འོག་ཏུ་འདུལ་བ་ལས་སོ་སོར་རྟོག་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་བསྟན་པའི་དབང་དུ་མཛད་ནས། སངས་རྒྱས་ཀྱི་གནས་པས་གནས་པ་ཞེས་བྱ་བ་གསུངས་ཏེ། དེ་ལ་སངས་རྒྱས་ཀྱི་གནས་པ་ཞེས་བྱ་བ་ནི་སྐབས་འདིར་ཐུགས་རྗེ་ཆེན་པོས་ཉིན་མཚན་དུ་ལན་དྲུག་ཏུ་འཇིག་རྟེན་ལ་གཟིགས་པ་དང་སྦྱར་རོ། །

[Block 284]
གནས་པ་ཞེས་བྱ་བ་ནི་དེ་ལྟ་བུའི་གནས་པས་རྟག་ཏུ་གནས་པ་སྟེ། དེ་ནི་འདུལ་བ་ལ་སོ་སོར་རྟོག་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར་ཡིན་ནོ། །

[Block 285 [HEADING]]
###### སངས་རྒྱས་ཐམས་ཅད་དང་ཕྲིན་ལས་ཀྱི་མཛད་པ་མཐུན་པའི་ཡོན་ཏན་གྱི་ཁྱད་པར། ^3-2-2-1-5-0
--- END BLOCKS ---
