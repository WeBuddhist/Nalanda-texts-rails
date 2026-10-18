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
[Block 771 [HEADING]]
### ལས་ཀྱི་ལམ་ཞེས་བྱ་བའི་དོན། ^1-49-0

[Block 772]
ལས་ཀྱི་ལམ་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། འདི་ལ། གསུམ་མམ་བདུན་ནི་ལས་ཀྱང་ཡིན། །བརྣབ་སེམས་ལ་སོགས་པ་གསུམ་ནི་ལས་ཀྱི་ལམ་ཡིན་པས་ལས་ཀྱི་ལམ༌[^557]དག་ཡིན་ནོ། །

[Block 773]
དེ་དག་དང་མཚུངས་པར་ལྡན་པ་ཅན་གྱི་སེམས་པ་ནི་དེ་དག་གི་རྒྱུ་བས་རྒྱུ་སྟེ། དེ་དག་གི་དབང་གིས་དེ་བཞིན་དུ་མངོན་པར་འདུ་བྱེད་པའི་ཕྱིར་དེ་དག་གི་འགྲོས་ཀྱིས་འགྲོའོ། །

[Block 774]
སྲོག་གཅོད་པ་ལ་སོགས་པ་བདུན་ནི་ལུས་དང་ངག་གི་ལས་ཡིན་པའི་ཕྱིར་ལས་ཀྱང་ཡིན་ལ༌[^558]ལས་ཀྱི་ལམ་ཡིན་པས་ལས་ཀྱི་ལམ་ཡང་ཡིན་ཏེ། དེ་དག་ཀུན་ནས་སློང་བའི་སེམས་པ་ནི་དེ་དག་ལ་བརྟེན་ནས་འཇུག་པའི་ཕྱིར་རོ། །

[Block 775]
དེ་ལྟར་ན་ལས་ཀྱི་ལམ་དང་། ལས་དང་ལས་ཀྱི་ལམ་ཡིན་པས་ན་ལས་ཀྱི་ལམ་སྟེ། མི་འདྲ་བ་རྣམས་ལ་ཡང་གཅིག་བསྡུས་པར༌[^559]འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 776]
བརྣབ་སེམས་མེད་པ་ལ་སོགས་པ་དང་། སྲོག་གཅོད་པ་སྤོང་བ་ལ་སོགས་པ་ཡང་དེ་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 777]
ཅིའི་ཕྱིར་སྦྱོར་བ་དང་མཇུག་དག་ལས་ཀྱི་ལམ་མ་ཡིན་ཞེ་ན། འདི་ལྟར་དེ་དག་གི༌[^560]དེའི་དོན་དང་། དེའི་རྩ་བ་ཅན་དུ་འཇུག་པ་ཡིན་ནོ། །

[Block 778]
སྔར་ཡང་ཆེ་ལོང་བསྡུས་པའི་ཕྱིར་ཞེས་བཤད་པ་ཡང་ཡིན་ནོ། །

[Block 779]
འཇིག་རྟེན་ན་གང་དག་འཕེལ་བ་དང་འགྲིབ་པས་ཕྱི་ནང་གི་དངོས་པོ་རྣམས་འཕེལ་བ་དང་འགྲིབ་པ༌[^561]ཡང་ཡིན་ནོ། །

[Block 780]
འོ་ན་མདོ་སྡེ་པ་གང་དག་བརྣབ་སེམས་པ༌[^562]ལ་སོགས་པ་ཁོ་ན་ཡིད་ཀྱི་ལས་སུ་འདོད་པ་དེ་དག་གི་ལྟར་ན་དེ་དག་ཇི་ལྟར་ལས་ཀྱི་ལམ་ཡིན་ཞེ་ན། དེ་དག་ཉིད་ལ་དྲིས་ཤིག །དེ་ལྟ་མོད་ཀྱི་བརྗོད་པར་ནུས་ཏེ། དེ་དག་ནི༌[^563]བདེ་འགྲོ་དང་ངན་འགྲོ་རྣམས་ཀྱི་ལས་ཀྱང༌[^564]ཡིན་ལ་ལམ་ཡང་ཡིན་པས་ལས་ཀྱི་ལམ་ཡིན་པའམ། ཡང་ན་གཅིག་གིས་གཅིག་འདྲེན་པས་ན་ལས་ཀྱི་ལམ་ཡིན་ནོ། །

