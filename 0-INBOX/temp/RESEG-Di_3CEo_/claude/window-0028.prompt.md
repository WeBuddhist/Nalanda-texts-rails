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
[Block 981]
འབྱུང་གྱུར༌[^376]རྣམ་གསུམ་ཕན་ཚུན་དུ། །ལྷན་ཅིག་འབྱུང་བ་དང་། སྐལ་བ་མཉམ་པ་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུ་དག་གིས་སོ། །

[Block 982]
དེ་ལ་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ནི་ལུས་དང་ངག་གི༌[^377]ལས་སེམས་ཀྱི་རྗེས་སུ་འཇུག་པ་ཕན་ཚུན་དུ་ཡིན་གྱི་གཞན་ནི་མ་ཡིན་ནོ། །

[Block 983]
སྐལ༌[^378]པ་མཉམ་པའིའོ། །

[Block 984]
རྣམ་པར་སྨིན་པའི་རྒྱུ་ནི་ལུས་དང་ངག་གི་ལས་གང་གི་རྣམ་པར་སྨིན་པ་མིག་ལ་སོགས་པ་གང་ཡིན་པའོ། །

[Block 985]
འབྱུང་བ་རྣམས་ཀྱི་དེ་རྣམས་གཅིག །འབྱུང་བ་ལས་གྱུར་པའི་གཟུགས་འབྱུང་བ་རྣམས་ཀྱི་ནི་རྣམ་པར་སྨིན་པའི་རྒྱུ་ཁོ་ན་ཡིན་ཏེ། ལུས་དང་ངག་གི་ལས་གང་གིས་འབྱུང་བ་རྣམས་རྣམ་པར་སྨིན་པའོ། །

[Block 986 [HEADING]]
### སེམས་གང་གི་མཇུག་ཐོགས་སུ་གང་འབྱུང་བ། ^2-4-0

[Block 987 [HEADING]]
#### སེམས་བཅུ་གཉིས། ^2-4-1-0

[Block 988]
སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་བྱེ་བྲག་མེད་པར་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་དུ་བཤད་ཀྱི་སེམས་གང་གི་མཇུག་ཐོགས་སུ་གང་འབྱུང་བ་མ་བཤད་པས་དེ་བརྗོད་པ། མདོར་བསྡུ་ན་སེམས་བཅུ་གཉིས་པོ་འདི་ལྟ་སྟེ།

[Block 989 [VERSE]]
འདོད་ཡིད་དགེ་དང་མི་དགེ་དང་། །
བསྒྲིབས་པ་དང༌[^379]ནི་མ༌[^380]བསྒྲིབས་པ། །
འདོད་པའི་ཁམས་ན་སེམས་བཞི་སྟེ། །

[Block 990]
དགེ་བ་དང་མི་དགེ་བ་དང་། བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དང་།

[Block 991 [VERSE]]
མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའོ། །
གཟུགས་དང་གཟུགས་མེད་པ་དག་ན། །

[Block 992]
མི་དགེ་ལས་གཞན། བཅུ་པོ་དེ་དག་ནི་ཟག་པ་དང་བཅས་པའི་སེམས་ཡིན་ནོ། །

[Block 993]
ཟག་མེད་གཉིས། སློབ་པ་དང་མི་སློབ་པ་སྟེ། དེ་ལྟར་ན༌[^381]དེ་དག་ནི་སེམས་བཅུ་གཉིས་ཡིན་ནོ། །

[Block 994]
དེ་ལ། འདོད་སེམས་དགེ་བ་ལས་སེམས་དགུ། །མཇུག་ཐོགས་སུ་ཞེས་འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 995]
འདི་ལྟ་སྟེ། རང་གི་ས་པ་བཞི་དང་། གཟུགས་ན་སྤྱོད་པ་གཉིས་དང་། སྙོམས་པར་འཇུག་པའི་ཚེ་དགེ་བ་དང་། ཉིང་མཚམས་སྦྱོར་བའི་ཚེ་བསྒྲིབས་པའོ། །

[Block 996]
གཟུགས་མེད་པ་ན་སྤྱོད་པ་ནི་བསྒྲིབས་པ་ཁོ་ནའོ། །

[Block 997]
སློབ་པ་དང་མི་སློབ་པ་ཞེས་སོ། །

[Block 998]
དེ་ནི་བརྒྱད་པོ་ཁོ་ན་ལས།

[Block 999]
འདོད་པ་ན་སྤྱོད་པའི་དགེ་བའི་སེམས་དེ་ཡང་ནི་བརྒྱད་ཀྱི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། རང་གི་ས་པ་བཞི་དང་། གཟུགས་ན་སྤྱོད་པ་གཉིས་ལས་ཏེ། ལྡང་བའི་ཚེ་དགེ་བ་དང་། ཉོན་མོངས་པ་ཅན་གྱི་སྙོམས་པར་འཇུག་པས་གཟིར་བའི་ཚེ་ས་འོག་མའི་དགེ་བ་ལ་བརྟེན་པའི་ཕྱིར་བསྒྲིབས་པ་དང་། ལྡང་བའི་ཚེ་སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །

