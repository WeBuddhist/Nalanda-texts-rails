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
[Block 2101]
སྐྱེ་རྒ༌[^1753]ན་འཆི་བ༌[^1754]ལ་སོགས་པ་ནི་ཐུགས་རྗེ་སྐྱེ་བའི་དངོས་པོའོ། །

[Block 2102]
དེ་འདྲ་བའི་སྡུག་བསྔལ་སྣ་ཚོགས་པ༌[^1755]ལ་སེམས་ཅན་འདི་དག་གནས་སོ་ཞེས་བཅོམ་ལྡན་འདས་ཐུགས་རྗེ་སྐྱེ་བའོ། །

[Block 2103]
དེ་ཡང་སྔར་ནི་འདོད་པའི་ཁམས་ཀྱི་སྡུག་བསྔལ་བདུན་བསྟན། སྡུག་བསྔལ་རྣམ་པ་མང་པོ་ཞེས་པ་ནི་གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་ཀྱི་སྡུག་བསྔལ་བསྟན་ཏོ། །

[Block 2104]
འདོད་པའི་ཁམས་ཀྱི་སྡུག་བསྔལ་ཡང་འདུ་བྱེད་ཀྱི་མཚན་ཉིད་བཞིས་འཇོམས་པ་དང་། འདོད་པ་རྣམ་ལྔས་བསྲེགས་པ༌[^1756]དང་རྒྱུད་རྣམས་སུ་འཁོར་བའོ། །

[Block 2105]
དེ་ཡང་སྔ་མ་གསུམ་ནི་ཚེ་འདིའི་སྡུག་བསྔལ་ལོ། །

[Block 2106]
གཅིག་ནི་ཚེ་ཕྱི་མའི་སྡུག་བསྔལ་ལོ།[^1757] །ཡང་ན་སྔ་མ་གཉིས་ནི་འདོད་པ་མི་རྙེད་པའི་སྡུག་བསྔལ་ལོ། །

[Block 2107]
འཁོར་བར་འཁོར་བ་ནི་སྡུག་པ་དང་བྲལ་བ་དང་མི་སྡུག་པ་དང་ཕྲད་པའི་སྡུག་བསྔལ་ལོ། །

[Block 2108]
རྣམ་པ་སྣ་ཚོགས་ཞེས་པ་ནི་ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་རྣམས་ལ་སྡུག་བསྔལ་བར་གྱུར་པའམ། སྡུག་བསྔལ་བརྒྱད་ལ་སོགས་པ་རྣམས་བསྡུའོ། །

[Block 2109]
དབང་པོ་ལྔ་དང་མངོན་པར་འགྱུར་བ༌[^1758]ནི་སྡུག་བསྔལ་བའོ། །

[Block 2110]
ཡིད་ཀྱི་དབང་པོ་དང་ཕྲད་པ་ནི་འཁྲུག་པ་ལ་སོགས་པའོ། །

[Block 2111]
མདོ་ལས་ད་ལྟར་གྱི་ཚེ་ལ་ཚོལ་བའི་ཕྱིར་ཡོངས་སུ་བསགས་པའི་ཕྱིར་ཞེས་པ་ནས་སྡུག་པ་དང་བྲལ་བའི་སྡུག་བསྔལ་རབ་ཏུ་མྱོང་བ་ཞེས་པའི་བར་དུ་ནི་འདོད་པས་གདུངས་པ་དང་། འཁོར་བར་འཁོར་བ་བསྟན་ཏེ། མ་རྙེད་པ་ཚོལ་བ༌[^1759]དང་། རྙེད་པ་ཡོངས་སུ་སོག༌[^1760]པའི་ཕྱིར་སྡུག་བསྔལ་སྐྱེའོ། །

[Block 2112]
དབུལ་ཕོངས་པའི༌[^1761]སྡུག་བསྔལ་ནི་མི་དང༌[^1762]སྦྱར་རོ། །

[Block 2113]
མི་སྡུག་པ་དང་ཕྲད་པ་དང་སྡུག་པ་དང་བྲལ་བའི་སྡུག་བསྔལ་ནི་ལྷ༌[^1763]དང་མི༌[^1764]གཉི་ག་དང་སྦྱར་རོ། །

[Block 2114]
ལྷ་དང་མི་ལ་སྡུག་བསྔལ་དེ་རབ་ཏུ་ཆེ་བའི་ཕྱིར་གཞན་ལས་བཀར༌[^1765]ཏེ་སྨོས་སོ། །

