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
དེར་གང་ཞིག་མ་གསུངས།

[Block 1682]
སྨྲས་པ། གནས་པའོ། །

[Block 1683]
འོ་ན་ནི་གནས་པ་གཞན་དུ་འགྱུར་བ་ཞེས་བྱ་བ་གང་ཡིན་པ་འདི་ཡིན་ནོ། །

[Block 1684]
འདི་ནི་རྒ་བའི་རྣམ་གྲངས་ཡིན་ཏེ། དཔེར་ན་སྐྱེ་བའི་འབྱུང་བ་ཞེས་བྱ་བ་དང་། མི་རྟག་པ་ཉིད་ཀྱི་འཇིག་པ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1685]
མདོ་ལས་ནི་ཡིད་འབྱུང་བར་བྱ་བའི་ཕྱིར་ཆོས་གང་དག་འདུ་བྱེད་རྣམས་ཀྱི་དུས་འཕོ་བར་བྱ་བའི་ཕྱིར་ཞུགས་པ་དེ་དག་ཉིད་མཚན་ཉིད་དུ་གསུངས་ཏེ། སྐྱེ་བས་ནི་འདུ་བྱེད་རྣམས་མ་འོངས་པའི་དུས་ནས་ད་ལྟར་བྱུང་བའི་དུས་སུ་སྐྱེད་པར་བྱེད་དོ། །

[Block 1686]
རྒ་བ་དང་མི་རྟག་པ་ཉིད་དག་གིས་ནི་ད་ལྟར་བྱུང་བ་ནས་འདས་པར་ཏེ། ཉམ༌[^786]ཆུང་ངུར་བྱས་ཏེ་འཇོམས་པར་བྱེད་པའི་ཕྱིར་དཔེར་ན་ཐིབས་པོར་ཞུགས་པའི་མི་ཞིག་ལ་དགྲ་གསུམ་ཡོད་དེ། དེ་ལས་གཅིག་གིས་ནི༌[^787]ཐིབས་པོ་ནས་འབྱིན་པར་བྱེད། གཉིས་ཀྱིས་ནི་སྲོག་གཅོད་པར་བྱེད་པ་དེ་དང་འདྲའོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 1687]
གནས་པ་ནི་མི་འབྲལ་བར་འདོད་པ་དེ༌[^788]བཞིན་དུ་འདུ་བྱེད་དེ་དག་འཁྱུད་ནས་གནས་སོ།[^789] །དེའི་ཕྱིར་འདི་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དུ་རྣམ་པར་མ་བཞག་གོ། །

[Block 1688]
འདུས་མ་བྱས་ཀྱང་རང་གི་མཚན་ཉིད་ལ་གནས་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1689]
གཞན་དག་རྟོག་པར་བྱེད་པ་ནི་མདོ་ལས་གནས་པ་དང་རྒ་བ་བསྡུས་ཏེ། གནས་པ་གཞན་དུ་འགྱུར་བ་ཉིད་ཅེས་མཚན་ཉིད་གཅིག་ཏུ་གསུངས་སོ། །ཅི༌[^790]དགོས་ཤེ་ན། འདི་དག་གི་ནང་ན་འདི་ནི་ཆགས་པའི་གཞི་ཡིན་པས༌[^791]དེའི་ཕྱིར་དེ་ལ་མ་ཆགས་པར་བྱ་བའི་དོན་དུ་དེ་ནི་དཔལ་དང་འདྲ་བ༌[^792]འདི་དང་རྣ༌[^793]ནག་མ་དང་ལྷན་ཅིག་ཏུ་བསྟན་ཏེ། དེའི་ཕྱིར་འདུས་བྱས་ཀྱི་མཚན་ཉིད་ནི་བཞི་ཁོ་ནའོ་སྙམ་མོ། །

[Block 1690]
སྐྱེ་བ་ལ་སོགས་པ་དེ་དག་ཀྱང་འདུས་བྱས་ཡིན་པའི་ཕྱིར་སྐྱེ་བ་ལ་སོགས་པ་གཞན་ཡང་ཡོད་པར་འགྱུར་རོ་ཞེ་ན། ཡོད་པ་ཁོ་ན་སྟེ། དེ་དག་སྐྱེ་བའི་སྐྱེ༌[^794]ལ་སོགས། །དེ་དག་ལ་ཡང་སྐྱེ་བའི་སྐྱེ་བ་དང་། རྒ་བའི་རྒ་བ་དང་། གནས་པའི་གནས་པ་དང་། མི་རྟག་པ་ཉིད་ཀྱི་མི་རྟག་པ་ཉིད་ཅེས་བྱ་བ་རྗེས་སུ་མཐུན་པའི་མཚན་ཉིད་བཞི་ཡོད་དོ། །

