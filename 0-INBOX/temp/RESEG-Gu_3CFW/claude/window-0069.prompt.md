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
[Block 2416]
གསོ་སྦྱོང་བགྱིད་པར༌[^2197]བརྗོད་པར་བགྱིའམ། བཀའ་སྩལ་པ་བྱས་པར༌[^2198]བགྱིའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2417]
འདིར་སྨྱོན་པ་ནི་དཔེ་ཙམ༌[^2199]དུ་ཟད་དེ་དེས་ན་རང་བཞིན་དུ་ཉམས་པ་ཐམས་ཅད་འཕངས་པ་ཡིན་ཏེ་དོན་དྲན་པའི་ཕྱིར་རོ། །

[Block 2418]
དབྱེན་རྗེས་སུ་སྒྲུབ་པ་ནི་གསོལ་བ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་རྒྱུ་གང་དག་གིས་གསོལ་བའི་ལས་བྱས་པ་མི་འཆགས་པ་དེ་བཞིན་དུ་རྒྱུ་དེ་དག་ཉིད་ཀྱིས་དགེ་འདུན་གྱི་དབྱེན་གྱི་སྦྱོར་བ་རྗེས་སུ་སྒྲུབ་པ་ལ་ནི་ཡང་དེ་རྣམས་ཀྱིས་ཤེས་པའི་དོན་ཏོ། །

[Block 2419]
གང་ཞིག་འདིར་ཚུལ་ཤིང་དག་ལེན་པ་དང་། འདྲིམ་པར་བྱེད་པའི་ངོ་བོ་དེའི་དོན་དུ་མདོ་འདི་བྱས་ཏེ། གཞན་ལ་གསོལ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2420]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་གནས་ནས༌[^2200]ཕྱུང་བ་དང་དགུས་དགེ་འདུན་འབྱེད་ན་དགེ་འདུན་མ་ཕྱེད་པར་བརྗོད་པར་བྱའོ། །

[Block 2421]
རྐུ་ཐབས་སུ་གནས་པ་དང་དགུས་དགེ་འདུན་འབྱེད་ན་དགེ་འདུན་མ་ཕྱེད་པར་བརྗོད་པར་བྱའོ། །

[Block 2422]
མཚན་གཉིས་པས་ཚུལ་ཤིང་ལེན་ཏམ།[^2201] རྗེས་སུ་སྒྲོགས༌[^2202]ན་དགེ་འདུན་བྱེ་བར་བརྗོད་པར་བགྱིའམ། དགེ་འདུན་མ་བྱེ༌[^2203]བར་བརྗོད་པར་བགྱི། བཀའ་སྩལ་པ། དགེ་འདུན་མ་བྱེ་བར་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2423]
འདི་ལ་མཚན་མི་མཐུན་པ་ཉིད་ནི་ཡན་ལག་མ་ཡིན་ནོ། །

[Block 2424]
རྗེས་སུ༌[^2204]ཞེས་བྱ་བ་ནི་དབྱེན་རྗེས་སུ་སྒྲུབ་པ་འདི་ལ་ཕོ་རྣམས་ལ་ནི་མོ་ཉིད་ཡན་ལག་མ་ཡིན་ལ། མོ་རྣམས་ལ་ཡང་ཕོ་ཉིད་ཡན་ལག་མ་ཡིན་ནོ། །

[Block 2425]
འདིར་གཞུང་ནི་གཏམ་གྱི་གཞི་ལས།

[Block 2426]
ཉེ་བ༌[^2205]འཁོར་དགེ་སློང་ཁོ་ནས་དགེ་སློང་གི་དགེ་འདུན་འབྱེད་པར་འགྱུར་གྱི།[^2206] དགེ་སློང་མས་ཀྱང་མི་འགྱུར། དགེ་སློབ་མས་ཀྱང་མི་འགྱུར།[^2207] དགེ་ཚུལ་གྱིས་ཀྱང་མི་འགྱུར། དགེ་ཚུལ་མས་ཀྱང་མི་འགྱུར་མོད་ཀྱི་འོན་ཀྱང་དགེ་འདུན་འབྱེད་པའི་ཕྱིར་བརྟུལ་བར་ནི་འགྱུར་རོ། །

