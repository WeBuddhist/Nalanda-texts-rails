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
[Block 1051]
མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་དག་ཁོ་ན་ལས་སོ། །

[Block 1052]
སྤྲུལ་སེམས་ཕྱི་ནས་གཉིས། མངོན་པར་ཤེས་པའི་འབྲས་བུ་རང་ཉིད་དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བའོ། །

[Block 1053]
དེ་ཡང་གཉིས་ལས་བྱུང་། དེ་ཁོ་ན་ལས་སོ། །

[Block 1054]
འདོད་པ་ལས༌[^399]སྐྱེས་པ། བརྒྱད་པོ་དག་གོ། །

[Block 1055]
གཟུགས་གཏོགས་བརྗོད། སྦྱོར་བ་ལས་བྱུང་ལས༌[^400]བཅུ་གཉིས། །འདོད་པ་ན་སྤྱོད་པའི་དགེ་བ་དག་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དང་། རང་གི་དྲུག་དང་། གཟུགས་མེད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། སློབ་པ་དང་། མི་སློབ་པའོ། །

[Block 1056]
དེ་ཡང་སེམས་བཅུའི་མཇུག༌[^401]ཐོགས་སུ། འདོད་པ་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དག་དང་། སྤྱོད་ལམ་པ་དང་། རྣམ་པར་སྨིན་པ་ལ༌[^402]སྐྱེས་པ་དག་མ་གཏོགས་པ་རང་གི་བཞི་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། ཉོན་མོངས་པ་ཅན་དག་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །

[Block 1057]
སྐྱེས་ནས་ཐོབ་པའི་མཇུག་ཐོགས་བརྒྱད། །འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་ལྔ་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་ནོ། །

[Block 1058]
དེ་ནི་ལྔ་ལས།

[Block 1059]
མཇུག་ཐོགས་སུ་མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་དག་ཁོ་ན་ལས་སོ། །

[Block 1060]
བསྒྲིབས་ལས་དགུ། འདོད་པ་ན་སྤྱོད་པའི་དགེ་བ་དང་། ཉོན་མོངས་པ་ཅན་དག་སྟེ། བཞི་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་ལྔའོ། །

[Block 1061]
དེ་ཡང་སེམས་ནི་བཅུ་གཅིག་ལས།

[Block 1062]
འདོད་པ་ན་སྤྱོད་པའི་སྐྱེས་ནས་ཐོབ་པ་དང་། སྤྱོད་ལམ་པ་དང་། རྣམ་པར་སྨིན་པ་ལས༌[^403]སྐྱེས་པ་དག་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་ལྔ་དང་། སྦྱོར་བ་ལས་བྱུང་བ་མ་གཏོགས་པ་གཟུགས་མེད་པ་ན་སྤྱོད་པ་གསུམ་ལས་སོ། །

[Block 1063]
རྣམ་སྨིན་སྐྱེས་དང་སྤྱོད་ལམ་ལས། །

[Block 1064]
བདུན་ནོ། །

[Block 1065]
འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་དང་། སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་གཞི༌[^404]དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ༌[^405]ཅན་ནོ། །

[Block 1066]
དེ་དག་ལྔ་ཉིད་ལས།

[Block 1067]
མངོན་པར་ཤེས་པའི་འབྲས་བུ་མ་གཏོགས་པ་རང་གི་དག་ཁོ་ན་ལས་སོ། །

[Block 1068]
སྤྲུལ་སེམས་ལས་གཉིས། རང་གི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། མངོན་པར་ཤེས་པའི་འབྲས་བུ་དག་ཁོ་ནའོ། །

[Block 1069]
དེ་གཉིས་ལས།

[Block 1070]
དེ་ཁོ་ན་ལས་སོ། །

[Block 1071]
གཟུགས་སུ་གཏོགས་པ་བཤད་ནས། གཟུགས་མེད་པར་གཏོགས་པར༌[^406]བརྗོད་དེ།

[Block 1072]
གཟུགས་མེད་གཏོགས་པའི་མཇུག་ཐོགས་སུ། །སྦྱོར་བ་ལས་བྱུང༌[^407]སེམས་བདུན་ནོ། །

