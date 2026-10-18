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
[Block 876]
དྲི་ཞིམ་པོ་ནི་ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པ་དང་ལྡན་པས༌[^766]ཁ་ན་མ་ཐོ་བ་དང་ལྡན་པ་མི་རིགས་པའི༌[^767]ཆོས་དེ་ལ་མེད་པའི་ཕྱིར་ཏེ། དེ་བས་ན་དྲི་ང་བ་སྦྱོང་བ༌[^768]ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 877]
ལས་བཤད་ཟིན་ཏོ།། །།

[Block 878 [HEADING]]
#### ཁྱད་པར། ^2-1-5-0

[Block 879]
ཁྱད་པར་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་བྱམས་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་སྐྱོབ་པ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། ཐམས་ཅད་སྐྱོབ་པ་ཞེས་བྱ་བའི་ཚིག་འདི་ནི་བསྟན་པའོ། །

[Block 880]
ལྷག་མ་རྣམས་ནི་ཇི་ལྟར་བྱམས་པ་སེམས་ཅན་ཐམས་ཅད་སྐྱོབ་པར་བྱེད་པའི་བཤད་པའོ། །

[Block 881]
བདག་གི་བདེ་བ་གཏོང་ཞིང༌[^769]ཞེས་བྱ་བ་ནི་བྱམས་པ་ཆེན་པོ་དང་ལྡན་པ་རྣམས་རྟག་པར་བདག་བདེ་བ་དང་ལྡན་པར་མི་འདོད་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 882]
སེམས་ཅན་རྣམས་ལ་བདེ་བ་སྦྱིན་པའོ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་རྣམས་ཚེ་འདི་དང་ཚེ་རབས་གཞན་ན༌[^770]ཡང་བདེ་བ་ལ་འཇོག་པར་བྱེད་པའི་ཕྱིར་ཏེ། དེ་བས་ན་བྱམས་པ་ཆེན་པོར་འགྱུར་རོ། །

[Block 883]
སེམས་ཅན་རྣམས་ཚེ་འདིར་བདེ་བ་ལ་འཇོག་པ་ནི་ཁ་ན་མ་ཐོ་བ་མེད་པའི་ཟང་ཟིང་གི་བདེ་བ་ཐམས་ཅད་དང་ལྡན་པར་བྱས་པས་སོ། །

[Block 884]
སེམས་ཅན་རྣམས་ཚེ་རབས་གཞན་དུ་བདེ་བ་ལ་འཇོག་པ་ནི་སེམས་ཅན་རྣམས་ཚེ་རབས་གཞན་དུ་ལྷ་དང་མིའི་བདེ་འགྲོ་བྱས་པའི་ཕྱིར་རོ། །

[Block 885]
ཉན་ཐོས་རྣམས་ཀྱི་བྱམས་པ་ནི་བདག་སྐྱོབ་པའོ་ཞེས་བྱ་བ་ལ། དེ་དག་གི་བྱམས་པ་ནི་བདག་འཁོར་བ་ལས་ཐར་པར་བྱེད་པ་ཙམ་ལས་གཞན་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 886]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བྱམས་པ་ཆེན་པོ་ནི་སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་སྐྱོབ་པ་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བྱམས་པས་ནི་སེམས་ཅན་ཐམས་ཅད་འཁོར་བའི་སྡུག་བསྔལ་དང་ངན་སོང་གི་སྡུག་བསྔལ་ལས་འབྱིན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 887]
བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་བྱམས་པ་ནི་ཆུ་བོ་ལས་སྒྲོལ་བའོ་ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བྱམས་པ་ནི་ཞེས་བྱ་བར་སྦྱར་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་བྱམས་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ཆུ་བོ་བཞི་ལས་བསྒྲལ་ནས་མྱ་ངན་ལས་འདས་པའི་གནས་སུ་འཇོག་པར་བྱེད་པའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 888]
ཁྱད་པར་བཤད་ཟིན་ཏོ།། །།

[Block 889 [HEADING]]
#### རབ་ཏུ་དབྱེ་བ། ^2-1-6-0

[Block 890]
རབ་ཏུ་དབྱེ་བ༌[^771]བསྟན་པའི་ཕྱིར། འདི་ལྟར་བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། བྱང་ཆུབ་སེམས་དཔའི་བྱམས་པ་ཕྱེ་ན༌[^772]རྣམ་པ་གསུམ་དུ་འགྱུར་རོ། །

[Block 891 [HEADING]]
##### སེམས་ཅན་ལ་དམིགས་པའི་བྱམས་པ། ^2-1-6-1-0

