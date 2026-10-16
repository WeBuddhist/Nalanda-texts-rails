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
ཐམས་ཅད་ཅེས་བྱ་བ་ནི་དེའི་གཉེན་པོ་སྟེ༌[^986]མང་པོའོ། །

[Block 1717]
འདི་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་མཚན་ཉིད་ཀྱི་སྐྱེ་དགུ་ལ་ཕན་པར་འཇུག་པའི་མཚན་ཉིད་དེ། དེའི་གཉེན་པོའི༌[^987]འབངས་ཞེས་སྨོས་ཏེ། ཁྱད་པར་མེད་པས་བཟང་པོ་དང་། བར་མ་དང་། ཐ་མའི་འགྲོ་བ་དག་གོ། །

[Block 1718]
འདི་ལྟ་བུ་ཆོས་གང་གི་ལམ་ལགས༌[^988]ཞེས་བྱ་བ་ནི་སྔོན་མ་ཐོས་པའི་ཆོས་ཀྱི་ལམ་མོ། །

[Block 1719]
བདག་ཅག་ལ་ཞེས་བྱ་བ་ནི་བདག་གི་དོན་ནི༌[^989]དྲུག་པའོ། །

[Block 1720]
དེ་ལ་ཤ་དང་ཁྲག་ཅེས་བྱ་བ་དེ་ལ་ནི་འདི་དག་ལ་ཤ་དང་ཁྲག་ཡོད་བཞིན་དུ་ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་སོ། །

[Block 1721]
བདག་གི་ཤ་སྦྱིན་པར་སྩོལ་བ་འདི་ཐོང་ཞེས་བསྟན་པ་ལ་ཇི་ལྟར་མི་གཏང་བ༌[^990]ཡིན་ཞེ་ན། ངེད་ཅག་ལྟ་བུ་ཞེས་བྱ་བ་སྨོས་ཏེ། འཕགས་པ་རྣམས་ལ་ནི་མེད་ཅེས་བྱ་བ་ཡིན་ཏེ། བརྫུན་གྱི་ཚིག་མེད་པའི་ཕྱིར་དང་། ཚོགས་པར་མི་འབྱུང་བ༌[^991]དང་། རྩུབ་པའི་ཚིག་མེད་པའི་ཕྱིར་རོ། །

[Block 1722]
གསལ་བར་བསླངས་པ་ལ་ཞེས་བྱ་བ་ནི་ངེད་ཅག་ལྟ་བུས་ནི་མ་བསླངས་ཀྱང་ཡོད་པར་གྱུར་ན་མཚན་མ་ལས་ཤེས་པར་བྱ་སྟེ། སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1723]
ད་ནི་ལྔ་པོ་འདི་དག་ཅེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐང་གི་ལན་ཆོས་ཀྱི༌[^992]ལམ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། ཆོས་ཀྱི་བཀའ་ཁྲིམས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1724]
མདུན་དུ་འགྲོ་བ་ཡིན་པས་ཐོག་མར་འགྲོ་བའོ། །

[Block 1725]
ངན་པའི་ལམ་དུ་ཞེས་བྱ་བ་ནི་བརྫུན༌[^993]དུ་སྨྲ་བ་དང་། ཚིག་རྩུབ་པོའི་མཚན་ཉིད་ཀྱིས་སོ། །

[Block 1726]
ངའི་ཡང་ཡིན་ལ་སྤྱོད་པའི་ལམ་ཡིན་བས་ངའི་སྤྱོད་པའི༌[^994]ལམ་མོ། །

[Block 1727]
དེའི་རྗེས་སུ་འགྲོ་བ་ནི་ངའི་སྤྱོད་པའི་ལམ་གྱི་རྗེས་སུ་འཇུག་པ་དེ་དག་གོ། །

