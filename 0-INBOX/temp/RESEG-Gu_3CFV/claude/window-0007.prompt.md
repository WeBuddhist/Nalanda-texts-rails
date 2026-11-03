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
[Block 246]
ལོ་ཉི་ཤུ་ལས་མི་ཉུང་བ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ཚིག་འདིས༌[^179]ནི་རྒྱལ་ཚབ༌[^180]ལྟ་བུ་ཞེས་བྱ་བ་མངའ༌[^181]བདག་ཉིད་དང་བདག་པོ་དང་ལྡན་པ་ཉིད་དེའི་དོན་ཏོ། །

[Block 247]
གནས་བརྟན་ཉིད་ཀྱི་བདག་པོ་ཉིད་གང་ཡིན་པ་དེ་ནི་འདིར་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་གནས་བརྟན་གྱི་རྣམ་གྲངས་ཉིད་ཀྱིས་བརྗོད་པར་རྟོགས་པའོ། །

[Block 248]
གྲོང་ཁྱེར་བའི་སྐད་སྨྲ་བ་ཞེས་བྱ་བ་ནི་སྒྲ་མཁས་པ་སྟེ་རིགས་པ་དང་གྲོལ་བར་སྨྲ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 249]
རང་བཞིན་ཉིད་ཀྱིས༌[^182]གཞན་གང་ཞིག་སྤང་བ་རྣམས་ལ་བདག་གིས་བརྩམས་པ་གང་ཞིག་སྤོང་བ་རྣམས་ལ་ཁྱོད་ཀྱི་ལས་ཏེ། འདི་སྐད་ཅེས་གང་ཞིག་སྤང་བར་བྱ་བ་ཉིད་བདག་གིས་སྨྲས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་ཀྱིས་མི་ནུས་པ་ལ་མཐོ་བཙམས༌[^183]པ་ཞེས་བྱ་བ་དེ་ལ་བརྟེན་པའོ། །

[Block 250]
དགེ་སློང་མ་ལ་ལུས་ཉེ་བར་གཞོལ་བ་ཉིད་ཀྱི་ཕྱིར་བཅོས་པ་བྱས་པ་ཞེས་བྱ་བ་ལ། [^184]འདིར་གཞི་ནི་འདིས༌[^185]དགེ་སློང་མ་ལུས་ཉེ་བར་འདྲེས་པས་སྐྱོན་ཅན་དུ་འགྱུར་བ་ནི་མ་ཡིན་ནོ། །

[Block 251]
འདིས་དགེ་སློང་མའི་ལུས་ལ་ལུས་ཉེ་བར་གཞོལ་བར་ནི་མི་འགྱུར་བའམ། འདིས་དེ་སྐྱོན་ཅན་དུ་བྱས་པ་ལ་ལྟུང་བ་ཕྱིར་བཅོས་པ་བྱས་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 252]
ཡོན་ཏན་དེ་ལྟ་བུ་དང་ལྡན་པ་དེ་ལ་བསྒྲུབ་པའོ། །གང་གི་ཚེ་ན་མཐུན་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གསོ་སྦྱོང་བཅོ་ལྔ་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ནི་མཐུན་པའི་གསོ་སྦྱོང་ལ་སོགས་པ་བསལ་བའི་ཕྱིར་རོ། །

[Block 253]
འདིས་གསོ་སྦྱོང་བཅུ་བཞི་པ་ནི་མ་བསལ་བ་སྟེ། བཅོ་ལྔ་པ་ཉིད་གཞན་ཞེས་བྱ་བའི་ཚེས་བཅོ་ལྔའི་ཡིན་པའི་ཕྱིར་རོ། །

[Block 254]
ཕྱོགས་གང་དུ་བསྐོ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་མཚམས་ཀྱི་ནང་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་མདོ་སྡེ་ལ་སོགས་པ་འཛིན་པ་མེད་ན་ཇི་ལྟ་བུ་ལས་བསྐོ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་མདོ་སྡེ་ལ་སོགས་པ་འཛིན་པ་མེད་ན༌[^186]སོ་སོར་ཐར་པ་ཐོན་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མའི་སྟོན་པར་བསྐོ་བར་བྱའོ། །

