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
[Block 141]
གང་གིས་བརྗོད་ཅེས་བྱ་བ་ནི་བུམ་པ་དང་། སྣམ་བུ་དང་བ་གླང་དང་། རྟ་ལ་སོགས་པའི་མིང་བརྗོད་པའི་དབང་གིས་བརྗོད་པའོ། །

[Block 142]
གང་གིས་སྟོན་པ་ཞེས་བྱ་བ་ནི་རིང་པོ་དང་ཐུང་ངུ་དང་། དཀར་ཤམ་དང་། སྔོ་བསངས༌[^99]དང་། སྔོན་པོ་དང་། སེར་པོ་ལ་སོགས་པའི་ཡོན་ཏན་བསྟན་པའི་དབང་གིས་བརྗོད་དོ། །

[Block 143]
ཉན་པ་པོ་ཡང་རྗེས་སུ་དག་པའི༌[^100]དབང་གིས་དོན་རྗེས་སུ་རྟོགས་པར༌[^101]བྱེད་པ་སྟེ། གང་གིས་རྟོགས་པ༌[^102]ཞེས་བྱ་བ་ནི་རྗེས་སུ་དཔག་པའི་དབང་གིས་བརྗོད་དོ། །

[Block 144]
གང་གིས་མཐོང་བ་ཞེས་བྱ་བ་དེ་ནི་མངོན་སུམ་གྱི༌[^103]དོན་མཐོང་བའི་དབང་གིས་བརྗོད་དོ། །

[Block 145]
སྒྲ་གང་ལ་ཡང་ཐོགས་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་བརྗོད་པ་ཐམས་ཅད་ལ་དོན་དམ་པ་ཚོལ་བར་འགྱུར་བའོ། །

[Block 146]
ཆོས་ཐམས་ཅད་མཉམ་པ་ཉིད་ཀྱིས་ཡང་དག་པར་སྒྲུབ་པར་འགྱུར་ཏེ་ཞེས་བྱ་བ་ནི་སྒྲ་ཐམས་ཅད་དེ་བཞིན་ཉིད༌[^104]དུ་སྦྱོར་བར་བྱེད་པའོ། །

[Block 147]
སྒྲ་ཤེས་པ་ལ་མཁས་པ་ཡང༌[^105]ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྐད་དང་། བསམ་པ་ཐམས་ཅད་ཤེས་པའོ། །

[Block 148]
དྲན་པ་ནི་མི་བརྗེད་པའོ། །

[Block 149]
བློ་གྲོས་ཞེས་བྱ་བ༌[^106]ནི་དོན་དམ་པའི་རྗེས་སུ་འབྲང་བའི་ཤེས་རབ་སྟེ། བློ་གྲོས་དང་། ཡིད་གཞུངས་པ་དང་། མྱུར་དུ་མང་པོ་འཛིན་པའི་བདག་ཉིད་དེ། དེའི་དབང་གིས་ཤེས་རབ་མྱུར་བ་ཞེས་བྱའོ། །

[Block 150]
བློ་ནི་ཀུན་རྫོབ་ཀྱི་སྤྱོད་ཡུལ་ལོ། །

[Block 151]
ལྷག་མ་ནི་དོན་གསལ་ལོ། །

[Block 152 [HEADING]]
#### ཐེག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ། ^1-1-2-0

[Block 153]
འདི་ནི་ཐེག་པ་ཆེན་པོ་བསྟན་པ་སྟེ། དེ་ལྟར་ཐེག་པ་ཆེན་པོ་བསྟན་པ་ཡོངས་སུ་རྫོགས་པར་བྱས་ནས། ད་ནི་ཞུས་པ་གཉིས་པ་སྐབས་དབྱེ་བ་སྟེ། ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཐེག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ཡིན་ཞེས་ཟེར་བ་ཞེས་བྱ་བ་ནི་འོག་ནས་འབྱུང་བའི༌[^107]ས་བཅུ་པོ་དག་ལ་ཞུགས་པ་ནི་ཐེག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ཞེས་བྱ་སྟེ། དེས་ན༌[^108]ཐེག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ཡིན་ནོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་བསྟན་པ་དང་། བྱང་ཆུབ་སེམས་དཔའི་ས་བཅུ་དང་། ས་ཡོངས་སུ་སྦྱང་བར༌[^109]བྱ་བ་ཞུས་སོ། །

