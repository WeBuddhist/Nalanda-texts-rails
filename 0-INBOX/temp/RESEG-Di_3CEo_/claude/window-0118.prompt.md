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
[Block 4131]
དེ་ལྟར་སྙོམས་འཇུག་དངོས་གཞིའི༌[^1596]རྫས། །རྣམ་པ་བརྒྱད། བསམ་གཏན་བཞི་དང་། གཟུགས་མེད་པ་བཞིའོ། །

[Block 4132]
དེ་དག་ལས།

[Block 4133]
བདུན༌[^1597]རྣམ་པ་གསུམ། སྲིད་པའི་རྩེ་མོ་ལས་གཞན་པ་བདུན་ནི་རྣམ་པ་གསུམ་ཡིན་ཏེ། རོ་མྱང་ལྡན་དང་དག་པ་དང་། །ཟག་མེད། རོ་མྱོང༌[^1598]བ་དང་མཚུངས་པར་ལྡན་པ་དང་། དག་པ་བ་དང་། ཟག་པ་མེད་པ་རྣམས་སོ། །

[Block 4134]
བརྒྱད་པ་རྣམ་པ་གཉིས། ཟག་པ་མེད་པ་མ་གཏོགས་སོ། །

[Block 4135]
དེ་ལ།

[Block 4136 [VERSE]]
རོ་མྱང་མཚུངས་ལྡན་སྲེད་བཅས་སོ། །
རོ་མྱང་བ་ནི་སྲེད་པ་ཡིན་ནོ། །
འཇིག་རྟེན་པ་ཡི་དགེ་བ་ནི། །

[Block 4137]
དག་པ། འཇིག་རྟེན་པའི་དགེ་བ་སྙོམས་པར་འཇུག་པའི་རྫས་ནི་དག་པ་པ་ཞེས་བྱ་སྟེ། མ་ཆགས་པ་ལ་སོགས་པ་ཆོས་དཀར་པོ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་རོ། །

[Block 4138]
རོ་མྱང་བ༌[^1599]དང་མཚུངས་པར་ལྡན་པ་དེས་ཅི་ཞིག་རོ་མྱོང༌[^1600]བར་བྱེད་ཅེ་ན། དེ་ནི་ངེས་མྱང་བྱ། སྙོམས་པར་འཇུག་པའི་རྫས་དག་པ་པ་འདས་མ་ཐག་པ་དེ་ནི་དེས་རོ་མྱོང༌[^1601]བར་བྱེད་དོ། །

[Block 4139]
ཟག༌[^1602]མེད་འཇིག་རྟེན་འདས་པ་པོ།[^1603] །འཇིག་རྟེན་ལས་འདས་པའི་སྙོམས་པར་འཇུག་པའི་རྫས་གང་ཡིན་པ་དེ་ནི་ཟག་པ་མེད་པ་ཡིན་ནོ། །

[Block 4140 [HEADING]]
#### བསམ་གཏན་གྱི་ཡན་ལག། ^8-1-4-0

[Block 4141]
སྙོམས་པར་འཇུག་པའི་རྫས་དེ་དག་ལས༌[^1604]བསམ་གཏན་རྣམས་ཁོ་ན་ཡན་ལག་དང་ལྡན་པ་ཡིན་གྱི་གཟུགས་མེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 4142]
དེ་ལ།

[Block 4143 [VERSE]]
དང་པོ་ལ་ལྔ་རྟོག་དཔྱོད་དང་། །
དགའ་དང་བདེ་དང་ཏིང་འཛིན་རྣམས། །

[Block 4144]
དེ་དག་ནི་བསམ་གཏན་དང་པོའི་ཡན་ལག་ལྔ་ཡིན་ནོ། །

[Block 4145 [VERSE]]
གཉིས་པ་ལ་ནི་ཡན་ལག་བཞི། །
རབ་དང་དང་ནི་དགའ་ལ་སོགས། །

[Block 4146]
རབ་ཏུ་དང་བ་དང་། དགའ་བ་དང་། བདེ་བ་དང་། སེམས་རྩེ་གཅིག་པ་ཉིད་དོ། །

[Block 4147]
གཉིས་པ་ནི་ཡན་ལག་བཞི་དང་ལྡན་ནོ། །

[Block 4148 [VERSE]]
གསུམ་པ་ལ་ལྔ་བཏང་སྙོམས་དང་། །
དྲན་དང་ཤེས་བཞིན་བདེ་དང་གནས། །

[Block 4149]
གསུམ་པ་ནི་བཏང་སྙོམས་དང་། དྲན་པ་དང་། ཤེས་བཞིན་དང་། བདེ་བ་དང་། ཏིང་ངེ་འཛིན་དེ༌[^1605]ཡན་ལག་ལྔ་དང་ལྡན་ནོ། །

[Block 4150 [VERSE]]
མཐའ་ན་བཞི་དྲན་བཏང་སྙོམས་དང་། །
བདེ་མིན་སྡུག་མིན་ཏིང་འཛིན་རྣམས། །

[Block 4151]
བཞི་པ་ནི་བདེ་བ་ཡང་མ་ཡིན། སྡུག་བསྔལ་བ་ཡང་མ་ཡིན་པའི་ཚོར་བ་དང་།

