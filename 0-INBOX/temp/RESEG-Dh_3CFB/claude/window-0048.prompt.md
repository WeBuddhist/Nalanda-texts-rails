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
ཁྱད་པར་རྟོགས་པ་ལ་བརྟེན་པ་རྟོགས་པ་མེད་པའི་ཕྱིར་འདི་རྟོགས་པ་མ་ཡིན་ཏེ། འབྲེལ་པའི་ཁྱད་པར་མེད་པར་ནི་དེ་རིགས་པ་མ་ཡིན་པའམ། དེ་རྒྱུ་མཚན་མེད་པ་ཅན་ཉིད་ཡིན་ན། དེའི་ཁྱད་པར་རྟོགས་པ་ངེས་པ་དང་འདྲ་བར་སྒྲ་རྣམས་ཀྱིས་བསྟན་པ་ཡང་རྒྱུ་མཚན་མེད་པ་ཅན་དུ་ཅིའི་ཕྱིར་མི་འདོད། དེ་བས་ན་འབྲེལ་པ་ཐམས་ཅད་ལ་རྟགས་དེ་དང་འདྲ་བར་ཁྱད་པར་མེད་པར་གོ་བར་འགྱུར་རོ། །

[Block 1682]
དེའི་ཕྱིར་ཁྱད་པར་མེད་པ་ཅན༌[^1231]ཉིད་དུ་ཐམས་ཅད་ཀྱིས་རྟོགས་པར་འགྱུར་རོ། །

[Block 1683]
དེ་བས་ན་འབྲེལ་པ་གྲུབ་པས་དོན་རྟོགས་པའི་ཕྱིར་འགའ་ཞིག་གིས་ཡང་དག་པའི་མན་ངག་ལ་ལྟོས་པར་མི་འགྱུར་རོ། །

[Block 1684]
གལ་ཏེ་ཡང་དག་པའི་མན་ངག་དང་བཅས་པ་ནི་རྟགས་ཡིན་ནོ་ཞེ་ན། དེ་བས་ན་ད༌[^1232]ནི་བརྒྱུད་པ་འདིས་ཅི་ཞིག་བྱ་སྟེ། ཡང་དག་པའི་མན་ངག་ལ་ལྟོས་པ་དེ་ཉིད་དོན་ཤེས་པར་བྱེད་པ༌[^1233]ཅིའི་ཕྱིར་མི་བྱེད། སྒྲ་དེ་ཡང་གང་ལ་བསམ་པ་ཅན་གྱིས་རབ་ཏུ་སྦྱོར་བར་བྱེད་པ་ནི་མཐོང་གི་གཞན་དུ་ན་ནི་མ་མཐོང་སྟེ། མཐོང་བ་དང་མ་མཐོང་བ་དག་ལས་དུ་བ་ལ་སོགས་པ་དང་འདྲ་བར་དེ་རྟོག་པར༌[^1234]བསྐྱེད་པའི་ཕྱིར། མེད་ན་མི་འབྱུང་བ་ཞེས་བྱ་བ་དེ་ཉིད་འབྲེལ་པ་ཡིན་ནོ། །

[Block 1685]
འདི་ལ༌[^1235]ཡང་གཞན་གྱི་ནུས་པ་མ་མཐོང་ཞིང་གྲུབ་པའི་ཐབས་མ་མཐོང་ངོ་། །ཅི་སྟེ་ཡང་སྒྲ་དང་དོན་དག་གི་འབྲེལ་པ་ནི་གཞན་ཉིད་མ་ཡིན་ན།

[Block 1686 [VERSE]]
དེ་ལས་ཐ་དད་མིན་དེ་ཉིད། །
འདི་ལས་གཞན་དངོས་ཡོད་མ་ཡིན། །

[Block 1687]
གནས་སྐབས་གཞན་ནི་ངོ་བོ་ཐ་དད་པའི་རྒྱུ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ།[^1236] །དེའི་ངོ་བོ་ཅན་ནི་དེ་ཉིད་ཡིན་པར་འགྱུར་རོ། །

[Block 1688]
སྔར་བཤད་པའི་རྣམ་པས་ཆོས་ཐ་དད་པར་ཡང་འགྱུར་ན། དེ་ཡང་འགལ་བ༌[^1237]མེད་པ་ཁོ་ན་ཡིན་ཏེ། དངོས་པོ་ཐ་དད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1689]
ཐ་དད་པ་དང་ཐ་དད་པ་མེད་པ་མ་གཏོགས་པ་དངོས་པོ་རྣམས་ལ་གཞན་པ་ནི་མེད་དེ། དེའི་ངོ་བོ་ནི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1690]
ངོ་བོ་ཡང་རྣམ་པར་རྟོག་པ་དེ་ལས་མ་འདས་པའི་ཕྱིར་རོ། །

[Block 1691]
གཞན་ཡང་།

