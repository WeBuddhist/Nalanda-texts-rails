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
གོ་རིམས་ཐ་དད་པ་དང་ལྡན་པ་ཡང་མེད་ན་ནི་ཐམས་ཅད་དུ་ཡི་གེ་ཙམ་ལུས་པའི་ཕྱིར་སྔ་མ་བཞིན་དུ་ཐལ་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 1962 [VERSE]]
དེ་དག་རྣམ་པར་གཞག་པའང་མེད། །
གོ་རིམས་གཞན་ནི་འགལ་ཕྱིར་རོ། །

[Block 1963]
གལ་ཏེ་ཡི་གེ་རྣམས་ཀྱི་གོ་རིམས་མ་བྱས་པ་ཡིན་ལ། དེ་དག་རིགས་མཚུངས་པ་མང་པོ་དག་མ་ཡིན་ན། གང་གིས་འགའ་ཞིག་རྣམ་པར༌[^1441]གནས་པའི་གོ་རིམས་ཅན་དུ་འགྱུར་ཞིང་། གཞན་དག་ཇི་ལྟར་འདོད་པ་བཞིན་དུ་གཞན་དུ་འགྱུར་བ༌[^1442]ཅན་དུ་འགྱུར། འོ་ན་ཅི་ཡིན་ཞེ་ན། འཇིག་རྟེན་གསུམ་ན་ཡི་གེ་ཨ་གཅིག་ཉིད་དང་དེ་བཞིན་དུ་ཡི་གེ༌[^1443]ཡང་ངོ་། །དེའི་ཚེ་ཨག་ནི་ཞེས་བྱ་བ་ཉིད་དུ་འགྱུར་གྱི། ག་གྷ་ན་ཞེས་བྱ་བ་མ་ཡིན་ཏེ། ཡི་གེ་ཨ་དང་ག་དག་ནི་སྔ་ཕྱིའི་ངོ་བོར་རྣམ་པར་གནས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1964]
རྒྱུ་ཡོངས་སུ་གྱུར་པ་ལས་ངེས་པ་དང་ལྡན་པའི་བྱས་པ་དག་གི་ཡང་གོ་རིམས་བཟློག་པར་བྱ་བར༌[^1444]ནུས་པ་མ་ཡིན་ཏེ། དཔེར་ན་ས་བོན་དང་མྱུ་གུ་དང་ལོ་མ་ལ་སོགས་པ་དང་དུས་དང་ལོ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 1965]
མ་བྱས་པ་གནས་སྐབས་དང་རང་བཞིན་བསྐྱོད་པ་ཅན་རྣམ་པ་འགའ་ཞིག་གིས་གནས་པ་དག་ཀྱང་ཅི་སྨོས་ཏེ། སྔ་མའི་གནས་སྐབས་དོར་བ་མེད་པ་རྣམ་པ་གཞན་དུ་མི་འགྱུར་བ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1966]
དོར་ན་ཡང་འཇིག་པར་ཐལ་བའི་ཕྱིར་རོ། །

[Block 1967]
ཁྱད་པར་དུ་གོ་རིམས་རྟག་པའི་ཡང་ངོ་། །ཚིག་སོ་སོ་ཡི་གེ་གཞན་ཉིད་ཡིན་ན་སྔ་ན་མེད་པ་འབྱུང་བའི་ཕྱིར་རམ། ཡི་གེ་མང་པོ་ཉིད་ཀྱི་ཕྱིར་དེ་དང་དེར་འགྱུར་ན་དེ་ཡང་འདོད་པ་མ་ཡིན་ནོ། །

[Block 1968]
གཞན་ཡང་།

[Block 1969 [VERSE]]
ཁྱབ་དང་རྟག་པར་བརྗོད་པའི་ཕྱིར། །
ཡུལ་དང་དུས་ཀྱི་གོ་རིམས་མེད། །

[Block 1970]
ཡི་གེ་རྣམས་ཀྱི་གོ་རིམས་དེ་ཡང་ཡུལ་གྱིས༌[^1445]བྱས་པ་སྟེ། དཔེར་ན་གྲོག་མོ་དག་རྒྱུ་བ་ལྟ་བུའོ། །

[Block 1971]
དུས་ཀྱིས་བྱས་པ་སྟེ། དཔེར་ན་ས་བོན་དང་མྱུ་གུ་ལ་སོགས་པར་འགྱུར་གྲང༌[^1446]ན། ཡི་གེ་རྣམས་ལ་དེ་རྣམ་པ་གཉི་ག་ཡོད་པ་མ་ཡིན་ཏེ། ཁྱབ་པའི་ཕྱིར་དང་རྟག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1972]
ཡུལ་ཕན་ཚུན་སྤངས་པས་འཇུག་པ་ནི་ཡུལ་གྱི་སྔ་ཕྱིར་འགྱུར་བ་ཡིན་ན། ཐམས་ཅད་ཐམས་ཅད་ལ་མཚུངས་པ་ཉིད་ཀྱི་ཕྱིར། དེ་ནི་ཡི་གེ་རྣམས་ལ་ཡོད་པ་མ་ཡིན་ཏེ། རླུང་དང་ཉིན་མོ་བཞིན་དང་བདག༌[^1447]ལ་སོགས་པ་བཞིན་ནོ། །

