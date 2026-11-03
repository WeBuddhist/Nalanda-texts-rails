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
དེ་དག༌[^1467]ལས་ཀྱང་། གསུམ་རྣམ་གཉིས། རྨུགས་པ་དང་། རྒོད་པ་དང་། གཉིད་རྣམས་ནི་མི་དགེ་བ་དང་།

[Block 1997 [VERSE]]
ལུང་དུ་མ་བསྟན་པ་དག་ཡིན་ནོ། །
དེ་ཡན་ཆད་ནི་ལུང་མ་བསྟན། །

[Block 1998]
འདོད་པའི་ཁམས་ཡན་ཆད་ཀྱི་ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་ནི་ཅི་རིགས་པར་ལུང་དུ་མ་བསྟན་པ་དག་ཡིན་ནོ། །

[Block 1999 [HEADING]]
##### ཉེ་བའི་ཉོན་མོངས་པ་དུ་ཞིག་གང་ན་ཡོད་པ། ^2-28-4-3-0

[Block 2000]
དེ་དག་ལས་དུ་ཞིག་གང་ན་ཡོད་པར་རིག་པར་བྱ་ཞེ་ན། འདོད་དང་བསམ་གཏན་དང་པོ་ན། །གཡོ་སྒྱུ། འདི་གཉིས་ནི་འདོད་པའི་ཁམས་དང་། བསམ་གཏན་དང་པོ་ན་ཡོད་དོ། །

[Block 2001]
ཚངས་པའི་འཇིག་རྟེན་ན་སྒྱུ་ཇི་ལྟར་ཡོད་ཅེ་ན། ཚངས་པས་འདྲིད་ཕྱིར་རོ། །

[Block 2002]
ཚངས་པ་ཆེན་པོ་དེ་ནི༌[^1468]བདག་ཉིད་ལོག་པར་ཀུན་དུ་སྟོན་པས་ཚེ་དང་ལྡན་པ་རྟ་ཐུལ་ལ་འདྲེད་པར༌[^1469]ཞུགས་སོ། །

[Block 2003]
གཡོ་ནི་བཤད་ཟིན་མོད་ཀྱི་ཞར་ལ་འོངས་པས༌[^1470]སྨོས་སོ། །

[Block 2004]
རྨུགས་རྒོད་རྒྱགས་པ་ཁམས་གསུམ་ན། །གསུམ་པོ་འདི་དག་ནི་ཁམས་གསུམ་པོ་དག་ཡིན་ནོ། །

[Block 2005]
གཞན་དག་ན༌[^1471]འདོད་ཁམས་ལས་སྐྱེས་པ། བཅུ་དྲུག་ལས་ལྔ་བོར་ཏེ། ཉེ་བའི་ཉོན་མོངས་པ་བཅུ་གཅིག་ནི་འདོད་པ་ན་སྤྱོད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2006]
ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 2007 [HEADING]]
### ཡིད་ཀྱི་ས་པ་དང་རྣམ་པར་ཤེས་པ་དྲུག་གི་ས་པ། ^2-29-0

[Block 2008]
ཡང་དེ་རྣམས་ལས་ཡིད་ཀྱི་ས་པ་ནི་དུ་ཞིག་ཡིན། རྣམ་པར་ཤེས་པ་དྲུག་གི་ས་པ་ནི་དུ་ཞིག་ཡིན་ཞེ་ན། མདོར་བསྡུ་ན།

[Block 2009 [VERSE]]
མཐོང་སྤང་བྱ་ཉིད༌[^1472]ང་རྒྱལ་བཅས། །
ཡིད་རྣམ་ཤེས་ཀྱི་ས་པ་ཡིན། །

[Block 2010]
མཐོང་བས་སྤང་བར་བྱ་བ་ཐམས་ཅད་ནི་ཡིད་ཀྱི་ས་པ་དག་ཡིན་ཏེ། གཉིད་དང་ང་རྒྱལ་བསྒོམ་པས་སྤང་བར་བྱ་བ་དང་ཡང་བཅས་པ་ཐམས་ཅད་ནི་ཡིད་ཀྱི་ས་པ་དག་ཡིན་ཏེ། [^1473]དེ་དག་ནི་ཐམས་ཅད་ཡིད་ཀྱི་ས་པ་དག་ཡིན་ནོ། །

