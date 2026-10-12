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
བཅུ་པ་ནི་ཧ་སྟེ་གང་གིས་གང་གི་དོན་དུ་གནས་པ་ཉིད་དོ། །

[Block 982]
ཡང་ན་སུམ་ཅུ་པ་ནི་ཀྵ་སྟེ། ཆ་གཉིས་པོ་ནི༌[^473]ཀྵའོ། །

[Block 983]
དགུ་པ་ནི་དེ་ཉིད་དོ། །

[Block 984]
བཅུ་པ་ནི་ལའོ། །

[Block 985]
ལྔ་པ་ནི་ཧའོ། །

[Block 986]
ཆ་གཉིས་པ་ནི་ཨ་ཨཱ་ཞེས་པ་སྟེ། དེས་དེ་ལྟར་འགྱུར་རོ། །

[Block 987]
དྲུག་པ་ནི་ཨཱུ་སྟེ། གང་ལ་གང་གིས་ཉེ་བར་མཛེས་པའོ། །

[Block 988]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ཟབ་པ་དང་མི་ཟབ༌[^474]པ་གཉིས་ལ་དགོངས་ནས་གསུངས་པར་རིག་པར་བྱའོ། །

[Block 989]
གང་གིས་འདི་དང་བཅས་པ་དང་ལྡན་པ་ལས་འདིར་གཅིག་གཟུང་བར་བྱའོ། །

[Block 990]
འདི་དག་ལ་ཡང་ཅིའི་ཕྱིར་སྤྱི་ཞེས་བྱ་ཞེ་ན། གོང་དུ་བཤད་པ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 991]
སྦས་པའི་དོན་དུ་བཤད་པ་རྒྱས་པར་འདོད་ནས་གསུངས་པ། ལུང་གིས་བཤད་པ་ཞེས་པ་ནི་རིགས་པ༌[^475]དང་བྲལ་ཞིང་རྟོག་གེ་པ་རྣམས་ཀྱི་ཡུལ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 992]
ཨེ་ནི་ཤེས་རབ་དམ་པ་སྟེ། །ཞེས་པ་ནི་ཨེ་ནི་ཤེས་རབ་སྣང་བའི་མཚན་ཉིད་དོ། །

[Block 993]
འདི་ཅིའི་ཕྱིར་བཤད་སྙམ་པ་ལ། གང་གིས་སེམས་ལ་དམིགས་པ་ལ་སོགས་པ་གང་ཞིག་ཡོངས་སུ་གསལ་བར་བྱ་བའི་ཕྱིར་རོ། །

[Block 994]
གང་ཡང་སྦས་པ་གསུམ་པོ་ཉིད༌[^476]འདིས་རྟོགས་པར༌[^477]བྱ་བའི་ཕྱིར་ཡང་འདི་དག་རྒྱས་པར་འཆད་པར་འགྱུར་རོ། །

[Block 995]
དེ་བས་ན་གང་གིས་གང་གི་དོན་དུ་གང་ཞིག་བྱེད་པ་དེས་ནི་དེའི་དེ་དག་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ། །

[Block 996]
བདག་ཉིད་དམ་པ་ཡོངས་སུ་རྫོགས་པར་འདོད་པ་དེས་ཀྱང་འདི༌[^478]ལ་བརྟེན་ནས་འདི་དག་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ། །

[Block 997]
[^479]སྣང་བའི་བྲལ་ཚུལ་དང་རང་བཞིན་གང་ཞེ་ན། འདོད་ཆགས་བྲལ་སོགས་ཞེས་པ་འདོད་ཆགས་དང༌[^480]བྲལ་བ་དང་འདོད་ཆགས་དང་བྲལ་བ་བར་མ་དང་། ཤིན་ཏུ་འདོད་ཆགས་དང་བྲལ་བ་དང་། གང་ཡིད་ཀྱིས་འགྲོ་བ་དང་འོང་བ་དང་། མྱ་ངན་དང་མྱ་ངན་བར་མ་དང་། ཤིན་ཏུ་མྱ་ངན་དུ་གྱུར་པ་དང་། ཞི་བ་དང་རྣམ་པར་རྟོག་པ་དང་། འཇིགས་པ་དང་འཇིགས་པ་བར་མ་དང་། ཤིན་ཏུ་འཇིགས་པ་དང་། སྲེད་པ་དང་། སྲེད་པ་བར་མ་དང་། ཤིན་ཏུ་སྲེད་པ་དང་། ཉེ་བར་ལེན་པ་དང་། མི་དགེ་བ་དང་། བཀྲེས་པ་དང་། སྐོམ་པ་དང་། ཚོར་བ་དང་། ཚོར་བ་བར་མ་དང་། ཤིན་ཏུ་ཚོར་བ་དང་། རིག་པ་པོ་དང་། རིག་པ་དང་། རིག་པ་འཛིན་པའི་གཞི་དང་། སོ་སོར་རྟོག་པ་དང་། ངོ་ཚ་ཤེས་པ་དང་། སྙིང་རྗེ་བ་དང་། སྙིང་བརྩེ་བ་དང་། བརྩེ་བ་བར་མ་དང་། ཤིན་ཏུ་བརྩེ་བ་དང་། དོགས་པ་དང་བཅས་པ་དང་། སྡུད་པ་དང་། ཕྲག་དོག་སྟེ་འདི་དག་ནི་སྣང་བའི་རང་བཞིན་ནོ། །

