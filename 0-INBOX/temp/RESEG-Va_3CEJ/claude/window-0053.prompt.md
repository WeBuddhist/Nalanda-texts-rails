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

[Block 1861]
དེ་ལ་སེམས་ནང་ན་ཉུང་བ་ནི་ཆོས་ལྔ་བཅུ་རྩ་བརྒྱད་ཀྱི་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཡིན་ཏེ། ས་མང་པོ་པ་བཅུ་དང་། དེ་དག་གི་མཚན་ཉིད་བཞི་བཅུ་དང་། རང་གི་མཚན་ཉིད་དང༌[^925]མཐུན་པའི་མཚན་ཉིད་བརྒྱད་ཀྱི་ཡིན་ནོ།[^926] །དེའི་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ནི་ཆོས་ལྔ་བཅུ་རྩ་བཞི་སྟེ། རང་གི་མཐུན་པའི་མཚན་ཉིད་མ་གཏོགས་པ་རྣམས་སོ། །

[Block 1862]
གཞན་དག་ན་རེ་བཅུ་བཞི་ཡིན་ཏེ། ས་མང་པོ་པ༌[^927]བཅུ་དང་། རང་གི་མཚན་ཉིད་དག་ཁོ་ནའོ་ཞེས་ཟེར་རོ། །

[Block 1863]
དེ་སྐད་དུ་ནི་མི་བརྗོད་དེ། །དེ་ལྟར་ན་རབ་ཏུ་བྱེད་པའི་གཞུང་། སྡུག་བསྔལ་གྱི་བདེན་པ་ལ་འཇིག་ཚོགས་ལ་ལྟ་བའི་རྒྱུ་ཅན་ཡིན་ལ་འཇིག་ཚོགས་ལ་ལྟ་བའི་རྒྱུ་མ་ཡིན་པ་ཡང་ཡོད་དེ། འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། དེ་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་རྣམས་ཀྱི་སྐྱེ་བ་དང་རྒ་བ་དང་གནས་པ་དང་མི་རྟག་པ་དག་མ་གཏོགས་པ་དེ་དག་ལས་གཞན་པའི་སྡུག་བསྔལ་གྱི་བདེན་པ་ཉོན་མོངས་པ་ཅན་གང་ཡིན་པའོ། །

[Block 1864]
འཇིག་ཚོགས་ལ་ལྟ་བའི་རྒྱུ་ཅན་ཡང་ཡིན་ལ་འཇིག་ཚོགས་ལ་ལྟ་བའི་རྒྱུ་ཡང་ཡིན་པ༌[^928]ནི་མ་གཏོགས་པ་གང་ཡིན་པའོ་ཞེས་འབྱུང་བ་དང་འགལ་བར་འགྱུར་རོ། །

[Block 1865]
ཁ་ཆེ་བ་རྣམས་ན་རེ་འོ་ན་ནི་གང་དག་དེ་དང་མཚུངས་པར་ལྡན་པའི་ཆོས་རྣམས་ཀྱི་ཞེས་དེ་སྐད་དུ་མི་འདོན་པ་དེ་དག་གིས་ཀྱང་དེ་སྐད་དུ་གདོན་པར༌[^929]བྱ་བ་འམ། ཡང་ན་དོན་གྱིས་དེ་ལྟར་གོ་བར་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 1866]
རེ་ཞིག་གང་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུས་རྒྱུ་ཡིན་པ་དེས་ནི་ལྷན་ཅིག་འབྱུང་བ་ཡང་ཡིན་ནོ། །

[Block 1867]
ལྷན་ཅིག་འབྱུང་བ་ཡིན་ལ་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུས་རྒྱུ་མ་ཡིན་པ་ཡང་ཡོད་དེ། ཆོས་ཀྱི་མཐུན་པའི་མཚན་ཉིད་རྣམས་དང་། དེ་དག་ཕན་ཚུན་དང་། སེམས་ཀྱི་རྗེས་སུ་འཇུག་པའི་མཐུན་པའི་མཚན་ཉིད་རྣམས་ཉིད་དང་། དེ་དག་ཕན་ཚུན་དང་། རྒྱུར་བྱས་པའི་གཟུགས་ཐོགས་པ་དང་བཅས་པ་ཕན་ཚུན་དང་། ཐོགས་པ་མེད་པ་ཅུང་ཟད་དང་། ཐམས་ཅད་འབྱུང་བ་དག་དང་ལྟ་བུའོ། །

