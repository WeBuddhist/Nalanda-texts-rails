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
[Block 3361]
ལྕི་བའི་ཆོས་ལས་འདས་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 3362]
ད་འདི་མན་ཆད་ནི་གཞན་ལ་གནོད་པར་བྱེད་པའི་ལྟུང་བྱེད་གསུམ་སྟེ། [^2195]དེ་རྣམས་ཀྱི་དང་པོ་ནི་གང་ཞེ་ན་དབུལ་པོ་སྲ་བརྐྱང་སྦྱོར་དུ་བཅུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་འདིར་སྦྱིན་པ་དང་སྦྱོར་དུ་འཇུག་པ་དང་། བསོད་ནམས་ལྷག་པར་སྦྱོང་པའི་སྒོ་ནས་གཉིས་ཀའི་དོན་དུ་སྲ་བརྐྱང་སྦྱོར་དུ་འཇུག་ན་བྱས་སམ་བྱེད་དུ་འཇུག་ན་ཐོབ༌[^2196]ན་དངོས་གཞིའོ། །

[Block 3363]
མདུན་རོལ་དུ་ནི་ཉེས་བྱས་སོ། །

[Block 3364]
གཞན་ལ་ཡང་ཆོས་གོས་གཏན་པའི་ཟོང་ཙམ་དགེ་འདུན་གྱི་དོན་དུ་དབུལ་པོ་སྦྱོར་དུ་བཅུག་ན༌[^2197]ཡང་ལྟུང་བྱེད་དོ།[^2198] །ཆོས་གོས་གཏན་པ་ཞེས་བྱ་བ་ནི་འདིར་དཔེ་ཙམ་དུ་རྣམ་པར་གནས་པར་གྱུར་པར་རིག་པར༌[^2199]བྱ་སྟེ་མ་ཆོག་པ་ལ་ནི་ཉེས་པས༌[^2200]སོ། །

[Block 3365]
དུ་མ་སྦྱོར་དུ་བཅུག་པ་ལ་ནི་རེ་རེ་ལས་ཁ་ན་མ་ཐོ་བ་རེ་རེར་འགྱུར་རོ། །

[Block 3366]
གཉིས་པ་ནི་གང་ལ་ཆོས་གོས་གཏན་པ་དབྱུང་བའི་ཕྱིར་བག་ཡངས་སུ་བྱ་བའི་ཚོགས་པ་ལ་མི༌[^2201]སྦྱིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དུས་སུ་དབྱུང་བའི་ཕྱིར་ཚོགས་པ་མི་སྦྱིན་པ་ལ་ནི་སྤང་བའི་ལྟུང་བྱེད་དུ་རྣམ་པར་གཞག་པའི་ཕྱིར་བག་ཡངས་སུ་བྱ་བ་ཞེས་བྱ་བ་འདི་ཡང་དག་པར་བསྟན༌[^2202]པའོ། །

[Block 3367]
དཔྱིད་ཟླ་ར་བའི་ཉ་ཚུན་ཆད་གློ་བུར་དུ་སྲ་བརྐྱང་འབྱིན་པར་རྗེས་སུ་གནང་བའི་དུས་དེར་རམ་གཞན་ལ་དགོས་པའི་དབང་འགའ་ཞིག་གིས་སྲ་བརྐྱང་དབྱུང་བའི་ཕྱིར། བག་ཡངས་སུ་བྱ་བ་གང་ཡིན་པ་དེ་ལའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3368]
དེ་ལྟ་བས་ན་དུས་ཐ་དད་པ་ཙམ་གྱིས་འདི་ནི༌[^2203]སྤང་བའི་ལྟུང་བྱེད་ལས་ཐ་དད་པར་རིག་པར་བྱའོ། །

[Block 3369]
འདིར་སྤང་བ་ཉིད་ལ་རྙེད་པ་མ་བྱས་པའི༌[^2204]རྒྱུ་མཚན་ཡིན་པ་དེ་བས་ན་འདི་རྣམ་པར་མ་བཞག༌[^2205]གོ། །

[Block 3370]
དགེ་སློང་མའི་དགེ་འདུན་ཚོགས་པ་ཉིད་ལ་ཆོས་གོས་གཏན་པ་དབྱུང་བའི་ཕྱིར་དེ་ཐོབ་པའི་ཞུ་བ་ཉིད་ཞུ་བ་མི་བྱེད་པར་མཚམས་ལས་འདའ་བར་བྱེད་པ་ལ་ཚོགས་པ་མི་སྦྱིན་པའི་སེམས་ཀྱིས་འདི་དང་འོག་མ་ལ་ཁ་ན་མ་ཐོ་བར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3371]
གང་ལ་གསུམ་པ་དེ་བརྗོད་པར༌[^2206]བྱ་སྟེ། དེའི་ཕྱིར་གོས་འགྱེད་པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚོགས་པ་མི་སྦྱིན་པ་ལ་ཞེས་བྱ་བའི་རྗེས་སྙེག༌[^2207]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ༌[^2208]སྨོས་སོ། །

