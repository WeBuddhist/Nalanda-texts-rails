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
[Block 806 [VERSE]]
སྡིག་པའི་བསམ་པ་བརྟན་པ་དང་། །
མཁྱུད་པ༌[^595]ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 807]
དེ་ཉིད་ཀྱི་ཕྱིར་མ་ནིང་ལ་སོགས་པས་ཀྱང་མ་ཡིན་ཏེ། སྲེད་པའི་སྤྱད་པའི་ཕྱོགས་དང་མཐུན་པའི་ཕྱིར་དང་། ངན་སོང༌[^596]བཞིན་ནོ་དགེ་བའི་རྩ་བ་ཀུན་དུ་འཆད་པའི་རང་བཞིན་ཇི་ལྟ་བུ་ཞིག་ཡིན་ཞེ་ན། དེ་ནི་མི་ལྡན་པའོ། །

[Block 808]
གང་གི་ཚེ་དགེ་བའི་རྩ་བ་རྣམས་ཀྱི་ཐོབ་པ་ཡང་མི་སྐྱེ་ལ་མ་ཐོབ་པ་སྐྱེ་བ་སྟེ། མི་ལྡན་པ་དེ་སྐྱེས་ན་དགེ་བའི་རྩ་བ་རྣམས༌[^597]ཀུན་དུ་ཆད་པ་ཞེས་བྱའོ། །

[Block 809 [HEADING]]
### དགེ་བའི་རྩ་བ་ཉིང་མཚམས་སྦྱོར་བ། ^1-51-0

[Block 810]
ཀུན་དུ་ཆད་པ་དེ་དག་ཇི་ལྟར་ན་ཡང་ཉིང་མཚམས་སྦྱོར་ཞེ་ན། མཚམས་ནི་ཐེ་ཚོམ་ཡོད་ལྟ་བས། །ནམ་ཞིག་འདི་ལ་རྒྱུ་དང་འབྲས་བུ་ལ་ཐེ་ཚོམ་སྐྱེས་པའམ། ཡང་དག་པའི་ལྟ་བ་ཞེས་བྱ་བའི་དོན་ཏེ། ཡོད་པར་ལྟ་བ་སྐྱེས་པ་དེའི་ཚེ་ཡང་དེའི་ཐོབ་པ་ཀུན་དུ་སྤྱོད་པའི་ཕྱིར་དགེ་བའི་རྩ་བ་རྣམས་ཉིང་མཚམས་སྦྱོར་ཞེས་བྱའོ། །

[Block 811]
ཉིང་མཚམས་ནི་རྣམ་པ་དགུ་ཅིག་ཅར་དུ་སྦྱར་བ༌[^598]ལ། མངོན་སུམ་དུ་ནི་རིམ་གྱིས་འགྱུར་ཏེ། ནད་མེད་ནས་སྟོབས་རྙེད་པ་བཞིན་ནོ། །

[Block 812]
ཡང་དེ་དག་གི་ཉིང་མཚམས་སྦྱོར་བ་ནི། མཚམས་མེད་བྱེད་པ༌[^599]འདི་ལས༌[^600]མིན། །གཞན་གྱིས༌[^601]ནི་འདི་ཉིད་ལ་འགྱུར་གྱི༌[^602]མཚམས་མེད་པར༌[^603]བྱེད་པ༌[^604]ནི་མ་ཡིན་ཏེ། དེ་ཉིད་ལ་དགོངས་ནས། གང་ཟག་འདི་ནི་མཐོང་བའི་ཆོས་ཁོ་ན་ལ་དགེ་བའི་རྩ་བ་རྣམས་ཉིང་མཚམས་སྦྱོར་བའི་སྐལ་བ་དང་ལྡན་པ་མ་ཡིན་གྱི་འདི་ནི་ངེས་པར་དམྱལ་བ་དག་ན༌[^605]འཆི་འཕོ་བ་འམ་སྐྱེ་བ་ན་དགེ་བའི་རྩ་བ་རྣམས་ཉིང་མཚམས་སྦྱོར་བར་འགྱུར་རོ་ཞེས་གསུངས་ཏེ། སྐྱེ་བ་ནི་སྲིད་པ་བར་མ་ལ་གནས་པའོ། །

