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
[Block 3536 [VERSE]]
[^2022]གནམ་འཕང་དང་རྒྱར་ནི་དཔག་ཚད་ཉི་ཁྲིའོ། །
དེའི་འོག་གཞི་ཡང་དེ་དང་འདྲ་སྟེ།
འདི་ནས་ནི་དཔག་ཚད་བཞི་ཁྲི་ཡོད་དོ། །

[Block 3537]
སྡུག་བསྔལ༌[^2023]བར་ཆད་མེད་པས་ན་མནར་མེད་པའོ། །

[Block 3538]
གཞན་དག༌[^2024]ནི་སྡུག་བསྔལ་བར་ཆད་དང་བཅས་པ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། ཡང་སོས་ན་ནི་ལུས་རྣམས་བཅད་ཅིང་ཕུག་ལ་བཏགས་ཀྱང་རླུང་གྲང་མོ་དག༌[^2025]ལངས་ན་སེམས་ཅན་དེ་དག་ཡང་སོས་པར་འགྱུར་བས་དེའི་ཕྱིར་ཡང་སོས་ཡིན་ནོ། །

[Block 3539]
གཞན་དག་ན་རེ་དེ་ན་བདེ་བའི་གནས་སྐབས་མེད་པས་ན་མནར་མེད་པ༌[^2026]སྟེ། གཞན་དག་ན་ཡང་བདེ་བའི་ཚོར་བ་རྣམ་པར་སྨིན་པ་ལས་བྱུང་བ༌[^2027]ནི་མེད་ཀྱི་རྒྱུ་མཐུན་པར༌[^2028]བྱུང་བ་ནི་འགག་པ་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 3540 [HEADING]]
###### དམྱལ་བ་བདུན། ^3-2-1-9-2-0

[Block 3541]
དེ་ཡི་སྟེང་ན་དམྱལ་བ་བདུན། །མནར་མེད་པ་དེའི་སྟེང་ན་དམྱལ་བ་བདུན་པོ་རབ་ཏུ་ཚ་བ་དང་། ཚ་བ་དང་། ངུ་འབོད་ཆེན་པོ་དང་། ངུ་འབོད་དང་། བསྡུས་འཇོམས་དང་། ཐིག་ནག་དང་། ཡང་སོས་དག་གོང་ནས་གོང་དུ་གནས་སོ། །

[Block 3542]
གཞན་དག་ན་རེ་མནར་མེད་པའི་གློ་དག༌[^2029]ན་གནས་སོ་ཞེས་ཟེར་རོ། །

[Block 3543 [HEADING]]
###### ལྷག་པ་བཅུ་དྲུག། ^3-2-1-9-3-0

[Block 3544]
དེ་དག་ཀྱང་། [^2030]བརྒྱད་པོ་ཀུན་ལ་ལྷག་བཅུ་དྲུག །བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 3545 [VERSE]]
དེ་ལྟར་དེ་དག་དམྱལ་བ་ནི། །
བརྒྱད་ཅེས་བྱ་སྟེ་རྒལ་བར༌[^2031]དཀའ། །
དྲག་པོའི་ལས་ཀྱིས་ཀུན་དུ་གང་། །
རེ་རེ་ལ་ཡང་ལྷག་བཅུ་དྲུག །

[Block 3546 [VERSE]]
རྩིག་པ་བཞི་དང་སྒོ་བཞི་སྟེ། །
རྣམ་ཕྱེ་རིས་སུ་ཆད་པ་ཡིན། །
ལྕགས་ཀྱི་ར་བས་ཀུན་དུ་བསྐོར། །
ལྕགས་དག་གིས་ནི་གང་བ་ཡིན། །

[Block 3547 [VERSE]]
དེ་ལ་ལྕགས་འབར་ས་གཞི་སྟེ། །
འབར་བའི་མེ་དང་ལྡན་པ་ཡིན། །
དཔག་ཚད་བརྒྱ་ཕྲག་དུ་མར་ནི། །
མེ་ལྕེ་དག་གིས་ཁྱབ་པར་གནས། །

[Block 3548]
ཞེས་གསུངས་སོ། །

