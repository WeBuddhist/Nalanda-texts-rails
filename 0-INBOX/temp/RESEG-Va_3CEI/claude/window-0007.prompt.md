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
[Block 246 [HEADING]]
###### འཕགས་པའི་ཡོན་ཏན་བསམ་གྱིས་མི་ཁྱབ་པ་བསྟན་པ། ^4-1-5-5-3-0

[Block 247]
མདོ་ལས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་སྟོང་ཕྲག་བརྒྱད་ཅུ་ཞེས་སྨོས་པ་ལྔ་པ་སྟེ། །འཕགས་པའི་ཡོན་ཏན་བསམ་གྱིས་མི་ཁྱབ་པ་བསྟན་པ་དེ་ཡང་རྣམ་པ་གསུམ་དུ་དབྱེའོ། །

[Block 248 [VERSE]]
དེའི་གྲངས་དང་དེའི་ཡོན་ཏན་དང་། །
དེ་དག་གི་མཚན་སོ་སོར་དབྱེ་བའོ། །

[Block 249 [HEADING]]
###### **དེའི་གྲངས།** ^4-1-5-5-3-1-0

[Block 250]
དེ་ལ༌[^319]བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཞེས་སྨོས་པ་དོན་རྣམ་པ་གཉིས་ཏེ། ཡེ་ཤེས་ཆེན་པོ་གཙོར་བྱས་པས་བདག་གི༌[^320]དོན་བསྟན་པ་དང་ཐུགས་རྗེ་ཆེན་པོ་གཙོར་བྱས་པས་གཞན་གྱི་དོན་བསྟན་པའོ། །

[Block 251]
བྱང་ཆུབ་ནི་རྟོགས་པའི༌[^321]དོན་ཏེ་བསྒྲུབ་པར་བྱ་བའི་འབྲས་བུའོ། །

[Block 252]
སེམས་དཔའ་ནི་ཐུགས་རྗེས་སེམས་ཅན་སྒྲོལ་བ་ལ་དཔའ་བའོ། །

[Block 253]
ཡང་ན་བྱང་ཆུབ་གསུམ་པོས་བསྒྲུབ་པ་ལ་ཡུལ་དང་དུས་ཀྱིས༌[^322]སྤ་བཀོང་བ་མེད་པར་བརྩོན་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 254]
ཡང་ན་བྱང་ཆུབ་ནི་ཤེས་རབ་བོ། །

[Block 255]
སེམས་དཔའ་ནི་ཐབས་ཏེ། ཆོས་དེ་ཉིད་ཀྱིས༌[^323]སེམས་ཅན་རྣམས་ལ་ཕན་པ་དང་བདེ་བ་སྟོབས་པའི་ཕྱིར་རོ། །

[Block 256]
ཆེན་པོ་ནི་ས་བརྒྱད་པ་ཡན་ཆད་ཆེན་པོ་ཞེས་བྱ་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་གཞན་དང༌[^324]ཐེག་པ་གཉིས་པ་དག་དགར་པའི་ཕྱིར་ཆེན་པོ་ཞེས་སྨོས་སོ། །

[Block 257 [HEADING]]
###### **དེའི་ཡོན་ཏན།** ^4-1-5-5-3-2-0

[Block 258]
མདོ་ལས་བླ་ན་མེད་པ་ཡང་དག་པའི་བྱང་ཆུབ་ཕྱིར་མི་ལྡོག་པ་ཤེ་དག༌[^325]ཅེས་འབྱུང་བ་ནི།[^326] མན་ཆད་ཚིག་བཅུ་གསུམ་གྱིས་འཕགས་པའི་ཡོན་ཏན་བསྟན་ཏེ།[^327] དེ་ཡང་རྣམ་པ་གཉིས་སུ་དབྱེའོ། །

[Block 259]
བླ་འོག་གི་ཡན་ལག་ཏུ་དབྱེ་བ་དང་བསྡུས་པའི་དོན་བསྟན་པའོ། །

[Block 260 [HEADING]]
###### **བླ་འོག་གི་ཡན་ལག་ཏུ་དབྱེ་བ།** ^4-1-5-5-3-2-1-0