[Block 255]
དེ་ཡང་མེད༌[^187]ན་ཕམ་པར་འགྱུར་བའམ་ལྕི་བའི་ཆོས་རྣམས་སྟོན་པར་ནུས་པའོ་ཞེས་བྱ་བ་ནི། སོ་སོར་ཐར་པ་ཐོན་པ་དེ་ཡང་མེད་ན་དགེ་སློང་མའི་ཕམ་པར་འགྱུར་བ་བརྒྱད་དམ་ལྕི་བའི་ཆོས་རྣམས་སྟོན་ནུས་པའི་ངང་ཚུལ་ཅན་དེ་བསྐོ་བར་བྱའོ། །

[Block 256]
ཕྱི་མ་ནི་སྲིང་མོ་དག་ཅི་ཁྱེད་ཅག་དགེ་སློང་མའི་དགེ་འདུན་ཚོགས་སམ་ཡོངས་སུ་དག་གམ། མཐུན་ནམ་ཁ་ན་མ་ཐོ་བ་མེད་དམ། ཁྱེད་ཅག་ལ་དགེ་འདུན་གྱིས་མ་བསྐོས་པའི་གང་ཟག་འགའ་ཞིག་སྟོན་པར་མི་བྱེད་དམ། ཁྱེད་ཅག་ལ་སྟོན་པའི་གང་ཟག་འགའ་ཞིག་དགེ་འདུན་ལས་འོང་ངོ་། །ཁྱེད་ཅག་ལ་དགེ་སློང་འགའ་ཡང་སྟོན་པར་མི་སྤྲོའོ། །

[Block 257]
ཁྱེད་ཅག་གིས༌[^188]གདམས་ངག་དང༌[^189]རྗེས་སུ་སྟོན་པ་ནི་དགེ་འདུན་ལས་སོ། །

[Block 258]
སྲིང་མོ་དག་གིས་བག་ཡོད་པར་སྒྲུབས༌[^190]ཤིག་ཅེས་བྱ་བ་དེ་སྟོན་ནུས་པའོ་ཞེས་བྱ་བ་ནི་འདི་ལ་ཡང་དག་པར་བསལ་བར༌[^191]བྱེད་པ་དགེ་སློང་མའི་སྟོན་པ་ཕྱི་མ་ནི་དེ་ལྟ་བུ་ལས་བསྐོ་བར་བྱའོ་ཞེས་སྦྱར་བར་བྱའོ། །

[Block 259]
ཆོས་བླ་མའི་མཐུ་དང་ལྡན་པ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ནི་མ་བསྐོས་ཀྱང་འདི་དང་རྗེས་སུ་མཐུན་པའི་གདམས་ངག་སྟོན་པ་ལ་ཉེས་པ་མེད་ཅེས་བྱ་བའོ། །

[Block 260]
བསྐོས་པ་དེ་དག་ལས་གཅིག་དང་ཡང་མི་ལྡན་པ་དང་མ་བསྐོས་པ་དགེ་སློང་མ་ལ་སྟོན་ནའོ་ཞེས་བྱ་བ་ལ། གཅིག་དང་ཡང་མི་ལྡན་པ་ཞེས་བྱ་བའི་ཆོ་ག་འདའ་བར་བྱེད་པ་ལས་མ་གྲགས་པ་མེད་དོ་ཞེས་བྱ་བ་བསྐོས་པ་ཉིད་ཁོ་ན་ལ་འདིའི་ལས་བྱས་པ་ཉིད་དུ་སེམས་པར༌[^192]དེའི་ཕྱིར་ཚིག་འདི་སྨོས་སོ། །

[Block 261]
དེ་བས་ན་ཇི་ལྟར་ཉེ་བར་བརྗོད་པའི་ཡན་ལག་གཅིག་མེད་ཀྱང་བསྐོས་པ་དང་མ་བསྐོས་པ་ཡོད་ཀྱང་ཡན་ལག་འདི་རྣམས་ལ་ཡང་མ་བསྐོས་པར་གདམས་ངག་སྟོན་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 262]
སྔར་བསྐོས་པ་ནི་མ་བསྐོས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ལ་གསོ་སྦྱོང་གི་ཚིག་མེད་པ་དེ་ཉིད་ལ་འདིར་བསྐོས་པ་དེའང་མ་བསྐོས་པར་ཤེས་པར་མི་བྱའོ། །

[Block 263]
འདི་ལྟར་བསྐོས་པ་ཉིད་ཡིན་པས་ལན་ཅིག་བསྐོས་པས་ཇི་སྲིད་འཚོའི་བར་དུ་ཉེས་པ་མེད་ཅེས་བྱ་བ་དེ་ལ་འདི་བསྟན་པར་བྱའོ། །