[Block 1692 [VERSE]]
དངོས་པོའི་ངོ་བོ་ཐ་དད་ཕྱིར། །
འབྲེལ་པ་རྟོགས་པས་བྱས་པ་ཡིན། །

[Block 1693]
ཞེས་བྱ་བ་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 1694]
འདྲེས་པའི་མཚན་ཉིད་ཅན་གྱི་འབྲེལ་པ་ནི་དངོས་པོ་མ་འདྲེས་པ་རྣམས་ལ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1695]
དེ་དག་གི་འབྲེལ་པ་ནི་དོན་གཞན་ཡང་མ་ཡིན་ཏེ། འདི་ལྟར།

[Block 1696]
ཇི་ལྟར་ཡོད་གཞན་རག་ལུས་པ། །རྫས་ནི་གཞན་གྱི་འབྲེལ་པར་འགྱུར། །

[Block 1697]
ཡོད་པར་གྲུབ་པ་གཞན་ལ་ལྟོས་པར་མི་འགྱུར་ཏེ། ལྟོས་པ་མེད་པར་རང་རྒྱུད་པ༌[^1238]ནི་འབྲེལ་པ་མ་ཡིན་ནོ། །

[Block 1698]
རྫས་ཞེས་བྱ་བ་ནི་རང་བཞིན་བརྗོད་པ་ཡིན་ན་དེ་ཇི་ལྟར་དངོས་པོ་གཞན་ལ་འདྲེས་པར་འགྱུར་ཏེ། རང་བཞིན་གཞན་ཡོད་པ་ཉིད་ཀྱིས་གཞན་དང་འདྲེས་པ་ཞེས་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1699]
གལ་ཏེ་མ་འདྲེས་པ་ཅན་དང་མི་འགྱུར་མོད་ཀྱི་འདྲེས་པ་ཅན་དང་ནི་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། གང་གིས་དེ་དག་ལ་འདྲེས་པར་འགྱུར་བ་དེ་ཉིད་དེ་དག་དང་འདྲེས་པ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1700]
དེ་བས་ན་གལ་ཏེ་དོན་དག་དོན་གཞན་དང་འདྲེས་པར་འགྱུར་བ་འདི་ནི་ཤིན་ཏུ་ཐལ་བར་འགྱུར་ཏེ། ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 1701]
གཞན་ཡང་།

[Block 1702 [VERSE]]
ཡི་གེ་དོན་མེད་ཅན་འགྱུར་ཞིང་། །
ཚིག་སོགས་ཀུན་བརྟགས་དངོས་མེད་ལ། །
ཇི་ལྟར་དོན་དམ་པ་འབྲེལ་པ། །
འདི་ནི་གནས་པར་འགྱུར་བ་ཡིན། །

[Block 1703]
རྗོད་པར་བྱེད་པ་ནི་ཚིག་ཡན་ལག་གིས་དེ་དང་ལྡན་པར་འགྱུར་ན། ཡི་གེ་དག་ཡོད་དུ་ཟིན་ཀྱང་རྗོད་པར་བྱེད་པ༌[^1239]ཡིན་ནོ། །

[Block 1704]
དེ་བས་ན་དེ་དག་ལ་བརྗོད་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1705]
དེ་བས་ན་དེ་དག་ལ་བརྗོད་པར་བྱ་བ་དང་། རྗོད་པར་བྱེད་པའི་འབྲེལ་པ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་དག་ལ་གནས་ན་རང་གི་ངོ་བོ་ཉམས་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། གལ་ཏེ་བཀོད་པའི་ཁྱད་པར་གྱིས་ཡི་གེ་ཉིད་རྗོད་པར་བྱེད་པ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། བཀོད་པ་ནི་དོན་གཞན་མ་ཡིན་པ་ཉིད་ཀྱིས་ཐ་དད་པ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1706]
དེའི་ངོ་བོ་ཅན་ནི་བཀོད་པ་གཞན་ལ་ཡང་ཁྱད་པར་མེད་པའི་ཕྱིར་རྟོགས་པ་མཚུངས་པར་འགྱུར་རོ། །

[Block 1707]
བཀོད་པ་དོན་གཞན་ཉིད་ཡིན་ན་ཡང་འོག་ནས་འགོག༌[^1240]པར་འགྱུར་རོ། །

[Block 1708]
དེ་བས་ན་ཡི་གེ་རྣམས་རྗོད་པར་བྱེད་པ་ཉིད་མ་ཡིན་ན་ཚིག་ལ་སོགས་པ་རྗོད་པར་བྱེད་པར་འགྱུར་སྙམ་ན། དེ་ཅིར་ཡང་མི་རུང་སྟེ། ཐ་དད་པ་དང་ཐ་དད་པ་མེད་པ༌[^1241]ནི་འགལ་བའི་ཕྱིར་རོ། །