[Block 1868]
ཐོབ་པ་དང་ལྡན་པའི་ཐོབ་པ་ལྷན་ཅིག་སྐྱེས་པ་རྣམས་ཀྱང་ལྷན་ཅིག་འབྱུང་བ་ཡིན་ལ་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ནི་མ་ཡིན་ཏེ། འབྲས་བུ་དང་རྣམ་པར་སྨིན་པ་དང་རྒྱུ་མཐུན་པ་གཅིག་པ༌[^930]མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1869]
དེ་དག་ནི་སེམས་དང་ལྷན་ཅིག་སྤྱོད་པའི་ངང་ཚུལ་ཅན་ཡང་མ་ཡིན་ཏེ་སྔར་ཡང་སྐྱེ་ལ་ཕྱིས་ཀྱང་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1870]
དེ་ཐམས་ཅད་ཀྱང་རུང་མོད་ཀྱི་འོན་ཀྱང་ས་བོན་ལ་སོགས་པ་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོར་གྲགས་པ་རྣམས་ལ་ཚུལ་འདི་མི་སྣང་བས་ཇི་ལྟར་ལྷན་ཅིག་འབྱུང་བའི་ཆོས་རྣམས་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོ་ཡིན་པ་དེ་བརྗོད་པར་བྱའོ། །

[Block 1871]
དཔེར་ན་མར་མེ་དང་འོད་དག་དང་མྱུ་གུ་དང་གྲིབ་མ་དག་ལྟ་བུ་ཡིན་ནོ། །

[Block 1872]
རེ་ཞིག་ཅི་མར་མེ་འོད་ཀྱི་རྒྱུ་ཡིན་ནམ། འོན་ཏེ་ཚོགས་པ་སྔར་བྱུང་བ་ཁོ་ན་མར་མེ་འོད་དང་བཅས་པ་སྐྱེ་བའི་རྒྱུ་ཡིན་ཞེས་བྱ་བ་འདི་དཔྱད་པར་བྱའོ། །

[Block 1873]
འོ་ན་ནི་ཡོད་དམ་མེད་ན་དེ་དག་དང་ལྷན་ཅིག༌[^931]དེའི་ཕྱིར་རྒྱུ་སྨྲ་བ་རྣམས་རྒྱུ་དང་ལྡན་པའི་རྒྱུའི་མཚན༌[^932]ཉིད་ནི་དེ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1874]
གང་ཞིག་ཡོད་དམ་མེད་ན་གང་ཞིག་ངེས་པར་ཡོད་དམ་མེད་པ་དེ་ནི་རྒྱུ་ཡིན་ཞིང་ཅིག་ཤོས་ནི་རྒྱུ་དང་ལྡན་པ་ཡིན་ལ། ལྷན་ཅིག་འབྱུང་བའི་ཆོས་རྣམས་ཀྱང་གཅིག་ཡོད་ན་ཐམས་ཅད་ཡོད་ལ༌[^933]གཅིག་མེད་ན་ཐམས་ཅད་མེད་པས་རྒྱུ་དེ༌[^934]དང་འབྲས་བུའི་དངོས་པོ་རིགས་པ་ཡིན་ནོ། །

[Block 1875]
རེ་ཞིག་ལྷན་ཅིག་འབྱུང་བ་རྣམས་ནི་རུང་ན་ཕན་ཚུན་དུ་གོ་ཇི་ལྟར་རུང་། དེ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1876]
དེ་ལྟ་ན་འོ་ན་ནི་རྒྱུར་བྱས་པའི་གཟུགས་མེད་ན་མི་འབྱུང་བ་ཕན་ཚུན་དང་འབྱུང་བ་རྣམས་དང་ཡང་ལྷན་ཅིག་དེར་ཐལ་བར་འགྱུར་ལ། སེམས་ཀྱི་མཐུན་པའི་མཚན་ཉིད་ལ་སོགས་པ་ཡང༌[^935]སེམས་ལ་སོགས་པ་དང་དེར༌[^936]ཐལ་བར་འགྱུར་རོ། །

[Block 1877]
འོ་ན་ནི་མྱུ༌[^937]གུ་གསུམ་ཕན་ཚུན་སྟོབས་ཀྱིས༌[^938]གནས་པ་བཞིན་དུ་ལྷན་ཅིག་འབྱུང་བ་རྣམས༌[^939]རྒྱུ་དང་འབྲས་བུའི་དངོས་པོར་འགྲུབ་བོ། །

