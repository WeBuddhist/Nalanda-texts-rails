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
ཐོབ་རྣམ་གཉིས། ཐོབ་པ་རྣམས་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དག་ཡིན་ནོ། །

[Block 1822]
མཚན་ཉིད་རྣམས་ཀྱང་། རྣམ་གཉིས་ཞེས་བྱ་བར་སྦྱར་ཏེ་ཐོབ་པ་བཞིན་ནོ། །

[Block 1823]
སྙོམས་འཇུག་དང་། མི་ལྡན་པ་དག་རྒྱུ་མཐུན་པ། སེམས་མེད་པའི་སྙོམས་པར་འཇུག་པ༌[^891]གཉིས་དང་མི་ལྡན་པ་རྣམས་ནི་རྒྱུ་མཐུན་པ་ལས་བྱུང་བ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 1824]
འདི་དག་གི་བརྗོད་པར་བྱ་བ་ལྷག་མ་དང་། ལྷག་མ་འདུ་ཤེས་མེད་པ་པ་དང་། སྲོག་གི་དབང་པོ་དག་གིས༌[^892]ནི་བཤད་ཟིན་པས་དེའི་ཕྱིར་ཡང་མི་བརྗོད་དོ། །

[Block 1825]
ཇི་ལྟར་ཐོབ་པ་རྣམས་ཀྱི་སེམས་ཅན་དུ་སྟོན་པ་ཉིད་བཤད་ཟིན་ཅེ་ན། ལྡན་པ་ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 1826]
ཇི་ལྟར་མཚན་ཉིད་རྣམས་སེམས་ཅན་དུ་སྟོན་པ་དང་། སེམས་ཅན་དུ་སྟོན་པ་མ་ཡིན་པར་བཤད་ཅེ་ན། འདུས་བྱས་ཐམས་ཅད་དང་ལྷན་ཅིག་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1827]
ལྡན་པ་མ་ཡིན་པ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 1828 [HEADING]]
### རྒྱུ་རྣམས་དང་འབྲས་བུ་རྣམས། ^2-4-0

[Block 1829 [VERSE]]
རྒྱུ་དང་རྐྱེན་དག་མེད་པར་ནི། །
སྐྱེ་བ་བསྐྱེད་བྱ་སྐྱེད་བྱེད་མིན། །

[Block 1830 [HEADING]]
#### རྒྱུ་རྣམས། ^2-4-1-0

[Block 1831]
ཞེས་གང་བཤད་པ།[^893] རྒྱུ་རྣམས་ནི་གང་། རྐྱེན་རྣམས་ནི་གང་ཞེ་ན།

[Block 1832 [HEADING]]
##### རྒྱུ་རྣམ་པ་དྲུག། ^2-4-1-1-0

[Block 1833 [VERSE]]
བྱེད་རྒྱུ་ལྷན་ཅིག་འབྱུང་བ་དང་། །
སྐལ་མཉམ་མཚུངས་པར་ལྡན་པ་དང་། །
ཀུན་ཏུ་འགྲོ་དང་རྣམ་སྨིན་དང་། །
རྒྱུ་ནི་རྣམ་པ་དྲུག་ཏུ་འདོད། །

[Block 1834]
རྒྱུ་ནི་དྲུག་པོ་འདི་དག་སྟེ། །བྱེད་པའི་རྒྱུ་དང་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་དང་། སྐལ་བ་མཉམ་པའི་རྒྱུ་དང་། མཚུངས་པར་ལྡན་པའི་རྒྱུ་དང་། ཀུན་ཏུ་འགྲོ་བའི་རྒྱུ་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུའོ། །

[Block 1835 [HEADING]]
###### བྱེད་པའི་རྒྱུ། ^2-4-1-1-1-0

