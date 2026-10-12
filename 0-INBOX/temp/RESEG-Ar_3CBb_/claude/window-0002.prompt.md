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
དཔལ་དེ་དང་ལྡན་པས་ན༌[^44]དཔལ་ལྡན་ཏེ། དེ་བཞིན་གཤེགས་པ་བཙུན་མོའི་ཚོགས་དང་རྣམ་པར་རོལ་པའོ། །

[Block 72]
དེ་ཉིད་ཐབས་ཤེས་རབ་གཉིས་སུ་མེད་པའི་སྙོམས་པར་ཞུགས་པའི་རྒྱུད་དོ། །

[Block 73]
རྒྱུད་དེ་ཉིད་རྒྱལ་པོ་སྟེ་རྣལ་འབྱོར་རྒྱུད་ཀྱི༌[^45]ཤིན་ཏུ་གསལ་བར་རྣམ་ཕྱེ་ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 74]
སེམས་ཅན་ཐམས་ཅད་ཀྱང་དེ་ལྟ་བུའི་ཆོས་དང་ལྡན་པར་འགྱུར་རོ་ཞེ་ན། མཐའ་དྲུག་གི་ནི་འཆིང་བས་བཅིངས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདིར་མཐའ་རྣམ་པ་དྲུག་ནི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་དང་ང་རྒྱལ་དང་། ལྟ་བ་དང་། ཐེ་ཚོམ་དང་། མ་རིག་པ་དང་རྣམ་པ་དྲུག་གོ། །

[Block 75]
འདི་ནི་མཐའ་སྟེ། འཁོར་བའི་གཡང་ས་དང་ཉེ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 76]
མཐའ་ཡང་ཡིན་དྲུག་ཀྱང་ཡིན་པས༌[^46]འདི་ནི་མཐའ་དྲུག་གོ། །

[Block 77]
མཐའ་དྲུག་ཀྱང༌[^47]ཡིན་པ་དེ་ནི་འཆིང་བས་བཅིངས་པ༌[^48]ཡང་ཡིན་པས་མཐའ་དྲུག་གི་འཆིང་བས་བཅིངས་པའོ། །

[Block 78]
དེས་ཅིར་འགྱུར་ཞེ་ན། རྒྱལ་པོར་མ་གྱུར་ཞེས་པ་ནི་དམན་པར་གྱུར་ཞེས་པའོ། །

[Block 79]
དེ་བས་ན་མཆོག་ཏུ་མ་གྱུར་པ་དེ་ནི་དམན་པར་གྱུར་པའོ། །

[Block 80]
གང་དམན་པར་གྱུར་པ་དེ་ནི་རྨད་དུ༌[^49]བྱུང་བའི་སྤྱོད་པ་ལ་མི་གནས་པའོ། །

[Block 81]
གང་རྨད་དུ་བྱུང་བའི་སྤྱོད་པ་ལ་མི་གནས་པ༌[^50]དེ་ནི་རྨད་དུ་བྱུང་བའི་སྤྱོད་ཡུལ་མ་ཡིན་ནོ། །

[Block 82]
གང་རྨད་དུ་བྱུང་བའི་སྤྱོད་ཡུལ་མ་ཡིན་པ་དེ་ནི་དེའི་འབྲས་བུ་ཅན་མ་ཡིན་ནོ། །

[Block 83]
གང་དེའི་འབྲས་བུ་ཅན་མ་ཡིན་པ་དེ་ནི་ལོག་པའི་འབྲས་བུ་དང་ལྡན་པར་འགྱུར་རོ། །

[Block 84]
མདོ་དག་ལས་ཀྱང་། སེམས་དཔའ་ཆེན་པོ་མ་རིག་པ་ལས་ནི་འདུ་བྱེད་འབྱུང་ངོ་། །འདུ་བྱེད་ལས་ནི་རྣམ་པར་ཤེས་པ་འབྱུང་ངོ་། །རྣམ་པར་ཤེས་པ་ལས་ནི་མིང་དང་གཟུགས་འབྱུང་ངོ་། །མིང་དང་གཟུགས་ལས་ནི་སྐྱེ་མཆེད་དྲུག་འབྱུང་ངོ་། །སྐྱེ་མཆེད་དྲུག་ལས་ནི་རེག་པ་འབྱུང་ངོ་། །རེག་པ་ལས་ནི་ཚོར་བ་འབྱུང་ངོ་། །ཚོར་བ་ལས་ནི་སྲིད་པ༌[^51]ལ་སོགས་པ་འབྱུང་བ་དང་། གཞན་ལས་ཀྱང་། སེམས་དཔའ་ཆེན་པོ་དེ་བཞིན་གཤེགས་པ་བཙུན་མོ་ལ་ཉེ་བར་ལོངས་སྤྱོད་པ་ནི་རྨད་དུ་བྱུང་བའི་སྤྱོད་པའོ། །

