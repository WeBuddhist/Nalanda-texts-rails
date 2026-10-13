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
[Block 1996]
ཡང་ཅིའི་ཕྱིར་བརྫུན་དུ་སྨྲ་བ་སྤོང་བ་ཁོ་ན་བསླབ་པའི་གཞིར་གཞག་ལ་ཕྲ་མ་ལ་སོགས་པ་ལས་ནི་མ་ཡིན་ཞེ་ན། རྒྱུ་གསུམ་པོ་དེ་དག་ཉིད་ཀྱི་ཕྱིར་ཏེ།

[Block 1997 [VERSE]]
བརྫུན་སྨྲ་ཤིན་ཏུ་སྨད་ཕྱིར་དང་། །
སླ་ཕྱིར་མི་བྱེད་འཐོབ་ཕྱིར་རོ། །
བསླབ་པ་ཐམས་ཅད་འདས་གྱུར་ན། །
བརྫུན་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར། །

[Block 1998]
བསླབ་པ་ཐམས་ཅད་འདས་ན་དྲི་བར་བྱ་བ་ལ་བདག་གིས་དེ་ལྟ་བུ་མ་བྱས་སོ་ཞེས་བྱ་བ་འདི་ཉེ་བར་གནས་པར་འགྱུར་ཏེ། བརྫུན་དུ་སྨྲ་བར་ཐལ་བར་འགྱུར་བས་དེའི༌[^785]ཇི་ལྟར་འདས་པར་བྱས་ཀྱང་བདག་ཉིད་འཆགས་པར་འགྱུར་སྙམ་ནས་བརྫུན་དུ་སྨྲ་བ་ལས་ལྡོག་པར་བཤད་དོ། །

[Block 1999]
ཡང་ཅིའི་ཕྱིར་བཅས་པའི༌[^786]ཁ་ན་མ་ཐོ་བ་ལས་མྱོས་པར་འགྱུར་བ་འཐུངས་པ༌[^787]ལས་གཞན་འདིའི་བསླབ་པའི་གཞི་རྣམ་པར་མ་བཞག་ཅེ་ན།

[Block 2000]
བཅས་པའི༌[^788]ཁ་ན་མ་ཐོ་བ། །མྱོས་འགྱུར་ཉིད་ལས། ཅིའི་ཕྱིར་ཞེ་ན། གཞན་བསྲུང་ཕྱིར་རོ། །

[Block 2001]
མྱོས་པར་འགྱུར་བ་འཐུངས་ན་ཡན་ལག་གཞན་དང་གཞན་དག་ཀྱང་མི་བསྲུང་བར༌[^789]འགྱུར་རོ། །

[Block 2002]
ཅི་སྡོམ་པ་གསུམ་པོ་འདི་དག་གང༌[^790]ལས་གཅིག་འཐོབ། དེ་ལས་ལྷག་མ་དག་ཀྱང་འཐོབ་བམ་ཞེ་ན་མ་ཡིན་ནོ། །

[Block 2003]
འོན་ཀྱང་།

[Block 2004 [VERSE]]
འདོད་གཏོགས་ཐམས་ཅད་གཉིས་ཀ་དང་། །
དེ་ལྟར་དག་ལས་འཐོབ་པར་འགྱུར། །

[Block 2005]
འདོད་གཏོགས་ཞེས་བྱ་བ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཡིན་ནོ། །

[Block 2006]
ཐམས་ཅད་ལས་ཞེས་བྱ་བ་ནི་སྦྱོར་བ་དང་དངོས་དང་མཇུག་ལས་སོ། །

[Block 2007]
གཉིས་ཀ་ལས་ཞེས་བྱ་བ་ནི་སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པར་སྟོན་པ་དང་། རང་བཞིན་དང་བཅས་པའི་ཁ་ན་མ་ཐོ་བ་ལས་སོ། །

[Block 2008]
སེམས་ཅན་གྱི་རྟེན་ལ་འཇུག་པའི་ཕྱིར་དུས་ད་ལྟར་གྱི་ཕུང་པོ་དང་ཁམས་དང་། སྐྱེ་མཆེད་ཁོ་ན་ལས་འཐོབ་ཀྱི་འདས་པ་དང་མ་འོངས་པ་དག་ལས་མ་ཡིན་ཏེ། དེ༌[^791]དག་ནི་སེམས་ཅན་དུ་མི་བགྲང་བའི་ཕྱིར་རོ། །

