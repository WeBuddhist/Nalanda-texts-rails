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
[Block 3571]
གང་དུ་བསྒོ་བ་ལས་གྱུར་པའི་དགེ་འདུན༌[^2448]ལྷག་མ་རྣམས་ཤེ་ན། དེའི་ཕྱིར་དེའི་མཐའ་ལ་མི་གཏོང་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་འདི་ལས་ཀྱི༌[^2449]གལ་ཏེ་ཞེས་བྱ་བ་སྨོས་པ་ལ་བསྒོ་བའི་མཐའ་སྟེ། ཐ་མ་ལ་མི་གཏོང་བ་གང་ཡིན་པ་དེ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3572]
ད་ནི་འདི་བསྒོ་བར་བྱེད་པ་ཐུན་མོང་བ་སྟེ་བསྒོ་བར་བྱེད་པ་ལས་སྐྱེས་པའི་དགེ་འདུན་གྱི་ལྷག་མ་རྣམས་ལ་བརྩམས་ལ༌[^2450]སོ་སོ་དང་འབྲེལ་པ་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་བརྗོད་པར་བྱ་སྟེ། དོན་གང་མི་གཏོང་ན། དགེ་འདུན་གྱི་དབྱེན་བྱེད་པའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བརྟུལ་བར་བྱེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་བརྟུལ་བར་བྱེད་པ་ཉིད་ཅེ་ན་དེའི་ཕྱིར་དབྱེན་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །གང་གི་ཕྱིར་དབྱེན་བྱེད་པ་ལ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་གྱིའོ་ཞེས་སྨོས་ཏེ། དགེ་འདུན་གྱི་དབྱེན་ལའོ། །

[Block 3573]
དབྱེན་བྱེད་པའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 3574]
གང་ཞིག་མི་གཏོང་ན་དེའི་རྗེས་སུ་ཕྱོགས་པ་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དེའི་གྲོགས་ཉིད་རྗེས་སུ་སྒྲུབ་པར་བྱེད་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དང་འབྲེལ་པ་དེར་དགེ་འདུན་གྱི་དབྱེན་དང་འབྲེལ་པའི་གྲོགས༌[^2451]ནི་དེའི་གྲོགས་ཉིད་དོ། །

[Block 3575]
དེ་ལ༌[^2452]རྗེས་སུ་བསྒྲུབ་པ་ཉིད་ནི་ཤིན་ཏུ་དམན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3576]
སྔོན་ནས་འཇུག་པ་འདི་ལ་ན་སྨད་པ་ཐོབ་པ་ཉིད་ལ་འདི་བཏགས་པའོ། །

[Block 3577]
རྗེས་སུ་ཕྱོགས་པའི་དགེ་འདུན་ལྷག་མའོ།། །།

[Block 3578]
གང་ཞིག་མི་གཏོང་ན་ཁྱིམ་སུན་འབྱིན་པའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རང་སྐྲོད་པར་བྱེད་པའི་དགེ་འདུན་ལ་ལོག་པའི་བསམ་པས་དེ་དེ་ལ་དེ་ལྟར་ཞུགས་སོ་ཞེས་བརྫུན་དུ་སྨྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིའི་བདག་ཉིད་ཀྱི་རང་སྐྲོད་པ་ལ་དགེ་འདུན་གང་ཞིག་བྱེད་པ་པོ་དེར་འདི་ལ་ཁོ་བོ་ཅག་གི༌[^2453]སྐྲོད་པ་ལ་ལས་གོ་བར་བྱ་བ་ལ་འཇུག་པར་གྱུར་པ་ལ་ལོག་པའི་བསམ་པས་འདུན་པ་དང་ཞེ་སྡང་དང་འཇིགས་པ༌[^2454]དང་རྨོངས་པ་དང་སྡུག་བསྔལ་གྱིས་འབྱུང་བར་འགྱུར་བ་ཞེས་བྱ་བ་ལོག་པར་སྨྲ་བ་པོ་ཉིད་གང་ཡིན་པའི་རྣམ་པ་དེ་ལྟ་བུའི་བརྫུན་དུ་སྨྲ་བ་རྣམ་པ་དེ་ལྟ་བུའི་ཚིག་གིས་མཐའ་མར་མ་བཏང་བ་ལའོ། །

[Block 3579]
ཁྱིམ་སུན་འབྱིན་པའི་དགེ་འདུན་ལྷག་མ་སྟེ་བཅུ་གཉིས་པའོ།། །།

