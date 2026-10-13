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
[Block 1681]
སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་ཀྱི་ཡི་གེ་གསུམ་མམ་ཡི་གེ་ཨའོ། །

[Block 1682]
རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་ཡང་འཇུག་པ་ལ་སོགས་པའི་བྱ་བའི་གཞི་སྲོག་དང་རྩོལ་བ་དང་མེ་དང་མཉམ་པའི་ངོ་བོ་ཡིན་ཞེས་བྱེ་བྲག་གོ། །

[Block 1683]
དེའི་བདག་ཉིད་ཀྱི་འབྲེལ་པས་ནི་བྱས་པ་དང་། མི་རྟག་པ༌[^1201]དང་ཤིང་དང་ཤ་བ་བཞིན་དབྱེར་མེད་པར་ངེས་པར་བྱེད་པའོ། །

[Block 1684]
མི་དམིགས་པའི་གཏན་ཚིགས་ཀྱིས་ཀྱང་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ་ཡང་ངེས་པར་མི་ནུས་ཏེ། དངོས་པོ་མེད་པའི་ཐ་སྙད་དེའི་ཡུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1685]
འདིར་ཆོས་ཅན་ཐམས་ཅད་ཀྱི་ཆོས་ཉིད་ཀྱི་ངོ་བོ་དེ་ཁོ་ན་ཉིད་དངོས་པོ་དང་དངོས་པོ་མེད་པ་དག་གིས་བརྗོད་དུ་མེད་པར་གྲགས་སོ། །

[Block 1686]
དེའི་ཕྱིར་མངོན་སུམ་དང་རྗེས་སུ་དཔག་པ་དག་གིས་གང་མ་གྲུབ་པའི་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་དེ༌[^1202]རྣམས་ཚད་མ་མེད་པ་ཁོ་ནའོ། །

[Block 1687]
དེ་ལ་སྨྲས་པ། མངོན་སུམ་ཁོ་ནས་འགྲུབ་པ་ཡིན་ཏེ། ཡང་རྣམ་པ་བཞི་ཡིན་པས་རང་རིག་པའི་མངོན་སུམ་གྱིས་རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པ་མངོན་པར་བྱང་ཆུབ་པའི་བར་དུ་ངེས་པར་བྱེད་དོ། །

[Block 1688]
རླུང་དང་སྔགས་ཀྱི་དེ་ཁོ་ན་ཉིད་ཅེས་བྱ་བའི་ཐིག་ལེ་ཙམ་བསྒོམ་པ༌[^1203]ནི་རང༌[^1204]གི་མངོན་སུམ་གྱི་ཡུལ་ཁོ་ནའོ། །

[Block 1689]
ཐིག་ལེ་བསྒོམ་པ་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་གྱི་ཆོས་ཏེ་སེམས་ལས་བྱུང་བའོ། །

[Block 1690]
སེམས་ལས་བྱུང་བའི་ཆོས་རྣམས་ཀྱང་རང་རིག་པའི་ཡུལ་ཡིན་ནོ། །

[Block 1691]
རང་རིག་པའི་མངོན་སུམ་གྱི་མཚན་ཉིད་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་ཐམས་ཅད་རང་གིས་རིག་པའོ། །

[Block 1692]
སེམས་ལ་རྣམ་པར་དག་པ་ཡང་རྣམ་པར་ཤེས་པ་གསུམ་གནས་གྱུར༌[^1205]པའི་མཚན་ཉིད་འོད་གསལ་བ་དེ་ཉིད་ཀྱི་རྗེས་སུ་མྱོང་ངོ་། །བདག་བྱིན་གྱིས་བརླབ༌[^1206]པའི་རིམ་པ་ལ་ཡང་སྒྱུ་མའི་དཔེ་བཅུ་གཉིས་ཀྱིས་ཉེ་བར་མཚོན་པའི་ཡེ་ཤེས་ཀྱི་སྐུ་ཐོབ་པ་སྟེ། སེམས་ལས་བྱུང་བའོ། །

[Block 1693]
ཐོབ་པ་དང་མ་ཐོབ་པ་དང་རིགས་གཅིག་ཅེས་བྱ་བ་ལ་སོགས་པ་སེམས་དང་མི་ལྡན་པའི་འདུ་བྱེད་ཀྱང་སེམས་ལས་བྱུང་བ་ཉིད་དོ། །

[Block 1694]
མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་ལ་ཡང་བདེ་བ་ཆེན་པོ་འོད་གསལ་བ་འདོད་ཆགས་ལ་སོགས་པ་དང་བྲལ་བ་ནི་རང་རིག་པ་ཉིད་དོ། །