[Block 892]
བྱང་ཆུབ་སེམས་དཔའི་བྱམས་པ་གང་གིས་དམིགས་པའི་ཡུལ་གང་ལ་དམིགས་པ་བསྟན་པའི་ཕྱིར་དེ་ལ་སེམས་ཅན་ལ་དམིགས་པའི་བྱམས་པ་ནི། སེམས་དང་པོ་བསྐྱེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སེམས་དང་པོ་བསྐྱེད་པའི༌[^773]བྱང་ཆུབ་སེམས་དཔའ་ནི་དང་པོ་སོ་སོའི་སྐྱེ་བོའི་དུས་ན་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་ཡན་ཆད་མོས་པས་སྤྱོད་པའི་ས་ལ་གནས་པ་རྣམས་སོ། །

[Block 893]
དེའི་ཚེ་ན་སེམས་ཅན་ཐམས་ཅད་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་འགོད་པར༌[^774]བྱའོ་ཞེས་སེམས་ཅན་གྱི་དངོས་པོ་ཡོད་པར་ལྟ་བའི་ཕྱིར་སེམས་ཅན་ལ་དམིགས་པ་ཞེས་བྱའོ། །

[Block 894 [HEADING]]
##### ཆོས་ལ་དམིགས་པའི་བྱམས་པ། ^2-1-6-2-0

[Block 895]
ཆོས་ལ་དམིགས་པའི་བྱམས་པ་ནི་སྤྱོད་པ་ལ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་ཞེས་བྱ་བ་ལ། ས་དང་པོ་ཡན་ཆད་ས་བདུན་པ་མན་ཆད་ནི་སྤྱོད་པ་ལ་ཞུགས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཞེས་བྱ་སྟེ། དེའི་ཚེ་ས་དང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ལ་སོགས་པའི་ཆོས་ཐམས་ཅད་སྦྱོང་ཞིང་སྤྱོད་པས་སྤྱོད་པ་ལ་ཞུགས་པ་ཞེས་བྱའོ། །

[Block 896]
དེ་དག་གི་བྱམས་པ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་དེ་དག་ལ་དམིགས་པའི་ཕྱིར་ཆོས་ལ་དམིགས་པའོ། །

[Block 897 [HEADING]]
##### དམིགས་པ་མེད་པའི་བྱམས་པ། ^2-1-6-3-0

[Block 898]
དམིགས་པ་མེད་པའི་བྱམས་པ་ནི་མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ཐོབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སྟེ་ཞེས་བྱ་བ་ལ། མི་སྐྱེ་བའི་ཆོས་ལ་བཟོད་པ་ནི་ས་བརྒྱད་པ་ཡན་ཆད་ལ་བྱ་སྟེ། དེ་དག་གི་མཚན་མ་མེད་པ་ལ་ལྷུན་གྱིས་གྲུབ་པར་འཇུག་པས་དེ་དག་གི་བྱམས་པ་ནི་གོང་དུ་སྨོས་པའི་སེམས་ཅན་དང་ཆོས་གཉི་ག་ཡང་དོན་དམ་པར་མ་བྱུང་མ་སྐྱེས་པར༌[^775]རྟོགས་པས་དེ་དག་ལ་མི༌[^776]དམིགས་པའི་ཕྱིར་དམིགས་པ་མེད་པའོ། །

[Block 899]
གལ་ཏེ་དེ་ལྟར་གཉི་གར་མི་དམིགས་ན་ཇི་ལྟར་བྱམས་པར་འགྱུར་ཞེ་ན། དོན་དམ་པར་དེ་ལྟར་མི་དམིགས་ཀྱང་ཀུན་རྫོབ་ཏུ་སེམས་ཅན་ལ་མ༌[^777]དམིགས་པར་འདྲ་བར་སྣང་བས་བྱམས་པ་ཞེས་བཏགས་པ་ལ་ཉེས་པ་མེད་དོ། །

[Block 900]
བྱམས་པ་མི་ཟད་པ་བཤད་ཟིན་ཏོ།། །།

[Block 901 [HEADING]]
### སྡུག་བསྔལ་གྱིས་གདུངས་པ། ^2-2-0

[Block 902]
སྡུག་བསྔལ་གྱིས་གདུངས་པའི༌[^778]བྱང་ཆུབ་སེམས་དཔའི་དབང་དུ་བྱས་ནས། བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་གཞན་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དེ་ཡང་རྣམ་པ་བཞིར་རིག་པར་བྱའོ། །

[Block 903]
བཞི་གང་ཞེ་ན། སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཀྱི་མཆོག་ཏུ་གྱུར་པ་དང་། ངེས་པའི་ཚིག་དང་། རྒྱུ་དང་། རང་བཞིན་དང་། ལས་སོ། །

