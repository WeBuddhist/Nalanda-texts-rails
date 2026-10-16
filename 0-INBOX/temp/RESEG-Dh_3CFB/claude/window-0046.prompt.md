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
[Block 1611]
འབྲེལ་པ་དེས་འབྲེལ་པ་མེད་པའི་དོན་རྟོགས་པར་རིགས་པ་མ་ཡིན་ཏེ། དེ་ནི་དོན་མེད་པ་ཅན་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1612]
འདོད་པའི་དབང་གིས་བརྡར་བྱས་པ་ཅན་ཐམས་ཅད་ཀྱི་ཐམས་ཅད་གསལ་བར་བྱེད་པ་ཡང་མཐོང་ངོ་། །

[Block 1613 [VERSE]]
དོན་དུ་མ་དང་མངོན་འབྲེལ་ན། །
འགལ་བ་གསལ་བར་བྱེད་པ་སྲིད། །

[Block 1614]
ཅི་སྟེ་མཐོང་བ་འགལ་བར་མ་གྱུར་ཅིག་སྙམ་པས་ཐམས་ཅད་ཐམས་ཅད་ཀྱི་རྗོད་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1615]
དེ༌[^1196]ལྟར་ན་ཐམས་ཅད་ཐམས་ཅད་ཀྱི་སྒྲུབ་པར་ནི་མ་ཡིན་ཏེ། རྒྱུ་དང་འབྲས་བུ་དག་ནི་འཆོལ་བ་མེད་པའི་ཕྱིར་རོ།[^1197] ། དེ་ལས་སོ་སོར་ངེས་པར་བྱེད་པ་སྒྲུབ་པ་ཅན་གྱི་མངོན་པར་འདོད་པའི་དོན་ལ་བསྒྲུབ་པར་བྱ་བ་དང་། སྒྲུབ་པར་བྱེད༌[^1198]པ་ཐམས་ཅད་ཀྱི་ཐུན་མོང་གི་སྒྲ་ནི་འདོད་པའི་དོན་གསལ་བར་བྱེད༌[^1199]པས་བྱས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་གང་ལས་ཡིན། དེ་མ་ངེས་པ་ངེས་པ་སྐྱེས་བུ༌[^1200]ལས་མཐོང་བར་འགྱུར་བ་དེའི་ཚེ། སྐྱེས་བུས་མ་བྱས་པ་ཉིད་ཀྱི་ཀུན་ཏུ་རྟོག་པའང་དོན་མེད་འགྱུར། ཇི་ལྟར་ཡང་དོན་མ་འཆོལ་བ་རྟོགས་པའི་ཕྱིར་སྐྱེས་བུ་རྒྱུར་འཆོལ་བ་གསལ་བ་ཡིན་ནོ། །

[Block 1616]
དེ་ལ༌[^1201]སྐྱེས་བུ་རྣམས་ཀྱི་ཅི་འདྲ་བ་དག་འགའ་ཞིག་ལ་རབ་ཏུ་སྦྱོར་བ་འཆོལ་བར་འགྱུར་རོ། །

[Block 1617]
དེ་འདྲ་བ་ཉིད་ཐམས་ཅད་དང་ཐུན་མོང་དུ་གྱུར་པ༌[^1202]ཡོད་ན། འགའ་ཞིག་ལ་དེ་རྣམས་ཀྱིས་ངེས་པར་བྱས་པ་ཡིན་ཏེ། དེ་ཁོ་ན་ཉིད་ཡོངས་སུ་ཤེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1618]
གལ་ཏེ་རིག་བྱེད་པའི་ངོ་བོ་ཉིད་ཀྱིས་ངེས་པ་ཡིན་ནོ་ཞེ་ན། བསྟན་པ་ལ་རག་ལས་པ་མེད་པར་འགྱུར་བ་དང་། བརྡ་རྣམ་པ་གཞན་གྱིས་སྟོན་པར་མི་འགྱུར་བ་དང་། འཆད་པའི་རྣམ་པར་རྟོག་པར་མི་འགྱུར་རོ། །

[Block 1619]
རྣམ་པར་རྟོག་པར་ནུས་པ་ཅན་ཡོད་ན་སྟོན་པའི་འདོད་པ་ལ་མི་སླུ་བ༌[^1203]མེད་པའི་ཕྱིར་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་ནི་དོན་མེད་པ་ཅན་ཉིད་དུ་འགྱུར་རོ། །

[Block 1620 [VERSE]]
ཐ་དད་རྣམས་ཀྱི་འབྲེལ་པ་ཡང་། །
རྣམ་པར་གཞག་ཕྱིར་གཏན་ཚིགས་བརྗོད། །

