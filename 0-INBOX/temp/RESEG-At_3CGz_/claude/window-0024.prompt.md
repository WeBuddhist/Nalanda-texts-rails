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
[Block 841]
མངོན་པར་ཤེས་པ་ནི་འདི་ལྟར་ལྷའི་མིག་གི་མངོན་པར་ཤེས་པ་དང་། ལྷའི་རྣ་བའི་མངོན་པར་ཤེས་པ་དང་། གཞན་གྱི་སེམས་ཤེས་པའི་མངོན་པར་ཤེས་པ་དང་། སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་དང་། རྫུ་འཕྲུལ་གྱི་མངོན་པར་ཤེས་པ་དང་། ཟག་པ་ཟད་པའི་མངོན་པར་ཤེས་པའོ།[^471] །

[Block 842]
དེ་ལྟ་བུའི་མངོན་པར་ཤེས་པ་དེ་དག་ཞི་གནས་ལས་འབྱུང་བ་ཡིན་པས་ཞི་གནས་བསྒྲུབ་པར་བྱ་སྟེ།

[Block 843 [VERSE]]
ཞི་གནས་ཡན་ལག་རྣམས༌[^472]ཉམས་པས། །
རབ་ཏུ་འབད་དེ་བསྒོམ༌[^473]བྱས་ཤིང་། །
ལོ་ནི་སྟོང་ཕྲག་དག་གིས་ཀྱང་། །
ཏིང་འཛིན་འགྲུབ་པར་མི་འགྱུར་རོ། །

[Block 844]
ཞི་གནས་ཡན་ལག་ཅེས་པ་ནི་བླ་མས་མཛད་པའི་ཏིང་ངེ་འཛིན་ཚོགས་ཀྱི་ལེའུའི་སྤང་བར་བྱ་བ་ལ་སོགས་པ་དགུའོ། །

[Block 845]
གཞན་ནི་གོ་སླའོ།[^474] །

[Block 846]
དེ་བས་ན་ཡན་ལག་ཉམས་ན་ཞི་གནས་མི་འགྲུབ་པ་དེའི་ཕྱིར་བདག་གི་བླ་མ་རྗེ་བཙུན་དཔལ་བྱང་ཆུབ་བཟང༌[^475]པོས་ཏིང་ངེ་འཛིན་གྱི་ཚོགས་ཀྱི་ལེའུ་ལས་ཡན་ལག་དགུ་གསུངས་པ་ནི། འདི་ལྟར་སྤང་བར་བྱ་བ་དང་། སྔོན་དུ་འགྲོ་བ་དང་། ལྡོག་པར་བྱ་བ་དང་། གདུང་བ་གཅད་པ་དང་། ཡིད་འབྱུང་བར་བྱ་བ་དང་། ཡོན་ཏན་རྗེས་སུ་དྲན་པར་བྱ་བ་དང་། བརྩོན་པར་བྱ་བ་དང་། འབྲེལ་པར་བྱ་བ་དང་། གནས་པའི་ཐབས་ཞེས་བྱའོ། །

[Block 847]
དེ་ལྟ་བུའི་ཡན་ལག་རྣམས་ཤེས་པར་བྱས་ལ་དེ་ལ་ལེགས་པར་གནས་པར་བྱའོ་ཞེས་བླ་མ་གསུང་བ་ཡིན་ནོ། །

