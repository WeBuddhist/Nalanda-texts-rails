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
[Block 1 [HEADING]]
### ༄༅། །རྩ་བའི་ལྟུང་བའི་རྒྱ་ཆེར་འགྲེལ་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། མཱུ་ལ་པཏྟི་ཊཱི་ཀཱ། བོད་སྐད་དུ། རྩ་བའི་ལྟུང་བའི་རྒྱ་ཆེར་འགྲེལ་པ། འཕགས་མ་སྒྲོལ་མ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [HEADING]]
## ལྟུང་བ་བཅུ་བཞི་པོ། ^1-0

[Block 5]
ལྟུང་བ་བཅུ་བཞི་པོ་ནི་དཀྱུས་སུ་བསྡེབས་པ་བདུན་ཏེ། བདུན་པོ་དེ་དག་ལ་ལྟུང་བའི་ངོ་བོ་བདུན་དང་། རྒྱུ་བདུན་དང་། དངོས་པོ་བཅུ་བཞི་ཟུང་ཕྲལ་ན་བཅུ་བཞི་པོ་ཚན་ཚན་གསུམ་མོ། །

[Block 6]
དེ་ལ་ལྟུང་བ་དང་པོ་དང་གཉིས་པའི་ངོ་བོ་དང་རྒྱུ༌[^1]གཅིག་སྟེ། བླ་མ་ལ་བརྙས་པ་ཉིད་བདེ་བར་གཤེགས་པའི་བཀའ་ལས་འདས་པ་སྟེ། དེ་ཡང་།

[Block 7 [VERSE]]
བླ་མ་དང་ནི་རྡོ་རྗེ་འཛིན། །
ཐ་དད་པར་ནི་མི་བརྟག་གོ། །

[Block 8]
ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 9]
དེས་ན་རྡོ་རྗེ་འཛིན་པ་དང་བླ་མ་ཐ་མི་དད་པའི་ཕྱིར་ལྟུང་བ་གཉིས་ངོ་བོ་དང་རྒྱུ་གཅིག །[^2]བརྙས་པའི་ཡུལ་བླ་མ་དེ་ཡང་ཐུན་མོང་གི་ལམ་འཁོར་བ་ཡིད་ལ་བྱས་པ་འདི་ལས་བློ་ལོག་པར༌[^3]བྱས་པ་ཤེས་ཤིང་བྱས་པ་གཟོ་བ་ལ་བརྟེན་ནས་བྱམས་པ་དང་སྙིང་རྗེ་བརྟན་པར་བྱས་པ་དེ་གཉིས་ཀྱི་སྟོབས་ལས་བྱུང་བའི་བྱང་ཆུབ་ཀྱི་སེམས་བརྟན་པར་བྱས་འཇུག་པའི་སྡོམ་པ་དང་ལྡན་པས་མི་མཐུན་པའི་ཕྱོགས། །

[Block 10 [VERSE]]
སྙིང་རྗེ་མེད་ཅིང་ཁྲོ་ལ་གདུང་། །
ཁེངས་ཤིང་ཆགས་ལ་མ་བསྡམས་དང་། །
སྤྱོམས་དང་བཅས་པར་མི་བྱའོ། །

[Block 11]
ཞེས་གསུངས་པས་ཐུན་མོང་གི་ལམ་གྱི་མི་མཐུན་པ་དེ་རྣམས་ལས་ལོག་ནས། ཐུན་མོང་མ་ཡིན་པའི་མཚན་ཉིད་དབང་བཞིའི་སྒོ་ནས་ལྟ་བ་དང་། སྤྱོད་པ་དང་། སྒོམ་པ་གསུམ་གྱི་མན་ངག་དང་ལྡན་པ་དེ་ཡང་དང་ཡང་དུ།

[Block 12 [VERSE]]
གོམས་པར་བྱས་པས་ཡོན་ཏན་དང་། །
བརྟན་ཞིང་དུལ་ལ་བློ་གྲོས་ལྡན། །
བཟོད་ལྡན་དྲང་ལ་གཡོ་སྒྱུ་མེད། །
སྔགས་དང་རྒྱུད་ཀྱི་སྦྱོར་བ་ཤེས། །

