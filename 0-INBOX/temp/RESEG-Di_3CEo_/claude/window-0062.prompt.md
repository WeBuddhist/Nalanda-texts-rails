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
[Block 2171]
འདི་ནི་རྒྱུད་ཀྱི་སྒོ་ནས་རྣམ་པར་གཞག་གི་ངོ་བོ་ཉིད་ཀྱི་སྒོ་ནས་ནི་མ་ཡིན་ནོ། །

[Block 2172]
ཟག་པ་མེད་པའི་ལས་ནི་ལས་གསུམ་པོ་དེ་དག་ཟད་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 2173]
དེ་ནི་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པའི་ཕྱིར་མི་གནག་པའོ། །

[Block 2174]
རྣམ་པར་སྨིན་པ་དཀར་པོ་ཉིད་མེད་པའི་ཕྱིར་མི་དཀར་བའོ། །

[Block 2175]
འཇུག་པ་དང་འགལ་བས༌[^863]ཁམས་སུ་མ་གཏོགས་པའི་ཕྱིར་རྣམ་པར་སྨིན་པ་མེད་པ་ཡིན་ནོ། །

[Block 2176]
ཟག་པ་མེད་པའི་ལས་ཐམས་ཅད་ལས་གསུམ་པོ་འདི་ཐམས་ཅད་ཟད་པར་བྱེད་པ་ཡང་མ་ཡིན་ཏེ། འོན་ཀྱང་།

[Block 2177 [VERSE]]
ཆོས་བཟོད་འདོད་ཆགས༌[^864]བྲལ་བ་ཡི།[^865] །
བར་ཆད་མེད་ལམ་བརྒྱད་ཀྱི་གང་། །
སེམས་པ་རྣམ་པ་བཅུ་གཉིས་ཏེ། །
ནག་པོ་ཟད་པར་བྱེད་པའི་ལས། །

[Block 2178]
མཐོང་བའི་ལམ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་བཞི་དང་། འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་ལ་བར་ཆད་མེད་པའི་ལམ་བརྒྱད་ཀྱི་སེམས་པ༌[^866]གང་ཡིན་པ་སྟེ། རྣམ་པ་བཅུ་གཉིས་པོ་དེ་དག་ནི་ནག་པོའི་ལས་ཟད་པར་བྱེད་པའི་ལས་ཡིན་ནོ། །

[Block 2179 [VERSE]]
དགུ་པའི་སེམས་པ་གང་ཡིན་པ། །
དེ་ནི་དཀར་ནག་ཟད་བྱེད་ཡིན། །

[Block 2180]
འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་ལ་བར་ཆད་མེད་པའི་ལམ་དགུ་པོའི༌[^867]སེམས་པ་གང་ཡིན་པ་དེ་ནི་དཀར་གནག་གི་ལས་དང་། ནག་པོ༌[^868]དཀར་བ་མ་ཡིན་པའི་རྣམ་པ་དགུ་པོ༌[^869]སྤོང་བར་བྱེད་དོ། །

[Block 2181 [VERSE]]
དཀར་པོ་བསམ་གཏན་ཆགས་བྲལ་བའི། །
བར་ཆད་མེད་ལམ་སྐྱེས་ཐ་མས། །

[Block 2182]
བསམ་གཏན་དང༌[^870]བསམ་གཏན་ལས་འདོད་ཆགས་དང་བྲལ་བར་བྱེད་པའི་བར་ཆད་མེད་པའི་ལམ་ཐ་མ་དགུ་པ་དེའི་སེམས་པ་འདི་ནི་དཀར་པོའི༌[^871]ལས་སྤོང་བར་བྱེད་པའོ། །

[Block 2183 [VERSE]]
གཞན་ནི་དམྱལ་བ་མྱང་འགྱུར་དང་། །
འདོད་གཞན་མྱོང་འགྱུར་གཉིས་སུ་རིག །
དམྱལ་བ་མྱོང་བར་འགྱུར་བ་དང་། །

[Block 2184]
དམྱལ་བ་ལས་གཞན་འདོད་པའི་ཁམས་སུ་མྱོང་བར་འགྱུར་བ་རིམ་པ་བཞིན་དུ་ནག་པོ་དང་དཀར་གནག་ཡིན་ནོ། །

[Block 2185 [VERSE]]
གཞན་ནི་མཐོང་བས་སྤང་བྱ་གནག །
དགེ་བ་དང་མ་འདྲེས༌[^872]པའི་ཕྱིར་རོ། །
འདོད་པ་ལས་སྐྱེས་གཞན་དཀར་གནག །

[Block 2186]
འདོད་པའི་ཁམས་ལ་དཀར་གནག་ནི་བསྒོམ་པས་སྤང་བ༌[^873]ཡིན་ནོ། །

[Block 2187 [HEADING]]
#### ཐུབ་པ་གསུམ། ^4-3-6-0

[Block 2188]
མདོ་ལས་ཐུབ་པའི་ནི་གསུམ་སྟེ་ཞེས་གསུངས་པ་དེ་ལ།

[Block 2189 [VERSE]]
མི་སློབ་ལུས་ངག་ལས་ཡིད་ཉིད། །
ཐུབ་པའི་གསུམ་སྟེ་གོ་རིམས་བཞིན། །

[Block 2190]
མི་སློབ་པའི་ལུས་དང་ངག་གི་ལས་ནི་ཐུབ་པའི་ལུས་དང་ངག་གི་ལས་ཡིན་ནོ། །