[Block 848]
དེ་རྣམས་ཀྱི་དོན་ནི་ཏིང་ངེ་འཛིན་གྱི་ཚོགས་ཀྱི་ལེའུ་དེ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 849]
འདིར་ཡན་ལག་ཐ་མའི་དོན་ཅུང་ཞིག་བྲི་བར་བྱའོ་སྟེ། བླ་མའི་ཞལ་ནས་ཏིང་ངེ་འཛིན་གྱི་ཚོགས་ཀྱི༌[^476]ལེའུ་ལས་འདི་སྐད་དུ། དེ་ལྟར་ཡན་ལག་བརྒྱད་དང་ལྡན་པ་དེས། གནས་རྗེས་སུ་མཐུན་པར་ཁ་ཟས་དང་སྤྱོད་ལམ་རྗེས་སུ་མཐུན་པ་དང་གོས་དང་གྲོགས་རྗེས་སུ་མཐུན་པ་དང་ལྡན་པར་བྱས་ལ། སེམས་མཉམ་པར་གཞག་པར་བྱའོ་ཞེས་པ་དང་། ཡང་གསུངས་པ་དེས་མཉམ་པར་མ་བཞག་པ་ན་ཡང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་བཀླག་པ་དང་། ཚ་ཚ་དང་། བསྐོར་བ༌[^477]ལ་སོགས་པ་བསོད་ནམས་ཀྱི་ཚོགས་ལ་འབད་པར་བྱའོ་ཞེས་པ་དང་། ཡང་གསུངས་པ་སེམས་མཉམ་པར་འཇོག་འདོད་པ་དེས་སྤོང་བའི་འདུ་བྱེད་བརྒྱད་བསྒོམ་པར་བྱ་སྟེ། དེའི་མི་མཐུན་པའི་ཆོས་ནི་འདི་དག་གོ། །

[Block 850 [VERSE]]
ཉེས་པ་ལྔ་ནི་ལེ་ལོ་དང་། །
གདམས་ངག་བརྗེད་དང་བྱིང་དང་རྒོད། །
འདུ་མི་བྱེད་དང་འདུ་བྱེད་དང་། །
འདི་དག་ཉེས་པ་ལྔར་འདོད་དོ། །

[Block 851]
དེ་དག་གི་གཉེན་པོ་སྤོང་བའི་འདུ་བྱེད་བརྒྱད་དག་ཀྱང་།

[Block 852 [VERSE]]
གནས་དང་དེ་ལ་གནས་པ་དང་། །
རྒྱུ་དང་འབྲས་བུ་ཉིད་དུའོ། །
དམིགས་པ་བརྗེད་པར་མ་གྱུར་དང་། །
བྱིང་དང་རྒོད་པ་རྟོགས་པ་དང་། །

[Block 853]
དེ་སྤོང་མངོན་པར་འདུ་བྱེད་དང་། །ཞི་ཚེ་རྣལ་དུ་འཇུག་པའོ། །ཞེས་གསུངས་སོ། །

[Block 854]
མདོ་སྡེ་རྒྱན་ལས་ཀྱང་།

[Block 855 [VERSE]]
གཅིག་ནི་འབད་པར་བྱེད་པ་སྟེ། །
གཉིས་པ་ཕན་འདོགས་བདག་ཉིད་ཡིན། །
གསུམ་པ་གཏོང༌[^478]བར་བྱེད་པ་སྟེ། །
བཞི་པ་གཉེན་པོ་ཉིད་ཡིན་ནོ། །

[Block 856]
ཞེས་གསུངས་སོ། །

[Block 857]
ཡང་བཤད་པ། འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་དང་། རྨུགས་པ་དང་། གཉིད་དང་། རྒོད་པ་དང་། འགྱོད་པ་དང་། ཐེ་ཚོམ་མོ། །

[Block 858]
དེ་ལ་རྨུགས་པ་དང་གཉིད་ཀྱི་འཁོར་ནི། རྨྱ་བ་དང་། མི་དགའ་བ་དང་། བྱ་རྨྱངས༌[^479]དང་། ཁ་ཟས་ཀྱི་ཚོད་མ་ཟིན་པ་དང་། སེམས་ཞུམ་པ་ལ་སོགས་པའོ། །

[Block 859]
ལས་ནི་སེམས་ཞུམ་པར་བྱེད་པའོ། །

[Block 860]
གཉེན་པོ་ནི་སྣང་བའི་འདུ་ཤེས་སོ། །

[Block 861]
རྒོད་པ་དང་། འགྱོད་པའི་འཁོར་ནི་ཉེ་དུའི་རྟོག་པ༌[^480]དང་། སྔོན་དགོད་པ་དང་། དགའ་བ་དང་། རྩེས་པ་དག་རྗེས་སུ་དྲན་པའོ། །

[Block 862]
ལས་ནི་སེམས་མ་ཞི་བར་བྱེད་པའོ། །

