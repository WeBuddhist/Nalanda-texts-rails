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
དེ་སྐད་དུ་ཡང་སློབ་དཔོན་ཕྱོགས་ཀྱི་གླང་པོས། །

[Block 37 [VERSE]]
དད་ལྡན་འཇུག་པའི་ཡན་ལག་ཏུ། །
རང་ཉིད་ཚད་མར་རབ་བསྒྲུབ་ཕྱིར། །
སྟོན་པ་དང་ནི་འཁོར་དབང་པོ། །
ཡུལ་དང་དུས་སོགས་བསྟན་པ་ཡིན། །

[Block 38 [VERSE]]
སྡུད་པར་བྱེད་པས་འཇིག་རྟེན་དུ། །
ཡུལ་དང་དུས་སོགས་བསྟན་པ་ནི། །
དཔང་པོར་བཅས་པའི་ཚིག་བརྗོད་ན། །
རང་ཉིད་ཚད་མར་འགྲོ་བ་ཡིན། །

[Block 39]
ཞེས་གསུངས་སོ། །

[Block 40]
འདི་རྣམས་ཀྱི་ཚིག་དོན་དང་ཚིག་རྣམ་པར་སྦྱར་བ་ནི་གསལ་ལོ། །

[Block 41]
དེས་ན་མདོ་ཐམས་ཅད་དེ་ལྟར་བཤད་པར་བྱ་བ་ཡིན་པར་བརྒྱད་སྟོང་པའི་བསྡུས་དོན་ན༌[^10]བསྟན་ཏོ། །

[Block 42]
ལྷག་མ་ནི་མཐུན་ནོ། །

[Block 43 [HEADING]]
## རང་གི་ལུགས་གསལ་བར་བྱེད་པ། ^2-0

[Block 44 [HEADING]]
### དང་པོ་སུན་འབྱིན། ^2-1-0

[Block 45]
འདིར་དྲི་མ་མེད་པའི་བཤེས་གཉེན་གྱིས་དེ་བཀག་སྟེ། རང་གི་ལུགས་གསལ་བར་བྱེད་པ་ལ་དང་པོ་སུན་འབྱིན་ཏེ། དེ་ལ༌[^11]སྐྱོན་གཉིས་ཏེ། མི་ནུས་པ་དང་དཔང་པོར་མི་འགྱུར་བའོ། །

[Block 46 [HEADING]]
#### མི་ནུས་པ། ^2-1-1-0

[Block 47]
དེ་ལ་མི་ནུས་པ་ནི༌[^12]དགོས་པ་དེ་སྒྲུབ་པར་མི་ནུས་པ་སྟེ། ད་ལྟ་ནི་དད་པས་རྗེས་སུ་འབྲང་བ་རྣམས་འཇུག་པའི་ཡན་ལག་ཏུ་རང་ཚད་མའི་སྐྱེས་བུར་བསྒྲུབ་པའི་ཕྱིར་དེ་སྨོས་སོ། །

[Block 48]
དཔང་པོའི་དགོས་པ་ཡང་ཕྱིས་དེ་ལ་ཐེ་ཚོམ་ཟ་བ་ལ་སོགས་པ་བྱུང་ཙམ་ན། དེ་ལ་ཐུག་པ་ཡིན་ལ། དེ་ལྟར་ན་རྫུ་འཕྲུལ་དང་མངོན་པར་ཤེས་པ་ཐོབ་པ་རྣམས་ཀྱིས་མདོའི་དོན་གཏན་ལ་འབེབས་པ་མི་སྲིད་པར་འགྱུར་ཏེ། དཔང་པོ་འགའ་ཞིག་ནི་མྱ་ངན་ལས་འདས་ལ། ཁ་ཅིག་གཞན་ན་བཞུགས་པ་སྟེ། དེ་ཡང་།

[Block 49 [VERSE]]
ཟབ་ཅིང་མཐའ་ཡས་མདོ་སྡེ་ཡི། །
དཀོན་མཆོག་ཐོས་པའི་སྲེད་པ་ཡིས། །
འཇིག་རྟེན་ཁམས་ནི་ཐམས་ཅད་དུ། །
དོན་བྱེད་པར་ནི་འགྲོ་ཕྱིར་ཏེ། །