[Block 261]
ཡན་ལག་ནི་ཆ་སྟེ་ཆ་སྔ་མས་ནི་སྤྱིའི་མཚན་ཉིད་བསྟན་པའོ། །

[Block 262]
ཆ་འོག་མས་ནི་སོ་སོའི་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 263 [HEADING]]
###### **སྤྱིའི་མཚན་ཉིད།** ^4-1-5-5-3-2-1-1-0

[Block 264]
བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ལས་ཕྱིར་མི་ལྡོག་པ་ཤེ་དག༌[^328]ཅེས་སྨོས་པ་ནི་དེ་སྤྱིའི་མཚན་ཉིད། །གཞན་ནི་སོ་སོའི་མཚན་ཉིད་དོ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པ་ཞེས་པ་ནི་ཆུད་པ་རྟོགས་པའི་དོན་རྣམ་པ་བཞིའོ། །

[Block 265]
ཆོས་ཀྱི་དབྱིངས་རྣམ་པར་དག་པ་རྟོགས་པ་ཉིད་བླ་ན་མེད་པའི་རྟོགས་པ་དང་། ཕྱི་རོལ་མུ་སྟེགས་ཅན་གྱི་རྟོགས་པ་ལས་ཁྱད་པར་དུ་བསྟན་པའི་ཕྱིར་ཡང་དག་པའི་རྟོགས་པ་དང་། ཐེག་པ་རྣམ་གཉིས་ཀྱི་རྟོགས་པ༌[^329]ལས་ཁྱད་པར་དུ་བསྟན་པའི་ཕྱིར་རྫོགས་པར་རྟོགས་པ་དང་། བྱང་ཆུབ་སེམས་དཔའ་ཡང་སྤྱོད་པ་མ་རྫོགས་པ་དག་ལ་ཁྱད་པར་དུ་བསྟན་པའི་ཕྱིར་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཅེས་བསྟན་ཏོ། །

[Block 266]
ཕྱིར་མི་ལྡོག་པའང་མོས་པ་ཕྱིར་མི་ལྡོག་པ་དང་། གྲལ་ཕྱིར་མི་ལྡོག་པ་དང་། ཆུད་པ་ཕྱིར་མི་ལྡོག་པ་དང་། སྤྱོད་པ་ཕྱིར་མི་ལྡོག་པའོ། །

[Block 267]
ཡང་ཕྱིར་མི་ལྡོག་པ་རྣམ་པ་གཉིས་ཏེ། ཐོས༌[^330]ཟིན་པ་ཕྱིར་མི་ལྡོག་པ་དང་། ཐོབ་པར་འགྱུར་བ་ཕྱིར་མི་ལྡོག་པའོ། །

[Block 268]
ཐོབ་པ་ནི་ས་དང་པོ་པའོ། །

[Block 269]
ཐོབ་པར་འགྱུར་བ་ནི་ས་བརྒྱད་པ་ཡན་ཆད་དོ། །

[Block 270 [HEADING]]
###### **སོ་སོའི་མཚན་ཉིད།** ^4-1-5-5-3-2-1-2-0

[Block 271]
ཡང་མདོ་ལས་གཟུངས་ཐོབ་པ་ཤེ་དག༌[^331]ཅེས་པ་ནས་ཕྱིར་མི་ལྡོག་པའི་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་ཤེ་དག༌[^332]ཅེས་བྱ་བའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིག་བཅུ་གཉིས་ཀྱིས༌[^333]དབྱེ་བའི་ཆ་བསྟན་ཏེ། དེ་ལ་དབྱེ་བ་རྣམ་པ་བཅུ་སྟེ། དེ་ལ་ཚིག༌[^334]

[Block 272]
དང་པོ་དགུས་ནི་རང་གི་དོན་བསྟན། འོག་མ་གཅིག་གིས་ནི་གཞན་གྱི་དོན་བསྟན།

[Block 273]
དང་པོ་དགུ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། དང་པོ་བརྒྱད་ཀྱིས་ནི་འདུས་བྱས་ཀྱི་ཡོན་ཏན་བསྟན། འོག་མ་གཅིག་གིས་ནི༌[^335]འདུས་མ་བྱས་ཀྱི༌[^336]ཡོན་ཏན་བསྟན།