[Block 264]
འདིར་གཞུང་ནི་བཙུན་པ་རེ་ཞིག་ལན་ཅིག་དགེ་སློང་མའི་སྟོན་པར་བསྐོས་པ་གང་ལགས་པ་དེ༌[^193]ཅི་དུས་གཞན་གྱི་ཚེ་ཡང་བསྐོ་བར་བགྱིའམ་འོན་ཏེ་མ་བསྐོས་པར་ཡང་བསྟན་པར་བགྱི། ཉེ་བ་འཁོར་དེར་བསྐོས་པ་དེ་ཉིད་ཀྱིས་བསྐོས་པ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 265]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་ཀྱང་ལན་ཅིག་བསྐོས་པ་ཇི་སྲིད་འཚོའི་བར་དུ་བསྟན་པར་བྱའི་ཡང་བསྐོ་བར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 266]
ཆོས་བཤད་པར་གསོལ་བ་ལ་ཡང་རྣམ་པ་འདི་ཉིད་ཡིན་པར་གསུངས་པ་ཡིན་ནོ། །

[Block 267]
འདིར་གཞུང་ནི་དགེ་སློང་མས་མ་གསོལ་བར་ཆོས་སྨྲ་བ་ལ་ལྟུང་བར་ཡང་མི་འགྱུར་བ་འགའ་མཆིས་སམ་ཡོད་དེ་སྔར་གསོལ་ཟིན་པའོ་ཞེས་བྱ་བ་ནི། དུས་སུ་མར་ལམ་ལ་བསྐུལ་བར་བྱས་པ་དེའི་ཕྱིར་འདི་གསུངས་པར་རྣམ་པར་གནས་པ་ཡིན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 268]
དགེ་འདུན་དུ་མ་ལངས༌[^194]ཤིང་འོས་པ་ལ་གསོལ་ན་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི། གནས་གང་ན་ཐམས་ཅད་དུ་དགེ་འདུན་དུ་མ་ལངས་པ༌[^195]དེ་ནི་འོས་པ་ཕམ་པར་མ་བྱུང་བ་ལ་སོགས་པ་ཕྱི་མའི་མཐར་མ་བསྐོས་པར་དེ་ལ་དགེ་སློང་མ་རྣམས་ཀྱིས༌[^196]གསོལ་བ་ཉིད་ན༌[^197]དགེ་སློང་མ་རྣམས་ལ་སྟོན་པ་ན་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 269]
དེ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གང་ལ་དགེ་སློང་མ་རྣམས་ཀྱིས་གསོལ་བ་འདེབས་པར་བྱེད་པ་དེ་དག་སྟོན་པ་ལ་ཡང་ལྟུང་བ་མེད་དོ། །

[Block 270]
གསོལ་བ་འདེབས་པ་དེ་དག་འོས་སུ་རུང་བ་མ་ཡིན་ན་མི་བྱའོ་ཞེས་བྱ་བ་འདིའི་རྗེས་སུ་འབྲངས་ནས་བྱ་བར་ཤེས་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 271]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་གང་ན་དགེ་སློང་གཅིག་གམ་གང་ན་གཉིས་སམ་གང་ན་གསུམ་གནས་པ་ལ་གལ་ཏེ་སྟོན་པའི་འོས་ཡིན་ན་ཉེ་བར་སོང་ལ་གསོལ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། སྟོན་པའི་འོས་སུ་རུང་བ་ཡིན་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 272]
མ་བསྐོས་པར་སྟོན་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 273]
ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 274]
དེའི་ཕྱིར་ཉི་མ་ནུབ་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 275]
ཅི་ཞིག་རྗེས་སུ་བསྒྲུབ་ན་འདིའི་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མཚན་ཐོག་ཐག་ཏུ་ཆོས་སྟོན་པ་མ་གཏོགས་པར་དགེ་སློང་མ་ལ་སྟོན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཚན་ཐོག་ཐག་ཏུ་ཉན་པ་ལས་གཞན་དུ་དགེ་སློང་མ་ལ་སྟོན་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅི་གནས་ཐམས་ཅད་དུའམ་ཞེ་ན། དེའི་ཚེ༌[^198]གལ་ཏེ་སྒོ་ཕྱེ་ཞིང་དེ་ལྟ་བུའི་གཙུག་ལག་ཁང་གི་མདུན་ན་དབྱར་ཁང་འདུག་པ་ནི་མ་ཡིན་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཚེ་ཞེས་བྱ་བ་ནི་སྟོན་པའི་དུས་ཀྱི་ཚེའོ། །

