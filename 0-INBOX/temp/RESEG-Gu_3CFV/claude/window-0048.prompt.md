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
དེའི་ཕྱིར་མ་བསམས་པར༌[^1071]བརྒལ་བ་དང༌[^1072]བརྒྱལ་བ་ལ་གདབ་པ་དག་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཁྲུས་ལ་རྩེ་གཅིག་པ་ཉིད་ཀྱི་ཆུ་ཉམས་སུ་མྱོང་བ་གང་ཡིན་པ་དེ་ནི་ཁྲུས་གཞན་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1682]
འདིར་གཞུང་ནི་དགེ་སློང་དག་ཆུ་ཀླུང་རྒལ་བར་བྱེད་དོ་ཞེས་གསུངས་པ་དང་། འདིར་གཞུང་གཞན་ལས་ཀྱང་རྐྱལ་བ༌[^1073]ལ་ཆུས༌[^1074]དབང་བསྐུར་བ་དང་། ཟམ་པ་ལས་ལྟུང་བ་ཆུ་ཀླུང་ལས་རྒལ་བར་བྱེད་པ་དང་། ཆུས་གང་བ་ལ་མཆོང་བར་བྱེད་པ་ལ་ཡང་ལྟུང་བ་མེད་དོ། །

[Block 1683]
དེ་བཞིན་དུ་མདུན་རོལ་དུ་འགྲོ་ཞིང་རྒྱ་མཚོ་ལ་གཟིངས་ནས་འགྲོ་བ་རྣམས་ལ་བཤང་བ་དང་གཅི་བ་བྱེད་པ་ཡང་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1684]
དེ་དང་དེའི་ངོ་བོ་གཞན་གྱི་རྐྱེན་རྣམས་ལ་ཆུ་ཉམས་སུ་མྱོང་བ་ལ་ཉེས་པ་མེད་པ་ཉིད་དུ་བསྟན་པའོ། །

[Block 1685]
ཇི་སྲིད་དུ་ཁྲུས་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་ཀྱིས་རིག་པར་བྱའོ། །

[Block 1686]
ཨ་མྲ༌[^1075]པ་རན་ཏའི་ཡུལ་དག་ལ་འདི་ནི་འདི༌[^1076]མེད་པར་ཤེས་པར་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ཞེས་བྱ་བ་ནི་ཁྲུས་ངེས་པའོ། །

[Block 1687]
འདིར་གཞུང་ནི་ཀོ་ལྤགས་ཀྱི་གཞི་དག་ལ་ཨ་མྲ༌[^1077]པ་རན་ཏའི་ཡུལ་དག་ཏུ་ནི་སྐྱེ་བོའི་ཚོགས་རྣམས་ལ་རྟག་ཏུ་ཁྲུས་བྱ་བ་རྗེས་སུ་གནང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1688]
འདིར་ཡུལ་དེ་ཉིད་དུས་སུ་རིག་པར་བྱའོ། །

[Block 1689]
དེའི་ཕྱིར་དེ་ཉིད་ཉེ་བར་བཞག་སྟེ། དུས་མ་ཡིན་པར་ཡང་ཁྲུས་ལ་འཇུག་པར་བྱའོ། །

[Block 1690]
ཆོ་ག་བཙན་པོ་ཡོད་ན་བག་ཡངས་བྱ་བ་ལ་བརྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བག་ཡངས་སུ་གྱུར་པའི་རྟོགས་པ༌[^1078]ནི་བག་ཡངས་སུ་གྱུར་པའོ། །

[Block 1691]
ཆོ་ག་བཙན་པོ་གཞན༌[^1079]ཡོད་ན་བག་ཡངས་སུ་བྱ་བ་ལ་བརྟེན་པར་མི་བྱའོ། །