[Block 274]
དང་པོ་ལའང་རྣམ་པ་གཉིས་ཏེ། དང་པོ་ལྔས་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་བསྟན། ཕྱི་མ་གསུམ་གྱིས་ནི་ཐུགས་རྗེ་དང་ཡེ་ཤེས་བསྟན་ཏོ། །

[Block 275]
དང་པོ་ལྔ་ལ་ཡང༌[^337]གཉིས་སུ་དབྱེ་སྟེ།

[Block 276]
དང་པོ་གསུམ་གྱིས་ནི་ནང་གི་སྤྱོད་པ་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས༌[^338]ནི་དགེ་བ་ལ་དམིགས་པ་བསྟན་ཏོ། །

[Block 277]
དང་པོ་ལ་ཡང་རྣམ་པ་གསུམ་སྟེ། བདག་གི་དོན་བསྒྲུབ་པ་དང་། གཞན་གྱི་དོན་བསྒྲུབ་པ་དང་། དགེ་བའི་ཆོས་ལ་དམིགས་པའི་ཕན་པའོ། །

[Block 278]
དམིགས་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། སྤྱོད་པ་བསྒྲུབ་པ་ལ་དམིགས་པ་དང་། ཐེ་ཙོམ་བཅད་པའོ། །

[Block 279]
ཐུགས་རྗེ་དང་ཡེ་ཤེས་བཤད་པ་ཡང་སྔར་ནི་བྱམས་པ་དང་སྙིང་རྗེ་བསྟན། དེའི་འོག་ཏུ་ནི་ཤེས་རབ་དང་ཡེ་ཤེས་བསྟན་ཏོ། །

[Block 280]
དེ་ཡང་རྣམ་པ་གསུམ་མོ། །

[Block 281]
ཆོས་ཐོས་པ་རྣམས་ལས་ཕྱིར་མི་ལྡོག་པ་ནི་དེ་ཀུན་ཀྱང་གཟུངས་ཐོབ་པ་ཤེ་དག༌[^339]གི་ཕྱིར་རོ། །

[Block 282]
གཟུངས་ནི་འཛིན་པའི་ཕྱིར་གཟུངས་ཏེ། དེ་ཡང་རྣམ་པ་གཉིས་སོ།[^340] །བསྡུས་པ་འཛིན་པ་དང་། སྤྲོས་པ་འཛིན་པའོ། །

[Block 283]
ཡང་འཛིན་པ་ནི་ཚིག་དང་དོན་འཛིན་པས་ཆོས་ཐོས་པ་རྣམས་མི་བརྗེད་པར་འཛིན་པའི་ཕྱིར་བསྡུས་པ་འཛིན་པའོ། །

[Block 284]
བྱང་ཆུབ་སེམས་དཔའ་ས་བརྒྱད་པ་ཡན་ཆད་ཀྱི་ཆོས་ཐམས་ཅད་ལ་བཟོད་པར་ནུས་པ། སེམས་པར་ནུས་པ་འཛིན་པར་ནུས་པ་སྟེ། བཟོད་པ་ནི་ཐོས་པའི་ཤེས་རབ། སེམས་ནི་བསམ་པའི་ཤེས་རབ། འཛིན་པ་ནི་བསྒོམ་པའི༌[^341]ཤེས་རབ་པོ། །དེ་ལ་ཡང་སྤྲོས་པ་འཛིན་པ་ནི་རྣམ་པ་བཞི་སྟེ། ཆོས་སྤྲོས་པ་འཛིན་པ་དང་། དོན་སྤྲོས་པ་འཛིན་པ་དང་། ཆོས་དགའ་བ་བཟོད་པ་དང་། རིགས༌[^342]སྔགས་ཀྱི་གཟུངས་རྣམས་སོ། །

[Block 285]
དེ་ཡང་རྣམ་པ་གཉིས་ཏེ། དང་པོ་ནི་སྒྲུབ་པའོ།[^343] །
--- END BLOCKS ---