[Block 781 [HEADING]]
### དགེ་བའི་རྩ་བ་གཅོད་པ། ^1-50-0

[Block 782]
མི་དགེ་བའི་ལས་ཀྱི་ལམ་བཅུ་པོ་གང་དག་ཡིན་པ་དེ་དག་ཐམས་ཅད་ཀྱང་དགེ་བའི་ཆོས་རྣམས་ཀུན་ཏུ་སྤྱོད་པ་དང་འགལ་བ་ཡིན་ལ། མེད་པར་ལྟ་བས༌[^565]རྩ་བ་གཅོད། །དགེ་བའི་རྩ་བ་གཅོད་པ་ནི་ལོག་པར་ལྟ་བ་ཆེན་པོ་ཡོངས་སུ་རྫོགས་པར་གཅོད་དོ། །

[Block 783]
འོ་ན་ཅིའི་ཕྱིར་བསྟན་བཅོས་ལ་མི༌[^566]དགེ་བའི་རྩ་བ་ཆེན་པོ་རྣམས་གང་དག་ཡིན་ཞེ་ན། མི་དགེ་བའི་རྩ་བ་གང་དག་གིས་དགེ་བའི་རྩ་བ་གཅོད་པར་བྱེད་པ་དང་། འདོད་པ་ལ༌[^567]འདོད་ཆགས་དང་བྲལ་བ་ཐོབ་པར་བྱེད་པ་ན་དང་པོ་ཉིད་དུ་སྤོང་བ༌[^568]དག་ཡིན་པའོ་ཞེས་བཤད་ཅེ་ན། ལོག་པར་ལྟ་བ་མི་དགེ་བའི་རྩ་བས་དྲངས་པའི་ཕྱིར་དེ་དག་ཁོ་ན་ལ་ལས་ཀྱི་ལམ་དེ་བསྟན་པར་མཛད་དེ། དཔེར་ན་མེ༌[^569]ཁོ་ནས་གྲོང་སྲེག་པར་བྱེད་ན་རྐུན་པོ་རྣམས་མེ་དེ༌[^570]འདྲེན་པ༌[^571]བྱེད་པ་ཡིན་པས་རྐུན་པོ་རྣམས་ཀྱིས་གྲོང་བསྲེགས་སོ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 784]
དགེ་བའི་རྩ་བ་གང་དག་གཅིག་ཀུན་དུ་འཆད་པར་འགྱུར་ཞེ་ན། འདོད་གཏོགས་སྐྱེས་ནས་ཐོབ་པ་རྣམས། །འདོད་པ་ན་སྤྱོད་པའི་དགེ་བའི་རྩ་བ་རྣམས་ཀུན་དུ་འཆད་པར་འགྱུར་ཏེ། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་དག་དང་མི་ལྡན་པའི་ཕྱིར་རོ། །

[Block 785]
འོ་ན་བཏགས་པ་ལས་འདི་ཙམ་གྱིས་ན་གང་ཟག་འདིས་ཁམས་གསུམ་པའི་དགེ་བའི་རྩ་བ་རྣམས་ཀུན་དུ་གཅད་པ༌[^572]ཡིན་ནོ་ཞེས་བཤད་པ་ཇི་ལྟར་གྲངས༌[^573]དེ་ནི་དེའི་ཐོབ་པ་ཐག་སྲིང་བར་བྱེད་པ་ལས་དགོངས་ནས་གསུངས་པ་ཡིན་ཏེ། རྒྱུད་དེའི་སྣོད་མ་ཡིན་པ་ཉིད་དུ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 786]
སྐྱེས་ནས་ཐོབ་པ་ཁོ་ན་དག་ཀུན་དུ་ཆད་པར༌[^574]འགྱུར་ཏེ། སྦྱོར་བ་ལས་བྱུང་བ་དག་ལས་ནི་སྔར་ཡོངས་སུ་ཉམས་ཟིན་པའི་ཕྱིར་རོ། །

