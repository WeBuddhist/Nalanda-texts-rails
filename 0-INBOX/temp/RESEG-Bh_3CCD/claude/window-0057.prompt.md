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
གང་གི་ཚེ། བསྐྱེད་པའི་རིམ་པ་དང་པོ་ཡིན། །ཞེས་དང་པོ་བསྐྱེད་པའི༌[^1356]རིམ་པ་བསྒོམ་པ༌[^1357]ཡིན་ན་དེའི་ཚེ་གཅིག་ཅེས༌[^1358]སྨྲས་པས།[^1359] རྡོ་རྗེ་བཟླས་པའི་རིམ་པའི་འོག་ཏུ་སེམས་ལ་དམིགས་པ་ཙམ་ཞིག་ནི་རིམ་པ་གཉིས་པ་ཞེས་བརྗོད་དོ་ཞེས་སྨྲས་པར༌[^1360]མི་རིགས་ཏེ། རྡོ་རྗེ་བཟླས་པའི་འོག་ཏུ་དེ་ཉེ་བར་བསྟན་པ་ཡིན་གྱི་བསྐྱེད་པའི་རིམ་པའི་འོག་ཏུ་ནི་མ་ཡིན་ནོ། །

[Block 1997]
དེའི་ཕྱིར་གསང་སྔགས་ཀྱི་སྐུ་རབ་ཏུ་སྒྲུབ་པར་བྱེད་པའི་སྒྲ་ནི་བསྐྱེད་པའི་རིམ་པའི་ཁྱད་པར་མ་ཡིན་ཏེ་འོན་ཀྱང་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་ཁོ་ན་སྟོན་པར་བྱེད་པའོ། །

[Block 1998]
དེའི་ཁྱད་པར་བྱེད་པའི་ཕྱིར་གཅིག་ཅེས་སྨྲ་བར་བྱ་བ༌[^1361]ཁོ་ནའོ། །

[Block 1999]
ཇི་ལྟར་རིམ་པ་ཁོ་ན་མཆོག་གོ། །

[Block 2000]
སེམས་ལ་དམིགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ངག་རྣམ་པར་དག་པར་གྱུར་པས་རྣམ་པར་ཤེས་པ་གསུམ་གྱི་བདག་ཉིད་ཀྱི་སེམས་ལ་དམིགས་པ་ནི་མཐོང་བ་སྟེ། སྔར་བཤད་པའི་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་འོད་གསལ་བར་བྱའོ། །

[Block 2001]
དེ་ཉིད་ནི་དེ་ཙམ་ཞིག་ཡིན་གྱི་སྔགས་ཀྱི་སྐུའི་བདག་ཉིད་གཞན་ནི་མ་ཡིན་ནོ། །

[Block 2002]
སེམས་རྣམ་པར་དག་པ་ཙམ་གཅིག་པུ་རིམ་པ་གཉིས་པ་ཡིན་ཞེས་ཚིག་གི་དོན་ཏོ། །

[Block 2003]
རྣམ་པར་དག་པའི་སེམས་ཀྱི་རྒྱུད་དང་ལྡན་པའི་རྣལ་འབྱོར་པས་གཞན་གྱི་དོན་བྱ་བའི་ཕྱིར། ལྷའི་སྐུ་ཡིད་ཀྱི་རང་བཞིན་གྱིས་ཆོས་ཐམས་ཅད་སྒྱུ་མ་ལྟ་བུར་བལྟ་བར༌[^1362]བྱ་ཞེས་དེའི་སླད་དུ། ཀུན་རྫོབ་བདེན་པ་བསྟན་པ་ནི། །ཞེས་བྱ་བ་སྨོས་ཏེ། འོད་གསལ་བ་ལས་མྱུར་བར་རྣམ་པ་ཐམས་ཅད་ཀྱི་མཆོག་དང་ལྡན་པ་ཡིད་དུ་འོང་བ་ནི་དཀྱིལ་འཁོར་པའི་ལྷ་ཚོགས་ཀྱིས་ཡོངས་སུ་བསྐོར་བ། མི་ངོམས་པའི་གཟུགས་ཡེ་ཤེས་ཀྱི་སྐུ་སྤྲས་ཏེ་གནས་པ་བསྟན་པ་ནི་སྒྱུ་མ་དང་མཚུངས་པར་བདག་དང་དངོས་པོ་ཐམས་ཅད་ལ་བལྟའོ། །