[Block 2009 [VERSE]]
བསམ་གཏན་ཟག་མེད་སྡོམ་པ་ནི། །
དངོས་དང་དུས་ནི་ཐམས་ཅད་ལས། །

[Block 2010]
བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པ་ནི་ལས་ཀྱི་ལམ་དངོས་ཁ་ན༌[^792]ལས་འཐོབ་ཀྱི་སྦྱོར་བ་དང་མཇུག་ལས་ཀྱང་མ་ཡིན་ན་བཅས་པའི༌[^793]ཁོ་ན་མ་ཐོ༌[^794]བ་ལས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། དུས་ཐམས་ཅད་ཀྱི་ཕུང་པོ་དང་། ཁམས་དང་སྐྱེ་མཆེད་ལས་འཐོབ་བོ། །

[Block 2011]
ཡང་ཅི་སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་དག་སེམས་ཅན་ཐམས་ཅད་དང་། ཡན་ལག་ཐམས་ཅད་དང་། རྒྱུ་ཐམས་ཅད་ཀྱིས་འཐོབ་བམ། འོན་ཏེ་བྱེ་བྲག་ཅི་ཡོད་ཅེ་ན། རེ་ཞིག་ངེས་པར། སྡོམ་པ་སེམས་ཅན་ཐམས་ཅད་ལས་འཐོབ་ལ། ཡན་ལག་རྒྱུ་ལ་དབྱེ་བ་ཡོད། །དེ་ལ་དགེ་སློང་གི་སྡོམ་པ་ནི་ཐམས་ཅད་ལས་འཐོབ༌[^795]བོ། །

[Block 2012]
དེ་ལས་གཞན་ནི་གཞི༌[^796]ལས་སོ། །

[Block 2013]
ལས་ཀྱི་ལམ་རྣམས་ནི༌[^797]སྡོམ་པའི་ཡན་ལག་ལས་ཡིན་ནོ། །

[Block 2014]
རྒྱུ་ལས་ཀྱང་རྣམ་གྲངས་ལ་ལས་ནི་ཐམས་ཅད་ཀྱིས་ཏེ། གལ་ཏེ་མ་ཆགས་པ་དང་། ཞེ་སྡང་མེད་པ་དང་།

[Block 2015]
གཏི་མུག་མེད་པ་རྒྱུ་ཡིན་ནའོ།[^798] །ལ་ལ་ལས་ནི་གཅིག་གིས་ཏེ། །

[Block 2016]
སེམས་ཆུང་ངུ་དང་འབྲིད་དང་ཆེན་པོ་དག་རྒྱུར་འདོད་པ་ཡིན་ནའོ། །

[Block 2017 [VERSE]]
སྡོམ་པ་མིན་པ་ཐམས་ཅད་དང་། །
ཡན་ལག་ཀུན་ལས་རྒྱུས་མིན༌[^799]ནོ། །

[Block 2018]
མ་ཚང་བའི་སྡོམ་པ་མ་ཡིན་པ་ཅན་ནི་མེད་དོ། །

[Block 2019]
རྒྱུ་ཐམས་ཅད་ཀྱིས་ནི་མ་ཡིན་ཏེ། སེམས་ཆུང་ངུ་ལ་སོགས་པ་ཅིག་ཅར་དུ་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2020]
གང་དག་ལས་འཐོབ་པ་བཤད་ནས་ཇི་ལྟར་འཐོབ་པ་དེ་བརྗོད་པར་བྱ་སྟེ།

[Block 2021 [VERSE]]
སྡོམ་པ་མིན་པ་བྱ་བའམ། །
ཁས་ལེན་པ་ལས་འཐོབ་པར་འགྱུར། །

[Block 2022]
དེའི་རིགས་སུ་སྐྱེས་པ་རྣམས་ཀྱིས་ནི་གསོད་པར༌[^800]སྦྱོར་བ་བྱ་བ་ལས་སྡོམ་པ་མ་ཡིན་པ་འཐོབ་བོ། །

