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
[Block 3431]
གང་བྱས་ན་གཙུག་ལག་ཁང་གི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། འདིར་འོག་མ་ལ་ཡང་དེ་དག་ཉིད་དེ། དེ་མ་བཙལ་བ་ཉིད་དོ་ཞེས་བྱ་བ་སྔར་བསྟན་པའི་ཆོ་ག་ལ་ལྟོས་ནས་བྱེ་བྲག་བརྗོད་པར་བྱ་སྟེ། ཚོགས་ཀྱི་དོན་དུའོ་ཞེས་བྱ་བ་ནི་འདིར་ཁྱིམ་པ་ཡན་ཆད་ཀྱི་གང་ཟག་བཞི་ལ་སོགས་པ་ཚོགས་ཞེས་བྱ་བ་མངོན་པར་འདོད་པར་རིག་པར་བྱའོ། །

[Block 3432]
ཤིན་ཏུ་སྡིག་པ་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་ཁྱིམ་པའི་དོན་ཉིད་ཀྱི་བསམ་པ་ལ་འཕགས་པའི་དགེ་འདུན་རྗེས་སུ་གཟུང་བའི་བསམ་པ་ལ་ཤིན་ཏུ་དགེ་བ་ཉིད་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་རྣམ་པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 3433]
གང་ཞིག་ཚོགས་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་ཉན་ཐོས་ཀྱི་དགེ་འདུན་ནོ་ཞེས་གསུངས་པ་དེ་ནི་གླེང་གཞིའི་དབང་གིས་དེ་དཔེ་ཙམ་དུ་ཟད་པར༌[^2384]འདི་ལ་ཉེས་པ་མེད་དོ་ཞེས་རིག་པར་བྱའོ། །

[Block 3434]
གཙུག་ལག་ཁང་གི་དགེ་འདུན་ལྷག་མའོ།། །།

[Block 3435]
རྩོམ་པ་ཉིད་ནི་སྦྱོར་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་མཐར་ཐུག་པ་གང་ལ་དངོས་གཞིའི་ཚད་འདའ་བར་བྱེད་པ་ཉིད་ལ་ཐམས་ཅད་དུ་ཡན་ལག་ལྷག་མ་རྣམས་ལ་འདའ་བར་བྱེད་པ་དང་། སྦྱོར་བ་ཉིད་ལ་དེར་འདི་རྣམས་སྦོམ་པོར་སྟོན་པར་བྱེད་པའི་ཚིག་རྣམས་ཞེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 3436]
མཐར་ཐུག་པ་གང་ལ་སྦོམ་པོ་དེས་སྦྱོར་བ་ཡང་སྦོམ་པོ་རིགས་པ༌[^2385]མ་ཡིན་ནོ། །

[Block 3437]
འདིར་གཞུང་ནི་བརྩམས་ནས་བདག་ཉིད་གསོད་པར༌[^2386]བྱེད་པ་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3438]
མ་གཡོགས་པ་བྱེད་དུ་འཇུག་པའི་མཐའ་ཡང་དེ་འདྲའོ་ཞེས་བྱ་བ་ནི་གནས་དེ་མ་གཡོགས་པ་ཞིག་བྱེད་དུ་གཞུག་གོ་སྙམ་པའི་བསམ་པས་མཐའི་མཐར་ཐུག་པ་གང་ཡིན་པ་དེ་ཡང་དེ་བཞིན་དུ་སྟེ་སྦྱོར་བ་དང་འདྲ་བར་བལྟ་བར་བྱའོ། །

[Block 3439]
འདིར་གཞུང་ནི་སྟེང་མ་གཡོགས་པ་ཞིག་བྱེད་དུ་འཇུག་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3440]
སྔར་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་འདིའི་སྦྱོར་བ་ལ་ཉེས་བྱས་སོ། །

[Block 3441]
ཐམས་ཅད་དུ་ཞེས་བྱ་བ་འདིས་བྱས་པ་ཉིད་རིག་པར་བྱའོ། །

[Block 3442]
དུ་མའི་དོན་དུའོ་ཞེས་བྱ་བ་ནི་ཁང་པ་མི་རུང་བ་ལ་སོགས་པའི་ཡན་ལག་ཐམས་ཅད་ལས་འདས་པ་དུ་མའི་དོན་དུ་བྱེད་དུ་བཅུག་པའི་མཐའ་གང་ཡིན་པ་དེ་ཡང་སྦྱོར་བ་དང་འདྲ་བར་བལྟ་བར་བྱའོ། །

[Block 3443]
འདིར་གཞུང་ནི་གཉིས་ཀྱི་སྤྱི་ལ་བྱེད་དུ་འཇུག་ན་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3444]
མ་བསྐོས་པར་རོ་ཞེས་བྱ་བ་ནི་འཚོལ་བ་པོ་འམ་གནང་བ་པོས་རྗེས་སུ་མ་གནང་བར་གནས་བྱེད་དུ་འཇུག་པ་སྟེ། དེའི་མཐའ་གང་ཡིན་པ་དེ་ཡང་སྦྱོར་བ་དང་འདྲ་བར་བལྟ་བར་བྱའོ། །

