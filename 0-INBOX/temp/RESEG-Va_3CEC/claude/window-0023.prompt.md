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
[Block 806]
ལུས་བདེ་བ་སྐྱེད་པ་ནི། ལུས་སིམ་པར་བྱེད་པས་སོ། །

[Block 807]
སེམས་བདེ་བ་སྐྱེད་པ༌[^707]ནི། སེམས་སིམ་པས་སོ། །

[Block 808]
གཞན་གྱིས་གནོད་པར་བྱ་བ་ལས་ཤིན་ཏུ་འདས་ཞེས་བྱ་བ་ནི། བྱམས་པ་དང་ལྡན་པ་ལ་སུ་ཡང་གནོད་པར་མི་བྱེད་པས་སོ། །

[Block 809]
ཉེས་པ་ཐམས་ཅད་ཀྱི་འཇིགས་པ༌[^708]དང་བྲལ་ཏེ༌[^709]ཞེས་བྱ་བ་ནི་བྱམས་པ་ཅན་གྱི་གང་ཟག་དེ་སྲོག་གཅོད་པ་དང་། མ་བྱིན་པར་ལེན་པ་ལ་སོགས་པའི་ལས་ལ་མི་འཇུག་པས་དེ་ལ་ཉེས་པ་བྱས་པ་ནི་རྒྱུ་ལས་མི་འབྱུང་བའི་ཚེ་འདི་ལ་བཅིངས་པ༌[^710]དང་། གསད་པ་དང་། ཚེ་རབས་གཞན་དུ་ངན་སོང་དུ་སྐྱེ་བའི་འཇིགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 810]
འཕགས་པའི་ལམ་དང་མཐུན་ཞེས་བྱ་བ་ནི་བྱམས་པ་དེ་འཕགས་པའི་ལམ་གྱི་ཡན་ལག་བརྒྱད་དང་མི་འགལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 811]
གཤེ་བ་དང་། སྡང་བའི་སེམས་དང་ལྡན་པའི་སེམས་ཅན་རྣམས་དད་པར་བྱེད་པ་ཞེས་བྱ་བ་ལ། ཞེ་སྡང་གི་རྒྱུས་ཚིག་རྩུབ་པོ་སྨྲ་བ་ནི་གཤེ་བའོ། །

[Block 812]
སེམས་ཅན་གསད་པ་ལ་སོགས་པས་ཕུང་བར་བྱ་བའི༌[^711]བསམ་པ་རྩུབ་པོ་ནི་སྡང་བའི་སེམས་དང་ལྡན་ཏེ།[^712] དེ་ལྟ་བུ་དག་ཀྱང་བྱམས་པ་དང་ལྡན་པའི་གང་ཟག་ལ་དད་པ་སྐྱེ་བར་འགྱུར་བས་ནི༌[^713]བྱམས་པ་ནི་གཤེ་བ་དང་སྡང་བའི་སེམས་དང་ལྡན་པའི་སེམས་ཅན་རྣམས་དད་པར་བྱེད་པའོ། །

[Block 813]
གཡུལ་ཐམས་ཅད་ལས་སྒྲོལ་བ༌[^714]སྟེ་ཞེས་བྱ་བ་ནི་མཚོན་ཆ་མེད་པར་བྱམས་པའི་ཏིང་ངེ་འཛིན་གྱིས་བདུད་དང་མུ་སྟེགས་ཅན་ལ་སོགས་པ་ཐམས་ཅད་ལས་རྒྱལ་བར་བྱེད་དེ། དེ་བས་ན་དབྱིག་པ་དང་། མཚོན་ཆ་འཆང་བ་མ་ཡིན་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 814]
སེམས་ཅན་ཐམས་ཅད་རབ་ཏུ་ཐར་བར་བྱ་བ་ལ་དགའ་བ་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་མྱ་ངན་ལས་འདས་པར་བྱ་བ་ལ་མོས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 815]
ཚུལ་འཆོས་པ་དང་ཁ་གསག་ཅེས་བྱ་བ་ལ་སོགས་པ་ལ། ཁེ་དང་བཀུར་སྟི༌[^715]ལ་སོགས་པའི་བསམ་པ་ཉོན་མོངས་པ་ཅན་གྱི་སྤྱོད་ལམ་འཆོས་པ་ཐམས་ཅད་ནི་ཚུལ་འཆོས་པའོ། །

[Block 816]
ཐོབ་པ་ལ་ཆགས་པའི་ཕྱིར་ཚིག་སྙན་པར་སྨྲ་བ་ཐམས་ཅད་ནི་ཁ་གསག་གོ། །

[Block 817]
རྙེད་པ་ལ་ཆགས་པའི་སེམས་ཀྱིས་ལྷུང་བཟེད་དང་ཆོས་གོས་ལ་སོགས་པའི་ཡོ་བྱད་ནན་གྱིས་སློང་བ་ནི་ཐོབ་ཀྱིས་འཇལ་བའོ། །

