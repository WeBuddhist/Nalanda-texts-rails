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
རེ་ཞིག་མི་དགེ་བ་ཀུན་དུ་བསྟན་པ་དང་གོམས་པར་བྱས་པ་དང་། ལན་མང་དུ་བྱས་པ་ཐམས་ཅད་ཀྱིས་ནི་དམྱལ་བ་དག་གི་ནང་དུ་སྐྱེ་བར་འགྱུར་ཏེ། འདི་ནི་དེ་དག་གི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 877]
བརྒྱ་ལ་འདི་ལྟ་བུར་མི་རྣམས་དང་སྐལ་བ་མཉམ་པར་འོངས་ན༌[^663]ཡང་སྲོག་གཅོད་པས་ནི་ཚེ་ཐུང་བར་འགྱུར་རོ། །

[Block 878]
མ་བྱིན་པར་ལེན་པས་ནི་ལོངས་སྤྱོད་ཀྱིས་ཕོངས་པར་འགྱུར་རོ། །

[Block 879]
འདོད་པས་ལོག་པར་གཡེམ་པས་ནི་དགྲ་དང་བཅས་པའི་ཆུང་མ་ཅན་དུ་འགྱུར་རོ། །

[Block 880]
བརྫུན་དུ་སྨྲ་བས་ནི་སྐུར་བ་མང་པོར་འགྱུར་རོ། །

[Block 881]
ཕྲ་མས་ནི་དེ་མཛའ་བོ་དང་འབྱེད་པར༌[^664]འགྱུར་རོ། །

[Block 882]
ཚིག་རྩུབ་པོས་ནི་ཡིད་དུ་མི་འོང་བའི་སྒྲ་ཐོས་པར་འགྱུར་རོ། །

[Block 883]
ཚིག་ཀྱལ་པས་ནི་ཚིག་གཟུང་བར༌[^665]མི་འོས་པར་འགྱུར་རོ། །

[Block 884]
བརྣབ་སེམས་ཀྱིས་ནི་འདོད་ཆགས་ཤས་ཆེ་བར་འགྱུར་རོ། །

[Block 885]
གནོད་སེམས་ཀྱིས་ནི་ཞེ་སྡང་ཤས་ཆེ་བར་འགྱུར་རོ། །

[Block 886]
ལོག་པར་ལྟ་བས་ནི་གཏི་མུག་ཤས་ཆེ་བར་འགྱུར་ཏེ།[^666] དེ་ལ་ནི་གཏི་མུག་མང་པོའི༌[^667]ཕྱིར་རོ། །

[Block 887]
འདི་ནི་དེ་དག་གི་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 888]
མི་དག་གི་ནང་ན་ཚེ་ཐུང་བ་ཡང་མི༌[^668]དགེ་བའི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཡིན་ན་དེ་ཇི་ལྟར་སྲོག་གཅོད་པའི་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ཡིན་ཞེ་ན། ཚེ་དེ་ཉིད་དེའི་འབྲས་བུ་ཡིན་ནོ་ཞེས་ནི་མི་ཟེར་རོ། །

[Block 889]
འོ་ན་ཅི་ཞེ་ན། དེས་ཚེ་ཐུང་ངུར་འགྱུར་བས་དེའི་ཕྱིར་སྲོག་གཅོད་པ་ནི་ཚེ་དེའི་བར་ཆད་བྱེད་པའི་ཕྱིར༌[^669]རྒྱུ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 890]
སྲོག་གཅོད་པ་ཧ་ཅང་ཀུན་དུ་བསྟེན་པས་ནི་ཕྱིའི་དངོས་པོ་རྣམས་གཟི་མཐུ་ཆུང་བར་འགྱུར་རོ། །

[Block 891]
མ་བྱིན་པར་ལེན་པས་ནི་སེར་བ་དང་ཆར་པ་མང་བར་འགྱུར་རོ། །

[Block 892]
འདོད་པས་ལོག་པར་གཡེམ་པས་ནི་རྡུལ་གྱིས་འཁྲིག་པར༌[^670]འགྱུར་རོ། །

