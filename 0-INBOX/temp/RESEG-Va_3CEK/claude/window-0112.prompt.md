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
ས་ལས་ནི་བསམ་གཏན་བཞི་དང་། བསམ་གཏན་བཞི་པའི་ས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3922]
རྒྱུད་ལས་ནི་ཉན་ཐོས་ལ་སོགས་པ་དང་། སངས་རྒྱས་ཀྱི་རྒྱུད་ལས་སྐྱེ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3923]
ཐོབ་པ་ལས་ནི་འདོད་པའི་ཁམས་དང་། སྲིད་པའི་རྩེ་མོ་ལས་འདོད་ཆགས་དང་བྲལ་བས་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 3924]
ཡོངས་སུ་མི་སྐྱོབ་པ་དང་། ཡོངས་སུ་སྐྱོབ་པ་དང་། མི་འདྲ་བ་དང་འདྲ་བར་ཐུགས་རྗེ་མཛད་པའི་ཕྱིར་རོ། །

[Block 3925 [HEADING]]
#### སངས་རྒྱས་ཐམས་ཅད་མཉམ་པ་ཉིད། ^4-12-5-0

[Block 3926]
ཅི་སངས་རྒྱས་ཐམས་ཅད་རྣམ་པ་ཐམས་ཅད་ཀྱིས་མཉམ་པ༌[^2770]ཡིན་ནམ་ཞེ་ན།

[Block 3927 [VERSE]]
སངས་རྒྱས་ཐམས་ཅད་ཚོགས་དང་ནི། །
ཆོས་སྐུ་འགྲོ་བའི་དོན་སྤྱོད་པས། །
མཉམ་པ་ཉིད་དེ་སྐུ་ཚེ་དང་། །
རིགས་དང་སྐུ་བོང་ཚོད་ཀྱིས་མིན། །

[Block 3928]
སངས་རྒྱས་ཐམས་ཅད་ནི་རྒྱུ་གསུམ་པོ་སྔོན་གྱི་བསོད་ནམས་དང་། ཡེ་ཤེས་ཀྱི་ཚོགས་ཀྱིས༌[^2771]ཡང་དག་པར་འགྲུབ་པ་དང་། ཆོས་ཀྱི་སྐུ་ཡོངས་སུ་འགྲུབ་པ་དང་། འཇིག་རྟེན་གྱི་དོན་སྤྱོད་པས༌[^2772]མཉམ་པ་ཉིད་ཡིན་ནོ། །

[Block 3929]
སྐུ་ཚེ་དང་། རིགས་དང་། གདུང་དང་། སྐུ་བོང་ཚོད་དུ་མཛད་པ་ལ་ནི་བྱེ་བྲག་ཡོད་དེ་དུས་ཇི་ལྟ་བ་བཞིན་དུ་ཡུན་ཤིན་ཏུ་རིང་བ་དང་། ཐུང་ངུར་འཚོ་བའི་ཕྱིར་དང་། རྒྱལ་རིགས་དང་། བྲམ་ཟེའི་རིགས་ཐ་དད་པའི་ཕྱིར་དང་། འོད་སྲུངས་དང་ཤཱཀྱ་ལ་སོགས་པ་གདུང་ཐ་དད་པའི་ཕྱིར་དང་། སྐུ་བོང་ཚོད་ཆུང་བ་དང་། ཆུང་བ་མ་ཡིན་པ་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 3930 [HEADING]]
#### ཕུན་སུམ་ཚོགས་པ། ^4-12-6-0

[Block 3931 [HEADING]]
##### རྒྱུ་ཕུན་སུམ་ཚོགས་པ། ^4-12-6-1-0

[Block 3932]
ཕུན་སུམ་ཚོགས་པ་རྣམ་པ་གསུམ་པོ་འདི་ཁོ་ན་ཡིད་ལ་བྱེད་པ༌[^2773]མཁས་པས་ནི། སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ལ་དགའ་བ་དང་། གུས་པ་ཆེན་པོ་སྐྱེད་པར་ནུས་ཏེ། འདི་ལྟ་སྟེ། རྒྱུ་ཕུན་སུམ་ཚོགས་པ་དང་། འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་དང་། ཕན་འདོགས་པ་ཕུན་སུམ་ཚོགས་པ་དང་། ཡེ་ཤེས་ཕུན་སུམ་ཚོགས་པའོ།[^2774] །དེ་ལ་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་ནི། རྣམ་པ་བཞི་སྟེ། བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཐམས་ཅད་ལ་གོམས་པ་དང་། ཡུན་རིང་པོ་ནས་གོམས་པ་དང་། བར་ཆད་མེད་པར་གོམས་པ་དང་། གུས་པར་བྱས་ཏེ་གོམས་པའོ། །

[Block 3933 [HEADING]]
##### འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ། ^4-12-6-2-0

