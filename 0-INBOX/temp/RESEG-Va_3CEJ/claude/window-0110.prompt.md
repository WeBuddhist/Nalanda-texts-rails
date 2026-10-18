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
[Block 3851 [HEADING]]
#### བསྐལ་པ། ^3-2-5-0

[Block 3852]
ད་ནི་བསྐལ་པ༌[^2199]བརྗོད་པར་བྱ་སྟེ། བསྐལ་པ་རྣམ་པ་མང་བཤད་པ། །བར་གྱི་བསྐལ་པ་དང་། འཇིག་པའི་བསྐལ་པ་དང་། འཆགས་པའི་བསྐལ་པ་དང་། བསྐལ་པ་ཆེན་པོའོ། །

[Block 3853]
དེ་ལ་རེ་ཞིག །

[Block 3854 [HEADING]]
##### འཇིག་པའི་བསྐལ་པ། ^3-2-5-1-0

[Block 3855 [VERSE]]
འཇིག་པའི་བསྐལ་པ་དམྱལ་བ་ཡི། །
སྲིད་པ་མེད་ནས་སྣོད་ཟད་པ། །

[Block 3856]
དམྱལ་བ་དག་ནས་སེམས་ཅན་མི་སྲིད་པ་ནས་བཟུང་སྟེ་སྣོད་ཟད་པའི་བར་རོ། །ཇི་ལྟ་བུ་ཞེ་ན། འཇིག་པ་ནི་གཉིས་ཏེ། འགྲོ་བ་འཇིག་པ་དང་། ཁམས་འཇིག་པའོ། །

[Block 3857]
ཡང་གཉིས་ཏེ། སེམས་ཅན་འཇིག་པ་དང་སྣོད་འཇིག་པའོ། །

[Block 3858 [HEADING]]
###### སེམས་ཅན་འཇིག་པ། ^3-2-5-1-1-0

[Block 3859]
གང་སེམས་ཅན་རྣམས་དམྱལ་བ་དག་ནས་འཆི་འཕོ་བར་འགྱུར་ཞིང་སྐྱེ་བར་མི་འགྱུར་བ་དེ་ལྟ་བུའི་དུས་ཀྱང་ཡོད་དེ། ད་ནི་འཇིག་པའི་བསྐལ་པ་མགོ་བརྩམ་པ༌[^2200]ཡིན་ཏེ། གང་འཇིག་རྟེན༌[^2201]འདི་ཆགས་ནས་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འདུག་པ་དེ་ལས་ནི་ངེས་པར་འབྱུང་བ་ཞེས་བརྗོད་པར་བྱ་ལ། གང་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འཇིག་པར་འགྱུར་བ་དེ་ལ་ནི་ཞུགས་པ་ཞེས་བརྗོད་པར་བྱ་སྟེ། གང་གི་ཚེ་དམྱལ་བ་དག་ན་སེམས་ཅན་འགའ་ཡང་མ་ལུས་པར་གྱུར་པ༌[^2202]དེ་ཙམ་གྱིས་འདི་ལྟ་སྟེ། དམྱལ་བ་འཇིག་པས་འཇིག་རྟེན་འདི་ཞིག་པ་ཡིན་ནོ། །

[Block 3860]
དེའི་ཚེ་གང་ལ་ངེས་པར་དམྱལ་བ་མྱོང་བར་འགྱུར་བའི་ལས་ཡོད་པ་དེ་ནི་འཇིག་རྟེན་གྱི་ཁམས་གཞན་དག་ཏུ་འཕེན་པར་འགྱུར་ཏེ། དུད་འགྲོ་མྱོང་བར་འགྱུར་བ་དང་། ཡི་དགས་མྱོང་བར་འགྱུར་བ་ཡང་དེ་བཞིན་དུ་བརྗོད་པར་བྱའོ། །

[Block 3861]
རྒྱ་མཚོ་ཆེན་པོ་ན་འཁོད་པའི་དུད་འགྲོ་རྣམས་ནི་སྔར་འཇིག་གོ། །

[Block 3862]
མི་དང་ལྷན་ཅིག་རྒྱུ་བ༌[^2203]རྣམས་ནི་དེ་དག་མི་དང་ལྷན་ཅིག་ཏུའོ། །

[Block 3863]
གང་མི་རྣམས་དག་གི་ནང་ན་སེམས་ཅན་གང་ཡང་རུང་བ་བདག་ཉིད་ཀྱིས་སློབ་དཔོན་མེད་པར༌[^2204]ཆོས་ཉིད་ཀྱིས་ཐོབ་པའི་བསམ་གཏན་དང་པོ་ལ་སྙོམས་པར་འཇུག་པ་དེ་ལྟ་བུའི་དུས་ཀྱང་ཡོད་དེ། དེ་དེ་ལས་ལངས་ནས་ཚིག་ཏུ་ཀྱེ་མ་དབེན་པ་ལས་སྐྱེས་པའི་དགའ་བ་དང་བདེ་བ་ནི་བདེ་བ་ཡིན་ནོ། །

