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
[Block 2311]
དགེ་འདུན་ནམ་གཅིག་ཁོ་ན་ལ་མ་བརྟེན་པ་ནི་གང་ཟག་དགེ་སློང་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ལ་གང་དུ་འདིར་དགེ་འདུན་ནམ་གང་ཟག་གསོལ་བར་བྱ་བ་ལ་མི་བརྟེན་པར༌[^2094]ནི་འདི་ལྟ་སྟེ། གནས་ལ་སོགས་པའི༌[^2095]མིང་བརྗོད་པ༌[^2096]སྟེ། གྲོང་དུ་ཞུགས་པའི་དོན་དུའོ། །

[Block 2312]
ལྟ་བ་དག་དང་། དེ་ལས་གཞན་དུ་གཅིག་པུ་བྱ་བ་ཉིད་ལ་འདི་ལྟ་སྟེ། རྫས་བྱིན་གྱིས་བརླབ་པ་དང་། ཉིན་ཞག་བྱིན་གྱིས་བརླབ་པ་ལ་གང་ཟག་གི་དེར་གསོལ་བར་བྱ་བ་ཉིད་ཤེས་པར་བྱའོ། །

[Block 2313]
དགེ་སློང་གཞན་ལ་བརྗོད་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་ལ་སོགས་པ༌[^2097]ཉིད་ཡིན་གྱི་གཞན་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2314]
ཆོས་གོས་དབྱུང་བ་དང་བྱིན་གྱིས་བརླབ་པ་ནི་ཉེ་བར་མི་གནས་ན་ཡིད་ཀྱིས་རྣམ་པར་བརྟགས་པས་འཆགས་སོ་ཞེས་བྱ་བ་ལ་ཉེ་བར་མི་གནས་ན་ཞེས་བྱ་བ་ནི་དབང་དུ་བྱ་བ་ཉིད་ཀྱི་ཕྱིར་དགེ་སློང་ལའོ། །

[Block 2315]
འདིར་ཆོས་གོས་ཉེ་བར་མི་གནས་ན་རྣམ་པར་བརྟག་པ་དང་བྱིན་གྱིས་བརླབ་པ་དག་བྱའོ། །

[Block 2316]
ཕྱིར་བཏང་བ་ནི་ཉེ་བར་གནས་པ་དགོས་པ་ཡིན་གྱི།[^2098] དེ་བས་ན་ཆོས་གོས་ཉེ་བར་མི་གནས་པ་ལ་བཏང་བ་མ་གྲུབ་པ་ཤེས་པར་མི་བྱའོ། །

[Block 2317]
དགེ་སློང་ཉེ་བར་གནས་པ་ཡོད་པར་གྱུར་པ་ལག་ཏུ་བྱ་སྟེ་བཏང་བ་ཉིད་དོ། །

[Block 2318]
འདིར་གཞུང་ནི་དགེ་སློང་དག་ལྔ་པོ་འདི་དག་ནི་སེམས་བསྐྱེད་པས་འགྲུབ་པ་ཡིན་ཏེ། གསོ་སྦྱོང་དང་དགག་དབྱེ་དང་ཆོས་གོས་བྱིན་གྱིས་བརླབ་པ་དང་། ཆོས་གོས་རྣམ་པར་བརྟག་པ་དང་། གང་ཟག་གི་མགྲོན་དུ་བོས་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2319]
དེ་ལ་གསོ་སྦྱོང་དང་དགག་དབྱེ་གཉིས་ལ་མདོ་འདི་བྱས་པ་མདུན་རོལ་དུ་ཞེས་བྱ་བ་འདིར་བསྡུ་བ་མ་བྱས་པའོ། །

[Block 2320]
འདིར་མགྲོན་དུ་བོས་པ་བླངས་པས་ཆོ་ག་བརྗོད་པར་རིག་པར་བྱའོ། །

