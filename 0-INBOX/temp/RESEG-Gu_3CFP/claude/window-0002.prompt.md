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

[Block 76]
དོན་དང་ལྡན་པའི་ལོངས་སྤྱོད་ཀྱི་དབང་དུ་བྱས་པ་ནི། ལོངས་སྤྱོད་དེ་ལུས་བདེ་བར་བྱེད་པའོ། །

[Block 77]
ཡིད་མགུ་བར་བྱེད་པ་ནི་ཡོངས་སུ་སྤྱོད་པ་སྟེ། ལས་ཀྱི་མཐའ་རྒྱ་ཆེན་པོ་དག་ལ་མོས་པས་སྒྲུབ་པའོ། །

[Block 78]
གང་འཇིག་རྟེན་ན་ཞུགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི། ཕྱིན་ཅི་ལོག་གི་ལོངས་སྤྱོད་དགག་པའི་དབང་དུ་བྱས་ནས་བསྟན་པའོ། །

[Block 79]
འདོད་ཆགས་དང་བྲལ་བ་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བ་ནི། ཞུགས་པ་ཐོབ་པ་རྣམས་ལས་ངོ་ཚ་དང་ཁྲེལ་ཡོད་པ་བསྟན༌[^37]པའོ། །

[Block 80]
མ་འོངས་པའི་ནི། ལོངས་སྤྱོད་རྒྱ་ཆེན་པོ་དག་རྙེད་ན་ཞེས་བྱ་བ་སྟེ། སྔར་གྱི་ནི་གཏང་བར་བྱ་བ་རབ་ཏུ་བསྟན་པ་ཡིན་ལ། འདི་ནི་སྦྱིན་པར་བྱ་བའི་རྫས་འཐོབ་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 81]
ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རིགས་ཀྱི་རྟགས་བསྡུས་པའི་དོན་ནི། ཚུལ་ཁྲིམས་རྣམ་པ་གསུམ་གྱི་རྟགས་རྣམས་ཏེ། སྡོམ་པའི་ཚུལ་ཁྲིམས་དང་། དགེ་བ་ཆོས་སྡུད་པ་དང་། སེམས་ཅན་གྱི་དོན་བྱ་བའི་ཚུལ་ཁྲིམས་ཀྱིའོ། །

[Block 82]
དེ་ལ་སྡོམ་པའི་ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་ནས། ལུས་དང་ངག་གི་ལས་ཞེས་བྱ་བ་ལས་བརྩམས་པའོ། །

[Block 83]
མི་དགེ་བ་ཞེས་བྱ་བ་ལ༌[^38]ནི་རང་ལ་མི་ཕན་པ་བྱེད་པའོ། །

[Block 84]
ཤིན་ཏུ་དྲག་པོའི༌[^39]ཞེས་བྱ་བ་ནི། དེའི་མི་མཐུན་པའི་ཕྱོགས་སྤོང་བའོ། །

[Block 85]
སེམས་ཅན་ལ་ཤིན་ཏུ་གནོད་པ་མ་ཡིན་ཞེས་བྱ་བ་ནི། སྲོག་གཅོད་པ་སྤངས་པའི་ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་ནས་བསྟན་པ་སྟེ། སྦྱོར་བའི་དུས་ཀྱིའོ། །

[Block 86]
བྱས་སུ་ཟིན་ཀྱང་ཞེས་བྱ་བ་ནི་མཇུག་གི་དབང་དུ་བྱས་ནས་བསྟན་པའོ། །

[Block 87]
དེ༌[^40]ཡང་འཛེམ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་དངོས་པོ༌[^41]བཞིའི་དུས་སུའོ། །

[Block 88]
དགའ་བཞིན་པས་མ་ཡིན་ཞེས་བྱ་བ་ནི་མི་མཐུན་པའི་ཕྱོགས་སྤོང་བའོ། །