[Block 1836]
དེ་ལ་རང་ལས་གཞན་པ་བྱེད་རྒྱུའི་རྒྱུ། །རང་གི་ངོ་བོ་མ་གཏོགས་པ་ཆོས་ཐམས་ཅད་ནི་ཆོས་འདུས་བྱས་ཀྱི་བྱེད་རྒྱུའི་རྒྱུ་ཡིན་ཏེ། སྐྱེ་བ་ལ་བགེགས༌[^894]མི་བྱེད་པའི་ངོ་བོར་གནས་པའི་ཕྱིར་རོ། །

[Block 1837]
ཟག་པ་གང་དག་མི་ཤེས་པ་དེ་ལ་སྐྱེ་བ་དེ་དག་ཤེས་པ་དེ་ལ་མི་སྐྱེའོ་ཞེས་གསུངས་པས་དེ་དག་སྐྱེ་བ་ལ་ཡང་ཤེས་པ་གེགས་བྱེད་ལ། སྐར་མ་རྣམས་མཐོང་བ་ལ་ཡང་ཉི་མའི་འོད་བགེགས་བྱེད༌[^895]པ་མ་ཡིན་ན༌[^896]ནམ། ཇི་ལྟར་ན་རང་གི་ངོ་བོ་མ་གཏོགས་པ་ཆོས་ཐམས་ཅད་ཆོས་འདུས་བྱས་ཀྱི་བྱེད་རྒྱུ་ཡིན་ཞེ་ན། སྐྱེ་བ་ལ་བགེགས་མི༌[^897]བྱེད་པའི་ངོ་བོར༌[^898]གནས་པའི་ཕྱིར་ཤེས་པར་བྱའོ། །

[Block 1838]
རེ་ཞིག་སྐྱེ་བ་ལ་བགེགས་བྱེད༌[^899]ནུས་པ་རྣམས་ནི་བགེགས༌[^900]མི་བྱེད་པའི་ཕྱིར་རྒྱུ་ཉིད་དུ་ཡང་འགྱུར་ཏེ། དཔེར་ན་སྤྱོད་པར་བྱེད་པའི༌[^901]མི་འཚེ་བའི་དབང་དུ་བྱས་ནས༌[^902]གྲོང་མི་རྣམས་བདག་ཅག་ནི་རྗེ་བོས་བདེ་བར་བྱས་སོ་ཞེས་འཛེར་བ་ལྟ་བུ་ཡིན་ན།[^903] གང་ཞིག་བགེགས༌[^904]བྱེད་པར་མི་ནུས་པ་དཔེར་ན་ཆོས་ཐམས་ཅད་སྐྱེ་བ་ལ་མྱ་ངན་ལས་འདས་པ་དང་། མི་སྐྱེ་བའི་ཆོས་ཅན་རྣམས་ལྟ་བུ་དང་། གཟུགས་མེད་པའི་སེམས་ཅན་གྱི་ཕུང་པོ་སྐྱེ་བ་ལ་དམྱལ་བ༌[^905]ལ་སོགས་པ་དག་ལྟ་བུ་དེ་གོ་ཇི་ལྟར་ན་རྒྱུའི་དངོས་པོ་ཡིན། དེ་དག་མེད་དུ་ཟིན་ཀྱང་དེ་ཁོ་ན་བཞིན་དུ་བགེགས༌[^906]བྱེད་མི་ནུས་པར་འགྱུར་ཏེ། སྤྱོད་པར་བྱེད་པར་མི་ནུས་བཞིན་དུ་ཡང་དེ་སྐད་དུ་འཛེར་བ་ཡོད་པས་འདིར་དཔེ་ནི་དེ་ཉིད་ཡིན་ནོ། །

