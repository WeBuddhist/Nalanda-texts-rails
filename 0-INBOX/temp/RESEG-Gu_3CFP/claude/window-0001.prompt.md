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
འདིས་འཛིན་པར་བྱེད་པས་ན་རྟེན་ཏེ། གང་གི་ཕྱིར་བརྟེན་པ༌[^18]ལ་ལྟོས་ནས་རྟེན་ཉིད་ཡིན་ན། གང་གི་རྟེན་ཡིན་ཞེས་བརྟེན་པ་འདྲི་བས། དེ་ལྟ་བས་ན་སྐལ་བ་དང་ལྡན་པ་ཞེས་སྨྲས་སོ། །

[Block 37]
དེ་བཞིན་དུ་གཞན་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 38]
ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཡོངས་སུ་རྫོགས་ཞེས་ཅིའི་ཕྱིར་བརྗོད། འདི་ལྟར་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་འཐོབ༌[^19]ཅེས་མི་བརྗོད་ཅེ་ན། རྣམ་པ་ཐམས་ཅད་ཤིན་ཏུ་གནས་གྱུར་པའི་མཚན་ཉིད་ཅན་ནི་བྱང་ཆུབ་ཡིན་ལ། སྦྱིན་པ་ལ་སོགས་པའི་སྦྱོར་བ་ཙམ་གྱིས་ནི་མི་ཐོབ་བོ། །

[Block 39]
འོན་ཀྱང་སྦྱིན་པ་ལ་སོགས་པའི་རིམ་གྱིས་གང་གློ་བུར་པའི་དྲི་མ་བསལ་ནས། མཐར་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ལ་ཡང་དག་པར་བརྟེན་པའི་ལམ་ནི་བྱང་ཆུབ་བོ། །

[Block 40]
གང་ཟག་རིགས་ལ་གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའི༌[^20]གཞུང་གིས་ཅི་ཞིག་བསྟན། རིགས་ལ་གནས༌[^21]པའི་རྟེན་རྣམས་ཡོད་ན་ཡང་རིགས་ཉིད་གཙོར་བརྟེན༌[^22]ཞེས་རབ་ཏུ་བསྟན་ཏེ། རིགས་མེད་ན་གཞན་ཡོད་ན་ཡང་རྣམ་པ་ཐམས་ཅད་དུ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བ་མེད་པ་ཉིད་ཡིན་ལ། རིགས་ཡོད་ན་ནི་དུས་གཞན་ན་སེམས་བསྐྱེད་པ་ལ་སོགས་པ་བྱས་ནས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བའི་ཕྱིར་རོ། །

[Block 41]
རིགས་ཇི་ལྟ་བ༌[^23]བཞིན་དུ་དང་པོ་སེམས་བསྐྱེད་པ་དང་། བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ཐམས་ཅད་ཀྱང་དེ་བཞིན་ནོ། །

[Block 42]
ཅི་ལྟར་རིགས་ལ་གཞི་ཞེས་བརྗོད་ཅིང་ཉེ་བར་རྟོག་པ༌[^24]ལ་སོགས་པ་བརྗོད་པ་ལྟར།

[Block 43]
དང་པོ་སེམས་བསྐྱེད་པ་ལ་ཡང་གཞི་དང་རྟོག་པ༌[^25]ལ་སོགས་པར་བརྗོད་དོ། །

[Block 44]
དེ་ལ་ཡང་རིགས་ཞེས་བྱ་བ་ནི། རང་བཞིན་གྱིས་གནས་པའི་རིགས་སོ། །

[Block 45]
འབྲས་བུ་མེད་པས་ཆ་ཕྲ་བ་ཞེས་བྱ་བ་ནི། འབྲས་བུ་མི་དམིགས་པའི་དོན་ཏོ།[^26] །འབྲས་བུ་ལ་ལྟོས་ནས་རིགས་ཡོད་པར་ཤེས་ཀྱི་གཞན་དག་ཏུ་ནི་མ་ཡིན་ནོ། །

[Block 46]
བདག་ལ་ཕན་པའི་ཕྱིར་ཞུགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། དགེ་བ་ལ་སྤྱོད་པ་ནི་ཕན་པ་ཞེས་བརྗོད་དོ། །

[Block 47]
བདེ་བ་ནི་གནོད་པ་མ་ཡིན་པའོ། །

[Block 48]
སྙིང་བརྩེ་བ་ནི་འདི་ན་ལ་ལ་མི་གནོད་པའི་དགེ་བ་ལ་སྤྱོད་པས་གཞན་དག་ལ་བརྩེ་བའོ། །

[Block 49]
འདོད་པར་བྱ་བ་ཉིད་དང་དོན་དང་ལྡན་པ་ཉིད་ཀྱིས་དོན་ཡིན་ལ་གང་འདོད་པར་བྱ་བ་ཉིད་དང་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཉིད་ཀྱིས་ཕན་པ་དང་བདེ་བའོ། །

