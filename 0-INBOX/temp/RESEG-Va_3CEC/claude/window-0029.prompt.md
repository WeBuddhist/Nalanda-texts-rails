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
སེར་སྣ་མེད་པས་མ་ཞུམ་པར་སེམས་བསྐྱེད་པ་དང་ཞེས་བྱ་བ་ལ། སེར་སྣའི་དབང་གིས་དངོས་པོ་གཏོང་བར་མི་ནུས་པའམ། ཅུང་ཟད་གཏོང་གི་ཐམས་ཅད་མི་གཏོང་བ་ནི་ཞུམ་པར་སེམས་བསྐྱེད་པ་སྟེ། དགའ་བ་དང་ལྡན་པ་ལ་སེར་སྣ་མེད་པས༌[^883]དངོས་པོ་ཐམས་ཅད་གཏོང་བའི་ཕྱིར་མ་ཞུམ་པར་སེམས་བསྐྱེད་པའོ། །

[Block 1017]
སློང་བ་ལ་སྦྱིན་པ༌[^884]བྱིན་ནས་ཞེས་བྱ་བ་ལ་དེ་ལྟར་མ་ཞུམ་པའི་སེམས་ཀྱིས༌[^885]སློང་བ་པོའི་གང་ཟག་རྣམས་ལ་ཕྱི་དང་ནང་གི་དངོས་པོའི་སྦྱིན་པ་བྱིན་ནས་བདག་དང་སློང་བ་པོ་དང་། སྦྱིན་པ་གསུམ་ཆར་ཡང་གཏོང་བའི༌[^886]རང་བཞིན་དུ་ལྟ་བ་ནི་འཁོར་གསུམ་ཡོངས་སུ་དག་པར་སྦྱངས་པ་སྟེ། དེ་བས་ན་སྦྱིན་པ་ལ་མཆོག་ཏུ་དགའ་བ༌[^887]ཞེས་བྱའོ། །

[Block 1018]
ཚུལ་ཁྲིམས་དང་ལྡན་པ་རྣམས་ལ་དད་པ་ནི་གང་ཟག་ཚུལ་ཁྲིམས་དང་ལྡན་པ་རྣམས་ལ་སེམས་དང་བའོ། །

[Block 1019]
ཚུལ་ཁྲིམས་འཆལ་བ་རྣམས་ལ་རྗེས་སུ་འཛིན་ཅིང་བྱམས་པ་ཞེས་བྱ་བ་ལ་ཚུལ་ཁྲིམས་ཞིག་པའི་གང་ཟག་རྣམས་ནི་ཚུལ་ཁྲིམས༌[^888]འཆལ་བ་རྣམས་སོ། །

[Block 1020]
དེ་དག་མི་དགེ་བའི་ཆོས་ལ་ཕྱིས་མི་གཏོང་བ་ནི་རྗེས་སུ་འཛིན་པའོ། །

[Block 1021]
དགེ་བའི་གནས་སུ་བཀོད་ཅིང་ཕན་བཏགས་པ་ནི་བྱམས་པའོ། །

[Block 1022]
རང་གི་ཚུལ་ཁྲིམས་ཡོངས་སུ་དག་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། བདག་གི་ཚུལ་ཁྲིམས་ལེགས་པར་བསྲུངས་བས་ཚུལ་ཁྲིམས་ཀྱི་སྐྱོན་མེད་པའི་ཕྱིར་དེའི་རྒྱུས་ངན་སོང་གསུམ་དུ་མི་སྐྱེ་བས་ན་ངན་འགྲོའི་འཇིགས་པ་ཐམས་ཅད་ལས་ཤིན་ཏུ་འདའ་བས་དབུགས་འབྱིན་པའོ། །

[Block 1023]
དེ་བཞིན་གཤེགས་པའི་ཚུལ་ཁྲིམས་ལ་ཡོངས་སུ་བསྔོ་བ་དང་ཞེས་བྱ་བ་ལ། བདག་གི་ཚུལ་ཁྲིམས་ཡོངས་སུ་དག་པར་བྱེད་པས་དེ་ཡང་སངས་རྒྱས་ཀྱི་ཚུལ་ཁྲིམས་ཐོབ་པར་བྱ་བའི་ཕྱིར་སྔོ་བར༌[^889]བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1024]
སྡིག་པའི་ཆོས་ཀྱི་དབང་དུ་མི་འགྱུར་བས་ན་བརྟན་པའོ། །

