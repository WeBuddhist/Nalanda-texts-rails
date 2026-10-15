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
དེས་གཙུག་ལག་ཁང་དུ་ཡོན་བདག་རྣམས་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་ཀྱང་མ་བསྟན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེས་ཡོན་བདག་ལ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་དེས་གཙུག་ལག་ཁང་དུ་ཡོན་བདག་རྣམས་འོངས་ཏེ་བརྙན་པ་དག་ལ་གཡར་བ༌[^615]སྦྱིན་པར་བྱ་བ་ཉིད་ཀྱང་མ་བསྟན་པ་མ་ཡིན་པ་དེ་ནི་སྔར་གཞུང་ལས།

[Block 1017]
ཡོན་བདག་གཙུག་ལག་ཁང་དུ་ལྷགས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་དེ༌[^616]ཉིད་འདིས་བསྡུས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 1018]
དགེ་སློང་ལ་ནི་སར་པ་ཕྱིས་བླང་བ་མེད་པ་ཉིད་དུའོ་ཞེས་བྱ་བ་ནི་སྣོད་སྤྱད་སར་པ་དགེ་སློང་ལ་ཐམས་ཅད་ཀྱི་ཐམས་ཅད༌[^617]དུ་སྦྱིན་པའོ། །

[Block 1019]
དེ་ཡང་དེ་ཡོད་པ་གཉིས་ལ་སྦྱིན་པ་འདི་ཆ་གཅིག་གིས་བརྟགས་པའོ། །

[Block 1020]
འདིར་གཞུང་ནི་དགེ་སློང་རྣམས་ལ་ནི་སར་པ་དག་སྦྱིན་པར་བྱའོ། །

[Block 1021]
ཁྱིམ་པ་རྣམས་ལ་ནི་རྙིང་པ་དག་བརྙན་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1022]
སྣོད་སྤྱད་ཀྱི་ཆེད་དུ་མཛོད་ཁང་བསྐོ་བར་བྱའོ། །

[Block 1023]
ས་དང་ཟངས་མའི་སྣོད་སྤྱད་དག་སོ་སོར་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་ཐ་དད་པ་ཉིད་དུ་གདོན་མི་ཟ་བར་བསྒྲུབ་པར་བྱའི་གནས་ཐ་དད་པར་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དགོངས་པའོ། །

[Block 1024]
འདིར་གཞུང་ནི་གནས་བརྟན་གཉིས་པ་སྦྱིན་པར་བྱ་སྟེ། གང་དུ་ཟངས་ལས་བྱས་པའི་སྣོད་སྤྱད་དག་གཞག་པ་ཞེས་བྱ་བ་འདི་གསུངས་སོ། །

[Block 1025]
དེ་ནི་འདིར་དེ་དང་རྩེ་གཅིག་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1026]
ཆུ་ཉེ་བར་གཞག་པར་བྱའོ། །

[Block 1027]
གར་བབ་བབ་ཏུ་མི་གཞག་གོ། །

[Block 1028]
དེའི་ཆེད་དུ་ཆུ་ཁང་བྱའོ། །

[Block 1029]
གཙུག་ལག་ཁང་གི་ལྷོ་ནུབ་ཀྱི་མཚམས་སུའོ་ཞེས་བྱ་བ་ལ་ལྷོ་ནུབ་ཀྱི་མཚམས་སུ་ཞེས་བྱ་བ་ནི་སྒོ་ནི་ཤར་ཕྱོགས་སུ་ངེས་པར་བྱ་སྟེ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1030]
སྒོ་ཕྱོགས་གཞན་དུ་ལྟ་བ༌[^618]ལ་ནི། ལྷོ་དང་ནུབ་ཀྱི་ཕྱོགས་མཚམས་ཁོ་ནར་ཆ་དང་འབྲེལ་པའི་མཚམས་ཀྱི་རྩ་བ་ལ་བྱེད་པ་ཁང་པའི་མཚམས་སྤང་ནང་དུ་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1031]
འདིར་ཕྱོགས་འདིའི་ནང་དུ་ཡིན་གྱི་གར་བབ་བབ་ཏུ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1032]
སྐར་ཁུང་གདོད་པ་དང་སོ་ཕག་གི་གཅལ་དགྲམ་པ་དང་། ཆུ་ཁུང༌[^619]གདོད་པ་དང་སྒོ་གདོད་པ་དང་སྒོ་གླེགས་དང་ཡང༌[^620]མིག་གཞུག་པར་བྱའོ། །

