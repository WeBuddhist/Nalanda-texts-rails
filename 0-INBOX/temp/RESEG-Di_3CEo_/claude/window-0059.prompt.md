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
[Block 2066]
མི་རྣམས་ལ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ལ་སོགས་པ་ཐམས་ཅད་ཡོད་དོ། །

[Block 2067]
འདོད་དང་གཟུགས་སྐྱེས་ལྷ་རྣམས་ལ། །བསམ་གཏན་སྐྱེས་ཡོད། བསམ་གཏན་གྱི་སྡོམ་པ་ནི་འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་སུ་སྐྱེས་པའི་ལྷ་རྣམས་ཁོ་ན་ལ་ཡོད་དོ། །

[Block 2068]
ཟག་མེད་ནི།

[Block 2069 [VERSE]]
བསམ་གཏན་ཁྱད་པར་འདུ་ཤེས་མེད། །
སེམས་ཅན་མ་གཏོགས་གཟུགས་མེད་ན་འང་། །

[Block 2070]
འདོད་པ་དང་གཟུགས་ཀྱི་ཁམས་སུ་སྐྱེས་པ་རྣམས་ལ༌[^822]ཡང་ཡོད་དོ།[^823] །

[Block 2071]
བསམ་གཏན་ཁྱད་པར་ཅན་དང་། འདུ་ཤེས་མེད་པའི་སེམས་ཅན་དུ་སྐྱེས་པ་མ་གཏོགས་སོ། །

[Block 2072]
གཟུགས་མེད་པར་སྐྱེས་པ་རྣམས་ལ་ཡང་ལྡན་པ་ཁོ་ནའི་སྒོ་ནས་ཡོད་དོ། །

[Block 2073 [HEADING]]
### མདོ་ལས་བསྟན་པའི་ལས་རྣམ་པར་བཤད་པ། ^4-3-0

[Block 2074]
འདི་མན་ཆད་ནི་མདོ་ལས་བསྟན་པའི་ལས་རྣམ་པར་བཤད་པ་བརྩམ་མོ། །

[Block 2075 [HEADING]]
#### ལས་བདེ་མི་བདེ་དང་གཞན། ^4-3-1-0

[Block 2076]
ལས་ནི་དགེ་བ་ལ་སོགས་པ་བསམ༌[^824]སྟེ། དེ་ལ།

[Block 2077 [VERSE]]
ལས་བདེ་མི་བདེ་དང་གཞན་ནི། །
བདེ༌[^825]བའི་ལས་ནི་དགེ་བ་སྟེ། །
འབྲས་བུ་ཡིད་དུ་འོང་བ་དང་། །

[Block 2078]
མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་བྱེད་པ་གང་ཡིན་པའོ། །

[Block 2079]
མི་དགེ་བའི་ལས་ནི་མི་དགེ་བ་སྟེ་དེ་ལས་བཟློག་པའོ། །

[Block 2080]
དེ་དག་ལས་གཞན༌[^826]བདེ་བ་ཡང་མ་ཡིན་པ་ལ་མི་བདེ་བ་ཡང་མ་ཡིན་པ་ནི་ལུང་དུ་མ་བསྟན་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2081 [HEADING]]
#### བསོད་ནམས་བསོད་ནམས་མིན་མི་གཡོ། ^4-3-2-0

[Block 2082 [VERSE]]
བསོད་ནམས་བསོད་ནམས་མིན་མི་གཡོ། །
བདེ་བ་མྱོང་འགྱུར་ལ་སོགས་གསུམ། །

[Block 2083]
དེ་ལ།

[Block 2084 [VERSE]]
བསོད་ནམས་འདོད་ཁམས་དགེ་བའི་ལས། །
མིག་ཡོ་གོང་མ་ལས་སྐྱེས་པའི། །

[Block 2085]
དགེ་བའི༌[^827]ཞེས་བྱ་བར་སྦྱར་ཏེ། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ལས་དགེ་བ་ནི་མི་གཡོ་བ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 2086 [VERSE]]
གང་ཕྱིར་ས་ནི་དེ་དག་ཏུ། །
ལས་རྣམ༌[^828]སྨིན་ཕྱིར་མི་གཡོའི་ཕྱིར། །

[Block 2087]
འདོད་པ་ན་སྤྱོད་པའི་ལས་ནི་རྣམ་པར་སྨིན་པའི་ཕྱིར་གཡོ་སྟེ། །འགྲོ་བ་གཞན་གྱི་ལས་འགྲོ་བ་གཞན་དུ་རྣམ་པར་སྨིན་པར་འགྱུར་ལ། ལྷའི་རིས་གཞན་གྱི་ཡང་ལྷའི་རིས་གཞན་ལའོ། །

[Block 2088]
བསོད་ནམས་མ་ཡིན་པའི་ལས་ནི་མི་དགེ་བའོ་ཞེས་འཇིག་རྟེན་ཉིད་དུ་གྲགས་སོ། །

[Block 2089]
བསོད་ནམས་ལ་སོགས་པའི་ལམ་བསྟན་ཟིན་ཏོ། །

