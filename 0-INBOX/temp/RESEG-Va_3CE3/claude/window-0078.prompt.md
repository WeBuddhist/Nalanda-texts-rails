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
[Block 2731]
དེ་བཞིན་ཉིད་དང་། ཡང་དག་པའི་མཐའ་ནི་འདའ་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ཆོས་ཀྱི་དབྱིངས་ནི་ཆོས་ཀྱི་སྐུ་སྟེ་འདའ་བ་མེད་དོ། །

[Block 2732]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་དེ་བཞིན་ཉིད་འདའ་བ་མེད་དོ། །

[Block 2733]
རང་སངས་རྒྱས་དང་། ཉན་ཐོས་རྣམས་ཀྱི་ཡང་དག་པའི་མཐའ་ལ་འདའ་བ་མེད་དོ་ཞེས་བྱ་བར་བྱེ་བྲག་ཏུ་ཕྱེ་སྟེ་གཟུང་བར༌[^1963]བྱའོ། །

[Block 2734]
འདི་ལྟར་དེ་དག་ལ་གང་འདའ་བར་འགྱུར་བའི་རང་བཞིན་མེད་དོ་ཞེས་བྱ་བ་ནི་འདའ་བར་བྱ་བའི་ངོ་བོ་ཉིད་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2735]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ཆོས་ཀྱི་དབྱིངས་དང་། དེ་བཞིན་ཉིད་དང་། ཡང་དག་པའི་མཐའ་ལས༌[^1964]འདའ་བ་མ་མཆིས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་ཞུས་ཏེ། གཟུགས་དང་ཚོར་བ་ལ་སོགས་པ་ནི་རྣམ་པར་འགྱུར་བའི་ངོ་བོ་ཉིད་ཡིན་པས་འདའ་བར་སྣང་ན། འདི་ལྟར་གཟུགས་ལ་སོགས་པ་ལ་ནི་འདའ་བ་ཡོད་ཀྱི། ཆོས་ཀྱི་དབྱིངས་ལ་སོགས་པ་ལ་ནི༌[^1965]མེད་ན་དེའི་ཚེ་ཅི་གཟུགས་ལ་སོགས་པ་དང་། ཆོས་ཀྱི་དབྱིངས་ལ་སོགས་པ་ལ་ཐ་དད་པ་ཡོད་དམ་ཞེས་ཞུས་པའོ། །

[Block 2736]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་རབ་འབྱོར་དེ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པས་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པའི་ཆོས་རྣམས༌[^1966]དང་། ཆོས་ཀྱི་དབྱིངས་ལ་སོགས་པ་གསུམ་ཐ་དད་པ་མེད་པར་བསྟན་ཏོ། །

[Block 2737]
དེའི་དགོངས་པ་ནི་འདི་ཡིན་ཏེ་དོན་དམ་པའི་གཟུགས་ལ་སོགས་པ་ལ་ནི་འདའ་བ་མེད་དོ་ཞེས་བྱ་བའོ། །

[Block 2738]
དེ་ནས་གནས་བརྟན་རབ་འབྱོར་གྱིས་བཅོམ་ལྡན་འདས་གལ་ཏེ་གཟུགས་ཀྱང་གཞན་མ་ལགས། ཆོས་ཀྱི་དབྱིངས་ཀྱང་གཞན་མ་ལགས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་ཞུས་ཏེ། གལ་ཏེ་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པ་དང་། ཆོས་ཀྱི་དབྱིངས་ལ་སོགས་པ་ལ་ཐ་དད་པ་མེད་ན། འོ་ན་ནི་ཆོས་ཀྱི་དབྱིངས་ལ་སོགས་པ་བཞིན་དུ་ཆོས་ཐམས་ཅད་འདུས་མ་བྱས་པ་ཡིན་པའི་ཕྱིར་དགེ་བ་དང་མི་དགེ་བའི་ལས་རྣམས་ཀྱི་འབྲས་བུ་རྣམ་པར་དགོད་པ་མེད་པར་འགྱུར་རོ་ཞེས་ཞུས་པའོ། །