[Block 13 [VERSE]]
སྙིང་རྗེ་ལྡན་ཞིང་བསྟན་བཅོས་མཁས། །
དེ་ཉིད་བཅུ་ནི་ཡོངས་སུ་ཤེས། །
དཀྱིལ་འཁོར་འདྲི་བའི་ལས་ལ་མཁས། །
སྔགས་བཤད་པ་ཡི་སྤྱོད་པ་ཤེས། །

[Block 14]
རབ་ཏུ་ཞི་དང་དབང་པོ་དུལ། །ཞེས་བྱ་བས་དེ་ལྟར་ཡོན༌[^4]བཅུ་བཞི་དང་ལྡན་པ་ལྟ་བ་རྣམ་གཉིས་གྲུབ་པར་གནས་པའི་དོན་དང་། ངེས་པར་གྲུབ་པའི་ཐབས་ལྔ་དང་། སྤྱོད་པ་རྣམ་པ་གཉིས་དང་། དབང་རྣམ་པ་བཞིའི་མན་ངག་དང་ལྡན་པའི༌[^5]གྲུབ་པའི་ཚིག་གི་ཉམས་དང་ལྡན་པའི་བླ་མ་ཞེས་བྱ་བ་སྟེ། དེ་ལྟ་བུའི་བླ་མ་དམ་པ་ཉེ་བར་བསྟེན་པའི་སྒོ་ནས། སློབ་མ་དེ་རྫོགས་པའི་བྱང་ཆུབ་ཀྱི༌[^6]སེམས་བརྟན་པར་བྱ་བ་དང་། འཇུག་སེམས་ཀྱི་སྡོམ་པ་དང་ལྡན་པར་བྱ་སྟེ། འོག་ནས།

[Block 15 [VERSE]]
མཉམ་པར་བཞག་པས་བླ་མ་ལ། །
ཅི་འབྱོར་པ་ཡིས་མཆོད་བྱས་ལ། །
གསུམ་ལ་སྐྱབས་འགྲོ་ནས་བརྩམས་ཏེ། །
བྱང་ཆུབ་སེམས་སོགས་སྡོམ་པ་ནི། །

[Block 16 [VERSE]]
གལ་ཏེ་བདག་ལ་ཕན་འདོད་ན། །
སྔགས་པས་འབད་དེ་གཟུང་བར༌[^7]བྱ། །

[Block 17]
ཞེས་གསུངས་པས་བླ་མ་དེས་དང་པོ་འཁོར་བའི་ཉེས་དམིགས་ཡིད་ལ་བྱ་བ་དང་། སྐྱབས་སུ་འགྲོ་བ་དང་བྱམས་པ་དང་སྙིང་རྗེའི་སྒོ་ནས་བྱང་ཆུབ་ཏུ་སེམས་བརྟན་པར་བྱས་ནས༌[^8]འཇུག་སེམས་ཀྱི་སྡོམ་པ་དང་ལྡན་པ་ལ་དབང་བཞི་སྣོད་དུ་བསྒྲུབས་ནས་ལྟ་སྤྱོད་སྒོམ་པ་གསུམ་གྱི་མན་ངག་དང་ལྡན་པར་བསྒྲུབ་པ་དེའི་ཕྱིར་རོ། །

[Block 18 [VERSE]]
དེ་ནས་སྔགས་སོགས་སྦྱིན་པ་ཡིས། །
དམ་ཆོས་སྣོད་དུ་བྱས་ནས་སོ། །

[Block 19]
ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 20]
དེ་བླ་མ་ལ་རག་ལས་པས།

[Block 21 [VERSE]]
དངོས་གྲུབ་སློབ་དཔོན་རྗེས་འབྲངས༌[^9]ཞེས། །
རྡོ་རྗེ་འཛིན་པ་ཉིད་གསུངས་པར། །
ཤེས་ནས་དངོས་པོ་ཐམས་ཅད་ཀྱིས། །
བླ་མ་ཡོངས་སུ་མཉེས་པར་བྱ། །

