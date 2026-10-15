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
[Block 2031]
འདིར་དེ་རྣམས་ལ་ལས་བྱེད་པ་པོ་ཉིད་བཀག་པ་ལ་ཡོངས་སུ་བསྡུ་བའོ། །

[Block 2032]
ལྷག་མ་དང་བཅས་པའི་ཕྱིར་བཅོས་པ་ལ་ཞུགས་པ༌[^1797]ནི་འདོན་པར་བྱེད་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྔར་དེ་དག་ནི༌[^1798]བྱེད་པ་པོ་ཉིད་མ་ཡིན་ནོ་ཞེས་སྨོས་པ་དེའི་དམིགས་ཀྱིས་བསལ་བ་ཡིན་ཏེ། དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་ཕྱིར་འཆོས་པ་ལ་ཞུགས་པ་སྤོ་བ་ལ་སོགས་པ་དང་། དབྱུང་བ་ལ་སོགས་པས་གསོ་བར༌[^1799]ཞུགས་པའི་གང་ཟག་གིས་ནི་སོ་སོར་ཐར་པའི་མདོ་འདོན་དུ་རུང་བ་ཉིད་ཡིན་པའོ། །

[Block 2033]
བསྐོ་བ་པོ་གཞན་ཡོད་ན་ཉེས་བྱས་ཙམ་གྱི་མི་འཆགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2034]
དེ་ལས་གཞན༌[^1800]དེ་དག་གིས༌[^1801]ནི་ཐོས་པ་དང་བཅས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལས་གཞན་ཞེས་བྱ་བ་ནི་ལྷག་མ་དང་བཅས་པ༌[^1802]ཕྱིར་འཆོས་པ་ལ་ཞུགས་པས་སོ། །

[Block 2035]
གཞན་པ་དེ་དག་གིས་ནི་ཞེས་བྱ་བ་ནི་བསྙེན་པར་མ་རྫོགས་པ་ལ་སོགས་པ་རྣམས་ཀྱིས་སོ། །

[Block 2036]
ཐོས་པ་དང་བཅས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལས་སོ། །

[Block 2037]
དེ་དག་ལས་ཁ་ཅིག་དམིགས་ཀྱིས་བསལ་བ༌[^1803]བསྟན་པའི་ཕྱིར། མ་སྤངས་པ་དང་མ་ལོག་པ་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མ་སྤངས་ཞེས་སྨོས་པས་ནི་སྤངས་པ་ཐ་དད་པ་དང་གནས་ནས་ཕྱུང་བ་གཉིས་དམིགས་ཀྱིས་བསལ་བའོ། །

[Block 2038]
ཉམས་པ་དང་མཚམས་མེད་པ་བྱེད་པ་གཉིས་བྲལ་བའི་བསྙེན་པར་རྫོགས་པ་རྣམས་སྤོངས་པའི༌[^1804]ཕྱིར་ལོག་པ་ནི་འདིར་ལོག་པར་མངོན་པར་འདོད་པའོ། །

[Block 2039]
ཉམས་པ་དང་མཚམས་མེད་པ་བྱེད་པ་གཉིས་ནི་ལོག་པ་ཡིན་ཏེ། གང་ལས་ཤེ་ན། བདེ་འགྲོར་འགྲོ་བ་དང་རང་བཞིན་དུ་གནས་པའི་རྗེས་སུ་མཐུན་པ་ཉིད་ལས་སོ། །

[Block 2040]
བསྙེན་པར་རྫོགས་པ་དང་བྲལ་བ་ནི། ཡང་བསྙེན་པར་རྫོགས་པ་ལས་ལོག་པ་ཡིན་ནོ། །

[Block 2041]
མ་སྤངས་པ་དང་མ་ལོག་པ་མ་གཏོགས་པ་དེ་ལས་གཞན་པ་འདི་རྣམས༌[^1805]ཀྱིས་ཐོས་པ་དང་བཅས་པར་ལས་མི་བྱའོ་ཞེས་བྱ་བ་འདིས་ནི་བསླབ་པ་དང་། དེའི་ངོ་བོ་ཉིད་ཚོལ་བ་བྱིན་པ་དང་། བསྡིགས་པ་དང་སྨད་པ་དང་བསྐྲད་པ་དང་སྤངས་པ་རྣམས་བསྟན་པར་རིག་པར༌[^1806]བྱ་སྟེ། དེ་རྣམས་ཀྱིས་ཐོས་པ་དང་བཅས་པར་ལས་བྱེད་པ་ལ་ཉེས་པ་མེད་དོ། །

