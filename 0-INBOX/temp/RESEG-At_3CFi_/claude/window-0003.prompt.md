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
[Block 106]
དེའི་ཕྱིར། མིག་འཕྲུལ༌[^28]ཇི་བཞིན་ངེས་པར་ཡོངས་སུ་སྣང་། །ཞེས་བྱའོ། །

[Block 107]
ད་ནི་ཞར་ལ་འོངས་པའི་བརྟགས༌[^29]པའི་རྣལ་འབྱོར་དགག་པའི་ཕྱིར། བརྟགས་པའི་སྤྲོས་པས་བསྐྱེད་ལ་མ་ཆགས་ཤིག །ཅེས་བྱ་བ་ལ། བརྟགས་པའི་སྤྲོས་པ་ནི་ཐིག་ལེ་དང་ཕྲ་མོ་ལ་སོགས་པའོ། །

[Block 108]
མ་ཆགས་པ་ནི་དེ་ལ་བརྟེན་ནས་སེམས་གནས་པ་ཕྲ་མོ་ཡོད་ཀྱང་ལམ་གྱི་མཚན་ཉིད་མ་ཚང་བས་བྱང་ཆུབ་ཀྱི་ལམ་མ་ཡིན་པས་དགག་པའོ། །

[Block 109]
དེ་ཉིད་འཁོར་བའི་འཁྲུལ་འཁོར་གཅོད་པའི་ལམ་མ་ཡིན་པས་འཁོར་བའི་རྒྱུར་བསྟན་པ་ནི།

[Block 110 [VERSE]]
སྣ་ཚོགས་རྣམ་རྟོག་ལས་གཞན་འཆིང་བ་མེད། །
དེ་ལ་སྐྱེ་འཆི་འཁོར་བ་གཞན་མ་ཡིན། །

[Block 111]
ཞེས་བྱ་བ་ལས་སྲིད་པའི་འཁྲུལ་འཁོར་གཅོད་པའི་མཚན་ཉིད་དང་མི་ལྡན་པའི་ཐབས་རྣམས༌[^30]གོམས་སུ་ཟིན་ཀྱང་འཁྲུལ་འཁོར་དེ་ཉིད་མི་ཆོད་པས་སྤང་བར་བྱའོ། །

[Block 112]
དེས་དོན་གོམས་པར་བྱེད་པའི་རྣལ་འབྱོར་པ་ལ་གདམས་པ་བསྟན་པའི་ཕྱིར། རྣལ་འབྱོར་འགྲོ་ལ་བདག་གིས་སྙིང་པོ་སྨྲ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། གང་ལ་གདམས་པ་དང་། གང་གདམས་པ་དང་། ཚུལ་ཇི་ལྟར་གདམས་པའོ། །

[Block 113]
རྣལ་འབྱོར་པ་དང་སྙིང་པོའི་དོན་དང་དྲན་པ་ལ་གདམས་པའོ། །

[Block 114]
གང་ལ་གདམས་ན༌[^31]རྣལ་འབྱོར་པ་རྣམས་ལའོ། །

[Block 115]
གང་གདམས་ན་སྙིང་པོ་སྟེ་འོད་གསལ་བའོ། །

[Block 116]
ཇི་ལྟར་གདམས་ན་དྲན་པ་ལ་སོགས་པའོ། །

[Block 117]
རྣམ་རྟོག་རྒྱུ་བ་ནི་འཇིག་རྟེན་པའི་སེམས་སོ། །

[Block 118]
མ་ལྟ་བ་ནི་མ་འབྲང་བར་གདམས་པའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། གང་འཁོར་བ་སེམས་དང་། གང་གིས་འཁོར་ན་རླུང་གིས་དང་། ཚུལ་ཇི་ལྟར་འཁོར་ན་འཇིག་རྟེན་པའི་སེམས་རྣམས་ཀྱིས་ཉིན་མཚན་དུ་བག་ཆགས་སྣ་ཚོགས་གཞག་པའི་དབང་གིས་འཁོར་བ་སྟེ། དེ་བས༌[^32]ན།

[Block 119]
འཁོར་བར་བྱེད་པའི་རྣམ་རྟོག་གཞན་མིན་ལ། །འཁྲུལ་བར་བྱེད་པའི་མ་རིག་པ་གཞན་མིན་ནོ། །

