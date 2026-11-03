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

[Block 2071]
རྣམ་པ་གང་གིས་འདུས་པར་རྗེས་སུ་མ་ཞུགས་པ་ཉིད་ཅེ་ན། དེའི་ཕྱིར་ལུས་སམ་དེ་ལ་འདུན་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕྱིར་ཟློག༌[^1845]པར་བྱེད་པའི་མཐའ་མ་ཅན་མི་མཐུན་པ་ཉིད་ཅེས་བྱ་བ་འདི་དང་འདི༌[^1846]འབྲེལ་བའོ། །

[Block 2072]
གང་དུ་དེ་རྗེས་སུ་མ་ཞུགས་པ་ཉིད་སྨོས་པ་དེའི་མཚམས་ཀྱི་ཁོངས་སུ་གཏོགས་པ་ཁ་སྐོང་བའི་ཕྱིར་འོས་པ་དེ་ཉིད་ལ་ཆོས་དེ་བཞིན་ནོ་སྙམ་དུ་ཤེས་པར་བྱ་བའི་ཕྱིར་ཡང༌[^1847]གི་སྒྲའོ། །

[Block 2073]
ཕྱི་རོལ་གྱི༌[^1848]མཚམས་སུ་གནས་པ་ལ་ནི་ཕྱིར་ཟློག༌[^1849]པར་བྱེད་པ་སྐྱེ་བ་མ་ཡིན་ཏེ། ཕྱིར་ཟློག་པར་བྱེད་པ་ཞེས་བྱ་བ་ནི་ཕྱིར་ཟློག་པར་བྱེད་པས་ཡང་ཞེས་བྱ་བ་སྟོན་ཏེ། དེ་ལ་མི་མཐུན་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བར་སྦྱར་རོ། །གང་གི་ཕྱིར་ཟློག་པར་བྱེད་ཅེ་ན། དེའི་ཕྱིར་གང་ལ་ལས་དེ་བྱེད་པ་དེ་ལས་གཞན་ནི་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ཕྱིར་བཟློག་པ༌[^1850]འཆགས་ཀྱི་གང་ལ་ལས་དེ་བྱེད་པ་ཉིད་ཀྱིས་ཕྱིར་བཟློག་པ་ནི་མི་འཆགས་སོ། །

[Block 2074]
ཅི་ལས་ཐམས་ཅད་ལ་གང་ལ་བྱེད་པ་བརྩལ་བར༌[^1851]བྱ་བའམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་མི་མཐུན་པ་དང་ཆོས་དང་ལྡན་ན་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་ལས་དེ་ལྟ་བུ་ཡིན་ན་ལས་དེ་ལྟ་བུ་དེ་ལ་བརྩལ༌[^1852]བའོ། །

[Block 2075]
གཞན༌[^1853]མི་མཐུན་པའི་དེ་འཆགས་པ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2076]
ཆད་པ༌[^1854]ལས་གསོལ་བའི་གྲངས་སུ་གཞུག་པ་དག་ནི་གང་ལ་བྱེད་པ་དེས་ཕྱིར་བཟློག་པ༌[^1855]ནི་མི་འཆགས་སོ། །

[Block 2077]
སྦྱིན་པ་དང་དབྱུང་བ་དང་བཟོད་པ་དང་བསྐོ་བ་དག་ལ་ནི་དེ་བས་ན་དེ་བྱེད་པའོ། །

[Block 2078]
འདིར་གཞུང་ནི་གླེང་གཞི་དག་ལས།

[Block 2079]
བཙུན་པ་བཅོམ་ལྡན་འདས་ཀྱིས་གང་ལ་ལས་བྱེད་པ་དེས་ཕྱིར་བཟློག་པ༌[^1856]མི་འཆགས་སོ་ཞེས་གསུངས་པ་དེ་ལ། བཙུན་པ་གང༌[^1857]ལ་ཚོགས་མ་ལགས་པས་ལས་བགྱིས་པ་དེས་སླར་ཟློག་པ་ནི་མི་འཆགས་སམ། ཉེ་བ༌[^1858]འཁོར་འཆགས་སོ། །