[Block 813]
འཆི་འཕོ་བ་ནི་འཆི་འཕོ་བ་ལ་མངོན་དུ་ཕྱོགས་པའོ། །

[Block 814]
དེ་ལ་གང་ཞིག་རྒྱུའི་སྟོབས་ཀྱིས་ཀུན་དུ་གཅོད་པ་དེ་ནི་འཆི་འཕོ་བ་ན༌[^606]ཉིང་མཚམས་སྦྱོར་བར་འགྱུར་རོ། །

[Block 815]
གང་ཞིག་རྐྱེན་གྱི་སྟོབས་ཀྱིས་ཀུན་དུ་གཅོད་པ་དེ་ནི་སྐྱེ་བ་ན་ཉིང་མཚམས་སྦྱོར་བར་འགྱུར་ཏེ། རང་གི་སྟོབས་ཀྱིས་གཅོད་པ་གང་ཡིན་པ་དང་། གཞན་གྱི་སྟོབས་ཀྱིས་གཅོད་པ་གང་ཡིན་པ་དེ༌[^607]དང་འདྲའོ། །

[Block 816]
ཡང་སྨྲས་པ། གང་ཞིག་བསམ་པ་ཉམས་པས་ཀུན་དུ་གཅོད་པར་བྱེད་པ་དེ་ནི་མཐོང་བའི་ཆོས་ཁོ་ན་ལ་ཉིང་མཚམས་སྦྱོར་བར་འགྱུར་རོ། །

[Block 817]
གང་ཞིག་བསམ་པ་དང་སྦྱོར་བ་ཉམས་པས་གཅོད་པར་བྱེད་པ་དེ་ནི་ལུས་ཞིག་ནས་ཉིང་མཚམས་སྦྱོར་བར་འགྱུར་ཏེ། ལྟ་བ་ཉམས་པ་གང་ཡིན་པ་དང་། ལྟ་བ་དང་ཚུལ་ཁྲིམས་ཉམས་པ་གང་ཡིན་པ་དེ་ཡང་དེ་དང་འདྲའོ། །

[Block 818]
དགེ་བའི་རྩ་བ་ཀུན་དུ་འཆད་པ༌[^608]ཡིན་ལ་ལོག་པ་ཉིད་དུ་ངེས་པ་མ་ཡིན་པ་ཡང་ཡོད་ཅེས་བྱ་བ་མུ་བཞི་སྟེ། མུ་དང་པོ་ནི༌[^609]རྫོགས་བྱེད་ལ་སོགས་པའོ། །

[Block 819]
གཉིས་པ་ནི་མ་སྐྱེས་དགྲའོ། །

[Block 820]
གསུམ་པ་ནི་ལྷ་སྦྱིན༌[^610]ནོ། །

[Block 821]
བཞི་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 822]
དགེ་བའི་རྩ་བ་ཀུན་དུ་གཅོད་པར་བྱེད་པའི་ལོག་པར་ལྟ་བའི་རྣམ་པར་སྨིན་པ་ནི་མནར་མེད་པ་ཡིན་ནོ། །

[Block 823]
མཚམས་མེད་པར་བྱེད་པ་རྣམས་ཀྱིས༌[^611]ནི་དེར་རམ་གཞན་གྱི་ནང༌[^612]དུའོ། །

[Block 824 [HEADING]]
### ལས་ཀྱི་ལམ་དང་སེམས་པ་ལྷན་ཅིག་འབྱུང་བ། ^1-52-0

[Block 825]
འདི་ནི་ལས་ཀྱི་སྐབས་ཡིན་པས་དེ་ལ་ལས་ཀྱི་ལམ་དུ་ཞིག་དང་སེམས་པ༌[^613]ལྷན་ཅིག་ཏུ༌[^614]འབྱུང་བར་འགྱུར་བར༌[^615]བརྗོད་པར་བྱ་སྟེ།

[Block 826 [VERSE]]
མི་དགེ་བརྒྱད་ཀྱི་བར་དག་དང་། །
སེམས་པ་ཅིག་ཅར་ལྷན་ཅིག་འབྱུང་། །