[Block 2427]
དགེ་སློང་མ་ཁོ་ནས་དགེ་སློང་མའི་དགེ་འདུན་འབྱེད་པར་འགྱུར་གྱི། དགེ་སློང་གིས་ཀྱང་མི་འགྱུར། དགེ་སློབ༌[^2208]མས་ཀྱང་མི་འགྱུར། དགེ་ཚུལ་མས་ཀྱང་མི་འགྱུར་མོད་ཀྱི། འོན་ཀྱང་དགེ་འདུན་འབྱེད་པའི་ཕྱིར་བརྟུལ་བར་ནི༌[^2209]འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2428]
བཞད་གད་ཀྱི་དངོས་པོས་ནི་གང་གིར་ཡང་མི་འགྱུར་རོ་ཞེས་བྱ་བ་ནི། བཞད་གད་ཀྱི་དངོས་པོས་ཞེས་བྱ་བ་ནི་ཀུ༌[^2210]རེའི་བསམ་པས་ཁས་ལེན་པར་བྱེད་ཅིང་ལས་ཐམས་ཅད་ནི་གང་གི་ཡང་ཡན་ལག་དུ་མི་འགྱུར་ཏེ། བསམ་པའི་དབང་གིས་གནས་པ་ལྡང་བ་ཡིན་གྱི། ལས་གནས་པ་ལ་ལྟོས་པའི་བསམ་པས་ནི་འདིར་མ་ཡིན་ནོ། །

[Block 2429]
འདིར་གཞུང་ནི་དབྱེན་གྱི་སྐབས༌[^2211]སུ་དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 2430]
གང་གི་ཕྱིར་དབྱེན་གྱི་བྱ་བ་ལ་བཞད༌[^2212]གད་ཀྱི༌[^2213]བསམ་པས་རྗེས་སུ་སྒྲོགས་ཤིང༌[^2214]ཚུལ་ཤིང་ལེན་དུ་གསོལ་ན་དགེ་འདུན་བྱེ་བར༌[^2215]བགྱིའམ། ཉེ་བར༌[^2216]འཁོར་མི་བྱའོ་ལས༌[^2217]བགྱིད་པ་ལ་ལྟུང་བ༌[^2218]ཅིར་འགྱུར། དབྱེན་གྱི་སྐབས་ཀྱི་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2431]
གལ་ཏེ་དགེ་འདུན་གྱིས་ཤེས་ན་དགེ་འདུན་ཐམས་ཅད་ལ་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2432]
འདིར་ཐམས་ཅད་དུ་བྱེ་བྲག་མེད་པར་ཤེས་པས་འདིར་རྗེས་སུ་ཐོབ་པའི་སྒྲས་ནི་ལས་བརྗོད་པ་ལའོ། །

[Block 2433]
མི་འཆགས་པའི་བློས་དབྱེན་བྱེད་པ་དང་གནས་ནས་འབྱིན་པ་དག་ནི་སྦོམ་པོའི༌[^2219]ཞེས་བྱ་བ་ནི་དབྱེན་གྱི་ལས་དང་གནས་ནས་དབྱུང་བའི་ལས༌[^2220]མི་འཆགས་པར་ཤེས་བཞིན་དུ་མི་འཆགས་ཀྱང་བླའི། འོན་ཀྱང་བྱའོ་སྙམ་པའི་བློས་དབྱེན་དང་གནས་ནས་དབྱུང་བའི་ལས་བྱེད་དམ། དེའི་ཡན་ལག་གི༌[^2221]དངོས་པོ་བསྒྲུབས༌[^2222]ན་ཐམས་ཅད་དུ་དབྱེན་གྱི་ཕྱོགས་ཀྱི་སྦོམ་པོར་འགྱུར་བའོ། །

[Block 2434]
དགེ་འདུན་དུ་མ༌[^2223]གྱུར་པ་ཉིད་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་ནི་གྲོགས་མེད་པ་ཉིད་དུ༌[^2224]བྱེད་པའམ། གཅིག་དང་ལྷན་ཅིག་གམ་གཉིས་དང་ལྷན་ཅིག་ཏུ་དབྱེན་དང་གནས་ནས་འབྱིན་པ་དག་བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 2435]
འདི་ནི་རྩེད་མོའི་རྣམ་པ་ཡིན་གྱི་རྗེས་སུ་བསྒྲུབ་པའི་རྣམ་པ་ནི་མ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 2436]
འདིར་གཞུང་ནི་གཅིག་གིས་གཅིག་གནས༌[^2225]ནས་འབྱིན་ན་ཉེས་བྱས་སོ། །

[Block 2437]
གཅིག་གིས་གཉིས་སམ་གཅིག་གིས་མང་པོའམ་གཉིས་ཀྱིས་བཞིའམ། གཉིས་ཀྱིས་གཅིག་གམ། མང་པོས་མང་པོ་འམ་མང་པོས་བཞིའམ། མང་པོས་གཅིག་གམ། མང་པོས་གཉིས་གནས་ནས་འབྱིན་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས༌[^2226]གསུངས་པ་ཡིན་ནོ། །

