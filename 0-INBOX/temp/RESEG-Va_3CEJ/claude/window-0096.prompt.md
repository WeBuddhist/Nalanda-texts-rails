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
[Block 3361 [HEADING]]
##### འཛམ་བུའི་ཚལ་ན་འདུག་པའི་སོ་སོའི་སྐྱེ་བོ། ^3-1-12-5-0

[Block 3362]
བཅོམ་ལྡན་འདས་ཀྱིས། གང་གིས་ཕྱིའི༌[^1918]དྲང་སྲོང་འདོད་པ་དག༌[^1919]ལས་འདོད་ཆགས་དང་བྲལ་བ་བརྒྱ་ལ་ཟས་བྱིན་པ་བས་གང་གིས་འཛམ་བུའི་ཚལ་ན་འདུག་པའི་སོ་སོའི་སྐྱེ་བོ་གཅིག་ལ་བྱིན་ན་སྦྱིན་པ༌[^1920]དེ་བས་སྦྱིན་པ་འདི་འབྲས་བུ་ཆེས་ཆེའོ་ཞེས་གསུངས་པ། འཛམ་བུའི་ཚལ་ན་འདུག་པའི་སོ་སོའི་སྐྱེ་བོ་ཞེས་བྱ་བ་ནི༌[^1921]གང་ཞེ་ན། ཁ་ཅིག་ན་རེ་འཛམ་བུའི་གླིང་ན་གནས་པ་ལྟོ༌[^1922]དང་ལྡན་པ་དག་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3363]
དེ་ནི་རིགས་པ༌[^1923]མ་ཡིན་ཏེ། གཅིག་ཅེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3364]
སོ་སོའི་སྐྱེ་བོ་མང་པོ་ལ་ཟས་བྱིན་ན་བསོད་ནམས་མང་པོར་འགྱུར་གྱི་འདོད་ཆགས་དང་བྲལ་བ་ཉུང་ངུ་ལ་ཟས་བྱིན་པས༌[^1924]ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་གང་ཡིན་པ༌[^1925]འདི་ལ་ཁྱད་པར་ཅི་ཞིག་ཡོད། གཞན་དག་ན་རེ་བྱང་ཆུབ་སེམས་དཔའ་ཉེ་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3365]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་དེ་སྐད་དུ་མི་བརྗོད་དེ། དེ་ལ་བྱིན་ན་དགྲ་བཅོམ་པ་བྱེ་བ་ལ་བྱིན་པ་བས་བསོད་ནམས་ཆེས་མང་བའི་ཕྱིར་རོ། །

[Block 3366]
དེ་ལྟ་བས་ན་འདི་ནི་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ཐོབ་པ་སོ་སོའི་སྐྱེ་བོ་ཡིན་པར་དགོངས་སོ་ཞེས་ཟེར་རོ། །

[Block 3367]
འདིའི་མིང་ཡང་དོན་དང་མཐུན་པ་མ་ཡིན་ལ། མདོའམ་བསྟན་བཅོས་གང་ལས་ཀྱང་འཛམ་བུའི་ཚལ་དུ་གཏོགས་པ་ནི་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ཐོབ་པའོ༌[^1926]ཞེས་འོལ་ཕྱིར༌[^1927]མ་བཤད་པས་འདི་ནི་ཡོངས་སུ་རྟོག་པ་འབའ་ཞིག་ཏུ་ཟད་ཀྱི། འདི་ནི་བྱང་ཆུབ་སེམས་དཔའི༌[^1928]འཛམ་བུའི་ཚལ་ན་བཞུགས་པ་ཁོ་ན་ཡིན་པར་རིགས་ཏེ། སོ་སོའི་སྐྱེ་བོ་དེ་ནི་འདོད་པའི་འདོད་ཆགས་དང་བྲལ་བར་འདྲ་བས་དེའི་ཚེ་དེ་དག་ལས་ཁྱད་པར་དུ་འཕགས་པར་གསུངས་སོ། །

[Block 3368]
དེ་ནི་དེ་དག་མཐའ་ཡས་པ་བས་ཀྱང་ཁྱད་པར་དུ་འཕགས་ན། བརྒྱ་སྨོས་པ་ནི་དང་པོའི་དབང་དུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 3369]
དེ་ནི་གདོན་མི་ཟ་བར་དེ་ལྟ་ཡིན་པར་ཤེས་པར་བྱ་སྟེ། འདི་ལྟར་དེ་མ་གཏོགས་པའི་ཕྱི་རོལ་པ་རྣམས་ལས་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ལ་ཞུགས་པ་ཁྱད་པར་དུ་འཕགས་པར་མཛད་པར་གྱུར་ཏོ། །

