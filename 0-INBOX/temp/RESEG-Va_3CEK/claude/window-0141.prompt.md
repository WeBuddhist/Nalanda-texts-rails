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
[Block 4936]
ཡང་གང་ཟག་ཇི་ལྟར་འཁོར་ཕུང་པོ་གཞན་འདོར་བ་དང་། ལེན་པའི་ཕྱིར་རོ། །

[Block 4937]
ཕྱོགས་འདི་ནི་ལན་བཏབ་ཟིན་ཏོ།[^3493] །ཇི་ལྟར་མེ༌[^3494]སྐད་ཅིག་མ་ཡིན་ཡང་རྒྱུན་གྱིས་དྲོ་བ༌[^3495]དེ་བཞིན་དུ་སྲེད་པ་ཉེ་བར་ལེན་པ་ཅན་སེམས་ཅན་ཞེས་བྱ་བ་ཕུང་པོའི་ཚོགས་འཁོར་རོ། །

[Block 4938 [HEADING]]
#### ང་ཉིད་དེའི་ཚེ་སྟོན་པར་གྱུར་ཏོ་ཞེས་གསུངས་པ། ^6-2-15-0

[Block 4939]
གལ་ཏེ་འདི་ཕུང་པོ་ཙམ༌[^3496]ཡིན་ན་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ང་ཉིད༌[^3497]དེའི་ཚེ་དེའི༌[^3498]དུས་ན་མིག་བཟངས༌[^3499]ཞེས་བྱ་བའི་སྟོན་པར་གྱུར་ཏོ༌[^3500]ཞེས་གསུངས་སོ། །

[Block 4940]
ཅིའི་ཕྱིར་གསུང༌[^3501]བར༌[^3502]མི་འགྱུར། ཕུང་པོ་རྣམས་གཞན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4941]
འོ་ན་ཅི༌[^3503]དེ་ཉིད་གང་ཟག་ཡིན་ན་ནི་རྟག་པར་འགྱུར་རོ། །

[Block 4942]
དེ་ལྟ་བས་ན་ང་ཉིད་དེ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྒྱུད་གཅིག་པ་ཉིད་དུ་སྟོན་པར་མཛད་པ་ཡིན་ཏེ། དཔེར་ན་མེ་དེ་ཉིད་སྲེག་ཅིང་འོངས་སོ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 4943 [HEADING]]
#### ཐར་པ་ཐག་རིང་བར་འགྱུར་བ། ^6-2-16-0

[Block 4944]
གལ་ཏེ་ཡང་བདག་དེ༌[^3504]ཡོད་པར་གྱུར་ན་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས༌[^3505]ཤིན་ཏུ་གསལ་བ་ཁོ་ནར་གཟིགས་པར་འགྱུར་རོ། །

[Block 4945]
གཟིགས་ན་ཡང་བདག་ཏུ་འཛིན་པ་ཤིན་ཏུ་དམ་པོར་འགྱུར་རོ། །

[Block 4946]
བདག་ཡོད་ན་བདག་གིར་ཡང་འགྱུར་རོ་ཞེས་མདོ་ལས་འབྱུང་བའི་ཕྱིར་དེ་དག་ཕུང་པོ་རྣམས་ལ་བདག་གིར་འཛིན་པ་ལྷག་པར་འབྱུང་བས་དེ་ནི་དེ་དག་གི་འཇིག་ཚོགས་ལ་ལྟ་བར་འགྱུར་རོ། །

[Block 4947]
བདག་གིར་ལྟ་བ་ཡོད་ན་ཡང་བདག་གིར་ཆགས་པར་འགྱུར་ཏེ། དེ་ལྟ་བས་ན་བདག་དང་བདག་གིར་ཆགས་པའི་འཆིང་བ་ཤིན་ཏུ་དམ་པོས་གླགས་པ༌[^3506]དེ་དག་ལ་ཐར་པ་ཐག་རིང་བར་འགྱུར་རོ། །

