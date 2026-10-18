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
[Block 946]
ཐམས་ཅད་ཅེས་བྱ་བ་ནི་དུས་གསུམ་པ་རྣམས་ཏེ། འདས་པའི་ལས་ཀྱི་འབྲས་བུ་དུས་གསུམ་པའི་ཆོས་ནི་བཞི་སྟེ།

[Block 947 [VERSE]]
བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །
བར་མ་ཡི་ནི་མ་འོངས་པའང་། །

[Block 948]
ད་ལྟར་བྱུང་བའི་ལས་ཀྱི་འབྲས་བུ་ཆོས་མ་འོངས་པ་ཡང་བཞི་སྟེ། དེ་དག་ཉིད་དོ། །

[Block 949]
བར་མ་གཉིས་སོ། །

[Block 950]
ད་ལྟར་བྱུང་བའི་འབྲས་བུ་ད་ལྟར་བྱུང་བའི་ཆོས་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུ་དག་གོ། །

[Block 951]
མ་སྐྱེས་པའི། འབྲས་བུ་མ་འོངས་གསུམ་ཡིན་ནོ། །

[Block 952]
མ་འོངས་པའི་འབྲས་བུ་མ་འོངས་པའི་ཆོས་ནི་གསུམ་སྟེ། རྒྱུ་མཐུན་པ་དང་བྲལ་བའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 953]
རང་གི་ས་པ་ཡིན༌[^702]ནོ། །

[Block 954]
རང་གི་ས་པའི་ལས་ཀྱི་འབྲས་བུ་རང་གི་ས་པའི་ཆོས་ནི་བཞི་སྟེ།

[Block 955 [VERSE]]
བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །
གཞན་གྱི་ས་པ་གསུམ་དང་གཉིས། །

[Block 956]
གལ་ཏེ་གཞན་གྱི་ས་པའི་ཆོས་ཟག་པ་མེད་པ་ཞིག་ཡིན་ན་ནི་འབྲས་བུ་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་བྲལ་བའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 957]
ཁམས་གསུམ༌[^703]མ་གཏོགས་པའི་ཕྱིར་རོ། །

[Block 958]
གལ་ཏེ་ཟག་པ་དང་བཅས་པ་ཞིག་ཡིན་ན་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་།

[Block 959 [VERSE]]
བདག་པོའི་འབྲས་བུ་དག་གོ། །
སློབ་པའི་སློབ་པ་སོགས༌[^704]པ་གསུམ། །

[Block 960]
སློབ་པའི་ལས་ཀྱི་འབྲས་བུ་སློབ་པའི་ཆོས་ནི་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་བྲལ་བའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 961]
མི་སློབ་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 962]
སློབ་པ་ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་པ་ཡང་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་རྒྱུ་མཐུན་པའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 963 [VERSE]]
མི་སློབ་ལས་ཀྱི་འབྲས་བུ་ནི། །
སློབ་པ་ཡི་ནི་ཆོས་ལ་སོགས། །
གཅིག་དང་གསུམ་དང་གཉིས་ཡིན་ནོ། །

[Block 964]
མི་སློབ་པའི་ལས་ཀྱི་འབྲས་བུ་སློབ་པའི་ཆོས་ནི་གཅིག་སྟེ། བདག་པོའི་འབྲས་བུའོ། །

[Block 965]
མི་སློབ་པ་ནི་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང༌[^705]བྲལ་བའི་འབྲས་བུ་དག༌[^706]མ་གཏོགས་སོ། །

[Block 966]
སློབ་པ་ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་པ་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུ་དག་གོ། །

[Block 967 [VERSE]]
དེ་ལས་གཞན་པའི་འབྲས་བུ་ནི། །
སློབ་སོགས་གཉིས་དང་གཉིས་དང་ལྔ། །

