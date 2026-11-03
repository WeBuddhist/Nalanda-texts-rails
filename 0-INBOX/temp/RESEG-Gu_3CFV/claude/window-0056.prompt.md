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
[Block 1961]
མདོ་སྡེ༌[^1243]ལས་གསུངས་པ་ལ་ནི་ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་ཡང་མངོན་པར་ཤེས་པ་ཉིད་ལ་ཞེས་བྱ་བ་འདིའི༌[^1244]མཐར་བསླབ་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྗོད་པར་གྱུར་པ་ལ་ཇི་སྲིད་དུ་ཚིག་བརྗོད་པ་ལ་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1962]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས།

[Block 1963]
[^1245] འདུལ་བ་དང་ལྡན་པ་དག་མ་གཏོགས་པ་མདོ་སྡེ་དག་ལས་འདི་སྐད་ཅེས་ཁོ་བོ་འདི་ལ་མི་སློབ་པོ་ཞེས་ཟེར་ན་ཉེས་བྱས་སོ། །

[Block 1964]
གཞན་མདོ་སྡེ་ཉིད་བཞག་པ་འདི་ལས་མངོན་པར་བརྟེན་པ་ཤེས་པ་ཡིན་ནོ། །

[Block 1965]
བསླབ་པ་ལ་ཉེ་བར་འཇོག་པ་སྤང་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1966]
ཅི་ཞིག་བྱས་ན་འཇུག་པ་གང་ལ་ཉན་རྣ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་དག་རྩོད་པར་གྱུར་པ་དགེ་སློང་དག་དང་གྲོས་བྱེད་པ་ན་ཉན་པའི་ཕྱིར་རྣ་གཏོད་ན་སྟེ་ཉེ་བར་ཞི་བར་འདོད་པས་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡུལ་གྱི་དོན་གཅིག་ལ་བརྟེན་པའི་རྒོལ་བ་དང་ཕྱིར་རྒོལ་བ་དག་མང་པོ་ཞིག་ཡོད་མོད་ཀྱི། འོན་ཀྱང་རིགས་གཉིས་ཡིན་པའི་ཕྱིར་དགེ་སློང་དག་ཅེས་གཉིས་ཀྱི་ཚིག་ཏུ་བྱས་སོ། །

[Block 1967]
རྒོལ་བ་དང་ཕྱིར་རྒོལ་བའི་དགེ་སློང་གང་ཡིན་པ་དེ་དག་ལ་དགེ་སློང་རྣམས་ཀྱིས༌[^1246]སྡུམ་པ་གང་ཡིན་པ་དེ་ལ་རྣ་གཏོད་པའི་དོན་དུ་རྩེ་གཅིག་ཏུ་བྱེད༌[^1247]པའོ། །ཅི་རྣ་གཏོད་པ་ཐམས་ཅད་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཉེ་བར་ཞི་བར་འདོད་པས་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྣ་གཏོད་ཅིང་ཉན་པ་དོར་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1968]
འདིར་གང་ལ་ཁ་ན་མ་ཐོ་བ་ཇི་ལྟ་བུར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྒྲ་ཐོས་པ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 1969]
དོན་ལ་ནི༌[^1248]དངོས་གཞིའོ་ཞེས་བྱ་བ་ནི་སྒྲའི་དོན་གོ་ནས་དོན་སོ་སོར་རིག་པའོ། །

