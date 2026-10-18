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
གང་ཞིག་ཅི་གང་དག་འཆི་བར་འགྱུར་བ་དེ་དག་སྐྱེ་བར་འགྱུར་རམ་ཞེས་འདྲི་བ་དེ་ལ་ནི་རྣམ་པར་ཕྱེ་སྟེ་ལུང་བསྟན་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1647]
མི་ལ་ཡང་དམན་པ་དང་ཁྱད་པར་དུ་འཕགས་པ་གཉི་ག་ཡོད་དེ། ལྟོས་པ་ཡིན་པས་མགོ་གཅིག་ཏུ་གཉིས་ཀར་ལུང་བསྟན་པར་བྱ་དགོས་ཏེ། དཔེར་ན་རྣམ་པར་ཤེས་པ་ནི་རྒྱུ་ཡང་ཡིན་ལ་འབྲས་བུ་ཡང་ཡིན་པ་བཞིན་ནོ། །

[Block 1648]
གཅིག་ཏུ་འདྲི་བ་ལ་གཅིག་ཏུ་ལུང་བསྟན་དུ་མི་རུང་བས་རྣམ་པར་ཕྱེ་སྟེ་ལུང་བསྟན་པར་རིགས་སོ། །

[Block 1649]
ཕུང་པོ་དག་ལས་སེམས་ཅན་གཞན་ནམ་ཞེས་འདྲི་བ་འདི་ནི༌[^1184]ལུང་དུ་མ་བསྟན་པ་ཁོ་ན༌[^1185]ཡིན་ཏེ། ལུང་དུ་མ་བསྟན་པ་ཁོ་ན་ནི་ལུང༌[^1186]བསྟན་པར་མི་རུང་བའོ།[^1187] །གཞག་པར་བྱ་བའི་འདྲི་བ་གང་ཡིན་པ་གཞག་པར་བྱ་བ་ཉིད་དུ་ལུང་སྟོན་པ་དེ་ཇི་ལྟར་ན་ལུང་དུ༌[^1188]མ་བསྟན་པ་ཡིན། ཆོས་མངོན་པ༌[^1189]རྣམས་ན་རེ་བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་དང་། དེའི་ལེགས་པར་བཤད་པའི་ཆོས་དང་། ཉན་ཐོས་ཀྱི་དགེ་འདུན་ལེགས་པར་ཞུགས་པ་དང་། གཟུགས་མི་རྟག་པ་ནས་རྣམ་པར་ཤེས་པའི་བར་མི་རྟག་པ་དང་། སྡུག་བསྔལ་གདགས་པ་ནས་ལམ་གདགས་པའི་བར་ནི༌[^1190]དོན་དང་ལྡན་པ་ཡིན་པའི་ཕྱིར། མགོ་གཅིག་ཏུ་ལུང་བསྟན་པར་བྱའོ། །

[Block 1650]
རྣམ་པར་ཕྱེ་སྟེ་ལུང་བསྟན་པ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་འགའ་ཞིག་ཆོས་དག་སྨྲོས་ཤིག་ཅེས་ཟེར་ན། དེ་ལ་འདས་པ་དག་དང་། མ་འོངས་པ་དག་དང་། ད་ལྟར་བྱུང་བ་དག་དང་། ཆོས་མང་པོ༌[^1191]ཞིག་ཡོད་ན་གང་དག་སྨྲ་བར་བྱ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1651]
གལ་ཏེ་འདས་པ་དག་སྨྲོས་ཤིག་ཅེས་ཟེར་ན། དེ་ལ་འདས་པ་རྣམས་ལ་ཡང་གཟུགས་ནས་རྣམ་པར་ཤེས་པའི་བར་དུ་མང་དུ་ཡོད་ན་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1652]
འོན་ཏེ་གཟུགས་སྨྲོས་ཤིག་ཅེས་ཟེར་ན། གཟུགས་ལ་ཡང་དགེ་བ་དང་། མི་དགེ་བ་དང་། ལུང་དུ་མ་བསྟན་པ་རྣམ་པ་གསུམ་ཡོད་ན་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1653]
གལ་ཏེ་དགེ་བ་སྨྲོས་ཤིག་ཅེས་ཟེར་ན། དེ་ལ་ཡང་སྲོག་གཅོད་པ་སྤོང་བ་ནས་ཚིག་ཀྱལ༌[^1192]པ་ལས་སྤོང་བའི་བར་དུ་རྣམ་པ་བདུན་ཡོད་དོ༌[^1193]ཞེས་བརྗོད་པར་བྱའོ། །