[Block 89]
འདི་ལྟ་བུ་ནི་རེ་ཞིག་སྲོག་གཅོད་པའི་ལས་ཀྱི་ལམ་གྱིས་བསྡུས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 90]
ལག་པ་དང་བོང་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི། ལས་ཀྱི་ལམ་གྱིས་བསྡུས་པའི་དབང་དུ་བྱས་པ་སྟེ། རང་བཞིན་གྱིས་མཉེས་གཤིན་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་སྲོག་གཅོད་པ་ལ་ཡང་ངོ་། །དགེ་བ་ཆོས་སྡུད༌[^42]པའི་ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་ནས། རང་བཞིན་གྱིས་ཀྱང་བསོད་ནམས་ལ་དགའ་བ་ཡིན་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 91]
སེམས་ཅན་གྱི་དོན་བྱ་བའི་ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་ནས་བཤད་པ། སེམས་ཅན་ཕན་འདོགས༌[^43]པ་ཞེས་བྱ་བའི་བར་ནས། མ་བྱིན་པ༌[^44]ལེན་པ་སྤོང་བའི་ཚུལ་ཁྲིམས་ཀྱི་རྟགས་ཀྱི་དབང་དུ་བྱས་ནས་སེམས་ཅན་གྱི་དོན་བྱ་བའི་ཚུལ་ཁྲིམས་ནི་ཇི་ལྟར་རྟགས་དང་མཚན་མ་ལ༌[^45]ལྟོས་ལ་སྦྱར་བར་བྱ་སྟེ། བདག་གིས་ནི༌[^46]ཕྱོགས་ཙམ་བསྟན་ཏོ། །

[Block 92]
གནོད་པ་བྱེད་པ་ལ་མི་མཇེད་པའི་བཟོད་པའི་རྟགས་ནི་འདིར་རྟགས་ཞེས་བསྟན་ཏོ།[^47] །

[Block 93]
གནོད་པ་བྱེད་པ་ལ་མི་བཟོད་པ་ནི་ཤིན་ཏུ་སྨད་པའི་ཕྱིར་རོ། །

[Block 94]
གནོད་པ་བྱས་ཀྱང་མི་བཟོད་པ་མི་བྱེད་ལ་ཞེས་བྱ་བ་ནི། ལུས་དང་ངག་དག་གིས་མི་བྱེད་པའོ། །

[Block 95]
གྲོས་བཏབ་ན་ཡང་མྱུར་དུ་ཉན་པར་བྱེད་ལ་ཞེས་བྱ་བ་ནི་ལུས་དང་ངག་གིས་སོ། །

[Block 96]
ཞེ་ལ་མི་འཛིན་ཞེས་བྱ་བ་ནི་སེམས་ཀྱིས་སོ། །

[Block 97]
ཡུན་རིང་དུ་ཁོན༌[^48]དུ་མི་བྱེད་ཅེས་བྱ་བ་ནི། སྨྲའམ་མི་སྨྲའང་རུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 98]
བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རིགས་ཀྱི་རྟགས་རྣམས་ཀྱི་བསྡུས་པའི་དོན་ནི་རྣམ་པ་དྲུག་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་བརྩོན་པ་གང་དང་ལྡན་པས། རྣམ་པ་ཐམས་ཅད་དུ་བརྩོན་འགྲུས་བརྩམས་པ་དང་། བརྟན་པ་དང་ལྡན་པ་དང་། བརྩོན་འགྲུས་དང་ལྡན་པ་དང་། སྤྲོ་བ་དང་། ཕ་རོལ་གནོད་པ་དང་། བླངས་པ་མི་འདོར་བ་ཞེས་བྱའོ། །

