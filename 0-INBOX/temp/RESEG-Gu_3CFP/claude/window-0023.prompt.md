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
[Block 806]
ཚིག་ལེགས་པར་སྦྱར་བ་ནི་ལེགས་པར་སྦྱར་བའི་བརྗོད་པ་སྟེ། ཕན་ཡོན་ནོ། །

[Block 807]
དབྱངས་སམ་ཡི་གེ་ཉམས་པ་དང་ལྡན་པའི་སྔགས་ཀྱིས་ནི། ཉམས་པས་དོན་མི་འགྲུབ་སྟེ། ངག་གི་རྡོ་རྗེ་དེས་སྒྲུབ་པ༌[^606]པོ་ཉིད་ཉམས་པར་བྱེད་དོ། །

[Block 808]
དེ་སྟོན་པའི་རྣམ་པ་ནི་ལེགས་པར་སྦྱར་བའི་ཐབས་ཀྱིས་ཏེ། འདི་ལྟ་བུའི་ཕན་ཡོན་སྟོན་པའི་རྣམ་པའོ། །

[Block 809]
ནད་ལ་མཁས་པ་སྟོན་པའི་རྣམ་པ་དང་ཞེས་བྱ་བ་ལ། ནད་འདིའི་མིང་ནི་འདིའོ་ཞེས་བྱ་བར་ནད་དེ་ལ་མཁས་པའོ། །

[Block 810]
ནད་ཅི་ལས་བྱུང་བ་ལ་མཁས་པ་སྟོན་པའི་རྣམ་པ་དང་ཞེས་བྱ་བ་ལ། འདི་ལས་ཀུན་དུ་བྱུང་བས༌[^607]ན་ནད་ཀུན་དུ་སློང་བ་ནི་ནད་ཅི་ལས་བྱུང་བའོ། །

[Block 811]
དེ་ལ་མཁས་པ་སྟེ། མི་འཕྲོད་པ་འདི་ལས་ནད་འདི་བྱུང༌[^608]ངོ་ཞེས་བྱ་བར་ཤེས་པའོ། །

[Block 812]
ནད་བྱུང་བ༌[^609]བསལ་བ༌[^610]ལ་མཁས་པ་སྟོན་པའི་རྣམ་པ་དང་ཞེས་བྱ་བ་ལ། འདིར་སེལ་བར་བྱེད་པས་ན་བསལ་བ་སྟེ། ནད་བསལ་བའོ། །

[Block 813]
དེ་ལ་མཁས་པ་ནི་སྨན་འདིས་སོས་པར་བྱེད་དོ་ཞེས་བྱ་བར་ཤེས་པའོ། །

[Block 814]
ཡང་ན་བསལ་བར་བྱ་བ་ནི་བསལ་བ་སྟེ། ཉེ་བར་ཞི་བར་བྱ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 815]
ནད་ཉེ་བར་ཞི་བར་བྱ་བ་ཡིན་པས། ནད་རབ་ཏུ་ཞི་བ་ཉིད་དོ། །

[Block 816]
རང་རང་གི་བཟོ་དང་ལས་ཀྱི་གནས་གྲུབ་པའི་འབྲས་བུ་ཡོངས་སུ་གྲུབ་པ་སྟོན་པའི་རྣམ་པ་ཞེས་བྱ་བ་ལ། རང་རང་གི་བཟོ་དང་ལས་ཀྱི་གནས་སྒྲུབ་པ་སྟེ། འབྲས་བུ་འདི་ཡོངས་སུ་གྲུབ་པ༌[^611]ནི་འདི་ལས་ཡོངས་སུ་སྒྲུབ༌[^612]པའོ། །ཞེས་སྟོན་པའི་རྣམ་པའོ། །

[Block 817]
ཕྱིན་ཅི་མ་ལོག་པའི་རྒྱུ་རྣམ་པར་གཞག་པ་དང་། རྒྱུ་ཐམས་ཅད་བསྡུས་པ་ཞེས་བྱ་བ་ལ། རྒྱུ་རྣམས་ཇི་ལྟར་ཡོད་པ་ཉིད་དང་། ཇི་སྙེད་ཡོད་པ་ཉིད་དེ་སེམས་ཅན་གྱི་འཇིག་རྟེན་ལས་བརྩམས་ནས་ཀུན་ནས་ཉོན་མོངས་པའམ་རྣམ་པར་བྱང་བ་དག་གོ། །