[Block 3934]
འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་ཡང་རྣམ་པ་བཞི་སྟེ། ཡེ་ཤེས་ཕུན་སུམ་ཚོགས་པ་དང་། སྤང་བ༌[^2775]ཕུན་སུམ་ཚོགས་པ་དང་། མཐུ་ཕུན་སུམ་ཚོགས་པ་དང་། གཟུགས་ཀྱི་སྐུ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3935 [HEADING]]
##### ཕན་འདོགས་པ་ཕུན་སུམ་ཚོགས་པ། ^4-12-6-3-0

[Block 3936]
ཕན་འདོགས་པ་ཕུན་སུམ་ཚོགས་པ་ཡང༌[^2776]རྣམ་པ་བཞི་སྟེ། ངན་སོང་གསུམ་དང་འཁོར་བའི་སྡུག་བསྔལ་ལས་གཏན་དུ༌[^2777]ཐར་བར༌[^2778]མཛད་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3937]
ཡང་ན་ཐེག་པ་གསུམ་དང་བདེ་འགྲོ་ལ་འགོད་པར་མཛད་པ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3938 [HEADING]]
##### ཡེ་ཤེས་ཕུན་སུམ་ཚོགས་པ། ^4-12-6-4-0

[Block 3939]
ཡེ་ཤེས་ཕུན་སུམ་ཚོགས་པ་ཡང་རྣམ་པ་བཞི་སྟེ། མ་བསྟན་པར་མཁྱེན་པ་དང་། ཐམས་ཅད་མཁྱེན་པ་དང་། རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་དང་། མ་འབད་པར་མཁྱེན་པའོ། །

[Block 3940 [HEADING]]
##### སྤངས་པ་ཕུན་སུམ་ཚོགས་པ། ^4-12-6-5-0

[Block 3941]
སྤངས་པ་ཕུན་སུམ་ཚོགས་པ༌[^2779]ཡང་རྣམ་པ་བཞི་སྟེ། ཉོན་མོངས་པ་ཐམས་ཅད་སྤངས་པ་དང་། གཏན་དུ་སྤངས་པ་དང་། བག་ཆགས་དང་བཅས་ཏེ་སྤངས་པ་དང་། ཏིང་ངེ་འཛིན་དང་སྙོམས་པར་འཇུག་པའི་སྒྲིབ་པ་ཐམས་ཅད་སྤངས་པའོ། །

[Block 3942 [HEADING]]
##### མཐུ་ཕུན་སུམ་ཚོགས་པ། ^4-12-6-6-0

[Block 3943]
མཐུ་ཕུན་སུམ་ཚོགས་པ་ཡང་རྣམ་པ་བཞི་སྟེ། ཕྱིའི་ཡུལ་སྤྲུལ་པ་དང་། ཡོངས་སུ་བསྒྱུར་བ་དང་། [^2780]སྐུ་ཚེ་གཏོང་བ་དང་། བྱིན་གྱིས་རློབ་པའི་མངའ་ཕུན་སུམ་ཚོགས་པ་དང་། སྒྲིབ་པ་དང་ནམ་མཁའ་དང་ཤིན་ཏུ་རིང་བ་ལ་མྱུར་དུ་གཤེགས་པ་དང་། ཆུང་ངུར༌[^2781]མང་པོ་འཇུག་པར་མཛད་པའི་མངའ་ཕུན་སུམ་ཚོགས་པ་དང་། ཡ་མཚན་གྱི་ཆོས་ནར་མ་རྣམ་པ་སྣ་ཚོགས་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3944 [HEADING]]
##### གཟུགས་ཀྱི་སྐུ་ཕུན་སུམ་ཚོགས་པ། ^4-12-6-7-0

[Block 3945]
གཟུགས་ཀྱི་སྐུ་ཕུན་སུམ་ཚོགས་པ་ཡང་རྣམ་པ་བཞི་སྟེ། མཚན་ཕུན་སུམ་ཚོགས་པ་དང་། དཔེ་བྱད་བཟང་པོ་ཕུན་སུམ་ཚོགས་པ་དང་། སྟོབས་ཕུན་སུམ་ཚོགས་པ་དང་། སྐུ་གདུང་རྡོ་རྗེ་ལྟར་སྲ་བ་ཉིད༌[^2782]ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3946]
དེ་ལྟར་ན་དེ་དག་ནི་སངས་རྒྱས་རྣམས་ཀྱི་ཆེ་བའི་བདག་ཉིད་མདོར་བསྡུས་པ་ཡིན་ནོ། །

[Block 3947]
དེ་དབྱེ་ན་ནི་མཐའ་ཡས་པར་འགྱུར་ཏེ། དེ་ཡང་བཅོམ་ལྡན་འདས་རྣམས་ཁོ་ན༌[^2783]ནས་གལ་ཏེ་སྐུ་ཚེ་བསྐལ་པ་གྲངས་མེད་པ་དུ་མར་བྱིན་གྱིས་བརླབས་པར༌[^2784]གྱུར་ན་མཐའ་དག་མཁྱེན་པ་དང་བརྗོད་པར་སྤྱོད་དོ། །