[Block 85]
སེམས་ཅན་ལོག་སྲེད་ཅན་རྣམས་ནི་འདོད་ཆགས་དང་ཞེ་སྡང་ལ་སོགས་པས་དེ་བཞིན་གཤེགས་པའི་སྤྱོད་པ་ལ་མི་གནས་ཏེ། སེམས་ཅན་འདི་དག་ནི་ཉོན་མོངས་པའི་མཐའ་ལ་གནས་པའི་ཕྱིར་རོ། །

[Block 86]
ཀྱེ་མ་སེམས་ཅན་འདི་དག་ནི་རབ་ཏུ་བརླག་གོ། །

[Block 87]
ཀུན་དུ་བརླག་གོ། །

[Block 88]
ཀུན་དུ་རབ་ཏུ་བརླག་གོ། །

[Block 89]
འདི་དག་ནི་འཁོར་བའི་ཆོས་ཉེ་བར་ལེན་པའོ། །

[Block 90]
འདི་དག་ནི་ཉོན་མོངས་པ་ལྷུར་ལེན་པའོ། །

[Block 91]
སེམས་ཅན་འདི་དག་ནི་རྨད་དུ་བྱུང་བའི་སྤྱོད་པ་སྤངས་པའོ། །

[Block 92]
སེམས་ཅན་འདི་དག་ནི་དེ་བཞིན་གཤེགས་པའི་དངོས་གྲུབ་ཐམས་ཅད་སྤངས་པའོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 93]
མཐའ་དྲུག་གི༌[^52]འཆིང་བས་བཅིངས་པའི་ཕྱིར་ཐམས་ཅད་ཀྱི་སྤྱོད་ཡུལ་མ་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་ཕྱིར་རྒྱལ་སྲས་ཡུལ་གྱུར་ཞེས་བྱ་བ་སྨོས་ཏེ། རྒྱལ་བ་ནི་སངས་རྒྱས་ཏེ་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པའོ། །

[Block 94]
རྒྱལ་བའི་སྲས་ནི་རྒྱལ་བའི་སྲས་ཏེ་བྱམས་པ་ལ་སོགས་པའོ། །

[Block 95]
དེ་རྣམས་ཀྱི་ཡུལ་དུ་གྱུར་ཞེས་པ་འདིས་ནི་འཁོར་བ་པའི༌[^53]ཡུལ་མ་ཡིན་ཞེས་སྦྱར་རོ། །

[Block 96]
ཡུལ་དུ་གྱུར་ཞེས་པ་ནི་དེ་རྣམས་ཀྱིས་ཉེ་བར་ལོངས་སྤྱོད་དུ་ཡོད་ཅེས་པའོ། །གང་ལ་སྤྱོད་ཅེ་ན། དཔལ་ལྡན་རྒྱུད་རྒྱལ་ཞེས་བྱ་བ་དེ་ཉིད་བཤད་པ། རྒྱལ་བའི་འདུས་པ༌[^54]གང་ཡིན་ཞེས་བྱ་བ་སྨོས་ཏེ། རྒྱལ་བའི་འདུས་པ་ནི་རྒྱལ་བ་འདུས་པ་སྟེ། དེ་བཞིན་གཤེགས་པ་བཙུན་མོའི་ཚོགས་དང་ཉེ་བར་སྦྱོར་བའོ། །

[Block 97]
དེ་ཉིད་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཡུལ་དུ་མ་གྱུར་པ་ཅིའི་ཕྱིར་ཞེ་ན། སངས་རྒྱས་ཀུན་གྱིས་རྒྱས་བཏབ་ཅེས་སྨོས༌[^55]ཏེ། སངས་རྒྱས་ཀུན་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པས་སོ། །

[Block 98]
དེས་རྒྱས་བཏབ་ཅེས་པ་ནི་ཐམས་ཅད་ལ་སྦས་པ་ཞེས་པའོ། །