[Block 1654]
གལ་ཏེ་སྲོག་གཅོད་པ་ལས་སྤོང་བ་སྨྲོས་ཤིག༌[^1194]ཟེར་ན། དེ་ལ་ཡང་མ་ཆགས་པ་དང་། ཞེ་སྡང་མེད་པ་དང་། གཏི་མུག་མེད་པ་ལས་སྐྱེས་པ་དང་རྣམ་པ་གསུམ་ཡོད་ལ་མ་ཆགས་པ་ལས་སྐྱེས་པ་ལ་ཡང་རྣམ་པར་རིག་བྱེད་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་བྱེ་བྲག་གིས་རྣམ་པ་གཉིས་ཡོད་ན་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་རྣམ་པར་ཕྱེ་སྟེ་བརྗོད་པར་བྱ་བ་ཡིན་ནོ།[^1195] །གཡོན་ཅན་གྱི་འདྲི་བ་ལ༌[^1196]ལུང་བསྟན་པ་ཡང་དེ་ཉིད་ཡིན་ཏེ། དེ་ལ་ནི་ཆོས་མང་པོ༌[^1197]ཞིག་ཡོད་ན་ཞེས་བརྗོད་པར་བྱའི་རྣམ་པར་དབྱེ་བར་ནི་མི་བྱ་སྟེ། ཅང་མི་སྨྲ་བའམ། བདག་ཉིད་ལུང་སྟོན་དུ་གཞུག་ཅེས་བྱ་བའི་ཐ་ཚིག་གོ་ཞེས་ཟེར་རོ། །

[Block 1655]
གང་གི་ཚེ་དེ་གཉིས་ཅུང་ཟད་ཀྱང་མི་འདྲ་བའི༌[^1198]གསོལ་བ་འདེབས་པ་འབའ་ཞིག་ཏུ་ཟད་ལ། དེ་གཉིས་ལ་ཡང་ཅུང་ཟད་ཀྱང་ལུང་མི་སྟོན་གྱི་འདྲི་བ་འབའ་ཞིག༌[^1199]ཟད་ན་དེ་ཇི་ལྟར་ན་དེ་གཉིས་ཀྱི་འདྲི་བ་ཡིན། ཇི་ལྟར་ན་ལུང་དུ་སྟོན་པ་ཡིན། གང་ཞིག་ལམ་སྨྲོས་ཤིག་ཅེས་ཟེར་ན། ཅི་དེས་ལམ་མ༌[^1200]དྲིས་པ་ཡིན་ནམ། དྲི་བ་ཉིད་ཀྱིས་དེ་ལུང་བསྟན་པའི་ཕྱིར་ཇི་ལྟར་དྲིས་ནས་ལུང་བསྟན་པ་མ་ཡིན། གཞག་པར་བྱ་བ་ནི་དཔེར་ན་འཇིག་རྟེན་མཐའ་ཡོད་པ་ཞིག་གམ། མཐའ་མེད་པ་ཞིག་ཅེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 1656 [HEADING]]
#### དྲི་བ་ལུང་བསྟན་པ་རྣམས་ཀྱི་མཚན་ཉིད། ^2-20-2-0

[Block 1657]
དྲི་བ་ལུང་བསྟན་པ་རྣམས་ཀྱི་མཚན་ཉིད་ནི་མདོ་ཁོ་ན་ལས་བལྟ་བར་བྱ་སྟེ། བཙུན་པ་དགེ་འདུན་ཕལ་ཆེན་སྡེ་པ་རྣམས༌[^1201]དགེ་སློང་དག་བཞི་པོ་འདི་དག་ནི། དྲི་བ་ལུང་དུ་བསྟན་པ་དག་ཡིན་ཏེ། བཞི་གང་ཞེ་ན། དགེ་སློང་དག་མགོ་གཅིག་ཏུ་ལུང་དུ༌[^1202]བསྟན་པར་བྱ་བའི་དྲི་བ་ཡང་ཡོད། གཞག་པར་བྱ་བའི་བར་དུ་ཡང་ཡོད་དེ།[^1203] དགེ་སློང་དག༌[^1204]མགོ་གཅིག་ཏུ་ལུང་བསྟན་པར་བྱ་བའི་འདྲི་བ་གང་ཞེ་ན། འདུ་བྱེད་ཐམས་ཅད་མི་རྟག་པ་ཡིན་ནམ་ཞེས་འདྲི་བ་འདི་ནི། དགེ་སློང་དག་མགོ་གཅིག་ཏུ་ལུང་བསྟན་པར་བྱ་བའི་དྲི་བ༌[^1205]ཡིན་ནོ། །