[Block 1025]
ངོར་རུས་དང་རིགས་སྨོས་པའི་ཚིག་སྨྲ་བ་ནི་ནང༌[^890]དུ་བརྗོད་པའོ། །

[Block 1026]
ལྐོག་ནས་སྨྲ་བ་ནི༌[^891]ངན་དུ་སྨྲ་བ་སྟེ། དེ་དག་སྨྲས་ཀྱང་སེམས་མི་འཁྲུགས་པ་ནི་བཟོད་པའོ། །

[Block 1027]
ལན་དུ་ཚིག་ངན་པ་མི་སྨྲ་བ་ནི་ངེས་པའོ། །

[Block 1028]
བསམ་པ་དག་པ་ནི་ཁེ་དང་བཀུར་སྟི་ལ་ཆགས་པ་མེད་པའོ། །

[Block 1029]
སེམས་ལ་བརླངས་པ་མེད་པ་ནི་སེམས་ཅན་ལ་བརྡེག་པ་དང་གསད་པར༌[^892]བྱ་བའི་བསམ་པ་མེད་པའོ། །

[Block 1030]
གྱ་གྱུ་མེད་པ་ནི་སེམས་ཅན་ལ་གནོད་པ་བྱ་བའི་ཐབས་མི་ཚོལ་ཞིང་ཕྱི་རོལ་དགའ་བར་འདྲ་བར་སྟོན་ཀྱང་ནང་དུ་མི་དགའ་བར་གནས་པའི་སེམས་མེད༌[^893]པའོ། །

[Block 1031]
ཐམས་ཅད་ལ་ཕན་ཡོན་དུ་བལྟ་བ་ནི་སེམས་ཅན་ཐམས་ཅད༌[^894]ལ་ཕན་པར་ལྟ་བའམ། ཡང་ན་མཐོང་བ་དང་ཐོས་པ་ལ་སོགས་པའི་ཆོས་ཀུན་ཀྱང་དགེ་བའི་བསམ་པས་ཕན་ཡོན་དུ་མཐོང་གིས། འཁྲུག་པའི་གནས་སུ་མི་ལྟ་བ༌[^895]སྟེ། འཁྲུག་པའི་གནས་ཉིད་དུ་སྣང་བ་ཡང་རང་གི་བསམ་པ་ལས་གྱུར་པར་ཤེས་པའི་ཕྱིར་རོ། །

[Block 1032]
སྐྱོན་མེད་པར་ལྟ་བ་ནི་སེམས་ཅན་ལ་ཉེས་པ༌[^896]བྱ་བར་མི་སེམས་པའོ། །

[Block 1033]
ཡང་དག་པར་དགའ་བར་འགྱུར་བའི་ཆོས་ཀྱི་རྗེས་སུ་འཇུག་པ་ཞེས་བྱ་བ་ལ་ཡང་དག་པར་དགའ་བར་འགྱུར་བའི་ཆོས་དྲུག་པོ་སྟོན་པ་དང་ཆགས་པ་དང་ཚངས་པ་མཚུངས་པར་སྤྱོད་པའི༌[^897]མཁས་པ་རྣམས་ལ་བྱམས་པའི་ལུས་ཀྱི་ལས་དང་ལྡན་པ་དང་། བྱམས་པའི་ངག་གི་ལས་དང་། བྱམས་པའི་ཡིད་ཀྱི་ལས་དང༌[^898]ལྡན་པ་དང་། ཆོས་དང་ལྡན་ཞིང་ཆོས་ཀྱིས་ཐོབ་པའི་རྙེད་པ་ལྷུང་བཟེད་དུ་བླུགས་ཤིང་། ལྷུང་བཟེད་དུ་ཆུད་ཟིན་པ་རྣམས་ཀྱང་ཐུན་མོང་དུ་ཡོངས་སུ་ལོངས་སྤྱོད་པར་བྱེད་ཅིང་ཟས་མི་སྲི་བ་དང་། ཚུལ་ཁྲིམས་མཐུན་པར་ཞུགས་པ་དང་། ལྟ་བ་མཐུན་པར་ཞུགས་པ་སྟེ། དེ་ཡང་དག་པར་དགའ་བར་འགྱུར་བ། སྡུག་པར་བྱེད་པ། བླ་མར་བྱེད་པ་རྩོད་པ་མེད་པར་བྱེད་པའི་ཆོས་དྲུག་པོ་དེ་དག་གི་རྗེས་སུ་འཇུག་པར་བྱེད་པའོ། །

