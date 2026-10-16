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
[Block 6196]
རྣམ་པ་སྣ་ཚོགས་པའི་གསང་སྔགས་ཀྱི་མཐུ་སྟོབས་གང་ཡིན་པ་དེ་དག་ནི་གསང་སྔགས་ཀྱི་མཐུ་སྟོབས་རྣམས་སོ། །

[Block 6197]
ང་རྒྱལ་བདོ་བའི་བློ་ཅན་ཞེས་བྱ་བ་ནི་ལྷ་དང་ལྷ་མ་ཡིན་གྱི་དམག་ཚོགས་སོ། །

[Block 6198]
ཁྲོས་པ་མ་མཆིས་ཞེས་བྱ་བ་འདིས་ནི་གང་སྔར་བསྟན་པའི་བདག་ཉིད་ཕུང་བྱེད་པ་སུ་ཞིག་གིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་དེའི་དོན་མ་ཡིན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6199]
བྱམས་པ་མ་མཆིས་ཞེས་བྱ་བ་འདིས་ནི་གང་སྔར་བསྟན་པའི་ང་ལ་ཅུང་ཟད་དོགས་པའམ་ཞེས་བྱ་བའི་ཚིགས་བཅད་དོན་དེ་མེད་པ་ཉིད་དུ་སྟོན་ཏེ། [^3970]དེ་ལྟར༌[^3971]ན་ཅིའི་ཕྱིར་འགྲོ༌[^3972]ཞེ་ན། སྨྲས་པ། ཆོས་ཀྱི་དོན་དུ་འགྲོ་ཞེས་བྱ་བ་ཡིན་ཏེ། གང་དུ་འགྲོ་ཞེ་ན། ནགས་སུའོ། །ཇི་ལྟར་འགྲོ་ཞེ་ན། ངེས་པར་རོ། །

[Block 6200]
གལ་ཏེ་འཆི་བདག་འོང་བར་གྱུར་ན་ཡང་། ཇི་ལྟར་ལོག་པར་སྤྱོད་པ༌[^3973]ནི་ཆོས་མ་ཡིན་པའི་བདག་ཉིད་དེ། རྗེས་སུ་གདུངས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 6201]
དེ་ལྟ་མོད་ཀྱི། ཅིའི་ཕྱིར། ཆོས་ཀྱི་དོན་རྟོགས་པར་བྱ་བའི་ཕྱིར་རྒྱུར༌[^3974]འགྱུར་ཞེ་ན། སྨྲས་པ། ཆོས་ཀྱི་ནགས་ཚལ་དག་ན་བདེ་བར་སྒྲུབ༌[^3975]དུ་མཆིས། །ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 6202]
བག་མེད་དྲེགས་དང་འདོད་ཆགས་ཞེས་བྱ་བའི༌[^3976]ཚིགས་བཅད་འདིས་ནི། ཁྱིམ་ནི་ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས༌[^3977]པའི་ཕྱིར། ཉོན་མོངས་པའི་ཀུན་ནས་ཉོན་མོངས་པ་ནི། ཆོས་ཀྱི་དགྲ་ཡིན་པའི་ཕྱིར་དེ་དང་མི་མཐུན་པ་ཉིད་དུ་བསྟན༌[^3978]ཏོ། །

[Block 6203]
ལས་རྣམས་མང་པོ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི། ལས་དང་སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས་པ་ཉིད་དུ་བསྟན་ཏེ། སྡུག་བསྔལ་འབྱུང་བའི་གནས་ཞེས་བྱ་བ་འདིས་ནི་སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པས་ཉོན་མོངས༌[^3979]པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6204]
ཞི་བའི་ལམ་ནི་ཐར་པའི་ལམ་མོ། །

[Block 6205]
དེ་ལྟར་ཀུན་ནས་ཉོན་མོངས༌[^3980]པ་གསུམ་གྱིས་ཉོན་མོངས༌[^3981]པའི་ཕྱིར་ཆོས་དང་འགལ་བ་ཉིད་དོ། །

[Block 6206]
ནགས་ན་ནི་ཀུན་ནས་ཉོན་མོངས་པ་གསུམ་པོ་དེ་དག་མེད་པའི་ཕྱིར། ནགས་ན་བྱ་བ་ངན་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 6207]
ནགས་ན་བྱ་བ་ངན་པ་མང་པོ་བཏང་། །ཞེས་བྱ་བ་འདིས་ནི་ལས་ཀྱི་ཀུན་ནས་ཉོན་མོངས་པ་ནགས་ན་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6208]
བསོད་ནམས་འཐོབ་ཅིང་ཡོངས་སུ་བཟུང་བའི་སྡུག་བསྔལ་སྤངས་ལ་གཙང་ཞེས་བྱ་བ་འདིས་ནི་སྐྱེ་བའི་ཀུན་ནས་ཉོན་མོངས་པ་མེད་པར་བསྟན་ཏོ། །

[Block 6209]
དེ་མེད་པ་ཉིད་ཀྱིས། གཙང་ལ་ཞི་བ་འབའ་ཞིག་བྱེད། །[^3982]ཅེས་བྱ་བ་འདིས་ནི་བྱ་བ་ངན་པ་མང་པོ་བཏང་བ་དེའི་གཉེན་པོ་ཉོན་མོངས་པ་ཉེ་བར་ཞི་བ་འབའ་ཞིག་བྱེད་པའི་ཕྱིར་ཡང་ཆོས་ཡོངས་སུ་བཟུང་བ་ནི་ཉོན་མོངས་པའི་ཕྱོགས་ཡོངས་སུ་སྤངས་པའོ། །

