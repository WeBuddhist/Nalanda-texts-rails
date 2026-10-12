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
## ༄༅། །སྒྲོན་མ་གསལ་བ་ཞེས་བྱ་བའི་འགྲེལ་བཤད།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། པྲ་དཱིཔྟ་ན་ནཱ་མ་ཊཱི་ཀཱ། བོད་སྐད་དུ། སྒྲོན་མ༌[^1]གསལ་བ་ཞེས་བྱ་བའི་འགྲེལ་བཤད། བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་འཕགས་པ་སྤྱན་རས་གཟིགས་དབང་ཕྱུག་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4]
ཆོས་རྣམས་རང་བཞིན་མེད་ལས་སྒྱུ་མའི་སྐུར་བསྟན་ནས། །ཐུགས་རྗེ་ཆེན་པོའི་སྟོབས་ཀྱིས་སེམས་ཅན་ཁམས་རྣམས་མ་ལུས་པའི། །དོན་རྣམས་ཡོངས་སུ་གྲུབ་པའི་ཡིད་བཞིན་ནོར་བུ་དང་འདྲ་བས། །མངོན་པར་བྱང་ཆུབ་མཆོག་བརྙེས་དེ་ལ་རྟག་ཏུ་དང་བས་ཕྱག་འཚལ་ལོ། །

[Block 5]
དྲི་མེད་མཐའ་ཡས་དངོས་གྲུབ་ཀུན་བརྙེས་དེ་ལ་ཕྱག་འཚལ་ཏེ། །སྟོང་པ་ཉིད་ཀྱི་དོན་རྣམས་མངོན་གྱུར༌[^2]ཐོགས་མེད་ལ་ཕྱག་འཚལ། །འདས་དང་མ་བྱོན་དུས་རྣམས་ཀུན་དུ་ཁྱབ་པ་ཁྱོད་ལ་ཕྱག་འཚལ་ལོ། །

[Block 6]
རླུང་དང་སྔགས་དང་སེམས་ལ་སོགས་པ་ཀུན་མཁྱེན་ཁྱོད་ལ་ཕྱག་འཚལ་ལོ། །

[Block 7]
སེམས་ཅན་གང་དག་རྒྱལ་བ་ཡིས་གསུངས་ལེགས་པའི་དོན་ལ་རབ་རྨོངས་པ། །དེ་གསལ༌[^3]ཕྱིར་ནི་ཟླ་བ་གྲགས་པས་སྒྲོན་མ་གསལ་བའི་རྒྱ་ཆེར་འགྲེལ་པ་མཛད། །སེམས་ཅན་བློ་དམན་ཁ་ཅིག་དོན་དེ་ཉིད་ལ་རྨོངས་གྱུར་པས། །ཉི་མ་སྣང་བ་ལ་སོགས་ཐུན་མོང་ཁྱད་པར་རྒྱ་ཆེར་འགྲེལ་པ་བརྩམས། །འདོད་རྒྱལ་དབང་གིས་ལེགས་པའི་དོན་གསུངས་ལེགས་པར་གསལ་བྱས་ཀྱང་། །རྨོངས་པའི་དབང་གིས་རྒྱུད་དོན་ནུས་པ་མ་མཐོང་དེ་ཕྱིར་འདི་ལ་དགའ་བ་མཆོག་སྐྱེས་ནས། །བློ་དམན་དོན་དུ་བདག་གིས་ཅུང་ཟད་བཤད་པར་བྱ། །

[Block 8]
འདི་ན་མི་མཁས་གང་ཞིག་གིས། །སྔོན་དུ་བསྟན་བཅོས་མ་རྙེད་པར།[^4] །

[Block 9 [VERSE]]
གང་ཡིན་པ་ནི་ཕྱིས་རྙེད་པ། །
གང་ཡིན་དེ་ནི་ཡ་མཚན་ཏེ། །
དེ་འདིར་བདག་གིས་རྣམ་པར་དབྱེ། །
གང་ཡང་བློ་དམན་རྣམས་ཀྱི་ཕྱིར། །

[Block 10 [VERSE]]
མཁས་པས་བསྟན་བཅོས་མི་རྩོམ༌[^5]པར། །
ཉོན་མོངས་དྲ་བས་བཅིངས་པ་ཡིས། །
བསྟན་བཅོས་མཐའ་དག་གང་རྩོམ་ཡང་། །
སྡིག་པ་འབའ་ཞིག་བསོད་ནམས་མེད། །

