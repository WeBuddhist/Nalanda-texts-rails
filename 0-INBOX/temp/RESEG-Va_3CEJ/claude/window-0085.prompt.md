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
[Block 2976]
གཉིས་པ་ནི་དགྲ་བཅོམ་པའི་ཆོས་ཐ་མ་འདས་པ་དང་། ད་ལྟར་བྱུང་བ་རྣམས་སོ། །

[Block 2977]
གསུམ་པ་ནི་དེ་ལས་གཞན་པའི་ཆོས་འདས་པ་དང་། ད་ལྟར༌[^1678]བྱུང་བ་རྣམས་སོ། །

[Block 2978]
བཞི་པ་ནི་ཆོས་འདུས་མ་བྱས་རྣམས་སོ་ཞེས་ཟེར་རོ་ཞེས་གྲག་གོ། །

[Block 2979]
འདིར་མདོ་སྡེ་པ་རྣམས་རྒོལ་བར་བྱེད་དེ། ཅི་འདི་དག་གང་ཞིག་གང་འདོད་པའི་འདོད་རྒྱལ་དུ་འཆད་པ་ཞིག་གམ། འོན་ཏེ་མདོའི་དོན་ཡིན། སྨྲས་པ། མདོའི་དོན་ཡིན་ནོ། །

[Block 2980]
གལ༌[^1679]ཏེ་མདོའི་དོན་ཡིན་ནོ་ཞེ་ན། འདི་ནི་མདོའི་དོན་མ་ཡིན་ནོ། །

[Block 2981]
ཇི་ལྟར་ཞེ༌[^1680]ན་རེ་ཞིག་གནས་སྐབས་པའི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་འདི་ནི་བཅུ་གཉིས་དང་ལྡན་པའི་ཕུང་པོ་ལྔའི་གནས་སྐབས་ཀྱི་ཡན་ལག་བཅུ་གཉིས་པ་དག་ཡིན་ནོ་ཞེས་གང་སྨྲས་པ་ནི་མདོ་དང་འགལ་བ་ཡིན་ནོ། །

[Block 2982]
མདོ་ལས་ནི་མ་རིག་པ་གང་ཞེ་ན། སྨྲས་པ། སྔོན་གྱི་མཐའ་མི་ཤེས་པ་གང་ཡིན་པའོ་ཞེས་རྒྱས་པར་གསུངས་ཏེ། ངེས་པའི་དོན་གང་ཡིན་པ་དེ་ནི་དྲང་བའི་དོན་མ་ཡིན་པས་འདི་ནི་མདོའི་དོན་མ་ཡིན་ནོ། །

[Block 2983]
བསྟན་པའི་སྒོ་ནས་ཐམས་ཅད་ངེས་པའི་དོན་ཁོ་ན་ཡང་མ་ཡིན་གྱི། གཙོ་བོ་ཇི་ལྟ་བར་བསྟན་པར་ཡང་མཛད་དེ།

[Block 2984]
དཔེར་ན་གླང་པོ་ཆེའི་རྗེས་ལྟ་བུ་ལས།

[Block 2985]
སའི་ཁམས་གང་ཞེ་ན་ཞེས་བྱ་བའི་དབང་དུ་མཛད་ནས་འདི་ལྟ་སྟེ། སྐྲ་དང་ཁ༌[^1681]སྤུ་དག་གོ་ཞེས་གསུངས་པ་ལྟ་བུ་སྟེ། དེ་དག་ལ་ནི་གཟུགས་ལ་སོགས་པ་གཞན་ཡང་ཡོད་དེ། [^1682]དེ་བཞིན་དུ་འདིར་ཡང་གཙོ་བོ་ཇི་ལྟ་བ་བཞིན་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 2986]
འདི་ནི་དཔེ་མ་ཡིན་ཏེ། དེ་ལས་ནི་གང་གིས་ན༌[^1683]དེ་དག་མ་རྫོགས་པར་བསྟན་པར་འགྱུར་བ་སའི་ཁམས་ཀྱི༌[^1684]སྐྲ་ལ་སོགས་པ་སྟོན་པ་ནི་མ་ཡིན་གྱི་འོན་ཀྱང་དེ་ལས་ནི་སྐྲ་ལ་སོགས་པ་དག་ཁོ་ནས་སའི་ཁམས་སྟོན་པ་ཡིན་ཏེ། སྐྲ་ལ་སོགས་པ་མ་གཏོགས་པ༌[^1685]ཡང་སའི་ཁམས་མེད་པས་འདི་རྫོགས་པར་བསྟན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2987]
དེ་བཞིན་དུ་འདི་ལས་ཀྱང་མ་རིག་པ་ལ་སོགས་པ་རྣམས་ཡོངས་སུ་རྫོགས་པ་ཁོ་ནར་བསྟན་པ་ཡིན་གྱི་ལྷག་མ་དང་བཅས་པར་ནི་མ་ཡིན་ནོ། །

