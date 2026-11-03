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
དྲན་པ་གང་དུ་སྦྱར་བར་བྱ་ན། འདི་ལྟར་དེའི༌[^3517]རྗེ་བོ་བཙལ། དྲན་པར་བྱ་བའི་དོན་ལའོ། །

[Block 4972]
ཅིའི་ཕྱིར་སྦྱར་བར་བྱ། དྲན་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 4973]
ཀྱེ་མ་དེ་ཉིད་དེའི་དོན་དུ་སྦྱོར་རོ༌[^3518]ཞེས་བྱ་བ་ནི་བསོད་ནམས་ཀྱིས་བསྐྱེད་པ་རྣམས་ཀྱིས་ལེགས་པར་སྨྲས་སོ། །

[Block 4974]
ཇི་ལྟར་སྦྱར་བར་བྱ། ཅི་དེ་བསྐྱེད་པའི་སྒོ་ནས་སམ། འོན་ཏེ་མངག་པའི་སྒོ་ནས། དྲན་པ་ལ་འགྲོ་བ་མི་རུང་བས་བསྐྱེད་པའི་སྒོ་ནས་སོ། །

[Block 4975]
དེ་ལྟ་ན་ནི་རྒྱུ་ཁོ་ན་ལ༌[^3519]རྗེ་བོ་ཡིན་ལ་འབྲས་བུ་ཁོ་ན་བྲན་ཡིན་པར་འགྱུར་ཏེ། འདི་ལྟར་རྒྱུ་ནི་འབྲས་བུ་ལ་དབང་བྱེད་ལ་འབྲས་བུ་ཡང་དེ་དང་ལྡན་ན༌[^3520]རྒྱུ་ཡིན་པས་དེ་ནི་དྲན་པའི་རྒྱུ་གང་ཡིན་པ་དེ་ཁོ་ན༌[^3521]ཡིན་ནོ། །

[Block 4976]
གང་ཡང་ནག་པ་ཞེས་བྱ་བ་འདུ་བྱེད་ཀྱི་ཚོགས་ཀྱི༌[^3522]རྒྱུན་ལ་གཅིག་ཏུ་བཟུང་ནས་བ་ཞེས་བྱ་བའི་རྗེ་བོ་བརྗོད་པ་དེ་ཡང་དེ་ཡུལ་གཞན་དུ་དང་། འགྱུར་བ་འབྱུང་བ་ལ་རྒྱུའི་དངོས་པོ་ཡིད༌[^3523]ལ་བསམས་ནས་རྗེ་བོ་ཞེས་བརྗོད་པར་ཟད་ཀྱི་ནག་པ་ཞེས་བྱ་བ་གཅིག་པུ་ནི་འགའ་ཡང་མེད་ལ་བ་ཞེས་བྱ་བ་ཡང་མེད་དོ། །

[Block 4977]
དེ་ལྟ་བས་ན་དེ་ལ་ཡང་རྒྱུའི་དངོས་པོ་མ་གཏོགས་པའི་རྗེ་བོའི་དངོས་པོ་མེད་དོ། །

[Block 4978 [HEADING]]
#### སུ་ཞིག་གིས་རྣམ་པར་ཤེས་པ། ^6-3-4-0

[Block 4979]
དེ་བཞིན་དུ་སུ་ཞིག་གིས༌[^3524]རྣམ་པར་ཤེས། སུའི་རྣམ་པར་ཤེས་པ་ཡིན་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་ཡང་བརྗོད་པར་བྱ་སྟེ། དེའི་རྒྱུ་ནི་ཅི་རིགས་པར་དབང་པོ་དང་དོན་དང་ཡིད་ལ་བྱེད་པ་དག་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ནི་ཁྱད་པར་ཡིན་ནོ། །

[Block 4980]
གང་ཡང་བྱ་བ་ནི་བྱེད་པ་པོ་ལ་ལྟོས་པའི་ཕྱིར་ཏེ། བྱ་བ་ཐམས་ཅད་ནི་བྱེད་པ་པོ་ལ་ལྟོས་ཏེ། ཇི་ལྟར་ལྷ་སྦྱིན་འགྲོའོ་ཞེས་བྱ་བ་འདི་ལ་འགྲོ་བར་བྱ་བ་ནི་འགྲོ་བ་པོ་ལྷས་བྱིན་ལ་ལྟོས་པ་དེ་བཞིན་དུ་རྣམ་པར་ཤེས་པ་ནི་བྱ་བ་ཡིན་ནོ། །

