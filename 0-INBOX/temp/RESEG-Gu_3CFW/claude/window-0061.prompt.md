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

[Block 2141]
འདིར་དང་པོར་བྱས་ཏེ། རྗེས་སུ་བསྒྲགས་པ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པའོ། །

[Block 2142]
ཉམས་ན་མ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གང་ལ་ལས་བརྗོད་པ་ཇི་སྙེད་གསུངས་པ་དེ་ལས་ཉམས་ན་ནི་ལས་དེ་མ་བྱས་པ་ཉིད་དོ། །

[Block 2143]
བྱེད་པ་ཉིད་ནི་སོང་ན་ཚིག་མ་རྫོགས་པ་རྣམ་པར་འཁྲུགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ལས་བྱེད་པ་དག་སོང་ན་གང་དེའི་ཚེ་གསོལ་བའི༌[^1931]བདག་ཉིད་ཀྱི་ཚིག་མ་རྫོགས་པ་གང་ཡིན་པ་དེ་རྣམ་པར་འཁྲུགས་པ་ཉིད་ཡིན་ཏེ། གང་ཞིག་ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་དེ་ལ་ནི་མ་ཡིན་པ༌[^1932]བྱས་པ་ཉིད་མ་ཡིན་གྱི། རྫོགས་པར་བྱས་པ་གང་ཡིན་པ་དེ༌[^1933]ནི་བྱས་པ་ཁོ་ན་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2144]
ལས་དེ་ལ་དགེ་འདུན་གྱི་ཚད་དག་ཏུ་མ་ལངས་པ་རྣམས་མ་ལུས་པ་ཉིད་ན་རྫོགས་པའོ་ཞེས་བྱ་བ་ནི་རྩོམ༌[^1934]པར་བྱས་པར་གྱུར་པ༌[^1935]ཉིད་ལ་ནི་བྱེད་པར་འགྱུར་བའོ། །

[Block 2145]
ལས་དེ་དགེ་འདུན་གྱི་མཐའ་བཅུའི་ཚོགས་ལ་སོགས་པ་དེའི་ཚད་དག་ཏུ་དེ་ནས་མ་ལངས་པ་རྣམས་མ་ལུས་པ་ཉིད་ཡིན་ན་ནི། ཚིག་རྫོགས་པ་དག་ཀྱང་རྣམ་པར་འཁྲུགས་པ་ཉིད་ཡིན་ནོ། །

[Block 2146]
འདིར་ལངས་པ་ནི་སྟན་ལས་འཕགས་པར་རིག་པར་བྱའོ། །

[Block 2147]
ལུས་པ་ཉིད་ན་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་ལུས་པ་ཉིད་ན་དེའི་ལས་དང་དགེ་འདུན་གྱི་ཚད་མ་ལངས་པ་དག་དེའི་ཚེ། ལས་ཀྱི་ཚིག་སྔར་བརྗོད་པ་རྣམ་པར་འཁྲུགས་པར་མི་འགྱུར་བ་དག་གོ། །

[Block 2148]
གལ་ཏེ་དེ་ཡང་བྱེད་པར་འདོད་ན་ཚིག་གིས་རྣམ་པར་དཀྲུག༌[^1936]ཅིང་གསོལ་བས་དགེ་འདུན་ལ་བཙུན་པ་དག་ཡང་གསོལ་བར་བགྱིའོ། །

[Block 2149]
ཞི་འམ། [^1937]རྗེས་སུ་བསྒྲག་གོ་ཞེས་བྱ་བས་སོ་ཞེས་བྱ་བ་ལ། དེ་ཡང་བྱེད་པར་འདོད་ན་ཞེས་བྱ་བ་ནི་ཚིག་རྣམ་པར་མ་འཁྲུགས་པ་དེ་ལའོ། །

[Block 2150]
ཇི་ལྟར་ཚིག་གིས་རྣམ་པར་དཀྲུག་པར་བྱ་ཞེ༌[^1938]ན། གསོལ་བས་སོ། །

[Block 2151]
འདིས་སུ་ལ་གསོལ་བར་བྱེད་ན། དགེ་འདུན་ལ་གསོལ་བས་སོ། །