[Block 1621]
ཕྱི་རོལ་གྱི་དོན་ནི་སྒྲའི་ངོ་བོ་མ་ཡིན་ཞིང་། །སྒྲ་ནི་དོན་རྣམས་ཀྱི་མ་ཡིན་ཏེ། ཐ་དད་པ་མེད་པའི་བདག་ཉིད༌[^1204]གང་གིས་གནས་སྐབས་ཐ་དད་པ་ཡང་བྱས་པ་དང་མི་རྟག་པ་དང་འདྲ་བ་མེད་ན་མི་འབྱུང་བ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1622]
སྒྲ་དེ་དག་ཀྱང་བརྗོད་པར་འདོད་པ་ལས་སྐྱེ་བ་ཅན་ནམ། སྐྱེ་བ་མེད་པ་ཅན་བརྗོད་པར་འདོད་པས་གསལ་བར་བྱ་བ་དག་མ་ཡིན་ཞིང་དོན་ལ་རག་ལས་པ་མ་ཡིན་ནོ། །

[Block 1623]
དེ་བས་ན་དེ་ལ༌[^1205]སོ་སོར་ངེས་པར་བསྒྲུབ་པར་བྱ་བ་དེའི་རྗེས་སུ་འགྲོ་བ་ཇི་ལྟར་སྒྲུབ་པར་བྱེད་པར༌[^1206]འགྱུར་ཏེ། རག་ལས་པ་མེད་པ་དེའི་ནི་སྒྲུབ་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1624 [VERSE]]
སྐྱེས་བུས་ལེགས་པར་མ་བྱས་པས། །
རྣམ་པ་ཀུན་དུ་དོན་མེད་འགྱུར། །
ལེགས་བྱས་ཁས་ལེན་ན་འདི་ཡི། །
དངོས་སུ་གླང་པོ་ཁྲུས་འདྲར་འགྱུར། །

[Block 1625]
ཞེས་བྱ་བ་ནི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 1626]
གཞན་ཡང་སྒྲ་དང་དོན་དག་གི་འབྲེལ་པ་རྟག་པའམ་མི་རྟག་པར་འགྱུར། གལ་ཏེ་མི་རྟག་པ་སྐྱེས་བུས༌[^1207]འདོད་པས་འཇུག་པ༌[^1208]ཅན་ནམ། མི་འཇུག་པ་ཅན་ཡིན་གྲང༌[^1209]ན། སྐྱེས་བུ་ལ་རག་ལས་པ་ཉིད་མ་ཡིན་ན་སྐྱེས་བུའི་བསམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཡུལ་ལ་སོགས་པར་གྱུར་པ་དེར་སྟོན་པར་མི་འགྱུར་ཏེ། འདོད་པ་ལ་རག་ལུས་པ་མེད་པ་ཡང་རི་བོ་ལ་སོགས་པ༌[^1210]དང་འདྲ་བར་འགའ་ཞིག་ཏུ་ཡང་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1627]
འདི་ཉིད་ནི་རྟག་པ་ཉིད་ལ་ཡང་སྐྱོན་ཡིན་ཏེ། དེའི་རྟག་པ༌[^1211]ངོ་བོ་གཞན་དུ་གྱུར་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1628]
གནས་སྐབས་ཐམས་ཅད་ལ་ཡང་མཚུངས་པ་ཡིན་ཏེ། འདོད་པ་ལ་སོ་སོར་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1629]
དེ་ལས་ཁྱད་པར་རྟོགས་པ་མི་འགྱུར་བའི་ཕྱིར།

[Block 1630 [VERSE]]
སྔ་མ་བཞིན་དུ་ཐལ་བར་འགྱུར་རོ། །
འདོད་པས་འཇུག་པ་ཡིན་ན་ཡང་། །

[Block 1631]
སྐྱེས་བུས་བྱས་པ་ཉིད་ཡིན་པའི་ཕྱིར་འཁྲུལ་པར་དོགས་པར༌[^1212]འགྱུར་རོ། །

[Block 1632]
གཞན་ཡང་།

[Block 1633 [VERSE]]
འབྲེལ་པ་ཅན་རྣམས་མི་རྟག་ཕྱིར། །
འབྲེལ་པ་ལ་རྟག་ཡོད་མ་ཡིན། །

[Block 1634]
གཞན་ལ།[^1213] རྟེན་པ་ཅན་འབྲེལ་པ་ཡིན་ན་ནི་རག་ལས་པ་མེད་པ་ལ་དེ་དག་གི༌[^1214]འབྲེལ་པ་ཉིད༌[^1215]མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1635]
རྟེན་དེ་ཡང་མི་རྟག་པ་ཡིན་ཏེ། དེ་ཞིག༌[^1216]ན་འབྲེལ་པ་ཡང་ཞིག་པར་འགྱུར་རོ། །

[Block 1636]
དེ་ལྟ་མ་ཡིན་ན་ཞིག་པར་མི་འགྱུར་རོ། །

[Block 1637]
དེ་བས་ན་རྟག་པ་མ་ཡིན་ནོ། །

[Block 1638]
དེའི་རྟེན་གྱི་དོན་ཡང་བརྗོད་པར་བྱ་སྟེ། རྟག་པ་ལ་ཕན་གདགས་སུ་བྱར་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1639]
ཕན་འདོགས་པར་མི་བྱེད་པ་ཡང་རྟེན་མ་ཡིན་ནོ། །

