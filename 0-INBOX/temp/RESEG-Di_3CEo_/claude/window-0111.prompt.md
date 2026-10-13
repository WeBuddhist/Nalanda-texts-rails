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

[Block 3891]
ས་བདུན་ལས་རྒྱལ་མངོན་ཤེས་དང་།

[Block 3892 [VERSE]]
མི་གཡོ་འཐོབ༌[^1520]དང་སྤེལ་བསྒོམ་པའི། །
བར་ཆད་མེད་པའི་ལམ་དག་དང་། །
གོང་མའི་གྲོལ་བའི་ལམ་བརྒྱད་ལའང་། །

[Block 3893]
ས་བདུན་ནི་བསམ་གཏན་བཞི་དང་། གཟུགས་མེད་པ་གསུམ་མོ། །

[Block 3894]
དེ་དག་ལས་འདོད་ཆགས་དང་བྲལ་བ་དང་། མངོན་པར་ཤེས་པ་ལྔ་དང་། མི་གཡོ་བ༌[^1521]རྟོགས་པར་བྱེད་པ་དང་། བསམ་གཏན་སྤེལ་མར་བསྒོམ་པ་སློབ་པ་བར་ཆད་མེད་པའི་ལམ་ཇི་སྙེད་པ་དེ་ཐམས་ཅད་ལ་ཤེས་པ་བདུན་འཐོབ་སྟེ། དེ་དག་ཉིད་དོ། །

[Block 3895]
མི་གཡོ་བ་རྟོགས་པར་བྱེད་པ་ལ་ནི་ཀུན་རྫོབ་ཤེས་པ་ནི་མི་འཐོབ་སྟེ། དེར་ནི་ཟད་པ་ཤེས་པ་བདུན་པ་ཡིན་ནོ། །

[Block 3896]
སྲིད་པའི་རྩེ་མོའི་འདོད་ཆགས་དང་བྲལ་བའི་རྣམ་པར་གྲོལ་བའི་ལམ་བརྒྱད་ལ་ཡང་ཤེས་པ་བདུན་པོ་ཁོ་ན་འཐོབ་སྟེ། གཞན་གྱི་སེམས་ཤེས་པ་ནི་བདུན་པ་ཡིན་ལ་ཀུན་རྫོབ་ཤེས་པ་ནི་མ་ཡིན་ཏེ། སྲིད་པའི་རྩེ་མོའི་གཉེན་པོ་མ༌[^1522]ཡིན་པའི་ཕྱིར་རོ། །

[Block 3897 [VERSE]]
སློབ་པ་སྦྱོང་བའི་གྲོལ་བ་ལ། །
ཤེས་པ་དྲུག་དང་བདུན་འཐོབ་བམ། །

[Block 3898]
སློབ་པ་སྦྱོང་བའི་རྣམ་པར་གྲོལ་བའི་ལམ་ལ་འདོད་ཆགས་དང་བཅས་པས་ནི་དྲུག་འཐོབ་བོ། །

[Block 3899]
འདོད་ཆགས་དང་བྲལ་བ་ལ་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ནི་བདུན་པ་ཡིན་ནོ། །

[Block 3900]
བར་ཆད་མེད་པའི་ལམ་ལ་དྲུག །སློབ་པ་སྦྱོང་བའི་བར་ཆད་མེད་པའི༌[^1523]ལམ་ལ་དྲུག་འཐོབ་བོ། །

[Block 3901]
དེ་བཞིན་སྲིད་རྩེའི་ལམ༌[^1524]རྒྱལ་ལའང་། །སྲིད་པའི་རྩེ་མོ་ལས་འདོད་ཆགས་དང་བྲལ་བའི་བར་ཆད་མེད་པའི་ལམ་ལ་ཡང་དེ་བཞིན་དྲུག་འཐོབ་པོ། །ཟད་པ་ཤེས་པ་ལ་དགུའོ། །

[Block 3902]
མི་སྐྱེ་བ་ཤེས་པ་ལས་གཞན་པ༌[^1525]རྣམས་སོ། །

[Block 3903]
མི་གཡོ་བས་ནི་བཅུ་འཐོབ་པོ། །མི་གཡོ་བའི་ཆོས་ཅན་གང་ཡིན་པ་དེས་ནི་བཅུ་ཆར་འཐོབ་བོ། །

[Block 3904]
དེར་འཕོ་གྲོལ་བའི་ཐ་མ་ལའང་།[^1526] །གང་ཞིག་མི་གཡོ་བ་ཉིད་དུ་འཕོ་བ་དེའི་རྣམ་པར་གྲོལ་བའི་ལས༌[^1527]ཐ་མ་ལ༌[^1528]ཡང་བཅུ་འཐོབ་པོ། །བཤད་པའི་ལྷག་མ་ལ་བརྒྱད་འཐོབ། །ལྷག་མ་ཡང་གང་ཞིག་ཅེ་ན། འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བའི་རྣམ་པར་གྲོལ་བའི་ལམ་དགུ་པ་དང་། ས་བདུན་པ་ལས་འདོད་ཆགས་དང་བྲལ་བ་དང་། མངོན་པར་ཤེས་པ་དང་སྤེལ་མར་བསྒོམ་པ་དག་གི་རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་དང་། མི་གཡོ་བ་རྟོགས་པར་བྱེད་པའི་རྣམ་པར་གྲོལ་བའི་ལམ་བརྒྱད་དང་། འདོད་ཆགས་དང་བྲལ་བའི་སྦྱོར་བ་དང་། ཁྱད་པར་ཅན་གྱི་ལམ་ཐམས་ཅད་དེ། དེ་དག་ཐམས་ཅད་ལ་ནི་ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་མ་གཏོགས་པ་ཤེས་པ་བརྒྱད་མ་འོངས་པ་འཐོབ་པོ། །ཡང་ལམ་གང་ལས་དུ་བའི་ཤེས་པ་འཐོབ་ཅེ་ན། རེ་ཞིག་ཀུན་རྫོབ་ཤེས་པ་ནི་ལམ་ས་གང་པ༌[^1529]ཡིན་པ་དང་།

