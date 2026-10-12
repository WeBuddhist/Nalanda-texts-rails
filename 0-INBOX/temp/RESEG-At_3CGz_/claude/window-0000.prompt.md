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
[Block 1 [HEADING]]
## ༄༅། །བྱང་ཆུབ་ལམ་གྱི་སྒྲོན་མའི་དཀའ་འགྲེལ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། བོ་དྷི་མཱརྒ་དཱི་པཾ་པཉྩི་ཀ་ནཱ་མ། བོད་སྐད་དུ། བྱང་ཆུབ་ལམ་གྱི་སྒྲོན་མའི་དཀའ་འགྲེལ་ཞེས་བྱ་བ།

[Block 4 [VERSE]]
འཕགས་མ་རྗེ་བཙུན་སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ལོ། །
འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལ་ཕྱག་འཚལ་ལོ། །
བདེ་མཆོག་འཁོར་ལོ་དམ་ཚིག་གསུམ་རྒྱལ་པོ། །
འཇིག་རྟེན་དབང་ཕྱུག་སྒྲོལ་མ་ཕྱག་འཚལ་འདུད། །

[Block 5 [VERSE]]
བྱམས་པ་ཐོགས་མེད་བླ་མ་གསེར་གླིང་པ། །
འཇམ་དབྱངས་ཞི་བའི་ལྷ་དང་བྱང་ཆུབ་བཟང་། །
བླ་མ་རྣམས་ལ་དང་བས་ཕྱག་བྱས་ནས། །
ཉི་ཟེར་ལྟ་བུའི་དཀའ་འགྲེལ་བྲི་བར་བྱ། །

[Block 6 [VERSE]]
བྱང་ཆུབ་སྙིང་པོར་བགྲོད་པའི་ལམ་བཟང་པོ། །
ཟླ་ཟེར་ལྟ་བུའི་ལམ་སྒྲོན་འདི་ཡིན་ཏེ། །
འདི་ན་ཅུང་ཟད་མི་གསལ་གང་ཡིན་པ། །
ཉི་ཟེར་ལྟ་བུའི་འགྲེལ་པས་ལམ་གསལ་བྱ། །

[Block 7 [VERSE]]
བསྟན་བཅོས་རྩོམ་པའི་ཚད་དང་མི་ལྡན་ཡང་། །
འདུན་ཅིང་གུས་པའི་སློབ་མས་བསྐུལ་བ་དང་། །
སངས་རྒྱས་བསྟན་པ་རབ་ཏུ་འཕེལ་བྱ་དང་། །
གཞུང་རྣམས་མི་མཐུན་རྩོད་པ་ཞི་བྱའི་ཕྱིར། །

[Block 8]
ཉི་ཟེར་ལྟ་བུའི་འགྲེལ་པ་བྲི་བར་བྱ། །

[Block 9 [VERSE]]
མཁས་རྣམས་ངོ་མཚར་བསྐྱེད་པ་དང་། །
མཉམ་རྣམས་གོ་བར་སླ་བ་དང་། །
དམན་རྣམས་བག་ཆགས་གཞག་པའི་ཕྱིར། །
དཀའ་འགྲེལ་འདི་ནི་བྲི་བར་བྱ། །

[Block 10 [VERSE]]
གཞུང་ཉུང་བ་ལ་དོན་མང་བའི། །
བསྟན་བཅོས་འདི་ནི་རྟོགས་པར་དཀའ། །
དམ་པ་རྣམས་དང་བྲལ་བས་ན། །
ཐམས་ཅད་དུ་ནི་རྣམ་པར་འཁོར། །

[Block 11 [VERSE]]
དེ་བས་སྐྱེས་བུ་བློ་ལྡན་པས། །
བླ་མ་ཡོངས་སུ་མཉེས་བྱས་ལ། །
བླ་མ་བརྒྱུད་རིམ་ལས་འོངས་པའི། །
ཡང་དག་མན་ངག་ཞུ་བར་བྱ། །

[Block 12]
འདིར་བླ་མ་དམ་པ་གསེར་གླིང་པ་དང་བླ་མ་དམ་པ་རྗེ་བཙུན་དཔལ་བྱང་ཆུབ་བཟང་པོའི་ཞལ་རིན་པོ་ཆེ་བུམ་པ་ལྟ་བུ་ནས། བདུད་རྩི་ལྟ་བུ་དང་། སྦྲང་རྩི་ལྟ་བུའི་མན་ངག་གི་ཐིགས་པ༌[^1]རྒྱལ་རིགས་ཀྱི་སློབ་མ་བྱང་ཆུབ་འོད་དང་། དུས་ཡུན་རིང་པོར་ཉེ་བར་བསྟན་པའི༌[^2]སློབ་མ་དགེ་སློང་ཚུལ་ཁྲིམས་རྒྱལ་བ་གཉིས་ཀྱིས་ཡང་དང་ཡང་དུ་གསོལ་བ་བཏབ་པའི་ངོར་མན་ངག་གི་ཐིགས་པ་འཐོར་བ་རྣམས་འདིར་བླ་མའི་ཞལ་སྔ་ནས་དང་། མདོ་སྡེ་ལ་སོགས་པའི་རྗེས་སུ་འབྲངས་ནས་བསྡུ་བར་བྱའོ། །

