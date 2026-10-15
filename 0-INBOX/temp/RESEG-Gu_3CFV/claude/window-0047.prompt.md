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
[Block 1646]
འདི་ནི་མཚོན་པ་ཙམ་ཡིན་ཏེ། འདིས་ཕྲེང༌[^1050]བ་བརྒྱུ་ཞིང་འདོགས་པ་ཐམས་ཅད་ལ་དགག་པར་བྱས་པ་རྟོགས་པར་བྱའོ། །

[Block 1647]
ངོ་སོ་ལས་བྱུང་བར་སྦྱིན་པར་མི་བྱའོ། །

[Block 1648]
མི་རིངས་པར་རྒྱུག་པར༌[^1051]མི་བྱའོ། །

[Block 1649]
མྱུར་བ་དང་མཆོངས་པར་མི་བྱའོ། །

[Block 1650]
བརླ་དང་ལག་པ་ཉ་ལྟར་བསྐོར་བར་མི་བྱའོ། །

[Block 1651]
ཆུར་གསེག་མ༌[^1052]དག་གདབ་པར་མི་བྱའོ། །

[Block 1652]
ཆུར་རྫ་རྔ་ཁ་ཅིག༌[^1053]པ་དང་རྔ་བོ་ཆེ་ལྟར་བརྡུང་བར་མི་བྱའོ། །

[Block 1653]
རྫ་བ་ལ་ཕྱིལ་མོ་ཉུག་པར་མི་བྱའོ། །

[Block 1654]
གླང་པོ་ཆེའི་སྐད་དང་། རྟའི་སྐད་དང་། ཁྱུ་མཆོག་གི་སྐད་དང་། ཁུ་བྱུག་གི་སྐད་མི་དབྱུང༌[^1054]ངོ་། །ཁས་དུང་དང་སིལ་ཁྲོལ་དང་རྔ་བོ་ཆེའི་སྐད་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1655]
ལོངས་པའི་གཞིར་གཏོགས་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1656]
ཅི་ཞིག་བྱས་ན་ཁྲུས་བྱས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེས་བྱ་བ་འདི་ལ་མདུན་རོལ་གྱི་གནས་ལ་ཞེས་འཆད་པར་འགྱུར་ཏེ། གང་གིས་མདུན་རོལ་ནས་ཞེས་བྱ་བའི་དྲི་བ་འདི་ལ་ཁྲུས་ཀྱི་ཞག་བཅོ་ལྔ་པོ་ལས་བྱ་བ་འཆད་པར་འགྱུར་རོ། །གང་ལས་ཤེ་ན། དུས་གཞན་དུ་གང་ཞག༌[^1055]བཅོ་ལྔ་པ་ལས༌[^1056]ཁྲུས་ཀྱི་ཞག་གཅིག་བྱ་བ་འདི་ལ་བརྗོད་པར་བྱ་སྟེ། སོ་ག་རྣམས་ཀྱི་ཟླ་བ་ལྷག་མ་ཕྱེད་དང་གཉིས་དང་དབྱར་རྣམས་ཀྱི་དང་པོ་ལས་སོ་ཞེས་བྱ་བ་ནི་ལྷག་མ་ཅི་ཙམ་པས་ཞེས་བྱ་བའི་དྲི་བ་འདི་ལ་ཟླ་བ་ལྷག་མ་ཕྱེད་དང་གཉིས་དང་། གང་གི་ཟླ་བ་ཕྱེད་དང་གཉིས་ལྷག་པའི་ལྷག་མ་ཞེས་བྱ་བའི་དྲི་བ་འདི་ལ་སོ་ག་རྣམས་ཀྱི་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1657]
ཅི་སོ་གའི་ཟླ་བ་ཕྱེད་དང་གཉིས་ལས་ལྷག་པ་ལྷག་མའི་དུས་གཞན་ལ་ཡང་ཡིན་ནམ༌[^1057]ཞེ་ན། དེའི་ཕྱིར་དབྱར་རྣམས་ཀྱི་དང་པོ་ལས༌[^1058]སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སོ་ག་རྣམས་ཀྱི་ཟླ་བ་ལྷག་མ་ཕྱེད་དང་གཉིས་དང་། དབྱར་རྣམས་ཀྱི་དང་པོའི་ཟླ་བ་ལས་དུས་གཞན་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1658]
ཟླ་བ་ཕྱེད་དང་གསུམ་པོ༌[^1059]དེ་དག་ལ་ཚ་བའི་གཉེན་པོའི་ཕྱིར་འདི་རྗེས་སུ་གནང་ངོ་། །དེ་བས་ན་འདིར་ཁས་བླངས་པར་རྣམ་པར་གཞག་པར་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1659]
ཅི་གནས་སྐབས་ཐམས་ཅད་དུ་དགེ་སློང་ལ་དེ་ལྟ་བུའི་དུས་ཀྱི་ཐ་མར་ཁྲུས་བྱེད་པ་ལ་ལྟུང་བྱེད་དུ་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་གོས་མེད་པའི་ཟས་གཉིས་པ་རྙེད་པའི་རྣམ་པ་གང་ཡིན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གོས་མེད་པའི་ཟས་གཉིས་པ་རྙེད་པ་ལ་རྣམ་པ་གང་ཡིན་པའི་དགེ་སློང་ལ་ལྷག་པར་གནས་ཏེ་ཟ་བ་ལ་ཁ་ན་མ་ཐོ་བ་དེ་ལྟ་བུ་ཞེས་བྱ་བའི་དོན་ཏེ། །ནད་པ་མ་ཡིན་པ་དང་ལས་མ་བྱས་པ་དང་ལམ་དུ་མ་ཞུགས་པ་ཞེས་བྱ་བ་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 1660]
ཅི་གནས་སྐབས་གཞན༌[^1060]ཐམས་ཅད་ལ་ཡང་བབ་པ་ལ་ཡང་འདིར་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་རླུང་གིས་མ་བསྐྱོད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། །འདིར་ཚད་ཇི་ཙམ་གྱིས་ན་བསྐྱོད་པ་ཡིན་པར་རིག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གོས་ཀྱི་གྲྭ་འགུལ་བ་ནི་དེའི་མཐའ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་བཏིང་བ་ནི་རྒྱུ་མཚན་ཉིད་དོ། །

