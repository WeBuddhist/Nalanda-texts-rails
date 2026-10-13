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
དཔེར་ན་སྔར་བཞིན༌[^1542]བྱས་པ་ལ་གཏན་ནས་བྱུང་བ་མ་ཡིན་པའི་ཕྱིར་བསྒྲུབ་པར་བྱ་བ་དང་གཏན་ཚིགས་ཀྱི་དོན་དག་ལ་བྱེ་བྲག་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་སོ། །

[Block 1962]
དེ་ལ་བརྗོད་པ། དེ་ལྟ་བུ་ཡང་མ་གྲུབ་པ་ལྟར་སྣང་བ་སྟེ། སྔ་ན་མེད་པ་སྐྱེས་པ་ལ་བསྒྲུབ་པར་བྱ་བ་ཉིད་དུ་སྒྲོ་བཏགས་ནས་བསྒྲུབ་པར་བྱ་བ་དང་གཏན་ཚིགས་སུ་བྱེ་བྲག་མེད་པར་མགོ་བསྒྲེ་བའི་ཕྱིར་རོ། །

[Block 1963]
གྲུབ་ན་ནི་སྔར་ནས་ཡོད་པ༌[^1543]ཞིག་ན༌[^1544]མེད་པ་བསྒྲུབ་པར་བྱའོ། །

[Block 1964]
གཞན་ཡང་བྱེ་བྲག་མེད་པར་མཚུངས་པ་བརྗོད་པར་བྱ་སྟེ། བརྩལ༌[^1545]མ་ཐག་ཏུ་བྱུང་བ་ཉིད་ནི་མི་རྟག་པ་བསྒྲུབ་པ༌[^1546]བཞིན་ཆོས་གཞན་ཡང་སྒྲུབ་པར་བྱེད་དོ་ཞེས་བྱ་བ་ནི་བྱེ་བྲག་མེད་པའོ། །

[Block 1965]
དེ་ལྟ་བུ་ཡང་བསྒྲུབ་པར་བྱ་བ་ལ་གནོད་པ་སྒྲུབ་པར་བྱེད་པ་ཉིད་ཀྱིས་ནི༌[^1547]འགལ་བ་ལྟར་སྣང་བའོ། །

[Block 1966]
བསྲེག་པར་བྱ་བ་ལ་སོགས་པ་མ་ངེས་པ་ཡིན་པའི་ཕྱིར་ཕྱོགས་གཅིག་ཏུ་ངེས་པ་ཉིད་འགལ་བར་རྩོད་པར༌[^1548]གལ་ཏེ་མཐོང་ན་གནོད་པར་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱའོ།[^1549] །

[Block 1967]
ཡང་བརྗོད་པ།

[Block 1968 [VERSE]]
བསྒྲུབ་བྱ་བ་ནི་གནོད་ཆོས་ཀྱང་། །
མཚུངས་པ་ཉིད་ཀྱི༌[^1550]བྱེ་བྲག་མེད། །
གཏན་ཚིགས་སྐྱོན་ལ་འགལ་ལྟར་སྣང་།[^1551] །
སྐྱོན་ཡོད་མིན་ཏེ་ཕྱོགས་ཕྱི་མ། །

[Block 1969]
དེ་དག་ནི་ཆོས་ཉིད་ཆོས་མཐུན་པ་མཚུངས་པ་ལ་སོགས་པ་ཕྱོགས་ཕྱི་མའོ། །

[Block 1970]
གལ་ཏེ་ཕྱོགས་ཕྱི་མ་ལས༌[^1552]ཕྱོགས་གཅིག་ཏུ་ངེས་པར་ཆོས་མཐུན་པ་ལ་སོགས་པས་ཕྱོགས་གཅིག་ཏུ་ངེས་པས་འགལ་བར་འགྱུར་རོ། །

