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
[Block 5496]
དེས་ན་ཐིག་ནག་ཅེས་བྱ་བའི་དམྱལ་བ་དེའི་དབང་དུ་བྱས་ནས། ལ་ལ་གཤིན་རྗེའི༌[^3495]གཤེད་མ༌[^3496]མ་རུངས་པས། །[^3497]ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་སྨོས་སོ། །

[Block 5497]
འབར་བའི་མེ་འདྲ་བའི་གླང་དང་། ལྕགས་དེ་གཉིས་ཀྱིས་དབང་མེད་པར་བྱས་པ་ནི། གླང་ལྕགས་མེ་ལྟར་འབར་བས་དབང་མེད༌[^3498]བྱས་པའོ། །

[Block 5498]
བསྡུས་འཇོམས་རི་ཡིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་དམྱལ་བ་བསྡུས་འཇོམས་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པ་སྟེ། བསྡུས་འཇོམས་ཞེས་བྱ་བ་རི་གཉིས་ཕྲད་པ་ནི་བསྡུས་འཇོམས་རིའོ། །

[Block 5499]
དེར་ལུས་གཟིར་བ་གང་ཡིན་པ་དེ་ནི་བསྡུས་འཇོམས་རི་ཡིས་ཁ་ཅིག་ལུས་ཀྱང་གཟིར་བའོ། །

[Block 5500]
དེ་ཡིས་བརྫིས་པ་སྟེ། བསྡུས་འཇོམས༌[^3499]རི་བོས་བརྫིས་པའོ། །

[Block 5501]
དེས་ལུས་ཕྱེ་མར་བྱས་པ་གང་ཡིན་པ་དེ་ནི་དེ་ཡིས་བརྫིས་པས་ཕྱེ་མར་ལུས་གྱུར་པའོ། །

[Block 5502]
ལྕགས་གཏུན་རབ་ཏུ་འབར་བའི་ནང་དག་ཏུ། ། ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ནི་སེམས་ཅན་དམྱལ་བ་ངུ་འབོད་དག་གི་དབང་དུ་བྱས་པའོ། །

[Block 5503]
རྣོ་བ་ཡང་ཡིན་ལ་ལྕགས་ཀྱང་ཡིན་པས་ལྕགས་རྣོ་བའོ། །

[Block 5504]
ལྕགས་རྣོ་ཞིང་འབར་བའི་ཚེར་མ་ནི༌[^3500]ལྕགས་ཀྱི་ཚེར་མ་རྣོ་ཞིང་འབར་བའོ། །

[Block 5505]
དེ་རྩུབ་པ༌[^3501]ནི་ལྕགས་ཀྱི་ཚེར་མ་རྣོ་ཞིང་རྩུབ་པའོ། །

[Block 5506]
ལ་ལ་མེ་མདག་ཕུང་པོ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་སེམས་ཅན་དམྱལ་བ་ཚ་བ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 5507]
འགྲོ༌[^3502]ལྡོག་པའི་ངུ་འབོད་ནི་འགྲོ༌[^3503]ལྡོག་ངུ་འབོད་དོ། །

[Block 5508]
འགྲོ༌[^3504]ལྡོག་ངུ་འབོད་ཉིད་ཙམ་ནི་འགྲོ༌[^3505]ལྡོག༌[^3506]ངུ་འབོད་ཙམ་མོ། །

[Block 5509]
དེ་ཉིད་ཀྱི་མཐུ་ལ་བརྟེན་པ་གང་ཡིན་པ་དེ་ནི་འགྲོ༌[^3507]ལྡོག་ངུ་འབོད་ཙམ་གྱི་མཐུ་ལ་བརྟེན་པའོ། །

[Block 5510]
ཁ་ཅིག་ས་གཞི་རབ་ཏུ་འབར་བ་ལ། །ཞེས་བྱ་བ་དང་། ལྕགས་ཀྱི་ལེབ་མ་དག་གིས་ཁ་ཅིག་དཀྲིས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ནི། རབ་ཏུ་ཚ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 5511]
བརྒྱངས་ཤིང་བརྐྱང་བའི་ལྕེ་གང་ཡིན་པ་དེ་ནི་ལྕེ་ཡང་རབ་ཏུ་བརྒྱངས་པའོ། །

[Block 5512]
གཅན་གཟན་ཁྲོ་བོ་ཞེས་བྱ་བ་ནི་གཅན་གཟན་གདུག་པ་དག་གི་ཚོགས་སོ། །

[Block 5513]
ཁ་ཅིག་མེ་འབར་ཚ༌[^3508]བས་གདུངས་གྱུར་ནས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི། ཉེ་འཁོར་བ་ཆུ་བོ་རབ་མེད་ཅེས་བྱ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 5514]
མི་གཙང་རོ་མྱགས་ཁུང་ལ་མཚོ༌[^3509]སྙམ་སྟེ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི། ཉེ་འཁོར་བ་རོ་མྱགས༌[^3510]ཞེས་བྱ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 5515]
ཁ་ཅིག་མེ་ཡི་ནང་ན་ལུས་འབར་ཞིང་། །ཞེས་བྱ་བ་ལ༌[^3511]སོགས་པའི་ཚིགས་བཅད་གསུམ་ནི་སེམས་ཅན་དམྱལ་བ་མནར་མེད་པ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 5516]
ལྕགས་ཀྱི་རྣམ་པར་གྱུར་ཏེ། ཀུན་དུ་འབར་ཞིང་ཚ་བར་གྱུར་པ་དེ་ནི་མེ་འབར་ལྕགས་བསྲེགས་སོ། །