[Block 893]
བརྫུན་དུ་སྨྲ་བས་ནི་དྲི་ང་བར་འགྱུར་རོ། །

[Block 894]
ཕྲ་མས༌[^671]ནི་མཐོན་དམན༌[^672]ཅན་དུ་འགྱུར་རོ། །

[Block 895]
ཚིག་རྩུབ་པོས་ནི་ས་ཚྭ་སྒོ༌[^673]ཅན་དང་། དགོན་དུང་དང་། ཐ་ཆད་དང་། སྡིག་པ་ཅན་གྱི་སར་འགྱུར་རོ། །

[Block 896]
ཚིག་ཀྱལ་པས་ནི་དུས་ལོག་པ༌[^674]ཅན་དུ་འགྱུར་རོ། །

[Block 897]
བརྣབ་སེམས་ཀྱིས་ནི་འབྲས་བུ་ཕྲ་མོར་འགྱུར་རོ། །

[Block 898]
གནོད་སེམས་ཀྱིས་ནི་འབྲས་བུ་ཁ་བར་འགྱུར་རོ། །

[Block 899]
ལོག་པར་ལྟ་བས་ནི་འབྲས་བུ༌[^675]ཆུང་ངུ་འམ་འབྲས་བུ་མེད་པར་འགྱུར་ཏེ། འདི་ནི་དེ་དག་གི་བདག་པོའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 900]
ཅི་ལས་དེ་ཁོ་ནས་དེ་འདིར་ཚེ་ཐུང་ངུར་འགྱུར་རམ། འོན་ཏེ་གཞན་ཞིག་གིས་ཤེ༌[^676]ན། ཁ་ཅིག་ན་རེ་དེ་ཁོ་ནས་ཏེ། དེ་ནི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་ཡིན་ལ་འདི་ནི་རྒྱུ་མཐུན་པའི་འབྲས་བུ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 901]
གཞན་དག་ན་རེ་དེར་ནི་སྦྱོར་བས་ཡིན་ལ། འདིར་ནི་དངོས་ཀྱིས་ཡིན་ཏེ། འཁོར་དང་བཅས་པ་སྨོས་པའི་ཕྱིར་སྲོག་གཅོད་པས༌[^677]ཞེས་གསུངས་པར༌[^678]ཟད་དོ་ཞེས་ཟེར་རོ། །

[Block 902]
རྒྱུ་མཐུན་པའི༌[^679]འབྲས་བུར་བཤད་པ་གང་ཡིན་པ་དེ་ཡང་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་དང་བདག་པོའི་འབྲས་བུ་དང༌[^680]གཉིས་པོ་འདི་ལས་ནི་མི་འདའི། འདྲ་བའི་ཁྱད་པར་ལས་དེ་སྐད་དུ་བཤད་པར་ཟད་དོ། །

[Block 903]
ཡང་ཅིའི་ཕྱིར་ལས་ཀྱི་ལམ་འདི་དག་གིས༌[^681]འབྲས་བུ་རྣམ་པ་གསུམ་མངོན་པར་འགྲུབ་ཅེ་ན། རེ་ཞིག་སྲོག་གཅོད་པར་བྱེད་པས་ནི་གསད་པར་བྱ་བ་སྡུག་བསྔལ་བསྐྱེད་པ་དང་། གསད་པ་དང་གཟི་བྱིན་མེད་པར་བྱ་བས༌[^682]ཡིན་ཏེ། དེ་ཉིད་ཀྱི་ཕྱིར་འདི།

[Block 904 [VERSE]]
སྡུག་བསྔལ་ཕྱིར་དང་གསད་ཕྱིར་དང་། །
གཟི་བྱིན་མེད་ཕྱིར་འབྲས་རྣམ་གསུམ། །

[Block 905]
ཕ་རོལ་པོ་སྡུག་བསྔལ་བར་བྱས་པའི་ཕྱིར་རྣམ་པར་སྨིན་པའི་འབྲས་བུས་དམྱལ་བ་དག་ཏུ་སྡུག་བསྔལ་མྱོང་བར་འགྱུར་རོ། །

