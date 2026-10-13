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
[Block 4166]
དེ་དག་ན་ཅི་ཞིག་མེད་ཅེ་ན།

[Block 4167 [VERSE]]
ཉོན་མོངས་ཅན་ལ་དགའ་བདེ་དང་། །
རབ་དང་ཤེས་བཞིན་དྲན་པ་དང་། །
བཏང་སྙོམས་དྲན་པ་དག་པ་མེད། །

[Block 4168]
བསམ་གཏན་དང་པོ་ན་ནི་དབེན་པ་ལས་སྐྱེས་པའི་དགའ་བ་དང་བདེ་བ་མེད་དེ། ཉོན་མོངས་པ་ལས་དབེན་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4169]
གཉིས་པ་ན་ནི་རབ་ཏུ་དང་བ་མེད་དེ། ཉོན་མོངས་པས་རྙོགས་པའི་ཕྱིར་རོ། །

[Block 4170]
གསུམ་པ་ན་ནི་དྲན་པ་དང་ཤེས་བཞིན་མེད་དེ། ཉོན་མོངས་པ་ཅན་གྱི་བདེ་བས་ཀུན་དུ་རྨོངས་པར་བྱེད་དོ། །

[Block 4171]
བཞི་པ་ལ་ནི་བཏང་སྙོམས་དང་། །དྲན་པ་ཡོངས་སུ་དག་པ་མེད་དེ། ཉོན་མོངས་པས་དྲི་མ་ཅན་དུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 4172]
ཁ་ཅིག་ཤིན་ཏུ་སྦྱངས་བཏང་སྙོམས། །ཁ་ཅིག་ན་རེ་དང་པོ་དང་གཉིས་པ་དག་ན་ནི་ཤིན་ཏུ་སྦྱངས་པ་མེད་ལ།

[Block 4173]
གསུམ་པ་དང་བཞི་པ་དག་ན་ནི་བཏང་སྙོམས་མེད་དེ། དེ་གཉིས་ནི་དགེ་བའི་ས་མང་པོ་པ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 4174]
བཅོམ་ལྡན་འདས་ཀྱིས་བསམ་གཏན་གསུམ་ནི་སྐྱོན་དང་བཅས་པའི་ཕྱིར་གཡོ་བ་དང་བཅས་པ་དག་ཡིན་ནོ་ཞེས་བཀའ་སྩལ་ཏོ། །

[Block 4175 [VERSE]]
སྐྱོན་བརྒྱད་ལས་ནི་གྲོལ་བའི་ཕྱིར། །
བཞི་པ་གཡོ་བ་མེད་པ་ཡིན། །

[Block 4176]
སྐྱོན་དེ་དག་ཀྱང་གང་ཞེ་ན།

[Block 4177 [VERSE]]
རྟོག་དང་དཔྱོད་དང་དབུགས་དག་དང་།
བདེ་བ་ལ་སོགས་བཞི་ཡིན་ནོ། །

[Block 4178]
བསམ་གཏན་བཞི་པ་ལ་སྐྱོན་བརྒྱད་པོ་དེ་དག་ཀྱང་མེད་པས་དེའི་ཕྱིར་དེ་ནི་མི་གཡོ་བ་ཞེས་བཤད་དོ། །

[Block 4179 [HEADING]]
#### སྐྱེ་བའི་བསམ་གཏན་དག་གི་ཚོར་བ། ^8-1-5-0

[Block 4180]
ཅི་སྙོམས་པར་འཇུག་པའི་བསམ་གཏན་དག་ན་ཡོད་པའི་ཚོར་བ་གང་དག་ཡིན་པ་དེ་དག་ཉིད་སྐྱེ་བའི་བསམ་གཏན་དག་ན་ཡང་ཡོད་དམ་ཞེ་ན། མ་ཡིན་ཏེ། འོན་ཀྱང་།

[Block 4181 [VERSE]]
སྐྱེ་བའི་བསམ་གཏན་དག་ན་ནི། །
ཡིད་བདེ་བདེ་དང་བཏང་སྙོམས་དང་། །
བཏང་སྙོམས་ཡིད་བདེ་བདེ་བ་དང་། །
བཏང་སྙོམས་བཏང་སྙོམས་ཚོར་བ་ཡོད། །

[Block 4182]
འདི་ནི་བསམ་གཏན་རྣམས་ཀྱི་རྣམ་པར་ཤེས་པ་གསུམ་མམ་བཞིའི་ཚོགས་ཅི་རིགས་པ་དང་ཡིད་ཀྱི་ས་པའི་ཚོར་བ་དག་ཡིན་ནོ། །

[Block 4183]
རྣམ་པར་ཤེས་པའི་ཚོགས་གསུམ་རྟོག་པ་དང་དཔྱོད་པ༌[^1613]རྣམས་མེད་ཀྱང་།

[Block 4184 [VERSE]]
གཉིས་པ་སོགས་ན་ལུས་མིག་དང་། །
རྣ་བའི་རྣམ་ཤེས་རྣམ་རིག་སློང་། །
གང་ཡིན་དེ་ནི་དང་པོར་གཏོགས། །

[Block 4185]
བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་དག་ན་ནི་བསམ་གཏན་དང་པོའི་ས་པའི་མིག་དང་། རྣ་བ་དང་། ལུས་ཀྱི་རྣམ་པར་ཤེས་པ་དང་། རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་བྱེད་པ་མངོན་སུམ་དུ་བྱེད་དོ། །

