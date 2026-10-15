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
[Block 1926]
ཇི་ལྟར་གཙུག་ལག་ཁང་གི་ཁ་ཟས་ནི་གང་ཟག་མགྲོན་དུ་བོས་པ་མ་ཡིན་པ་དེ་བཞིན་དུ་འདིས་ཞེས་བྱ་བའི་ཚིག་འདིའོ། །

[Block 1927]
དུས་ཐམས་ཅད་དུ་ཡང༌[^1219]ཞེས་བྱ་བ་ནི་དགེ་འདུན་ནམ་གང་ཟག་ཇི་སྲིད་འཚོའི་བར་དུ་མགྲོན་དུ་བོས་ན་ཡང་བདག་གིར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1928]
ཅི་ཞིག་བྱས་ནས་མགྲོན་དུ་གཉེར་བ་ལས་རིང་དུ་འདུག་པའམ་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཚིག་རྣམ་པར་གཞག་པ་མེད་པར་མགྲོན་དུ་གཉེར་བ་དང་ལྡན་པ་ལ། ཕྱིས་གཞན་ནམ་ཡང་དང་ཡང་དུའམ་དུས་ཀྱི་མགྲོན་དུ་གཉེར་བར་མ་བྱས་པ་ཟླ་བ་བཞི་པ་ཡོངས་སུ་རྫོགས་པའི་འོག་ཏུ་བཤམས་པ་ཟོས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཞིག་དུས་འདི་ཙམ་དུ་རྟག་པ་ཉིད་དུ་ངེས་པ་རྣམ་པར་གཞག་ནས་ཁྱད་པར་དུ་དགེ་འདུན་གྱི་སྒོ་ནས་མགྲོན་དུ་གཉེར་བར་བྱེད་པ་རབ་ཏུ་སྦྱར་བའི་མགྲོན་དུ་གཉེར་བར་བྱས་པའམ། ཉེ་བར་སྤྱན་དྲངས་པར་གྱུར་པ་འདི་ལྟ་བུར་གྱུར་པའི་མགྲོན་དུ་བོས་པའི་འོག་ཏུ་དགེ་འདུན་ལ་གཞན་དུ་བྱས་པ་ཉིད་ལ་གང་ཟག་ལ༌[^1220]བྱས་པས་དགེ་འདུན་ལ་བྱས་པ་ཉིད་དོ། །

[Block 1929]
ཡང་དང་ཡང་དུའམ་ཤིན་ཏུ་དོན་ཉིད་ཀྱིས་མགྲོན་དུ་བོས་པ་བྱས་པ་ནི་ཟླ་བ་བཞིའི་མཐར་ཐུག་པའི་འོག་ཏུ་བཤམས་པ་རྣམ་པར་གཞག་པ་བྱས་པ་ནི༌[^1221]མགྲོན་དུ་གཉེར་བར་བྱས་པ་ཁ་ཟས་སུ་བྱས་པ་ཟ་བར་བྱེད་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1930]
མགྲོན་དུ་གཉེར་བ་ལས་ལྷག་པར་གནས་པའི་ཁ་ན་མ་ཐོ་བ་འདི་དང་མགྲོན་དུ་མ༌[^1222]བོས་པའི་དོན་དུ༌[^1223]ཁ་ཟས་བསོད་པའི་ཁ་ན་མ་ཐོ་བའི་ཆོ་ག་འདི་གཉིས་ཀྱི་བྱེ་བྲག་རྟོགས་པར་བྱའོ། །

[Block 1931]
རྟག་ཏུ་མགྲོན་དུ་བོས་པ་ལས་གཞན་དུ་ཞེས་བྱ་བ༌[^1224]འདི་ལ་ངེས་པར་རྣམ་པར་གཞག་པ་མེད་པར་ཞེས་བྱ་བ་བསྡུ་བའོ། །

[Block 1932]
དངོས་སུ་ནི་ཟླ་བ་བཞིའི་འོག་ཏུ་རྙེད་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་དེ་ལ་འདི་བསྟན་པའི་དོན་དུའོ། །

[Block 1933]
གཞན་དག་གིས༌[^1225]སོ་སོར་མགྲོན་དུ་གཉེར་བ་ཞེས་བྱ་བ་དེ་ལ་གཞན་དུ་ཞེས་བྱ་བ་དེའི༌[^1226]འདི་བསྡུ་བའོ། །

[Block 1934]
འདིར་ཁ་ཟས་བསོད་པ་ལ་མངོན་པར་བརྟེན་པ་ཡོད་པ་མ༌[^1227]ཡིན་ནོ། །

[Block 1935]
དེ་བས་ན་ཁ་ཟས་ཐ་མལ་པ་ལ་ཡང་འདིར་ཡོངས་སུ་རྫོགས་པ་ལ་ཁ་ན་མ་ཐོ་བ་བྱེད་པ་ཉིད་དོ། །