[Block 3864]
དབེན་པ་ལས་སྐྱེས་པའི་དགའ་བ་དང་བདེ་བ་ནི་ཞི་བ་ཡིན་ནོ་ཞེས་ཀྱང་སྨྲ་ལ། སྒྲ་དེ་ཐོས་ནས་སེམས་ཅན་དེ་དག༌[^2205]ཀྱང་སྙོམས་པར་འཇུག་ཅིང་། ཤི་ནས་ཚངས་པའི་འཇིག་རྟེན་དུ་སྐྱེ་བར་འགྱུར་ཏེ། གང་གི་ཚེ་འཛམ་བུའི་གླིང་ན་སེམས་ཅན་འགའ་ཡང་མ་ལུས་པར་གྱུར་ན་དེ་ཙམ་གྱིས་འདི་ལྟ་སྟེ། འཛམ་བུའི་གླིང་འཇིག་པས་འཇིག་རྟེན་འདི་ཞིག་པ་ཡིན་ནོ། །

[Block 3865]
ཤར་གྱི་ལུས་འཕགས་དང་། ནུབ་ཀྱི་བ་ལང་སྤྱོད་དང་། བྱང་གི་སྒྲ་མི་སྙན་འཇིག་པ་དག་ཀྱང་དེ་བཞིན་དུ་བརྗོད་པར་བྱ་སྟེ། གང་གི་ཚེ་མི་དག་གི་ནང་ན་སེམས་ཅན་འགའ་ཡང་མ་ལུས་པར་གྱུར་པ་དེ་ཙམ་གྱིས་ན་འདི་ལྟ་སྟེ། མི་འཇིག་པས་འཇིག་རྟེན་འདི་ཞིག་པ་ཡིན་ནོ། །

[Block 3866]
བྱང་གི་སྒྲ་མི་སྙན་པ་རྣམས་ནི་འདོད་པ་ན་སྤྱོད་པའི་ལྷ་དག་གི་ནང་དུ་སྐྱེ་བར་འགྱུར་ཏེ། དེ་ན་འདོད་ཆགས་དང་བྲལ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 3867]
དེ་བཞིན་དུ་རྒྱལ་ཆེན་བཞིའི་རིས་ཀྱི་ལྷ་དག་ན། ཡང་བསམ་གཏན་དང་པོ་བསྐྱེད་པ་ནས་ཚངས་པའི་འཇིག་རྟེན་དུ་སྐྱེ་བར་འགྱུར་ཏེ། གང་གི་ཚེ་དེ་ན་སེམས་ཅན་འགའ་ཡང་མ་ལུས་པར་གྱུར་ན་དེ་ཙམ་གྱིས་འདི་ལྟ་སྟེ། རྒྱལ་ཆེན་བཞིའི་རིས་འཇིག་པས་འཇིག་རྟེན་འདི་ཞིག་པ་ཡིན་ནོ། །

[Block 3868]
གཞན་འཕྲུལ་དབང་བྱེད་འཇིག་པའི་བར་དུ་ཡང་དེ་བཞིན་དུ་བརྗོད་པར་བྱ་སྟེ། གང་གི་ཚེ་འདོད་པ་ན་སྤྱོད་པའི་ལྷ་དག་གི་ནང་ན་སེམས་ཅན་འགའ་ཡང་མ་ལུས་པར་གྱུར་པ་དེ་ཙམ་གྱིས་ན་འདི་ལྟ་སྟེ་འདོད་པའི་ཁམས་འཇིག་པས་འཇིག་རྟེན་འདི༌[^2206]ཞིག་པ་ཡིན་ནོ། །

[Block 3869]
ཚངས་པའི་འཇིག་རྟེན་ན་ཡང་སེམས་ཅན་གང་ཡང་རུང་བ་ཞིག་ཆོས་ཉིད་ཀྱིས་ཐོབ་པའི་བསམ་གཏན་གཉིས་པ་ལ་སྙོམས་པར་ཞུགས་ཏེ། ལངས་ནས་ཚིག་ཏུ་ཀྱེ་མ་ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པའི་དགའ་བ་དང་བདེ་བ་ནི་བདེ་བ་ཡིན་ནོ། །

