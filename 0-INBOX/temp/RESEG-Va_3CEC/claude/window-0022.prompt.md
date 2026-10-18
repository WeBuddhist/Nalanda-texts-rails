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
[Block 771]
དེའང་རྣམ་པ་དྲུག་སྟེ། དམིགས་པར་བྱ་བ་ཚད་མེད་པས་དམིགས་པར་བྱེད་པ༌[^667]ཚད་མེད་པ་དང་། ལས་དང་འབྲས་བུ་དང་། རང་བཞིན་དང་ཁྱད་པར་དང་། རབ་ཏུ་དབྱེ་བ་བསྟན་ཏོ། །

[Block 772]
བཙུན་པ་ཤ་ར་དྭ༌[^668]ཏིའི་བུ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བྱམས་པ་ཡང་མི་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། དེ་དག་ཀྱང་བྱམས་པ་མི་ཟད་པར་འཕགས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་དམིགས་པ་ཚད་མེད་པས་དམིགས་པར་བྱེད་པ་ཚད་མེད་པ་བསྟན་ཏོ། །

[Block 773]
བློ་གྲོས་མི་ཟད་པས་སྨྲས་པ། བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་བྱམས་པ་ནི་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཚུལ་འཆོས་པ་དང་། ཁ་གསག་དང་། ཐོབ་ཀྱིས་འཇལ་བ་ཐམས་ཅད་དང་བྲལ་བ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^669]བསྟན་ཏོ། །

[Block 774]
རྙེད་པ་དང་བཀུར་སྟི་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ངན་སོང་ཐམས་ཅད་དང་མི་ཁོམ་པ་བརྒྱད་ལས་འདས་པ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་འབྲས་བུ་བསྟན་ཏོ། །

[Block 775]
ཆོས་ཀྱི་ཀུན་དགའ་ལ་དགའ༌[^670]མོས་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བག་ཆགས་དང་མཚམས༌[^671]སྦྱོར་བ་དང་ཉོན་མོངས་པའི་དྲི་ང་བ་སྦྱོང་བ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་རང་བཞིན་བསྟན་ཏོ། །

[Block 776]
བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་བྱམས་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་སྐྱོང་བ༌[^672]ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། བྱམས་པ་ནི༌[^673]ཆུ་བོ་ལས་སྒྲོལ་བའོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^674]ཁྱད་པར་བསྟན་ཏོ། །

[Block 777]
འདི་ལྟར༌[^675]བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་གསུམ་པོ་འདི་དག་ནི་བྱམས་པ་སྟེ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། འདི་ནི་བཙུན་པ་ཤ་ར་དྭ༌[^676]ཏིའི་བུ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བྱམས་པ་མི་ཟད་པ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^677]རབ་ཏུ་དབྱེ་བ་བསྟན་ཏོ། །

[Block 778 [HEADING]]
#### དམིགས་པ་ཚད་མེད་པས་དམིགས་པར་བྱེད་པ་ཚད་མེད་པ། ^2-1-1-0

[Block 779]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བྱམས་པ་མི་ཟད་པ་སྟེ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བྱམས་པ་ཡང་མི་ཟད་པ་ཡིན་ཏེ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 780]
ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་མི་ཟད་པའི་རྒྱུ་འདྲི་བ་སྟེ། བྱང་ཆུབ་སེམས་དཔའི་བྱམས་པ་དེ༌[^678]ཅིའི་ཕྱིར་མི་ཟད་པ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 781]
ཐུག་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བས་ནི་རྒྱུ་བསྟན་ཏེ། འདི་ཙམ་ཞིག་ཅེས་བྱ་བ་ནི་ཐུག་པའོ། །

[Block 782]
འདི་ཙམ་ཞིག་ཅེས་གཅད་དུ་མེད་པས་ཐུག་པ་མེད་པ་སྟེ། དེ་བས་ན་མི་ཟད་པའོ། །

[Block 783]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བྱམས་པ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས་བྱམས་པ་མི་ཟད་པའི༌[^679]གཏན་ཚིགས་བསྟན་ཏོ། །

[Block 784]
དེ་དག་གི་བྱམས་པ་ཉེ་བར་བསྒྲུབས་པ༌[^680]ཡོངས་སུ་ཆད་པ་མེད་དོ་ཞེས་བྱ་བ་ལ། འདི་ཙམ་ཞིག་ཚུན་ཆད་ནི་དམིགས་པར་བྱེད་ཀྱི། དེ་ཕན་ཆད་དམིགས་པར་མི་བྱེད་པ་ནི་བྱམས་པ་ཉེ་བར་བསྒྲུབ་པ༌[^681]ཡོངས་སུ་ཆད་པ་ཞེས་བྱ་སྟེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་བྱམས་པས་སེམས་ཅན་ཐམས་ཅད་ལ་དམིགས་པར་བྱེད་པས་ན་བྱམས་པ་ཉེ་བར་སྒྲུབ་པ༌[^682]ཆད་པ་མེད་པའོ། །

