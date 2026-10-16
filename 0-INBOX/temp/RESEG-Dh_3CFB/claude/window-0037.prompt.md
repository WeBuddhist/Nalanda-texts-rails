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
[Block 1296]
གཙོ་བོ་ལ་སོགས་པའི་སྒྲ་བརྗོད་པའི་དོན་འགའ་ཞིག་ཀྱང་མེད་པའི་ཕྱིར་དེ་ནི་ཁྱད་པར་མེད་པ་ཅན་ཁོ་ན་ཡིན་ནོ། །

[Block 1297]
ཇི་ལྟར་མེད་པ་ཡིན་ཏེ། ཤེས་བྱ་དང་བརྗོད་པར་བྱ་བ་དང་གཞལ་བྱ་དག་ཏུ་དེ་ཡང་གྲུབ་པ་ཁོ་ན་ཡིན་ནོ་ཞེ་ན། [^1009]དེ་བས་ན་ད་ཅི་ཤེས་བྱ་ཡོད་ཅེས་བྱ་བས་གྲུབ་པ་ཡིན་ཡང་བླ་སྟེ། དེ་ལྟར་ན་ཡང་ཅི་ཞིག་འགྲུབ་པར་འགྱུར། གཞན་དུ་མེའི་སྤྱི་དེ་ཉིད་དེ་ལ་མ་གྲུབ་པའི་ཕྱིར་བསྒྲུབ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1298]
དེ་ལ་ཡང་དེ་དང༌[^1010]མི་ལྡན་པ་བྲལ་བ་ཅན་གྱི་སྤྱིས་རྗེས་སུ་འགྲོ་བ་མ་གྲུབ་པ་ཁོ་ན་མ་ཡིན་ནམ། འགའ་ཞིག་དེ་ལྟ་བུར་གྱུར་པའི་དོན་གྱི་རྗེས་སུ་འགྲོ་བར་བྱེད་པ་མ་ཡིན་གྱི། གཞན་ལ་ཁོང་དུ་ཆུད་པར་བྱེད་པས་ནི་དུ་བས་ནི་གང་ན་དུ་བ་ཡོད་པ་དེ་ནི༌[^1011]མེ་ཡོད་དོ་ཞེས་མེ་མེད་ན་མི་འབྱུང་བར་བསྟན་པར་བྱ་བ་ཡིན་ནོ། །

[Block 1299]
དེ་ལྟར་ན་དེ་མེ་ཙམ་གྱིས་ཁྱབ་པར་གྲུབ་པས་གང་ན་བདག་ཉིད་སྣང་བར་འགྱུར་པ་དེ་ཉིད་དུ་མེའི་བློ་སྐྱེད་པར་བྱེད་དོ། །

[Block 1300]
དེ་ལ་སྒྲུབ་པར༌[^1012]བྱེད་པ་བསྟན་པས་ཅིར་ཡང་མི་རུང་སྟེ། དེ་ལ་མཐོང་བ་དང་འབྲེལ་པ་བསྟན་པ་ཙམ་གྱིས་འདོད་པ་འགྲུབ་པའི༌[^1013]ཕྱིར་རོ། །

[Block 1301]
དེ་མ་བསྟན་པར་ཡང་ཇི་ལྟར་དེ་ཁྱད་པར་དུ་བྱས་པ་དང་རྗེས་སུ་འགྲོ་བ་ཡིན་ཏེ། དེ་བས་ན་འདི་ནི་མེ་མེད་ན་མི་འབྱུང་བར་གྲུབ་པ་ཡིན་ཏེ། དོན་གྱིས་མེ་ནི་ཕྱོགས་དེར་མི་ལྡན་པ་རྣམ་པར་བཅད་པ་ཡིན་པའི་ཕྱིར། དེ་ནི་དེ་ལྟར་བསྒྲུབ་པར་བྱ་ཞེས་བྱའོ། །

[Block 1302]
འདི་ལྟར་ཉེ་བར་དགོད་པ་སྔོན་དུ་འགྲོ་བ་ཅན་གྱི་རྗེས་སུ་འགྲོ་བ་མ་ཡིན་ཏེ། བསྒྲུབ་བྱ༌[^1014]བསྟན་པར་འདིར་ཡན་ལག་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1303]
དེ་སྔོན་དུ་སོང་བ་ཅན་ལ་དམ་བཅས་པ་སྒྲུབ་པར་བྱེད་པས་ཅི་ཞིག་སེལ་བར་བྱེད། དེ་སྐད་དུ་ཡང་།

[Block 1304 [VERSE]]
གཞན་ལ་ཆོས་དང་གཏན་ཚིགས་ནི། །
མ་འཁྲུལ་པར་ཡང་བསྟན་པ་ན། །
དེ་ལ་རབ་གྲུབ་དེ་ལྡན་པའི། །
ཆོས་ཅན་ཁོང་དུ་ཆུད་པར་བྱེད། །

