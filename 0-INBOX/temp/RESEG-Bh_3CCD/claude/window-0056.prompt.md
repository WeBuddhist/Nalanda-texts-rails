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
སེམས་དཔའ་ནི་ཤེས་རབ་ཀྱི་ཡེ་ཤེས་སོ། །

[Block 1962]
དེ་དག་རོ་གཅིག་པ་ནི་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་སེམས་དཔའོ། །

[Block 1963]
ཡང་ན་དཔལ་ནི་ཐབས་ཏེ་རྡོ་རྗེ་ཤེས་རབ་བོ། །

[Block 1964]
དེས་ན་སྙིང་རྗེ་དང་སྟོང་པ་ཉིད་དབྱེར་མེད་པ་ཉིད་དཔལ་རྡོ་རྗེ་སེམས་དཔའོ། །

[Block 1965]
རྡོ་རྗེ་རྩེ་མོ་ལས་ཀྱང་།

[Block 1966 [VERSE]]
བརྟན་ཞིང་སྙིང་པོ་ཁོང་སྟོང་མེད། །
དབྱེར་མེད་བཅད༌[^1333]མེད་མཚན་ཉིད་ཅན། །
བསྲེག་ཏུ་མེད་དང་མི༌[^1334]འཇིག་ནི། །
སྟོང་ཉིད་རྡོ་རྗེ་ཞེས་སུ་བཤད། །

[Block 1967]
ཅེས་འབྱུང་ངོ་། །

[Block 1968]
བཏུད་དེ་ཞེས་པ་ནི་ལུས་ངག་ཡིད་ཀྱིས་འདུད་པའམ༌[^1335]དེའི་བདག་ཉིད་དུ་རྗེས་སུ་འཇུག་པའོ། །

[Block 1969]
རིམ་པ་བཞིན་ནི་གོ་རིམས་ཀྱིས༌[^1336]སོ། །

[Block 1970]
ཟླ་བ་གྲགས་པས་རབ་གསལ་བཤད་པ་ནི། གསལ་བར་སྟོན་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 1971]
རིམ་པ་གཉིས་པོའི་གནས་ཞེས་གང་བཤད་པ་དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། བསྐྱེད་པའི་རིམ་པ་དང་པོ་ཡིན། །ཞེས་སྨོས་ཏེ། བསྐྱེད་པའི༌[^1337]གཙོར་གྱུར་པའི་རིམ་པ་ནི་བསྐྱེད་པའི་རིམ་པ༌[^1338]སྟེ་དེ་བཞིན་དུ་བཟླ་བ༌[^1339]དང་རྡོ་རྗེ་དང་ས་བོན་དང་སྤྲོ་བ་དང་བསྡུ་བས་ལྷའི་གཟུགས་ཀྱིས་ཐ་མལ་པའི་ལུས་བཟློག་པས་འཇིག་རྟེན་ལས་འདས་པའི་རྡོ་རྗེ་ལྟ་བུའི་སྐུ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1972]
དེ་ལ་དང་པོའི་སྦྱོར་བ་ལ་སོགས་པ་དབྱེ་བ་གསུམ་སྔར་བཤད་ཟིན་ཏོ། །

[Block 1973]
རིགས་བརྒྱའི་བྱེ་བྲག་གི་མཐའ་ཅན་ཞེས་སྨྲ་བར་བྱ་བ་ཡིན་ཏེ། བསྐྱེད་པའི་རིམ་པ་གཅིག་པུས་ཐ་མལ་པའི་ལུས་རྣམ་པར་དག་པར་བྱེད་མི་ནུས་ཏེ། འོན་ཀྱང་ཏིང་ངེ་འཛིན་གསུམ་གྱི་འོག་ཏུ་གང་གི་ཚེ་ཕུང་པོ་ཁམས་དང་སྐྱེ་མཆེད་ཀྱི་བདག་ཉིད་ཀྱི་ལུས་ཆ་ཤས་ཀྱི་དབྱེ་བས་ཡེ་ཤེས་ལྔའི་ངོ་བོ་དེ་བཞིན་གཤེགས་པ་ལྔས་རྣམ་པར་དབེན་པར་བྱེད་པ་དེའི་ཚེ་ཐ་མལ་པའི་ལུས་ཀྱི་ཉེ་བར་དམིགས་པ་སྤངས་ནས། ཐ་མལ་པ་མ་ཡིན་པའི་སྐུ་བྱུང་བ་དེ་ཉིད་བསྐྱེད་པའི་རིམ་པའི་མཐར་ཕྱིན་པའོ། །

