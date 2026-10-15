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

[Block 846]
གང་དག་གིས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། འཇིག་རྟེན་ན་འབྲུ་ཁོ་ན་ངེས་པར་གཟུང་བ་ནི་འཇིག་རྟེན་གྱི་དངོས་པོ་དཔག་ཏུ་མེད་པ་ཡོད་པ་ཡིན་ན་ཡང་ཉེ་བར་མཚོན་པར་བསྟན་པའི་དོན་ཏོ། །

[Block 847]
ཀུན་ནས་ཉོན་མོངས་པ་དང་། རྣམ་པར་བྱང་བའི་དབང་དུ་བྱས་ནས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཐམས་ཅད་ཅེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཡུལ་གྱི་རོ་མྱང་བ་ལ་ལྟོས་ནས་སྲིད་པའི་ཡན་ལག་ཅེས་བྱ་བའི་བར་ཏེ། ཀུན་ནས་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱི་རོ་མྱང་བའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 848]
ཚེ་འདི་ལ་སྐྱེས་ཤིང་བྱུང་བའི་ཞེས་བྱ་བ་དང་། མཐོང་བའི་ཆོས་རྣམས་ཀྱི་ས་བོན་ཞེས་བྱ་བ་དང་། སྐྱེ་བ་གཞན་གྱི་ཞེས་བྱ་བ་ལ།[^631] སྐྱེས་ནས་མྱོང་བར་འགྱུར་བའམ། ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བའི་མ་རིག་པ་ལ་སོགས་པའོ། །

[Block 849]
རང་རང་གི་ས་བོན་ཞེས་བྱ་བ་ལ། ཀུན་གཞིའི༌[^632]རྣམ་པར་ཤེས་པའི་གནས་དང་། མ་རིག་པའི་ས་བོན་ལས་མ་རིག་པ་ལ་སོགས་པ་མཐོང་བའི་ཆོས་བསྒྲུབ་པའི༌[^633]རྒྱུ་ཉིད་དོ། །

[Block 850]
དེ་ལས་གཞན་པ་མ་རིག་པ་ལ་སོགས་པ་སྲིད་པའི་མཐར་ཐུག་པ་ཞེས་བྱ་བ་ལ། མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད། འདུ་བྱེད་ཀྱི་རྐྱེན་གྱིས༌[^634]རྣམ་པར་ཤེས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་རིམ་གྱིས་སོ། །

[Block 851]
རང་གི་ས་བོན་རྣམས་དང་བཅས་པ་ཞེས་བྱ་བ་ནི་ས་བོན་གང་ཡིན་པ་ཀུན་གཞིའི༌[^635]རྣམ་པར་ཤེས་པ་དང་། སྲིད་པའི་ཡན་ལག་གང་ཡིན་པ་དང་། མཐོང་བའི་ཆོས་ལ་མ་རིག་པ་ལ་སོགས་པ་འབྱུང་བའོ། །

[Block 852]
མེད་པ་ཞེས་བྱ་བ་ནི་ཕྱོགས་གཅིག་མ་ཚང་བའོ། །

[Block 853]
བྲལ་བ་ཉིད་ཅེས་བྱ་བ་ནི་ཐམས་ཅད་ནས་མེད་པ་ཉིད་དོ། །

[Block 854]
ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས་དེ་ལྟར་བསྟན་ནས། རྣམ་པར་བྱང་བའི་ཕྱོགས་ཞེས་བྱ་བ་ལ། དྲན་པ་ཉེ་བར་གཞག་པ་ལ་སོགས་པའི་ཕྱོགས་ཏེ། འགོག་པ་མྱ་ངན་ལས་འདས་པ་ཞེས་བྱ་བ་ལ། མ་རིག་པ་འགགས་པས་འདུ་བྱེད་འགག༌[^636]ཅེས་བྱ་བ་ནས། སྐྱེ་བ་འགགས་པས་རྒ་ཤི་འགག་ཅེས་བྱ་བའི་བར་དུའོ། །