[Block 1695]
བཞི་པོ་དེ་དག་རང༌[^1207]རིག་པ་སྟེ། མ་འཁྲུལ་ཞིང་གསལ་བར་སྣང་བའི་ཕྱིར་རོ། །

[Block 1696]
རང་བཞིན་གྱིས་གྲུབ་པའི་དངོས་པོ་ལས་སྐྱེས་པའི་ཕྱིར་རྟོག་པ་མེད་པའོ་ཞེས་མངོན་སུམ་གྱི་མཚན་ཉིད་ལས་མ་འདས་པའོ། །

[Block 1697]
ཇི་སྐད་དུ། མངོན་སུམ་མི་རྟོག༌[^1208]མི་སླུ༌[^1209]བ། །ཞེས་འབྱུང་ངོ་། །རིམ་པ་ཐ་མ་ནི་རྣལ་འབྱོར༌[^1210]གྱིས་ཐོབ་པ་ཡིན་ཏེ། གང་གི༌[^1211]ཕྱིར་དེ་ནི་ལྷུན་གྱིས་གྲུབ་པའི་ཡང་དག་པའི་དོན་ལ་བསྒོམ་པ་མཐར་ཐུག་པའི་དབང་གིས་རྡོ་རྗེའི་སྐུ་ལག་མཐིལ་གྱི་སྐྱུ་རུ་ར་བཞིན་དུ༌[^1212]དངོས་པོ་ཐམས་ཅད་མཐོང་བ་ལ་བརྩོན་པ་ཐམས་ཅད་མཁྱེན་པ་ཡིན་པས་རྟོག་པ་མེད་ཅིང་མ་འཁྲུལ་པ་ཡིན་ནོ། །

[Block 1698]
ཇི་སྐད་དུ།

[Block 1699 [VERSE]]
བསྒོམས་པའི༌[^1213]སྟོབས་ཀྱིས་གསལ་བ་ནི། །
འཇིགས་པ་ལ་སོགས་གསལ་བ་བཞིན། །
མི་སླུ་བ༌[^1214]ཡིས་ཤེས་པ་གང་། །
དེ་ནི་རྟོག་མེད་མངོན་སུམ་མོ། །

[Block 1700]
ཞེས་འབྱུང་ངོ་། །རྫོགས་པའི་རིམ་པ༌[^1215]ཚད་མ་ཉིད་དུ་བརྟགས༌[^1216]པའོ། །

[Block 1701]
[^1217]

[Block 1702 [HEADING]]
### རྒྱུད་ཀྱི་ཡན་ལག། ^1-6-0

[Block 1703]
ད་ནི་འདི་ལྟར་དཔྱད་པར༌[^1218]བྱ་སྟེ། གསང་བ་འདུས་པའི་རྣལ་འབྱོར་གྱི་རྒྱུད་ཆེན་པོ་འདི་གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་ཀྱི་ནང་ནས༌[^1219]གང་ཡིན་ཞེ་ན། སྨྲས་པ། མདོ་སྡེ་ཞེས་བྱ་བ་འདི་ཡིན་ཏེ། དེ་ཡང་ཟབ་པ་དང་རྒྱ་ཆེ་བའི་ཚིག་གི་དོན་མཚོན་པར་བྱེད་པས༌[^1220]མདོ་ཞེས་བྱའོ། །

[Block 1704]
འོ་ན་དཔལ་གསང་བ་འདུས་པ་ཞེས་བྱ་བ་རྣལ་འབྱོར་ཆེན་པོའི་རྒྱུད་ཡིན་ན། ཇི་ལྟར་མདོ་ཞེས༌[^1221]བཤད་ཅེ་ན། སྨྲས་པ། ཡན་ལག་ཡིན་པའི་ཕྱིར་དེའི་ཐ་སྙད་ཡིན་ཏེ། རྒྱུད་ཀྱི་མདོ་ཞེས་བྱ་བ་ཡན་ལག་གཙོ་བོ་ཡིན་ཏེ། དེའི་ཕྱིར་དེ་ཉིད་ཀྱིས་བསྟན་པ་ཡིན་ཏེ། གདེངས་ཀ་ཅན་དང་སྣ་ཅན་བཞིན་ནོ། །