[Block 99]
དེ་དག་གི་དོན་ཡང་དོན༌[^56]འདི་སྐད་དུ་སྟོན་པར་འགྱུར་ཏེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་སྤྱོད་པ་རྨད་དུ་བྱུང་བ་གཉིས་སུ་མེད་པའི་ཐབས་ཀྱི་སྦྱོར་བ་འདི་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ལ་སོགས་པ་རྣམས་ཀྱི་ཐུན་མོང་མ་ཡིན་པ་ཤིན་ཏུ་གསང་བར་དགོངས་སོ། །

[Block 100]
གལ་ཏེ་གསང་བ་ཞིག་ཡིན་ན། ཐམས་ཅད་ནས་ཐམས་ཅད་དུ་རྟོག་པ༌[^57]མེད་པར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་པའི་ཕྱིར་ཀླུ་སྒྲུབ་ལས་རྙེད་པ་ཞེས་སྨོས་ཏེ། ལེགས་པར་ལུང་བསྟན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཀླུ་སྒྲུབ་ལས་རྙེད་པ་བཤད་ཅེས་སྦྱར་རོ། །

[Block 101]
ཡང་ན་དཔལ་ལྡན་རྒྱུད་རྒྱལ་གྱི་དཔལ་ནི་སྐུ་རྣམ་པ་གསུམ་མོ། །

[Block 102]
དཔལ་དེ་ཐོབ་པའི་ཐབས་གང་ལ་ཡོད་པ་དེ་ནི་དཔལ་ལྡན་ཏེ། བསྐྱེད་པའི་རིམ་པ་དང་རྫོགས་པའི་རིམ་པའོ། །

[Block 103]
རིམ་པ་རྣམ་པ་གཉིས་གཙོ་བོར་སྟོན་པའི་རྒྱུད་ནི་རྒྱུད་རྒྱལ་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པའོ། །

[Block 104]
ཡང་ན་དཔལ་ལྡན་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་སོ། །

[Block 105]
དེ་དང་གང་ལྡན་པ་ནི་དཔལ་ལྡན་ཏེ་རྡོ་རྗེ་འཆང་ཆེན་པོའོ། །

[Block 106]
དེ་ཉིད་ཀྱིས་གསུངས་པ་འདི་ཉིད་ནི་རྒྱུད་ཀྱི་རྒྱལ་པོ་ཡིན་ཞེས་སྦྱར་རོ། །

[Block 107]
ཡང་ན་དཔལ་ལྡན་ཡང་ཡིན་རྒྱུད་ཀྱང་ཡིན་པས་ན་དཔལ་ལྡན་རྒྱུད་རྒྱལ་ཏེ། གང་ལ་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཐོབ་པར་བྱེད་པའི་ཐབས་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 108]
དེ་ཉིད་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་ཀྱིས་ཤིན་ཏུ་གསལ་བར་རྣམ་ཕྱེ་སྟེ། གང་ལ་ཏིང་ངེ་འཛིན་གཙོ་བོར༌[^58]སྟོན་པར་བྱེད་པའི་རྒྱུད་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་དོ། །གང་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ལ་བྱམས་པ་ལ་སོགས་པས་ཞུས་པའི་རྒྱུད་ཡེ་ཤེས་རྡོ་རྗེ་ཀུན་ལས་བཏུས་པ་ལ་སོགས་པའོ། །

[Block 109]
དེས་གསལ་བར་བྱེད་པ་ནི་དེས་གསལ་བར་བཤད་པ་སྟེ། སྒྲ་དང་དོན་ཐམས་ཅད་རྒྱས་པར་བྱས་ཤེའོ།[^59] །དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པ་ལ་རྣལ་འབྱོར་གྱི་རྒྱུད་ཀྱིས་རྒྱས་པར་བྱེད་པ་ཅིའི་ཕྱིར་ཞེ་ན། མཐའ་དྲུག་གི་ནི་འཆིང་བས་བཅིངས། །ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་མཐའ་དྲུག་གི་འཆིང་བ་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 110]
གལ་ཏེ་མཐའ་དྲུག་གི་འཆིང་བས་བཅིངས་ཀྱང་ཉེ་བར་གདགས་པ་མི་བྱའོ་ཞེ་ན། བློ་དམན་པ་རྣམས་ཀྱིས་རྟོགས་པར་བྱེད་པར་འགྱུར་ཏེ། དེའི་ཕྱིར་རྒྱལ་སྲས་ཡུལ་གྱུར་ཞེས་བྱ་བ་སྨོས་སོ། །
--- END BLOCKS ---