[Block 50]
ཞེས་བྱ་བའི་ཚུལ་གྱིས་སོ། །

[Block 51]
ཁ་ཅིག་ནི་འདི་ན་བཞུགས་ཀྱང་མཐོང་བའི་སྐལ་བ་མེད་དོ།[^13] །

[Block 52]
འོད་སྲུངས་ཆེན་པོ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 53 [HEADING]]
#### དཔང་པོར་མི་འགྱུར་བ། ^2-1-2-0

[Block 54]
སྐྱོན་གཉིས་པ་དེ་དགོས་པ་དེ་བསྒྲུབ་པར་ནུས་སུ་ཆུག་ཀྱང་དཔང་པོ་ཉིད་དུ་མི་འགྱུར་ཏེ། །དཔང་པོར་འགྱུར་བ་ལ་འདི་དང་འདི་དག་སྟེ་ཞེས་འཁོར་རྣམས་ཀྱི་མིང་བསྟན་པས་དཔང་པོར་འགྱུར་བར་འདོད་ན། རབ་འབྱོར་དང་ཞེས་བྱ་བ་ལ༌[^14]སོགས་པ་དངོས་སུ་མིང་བསྟན་པས༌[^15]དེ་ལྟར་དཔང་དུ་འགྱུར་བ་ལ་རག་ན། མདོ་འདི་བཞིན་དུ་འཁོར་གྱི་མིང་མེད་པ་དང་དཔང་དུ་ཇི་ལྟར་འགྱུར་ཞེས་ཟེར་རོ། །

[Block 55]
དེས་ན་འདི་ལྟར་བཤད་དེ། སྔོན་བྱུང་བའི་གླེང་གཞི་དང་བཅས་པའི་མདོ་བཤད་པའི་སྔོན་རོལ་དུ་དེའི་གླེང་སློང་བར་བྱེད་པ་ནི་འདི་སྐད་བདག་གིས་ཐོས་པའི༌[^16]གསུངས་པ་ཡིན་ནོ། །

[Block 56]
འདིས་ནི་དབྲི་བསྐྱུངས་མེད་པར་ཡང་དག་པར་ཐོས་པར་བསྟན་ཏེ། དེས་འཁོར་རྣམས་ཀྱིས་ཕྱིན་ཅི་མ་ལོག་པར་བསྟན་པར་ཤེས་པས་སྡུད་པ་པོ་ལ་ལེགས་པར་རྣ་བ་གཏོད་པ་ལ་སོགས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 57]
ད་ནི་གང་ལ་བརྟེན་ནས་མདོ་འདི་འབྱུང་བའི་སྐབས་སུ་གྱུར་པའི་གནས་སྐབས་དེ་རྩོམ་པ་སྟེ། དེ་ལ་འཇུག་པར་བྱེད་པ་ནི་དུས་གཅིག་ན་བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 58]
འོ་ན་སྐབས་དེ་ལྟ་བུ་ལ་བརྟེན་ནས་བྱུང་བའི་མདོའི་དབང་དུ་བྱས་པའི་གང་ཟག་ཇི་ལྟ་བུ་ཡིན་སྙམ་ནས་བསྟན་པར་གཏོགས་པ་འདུས་པ་སྟེ། དགེ་སློང་གི་དགེ་འདུན་ཆེན་པོ་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཆོས་ཉན༌[^17]པའི་སྐལ་པ༌[^18]ཡོད་པ་ཚོགས་པ་དང་ལྡན༌[^19]པར་གཏོགས་པ་འདུས་པ་ཞེས་བྱའོ། །

[Block 59]
ཁྱད་པར་གྱི་གླེང་གཞི་གང་ཞེ་ན། དེའི་ཚེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གཙོ་བོ་དང་འཁོར་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་པ་གཉིས་བསྟན་ཏོ། །

[Block 60 [HEADING]]
## མདོ་དངོས། ^3-0