[Block 1728]
ང་ཡི་འབངས་རྣམས་གནས་སབས་ཇི་ལྟར་གྱུར། །ཞེས་བྱ་བ་ནི་ཤིན་ཏུ་ཉམས་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1729]
དེ་ལྟར་འདིར་སྦྱིན་པས་ནི་ཆོས་ཀྱི་ལམ་ཉིད་དུ་བསྟན་ལ། སྦྱིན་པ་མ་ཡིན་པས་ནི་ཆོས་མ་ཡིན་པའི་ལམ་ཉིད༌[^995]དུ་བསྟན་ནས། ང་ནི་གང་སྔར་བསྟན་པའི་འབངས་ཐམས་ཅད་མགོན་མ་མཆིས་པར་བགྱིས་པའམ་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་པ་སྟེ། འདི་ཡང་སྐྱེ་དགུ་རྣམས་ཀྱི་དོན་གྱི་ཕྱིར། །ཞེས་སྨོས་ཏེ། འབངས་ཐམས་ཅད་མགོན་མ་མཆིས་པར་བགྱིས་པ་ཉིད་འགྲོ་བའི་དོན་བཟང་པོ་སྟེ། འགྲོ་བའི་དོན་ནུས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1730]
སེར་སྣས་ཕྲོགས་པ་ཉིད་ནི་སེར་སྣས་ཕྲོགས་པར་གྱུར་པ་སྟེ། སེར་སྣས་ཕྲོགས་པའི་སྙིང་གང་ཡིན་པ་དེ་ནི་སེམས་སེར་སྣས་ཕྲོགས་པར་གྱུར་པའོ། །

[Block 1731]
དགའ་བ་དང་གུས་པ་ནི་དགའ་བ་དང་གུས་པ་སྟེ། ང་ལ་དགའ་བ་དང་གུས་པ་ནི་ང་ལ་དགའ་བ་དང་གུས་བ་དང་བཅས་པའོ། །

[Block 1732]
བྱམས་པ་དང་། བག་ཕབ་པ་ནི་བྱམས་པས་བག་ཕབ་པ་སྟེ། དེ་གཉིས་ཀྱི༌[^996]སྙིང་པོ་གང་ཡིན་པ་དེ་ནི་བྱམས་པ་དང་། བག་ཕབ་པའི་སྙིང་པོ་ཉིད་དོ། །

[Block 1733]
འདི་ལྟར་བདག་ཅག་ལ་མི༌[^997]བྱམས་བ་ཅི་ལས་གྱུར་ཞེས་བྱ་བ་འདིས་ནི་བག་ཕབ་པའི་སྙིང་པོ་བསྟན་ཏོ། །

[Block 1734]
རྗེའི་ཆེད་དུ་འཚལ་བ༌[^998]ལ་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་། འདི་ལྟར་བདག་ཅག་ལ་མི་བྱམས་པ་ཅི་ལས་གྱུར་ཞེས་བྱ་བའི་ལན་ནི། ང་ཁྱེད་ལ་མི་འཇར་ཞིང་མི་བྱམས་པ་ཡང་མ་ཡིན་ལ་ཞེས་བྱ་བ་ཡིན་ཏེ། འཇར་བ་ནི་བག་འབེབས་པར་བྱེད་པའི་དོན་ཏོ། །

[Block 1735]
འཇར་བ་མེད་པ་ནི་མི་འཇར་བའོ། །

[Block 1736]
མི་འཇར་བ་ཡང་ཡིན་ལ་མི་བྱམས་པ་ཡང་ཡིན་པས་ན་མི་འཇར༌[^999]ཞིང་མི་བྱམས་པའོ། །

[Block 1737]
ཤ་དང་ཁྲག་བདག་ཅག་ལ་མཆིས་བཞིན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ལན་ནི། མ་བྱིན་དུ་དོགས་པ་ཡང་མེད་མོད་ཀྱི་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 1738]
ཡོངས་སུ་དོགས་ཤིང་རྒལ༌[^1000]དཀའ་བ་གང་ཡིན་པ་དེ་ནི་དོགས་ཤིང་རྒལ༌[^1001]དཀའ་བ་སྟེ། དཀའ་བས་རྟོགས་པ་གང་ཡིན་པའི་བྱམས་པའི་ལམ་གང་ཡིན་པ་དེ་ནི་རྟོགས་པར་དཀའ་པའི་དོགས་པའོ། །