[Block 827]
རེ་ཞིག་སེམས་པ༌[^616]གཅིག་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་གཞན་མེད་པར་བརྣབ་སེམས་ལ་སོགས་པར༌[^617]མངོན་དུ་འགྱུར་བའམ།[^618] སེམས་པ་ཉོན་མོངས་པ༌[^619]ཅན། དེའི་སྦྱོར་བས་གཟུགས་ཅན་རྣམས་ལས་གང་ཡང་རུང་བ་ཞིག་མཐར་ཕྱིན་པར་བྱེད་ནའོ། །

[Block 828]
གཉིས་དང་ལྷན་ཅིག་ཏུ་འབྱུང་བ་ནི་གནོད་སེམས་སུ་འགྱུར་བ༌[^620]སྲོག་གཅོད་པ་དང་། བརྣབ་སེམས་དང་ལྡན་པ་མ་བྱིན་པར་ལེན་པའམ། འདོད་པས་ལོག་པར་གཡེམ་པའམ། ཚིག་ཀྱལ་པ་སྨྲ་ནའོ། །

[Block 829]
གསུམ་དང་ལྷན་ཅིག་ཏུ་འབྱུང་བ་ན་བརྣབ༌[^621]སེམས་དང་ལྡན་པ་ཅིག་ཅར་དུ་གཞན་གྱིས༌[^622]སྲོག་ཆགས་བསད་པས༌[^623]འཕྲོག་ནའོ། །

[Block 830]
འོ་ན་ནི་དེ༌[^624]ཆགས་པ་ཁོ་ནས་མ་བྱིན་པར་ལེན་པ་མཐར་ཕྱིན་པར་བྱེད་པ་མི་འགྲུབ་པ་མ་ཡིན་ནམ་ཞེ་ན། ངེས་པ་དེ་ནི་སེམས་གཞན་དང་མི་ལྡན་པའི་དེ་རྫོགས་པ་ལ་ཤེས་པར་བྱའོ། །

[Block 831]
བརྣབ་སེམས་མངོན་སུམ་དུ་གྱུར་པ་དེའི་སྦྱོར་བས་གཟུགས་ཅན་གཉིས་མཐར་ཕྱིན་པར་བྱེད་ན་ཡང་གསུམ་ཁོ་ན་དང་ལྷན་ཅིག་འབྱུང་ངོ་། །བཞི་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་དབྱེན་བྱ་བའི་བསམ་པ་དང་ལྡན་པ་བརྫུན་གྱི་ཚིག་གམ་ཚིག་རྩུབ་པོ་སྨྲ་ན་སྟེ། དེ་ལ་ནི་ཡིད་ཀྱི་གཅིག་ཡིན་ལ་ངག་གི་གསུམ་ཡིན་ནོ། །

[Block 832]
ཡང་ན་བརྣབ་སེམས་ལ་སོགས་པར་གྱུར་པ་དེའི་སྦྱོར་བས་གཞན་གསུམ་མཐར་ཕྱིན་པར་བྱེད་ན་སྟེ། ལྔ་དང་དྲུག་དང་བདུན་དང་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 833]
བརྒྱད་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་བརྣབ་སེམས་ལ་སོགས་པ་མངོན༌[^625]དུ་གྱུར་པ་ཁོ་ན་དྲུག་ལ་སྦྱོར་བ་བྱས་ནས་འདོད་པས་ལོག་པར་གཡེམ་པ་དག་ཉིད༌[^626]ཀྱིས་བྱེད་ལ་མཉམ་དུ་མཐར་ཕྱིན་པར་འགྱུར༌[^627]ནའོ། །

[Block 834]
རེ་ཞིག་མི་དགེ་བ་དག་དང་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 835]
དགེ་བ་བཅུ་ཡི་བར་དག་དང་། །དགེ་བའི་ལས་ཀྱི་ལམ་དག་ནི་བཅུའི་བར་དང་སེམས་པ་ལྷན་ཅིག་འབྱུང་ངོ་ཞེས་སྤྱིར་བསྟན་ནས་དམིགས་ཀྱིས་སྟོན་པར་བྱེད་དེ། གཅིག་དང་བརྒྱད་དང་ལྔ་དང་མིན། །ལས་ཀྱི་ལམ་གཅིག་དང་བརྒྱད་དང་ལྔ་དང་ལྷན་ཅིག་ཏུ་མི་འབྱུང་ངོ་། །དེ་ལ་གཉིས་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་དེ་དག༌[^628]རྣམ་པར་ཤེས་པ་ལྔ་ལ་གནས་པ་ནི།[^629] གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པའི་ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པའི་གནས་པའོ། །