[Block 4981]
དེ་ལྟ་བས་ན་གང་ཞིག་གིས་རྣམ་པར་ཤེས་པ་དེ་ཡང་བརྗོད༌[^3525]དགོས་སོ་ཞེས་ཟེར་བ་དེ་ལ་ལྷས་བྱིན་ཞེས་བྱ་བ་འདི་ཅི་ཡིན་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 4982]
གལ་ཏེ་བདག་ཡིན་ནོ་ཞེ་ན། དེ་ཉིད་བསྒྲུབ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 4983]
འོན་ཏེ་སྐྱེས་བུར༌[^3526]ཐ་སྙད་གདགས་པ་ཡིན་ནོ་ཞེ་ན། དེ་ཡང་གཅིག་པུ་ནི་འགའ་ཡང་མེད་ཀྱི་འདུ་བྱེད་དེ་དག་ལ་ཡང༌[^3527]མིང་དེ་སྐད་ཅེས་བྱའོ། །

[Block 4984]
དེ་ལ་ཇི་ལྟར་ལྷས་བྱིན་འགྲོ་བ་དེ་བཞིན་དུ་རྣམ་པར་ཤེས་སོ། །

[Block 4985]
ལྷ་སྦྱིན་ཇི་ལྟར་འགྲོ་ཞེ་ན། འདུ་བྱེད་སྐད་ཅིག་པ་རྒྱུན་ཐ་མི་དད་པ་རྣམས་ལ་བྱིས་པ་རྣམས་ཀྱིས་གཅིག་པ་ཉིད་དུ༌[^3528]བཟུང་ནས་ལྷས་བྱིན་ཞེས་མོས་པ་རྣམས་རང་གི་རྒྱུན་ཡུལ་གཞན་དུ་འབྱུང་བ་ལ་རྒྱུར་གྱུར་ན་ལྷས་བྱིན་འགྲོའོ་ཞེས་བྱའོ། །

[Block 4986]
ཡུལ་གཞན་དུ་འབྱུང་བ་དེ་ནི་འགྲོ་བ་ཡིན་ཏེ། མེ༌[^3529]དང་སྒྲའི་རྒྱུན་དག་ལ་འགྲོའོ་ཞེས༌[^3530]བརྗོད་པ་ཡིན་ནོ། །

[Block 4987]
དེ་དག་ཉིད་རྣམ་པར་ཤེས་པའི་རྒྱུར་གྱུར་ན་ལྷས་བྱིན་གྱིས་རྣམ་པར་ཤེས་སོ་ཞེས་ཀྱང་བྱའོ། །

[Block 4988]
འཕགས་པ་རྣམས་ཀྱིས་ཀྱང་ཐ་སྙད་གདགས་པའི་དོན་དུ༌[^3531]དེ་དག་ལ་མིང་དུ་དེ་སྐད་ཅེས་གསུངས་སོ། །

[Block 4989]
འོ་ན་གང་མདོ་ལས་རྣམ་པར་ཤེས་པས་རྣམ་པར་ཤེས་སོ་ཞེས་གསུངས་པ་དེ་ལ་རྣམ་པར་ཤེས་པ་ཅི་ཞིག་བྱེད། ཅུང་ཟད་ཀྱང་མི་བྱེད་དེ། ཇི་ལྟར་འབྲས་བུ་ནི་ཅུང་ཟད་ཀྱང་མི་བྱེད་མོད་ཀྱི་འདྲ་བར་བདག་ཉིད་ཐོབ་པའི་ཕྱིར་རྒྱུ་དང་མཐུན་པར་བྱེད་དོ་ཞེས་བྱ་བ་དེ་བཞིན་དུ་རྣམ་པར་ཤེས་པ་ཡང་ཅུང་ཟད་ཀྱང་མི་བྱེད་མོད་ཀྱི་འདྲ་བར་བདག་ཉིད་ཐོབ་པའི་ཕྱིར་ཡུལ་རྣམ་པར་ཤེས་སོ་ཞེས་བྱའོ། །

[Block 4990]
འདིའི་འདྲ་བ་ཅི་ཞེ་ན།[^3532] དེའི་རྣམ་པ་ཉིད་དོ། །

[Block 4991]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་ནི་དབང་པོ་ལས་ཀྱང་སྐྱེས་མོད་ཀྱི་ཡུལ་རྣམ་པར་ཤེས་སོ་ཞེས་བྱ་བའི་དབང་པོ་ནི༌[^3533]མ་ཡིན་ནོ། །