[Block 2090 [HEADING]]
#### བདེ་བ་མྱོང་འགྱུར་ལ་སོགས་གསུམ། ^4-3-3-0

[Block 2091]
བསམ་གཏན་གསུམ་པའི་བར་དགེ་བ་དང་། བདེ་བ་མྱོང་འགྱུར། ས་འདི་ནི་ཚོར་བའི་ཡིན་ཏེ། འདི་ལྟ་སྟེ། འདོད་པའི་ཁམས་དང་བསམ་གཏན་གསུམ་མོ། །

[Block 2092]
དེ་ཡན་ཆད། སྡུག་མིན་བདེ་མིན་མྱོང་འགྱུར་བ། །དགེ་བ་ཞེས་བྱ་བར་སྦྱར་ཏེ། བསམ་གཏན་གསུམ་པ་ཡན་ཆད་ཀྱི་ལས་དགེ་བ་ནི་བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ༌[^829]ཡང་མ་ཡིན་པ་མྱོང་བ་ཡིན་ནོ། །

[Block 2093]
སྡུག་བསྔལ་མྱོང་འགྱུར་འདིའི་མི་དགེ །འདོད་པའི་ཁམས་ཁོ་ནའི་མི་དགེ་བའི་ལས་ནི་སྡུག་བསྔལ་གྱི་ཚོར་བ་མྱོང་བའོ། །

[Block 2094]
འོག་ནའང་བར་མ་ཡོད་དོ་ཞེས། །ཁ་ཅིག་ཟེར་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། གང་གི་ཕྱིར། བསམ་གཏན་ཁྱད་པར་རྣམ་སྨིན་ལས། །

[Block 2095]
དེ་ལྟ་མ་ཡིན་ན་བསམ་གཏན་ཁྱད་པར་ཅན་གྱི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་མེད་པའམ། ལས་གང་གིས་ཀྱང་བསམ་གཏན་ཁྱད་པར་ཅན་དུ་སྨིན་པར་མི་འགྱུར་རོ། །

[Block 2096]
སྔ་ཕྱི་མེད་གསུམ་སྨིན་འདོད་ཕྱིར། །འདོད་པའི་ཁམས་ལས་གཞན་ན༌[^830]ནི་ལས་གསུམ་གྱི་རྣམ་པར་སྨིན་པ་དག་ཅིག་ཅར་དུ་ལྡན་པ་མེད་དེ། བདེ་བ་མྱོང་བར་འགྱུར་བ་ནི་གཟུགས་སོ། །

[Block 2097]
སྡུག་བསྔལ་མྱོང་བར་འགྱུར་བ་ནི་སེམས་དང་། སེམས་ལས་བྱུང་བ་རྣམས་སོ། །

[Block 2098]
བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ་ཡང་མ་ཡིན་པ་མྱོང་བ་ནི་མི་ལྡན་པའི་འདུ་བྱེད་རྣམས་ཏེ། དེའི་ཕྱིར་ཡང་འོག་ན་བར་མ་ཡོད་དོ། །

[Block 2099]
ཇི་ལྟར་ན་ཚོར་བའི་རང་བཞིན་མ་ཡིན་པའི་ལས་བདེ་བ་མྱོང་བར་འགྱུར་ཞེས་བྱ་ཞེ་ན། འདི་ལ་འགལ་བ་མེད་དེ། གང་གི་ཕྱིར།

[Block 2100 [VERSE]]
ངོ་བོ་ཉིད་དང་མཚུངས་ལྡན་དང་། །
དམིགས་པ་དང་ནི་རྣམ་སྨིན་དང་། །
མངོན་སུམ་དུ་ནི་གྱུར་པ་ལས། །
མྱོང་འགྱུར་རྣམ་པ་ལྔ་ཡིན་ནོ། །

[Block 2101]
དེ་ལ་ངོ་བོ་ཉིད་ཀྱིས་མྱོང་བར་འགྱུར་བ་ནི་ཚོར་བ་རྣམས་སོ། །

[Block 2102]
མཚུངས་པར་ལྡན་པས་མྱོང་བར་འགྱུར་བ་ནི་རེག་པ་སྟེ། བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པ་ཞེས་བྱའོ། །

[Block 2103]
དམིགས་པ་མྱོང་བར་འགྱུར་བ་ནི་ཡུལ་རྣམས་ཏེ། ཇི་སྐད་དུ། མིག་གིས་གཟུགས་རྣམས་མཐོང་ནས་གཟུགས་སོ་སོར་ཡང་དག་པར་མྱོང་བ་ཞེས་བྱའོ། །

[Block 2104]
རྣམ་པར་སྨིན་པ་མྱོང་བར་འགྱུར་བ་ནི་ལས་ཡིན་ཏེ། མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཞེས་བྱའོ། །

[Block 2105]
མངོན་སུམ་དུ་གྱུར་པ་མྱོང་བར་འགྱུར་བ་ནི་ཇི་སྐད་དུ། གང་གི་ཚེ་བདེ་བའི་ཚོར་བ་ཉམས་སུ་མྱོང་བའོ། །
--- END BLOCKS ---