[Block 818]
བྱམས་པ་དང་ལྡན་པ་ལ་སོགས་པའི༌[^716]འཚོ་བ་དེ་དག་མེད་པས་ན་བྲལ་བ་ཞེས་བྱ༌[^717]སྟེ། ལས་བཤད་ཟིན་ཏོ།། །།

[Block 819 [HEADING]]
#### འབྲས་བུ། ^2-1-3-0

[Block 820]
འབྲས་བུ་བསྟན་པའི་ཕྱིར་རྙེད་པ་དང་བཀུར་སྟི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། རྙེད་པ་ནི་ཆོས་གོས་ལ་སོགས་པའོ། །

[Block 821]
བཀུར་སྟི་ནི་ཕྱག་འཚལ་བ་ལ་སོགས་པའོ། །

[Block 822]
ཚིགས་སུ་བཅད་པ་ནི་བསྟོད་པ་སྟེ། དེ་ལྟ་བུ་དག་དང་ལྡན་པར་འགྱུར་བས་ན༌[^718]འབྱུང་བར་བྱེད་པ་ཞེས་བྱའོ། །

[Block 823]
ཕྱག་བྱས་པ་ནི་འཇིག་རྟེན་གྱི་གཙོ་བོ་དེ་དག་གིས་བྱམས་པ་དང་ལྡན་པ་ལ་ཕྱག་བྱེད་པའི་ཕྱིར་རོ། །

[Block 824]
གང་གི་གཟི་བརྗིད་ཀྱི་རྒྱན་གྱིས་བརྒྱན་པ་ནི་བྱམས་པའི༌[^719]གཟི་བརྗིད་ཀྱི་རྒྱན་གྱིས་བརྒྱན་པའི་ཕྱིར་རོ། །

[Block 825]
མཁས་པས་རབ་ཏུ་བསྔགས་པ་ནི་བྱམས་པ་དང་ལྡན་པའི་གང་ཟག་ལ་ཉན་ཐོས་དང་རང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་བསྟོད་པར་མཛད་པས་སོ། །

[Block 826]
བྱིས་པ་ཐམས་ཅད་བསྲུང་བ་ནི་བྱམས་པ་དེས་སོ་སོའི་སྐྱེ་བོ་རྣམས་ཞེ་སྡང་གི་ལམ་དུ་མི་གཏོང༌[^720]བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 827]
ཚངས་པའི་ལམ་དང་མཐུན་པ་ནི་མྱ་ངན་ལས་འདས་པའི་ལམ་དང་མཐུན་པའམ། ཚད་མེད་པ་བཞི་དང་མཐུན་པའོ། །

[Block 828]
འདོད་པའི་ཁམས་དང་མ་འདྲེས་པ་ནི་འདོད་པའི་ཁམས་ན༌[^721]བྱམས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 829]
སེམས་ཅན་ཐམས་ཅད་ཐར་པའི་ལམ་གྱི་མཆོག་ཅེས་བྱ་བ་ནི་སེམས་ཅན་རྣམས་མྱ་ངན་ལས་འདས་པར་འགྲོ་བའི་ལམ་གྱི༌[^722]ནང་ན་ལམ་གྱི་དམ་པ་བྱམས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 830]
ཐེག་པ་ཐམས་ཅད་ཡང་དག་པར་བསྡུས་པ་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཐམས་ཅད་ཀྱང་བྱམས་པར་འདུས་ཏེ། ཐེག་པ་གསུམ་ཆར་གྱི་རྩ་བ་བྱམས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 831]
ཟང་ཟིང་མེད་པའི་བསོད་ནམས་ཀྱིས་གཟུང་བ༌[^723]ཞེས་བྱ་བ་ལ་བསོད་ནམས་ཀྱི་དངོས་པོ་རྣམ་པ་གསུམ་སྟེ།[^724] སྦྱིན་པའི་བསོད་ནམས་བྱ་བའི་དངོས་པོ་དང་། ཚུལ་ཁྲིམས་ཀྱི་བསོད་ནམས་བྱ་བའི་དངོས་པོ་དང་། བསྒོམས་པའི༌[^725]བསོད་ནམས་བྱ་བའི་དངོས་པོའོ། །

[Block 832]
དེ་ལ་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་གཉིས་ནི་ཟང་ཟིང་དང་བཅས་པའི་བསོད་ནམས་ཀྱི་དངོས་པོ་སྟེ། སྦྱིན་པས་ལོངས་སྤྱོད་ཀྱི་རྒྱུར་འགྱུར་ལ། ཚུལ་ཁྲིམས་ཀྱིས་མཐོ་རིས་ཀྱི་རྒྱུར་འགྱུར་བས་འཁོར་བའི་རྒྱུ༌[^726]ཡིན་པའི་ཕྱིར་རོ། །

[Block 833]
བསྒོམས་པའི༌[^727]བསོད་ནམས་བྱ་བའི་དངོས་པོ་ནི༌[^728]ཟང་ཟིང་མེད་པ་སྟེ། ཐར་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 834]
བྱམས་པ་ཡང་བསྒོམས་པའི༌[^729]བསོད་ནམས་བྱ་བའི་དངོས་པོར་གཏོགས་པས་ན་ཟང་ཟིང་མེད་པའི་བསོད་ནམས་ཀྱིས་གཟུང༌[^730]བ་ཞེས་བྱའོ། །