[Block 11 [VERSE]]
དེ་ཕྱིར་མཁས་པས་སྤང་བར་བྱ། །
བསྟན་བཅོས་རྩོམ་པའི་མཁན་པོ་ཡིས། །
རྒྱལ་བའི་བཀའ་ནི་འབྱུང་ཁུངས་སུ། །
རྣམ་པར་བཞག་པས་དེ་ལས་ནི། །

[Block 12 [VERSE]]
དྲན་དང་ངོ་ཚ་ཤེས་པ་དང་། །
ཁྲེལ་ཡོད་པ་དང་ཤེས་རབ་དང་། །
དད་དང་མོས་པ་ལ་སོགས་ལ། །
སེམས་ལས་བྱུང་བ་དགེ་བའི་ཆོས། །

[Block 13 [VERSE]]
གང་གིས༌[^6]སྔོན་དུ་སོང་བ་ཡིས། །
བསྟན་བཅོས་མི་རྩོམ་གྱུར་ཀྱང་བླའི། །
བསོད་ནམས་འབའ་ཞིག་སྡིག་པ་མེད། །
གང་གིས་འདོད་ཆགས་ཁོང་ཁྲོ་དང་། །

[Block 14 [VERSE]]
དེ་བཞིན་ང་རྒྱལ་ལ་སོགས་པ། །
ཉོན་མོངས་མི་དགེ་སྔོན་སོང་ནས། །
རྒྱལ་བའི་བཀའ་རྣམས་མ་ལུས་པའི། །
རྗེས་སུ་འབྲངས༌[^7]ཏེ་རབ༌[^8]བཤད་ཀྱང་། །

[Block 15 [VERSE]]
ས་བོན་མི་དགེའི་དབང་གྱུར་པས། །
མཐོང་བའི་ཆོས་ལ་དམྱལ་ཚོགས་བསྲེག །
དེ་བས་བསྟན་བཅོས་རྩོམ་པ༌[^9]ཡིས། །
དགེ་བའི་ཆོས་འདི་སྔོན་སོང་ནས། །

[Block 16]
གང་ཡིན་བསྟན་བཅོས་བརྩམ་པར་བྱ། །

[Block 17 [VERSE]]
ཤེས་རབ་ཞན་པར་གྱུར་པ་ཡིས། །
བསྟན་བཅོས་གང་ཞིག་བརྩམས་གྱུར་ཀྱང་། །
དེ་ཡིས་དོན་བྱེད་ནུས་མ་ཡིན། །
དཔེར་ན་ལོང་བ་གང་ཞིག་གིས། །

[Block 18 [VERSE]]
གཞན་གྱི་ལོང་ཁྲིད་མི་ནུས་པ། །
དེ་བཞིན་དེ་ཡང་དེ་བཞིན་ནོ། །
གང་ཚེ་བསྟན་བཅོས་རྩོམ་པ་ཡང་། །
སྒྲ་དང་དོན་རྣམས་གཏན་ལ་འབེབས། །

[Block 19]
ཕྱི་རོལ་བསྟན་བཅོས་ལེགས་པར་མཁས། །གྲུབ་པའི་མཐའ་རྣམས་ཀུན་ལ་མཁས།[^10] །

[Block 20 [VERSE]]
སྔགས་དང་རྫས་དང་སྨན་རྣམས་དང་། །
ཐུན་མོང་གསོ་བ་ལ་སོགས་ལ། །
རབ་ཏུ་མཁས་པར་གྱུར་པ་དང་། །

[Block 21]
གཞན་གྱི་བསྟན་བཅོས་སུན་འབྱིན་གྱི།[^11] །

[Block 22 [VERSE]]
སྦྱོར་བ་ལ་ནི་ཤིན་ཏུ་མཁས། །
དགེ་བའི་ཆོས་ཀྱིས་རྣམ་པར་བརྒྱན། །
དེ་ཡིས་བསྟན་བཅོས་བརྩམ་པར་བྱ། །
ཡང་ན་བྱང་ཆུབ་སེམས་དཔའ་འམ། །

[Block 23 [VERSE]]
ཐུགས་རྗེའི་སྟོབས་ཀྱིས་སྤྲུལ་པ་ཡི། །
སངས་རྒྱས་འཇིག་རྟེན་ལྷར་སྣང་སྟེ། །
དེ་ཡིས་བརྩམ་བྱ་མ་གཏོགས་པ། །
གཞན་གྱིས་བརྩམས་པ་དོན་མེད་འགྱུར། །