[Block 2042]
གནས་ནས་ཕྱུང་བ་ནི་རང་གིས་ལས་ཡང༌[^1807]ངོ་ཞེས་བྱ་བ་ཡང་མ་གཏོགས་སོ་ཞེས་བྱ་བ་རྗེས་སྙེགས༌[^1808]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་ཏེ། གནས་ནས་བྱུང་བ༌[^1809]དེའི་རང་གིས༌[^1810]བཟོད་པ་གསོལ་བ་དེ་ནི་དེས་ཐོས་པ་དང་བཅས་པར་བྱ་བ་ལས་གཞན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2043]
འོ་ན་ཐ་དད་པར་གནས་པ་རྣམས་ཀྱིས་ཞེས་བྱ་བ་བྱེ་བྲག་མེད་པར་འདི་རྣམས་སྤང་བར་སྨོས་སོ་ཞེ་ན། བདེན་མོད་ཀྱི་འོན་ཀྱང་ཡོངས་སུ་མ་བཟུང་བའི་ཐ་དད་པའི་གནས་ལ་དགོངས་ནས་ངེས་ཞེས་བྱ་བར་ཤེས་པར་བྱ་སྟེ། ཡོངས་སུ་བཟུང་བ་ལ་ཡོངས་སུ་སྤངས་པར༌[^1811]མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 2044]
གནས་ནས༌[^1812]ཕྱུང་བ་དག་ལ་ཐོས་པའི༌[^1813]ཉེན་ཀོར་སྤངས་ཏེ་མཐོང་བའི་ཉེན་ཀོར་དུ་བཞག་ནས། གཞན་འདོན་པས༌[^1814]མ་ཡིན་པའི་འདིར་ལུང་དུ་རིག་པར་བྱའོ། །

[Block 2045]
ནང་དུ་དྲི་བའི༌[^1815]ཕྱིར་གསོལ་བ་ལ་སོགས་པ་བསྙེན་པར་རྫོགས་པར་བྱ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ༌[^1816]ཡང་མ་གཏོགས་སོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^1817]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 2046]
ནང་དུ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་ནང་དུ་བར་ཆད་ཀྱི་ཆོས་གང་དག་དྲི་བ་སྟེ་དེའི་ཕྱིར་རོ། །

[Block 2047]
གསོལ་བ་ཞེས་བྱ་བ་ནི་དེ་དང་པོའི་ལས་ལ་བསྙེན་པར་རྫོགས་བཞིན་སྤངས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2048]
བསྙེན་པར་མ་རྫོགས་པས་ཐོས་པ་དང་བཅས་པའི་ལས་དེ་བྱའོ། །

[Block 2049]
དེ་ལས་གཞན་ཐོས་པའི་ཉན་ཀོར༌[^1818]དོར་བར་བྱས་ནས་མཐོང་བའི་ཉེན་ཀོར་དུ་བཞག་སྟེ་ཞེས་བྱ་བའི་ཚིག་ནི་འདིར་ལུང༌[^1819]ལས་སོ། །

[Block 2050]
ཅི་ཐོས་པར་བྱ་བ་མ་ཡིན་པ་ལས་མངོན་སུམ་དུ་བྱས་པ༌[^1820]དང་། རྗེས་སུ་བསྒྲག་པར༌[^1821]བྱ་བ་དང་། དེ་བྱ་བའི་ལས་ལ་བསྙིལ་ལམ་འོན་ཏེ་རྣམ་པ་གང་གིས་གཟུང་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དེ་དག་བྱ་བ་ལ་ལྟ་བའི༌[^1822]ཉེན་ཀོར་དུ་གཞག་པས་ནི་མངོན་སུམ་དུ་བསྒྲུབ་བོ། །

[Block 2051]
གོ་བར་བྱ་བས་ནི་རྗེས་སུ་བསྒྲག་པའོ༌[^1823]ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དག་བྱ་བ་ལས་ཞེས་བྱ་བ་ནི་མངོན་སུམ་དུ་བྱ་བ་དང་རྗེས་སུ་བསྒྲག་པར༌[^1824]བྱ་བ་ལའོ། །

[Block 2052]
མངོན་སུམ་དུ་བྱ་བ་ནི་གང་ཞིག་ཐོས་པར་བྱ་བ་ཡིན་པའི་ལས་བྱེད་པ་དེར་ལྟ་བའི༌[^1825]ཉེན་ཀོར་དུ་གཞག་པས་མངོན་སུམ་དུ༌[^1826]བསྒྲུབ་པར་བྱའོ། །