[Block 2321]
དེ་ལྟར་འདི་ལ་ཁས་ལེན་པར་མི་བྱ་ཞེས་བྱ་བ་འགའ་ཞིག་ཏུ་ཡང་འགྲུབ་པ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2322]
དེ་ཡང་ཡོད་པ་མ་ཡིན་ཏེ། འདི་ལ་འདི་ལྟར་འཕེལ་བ་ཞེས་བྱ་བ་སྨོས་པས་རྣམ་པ༌[^2099]དེ་ལྟར་འདི་མི་བྱ་ཞེས༌[^2100]བྱ་བ་དེ་བས་ན་དེ་མདོར་མ་བྲིས་སོ། །

[Block 2323]
མི་སྨྲ་བའི་ངོ་བོ་དང་དུ་ལེན་པས་དེ་བྱ་བའི་དེའི་ངོ་བོ་མཉམ་པར་སྦྱར་བ་ཡོད་པ་ལ་ཚིག་གིས་ཞེས་བྱ་བ་འདིར་ཆོ་ག་ཤེས་པར་བྱ་སྟེ། མདོའི་རྗེས་སུ་འབྲངས༌[^2101]ནས་ཀྱང་ངོ་། །གང་ཟག་གིས་མགྲོན་དུ་བོས་པ་སེམས་བསྐྱེད་པས་འགྲུབ་པ་ནི་ཅང་མི་གསུང་པས༌[^2102]ཞེས་མདོའི་སྡེ་ལས་གསུངས་པ་ཡིན་ནོ། །

[Block 2324]
དེའི་ངོ་བོ་མཉམ་པར་སྦྱར་བ་ཡོད་པ་ལ་ཚིག་གིས༌[^2103]སོ། །

[Block 2325]
གལ་ཏེ་དེ་རྒྱལ་པོ་ཆེན་པོ་ཁྱོད་ཀྱི་བཙུན་མོ་ཕྲེང་ལྡན་མ་རྗེས་སུ་ཤེས༌[^2104]ན་དེ་ལྟར་དུ་བདག་ནི་དང་དུ་མི་ལེན་པ་ཞེས་བྱའོ། །

[Block 2326]
འདིར་རིགས་པས་ཀྱང་བརྗོད་པའི་རྣམ་པ་ཉིད་འདིར་ཚིག་མྱུར་བ་ཉིད་དུ་བསྟན་པའོ། །

[Block 2327]
འདིར་ཅང་མི་གསུང་བས༌[^2105]གནང་ངོ་ཞེས་གསོལ་བ་མ་གྲུབ་པ་མ༌[^2106]ཡིན་ཏེ། དེ་ལྟ་བས་ན་འདིར༌[^2107]ཅང་མི་གསུང་བའི་ངོ་བོ་ནི་ལེགས་པ་ཡིན་ནོ། །

[Block 2328]
སྔ་མ་མ་ཕྱུང་ན་ཕྱི་མ་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་དངོས་པོ་ལ་སྔར་བྱིན་གྱིས་བརླབས་པ་མ་ཕྱུང་བར་གཞན་བྱིན་གྱིས་རློབ་པར་བྱེད་པ་གང་ཡིན་པ་དེ་མི་འཆགས་སོ། །

[Block 2329]
གཅིག་པུས་བྱིན་གྱིས་རློབ་ན་དེ་ལ་དང་པོར་བསམ་པ་བསྒྲུབ་ཅིང་ཚིག་ཏུ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་གཅིག་པུས་བྱིན་གྱིས་རློབ་པར་བྱེད་ན་ཡང་དེ་ལ་ཡང་ཚིག་ཏུ་བརྗོད་པས་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 2330]
འདིར་གཞུང་ནི་དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 2331]
དེ་ལྟར་སེམས་བསྐྱེད་པར་བྱ་ཞིང་ཚིག་ཏུ་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2332]
དགེ་སློང་དང་འདུ་བ་ཉིད་ན་བླ་གོས་ཕྲག་པ་གཅིག་ཏུ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འཆགས་པ༌[^2108]ལ་སོགས་པ་དག་ལ་དགེ་སློང་དང་ལྷན་ཅིག་འདུ་བ་ཉིད་ན་བླ་གོས་ཕྲག་པ་གཅིག་ཏུ་བྱས་པ་ཉིད་ཀྱིས་ཀུན་ནས་གཡོགས་པ་དང་བྲལ་བ་ཉིད་རིགས་པར་བལྟ་བར་བྱའོ། །