[Block 24]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་དང་གསུང་དང་ཐུགས་ཀྱི་གསང་བ་བསྡུས་པ་འདི་ཅིའི་ཕྱིར་གསུངས་ཤེ་ན། འདི་ལྟར་རིགས་ཐམས་ཅད་གཟུང་བར་བྱ་བ་དང་། རིགས་མཆོག་ཏུ་གྱུར་པ་གཟུང་བར་བྱ་བའི་ཕྱིར་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པའི་དཀྱིལ་འཁོར་འདིར་མཚམས་མེད་པ་ལྔ་ལ་སོགས་པ་བྱས་པ་ཡང་བླ་ན་མེད་པའི་མཆོག་ཐོབ་པར་འགྱུར་རོ༌[^12]ཞེས་གསུངས་པའི་ཕྱིར་དང་། གསང་བའི་དོན་འདི་ནི་ཐམས་ཅད་ཀྱི་ཐུན་མོང་མ་ཡིན་ནོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 25]
གལ༌[^13]ཏེ། རིགས་ཐམས་ཅད་ཅེས་བྱ་བ་ནི་རིགས་ཆད་པ་ལ་སོགས་པ་ཡང་སྨོས་པ་ཡིན་ནམ། གལ་ཏེ་དེ་ལྟ་ཡིན་ན་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བདེན་པ་བཞི་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་གསུངས་པ་དོན་མེད་པར་འགྱུར་རོ་ཞེ་ན་མ་ཡིན་ཏེ། རིགས་མཆོག་ཏུ་འགྱུར་བའི༌[^14]ཕྱིར་རོ། །

[Block 26]
དེ་ལྟ༌[^15]ན་ནི་རིགས་མཆོག་ཏུ་གྱུར་པ་འདུལ་བ་དང་། རིགས་ཐམས་ཅད་པ་འདུལ་བ་གཅིག་གིས་གཅིག་སྤངས་པ་མ་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ། ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་བཞི་སྟོང་གི་སྣོད་ཡིན་པའི་ཕྱིར་རོ་ཞེའོ། །

[Block 27]
དེ་ལྟ་ན་ནི་ཐེག་པ་མཆོག་ཏུ་མི་འགྱུར་གྱི་ཐེག་པ་ཐམས་ཅད་པར་འགྱུར་རོ་ཞེ་ན་མ་ཡིན་ཏེ། ཐེག་པ་ནི་གཉིས་དང་གསུམ་དུ་ཡོད་པ་མ་ཡིན་ནོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་དང་གསུང་དང་ཐུགས་གསང་བ་ལས་མི་འདའ་ལ་སེམས་ཅན་ཐམས་ཅད་ཀྱང་དེའི་རང་བཞིན་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 28]
དེ་ལྟ་ན་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་བདེན་པ་བཞིའི་ཆོས་ཀྱི་འཁོར་ལོ་ལ་སོགས་པ་གསུངས་པ་དོན་ཡོད༌[^16]པར་འགྱུར་ཏེ་སྔ་མ་བཞིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། སེམས་ཅན་ཐམས་ཅད་ཀྱང་རང་རང་གི་རིགས་ལ་གནས་པའི་ཕྱིར་རོ། །

