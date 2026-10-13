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
[Block 4236 [HEADING]]
#### དམིགས་པ། ^8-1-11-0

[Block 4237]
བསམ་གཏན་དང་། གཟུགས་མེད་པའི་དམིགས་པ་ཅི་ཞེ་ན། སྲེད་བཅས་རང་གི་སྲིད་ལ༌[^1628]དམིགས། །ཟག་པ་དང་བཅས་པ་རང་གི་ས་པ་ལ་དམིགས་སོ། །

[Block 4238]
བསམ་གཏན་དགེ་ཡུལ་ཡོད་དགུ་ཡིན།[^1629] །དགེ་བའི་བསམ་གཏན་དག་པ་པ་དང་ཟག་པ་མེད་པའི༌[^1630]དམིགས་པ་ནི་ཐམས་ཅད་ཡིན་ནོ། །

[Block 4239 [VERSE]]
གཟུགས་མེད་དངོས་གཞི་དགེ་རྣམས་ཀྱི། །
སྤྱོད་ཡུལ་ཟག་བཅས་འོག་མ་མིན། །

[Block 4240]
གཟུགས་མེད་པའི་དངོས་གཞི་དགེ་བ་རྣམས་ཀྱི་དམིགས་པ་ནི་ས་འོག་མའི་ཟག་པ་དང་བཅས་པ་མ་ཡིན་ཏེ། རང་གི་ས་དང་གོང་མ་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 4241 [HEADING]]
#### ཉོན་མོངས་སྤོང་བ། ^8-1-12-0

[Block 4242]
བསམ་གཏན་དང་། གཟུགས་མེད་པ་རྣམ་པ་གསུམ་པོ་འདི་དག་ལས། །

[Block 4243]
ཟག་པ་མེད་པས་ཉོན་མོངས་རྣམས། །སྤོང་ངོ་། །དག་པ་པས་ཀྱང་མི་སྤོང་ན་ཉོན་མོངས་པ་ཅན་གྱིས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཏེ། ཉེར་བསྡོགས་དག་པས་ཀྱང་། གཟུགས་དང་གཟུགས་མེད་པའི་ཉེར་བསྡོགས་དག་པ་པས་ཀྱང་ཉོན་མོངས་པ་རྣམས་སྤང༌[^1631]སྟེ། ས་འོག་མའི་གཉེན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4244 [HEADING]]
#### ཉེར་བསྡོགས། ^8-1-13-0

[Block 4245]
ཉེར་བསྡོགས་དུ་ཞིག་ཡོད་ཅེ་ན། དེ་དག་ལ་ནི་ཉེར་བསྡོགས་བརྒྱད། །རེ་རེ་ལ་གང་གིས་དེ་ལ་འཇུག་པ་རེ་རེ་ཡོད་དོ། །

[Block 4246]
ཅི་དེ་དག་ཀྱང་རྣམ་པ་གསུམ་ཡིན་ལ། དེ་དག་ལ་ཚོར་བ་དང་། [^1632]ཡང་དེ་དང་འདྲ་བར་ཡོད་དམ་ཞེ་ན། མ་ཡིན་ཏེ། དག་པ་བདེ་མིན་སྡུག་བསྔལ་མིན། །དེ་དག་ནི་དག་པ་པ་ཡིན་ལ་བཏང་སྙོམས་ཀྱི་དབང་པོ་དང་མཚུངས་པར་ལྡན་པ་དག་ཀྱང་ཡིན་ཏེ། འབད་དེ༌[^1633]དྲང་བར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4247]
དང་པོ་འཕགས་པའང་། ཉེར་བསྡོགས་ཀྱི་དང་པོ་མི་ལྕོགས་པ་མེད་པ་སྟེ། དེ་ནི་དག་པ་པ་ཡང་ཡིན་ལ་ཟག་པ་མེད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 4248]
ཁ་ཅིག་གསུམ། རོ་མྱང་བ་དང་མཚུངས་པར་ལྡན་པ་ཡང་ཞེས་ཟེར་རོ། །ཅི་འདི་དོན་གཅིག༌[^1634]གམ་ཐ་དད་ཅེ་ན། ཐ་དད་དེ། ཉེར་བསྡོགས་ནི་འདོད་ཆགས་དང་བྲལ་བའི་ལམ་ཡིན་ལ།

[Block 4249 [HEADING]]
#### བསམ་གཏན་ཁྱད་པར་ཅན། ^8-1-14-0

[Block 4250]
རྟོག་མེད་བསམ་གཏན་ཁྱད་པར་ཅན། །བསམ་གཏན་དང་པོ་ཁོ་ན་རྟོག་པ་དང་མཚུངས་པར་མི་ལྡན་པ་ནི་བསམ་གཏན་ཁྱད་པར་ཅན་ཡིན་ཏེ། བསམ་གཏན་གྱི་ཁྱད་པར་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4251 [VERSE]]
རྣམ་གསུམ་བདེ་མིན་སྡུག་བསྔལ་མིན། །
དེ་ནི་ཚངས་ཆེན་འབྲས་བུ་ཅན། །

