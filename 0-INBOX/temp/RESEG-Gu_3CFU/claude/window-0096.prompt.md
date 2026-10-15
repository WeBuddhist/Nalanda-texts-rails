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
བྱས་པ་ནི་གཅིག་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདིར་བྱེད་པ་ཐམས་ཅད་རྗེས་སུ་བསྒྲུབ་པའི་ཕྱིར་གཅིག་པ་ཉིད་དེ། ལོ་ལ་སོགས་པའི་ཚད་ཀྱང་སྡོད་པ་ལ་གཞན་ལ་མི་ལྟོས་པས་མ་བཏང་བ་ནི་འདིར་སྡོད་ཅིང་བྱས་པ་ལྟུང་བ་མང་བ་ཉིད་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3362]
མི་ལྟོས་པས་བཏང་བ་ནི་དུམ་བུ་ལ་སོ་སོ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3363]
དེ་ལྟར་ན༌[^2331]མི་ལྟོས་པས་བཏང་བ་ལ་སྔར་གྱི་ཆ་ཙམ་ལྟུང་བ་སྟེ། མི་ལྟོས་པས་བར་དུ་ཡེ་བཏང་བ་ལ་གང་ཞིག་ཕྱིས་ཡང་རྩོམ་པར་བྱུང་བ༌[^2332]ལ་ཡང་ཕྱི་མའི་ཆ་ལའོ། །

[Block 3364]
ཕྱིས་ཀྱང་བསམ་པ་གཞན་གྱིས་རྩོམ་པ་ལ་ནི་གཞན་ཉིད་དོ། །

[Block 3365]
གཙོ་བོ་མ་ཡིན་པར་མཐར་ཐུག་པ་ལ་གང་ཞིག་འདིར་གཞན་ཐམས་ཅད་ལ་ཆ་ཐམས་ཅད་ཀྱི་བདག་ཉིད་མེད་པར་ལྟུང་བ་བྱས་པ་ཉིད་ཅེས་བྱ་བ་འདིར་རྣམ་པར་གནས་པར་རིག་པར་བྱའོ། །

[Block 3366]
རྗེས་སུ་བསྒྲུབ་པ་ཅིག༌[^2333]ཁོ་ན་ཡིན་དུ་ཟིན་ཀྱང་། དཔེར་ན་འཐབས་པའི་མོད་ལ་དང་འཐབས་པའི་འོག་ཏུ་སྡུམ༌[^2334]བྱེད་པ་ལ་སོགས་པའི་ཚིག་དག་ལ་ལྟུང་བ་ཐ་དད་པར་བྱས་པ་བཞིན་དུ་ཅིའི་ཕྱིར་འདིར༌[^2335]ཡང་རུང་བ་ཉིད་མ་ཡིན་པ་དང་། རྩོད་པ་དང་བཅས་པ་ཉིད་དང་རྣམ་པར་གནོན་པ་ཉིད་མ་ཡིན་པ་དང་། མ་བསྟན་པ་ཉིད་རྣམས་ལ་ཞེས་བྱ་བ་འདོད་པ་འདི༌[^2336]ལ་ལྟུང་བའོ་སྙམ་དུ་དོགས་པ༌[^2337]བསལ་བའི༌[^2338]ཕྱིར། ཡན་ལག་རྣམས་ནི་བྱེད་པ་པོ་ཐ་དད་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐོབ་པ་ལ་སྒྲིབ་པར་བྱེད་པར་འགྱུར་བ་ཉིད་ནི་དེའི་འོག་ཏུ་སྡུམ་བྱེད་པ་ལ་སོགས་པ་རྣམས་ལ་སྟེ། དེ་བས་ན་འདི་རྣམས་ལས་ཐ་དད་པ་འདི་ལ་བསྐྱེད་པའོ། །

[Block 3367]
འདིར་ནི་ཁྱིམ་བྱེད་པར་འདོད་པ་ལ་འབྲེལ་པའི་དབང་ཉིད་ལྟུང་བ་བསྒྲུབ་པ་ལ་འདི་གསལ་བར་བྱ་སྟེ། འདིའི་ཡན་ལག་འདའ་བར་བྱེད་པ་གང་ཡིན་པ་ནི་ཤིན་ཏུ་ཁྱབ་པ་ཉིད་དུ་གྱུར་པ་འདི་ལ་གང་ཞིག་སྲོག་ཆགས་རྣམས་ལ་གནོད་པར་བྱེད་པའི་དོགས་པ་མངོན་པར་རྗེས་སུ་གནང་བ་རྣམས་ལ་མ་ལྟོས་པ་བྱེད་པ་དང་། བརྩམ་དུ་མི་རུང་བ་ཉིད་ཅེས་བྱ་བ་འདའ་བར་གྱུར་པའི་ཡན་ལག་རྣམས་འདིར་དགོས་པའོ། །

[Block 3368]
དེ་བས་ན་རབ་ཏུ་འབྱེད་པ་པོ་འདི་རྣམས་དང་མི་སྦྱོར་རོ། །

