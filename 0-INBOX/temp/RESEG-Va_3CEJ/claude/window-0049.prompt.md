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

[Block 1721 [VERSE]]
སྐད་ཅིག་མ་ཡི་ཆོས་ལ་ནི། །
གནས་པ་མེད་ན་འཇིག་པར་འགྱུར། །
དེ་ཡང་འཇིག་འགྱུར་དེ་ཡི་ཕྱིར། །
དེ་ཡི་དེར་རྟོགས༌[^809]དོན་མེད་དོ། །

[Block 1722]
དེ་ལྟ་བས་ན་གནས་པ་ནི་རྒྱུན་ཁོ་ན་ཡིན་ནོ། །

[Block 1723]
དེ་ལྟར་བཤད་ན་ཆོས་མངོན་པ་ལས་གནས་པ་གང་ཞེ་ན། འདུས་བྱས་སྐྱེ་བ་རྣམས་མི་འཇིག་པ་ཡིན་ནོ་ཞེས་བསྟན་པ་འདི་ཡང་འཐད་པ་ཡིན་ཏེ། སྐྱེས་པ་སྐད་ཅིག་མ་ལ་ནི༌[^810]འཇིག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1724]
གང་ཡང་ཡེ་ཤེས་ལ་འཇུག་པ་ལས།

[Block 1725]
སེམས་གཅིག་ལ་འབྱུང་བ་གང་ཞེ་ན། སྨྲས་པ། སྐྱེ་བའོ། །

[Block 1726]
འཇིག་པ་གང་ཞེ་ན། འཆི་བའོ། །

[Block 1727]
གནས་པ་གཞན་དུ་འགྱུར་བ་ཉིད༌[^811]གང་ཞེ་ན། རྒ་བའོ་ཞེས་གསུངས་པ་དེར་ཡང་རིས་མཐུན་པའི་སེམས་ལ་རུང་བར་འགྱུར་རོ། །

[Block 1728]
སྐད་ཅིག་མ་རེ་རེ་ལ་ཡང་རྫས་གཞན་དུ་རྟོགས་པ༌[^812]མེད་པ༌[^813]བཞིན་དུ་འདུས་བྱས་ཀྱི་དེ་དག་རུང་སྟེ། ཇི་ལྟ་ཞེ་ན། སྐད་ཅིག་མ་རེ་རེ་ལ་མ་བྱུང་བ་ལས་བྱུང་བ་ནི་སྐྱེ་བའོ། །

[Block 1729]
བྱུང་ནས་མེད་པ་ནི་འཇིག་པའོ། །

[Block 1730]
སྔ་མ་སྔ་མ་དང་ཕྱི་མ་ཕྱི་མའི་སྐད་ཅིག་མ་རྗེས་སུ་འབྲེལ་བ་ནི་གནས་པའོ། །

[Block 1731]
དེའི་མི་འདྲ་བ་ཉིད་ནི་གནས་པ་གཞན་དུ་འགྱུར་བ་ཉིད་དོ། །

[Block 1732]
འོ་ན་གང་གི་ཚེ་འདྲ་བར་ཡང་སྐྱེའོ་ཞེ་ན། དེ་དག་ཁྱད་པར་མེད་པ་མ་ཡིན་ནོ། །

