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
དེའི་བྱ་བ་ནི་ཡང༌[^39]དག་པའོ། །

[Block 72]
སྒོམ་པ་རབ་ཏུ་དབྱེ་བ་དེ་ཉིད་ལ་ལྷག་པའི་ཚུལ་ཁྲིམས་ཞེས་བྱ་བ་ལ།[^40] ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་པའི་བསླབ་པ་ནི་ལྷག་པའི་ཚུལ་ཁྲིམས་ཏེ། བསླབ་པ་དེ་ཡང་བྱང་ཆུབ་སེམས་དཔའི་སྒོམ་པ་གང་མི་དགེ་བའི་ཆོས་མི་བྱེད་པའི་སེམས་སོ། །

[Block 73]
ལྷག་པའི་སེམས་ཞེས་བྱ་བ་ལ། ནང་གི་སེམས་ནི་ལྷག་པའི་སེམས་སོ།[^41] །སེམས་ཉིད་ཀྱི་དབང་དུ་བྱས་པའི་བསླབ་པ་ནི་ལྷག་པའི་སེམས་ཏེ་ཏིང་ངེ་འཛིན་ཏོ།[^42] །ལྷག་པའི་ཤེས་རབ་ཅེས་བྱ་བ་ལ། མངོན་པར་རྟོགས་པར་བྱེད་པའི་ཤེས་རབ་ནི་ལྷག་པའི་ཤེས་རབ་བམ། ཤེས་རབ་ཉིད་ཀྱི་དབང་དུ་བྱས་པའི་བསླབ་པ་ནི་ལྷག་པའི་ཤེས་རབ་སྟེ། དེ་ཡང་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་སོ། །

[Block 74]
སྤངས་པའི་ཁྱད་པར་ཞེས་བྱ་བ་ལ། ཁྱད་པར་དུ་འཕགས་པའམ། རབ་ཏུ་དབྱེ་བས་སམ། སོ་སོ་རང་གི་རིག་པས་ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་པ་སྟེ། དེ་ཡང་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 75]
ཡེ་ཤེས་ཀྱི་ཁྱད་པར་གྱིས༌[^43]ཁྱད་པར་དུ་འཕགས་པའི་གསུང་ཞེས་བྱ་བ་ནི་སྒྲིབ་པ་དང་བྲལ་བའི་ཡེ་ཤེས་ཏེ། དེ་ཡང་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་རྗེས་སུ་མཐུན་པའོ།[^44] །སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ནི་སྒྲིབ་པ་ཐམས་ཅད་ཀྱི་བག་ཆགས་སྤངས་པ་སྟེ། འདི་ནི་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་དང་། ཡེ་ཤེས་ཀྱི་ཁྱད་པར་རོ། །

[Block 76]
ཇི་ལྟར་བརྗོད་ཅེས་བྱ་བ་ནི་རྣམ་པ་གང་གིས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 77]
ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་དག་ནི་དེ་ལ་འཇུག་པའི་རྒྱུ་དང་འབྲས་བུར་ཞེས་བྱ་བ་ལ། རྣམ་པར་ཤེས་པ་ཙམ་ཉིད་ཀྱིས་ན་ངོ་བོ་ཉིད་གསུམ་གྱི་ཁྱད་པར་དག་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་རྒྱུ་སྟེ། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་འདྲེན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 78]
སར་ཆུད་པ་རྣམས་ཀྱིས༌[^45]ནི་དེ་དག་ཉིད་དག་པའོ། །

[Block 79]
འཇིག་རྟེན་ལས་འདས་པར་གྱུར་པ་ནི་འབྲས་བུའོ། །

[Block 80]
བྱང་ཆུབ་སེམས་དཔའི་ས་བཅུ་དག་ནི་དེའི་རྒྱུ་དང་འབྲས་བུ་སྒོམ་པ༌[^46]རབ་ཏུ་དབྱེ་བ་ཞེས་བྱ་བ་ལ་བསླབ་པ་གསུམ་དང་། དེའི་འབྲས་བུ་དང་། དེའི་སྤངས་པ་ནི་དེའི་འབྲས་བུ་སྤངས་པའོ། །