[Block 2438]
ཐ་དད་པར་གནས་པ་དག་ལས་གཞན་པ་ཁ་སྐོང་བར་འོས་པ་མ་ཡིན་པ་དག་གིས་ཚོགས་ཀྱིས༌[^2227]གསོལ་བ་དང་བརྗོད་པ་དག་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། བྱས་པ་ཉིད་ལ་བྱས་པ་ཉིད་དོར་ནས་གནས༌[^2228]ཐ་དད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2439]
འདི་ལྟར་ཁ་སྐོང་བར་འོས་པ་མ་ཡིན་པ་ཐམས་ཅད་ཀྱང་རྣམ་གྲངས་ཀྱིས་ཐ་དད་པར་གནས་པ་ཡིན་ནོ། །

[Block 2440]
དེ་ལྟ་བས་ན་གནས་པ་ཐ་དད་པར་གནས་པ་ཉིད་དང་གང་དག་རང་བཞིན་དུ་མི་གནས་པ་ཉིད་ནི་གཞན་མ་ཡིན་ནོ། །

[Block 2441]
དེ་རྣམས་ལ་དེ་ལེན་པར་རྟོགས་པར་བྱའོ། །

[Block 2442]
ཡང་དེ་རྣམས་ནི་ཆོས་མ་ཡིན་པའི་ཕྱོགས་ཁས་བླངས་པ་འདི་ཐོབ་པ་རྣམས་ལ་དེ་རྣམས་ཡང་ཁས་བླངས་པས༌[^2229]ཐ་དད་པ་ཉིད་ཡིན་པས་ཐ་དད་པ་ཉིད་དུ་རིག་པར༌[^2230]བྱའོ། །

[Block 2443]
བསྙེན་པར་རྫོགས་པ་དང་བཅས་པ་མ་ཉམས་པ་རྣམས་ཀྱིས་བསླབ་པ༌[^2231]ལ་གུས་པར་བྱ་དགོས་ལ༌[^2232]གསོ་སྦྱོང་དང་དགག་དབྱེ་དག་བྱ་བ་གང་ཡིན་པ་དེ་ནི་བསླབ་པའི་ཡན་ལག་དང་། བསླབ་པ་རྗེས་སུ་སྐྱོང་བར་འགྱུར་བ་དག་ཡིན་པ་དེའི་ཕྱིར་ཁ་སྐོང་བར་འོས་པ༌[^2233]མ་ཡིན་པས༌[^2234]གསོ་སྦྱོང་དང་དགག་དབྱེ་དག་བྱས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2444]
རང་གི་འོས་པའི་དགེ་འདུན་ཉམས་སུ་མྱོང་བ་མ་གྲུབ་པ་ཉིད་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ལས་དེ་ལ་རང་གི་འོས་པའི་དགེ་འདུན་བཞིའི་ཚོགས་ལ་སོགས་པའི་དགེ་འདུན་གང་ཡིན་པ་དེ་ལས་ཉམས་སུ་མྱོང་བ་མ་གྲུབ་པ༌[^2235]ཉིད་ན་ལས་དེ་བྱས་པ་ཉིད་མ་ཡིན་ཏེ་ལས་མ་གྲུབ་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2445]
གསོལ་བ་ཐོས་ན་དེ༌[^2236]གྲུབ་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། དགེ་འདུན་དང་ཉན་དུ་གཞུག་པ་བསྙེན་པར་རྫོགས་པར་བྱ་བ་ལ་སོགས་པས་གསོལ་བ་ཙམ་ཐོས་ན་ཡང་ཉམས་སུ་མྱོང་བ་དེ་འགྲུབ་པ་ཉིད་ཡིན་ཏེ། དེ་ཙམ་ཐོས་པས་ལས་དེ་བྱས་པ་ཉིད་ཡིན་ནོ། །

[Block 2446]
སྐལ་བ་དང་ལྡན་པའི་རང་བཞིན་ཅན་ལ་མ་དག་པ་འདྲ་བས་རབ་ཏུ་འབྱིན་དུ་གཞུག་པ་ནི་ཆོ་ག་མ་ཡིན་པ་མ་ཡིན༌[^2237]ནོ་ཞེས་བྱ་བ་ནི་གང་ཞིག །སྐལ་བ་དང་ལྡན་པའི་རང་བཞིན་ཅན་གྱི་གང་ཟག་གང་ཡིན་པ་ཁྱིམ་ནས་འབྱུང་བའི་སྐབས་མི་རྙེད་ན། དེ་ལ་མངགས་པ་དང་འདྲ་བས་རབ་ཏུ་འབྱིན་དུ་གཞུག་པ་གང་ཡིན་པ་དེ་ནི་ཆོ་ག་མ་ཡིན་པ་མ་ཡིན་ཏེ། ཆོ་ག་ཡིན་པ་ཁོ་ནར་བལྟ་བར་བྱ་བ་ཞེས་བྱ་བའི༌[^2238]དོན་ཏོ། །

