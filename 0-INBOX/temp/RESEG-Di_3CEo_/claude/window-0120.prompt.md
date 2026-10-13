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

[Block 4206]
དག་པ་པ་ཐམས་ཅད་ལས་ཟག་པ་མེད་པའི་སྙོམས་པར་འཇུག་པའི་རྫས་སྐྱེ་བ་ཡང་མ་ཡིན་ནོ། །

[Block 4207 [HEADING]]
#### ཉམས་པའི་ཆ་མཐུན་སོགས་རྣམ་བཞི། ^8-1-8-0

[Block 4208]
འདི་ལྟར། དག་པ་ཉམས་པའི་ཆ་མཐུན་སོགས། །རྣམ་བཞི། [^1619]དེ་ཡང་། དེ༌[^1620]ནི་གོ་རིམས་བཞིན།

[Block 4209 [VERSE]]
ཉོན་མོངས་སྐྱེ་དང་རང་ས་དང་།
གོང་དང་ཟག་མེད་རྗེས་མཐུན་པའོ། །

[Block 4210]
ཉམས་པའི་ཆ་དང་མཐུན་པ་ནི་ཉོན་མོངས་པ་སྐྱེ་བ་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 4211]
གནས་པའི་ཆ་དང་མཐུན་པ་ནི་རང་གི་ས་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 4212]
ཁྱད་པར་གྱི་ཆ་དང་མཐུན་པ་ནི་ས་གོང་མ་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 4213]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ནི་ཟག་པ་མེད་པའི་རྗེས་སུ་མཐུན་པ་སྟེ། ཟག་པ་མེད་པ་ནི་དེ་ལས་སྐྱེའོ། །

[Block 4214]
ཡང་བཞི་པོ་དེ་དག་ལས་གང་གི་མཇུག་ཐོགས་སུ་དུ་ཞིག་སྐྱེ་ཞེ་ན།

[Block 4215 [VERSE]]
ཉམས་ཆ་མཐུན་སོགས་མཇུག་ཐོགས་སུ། །
གཉིས་དང་གསུམ་དང་གསུམ་དང་གཅིག །

[Block 4216]
ཉམས་པའི་ཆ་དང་མཐུན་པའི་མཇུག་ཐོགས་སུ་གཉིས་སྐྱེ་སྟེ། ཉམས་པ་དང་། གནས་པའི་ཆ་དང་མཐུན་པ་དག་གོ། །

[Block 4217]
གནས་པའི་ཆ་དང་མཐུན་པ༌[^1621]ནི་གསུམ་སྟེ། ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་མི༌[^1622]གཏོགས་སོ། །

[Block 4218]
ཁྱད་པར་གྱི་ཆ་དང་མཐུན་པའི་ནི་གསུམ་སྟེ། ཉམས་པའི་ཆ་དང་མཐུན་པ་མ་གཏོགས་སོ། །

[Block 4219]
ངེས་པར་འབྱེད་པའི་ནི༌[^1623]གཅིག་སྟེ། དེ་གཅིག་པུ་སྐྱེའོ། །

[Block 4220 [HEADING]]
#### ཐོད་རྒལ་གྱི་སྙོམས་འཇུག། ^8-1-9-0

[Block 4221]
ཐོད་རྒལ་གྱི་སྙོམས་པར་འཇུག་པ་ཇི་ལྟ་བར་སྐྱེད་ཅེ་ན།

[Block 4222 [VERSE]]
ས་བརྒྱད་རྣམ་གཉིས་འབྲེལ་བ་དང་། །
གཅིག་རྒལ་སོང་ཞིང་འོངས་ནས་ནི། །
རིས་མི་མཐུན་པ་གསུམ་པར་འགྲོ། །
ཐོད་རྒལ་གྱི་ནི་སྙོམས་འཇུག་ཡིན། །

[Block 4223]
ས་བརྒྱད་ནི་བསམ་གཏན་དང་གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པ་དག་གོ། །

[Block 4224]
རྣམ་གཉིས་ནི་ཟག་པ་དང་བཅས་པ་དང་། ཟག་པ་མེད་པའོ། །

[Block 4225]
འབྲེལ་པ་དང་། ཞེས་པ་ནི་གོ་རིམས་བཞིན་དུའོ། །

