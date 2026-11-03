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
དེ་ལྟར་སོ་སོ་ཞིང་དོན་རྣམ་པ་བཞི་ཡིན་ཞེ་ན། གནས་དང་མཚན་ཉིད་དང་། ཆོས་དང་དོན་མདོར་སྟོན་པས་ན། མདོ་སྡེའོ། །

[Block 37]
དེ་ལ་གནས་ནི་ཡུལ་གང་དུ་གང་གིས་གང་ལ་བསྟན་པའོ། །

[Block 38]
མཚན་ཉིད་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པའི་མཚན་ཉིད་དང་། དོན་དམ་པའི་བདེན་པའི་མཚན་ཉིད་དོ། །

[Block 39]
ཆོས་ནི་ཕུང་པོ་དང་། སྐྱེ་མཆེད་དང་། ཁམས་དང་། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དང་། ཟས་དང་། བསམ་གཏན་དང་། ཚད་མེད་པ་དང་། རྣམ་པར་ཐར་པ་བརྒྱད་དང་། ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་དང་། ཟད་པར་གྱི་སྐྱེ་མཆེད་དང་། བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་། སོ་སོ་ཡང་དག་པར་རིག་པ་ལ་སོགས་པའོ། །

[Block 40]
དོན་ནི་རྗེས་སུ་བརྗོད་པའོ། །

[Block 41]
མངོན་དུ་ཕྱོགས་པའི་ཕྱིར་དང་། ཡང་དང་ཡང་དུ་སྟོན་པའི་ཕྱིར་དང་། ཟིལ་གྱིས་གནོན་པའི་ཕྱིར་དང་། མངོན་པར་རྟོགས་པའི་ཕྱིར་ཆོས་མངོན་པར་རིག་པར་བྱ་སྟེ། མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་ལ་མངོན་དུ་ཕྱོགས་པའི་ཆོས་ནི་ཆོས་མངོན་པའོ། །

[Block 42]
བདེན་པ་དང་། བྱང་ཆུབ་ཀྱི་ཕྱོགས་དང་། རྣམ་པར་ཐར་པའི་སྒོ་ལ་སོགས་པ་ཡང་དང་ཡང་དུ་སྟོན་པའི་ཆོས་ནི་ཆོས་མངོན་པ་སྟེ། ཆོས་རེ་རེ་ཞིང་ཡང་ངེས་པའི་ཚིག་དང་། རང་གི་མཚན་ཉིད་དང་། སྤྱིའི་མཚན་ཉིད་ལ་སོགས་པ་རབ་ཏུ་དབྱེ་བ་མང་པོས་སྟོན་པའི་ཕྱིར་རོ། །

[Block 43]
ཟིལ་གྱིས་གནོན་པས་ན་ཆོས་མངོན་པ་སྟེ། ཕས་ཀྱི་རྒོལ་བར༌[^30]འདོད་པའི་དབང་དུ་བྱས་ནས་ཟིལ་གྱིས་གནོན་པ་ཉིད་དོ། །

[Block 44]
མདོ་སྡེའི་དོན་འདིས་རྟོགས་པར་བྱེད་པས་ན་ཡང་ཆོས་མངོན་པའོ། །

[Block 45]
ཡང་འདུལ་བ་ནི་ལྟུང་བ་དང་། ཀུན་ནས་འབྱུང་བ་དང་། ལྡང་བ་དང་། ངེས་པར་འབྱུང་བར་རིག་པར་བྱའོ། །

[Block 46]
དེ་ལ་ལྟུང་བ་ནི་ལྟུང་བའི༌[^31]རིས་ལྔའོ། །

[Block 47]
ཀུན་ནས་འབྱུང་བ་ནི་ལྟུང་བ་མི་ཤེས་པ་ཉིད་དང་། བག་མེད་པ་ཉིད་དང་། ཉོན་མོངས་པ་མང་བ་དང་། མ་གུས་པ་ལས་སོ། །