[Block 1691]
དེ་དག་ལ་ཡང་སྐྱེ་བ་ལ་སོགས་པ་གཞན་དུ་ཐལ་བའི་ཕྱིར་རེ་རེ་ལ་ཡང་མཚན་ཉིད་བཞི་པ་དང་མཐར་ཐུག་པ་མེད་པའི་སྐྱོན་དུ་ཡང་འགྱུར་བ་མ་ཡིན་ནམ་ཞེ་ན། མི་འགྱུར་ཏེ། འདི་ལྟར། དེ་ཆོས་བརྒྱད་དང་གཅིག་ལ་འཇུག །སྐྱེ་བ་ལ་སོགས་པ་དེ་དག་ནི་ཆོས་བརྒྱད་ལ་འཇུག་གོ། །

[Block 1692]
འཇུག་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན། བྱེད་པ་སྟེ་སྐྱེས་བུའི་རྩལ་ལོ། །

[Block 1693]
སྐྱེ་བའི་སྐྱེ་བ་ལ་སོགས་པ་ནི་ཆོས་གཅིག་ལ་འཇུག་གོ། །ཇི་ལྟ་ཞེ་ན། ཆོས་བདག་ཉིད་གཏོགས་པར་མཚན་ཉིད་དང་རྗེས་སུ་མཐུན་པའི་མཚན་ཉིད་བརྒྱད་དང་ལྷན་ཅིག་ཏུ་དགུ་སྐྱེ་ལ། དེ་ལ་སྐྱེ་བས་ནི་བདག་ཉིད་མ་གཏོགས་པའི༌[^795]ཆོས་གཞན་བརྒྱད་སྐྱེད་པར་བྱེད་དོ། །

[Block 1694]
སྐྱེ་བའི་སྐྱེ་བས་ནི་སྐྱེ་བ་དེ་ཁོ་ན་སྐྱེད་པར་བྱེད་དོ། །

[Block 1695]
དཔེར་ན༌[^796]ཁྱིམ་བྱ་མོ་ལ་ལ༌[^797]ལས་ནི་ཕྲུ་གུ་མང་དུ་འབྲང་ལ། ལ་ལས་ནི་ཉུང་ངུ་འབྲང་བ་དེ་དང་འདྲའོ། །

[Block 1696]
གནས་པས་ཀྱང་བདག་ཉིད་མ་གཏོགས་པའི༌[^798]ཆོས་གཞན་བརྒྱད་གནས་པར་བྱེད་ལ། གནས་པའི་གནས་པས་ནི་གནས་པ་དེ་ཁོ་ན་གནས་པར་བྱེད་དོ། །

[Block 1697]
དེ་བཞིན་དུ་རྒ་བ་དང་མི་རྟག་པ་ཉིད་དག་ལ་ཡང་ཅི་རིགས་པར་སྦྱར་བར་བྱ་སྟེ། དེ་བས་ན༌[^799]ཐུག་པ་མེད་པར་ཐལ་བར་མི་འགྱུར་རོ་ཞེས་གྲག་གོ། །

[Block 1698]
མདོ་སྡེ་པ་རྣམས་ན་རེ་འདི་ནི་ནམ་མཁའ་ལ་འདྲལ་བར་བསྐྱོད་པ་ཡིན་ཏེ། སྐྱེ་བ་ལ་སོགས་པའི་ཆོས་ཅན༌[^800]དེ་དག་ནི་ཇི་ལྟར་རྣམ་པར་འབྱེད་པ་ལྟར་རྫས་སུ་ཡོད་པ་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། ཚད་མ་མེད་པའི་ཕྱིར་ཏེ། དེ་དག་རྫས་སུ་ཡོད་པའི་ཚད་མ་ཇི་ལྟར་གཟུགས་ལ་སོགས་པའི་ཆོས་བཞིན་དུ་མངོན་སུམ་པ་འམ།[^801] རྗེས་སུ་དཔག་པ་འམ། ཡིད་ཆེས་པའི་ལུང་ནི་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 1699]
འོ་ན་གང་མདོ་སྡེ༌[^802]ལས།

[Block 1700]
འདུས་བྱས་སྐྱེ་བར་ཡང་མངོན་ནོ། །

[Block 1701]
འཇིག་པར་ཡང་མངོན་ནོ། །

[Block 1702]
གནས་པ་གཞན་དུ་འགྱུར་བ་ཉིད་དུ་ཡང་མངོན་ནོ་ཞེས་གསུངས་སོ་ཞེ་ན། ཚིག་ཤེས་པ་ནི་ལྷ་རྣམས་དགའ་བ་ཡིན་གྱི་དོན་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1703]
བཅོམ་ལྡན་འདས་ཀྱིས་ནི་དོན་ལ་བརྟེན་པར༌[^803]གསུངས་སོ། །

