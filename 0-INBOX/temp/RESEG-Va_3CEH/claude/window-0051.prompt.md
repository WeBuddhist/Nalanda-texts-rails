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
[Block 1786]
འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་ཡང་ཚིག་གཅིག་གིས་སོ། །

[Block 1787]
ཤིན་ཏུ་རྣམ་པར་དག་པའི་རིགས༌[^1051]ལ་གང་དབང་སྒྱུར་བའི་མཚན་ཉིད་དེ་ནི་བདག་པོ་ཕུན་སུམ་ཚོགས་པ་སྟེ་ཚིག་གཅིག་གིས་སོ། །

[Block 1788]
ཕྱོགས་ཕུན་སུམ་ཚོགས་པ་ནི་ཚིག་གཅིག་གིས་སོ། །

[Block 1789]
ཞམ༌[^1052]རིང་བ་ཕུན་སུམ་ཚོགས་པ་ཡང་ཚིག་གཅིག༌[^1053]གིས་སོ།[^1054] །དེ་དག་ཉིད་ལ་ཀླུ་སྨོས་པས༌[^1055]ནི་ལྟོ་འཕྱེ་ཆེན་པོ་ཡང༌[^1056]གཟུང་བར་བྱ་སྟེ། སྦྲུལ་ཆེན་པོ་བསྡུ་བའི་ཕྱིར་རོ། །

[Block 1790]
དེ་ལ་ཉེ་བར་སྟོན་པར་བྱེད་པ་ནི་སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ཏེ། ཚིག་གཅིག་གིས་བསྟན་ཏོ། །

[Block 1791]
དེ་དག་བརྗོད་ནས་ཕྲིན་ལས་གང་ཡིན་ཞེ་ན། སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་ཐམས་ཅད་མཛད་པ་སྟེ། ཕུན་སུམ་ཚོགས་པ་དེ་ཡང་ཚིག་གཅིག་གིས་སོ། །

[Block 1792]
ཕན་འདོགས་པ་ཕུན་སུམ་ཚོགས་པ་ཡང་ཚིག་གཅིག་གིས་ཏེ། གང་གི་ཕྱིར་དེར༌[^1057]ཉོན་མོངས་པ་ཡང་མི་འབྱུང་སྡུག་བསྔལ་ཡང་མི་འབྱུང་བའོ། །

[Block 1793]
གང་ལ་དགྲ་མེད་པ་དེ་ནི་འཇིགས་པ་མེད་པ་ཡིན་ཏེ། བདུད་བཞི་མེད་པའི་ཕྱིར་རོ། །

[Block 1794]
ཡང་དེ་ནི་སངས་རྒྱས་ཀྱི་ཞིང་དེ་ན་ཕུང་པོའི་བདུད་ཡོད་པ་མ་ཡིན། ཉོན་མོངས་པའི་བདུད་ཡོད་པ་མ་ཡིན། འཆི་བདག་གི་བདུད་ཡོད་པ་མ་ཡིན། ལྷའི་བུའི་བདུད་ཡོད་པ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་འཇིགས་པ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་སྟེ། དེ་ཡང་ཚིག་གཅིག་གིས་བསྟན་ཏོ། །

[Block 1795]
གནས་ཕུན་སུམ་ཚོགས་པ་ཡང་གཅིག་གིས་བསྟན་ཏོ། །

[Block 1796]
ཡང་ལམ་གང་གིས་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པ་དེར་དེ་འཇུག་ཅེ་ན། ཐེག་པ་ཆེན་པོ་ཐོས་པ་དང་། བསམས་པ༌[^1058]དང་། བསྒོམས་པའི་ཤེས་རབ་ཀྱིས་ཏེ། དྲན་པ་དང་། བློ་གྲོས་དང་། རྟོགས་པ་ཆེན་པོ་དང་གོ་རིམས་བཞིན་དུ་སྦྱར་རོ། །

[Block 1797]
ལམ་ཕུན་སུམ་ཚོགས་པ་དེ་ཡང་ཚིག་གཅིག་གིས་བསྟན་ཏོ། །