[Block 2739]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་རབ་འབྱོར་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཉེ་བར་བཟུང་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་གསུངས་ཏེ། ཆོས་ཐམས་ཅད་འདུས་མ་བྱས་པའི་ངོ་བོ་ཉིད་ཡིན་དུ་ཟིན་ཀྱང་། འོན་ཀྱང་བྱིས་པ་ཀུན་བརྟགས་པའི་སྤྱོད་ཡུལ་དུ་བྱེད་པ་རྣམས་ལ། དགེ་བ་དང་མི་དགེ་བ་ཀུན་བརྟགས་པ་རྣམས་ཡོད་དེ། དེའི་དབང་གིས་རྣམ་པར་སྨིན་པ་དཀར་པོ་དང་ནག་པོ་ཡང་ཡོད་དོ། །

[Block 2740]
དེའི་དབང་གིས་བཅོམ་ལྡན་འདས་ཀྱིས་ཀུན་རྫོབ་ཀྱི་བདེན་པའི་ཚུལ་དུ་དེ་དག་བཤད་ཀྱི། དོན་དམ་པར་ནི་ཆོས་ཐམས་ཅད་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཡིན་པས། ལས་དང་རྣམ་པར་སྨིན་པ་རྣམ་པར་དགོད་པ་བསྟན་པར་མི་ནུས་སོ་ཞེས་བྱ་བ་ནི་དོན་དམ་པར་རྣམ་པར་མི་རྟོག་པའི་ཕྱིར་རོ། །

[Block 2741]
ཆོས་དེ་ནི་རྣམ་པར་མི་རྟོག་པ་བརྗོད་དུ་མི་རུང་བས༌[^1967]བརྗོད་དུ་མེད་པ་སྟེ། འདི་ལྟར་མིང་དང་གཟུགས་ནི་སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པ་དང་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པ༌[^1968]དང་། རྣམ་པར་བྱང་བ་མེད་པ་སྟེ་ཞེས་བྱ་བ་ནི་གཟུགས་མེད་པའི་ཆོས་རྣམས་དང་གཟུགས་ཀྱི་ཆོས་རྣམས་ཀྱི་ནང་ནས་མིང་ཞེས་བྱ་བ་དང་། གཟུགས་ཞེས་བྱ་བ་སྨོས་པ་ནི་ཀུན་རྫོབ་ཀྱི་བདེན་པའི་ཚུལ་ལོ། །

[Block 2742]
དོན་དམ་པར་དེ་བཞིན་ཉིད་དེ་ནི་ཡོངས་སུ་གྲུབ་པ་ཡིན་པའི་ཕྱིར་རྣམ་པར་མི་རྟོག་པའོ། །

[Block 2743]
བརྗོད་དུ་མེད་པའི་ཕྱིར་བརྗོད་དུ་མི་རུང་བའོ། །

[Block 2744]
འདུས་མ་བྱས་པའི་ཕྱིར་སྐྱེ་བ་མེད་པའོ། །

[Block 2745]
སྐྱེ་བ་མེད་པའི་ཕྱིར་འགག་པ་མེད་པའོ། །

[Block 2746]
རང་བཞིན་གྱིས་དབེན་པའི་ཕྱིར་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པའོ། །

[Block 2747]
རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པའི་ཕྱིར་རྣམ་པར་བྱང་བ་མེད་པའོ། །

[Block 2748]
འདི་ནི་མཐའ་ལས་འདས་པ་སྟོང་པ་ཉིད་དང་། ཐོག་མ་དང་ཐ་མ་མེད་པ་སྟོང་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རྣམ་པར་མི་རྟོག་པ་ལ་སོགས་པ་དེ་དག་ཉིད་སྟོང་པ་ཉིད་རྣམ་པ་གཉིས་སུ་བརྗོད་དོ་ཞེས་བསྟན་པའོ། །

[Block 2749]
རབ་འབྱོར་གྱིས་གསོལ་པ། བཅོམ་ལྡན་འདས་གལ་ཏེ་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ཉེ་བར་བཟུང་སྟེ་འབྲས་བུ་རྣམ་པར་དགོད་པ་མཆིས་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་ཞུས་ཏེ། གལ་ཏེ་ཡང་དག་པ་མ་ཡིན་པར་འབྲས་བུ་རྣམ་པར་དགོད་པར་བྱ་ན། བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་ལ་སོགས་པ་ཡང་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་སོགས་པར་ཅིའི་ཕྱིར་རྣམ་པར་མི༌[^1969]དགོད་ཅེས་བྱའོ། །

