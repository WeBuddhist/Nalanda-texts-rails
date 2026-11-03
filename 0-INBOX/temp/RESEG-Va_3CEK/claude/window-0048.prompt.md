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
གཉིས་ཕྱིར། རྣམ་པར་ཤེས་པ་ནི་གཉིས་ལ་བརྟེན་ནས་སྐྱེའོ་ཞེས་གསུངས་པ། གཉིས་གང་ཞེ་ན། མིག་དང་གཟུགས་རྣམས་ནས་ཡིད་དང་ཆོས་རྣམས་ཀྱི་བར་ཡིན་ཏེ། འདས་པ་དང་མ་འོངས་པ་དག༌[^1235]མེད་ན་དེ་ལ་དམིགས་པའི་རྣམ་པར་ཤེས་པ་གཉིས་ལ་བརྟེན་པར༌[^1236]མི་འགྱུར་རོ། །

[Block 1682]
རེ་ཞིག་ལུང་ལས་འདས་པ་དང་མ་འོངས་པ་ཡོད་པ་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 1683 [HEADING]]
#### རིགས་པ། ^2-22-2-0

[Block 1684]
རིགས་པས་ཀྱང་། ཡུལ་ཡོད་ཕྱིར། ཡུལ་ཡོད་ན་རྣམ་པར་ཤེས་པ་སྐྱེ་བར་འགྱུར་གྱི་མེད་པར་ནི་མ་ཡིན་ནོ། །

[Block 1685]
གལ་ཏེ་འདས་པ་དང་མ་འོངས་པ་མེད་ན་ནི་དམིགས་པ་མེད་པའི་རྣམ་པར་འགྱུར་ཏེ། དེ་བས་ན་དམིགས་པ་མེད་པའི་ཕྱིར་རྣམ་པར་ཤེས་པ་ཉིད་དུ་ཡང་མི་འགྱུར་རོ། །

[Block 1686]
འབྲས་ཕྱིར། གལ་ཏེ་འདས་པ་ཞིག་མེད་ན་ཚེ་ཕྱི་མ་ལ་ལས་དགེ་བ་དང་མི་དགེ་བའི་འབྲས་བུར་ཡང་ཇི་ལྟར་འགྱུར་ཏེ། འབྲས་བུ་བསྐྱེད༌[^1237]པའི་ཚེ་ནི་ད་ལྟར་གྱི༌[^1238]རྣམ་པར་སྨིན་པའི་རྒྱུ་ནི༌[^1239]མེད་དོ། །

[Block 1687]
དེ་ལྟ་བས་ན་བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི༌[^1240]འདས་པ་དང་མ་འོངས་པ་ཡོད་པ་ཁོ་ནའོ་ཞེས་ཟེར་རོ། །

[Block 1688]
ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་ཡིན་ཕན་ཆད་གདོན་མི་ཟ་བར་འདི་ཁས་བླང་བར་བྱ་དགོས་སོ་ཞེས་གྲགས་ཏེ།[^1241] འདི་ལྟར། དེ་ཡོད་སྨྲ་བའི་ཕྱིར་ཐམས་ཅད། །ཡོད་པར་སྨྲ་བར་འདོད། གང་དག་འདས་པ་དང་མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བ་ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་དེ་དག་གི༌[^1242]ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་ཡིན་གྱི། གང་དག་ད་ལྟར་བྱུང་བ་དང་འབྲས་བུ་མ་བསྐྱེད་པའི༌[^1243]ལས་འདས་པ་གང་ཡིན་པ་ཅུང་ཟད་ཅིག་ནི་ཡོད། མ་འོངས་པ་དང་འབྲས་བུ་བསྐྱེད་ཟིན་པའི་འདས་པ་གང་ཡིན་པ་ཅུང་ཟད་ཅིག་ནི་མེད་དོ་ཞེས་རྣམ་པར་ཕྱེ་སྟེ་སྨྲ་བ་དེ་དག་ནི་རྣམ་པར་ཕྱེ་སྟེ་སྨྲ་བ་དག་ཡིན་ནོ། །

[Block 1689 [HEADING]]
#### ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་རྣམ་བཞི། ^2-22-3-0

