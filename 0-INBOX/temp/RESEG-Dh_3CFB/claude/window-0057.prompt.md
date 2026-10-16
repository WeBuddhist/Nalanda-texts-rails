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
ནུས་པ་བར་དུ་མ་ཆོད་པས་ཉེ་བར་སྦྱོར་བ་ཅན་གྱི་གནས་སྐབས་ལས་ཐ་དད་པས་དེ་ལས་གཞན་པ་ཉིད་ཁྱད་པར་དུ་བྱེད་དོ། །

[Block 1997]
ཕུལ་དུ་དབྱུང་དུ་མེད་པ་ཅན་གྱི་ལྟོས་པ་ཡང་སྔར་བཀག་ཟིན་ཏོ། །

[Block 1998]
དེ་ཡང་བྱེད་པའི་བྱ་བ་ཉིད་ལས་གྲུབ་པའི་ཕྱིར། འབྲས་བུ་ཐམས་ཅད་དང་ཆོས་མཚུངས་པ་ཉིད་ཅན་ནོ། །

[Block 1999]
དེ་འདྲ་བ་དེ་གསལ་བ་ཡིན་ན་ཐམས་ཅད་གསལ་བྱའམ། ཅུང་ཞིག་ཀྱང་མ་ཡིན་ཏེ་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 2000]
དེ་ལྟར་ན་ནི།

[Block 2001 [VERSE]]
གྲུབ་པའི་དོན་ལ་རང་ཤེས་པས། །
གཞན་བློའི་རྒྱུ༌[^1462]ནི་གསལ་བྱེད་འདོད། །
དཔེར་ན་སྒྲོན་བཞིན་གཞན་དུ་ཡང་། །
བྱེད་པོ་ལས་འདི་ཁྱད་པར་ཅི། །

[Block 2002]
བདག་ཉིད་རྟོགས་པའི་སྒོ་ནས་གཞན་རྟོགས་པའི་རྒྱུ་འཇིག་རྟེན་ལ་སྒྲོན་མ་ལ་སོགས་པ་དང་འདྲ་བར་གསལ་བྱེད་དུ་གྲགས་པ་ཡིན་ནོ། །

[Block 2003]
གལ་ཏེ་དེ་སྔར་གྲུབ་པར་འགྱུར་ཏེ། རིགས་མཐུན་པའི་ཉེ་བར་ལེན་པའི་སྐད་ཅིག་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2004]
ཕུལ་དུ་བྱུང་བ་དེ་ཉིད་ཀྱི་ཤེས་པའི་རྒྱུ་ནི་དེའི་ཚོགས་པའི་རྐྱེན་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2005]
མ་གྲུབ་པ་དམིགས་པ༌[^1463]གང་ཡིན་པ་དེ་དག་ཀྱང་བྱེད་པ་པོ་ཡིན་ཏེ། བུམ་པ་ལ་སོགས་པའི་རྫ་མཁན་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2006]
ངོ་ཤེས་པ་ལ་སོགས་པའི་གྲུབ་པའི་རྒྱུ་དག་གིས་ཀྱང་རྒྱུའི་མཚན་ཉིད་གསོ་བར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 2007]
གང་ཅུང་ཟད་ཕྱིས་ཡི་གེ་ཨ་རྟོགས་པ་ནི་སྔ་མ་དང་ཐ་དད་པ་མེད་པ་ཡུལ་ཅན་ཡིན་ཏེ། ཡི་གེ་ཨ་རྟོགས་པའི་ཕྱིར་དེ་འདྲའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2008]
དེས་ཀྱང་རང་གི་མཚན་ཉིད་ཐ་དད་པ་མེད་པར་སྒྲུབ་པར་ནུས་པ་མ་ཡིན་ཏེ། དེའི་རང་བཞིན་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2009]
སྤྱི་བརྗོད་ན་ཐ་དད་པ་མེད་པའི་ཡུལ་ཅན་ལ་ཡང་འགལ་བ་མེད་དོ། །

[Block 2010]
ཡུལ་གཅིག་རྟོགས་པ༌[^1464]ཡང་སྔ་མ་དང་ཕྱི་མའི་ངོ་བོ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 2011]
རྒྱུ་ཐག་ཉེ་བ་ཅན་དང་རྒྱུ་ཐག་ཉེ་བ་ཅན་མ་ཡིན་པ་ཉིད་ཀྱིས་བསྐྱེད་པ་དང་མི་བསྐྱེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2012]
ཐག་ཉེ་བ་ཡིན་དུ་ཟིན་ཀྱང་མི་སྐྱེ་བ་ནི་དེའི་རྒྱུ་ཅན་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ།[^1465] །དེ་དག་ནི་རྒྱུ་མ་ལུས་པ་ཐ་དད་པ་ཅན་ཉིད་ཡིན་ནོ། །