[Block 1973]
དེ་བཞིན་དུ་དུས་ཕན་ཚུན་སྤངས་ནས་འཇུག་པ་ནི་དུས་ཀྱི་སྔ་ཕྱིར་འགྱུར་བ་ཡིན་ཏེ། གང་གི༌[^1448]ཚེ་གཅིག་མེད་པ་དེའི་ཚེ་གཞན་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1974]
དེ༌[^1449]ཡང་རྟག་པ་ལ་སོགས་པ་ལ་མ་ཡིན་ཏེ། ཐམས་ཅད་ཀྱི་ཚེ་ཐམས་ཅད་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1975]
རྣམ་པ་གཞན་ཡོད་པ་ཡང་མ་ཡིན་ན་ཡི་གེའི་སྔ་ཕྱིར་གྱུར་པའི་ངག་ཡིན་པ་དེ་ཇི་ལྟར་སྐྱེས་བུས་མ་བྱས་པར་སྒྲུབ།

[Block 1976 [VERSE]]
མི་རྟག་ཁྱབ་བྱེད་མ་ཡིན་པའི། །
སྐྱོན་ཡང་སྔར་ནི་བརྗོད་པ་ཡིན། །

[Block 1977]
ཅི་སྟེ་ཉེས་པ་དེར་མ་གྱུར་ཅིག་སྙམ་པས་ཡི་གེ་མི་རྟག་པ་དང་ཁྱབ་པར་བྱེད་པ་མ་ཡིན་པར་འདོད་ན། ཕྱོགས་དེ་ཡང་སྔར་གསལ་བའི་ཕྱིར་ལན་མ་ཡིན་ནོ། །

[Block 1978]
གསལ་བའི་གོ་རིམས་ཀྱང་ངག་མིན། །རྟག་པའི་གསལ་བ་གསལ་ཕྱིར་རོ། །

[Block 1979]
ཡི་གེའི་ངོ་བོའི་གོ་རིམས་ནི་ངག་མ་ཡིན་ནོ། །

[Block 1980]
འོ་ན་ཅི་ཡིན་ཞེ་ན། དེ་དག་གི་གསལ་བ་ཡིན་ནོ། །

[Block 1981]
དེ་ནི་བདག་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་ཡི་གེ་མངོན་པར་གསལ་བའི་རྐྱེན་གྱི་གོ་རིམས་ལས་འབྱུང་བའི་གོ་རིམས་དང་ལྡན་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1982]
དེའི་གོ་རིམས་ངག་ཡིན་ནོ་ཞེས་བྱ་བ་ཡང་ལོག་པ་ཡིན༌[^1450]ཏེ། རྟག་པ་དག་གི་དེ་ནི་སྔར་བཀག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1983]
མངོན་སུམ་དུ་ནུས་པ་ཉེ་བས་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་འབྲས་བུ་ཁྱད་པར་ཅན་ཉིད་གསལ་བ༌[^1451]ཡིན་ནོ་ཞེས་དེ༌[^1452]བཤད་པ་ཡིན་ནོ། །

[Block 1984 [VERSE]]
བྱེད་པ་རྣམས་ཀྱི་བྱ་ཉིད༌[^1453]ལས། །
དེ་གྲུབ་ཕྱིར་ན་འབྲས་ཉིད་ཡིན། །

[Block 1985]
གང་ཁོ་ན་ལས་ངོ་བོ་དམིགས་པ་གང་ཡིན་པ་དེ་ལ་དམིགས་པ་མེད་ན་མི་འབྱུང་བ་དམིགས་པ་ལ་བརྟེན་ནས་འཇིག་རྟེན་པ་དག་འབྲས་བུ་ཉིད༌[^1454]ཐ་སྙད་འདོགས་པར་བྱེད་དོ། །

[Block 1986]
དེ་ནི་ཡི་གེ་དག་ལ་ཡང༌[^1455]ཡོད་དེ། [^1456]དེ་ཉིད་ཀྱང་གཞན་དག་གི་ཡང་དེའི་རྟེན་ཡིན་པར་ཁྱད་པར་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1987]
དེ་བས་ན་ཁས་ལེན་པའི་རྒྱུ་མཚུངས་པ་ཡིན་ན་ཇི་ལྟར་ན་ཡི་གེ་འབྲས་བུ་དག་མ་ཡིན། དེ་དམིགས་པའི་རྟེན་ཅན་འབྲས་བུ་ཉིད་ཀྱི་ཐ་སྙད་མ་ཡིན་ནོ། །