[Block 4152]
བཏང་སྙོམས་ཡོངས་སུ་དག་པ་དང་། །དྲན་པ་ཡོངས་སུ་དག་པ་དང་། །

[Block 4153]
ཏིང་ངེ་འཛིན་ཏེ༌[^1606]ཡན་ལག་བཞི་དང་ལྡན་ནོ། །

[Block 4154]
དེ་དག་ནི། བཞི་པོ་ལ་མིང་གི་སྒོ་ནས་ཡན་ལག་བཅོ་བརྒྱད་ཡིན་ནོ། །

[Block 4155]
རྫས་སུ་བཅུ་གཅིག །དེ་ལ་བསམ་གཏན་དང་པོ་བའི་ལྔ་དང་།

[Block 4156]
གཉིས་པ་ན་ནི་རབ་ཏུ་དང་བ་ལྷག་གོ། །

[Block 4157]
གསུམ་པ་ན་ནི་བཏང་སྙོམས་དང་། དྲན་པ་དང་། ཤེས་བཞིན་དང་། བདེ་བ་རྣམས་སོ། །

[Block 4158]
བཞི་པ་ན་ནི་བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་བ་ཡང་མ་ཡིན་པའི་ཕྱིར༌[^1607]ཚོར་བའོ། །

[Block 4159]
ཅིའི་ཕྱིར་བསམ་གཏན་གསུམ་པ་ན་ཡོད་པའི་བདེ་བ་རྫས་གཞན་དུ་བརྗོད་ཅེ་ན། འདི་ལྟར་དེའི་བདེ་བ་ནི་ཚོར་བ་ཡིན་ལ། བསམ་གཏན་དང་པོ་ན། ཤིན་ཏུ་སྦྱངས་པ་བདེ་བ་ཡིན། །བསམ་གཏན་དང་པོ་དང་གཉིས་པ་དག་ན། ཤིན་ཏུ་སྦྱངས་པ་ལ་བདེ་བར་གསུངས་པའི་ཕྱིར་རོ། །

[Block 4160]
ནང་རབ་ཏུ་དང་བ་གང་ཞེ་ན། རབ་ཏུ་དང་བ་དད་པ་ཡིན། །དེ་ནི་བསམ་གཏན་གཉིས་པ་ཐོབ་པའི་ཕྱིར་མཉམ་པར་གཞག་པའི་ས་ལས་ངེས་པར་འབྱུང་བར་ཡིད་ཆེས་པར་བྱས་ཏེ། དེ་ནི་འདིར་ནང་རབ་ཏུ་དང་བ་ཞེས་བྱའོ། །

[Block 4161]
དགའ་བ་ནི་ཡིད་བདེ་བ་ཡིན་ནོ་ཞེས་གང་བཤད་པ་འདི༌[^1608]ལྟར་ཁོང་དུ་ཆུད། གཞན་ཇི་ལྟར་འགྱུར། དགའ་བ་ནི་སེམས་ལས་བྱུང་བའི་ཆོས་གཞན་ཁོ་ན་ཡིན་ལ། ཡིད་བདེ་བ་ནི་བསམ་གཏན་གསུམ་ཆར་གྱི་བདེ་བ༌[^1609]ཡིན་ནོ། །

[Block 4162]
བསམ་གཏན་དག་གི་བདེ་བ༌[^1610]ནི་ཡིད་བདེ་བ་ཡིན་པར་མི་རུང་བ་ཉིད་ཀྱིས། ལུང་རྣམ་གཉིས་ཕྱིར་དགའ་ཡིད་བདེ། །བཅོམ་ལྡན་འདས་ཀྱིས་རྣམ་པར་འགྱུར་བའི་མདོ་ལས་བསམ་གཏན་གསུམ་པ་བཀའ་སྩལ་ནས་འདིར༌[^1611]འདིའི་ཡིད་བདེ་བའི་དབང་པོ་སྐྱེས་པ་མ་ལུས་པར་འགག་པར་འགྱུར་རོ། །ཞེས་བཀའ་སྩལ་པ། བསམ་གཏན་བཞི་པ་ན་ནི་བདེ་བའི་དབང་པོ་འགག་པར་བགྱུར་རོ་ཞེས་བཀའ་སྩལ་ཏོ། །

[Block 4163]
ཡང་བདེ་བ་ཡང་སྤངས་ཏེ་སྔ་ནས་སྡུག་བསྔལ་ཡང་སྤངས་ཤིང་ཡིད་བདེ་བ་དང་ཡིད་མི་བདེ་བ༌[^1612]ཡང་ནུབ་ཅེས་ཀྱང་གསུངས་པས་དེའི་ཕྱིར་བསམ་གཏན་གསུམ་པ་ན་ཡིད་བདེ་བའི་དབང་པོ་མེད་དོ། །

[Block 4164]
དེ་ལྟ་བས་ན་དགའ་བ་ཁོ་ན་ཡིད་བདེ་བ་ཡིན་གྱི་བདེ་བ་ནི་མ་ཡིན་ནོ། །

[Block 4165]
ཅི་ཉོན་མོངས་པ་ཅན་གྱི་བསམ་གཏན་དག་ན་ཡང་ཇི་སྐད་དུ་བཤད་པའི་ཡན་ལག་དེ་དག་ཡོད་དམ་ཞེ་ན། མེད་དོ། །

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
--- END BLOCKS ---
