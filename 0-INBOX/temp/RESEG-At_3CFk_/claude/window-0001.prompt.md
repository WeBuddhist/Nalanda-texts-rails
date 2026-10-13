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
མཚོན་པར་བྱ་བ་མཆོག་ཏུ་བདེ་ཆེན་ཞེས་པ་སྟེ། །ཞེས་པའི་ཚིག་གཉིས་པོ་གོ་སླའོ། །

[Block 37]
ཁྱེད་ཀྱིས་བརྟགས་ཤིང་བསྐྱེད་པའི་ཚུལ་ནི་གང་ཡིན་པ། །ཞེས་བྱ་བ་ནི་བདེན་པ་གཉིས་ཀྱི་མཚན་ཉིད་དང་མི་ལྡན་པའི་བརྟགས་པའི་རྣལ་འབྱོར་དགག་པ་སྟེ་གོ་སླའོ། །

[Block 38 [VERSE]]
ཇི་སྲིད་དེ་ནི་རང་བཞིན་ཡོངས་སུ་མི་ཤེས་པས། །
དེ་སྲིད་བྱང་ཆུབ་བླ་ན་མེད་པ་ཇི་ལྟར་འགྲུབ། །
ཅེས་བྱ་བ་ནི་འོད་གསལ་དང་ཟུང་འཇུག་གོ། །
རྣམ་རྟོག་སྤྲོས་པ་མ་ལུས་དངོས་པོ་མེད་པ་སྟེ། །

[Block 39]
ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་པའི་སེམས་བརྒྱ་དྲུག་ཅུའོ། །

[Block 40]
དེ་དག་མཆོག་ཏུ་བདེ་བ་ཆེན་པོ་འོད་གསལ་གྱི་རང་བཞིན་གྱིས་སྦྱངས་པ་ཡིན་ཞེས་བྱའོ། །

[Block 41 [HEADING]]
##### དེའི་རྒྱུ། ^1-2-5-1-0

[Block 42 [HEADING]]
###### ཐུན་མོང་གི་ཚོགས། ^1-2-5-1-1-0

[Block 43]
དེའི་རྒྱུ་ཅི་ཞེ་ན། འཇིག་རྟེན་གྱི་ཆོས་བརྒྱད་ལ་མཉམ་པ་ཉིད་དུ་བྱ་བ་དང་། །ཏིང་ངེ་འཛིན་གྱི་མཆོག་ལ་གནས་པར་འགྱུར་བ་སྟེ། དེ་ལ་གཉིས། ཐུན་མོང་གི་ཚོགས་ཚུལ་ཁྲིམས་དང་ལྡན་པ་དང་། ལོངས་སྤྱོད་ལ་མི་ལྟོས་པ་དང་། བཟོད་པ་དང་ལྡན་པ་དང་། དམ་བཅའ་བརྟན་པ་དང་། འདུ་འཛི་སྤོང་བ་དང་། ཤེས་བཞིན་དང་ལྡན་པ་དང་། བདེན་པ་གཉིས་ལ་མ་ཡེངས་པའི་དྲན་པ་དང་། བྱ་བ་དང་དེ་མ་ཡིན་པ་ཤེས་པ་དང་། སྒྲིབ་པ་ལྔ་སྦོང་བ་དང་། ཟས་ཀྱི་ཚོད་རིག་པ་དང་། འཇིག་རྟེན་པའི་སྤྱོད་པ་ལ་བློ་རྣལ་དུ་ཕེབས་པའོ། །

[Block 44 [HEADING]]
###### ཐུན་མོང་མ་ཡིན་པ། ^1-2-5-1-2-0

[Block 45]
ཐུན་མོང་མ་ཡིན་པའི་དབང་བཞི་ལེགས་པར་ཐོབ་པ། བྱང་ཆུབ་ཀྱི་སེམས་བརྟན་པ། བླ་མ་ལ་གུས་པའོ། །

[Block 46]
དེ་ལྟ་བུའི་ཚོགས་ལ་གནས་ན་ལུས་ངག་ཡིད་གསུམ་དང་། སྒྲིབ་པ་གསུམ་ཤིན་ཏུ་རྣམ་པར་དག་པར་འགྱུར་བ་སྟེ་སྤྲོས་པའི་སྤྱོད་པ་མ་ལུས་པ་སྤོང་པའོ། །

[Block 47]
རྣམ་པར་རྟོག་པ་ཞེས་བྱ་བའི་ཚིག་གཉིས་སྤྲོས་པའི་རྣལ་འབྱོར་དགག་པ་སྟེ་གོ་སླའོ། །

[Block 48]
ཇི་སྲིད་སྲིད་པ་གསུམ་དང་། ཅིར་སྣང་འཇིག་རྟེན་པའི་སེམས་སྤྲོས་པ་དང་། རྣམ་རྟོག་མ་ལུས་པ་དོན་ཡོད་པ་མ་ཡིན་པས། དེ༌[^9]ཕྱིར་བསལ་བ་དེ་ནི་དེ་བཞིན་མཆོག་ཏུ་རྣམ་པར་དག་པའི་རང་བཞིན་ནོ། །