[Block 1971]
ཕྱོགས་སྔ་མ་ལ་ནི་ཇི་སྐད་དུ་བརྗོད་པའི་མ་ངེས་པ་དང་ལྡན་པས་དེ་སུན་བཏོན་པ་དང་། སྒྲུབ་པའི་སྒོ་ནས་འགལ་བ་དང་མ་ངེས་པ་བསྒྲུབ་པར་བྱ་བ་ལ་གནོད་པར་བརྩད་པའི་ཕྱིར་དེ་དག་ནི་སུན་འབྱིན་གཞན་ཉིད་ཡིན་ནོ། །

[Block 1972]
གལ་ཏེ་གནོད་པར་མི་བྱེད་པར༌[^1553]མཐོང་སྟེ། དཔེར་ན་འགལ་བ་ཁ་ཅིག་ནི་བརྩལ༌[^1554]མ་ཐག་ཏུ་བྱུང་བ་ཉིད་མི་རྟག་པ་ཉིད་ལས༌[^1555]མི་འཁྲུལ་བ་དེ་བཞིན་མཉན་བྱ་མ་ཡིན་པ་ཡང་ངོ་། །

[Block 1973]
དེ་བཞིན་དུ་སྒྲ་མཉན་བྱ་མ་ཡིན་ནོ་ཞེས་དེ་ཡང་བརྗོད་པར་བྱའོ། །

[Block 1974]
དེ་ལྟར་འདིར་མཉན་བྱ་ཉིད་ལ་གནོད་པ་ནི་མཐོང་གི །སྒྲ་རྟག་པ་ཉིད་ནི་མ་མཐོང་ངོ་། །གང་ལས་མི་རྟག་པ་ཉིད་འཐོབ་པའི་རྗེས་སུ་དཔག་པར༌[^1556]འཇུག་པར་བྱེད། དམ་བཅའ་བའི་སྐྱོན་ཉིད་ཀྱིས་སྔ་མ་ལ༌[^1557]མཉན་བྱ་མ་ཡིན་པ་ཉིད་མི་འགྲུབ༌[^1558]བོ། །

[Block 1975]
གང་ལ་ཕྱོགས་གཅིག་ཏུ་ངེས་པ་མཐོང་ན་ནི་གནོད་པ་མེད་དེ། ཇི་ལྟར་རྡུལ་གཉིས་པ་ནི་རྡུལ་གཅིག་སྔོན་དུ་སོང་བ་ཡིན་ཏེ། རགས་པ་ཡིན་པའི་ཕྱིར་བུམ་པ་ལ་སོགས་པ་བཞིན་ཞེས་བྱས་ནས་རྡུལ་ཕྲ་རབ་རྣམས་ཀྱིས་རགས་པ༌[^1559]ཉིད་ཀྱང་བསྒྲུབ་པ༌[^1560]བཞིན་ནོ། །

[Block 1976]
བུམ་པ་ལ་སོགས་པ་རྣམས་ཀྱི༌[^1561]སྔོན་དུ་རྡུལ་རགས་པ་སོང་བ་ཡིན་པའི་ཕྱིར་དེ་ལ་ལན་གང་ཞིག་ཡོད། །

[Block 1977]
བསྒྲུབ་བྱ་ལ་གནོད་བསྒྲུབ་པའི༌[^1562]ཕྱིར། །གནོད་པ༌[^1563]བྱེད་པ་འགལ་ཉིད་མིན། །

[Block 1978]
བསྒྲུབ་བྱ་ལ་ནི་འདིར་ཆོས་སམ་ཆོས་ཅན་ཡང་རུང་སྟེ། དེ་ལ་གནོད་པ་གྲུབ་ན་དེ་འགལ་བ་ཉིད་ཡིན་ནོ། །

[Block 1979 [HEADING]]
### དམིགས་པ་མཚུངས་པ། ^6-10-0

[Block 1980 [VERSE]]
བསྒྲུབ་བྱ་ལས་གཞན་གཏན་ཚིགས་ཀྱིས། །
བསྟན་ན་དམིགས་པ་མཚུངས་པའོ། །