[Block 2115]
མདོ་ལས་དེ་ཉིད་དུ་སྡུག་བསྔལ་གྱི་ཕུང་པོར་འཁོར་ཞིང་ཞེས་པ་ནས་ཡིད་ལ་བྱ་བ་མི་བསྐྱེད་པར༌[^1766]གཟིགས་སོ་ཞེས་པའི་བར་དུ་ནི་སྡུག་བསྔལ་དེ་དག་ལ་གནས་ཀྱང་སྤོང་ཞིང་སྐྱེ་བར་མི་སེམས་ཏེ་རྗེས་སུ་དཔོག༌[^1767]པའི་སྒོ་ནས་རིག་པ་མི་སྐྱེད།[^1768] མངོན་སུམ་གྱི་སྒོ་ནས་ཚོར་བར་མི་བྱེད། འབྲས་བུ་ལ་མི་འཇིག་པ་དང་རྒྱུ་ལ་མི་གྲག༌[^1769]པ་དེ་དག་ཀུན་ལ་སྐྱོ་བ་མི་བསྐྱེད༌[^1770]འབྱུང་བར་མི་སེམས་ཏེ་དེ་ལ་གཞོལ༌[^1771]དེར་རྒྱུགས་ཅེས་པའི་དོན་ཏོ། །

[Block 2116 [HEADING]]
###### **ཐེག་པ་ཆེན་པོ་ལ་རེ་བ་བསྐྱེད་པ།** ^4-3-5-4-1-2-1-1-0

[Block 2117]
མདོ་ལས༌[^1772]ཤཱ་རིའི་བུ་ང་ནི་སེམས་ཅན་འདི་དག་གི་ཕ་སྟེ་ཞེས་པ་ནས་དེ་ལྟར་གཟིགས་སོ་ཞེས་པའི་བར་དུ་ནི་འདི་ཐེག་པ་ཆེན་པོ་ལ་རེ་བ་བསྐྱེད་པ༌[^1773]བསྟན་ཏེ། དེ་ཡང་ཐེག་པ་ཆེན་པོའི་འབྲས་བུ་སེམས་སུ་བཅུག་སྟེ་གདུལ་བ་དང་ཐེག་པ་ཆེན་པོའི་རྒྱུ་བསྟན་ཏེ་གདུལ་བ་དང་ཐེག་པ་ཆེན་པོའི་སྤྱོད་པ་གསང་བ་བསྟན་ཏེ་གདུལ་བ་དང་ཐེག་པ་ཆེན་པོ་མངོན་དུ་ཆུད་པར་བྱ་བ་སྟོན་པ་དང་བཞི་ལ་འདི་ནི་དང་པོ་དང་སྦྱར་རོ། །

[Block 2118]
མདོ་ལས་དེ་ལ་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་སེམས་ཅན་དེ་དག་ཆོས་དེ་དག་གིས་འབྱུང་བར་མི་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེན་པོའི་རྒྱུ་སེམས་སུ་གཞུག༌[^1774]པས་གདུལ་བ་སྟེ། གོང་དུ་ཁང་པ་དེ་ཡང་གཅིག་ལ་ཞེས་འབྱུང་བ༌[^1775]དེ་དང་སྦྱར་ཏེ། སྒོ་དེ་ལས་བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པ་འབའ་ཞིག་གིས་འབྱུང་གི་གཞན་གྱིས་འབྱུང་ནུས་པ་མ་ཡིན་པ་བསྟན་ཏེ། སྟོབས་དང་རྫུ་འཕྲུལ་ལ༌[^1776]སོགས་པ་རྒྱ་ཆེན་པོ་བསྟན་པས་ཐེག་པ་རྣམ་གཉིས་སྣོད་ཆུང་ངུ་ཅན་སྤྱོད་པ་ཞན་པ་འདོར༌[^1777]ཞིང་ཐེག་པ་ཆེན་པོ་ལ་ཞུགས་པས་འདོད་ཁམས་གསུམ་ལ་འབྱུང་གི་གཞན་གྱི་ཐབས་དང་སྤྱོད་པ་ལ་གནས་པས་འབྱུང་བར་མི་ནུས་པ༌[^1778]ཞེས་པའི་དོན་ཏོ། །

[Block 2119]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེ་ན་སེམས་ཅན་འདི་དག་ནི་ཞེས་པ་ནས་དེ་བཞིན་གཤེགས་པ་དེ་ལྟར་གཟིགས་སོ་ཞེས་པའི་བར་དུ་ནི་རེ་བ་མེད་པར་ཆེན་པོ་ཐོབ་པ་བསྟན་ཏེ། དེ་བཞིན་གཤེགས་པའི་ཡེ་ཤེས་ཟབ་མོ་དེ་བསྟན་པར༌[^1779]མི་ནུས་པའི་ཕྱིར་རེ་བ་མེད་ཅེས་པའི་དོན་ཏོ། །