[Block 1034]
བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་སྟོན་པ་ལྟར་ཕངས༌[^899]སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་སྟོན་པ་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ལ་ནི་ལམ་སྟོན་པ་མིག་སྦྱིན་པར་བྱེད་པ་ཡིན་པས། ཕངས་པ་བཞིན་དུ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་ཡང་གཅེས་པར༌[^900]འཛིན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1035]
ཆོས་རྣམས་བདག་བཞིན་དུ་ཕངས་པར༌[^901]སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི། བདག་ལ་བདག་ཕངས་པ་བཞིན་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་ལ་ཡང་ཕངས་པར་འཛིན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1036]
དེ་བཞིན་གཤེགས་པ་རྣམས་ལ་སྲོག་བཞིན་དུ་ཕངས་པར་འཛིན༌[^902]ཞེས་བྱ་བ་ནི། ཇི་ལྟར་སྲོག་ནི་ལུས་གནས་པའི་རྒྱུའི་གཙོ་བོ་ཡིན་པས་གཅེས་པ་བཞིན་ནོ། །

[Block 1037]
དེ་བཞིན་གཤེགས་པ་ལ་ཡང་གཅེས་སུ་འཛིན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1038]
བླ་མ་རྣམས་ལ་ཕ་མ་བཞིན་དུ་ཕངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་བདག་པས་ན༌[^903]རྒན་ཞིང་ཡོན་ཏན་དང་ལྡན་པའི་གང་ཟག་ནི་བླ་མ་སྟེ། ཇི་ལྟར་ཕ་མ་ནི་འཛམ་བུའི་གླིང་སྟོན་པ་བསྐྱེད༌[^904]པ། གསོ་བར་བྱེད་པ་ཡིན་པས་གཅེས་པ་ཡིན་པ༌[^905]དེ་བཞིན་དུ་དེ་དག་ལ་ཡང་གཅེས་སུ་འཛིན་པའོ།[^906] །སེམས་ཅན་རྣམས་ལ་བུ་བཞིན་དུ་ཕངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་བུ་གཅིག་པ་གཅེས་ཤིང་ཕོངས་པས༌[^907]མི་བདེ་བར་མི་འགྱུར་བ་དང་། བདེ་བ་ལ་འཇོག་པ་བཞིན་དུ་སེམས་ཅན་རྣམས་ཀྱང་མི་བདེ་བར་མི་འགྱུར་ཞིང་བདེ་བ་ལ་འཇོག་པར་བྱེད་པའོ། །

[Block 1039]
མཁན་པོ་དང་སློབ་དཔོན་རྣམས་ལ་སངས་རྒྱས་བཞིན་དུ་ཕངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སངས་རྒྱས་ཀྱིས་འཇིག་རྟེན་དུ་བདེན་པ་བཞི་ལ་སོགས་པ་བཤད་ནས། སྡུག་བསྔལ་གྱི་གནས་ཐམས་ཅད་ལས་བཏོན་པ་བཞིན་མཁན་པོ་དང་སློབ་དཔོན་གྱིས་ཀྱང་ཆོས་བསྟན་པའི་སྒོ་ནས་སྡུག་བསྔལ་ཐམས་ཅད་ལས་འདོན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1040]
ནན་ཏན་རྣམས་ལ་ཡན་ལག་གི་དམ་པ་མགོ་བོ་བཞིན་དུ་ཕངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཡན་ལག་གི་དམ་པ་མགོ་ཡིན་པ་བཞིན་ནན་ཏན་གྱིས་བསྒྲུབ་པར་བྱ་བའི་ཆོས་འཕགས་པའི་ལམ་ལ་སོགས་པ་ལའང་གཅེས་སུ་འཛིན་པའོ། །

