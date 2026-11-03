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
[Block 4971]
མཐོང་བའི་ཆོས་ལ་ཇི་ལྟར་བསོད་ནམས་ཟད་པ་ཡིན་ཞེ་ན། བསོད་ནམས་ཟད་པའི་ཉེས་པ་བསྟན་པའི་ཕྱིར། །སྡུག་བསྔལ་བཟོད་པར་དཀའ་བས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4972]
འདི་ལྟ་བུར་ནི་བརླག་པར་འགྱུར། །ཞེས་བྱ་བ་ནི་བྱ་བ་མ་ཡིན་པ་བྱེད་པས་ལྟུང་བ་སྟེ། བྱ་བ་མ་ཡིན་པ་བྱས་པས་བརླག་པ་ནི་ངན་སོང་གི་སྡུག་བསྔལ་ཡིན་ཏེ། བརླག་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4973]
འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་འདོད་པས་བསླུས། །ཞེས་བྱ་བ་ནི། ངན་འགྲོར་འགྲོ་བའི་ལས་དེ༌[^3213]འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་འདོད་པ་ལ་བསླུས་པའི་ཕྱིར་རོ། །

[Block 4974]
ཕྱེ་མ་ལེབ་བྲིད་པ་དང་འདྲ་བ་ནི༌[^3214]ངན་འགྲོར་འགྲོ་ཞིང་བརླག་པའི་རྒྱུར་གྱུར་པའི་ལས་ཀྱི་ལྟུང་བའོ། །

[Block 4975]
དེ་བས་སྙིང་རྗེ་ཞེས་བྱ་བ་ལ་འདིར་དེ་བས་ཞེས་བྱ་བ་ནི། འཇིག་རྟེན་གཉིག་ལ་ཕན་པའི་ཕྱིར་རོ། །

[Block 4976]
འདིར་གྲགས་པ་དང་། ཕ་རོལ་དུ་ཡང་སྙིང་རྗེ་ནི་ཕན་པ་ཡིན་ཏེ། བཀྱོན་པར་མ་མཛད་ཅིག་པའོ། །

[Block 4977]
འདི་ནི་ཅུང་ཟད་ཅི༌[^3215]དང་ཅི་འཚལ་བ། །ཞེས་བྱ་བ་ནི་རྙེད་བ་ལ་སོགས་པའོ། །

[Block 4978]
དེ་དག་ཅེས་བྱ་བ་ནི་བྱ་བ་མ་ཡིན་པ་བྱས་པ་དེའི་ཅི་འཚལ་བ་དེ་དེ་དང་། དེ་རྙེད་པ་ལ་སོགས་པས་སོ། །

[Block 4979]
ཐུབ་ཆོད་དོན་ཡོད་ཅེས་བྱ་བ་ནི་འབྲས་བུ་ཡོད་བར་རོ། །

[Block 4980]
ད་ནི་ཁྱོད་ཀྱིས་བཀའ་སྩོལ་སྤྱི་བོས་ནོད། །ཅེས་བྱ་བ་འདིས་ནི་གང་སྔར་བསྟན་པའི་རྒྱལ་པོ་ཆེན་པོ་རེ་ཞིག་གཞེས་ཤིག །བདག་ལ་མ་འཕེན་བར་ཞེས་བྱ་བ་དེའི་མི་མཐུན་པའི་ཕྱོགས་བདག་གི་ཤུགས་ཁས་ལེན་པར་སྟོན་པ་ཡིན་ནོ། །

[Block 4981]
སྙིང་རྗེ་དང་བཅས་པར་སྟོན་པ༌[^3216]ཞེས་བྱ་བ་ནི། གང་སྔར་བསྟན་པའི་རྒྱལ་པོ་ཆེན་པོ་གུམ་ལགས་པ་བཀུམ་སྟེ་ཅི་བགྱི་ཞེས་པ་དང་། དེ་བས་སྙིང་རྗེ་མཛོད་ལ་མ་བཀྱོན་པར་ཞེས་བྱ་བ་དེ་དག་གིས་བསྟན་པ་ཡིན་ནོ། །

[Block 4982]
གཡོ་མེད་པར་དེ་ལ་ཕན་འདོགས་པར་བྱེད་པ་དེ་ཞེས་བྱ་བ་ནི། གང་སྔར་བསྟན་པ་འདི་ནི་ཅུང་ཟད་ཅི་འཚལ་བ། །ཞེས་བྱ་བ་ལ་སོགས་པ་བསྟན་ཏོ། །

