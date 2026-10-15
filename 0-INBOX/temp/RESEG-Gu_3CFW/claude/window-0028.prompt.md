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
དེ་དག་གི་སྔགས་ནི། ཚེ་དང་ལྡན་པ་དགོངས་སུ་གསོལ་བདག་མིང་འདི་ཞེས་བྱ་བའི་ཆོས་གོས་བགྱིས་ལགས་པ་རུང་བར་སྤྱད་པར་འོས་པ་འདི་ཆོས་གོས་སྣམ་སྦྱར་དུ་བྱིན་གྱིས་བརླབ་པོ། །ལན་གསུམ་བཟླས། དེ་བཞིན་དུ་བླ་གོས་ནས་དབྱར་གྱི་གོས་རས་ཆེན་གྱི་མཐར་ཐུག་པ་རྣམས་ལ་ཡང་བརྗོད་པར་བྱའོ། །

[Block 982]
ཡོ་བྱད་ཀྱི་གོས་ཀྱང་ངོ་། །དེ་ནི་དཀར་པོ་ཉིད་དང་། ཁ་ཚར་དང་། ཕུན་ཚར་དང་བཅས་པ་ལ་ཡང་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་ཡོ་བྱད་ཀྱི་གོས་འཆང་བ་དེའོ། །

[Block 983]
དགེ་འདུན་གྱི་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡོ་བྱད་ཀྱི་གོས་ཀྱང་དཀར་པོ་དང་། ཁ༌[^839]ཚར་དང་ཕུན་ཚར་དང་བཅས་པ་འཆང་བ་ལ་ཡང་ཉེས་པ་མེད་པའོ། །

[Block 984]
འདིར་གཞུང་ནི། དེ་ལྟ་བས་ན་དགེ་འདུན་གྱིས༌[^840]གོས་དག་ནི་སར་པ་དང་། ཁར་ཚར༌[^841]དང་ཕུན་ཚར་རིང་པོ་དག་ཀྱང་བཅང་བར་གནང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 985]
གཞན་དུ་མ་ཡང༌[^842]རུང་བར་བྱ་སྟེ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་འཆང་བའི་ཉེས་པ་མེད་པར་རྗེས་སུ་གནང་བར་བྱས་སོ། །

[Block 986]
སྐྱོན་མང་པོ་མཐོང་བ་མི་རིགས་པའི་བློ་ལ་འབབ་སྟེ། དེ་བཟློག་པའི་དོན་དུ་དེའོ། །

[Block 987]
སེམས་མི་བརྟན་པ་ལ་རུང་བར་མི་བྱའོ། །

[Block 988]
བསྙེན་པར་མ་རྫོགས་པ་ལ་མི་བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་གཞུང་ནི། དགེ་སློང་དག་དགེ་ཚུལ་ལ་གོས་དག་ཏུ༌[^843]རུང་བར་བྱེད་ན། དེས་གོས་ཀྱི་ཕྲེང་བ་ཕུལ་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བསྙེན་པར་མ་རྫོགས་པ་ལ་གོས་དག་རུང་བར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 989]
མངོན་སུམ་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི། གང་ལ་རུང་བར་བྱ་བ་དེའི་མངོན་སུམ་དུ་རུང་བར་མི་བྱའོ། །

[Block 990]
ཡུལ་གཞན་དུ་གནས་པར་གྱུར་པ་ཉིད་ཡིན་ན་ཡང་རུང་བ་མི་ཉམས་སོ། །

[Block 991]
ཤིན་ཉམས་སོ་ཞེས་བྱ་བ་ནི་གང་གི༌[^844]མིང་གིས་རུང་བར་བྱས་པ་དེ་ཡུལ་གཞན་དུ་གནས་པར་གྱུར་ཀྱང་རུང་སྟེ། དེ་མི་ཉམས་སོ། །

