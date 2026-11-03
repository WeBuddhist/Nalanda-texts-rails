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
[Block 2801]
གོས་ལྕི་བ་བསྟེན་པའི་སྤང་བའོ། །གང་ལ་གོས་ཡང་བ་བསྟེན་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྲང་ལྔ་པའི་མཐར་ཐུག་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སོགས་པ༌[^1824]ཞེས་བྱ་བའི་སྒྲས་ནི་ཀཱར་ཥཱ་པ་ཎ་ཉི་ཤུ་ལ་སོགས་པ་རི་བའི་གོས་བདག་གིར་བྱེད་པ་ལའོ་ཞེས་བྱ་བའི་རྗེས་བསྙེགས་པའི་ཕྱིར་རོ། །

[Block 2802]
འདིར་མཐར་ཐུག་པའི་སྒྲས་ནི་སྐྱེ་བོའི་གྲངས་བཟུང་བར་བྱས་པར་རིག་པར་བྱའོ། །

[Block 2803]
འདིར་གཞུང་ནི་སྤང་བ་ཞེས་བྱ་བ་ནི་སྲང་ལྔའམ་ལྔ་ལས་ཆུང་བའོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ཏེ། འདིས་ནི་འདི་ལྟ་སྟེ་བུད་མེད་ནི་གོས་བཟང་པོ་གྱོན་ན་གསོ་རོ་སྐྱེ་བས་དེའི་ཕྱིར་འདི་གཉིས་བཀག་པའོ། །

[Block 2804]
གོས་ཡང་བ་བསྟེན་པའི་སྤང་བའོ། །

[Block 2805]
[^1825]སྤང་བའི་ལྟུང་བྱེད་རྣམས་རྫོགས་སོ།། །།

[Block 2806 [HEADING]]
## དགེ་སློང་མའི་ལྟུང་བྱེད་འབའ་ཞིག་ཏུ་གྱུར་པ་རྣམས། ^7-0

[Block 2807]
ད་ནི་དགེ་སློང་མ་རྣམས་ཀྱི་ལྟུང་བྱེད་འབའ་ཞིག་ཏུ་འགྱུར་བ་དག་བཤད་པར་བྱ་སྟེ། དེ་ལ་བདུན་ཅུ་རྩ་གཉིས་སོ་ཞེས་བྱ་བ་ནི་སྔར་དགེ་སློང་གི་རྣམ་པར་འབྱེད་པའི་སྐབས་སུ་བསྟན་ཟིན་ཏོ། །

[Block 2808]
དེ་དག་ཀྱང་གང་ཞེ་ན། མ་བསྐོས་པ་ལ་སོགས་པ་བཅུ་དང་། སྐྲོད་པ་དང་། ཡང་ཡང་ཟ་བ་དང་། ཟས་བསོད་པ་སློང་བ་དང་། འདུག་པ་དང་། འགྲེང་བ་དང་། ཕྱིར་མ་བླངས་པ་སྤྱོད་པ་དང་། མ་ལོན་པ་དང་དབྱར་གྱི་རས་ཆེན་ལས་གྱུར་པ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྟུང་བྱེད་དགུ་བཅུ་པོ་འདི་དག་ལས་བཅོ་བརྒྱད་པོ་འདི་དག་མ་གཏོགས་པ་ལྷག་མ་ཇི་སྙེད་པར་གྱུར་པ་རྣམས་ཞེས་བྱ་བའི༌[^1826]དོན་ཏོ། །

[Block 2809]
འདིར་ཁ་ཅིག་ནི་མི་སྲིད་པའི་ཕྱིར་དགེ་སློང་མ་རྣམས་ཀྱི་ལྟུང་བར་མི་གཞག་པ་ཡང་ཡོད་དེ། འདི་ལྟ་སྟེ་མ་བསྐོས་པར་སྟོན་པ་ལ་སོགས་པ་རྣམས་ཏེ། གང་གི་ཕྱིར་དགེ་སློང་མ་རྣམས་ཀྱིས་དགེ་སློང་དག་ལ་བསྟན་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2810]
ཁ་ཅིག་ནི་ཤིན་ཏུ་སྨད་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2811]
འདི་ལྟ་སྟེ་བླངས་པ་ཟ་བའི་ལྟུང་བྱེད་དེ་གང་གི་ཕྱིར་སྐྱེས་པས་བླངས་པ་ཟ་བ་ལ། བུད་མེད་ཀྱིས་ཟ་བ་ནི་སྨད་པར་བྱ་བ་མ་ཡིན་ཏེ། དེ་བཞིན་དུ་གཞན་དུ་ཡང་ཇི་ལྟར་རིག༌[^1827]པར་རྟོགས་པར་བྱའོ། །

