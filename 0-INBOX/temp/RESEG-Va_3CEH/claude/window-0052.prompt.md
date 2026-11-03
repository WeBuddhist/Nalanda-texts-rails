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
གནས་ཐ་དད་པ་ཉིད་ནི་འདི་ལྟར་འདི༌[^1068]དག་གིས༌[^1069]གནས་ཐ་དད་པ་སྟེ་ལུས་སོ། །

[Block 1822]
དེས་ན་ལས་ཀྱང་ཐ་དད་དོ། །

[Block 1823 [HEADING]]
#### བྱ་བ་ཐ་དད་པ། ^9-5-3-0

[Block 1824]
བྱ་བ་ཐ་དད་པ༌[^1070]ཞེས་བྱ་བ་ནི་འདི་ལྟར་གཞན་དག་ནི་ཚོང་བྱེད། གཞན་དག་ནི་གར་བྱེད་པ་ལ་སོགས་པའི་ལས་ཐ་དད་པ་དང་རབ་ཏུ་ལྡན་པ་སྟེ། དེའི་ཕྱིར་བྱ་བ་ཐ་དད་པས་ཀྱང་འཇིག་རྟེན་པ་རྣམས་ཀྱི་ལས་ཐ་དད་པ་ཡིན་ནོ། །

[Block 1825 [HEADING]]
#### བསམ་པ་ཐ་དད་པ། ^9-5-4-0

[Block 1826]
བསམ་པ་ཐ་དད་པ་ཞེས་བྱ་བ་ལ། བསམ་པ་ནི་འདིར་མོས་པ་སྟེ། དེ་ལྟ་བས་ན་བསམ་པ་ཐ་དད་པའི་ཕྱིར་ཡང་འཇིག་རྟེན་པ་རྣམས་ཀྱི་ལས་ཐ་དད་དོ། །

[Block 1827 [HEADING]]
#### འདུ་བྱེད་ཐ་དད་པ། ^9-5-5-0

[Block 1828]
འདུ་བྱེད་རྣམས་ཀྱང་འདི་ལྟར་ཐ་དད་པ་ཉིད་དུ་འཇུག་པ་སྟེ། གང་འདུ་བྱེད་པ་རྣམས་ཀྱི་བྱ་བ་ཐ་དད་པ་གང་ཡིན་པ་དེ་ཡིན་ནོ། །

[Block 1829]
གང་དག༌[^1071]གི་ཞེ་ན། འཇིག་རྟེན་པ་རྣམས་ཀྱིའོ། །

[Block 1830]
སངས་རྒྱས་རྣམས་ཀྱི་ནི་ལྷུན་གྱིས་གྲུབ་པར༌[^1072]མཛད་པའི་བྱ་བ་ཡིན་པས་དེ་དག་ཐམས་ཅད་མེད་པའི་ཕྱིར་སངས་རྒྱས་རྣམས་ཀྱི་རྒྱུ་ལ་སོགས་པ་ཐ་དད་པ་མེད་པས་དེའི་ཕྱིར་དེ་དག་རྣམས་ཀྱི་ཕྲིན་ལས་ཀྱི་མཛད་པ་ལ་ཐ་དད་པ་མེད་དོ། །

[Block 1831 [HEADING]]
### ཐེག་པ་གཅིག་ཉིད་དུ་བསྟན་པ་དགོངས་པ་ཅན། ^9-6-0

[Block 1832 [HEADING]]
#### དྲང་ཕྱིར། ^9-6-1-0

[Block 1833]
ཐེག་པ་གཅིག་ཉིད་དུ་བསྟན་པ་དགོངས་པ་ཅན་དུ་གསུངས་པ་ཡིན་པར་སྟོན་པའི་ཚིགས་སུ་བཅད་པ་ནི། ཁ་ཅིག་དག་ནི་དྲང་ཕྱིར་དང་། །ཞེས་བྱ་བ་ལ། ཉན་ཐོས་རིགས་མ་ངེས་པ་རྣམས་ཐེག་པ་ཆེན་པོར་དྲང་བར་བྱ་བའི་ཆེད་དུ་སྟེ། མ་ངེས་པ་དེ་ཅི་ནས་ཀྱང་ཐེག་པ་ཆེན་པོར་མྱ་ངན་ལས་འདའ་བར་བྱའོ་ཞེས་བྱའོ། །

[Block 1834 [HEADING]]
#### ཀུན་ཏུ་གཟུང་བའི་ཕྱིར། ^9-6-2-0

