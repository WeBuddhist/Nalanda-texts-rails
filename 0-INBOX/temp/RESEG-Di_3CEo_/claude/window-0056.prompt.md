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
[Block 1961]
གཞན་ལས་མནོད་པར༌[^764]བྱ་སྟེ། རྐྱེན་ཡོད་ཀྱང་མི་འདའ་བར་བྱ་བའི་ཕྱིར་རོ། །

[Block 1962]
དེ་ལས་གཞན་དུ་མནོས༌[^765]པས་ནི་ལེགས་པར་སྤྱད་པ་ཙམ་དུ་འགྱུར་གྱི།

[Block 1963]
བསྙེན་གནས་ཀྱི་སྡོམ་པ་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཡན་ལག་བརྒྱད་ནོད་ཅེ་ན། །

[Block 1964 [VERSE]]
ཚུལ་ཁྲིམས་ཡན་ལག་བག་ཡོད་པའི། །
ཡན་ལག་བརྟུལ་ཞུགས་ཡན་ལག་སྟེ། །
བཞི་གཅིག་དེ་བཞིན་གསུམ་རིམ་བཞིན། །
ཡང་བག་ཡོད་པའི་ཡན་ལག་དང་། །

[Block 1965]
བརྟུལ་ཞུགས་ཀྱི་ཡན་ལག་འདི་དག་མནོས་པས་ཅིར་འགྱུར་ཞེ་ན། དེ་ཡིས་དྲན་ཉམས་དྲེགས་པར་འགྱུར། །མྱོས་པས་འགྱུར་བ་འཐུངས་པས་ནི་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པའི་དྲན་པ་ཉམས་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1966]
ཁྲི་སྟན་མཐོན་པོ་ལ་སོགས་པ་བསྟན་ན་དྲེགས༌[^766]པར་འགྱུར་རོ། །

[Block 1967]
དུས་སུ་ཟ་ཞིང་ཟས་ནར་མའི་དུས་སུ་ཟབ་ཡོངས་སུ་སྤངས་པ་ལས་བསྙེན་གནས་ཀྱི་དྲན་པ་དང་སྐྱོ་བའི་དྲན་པ་ཉེ་བར་གནས་པར་འགྱུར་ཏེ། དེ་མེད་ན་གཉིས་ཀ་ཡང་མེད་དོ། །

[Block 1968]
ཡང་ཅི་བསྙེན་གནས་འདི་དག་དགེ་བསྙེན་ཁོ་ན་ལ་ཡོད་དམ༌[^767]གཞན་ལའང་བསྙེན་གནས་ཀྱི་སྡོམ་པ་ཡོད་མོད་ཀྱི། སྐྱབས་སུ་མ་སོང་བ་ལ་མེད། །དགེ་བསྙེན་མ་ཡིན་པ་ཡང་གང་ཞིག་ཉིན་ཞག་དེ་ལ། སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན་ལ་སྐྱབས་སུ་སོང་སྟེ། བསྙེན་གནས་ཀྱི་སྡོམ་པ༌[^768]ནོད་པ་དེ་ལ་བསྙེན་གནས་ཀྱི་སྡོམ་པ་སྐྱེ་བར་འགྱུར་ཏེ། གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 1969]
མདོ་ལས།

[Block 1970]
སྐྱབས་སུ་འགྲོ་བ་ཙམ་གྱིས་དགེ་བསྙེན་དུ་བཤད་པ། ཅི་སྐྱབས་སུ་འགྲོ་བ་ཁོ་ནས་དགེ་བསྙེན་དུ་འགྱུར་རམ་ཞེ་ན། ཁ་ཆེ་པ་རྣམས་ན་རེ་སྡོམ་པ་མེད་པར་མི་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 1971]
འོ་ན་གང་མདོ་ལས་གསུངས་པ་ཇི་ལྟ་བུ་ཞེ་ན། འདི་ལ་འགལ་བ་མེད་དེ། འདི་ལྟར།