[Block 2812]
དགེ་སློང་མའི་ལྟུང་བྱེད་རྣམས་ལ། དགེ་སློང་གི་ཅུང་ཟད་འཇུག་པ་མཉམ་པ་ཁོ་ན་ཡིན་ཏེ། འདི་ལྟ་སྟེ་དཔེར་ན། སྐྲོད་པའི་ལྟུང་བྱེད་ལྟ་བུའོ། །

[Block 2813]
ཅུང་ཟད་མེད་པ་ནི་འདི་ལྟ་སྟེ། མ་བསླབས་པའི༌[^1828]བསླབ་པ་ལ་བསྙེན་པར་རྫོགས་པ་རྣམ་པར་མ་བཞག་པའི་ཕྱིར། སྐྱེས་པ་བསླབ་པ་སྤྱོད་པ༌[^1829]ལའོ། །

[Block 2814]
འགའ་ཞིག་ཏུ༌[^1830]ལྟུང་བ་མེད་དོ། །

[Block 2815]
ཉེས་པའི་གླགས༌[^1831]མི་རྙེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2816]
འདི་ལྟ་སྟེ་ལོ་རེ་རེར་རབ་ཏུ་འབྱིན་ཏུ་བཅུག་པ་ལ་གང་གི༌[^1832]ཕྱིར་བུད་མེད་ཀྱི་ཚོགས་ལ་ཉེ་བའི་ཉོན་མོངས་པ་སྲེད་པ་ཤས་ཆེ་བ་ཡིན་གྱི་སྐྱེས་པ་ལ་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 2817]
འགའ་ཞིག་ཏུ་ཇི་ལྟར་ཐོབ་པའི་ཉེས་བྱས་ནི་འདི་ལྟ་སྟེ་ཁྲི་གཅིག་ལ་དགེ་སློང་དག་ཉལ་བ་ལྟར༌[^1833]ཀུན་ནས་རེག་པར་འགྱུར་ནའོ། །

[Block 2818]
འདིར་ནི་ཕྱོགས་ཙམ་ཞིག་བསྟན་པ་ཡིན་གྱི། རྒྱས་པར་ནི་བྱེ་བྲག་བཤད་མཚོ་ལས་ཤེས་པར་བྱའོ། །

[Block 2819]
ཆོས་ཡོངས་སུ་ཞུས་པ་ལས་དགེ་སློང་ལས་དགེ་སློང་མས་ཟང་ཟིང་ཉེ་བར་བསྒྲུབ་ཏུ་རུང་ངོ་ཞེས་བྱ་བ་འདི་གནས་ལས་ཐོབ་པ་ཕྲན་ཚེགས་དག་ལས་སྡུད་པ་པོ་རྣམས་ཀྱིས་ཡང་དག་པར་བཅུག་པ་དེ་བསྟན་པར་བྱ་སྟེ། དགེ་སློང་གིས་རབ་ཏུ་བྱུང་བ་མོའི་ཕྱིར་ཟང་ཟིང་ཉེ་བར་སྒྲུབ༌[^1834]ཏུ་རུང་སྟེ། ཆུང་མར་གྱུར་པ་ཉིད་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་སྔོན་ཁྱིམ་པར་གནས་པའི་ཚེ་གང་ཞིག་ཆུང་མར་གྱུར་པ་ཉིད་ལས་ཏེ། དེ་ལ་ཡང་དགེ་སློང་མ་ཉིད་དུ་གྱུར་ཟིན་པ་ལ་དགེ་སློང་གིས་ཉེ་བར་བསྒྲུབ་ཏུ་རུང་བ་ཁོ་ན་སྟེ། དེ་ནི་རུང་བ་མ་ཡིན་པར་ཤེས་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2820]
དེས་བླང་དུ་རུང་ངོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་དེས་ཟང་ཟིང་ཉེ་བར་སྒྲུབ་པར༌[^1835]བྱེད་པའི་དགེ་སློང་དེ་ལས་ཟང་ཟིང་བླང་དུ་རུང་བ་ཁོ་ན་ཡིན་པའོ། །