[Block 1835]
གཞན་ཡང་ཀུན་ཏུ་གཟུང་བའི་ཕྱིར། །ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའ༌[^1073]རིགས་མ་ངེས་པ་གང་ཡིན་པ་དེ་དག་ཅི་ནས་ཐེག་པ་ཆེན་པོ་ལ་ཐུན་མོང་དུ་འགྱུར་བ་དང་། ཐེག་པ་ཆེན་པོ་བོར་ནས་ཉན་ཐོས་ཀྱི་ཐེག་པས་མྱ་ངན་ལས་འདའ་བར་མ་གྱུར་ཅིག་ཅེས་བྱ་བས་སོ། །

[Block 1836]
དོན་དེ་དག་གི་ཕྱིར་ཐེག་པ་གཅིག་ཉིད་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 1837]
ཡང་མ་ངེས་པ་རྣམས་ཀྱི་དོན་ནི་གོ་སླའོ། །

[Block 1838 [HEADING]]
#### ཆོས་དང་བདག་མེད་གྲོལ་བ་མཐུན་པ། ^9-6-3-0

[Block 1839]
ཆོས་དང་བདག་མེད་གྲོལ་མཐུན་ཕྱིར། །ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱས་པར་འབྱུང་བ་ལ། འདིར་ཡང་དགོངས་པའི་དབང་གིས་ཐེག་པ་གཅིག་ཉིད་དུ་གཅིག་པར་བསྟན་ཏོ། །

[Block 1840]
ཡང་འདིའི་དགོངས་པ་གང་ཡིན་ཞེ་ན། ཆོས་མཐུན་པའི་ཕྱིར་དང་། བདག་མེད་པ་མཐུན་པའི་ཕྱིར་དང་གྲོལ་བ་མཐུན་པའི༌[^1074]ཕྱིར་རོ། །

[Block 1841 [HEADING]]
##### ཆོས་མཐུན་པ། ^9-6-3-1-0

[Block 1842]
དེ་ལ་ཆོས་མཐུན་པ་ཉིད་ནི་རེ་ཞིག་འདིར་ཆོས་ནི་དེ་བཞིན་ཉིད་དོ། །

[Block 1843]
དེ་ནི་མཐུན་པ་ཉིད་དེ། ཉན་ཐོས་ལ་སོགས་པ་ཐམས་ཅད་འདིར་འགྲོ་བར་བྱ་བ་ཡིན་པས་ན་ཐེག་པ་ཆེན་པོ༌[^1075]ཞེས་བྱས་ནས༌[^1076]སོ། །

[Block 1844]
དེ་མཐུན་པ་ཉིད་ཡིན་པའི་ཕྱིར་ཐེག་པ་གཅིག་ཉིད་དོ། །

[Block 1845 [HEADING]]
##### བདག་མེད་པ་མཐུན་པ། ^9-6-3-2-0

[Block 1846]
བདག་མེད་པ་མཐུན་པ་ཉིད་ནི་བདག་དང་གང་ཟག་མེད་པས་དེའི་ཕྱིར་མེད་པ་འདི་ལ་འདི༌[^1077]ནི་ཉན་ཐོས་སོ། །

[Block 1847]
འདི་ནི་བྱང་ཆུབ་སེམས་དཔའོ་ཞེས་བརྗོད་པར་མི་རིགས་ཏེ། དེའི་ཕྱིར་ན་ཡང་བདག་མེད་པ་ལ་དགོངས་ནས་ཐེག་པ་གཅིག༌[^1078]ཉིད་དོ། །

[Block 1848 [HEADING]]
##### གྲོལ་བ་མཐུན་པ། ^9-6-3-3-0

[Block 1849]
གྲོལ་བ་མཐུན་པ་ཉིད་ཅེས་བྱ་བ་ནི་ཉན་ཐོས་ལ་སོགས་པ་རྣམས་ཀྱང་ཉོན་མོངས་པ་ལས་གྲོལ་བ་མཐུན་པ་ཉིད་ཡིན་ཏེ། དེའི་ཕྱིར་འདི་ལ་དགོངས་ནས་ཀྱང་ཐེག་པ་གཅིག་ཉིད་དུ་བསྟན་ཏེ། དེའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་རྣམ་པར་གྲོལ་བ་དང་། རྣམ་པར་གྲོལ་བ་ནི༌[^1079]ཐ་དད་དུ་བྱ་བ་མེད་དོ་ཞེས་གསུངས་སོ།། །།

