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
གནས་སུ་སོང་བ་དོན་གཞན་གཙོ་བོ་ལ་ཞུགས་པ་ཞེས་བྱ་བ་ནི་ཆགས་པའོ། །

[Block 2102]
ལྟ་བ་དགེ་འདུན་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་བྱ་བ་དོགས་པ་ལ་ལྟ་བའི༌[^1891]བློ་ནི་ལྟ་བ་ཞེས་བྱ་བའི་སྒྲ་བརྗོད་པ་ཡིན་ནོ། །

[Block 2103]
གཞན་ལ་ནི་མི་བྱའོ་ཞེས་བྱ་བ་ནི༌[^1892]དགེ་འདུན་ལས་གཞན་པའི་ཚོགས་དགེ་འདུན་མ་ཡིན་པ་ལ་ལྟ་བ་བརྗོད་པར་མི་བྱ་ན། གང་ཟག་ལ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། བསྙེན་པར་མ་རྫོགས་པ་ལ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་ཚུལ་གྱི་དགེ༌[^1893]འདུན་ལ་ཡང་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2104]
ཁ་སྐོང་བར༌[^1894]འོས་པ་མ་ཡིན་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། བསྙེན་པར་རྫོགས་པ་ཡིན་ཡང་དགེ་འདུན་གྱི་ཁ་སྐོང་བའི་འོས་མ་ཡིན་པ་རྣམས་ལ་ཡང་ལྟ་བ་བརྗོད་པར་མི་བྱའོ། །

[Block 2105]
ལྷག་མ་མ་ལུས་པ་ཉིད་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བསྡུས་པའི་གང་ཟག་ཏུ་གཏོགས་པའི་གཞི་ལ་མ་བསྡུས་པའི༌[^1895]གང་ཟག་ལས།

[Block 2106]
དེའི་རྒྱུས་གནོད་པ་འབྱུང་བ་སྤང་བའི༌[^1896]ཕྱིར། ལྟ་བ་བརྗོད་པ་ཉིད་མི་བྱའོ། །

[Block 2107]
འདིར་གཞུང་ནི་མ་མོ་ལས།

[Block 2108]
ཆོས་དང་ལྡན་པ་མ་ཡིན་པའི་ལྟ་བ་བརྗོད་པ་ལྔ་གང་ཞེ་ན། གནས་པར་མི་བྱ་བ་ལ་ལྟ་བ་བརྗོད་པ་དང་། ཐ་དད་པར་གནས་པ་ལ་ལྟ་བ་བརྗོད་པ་དང་། བསྙེན་པར་མ་རྫོགས་པ་ལ་ལྟ་བ་བརྗོད་པ་དང་། ཚོགས་ལ་ལྟ་བ་བརྗོད་པ་དང་། ལྷག་མ་མ་ལུས་པའི་དངོས་པོའི་ལྟ་བ་བརྗོད་པ་སྟེ། ལྔ་པོ་དེ་དག་ནི་ཆོས་དང་ལྡན་པ་མ་ཡིན་པའི་ལྟ་བ་བརྗོད་པ་དང་། དེ་ལས་བཟློག་པ་ལྔ་ནི་ཆོས་དང་ལྡན་པའི་ལྟ་བ་བརྗོད་པ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2109]
འདིར་ཚོགས་ཞེས་སྨོས་པ་ནི་དགེ་འདུན་དུ་མར་གྱུར་པ་རྣམས་བཟུང༌[^1897]ངོ་། །གང་རྣམས་ཀྱི་མདུན་དུ་ཆོས་དང་ལྡན་པ་འབྱུང་བ་སྨོས་པ་དེ་རྣམས་ནི་དགེ་འདུན་དུ་གྱུར་པ་རྣམས་ལ་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ། །

[Block 2110]
ལྷག་མ་མ་ལུས་པའི་དངོས་པོའི་ལྟ་བ་བརྗོད་པ་བཀག་པ་ནི་དེའི་ཕྱིར། གང་ཟག་དེ་ལས་དེའི་རྒྱུས་གནོད་པ་འབྱུང་བ་སྤང་བའི་ཕྱིར།

[Block 2111]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 2112]
སྔོན་ལྟུང་བ་བྱུང་བ་ལས་ལྟ་བ་བརྗོད་ན་ཉེས་བྱས་སོ། །

[Block 2113]
རྐུ་ཐབས་སུ་གནས་པ་དང་།