[Block 1798]
བཞོན་པ༌[^1059]ནི་ཞི་གནས་དང་ལྷག་མཐོང་སྟེ། དེས་འགྲོ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1799]
ཕུན་སུམ་ཚོགས་པ་དེ་ཡང་གཅིག་གིས་བསྟན་ཏོ། །

[Block 1800]
སྒོ་གང་ནས་དེར་འཇུག་ཅེ་ན། སྟོང་པ་ཉིད་དང་། མཚན་མ་མེད་པ་དང་། སྨོན་པ་མེད་པ་ཉིད་ནི་སྒོ་ཕུན་སུམ་ཚོགས་པ་སྟེ། དེ་ཡང་ཚིག་གཅིག་གིས་བསྟན་ཏོ། །

[Block 1801]
གཞི་ཕུན་སུམ་ཚོགས་པ་ཡང་ཚིག་གཅིག་གིས་བསྟན་ཏེ། ཇི་ལྟར་ས་གཞི་རླུང་གི་དཀྱིལ་འཁོར་ལ་རབ་ཏུ་བརྟེན་ཅིང་གནས་པ་དེ་བཞིན་དུ་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པ་དེ་གང་ལ་བརྟེན་ཅིང་གནས་ཤེ་ན། ཡོན་ཏན་གྱི་ཚོགས་ཚད་མེད་པས་བརྒྱན་པའི་རིན་པོ་ཆེའི་པདྨའི་རྒྱལ་པོ་ཆེན་པོ་བཀོད་པ༌[^1060]ལ་བརྟེན་པ་ན་ཞེས་བྱའོ།[^1061] །

[Block 1802 [HEADING]]
#### ཡོངས་སུ་དག་པ་དེའི་ལོངས་སྤྱོད། ^9-3-2-0

[Block 1803]
ཡོངས་སུ་དག་པ་དེའི་ལོངས་སྤྱོད་ནི་ཤིན་ཏུ་གཙང་བ་ཞེས་བྱ་བ་ལ། གང་གི༌[^1062]ཕྱིར་དེའི་གཙང་བ་ཉིད་ནི་དེ་ན་ཕྱི་ས་ལ་སོགས་པ་མི་གཙང་བ་མེད་པ་ཉིད་དོ། །

[Block 1804]
ཤིན་ཏུ་བདེ་བ་ནི་གང་ཚོར་བ་བདེ་བ་འབའ་ཞིག་དང་ལྡན་གྱི་སྡུག་བསྔལ་ཡང་མེད་ཅིང་བཏང་སྙོམས་ཀྱང་མེད་པའོ། །

[Block 1805]
ཤིན་ཏུ་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཞེས་བྱ་བ་ནི། འདི་ལྟར་དེ་ནི་མི་དགེ་བའམ། ལུང་དུ་མ་བསྟན་པ་མེད་པའོ། །

[Block 1806]
ཤིན་ཏུ་དབང་སྒྱུར་བ་ཞེས་བྱ་བ་ནི། དེས༌[^1063]རང་གི་སེམས་ལ་དབང་སྒྱུར་བ༌[^1064]ཡིན་པའི་ཕྱིར་གང་རྐྱེན་གཞན་ལ་ནི་མི་ལྟོས༌[^1065]པའོ། །

[Block 1807 [HEADING]]
### ཕྲིན་ལས་ལྔ་དང་ལྡན་པ། ^9-4-0

[Block 1808]
ཡང་སངས་རྒྱས་རྣམས་ཀྱི་ཆོས་ཀྱི་དབྱིངས་དེ་ནི་ཞེས་བྱ་བ་ནི་ཆོས་ཀྱི་སྐུའོ། །

[Block 1809]
དེ་ཡང་ཕྲིན་ལས༌[^1066]ལྔ་དང་ལྡན་པར་རིག་པར་བྱའོ། །