[Block 1739]
རྟོགས་པར་དཀའ་བ་ཡང་ཡིན་ལ་རྒལ་བར༌[^1002]དཀའ་བ་ཡང་ཡིན་པས་དོགས་པ་དང་རྒལ་དཀའ་ཞིང་རྟོགས་པར་དཀའ་བ་སྟེ། སྐལ་བའི༌[^1003]ཚུལ་འདི་ཆུང་བ༌[^1004]དང་ཟད་པར་གྱུར་པ་དང་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 1740]
སློང་བ་རྣམ་པར་མཛེས་པ་གང་ཡིན་པ་དེ་ནི་སློང་བ་མཛེས་པ་སྟེ། སློང་བ་འཕེལ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1741]
དབུལ་བ་ཞེས་བྱ་བའི་ཚིག་གིས་ནི་འབྱོར་པ་དང་ལྡན་པ་ནོར་གྱིས་རྒུད་པར་གྱུར་པ་ལ་སྟེ། དབུལ་ཞིང་ཕོངས་པར་གྱུར་པ་ལའོ། །

[Block 1742]
ཡང་ན་དབུལ་བ་ཉིད་སློང་བ་འཕེལ་བ་ཡིན་ནོ། །

[Block 1743]
ཡང་ན་ནོར་རིམ་གྱིས་ཉུང་ངུར་གྱུར་པ་ནི་མཛའ་བོ་ནོར་དང་ལྡན་པ་རྣམས་ལ་སློང་བ་འཕེལ་བ་མཛེས་པ་ཡིན་ཏེ། དེ་ཟད་ཅིང་དབུལ་པོར་གྱུར་པ་མཛའ་བོ་དག་ལ་སློང་བ་འཕེལ་བ་མཛེས་པ་ཡིན་ནོ། །

[Block 1744]
འདི་ཇི་ལྟར་ཤེས་པར་བྱ་སྟེ། ནོར་དང་ལྡན་པ་ནི་དབུལ་པོ་ལ་མི་མཛེས་ཏེ། དེ་བས་ན་ང་ལ་ནི་ནོར་ཟད་པ་ཡང་མེད་ལ། གང་ལྟ་བུས་བསྟན་པ་དེ་ཇི་ལྟར་ནོར་དང་ལྡན་པ་ལ་སྦྱར་ཏེ། འབྱོར་པ་ཉུང་ངུར༌[^1005]གྱུར་པ་ལ་ཡང་མི་རིགས་ན། འབྱོར་པ་ཆུང་བའི་མཛའ་བོ་ལ་ནོར་དང་ལྡན་པས་བསླང་བ་ལྟ་ཅི་སྨོས་ཏེ། དེ་བས་ན་ཁྱད་པར་བསྟན་པར་འགྱུར་ཏེ།

[Block 1745 [VERSE]]
ཤིན་ཏུ་སྐལ་བས་འགྱུར་བའི༌[^1006]ཕྱིར་རོ། །
སྐྱེ་བོ་ཕོངས་པ་རྣམས་ཀྱིས༌[^1007]ཕྱིར་བསྐྱེད་པའི། །
ལུས་ནི་ང་བདག་ཉིད་ལ་ཡོད་བཞིན་དུ། །

[Block 1746]
ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པའི་དངོས་པོ་ཐ་དད་པ་མེད་པར་བསྟན་ཏོ། །

[Block 1747]
ལུས་ནི་ཆེན་པོ་ཤ་རྒྱས་ཞེས་བྱ་བ་འདིས་ནི་ཉུང་ངུར༌[^1008]གྱུར་པ་མེད་པར་བསྟན་ཏོ། །