[Block 787]
ཅི་ལ་དམིགས་པའི་ལོག་པར་ལྟ་བས་ཀུན་དུ་གཅོད་པར་བྱེད་ཅེ་ན། རྒྱུ་དང་འབྲས༌[^575]ལ་སྐུར་འདེབས་པ།[^576] །ལེགས་པར་སྤྱད་པ་མེད་དོ། །

[Block 788]
ཉེས་པར་སྤྱད་པ་མེད་དོ་ཞེས་རྒྱུ་ལ་སྐུར་པ་འདེབས་པ་གང་དག་ཡིན་པ་དང་། ལེགས་པར་སྤྱད་པ་དང་ཉེས་པར་སྤྱད་པའི༌[^577]རྣམ་པར་སྨིན་པ་མེད་དོ་ཞེས་འབྲས་བུ་ལ་སྐུར་པ་འདེབས་པ་གང་དག་ཡིན་པའོ། །

[Block 789]
གཞན་དག་ན་རེ་དེ་དག་ནི་བར་ཆད་མེད་པའི་ལམ་དང་། རྣམ་པར་གྲོལ་བའི་ལམ་ལྟ་བུ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 790]
ཁ་ཅིག་ན་རེ་ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་ཁོ་ནས་ཡིན་གྱི་ཟག་པ་མེད་པ་ལ་དམིགས་པས་ནི་མ་ཡིན་ནོ། །

[Block 791]
སྐལ་བ་མཉམ་པའི་ཁམས་ལ་དམིགས་པ་ཁོ་ནས་ཡིན་གྱི༌[^578]སྐལ་བ་མི་མཉམ་པའི་ཁམས་ལ་ནི༌[^579]དམིགས་པས་ནི་མ་ཡིན་ཏེ། མཚུངས་པར་ལྡན་པ་ཙམ་གྱི་སྒོ་ནས་རྒྱས་པས་ཉམ༌[^580]ཆུང་བའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 792]
འདི་སྐད་དུ་ཀུན་གྱིས་ཁ་ཅིག་ན་རེ་དགེ་བའི་རྩ་བ་རྣམ་པ་དགུ༌[^581]ཆར་ཡང་ཅིག་ཅར་དུ་འཆད་དེ། མཐོང་བས་སྤང་བར་བྱ་བ་དག་བཞིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 793]
འདི་སྐད་དུ་རིམ་གྱིས་ཞེས་བརྗོད་དེ། བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་བཞིན་དུ་ཆེན་པོའི་ཆེན་པོས་ཆུང་ངུའི་ཆུང་ངུ་གཅོད་པར་བྱེད་པའི་བར་དུ་ལོག་པར་ལྟ་བ་རྣམ་པ་དགུས་དགེ་བའི་རྩ་བ་རྣམ་པ་དགུ་གཅོད་པར་བྱེད་དེ། དེ་ལྟར་ན་ཕྲ་མོ་དང་ལྷན་ཅིག་ཏུ་གྱུར་པའི་དགེ་བའི་རྩ་བ་རྣམས་གང་ཞེ་ན། དགེ་བའི་རྩ་བ་རྣམས་ཀུན་དུ་གཅོད་པར་བྱེད་པ་ན་ཐམས་ཅད་ཀྱི་ཐ་མར་འདོར་བ་གང་དག་ཡིན་པ་སྟེ།[^582] གང་དག་མེད་པས་དགེ་བའི་རྩ་བ་རྣམས༌[^583]ཀུན་དུ་འཆད་པ༌[^584]ཞེས་བྱ་བའི་གྲངས་སུ་འགྲོ་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་གཞུང་འདི་བསྐྱབ་པ་ཡིན་ནོ། །