[Block 13 [VERSE]]
བྱང་ཆུབ་འོད་ཀྱིས༌[^3]དུས་རྟག་ཏུ། །
བདག་ལ་ཚིག་ནི་བདུན་དྲིས་པས། །
རྩ་བར་དོན་དེ་མ་གསལ་ཞེས། །
བསྐུལ་བའི་དོན་དུ་བྲི་བར་བྱ། །

[Block 14]
སྔོན་གྱི་སློབ་དཔོན་མཁས་པ་ཆེན་པོ་ནོར་གྱི་རྩ་ལག་གི་ཞལ་ནས།

[Block 15 [VERSE]]
མདོ་དོན་སྨྲ་བ་རྣམས་ལ་ནི། །
མན་ངག་ཅུང་ཟད་སྦྱིན་པར་བྱ། །
དགོས་པ་བཅས་དང་བསྡུས་དོན་བཅས། །
ཚིག་དོན་བཅས་དང་མཚམས་སྦྱོར་བཅས། །

[Block 16]
བརྒལ་ལན་བཅས་པས༌[^4]བསྙད་པར་བྱ། །ཞེས་བཤད་པས་འདིར་ཡང་ཤེས་རབ་དང་ལྡན་པ་དང་། བླ་མ་མཁས་པ་ལ་བརྟེན་པ་དག་གིས་ཚུལ་ཇི་ལྟ་བ་བཞིན་དུ་སྦྱར་བ་བྱས་ན་ཐེག་པ་ཆེན་པོའི་ལམ་བཟང་པོ་སྐྱེ་བོ་ཆེན་པོའི་ཆོས་ལུགས་ཤིང་རྟ་ཆེན་པོའི་ལམ་ཆེན་པོ་འདི་མྱུར་དུ་རྟོགས་པར་འགྱུར་རོ། །

[Block 17 [VERSE]]
མདོ་སོགས་ལུང་དང་བསྟན་བཅོས་དང་། །
བླ་མ་རྣམས་ཀྱི༌[^5]གསུང་བཞིན་དུ། །
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ལམ། །
བདག་གིས་ངེས་པར་བཤད་པར་བྱ། །

[Block 18]
དེ་གང་ཡིན་ཞེ་ན།

[Block 19 [VERSE]]
དུས་གསུམ་རྒྱལ་བ་ཐམས་ཅད་དག་དང་དེའི་ཆོས་དང་། །
དགེ་འདུན་རྣམས་ལ་གུས་པ་ཆེན་པོས་ཕྱག་བྱ་སྟེ། །
སློབ་མ་བཟང་པོ་བྱང་ཆུབ་འོད་ཀྱིས་བསྐུལ་གྱུར་པས། །
བྱང་ཆུབ་ལམ་གྱི་སྒྲོན་མ་རབ་ཏུ་གསལ་བར་བྱ། །

[Block 20]
ཞེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་འདི་ཡིན་ནོ། །

[Block 21]
གཞུང་དེ་དག་གང་ཡིན་ཞེ་ན། དུས་གསུམ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དུས་གསུམ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐང་པ་གཅིག་ནི་རྟོགས་པར་སླའོ། །

[Block 22]
སློབ་མ་བཟང་པོ་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོའི་ཆོས་ཀྱི་སྣོད་ཡིན་པས་སོ། །

[Block 23]
དེ་གང་ཡིན་ཞེ་ན། བྱང་ཆུབ་འོད་ཅེས་བྱ་བ་འདི་ཡིན་ནོ། །

