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
## ༄༅། །རིགས་པ་དྲུག་ཅུ་པའི་འགྲེལ་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ཡུཀྟི་ཥཥྛི་ཀ་བྲྀཏྟི། བོད་སྐད་དུ། རིགས་པ་དྲུག་ཅུ་པའི་འགྲེལ་པ།

[Block 4 [VERSE]]
འཇམ་དཔལ་ཡེ་ཤེས་སེམས་དཔའ་ལ་ཕྱག་འཚལ་ལོ། །
རྒྱལ་བའི་རིགས་པའི་ལམ་གྱི་རྗེས་འབྲང༌[^1]བ། །
མཐའ་གཉིས་སེལ་བའི་རིགས་པ་དྲུག་ཅུ་པ། །
གང་གིས་མཛད་པ་དེ་ལ་ཕྱག་འཚལ་ཏེ། །

[Block 5]
བདག་གིས་དབུ་མའི་ཚུལ་གྱིས་དེ་རྣམས་དབྱེ། །དེ་ལ༌[^2]སློབ་དཔོན་འདི་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཇི་ལྟར་གནས་པ་བཞིན་དུ་དེ་ཁོ་ན་གཟིགས་པས་དགྱེས་པའི་ཁྱད་པར་བརྙེས་པ་སྟེ། དེ་རྟོགས་པ་ནི་དད་པ་མཆོག་གི་གནས་ཡིན་པར་མཁྱེན་ནས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མཐོང་བ་ལས་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་དགེ་བའི་ཚོགས་མ་ལུས་པར་འབྱུང་བ་དང་འཕགས་པའི་གང་ཟག་མ་ལུས་པར་འབྱུང་བ་དང་། སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཡེ་ཤེས་སྒྲིབ་པ་མེད་པ་དང་ལྡན་པ་རྣམས་ཀྱི་རྣམ་པ་ཐམས་ཅད་དུ་དེ་ཁོ་ན་ཉིད༌[^3]མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པ་ཡང་གཟིགས་ནས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རང་བཞིན་གྱིས་མ་སྐྱེས་པའི་ཕྱིར་སྐྱེ་བ་དང་འཇིག་པ་དང་ཡོད་པ་དང་མེད་པའི་མཐར། རྟོག་པའི་དྲི་མས་མ་གོས་པ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ངོ་བོ་ཉིད་ཀྱིས་སྟོང་པ་ཡིན་པར་ཆེ་བ་ཉིད་ཀྱིས༌[^4]བརྗོད་ནས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་འཆད་པར་བཞེད་དེ། དེ་སྟོན་པའི་དེ་བཞིན་གཤེགས་པ་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་ངོ་བོ་ཉིད་དང་ཐ་མི་དད་པར་གྱུར་པ་ལ། གུས་པ་སྐྱེས་ནས་དེ་ལ་ཕྱག་འཚལ་བ་རྩོམ་མོ། །

[Block 6 [HEADING]]
## གཞུང་དོན། ^1-0

[Block 7 [HEADING]]
### ཕྱག་འཚལ་བ། ^1-1-0

[Block 8 [VERSE]]
གང་དག་སྐྱེ་དང་འཇིག་པ་དག །
འདི་ཡི་ཚུལ་གྱིས་རབ་སྤངས་པ། །
རྟེན་ཅིང་འབྱུང་བ༌[^5]གསུངས་པ་ཡི། །
ཐུབ་དབང་དེ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 9]
ཞེས་ཕྱག་འཚལ་བ་བརྩམ་མོ། །

[Block 10]
ཅིའི་ཕྱིར་སྟོང་པ་ཉིད་བདུན་ཅུ་པ་དང་། རྩོད་པ་བཟློག་པ་ལས་སློབ་དཔོན་གྱིས་བསྟོད་པ་མ་བརྗོད་པ༌[^6]དབུ་མ་འདི་ལས་བརྗོད་ཅེ་ན། སྨྲས་པ། སྟོང་པ་ཉིད་བདུན་ཅུ་པ་དང་རྩོད་པ་བཟློག་པ་གཉིས་དབུ་མ་ལས་འཕྲོས་པ་སྟེ། རང་གི་རྒྱུད་གུད་ན་མེད་པས་ལོགས་ཤིག་ཏུ་བསྟོད་པ་མ་བརྗོད་དེ།

[Block 11 [VERSE]]
འདི་ལྟར་རྩོད་པ་བཟློག་པ་ནི། །
དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་ནི། །
རྐྱེན་ལ་སོགས་པ་མེད་པ་སྟེ། །