[Block 1936]
འདིར་གཞུང་ནི་བསྡུ་བ་བསྟན་པ་ལས་དགེ་སློང་ཟླ་བ་བཞིའི་བར་དུ་མགྲོན་དུ་བོས་པ་ལས་ཅུང་ཟད་ལྷག་པར་རོ་མྱོང་བར་བྱེད་ན་སོ་སོར་མགྲོན་དུ་བོས་པ་དང་། རྟག་ཏུ་མགྲོན་དུ་བོས་པ་མ་གཏོགས༌[^1228]པར་ཐམས་ཅད་དུ་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1937]
རྣམ་པར་རིག་བྱེད་ལ་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་འདི་ནི་སྦྱོར་བ་ལ་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་དེའི་སྤྲོས་པ་ཡིན་ཏེ། འདིར་རྣམ་པར་རིག་བྱེད་ཅེས་བྱ་བ་འདི་ནི་ཟླ་བ་བཞི་ལས་ལྷག་པར་བཤམས་པའི་ཟན་གྱི་ཕྱིར་ཉེ་བར་འགྲོ་བ་ཡང་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 1938]
ནད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ནད་པའི་ཕྱིར་བླངས་པ་དང་ཟ་བ་ནི་ཉེས་པ་མེད་དོ། །

[Block 1939]
འདིར་གཞུང་ནི་ཞུ་བ་དག་ལས་མི་ན་བར་བླངས་ཏེ་ཟ་ན་བླངས་པ་ལ་ནི་ཉེས་བྱས་ལ། ཟོས་པ་ལ་ནི་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་དེ༌[^1229]ཉིད་མདོ་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 1940]
ཉེ་དུ་ལས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་སྦྱིན་བདག་ཉེ་དུ་ལས་བླངས་ཏེ་ཟོས་པ་ལ་ཡང་ལྟུང་བ་མེད་དོ། །

[Block 1941]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་ཁྱིམ་བདག་དེ་དེའི༌[^1230]ཕུ་ནུ་འམ། བུ་ཚའམ་བུ་སྲིང་ཡིན་ན་དེ་དག་ལས་རོ་མྱོང༌[^1231]བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1942]
རྣམ་པར་འཁྱམས་པ་ལས་སྔ་མ་ནི་ཐ་དད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རྣམ་པར་འཁྱམས་པ་ཞེས་བྱ་བ་ཁྱིམ་པར་བབས་པ་ལས་སྔ་མ་ཞེས་བྱ་བ་དེ་དགེ་སློང་ཉིད་ནི་ཐ་དད་པ་ཉིད་ཡིན་པའོ། །

[Block 1943]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་ཚེ་དང་ལྡན་པ་ལ་གང་དགོས་པ་དེ་ཁྱེར་ཅིག་ཅེས་དགེ་སློང་ལ་བསྟབས་པར་གྱུར་པ་ལས་དགེ་སློང་དེ་རྣམ་པར་འཁྱམས་པར་གྱུར་ཅིང་དེ་དང་བསྙེན་པར་རྫོགས་པར་བགྱིད་ན། དགེ་སློང་དེས་ཆོ་ག་སྔ་མ་དེ་ཉིད་ཀྱིས་རོ་མྱང་བར་བགྱི་འམ། གལ་ཏེ་ཡང་སྟོབས་པར༌[^1232]བྱེད་ན་ནི་རོ་མྱང་བར་བྱ་བའོ། །

[Block 1944]
སྟོབས་པར་མི་བྱེད་ན་ནི་རོ་མྱང་བར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1945]
དེ་ནི་མ་བསྟབས་པའི་ཉེས་པ་བྱེད་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རྣམ་པར་འཁྱམས་པའི་འོག་ཏུ་མགྲོན་དུ་བོས་པ་ལ་བསོད་པ་སློང་བའི་ཁ་ན་མ་ཐོ་བ་བྱེད་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1946]
མདུན་རོལ་དུ་ཡང་གང་གིས་མ་བསྟབས་པའོ་ཞེས་བྱ་བ་ནི། ཟླ་བ་བཞིའི་འོག་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་ཟླ་བ་བཞི་མ་ཚང་བའི་མདུན་རོལ་དུ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1947]
བཟའ་བར་བྱ་བའི་དངོས་པོ་གང་གིས་མགྲོན་དུ་བོས་པ་དེ་སློང་ངམ་ཟ་ན་མ་བསྟབས་པའི་ཉེས་པ་བྱེད་པ་ཉིད༌[^1233]ཡིན་པའོ། །