[Block 2013]
དེ་ལ་གཅིག་ཐ་དད་པ་མེད་དུ་ཟིན་ཀྱང་ནུས་པ་ན་ལྟོས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2014]
སྔ་ཕྱིའི་རྟོགས་པ་དག་ནི་ཡུལ་གཅིག་པ་ཉིད་དུ་རིགས་པ་དང་འགལ་ལོ། །

[Block 2015]
རྟོགས་པའི་སྣང་བ་དང་རང་བཞིན་ཐ་དད་པ་ཡང་མི་མཚུངས་པའི་ཕྱིར་ཡུལ་གཅིག་པ་མ་ཡིན་ཏེ། [^1466]བུམ་པ་ལ་སོགས་པ་དག་ལ་ཡང་བྲལ་བར༌[^1467]འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2016]
གལ་ཏེ་དེ་ལས་མཐོང་བ་དང་འགལ་བའི་ཕྱིར་སྒྲུབ་པར་བྱེད་པ་ཉིད་མ་ཡིན་ནོ་ཞེ་ན། འདི་ལ་ཡང་འགལ་བ་མེད་པ་གང་གིས་གྲུབ། ཇི་སྲིད་དེ་སྐད་དུ་བརྗོད་པ་དོན་ཐ་དད་པ་མེད་པས་ཁྱབ་པར་མ་བསྒྲུབས་པ༌[^1468]དེ་སྲིད་དུ་ལྡོག་པ་ལ་ཐེ་ཚོམ་ཟ་བ་ཡིན་ནོ། །

[Block 2017]
གང་གི་ཚེ་བྱེད་པ་སོ་སོ་ཐ་དད་པས་ཀྱང་སྒྲ་ཐ་དད་པའི་རང་བཞིན་ཅན་མཉན་པ་ལ་སྣང་བ་ན་གཅིག་སྒྲུབ་པར་བྱེད༌[^1469]ན་ཅིའི་ཕྱིར་བུམ་པ་ལ་སོགས་པ་མ་ཡིན། དེ་ལ་ཡང་གསལ་བྱེད་ཐ་དད་པ་ལས་སྣང་བ་ཐ་དད་དོ་ཞེས་ལན་བཏབ་བར་ནུས་པ་ཁོ་ན་ཡིན་ན། [^1470]གཞན་ཡང་།

[Block 2018 [VERSE]]
བྱེད་པ་རྣམས་ཀྱི་ཚོགས་པ་ཡི། །
བྱ་བ་ཡིས་ནི་ངེས་པ་ཡང་། །
དམིགས་ཕྱིར་འབྲས་བུ་ཉིད་ཡིན་ཏེ། །
གསལ་བྱེད་དེ་ལ་མི་སྲིད་ཕྱིར། །

[Block 2019]
འགའ་ཞིག་གི་ཚེ་ཡང་བྱེད་པའི་བྱ་བ་རྣམས་ལ་སྒྲ་མ༌[^1471]དམིགས་པ་ནི་ཡོད་པ་ཡིན། གདོན་མི་ཟ་བར་གསལ་བྱེད་ཀྱི་བྱ་བས་དོན་ལ་དམིགས་པར་བྱེད་པ་དག་མ་ཡིན་ཏེ། འགའ་ཞིག་ན་གསལ་བྱེད་ཡོད་དུ་ཟིན་ཀྱང་བུམ་པ་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 2020]
དེའི་བྱ་བ་ལས་སྒྲ་ངེས་པར་དམིགས་པ་དེས་དེ་བྱུང་བར༌[^1472]འགྱུར་རོ། །

[Block 2021]
བྱེད་པ་པོ་མ་ཡིན་པའི་བྱ་བ་དེ་ཡོད་ན་ཡང་དེ་གྲུབ་པ༌[^1473]མི་རུང་བའི་ཕྱིར་རོ། །