[Block 794]
འོ་ན་མི་དགེ་བའི་རྩ་བ་ཆེན་པོ་གང་དག་ཡིན་ཞེ་ན། མི་དགེ་བའི་རྩ་བ་གང་དག་གིས་དགེ་བའི་རྩ་བ་རྣམས་ཀུན་དུ་གཅོད་པར་བྱེད་པའོ་ཞེས་བྱ་བའི༌[^585]གཞུང་འདིའི་ཚུལ་ཇི་ལྟ་བུ་ཡིན༌[^586]ཞེ་ན། དེ་དག་གིས་མ་ལུས་པར་གཅོད་པའི་ཕྱིར་དེ་ནི་རྫོགས་པ་ལས་དགོངས་ཏེ་གསུངས་པ་ཡིན་ཏེ། དེ་དག་ལས་རྣམ་པ་གཅིག་མ་ཆད་ན་ཡང་ཐམས་ཅད་སྐྱེ་བའི་རྒྱུར་འགྱུར་རོ། །

[Block 795]
ཁ་ཅིག་ན་རེ་མཐོང་བའི་ལམ་བཞིན་དུ་མ་ལངས་པར་གཅོད་པར་བྱེད་དོ་ཞེས་ཟེར་རོ། །

[Block 796]
འདི་སྐད་དུ་གཉི་གར་གཅོད་པར་བྱེད་དོ་ཞེས་བརྗོད་དོ། །

[Block 797]
ཁ་ཅིག་ན་རེ་སྔར་སྡོམ་པ་སྤངས་ལ༌[^587]ཕྱིས་དགེ་བའི་རྩ་བ་རྣམས་ཀུན་དུ་གཅོད་དོ་ཞེས་ཟེར་རོ། །

[Block 798]
འདི་སྐད་དུ་སྡོམ་པ་སེམས་གང་གི་འབྲས་བུ་ཡིན་པ་དེ་གཏོང་བ༌[^588]དེ་ཡང་གཏོང་ངོ་ཞེས་བརྗོད་དོ། །གང་དུ་དགེ་བའི་རྩ་བ་རྣམས་ཀུན་དུ་གཅོད་ཅེ་ན། མིའི་ནང་དུ་མིའི་ནང་ཁོ་ན་དག་ཏུ་གཅོད་ཀྱི་ངན་སོང་དག་ན་ནི་མ་ཡིན་ཏེ། ཤེས་རབ་ཉོན་མོངས་པ་ཅན་དང་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་དག་མི་བསྟན་པའི༌[^589]ཕྱིར་རོ། །

[Block 799]
ལྷ་དག་གི་ནང་ན་ཡང་མེད་དེ། ལས་ཀྱི་འབྲས་བུ་མངོན་སུམ་དུ་འགྱུར་བའི༌[^590]ཕྱིར་རོ། །

[Block 800]
གླིང་གསུམ་དག་ན་ཡོད་ཀྱི་བྱང་གི་སྒྲ་མི་སྙན་དག༌[^591]ན་ཡང་མེད་དེ། སྡིག་པའི་བསམ་པ་ཅན༌[^592]མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 801]
གཞན་དག་ན་རེ་འཛམ་བུའི་གླིང་ཁོ་ན་ན་ཡོད་དོ་ཞེས་ཟེར་ཏེ། འཛམ་བུའི༌[^593]གླིང་པ་ཐམས་ཅད་པས་ཉུང་ན་དབང་པོ་བརྒྱད་དང་ལྡན་པ་ཡིན་ཏེ། ཤར་གྱི་ལུས་འཕགས་པོ་དང་། ནུབ་ཀྱི་བ་ལང་སྤྱོད་པ་ཡང་དེ་དང་འདྲའོ་ཞེས་བྱ་བའི་གཞུང་འདི་དང་འགལ་བར་འགྱུར་རོ། །

