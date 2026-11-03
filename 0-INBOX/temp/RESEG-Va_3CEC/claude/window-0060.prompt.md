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
ཡང་ན་སེམས་ལ་རྙོག་པ་མེད་པ་ནི་ཆོས་དེ་ཉིད་ལ་དད་ཅིང་ཡིད་ཆེས་པས་སེམས་དང་བའོ།[^1844] །སྒྲིབ་པ་རྣམས་རྣམ་པར་སེལ་བ་ནི་འདོད་པ་ལ་འདུན་པ་ལ་སོགས་པའི་སྒྲིབ་པ་ལྔ་རྣམས་ནི་མི་ལྡང་བར་གནོན་ཞིང་སེལ་བར་བྱེད་པའོ། །

[Block 2102]
ལྟུང་བ་རྣམས་ལས་འབྱུང་བ་ཤེས་པ་ནི་ཉེས་པ་བྱུང་བ་རྣམས་ཚངས་པ་འམ་ཐར་བར་བྱ་བའི་ཐབས་ལ་མཁས་པ་འམ། གཉེན་པོ་སྤྱོད་པ་ལ་མཁས་པའོ། །

[Block 2103]
འགྱོད་པ་མེད་པ་ནི་དགེ་བ་བྱས་པ་ལ་མི་འགྱེད་པའོ། །

[Block 2104]
ཀུན་ནས་ལྡང་བ་མེད་པ་ནི་ཉོན་མོངས་པ་རྣམས་སེམས་ལ་མི་སྐྱེ་བར་བྱེད་པའོ། །

[Block 2105]
སྒྲུབ་པའི༌[^1845]སྙིང་པོར་བྱེད་པ་ནི་ཚིག་ཙམ་གྱིས་ཆོག་པར་མི་འཛིན་གྱི། །ཇི་ལྟར་ཐོས་པའི་ཆོས་རྣམས་སྒྲུབ་པ་ལྷུར་བྱེད་པའོ། །

[Block 2106]
ཆོས་ལ་གཞོལ་བ་ནི་ཐོས་པའི་དུས་ན་ཇི་ལྟར་བཤད་པའི་ཆོས་རྣམས་ཀྱི་ཚིག་བཟུང་བའི་ཕྱིར་རོ། །

[Block 2107]
ཆོས་ལ་འབབ་པ་ནི་སེམས་པའི་དུས་ན་ཐོས་པའི་ཆོས་ཀྱི་དོན་རྙེད་པའི་ཕྱིར་རོ། །

[Block 2108]
ཆོས་ལ་བབ་པ་ནི་སེམས་པས་རྙེད་པའི་དོན་ལ་ཡང་ནས་ཡང་དུ་བསྒོམས་པས་འབྲས་བུ་དང་ཉེ་བའི་ཕྱིར་རོ། །

[Block 2109]
བརྟུལ་བ༌[^1846]དང་ལྡན་པ་ནི་ཉོན་མོངས་པ་ལ་སོགས་པ་མི་མཐུན་པའི་ཕྱོགས་ཀྱིས༌[^1847]ཟིལ་གྱིས༌[^1848]མི་གནོན༌[^1849]པའོ། །

[Block 2110]
མགོ་དང་གོས་ལ་མེ་འབར་བ་ལྟ་བུ་ནི་སྒྲུབ་པ་ཐམས་ཅད་སྨྱུར༌[^1850]ཏེ་སྒྲུབ་པའོ། །

[Block 2111]
དེ་ལ་ཆགས་པ་ནི་གོང་དུ་སྨོས་པའི་དངོས་པོ༌[^1851]རྣམས་ལ་མ་ཆགས་པར་མི་དམིགས་པའི་ཚུལ་གྱིས་སྤྱོད་པ་འམ། ཟང་ཟིང་ལ་མ་ཆགས་པར་གནས་པའོ། །

[Block 2112]
ཚུལ་ཁྲིམས་མི་ལྷོད་པ་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཡན་ལག་ཕྲན་ཚེགས་ཀྱང་མ་ཉམས་པའོ། །

[Block 2113]
བརྩོན་པ༌[^1852]མི་གཏོང་བ་ནི་དགེ་བ་བསྒྲུབ་པའི་བརྩོན་འགྲུས་ནམས་ཀྱང་མི་འདོར་བའོ། །

[Block 2114]
ཁྱད་པར་འགྲོ་བ་ནི་ཤེས་པ་གོང་ནས་གོང་དུ་ཕྱིར་ཞིང་ཆེར་སྐྱེས༌[^1853]པའོ། །

[Block 2115]
འདུ་འཛི་ལ་མི་དགའ་བ་ནི་འགྲོ་བ་མང་པོའི་ནང་ན་གནས་པར་མི༌[^1854]མོས་པའོ། །

[Block 2116]
གཅིག་པུར་དགའ་བ་ནི་གཅིག་པུར་གནས་པར་མོས་པའོ། །

[Block 2117]
དགོན་པ་ལ་མངོན་དུ་ཕྱོགས་པ་ནི་དགོན་པའི་གནས་སུ་གནས་འཆའ་ཞིང་ཏིང་ངེ་འཛིན་བསྒོམ༌[^1855]པའོ། །

[Block 2118]
འཕགས་པའི་རིགས་ཀྱིས༌[^1856]ཆོག་ཤེས་པ་ནི་འཕགས་པའི་རིགས་བཞི༌[^1857]ལ་གནས་པའོ། །

[Block 2119]
མི་གཡོ་བ་ནི༌[^1858]སྦྱངས་པའི་ཡོན་ཏན་མི་འདོར་བའོ། །