[Block 2750]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས། རབ་འབྱོར་ཅི་བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱིས་ཀུན་རྫོབ་ཀྱི་བདེན་པའམ། དོན་དམ་པའི་བདེན་པ་ཤེས་སམ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་བཀའ་སྩལ་ཏེ། འབྲས་བུ་རྣམ་པར་དགོད་པ་མེད་དུ་ཟིན་ཀྱང་ཀུན་བརྟགས་པ་རྣམས་ཡོངས་སུ་ཤེས་པ་ཉིད་ཀྱི་ཕྱིར་ཀུན་བརྟགས་པའི་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་སོགས་པ་རྣམ་པར་དགོད་པ་ཡོད་དོ། །

[Block 2751]
བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་རྣམས་ལ་ནི་དེ་ཡོངས་སུ་ཤེས་པ་མེད་དེ། དེའི་ཕྱིར་ལམ་སྒོམ་པ༌[^1970]ཡང་མེད་དོ། །

[Block 2752]
དེ་བས་ན་དེ་དག་ལ་འབྲས་བུ་རྣམ་པར་དགོད་པ་ཡང་མི་བྱའོ། །

[Block 2753]
འཕགས་པའི་གང་ཟག་རྣམས་ལ་ནི་ཡོངས་སུ་ཤེས་པ་ཡོད་པས་དེའི་ཕྱིར་དེ་དག་ཉིད་ལ་ལམ་དང་ལམ་མ་ཡིན་པ་དང་། འབྲས་བུ་རྣམ་པར་དགོད་པར་བྱའོ། །

[Block 2754]
གནས་བརྟན་རབ་འབྱོར་གྱིས། བཅོམ་ལྡན་འདས་ཅི་ལགས་ལམ་ལ༌[^1971]བསྒོམས་པས་འབྲས་བུ་འབྱུང་བར་འགྱུར་རམ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཅི་ལམ་བསྒོམས་པའི་རྒྱུས་འབྲས་བུ་འབྱུང་བར་འགྱུར་རམ། འབྲས་བུ་ཐོབ་པར་འགྱུར་རམ་ཞེས་དེ་སྐད་ཞུས་ཏེ། དེ་ལྟར་གྱུར་ན་དེ་ཡང་དོན་དམ་པ་ཉིད་དུ་འགྱུར་རོ་ཞེས་བྱའོ། །

[Block 2755]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས། རབ་འབྱོར་དེ་ནི་མ་ཡིན་ཏེ། ལམ་བསྒོམས་པས་འབྲས་བུ་འབྱུང་བར་མི་འགྱུར། འབྲས་བུ་ཐོབ་པར་མི་འགྱུར་ཏེ་ཞེས་བྱ་བ་ནི། ལམ་དང་འབྲས་བུ་གཉིས་ཀ་ཡང་ཀུན་བརྟགས་པ་ཡིན་པས་བསལ་བ༌[^1972]བཀའ་སྩལ་ཏོ། །

[Block 2756]
རབ་འབྱོར་ལམ་མ་བསྒོམས་པས་ཀྱང༌[^1973]འབྲས་བུ་ཐོབ་པར་མི་འགྱུར་ཏེ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པ་ཡིན་དུ་ཟིན་ཀྱང་ངེས་པ་བསྟན་པའོ། །

[Block 2757]
ལམ་གྱིས༌[^1974]འབྲས་བུ་ཐོབ་པར་བྱ་བ་ཡང་མེད་དོ། །

[Block 2758]
ལམ་མ་ཡིན་པས་ཀྱང་ཐོབ་པར་མི་འགྱུར། ལམ་ལ་ཡོད་པའང་མ་ཡིན་ཞེས་བྱ་བ་ནི་ཆོས་ངེས་པར་གྱུར་པ་ཉིད་བསྟན་པའོ། །