[Block 1850]
བམ་པོ་བརྒྱད་པའོ།[^1080] །

[Block 1851 [HEADING]]
#### རིགས་ཐ་དད་པ། ^9-6-4-0

[Block 1852]
རིགས་ནི་ཐ་དད་ཅེས་བྱ་བ་ནི་གང་ལ་རིགས་ཐ་དད་པ་ཡོད་པ་སྟེ། རིགས་མ་ངེས་པའི་ཉན་ཐོས་དག་སངས་རྒྱས་སུ་འགྱུར་བ་ལ་དགོངས་ནས་ཀྱང་ཐེག་པ་གཅིག་ཉིད་དུ་བསྟན་ཏེ།

[Block 1853 [HEADING]]
#### བསམ་པ་གཉིས་ཐོབ་པ། ^9-6-5-0

[Block 1854 [HEADING]]
##### མཉམ་པ་ཉིད་ཀྱི་བསམ་པ། ^9-6-5-1-0

[Block 1855]
བསམ་གཉིས་རྙེད༌[^1081]ཕྱིར་ཞེས་བྱ་བ་ནི་བསམ་པ་གཉིས་ཐོབ་པའི་ཕྱིར་ཏེ། གཅིག་ནི་མཉམ་པ་ཉིད་ཀྱི་བསམ་པ་སྟེ། གང་གིས་སེམས་ཅན་ཐམས་ཅད་གང་ཡིན་པ་ཉིད་ནི་བདག་ཡིན་ལ། བདག་ཀྱང་དེ་དག་ཉིད་ཡིན་ནོ་ཞེས་དེ་ལྟར་འཛིན་པ་སྟེ། དེ་ལྟར་འཛིན་པས་ཀྱང་དེ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པར་གྱུར་པས་དེ་དག་ཀྱང་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པར་གྱུར་པ་ཡིན་ཏེ། དགོངས་པ་དེའི་ཕྱིར་ཡང་ཐེག་པ་གཅིག་ཉིད་དོ། །

[Block 1856 [HEADING]]
##### མཐུན་པའི་བསམ་པ། ^9-6-5-2-0

[Block 1857]
ཡང་བསམ་པ་གཉིས་པ་ནི་གང་དམ་པའི་ཆོས་པདྨ་དཀར་པོ་ལས་ཉན་ཐོས་ལུང་བསྟན་པ་དེ་དག་གིས་ནི་སངས་རྒྱས་ཀྱིས་ཀྱང་ཆོས་ཉིད་མཉམ་པ་ཉིད་ལ་དགོངས་ནས། ཆོས་ཀྱི་སྐུ་ཐོབ་པ་ཉིད༌[^1082]ཡིན་ནོ་ཞེས་བསམས་ནས་མཉམ་པ་ཉིད་ལ་དགོངས་པ་དང་། མཐུན་པའི་བསམ་པ་ཐོབ་པ་ནི་སངས་རྒྱས་ཀྱི་ཆོས་ཉིད་ཡང་དག་པར་ཐོབ་པ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 1858 [HEADING]]
#### སྤྲུལ་པའི་ཕྱིར། ^9-6-6-0

[Block 1859]
དོན་གཞན་ཡང་དེ་ལྟ་བུའི་མིང་ཅན་གྱི་བྱང་ཆུབ་སེམས་དཔའི་འཁོར་དེ་ལུང་བསྟན་པ་ཡིན་པས་སྤྲུལ་པའི་ཕྱིར་ཡང༌[^1083]ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟར་ངས་མངོན་པར་ཤེས་ཏེ། ང་ཉིད་ལན་བརྒྱ་སྟོང་དུ་མར་ཉན་ཐོས་ཀྱི་ཐེག་པར་མྱ་ངན་ལས་འདས་པར་གྱུར་ཏོ་ཞེས་པ་དེ༌[^1084]ལྟ་བུ་ལ་དགོངས་ནས་ཐེག་པ་གཅིག་ཉིད་དུ་བསྟན་ཏེ། གང་ཉན་ཐོས་ཀྱི་ཐེག་པས་གདུལ་བའི་སེམས་ཅན་རྣམས་མྱ་ངན་ལས་བཟླ་བའི་ཕྱིར་བསྟན་པ་ཡིན་ནོ། །

[Block 1860 [HEADING]]
#### མཐར་ཕྱིན་པ། ^9-6-7-0
--- END BLOCKS ---