[Block 50]
གང་དག་དགེ་བ༌[^27]སྤྱོད་པ་ལ་འཇུག་པ་རྣམས་ནི་མི་སྟེ། རྒྱལ་རིགས་ལ་སོགས་པའོ། །

[Block 51]
གང་དག་སངས་རྒྱས་འབྱུང་བ་དང་། ལེགས་པར་གསུངས་པའི་ཆོས་དང་། ལེགས་པར་སྤྱོད་པའི་དགེ་འདུན་ལ་མང་དུ་ཞུགས་པས་ཕན་པ་འབྱུང་བར་འགྱུར། བདེ་བ་འབྱུང་བར་འགྱུར་ཞེས་གསུངས་སོ། །

[Block 52]
ཡང་དེ་ནི་བདག་ལ་ཕན་པ་དང་བདེ་བ་བྱས་ནས་འཇིག་རྟེན་ལ་སྙིང་བརྩེ་བས། འདི་སྙམ་དུ་སེམས་པར་འགྱུར་ཏེ། ཇི་ལྟར་གཞན་དག་ལ་ཕན་པ་དང་།

[Block 53 [VERSE]]
བདེ་བ་དང་ལྡན་པར་བྱ་སྙམ་མོ། །
གཞན་དག་ཀྱང་འདི་སྙམ་དུ་སེམས་ཏེ།
ཇི་ལྟར་བདག་ཀྱང་འདི་ལྟར་འགྱུར་སྙམ་མོ། །

[Block 54]
དེས་ན་དོན་དང་ཕན་པ་དང་བདེ་བ་ཞེས་བྱའོ། །

[Block 55]
ལྷ་དང་མི་རྣམས་ཞེས་བྱ་བ་ནི། དོན་ཤེས་པ་དང་། བསྒྲུབ་པ་ལ་ནུས་པ་དང་ལྡན་པས་ལྷ་དང་མིའོ། །

[Block 56]
སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རིགས་ཀྱི་རྟགས་ནི་མདོར་བསྡུ་ན་རྣམ་པ་གསུམ་སྟེ། ཟང་ཟིང་གི་སྦྱིན་པ་དང་། ཆོས་ཀྱི་སྦྱིན་པ་དང་། མི་འཇིགས་པའི་སྦྱིན་པའོ། །

[Block 57]
སྦྱིན་པའི་རྟགས་གསུམ་པོ་དེ་རྣམས་ལས།

[Block 58]
དེ་ལ་རེ་ཞིག་དང་པོར་ཟང་ཟིང་གི་སྦྱིན་པའི་རྟགས་ནི་ཡོད་ཅིང་བདོག་པ་ནི་རྟགས་གསུམ་སྟེ། སྦྱིན་པའི་བདག་ཉིད་ཅན་དང་། སྦྱིན་འདོད་པའི་བསམ་པ་ཉིད་དང་། རྟག་ཏུ་རྒྱུན་མི་འཆད་པར་བགོ་བཤའ༌[^28]བྱེད་པའི་ངང་ཚུལ་ཅན་དང་། སྦྱིན་པའི་དུས་སུ་རབ་ཏུ་དགའ་བའི་སེམས་ཀྱིས་སྟེར་བའོ། །

[Block 59]
མེད་ཅིང་མི་བདོག་ན་ཡང་ཆུང་ན་ཡང་བགོ་བཤའ་བྱེད་པ་དང་། བསམ་པ་ནི་སྦྱིན་པར་བྱ་བའམ༌[^29]མི་སྦྱིན་ཞེས་སེམས་དང་འཐབ་མོ་བྱས་ན༌[^30]སྦྱིན་པ་མ་ཡིན། དེ་བཞིན་སེར་སྣའི་ཕྱོགས་ཀྱི་གཉེན་པོ་དང་། རྒུད་པའི་གཉེན་པོས་སྦྱིན་པ་ནི་ངོ་ཚའོ་ཞེས་དེ་ལྟར་རེ་ཞིག་སྦྱིན་པ་ལ་བདག་ཉིད་སྒྲུབ་པའོ། །

[Block 60]
གཞན་ལ་སྒྲུབ་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། གཞན་སྦྱིན་པ་ལ་མ་ཞུགས་པ་ལ་སྒྲུབ་པ༌[^31]དང་། སྦྱིན་པ་ལ་ཞུགས་པ་ལ་སྒྲུབ་པའོ། །

[Block 61]
སྦྱིན་པ་ལ་མ་ཞུགས་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། སྦྱིན་པའི་ཕན་ཡོན་མི་ཤེས་པའི་སྐྱེ་བོ་རྨོངས་པ་དང་། བག་མེད་ཅིང་ཞུམ་པ་སྟེ། རྨོངས་པ་རྣམས་ལ་བསྟན་པ་དང་། བག་མེད་པའི་ངང་ཚུལ་ཅན་རྣམས་ཉེ་བར་འདུན་པར་བྱའོ།[^32] །