[Block 1970]
དེ་བས་ན་འདིར་སྦྱོར་བ་ཐོབ་པ་ནི་སྒྲ་སོ་སོར་རིག་པ་དང་འབྲེལ་པ་སྟེ། དངོས་གཞིའི་ལྟུང་བ་ན་སྨད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1971]
ཅི་དོན་གང་ཡང་རུང་བ་ཁོ་ནས་དངོས་གཞིར་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་འཁྲུག་ལོང་བྱ་བ་ལ། གཞོལ་བས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དོན་གཞན་གྱི་དབང་ཉིད་དུ་སོན་ཅིང་ཤེས་པའི་འོག་ཏུ་རྐང་པ་དང་སེ་གོལ་དང་ལུད་པའི་སྒྲ་དག་གིས་གོ་བར་མི་བྱེད་ན་ངེས་པར་ལྟུང་བ་འབྱིན་པ་ཉིད་དུ་འགྱུར་ཏེ། གལ་ཏེ་ནོར་བ་དང་ཞི་བར་འདོད་པ་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉེ་བར་ཐོས་པ་ལས་དོན་གཞན་མངོན་དུ་བྱས་ཏེ་ཉེ་བར་འབྲེལ་པར་བྱའོ། །

[Block 1972]
དུས་གང་གི་ཚེ་ན་ཤེས་པར་འགྱུར་བ་ཅུང་ཟད་འདིར་བསྡད་པར་བྱ་སྟེ། ད་ལྟར༌[^1249]ཤེས་པའི་འོག་ཏུ་རྐང་པའི་ཏིང༌[^1250]སྒྲ་ལ་སོགས་པས་བསྡད་པར་བྱའོ། །

[Block 1973]
གལ་ཏེ་མ་ཡིན་ན་གང་ལས་ངེས་པར་ལྟུང་བར་བྱེད་པ་ལ་ལྟུང་བར་འགྱུར་བ་ནི་ལྟུང་བ་བསྐྱེད་པའོ། །

[Block 1974]
གལ་ཏེ་ནོར་བར་གྱུར་ཏམ་ཞི་བར་འདོད་པས་ནི་མ་གཏོགས་ཏེ། ཉེ་བར་མི་གནས་པར་གྱུར་པའི་ཚེ་གཅིག་པའི་སྦྱིན་པར་མི་འགྱུར་བ་ཞི་བ་ལ་དོན་དུ་གཉེར་བའམ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1975]
འཐབ་གཅུགས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་རྟེན་དུ་གྱུར་པ་ལ་ཆོ་ག་སྔ་མ་རྣམ་པར་གཞག་པའི་ཕྱིར་གཞན་ཞེས་བྱ་བའི་རྐྱེན་ཏོ། །

[Block 1976]
མི་སྟོབས་པ༌[^1251]ཉིད་ཀྱིས་ཐོབ་པ་ལ་ཚིག་འདིའོ། །

[Block 1977]
མཉན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འཐབ་མོའོ། །

[Block 1978]
དེ་བྱེད་པ་ལ་ཉེ་བར་བསྐོར་ཏེ་འདུག་པར་མི་བྱའོ། །

[Block 1979]
ཉེ་བར་ཞི་བར་བྱ་བའི་ཕྱིར་མི་འབད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི༌[^1252]རྩོད་པ་ལའོ། །

[Block 1980]
ཉན་རྣ་ལས་གྱུར་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1981]
གང་ལ་མི་སྨྲ་བར་འགྲོ་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གསོལ་བ་ལ་སོགས་པའི་ལས་ལ་འདུས་པ་དགེ་སློང་ལ་མ་སྨྲས་པར་འགྲོ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གསོལ་པ་ལ་སོགས་པའི་ལས་ལ་ཞེས་བྱ་བ་ནི་གསོལ་བ་འབའ་ཞིག་དང་གསོལ་བ་དང་གཉིས་དང་། གསོལ་བ་དང་བཞིའི་ལས་ལ་ཡང་དགག་དབྱེའི་བདག་ཉིད་ཅན་གྱི་ལས་ལའོ། །

[Block 1982]
རབ་ཏུ་བྱུང་བ་ལ་ལྟོས་པ་ཞུ་བ་ལ་སོགས་པ་ལ་ནི༌[^1253]མ་ཡིན་ནོ། །

[Block 1983]
འདུས་པ་ཞེས་བྱ་བ་ནི་ཞུགས་པ་ལའོ། །