[Block 863 [VERSE]]
གཉེན་པོ་ནི་ཞི་གནས་སོ། །
དམིགས་པ་གང་རུང་ཅིག་དག་ལ། །
ཡིད་ནི་དགེ་ལ་གཞག་པར་བྱ། །

[Block 864]
དམིགས་པ་ནི་སེམས་ཀྱི་ཡུལ་ཡིན་ཏེ། ཇི་སྐད་དུ།

[Block 865 [VERSE]]
དབུ་མ་རྟོག་གེ་འབར་བ་ལས། །
ཡིད་ཀྱི་གླང་པོ་ལོག་གཡོ་བ། །
དམིགས་པའི་ཀ་བ་བརྟན་པོ་ལ། །
དྲན་པའི་ཐག་པས་ངེས་བཅིངས་ཏེ། །

[Block 866]
སེམས་ནི་ཞི་ལ་གཞག་པར་བྱ། །ཞེས་འབྱུང་ངོ་། །གང་རུང་ཅིག་དག་ལ་ཞེས་པ་ནི། མཚན་མ་དང་བཅས་པའི་ཞི་གནས་དང་། མཚན་མ་མེད་པའི་ཞི་གནས་སོ། །

[Block 867]
དེ་ཡང་བླ་མའི་ཞལ་སྔ་ནས་ཏིང་ངེ་འཛིན་གྱི་ཚོགས་ཀྱི་ལེའུ་ལས་འདི་སྐད་དུ་འདིར་ཞི་གནས་ནི་གཉིས་ཏེ། མཚན་མ་དང་བཅས་པ་དང་། མཚན་མ་མེད་པའོ། །

[Block 868]
མཚན་མ་དང་བཅས་པ་ལ་གཉིས་ཏེ། ཁ་ནང་དུ་བལྟས་པ་དང་། ཁ་ཕྱིར་བལྟས་པའོ། །

[Block 869]
ནང་དུ་བལྟས་པ་ལ་གཉིས་ཏེ། ལུས་ལ་དམིགས་པ་དང་། ལུས་ལ་བརྟེན་པ་ལ་དམིགས་པའོ། །

[Block 870]
ལུས་ལ་དམིགས་པ་ལ་གསུམ་སྟེ། ལུས་ཉིད་ལྷའི་རྣམ་པར་དམིགས་པ་དང་། ཀེང་རུས་ལ་སོགས་པ་ལ་མི་སྡུག་པའི་རྣམ་པར་དམིགས་པ་དང་། ཁ་ཊྭཱཾ་ག་ལ་སོགས་པ་མཚན་མ་ཁྱད་པར་ཅན་ལ་དམིགས་པའོ། །

[Block 871]
ལུས་ལ་བརྟེན་པ་ལ་ལྔ་སྟེ། དབུགས་ལ་དམིགས་པ་དང་། མཚན་མ་ཕྲ་མོ་ལ་དམིགས་པ་དང་། ཐིག་ལེ་ལ་དམིགས་པ་དང་། འོད་ཟེར་གྱི་ཡན་ལག༌[^481]ལ་དམིགས་པ་དང་། དགའ་བ་དང་བདེ་བ་ལ་དམིགས་པའོ། །

[Block 872]
ཁ་ཕྱིར་བལྟས་པ་ལ་གཉིས་ཏེ། ཁྱད་པར་ཅན་དང་། ཕལ་པའོ། །

[Block 873]
ཁྱད་པར་ཅན་ལ་གཉིས་ཏེ། སྐུ་ལ་དམིགས་པ་དང་། གསུང་ལ་དམིགས་པའོ། །

[Block 874]
འདི་དག་ནི་ཞི་གནས་ལ་འཇུག་པའི་ཡན་ལག་གོ་ཞེས་པ་དང་། མཚན་མ་མེད་པའི་ཞི་གནས་ནི།

[Block 875]
ཡང་དེ་ཉིད་ལས་མཚན་མ་མེད་པའི་ཞི་གནས་སོ་སོར་རྟོག་པའི་ཤེས་རབ་ཉིད་ལས།

