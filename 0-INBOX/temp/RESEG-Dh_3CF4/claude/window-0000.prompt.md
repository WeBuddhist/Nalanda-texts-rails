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
## ༄༅། །སྐྱེས་པའི་རབས་ཀྱི་རྒྱ་ཆེར་བཤད་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། ཛཱ་ཏ་ཀ་མཱ་ལཱ་ཊཱི་ཀཱ། བོད་སྐད་དུ། སྐྱེས་པའི་རབས་ཀྱི་རྒྱ་ཆེར་བཤད་པ། བཅོམ་ལྡན་འདས་ངག་གི་དབང་པོ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [VERSE]]
ཐུབ་པའི་ལེགས་སྤྱོད་རྨད་བྱུང་དཔག་མེད་པ། །
སྙན་ངག་མཁན་པོ་འཕགས་པ་དཔའ་བོས་བཀོད། །
བདག་བློ་ཞན་ཀྱང་གུས་པས་བཤད་པ་ནི། །
བློ་ཆུང་དག་ལ་ཕན༌[^1]ཕྱིར་རབ་ཏུ་བརྩམས། །

[Block 5]
དཔལ་ལྡན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས༌[^2]བཅད་འདི་ནི་འོག་ནས་འབྱུང་བའི་སྙན་ངག་མཐའ་དག་གི༌[^3]བསྡུས་པའི་དོན་ཡིན་ཏེ། བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱི་རང་བཞིན་བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པའི་དབང་དུ་བྱས་ནས་བདག་གིས་སྙན་ངག་འདི་བྱའོ། །ཞེས་བྱ་བ་ནི་ཚིགས་སུ་བཅད་པ་འདིའི་བསྡུས་པའི་དོན་ནོ། །

[Block 6]
དེ་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་སྟེ། སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པ་དང་། བརྩོན་འགྲུས་དང་། བསམ་གཏན་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའོ། །

[Block 7]
ཕ་རོལ་ཏུ་ཕྱིན་པ་དེ་དག་ལས་དང་པོའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གསུམ་པོ་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་དང་། བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་ཏེ། འཁོར་བའི་འཁོར་དང་། ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པའི་རྒྱུར་གྱུར་པས་སོ། །

[Block 8]
བསམ་གཏན་དང་། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཉིས་ནི་རྣམ་པར་གྲོལ་བའི་རྒྱུར་གྱུར་པ་ཡིན་པར་ངེས་པར་གཟུང་ངོ་། །བརྩོན་འགྲུས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་གཉིས་ཀའི་ཕྱོགས་ལ་བརྟེན་པ་ཡིན་ནོ། །

[Block 9]
གང་དག་ལ་དཔལ་ཡོད་པ་དེ་ནི་དཔལ་ལྡན་ཏེ། གཟི་མདངས་བཟང་པོ་དང་ལྡན་པ་ཡིན་ནོ།[^4] །དཔལ་དང་། འོད་དང་། འབར་བ་ཞེས་བྱ་བ་ནི་རྣམ་གྲངས་སོ། །

[Block 10]
འདིར་དཔལ་ཞེས་བྱ་བ་སྨོས་པས་ནི། བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་སྟེ། འཁོར་བའི་ལོངས་སྤྱོད་དང་། འཁོར་ཕུན་སུམ་ཚོགས་པ་བཟུང་སྟེ།

[Block 11 [VERSE]]
སྦྱོར་བ་འདིས་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །
ཡོན་ཏན་དམ་པས་ཡོངས་བཟུང་བཀྲ་ཤིས་པ། །

[Block 12]
ཞེས་བྱ་བ་ནི་ཡོན་ཏན་ཡང་ཡིན་ལ་དམ་པ་ཡང་ཡིན་པས་ཡོན་ཏན་དམ་པའོ། །

[Block 13]
ཡང་ན་ཡོན་ཏན་བཟང་པོ་ཡིན་པས་ཡོན་ཏན་དམ་པའོ། །

[Block 14]
ཡང་ན་སྐྱེས་བུ་དམ་པ་རྣམས་ཀྱི་ཡོན་ཏན་ཡིན་པས་སོ།[^5] །ཡོངས་བཟུང་ཞེས་བྱ་བ་ནི་འདི་དག་གིས་ཡོངས་སུ་བཟུང་བས་ནའོ། །