[Block 855]
འདུ་བྱེད་ཀྱི་ཉེས་དམིགས་ལ་ལྟོས་ནས་ཞེས་བྱ་བ་ནི། ཐམས་ཅད་ཀྱི་ཉེས་དམིགས་མཐོང་བ་ནི་རྣམ་པར་བྱང་བའི་རྒྱུ་ཡིན་པའི་ཕྱིར་དེའི་ཞེས་བྱ་བ་སྨོས་པ་ཡིན་ནོ། །

[Block 856]
གང་ཟག་རིགས་ལ་གནས་པའི་ཞེས་བྱ་བ་ལ་རིགས་ལ་གནས་པ་ནི་རིགས་ཀྱིས་བསྡུས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། རིགས་ཞེས་བྱ་བ་ནི་ཐེག་པ་གསུམ་གྱིས༌[^637]མྱ་ངན་ལས་འདའ་བའི༌[^638]ས་བོན་དེས་བསྡུས་པ་ཡིན་ཏེ། ས་བོན་དེས༌[^639]བྱང་ཆུབ་སེམས་དཔའ་དེའི་རྒྱུད་ལ་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ས་བོན་རྣམས་སྐྱེད་པར་བྱེད་དོ། །

[Block 857]
སྔོན་གྱི་ལས་དང་མཐུན་པར་ཕྱིས་འབྲས་བུའི་རྗེས་སུ་འཇུག་པ་ཞེས་བྱ་བ་ལ། འདི་ལྟ་སྟེ་སྲོག་གཅོད་པ་ཀུན་དུ་བསྟེན་པ༌[^640]དང་། མང་དུ་གོམས་པས་ངན་སོང་དུ་སྐྱེ་བ་ནི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་སྟེ། དེ་གལ་ཏེ་མིར་སྐྱེས་ན་ཡང་ཚེ་ཐུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ༌[^641]སོགས་པའོ། །

[Block 858]
དེ་ལྟར་དབང་པོ་ཉི་ཤུ་རྩ་གཉིས་པོ་ཐམས་ཅད་ཀྱི་སོ་སོའི་དབང་གིས་ཞེས་བྱ་བ་ལ། ཀུན་ནས་ཉོན་མོངས་པའི་བདག་པོ་ཚོར་བའི་དབང་པོ་ལྔ་པོ་རྣམས་དང་། འཇིག་རྟེན་པའི་རྣམ་པར་བྱང་བའི༌[^642]བདག་པོ་དད་པ་ལ་སོགས་པའི་དབང་པོ་ལྔ་པོ་རྣམས༌[^643]དང་། འཇིག་རྟེན་ལས་འདས་པའི་རྣམ་པར་བྱང་བའི་བདག་པོ་མི་ཤེས་པ་ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་ལ་སོགས་པ་གསུམ་པོ་དག་གོ། །

[Block 859]
ཁེངས་པའི་ཀུན་ནས་ཉོན་མོངས་པ་དང་བྲལ་བ་དང་། ཁྱད༌[^644]དུ་གསོད་པའི་ཀུན་ནས་ཉོན་མོངས་པ་དང་བྲལ་བ་དང་། ཞུམ་པའི་ཀུན་ནས་ཉོན་མོངས་པ་དང་བྲལ༌[^645]ཞེས་བྱ་བ་ལ། གསུམ་པོ་འདི་དག་མདོར་བསྡུ་ན་བདག་ཏུ་ང་རྒྱལ་མང་བས་བྱས་པ་ནི་ཁེངས་པའོ། །

[Block 860]
གཞན་དག་ལ་ཡང་ཡོད་པར་མི་འཛིན་པས་བྱས་པ་ནི་ཁྱད་དུ་གསོད་པའི་ཀུན་ནས་ཉོན་མོངས་པའོ། །

[Block 861]
བདག་ཉིད་ལ་བརྙས་པས་བྱས་པ་ནི་ཞུམ་པའི་ཀུན་ནས་ཉོན་མོངས་པའོ། །

