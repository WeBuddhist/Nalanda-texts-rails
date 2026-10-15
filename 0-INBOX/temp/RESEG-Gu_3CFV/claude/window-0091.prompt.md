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
[Block 3186]
ཁྱིམ་པ་མོའི་བཟོ་སྟོན་པའི་ལྟུང་བྱེད་གསུམ་པ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་རྗེན་པ་འཚོད་པའིའོ༌[^2044]ཞེས་བྱ་བ་སྨོས་ཏེ། མི་སྙི་བ་རྣམས་ཀྱི་སུམ་ཆ་བངས་པ་ཉིད་ཀྱི་མདུན་རོལ་དུ་དེ་ཉིད་ཡིན་ཏེ་མ༌[^2045]ཚོས་པའི་ཕྱིར་རོ། །

[Block 3187]
སྙི་བ་རྣམས་ཀྱི་ཁ་དོག་གྱུར་པའིའོ།[^2046] །ཁུ་བ་རྣམས་ཀྱི་ནི་ལན་གཉིས་ཁོལ་བར་གྱུར་པའིའོ་ཞེས་སྨོས་པ་ཡིན་ཏེ། འདི་རྗེན་པ་ཉིད་ཀྱི་ཕྱིར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3188]
གང་ཡང་རུང་བ་ལ་དེ་བཏགས་པའི་དབང་གིས་མེ་ལས་ཁྱད་པར་བསྒྲུབ་པ་ཉིད་ལ་འཚོད་པ༌[^2047]ལས་སྐྱེས་པ་ཉིད་རྩོམ་པ་གཅིག་པར་གྱུར་པ་ཉིད་ཀྱིས་ཆ་གཞན་དེར་ཞུགས་པའོ།[^2048] །བཏགས་པ༌[^2049]ལ་ནི་སྦྱོར་བ་ཉིད་དེ་སྔ་མ་ལ་དེ་སྦྱོར་བ་མ་ཡིན་པའི་སྦྱོར་བ་ཉིད་དོ། །

[Block 3189]
དགེ་སློང་གི་དགེ་འདུན་དང་། མཁན་པོ་དང་། སློབ་དཔོན་དང་། ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་རྣམས་ཀྱི་ཕྱིར་དབེན་པའི་ཕྱོགས་སུ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་ཚིག་ནི། སློབ་དཔོན་གང་ལ་ངེས་པ་ཉེ་བར་གཞག་པར་བྱ་བ་ཉིད་ནི་དེའམ་གཞན་ལ་ཡང་ངོ་། །ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི། རྣམ་པ་འདི་ལ་མངོན་པར་བརྟེན་ནས་འདིར་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་དང་བཅས་པ་ཉིད་ཀྱི་ཚིག་གིས་བཟུང་བ་བསྒྲུབ་པ་ཡོད་པ་ལ་ཐ་དད་པའི་ཞེས་སྨོས་སོ། །

[Block 3190]
དེ་བས་ན་འདི་ནི་མཚོན་པ་ཙམ་ཡིན་ཏེ། སློབ་དཔོན་ཡང་འདིས༌[^2050]འཕངས་པ་ཉིད་ཡིན་ནོ། །

[Block 3191]
འདིར་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་ཞེས་སྨོས་པས་ནི་ཆོས་འདི་པའི་རབ་ཏུ་བྱུང་བ་ཉིད་དང་། སློབ་དཔོན་སྨོས་པས་རབ་ཏུ་བྱུང་བ་བསྡུས་པར་རྣམ་པར་གནས་པ་ཡིན་ཏེ། ཁྱིམ་པ་རྣམས་ལ་མ་ཡིན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3192]
ཕྱིར་ཞེས་བྱ་བ་ནི་འཚོད་པ༌[^2051]ཉིད་ལ་ཆོས་དང་ལྡན་པའི་དོན་གྱི་དབང་གིས་འཚོད་པ༌[^2052]ལ་ནི་ལྟུང་བ་མེད་པར་རིག་པར་བྱའོ། །

[Block 3193]
ཁྱིམ་པ་མོའི་བཟོ་སྟོན་པའི་ལྟུང་བྱེད་གསུམ་མོ།། །།

[Block 3194]
གང་ལ་ལྟོ་འདུན་ལས་གྱུར་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར༌[^2053]ཟས་ཟོས་ནས༌[^2054]སྟན་ལས་ལངས་ཏེ་ཡང་ཟ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གནས་བཏང་བར་བྱས་ནས་བཟའ་བར་བྱ་བ་གང་ཡང་རུང་བ་ཟོས་པ་ལ་ལྟུང་བྱེད་འདི་ལྷག་པོར་མ་བྱས་པ་ཟ་བའི་ལྟུང་བྱེད་དུ་རྣམ་པར་གཞག་པ་མ་ཡིན་པ་སྟེ། འོན་ཀྱང་འདི་ནི་ཟས་གཅིག་ཁོ་ན་ལ་ཉེ་བར་བཏགས་པའི་བཟའ་བར་བྱ་བ་ཟ་བ་དང་ལྡན་པ་ཉིད་ཡོད་པ་ལ་ལྷག་པོར་མ་བྱས་པར་སྟན་ལས་ལངས་ཏེ་ཡང་ཟ་བ་ལ་ལྟུང་བ་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 3195]
ངེས་པར་བྱས་པ་ཞེས་བྱ་བ་ལྟུང་བྱེད་གཉིས་སོ། །