[Block 61]
འོ་ན་གླེང་གཞི་དེ་གཉིས་རྒྱུར་བྱས་པ་ལས་རྩོམ་པ་འབྱུང་བའི་མདོ་གང་ཞེ་ན། དྲིས་པ་དང་ལན་གཉིས་ཀྱིས་སྟོན་པ་ནི་དེ་ནས་ཞེས་བྱ་བ་ནས་དེ་ལྟར་བསླབ་པར་བྱ་བའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 62]
འོ་ན་དེ་དེ་བཞིན་གཤེགས་པས་མ་གསུངས་པར་སྤྱན་རས་གཟིགས་ཀྱིས་བཤད་པ་འདི་ཅང་ཡིན་ནམ་སྙམ་པའི་འཁོར་གྱི་ལོག་རྟོག་བཟློག་པའི་ཕྱིར་ཤཱཀྱ་ཐུབ་པ་ཉིད་ཀྱིས་མཐུན་འགྱུར་བྱིན་པའོ། །

[Block 63]
འོ་ན་འདི་ཡང་སྙིགས་མ་ལྔ་བདོ་བའི་དུས་སུ་སངས་རྒྱས་པས། སངས་རྒྱས་གཞན་པས་འོད་ལ་སོགས་པ་ཆུང་བས་དེ་ཁོ་ན་ལྟར་ཡིན་ནམ་མ་ཡིན་ནམ༌[^20]སྙམ་པ་ལ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱང་རྗེས་སུ་ཡི་རང་ངོ་ཞེས་བྱ་བ༌[^21]དེ་ཁོ་ན་ལྟར་ཟད་དོ་སྙམ་དུ་དགོངས་པའོ། །

[Block 64]
འདི་གཉིས་ནི་མཐུན་འགྱུར་རོ། །

[Block 65]
ཡང་ན་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱང་ཞེས་བྱ་བས་ནི་རྗེས་སུ་ཡི་རང་བ་དང་སྦྱར་རོ། །

[Block 66]
དེ་ལྟར་ན་མདོ་སྡེ་རིན་པོ་ཆེ་བཤད་པ་ལ་དགའ་བ་སྐྱེས་ནས་རྗེས་སུ་ཡི་རང་བར་བྱེད་པ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 67]
དེ་ནི་སྤྱིའི་དོན་བསྡུས་པ་ཙམ་མོ། །

[Block 68 [HEADING]]
### དྲིས་པ། ^3-1-0

[Block 69]
དེ་ལ་དྲིས་པ་ནི་དེ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 70]
འདིའི་དོན་ནི་རྟེན་གྱི་གང་ཟག་གང་ལ་ལ་འདོད་པ་སྟེ། བྱེ་བྲག་སྒྲུབ་པ༌[^22]དང༌[^23]སེམས་བསྐྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 71]
ཇི་ལྟར་བསླབ་པར་བྱ་བ་སྟེ། ཚོགས་ལམ་དང་། སྦྱོར་ལམ་དང་། མཐོང་ལམ་དང་། བསྒོམ་ལམ་དང་། མི་སློབ་པ་ལའོ། །

[Block 72]
འདི་ལྔ་ཡང་བསམ་པ་དང་། སྦྱོར་བ་དང་། མངོན་དུ་བྱ་བ་དང་། སྒྲུབ་པ་དང་། རྟོགས་པ་ཞེས་བྱ་བ་རྣམས་ཀྱི་རང་བཞིན་ནོ། །

[Block 73]
དེ་ལ་གདམས་ངག་ནི་འདི་ཡིན་ཏེ། རིགས་དང་ལྡན་པའི་གང་ཟག་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པས་ལམ་ལྔ་ལ་ཇི་ལྟར་བསླབ་པར་བྱ་ཞེས་དྲིས་པའི་དོན་ཏོ། །

[Block 74 [HEADING]]
### ལན། ^3-2-0

[Block 75]
ལན་ནི་ལམ་རྣམ་པ་ལྔ་ལ་རྣམ་པར་ཕྱེ་ནས་བསྟན་པས་བཅུ་གཅིག་ཏུ་འགྱུར་རོ། །
--- END BLOCKS ---