[Block 968]
སློབ་པ་དང་མི་སློབ་པ་དག་ལས་གཞན་པའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 969]
[^707]སློབ་པ་ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་པའི་ལས་ཀྱི་འབྲས་བུ་སློབ་པའི་ཆོས་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་། བདག་པོའི་འབྲས་བུ་དག་གོ། །

[Block 970]
མི་སློབ་པའང་དེ་དང་འདྲའོ། །

[Block 971]
སློབ་པ་ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་པ་ནི་འབྲས་བུ་ལྔ་ཆར་ཡིན་ནོ། །

[Block 972 [VERSE]]
མཐོང་བས་སྤང་བྱའི་དེ་ལ་སོགས། །
གསུམ་དང་བཞི་དང་གཅིག་ཡིན་ནོ། །

[Block 973]
མཐོང་བས་སྤང་བར་བྱ་བའི་ལས་ཀྱི་འབྲས་བུ་མཐོང་བས་སྤང་བར་བྱ་བའི་ཆོས་ནི་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་བྲལ་བའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 974]
བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི་བཞི་སྟེ། བྲལ་བའི་འབྲས་བུ་མ་གཏོགས་སོ། །

[Block 975]
སྤང་བར་བྱ་བ་མ་ཡིན་པ་ནི་གཅིག་སྟེ། བདག་པོའི་འབྲས་བུའོ། །

[Block 976]
བསྒོམ་པས་སྤང་བར༌[^708]བྱ༌[^709]ལས་ཀྱི། །དེ་དག་གཉིས་དང་བཞི་དང་གསུམ།[^710] །བསྒོམ་པས་སྤང་བར་བྱ་བའི་ལས་ཀྱི་འབྲས་བུ་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་གཉིས་ཏེ། སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི༌[^711]འབྲས་བུ་དག་གོ། །

[Block 977]
བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི་བཞི་སྟེ། བྲལ་བའི་འབྲས་བུ་དག༌[^712]མ་གཏོགས་སོ། །

[Block 978]
སྤང་བར་བྱ་བ་མ་ཡིན་པ་ནི་གསུམ་སྟེ། རྣམ་པར་སྨིན་པ་དང་རྒྱུ་མཐུན་པའི་འབྲས་བུ་དག་མ་གཏོགས་སོ། །

[Block 979 [VERSE]]
སྤང་བྱ་མིན་པའི་དེ་དག་གཅིག །
གཉིས་དང་བཞི་སྟེ་གོ་རིམས་བཞིན། །

[Block 980]
སྤང་བར་བྱ་བ་མ་ཡིན་པའི་ལས་ཀྱི་འབྲས་བུ་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་གཅིག་སྟེ་བདག་པོའི་འབྲས་བུའོ། །

[Block 981]
བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི་གཉིས་ཏེ།

[Block 982 [VERSE]]
སྐྱེས་བུ་བྱེད་པ་དང་བདག་པོའི་འབྲས་བུའོ། །
སྤང་བར་བྱ་བ་མ་ཡིན་པ་ནི༌[^713]བཞི་སྟེ།
རྣམ་པར་སྨིན་པའི་འབྲས་བུ་མ་གཏོགས་སོ། །

[Block 983]
ཡང་གོ་རིམས་བཞིན་ཞེས་སྨོས་པ་ནི་དབུས་སུ་ཡང་ཐོག་མ་དང་ཐ་མ་བཞིན་ཤེས་པར་བྱ་བའི་ཕྱིར་ཏེ། དེ་ནི་མཐུན་པར་སྦྱོར་བའི༌[^714]ཆོས་ཡིན་ནོ། །

[Block 984 [HEADING]]
### རིགས་པ་མ་ཡིན་པས་བསྐྱེད་པ་ལ་སོགས་པའི་ལས། ^1-57-0

[Block 985]
ལས་བསྟན་པའི་སྐབས་སུ་འདི་ཡང་ཡོངས་སུ་བྲི་བར༌[^715]བྱ་སྟེ།
--- END BLOCKS ---
