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
[Block 4061]
ངག་དང་རང་ས་ལས།

[Block 4062]
སྐྱེ་བར་འགྱུར་ཏེ། སྤྲུལ་པའི་སེམས་ནི་བསམ་གཏན་དག་པ་པའི་མཇུག་ཐོགས་སུ་སྐྱེ་བའམ། སྤྲུལ་པའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་སྐྱེའོ། །

[Block 4063]
དེ་ལས་གཉིས། བསམ་གཏན་དག་པ་པ་དང་སྤྲུལ་པའི་སེམས་དག་སྐྱེའོ། །

[Block 4064]
སྤྲུལ་པའི་སེམས་ཐམས་ཅད་ཀྱང་།

[Block 4065 [VERSE]]
རང་གི་ས་པས་སྤྲུལ་བར་བྱེད། །
ས་གཞན་པ་ཡིས་ནི་མ་ཡིན་ནོ། །
སྨྲར་འཇུག་པ་ནི་འོག་མས་ཀྱང་། །

[Block 4066]
ཀྱང་གི་སྒྲས་ནི་རང་གི་ས་པས་ཡང་ངོ་། །འདོད་པའི་ཁམས་དང་། བསམ་གཏན་དང་པོའི་ས་པའི་སྤྲུལ་པ་ནི་རང་གི༌[^1575]ས་པའི་སེམས་ཁོ་ནས་སྨྲར་འཇུག་གོ། །

[Block 4067]
ས་གོང་མ་པ་ནི་བསམ་གཏན་དང་པོའི་ས་པས་སོ། །

[Block 4068]
སྤྲུལ་པ་མང་པོ་རྣམས་སྨྲ་བ་ནི། སྟོན་མིན་སྤྲུལ་པ་པོ་དང་བཅས། །སངས་རྒྱས་ལས་གཞན་པ་ནི་སྤྲུལ་པ་པོ་དང་བཅས་ཏེ་སྨྲའོ། །

[Block 4069]
གང་གི་ཚེ་སྨྲ་བའི་སེམས་པ་དེའི་ཚེ་སྤྲུལ་པའི་སེམས་མེད་པས་སྤྲུལ་པ་རྣམས་ཀྱང་མེད་དེ།

[Block 4070 [VERSE]]
ཇི་ལྟར་དེ་སྨྲ་འཇུག་ཅེ་ན། །
བྱིན་གྱིས་བརླབས་ནས་གཞན་འཇུག་ཕྱིར། །

[Block 4071]
གནས་པར་འདོད་པས་སྤྲུལ་པ་བྱིན་གྱིས་བརླབས་ནས་ཡིད་གཞན་རྣམ་པར་རིག་བྱེད་ཀུན་ནས༌[^1576]སློང་བར་བྱེད་པས་ངག་འཇུག་པར་བྱེད་དོ། །

[Block 4072]
ཅི་གསོན་པོ་ཁོ་ན་ལ་བྱིན་གྱི་རླབ༌[^1577]ཡོད་དམ་ཞེ་ན། ཤི་བ་ལ་ཡང་བྱིན་རླབས༌[^1578]ཡོད། །མི་བརྟེན་ལ་མེད། ཤ་དང་ཁྲག་ལ་སོགས་པ་བྱིན་གྱིས་བརླབས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4073]
གཞན་དག་མིན། གཞན་དག་ན་རེ་ཤི་བ་ལ་བྱིན་གྱིས་བརླབས་པ༌[^1579]མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 4074]
ཅི་སེམས་གཅིག་གིས་སྤྲུལ་པ་གཅིག་ཁོ་ན་སྤྲུལ་པར་བྱེད་དམ་ཞེ་ན། དང་པོར་དུ་མས་གཅིག་ཡིན་ཏེ། །

[Block 4075]
དང་པོ་ཉིད་དུ་ནི་སྤྲུལ་པའི་སེམས་དུ་མས་སྤྲུལ་པ་གཅིག་སྤྲུལ་པར་བྱེད་དོ། །

[Block 4076]
བྱང་བར་གྱུར་ནས་བཟློག་པའོ། །

[Block 4077]
མངོན་པར་ཤེས་པ་བྱང་ནས་ནི་སེམས་གཅིག་གིས་སྤྲུལ་པ༌[^1580]པོ་ཇི་སྙེད་འདོད་པ་དུ་མས་སྤྲུལ་པར་བྱེད་དོ། །

[Block 4078]
ཡང་ཅི༌[^1581]སྤྲུལ་པའི་སེམས་ཐམས་ཅད་ལུང་དུ་མ་བསྟན་པ་ཡིན་ནམ་ཞེ་ན།

[Block 4079 [VERSE]]
བསྒོམས་ལས་སྐྱེས་པ་ལུང་མ་བསྟན། །
སྐྱེ་བ་ལས་སྐྱེས་རྣམ་གསུམ་མོ། །

[Block 4080]
ལྷ་དང་ཤ་ཟ་ལ་སོགས་པའི་སྐྱེ་བས་ཐོབ་པའི་སྤྲུལ་པའི་སེམས་ནི་དགེ་བ་དང་མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 4081]
ཅི་བསྒོམས་པ་ལས་བྱུང་བ་དང་སྐྱེ་བས་ཐོབ་པའི་རྫུ་འཕྲུལ་རྣམ་པ་འདི་གཉིས་ཁོ་ནར་ཟད་དམ་ཞེ་ན། རྫུ་འཕྲུལ་རྣམ་པ་གཉིས་པོ་དེ་དག་དང་། གསང་སྔགས་སྨན་དག་དང་། །ལས་ལས་སྐྱེས་དང་རྣམ་པ་ལྔ། །རྫུ་འཕྲུལ་བཤད་ཟིན་ཏོ། །

