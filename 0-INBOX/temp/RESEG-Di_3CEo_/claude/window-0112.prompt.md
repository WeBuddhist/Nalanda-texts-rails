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
[Block 3921]
སྟོབས་བཅུ་དང་། མི་འཇིགས་པ་བཞི་དང་། དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ་དང་། ཐུགས་རྗེ་ཆེན་པོ་སྟེ། འདི་རྣམས་བཅོམ་ལྡན་འདས་ཀྱི་ཟད་པ་མཁྱེན་པ་ཁོ་ནས་བརྙེས་པར༌[^1538]འགྱུར་རོ། །

[Block 3922 [HEADING]]
#### སྟོབས་བཅུ། ^7-5-1-0

[Block 3923]
དེ་ལ་གནས་དང་གནས་མིན་ཤེས་པ་བཅུ། །ལས་འབྲས་ལ་བརྒྱད། ལས་དང་རྣམ་པར་སྨིན་པ་མཁྱེན་པའི༌[^1539]སྟོབས་ནི་ཤེས་པ་བརྒྱད་དེ། འགོག་པ་དང་། ལམ་ཤེས་པ་དག་མ་གཏོགས་སོ། །

[Block 3924]
བསམ་གཏན་སོགས། དབང་པོ་མོས་དང་ཁམས་དང་ལ༌[^1540]ནི། དགུའོ། །

[Block 3925]
བསམ་གཏན་དང་། རྣམ་པར་ཐར་པ་དང་། ཏིང་ངེ་འཛིན་དང་། སྙོམས་པར་འཇུག་པ་མཁྱེན་པའི་སྟོབས་ནི་ཤེས་པ་དགུ་སྟེ། འགོག་པ་ཤེས་པ་མ་གཏོགས་པའོ། །

[Block 3926]
དབང་པོ་མཆོག་དང་མཆོག་མ་ཡིན་པ་མཁྱེན་པའི་སྟོབས་དང་། མོས་པ་སྣ་ཚོགས་མཁྱེན་པའི་སྟོབས་དང་། ཁམས་སྣ་ཚོགས་མཁྱེན་པའི་སྟོབས་ཀྱང་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 3927]
ལམ་དག་ལ་བཅུའམ། འམ་གྱི་སྒྲ་ལས་དགུ་ཞེས་པ་ཡང་ངོ་། །གལ་ཏེ་ལམ་དེ་འབྲས་བུ་དང་བཅས་པར་གཟུང་ན་ནི་ཤེས་པ་བཅུའོ། །

[Block 3928]
གལ་ཏེ་མ་ཡིན་ན་ནི་དགུ་སྟེ། དེ་དག༌[^1541]ཁོ་ནའོ། །

[Block 3929]
གཉིས་ནི་ཀུན་རྫོབ་ཤེས་པ་ཡིན། །སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་མཁྱེན་པའི་སྟོབས་དང་། འཆི་འཕོ་དང་སྐྱེ་བ་མཁྱེན་པའི་སྟོབས་དག་ནི་ཀུན་རྫོབ་ཤེས་པའོ། །

[Block 3930]
ཟད་པ་དྲུག་གམ་བཅུ་ཡིན་ནོ། །

[Block 3931]
ཟག་པ་ཟད་པའམ་མཁྱེན་པའི་སྟོབས་ནི་ཤེས་པ་དྲུག་སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། འགོག་པ་ཤེས་པ་དང་། ཟད་པ་ཤེས་པ་དང་། མི་སྐྱེ་བ་ཤེས་པ་དང་། ཀུན་རྫོབ་ཤེས་པ་རྣམས་ཏེ། གལ་ཏེ་ཟག་པ་ཟད་པ་འགོག་པ་ཤེས་པ་ཁོ་ན་ཞིག་ཡིན་ནམ། [^1542]འོན་ཏེ་ཟད་པ་ཤེས་པ་ཟག་པ་ཟད་པའི་ཤེས་པའི༌[^1543]རྒྱུད་ལ་ཡོད་པ་ཡིན་ན་ནི་དེས་ན༌[^1544]ཤེས་པ་བཅུ་ཡིན་ནོ།[^1545] །

