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
[Block 596]
རིམ་པ་གཉིས་ལ་ཡང་དག་གནས། །ཞེས་པ་ནི་དེ་ཐམས་ཅད་ཀྱང་རིམ་པ་གཉིས་སུ་འདུས་ཞེས་པའི་དོན་ཏོ། །

[Block 597]
རིམ་པ་གཉིས་ཉིད་གང་ཡིན་ཞེ་ན། བསྐྱེད་པ་ཡི་ནི་རིམ་པ་དང་། ཞེས་སྨོས་ཏེ་བསྐྱེད་པའི་རིམ་པ་ནི་བསྐྱེད་པའི་རིམ་པ་སྟེ། གང་གིས༌[^296]བློས་བསྐྱེད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 598]
བསྐྱེད་པའི་རིམ་པ་ཞེས་བྱ་བ༌[^297]ནི་དེ་ལས་སྐྱེས་པའི་སྐུའོ། །

[Block 599]
ཡང་ན་བསྐྱེད་པའི་རིམ་པ་ནི་ལྷའི་རྣལ་འབྱོར་འབའ་ཞིག་པའོ། །

[Block 600]
རྫོགས་པའི་རིམ་པ་ནི་ཕྲ་མོའི་རྣལ་འབྱོར་འབའ་ཞིག་པའོ། །

[Block 601]
འདི་ཡང་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བའི་མཛོད་ཅེས་བྱ་བ་ལས་གསུངས་ཏེ་བཅོམ་ལྡན་འདས་བསྐྱེད་པའི་རིམ་པ་ཞེས་བྱ་བ་དེ་གང་ལགས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སེམས་དཔའ་ཆེན་པོ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་བསྐྱེད་པའི་རིམ་པ་ནི་རྟེན་དུ་གྱུར་པ་ཉིད་དོ། །

[Block 602]
བཅོམ་ལྡན་འདས་རྟེན་དུ་གྱུར་པ༌[^298]ཞེས་བྱ་བ་དེ༌[^299]གང་ལགས། སེམས་དཔའ་ཆེན་པོ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་ཆེན་པོའི་རྟེན་དུ་གྱུར་པའོ། །

[Block 603]
བཅོམ་ལྡན་འདས་གསང་བ་ཆེན་པོ་ཞེས་བྱ་བ་དེ་གང་ལགས། དེའི་རྟེན་ཞེས་བྱ་བ་དེ་གང་ལགས། སེམས་དཔའ་ཆེན་པོ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་ཆེན་པོ་ཞེས་བྱ་བ་དེ༌[^300]ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ལ་སོགས་པ་རྣམས་ཀྱི་ཡུལ་མ་ཡིན་པ་ཚོགས་ཀྱི་གང་ཟག་གི་ཡང་ཡུལ་མ་ཡིན་པ་ཤིན་ཏུ་རྨད་དུ་བྱུང་བ་ཐེག་པ་ཆེན་པོའི་རིགས་ཅན་གྱི་སྤྱོད་ཡུལ་དུ་གྱུར་པའོ། །

[Block 604]
སེམས་དཔའ་ཆེན་པོ་དེའི་རྟེན་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྤྲུལ་པའི་སྐུ་ཤིན་ཏུ་རྨད་དུ་བྱུང་བའོ། །

[Block 605]
བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི༌[^301]བསྐྱེད་པའི་རིམ་པ་ཞེས་བྱ་བ་དེ་གང་ལགས། སེམས་དཔའ་ཆེན་པོ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་བསྐྱེད་པའི་རིམ་པ་ཞེས་བྱ་བ་ནི་གསང་བའི་ཡང་ཤིན་ཏུ་གསང་བ་ཕྲ་མོའི་ཏིང་ངེ་འཛིན་ཏོ་ཞེས་འབྱུང་བ་ལྟ་བུའོ། །

[Block 606]
ཉིད་ཅེས་བྱ་བ་ནི་ཁོ་ན་ཞེས་པ་སྟེ། འདིར་གཞན་དང་ལྡན་པ་རྣམ་པར་གཅོད་པའི་དབང་དུ་བྱས་པའོ། །

[Block 607]
རྒོལ་ཏེ་འོག་ནས་འཆད་པ་ཞེས་བྱ་བ་ཡང་འདི་ཉིད་དམ་འདི་ལས༌[^302]གཞན་ཞིག་རྟོག་གྲང་ན། འདི་ཉིད་ནི་མ་ཡིན་ཏེ་གྲུབ་པ་ལ་སྒྲུབ་པ་ཉིད་ཀྱི་ཕྱིར་དོན་མེད་པར་འགྱུར་རོ། །