[Block 2004]
ཡང་ན་ཡིད་འོང་ནི་བསྟན་པ་དང་དགེ་བའི་རྩ་བ་སྨིན་པ་དང་རྣམ་པར་གྲོལ་བ་དང་། སྤྲོ་བའི་རིམ་པས་འགྲོ་བའི་དོན་བྱེད་པས་སོ། །

[Block 2005]
དེ་བས་ན་བདག་བྱིན་གྱིས་རློབ་པ་ཞེས་བྱ་བ་རིམ་པ་གསུམ་པ་བསྟན༌[^1363]ཏོ། །

[Block 2006]
སྒྱུ་མ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་མངོན་དུ་བྱས་ནས་དེ་ཉིད་དུ་མངོན་པར་ཞེན་པར་བརྒྱ་ལམ་དུ་འགྱུར་བས་དེ་དག་པར༌[^1364]བྱ་བའི་ཕྱིར། ཀུན་རྫོབ་བདེན་པའི་དག་པ་ནི། །ཞེས་སྨོས་ཏེ་ཀུན་རྫོབ་ཀྱི་བདེན་པ་ནི་སྒྱུ་མ་ལྟ་བུར་མཐོང་བ་དེའི་དག་པ་གང་ཡིན་པ་ཐམས་ཅད་སྟོང་པ་ལ་འཇུག་པ༌[^1365]སྟེ་འོད་གསལ་བ་རྟོགས་པའོ། །

[Block 2007]
དེ་ནི་མངོན་པར་བྱང་ཆུབ་པ། །ཞེས་བྱ་བ་རིམ་པ་བཞི་པར་བཤད་དོ། །

[Block 2008]
འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་ཐོབ་པས་ཆད་པའི་ཕྱོགས་སུ་ལྷུང་བས་སྐྱོན་དེ་བསལ༌[^1366]བའི་ཕྱིར། བདེན་གཉིས་སྦྱོར་བ་གང་ཡིན་པ། ཞེས་སྨོས་ཏེ། བདེན་པ་གཉིས་ནི་ཀུན་རྫོབ་དང་དོན་དམ་པའི་བདག་ཉིད་ཡེ་ཤེས་ཀྱི་སྐུ༌[^1367]དང་འོད་གསལ་བའི་རྣམ་གྲངས་ཅན་བདག་ལ་བྱིན་གྱིས་རློབ་པ་དང་། མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་གཉིས་དང་། དེ་བཞིན་དུ་ཕན་ཚུན་འགལ་བའི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ལ་སོགས་པའི་ཆོས་རྣམས་ལ་སྦྱོར་བ་ནི་གཅིག་ཏུ་བྱེད་པ་སྟེ་གཉིས་སུ་མེད་པར་ཡོངས་སུ་ཤེས་པ་གང་ཡིན་པ་དེ་ཟུང་དུ་འཇུག་པའོ། །

[Block 2009]
ཟུང་ནི་དངོས་པོ་དང་དངོས་པོ་མེད་པ་ལ་སོགས་པའི་བདག་ཉིད་དུ་འཇུག་པ་ནི་དབྱེར་མེད་པའོ་ཞེས་རིམ་པ་ལྔ་པར་ཤེས་པར་བྱའོ། །

[Block 2010]
དེ་ལས་གཞན་པའི་རིམ་པ་མེད་དེ་བྱ་བ་མེད་པའི་ཕྱིར་དང་མི་སློབ་པའི་ཕྱིར་རོ། །

[Block 2011]
གྲངས་ལ་ལོག་པར་རྟོགས་པ་ལ་སོགས་པ་སྔོན་དུ་བཤད་ཟིན་ཏོ། །

[Block 2012]
བསྡུས་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། འདི་ནི་སྒྲུབ་པའི་ཡན་ལག་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། སྒྲུབ་པ་ནི་ལྷའི་རྣལ་འབྱོར་གཉིས་ཏེ། བརྟགས་པ་དང་ཡོངས་སུ་རྫོགས་པའོ། །