[Block 3932 [VERSE]]
རང་བཞིན་བཤད་ནས་ས་བརྗོད་པ། །
སྔོན་གནས་འཆི་འཕོ་སྐྱེ་བའི་སྟོབས། །

[Block 3933]
བསམ་གཏན་དག་ན། སྔོན་གྱི་གནས་དང་། འཆི་འཕོ་བ་དང་། སྐྱེ་བ་མཁྱེན་པའི་སྟོབས་ནི་བསམ་གཏན་བཞིའི་ས་པའོ། །

[Block 3934]
ལྷག་མ་ནི། ས་རྣམས་ཀུན་ན། དེ་དག་ཀྱང་འདོད་པའི་ཁམས་དང་། མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་དང་། གཟུགས་མེད་པ་དག་སྟེ་བཅུ་གཅིག་གོ། །ཤེས་པ་རྣམ་པ་བཅུ་པོ་དེ་ཉིད་གཞན་གྱི་སྟོབས་ཞེས་མི་བྱའི། སངས་རྒྱས་ཁོ་ནའི་སྟོབས་ཞེས་བྱ་སྟེ། ཅིའི་ཕྱིར། འདི་སྟོབས་གང་ཕྱིར་ཐོགས་མི་མངའ། །གང་གི་ཕྱིར་འདིའི་མཁྱེན་པ་ཤེས་བྱ་ཐམས་ཅད་ལ་ཐོགས་པ་མི་མངའ་བར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 3935]
རེ་ཞིག་དེ་ལྟར་ན་མཁྱེན་པ་ཐོགས་པ་མི་མངའ་བའི་ཕྱིར་སངས་རྒྱས་རྣམས་ཀྱི་ཡིད་ཀྱི་སྟོབས་ནི་ཤེས་བྱ་བཞིན་དུ་མཐའ་ཡས་པ་ཡིན་ནོ། །

[Block 3936]
སྐུ་ལ་སྲེད་མེད་བུ་ཡི་སྟོབས། །གཞན་དག་ཚིགས་ན། གཞན་དག་ན་རེ་ཚིགས༌[^1546]དང་ཚིགས་ན་སྲེད་མེད་ཀྱི་བུའི་སྟོབས་མངའོ་ཞེས་ཟེར་རོ། །

[Block 3937]
སྲེད་མེད་ཀྱི་བུའི་སྟོབས་ཀྱི་ཚད་ཇི་ཙམ་ཞེ༌[^1547]ན། གླང་ཆེན་སོགས། །བདུན་ཅུས་ལྷག་པའི་སྟོབས་ཡིན་ནོ། །

[Block 3938]
གླང་པོ་ཆེ་ཕལ་པ་དང་། སྟོབས་ཀྱི་གླང་པོ་ཆེ་དང་། ཚན་པོ་ཆེ་དང་། རབ་གནོན་དང་། ཡན་ལག་མཆོག་དང་། སྟོབས་མཆོག་དང་། སྲེད་མེད་ཀྱི་བུ་རྣམས་གོང་མས༌[^1548]གོང་དུ་བཅུ་འགྱུར་དུ་བསྐྱེད་དེ་བརྗོད་པར་བྱའོ། །

[Block 3939]
དེ་ནི་རེག་བྱའི་སྐྱེ་མཆེད་དོ། །

[Block 3940]
ལུས་ཀྱི་སྟོབས་དེ་ནི་ཐམས་ཅད་ཀྱང་རེག་བྱའི་སྐྱེ་མཆེད་ཀྱི་རང་བཞིན་འབྱུང་བ་ཆེན་པོའི་ཁྱད་པར་ཁོ་ནར་རིག་པར་བྱའོ། །

[Block 3941]
སྟོབས་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 3942 [HEADING]]
#### མི་འཇིགས་པ་བཞི། ^7-5-2-0

[Block 3943]
མི་འཇིགས་པ་ནི་རྣམ་པ་བཞི། །མདོ་ལས་ཇི་སྐད་དུ་འབྱུང་བ་བཞིན་ནོ། །

[Block 3944]
དེ་དག་ཀྱང་།