[Block 1984]
དགེ་འདུན་འདུས་པ་ལ་མ་དྲིས་པར་རོ། །

[Block 1985]
དགེ་སློང་ལ་མ་དྲིས་པར་འགྲོ་ནའོ་ཞེས་བྱ་བ་ལ། དགེ་སློང་ལ་མ་སྨྲས་པར་ཞེས་བྱ་བ་ནི་ལྟ་བ་ཡང་དག་པར་བསྒྲུབ་པའི་དོན་དུ་མ་ཡིན་ནོ། །

[Block 1986]
འོན་ཀྱང་ཚོགས་པ་བསྒྲུབ་པའི་དོན་དུ་འདུན་པ་འབུལ་བ་ལྟར་རྟོགས་པར༌[^1254]བྱའོ། །

[Block 1987]
ཐག་ཇི་སྲིད་དུ་སོང་ན་འགྲོ་བའི་ཆ་དེ་ཁ་ན་མ་ཐོ་བ་ཅིར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཐོས་པའི་ཉེ་འཁོར་ལས་འདས་ན་དངོས་གཞིའོ། །

[Block 1988]
མདུན་རོལ་དུ་ནི་ཉེས་བྱས་སོ། །

[Block 1989]
དོན་མེད་པ་དང་མི་རིགས་པས༌[^1255]འགྲོ་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགོས་པ༌[^1256]མེད་པ་དང་མི་རིགས་པའི་ཚུལ་གྱིས་དགོས་པར༌[^1257]འགྲོ་ན་ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ།[^1258] །གསོལ་བ་བྱས་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་ནི།

[Block 1990]
འདིར་གཞུང་ནི་ལས་ཀྱི་གཞི་ཞུ་བ་ལས།

[Block 1991]
བཙུན་པ་རེ་ཞིག་ལས་བརྗོད་པར༌[^1259]བགྱིད་པ་ན། དགེ་སློང་སྟན་ལས་ལངས་ཏེ་མཆི་ཞིང་དགེ་སློང༌[^1260]མཆིས་པ་དག་ལ་ཡང་མི་སྨྲ་བར་མཆི་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེ་བ་འཁོར་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1992]
ཆོས་དང་ལྡན་པ་ཉིད་མ་ཡིན་པའི་ལས་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཆོས་དང་ལྡན་པ་ཉིད་མ་ཡིན་པ་འདི་རྣམས་ལ་དངོས་གཞིའི་གནས་སུ་ཉེས་བྱས་སོ། །

[Block 1993]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས།

[Block 1994]
ཆོས་དང་ལྡན་པ་ཉིད་མ་ཡིན་པའི་ལས་བྱེད་པ་ན་འགྲོ་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1995]
ཐོས་པའི་ཡུལ་ལས་མི་འདའ་བར་འདོད་པ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ༌[^1261]འདི་ནི་སྔར་མདུན་རོལ་དུ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་སྨོས་པ་དེའི་དམིགས་ཀྱིས་བསལ་བ་ཡིན་ནོ། །

[Block 1996]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 1997]
གསོལ་བ་བརྩམས་པ་ནས་བཤང་བའི་ས་འམ་གཅི་བའི་སར་འགྲོ་བ་འམ་འོང་ཡང་རུང་སྟེ། དགེ་སློང་འཁོད་པ་དག་ལ་མི་སྨྲ་ཡང་ཐོས་པའི་ཉེ་འཁོར་ཡོངས་སུ་མི་གཏོང་བ་གང་ཡིན་པ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1998]
འདིར་སྔ་མ་ལ་ཡང་ཐོས་པའི་ཉེ་འཁོར་མི་གཏོང་བ་ལ་ལྟུང་བ་མེད་པར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 1999]
གཏོང་ན་ནི་ངེས་པར་ཉམས་པར་འགྱུར་རོ། །

[Block 2000]
མི་སྨྲ་བར་འགྲོ་བའི་ལྟུང་བྱེད་དོ།། །།
--- END BLOCKS ---