[Block 2053]
རྗེས་སུ་བསྒྲག་པ༌[^1827]ནི་ཐོས་པར་བྱ་བ་མ་ཡིན་པའི་ལས་བྱ་བ་ལ་སོགས་པའི་བྱ་བས་རྗེས༌[^1828]སུ་བསྒྲག་པར༌[^1829]བསྒྲུབ་པར་བྱ་སྟེ། ཁྱོད་ལ་གསོལ་བ་དང་བཞིའི་ལས་བྱ་བ་ལས་གསོལ་བ་ནི་བྱས་ཟིན་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གོ་བར་བྱ་བས་སོ། །

[Block 2054]
སྨྱོས་པའི་གནང་བ་དང་ཕྱག་མི་བྱ་བ་དང་མི་སྨྲ་བ་དང་། ལོངས་མི་སྤྱོད་པ་དང་གཙུག་ལག་ཁང་གི་སྡོམ་པ་དག་ནི་མངོན་སུམ་དུ་མ་གྱུར་པར་རོ་ཞེས་བྱ་བ་ནི། གཙུག་ལག་ཁང་ལ་སོགས་པ་རེ་རེ་ལ་སྡོམ་པའི་སྒྲ་སྦྱར་བར་བྱ་སྟེ། གཙུག་ལག་ཁང་གི་སྡོམ་པ་དང་སྨྱོས་པའི་སྡོམ་པ་དང་ཕྱག་མི་བྱ་བའི་སྡོམ་པ་དང་། ལོངས་མི་སྤྱོད་པའི་སྡོམ་པ་ཞེས་བྱ་བའོ། །

[Block 2055]
འདིར་གཞུང་ནི་མ་མོ་ལས།

[Block 2056]
མངོན་སུམ་དུ་མ་གྱུར་པར༌[^1830]བྱ་བའི་ལས་བཅུ་གང་ཞེ་ན། ལྷུང་བཟེད་ཁ་སྦུབ་པ༌[^1831]དང་། ལྷུང་བཟེད་ཁ་སྦུབ་བག་ཡངས་སུ་བྱ་བ་དང་། བསླབ་པའི་སྡོམ་པ་དང་བསླབ་པའི་སྡོམ་པ་བག་ཡངས་སུ་བྱ་བ་དང་། གཙུག་ལག་ཁང་གི་སྡོམ་པ་དང་། དགེ་ཚུལ་གྱི་སྡོམ་པ་དང་། སྨྱོས་པའི་སྡོམ་པ་དང་། ཕྱག་མི་བྱ་བའི་སྡོམ་པ་དང་། མི་སྨྲ་བའི་སྡོམ་པ་དང་། ལོངས་མི་སྤྱོད་པའི་སྡོམ་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2057]
ཅི་སྟེ་ཅིའི་ཕྱིར་ལྷུང་བཟེད་ཁ་སྦུབ་པ་ལ་སོགས་པ་ནས་དགེ་ཚུལ་གྱི་སྡོམ་པའི་བར་གྱི་སྡོམ་པ་ལྔ་པོ་རྣམས་འདིར་ཅིའི་ཕྱིར་འདིར་མ་བསྡུས་ཤེ་ན། དེ་རྣམས་ནི་བསྙེན་པར་མ་རྫོགས་པའི་ཡུལ་ཡིན་པས་དེ་དག་ལ་མངོན་སུམ་དུ་གྱུར་པའི་དོགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2058 [VERSE]]
དེ་ལྟ་བས་ན་མདོ་འདིར་མ་སྨོས་སོ། །
འདི་ན་རང་ལ་ངེས་པ་བྱེད་པ་སྟེ།
གཞན་དག་བསྐྲད་པས་ནི་མ་ཡིན་ནོ། །

[Block 2059]
དེ་བས་ན་དེ་རྣམས་ལ་མངོན་སུམ་དུ་མ་གྱུར་པ་ཉིད་ལ་བྱ་བ་ཉིད་དོ། །

[Block 2060]
འདི་ནི་སྨྲ་བར་མི་བྱ་བ་དང་། དེ་ནི་ལོངས་སྤྱོད་པར་བྱ་བ་མ་ཡིན་པ་དང་། དེའི་གཙུག་ལག་ཁང་དུ་འགྲོ་བ་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་དེ་རྣམས་ལ་གོ་རིམས་ཇི་ལྟ་བ་བཞིན་དུ་མི་སྨྲ་བ་དང་། ལོངས་སྤྱད་པར་མི་བྱ་བ་དང་། གཙུག་ལག་ཁང་གི་སྡོམ་པ་རྣམས་རིག་པར༌[^1832]བྱའོ། །