[Block 1988]
འོ་ན་ཅི་ཡིན་ཞེ་ན། གང་ཡོད་ན་འགྱུར་བ་དེ་ལྟར་ན་ཡོད་པ་ཉིད་ཀྱི་རྟེན་ཅན་ཡིན་ནོ། །

[Block 1989]
ཡོད་པ་ཉིད་དེ་གང་ལས་གྲུབ་ན་གང་གིས༌[^1457]འབྲས་བུ་ཉིད་དུ་གྲུབ་པར་འགྱུར། འདི་མ་གྲུབ་པ་ནི་དེ་ལྟར་མི་འགྱུར་རོ། །

[Block 1990]
དེ་བས་ན་ཡོད་པ་ཉིད་དུ༌[^1458]གྲུབ་ན་དེ་གྲུབ་པར་བྱེད་པ་ཡིན་ལ་དེ་ཡང་དམིགས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1991]
དེ་ལྟར་ནི་བདེན་ན་གལ་ཏེ་དེ་ནི་སྔར་ཡོད་པ་ཉིད་དུ༌[^1459]གྲུབ་པར་མི་འགྱུར་ཏེ། ཡོད་པ་ཉིད་དུ་གྲུབ་པ་གང་ཡིན་པ་དེ་ནི་མ་གྲུབ་པ་སྔོན་དུ་སོང་བ་ཅན་ཡིན་ནོ། །

[Block 1992]
དེ་ལྟ་བུར་གྱུར་པའི་རྣམ་པར་ཤེས་པ་མ་ཆོད་པས་ཉེ་བར་སྦྱོར་བ་ཅན་གྱི་ངོ་བོ་གང་ཡིན་པ་དེ་མ་གྲུབ་པ་ཉིད་མ་ཡིན་ནམ། གལ་ཏེ་དེ་ནི་གྲུབ་པ་ཉིད་ཡིན་མོད་ཀྱི་གཞན་དང་བྲལ་བས་ཉེ་བར་སྦྱོར་བ་མ་ཡིན་ནོ་ཞེ་ན། ད་ནི་ཉེ་བར་སྦྱོར་བ་དང་ཉེ་བར་སྦྱོར་བ་མ་ཡིན་པའི་གནས་སྐབས་དག་ལ་ཇི་ལྟར་ན་ཐ་དད་པ་མེད། ཁྱད་པར་ནི་རང་བཞིན་ལ་མི་རེག་པའི་ངང་ཚུལ་ཅན་ཡང་མ་ཡིན་ཏེ། ཕུལ་དུ་བྱུང་བ་དེ་ཉིད་ལ་ཉེ་བར་སྦྱོར་བ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 1993]
དེ་ནི་རྒྱུ་མེད་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1994]
གང་ཁོ་ན་ཡོད་ན་བསྒྲུབ་བྱར་གྱུར་པ་དེ་ནི་དེ་ལ་ཉེ་བར་སྦྱོར་བ་ཅན་དུ་རིགས་པ༌[^1460]ཡིན་ནོ། །

[Block 1995]
ཕུལ་དུ་བྱུང་བ་དེ་ཉེ་བར་སྦྱོར་བ་ན་ཡང་འདི་ནི་དེ་དང་འདྲ་བའི༌[^1461]ཐལ་བར་འགྱུར་རོ། །

[Block 1996]
ནུས་པ་བར་དུ་མ་ཆོད་པས་ཉེ་བར་སྦྱོར་བ་ཅན་གྱི་གནས་སྐབས་ལས་ཐ་དད་པས་དེ་ལས་གཞན་པ་ཉིད་ཁྱད་པར་དུ་བྱེད་དོ། །

[Block 1997]
ཕུལ་དུ་དབྱུང་དུ་མེད་པ་ཅན་གྱི་ལྟོས་པ་ཡང་སྔར་བཀག་ཟིན་ཏོ། །

[Block 1998]
དེ་ཡང་བྱེད་པའི་བྱ་བ་ཉིད་ལས་གྲུབ་པའི་ཕྱིར། འབྲས་བུ་ཐམས་ཅད་དང་ཆོས་མཚུངས་པ་ཉིད་ཅན་ནོ། །

[Block 1999]
དེ་འདྲ་བ་དེ་གསལ་བ་ཡིན་ན་ཐམས་ཅད་གསལ་བྱའམ། ཅུང་ཞིག་ཀྱང་མ་ཡིན་ཏེ་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 2000]
དེ་ལྟར་ན་ནི།
--- END BLOCKS ---
