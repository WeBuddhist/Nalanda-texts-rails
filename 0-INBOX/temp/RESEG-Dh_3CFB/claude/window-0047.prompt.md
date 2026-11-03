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
དེ་ལ་ཡང་དོན་དང་ལྷན་ཅིག་སྐྱེས་པ་མ་རྟོགས་པར་གྱུར༌[^1218]ན།

[Block 1647 [VERSE]]
སྒྲ་རྣམས་ལ་ནི་རང་བཞིན་དག །
[^1219]རྣམ་པར་བཟློག་པ་མི་རིགས་སོ། །

[Block 1648]
ཅི་སྟེ་འབྲེལ་པ་ཞིག་པ་དོན་གཞན་ལ་མེད་པའམ། དོན་རྣམས་བརྗོད་པར་བྱ་བ་མ་ཡིན་པར་མ་གྱུར་ཅིག་སྙམ་པས། གལ་ཏེ་སྐྱེས་ཤིང་བྱུང་བའི་དོན་འབྲེལ་པ་དང་ལྡན་པ་སྐྱེ་བར༌[^1220]འགྱུར་ན། འབྲེལ་པ་དེ་སྐྱེས་སུ་ཟིན་ཀྱང་སྒྲ་ལ་མི་འགྱུར་ཏེ། དེ་དང་འབྲེལ་པ་མེད་པ་ཅན་གྱི་རང་བཞིན་ནི་རང་བཞིན་བཟློག་པ་མེད་པར་དེའི་ངོ་བོ་མི་རུང་བའི་ཕྱིར་དང་། དོན་དང་ལྷན་ཅིག་སྐྱེས་པ་གཞན་ལས་གྲུབ་པ་ཡང་སྒྲ་ཕན་འདོགས་པ་མེད་པ་ལ་མི་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 1649]
དེ་ཡང་དེ་སྐྱེད་པར་བྱེད་པའི་ལྷན་ཅིག་བྱེད་པ་ཉིད་ཡིན་ན་ནུས་པ་ནི་རྟག་ཏུ་བསྐྱེད་པར་ཐལ་བར་འགྱུར་ཏེ། ལྟོས་པ་མེད་པའི་ཕྱིར་ཏེ། རྟག་པ་ལ་ཕན་གདགས་སུ་མེད་པའི་ཕྱིར་རོ། །

[Block 1650]
ནུས་པ་མེད་པ་ཡིན་ན༌[^1221]ཡང་ཕྱིས་ཀྱང་ནུས་པ་མ་ཡིན་ཏེ།

[Block 1651 [VERSE]]
རང་བཞིན་མི་འདོར་བའི་ཕྱིར་རོ། །
རྣམ་བརྟགས་འབྲེལ་ལ་ཉེས་འདི་མེད། །

[Block 1652]
དངོས་པོ་འདྲེས་པ་ལྟོས་པ་ཅན་ནི་མ་ཡིན་གྱི་སྐྱེས་བུ་གོམས་པ་སྣང་བ་ཅན་དེ་ལ་ལྟོས་པའི་མཚན་ཉིད་ཅན་ནི་འབྲེལ་པ་ཡིན་ཏེ། དེས་རྟག་ཏུ་ཟིན་ཀྱང་རང་བཞིན་གཞན་དུ་བསྒྱུར་བ་མེད་པར་འགའ་ཞིག་ལས་རང་ཉིད་ཀྱིས་དཔྱད་ནས་སྦྱོར་བར་བྱེད་པའི་ཕྱིར། དེ་དག་ཀྱང་དེ་བཞིན་འགྱུར་ན་ཡང་འཇིག་པའི་ཆོས་ཅན་མ་ཡིན་ནོ། །

[Block 1653]
རྟེན་ཞིག་པས་བརྟེན་པ་འབྲེལ་པ་ཞིག་པའི་ཕྱིར་དེ་མི་རྟག་པ་ཡིན་ནོ་ཞེས་བཤད་པ་གང་ཡིན་པ་དེ་ལ།

[Block 1654 [VERSE]]
གལ་ཏེ་རྟེན་ནི་འཇིག་ན་ཡང་། །
འཇིག་མིན་རྟག་ཕྱིར་རིགས་དང་འདྲ། །
རྟག་རྣམས་ལ་བརྟེན་ནུས་པ་གང་། །
གང་གིས་བརྟེན་ཏེ༌[^1222]འདོད་པ་ཡིན། །