[Block 1692]
འདིར་གཞུང་ནི་བཙུན་པ་བཅོམ་ལྡན་འདས་ཀྱིས་བྲམ་ཟེའི་བུ་མོ་ལ༌[^1080]ཇི་སྐད་དུ་ཡུལ་མཐའ་འཁོབ་དག་ཏུ་འདུལ་བ་འཛིན་པ་དང་ལྔའི་ཚོགས་ཀྱིས་བསྙེན་པར་རྫོགས་པར་བྱའོ་ཞེས་གསུངས་པ་དེ་ལ། བཙུན་པ་གལ་ཏེ་བཅུའི་ཚོགས་མཆིས་བཞིན་དུ་འདུལ་བ་འཛིན་པ་དང་ལྔའི་ཚོགས་ཀྱིས་བསྙེན་པར་རྫོགས་པར་བགྱི་ན་བསྙེན་པར་རྫོགས་ཞེས་བགྱིའམ། ཉེ་བ་འཁོར་བསྙེན་པར་རྫོགས་ཞེས་བྱ་སྟེ། བསྙེན་པར་རྫོགས་པར་བྱེད་པ་དག་ལ་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པས་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1693]
ཚིག་འདི་ནི་ཆོ་ག་བཙན་པོ་ཡོད་ན་ཞེས་བྱ་བའི་ཚིག༌[^1081]གིས་ཏེ། རྣམ་པར་གཞག་པར་བྱས་པར་གྱུར་པ་ནི་མ་ཡིན་ནོ། །

[Block 1694]
དེ་ལྟ་བས་ན་དེ་ལྟ་བུའི་རིགས་ཅན་ལ་དབང་དུ་བྱེད་པ་ཉིད་ནི་འདིར་རོ། །

[Block 1695]
ཁྲུས་བྱེད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1696]
ཅི་ཞིག་བྱས་ན་དུད་འགྲོ་གསོད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གསོད་པའི་སེམས་ཀྱིས༌[^1082]དུད་འགྲོ་ལ་བསྣུན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གང་གི་ཚེ༌[^1083]བྱས་པ་ལ་གང་བསྐྱེད་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གཞི་དེས་དེའི་ཚེའམ་གཞན་གྱི་ཚེ་ཤི་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཞི་དེས་ཞེས་བྱ་བ་ནི་གསོད་པའི་སེམས་ཀྱིས་བསྣུན་པའི་གཞི་དེས་སོ། །

[Block 1697]
དེའི་ཚེའམ་ཞེས་བྱ་བ་ནི༌[^1084]དུས་དེ་ཉིད་ཀྱི་ཚེའོ། །

[Block 1698]
གཞན་གྱི་ཚེ་ཞེས་བྱ་བ་ནི་བསྣུན་པའི་དུས་ཀྱི་འོག་དུས་གཞན་གྱི་ཚེ་ཤི་ནའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1699]
གཞན་གྱི་ཚེ་ཞེས་བྱ་བ་འདི་ནི་གཞི་དེས་ཞེས་བྱ་བ་བྱེ་བྲག་ཏུ་བསྟན་པའོ། །

[Block 1700]
དེའི་ཚེའམ་ཞེས་བྱ་བ༌[^1085]འདི་ལ་ཡང་རྣམ་པར་དཔྱད་པར་བྱ་བ་མེད་པས་གང་ཞིག་འདིར་ཞུ་བ༌[^1086]ལས་སྦྱོར་བ་གཅིག་གིས་བྱས་ན་ཡང་གསོད་པར་བྱ་བ་ཇི་སྙེད་པ་རེ་རེ་ལ༌[^1087]ལྟུང་བྱེད་རེ་རེར་འགྱུར་རོ། །

[Block 1701]
སེམས་ཅན་རེ་རེ་དེ་དང་འབྲེལ་པ་ཞེས་བྱ་བ་འདིས་དེ་བསྡུས་པར་རིག་པར་བྱའོ། །

[Block 1702]
ལུས་དེ༌[^1088]དང་འབྲེལ་པ་ནི་ཐ་མི་དད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཐམས་ཅད་འདིར་གསོད་པའི་ཕམ་པར་འགྱུར་བ་ལ་རིག་པར་བྱའོ། །

[Block 1703]
སེམས་ཅན་གྱི་གཟུགས་སེམས་ཅན་མ་ཡིན་པ་ལ་ནི་ཉེས་བྱས་བྱེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་ཤིང་ལས་བྱས་པའམ་ས་ལས་བྱས་པའི་གཟུགས་ལ་བསྣུན་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། འདི་ནི་རིག་པར་མ་གྱུར་པར་ཤེས་པར་མི་བྱའོ། །

