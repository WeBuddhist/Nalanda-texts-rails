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
[Block 1891]
མཁས་པས་བསྔགས་པས་ན་ལེགས་སྤྱད་དོ། །

[Block 1892]
བྱ་བའི་རང་བཞིན་ཡིན་པས་ན་ལས་སོ། །

[Block 1893]
དེ་ལྟར་ན་རེ་ཞིག་བྱེ་བྲག་མེད་པར་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཡང་དག་པར་བསྟན་ནོ། །

[Block 1894]
ཡང་།

[Block 1895 [VERSE]]
དང་པོའི་རྣམ་རིག་རྣམ༌[^732]རིག་མིན། །
སོ་སོར་ཐར་དང་བྱ་བའི་ལམ། །

[Block 1896]
སྡོམ་པ་ཡང་དག་པར་བླངས་པའི་རྣམ་པར་རིག་བྱེད་དང་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་པོ་དག་ནི་སོ་སོར་ཐར་པ་ཞེས་བྱ་སྟེ། དེས་སྡིག་པ་ལས་སོ་སོར་ཐར་པའི་ཕྱིར་རོ། །

[Block 1897]
དངོས་གཞིའི་ལས་ཀྱི་ལམ་ཞེས་བྱའོ། །

[Block 1898]
སྐད་ཅིག་མ་གཉིས་པ༌[^733]ལ་སོགས་པ་ནི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཁོ་ན་ཡིན་གྱི། སོ་སོར་ཐར་པ་ནི་མ་ཡིན་ནོ། །

[Block 1899]
མཇུག་ཡིན་གྱི་ལས་ཀྱི༌[^734]ལམ་དངོས་གཞི་ནི་མ་ཡིན་ནོ། །

[Block 1900 [HEADING]]
#### སྡོམ་པ་གང་ཞིག་གང་དང་ལྡན་པ། ^4-2-2-0

[Block 1901]
ཡང་སྡོམ་པ་འདི་རྣམས་ལས་གང་ཞིག་གང་དང་ལྡན་ཞེ་ན། སོ་སོར་ཐར་དང་ལྡན་པ་བརྒྱད། །དགེ་སློང་དག་དགེ་སློང་མ་ལ་སོགས་པའོ། །

[Block 1902]
བསམ་གཏན་སྐྱེས་དང་དེ་ལྡན་པ། །བསམ་གཏན་ལས་སམ༌[^735]བསམ་གཏན་གྱིས་བསྐྱེད༌[^736]པས་ན་བསམ་གཏན་སྐྱེས་ཏེ། གང་བསམ་གཏན་དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་པར་བསམ་གཏན་གྱི་སྡོམ་པ་དང་ལྡན་ནོ། །

[Block 1903]
འདིར་ནི་ཉེར་བསྡོགས་ཀྱང་བསམ་གཏན་དུ་བརྗོད་ནས་བསྟན་ཏོ། །

[Block 1904]
ཟག་མེད་འཕགས་པའི་སེམས་ཅན་དང་། །ཟག་པ་མེད་པའི་སྡོམ་པ་ནི་འཕགས་པའི་གང་ཟག་རྣམས་དང༌[^737]ལྡན་ནོ། །

[Block 1905]
སེམས་ཀྱི་རྗེས་སུ་འབྲང་བ་སྔར་བཤད་པ་དེ་ལས།

[Block 1906 [VERSE]]
ཐ་མ་གཉིས་ནི་སེམས༌[^738]རྗེས་འབྲང་། །
བསམ་གཏན་གྱི་སྡོམ་པ་དང་།
ཟག་པ་མེད་པའི་སྡོམ་པའོ། །

[Block 1907]
ཡང་སྨྲས་པ།

[Block 1908 [VERSE]]
བར་ཆད་མེད་ལམ་སྐྱེས་དེ་གཉིས། །
མི་ལྕོགས་མེད་ལ་སྤོང་ཞེས་བྱ། །

[Block 1909]
དེ་དག་ཁོ་ན་བར་ཆད་མེད་པའི་ལམ་དགུ་དག་ཏུ་སྤོང་བའི་སྡོམ་པ་ཞེས་བརྗོད་དོ། །