[Block 22]
ཞེས་བྱ་བ་དེ་ལྟ་བུའི་བླ་མ་དེ༌[^10]དུས་རྟག་ཏུ་ཕུན་སུམ་ཚོགས་པ་མཐའ་དག་གི་འབྱུང་གནས་འཁོར་བའི་རྒྱ་མཚོ་ནས་འབྱིན་བྱེད་དངོས་གྲུབ་ཐམས་ཅད་ཀྱི་རག་ལས་པ༌[^11]ཡིན་པས་དེའི་ཕྱིར། གདན་བསྟབས་པ༌[^12]དང་ལྡང་བ་དང་། །དོན་གྱི་བྱ་བ་སོགས་བསྙེན་བཀུར་བྱེད༌[^13]པ་དང་།

[Block 23 [VERSE]]
བླ་མ་ལས་ནི་དངོས་གྲུབ་དང་། །
མཐོ་རིས་དང་ནི་ཐར་པ་ཐོབ། །

[Block 24]
ཅེས་པ་ནས། མདུན་དུ་དུལ་བས་འདུག་པར་བྱ། །ཞེས་བྱ་བའི་བར་དུ་བྱ་བ་མཐའ་དག་དྲན་པ་དང་ཤེས་བཞིན་གྱིས་མ་ཡེངས་པར་བྱ་བའི་ཚུལ་གྱིས་བླ་མ་བསྟེན་པར་བྱའོ། །

[Block 25]
དེ་ལྟ་བུའི་བླ་མ་ལ་བརྙས་ན་སངས་རྒྱས་ཐམས་ཅད་ལ་བརྙས་པ་སྟེ།

[Block 26 [VERSE]]
དེ་འདྲའི་མགོན་ལ་བསམ་བཅས་པས། །
སློབ་མར་གྱུར་པས༌[^14]བརྙས་ན་ནི། །
སངས་རྒྱས་ཐམས་ཅད་བརྙས་པ་སྟེ།[^15] །
དེས་ནི་རྟག་ཏུ་སྡུག་བསྔལ་འཐོབ། །

[Block 27]
ཅེས་པ་ནས། དེར་ནི་གནས་པ་ཡང་དག་བཤད། །ཅེས་བྱ་བའི་བར་དང་།

[Block 28 [VERSE]]
དེ་བས་འབད་པ་ཐམས་ཅད་ཀྱིས། །
རྡོ་རྗེ་སློབ་དཔོན་བློ་གྲོས་ཆེ། །
དགེ་བ་ཡོངས་སུ་མི་སྤྱོམས་པ། །
ནམ་ཡང་སྨད་པར་མི་བྱའོ། །

[Block 29]
ཞེས་པ་དེ་ནི་རྩ་བའི་ལྟུང་བ་ཀུན་གྱི་ངོ་བོ་ཉིད་དོ། །

[Block 30]
སྦྱོང་བ་ལ་སོགས་པ་ནི་ཕལ་ཆེར་བླ་མ་གསེར་གླིང་པ་ལ་སོགས་པའི་བཤད་པ་ལས་ཤེས་པར་བྱའོ། །

[Block 31]
ལྟུང་བ་དེ་གཉིས་ཀྱི་རྒྱུ་ནི་བླ་མ་གྲུབ་པ་ཐོབ་པའི་ཚིག་གི་ཉམས་དང་བྲལ་པ་རྣམས་དང་ཕྲད་པའི་དབང་གིས་ལམ་གྱི་སྣོད་དུ་མ་བསྒྲུབས་པར་དབང་ལ་སོགས་པ་བྱས་ཀྱང་། རྩ་བ་མ་བརྟན་པའི་དབང་གིས་ངེས་པར་འདྲེན་མི༌[^16]ནུས་ཤིང་། ངེས་པ་མེད་པའི་ཕྱིར་བླ་མ་གཙོ་བོར་མི་བྱེད་དེ། དེའི་ཕྱིར་སློབ་དཔོན་བརྙས་པ་ལ་སོགས་པ་ཐམས་ཅད་འབྱུང་སྟེ་དེ་ནི་ལོག་པར་བསྟན་ཅིང་བསྒྲུབ་པ༌[^17]ཞེས་བྱ་སྟེ། སྔོན་དུ་འགྲོ་བའི་སྦྱང་བ་གང་ཡང་མེད་པར་དབང་དང་བསྐྱེད་རྫོགས་ཀྱི་མན་ངག་བསྟན༌[^18]དུ་ཟིན་ཀྱང་རྩ་བ་མེད་པའི་དབང་གིས་མྱུར་དུ་འཇིག་ལ་ངེས་པར་ཆུང་ངོ་། །དེ་བས་ན་དེ་གཉིས་ནི་བཀའ་འདས་དང་གཉིས་ཀྱི་རྒྱུ་ཡིན་པས་ན།

