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
སྔོན་གྱི་དུས་ན་བུམ་པ་དང་བུམ་པའི་འབྲས་བུ་མེད་དོ༌[^11]སྙམ་པའི་གཉེན་པོར་གླེང་གཞི་བསྙད་དོ། །

[Block 37]
གང་དུ་བྱ་བའི་ས་མི་ཤེས་པའི༌[^12]གཉེན༌[^13]པོར་གནས་བསྙད་དོ། །

[Block 38]
དུས་ཅི་ཙམ་ན་བྱ་བ་མི་ཤེས་པའི་གཉེན་པོར་དུས་བསྙད་དོ། །

[Block 39]
གང་ཟག་གང་གིས་བྱ་བ་མི་ཤེས་པའི་གཉེན་པོར་སློབ་དཔོན་བསྙད་དོ། །

[Block 40]
དེས་གང་ལ་བྱ་བ་མི་ཤེས་པའི་གཉེན་པོར་སློབ་མ་བསྙད་དོ། །

[Block 41]
རྫས་གང་ལ་བྱ་བ་མི་ཤེས་པའི་གཉེན་པོར་རྫས་བསྙད་དོ། །

[Block 42]
དེའང་གང་ལ་གང་གིས་བསྐུར་བ་མི་ཤེས་པའི་གཉེན་པོར་དབང་གི་རིམ་པ་བསྙད་དོ། །

[Block 43]
ཚུལ་ཇི་ལྟ་བུ་ཞིག་གིས་བསྐུར་བ་མི་ཤེས་པའི་གཉེན་པོར་ཐབས་བསྙད་དོ། །

[Block 44]
དེའང་གང་དུ་བསྐུར་བའི་ས་མི་ཤེས་པའི་གཉེན་པོར་གནས་བསྙད་དོ། །

[Block 45]
དེའི་དཀྱིལ་འཁོར་མི་ཤེས་པའི་གཉེན་པོར་དཀྱིལ་འཁོར་བསྙད་དོ། །

[Block 46]
དཀྱིལ་འཁོར་དུའང་ཐོག་མ་ནས་ཐ་མའི་བར་གྱི་ལས་མི་ཤེས་པའི་གཉེན་པོར་འཇུག་པའི་རིམ་པ་བསྙད་དོ། །

[Block 47]
དེའང་སྔོན་དུ་བྱ་བ་མི་ཤེས་པའི་གཉེན་པོར་ས་དང་སྟ་གོན་བཤད་དོ། །

[Block 48]
དེ་ལའང་རྟགས་ཇི་ལྟ་བུ་འབྱུང་བ་མི་ཤེས་པའི་གཉེན་པོར་རྟགས་བསྙད་དོ། །

[Block 49]
ཉན་ཐོས་དང་མུ་སྟེགས་ལ་སོགས་པས་ཐོས་ནས་ཉམས་པར་འགྱུར་བའི་ཕྱིར་བརྡ་བཤད་དོ། །

[Block 50]
བསམ་གཏན་མེད་ན་ནུས་པ་མི་འབྱུང་བས་བསམ་གཏན་བཤད་དོ། །

[Block 51]
དེས་བག་ཆགས་དྲི་མ་གང་འཁྲུ་བ་མི་ཤེས་པའི་གཉེན་པོར་ནུས་པ་བསྙད་དོ། །

[Block 52]
དེ་ལ་མན་ངག་གང་བསྟན་པ་མི༌[^14]ཤེས་པའི་གཉེན་པོར་དེ་དང་འབྲེལ་བའི་མན་ངག་བསྟན་ཏོ། །

[Block 53]
དེའང་ཚོགས་གང་དང་འབྲེལ་པ་མི་ཤེས་པའི་གཉེན་པོར་ཚོགས་ཀྱི་འབྲེལ་པ་བཤད་དོ། །