[Block 2152]
རྣམ་པ་གང་གིས་ཤེ་ན། དེའི་ཕྱིར་བཙུན་པ་དག་ཡང་གསོལ་བར་བགྱིའོ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^1939]རྣམ་པར་དཀྲུག་ཅིང་ལས་དེ་སླར་བྱ་སྟེ། རྣམ་པར་མ་དཀྲུགས་པས་ནི་མ་ཡིན་ཏེ། དེ་བས་ན་དེ་བྱེད་པའོ། །

[Block 2153]
འདི་ནི་བསྟན་པ་ཡིན་ཏེ་དེ་ལུས་པའི་ཚིག་གཉིས་རྫོགས་ཟིན་པའི་དབང་དུ་བྱས་ཏེའོ། །

[Block 2154]
གསོལ་བ་ཙམ་རྫོགས་ཟིན་པ་དེ་ལས་གསོལ་བར་བགྱིའོ་ཞེས་བྱ་བའི་བར་བརྗོད་པར་བྱ་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2155]
གསོལ་བ་མ་བྱས་པའི་ཚིག་དག་ལ་དེ་སྤངས་ཏེ། དེས་ན་གང་ཟག་ལ་ལྷུང་བཟེད་ལ་སོགས་པ་བྱིན་གྱིས་བརླབ་པའི་ཚིག་དེ་ཡང་རང་བཞིན་དང་བྲལ་བ་ཉིད་ལ་ཉམས་པར་འགྱུར་རོ། །

[Block 2156]
དེ་ལྟ་བས་ན་འདིར་དགེ་འདུན་ལ་ཞེས་བྱ་བ༌[^1940]སྨོས་པ་དེ་ནི་དཔེ་ཙམ་དུ་ཟད་དེ། བཟློག་པའི་ཕྱིར་བསྒོ་བ་དང་། བསྙིལ་བ་དང་། དེའི་ངོ་བོ་ཉིད་ཚོལ་དུ་གཞུག་པ་དང་། བསླབ་པ་དང་མཐུན་པ་དང་། དེའི་གསོ་སྦྱོང་དང་། མུ་སྟེགས་ཅན་གྱི་གནས་པ་དང་། དེ་ལས་གཞན་པའི་སྤོ་བ་དང་། མགུ་བ་དང་། ཡང་གཞི་ནས་བསླང་བ་དང༌[^1941]དྲན་པས་འདུལ་བ་དང་། མ་མྱོས་པར་འདུལ་བ་སྦྱིན་པ་དང་། བསྙེན་པར་རྫོགས་པར་བྱ་བ་དང་། མཚམས་དགྲོལ་བ་དང་། ནན་ཏུར་གྱི་ལས་དང་། དབྱུང་བ་དག་ལ་ནི་བརྗོད་པ་གསུམ་མོ་ཞེས་བྱ་བ་ལ། དེ་ལས་བཟློག་པའི་ཕྱིར་བསྒོ་བས་ཞེས་བྱ་བ་ནི་དགེ་འདུན་འབྱེད་པའི་ཕྱིར་བརྟུལ་བ་ལ་སོགས་པ་དེ་རྗེས་སུ་འཇུག་པ་རྣམས་ཀྱི་འདུན་པ་ལ་སོགས་པས་འགྲོ་བ་ཉིད་ལས་ཀྱིས༌[^1942]བརྗོད་པར་གྱུར་པ་ལ་བདག་ཉིད་བརྗོད་པར་བྱ་བ་མ་ཡིན་པ་བྱེད་ཅིང་དགེ་སློང་དང་དགེ་ཚུལ་སྡིག་པ་ཅན་གྱི་ལྟ་བའི་རྣམ་པ་མི་གཏོང་བ་གནས་ནས་ཕྱུང་བ་རྗེས་སུ་འཇུག་པའི་དགེ་སློང་མ་དཀོན་མཆོག་དག་གཏོང་བ་ལ་སོགས་པ་གཞི་ལ་ཞུགས་པ་དག་བཟློག་པའི་ཕྱིར་བསྒོ་བ་སྟེ། དགེ་ཚུལ་སྡིག་པ་ཅན་གྱི་ལྟ་བའི་རྣམ་པ་མི་གཏོང་བ་དེའི་ངོ་བོ་ཉིད་ཚོལ་དུ་གཞུག་པ་སྦྱིན་པ་དང་གང་གི་བསླབ་པ་སྦྱིན་པ་པོར་གྱུར་པ་དང་། མཐུན་པ༌[^1943]སྦྱིན་པ་དང་། མཐུན་པའི་གསོ་སྦྱོང་སྦྱིན་པ་དང་། མུ་སྟེགས་ཅན་གྱི་གནས་པ་སྦྱིན་པ་ཞེས་བྱ་བས་ནི། མུ་སྟེགས་ཅན་རབ་ཏུ་དབྱུང་བར༌[^1944]འདོད་པ་ལ། ཟླ་བ་བཞིའི་བར་དུ་མཁན་པོས་སྦྱར་བའི་གོས་ཀྱི་གནས་པ་སྦྱིན་པའི་ལས་གཅིག་བསྟན་ཏོ། །