[Block 4948]
འོན་ཏེ་བདག་ལ་ཆགས་པ་མི་འབྱུང་བ་ཁོ་ནའོ་ཞེས་བྱ་བར་འདོད་ན། དེ་ནི་བདག་མེད་པ་ལ་ནི་བདག་ཏུ་རྨོངས་པས་ཆགས་པ་སྐྱེའི་བདག་ཉིད་ལ༌[^3507]མི་སྐྱེའོ་ཞེས་བྱ་བ་དེ་ག༌[^3508]ལ་རུང་སྟེ། དེ་ལྟ་བས་ན་ཁ་ཅིག་ནི་གང་ཟག་ཏུ་འཛིན་ཁ་ཅིག་ནི་ཐམས་ཅད་མེད་པ་ཉིད་དུ་འཛིན་པ་གང་ཡིན་པ་དེ་ནི་བསྟན་པ་འདི་ལ་སྐྱོན་བྱུང་བ་ཡིན་ནོ། །

[Block 4949 [HEADING]]
### མུ་སྟེགས་བྱེད་བདག་རྫས་གཞན་ཁོ་ན་ཡིན་པར་སེམས་པ། ^6-3-0

[Block 4950]
མུ་སྟེགས་བྱེད་གང་དག་བདག་རྫས་གཞན་ཁོ་ན་ཡིན་པར་སེམས་པ་དེ་དག་གི་ལྟར་ན་ཡང་ཐར་པ་མེད་པའི་ཉེས་པ་འདི་གཡོ་བ་མེད་པ་ཡིན་ནོ། །

[Block 4951 [HEADING]]
#### དྲན་པའམ་ངོ་ཤེས་པ། ^6-3-1-0

[Block 4952]
འོ་ན་གལ་ཏེ་བདག་རྣམ་པ་ཐམས་ཅད་དུ་མེད་ན་སེམས་སྐད་ཅིག་མ་རྣམས་ལ་ཉམས་སུ་མྱོང་ནས་རིང་མོ་ཞིག་ལོན་པའི་དོན་ཇི་ལྟར༌[^3509]དྲན་པའམ་ངོ་ཤེས་པར་འགྱུར། དྲན་པའི་ཡུལ་ལ་འདུ་ཤེས་པའི་རྒྱུ་ལས་བྱུང་བའི་སེམས་ཀྱི་ཁྱད་པར་ལས་སོ། །

[Block 4953]
སེམས་ཀྱི་ཁྱད་པར་ཇི་ལྟ་བུ་ལས་ཤེ་ན། གང་གི་མཇུག་ཐོགས་སུ་དྲན་པ་སྐྱེ་བ་སྟེ། དེ་དག་ལ་རྟག་པ་དང་འདྲ་བ་དང་འབྲེལ་བ་ཅན་གྱི་འདུ་ཤེས་ལ་སོགས་པ་དང་ལྡན་པ་དང་རྟེན་གྱི་ཁྱད་པར་དང་། མྱ་ངན་དང་རྣམ་པར་གཡེངས་པ་ལ་སོགས་པས་མཐུ་མ་ཉམས་པ་ཅན་ལས་སོ། །

[Block 4954]
དེ་ལྟ་བུ་ཡིན་ཡང་དེའི་རྒྱུ་ལས་བྱུང་བ་མ་ཡིན་པའི་སེམས་ཀྱི་ཁྱད་པར་གྱིས་ནི་དྲན་པ་དེ་བསྐྱེད་པར་མི་ནུས་སོ། །

[Block 4955]
དེའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་ཡང་གཞན་ལྟ་བུ་ནི་དྲན་པ་དེ་སྐྱེད་པར༌[^3510]མི་ནུས་ཀྱི་གཉི་ག་ལྟར་ན་ནུས་པས་དེ་ལྟར་ན་དྲན་པར་འགྱུར་ཏེ། གཞན་ལ་ནི་དེའི་མཐུ་མ་མཐོང་པའི་ཕྱིར་རོ། །

