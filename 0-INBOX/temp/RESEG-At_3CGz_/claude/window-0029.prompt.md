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
འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ༌[^569]ནས་ཀྱང་དོན་འདི་ལ་དགོངས་ནས།

[Block 1017 [VERSE]]
སེམས་ནི་སངས་རྒྱས་ཐམས་ཅད་ཀྱིས། །
མ་གཟིགས་གཟིགས་པ་མ་ཡིན་ཏེ། །
རང་བཞིན་མེད་པའི་ངོ་བོ་ལ། །
ཇི་ལྟ་བུ་ཞིག་གཟིགས་པར་འགྱུར། །

[Block 1018]
ཞེས་གསུངས་སོ། །

[Block 1019]
སློབ་དཔོན་འཕགས་པ་ལྷའི་ཞལ་ནས་ཀྱང་།

[Block 1020 [VERSE]]
རྣམ་ཤེས་དེ་ཡང་དོན་དམ་པར། །
དེ་ནི་མཁས་རྣམས་མི་བཞེད་དེ། །
གཅིག་དང་དུ་མ་བྲལ་བའི་ཕྱིར། །
ནམ་མཁའི་པདྨ་ཉིད་དང་མཚུངས། །

[Block 1021]
ཞེས་ཡེ་ཤེས་སྙིང་པོ་ཀུན་ལས་བཏུས་པ་ལས་གསུངས་སོ། །

[Block 1022]
འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་ནས།

[Block 1023 [VERSE]]
བདག་ཏུ་འཛིན་པ་བཟློག་དོན་དུ། །
ཕུང་པོ་ཁམས་ལ་སོགས་པ་བསྟན། །
སེམས་ཙམ་ཉིད་དུ་རྣམ་གནས་ནས། །
སྐལ་ཆེན་རྣམས་ཀྱིས༌[^570]དེ་དག་གཞོམ། །

[Block 1024 [VERSE]]
འདི་དག་ཐམས་ཅད་སེམས་ཙམ་ཞེས། །
ཐུབ་པ་ཡིས་ནི་གང་གསུངས་པ། །
བྱིས་རྣམས་སྐྲག་པ་སྤང་ཕྱིར་ཏེ། །
ཡང་དག་ཏུ་ནི་དེ་ཉིད་མིན། །

[Block 1025]
ཞེས་པ་དང་། ཡང་དེ་ཉིད་ལས་ཆོས་བདག་མེད་པ་འདི་ལྟ་བུ། །

[Block 1026 [VERSE]]
ཐེག་ཆེན་དག་ལ་དགའ་རྣམས་ཀྱི། །
རང་སེམས་གདོད་ནས་མ་སྐྱེས་པ། །
མདོར་བསྡུས༌[^571]ནས་ནི་དེ་ཡིན་ནོ། །

[Block 1027]
ཞེས་གསུངས་སོ། །

[Block 1028]
དེ་བས་ན༌[^572]ཕྱི་རོལ་པས་བརྟགས་པའི་བདག་ལ་སོགས་པ་དང་། རང་གི་སྡེ་པས་བརྟགས་པའི་ཕུང་པོ་ལ་སོགས་པ་དང་། སེམས་དང་སྒྱུ་མ་ལ་སོགས་པའི་རྟོག་པ་བསལ་བར་བྱས་ནས་དེ་ལྟ་བུའི་དོན་ལ་དུས་རྟག་ཏུ་གནས་ནས་རྣམ་པར་རྟོག་པ་སྤང་བར་བྱའོ། །

[Block 1029]
དེ་བས་ན་འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་ནས།

[Block 1030 [VERSE]]
བདག་དང་ཕུང་པོ་ལ་སོགས་དང་། །
རྣམ་ཤེས་རྟོག་པས་མ་བསྒྲིབས་པ། །
སངས་རྒྱས་རྣམས་ཀྱི་བྱང་ཆུབ་སེམས། །
སྟོང་པའི་མཚན་ཉིད་དག་ཏུ་བཞེད། །

[Block 1031]
ཅེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1032]
དེ་ལྟ་བུའི་རྣམ་པར་རྟོག་པ་སྤངས་པ༌[^573]ནི་མྱ་ངན་ལས་འདས་པའི་མཆོག་ཡིན་ནོ་ཞེས་སྨྲས་སོ། །