[Block 3549]
ལྷག་མ༌[^2032]བཅུ་དྲུག་གང་ཞེ་ན།

[Block 3550 [VERSE]]
དེ་དག་གི་ནི་ངོས་བཞི་ན། །
མེ་མ་མུར་དང་རོ་མྱགས་དང་། །
སྤུ་གྲི་ལ༌[^2033]སོགས་ཆུ་བོ་ཡིན། །

[Block 3551]
དེ་དག་གི་སྒོ་རེ་རེ་ན་ལྷག་པ་བཞི་བཞི་ཡོད་དེ། མེ་མ་མུར་པུས་མོ་ནུབ་ཙམ་གང་དུ་སེམས་ཅན་དེ་དག་གི་རྐང་པ་བཞག་ན་ནི་པགས་པ་དང་ཤ་དང་ཁྲག་ཞིག་པར་འགྱུར་ལ། རྐང་པ་བཏེག་ན་ནི་པགས་པ་དང་ཤ་དང་ཁྲག་སླར་སྐྱེ་བ་དང་། རོ་མྱགས་རྐྱག་པའི་འདམ་རྫབ་གང་དུ་འབུ་མཆུ་རྣོན་ཞེས་བྱ་བ་ལུས་ཐམས་ཅད་དཀར་ཞིང་མགོ་གནག་ལ་མཆུ་སྨྱུང་བའི་སྲོག་ཆགས་དག་གནས་ཤིང་དེ་དག་གིས་སེམས་ཅན་དེ་དག་གི་རུས་པའི་བར་དུ་འབིགས་པར་བྱེད་པ་དང་། སྤུ་གྲིའི་སོས༌[^2034]གཏམས་པའི་ལམ་པོ་ཆེ་གང་དུ་སེམས་ཅན་དེ་དག་འགྲོ་བ་ན༌[^2035]རྐང་པ་བཞག་ན་ནི་པགས་པ་དང་ཤ་དང་ཁྲག་ཞིག་པར་འགྱུར་ཞེས་བྱ་བ་སྔ་མ་བཞིན་ནོ། །

[Block 3552]
ལོ་མ་རལ་གྲི་ལྟ་བུའི་གནས༌[^2036]གང་དུ་རལ་གྲི་རྣོན་པོ་རྣམས་ལྷུང་ཞིང་། སེམས་ཅན་དེ་དག་གི་ཡན་ལག་དང་ཉིང་ལག་རྣམས་གཅོད་པར་འགྱུར་ཞིང་། ཁྱི་སྲེ་བོ་རྣམས་ཀྱང་ཟ་བར་བྱེད་པ་དང་། ལྕགས་ཀྱི་ཤལ་མ་རི་ནགས་ཚེར་མ་རྣོན་པོ་སོར་བཅུ་དྲུག་པ་གང་དུ་སེམས་ཅན་དེ་དག་འཛེག་པ་ན་ནི་ཚེར་མ་དེ་རྣམས་ཁ་ཐུར་དུ་ལྟ་བར་འགྱུར་ཞིང་ལུས་འབིགས་པར་བྱེད་ལ། འབབ་པ་ན་ནི་ཁ་གྱེན་དུ་ལྟ་བར་འགྱུར་ཞིང་། ཁྭ༌[^2037]ལྕགས་ཀྱི་མཆུ་ཅན་རྣམས་ཀྱིས་མིག་དག་ཕྱུང་ཞིང་ཕྱུང་ནས་ཟ་བར་བྱེད་པ་སྟེ། སྤུ་གྲིའི་ལམ་ལ་སོགས་པ་གསུམ་པོ་དེ་ནི་མཚོན་ཆ་མངོན་པར་འབབ་པ༌[^2038]འདྲ་བའི་ཕྱིར་གཅིག་ཏུ་བྱའོ། །

[Block 3553]
ལྷག་མ༌[^2039]