[Block 3948]
རེ་ཞིག་དེ་ལྟར་ན་དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་ཡོན་ཏན་དང་ཡེ་ཤེས་དང་མཐུ་དང་ཕན་འདོགས་པ་མཐའ་ཡས་ཤིང་རྨད་དུ་བྱུང་བ་ནི༌[^2785]རིན་པོ་ཆེ་ཆེན་པོའི་འབྱུང་གནས་ཡིན་ནོ། །

[Block 3949]
འོན་ཀྱང་བྱིས་པ་རང་ཉིད་ཡོན་ཏན་དབུལ་བས་མོས་པ་བཅོམ༌[^2786]པ་རྣམས་ནི་ཡོན་ཏན་འབྱོར་པ་དེ་ལྟ་བུ་དེ་ཐོས་སུ༌[^2787]ཟིན་ཀྱང་སངས་རྒྱས་དང་དེའི་ཆོས་ལ་གུས་པར་མི་བྱེད་ཀྱི། མཁས་པ་རྣམས་ནི་རྐང་ཡན་ཆད་ནས་ཀྱང་། བཅོམ་ལྡན་འདས་དེ་དང་དེའི་ཆོས་ལ་མངོན་པར་རབ་ཏུ་དང་བར་འགྱུར་ཏེ། གཅིག་ཏུ་རབ་ཏུ་དང་བ་དེ་དག་ནི་དང་བ་ཙམ་གྱིས་ཀྱང་རྣམ་པར་སྨིན་པར་མ་ངེས་པའི་སྡིག་པའི་ཚོགས་རྣམས་ཟིལ་གྱིས་མནན་ཏེ་ལྷ༌[^2788]དང་མིའི་ལེགས་པ་ཉམས་སུ་མྱོང་ནས་བགྲོད༌[^2789]པར་བྱ་བའི་མཆོག་མྱ་ངན་ལས་འདས་པར་འགྱུར་རོ། །

[Block 3950]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་བསོད་ནམས་ཀྱི་ཞིང༌[^2790]བླ་ན་མེད་པ་ཞེས་བྱ༌[^2791]སྟེ། འབྲས་བུ་མེད་པ་མ་ཡིན་པ་དང་། ཡིད་དུ་འོང་བ༌[^2792]དང་། མཆོག་ཏུ་གྱུར་པ་དང་། མྱུར་བ་དང་། མཐའ་བཟང་བའི་ཕྱིར་རོ། །

[Block 3951]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་།

[Block 3952 [VERSE]]
གང་དག་རྒྱལ་བ་རྣམ་འདྲེན་ལ། །
བྱ་བ་ཆུང་ངུ་བྱེད་འགྱུར་བའང་། །
དེ་དག་མཐོ་རིས་སྣ་ཚོགས་དག །
བགྲོད་ནས་བདུད་རྩིའི་གོ་འཕང་འཐོབ། །

[Block 3953]
ཅེས་གསུངས་སོ། །

[Block 3954]
རེ་ཞིག་དེ་དག་ནི་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་བཅོ་བརྒྱད་ཅེས་བྱའོ། །

[Block 3955 [HEADING]]
### ཉན་ཐོས་དང་ཐུན་མོང་བའི་ཡོན་ཏན། ^4-13-0

[Block 3956]
ཆོས་གཞན་སློབ་དང་ཐུན་མོང་མིན།[^2793] །སངས་རྒྱས་རྣམས་ཀྱི་ཡོན་ཏན་གཞན་དག་ནི་ཉན་ཐོས་དང་ཐུན་མོང་ཡིན་ནོ། །

[Block 3957]
ཁ་ཅིག་སོ་སོའི་སྐྱེ་བོ་དང་། དེ་དག་ཀྱང་གང་ཞེ་ན། ཅི་རིགས་པར།

[Block 3958 [VERSE]]
ཉོན་མོངས་མེད་དང་སྨོན་ནས་ཤེས། །
སོ་སོ༌[^2794]ཡང་དག་རིག་སྔོན༌[^2795]སོགས། །

[Block 3959]
ཉོན་མོངས་པ་མེད་པ་དང་། སྨོན་ནས་ཤེས་པ་དང་། སོ་སོ་ཡང་དག་པར་རིག་པ་དང་། མངོན་པར་ཤེས་པ་དང་། བསམ་གཏན་དང་། གཟུགས་མེད་པ་དང་། ཚད་མེད་པ་དང་། རྣམ་པར་ཐར་པ་དང་། ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་དང་། ཟད་པར་གྱི་སྐྱེ་མཆེད་ལ་སོགས་པའོ། །

[Block 3960 [HEADING]]
#### ཉོན་མོངས་པ་མེད་པ། ^4-13-1-0
--- END BLOCKS ---
