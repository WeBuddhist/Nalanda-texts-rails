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
[Block 4516]
སྡུག་བསྔལ་བར་ཡང་མ་ཡིན་ལ་རྒྱུ་ལ་སོགས་པར༌[^3250]ཡང་མ་ཡིན་ཏེ། ཟག་པ་མེད་པ་ནི་དེའི་མཚན་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4517]
ལམ་གྱི་རྣམ་པ་རྣམས་སུ་ཡང་མ་ཡིན་ཏེ། སུན་དབྱུང་བར༌[^3251]བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4518 [VERSE]]
མཚན་མ་མེད་པ་མཚན་མེད་ནི། །
ཞི་བར་མ་བརྟགས་ཟད་པ་ལ། །

[Block 4519]
མཚན་མ་མེད་པ་མཚན་མ་མེད་པའི་ཏིང་ངེ་འཛིན་ནི་མི་སློབ་པའི་མཚན་མ་མེད་པའི་སོ་སོར་མ་བརྟགས་པས། འགོག་པ་ལ་ཞི་བའི་རྣམ་པར་དམིགས་ཏེ། [^3252]ཟག་པ་མེད་པ་ལ་སོ་སོར་བརྟགས་པས། འགོག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4520]
འགོག་པ་དང་། གྱ་ནོམ་པ་དང་། ངེས་པར་འབྱུང་བའི་རྣམ་པར་ནི་མ་ཡིན་ཏེ། མི་རྟག་པ་ཉིད་ཀྱི་འགོག་པ་དང་། ཐུན་མོང་ཡིན༌[^3253]པ་ཉིད་ཀྱི་ཕྱིར་དང་། ལུང་དུ་མ་བསྟན་པའི་ཕྱིར་དང་། བྲལ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4521]
ཏིང་ངེ་འཛིན་གཞན་འདི་དག་ནི་གཅིག་ཏུ་ཟག་བཅས། འཕགས་པའི་ལམ་ལ་སྡང༌[^3254]པའི་ཕྱིར་ཏེ། ཟག་པ་མེད་པ་དག་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །གང་དུ་སྐྱེད་པར་བྱེད་ཅེ་ན། མིའི་ནང་། མི་རྣམས་ཀྱི་ནང་ཁོ་ནར་སྐྱེད་ཀྱི་ལྷ་དག་གི་ནང་དུ་ནི་མ་ཡིན་ནོ། །སུ་ལ་སྐྱེ་ཞེ་ན། མི་གཡོ་ལ་དགྲ་བཅོམ་པ་གཞན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4522]
ས་དུ་པ་ཞིག་ལ་ནི་མ༌[^3255]ཡིན་ཞེ་ན། ཉེར་བསྡོགས་བདུན་ནི༌[^3256]མ་གཏོགས་སོ། །

[Block 4523]
ཉེར་བསྡོགས་བདུན་མ་གཏོགས་པ་ས་གཞན་བཅུ་གཅིག་པོ་འདོད་པའི་ཁམས་དང་། མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་དང་། གཟུགས་མེད་པ་རྣམས་ན་ཡོད་དོ། །

[Block 4524 [HEADING]]
### ཏིང་ངེ་འཛིན་བསྒོམ་པ་བཞི། ^5-16-0

[Block 4525 [HEADING]]
#### མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པར་འགྱུར་བ། ^5-16-1-0

[Block 4526]
ཡང་ཏིང་ངེ་འཛིན་བསྒོམ་པ༌[^3257]བཞི་སྟེ། ཏིང་ངེ་འཛིན་བསྒོམ་པ༌[^3258]ཀུན་ཏུ་བརྟེན་བསྒོམས་པར་བྱས་ལན་མང་དུ་བྱས་ན། མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པར་འགྱུར་བ་ཡང་ཡོད་ཅེས་བྱ་བ་རྒྱས་པར་འབྱུང་བ་དེ་ལ། དགེ་བའི་བསམ་གཏན་དང་པོ་ནི། བདེ་འགྱུར་ཏིང་འཛིན༌[^3259]བསྒོམ་པ༌[^3260]ཡིན། །དགེ་བའི་བསམ་གཏན་དང་པོ་སྟེ། དག་པ་པའམ། ཟག་པ་མེད་པ་ནི། མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པར་འགྱུར་བའི་ཏིང་ངེ་འཛིན་བསྒོམ་པ༌[^3261]ཡིན་ནོ། །