[Block 48]
ལྟུང་བ༌[^32]ནི་ཇི་ལྟ་བ་བཞིན་དུ་སྡོམ་པ་འཛིན་པའི་བསམ་པས་ཡིན་གྱི། ཆད་པའི་ལས་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 49]
ངེས་པར་འབྱུང་བ་ནི་རྣམ་པ་བདུན་ཏེ། སོ་སོར་ཆགས་པ༌[^33]དང་། ལྟུང་བར་མཐོང་བ་དང་། བསླབ་པ་སྦྱིན་པ་ལ་སོགས་པའི་ཆད་པའི་ལས་དང་། ནང་ཁྲིམས་ཀྱིས་ཏེ། བསླབ་པའི་གནས་བཅས་པ་ལ་ཡང་རིམ་གྱིས་རྗེས་སུ་གནང་བ་ལ་བརྟེན་ནས་དགེ་འདུན་བློ་མཐུན་པས་རབ་ཏུ་བཅས་པའི་བསླབ་པའི་གཞི་རྗེས་སུ་གནང་བ་ཉིད་དང་། རྟེན་གནས་གྱུར་པ་ཉིད་ཀྱིས་ཏེ། དགེ་སློང་དང་དགེ་སློང་མ་བུད་མེད་དང་སྐྱེས་པ་ཉིད་དུ་མཚན་གྱུར་པས་ཐུན་མོང་མ་ཡིན་པའི་བྱེ་བྲག་དག་གོ། །

[Block 50]
ལྟུང་བའི་དེ་ཁོ་ན་ཉིད་ཆོས་ཀྱི་སྐྱེད་མོས་ཚལ་གྱི་རྣམ་པས་སོ་སོར་རྟོག་པའི་ཁྱད་པར་དང་། ཆོས་ཉིད་རབ་ཏུ་རྟོགས་པས་བདེན་པ་མཐོང་བ་ཉིད་ཀྱིས་ལྟུང་བ་ཕྲ་ཞིང་ཕྲ་བ་དག་ལས་ངེས་པར་འབྱུང་ངོ་། །ཡང་དོན་རྣམ་པ་བཞིས་ན་འདུལ་བར་རིག་པར་བྱ་སྟེ། གང་ཟག་ཉིད་ནི་གང་ལ་བརྟེན་ནས་བསླབ་པ་བཅས་པའོ། །

[Block 51]
གང་ཟག་གི་ཉེས་པ་གང་གིས་ཞུས་པ་ན། དེའི་དབང་གིས་དགེ་འདུན་ཐམས་ཅད་འདུས་ནས་བསླབ་པ་བཅས་པས༌[^34]ན་བཅས་པའོ། །

[Block 52]
རབ་ཏུ་དབྱེ་བ་ནི་བསླབ་པའི་གཞི་བཅས་པ་དེ་རྣམ་པར་ཕྱེ་ནས་གཏན་ལ་ཕབ་པའོ། །

[Block 53]
ངེས་པར་གཟུང་བ་ནི་དེ་ལ་ཇི་ལྟར་ལྟུང་བ་དང་། ལྟུང་བ་མེད་པར་ངེས་པར་གཟུང་བའོ། །

[Block 54 [HEADING]]
## ཤེས་བྱའི་གནས། ^1-0

[Block 55 [HEADING]]
### གསུང་ཁྱད་པར་རྣམ་པ་བཅུས་ཁྱད་པར་དུ་འཕགས་པ། ^1-1-0

[Block 56]
ད་ནི་རྩ་བའི་གཞུང་བརྩམ་པར་བྱ་སྟེ། བཅོམ་ལྡན་འདས་ཀྱི་སྤྱན་སྔར་ཞེས་བྱ་བ་ནི་འབད་པ་དང་གུས་པར་བཅས་པས་ཚིག་གཞན་དུ་མ་ཡིན་པའི་དོན་ཏོ། །

