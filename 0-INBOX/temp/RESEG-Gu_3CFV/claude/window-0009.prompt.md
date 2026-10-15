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
[Block 316]
ཅི་ཞིག་གྲུར༌[^223]འཇུག་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་འགྲམ་གཉིས་འཇིགས་པ་དང་བཅས་པ་ཉིད་མ་གཏོགས་པར་འཐམས་ནས་ཅིག་ཅར་གྲུ་གཅིག་གི་ལམ་ལས་འདས་ཤིང་འགྲོ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐད་ཀར་ཕ་རོལ་དུ་འགྲོ་བ་མ་གཏོགས་སོ། །

[Block 317]
ལམ་ལས་འདས་ཤིང་རྒྱང་གྲགས་རེ་རེ་དང་རྒྱང་གྲགས་ཕྱེད་དུ་ཉེས་བྱས་སུ༌[^224]ཞེས་བྱ་བར༌[^225]སྦྱར་རོ། །

[Block 318]
དགེ་སློང་མ་གཅིག་གིས་ཀྱང་ཞེས་བྱ་བ་ལ་སོགས་པ་འདི་ལ་དོན་གྱིས་གསུམ་པར༌[^226]འགྱུར་བ་དང་ལྷན་ཅིག་ཏུ་འདི་དོན་གྱིས་ཐོབ་པའོ། །

[Block 319]
འགྲམ་གཉིས༌[^227]འཇིགས་པ་དང་བཅས་པ་ཉིད་ལས་གང་ཞིག་འདའ་ཞིང་འགྲོ་ནའོ། །

[Block 320]
འཐམས་ནས་དེ་མ་གཏོགས་པར་དགེ་སློང་མ་དང་ལྷན་ཅིག་ཏུ་དེའི་ཕྱིར་ཞུགས་པ་ན་ཡོ་བ་དང་གཏིབ་ཆད་པ་དང་རྦ་ཀློང་དང་ལས་བཟུར་བ་དང་རུ་སྐྱ་དང་གདོས་པ་ཆག་པ་དང་རུ་སྐྱ་འཛིན་པའི་དབང་གིས་འཇུག་པ་གཞན་དུ༌[^228]སོང་བ་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡོ་བ་ལ་སོགས་པ་ལས་བཟུང་བའི་དབང་གིས་རུ་སྐྱ་དང་གདོས་པའི་དབང་ངམ། རུ་སྐྱ་འཛིན་པའི་དབང་གིས་ཐད་ཀར་ཕ་རོལ་དུ་འགྲོ་བའི་དོན་དུ་ཞུགས་པ་ཡོད་པ་ལས་འཇུག་པ་གཞན་དུ་སོང་བ་ལ་ཉེས་པ་མེད་དོ། །

[Block 321]
དགེ་སློང་མ་དང་ལྷན་ཅིག་གྲུར་འཇུག་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 322]
གཅིག་པུ་འདུག་པའི་ལྟུང་བྱེད་ལ་ཡན་ལག་གང་དག་བྱེད་པ་པོ་དག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བུད་མེད་གཅིག་པུ་ཉིད་དང་སྐྱེ་བོའི་རྒྱུན་ལུགས་མེད་པ་ཉིད་ཀྱིས་ཕྱོགས་དབེན་པ་ཉིད་དང་སྐྱབས་དང་བཅས་པ་ཉིད་དང་བར་འདམ་གང༌[^229]ཉིད་ནི་བྱེད་པ་པོ་དག་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུད་མེད་གཅིག་པུ༌[^230]ཉིད་ནི་བུད་མེད་གཅིག་པུ་ཉིད་དོ། །

