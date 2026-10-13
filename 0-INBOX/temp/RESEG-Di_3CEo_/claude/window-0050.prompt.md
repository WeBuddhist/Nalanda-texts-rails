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
[Block 1751 [HEADING]]
#### འཇིག་པ་གསུམ། ^3-8-9-0

[Block 1752]
ཡང་འཇིག་པ་དག་ནི་དུ་ཞེ་ན།

[Block 1753 [VERSE]]
མེ་དང་ཆུ་དང་རླུང་དག་གིས། །
འཇིག་པ་དག་ནི་ཡང་གསུམ་ཡིན། །

[Block 1754]
འདིའི་སེམས་ཅན་རྣམས་བསམ་གཏན་གཅིག་ཏུ་འདུ་བས་ན་འཇིག་པ་ཡིན་ནོ། །

[Block 1755]
ཉི་མ་བདུན་དུ་ནི་མེས་འཇིག་པ་ཡིན་ནོ། །

[Block 1756]
བར་གྱི་ཆུས་ནི་ཆུས་འཇིག་པ་ཡིན་ནོ། །

[Block 1757]
རླུང་རབ་ཏུ་འཁྲུགས་པས་ནི༌[^669]རླུང་གིས་རབ་ཏུ༌[^670]འཇིག་པ་ཡིན་ཏོ།[^671] །

[Block 1758]
དེ་དག་གིས་ནི་སྣོད་རྣམས་ཀྱི་ཆ་ཤས་ཕྲ་མོ་ཡང་མ་ལུས་པར་བྱེད་དོ། །

[Block 1759]
ཡང་འཇིག་པ་གང་གི་རྩེ་མོ་གང་ཡིན་ཞེ་ན།

[Block 1760 [VERSE]]
བསམ་གཏན་གཉིས་སོགས་གསུམ་པོ་ནི། །
དེ་དག་གི་རྩེ༌[^672]གོ་རིམས་བཞིན། །

[Block 1761]
མེས་འཇིག་པའི་རྩེ་མོ་ནི་བསམ་གཏན་གཉིས་པ་ཡིན་ཏེ། མན་ཆད་སྲེག་པར་བྱེད་དོ། །

[Block 1762]
ཆུས་འཇིག་པའི་རྩེ་མོ་ནི་གསུམ་པ་ཡིན་ཏེ། མན་ཆད་སྲུལ་བར་བྱེད་དོ། །

[Block 1763]
རླུང་གིས༌[^673]འཇིག་པའི་རྩེ་མོ་ནི་བཞི་པ་ཡིན་ཏེ། མན་ཆད་འཐོར་པར་བྱེད་དོ། །

[Block 1764]
ཡང་ཅིའི་ཕྱིར་བསམ་གཏན་དང་པོ་དང་།

[Block 1765]
གཉིས་པ་དང་།

[Block 1766]
གསུམ་པ་དག་མེ་དང་ཆུ་དང་རླུང་དག་གིས་འཇིག་ཅེ་ན། དེ་ཡི་སྐྱོན་དང་ཆོས་མཐུན་ཕྱིར། །བསམ་གཏན་དང་པོ་ན་ནི་རྟོག་པ་དང་དཔྱོད་པ་དག་སྐྱོན་ཡིན་ཏེ། དེ་དག་ཀྱང་ཡིད་ཡོངས་སུ་གདུང་བར་བྱེད་པ་དག་ཡིན་པའི་ཕྱིར་མེ་ལྟ་བུ་དག་ཡིན་ནོ། །

[Block 1767]
གཉིས་པ་ན་ནི་དགའ་བ་སྐྱོན་ཡིན་ཏེ། དེ་ཡང་ཤིན་ཏུ་སྦྱངས་པ་དང་ལྡན་པས་ལུས་མཉེན་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར། ཆུ་ལྟ་བུ་ཡིན་ནོ། །

[Block 1768]
བསམ་གཏན་གསུམ་པ་ན་ནི་དབུགས་རྔུབ་པ་དང་དབུགས་འབྱུང་བ་སྟེ། དེ་དག་ཀྱང་རླུང་ཁོ་ན་ཡིན་པས་སྙོམས་པར་འཇུག་པའི་བསམ་གཏན་གང་ན་ནང་གི་སྐྱོན་ཇི་ལྟ་བར་སྐྱེ་བའི་བསམ་གཏན་དེ་ན་ཕྱི་རོལ་གྱི་ཡང་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 1769]
འདི་ཁོ་ནའི་ཕྱིར།

[Block 1770]
བཞི་པ་ན་མེད་མི་གཡོའི་ཕྱིར། །བསམ་གཏན་བཞི་པ་ནི་ནང་གི་སྐྱོན་དང་བྲལ་བའི་ཕྱིར་མི་གཡོ་བ་ཞེས་གསུངས་ཏེ། དེའི་ཕྱིར་འདིར་ཕྱིའི་སྐྱོན་ཡང་མི་འཇུག་གོ། །