[Block 24]
བསྐུལ་གྱུར་པས་ཞེས་བྱ་བ་ནི་དེས་བདག་ལ་འདི་སྐད་དུ། བོད་ཀྱི་ཡུལ་འདི་ན་སངས་རྒྱས་ཀྱི་བསྟན་པ་ཐེག་པ་ཆེན་པོའི་ལམ་འདི་ལ་ལོག་པར་རྟོག་པའི་གང་ཟག་བླ་མ་དགེ་བའི་བཤེས་གཉེན་གྱིས་ཡོངས་སུ་མ་ཟིན་པ་དག་ཕན་ཚུན་རྩོད་ཅིང་རང་རང་གི་རྟོག་གེས་ཟབ་པ་དང་རྒྱ་ཆེན་པོའི་དོན་ལ་རང་གི་རྟོག་པ་དཔྱོད༌[^6]ཅིང་སོ་སོ་ནས་མི་མཐུན་པ་དག་མང་དུ་མཆིས་པས་དེ་དག་ཐེ་ཚོམ་བསལ་དུ་གསོལ་ཞེས་བདག་ལ་ཡང་དང་ཡང་དུ་བསྐུལ་བར་གྱུར་པས། དེའི་དོན་དུ་བདག་གིས༌[^7]མདོ་ལ་སོགས་པའི་རྗེས་སུ་འབྲངས་ནས་བྱང་ཆུབ་ལམ་གྱི་སྒྲོན་མ་རབ་ཏུ་གསལ་བར་བྱའོ། །

[Block 25]
བྱང་ཆུབ་ལམ་གྱི་སྒྲོན་མ་དེ་གང་ཡིན་ཞེ་ན། སེམས་ཅན་དམ་པ་བྱང་ཆུབ་མཆོག །ཅེས་བྱ་བ་ནས། དེ་ཉིད་རིག༌[^8]ལ་ཉེས་པ་མེད། །ཅེས་པའི་བར་གྱི་གཞུང་འདི༌[^9]ཡིན་ནོ། །

[Block 26]
དེ་ལ་ཆུང་དང་ཞེས་པ་ནས་མཆོག་ཡིན་ནོ་ཞེས་པའི་གཞུང་གིས་ཐེག་པ་ཆེན་པོའི་སྣོད་དང་སྣོད་མ་ཡིན་པ་བསྟན་ཏེ། སྐྱེས་བུ་ཐ་མ་དང་། སྐྱེས་བུ་འབྲིང་ནི་ཞར་ལ་བཤད་པ་ཡིན་ནོ། །

[Block 27 [VERSE]]
ཚིག་དོན་རྣམས་ནི་རྟོགས་པར་སླའོ། །
རང་རྒྱུད་གཏོགས་པའི་སྡུག་བསྔལ་གྱིས། །
གང་ཞིག་གཞན་གྱི་སྡུག་བསྔལ་ཀུན། །
ཡང་དག་ཟད་པར་ཀུན་ནས་འདོད། །
སྐྱེས་བུ་དེ་ནི་མཆོག་ཡིན་ནོ། །

[Block 28]
ཞེས་པས་ནི་ཐེག་པ་ཆེན་པོའི་སྣོད་བསྟན་པ་ཡིན་ནོ། །

[Block 29]
དོན་འདི་ལ་དགོངས་ནས་ཇི་སྐད་དུ།

[Block 30 [VERSE]]
བྱང་ཆུབ་སེམས་དཔའ་སེམས་ཅན་ལ། །
བུ་གཅིག་པ་ལ་བྱ་བ་བཞིན། །
རྐང་གི༌[^10]གཏིང་ནས་བྱམས་པ་སྟེ། །
དེ་ལྟར་རྟག་ཏུ་བྱེད་པར་འདོད། །

[Block 31 [VERSE]]
ཡང་ཇི་ལྟར་ཕུག་རོན་རང་གི་བུ་མཆོག་བྱམས། །
རང་གི་བུ་དེ་པང་ན་འཁྱུད་ནས་འདུག །
དེ་འདྲ་བ་ལ་ཁོང་ཁྲོ་འགལ་བ་ལྟར། །
བརྩེར་བཅས་ལུས་ཅན་བུ་ལའང༌[^11]དེ་དང་འདྲ། །

[Block 32]
ཞེས་གསུངས་པ་དང་། སློབ་དཔོན་མཁས་པ་ཆེན་པོ་ནོར་གྱི་རྩ་ལག་གིས་ཀྱང་ཇི་སྐད་དུ། དམན་པ་དེ་དང་དེའི་ཐབས་ཀྱིས༌[^12]རང་གི་རྒྱུད་དུ་གཏོགས་པའི་བདེ་བ་དོན་དུ་གཉེར། །འབྲིང་པོ་སྡུག་བསྔལ་ལྡོག་པ་ཁོ་ནའོ་བདེ་མིན་གང་ཕྱིར་དེ་ནི་སྡུག་བསྔལ་གནས་ཡིན་ཕྱིར། །དམ་པ་རང་གི་རྒྱུད་ལ་ཡོད་པའི་སྡུག་བསྔལ་རྣམས་ཀྱིས་གཞན་དག་ལ་ནི་བདེ་བ་དང་། །སྡུག་བསྔལ་གཏན་ལྡོག་ཁོ་ན་དོན་གཉེར་གང་ཕྱིར་དེ་ཡི་སྡུག་བསྔལ་གྱིས་དེ་སྡུག་བསྔལ་ཕྱིར། །ཞེས་གསུངས་པ་དང་། ཡང་གང་གཞན་གྱི་སྡུག་བསྔལ་གྱིས༌[^13]སྡུག་བསྔལ་བར་འགྱུར་ཞིང་། གཞན་གྱི་བདེ་བས་ཡིད་བདེ་ཞིང་དགའ་བར་འགྱུར་གྱི། བདག་གི་ནི་མ་ཡིན་པ་དེ་ལྟ་བུའི་རིགས་ཅན་ལ་ཡིན་ཏེ། དེ་དག་ནི་རང་གི་བདེ་བ་ལ་མི་ལྟ་བ་དང་། དེ་དག་ནི་གཞན་དག་སྡུག་བསྔལ་གྱི་ཆུ་བོ་ཆེན་པོ་ལས་ཡོངས་སུ་བསྐྱབ་པར་ནུས་སོ་སྙམ་དུ་འབད་པ་བྱེད་དོ། །