[Block 1690]
ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་དེ་དག་ཀྱང་དུ་ཞིག་ཅེ་ན། སྨྲས་པ། དེ་དག །

[Block 1691 [VERSE]]
རྣམ་བཞི་དངོས་དང་མཚན་ཉིད་དང་། །
གནས་སྐབས་གཞན་གཞན་འགྱུར་ཞེས་བྱ། །

[Block 1692 [HEADING]]
##### དངོས་པོ་གཞན་དུ་འགྱུར་བ། ^2-22-3-1-0

[Block 1693]
དངོས་པོ་གཞན་དུ་འགྱུར་བ་པ་ནི། བཙུན་པ་ཆོས་སྐྱོབ་ཡིན་ཏེ། དེ་ན་རེ་ཆོས་དུས་རྣམས་སུ་འཇུག་པ་ན་དངོས་པོ་གཞན་དུ་འགྱུར་གྱི་རྫས་གཞན་དུ་འགྱུར་བ་ནི་མ་ཡིན་ཏེ། དཔེར་ན་གསེར་གྱི་སྣོད་བཅོམ་ནས་གཞན་དུ་བྱེད་པ་ན། དབྱིབས་གཞན་དུ་འགྱུར་གྱི་ཁ་དོག་གཞན་དུ་འགྱུར་བ་ནི་མ་ཡིན་པ་དང་། ཡང་དཔེར་ན་འོ་མ་ཞོ་ཉིད་དུ་འགྱུར་བ་ན་རོ་དང་མཐུ་དང་སྨིན་པར་བྱེད་པ་དག །ཡོངས་སུ་འདོར་གྱི་ཁ་དོག་ནི་མ་ཡིན་པ་དེ་བཞིན་དུ་ཆོས་ཀྱང་མ་འོངས་པའི་དུས་ནས་ད་ལྟར་བྱུང་བའི་དུས་སུ་འོངས་པ༌[^1244]ན་མ་འོངས་པའི་དངོས་པོ་འདོར་གྱི་རྫས་ཀྱི་དངོས་པོ་ནི་མ་ཡིན་ནོ། །

[Block 1694]
དེ་བཞིན་དུ་ད་ལྟར་བྱུང་བ་ནས་འདས་པའི་དུས་སུ་འགྲོ་བ་ན༌[^1245]ད་ལྟར་བྱུང་བའི་དངོས་པོ་འདོར་གྱི། རྫས་ཀྱི་དངོས་པོ་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 1695 [HEADING]]
##### མཚན་ཉིད་གཞན་དུ་འགྱུར་བ། ^2-22-3-2-0

[Block 1696]
མཚན་ཉིད་གཞན་དུ་འགྱུར་བ་པ་ནི་བཙུན་པ་དབྱངས་སྒྲོགས་ཡིན་ཏེ། དེ་ན་རེ་ཆོས་དུས་རྣམས་སུ་འཇུག་པ་ན་འདས་པ་ནི་འདས་པའི་མཚན་ཉིད་དང་ལྡན་ལ་མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བའི་མཚན་ཉིད་དག༌[^1246]ནི་མི་ལྡན་པ་མ་ཡིན་ནོ། །

[Block 1697]
མ་འོངས་པ་ནི་མ་འོངས་པའི་མཚན་ཉིད་དང་ལྡན་པ་ལ༌[^1247]འདས་པ༌[^1248]ད་ལྟར་བྱུང་བ་དག་ནི་མི་ལྡན་པ་མ་ཡིན་ནོ། །

[Block 1698]
དེ་བཞིན་དུ་ད་ལྟར་བྱུང་བ་ཡང་འདས་པ་དང་མ་འོངས་པ༌[^1249]དག་དང་མི་ལྡན་པ་མ་ཡིན་ཏེ། དཔེར་ན་སྐྱེས་བུ་བུད་མེད་དག་ཅིག༌[^1250]ལ་ཆགས་པ་ལྷག་མ་རྣམས་ལ་འདོད་ཆགས་དང་བྲལ་བ་མ་ཡིན་པ་བཞིན་ནོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 1699 [HEADING]]
##### གནས་སྐབས་གཞན་དུ་འགྱུར་བ། ^2-22-3-3-0

