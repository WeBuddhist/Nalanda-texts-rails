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

[Block 146]
མཇུག་བསྡུ་བའི་ཚུལ་གྱིས་གདམས་པ་ནི། རྣམ་རྟོག་དྲི་མ་ཆེན་པོ་མ་ལུས་ཁྲུས། །ནམ་མཁའི་མེ་ཏོག་དང་འདྲ་དངོས་པོ་མཉམ་པར་རྟོགས།[^37] །ཞེས་བྱ་བ་ནི། རྟོག་པའི་དྲི་མ་འཁྲུ་བ་ལ་འཁྲུལ་པའི་དངོས་པོ་ནམ་མཁའི་མེ་ཏོག་དང་འདྲ་བར་ཤེས་རབ་ཀྱིས་བརྟགས་པ་དང་ཤེས་ཤིང་གོམས་པར་བྱ་བའི་ལམ་དེ་ཟུང་འཇུག་ཏུ་མཉམ་པར་བརྟག་པར་བྱའོ། །

[Block 147 [HEADING]]
### དཔེ་གཉིས་པ་ལྡོག་པའི་དབང་དུ་བྱས་པ། ^5-2-0

[Block 148]
དཔེ་གཉིས་པ་ལྡོག་པའི་དབང་དུ་བྱས་ནས།

[Block 149 [VERSE]]
ངེས་སྦྱངས་བག་ཆགས་བྲལ་བས་རྣལ་འབྱོར་མ་མཐོང་བ། །
ནམ་མཁའི་མེ་ཏོག་བུང་བས་འཇིབ་པ་མཐོང་བ་འདྲ། །

[Block 150]
ཞེས་བྱ་བ་ནི། མཚོན་བྱེད་ཀྱི་བདེ་བ་དེ་ལ་སེམས་ངེས་པར་སྦྱངས་པས་འཇིག་རྟེན་པའི་སེམས་རྣམས་རྒྱུ་བའི་བག་ཆགས་དང་བྲལ་ཡང་རྣལ་འབྱོར་ཏེ། དབྱིངས་དང་རིག་པ་གཉིས་མེད་མ་མཐོང་བ་ནི་རླུང༌[^38]སེམས་རང་བཞིན་ལ་མ་བཅུག་པར་ཚོར་བ་བདེ་བས་ཀུན་ནས་དཀྲིས་པ་དང་བཅས་པ་ལ་ཞེན་པ་ནི་ནམ་མཁའི་མེ་ཏོག་ལ་བུང་བས་འཇིབ་པ་མཐོང་བ་དང་འདྲ་བའི་ཕྱིར་རོ། །

[Block 151]
འོ་ན་མཚོན་བྱེད་དུ་བཤད་པ་ཅི་ཞེ་ན། དེ་ནི་ཉེས་པ་མེད་དེ་མཛུབ་མོས་ཟླ་བ་མཚོན་པ་དང་འདྲ་བར། རླུང་སེམས་བདེ་བའི་རྣམ་པར་བརླབས་ནས་བརྟན་པ་དང་། རླུང་སེམས་རང་བཞིན་ལ་གཞུག་དགོས་པའི་ཕྱིར་རོ། །

[Block 152]
དེ་ཉིད་ལ་ཞེན་ན་དོན་དམ་པ་ལ་སླུ་བ་དང་འཁྲུལ་པ་ཞེས་བྱ་སྟེ་ལྟོས་པས་གཞག་པའི༌[^39]ཕྱིར་རོ། །

[Block 153]
འོ་ན་ཅི་ཞེ་ན། རྗེས་སུ་འགྲོ་བའི་སྒོ་ནས་བསྟན་པ་ནི་ངེས་སྦྱངས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། དེ་ལྟར་རླུང་སེམས་བདེ་བའི་རྣམ་པར་ངེས་པར་སྦྱངས་པས་འཇིག་རྟེན་པའི་སེམས་བརྒྱ་དྲུག་ཅུས་སྟོང་པའི་སྟོང་པ་ཆེན་པོ་དེ་བླ་མ་དམ་པ་དང་། སངས་རྒྱས་ཀྱི་ཚིག་བཞིན་དུ་ཐམས་ཅད་སྟོང་པ་འོད་གསལ་དུ་བཅུག་ལ་བསྒོམ། སྤྱོད་པ་རྣམ་པར་དག་པ་སྟེ་དེ་ལས་སྒྱུ་མ་ལྟ་བུའི་ལྷའི་སྐུར་ལངས་ལ་ལྷའི་སྐུ་དེ་ཡང་ཆུ་ཟླ་ལྟར་ཤེས་པའི་ཚུལ་གྱིས་དགེ་བའི་ཆོས་ཐམས་ཅད་རྫོགས་པར་བྱའོ། །

