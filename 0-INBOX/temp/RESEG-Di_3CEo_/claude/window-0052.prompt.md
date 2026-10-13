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
[Block 1821]
ཡང་གང་ན་ཡོད་པའི་ལུས་དང་ངག་གི་ལས་གང་ན་ཡོད་པའི་འབྱུང་བ་ཆེན་པོ་དག་རྒྱུར་བྱས་པ་ཡིན་ཞེ་ན།

[Block 1822 [VERSE]]
ཟག་བཅས་ལུས་དང་ངག་གི་ལས། །
རང་གི་འབྱུང་བ་དག་རྒྱུར་བྱས། །

[Block 1823]
འདོད་པ་ན་སྤྱོད་པ་ནས་བསམ་གཏན་བཞི་པའི་བར་གྱི་ལུས་དང་ངག་གི་ལས་དེའི་ས་པའི་འབྱུང་བ་དག་ཁོ་ན༌[^695]རྒྱུར་བྱས་པ་ཡིན་ནོ། །

[Block 1824]
ཟག་མེད་གང་དུ་སྐྱེས་པའི་ཡིན། །ས་གང་དུ་སྐྱེས་པ་དེ་སྐྱེད་པར༌[^696]བྱེད་པ་དེའི་ས་པའི་འབྱུང་བ་ཆེན་པོ་དག་རྒྱུར་བྱས་པར༌[^697]རིག་པར་བྱ༌[^698]སྟེ། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་ལས་དེ་ལས་ཀྱང་།

[Block 1825 [VERSE]]
རྣམ་རིག་བྱེད་མིན་མ་ཟིན་དང་། །
རྒྱུ་མཐུན་ལས་བྱུང་སེམས་ཅན་སྟོན། །

[Block 1826]
གཞན་ཡང་། རྒྱུ་མཐུན་ཟིན་པའི་འབྱུང་ལས་སྐྱེས། །རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ནི་རྒྱུ་མཐུན་པ་དང་ཟིན་པའི་འབྱུང་བ༌[^699]ཁོ་ན་དག་རྒྱུར་བྱས་ནས་སྐྱེ་སྟེ། འདི་ནི་མཉམ་པར་གཞག་པ་མ་ཡིན་པའི་ས་པའི་རྣམ་པ་ཡིན་ནོ། །

[Block 1827 [VERSE]]
ཏིང་འཛིན་སྐྱེས་འབྱུང་མ་ཟིན་དང་། །
རྒྱས་བྱུང་ཐ་དད་མིན་ལས་སྐྱེས། །

[Block 1828]
ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པ་རྒྱས་པ་ལས་བྱུང་བ༌[^700]དང་། མ་ཟིན་པའི་འབྱུང་བ་དག་ཁོ་ན་རྒྱུར་བྱས་ནས་སྐྱེའོ། །

[Block 1829]
ཐ༌[^701]དད་པ་དག་ཀྱང་ཡིན་ཏེ། འབྱུང་བ་ཆེན་པོ་དག་རྒྱུར་བྱས་ནས་སྲོག་གཅོད་པ་སྤང་བ༌[^702]སྐྱེ།[^703] དེ་དག་ཁོ་ན་ལས་ཚིག་འཆལ་པ༌[^704]སྤོང་བའི༌[^705]བར་དུ་སྐྱེའོ། །

[Block 1830 [HEADING]]
#### དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ། ^4-1-4-0

[Block 1831]
ཡང་ལས་དེ་རྣམ་པ་གཉིས་དང་། རྣམ་པ་གསུམ་དང་། རྣམ་པ་ལྔར་བཤད་པ་དེ་ལ། རྣམ་རིག་མིན་ལུང་བསྟན་མིན་མེད། །དགེ་བ་དང་མི་དགེ་བ་ཡོད། ཅེས་གསུངས་པར་འགྱུར་རོ། །

[Block 1832]
གཞན་ནི་རྣམ་གསུམ་རྣམ་པར་རིག་བྱེད་དང་། སེམས་པ་ནི་རྣམ་པ༌[^706]གསུམ་མོ། །

[Block 1833]
མི་དགེ་ནི་འདོད་ནའོ། །

[Block 1834]
མི་དགེ་བ་ནི་འདོད་པའི་ཁམས་ཁོ་ན་ནི་ཡོད༌[^707]ཀྱི་གཞན་ན་ནི་མ་ཡིན་ནོ། །

[Block 1835]
དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་ནི་མ་བཀག་པའི་ཕྱིར་ཐམས་ཅད་ན་ཡོད་དོ། །

[Block 1836]
དེ་ལ། གཟུགས་ནའང་རྣམ་རིག་མིན། འང་གི་སྒྲས་ནི་འདོད་པ་ན་ཡང་ཡོད་དོ། །

[Block 1837]
གཟུགས་མེད་པ་དག་ན་ནི་འབྱུང་བ་མེད་པའི་ཕྱིར་མེད་དོ། །