[Block 1700]
གནས་སྐབས་གཞན་དུ་འགྱུར་བ་པ་ནི་བཙུན་པ་དབྱིག་བཤེས་ཡིན་ཏེ། དེ་ན་རེ་ཆོས་དུས་རྣམས་སུ་འཇུག་པ་ན་གནས་སྐབས་དང་གནས་སྐབས་སུ་ཕྱིན་ནས་གནས་སྐབས་གཞན་གྱི་སྒོ་ནས་གཞན་དང་གཞན་ཞེས་སྟོན་གྱི་རྫས་གཞན་གྱི་སྒོ་ནས་ནི་མ་ཡིན་ཏེ། དཔེར་ན་རི་ལུ༌[^1251]གཅིག་གཅིག་གི་ཤོད་མིག་ཏུ་གཞག་ན་གཅིག་ཅེས་བྱ། བརྒྱའི་ཤོད་མིག་ཏུ་གཞག་ན་བརྒྱ། སྟོང་གི་ཤོད་མིག་ཏུ་གཞག་ན་སྟོང་ཞེས་བྱ་བ་བཞིན་ནོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 1701 [HEADING]]
##### གཞན་དང་གཞན་དུ་འགྱུར་བ། ^2-22-3-4-0

[Block 1702]
གཞན་དང་གཞན་དུ་འགྱུར་བ༌[^1252]ནི་བཙུན་པ་སངས་རྒྱས་ལྷ་ཡིན་ཏེ། དེ་ན་རེ་ཆོས་དུས་རྣམས་སུ་འཇུག་པ་ན་སྔ་མ་དང་ཕྱི་མ་ལ་ལྟོས་ནས་གཞན་དང་གཞན་ཞེས་བརྗོད་དེ། དཔེར་ན་བུད་མེད་གཅིག་ལ་མ་ཞེས་ཀྱང་བྱ། བུ་མོ་ཞེས་ཀྱང་བྱ་བ་བཞིན་ནོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་སྟེ། དེ་ལྟར་ན་བཞི་པོ་དེ་དག་ནི་ཐམས་ཅད་ཡོད་པར་སྨྲ་བ་དག་ཡིན་ནོ། །

[Block 1703]
དེ་དག་ལས་དང་པོ་ནི་ཡོངས་སུ་འགྱུར་བར་སྨྲ་བའི་ཕྱིར་གྲངས་ཅན་གྱི་ཕྱོགས་ལ་བསླན་པར་བྱའོ། །

[Block 1704]
གཉིས་པའི་ཡང་ཐམས་ཅད་ལ་མཚན་ཉིད་ཐམས་ཅད་དང་ལྡན་པའི་ཕྱིར་དུས་འཆོལ་བར་འགྱུར་ཏེ། སྐྱེས་བུ་ཞིག༌[^1253]བུད་མེད་ལ་ལ་ལ་ནི་འདོད་ཆགས་ཀུན་དུ་འབྱུང་ལ། ལ་ལ་ལ་ནི་ལྡན་པ་འབའ་ཞིག་གོ་ཞེས་བྱ་བ་འདིར༌[^1254]ཅི་ཞིག་མཚུངས། བཞི་པའི་ཡང་དུས་གཅིག་ལ་དུས་གསུམ་ཆར་དུ་འགྱུར་ཏེ། འདས་པའི་དུས་ལ་སྔ་མ་དང་ཕྱི་མའི་སྐད་ཅིག་མ་དག་ནི་འདས་པ་དང་མ་འོངས་པ་ཡིན་ལ། དབུས་ཀྱི་སྐད་ཅིག་མ་ནི་ད་ལྟར་བྱུང་བར་འགྱུར་རོ། །

[Block 1705]
དེ་ལྟ་བས་ན་དེ་དག་ཐམས་ཅད་ཀྱི་ནང་ན།

[Block 1706]
གསུམ་པ་བཟང་སྟེ། གནས་སྐབས་གཞན་དུ་འགྱུར་བ༌[^1255]གང་ཡིན་པའོ། །

[Block 1707 [HEADING]]
#### བྱ་བས་དུས་རྣམས་རྣམ་གཞག་པ། ^2-22-4-0

