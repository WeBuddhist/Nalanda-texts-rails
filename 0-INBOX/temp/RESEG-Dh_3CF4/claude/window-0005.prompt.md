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
[Block 176]
གྲགས་པ་ནི་སྙན་པར་གྲགས་པའོ། །

[Block 177]
ཁྱད་པར་ནི་ཁྱད་པར་དུ་འཕགས་པ་སྟེ་བྱུང་བར་གྱུར་ཏེ་ཞེས་བྱ་བ་ནི་བྱུང་ངོ༌[^92]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 178]
བྱང་ཆུབ་སེམས་དཔའ་དེའི་བློ་ནི་སེམས་སོ། །

[Block 179]
ཆོས་ལ་གོམས་པ་ཞེས་བྱ་བ་ལ་ཆོས་ནི་རྣམ་པ་གཉིས་ཏེ། ཁྱིམ་ན་གནས་པའི་ཆོས་དང་། མངོན་པར་འབྱུང་བའི་ཆོས་སོ། །

[Block 180]
ཁྱིམ་ན་གནས་པའི་ཆོས་ལ༌[^93]གོམས་ཤིང་བསྒོམས་པར་གྱུར་ཀྱང་དེ་རྙེད་པ་ལ་སོགས་པ་དེ་ལ་མངོན་པར་དགའ་བར་མ་གྱུར་ཏེ། རབ་ཏུ་བྱུང་བ་དང་འདྲིས་པར་བྱས་པ་ཞེས་བྱ་བ་རབ་ཏུ་བྱུང་བ་ལ་འདྲིས་པར་བྱས་པས་ནི། བྱང་ཆུབ་སེམས་དཔའ་དེ་རབ་ཏུ་བྱུང་བ་ལ་དགའ་ཞིང་། དེ་ལ་དགའ་བར་མ་གྱུར་པ་ནི།

[Block 181 [VERSE]]
མངོན་པར་དགའ་བ་མེད་པ་ཡིན་ནོ། །
སྔོན་གྱི་སྤྱོད་པས་དེ༌[^94]བློ་ཡོངས་སུ་དག །

[Block 182]
[^95]ཅེས་བྱ་བ་ནི་སྐྱེ་བ་གཞན་དག༌[^96]ལ་དེས་ཡོངས་སུ་དག་པར་བྱས་པ་སྟེ། གང་གིས༌[^97]བློ་ཡོངས་སུ་དག་པ་དེ་ནི་བློ་ཡོངས་སུ་དག་པའོ། །

[Block 183]
འདོད་པར་བྱ་བ་ཡིན་པས་འདོད་པ་རྣམས་སོ། །

[Block 184]
མངོན་པ་ནི་རྟོགས་པའོ། །

[Block 185]
སྐྱོན་མང་ཞེས་བྱ་བ་ནི་བསགས་པ་དང་། བསྲུངས་པ༌[^98]དང་། ཉེ་བར་སྤྱོད་པའི་ཀུན་ནས་ཉོན་མོངས་པ་ལ་སོགས་པའི་མངོན་པའི་ཉེས་པས་སོ། །

[Block 186]
ཁྱིམ་ན་གནས་པ་ནད་བཞིན་ཡོངས༌[^99]སྤངས་ནས་ཞེས་བྱ་བ་ནི་ནད་ནི་མི་བདེ་བའོ། །

[Block 187]
ཡོངས་སུ་སྤངས་པ་ནི་ཡོངས་སུ་དོར་བའོ། །

[Block 188]
ནགས་ཚལ་གནས་ཤིང་ཞེས་བྱ་བ་ནི་ནགས་ཀྱི་ཕྱོགས་གཅིག་གོ། །

[Block 189]
བརྒྱན་པར་གྱུར་ཞེས་བྱ་བ་ནི་སྡུད༌[^100]པའོ། །

[Block 190 [VERSE]]
དེ༌[^101]ནི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའོ། །
དེར་ནི་ཞེས་བྱ་བ་ནི་ནགས་ཀྱི་གནས་དེར་རོ། །
ཆགས་མེད་ཅེས་བྱ་བ་ནི་ཞེན་པ་མེད་པ་སྟེ།
ཆགས་པ་མེད་པར་གྱུར་པའི་ཕྱིར་ཆགས་པ་མེད་པའོ། །