[Block 1305]
ཅེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1306]
དེ་བས་ན་མེ་ལ་སོགས་པ་སྒྲུབ་པར་བྱེད་པ་དང་འདྲ་བར་ཡོད་པ་ཉིད་སྒྲུབ་པར་བྱེད་པ་ཡང་ཁ་ན་མ་ཐོ་བ་མེད་པ་མ་ཡིན་ནོ། །

[Block 1307 [VERSE]]
དེ་ཁྱད་གཟུང་བ་མེད་པ་ཅན། །
དངོས་པོ་ཙམ་ནི་སྒྲུབ་ཡིན་ན། །
དེ་ཙམ་ཁྱབ་བྱེད་བསྒྲུབ་བྱ་ལ། །
རྗེས་སུ་འགྲོ་བ་འགལ་བ་མེད། །

[Block 1308]
རང་གི་ངོ་བོའི་ཁྱད་པར་ཡོངས་སུ་གཟུང་བ་མེད་པར་སྒྲུབ་པར་བྱེད་པ་ཡོད་པ་ཉིད་ཡིན་ན་ཡང་དངོས་པོ་ཙམ་ཁྱབ་པར་བྱེད་པ་བསྒྲུབ་པར་བྱ་བའི་ཆོས་ལ་རྗེས་སུ་འགྲོ་བ་འགལ་བ་མེད་དེ། དེ་ལ་གདོན་མི་ཟ་བར་ཁྱད་པར་ཡོངས་སུ་གཟུང་བར་བྱ་བ་མ་ཡིན་ཏེ། ཡོད་པ་ཙམ་ལ་བརྟེན་པ་ལ་ཡང་སྒྲུབ་པར་བྱེད་པར་ནུས་པའི་ཕྱིར་དང་བསྒྲུབ་པར་བྱ་བ་ཉིད་ནི་མ་ཡིན་ཏེ། འབྲས་བུ་མེད་པའི་ཕྱིར་རོ། །

[Block 1309]
གཞན་ཡང་།

[Block 1310 [VERSE]]
མ་གྲུབ་པ་ལ་ཡོད་ཆོས་མེད། །
གཉི་ག་ལ་བརྟེན༌[^1015]འཁྲུལ་པ་དང་། །
མེད་པའི་ཆོས་ནི་འགལ་ཡིན་ན། །
ཇི་ལྟར་ཡོད་ཉིད་དེ༌[^1016]སྒྲུབ་འགྱུར། །

[Block 1311]
ཡོད་པ་ཉིད་བསྒྲུབ་པར་བྱ་བ་ལ་གཏན་ཚིགས་དེ་ཐམས་ཅད་ནི། སྐྱོན་ནི་རྣམ་པ་གསུམ་དང་ལྡན་ཏེ། མ་གྲུབ་པ་དང་འཁྲུལ་པ་དང་འགལ་བ་ལས་མ་འདས་པ་ཡིན་ནོ། །

[Block 1312]
དེ་ལ་གལ་ཏེ་གཏན་ཚིགས་ཡོད་པའི་ཆོས་ཞིག་སྟོན་ན་ནི་དེ་ཇི་ལྟར་ཡོད་པ་ཉིད་མ་གྲུབ་པ་ཅན་དུ་འགྱུར། གང་ཞིག་དེར་ཡོད་པའི་ཆོས་འདོད་ན་དེ་ཇི་ལྟར་དངོས་པོར་མི་འདོད། རང་བཞིན་ཉིད་ནི་འགའ་ཞིག་ལ་ལྟོས་ནས་ཆོས་ཤེས༌[^1017]ཆོས་ཅན་ལ༌[^1018]ཐ་དད་པ་ཅན་བཞིན་དུ་བསྟན་པ་ཡིན་ཏེ། ཆོས་དང་ཆོས་ཅན་བརྗོད་པའི་སྒྲ་དག་གི་བརྗོད་པར་བྱ་བའི་དོན་ལ་ངེས་པའི་ཤེས་པའི་ཡུལ་ཉིད་དུ་ཁྱད་པར་འགའ་ཡང་མེད་དོ་ཞེས་བྱ་བ་དེས་བཤད་ཟིན་ཏོ། །

[Block 1313]
ཇི་སྟེ་ཡང་གཉི་གའི་ཆོས་ཡིན་པར་སྨྲ་ན་དངོས་པོ་ལ་མི་བརྟེན་པ་ཅན༌[^1019]མ་ཡིན་པར་དགག་པ༌[^1020]མ་ཡིན་པས་ལྡོག་པ་ཙམ་ནི་མེད་པ་ལ་ཡང་འགལ་བ་མེད་པའི་ཕྱིར་ཏེ། དཔེར་ན་གཟུགས་ཅན་དུ་མི་འགྱུར་རོ་ཞེས་བྱ་བ་གཟུགས་ཅན་མ་ཡིན་པ་ཉིད་ནི་ཉེ་བར་བརྗོད་པ་མེད་པ་ལ་ཡང་འགྱུར་བ་ལྟ་བུའོ། །