[Block 1839]
འདི་ནི་སྤྱིར་བསྟན་པ་ཡིན་གྱི། བྱེད་རྒྱུའི་རྒྱུ་གཙོ་བོ་གང་ཡིན་པ་འདི་ནི་བསྐྱེད་པར་བྱ་བ་ལ་ཡང་ནུས་པ་ཡོད་དེ༌[^907]དཔེར་ན་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་མིག་དང་གཟུགས་དག་དང་། ལུས་ལ་ཟས་དང་། མྱུ་གུ་ལ་སོགས་པ་ལ་ས་བོན་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 1840]
གང་ཞིག་འདི་སྐད་དུ་གལ་ཏེ་མི་སྒྲིབ་པའི་ངོ་བོས་ཆོས་ཐམས་ཅད་རྒྱུ་དག་ཡིན་ནོ། །

[Block 1841]
[^908]ཅིའི་ཕྱིར་ཆོས་ཐམས་ཅད་ཅིག་ཅར་སྐྱེ་བར་མི་འགྱུར་རོ། །

[Block 1842]
[^909]སྲོག་གཅོད་པ་ལ་སོགས་པ༌[^910]ལ་ཡང་གཤེད་མ་པ་བཞིན་དུ་ཐམས་ཅད་དེ་བསྟེན་པར༌[^911]མི་འགྱུར་ཞེས་རྒོལ་བར་བྱེད་པ་དེའི་དེ་ནི་ཀླན་ཀར་མི་རུང་སྟེ། འདི་ལྟར་མི་སྒྲིབ་པའི་ངོ་བོས་ཆོས་ཐམས་ཅད་རྒྱུ་ཡིན་པར་དམ་འཆའི། བྱེད་པ་པོའི་ངོ་བོ་ནི་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1843]
གཞན་དག་ན་རེ་ཐམས་ཅད་སྐྱེས་པ༌[^912]ལ་བྱེད་པའི་རྒྱུ་ཐམས་ཅད་ཀྱང་ནུས་པ་ཡོད་དེ། འདི་ལྟ་སྟེ་མྱ་ངན་ལས་འདས་པ་ཡང་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་ནུས་པ་ཡོད་པ་ལྟ་བུའོ་ཞེས་ཟེར་རོ། །ཇི་ལྟ་བུ་ཞེ་ན། དམིགས་པ་དེས་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དགེ་བ་དང་མི་དགེ་བ་སྐྱེ་ལ། དེས་རིམ་གྱིས་ཕྱིས༌[^913]མིག་གི་རྣམ་པར་ཤེས་པ་སྐྱེད་པའི་ཕྱིར་རྒྱུ་རྒྱུད་པའི་སྒོ་ནས་དེ་ཡང་རྐྱེན་དུ་གྱུར་པའི་ཕྱིར་ནུས་པ་ཡོད་དོ། །

[Block 1844]
དེ་བཞིན་དུ་གཞན་ལ༌[^914]ཡང་རྟོགས་པར་བྱ་སྟེ། འདི་ནི་ཕྱོགས་ཙམ་དུ་ཟད་དོ། །

[Block 1845]
བྱེད་པའི༌[^915]རྒྱུ་བཤད་ཟིན་ཏོ། །

[Block 1846 [HEADING]]
###### ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ། ^2-4-1-1-2-0

[Block 1847]
ལྷན་ཅིག་འབྱུང་གང་ཕན་ཚུན་འབྲས། །ཕན་ཚུན་ཞེས་བྱ་བ་ནི་གཅིག་ལ་གཅིག་སྟེ། ཆོས་གང་དག་ཕན་ཚུན་གྱི་འབྲས་བུ་ཡིན་པ་དེ་དག་ནི་ཕན་ཚུན་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུའོ། །

[Block 1848]
དཔེ་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 1849 [VERSE]]
འབྱུང་བཞིན་སེམས་ཀྱི་རྗེས་འཇུག་དང་། །
སེམས་དང་མཚན་ཉིད་མཚན་གཞི༌[^916]བཞིན། །

[Block 1850]
འབྱུང་བ་ཆེན་པོ་བཞི་དག་ནི་ཕན་ཚུན་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཡིན་ནོ། །