[Block 1041]
ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་ལ་རྐང་ལག་བཞིན་དུ་ཕངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རྐང་ལག༌[^908]མེད་ན་གང་དུ་ཡང་མི་ཕྱིན་པས་བགྲོད་པར་བྱ་བའི་གནས་སུ་འདོང་བ་རྣམས་ལ་རྐང་ལག་གཅེས་པ་བཞིན་མྱ་ངན་ལས་འདས་པར་འགྲོ་འདོད་པ་ཡང་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་མེད་ན་མི་ཕྱིན་པས༌[^909]རྐང་ལག་དང་འདྲ་བས་གཅེས་སུ་འཛིན་པའོ། །

[Block 1042]
ཆོས་སྨྲ་བ་རྣམས་ལ་ཡང༌[^910]རིན་པོ་ཆེ་ཐམས་ཅད་བཞིན་དུ་ཕངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་གསེར་དང་དངུལ་ལ་སོགས་པ་རིན་པོ་ཆེ་སྣ་ཚོགས་པ༌[^911]ཕངས་པ་བཞིན་དུ་ཆོས་སྨྲ་བ་རྣམས་ཀྱང་ཆོས་རིན་པོ་ཆེ་སྟོན་པའི་ཕྱིར་ཕངས་པར་འཛིན་པའོ། །

[Block 1043]
སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ལ་ཡིད་བཞིན་གྱི་ནོར་བུ་བཞིན་དུ་ཕངས༌[^912]སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཡིད་བཞིན་གྱི་ནོར་བུས་རེ་བ་ཡོངས་སུ་རྫོགས་པར་བྱེད་པས་གཅེས་པ་བཞིན་དུ་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པས་སངས་རྒྱས་ཀྱི་ཆོས་ཐམས་ཅད་ཀྱིས་ཀྱང་བསམ་པ་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 1044]
རྗེས་སུ་བསྟན་པ་རྣམས་ལ་དགའ་བའི་རྩེད་མོ་བཞིན་དུ་ཕངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་འདོད་པའི་ལོངས་སྤྱོད་ཅན་དག་ལ་དགའ་བའི་རྩེད་མོ་རོལ་མོ་རྣམ་པ་སྣ་ཚོགས་གཅེས་པ་བཞིན་དུ་རྣལ་འབྱོར་པ་ཉོན་མོངས་པ་འདུལ་བ་ལ་ཞུགས་པ་དག་ལ་ཡང་ཉོན་མོངས་པ་གང་གིས་རང་དབང་མེད་པར་གྱུར་པ་དེའི་གཉེན་པོ་མི་གཙང་བ་ལ་སོགས་པས་ཅི༌[^913]དགར་ཉོན་མོངས་པ་སྤོང་བར་བྱེད་པས་ཉོན་མོངས་པའི་གཉེན་པོ་རྗེས་སུ་བསྟན་པ་དེ་དག་ལ་གཅེས་སུ་འཛིན་པའོ། །

[Block 1045]
ཆོག་ཤེས་པ་རྣམས་ལ་ནད་མེད་པ་བཞིན་དུ་ཕངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ནད་མེད་པ་གཅེས་པ་ལྟར་ལྷུང་བཟེད་དང་ཆོས་གོས་ལ་སོགས་པས་ཆོག་ཤེས་པ་ལ་ཡང་གཅེས་སུ་འཛིན་ཏེ། ཆོག་མི་ཤེས་པའི་དབང་གིས༌[^914]ནི་ཚོལ་བ་དང་སྲུང་བ་ལ་སོགས་པའི་ཚེ་ལུས་དང་སེམས་ལ་མི་བདེ་བ་ཐམས་ཅད་སྐྱེད་པའི་ཕྱིར་རོ། །

[Block 1046]
ཆོས་བཙལ་བ་རྣམས་ལ་སྨན་བཞིན་དུ་ཕངས་སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་སྨན་གྱིས་ནད་སེལ་བ་བཞིན་ཆོས་བཙལ་བས་ཀྱང་ཉོན་མོངས་པའི་ནད་སེལ་བའི་ཕྱིར་རོ། །