[Block 49]
དེ་ལ་དབང་པོ་ལྔས་དབང་བྱས་པའི་ཏིང་ངེ་འཛིན་གྱི་མེས་ཉོན་མོངས་པའི་སོག་མ་འཇིག་རྟེན་པའི་སེམས་རྣམ་པར་བསྲེགས་པས༌[^10]གང་གི་ཚེ་འཇིག་རྟེན་གསུམ་དང་། འཇིག་རྟེན་པའི་སེམས་རྣམས་ནམ་མཁའི་དཀྱིལ་ལྟར་ཡོངས་སུ་ཤེས་པ་དེའི་ཚེ། འགྲོ་བ་མ་ལུས་པའི་རྟོག་པ་ནུབ་ནས་ནམ་མཁའ་བཞིན་དུ་འགྱུར་རོ། །

[Block 50]
དེ་ལྟར་ཆོས་ཐམས་ཅད་སྣང་ལ་ངེས་པའི་ཤེས་པ་སྐྱེ་བའི་དྲི་མ་སྦྱོང་དགོས་པ་གསུངས་པ། རྣམ་རྟོག་རབ་རིབ་ཀྱིས་རྨོངས་ལྡོངས་པར་མ་བྱེད་ཅིག །ཅེས་བྱའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། འགྲོ་བ་གསུམ་པོ་རང་བཞིན་དག་པའི་ངང་དུ་ཁྱད་པར་གང་ཡང་མེད་ལ། རྟོག་པས་བྱེ་བྲག་བྱས་པའོ། །

[Block 51]
དེའི་དོན་རྒྱས་པར་བསྟན་པའི་ཕྱིར། རབ་རིབ་ཅན་གྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ་གོ་སླའོ། །

[Block 52]
ད་ནི་འོད་གསལ་བའི་ཏིང་ངེ་འཛིན་གྱིས་ལས་དང་ཉོན་མོངས་པ་སྐྱེ་བ་དག་པར་མ་བྱས་བར་དུ། ལས་འབྲས་ཤིན་ཏུ་ཕྲ་བ་ལ་ཡང་འཛེམ་དགོས་པ་བསྟན་པའི་ཕྱིར། སྡིག་པའི་རྣམ་སྨིན་ཆོམ་རྐུན་འཇིགས་པ་མཐོང་བ་ཡིས། ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ་གོ་སླའོ། །

[Block 53]
དེ་ཁོ་ན་ཉིད་ཀྱི༌[^11]ཉི་མ་འོད་གསལ་བའི་ཏིང་ངེ་འཛིན་གྱིས་ལས་ཀྱི་འཇུག་པ་བཅད་ནས། བཟོད་པ་དེ་དང་ལྡན་པ་བཞིན་དུ་རང་གི་རྒྱུད་ལ་དགེ་བའི་སེམས་རྫོགས་པར་བྱེད་པ་ལ་སོགས་པའི་ཚེ་ནི་དེ་མི་དགོས་པས༌[^12]དེ་སྲིད་ཅི་དགར་སྤྱོད་ཅེས་བྱའོ། །

[Block 54]
དེ་བས་ན་དེ་སྲིད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྟེ་གོ་སླའོ། །

[Block 55]
དེ་ལྟར་ལྟ་བ་དང་སྤྱོད་པ་དག་ལ་བྲམ་ཟེ་ཞེས་བྱའི། རིགས་ལ་སོགས་པ་མ་ཡིན་པར་བསྟན་པའི་ཕྱིར་གཅེར་བུ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ་གོ་སླའོ། །

[Block 56]
ལམ་ཕྱིན་ཅི་མ་ལོག་པ་དང་ལྡན་ན་རིགས་ལ༌[^13]མི་ལྟོས་པར་བསྟན་པའི་ཕྱིར། དམན་པའི་རིགས་སུ་སྐྱེས་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 57]
འཁྲུལ་པའི་དབང་གིས་རྟག་ཏུ་འཁོར་བ་དེ་ལས་བཟློག་པར་གདམས་པ་ནི། ཡང་དང་ཡང་དུ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^14]མཇུག་བསྡུས་ཏེ་གདམས་པ། ཀྭའི་ཞེས་བོས་ནས་སེམས་ཁྱོད་རང་གིས་རང་གི་དྲི་མ་ཁྲུས། །ཞེས་བྱ་བ་ལ། བཞིན་གྱི་དྲི་མ་མེ་ལོང༌[^15]ལ་བལྟས་ནས་སེལ་བ་ལྟར། མེ་ལོང་དང་འདྲ་བའི་བླ་མ་དང་། ཆུ་དང་འདྲ་བའི་མན་ངག་གིས་མ་རིག་པའི་དྲི་མས་གང་གོས་པ་དེ་ཟད་པར་བྱའོ། །

[Block 58]
དེའི་ཕྱིར་བླ་མའི་མན་ངག་གི་ཆུས་རྟོག་པའི་དྲི་མ་བཀྲུ་བར་བྱའོ། །