[Block 12]
རང་གི་དངོས་པོ་ཡོད་མིན་ཏེ།[^7] །གཞན་གྱི་དངོས་པོ་ཡོད་རེ་སྐན། །རྩོད་པ་བཟློག་པ་ནི་དེ་ལ་བརྒལ་བ་དང་ལན་བཏབ་པར་གྱུར་པའི་ཕྱིར་དེ་ལས་འཕྲོས་པ་ཡིན་པར་མངོན་ནོ། །

[Block 13 [VERSE]]
ཇི་ལྟར་སྒྱུ་མ་རྨི་ལམ་བཞིན། །
དྲི་ཟའི་གྲོང་ཁྱེར་ཅི་འདྲ་བ། །
དེ་བཞིན་སྐྱེ་དང་དེ་བཞིན་གནས། །
དེ་བཞིན་དུ་ནི་འཇིག་པར་བཤད། །

[Block 14]
སྟོང་པ་ཉིད་བདུན་ཅུ་པ་ནི་དེ་ལ་བརྒལ་བ་དང་ལན་བཏབ་པར་གྱུར་པའི་ཕྱིར་དེ་ལས་འཕྲོས་པ་ཡིན་པར་མངོན་ནོ། །

[Block 15]
རིགས་པ་དྲུག་ཅུ་པ་འདི་ནི་དབུ་མ་བཞིན་དུ་འདིར་ཡང་གཙོ་བོར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དཔྱད་པ་ལས་བརྩམས་ཏེ། བྱས་པའི་ཕྱིར་དབུ་མ་ལས་འཕྲོས་པ་ལྟ་བུ་ནི་མ་ཡིན་ནོ། །

[Block 16]
དེ་ལ་ངོ་བོ་ཉིད་དང་དབང་ཕྱུག་ལ་སོགས་པར་སྨྲ་བ་ངོ་བོ་ཉིད་དང་དབང་ཕྱུག་དང་རང་བཞིན་དང་སྐྱེས་བུ་དང་དུས་དང་སྲེད་མེད་ཀྱི་བུ་ལ་སོགས་པ་ལས་འགྲོ་བ་རྣམས་ཀྱི་སྐྱེ་བ་དང་འཇིག་པ་ལ་སོགས་པ་ཁས་ལེན་པ་དག་ཐམས་ཅད་བཏང་བས་མྱ་ངན་ལས་འདས་པའི་གྲོང་ཁྱེར་དུ་འགྲོ་འདོད་ཀྱང་བདེན་པ་གཉིས་ཕྱིན་ཅི༌[^8]ལོག་པར་མཐོང་བ་ལས་ཉམས་པས་ཕྱིར་ཕྱོགས་པ་བཞིན་དུ་འཁོར་བ་རྣམ༌[^9]པར་ཆད་པའི་མཚན་ཉིད་མྱ་ངན་ལས་འདས་པའི་གྲོང་ཁྱེར་དུ་ཡུན་རིང་མོར་ཡང་འགྲོ་མི་ནུས་སོ། །

[Block 17]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་བསྟན་པ་རྐྱེན་ཉིད་འདི་པ་ཙམ་འདི་ནི་བདེན་པ་གཉིས་ཕྱིན་ཅི་མ་ལོག་པར་མཐོང་བའི་རྒྱུར་གྱུར་པའི་ཕྱིར་འཕགས་པའི་སྐྱེ་བོ་ཐམས་ཅད་གཤེགས་ཤིང་རྗེས་སུ་གཤེགས་པ་དང་པོ༌[^10]ཟླ་མེད་པ། འདུས་བྱས་ཐམས་ཅད་ཡོངས་སུ་སྤངས་པ། མྱ་ངན་ལས་འདས་པའི་གྲོང་ཁྱེར་དུ་གཅིག་ཏུ་གཞོལ་བར་འགྱུར་བའི༌[^11]ཆེན་པོའོ། །

[Block 18]
དེ་བས་ན་དེ་སྟོན་པས་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་མ་ལུས་པའི་དབང་ཕྱུག་ཕུན་སུམ་ཚོགས་པ་སྟོན་པ་བླ་ན་མེད་པ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཐུབ་པ་རྣམས་ཀྱི་གཙོ་བོ་ཡིན་པས་ཐུབ་པའི་དབང་པོར་དགའ་བ་མ་ཡིན་ཏེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྟོན་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་ཐུབ་པའི་དབང་པོ་ཡིན་པར་རྟོགས་ནས།