[Block 1314]
གལ་ཏེ་ཉེ་བར་བརྗོད་པ་མེད་པ་ནི་དངོས་པོ་མེད་པའི་ཕྱིར། དགག་པའི་ཡུལ་ཉིད་མ་ཡིན་ནོ་ཞེ་ན། དེ་བས་ན་ད་ཅི་བསྒྲུབ་པར་བྱ་བའི་ཡུལ་ཡིན་ནམ། གལ་ཏེ་དེ་ཡང་མ་ཡིན་ནོ་ཞེ་ན། ད་ཇི་ལྟར་དགག་པའི་ཡུལ་མ་ཡིན་ཏེ། དགག་པ་ནི་སྒྲུབ་པ་ལྡོག་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1315]
དེ་བས་ན་རྣམ་པར་བཅད་པ་ཙམ་དེ་གཉི་ག་ཡང་ཡོད་པས་མི་མཐུན་པའི་ཕྱོགས་ལ་འཇུག་པའི་དོགས་པ་རྣམ་པར་བཅད་པའི་སྒོ་ནས་གོ་བར་བྱེད་པ་ཉིད་རྙེད་པ་ལ་ཇི་ལྟར་བདག་གིར་བྱེད། དེ་ཡང་བདག་ཉིད་རང་གི་ཚིག་གིས་གཉི་གའི་ཆོས་ཉིད་སྨྲ་བ་ན། ཡོད་པ་ཉིད་ལས་གཞན་ལ་ཡང་འདི་འཇུག་པ་དང་། ཡོད་པ་ཉིད་ལ་མ་འཁྲུལ་བར་བརྗོད་པའི་ཕྱིར། ཇི་ལྟར་ན་འཁྲུལ་པ་མ་ཡིན། ཡོད་པ་ཉིད་ལ་མེད་པའི་ཆོས་ཀྱང་དངོས་པོ་ཙམ་ཁྱབ་པར༌[^1021]བྱེད་པའི་དོན་རྣམ་པར་གཅོད་པའི་གཏན་ཚིགས་སུ་བརྗོད་པ་འདིའི་འགལ་བའི་གཏན་ཚིགས་སུ་འགྱུར་ཏེ། དེ་ནི་དངོས་པོ་འགའ་ཞིག་ལ་ཡང་མི་སྲིད་པའི་ཕྱིར་དང་། མེད་པ་ནི་དངོས་པོ་རྣམ་པར་བཅད་པ་ལ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1316]
དེ་བས་ན་ཆོས་རྣམ་པ་གསུམ་པོ་འདི་ཡང་ཡོད་པ་ཉིད་སྒྲུབ་པར་བྱེད་པ་ལ་གཏན་ཚིགས་ཀྱི་མཚན་ཉིད་བརྟེན་པ་མ་ཡིན་ཞིང་རྣམ་པ་གཞན་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1317]
དེ་བས་ན་ཡོད་པ་ཉིད་བསྒྲུབ་པར༌[^1022]འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 1318]
དེ་ཙམ་ལ་ཁྱབ་པར་བྱེད་པ་དངོས་པོའི་ཆོས་ཀྱི་འདིར་སྤྱིར་སྒྲུབ་པར་བྱེད་པ་ཉིད་ཡིན་ན་ཡང་ཡོད་པ་ཉིད་གྲུབ་པ་ཅན་གྱི་ཆོས་ཅན་ལ་མ་གྲུབ་པ༌[^1023]ཡིན་ནོ། །

[Block 1319]
གལ་ཏེ་བསྒྲུབ་པར་བྱ་བའི་ཆོས་དེས་ཁྱབ་པ་རྣམ་པ་འགའ་ཞིག་གིས་ངེས་པར་བྱས་པས་འགལ་བ་དང་འཁྲུལ་པ་དག་མེད་པའི་ཕྱིར། ཐལ་བར་འགྱུར་བ་འདི་མེད་དོ། །

[Block 1320]
ཁྱབ་པའམ་ཆོས་ཅན་ལ་བརྟེན་པ་ངེས་པར་མ་བྱས་པ་ཡང་དེའི་རང་བཞིན་ཅན་ཉིད་དུ་གོ་བར་བྱེད་པ་ནི་གོ་བར་བྱེད་པ་འགའ་ཞིག་ཏུ་ཡང་མི་འགྱུར་རོ། །