[Block 323]
འདིར་དབེན་པ་ན་འདུག་སྟེ་བྱེད་པ་པོ་ནི་བུད་མེད་ཉིད་དོ་ཞེས་བྱ་བ་ཁྱད་པར་ཉིད་ཀྱིས་དེ་འདིར་བརྟེན་པ་སྟེ་བུད་མེད་ཉིད་ནི་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 324]
ཐ་དད་པ་ཉིད་ཀྱིས་ཇི་ལྟར་དབེན་པ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྐྱེ་བོའི་རྒྱུན་ལུགས་མེད་པ་ཉིད་ཀྱིས་ཞེས་བྱ་བ་སྨོས་ཏེ། སྐྱེ་བོ་མང་པོའི་རྒྱུན་ལུགས་བྱེད་པ༌[^231]ཉིད་འདི་ལ་ཡོད་པ་ན་ཞེས་བྱ་བའི་བསྡུ་བའོ། །

[Block 325]
སྐྱབས་དང་བཅས་པ་ཉིད་ཅེས་བྱ་བ་ནི། རྩིག་པས་བསྒྲིབས་པའམ་སབ་མོས་བསྒྲིབས་པ་འམ་ཡོལ་བས་བསྒྲིབས་པ་ཞེས་བྱ་བ་འདིར་གསུངས་སོ། །

[Block 326]
དེ་ཡང་མཚོན་པ་ཙམ་གྱིས་དེ་མཐོང་བའི་ཡུལ་བཅད་པས་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 327]
དེ་ལྟར་ཡང་དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས་མུན་ནག་མཐུག་པོ་དག་ཀྱང་བསྡུའོ་ཞེས་བྱ་བ་སྐྱབས་ཙམ་ལ་ཡང་དག་པར་བརྟེན་པ་དང་བར་འདོམ་གང་ཉིད་ཅེས་བྱ་བའོ། །

[Block 328]
བུད་མེད་དང་ལྷན་ཅིག་ཏུ་གནས་པ་འདིའི་གང་དུ་འདི་རྣམས་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 329]
དེའི་ངོ་བོ་ཇི་ལྟ་བུ་ཞེ་ན་དེའི་ཕྱིར་དེ་ནི་རྐུབ་ཚོས་ཙམ་བཞག་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཞེས་བྱ་བ་ནི་འདུག་པའོ། །

[Block 330]
གཅིག་པུ་འདུག་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 331]
དེ་མ་ཐག་པར་བསྟན་པ་འདི་ཐམས་ཅད་ཁས་བླངས་ནས་བྱེ་བྲག་འགའ་ཞིག་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དགེ་སློང་མ་དང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུད་མེད་ཀྱི་གནས་སུ་འདིའོ། །

[Block 332]
འདི་བྱེ་བྲག་བསྟན་པ་ཡིན་ཏེ། འདིར་དགེ་སློང་མ་གཅིག་པུ་ཉིད་བྱེད་པ་པོ་ཡིན་གྱི། བུད་མེད་ཙམ་པོ་གཅིག་པུ་ཉིད་ནི་མ་ཡིན་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 333]
སླར་འདིར་ཅིའི་ཕྱིར་བུད་མེད་ཙམ་བརྟེན་པ་ཡིན་ཏེ། བསོད་ནམས་ཀྱི་དོན་དུ་འགྲེང་བ་ལ་སོགས་པ་ལ་འདི་དག་ལ་སྦྱར་བའི་ཕྱིར་ཁྱིམ་པ་མོ་དང་ལྷན་ཅིག་ཏུ་གནས་པ་འདི་ལ་བཟུར་བ་ཞེས་བྱ་བ་མཐོང་བ་ཡིན་ནོ། །