[Block 876]
མཚན་མ་མེད་པའི་ལྷག་མཐོང་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་འབྱུང་ཞེས་ཏེ་ཞེས་པ་དང་། ཡང་དེ་ཉིད་ལས་མཚན་མ་དང་བཅས་པའི་ཞི་གནས་ལ་བརྟེན་པ་པས༌[^482]ནི་མཚན་མ་མེད་པའི་ཞི་གནས་ལ་དམིགས་ནས་ལྷག་མཐོང་སྐྱེད་པའི༌[^483]ཕྱོགས་འདི་བསྔགས་ཏེ། དེ་ལ་གནས་པ་བརྟན་པ་དང་། ཞི་གནས་འབའ་ཞིག་གིས༌[^484]ཉོན་མོངས་པ་སེལ་བ་དང་། རབ་ཏུ་གནོན་པར་འགྱུར་བས་དེ་ནི་འབྲས་བུ་དང་རྗེས་སུ་མཐུན་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་གསུངས་སོ། །

[Block 877]
ཡང་དེ་ཉིད་ལས་ཇི་ལྟར་བསྒོམ་པ་ནི་འདིར་མི༌[^485]བརྗོད་དེ་གཞུང་མངས་པའི་འཇིགས་པ་དང་། བླ་མ་དམ་པས་ཉམས་སུ་མྱོང་བའི་མན་ངག་ལ་བརྟེན་པར༌[^486]རིགས་ཀྱི། བསྒོམ་པའི༌[^487]མན་ངག་ནི་ཡི་གེར་གནས་པས་ཤེས་པར་དཀའ་བའི་ཕྱིར་དང་། ཞིབ་ཏུ་ནི་ཞི་གནས་དང་ལྷག་མཐོང་བསྟན་པ་ལས་བཤད་པའི་ཕྱིར་རོ་ཞེས་གསུངས་སོ། །

[Block 878]
དེ་ལྟ་བུའི་རྣལ་འབྱོར་པས་ཞི་གནས་གྲུབ་པར་གྱུར་ནས། སྔར་བཤད་པའི་མངོན་པར་ཤེས་པ་ལྔ་པོ་དག་འགྲུབ་པར་འགྱུར་བ་ལ་ཐེ་ཚོམ་མེད་དོ་ཞེས་བླ་མ་གསུང་ངོ་། །གཞན་ཡང་མངོན་པར་ཤེས་པ་བསྐྱེད་པའི་ཐབས་སུ་གྱུར་བ་འཕགས་པ་སྤྱན་རས་གཟིགས་ཀྱིས་ཞུས་པའི་ཆོས་བདུན་པའི་མདོ་ལས་འབྱུང་བའི་བསླབ་པའི་གཞི་དེ་དག་ཀྱང་ཉམས་སུ་བླང་བར་བྱ་བ་དང་། མདོ་དེ་ཉིད་ཀྱང་དུས་དུས་སུ་ཁ་ཏོན་དུ་གདོན་པར་ཡང་བྱའོ། །

[Block 879]
འཕགས་པ་ཐོགས་མེད་ཀྱིས་ཀྱང་བྱང་ཆུབ་སེམས་དཔའ་མངོན་པར་ཤེས་པ་མྱུར་དུ་ཐོབ་པར་འདོད་པས་ཉིན་ལན་གསུམ་མཚན་ལན་གསུམ་དུ་ཕྱག་འཚལ་བ་དང་། མཆོད་པ་དང་སྡིག་པ་བཤགས་པ་དང་། རྗེས་སུ་ཡི་རང་བ་དང་། བསྐུལ་བ་དང་། གསོལ་བ་གདབ་པ་དང་། ཡོངས་སུ་བསྔོ་བ་ལ་བརྩོན་པར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 880]
གཞན་ཡང་འདོད་པ་ཆུང་བ་དང་ཆོག་ཤེས་པ་དང་། གསོ་སླ་བ་དང་རབ་ཏུ་དབེན་པ་ལ་སོགས་པ་ཞི་གནས་ཀྱི་ཚོགས་ཐམས་ཅད་དང་ལྡན་པའོ། །
--- END BLOCKS ---