[Block 1708]
དེ་ཡིས༌[^1256]ནི། བྱ་བ་ཡིས། དུས་རྣམས་རྣམ་གཞག་གང་གི་ཚེ་ཆོས་དེ་བྱ་བ་མི་བྱེད་པ་དེའི་ཚེ་མ་འོངས་པ་ཡིན་ལ། གང་གི་ཚེ་བྱེད་པ་དེའི་ཚེ་ནི་ད་ལྟར་བྱུང་བ་ཡིན། གང་གི་ཚེ་བྱས་ནས་འགགས་པ་དེའི་ཚེ་ནི་འདས་པ་ཡིན་ནོ་ཞེས་གྲག་གོ། །

[Block 1709]
དེ་དག༌[^1257]ཐམས་ཅད་ནི་ཡོངས་སུ་གོ་ན་གལ་ཏེ་འདས་པ་ཡང་རྫས་སུ་ཡོད་ལ་མ་འོངས་པ་ཡང་རྫས་སུ་ཡོད་ན། ཅིའི་ཕྱིར་འདས་པའམ་མ་འོངས་པ་ཞེས་བྱ་བ་བརྗོད་པར་བྱ་དགོས་སོ། །

[Block 1710]
བྱ་བ་ཡིས། དུས་རྣམས་རྣམ་གཞག་ཅེས་བཤད་པ་མ་ཡིན་ནམ། གལ་ཏེ་ཁྱིམ༌[^1258]དེ་ལྟ་ན་ད་ལྟར་བྱུང་བའི་མིག་དེ་དང་འདྲ་བའི་བྱ་བ་གང་ཞིག་ཡིན། འབྲས་བུ་འབྱིན་པ་དང་འཛིན་པ་ཡིན་ནོ། །

[Block 1711]
འོ་ན་ནི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ལ་སོགས་པ་འདས་པ་རྣམས་ཀྱང་འབྲས་བུ་འབྱིན་པའི་ཕྱིར་བྱ་བ་འམ་བྱ་བ་བྱེད༌[^1259]དུ་ཐལ་བར་འགྱུར་བས་མཚན་ཉིད་འཆོལ་བར་འགྱུར་རོ། །

[Block 1712]
འདི་ཡང་བརྗོད་པར་བྱ་དགོས་ཏེ། གལ་ཏེ་ཆོས་དེའི་བདག་ཉིད་ཁོ་ནར་ཡོད་ན་རྟག་ཏུ་བྱ་བ་བྱེད་པ་ལ། བགེགས༌[^1260]སུ་བྱེད། གང་གིས་ན་རེས་འགའ་ནི་བྱ་བ་བྱེད་ལ་རེས་འགའ་ནི་མ་ཡིན་ཞེས་བྱ། གལ་ཏེ་རྐྱེན་རྣམས་མ་ཚོགས་པ་ཡིན་ནོ་ཞེ་ན། མི་རུང་སྟེ། རྟག་ཏུ་ཡོད་པ་ཉིད་དུ་ཁས་བླངས་པའི་ཕྱིར་རོ། །

[Block 1713]
བྱ་བ་འདས་པ་དང་མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བ་ཞེས་བྱ་བ་གང་ཡིན་པ། དེ་ཡང་ཇི་ལྟར། བྱ་བ་ལ་ཡང་བྱ་བ་གཞན་ཞིག་ཡོད་དམ་ཅི། འོན་ཏེ་དེ༌[^1261]འདས་པ་ཡང་མ་ཡིན། མ་འོངས་པ་ཡང་མ་ཡིན་ད་ལྟར་བྱུང་བ་ཡང་མ་ཡིན་ལ། ཡོད་པ་ཡང་ཡིན་ན་ནི་དེས་ན་འདུས་མ་བྱས་ཡིན་པས་རྟག་ཏུ་ཡོད་དོ་ཞེས་བྱ་བར་འགྱུར་ཏེ། དེའི་ཕྱིར་གང་གི་ཚེ་ཆོས་བྱ་བ་མི་བྱེད་པ་དེའི་ཚེ་མ་འོངས་པ་ཡིན་ནོ་ཞེས་བརྗོད་པར་མི་བྱའོ། །

