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
[Block 4026]
ཚེ་དང་ལྡན་པས་ཕྱོགས་འདི་ན་ལྡེ་མིག་སྦས་པ་བལྟས་ནས་དབྱུང་བར་བྱའོ། །

[Block 4027]
གསོ་སྦྱོང་གི་གཞི་ལས་ཞི་གནས་ཀྱི་གསོ་སྦྱོང་གི་སྐབས་སོ། །

[Block 4028]
གསོ་སྦྱོང་གི་གནས་ལ་བློ་མཐུན་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ནས། གནས་ཇི་ལྟ་བུར༌[^2791]བློ་མཐུན་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གནས་ཐམས་ཅད་གྲུབ་པའམ། བྱས་པའམ་ཟིན་པ་ལའོ་ཞེས་བྱ་བ༌[^2792]སྨོས་ཏེ། གནས་གང་ལ་ཐམས་ཅད་གྲུབ་པའམ། ཐམས་ཅད་བྱས༌[^2793]པའམ། ཐམས་ཅད་ཟིན་པ་ཡོད་པ་དེ་ནི་གང་ལ་ཞེས་བྱ་བ་འདིས་བསྡུས་པའོ། །

[Block 4029]
དེ་ལ་གྲུབ་པ་ཞེས་བྱ་བ་ནི་འཆགས་པའི་བསྐལ་པ༌[^2794]ཚེ་རང་གྲུབ་པའམ། གཏིབ་ཆད་པ་ལ་སོགས་པས་རང་གྲུབ་པ་སྟེ། དཔེར་ན་རིའི་བྱ་སྐྱིབས་ལ་སོགས་པ་ལྟ་བུ་གཞན་གྱིས་བྱས་པ་ལ་མི་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 4030]
བྱས་པ་ཞེས་བྱ་བ་ནི་འབད་པ་ལ་བརྟེན་ནས། བསྒྲུབ་པ་གང་ཡིན་པའོ། །

[Block 4031]
ཟིན་པ་ཞེས་བྱ་བ་ནི། བྱ་བ་བྱེད་པའི་གནས་ལ་སོགས་པར་རུང་བ་སྟེ། གྲུབ་པ་དང་བྱས་པ་དང་ཟིན་པ་ལའོ་ཞེས༌[^2795]བྱ་བ་འདི་ཡོངས་སུ་རྫོགས་པ་དེ་བས་ན་གྲུབ་པ་ལ་སོགས་པ་ནི་མིང་གི་རྣམ་གྲངས་ཉིད་དོ། །

[Block 4032]
ཡོངས་སུ་མ་རྫོགས་པ་ལ་ཡང་འདི་དག་གི་སྒྲ་འཇུག་པར་འགྱུར་བ་ཡིན་ཏེ། དེའི་ཕྱིར་བྱེ་བྲག་འདི་ཡིན་ནོ། །

[Block 4033]
ཕྱི་རོལ་ཉེ༌[^2796]འཁོར་འདོམ་གང་དང་ལྡན་པའོ་ཞེས་བྱ་བ་ནི། དགེ་འདུན་ལས་ཕྱི་རོལ་དུ་གྱུར་པའི་ཉེན་ཀོར་དུ་འདོམ་གང་ཙམ་དང་བཅས་པ་གང་ཡིན་པ་དེ་ནི་ཕྱི་རོལ་ཉེན་ཀོར་འདོམ་གང་དང་ལྡན་པ་ཞེས་བྱ་བའོ།

[Block 4034]
[^2797] །ཉེན་ཀོར་འདོམ་གང་དང་བཅས་པ་ཞེས་བྱ་བ་ནི། མཐའི་སྒྲ་ནི་འདིར་དྲང་སྲོང་གིས་གསུངས་པ་ལས་འདོན་པ་ཡིན་ཏེ། དེའི་དོན་ནི་བར་དང་བཅས་པར་གྱུར་པ་དང་ལྷན་ཅིག་ཏུ་དེ་ཙམ་པའི་ཕྱི་རོལ་དུ་གྱུར་པའི་ཉེ་འཁོར་ཞེས་གསུངས་པ་ཡིན་ནོ། །ཅི་མི་འདོད་བཞིན་དུ་ཡང་བློ་མཐུན་པར་བྱ་བའམ་ཞེ་ན། མ་ཡིན་ཏེ་དེའི་ཕྱིར་དགེ་འདུན་འདོད་ནའོ། །