[Block 99]
བརྩོན་འགྲུས་རྣམ་པ་དྲུག་པོ་འདི་དག་ནི་རྟགས་ཞེས་བསྟན་ཏེ། ཇི་ལྟར་བྱས་ནས་ཤེ་ན། དུས་རྟག་ཏུ་སྦྱོར་བ་ཉིད་དང་། རྟག་ཏུ་བརྩོན་པ་ཉིད་ནི་བརྩོན་འགྲུས་བརྩམས་པ་ཞེས་བརྗོད་དེ། དེའི་རྟགས་ནི་རང་བཞིན་གྱིས་འབད་པ་དང་ལྡན་པ་ཡིན་ཏེ། ནང་པར་སྔར་ལྡང་ཞིང་དགོངས་ཁ་ཉལ་བར་བྱེད་ཅེས་བྱ་བའོ། །

[Block 100]
སྦྱོར་བ་མི་ཞན་པ་རྟག་ཏུ་བྱ་བ་ལ་བརྩོན་པ་ནི་བརྟན་པ་དང་ལྡན་པ་ཞེས་བརྗོད་དེ། དེའི་རྟགས་ནི་གཉིད་ཀྱི་བདེ་བ་དང་། ཉལ་བའི་བདེ་བ་དང་། གློས་དབབ་པའི༌[^49]བདེ་བ་ཧ་ཅང་ཉམས་སུ་ལེན་པར་མི་བྱེད་ཅེས་བྱ་བའོ། །

[Block 101]
སྔོན་གྱི་རྒྱུའི་སྟོབས་ཀྱིས་བསྐོས་པའི་རྒྱུ་མཐུན་པ་ཅན་ནི་བརྩོན་འགྲུས་དང་ལྡན་པ་ཞེས་བརྗོད་དོ། །

[Block 102]
དེའི་རྟགས་ནི་བྱ་བ་ཞིག་བྱུང་ན་དོན་དེ་འགྲུབ་པར་བྱ་བའི་ཕྱིར་བྱེད་མི་འདོད་པ་དང་། ལེ་ལོ་ཟིལ་གྱིས་མནན་ཏེ། སོ་སོར་བརྟགས་ནས་བརྩོན་པ༌[^50]དེའི་བྱ་བ་དེ་མངོན་པར་རྫོགས་པར་བྱེད་ཅེས་བྱ་བའོ། །

[Block 103]
སྦྱོར་བ་དང་ལྡན་པའི་བརྩོན་འགྲུས་ཀྱིས་སོ་སོར་བརྟགས་ནས་སྦྱོར་བ་ཉིད་ནི་སྦྱོར་བ་ཞེས་བྱ་སྟེ། དེའི་རྟགས་ནི་བྱ་བ་ཐམས་ཅད་བརྩོན་པ༌[^51]ལ་ཡང་ངེས་པ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 104]
མི་འཁྲུགས་པའི་བརྩོན་འགྲུས་ཀྱི༌[^52]སྡུག་བསྔལ་གྱིས༌[^53]རེག་པ་ཐམས་ཅད་ཀྱིས་མི་འཁྲུགས་པའི་ཕྱིར་དམ་བཅས་པའི་དངོས་པོ་ལས་གཞན་དུ་མི་འགྱུར་བ་ཉིད་ནི་ཕ་རོལ་གནོད་པ་ཞེས་བྱ་སྟེ། དེའི་རྟགས་ནི་མ་བྱས་སམ་མ་ཟིན་གྱི་བར་དུ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་དུ་བརྩོན་པ་མི་འདོར་ཞིང་། བར་མ་དོར་ཡང་སྒྱིད་ལུག་པར་མི་བྱེད་པ་དང་ཞེས་བྱ་བའོ། །

