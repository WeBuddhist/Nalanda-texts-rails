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
གང་གི་མིག་གི་སྐྱེ་མཆེད་ཡིན་པ་དེའི་ནི་བཞི་སྟེ། མིག་དང་ལུས་དང་རེག་བྱ་དང་ཆོས་ཀྱི་སྐྱེ་མཆེད་རྣམས་སོ། །

[Block 1997]
གང་གི་རྣ་བ་དང་། སྣ་དང་། ལྕེའི་སྐྱེ་མཆེད་དག་ཡིན་པ་ཡང་དེ་དང་འདྲའོ། །

[Block 1998]
གང་གི་རྣམ་པར་སྨིན་པ་ལྔ་དང་། དྲུག་དང་། བདུན་དང་། བརྒྱད་དང་། དགུ་དང་། བཅུ་དང་། བཅུ་གཅིག་སྨིན་པར་འགྱུར་བའི་ལས་དེ་ཡང་ཡོད་དེ། ལས་ཀྱི་འབྲས་བུ་སྣ་ཚོགས་དང་། སྣ་ཚོགས་མ་ཡིན་པའི་ཕྱིར་ཕྱིའི་ས་བོན་བཞིན་ནོ། །

[Block 1999]
དཔེར་ན་ཕྱིའི་ས་བོན་རྣམས་ལ༌[^1015]ཁ་ཅིག་ནི་འབྲས་བུ་སྣ་ཚོགས་པ་ཡིན་ཏེ། འདི་ལྟ་སྟེ་པདྨ་དང་། བལ་པོ་སེའུ་དང་། ཤིང་ནྱ་གྲོ་དྷ་ལ་སོགས་པ་དག་གི་ལྟ་བུའོ། །

[Block 2000]
ཁ་ཅིག་ནི་འབྲས་བུ་སྣ་ཚོགས་པ་མ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། ནས་དང་གྲོ་ལ་སོགས་པ་དག་གི་ལྟ་བུའོ། །

[Block 2001]
ལས་དུས་གཅིག་པའི་རྣམ་པར་སྨིན་པ་དུས་གསུམ་པ་རྣམ་པར་སྨིན་པ་ནི་མི༌[^1016]འགྱུར་གྱི་ལས་དུས་གཉིས་པའི་ཡང༌[^1017]དུས་གཅིག་པ་ནི་མ་ཡིན་ཏེ། རྒྱུ་བས་འབྲས་བུ་ཧ་ཅང་ཉུང་བར་འགྱུར་དུ་འོང་བའི་ཕྱིར་རོ། །

[Block 2002]
དེ་བཞིན་དུ་སྐད་ཅིག་མ་གཅིག་པའི་སྐད་ཅིག་མ་དུ་མ་པ་ནི་ཡིན་གྱི་བཟློག་པ་ནི་མ་ཡིན་ནོ། །

[Block 2003]
རྣམ་པར་སྨིན་པ་ནི་ལས་དང་ལྷན་ཅིག་ཏུ་རྣམ་པར་སྨིན་པ༌[^1018]ཡང་མ་ཡིན་ལ་མཇུག་ཐོགས་སུ་ཡང་མ་ཡིན་ཏེ། མཇུག་ཐོགས་ཀྱི་སྐད་ཅིག་མ་ནི་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་གྱིས་དྲངས་པའི་ཕྱིར་རོ། །

[Block 2004]
རྣམ་པར་སྨིན་པའི་རྒྱུ་ལས་འབྲས་བུ་སྨིན་པ་ནི་རྒྱུ་ལ་ལྟོས་པ་ཡིན་ནོ། །

[Block 2005 [HEADING]]
##### རྒྱུ་འདི་དག་གི་དུས་ངེས་པ། ^2-4-1-2-0

[Block 2006]
ཡང་རྒྱུ་འདི་དག་གི་དུས་ངེས་པ་གང་ཞེ་ན། འདི་དག་གི་དུས་ངེས་པར༌[^1019]དོན་གྱིས་ནི་བཤད་མོད་ཀྱི་མདོར་བྱས་ནས་མ་བཤད་པས། དེའི་ཕྱིར་མདོར་བྱས་ཏེ། ཀུན་འགྲོ་སྐལ་མཉམ་དུས་གཉིས་པ་དང་། འདས་པ་དང་ད་ལྟར་བྱུང་བ་ཁོ་ན་ཡིན་གྱི་མ་འོངས་པ་དག་ནི་མེད་དོ། །