[Block 154]
འོ་ན་ཐམས་ཅད་སྟོང་པ་འོད་གསལ་འབའ་ཞིག་གོམས་པར་བྱ་བ་ལས་སྤྲོས་པས་ཅི་བྱེད་ཅེ་ན། སྤྲོས་པ་ལྟར་སྣང་ཡང་འཇིག་རྟེན་པ་རྣམས་ཀྱི་སྤྲོས་པའི་གནས་པ་དང་འགལ་བ་ཞེས་བྱའོ། །

[Block 155]
དེ་ནི་ནམ་མཁའི་མེ་ཏོག་ལ་བུང་བས་འཇིབ་པ་དང་འདྲ་བའི་ཕྱག་རྒྱ་དང་། བདག་གཞན་དུ་ལྟ་བའི་འཁྲུལ་པ་འོད་གསལ་གྱིས་སྦྱོང་བའོ། །

[Block 156]
འོད་གསལ་དུ་ཇི་ལྟར་བསྒོམ་ཞེ་ན། འཇིག་རྟེན་སྤྲོས་ལ་རྡོ་རྗེ་ཕབ་ནས་ནི། །ཞེས་བྱ་བ་ནི་སྣོད་བཅུད་ཐམས་ཅད་འོད་གསལ་དུ་བཞུ་ལ་ཚུར་བསྡུའོ། །

[Block 157]
འཇིག༌[^40]འཛིན་ངོ་ཚ་ཨ་ཝ་དྷཱུ་ཏཱིས་སྤོངས། །ཞེས་བྱ་བ་ནི་རླུང་སེམས་དང་བཅས་པ་རྩ་དབུ་མར་བཅུག་ལ་འོད་གསལ་བསྒོམ་པའོ། །

[Block 158]
དཔེ་བཞི་པའི་མཇུག་བསྡུ་བའི་ཕྱིར། བྱང་ཆུབ་སྨོན་པ་ཞེས་བྱ་སྟེ་བཤད་ཟིན་ཏོ། །

[Block 159]
སྙིང་རྗེ་དང་ཤེས་རབ་གཉིས་མེད་དུ་ངེས་པར་སྦྱང་བ་འདིར་ཐེག་པ་ཆེན་པོའི་ལམ་ཐམས་ཅད་འདུས་པའི་ཕྱིར་རོ། །

[Block 160]
དེ་ལྟ་བུའི་ལམ་དེ་ནི་མཁའ་འགྲོ་མའི་དམོད་སྔགས་དང་འདྲ་བ་དེ་གང་ལས་རྙེད་ཅེ་ན་བླ་མ་ལས་ཏེ་དེ་མེད་ན་དེ་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 161]
དེའི་ཕྱིར། རྣལ་འབྱོར་མ་ཉམས་མྱོང་ན་རྣལ་འབྱོར་པར་འགྱུར་བས། །ཞེས་བྱ་བ་ནི། སྙིང་རྗེ་དང་ཤེས་རབ་དང་། དབྱིངས་དང་རིག་པ་གཉིས་མེད་དུ་བསྒོམས་པ་ལ་བྱ་ལ་དེ་བླ་མ་ལ་རག་ལས་ཏེ། དཔེར་ན་གཞོན་ནུ་མའི་བདེ་བ་སྐྱེས་པ་ལ་རག་ལས་པ་དང་འདྲའོ། །

[Block 162]
དེ་བས་བླ་མ་དམ་པའི་ཐབས་གང་གིས་སྲིད་པའི་འཁྲུལ་པ་དེ་ཚེ་འདི་ལ་གཅོད་པས་དེའི་ལུང་ལས་གཅེས་པར་བྱ་བ་ཅི་ཡང་མེད་དོ། །