[Block 818]
འཇིག་རྟེན་པའི་ཡང་དེ་དག་ཏུ་ལོ་ཐོག་ལ་སོགས་པ༌[^613]སྣོད་ཀྱི་འཇིག་རྟེན་གྱི་དབང་དུ་བྱས་ནས། ལྷན་ཅིག་བྱེད་པས་དེ་ཀུན་ནས་བསླང་བའི་རྩི་ལ་སོགས་པ་དག་གོ། །

[Block 819]
མིང་དང་ཞེས་བྱ་བ་ལ་སྐྱེས་པ༌[^614]དང་རྟ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 820]
མིང༌[^615]སྔོན་དུ་འགྲོ་བའི་འདུ་ཤེས་ཞེས་བྱ་བ་དང་། འདུ་ཤེས་སྔོན་དུ་འགྲོ་བའི་བརྗོད་པ་ཞེས་བྱ་བ་ལ། འདི་ནི་སྐྱེས་པ།[^616] འདི་ནི་རྟ་ཞེས་བྱ་བའི་གཞན་གོ་བར་བྱེད་པའི་ཐ་སྙད་དོ། །

[Block 821]
ཆོས་དེ་དང་དེ༌[^617]དག་གི་རྗེས་སུ་ཐ་སྙད་འདོགས་པའི་རྒྱུ་སྟེ། རྗེས་སུ་ནི་ཉེ་བར་བསྒྱུར༌[^618]བའམ། གོམས་པ་ལས༌[^619]རྗེས་སུ་ཐ་སྙད་བྱེད་པ་སྟེ། གོམས་པ་ཉིད་ལས་ཐ་སྙད་དུ་བྱེད་པའོ། །

[Block 822]
ལག་པ་ལ༌[^620]ལྟོས་ནས་ནི་ལེན་པ་ཡོད་པ་ཉིད་དོ། །

[Block 823]
བཀྲེས་པ་དང་སྐོམ་པ་ལ༌[^621]ལྟོས་ནས་ནི་ཟས་དང་སྐོམ་ལེན་ཏོ། །

[Block 824]
རང་གི་འབྲས་བུ་ཐ་མའི་བར་ཏེ། རང་གི་འབྲས་བུ་ཐ་མའི་བར་དུའོ། །

[Block 825]
དེ་ལས་གཞན་པའི་རྐྱེན་ནི་ཆུ་དང་ས་ལ་སོགས་པའི་རྐྱེན་ནོ། །

[Block 826]
རང་གི་འབྲས་བུ༌[^622]ནི་མྱུ་གུའོ། །

[Block 827]
གང་གི་རྗེས་ཐོགས་ལ་གང་བྱུང་བ་ནི་འབྲས་བུ་སྟེ། དེ་ནི་ཡང་ས་བོན་ལས་འགྲུབ་པའི་འབྲས་བུ་སྟེ། མྱུ་གུ་ནི་ས་བོན་གྱིས་འཕངས་པ་ཞེས་བྱ་བ་སྟེ། འཕངས་པའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 828]
རྣམ་པ་སྣ་ཚོགས་རྣམ་པ་ཐ་དད་པ་ཞེས་བྱ་བ་ལ། སྣ་ཚོགས་ནི་ཐ་དད་པར༌[^623]རིས་མི་མཐུན་པ་རིང་བའི་རིགས་ཉིད་དོ། །

[Block 829]
ཐ་དད་པའི་རྒྱུ་ཉིད་ནི་རྣམ་པ་ཐ་དད་ཅིང་རིགས་ཐ་དད་པ་ཉིད་དོ། །

[Block 830]
སོ་སོར་ངེས་པ་ཞེས་བྱ་བ་ནི་ཡུན༌[^624]རིང་བ་ཉིད་དམ། ལྟོས་པ་མེད་པའོ། །

[Block 831]
ལྟོས་པ་ཡིན་པས་ལྟོས་པ་སྟེ། དེ་ཉིད་རྒྱུའོ། །

[Block 832]
འདིས་ཡོངས་སུ་འཛིན་པས་ན་ཡོངས་སུ་འཛིན༌[^625]ལ། དེ་ཉིད་ནི་རྒྱུའོ། །

[Block 833]
འགྲུབ་པའི་རྒྱུ་ཞེས་བྱ་བ་ལ། །འདི་མངོན་པར་གྲུབ་པར༌[^626]བྱ་བས་ན་མངོན་པར་འགྲུབ་པ་སྟེ། དེ་ཉིད་ནི་རྒྱུའོ། །

[Block 834]
ཡང་ན་མངོན་པར་འགྲུབ་པར་བྱེད་པ་ནི། མངོན་པར་འགྲུབ་པ་ཡིན་ལ། དེའི་རྒྱུའོ། །