[Block 1658]
དགེ་སློང་དག་རྣམ་པར་ཕྱེ་སྟེ། ལུང་བསྟན་པར་བྱ་བའི་འདྲི་བ་གང་ཞེ་ན། ཆེད་དུ་བསམ་པར་བྱ་བའི་ལས་བྱས་ནས༌[^1206]ཅི་ཞིག་སོ་སོར་ཡང་དག་པར་མྱོང་བར་འགྱུར་ཞེ་ན།[^1207] འདྲི་བ་འདི་ནི་དགེ་སློང་དག་མགོ༌[^1208]རྣམ་པར་ཕྱེ་སྟེ། ལུང་བསྟན་པར་བྱ་བའི་འདྲི་བ་ཡིན་ནོ། །

[Block 1659]
དགེ་སློང་དག་དྲིས་ནས་ལུང་བསྟན་པར་བྱ་བའི་དྲི་བ༌[^1209]གང་ཞེ་ན། འདུ་ཤེས་སྐྱེས་བུ༌[^1210]བདག་ཉིད༌[^1211]ཡིན་ནམ། འོན་ཏེ་འདུ་ཤེས་ཀྱང་གཞན་ཞིག་ལ། བདག་ཀྱང་གཞན་ཞིག་ཡིན་ཞེས་དྲིས་ན། ཚེ་དང་ལྡན་པ་བདག༌[^1212]གང་ཡིན་པར་ཡིད་ཆེས་ཞེས་འདྲི་བར༌[^1213]བྱའོ། །

[Block 1660]
གལ་ཏེ་འདི་སྐད་དུ་ཚེ་དང་ལྡན་པ་བདག་གིས་ནི་རིག་པ༌[^1214]བདག་ཡིན་པར་ཤེས་སོ་ཞེས་ཟེར་ན། དེ་ལྟ་ཡིན་ན་འདི་སྐད་དུ་འདུ་ཤེས་ཀྱང་གཞན་ལ་བདག་ཀྱང་གཞན་ཡིན༌[^1215]ནོ་ཞེས་བརྗོད་པར་བྱ་སྟེ། འདི་ནི་དགེ་སློང་དག་དྲིས་ནས་ལུང༌[^1216]བསྟན་པར་བྱ་བའི་དྲི་བ་འདི༌[^1217]ཡིན་ནོ། །

[Block 1661]
དགེ་སློང་དག་གཞག་པར་བྱ་བའི་འདྲི་བ་གང་ཞེ་ན། དཔེར་ན་འཇིག་རྟེན་རྟག་པ་ཞིག་གམ། མི་རྟག་པ་ཞིག་གམ། རྟག་ཀྱང་རྟག་ལ་མི་རྟག་ཀྱང་མི་རྟག༌[^1218]པ་ཞིག་གམ། རྟག་པ་ཡང་མ་ཡིན་མི་རྟག་པ་ཡང་མ་ཡིན་པ་ཞིག་གམ། མཐའ་ཡོད་པ་ཞིག་གམ། མཐའ་ཡོད་པ་མ་ཡིན་པ་ཞིག་གམ། མཐའ་ཡོད་ཀྱང་ཡོད་ལ་མཐའ་མེད་ཀྱང་མེད་པ་ཞིག་གམ། མཐའ་ཡོད་པ་ཡང་མ་ཡིན་མཐའ་མེད་པ་ཡང་མ་ཡིན་པ་ཞིག་གམ། དེ་བཞིན་འོངས་པ་ཤི་ནས་ཡོད་པ་ཞིག་གམ་ཞེས་བྱ་བ་ནས་སྲོག་ཀྱང་གཞན་ལ་ལུས་ཀྱང་གཞན་ཞིག་གམ་ཞེས་བྱ་བའི་བར་དུ༌[^1219]འདྲི་བ་ལྟ་བུ་སྟེ། འདི་ནི་དགེ་སློང་དག༌[^1220]གཞག་པར་བྱ་བའི་འདྲི་བ་ཡིན་ནོ་ཞེས་འདོན་ཏོ། །

[Block 1662 [HEADING]]
### དངོས་པོ་དེ་དང་ལྡན་པ། ^2-21-0