[Block 906]
གསད་པའི་ཕྱིར་རྒྱུ་མཐུན་པའི་འབྲས་བུས་ཚེ་ཐུང་ངུར་འགྱུར་རོ། །

[Block 907]
གཟི་བྱིན་མེད་པར་བྱས་པའི་ཕྱིར་བདག་པོའི་འབྲས་བུས་ཕྱིའི་སྨན་རྣམས་གཟི་མཐུ་ཆུང་བར་འགྱུར་ཏེ། གཞན་དག་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 908]
དགེ་བའི་ལས་ཀྱི་ལམ་རྣམས་ཀྱི་འབྲས་བུ་གསུམ་ཡང་དེ་བཞིན་དུ་རིག་པར༌[^683]བྱ་སྟེ། སྲོག་གཅོད་པ་སྤོང་བ་ཀུན་ཏུ་བསྟེན་པ༌[^684]དང་། གོམས་པར་བྱས་པ་དང་། ལན་མང་དུ་བྱས་པས་ནི་ལྷ་དག་གི་ནང་དུ་སྐྱེས་པར༌[^685]འགྱུར་རོ། །

[Block 909]
བརྒྱ་ལ་འདི་ལྟ་བུར་མི་རྣམས་དང་སྐལ་བ་མཉམ་པར་འོངས་ན་ཡང་ཚེ་རིང་པོར་འགྱུར་ཏེ། ཐམས་ཅད་མི་དགེ་བ་ལས་བཟློག་སྟེ་སྦྱར་བར་བྱའོ། །

[Block 910 [HEADING]]
### ལོག་པའི་འཚོ་བ། ^1-55-0

[Block 911]
བཅོམ་ལྡན་འདས་ཀྱིས་ལོག་པའི་ངག་དང་། ལོག་པའི་ལས་ཀྱི་མཐའ་དང་། ལོག་པའི་འཚོ་བ་ཞེས་གང་གསུངས་པ་དེ་གཉིས་ལས་གཞན་པའི་ལོག་པའི་འཚོ་བ་གང་ཞིག་ཡིན་ཞེ་ན། འདི་གཞན་ནི་མེད་ཀྱི་དེ་ཉིད་ཡིན་ཏེ། ལུས་དང་ངག་ལས་ཆགས་ལས་སྐྱེས། །ལོག་འཚོ། ལུས་དང་ངག་གི་ལས་ཀྱི་མཐའ་ཞེ་སྡང་ལས་སྐྱེས་པ་དང་། གཏི་མུག་ལས་སྐྱེས་པ་ནི་ལོག་པའི་ངག་དང་། ལོག་པའི་ལས་ཀྱི་མཐའ་ཡིན་ནོ། །

[Block 912]
དེ་ནི་སྦྱང་དཀའི་ཕྱིར། དེ་གཉིས་ལས་ལོགས་ཤིག་ཏུ་བསྟན་ཏོ། །

[Block 913]
ཆགས་པའི་ཆོས་ནི་འཕྲོག་པར་བྱེད་པ་ཡིན་པས༌[^686]དེས་ཀུན་ནས་བསླང་བའི་ལས་ལས་སེམས་བསྲུང་བར༌[^687]སླ་བ་མ་ཡིན་ཏེ། དེའི་ཕྱིར་ཇི་སྲིད་འཚོའི་བར་དུ་སྦྱང་དཀའ་བས་བསྒྲིམ་པར་བྱ་བའི་ཕྱིར་དེ་ནི་དེར་ལོགས་ཤིག་ཏུ་བསྟན་ཏོ། །

[Block 914]
འདིར་སྨྲས་པ། རྟག་ཏུ་ལྟ་བ་སྣ་ཚོགས་ཀྱིས།[^688] །

[Block 915 [VERSE]]
ཁྱིམ་པས་ལྟ་བ་སྦྱང་བར་དཀའ། །
གཞན་ལ་འཚོ་བ་རག་ལུས་པའི། །
--- END BLOCKS ---