[Block 1838]
རྣམ་རིག་དཔྱོད་དང་བཅས་དག་ན། །འདོད་པའི་ཁམས་དང་།[^708] བསམ་གཏན་དང་པོ་ཁོ་ན་ན་ཡོད་ཀྱི་དེ་མན་ཆད་ན་མེད་དོ། །

[Block 1839]
འདོད་པ་ན་ཡང་བསྒྲིབས་པ༌[^709]མེད། ཅིའི་ཕྱིར་ཚངས་པའི་འཇིག་རྟེན་མན་ཆད་ན་རྣམ་པར་རིག་བྱེད་མེད་ལ། འདོད་པའི་ཁམས་ན་བསྒྲིབས་པ་མེད་ཅེ་ན། གང་ཕྱིར་ཀུན་སློང་མེད།[^710] རྟོག་པ་དང་། དཔྱོད་པ་དང་བཅས་པའི་སེམས་ཀྱིས་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བར་བྱེད་ན། དེ་ཡང་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་དག་ན་མེད་དེ། བསྒོམ་པས་སྤང་བར་བྱ་བས་སྐྱེད་ཀྱི། བསྒྲིབས་ལ་ལུང་དུ་མ་བསྟན་པའི་ཡང་འདོད་པའི་ཁམས་ན་མེད་དོ། །

[Block 1840 [HEADING]]
#### ཞར་ལ་འོངས་པ། ^4-1-5-0

[Block 1841]
ཡང་ཅི་ཀུན་ནས་སློང་བའི་དབང་ཁོ་ན་ལས་ཆོས་རྣམས་ཀྱི་དགེ་བ་ལ་སོགས་པར་རིག་པར་བྱའམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ཏེ། འོན་ཀྱང་རྣམ་པ་བཞི་སྟེ། དོན་དམ་པ་དང་། ངོ་བོ་ཉིད་དང་། མཚུངས་པར་ལྡན་པ་དང་། ཀུན་ནས་སློང་བས་སོ། །

[Block 1842]
དེ་ལས་རེ་ཞིག་ཐར་པ་དམ་པའི་དོན་དུ་དགེ །མྱ་ངན་ལས་འདས་པ་ནི་སྡུག་བསྔལ་ཐམས་ཅད་ཉེ་བར་ཞི་བ་ཡིན་ཏེ། དེ་བས་ན་མཆོག་ཏུ་བདེ་བའི་ཕྱིར་དོན་དམ་པར་དགེ་བ་སྟེ། ནད་མེད་པ་བཞིན་ནོ། །

[Block 1843]
རྩ་བ། ངོ་ཚ་ཁྲེལ་ཡོད་བདག་ཉིད་ཀྱིས། །དགེ་བའི་རྩ་བ་གསུམ་དང་། ངོ་ཚ་ཤེས་པ་དང་། ཁྲེལ་ཡོད་པ་ནི་ངོ་བོ་ཉིད་ཀྱིས་དགེ་བ་དག་སྟེ། གཞན་མཚུངས་པར་ལྡན་པ་དང་ཀུན་ནས་སློང་བ་ལ་མི་ལྟོས་པའི་ཕྱིར་ཏེ། འཕྲོད་པའི་སྨན་བཞིན་ནོ། །

[Block 1844]
དེ་དག་དང་ལྡན་མཚུངས་ལྡན་གྱིས། དགེ་བའི་རྩ་བ་དང་། ངོ་ཚ་ཤེས་པ་དང་། ཁྲེལ་ཡོད་པ་དེ་དག་ཉིད་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་རྣམས་ནི་མཚུངས་པར་ལྡན་པའི་དགེ་བ་དག་ཡིན་ཏེ།

[Block 1845 [VERSE]]
སྨན་དང་སྦྱར་བའི་བཏུང་བ་བཞིན་ནོ། །
བྱ་བ་ལ་སོགས་ཀུན་སློང་བས། །

[Block 1846]
དགེ་བའི་རྩ་བ་ལ་སོགས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་དེ་དག་ཁོ་ནས་ཀུན་ནས་བསླང་བའི་ལུས་དང་ངག་གི་ལས་སེམས་ཀྱིས་མ་ཟིན་པ་དག་ཀུན་ནས་སློང་བས་དགེ་བ་ཡིན་ཏེ། སྨན་དང་སྦྱར་བའི་བཏུང་བ་ལས༌[^711]བྱུང་བའི་འོ་མ༌[^712]བཞིན་ནོ། །

[Block 1847]
དགེ་བ་ཇི་སྐད་དུ་བཤད་པ་དེ་ལས།

[Block 1848]
བཟློག་པ་མི་དགེ །འཁོར༌[^713]བ་ནི་སྡུག་བསྔལ་ཐམས་ཅད་འཇུག་པའི་བདག་ཉིད་ཀྱིས་མཆོག་ཏུ་མི་བདེ་བའི་ཕྱིར་དོན་དམ་པར་མི་དགེ་བ་ཡིན་ནོ། །