[Block 992]
གང་ལ་རུང་བར་བྱས་པ་དེ་ཤིན་ཏུ་རུང་བར་ཉམས་པའོ། །

[Block 993]
ཅི་གང་གི་ཚེ་ཤི་བ༌[^845]དེའི་ཚེ་ཁོ་ན་ན་དེ༌[^846]ཉམས་སམ་ཞེ་ན། དེའི་ཕྱིར་ཤེས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཤི་བར་ཤེས་ནའོ། །

[Block 994]
འདི་ལ་རུང་བར་བྱེད་པ་བདག་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རུང་བར་བྱས་པའི་དངོས་པོ་འདི་ལ་གང་ཞིག་རུང་བར་བྱེད་པའོ། །

[Block 995]
སྤངས་པ་བདག༌[^847]གིར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱིས་སམ་གང་ཟག་གིས་སོ། །

[Block 996]
དགེ་སློང་ལ་སྤང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 997]
མི་གསལ་བ༌[^848]ལ་ཡང་མི་བྱའོ། །

[Block 998]
མ་བྱིན་པར་ནི༌[^849]བླང་ངོ་ཞེས་བྱ་བ་ནི་སྤངས་པའི་གོས་གང་ལ་དེས་ཕྱིར་མ་བྱིན་ན་སྤོང་བར༌[^850]བྱེད་པས་ཕྱིར་བླང་བར་བྱའོ། །

[Block 999]
མཐུས་ཀྱང་དགུག་གོ་ཞེས་བྱ་བ་ནི་མ་བྱིན་ན་ཞེས་རྗེས་སྙེགས༌[^851]པའི་ཕྱིར་ཀྱང་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 1000]
གོས་དྲི་མ་དག་གིས་གོས་པ་བཀྲུས་ཏེ་བགོ་བར་བྱའོ། །

[Block 1001]
ཕྱེ་མ་དག་གིས་ནི་སྤྲུགས་ཏེའོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་དག་པའི་གོས་ལ་ལོངས་སྤྱད་པའོ། །

[Block 1002]
སྣུམ་གྱིས་ནི་རྩུབ་པར་བྱས་ཏེའོ་ཞེས་བྱ་བ་ནི་གོས་སྣུམ་གྱིས་གོས་ན་ཐལ་ཆུ་ལ་སོགས་པས་རྩུབ་པར་བྱས་ཏེ་བགོ་བར་བྱའོ། །

[Block 1003]
དེ་དག་གི༌[^852]ནི་མི་སྡུག་པ་བསལ་བ་ཡིན་གྱི། གསོག་འཇོག་ཏུ་གྱུར་པ་ནི་མ་ཡིན་ཏེ། མི་བདེན་པ་དེ་གང་ཞིག་འདིར་ཁ་ཅིག་ནི་འདོད་པ་དེ་གསོག་འཇོག་ནི་ཟས༌[^853]དང་འབྲེལ་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1004]
ཆར་འབབ་པའི་ཚེ་བླ་གབ༌[^854]མེད་པར་དགེ་འདུན་གྱི་མི་བགོའོ་ཞེས་བྱ་བ་ནི་བགོ་བར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1005]
བཀྲུ་བཤལ་དང་ཚོན་དང་ལྷུང་བཟེད་ཀྱི༌[^855]ལས་དང་ཤིང་གཤེག་པ་ལ་སོགས་པ་དེའི་ཚེ་མི་བགོའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་གོས་མི་བགོ་བའོ། །

[Block 1006]
ལྷན་ཅིག་ཉིད་ལ་ཞེས་བྱ་བ༌[^856]མི་བགོ་ན་ལྷན་ཅིག་དང་བྲལ་བའི་ཕྱིར་འདོམས་པ་ལ་བྱིན་པ་ནི་ཡང་དག་པ་ཉིད་ཀྱི་གྲངས་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། ལྷན་ཅིག་ཉིད་ལ་ཞེས་བྱ་བ་ནི་ཁོ་བོ་ཅག་ལ་འདི་སྦྱིན་པར་བྱའོ། །

