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
[Block 3851]
ཆོས་བཅུ་པོ་འདི་དག་ཇི་ལྟར་སྦྱར་བར་བྱ་ཞེ་ན། ཤེས་པ་གང་གི་དམིགས་པ་དུ་ཞིག་ཡིན་ཞེས་སྦྱར་བར་བྱ་ཞེ་ན། དེ་ལ་ཀུན་རྫོབ་ཤེས་པའི་དམིགས་པ་ནི་ཆོས་བཅུ་པོ་ཐམས་ཅད་ཡིན་ནོ། །

[Block 3852]
ཆོས་ཤེས་པའི་ནི་ལྔ་སྟེ། འདོད་པ་ན་སྤྱོད་པ་དང་། ཟག་པ་མེད་པ་བཞི་དང་། འདུས་མ་བྱས་དགེ་བ་ཡིན་ནོ། །

[Block 3853]
རྗེས་སུ་ཤེས་པ་ནི་བདུན་ཏེ། གཟུགས་དང་། གཟུགས་མེད་པ་ན༌[^1507]སྤྱོད་པ་དང་། ཟག་པ་མེད་པ་དྲུག་དང་། འདུས་མ་བྱས་དགེ་བ་ཡིན་ནོ། །

[Block 3854]
སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་ཤེས་པ་དག་གི་ནི་དྲུག་སྟེ། འདོད་པ་དང་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་རྣམས་སོ། །

[Block 3855]
འགོག་པ་ཤེས་པ་ནི་གཅིག་སྟེ།

[Block 3856 [VERSE]]
འདུས་མ་བྱས་དགེ་བ་ཁོ་ནའོ། །
ལམ་ཤེས་པ་ནི་གཉིས་ཏེ།
ཟག་པ་མེད་པ་དག་གོ། །

[Block 3857]
གཞན་གྱི་སེམས་ཤེས་པ་ནི་གསུམ་སྟེ། འདོད་པ་ན་སྤྱོད་པ་དང་། གཟུགས་ན་སྤྱོད་པ་དང་། ཟག་པ་མེད་པར་མཚུངས་པར་ལྡན་པ་རྣམས་སོ། །

[Block 3858]
ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་དག་གི་དམིགས་པ་ནི་ཆོས་དགུ་སྟེ། འདུས་མ་བྱས་ལུང་དུ་མ་བསྟན་པ་མ་གཏོགས་སོ། །

[Block 3859 [HEADING]]
#### ཤེས་པ་གཅིག་གིས་ཐམས་ཅད་ཤེས་པ། ^7-4-7-0

[Block 3860]
ཤེས་པ་གཅིག་གིས་ཐམས་ཅད་ཤེས་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན། མེད་དོ། །

[Block 3861]
འོན་ཀྱང་།

[Block 3862 [VERSE]]
ཀུན་རྫོབ་གཅིག་པུས་རང་ཚོགས་ལས། །
གཞན་ནི་བདག་མེད་ཉིད་རིག༌[^1508]འགྱུར། །

[Block 3863]
ཀུན་རྫོབ་ཤེས་པས་ནི་རང་གི་ཚོགས་ལས་གཞན་པའི་ཆོས་ཐམས་ཅད་ནི་བདག་མེད་པའོ་ཞེས་བདག་མེད་པ་ཉིད་དུ་ཤེས་པར་འགྱུར་རོ། །

[Block 3864]
དེ་ནི་རྫོགས་སོ། །

[Block 3865 [HEADING]]
#### ཤེས་པ་དུ་དང་ལྡན་པ། ^7-4-8-0

[Block 3866]
གང་ཞིག་ཤེས་པ་དུ་དང་ལྡན་པ་ཞེས་བྱ་བ་འདི་བརྗོད་པར་བྱ་སྟེ། རེ་ཞིག་སོ་སོའི་སྐྱེ་བོ་ནི་ཀུན་རྫོབ་ཤེས་པ་གཅིག་པུ་དང་ལྡན་ནོ། །

[Block 3867]
འདོད་ཆགས་དང་བྲལ་བ་ཞིག་ཡིན་ན་ནི་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་དང་ཡང་ངོ་། །འཕགས་པ་ནི།