[Block 1771]
འོ་ན་བསམ་གཏན་བཞི་པའི་སྣོད་རྟག་པར་འགྱུར་རོ་ཞེ་ན།

[Block 1772 [VERSE]]
མི་རྟག་དེ་ཡི་གཞལ་མེད་ཁང་། །
སེམས་ཅན་བཅས་ཏེ་འབྱུང་འཇིག་ཕྱིར། །

[Block 1773]
བསམ་གཏན་བཞི་པ་ན་ནི་སེམས་ཅན་སྐྱེ་བ་འམ་འཆི་འཕོ་བའང་རུང་སྟེ། དེ་ནི་གཞལ་མེད་ཁང་དང་བཅས་ཏེ་ཡིན་པས་དེ་ལ་རྟག་པ་མེད་དོ། །

[Block 1774]
ཡང་འཇིག་པ་དེ་དག་གོ་རིམས་གང་གིས་འབྱུང་ཞེ་ན། རེ་ཞིག་བར་ཆད་མེད་པར་ནི། །མེ་ཡིས་བདུན་ནོ། །

[Block 1775]
མེས་འཇིག་པ་བདུན་འབྱུང་ངོ་། །དེའི་འོག་ཏུ་ནི་ཆུ་ཡིས་གཅིག །

[Block 1776]
མེས་འཇིག་པ་བདུན་གྱི་མཇུག་ཐོགས་སུ་ཆུ་ཡིས་གཅིག་འབྱུང་ངོ་། །དེ་ལྟར་ཆུ་བདུན་ཐལ་ནས་ཀྱང་། །མེ་ཡིས་བདུན་ནོ། །

[Block 1777]
རིམ་པ་དེས་ན་ཆུས་འཇིག་པ་བདུན་ཐལ་ནས་ཡང་མེས་འཇིག་པ་བདུན་འབྱུང་ངོ་། །དེ་ནས་ནི། མཇུག་ཏུ་རླུང་གིས༌[^674]འཇིག་པ་ཡིན། །དེ་ནས་རླུང་གིས་འཇིག་པ་གཅིག་འབྱུང་ངོ་། །དེ་ལྟར་འཇིག་པ་ནི་དེ་དག་གི་རིམ་པ་ཡིན་ནོ། །

[Block 1778]
འཇིག་རྟེན་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་གསུམ་པའོ།། །།

[Block 1779 [HEADING]]
## ལས་བསྟན་པ། ^4-0

[Block 1780]
ཡང་སེམས་ཅན་དང་སྣོད་ཀྱི་འཇིག་རྟེན་རྣམ་པ་སྣ་ཚོགས་པ་བཤད་པ་གང་ཡིན་པ་དེ་དག་སུས་བྱས་ཤེ་ན། སུས་ཀྱང་བློ་སྔོན་དུ་བཏང་ནས་བྱས་པ་ནི་མེད་དོ། །

[Block 1781]
འོན་ཀྱང་སེམས་ཅན་རྣམས་ཀྱི།

[Block 1782 [HEADING]]
### སེམས་པ་དང་བསམས་པའི་ལས། ^4-1-0

[Block 1783 [VERSE]]
ལས་ལས་འཇིག་རྟེན་སྣ་ཚོགས་སྐྱེས། །
ལས་ལས་དེ་ཅི་ཞིག་ཅེ་ན། །
དེ་ནི་སེམས་པ་དང་དེས་བྱས། །

[Block 1784]
སེམས་པ་དང་བསམས་པའི༌[^675]ལས་སོ་ཞེས་གསུངས་ལ། བསམས་པ་གང་ཡིན་པ་དེ་ནི་སེམས་པས་བྱས་པ་ཡིན་ནོ། །

[Block 1785]
ལས་གཉིས་པོ་དེ་དག་ནི་གསུམ་ཡིན་ཏེ། ལུས་དང་། ངག་དང་། ཡིད་ཀྱི་ལས་སོ། །

[Block 1786]
དེ་ལ་ཡང་།

[Block 1787 [VERSE]]
སེམས་པ་ཡིད་ཀྱི་ལས་ཡིན་ནོ། །
དེས་བསྐྱེད་ལུས་དང་ངག་གི་ལས། །
སེམས་པས་བསྐྱེད་པ་གང་ཡིན་པ། །

[Block 1788]
བསམས་པའི་ལས་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེ་དག་ནི་ལུས་དང་ངག་གི་ལས་སུ་རིག་པར་བྱའོ། །

[Block 1789]
དེ་དག་རྣམ༌[^676]རིག་རྣམ༌[^677]རིག་མིན། །དེ་དག་ཀྱང་རྣམ་པར་རིག་བྱེད་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་རང་བཞིན་ནོ། །

[Block 1790 [HEADING]]
#### ལུས་རྣམ་རིག་བྱེད། ^4-1-1-0
--- END BLOCKS ---