[Block 2022]
གལ་ཏེ་ཁྱབ་པ་དང་རྟག་པ་ཉིད་ཀྱི་ཕྱིར་དམིགས་པ་ཡིན་ནོ་ཞེ་ན། ད་ནི་བུམ་པ་ལ་སོགས་པ་དག་ལ་ངེས་པ་ཅི་ཡོད། གལ་ཏེ་དེ་དག་དེ་ལྟར་མི་འདོད་དོ་ཞེ་ན། དེ་དང་ཆོས་མཐུན་པ་ཉིད་ཅན་གྱི་སྒྲ་ཅིའི་ཕྱིར་འདོད། །འདི་ལ་ཕུལ་དུ་བྱུང་བ་ཅུང་ཞིག་ཀྱང་མེད་དོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 2023]
ཁྱབ་པར་བྱེད་པ་དང་རྟག་པ་ཉིད་ཀྱང་བཀག་ཟིན་ཏོ། །

[Block 2024]
བུམ་པ་ལ་སོགས་པ་དག་ལ་གསལ་བྱེད་ཀྱི་ཁྱད་པར་ཡོད་པའི་ཕྱིར། སྐྱོན་ཡོད་པ་མ་ཡིན་ཏེ། དེ་དག་གི་གསལ་བྱེད་གྲགས་པ་དང་། རྫ་མཁན་ལ་སོགས་པ་དག་གསལ་བྱེད་ཉིད་ཡིན་ན། དེ་འདྲ་བ་ཉིད་དུ་འགྱུར་བ་ན་ཁྱད་པར་དུ་བྱས་པར་འགྱུར་བ༌[^1474]གསལ་བྱེད་ཀྱི་ཁྱད་པར་དེ་ལས་བྱེད་པ་པོ་ཡིན་ཏེ། ཕན་འདོགས་པ༌[^1475]བྱེད་པ་ལ་རྣམ་པ་གཞན་མེད་པའི་ཕྱིར་རོ། །

[Block 2025]
དེ་དང་དེ་ནི་སྒྲ་དག་ལ་ཡང་མཚུངས་སོ། །

[Block 2026]
དེ་ལ་ཡང་དབང་པོ་དང་ཡུལ་རུང་བ་ལ་སོགས་པ་དག་ལས་བྱེད་པ་རྣམས་ཕུལ་དུ་བྱུང་བའི་ཕྱིར་རོ། །

[Block 2027]
བྱེད་པ་དག་ལ་ཡང་བུམ་པ་ལ་སོགས་པའི་བྱེད་པ་པོའི་ཆོས་ཀྱང་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2028]
སྒྲོན་མ་ལ་སོགས་པ་དེ་ཉིད་དང་ཡུལ་གཞན་འགའ་ཞིག་ལ་གསལ་བྱེད་གཞན་མེད་པའི་ཕྱིར་དེ་དག་གི་རྒྱུ་དག༌[^1476]ཀྱང་དེ་དག་གསལ་བྱེད་དུ་འགྱུར་རོ། །

[Block 2029]
དེ་བས་ན་སྒྲ་གསལ་བ་མ་ཡིན་ནོ། །

[Block 2030]
འགྱུར་ན་ཡང་བྱེད་པ་དག་ལས་སྒྲ་ཕུལ་དུ་བྱུང་བ་དང་ལྡན་པའམ། སྒྲིབ་པར་བྱེད་པ་དང་བྲལ་བའམ། རྣམ་པར་ཤེས་པ་གསལ་བ་ཡིན་ཏེ། རྣམ་པ་གཞན་མེད་པའི་ཕྱིར་རོ། །

[Block 2031]
དེ་ལ་ཕུལ་དུ་བྱུང་བ་བསྐྱེད་པ་ནི་མ་ཡིན་ཏེ། མི་རྟག་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2032]
དེ་ནི་ངོ་བོ་སྔ་མ་དང་ཕྱི་མ་ཉམས་པ་དང་སྐྱེ་བའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2033]
ཅི་སྟེ།

[Block 2034 [VERSE]]
གལ་ཏེ་ཁྱེད་ཀྱི་དེ་ངོ་བོའི། །
སྒྲིབ་བྱེད་བྲལ་བ་གསལ་ཡིན་ནའང་། །
ཅི་ཕྱིར༌[^1477]མེད་པ་ལ་མེད་པའི། །
ཚོགས་ཀྱི་ནུས་པ་དེ་རུང་འགྱུར། །

[Block 2035]
སྒྲིབ་པར་བྱེད་པ་ཅུང་ཞིག་ཀྱང་མི་བྱེད་པ་ནུས་པ་ཞེས་བྱ་བ་མེད་དོ། །
--- END BLOCKS ---