[Block 1073]
གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། རང་གི་བཞི་དང་། སློབ་པ་དང་མི་སློབ་པའོ། །

[Block 1074]
དེ་དྲུག་ལས་གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་མ་གཏོགས་པ་རང་གི་གསུམ་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །

[Block 1075]
སྐྱེས་ནས་ཐོབ་པའི། མཇུག་ཐོགས་སུ་ནི་སེམས་བདུན་ཏེ། །རང་གི་བཞི་དང་། ས་འོག་མའི་ཉོན་མོངས་པ་ཅན་དག་གོ། །

[Block 1076]
དེ་ཡང་བཞི་ལས།

[Block 1077]
རང་གི་དག་ཁོ་ན་ལས་སོ། །

[Block 1078]
བསྒྲིབས་ལས་བརྒྱད། རང་གི་བཞི་དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། ཉོན་མོངས་པ་ཅན་དག་དང་། འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་གོ། །

[Block 1079]
དེ་ཡང་བཅུ་ཡི་མཇུག་ཐོགས་སུ། །རང་གི་བཞི་དང་། འདོད་པ་དང་། གཟུགས་ན་སྤྱོད་པའི་སྐྱེས་ནས་ཐོབ་པ་དང་། སྤྱོད་ལམ་པ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དག་ལས་སོ། །

[Block 1080]
རྣམ་སྨིན་སྐྱེས་ལས་དྲུག །སྦྱོར་བ་ལས་བྱུང་བ་མ་གཏོགས་པ་རང་གི་གསུམ་དང་། འོག་མའི་ཉོན་མོངས་པ་ཅན་གསུམ་མོ། །

[Block 1081]
བཞི་ལས།

[Block 1082]
དེ་ཡང་རང་གི་དག་ཁོ་ན་ལས་སོ། །

[Block 1083]
སློབ་པའི་མཇུག་ཐོགས་དྲུག །ཁམས་གསུམ་པའི་སྦྱོར་བ་ལས་བྱུང་བ་རྣམས་དང་། འདོད་པ་ན་སྤྱོད་པའི་སྐྱེས་ནས་ཐོབ་པ་དང་། སློབ་པ་དང་མི་སློབ་པའོ། །

[Block 1084]
དེ་ཡང་བཞི་ལས།

[Block 1085]
སྦྱོར་བ་ལས་བྱུང་བ་གསུམ་དང་། སློབ་པ་ལས་སོ། །

[Block 1086]
མི་སློབ་པ་ལས་ནི་ལྔ་སྟེ། སློབ་པའི་གཅིག་པུ་མ་གཏོགས་པ་སློབ་པའི་མཇུག་ཐོགས་སུ་ལྔ་པོ་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 1087]
དེ་ཡང་དེ་གཉིས༌[^408]ལས།

[Block 1088]
མི་སློབ་པ་ནི༌[^409]ལྔ་ཁོ་ན་ལས་ཏེ། སྦྱོར་བ་ལས་བྱུང་བ་གསུམ་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །

[Block 1089]
ཅིའི་ཕྱིར་སྦྱོར་བ་ལས་བྱུང་བའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་ནི་རྣམ་པར༌[^410]སྨིན་པ་ལས་སྐྱེས་པ་དང་། སྤྱོད་ལམ་པ་དང་། བཟོའི་གནས་པའི་སེམས་དག་འབྱུང་ལ། སྦྱོར་བ་ལས་བྱུང་བ་ནི་དེ་དག་ལས་མ་ཡིན་ཞེ་ན།

[Block 1090 [VERSE]]
མངོན་པར་འདུ་བྱེད་ཞུགས་པའི་ཕྱིར། །
སྟོབས་ཆུང་ཕྱིར་དང་འབད་མེད་ཕྱིར། །
སྦྱོར་བ་ལས་བྱུང་རྗེས་མཐུན་མིན། །
དེའི་ཕྱིར་དེ་ཡི་མཇུག་ཐོགས་མིན། །
--- END BLOCKS ---