[Block 1981]
གང༌[^1564]བསྒྲུབ་པར་བྱ་བ་ལས་གཞན་ཡང་གཏན་ཚིགས་ཀྱིས་ཉེ་བར་བསྟན་པ་དེ་ནི༌[^1565]དམིགས་པ་མཚུངས་པའོ། །

[Block 1982]
དཔེར་ན་སྔ་མ༌[^1566]བཞིན་དུ་མི་རྟག་པར་བསྒྲུབ་པ༌[^1567]ལ་གཏན་ཚིགས་འདི་གློག་ལ་སོགས་པ་ལ་ཡོད་པ༌[^1568]མ་ཡིན་ཞིང་འདི་ལས་མངོན་སུམ་ལ་སོགས་པས་མི་རྟག་པ་གྲུབ་པོ། །གལ་ཏེ་དེ་མེད་ཀྱང་དེའི་རྒྱུར་འགྱུར་བ་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1983]
གཞན་དེ་ལས་གཞན་དུ་སྦྱོར་བར་བྱེད་དོ། །

[Block 1984]
འདི་མི་རྟག་པའི་གཏན་ཚིགས་མ་ཡིན་ཏེ། ཁྱབ་པ་མེད་པའི་ཕྱིར་ནགས་ཀྱི་ཤིང་ནུབ་མོ་ཉལ་བ་ལས་སེམས་པ་དང་ལྡན་པ་བཞིན་ནོ་ཞེས་སོ། །

[Block 1985]
འདི་ལ་ཡང་།

[Block 1986]
བསྒྲུབ་བྱ་དུ་མ་བཀོད་པ་ལས། །གཏན་ཚིགས་དེ་དང་རྗེས་མཐུན་ཉིད། །

[Block 1987]
གལ་ཏེ་གཏན་ཚིགས་གཞན་གྱིས་རྟག་པར་གྲུབ་དེ་ལྟ་ན་ནི་མི་རྟག་པའི་འཁྲུལ་པ་ཡིན་པས་གཏན་ཚིགས་གཞན་གྱིས་སྒྲུབ་པོ། །གཏན་ཚིགས་ནི་མ་ཡིན་ནོ།[^1569] །

[Block 1988]
དེ་ནི་མི་རྟག་པ་མེད་པར་མཐོང་བར༌[^1570]མེད་དོ། །བྱེད་པ་པོའི་རྒྱུ་ལས་གཞན་གྱི་འབྲས་བུ་སྒྲུབ་པོ། །

[Block 1989]
དེའི་གཏན་ཚིགས་ཉིད་དུ་མ་གྱུར་པའི་ཕྱིར་ཤེས་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1990 [VERSE]]
དེའི་ཕྱིར་མ་ངེས་པ་ལྟར་སྣང་བའོ། །
གཏན་ཚིགས་ཀྱིས་ནི་མ་ཁྱབ་ཀྱང་། །
བསྒྲུབ་བྱའི་དངོས་པོ་རྟོགས་པའི་ཕྱིར། །
མ་གྲུབ་ལྟར་སྣང་སྒྲར་གནས་ཀྱིས། །

[Block 1991]
ཐམས་ཅད་རབ་ཏུ་སྒྲུབ་པ༌[^1571]ཡིན། །གང་མ་ཁྱབ་པའི་སྒྲུབ་བྱེད་མ་ཡིན་ནོ་ཞེས་བརྗོད་པ་ལ། དེ་མི་རྟག་པ་ལས་གཞན་ལ་གཏན་ཚིགས་མི་སྲིད་ཅིང་། སྒྲ་ལ་མེད་པ་ཡང་མ་ཡིན་པ་ལ་མེད་པར་བཏགས་པའི་ཕྱིར་མ་གྲུབ་པ་ལྟར་སྣང་བ་སྟེ། བསྒྲུབ་བྱ་ཁོ་ན་ལ་མེད་པ་ཡིན་པའི་ཕྱིར་སུན་འབྱིན་པ་ཡིན་ནོ། །