[Block 2821]
ཕྲན་ཚེགས་དག་ལས་སྐྱེས་པ་རྣམས་དང་ལྷན་ཅིག་མལ་དུ་གཏོགས་པ་ཡང་དག་པར་ཞུགས་པ་བརྗོད་པར་བྱ་སྟེ། བུ་ཆུང་ངུ་དང་ལྷན་ཅིག་ཉལ་བ་ལ་ནི་མ་གཏོགས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བྱིས་པ་གང་མ་མེད་པར་མཚན་མོ་ཉལ་མི་ནུས་པ་དེ་ནི་བུ་ཆུང་ངུ་ཞེས་བྱ་བར་རྣམ་པར་གནས་པ་ཡིན་ཏེ། རང་གི་བུ་ཆུང་ངུ་དེ་དང་ལྷན་ཅིག་གནས་པའི་དོན་དུ་འདི་རྗེས་སུ་གནང་བ་ནི༌[^1836]གླེང་གཞི་དང་དོན་ལས་གཏོགས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2822]
ཅི་དགེ་སློང་མ་ཐམས་ཅད་ལས་མ༌[^1837]གཏོགས་པ་ཉིད་མ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་གནང་བ་ཐོབ་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བུ་ཆུང་ངུ་མ་ཡིན་པ་དང་གང་གིས་ལྷན་ཅིག་ཉལ་བའི་གནང་བ་ཐོབ་པར་གྱུར་པ་དེ་ལས་མ༌[^1838]གཏོགས་པ་ཉིད་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2823]
དེ་ལ་གནང་བ་དེ་སྦྱིན་པ་ཆོས་དང་མཐུན་པ་ཉིད་རིགས་སམ་ཞེ་ན། དེའི་ཕྱིར་དེ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ལ་དགེ་སློང་མའི་དགེ་འདུན་གྱིས་གནང་བ་སྦྱིན་པ་ལ་ནི་ཆོས་དང་མཐུན་པ་ཉིད་ཡིན་ཏེ། ངེས་པར་སྦྱིན་པ་དང་། ངེས་པར་ལེན་པ་དང་། ཡང་དག་པར་བསྒྲུབ་པ་དང་། ཚངས་པར་སྤྱད་པ༌[^1839]དང་། ཡོ་བྱད་དང་། རྩེ་བ་དང་། འཇོ་སྒེག་དང་། སྟན་གདིང་བ༌[^1840]དང་། བཟའ་བ་དང་། གོས་དང་། སེར་སྣ་བྱེད་པ་དང་། གནས་ཁང་ན་འདུག་པར་འགྲོ་བ་དང་། ངེས་པར་འབྱུང་བ་ལ་གཏོགས་པའི་འཇུག་པ་རྣམས་ལས་གཞན་པའི་ལྟུང་བྱེད་འབའ་ཞིག་ཏུ་འགྱུར་བ་བརྒྱ་རྩ་བརྒྱད་པ་དག་ནི་ཡུལ་དུ་གྱུར་པའི་སྤྱོད་པ་དེ་དག་ལ་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 2824]
ད་ནི་འདི་མན་ཆད་རྣམ་པར་བཤད་པར་བྱ་སྟེ། གང་ལ་བདག་ཉིད་ཀྱི་མ་ལོན་པ་འཇོག་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་རབ་ཏུ་འབྱིན་པ་དང་། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2825]
གནས་སྐབས་གང་ལ་ཞེ་ན། དེའི་ཕྱིར་ལོ་བཅུ་གཉིས་མ་ལོན་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2826]
གང་གིས་ཤེ་ན་དེའི་ཕྱིར་བདག་ཉིད་བསྙེན་པར་རྫོགས་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བདག་ཉིད་བསྙེན་པར་རྫོགས་ནས་ལོ་བཅུ་གཉིས་མ་ལོན་པར་རབ་ཏུ་འབྱིན་པ་དང་། བསྙེན་པར་རྫོགས་པར་བྱེད་དུ་འཇུག་པ་ལ་ལྟུང་བྱེད་འདི་རྣམ་པར་གཞག་གོ། །

[Block 2827]
མ་ལོན་པས་ཉེ་བར་འཇོག་པའི་ལྟུང་བྱེད་དོ། །

[Block 2828]
འཁོར་དང་འཁོར་མང་པོ་ཉེ་བར་གཞག་པའི་གནང་བ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི། འཁོར་ཉེ་བར་གཞག་པའི་གནང་བ་དང་། འཁོར་མང་པོ་ཉེ་བར་གཞག་པའི་གནང་བ་དགེ་སློང་མ་རྣམས་ཀྱིས་སྦྱིན་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2829]
འདིར་མེའི་སྒྲ་ནི་མང་པོ་ལས་ཏེ། དེ་བས་ན་འཁོར་མང་པོ་གཞན་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པ་མང་པོས་ཚོལ་བ་ཉིད་དོ། །