[Block 3580]
གང་ཞིག་མི་གཏོང་ན་བཀའ་བློ་མི་བདེ་བའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་གིས་ལྷག་པའི་ཚུལ་ཁྲིམས་ཀྱིས་གླེང་བ་ཉིད་ན་བདག་ཉིད་ཀྱི་དེ་ལ་དགེ་སློང་དག་གིས་བརྗོད་པར་མི་བྱ་བ་ཉིད་དུ་བྱེད་པའོ༌[^2455]ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་གིས་ལྷག་པའི་ཚུལ་ཁྲིམས་ཀྱིས་གླེང་བ༌[^2456]ཉིད་ན་འདིར་བདག་ཉིད་དང་འབྲེལ་པའི་ལྷག་པའི་ཚུལ་ཁྲིམས་ལ་དགེ་སློང་རྣམས་ཀྱིས་བརྗོད་པར་མི་བྱ་བ་ཉིད་ལ༌[^2457]བྱེད་པ་གང་ཡིན་པ་དེ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3581]
ཕྱོགས་བཅུ་ན་གནས་པའི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་དགེ་སློང་གི་དགེ་འདུན་ལ་འདིར་དགེ་སློང་རྣམས་ཀྱིས་ཞེས་བྱ་བ་བརྗོད་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 3582]
ལྷག་པའི་ཚུལ་ཁྲིམས་ཞེས་བྱ་བ་ནི་འདིར་འདུལ་བའི་རྣམ་པ་ཐམས་ཅད་བསྟན་པ་ཡིན་ནོ། །

[Block 3583]
ཡོངས་སུ་གཅོད་པ་བརྗོད་པར་མི་བྱ་བ་ཉིད་བྱེད་པ་ལ་ཇི་སྲིད་དུ་ཅུང་ཟད་དགེ་སློང་ཞེས་བྱ་བ་འདིས་ཉེས་བྱས་སུ་བྱ་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 3584]
བསླབ་པའི་གཞི་རྣམས་ཀྱིས་ཀྱང་རྣམ་པར་གཅོད་པར༌[^2458]བརྗོད་པར་མི་བྱ་བ་ཉིད་བྱེད་པ་ལ་ཉེས་བྱས་ཉིད་དོ། །

[Block 3585]
སོ་སོ་ཉིད་ཐོབ་པ་ལ་འདི་ནི་ཁ་ན་མ་ཐོ་བ་སྟེ། ཡོངས་སུ་གཅོད་པའི་བསླབ་པའི་གཞི་རྣམས་ཀྱིས་བརྗོད་པར་མི་བྱ་བ་ཉིད་བྱེད་པ་ནི་སོ་སོ་ཉིད་ཐོབ་པ་མ་ཡིན་ནོ། །

[Block 3586]
དེ་བས་ན་འདིར་སྦོམ་པོ་མི་བསྐྱེད་པ༌[^2459]ཉིད་དོ། །

[Block 3587]
དེར་ཉེས་བྱས་ཉིད་དེ༌[^2460]མི་མཛེས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 3588]
བཀའ་བློ་མི་བདེ་བའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 3589]
དགེ་འདུན་ལྷག་མ་རྣམས་རྫོགས་སོ།། །།

[Block 3590 [HEADING]]
## སྤང་བ་རྣམས། ^7-0

[Block 3591]
ཉིན་མཚན་གྱི་དང་པོ་མ་ཡིན་པ་ལ་ཐ་མ་མ་ཡིན་པ་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཆོ་ག་ཐམས་ཅད་ཀྱི་དབང་དུ་བྱ་བ་མདོ་འདི༌[^2461]དང་མདོ་འོག་མ་གཉིས་ཀྱང་དེའི་ཁ་ན་མ་ཐོ་བའི་ཡན་ལག་ཏུ་གྱུར་པ་དང་པོའོ། །

[Block 3592]
ཉིན་མཚན་གང་ལ་ཉིན་མཚན་གྱི་དང་པོ་མེད་པ་དེ་ནི་དང་པོ་མ་ཡིན་པའོ། །

[Block 3593]
དེའི་མཐའི་ཐ་མ་ལ་མཐར་ཐུག་པར་གྱུར་པའི་སྐད་ཅིག་མ་གང་ཡིན་པ་དེ་ལས་གཞན་ལ་ཡོད་པ་ཉིད་ནི་ཡོད་པ་ཉིད༌[^2462]མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3594]
ཞག་བཅུ་འདས་པར་བྱེད་པ་ལ་གང་ཞིག་སྤང་བ་རྣམ་པར་གཞག་པ་ཟླ་བ་གཅིག་འདས་པ་དང་། ཞག་དྲུག་འདས་པ་དང་ཞག་བདུན་འདས་པ་ལ་ཕྱི་མའི་ཆ་ཙམ་ཡོད་པ་ལ་ཡང་དེར་གཞན་ཉིན་ཞག་གཅིག༌[^2463]པའི་དང་པོ་ཉིད་དོ། །

[Block 3595]
མཐར་འབྱུང་བའི་ཆ་ལ་བསྐྲད་པ་བརྗོད་པ་སྟེ།

[Block 3596]
དང་པོ་འགའ་ཞིག་ལ་ནི་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་འདི་ལ་འདི་བྱེད་པའོ། །