[Block 1972]
དགེ་བསྙེན་ཉིད་དུ་ཁས་བླངས་པ། །དེ་ཁོ་ན་ལས།

[Block 1973]
སྡོམ་པ་སྐྱེ་བར་འགྱུར་བ། དགེ་བསྙེན་དུ་ཁས་བླངས་པ་ཁོ་ནས་འདིའི་དགེ་བསྙེན་གྱི་སྡོམ་པ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1974]
སྡོམ་པ་ཐོབ་ཀྱང་བསླབ་པའི་གཞི་རྣམས་ཤེས་པར་བྱ་བའི་ཕྱིར། བསྟན་པ་དགེ་སློང་བཞིན། ཇི་ལྟར་དགེ་སློང་དང་དགེ་ཚུལ་གྱི་སྡོམ་པ་ཐོབ་ཟིན་པ་ཤེས་པར་བྱ་བའི་ཕྱིར་ཁྱོད་ཀྱིས་འདི་དང་འདི་བསྡམ༌[^769]མོ་ཞེས་བསླབ༌[^770]པའི་གཞི་རྣམས་འཛིན་དུ་འཇུག་པ་ལྟར་དགེ་བསྙེན་ཡང་དེ་དང་འདྲ་བས་སྡོམ་པ་མེད་པའི་དགེ་བསྙེན་ནི་མེད་དོ། །

[Block 1975]
གལ་ཏེ་ཐམས་ཅད་བསྡམས་པ༌[^771]ཡིན་ན། སྣ་གཅིག་སྤྱོད་སོགས་ཇི་ལྟ་བུ། །གལ་ཏེ་དགེ་བསྙེན་ཐམས་ཅད་དགེ་བསྙེན་གྱི་སྡོམ་པ་ལ་གནས་པ་ཡིན་ནོ།[^772] །

[Block 1976]
བཅོམ་ལྡན་འདས་ཀྱིས་སྣ་གཅིག་སྤྱོད་པ་དང་། ཕྱོགས་གཅིག་སྤྱོད་པ་དང་། ཕལ་ཆེར་སྤྱོད་པ་དང་། ཡོངས་སུ་རྫོགས་པར་སྤྱོད་པའི་དགེ་བསྙེན་ཞེས་གསུངས་པ་ཇི་ལྟ་བུ་ཡིན། དེ་སྲུང་བ་ལས་གསུངས་ཞེས་གྲགས། །[^773]གང་ཞིག་བསླབ་པའི་གཞི་གང་སྲུང་བར་བྱེད་པ་དེ་ནི་དེ༌[^774]སྤྱོད་པ་ཞེས་གསུངས་པར་ཟད་ཀྱི་ཐམས་ཅད་སྡོམ་པ་ལ་གནས་པར༌[^775]ནི་འདྲའོ། །

[Block 1977]
སྡོམ་པ་ཐམས་ཅད་ཀྱང་། ཆུང་ངུ་ལ་སོགས་ཡིད་ཇི་བཞིན། ཆུང་ངུ་དང་འབྲིང་དང་ཆེན་པོ་ཉིད་ནི་ཡང་དག་པར་ལེན་པའི་སེམས་ཀྱི༌[^776]དབང་གིས་སོ། །

[Block 1978]
གང་ཞིག་སངས་རྒྱས་དང་། ཆོས་དང་། དགེ་འདུན་ལ་སྐྱབས་སུ་འགྲོ་བ་དེ་ཅི་ལ་སྐྱབས་སུ་འགྲོ་ཞེ་ན། གང་ཞིག་གསུམ་ལ་སྐྱབས་སུ་འགྲོ་སྟེ།

[Block 1979 [VERSE]]
སངས་རྒྱས་དགེ་འདུན་བྱེད་པའི་ཆོས། །
མི་སློབ་པ་དང་གཉིས་ཀ་དང་། །
མྱ་ངན་འདས་ལ་སྐྱབས་སུ་འགྲོ། །