[Block 3372]
རང་གི་རྙེད་པ་གཞན་ལ་བགོ་བའི་ཕྱིར་རྒྱུ་མཚན་འདི་ཡིན་པ་དེ་བས་ན་འདིར་ཡང་བ་ཉིད་མེད་པའོ། །

[Block 3373]
འདིར་གོས་སྨོས་པ་ནི། དཔེ་ཙམ་དུ་ཟད་དེ་ད་ལྟར་ཡང་། ཆོས་དང་ལྡན་པའི་རྙེད་པ་གཞན་ལ་བགོ་བའི་ཕྱིར་ཁ་ན་མ་ཐོ་བ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ་ཞེས་རིག་པར་བྱའོ། །

[Block 3374]
འདིས་ལེན་མི་འདོད་པ་ཉིད་ནི་མ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། འདིས་ཞེས་བྱ་བ་ནི་ཚོགས་པ་མི་སྦྱིན་པ་ལའོ། །

[Block 3375]
ལེན་མི་འདོད་པ་ཉིད་ཅེས་བྱ་བ་ནི་ཤུགས་ཀྱིས་སྐལ་བ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 3376]
ལེན་མི་འདོད་པ་ཉིད་ལ། ཚོགས་པ་མི་སྦྱིན་པ་ལ་བྱས་པ་ཉིད་དོ། །

[Block 3377]
དེ་བས་ན་ལེན་མི་འདོད་པ་ལ་འདིར་ལྟུང་བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3378]
གཞན་ལ་གནོད་པར་སྤྱོད་པ་ལས་གྱུར་པའི་ལྟུང་བྱེད་གསུམ་མོ།། །།

[Block 3379]
གང་ལ་དབྱར་ཁང་ཡལ་བར་འདོར་བ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དབྱར་ཁང་མ་གཏད་པར་འགྲོ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་གྱིའམ། གང་ཟག་གི་ཡང་ཞེས་བྱ་བ་བྱེ་བྲག་མ་སྨོས་པའོ། །

[Block 3380]
ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་ལ་དགེ་འདུན་གྱི༌[^2209]ལས་ལོག་པར་རྟོགས་པ་ལ་ཉེས་བྱས་སུ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 3381]
གནས་མལ་གྱི་རྣམ་པ་ལ་དབྱར་ཁང་འདི་ཡིན་ཏེ། དེ་བས་ན་འདི་ལ་གནས་མལ་བཞིན་དུ་བལྟ་བར་བྱ་བ་ཡིན་ཏེ། དེ་འདིར་མ་གཏད་པ་དེ་ལ་བྱ་བ་ཉིད་དོ། །

[Block 3382]
གལ་ཏེ་གནས་དེ་ལ་ཉེ་གནས་པ་ཉིད་ཡོད་ན་བྱ་བ་ཉིད་དོ། །

[Block 3383]
གལ་ཏེ་མེད་ན་ཁྱིམ་པ་འདི་ལ་ཞེས་བྱ་བར་རྣམ་པར་གཞག་པར་རིག་པར་བྱའོ། །

[Block 3384]
བརྩམས་པའི་ཆ་གང་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཉེ་འཁོར་བཏང་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དབྱར་ཁང་གི་འཕྲལ་གྱི་བྱ་བ་རྣམས་ཀྱི་ཡང་དག་པར་སྲིད་པར་གྱུར་པའི་ཕྱོགས་ནི་འདིར་ཉེ་འཁོར་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3385]
དབྱར་ཁང་སླར་མི་གཏོང༌[^2210]ངོ་། །ཁང་ཁྱིམ་གྱི་གཞི་དང་ཚོང་ཁང་གི་གཞི་ཡང་ངོ་ཞེས་བྱ་བ་ལ། སླར་མི་གཏོང༌[^2211]ངོ་ཞེས་བྱ་བའི་རྗེས་སྙེག༌[^2212]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3386]
འདིར་མདོ་དེ་གཉིས་ཀྱི་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས།