[Block 3905]
དང་པོ་ཉིད་དུ་ས་གང་ཐོབ་པ༌[^1530]ས་དེ་པའི་མ་འོངས་པ་འཐོབ་བོ། །

[Block 3906]
ཟག་པ་མེད་པ་ནི་ལམ་ས་གང་ཡིན་པ་འབའ་ཞིག་ཏུ་ཡང་མ་ཟད་དེ། འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 3907 [VERSE]]
གང་ལས་ཆགས་བྲལ་བྱ་ཕྱིར་གང་། །
ཐོབ་པ་དེར་ཡང་འོག་མའང༌[^1531]འཐོབ། །

[Block 3908]
ས་གང་ལས་འདོད་ཆགས་དང་བྲལ་བར་བྱ་བ་ལ་ཡང་སྦྱོར་བའི་ལམ་ལ་སོགས་པ་རྣམ་པ་གཉིས་ཡིན་ལ། འདོད་ཆགས་དང་བྲལ་བས་ས་གང་ཞིག་འཐོབ་པ་དེའི་ས་པ་དང་ས་འོག་མའི་ཟག་པ་མེད་པའི་ཤེས་པ་རྣམས་ཐོབ་པར་འགྱུར་རོ། །

[Block 3909]
ཟད་པ་ཤེས་ལ་ཟག་བཅས་ཀྱང་། །ཟད་པ་ཤེས་པ་ལ་ནི་ཟག་པ་དང་བཅས་པའི་ཡོན་ཏན་མི་སྡུག་པ་དང་། དབུགས་འབྱུང་བ་དང་། རྔུབ་པ་དྲན་པ་དང་། དྲན་པ་ཉེ་བར་གཞག་པ་དང་། ཚད་མེད་པ་དང་། རྣམ་པར་ཐར་པ་ལ་སོགས་པ་གང་ཇི་སྙེད༌[^1532]པ་དེ་ཐམས་ཅད་འཐོབ་བམ་ཞེ་ན།

[Block 3910 [VERSE]]
གང་སྔོན་མེད་པ་དེ་སྙེད༌[^1533]ཀྱི། །
ས་ཀུན་སྔོན་སྙེད༌[^1534]མི་འཐོབ་བོ། །

[Block 3911]
གང་རྣམ་པར་ཉམས་པ་ལས་གང་རྙེད་པ་དེ་ཡང་མི་འཐོབ་སྟེ། འཐོབ་པ༌[^1535]བཏང་བའི་ཕྱིར་རོ། །ཅི་ཐོབ་པ་རྙེད་པ་ཁོ་ན་ཡིན་ནམ༌[^1536]ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 3912 [HEADING]]
##### ཐོབ་པ་རྣམ་པ་བཞི། ^7-4-9-1-0

[Block 3913]
ཐོབ་པ་ནི་རྣམ་པ་བཞི་སྟེ། དེ་ལ།

[Block 3914 [VERSE]]
རྙེད་དང་བསྟེན་ཞེས་བྱ་བ་ནི། །
དགེ་བ་འདུས་བྱས་ཐོབ་པའོ། །
གཉེན་པོ་དང་ནི་ཐག་བསྲིང་བའི། །
ཐོབ་པ་ཟག་དང་བཅས་པ་ཡིན།

[Block 3915]
རྙེད་པ་དང་། བསྟེན་པས་ཐོབ་པ་དག་ནི་དགེ་བ་དང་འདུས་བྱས་རྣམས་ཀྱི་ཡིན་ཏེ། མ་འོངས་པ་རྣམས་ཀྱི་གཅིག་གོ། །

[Block 3916]
ད་ལྟར་བྱུང་བ་རྣམས་ཀྱི་གཉིས་ཀའོ། །

[Block 3917]
གཉེན་པོ་དང་ཐག་བསྲིང་བའི་ཐོབ་པ་དག་ནི་ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 3918]
གང་ཟག་ཐམས་ཅད་ཀྱི་ཟད་པ་ཤེས་པའི་ཡོན་ཏན་ཐོབ་པའི་ཕྱིར༌[^1537]བཤད་ཀྱི།

[Block 3919 [HEADING]]
### སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་བཅོ་བརྒྱད། ^7-5-0

[Block 3920 [VERSE]]
སངས་རྒྱས་ཆོས་ནི་མ་འདྲེས་པ། །
སྟོབས་ལ་སོགས་པ་བཅོ་བརྒྱད་དོ། །

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
--- END BLOCKS ---