[Block 608]
མདོར་བསྟན་པ་ཡང་མ་ཡིན་ཏེ་མིང་ཉིད་ཀྱིས༌[^303]ཐམས་ཅད་མདོར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 609 [VERSE]]
རྒྱས་པར་བཤད་པ་ཡང་མ་ཡིན་ཏེ། །
མིང་ཉིད་དང་འགལ་བའི་ཕྱིར་དང་།
གཞུང་རྒྱས་པས་འཇིགས་པའི་ཕྱིར་རོ། །

[Block 610]
འོག་མ་དང་ཐ་དད་པ་ཡང༌[^304]མ་ཡིན་ཏེ། ཐ་དད་པ་དང་ཐ་དད་པ་མ་ཡིན་པ་ནི་གཅིག་གིས་གཅིག་སྤངས་པའི་འགལ་བ་ཡིན་པའི་ཕྱིར་རོ།[^305] །དེ་ལྟ་ན་ཡང་འགྱུར་རོ་ཞེ་ན། ཧ་ཅང་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 611]
འོན་ཏེ་ཐ་མི་དད་ན་ནི་སྔ་མའི་སྐྱོན་དུ་འགྱུར་རོ། །

[Block 612]
རྒྱུ་ཐ་མི་དད་པ་གཅིག་ཡིན་ནོ་ཞེ་ན་ནི་འབྲས་བུ་ཡང་དེ་ལྟར་འགྱུར་རོ། །

[Block 613]
ཐ་མི་དད་པས་ཐ་དད་པ་སྐྱེད༌[^306]ན་ནི་ཧ་ཅང་ཡང་ཐལ་བར་འགྱུར་རོ། །

[Block 614]
ཐམས་ཅད་ཐ་མི་དད་ཀྱང་ཡིན་ནོ་ཞེ་ན་ནི་གོང་མའི་སྐྱོན་དེ་ཉིད་དུ་འགྱུར་རོ། །

[Block 615]
གཞན་ཡང་རྒྱུ་ཐ་མི་དད་པས་འབྲས་བུ་ཐ་དད་པ་སྐྱེད་ན་ནི་རྫོགས་པའི་རིམ་པ་ཡང་དོན་མེད་པར་འགྱུར་རོ། །

[Block 616]
ཅི་སྟེ་གལ་ཏེ༌[^307]ཉེ་བའི་ཕྱིར་ཡིན་ནོ་ཞེ་ན༌[^308]དེ་ལྟ་ན་ནི་བསྐྱེད་པའི་རིམ་པ་ཡང་བླང་བྱ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 617]
འདི་ལྟར་རིང་བར་འགྱུར་བ་ཉིད་དང་ཕན་མི་འདོགས་པ་ཉིད་དང་། གནོད་པ་སྒྲུབ་པ་ཉིད་ནི་སྦྲུལ་ནག་པོ་བཞིན་དུ་དོར་བར་བྱ་བ་ཡིན་གྱི་ནོར་བུ་བཞིན་བླང་བར་བྱ་བ་མ་ཡིན་ནོ་ཞེ་ན་དེ་ནི་མ༌[^309]ཡིན་ཏེ། འདི་ལྟར་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་དང་གསུང་དང་ཐུགས་གསང་བ་ཆེན་པོ་འདི་ནི་མདོར་བསྟན་པ་དང་རྒྱས་པར་བསྟན་པ་གཉིས་ལ་འཇུག་སྟེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་འདུས་པའི་ལེའུ་དང་པོ་ལས་ནི་མདོར་བསྟན་པ་འབའ་ཞིག་ཉེ་བར་བསྟན་ཏེ། དེ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་སེམས་ཅན་གྱི་དོན་ཆེན་པོ་ལ་རབ་ཏུ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 618]
བསྡུས་པ་འདི་ཉིད་ཀྱིས་སེམས་ཅན་གྱི་དོན་དུ་ཇི་ལྟར་འགྱུར་ཞེ་ན། འདི་ནི་སེམས་ཅན་མདོར་བསྡུས་པ་ལ་དགའ་བའི་ཕྱིར་རོ། །

[Block 619]
ལྷག་མ་ནི་རྒྱས་པར་བསྟན་པ་ལ་དགའ་བའི་ཕྱིར་རོ། །