[Block 802]
དེ་དག་ཀྱང་། སྐྱེས་པ་བུད་མེད་ཀྱིས་གཅོད་དོ། །

[Block 803]
སྐྱེས་པ་དང་བུད་མེད་ཀྱིས་ཀུན་དུ་གཅོད་པར་བྱེད་དེ། གཞན་དག་ན་རེ་འདུན་པ་དང་བརྩོན་འགྲུས་ཞེན་པའི་ཕྱིར་བུད་མེད་ཀྱིས་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། གོང་མའི་དབང་པོ་དང་ལྡན་པ་དེ་དག༌[^594]གདོན་མི་ཟ་བར་དབང་པོ་བརྒྱད་དང་ལྡན་ནོ་ཞེས་བྱ་བའི་གཞུང་འདི་དང་འགལ་བར་འགྱུར་རོ། །

[Block 804]
དེ་དག་ལས་ཀྱང་སྲེད་པ་སྤྱད་པས་ནི་ཀུན་དུ་གཅོད་པར་མི་བྱེད་དེ། བསམ་པ་གཡོ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 805]
འོ་ན་ཅི་ཞེ་ན། ལྟ་སྤྱད།

[Block 806 [VERSE]]
སྡིག་པའི་བསམ་པ་བརྟན་པ་དང་། །
མཁྱུད་པ༌[^595]ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 807]
དེ་ཉིད་ཀྱི་ཕྱིར་མ་ནིང་ལ་སོགས་པས་ཀྱང་མ་ཡིན་ཏེ། སྲེད་པའི་སྤྱད་པའི་ཕྱོགས་དང་མཐུན་པའི་ཕྱིར་དང་། ངན་སོང༌[^596]བཞིན་ནོ་དགེ་བའི་རྩ་བ་ཀུན་དུ་འཆད་པའི་རང་བཞིན་ཇི་ལྟ་བུ་ཞིག་ཡིན་ཞེ་ན། དེ་ནི་མི་ལྡན་པའོ། །

[Block 808]
གང་གི་ཚེ་དགེ་བའི་རྩ་བ་རྣམས་ཀྱི་ཐོབ་པ་ཡང་མི་སྐྱེ་ལ་མ་ཐོབ་པ་སྐྱེ་བ་སྟེ། མི་ལྡན་པ་དེ་སྐྱེས་ན་དགེ་བའི་རྩ་བ་རྣམས༌[^597]ཀུན་དུ་ཆད་པ་ཞེས་བྱའོ། །

[Block 809 [HEADING]]
### དགེ་བའི་རྩ་བ་ཉིང་མཚམས་སྦྱོར་བ། ^1-51-0

[Block 810]
ཀུན་དུ་ཆད་པ་དེ་དག་ཇི་ལྟར་ན་ཡང་ཉིང་མཚམས་སྦྱོར་ཞེ་ན། མཚམས་ནི་ཐེ་ཚོམ་ཡོད་ལྟ་བས། །ནམ་ཞིག་འདི་ལ་རྒྱུ་དང་འབྲས་བུ་ལ་ཐེ་ཚོམ་སྐྱེས་པའམ། ཡང་དག་པའི་ལྟ་བ་ཞེས་བྱ་བའི་དོན་ཏེ། ཡོད་པར་ལྟ་བ་སྐྱེས་པ་དེའི་ཚེ་ཡང་དེའི་ཐོབ་པ་ཀུན་དུ་སྤྱོད་པའི་ཕྱིར་དགེ་བའི་རྩ་བ་རྣམས་ཉིང་མཚམས་སྦྱོར་ཞེས་བྱའོ། །
--- END BLOCKS ---
