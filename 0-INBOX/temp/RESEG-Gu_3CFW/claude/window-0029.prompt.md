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
[Block 1016]
མདོ་འདི་དང་ཕྱི་མ་གཉིས་རིག་པར་བྱའོ། །

[Block 1017]
བུ་བསྐྲད་པ༌[^865]ལས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཕས་བུ་རེ་ཞིག་བསྐྲད་པའི་ལག་ནས་རྫས་བླང་བར་བྱ་བ་སྟེ། བུ་དེ༌[^866]ཕའི་ཁྱིམ་གྱི་བདག་པོ་ལས་ཕྱིར་མི་ལྡོག་པའི་ཕྱིར་སྙམ་དུ་དགོངས་པའོ། །

[Block 1018]
དུར་ཁྲོད་ནས་ཕྱིར་ཟློག་པ༌[^867]ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཟློག་པ༌[^868]བླང་བར་བྱའོ། །

[Block 1019]
དུར་ཁྲོད་པས་ནི་གཙུག་ལག་ཁང་དུ་འཇུག་པར་བྱ་བ་ཉིད་དང་བཟའ་བར་བྱ་བ་ཉིད་མ་ཡིན་ཏེ། གཙུག་ལག་ཁང་དུ་གནས་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་གཞན་ལ་བླང་བར༌[^869]བྱ་བ་ཉིད་འདི༌[^870]ལས་བསམ་པར་བྱེད་པ་རྣམས་ལ་འདི་སྨོས་སོ། །

[Block 1020]
ཕྱིར་འགུགས་ན་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དུར་ཁྲོད་ནས་ཕྱིར་བཟློག་པ་རྙེད་པ་ལའོ། །

[Block 1021]
དམན༌[^871]ལ་མངོན་པར་ཞེན་པ་འདི་ལྟ་བུ་མ་ཡིན་པ་གཞན་ལ་དེ་བས་ན་འདི་མ་གྲུབ་པ་ཉིད་སྨོས་པར་རིག་པར་བྱའོ། །

[Block 1022]
ཡང་རྙེད་ན་བླང་ངོ་ཞེས་བྱ་བ་ནི་གོ་སྐབས་དབྱེ་བའམ་ཕུལ་བ་དེ་བླང་བར་བྱ་སྟེ། དེ་ནི་དེས་ཁྲོ་བ་མི་བརྟན་པར་བྱས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདིར་རྒྱུའོ། །

[Block 1023]
མཆོད་རྟེན་གྱི་དཀོར་དང་འབྱུང་ཁུང་དང་རྩ་བ་དང་། འབྲས་བུ་དང་བུ་རམ་ཤིང་ལས་གཞན་པའི་ཟས་ཀྱི་དོན་དང་། བསྐོ་བས་ཉེ་བར་འཚོ་བར་བྱ་བ་དང་། ན་བའི་རུང་བ་ནི་བདག་གིར་བྱ་བའི་ཕྱིར་བགོ་བར་མི་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། མཆོད་རྟེན་གྱི་དཀོར་ཞེས་བྱ་བྱ་ནི་དགེ་འདུན་གྱིས་ཐོབ་པར་བྱ་བ་ཉིད་ཀྱི་ཕྱིར། བཅོམ་ལྡན་འདས་ལ་ཤི་བའི་ཡོ་བྱད་འདི་ལ་ཞེས་བྱ་བ་ཐོབ་པ་ལ་སོགས་པའོ། །

[Block 1024]
རྣམ་པ་ཐམས་ཅད་དུ་དཀོན་མཆོག་ཐ་དད་པ་ཡིན་པའི་ཕྱིར། བཅོམ་ལྡན་འདས་དང་དེ་དག་ཀྱང་བདག་གིར་བྱ་བའི་ཕྱིར་བགོ་བར་མི་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 1025]
འབྱུང་ཁུང་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མ་སྨོས་པས་དངོས་གཞིའི་འཇུག་པ་འདི་ལྟ་སྟེ་ཞིང་དང་ལོ་ཐང་དང་ཀུན་དགའ་ར་བ་ལ་སོགས་པ་དང་། ཚོང་འདུས༌[^872]ལ་སོགས་པའི་འཇུག་པ་དང་དཀོར་གྱི་འཇུག་པ་དང་། འདུ་བའི་སྒོ་མི་ཟད་པར་ངེས་པ་ཉིད་བྱས་གཞན་པ༌[^873]དག་དང་། བ་ལང༌[^874]དང་མ་ཧེ་ལ་སོགས་པ་དང་། ལྷ་འབངས་དང་རྩེ་རྒོད་ལ་སོགས་པ་དག་ལ༌[^875]ཡང་བཟའ་བར༌[^876]བྱེད་པ་རྣམས་ཡིན་ནོ། །