[Block 4186 [VERSE]]
དེ་ལུང་མ་བསྟན་ཉོན་མོངས་མིན། །
ཉོན་མོངས་པ་ཅན་ནི་མ་ཡིན་ཏེ། །
འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 4187]
དམན་པའི་ཕྱིར་དགེ་བ་ཡང་མ་ཡིན་ནོ། །

[Block 4188 [HEADING]]
#### བསམ་གཏན་དང་གཟུགས་མེད་འཐོབ་པ། ^8-1-6-0

[Block 4189]
ཡང་དག་པ་ལ་སོགས་པའི་བསམ་གཏན་དང་། གཟུགས་མེད་པ་རྣམས་ཇི་ལྟར་འཐོབ་ཅེ་ན།

[Block 4190 [VERSE]]
དེ་དང་མི་ལྡན་འདོད་ཆགས་བྲལ། །
སྐྱེ་བ་ལས་ནི་དག་པ་འཐོབ།[^1614] །

[Block 4191]
ས་འོག་མ་ལས་འདོད་ཆགས་དང་བྲལ་བའམ། ས་འོག་མར་སྐྱེ་བ་ལས་ལས༌[^1615]དག་པ་འཐོབ་པོ། །

[Block 4192 [VERSE]]
ཟག་མེད་འདོད་ཆགས་བྲལ་བ་ཡིས། །
དེ་དང་མི་ལྡན་པ་ལས་འཐོབ། །

[Block 4193]
ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 4194]
ཉོན་མོངས་ཅན་ཉམས་སྐྱེ་བ་ཡིས། །གལ་ཏེ་དེ་ལས་འདོད་ཆགས་དང་བྲལ་བ་ཁོ་ན་ལས་ཡོངས་སུ་ཉམས་པ་ལས་འཐོབ་པོ། གལ་ཏེ་ས་འོག་མར་སྐྱེ་བ་ལས་འཐོབ་པོ། །

[Block 4195 [HEADING]]
#### མཇུག་ཐོགས་སུ་སྐྱེ་བ། ^8-1-7-0

[Block 4196]
སྙོམས་པར་འཇུག་པའི་རྫས་གང་ཞིག་ལས་ཅི་ཞིག་སྐྱེ་ཞེ་ན།

[Block 4197 [VERSE]]
ཟག་པ་མེད་པའི་མཇུག་ཐོགས་སུ། །
ལྟག་འོག་གསུམ་པའི་བར་དགེ་བ་སྐྱེའོ། །

[Block 4198]
དགེ་བ་སྨོས་པས་ནི་དག་པ་པ་དང་ཟག་པ་མེད་པ་གཟུང་སྟེ། ཟག་པ་མེད་པའི་སྙོམས་པར་འཇུག་པའི་རྫས་ཀྱི་མཇུག་ཐོགས་སུ་རང་གི་ས་པའི་དག་པ་དང་། ཟག་པ་མེད་པ་དང་། ས་གོང་མ་དང་འོག་མའི་ས་པ་གཉིས་གཉིས་སྐྱེའོ། །

[Block 4199]
ཇི་ལྟར་ཟག་པ་མེད་པའི་མཇུག་ཐོགས་སུ་བཤད་པ་ལྟར། དག་པ་ལས་དེ་བཞིན། རང་གི་ས་པའི་ཉོན་མོངས་ཀྱང་། །དག་པ་པའི༌[^1616]མཇུག་ཐོགས་སུ་ལྷག་པར་རང་གི་ས་པའི་ཉོན་མོངས་པ་ཅན་སྐྱེའོ། །

[Block 4200]
ལྷག་མ་ནི་ཟག་པ་མེད་པ་ལས་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 4201]
ཉོན་མོངས་ཅན་ལས་རང་དག་དང་། །ཉོན་མོངས། ཉོན་མོངས་པ་ཅན་གྱི་མཇུག་ཐོགས་སུ་ནི་རང་གི་ས་པའི་དག་པ་པ་དང་། ཉོན་མོངས་པ་ཅན་དག་སྐྱེའོ། །

[Block 4202]
འོག་མའི་དག་གཅིག་ཀྱང་། ཉོན་མོངས་པས་གཟིར་བའི་ས་འོག་མ་པའི་དག་པ་ལ་ཡང་དགའ་བར་འགྱུར་རོ། །

[Block 4203]
སྙོམས་པར་ཞུགས་པའི་དུས་ལ་ལྟོས༌[^1617]ནས་དག་པ་པ་དང་། ཉོན་མོངས་པ་ཅན་ལས་རང་གི་ས་པའི་ཉོན་མོངས་པ་ཅན་ཁོ་ན་སྐྱེའོ། །

[Block 4204]
འཆི་འཕོའི་དག་ལས་ཉོན་མོངས་ཀུན། །འཆི་འཕོ་བའི་ཚེ༌[^1618]སྐྱེ་བས་ཐོབ་པའི་དག་པ་པའི་མཇུག་ཐོགས་སུ་ས་ཐམས་ཅད་པའི་ཉོན་མོངས་པ་ཅན་སྐྱེའོ། །

[Block 4205]
ཉོན་མོངས་ཅན་ལས་གོང་མ་མིན། །འཆི་འཕོ་བའི་ཚེ་ཉོན་མོངས་པ་ཅན་གྱི་བསམ་གཏན་དང་གཟུགས་མེད་པའི་མཇུག་ཐོགས་སུ་རང་གི་ས་པ་དང་ས་འོག་མའི་ཉོན་མོངས་པ་ཅན་སྐྱེའི་ས་གོང་མ་པ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