[Block 3445]
གང་གི་དེ་སོ་སོར་བཟུང་བ་དེའི་དོན་ཉིད་དུ་འདི་བྱེད་དུ་འཇུག་པས་མངོན་པར་འདོད་པའོ། །

[Block 3446]
འོ་ན་ཅིའི་ཕྱིར་དངོས་གཞིར་རྣམ་པར་མི་གཞག་སྟེ། ལྷག་མ་བསྒྲུབ་པ་དག་ལ་འདིར་གནས་པར་འགྱུར་རོ། །

[Block 3447]
ཇི་ལྟར་རང་བཞིན་མི་མཐུན་པ་བྱེད་དུ་འཇུག་པས་འདས་པ་ལ་ཡང་རྗེས་སུ་གནང་བ་ལ་ནི་བཟུང་བ༌[^2387]འདིས་འགྱུར་ཏེ་དེ་ནི་འཇུག་པའོ། །

[Block 3448]
དེ་བས་ན་རྗེས་སུ་གནང་བ་དང་བསྒྲུབ་པ་དེ་ལ་གནོད་པ་ཉིད་ཀྱི་ཕྱིར་དངོས་གཞི་བསྐྱེད་པའོ། །

[Block 3449]
རྗེས་སུ་མ་གནང་བ་ལ་སྦྱོར་བའོ། །

[Block 3450]
འདིར་གཞུང་ནི་ཡི་གེ་ཁ་ཅིག་ལས་མ་བསྐོས་པར་བྱེད་དུ་འཇུག་ན་ཉེས་པ༌[^2388]སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3451]
གང་ཟག་གིས་སོ་ཞེས་བྱ་བ་ནི་སྒྲུབ་པར་བྱེད་པས་བྱེད་དུ་འཇུག་ན་དེ་བཞིན་དུ་མཐའོ། །

[Block 3452]
འདིར་གཞུང་ནི་གང་ཟག་གི་གཞིས་བྱེད་དུ་འཇུག་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3453]
འདི་ཐམས་ཅད་ཞུ་བ་དང་འབྲེལ་པ་བསླབ་པའི་གཞི་གཉིས་ཀྱི་དབང་དུ་བྱས་པ་ཡིན་གྱི་གང་ཟག་གི་ཞེས་བྱ་བ་འདི་ནི་མ་གཏོགས་པར་རིག་པར་བྱའོ། །

[Block 3454]
གང་གི་ཕྱིར་གཙུག་ལག་ཁང་གི་བསླབ་པའི་གཞི་ལ་བཙལ་བ་ཉིད་ཀྱི་ཡན་ལག་རྣམ་པར་མ༌[^2389]བཞག་པའི་ཕྱིར་རོ། །

[Block 3455]
རང་བཞིན་མི་མཐུན་པ་ཡང་ངོ་ཞེས་བྱ་བ་ལ༌[^2390]ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་ནི་དེ་བཞིན་དུ་བྱེད་དུ་འཇུག་ན་མཐའ་དེ་དང་འདྲའོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^2391]པའི་ཕྱིར་རོ། །

[Block 3456]
འདིར་གཞུང་ནི་རང་བཞིན་མི་མཐུན་པའི་ཞལ་ཏ་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3457]
གསོལ་བའི་འོག་ཏུ་མ་གྲུབ་ན་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་གསོལ་བའི་འོག་ཏུ་གནས་དེ་མོར་མ་གྲུབ་པ༌[^2392]གང་ཡིན་པ་དེ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 3458]
འདིར་རིམ་པ་ཉིད་ནི་སྐྱོན་ཏེ་དེ་བས་ན་རིམ་པའི་ངོ་བོས་མི་འདོད་པའི་བསམ་པས་མ་གྲུབ་པ་ལ་ཉེས་བྱས་སུ༌[^2393]རྣམ་པར་གཞག་གི་བར་ཆད་ཀྱི་དབང་གིས་མ་གྲུབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 3459]
འདིར་གཞུང་ནི་བཙུན་པ་རེ་ཞིག་གཞི་བཙལ་ནས་མི་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སུའོ། །

[Block 3460]
ཁང་པ་བསྟན་པ་གསོལ་ནས་བགྱིད་དུ་མི་སྩོལ༌[^2394]ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་བྱས་སུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3461]
ཁང་པ་དང་གཙུག་ལག་ཁང་གི་དགེ་འདུན་ལྷག་མ་ཞུ་བའི་སྐབས་སོ།། །།