[Block 2120]
མདོ་ལས་དེ་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་ཐེག་པ་གསུམ་མངོན་པར་སྟོན༌[^1780]པའི་བར་དུ་ནི་ཇི་ལྟར་འབྱུང༌[^1781]བའི་ཐབས་སྦྱོར་བ་བསྟན་པ་དང་སྦྱར་ཏེ། སྟོབས་ལ་སོགས་པ་རྫུ་འཕྲུལ་གྱི་རྣམ་གཞག་སྟེ་གསུང་གི་ཐབས་མཁས་པས་སེམས་ཅན་རྣམས་མེ་འབར་བའི་ཁང་པ་ལས་ཐར་བར་བྱས་ནས་གདོད་ཐེག་པ་ཆེན་པོ་སྟོན་ཞེས་པའོ། །

[Block 2121]
བཅོམ་ལྡན་འདས་ཇི་ལྟར་སྨན་པ་མཁས་པ་ནད་ཐབས་དང་སྦྱོར་ཞིང་སྨན་གཏོང་བ་བཞིན་སེམས༌[^1782]ཅན་གྱི་དབང་པོ་དང་སྦྱོར་ཞིང་ཆོས་སྟོན་ཞེས་པའོ། །

[Block 2122 [HEADING]]
###### **ཐེག་པ་རྣམ་གསུམ་དངོས་སུ་བསྟན་པ།** ^4-3-5-4-1-2-1-2-0

[Block 2123 [HEADING]]
###### **ཁམས་གསུམ་ལ་སྐྱོ་བ་བསྐྱེད་པ།** ^4-3-5-4-1-2-1-2-1-0

[Block 2124]
མདོ་ལས་ཁྱེད་ཅག་འབར་བའི་ཁྱིམ་དང་འདྲ་བའི་ཞེས་པ༌[^1783]ནས། ཁམས༌[^1784]འདི་ནས་བྱུང་ལ་ཞེས་པའི་བར་དུ་འདི་ནི་ཐེག་པ་རྣམ་གསུམ་དངོས་སུ་བསྟན་པ་སྟེ། དེ་ཡང་ཁམས་གསུམ་ལ་སྐྱོ་བ་བསྐྱེད་པ༌[^1785]དང་། ཐེག་པ་རྣམ་པ༌[^1786]གསུམ་ལ་གཟུད་པ་དང་། མངོན་དུ་ཆུད་པ་རྣམས་ཀྱི་དཔེ་དང་། ཐེག་པ་ཆེན་པོའི་བསྔགས་པ་དང་བཞི་ཞིག་སྟོན་པ༌[^1787]ལ་འདི་ནི་དང་པོ་དང་སྦྱར་རོ། །

[Block 2125]
འདོད་པ་ལྔ་ནི་ཕྱིའི་ཡུལ་ལོ། །

[Block 2126]
གདུང་བ་ཞེས་པ་ནི་ནང་གི་དམིགས་པ་སྟེ། དེ་གཉིས་སྤོང་བ་ལ་ཁམས་གསུམ་ནས་འབྱུང་བའི་ལམ་ཚོལ་ཅིག་པའོ། །

[Block 2127 [HEADING]]
###### **ཐེག་པ་རྣམ་གསུམ་ལ་གཟུད་པ།** ^4-3-5-4-1-2-1-2-2-0

[Block 2128]
མདོ་ལས་ཉན་ཐོས་ཀྱི་ཐེག་པ་དང་ཞེས་པ་ནས་ཐོབ་པར་གྱིས་ཤིག་ཅེས་པའི་བར་དུ་ནི་ཐེག་པ་རྣམ་གསུམ་ཐོབ་པ་སྩོལ༌[^1788]དུ་གཞུག༌[^1789]པའོ། །

[Block 2129 [HEADING]]
###### **མངོན་དུ་ཆུད་པ་རྣམས་ཀྱི་དཔེ།** ^4-3-5-4-1-2-1-2-3-0

[Block 2130]
མདོ་ལས་ང་ནི་གནས་འདི་ལ་ཁྱེད་ཀྱི་སྙིང་རྗེ་བ༌[^1790]སྟེ་ཞེས་པ་ནས་བརྩོན་འགྲུས་གྱིས་ཤིག་ཅེས་པའི་བར་དུ་ནི། འཕགས་པ་རྣམས་ཀྱིས༌[^1791]མངོན་དུ་ཆུད་པའི་དཔེ་བསྟན་ཏེ། ཐེག་པ་རྣམ་གསུམ་གྱི་དོན་འཕགས་པ་རྣམས་ཀྱིས་མངོན་དུ་གཟིགས་པའི་ཕྱིར་བསླུ་བ་མ་ཡིན་ནོ་ཞེས་སྟོན་པའོ། །