[Block 1026]
རྩ་བ་དང་ཞེས་བྱ་བ་ནི་རྩ་བ་དང་འབྲས་བུ་དང་བུ་རམ༌[^877]ཤིང་ལས་གཞན་པའི་ཟས་ནི་བགོ་བར་བྱ་བ་ཉིད་དོ། །

[Block 1027]
དེ་དག་ལས་གཞན་པ་ཟས་ཀྱི་དོན་དུ་སྦྱོར་བ༌[^878]དེ་དག་ལ་སོགས་པའི་དངོས་པོའི་ཁ་འདུ་བའི་སྒོ་དག་ཅེས༌[^879]བྱ་བ་དེ་ཙམ་འདིར་བརྗོད་དེ། གཞན་དུ་ན་འདི་རྣམས་ལ་བགོ་བར་བྱ་བ་ཉིད་དུ་གསུངས་སོ། །

[Block 1028]
དེ་བས་ན་དེ་གསལ་བའོ། །

[Block 1029]
བསྐོ་བས་ཉེ་བར་འཚོ་བ་ཞེས་བྱ་བ་ནི་བསྐོ་བས་ཉེ་བར་འཚོ་བར་འགྱུར་བ་གང་ཡིན་པ་དང་། གནས་ཁང་དང་གནས་མལ་དང་བགོ་བ་ལ་སོགས་པའོ། །

[Block 1030]
ན་བའི་རུང་བ༌[^880]ཞེས་བྱ་བ་ནི་སྨན་དུ་གྱུར་པ་དང་། དགེ་སློང་གི༌[^881]ལྷག་མ་བཏང་བ༌[^882]དང་། གཞན་མ་གྲུབ་པའམ། དེའི་རིན༌[^883]ཐང་ལའོ། །

[Block 1031]
བདག་གིར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི་བདག་གིར་བྱ་བའི་དོན་དུ་མཆོད་རྟེན་གྱི་དཀོར་ལ་སོགས་པ་ལྔ་པོ་དེ་རྣམས་ཀྱིས་བགོ་བར༌[^884]བྱ་བ་གང་ཡིན་པ་དེ་ལ་བཀག་པ་འདི་ཡིན་གྱི་འདུས་བྱས་པའི་ཕྲིན་ལ་སོགས་པའི་དོན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 1032]
རྙེད་པ་ལས་ནི་དབྱར་གྱི་མཚམས་འཇུག་གོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ཙམ་ལ་བརྟེན་ནས་རྙེད་པ་གང་ཡིན་པ་དེ་འབུལ་བར་བྱེད་དེ་དེ་ལ་དབྱར་གྱི་དུས་སུ་གྱུར་པའི་མཚམས་འཇུག་པ་སྟེ།

[Block 1033]
འདིར་གཞུང་ནི་གཏན་པའི་གཞི་ཞུ་བ་ལས།