[Block 29]
རིགས་ཞེས་བྱ་བ་འདི་ཡང་རྐྱེན་ལས་བྱུང་བའམ། ཆོས་ཉིད་ཀྱིས་ཡིན་ཞེས་རྟོག་གྲང་ན། རྐྱེན་ལས་བྱུང་བ་ནི་མ་ཡིན་ཏེ། རྐྱེན་ཐམས་ཅད་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 30]
དེ་ལྟ་ན་ནི་རིགས་ངེས་པར་མི་འགྱུར་གྱི། རིགས་མ་ངེས་པར་ནི་འགྱུར་རོ་ཞེ་ན། རང་གི་རིགས་ཀྱི༌[^17]བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 31]
རང་གི་ཆོས་ཀྱིས༌[^18]བསྐྱེད་པ་ཞེས་བྱ་བ་འདི་ཡང་ས་བོན་ཐམས་ཅད་ཀྱིས་གཅིག་བསྐྱེད་དམ། ས་བོན་གཅིག་གིས་ཐམས་ཅད་བསྐྱེད་ཅེ་ན། ས་བོན་ཐམས་ཅད་གཅིག་གིས་བསྐྱེད་པ་ནི་མ་ཡིན་ཏེ། རྐྱེན་མ་ངེས་པར་འགྱུར་བ་ཉིད་དང་། ཐམས་ཅད་ལས་ཐམས་ཅད་སྐྱེ་བར་འགྱུར་བ་དང་། རྐྱེན་ཅན་དོན་མེད་པ་ཉིད་དུ་ཡང་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། འདིར་ནི་ས་བོན་ཐམས་ཅད་རྐྱེན་ཐམས་ཅད་ཀྱིས་གསོས་འདེབས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 32]
གསོས་འདེབས་པ་ཞེས་བྱ་བ་འདི་ཡང་ས་བོན་ཉིད་རྐྱེན་གཞན་གྱི་དབང་དུ་འགྱུར་བ་ནི་མ་ཡིན་ཏེ། གོང་མའི་སྐྱོན་ཉིད༌[^19]དུ་འགྱུར་རོ། །

[Block 33]
ལུང་ལས་དེ་བཞིན་གཤེགས་པ་གསང་བ་མཆོག་གི་ཕྱིར། ས་བོན་རྣམས་ནི་གཅིག་ཏུ་འགྱུར། །ཞེས་འབྱུང་བའི་ཕྱིར་ཆོས་ཉིད་ཀྱིས་ཐམས་ཅད་ཡོད་པ་མ་ཡིན་ནོ་ཞེ་ན། འདི་ལས་དང་པོ་པ་འམ། ས་ལ་གནས་པ་ཡིན། ས་ལ་གནས་པའི་དབང་དུ་ནི་འདོད་པ་ཡིན་ཏེ། གནོད་པ་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 34]
ཕྱོགས་ཕྱི་མ་ལྟར་ན་ནི་འཇུག་པར་ཡང་མི་འགྱུར་ན། རིགས་གཅིག་པ་ལྟར་གྱུར་པ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། འོན་ཀྱང༌[^20]ས་ལ་གནས་པ་ཐམས་ཅད་ཀྱང་གསད་པའི་མཆོག་ལ་གནས་པའམ། སོ་སོ་རང་རང་གི་ལམ་ལ་གནས་ཤེ་ན།

[Block 35]
དང་པོ་ལྟར་ནི་མ་ཡིན་ཏེ། དུས་ཀྱིས་གནོད་པའི་ཕྱིར་རོ། །

[Block 36]
ཕྱོགས་ཕྱི་མ་ལྟར་ན་ནི་རང་གི་ཚིག་གིས་གནོད་པའི་ཕྱིར་རོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ཚིག་གི་བླང་དོར་མེད་པའི་བྱང་ཆུབ་སྒྲུབ་པའམ། བསྐལ་པ་གྲངས་མེད་པ་གསུམ་གྱིས་འགྲུབ་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 37]
ཐམས་ཅད་གསང་བ་མཆོག་ལ་གནས། །ཞེས་བྱ་བ༌[^21]དང་། རང་གི་ལམ་ལ་གནས་ཞེས་པ་ཡང་གཅིག་གིས་གཅིག་སྤངས་པའི་ཕྱིར་རོ། །

[Block 38]
དེ་བས་ན་འདི་ནི་བླང་བར་བྱ་བ་ཉིད་དོ་ཞེ་ན་མ་ཡིན་ཏེ། ས་ལ་གནས་པ་རྣམས་ནི་ཐམས་ཅད་ཀྱང་བསྐྱེད་པའི་རིམ་པ་ཉམས་སུ་ལེན་པའི་ཕྱིར་དང་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་ཆེན་པོར་ལུང་བསྟན་པའི་ཕྱིར་རོ། །

[Block 39]
དེ་ལྟ་ན་ནི་ཐེག་པའི་བྱེ་བྲག་མེད་པར་འགྱུར་རོ་ཞེ་ན་མ་ཡིན་ཏེ་གཉིས་པ༌[^22]ཡོད་པའི་ཕྱིར་རོ། །

[Block 40]
གཉིས་ཞེས་བྱ་བ་འདི་ཡང་གསུམ་དང་གཉིས་ཀྱི་བྱེ་བྲག་གིས་ཡིན་ནོ། །
--- END BLOCKS ---