[Block 3369]
འདིར་ཡན་ལག་རྣམས་ཇི་ཙམ་འདའ་བར་བྱེད་པ་ལྟུང་བ་རྣམ་དེ་ཙམ་མ་ཡིན་ཏེ། འོན་ཀྱང་ལྟུང་བ་གཅིག་ཁོ་ནར་ཟད་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་ལ་ཁང་པའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བཙལ་བ་ལའོ། །

[Block 3370]
དེས་རྗེས་སུ་གནང་བ་ལའོ། །

[Block 3371]
རྣམ་པ་དེ་ལྟ་བུས་སོ། །

[Block 3372]
གཞི་མ་དག༌[^2339]ལའོ། །

[Block 3373]
མ་བསྟན་པ་ལའོ། །

[Block 3374]
གནས་བྱས་སམ་བྱེད་དུ་བཅུག་ནའོ། །

[Block 3375]
མཐར་རོ་ཞེས་བྱ་བ་རྣམས་སྨོས་ཏེ། འདིར་གཞི་ཞེས་བྱ་བའི་སྒྲས་ནི་ས་གཞི་བརྗོད་དོ། །

[Block 3376]
བཙལ་བ་ཞེས་བྱ་བ་ནི་ཁྱད་པར་ཡོངས་སུ་མ་བཟུང་བས་ཆོས་འདི་ལ༌[^2340]རབ་ཏུ་བྱུང་བ་ལས་ཀྱང་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །སུས་བཙལ་ཞེ་ན། དེ་ནི་འདིར་སྐབས་ཡིན་པས་ལྟུང་བ་འབྱིན་པ་པོས་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 3377]
དེས་རྗེས་སུ་གནང་བ་ལའོ་ཞེས་བྱ་བ་ནི༌[^2341]དགེ་སློང་གང་གིས་ས་གཞི་བཙལ་བར་གྱུར་པས་སོ། །

[Block 3378]
རྣམ་པ་དེ་ལྟ་བུས་སོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་འབྱིན་པ་པོས་བཙལ་བ་འམ་བཙལ་བ་པོས་སོ། །

[Block 3379]
དེ་དགེ་སློང་གིས་རྟེན་དུ་གནང་བ་ལ་སྒྲུབ་པར་བྱེད་པའི་ཚིག་འདིའོ། །

[Block 3380]
དེ་ཡང་ལས་ལ་དགོས་པར་བྱ་བའི་རྫས་རྣམས་དང་འདི་རྣམས་ཀྱི་རིན་ཐང་ངོ་། །འགའ་ཞིག་ལས་ནི་གཉིས་ཀ་དག་ལ་ཞེས་འབྱུང་ངོ་། །ཉེ་བ་འཁོར་གྱིས་ཞུས་པ། [^2342]ལས་འདི་སྐད་ཅེས་ཇི་ཙམ་གྱིས་ན་རང་གིས་བཙལ་བའི་ཁང་པ་ཞེས་བགྱི། གང་ལས་གཉིས་ཡོངས་སུ་འགྲུབ་པར་འགྱུར་བ་སྟེ། བྱེད་དུ་བཅུག་པ་དང་གཞི་ཞེས་བྱ་བའོ། །

[Block 3381]
འདིར་འདི་ནི་བཙལ་བའི་ཆ་ཉིད་ལ་ལུང་རིག་པར་བྱའོ། །

[Block 3382]
དེ་ཉིད་ཀྱི་གཞུང་ཡང་འདི་ཡིན་ཏེ། གང་ཟག་གི་གཞིར་བྱེད་དུ་འཇུག་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར༌[^2343]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3383]
སོ་སོར་ཐར་པའི་མདོ་ལས་ཀྱང་རང་གིས་བཙལ་བ་ཞེས་གསུངས་པའོ། །

[Block 3384]
གང་གི་ཕྱིར་འདི་གཉིས་ཀ་དོན་མེད་པ་སྟེ་གཞན་དུ་ན་གཉིས་ཀ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3385]
གཞི་མ་དག་པ་ལའོ་ཞེས་བྱ་བ་ནི་མི་རུང་བ་ཉིད་ལ་སོགས་པ་ནི་མ་དག་པའོ་ཞེས་འོག་ནས་འབྱུང་ངོ་། །མ་བསྟན་པ་ལའོ་གནས་བྱས་སམ་བྱེད་དུ་བཅུག་ནའོ་ཞེས་བྱ་བ་ལ། མ་བསྟན་པ་ལའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་ལས་བསྟན་པ་ཐོབ་པ་ནི་བསྟན་པ་ཉིད་དོ་ཞེས་བསྟན་པ་ཉིད་ཀྱང་འོག་ནས་འབྱུང་སྟེ། དེ་ལས་བཟློག་པ་ནི་མ་བསྟན་པ་ཉིད་དོ། །

[Block 3386]
གནས་བྱས་སམ་བྱེད་དུ་བཅུག་ནའོ་ཞེས་བྱ་བ་ནི་ཁང་པ༌[^2344]བྱེད་དུ་བཅུག་ནའོ། །