[Block 59]
ཚུལ་ཇི་ལྟར་བཀྲུ་ཞེ་ན།

[Block 60 [VERSE]]
སེམས་ཁྱོད་ཡོངས་སུ་གོ་བར་གྱིས་ལ་རང་ལ་ནི། །
ཡོངས་སུ་བལྟ་ཞིང་གཏི་མུག་མུན་པ་ཆེན་པོ་སྦྱོངས། །

[Block 61]
ཞེས་བྱ་བ་ལ་ཆོས་ཐམས་ཅད་སེམས་དང་རླུང་གི་རྣམ་པར་འཕྲུལ་བར་གོ་བར་གྱིས་ལ་རང་ལ་རང་སྟེ། རླུང་དང་སེམས་རང་བཞིན་ལ་བཅུག་ལ་ནམ་མཁའ་དང་འདྲ་བར་ལྟོས་ཞེས་བྱའོ། །

[Block 62]
དེ་ལྟ་བུའི་ཐུབ་པའི་ཆོས་ཀྱི་གཏམ་མི་ཉན་པ་དང་། དེའི་སྐལ་བ་མེད་པ་ནི་མེ་ལྟར་སྣང་བ་ཡིན་ནོ། །

[Block 63]
དེ་བས་ན་ངེས་པར་འཇིག་རྟེན་ཕ་རོལ་དུ་འགྲོ་དགོས་པ་ཡིད་ལ་བྱས་ལ། ཐུབ་པའི་ཆོས་ཀྱི་གཏམ་བྱང་ཆུབ་ཀྱི་སེམས་ལ་སོགས་པ་མཉན་ཞིང་གོམས་པར་བྱའོ། །

[Block 64]
དེ་ཐོས་ནས་དེ་དང་འགལ་བའི་ལས་མི་བྱ་སྟེ་མནར་མེད་པར་འགྲོ་བ་ལ་དེ་མིན་པ་གང་གིས་ཀྱང་འཛིན་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 65]
དེ་ཐོས་ནས་དེ་ལྟར་དེ་སྦྱངས་ནས་གནས་སྐབས་ཀྱི་འབྲས་བུ་མཐོ་རིས་ལ། མཐར་ཐུག་གི་འབྲས་བུ་བྱང་ཆུབ་འཐོབ་པའོ། །

[Block 66]
མ་རིག་པའི་མུན་པ་ལ་ཆོས་ཏེ་སྐྱབས་སུ་འགྲོ་བ་དང་། བྱང་ཆུབ་ཀྱི་སེམས་ལ་སོགས་པ་དང་། ཐ་མ་བདེ་བ༌[^16]ཆེན་པོའི་ཏིང་ངེ་འཛིན་གྱི་བར་ནི་སྒྲོན་མ་སྟེ་རང་བཞིན་གྱིས་འོད་གསལ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 67]
དེའི་ཕྱིར་སྲིད་པའི་རྒྱ་མཚོ་ཆེན་པོ་སྒྲོལ་བར་བྱེད་པའི་གྲུ་དང་གཟིངས་ཡིན་པས་ངེས་པར་བསྟེན་ཞིང་གོམས་པར་བྱའོ། །

[Block 68 [HEADING]]
## མཇུག་བྱང། ^a-0

[Block 69 [HEADING]]
### མཛད་བྱང། ^a-1-0

[Block 70]
སྤྱོད་པའི་གླུའི་འགྲེལ་པ་རྫོགས་སོ། །

[Block 71]
[^1]: ཏི་ ༼སྣར། པེ།༽ ཏ་
[^2]: དེའི་ ༼སྣར། པེ།༽ དེ་
[^3]: པ་ལ། ༼སྣར། པེ།༽ པའོ། །
[^4]: སྣང་ཡང་ ༼སྣར། པེ།༽ སྣང་བའང་
[^5]: དཀྲུགས་ ༼པེ།༽ དཀྲུག་
[^6]: རླབས་ ༼སྣར། པེ།༽ བརླབས་
[^7]: རླབས་ ༼སྣར། པེ།༽ བརླབས་
[^8]: འོད་གསལ་གྱིས་ ༼སྣར། པེ།༽ འོད་ཀྱི་
[^9]: དེ་ ༼སྣར། པེ།༽ དེའི་
[^10]: བསྲེགས་པས་ ༼སྣར། པེ།༽ བསྲེག་པས་
[^11]: ཁོ་ན་ཉིད་ཀྱི་ ༼སྣར། པེ།༽ ཁོ་ན་
[^12]: དགོས་པས་ ༼སྣར།༽ དགོས་པར་
[^13]: རིགས་ལ་ ༼སྣར།༽ རིགས་
[^14]: པས་ ༼སྣར། པེ།༽ པའི་
[^15]: མེ་ལོང་ ༼སྣར། པེ།༽ མེད་ང་
[^16]: བདེ་བ་ ༼སྣར། པེ།༽ བདེ་
--- END BLOCKS ---