[Block 120]
འོ་ན་ཅི་ཞེ་ན། སེམས་དང་རླུང་ངོ་། །འཇིག་རྟེན་པའི་སེམས་བཤད་པ་ནི་ཆགས་སྡང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ་གོ་སླའོ། །ཤེས་རབ་ལ་གདམས་པ་ནི། གང་གང་རྣམ་བརྟགས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་སེམས་དང་རླུང་གི་རྣམ་པར་འཁྲུལ་པ་ལ་བརྟེན་ནས། འཇིག་རྟེན་པའི་སེམས་གང་དང་གང་བྱུང་བ་ལ་ཤེས་རབ་ཀྱིས་བརྟགས་ན་བརྫུན་པ་དང་ཕྱིན་ཅི་ལོག་ཏུ་རྟོགས་ལ། སྙིང་པོའི་དོན་ལ་ངེས་པར་བརྟགས་ན་བདེ་བ་ཆེན་པོའོ། །

[Block 121]
དེ་བས་ན། འདི་ལྟའི་ཏིང་འཛིན་བདེ་བ་ཆེན་པོར་སྨྲ། །ཞེས་བྱ་སྟེ། འོད་གསལ་ལ་དབང་པོ་ལྔས་དབང་བྱས་པའོ། །

[Block 122]
སྲིད་པའི་འཁྲུལ་པ་མ་ལུས་བཅད་པས་སྐྱེ་བ་དང་འཆི་བའི་འཇིགས་པ་དང་། ནད་དང་གནོད་པའི་སྡུག་བསྔལ་གང་ཡང་མེད་དོ། །

[Block 123]
ད་ནི་རང་བཞིན་མ་ཤེས་ན་འདོད་པའི་ཡོན་ཏན་རྣམས་ལ་ཆགས་པས་འཆིང་བར་བསྟན་པའི་ཕྱིར། རི་དགས་སྨིག་རྒྱུ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ་གོ་སླའོ། །

[Block 124]
གྲོང་དུ་ལོངས་སྤྱོད་བདེ་བ་ཚོལ་ཞེས་བྱ་བ་ལ་སོགས་པས་འཆིང་བའི་དཔེ་བསྟན་པའོ། །

[Block 125]
ད་ནི་རང་བཞིན་ཤེས་ན་གྲོལ་བའི་རྒྱུར་བསྟན་པའི་ཕྱིར། གང་ཞིག་ངོ་བོ་ཤེས་པས་གར་ཡང་འགྲོ་མེད་པའི། །ཏིང་འཛིན་རོལ་པས་བསམ་མི་ཁྱབ་པར་སྤྲོ། །ཞེས་པ་ལ། དངོས་པོ་ཐམས་ཅད་སེམས་རླུང་གི་རྣམ་འཕྲུལ་དུ་ཤེས་ལ་དེ་མ་སྐྱེས་པར་ཤེས་ནའོ། །

[Block 126]
ད་ནི་མཚོན་བྱེད་ཀྱི་བདེ་བ་ལ་ཞེན་ན་དེ་ཉིད་མི་མཐོང་བར་བསྟན་པའི་ཕྱིར། གང་ལ་ཡིད་ཀྱི་བྱ་རྒོད་ཅེས་བྱ་བ་ལ་སོགས་པ་ལ།

[Block 127 [HEADING]]
## དེ་ལ་དཔེ་གཉིས། ^5-0

[Block 128]
དེ་ལ་དཔེ་གཉིས་ཏེ། བྱ་རྒོད་རྟེན་པའི་ཤིང་གི་དཔེ་དང་། ནམ་མཁའི་མེ་ཏོག་ལ་བུང་བས་འཇིབ་པ་མཐོང་བའི་དཔེའོ། །

[Block 129 [HEADING]]
### དང་པོ། ^5-1-0

[Block 130 [HEADING]]
#### བཅིང་བའི་དཔེ། ^5-1-1-0

[Block 131]
དང་པོ་ལ་གཉིས་ཏེ། བཅིང་བ་དང་བཏང་བའི་དཔེའོ། །

[Block 132]
བྱ་རྒོད་གནས་པའི་ཤིང་དེ་བྱ་ཐལ་གྱིས་རྩ་བ་བསྲུལ། མཆུས་ཤུན་པ་བཤུས་པས་ལོ་མ་དང་མེ་ཏོག་མི་སྐྱེ་བ་དེ་བཞིན་དུ་རྣལ་འབྱོར་པས་སེམས་རླུང་འདྲེས་ནས་སེམས་བདེ་བའི་རྣམ་པར་སྐྱེས་པ་ལ་དེར་ཞེན་ན་མེ་ཏོག་དང་འདྲ་བའི་འོད་གསལ་མི་མཐོང་ལ། ལོ་མ་དང་འདྲ་བའི་ཟུང་འཇུག་གི་སྐུ་མི་མཐོང་བའོ། །

[Block 133]
དེའི་ཕྱིར།

[Block 134 [VERSE]]
གང་ལ་ཡིད་ཀྱི་བྱ་རྒོད་རྟེན་ཅིང་གནས་པའི་ཤིང་། །
དེ་ལ་བདེ་བའི་མེ་ཏོག་ལོ་མ་སྐྱེ་བ་མེད། །