[Block 3945 [VERSE]]
ཇི་ལྟར་སྟོབས་ནི་དང་པོ་དང་། །
བཅུ་པ་གཉིས་པ་བདུན་པ་བཞིན། །

[Block 3946]
སྟོབས་དང་པོ་ཇི་ལྟ་བར། ཀྱེ་མ་ང་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པར་གྱུར་པ་ལ་ཞེས་བྱ་བའི་མི་འཇིགས་པ་འདི་ཡང་དེ་དང་འདྲའོ། །

[Block 3947]
ཟག་པ་ཟད་པ་མཁྱེན་པའི་སྟོབས་ཇི་ལྟ་བར་ཀྱེ་མ་ང་ཟག་པ་ཟད་པར་གྱུར་པ་ལ་ཞེས་བྱ་བའི་མི་འཇིགས་པ་འདི་ཡང་དེ་དང་འདྲའོ། །

[Block 3948]
ལས་བདག་གིར་བྱ་བ་མཁྱེན་པའི་སྟོབས་ཇི་ལྟ་བར་ངས་གང་དག་བར་དུ་གཅོད་པར་འགྱུར་བའི་ཆོས་གསུངས་པ་ལ་ཞེས་མི་འཇིགས་པ༌[^1549]ཡང་དེ་དང་འདྲའོ། །

[Block 3949]
ཀུན་དུ་འགྲོ་བའི་ལམ་མཁྱེན་པའི་སྟོབས་ཇི་ལྟ་བར་ངས་གང་ཉན་ཐོས་རྣམས་ཀྱི་ངེས་པར་འབྱུང་བའི་ལམ་དུ་གསུངས་པ་ལ་ཞེས་བྱ་བའི་མི་འཇིགས་པ་འདི་ཡང་དེ་དང་འདྲའོ། །

[Block 3950 [HEADING]]
#### དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ། ^7-5-3-0

[Block 3951]
དྲན་པ་ཉེ་བར་གཞག་པ་ནི་འཁོར་གྱི་བྱེ་བྲག་ལས་གསུམ་ཡིན་ཏེ། མདོ་ཇི་ལྟ་བར་དེ་ཡང་། དྲན་དང་ཤེས་བཞིན་བདག་ཉིད་གསུམ། དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ་པོ་འདི་དག་ནི་དྲན་པ་དང་ཤེས་བཞིན་གྱི་བདག་ཉིད་ཡིན་ནོ། །

[Block 3952 [HEADING]]
#### ཐུགས་རྗེ་ཆེན་པོ། ^7-5-4-0

[Block 3953]
ཐུགས་རྗེ་ཆེན་པོ་ཀུན་རྫོབ་བློ། །ཐུགས་རྗེ་ཆེན་པོ་ནི་ཀུན་རྫོབ་ཤེས་པའི་བདག་ཉིད་དོ། །ཅིའི་ཕྱིར་ཐུགས་རྗེ་ཆེན་པོ་ཞེས་བྱ་ཞེ་ན།

[Block 3954 [VERSE]]
ཚོགས་དང་རྣམ་པ་སྤྱོད་ཡུལ་དང་། །
མཉམ་པའི་ཕྱིར་དང་ཆེས་ཆེའི་ཕྱིར། །

[Block 3955]
ཚོགས་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཆེན་པོས་ཡང་དག་པར་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 3956]
རྣམ་པ་ནི་སྡུག་བསྔལ་གསུམ་ལ་རྟོག་པའི་ཕྱིར་རོ། །

[Block 3957]
དམིགས་པ་ནི་ཁམས་གསུམ་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3958]
མཉམ་པ་ཉིད་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་འདྲ་བར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 3959]
ཆས༌[^1550]ཆེ་བ་ཉིད་ནི་དེ་ལས་ཆེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 3960]
སྙིང་རྗེ་དང་། ཐུགས་རྗེ་ཆེན་པོ་གཉིས་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཡོད་ཅེ་ན། ཐ་དད་བྱ་བ་རྣམ་པ་བརྒྱད། །ངོ་བོ་ཉིད་ལས་ནི་ཞེ་སྡང་མེད་པ་དང་།
--- END BLOCKS ---