[Block 5517]
དེ་དང་མཉམ་པ་ནི་མེ་འབར་ནང་ན་ལྕགས་བསྲེགས༌[^3512]འདྲར་གྱུར་པའོ། །

[Block 5518]
རང་གི་ལས་ཀྱིས་བཟུང༌[^3513]ཞེས་བྱ་བ་ནི་མི་དགེ་བའི་ལས་ཀྱིས་བཟུང་བའོ། །

[Block 5519]
སྒྲ་འབྱིན་ཞེས་བྱ་བ་ནི་སྒྲ་སྣ་ཚོགས་འབྱིན་པའོ། །

[Block 5520]
བུ་ལོན་དེ་ད་དུ་མི་རུང་བ་ཉིད་ཀྱི་དབང་དུ་བྱས་ནས་དམྱལ་བ་མི་བཟད་ཅེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་ལྔ་སྨོས་སོ། །

[Block 5521]
དེ་ལ་ལྕགས༌[^3514]ཀྱི་རྫ་ཆེན་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་རྫ་མ་ཆེན་པོར་ཆུད་པའི་ཕྱིར་རང་དབང་མེད་པ་ཉིད་དུ་བསྟན་ཏེ། དེ་ཇི་ལྟར་ཁྱོད་ལ་བུ་ལོན་དེད་དུ་འགྲོ་བའོ། །

[Block 5522]
ས་གཞིར་མེ་འབར་དུ་བ་མེད་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་ལྕགས་ཀྱི་ཕུར་པ་མེ་འབར་བ་ལྔ་བརྒྱས་ལུས་བརྒྱངས་པ་དེས་རང་དབང་མེད་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5523]
[^3515]དེར་ཇི་ལྟར་བུ་ལོན་དེད་དུ་འགྲོ་ཞེས་པའོ། །

[Block 5524]
རབ་ཏུ་མནར་བ་ནི་ཡོངས་སུ་གདུངས་པའོ། །

[Block 5525]
སྡུག་བསྔལ་ཆེན་པོ་མྱོང་བ་ནི་སྡུག་བསྔལ་གྱི་ཚོར་བ་ཉམས་སུ་མྱོང་བ་སྟེ། འདིར༌[^3516]ཁྱོད་རང་དབང་མེད་པའོ། །

[Block 5526]
གྲང་བའི་དམྱལ་བ་ལས་བརྩམས་ཏེ། བུ་ཡུག་རླུང་གིས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། རུས་པ་དུམ་བུ༌[^3517]བརྒྱར་ཞིགས་པ་དེས་ཕོངས་ཤིང་སྒྲ་འབྱིན་པ་ག་ལ་ཡོད་པ་དེ་ནི་རུས་པ་བརྒྱར་ཞིགས་ཕོངས་པའི་སྒྲ་འབྱིན་པའོ། །

[Block 5527]
གཤིན་རྗེའི༌[^3518]གཤེད་པོས་བསད་པར་གྱུར་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་དམྱལ་བ་ཐམས་ཅད་ཀྱི་སྡུག་བསྔལ་བསྡུ་ན་རྣམ་པ་བདུན་དུ་འགྱུར་ཏེ། དེ་བསྟན་པའི་ཕྱིར་གཤིན་རྗེའི་གཤེད་པ༌[^3519]པོས་གསད་པར༌[^3520]གྱུར་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། ཇི་ལྟར་བསད་པ་ཞེ་ན། དེ་བསད་པའི་རྣམ་པ་བསྟན་པའི་ཕྱིར། གསད༌[^3521]དང་བཅད་དང་གཤགས་དང་བརྡེག༌[^3522]པ་དང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5528]
བསད་པ་ནི་རྡོ་ལ་སོགས་པས་སོ། །

[Block 5529]
བཅད་པ༌[^3523]ནི་རལ་གྲི་ལ་སོགས་པས་སོ། །

[Block 5530]
གཤགས་པ༌[^3524]ནི་སོག༌[^3525]ལེ་ལ་སོགས་པས་སོ། །

[Block 5531]
བསྲེགས་པ་ནི་མེ་འམ། རྫ་མ་ཆེན་པོའི་ནང་དུ་བཅུག་སྟེ། བཙོ་བ༌[^3526]ལ་སོགས་པས་སོ། །

[Block 5532 [VERSE]]
གཞོག་པ་ནི་སྟེའུ་ལ་སོགས་པས་སོ། །
བརྡུང་བ་ནི་བན་གླང་ལ་སོགས་པ་དང་།
བསྡུས་འཇོམས་ཀྱི༌[^3527]རི་བོ་ལ་སོགས་པས་སོ། །
གཞིག་པ་ནི༌[^3528]མདུང་ཐུང་ལ་སོགས་པས་སོ། །

[Block 5533]
གནོད་པ་མང་པོས་སྡུག་བསྔལ་བ་སྟེ། དེ་ལྟར་བཤད་པ་དག་ལས་མ་གྲོལ་བ་ཡིན་ན། ཇི་ལྟར་ངལ་བུ་ལོན་གཞལ་བའོ། །

[Block 5534]
དེ་དག་བདག་གིས་ཞེས་བྱ་བས་ནི་བསད་པ་ལ་སོགས་པས་སོ། །

[Block 5535]
དགེ་བ་དག་གི་གནས་ནི་དགེ་བའི་གནས་སོ། །
--- END BLOCKS ---