[Block 1748]
ཁྱེད་ལ་ཞེས་བྱ་བ་འདིས་ནི་མི་འཇར་ཞིང་མི་བྱམས་པའི་སྐྱོན་མེད་ཅིང་ལུས་རིང་བ་དག་ལ་སློང་བ་ནི་རིགས་པ་མ་ཡིན་ནོ་ཞེས་སྨོས་ཏེ། བརྒྱ་ལ་འབྱོར་པ་ཟད་པར་མ་གྱུར་ན་ཡང་བྱམས་ཤིང་ཡིད་གཅུགས་པར༌[^1009]བསྟན་པའི་ཕྱིར་དབུལ་བ་ལ་ཡང་སློང་བར་མི་རིགས་སོ། །

[Block 1749]
ནམ་ཡང་ནང་གི་དངོས་པོ་ནི་སློང་བར་རིགས་པ་མེད་དེ། གཞན་ལ་གནོད་པ་དང་འབྲེལ་པའི་ཕྱིར་རོ་ཞེས་བསྟན་པའི་ཕྱིར། མི་ཤེས་གཞན་གྱི་གནོད་པ་འང་མི་བཟོད་ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་སོ། །

[Block 1750]
མི་ཤེས་པ་ཞེས་བྱ་བ་ནི་སྔོན་མ་མཐོང་ཞིང་མ་འདྲིས་པའོ། །

[Block 1751]
ཁྱེད་ཀྱི་གནོད་པ་བདག་གིས་ག་ལ་བཟོད། །[^1010]ཅེས་བྱ་བ་ནི་འདི་ལྟར་བྱམས་ཤིང་ཡིད་གཅུགས༌[^1011]པའི་དངོས་པོ་དག་ལ་སྟེ། །དེས་ན་ཁྱེད་ལ་ཡང་གནོད་པ་བཏང་སྙོམས་སུ་བྱ་ཞིང་། གང་འདི་དག་ཁྱེད་ལ་སློང་ན་དེ་ལ་སྦྱིན་པའི་རྗེས་སུ་ཡི༌[^1012]རང་བར་བྱས་ཏེ། འདི་ལྟར་ངའི་སྦྱིན་པ་ལ་ཁྱེད་ཅག་གིས་རྗེས་སུ་ཡི་རང་བ་དེ་ལྟར་བྱའོ།[^1013] །ཇི་ལྟར་འོག་ནས་བརྗོད་པ་ཞེས་བྱ་བ་ནི་མདུན་ནས་སོ། །

[Block 1752]
དེ་ལྟར་རེ་ཞིག་སྦྱིན་པའི་བྱ་བ་རིགས་པ་ཉིད་དུ་བསྟན་ནས། སྔར་བཤད་པའི་དབྱེ་བས་དབྱེ་བ་བསྟན་པའི་ཕྱིར། དེ་བས་ན་ང་ལ༌[^1014]རབ་ཏུ་བྱམས་པའི༌[^1015]ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་སོ། །

[Block 1753]
ཆོས་ཀྱི་བགེགས་ལ་འཛེམ་པ་མེད་པ་ཞེས་བྱ་བས་ནི་དེ༌[^1016]དག་ཆོས་མ་ཡིན་པ་ཉིད་དུ་བསྟན་པས་འཛེམ་པ་བསྐྱེད་པའི༌[^1017]མཚན་ཉིད་ཀྱི་དབྱེ་བ་བསྟན་ཏོ། །

[Block 1754]
ཇི་ལྟར་དབྱེ་བ་དེ་ཡང་ཆོས་མ་ཡིན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 1755]
ད་ནི་ལོག་པ་ཉིད་དུ་བསྟན་པར་འདོད་པས། ངའི་དོན་དུ་ཁྱོད་ཅི་སྤྱོད་པ་འདི་ལྟ་བུ་བྱ་བ་མི་རིགས་ཏེ་ཞེས་བྱ་བ་འདི་བརྩམས་སོ། །
--- END BLOCKS ---