[Block 2011]
ཉེ་བའི་ཉོན་མོངས་རང་དབང་ཡང་། །ཉོན་མོངས་པ༌[^1474]རང་དབང་ཅན་གང་དག་ཡིན་པ་དེ་དག་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་ཡང་ཡིད་ཀྱི་ས་པ་ཁོ་ན་ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 2012]
གཞན་ནི་རྣམ་ཤེས་དྲུག་རྟེན་ཅན། །ཉོན་མོངས་པ་དང་ཉེ་བའི་ཉོན་མོངས་པ་གཞན་དག་ནི་རྣམ་པར་ཤེས་པ་དྲུག་གི་ས་པ་དག་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2013]
གཞན་ཡང་གང་དག་ཅིག་ཡིན་ཞེ་ན། བསྒོམ་པས་སྤང་བར་བྱ་བའི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། མ་རིག་པ་རྣམས་དང་། དེ་དག་དང་མཚུངས་པར་ལྡན་པ་ཉེ་བའི་ཉོན་མོངས་པ་ངོ་ཚ་མེད་པ་དང་། ཁྲེལ་མེད་པ་དང་། རྨུགས་པ་དང་། རྒོད་པ་རྣམས་དང་། ཉོན་མོངས་པའི་ས་པ༌[^1475]མང་པོ་པ་དག༌[^1476]གི་ནང་དུ་བཤད་པ་གང་དག་ཡིན་པའོ། །

[Block 2014 [HEADING]]
### དབང་པོ་དང་མཚུངས་པར་ལྡན་པ། ^2-30-0

[Block 2015 [HEADING]]
#### ཉོན་མོངས་པ་རྣམས་དབང་པོ་དང་མཚུངས་པར་ལྡན་པ། ^2-30-1-0

[Block 2016]
བདེ་བ་ལ་སོགས་པའི་དབང་པོ་ལྔ་པོ༌[^1477]གང་དག་ཡིན་པ། དེ་དག་ལས་དབང་པོ་གང་ཞིག་ཉོན་མོངས་པ་འམ། ཉེ་བའི་ཉོན་མོངས་པ་གང་དང་མཚུངས་པར་ལྡན་ཞེ་ན། བདེ་བ་དག་དང་འདོད་ཆགས་སུ། །མཚུངས་ལྡན། འདོད་ཆགས་ནི་བདེ་བ་དང་ཡིད་བདེ་བ་དག་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 2017]
ཞེ་སྡང་བཟློག་པའོ། །

[Block 2018]
སྡུག་བསྔལ་དག༌[^1478]དང་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། སྡུག་བསྔལ་དང་ཡིད་མི་བདེ་བ་དང་མཚུངས་པར་ལྡན་ཏེ། འདོད་ཆགས་དང་ཞེ་སྡང་དག་ནི་དགའ་བ་དང་སྐྱོ་བའི་རྣམ་པར་འཇུག་པའི་ཕྱིར་དང་། རྣམ་པར་ཤེས་པ་དྲུག་གི་ས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2019]
མ་རིག་པ་དག་ཐམས་ཅད་དང་། །མ་རིག་པ་རྣམས་ནི་ཉོན་མོངས་པ་ཐམས་ཅད་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་དབང་པོ་ལྔ་ཆར་དང་ཡང་མཚུངས་པར་ལྡན་ནོ། །

[Block 2020]
མེད་ལྟ་ཡིད་བདེ་སྡུག་བསྔལ་དང་། །ཡིད་སྡུག་བསྔལ་བ་ནི་ཡིད་མི་བདེ་བའོ། །

[Block 2021]
ཡིད་བདེ་བ་ནི་ཡིད་བདེ་བ་སྟེ། ལོག་པར་ལྟ་བ་ནི་དེ་དག་དེ༌[^1479]དང་མཚུངས་པར་ལྡན་ཏེ། བསོད་ནམས་ཀྱི་ལས་ཅན་རྣམས་དང་། སྡིག་པའི་ལས་ཅན་རྣམས་ཀྱི་དང་གོ་རིམས་བཞིན་ནོ། །

[Block 2022]
ཡིད་མི་བདེ་བ༌[^1480]དང་ཐེ་ཚོམ་མོ། །

[Block 2023]
ཐེ་ཚོམ་ཟོས་པ་ངེས་པ་དོན་དུ་གཉེར་བ་ན། ཡིད་མི་བདེ་བར་འགྱུར་རོ། །