[Block 81]
དེའི་ངོ་བོ་ནི་དེའི་འབྲས་བུ་སྤངས་པ་ཉིད་དེ། ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 82]
རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་ནི་ལྷག་པའི་ཤེས་རབ་ཅེས་བྱ་བ་ལ། ཉན་ཐོས་ཀྱི་རྣམ་པར་མི་རྟོག་པ་ནི་ཕྱིན་ཅི་ལོག་བཞིས་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 83]
བྱང་ཆུབ་སེམས་དཔའི་ཆོས༌[^47]ནི་ཆོས་ཐམས་ཅད་རྣམ་པར་མི་རྟོག་པ་ཉིད་དེ། དེ་དག་ནི་རྣམ་པར་མི་རྟོག་པ་དག་གི་ཁྱད་པར་ཡིན་ནོ། །

[Block 84]
སངས་རྒྱས་ཀྱི་སྐུ་གསུམ་ནི་དེའི་འབྲས་བུ་ཞེས་བྱ་བ་ལ། དེ་རྣམས་ཀྱི་འབྲས་བུ་ནི་དེའི་འབྲས་བུ་སྟེ། དེའི་འབྲས་བུ་དང་ཡེ་ཤེས་ནི་དེའི་འབྲས་བུ་ཡེ་ཤེས་སོ། །

[Block 85]
དེའི་ངོ་བོ་ནི་དེའི་འབྲས་བུ་ཡེ་ཤེས་ཉིད་དོ། །

[Block 86]
དེ་ལ་ངོ་བོ་ཉིད་མེད་ན་ཆོས་ཀྱི་སྐུ་ཉིད་ཀྱང་མ་ཡིན་ཏེ། མིག་བཞིན་ནོ། །

[Block 87]
དེ་མེད་ན་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་ཡང་མ་ཡིན་ཏེ། མིག་གི་རྣམ་པར་ཤེས་པ་བཞིན་ཏེ། འདིར་རྟེན་དང་བརྟེན་པ༌[^48]མཚུངས་པའི་ཆོས་བལྟ་བར་བྱའོ། །

[Block 88]
ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་མེད་པར་ས་ཆེན་པོར་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཆོས་ཀྱི་ལོངས་སྤྱོད་མི་འབྱུང་ངོ་། །དེ་མེད་པར་ཡང་ཚོགས་ཡོངས་སུ་རྫོགས་པ་མི་འབྱུང་སྟེ། གཟུགས་མི་མཐོང་བ་བཞིན་ནོ། །

[Block 89]
སྤྲུལ༌[^49]པར་ཡང་མོས་པས་སྤྱོད་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་དང་། ཉན་ཐོས་དམན་པ་ལ་མོས་པ་རྣམས་ཀྱི་དང་བའི་ཚོལ་བ༌[^50]ཉིད་ཉམས་པར་འགྱུར་བ་དེས་ན་ངེས་པར་སྐུ་གསུམ་དུ་འགྱུར་བ་ཡིན་ནོ། །

[Block 90]
ཐེག་པ་ཆེན་པོ་ཉན་ཐོས་ཀྱི་ཐེག་པ་ལས་ཁྱད་པར་དུ་བྱས་པ་ཞེས་བྱ་བ་ལ། ཉན་ཐོས་ཀྱི་ཐེག་པ་ལས་མ་བསྟན་པ་ཐེག་པ་ཆེན་པོ་ལས་ཁྱད་པར་དུ་འཕགས་པ་མཆོག་ཉིད་དུ་བསྟན་པ་དག་གོ། །