[Block 15]
ཡོན་ཏན་དམ་པ་ཡང་ཡིན་ལ་ཡོངས་སུ་བཟུང་བ་ཡང་ཡིན་པས་ཡོན་ཏན་དམ་པས་ཡོངས་བཟུང་ངོ་། །དེ་དག་གི་བཀྲ་ཤིས་ཡིན་པས་ཡོན་ཏན་དམ་པས་ཡོངས༌[^6]བཟུང་བཀྲ་ཤིས་སོ།[^7] །དེ་ལ་ཡོན་ཏན་ནི་གཞན་ལ་ཕན་པ་ཁ་ན་མ་ཐོ་བ་མེད་པའི་བསོད་ནམས་ལ་འཇུག་པའོ། །

[Block 16]
གལ་ཏེ་དེ་ནི་དེ་ལྟ་ན་དམ་པ་ཞེས་སྨོས་པ་ཅི་ཞིག་དགོས་ཤེ་ན། བྱང་ཆུབ་སེམས་དཔའ་མ་ཡིན་པ་ཡང་གཞན་ལ་ཕན་པ་ལ་འཇུག་པ་དེ་དག་ནི་བདག་ལ་ཕན་པ་དང་འབྲེལ་པའི་དངོས་པོ་སྟོན་ཅིང་ཡོན་ཏན་གྱི་འབྲས་བུ་ཡོད་པར་གྱུར་པ་སྟེ།[^8] གང་ཞིག་ཅེ་ན། ཉན་ཐོས་དང་རང་སངས་རྒྱས་ལྟ་བུ་སྟེ། དེའི་ཡོན་ཏན་ནི་རང་གི་རྒྱུད་ལས་བྱུང་བའི་ཉོན་མོངས་པ་འཇོམས་པའོ། །

[Block 17]
[^9]ཡོངས་སུ་སྔོ་བར༌[^10]བྱེད་པ་སྟེ། སྔ་མ་ནི་དེ་ལྟ་བུ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 18]
ཡང་ན་ཡོངས་སུ་བཟུང་བ་ཡིན་པས་ན་ཡོངས་སུ་བཟུང་བ་སྟེ། ཡོན་ཏན་དམ་པ་རྣམས་ཀྱིས་ཡོངས་སུ་བཟུང་བས་ན། ཡོན་ཏན་དམ་པས་ཡོངས་བཟུང་ངོ་། །ཡོན་ཏན་དམ་པས་ཡོངས་སུ་གཟུང་བའི༌[^11]བཀྲ་ཤིས་པ་ནི། ཡོན་ཏན་དམ་པས་ཡོངས་བཟུང་བཀྲ་ཤིས་པའོ། །

[Block 19]
བཀྲ་ཤིས་ཞེས་བྱ་བ་ནི། དགེ་ཤིས་དང་དག་བྱེད་དོ། །

[Block 20]
གྲགས་པའི་གཞིར་གྱུར་ཅེས་བྱ་བ་ནི་གྲགས་པའི་གཞིར་གྱུར་པས་ན་གྲགས་པའི་གཞིར་གྱུར་ཏེ། གྲགས་པའི་གནས་སུ་གྱུར་པ་ཞེས་པའི༌[^12]དོན་ཏོ། །

[Block 21]
འདིས་ནི་མངོན་དུ་འགྲོ་བས་དེའི་སྤྱོད་པ་སྟོན་པ་ཡིན་ནོ། །

[Block 22]
གལ་ཏེ་དེ་ལྟ་ཡིན་ན་ནི། བྱང་ཆུབ་སེམས་དཔའ་མ་ཡིན་པ་གཞན་བརྒྱ་བྱིན་དང་། པ་བ་སངས་དང་། སྐེམ་བྱེད་དང་། ཉེ་དབང་ལ་སོགས་པའི་སྤྱོད་པ་དག་ལ་ཡང་གྲགས་པའི་གཞིར་གྱུར་པ་ཡོད་ཅེ་ན། སྨྲས་པ། མ་སྨད་བཞིན་དུ༌[^13]ཤིན་ཏུ་ཡིད་དུ་འོང་། །ཞེས་སྨོས༌[^14]སོ། །

[Block 23]
གྲགས་པ་ནི་སྙན་པ་སྟེ་རྣམ་གྲངས་སོ། །