[Block 1034]
དགེ་སློང་དག་དབྱར་གནས་པར་ཁས་བླངས་ནས་སྤྱོད་ཡུལ་གྱི་གྲོང་གི་ཉེན་ཀོར༌[^885]དུ་མཚམས་བགྱིད་ཅིང་དེ་དག་གིས་དགག་དབྱེ་བགྱིས་ནས་ཕྱི་རོལ་དུ་མཚམས་བགྱིས་ཏེ། དེར་ཡང་མིས་དགེ་འདུན་གཞན་བཙུད་ན༌[^886]དགེ་འདུན་ལ་ཆོས་གོས་འབུལ་ན༌[^887]གང་གིས་འཐོབ་པར་འགྱུར། གང་དག་དེར་དབྱར་གནས་པ་དག་གིས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། རྙེད་པ་དེ་གནས་ཀྱིས་བསྟབས་པ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1035]
འོན་ཏེ་དགེ་སློང་གཞན་དག་གནས་དེར་སྦྱིན་བདག་གིས་བཙུད་པ་ལ་རྙེད་པ་ཡང་ཅིའི་ཕྱིར་དེ་དག་མི་དབང་ཞེ་ན། ཁོ་བོས་དགེ་འདུན་ཙམ་གྱི་ཕྱིར་དབུལ་བར་བྱ་སྟེ། འདི་དག་རང་གིས་དབང་བ་ཉིད་དུ་རྣམ་པར་འཇོག་ཅིང་ལེན་གྲངས༌[^888]སྙམ་པའི་ཕྱིར་ཏེ། འདི་དག་དང་གཞན་དག་ཞུགས་པར་བྱེད་པ་ནི་རིགས་པའི་ཕྱིར་རོ། །

[Block 1036]
གལ་ཏེ་ཡང་འདི་དག་དང་གཞན་དག་ལ་ཡང་རྙེད་པ་དེ་དབུལ་བར་བྱའོ་ཞེས་ཡོངས་སུ་ཆད་པར་བྱེད་ན་ནི། དེའི་ཚེ་གཞན་དག་ཀྱང་དབང་བར་ཐེ་ཚོམ་མེད་དོ། །

[Block 1037]
དེའི་སྤྱོད་ཡུལ་གྱི༌[^889]གྲོང་ཞེས་བྱ་བ་ཉམས་པར་བལྟ་བར་བྱའོ། །

[Block 1038]
རླུང་དང་ཆར་པ་འབྱུང་བར༌[^890]ཞེས་བྱ་བ་དེའི་དབྱར་གྱི་གནས་ངེས་པར་བསྒྲུབས་པའི་རྙེད་པའི་ཚོགས་ནི་འདིར་དབྱར་གནས་པ་རྣམས་ལ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 1039]
རྙེད་པ་དེ་གནས་ཀྱིས་བསྟབས་པ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་གསུངས་པ་ལ་འདིར་གནས་ཞེས༌[^891]བྱ་བ་ནི༌[^892]འདིར་དབྱར་གྱི་གནས་ལ་བརྗོད་དོ། །

[Block 1040]
འདི་ལ་གཙོ་བོ་བསྟན་པ་ལ་དངོས་གཞིར་གྱུར་པའི་ལུས་ལ་མངོན་པར་བརྟན་པ༌[^893]ཉིད་ཀྱིས་གནས་ཉིད་ཅེས་བྱ་བ་སྟེ།

[Block 1041]
དབྱར་རལ་བ༌[^894]ལ་ནི་མི་དབང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི་དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས། གང་ལས་སྦྱིན་པར་བྱ་ཞེ་ན། དབྱར་སྔ་མའམ་ཕྱི་མ་གང་ཡོད་པ་ལས་ཏེ། ཡུན་རིང་དུ་གནས་པ་ལས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1042]
ཐམས་ཅད་ཉིད་དམ་ཤིན་ཏུ་མང་པོར་གནས་པ་ཉིད་ཀྱིས་དབྱར་གྱི་རྙེད་པ་དེའི་རྒྱུས་དབང་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 1043]
འདིར་གནས་པ་ཙམ་རྒྱུ་ཡིན་གྱི། དབྱར་མ་རལ་བར་གནས་པ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1044]
གནས་ནས་བྱུང་བ་ཉིད་ནི་མི་དབང་ངོ་ཞེས་བྱ་བ་ནི་གནས་ནས་ཕྱུང་བ་ཉིད་དུ་གྱུར་པ་ན་ཐམས་ཅད་ཀྱིས་ཕལ་ཆེར་དབྱར་གནས་པའི་རྙེད་པ་དེ་ནི་མི་དབང་བ་ཉིད་དོ། །