[Block 2830]
མེའི་ཆོས་རྣམས་གང་ཡིན་པ་དེ་དང་རྟོགས་པ༌[^1841]མང་པོ་ཉིད་ཀྱི་རྒྱུ་མཚན་གྱིས་འདིར་མེའི་སྒྲ་འདི་འཇུག་པ་ཡིན་ནོ། །

[Block 2831]
ཅི་དགེ་སློང་མ་ཐམས་ཅད་ལ་སྦྱིན་པར་བྱའམ༌[^1842]ཞེ་ན། དེའི༌[^1843]ཕྱིར་དེ་ཉེ་བར་འཇོག་ནུས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འཁོར་དེ་ཉེ་བར་འཇོག་པ་དང་འཇོག་ནུས་པའི་གནང་བ་སྦྱིན་པའོ། །

[Block 2832]
འདིར་ནུས་ཞེས་བྱ་བ་ནི་གཉིས་ཀ་ལ་ཡང་ནད་གཡོག་དང་འགྱོད་པ་བསལ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་གང་ཡིན་པ་དེ་སྔ་མ་ལ་གཏོགས་པར་བྱའོ། །

[Block 2833]
ཕྱི་མ་བསྒྲུབ་པའི་ཕྱིར་འབྱུང་བ་རྣམས་ཀྱི་ནུས་པའོ། །

[Block 2834]
འདིར་གཞུང་ནི་གང་གིས་འཁོར་ཉེ་བར་གཞག་པར་ནུས་པ་དེས་དགེ་འདུན་ལ་འཁོར་ཉེ་བར་གཞག་པའི་གནང་བ་ཐོབ་ནས་འཁོར་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དགེ་སློང་མ་མིང་འདི་ཞེས་བགྱི་བ་ལོ་བཅུ་གཉིས་ལོན་ལགས་ཏེ། འཁོར་ཉེ་བར་གཞག་པར་སྤྲོ་ནས་ཞེས་བྱ་བ་ཡང་སྔ་མ་དང་ཕྱི་མ་ལ་གང་ཞིག་དང་ལྡན་པ་དེས་འཁོར་མང་པོ་ཉེ་བར་གཞག་པའི་གནང་བ་གསོལ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 2835]
བདག་མིང་འདི་ཞེས་བྱ་བ་ལོ་བཅུ་གཉིས་ལོན་ལགས་ཏེ། འཁོར་མང་པོ་ཉེ་བར་གཞག་པ་སྤྲོ་ནས་འཁོར་མང་པོ་ཉེ་བར་གཞག་པའི་གནང་བ་གསོལ་ནས་བདག་མིང་འདི་ཞེས་བགྱི་བ་ལོ་བཅུ་གཉིས་ལོན་པ་འཁོར་མང་པོ་གཞག་པའི་དོན་དུ་སྤྲོ་བ་ཞེས་བྱ་བ་ཡང་ངོ་། །ཅི་ནུས་པ་ཐམས་ཅད་ལ་གནང་བ་དེ་སྦྱིན་པར་བྱའམ་ཞེ་ན། དེའི་ཕྱིར་བསྙེན་པར་རྫོགས་ནས་ལོ་བཅུ་གཉིས་ལོན་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ལུང་ནི་གནང་བ་སློང་བའི་སྔགས་རྣམས་ལ་བསྙེན་པར་རྫོགས་ནས་ལོ་བཅུ་གཉིས་ལོན་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 2836]
བསླབ་པའི་གཞི་སྔ་མ་བཅས་པ་ལ་ཡང་འདི་ཐོབ་པའོ། །

[Block 2837]
གནས་སྦྱིན་པ་ལ་ཡང་ལོ་བཅུའི་གནས་ལ་ཡང༌[^1844]ལོ་བཅུ་གཉིས་ལོན་པ་ཉིད་དགེ་སློང་མ་རྣམས་ལ་འདི་ལས་སྐྱེས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2838]
གཞན་གྱིས་གསོལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མི་ནུས་པ་ལོ་བཅུ་གཉིས་མ་ལོན་པས་གནང་བ་འདི་དག་གསོལ་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2839]
འདིར་ཡང་ཚིག་འདི་དག་ཉིད་མདོ་ལས་རྟོགས་པར་བྱའོ། །

[Block 2840]
གང་ཡང་ནུས་པ་ཞེས་བྱ་བ་དེ་འདིར་དངོས་ཀྱི་ཚིག་སྟེ། དོན་གཞན་དང་གཞན་ལས་ཐོབ་པར་བྱེད་པའོ། །
--- END BLOCKS ---