[Block 24]
མ་སྨད་ཅེས་བྱ་བ་ནི་སྨད་པ་མ་ཡིན་པས་ན་མ་སྨད་པ་སྟེ། དེས་རང་གི་རྒྱུད་བརྒྱན་ཅིང་འཇིག་རྟེན་ལས་འདས་པར་གྱུར་པས་སོ། །

[Block 25]
ཡང་ན་མ་སྨད་པ༌[^15]ནི་མཆོད་པར་འོས་པའི་གཞིར་གྱུར་པ་སྟེ་མ་སྨད་པའོ། །

[Block 26]
དེ་བས་ན་དེ་ཉིད་ཡིད་དུ་འོང་བ་སྟེ། མ་སྨད་ཤིན་ཏུ་ཡིད་འོང་ངོ་། །འདིས་ནི་སྤྱོད་པ་དེའི་ཡེ་ཤེས་ཀྱི་ཚོགས་གཞན་ལ་ཕན་པར་སྟོན་པ་ཡིན་ནོ། །

[Block 27]
འཇིག་རྟེན་པ་རྣམས་ལ་ཡང་། ཤེས་པ་ནི་ཡོད་མོད་ཀྱི་ཚོགས་ནི་མ་ཡིན་ཏེ། འདིས་སངས་རྒྱས་པའི་རྒྱུར་གྱུར་པ་དང་། སངས་རྒྱས་སུ་འཇོག་པར་བྱེད་པས་ཚོགས་སོ། །

[Block 28]
ཡིད་འཕྲོག་པར་བྱེད་པས་ཡིད་དུ་འོང་བའོ། །

[Block 29]
སྐུ་ཚེ་སྔ་མ་རྣམས་སུ་ཞེས་བྱ་བ་ནི་འདི་ལྟར་སྔོན་གྱི་མཐའི་སྐྱེ་བ་ནས་གང་དུ་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པའི་བར་བརྙེས་པའི་སྐྱེ་བ་དེ་ནི་མཐའི་བར་རོ། །

[Block 30]
ཐུབ་པ་ཞེས་བྱ་བ་ནི་གསུམ་ཐུབ་པས་ན་ཐུབ་པ་སྟེ། བཅོམ་ལྡན་འདས་སོ། །

[Block 31]
ཡང་ན༌[^16]ཉོན་མོངས་པ་སྐྱེ་བ་འགོག་པས་ན་ཐུབ་བའོ། །

[Block 32]
དེའི་སྤྱོད་པ་ནི་སྤྱོད་པ་སྟེ་ཚུལ་ལོ། །

[Block 33]
དེའི་སྤྱོད་པ་རྨད་དུ་བྱུང་བ་ཡིན་པས༌[^17]རྨད་དུ་བྱུང་བ་སྟེ་སྤྱོད་པ་ངོ་མཚར་བའོ། །

[Block 34]
ཡང་ན་དེའི་སྤྱོད་པ་འདས་པར་གྱུར་པས་ནི༌[^18]མཐོང་བ་སྟེ། བརྒྱ་ལ་ཞིག་ན་ཉེ་བར་དམིགས་པ་ཡིན་པས་རྨད་དུ་བྱུང་བ་རྣམས་སོ། །

[Block 35]
གུས་པས་ཞེས་བྱ་བ་ནི་དགའ་ཞིང་ཞེས་པས་ཞེས་བྱའོ། །

[Block 36]
འདིས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་སྟོན་པ་ཡིན་ནོ། །

[Block 37]
རང་གི་སྙན་ངག་ཡིན་པས་བདག་གི་སྙན་ངག་གོ། །

[Block 38]
བདག་གི་སྙན་ངག་ཉིད་མེ་ཏོག་ཡིན་པས་བདག་གི་སྙན་ངག་མེ་ཏོག་གོ། །

[Block 39]
མེ་ཏོག་བཞིན་དུ་མེ་ཏོག་གི་མཆོད་པའི་ཡོ་བྱད༌[^19]ཆོས་མཐུན་པ་ཡིན་པའི་ཕྱིར་ཇི་ལྟར་དེ་མེ་ཏོག་ལ་སོགས་པའི་སྙིམ་པ་སྟེ། བདག་གི་སྙན་ངག་མེ་ཏོག་སྙིམ་པའོ། །

[Block 40]
སྙིམ་པ་ནི་ལག་པ་གཉིས་སྦྱར༌[^20]བའོ། །
--- END BLOCKS ---