[Block 1980]
གང་ཞིག་སངས་རྒྱས་ལ་སྐྱབས་སུ་འགྲོ་བ་དེ་ནི་སངས་རྒྱས་སུ་བྱེད་པའི་ཆོས་མི་སློབ་པ་ལ་སྐྱབས་སུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 1981]
དེ་དག་ཀྱང་ཟད་པ་ཤེས་པ་ལ་སོགས་པ་འཁོར་དང་བཅས་པ་ཡིན་ནོ། །

[Block 1982]
གཟུགས་ཀྱི་སྐུ་ནི་སྔ་མ་དང་ཕྱི་མར་ཡང་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 1983]
གང་ཞིག་དགེ་འདུན་ལ་སྐྱབས་སུ་འགྲོ་བ་དེ་ནི་དགེ་འདུན་དུ༌[^777]བྱེད་པའི་ཆོས་སློབ་པ་དང་མི་སློབ་པ་ལ་སྐྱབས་སུ་འགྲོ་བ་ཡིན་ཏེ། གང་དག་འཐོབ་པས༌[^778]གང་ཟག་བརྒྱད་པོ་མི་ཕྱེད་པའི་ཕྱིར་དགེ་འདུན་དུ་འགྱུར་བའོ། །

[Block 1984]
གང་ཞིག་ཆོས་ལ་སྐྱབས་སུ་འགྲོ་བ་དེ་ནི་མྱ་ངན་ལས་འདས་པའི་ཆོས་སོ་སོར་བརྟགས་པས་འགོག་པ་ལ་སྐྱབས་སུ་འགྲོ་བ་ཡིན་ཏེ། བདག་གཞན་གྱི་རྒྱུད་ཀྱི་ཉོན་མོངས་པ་རྣམས་དང༌[^779]སྡུག་བསྔལ་ཞི་བར་མཚན་ཉིད་གཅིག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1985]
དེ་ལྟ་ནའང་མཚན་ཉིད་ཐ་མི་དད་པའི་ཕྱིར་སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན་ཐམས་ཅད་ལ་སྐྱབས་སུ་འགྲོའོ་ཞེས་གསུངས་པར་འགྱུར་རོ། །

[Block 1986]
སྐྱབས་ཀྱི་དོན་ཀྱང་སྐྱོབ་པའི་དོན་ཡིན་ཏེ། དེ་ལ་བརྟེན་ནས་སྡུག་བསྔལ་ཐམས་ཅད་ལས་གཏན་དུ་ངེས་པར་ཐར་པའི་ཕྱིར་རོ། །

[Block 1987]
ཡང་ཅིའི་ཕྱིར་སྡོམ་པ་གཞན་དག་ལ་ནི་མི་ཚངས་པར་སྤྱོད་པ་སྤོང་བའི་གཞི་རྣམ་པར་གཞག་ལ། དགེ་བསྙེན་ལ་ནི་འདོད་པས་ལོག་པར་གཡེམ་པ་སྤོང་བ་བསླབ༌[^780]པའི་གཞིར་རྣམ་པར་གཞག་ཅེ་ན།

[Block 1988 [VERSE]]
ལོག་གཡེམ་ཤིན་ཏུ་སྨད་ཕྱིར་དང་། །
སླ་ཕྱིར་མི་བྱེད་ཐོབ་ཕྱིར་རོ། །

[Block 1989]
འདོད་པས་ལོག༌[^781]པར་གཡེམ་པ་ནི་འཇིག་རྟེན་ན་ཤིན་ཏུ་སྨད་པ་ཡིན་ནོ། །

[Block 1990]
ཁྱིམ་པ་དག་གིས་འདོད་པས་ལོག་པར་གཡེམ་པ་ལས་སྡོམ་པ་སླའི་འཕགས་པས་ཀྱང་འདོད་པ་ལ༌[^782]ལོག་པར་གཡེམ་པ་མི་བྱེད་པའི་སྡོམ་པ་ཐོབ༌[^783]བོ། །

