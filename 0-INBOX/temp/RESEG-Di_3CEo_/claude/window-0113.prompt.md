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
[Block 3956]
རྣམ་པ་ནི་སྡུག་བསྔལ་གསུམ་ལ་རྟོག་པའི་ཕྱིར་རོ། །

[Block 3957]
དམིགས་པ་ནི་ཁམས་གསུམ་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3958]
མཉམ་པ་ཉིད་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་འདྲ་བར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 3959]
ཆས༌[^1550]ཆེ་བ་ཉིད་ནི་དེ་ལས་ཆེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 3960]
སྙིང་རྗེ་དང་། ཐུགས་རྗེ་ཆེན་པོ་གཉིས་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཡོད་ཅེ་ན། ཐ་དད་བྱ་བ་རྣམ་པ་བརྒྱད། །ངོ་བོ་ཉིད་ལས་ནི་ཞེ་སྡང་མེད་པ་དང་།

[Block 3961 [VERSE]]
གཏི་མུག་མེད་པའི་ངོ་བོའི་ཕྱིར་རོ། །
རྣམ་པ་ལས་ནི་སྡུག་བསྔལ་གཅིག་དང་།
གསུམ་གྱི་རྣམ་པ་ཅན་གྱིས་སོ། །
དམིགས་པ་ལས་ནི་ཁམས་གཅིག་དང་། །

[Block 3962 [VERSE]]
གསུམ་གྱི་སེམས་ཅན་ལ་དམིགས་པས་སོ། །
ས་ལས་ནི་བསམ་གཏན་བཞི་དང་།
བསམ་གཏན་བཞི་པའི་ས་པས་སོ། །

[Block 3963]
རྒྱུད་ལས་ནི་ཉན་ཐོས་ལ་སོགས་པ་དང་། སངས་རྒྱས་ཀྱི་རྒྱུད་ལ་སྐྱེས་པས་སོ། །

[Block 3964]
ཐོབ་པ་ལས་ནི་འདོད་པའི་ཁམས་དང་། སྲིད་པའི་རྩེ་མོའི་འདོད་ཆགས་དང་བྲལ་བས་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 3965]
ཡོངས་སུ་མི་སྐྱོབ་པ་དང་ཡོངས་སུ་སྐྱོབ་པ་དང་། མི་འདྲ་བ་དང་། འདྲ་བར་ཐུགས་རྗེ་ཆེན་པོ་མཛད་པའི་ཕྱིར་རོ། །

[Block 3966 [HEADING]]
#### སངས་རྒྱས་ཐམས་ཅད་མཉམ་པ། ^7-5-5-0

[Block 3967]
ཅི་སངས་རྒྱས་ཐམས་ཅད་ཀྱིས་མཉམ་པ་ཡིན་ཞེ་ན།

[Block 3968 [VERSE]]
སངས་རྒྱས་ཐམས་ཅད་ཚོགས་དང་ནི། །
ཆོས་སྐུ་འགྲོ་བའི་དོན་སྤྱོད་པས། །
མཉམ་པ་ཉིད་དེ་སྐུ་ཚེ་དང་། །
རིགས་དང་སྐུ་བོང་ཚོད་ཀྱིས་མིན། །

[Block 3969]
སངས་རྒྱས་ཐམས་ཅད་ནི་རྒྱུ་གསུམ་པོ་སྔོན་གྱི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱིས་ཡང་དག་པར་འགྲུབ་པ་དང་། ཆོས་ཀྱི་སྐུ་ཡོངས་སུ་འགྲུབ་པ་དང་། འཇིག་རྟེན་གྱི་དོན་སྤྱོད་པས་མཉམ་པ་ཉིད་ཡིན་ནོ། །

[Block 3970]
སྐུ་ཚེ་དང་། རིགས་དང་། གདུང་དང་། སྐུ་བོང་ཚོད་དུ་མཛད་པ་ལ་ནི་བྱེ་བྲག་ཡོད་དོ། །

[Block 3971]
རེ་ཞིག་དེ་དག་ནི་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་བཅོ་བརྒྱད་ཅེས་བྱའོ། །

[Block 3972 [HEADING]]
### སློབ་པ་དང་ཐུན་མོང་བའི་ཆོས། ^7-6-0

[Block 3973 [VERSE]]
ཆོས་གཞན་སློབ་དང་ཐུན་མོང་ཡིན། །
ཁ་ཅིག་སོ་སོའི་སྐྱེ་བོ་དང་། །
དེ་དག་ཀྱང་གང་ཞེ་ན།
ཉོན་མོངས་མེད་དང་སྨོན་ནས་ཤེས། །
སོ་སོ་ཡང་དག་རིག་མངོན་སོགས། །

[Block 3974]
དེ་ལ།

[Block 3975 [HEADING]]
#### ཉོན་མོངས་མེད་པ། ^7-6-1-0