[Block 2157]
དེ་ལས་གཞན་པའི་སྤོ་བ་སྦྱིན་པ་ཞེས་བྱ་བ་ནི་མུ་སྟེགས་ཅན་ལ་ཟླ་བ་བཞིའི་བར་དུ་མཁན་པོས་སྦྱར་བའི་གོས་ཀྱི་གནས་པ་སྦྱིན་པ་ལས་གཞན་པ། དགེ་འདུན་ལྷག་མའི་བཅབས་པ་ལ་སྤོ་བ་སྦྱིན་པའི་ལས་ཡིན་པའོ། །

[Block 2158]
མགུ་བ་སྦྱིན་པ་ཞེས་བྱ་བས་ནི། དགེ་འདུན་ལྷག་མའི་ལྟུང་བའི་ཕྱིར་མགུ་བ་སྦྱིན་པ་དང་། ལྕི་བའི་ཆོས་ཀྱི་ལྟུང་བའི་མཚན་མ་མགུ་བ་ལའོ། །

[Block 2159]
ཡང་གཞི་ནས་བསླང་སྟེ༌[^1945]སྦྱིན་པ་ཞེས་བྱ་བ་ནི། སྤོ་བ་དང་མགུ་བར་བྱ་བ་བྱེད་པའི་སྐབས་སུ་ལྷག་མའི་ལྟུང་བ་བྱུང་ན་གཞི་ནས་སྤོ་བ་དང་། གཞི་ནས་མགུ་བར་བྱ་བ༌[^1946]དང་། ཡང་གཞི་ནས་བསླང་སྟེ།[^1947] སྤོ་བ་དང་། ཡང་གཞི་ནས་བསླང་སྟེ༌[^1948]མགུ་བར་བྱ་བ་དག་གིས་འདིར་གཞི་ནས་བསླངས་པའི་སྒྲ་རིག་པར་བྱའོ། །

[Block 2160]
ཡང་གཞི་ནས་བསླངས་པར་གྱུར་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཞེས་བྱ་བས་ཡང་གཞི་ནས་བསླངས་པ་ལ་སོགས་པ་བཞི་པོ་རྣམས་ཀྱང་ཡང་གཞི་ནས་བསླངས་ཏེ་མགུ་བར་བྱ་བ་སྦྱིན་པ་ལ་སོགས་པའི་སྒྲས༌[^1949]བརྗོད་དོ་ཞེས་བྱ་བ་ལ་དགོངས་པའོ། །

[Block 2161]
དྲན་པས་འདུལ་བ་སྦྱིན་པ་ཞེས་བྱ་བས་ནི་དྲན་པས་དང་མ་མྱོས་པས་འདུལ་བ་སྦྱིན་པ་གཉིས་བསྟན་ཏོ། །

[Block 2162]
བསྙེན་པར་རྫོགས་པར་བྱ་བ་དང་མཚམས་དགྲོལ་བ་ཞེས་བྱ་བས་མཚམས་དགྲོལ་བའི་ལས་གཅིག་བསྟན་ཏོ། །

[Block 2163]
ནན་ཏུར་གྱི་ལས་ཞེས་བྱ་བ་ནི་འདི་ལྟ་སྟེ། བསྡིགས་པ་དང་། སྨད་པ་དང་། བསྐྲད་པ་དང་། ཕྱིར་འགྱེད་པ་དང་མ་མཐོང་བས་གནས་ནས་དབྱུང་བ་དང་། ཕྱིར་མི་འཆོས་པས་གནས་ནས་དབྱུང་བ་དང་། སྡིག་པ་ཅན་གྱི་ལྟ་བའི་རྣམ་པ་མི་གཏོང་བས༌[^1950]གནས་ནས་དབྱུང་བ་དང་། དབྱུང་བ་དག་ལ་ནི་བརྗོད་པ་གསུམ་མོ་ཞེས་བྱ་བ་ནི་ལས་ལན༌[^1951]གསུམ་དུ་བརྗོད་པའོ། །