[Block 1991]
དེ་བས་ན་བསླབ་པའི་གཞི་འདི་ཉིད་རྣམ་པར་གཞག་གོ། །

[Block 1992]
གང་དག་དགེ་བསྙེན་ཡིན་བཞིན་དུ་ཡང་ཆུང་མ་ལེན་པར་བྱེད་ན། ཅི་དེ་དག་གིས༌[^784]དེ་དག་ལས་ཀྱང་། སྡོམ་པ་ཐོབ་པའམ། འོན་ཏེ་མིན་ཞེ་ན། ཉི་ཚེ་བའི་སྡོམ་པ་ཐོབ་པར་འགྱུར་དུ་འོང་བས་འཐོབ་བོ། །ཇི་ལྟར་སྡོམ་པ་ཉམས་པར་མི་འགྱུར་ཞེ་ན། འདི་ལྟར།

[Block 1993 [VERSE]]
སྡོམ་པ་ཇི་ལྟར་ཁས་བླངས་བཞིན། །
འཐོབ་ཀྱི་རྒྱུད་ལས་མ་ཡིན་ནོ། །

[Block 1994]
འདི་དག་གི་སྡོམ་པ་ནི་ཇི་ལྟར་འདོད་པས་ལོག་པར་གཡེམ་པ་སྤོང་ངོ་ཞེས་ཁས་ལེན་པ་དེ་བཞིན་འཐོབ་བོ། །

[Block 1995]
དེ་ལ་འདོད་ལོག་མེད་པས་སྡོམ་པ་ཉམས་པ་ཡང་མེད་དོ། །

[Block 1996]
ཡང་ཅིའི་ཕྱིར་བརྫུན་དུ་སྨྲ་བ་སྤོང་བ་ཁོ་ན་བསླབ་པའི་གཞིར་གཞག་ལ་ཕྲ་མ་ལ་སོགས་པ་ལས་ནི་མ་ཡིན་ཞེ་ན། རྒྱུ་གསུམ་པོ་དེ་དག་ཉིད་ཀྱི་ཕྱིར་ཏེ།

[Block 1997 [VERSE]]
བརྫུན་སྨྲ་ཤིན་ཏུ་སྨད་ཕྱིར་དང་། །
སླ་ཕྱིར་མི་བྱེད་འཐོབ་ཕྱིར་རོ། །
བསླབ་པ་ཐམས་ཅད་འདས་གྱུར་ན། །
བརྫུན་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར། །

[Block 1998]
བསླབ་པ་ཐམས་ཅད་འདས་ན་དྲི་བར་བྱ་བ་ལ་བདག་གིས་དེ་ལྟ་བུ་མ་བྱས་སོ་ཞེས་བྱ་བ་འདི་ཉེ་བར་གནས་པར་འགྱུར་ཏེ། བརྫུན་དུ་སྨྲ་བར་ཐལ་བར་འགྱུར་བས་དེའི༌[^785]ཇི་ལྟར་འདས་པར་བྱས་ཀྱང་བདག་ཉིད་འཆགས་པར་འགྱུར་སྙམ་ནས་བརྫུན་དུ་སྨྲ་བ་ལས་ལྡོག་པར་བཤད་དོ། །

[Block 1999]
ཡང་ཅིའི་ཕྱིར་བཅས་པའི༌[^786]ཁ་ན་མ་ཐོ་བ་ལས་མྱོས་པར་འགྱུར་བ་འཐུངས་པ༌[^787]ལས་གཞན་འདིའི་བསླབ་པའི་གཞི་རྣམ་པར་མ་བཞག་ཅེ་ན།

[Block 2000]
བཅས་པའི༌[^788]ཁ་ན་མ་ཐོ་བ། །མྱོས་འགྱུར་ཉིད་ལས། ཅིའི་ཕྱིར་ཞེ་ན། གཞན་བསྲུང་ཕྱིར་རོ། །
--- END BLOCKS ---