[Block 785]
འདི་ལྟར་སེམས་ཅན་གྱི་ཁམས་ཇི་ཙམ་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་བྱམས་པ༌[^683]ཉེ་བར་སྒྲུབ་པ༌[^684]ཡོངས་སུ་ཆད་པ་མེད་པའི་གཏན་ཚིགས་བསྒྲུབས་ཏེ་བསྟན་ཏོ།[^685] །བྱམས་པའི་སེམས་བསྐྱེད་པ༌[^686]ཞེས་བྱ་བ་ལ། བྱམས་པས༌[^687]སེམས་ཅན་ཐམས་ཅད་ལ་ཁྱབ་པར་བྱའོ་ཞེས་སེམས་བསྐྱེད་པ་ནི་བྱམས་པའི་སེམས་བསྐྱེད་པའོ། །

[Block 786]
བཙུན་པ་ཤ་ར་དྭ༌[^688]ཏིའི་བུ་འདི་ལྟ་སྟེ་དཔེར་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་བྱམས་པ་དེ་སེམས་ཅན་ཐམས་ཅད་ལ་ཁྱབ་པ་དང་མི་ཟད་པའི་དཔེ་སྟོན་པའོ། །

[Block 787]
རྒྱུ་ཆུང་ངུས༌[^689]ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཤེས་པ་ཆུང་ངུ་དང་། དཔེ་ཆུང༌[^690]ངུས་ནི་བསྟན་པར་མི་ནུས་སོ༌[^691]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 788]
མཚན་མ་བཞག་པ་འདི་དང་ཞེས་བྱ་བ་ནི༌[^692]ཕྱོགས་ཐམས་ཅད་རྒྱ་མཚོའི་ཆུས་གང་བར་གྱུར་པ་ལ་གོང་དུ་སྨོས་པའི་གྲངས༌[^693]སྙེད་ཀྱི་སེམས་ཅན་འདུས་ནས།[^694] སྐྲའི་རྩེ༌[^695]བརྒྱར་གཤགས་པའི་ཆས་ཆུའི་ཐིགས་པ༌[^696]གཅིག་བླངས་པའོ། །

[Block 789]
བགྲང་བ་འདི་ལྟ་བུ་ཞེས་བྱ་བ་ནི་ཡང་གང་གཱའི་ཀླུང་གི་བྱེ་མ་སྙེད་ཀྱི་སེམས་ཅན་རྣམས་འདུས་ཏེ། གང་གཱའི་ཀླུང་གི་བྱེ་མ་སྙེད་ཀྱི་བསྐལ་པ་འདས་པ་དང་། སྐྲའི་རྩེ་མོ་བརྒྱར་གཤགས་པའི་ཆས་ཆུའི་ཐིགས་པ༌[^697]གཉིས་བླངས་པ་ནས། གསུམ་བཞི་ཡན་ཆད་གོང་དུ༌[^698]བླངས་པ་བཞིན་དུ་བསྒྲེ་བའོ། །

[Block 790]
དེ་དག་ཀྱང་བྱམས་པ་མི་ཟད་པར་འཕགས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་སྐྲག་པ་མེད་པའི་བྱང་ཆུབ་སེམས་དཔའ༌[^699]དེ་དག་སོ་སོའི་སྐྱེ་བོ་དང་འཕགས་པ་ཉན་ཐོས་ལ་སོགས་པ་ཀུན་ལས་འཕགས་པའི་བྱམས་པ་མི་ཟད་པར་ལྡན་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 791]
དམིགས་པ་ཚད་མེད་པས་དམིགས་པར༌[^700]བྱེད་པ་ཚད་མེད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 792 [HEADING]]
#### ལས། ^2-1-2-0

[Block 793]
ལས་བསྟན་པའི་ཕྱིར། བློ་གྲོས་མི་ཟད་པར༌[^701]སྨྲས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 794]
བྱམས་པ་ནི་བདག་བསྲུང༌[^702]ཞིང་གཞན་ལ་ཕན་པར་གནས་པ་ཞེས་བྱ་བ་ལ། བྱམས་པ་དང་ལྡན་པ་ལ་གནོད་པར་བྱེད་པའི་དགྲ་མི་འབྱུང་བས་ན་བདག་བསྲུང་བའོ། །