[Block 1704]
སེམས་ཅན་གྱི་འདུ་ཤེས་དང་འབྲེལ་པའི་འདུ་ཤེས་ལ་འདིར་དངོས་པོ་ལས་ཡོད་པར་གྱུར་པ་ཉིད་ཀྱིས་དུད་འགྲོའི་རྣམ་པ་ཉིད་ལ་ནི་འདིར་གཏོགས་པའི་ཁ་ན་མ་ཐོ་བར་རིག་པར་བྱའོ། །

[Block 1705]
གཞན་གྱི་རྣམ་པ་ཉིད་ལ་ནི་མི་གསོད་པ་དང་འབྲེལ་པའོ། །

[Block 1706]
དུད་འགྲོ་གསོད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1707]
ཅི་ཞིག་རྗེས་སུ་སྒྲུབ༌[^1089]ན་འགྱོད་པ་བསྐྱེད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཁྱོད་བསྙེན་པར་རྫོགས་པ་མ་ཡིན་ཞིང་ཕམ་པར་འགྱུར་བ་བྱུང་ངོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དགེ་སློང་མ་ཡིན་པའི་དོན་གྱིས་འགྱོད་པ་བསྐྱེད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པ་དགེ་སློང་མ་ཡིན་པ་ཉིད་དུ་ཇི་སྲིད་བསྙེན་པར་རྫོགས་པའི་དངོས་པོ་ཉམས་པ་ཉིད་དུ་གསལ་བར་བྱེད་ཅིང་དགེ་སློང་མ་ཡིན་པ་ཉིད་དུ་གསལ་བར་བྱེད་པ་དེ་རྣམ་པར་རིག་པའི་རྫས་དེ་ཐམས་ཅད་ཀྱིས་ཚེ་དང་ལྡན་པ་ཁྱོད་ལ་དགེ་སློང༌[^1090]གི་ཚུལ་ག་ལ་ཡོད་དེ་བྲམ་ཟེ་ཉིད་ཀྱང་ག་ལ་ཡོད། ཚེ་དང་ལྡན་པ་ནི་བྲམ་ཟེ་རབ་ཏུ་བྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ཀྱང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1708]
འདིར་དགོས་པ་ནི་རིགས་དམིགས་ཀྱིས་བསལ་བ་ལ་རྣམ་པར་གཞག་པར་རིག་པར་བྱའོ། །

[Block 1709]
མིའི་སྐྱོན་ནས་སྨྲ་བའི་བསམ་པས་གོ་བར་མི་བྱེད་ཅིང་དེ་ཁ་ན་མ་ཐོ་བ་ཉམས་པའི་བསམ་པ་ཉིད་ནི་གཉིས་ཀའི་བསམ་པ་ཉིད་ལ་གཉིས་ཀ་ཞེས་བྱ་བའོ། །སུ་ལ་འགྱོད་པ་བསྐྱེད་ཅེ་ན། དེའི་ཕྱིར་དགེ་སློང་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཅི་བསམ་པ་གང་ཡང་རུང་བས་སམ་ཞེ་ན། དེའི་ཕྱིར་བདེ་བ་ལ་མི་རེག་པ་བསྐྱེད་པའི་སེམས་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། །འདིར་བདེ་བ་ལ་མི་རེག་པ་ཞེས་བྱ་བ་ནི་དགེ་སློང་ལ་ཡིད་ལ་གཅགས་པ་བསྐྱེད་པ་གང་ཡིན་པ་དེ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1710]
བཞད་གད་ཀྱིས་ཀྱང་འགྱོད་པ་བསྐྱེད་པའི༌[^1091]བསམ་པས་ཞེས་སྨོས་ཏེ། འདིར་ན་སྨད་པར་ཡོད་པར་འགྱུར་རམ་ཞེས་བྱ་བའི་དགོས་པ་སྲིད་པས་གནས་སྐབས་པ་དེ་བཟློག་པའི་ཕྱིར་བརྗོད་པར་བྱ་སྟེ། བཞད་གད་ཀྱིས་ཀྱང་ཞེས་བྱ་བ་སྨོས་ཏེ། ཅི་འགྱོད་པ་སྐྱེས་པ་ཁོ་ན་འམ་ཞེ་ན། མ་ཡིན་ཏེ། དེའི་ཕྱིར་འགྱོད་པ་མ་སྐྱེས་ན་ཡང་ངོ་། །གཞན་གྱིས་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་གཞན་གྱི༌[^1092]འགྱོད་པ་བསྐྱེད་པ་ལ་ཉེས་བྱས་སོ། །