[Block 3370]
དེ་ལྟ་མ་ཡིན་ན་འཛམ་བུའི་ཚལ་དུ་གཏོགས་པ་ལས་ཀྱང་ཁྱད་པར་དུ་འཕགས་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 3371]
སེམས་ཅན་རྣམས་ཀྱི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཇི་ལྟ་བ་དང་། ཇི་ལྟར་གནས་པ་བཤད་ཟིན་ཏོ། །

[Block 3372]
ཇི་ལྟར་ཚེ་ཟད་པ་ལ་སོགས་པས་འཆི་འཕོ་བ་ལ༌[^1929]ཡང་བཤད་ཟིན་ཏོ། །

[Block 3373 [HEADING]]
#### སེམས་གང་ལ་གནས་ཏེ་འཆི་འཕོ་བ་དང་སྐྱེ་བ། ^3-1-13-0

[Block 3374]
ད་ནི་སེམས༌[^1930]གང་ལ་གནས་ཏེ་འཆི་འཕོ་བ་དང་སྐྱེ་བར་འགྱུར་བ་འདི་བརྗོད་པར་བྱ་སྟེ།

[Block 3375 [VERSE]]
འཆད་དང་མཚམས་སྦྱོར་འདོད་ཆགས་བྲལ། །
ཉམས་དང་འཆི་འཕོ༌[^1931]སྐྱེ་བ་རྣམས། །
ཡིད་ཀྱི་རྣམ་ཤེས་ཁོ་ནར་འདོད། །

[Block 3376]
ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 3377]
དེ༌[^1932]དགེ་བའི་རྩ་བ་ཡང་དག་པར་འཆད་པ་དང་། དགེ་བའི་རྩ་བ་ཉིང་མཚམས་སྦྱོར་བ་དང་། ཁམས་དང་ས་ལས་འདོད་ཆགས་དང༌[^1933]བྲལ་བ་དང་། ཡོངས་སུ་ཉམས་པ་དང་། འཆི་འཕོ་བ་དང་། སྐྱེ་བ་དང་། ཆོས་དྲུག་པོ་འདི་དག་ནི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་ཁོ་ན་ཡིན་པར་འདོད་ཀྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 3378]
སྐྱེ་བ་སྨོས་པ་ནི་སྲིད་པ་བར་མར་ཉིང་མཚམས་སྦྱོར་བ༌[^1934]བཤད་ཟིན་པའི་ངོ་བོར་རིག་པར་བྱའོ། །

[Block 3379]
ཚོར་བ་ནི། འཆི་འཕོ་སྐྱེ་བ་བཏང་སྙོམས་ལ། །འཆི་འཕོ་བ་ནི་འཆི་འཕོ་བ་ཉིད་ཡིན་ནོ། །

[Block 3380]
སྐྱེ་བ་ནི་སྐྱེ་བ་ཡིན་ནོ། །

[Block 3381]
འདི་གཉིས་བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་ཡང་མ་ཡིན་པའི་ཚོར་བ༌[^1935]ཡིན་ཏེ། དེ་ནི་མི་གསལ་བའི་ཕྱིར་རོ། །

[Block 3382]
ཚོར་བ་གཞན་དག་ནི་གསལ་བ་ཡིན་ཏེ། རྣམ་པར་ཤེས་པ་གསལ་བ་དག་གིས་འཆི་འཕོ་བ་དང་སྐྱེ་བར་ནི་རུང་བ་མ་ཡིན་ནོ། །

[Block 3383]
ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་དེ་ལ་ཡང་། རྩེ་གཅིག་སེམས་མེད་ལ་དེ་མེད། །འཆི་འཕོ་བ་དང་སྐྱེ་བ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3384]
སྐལ་བ་མི་མཉམ་པའི་ས་པ་ཡིན་པའི་ཕྱིར་དང་། མངོན་པར་འདུ་བྱེད་པ་ལས་བྱུང་བ་ཉིད་ཡིན་པའི་ཕྱིར་དང་། ཕན་འདོགས་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་མཉམ་པར་གཞག་པའི་སེམས་ལ་འཆི་འཕོ་བའམ་སྐྱེ་བ་མེད་དོ། །

[Block 3385]
སེམས་མེད་པ་ལ་ཡང་མེད་དེ། སེམས་མེད་པ་ལ་ནི་གནོད་པ་བྱ་བར་མི་ནུས་སོ། །