[Block 1033]
ཆུ་ཚགས་གཞག་པའི་ཕྱིར་གདང་བུ་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་སྦྱིན་པ་སྟེ་དེར་གདང་བུ་བཅིང༌[^621]བར་བྱའོ། །

[Block 1034]
གང་དུ་ཆུ་ཚགས་རུང་བ་དག་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1035]
ཤིང་གི་ཁྲིའུ་དག་ལ་གཞག་གོ་ཞེས་བྱ་བ་ནི་ཆུ་སྣོད་ལ་ཞེས་བྱ་བ་ལ་སྐབས་ཀྱིས་རྟོགས་པའོ། །

[Block 1036]
ཡང་ན་སོ་ཕག་གི་སྟེགས་བུའི་སྟེང་དུ་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་ཙམ་ཉིད་ཀྱིས༌[^622]མ་ཡིན་ཏེ་འོན་ཀྱང་གཞི་དག་ལའོ་ཞེས་བྱ་བས་ཏེ། མ་མོ་ལས་རྒྱུ་བར་བྱ་ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 1037]
ཆུ་སྣོད་ནི་ཁྲུས་ཆུའི་ཆེད་ཀྱི་བར་ཡན་ཆད་གཙང་སྦྲ་བྱ་བ་ནི་གཞན་གྱིས་སློབ་དཔོན་ལ་སོགས་པ་དང་འབྲེལ་པའི་ཡོངས་སུ་འཛིན་པའི་ཆོ་ག་འདི་རྟོགས་པའི་དོན་དུ་གཞན་གྱི༌[^623]དོན་གྱི་ཚིག་ཉེ་བར་བླང་བའོ། །

[Block 1038]
དེ་ནི་འདིར་དྲི་མ་མེད་པར་བྱ་བ་བསྒྲུབ་པ་བསྟན་པ་དེ་ནི་གཙང་བར་བྱ་བ་ཉིད་བསྟན་པའི་ཕྱིར་གཙང་བར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡོངས་སུ་ལོངས་སྤྱོད་པར་བྱེད་པ་ལ༌[^624]གཙང་བ་ཉིད་དུ་བྱེད་པ་དང་། སྦྱོར་ཤེས་པར་བྱ་བ་མ་ཡིན་ཏེ་ཤིན་ཏུ་ཡོད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1039]
དེའི་གནས་འཇོག་པ་ཡོངས་སུ་དག་པས་གཙང་བར༌[^625]བྱེད་པས་གཙང་བ་ཉིད་ལའོ། །

[Block 1040]
བཏུང་བར་བྱ་བའི་ཆུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བཏུང་བར་བྱ་བའི་ཆུ་ཡང་གཙང་སྦྲ་དང་གཙང་བར་བྱའོ། །

[Block 1041]
ཡོངས་སུ་ལོངས་སྤྱོད་པར་བྱ་བའི་ཆུ་ལ་དེ་དང་རྗེས་སུ་མཐུན་པའི་གཙང་སྦྲ་བསྒྲུབ་པ་འདི་ནི་རྗེས་སུ་འབྲངས་པས་ཤེས་པར་བྱའོ། །

[Block 1042]
དེ་ལག་པ་དང་གོས་རུང་བ་མ་ཡིན་པ་དག་གིས་བྲིམ་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི་བཏུང་བར་བྱ་བའི་ཆུའོ། །

[Block 1043]
ལག་པ་དང་གོས་རུང་བ་མ་ཡིན་པ་ཞེས་བྱ་བ་ནས༌[^626]ཀུན་ནས་རེག་པས་ཉེ་བར་འབགས་པར་གྱུར་པ་དག་གིས་སོ། །