[Block 2061]
སྨྱོས་པའི་སྡོམ་པ་ནི་སྨྱོས་པ་དང་རྩེ་གཅིག་པ་དང་། སྨྱོས་པ་དང་རྩེ་གཅིག་པ་མ་ཡིན་པའི་གྲུབ་པའི་དོན་དུ་སྦྱིན་པ་ཡིན་ནོ། །

[Block 2062]
ཕྱག་མི་བྱ་བའི་སྡོམ་པ་ནི་དགེ་སློང་བསྙིལ་བ་ལ། དགེ་སློང་མ་རྣམས་ཀྱིས་བྱ་བའོ། །

[Block 2063]
སྡོམ་པ་འདི་རྣམས་ནི་བསྙེན་པར་རྫོགས་པ་མངོན་སུམ་དུ་མ་གྱུར་པ་མ༌[^1833]ཡིན་པ་རྣམས་ལ་བྱེད་པ་ཡིན་གྱི། ལས་གཞན་ཐམས་ཅད་ནི་མངོན་སུམ༌[^1834]དུ་གྱུར་པ་རྣམས་ལའོ། །

[Block 2064]
གསོལ་བ་མ་བྱས་པར་དེའི་དོན་དུ་བརྗོད་པར༌[^1835]མི་བྱའོ་ཞེས་བྱ་བ་ནི་གང་གི་དོན་དུ་ལས་བརྗོད་པ་དེ་མ་ཤེས་པ་ལ༌[^1836]ལས་བརྗོད་པར་མི་བྱའོ། །

[Block 2065]
སྔར་མི་མཐུན་པ་དག་མི་བྱའོ་ཞེས་སྨོས་པ་དེའི་མི༌[^1837]མཐུན་པའི་ངོ་བོ་ཉིད་བསྟན་པའི་ཕྱིར། དེའི་མཚམས་ཀྱི་ཁོངས་སུ་གཏོགས་པའི་ཁ་སྐོང་བར་འོས་པ༌[^1838]ལུས་སམ་དེ་ལ་འདུན་པས་རྗེས་སུ་མ་ཞུགས་པ་ཉིད་དང་། ཕྱིར་ཟློག་པར་བྱེད་པ་ཡང་གང༌[^1839]ལ་ལས་དེ་བྱེད་པ་དེ་ལས་གཞན་པས་གལ་ཏེ་མི་མཐུན་པ་དང་ཆོས་དང་ལྡན་ན་སྤྱོད་ལམ༌[^1840]མ་ཉམས་པ་དང་། རང་བཞིན་དུ་གནས་པ་དང་། ངག་ཡང་དག་པར་བསྡམས་པས་མངོན་པར་མི་ཤེས་པ་དང་། ནད་དང་བཅས་པ་མ་གཏོགས་པས་ནི་མི་མཐུན་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མི་མཐུན་པ་ཉིད་ནི་རྣམ་པ་གཉིས༌[^1841]ཏེ། འདུས་པར་རྗེས་སུ་ཞུགས་པ་ཉིད་དང་། ཕྱིར་ཟློག༌[^1842]པར་བྱེད་པའོ། །

[Block 2066]
གང་དུ་བྱེ་བྲག་གང་དང་ལྷན་ཅིག་པའི་འདུག་པ་ལ་རྗེས་སུ་མ་ཞུགས་པ་ཉིད་ཅེས་བྱ་བ་དེ་དང་པོར་བསྟན་པའི་ཕྱིར། དེའི་མཚམས་ཀྱི་ཁོངས་སུ་གཏོགས་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། མཚམས་གང་དུ་ལས་དེ་བྱེད་པ་དེའི་ཁོངས་སུ་གཏོགས་པའི་དགེ་སློང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2067]
ཁ་སྐོང་བར་འོས་པ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་མ་རྫོགས་པ་དང་། ཉམས་པ་ལ་སོགས་པ་གཞན་ལ༌[^1843]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2068]
འདིར་ལུང་ནི་ཇི་སྲིད་དུ་དགེ་སློང་དག་མཚམས་ཐོབ་པ་དང་བྱ་བ་ཐོབ་པ་ཞེས་བྱ་བའོ། །

[Block 2069]
དེ་བས་ན་བྱ་བ་ཐོབ་པའི་ཚིག་གོ། །

[Block 2070]
གང་གི་ཕྱིར་དེ་ནི་བྱ་བ་ཐོབ་པ་ཉིད་ཡིན་ཏེ། གང་ཞིག་བསྐང༌[^1844]བའི་ཕྱིར་འོས་པ་ཉིད་དོ། །
--- END BLOCKS ---