[Block 1714]
གལ་ཏེ་ཆོས་ལས་བྱ་བ་གཞན་ཞིག་ཡིན་ན་ནི་སྐྱོན་དེར་ཡང་འགྱུར་བ་ཞིག་ན་དེ་ནི་གཞན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་སྐྱོན་དེར་མི་འགྱུར་རོ། །

[Block 1715]
དེ་ལྟ་ན་ནི༌[^1262]འོ་ན་དེ་ཉིད་དུས་སུ་མི་རུང་སྟེ། གལ་ཏེ་ཆོས་ཁོ་ན་བྱ་བ་ཡིན་ན་ཆོས་དེ་དེའི་བདག་ཉིད་ཁོ་ནར་ཡོད་བཞིན་དུ་ཅིའི་ཕྱིར་རེས་འགའ་ནི་འདས་པ་ཞེས་བྱ། རེས་འགའ་ནི་མ་འོངས་པ་ཞེས་བྱ་སྟེ། དུས་རྣམ་པར་གཞག་པ་མི་འགྲུབ་བོ། །

[Block 1716]
ཆོས་གང་མ་སྐྱེས་པ་དེ་ནི་མ་འོངས་པ་ཡིན་ནོ། །

[Block 1717]
གང་སྐྱེས་ལ་མ་ཞིག་པ་དེ་ནི་ད་ལྟར་བྱུང་བ་ཡིན་ནོ། །

[Block 1718]
གང་ཞིག་པ་དེ་ནི་འདས་པ༌[^1263]ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་མི་འགྲུབ་པ་ཅི་ཞིག་ཡོད། འདིར་དེ་ཉིད་བརྗོད་པར་བྱ་དགོས་ཏེ། གལ་ཏེ་ཇི་ལྟར་ད་ལྟར་གྱི་རྫས་སུ་ཡོད་པ་དེ་བཞིན་དུ། འདས་པ་དང་མ་འོངས་པ་ལ༌[^1264]ཡང་ཡོད་ན་ནི། དེ་བཞིན་དུ། ཡོད་ན་ཅིའི་ཕྱིར་མ་སྐྱེས་ཤིག །[^1265]ཆོས་དེའི་རང་གི་ངོ་བོ་ཁོ་ནར་ཡོད་ན་ནི༌[^1266]ཇི་ལྟར་ན་མ་སྐྱེས་པ་ཞེས་བྱ་བའམ། ཞིག་པ་ཞེས་བྱ་བ་འདི་འགྲུབ་པར་འགྱུར། གང་ཞིག་མེད་པས་མ་སྐྱེས་པ་ཞེས་བྱ་བ་ནི༌[^1267]སྔོན་ཅི་ཞིག་མ་བྱུང་བར་འགྱུར།[^1268] གང་ཞིག་མེད་པས་ཞིག་པ་ཞེས་བྱ་བ་ཡང་ཕྱིས་ཅི་ཞིག་མེད་དེ། དེ་ལྟ་བས་ན་གལ་ཏེ་མ་བྱུང་བ་ལས་བྱུང་བ་དང་། བྱུང་ནས་ཀྱང་ཡང་མི་འབྱུང་བར་མི་འདོད་ཕན་ཆད་དུས་གསུམ་རྣམ་པ་ཐམས་ཅད་དུ་མི་འགྲུབ་བོ། །

[Block 1719]
གང་ཡང་འདུ་བྱེད་ཀྱི་མཚན་ཉིད་དང་ལྡན་པའི་ཕྱིར་རྟག་པ་ཉིད་དུ་ཐལ་བར་མི་འགྱུར་རོ་ཞེས་སྨྲས་པ་དེ་ཡང་སྐྱེ་བ་དང་། འཇིག་པ་དག་མི་རུང་བའི་ཕྱིར་ཚིག་ཙམ་སྟེ། ཆོས་དེ་རྟག་པ༌[^1269]ཡང་ཡོད་ལ་མི་རྟག་པ་ཡང་ཡིན་ནོ་ཞེས་བྱ་བའི་ཚིག་གི་ལུགས་འདི་ནི་སྔོན་མ་བྱུང་བ་ཡིན་ནོ། །

[Block 1720]
ཡང་སྨྲས་པ།
--- END BLOCKS ---