[Block 2759]
ཆོས་ཀྱི་དབྱིངས་ལ༌[^1975]ཆར་བཅད་པའི་ཚུལ་གྱིས་འབྲས་བུ་རྣམ་པར་དགོད་པ་ནི་མ་ཡིན་ནོ་ཞེས༌[^1976]བྱ་བ་ནི་ཆོས་ཀྱི་དབྱིངས་ལ་དེ་ལྟར་ཆ་ཤས་སུ་བཅད་དེ་རྣམ་པར་དགོད་པ་དོན་དམ་པར་མེད་དོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2760]
བཅོམ་ལྡན་འདས་གལ་ཏེ་འདུས་བྱས་དང་། འདུས་མ་བྱས་ཀྱི་ཁམས་དག་ལ་ཆར་བཅད་པ་མ་མཆིས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་གནས་བརྟན་གྱིས་འདི་སྐད་ཞུས་ཏེ། ཅིའི་ཕྱིར་སྤོང་བ་དང་། ལམ་དང་། འབྲས་བུ་དག་རིས་སུ་བཅད་དེ། རྣམ་པར་དགོད་པར་བྱས་ཞེས་བྱའོ། །

[Block 2761]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས། རབ་འབྱོར་ཅི་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་འམ་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་བཀའ་སྩལ་ཏེ། དེ་དག་ལ་ནི་དོན་དམ་པར་ཡོངས་སུ་ཤེས་པ་དང་། རབ་ཏུ་རྟོགས་པའི་རིམ་པ་མེད་པ་ཉིད་དེ། འདི་ལྟར་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་སོགས་པ་དེ་དག་ནི་འདུས་མ་བྱས་པ་སྟེ། དེ་དག་ལ་རིམ་པར་དབྱེ་བ་ཉིད་མེད་དོ། །

[Block 2762]
དེ་བས་ན་དེ་དག་ཐམས་ཅད་སྟོང་པ་ཉིད་དུ་རབ་ཏུ་རྟོགས་པ༌[^1977]ན་ཆར་བཅད་པ་མེད་དོ། །

[Block 2763]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་ཆོས་རྣམས་ཀྱི་ཆོས་ཀྱི་མཚན་ཉིད༌[^1978]རབ་ཏུ་རྟོགས་པ་ལགས་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དོན་དམ་པར་ཆར་བཅད་པ༌[^1979]དེ་རབ་ཏུ་རྟོགས་པ་མེད་ན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2764]
བཅོམ་ལྡན་འདས་སྤྲུལ་པའི་ལམ་སྒོམ་པ༌[^1980]ཇི་ལྟ་བུ་ལགས་ཞེས་བྱ་བ་ནི༌[^1981]སྤྲུལ་པ་དཔེར་བསྟན་པ་ཞུས་པའོ། །

[Block 2765]
རབ་འབྱོར་ལམ་བསྒོམས་པ༌[^1982]གང་ལ་བརྟེན་ནས་ཞེས་བྱ་བ་ལ་སོགས་པས་སྤྲུལ་པའི་དཔེ་ཉིད་སྒྲུབ་པོ། །བཅོམ་ལྡན་འདས་ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོས༌[^1983]ཆོས་ཐམས་ཅད་དངོས་པོ་མ་མཆིས་པར་རབ་ཏུ་རྟོགས་པར་འགྱུར་ཞེས་བྱ་བ་ནི་མེད་པ་ལ་ཇི་ལྟར་རབ་ཏུ་རྟོགས་ཏེ། རི་བོང་གི་རྭ་ལ་སོགས་པ་རབ་ཏུ་རྟོགས་པར་མི་འགྲུབ་པོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2766]
དེ་བཞིན་གཤེགས་པའི་སྤྲུལ་པ་དངོས་པོ་འགའ་ཞིག་ལ་བརྟེན་ཏེ། ཀུན་ནས་ཉོན་མོངས་པར་འགྱུར་བའམ། རྣམ་པར་བྱང་བར་འགྱུར་བའི་དངོས་པོ་གང་ཡང་དམིགས་སུ༌[^1984]ཡོད་དམ་ཞེས་བྱ་བ་འདིས་དེ་བཞིན་གཤེགས་པ་ལ་ཀུན་ནས་ཉོན་མོངས་པ་མེད་ཅིང་རྣམ་པར་བྱང་བ་མེད་པས་འགྲོ་བ་དང་ཐར་པ་མཚུངས་པའི་ཕྱིར་རབ་ཏུ་རྟོགས་པ་ཡང་མེད་དེ། མེད་པ་ཉིད་དུ་གཞག་པ་ཙམ་དུ་ཟད་པའི་ཕྱིར་ཅི་ཡང་མ་ཡིན་ནོ་ཞེས་བསྟན་ཏོ། །