[Block 3976 [VERSE]]
ཉོན་མོངས་མེད་པ་ཀུན་རྫོབ་ཤེས། །
དེ་ཡི་རང་བཞིན་འདི་ཡིན་ཏེ། །

[Block 3977]
བསམ་གཏན་མཐའ་ན། བསམ་གཏན་བཞི་པའི་ས་པ་ཡིན་ཏེ། ལམ་སླ་བ་རྣམས་ཀྱི་མཆོག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3978]
མི་གཡོའི་ཆོས། དགྲ་བཅོམ་པ་གཞན་གྱི་ནི་མ་ཡིན་ནོ། །

[Block 3979]
མིས་བསྐྱེད། གླིང་གསུམ་དུ་བསྐྱེད་དོ། །

[Block 3980]
ཉོན་མོངས་འདོད་གཏོགས་པ། མ་སྐྱེས་གཞིར༌[^1551]བཅས་སྤྱོད་ཡུལ་ཅན། །དེའི་དམིགས་པ་ནི་ཉོན་མོངས་པ་འདོད་པ་ན་སྤྱོད་པ་མ་འོངས་པ་གཞི་དང་བཅས་པ་རྣམས་ཡིན་ཏེ། ཕ་རོལ་པོ་དག་ཉོན་མོངས་པ་སྐྱེ་བར་མ་གྱུར་ཅིག་ཅེས་ཞུགས་པའི་ཕྱིར་རོ། །

[Block 3981 [HEADING]]
#### སྨོན་ནས་ཤེས་པ། ^7-6-2-0

[Block 3982]
ཉོན་མོངས་པ་མེད་པ་ཇི་སྐད་དུ་བཤད་པ།

[Block 3983 [VERSE]]
སྨོན་ནས་ཤེས་པའང་དེ་བཞིན་ནོ། །
དེ་ཡང་ཀུན་རྫོབ་ཤེས་པ་དང་། །

[Block 3984]
བསམ་གཏན་གྱི་མཐའ་ན་ཡོད་པ་དང་། མི་གཡོ་བའི་ཆོས་ཅན་ཡིན་པ་དང་། མིའི་རྟེན་ཅན་ཡིན་ནོ། །

[Block 3985]
དེའི་དམིགས་པ་ཐམས་ཅད་དོ། །

[Block 3986]
སྨོན་ནས་ཤེས་པའི་དམིགས་པ་ནི་ཆོས་ཐམས་ཅད་དང་ལྡན་ནོ། །

[Block 3987 [HEADING]]
#### སོ་སོ་ཡང་དག་པར་རིག་པ། ^7-6-3-0

[Block 3988 [VERSE]]
དེ་བཞིན་ཆོས་དོན་ངེས་ཚིག་དང་། །
སྤོབས་པ་སོ་སོ་ཡང་དག་རིག །

[Block 3989]
དེ་བཞིན་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་མེད་པ་མི་གཡོ་བའི་ཆོས་ཅན་དང་། མིའི་རྟེན་ཅན་བཞིན་ནོ། །

[Block 3990]
འདི་དག་ནི་དམིགས་པ་དང་། ས་དང་། རང་གི་ངོ་བོའི་བྱེ་བྲག་ནི་ཐ་དད་པར་བརྗོད་དོ།[^1552] །

[Block 3991]
གསུམ་ནི་གོ་རིམས་བཞིན་མིང་དང་། དོན་དང་ངག་ལ་ཐོགས་མེད་ཤེས། །མིང་དང་ཚིག་དང་ཡི་གེའི་ཚོགས་རྣམས་དང་། དོན་དང་། ངག་ལ་ཐོགས་པ་མེད་པར་ཤེས་པ་ནི་ཆོས་དང་། དོན་དང་། ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་རྣམས་སོ། །

[Block 3992 [VERSE]]
བཞི་པ་རིག་པ་ཐགས་ཐོགས་མེད། །
མངོན་སྤྱོད་ལམ་ལ་དབང་ཉིད་ལ། །

[Block 3993]
ཐགས་ཐོགས་མེད་པར་མངོན་པར་བརྗོད་པ་ཉིད་དང་། ཏིང་ངེ་འཛིན་ལ་དབང་བར་བསལ་བར༌[^1553]བྱ་བ་ལ་ཐོགས་པ་མེད་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 3994]
དེ་ཡི་དམིགས་པ་ངག་དང་ལམ། །དེའི་དམིགས་པ་ནི་ངག་ཀྱང་ཡིན་ལ་ལམ་ཡང་ཡིན་ནོ། །ཤེས་པ་དགུའོ། །

[Block 3995]
དེའི་རང་བཞིན་ནི་འགོག་པ་ཤེས་པ་མ་གཏོགས་པ་དགུའོ། །
--- END BLOCKS ---