[Block 1878]
རེ་ཞིག་ཅི་འདི་དག་ལྷན་ཅིག་འབྱུང་བའི་སྟོབས་ཀྱིས༌[^940]གནས་སམ། འོན་ཏེ་ཚོགས་པ་སྔ་མའི་དབང་གིས་དེ་ལྟར་འབྱུང་བ༌[^941]ཞེས་བྱ་བ་འདི་དཔྱད་པར་བྱའོ། །

[Block 1879]
དེ་ལ་གཞན་ཡང་སྲད་བུ་འམ༌[^942]གཟེར་བུ་འམ་རྟེན་པར་བྱེད་པ་ས་ཡང་ཅུང་ཟད་ཡོད་དོ། །

[Block 1880]
དེ་ལ་ཡང་སྐལ་བ་མཉམ་པའི་རྒྱུ་ལ་སོགས་པ་གཞན་དག་ཀྱང་ཡོད་པས་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ཉིད༌[^943]གྲུབ་བོ། །

[Block 1881 [HEADING]]
###### སྐལ་བ་མཉམ་པའི་རྒྱུ། ^2-4-1-1-3-0

[Block 1882]
སྐལ་བ་མཉམ་པའི་རྒྱུ་གང་ཞེ་ན། སྐལ་མཉམ་རྒྱུ་ནི་འདྲ་བའོ། །

[Block 1883]
ཆོས་འདྲ་བ་རྣམས་ནི་ཆོས་འདྲ་བ་རྣམས་ཀྱི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། དགེ་བའི་ཕུང་པོ་ལྔ་པོ་དག་ནི་ཕན་ཚུན་དགེ་བ་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 1884]
ཉོན་མོངས་པ་ཅན་རྣམས་ནི་ཉོན་མོངས་པ་ཅན་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 1885]
ལུང་དུ་མ་བསྟན་པ་རྣམས་ནི་ལུང་དུ་མ་བསྟན་པ་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 1886]
གཞན་དག་ན་རེ་ལུང་དུ་མ་བསྟན་པའི་གཟུགས་ནི་ལྔ་པོ་དག་གི་ཡིན་ལ། བཞི་ནི་གཟུགས་ཀྱི་མ་ཡིན་ཏེ། དམན་པ་དང་སྟོབས་ཆུང་བའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 1887]
ནུར་ནུར་པོ་ནི་ནུར་ནུར་པོ་ལ་སོགས་པ་གནས་སྐབས་བཅུ་པོ་དག་གི་ཡིན་ནོ། །

[Block 1888]
མེར་མེར་པོ་ལ་སོགས་པ་ནི་རིས་མཐུན་པ་གཅིག་ལ་རེ་རེ་ཕྲི་ནས་མེར་མེར་པོ་ལ་སོགས་པའི་ཡིན་ནོ། །

[Block 1889]
རྣམ་པ་མཐུན་པ་གཞན་དག་ཏུ་ནི་གནས་སྐབས་བཅུ་ཆར་ཡང་བཅུ་པོ་དག་གི་ཡིན་ནོ། །

[Block 1890]
ཕྱིའི་དག་ལ་ཡང་ནས་ནི་ནས་ཀྱི་ཡིན་ལ། སཱ་ལུ་ནི་སཱ་ལུའི་ཡིན་ནོ་ཞེས་བྱ་བ་རྒྱས་པར་སྦྱར་བར་བྱའོ། །

[Block 1891]
གང་དག་གཟུགས་ཀྱི་སྐལ་བ་མཉམ་པའི་རྒྱུ་གཟུགས་ཡིན་པར་མི་འདོད་པ་དེ་དག་ལ་ནི་འདས་པའི་འབྱུང་བ་ཆེན་པོ་རྣམས་ནི་མ་འོངས་པའི་འབྱུང་བ་ཆེན་པོ་རྣམས་ཀྱི་རྒྱུ་དང་བདག་པོ་ཡིན་ནོ་ཞེས་བྱ་བའི་གཞུང་འདི་འདོད་པ་ལ་གནོད་པར་གནས་སོ། །

[Block 1892]
ཅི་འདྲ་བ་ཐམས་ཅད་འདྲ་བ་ཐམས་ཅད་ཀྱི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 1893]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། རང་རིས་ས་པའོ། །

[Block 1894]
འདི་དག་ལ་རང་གི་རིས་དང་ས་ཡོད་པས་འདི་དག་ནི་རང་གི་རིས་དང་ས་པ་དག་གོ། །

[Block 1895]
རིས་ནི་ལྔ་སྟེ། སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་ནས་བསྒོམ་པས་སྤང་བར་བྱ་བའི་བར་རོ། །
--- END BLOCKS ---