[Block 3597]
འདིར་ལུང་ནི་འཆང་བ་འམ༌[^2464]བསླབ་པའི་གཞི་ལས་དགེ་སློང་གིས་ཚེས་གཅིག་ལ་ཆོས་གོས་རྙེད་དམ་ཚེས་ལྔ་ལ་ལྷུང་བཟེད་རྙེད་ན་ཞེས་གསུངས་པས་ཚེས་འདིའི༌[^2465]

[Block 3598]
དང་པོ་ཐུན་ཚོད་ངེས་པར་མ་སྨོས་པར་ཚེས་བཅུ་གཅིག་གི་ཉིན་པར་སྐྱ་རེངས༌[^2466]ཤར་ན་སྤང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3599]
གང་གི་ཕྱིར་འདིས་ཚིག་བསྟན་པར་འགྱུར་ཏེ། མཐའ་མ་ལས་གཞན་པའི་ཉིན་མཚན་གྱི་ཆ་རྣམས་ལ་ཉིན་མཚན་གྱི་ཡན་ལག་རྣམས་ལ༌[^2467]ཡོད་པ་མ་ཡིན་པ་ཉིད་གང་གི་ཕྱིར་འདི་རྣམས་ཡོད་པ་ཉིད་ལ་འདི་ནི་འདི་སྐད་ཅེས་ཚེས་གཅིག་གི༌[^2468]སྔ་དྲོ་ཞིག་ལ་ཞེས་བྱ་བ་བརྗོད་པར་བྱ་བ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 3600]
གནས་པ་ལ་ནི་སྦྱོར་བའི་སྣོད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་མ་རྫོགས་པ་དང་ལྷན་ཅིག་གནས་པ་དང་བསྙེན་པར་རྫོགས་ན་ཡང་ལྟ་བའི་རྣམ་པ་མི་གཏོང་བ་དང་ལྷན་ཅིག་གནས་པ་དང་། དགེ་ཚུལ་བསྙིལ་བ་དང་ལྷན་ཅིག༌[^2469]གནས་པ་དང་། [^2470]མཚན་མི་མཐུན་པ་དང་གནས་པ་དང་། མཚན་མི༌[^2471]མཐུན་པ་དང་གནས་གཅིག་ན་ལྷན་ཅིག་ཉལ་བ༌[^2472]དང་། སྣང་བ་དང་བཅས་པ་དང་དམག་གི་ནང་ན་གནས་པ་ལ་སྦྱོར་བའི་སྣོད་ཉིད་ཡིན་པའོ། །

[Block 3601]
མཐའ་ཡས་པ་གནས་པ་ཉིད་ནི་སྦྱོར་བ་ཉིད་དོ། །

[Block 3602]
དེའི་ཡུལ་ལྷན་ཅིག་ཉལ་བ་ལ་ཕྱོགས་སྔ་མ་རྣམས་དང་དམག་གི་ནང་དུ་གནས་པ་ལ་ཉེས་པ་མེད་པ་ཉིད་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3603]
འདིར་མཚན་མོ་ཙམ་ལ་དམག་གི་ནང་ན་འདུག་པ་མ་གཏོགས་པ་གནས་ན་མལ་ཆ་བཟུང་བའི༌[^2473]ཕྱིར་རོ། །

[Block 3604]
གང་གི་ཕྱིར་མཚན་མོ་ལམ་ལ་རབ་ཏུ་གྲགས་པ་ཡིན་པ་སྟེ། དེ་དག་གི་མཚན་མོ་གསུམ་པ་ལ་འདྲོན་པ་དག་ཕྱི་རོལ་དུ་དགར་བར་བྱའོ་ཞེས་གསུངས་པ་ལས་མཚན་མོ་ཞེས་སྨོས་པའི་ཕྱིར་རོ། །

[Block 3605]
དེ་བས་ན་མཚན་མོ་དང་འབྲེལ་པ་འདི་རྣམས་ལ་མལ་དང་ལྷན་ཅིག་སྦྱོར་བར་རྟོགས་པར་བྱའོ། །

[Block 3606]
དམག་གི་ནང་ན་གནས་པ་ལ་ཉེས་པ་དང་ལྡན་པ་ཉིད་དོ། །

[Block 3607]
དེ་བས་ན་ཉིན་མོ་ཡང་འདིར་གནས་པར་སྦྱོར་བ་ལ་ཞུགས་པའོ། །

[Block 3608]
དེའི་དང་པོ་ནི་སྐྱ་རེངས༌[^2474]

[Block 3609]
དང་པོ་དེའིའོ༌[^2475]ཞེས་བྱ་བ་ལ༌[^2476]ཉིན་མཚན་དེའི་དང་པོ་ནི་སྐྱ་རེངས༌[^2477]

[Block 3610]
དང་པོ་གང་ཡིན་པ་དེ༌[^2478]ཡིན་པར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