[Block 6210]
མགུ་བ་དང་།

[Block 6211 [VERSE]]
གྲགས་པ་དེ་གཉིས་ནི་མཐོང་བའི་ཆོས་ཉིད་ཀྱིའོ། །
མི་རྣམས་ཆོས་ཀྱིས་བསྲུངས་ཀྱིས༌[^3983]ནོར་དང་དཔུང་གིས་མིན། །

[Block 6212]
ཞེས་བྱ་བ་འདིས་ནི་དོན་བཟློག་པའི་རྒྱུ་ཉིད་དུ་ཆོས་སྟོན་ཏེ། ནོར་དང་དཔུང་ནི་མ་ཡིན་ནོ། །ཞེས་བྱ་བ་སྟེ། སེམས་ཅན་དང་། སེམས་ཅན་མ་ཡིན་པས་མི་བསྲུང་ངོ་ཞེས་པའོ། །

[Block 6213]
ཆོས་ཀྱི་བདེ་བ་ཞེས་བྱ་བ་ནི། ཆོས་ཉིད་ཀྱིས་འདོད་པའི་དོན་སྒྲུབ་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 6214]
འཐོབ་ཅེས་བྱ་བ་ནི་སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པའི་དབང་ཕྱུག་གོ། །

[Block 6215]
ཆོས་ཀྱི་བདག་ཉིད་ཅན་ནི་ཤི་ནའང་དགའ་བར་འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི་འཆི་བའི་འཇིགས་པ་མེད་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 6216]
ངན་འགྲོའི་འཇིགས་པ་མེད་པར་འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི་ངན་སོང་དུ་འགྲོ་བའི་འཇིགས་པ་མེད་པར་སྟོན་ཏོ། །

[Block 6217]
འཆི་བའི་དུས་སུ་ངན་སོང་གི་འཇིགས་པ་མེད་པ་ནི་ཆོས་ལ་གནས་པའི་ཕྱིར་རོ། །

[Block 6218]
ད་ནི་དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། ལས་ཀྱི་ཁྱད་པར་དག་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 6219]
དགེ་བའི་མཚན་ཉིད་ཐ་དད་པ་ནི། སྲོག་གཅོད་པ་ལ་སོགས་པ་ལས་ལྡོག་པའི་མཚན་ཉིད་ཀྱི་ལས་ཀྱི་ཁྱད་པར་རོ། །

[Block 6220]
སྡིག་པའི་ལས་ཀྱི་མཚན་ཉིད་ནི། སྲོག་གཅོད་པ་ལ་སོགས་པའི་མཚན་ཉིད་དང་། སྦྱིན་པ་ལ་སོགས་པ་མེད་པའི་མཚན་ཉིད་དོ། །

[Block 6221]
ཇི་ལྟར་དགེ་བ་དང་མི་དགེ་བའི་ལས་ཀྱི་ཁྱད་པར་ཐ་དད་པ་དེ་བཞིན་དུ། རྣམ་པར་སྨིན་པ་ཡང་ཐ་དད་པ་ཡིན་ཏེ། ཇི་ལྟར་ཞེ་ན་སྨྲས་པ། མི་དགེ་བས་ནི་ངན་སོང་དུ་ལྟུང་བ་ཡིན་ལ། བསོད་ནམས་བསགས་པས༌[^3984]ནི་བདེ་བའི་གནས་སུ་འགྱུར་ཏེ། བདེ་བའི་གནས་སུ་འགྲོ་བ་གང་ཡིན་པ་དེ་ནི་བདེ་བའི་གནས་སུ་འགྲོ་བའོ། །

[Block 6222]
རྒྱལ་སྲིད༌[^3985]དཔལ་ཡང་རྩྭ་དང་འདྲ་བར་བོར། །ཞེས་བྱ་བ་ནི་ཕུན་སུམ་ཚོགས་པ་ཆེན་པོ་ལ་ཡང་མ་ཆགས་པ་སྟེ། དེས་ནི་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 6223]
དཀའ་ཐུབ་ཀྱི་ནགས་ཚལ་དུ་གནས་པར་གྱུར་ཏོ་ཞེས་བྱ་བས་ནི་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 6224]
བསམ་གཏན་ནི་བསམ་གཏན་བཞིའོ། །

[Block 6225]
ཚད་མེད་པ་ནི་བྱམས་པ་ལ་སོགས་པ་བཞིའོ། །

[Block 6226]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས།

[Block 6227]
ལྕགས་ཀྱི་ཁྱིམ་ནས་བསྐྱེད་པའི་སྐྱེས་པའི༌[^3986]རབས་སོ། །

[Block 6228 [HEADING]]
## མཇུག་བྱང། ^b-0

[Block 6229 [HEADING]]
### མཛད་བྱང། ^b-1-0

[Block 6230]
སྐྱེས་པའི་རབས་ཀྱི༌[^3987]རྒྱ་ཆེར་བཤད་པ༌[^3988]སློབ་དཔོན་དྷརྨ་ཀླི་རྟིས་མཛད་པ་རྫོགས་སོ།། །།

[Block 6231 [HEADING]]
### འགྱུར་བྱང། ^b-2-0

[Block 6232]
རྒྱ་གར་གྱི་མཁན་པོ་པཎྜི་ཏ་ཛ་ནཱར་དྷ་ན་དང་། ཞུ་ཆེན་གྱི་ལོ་ཙཱ་བ་ཨི་བུ་དགེ་སློང་ཤཱཀྱ་བློ་གྲོས་ཀྱིས་བསྒྱུར་བའོ།། །།

[Block 6233]
[^3989]
--- END BLOCKS ---