[Block 2191]
མི་སློབ་པའི་ཡིད་ཁོ་ན་ཡིད་ཀྱི་ཐུབ་པ་ཡིན་ཏེ། ཡིད་ཀྱི་ལས་ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། ཐུབ་པའི་ཡང་སྤོང་བའི་དོན་གྱིས་ཡིན་ཏེ། དེའི་ཕྱིར་ཡིད་ཉིད་སྤོང་བ་ལ་ཐུབ་པ་ཞེས་བྱའོ། །

[Block 2192 [HEADING]]
#### གཙང་བྱེད་གསུམ། ^4-3-7-0

[Block 2193]
གཙང་བྱེད་གསུམ་གསུངས་པ་དེ་ལ།

[Block 2194 [VERSE]]
ལེགས་སྤྱད་གསུམ་པོ་ཐམས་ཅད་ནི། །
གཙང་བྱེད་རྣམ་པ་གསུམ་ཡིན་ནོ། །

[Block 2195]
ལུས་ཀྱི་ལེགས་པར་སྤྱད་པ་ཐམས་ཅད་ནི་ལུས་གཙང་བྱེད་ཡིན་ནོ། །

[Block 2196]
དེ་བཞིན་དུ་ངག་དང་ཡིད་ཀྱི་ལས་གཙང་བ་ཡིན་ཏེ། ལུས༌[^874]རེ་ཞིག་དང་གཏན་དུ་ཉེས་པར་སྤྱད་པའི་ཉོན་མོངས་པའི་དྲི་མ་སྤོང་བའི་ཕྱིར་རོ། །

[Block 2197 [HEADING]]
#### ཉེས་པར་སྤྱད་པ་གསུམ། ^4-3-8-0

[Block 2198]
ཉེས་པར་སྤྱད་པ་གསུམ་གསུངས་པ་དེ་ལ།

[Block 2199 [VERSE]]
ལུས་ཀྱི་ལ་སོགས་མི་དགེ་བ། །
ཉེས་པར་སྤྱད་པ༌[^875]གསུམ་དུ་འདོད། །

[Block 2200]
ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་མི་དགེ་བ་ནི་ལུས་དང་ངག་དང་ཡིད་ཀྱི་ཉེས་པར་སྤྱད་པ་ཡིན་ནོ། །

[Block 2201 [VERSE]]
བརྣབ་སེམས་ལ་སོགས་ལས་མིན་ཡང་། །
ཡིད་ཀྱི་ཉེས་སྤྱད་རྣམ་གསུམ་མོ། །
ལས་ཀྱི་རང་བཞིན་མ་ཡིན་ཡང་། །

[Block 2202]
ཡིད་ཀྱི་ཉེས་པར་སྤྱད་པ་རྣམ་པ་གསུམ་ཡོད་དེ། བརྣབ་སེམས་དང་། གནོད་སེམས་དང་ལོག་པར་ལྟ་བའོ། །

[Block 2203]
བཟློག་པ་ལེགས་པར་སྤྱད་པ་ཡིན། ཉེས་པར་སྤྱད་པ་ལས་བཟློག་པ་ནི་ལེགས་པར་སྤྱད་པར༌[^876]རིག་པར་བྱའོ། །

[Block 2204 [HEADING]]
#### ལས་ཀྱི་ལམ་བཅུ། ^4-3-9-0

[Block 2205]
ཉེས་པར་སྤྱད་པ་དང་ལེགས་པར་སྤྱད་པ་བཤད་པ་གང་དག་ཡིན་པ།

[Block 2206 [VERSE]]
དེ་ལས་ཆེ་ལོང་བསྡུས་ནས་ནི། །
དགེ་དང༌[^877]མི་དགེ་ཅི་རིགས་པར། །
ལས་ཀྱི་ལམ་ནི་བཅུར་གསུངས་སོ། །

[Block 2207]
དགེ་བ་རྣམས་ནི་ལེགས་པར་སྤྱད་པ་དག་ལས་སོ། །

[Block 2208]
མི་དགེ་བ་རྣམས་ནི་ཉེས་པར་སྤྱད་པ་དག་ལས་སོ། །

[Block 2209]
འདིར་ཉེས་པར་སྤྱད་པ་ཅི་ཞིག་དང་། ལེགས་པར་སྤྱད་པ་ཅི་ཞིག་མ་བསྡུས་ཤེ་ན། རེ་ཞིག་མི་དགེ་བ་རྣམས་ལས་ལུས་ཀྱི་ཉེས་པར་སྤྱད་པའི་ཕྱོགས་སྦྱོར་བ་དང་། མཇུག་དང་། ཉོན་མོངས་པ་ཅན་རྡེག་པ༌[^878]ལ་སོགས་པ་དང་། ཡིད་ཀྱི་ཉེས་པར་སྤྱད་པའི་ཕྱོགས་སེམས་པ་མ་བསྡུས་སོ། །

[Block 2210]
དགེ་བ༌[^879]ལ་ལུས་ཀྱི་ལེགས་པར་སྤྱད་པའི་ཕྱོགས་སྦྱོར་བ་དང་། མཇུག་དང་། མྱོས་པར་འགྱུར་བ་ལ་སོགས་པ་སྤོང་བ་དང་། སྦྱིན་པ་དང་། མཆོད་སྦྱིན་ལ་སོགས་པ་དང་། ངག་གི་ཉེས་པར་སྤྱད་པ་ཡང་སྙན་པར་སྨྲ་བ་ལ་སོགས་པ་དང་། ཡིད་ཀྱི་ལེགས་པར་སྤྱད་པའི་སེམས་པ་མ་བསྡུས་སོ། །
--- END BLOCKS ---
