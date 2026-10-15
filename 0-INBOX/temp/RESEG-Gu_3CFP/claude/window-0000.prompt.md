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
### ༄༅། །བྱང་ཆུབ་སེམས་དཔའི་སའི་འགྲེལ་པ།

[Block 2 [HEADING]]
## ཀླད་ཀྱི་དོན། ^I-0

[Block 3]
༄༅༅། །རྒྱ་གར་སྐད་དུ། བོ་དྷི་སཏྭ་བྷཱུ་མི་བྲྀཏྟི། བོད་སྐད་དུ། བྱང་ཆུབ་སེམས་དཔའི་སའི་འགྲེལ་པ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །

[Block 4 [HEADING]]
## བྱང་ཆུབ་སེམས་དཔའི་སའི་གཞིའི་རྣལ་འབྱོར་གྱི་གནས་ལས་རིམ་པར་ཕྱེ་བ། ^1-0

[Block 5]
འཕགས་པ་འཇམ་དཔལ་གཞོན་ནུར་གྱུར་པ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 6 [VERSE]]
སེམས་ཅན་ཀུན་ལ་ཕན་འདོད༌[^1]པས། །
མ་མོ་གང་ཞིག་ཤེས་པ་དེ། །
ཤེས་བྱའི་ཕ་རོལ་མཐར་འགྲོ་བ། །
དེ་ཡི་བཤད་པ་བརྩམ་པར་བྱ། །

[Block 7]
ཚིགས་སུ་བཅད་པ་འདི་བརྩམས་པའི་དགོས་པ་གང་ཞེ་ན། དགོས་པ་མཐོང་བའོ། །

[Block 8]
དགོས་པའི་དོན་གང་དོན་ཆེན་པོའི་དོན་མཐོང་བ་སྟེ།

[Block 9 [VERSE]]
བསྟན་བཅོས་དོན་ཆེན་མཐོང་ནས་ནི། །
མཉན་པ་དང་ནི་གཟུང་བའི་ཕྱིར། །
ཐོས་འདོད་གུས་པར་གྱུར་པ༌[^2]ནི། །
དང་པོ་ཚིག་གིས་དགོས་པ་ཡིན། །

[Block 10]
ཞེས་གསུངས་པས་སོ། །

[Block 11]
མ་མོའི་དོན་ཆེན་པོ་མཐོང་བས།[^3] ཚིགས་སུ་བཅད་པ་འདི་ཡང་དོན་ཆེ་བ་ཉིད་ཀྱིས། ཡང་འདི་ཉིད་ཀྱི༌[^4]དོན་ཆེ་བའི་ངོ་བོ་ནི་བརྗོད་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 12]
འགྲོ་བ་ཞེས་བྱ་བ་ནི་འཐོབ་པའོ། །

[Block 13]
ཡང་ན་རྟོགས་པ་སྟེ། ཡེ་ཤེས་མཐོང་བའི་དོན་དུ་འགྲོ་བས་སོ། །

[Block 14]
ཚིག་གཅིག་ལ་ཡང་ངེས་པར་བཟུང་བ༌[^5]མཐོང་བའི་ཕྱིར་ཏེ། འདི་ལྟ་སྟེ་ཆུ་འཐུང་དང་རླུང་ཟ་ཞེས་བྱ་བ་ལྟ་བུས་ན། འགྲོ་བ་ཞེས་བྱ་བ་ངེས་པར་གཟུང་བའི་དོན་དུ་རྟོགས་པར་བྱའོ། །

[Block 15]
གཞན་དུ་ན་ཚིག་ལ་ནུས་པ་མེད་པར་འགྱུར་རོ། །

[Block 16]
འགྲོ་བ་ནི་སོང་བར་གྱུར་པ་དང་། འོང་བར་འགྱུར་བ་དང་། འགྲོ་བ་སྟེ། འདི་ལྟ་སྟེ། རི་ནི་གནས་སོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །ཤེས་བྱ་ཞེས་བྱ་བ་ནི་ཤེས་པར་བྱ་བའོ།[^6] །དེའི་མཐའ་ནི་ཤེས་བྱའི་མཐའོ། །

[Block 17]
འདིར་པ་རིའི་རི་ཉེ་བར་བསྒྱུར་བ་ནི་ཁྱབ་པ་དང་ཀུན་དུའི༌[^7]དོན་ཏེ། ཀུན་དང་ཁྱབ་པའི་མཐའ་ནི༌[^8]པ་རི་ཨན་ཏ་སྟེ། མཐར་འགྲོ་བའོ། །