[Block 2023]
གཞན་གྱི་རིགས་སུ་སྐྱེས་པ་རྣམས་ནི་ལས་དེ་ཁས་ལེན་པ་ལས་སོ། །

[Block 2024 [VERSE]]
ལྷག་མའི་རྣམ་རིག་མིན་ཞིང་དང་། །
ལེན་དུ༌[^801]གུས་པར་བྱེད་པས་འཐོབ། །

[Block 2025]
གང་ཀུན་དགའ་ར་བ་ལ་སོགས་པ་ཕུལ་བ་ཙམ་གྱིས་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྐྱེ་བར་འགྱུར་བ་དེ་ལྟ་བུའི་ཞིང་ཡང་ཡོད་དོ། །

[Block 2026]
ཡང་ན་སངས་རྒྱས་ལ་ཕྱག་མ་འཚལ་གྱི་བར་དུ་ཟས་མི་བཟའོ༌[^802]ཞེས་བྱ་བ་ལ་སོགས་པའི་ཡི་དམ་བཅས་པའམ། དགེ་བའམ་མི་དགེ་བ་གང་ལས་འདིའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྐྱེ་བར་འགྱུར་བ་དེ་ལྟ་བུའི་གུས་པས་ལས་བྱེད་པ་ལས་སོ། །

[Block 2027 [HEADING]]
#### སྡོམ་པ་གཏོང་བ། ^4-2-5-0

[Block 2028]
ཐོབ་པ་བཤད་ནས་གཏོང་བ་བརྗོད་པར་བྱ་སྟེ།

[Block 2029 [VERSE]]
བསླབ་པ་ཕུལ་དང་ཤི་འཕོས་དང་། །
མཚན་གཉིས་དག་ནི་འབྱུང་བ་དང་། །
རྩ་བ་ཆད་དང་མཚན་འདས་ལས། །
སོ་སོར་ཐར་པའི་འདུལ་བ་གཏོང་། །

[Block 2030]
བསླབ་པའི་གཞི་རྣམས་ཀྱི༌[^803]མི་བརྡ་ཕྲད་པའི་དྲུང་དུ་བསམ་པ་ཐག་པ་ནས་སླར་ཕུལ་པ་དང་། རིས་མཐུན་བཏང་བ་དང་། མཚན་གཉིས་ཅིག་ཅར་བྱུང་བ་དང་། དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པ་ལས་སོ། །

[Block 2031]
བསྙེན་གནས་ཀྱི་སྡོམ་པ་ནི་མཚན་མོ་འདས་པ་ལས་ཀྱང་ངོ་། །ཁ་ཅིག་ལྟུང་བར་འགྱུར་ལས་སྨྲ། །གཞན་དག་ན་རེ་ལྟུང་བར་འགྱུར་བ་བཞི་ལས་གང་ཡང་རུང་བ་ཞིག་གིས་དགེ་སློང་དང་དགེ་སྦྱོང་གི་སྡོམ་པ་གཏོང་ངོ་ཞེས་ཟེར་རོ། །

[Block 2032]
གཞན་དག་དམ་ཆོས་ནུབ་པ་ལས། །

[Block 2033]
འདི་ལྟར་དམ་པའི་ཆོས་ནུབ་ན་བསླབ་པའི་མཚམས་ཐམས་ཅད་དང་། །

[Block 2034 [VERSE]]
ལས་ཀྱི་མཐའ་རྣམས་མེད་པར་འགྱུར་རོ། །
ཁ་ཆེ་རྣམས་ནི་བྱུང་བ་ལ། །
བུ་ལོན་ནོར༌[^804]བཞིན་གཉིས་སུ་འདོད། །

[Block 2035]
ཁ་ཆེ་བ་རྣམས་ན་རེ་རྩ་བའི་ལྟུང་བ་ལ་ཡང་དགེ་སློང་གི་སྡོམ་པ་གཏོང་བ་མེད་དོ། །ཅིའི་ཕྱིར་ཞེ་ན། ཕྱོགས་གཅིག་ཉམས་པས་སྡོམ་པ་ཟད་པར་གཏོང་བ་ནི་མ་རིགས༌[^805]པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