[Block 1045]
རྫས་ཀྱིས་མནན་པར་གནས་པར་ཁས་བླངས་པ་ནི་སྐལ་བ་གཅིག་ཁོ་ནའོ་ཞེས་བྱ་བ་ནི་མཚམས་དུ་མ་ཁྲི་ལ་སོགས་པའི་རྫས་གཅིག་གིས་མནན་པས་ཁས་བླངས་པ་སྔོན་དུ་འགྲོ་བར་དུ་མ་མནན་པ་ལ་ཇི་སྲིད་དུ་མནན་པ་ཉིད་མ་ཡིན་པ་དེ་སྲིད་དུ་ཆ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 1046]
འོན་ཀྱང་སྐལ་བ་གཅིག་ཁོ་ན་སྦྱིན་པའོ། །

[Block 1047]
དེ་ལ་མནན་པ་རྣམས་སུ་བདག་ཉིད་བགྲང་བའི་ཆ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་བདག་ཉིད་བགྲང་བའི་ཆ་མཚམས་གང་ལ་ཡོད་པ་རྣམས་ནི་རང་གི་གྲངས་ཀྱི་ཆའོ།[^895] །མཚམས་ཀྱི་ཇི་སྙེད་ཁས་བླངས་ཤིང་མནན་པ་རྣམས་དེ་ཙམ་མོ། །

[Block 1048]
གྲངས་ཀྱི་ཆའི་དབྱེ་བ་གཅིག་གང་ཡིན་ན་དེ་ནི་དེ་ལས་སྐལ་བ་གཅིག་པ་ཉིད་ཅེས་བྱ་བར་བརྗོད་པ་ལ་ཆ་མནན་པའི་གནས་སྐབས་སུ་སྐལ་བ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1049]
འདིར་གཞུང་ནི་གཙུག་ལག་ཁང་ཅིག་སྙེད༌[^896]པའི་ཐང་གང་ཡིན་པ་དེ་དེས༌[^897]གནས་ཇི་སྙེད་མནན་པ་དེ་སྙེད་ནས་ཆ་བསྡུས་ཏེ། དེ་ལས་སྐལ་བ་གཅིག་སྦྱིན་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1050]
དེ་བཞིན་དུ་གནས་ལྷག་མ་རྣམས་ཀྱང་ཞེས་གསུངས་པ་དེ་བས་ན་འདི་མདོར་བྱས་སོ། །

[Block 1051]
གཞན་པ་གཅིག་ཏུ་གནས་པ་ཁས་བླངས་པ་ལ་ནི་ཡུན་རིང་བ་ཉིད་ཀྱིས༌[^898]རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་ལ། གཞན་པ་གཅིག་ཏུ་གནས་པར་ཁས་བླངས་པ་ལ་ཞེས་བྱ་བ་ནི་མནན་པའི་རྫས་མེད་པར་ཁས་བླངས་པ་ཞེས་གཞན་ལ་ཐ་དད་པར་ཁས་བླངས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1052]
དེ་དུས་ཡུན་རིང་དུ་གནས་པ་ཉིད་ཀྱིས་རྣམ་པར་གཞག་གོ།[^899] །གང་དུ་ཡུན་རིང་བར་གནས་པ་དེ་ཉིད་ལ་རྙེད་པ་འདི་སྦྱིན་པར་བྱའི་གཞན་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1053]
འདིར་གཞུང་ནི་གནས་མལ་གྱི་གཞི་ལས།

[Block 1054]
ཚེ་དང་ལྡན་པ་ཉེ་དགས་རྙེད་པ་འདོད་པས་གཙུག་ལག་ཁང་གཉིས་སུ་ཚུལ་ཤིང་དང་གནས་མལ་བླངས་ཏེ། གནས་མལ་ཁས་བླངས་པ་ན་དེས་གནས་གཙུག་ལག་ཁང་གཅིག་ནས་ཆོས་གོས་ཀྱི་རིན་ཐོབ་ལ། ཅིག་ཤོས་ནས་མ་ཐོབ་ནས།[^900] དེ་ནས་རྙེད་པ་སྒྲུབ་པ༌[^901]ན། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གང་དུ་གང་གསོ་སྦྱོང་ལན་མང་དུ་བྱས་པ་དེ་ནས་རྙེད་པ་བླང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1055]
དགེ་ཚུལ་དང་དགེ་ཚུལ་མ་ནི་རྙེད་པ་ལ་སུམ་ཆ་དབྲི་བ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། སུམ་ཆ་དབྲི་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སུམ་ཆ་དེ་ཆ་ཉིད་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
