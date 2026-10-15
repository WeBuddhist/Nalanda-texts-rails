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
བང་རིམ་དང་འཆག་ས་དང་སྒོ་ཁང་དང་། ཁྱམས་དག་ལ་ཕུལ་བའི་སྣོད་སྒོའོ། །

[Block 877]
རྫིང་བུའི་ཡང་ངོ་ཞེས་བྱ་བ་ནི། སྣོད་སྒོ་ཁང་ཞེས་བྱ་བ་འདོན་པ་འདི་འདིར་འདོན་པར་འདོད་པ་ཉིད་ཀྱིས་ཉེ་བར་བཏགས་པའོ། །

[Block 878]
ཁ་ཅིག་ལས་དེ་ནི་ཕྱོགས་བཞིའི་དགེ་འདུན་གྱི་ཉིད་དུ་གཞག་གོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་རྫིང་བུ་ལའོ། །

[Block 879]
ཁ་ཅིག་ལས་ཞེས་བྱ་བ་ནི་འདོད་པའོ། །

[Block 880]
དཀོན་མཆོག་གི་དོན་དུ་བླང་དུ་རུང་ངོ་། །བསྒྲག་ཏུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། དགེ་སློང་གི་བྱར་མི་རུང་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་གི་ཚེ་བསྒྲགས༌[^772]པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ལེན་པའི་ཚེའོ་ཞེས་སྨོས་ཏེ། རྙེད་པ་འབུལ་བ་ལེན་པའི་ཚེ་ནའོ་ཞེས་བྱ་བའི་དོན་གྱིས་སོ། །

[Block 881]
མཐོང་བར་བྱ་བའི་ཕྱིར་འཕང་ལོ༌[^773]བྱའོ་ཞེས་བྱ་བ་ནི། གང་གི་ཕྱིར་དེར་སྒྲོགས་པར་བྱེད་པ་མཐོང་བ་ཡིན་ནོ། །

[Block 882]
འཕང་ལོ༌[^774]གཉིས་སྨོས་པ་ནི་ཤིང་རྟའི་འཕང་ལོའི༌[^775]རྣམ་པ་ལ་འདིར་འཁོར་ལོར་འདོད་པ་ཡིན་ནོ། །

[Block 883]
ཚ་བ་དང་རླུང་དང་ཆར་བའི་གནོད་པས་མི་རེག༌[^776]པར་བྱ་བའི་ཕྱིར་ཁང་པ་བརྩེགས་པ་སྒོ་བཞི་དང་ལྡན་པའོ། །

[Block 884]
དུས་སྟོན་གྱི༌[^777]རྗེས་ལ་འཕང་ལོ༌[^778]བརྟུལ༌[^779]ལོ་ཞེས་བྱ་བ་ནི་དུས་སྟོན་ལ་འཕང་ལོ༌[^780]གང་ཡིན་པ་དེ་ལ་ཆོ་ག་འདི་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པའོ། །

[Block 885]
སྣོད་སྤྱད་འབྲུབ་པས་རྙེད་པ་འབྲུབ་པར་བྱའོ། །

[Block 886]
གཉིས་ཀ་ལ་མ་བསྔོས་པ་སྟོན་པ་མཆོད་པའི་ཚེ་ཕུལ་བ་དགེ་འདུན་གྱི་ལ་དགེ་སློང་མ་རྣམས་ཀྱི་འཇུག་པ་མེད་དོ་ཞེས་བྱ་བ་ལ། གཉིས་ཀ་ལ་ཞེས་བྱ་བ་ནི། དགེ་སློང་གི་དགེ་འདུན་དང་། དགེ་སློང་མའི་དགེ་འདུན་ནོ། །

[Block 887]
སྟོན་པ་མཆོད་པའི་ཚེ་ཞེས་བྱ་བ་ནི། བྱང་ཆུབ་སེམས་དཔའི་གནས་སྐབས་ཀྱང་སྟོན་པ་ཡིན་པས་སོ། །

[Block 888]
དགེ་སློང་བྱེད་པ་པོ་རྣམས་ཀྱིས་མཆོད་པ་ལ་འདི་ཆོ་ག་ཞེས་བྱ་བའོ།

[Block 889]
[^781] །དགེ་སློང་མ་རྣམས་ཀྱིས་བྱས་པའི་ཚེ་ལ་བསྔོས་པའི་རྙེད་པ་བྱུང་བ་གང་ཡིན་པ་དེ་ཉིད་ཀྱིས་རྟོགས་པའོ། །