[Block 191]
དེ་ཡིས་ཞེས་བྱ་བ་ནི་ཆགས་པ་མེད་པ་དེ་ཡིས་ཞེས་འདྲེན་པ་ཡིན་ནོ། །ཤེས་རབ་ཡོངས་སུ་སྦྱངས་པ་ནི་ཤེས་རབ་དག་པའོ། །

[Block 192]
ཞི་བ་ནི་ཉེ་བར་ཞི་བའོ། །

[Block 193]
མིའི་འཇིག་རྟེན་ཞེས་བྱ་བ་ནི་མིའི་འཇིག་རྟེན་དུའོ། །

[Block 194]
དམ་པ་ནི་གཞུང་ལུགས༌[^102]སྟོན་པར་བྱེད་པའི་སྐྱེས་བུ་དམ་པ་དེ་དག་གི་རྗེས་སུ་སྤྱོད་པ་སྟེ། རྗེས་སུ་འཇུག་ཅིང་དབང་པོ་སྡོམ་པའོ། །

[Block 195]
བྲལ་བ་ནི་མེད་པར་གྱུར་པའོ། །

[Block 196]
ངན་པ་ནི་འཇིག་རྟེན་ངན་པ་བཞིན་དུ་སྤྱོད་པ་སྟེ། ངན་པ་བྱེད་པ་ཡིན་པས་ངན་པ་སྤྱོད་པའོ། །

[Block 197]
ཆགས་པ་ནི་ཞེན་པའོ། །

[Block 198]
བཟློག་པ་ནི་བསལ༌[^103]བའོ། །

[Block 199]
བྱམས་པའི་རང་བཞིན་ཞེས་བྱ་བ་ནི་བྱམས་པའི་ངོ་བོ་ཉིད་ཀྱིས་སོ། །

[Block 200]
རབ་ཞི་ཞེས་བྱ་བ་ནི་ཉེ་བར་ཞི་བ་ཉིད་དོ། །

[Block 201]
དེའི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་འོ། །

[Block 202]
རྣམ་པར་བརླན་པ་ཞེས་བྱ་བ་ནི་རྣམ་པར་བརླན་ཅིང་འཇོག༌[^104]པའོ། །

[Block 203]
སེམས་མཐུན་ཞིང་ཞེས་བྱ་བ་ནི་མི་མཐུན་པ་མེད་པའོ། །

[Block 204]
ཕན་ཚུན་ནི་གཅིག་ལ་གཅིག་གོ། །

[Block 205]
གནོད་པ༌[^105]མེད་པ་ཞེས་བྱ་བ་ནི་ལྡོག་པ་སྟེ། དེ་གང་ལས་ལྡོག་པ་ཡིན་ཞེ་ན། གནོད་པའི་དངོས་པོ་སྟེ་ཀུན་ནས་གནོད་པའི་སེམས་ལས་སོ། །

[Block 206]
དཀའ་ཐུབ་ཅན༌[^106]ཞེས་བྱ་བ་ནི་དྲང་སྲོང་བཞིན་ནོ།[^107] །གཅན་གཟན༌[^108]ཁྲོ་བོ་ནི་སེང་གེ་དང་། སྟག་དང་། དོམ་ལ་སོགས་པའོ། །

[Block 207]
སྤྱོད་ཅེས་བྱ་བ་ནི་སྤྱོད་པ་དང་ལྡན་པའོ། །

[Block 208]
སྤྱོད་པ་དག་པ་ནི་གཞུང་ལུགས་དག་པའོ། །

[Block 209]
ཡང་ན་སྤྱོད་པ་དག་པ་ནི་བདུན་ལས་ལྡོག་པའོ། །

[Block 210]
དབང་པོ་དུལ་བ་ཞེས་བྱ་བ་ནི་དབང་པོ་དམ༌[^109]པར་བསྡམས་པའོ། །

[Block 211]
ཆོ་ག་ཤེས་པ་ནི་ངན་ངོན་ཙམ་གྱིས༌[^110]ཆོ་ག་ཤེས་པའོ། །

[Block 212]
བཟའ་བ་དང་བགོ་བ་ལ་སོགས་པའི་རྒྱུས་སོ། །

[Block 213]
སྙིང་རྗེའི་ཡོན་ཏན་ཞེས་བྱ་བ་ནི་གོམས་པས་སོ། །

[Block 214]
འཇིག་རྟེན་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་ནོ། །

[Block 215]
སྐྱེ་བོ་ནི་དེ་ན་གནས་པའི་སྐྱེ་བོ་ལ་བརྗོད་དོ། །
--- END BLOCKS ---