[Block 32]
ཛྙཱ་ན་སིདྡྷི་ལས།

[Block 33 [VERSE]]
རང་ཉིད་ཀྱིས་ལམ་མ་མཐོང་བས། །
ཇི་ལྟ་བཞིན་དུ་གཞན་དག་འདྲེན། །
ལོང་བ་གཉིས་ནི་འགྲོགས་གྱུར་ན། །
གཉིས་ཀ་ལྟུང་བར༌[^19]ཐེ་ཚོམ་མེད། །

[Block 34]
ཅེས་པ་དང་། ཡང་།

[Block 35 [VERSE]]
སྡིག་པ་ཅན་གྱི་ལམ་དེ་ཡིས། །
བགྲོད་པ་ཉམས་པ་ཐོབ་པར་འགྱུར། །

[Block 36]
ཞེས་པས་བླ་མ་དམ་པ་ལ་བརྟེན་པར་བྱའོ། །

[Block 37]
སྤུན་ལ་ཉེས་པ་བརྗོད་པ་དང་བྱམས་པ་སྤོང་བ་གཉིས་ལྟུང་བའི་ངོ་བོ་གཅིག་ལ་དེ་འབྱུང་བའི་རྒྱུ་ཡང་གཅིག་སྟེ། དེའི་རྒྱུ་ནི་སྔོན་དུ་ཐུན་མོང་གི་ལམ་བྱམས༌[^20]སྙིང་རྗེ་མ་སྦྱངས་པས་སེམས་ཅན་ལ་ཕན་འདོད་པ༌[^21]དང་། གཅེས་པར་འཛིན་པའི་བློ༌[^22]མེད་ལ་དེའི་དབང་གིས་གནོད་ཅིང་སྨོད་པ་ལ་སོགས་པའི་རྐྱེན་ཕྲ་མོ་མི་བཟོད་དེ། དེའི་ཕྱིར་སྤུན་ལ་ཉེས་པ་བརྗོད་ཅིང་སེམས་ཅན་ལ་བྱམས་པ་སྤོང་བ་དེས་དེ་གཉིས་ངོ་བོ་གཅིག་སྟེ་གཞན་ལ་གནོད་པར་འདྲ་བས་སོ། །

[Block 38]
བྱང་ཆུབ་སེམས་སྤོང་དང་གྲུབ་པའི་མཐའ་སྨོད་པ་གཉིས་རྒྱུ་དང་ངོ་བོ་གཅིག་སྟེ། རྒྱུ་ནི་བྱམས་པ་དང་སྙིང་རྗེའི་སྟོབས་ཀྱིས༌[^23]བྱང་ཆུབ་ཀྱི་སེམས་བརྟན་པར་མ་བྱས་པར་བླངས་སུ་ཟིན་ཡང་མི་བརྟན་ཏེ། དེ་ཡང་།

[Block 39 [VERSE]]
ཐམས་ཅད་ལ་ནི་ལྷག་པའི་གནས། །
གང་དུ་ཐམས་ཅད་འཇིག་པ་སྟེ། །
བསྐལ་པ་བྱེ་བ་སྟོང་དུ་ཡང་། །
ཡང་དག་བསྐྱེད་པའི༌[^24]དགེ་བ་ཆེ། །

[Block 40 [VERSE]]
བྱང་ཆུབ་སེམས་ནི་བསྐྱེད་པ་ཡི། །
བསོད་ནམས་ཚོགས་ནི་བསགས༌[^25]པས་སོ། །
བསྐལ་པ་བྱེ་བས་འབྱུང་བ་ནི། །
སྐད་ཅིག་ཉིད་ལ་རྣམ་པར་འཇིག །
--- END BLOCKS ---