[Block 904]
དེ་ལ་བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། སེམས་ཅན་ཐམས་ཅད་ལ་སྙིང་ཐག་པ་ནས་སྡུག་པར་འཛིན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་ཆོས་ཐམས་ཅད་ཀྱི་མཆོག་ཏུ་གྱུར་པ་བསྟན་ཏོ། །

[Block 905]
བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་སྙིང་རྗེ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། གཞན་གྱི་སྐབས་མི་རྙེད་བས་ན་སྙིང་རྗེ་ཆེན་པོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^779]ངེས་པའི་ཚིག་བསྟན་ཏོ། །

[Block 906]
གཡོ་མེད་པ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཚུལ་ཁྲིམས་འཆལ་བའི་སེམས་ཅན་རྣམས་ལ་བལྟའོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^780]རྒྱུ་དང་རང་བཞིན་བསྟན་ཏོ།[^781] །བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་དེ་ལྟར་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། སོ་སོར༌[^782]ཉེ་བར་གནས་པ་ལས་བྱུང་བས་ན་དེའི་ཕྱིར་སྙིང་རྗེ་ཆེན་པོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་ལས་བསྟན་ཏོ། །

[Block 907 [HEADING]]
#### ཆོས་ཐམས་ཅད་ཀྱི་མཆོག་ཏུ་གྱུར་པ། ^2-2-1-0

[Block 908]
བྱམས་པ་དང་སྙིང་རྗེ་གཉིས་ལ་ཐ་དད་པར་བྱ་བ་ཅི་ཡོད་ཅེ་ན། [^783]བྱམས་པ་ནི་སེམས༌[^784]ཅན་བདེ་བ་ལ་བཀོད༌[^785]པའོ། །

[Block 909]
སྙིང་རྗེ་ནི་སེམས་ཅན་གྱི་སྡུག་བསྔལ་སེལ་བ་སྟེ། དེ་བས་ན་མདོ་ལས་ཀྱང་། བྱང་ཆུབ་སེམས་དཔའ་སྙིང་རྗེ་དང་ལྡན་པ་ནི་གཞན་སྡུག་བསྔལ་བས་སྡུག་བསྔལ་བའོ་ཞེས་གསུངས་སོ། །

[Block 910]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་མི་ཟད་པ་ཡིན་པའི་རྒྱུ་འདྲི་བའི་ཚིག་སྟེ།[^786] བྱང་ཆུབ་སེམས་དཔའི༌[^787]སྙིང་རྗེ་ཅིའི་ཕྱིར་མི་ཟད་པ་ཡིན་ཞེ་ན༌[^788]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 911]
ལན་དུ་སྔོན་དུ་འགྲོ་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་གསུངས་ཏེ། སངས་རྒྱས་ཀྱི་ཆོས་བྱེད་དོ་ཅོག་ཐམས་ཅད་བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་གི་དོན་སྒྲུབ་པའི་ཕྱིར་མ་ཡིན་གྱི། མཐའ་ཡས་པའི་སེམས་ཅན་རྣམས་འཁོར་བའི་དགོན་པ་ན་འཁྱམས་པ༌[^789]རྣམས་ལ་ཐུགས་བརྩེ་སྟེ། དེ་དག་བསྒྲལ་བའི་ཕྱིར་སངས་རྒྱས་སུ་བསྒྲུབས་པས༌[^790]དེ་དག་གི་རྒྱུ་སྙིང་རྗེ་ཆེན་པོ་ཡིན་པའི་ཕྱིར་སྔོན་དུ་འགྲོ་བ༌[^791]ཞེས་བྱ༌[^792]སྟེ། དེ་བས་ན་འབྲས་བུ་མི་ཟད་པས་རྒྱུ་ཡང་མི་ཟད་པའོ། །

[Block 912]
གཉིས་སུ་ན་བྱང་ཆུབ་སེམས་དཔའི་ཡོན་ཏན་ནོ། །

[Block 913]
ཚོགས་ཀྱི་ནང་ན་སྙིང་རྗེ་གཙོ་བོ་ཡིན་པས་ཐོག་མར་འགྲོ་བའོ༌[^793]ཞེས་བྱ༌[^794]སྟེ། སྲོག་གི་དབང་པོ་ལ་སོགས་པའི་དཔེས་བསྟན་པ་ལྟ་བུའོ། །

[Block 914]
ཆོས་ཐམས་ཅད་ཀྱི་མཆོག་ཏུ་གྱུར་པ་བཤད་ཟིན་ཏོ།། །།

[Block 915 [HEADING]]
#### ངེས་པའི་ཚིག། ^2-2-2-0
--- END BLOCKS ---