[Block 1851]
སེམས་ནི་སེམས་ཀྱི་རྗེས་སུ་འཇུག་པའི་ཆོས་རྣམས་ཀྱི་ཡིན་ལ་དེ་དག་ཀྱང་སེམས་ཀྱི་ཡིན་ནོ། །

[Block 1852]
འདུས་བྱས་ཀྱི་མཚན་ཉིད་རྣམས་ནི་མཚན་གཞིའི་ཡིན་ལ་དེ་ཡང་དེ་དག་གི་ཡིན་ཏེ། དེ་ལྟར་ན༌[^917]འདུས་བྱས་ཐམས་ཅད་ནི་ཅི་རིགས་པར་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཉིད་ཡིན་ནོ། །

[Block 1853]
ཕན་ཚུན་འབྲས་བུ་ཉིད་མེད་བཞིན་དུ་ཆོས་ནི་མཐུན་པའི་མཚན་ཉིད་རྣམས་ཀྱི་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཡིན་ལ་དེ་དག་ནི་དེའི་མ་ཡིན་པས་ཁ་བསྐང་བར་བྱའོ། །

[Block 1854]
སེམས་ཀྱི་རྗེས་སུ་འཇུག་པའི་ཆོས་དེ་དག་ཀྱང་གང་ཞེ་ན།

[Block 1855 [VERSE]]
སེམས་ལས་བྱུང་དང་སྡོམ་གཉིས་དང་། །
སེམས་དང་དེ་དག་གི་མཚན་ཉིད། །
སེམས་ཀྱི་རྗེས་སུ་འཇུག་པ༌[^918]དང་། །

[Block 1856]
སེམས་དང་མཚུངས་པར་ལྡན་པ་ཐམས་ཅད་དང་། བསམ་གཏན་གྱི་སྡོམ་པ་དང་། ཟག་པ་མེད་པའི་སྡོམ་པ་དང་། དེ་དག་དང་སེམས་ཀྱི་སྐྱེ་བ་ལ་སོགས་པ་གང་དག་ཡིན་པའི་ཆོས་དེ་དག་ནི་སེམས་ཀྱི༌[^919]རྗེས་སུ་འཇུག་པ་ཞེས་བྱའོ། །

[Block 1857]
[^920]དེ་དག་ཇི་ལྟར་སེམས་ཀྱི་རྗེས་སུ་འཇུག་ཅེ་ན། མདོར་བསྡུ༌[^921]ན། དུས་དང་ནི། འབྲས་སོགས་དགེ་ལ་སོགས་པས་སོ། །

[Block 1858]
རེ་ཞིག་དུས་ལས་ནི་སེམས་དང་ལྷན་ཅིག་སྐྱེ་བ་དང་གནས་པ་དང་འགག་པ་གཅིག་པ་ཉིད་དང་དུས་གཅིག་ཏུ་གཏོགས་པ་ཉིད་ཀྱིས་སོ། །

[Block 1859]
འབྲས་བུ་ལ་སོགས་པས་ནི་འབྲས་བུ་དང་རྣམ་པར་སྨིན་པ་དང་། རྒྱུ་མཐུན་པ་གཅིག་པ༌[^922]ཉིད་ཀྱིས་ཏེ། གཅིག་ཅེས་བྱ་བའི་སྒྲ་སྔ་མ་ནི༌[^923]ལྷན་ཅིག་པའི་དོན་དུ་རིག་པར་བྱའོ། །

[Block 1860]
དགེ་བ་ལ་སོགས་པས་ནི་དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པའི་སེམས་ལ། [^924]དགེ་བ་དང་མི་དགེ་བ་དང་ལུང་དུ་མ་བསྟན་པ་ཉིད་ཀྱིས་ཏེ། དེ་ལྟར་ན་རྒྱུ་བཅུས་སེམས་ཀྱི་རྗེས་སུ་འཇུག་པ་ཞེས་བྱའོ། །
--- END BLOCKS ---