[Block 54]
དེའང་དངོས་གྲུབ་གང་དང་འབྲེལ་པ་མི་ཤེས་པའི་གཉེན་པོར་དངོས་གྲུབ་ཀྱི་འབྲེལ་པ་བསྙད་དོ། །

[Block 55]
དེས་འབྲས་བུ་ཇི་ལྟ་བུ་ཞིག་ཐོབ་པ་མི་ཤེས་པའི་གཉེན་པོར་འབྲས་བུ་བསྙད་དོ། །

[Block 56]
དེའང་རྣལ་འབྱོར་གང་ཡིན་པ་མི་ཤེས་པའི་གཉེན་པོར་རྣལ་འབྱོར་དངོས་བསྟན་ཏོ། །

[Block 57]
དེའང་རྒྱུ༌[^15]དང་སྦྱོར་བ༌[^16]མི་ཤེས་པའི་གཉེན་པོར་ཐུན་མོང་གི་སྦྱོར་བ་བསྟན༌[^17]ཏོ། །

[Block 58]
གང་ཟག་གང་ལ་བསྟན་པ༌[^18]མི་ཤེས་པའི་གཉེན་པོར་གང་ཟག་གི་དབྱེ་བ་བསྟན་ཏོ། །

[Block 59]
དེ་ལྟར་མདོར་བསྡུས་པ་བསྟན་ནས། ད་ནི་དེ་ཉིད་ཀྱི་མཚན་ཉིད་བཤད་པར་བྱ་སྟེ། དེ་ལ་ངོ་བོ་ཞེས་བྱ་བ་འང་གང་ཞིག་ཡིན་ཞེ་ན། འདི་ཡི་ངོ་བོ་ནུས་པ་སྟེ། །ཞེས་པ་གང་གིས་གང་ནུས་པ་དེ་ནུས་པའོ། །

[Block 60]
ནུས་པ་ཞེས་བྱ་བའང་ཅི་ཞིག་བྱེད་པ་ཡིན་ཞེ་ན། ས་ཐོབ་པ་དང་དྲི་མ་འཁྲུད་པར༌[^19]ནུས་པ་དེ༌[^20]ཉིད་ནུས་པའོ། །

[Block 61]
ནུས་པ་ཞེས་བྱ་བ་འདིའང་གཉིས་ཏེ། ས་བོན་དང་ཐོབ་པ་ཞེས་བརྟགས༌[^21]ན། རེ་ཞིག་ས་བོན་ནི་མ་ཡིན་ཏེ། སེམས་ཅན་ཐམས་ཅད་ལ་སྙིང་པོ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 62]
ཐོབ་པ་ཞེས་བྱ་བའང་འབྲས་བུ་མཆོག་དང་ཐུན་མོང༌[^22]གི་ཐོབ་པ་དེ་ནི་ཐོབ་པ་ཡིན་ན། འདི་ནི་དེ་མ་ཡིན་ནོ་ཞེ་ན། འདི་ནི་ཡིན་ཏེ། འདི་ལྟར་ས་བོན་ཁྱད་པར་ཅན་དུ་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 63]
ངེས་པའི་ཚིག་འདི་ཉིད་བཤད་པ། འདི་ཅིའི་ཕྱིར་བུམ་པའི་དབང་ཞེ་ན། འདིས་དངོས་གྲུབ་ཀྱི་བདག་པོར་བསྟབས་པའི་ཕྱིར་དང་། དྲི་མ་འཁྲུ་བར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་ཡང་ངོ་། །འོ་ན་རྡོ་རྗེ་ལ་སོགས་པ་འདི་ལ་ཅིའི་ཕྱིར་བུམ་པའི་དབང་ཞེས་གྲགས་ཤེ་ན། འདི་དག་ལའང་གནས་མཐུན་པ་ཉིད་དང་། ཐོབ་པ༌[^23]མཐུན་པ་ཉིད་དང་། སེལ་བ་མཐུན་པ་ཉིད་དང་། ཐམས་ཅད་ལས༌[^24]བུམ་པའི་ཆུས་འཁྲུ་བ་ཉིད་ཀྱི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 64]
དབྱེ་བའང་དུ་ཞིག་ཅེ་ན།