[Block 1047]
སྐུལ༌[^915]ཞིང་དྲན་པ་རྣམས་ལ་སྨན་པ་བཞིན་དུ་ཕོངས༌[^916]སུ་འཛིན་པ་ཞེས་བྱ་བ་ནི་སྨན་པ༌[^917]ནད་མེད་པར་གྱུར་པའི༌[^918]ཐབས་དང་། སྨན་སྟོན་པ་བཞིན་དུ་སྐུལ་ཞིང་དྲན་པར་བྱེད་པས་ཀྱང་ཉོན་མོངས་པའི་ནད་སེལ་བས་སྟོན་པས་ཕངས་པའོ། །

[Block 1048 [HEADING]]
#### དགའ་བ་ཆེན་པོ་རྒྱ་ཆེར་བཤད་པའི་དོན་བསྡུ་ཞིང་དེའི་རང་བཞིན་མདོར་བསྟན་པ། ^2-3-2-0

[Block 1049]
དགའ་བ་ཆེན་པོ་རྒྱ་ཆེར་བཤད་པའི་དོན་བསྡུ་ཞིང་དེའི་རང་བཞིན་མདོར་བསྟན་པར་བྱ་བའི་ཕྱིར། གང་དབང་པོ་ཐམས་ཅད་ལ་དབང་པོ་མ་གོད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དབང་པོ་ཐམས་ཅད་དད་པ་ལ་སོགས་པའི་དབང་པོ་ལྔ་དང་མིག་ལ་སོགས་པའི་དབང་པོ་རྣམས་སོ། །

[Block 1050]
དབང་པོ་མ་གོད་པ་ནི་དབང་པོ་དེ་རྣམས་མ་ཉམས་ཤིང་མ་གོད་པ་སྟེ། དེ་ནི་དགའ་བ་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 1051]
རྟོགས༌[^919]པའི་ཡེ་ཤེས་ཀྱི་ཕྱིར་ཞི་བའི་རྣམ་པའོ་ཞེས་བྱ་བ་ནི་དབང་པོ་མ་ཞི་ཞིང་ཆགས་པར་འགྱུར་བའི་རྒྱུའི་ཆོས་རྣམས་རང་བཞིན་གྱིས་མ་བྱུང་མ་སྐྱེས་པར་རྟོགས་པས༌[^920]དེ་ལ་མ་གཡེངས་པའི་ཕྱིར་ཞི་བའི་རྣམ་པ་སྟེ། ཞི་བའི་རང་བཞིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1052]
མི་རྒོད་པའི་ཕྱིར་རབ་ཏུ་ཞི་བའི་རྣམ་པ་ཞེས་བྱ་བ་ནི་གོང་དུ་བཤད་པ་ལྟར་རྒོད་པར་བྱ་བའི་ཡུལ་མེད་པས་ན་རབ་ཏུ་ཞི་བའི་རྣམ་པའོ། །

[Block 1053]
ཁེངས་པ་མ་ཡིན་པའི་ཕྱིར་ཤིན་ཏུ་སྦྱངས་པའི་རྣམ་པའོ་ཞེས་བྱ་བ་ལ། [^921]ཉོན་མོངས་པ་རྣམས་མ་སྤངས་པ་ནི་ཁེངས་པ་སྟེ། ཉོན་མོངས་པ་མ་སྤངས་པ་མ་ཡིན་པ་ནི་ཁེངས་པ་མ་ཡིན་པའོ། །

[Block 1054]
དེ་བས་ན་ཤིན་ཏུ་སྦྱངས་པའི་རྣམ་པ་སྟེ། ཉོན་མོངས་པ་དག་པའི་རྣམ་པའམ།[^922] ཉོན་མོངས་པ་དུལ་བའི་རྣམ་པ་ཞེས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 1055]
རྣམ་པར་མི་གཡེངས་པའི་ཕྱིར་དབང་པོ་དགའ་བའི་རྣམ་པ་ཞེས་བྱ་བ་ནི་སེམས་གཡེངས་པ་ལས་དབང་པོ་འཁྲུག་པར༌[^923]འགྱུར་གྱི། སེམས་ཡུལ་ལ་སོགས་པ་ལ་མ་གཡེང་སྟེ།[^924] ཏིང་ངེ་འཛིན་དུ་གྱུར་པ་ལས་ཞི་ཞིང་དགའ་བར་འགྱུར་བས་ན་དབང་པོ་དགའ་བའི་རྣམ་པའོ། །
--- END BLOCKS ---