[Block 1663]
གང་ཟག་གང་གི་ཕྲ་རྒྱས་གང་ཞིག་དམིགས་པ་གང་ལ་རྒྱས་པར་འགྱུར་བ་འདི༌[^1221]ནི་དེས་དེ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 1664]
འདས་པས་ནི་གང་དང་ལྡན་པ༌[^1222]ཞེས་བྱ་བ་ནས་ད་ལྟར་བྱུང་བས་ནི་གང་དང་ལྡན་ཞེས་བྱ་བའི་བར་འདི་བརྗོད་པར་བྱ་སྟེ། མདོར་བསྡུ་ན་ཉོན་མོངས་པ་ནི་རྣམ་པ་འདི་གཉིས་ཏེ། རང་གི་མཚན་ཉིད་པའི་ཉོན་མོངས་པ་ནི་འདོད་ཆགས་དང་།

[Block 1665 [VERSE]]
ཁོང་ཁྲོ་བ་དང་ང་རྒྱལ་རྣམས་སོ། །
ཉོན་མོངས་པ་སྤྱི་པ་ནི་ལྟ་བ་དང་།
ཐེ་ཚོམ་དང་མ་རིག་པ་རྣམས་སོ། །

[Block 1666]
དེ་ལ་རེ་ཞིག །

[Block 1667 [VERSE]]
འདས་དང་ཉེར་གནས་འདོད་ཆགས་དང་། །
ཁོང་ཁྲོ་ང་རྒྱལ་དག་གིས་ནི། །
གང་ལ་དེ་སྐྱེས་མ་སྤངས་པའི། །
དངོས་པོ་དེ་དང་ལྡན་པ་ཡིན། །

[Block 1668]
དངོས་པོ་གང་ལ་འདས་པ་དང་ད་ལྟར་བྱུང་བའི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་རྣམས་སྐྱེས་ལ་མ་སྤངས་པ་དེ་དག་གི༌[^1223]དངོས་པོ་དེ་དང་ལྡན་ཏེ། དེ་དག་ནི་རང་གི་མཚན་ཉིད་པའི་ཉོན་མོངས་པ་ཡིན་པའི་ཕྱིར་གདོན་མི་ཟ་བར་ཐམས་ཅད་ལ་ཐམས་ཅད་དུ་འབྱུང་བ་མ་ཡིན་ནོ། །

[Block 1669]
ཉིད་ཀྱིས༌[^1224]དེ་དག་མ་འོངས་པས། །ཀུན་དང་། གང་ལ་མ་སྤངས་པ་དེ་དག་ཅེས་བྱ་བར་སྦྱར་ཏེ། ཡིད་ཀྱི་ས་པའི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་མ་འོངས་པ་དེ་དག་ཉིད་ཀྱིས་དུས་གསུམ་པའི་དངོས་པོ་ཐམས་ཅད་དང་ལྡན་ཏེ། ཡིད་དག་གི་ཡུལ་ནི་དུས་གསུམ་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1670]
གཞན་གྱིས་རང་དུས་པ།[^1225] འདོད་ཆགས་དང་ཁོང་ཁྲོ་བ་གཞན་དག་གིས་ནི་མ་འོངས་པའི་དངོས་པོ་ཁོ་ན་དང་ལྡན་ནོ། །

[Block 1671]
གཞན་ཡང་གང་དག་ཡིན་ཞེ་ན། གང་གི༌[^1226]རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་པོའི་འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་སྟེ། སྐྱེ་བའི་ཆོས་ཅན་རྣམས་ཀྱི་ནི༌[^1227]དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 1672]
དེ་དག་ཉིད། མི་སྐྱེ་རྣམས་ཀྱིས་ཐམས་ཅད་དང་། །མི་སྐྱེ་བའི་ཆོས་ཅན་རྣམས་ཀྱིས་རྣམ་པར་ཤེས་པའི་ཚོགས་ལྔ་པོ་དག་གིས་ཀྱང་དུས་གསུམ་པའི་དངོས་པོ་ཐམས་ཅད་དང་ལྡན་ནོ། །

[Block 1673]
ལྷག་མ་ཀུན་གྱི༌[^1228]ཀུན་དང་ལྡན། །ལྷག་མ་ཡང་གང་དག་ཅིག་ཡིན་ཞེ་ན། ལྟ་བ་དང་། ཐེ་ཚོམ་དང་། མ་རིག་པ་རྣམས་ཏེ། ཉོན་མོངས་པ་སྤྱི་དང་ལྡན༌[^1229]པ་ཡིན་པའི་ཕྱིར་དུས་གསུམ་པའི་དངོས་པོ་མེད་པའི༌[^1230]དངོས་པོ་ཐམས་ཅད༌[^1231]ལྡན་ནོ། །