[Block 3554]
བཞི་པ་ནི་ཆུ་བོ་རབ་མེད་ཐལ་ཆུ་ཁོལ་མས་གང་བ་སྟེ། གང་དུ་སེམས་ཅན་དེ་དག་འགྲམ་གཉིས་ནས༌[^2040]སྐྱེས་བུ་ལག་ན་རལ་གྲི་དང་། མདུང་ཐུང་དང་། ཐག་མདུང་ཐོགས་པ་དག་གིས་འགོག་ཅིང་། དཔེར་ན་ཕྲུ་བ་ཆུ་མང་པོས་བཀང་བ་ཐབ་ཏུ་བཅུག་པའི༌[^2041]ནང་དུ་ཏིལ་དང་འབྲས་ཐུག་པོ་ཆེ་ལ་སོགས་པ་བླུགས་པ་བཞིན་དུ། སྟེང་དུ་འགྲོ་ན་ཡང་གདུ༌[^2042]ཞིང་འཚེད་ལ། འོག་དང་ཐད་ཀར་འགྲོ་ན་ཡང་གདུ༌[^2043]ཞིང་འཚེད་པར་བྱེད་པའོ། །

[Block 3555]
དེས་ཀྱང་དམྱལ་བ་ཆེན་པོ་འོབས་བཞིན་དུ་བསྐོར་རོ། །

[Block 3556]
ལྷག་མ༌[^2044]བཞི་པོ་འདི་དག་ནི་ཕྱོགས་ཀྱི་བྱེ་བྲག་གིས་བཅུ་དྲུག་ཅེས་བྱའོ། །

[Block 3557]
གནོད་པ་ལྷག་མའི༌[^2045]གནས༌[^2046]ཡིན་པའི་ཕྱིར་ལྷག་པའོ༌[^2047]ཞེས་བྱ་སྟེ། དམྱལ་བ་དག་ཏུ་གནོད་པ་བྱས་ནས་ཡང་འདི་དག་ཏུ་གནོད་པར་བྱེད་དོ། །

[Block 3558]
གཞན་དག་ན་རེ་དམྱལ་བ་པའི༌[^2048]འཆིང་བའི༌[^2049]འོག་ཏུ་འདི་དག་ཏུ་བྱིང༌[^2050]བས་ན་ལྷག་པའོ་ཞེས་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 3559]
དྲི་བ་ལས་དྲི་བ་གཞན་འབྱུང་སྟེ། ཅི་དམྱལ་བའི་སྲུང་མ་དེ་དག་སེམས་ཅན་དུ་བགྲང་བ་ཞིག་ཡིན་ནམ། འོན་ཏེ་མ་ཡིན་ཞེ་ན། ཁ་ཅིག་ན་རེ་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3560]
ད་ནི་ཇི་ལྟར་ན་དེ་དག་གཡོ་བ་ཡིན་ཞེ་ན། སེམས་ཅན་རྣམས་ཀྱི་ལས་དག་གིས་ཏེ། འཆགས་པའི་རླུང་བཞིན་ནོ། །

[Block 3561]
འོ་ན་བཙུན་པ་ཆོས་ལྡན་རབ་འབྱོར་གྱིས།

[Block 3562 [VERSE]]
གང་དག་ཁྲོ་ཞིང་གཏུམ་ལས་དང་། །
སྡིག་ལ་མངོན་པར་དགའ་བ་དང་། །
སྡུག་བསྔལ་བ་ལ་དགའ་དེ་དག །
གཤིན་རྗེ་སྲིན་པོར་སྐྱེ་བར་འགྱུར། །

[Block 3563]
ཞེས་གང་བཤད་པ་ཇི་ལྟར་དྲང་ཞེ་ན། གཤིན་རྗེས་བསྒོ་བ་གང་དག་གི༌[^2051]སེམས་ཅན་རྣམས་དམྱལ་བ་དག་ཏུ་ཁྲིད་པར་བྱེད་པ་དེ་དག་གཤིན་རྗེ་སྲིན་པོ་ཞེས་བཤད་ཀྱི། གང་དག་ལས་རྣམ་པར༌[^2052]བྱེད་པ་དེ༌[^2053]ནི་མ་ཡིན་ནོ། །