[Block 1655]
འདི་སྐད་དུ་རིགས༌[^1223]བརྟེན་པ་ནི་རྟག་པ་ཡིན་ན་རྟེན་དང་ལྷན་ཅིག་འཇིག་པ་ཡང་མ་ཡིན་ནོ་ཞེས་ཐོས་མོད་ཀྱི། འོན་ཀྱང་རྟག་པ་རྣམས་ལ་རྟེན་གྱི་ནུས་པ་མ་མཐོང་ན་གང་གིས་ན་འདིའི་རྟེན་ཡིན་ཏེ། བྱས་པ་ལ་བྱེད་པ་མེད་པའི་ཕྱིར་དང་། བྱེད་པ་པོ་མ་ཡིན་པ་ལ་ཡང་མི་ལྟོས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1656]
གལ་ཏེ་རིགས་དང་འབྲེལ་པ་ནི་བརྟེན་ནས་གསལ་བར་ཕན་འདོགས་པ༌[^1224]ཡིན་པ་དེས་ན་རྟེན༌[^1225]ཞེས་བྱའོ་ཞེ་ན།

[Block 1657 [VERSE]]
ཤེས་པ་སྐྱེད་བྱེད་ལྷན་ཅིག་བྱེད། །
རྒྱུ་རྣམས་ཚོགས་པར་གྱུར་པ་ལས། །
དེ་བསྐྱེད་པར་ནི་རུད་ཉིད་ཕྱིར། །
རིགས་པ་ཤེས་པས་བུམ་སོགས་ཀྱི། །

[Block 1658 [VERSE]]
གསལ་བ་བསྐྱེད་པ་ལ་ཡང་འདོད། །
ཁྱད་མེད་འགྱུར་བ་མེད་རྣམས་ཀྱི། །
གསལ་བྱེད་རང་གི་དོན་ཅི་བྱས། །
གང་ཕྱིར་དེ་དག་ངེས་གསལ་འདོད། །

[Block 1659]
ལྷན་ཅིག་བྱེད་པ་སྣང་བ་ཉེ་བར་ལེན་པ་ལ་ལྟོས་པ་ལས་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་སྐད་ཅིག་མ་གཞན་བསྐྱེད་པ་ཁོ་ན་བུམ་པ་ལ་སོགས་པ་རྣམས་མངོན་པར་གསལ་བ་ཡིན་ནོ། །

[Block 1660]
དེ་ལྟ་མ་ཡིན་ན་དེ་ལས་ཕན་འདོགས་པ་ལ་ལྟོས་པ་མེད་པ་ཤེས་པ་བསྐྱེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1661]
ནུས་པ་བྱེད་པ་ཡང་སྐྱེད་པར་བྱེད་པ་ཉིད་ཡིན་པའི་ཕྱིར་ཏེ། དེ་ནི་དེའི་བདག་ཉིད་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1662]
དོན་གཞན་ཉིད་ཡིན་ན་ནི་དངོས་པོ་ལ་ཕན་འདོགས་པར་བྱེད་པ་མ་ཡིན་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1663]
[^1226]ནུས་པས་ཀྱང་ཤེས་པ་བསྐྱེད་པའི་ཕྱིར། རྟག་ཏུ་བུམ་པ་ལ་སོགས་པ་མི་འཛིན་པར་འགྱུར་ལ། སྣང་བ་ལ་ལྟོས་པ་མེད་པ་ཅན་འཛིན་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1664]
ལྟོས་པ་མེད་པ་ནི་བདག་ཉིད་ལ་ཕན་འདོགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1665]
དེ་བས་ན་འདི་དག་ནི་རང་གི་ཡུལ་ལ་རྣམ་པར་ཤེས་པ་བསྐྱེད་པའི་ཕྱིར། གཞན་ལ་ལྟོས་པར་གྱུར་པ་ན་དེ་ལས་རང་གི་ངོ་བོ་ཕུལ་དུ་དབྱུང་བ་བདག་གིར་བྱེད་དོ། །