[Block 2007]
འདིར་གཏན་ཚིགས་ནི་བཤད་ཟིན་ཏོ། །

[Block 2008]
གསུམ་པོ་དག་ནི་དུས་གསུམ་པ། །ལྷན་ཅིག་འབྱུང་བ་དང་མཚུངས་པར་ལྡན་པ་དང་རྣམ་པར་སྨིན་པའི་རྒྱུ་དག་ནི་དུས་གསུམ་པ་ཡིན༌[^1020]ནོ། །

[Block 2009]
བྱེད་རྒྱུའི་རྒྱུ་ནི་དུས་ངེས་པ་མ་བསྟན་པས་དུས་ཐམས་ཅད་པ་དང་། དུས་དང་བྲལ་བར་ཡང་རིག་པར་བྱའོ། །

[Block 2010]
རྒྱུ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 2011 [HEADING]]
#### འབྲས་བུ་རྣམས། ^2-4-2-0

[Block 2012]
རྒྱུ་དེ་དག་གང་གི་ཡིན་པའི༌[^1021]འབྲས་བུ་དེ་དག་གང་ཞེ་ན།

[Block 2013 [HEADING]]
##### འབྲས་བུའི་ཆོས་རྣམས། ^2-4-2-1-0

[Block 2014]
འདུས་བྱས་བྲལ་བཅས་འབྲས་བུ་ཡིན། །བསྟན་བཅོས་ལས།

[Block 2015]
འབྲས་བུའི་ཆོས་རྣམས་གང་ཞེ་ན། འདུས་བྱས་ཀྱི་ཆོས་ཐམས་ཅད་དང་། སོ་སོར་བརྟགས་པས་འགོག་པའོ༌[^1022]ཞེས་འབྱུང་བའོ། །

[Block 2016]
དེ་ལྟ་ན་འོ་ན་ནི་འདུས་མ་བྱས་འབྲས་བུ་ཡིན་པའི་ཕྱིར་དེ་གང་གི་འབྲས་བུ་ཡིན་པའི་རྒྱུར་ཡང་འགྱུར་ལ། རྒྱུ་ཡིན་པའི་ཕྱིར་དེ་གང་གི་རྒྱུ་ཡིན་པའི་འབྲས་བུར་ཡང་འགྱུར་རོ། །

[Block 2017]
འདུས་བྱས་ཁོ་ན་ལ་རྒྱུ་དང་འབྲས་བུ་དག་ཡོད་ཀྱི། འདུས་མ་བྱས་ལ་དེ་དག་མེད། །ཅིའི་ཕྱིར་ཞེ་ན། རྒྱུ་རྣམ་པ་དྲུག་མི་སྲིད་པའི་ཕྱིར་དང་། འབྲས་བུ་རྣམ་པ་ལྔ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 2018]
ཅིའི་ཕྱིར་ལམ་འབྲལ་བའི་བྱེད་རྒྱུའི་རྒྱུར་མི་འདོད་ཅེ་ན། འདི་ལྟར་དེ་ནི་སྐྱེ་བ་ལ་བགེགས༌[^1023]མི་བྱེད་པའི་ངོ་བོར་རྣམ་པར་གཞག་པ་ཡིན་ན་འདུས་མ་བྱས་ནི་སྐྱེ་བ་དང་ལྡན་པ་མ་ཡིན་ནོ། །

[Block 2019]
ད་ནི་དེ་གང་གིའམ་ཇི་ལྟར་ན་འབྲས་བུ་ཡིན་ཞེ་ན། ལམ་གྱི་འབྲས་བུ་ཡིན་ཏེ། དེའི་སྟོབས་ཀྱིས་འཐོབ༌[^1024]པའི་ཕྱིར་རོ། །

[Block 2020]
འོ་ན་ནི་དེ་དེ་ཁོ་ན་ལ་ནུས་པའི་ཕྱིར་ཐོབ་པ་ཁོ་ན་ལམ་གྱི་འབྲས་བུ་ཡིན་གྱི་བྲལ་བ་ནི་མ༌[^1025]ཡིན་ནོ། །