[Block 135]
ཅེས་བྱའོ། །

[Block 136]
འོ་ན་དེ་གཉིས་གང་གིས་མཐོང་ཞེ་ན། སེམས་རླུང་བཅིངས་པ་དང་འཇིག་རྟེན་པའི་སེམས་བསད་པས་འོད་གསལ་མཐོང་ལ། བཏང་བས་ཟུང་འཇུག་མཐོང་བའོ། །

[Block 137]
ངེས་པར་ཡིད་ཀྱིས་བྱ་རྒོད་བཅིངས་བསད་ན། །ཞེས་པ་ནི་འོད་གསལ་བའི་ངང་དུ་སེམས་རླུང་བཅིང་བ་དང་བསད་པའོ། །

[Block 138]
དེས་ཅིར་འགྱུར་ཞེ་ན། འཁྲུལ་འཁོར་འཆད་དེ། གཡོ་ཞིང་འགྱུར་བས་མ་ལེགས་བྱེད་པར་གང་ཞིག་འགྱུར། །ཞེས་བྱ་བ་ལ་རླུང་གིས་གཡོ་ཞིང་སེམས་བརྒྱ་དྲུག་ཅུར་འགྱུར་བ་བཅད་པས་མ་ལེགས་བྱེད་པ་སྟེ། དགེ་མི་དགེའི་བག་ཆགས་འཇོག་པར་ཇི་ལྟར་འགྱུར་ཏེ་མི་འགྱུར་རོ། །

[Block 139 [HEADING]]
#### བཏང་བའི་དཔེ། ^5-1-2-0

[Block 140]
བྱ་རྒོད་བཅིངས་པ་ལས་བཏང་ན་ཤ་ཁྲག་འཐུང་བས་བཀྲེས་པ་མེད་པ་དང་འདྲ་བར་ཡིད་ཀྱི་ལུས་ཆུ་ཟླ་ལྟར་གནས་པ་དེ་ཤེས་རབ་ཀྱིས་གཉིས་སུ་མཐོང་བའི་ཕྱོགས་བཅོམ་པས་དེ་ཉིད་གྲོགས་ཡིན་ནོ། །

[Block 141]
སྣང་བའི་དངོས་པོ་གང་ཆུ་ཟླ་ལྟར་ཤེས་པའི་རྣལ་འབྱོར་པ་དེ་ལ་གནས་གར་ཡང་གཟུང་འཛིན་གྱིས་གནོད་པའི་འབད་པ་བྱེད་པ་མེད་དོ། །

[Block 142]
དེ་བས་ན་འོད་གསལ་སྟོང་ཉིད་བརྟན་པར་བྱ་བ་ལས་འཁྲུལ་པ་སྤང་དུ་མེད་པའི་ཕྱིར། སྟོང་ཉིད་བརྟན་གྱིས་འཁྲུལ་པ་སྤང་དུ་མེད། །ཅེས་བྱའོ། །

[Block 143]
འཁྲུལ་པས་འཆིང་སྤངས་སེམས་པར་མ་བྱེད་ཅིག །ཅེས་བྱ་བ་ནི་འོད་གསལ་བས་ས་ཧ་ཛའི་རྣལ་འབྱོར་མ་རྟོགས་པར་འཁྲུལ་པའི་རྣལ་འབྱོར་གང་གིས་ཀྱང་འཇིག་རྟེན་པའི་སེམས་འཆིང་བ་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 144 [VERSE]]
གང་གང་ལས་བྱུང་དེ་ནི་ངེས་ལྟོས༌[^33]ལ། །
མི་རྟོག་ཏིང་ངེ་འཛིན་གྱིས་དེ་གསལ་གྱིས། །

[Block 145]
ཞེས་བྱ་བ་ལ་འཇིག་རྟེན་པའི་སེམས༌[^34]གང་དང་གང་བྱུང་བ་དེ་ཤེས་རབ་ཀྱི་མིག་གིས་ལྟོས་ལ་གསལ་བར་གྱིས་ཞེས་བྱ། གང་གིས་ཤེས༌[^35]ན་མི་རྟོག་ཏིང་ངེ་འཛིན་གྱིས་ཏེ་མི་རྟོག་པ་ཤེས་རབ་དང་། ཏིང་ངེ་འཛིན་དངོས་སུ་སྨོས་ལ་གསུམ་ཤུགས་ཀྱིས་ཤེས་པར་བྱ་སྟེ་དབང་པོ་ལྔ་ལྡན་གྱིས་གསལ༌[^36]བའོ། །
--- END BLOCKS ---