[Block 2988]
སྐྲ་ལ་སོགས་པ་མ་གཏོགས་པར་ཡང་མཆི་མ་དང་། མཆིལ་མ་དང་། སྣབས་ལ་སོགས་པ་དག་ལ་སའི་ཁམས་ཡོད་པ་མ་ཡིན་ནམ་ཞེ་ན། དེ་ཡང་བསྟན་ཟིན་པ་ཉིད་དེ། ལུས་འདི་ལ་གཞན་ཡང་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 2989]
ཡང་ན་གལ་ཏེ་དེ་ཁོ་ན་དང་འདྲ་བར་བསྟན་པར་ནུས་ན་མ་རིག་པའི་ལྷག་མ་ཡོད་ལ་རག་གོ། །

[Block 2990]
རིགས༌[^1686]ཐ་དད་པ་ནི་མ་རིག་པར་ཅིའི་ཕྱིར་བསྟན། གནས་སྐབས་དེ་དག་ལ་ཕུང་པོ་ལྔ་ཆར་ཡོད་དུ་ཟིན་ཀྱང་གང་ཞིག་ཡོད་དམ་མེད་ན་གང་ཡོད་པ་དང་མེད་པར་ངེས་པ་དེ་ཁོ་ན་ཡན་ལག་ཡིན་ནོ། །

[Block 2991]
དགྲ་བཅོམ་པ་ལ་ཕུང་པོ་ལྔ་ཡོད་ཀྱང་འདུ་བྱེད་རྣམས་ཀྱང་མི་འབྱུང་ལ།[^1687] བསོད་ནམས་མ་ཡིན་པ་དང་། མི་གཡོ་བར་ཉེ་བར་འགྲོ་བའི་རྣམ་པར་ཤེས་པ་དང་། སྲེད་པ་ལ་སོགས་པ་ཡང་མ་ཡིན་པས་མདོའི་དོན་ནི་ཇི་སྐད་བསྟན་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2992]
མུ་བཞིར་བཤད་པ་གང་ཡིན་པ་དེ་ལ་ཡང་། གལ་ཏེ་ཆོས་མ་འོངས་པ་རྣམས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ༌[^1688]ཡིན་ནམ༌[^1689]རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི༌[^1690]ཆོས་རྣམས་གང་ཞེ་ན། མ་རིག་པ་ནས་རྒ་ཤིའི་བར་དག༌[^1691]ཡིན་ནོ་ཞེས་གསུངས་པའི་མདོ་དང་འགལ་ལོ། །

[Block 2993]
ཡང་ན་སྐྱེ་བ་དང་། རྒ་ཤིའི་ཡན་ལག་དག་མ་འོངས་པའི་དུས་སུ་རྣམ་པར་གཞག་པར་མི་འདོད་པར་བྱ་དགོས་པས་ཆ་གསུམ་དུ་དགོད་པ་རྣམ་པར་ཉམས་པར་འགྱུར་རོ། །

[Block 2994]
དེ༌[^1692]སྡེ་པ་གཞན་དག་ན་རེ། དེ་བཞིན་གཤེགས་པ་རྣམས་བྱུང་ཡང་རུང་མ་བྱུང་ཡང་རུང༌[^1693]ཆོས་ཉིད་འདི་དག༌[^1694]ནི་གནས་པ་ཁོ་ནའོ་ཞེས་གསུངས་པའི་ཕྱིར་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ནི་འདུས་མ་བྱས་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2995]
དེ་ནི་དགོངས་པའི་དབང་གིས་དེ་བཞིན་ཡང་ཡིན་ལ་དེ་བཞིན་ཡང་མ་ཡིན་ནོ། །