[Block 33]
རང་བཞིན་གྱིས་སྙིང་རྗེ་ཆེ་བ་དག་ནི་སྙིང་རྗེ་ལ་གོམས་པའི་སྟོབས་ཀྱིས་རང་སྡུག་བསྔལ་ཡང་གཞན་བདེ་བ་ལ་མངོན་པར་དགའ་བ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 34]
དེ་བས་ན་སྐྱེས་བུ་གང་ཞིག་རང་བཞིན་གྱིས་ཕ་རོལ་པོ་ཉམ༌[^14]ཐག་པ་དག་མཐོང་ན་མི་བཟོད་ཅིང་བདག་དང་གཞན་བརྗེ་བར༌[^15]སེམས་ཤིང་བུ་གཅིག་པ་གཡང་སར་ལྷུང་བ་དང་། ཆུ་བོ་ཆེན་པོས་ཁྱེར་བ་དང་། མེ་འབར་བའི་ནང་དུ་འདུག་པ་མཐོང་བ་ན་དེ་མི་བཟོད་པ་བཞིན་དུ། འགྲོ་བ་མཐའ་དག་ལ་བུ་གཅིག་པ་ལྟར་ལྟ་བ་དེ་ནི་འདིར་ཐེག་པ་ཆེན་པོའི་སྣོད་དུ་བསྔགས་སོ། །

[Block 35]
དེ་ལྟ་བུའི་སེམས་ཅན་ཆེན་པོ་དེ་ལ་ཇི་ལྟར་བྱ་སྙམ་པ་ལ།

[Block 36 [VERSE]]
བླ་མ་རྣམས་ཀྱིས་བསྟན་པ་ཡིས། །
ཡང་དག་ཐབས་ནི་བསྟན་པར་བྱ། །

[Block 37]
ཞེས་བྱ་བ་ནི་འདི་ཡིན་ནོ། །

[Block 38]
དེ་ལ་བླ་མ་རྣམས་ནི་རྗེ་བཙུན་དཔལ་བྱང་ཆུབ་བཟང་པོ་དང་། རྗེ་བཙུན་སུ་ཝརྞྞ་དྭཱི་པ་ལ་སོགས་པའོ། །

[Block 39]
ཡང་དག་ཐབས་ཞེས་བྱ་བ་ནི། གསུམ་ལ་སྐྱབས་སུ་འགྲོ་བ་དང་། བྱང་ཆུབ་ཀྱི་སེམས་རྣམ་པ་གཉིས་དང་། མངོན་པར་ཤེས་པ་བསྐྱེད་ནས་གཞན་དོན་ཁྱད་པར་ཅན་བྱ་བའི་ཐབས་དང་། ཐབས་དང་ཤེས་རབ་ཟུང་དུ་འབྲེལ་བའི་ཚོགས་གཉིས་བསག་པའི༌[^16]ཐབས་དང་། བདག་དང་གཞན་དོན་མྱུར་དུ་རྫོགས་པར་འགྱུར་བའི་ཐེག་པ་ཆེན་པོའི་ཆེན་པོ་གསང་སྔགས་ཀྱི་ལུགས་ཀྱི༌[^17]ཐུན་མོང་མ་ཡིན་པའི་ཚོགས་གཉིས་བསགས་པའི་ཐབས་རྣམས་སོ། །

[Block 40]
དེ་ལྟ་བུའི་ཐབས་དེ་དག་རྒྱས་པར་བཤད་པར་འདོད་ནས། རྫོགས་སངས་བྲིས་སྐུ་ལ་སོགས་དང་། །ཞེས་པ་ནས། དེ་ཉིད་རིག་ལ་ཉེས་པ་མེད་པའི་བར་རོ། །
--- END BLOCKS ---