[Block 2080]
བཙུན་པ། རེ་ཞིག་གང་ཟག་བཅུ་གཉིས་པོ་དེ་དག་བསྐོ་བ་ན། དེ་དག་འདི་སྐད་ཅེས་བདག་ཅག་མ་བསྐོ་ཅིག༌[^1859]ཅེས་མཆི༌[^1860]ན། དེ་དག་གིས༌[^1861]སླར་བཟློག་པ་ཡང་མི༌[^1862]འཆགས་སམ། ཉེ་བ༌[^1863]འཁོར་འཆགས་ཏེ། མི་འཆགས་སོ་ཞེས་བྱ་བ་དེ་ནི་ངས་ཆད་པའི་ལས་ལ་དགོངས་ཏེ་གསུངས་པ་ཡིན་ནོ། །

[Block 2081]
གང་ཟག་གི་རྣམ་པ་ཇི་ལྟ་བུས་ཕྱིར་བཟློག་པ༌[^1864]འཆགས་ཤེ་ན། དེ་བསྟན་པའི་ཕྱིར་སྤྱོད་ལམ་ལས་མ་ཉམས་པ་དང་། རང་བཞིན་དུ་གནས་པ་དང་། ངག་ཡང་དག་པར་བསྡམས་པ་མངོན་པར་མི་ཤེས་པ་དང་ནང་དང་བཅས་པ་མ་གཏོགས་སོ༌[^1865]ཞེས་སྨོས་ཏེ།[^1866] དེ་ལྟ་བུའི་རྣམ་པ་ཐམས་ཅད་ལས་འཆགས་པར་འོས་པ་ཉིད་དུ་ཐལ་བ༌[^1867]བསྟན་པའི་ཕྱིར། མངོན་པར་མི་ཤེས་པ་དང་ནང་དང་བཅས་པ་མ་གཏོགས་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིས་མངོན་པར་མི་ཤེས་པ་ཞེས་བྱ་བ་འདིས་ནི་བྱིས་པ་དང་རྨོངས་པ་དང་མི་མཁས་པ་དང་། རིགས་ངན་པའོ་ཞེས་གསུངས་པ་གང་ཡིན་པ་དེའི་འདི་བསྡུས་པ་ཡིན་ནོ། །

[Block 2082]
དེ་ནི་འདིར་མི་ཤེས་པ་སྟེ། འདི་ལ་ཕྱིར་བཟློག་པ་དེ་ལ་གཏོགས་པའི་རིགས་པས༌[^1868]སྨྲ་བ་ཉིད་འབྱུང་བར་འགྱུར་ཞེས་བྱ་བ་གཟུང༌[^1869]བར་བྱ་བ་མ་ཡིན་པའི་ཚིག་སྤངས་པ་འདི་ཉིད་ལ་གང་ཞིག་དེ་རྣམས་འཆགས་པའོ། །

[Block 2083]
ནང་དང་བཅས་པ་ཞེས་བྱ་བ་ནི་ཞེ་འགྲས་པའི་དངོས་པོར་རིགས་པ་རྗེས་སུ་གཟུང་བར་བྱ་བ་མ་ཡིན་པས། དེ་རྗེས་སུ་བཟུང་བ་འདི་ལ་ཡང་རིགས་པ་དོགས་པར་བྱ་བ་མ་ཡིན་ཏེ། ཡིད་ཆེས་པ་ལ་བརྟེན་པ་མ་ཡིན་པ་ཉིད་དེ་བས་ན་འདི་ལ་ཚིག་ཏུ་མ༌[^1870]བསྡུས་པ་ཉིད་དོ། །

[Block 2084]
གཞུང་ལས་བཙུན་པ་དུ་དག་གིས་སླར་ཟློག་པ་འཆགས།[^1871] ཉེ་བ༌[^1872]འཁོར་བཞི་སྟེ། རང་བཞིན་དུ་གནས་པ་དང་། དེའི་མཚམས་ན་གནས་པ་དང་། སྤྱོད་ལམ་ལས་མ་ཉམས་པ་དང་། ངག་ཡང་དག་པར་བསྡམས་པས་སོ་ཞེས་གསུངས་པ་ལ། འདིར་ངག་ཡང་དག་པར་བསྡམས་པ་ཉིད་ཀྱིས་གནོང་བར༌[^1873]མི་ཤེས་པ༌[^1874]དང་། ནང་དང་བཅས༌[^1875]པ་གཉིས་གསལ་བར་རིག་པར་བྱའོ། །