[Block 2996]
རེ་ཞིག་ཇི་ལྟར་དེ་བཞིན་ཡིན། །ཡང་ན་ཇི་ལྟར་ན་དེ་བཞིན་མ་ཡིན་ཞེ་ན། གལ་ཏེ་དགོངས་པ་འདི་དེ་བཞིན་གཤེགས་པ་རྣམས་བྱུང་ཡང་རུང་མ་བྱུང་ཡང་རུང་རྟག་ཏུ་མ་རིག་པ་ལ་སོགས་པ་དག་ལ་བརྟེན་ནས་འདུ་བྱེད་ལ་སོགས་པ་རྣམ་པ༌[^1695]ཀུན་ཏུ་འབྱུང་གི་མ་བརྟེན་པར་རམ། གཞན་དག་ལ་བརྟེན་ནས་ནི་ནམ་ཡང་མ་ཡིན་པས་རྟེན་ཅིང་འབྲེལ་པ༌[^1696]ནི་རྟག་པའོ་ཞེས་བྱ་བ་ཡིན་ནོ་ཞེ་ན་ནི། དེ་དེ་བཞིན༌[^1697]ནོ་ཞེས་གཟུང་བར་བྱའོ། །

[Block 2997]
འོན་ཏེ་དགོངས་པ་འདི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་བྱ་བ་དངོས་པོ་གཞན་རྟག་པ༌[^1698]ཅུང་ཟད་ཅིག་ཡོད་དོ་ཞེས་བྱ་བ་ཡིན་ནོ༌[^1699]ཞེ་ན་ནི་དེ་དེ་ལྟ་མ་ཡིན་ནོ་ཞེས་དགག་པར་བྱའོ། ། ཅིའི་ཕྱིར་ཞེ་ན། འབྱུང་བ་ནི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2998]
དངོས་པོ་གཞན་རྟག་པ་ནི་མི་རྟག་པའི་མཚན་ཉིད་ཡིན་པར་ཡང་མི་རུང་ངོ་། །འབྱུང་བ་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་ཡིན་པའི་ཕྱིར་འདི་མ་རིག་པ་ལ་སོགས་པ་དང་ཅི་ཞིག་འབྲེལ་ན་གང་གི་ཕྱིར་དེ་དག་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་བརྗོད་པར་འགྱུར། རྟག་པ་ཞེས་ཀྱང་བྱ་ལ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་ཀྱང་བྱ་བས་ཚིག་གི་དོན་ཀྱང་ནུས་པ་མེད་པར་འགྱུར་རོ། །

[Block 2999 [HEADING]]
##### རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཚིག་གི་དོན། ^3-1-11-7-0

[Block 3000]
ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཞེས་བྱ་བའི༌[^1700]ཚིག་གི་དོན་གང་ཡིན་ཞེ་ན། རྟེན་ཅིང་འབྲེལ་པ་ཞེས་བྱ་བ་ནི་ཕྲད་པའི་དོན་ཏོ། །

[Block 3001]
ཨི་ཏི་ནི་འགྲོ་བའི་དོན་ཏོ། །

[Block 3002]
ཉེ་བར་བསྒྱུར་བའི་དབང་གིས་སྐད་ཀྱི་དབྱིངས༌[^1701]ཀྱི་དོན་ཡོངས་སུ་བསྒྱུར་བའི་ཕྱིར་ཕྲད་ནས་ཞེས་བྱ་བའི་དོན་གང་ཡིན་པ་དེ་ནི་རྟེན་ཅིང་འབྲེལ་ཏེ་ཞེས་བྱ་བའི་དོན་ཡིན་ནོ། །

[Block 3003]
པ་ད༌[^1702]ནི་ཡོད་པའི་དོན་ཏོ། །

[Block 3004]
སམ་དང་ཨུད་གོང་ན་ཡོད་ན༌[^1703]འབྱུང་བའི་དོན་ཏོ། །

[Block 3005]
དེས་ན་ཕྲད་ནས་འབྱུང་བ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡིན་ནོ། །

[Block 3006]
ཚིག་གི་དོན་འདི་ནི་རིགས་པ་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། བྱེད་པ་པོ་གཅིག་གིས༌[^1704]བྱ་བ་གཉིས་ནི་དུས་སྔར་ཏེ་ཞེས་བྱ་བའི་རྐྱེན་ཡིན་ཏེ། དཔེར་ན་ཁྲུས་བྱས་ཏེ་བཟའོ༌[^1705]ཞེས་བྱ་བ་ལྟ་བུ་ཡིན་ནོ༌[^1706]སྔར་ཕྲད་ནས་ཕྱིས་སྐྱེ་བར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་སྐྱེ་བའི་སྔོན་རོལ་ན་འགའ་ཡང་མེད་ལ། བྱེད་པ་པོ་མེད་པའི་བྱ་བ་ཡང་མེད་དོ། །