[Block 4992]
ཡང་ན་ནི་དེར་ཡང་རྣམ་པར་ཤེས་པའི་རྒྱུན་རྣམ་པར་ཤེས་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རྣམ་པར་ཤེས་པས་རྣམ་པར་ཤེས་སོ་ཞེས་གསུངས་པས༌[^3534]ཉེས་པ་མེད་དེ། [^3535]རྒྱུ་ལ་བྱེད་པ་པོའི་སྒྲར་བསྟན་པའི་ཕྱིར་དྲིལ་བུ༌[^3536]སྒྲོགས་སོ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 4993]
གཞན་ཡང་ཇི་ལྟར་སྒྲོན་མ་འགྲོ་བ་ལྟར་རྣམ་པར་ཤེས་པས༌[^3537]རྣམ་པར་ཤེས་སོ་ཞེས་བྱ་བ་ཡང་དེ་དང་འདྲའོ། །

[Block 4994]
སྒྲོན་མ་ཇི་ལྟར་འགྲོ་ཞེ་ན། སྒྲོན་མ་ཞེས་བྱ་བ་ནི་མེ་ལྕེ་རྣམས་ཀྱི༌[^3538]རྒྱུན་ལ་ཉེ་བར་འདོགས་པར་བྱེད་ལ། དེ་ཡུལ་གཞན་དག་ཏུ༌[^3539]འབྱུང་བ་ལས༌[^3540]ཡུལ་དེ་དང་དེར༌[^3541]འགྲོའོ་ཞེས་བྱའོ། །

[Block 4995]
དེ་བཞིན་དུ་རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ནི་སེམས་རྣམས་ཀྱི་རྒྱུན་ལ་ཉེ་བར་འདོགས་པར་བྱེད་ལ་དེ་ཡུལ་གཞན་དག་ལ་སྐྱེ་བ་ལ་ཡུལ་དེ་དང་དེ་རྣམ་པར་ཤེས་སོ་ཞེས་བྱའོ། །

[Block 4996]
ཡང་ན་ཇི་ལྟར་གཟུགས་འགྱུར་རོ། །

[Block 4997]
སྐྱེའོ་གནས་སོ་ཞེས་བྱ་བ་འདི་ལ་འགྱུར་བ་པོ་དང་འགྱུར་བ་དོན་གཞན་མ་ཡིན་པ་ལྟར་རྣམ་པར་ཤེས་པ་ལ༌[^3542]དེ་དང་འདྲ་བར་འགྱུར་རོ། །

[Block 4998 [HEADING]]
#### རིམ་པ་ངེས་པར་སྐྱེ་བ། ^6-3-5-0

[Block 4999]
གལ་ཏེ་རྣམ་པར་ཤེས་པ་ལས་རྣམ་པར་ཤེས་པ་སྐྱེའི༌[^3543]བདག་ལས་མ་ཡིན་ན་ཅིའི་ཕྱིར་རྟག་ཏུ་དེ་དག༌[^3544]འདྲ་བ་ཁོ་ནར་སྐྱེ་བར་མི་འགྱུར་ཞིང་མྱུ་གུ་དང་སྡོང་པོ་དང་འདབ་མ་ལ་སོགས་པ་བཞིན་དུ་རིམ་པ་ངེས་པར་སྐྱེ་བར་མི་འགྱུར་ཞེ་ན། གནས་པ་གཞན་དུ་འགྱུར་བ་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་ཏེ། རྒྱུན་གདོན་མི་ཟ་བར་གཞན་དུ་འགྱུར་བ་གང་ཡིན་པ་འདི་ནི་འདུས་བྱས༌[^3545]ཀྱི་རང་བཞིན༌[^3546]ནོ། །

[Block 5000]
དེ་ལྟ་མ་ཡིན་ན་བསམ་གཏན་རྫོགས་པས་མཉམ་པར་གཞག་པ་རྣམས་ལས་ལུས་དང་སེམས་འདྲ་བ་སྐྱེ་ན་སྐད་ཅིག་མ་དང་པོ་དང་ཁྱད་པར་མེད་པའི་ཕྱིར་ཕྱིས་ཀྱང་བདག་ཉིད་ལྡང་བར་མི་འགྱུར་རོ། །

[Block 5001]
གང་ལས་གང་ཞིག་སྐྱེ་བར་འགྱུར་བ་དེ་ཁོ་ན་ལས་དེ་སྐྱེ་བའི་ཕྱིར་སེམས་ཅན་རྣམས་ཀྱི་རིམ་པ་ཡང་ངེས་པ༌[^3547]ཁོ་ན་སྟེ། རིགས་ཀྱི་བྱེ་བྲག་ལས་སེམས་རྣམ་པ་འདྲ་ཡང་འགའ་ཞིག་སེམས་འགའ་བསྐྱེད་པ༌[^3548]ལ་ནུས་པ་ཡིན་ཏེ། དཔེར་ན་བུད་མེད་ཀྱི༌[^3549]མཇུག་ཐོགས་སུ་གལ་ཏེ་དེའི་ལུས་སུན་འབྱིན་པའི་སེམས་སམ། དེའི་ཁྱོ་འམ་བུ་ལ་སོགས་པའི་སེམས་སྐྱེ་བར་འགྱུར་ལ། ཡང་ཕྱིས་རྒྱུད་ཡོངས་སུ་འགྱུར་བས་བུད་མེད་ཀྱི་སེམས་སྐྱེ་ན་དེ་ནི། དེའི་ལུས་སུན་འབྱིན་པའི་སེམས་བསྐྱེད༌[^3550]པའམ། དེའི་ཁྱོ་འམ། བུ་ལ་སོགས་པའི་སེམས་བསྐྱེད༌[^3551]པར་ནུས་པ་ཡིན་ཏེ། དེའི་རིགས་ཅན་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 5002]
གཞན་དུ་ནི་མི་ནུས་སོ། །