[Block 4252]
བསམ་གཏན་ཁྱད་པར་ཅན་དེ་བསྒོམས་ན་ཚངས་པ་ཆེན་པོར་འགྱུར་རོ། །

[Block 4253 [HEADING]]
### ཏིང་ངེ་འཛིན། ^8-2-0

[Block 4254 [HEADING]]
#### རྟོག་དཔྱོད་བཅས་པ་སོགས་ཏིང་ངེ་འཛིན་གསུམ། ^8-2-1-0

[Block 4255]
ཡང་ཏིང་ངེ་འཛིན་ཐམས་ཅད་མདོར་བསྡུས་ནས་མདོ་ལས་གསུམ་དུ་གསུངས༌[^1635]ཏེ། དེ་ལ་རེ་ཞིག་བསམ་གཏན་ཁྱད་པར་ཅན་ནི་རྟོག་པ་མེད་ལ༌[^1636]དཔྱོད་པ་ཙམ་གྱི་ཏིང་ངེ་འཛིན་ཏོ་ཞེས་ཤེས་པར་བྱས་ཟིན་ཏོ། །

[Block 4256]
དེ།

[Block 4257 [VERSE]]
མན་ཆད་རྟོག་དཔྱོད་བཅས་པ་ཡིས།[^1637] །
ཏིང་འཛིན་བསམ་གཏན་ཁྱད་པར་ཅན། །

[Block 4258]
དེ་མན་ཆད་ནི་བསམ་གཏན་དང་པོ་དང་མི་ལྕོགས་པ་མེད་པའོ། །

[Block 4259]
ཡན་ཆད་གཉིས་ཀ་མེད། བསམ་གཏན་ཁྱད་པར་ཅན༌[^1638]ཡན་ཆད་རྟོག་པ་དང་དཔྱོད་པ་མེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4260 [HEADING]]
#### མཚན་མེད་སྟོང་ཉིད་སྨོན་མེད་ཀྱི་ཏིང་ངེ་འཛིན། ^8-2-2-0

[Block 4261]
ཡང་ཏིང་ངེ་འཛིན་གསུམ་གསུངས་ཏེ། དེ་ལ། མཚན་མེད་ཞི་བའི་རྣམ་པ་ཅན། །འགོག་པའི་བདེན་པའི་རྣམ་པ་དག་དང་མཚུངས་པར་ལྡན་པའི་ཏིང་ངེ་འཛིན་ནི་མཚན་མ་མེད་པའོ། །

[Block 4262]
སྟོང་ཉིད་བདག་མེད་སྟོང་ཉིད་དུ། །འཇུག་པའོ། །

[Block 4263]
སྟོང་པ་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་ནི་རྣམ་པ་གཉིས་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 4264]
སྨོན་པ་མེད་པ་ནི། དེ་ལས་གཞན་བདེན་རྣམ་པ་དང་། །སྨོན་པ་མེད་པའི་ཏིང་ངེ་འཛིན་ནི་རྣམ་པ་བཅུ་དང་ལྡན་པར་འཇུག་གོ། །

[Block 4265]
ཏིང་ངེ་འཛིན་གསུམ་པོ་འདི་དག་ནི་རྣམ་པ་གཉིས་ཏེ། དག་དང་དྲི་མ་མེད། དག་པ་པ་དང་། དྲི་མ་མེད་པ་དག་གོ། །

[Block 4266]
དེ་དག །དྲི་མེད་རྣམ་ཐར་སྒོ་གསུམ་མོ། །

[Block 4267]
གསུམ་པོ་དེ་དག་ལས།

[Block 4268]
ཟག་པ་མེད་པ་ནི་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་ཡིན་ནོ། །

[Block 4269 [HEADING]]
#### སྟོང་ཉིད་སྟོང་ཉིད་སོགས་ཏིང་ངེ་འཛིན་གསུམ། ^8-2-3-0

[Block 4270]
ཡང་། སྟོང་ཉིད་སྟོང་ཉིད་ཅེས་ལ་སོགས། །གཞན་ཡང་ཏིང་ངེ་འཛིན་གསུམ་མོ་ཞེས་པའོ། །

[Block 4271]
དེ་དག་ལས།

[Block 4272 [VERSE]]
གཉིས་ནི་སྟོང་དང་མི་རྟག་པར། །
མི་སློབ་པའི་ལ་དམིགས་པ་ཡིན། །

[Block 4273]
སྟོང་པ་ཉིད་སྟོང་པ་ཉིད་ནི་མི་སློབ་པའི་སྟོང་པ་ཉིད་ཀྱི་ཏིང་ངེ་འཛིན་ལ་སྟོང་པ༌[^1639]ཉིད་ཀྱི་རྣམ་པས་དམིགས་སོ། །

[Block 4274]
སྨོན་པ་མེད་པ་སྨོན་པ་མེད་པ་ཡང་མི་སློབ་པའི་སྨོན་པ་མེད་པ་ལ་མི་རྟག་པའི་རྣམ་པས་དམིགས་སོ། །

[Block 4275 [VERSE]]
མཚན་མ་མེད་པ་མཚན་མེད་ནི། །
ཞི་བར་མ་བརྟགས་ཟད་པ་ལ། །
--- END BLOCKS ---