[Block 1974]
གཅིག་པུས་མི་ནུས་ཞེས་སྨྲ་བར་མི་བྱ་སྟེ། ཏིང་ངེ་འཛིན་གསུམ་བཞིན་དུ༌[^1340]དེ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1975]
རིགས་བརྒྱའི་དབྱེ་བའི་མཐའ་ཅན་བསྐྱེད་པའི་རིམ་པ་ཡིན་ཞེས་སྨྲ་བར་མི་བྱ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། ཏིང་ངེ་འཛིན་གསུམ་རྩ་བའི༌[^1341]རྒྱུད་ལས་ཇི་ལྟར་བརྟག་པ༌[^1342]བཞིན་དུ་རིགས་བརྒྱའི་དབྱེ་བ་ཡང་ཤེས་པར་བྱའོ། །

[Block 1976]
དེ་ལྟར་མ་ཡིན་ཏེ་གུད་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 1977]
ཏིང་ངེ་འཛིན་གསུམ་བཞིན་དུ་དེ་ཡང་གྲུབ་པོ་ཞེས་གང་སྨྲས་པ་དེ་ནི་མ་ཡིན་ནོ།[^1343] །

[Block 1978]
གཉི་ག་གསུངས་པའི་ཕྱིར་རོ། །

[Block 1979]
འདི་ལྟ་སྟེ། དེ་ནས་བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་རྡོ་རྗེ་རྣམ་པར་སྣང༌[^1344]མཛད་ཆེན་པོས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་འདོད་ཆགས་ཆེན་པོའི་ཚུལ་ཞེས་བྱ་བའི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་སོ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་དང་གསུང་དང་ཐུགས་ཀྱི་རྡོ་རྗེ་ལ་བཞུགས༌[^1345]པར་གྱུར་ཏོ་ཞེས་བྱ་བའི་བར་དུ་དང་པོའི་སྦྱོར་བ་ཞེས་བྱ་བ་ཉེ་བར་བསྟན་ཏོ། །

[Block 1980]
དེ་ནས་བཅོམ་ལྡན་འདས་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་དམ་ཚིག་འབྱུང་བ་ཆེན་པོ་རྡོ་རྗེ་ཞེས་བྱ་བའི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་ཏེ་ཞེས་པ་ནས་བརྩམས་ཏེ། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་སྐུ་དང་གསུང་དང་ཐུགས་མཉེས་པར་བྱེད་པ་དཀྱིལ་འཁོར་གྱི་དམ་ཚིག་སེམས་དཔའ་རྣམས་སོ་སོ་ཞེས་བྱ་བའི་བར་གྱིས་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 1981]
དེའི་རྗེས་སུ་ལེའུ་དྲུག་པ་ལ་སོགས་པ་དག་ཏུ། སྣ་ཡི་རྩེ་མོར་ཡུངས་ཀར་བསམ། །ཞེས་བྱ་བ་ལ་སོགས་པས་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ་ཞེས་དེའི་ཕྱིར་ཏིང་ངེ་འཛིན་གསུམ་པོ་གསལ་བར་བསྟན་ཏོ། །

[Block 1982]
རིགས་བརྒྱའི་བྱེ་བྲག་གི་མཐའ་ཅན་དུ་སྨྲ་བ་ཁོ་ནའོ། །