[Block 620]
དེ་བས་ན་འདི་ནི་དགོས་པ་ཆེན་པོ་དང་ལྡན་པའི་ཕྱིར་བླང་བར་བྱ་བ་ཉིད་དོ་ཞེའོ། །

[Block 621]
ལེའུ་དང་པོ་བསྡུས་པ་བཤད་པའོ།། །།

[Block 622 [HEADING]]
### ལེའུ་གཉིས་པ། ^2-2-0

[Block 623]
ལེའུ་གཉིས་པ་ལས་ནི་རྫོགས་པའི་རིམ་པ་འབའ་ཞིག་ཉེ་བར་སྟོན་ཏོ་ཞེས་པ་ནི་དང་པོ་ནི་བཤད་ཟིན་ལ་དེ་ལས་གཞན་ནི་མ་བྱུང་བས་དེ་ཉིད་ཀྱི་སྐབས་སུ་བབ་སྟེ། དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 624]
རྫོགས་པའི་རིམ་པ་ནི་རྫོགས་པའི་རིམ་པ་སྟེ། རྫོགས་པ་ཆེན་པོ་དང་ཤིན་ཏུ་ཉེ་བའི་རྒྱུར་གྱུར་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 625]
ཡང་ན་རྫོགས་པ་ནི་རྫོགས་པ་ཆེན་པོ་སྟེ་དེ་ཁོ་ན་ཉིད་ཆོས་ཀྱི་སྐུའོ། །

[Block 626]
དེའི་རིམ་པ་ནི་རྫོགས་པ་ཐོབ་པའི་ཐབས་ཀྱི་རིམ་པ་སྟེ་ཕྲ་མོའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 627]
འབའ་ཞིག་ཅེས་བྱ་བ་ནི་ལྷག༌[^310]མེད་ཅེས་བྱ་བའི་དོན་ཏེ་རྫོགས་པའི་རིམ་པ་འབའ་ཞིག་ཉེ་བར་སྟོན་གྱི་གཞན་མི་སྟོན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 628]
འདིར་ཡང་རྫོགས་པའི་རིམ་པ་འབའ་ཞིག་སྟོན་གྱི་གཞན་མི་སྟོན་པ་ཅིའི་ཕྱིར་ཞེ་ན། འདི་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱིས་ཚོགས་ཀྱི་གང་ཟག་གི་དབང་དུ་བྱས་པ་མ་ཡིན་གྱི་སློབ་མ་འབའ་ཞིག་གི་དབང་དུ་བྱས་པའོ། །

[Block 629]
དེ་ལྟར་ཡང་ཅི་མངོན་ཞེ་ན། གསང་བ་ལུང་བསྟན་པ་ཞེས་བྱ་བ་ལས་ཀྱང་། བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་དང་། གསུང་དང་ཐུགས་གསང་བའི་ཡང་ཤིན་ཏུ་གསང་བ་མཆོག་ཏུ་གྱུར་པའི་དངོས་ཀྱི་ལམ་དུ་གྱུར་པ་འདི་ནི་ཉན་ཐོས་ཀྱི་ཡུལ་མ་ཡིན་རང་སངས་རྒྱས་ཀྱི་ཡུལ་མ་ཡིན་བྱང་ཆུབ་སེམས་དཔའི་ཡུལ་མ་ཡིན་ནོ། །

[Block 630]
དེའི༌[^311]ཕྱིར་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་གསང་བ་ཆེན་པོ་འདི་ནི་འདས་པའི་དུས་སུ་ཡང་མ་གསུངས་སོ། །

[Block 631]
མ་འོངས་པའི་དུས་སུ་ཡང་གསུང་བར་མི་འགྱུར་རོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་གསང་བ་ཆེན་པོ༌[^312]དེའི་སྣོད་དུ་མ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 632]
དེ་བས་ན་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ།། །།

[Block 633 [HEADING]]
### ལེའུ་གསུམ་པ། ^2-3-0

[Block 634]
ལེའུ་གཉིས་པ་བརྗོད་ཟིན་ནས་གསུམ་པ་བརྗོད་པར་རིགས་པས་དེའི་ཕྱིར་ལེའུ་གསུམ་པ་ལས་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། ལེའུ་གསུམ་པ་ནི་འདིར་གྲངས་ཀྱིས༌[^313]

[Block 635]
གསུམ་པ་ཉིད་དོ། །
--- END BLOCKS ---