[Block 998]
དེ་ཡང་གང་ཞེ་ན། འདོད་ཆགས་དང་བྲལ་བ་ནི་ཡིད་དུ་འོང་བ་མཐོང་བ་ལ་མ་ཆགས་པའོ། །

[Block 999]
བར་མ་ལ་སོགས་པ་ནི་ཅི་རིགས་པའོ། །

[Block 1000]
ཡིད་ཀྱིས༌[^481]འགྲོ་བ་དང་འོང་བ་གང་ཡིན་ཞེ་ན། འགྲོ་བ་དང་འོང་བ་ལ་སེམས་རྣམ་པར་གཡོ་བའོ། །

[Block 1001]
མྱ་ངན་གང་ཞེ་ན། སྡུག་པ་དང་བྲལ་བར་གྱུར་ནས་སེམས་ཤིན་ཏུ་གདུང་བའོ། །

[Block 1002]
འདི་ཡང་ཅི་རིགས་སུ་སྦྱར་རོ། །

[Block 1003]
ཞི་བ་གང་ཞེ་ན། སེམས་གཡེང་བ་དང་བྲལ་བའོ། །

[Block 1004]
རྣམ་པར་རྟོག་པ་གང་ཞེ་ན་སེམས་པ༌[^482]དང་ཤེས་རབ་རྩིང་བའོ། །

[Block 1005]
འཇིགས་པ་གང་ཞེ་ན་ཡིད་དུ་མི་འོང་བ་དང་ཕྲད་ནས་སེམས་སྐྲག་པའོ། །

[Block 1006]
འདི་ལ་ཡང་ཅི་རིགས་སུ་སྦྱར་རོ། །

[Block 1007]
སྲིད་པ་གང་ཞེ་ན། ཕན་འདོགས་པ་དང་ཡིད་དུ་འོང་བ་ལ་ཞེན་པའི་བདེ་བའི་ཚོར་བ་ལས་བྱུང་བའོ། །

[Block 1008]
འདི་ཡང་ཡུལ་གྱི་བྱེ་བྲག་ལས་ཅི་རིགས་སུ་སྦྱར་རོ། །

[Block 1009]
ཉེ་བར་ལེན་པ་གང་ཞེ་ན། གཞན་གྱི་ནོར་དང་ཡོ་བྱད་ལ་སོགས་པ་གང་ཡིད་ཀྱིས་ལེན་པ་སྟེ་སྲེད་པ་ལས་བྱུང་བའོ། །

[Block 1010]
མི་དགེ་བ་གང་ཞེ་ན་འདོད་ཆགས་ལ་སོགས་པ་དང་། དེ་དང་མཚུངས་པར་ལྡན་པའི༌[^483]ལུས་ངག་གི་ལས་སོ། །

[Block 1011]
བཀྲེས་པ་གང་ཞེ་ན་རྒྱུད་པས༌[^484]ཟས་འདོད་པའོ། །

[Block 1012]
སྐོམ་པ་གང་ཞེ་ན། ཡོངས་སུ་གདུང་བས༌[^485]སྐོམ་འདོད་པའོ། །

[Block 1013]
ཚོར་བ་གང་ཞེ་ན། བདེ་བ་དང་སྡུག་བསྔལ་བ་དང་གཉི་ག་དང་བྲལ་བའི་རྣམ་པ་ཡོངས་སུ་མྱོང་བའོ། །

[Block 1014]
རིག་པ་པོ་གང་ཞེ་ན། གང་གིས་གང་གི་རྣམ་པ་འཛིན་པའི་ཤེས་པའོ། །

[Block 1015]
རིག་པ་འཛིན་པ་གང་ཞེ་ན་གང་ཞིག་གང་གིས་བརྟེན་ཞིང་གང་ལ༌[^486]དམིགས་པའོ། །

[Block 1016]
གཞི་གང་ཞེ་ན་ཡུལ་གྱི་དངོས་པོ་ཉིད་དོ། །

[Block 1017]
སོ་སོར་རྟོག་པ་གང་ཞེ་ན་རིགས་པ༌[^487]དང་མི་རིགས་པ་གང་དུ་འཚོལ་བ༌[^488]དང་འདས་པ་སྟེ་སྤྱོད་པ་ཉིད་དོ། །

[Block 1018]
ངོ་ཚ་ཤེས་པ་གང་ཞེ་ན་བདག་གམ་ཆོས་ཀྱི་དབང་དུ་བྱས་ཏེ་ཁ་ན་མ་ཐོ་བ༌[^489]འཛེམ་པའོ། །

[Block 1019]
སྙིང་རྗེ་གང་ཞེ་ན་གང་ཞིག་གང་གིས༌[^490]རྣམ་པ་དང་བྲལ་བར་འདོད་པའོ། །

[Block 1020]
བརྩེ་བ་གང་ཞེ་ན་གང་ཞིག་གང་དང་བྲལ་ནས་དེ་དང་ཕྲད་པར་འདོད་པའོ། །
--- END BLOCKS ---