[Block 862]
དུས་སུ་ཞེས་བྱ་བ༌[^646]ཇི་ལྟ་བུ་ཞེ་ན། སྨྲས་པ། རྗེས་སུ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 863]
ཇི་ལྟ་ཞེ་ན་བཀུར་སྟི་བྱེད་པ་དང༌[^647]ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 864]
ཐམས་ཅད་ལ་སྟོན་ཅིང་ཞེས་བྱ་བ་ལ། ཇི་ལྟ༌[^648]ཞེ་ན། རྒྱུན་མི་འཆད་པར་ཐམས་ཅད་སྟོན་པ་ཞེས་བྱ་བའོ།

[Block 865]
[^649] །ཇི་ལྟ༌[^650]ཞེ་ན། ཚིག་དང་ཡི་གེ་གོ་རིམ་བཞིན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 866]
ཇི་ལྟར་རྗེས་སུ་མཐུན་པའི་དོན་དང་བཅས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཇི་ལྟར་དགའ་བར་བྱེད་པ་ཡིན་ཞེ་ན།

[Block 867 [VERSE]]
དེ་བསྟན་པར་བྱ་བ་ལ་བསྟན་པས་སོ། །
ཇི་ལྟར་འདོད་པར་བྱེད་པ་ཡིན་ཞེ་ན།
དགོད་པར་བྱ་བ་རྣམས་སྐུལ༌[^651]ཞིང་བཀོད་པས་སོ། །

[Block 868]
ཇི་ལྟར་མགུ་བར་བྱེད་ཅེ་ན། གཟེངས༌[^652]བསྟོད་པར་བྱ་བ་རྣམས་གཟེངས༌[^653]བསྟོད་ནས་སོ། །

[Block 869]
ཇི་ལྟར་སྤྲོ་བར་བྱེད་པ་དང་། སྨ་མི་འབེབས་པ་ཡིན་ཞེ་ན། ཡང་དག་པར་དགའ་བར་བྱ་བ་རྣམས་ཡང་དག་པར་དགའ་བར་བྱེད་པས་སོ། ། ཇི་ལྟར་རིག་པ༌[^654]ཡིན་ཞེ་ན། མངོན་སུམ་ལ་སོགས་པས་སོ། །ཇི་ལྟར་འཚམ་པ་ཡིན་ཞེ་ན། བདེ་འགྲོར་འགྲོ་བ་དང་རྗེས་སུ་མཐུན༌[^655]པའོ། །ཇི་ལྟར་མ་འདྲེས་པ་ཡིན་ཞེ་ན། མ་འདྲེས་པར་གྱུར་ནས་ཀྱང་གོ་མི་དཀའ་ཞིང་མྱུར་དུ་འཇུག་པར་སླ་བའོ། །

[Block 870]
ཇི་ལྟར་ཆོས་དང་ལྡན་པ་ཡིན་ཞེ་ན། འཕགས་པའི་བདེན་པ་བཞི་དང་། རྗེས་སུ་མཐུན་པའོ། །ཇི་ལྟར་ན་འཁོར་བ༌[^656]ཇི་ལྟ་བ་ཡིན་ཞེ་ན། ཐམས་ཅད་ལ་འཚམ་པའོ། །ཇི་ལྟར་བྱམས་པའི་སེམས་ཡིན་ཞེ་ན། གནོད་པ་བྱེད་པ་ལ་སོགས་པ་ལ་ཡང་ངོ་། །ཇི་ལྟར་ཕན་པའི་སེམས་ཡིན་ཞེ་ན། ཉེས་པར་བྱེད༌[^657]པ་སྤྱོད་པ་ལའོ། །ཇི་ལྟར་སྙིང་བརྩེ་བའི་སེམས་ཡིན་ཞེ་ན། བདེ་བ་ཉིད་དང་སྡུག་བསྔལ་བ་ལ་སོགས་པ་ལའོ། །