[Block 1000]
མི་དགེ་བ་ནི་བཅུ་དག་ལས། །

[Block 1001]
སློབ་པ་དང་མི་སློབ་པ་མ་གཏོགས་པའོ། །

[Block 1002]
དེ་ལས་བཞི་སྟེ། རང་གི་ས་པ་དག་ཁོ་ནའོ། །

[Block 1003]
ཇི་ལྟར་འདོད་པའི་ཁམས་ཀྱི་མི་དགེ་བའི་སེམས་ཀྱི་བཤད་པ། བསྒྲིབས་དེ་བཞིན།

[Block 1004 [VERSE]]
མི་དགེ་བ་ཇི་ལྟ་བ་བཞིན་ནོ། །
མ་བསྒྲིབས་པ་ནི་ལྔ་དག་ལས། །

[Block 1005]
མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་སེམས་ནི་ལྔ་ལས་ཏེ། རང་གི་ས་པ་བཞི་དང་། གཟུགས་ན་སྤྱོད་པའི་དགེ་བ་ལས་སྤྲུལ་པའི་སེམས་སོ། །

[Block 1006]
དེ་ལས་མཇུག་ཐོགས་སེམས་བདུན་ནོ། །

[Block 1007]
རང་གི་བཞི་དང་། གཟུགས་ན་སྤྱོད་པ་གཉིས་ཏེ། སྤྲུལ་པའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་དགེ་བ་དང་། ཉིང་མཚམས་སྦྱོར་བའི་ཚེ་ཉོན་མོངས་པ་ཅན་དང་། དེ་བཞིན་དུ་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་ནོ། །

[Block 1008]
གཟུགས་ན་དགེ་ལས་བཅུ་གཅིག་གོ། །

[Block 1009]
གཟུགས་མེད་པ་ན་སྤྱོད་པ་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་མ་གཏོགས་པའོ། །

[Block 1010]
དེ་ནི་དགུ་ཡི་མཇུག་ཐོགས་སུ། །འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་གཉིས་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་མ་གཏོགས་སོ། །

[Block 1011]
བསྒྲིབས་པ་བརྒྱད་ལས།

[Block 1012]
འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་གཉིས་དང་། སློབ་པ་དང་། མི་སློབ་པ་གཉིས་མ་གཏོགས་སོ། །

[Block 1013]
དེ་ལས༌[^382]དྲུག་བསྒྲིབས་པ་ལས་རང་གི་ས་པ་གསུམ་དང་། འདོད་པ་ན་སྤྱོད་པའི༌[^383]མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་མ་གཏོགས་སོ། །

[Block 1014]
མ་བསྒྲིབས་པ་ནི་གསུམ་ལས་སོ། །

[Block 1015]
མ་བསྒྲིབས་པ་ནི་རང་གི་ས་པ་དག་ཁོ་ན་ལས་སོ། །

[Block 1016]
དེ་ལས་དྲུག་སྟེ། རང་གི་ས་པ་གསུམ༌[^384]དང་། འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་དང་། གཟུགས་མེད་པ་ན་སྤྱོད་པ་ཡང་ངོ་། །གཟུགས་ཀྱི་ཁམས་ཀྱི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་ཇི་སྐད་བཤད་པ་ལྟར། གཟུགས་མེད་པའང་དེའི་ཚུལ་ལོ། །

[Block 1017]
དེ་ན་ཡོད་པའི་ཡང་རང་གི་ས་པ་གསུམ་ཁོ་ན་ལས་འབྱུང་ལ། དེ་ལས་ཀྱང་རང་གི་ས་པ་གསུམ་པོ་དང་ས་འོག་མ་པའི་ཉོན་མོངས་པ་ཅན་རྣམས་དང་དྲུག་འབྱུང་ངོ་། །དགེ་བ་ལས་སེམས་དགུ་དག་གོ། །

[Block 1018]
གཟུགས་མེད་པ་ན་སྤྱོད་པའི་དགེ་བའི་སེམས་ལས་ནི་སེམས༌[^385]དགུ་འབྱུང་སྟེ། འདོད་པ་ན་སྤྱོད་པའི་དགེ་བ་དང་། འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་མ་བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པ་དག་མ་གཏོགས་སོ། །

[Block 1019]
དེ་དྲུག་གོ།[^386] །

[Block 1020]
རང་གི་ས་པ་གསུམ་དང་། གཟུགས་ན་སྤྱོད་པའི་དགེ་བ་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །
--- END BLOCKS ---