[Block 62]
ཡང་དག་པར་ཞུགས་པ་རྣམས་ལ་ཡིད་དགའ་བ་དང་ཡིད་བདེ་བ་སྟེ། སྦྱིན་པ་པོ་ལ་ནི་ཡིད་དགའ་ལ། སྦྱིན་པ་ལ་རྗེས་སུ་ཡི་རང་བ་ནི་ཡིད་བདེ་བའོ། །

[Block 63]
ཆོས་ཀྱི་སྦྱིན་པ་ལས་བརྩམས་ནས་བསྟན་པ་བླ་མ་རྣམས་ཞེས་བྱ་བ་དེ་ལ། ཆོས་ཀྱི་ཕྱིར་སྦྱིན་པའམ། ཆོས་སྦྱིན་པའོ། །

[Block 64]
དེ་ལ་ཆོས་ཀྱི་ཕྱིར་སྦྱིན་པའི་དབང་དུ་བྱས་ནས་བླ་མ་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་དེ་ལ། མཁན་པོ་དང་སློབ་དཔོན་ནི་ཕ་མའོ། །

[Block 65]
རྒན་རབས་ནི་གང་རབ་ཏུ་བྱུང་བ་ཚངས་པ་མཚུངས་པར་སྤྱོད་པའམ་ལོས་རྒན་པའོ། །

[Block 66]
ཡོན་གནས་ནི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 67]
བཀུར་སྟི་བྱ་བར་འོས་པ་ནི་ཡོན་ཏན་དང་ལྡན་པའི་བྱེ་བྲག་གམ། ཡང་ན་གཞན་ཡང་བཀུར་སྟི་བྱ་བར་འོས་པའོ། །

[Block 68]
ཆོས་ཀྱི༌[^33]སྦྱིན་པའི་དབང་དུ་བྱས་ནས། དྲིས་ཀྱང་རུང་མ་དྲིས་ཀྱང་རུང་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 69]
མི་འཇིགས་པ༌[^34]སྦྱིན་པའི་དབང་དུ་བྱས་ནས་བསྟན་པ་ནི། རྒྱལ་པོ་དང་དགྲ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏེ། མི་འཇིགས་པ་ལ༌[^35]རྗེས་སུ་སྦྱིན་པ་ལུས་སམ་ངག་གིས་བདག་གི་དངོས་པོ་ཉམས་པ་ལས་ཡོངས་སུ་བསྲུང་བའོ། །

[Block 70]
ལོངས་སྤྱོད་ཉམས་པ་ལ་མི་འཇིགས་པ་སྦྱིན་པ་ནི། གཏམས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། འཇིགས་ནས་ཕ་རོལ་རང་གིས་གཞག་པའམ་བདག་གིས་སྐྱིན་པོར་བླངས་པ་ལ་སླུ་བར༌[^36]མི་བྱེད་དེ། དེ་ཇི་ལྟར་ཆད་པའི་སྐྱེད་དང་བཅས་པར་སྦྱིན་གྱི་དོར་ཡང་མི་བྱེད་ལ། འབྲོས་པར་ཡང་མི་བྱེད་དོ། །

[Block 71]
རང་གི་རིགས་རྒྱུད་ལ་ཡང་ཞེས་བྱ་བ་ནི་གཉིས་ཀྱི་ཕན་ཚུན་ནོ། །

[Block 72]
ནོར་བུ་དང་མུ་ཏིག་དང་བཻ་ཌཱུརྱ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཚོང་པ་རྣམས་ཀྱི་ཐ་སྙད་དུ་བྱ་བའོ། །

[Block 73]
ལོངས་སྤྱོད་དང་ཞུགས་པ་དང་སྦྱིན་པའི་སེམས་གསུམ་དུ་གྱུར་པའི་སྦྱིན་པ་དང་། ལོངས་སྤྱོད་པ་དང་ཟད་པ་ཞེས་བྱ་བ་ལ། སྦྱིན་པའི་དབང་དུ་བྱས་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 74]
ལོངས་སྤྱོད་ཀྱི་དབང་དུ་བྱས་ནས་བརྗོད་པ་ནི། རང་བཞིན་གྱིས་ལོངས་སྤྱོད་རྒྱ་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བསྟན་ཏོ། །

[Block 75]
ལོངས་སྤྱོད་དེ་ཡང་དོན་དང་ལྡན་པའི་ལོངས་སྤྱོད་དང་། དོན་དང་མི་ལྡན་པའི་ལོངས་སྤྱོད་དོ། །
--- END BLOCKS ---