[Block 4527]
དེ་དང་པོ་ཡིན་པའི་ཕྱིར་གཞན་དང་གཞན་དག༌[^3262]ཀྱང་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 4528]
ཚེ་ཕྱི་མ་ལ་བདེ་བར་གནས་པར་འགྱུར་བ་ནི་ངེས་པ་མེད་དེ། ཡོངས་སུ་ཉམས་པ་དང་། གོང་དུ་སྐྱེས་པ་དང་། ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་རྣམས་ལ་དེ་མེད་པའི་ཕྱིར་རོ། །

[Block 4529 [HEADING]]
#### ཤེས་པ་མཐོང་བར་འགྱུར་བ། ^5-16-2-0

[Block 4530]
མིག་གི་མངོན་ཤེས་མཐོང་འགྱུར་འདོད། །ལྷའི་མིག་གི་མངོན་པར་ཤེས་པ་ནི་ཤེས་པ་མཐོང་བར་འགྱུར་བའི་ཏིང་ངེ་འཛིན་བསྒོམ་པ་ཡིན་ནོ། །

[Block 4531 [HEADING]]
#### ཤེས་རབ་རབ་ཏུ་རྣམ་པར་དབྱེ་བར་འགྱུར་བ། ^5-16-3-0

[Block 4532]
སྦྱོར་བ་ལས་བྱུང་བློ་དབྱེར་འགྱུར། །སྦྱོར་བ་ལས་བྱུང་བའི་ཡོན་ཏན་ཁམས་གསུམ་པ་དང་། ཟག་པ་མེད་པ་ཐམས་ཅད་ནི་ཤེས་རབ་རབ་ཏུ་རྣམ་པར་དབྱེ་བར་འགྱུར་བའི་ཏིང་ངེ་འཛིན་བསྒོམ་པ་ཡིན་ནོ། །

[Block 4533 [HEADING]]
#### ཟག་པ་ཟད་པར་འགྱུར་བ། ^5-16-4-0

[Block 4534 [VERSE]]
རྡོ་རྗེ་ལྟ་བུའི་བསམ་གཏན་མཐའི། །
གང་ཡིན་དེ་ཟག་ཟད་འགྱུར་བསྒོམ། །

[Block 4535]
བསམ་གཏན་བཞི་པའི་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གང་ཡིན་པ་དེ་ནི་ཟག་པ་ཟད་པར་འགྱུར་བའི་ཏིང་ངེ་འཛིན་བསྒོམ་པ་ཡིན་ནོ། །

[Block 4536]
བཅོམ་ལྡན་འདས་ཀྱིས༌[^3263]ཆོས་སྟོན་པ་འདི་ནི༌[^3264]བདག་ཉིད་ལ་ཉེ་བར་གཏོད་པ་ཡིན་ཏེ། དེའི་ཕྱིར་བསམ་གཏན་བཞི་ཁོ་ནར་གསུངས་སོ་ཞེས་གྲག་གོ། །

[Block 4537]
ཏིང་ངེ་འཛིན་རྣམས་ཀྱི་སྐབས་ནས་འོངས་པ་བཤད་ཟིན་ཏོ། །

[Block 4538 [HEADING]]
### ཏིང་ངེ་འཛིན་ལ་བརྟེན་པའི་ཡོན་ཏན། ^5-17-0

[Block 4539 [HEADING]]
#### ཚད་མེད་པ་བཞི། ^5-17-1-0

[Block 4540]
ད་ནི་ཏིང་ངེ་འཛིན་ལ་བརྟེན་པའི་ཡོན་ཏན་རྣམས་བསྟན་པའི་སྐབས་ཡིན་པས་བཤད་པར་བྱ་སྟེ། ཚད་མེད་པ་ནི་བཞི་ཡིན་ནོ། །