[Block 2021]
ཐོབ་པ་ལ་ཡང་དེའི་ནུས་པ་གཞན་ལ། བྲལ་བ་ལ༌[^1026]ཡང་གཞན་ཏེ། ཐོབ་པ་ལ་དེ་ཇི་ལྟར་ནུས་ཤེ་ན་བསྐྱེད་པའི༌[^1027]ཕྱིར་རོ། །

[Block 2022]
བྲལ་བ་ལ་ཇི་ལྟར་ཞེ་ན། ཐོབ་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2023]
དེ་ལྟ་བས་ན་རེ་ཞིག་ལམ་ནི་ཇི་ལྟར་ཡང་འདིའི་རྒྱུ་མ་ཡིན་གྱི་བྲལ་བ་ནི་འདིའི་འབྲས་བུ་ཡིན་ནོ། །

[Block 2024]
ཡང་བདག་པོའི་འབྲས་བུ་ཡང་མེད་ན་གོ་ཇི་ལྟར་ན་འདུས་མ་བྱས་བྱེད་རྒྱུའི་རྒྱུ་ཡིན་ཞེ་ན། སྐྱེ་བ་ལ་མི་སྒྲིབ་པའི་དངོས་པོས་བྱེད་རྒྱུའི་རྒྱུ་ཡིན་གྱི་འདི་ལ་འབྲས་བུ་ཡོད་པ་ནི་མ་ཡིན་ཏེ། དུས་ལས་གྲོལ་བ་ལ་འབྲས་བུ་འཛིན་པ་དང་། སྨིན་པའི་མཐུ་མེད་པའི་ཕྱིར་རོ། །

[Block 2025]
མདོ་སྡེ་པ་རྣམས་ན་རེ། བཅོམ་ལྡན་འདས་ཀྱིས་གང་ལས་ཀྱང་འདུས་མ་བྱས་རྒྱུ་ཡིན་ནོ་ཞེས་མ་གསུངས་ཀྱི། རྒྱུ་མ་ཡིན་ནོ་ཞེས༌[^1028]རྣམ་གྲངས་ཀྱིས་གསུངས་སོ།[^1029] །ཇི་ལྟར་གསུངས་ཤེ་ན། གཟུགས་སྐྱེད་པའི༌[^1030]རྒྱུ་གང་དག་ཡིན་པ་དང་། རྐྱེན་གང་དག་ཡིན་པ་དེ་དག་ཀྱང་མི་རྟག་པ་ཡིན་ན་རྒྱུ་དང་རྐྱེན་མི་རྟག་པ་དག་ལ་བརྟེན་ནས་བྱུང་བའི་གཟུགས་ལྟ་རྟག་པར་ག་ལ་འགྱུར། རྣམ་པར་ཤེས་པའི་བར་དུ་ཡང་དེ་དང་འདྲའོ་ཞེས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 2026]
དེ་ལྟ་ན་འོ་ན་ནི་འདུས་མ་བྱས་རྣམ་པར་ཤེས་པའི་དམིགས་པའི་རྐྱེན་དུ་ཡང་མི་འགྱུར་རོ། །

[Block 2027]
སྐྱེས་པའི༌[^1031]ཞེས་དཀར་བའི༌[^1032]ཕྱིར་འགྱུར་ཏེ། རྣམ་པར་ཤེས་པ་སྐྱེད་པའི༌[^1033]རྒྱུ་གང་དག་ཡིན་པ་དང་རྐྱེན་གང་དག་ཡིན་པ༌[^1034]དེ་དག་ཀྱང་མི་རྟག་ན་ཞེས་གསུངས་ཀྱི་རྣམ་པར་ཤེས་པའི་རྐྱེན་གང་དག་ཡིན་པ༌[^1035]དེ་དག་ཀྱང་མི་རྟག་ན་ཞེས་ནི་མི་གསུངས༌[^1036]སོ། །

[Block 2028]
རྒྱུ་རྣམས་ཀྱང་གང་དག་སྐྱེད་པའི་རྒྱུ་དེ་དག་ཁོ་ན་མི་རྟག་གོ་ཞེས་འབྱུང་བའི་ཕྱིར༌[^1037]འདུས་མ་བྱས་ཀྱང་མི་སྒྲིབ་པའི་དངོས་པོ་ཙམ་གྱིས་བྱེད་རྒྱུའི་རྒྱུ་ཉིད་དུ་མི་དགག་པ༌[^1038]ཡིན་ནམ། མདོ་ལས་དམིགས་པའི་རྐྱེན་ཡིན་པར་གསུངས་ཀྱི་མི་སྒྲིབ་པའི་རྒྱུ་ཡིན་པར་ནི་མ་གསུངས་པས། མདོ་ལས་འདུས་མ་བྱས་རྒྱུའི་དངོས་པོ༌[^1039]མི་འགྲུབ་བོ། །