[Block 1983]
དེ་ཡང་དང་པོ་ཡིན་ཞེས་པ་ནི་དང་པོ་ལུས་ཀྱི་རྣམ་པར་རྟོག་པ་རགས་པ་སྤང་བར་བྱ་བ་ཡིན་ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 1984]
དེ་ལས་ལུས་རྣམ་པར་དག་ནས་ངག་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར། རིམ་པ་ལྔ་པོའི་དང་པོ་རྡོ་རྗེ་བཟླས་པ་ཞེས་བྱ་བ་བསྒོམ་པར་བྱ་སྟེ། དེའི་ཕྱིར་གསང་སྔགས་ཀྱི་སྐུ་ནི་རབ་སྒྲུབ་བྱེད་ཅེས་བྱ་བ༌[^1346]སྨོས་ཏེ། དེ་ལ༌[^1347]བཅོམ་ལྡན་འདས་ཀྱིས་བསམ་པ་དང་བག་ལ་ཉལ་བ་དང་ཁམས་དང་བག་ཆགས་ཀྱི་དབྱེ་བས་སྔགས་ཀྱི་ས་ཡ༌[^1348]བདུན་ཅུ་རྩ་གཉིས་བཤད་དོ། །

[Block 1985]
དེ་དག་ཐམས་ཅད་ཀྱི་རྩ་བ་ནི་ཡི་གེ་བཞི་བཅུ་རྩ་དགུ་པ་ཕྱི་མའོ། །

[Block 1986]
དེ་ཡང་སྡེ་ཚན་བརྒྱད་ཀྱི་བདག་ཉིད་དང་པོའི་ཡི་གེ་རྣམས་ལ་ཡོངས་སུ་ཐིམ་པར་གྱུར་པའོ། །

[Block 1987]
དེ་དག་ཀྱང་བཞི་པོ་ལ་ཐིམ། བཞི་པོ་ཡང་ཡི་གེ་གསུམ་གྱི་བདག་ཉིད་དུ་གྱུར་པས་ཞེས་ཡི་གེ་དང་ཚིག་དང་ངག་དང་རབ་ཏུ་བྱེད་པ་དང་སྔགས་ཐམས་ཅད་ཀྱི་ཡི་གེ་གསུམ་པོ་ཁོ་ན་རྒྱུའི༌[^1349]གཙོ་བོ་ཡིན་ཏེ། རིགས་གསུམ་རྣམ་པར་དག་པས་སྐུ་གསུང་ཐུགས་ཀྱི་ངོ་བོར༌[^1350]གྱུར་པ་གསང་སྔགས་ཀྱི་སྐུའོ། །

[Block 1988]
དེ་ཡང་གཉིས་ཏེ། རླུང་གི་བདག་ཉིད་དང་། ཡི་གེའི་བདག་ཉིད་དོ། །

[Block 1989]
དེ་ལ་འཇུག་པ་དང་། གནས་པ་དང་། ལྡང་བའི་རིམ་པས་ཉིན་མཚན་དུ་ཉི་ཁྲི་ཆིག་སྟོང་དྲུག་བརྒྱའི་དཀྱིལ་འཁོར་བཞིའི་སྦྱོར་བས་གོམས་པས་སེམས་རྩེ་གཅིག་པ་དེ་ཉིད་གང་ཡིན་པ་དེ༌[^1351]ནི་རླུང་གི་བདག་ཉིད་ཀྱི་སྔགས་ཀྱི་སྐུའོ། །

[Block 1990]
རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པའི་སྔགས་ཀྱི་བཟླས་པ་ལ་ཡི་གེ་གསུམ་པོ་ཁོ་ན་སྤྱི་བོ་ལ་སོགས་པར་གནས་པ་ཡན་ལག་མ་ཉམས་པར་བཟླས་པའི་རིམ་པ་གོམས་པར་བྱེད་པ་ན་སེམས་རྩེ་གཅིག་པ་ཉིད་གང་ཡིན་པ་དེ་ནི་ཡི་གེའི་བདག་ཉིད་གསང་སྔགས་ཀྱི་སྐུའོ། །

[Block 1991]
དེ་གཉིས་ཀ་རབ་ཏུ་སྒྲུབ་པར་བྱེད་པ་ནི་རྫོགས་པར་བྱེད་པ་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་སྟེ་གཅིག་གོ། །