[Block 2114]
དང་པོ་འཁྲུག་པ༌[^1898]དང༌[^1899]བསླབ་པ་བྱིན་པ་དང་། དགེ་ཚུལ་ལ་ལྟ་བ་བརྗོད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 2115]
དེ་བཞིན་དུ་གནས་ནས་ཕྱུང་བ༌[^1900]ལ་ལྟ་བ་བརྗོད་ན་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2116]
དེ་འདིར་བསྡུས་ནས་སྨོས་པ་གང་རྗེས་སུ་གནང་བ་ལ༌[^1901]དབང་བ་དེ༌[^1902]ལ་ནི་འབྱུང་བ་འདི་རིགས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི། གནས་པར་མི་བྱ་བ་ལ་སོགས་པ་རྣམས་ཀྱི་མདུན་དུ་འབྱུང་བ་དགག་པ་འདི་ཡིན་ཏེ། དེ་བས་ན་ཐམས་ཅད་དུ་ཡང་ཁ་སྐོང་བར་འོས་པ་མ་ཡིན་པ་བཀག་པར་ཤེས་པར་བྱའོ། །

[Block 2117]
བསྐོས་པ་རྗེས་ནས་ཆེས་ལེགས་པ་དང་ཆེས་མང་དུ་བྱེད་པ་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི། སྔར་བསྐོས་པའི་གང་ཟག་རྗེས་ནས་བྱ་བ་དེ་ལ་འདི༌[^1903]འབྱུང་བ་འདི་གང་ཞིག༌[^1904]ཆེས་ལེགས་པར་བྱེད་པ་དང་། ཆེས་མང་དུ་བྱེད་པའི་གང་ཟག་གཞན་ཡང་ཡིན་པ་དེ་བསྐོ་བར་བྱའོ། །

[Block 2118]
འདིར་གཞུང་ནི་མ་མོ་ལས་དེ་དང་པོར་བྱས་ཏེ། དེ་སྤང་བར་མི་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 2119]
དུས་ངེས་པར་བྱ་སྟེ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བསྐོ་བར་རོ། །

[Block 2120]
གང་ལ༌[^1905]དུས་ངེས་པར་བྱ་སྟེ་བསྐོ་བར་མི༌[^1906]བྱ་ཞེ་ན། དེའི་ཕྱིར་ཡང་དང་ཡང་དུའམ་གཞན་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་གཞན་དུ་ཡང་དགོས་པ་འབྱུང་ངོ་ཅོག་ཏུ་ཁྱོད་འབའ་ཞིག་བསྐོའོ་ཞེས་དེ་ལྟར་དུས་ངེས་པར་བྱ་སྟེ། མི་བསྐོའོ། །

[Block 2121]
གཞན་ལའོ་ཞེས་བྱ་བ་ནི་དགོས་པ་གཞན་དག་ལ་ཁྱོད་ཁོ་ན་བསྐོའོ་ཞེས་དེ་ལྟར་དུས་ངེས་པར་བྱ་སྟེ། ཡང་མི་བསྐོའོ།[^1907] །གཞན་ལ་ཡང་ཇི་ཙམ༌[^1908]གྱིས་ཆོག་པ་ན་སྤང་བ་སྦྱིན་ནོ་ཞེས་བྱ་བ༌[^1909]ལས་མཐུན་པ་གཅིག་ལ་ཇི་སྲིད་དུ་དགོས་པ་སྤོང་བར་བྱེད་པ་དེ་ལས་བསྐྲད་པར་མི་བྱའོ་ཞེས་བྱ་བའོ། །

[Block 2122]
བསྐོས་པ་མེད་ན་མདུང་དོར་བར་བགོའོ༌[^1910]ཞེས་བྱ་བ་ནི་གང་ཟག་རེ་རེ་ལ་བྱེ་བྲག་གཞན་དང་གཞན་ནི་མདུང་དོར་བའི་གང་ཟག་བསྐོ་བ་པས༌[^1911]མཚན་མའི་བྱེ་བྲག་མི་ཤེས་པས་སོ། །

[Block 2123]
འདིར་མཚན་མའི༌[^1912]ཞེས་ཀྱང་གཅིག་ཏུ་བྱ་སྟེ། དེས་མིག་བཀབ་སྟེ། མདུང་རེ༌[^1913]རྫས་རེའི་སྟེང་དུ་གཞག་པར་བྱའོ། །

[Block 2124]
བསྐོ་བ་པོ་མེད་ན་གང་ཟག་རེ་རེ་ལ༌[^1914]ཆ་རེ་རེའི་ཕྱིར་ཐ་དད་པར་བྱེ་བྲག་གཞན་དང་གཞན་བྱ་སྟེ། བྱེ་བྲག་ཏུ་མཚན་མའི་དབྱེ་བ་ཤེས་པ་རྣམས་ཀྱིས༌[^1915]ཤེས་པ་ལ་འདིར་གཅིག་ཏུ་བྱ་སྟེ། བཀབ་སྟེ་བཞག་ནས་ལག་ཏུ་བྱིན་ནས་གཟུང་བར༌[^1916]བྱ་བ་དེ་བཞིན་དུ་གང་ལ་གང༌[^1917]ཞིག་མཚན་མ་གཞག་པ་དེ་ནི་དེའི་སྐལ་བ་ཡིན་ནོ། །