[Block 57]
ཐེག་པ་ཆེན་པོ་ལ་ཤིན་ཏུ་ཞུགས་པའི་ཞེས་བྱ་བ་ནི་གཟུངས་ལ་སོགས་པའི་ཡོན་ཏན་རབ་ཏུ་ཐོབ་པ་ཞེས་བྱ་བའི་དོན་ཏེ། ཡོན་ཏན་དེ་དག་ཐོབ་པས་ཀྱང་དོན་དང་ཚིག་ཡང་དག་པར་འཛིན་པ་དང་། རབ་ཏུ་སྟོན་པ་ཉིད་དུ་འདིས་བསྟན་པའམ། དེ་ལྟ་བུའི་མིང་ཅན་གྱི་བྱང་ཆུབ་སེམས་དཔས་སོ། །ཅིའི་ཕྱིར་བརྗོད་ན། ཐེག་པ་ཆེན་པོ༌[^35]ཆེ་བའི་བདག་ཉིད་བརྗོད་པའི་ཕྱིར་ཏེ། དེ་ལ་བརྗོད་པ་ནི་ཐེག་པ་ཆེན་པོ་ཆེ་བའི་བདག་ཉིད་རབ་ཏུ་བསྟན་པའོ། །

[Block 58]
འདི་ལྟ་སྟེ། ཐེག་པ་ཆེན་པོ་ལས་བརྩམས་ནས་ཞེས་བྱ་བ་ནི་དེའི་དབང་དུ་བྱས་ནས་སོ། །

[Block 59]
གསུང་ཁྱད་པར་རྣམ་པ་བཅུས་ཁྱད་པར་དུ་འཕགས་པ་ཞེས་བྱ་བ་ལ། ཁྱད་པར་རྣམ་པ་བཅུས་ཁྱད་པར་དུ་འཕགས་པའི་གསུང༌[^36]གང་ལ་མངའ་བ་དེ་ནི་གསུང་ཁྱད་པར་རྣམ་པ་བཅུས་ཁྱད་པར་དུ་འཕགས་པའོ། །

[Block 60]
གང༌[^37]གཞན་ཡང་ཁྱད་པར་དུ་འཕགས་པའི་སྒྲའི་དོན་ནི་མཆོག་གི་དོན་ཏེ། དེ་ལྟ་བུ་ནི་ཁྱད་པར་དུ་འཕགས་པའི་དོན་ཏོ། །

[Block 61]
དེ་ལ་ཤེས་བྱའི་གནས་ཀྱི་ཁྱད་པར་གྱིས་ཁྱད་པར་དུ་འཕགས་པའི་གསུང་ཞེས་བྱ་བ་ལ། ཤེས་པར་བྱ་བས་ན་ཤེས་བྱའོ། །

[Block 62]
དེ་ཡང་ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བ༌[^38]སྟེ། དེ་ཡང་ངོ་བོ་ཉིད་གསུམ་མོ། །

[Block 63]
དེའི་གནས་ནི་རྒྱུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 64]
ཁྱད་པར་དུ་འཕགས་པའི་གསུང་ཞེས་བྱ་བ་དེ་ཡང་ཀུན་གཞི་རྣམ་པར་ཤེས་པས་སོ། །

[Block 65]
འདི་ནི་ལས་འཛིན་པ་སྟེ། ཤེས་བྱ་ཇི་སྙེད་པ་ཉིད་ཀྱི་ཁྱད་པར་ཡིན་པས་ཤེས་བྱའི་ཁྱད་པར་རོ། །ཤེས་བྱའི་མཚན་ཉིད་ནི་ཤེས་བྱའི་ངོ་བོ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཤེས་བྱའི་མཚན་ཉིད་ནི་ཤེས་བྱའི་མཚན་ཉིད་དེ་ངོ་བོ་ཉིད་གསུམ་མོ། །ཤེས་བྱའི་མཚན་ཉིད་དེ་ལ་ཇི་ལྟར་འཇུག་པར་འགྱུར་བའམ། གང་གིས་འཇུག་པར་འགྱུར་བ་སྟེ། རྣམ་པར་ཤེས་པ་ཙམ་མོ། །

[Block 66]
དེར་འཇུག་པ་ནི་དེ་ལ་འཇུག་པའོ། །