[Block 2333]
རང་གི་དོན་དུ་སྔགས་ལན་གསུམ་བརྗོད་པར༌[^2109]བྱེད་པ་ཉིད་ན་དེའི་འོས་ཉིད༌[^2110]ལ་ཕྱག་བྱས་ཏེའོ་ཞེས་བྱ་བ་ནི། རང་གི་དོན་དུ་དགེ་འདུན་ནམ་གང་ཟག་གང༌[^2111]ལ་བརྗོད་པའི་བདག་ཉིད་དམ། གཞན་གང་ཡང་རུང་བའི་སྔགས་ལན་གསུམ་བརྗོད་པ་ཉིད་ཀྱིས་མདུན་རོལ་དུ་གལ་ཏེ་བཟླས་ཏེ་ཕྱག་བྱ་བ་ཉིད་ཡིན་ན་ཕྱག་བྱ་སྟེ་བརྗོད་པར་བྱ་བའི་དུས་ནི་རིགས་པའོ། །

[Block 2334]
གསང་སྟེ༌[^2112]སྟོན་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་ཕྱག་བྱས་ཏེ་བྱ་བར་རིགས་པའོ། །

[Block 2335]
སྣམ་སྦྱར་དང་བཅས་པ་ཉིད་ལ་བསྙེན་པར་རྫོགས་པའི་ཕྱིར་འདུས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པར་བྱ་བའི་ཕྱིར་འཁོད་པ༌[^2113]ལ་སྣམ་སྦྱར་དང་བཅས་པ་ཉིད་དུ་གྱུར་པ་ནི༌[^2114]བསྙེན་པར་རྫོགས་པར་བྱ་བ་དེས་ཕྱག་བྱ་བ་ཉིད་དུ་རིགས་པའོ། །

[Block 2336]
ཆོས་གོས་བྱིན་གྱིས་བརླབ་པ་ལ་སྣམ་སྦྱར་དང་བཅས་པ༌[^2115]ཉིད་དེ༌[^2116]དེའི་གནས་སྐབས་ཅན་ལ་བསྟན་པར༌[^2117]རིག་པར་བྱའོ། །

[Block 2337]
དང་པོར་གསུམ་མོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པར་བྱ་བའི་ཕྱིར་འདུས་པའི༌[^2118]དང་པོར་དགེ་སློང་དང་ཕྲད་དོ་ཅོག་ཐམས་ཅད་ལ་བསྙེན་པར་རྫོགས་པར་བྱ་བ་དེས་ཕྱག་བྱ་བར་རིགས་པ་ཡིན་ནོ། །

[Block 2338]
དེ་ཡང་ལན་ཅིག༌[^2119]མ་ཡིན་ཏེ་འོན་ཀྱང་ལན་གསུམ་ཕྱག་བྱ་བར་རིགས་པ༌[^2120]ཡིན་ཏེ། དེའི་དོན་ཉིད་དུ་འདུས་པའི་དགེ་འདུན་ནམ་གང་ཟག་དེ་དག་ལ་ཡང་ཐལ་མོ་སྦྱར་བར༌[^2121]བྱེད་པའི་གང་ཟག་དེས་ཐལ་མོ་སྦྱོར་བ་ཉིད་དུ་རིགས་པ་ཡིན་ནོ། །

[Block 2339]
གཅིག་པུར་འདུས་པ་དང་གཉིས་པ་ནི་སྐལ་བ་མཉམ་པར་སོན་པ་ནི་རབ་ཏུ་བརྟེན་པར༌[^2122]གྱུར་པ་དང་པོ་ཤིན་ཏུ་གྱུར་པའི་སྔོན་རོལ་དུའོ། །