[Block 2125]
གང་ཞིག་འཇིག་རྟེན༌[^1918]ན་རྒྱན༌[^1919]འགྱེད་པའི་ཆོ་གར་གྲགས་པ་དེ་འདིར་རྣམ་པ༌[^1920]གཞན་གྱིས་སྨོས་པ་སྟེ། མི་མཐུན་པ་ལ་རྣམ་པར་གཞག་པ་འདིའོ། །

[Block 2126]
ཡོད་པར་གྱུར་པ་གང་ཞིག་དེས་སྐལ་བ་སྦྱིན་པ་དེའི་ཞེས་བྱ་བར་རྣམ་པར་གཞག་པར་བྱའོ། །

[Block 2127]
བསྐོས་པ་མེད་ན་སྣོད་སྤྱད་འགྱེད་པའི་རྣམ་པར་གཞག་པ་འདི་ལྟ་སྟེ། ཆ་གང་ཞིག་དེས༌[^1921]གང་ལ་སྟེར་བ་དེ་དེའི་ཞེས་བྱ་བར་རྣམ་པར་གཞག་གོ། །

[Block 2128]
བགོའོ་ཞེས་བྱ་བ་ནི་གོས་ཀྱི་གཞི་ལས་གསུངས་སོ། །

[Block 2129]
གོས་དེ་དག་ཇི་ལྟར་བགོ་བར་བྱ་ཞེ་ན། ཉེ་བ༌[^1922]འཁོར་མདུང་དོར་བས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2130]
འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རྣམ་པ༌[^1923]ཐམས་ཅད་དུ་ཤེས་པར་བྱ་སྟེ། འདི་གོས་ཀྱི་གཞི་ཞུ་བ་ལས་གསུངས་པ་ཡིན་ནོ། །

[Block 2131]
གང་ཁ་སྐོང་བར་མི་འོས་པ་དེ་མདུང་དོར་བར་ཡང༌[^1924]ཞེས་བྱ་བ་ལ། དེ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ཡང་ལས་བྱེད་པའི་ཆོ་ག་ཁོ་ན་རྗེས་སུ་འཇུག་པ་ཞེས་བྱ་བ་འདིར་རྣམ་པར་གཞག་སྟེ། གླེང་གཞི་དག་ལས་སོ། །

[Block 2132]
དགེ་འདུན་གྱི༌[^1925]དབྱེན་ལ༌[^1926]ཡང་འོས་པ་མ་ཡིན་པས་ཚུལ་ཤིང་བྲིམ་པ༌[^1927]མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་གདུལ་བྱ་དང་ལྡན་པའི་ལས་ཀྱི་ལྡང་བར༌[^1928]རྣམ་པར་གཞག་གོ། །

[Block 2133]
སངས་རྒྱས་ཀྱི་གདུལ་བྱ་ལས་ཉམས་པར་ཤེས་པར་མི་བྱའོ། །

[Block 2134]
དེ་བས་ན་འདི་སངས་རྒྱས་ཀྱི་གདུལ་བྱ་དང་ལྡན་པའི་ལས་ཀྱི་ཆོ་ག་ལ་ཡན་ལག་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་བསྟན་པའི་དོན་དུ་འདི་རྩོམ་པའོ། །

[Block 2135]
སངས་རྒྱས་དང་དགེ་འདུན་དུ་གཏོགས་པ་ལ་ཚུལ་འདིའོ། །

[Block 2136]
གཞན་དུ་སངས་རྒྱས་དང་ཆོས་ཀྱི་རྣམ་པར་གཞག་པ་མི་གནས་སོ་ཞེས་བྱ་བ་ལས་ཆོ་ག་འདི་ནི་སིལ་བུ་དག་ལས་གསུངས་པ་ཡིན་ནོ། །

[Block 2137]
ལས་ཀྱི་གཞིར་གཏོགས་པའོ།། །།

[Block 2138]
བརྗོད་པ་ལྷག་པ་དག་གིས་ནི་མ་བྱས་པ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ལ་ལས་བརྗོད་པ་དག་ལྷག་པར་བྱེད་པ་དེ་ལ༌[^1929]ཆོ་ག་ལས་འདས་ནས་ལས་མི་འཆགས་སོ་ཞེས་བྱ་བའི་ཉེས་པར་འགྱུར་བའི་དོགས་པར་མི་བྱའོ། །

[Block 2139]
རང་གི་དོན་ནི་བྲལ་བ་དང་སྟོང་པ་དང་ལྡན་པར་སྨོས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྣམས་འདིར་ལས་བརྗོད་པའི་ཚིག་གིས་བསྡུས་པར༌[^1930]རིག་པར་བྱའོ། །

[Block 2140]
མ་མོ་ལས།
--- END BLOCKS ---
