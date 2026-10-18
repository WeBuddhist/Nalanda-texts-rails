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
[Block 3886]
བདུན་པ་བཞིན་ནོ། །

[Block 3887 [HEADING]]
##### མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པ། ^4-12-2-1-0

[Block 3888]
[^2750]གནས་དང་གནས་མ་ཡིན་པ་མཁྱེན་པའི་སྟོབས་ཇི་ལྟ༌[^2751]བར། ཀྱེ་མ་ང་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པར་གྱུར་པ་ལ་ཞེས་བྱ་བའི་མི་འཇིགས་པ༌[^2752]འདི་ཡང་དེ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 3889 [HEADING]]
##### ཟག་པ་ཟད་པ། ^4-12-2-2-0

[Block 3890]
ཟག་པ་ཟད་པ་མཁྱེན་པའི་སྟོབས་ཇི་ལྟ་བར༌[^2753]ཀྱེ་མ་ང༌[^2754]ཟག་པ་ཟད་པར་གྱུར་པ་ལ་ཞེས་བྱ་བའི་མི་འཇིགས་པ་འདི་ཡང་དེ་དང་འདྲའོ། །

[Block 3891 [HEADING]]
##### བར་དུ་གཅོད་པའི་ཆོས། ^4-12-2-3-0

[Block 3892]
ལས་བདག་གིར་བྱ་བ་མཁྱེན་པའི་སྟོབས་ཇི་ལྟ་བར་ངས་གང་དག་ཉན་ཐོས་རྣམ༌[^2755]ལ་བར་དུ་གཅོད་པའི་ཆོས་སུ་གསུངས་པ་ལ་ཞེས་བྱ་བའི་མི་འཇིགས་པ༌[^2756]འདི་ཡང་དེ་དང་འདྲའོ། །

[Block 3893 [HEADING]]
##### ངེས་པར་འབྱུང་བའི་ལམ། ^4-12-2-4-0

[Block 3894]
ཀུན་དུ་འགྲོ་བའི་ལམ་མཁྱེན་པའི་སྟོབས་ཇི་ལྟ་བར་ངས་གང་ཉན་ཐོས་རྣམས་ཀྱི་ངེས་པར་འབྱུང་བའི་ལམ་དུ་གསུངས་པ་ལ་ཞེས་བྱ་བའི་མི་འཇིགས་པ༌[^2757]འདི་ཡང༌[^2758]དེ་དང་འདྲ་བར་རིག་པར་བྱའོ། །ཇི་ལྟར་ན་མཁྱེན་པ་ཉིད་མི་འཇིགས་པ་ཡིན་ཞེ་ན། མི་འཇིགས་པ་ནི་མི་སྐྲག་པ་ཡིན་ལ། འདི་དག་གིས་ཀྱང་མི་སྐྲག་པར་འགྱུར་རོ། །ཤེས་པས་བྱས་པ་ནི་མི་འཇིགས་པར་རུང་གི་ཤེས་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 3895 [HEADING]]
#### དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ། ^4-12-3-0

[Block 3896]
དྲན་པ་ཉེ་བར༌[^2759]གཞག་པ་ནི་འཁོར་གྱི་བྱེ་བྲག་ལས་གསུམ་ཡིན་ཏེ།

[Block 3897 [VERSE]]
མདོ་ལས་ཇི་སྐད་འབྱུང་བ་བཞིན་ནོ། །
[^2760]དེ་ཡང་དྲན་པ༌[^2761]ཤེས་རབ་དག་ཉིད༌[^2762]གསུམ། །

[Block 3898]
དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ་པོ་འདི་དག་ནི་དྲན་པ་དང་། ཤེས་བཞིན་གྱི་རང་བཞིན་དག་ཡིན་ནོ། །

[Block 3899]
གང་གི་ཚེ་ཉན་ཐོས་དག༌[^2763]ཀྱང་གུས་པར༌[^2764]ཉན་པ་དང་། གུས་པར་མི་ཉན་པ་དང་། གཉི་ག་ལ་ཀུན་དུ་དགའ་བའམ། ཀུན་ནས་མནར་སེམས་མི་འབྱུང་བ་ན། ཅིའི་ཕྱིར། འདི་དག་སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་རྣམས་ཞེས་བྱ་ཞེ་ན། བག་ཆགས་དང་བཅས་པར་སྤངས་པའི་ཕྱིར་རོ། །