[Block 1992]
གཏན་ཚིགས་དེ་སྒྲ་ལ་མེད་པ་ཡང་མ་ཡིན་ལ་སྒྲ་ལ་ཡོད་པས་ཐམས་ཅད་ཀྱིས་བསྒྲུབ་བྱ་སྒྲུབ་པ་ཡང་མ་ཡིན་ཏེ། [^1572]ཇི་ལྟར་སྦྲུལ་ལ་སོགས་པ་ལ་ཡོད་པའི་མཚན་མོ་ཉལ་བས་ན་ནགས་ན་གནས་པ་སེམས་པ་དང་བཅས་པར་བསྒྲུབ་པ་བཞིན་ནོ། །

[Block 1993 [HEADING]]
### ཐེ་ཚོམ་མཚུངས་པ། ^6-11-0

[Block 1994]
ཐེ་ཚོམ་བརྗོད་འདོད་ཐ་དད་ལས། །གཏན་ཚིགས་ཐེ་ཚོམ་རྩོད་པར་བྱེད། །

[Block 1995]
གང༌[^1573]དུ་དམ་བཅས་པའི་དོན་བཏགས་པས་གཏན་ཚིགས་འཁྲུལ་པའི་ཕྱིར་ཐེ་ཚོམ་དུ་བརྗོད་དོ། །

[Block 1996]
གཏན་ཚིགས་ཀྱི་དོན་རྟག་པ༌[^1574]ལས་ཀྱང་ཐེ་ཚོམ་མཚུངས་པའི་ལྟག་སྤྱོད༌[^1575]ཡིན་ནོ། །

[Block 1997]
དཔེར་ན་སྔར་བཞིན་བྱས་པ་ལ་བརྩལ༌[^1576]མ་ཐག་ཏུ་བྱུང་བ་བསལ་བ་དང་། སྐྱེས་པ་མཐོང་བ་ལས་ཐེ་ཚོམ་དུ་འགྱུར་ཏེ། ཅི་འདི་གསལ་བར་བྱ་བ༌[^1577]ཡིན་ནམ། བསྐྱེད་པར་བྱ་བ་ཡིན་ཞེས་སོ། །

[Block 1998]
འདི་རིགས་པ་མ་ཡིན་ཏེ། གང་གཏན་ཚིགས་དེ་དག་ལས་མི་རྟག་པའོ་ཞེས་པ་དེའི་ལྟ༌[^1578]ན། བསྒྲུབ་བྱ་སྒྲོ༌[^1579]བཏགས༌[^1580]མ་ངེས་པ། །ལྟར་སྣང་། འདི་བརྩལ་མ་ཐག་ཏུ་བྱུང་བ་དམིགས་ནས་འཇིག་པ་ཉིད་དུ་སྒྲུབ་པ་ལ་གང་ཞིག་དེ་ལྟར་སྒྲོ་འདོགས་ན་མི༌[^1581]རྟག་པ་བསྐྱེད་པར་བྱ་སྟེ། དེ་ལ་ཡང་མ་ངེས་པ་ཡིན་པའི་ཕྱིར་ཐེ་ཚོམ་ཡིན་ནོ། །

[Block 1999]
འདི་ལྟར་བརྩལ་མ་ཐག་ཏུ་བྱུང་བ་དམིགས་པ་བསལ་བ་ནི་རྩྭ༌[^1582]དང་ཆུ་ལ་སོགས་པ་ལ་ཡོད་པས་དེ་མ་ངེས་པ་ལ་སྣང་བ་སྟེ། འཇིག་པ་བསྒྲུབ་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2000]
གསལ་བ་རྣམས་ལ་ཡང་འཇིག་པ་ཉིད་ཡོད་པ་སྟེ། དེའི་ཕྱིར་མ་ངེས་པ་ལྟར་སྣང་བའོ། །
--- END BLOCKS ---