[Block 4035]
ལས་གཞན་གྱི་གནས་ཀྱང་དེ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གསོ་སྦྱོང་གི་གནས་ཞེས་སྨོས་པས་འདིར་ལས་གཞན་དེར་མི་བྱ་བའམ་སྙམ་དུ་སེམས་པ་རྣམས་ཀྱི༌[^2798]དོགས་པ་བསལ་བའི་ཕྱིར་འདིའོ། །

[Block 4036]
འདིར་གསོ་སྦྱོང་ཞེས་སྨོས་པ་ནི། དཔེ་ཙམ་དུ་ཟད་དེ་དེ༌[^2799]བས་ན་ལས་རྣམས་ཐ་དད་པར་གནས་པ་ཉིད་ཅེས་བྱ་བ་གསོ་སྦྱོང་གི་གཞི་ལས་དེ་བཅས་པའི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 4037]
མཚམས་གཅད་པར༌[^2800]བྱའོ། །

[Block 4038]
དཔག་ཚད་ཕྱེད་དང་གསུམ་གྱི་མཐའ་ཚུན་ཆད་དུའོ་ཞེས་བྱ་བ་ལ། ཕྱེད་ཅེས་བྱ་བ་ནི་ཇི་སྲིད་དང་ལྷན་དུ་སྦྱར་བ་འདི་སྟེ། དེ་སྲིད་དཔག་ཚད་ཕྱེད་དང་གསུམ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4039]
ཕྱོགས་ཕྱོགས་སུ་ཕ་བོང་དང་། རྩིག་པ་དང་། [^2801]ཀ་བ་དང་། ཤིང་ལྗོན་པ་དང་། ར་བ་དང་། བྱ་སྐྱིབས་དང་། ལམ་པོ་ཆེ་དང་། ཁྲོན་པ་ལ་སོགས་པ་དེ་ཤེས་པའི་དགེ་སློང་རྣམས་ཀྱིས་བརྟགས་ནས་དགེ་འདུན་གྱི་མདུན་དུ་མཚན་མ་བརྟན་པོ་བརྗོད་དེ་ལས་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཤེས་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་ནི་ཡུལ་དེ་ན་གནས་པའམ། གཉུག་མར་གནས་པ་རྣམས་ཀྱིའོ། །

[Block 4040]
གནས་པ་ཞེས་བྱ་བ་ནི་གང་དག་གནས་པ་དེའམ། ཕྱི་རོལ་དུ་མངོན་པར་ཤེས་པ་མ་གྲུབ་པ་ལས་སྔར་གནས་པའོ། །

[Block 4041]
སྔར་ཕ་བོང་ལ་སོགས་པ་མཚན་མ་བརྟན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲས་ནི་འཕངས་པ་རྣམ་པར་བཅད་པའོ། །

[Block 4042]
རྗེས་སུ་འཇུག་པར་བྱེད་ཙམ་ལ་བརྟན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲས་ནི་བརྗོད་པའོ། །

[Block 4043]
འདིས་རྣམ་པར་བཅད་ནས་ཡུན་རིང་དུ་གནས་པ་བརྗོད་པ་ལ་ཡིན་ཏེ། དོན་ལས་ཇི་ལྟར་ཡུན་རིང་དུ་ཡོངས་སུ་ཤེས་པ་བསྒྲུབ་པ་དེ་ལྟར་གོང་དུ་ཡང་མཚན་མ༌[^2802]གཞན་ངེས་པར་ཞུགས་པ༌[^2803]མངོན་པར་འདུ་བྱས་པས་བྱའོ་ཞེས་བྱ་བ་སྨོས་པ་དེའི་ཕྱིར། གང་ཞིག་གང་དུ་གཞན་སྒྲུབ་པར་འགྱུར་པ་དེ་བས་ན་རེ་ཞིག་འབྱུང་བར་གྱུར་ཅིག་སྙམ་དུ་བྱེད་པ་དེར་ན་པར་སྒྲུབ་པ་ལ་མཚན་མ་ཞེས་འབྱུང་བ་ཡིན་ཏེ། ཕ་བོང་ངམ་ཕུར་པ་གདབ་པ་ལ་སོགས་པ་བྱའོ་ཞེས་བྱ་བ༌[^2804]གསུངས་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 4044]
དེར་གནང་བ་བྱས་ན་ཆོས་གོས་དག་དང་བྲལ་བར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་མཚམས་ཀྱི་ནང་དུའོ། །