[Block 334]
གང་ལ་དེ་དག་བྱེད་པ་པོ་དག་ཅེས་བྱ་བ་འདིར་འདུག་པའི་གནས་ལས་ཐོབ་པ་འཇུག་པ་བརྗོད་པར་བྱ་སྟེ། འགྲེང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 335]
གཅིག་པུ་འགྲེང་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 336]
ཤེས་གཙོ་བོའོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 337]
གཙོ་ཆེར་ཤེས་ཤིང་ཞེས་བྱ་བ་འདི་ནི་དེའི་རྣམ་པར་འབྱེད་པ་ལས་ཀྱང་གལ་ཏེ་དགེ་སློང་གིས༌[^232]དེ་ཤེས་ལ་ཟོས་ཏེ། གལ་ཏེ་དགེ་སློང་མ་སྦྱོར་དུ་བཅུག་པ་ལ་དགེ་སློང་མས་སྦྱོར་དུ་བཅུག་པར་ཤེས་ན་ཞེས་བྱ་བ་འདི་ལྟར་གཞུང་ཡོད་པ་ཡིན་ཏེ། གཞན་དུ་ཤེས་པའི་བསླབ་པའི་གཞི་ལ་རྗེས་སུ་འབྲངས་ནས་འདིར་རྣམ་པར་ཤེས་པ་ཡིན་ནོ། །གང་དུ་འདུ་ཤེས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མས་སྦྱོར་དུ་བཅུག་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་སྦྱོར་དུ་བཅུག་པ་ནི་བསྐོས་པ་སྟེ། བསྐོས་པ་ནི་རྣམ་པར་རིག་བྱེད་དོ། །

[Block 338]
དེ་ཡང་ཚིག་གིས་ཏེ་སྤྲིང་ཡིག་ལ་སོགས་པ་རྣམས་ཀྱིས༌[^233]མ་ཡིན་པས་སོ། །

[Block 339]
སྦྱོར་དུ་བཅུག་པ་ཟ་བ་ལ་ཞུ་བ་ལས་ཉེས་བྱས་སུ་གསུངས་པའི་ཕྱིར་སྤྲིང་ཡིག་ལ་སོགས་པ་རྣམས་དང་ལག་རྩིས་དང་མངགས་པ་དག་བརྒྱུད་པ་དང་གཞན་ལ་ཟུར་གྱིས༌[^234]བསོད་སྙོམས་སྦྱོར་དུ་བཅུག་པ་ཟོས་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །ཇི་ལྟར་སྦྱོར་དུ་བཅུག་པ་ཉིད་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཡང་དག་པ་མ་ཡིན་པའི་ཡོན་ཏན་རྣམས་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་རྒྱུན་དུ་ཞུགས་པ་དང་ལན་ཅིག་ཕྱིར་འོང་བ་དང་ཕྱིར་མི་འོང་བ་དང་དགྲ་བཅོམ་པ་དག་ཡིན་པ་བདེན་ན་ལྟུང་བ་མེད་དོ། །

[Block 340]
མདོ་སྡེ་འཛིན་པ་དང་འདུལ་བ་འཛིན་པ་དང་མ་མོ་འཛིན་པ་དག་ཡིན་པ་བདེན་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །གང་ལ་སྦྱོར་དུ་བཅུག་པ་ཉིད་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མགྲོན་དུ་མ་བོས་པ་ལའོ། །

[Block 341]
བོས་པ་ལ་ཡང་ལྷག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མགྲོན་དུ་བོས་པ་ལ་ཡང་ལྷག་པར་སྦྱོར་དུ་བཅུག་པ་ཉིད་ལ་དེར་ལྟུང་བ་ཇི་ལྟར་འགྱུར་ཞེ་ན། ཇི་ལྟར་ཡང་འདིར་གཞུང་ནི་དགེ་སློང་རབ་ཏུ་མང་པོ་དག་ཁྱིམ་གཞན་དུ་མགྲོན་དུ་བོས་པས༌[^235]གྱུར་པ་ན། དེར་དགེ་སློང་མ་འོངས་ཏེ་དྲིས་པ་ཁྱེད་ཅག་གིས་དགེ་སློང་གང་དག་མགྲོན་དུ་བོས་མིང་ཆེ་གེ་མོ་དང་ཆེ་གེ་མོ་དག་གོ། །

[Block 342]
ཟན་ཇི་ལྟ་བུ་སྦྱིན་སུམ་འཕེལ་གྱི༌[^236]ཟན་དག་གོ། །

[Block 343]
མི་རུང་སྟེ་གང་གི་ཕྱིར་དགེ་སློང་དེ་དག་ནི་རྒྱུན་དུ་ཞུགས་པ་ཡིན་པས་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིར་གང་ཞིག་ལྟུང་བ་རྒྱས་པར་བཤད་པ་ལ་སོགས་པ་མཛད་པ་སྟེ་དེ་བས་ན་འདི་གསུངས་པ་ཡིན་ནོ། །