[Block 163]
དེའི་ཕྱིར་བདག་ལ་ལེགས་སུ་འདོད་པའི་མཁས་པ་རྣམས་ཀྱིས་དམ་པ་བསྟེན་པར་བྱའོ། །

[Block 164 [VERSE]]
སྙིང་རྗེས་གཞན་ཕན་ཞེས་པ་ནི་གོ་སླའོ། །
ད་ནི་གཞུང་ཉེ་བར་བསྡུ་བའི་ཕྱིར།
ཡི་གེ་ཤྲཱི་ནི་གཉིས་མེད་ཡེ་ཤེས་ཏེ། །

[Block 165]
ཞེས་བྱ་བ་ལ་སོགས་པ་ནི། ལམ་དེའི་མཇུག་སྡུད་དེ། བདེན་པ་གཉིས་ཀྱི་མཚན་ཉིད་དང་། དེ་གཉིས་སུ་མེད་པ་ཟུང་འཇུག་སྟོན་པ་སྟེ། དེའི་མིང་གི་རྣམ་གྲངས་དོན་དམ་པའི་ཧེ་རུ་ཀ་དང་། རྡོ་རྗེ་སེམས་དཔའ་དང་། བདེན་པ་གཉིས་ཀྱི་ཚུལ་ལ་གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 166 [HEADING]]
## བསྔོ་བ། ^a-0

[Block 167 [VERSE]]
ཆོས་ཚུལ་ཟབ་མོ་རྒྱ་མཚོ་ལྟ་བུ་འདི། །
གཞན་ལ་ཕན་པའི་བསམ་པས་བྲིས་པ་ཡིན།
འདི་ལ་ཉེས་པར་གྱུར་པ་དེ་དག་ཀུན། །
འཕགས་དང་མཁའ་འགྲོ་རྣམས་ཀྱིས་བཟོད་པར་མཛོད། །

[Block 168 [VERSE]]
ཐ་མའི་དུས་སུ་གྱུར་པ་ན། །
ཚེ་ཐུང་ནད་མང་ལོངས་སྤྱོད་དམན། །
རྐྱེན་ངན་བར་ཆད་མང་བ་ཡིས། །
ཡུན་རིང་གནས་པའི་མཐུ་མེད་པས། །

[Block 169 [VERSE]]
ཚིག་རྗེས་བཅད་པར་མི་ནུས་ཀྱིས། །
བཤེས་གཉེན་དམ་པ་བསྟེན་བྱ་སྟེ། །
ཤིན་ཏུ་བརྩོན་པའི་སེམས་ལྡན་པས། །
གཡང་ས་རབ་ཏུ་དྲན་བྱ་སྟེ། །

[Block 170 [VERSE]]
གཞན་དག་གྲོལ་བར་བྱ་བའི་ཕྱིར། །
སྙིང་པོའི་དོན་འདི་བཀྲོལ་བ་ཡིན། །

[Block 171 [VERSE]]
བརྩེ་བས་འདི་བཀྲོལ་བསོད་ནམས་ཀྱིས། །
ལམ་དམན་ཞུགས་པའི་འགྲོ་བ་རྣམས། །
དམ་པའི་ལམ་ལ་གནས་པར་ཤོག །

[Block 172 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 173 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 174]
རྡོ་རྗེའི་གླུའི་དོན་གསལ་བར་བྱེད་པ་མཁས་པ་ཆེན་པོ་དཱི་པཾ་ཀ་ར་ཤྲཱི་ཛྙཱ་ནས་མཛད་པ་རྫོགས་སོ།། །།

[Block 175 [HEADING]]
### འགྱུར་བྱང། ^b-2-0

[Block 176]
པཎྜི་ཏ་དེ་ཉིད་དང་། དགེ་སློང་ཚུལ་ཁྲིམས་རྒྱལ་བས་བསྒྱུར་ཏེ་གཏན་ལ་ཕབ་པའོ།། །།