[Block 2029]
མ་གསུངས་མོད་ཀྱི་བཀག་པ་ནི་མེད་དོ། །

[Block 2030]
མདོ་རྣམས་ཀྱང་ཕལ་ཆེར་ནུབ་ན་མ་གསུངས་སོ་ཞེས་བྱ་བ་འདི༌[^1040]ཇི་ལྟར་ངེས་པར་གཟུང་ཡང་བྲལ་བ་ཞེས་བྱ་བ་འདི་ཅི།[^1041] སྔར་སོ་སོར་བརྟགས་པས་འགོག་པ་ཡིན་ནོ་ཞེས་མ་བཤད་དམ། དེའི་ཚེ་ནི་སོ་སོར་བརྟགས་པས་འགོག་པ་གང་ཞེ་ན། གང་བྲལ་བའོ་ཞེས་བཤད།

[Block 2031]
ད་ནི་བྲལ་བ་གང་ཞེ་ན། གང་སོ་སོར་བརྟགས་པས་འགོག་པའོ་ཞེས་བཤད་པས་ཕན་ཚུན་རྟེན་པའི་བཤད་པ་འདི་ནི་དེའི་རང་གི་ངོ་བོ་གསལ་བར་བྱ་བ་ལ་ནུས་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་དེའི་རང་གི་ངོ་བོ་གཞན་དུ་བརྗོད་པར་བྱའོ། །

[Block 2032]
དེའི་རང་གི་ངོ་བོ་ནི་འཕགས་པ་རྣམས་ཁོ་ནས་སོ་སོ་རང་གིས་རིག་པར་བྱ་བ་ཡིན་ཏེ། བྲལ་བ་ཞེས་བྱ་བ་དང་། སོ་སོར་བརྟགས་པའི་འགོག་པ་ཞེས་བྱ་བ་གང་ཡིན་པ་བརྟགས༌[^1042]པ་དང་དགེ་བའི་རྫས་གཞན་ཞིག་ཡོད་དོ་ཞེས་བྱ་བ་དེ་ཙམ་ཞིག་ནི་བརྗོད་པར་ནུས་སོ།[^1043] །མདོ་སྡེ་པ་རྣམས་ན་རེ་འདུས་མ་བྱས་ཐམས་ཅད་ཀྱང་རྫས་སུ་མེད་པ་ཁོ་ན་སྟེ། དེ་ནི་གཟུགས་དང་ཚོར་བ་ལ་སོགས་པ་བཞིན་དུ་རྫས་གཞན་དུ་ནི་མེད་དོ། །

[Block 2033]
འོ་ན་ཅི་ཞེ་ན། རེག་བྱ་མེད་པ་ཙམ་ནི་ནམ་མཁའ་ཡིན་ཏེ། འདི་ལྟར་མུན་པའི་ནང་དག་ན་ཐོགས་པ་མ་རྙེད་ན་ནམ་མཁའོ་ཞེས་ཟེར༌[^1044]ཏོ། །

[Block 2034]
ཕྲ་རྒྱས་དང་སྐྱེ་བ་སྐྱེས་པ་འགགས༌[^1045]ནས་སོ་སོར་བརྟགས་པའི་སྟོབས་ཀྱིས་གཞན་མི་སྐྱེ་བ་ནི་སོ་སོར་བརྟགས་པས་འགོག་པ་ཡིན་ནོ། །

[Block 2035]
སོ་སོར་བརྟགས་པ་མེད་པ་ཁོ་ནར་རྐྱེན་མ་ཚང་བས་མི་སྐྱེ་བ་ནི་སོ་སོར་བརྟགས་པ་མ་ཡིན་པས་འགོག་པ་སྟེ་དཔེར་ན་བར་མ་དོར་འཆི་བའི་རིས་མཐུན་པ་ལྷག་མ་ལྟ་བུའོ་ཞེས་ཟེར་རོ། །
--- END BLOCKS ---