[Block 154]
ཆོས་ཐམས་ཅད་འཕོ་བ་མེད་པས་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ནི་ནམ་མཁའ་དང་མཚུངས་ཏེ། འཕོ་བ་མེད་པས་འཕོ་བ་མེད་པའི་ཡེ་ཤེས་ནི་ས་གཞན་དུ་འཕར་བའི་རྒྱུ་ཡིན་པར་བསྟན་ཏོ། །

[Block 155]
ཆོས་རྣམས་ཀྱི༌[^110]གང་ཡིན་པ་དེ་ལ་ཡང་རློམ་སེམས་སུ་མི་བྱེད་ལ་ས་ཡོངས་སུ་སྦྱོང་བར་ཡང་བྱེད་དོ་ཞེས་བྱ་བས་ས་གཞན་དུ་འཕར་བའི་རྒྱུ་བསྟན་ཏོ། །

[Block 156]
འཕོ་བ་མེད་པ་དང་། འགྲོ་བ་མེད་པ་དང་། འོང་བ་ལ་སོགས་པ་མེད་པའི་ཕྱིར་ཆོས་རྣམས་ཀྱི་ས་ལ་རློམ༌[^111]སེམས་མི་བྱེད་ཀྱང་ལས་རྣམས་མི་བྱེད་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། འདི་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཐབས་མཁས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་བྱ་བ་བསྟན་ཏོ། །

[Block 157]
ཐབས་མཁས་པ་ནི་ཀུན་རྫོབ་དང་། དོན་དམ་པའི་ཚུལ་གཉིས་ཤིན་ཏུ་འགལ་བ་འདྲ་བ༌[^112]ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་དགོས་པ་ཐམས་ཅད་ལ་འགལ་བ་མེད་པར་བསྒྲུབ༌[^113]པའོ། །

[Block 158]
ས་ཡོངས་སུ་སྦྱོང་བ་དེ་དག་ཀྱང་སྔར་གླེངས་ཏེ་བསྟན་ནས། ཕྱིས་བཤད་པའི་འགྲེས་ལ་བཅོམ་ལྡན་འདས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ས་དང་པོ་ལ་གནས་པའི་ལྷག་པའི་བསམ་པ་ཡོངས་སུ་སྦྱང་བར་བགྱི་བ་གང་ལགས་ཞེས་བྱ་བ་ལ་སོགས་པས་བཤད་དོ། །

[Block 159]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་གྱི་ཕྱིར་ཐེག་པ་ཆེན་པོའི་ཡེ་ཤེས་ཡོངས་སུ་ཚོལ་བ་ལ་འཇུག་པ་ཞེས་བྱ་བ་ལ། ཐེག་པ་ཆེན་པོའི༌[^114]ཡེ་ཤེས་ཞེས་བྱ་བ་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི་ཡེ་ཤེས་སོ། །

[Block 160]
དེ་ལ༌[^115]ཚོལ་བ་ནི་སྨོན་ལམ་གདབ་པ༌[^116]དང་། སེམས་བསྐྱེད་པ་སྟེ། འདི་ལྟར་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་དུ་སངས་རྒྱས་ཀྱི་ས་ཡོངས་སུ་ཚོལ་བའོ། །

[Block 161]
འདི་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པའི་དངོས་པོ་ཡོངས་སུ་སྦྱོང་བའོ།། །།

[Block 162]
བམ་པོ་བཅོ་ལྔ་པ། དེ་ལས་ཡོངས་སུ་སྦྱོང་བར་འདོད་པས་ཐོག་མར་བསམ་པ་ཡོངས་སུ༌[^117]སྦྱང་བར་བྱའོ། །

[Block 163]
དེའི་འོག་ཏུ་སྒྲུབ་པ༌[^118]ནི་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པའི་རྩ་བ་ཡིན་པའི་ཕྱིར་ཕན་པའི་སེམས་སུ་བྱའོ། །

[Block 164]
དེ་ཡང་སེམས་ཅན་ཐམས་ཅད་ལ་སེམས་སྙོམས་པ་ལས་འབྱུང་བའི་ཕྱིར་སེམས་མཉམ་པ་ཉིད་དུ་བྱའོ། །