[Block 2447]
འདིར་གཞུང་ནི་དེ་བས་ན་དེ་ལྟ་བུའི་མངགས་པས་བསྙེན་པར་རྫོགས་པར་བྱའོ། །

[Block 2448]
བསྙེན་པར་རྫོགས་པར་མི་བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པའི་སྐབས་ཀྱི་ཆོས་བྱིན་གྱིས༌[^2239]སྐབས་རྗེས་སུ་གནང་བ་དང་ཚུལ་ཡང་གསུངས་སོ། །

[Block 2449]
མངགས་པ་དེས་དེའི་སྐབས་རྗེས་སུ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེས་དེར་སོང་ནས་དེ་ལ་འདི་ལྟར་མངགས་པའི་ལས་ཀྱིས་བསླབ་པ༌[^2240]སྦྱིན་པ་དེ་ནི་སློབ་དཔོན་དང་འདྲ་བས་མངགས་པའི་ལས་ཞེས་བྱ་བ་བརྗོད་པར་བྱའོ། །

[Block 2450]
བུད་མེད་ལ་ནི་བུད་མེད་དང་སྐྱེས་པས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་རབ་ཏུ་དབྱུང་བར༌[^2241]བྱ་བ་བུད་མེད་ལ་ནི་མངགས་པ་བུད་མེད་ཀྱིས་ཀྱང་བྱར་རུང་སྐྱེས་པས་ཀྱང་བྱར་རུང་ངོ་། །སྐྱེས་པ་ལ་ནི་སྐྱེས་པ་ཁོ་ནས་སོ་ཞེས་བྱ་བས་ནི་བུད་མེད་ཀྱིས་མི་བྱ་སྟེ་མཐུ་དང་ལྡན་པའི་ཡུལ་ལ་དམན་པ་དབང་མེད་པའི་སྐྱེས་པ་བདག་པོར་གྱུར་པ་སྟེ། དེ་ཡང་འདི་ལ་ཡོད་པས་སྐྱེས་པའི་བྱ་བ་དག་ལ་བུད་མེད་ཀྱི་ཡིད་ཀྱིས་བྱ་བ་མི་རིགས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2451]
དེ་ལ་མངགས་པས་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གསོལ་བ་དང་ཁས་བླངས་པ་དག་དེའི་མིང་ཁོ་ནས་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མིང་འདི་ཞེས་བྱ་བ་དེ་རབ་ཏུ་དབྱུང་བར་གསོལ་ལོ་ཞེས། དེའི་མིང་ཉིད་ཀྱིས་རབ་ཏུ་འབྱུང་བ་ཡང་དག་པར་ལེན་ཏོ་ཞེས་དེ་ལྟར་དེའི་མིང་གིས་བྱའོ། །

[Block 2452]
དེའི་མིང་ནས་མ་སྨོས་པར༌[^2242]རབ་ཏུ་དབྱུང་བ་ཞུ་བ་ཡང་མངགས་པས་མི་བྱ་བའི་ཕྱིར་བརྗོད་པ་ཡང་རབ་ཏུ་བྱུང་བ་ཞེས་སྨོས་པས་འཕངས་པ་ཉིད་ཡིན་ནོ། །

[Block 2453]
བསྙེན་པར་རྫོགས་པ་མན་ཆད་གོང་མ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་མན་ཆད་ཀྱི་སྒྲས་དབྲི་བའོ། །

[Block 2454]
རབ་ཏུ་བྱུང་བའི་གོང་མ་བསྙེན་པར་རྫོགས་པ༌[^2243]མན་ཆད་ཀྱང་སྐལ་བ་དང་ལྡན་པའི་རང་བཞིན་ཅན་ལ་མངགས་པ༌[^2244]དང་འདྲ་བས་གང་བྱ་བ་དེ་མི་རིགས་པ་མ་ཡིན་ཏེ། རིགས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 2455]
འདིར་གོང་མ་ཞེས་བྱ་བ་ཡིན་ཏེ། སྔར་རབ་ཏུ་བྱུང་བ་དེ༌[^2245]སྨོས་པས་དགེ་ཚུལ་གྱི་སྡོམ་པ་སྦྱིན་པ་བསྟན་པ་དང་། གོང་མ་དགེ་ཚུལ་མའི་སྡོམ་པ་སྦྱིན་པ་དང་། བར་སློབ་མའི་སྡོམ་པ་སྦྱིན་པ་དང་། ཚངས་པར་སྤྱོད་པ་ལ་ཉེ་བར་གནས་པའི་སྡོམ་པ་སྦྱིན་པ་དང་། བསྙེན་པར་རྫོགས་པར་བྱ་བ་དག་གོ། །
--- END BLOCKS ---