[Block 835]
འདྲེན་པར་བྱེད་པས་ནི་འདྲེན་པ་སྟེ། དེ་ཉིད་ནི་རྒྱུའོ། །

[Block 836]
ལྷག་པར་བསྡམས་ཤིང་མཆོག་ཏུ་དགའ་བས་བསྡམས་པས་སོ་སོར་ངེས་པ་སྟེ། སོ་སོར་ངེས་པའི་རྒྱུ་ནི་སོ་སོར་ངེས་པའི་རྒྱུའོ། །

[Block 837]
ལྷན་ཅིག་བྱེད་པའི་ངང་ཚུལ་གང་ལ་ཡོད་པ་དེ་ནི་ལྷན་ཅིག་བྱེད་པ་སྟེ། ལྷན་ཅིག་ཏུ་བྱེད་པའི་རྒྱུ་ནི་ལྷན་ཅིག་བྱེད་པའི་རྒྱུའོ། །

[Block 838]
འདིས་མི་མཐུན་པར་བྱེད་པས་ན་མི་མཐུན་པ་སྟེ། མི་མཐུན་པ་དེ་ཉིད་ནི་རྒྱུ་སྟེ། མི་མཐུན་པའི་རྒྱུའོ། །

[Block 839]
ཚིག་གི་མི་མཐུན་པ་དང་། དེ་བཞིན་དུ་རིགས་པ་དང་མི་མཐུན་པ་དང་། ལྷན་ཅིག་ཏུ༌[^627]མི་གནས་པའི་མཚན་ཉིད་ཀྱི་མི་མཐུན་པ་དང་། མི་འཕྲོད་པའི་མི་མཐུན་པ་དང་ཞེས་བྱ་བ་ལ། རབ་ཏུ་མི་མཐུན་པ་དང་། ཤིན་ཏུ་རབ་ཏུ་མི་མཐུན་པ་དང་། ཤིན་ཏུ་ཆེར་མི་མཐུན་པ་དང་། རྣམ་པར་མི་མཐུན་པ་དང་། རྣམ་པར་མི་མཐུན་པའི་མཚན་ཉིད་ཅན་གྱི་འགལ་བ་ནི་རབ་ཏུ་རྣམ་པར་མི་མཐུན་པའོ། །

[Block 840]
མི་མཐུན་པའི་ཕྱོགས་དང་གཉེན་པོའི་ཕྱོགས་ཀྱི་མི་མཐུན་པ་ཞེས་བྱ་བ་ལ། རྣམ་པར་སྨད་པས་ངན་པའི་ཕྱོགས་ནི་མི་མཐུན་པའི་ཕྱོགས་སོ། །

[Block 841]
གཉེན་པོའི་ཕྱོགས་ཞེས་བྱ་བ་ལ། འདིར་རབ་ཏུ་མངོན་པར་ཕྱོགས་ནས་ཡང་དག་པར་འབྱུང་བའམ། ཡང་དག་པ་ལ་མངོན་དུ་ཕྱོགས་པའི་ཕྱོགས་ནི་གཉེན་པོའི་ཕྱོགས་སོ། །

[Block 842]
གཉེན་པོའི་ཕྱོགས་དང་མི་མཐུན་པའི་ཕྱོགས་ནི་གཉེན་པོའི་ཕྱོགས་དང་མི་མཐུན་པའི༌[^628]ཕྱོགས་ཏེ། དེའི་མཚན་ཉིད་ཅན་གྱི་མི་མཐུན་པ་ནི་མི་མཐུན་པ་དང་གཉེན་པོའི་ཕྱོགས་ཀྱི་མི་མཐུན་པའོ། །

[Block 843]
སྐབས་འབྱེད་པ་ནི་ཡུལ་གྱི་ཆ་ནི་སྐབས་ཡིན་ལ། དེ་སྦྱིན་པ་སྟེ། སྔ་མ་སྐྱེས་པ་རྣམས་ཀྱི་སྐབས་སྦྱིན་པ་ནི་སྔ་མ་སྐྱེས་པ་རྣམས་ཀྱི༌[^629]སྐབས་འབྱེད་པ་སྟེ། དེས་ཡོངས་སུ་ཟིན་པའོ། །

[Block 844]
འབྱུང་བར་འགྱུར་བ་ནི་རིགས་མི་གཅིག་པའི་སེམས་བསྐྱེད༌[^630]པའོ། །

[Block 845]
འཇུག་པར་འགྱུར་བ་ནི་རྒྱུན་དང་འདྲ་བའི་སེམས་འབྱུང་བའོ། །
--- END BLOCKS ---