[Block 4226]
གཅིག་རྒལ་ནི་རེ་རེ་རྒལ་ནས་སོ། །

[Block 4227]
སོང་ཞིང་ཞེས་བྱ་བ་ནི་ལུགས་དང་མཐུན་པར་འགྱུར་རོ། །

[Block 4228]
འོངས་ནས་ཞེས་བྱ་བ་ནི་ལུགས་དང་མི་མཐུན་པར་འགྱུར་རོ། །

[Block 4229]
ཟག་པ་དང་བཅས་པའི་ས་བརྒྱད་དང་། ཟག་པ་མེད་པའི་ས༌[^1624]བདུན་ལུགས་དང་མཐུན་པ་དང་ལུགས་དང་མི་མཐུན་པའི་སྒོ་ནས་བྱང་བར་བྱས་ནས་ཕྱིས་ཟག་པ་དང་བཅས་པའི་བསམ་གཏན་དང་པོ་ནས་ཟག་པ་དང་བཅས་པ་གསུམ་པ་ལ་སྙོམས་པར་འཇུག་ཅིང་། དེ་ནས་ནི་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ། དེ་ནས་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ལ་སྙོམས་པར་འཇུག་གོ། །

[Block 4230]
དེ་བཞིན་དུ་ལུགས་དང་མི་མཐུན་པ་ཡང་བྱང་བར་བྱས་ནས་ཟག་པ་མེད་པ༌[^1625]རྣམས་ཀྱང་རེ་རེ་རྒལ་ཞིང་ལུགས་དང་མཐུན་པ་དང་ལུགས་དང་མི་མཐུན་པར་སྙོམས་པར་འཇུག་པའི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 4231]
གང་གི་ཚེ་ཟག་པ་དང་བཅས་པ་དང་པོ་ནས་ཟག་པ་མེད་པའི་བསམ་གཏན་གསུམ་པ་ལ་སྙོམས་པར་འཇུག་ཅིང་། དེ་བཞིན་དུ་ལུགས་དང་མི་མཐུན་པར་ཡང་སྙོམས་པར་འཇུག་པ་དེའི་ཚེ་རིགས་མི་མཐུན་པའི་རྫས་གསུམ་པར་འགྲོ་བའི་ཕྱིར་མངོན་པར་གྲུབ་པ་ཡིན་ནོ། །

[Block 4232 [HEADING]]
#### རྟེན། ^8-1-10-0

[Block 4233]
རྟེན་གང་གིས༌[^1626]བསམ་གཏན་དང་གཟུགས་མེད་པ་དུ་ཞིག་མངོན་སུམ་དུ་བྱེད་ཅེ་ན། བསམ་གཏན་གཟུགས་མེད་རང་དང་ནི། །འོག་སའི་རྟེན་ཅན། སྲིད་པའི་རྩེ་མོ་ནི་སྲིད་པའི་རྩེ་མོར་ཡང་མངོན་སུམ་དུ་བྱེད་ལ། འོག་མ་འདོད་པའི་ཁམས་ཀྱི་བར་དུ་ཡང་ངོ་། །དེ་བཞིན་དུ་གཞན་ཡང་ངོ་། །ཅིའི་ཕྱིར་གོང་དུ་སྐྱེས་པ་སྙོམས་པར་འཇུག་པ་འོག་མ༌[^1627]མངོན་དུ་མི་བྱེད་ཅེ་ན། འདི་ལྟར་དེ་ལ། འོག་དགོས་མེད། སྤྱིར་བསྟན་པར་བྱས་ནས་དམིགས་ཀྱིས་སྟོན་པར་བྱེད་དེ།

[Block 4234 [VERSE]]
སྲིད་རྩེར་འཕགས་པའི་ཅི་ཡང་མེད། །
མངོན་སུམ་བྱས་ནས་ཟག་པ་ཟད། །

[Block 4235]
སྲིད་པའི་རྩེ་མོར་སྐྱེས་པ་ནི་ཟག་པ་མེད་པའི་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་མངོན་སུམ་དུ་བྱས་ནས་ཟག་པ་ཟད་པར་འགྱུར་རོ། །

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
--- END BLOCKS ---