[Block 1033]
འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་མན་ངག་གིས་དངོས་གྲུབ་བརྙེས་ནས་འཕགས་པ་འཇམ་པའི་དབྱངས་ཀྱི་གནང་བ་ཐོབ་པ། མངོན་པར་ཤེས་པ་བརྙེས་པ། རྒྱུད་ཐམས་ཅད་དང་། མདོ་སྡེ༌[^574]ཐམས་ཅད་དང་། འདུལ་བའི་ལུང་མ་ལུས་པའི་དགོངས་པ་དུས་གཅིག་ཏུ་ཐུགས་ལ་གསལ་བ་བདེན་པ་གཟིགས་པ་དེས་ན་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་བླ་མ་ནི་དཔལ་བྱང་ཆུབ་བཟང་པོ་འདི་ཡིན་པས་འདིའི་རྗེས་སུ་འབྲང་བར་བྱའོ། །

[Block 1034]
སྔར་བཀོད་པའི་གཞུང་དེ་དག་གི་དོན་ནི་འདི་ཡིན་ཏེ།

[Block 1035 [VERSE]]
ཡང་དག་ཉིད་དུ་རྣམ་དཔྱད་ན། །
སྣང་བའི་ཆོས་ཅན་ཐམས་ཅད་དང་། །
གྲུབ་མཐའ་སོགས་ཀྱིས་བརྟགས་པ་ཀུན། །
འཁྲུལ་ཏེ་བརྫུན་པ་ཡིན་པར་འདོད། །

[Block 1036 [VERSE]]
དཔེར་ན་མིག་ནད་ནད་སྐྱོན་གྱིས། །
ཁབ་འཛག་པ་དང་སྐྲ་ཤད་དང་། །
ཟླ་གཉིས་སྦྲང་མའི་ཕུང་པོ་མཐོང་། །
དེར་འཛིན་པ་ཡི་ཤེས་པའང་ཡོད། །

[Block 1037 [VERSE]]
དཔེར་ན་གཉིད་ལོག་གཉིད༌[^575]དབང་གིས། །
བག་ཆགས་ཀྱིས་ནི་བདེ་སྡུག་དང་། །
གཟུགས་ལ་སོགས་པ་ཉམས་སུ་མྱོང་། །
དེར་འཛིན་པ་ཡི་ཤེས་པའང་ཡོད། །

[Block 1038 [VERSE]]
དེ་བཞིན་ཐོག་མ་མེད་པ་ནས། །
མ་རིག་མིག་ནད་ནད་སྐྱོན་གྱིས། །
ཕྱི་དང་ནང་གི་དངོས་པོ་མྱོང་། །
དེར་འཛིན་པ་ཡི་ཤེས་པའང་ཡོད། །

[Block 1039 [VERSE]]
ཡང་ན་ཐོག་མ་མེད་པ་ནས། །
མ་རིག་གཉིད་མཐུག༌[^576]ཆེན་པོ་ལོག །
བག་ཆགས་བཞི་ཡི་རྨི་ལམ་དེ། །
དེར་འཛིན་ཉམས་སུ་མྱོང་བ་ཡོད། །

[Block 1040 [VERSE]]
དོན་དམ་ཉིད་ལ་རྣམ་དཔྱད་ན། །
ཆོས་རྣམས་ཀྱི་ནི་ཆོས་ཉིད་པས། །
ལོག་པར་རྟོག་པ༌[^577]དེ་དག་གིས། །
ཡོད་དང་མེད་པར་སྒྲུབ་མི་ནུས། །

[Block 1041 [VERSE]]
དཔེར་ན་མིག་ནད་མ་རུང་བར།[^578] །
སྐྲ་ཤད་མེད་པར་བྱ་མི་ནུས། །
གང་ཚེ་མིག་ནད་རུང་བ་ན། །
སྐྲ་ཤད་ཡོད་པར་བྱ་མི་ནུས། །

[Block 1042 [VERSE]]
དཔེར་ན་མ་རིག་གཉིད་སངས་ན། །
རྨི་ལམ་མཐོང་བར་བྱ་མི་ནུས། །
ཇི་སྲིད་གཉིད་ནི་མ་སངས་པར། །
རྨི་ལམ་མེད་པར་བྱ་མི་ནུས། །

[Block 1043 [VERSE]]
གང་ཚེ་རབ་རིབ་ནད་སངས་དང་། །
གཉིད་ལོག་པ་ལས་སད་ཙ་ན། །
སྐྲ་ཤད་སོགས་དང་རྨི་ལམ་དང་། །
དེར་འཛིན་པ་ཡི་ཤེས་པའང་མེད། །

[Block 1044 [VERSE]]
དེ་བཞིན་མ་རིག་མིག་ནད་དང་། །
མ་རིག་གཉིད་མཐུག༌[^579]སད་པ་ན། །
སྣང་དང་བརྟགས་པའི་ཐམས་ཅད་དང་། །
ཉམས་སུ་མྱོང་བའི་ཤེས་པའང་མེད། །