[Block 3196]
དེ་ཉིད་ལ་སྤངས་ཤིང་ལྷག་པོར་མ་བྱས་པར་ཟ་ན་ནི་ལྟུང་བ་འདི་ཡིན་པ་དེ་བས་ན། ཟ་བ་གཅིག་པ་ཉིད་ཀྱིས་ཉེ་བར་བརྟགས་པ༌[^2055]ལས་ལངས་ཤིང་ལངས་ཏེ། ཡང་ཡང་ཟ་བ་དེ༌[^2056]ཉིད་ལྟོ་འདུན་ལས་གྱུར་པའི་ལྟུང་བྱེད་དོ། །

[Block 3197]
དེ་ལྟར་འདིར་གླེང་གཞི་ལས།

[Block 3198]
དགེ་སློང་མ་སྦོམ་དགའ་མོ་ནང་པར་སྔར་ལངས་ཏེ། བསོད་སྙོམས་བླངས་ནས་རང་གི་ཉེན་འཁོར༌[^2057]དུ་གཞག་སྟེ། ལྷུང་བཟེད་ཡང་བླངས་ཡང་བླངས་ཡང་ཟོས་ཡང་ཟོས་ཤིང་འཆག་པར༌[^2058]བྱེད་ཅིང་། བཅགས་ནས་ཡང་ཟ་བར་བྱེད་དོ། །

[Block 3199]
ཡང་འཆག་པར༌[^2059]བྱེད་ཡང་ཟ་བར་བྱེད་ཅིང་དྲོའི་བར་དུ་མ་སྤངས་པར་དེ་ལྟར་བྱེད་པ་ལས་བཅས་པ་ཡིན་ཏེ། སྐྱེས་པ་ནི་ལྟོ་འདུན་ལས་གྱུར་པའི་གདུངས་པ༌[^2060]དང་། བརྐམ་ཆགས༌[^2061]ཆུང་བ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3200]
དགེ་སློང་ལ་ནི་ལྷག་པོར་མ་བྱས་ཤིང་ཟ་བ༌[^2062]གཅིག་པ་ཉིད་ཀྱིས་ཉེ་བར་བརྟགས་པ་ལ་སྟན་ལས་ལངས་ནས་ཡང་དང་ཡང་དུ་ཟ་བ་ན་ཉེས་བྱས་སོ། །

[Block 3201]
ལྟོ་འདུན་ལས་གྱུར་པའི་ལྟུང་བྱེད་དོ། །

[Block 3202]
གང་ལ་ཚོགས་པར༌[^2063]དབྱུང་བ་མ་ཡིན་པའི་དྲི་བསྟན་པའི༌[^2064]ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྒོག་སྐྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟ་བ་ལའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3203]
དེ་དག་ཅི་ཙམ་ལ་ཡང་རུང་སྟེ་ཞེས་བྱ་བ་བྱེ་བྲག་མ་སྨོས་པས༌[^2065]རྟོགས་པར་བྱའོ། །

[Block 3204]
ན་བའི་ཕྱིར་ནི་ལྟུང་བ་མེད་དོ། །

[Block 3205]
བཙོང་དང་སྒོག་སྐྱ་དག་ལ་བྱེ་བྲག་སྨོས་པས་ཇི་ལྟར་ཐོབ་པའི་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 3206]
ཀུན་དོང་ཀེའུ་དག་ཟ་བ་ལ་ནི་དྲི་ཆུང་བའི་ཕྱིར་ཉེས་བྱས་སོ། །

[Block 3207]
ཚོགས་པར་དབྱུང་བ་མ་ཡིན་པའི་དྲི་བསྟན་པའི༌[^2066]ལྟུང་བྱེད་དོ།། །།

[Block 3208]
ད་འདི་མན་ཆད་དུ་ནི་བསུ༌[^2067]བེལ་བ་ལས་གྱུར་པའི་ལྟུང་བྱེད་གསུམ་སྟོན་ཏེ། དེ་རྣམས་ཀྱི་དང་པོ་བསྟན་པ་དེའི་ཕྱིར། རྨེ་གབ་མི་འཆང་བ༌[^2068]ལའོ་ཞེས་སྨོས་ཏེ། ལོངས་སྤྱོད་པར་བྱེད་པ་སྣང་དུ་རུང་བའི་གོས་ངན་པ་མི་འདོག་པ༌[^2069]བསལ་བའི་ཕྱིར་འདི་ཡིན་ཏེ། བསུ་བེལ་བ་ཞེས་བྱ་བ་ནི་གོས་མ་རུངས་པར་གྱུར་པ༌[^2070]དེ་གཞན་དག་གིས་ཚོར་བ་ལ་བྱའོ། །