[Block 3900]
ཡང་ན་ཉན་ཐོས་རྣམས་གང༌[^2765]ཡིན་པ་དེ་ལ་ནི་གུས་པར་ཉན་པ་དང་། གུས་པར་མི་ཉན་པ་དང་། གཉིས་པོ་དེ་དག་ལ་ཤིན་ཏུ་ཡང་ཡིད་བདེ་བ་ལ་སོགས་པའི་གོ་སྐབས་སུ་མི༌[^2766]འགྱུར་གྱི། གཞན་ལ་ནི་དེ་ལྟ་མ་ཡིན་པས་དེ༌[^2767]ཁོ་ན་ལ་དེ་མི་འབྱུང་བ་ཡ་མཚན་དུ་རྣམ་པར་གཞག་གི་གཞན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3901 [HEADING]]
#### ཐུགས་རྗེ་ཆེན་པོ། ^4-12-4-0

[Block 3902]
ད་ནི་ཐུགས་རྗེ་ཆེན་པོ་བརྗོད་པར་བྱ་སྟེ། དེ་སྨྲས་པ། ཐུགས་རྗེ་ཆེན་པོ་ཀུན་རྫོབ་བློ། །ཐུགས་རྗེ་ཆེན་པོ་ནི་ཀུན་རྫོབ་ཤེས་པའི་བདག་ཉིད་ཡིན་ནོ། །

[Block 3903]
དེ་ལྟ་མ་ཡིན་ན་སེམས་ཅན་ཐམས་ཅད་ལ་དམིགས་པར་ཡང་མི་འགྲུབ་ལ། སྙིང་རྗེ་བཞིན་དུ་སྡུག་བསྔལ་གསུམ་གྱི་རྣམ་པ་ཅན་དུ་ཡང་མི་འགྲུབ་བོ། །

[Block 3904 [HEADING]]
##### ཐུགས་རྗེ་ཆེན་པོ་ཞེས་བྱ་བ། ^4-12-4-1-0

[Block 3905]
འདི་ཅིའི་ཕྱིར་ཐུགས་རྗེ་ཆེན་པོ་ཞེས་བྱ་ཞེ་ན།

[Block 3906 [VERSE]]
ཚོགས་དང་རྣམ་པ་སྤྱོད་ཡུལ་དང་། །
མཉམ་པའི་ཕྱིར་དང་ཆེས་ཆེའི་ཕྱིར། །

[Block 3907 [HEADING]]
###### ཚོགས། ^4-12-4-1-1-0

[Block 3908]
ཚོགས་ནི་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཆེན་པོས་ཡང་དག་པར་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 3909 [HEADING]]
###### རྣམ་པ། ^4-12-4-1-2-0

[Block 3910]
རྣམ་པ་ནི་སྡུག་བསྔལ་གསུམ་ལ་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 3911 [HEADING]]
###### དམིགས་པ། ^4-12-4-1-3-0

[Block 3912]
དམིགས་པ་ནི་ཁམས་གསུམ་པའི་སེམས་ཅན་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3913 [HEADING]]
###### མཉམ་པ་ཉིད། ^4-12-4-1-4-0

[Block 3914]
མཉམ་པ་ཉིད་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་འདྲ་བར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 3915 [HEADING]]
###### ཆེས་ཆེ་བ་ཉིད། ^4-12-4-1-5-0

[Block 3916]
ཆེས་ཆེ་བ་ཉིད་ནི་དེ་བས༌[^2768]ཆེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 3917 [HEADING]]
##### སྙིང་རྗེ་དང་ཐུགས་རྗེ་ཆེན་པོའི་ཐ་དད། ^4-12-4-2-0

[Block 3918]
སྙིང་རྗེ་དང་ཐུགས་རྗེ་ཆེན་པོ་གཉིས་ལ་ཐ་དད་དུ་བྱ་བ་ནི་ཅི་ཞིག་ཡོད་ཅེ་ན། ཐ་དད་བྱ་བ་རྣམ་པ་བརྒྱད། ངོ་བོ་ཉིད༌[^2769]ལས་ནི་ཞེ་སྡང་མེད་པ་དང་། གཏི་མུག་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3919]
རྣམ་པ་ལས་ནི་སྡུག་བསྔལ་གཅིག་དང་། གསུམ་གྱི་རྣམ་པ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3920]
དམིགས་པ་ལས་ནི་ཁམས་གཅིག་དང་། གསུམ་གྱི་སེམས་ཅན་ལ་དམིགས་པའི་ཕྱིར་རོ། །

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
--- END BLOCKS ---