[Block 3387]
མཐར་རོ་ཞེས་བྱ་བ་ནི་ཟིན་ནས་ཏེ་གནས་ཀྱི་ངོ་བོ་ཉིད་ནི་ཐོག་བཀབ་ཅིང་བསྒོ་བ་མ་གཏོགས་པ་ཀུན་ནས་བསྐོར་བ་ཉིད་དོ། །

[Block 3388]
དེ་ཟིན་པའི་སྐད་ཅིག་མ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3389]
སྔར་ནི་སྦོམ་པོར་རོ་ཞེས་བྱ་བ་འདིའི་རྗེས་ཀྱི་སྡེ་པ་ཞེས་བྱ་བ་ནི་མདོ་འདིས་བྱས་པར་རིག་པར་བྱའོ། །

[Block 3390]
འོག་མ་ལ་ཡང་དེ་དག་ཉིད་དེ་དེ་མ་བཙལ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གང་འདི་ཉེས་པ་མེད་པ་ཞེས་བྱ་བ་འདི་ནི་སྐབས་སུ་བབ་པ་དེ་དེ་མ་ཐག་པའི་གཙུག་ལག་ཁང་གི་རྒྱུ་བསླབ་པའི་གཞི་འོག་མ་ལ་ཡང་བལྟ་བར་བྱ་སྟེ། དེ་ནི་བཙལ་བ་ཉིད་མ་གཏོགས་པར་རིག་པར་བྱའོ། །

[Block 3391]
དེ་ལ་ཡང་བཙལ་བ་ཉིད་ཀྱི་དོན་དང་ངེས་པར་གྲོལ་བའི་ཆོ་ག་འདི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3392]
བཙལ་བ་ཉིད་གསལ་བ༌[^2345]ལ་འདིར་འདི་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3393]
རང་ཉིད་ཀྱིས་གནས་པ་འམ་རྗེས་སུ་གནང་བའི་གཞི་ལ་སྒྲུབ་པར་བྱེད་པ་གནས་པ་འམ་རྗེས་སུ་གནང་བས་དག་པའི་དངོས་པོ་མ་བསྟན་པའི་གནས་ཀྱི་རྒྱུའི་མཐར་ཞེས་བྱ་བའོ། །

[Block 3394]
བདག་པོ་དང་བཅས་པ་ཞེས་བྱ་བ་གཙུག་ལག་ཁང་གི་ཚིག་འདིར་གང་ཡིན་པ་ཕལ་ཆེ་བའི་ཆོས་ལ་འདི་སྐྱེ་བའི་དབང་གིས་སྨོས་པ་སྟེ་དེའི་ཡན་ལག་ནི་མ་ཡིན་ནོ། །

[Block 3395]
ཇི་ལྟར་བདག་པོ་མེད་པ་ཉིད་ལ་ཡང་ས་གཞི་སྲིད་པ་སྟེ། ཁྱིམ་གྱི་གཞི་ཡོངས་སུ་འཛིན་པ་དགག་པ་ལས་འདའ་བར་བྱས་ནས་དགེ་འདུན་ལ་བརྟེན་ནས་ཉོས་པ་བཟུང་བ་དང་། དགེ་འདུན་གྱི་གཞི་རྗེས་སུ་གནང་བས་ཞེས་བྱ་བའོ། །

[Block 3396]
ཁང་པའི་དགེ་འདུན་ལྷག་མ་པ༌[^2346]ཡན་ལག་གཞན་གཉིས་བརྗོད་པར་བྱ་སྟེ། གཅིག་གི་དོན་དུའོ་ཞེས་བྱ་བ་ནི་གང་ཟག་གཅིག་གི་དོན་དུ་བྱེད་དུ་འཇུག་ན་དགེ་འདུན་ལྷག་མར་འགྱུར་གྱི་གཉིས་དང་མང་པོ་དག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3397]
འདིར་གཞུང་ནི་ཉེ་བ་འཁོར་གྱིས་ཞུས་པའི་གཞུང་ཁ་ཅིག་ལས།

[Block 3398]
[^2347] གཉིས་ཀྱིས་སྤྱི་ལ་བྱེད་དུ་འཇུག་ན་སྦོམ་པོར་རོ་ཞེས་འབྱུང་ངོ་། །འདིར་མང་པོའི་དོན་དུ་ནི་ཉེས་པ་མེད་པ་ཉིད་རིགས་པ་ཡིན་ཏེ། དགེ་འདུན་གྱི་དོན་ཉིད་དུ་ནི་ཉེས་བྱས་སུ༌[^2348]བརྗོད་པའི་ཕྱིར་དངོས་གཞི་ནི་མ་ཡིན་ནོ། །

[Block 3399]
འདིར་ཤིན་ཏུ་འབྱུང་བར་འདོད་པ་དང་འབྲེལ་པ་ལ་གནས་པས་ཉེས་བྱས་ཙམ་ནི་མ་ཡིན་ནོ། །

[Block 3400]
ལྟུང་བ་བྱེད་པའི་དངོས་པོ་ཐམས་ཅད་ལ་ཡན་ལག་འདའ་བར་བྱེད་པ་ལ་སྦོམ་པོའི་ལྟུང་བ་བྱེད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