[Block 2767]
བཅོམ་ལྡན་འདས་གང་གིས་སེམས་ཅན་རྣམས་འཁོར་བ་ལས་ཐར་བར་བགྱི་བའི་འགྲོ་བ་ལྔའི་འཁོར་བ་ཡང་མ་མཆིས་ལགས༌[^1985]ན་ཇི་ལྟར་བྱང་ཆུབ་སེམས་དཔའི་སྐྱེས་བུའི་མཐར་འགྱུར་ཞེས་བྱ་བ་ནི་འཁོར་བ་རང་བཞིན་གྱིས་ཡང་དག་པར་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་ངོ་བོ་ཉིད་ཀྱིས་གྲོལ་བའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2768]
དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས། རབ་འབྱོར་དེ་ཇི་སྙམ་དུ་སེམས་ཞེས་བྱ་བ་ལ་སོགས་པས་འདི་སྐད་བཀའ་སྩལ་ཏེ་བྱང་ཆུབ་སེམས་དཔའ་ནི་སེམས་ཅན་ནམ༌[^1986]འཁོར་བ་མི་མཐོང་ངོ་། །རྨི་ལམ་ལ་སོགས་པའི་དཔེ་དེ་དག༌[^1987]གིས་སྔོན་མཐོང་མོད་ཀྱི། འོན་ཀྱང་དེ་དག་མེད་པར་སེམས་ཅན་རྣམས་ཀྱིས་མི་ཤེས་ཏེ། དེ་བས་ན་དེ་དག་ཤེས་པར་བྱེད་པ་ནི་དེའི་སྐྱེས་བུའི་མཐུ་ཡིན་ནོ་ཞེས་བསྟན་ཏེ། [^1988]དེ་ཉིད་རབ་འབྱོར་གལ་ཏེ། སེམས་ཅན་རྣམས་རང་རང་གིས་ཆོས་ཐམས་ཅད་རྨི་ལམ་ལྟ་བུ་ནས། སྤྲུལ་པ་ལྟ་བུའི་བར་དུ་ཤེས་སུ་ཟིན་ན་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས་སྟོན་ཏོ། །

[Block 2769]
ཆོས་ཐམས་ཅད་ཀྱི་རང་བཞིན་ནི་མིང་སྟེ་གཞོལ་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པའི་ཆོས་ཐམས་ཅད་ཀུན་བརྟགས་པའི་རང་བཞིན་ལ་མིང་ཞེས་བྱ་སྟེ། འདི་ལྟར་སེམས་ཅན་རྣམས་ཀྱི་བློ་དེ་ལ། དེ་བཞིན་དུ་གཞོལ་བའམ། བློ་ལ་རང་བཞིན་དེ་གཞོལ་བའོ། །

[Block 2770]
མཚན་མ་མེད་པ་ཡང་གཞན་ལ། ཉན་ཐོས་ཀྱི་ཆོས་རྣམས་ཀྱང་གཞན་ནམ༌[^1989]ཞེས་བྱ་བ་ལ་སོགས་པས་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་དུ། གལ་ཏེ་ཆོས་ཐམས་ཅད་མཚན་མ་མེད་པ་ཡིན་ལ། ཉན་ཐོས་ཀྱི་ཆོས་ལ་སོགས་པ་མཚན་མ་དང་བཅས་པར་རྣམ་པར་བཀོད་པར་གྱུར་ན། དེ་ལྟ་ན་ནི་སྐྱོན་དུ་ཡང་འགྱུར་ན།[^1990] འདི་ལྟར་དེ་དག་ཐམས་ཅད་ནི་མཚན་མ་མེད་པ་སྟེ། དེའི་ཕྱིར་ཉེས་པ་མེད་དོ་ཞེས་སྟོན་ཏོ། །
--- END BLOCKS ---