[Block 4956]
ད་ནི་ཇི་ལྟར་ན་སེམས་གཞན་གྱིས་མཐོང་ལ་གཞན་གྱིས་དྲན་དེ་ལྟར་ན་ནི་ལྷ་སྦྱིན་གྱིས་སེམས་ཀྱིས༌[^3511]མཐོང་ལ་མཆོད་སྦྱིན་གྱིས༌[^3512]སེམས་ཀྱིས་དྲན་པར་འགྱུར་རོ། །

[Block 4957]
མ་ཡིན་ཏེ་འབྲེལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 4958]
དེ་གཉིས་ནི་རྒྱུ་དང་འབྲས་བུར་མ་གྱུར་པའི་ཕྱིར་ཇི་ལྟར་ན༌[^3513]རྒྱུད་གཅིག་ལ་ཡོད་པའི་རྒྱུ་དང་འབྲས་བུར༌[^3514]འབྲེལ་བ་ནི་མེད་དོ། །

[Block 4959]
སེམས་གཞན་གྱིས་མཐོང་ལ་གཞན་གྱིས་དྲན་ནོ་ཞེས་ཀྱང་མི་ཟེར་རོ། །

[Block 4960]
འོན་ཀྱང་ཇི་སྐད་བཤད་པ་ལྟར་རྒྱུད་ཡོངས་སུ་འགྱུར་བའི་ཚུལ་གྱིས་མཐོང་པའི་སེམས་ལ་དྲན་པའི་སེམས་གཞན་སྐྱེའོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་ཉེས་པ་ཅི་ཞིག་ཡོད། དྲན་པ་ཁོ་ན་ལས་ངོ་ཤེས་པ་ཡང་ཡིན་ནོ། །

[Block 4961 [HEADING]]
#### སུ་ཞིག་གིས་དྲན་པ། ^6-3-2-0

[Block 4962]
བདག་མེད་ན་སུ་ཞིག་གིས་དེ་ལྟར་དྲན། དྲན་ཞེས་བྱ་བའི་དོན་ཅི་ཡིན། དྲན་པས་ཡུལ་འཛིན་པའོ། །

[Block 4963]
ཅི་དེ་འཛིན་པ་དྲན་པ་ལས་གཞན་ཞིག་ཡིན་ནམ།

[Block 4964 [VERSE]]
འོ་ན་ནི་དྲན་པ༌[^3515]བྱེད་པ་ཡིན་ནོ། །
གང་གིས་དེ་བྱེད་པ་དེ་ནི་བཤད་ཟིན་ཏེ།
དྲན་པའི་རྒྱུ་ནི་སེམས་ཀྱི་ཁྱད་པར་ཡིན་ནོ། །

[Block 4965]
འོ་ན་གང་ནག་པས་དྲན་ནོ་ཞེས་བྱ་བ་ཇི་ལྟ་བུ་ཞེ་ན། ནག་པ་ཞེས་བྱ་བའི་རྒྱུད་དེ་ལས་དེ་སྐྱེ་བར་མཐོང་ནས་སྨྲ་བར་ཟད་དོ། །

[Block 4966 [HEADING]]
#### དྲན་པ་འདི་སུའི་ཡིན་པ། ^6-3-3-0

[Block 4967]
བདག་མེད་པ༌[^3516]ན་དྲན་པ་འདི་སུའི་ཡིན།

[Block 4968]
དྲུག་པ་འདིའི་དོན་ཇི་ལྟ་བུ་ཡིན། རྗེ་བོའི་དོན་ཡིན་ནོ། །

[Block 4969]
དཔེར་ན་གང་གི་རྗེ་བོ་གང་ལྟ་བུ་ཡིན། དཔེར་ན་བའི་ནག་པ་ལྟ་བུ་ཡིན་ནོ། །

[Block 4970]
འདི་ཇི་ལྟར་དེའི་རྗེ་བོ་ཡིན། དེ་རྨོ་བ་དང་བཞོ་བ་ལ་སོགས་པ་ལ་སྦྱོར་བ་དེ་ལ་རག་ལུས་པ་ཡིན་ནོ། །

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
--- END BLOCKS ---