[Block 2013]
དེ་ལ་བརྟགས་པ་ནི་ཏིང་ངེ་འཛིན་གསུམ་གྱི་བདག་ཉིད་དོ། །

[Block 2014]
ཡོངས་སུ་རྫོགས་པ་ནི་རིམ་པ་ལྔའི་བདག་ཉིད་དོ། །

[Block 2015]
དེ་དག་གི་ཡན་ལག་ནི་བྱེ་བྲག་སྟེ། ཏིང་ངེ་འཛིན་གསུམ་དང་རིམ་པ་ལྔའོ། །

[Block 2016]
དེ་ཉིད་ཀྱི་ཕྱིར་མཆོག༌[^1368]ཅེས་སྨོས་ཏེ། གཞན་ལ་ལྟོས་པ་མེད་པ་སྟེ། བདག་དང་གཞན་གྱི་དོན་བྱེད་ནུས་པའི་ཕྱིར་རོ། །

[Block 2017]
དེ་བཞིན་དུ་ཡང་རྒྱུད་ཀུན་གྱི༌[^1369]དོན་ཞེས་བྱ་བ་ནི་དཔལ་གསང་བ་འདུས་པ་མ་ལུས་པའི་བརྗོད་པར་བྱ་བ་གང་ཡིན་པ་དེ་བསྡུ༌[^1370]བར་བྱེད་པ་ནི་རིམ་པ་གཉིས་པོ་ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 2018]
ལ་ལ་ན་རེ་བསྙེན་པ་ལ་སོགས་པ་ཡན་ལག་བཞི་དང་ལྡན་པ་རྒྱུད་ཀྱི་དོན་དུ་འཆད་པ་དེ་རྣམས་ཀྱིས་རྫོགས་པའི་རིམ་པ་མ་བཟུང༌[^1371]སྟེ། དཔལ་སངས་རྒྱས་ཡེ་ཤེས་ཞབས་ཀྱི་གཞུང་བཞིན་ནོ། །

[Block 2019]
གང་ཡང་རྡོ་རྗེ་བཞི་པོས་རྒྱུད་ཀྱི་དོན་བཤད་པར༌[^1372]བྱེད་པ་དེ་རྣམས་ཀྱི་བསྐྱེད་པའི་རིམ་པའི་རིམ་པ༌[^1373]ཙམ་ཡང་ཡོངས་སུ་མ་རྫོགས་པའོ། །

[Block 2020]
ཇི་སྐད་དུ།

[Block 2021 [VERSE]]
དང་པོ་སྟོང་ཉིད་བྱང་ཆུབ་སེམས། །
གཉིས་པ་ས་བོན་བསྡུ་བ་སྟེ། །
གསུམ་པ་གཟུགས་བརྙན་རྫོགས་པ་ནི། །
ཡི་གེ་དགོད་པ་བཞི་པའོ། །

[Block 2022]
ཞེས་བྱ་བས་སྦྱོར་བ་དང་པོ་ཏིང་ངེ་འཛིན་ཁོ་ན་གཟུང་བ་ཡིན༌[^1374]ནོ། །

[Block 2023]
ཁོ་བོས་ནི་ཇི་ལྟར་གྱུར་པ་དེ་བཞིན་དུ༌[^1375]འོག་ནས་བཤད་པར་བྱའོ། །

[Block 2024]
ད་ནི་རིམ་པ་གཉིས་ཀྱི་ནང་ནས་རྫོགས་པའི་རིམ་པ་རྒྱས་པ་དང་མདོར་བསྡུས་པར་རྟོགས་པར་བྱེད་པས་རྒྱུད་ཤེས༌[^1376]པ་ཡིན་གྱི་གཞན༌[^1377]གྱིས་མ་ཡིན་ཞེས་དགོངས་ནས། རིམ་པ་འདིའི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དེའི་སྔོན་དུ་བཤད་པའི་རིམ་པ་རྣམས་ཀྱིའོ། །