[Block 3386]
གང་གི་ཚེ་དེའི་ལུས་ཡོངས་སུ་འཇིག་པར་རྩོམ་པ་དེའི་ཚེ་ཡང་དེ་ལས་གདོན་མི་ཟ་བར་དེའི་ལུས་དང་འབྲེལ་པའི་སེམས་མངོན་དུ་གྱུར་ནས་ཕྱིས་འཆི་འཕོ་བར་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 3387]
སྐྱེ་བ་ལ་ཡང་སེམས་འཆད་པའི་རྒྱུ་མེད་པའི་ཕྱིར་དང་། ཉོན་མོངས་པ་མེད་པར་མི་སྐྱེ་བའི་ཕྱིར་སེམས་མེད་པར་རིགས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 3388]
འཆི་བའི་སྲིད་པ་རྣམ་པ་གསུམ་དུ་བཤད་པ་ལ། དགྲ་བཅོམ་པ་ནི། མྱ་ངན་འདས་ལུང་བསྟན་མིན་གཉིས། །སྤྱོད་ལམ་པ་དང་། གལ་ཏེ་འདོད་པའི་ཁམས་ན༌[^1936]རྣམ་པར་སྨིན་པའི༌[^1937]བཏང་སྙོམས་ཡོད་ན་རྣམ་པར་སྨིན་པའི་སེམས་ལ་གནས་ནས་སོ། །

[Block 3389]
ཅི་སྟེ་མེད་ན་ནི་སྤྱོད་ལམ་པ་ཁོ་ན་ལའོ། །

[Block 3390]
ཅིའི་ཕྱིར་ལུང་དུ་མ་བསྟན་པ་ཁོ་ན་ལ་ཡིན་གྱི་གཞན་ལ་མ་ཡིན་ཞེ་ན། དེ་ནི་ཉམ་ཆུང་བའི་ཕྱིར་སེམས་འཆད་པའི་རྗེས་སུ་མཐུན་པ་ཡིན་ནོ། །

[Block 3391 [HEADING]]
#### ལུས་ཀྱི་ཕྱོགས་གང་དུ་རྣམ་པར་ཤེས་པ་འགག་པ། ^3-1-14-0

[Block 3392]
ཡང་འཆི་བ་ན་ལུས་ཀྱི་ཕྱོགས་གང་དུ་རྣམ་པར་ཤེས་པ༌[^1938]འགག་ཅེ་ན། ཅིག་ཅར་འཆི་ན་ནི་ཡིད་དང་བཅས་པའི་ལུས་ཀྱི་དབང་པོ་མོད་ལ་འགག་པར་འགྱུར་རོ། །

[Block 3393]
གལ་ཏེ་རིམ་གྱིས་འཆི་འཕོ་བ༌[^1939]ན༌[^1940]དེའི་ཚེ།

[Block 3394 [VERSE]]
འོག་མིན༌[^1941]ལྷར་འགྲོ་མི་སྐྱེ་རྣམས། །
རིམ་གྱིས་འཆི་ན་རྐང་པ་དང་། །
ལྟེ་བ་སྙིང་གར་ཡིད་འཆི་འཕོ། །

[Block 3395]
འོག་ཏུ་འགྲོ་བས་ན་འོག་ཏུ་འགྲོ་བ་སྟེ།

[Block 3396 [VERSE]]
ངན་སོང་དུ་འགྲོ་བ་རྣམས་སོ། །
མིར་འགྲོ་བས་ན་མིར་འགྲོ་བས་ཏེ།
མིའི་ནང་དུ་འགྲོ་བ་རྣམས་སོ། །

[Block 3397]
ལྷར་འགྲོ་བས༌[^1942]ན་ལྷར་འགྲོ་བ་སྟེ། ལྷའི་ནང་དུ་འགྲོ་བ་རྣམས་སོ། །

[Block 3398]
དེ་དག་གི་རྣམ་པར་ཤེས་པ་ནི་གྲངས་བཞིན་དུ་རྐང་པ་དང་། ལྟེ་བ་དང་། སྙིང་གར་འགག་གོ། །

[Block 3399]
ཡང་མི་སྐྱེ་བས་ན་མི་སྐྱེ་བ་སྟེ། དགྲ་བཅོམ་པ་དག་གོ། །

[Block 3400]
དེ་དག་གི་རྣམ་པར་ཤེས་པ༌[^1943]སྙིང་ཁར་འགག་གོ། །
--- END BLOCKS ---