[Block 1666]
དེ་བས་ན་འདིའི་དེ་དག་བསྐྱེད་པར་བྱ་བ་ཡིན་ནོ། །ཤེས་བྱའི་ངོ་བོ་ཐོབ་ནས་ཀྱང་ཤེས་པའི་དབང་གིས་འབྲས་བུའི་ཁྱད་པར་བརྗོད་པའི་སྒྲས་ཁྱད་པར་གསལ་བར་བྱ་བའི་ཕྱིར། གསལ་བར་བརྗོད་དོ། །

[Block 1667]
དེ་ལྟར་རིགས་དང་འབྲེལ་པ་ལ་སོགས་པ་དག་ནི་རྣམ་པ་འགའ་ཞིག་ཀྱང་ཕན་གདགས་པར་བྱ་བ་ཉིད་མ་ཡིན་པའི་ཕྱིར། ཕན་འདོགས་པར་བྱེད་པ་མ་ཡིན་པས་གསལ་བར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1668]
འབྲེལ་པ་དངོས་པོ་ཉིད་ཡིན་ནོ།[^1227] །ཐ་དད་ཕྱིར་བློ་སྣ་ཚོགས་འགྱུར། །འབྲེལ་པ་དེ་ནི་དངོས་པོར་འགྱུར་ན་ངེས་པར་སྒྲ་དང་དོན་དག་ལས་ཐ་དད་པ་དང་ཐ་དད་པ་མེད་པ་ལས་འདས་པ་མ་ཡིན་ནོ། །

[Block 1669]
ངོ་བོ་དངོས་པོ་ཡིན་ན་ནི་དེའི་ངོ་བོ་ཉིད་མ་ཡིན་པ་ཉིད་ནི་གཞན་ཡིན་ནོ། །ཞེས་བཤད་ཟིན་ཏོ། །

[Block 1670]
དེ་ཡང་མིག་གིས་གཟུང་བར་བྱ་བ་ཡིན་ན་རང་གི་བློ་ལ་དེ་ལས་གཞན༌[^1228]དག་ལས་ངོ་བོ་ཐ་དད་པ་ཅན་སྣང་བ་མེད་ན་ཇི་ལྟར་ན་དེ་ལྟར་འགྱུར་ཏེ། སྣང་བ་ཐ་དད་པ་མེད་པ་དང་མ་མཐོང་བ་དག་ནི་ཐ་དད་པ་དང་ཡོད་པ་ཉིད་བཟློག་པ་དག་གི་རྟེན༌[^1229]ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1671]
དེ་ལྟ་མ་ཡིན་ན་དེ་དག་གི་གནས་པ་ནི་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1672]
གལ་ཏེ་དབང་པོ་ལས་འདས་པ་ཉིད་ཡིན་པའི་ཕྱིར་མི་སྣང་དུ་ཟིན་ཀྱང་དབང་པོ་ལ་སོགས་པ་དང་འདྲ་བར་སྐྱོན་ཡོད་པ་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ལས་མི་རྟོག་པར་ཐལ་བའི་ཕྱིར་དང་། རབ་ཏུ་མ་གྲུབ་པ་ནི་ཤེས་པར་བྱེད་པ་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1673]
ཐག་ཉེ་བ་ཙམ་གྱིས་ཤེས་པར་བྱེད་པ་ཉིད་ཡིན་ན་ནི་བློ་མ་བྱང་བ་རྣམས་ཀྱང་འགྱུར་རོ། །

[Block 1674]
རྗེས་སུ་དཔག་པ་ལས་རྟོགས་པ་མ་ཡིན་ཏེ། རྟགས་མེད་པའི་ཕྱིར་དང་དཔེ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1675]
དེ་ཡང་དབང་པོ་ལས་འདས་པ་ཉིད་ཀྱིས་སྒྲུབ་པར་བྱེད་པ་ལ་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 1676]
གལ་ཏེ་དབང་པོ་ལ་སོགས་པ་དག་ལ་ཡང་མཚུངས་སོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་དག་ནི་རྣམ་པ་གཞན་གྱིས་རྗེས་སུ་དཔག་པའི་ཕྱིར་རོ། །