[Block 1733]
འདི་ཇི་ལྟར་ཤེས་ཤེ་ན། རྡོ་རྗེ་ལ་སོགས་པ་འཕངས་པ་དང་མ་འཕངས་པ་དང་། སྟོབས་ཆེན་པོ་དང་། སྟོབས་ཆུང་ངུས་འཕངས་པ་བུལ་བ་དང་མྱུར་བ་དང་། ཆེས་དལ་བ་དང་། ཆེས་མྱུར་བར་ལྟུང་བའི་དུས་ཀྱི་བྱེ་བྲག་ལས་དེའི་འབྱུང་བ་རྣམས་ཡོངས་སུ་གྱུར་པའི་བྱེ་བྲག་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 1734]
འདུས་བྱས་རྣམས་ནི་བྱེ་བྲག་གི་ཁྱད་པར་ཆེན་པོ་མཚར་ཅིག་མེད་པས་གཞན་དུ་འགྱུར་བ་ཉིད་ཡོད༌[^814]དུ་ཟིན་ཀྱང་འདྲ་བ་བཞིན་དུ་སྣང་ངོ་། །འོ་ན་ནི་སྒྲ་དང་མེ་ལྕེའི་སྐད་ཅིག་མ་ཐ་མ་དང་། ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་ཚེའི་སྐྱེ་མཆེད་དྲུག་ལ་སྐད་ཅིག་མ་ཕྱི་མ་མེད་པའི་ཕྱིར་གནས་པ་གཞན་དུ་འགྱུར་བ༌[^815]མེད་པས་མཚན་ཉིད་རྣམ་པར་གཞག་པ་མ་ཁྱབ་པ་ཅན་དུ་འགྱུར་རོ། །

[Block 1735]
འདུས་བྱས་ཀྱི་མཚན་ཉིད་ནི་གནས་པ་ཁོ་ན་ཡང་མ་ཡིན་གྱི་གནས་པ་གཞན་དུ་འགྱུར་བ་ཉིད་ཀྱང་ཡིན་ནོ། །

[Block 1736]
དེའི་ཕྱིར་གང་ལ་གནས་པ་ཡོད་པ་དེ་ལ་གདོན་མི་ཟ་བར་གཞན་དུ་འགྱུར་བ་ཉིད་ཀྱང་ཡོད་པས་རྣམ་པར་གཞག་པ་ཉམས་པ་མེད་དོ། །

[Block 1737]
མདོར་ན་བཅོམ་ལྡན་འདས་ཀྱིས་ནི་མདོ་འདི་ལས༌[^816]འདུས་བྱས་ཞེས་བྱ་བ་ནི། གང་མ་བྱུང་བ་ལས་འབྱུང་བ་དང་། བྱུང་ནས་ཀྱང་མི་འབྱུང་བ་འདི་འདུས་བྱས་ཀྱི་མཚན་ཉིད་ཡིན་པར་གསུངས་ལ། འདིའི་གནས་པ་ཞེས་བྱ་བ་རྒྱུན་གང་ཡིན་པ་དེ་ཡང་གཞན་དང་གཞན་དུ་འགྱུར་བ་ཡིན་ན། འདིར་སྐྱེ་བ་ལ་སོགས་པ་རྫས་གཞན་དག་གིས་ཅི་ཞིག་བྱ།

[Block 1738]
ད་ནི་ཇི་ལྟར་ན་མཚན་ཉིད་ཀྱི་གཞིའི་ཆོས་དེ༌[^817]ཉིད་ཀྱི་མཚན་ཉིད་དུ་རུང་བར་འགྱུར་ཞེ་ན། རེ་ཞིག་ཇི་ལྟར་ན་སྐྱེས་བུ་ཆེན་པོའི་མཚན་རྣམས་སྐྱེས་བུ་ཆེན་པོ༌[^818]ལས་མི་གཞན་པ་ཡིན། བ་ལང་ཉིད་ཀྱི་མཚན་ཉིད་ལྐོག་ཤལ་དང་། མཇུག་མ་དང་། ནོག་དང་། རྨིག་པ་དང་། རྭ་རྣམས་ཀྱང་བ་ལང་ལས་མི་གཞན་པ་ཡིན། སའི་ཁམས་ལ་སོགས་པའི་མཚན་ཉིད་སྲ་བ་ཉིད་ལ་སོགས་པ་རྣམས་ཀྱང་དེ་དག་ལས་མི་གཞན་པ་ཡིན། གཞན་ཡང་ཇི་ལྟར་གྱེན་དུ་འགྲོ་བ་ལས་ནི༌[^819]ཐག་རིང་པོ་ནས་དུ་བ་ལ་དུ་བ་ཉིད་དུ་ཤེས་མོད་ཀྱི། དེ་ནི་དེ་ལས་ཀྱང་མི་གཞན་པ་ལྟར་འདིར་ཡང་ཚུལ་དེ་ཉིད་ཡིན་ནོ། །