[Block 65 [VERSE]]
བུམ་པའི་དབང་ནི་རྣམ་པ་གསུམ། །
ཕྱི་དང་ནང་དང་སྦས་པའོ། །
དེ་ལྟར་རྣམ་པ་གསུམ་མོ། །

[Block 66]
ཕྱིའི་བུམ་པའི་དབང་གང་ཡིན་ཞེ་ན། གསེར་དངུལ་རྫས་བཅས་ཕྱི་ཡིན་ཏེ། །ཞེས་པ་ནི་རིན་པོ་ཆེ་སྣ་ལྔའི་བུམ་པ་ཐུན་མོང་གི་རྫས་དང་ལྡན་པ་ནི་ཕྱིའི་བུམ་པའོ། །

[Block 67]
ནང་གི་བདུད་རྩི་ལྔ་དང་ལྡན། །ཞེས་པ་ནི་ནང་གི་བུམ་པ་ནི་ཐུན་མོང་གི་རྫས་ཀྱི་སྟེང་དུ་བདུད་རྩི་ལྔ་བླུགས་ཏེ་བྱིན་གྱིས་བརླབས་པའོ། །

[Block 68]
སྦས་པའི་བུམ་པ་འདིའང་གང་ཡིན་དུ་ཞིག་ཅེ་ན། གཉིས་ཡོད་པའི་ཕྱིར།

[Block 69 [VERSE]]
སྦས་པ་དག་ནི་རྣམ་པ་གཉིས། །
ཐབས་དང་ཤེས་རབ་བུམ་པའོ། །
སྦས་པ་ཐབས་ཀྱི་བུམ་པ་ནི། །
བླ་མའི་ཁ་ནས་ཆུ་འབྱུང་བའོ། །

[Block 70]
སྦས་པ་ཤེས་རབ་བུམ་པ་ནི་ཤེས་རབ་མའི་པདྨ་ནས་ཆུ་འབྱུང་བའོ། །

[Block 71]
དེ་ལྟར་ཡང་གསུངས་པ།

[Block 72 [VERSE]]
བླ་མ་ཡི་ནི་ཐོད་རློན་ལ། །
རྣམ་ཤེས་ལྔ་ནི་སངས་རྒྱས་ཏེ། །
ཀླད་པ་བྱང་ཆུབ་སེམས་ཀྱི་ཆུ། །
དབང་པོ་ལྔ་དང་རྟེན་ལྔ་ནི། །

[Block 73 [VERSE]]
གང་དུ་སྨན་དང་འབྲུ༌[^25]ཞེས་བཤད། །
ཀླད་པའི་སྤྲིས་མ་རས་ཀྱིས༌[^26]དཀྲིས། །
སྐྲ་ནི་བུམ་པའི་ཁ་རྒྱན་ནོ། །
དེ་ཡི་ཁ་ནས་ཆུ་བྱུང་བ། །

[Block 74 [VERSE]]
ཡེ་ཤེས་བདུད་རྩི་དྲི་མ་མེད། །
ལུས་ཀྱི་སྡིག་པ་དག་པར་བྱེད། །
ཅེས་གསུངས་པ་དང་གཞན་ཡང་། །
ཤེས་རབ་ལུས་ཀྱི་བུམ་པ་ནི། །

[Block 75 [VERSE]]
བྱང་ཆུབ་སེམས་ཀྱི་ཆུས་བཀང་ནས། །
གསང་བའི་པདྨར་དབབ་བྱས་ཏེ། །
ཐབས་ཀྱི་རྡོ་རྗེ་དག་པར་བྱེད། །
--- END BLOCKS ---