[Block 1045 [VERSE]]
རྒྱུན་ཆད་མ་ཆད་ཅེས་བརྗོད་པ། །
གང་ཞིག་ཡོད་པ་དེ་རྒྱུན་ཆད། །
ཆོས་ཉིད་ལ་ནི་དེ་མེད་དེ། །
གློ་བུར་བྱིས་པས་བརྟགས་པར་ཟད། །

[Block 1046 [VERSE]]
དེ་བས་སློབ་དཔོན་ཞི་བའི་ལྷ། །
རྒྱུན་ཆད་པར་ནི་འདིར་མི་བཞེད། །
དེ་ཡི་གདམས་ངག་མེད་པ་དང་། །
རྒྱུན་ཆད་པ་ཡི་གཞུང་ཡིན་ཟེར། །

[Block 1047 [VERSE]]
འདི་ལ་བསལ་བྱ་ཅི་ཡང་མེད། །
གཞག་པར་བྱ་བ་ཅུང་ཟད་མེད། །
ཡང་དག་ཉིད་ལ་ཡང་དག་བལྟ། །
ཡང་དག་མཐོང་བས་རྣམ་གྲོལ་འགྱུར། །

[Block 1048 [VERSE]]
བདག་དང་གཞན་གྱི་གྲུབ་པའི་མཐའ། །
ཁ་ཅིག་ཆོས་རྣམས་ཡོད་པར་བསྒྲུབ། །
གཞན་དག་ཆོས་རྣམས་མེད་ཅེས་ཟེར། །
ཡང་དག་ཉིད་ལ་རྣམ་དཔྱད་ན། །

[Block 1049 [VERSE]]
ཡོད་ཅེས་པ་དང་མེད་ཅེས་པ། །
ཡང་དག་མཐའ་ལ་དེ་དག་མེད། །
དེ་བས་གར་ཡང་བསྒྲུབ་མི་ནུས། །
བླ་མའི་བརྒྱུད་པ་བྲལ་བ་དག །

[Block 1050 [VERSE]]
རྗེས་སུ་དཔག་པའི་ཤེས་རབ་ཀྱིས། །
ཡོད་མེད་རྟག་ཆད་སོགས་བསྒྲུབས་ཀྱང་། །
ངལ་འགྱུར་དོན་ལ་རེག་མི་འགྱུར། །
ཆོས་གྲགས་ཆོས་མཆོག་ལ་སོགས་པས། །

[Block 1051 [VERSE]]
གཞུང་མང་བྱས་པ་ཇི་ལྟ་བུ། །
མུ་སྟེགས་རྒོལ་བ་བཟློག་པའི་ཕྱིར། །
མཁས་པ་རྣམས་ཀྱིས་བྱས་པ་ཡིན། །
དེ་བས་དོན་དམ་བསྒོམ་པ་ལ། །

[Block 1052 [VERSE]]
ཚད་མས་དགོས་པ་མེད་དོ་ཞེས། །
བདག་གིས་གཞན་དུ་བཀོད་པས༌[^580]ན། །
རེ་ཞིག་འདིར་ནི་བརྗོད་མི་དགོས། །
དེ་བས་རྗེས་དཔག་གཙོར་བྱེད་པའི། །

[Block 1053 [VERSE]]
རྟོག་གེའི་གཞུང་རྣམས་དོར་བྱས་ལ། །
འཕགས་པ་ཀླུ་སྒྲུབ་གཞུང་ལུགས་ཀྱི།[^581] །
བརྒྱུད་པའི་མན་ངག་བསྒོམ་པར་བྱ། །
ཡོད་མིན་མེད་མིན་ཡོད་མེད་མིན། །

[Block 1054 [VERSE]]
གཉི་ག་མིན་པའང་མ་ཡིན་པའི། །
མཐའ་བཞི་ལས་ནི་རྣམ་གྲོལ་བའི། །
དེ་ཉིད་དབུ་མ་པ་ཡིས་རིག །
རྟག་མིན་ཆད་མིན་རྟག་ཆད་མིན། །

[Block 1055 [VERSE]]
གཉི་ག་མིན་པའང་མ་ཡིན་པའི། །
མུ་བཞི་ལས་ནི་རྣམ་གྲོལ་བའི། །
དེ་ཉིད་དབུ་མ་པ་ཡིས་རྟོགས། །
ཡོད་མེད་ལྟ་བུ་ལས་འདས་ཤིང་། །
--- END BLOCKS ---