[Block 344]
མགྲོན༌[^237]དུ་བོས་སུ་ཟིན་ཀྱང་གང་ཞིག་སྦྱིན་བདག་གིས་མ་བསམས་པ་སྦྱིན་དུ་བཅུག་པ་གང་ཡིན་པ་དེ་ཡང་བཟའ་བར་བྱ་བ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་བོས་པ་ཉིད་ལ་ཡང་མ་བསམས་པ་སྦྱིན་དུ་འཇུག་པ་ལ་ཁྱད་པར་འགའ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །ཅི་ཞིག་སྦྱོར་དུ་བཅུག་པ་ཉིད་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བཟའ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡོན་ཏན་ཇི་ལྟ་བུ་དག་གིས་ཤེ་ན། དེའི་ཕྱིར་བསྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པས་སོ། །

[Block 345]
དེ་ཐོས་པས་ཀྱང་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པའི་ཐབས་སུ་གྱུར་པའི་ཐོས་པ་གང་དེའི་རིགས་ལས་སྐྱེས་པའི་ཡོན་ཏན་རྣམས་ལས་ཏེ། བྲོ་གར་དང་གླུ་གླིང་ལ་མཁས་པ་ལ་སོགས་པས་གཞན་དག་གིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 346]
འདི་རྣམས་ཀྱི་རྗེས་སུ་འབྲངས༌[^238]ནས་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 347]
བསྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་ནི་རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པའོ། །

[Block 348]
དེའི་ཐོས་པ་ནི་དེ་ཐོས་པ་དང་རྗེས་སུ་མཐུན་པའོ། །

[Block 349]
བསོད་སྙོམས་སྦྱོར་དུ་བཅུག་པ་ནི་རྣམ་པ་གཉིས་ཏེ། ཚུལ་ཁྲིམས་ཀྱིས་སྦྱོར་དུ་བཅུག་པ་དང་ཐོས་པས་སྦྱོར་དུ་བཅུག་པའོ། །

[Block 350]
གང་དེར་ཚུལ་ཁྲིམས་ཀྱིས༌[^239]སྨོས་པ་དེ་ལ་ནི་བསྒྲུབ་པའི་ཚིག་འདི་དང་འགལ་བར་ཤེས་པར་བྱ་བ་མ་ཡིན་ཏེ། འདིར་དམ་པ་རྣམས་ཀྱིས་སྤྱོད་པ་ཐམས་ཅད་ལ་ཚུལ་ཁྲིམས་ཉིད་དུ་གསུངས་པ་ཡིན་ཏེ། དེ་བས་ན་རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ་རྣམས་ལ་གོ་རིམས་ཀྱིས༌[^240]ཤེས་པའོ། །

[Block 351]
རྗེས་སུ་བསྒྲུབ་པ་ལ་འདི་བྱེད་པ་པོ༌[^241]ཉིད་ཡིན་ཞེ་ན་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟོས་པའི་ངོ་བོ་ཉིད་བསྟན་པའི་ཕྱིར་དེ་ནི་མིད་ན་དེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟོས་པ་དེ་ནི་མིད་ན་དངོས་གཞིར་གྱུར་པའི་ཟོས་པའོ། །

[Block 352]
གང་ཞིག་འདུན་ནས་ཞེས་བྱ་བ་འདིར་དོན་མ་ཡིན་ནོ། །

[Block 353]
གཞན་གྱི་དོན་དུ་ན་ན་སྨད་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གཞན་གྱི་དོན་དུ་དགེ་སློང་མས་སྦྱོར་དུ་བཅུག་པ་གཞན་གྱིས༌[^242]ཟ་བ་ལ་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 354]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་གཞན་གྱི་དོན་དུ་སྦྱོར་དུ་བཅུག་པར་ཤེས་བཞིན་དུ་ཟོས་ན་ཉེས་བྱས་སོ། །

[Block 355]
མི་ཤེས་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