[Block 890]
གཉིས་ཀ་བྱས་པ་ན་གཉིས་ཀ་ལ་བསྔོས་པ་རྙེད་པ་འབྱུང་བ་གང་ཡིན་པ་དེ་ལ་ནི་རྗེས་སུ་མ་བརྗོད་པར་ཕུལ་བ་ལ་ཐུན་མོང་བ་ཉིད་ཀྱི་ཕྱིར་སྟོན་པ་ལ་དོགས་པ་དེ་བཟློག་པའི་དོན་དུ་འདིར་བྱས་སོ། །

[Block 891]
འདི་ལ་གཅིག་གི་ནང་དུ་དེ་དག་གིས་འཕང་ལོ༌[^782]ཐ་དད་པ་བཙུགས་ན་ཉེས་པ་སྦོམ་པོའོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་མཆོད་པ་ལའོ། །

[Block 892]
ཁ་ཅིག་གིས་ཞེས་བྱ་བ་ནི་གང་དུ་དགེ་སློང་རྣམས་ཀྱིས་འཕང་ལོ༌[^783]བཙུགས་པ་དེ་ལས་གཞན་པ་དག་ལས་དགེ་འདུན་གྱི་དབྱེན་གྱི་སྐབས་སུ་འདི་གཏོགས་པར་རིག་པར་བྱའོ། །

[Block 893 [VERSE]]
སྣོད་སྤྱད་འགྱེད་པས་བགོ་བར་བྱའོ། །
དེ་བསྐོར་བར༌[^784]བྱའོ་ཞེས་བྱ་བ་ནི།
སྣོད་སྤྱད་འགྱེད་པ་པོ་དེས་སོ། །

[Block 894]
དེས་ཇི་ལྟར་བགོ་བར་བྱ་བ༌[^785]ཞེ་ན། དེའི་ཕྱིར་བཙོང་བར་བྱ་བ་རྣམས་བཙོངས་ཏེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སུ་ལ་བཙོངས་ཏེ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་འདུས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཇི་ལྟར་བཙོངས་ཏེ་ཞེ་ན། དེའི་ཕྱིར་བསྐྱེད་པས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 895]
དེ་ཉིད་ཀྱིས་དེར་འདུ་བའི་སྐབས་སུ་རྗེས་སུ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི། སྣོད་སྤྱད་འགྱེད་པའི་གང་ཟག་དེ་ཉིད་ཀྱིས་གནས་མལ་བཤམ་པ་ལ་སོགས་པ་འདུ་བ་དང་འབྲེལ་བའི་ལས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 896]
དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་རིན་ཐང་གང་བ་པོ་ཞེས་བྱ་བ་ནི། བཙོང་བར་བྱ་བའི་དངོས་པོ་རྣམས་ཀྱིའོ། །

[Block 897]
རིན་ཐང་ཇི་ཙམ་དུ་གདབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་རན་པར་རོ། །

[Block 898]
དེས་ནི་དེ་ལ་མི་དབབ་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། རིན་ཐང་བཏབ་པ་དེས་ནི་དགེ་འདུན་གྱི་གནས་བརྟན་དེ་ལ་རྫས་དེ་ཉོ་བ་དང་དེའི་རིན་ཐང་གཞལ་བ་མི་དབབ་པ་ཉིད་དོ། །

[Block 899]
ཡང་མི་འབྱུང་བར་ངེས་པར་བྱས་ནས་བསྐྱེད་པ་ལ་དབབ་བོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་སླར་མི་བསྐྱེད་ཅེས༌[^786]བྱ་བ་ངེས་པར་གྱུར་ན་དེ་ལ་ཡང་དབབ་པ་ཉིད་ཡིན་ནོ། །

[Block 900 [VERSE]]
མི་ཉོ་བས་བསྐྱེད་པར་མི་བྱའོ། །
བུད་མེད་མི་བྱའོ་ཞེས་བྱ་བ་ནི།
རིན་ཐང་དེ་ལྟར་བསྐྱེད་པར་མི་བྱའོ། །

[Block 901]
རིན་མ་ཕུལ་གྱི་བར་དུ་སྤྱད་པ་དང་བྱི་དོར་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ནི། བཀྲུ་བ་དང་ཁ་བསྒྱུར་བ་ལ་སོགས་པའི་བྱི་དོར་ཡང་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 902]
བགོ་སྐལ་བ་རྣམས་མང་བ་ཉིད་ཡིན་ན་བཅུ་ལ་སོགས་པའི་ཚོམས་ཀྱིས་བགོ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་བགོ་སྐལ་བ་རྣམས་ཀྱི་སྒྲ་ནི་ཚོམས་བརྗོད་པའོ། །