[Block 4541 [HEADING]]
##### གནོད་སེམས་ལ་སོགས་པའི་གཉེན་པོ། ^5-17-1-1-0

[Block 4542]
བྱམས་པ་དང་། སྙིང་རྗེ་དང་། དགའ་བ་དང་། བཏང་སྙོམས་ཏེ། སེམས་ཅན་ཚད་མེད་པ་ལ་དམིགས་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་བཞི་ཁོ་ན་ཡིན་ཞེ་ན། གནོད་སེམས་ལ་སོགས་གཉེན་པོའི་ཕྱིར། །གནོད་སེམས་དང་རྣམ་པར་འཚེ་བ་དང་། མི་དགའ་བ་དང་། འདོད་པའི་འདོད་ཆགས་དང་གནོད་སེམས་མང་བ་རྣམས་ཀྱིས༌[^3265]དེ་དག་སྤང་བར་བྱ་བའི་ཕྱིར་བཞི་སྟེ་གྲངས་བཞིན་ནོ། །

[Block 4543]
མི་སྡུག་པ་དང་བཏང་སྙོམས་གཉིས་འདོད་པའི་འདོད་ཆགས་ཀྱི་གཉེན་པོ་ཉིད་དུ་ཁྱད་པར་ཅི་ཞིག་ཡོད་ཅེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ། ཁ་དོག་གི་འདོད་ཆགས་ཀྱི་གཉེན་པོ་ནི་མི་སྡུག་པའོ། །

[Block 4544]
འཁྲིག་པའི་འདོད་ཆགས་ཀྱི་གཉེན་པོ་ནི་བཏང་སྙོམས་སོ་ཞེས་ཟེར་རོ། །

[Block 4545]
འདི་སྐད་དུ་འཁྲིག་པའི་འདོད་ཆགས་ཀྱི་གཉེན་པོ་ནི་མི་སྡུག་པའོ། །

[Block 4546]
ཕ་དང༌[^3266]མ་དང་བུ་དང་ཉེ་དུའི་འདོད་ཆགས་ཀྱི་གཉེན་པོ་ནི་བཏང་སྙོམས་སོ་ཞེས་བྱ་བ་ནི་རུང་ངོ་། །

[Block 4547 [HEADING]]
##### ཚད་མེད་པའི་རང་བཞིན། ^5-17-1-2-0

[Block 4548]
དེ་ལ། ཞེ་སྡང་མེད་བྱམས། བྱམས་པ་ནི་ཞེ་སྡང་མེད་པའི་རང་བཞིན་ནོ། །

[Block 4549]
སྙིང་རྗེ་ཡང་།

[Block 4550 [VERSE]]
སྙིང་རྗེ་ཡང༌[^3267]དེ་དང་འདྲའོ། །
ཡིད་བདེ་བ་ནི་དགའ་བ་ཡིན། །

[Block 4551]
དགའ་བ་ནི་ཡིད་བདེ་བའི་རང་བཞིན༌[^3268]ནོ། །

[Block 4552]
བཏང་སྙོམས་མ་ཆགས།

[Block 4553 [VERSE]]
བཏང་སྙོམས་ནི་མ་ཆགས་པའི་བདག་ཉིད་ཡིན་ནོ། །
ཇི་ལྟར་ན་གནོད་སེམས་ཀྱི་གཉེན་པོ་ཡིན་ཞེ་ན།
དེ་ནི་ཆགས་པས་དྲངས་པ་ཡིན་པའི་ཕྱིར་རོ། །
འདི་ནི་གཉི་གའི་རང་བཞིན་ཡིན་ན་རུང་ངོ་། །

[Block 4554 [HEADING]]
##### ཚད་མེད་པའི་རྣམ་པ། ^5-17-1-3-0

[Block 4555]
བྱམས་པ་ལ་སོགས་པ་འདི་དག་གི་རྣམ་པ་ནི།
--- END BLOCKS ---