[Block 4045]
གལ་ཏེ་ཆོས་གོས་དག་དང་མི་འབྲལ་བའི་གནང་བ་བྱས་པར་གྱུར་ན་འདིར་ཆོས་གོས་དག་དང་འབྲལ་བར་མི་འགྱུར་བ་ཡིན་ནོ། །

[Block 4046]
མཚམས་བཅད་པ་ཙམ་ཆོས་གོས་དང་མི་འབྲལ་བར་གྱུར་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4047]
དེ་བྱའོ་ཞེས་བྱ་བ་ནི། ཆོས་གོས་དང་བྲལ་བར་མི་འགྱུར་བའི་གནང་བ་དེ་བྱ་སྟེ། ཆོས་གོས་དག་དང་མི་འབྲལ་བའི་གནང་བ་དེ་བྱས་པར་འགྱུར་རོ། །

[Block 4048]
དེ་ལ་བྱེད་པ་གནང་བ་མ་ཡིན་ནོ་སྙམ་དུ་འགའ་ཞིག་སེམས་སོ་ཞེས་སྨོས་སོ། །

[Block 4049]
ཐམས་ཅད་ཀྱི་ཆེད་དུ་དཀྱིལ་འཁོར་བར་བློ་མཐུན་པར་བྱའོ་ཞེས་བྱ་བ་ནི། ལས་ཐམས་ཅད་ལ་བརྟེན་ནས་གསོ་སྦྱོང་གི་རྗེས་ལ་དཀྱིལ་འཁོར༌[^2805]བློ་མཐུན་པར་བྱའོ། །

[Block 4050]
སྔ་མ་བག་ཡངས་སུ་མ་བྱས་པ་བཅད་པ་གཞན་མི་འཆགས་སོ་ཞེས་བྱ་བ་སྔར་གྱི་མཚམས་བག་ཡངས་སུ་མ་བྱས་པ༌[^2806]ལ་མཆོམས་གཞན་མི་འཆགས་སོ། །

[Block 4051]
དེ་ལྟ་བས་ན་དཀྱིལ་འཁོར་བའི་མཚམས༌[^2807]སུ་བློ་མཐུན་པར་མ་བྱས་པར་མཚམས་བཅད་པའི་བློས་མཐུན་པར་བྱེད་འདོད་པ་ལ་མཚམས་དགྲོལ་བར་བྱའོ། །

[Block 4052]
འདི་ནི་རིགས་པ༌[^2808]མ་ཡིན་ནོ་སྙམ་དུ་ཤེས་པར་མི་བྱའོ། །

[Block 4053]
དེའི་ཕྱིར་མཚམས་དག་དགྲོལ་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཚམས་པོ་ཆེའི་སྟེང་དུ་དཀྱིལ་འཁོར་བ་མི་འཆགས་པས་དེ་དགྲོལ་ནས་བྱའོ། །