[Block 2024]
གཞན་ཡིད་བདེ༌[^1481]དང་། ཕྲ་རྒྱས་གཞན་དག་ནི་ཡིད་བདེ་བ་ཁོ་ན་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 2025]
གཞན་ཡང་གང་དག་གཅིག་ཡིན་ཞེ་ན། ལྟ་བ་བཞི་དང་། ང་རྒྱལ་ཏེ། དགའ་བའི་རྣམ་པར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 2026]
ཕྲ་རྒྱས་སུ་བཤད་པ་དེ་དག་ཅི་ཞིག༌[^1482]དང་ལྡན་ཞེ་ན། འདོད་ལས་སྐྱེས། དེ་ལྟར་ན༌[^1483]མཚུངས་པར་ལྡན་པ་སོ་སོར་ངེས་པ་བཤད་ནས་སྤྱིར་སྨྲས་པ། བཏང་སྙོམས་དང་ཀུན། ཕྲ་རྒྱས་འདི་དག་ཐམས་ཅད་ནི་བཏང་སྙོམས་ཀྱི་དབང་པོ་དང་མཚུངས་པར་ལྡན་ཏེ། ཉོན་མོངས་པ་རྣམས་ཀྱི་རྒྱུན་འཆད་པའི་དུས་ན་གདོན་མི་ཟ་བར་བཏང་སྙོམས་ཀུན་དུ་གནས་སོ་ཞེས་གྲག་གོ། །

[Block 2027]
ཡང་ས་གོང་མ་པ་རྣམས་ཇི་ལྟ་བུར་ཞེ་ན། ས་གོང་མ་རྣམས། [^1484]ས་ཇི་བཞིན་དུ་རང་རང་དང་། །ས་གོང་མའི་ཕྲ་རྒྱས་རྣམས་ནི་ས་གང་ན་དབང་པོ་ཇི་སྙེད་ཅིག༌[^1485]ཡོད་པ་རང་རང་གི་དབང་པོ་རྣམས་དང་མཚུངས་པར་ལྡན་ཏེ། དེ་ན་ཡང་ཅི་རིགས་པར་རྣམ་པར་ཤེས་པའི་ཚོགས་བཞི་པ་རྣམས་ནི་རྣམ་པར་ཤེས་པའི་ཚོགས་བཞི་པ་རྣམས་དང་མཚུངས་པར་ལྡན་ལ་ཡིད་ཀྱི་ས་པ་རྣམས་ནི་ཡིད་ཀྱི་ས་པ་རྣམས་ཁོ་ན་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 2028]
ཉོན་མོངས་པ་རྣམས་དབང་པོ་དང་མཚུངས་པར་ལྡན་པ་བཤད་ཟིན་ཏོ། །

[Block 2029 [HEADING]]
#### ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་དབང་པོ་དང་མཚུངས་པར་ལྡན་པ། ^2-30-2-0

[Block 2030]
ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་ལས།

[Block 2031 [VERSE]]
འགྱོད་དང་ཕྲག་དོག་ཁོང༌[^1486]ཁྲོ༌[^1487]དང་། །
རྣམ་འཚེ་ཁོན་དུ་འཛིན་པ་དང་། །
འཆབ་པ༌[^1488]ཡིད་མི་བདེ་བ་དང་། །

[Block 2032]
མཚུངས་པར་ལྡན་པ༌[^1489]ཞེས་བྱ་བར་སྦྱར་ཏེ། འདི་དག་ནི་སྐྱོ་བའི་རྣམ་པར་འཇུག་པའི་ཕྱིར་དང་ཡིད་ཀྱི་ས་པ་ཡིན་པའི་ཕྱིར་དང་།[^1490] སེར་སྣ་དག་གི༌[^1491]བཟློག་པ་ཡིན། །ཡིད་བདེ་བ་དང་མཚུངས་པར་ལྡན་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2033]
[^1492]ཆགས་པའི་རྒྱུ་ལས་བྱུང་བ༌[^1493]དགའ་བའི་རྣམ་པར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 2034]
གཡོ་དང་སྒྱུ་དང་རྒྱགས་འཆབ་གཉིད།[^1494] །གཉི་ག་དང་ལྡན། ཡིད་བདེ་བ་དང་ཡིད་མི་བདེ་བ་དག་དང་མཚུངས་པར་ལྡན་ཏེ། རེས་འགའ་ནི་ཡིད་བདེ་བ་དག་གིས་ཕ་རོལ་པོ་འདྲིད་པར་བྱེད་ལ། རེས་འགའ་ནི་ཡིད་མི་བདེ་བ་དག་གིས་ཏེ། གཉིད་ཀྱི་བར་དུ་ཡང་དེ་དང་འདྲའོ། །

[Block 2035]
བདེ་དག་དང་། རྒྱགས་པ། བསམ་གཏན་གསུམ་པ་ན་ནི་བདེ་བ་དང་མཚུངས་པར་ལྡན་ནོ། །
--- END BLOCKS ---