[Block 1677]
འགའ་ཞིག་ཡོད་ན་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་དང་ལྡན་པའི་ཤེས་པས་དེ་ཙམ་ལས་མི་འབྱུང་བ་ཅན་དང་། དེ་ལས་བཟློག་པ་ལ་ལྟོས་པ་སྒྲུབ་པར་བྱེད་དོ། །

[Block 1678]
དེ་བས་ན་འབྲས་བུའི་སྒོ་ནས་དབང་པོ་གྲུབ་པ་ཡིན་ནོ། །

[Block 1679]
དེ་ལྟར་འབྲེལ་པ་ནི་མ་ཡིན་ཏེ། དེ་མ་གྲུབ་ན་དེའི་འབྲས་བུའི་ཤེས་པ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 1680]
དེ་ལ་ནི་སྒྲའམ་དོན་གྱི་ངོ་བོ་རྟག་པ༌[^1230]ཡིན་ཏེ། དེ་དག་ནི་ཐམས་ཅད་ལ་རུང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1681]
ཁྱད་པར་རྟོགས་པ་ལ་བརྟེན་པ་རྟོགས་པ་མེད་པའི་ཕྱིར་འདི་རྟོགས་པ་མ་ཡིན་ཏེ། འབྲེལ་པའི་ཁྱད་པར་མེད་པར་ནི་དེ་རིགས་པ་མ་ཡིན་པའམ། དེ་རྒྱུ་མཚན་མེད་པ་ཅན་ཉིད་ཡིན་ན། དེའི་ཁྱད་པར་རྟོགས་པ་ངེས་པ་དང་འདྲ་བར་སྒྲ་རྣམས་ཀྱིས་བསྟན་པ་ཡང་རྒྱུ་མཚན་མེད་པ་ཅན་དུ་ཅིའི་ཕྱིར་མི་འདོད། དེ་བས་ན་འབྲེལ་པ་ཐམས་ཅད་ལ་རྟགས་དེ་དང་འདྲ་བར་ཁྱད་པར་མེད་པར་གོ་བར་འགྱུར་རོ། །

[Block 1682]
དེའི་ཕྱིར་ཁྱད་པར་མེད་པ་ཅན༌[^1231]ཉིད་དུ་ཐམས་ཅད་ཀྱིས་རྟོགས་པར་འགྱུར་རོ། །

[Block 1683]
དེ་བས་ན་འབྲེལ་པ་གྲུབ་པས་དོན་རྟོགས་པའི་ཕྱིར་འགའ་ཞིག་གིས་ཡང་དག་པའི་མན་ངག་ལ་ལྟོས་པར་མི་འགྱུར་རོ། །

[Block 1684]
གལ་ཏེ་ཡང་དག་པའི་མན་ངག་དང་བཅས་པ་ནི་རྟགས་ཡིན་ནོ་ཞེ་ན། དེ་བས་ན་ད༌[^1232]ནི་བརྒྱུད་པ་འདིས་ཅི་ཞིག་བྱ་སྟེ། ཡང་དག་པའི་མན་ངག་ལ་ལྟོས་པ་དེ་ཉིད་དོན་ཤེས་པར་བྱེད་པ༌[^1233]ཅིའི་ཕྱིར་མི་བྱེད། སྒྲ་དེ་ཡང་གང་ལ་བསམ་པ་ཅན་གྱིས་རབ་ཏུ་སྦྱོར་བར་བྱེད་པ་ནི་མཐོང་གི་གཞན་དུ་ན་ནི་མ་མཐོང་སྟེ། མཐོང་བ་དང་མ་མཐོང་བ་དག་ལས་དུ་བ་ལ་སོགས་པ་དང་འདྲ་བར་དེ་རྟོག་པར༌[^1234]བསྐྱེད་པའི་ཕྱིར། མེད་ན་མི་འབྱུང་བ་ཞེས་བྱ་བ་དེ་ཉིད་འབྲེལ་པ་ཡིན་ནོ། །

[Block 1685]
འདི་ལ༌[^1235]ཡང་གཞན་གྱི་ནུས་པ་མ་མཐོང་ཞིང་གྲུབ་པའི་ཐབས་མ་མཐོང་ངོ་། །ཅི་སྟེ་ཡང་སྒྲ་དང་དོན་དག་གི་འབྲེལ་པ་ནི་གཞན་ཉིད་མ་ཡིན་ན།
--- END BLOCKS ---