[Block 3209]
དེ་བས་ན་དེ་ལྟ་བུར་གྱུར་པའི་ལུས་འོག་མའི་གོས་སྤང་བར༌[^2071]བྱ༌[^2072]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3210]
ཇི་ལྟར་བརྗོད་པའི་ཉེས་པ་ཡོངས་སུ་སྤང་བའི༌[^2073]དོན་དུ་རྨེ་གབ་བཅང་བར་བྱའོ། །

[Block 3211]
སྐྱེ་གནས་ཀྱི་སྒོར་འདི་མ་བརྟགས་པ་ཉིད་ལ་ལྟུང་བྱེད་དོ། །

[Block 3212]
དེ་ཐིག་གུས༌[^2074]བཏགས་ཏེ་བཞག་གོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་རྨེ་གབ་དེའོ། །

[Block 3213]
མདོ་དེ་གཉིས་ཀྱི༌[^2075]ལུང་ནི་ཕྲན་ཚེགས་དག་ལས་ཁ་བསྒྱུར་བར་བྱའོ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3214]
དེ་དུས་དུས་སུ་བཀྲུ་བ་དང་ཁ་བསྒྱུར་བར་བྱའོ་ཞེས་བྱ་བ་ནི། རྨེ་གབ་དེ་ཞེས་བྱ་བར་སྦྱར༌[^2076]རོ། །

[Block 3215]
གང་ལ་བསླབ་པའི་གཞི་གཉིས་པ་དེ་བརྗོད་པར་བྱ་སྟེ། ཆུ༌[^2077]གོས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། ཀྱང་གི་སྒྲ་ནི་མི་འཆང་བ་ལའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3216]
གང་གི་ཚེ་ལུས་གཤེར་བར་གྱུར་པ་དེའི་ཚེ། གང་གིས༌[^2078]ཆུ་གོས་མི་འཆང་མི་གོན་ཞིང་དེ་ལ༌[^2079]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3217]
མདོམས༌[^2080]ཀྱི་སྤུ་མན་ཆད་ནས། པུས་མོའི་ལྷ་ང་ཡན་ཆད་ཀྱི་ཕྱོགས་མི་འགེབས་པ་ལ་དངོས་གཞིའོ། །

[Block 3218]
གཞན་གཉའ་བ་མན་ཆད་ནས་ལོང༌[^2081]བུ་ཡན་ཆད་ཀྱི་ལུས་མགྲིན་པའི་བར་དུ་ལུས་ཀྱི་ཕྱོགས་མི་འགེབས་པ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 3219]
འདིར་གླེང་གཞི་ལས་དགེ་སློང་མ་རབ་ཏུ་མང་པོ་དག་བུད་མེད་ཁྱིམ་པ་མོ་དག་དང་ལྷན་ཅིག་ཏུ་ཆུ་ཀླུང་གནས་ཅན་གྱི་ནང་དུ་ཁྲུས་བྱེད་ཅིང་དེ་དག་ཁྲུས་བྱེད་པ་ན་བུད་མེད་དག་མཛུབ་མོས་སྟོན་ཅིང་རབ་ཏུ་བྱུང་བ་མོ་ཆེ་གེ་མོ་དག་གི་ནུ་མ་གཉིས་ནི་འདི་འདྲའོ། །

[Block 3220]
ཆེ་གེ་མོ་ཞིག་གི་ལྟོ་བ་ནི་སྤྱང་ཁྱི་འདྲའོ། །

[Block 3221]
ཆེ་གེ་མོ་ཞིག་གི་རྐེད་པ་ནི་སྦོམ་མོ། །

[Block 3222]
ཆེ་གེ་མོ་ཞིག་གི་བརླ་ནི་གླང་པོ་ཆེའི་སྣ་འདྲའོ་ཞེས་ལུས་ཀྱི་ཡན་ལག་དང་གསང་བའི་ཕྱོགས་དག་གི༌[^2082]བརྗོད་པ་རྣམ་པ་མང་པོས་བསྙད་འདོགས་པ་ལས་འདི་བཅས་པ་ཡིན་ནོ། །

[Block 3223]
འདིས་ནི་རོ་སྟོད་མ་གཡོགས་པའི་ཁ་ན་མ་ཐོ་བ་ཉིད་དུ་ཤེས་པར་བྱ་སྟེ་ཞེས་བྱ་བ་འདིས་ཤེས་པར་བྱའོ། །

[Block 3224]
ཆུ་གོས་དང་ཁྲུས་རས་ཞེས་བྱ་བ་འདིའི་རྣམ་པར་འབྱེད་པ་ལས་སོ། །

[Block 3225]
ཆུ་གོས་འདི་དུས་ཐམས་ཅད་དུ་ཕྱི་རོལ་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །
--- END BLOCKS ---