[Block 2120]
འཇིག་རྟེན་གྱི་སྔགས་དྲན་པར་མི་འཛིན་པ་ནི་འཇིག་རྟེན་གྱི་གཙུག་ལག་རྣམས་མི་སློབ་ཅིང་སྔོན་ཤེས་པ་རྣམས་ལ་ཡང་རྒྱུན་དུ་དམིགས་ཤིང་སེམས་པར་མི་བྱེད་པའོ། །

[Block 2121]
འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་ཚོལ་བ་ནི་གསུང་རབ་ཀྱི་ཆོས་རྣམས་ཉན་ཅིང་ཚོལ་བའོ། །

[Block 2122]
བརྗེད་པ༌[^1859]མེད་པ་ནི་མཉན་ཞིང་བརྩལ༌[^1860]བའི་ཆོས་རྣམས་བརྗེད་པར་མི་བྱེད་པའོ། །

[Block 2123]
དོན་རྟོགས་པའི༌[^1861]རྗེས་སུ་འགྲོ་བ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་དོན་རྟོགས་པ་དང་མཐུན་པར་སེམས་ཤིང་དཔྱོད་པའོ། །

[Block 2124]
བློ་གྲོས་ཀྱི་ལམ་དང་མཐུན་པ་ནི་བློ་འམ་ཤེས་རབ་ཀྱིས༌[^1862]འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་ཐོབ་པར་བྱེད་པའོ། །

[Block 2125]
བརྟན་པས༌[^1863]བསྡོམས་པ༌[^1864]ནི་སྡོམ་པ་གང་བླངས་པའི་དངོས་པོ་དེ་ལ་མི་འགྱུར་བས་བརྟན་པར༌[^1865]ལུས་དང་ངག་དང༌[^1866]ཡིད་སྡོམ་པའོ། །

[Block 2126]
རྐྱེན་རྣམས་ཀྱིས༌[^1867]ཡེ་ཤེས་ཀྱི་རྗེས་སུ་འགྲོ་བ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་ཤེས་པ་དང་མཐུན་པའོ། །

[Block 2127]
ཡང་ན་ཆོས་རྣམས་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་མཚན་ཉིད་དུ་ཤེས་པས་གཉིས་སུ་མེད་པའི་ཡེ་ཤེས་ཀྱི་རྒྱུ་བསགས་པའོ། །

[Block 2128]
ངོ་ཚ་ཤེས་པ་དང་ཁྲེལ་ཡོད་པས་བརྒྱན་པ་ནི་བདག་དང་གཞན་ལ་ལྟོས༌[^1868]ནས་རྟག་ཏུ་སྡིག་པ་མི་བྱེད་པའོ། །

[Block 2129]
ཡེ་ཤེས་ཀྱི་རྗེས་སུ་འགྲོ་བ་ལྷུར་བྱེད་པ་ནི་ཇི་སྤྱད་དོ་ཅོག་ཐམས་ཅད་ཡེ་ཤེས་ཐོབ་པར་བྱ་བའི་ཕྱིར་སྤྱོད་ཅིང་སྒྲུབ་པའོ། །ཤེས་རབ་ཀྱི་མིག་རྣམ་པར་དག་པ་ནི་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་ཐམས་ཅད་ལ་མཁས་པའོ། །

[Block 2130]
བློ་ཤིན་ཏུ་རྣམ་པར་དག་པ་ནི་ཤེས་བྱ་དང་ཉོན་མོངས་པའི་སྒྲིབ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2131]
བློ་རྒྱ་ཆེ་བ་ནི་ཐེག་པ་ཆེན་པོ་ལ་དམིགས་པའི་ཕྱིར་རོ། །

[Block 2132]
བློ་མ་ཞུམ་པ༌[^1869]ནི་ཐེག་པ་ཆུང་ངུ་ལ་མ་ཕྱོགས་པས་སོ། །

[Block 2133]
བློ་མ་གྱེས་པ་ནི་ལྟ་བ་སྣ་ཚོགས་ལ་ཆགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2134]
བློ་རབ་ཏུ་གསལ་བ་ནི་རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པའི་ཕྱིར་རོ། །

[Block 2135]
མངོན་སུམ་དུ་ཤེས་པ་ནི་དུས་གསུམ་ལ་སྒྲིབ་པ་མེད་པར་ཤེས་པའི་ཕྱིར་རོ། །

[Block 2136]
ཡོན་ཏན་གཞན་ལ་རག་མ་ལུས་པ་ནི་བདག་གིས༌[^1870]ཡོན་ཏན་རྣམས་ཐོབ་པར་བྱ་བ་གཞན་ལ་མི་བརྟེན་ཞིང་གཞན་གྱི་དྲིང་ལ་མི་འཇོག་པའོ། །

[Block 2137]
བདག་གི་ཡོན་ཏན་མི་སྙེམས་པ་ནི་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་ཤིང་ཡོངས་སུ་རྫོགས་པའི་ཕྱིར་རོ། །

[Block 2138]
གཞན་གྱི་ཡོན་ཏན་བརྗོད་པ་ནི་ཕྲག་དོག་མེད་པའི་ཕྱིར་རོ། །

[Block 2139]
ལེགས་པར་བྱ་བའི་ལས་བྱེད་པ་ནི་དགེ་བ་ཤ་སྟག་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2140]
ལས་ཀྱི་རྣམ་པར་སྨིན་པ་དང་འགལ་བར་མི་བྱེད་པ་ནི་སྟོང་པ་ཉིད་ཀྱི་ཆོས་རྟོགས་ཀྱང་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཡོད་པར་ལྟ་བའོ། །
--- END BLOCKS ---