[Block 67]
འཇུག་པ་དེའི་རྒྱུ་དང་འབྲས་བུ་ཞེས་བྱ་བ་ལ་རྣམ་པར་ཤེས་པ་ཙམ་ལ་འཇུག་པ་ནི་འཇིག་རྟེན་པའི་སྦྱིན་པ་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སྦྱོར་བའི་དུས་སུ་ནི་རྒྱུའོ། །

[Block 68]
དེ་དག་ཉིད་མངོན་དུ་གྱུར་ཅིང་འཇིག་རྟེན་ལས་འདས་པར་གྱུར་པ་ནི་འབྲས་བུའོ། །

[Block 69]
དེའི་རྒྱུ་དང་འབྲས་བུའི་སྒོམ་པ་རབ་ཏུ་དབྱེ་བ་ཞེས་བྱ་བ་ལ། དེའི་རྒྱུ་དང་འབྲས་བུ་ཉིད་ནི་དེའི་རྒྱུ་དང་འབྲས་བུའོ། །

[Block 70]
དེའི་སྒོམ་པའི་རབ་ཏུ་དབྱེ་བ་ནི་སྒོམ་པ་གོམས་པ་སྟེ། དེའི་གོམས་པ་ནི་སའི་ཁྱད་པར་གང་ཡིན་པའོ། །

[Block 71]
དེའི་བྱ་བ་ནི་ཡང༌[^39]དག་པའོ། །

[Block 72]
སྒོམ་པ་རབ་ཏུ་དབྱེ་བ་དེ་ཉིད་ལ་ལྷག་པའི་ཚུལ་ཁྲིམས་ཞེས་བྱ་བ་ལ།[^40] ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་པའི་བསླབ་པ་ནི་ལྷག་པའི་ཚུལ་ཁྲིམས་ཏེ། བསླབ་པ་དེ་ཡང་བྱང་ཆུབ་སེམས་དཔའི་སྒོམ་པ་གང་མི་དགེ་བའི་ཆོས་མི་བྱེད་པའི་སེམས་སོ། །

[Block 73]
ལྷག་པའི་སེམས་ཞེས་བྱ་བ་ལ། ནང་གི་སེམས་ནི་ལྷག་པའི་སེམས་སོ།[^41] །སེམས་ཉིད་ཀྱི་དབང་དུ་བྱས་པའི་བསླབ་པ་ནི་ལྷག་པའི་སེམས་ཏེ་ཏིང་ངེ་འཛིན་ཏོ།[^42] །ལྷག་པའི་ཤེས་རབ་ཅེས་བྱ་བ་ལ། མངོན་པར་རྟོགས་པར་བྱེད་པའི་ཤེས་རབ་ནི་ལྷག་པའི་ཤེས་རབ་བམ། ཤེས་རབ་ཉིད་ཀྱི་དབང་དུ་བྱས་པའི་བསླབ་པ་ནི་ལྷག་པའི་ཤེས་རབ་སྟེ། དེ་ཡང་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་སོ། །

[Block 74]
སྤངས་པའི་ཁྱད་པར་ཞེས་བྱ་བ་ལ། ཁྱད་པར་དུ་འཕགས་པའམ། རབ་ཏུ་དབྱེ་བས་སམ། སོ་སོ་རང་གི་རིག་པས་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་པ་སྟེ། དེ་ཡང་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 75]
ཡེ་ཤེས་ཀྱི་ཁྱད་པར་གྱིས༌[^43]ཁྱད་པར་དུ་འཕགས་པའི་གསུང་ཞེས་བྱ་བ་ནི་སྒྲིབ་པ་དང་བྲལ་བའི་ཡེ་ཤེས་ཏེ། དེ་ཡང་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་རྗེས་སུ་མཐུན་པའོ།[^44] །སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ནི་སྒྲིབ་པ་ཐམས་ཅད་ཀྱི་བག་ཆགས་སྤངས་པ་སྟེ། འདི་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་དང་། ཡེ་ཤེས་ཀྱི་ཁྱད་པར་རོ། །
--- END BLOCKS ---