[Block 3870]
ཀྱེ་མ་ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པའི་དགའ་བ་དང་བདེ་བ་ནི་ཞི་བ་ཡིན་ནོ་ཞེས་སྨྲ་བ། སེམས་ཅན་གཞན་དག་གིས་ཀྱང་སྒྲ་དེ་ཐོས་ནས་སྙོམས་པར་འཇུག་ཅིང་ཤི་ནས་ཀྱང་འོད་གསལ་གྱི་ལྷ་དག་གི་ནང་དུ་སྐྱེ་བར་འགྱུར་ཏེ། གང་གི་ཚེ་ཚངས་པའི་འཇིག་རྟེན་ན་སེམས་ཅན་འགའ་ཡང་མ་ལུས་པར་གྱུར་ན་དེ་ཙམ་གྱིས་འདི་ལྟ་སྟེ། སེམས་ཅན་འཇིག་པས་འཇིག་རྟེན་འདི་ཞིག་པ་ཡིན་ནོ། །

[Block 3871 [HEADING]]
###### སྣོད་འཇིག་པ། ^3-2-5-1-2-0

[Block 3872]
དེའི་འོག་ཏུ་སེམས་ཅན་རྣམས་ཀྱི་དེ་འཕེན་པའི་ལས་ཡོངས་སུ་ཟད་པ་དང་། སྣོད་སྟོང་པས་འདི་ཉིད་ནས་ཀུན་ནས་ཉི་མ་བདུན་བྱུང་ནས་རིམ་གྱིས་ས་དང་རི་རབ་ཀྱི་བར་དུ་མ་ལུས་པར་སྲེག་པར་བྱེད་དོ། །

[Block 3873]
རབ་ཏུ་འབར་བ་དེ་ཉིད་ལས་མེ་ལྕེ་རླུང་གིས་ཁྱེར་ནས་ཚངས་པའི་གཞལ་མེད་ཁང་གི་བར་དུ་སྲེག་པར་འགྱུར་རོ། །

[Block 3874]
མེ་ལྕེ་དེ་དང༌[^2207]དེའི་ས་པ་ཁོ་ནར་རིག་པར་བྱ་སྟེ། རིས་མི་མཐུན་པའི་སྐྱོན་དག་འགྲོ་བ་ནི་མེད་དེ། [^2208]དེ་དང་འབྲེལ་པ་ལས་བྱུང་བ་ཉིད་ཀྱི་ཕྱིར་དེ་ཉིད་ལས་ཞེས་བཤད་དེ། འདོད་པ་ན་སྤྱོད་པའི་མེ་ནི་གཟུགས་ན་སྤྱོད་པ་དང་འབྲེལ་པར་བྱེད་དོ། །

[Block 3875]
དེ་བཞིན༌[^2209]དུ་འཇིག་པ་གཞན་དག་ལ་ཡང་ཅི་རིགས་པར་བརྗོད་པར་བྱའོ། །

[Block 3876]
དེ་ལྟར་ན་དམྱལ་བ་དག་ན་སེམས་ཅན་རྣམས་འཆི་འཕོ་བ་དང་མི་སྐྱེ་བ་ནས་བཟུང་སྟེ། སྣོད་རྣམས་ཟད་པའི༌[^2210]བར་གྱི་དུས་དེ་ནི་འཇིག་པའི་བསྐལ་པ་ཞེས་བྱའོ། །

[Block 3877 [HEADING]]
##### འཆགས་པའི་བསྐལ་པ། ^3-2-5-2-0

[Block 3878]
འཆགས་པ་དང་པོའི་རླུང༌[^2211]ནི་དམྱལ་བ་སྲིད་པའི་བར་དུའོ། །

[Block 3879]
དང་པོའི་རླུང་ནས་བཟུང༌[^2212]སྟེ་དམྱལ་བ་དག་ནས་སེམས་ཅན་སྲིད་པའི་བར་ཏེ། དེ་ལྟར་འཇིག་རྟེན་ཞིག་པ་ནི་ནམ་མཁའ་ཙམ་ལུས་པར་ཡུན་རིང་དུ་གནས་སོ། །

[Block 3880]
ཡང་རིམ་གྱིས་སེམས་ཅན་རྣམས་ཀྱི་ལས་ཀྱི་དབང་གིས་ནམ་མཁའ་ལ་སྣོད་རྣམས་ཀྱི་སྔ་ལྟས་སུ་གྱུར་པ་རླུང་འཇམ་པོ་འཇམ་པོ་དག་ལྡང་སྟེ། དེའི་ཚེ་འཇིག་རྟེན་འདི་ཞིག་ནས་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འདུག་པ་གང་ཡིན་པ་དེ་ལས་ནི་ངེས་པར་བྱུང་བ་ཞེས་བརྗོད་པར་བྱ་ལ། བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འཆགས་པར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་ཉེ་བར་འོངས་པར་བརྗོད་པར་བྱའོ། །

[Block 3881]
དེ་ནས་རླུང་དེ་དག་སྐྱེ་བ་ན་ཇི་སྐད་བཤད་པའི་རླུང་གི་དཀྱིལ་འཁོར་དུ་འགྱུར་རོ། །