[Block 1810]
སེམས་ཅན་ཐམས་ཅད་ཀྱི༌[^1067]གནོད་པ་ལས་ཡོངས་སུ་སྐྱོབ་པའི་ཕྲིན་ལས་ཅན་ཞེས་བྱ་བ་ནི་གང་གིས་ཁམས་གསུམ་ལས་ཤིན་ཏུ་འདའ་བར་བྱེད་པའི་ལམ་དེ་འཇིག་རྟེན་ལ་སྟོན་པའོ། །

[Block 1811]
ཁམས་གསུམ་ནི་འདིར་འཇིག་ཚོགས་སྨོས་པས་བསྟན་པ་ཡིན་ནོ། །

[Block 1812]
ཚིག་ལྷག་མ་རྣམས་ཀྱི་དོན་ནི་གོ་སླའོ། །

[Block 1813]
སངས་རྒྱས་ཐམས་ཅད་ཕྲིན་ལས་ལྔ་པོ་འདི་དག་གིས་ཕྲིན་ལས་མཉམ་པ་ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 1814 [HEADING]]
### ཕྲིན་ལས་མཉམ་པ་ཉིད། ^9-5-0

[Block 1815]
འདིར་དོན་འདི་དག་གི་ཚིགས་སུ་བཅད་པ་ནི། རྒྱུ་དང་གནས་དང་བྱ་བ་དང་ནི་བསམ་པ་དང་། །ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གང་སངས་རྒྱས་རྣམས་ཀྱི་ཕྲིན་ལས་མཉམ་པ་ཉིད་དེ་རྒྱུ་གང་གིས་ཡིན་པ་རྒྱས་པར་བསྟན་ཏོ། །

[Block 1816]
གང་ཡང་འཇིག་རྟེན་པ་རྣམས་ཀྱི་ཡུལ་གྱི་ལས་ཉིད་གང་ཡིན་པ་དེ་ནི་ཚིགས་སུ་བཅད་པ་འདི་དག་གིས་བསྟན་ཏེ།

[Block 1817 [HEADING]]
#### རྒྱུ་ཐ་དད་པ། ^9-5-1-0

[Block 1818]
འཇིག་རྟེན་པ་རྣམས་ཀྱི་རྒྱུ་ཐ་དད་པ་ཡིན་པ་དེའི་ཕྱིར་འདི་ལྟར་དམྱལ་བ་ཡང་རྒྱུ་གཞན་ལས།

[Block 1819]
མི་རྣམས་ཀྱང་རྒྱུ་གཞན་ལས་དེ་བཞིན་དུ་ཡི་དགས་ཀྱི་བར་དུ་ཡང་སྟེ། དེའི་ཕྱིར་རྒྱུ་ཐ་དད་པ་དེས་ན། འཇིག་རྟེན་རྣམས་ཀྱི་ལས་ནི་ཐ་དད་གྱུར་པར་འདོད།

[Block 1820 [HEADING]]
#### གནས་ཐ་དད་པ། ^9-5-2-0

[Block 1821]
གནས་ཐ་དད་པ་ཉིད་ནི་འདི་ལྟར་འདི༌[^1068]དག་གིས༌[^1069]གནས་ཐ་དད་པ་སྟེ་ལུས་སོ། །

[Block 1822]
དེས་ན་ལས་ཀྱང་ཐ་དད་དོ། །

[Block 1823 [HEADING]]
#### བྱ་བ་ཐ་དད་པ། ^9-5-3-0

[Block 1824]
བྱ་བ་ཐ་དད་པ༌[^1070]ཞེས་བྱ་བ་ནི་འདི་ལྟར་གཞན་དག་ནི་ཚོང་བྱེད། གཞན་དག་ནི་གར་བྱེད་པ་ལ་སོགས་པའི་ལས་ཐ་དད་པ་དང་རབ་ཏུ་ལྡན་པ་སྟེ། དེའི་ཕྱིར་བྱ་བ་ཐ་དད་པས་ཀྱང་འཇིག་རྟེན་པ་རྣམས་ཀྱི་ལས་ཐ་དད་པ་ཡིན་ནོ། །

[Block 1825 [HEADING]]
#### བསམ་པ་ཐ་དད་པ། ^9-5-4-0
--- END BLOCKS ---