[Block 4054]
ཚིག་གཅིག་གིས་མཚམས་གཉིས་བཅད་པ་དང་དགྲོལ་དུ་རུང་ངོ་ཞེས་བྱ་བ་ནི། མཚམས་གཉིས་པོ་དག་ལ་ཚིག་གཅིག༌[^2809]གིས་བཅད་པའམ་དགྲོལ་བར་རིགས་པ་ཡིན་ཏེ། མཚམས་གཉིས་ཀར་དགེ་འདུན་བཀོད་ནས་ལས་བྱེད་པའི་དགེ་སློང་གིས་མཚམས་གཉིས་ཀར་ཤིང་ངམ་དབྱུག་པའམ་རེ་ལྡེས་མནན་ནས་གསོལ་བ༌[^2810]བྱ་སྟེ་ལས་བྱའོ་ཞེས་གསུངས་པ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 4055]
མཚམས་མ་བཅད་པའི་གནས་སུ་ནི་ལས་ལ་རྩིག་པ་མཚམས་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། མཚམས་མ་བཅད་པའི་གནས་གང་ཡིན་པ་དེར་ལས་བྱ་བའི་ཡུལ་ལ་གཙུག་ལག་ཁང་གི་རྩིག་པ༌[^2811]ཉིད་མཚམས་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4056]
འདིར་ཆོས་གོས་དང་འབྲལ་བའི་མཚམས་བསལ་བའི་ཕྱིར་ལ་ཞེས་སྨོས་པ་ནི། དེ་ལ་ཆོ་ག་ཡིན་ནོ། །

[Block 4057]
དབྱར་གྱི༌[^2812]མཚམས་བཅད་པ་ལ་ཁས་བླངས་པའི་རྣམ་པ་གང་ཡིན་པ་དེ་ནི་འདིར་མཚམས་སོ། །

[Block 4058]
ཁས་བླངས་པ་ཡང་ལས་ཏེ་གང་གི་ཕྱིར་འདིར་ལས་ཀྱི་གཞིར་སྤྱིར་བསྟན་པ་བཟུང་བ་ནི་མ་ཡིན་ཏེ། འོན་ཀྱང་ཐམས་ཅད་ངེས་པར་རྟོགས་པའི་རྗེས་སུ་བསྒྲུབ་པ་ལའོ། །

[Block 4059]
དེ་ལྟར་ཡང་མཚམས་འདིར་རྙེད་པ་བགོ་བ་དང་ཤི་བའི་ཡོ་བྱད་བྱིན་གྱིས་བརླབས་པ༌[^2813]ཡང་དེ་ལྟ་བུའི་རྣམ་པ་ལས་འབྱུང་བའོ། །

[Block 4060]
དེ་ལྟར་ཡང་ཚེ་དང་ལྡན་པ་ཉེ༌[^2814]དགའ་གཙུག་ལག་ཁང་ནས་ཐག་རིང་པོ་ན་འདུག་པས་ཁོ་བོ་མཚམས་སུ་གཏོགས་པས་རྙེད་པ་དབང་ངོ་ཞེས་བྱ་བ་སྨྲས་པ་ཡིན་ནོ། །

[Block 4061]
ནང་དུ་འཚེད་པ་དང་སྨིག་པ་དག་ལ་སྒྲུབ་པ་གང་ཡིན་ཞེ་ན། གནས་སུ་འདི་དག་ལ་མི་མཐུན་པ་ཉིད་དོ། །

[Block 4062]
དེ་ལྟ་བས་ན་ཇི་སྲིད་གནས་ཀྱི་བློ་ཡོད་པ་དེ་སྲིད་དུ་ཞེས་བྱའོ། །

[Block 4063]
དེ་ཡང་ཕྱི༌[^2815]རོལ་འདོམ་གང་དང་བཅས་པའོ། །

[Block 4064]
གཞི་མེད་པའི་གནས་སུ་ཇི་ལྟར་བྱ་ཞེ་ན། ཇི་སྲིད་དུ་དེར༌[^2816]ལྷག་པར་གནས་པའི་ངོ་བོས་སྒྲུབ་པར༌[^2817]བྱེད་པ་དེ་སྲིད༌[^2818]སྤང་བར་བྱའོ། །

[Block 4065]
དགེ་སློང་གྲོང་དག་ཏུ་དགེ་སློང་རྣམས་ཀྱི༌[^2819]དོན་དུ་ཉེ་བར་མི༌[^2820]མཁོ་བའི་གནས་རྣམས་གང་ཡིན་པར་བྱེད་པ་དེ་རྣམས་ལ༌[^2821]ཇི་ལྟར་བྱ་ཞེ་ན། གང་ཞིག་དེར་དགེ་སློང་རྣམས་ཀྱི་གནས་དོན་དུ་དེ་ཉེ་འཁོར་དང་བཅས་པ་སྤང་བར་བྱའོ། །
--- END BLOCKS ---