[Block 18]
གང་ཞིག་ཤེས་པ་ཞེས་བྱ་བ་ནི་གང་དེ་ཤེས་པས་ཡིན་གྱི། གཞན་གྱིས་ནི་མ་ཡིན་ལ་ཤེས་པ་ཡིན་གྱི་མི་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 19]
གང་ཞིག་ཤེས་པས་ཤེས་བྱའི་ཕ་རོལ་མཐར་འགྲོ་བ་དེ་གང་ཡིན་ཞེ་ན། བྱང་ཆུབ་སེམས་དཔའི་སྡེ་སྣོད་རྒྱས་པ་སྟེ། ཤེས་བྱའི་ཕ་རོལ་མཐར་འགྲོ་བ་གཞན་དག་ལ་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 20]
དེའི་མ་མོས༌[^9]ནི་ཤིན་ཏུ་རྒྱས་པའི་མཚན་ཉིད་ཅན་གྱི༌[^10]ཤིན་ཏུ་རྒྱས་པའི་སྡེ་སྣོད་ཀྱི་མ་མོ་ཞེས་བྱ་བ༌[^11]སྟེ། མ་མོ་དང་འདྲ་བས་ན་མ་མོའོ། །

[Block 21]
ཇི་ལྟར་ཡི་གེའི་མ་མོ་མ་གཏོགས་པའི་བསྟན་བཅོས་མི་དམིགས་པ་དེ་བཞིན་དུ། བྱང་ཆུབ་སེམས་དཔའི་སར་བསྟན་པའི་མཚན་ཉིད་དང་བྲལ་བའི་ཤིན་ཏུ་རྒྱས་པའི་སྡེ་སྣོད་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 22]
དེའི་ཞེས་བྱ་བ་ནི་མ་མོའིའོ། །གང་གིས་ཅི་ཙམ༌[^12]ཞེ་ན། སྨྲས་པ། སེམས་ཅན་ཀུན་ལ་ཕན་འདོད༌[^13]པས་སོ། །

[Block 23]
སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པར༌[^14]འདོད་པ་ནི་ལེགས་པར་བྱེད་པ་སྟེ།

[Block 24 [VERSE]]
སེམས་ཅན་ཀུན་ལ་ཕན་པར༌[^15]འདོད་པའོ། །
ཇི་ལྟ་བུའི་ཕན་པ་ཞིག་ཅེ་ན།
བཤད་པ་མ་མོའི་དོན་བསྟན་པའོ། །

[Block 25]
དེ་བསྟན་པས་ཀྱང་རྒྱ་ཆེན་པོའི་སྡེ་སྣོད་ཀྱང་བསྟན་པར་འགྱུར་བས་ཚིགས་སུ་བཅད་པ་འདིའི་བསྡུས་པའི་དོན་ནི་དེ་ཡིན་ནོ། །

[Block 26]
བྱང་ཆུབ་སེམས་དཔའི་སའི་སྡེ་འདིའི་བསྡུས་པའི་དོན་ནི། རྣལ་འབྱོར་གྱི་གཞིའི་གནས་དང་། རྣལ་འབྱོར་གྱི་གཞིའི་བདག་ཉིད་ཀྱི་གནས་དང་། རྣལ་འབྱོར་གྱི་གཞིའི་མཐའི་གནས་སོ། །

[Block 27]
རྣལ་འབྱོར་གྱི་གཞིའི་གནས་ནི༌[^16]ལེའུ་བཅོ་བརྒྱད་དོ། །

[Block 28]
རྣལ་འབྱོར་གྱི་གཞིའི་སྒྲུབ་པའི་ཆོས་ནི་ལེའུ་བཞིའོ། །

[Block 29]
རྣལ་འབྱོར་གྱི་གཞིའི་མཐའ་ནི་ལེའུ་ལྔ་སྟེ། གང་དེ་ནི་ཆོས་བཅུ་པོ་འདི་དག་ནི་ཐེག་པ་ཆེན་པོ་བྱང་ཆུབ་སེམས་དཔའི་ལམ་འབྲས་བུ་དང་བཅས་པ་སྡུད་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 30]
བཅུ་གང་ཞེ་ན། གཞི་དང་། རྟགས་དང་། ཕྱོགས་དང་། ལྷག་པའི་བསམ་པ་དང་། གནས་པ་དང་། སྐྱེ་བ་དང་། ཡོངས་སུ་འཛིན་པ་དང་། ས་དང་། སྤྱོད་པ་དང་། རབ་ཏུ་གནས་པའོ་ཞེས་བྱ་བའོ། །