[Block 2340]
འདི་བསྟན་པ་ངེས་པར་འབྱེད་པར་རིགས་པ༌[^2123]ཞེས་བྱ་བ་འདིར་དང་པོར་ཕྱག་བཙལ་བར༌[^2124]བྱེད་པ་ལ་དང་པོར་འཇུག་པར་རིགས་པ་དེའི་ཕྱིར་འདིར་དང་པོར་ལན་གསུམ་ཕྱག་བྱ་བར་གསུངས་སོ། །

[Block 2341]
དེའི་དོན་ཉིད་དུ་དང་ཉི་མ་བརྗོད་པ་ལ་ཐལ་མོ་སྦྱར་བ༌[^2125]ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཐལ་མོ་སྦྱོར་བར་བྱེད་པའི་གང་ཟག་དེའི་དོན་འདི་ལྟ་སྟེ། རབ་ཏུ་དབྱུང་བའི་ཕྱིར་ཞུ་བ་དང་། ཡང་དག་པར་བླང་བ་དང་། མཁན་པོ་ཉིད་ལ་སོགས་པར་གསོལ་བ་དང་། སྦྱིན་པ་དག་དང་བར་ཆད་དྲི་བ་དང་། བསྙེན་པར་རྫོགས་པའི་ཕྱིར་འདུ་བ་དག་བསྒྲུབ་པའི་ཕྱིར་དགེ་འདུན་ནམ་གང་ཟག་འདུས་པར་གྱུར་པ་དེ་ནི་དེའི་དོན་ཉིད་དུ་ཞེས་བྱ་སྟེ། ཉིན་ཞག་བྱིན་གྱིས་བརླབ་པ་དང་། གསོ་སྦྱོང་དང་དགག་དབྱེའི་དུས་བྱིན་གྱིས་བརླབ་པ་དང་། འདུན་པ་དང་ཡོངས་སུ་དག་པ་དང་དགག་དབྱེ་སྦྱིན་པ་དང་། གཅིག་ཏུ་འདུན་པ་ཡོངས་སུ་དག་པ་དང་། དགག་དབྱེ་སྦྱིན་པ་དང་། དབྱུང་བ་དག་དང་ཡོངས་སུ་གནས་པའི་དུས་འདས་པ༌[^2126]བརྗོད་པ་དང་། ཡོངས་སུ་གནས་པ་ལ་སོགས་པ་ལས་དབྱུང་བ་ལ་སོགས་པ་དེ་ལ་ཡང་དེའི་ཟླ་བའི་ངོ་བོ་འདིའི་ཉི་མའི་འདིའོ་ཞེས་བརྗོད་པ༌[^2127]དག་སྟེ། དེ་ལ་ཡང་ཐལ་མོ་སྦྱར་བ་ཉིད་དུ་རིགས་པ༌[^2128]ཡིན་ནོ། །

[Block 2342]
གལ་ཏེ་གང་ཟག་གིས་རང་གི་དོན་དུ་བརྗོད་ན་གསོལ་བ་བཏབ་པས་མཇུག་ཏུ་ཐབས་ཡིན་ནོ་ཞེས་སོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་གང་ཟག་གིས་རང་གི༌[^2129]དོན་ཙམ་སྒྲུབ་པའི་ཕྱིར་བརྗོད་ན་གསོལ་བ་གང་བཏབ་པའི་གང་ཟག་གིས་དེ༌[^2130]སྔགས་བརྗོད་དུ་བཅུག་པའི་མཇུག་ཏུ་ཐབས་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 2343]
ཐབས་ལས་བྱུང་བའི་ཐབས་ཡིན་ཏེ། ཁྱོད་ཀྱིས་འདུལ་བ་ལ་སོགས་པ་ཉིད་ཀྱི༌[^2131]ཕྱིར་རང་གི་དོན་ལ་ཨེ་ཀཎ་ནོ། །

[Block 2344]
དེ་ལྟར་བྱས་ན་དོན་དེ་སྒྲུབ་པའི་ཐབས༌[^2132]ཡིན་ནོ་ཞེས་བྱ་བའི༌[^2133]དོན་ཏོ། །