[Block 5003]
ཡང་བུད་མེད་ཀྱི་སེམས་ལས་རྣམ་གྲངས་ཀྱི་སེམས་རྣམ་པ་མང་པོ་ཞིག་སྐྱེས་པར་གྱུར་ན་དེ་ལས་ཆེས་མང་བ་དང་། ཆེས་གསལ་བ་དང་། ཆེས་ཉེ་བར༌[^3552]སྐྱེས་པ་གང་ཡིན་པ་དེ་ཁོ་ན་སྐྱེ་བར་འགྱུར་ཏེ། དེའི་བསྒོས་པ༌[^3553]སྟོབས་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 5004]
དེའི་འདུས་པའི་ལུས་དང་ཕྱི་རོལ་གྱི་རྐྱེན་གྱི་ཁྱད་པར་ནི་མ་གཏོགས་སོ། །

[Block 5005]
བསྒོས་པ༌[^3554]དེ་ཉིད་ཆེས་སྟོབས་དང༌[^3555]ལྡན་ན་ཅིའི་ཕྱིར་རྟག་ཏུ་འབྲས་བུ་མི་འབྱིན་ཞེ་ན། གནས་པ་གཞན་དུ་འགྱུར་པ་ཉིད་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་ལ། གཞན་དུ་འགྱུར་བ་དེ་ཡང་བསྒོས་པ༌[^3556]གཞན་གྱི༌[^3557]འབྲས་བུ་སྐྱེ་བའི་རྗེས་སུ་མཐུན་པའི་ཕྱིར་རོ། །

[Block 5006]
འདི་ནི་སེམས་ཀྱི་རྣམ་པ་ཐམས་ཅད་ལ་ཕྱོགས་ཙམ་དུ་ཟད་ཀྱི་མཇུག༌[^3558]ཐོགས་ཀྱི་རྒྱུ་ཤེས་པ་ལ་ནི་སངས་རྒྱས་རྣམས༌[^3559]མངའ་བདག་ཡིན་ཏེ། འདི་སྐད་དུ་རྨ་བྱའི་མདོངས་ནི་གཅིག་ལ་ཡང་། །

[Block 5007 [VERSE]]
རྒྱུ་ཡི་རྣམ་པ་ཐམས་ཅད་ནི། །
ཀུན་མཁྱེན་མིན་པས་ཤེས་བྱ་མིན། །
དེ་ཤེས་ཀུན་མཁྱེན་སྟོབས་ཡིན་ནོ། །

[Block 5008]
ཞེས་བཤད་ན། གཟུགས་ཅན་མ་ཡིན་པ་སེམས་ཀྱི་བྱེ་བྲག་རྣམས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། ཅིའི་ཕྱིར་དེ་དང་འདྲ་བ་ཁོ་ནར་སྐྱེ་བར་མི་འགྱུར་ཞིང་མྱུ་གུ་དང་སྡོང་བུ་དང་འདབ་མ་ལ་སོགས་པ་བཞིན་དུ་རིམ་པ་ངེས་པར་སྐྱེ་བར་མི་འགྱུར་ཞེས་བྱ་བ་འདི་ནི་མུ་སྟེགས་ཅན་གང་ལ་ལ་སེམས་ནི་བདག་ལས་སྐྱེའོ་སྙམ་དུ་སེམས་པ་དེ་ཁོ་ན་ལ་གསལ་བར་ཀླན་ཀར་འགྱུར་རོ། །

[Block 5009 [HEADING]]
#### ཡིད་དང་ཕྲད་པའི་བྱེ་བྲག། ^6-3-6-0

[Block 5010]
གལ་ཏེ་ཡིད་དང་ཕྲད་པའི་བྱེ་བྲག་ལ་ལྟོས་པའི་ཕྱིར་རོ་ཞེ་ན་མ་ཡིན་ཏེ། འབྲེལ་པ་གཞན་མ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
