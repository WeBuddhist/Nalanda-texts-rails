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

[Block 3996]
ས་ཐམས་ཅད་འདོད་པ་ནས་སྲིད་པའི་རྩེ་མོའི་བར་ས་ཐམས་ཅད་པ་ཡིན་ནོ། །

[Block 3997]
ཡང་དག་དོན་རིག་བཅུའམ་དྲུག །གལ་ཏེ་ཆོས་ཐམས་ཅད་ཡིན་ན་ནི་ཤེས་པ་བཅུའོ། །

[Block 3998]
འོན་ཏེ་མྱ་ངན་ལས་འདས་པ་ཡིན་ན་དྲུག་སྟེ། ཆོས་དང་རྗེས་སུ་ཤེས་པ་དང་། འགོག་པ་དང་། ཟད་པ་དང་། མི་སྐྱེ་བ་དང་། ཀུན་རྫོབ་ཤེས་པ་རྣམས་སོ། །

[Block 3999]
དེ་ནི་ཀུན་ན། དོན་སོ་སོ་ཡང་དག་པར་རིག་པ་ནི་ཐམས་ཅད་པའོ། །

[Block 4000]
གཞན་ཀུན་རྫོབ། ཆོས་དང་ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་དག་ནི་ཀུན་རྫོབ་ཤེས་པའི་རང་བཞིན་ནོ། །

[Block 4001 [VERSE]]
ཆོས་རིག་འདོད་དང་བསམ་གཏན་ན། །
འདོད་པ་དང་བསམ་གཏན་བཞི་ནའོ།[^1554] །
ངག་ནི་འདོད་དང་དང་པོ་ན། །

[Block 4002]
ངེས་པའི་ཚིག་སོ་སོ་ཡང་དག་པར་རིག་པ་ནི་འདོད་པའི་ཁམས་དང་།

[Block 4003 [VERSE]]
བསམ་གཏན་དང་པོའི་ས་པའོ། །
མ་ཚང་བར་ནི་དེ་ཐོབ་མེད། །

[Block 4004]
གང་ལ་གཅིག་ཡོད་པ་དེ་ལ་སོ་སོ་ཡང་དག་པར་རིག་པ་བཞི་ཆར་གདོན་མི་ཟ་བར་ཡོད་དོ། །

[Block 4005 [HEADING]]
#### རབ་ཀྱི་མཐའ། ^7-6-4-0

[Block 4006]
ཉོན་མོངས་པ་མེད་པ་ལ་སོགས་པའི་ཡོན་ཏན་བསྟན་པ༌[^1555]གང་ཡིན་པ། དྲུག་པོ་དེ་དག་བར་མཐའ་བས། །བསམ་གཏན་བཞི་པའི་སྟོབས་ཀྱིས་འདི་དག་འཐོབ་པོ། །དེ་ནི་རྣམ་དྲུག་ཉོན་མོངས་པ་མེད་པ་དང་། སྨོན་ནས་ཤེས་པ་དང་། སོ་སོ་ཡང་དག་པར་རིག་པ་གསུམ་དང་། རབ་ཀྱི་མཐའ་དེ་ཉིད་དང་། དྲུག་གི་བདག་ཉིད་དོ། །

[Block 4007]
རབ་ཀྱི་མཐའ་ཞེས་བྱ་བ་ནི༌[^1556]ཅི༌[^1557]ཞེ་ན། བསམ་གཏན་མཐའ། བསམ་གཏན་བཞི་པའོ། །

[Block 4008 [VERSE]]
དེ་ནི་ས་ཀུན་གྱིས་མཐུན་བྱས། །
འཕེལ་བའི་རབ་ཏུ་ཕྱིན་པ་ཡིན། །

[Block 4009]
འདོད་པ་ན་སྤྱོད་པའི་སེམས་ལས་བསམ་གཏན་དང་པོ་ལ་སྙོམས་པར་ཞུགས་པ་ནས། རིམ་གྱིས་བསམ་གཏན་བཞི་པའི་བར་དང་། དེ་བཞིན་དུ་གོང་མ་ལ་ཡང་སྟེ། དེ་ལྟར་ན་ས་ཐམས་ཅད་ཀྱིས་མཐུན་པར་བྱས་པ་ཡིན་ནོ། །

[Block 4010]
དེ་ལྟར་བསྒོམ་པ་ཆུང་ངུ་ལས་འབྲིང་དང་། འབྲིང་ལས་ཆེན་པོ་ལ་སྙོམས་པར་འཇུག་སྟེ། འཕེལ་བའི་རབ་ཡིན་ནོ། །