[Block 276]
དེ་ལྟ་བུའི་ཞེས་བྱ་བ་ནི་སྟོན་པའི་དུས་ལའོ། །

[Block 277]
སྒོ་ཕྱེ་ཞིང་ཞེས་བྱ་བ་ནི་རང་གི་གནས་ཐོབ་པ་ལས་འདིར་ཕོངས་པ་མེད་པ་ཞེས་བྱ་བ་ནི་ཉེས་པ་མེད་པའོ། །

[Block 278]
དེ་བས་ན་འདི་མཚོན་པ་ཙམ་ཡིན་ཏེ། གཞན་དུ་ན་ཡང་གང་དུ་དགེ་སློང་མ་རྣམས་ལ་ཕོངས་པ༌[^199]མེད་པ་དེ་ལ་ཡང་ལྟུང་བ་མེད་དོ། །

[Block 279]
དེ་ལྟར་ཡང་འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་དགེ་སློང་འགའ་ཞིག་ཡོད་དེ་གདུགས་བས་པའི་དུས་ཀྱི་ཚེའི་བར་དུ་དགེ་སློང་མ་ལ་སྟོན་པར་བགྱིད་ན་ལྟུང་བར་ཡང་མི་འགྱུར་བ་འགའ་མཆིས་སམ། བཀའ་སྩལ་པ་ཡོད་དེ་དབྱར་ཁང༌[^200]དུ་སྟོན་ན་ཇི་སྲིད་དུ་དགེ་སློང་མ་རྣམས་ཀྱི་གྲོང་འདབ་ཀྱི་གཙུག་ལག་ཁང་ངམ་ཁང་ཁྱིམ་དག་ཏུ་སྟོན་ན་ལྟུང་བ་མེད་དོ། །

[Block 280]
གྲོང་གི་ཕྱི་རོལ་དུ་སྟོན་པ་ནི་མ་གཏོགས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 281]
ཉི་མ་ནུབ་ནུབ་ཀྱི་བར་དུ་སྟོན་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 282]
དགེ་སློང་མས་ཆོས་འདྲི་བ༌[^201]ལ་མི་འཇིགས་པར་བྱ་བའི་ཕྱིར་དགེ་སློང་ལ་ཟས་དབུལ་བར༌[^202]བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མས་ཆོས་དྲི་བ་ལ་མི་འཇིགས་པར་བྱ་བའི་ཕྱིར་དགེ་སློང་ལ་ཟང་ཟིང་དབུལ་བར་བྱའོ། །

[Block 283]
རྒྱ་ཅང་དང༌[^203]ཤུར་བུ་དང་ལྕག་པོད༌[^204]དང་ཤུར་བུ་ཕྲེའུ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དབུལ་བར་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 284]
དགེ་སློང་གིས་དེ་དག་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་དག་ཅེས་བྱ་བ་ལ་སོགས་པ་གོས་འཛིན་པ་དགག་པ་དང་འབྲེལ་པའི་དོན་ལ་དམིགས་ཀྱིས་བསལ་བ༌[^205]ལྡེ་མིག༌[^206]ཀྱོག་པོ་ལ་སོགས་པ་བཟུང་ངོ་། །ཅི་ཞིག་རྗེས་སུ་བསྒྲུབ་ན་ཟས་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་སྟོན་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་དེ་ལྟར་གྱུར་པ་མ་ཡིན་པ་ལ་ཟས་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་དགེ་སློང་མ་ལ་སྟོན་ཏོ་ཞེས་སྨྲས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལྟ་བུར་གྱུར་པ་མ་ཡིན་པ་ལ་ཞེས་བྱ་བ་ནི་ཟས་ཅུང་ཟད་ཙམ་གྱི་ཕྱིར་སྟོན་པར་བྱེད་པ་པོ་མ་ཡིན་པ་ལའོ། །

[Block 285]
འདིར་བདེན་པ་ཉིད་དུ་རྣམ་པར་གཞག་པར་རིགས་པ་ཡིན་ཏེ། འདུ་ཤེས་ཙམ་ལས་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