[Block 165]
དང་པོ་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ས་ཡིན་པས་ན་གཏོང་བ་ཡོངས་སུ་སྦྱང་བར་བྱའོ། །

[Block 166]
དག་པའི་ས་ཐོབ་པར་བྱ་བ་ལ་སྔར་བྱ་བ་ཡིན་པས་དགེ་བའི་བཤེས་གཉེན་གདོན་མི་ཟ་བར་དགོས་པའི་ཕྱིར་དེ་ལ་བརྟེན་པར་བྱའོ། །

[Block 167]
དེའི་འོག་ཏུ་དགེ་བའི་བཤེས་གཉེན་ལས་དམ་པའི་ཆོས་མཉན་པར་བྱ་དགོས་པས་ཆོས་ཡོངས་སུ་བཙལ་བར་བྱའོ། །

[Block 168]
རྒྱུད་ཡོངས་སུ་མ་སྨིན་པའི་ཕྱིར་མངོན་པར་འབྱུང་བ་ལ་གནས་པ་ཉིད་དུ་བྱའོ། །

[Block 169]
རྟག་ཏུ་རྒྱུན་མི་ཆད་པར་སངས་རྒྱས་ཀྱི་སྐུ་དང་། སངས་རྒྱས་ཉིད་ལ་འདོད་པར་བྱའོ། །

[Block 170]
ཅི་ནུས་སུ་སེམས་ཅན་ཡོངས་སུ་སྨིན་པར་བྱ་དགོས་པས་བརྩོན་འགྲུས་ལ་ཡོངས་སུ་སྐྱོ་བ་མི་འབྱུང་བར་བྱ་བའི་ཕྱིར་ཆོས་བཤད་པར་བྱའོ། །

[Block 171]
དང་པོ༌[^119]སྨོན་ལམ་ནས་བཟུང་ནས་བདེན་པའི་ཚིག་ལ་གུས་པར་བྱ་སྟེ། འདི་དག་ནི་ཡོངས་སུ་སྦྱང་བ་བཅུ་པོ་དག་གིས་མཚམས་སྦྱར་བའོ། །

[Block 172]
ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ས་ཡིན་པའི༌[^120]ས་གཉིས་པ་ལ་ཡང་ཚུལ་ཁྲིམས་ཡིད་ལ་བྱེད་དོ། །

[Block 173]
སེམས་ཅན་ཐམས་ཅད་ལ་བྱམས་པ་སྤེལ་བའི་ཕྱིར་བྱས་པ་གཟོ་བ་དང་། བྱས་པ་ཚོར་བ་ཡིད་ལ་བྱེད་དོ། །

[Block 174]
སེམས་ཅན་རྣམས་ཀྱི་ཉེས་པ་ལ་མི་ལྟ་བའི་ཕྱིར་བཟོད་པ་ཡིད་ལ་བྱེད་དོ། །

[Block 175]
སེམས་ཅན་གྱི་རྒྱུད་སྣོད་དུ་རུང་བར་བྱ་བའི་ཕྱིར་མཆོག་ཏུ་དགའ་བ་ཡིད་ལ་བྱེད་དོ། །

[Block 176]
རྩོམ་པ་ཐམས་ཅད་ཀྱི་རྩ་བ་ནི་དེ་དག་ཡིན་པས་སེམས་ཅན་ཡོངས་སུ་མི་གཏོང་བ༌[^121]ཡིད་ལ་བྱེད་དོ། །

[Block 177]
བདག་གི་སྡུག་བསྔལ་གྱི་འདུ་ཤེས་རྣམ་པར་བཟློག་པའི་ཕྱིར་སྙིང་རྗེ་ཡིད་ལ་བྱེད་དོ། །

[Block 178]
གུས་པ་བསྐྱེད་པའི་ཕྱིར་བླ་མ་རྣམས་ལ་དད་པས་འཕངས་པར༌[^122]ཡིད་ལ་བྱེད་དོ། །

[Block 179]
བྱང་ཆུབ་ཀྱི་ཚོགས་ཀྱི་ཕྱིར་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡིད་ལ་བྱེད་དེ། ཡིད་ལ་བྱེད་པ་བརྒྱད་དོ། །

[Block 180]
དེ་བཞིན་དུ་ཐམས་ཅད་ལ་ཡང་སྦྱར་བར་བྱའོ། །
--- END BLOCKS ---