[Block 3868 [VERSE]]
ཟག་མེད་སྐད་ཅིག་དང་པོ་ལ། །
ཆགས་བཅས་ཤེས་པ་གཅིག་དང་ལྡན། །

[Block 3869]
འདོད་པ་ལས་འདོད་ཆགས་དང་མ་བྲལ་བ་ཞིག་ཡིན་ན་སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་ལ་ཀུན་རྫོབ་ཤེས་པ་གཅིག་ཁོ་ན་དང་ལྡན་ནོ། །

[Block 3870]
གཉིས་པ་ལ་གསུམ། སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པ་ལ་ནི་ཀུན་རྫོབ་ཤེས་པ་དང་། ཆོས་ཤེས་པ་དང་། སྡུག་བསྔལ་ཤེས་པ་སྟེ་གསུམ་དང་ངོ་། །ཡན་ཆད་ནི། བཞི་ལ་རེ་རེ་འཕེལ་དང་ལྡན། །སྡུག་བསྔལ་ལ་རྗེས་སུ་ཤེས་པ་ལ་ནི་རྗེས་སུ་ཤེས་པ་འཕེལ་ལ། ཀུན་འབྱུང་བ་དང་། འགོག་པ་དང་། ལམ་ལ་ཆོས་ཤེས་པ་རྣམས་ལ་ནི་དེ་དག་ཁོ་ན་འཕེལ་ལོ། །

[Block 3871]
འདོད་ཆགས་དང་བྲལ་བ་ཞིག་ཡིན་ན་ནི་ཐམས་ཅད་དུ་གཞན་གྱི་སེམས་ཤེས་པ་ལྷག་པར་ལྡན་པར་རིག་པར་བྱའོ། །

[Block 3872 [HEADING]]
#### གནས་སྐབས་གང་དུ་ཤེས་པ་དུ་ཞིག་འཐོབ་པ། ^7-4-9-0

[Block 3873]
ཡང་གནས་སྐབས་གང་དུ་ཤེས་པ་དུ་ཞིག་འཐོབ་ཅེ་ན།

[Block 3874 [VERSE]]
མཐོང་བའི་ལམ་ལ་བཟོད་པ་དང་། །
ཤེས་པ་ཇི་ལྟར་སྐྱེས་པ་རྣམས། །

[Block 3875]
མ་འོངས་པ་འཐོབ། མཐོང་བའི་ལམ་ལ་བཟོད་པའམ་ཤེས་པ་གང་དང་གང་སྐྱེས་པ༌[^1509]དང་འདྲ་བ་མ་འོངས་པ་དེའི་རྣམ་པ་བཞི་ཁོ་ན་འཐོབ་པར༌[^1510]འགྱུར་རོ། །

[Block 3876]
དེ་ཉིད་ལ། རྗེས་གསུམ་ལ་ནི་ཀུན་རྫོབ་ཀྱང་། །མཐོང་བའི་ལམ་དེ་ཉིད་ལ་སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་བ་དང་། འགོག་པ་ལ་རྗེས་སུ་ཤེས་པ་གསུམ་ལ་ཀུན་རྫོབ་ཤེས་པ་ཡང་འཐོབ་བོ། །

[Block 3877]
ཆོས་ཤེས་པ་ལ་ནི་མ་ཡིན་ཏེ། བདེན་པ་ཟད་པར་མངོན་པར་མ་གཏོགས་པའི་ཕྱིར་རོ། །

[Block 3878]
དེའི་ཕྱིར༌[^1511]མངོན་རྟོགས་མཐའ་ཞེས་བྱ། །དེ་ཉིད་ཀྱི་ཕྱིར་ཀུན་རྫོབ་ཤེས་པ་དེ་ནི་མངོན་པར་རྟོགས་པའི་མཐའ་ལས་འབྱུང༌[^1512]བའོ། །