[Block 835]
བསོད་ནམས་ཀྱི་ཚོགས་ཐམས་ཅད་སྩོགས་པ༌[^731]ཞེས་བྱ་བ་ནི་བྱམས་པ་བསྒོམས་པའི༌[^732]མཐུ་ལས་བསོད་ནམས་ཀྱི་ཚོགས་དཔག་ཏུ་མེད་པའི་སྩོགས་པས། རྫས་ལས་བྱུང་བའི༌[^733]བསོད་ནམས་བྱ་བའི་དངོས་པོ་ཐམས་ཅད་ཀྱིས༌[^734]ཟིལ་གྱིས༌[^735]མི་ནོན་པ་ཞེས་བྱ་བ་ལ། རྫས་ནི་ལོངས་སྤྱོད་ཀྱི་ནོར་ལ་བྱའོ། །

[Block 836]
ནོར་བཏང་བའི་གཞི་ལས་བྱུང་བའི་བསོད་ནམས་ནི་རྫས་ལས་བྱུང་བའི་བསོད་ནམས་ཏེ། དེ་ཡང་གཙུག་ལག་ཁང་དང་། དེའི་ས་གཞི༌[^736]དང་། མལ་སྟན་དང་། འཚོ་བའི་ཡོ་བྱད་དང་། བསོད་སྙོམས་ལ་སོགས་པའོ། །

[Block 837]
བྱམས་པ་བསྒོམས་པའི༌[^737]བསོད་ནམས་ལ་རྫས་ལས་བྱུང་བའི་བསོད་ནམས་ཐམས་ཅད་ཀྱིས༌[^738]ཟིལ་གྱིས་གནོན་པར་མི་ནུས་པས་ན་ཟིལ་གྱིས་མི་ནོན་པ་ཞེས་བྱ་སྟེ།[^739] བསོད་ནམས་དེ་དག་བས་བྱམས་པའི་བསོད་ནམས་འབྲས་བུ་ཆེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 838]
བརྒྱན་ཞེས་བྱ་བ་ནི་བྱམས་པ་དང་ལྡན་པ་ནི་མིང་གིས་སྨོས་པའི་ཡོན་ཏན་དེ་དག་ཐོབ་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 839]
དབང་པོ་ཉམས་པ་དང་མ་ཚང་བ་ཐམས་ཅད་སྤངས་པ་ཞེས་བྱ་བ་ལ་མིག་དང་རྣ་བ་ལ་སོགས་པའི་དབང་པོ་ཡོད་ཀྱང་གཟུགས་ལྟ་བ་ལ་མི་གསལ་བ་དང་། སྒྲ་མཉན་པ་ལ་མི་གསལ་བ་ནི༌[^740]དབང་པོ་ཉམས་པའོ། །

[Block 840]
རྣ་བ་རྡུམ་པོ་དང་། མིག་ཞར་བ་དང་། ལག་པ་རྡུམ་པོར་འགྱུར་བ་ནི་དབང་པོ་མ་ཚང་བའོ། །

[Block 841]
བྱམས་པ་དང་ལྡན་པ་ནི། གར་སྐྱེས་ཀྱང་དབང་པོ་གསལ་ཞིང་དབང་པོ་ཚང་བར་སྐྱེ་བར་འགྱུར་བས་ན། དབང་པོ་ཉམས་པ་དང་མ་ཚང་བ་ཐམས་ཅད་སྤངས་པ༌[^741]ཞེས་བྱའོ། །

[Block 842]
བདེ་འགྲོ་ཐམས་ཅད་དང་མྱ་ངན་ལས་འདས་པའི་ལམ་དང་མཐུན་པ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་ཚུལ་ཁྲིམས་དང་སྦྱིན་པ་ལ་སོགས་པས་ལྷ་དང་མིར༌[^742]སྐྱེ་བ༌[^743]དང་། འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པས་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་འགྱུར་བ་བཞིན་དུ་བྱམས་པ་ལ་གནས་པས་ཀྱང་རྟག་ཏུ་ལྷ་དང་མིར་སྐྱེ་བ་དང་། མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་འགྱུར་བས་ན་བདེ་འགྲོ་ཐམས་ཅད་དང་མྱ་ངན་ལས་འདས་པའི་ལམ་དང་མཐུན་པ་ཞེས་བྱའོ། །

[Block 843]
ངན་སོང་ཐམས་ཅད་དང་། མི་ཁོམ་པ་བརྒྱད་ལས་འདས་པ་ཞེས་བྱ་བ་ནི་བྱམས་པ་དང་ལྡན་པ་དེ་ནམས་ཀྱང་ཉམས་ང་བའི་གནས་དག་ཏུ་མི་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 844]
འབྲས་བུ་བཤད་ཟིན་ཏོ།། །།

[Block 845 [HEADING]]
#### རང་བཞིན། ^2-1-4-0
--- END BLOCKS ---