[Block 1711]
འགྱོད་པ་བསྐྱེད་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1712]
ཅི་ཞིག་བྱས་ན་ག་ག་ཚིལ་བྱེད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་ལ་སོར་མོ་འམ་ཁུ་ཚུར་རམ་གྲེ་མོ་འམ་ཕྲག་པའམ་མགོ་འམ་རྐེད་པ་འམ་བརླ་འམ་པུས་མོ་འམ་བྱིན་པ་འམ་རྐང་པའམ། མཐེ་བོ་ལ་སོགས་པ་དག་གིས་ག་ག་ཚིལ་བྱེད་པས༌[^1093]རེག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རེག་པའི་བྱེ་བྲག་ཉམས་སུ་མྱོང་བ་དང་། ཉམས་སུ་མྱོང་དུ་བཅུག་པ་དག་ལ་ནི་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་རོ། །

[Block 1713]
དེ་ལྟར་ན་ཡང་རང་གི་འམ་གཞན་གྱི་ལུས་ཀྱི་དབང་པོ་ཉམས་པ་ཉིད་ལ་རེག་ན་ནི་ཉེས་བྱས་ཀྱི་ཚིག་གོ། །

[Block 1714]
དེ་ལྟ་བས་ན་སོགས༌[^1094]པ་ཞེས་བྱ་བའི་སྒྲས་ནི་རང་གི་ལུས་ཀྱི་ཡན་ལག་གཞན་དག་ཀྱང་འཕངས་པ་ཡིན་གྱི། གོས་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 1715]
ལུས་མ་ཡིན་པས་ལུས་མ་ཡིན་པ་ལ་རེག་པ་དང་སྐྲ་དང་སེན་མོ་དང་སོ་རྣམས་ལ་ནི་ལུས་ཀྱི་དབང་པོ་ཉམས་པ་ཉིད་ཀྱི་ཚུལ་གྱི་རྗེས་སུ་འབྲངས་པས་ཉེས་བྱས་སུ༌[^1095]རྟོགས་པར་བྱའོ། །

[Block 1716]
ག་ག་ཚིལ་བྱེད་པ་འདི་ནི་མཚོན་པ་ཙམ་ཡིན་ཏེ། འབྲེལ་པ་བྱེད་པའི་རྣམ་པ་ལའོ། །

[Block 1717]
བཟོད་པ་དང་ཀུན་ནས་བཟོད་པ་དང་རེག་པ་ལ་ཡང་ཀུན་དུ་ཆགས་པ་མེད་པའི་སེམས་ཀྱིས་གལ་ཏེ་དེ་དང་འབྲེལ་པར་བྱེད་པའི་དེ་ལ་ཡང་འདིས་འཕངས་པའོ། །

[Block 1718]
བག་འཁུམས་པར་མི་བྱེད་པའི་རྣམ་པས་ཀུན་དུ་ཆགས་པ་མེད་པའི་སེམས་ཀྱིས་རེག་པ་ལ་ལྟུང་བ་མེད་པར་རིག་པར་བྱའོ། །ཅི་བསམ་པ་གང་ཡང་རུང་བས་རེག་ན་འམ་ཞེ་ན། དེའི་ཕྱིར་སྐྱི་གཡའ་བར་བྱ་བའི་སེམས་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་སྐྱི་གཡའ་ཞེས་བྱ་བ་ནི་བག་འཁུམས་པར་རིག་པར་བྱའོ། །

[Block 1719]
འདིར་ཀུན་དུ་འདོད་ཆགས་པ་དང་ལྡན་པའི་སེམས་ཀྱིས༌[^1096]རེག་པ་ལ་ནི་དགེ་འདུན་ལྷག་མར་གཏོགས་པའི་ཁ་ན་མ་ཐོ་བའི་ཆོ་ག་དམིགས་ཀྱིས་བསལ་བའོ། །

[Block 1720]
སྐྱི་གཡའ་བ་དང་ལྷན་ཅིག་འབྲེལ་པ་ལ་གསོད་པ་དང་རྡེག་པར་བྱེད་པའི་ལྟུང་བྱེད་དོ། །
--- END BLOCKS ---