[Block 31]
གྲངས་བཅུར་བསྡུས་པ་ནི་གྲངས་ངེས་པར་གཟུང་བའི་དོན་ཏེ། བཅུ་ལས་མི་མང་ཞིང་མི་ཉུང་ངོ་། །ཐེག་པ་ཆེན་པོ་སྡུད་པར་བྱེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ཕྱིན་པར་བྱེད་པས་ན་ཐེག་པའོ། །

[Block 32]
དེ་ནི་ཐེག་པ་ཡང་ཡིན་ལ་ཆེན་པོ་ཡང་ཡིན་པས་ཐེག་པ་ཆེན་པོ་སྟེ། འཆད་པར་འགྱུར་བའི་ཆེན་པོ་ཉིད་རྣམ་པ་བདུན་གྱི༌[^17]ཚུལ་གྱིས་སོ། །

[Block 33]
རབ་ཏུ་གནས་པའི་ལེའུ་ནི་འབྲས་བུ་ཉིད་ཡིན་པས་ན། ཐེག་པ་ཆེན་པོར་མ་བསྡུས་པས་དེས་ན་བྱང་ཆུབ་སེམས་དཔའི་ལམ་འབྲས་བུ་དང་བཅས་པ་ཞེས་བསྟན་ཏོ། །

[Block 34]
འདིས་ཐོབ་པར་བྱེད་པས་ན་ལམ་མམ་ཐོབ་པར་བྱ་བས་ན་ལམ་སྟེ། འདི་ལྟར་ཡེ་ཤེས་དང་ཐོབ་པར་བྱ་བའི་འབྲས་བུ་ནི་ལམ་ཞེས་བསྟན་པར་འགྱུར་རོ། །

[Block 35]
དེ་ལྟ་བུའི་མཚན་ཉིད་ཅན་གྱིས་ཐེག་པ་ཆེན་པོས་ནི་རབ་ཏུ་གནས་པའི་ལེའུ་ཡང་འདི་ལྟར་བསྡུས་པར་འགྱུར་རོ། །

[Block 36]
འདིས་འཛིན་པར་བྱེད་པས་ན་རྟེན་ཏེ། གང་གི་ཕྱིར་བརྟེན་པ༌[^18]ལ་ལྟོས་ནས་རྟེན་ཉིད་ཡིན་ན། གང་གི་རྟེན་ཡིན་ཞེས་བརྟེན་པ་འདྲི་བས། དེ་ལྟ་བས་ན་སྐལ་བ་དང་ལྡན་པ་ཞེས་སྨྲས་སོ། །

[Block 37]
དེ་བཞིན་དུ་གཞན་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 38]
ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཡོངས་སུ་རྫོགས་ཞེས་ཅིའི་ཕྱིར་བརྗོད། འདི་ལྟར་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་འཐོབ༌[^19]ཅེས་མི་བརྗོད་ཅེ་ན། རྣམ་པ་ཐམས་ཅད་ཤིན་ཏུ་གནས་གྱུར་པའི་མཚན་ཉིད་ཅན་ནི་བྱང་ཆུབ་ཡིན་ལ། སྦྱིན་པ་ལ་སོགས་པའི་སྦྱོར་བ་ཙམ་གྱིས་ནི་མི་ཐོབ་བོ། །

[Block 39]
འོན་ཀྱང་སྦྱིན་པ་ལ་སོགས་པའི་རིམ་གྱིས་གང་གློ་བུར་པའི་དྲི་མ་བསལ་ནས། མཐར་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ལ་ཡང་དག་པར་བརྟེན་པའི་ལམ་ནི་བྱང་ཆུབ་བོ། །

[Block 40]
གང་ཟག་རིགས་ལ་གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པའི༌[^20]གཞུང་གིས་ཅི་ཞིག་བསྟན། རིགས་ལ་གནས༌[^21]པའི་རྟེན་རྣམས་ཡོད་ན་ཡང་རིགས་ཉིད་གཙོར་བརྟེན༌[^22]ཞེས་རབ་ཏུ་བསྟན་ཏེ། རིགས་མེད་ན་གཞན་ཡོད་ན་ཡང་རྣམ་པ་ཐམས་ཅད་དུ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བ་མེད་པ་ཉིད་ཡིན་ལ། རིགས་ཡོད་ན་ནི་དུས་གཞན་ན་སེམས་བསྐྱེད་པ་ལ་སོགས་པ་བྱས་ནས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