[Block 1705]
འོ་ན་རྒྱུད་ཀྱི་ཡན་ལག་གཙོ་བོ་མདོ་སྡེ་ཞེས་སྨྲས་པས་ཡན་ལག་གཞན་རྣམས་ཀྱང་སྨྲ་བར༌[^1222]བྱ་བའི་རིགས་སོ་ཞེས་ཡན་ལག་དེ༌[^1223]ཇི་ལྟ་བུ་ཡིན་ཞེ་ན། སྨྲས་པ།

[Block 1706 [VERSE]]
མདོ་དང་ཚད་མ་ཡན་ལག་གྲུབ་པ་དང་། །
མ་ཚང་མེད་དང་འདྲི་ལ༌[^1224]ལན་འདེབས༌[^1225]དང་། །
མདོར་བསྟན་པ་དང་རྒྱས་བཤད་གོ་རིམས༌[^1226]དང་། །
མིང་དང་ཉེ་བར་བསྟན་པ་རྒྱུད་ཀུན་ཡིན། །

[Block 1707]
མདོ་དང་ཚད་མ་ཡན་ལག་རྣམས་ནི་མདོ་དང་ཚད་མ་དང་ཡན་ལག་རྣམས་སོ། །

[Block 1708]
དེ་རྣམས་གྲུབ་པ་ནི་མདོ་དང་ཚད་མ་ཡན་ལག་གྲུབ་པའོ། །

[Block 1709]
འགྲུབ་པ་ནི་ཡོད་པ་ཞེས་དོན་གཞན་མ་ཡིན་ནོ། །

[Block 1710]
འགྲུབ་པའི་སྒྲ་ནི་རེ་རེ་དང་སྦྱར་ཏེ་མདོ་གྲུབ་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1711 [HEADING]]
#### མདོ། ^1-6-1-0

[Block 1712]
མཚན་ཉིད་དང་ལྡན་པའི་མདོ་གྲུབ་པ་ཞེས་བཤད་པར་བྱ་སྟེ། གཞན་དུ་ན་མཚན་ཉིད་དང་མི་ལྡན་པའི་མདོ་རྒྱུད་ཀྱི་ཡན་ལག་ཏུ་འགྱུར༌[^1227]ཞེ་ན། སྨྲས་པ། བརྗོད་པར་མི་བྱ་སྟེ། མེད་པར་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1713]
མཚན་ཉིད་གྲུབ་པ་མ་གཏོགས་པར༌[^1228]མདོ་ཉིད༌[^1229]མི་འགྱུར་རོ། །

[Block 1714]
དེའི་ཕྱིར་མཚན་ཉིད་བརྗོད་པར་མི་བྱ་སྟེ། ཡང་ན་མདོ་ཞེས་བྱ་བ་ཅིའི་ཕྱིར་ཞེ་ན། སྨྲས་པ། དོན་མདོར་བསྟན་པས་ན་མདོའོ། །

[Block 1715]
ཁྱད་པར་གྱི་དོན་དེ་དག་སྟོན་པར་བྱེད་པས་ན་མདོའོ། །

[Block 1716]
དེ་ནས་བཅོམ་ལྡན་འདས་ཡེ་ཤེས་སྒྲོན་མ་རྡོ་རྗེ་ཞེས་བྱ་བའི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་ཏེ་ཞེས་བྱ་བ་དེའི་བཤད་པ་རྣམ་པ་བཞིའི་རིགས་པས་བསྐྱེད་པའི་རིམ་པ་དང་། རྡོ་རྗེ་བཟླས་པ་དང་། སེམས་རྣམ་པར་དག་པ་དང་། བདག་ལ་བྱིན་གྱིས་བརླབ་པ་དང་། འོད་གསལ་བ་དང་། ཟུང་དུ་འཇུག་པའི་རིམ་པ་རྣམས་མཚོན་ཏོ། །

[Block 1717]
དེ་བཞིན་དུ།

[Block 1718 [VERSE]]
དངོས་པོ་ཐམས་ཅད་དང་བྲལ་བ། །
ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་དང་། །
གཟུང་དང་འཛིན་པ་རྣམ་སྤངས་པ། །
ཆོས་བདག་མེད་པ་མཉམ་ཉིད་པས། །

[Block 1719 [VERSE]]
རང་སེམས་གཟོད་ནས་མ་སྐྱེས་པ། །
སྟོང་པ་ཉིད་ཀྱི༌[^1230]རང་བཞིན་ནོ། །

[Block 1720]
ཞེས་བྱ་བས་རང་གི་སེམས་ལ་དམ་བཅའ་བ་དང་། གཏན་ཚིགས་དག་ཉིད་ཀྱིས་གསུངས་སོ། །
--- END BLOCKS ---