[Block 4983]
གསོད་དང་རྐུན༌[^3217]ལ་སོགས་པ་སྤོངས། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པས་ནི་ལོག་པར་གཡེམ་པ་དང་། བརྫུན་དུ་སྨྲ་བ་དང་། ཕྲ་མ་དང་། ཚིག་རྩུབ་པོ་དང་། ངག་འཁྱལ་བ་དང་། བརྣབ་སེམས་དང་། གནོད་སེམས་དང་། ལོག་པར་ལྟ་བ་ལས་ལྡོག་པའོ། །

[Block 4984]
རྣམ་པ་གསུམ་དུ་དབྱེ་བ་གང་ཡིན་པ་དེ་ནི། རྣམ་པ་གསུམ་དུ་གྱེས་པའི་བྱེད་པའོ། །

[Block 4985]
རྣམ་པ་གསུམ་དུ་བྱེད་པ་ནི། ལུས་ཀྱི་ལས་དང་། ངག་གི་ལས་དང་། ཡིད་ཀྱི་ལས་དང་རྣམ་པ་གསུམ་མོ། །

[Block 4986]
གསུམ་དང་། བཞི་དང་། གསུམ་ནི་ལས་ཀྱི་ལམ་མོ། །ཇི་ལྟར་སྙིང་རྗེ་བསྐྱེད་པ་ཡིན་ཞེ་ན། གང་གི་ཕྱིར་སྙིང་རྗེ་ཡོད་ན་ནི། གསོད་པ་ལ་སོགས་པ་ལས་སྡིག་པའི་མཚན་ཉིད་ཀྱི་ཆོས་སུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 4987]
རྣམ་པ་གསུམ་དུ་གྱེས་པ་བྱེད་པ་དེ་བསྟན་པའི་ཕྱིར། བདག་རང་ཉིད་དམ། ནང་མི་ལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། ཇི་ལྟར་བདག་དང་ནང་མི་དག་ལ༌[^3218]བརྩེ་བ་དེ་བཞིན་དུ་གཞན་ལ་ཡང་ངོ་། །

[Block 4988 [VERSE]]
དེ་ཡིས༌[^3219]སེམས་ནི་ཆོས་མིན་ལ། །
འཇུག་པའི་མི་དགེ་ག་ལ་འབྱུང་། །

[Block 4989]
ཞེས་བྱ་བ་སྟེ། འདིས་ནི་མི་དགེ་བ་བཅུའི་ལས་ཀྱི་ལམ་ལས་ལོག་པར་བསྟན་ཏོ། །

[Block 4990]
སྐྱེ་བོ་སྙིང་རྗེ་མེད་པར་གྱུར་ན་ནི། །མི་དགེ་བ་བཅུའི་ལམ་ལ་འཇུག་པར་འགྱུར་བ་དེའི་དབང་དུ་བྱས་ནས།

[Block 4991 [VERSE]]
སྐྱེ་བོ་སྙིང་རྗེ་མེད་པས་ན། །
ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །
དེ་བས་ཆོས་ལ་དད་པ་ཡིས། །

[Block 4992]
ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་བསྡུས་པ་ཡིན་ཏེ། དེ་ལས་ཡོན་ཏན་འཕེལ་བར་འགྱུར། །ཞེས་བྱ་བ་ལ། ཡོན་ཏན་གང་ཡིན་པ་དེ་དག་བསྟན་པའི་ཕྱིར། སྙིང་རྗེས་ནོན་པའི་སེམས་ནི་གཞན་ལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4993]
གནོད་པ༌[^3220]བྱེད་མི་འགྱུར་ཞེས་བྱ་བ་ནི་ཡིད་ཀྱི་མི་དགེ་བའི་ལས་ཀྱི་ལམ་མེད་པར་བསྟན་ཏོ། །

[Block 4994]
ངག་ཀྱང་གཞན་དུ་འགྱུར་བ་མེད། །ཅེས་བྱ་བ་ནི་ངག་གི་མི་དགེ་བའི་ལས་ཀྱི་ལམ་མེད་པར་བསྟན་ཏོ། །

[Block 4995]
ལུས་ཀྱང་གཞན་དུ་འགྱུར་བ་མེད། །ཅེས་བྱ་བ་འདིས་ནི་ལུས་ཀྱི་མི་དགེ་བའི་ལམ་གྱི་ལམ་མེད་པར་བསྟན་ཏོ། །