[Block 1044]
ཆུ་སྣོད་རྣམས་ཀྱི་ནང་དུས་དུས་སུ་སྦྱང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། ནང༌[^627]ཞེས་བྱ་བ་ནི་ཁྱད་པར་ཡང་དག་པར་བསྟན་པའོ། །

[Block 1045]
ཕྱི་རོལ་དུ་ནི་གཙང་སྦྲ་ཞེས་བྱ་བ་འདི་ཉིད་ཀྱིས་བྱས་པའོ། །

[Block 1046]
ཟབ་མོ་རྣམས་ཀྱི་ནི་པུ་ཤེལ་ཙིའི་ཁྲུ་ད་ཤིང་ངམ་འདབ་མའི་ཆང་བུའམ་རས་མ་ཤིང་བུའི་རྩེ་མོ་ལ་བཏགས་པས་སོ་ཞེས་བྱ་བ་ལ་པུ་ཤེལ་ཙི་ཞེས་བྱ་བ་འདི་ལ་གང་དུ་རྣམ་པར་འབྱེད་པ་རྣམས་ཀྱི་ཁྲུ་ད་ཤིང་ཞེས་བྱ་བར་སྨོས་པ་དེ་བས་ན་འདིར་ཡོངས་སུ་གྱུར་པ་འདི་ལ་འབྲེལ་པ་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1047]
དེ་ལ་ཟས་ཀྱི་འབྲེལ་ཟེར་མི་བསྲུང་བ་ཉིད་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་པུ་ཤེལ་ཙིའི་ཤིང་ལ་སོགས་པའོ། །

[Block 1048]
གང་ཞིག་ཟང་ཟིང་ཅན་དུ་འགྱུར་བ་ནི་ཟང་ཟིང་དང་བཅས་པ་ཉིད་དུ་འགྱུར་བ་དེ་ལ་ནི་མི་བསྲུང་བ་ཉིད་དུ་མི་བྱའོ། །

[Block 1049]
མི་རུང་བ་ཉིད་ཡོད་པ་ལ་འདི་ནི་རུང་བར་བྱེད་པ་ཡིན་ཏེ། འདི་ནི་གཙང་བར་བྱའོ་ཞེས་བྱ་བ་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 1050]
བསྐམ་པར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཆུ་སྣོད་བཀྲུ་བཤལ་བྱས་པ་རྣམས་ལའོ། །

[Block 1051]
དེའི་ཚེ་འབྲེལ་པར༌[^628]མི་འགྱུར་བར་བྱ་བའི་ཕྱིར་ཅིག་ཅར་ཉིད་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བཀྲུ་བཤལ་བྱ་བ་དང་བསྐམ་པའི་དུས་དེ་ལ་བྲེལ་པར་མ་གྱུར་ཅིག་ཅེས་བྱ་བ་འདིའི་དོན་ཅིག་ཅར་ཉིད་དུ་འདི་བཀྲུ་བ་དང་བསྐམ་པར་མི་བྱའོ། །

[Block 1052]
སྣོད་རྣམས་ཀུན་ལ་དུས་གཅིག་ཏུ་མ་ཡིན་ནོ། །

[Block 1053]
ཆུ་དང་འབྲེལ་པའི་ལས་ནི་གནས་པས་བྱ་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདི་རྣམས་ལ་བརྩམ་པ་དང་གཞན་ལ་བརྗོད་པའོ། །

[Block 1054]
འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཆུ་བླང་བར་བྱའོ་ཞེས་གསུངས་པ་དང་། དགེ་སློང་གིས་སུས་བླང་བར་བྱ་མི་ཤེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གནས་པ་དག་གིས་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1055]
ཆུ་ཁང་གི་འཁོར་དུ་གཏོགས་པ་དང་ཆུ་ཚགས་ཀྱི་བྱ་བ་ཡང་འདི་རྣམས་ཉིད་ལ་རིགས་པ་ཡིན་གྱི་གཞན་དུ་ན་ཡང་ཞེས་བྱ་བ་འདི་བསྟན་པ་ཡིན་ནོ། །
--- END BLOCKS ---