[Block 1739]
འདུས་བྱས་གཟུགས་ལ་སོགས་པ་རང་གི་ངོ་བོ་བཟུང་ཡང་ཇི་སྲིད་དུ་སྔ་ན་མེད་པ་དང་ཕྱིས་མེད་པ་དང་རྒྱུན་གྱི་བྱེ་བྲག་མི་ཤེས་པ་དེ་སྲིད་དུ་འདུས་བྱས་ཉིད་དུ་མི་ཤེས་ཏེ། དེ་ལྟ་བས་ན་དེ་ཉིད་ཀྱིས་དེ་མཚོན་པ་ཡང་མ་ཡིན་ལ། དེ་དག་ལས་སྐྱེ་བ་ལ་སོགས་པ་རྫས་གཞན་ཉིད་དུ་ཡོད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1740]
འོན་ཏེ་སྐྱེ་བ་ལ་སོགས་པ་རྫས་གཞན་ཞིག་ཏུ་གྱུར་ན་ཡང་ཅི་ལྟར༌[^820]འགྱུར་ཞེ་ན། དེ་དག་ནི་ལྷན་ཅིག་འབྱུང་བའི་ཕྱིར་ཆོས་གཅིག་དུས་གཅིག་ཏུ་སྐྱེས་པ༌[^821]དང་གནས་པ་དང་རྒས་པ་དང་ཞིག་པར་འགྱུར་རོ། །

[Block 1741]
མ་ཡིན་ཏེ། བྱ་བའི་དུས་ཐ་དད་པའི་ཕྱིར་རོ། །

[Block 1742]
སྐྱེ་བ་མ་འོངས་པ༌[^822]ནི་བྱ་བ་བྱེད་དེ། འདི་ལྟར་མ་སྐྱེས་པ་སྐྱེད་དོ། །

[Block 1743]
བསྐྱེད་ཟིན་པའི་ཆོས་ལ་ནི་ད་ལྟར་གནས་པ་ལ་སོགས་པ་བྱ་བ་བྱེད་པས་གང་གི་ཚེ་སྐྱེ་བ་དེ༌[^823]ཚེ་གནས་པའམ། རྒ་བ་འམ། འཇིག་པར་མི་འགྱུར་རོ། །

[Block 1744]
རེ་ཞིག་འདིར་ཅི་མ་འོངས་པ་རྫས་སུ་ཡོད་དམ་མེད་ཅེས་བྱ་བ་འདི་དཔྱད་དགོས་པར་འགྱུར་ཏེ། ཕྱིས་ནི་སྐྱེད་པར་བྱེད་དམ་འོན་ཏེ་མ་ཡིན་ཞེས་བྱ་བ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 1745]
དེ་ཡོད་དུ་ཆུག༌[^824]ན་ཡང་སྐྱེ་བ་བྱ་བ་བྱེད་ན་ཇི་ལྟར་མ་འོངས་པར༌[^825]འགྲུབ་པར་འགྱུར། དེ་ལྟ་བས་ན་མ་འོངས་པའི་མཚན་ཉིད་ཀྱང་བརྗོད་པར་བྱའོ། །

[Block 1746]
བྱུང་བ་ཡང་བྱ་བ་ཞིག་པ་ཡིན་ན་ཇི་ལྟར་ན་ད་ལྟར་འགྲུབ་པར་འགྱུར། དེ་ལྟ་བས་ན་ད་ལྟའི་མཚན་ཉིད་ཀྱང་བརྗོད་པར་བྱའོ། །