[Block 2085]
ནང་དང་བཅས་པ་ལ་དུ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར༌[^1876]བརྗོད་པ་མི་རིགས་པ༌[^1877]ཡིན་ནོ། །

[Block 2086]
མངོན་པར་མི་ཤེས་པ་ལ་ནི་མི༌[^1878]རུང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2087]
དེ་ལྟ་བས་ན་ཚིག་འདི་དག་ལ་བསྡམས་པའི་དབང་གིས་སོ། །

[Block 2088]
དེ་ཞེས་བྱ་བ་ནི་མ་བསྡམས་པ་ཉིད་དེ་དག་ལ་འདི་སྨོས་སོ། །

[Block 2089]
འོ་ན་མདོ་ལས་ཅིའི་ཕྱིར་འདི་དག་བཏང་བར༌[^1879]བྱས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཤིན་ཏུ་གསལ་བར་བསྟན་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2090]
མ་ཉམས་པ་ཞེས་བྱ་བ་ལ། འདིར་ཉམས་པ་ནི་གང་ཡིན། གང་ཞིག་མེད་པས་མ་ཉམས་པ་ཉིད་དོ། །

[Block 2091]
ཅི་རང་བཞིན་དུ་མི་གནས་པ་ཉིད་དམ། མ་བསྡམས་པ་ནི་གང་ཡིན། གང་ཞིག་ཟློག་པ་དང་ལྡན་པས་བསྡམས་པ་ཉིད་ནི་རང་བཞིན་དུ་གནས་པ་ཉིད་དོ་སྙམ་པ་ལ།

[Block 2092]
སིལ་བུ་དག་ལས།

[Block 2093]
བཙུན་པ་ཇི་ཙམ་གྱིས་ན་ངག་ཡང་དག་པར་མ་བསྡམས་པ་ལགས་ཉེ་བ༌[^1880]འཁོར་གང་ཚུན་ཆད་བརྫུན་དུ་སྨྲ་བའམ། ཕྲ་མ་ཅན་ནམ། ངག་རྩུབ་པོ་ཅན་ནམ། ཚིག་འཁྱལ་པ་ཅན་ཡིན་ནའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དག་བསྡུ་བའི་ཕྱིར། བརྫུན་དུ་སྨྲ་བའི་རྗེས་སུ་མཐུན་པ་ཉིད་ནི་ངག་ཡང་དག་པར་མ་བསྡམས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ།[^1881] བརྫུན་དུ་སྨྲ་བའི་རྗེས་སུ་མཐུན་པ་ཉིད་ཅེས་བྱ་བ་ནི། བརྫུན་དུ་སྨྲ་བ་ལས་སེམས་ཕྱིར་མ་བསྡམས་པ༌[^1882]ཉིད་དེ། དེ་ནི་ངག་ཡང་དག་པར་མ་བསྡམས་པ་ཡིན་གྱི། དྲན་པ་ཉམས་པ་གང་ཡང་རུང་བས་བརྫུན་དུ་གྱུར་པ་ནི་མ་ཡིན་ནོ། །

[Block 2094]
ཅི་དེ་འབའ་ཞིག་གིས་ངག་ཡང་དག་པར་མ་བསྡམས་པ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཕྲ་མ་དང་། ངག་རྩུབ་མོ་དང་ཚིག་འཁྱལ་པའི་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྗེས་སུ་མཐུན་པ་ཉིད་ནི་ངག་ཡང་དག་པར་མ་བསྡམས་པའོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^1883]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་ཏེ། དེ་དག་རེ་རེའི་རྗེས་སུ་མཐུན་པ༌[^1884]ཉིད་ཀྱང་འདིར་ངག༌[^1885]ཡང་དག་པར་མ་བསྡམས་པ་ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 2095]
རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པ་ཉིད་ཀྱང་དེ་དག་གིའོ་ཞེས་བྱ་བ་ནི་བརྫུན་དུ་སྨྲ་བ་ལ་སོགས་པ་དེ་དག་གི་རྗེས་སུ་མཐུན་པ་ཉིད་ཡིན་ཏེ་དེ་བས་ན་ངག་ཡང་དག་པར་མ་བསྡམས་པ་དེ་ནི་རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པ་ཞེས་ཀྱང་བྱའོ། །