[Block 1661]
དེ་ཙམ་གྱིས་བསྒུལ་བ་ལ་སྟེ་འདིང་བ༌[^1061]ནི་མ་ཡིན་ནོ། །

[Block 1662]
གང་ཇི་སྲིད་ཅེས་བྱ་བ་འདི་ལ་བཟུང་བ་ནི་དེའི་མཐའོ་ཞེས་བྱ་བ་ནི་བསྐྱེད་པའི་མཐའོ། །

[Block 1663]
བཞི་པོ་འདི༌[^1062]རྣམས་ལས་གཞན་པའི་གནས་སྐབས་ཐམས་ཅད་ལ་ཅི་ཡོད་པར་གྱུར་པ་ཡིན་ནམ་ཞེ་ན། ཆར་གྱིས་མ་ཕོག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གང་ཡང་རུང་བའི་ཆུས་ཕོག་པ་གང་ཡིན་པ་དེ་ནི་འདིར་ཆར་གྱིས་ཕོག་པ་ཡིན་ནོ། །

[Block 1664]
དེ་ལྟར་ཡང་ཆུ་ཀླུང་རྒལ་བ་ལ་སོགས་པ་ལ་དུས་དེ་ཉིད་དུ་ལྷག་པར་གནས་ཏེ་ཁྲུས་བྱའོ་ཞེས་སྨོས་པ་ཡིན་ནོ། །