[Block 91]
དེ་དག་ཀྱང་གང་ཞེ༌[^51]ན། གནས་བཅུ་པོ་འདི་དག་ནི་བྱང་ཆུབ་ཆེན་པོ་ཀུན་ཏུ་སྒྲུབ་པར་བྱེད་པ་སྟེ། ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་འཐོབ་པར་ཤིན་ཏུ་འཐད་པ་མཐུན་པ་འགལ་བ༌[^52]མེད་པའོ་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་ཆེན་པོ་ཀུན་ཏུ་སྒྲུབ་པར་བྱེད་པ་ཉིད་ནི། བྱང་ཆུབ་ཆེན་པོར་སྒྲུབ་པར་བྱེད་པ་ཉིད་དེ་རྒྱུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 92]
ཤིན་ཏུ་འཐད་པ་ཞེས་བྱ་བ་ནི་རིགས་པ་ལ་སོགས་པའི་ཚད་མས་བརྟགས་ནས་ཉེ་བར་བསྟན་པའི་ལམ་གྱི་རྒྱུ་མཚན་ཏེ། རྒྱུ་མཚན་རྣམ་པ་བཅུ་པོའོ། །

[Block 93]
མཐུན་པ་ཞེས་བྱ་བ་ནི་མངོན་པར་རྟོགས་པ་ལ་རབ་ཏུ་སྦྱོར་བ་ནི།[^53] རྗེས་སུ་མཐུན་པར་གནས་པ་སྟེ། ཇི་ལྟར་ལམ་བསྟན་པ་རྗེས་སུ་མཐུན་པར་གནས་པ་བཞིན་ནོ། །

[Block 94]
འགལ་བ་མེད་པ་ཞེས་བྱ་བ་ནི་ས་རྣམས་ལ་མི་མཐུན་པའི་གནོད་པའི་རྒྱུ་མེད་པ་སྟེ། ཇི་ལྟར་བསྟན་པའི་ལམ་ལ་ཆོམ་རྐུན་ལ་སོགས་པའི་གནོད་པ་མེད་པ་བཞིན་ཏེ། འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པ་དག་མི་འགལ་བ་ཉིད་དོ། །

[Block 95 [HEADING]]
### གོ་རིམས་འདི་ལྟར་བསྟན་པ། ^1-2-0

[Block 96]
ཅིའི་ཕྱིར་གོ་རིམས་འདི་ལྟར་བསྟན་ཞེ༌[^54]ན། གང་གི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔས་རེ་ཞིག་དང་པོ་ཉིད་དུ་ཆོས་ཞེས་བྱ་བ་ནས་བརྩམས་ནས། འབྲས་བུ་མྱ་ངན་ལས་འདས་པ་དང་། བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པའི་བར་དུ་འདི་ལས་བསྟན་ཏེ། འདི་ལྟར་རྒྱུའི་ཆོས་རྣམས་ཤེས་ནས། [^55]རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ལ་མཁས་པར་འགྱུར་ཏེ། གང་གི་རྒྱུ་ལས་འབྲས་བུ་འབྱུང་གི །དབང་ཕྱུག་ལ་སོགས་པ་ལས་ནི་མ་ཡིན་པས་དེས་ན་རྒྱུ་དང་འབྲས་བུ་གཉིས་ཀ་ཡང་ཤེས་པར་འགྱུར་རོ། །

[Block 97]
དེས་ན༌[^56]ནི་གང་རྒྱུ་ཉིད་ལས་བྱུང་བའི་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ཤེས་པར་བྱ་སྟེ། མཚན་ཉིད་ཀྱང་གང་ཞེ་ན། ཡོད་པ་མ་ཡིན་པའི་ཀུན་ཏུ་བརྟགས་པ་ལ་ཡོད་པར་མངོན་པར་ཞེན་ཅིང་སྒྲོ་བཏགས་པ་སྟེ། ཡོད་པ་མ་ཡིན་པ་ལ་སྒྲོ་བཏགས་པས་ན་ཡོད་པའི་ཡོངས་སུ་གྲུབ་པ་ལ་སྐུར་པ་བཏབ་པར་འགྱུར་བས་མཐའ་དེ་དག་གཉི་གའི་སྐྱོན་སྤངས་པ་ནི་མཁས་པ་ཡིན་ནོ། །