[Block 2131 [HEADING]]
###### **ཐེག་པ་ཆེན་པོའི་བསྔགས་པ།** ^4-3-5-4-1-2-1-2-4-0

[Block 2132]
མདོ་ལས་ཀྱེ་མ༌[^1792]སེམས་ཅན་དག་ཞེས༌[^1793]པ་ནས། ཀུན་ཏུ་རྒྱུག་པར་འགྱུར་གྱིས་ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་ཆེན་པོའི་ཡོན་ཏན་བསྔགས་པ་སྟེ། སྔར་ནི་འཁོར་བ་དང་མི་མཐུན་པ་བསྟན། དེའི་འོག་ཏུ་ནི་ཐེག་པ་གཞན་ལས་ཁྱད་པར་དུ་གྱུར་པ་ལས་བསྔགས་པ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 2133]
འཇིག་རྟེན་གྱི་འཁོར་བ་ནི་ཉོན་མོངས་པས་བཅིངས་པ་རང་དབང་མེད་པ་ཡིན་ན། འཕགས་པ་རྣམས་ཀྱིས་གཟིགས་ཤིང་བརྙེས་པའི་ཐེག་པ་ནི་ཟག་པ་མེད༌[^1794]པས་དགའ་བ་ཆེན་པོ་དང་ལྡན་པའོ། །

[Block 2134]
མི་ཕོངས་པར༌[^1795]རྩེན༌[^1796]ཞེས༌[^1797]གཞན་ལ་རག་ལུས་པ༌[^1798]མེད་པའི་ཕྱིར་རོ། །

[Block 2135]
མི་ཕོངས་པ༌[^1799]ནི་མི་ཚོལ་བའི་དོན་ཏེ་ཚོལ་བ་རྣམ་གསུམ་སྤངས་པའོ། །

[Block 2136]
ཚོལ་བ་རྣམ་གསུམ་ནི་འདོད་པའི་ཚོལ་བ་དང་། སྲིད་པའི་ཚོལ་བ་དང་། [^1800]ལོག་པའི་སྤྱོད་པས་ཚོལ་བའོ། །

[Block 2137]
མདོ་ལས་དབང་པོ་དང་སྟོབས་དང་། བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་ཞེས་པ་ནས་ཡིད་བདེ་བ་ཆེན་པོ་དང་ལྡན་པར་བྱོས་ཤིག་ཅེས་པའི་བར༌[^1801]ནི་འདིས་ཐེག་པའི་དམིགས་པའི་ཡོན་ཏན་བསྟན་ཏེ་ཐེག་པ་ཆེན་པོ་དེ་སྟོབས་དང་། མི་འཇིགས་པ་དང་བྱང་ཆུབ་ཀྱི་ཡན་ལག་བདུན་དང་། འཕགས་པའི་ལམ་ཡན་ལག༌[^1802]བརྒྱད་དང་། བསམ་གཏན་བཞི་དང་། སྙོམས་པར་འཇུག་པ་དགུ་དང་། རྣམ་པར་ཐར་པ་བརྒྱད་དང་། ཏིང་ངེ་འཛིན་གསུམ་ལ་སོགས་པ་ལ་དམིགས་ཤིང་གནས་པའི་ཕྱིར་བདེ་བ་དང་ཡིད་བདེ་བ་སྐྱེ་ཞེས་པའི་དོན་ཏོ། །

[Block 2138 [HEADING]]
###### **ཐེག་པ་རྣམ་གསུམ་སོ་སོར་གྲོལ་བ་ཐོབ་པ།** ^4-3-5-4-1-2-1-3-0

[Block 2139]
མདོ་ལས་དེ་ལ་ཤཱ་རིའི་བུ་སེམས་ཅན༌[^1803]གང་མཁས་པར་འགྱུར་ཞེས་པ་ནི་བྱིས་པ་ཁ་ཅིག་རི་དགས་ཀྱི་ཤིང་རྟ་འདོད་དེ་འབྱུང་བ་བཞིན་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་དེ་བཞིན་གཤེགས་པའི་གསུང་རབ་ལ་བརྟེན་ཏེ། ཐེག་པ་རྣམ་གསུམ་སོ་སོར་གྲོལ་བ་ཐོབ་པར་སྟོན་པ་ལ། འདི་ཉན་ཐོས་ཀྱི་ཐེག་པ་དང་སྦྱར་ཏེ་དཔེ་དང་དོན་དུ༌[^1804]སྦྱར་བར་དབྱེའོ། །

[Block 2140]
མཁས་པར་གྱུར་པ་ཞེས་པ་ནི་མཐུ་རྣམ་བཞི་སྟོན་ཏེ་མཁས་པ་ནི་རྒྱུ་དང་ལྡན་པའི་མཐུའོ། །
--- END BLOCKS ---