[Block 1665]
ཆར་གྱིས་ཕོག་པ་འདིའི་མཐའ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེའི་ཐིགས་པ་གཉིས་ཀྱིས་ཕོག་པའོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཅི་གོས་ལ་ཡང་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ལུས་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཐ་ན་ཆུའི་ཐིགས་པ་གཉིས་སམ་གསུམ་གྱིས་ལུས་ལ་ཕོག་པར་གྱུར་ན་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1666]
འདིར་བསྒྲུབ་པའི་ཚུལ་གྱིས་ནི་འདི་སྐད་བསྟན་པ་ཡིན་ཏེ། དེ་བས་ན་འདི་མ་བཟུང་ངོ་། །འདིར་རླུང་དང་ཆར་གྱིས་ཕོག་པའི་གཞན་གྱི༌[^1063]འདུ་ཤེས་འབྱུང་བ་ཡིན་ཏེ། འདིར་རླུང་ནི་རྒྱུ་མཚན་ཅན་གྱི་སྒྲིབ་པ་ནི། རྒྱུ་མཚན་ཉིད་མ་ཡིན་ཏེ་ཆར་གྱིས༌[^1064]འདི་ལ་སོ་སོར་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1667]
ཆར་མི་བབ༌[^1065]ན་སྐམས་པ་བཞིན་དུ་གཉེན་པོ་གོས་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་འདོད་པར་གྱུར་པའི་ཕྱིར་འདི་སྨོས་སོ། །

[Block 1668]
ཕྱིར་འདོད་པ་འདི་བྱེ་བྲག་མེད་པར་འབྱུང་བ་ཡིན་ཏེ། གོ་སྐབས་མེད་པར་བྱས་པ་འདི་ཞེས་བྱ་བ་མ་བཟུང་བའོ། །

[Block 1669]
གཞན་གྱི་དུས་སུ་ཁྲུས་ཀྱི་ཉིན་མོ་མ་ཡིན་པ་ཞག་བཅོ་ལྔའི་མདུན་རོལ་དུ་ཁྲུས་བྱེད་ནའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དུས་འདི་སྨོས་པ་དེ་ལས་གཞན་པའི་དུས་ལ་གང་ཞིག་བཅོ་ལྔ་པ་ཁྲུས་མ་ཡིན་པའི༌[^1066]ཞག་སྨོས་པ་དེའི༌[^1067]མདུན་རོལ་དུ་ཁྲུས་བྱེད་པ་ལ་ལྟུང་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1670]
ཁྲུས་ཇི་ལྟར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དབང་བསྐུར་བས་སམ་འཇུག་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆུས་ལུས་ཀྱི་ཚད་ཙམ་དུ་བྱས་ན་ཁྲུས་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ལྟེ་བར་སོན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ཡང་དབང་བསྐུར་བས་སྤྱི་བོ་ནས་བརྩམས་ཏེ་རྐང་མཐིལ་གྱི་བར་དུ་ཕྱོགས་གཞན་ནས་རྩོམ་པ་ཡོད་པ་ལ། གལ་ཏེ་ལྟེ་བའི་ལྟག་ཡན་ཆད་འཁྲུ་ཞིང་འོག་ཏུ་མ་སོན་པ་དང་ཆུས་འཁྲུ་ཞིང་ལྟག་ཏུ་མ་སོན་པ་ཡང་མ་ཆོག་པ་ཉིད་དོ། །

[Block 1671]
གལ་ཏེ་དེ་གཉིས་ཀ་ཡང་དུས་གཅིག་ཏུ་ཁྲུས༌[^1068]རྩོམ་པ་ན་གལ་ཏེ་མཉམ་དུ་འཇུག་པར་གྱུར་ན་ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་རྫོགས་པ་གཅིག་གི་ཕྱེད་དུ་འགྱུར་རོ། །

[Block 1672]
གལ་ཏེ་མ་ཡིན་ན་མ་ཆོག་པ་ཉིད་དོ། །

[Block 1673]
དེ་བས་ན་གོང་མའམ་འོག་གི་ཆ་དག་ལ་ཐམས་ཅད་དུ་གྱུར་པ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་ལྟེ་བར་ཞེས་སྨོས་པ་ནི་གཙོ་བོ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་མི་སྲིད་པ་ཉིད་ལ་ཡང་ལྟེ་བའི་ཕྱོགས་གཏམས༌[^1069]ཏེ་རྫོགས་པ་ལ་རྫོགས་པ་ཉིད་དོ། །