[Block 1948]
མགྲོན་དུ་གཉེར་བ་ལས་རིང་དུ་འདུག་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1949]
བསླབ་པ་ལ་ཉེ་བར་འཇོག་པ་སྤོང་བའི་ལྟུང་བྱེད་ལ་བྱེད་པ་པོ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མངོན་པར་ཤེས་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ།[^1234] །མངོན་པར་ཤེས་པ་ཉིད་གང་ལ༌[^1235]ཞེ་ན། དེའི་ཕྱིར་སྨྲ་བ་པོ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1950]
དེས་གང་ལ་མངོན་པར་ཤེས་པ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བསླབ་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་ཡང་དག་པ་ཁོ་ནར་བྱིས་པ་གླེན་པ་མི་གསལ་བ་མི་མཁས་པ་དག་ཡིན་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1951]
འདིར་ཆོ་ག་འདི་རྣམ་པར་གནས་པ་ཡིན་ཏེ། མངོན་དུ་བྱས་པ་ལ་དྲང་སྲོང་གིས་ཡེ་ཤེས་ཀྱིས་འདུལ་བ་མངོན་པར་ཤེས་པ་ཉིད་ལ་ཡིད་ཆེས་པ་ལས༌[^1236]ཉེ་བར་ཐོས་པ་ལ་འདིར་འདུ་ཤེས་དག་པ་སྟེ། གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 1952]
དེའི་ཕྱིར་དེ་རྣམས་ལ་གཅིག་ཏུ་ཁ་ན་མ་ཐོ་བ་མི་སྐྱེད་པ༌[^1237]སྟེ། གཞན་འགའ་ཞིག་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 1953]
གལ་ཏེ་བྱེད་པ་པོ་ཉིད་ཡིན༌[^1238]ཞེ་ན། དེའི་ཕྱིར། དགེ་སློང་གིས་ཁྱེད་ཀྱིས་འདི་ལ་བསླབ་པར་བྱའོ་ཞེས་བརྗོད་པ་ན་འམ་བསྒོ་བ་ནི་མི་སློབ་པ་ཞེས་རྒྱུའི༌[^1239]དངོས་པོ་དེས་གོ་བར་བྱེད་པ་ལ༌[^1240]མི་ཤེས་པ་ཉིད་སྒྲོགས་པར་བྱེད་པའི་ཚིག་བརྗོད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བརྗོད་པ་ནའམ་ཞེས་བྱ་བ་ནི་བསླབ་པ་ལ་ཞེས་བྱ་བ་འདིས་སྐབས་ཀྱིས་སོ་སོར་གནས་པའི་འབྲེལ་པ་ཅན་དུ་རིག་པར་བྱའོ། །

[Block 1954]
འདི་ལ་ཞེས་བྱ་བ་ནི་འདུལ་བ་ལས་གསུངས་པ་ལས་ཏེ། མདོ་སྡེ་ལས་གསུངས་པ་ནི་ཉེས་བྱས་ཀྱིའོ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1955]
བསྒོ་བ་ན་ཞེས་བྱ་བ་ནི་བརྗོད་པ་ལའོ། །

[Block 1956]
འདི་ལ་ཁྱོད་ཀྱིས་བསླབ་པར་བྱའོ་ཞེས་མོས་པར་བྱས༌[^1241]ནའོ། །

[Block 1957]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས།

[Block 1958]
འདུལ་བ་དང་ཉེ་བར་གྱུར་པའི་མདོ་སྡེ་རྣམས་བཞག་ནས་འདི་སྐད་ཅེས་སྨྲ་བར་བྱེད་དེ། བདག་གིས་འདི་ལ་བསླབ་པར་མི་བྱའོ་ཞེས་ཟེར་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 1959]
དེ་བས་ན་འདི་བརྗོད་པ་ཡིན་ནོ། །གང་གིས་འདི་ལྟར་བརྗོད་པ་ཞེ་ན། དགེ་སློང་ཞེས་སྨོས་པས་སོ། །

[Block 1960]
རྣམ་པ་གང་གིས་མི་ཤེས་པ་སྲིད་པ་ཉིད་ཀྱིས༌[^1242]ཕྱིར་ཞེ་ན། དེའི་ཕྱིར་མི་སློབ་བོ་ཞེས་རྒྱུའི་དངོས་པོ་དེས་གོ་བར་བྱེད་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། བདག་གིས་བསླབ་པ་འདི་ལ་མི་སློབ་བོ་ཞེས་དེ་སྐད་ཟེར་བ་སྟེ། གང་གི་ཕྱིར་ཁྱོད་མི་ཤེས་པ་ཉིད་སྒྲོགས་པར་བྱེད་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གོ་བར་བྱེད་པ་ལ་ཞེས་སྨོས་ཏེ། གང་གི་ཕྱིར་ཁྱོད་མི་ཤེས་པ་དེའི་ཕྱིར་ཁོ་བོ་མི་སློབ་པོ་ཞེས་གོ་བར་བྱེད་པ་ལ་མི་ཤེས་པ་ཉིད་སྒྲོགས་པར་བྱེད་པའི་ཚིག་གང་ཡིན་པ་དེ་བརྗོད་ན་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

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
--- END BLOCKS ---