[Block 1910]
དེ་གཉིས་ཀྱིས་འཆལ་བའི་ཚུལ་ཁྲིམས་དང་། དེ་ཀུན་ནས་སློང་བར་བྱེད་པའི་ཉོན་མོངས་པ་རྣམས་སྤོང་བའི་ཕྱིར་རོ། །

[Block 1911]
འོ་ན་བཅོམ་ལྡན་འདས་ཀྱིས། །ཡིད་ཀྱི་སྡོམ་པ་ལེགས་པ་སྟེ། །ཞེས་གསུངས་པ་དང་། དེ་བཞིན་དུ་མིག་གི་དབང་པོ་སྡོམ་པས་བསྡམས་ཏེ་གནས་སོ་ཞེས་གསུངས་པ། ཡིད་དང་དབང་པོའི་སྡོམ་པ་འདི་གཉིས་ཀྱི་རང་བཞིན་ཅི་ཞེ་ན། འདི་གཉིས་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་ཚུལ་ཁྲིམས་ཀྱི་རང་བཞིན་མ་ཡིན་ཏེ། འོན་ཀྱང་།

[Block 1912 [VERSE]]
ཤེས་བཞིན་དང་ནི་དྲན་དག་གཉིས། །
ཡིད་དང་དབང་པོའི་སྡོམ་པ་ཡིན། །

[Block 1913]
ཡིད་ཀྱི་སྡོམ་པ་ཡང་དྲན་པ་དང་ཤེས་བཞིན་གྱི་རང་བཞིན་ཡིན་ལ། དབང་པོའི་སྡོམ་པ་ཡང་ངོ་། །ཡང་གང་ཞིག་རྣམ་པར་རིག་བྱེད་དང་། རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་། དུས་ཇི་སྲིད་དུ་ལྡན་ཞེ་ན།

[Block 1914 [HEADING]]
#### སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་ལ་གནས་པ། ^4-2-3-0

[Block 1915 [VERSE]]
སོ་སོར་ཐར་གནས་ཇི་སྲིད་དུ། །
མ་བཏང་བར་རྟག་ད་ལྟར་གྱི། །

[Block 1916]
རྣམ་རིག་མི་ལྡན། སོ་སོར་ཐར་པའི་སྡོམ་པ་ལ་གནས་པ་གང་དེ་ནི་ཇི་སྲིད་དུ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་མི་གཏོང་བ་དེ་སྲིད་དུ་ད་ལྟར་གྱི་དང་ལྡན་ནོ། །

[Block 1917]
སྐད་ཅིག་མ་དང་པོ་ཕྱིན་ཆད་འདས་པ་དང་། མ་བཏང་བ༌[^739]ཞེས་སྦྱར་བར་བྱའོ། །

[Block 1918]
སོ་སོར་ཐར་པའི་སྡོམ་པ་ལ་གནས་པ་ཇི་སྐད་བཤད་པ། སྡོམ་མིན་གནས་པའང་དེ་དང་འདྲ། །དེ་ཡང་རྟག་ཏུ་ད་ལྟར་བ་དང་། སྐད་ཅིག་མ་གཅིག་ཕྱིན་ཆད་འདས་པ་ཡང་ལྡན་ནོ། །

[Block 1919 [VERSE]]
བསམ་གཏན་སྡོམ་དང་ལྡན་པ་ནི། །
རྟག་ཏུ་འདས་དང་མ་འོངས་དང་། །

[Block 1920]
སྐད་ཅིག་མ་དང་པོའི་ལ་ཡང་ཚེ་རབས་གཞན་དག་ཏུ་གཏང་བའི་བསམ་གཏན་གྱི་སྡོམ་པ་འདས་པ་འཐོབ་བོ། །

[Block 1921]
འཕགས༌[^740]ནི་དང་པོ༌[^741]འདས་དང་མིན། །འཕགས་པ་ཡང་སྐད་ཅིག་མ་དང་པོ་ལ་མ་འོངས་པའི་གང་ཟག་པ་མེད་པའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་ལྡན་ལ། འདས་པ་དང་མི་ལྡན་ཏེ།