[Block 1007]
འདོམས་པ་པོ་རྣམས་ཀྱིས་བྱ་བ་མ་བསྒོ༌[^857]ན་གང་ཞིག་དེར་གཞན་གཅིག་གམ་དུ་མ་གྲོགས་བྱེད་པ་འདོམས་པར་བྱེད་པ་པོ་དེ་སྤངས་ནས་འདོམས་པར་བྱེད་པ་ལ་བྱིན་པ་ནི་ཡང་དག་པ་ཉིད་ཀྱི་གྲངས་དེའོ།[^858] །འདིར་གཞུང་ནི། བཙུན་པ་རེ་ཞིག་སྐྱེ་བོ་བཞིས་གོས་གཏམས༌[^859]པར་གྱུར་པ་གཅིག་གིས༌[^860]ལེན་ན་སྩལ་བར་བགྱིའམ། ཉེ་བ༌[^861]འཁོར་སྦྱིན་པར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 1008]
བྱེ་བྲག་འདི་མ་སྨོས་ཏེ། ཤུགས་ཀྱིས་འདི་ལ་ལྟ་བ་མཐོང་བ་དེ་བས་ན་འདི་སྨོས་སོ། །

[Block 1009]
འདོམས་པར་བྱེད་པ་དང་བཅས་པ་ལ་མི་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་འདོམས་པར་བྱེད་པ་མ་ཡིན་པའི་གང་ཟག་དང་ལྷན་ཅིག་ལེན་དུ་འོངས་ན་བསྐུར་བར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏེ། དངོས་པོ་དེ་བདག་པོ་མ་ཡིན་པ་གཞན་ལ་ཡང་སྦྱིན་པར་འགྱུར་བ་དང་། བསྐུར་བར་འགྱུར་བ་དང་། བདག་པོ་ལ་ཞེས་བྱ་བ་ནི༌[^862]དེའི་རྒྱུ་རིག་པར་བྱའོ། །

[Block 1010]
སྨྱོན་པས་ཉེ་དུ་མ་ཡིན་པ་དང་དེའི་ཁྱིམ་ནས་བླངས་པ་ལ་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྨྱོན་པས་རང་གི་ཉེ་དུ་མ་ཡིན་པའི་ཁྱིམ་ནས་བླངས་པ་དང་། དེ་ལས་གཞན་པ་ཡང་རུང་སྟེ་དེས་གང་བླངས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1011]
འདིར་གཞུང་ནི་གང་ན་ཕའམ་མའམ་ཕུ་ནུའམ་སྲིང་མོ་མངོན་པར་རང་གི་ཁྱིམ་ནས་སྦྱིན་པར་བྱེད་པ་དེ་ལས་བླང་བར་བྱའོ། །

[Block 1012]
གང་ལས་བླང་བར་མི་བགྱི། གང་ན་ཕ་མ་ལ་སོགས་པ་མི་མངོན་པ་ནས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^863]འདིར་གསུངས་པ་ཡིན་ནོ། །

[Block 1013]
ཉེ་བ་དང་འབྲེལ་པ་དེ་ལ་ནི་སྦྱིན་པའམ་ཉེ་དུས་གང་གིས་བླངས་པའམ་ཞེས་བྱ་བ་ཡིད་ཆེས་པའི་གཙོ་བོ་ཕ་མ་ལ་སོགས་པར་གཏམས་པ་ཡིན་ནོ། །

[Block 1014]
གསལ་མི་གསལ་གྱིས་འདིར་བྱ་བ་ཉིད་དུ་རྣམ་པར་གཞག་པས་དེ་ལྟ་བས་ན་དེ་ལྟར་ཉེ་བར་བཏགས༌[^864]པའོ། །

[Block 1015]
དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

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
--- END BLOCKS ---