[Block 3387]
དེ་ལྟ་བས་ན་དགེ་སློང་མས་དབྱར་ཁང་སླར་མི་གཏོང༌[^2213]ངོ་། །གཏོང་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3388]
དབྱར་ཁང་ཡལ་བར་འདོར་བ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 3389]
ད་འདི་མན་ཆད་ནི་འགྲོ་བ་དང་མི་འགྲོ་བ་ལས་གྱུར་པའི་ལྟུང་བྱེད་བཞི་སྟོན་ཏེ། དེ་རྣམས་ཀྱི་དང་པོ་ནི་གང་ལ་དབྱར་གྱི་ནང་དུ་ལྗོངས་རྒྱུ་ཞིང་འགྲོ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱེ་བྲག་མ་སྨོས་པའི་ཕྱིར་ཁས་མི་ལེན་པ་ཉིད་ལ་ཡང༌[^2214]ཞེས་བྱ་བས་རྟོགས་པའོ། །

[Block 3390]
བྱ་བས་འགྲོ་བ་ནི་ལྗོངས་རྒྱུ་ཞིང་འགྲོ་བ་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་བྱིན་གྱིས་བརླབས་ཏེ་འགྲོ་བ་ལ་འདིས་གནོད་པ་མ་ཡིན་ནོ། །

[Block 3391]
བུད་མེད་ཀྱི་ཚོགས་ལ་ནི་ཤིན་ཏུ་འཕྱན་པ་ཉིད་འདི་ཡིན་ཏེ་དུས་གང་གི་ཚེ་སྐྱེས་པས་ཀྱང་འཕྱན་པར༌[^2215]མི་བྱ་སྟེ། དེར་ཡང་འགྲོ་བ་དེ་བས་ན་ཁ་ན་མ་ཐོ་བ་འདིའོ། །

[Block 3392]
ལམ་དུ་ཞུགས་པའི༌[^2216]ཚེ་ནི་ལྟུང་བྱེད་འདི་རྟོགས་པར་བྱའོ།[^2217] །བར་ཆད་ཉེ་བར་གནས་པ༌[^2218]ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་བར་ཆད་བརྒྱད་པོ་དག་ལས་གང་ཡང་རུང་བ་བྱུང་ན་དབྱར་གྱི་ནང་ལོགས་སུ་འགྲོ་བ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 3393]
གཉིས་པ༌[^2219]ནི་གང་ལ་དབྱར་གནས་པའི་འོག་ཏུ་དེར་མི་འགྲོ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེར་ཞེས་བྱ་བ་ནི་ལྗོངས་རྒྱུ་ཞིང་མི་འགྲོ་བ་ལའོ། །

[Block 3394]
དགག་དབྱེ་བྱས་པའི་འོག་ཏུ་ལམ་མི་འདའ་བར་བྱེད་པ་ལ་ཁ་ན་མ་ཐོ་བ་འདི་སྐྱེད་པར་བྱེད༌[^2220]པའོ། །

[Block 3395]
ཕྱོགས་ཀུན་ནས་འཇིགས་པ་དང་བཅས་པ་ཉིད་ཀྱིས་མི་འགྲོ་བ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་འོག་མ་དག་གི་ཆོ་གས་རྟོགས་པའོ། །

[Block 3396]
ནུས་པ་གང་དང་ལྷན་ཅིག་ཏུ་འགྲོ་བ་ལ་དོགས་པ་དང་འགལ་བ་གཉིས་མི་སྲིད་པས་དེ་ལྟ་བུའི་ལམ་གྲོགས་དང་འཕྲད་པ་ལ་མི་འགྲོ་ན་ལྟུང་བར་འགྱུར་རོ། །

[Block 3397]
ཚེས་བཅུ་དྲུག་གི་འོག་རོལ༌[^2221]དུ་ལམ་གྲོགས་ལ་སྡོད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 3398]
གསུམ་པ་ནི་གང་ལ་ཡུལ་འཁོར་དོགས་པ་དང་བཅས་པར་འགྲོ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྗོངས་རྒྱུ་ཞིང་ཞེས་བྱ་བར་སྦྱོར༌[^2222]རོ། །

[Block 3399]
དོགས་པ་དང་བཅས་པ་ཉིད་ནི་ཆོམ་རྐུན་པའི་འཇིགས་པས་འཇིགས་པ་དང་བཅས་པ་ཉིད་དོ། །

[Block 3400]
བཞི་པ་གང་ཡིན་པ་དེ་ནི་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་མི་མཐུན་པ་དང་བཅས་པར་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡུལ་འཁོར་དུ་འགྲོ་བ་ལའོ་ཞེས་བྱ་བའི་ཕྱིར༌[^2223]རྗེས་སྙེག་པའི༌[^2224]ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །
--- END BLOCKS ---