[Block 871]
ཇི་ལྟར་བདག་ལ་མི་བསྟོད་ཅིང་གཞན་ལ་མི་སྨོད་པ་ཡིན་ཞེ་ན། ཕྲག་དོག་ལ་མི་གནས་པ་ལ་སོགས་པའོ། །ཇི་ལྟར་རྙེད་པ་དང་བཀུར་སྟི་ལ་མི་གནས་པ་ཡིན་ཞེ་ན། ཟང་ཟིང་མེད་པའི་སེམས་ལ་སོགས་པའོ། །

[Block 872]
ཆོས་གང་དག་ལུས་ལ་སོགས་པ་དག་ལ་བཀག་པ་དེ་དག་ཡོངས་སུ་སྤོང་བ་སྟེ། གང་དག་ལུས་ལ་སོགས་པ་ལ་མ་གནང་བ༌[^658]རབ་ཏུ་བཀག་པ་དེ་དག་གོ། །

[Block 873]
རྗེས་སུ་སྒྲུབ་པ་ནི་སྔར་ཐོབ་པ་ལ༌[^659]ཇི་ལྟ་བ་བཞིན་དུའོ། །

[Block 874]
གཅིག་པུ་དབེན་པར་སོང་སྟེ་ཞེས་བྱ་བ་ནི་དབེན་པའི་གནས་སུ་སོང་བའོ། །

[Block 875]
ཐོག་མ་ཁོ་ནར་བསམ་པར་བྱ་བ་མ་ཡིན་པའི་གནས་རྣམས་སྤངས་ནས། ཆོས་རྣམས་བསམ་པ་བརྩོན་པར༌[^660]བྱེད་དེ་ཞེས་བྱ་བ་ལ། བསམ་པ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་མཐོང་ཞིང་ཆུབ་པར་བྱས་པ་དང་། ཡོངས་སུ་བརྟགས་པ་སྟེ། བསམ་པར་ནུས་པ་དང་། བསམ་པར་འོས་པ་ནི་བསམ་པར་བྱ་བའོ། །

[Block 876]
བསམ་པར་བྱ་བ་མ་ཡིན་པ་ནི་མི་བསམ་པ་སྟེ། དེའི་མི་མཐུན་པའི་ཕྱོགས་སུ་གྱུར་པ༌[^661]བསམ་པར་མི་ནུས་པ་དང་། བསམ་པར་མི་འོས་པའོ། །

[Block 877]
གནས་གང་ལ་ཡིན་ན་ཆོས་རྣམས་བསམ་པ་ལས་རྩོམ་པར་བྱེད་དེ། རྒྱས་པར་བསམ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 878]
རྟག་ཏུ་གུས་པར་བྱེད་པའི་སྦྱོར་བ་སེམས་པས་རྟག་ཏུ་གུས་པར་བྱེད་པའི་སྦྱོར་བའི་མི་མཐུན་པའི་ཕྱོགས་ནི་ལྷོད་ལ། དེའི་གཉེན་པོའི་ཕྱོགས་ནི་ལྷོད་པར་མི་བྱེད་དོ། །

[Block 879]
སྤྱོད༌[^662]པར་བྱེད་ཅིང་ཞེས་བྱ་བ་ནི་འདི་ལྟར་རིགས་ལ་འདི་ལྟར་ནི་མི་རིགས་པའོ་ཞེས་རྗེས་སུ་ཞུགས་ཤིང་དེ་ལྟར་སྦྱོར་བའོ། །

[Block 880]
ནག་པོ་བསྟན་པ་དང་ཆེན་པོ་བསྟན་པ་རྣམས་ཀྱང་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་བྱ་བ་ནི། གང་མདོ་སྡེ་ལ་འཇུག་ཅིང་འདུལ་བ་ལ་སྣང་ལ། ཆོས་ཉིད་དང་མི་འགལ་བ་དེ་ནི་ཆེན་པོ་བསྟན་པ་ཡིན་ལ། དེ་ལས་བཟློག་པ་ནི་ནག་པོ་བསྟན་པའོ། །
--- END BLOCKS ---