[Block 1640]
གལ་ཏེ་རིགས་བརྗོད་པར་བྱ་བ་ཉིད་ཡིན་པའི་ཕྱིར་སྐྱོན་མེད་དོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་བརྗོད་པ་ལ་དགོས་པ་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བས་དེ་དཔྱད་ཟིན་ཏོ། །

[Block 1641]
ཐམས་ཅད་དུ་ཡང་རིགས་མེད་པའི་ཕྱིར་འདོད་རྒྱལ་ཉིད་གསལ་བར་བརྗོད་པ་རྣམས་ལ་མི་རུང་བ་དང་། རྣམ་པ་ཐམས་ཅད་དུ་རིགས་བརྗོད་པ་ན་ཁྱད་པར་གཞན་སྤངས་ནས་འཇུག་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1642]
དེའི་ཕྱིར་དེའི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་ཅན་གྱི་དངོས་པོའི་ཡོད་པ་དང་མེད་པ་ནི་འབྲེལ་པ་ཡིན་ནོ། །

[Block 1643 [VERSE]]
དེའི་ཕྱིར་དོན་དང་སྒྲ་ཡི༌[^1217]དེ། །
སྐྱེས་བུས་བློ་ཡིས་ལེགས་པར་བྱས། །

[Block 1644]
ཡོད་པ་དང་མེད་པ་དེ་དག་ལ་བརྟེན་ནས་མ་འདྲེས་སུ་ཟིན་ཀྱང་ཐ་སྙད་ལ་གོམས་པ་ལས་སྐྱེས་བུ་ལ་འདྲེས་པར་སྣང་བའི་ཕྱིར། དངོས་པོ་རྣམས་ཀྱི་འདྲེས་པ་ནི་སྐྱེས་བུས་བྱས་པ་ཡིན་ནོ། །

[Block 1645]
གཞན་ཡང་རྟེན་ཞིག་པ་ལ་འབྲེལ་པ་ཞིག་པར་འགྱུར་ན། སྒྲ་དེ་ཡང་སྔ་ན་མེད་པ་དང་འབྲེལ་པ་མ་ཡིན་ཏེ། འབྲེལ་པ་ཅན་ཉིད་མེད་པའི་ཕྱིར་དང་། སྐྱེས་ཤིང་འགྱུར་བའི་དངོས་པོ་འབྲེལ་པ་ཅན་མ་ཡིན་པ་རྣམས་ནི་བརྗོད་པར་བྱ་བ་མ་ཡིན་པར་འགྱུར་ཏེ། འབྲེལ་པ་གནས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 1646]
དེ་ལ་ཡང་དོན་དང་ལྷན་ཅིག་སྐྱེས་པ་མ་རྟོགས་པར་གྱུར༌[^1218]ན།

[Block 1647 [VERSE]]
སྒྲ་རྣམས་ལ་ནི་རང་བཞིན་དག །
[^1219]རྣམ་པར་བཟློག་པ་མི་རིགས་སོ། །

[Block 1648]
ཅི་སྟེ་འབྲེལ་པ་ཞིག་པ་དོན་གཞན་ལ་མེད་པའམ། དོན་རྣམས་བརྗོད་པར་བྱ་བ་མ་ཡིན་པར་མ་གྱུར་ཅིག་སྙམ་པས། གལ་ཏེ་སྐྱེས་ཤིང་བྱུང་བའི་དོན་འབྲེལ་པ་དང་ལྡན་པ་སྐྱེ་བར༌[^1220]འགྱུར་ན། འབྲེལ་པ་དེ་སྐྱེས་སུ་ཟིན་ཀྱང་སྒྲ་ལ་མི་འགྱུར་ཏེ། དེ་དང་འབྲེལ་པ་མེད་པ་ཅན་གྱི་རང་བཞིན་ནི་རང་བཞིན་བཟློག་པ་མེད་པར་དེའི་ངོ་བོ་མི་རུང་བའི་ཕྱིར་དང་། དོན་དང་ལྷན་ཅིག་སྐྱེས་པ་གཞན་ལས་གྲུབ་པ་ཡང་སྒྲ་ཕན་འདོགས་པ་མེད་པ་ལ་མི་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 1649]
དེ་ཡང་དེ་སྐྱེད་པར་བྱེད་པའི་ལྷན་ཅིག་བྱེད་པ་ཉིད་ཡིན་ན་ནུས་པ་ནི་རྟག་ཏུ་བསྐྱེད་པར་ཐལ་བར་འགྱུར་ཏེ། ལྟོས་པ་མེད་པའི་ཕྱིར་ཏེ། རྟག་པ་ལ་ཕན་གདགས་སུ་མེད་པའི་ཕྱིར་རོ། །

[Block 1650]
ནུས་པ་མེད་པ་ཡིན་ན༌[^1221]ཡང་ཕྱིས་ཀྱང་ནུས་པ་མ་ཡིན་ཏེ།
--- END BLOCKS ---