[Block 1674]
ཇི་སྲིད་དུ་མ་སྤངས་པ་ཞེས་བྱ་བའི་དབང་དུ་བྱས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1675 [HEADING]]
### འདས་པ་དང་མ་འོངས་པ་རྫས་སུ་ཡོད་པ། ^2-22-0

[Block 1676]
ཅི་འདས་པ་དང་། མ་འོངས་པའི་དངོས་པོ༌[^1232]རྫས་སུ་ཡོད་དམ། འོན་ཏེ་མེད། གལ་ཏེ་ཡོད་ན་ནི་དུས་ཐམས་ཅད་དུ་ཡོད་པའི་ཕྱིར་འདུ་བྱེད་རྣམས་རྟག་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1677]
འོན་ཏེ་མེད་ན་ནི་ཇི་ལྟར་ན་དེ་དང་ངམ། དེས་ལྡན་པའམ་བྲལ་བ་ཡིན་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དང༌[^1233]ལྡན་པའི་ཕྱིར་འདུས་བྱས་རྣམས་རྟག་པ་ཉིད་དུ་དམ་མི་འཆའོ། །

[Block 1678 [HEADING]]
#### ལུང། ^2-22-1-0

[Block 1679]
[^1234]དུས་རྣམས་ཀུན་དུ་ཡོད་པར་ནི་གསལ་བར་དམ་འཆའོ། །ཅིའི་ཕྱིར་ཞེ་ན། གསུངས་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་དག་གལ་ཏེ་འདས་པའི་གཟུགས་ཤིག་ཡོད་པར་མ་གྱུར་ན་འཕགས་པ་ཉན་ཐོས་ཐོས་པ་དང་ལྡན་པ་འདས་པའི་གཟུགས་ལ་མི་ལྟ་བར་ཡང་མི་འགྱུར་བ་ཞིག་ན། གང་གི་ཕྱིར་འདས་པའི་གཟུགས་ཡོད་པ་དེའི་ཕྱིར་འཕགས་པ་ཉན་ཐོས་ཐོས་པ་དང་ལྡན་པ་འདས་པའི་གཟུགས་ལ་མི་ལྟ་བ་ཡིན་ནོ། །

[Block 1680]
གལ་ཏེ་མ་འོངས་པའི་གཟུགས་ཤིག་ཡོད་པར་མ་གྱུར་ན་འཕགས་པ་ཉན་ཐོས་ཐོས་པ་དང་ལྡན་པ་མ་འོངས་པའི་གཟུགས་ལ་མངོན་པར་དགའ་བ་མེད་པར་ཡང་མི་འགྱུར་བ་ཞིག་ན། གང་གི་ཕྱིར་མ་འོངས་པའི་གཟུགས་ཡོད་པ་ཞེས་རྒྱས་པར་གསུངས་སོ། །

[Block 1681]
གཉིས་ཕྱིར། རྣམ་པར་ཤེས་པ་ནི་གཉིས་ལ་བརྟེན་ནས་སྐྱེའོ་ཞེས་གསུངས་པ། གཉིས་གང་ཞེ་ན། མིག་དང་གཟུགས་རྣམས་ནས་ཡིད་དང་ཆོས་རྣམས་ཀྱི་བར་ཡིན་ཏེ། འདས་པ་དང་མ་འོངས་པ་དག༌[^1235]མེད་ན་དེ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་གཉིས་ལ་བརྟེན་པར༌[^1236]མི་འགྱུར་རོ། །

[Block 1682]
རེ་ཞིག་ལུང་ལས་འདས་པ་དང་མ་འོངས་པ་ཡོད་པ་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 1683 [HEADING]]
#### རིགས་པ། ^2-22-2-0

[Block 1684]
རིགས་པས་ཀྱང་། ཡུལ་ཡོད་ཕྱིར། ཡུལ་ཡོད་ན་རྣམ་པར་ཤེས་པ་སྐྱེ་བར་འགྱུར་གྱི་མེད་པར་ནི་མ་ཡིན་ནོ། །

[Block 1685]
གལ་ཏེ་འདས་པ་དང་མ་འོངས་པ་མེད་ན་ནི་དམིགས་པ་མེད་པའི་རྣམ་པར་འགྱུར་ཏེ། དེ་བས་ན་དམིགས་པ་མེད་པའི་ཕྱིར་རྣམ་པར་ཤེས་པ་ཉིད་དུ་ཡང་མི་འགྱུར་རོ། །
--- END BLOCKS ---