[Block 177]
[^1]: ལས་ས་ ༼སྣར། པེ།༽ ལས་པ་
[^2]: དེའི་ཕྱིར་ ༼སྣར། པེ།༽ དེའི་
[^3]: བསྟེན་པ་ ༼སྣར། པེ།༽ རྟེན་པ་
[^4]: ལྷག་པའི་ ༼སྣར། པེ།༽ ལྡོག་པའི་
[^5]: གྱུར། ༼སྣར། པེ།༽ འགྱུར།
[^6]: མཚོན་བྱ་ ༼སྣར། པེ།༽ མཚོན་བྱ་དང་
[^7]: ། །མཛེས་མ་མཆོག་ལྡན་ ༼སྣར། པེ།༽ མཛེས་མ་མཆོག་
[^8]: དབེན་པ་ ༼སྣར། པེ།༽ བདེན་པ་
[^9]: སྒྲིབ་པ་ ༼སྣར།༽ བསྒྲུབ་པ་ ༼པེ།༽ སྒྲུབ་པ་
[^10]: ཉོན་མོངས་པའི་ ༼སྣར། པེ།༽ ཉོན་མོངས་ཀྱིས་
[^11]: མཚོན་བྱ་ ༼སྣར། པེ།༽ མཚོན་ཆ་
[^12]: ལ་ ༼སྣར། པེ།༽ ནི་
[^13]: རྣམ་ ༼པེ།༽ རྣམ་པར་
[^14]: བརླབས་པས་ ༼སྣར། པེ།༽ བླངས་པས་
[^15]: མཚོན་བྱའི་ ༼སྣར། པེ།༽ མཚོན་ཆའི་
[^16]: ངོ་བོ་ཡང་ ༼སྣར། པེ།༽ ངོ་བོ་ཡོངས་
[^17]: ལུས་ ༼སྣར། པེ།༽ ལུས་པ་
[^18]: བདག་མེད་མ་དེ་ ༼སྣར། པེ།༽ བདག་མེད་བདེ་
[^19]: མཐའ་ ༼སྣར།༽ མཐའི་
[^20]: བྱུང་བ། ༼སྣར། པེ།༽ བྱུང་བའི།
[^21]: བྱམས་པ་དང་ ༼སྣར། པེ།༽ བྱམས་པ་
[^22]: བརྟགས་ ༼སྣར། པེ།༽ བརྟག་
[^23]: བསམས་ ༼སྣར། པེ།༽ བསམ་
[^24]: དེའི་ ༼སྣར། པེ།༽ དེ་
[^25]: ཐབས་ཀྱིས་ ༼སྣར། པེ།༽ ཐབས་ཀྱི་
[^26]: ལྟ་བའི་ ༼སྣར། པེ།༽ བལྟ་བའི་
[^27]: དཔེར་ན་ ༼སྣར། པེ།༽ དཔེར་ན་ནི་
[^28]: མིག་འཕྲུལ་ ༼སྣར། པེ།༽ མིག་འཕྲུལ་ཅན་
[^29]: འོངས་པའི་བརྟགས་ ༼སྣར། པེ།༽ འོང་བའི་བརྟག་
[^30]: ཐབས་རྣམས་ ༼སྣར། པེ།༽ ཐབས་
[^31]: གདམས་ན་ ༼སྣར། པེ།༽ གདམས་པ་
[^32]: དེ་བས་ ༼སྣར། པེ།༽ བདེ་བས་
[^33]: ལྟོས་ ༼སྣར། པེ།༽ བལྟོས་
[^34]: ལ་འཇིག་རྟེན་པའི་སེམས་ ༼སྣར། པེ།༽ འཇིག་རྟེན་པའི་
[^35]: གིས་ཤེས་ ༼སྣར། པེ།༽ གིས་ཞེ་
[^36]: གསལ་ ༼སྣར། པེ།༽ བསལ་
[^37]: རྟོགས། ༼སྣར། པེ།༽ རྟོག།
[^38]: རླུང་ ༼སྣར། པེ།༽ རླུང་དང་
[^39]: གཞག་པའི་ ༼སྣར། པེ།༽ བཞག་པའི་
[^40]: འཇིག་ ༼སྣར། པེ།༽ འཇིགས་
--- END BLOCKS ---