[Block 3462]
གང་དུ་དངོས་གཞི་དང་འབྲེལ་པ་བརྗོད་པ་ལ་དགེ་འདུན་གྱི་ལྷག་མ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཕམ་པར་འགྱུར་བ་ལྷག་པར་སྤྱོད་པས་དགེ་སློང་ཉམས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མི་ཚངས་པར་སྤྱོད་པ་ལ་སོགས་པས་ཕམ་པར་འགྱུར་བ་ལྷག་པར་སྤྱོད་པ་དེས་སྐུར་པ་འདེབས་ན་དགེ་འདུན་གྱི་ལྷག་མའོ། །སུ་ལ་ལྷག་པར་སྤྱོད་པ་དེས་སྐུར་བ་འདེབས་ཤེ་ན། དེའི་ཕྱིར་དགེ་སློང་ཉམས་པ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ་ཚུལ་ཁྲིམས་དང་ལྡན་པ་འབའ་ཞིག་ལ་མ་ཡིན་གྱི་ཉམས་པ་ལ་སྐུར་བ་བཏབ་ན་ཡང་ངོ་། །བསྙེན་པར་རྫོགས་པའི་ལས་དང་བཅས་པ་ཚུལ་ཁྲིམས་དང་ལྡན་པ་གཅིག་པུ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3463]
ཉམས་པ་ལ་ཡང་ཞེས་བྱ་བའི་ཚིག་ནི་དགེ་སློང་ཕ་དང་དགེ་སློང་མ་ཉིད་ཉམས་པ་ཞེས་བྱ་བ་འདི་ལ་སྐུར་བ་འདེབས་པའི་དོན་དུའོ། །

[Block 3464]
མ་དག་པ་དང་ཉམས་པ་ལ་དགེ་འདུན་ལྷག་མའི་ལྟུང་བའི་ཚིག་ལ་གཞུང་ནི་འདི་ཡིན་ཏེ་ཞུ་བ་ལས་ཀྱང་བཙུན་པ་དགེ་སློང་རང་འདི་སྐད་ཅེས་བདག་གིས་མི་ཚངས་པར་སྤྱོད་པ་འཁྲིག་པའི་ཆོས་བསྟེན་ནོ་ཞེས་མཆི་བ་དེ་ལ་དགེ་སློང་གིས་གཞི་མ་མཆིས་པར་རྐུ་བ་འམ་འགུགས་པའི་སྨྲ་བས་སྐུར་པ་འདེབས་ན་ལྟུང་བ་ཅིར་འགྱུར། དགེ་འདུན་ལྷག་མར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3465]
རང་གི་ཕྱོགས་ཀྱི་བསྙེན་པར་རྫོགས་པ་དང་མཐུན་པ་ནི་མཚན་དང་ཁས་ལེན་པ་དག་གིས་ཞེས་བྱ་བ་འདི་ལ་དེའི་དམིགས་ཀྱིས་བསལ་བ་བསྟན་པའི་ཕྱིར། ཕྱོགས་ལས་རང་ཉིད་ནི་འདིར་ཡན་ལག་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་འདི་མཚན་དང་ཁས་ལེན་པ་དག་གི་ཕྱོགས་ལས༌[^2395]རང་ཉིད་དུ་གསུངས་པ་གང་ཡིན་པ་དེ་འདིར་ཁས་ལེན་པ་ནི་མ་ཡིན་ནོ། །

[Block 3466]
མཚན་མི་མཐུན་པ་ལ་སྐུར་བ་འདེབས་པ་དང་ལྟ་བ་མི་མཐུན་པ་ལ་སྐུར་བ་འདེབས་པ་ལའང་དགེ་འདུན་ལྷག་མའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3467]
འདིར༌[^2396]ཞུ་བ་ལས་མཚན་དང་ལྟ་བ་ཡན་ལག་མ་ཡིན་པ་ཉིད་ལ་གཞུང་ནི་དགེ་སློང་གིས་དགེ་སློང་མ་ལ་གཞི་མེད་པའི་ཕམ་པར་འགྱུར་བའི་ཆོས་ཀྱིས་སྐུར་བ་འདེབས་ན་དགེ་འདུན་ལྷག་མའོ། །

[Block 3468]
དེ་བཞིན་དུ་དགེ་སློང་མས་དགེ་སློང་ལ་གཞི་མེད་པའི་ཕམ་པར་འགྱུར་བའི་ཆོས་ཀྱིས་སྐུར་པ་འདེབས་ན་དགེ་འདུན་ལྷག་མའོ་ཞེས་གསུངས་སོ། །

[Block 3469]
ཉམས་པ་ལ་སྐུར་བ་འདེབས་པ་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པ་ཞེས་བྱ་བ་ལས་ན་ཁས་ལེན་པ་དང་མི་ལེན་པ་ཉིད་ཀྱི་ཐ་དད་པ་ལ་འདྲ་བའི་ཁ་ན་མ་ཐོ་བ་འདིར་རྣམ་པར་གཞག་གོ། །

[Block 3470]
ཤིན་ཏུ་སླར་ཁྲོས་པའི་འཇུག་པ་འདི་ཤིན་ཏུ་ཡང་སྒོར་གྱུར་པ་དགེ་སྦྱོང་གི་རིགས་ལ་སྐུར་པ་འདེབས་པ་ཞེས་བྱ་བ་དང་། ཉམས་པ་དང་མཚན་ཐ་དད་པའི་ཡུལ་ལ་ཡང་ལྟུང་བ་མཚུངས་པ་ཉིད་དུ་འདི་ལ་རྣམ་པར་གཞག་པའོ། །
--- END BLOCKS ---