[Block 2164]
དེ་ལྟར་འདུལ་བའི་གཞུང་ལས་བགྲང་བ་དང་། བཤུང་བ་བྱེད་པ་དང་། ཁྱིམ་གྱི་བསླབ་པའི་སྡོམ་པ་སྦྱིན་པ་དང་། ཕྱག་མི་བྱ་བའི་བསླབ་པའི་སྡོམ་པ་སྦྱིན་པ་དང་། རྩོད་པ་སྤོང་བར་བྱེད་པ་བསྐོ་བ་དང་། བཟོད་པ་གསོལ་བ་ཞེས་བྱ་བའི་ལས་དྲུག་པོ་འདི་རྣམས་ལ༌[^1952]ལན་གསུམ་རྗོད་པར༌[^1953]བྱེད་པ་ཞེས་བྱ་བ་འདི་སྟོན་པར༌[^1954]བྱེད་པ་མཐོང་བར་བྱེད་པ་དེ་དག་ནི་འདིར་གསོལ་བ་དང༌[^1955]བཞིའི་ལས་སུ་མ་བྱས་སོ། །

[Block 2165]
དེ་ལྟར་གང་ལས་ཤེས་ཤེ་ན།

[Block 2166]
གཏམ་གྱི་གཞི་ལས།

[Block 2167]
ལས་ཀྱི་གྲངས་བརྗོད་པ་ལས་འབྱུང་སྟེ། བཙུན་པ་ལས་རྣམ་པ་དུ་མཆིས། ཉེ་བ༌[^1956]འཁོར་བརྒྱ་རྩ་གཅིག་གོ། །

[Block 2168]
བཙུན་པ་ལས་དུ་རྣམས་ཀྱིས་ལས་རྣམས་བསྡུས། ཉེ་བ༌[^1957]འཁོར་གསུམ་གྱིས་ཏེ་གསུམ་གང་ཞེ་ན། གསོལ་བའི་ལས་དང་། གསོལ་བ་དང༌[^1958]གཉིས་ཀྱི༌[^1959]ལས་དང་། གསོལ་བ་དང༌[^1960]བཞིའི་ལས་ཀྱིས་སོ། །

[Block 2169]
དེའི་དབྱེ་བ་རྣམས་ནི༌[^1961]གཏམ་གྱི་གཞི་དེ་ཉིད་ལས་ལྟ་བ་རྣམ་པ་གསུམ་དུ་གསུངས་སོ། །

[Block 2170]
བཙུན་པ་ལས་བརྒྱ་རྩ་གཅིག་པོ་གང་ལགས་པ་དེ་རྣམས་ལ་གསོལ་བའི་ལས་རྣམས་ནི་དུ། གསོལ་བ་དང་གཉིས་ཀྱི༌[^1962]ལས་དག་ནི་དུ། གསོལ་བ་དང་བཞིའི་ལས་རྣམས་ནི་དུ་མཆིས། བཀའ་སྩལ་པ། ཉེ་བ༌[^1963]འཁོར་གསོལ་བའི་ལས་རྣམས༌[^1964]ནི་ཉི་ཤུ་རྩ་བཞིའོ། །

[Block 2171]
གསོལ་བ་དང་གཉིས་ཀྱི་ལས་ནི་བཞི་བཅུ་རྩ་བདུན་ནོ། །

[Block 2172]
གསོལ་བ་དང་བཞིའི་ལས་ནི་སུམ་ཅུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2173]
ལས་ཀྱི་གཞི་ཉིད་ལས་དབྱེ་བའི་ཚད་དེ་ལྟ་བུ་རྣམས་ལ༌[^1965]ལས་རྣམ་པར་གཞག་པའི་སྐབས་སུ་ངོ་བོ་ཉིད་བརྗོད་པ་ཡིན་ནོ། །

[Block 2174]
དེའི་ཕྱིར།

[Block 2175 [VERSE]]
གསང་དང་ནང་དུ་དྲི་ཕྱིར་དང་། །
གསོ་སྦྱོང་དེ་ལ་ལྟུང་བཅས་དང་། །
དེ་ལ༌[^1966]དགེ་འདུན་ཡིད་གཉིས་དང་། །
རྩོད་དང་ངེས་ཉིད་མ་ཡིན༌[^1967]དང་། །
--- END BLOCKS ---