[Block 1922 [VERSE]]
ལམ་དེ་སྔོན་མ་བསྐྱེད༌[^742]པའི་ཕྱིར་རོ། །
མཉམ་གཞག་འཕགས་ལམ་གནས་དེ་གཉིས། །

[Block 1923]
ད་ལྟར་དང་ལྡན། བསམ་གཏན་དང་ཟག་པ་མེད་པའི་སྡོམ་པ་ལ་གནས་པ༌[^743]དེ་དག་ནི་ཇི་སྲིད་མ་ལངས་པ་དེ་སྲིད་དུ་ད་ལྟར་གྱི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་ལྡན་ནོ། །

[Block 1924]
སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་ལ་གནས་པ་དག་བཤད་ཟིན་ཏོ། །

[Block 1925]
བར་གནས་ལ་ཡོད་ན་དང་པོ་བར་གྱི་དང་། གང་སྡོམ་པ་ཡང་མ་ཡིན་སྡོམ་པ་མ་ཡིན་པ་ཡང་མ་ཡིན་པ་དེ་ལ་གདོན་མི་ཟ་བར་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཡོད་པ་མ་ཡིན་གྱི། གང་ལ་ཡོད་པ་དེ་ནི་སྐད་ཅིག་དང་པོ་ལ་ད་ལྟར་བ་དང་ལྡན་ནོ། །

[Block 1926]
སྐད་ཅིག་དང་པོ་ནས། ཕྱིན་ཆད་དུས་ནི་གཉིས་དང་པོ། འདས༌[^744]དང་ད་ལྟར་བ་དང་ཡང་ངོ་། །སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པར་གནས་པ་དག་ཀྱང་གདོན་མི་ཟ་བར་རྟག་ཏུ་དགེ་བ་དང་མི་དགེ་བའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་དང་ལྡན་པ་ཁོ་ན་མ་ཡིན་ཏེ། འོན་ཀྱང་སྡོམ་མིན་གནས་པ་དགེ་བ་དང་།

[Block 1927 [VERSE]]
སྡོམ་ལ་གནས་པ་མི་དགེ་བའི། །
རྣམ་རིག་མི་ལྡན་ཇི་སྲིད་དུ། །
རིག༌[^745]དང་ཉོན་མོངས་ཤུགས་ལྡན་པར། །

[Block 1928]
སྡོམ་པ་མ་ཡིན་པ༌[^746]ལ་གནས་པ་ནི་རབ་ཏུ་དང་བའི་ཤུགས་ཀྱིས་མཆོད་རྟེན་ལ་ཕྱག་འཚལ་བ་ལ་སོགས་པའི་བྱ་བ་བྱེད་པ་ན་དགེ་བའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྐྱེ་ལ། སྡོམ་པ༌[^747]ལ་གནས་པ་ནི་ཉོན་མོངས་པའི་ཤུགས་གང་གིས་གསོད་པ་དང་འཆིང་བ༌[^748]ལ་སོགས་པའི་བྱ་བ་བྱེད་པ་ན་དེ་དག་ཇི་སྲིད་དུ་རྗེས་སུ་འབྲང་བ་དེ་སྲིད་དུ་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་ཡང་ངོ་། །རྣམ་པར་རིག་བྱེད་མ་ཡིན་པའི་སྐབས་བཤད་ཟིན་ཏོ། །

[Block 1929 [VERSE]]
རྣམ་རིག་བྱེད་ནི་ཐམས་ཅད་ལ། །
བྱེད་པ་དག་ལ་ད་ལྟར་ལྡན། །

[Block 1930]
སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་དང་བར་མ་ལ་གནས་པ་ཐམས་ཅད་ཇི་སྲིད་དུ་རྣམ་པར་རིག་བྱེད་བྱེད་པ་དེ་སྲིད་དུ་ད་ལྟར་གྱི་དང་ལྡན་ནོ། །
--- END BLOCKS ---