[Block 4082 [HEADING]]
##### ལྷའི་མིག་དང་རྣ་བ། ^7-6-5-4-0

[Block 4083 [VERSE]]
ལྷ་ཡི་མིག་དང་རྣ་བ་ཡིན། །
བསམ་གཏན་ས་པའི་གཟུགས་དང་བ། །

[Block 4084]
བསམ་གཏན་ལ་སྙོམས་པར་ཞུགས་པས་སྒྲ་དང་སྣང་བ་ལ་གཏོང་པ་བསམ་གཏན་གྱི་ས་པའི་རྒྱུར་བྱས་པའི་གཟུགས་དང་བདག་མངོན་པར་འགྲུབ་པོ། །ཡང་དེ་དག་ནི།

[Block 4085 [VERSE]]
རྟག་ཏུ་སྟེན་བཅས་མ་ཚང་མེད། །
ཐག་རིང་ཕྲ་སོགས་སྤྱོད་ཡུལ་ཅན། །

[Block 4086]
ལྷའི་མིག་དང་རྣ་བ་ནི་དེ་དང་མཚུངས་པ་མེད་དོ། །

[Block 4087]
ཞར་བ་དང་འོན་པ་མེད་པའི་ཕྱིར་མ་ཚང་བ་ཡང་མ་ཡིན་ནོ། །

[Block 4088]
དེ་གཉིས་ཀྱི་ཡུལ་ནི་གཟུགས་དང་སྒྲ་ཐག་རིང་བ་དང་། ཕྲ་བ་དང་། བསྒྲིབས་པ་དག་ཀྱང་ཡིན་ནོ། །

[Block 4089]
དེ་ལ་ཡང་།

[Block 4090 [VERSE]]
དགྲ་བཅོམ་བསེ་རུ་སྟོན་རྣམས་ཀྱིས། །
སྟོང་གཉིས་གསུམ་དང་གྲངས་མེད་མཐོང་། །

[Block 4091]
ཉན་ཐོས་ཀྱི་ལྷའི་མིག་གིས་སྟོང་གཉིས་པའི་འཇིག་རྟེན་གྱི་ཁམས་མཐོང་ངོ་། །རང་སངས་རྒྱས་ཀྱིས་སྟོང་གསུམ་མོ། །

[Block 4092]
སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཀྱིས་ནི་འཇིག་རྟེན་གྱི་ཁམས་གྲངས་མེད་པ་གཟིགས་སོ། །

[Block 4093 [HEADING]]
##### སྐྱེ་བས་ཐོབ་པ། ^7-6-5-5-0

[Block 4094]
ཅི་རྫུ་འཕྲུལ་འབའ་ཞིག་སྐྱེ་བས་ཐོབ་པ་ཡིན་ནམ། འོན་ཏེ་གཞན་ཡང་ཡིན་ཞེ་ན། །གཞན་ཡང་སྐྱེ་བས༌[^1582]ཐོབ། ལྷའི་རྣ་བ་ལ་སོགས་པ་སྐྱེ་བས་ཐོབ་པ་ཡང་ཡོད་མོད་ཀྱི། མངོན་པར་ཤེས་པའི་མིང་མི་ཐོབ་པ།[^1583] དེས་ནི། སྲིད་པ་བར་མ་མི་མཐོང་ངོ་། །དེ་ནི་མངོན་པར་ཤེས་པ་ཁོ་ནས་མཐོང་བའི་ཕྱིར་རོ། །

[Block 4095]
སེམས་ཤེས་དེ་ནི་རྣམ་གསུམ། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་སྐྱེ་བས་ཐོབ་པ་ནི་དགེ་བ་དང་། མི་དགེ་བ་དང་།

[Block 4096]
ལུང་དུ་མ་བསྟན་པ་རྣམ་པ་གསུམ་མོ། །གང་རྟོག༌[^1584]དང་རིག་སྔགས་ཀྱིས༌[^1585]བྱས་པའང་། །

[Block 4097]
གང་ཡང་མཚན་མ་རྣམས་ཀྱིས༌[^1586]ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དང་། གང་ཡང་རིག་སྔགས་ཀྱིས་བྱས་པ་དེ་ཡང་རྣམ་པ་གསུམ་མོ། །

[Block 4098]
གཞན་གྱི་སེམས་ཤེས་པ་དང་། སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་སྐྱེ་བས་ཐོབ་པ་དག་ནི། དམྱལ་བ་བས་ནི་དང་པོ་ཤེས། །སྡུག་བསྔལ་གྱི་ཚོར་བས་མཉེན་པའི་བར་དུའོ། །

[Block 4099]
འགྲོ་བ་གཞན་ན་གནས་པས་ནི་རྟག་ཏུ་ཤེས་སོ། །

[Block 4100]
མི་ལ་སྐྱེ་བས་ཐོབ་པ་མེད། །མི་རྣམས་ལ་ནི་རྫུ་འཕྲུལ་ལ་སོགས་པ་སྐྱེ་བས་ཐོབ་པ་མེད་དོ། །
--- END BLOCKS ---