[Block 105]
ཆོག་མི་ཤེས་པའི་བརྩོན་འགྲུས་ཀྱི༌[^54]དོན་གྱི་ཁྱད་པར་ཆུང་ངུ་རྟོགས་པས་ཆོག་མི་ཤེས་པ༌[^55]ནི་དགེ་བའི་ཆོས་ལ་བླངས་པ་མི་འདོར་བ་ཞེས་བརྗོད་དེ། དེའི་རྟགས་ནི། དོན་གྱི་མཆོག་རྒྱ་ཆེན་པོ་དག་ལ་ཡང་སེམས་ཞུམ་པར་མི་བྱེད་ཅིང་། བདག་ལ་ཁྱད་དུ་གསོད་པར་མི་བྱེད་པ་དང་། བདག་གིས་ནི་འདི་དག་རྟོགས་པར་ནུས་ཏེ། ཞོ་ཤ་དང་ལྡན་པའོ་ཞེས་སྤྲོ་བ་སྐྱེད་པ་དང་ཞེས་བྱ་བ་སྟེ། དེ་ལྟ་བུ་ནི་རེ་ཞིག་གོ་ཆའི་བརྩོན་འགྲུས་ཀྱི་རྟགས་བསྟན༌[^56]པའོ། །

[Block 106]
ད་ནི་དགེ་བ་ཆོས་སྡུད་པའི་བརྩོན་འགྲུས་ཀྱི་དབང་དུ་བྱས་ནས་བསྟན་པ་ནི། ཚོགས་ཆེན་པོའི་ནང་དུ་འགྲོ་བའམ། གཞན་དག་དང་འགྱེད་པའམ། ཕྱིར་བརྒལ་བའམ། དེ་ལས་གཞན་པའི༌[^57]ལས་དཀའ་བ་དག་ལ་ཡང་བརྟན་པ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 107]
སེམས་ཅན་གྱི་དོན་བྱ་བའི་བརྩོན་འགྲུས་ཀྱི་རྟགས་ཀྱི་དབང་དུ་བྱས་ནས་བསྟན་པ་ནི། དོན་དང་ལྡན་པའི་བརྩལ་བ༌[^58]ཆེན་པོ་དག་ལ་ཡང་སྐྱོ་བར་མི་བྱེད་ན་ཆུང་ངུ་དག་ལ་ཅི་སྨོས་ཏེ་ཞེས་བྱ་བའོ། །

[Block 108]
བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རིགས་ཀྱི་རྟགས་བསྡུས་པའི་དོན་ནི། ཏིང་ངེ་འཛིན་འདོད་པའི་སློབ་མ་གནས་ལྔ་ལ་ངེས་པར་སྦྱར་བར་བྱ་སྟེ། འདི་ལྟ་སྟེ། སེམས་རྩེ་གཅིག་པ་ཉིད་དང་། རབ་ཏུ་དབེན་པ་དང་། སྒྲིབ་པ་རྣམ་པར་སྦྱང་བ་དང་ཡིད་ལ་བྱེད་པ་གོམས་པར་བྱ་བ་དང་། སྡོམ་པ་སྲུང་ཞིང་སྤེལ་བར་བྱ་བ་སྟེ། དེ་དག་ནི་བསམ་གཏན་གྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རིགས་ཀྱི་རྟགས་ཏེ། འདི་ལ་ཆོས་ཀྱི་དོན་ལ་ངེས་པར་སེམས་པ་ནི། རང་བཞིན་གྱིས་གཡེང་བ་མི་མང་བ་ཡིན་ཞེས་བྱ་བས་ནི་སེམས་རྩེ་གཅིག་པ་ཉིད་ཀྱི་རྟགས་སོ། །

[Block 109]
དགོན་པ་དང་ནགས་ཚལ་གྱི་གནས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་རབ་ཏུ་དབེན་པའི་རྟགས་སོ། །

[Block 110]
རང་བཞིན་གྱིས་ཀྱང་ཉོན་མོངས་པ་ཤས་ཆུང་ཞིང་སྒྲིབ་པ་ཤས་ཆུང་ལ། གནས་ངན་ལེན་ཤས་ཆུང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། སྒྲིབ་པ་རྣམ་པར་སྦྱོང་བའི་རྟགས་སོ། །
--- END BLOCKS ---