[Block 2096]
གཞན་ཡང་བྱ་བ་མ་ཡིན་པའོ་ཞེས་བྱ་བ་ནི་ལྟུང་བར་འགྱུར་བ་དག་ལྷག་པར་སྤྱོད་པའི་རྗེས་སུ་མཐུན་པ་ཉིད་ཀྱང་རང་བཞིན་དུ་གནས་པ་མ༌[^1886]ཡིན་པ་ཞེས་བྱའོ། །

[Block 2097]
བྱ་བ་མི་བྱེད་པ་ཞེས་བྱ་བ་ནི་གང་ཞིག་བྱ་བ་གང་ཡིན་པ་དེ་མི་བྱེད་པ་ལ་ལྟུང་བ་བསྐྱེད་པ་ནི་མི་མཐུན་པ་ཉིད་དེ། བསླབ་པ་ཐམས་ཅད་ལ་བརྩོན་པ༌[^1887]བཏང་ཞིང་སྤྲོ་བ་བོར་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2098]
དེ་བརྩམས་པ་འགྲོ་བའི་སེམས་ཀྱིས་བཏང་བ་ནི་སྤྱོད་ལམ་ལས་ཉམས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདུག་པ་ཞེས་བྱ་བའི་སྤྱོད་ལམ་དེ་བརྩམས་ཤིང་སྔར་འདུག་པར་གྱུར་པ༌[^1888]གཞན་དུ་འགྲོ་བའི་སེམས་ཀྱིས་བཏང་བ་ནི་སྤྱོད་ལམ་ལས་ཉམས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་ལ༌[^1889]འཇུག་པ་ཞེ་ན། དེའི་སྤྱོད་ལམ་འདི་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2099]
དགེ་འདུན་གྱི་ནང་ནས་སྟན་ལས་ལངས་པ་ནི་སྤྱོད་ལམ་ལས་ཉམས་པ་ཡིན་གྱི། དེ་ནས་གཞན་དུ་མ་ཡིན་ནོ། །

[Block 2100]
འདིར་གཞུང་ནི་ཉེ་བ༌[^1890]འཁོར་གང་ཚུན་ཆད་དགེ་འདུན་གྱི་ནང་ནས་ལངས་པར་གྱུར་པའོ་ཞེས་བྱ་བ་འདི་གསུངས་པ་ཡིན་ཏེ། སྟན་ལས་ལངས་པ་ཉིད་དང་དགེ་འདུན་གྱི་ནང་ནས་ལངས་པ་ཉིད་མ་སོང་བ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་འདིར་དོན་རྣམ་པར་གཞག་པ་དང་འདྲ་བ་དེ་ནི་འདིའི་དོན་ཏོ། །

[Block 2101]
གནས་སུ་སོང་བ་དོན་གཞན་གཙོ་བོ་ལ་ཞུགས་པ་ཞེས་བྱ་བ་ནི་ཆགས་པའོ། །

[Block 2102]
ལྟ་བ་དགེ་འདུན་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་བྱ་བ་དོགས་པ་ལ་ལྟ་བའི༌[^1891]བློ་ནི་ལྟ་བ་ཞེས་བྱ་བའི་སྒྲ་བརྗོད་པ་ཡིན་ནོ། །

[Block 2103]
གཞན་ལ་ནི་མི་བྱའོ་ཞེས་བྱ་བ་ནི༌[^1892]དགེ་འདུན་ལས་གཞན་པའི་ཚོགས་དགེ་འདུན་མ་ཡིན་པ་ལ་ལྟ་བ་བརྗོད་པར་མི་བྱ་ན། གང་ཟག་ལ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། བསྙེན་པར་མ་རྫོགས་པ་ལ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་ཚུལ་གྱི་དགེ༌[^1893]འདུན་ལ་ཡང་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2104]
ཁ་སྐོང་བར༌[^1894]འོས་པ་མ་ཡིན་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། བསྙེན་པར་རྫོགས་པ་ཡིན་ཡང་དགེ་འདུན་གྱི་ཁ་སྐོང་བའི་འོས་མ་ཡིན་པ་རྣམས་ལ་ཡང་ལྟ་བ་བརྗོད་པར་མི་བྱའོ། །

[Block 2105]
ལྷག་མ་མ་ལུས་པ་ཉིད་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བསྡུས་པའི་གང་ཟག་ཏུ་གཏོགས་པའི་གཞི་ལ་མ་བསྡུས་པའི༌[^1895]གང་ཟག་ལས།
--- END BLOCKS ---