[Block 795]
སེམས་ཅན་གཞན་ལ་ཕན་པ་སྟོབས་པར་བྱེད་པའི་གཞན་ལ་ཕན་པར་གནས་པའོ། །

[Block 796]
ཡང་ན་བྱམས་པ་དང་ལྡན་པ་དང་། དེ་ལ་ཞེ་སྡང་མེད་པའི་ཕྱིར་བདག་བསྲུང་བའོ། །

[Block 797]
གཞན་ལ་གནོད་པར་མི་བྱེད་པའི་ཕྱིར་གཞན་ལ་ཕན་པར་གནས་པའོ། །

[Block 798]
མཆོག་ཏུ་རྩོད་པ་མེད་པ་ཞེས་བྱ་བ་ནི་དོན་དང་དགོས་པ་གང་གི་ཕྱིར་ཡང་གཞན་དང་མི་རྩོད་པས་སོ། །

[Block 799]
རབ་ཏུ་འཇོམས་ཞེས་བྱ་བ་ནི་དེ་དག་སྤོང་བར་བྱེད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 800]
གཞན་ནི་གོང་དུ་བཤད་པར་ཟད་དོ། །

[Block 801]
བྲལ་བ་ཞེས་བྱ་བ་ནི་བྱམས་པ་དང་ལྡན་པ་ལ་ཞེ་སྡང་གི་བག་ལ་ཉལ་དང་ཀུན་ནས་ལྡང་བ༌[^703]མེད་པའི་ཕྱིར་རོ། །

[Block 802]
དད་པ་བསྐྱེད༌[^704]ཅིང་ཞེས་བྱ་བ་ནི་བྱམས་པ་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔའ་ལ་གཞན་གྱིས༌[^705]གནོད་པ་བྱས་ཀྱང་དེ་ལ་སླར་གནོད་པ་མི་བྱེད་དེ། དེའི་རྒྱུས་སེམས་ཅན་དགའ་བ་སྐྱེད་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 803]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་འཁྲུལ་པ་ལ་ཉེས་པར་མི་ལྟ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པའི་དབང་དུ་གྱུར་ནས་མི་དགེ་བ་ལ་འཇུག་པ་ནི་འཁྲུལ་པ་སྟེ། དེ་ཡང་གཞན་གྱི་རྐྱེན་ལས་བྱུང་བར་གྱུར་པ་ཤེས་ནས་དེ་ལ་སྐྱོན་དུ་མི་ལྟ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 804]
ཡོངས་སུ་གདུང་བར་བྱེད་ཅེས་བྱ་བ་ནི། བྱམས་པ་དང་ལྡན་པའང་དེ་ལ་ཞེ་སྡང་གི་འཁྲུག༌[^706]པའི་སེམས་དང་ལུས་ལ་མི་བདེ་བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 805]
དེ་བས་ན་ལུས་དང་སེམས་བདེ་བ་སྐྱེད་པ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 806]
ལུས་བདེ་བ་སྐྱེད་པ་ནི། ལུས་སིམ་པར་བྱེད་པས་སོ། །

[Block 807]
སེམས་བདེ་བ་སྐྱེད་པ༌[^707]ནི། སེམས་སིམ་པས་སོ། །

[Block 808]
གཞན་གྱིས་གནོད་པར་བྱ་བ་ལས་ཤིན་ཏུ་འདས་ཞེས་བྱ་བ་ནི། བྱམས་པ་དང་ལྡན་པ་ལ་སུ་ཡང་གནོད་པར་མི་བྱེད་པས་སོ། །

[Block 809]
ཉེས་པ་ཐམས་ཅད་ཀྱི་འཇིགས་པ༌[^708]དང་བྲལ་ཏེ༌[^709]ཞེས་བྱ་བ་ནི་བྱམས་པ་ཅན་གྱི་གང་ཟག་དེ་སྲོག་གཅོད་པ་དང་། མ་བྱིན་པར་ལེན་པ་ལ་སོགས་པའི་ལས་ལ་མི་འཇུག་པས་དེ་ལ་ཉེས་པ་བྱས་པ་ནི་རྒྱུ་ལས་མི་འབྱུང་བའི་ཚེ་འདི་ལ་བཅིངས་པ༌[^710]དང་། གསད་པ་དང་། ཚེ་རབས་གཞན་དུ་ངན་སོང་དུ་སྐྱེ་བའི་འཇིགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 810]
འཕགས་པའི་ལམ་དང་མཐུན་ཞེས་བྱ་བ་ནི་བྱམས་པ་དེ་འཕགས་པའི་ལམ་གྱི་ཡན་ལག་བརྒྱད་དང་མི་འགལ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