[Block 4996]
དེ་ལྟར་མི་དགེ་བ་ལས་ལྡོག་པའི་ཚུལ་བསྟན་ནས། ད་ནི་དགེ་བ་ལ༌[^3221]འཇུག་པའི་ཚུལ་གྱི་དབང་དུ་བྱས་ནས། སྦྱིན་དང་བཟོད་ལ་སོགས་ཞེས་བྱ་བ་སྨོས་ཏེ། སོགས་པའི་སྒྲས་ནི་བརྩོན་འགྲུས་དང་། བསམ་གཏན་དང་། ཤེས་རབ་དང་། བསྡུ༌[^3222]བའི་དངོས་པོ་རྣམས་གཟུང༌[^3223]ངོ་། །ཚུལ་ཁྲིམས་མ་སྨོས་པ་ནི། སྡོམ་པའི་ཚུལ་ཁྲིམས་ནི་སྔར་བཤད་པའི་ཕྱིར་རོ། །

[Block 4997]
དགེ་བའི་ཆོས་སྡུད་པ་དང་། སེམས་ཅན་གྱི་དོན་བྱེད་པ་ནི་སྩོགས་པའི་སྒྲས་སྒྲུབ༌[^3224]པའོ། །

[Block 4998]
གཞན་དག་ཀྱང་སྩོགས་པའི་སྒྲས་གཟུང་བར༌[^3225]བྱ་སྟེ། ཡོན་ཏན་རྣམས་བསྟན་པའི་ཕྱིར། སྙིང་རྗེ་ཅན་ནི་ཉེ་བར་ཞི་བས་ཞེས་བྱ་བའི་ཚིག་རྐང་འདི་བསྟན་པ་ཡིན་ཏེ། འདིས་ནི་བདག་དང་གཞན་ལ་ཡིད་འབྱུང་བར་མི་བྱེད་པས་ཡོན་ཏན་ནོ། །

[Block 4999]
ཡིད་འབྱུང་བ་མེད་པ་ནི་ཉི་ཚེར་མ་ཟད་དེ། དེ་བཞིན་དུ་ཡིད་བརྟན་པར་ཡང་བྱེད་པ་ཡིན་ནོ། །

[Block 5000]
ཡོན་ཏན་འདི་གཉིས་ནི་གཞན་དང་འབྲེལ་པའོ། །

[Block 5001]
འཐབ་མོའི་འཁྲུག་པ་ཡོང༌[^3226]མི་འབྱུང་། །ཞེས་བྱ་བ་འདིས་ནི། ལུས་དང་། ངག་གི་ལས་ཀྱི་སྦྱོར་བས་བདག་དང་གཞན་ལ་གནོད་པ་མེད་པར་སྟོན་ཏོ། །

[Block 5002]
འཁྲུག་པའི་མེ་འབར་ཡོང་མི་འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི། བདག་གི་བསམ་པ་ལ་གནོད་པ་མེད་པར་བསྟན་ཏོ། །

[Block 5003]
མདོར་ན་ཞེས་བྱ་བ་ནི། སྔར་བསྟན་པའི་དོན་བསྡུ་བའི་ཚིགས་སུ་བཅད་པ་ཡིན་ཏེ། མཁས་པའི་ཆོས་ལ་ལྟ་ཞེས་བྱ་བ་འདིས་ནི། སེམས་ཅན་རྣམས་ལ་སྙིང་རྗེ་སྐྱེད། ། ཅེས་བྱ་བའི་ཚིགས་བཅད་སྔར་བསྟན་པ་དེ་སྟོན་པ་ཡིན་ནོ། །

[Block 5004]
དགའ་བའི་ཡོན་ཏན་བརྩེ་ལ༌[^3227]མི་བརྟེན་གང་ཞིག་ཡོད། །ཅེས་བྱ་བ་འདིས་ནི། གསོད་དང་རྐུ་ལ་སོགས་པ་སྤོངས། །ཞེས་གང་བསྟན་པ་དེ་དག་ཉིད་བསྟན་ཏོ། །

[Block 5005]
དེ་བས་བདག་དང་བུ་བཞིན་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི། བདག་རང་ཉིད་དམ་ནང་མི༌[^3228]ལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་དུ་གང་བསྟན་པ་ད་ཉིད་བསྟན་ཏོ། །

[Block 5006]
དམ་པའི་ཚུལ་ཞེས་བྱ་བ་འཇུག་པ་དང་། ལྡོག་པའི་ཚུལ་གྱིས་སོ། །

[Block 5007]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་རི་དགས་རུ༌[^3229]རུའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 5008 [HEADING]]
## སྤྲེའུའི་རྒྱལ་པོའི་སྐྱེས་པའི་རབས། ^29-0

[Block 5009]
དམ་པ་རྣམས་ཀྱི་ཚུལ་ནི་དམ་པའི་ཚུལ་ལོ། །

[Block 5010]
ཡང་ན་དམ་པ་ཉིད་ཚུལ་ཡིན་པས་དམ་པའི་ཚུལ་ལོ། །
--- END BLOCKS ---