[Block 2025]
སྤྲོས་པའི་རིམ་པ་ནི་རྒྱ་ཆེ་བའི་རིམ་པས་སོ། །

[Block 2026]
རྣམ་པ་མང་བ་ནི་བཤད་པར་བྱ་སྟེ། འདི་ལྟ་སྟེ། རྡོ་རྗེ་བཟླས་པ་ནི་རྣམ་པ་བཅུ་གཅིག་སྟེ། རྡོ་རྗེ་འཆང་ཆེན་པོའི་བཟླས་པ་དང་། སྐུའི་བཟླས་པ་དང་། གསུང་གི་བཟླས་པ་དང་། ཐུགས་ཀྱི་བཟླས་པ་དང་། རིན་པོ་ཆེའི་བཟླས་པ་དང་། དོན་ཡོད་པའི་བཟླས་པ་དང་། ཁྲོ་བོའི༌[^1378]བཟླས་པ་དང་། ཞེ་སྡང་གི་བཟླས་པ་དང་། འདོད་ཆགས་ཀྱི་བཟླས་པ་དང་། གཏི་མུག་གི་བཟླས་པ་དང་། མ་ནིང་གི་བཟླས་པའོ། །

[Block 2027]
སེམས་རྣམ་པར་དག་པ་ལ་གསུམ་སྟེ། སྣང་བ་རྣམ་པར་དག་པ་དང་། སྣང་བ་མཆེད་པ་རྣམ་པར་དག་པ་དང་། སྣང་བ་ཉེ་བར་ཐོབ་པ་རྣམ་པར་དག་པའོ། །

[Block 2028]
བདག་ལ་བྱིན་གྱིས་རློབ་པ་ལ་གསུམ་སྟེ། ཆོས་ཀྱི་སྐུར་བྱིན་གྱིས་རློབ་པ་དང་། ལོངས་སྤྱོད་རྫོགས་པའི་སྐུར་བྱིན་གྱིས་རློབ་པ་དང་། སྤྲུལ་པའི་སྐུར་བྱིན་གྱིས་རློབ་པའོ། །

[Block 2029]
མངོན་པར་བྱང་ཆུབ་པ་ལ་རྣམ་པ་གསུམ་སྟེ། ཆགས་པ་རྣམ་པར་དག་པ་དང་། ཆགས་བྲལ་རྣམ་པར་དག་པ་དང་། ཆགས་པ་བར་མ་རྣམ་པར་དག་པའོ། །

[Block 2030]
ཟུང་དུ་འཇུག་པ་ལ་གཉིས་ཏེ། རྒྱུའི་ཟུང་དུ་འཇུག་པ་དང་། འབྲས་བུའི་ཟུང་དུ་འཇུག་གོ། །

[Block 2031]
རྒྱུའི་ཟུང་དུ་འཇུག་པ༌[^1379]ལ་བཞི་སྟེ། ཉན་ཐོས་དང་། རྣལ་འབྱོར་སྤྱོད་པ་དང་། དབུ་མ་དང་། སྔགས་ཀྱི་དབྱེ་བས་སོ། །

[Block 2032]
འབྲས་བུ་ལ༌[^1380]ཡང་བཞི་སྟེ། རིགས་དང་། ཡོན་ཏན་དང་། བྱ་བ་དང་། རྫས་ཀྱི་བྱེ་བྲག་གིས་སོ། །

[Block 2033]
ཀུན་ཏུ་བསྡུས་པས་དབྱེ་བ་ཉི་ཤུ་རྩ་བརྒྱད་ཀྱི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 2034]
དེ་རྣམས་ཀྱི་དོན་ནི་སྔོན་དུ་བཤད་ཟིན་ཏོ། །

[Block 2035]
དེ་བཞིན་དུ་ཡང་ཕུང་པོ་ལྔ་དང་འབྱུང་བ་ཆེན་པོ་དང་རྣམ་པར་ཤེས་པ་དང་། དབང་བསྐུར་བ་དང་། ལམ་དང་དེ་བཞིན་གཤེགས་པ་དང་། ཡེ་ཤེས་ལྔའི་ངོ་བོ་ཉིད་རིམ་པ་ལྔའོ། །
--- END BLOCKS ---