[Block 1709]
དེ་བས་ན་དབང་པོའི་རྣམ་པར་ཤེས་པ་ཁྱད་པར་ཅན་གྱི་རྗེས་སུ་འཇུག་པའི་རིགས་མཐུན་པའི་བག་ཆགས་ཀྱི་ཉེ་བར་ལེན་པ་ཅན་གྱི་རྣམ་པར་རྟོག་པ་ལ་སྣང་བ་ཅན་གྱི༌[^1242]ཚིག་དང་ངག་ནི་འཁྲུལ་པ་ཡིན་ནོ། །

[Block 1710]
གཅིག་ཏུ་སྣང་བ་ཅན་ནི་ལོག་པ་ཁོ་ན་ཡིན་ཏེ། གཅིག་དང་དུ་མ་ཉིད་ནི་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1711]
གཅིག་མ་ཡིན་ཏེ་བློ་དུ་མའི་རིམ་པས༌[^1243]འཛིན་པ་མི་རུང་བའི་ཕྱིར་དང་། དེ་ནི་གཅིག་གིས་གཟུང་བར་བྱ་བ་མ་ཡིན་ཏེ། ཡི་གེ་བཀོད་པ་རྗེས་སུ་འཛིན་པའི་ཕྱིར་དང་། ཡི་གེ་གཅིག་འཛིན་པ་ན་ཡང་བློ་དུ་མ་འགགས་པའི་ཕྱིར་ཏེ། བློ་རྣམས་ནི་སྐད་ཅིག་མ་ཡིན་པའི་ཕྱིར་དང་། སྐད་ཅིག་མ་ནི་རྡུལ་ཕྲ་རབ་གཅིག་ལས་འདས་པའི་དུས་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་དང་། ལྷག་མ་ཡིན་ན་ནི་ཆ་ཅན་གྱི་མཐའ་མི་རུང་བའི་ཕྱིར་དང་། ཡི་གེ་ཐུང་ངུ་རྫོགས་པའི་རྡུལ་ཕྲ་རབ་དུ་མ་འདས་པ་ཅན་གྱི་མིག་འབྱེད་པའི་དུས་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་དང་། དྲན་པ་དང་དེའི་དུས་ཅན་ཁོ་ན་ཡིན་ཏེ། ཇི་ལྟར་ཉམས་སུ་མྱོང་བ་བཞིན་དུ་དྲན་པའི༌[^1244]ཕྱིར་དང་། ཉམས་སུ་མྱོང་བ་དང་དྲན་པའི་གོ་རིམས་དག་ཁྱད་པར་རྟོགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1712]
ཚིག་ལ་སོགས་པ་དུ་མ་ཡང་མ་ཡིན་ཏེ། བློ་ལ་ཐ་དད་པ་མེད་པར་སྣང༌[^1245]བའི་ཕྱིར་དང་། དེའི་དུ་མ་ཉིད་ནི་འགོག་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1713]
དེ་ནི་དངོས་པོ་མ་ཡིན་ཏེ། དེའི་རྣམ་པར་རྟོག་པ་དེ་ལས་མ་འདས་པའི་ཕྱིར་རོ། །

[Block 1714]
འབྲེལ་པ་དངོས་པོ་ཡིན་ན་ཡང་ཇི་ལྟར་དེའི་རྟེན༌[^1246]དུ་འགྱུར་ཏེ། རྟེན་དུ་བྱ་བར་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1715]
དེ་ལྟར་ན་རྟེན་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 1716]
དེ༌[^1247]བས་ན་སྒྲ་དང་དོན་དག་གི་འབྲེལ་པ་ནི་རང་བཞིན་ཅན་མ་ཡིན་ནོ། །

[Block 1717]
དེའི་བསམ་པ་ཅན་གྱི་སྦྱོར་བ་ལས་བྱུང་བའམ། མངོན་པར་གསལ་བའི་སྒྲ་ནི་དེར་འཁྲུལ་པ་མེད་པའི་ཕྱིར་འདིའི་འབྲེལ་པ་ནི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 1718]
འབྱུང་བའམ་མངོན་པར་གསལ་བ་དེ་ཡང་འཁྲུལ་པ་མེད་པ་ལ་བརྟེན་པའི་སྐྱེས་བུས་བྱས་པའི་ཕྱིར་འབྲེལ་པ་ནི་སྐྱེས་བུས་བྱས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1719]
དེའི་སྒོ་ནས་སྒྲ་རྣམས་ནི་དོན་རྟོགས་པ་ལ་ངེས་པ་ཡིན་པ་དེ་ལྟ་ན། སྐྱེས་བུས་མ་བྱས་པ་ཉིད་ཡིན་ན་ཡང་དེ་ཉིད་འཁྲུལ་པ་ཡིན་ནོ། །

[Block 1720 [VERSE]]
བྱེད་པ་པོ་རྣམས་མི་དྲན༌[^1248]ཕྱིར། །
སྐྱེས་བུས་མ་བྱས་ཀྱང་འདོད་ལོ། །
--- END BLOCKS ---