[Block 19 [VERSE]]
རྟེན་ཅིང་འབྲེལ་འབྱུང་གསུང་བ་ཡི། །
ཐུབ་དབང་དེ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 20]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 21]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ནི༌[^12]དབང་པོ་མ་ཡིན་པ་མི་འབྱུང་ངོ་། །རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ༌[^13]གསུང་བ་ནི་ཐུབ་པའི་དབང་པོར་འགྱུར་བའི་ཕྱིར་རྒྱུའོ། །

[Block 22]
ཐུབ་པའི་དབང་པོར་གྱུར་པ་ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་གསུང་བའི་རྒྱུ་སྟེ། གཞན་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་འཆད་ནུས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 23]
ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱང་ཐུབ་པའི་དབང་པོས་བསྟན་པ་ཉིད་ཀྱི་ཕྱིར་དེ་འཆད་ནུས་སོ། །

[Block 24]
གལ་ཏེ་གཅིག་ལ་གཅིག་ལྟོས་པའི༌[^14]ཕྱིར་གཉི་ག་མི་འགྲུབ་བོ་ཞེ་ན། སྨྲས་པ་འདི་ལྟ་སྟེ་གཅིག་ལ་གཅིག་ལྟོས་པ་གཞན་ངོ་བོ་ཉིད་ཀྱིས་མི་སྐྱེ་མི་འགག་ཅེས་བྱ་བ་གང་ཡིན་པ་དེ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྟེ། དེ་ཉིད་སྟོང་པ་ཉིད་དུ་སྨྲ་བ་རྣམས་འདོད་དོ། །

[Block 25]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་གསུང་བ་འབའ་ཞིག་གི་ཕྱིར་དེ་ཐུབ་པའི་དབང་པོར་གྱུར་པ་མ་ཡིན་གྱི། དངོས་པོ་རྣམས་གཅིག་ལ་གཅིག་ལྟོས་པའི་གྲུབ་པའི་ཚུལ་གསུང་བ་ན་དངོས་པོ་རྣམས་ཀྱི་སྐྱེ་བ་དང་འཇིག་པ་བཀག་པའི་ཕྱིར་རོ། །

[Block 26]
གང་གིས་ཞེས་བྱ་བ་ནི་རྒྱུ་སྟེ། དེས་ཀྱང་གཉིས་སུ་མེད་པ་སྟོན་པའི་ཕྱིར་སྟོན་པ་བླ་ན་མེད་པ་ཐུབ་པའི་དབང་པོ་མཐོང་ནས། ཐུབ་དབང་དེ་ལ་ཕྱག་འཚལ་ལོ། །ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 27]
ཡང་ན་ཐུབ་པའི་དབང་པོ་གང་གིས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་གསུང་བ་ན། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཚུལ་འདི་ཉིད་དོ། །

[Block 28]
རིམ་པ་འདིས་དངོས་པོ་རྣམས་ཀྱི༌[^15]སྐྱེ་བ་དང་འཇིག་པ་བཀག་པས་ཐུབ་དབང་དེ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 29]
ཡང་ན་གང་གིས་ཞེས་བྱ་བ་ནི་རྒྱུ་ཁོ་ན་སྟེ།[^16] གང་གི་ཕྱིར་ཐུབ་པའི་དབང་པོ་དེས་དངོས་པོ་རྣམས་ཀྱི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྟོན་པ་ན༌[^17]རང་བཞིན་གྱིས་དངོས་པོ་རྣམས་ཀྱི་སྐྱེ་བ་དང་འཇིག་པ་བཀག་པས་ཐུབ་དབང་དེ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 30]
འཇིག་རྟེན་རྣམས་ལ་ཤིན་ཏུ་ཕན་འདོགས་པའི་ཕྱིར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 31]
ཡང་ན་འོག་ནས་འབྱུང་བ་ཐུབ་པའི་དབང་པོའི་གསུང་རབ་ལ༌[^18]བརྟེན་ཏེ། རང་གི་སེམས་ལ་བཀོད་པ་གྲུབ་པར་མཐོང་ནས།

[Block 32 [VERSE]]
གང་དག༌[^19]སྐྱེ་དང་འཇིག་པ་དང་། །
[^20]འདི་ཡི་ཚུལ་གྱིས་རབ་སྤངས་པ། །

[Block 33]
ཞེས་བྱ་བ་སྨོས་ཏེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡི།[^21] །དེའི་ཕྱིར་ཐུབ་དབང་དེ་ལ་ཕྱག་འཚལ་ལོ། །ཞེས་བྱའོ། །