[Block 3564]
གཞན་དག་ན་རེ་སེམས་ཅན་དག་ཏུ་བགྲང་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3565]
ད་ནི་ལས་དེ་དག་གང་དུ་རྣམ་པར་སྨིན་ཞེ་ན། དམྱལ་བ་དེ་དག་ཉིད་དུ་སྟེ། གང་དག་ཏུ་མཚམས་མེད་པ་བྱེད་པ་རྣམས་ཀྱི་རྣམ་པར་སྨིན་པའི་གོ་སྐབས་ཡོད་པ་དེ་དག༌[^2054]གི་སུ་ཞིག་འགོག་པ། [^2055]མེའི་ནང་ན་གནས་པ་རྣམས་ཇི་ལྟར་མི་ཚིག༌[^2056]ཅེ་ན། མེ་ནི་གདོན་མི་ཟ་བར་ལས་དག་གིས་མཚམས་གཅད་པའི་ཕྱིར་རོ། །

[Block 3566]
ཡང་ན་འབྱུང་བའི་ཁྱད་པར་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 3567]
རེ་ཞིག་དེ་དག་ནི་ཚ་བའི་སེམས་ཅན་དམྱལ་བ་ཆེན་པོ་རྣམས་ཞེས་བྱའོ། །

[Block 3568 [HEADING]]
###### གྲང་བའི་དམྱལ་བ་བརྒྱད། ^3-2-1-9-4-0

[Block 3569]
ཆུ་བུར་ཅན་སོགས་གྲང་བརྒྱད་གཞན། །གཞན་ཡང་གྲང་བའི་དམྱལ་བ་བརྒྱད་དེ། འདི་ལྟ་སྟེ། ཆུ་བུར་ཅན་དང་། ཆུ་བུར་རྡོལ་པ་དང་། སོ་ཐམས་ཐམས་དང་། ཨ་ཆུ་ཟེར་བ་དང་། ཀྱི་ཧུད་ཟེར་བ་དང་། ཨུཏྤལ་ལྟར་གས་པ་དང་། པདྨ་ལྟར་གས་པ་དང་། པདྨ་ལྟར་ཆེར་གས་པའོ། །

[Block 3570]
མིང་འདི་རྣམས་ནི་སེམས་ཅན་གྲང་བ་མི་བཟད་པས་ཉེན་པ་དེ་དག་གི༌[^2057]ལུས་དང་སྒྲ་འགྱུར་བ་དང་སྒྲ་མཐུན་པ་དག་ཡིན་ནོ། །

[Block 3571]
དེ་དག་ཀྱང་འཛམ་བུའི་གླིང་འདི་ཉིད་ཀྱི་འོག་དམྱལ་བ་ཆེན་པོ་རྣམས་ཀྱི་ཐད་ཀ་ན་ཡོད་དོ། །

[Block 3572]
འཛམ་བུའི་གླིང་འདི་ཙམ་གྱི་འོག་ན་མནར་མེད་པ་ལ་སོགས་པའི་གོ་སྐབས་ག་ལ་ཡོད་ཅེ་ན། གླིང་རྣམས་ནི་འབྲུའི་ཕུང་པོ་བཞིན་དུ་ཞབས་རྒྱ་ཆེ་བ་ཡིན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་རྒྱ་མཚོ་ཆེན་པོ་རིམ་གྱིས་གཞོལ་བ་ཡིན་ནོ། །

[Block 3573]
དེ་ལྟར་ན་སེམས་ཅན་དམྱལ་བ་བཅུ་དྲུག་པོ་དེ་རྣམས་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ལས་ཀྱི་དབང་གིས་མངོན་པར་གྲུབ་པ་དག་ཡིན་ནོ། །

[Block 3574 [HEADING]]
###### ཉི་ཚེ་བའི་དམྱལ་བ། ^3-2-1-9-5-0

[Block 3575]
ཉི་ཚེ་བའི་དམྱལ་བ་རྣམས་ནི་མང་པོའམ་གཉིས་སམ་གཅིག་གི་སོ་སོའི་ལས་དག་གིས་མངོན་པར་གྲུབ་པ་ཡིན་ཏེ། དེ་དག་གི་རྣམ་པའི་བྱེ་བྲག་ནི་རྣམ་པ་དུ་མ་ཡོད་དོ། །
--- END BLOCKS ---