[Block 98]
དེ་ནས་ནི་འདི་ལྟར་རྣམ་པར་ཤེས་པ་ཙམ་ཉིད་ཀྱི་མཚན་ཉིད་དུ་བཟུང༌[^57]ཞིང་རྟོགས་པར་བྱ་སྟེ། དེས་ནི་སྒྲིབ་པ་མེད་པར་འགྱུར་རོ། །

[Block 99]
དེ་ནས་རྣམ་པར་ཤེས་པ་ཙམ་ཉིད་ལ་འདུག་པ༌[^58]ན་རྗེས་སུ་མཐུན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་པོ་འཇིག་རྟེན་པ་ཀུན་རྫོབ་ཏུ་རྟོགས་པ༌[^59]དང་། དོན་དམ་པ་དག་རྟོགས་པར་བྱ་སྟེ། ཡོངས་སུ་དག་པའི་བསམ་པས་གཟུང་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 100]
དེ་ནས་ནི་ས་བཅུ་པོ་རྣམས་ཀྱི་ཁྱད་པར་གྱིས་བསྐལ་པ་གྲངས་མེད་པ་གསུམ་དུ་གོམས་པར་བྱ་སྟེ། ཉན་ཐོས་ཀྱི་རྟོགས་པ་ལྟར་ནི་མ་ཡིན་ཏེ། དེ་དག༌[^60]ནི་སྐྱེ་བ་གསུམ་གྱི་གཉེན་པོས་ཐར་པར་འགྱུར་རོ། །

[Block 101]
དེ་ནས་དེ་དག་ཉིད་ལ་བསྒོམས་པས་བསླབ་པའི༌[^61]ཚུལ་ཁྲིམས་ལ་སོགས་པའི་བསླབ་པ༌[^62]གསུམ་ཡོངས་སུ་རྫོགས་པར་བྱའོ། །

[Block 102]
དེ་ནས་ལྷག་པའི༌[^63]འབྲས་བུ་མྱ་ངན་ལས་འདས་པ་ཉོན་མོངས་པ་དང་། ཤེས་བྱའི་སྒྲིབ་པ་སྤངས་པ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་སྐུ་གསུམ་རྫོགས་པར་བྱང་ཆུབ་པ་ཞེས་བྱ་བ་ནི་གོ་རིམས་ཏེ།[^64] འདི་དག་ཉིད་ནི་ཐེག་པ་ཆེན་པོའོ། །

[Block 103]
དེས་ན་འདི་ལྟར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་བརྗོད་པར་བྱ་བ་དེ་ཡང་ཀུན་གཞི་རྣམ་པར་ཤེས་པའི་ནང་དུ་འདུས་སོ། །

[Block 104]
དེའི་མཚན་ཉིད་ནི་དེའི་ངོ་བོ་ཉིད་གསུམ་མོ། །

[Block 105]
དེས་ན་རྟོགས་པ་ནི་རྣམ་པར་ཤེས་པ་ཙམ་ཉིད་དོ། །

[Block 106]
དེ་ལས་ནི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 107]
ཕ་རོལ་ཏུ་ཕྱིན་པ་ལས་ནི་ས་དག་གོ། །

[Block 108]
ས་དག་ནི་བསླབ་པའོ། །

[Block 109]
བསླབ་པ་ལས་ནི་སྤངས་པ་དང་ཡེ་ཤེས་ཏེ། མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་ནི་སྐུ་གསུམ་གྱིས༌[^65]བསྡུས་པའོ། །

[Block 110]
དེ་དག་ཉིད་ནི་སངས་རྒྱས་ཞེས་བྱ་སྟེ། དེ་བས་ན་གོ་རིམས་ནི་འདི་ལྟར་བསྟན་ཏོ། །
--- END BLOCKS ---