[Block 34]
འདིར་སྨྲས་པ། ཁྱོད་ཀྱི་ཚིག་གི་ལུགས་འདི་ནི་སྔོན་མ་བྱུང་བ་སྟེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྨྲ་བ་ནི་སྐྱེ་བ་དང་འགག་པ་མེད་པར་སྟོན་པ་མི་རུང༌[^22]སྟེ། ཁྱོད་ཀྱི་བུ་སྐྱེས་སོ་ཞེས་སྨྲ་ན་ཁྱོད་ཀྱི་བུ་མ་སྐྱེས་སོ་ཞེས་སྨྲས་པ་མ་ཡིན་པར་འགྱུར་བ་དེ་བཞིན་དུ་འདི་ཡང་མི་རིགས་སོ། །

[Block 35]
བཤད་པ་གལ་ཏེ་མ་རིག་པའི་རབ་རིབ་ཀྱིས་བློ་གྲོས་ཀྱི་མིག་ཉམས་པ་དང་སྦྱར་ཏེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་སྒྲ་ལ་རང་བཞིན་གྱིས་མི་སྐྱེ་བ་དང་མི་འགག་པའི་ཚིག་ཏུ་མི་འགྱུར་བར་བརྟག་ན་ནི་ཉེས་པ་ཅི་ཡང་མེད་ཀྱི་རྟོགས་ཤིག །བྱིས་པ་ངོ་བོ་ཉིད་དུ་མངོན་པར་ཞེན་པ་རྣམས་ནི་གཟུགས་བརྙན་ལ་བྱིས་པ་ལྟ་བུར་དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་མེད་པ་ཉིད་ཡོད་བཞིན་དུ་ཡང་རྟོགས་པར་མི་ནུས་ཀྱི། མཁས་པ་རྣམས་ནི་གཟུགས་བརྙན་ལ་མཁས་པ་ལྟ་བུར་དངོས་པོ་རྣམས་ཀྱི༌[^23]ངོ་བོ་ཉིད་མེད་པར་གསལ་བར་ཁོང་དུ་ཆུད་པར་ནུས་སོ་ཞེས་བསྟན་པའི་ཕྱིར།

[Block 36 [HEADING]]
### ཚིགས་བཅད་དང་པོ། ^1-2-0

[Block 37 [VERSE]]
གང་བློ་ཡོད་དང་མེད་པ་ལས། །
རྣམ་པར་འདས་ཤིང་མི་གནས་པ། །
དེ་དག་ཟབ་མོ་དམིགས་མེད་པའི། །
རྐྱེན་གྱི་དོན་ལ་རྣམ་པར་བསྒོམ། །

[Block 38]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 39]
གང་དག་འདས་པའི་སྲིད་པ་ན་སྟོང་པ་ཉིད་ལ་གོམས་པ་དེ་དག་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྟོགས་ཤིང་སྟོང་པ་ཉིད་མཐོང་བའི་ས་བོན་ཡོད་པའི་ཕྱིར་མཐུ་ཆེ་བ་ཡིན་ཏེ། ད་ལྟར་གྱི་དུས་ན་སྐྱེས་པའི་གོམས་པ་མཚར་པོ་ཆེ་མེད་ཀྱང་སྐྱེ་བོ་བྱིས་པའི་བློའི་སྤྱོད་ཡུལ་མ་ཡིན་པ་ཡོད་པ་དང་མེད་པའི་མཐར་རྟོག་པས་རྙོག་པའི་དྲི་མས་མ་སྦགས་པ་རྟེན༌[^24]ཅིང་འབྲེལ་པར་འབྱུང་བ་ཟབ་མོ་འཕགས་པ་ཤཱ་རིའི་བུ་ལ་སོགས་པས་ཁོང་དུ་ཆུད་པར་དམིགས་ཏེ། ཇི་ལྟར་འཇིག་རྟེན་ལས་དང་ཉོན་མོངས་རྒྱུར་བྱས་བྱེད་རྒྱུ་ལྡན་འབྱུང་བ། །ལས་དང་ཉོན་མོངས་པ་དག་ལྡོག་རྒྱུ་དེ་ཡང་འདྲེན་པས་རབ་ཏུ་གསུངས། །

[Block 40]
གང་ན་སྐྱེ་དང་རྒ་དང་རྒུད་པའི་སྡུག་བསྔལ་ངེས་པར་མི་གནས་པ། །ཐར་པ་མཆོག་དེ་སྨྲ་བའི་ཁྱུ་མཆོག་དེ་ཡིས་རང་གིས༌[^25]མཁྱེན་དེ་གསུངས། །
--- END BLOCKS ---