[Block 4011]
ཡོན་ཏན་དྲུག་པོ་དེ་ཡང་། སངས་རྒྱས་ལས་གཞན་སྦྱོར་ལས་སྐྱེས། །འདོད་ཆགས་དང་བྲལ་བས་ཐོབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 4012]
རེ་ཞིག་དེ་དག་ཉན་ཐོས་དང༌[^1558]ཐུན་མོང་པའོ། །

[Block 4013 [HEADING]]
#### མངོན་པར་ཤེས་པ། ^7-6-5-0

[Block 4014]
མངོན་པར་ཤེས་པ་ལ་སོགས་པ་སོ་སོའི་སྐྱེ་བོ་དང་ཡང་ངོ་། །མངོན་པར་ཤེས་པ་གང་ཞེ་ན།

[Block 4015 [VERSE]]
རྫུ་འཕྲུལ་རྣ་བ་ཡིད་དང་ནི། །
སྔོན་ཚེ་འཆི་འཕོ་སྐྱེ་བ་དང་། །
ཟད་ཤེས་མངོན་དུ་བྱ་བ་ཡི། །

[Block 4016]
མངོན་ཤེས་རྣམ་དྲུག་དེ་དག་ལས་ལྔ་ནི་སོ་སོའི་སྐྱེ་བོ་དང་ཐུན་མོང་པའོ། །

[Block 4017]
དེ་དག་ཐམས་ཅད་ནི། རྣམ་གྲོལ་བློ། རྣམ་པར་གྲོལ་བའི་ལམ་གྱི་ཤེས་རབ་ཀྱི་རང་བཞིན་ཡིན་ནོ། །

[Block 4018]
བཞི་ནི་ཀུན་རྫོབ་ཤེས་པ་སྟེ། །སེམས་ཀྱི་རྣམ་གྲངས་དང་། ཟག་པ་ཟད་པའི་མངོན་པར་ཤེས་པ་མ་གཏོགས་པའོ། །

[Block 4019]
སེམས་ལ་ཤེས་པ་ལྔ་ཡིན་ནོ། །

[Block 4020]
སེམས་ཀྱི་རྣམ་གྲངས་མངོན་པར་ཤེས་པ་ནི་ལྔ་སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། ལམ་དང་། ཀུན་རྫོབ་དང་། ཕ་རོལ་གྱི་སེམས་ཤེས་པ་རྣམས་སོ། །

[Block 4021]
ཟད་པའི་མངོན་ཤེས་སྟོབས་བཞིན་ནོ། །

[Block 4022]
འདི་ནི་ཟག་པ་ཟད་པའི་མཁྱེན་པའི་སྟོབས་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 4023]
ལྔ་ནི་བསམ་གཏན་བཞི་དག་ན།[^1559] ། མངོན་པར་ཤེས་པ་ལྔ་ནི་བསམ་གཏན་བཞིའི་ས་པའོ། །

[Block 4024]
ལྔ་པོ་དེ་དག་ནི།

[Block 4025 [VERSE]]
རང་དང་འོག་སའི་ཡུལ་ཅན་ཡིན། །
གོང་མའི་ནི་མ་ཡིན་ནོ། །

[Block 4026]
འདི་དག་ཇི་ལྟར་འཐོབ་ཅེ་ན། མ་འདྲིས་པ་རྣམས་ནི་སྦྱོར་བས། ཐོབ་བྱ་འདྲིས་པ་ཆགས་བྲལ་བས། །མངོན་པར་ཤེས་པ་ནི་ཚེ་རབས༌[^1560]གཞན་ན་གོམས་པ་རྣམས་ནི་འདོད་ཆགས་དང་བྲལ་བས་འཐོབ་བོ། །

[Block 4027]
གསུམ་པ་དྲན་པ་ཉེར་གཞག་གསུམ། །ཚོར་བ་དང་། སེམས་དང་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ་མོ། །

[Block 4028]
དང་པོ་རྫུ་འཕྲུལ་རྣ་བ་མིག །རྫུ་འཕྲུལ་དང་། ལྷའི་རྣ་བ་དང་། །མིག་གི་མངོན་པར་ཤེས་པ་ནི་ལུས་དྲན་པ་ཉེ་བར་གཞག་པའིའོ། །

[Block 4029]
ལྷག་མ་དག་ནི་དམིགས་ཀྱིས་མ་ཕྱེ་བའི་ཕྱིར་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་ཆར་གྱི་རང་བཞིན་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ༌[^1561]པོ། །

[Block 4030 [VERSE]]
མིག་དང་རྣ་བའི་མངོན་ཤེས་ནི། །
ལུང་དུ་མ་བསྟན་ལྷག་རྣམས་དགེ། །
--- END BLOCKS ---