[Block 1992]
དེས་ནི་ངག་གི་ངོ་བོ་ཤེས་ནས་བསྟོད་པ་དང་སྨད་པ༌[^1352]ལ་སོགས་པའི་ཚིག་གིས༌[^1353]རྣལ་འབྱོར་པ་མགུ་བ་དང༌[^1354]མི་མགུ་བར་མི་འགྱུར་རོ་ཞེས་གསུང་གི་རྡོ་རྗེའི་ཏིང་ངེ་འཛིན་ལ་གནས་པའོ། །

[Block 1993]
གཅིག་ཅེས་སྨྲ་བར་བྱ་བ་ཡིན་ཏེ། རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་གསང་སྔགས་ཀྱི་སྐུ་རབ་ཏུ་སྒྲུབ་པར་བྱེད་པ་གཅིག་ནི་དང་པོ་སྟེ་རྫོགས་པའི་རིམ་པའི་དང་པོའོ། །

[Block 1994]
ལ་ལ་ན་རེ་བསྐྱེད་པའི་རིམ་པ་ཁྱད་པར་དུ་གྱུར་པ་ཁོ་ན་གསང་སྔགས་ཀྱི་སྐུ་རབ་ཏུ་སྒྲུབ་པར་བྱེད་པ་ཞེས་འཆད་པ་དེ་ནི་མི་བདེན་ཏེ། དེ་ལྟ་ཡིན་ན་རྡོ་རྗེ་བཟླས་པ་མ་འདུས་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 1995]
དེ་མ༌[^1355]གཏོགས་པར་ངག་རྣམ་པར་དག་པ་མེད་པས་དགོས་པ་ཁོ་ནའོ། །

[Block 1996]
གང་གི་ཚེ། བསྐྱེད་པའི་རིམ་པ་དང་པོ་ཡིན། །ཞེས་དང་པོ་བསྐྱེད་པའི༌[^1356]རིམ་པ་བསྒོམ་པ༌[^1357]ཡིན་ན་དེའི་ཚེ་གཅིག་ཅེས༌[^1358]སྨྲས་པས།[^1359] རྡོ་རྗེ་བཟླས་པའི་རིམ་པའི་འོག་ཏུ་སེམས་ལ་དམིགས་པ་ཙམ་ཞིག་ནི་རིམ་པ་གཉིས་པ་ཞེས་བརྗོད་དོ་ཞེས་སྨྲས་པར༌[^1360]མི་རིགས་ཏེ། རྡོ་རྗེ་བཟླས་པའི་འོག་ཏུ་དེ་ཉེ་བར་བསྟན་པ་ཡིན་གྱི་བསྐྱེད་པའི་རིམ་པའི་འོག་ཏུ་ནི་མ་ཡིན་ནོ། །

[Block 1997]
དེའི་ཕྱིར་གསང་སྔགས་ཀྱི་སྐུ་རབ་ཏུ་སྒྲུབ་པར་བྱེད་པའི་སྒྲ་ནི་བསྐྱེད་པའི་རིམ་པའི་ཁྱད་པར་མ་ཡིན་ཏེ་འོན་ཀྱང་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་ཁོ་ན་སྟོན་པར་བྱེད་པའོ། །

[Block 1998]
དེའི་ཁྱད་པར་བྱེད་པའི་ཕྱིར་གཅིག་ཅེས་སྨྲ་བར་བྱ་བ༌[^1361]ཁོ་ནའོ། །

[Block 1999]
ཇི་ལྟར་རིམ་པ་ཁོ་ན་མཆོག་གོ། །

[Block 2000]
སེམས་ལ་དམིགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ངག་རྣམ་པར་དག་པར་གྱུར་པས་རྣམ་པར་ཤེས་པ་གསུམ་གྱི་བདག་ཉིད་ཀྱི་སེམས་ལ་དམིགས་པ་ནི་མཐོང་བ་སྟེ། སྔར་བཤད་པའི་སྔགས་དང་ཕྱག་རྒྱའི་རིམ་པས་འོད་གསལ་བར་བྱའོ། །
--- END BLOCKS ---