[Block 3882]
དེའི་འོག་ཏུ་རིམ་གྱིས་ཆུའི་དཀྱིལ་འཁོར་དང་། གསེར་གྱི་རང་བཞིན་གྱི་ས་གཞི་ཆེན་པོ་དང་། གླིང་རྣམས་དང་། རི་རབ་ལ་སོགས་པ་ཇི་སྐད་བཤད་པའི་རིམ་པ་དང་ཚུལ་དུ་ཐམས་ཅད་འབྱུང་ངོ་། །དང་པོར་ནི་ཚངས་པའི་གཞལ་མེད་ཁང་འབྱུང་ངོ་། །དེའི་འོག་ཏུ་ནི་འཐབ་བྲལ་པའི་བར་དུ་འབྱུང་ངོ་། །དེའི་འོག་ཏུ་ནི་རླུང་གི་དཀྱིལ་འཁོར་ལ་སོགས་པ་སྟེ། དེ་ཙམ་གྱིས་ན་འདི་ལྟ་སྟེ་སྣོད་ཆགས་པས་འཇིག་རྟེན་འདི་ཆགས་པ་ཡིན་ནོ། །

[Block 3883]
དེ་ནས་སེམས་ཅན་གང་ཡང་རུང་བ་ཞིག་འོད་གསལ་དག་ནས་ཤི་འཕོས་ནས་ཚངས་པའི་གཞལ་མེད་ཁང་སྟོང་པར་སྐྱེ་བར་འགྱུར་ལ། སེམས་ཅན་གཞན་དག་ཀྱང་དེ་ནས་ཤི་འཕོས་ནས་ཚངས་པའི་མདུན་ན་འདོན་དག་ཏུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3884]
དེའི་འོག་ཏུ་ཚངས་རིས་དག་དང་། གཞན་འཕྲུལ་དབང་བྱེད་དག་དང་། འཕྲུལ་དགའ་དག་ནས་རིམ་གྱིས་བྱང་གི་སྒྲ་མི་སྙན་པ་དང་། བ་ལང་སྤྱོད་དང་། ཤར་གྱི་ལུས་འཕགས་པོ་དང་། འཛམ་བུའི་གླིང་དང་། ཡི་དགས་རྣམས་དང་། དུད་འགྲོ་རྣམས་དང་། དམྱལ་བ་དག་གི་ནང་དུ་སྐྱེ་བར་འགྱུར་ཏེ། གང་མཇུག་ཏུ་འཇིག་པ་དེ་དང་པོར་འཆགས་པ་འདི་ནི་ཆོས་ཉིད་ཡིན་ནོ། །

[Block 3885]
གང་གི་ཚེ༌[^2213]དམྱལ་བ་དག་ན་སེམས་ཅན་འགའ་ཞིག་སྐྱེས་པར་གྱུར་པ་དེའི༌[^2214]ཚེ་འཇིག་རྟེན་འདི་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འཆགས་པ་གང་ཡིན་པ་དེ་ལས་ནི་ངེས་པར་བྱུང་བ་ཡིན་ལ། ཆགས་ནས་བར་གྱི་བསྐལ་པ་ཉི་ཤུར་འདུག་པར་འགྱུར་བ་གང༌[^2215]ཡིན་པ་དེ་ནི་ཉེ་བར་འོངས་པ་ཡིན་ནོ། །

[Block 3886 [HEADING]]
##### བར་གྱི་བསྐལ་པ། ^3-2-5-3-0

[Block 3887 [VERSE]]
བར་གྱི་བསྐལ་པ་དཔག་མེད་ནས། །
ཚེ་ལོ་བཅུ་པའི་བར་དུའོ། །

[Block 3888]
འཇིག་རྟེན་ཆགས་པ༌[^2216]ན་མི་རྣམས་ཀྱི་ཚེ་དཔག་ཏུ་མེད་པ་ལ་བར་གྱི་བསྐལ་པ་བཅུ་དགུར་འདའ་བར་འགྱུར་རོ། །

[Block 3889]
ཚེ་དཔག་ཏུ་མེད་པ་ནས་འགྲིབ་པ་ན་ཚེ་ལོ་བཅུ་པའི་བར་དུ་འགྱུར་ཏེ། འདི་ནི་ཆགས་ནས་གནས་པ་རྣམས་ཀྱི་བར་གྱི་བསྐལ་པ་དང་པོ་ཡིན་ནོ། །

[Block 3890 [VERSE]]
དེ་ནས་ཡར་སྐྱེ་མར་འབྲི་བའི། །
བསྐལ་པ་གཞན་ནི་བཅོ་བརྒྱད་དང་། །
--- END BLOCKS ---