[Block 3879]
དེ་རེས་འགའ༌[^1513]མངོན་སུམ་དུ་བྱེད་དམ་ཞེ་ན། ནམ་ཡང་མི་བྱེད། དེ་མཐའ་གཅིག་ཏུ། དེ་ནི་མི་སྐྱེའི་ཆོས་ཅན་ཡིན། །ས་དུ་པའི་ཀུན་རྫོབ་ཤེས་པ་དེ་འཐོབ་ཅེ་ན། མཐོང་བའི་ལམ་གྱིས་ནི། རང་དང་འོག་ས། མཐོང་བའི་ལམ་ས་གང་ཡིན་པའི་ས་དེ་བ་དང་། འོག་མའི་ཀུན་རྫོབ་ཤེས་པ་འཐོབ་སྟེ། གལ་ཏེ་མི་ལྕོགས་པ༌[^1514]མེད་པའི་ས་པ་ཞིག་ཡིན་ན་ནི་དེ་ཉིད་ཀྱི་ས་པ་དང་།

[Block 3880]
འདོད་པ་ན་སྤྱོད་པ་འཐོབ་པོ། །གཞན་ལ་ཡང་དེ་བཞིན་ནོ། །

[Block 3881]
དེ་ཡང་དྲན་པ་ཉེ་བར་གཞག་པ་དུ་དག་གཅིག༌[^1515]ཡིན་ཞེ་ན། འགོག་པའི་མཐའ། འགོག་པ༌[^1516]མངོན་པར་རྟོགས་པ་ལས་ཆོས་དྲན་པ་ཉེ་བར་གཞག་པའོ། །

[Block 3882]
ལྷག་མ་དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་ཆར་རོ། །

[Block 3883]
དེ་ཡང་འདི་མངོན་པར་རྟོགས་པའི་མཐའ་ལས་བྱུང་བ་ནི། རང་བདེན་རྣམ༌[^1517]ཅན་འབད་ལས་བྱུང་། །བདེན་པ་གང་ཞིག་མངོན་པར་རྟོགས་པས་ཐོབ་པ་དེ་ནི་བདེན་པའི་རྣམ་པ་ཅན་ཁོ་ནའོ། །

[Block 3884]
མཐོང་ལམ་གྱིས་ཐོབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་སྦྱོར་བ་ལས་བྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 3885]
ཆགས་བཅས་བཅུ་དྲུག་པ་ལ་དྲུག །འདོད་ཆགས་དང་མ་བྲལ་བ་ལ་ནི་ལམ་ལ་རྗེས་སུ་ཤེས་པའི་སྐད་ཅིག་མ་ལ་ཤེས་པ་གཉིས་པ༌[^1518]ད་ལྟར་བྱུང་བ་ཡིན་ཏེ། ལམ་ཤེས་པ་དང་། ལམ་ལ་རྗེས་སུ་ཤེས་པའོ། །

[Block 3886]
མ་འོངས་པ་དྲུག་འཐོབ་སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་དང་། འགོག་པ་དང་། ལམ་ཤེས་པ་རྣམས་སོ། །

[Block 3887]
འདོད་ལ་ཆགས་དང་བྲལ་བ་བདུན། །

[Block 3888]
བདུན་པ་ནི་ཕ་རོལ་གྱི་སེམས་ཤེས་པའོ། །

[Block 3889 [VERSE]]
དེ་ཡི་གོང་མ་ཆགས་བཅས་ཀྱིས།[^1519] །
བསྒོམ་པའི་ལམ་ལ་བདུན་ཐོབ་པོ། །

[Block 3890]
སྐད་ཅིག་མ་བཅུ་དྲུག་གི་གོང་མ་ཇི་སྲིད་དུ་འདོད་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་མ་ཡིན་པ་དེ་སྲིད་དུ་སྦྱོར་བ་དང་བར་ཆད་མེད་པ་དང་རྣམ་པར་གྲོལ་བ་དང་། ཁྱད་པར་གྱི་ལམ་ཐམས་ཅད་ལ་ཤེས་པ་བདུན་འཐོབ་སྟེ། དྲུག་པོ་དང་། ཀུན་རྫོབ་ཀྱི་ཤེས་པ་བདུན་པ་ཡིན་ནོ། །
--- END BLOCKS ---