[Block 836]
གསུམ་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་ཡང་དག་པའི་ལྟ་བ་དང་མཚུངས་པར་ལྡན་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ལ་གནས་པའོ། །

[Block 837]
བཞི་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་དགེ་བ་དང་། [^630]མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པའི་སེམས་དང་ལྡན་པ་དགེ་ཚུལ་གྱི་སྡོམ་པ་ཡང་དག་པར་ལེན་པ་ནའོ། །

[Block 838]
དྲུག་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་དགེ་བའི་རྣམ་པར་ཤེས་པ་ལྔ་ལ་གནས་པ་དེ་ཡང་དག་པར་ལེན་པ་ནའོ། །

[Block 839]
བདུན་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་དགེ་བའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ལ་གནས་ཏེ་དེ་ཁོ་ན་ཡང་དག་པར་ལེན་པ་དང་། མི་དགེ་བ་དང༌[^631]ལུང་དུ་མ་བསྟན་པའི་སེམས་དང་ལྡན་པ་དགེ་སློང་གི་སྡོམ་པ་ཡང་དག་པར་ལེན་པ་ནའོ། །

[Block 840]
དགུ་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་དགེ་བའི་རྣམ་པར་ཤེས་པ་ལྔ་ལ་གནས་པ་དང་ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་དང་། མཚུངས་པར་ལྡན་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ལ་གནས་པ་དེ་ཡང་དག་པར་ལེན་པ་དང་། དེ་ཉིད་བསམ་གཏན་གྱིས་བསྡུས་པ་ལ་གནས་པ༌[^632]བཅུ་དང་ལྷན་ཅིག་འབྱུང་བ་ནི་དེ་ལས་གཞན་པའི་དགེ་བའི༌[^633]ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་གནས་པ་དགེ་སློང་གི་སྡོམ་པ་ཡང་དག་པར་ལེན་པ་ཁོ་ན་དང་། ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་དག་ཁོ་ན་མ་གཏོགས་པ་བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པ་དང་ལྷན་ཅིག་འཇུག་པའི་སེམས་པ་ཐམས་ཅད་ཡིན་ནོ། །

[Block 841]
སྡོམ་པ་མ་གཏོགས་པར་ནི་གཅིག་དང་ལྷན་ཅིག་འབྱུང་བ་ཡང་ཡོད་དེ། སེམས་གཞན་དང་ལྡན་པ་སྤོང་བའི་ཡན་ལག་གཅིག་ཡང་དག་པར་ལེན་པ་ནའོ། །

[Block 842]
ལྔ་དང་བརྒྱད་དང་ལྷན་ཅིག་འབྱུང་བ་ཡང་ཡོད་དེ། དགེ་བའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དང་ལྡན་པ་ཅིག་ཅར་དུ་ཡན་ལག་གཉིས་དང་ལྔ་ཡང་དག་པར་ལེན་པ་ནའོ། །

[Block 843 [HEADING]]
### འགྲོ་བ་གང་ན་ལས་ཀྱི་ལམ་ཡོད་པ། ^1-53-0

[Block 844]
འགྲོ་བ་གང་ན་དགེ་བའམ་མི་དགེ་བའི་ལས་ཀྱི་ལམ་དུ་ཞིག་མངོན་སུམ་དུ་གྱུར་པའམ་ལྡན་པའི་སྒོ་ནས་ཡོད་ཅེ་ན།

[Block 845 [VERSE]]
དམྱལ་བ་ན་ནི་ཀྱལ་པ་དང་། །
ཚིག་རྩུབ་གནོད་སེམས་རྣམ་གཉིས་སོ། །
--- END BLOCKS ---