[Block 1321]
དེ་ཉིད་ཀྱི་ཕྱིར། རང་གི་ཆོས་ཀྱི་ཁྱབ་པ་གྲུབ་པའི་རང་བཞིན་གོ་བྱེད་ཡིན་པར་བརྗོད་པར་བྱ་སྟེ། གསལ་བར་བྱེད་པ་ཉིད་ཀྱིས་སྒྲོན་མ་གསལ་བར་བྱེད་པ་ནི། དེའི་ངོ་བོ་རྟོགས་པར་བྱེད་པ་མ་ཡིན་པ་ནི་རང་གི་དོན་གྱི་བྱ་བ་མི་བྱེད་དོ། །

[Block 1322 [VERSE]]
དེ་ལ་ཁྱབ་བྱེད་ངེས་པ་ནི། །
རྟོགས་པར་བྱ་བའི་རང་བཞིན་ཏེ། །
དེའི་ཆོས་ངེས་པ་ཁོ་ནའི་ཕྱིར། །

[Block 1323]
ཁྱབ་པར་བྱེད་པ་ཉིད་དུ་ངེས་པའི་ནི་ཆོས་ཅན་དེའི་ཆོས་ཏེ།

[Block 1324 [VERSE]]
གོ་བར་བྱ་བའི་རང་བཞིན་ཡིན་ནོ། །
འདི་ལྡོག་ན་ཡང་དེ་ལྡོག་བྱེད། །

[Block 1325]
བདག་ཉིད་ཁྱབ་པར་བྱེད་པའི་ཆོས་འདི་ལོག་པར་འགྱུར་བ༌[^1024]ན་ཁྱད་པར་བྱ་བའི་ཆོས་དེ་ལྡོག་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 1326]
གལ་ཏེ་འདི་མེད་ན་མི་འབྱུང་བ་དེ་ལྟར་ན་འདི་ནི་ཁྱབ་པར་བྱེད་པར་གྲུབ་པར་འགྱུར་རོ། །

[Block 1327]
དེ་བས་ན་འདིས་ནི་གོ་བར་བྱེད་པའི་མཚན་ཉིད་དུ་སྒྲུབ་པར་བྱེད་པའི་སྦྱོར་བ་རྣམ་པ་གཉིས་ཀྱང་བཤད་པར་རིག་པར་བྱའོ། །

[Block 1328]
སྦྱོར་བ་རྣམ་པ་གཉིས་ནི་ཆོས་མཐུན་པ་ཉིད༌[^1025]ཅན་དང་ཆོས་མི༌[^1026]མཐུན་པ་ཉིད་ཅན་ནོ། །

[Block 1329]
གང་གཞན་དག་ནི་རྗེས་སུ་འགྲོ་བ་ཅན་དང་ལྡོག་པ་ཅན་ཞེས་སྨྲའོ། །

[Block 1330]
སྦྱོར་བའི་བྱེ་བྲག་མ་གཏོགས་པར་འདི་གཉིས་ལ་དོན་དུ་བྱེ་བྲག་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 1331]
ཆོས་མཐུན་པ་ཉིད་ཅན་གྱི་སྦྱོར་བ་ལ་ཡང་དོན་གྱིས་ཆོས་མི་མཐུན་པ་ཉིད་ཅན་རྟོགས་པར་འགྱུར་ཏེ། དེ་མེད་ན་བསྒྲུབ་པར་བྱ་བ་དང་གཏན་ཚིགས་རྗེས་སུ་འགྲོ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 1332]
དེ་བཞིན་དུ་ཆོས་མི་མཐུན་པ་ཉིད་ཅན་གྱི༌[^1027]རྗེས་སུ་འགྲོ་བ༌[^1028]རྟོགས་པར་འགྱུར་ཏེ། དེ་མེད་ན་ནི་བསྒྲུབ་པར་བྱ་བ་མེད་ན་གཏན་ཚིགས་མེད་པར་ཐེ་ཚོམ་དུ་འགྱུར་ཞེས་རྒྱས་པར་འཆད་པར་འགྱུར་རོ། །

[Block 1333]
དཔེར་ན་མི་རྟག་ཉིད་བྱས་པའམ། འཇིག་བྱེད་མ་བྱས་པ་ལྟ་བུའོ། །

[Block 1334]
འདིས་ནི་འདི་གཉིས་ཀྱི་དཔེ་བསྟན་ཏོ། །

[Block 1335]
དེ་ལ་རྗེས་སུ་འགྲོ་བ་ཅན་ནི་གང་ཅུང་ཟད་བྱས་པ་དེ་ཐམས་ཅད་ནི་མི་རྟག་པ་སྟེ། དཔེར་ན་བུམ་པ་ལ་སོགས་པ་ལྟ་བུའོ། །
--- END BLOCKS ---