[Block 3007]
འདིར་སྨྲས་པ།

[Block 3008 [VERSE]]
གལ་ཏེ་འབྱུང་སྔོན་ཕྲད་ནས་ཡིན། །
མེད་ཕྱིར་རུང་བ་མ་ཡིན་ནོ། །
གལ་ཏེ་ལྷན་ཅིག་འདིར་དེ་ནི། །
མ་གྲུབ་སྔོན་དུ་བྱེད་ཕྱིར་རོ། །

[Block 3009]
འདི་ནི་ཉེས་པ་མེད་དེ། རེ་ཞིག་སྒྲ་པ་ལ་གནས་སྐབས་གང་གིས༌[^1707]ཆོས་ཞིག་སྐྱེ། ད་ལྟའི་འམ་འོན་ཏེ་མ་འོངས་པ་ཞིག་ཅེས་བྱ་བ་འདི་བྲི་བར༌[^1708]བྱའོ། །

[Block 3010]
དེ་ལས་ཅིར་འགྱུར། ཅི་སྟེ་ད་ལྟའི་ཞིག་སྐྱེའོ་ཞེ་ན་ནི། གལ་ཏེ་མ་སྐྱེས་ན་ཇི་ལྟར་ད་ལྟར་ཡིན། འོན་ཏེ་སྐྱེས་ཟིན་པ་ཞིག་ཡང་སྐྱེ་ན་ནི་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །ཅི་སྟེ་མ་འོངས་པ་ཞིག་སྐྱེའོ་ཞེ་ན། མེད་པ་ཇི་ལྟར་བྱེད་པ་པོ་ཉིད་དམ། བྱེད་པ་པོ་མེད་པའི་བྱ་བ་འགྲུབ། དེའི་ཕྱིར་གནས་སྐབས་གང་སྐྱེ་བའི་གནས་སྐབས་དེ་ཉིད་དང་ཕྲད་ནས་ཞེས་བྱ་བ་བཞིན༌[^1709]ནོ། །

[Block 3011]
གནས་སྐབས་གང་ཞིག་སྐྱེ་ཞེ་ན། སྐྱེ་བ་ལ་མངོན་དུ་ཕྱོགས་པའི་མ་འོངས་པ་སྟེ། གནས་སྐབས་དེ་ཁོ་ན་རྐྱེན་དང་ཕྲད་ནས་ཞེས་བྱའོ། །

[Block 3012]
སྒྲ་པའི་འདི་ལྟ་སྟེ། བྱེད་པ་པོ་དང་བྱ་བ་རྣམ་པར་འཇོག་པ་འདི་ཡང་གྲུབ་པ་མ་ཡིན་ཏེ། སྐྱེའོ༌[^1710]ཞེས་བྱ་བ་འདི་ནི་བྱེད་པ་པོ་ཡིན་ལ། སྐྱེ་ཞེས་བྱ་བ་འདི་ནི་བྱ་བ་ཡིན་ན་འདི་ལ༌[^1711]སྐྱེའོ་ཞེས་བྱ་བའི་དོན་ལས་བྱ་བ་གཞན་ཡང་མ་མཐོང་ངོ་། །དེ་ལྟ་བས་ན་ཐ་སྙད་དག་ལ་ཀླན་ཀ་མེད་དོ། །

[Block 3013]
ཚིག་གི་དོན་ནི་འདི་ཡོད་ན་འདི་འབྱུང་། འདི་སྐྱེས་པས་འདི་སྐྱེ་ཞེས་བྱ་བའི་དོན་གང་ཡིན་པ་དེ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་དོན་ཏོ་ཞེས་བྱ་བ་འདི་ཡིན་ནོ། །

[Block 3014]
འདིར་བཤད་པ།

[Block 3015 [VERSE]]
ཇི་ལྟར་མེད་པ་སྐྱེ་བ་ལྟར། །
མེད་པ་ཕྲད་པའང་དེ་དང་འདྲ། །
སྐྱེས་པ་སྐྱེ་ན་མཐར༌[^1712]ཐུག་མེད། །
འོན་ཏེ་སྔ་ན་ཡོད་ནའང་རུང་། །
--- END BLOCKS ---