[Block 1674]
འདིར་ལྟེ་བར་མ་ཕྱིན་པའི་མདུན་རོལ་དུ་ཅི་ཞིག་རྟོགས་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་མདུན་རོལ་དུ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆུ་ལ་རེག་པའི་མདུན་རོལ་དུ་སྦྱོར་བར་བྱེད་པ་ནི། དེ་སྦྱོར་བའི་ཉེས་བྱས་སུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1675]
ཐམས་ཅད་ལ་དུས་དག་ཡོད་ཀྱང་བྱིན་གྱིས་མ་བརླབས་ན་ཞེས་བྱ་བ་ནི་དུས་དག་ལ་ཐམས་ཅད་དུ་བྱས་པ་གང་ཡིན་པ་བསླབ་པའི་གཞི་གཞན་དང་འབྲེལ་པ་དེ་ལ་དུས་དག་ཡོད་དུ་ཟིན་ཀྱང་བྱིན་གྱིས་མ་བརླབས་ཤིང་མངོན་སུམ་དུ་མ་བྱས་ན་ཉེས་བྱས་སོ། །

[Block 1676]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 1677]
ཉེས་བྱས་ལས་ལྡང་བ་ནི་འདི་ཡིན་ཏེ། གང་ཞིག་རྒྱུར་གྱུར་པ༌[^1070]དུས་ཀྱི་གནས་སྐབས་སམ་གཞན་དེ་ནི་དུས་སོ། །

[Block 1678]
ཞག་བཅོ་ལྔ་ན་ཁྲུས་ཀྱི་ཉིན་མོ་ལ་ཁྲུས་བྱ་བ་གང་ཡིན་པ་དེ་ནི་གྲགས་པ་ཡིན་པས་ན་འདིར་དུས་མེད་པའོ། །

[Block 1679]
འདི་ནི་དུས་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་ལ་ཡུལ་མ་ཡིན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 1680]
དོན་གཞན་ལ་གཞོལ་བར་ཆུ་ཉམས་སུ་མྱོང་བ་ནི་ཁྲུས་མ་ཡིན་ནོ། །

[Block 1681]
དེའི་ཕྱིར་མ་བསམས་པར༌[^1071]བརྒལ་བ་དང༌[^1072]བརྒྱལ་བ་ལ་གདབ་པ་དག་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཁྲུས་ལ་རྩེ་གཅིག་པ་ཉིད་ཀྱི་ཆུ་ཉམས་སུ་མྱོང་བ་གང་ཡིན་པ་དེ་ནི་ཁྲུས་གཞན་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1682]
འདིར་གཞུང་ནི་དགེ་སློང་དག་ཆུ་ཀླུང་རྒལ་བར་བྱེད་དོ་ཞེས་གསུངས་པ་དང་། འདིར་གཞུང་གཞན་ལས་ཀྱང་རྐྱལ་བ༌[^1073]ལ་ཆུས༌[^1074]དབང་བསྐུར་བ་དང་། ཟམ་པ་ལས་ལྟུང་བ་ཆུ་ཀླུང་ལས་རྒལ་བར་བྱེད་པ་དང་། ཆུས་གང་བ་ལ་མཆོང་བར་བྱེད་པ་ལ་ཡང་ལྟུང་བ་མེད་དོ། །

[Block 1683]
དེ་བཞིན་དུ་མདུན་རོལ་དུ་འགྲོ་ཞིང་རྒྱ་མཚོ་ལ་གཟིངས་ནས་འགྲོ་བ་རྣམས་ལ་བཤང་བ་དང་གཅི་བ་བྱེད་པ་ཡང་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1684]
དེ་དང་དེའི་ངོ་བོ་གཞན་གྱི་རྐྱེན་རྣམས་ལ་ཆུ་ཉམས་སུ་མྱོང་བ་ལ་ཉེས་པ་མེད་པ་ཉིད་དུ་བསྟན་པའོ། །

[Block 1685]
ཇི་སྲིད་དུ་ཁྲུས་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་ཀྱིས་རིག་པར་བྱའོ། །
--- END BLOCKS ---