[Block 903]
ཕོག་པ་མ་བགོས་པར་ཚོམས་ལས་འགའ་ཞིག་ཤི་ན་དེའི་སྐལ་བ་ཚོམས་དེ་པ་དབང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཚོགས་ལ་ཕུལ་བ་དེའི་ཆ་མ་བསྒོས་པར༌[^787]ཚོགས་དེར་འགའ་ཞིག་ཤི་ན། འགའ་ཞིག་ཤི་བ་དེའི་སྐལ་བ་གང་ཞིག་ཐོབ་པའི་སྐལ་བ་དེ་ལ་ཚོགས་གང་ཞིག་འབྱུང་བ་རྣམས་ལ་དེ་དབང་བ་ཉིད་ཡིན་ནོ། །

[Block 904]
བགོས་པའི་འོག་ཏུ་ཤི་ན་ནི་དེའི་སྐལ་བ་མཚམས་སུ་གཏོགས་པའི་རབ་ཏུ་བྱུང་བ་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་རྣམས་ཀྱིས་ཤི་བའི་ཡོ་བྱད་དུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 905]
མྱ་ངན་ལས་འདས་བའི༌[^788]བསམ་པས་རབ་ཏུ་བྱུང་ཞིང་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ལ་ནི་གོས་སྟོང་ཕྲག་བརྒྱ་པ་དང་། ཁ་ཟས་རོ་བརྒྱ་པ་དང་། ཁང་པ་བརྩེགས་པ་ལྔ་བརྒྱ་པ་ཡང་འོས་སོ། །

[Block 906]
དགེ་འདུན་གྱི་རྫས་ཀྱང་ངོ་ཞེས་བྱ་བར་ཡང་འོས་སོ་ཞེས་བྱ་བར་ཡང་སྦྱར་རོ། །

[Block 907]
དགེ་འདུན་གྱི་རྫས་རྣམ་པ་ཇི་ལྟ་བུ་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མི་སློབ་པ་མན་ཆད༌[^789]ཀྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མི་སློབ་པའི་དགེ་འདུན་མན་ཆད་ཀྱི་རྫས་དེ། ཇི་སྲིད་དུ་དགྲ་བཅོམ་པའི་དགེ་འདུན་དབང་བའི་རྫས་ཀྱང་འོས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 908]
རྣམ་པ་གང་ལ་ཞེ་ན། ཚུལ་ཁྲིམས་དང་ལྡན་པ་ལ་ནི་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 909]
སོ་སོའི་སྐྱེ་བོ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་འཕགས་པ་འབའ་ཞིག་ལ་འོས་པར་ནི་མ་ཟད་དོ་ཞེས་བྱ་བ་བསྟན་ཏོ། །

[Block 910]
ཚུལ་ཁྲིམས་འཆལ༌[^790]བ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་རྫས་འོས་པ་མ་ཡིན་པའོ་ཞེས་སྨོས་པའི་ཚིག་གི་ལྷག་མའོ། །

[Block 911]
ལེ་ལོ་ཅན་ལ་ནི་བླངས་པ་དང་ཉེ་བར་སྤྱད་པ་བུ་ལོན་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་ནི། ཚུལ་ཁྲིམས་འཆལ་པ་ལ། རྣམ་པ་ཐམས་ཅད་དུ་མི་འོས་པའི་ཕྱིར་རོ། །

[Block 912]
དེ་ནི་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ལ་རིག་པར་བྱའོ། །

[Block 913]
མཚམས་ཀྱི་ནང་ཉིད་ན་གང་ཟག་གི་གཙུག་ལག་ཁང་ངམ་དེའི་རྙེད་པས་འཚོ་བ་ལ་ནི་དགེ་འདུན་གྱི་རྙེད་པ་འོས་སོ་ཞེས་བྱ་བ་ནི་གང་ཟག་གི་གཙུག་ལག་ཁང་ཡོད་པ་དེ་རྙེད་པས་འཚོ་བའོ། །

[Block 914]
གཙུག་ལག་ཁང་དེའི་མཚམས་ཀྱི་ནང་རོལ་དུ་རྙེད་པ་དེ་འོས་པ་ཡིན་ཏེ། ཇི་ལྟར་འགའ་ཞིག་གཙུག་ལག་ཁང་འདི་ལ་སུ༌[^791]གནས་པ་དེ་ལ་རྙེད་པ་འདི་ཙམ་ཞིག་ཁུད་པར་འབུལ་ལོ་ཞེས་དེའི་རྣམ་པ་ན་རྙེད་པ་དེའོ། །

[Block 915]
དེ་བས་ན་འདི་ལ་དགེ་འདུན་གྱིས་བགོ་བར་བྱ་བ་མ་ཡིན་ཏེ་རྙེད་པ༌[^792]བྱུང་ནའོ། །
--- END BLOCKS ---