[Block 2345]
དེའི་རྗེས་ལ་ཅིག་ཤོས་ཀྱིས་ལེགས་སོ་ཞེས་བྱ་བ་ནི་གསོལ་བ་བཏབ་པའི་གང་ཟག་དེས་ཐབས་ཡིན་ནོ་ཞེས་བརྗོད་པ་དེའི་རྗེས་སུ་གསོལ་བ་འདེབས་པའི་གང་ཟག་ཅིག་ཤོས་ཀྱིས་ལེགས་སོ་ཞེས་བྱ་བ་སྟེ། ཐབས་ཡིན་ནོ་ཞེས་གང་སྨྲས་པ་དེ༌[^2134]ལེགས་ཏེ། དེ་ནི་ཐབས་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏེ། འདུན་པ་དང་ཞེ་སྡང་དང་གཏི་མུག་དང་འཇིགས་པས་འགྲོ་བ་དང་བྲལ་བ་བྱས་པ་དང་མ་བྱས་པ་དྲན་པར་ནུས་པར་སྤྲོ་བར་བྱ་སྟེ་བསྐོའོ་ཞེས་བྱ་བ་ནི། དེ་ལྟ་བུའི་བྱ་བ་དེ་རྣམས་ལ་དེས་ཞེས་བྱ་བ་སྟེ། སྤྲོ་བས་བྱས་པ་ཡིན་གྱི། སྤྲོ་བ་མ་བྱས་པར་ནི་མ་ཡིན་ནོ། །

[Block 2346]
བྱས་པ་ཉིད་ནི་གནས་པར༌[^2135]བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ལས་ལ་རབ་ཏུ་གནས་པ༌[^2136]ཉིད་ཅེས་བྱ་བ་ལས་བྱེད་པ་པོ་མ་ཡིན་པས་བྱས་པ་ཉིད་འདི་ལ་རིག་པར་བྱའོ། །

[Block 2347]
དཔེར་ན་དགེ་འདུན་གྱིས་བཟོད་ཅིང་གནང་ནས་དགེ་འདུན་མིང་འདི་ཞེས་བགྱི་བ་དགེ་སློང་རུང་བ་ལ་འཆགས་པའི༌[^2137]གཞི་བསྟན་པ་སྦྱིན་པ་སྟེ། གང་གི་ཚེ༌[^2138]འདི་ལྟར༌[^2139]ཅང་མི་གསུང་བས༌[^2140]དེ་དེ་བཞིན་དུ་འཛིན་ཏོ་ཞེས་གསུངས་པ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2348]
གསོལ་བ་ནི་གོ་བར་བྱ་བ་ཙམ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2349]
འདི་ལ་བྱེད་པ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་གསོལ་བ་དང་བཞིའི་ལས་ལ་དེ་ཐལ་བ་མ་ཡིན་ནོ། །

[Block 2350]
མཚམས་གཅོད་པ་ཉིད་ནི་གཅད་པ༌[^2141]དང་འདྲ་བ་ཉིད་དུ་ཤེས་པར་བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་མཚམས་གཅོད་པ་ཉིད་ཅེས་བྱ་བ་ནི་མཚམས་མ༌[^2142]མནན་པར་དགེ་འདུན་གནས་པ་ལ་མཚམས་བཅད་པ་ཉིད་འགྲུབ་པ་མ་ཡིན་ཏེ། དེ་བཞིན་དུ་བཅད་པར་གྱུར་པ་ཉིད་ཀྱང་མི་འགྲུབ་སྟེ། འདི་ལྟར་མཚམས་གཅད་པར༌[^2143]འདོད་པ༌[^2144]ངོས་དེ་དང་ཉེ་བའི་ཕྱོགས་དེ་ན་གནས་པའི་དགེ་འདུན་གྱི་ཆའི་ཕྱོགས་དེར་ཡང་བཅད་པར་མི་འགྱུར་རོ། །
--- END BLOCKS ---