[Block 1849]
མི་དགེ་བའི་རྩ་བ་དང་ངོ་ཚ་མེད་པ་དང་ཁྲེལ་མེད་པ་རྣམས་ནི་ངོ་བོ་ཉིད་ཀྱིས་སོ། །

[Block 1850]
དེ་དག་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་རྣམས་ནི་མཚུངས་པར་ལྡན་པས་སོ། །

[Block 1851]
དེ་དག་གིས་ཀུན་ནས་བསླང༌[^714]པའི་ལུས་དང་ངག་གི་ལས་དང་། སྐྱེ་བ་ལ་སོགས་པ་དང་ཐོབ་པ་རྣམས་ནི་ཀུན་ནས་བསླང་བ་ལས་ཏེ། ནད་དང་མི་འཕྲོད་པའི་སྨན་ལ་སོགས་པ་དཔེར་བྱའོ། །

[Block 1852]
དེ་ལྟ་ན་འོ་ན་ནི་འཁོར་བའི་ཁོངས་སུ་གཏོགས་པའི་ཕྱིར་ཟག་པ་དང་བཅས་པ་ཅུང་ཟད་ཀྱང་ལུང་དུ་མ་བསྟན་པའམ། དགེ་བར་མི་འགྱུར་རོ་ཞེ་ན། དོན་དམ་པར་དེ་སྐད་དུ་བཤད་ཀྱི་ཟག་པ་དང་བཅས་པ་གང་ཞིག་རྣམ་པར་སྨིན་པའི་ཕྱིར་ལུང་དུ་མ་བསྟན་པ་དེ་ནི་ལུང་དུ་མ་བསྟན་པ་ཞེས་བྱ་བ༌[^715]ལ། རྣམ་པར་སྨིན་པ་ཡིད་དུ་འོང་བ་ཅན་ནི་དགེ་བ་ཞེས་བྱའོ། །

[Block 1853]
གལ་ཏེ་དོན་དམ་པར་ལུང་དུ༌[^716]མ་བསྟན་པ་ཚོལ་བ༌[^717]ན་ནི་དེ་ལ། དོན་དམ་པར་ལུང་མ་བསྟན་པ་བརྟག་པ་དག །འདུས་མ་བྱས་ནམ་མཁའ་དང་། སོ་སོར་མ༌[^718]བརྟགས་པས་འགོག་པ་ནི་རྣམ༌[^719]གྲངས་མེད་པར་ལུང་དུ་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 1854]
མཐོང་བས་སྤང་བར་བྱ་བའི་སེམས་ནི་རྣམ་པར་རིག་བྱེད་ཀུན་ནས་སློང་བ་མ་ཡིན་ནོ་ཞེས་གང་བཤད་པ། འོ་ན་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ལོག་པར་ལྟ་བ་དེ་ལས་ནི་ལོག་པར་རྟོག་པ་དང་ལོག་པའི་ངག་དང༌[^720]ལོག་པའི་ལས་ཀྱི་མཐའ་འབྱུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཤེ་ན། འདི་ནི་འགལ་བ་མེད་དེ། འདི་ལྟར།

[Block 1855 [VERSE]]
ཀུན་སློང་རྣམ་གཉིས་རྒྱུ་དང་ནི། །
དེ་ཡི་དུས་ཀྱི་སློང་ཞེས་བྱ། །

[Block 1856]
ཀུན་ནས་སློང་བ་ནི་རྣམ་པ་གཉིས་ཏེ། རྒྱུའི་ཀུན་སློང་དང་། དེའི་དུས་ཀྱི་ཀུན་ནས་སློང་བ་སྟེ། དེའི་དུས་ཁོ་ན་ན་དེ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1857 [VERSE]]
གཉིས་ལས་དང་པོ་རབ་འཇུག་བྱེད། །
གཉིས་པ་རྗེས་སུ་འཇུག་བྱེད་ཡིན། །

[Block 1858]
རྒྱུའི་ཀུན་ནས་སློང་བ་ནི་འཕེན་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1859]
དེའི་དུས་ཀྱི་ཀུན་ནས་སློང་བ་ནི་བྱ་བའི་དུས་སུ་མཐུན་པར་འཇུག་པའི་ཕྱིར་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1860]
དེ་ལ་ཡང་། མཐོང་བས་སྤང་བྱའི་རྣམ་ཤེས་ནི། །རབ་ཏུ་འཇུག་བྱེད་ཡིན། མཐོང་བས་སྤང་བར་བྱ་བའི་སེམས་ནི་དེ་ཀུན་ནས་སློང་བར་བྱེད་པ་དཔྱོད་པ་དང་རྟོག་པ་དག་གི་གཞིར་གྱུར་པའི་ཕྱིར་རྣམ་པར་རིག་བྱེད་རབ་ཏུ་འཇུག་པར་བྱེད་པ་ཡིན་གྱི་སེམས་ཁ་ཕྱིར་བལྟས་པའི་ཕྱིར་རྗེས་སུ་འཇུག་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