[Block 1704]
འདིའི་དོན་གང་ཞེ་ན། མ་རིག་པས་ལྡོངས་པའི་བྱིས་པ་རྣམས་འདུ་བྱེད་ཀྱི་རྒྱུན་ལ་བདག་དང་བདག་གིར་མོས་པས་མངོན་པར་ཞེན་པས་མོས་པ་དེ་བཟློག་པའི་ཕྱིར། བཅོམ་ལྡན་འདས་ཀྱིས་འདུ་བྱེད་ཀྱི་རྒྱུན་དེ་འདུས་བྱས་ཉིད་དང་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་ཉིད་དུ་བསྟན་པར་བཞེད༌[^804]ནས། གསུམ་པོ་འདི་དག་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་དག་ཡིན་ནོ་ཞེས་གསུངས་པར་ཟད་ཀྱི་ཡང༌[^805]སྐད་ཅིག་མ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 1705]
སྐད་ཅིག་མ་ལ་ནི་སྐྱེ་བ་ལ་སོགས་པ་མི་མངོན་ནོ། །

[Block 1706]
མི་མངོན་པ་དེ་དག་ནི་མཚན་ཉིད་ཡིན་པར་འོས་པ་མ་ཡིན་ཏེ།

[Block 1707]
དེ་ཉིད་ཀྱི་ཕྱིར་མདོ་དེ་ལས།

[Block 1708]
འདུས་བྱས་སྐྱེ་བར་ཡང་མངོན་ནོ་ཞེས་གསུངས་སོ། །

[Block 1709]
ཡང་འདུས་བྱས་ཞེས་སྨོས་པ༌[^806]ནི་ཅི་ནས་ཀྱང་འདུས་བྱས་ཉིད་ཀྱི་མཚན་ཉིད་དག་ཡིན་ནོ་སྙམ་དུ་ཤེས་པར་བྱ་བའི༌[^807]ཆུ་དང་ཆུ་སྐྱར་ལྟར་རམ། དགེ་བ་དང་མི་དགེ་བ་ཉིད་ཀྱི་བུ་མོའི་མཚན་བཞིན་དུ་འདུས་བྱས་ཀྱི་དངོས་པོ་ཡོད་པ་ཉིད་ཀྱི་མཚན་ཉིད་དག་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ལྟར་ཤེས་ན་ནི་མི་རུང་ངོ་སྙམ་ནས་སྨོས་པ་ཡིན་ནོ། །

[Block 1710]
དེ་ལ་རྒྱུན་གྱི་དབང་པོ༌[^808]ནི་སྐྱེ་བ་ཡིན་ནོ། །

[Block 1711]
ལྡོག་པ་ནི་འཇིག་པ་ཡིན་ནོ། །

[Block 1712]
རྒྱུན་དེ་ཉིད་རྗེས་སུ་འཇུག་པ་ནི་གནས་པ་ཡིན་ནོ། །

[Block 1713]
དེའི་སྔ་ཕྱིའི་བྱེ་བྲག་ནི་གནས་པ་གཞན་དུ་འགྱུར་བ་ཉིད་ཡིན་ནོ། །

[Block 1714]
དེ་ལྟ་ཡིན་པས་ན། རིགས་ཀྱི་བུ་དགའ་བོའི་ཚོར་བ་ནི་རིག་བཞིན་དུ་སྐྱེའོ། །

[Block 1715]
རིག་བཞིན་དུ་གནས་སོ། །

[Block 1716]
རིག་བཞིན་དུ་ནུབ་པ་དང་། ཡོངས་སུ་ཟད་པ་དང་། ཡོངས་སུ་གཏུགས་པར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 1717]
འདིར་སྨྲས་པ།

[Block 1718 [VERSE]]
རྒྱུན་གྱི་དང་པོ་སྐྱེ་བ་ཡིན། །
ཆད་པ་འཇིག་པ་གནས་པ་སྟེ། །
དེ་ཉིད་སྔ་ཕྱིའི་བྱེ་བྲག་ནི། །
གནས་པ་གཞན་དུ་འགྱུར་བ་ཉིད། །

[Block 1719]
ཡང་འདིར་སྨྲས་པ།

[Block 1720 [VERSE]]
སྔོན་མེད་ལས་བྱུང་སྐྱེ་བ་སྟེ། །
རྒྱུན་གནས་དེ་ཆད་འཇིག་པ་ཡིན། །
རྒྱུན་གྱི་སྔ་ཕྱིའི་བྱེ་བྲག་ནི། །
གནས་པ་གཞན་དུ་འགྱུར་བར་འདོད། །
--- END BLOCKS ---