[Block 1747]
གནས་པ་ལ་སོགས་པ་ཡང་ཅིག་ཅར་བྱ་བ་ལ་འཇུག་པ་ཡིན་ན་ནི་སྐད་ཅིག་མ་གཅིག་ཁོ་ན་ལ་ཆོས་གནས་པ་དང་རྒ་བ་དང་འཇིག་པར༌[^826]ཐལ་བར་འགྱུར་ཏེ། འདི་གང་གི་ཚེ་གནས་པས་གནས་པར་བྱེད་པ་དེ་ཉིད་ཀྱི་ཚེ་རྒ་བས་རྒ་བར་བྱེད་ཅིང་མི་རྟག་པ་ཉིད་ཀྱིས་འཇིག་པར་བྱེད་པའི་ཕྱིར་འདི་ཅི་དུས་དེར་གནས་སམ། འོན་ཏེ་རྒ་བའམ། [^827]འོན་ཏེ་འཇིག་པར་འགྱུར། གང་ཡང་སྐྱེ་བ་ལ་སོགས་པ་རྣམས་ཀྱང་བྱ་བ་རིམ་གྱིས་བྱེད་དོ་ཞེས་ཟེར་བ་དེའི་ལྟར་ན་སྐད་ཅིག་མ་གཅིག་ལ་གནོད་པར་འགྱུར་རོ། །

[Block 1748]
འོན་ཏེ་ཇི་སྐད་དུ་ཁོ་བོ་ཅག་གི་སྐད་ཅིག་མ་ནི་ཇི་ཙམ་གྱིས་འདི་ཐམས་ཅད་རྫོགས་པར་འགྱུར་བ་དེ་ཡིན་ནོ་ཞེས་བརྗོད་ན། དེ་ལྟ་ན་ཡང་དེ་དག་དང་ལྷན་ཅིག་འབྱུང་བ་ལས་རེ་ཞིག་གནས་པས་ནི་གནས་པར་བྱེད་ཀྱི་རྒ་བས་ཀྱང་རྒས་པར་མི་བྱེད་ལ།

[Block 1749]
མི་རྟག་པ་ཉིད་ཀྱིས་ཀྱང་འཇིག་པར་མི་བྱེད་དོ་ཞེས་བྱ་བ་འདི་ག་ལས།

[Block 1750]
གནས་པ་སྟོབས་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 1751]
ཕྱིས་ཅིའི་ཕྱིར་སྟོབས་དང་མི་ལྡན་པ་ཉིད་དུ་འགྱུར། གང་གི་ཕྱིར་ན་འདི་ཆོས་དང་ལྷན་ཅིག་ཏུ་མི་རྟག་པ་ཉིད་ཀྱིས་འཇོམས། བྱ་བ་བྱས་ཟིན་པས་ཡང་མི་ནུས་ཏེ་སྐྱེ་བ་བཞིན་ནོ། །

[Block 1752]
སྐྱེ་བས་ནི་མི་ནུས་པར་རིགས་ཏེ། སྐྱེ་བས་བསྐྱེད་པར་བྱ་བ་ད་ལྟ་ཉིད་དུ་ཁྱེར་ཏེ་འོངས་ནས་ཡང་བཀུར་བར་ནི༌[^828]མི་ནུས་སོ། །

[Block 1753]
གནས་པས་ནི་གནས་པར་བྱ་བ་ཡེ་གནས་པར་བྱ་བར་ཡང༌[^829]ནུས་སོ། །

[Block 1754]
དེ་ལྟ་བས་ན་གང་མི་ནུས་པ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1755]
ཡང་ན་འདི་ལ་བགེགས་བྱེད༌[^830]པ་ཡང་གང་ཞིག་ཡིན་ཏེ། [^831]རྒ་བ་དང་མི༌[^832]རྟག་པ་ཉིད་དེ་དག་ཁོ་ན་ཡིན་ནོ། །
--- END BLOCKS ---
