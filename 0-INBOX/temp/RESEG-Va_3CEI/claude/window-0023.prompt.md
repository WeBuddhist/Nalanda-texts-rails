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
[Block 806]
ཕྱོགས་ལ་ཆགས་པ་ནི་ཁྱིམ་པའི་ཕྱོགས་དང་། རབ་ཏུ་བྱུང་བའི་ཕྱོགས་ལ་སྟེ་ལས་དང་འཚོ་བ་སྣ་ཚོགས་དང་ཁེ་དང་གྲགས་པ་ལ་ཆགས་པའོ། །

[Block 807]
ཐེག་པ་ལ་ཆགས་པ་ནི་ཐེག་པ་ཆེ་ཆུང་གི་ལྟ་བ་ལ་གཙོར་འཛིན་ཅིང་ཆགས་པའོ། །

[Block 808]
མདོ་ལས་ཤཱ་རིའི་བུ་དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནས་རྨད་དུ་བྱུང་བའི་ཆོས་དང་ལྡན་ཏེ་ཞེས་པའི་བར་དུ་ནི་གོང་མའི་ཡེ་ཤེས་མཐོང་བ་ཞེས་པས༌[^819]སྟོན་ཏེ། ཆེན་པོ་ནི་བླ་ན་མེད་པ༌[^820]མཆོག་ཅེས་པ་ནི་དམ་པའོ། །

[Block 809]
དེ་ཀུན་ཀྱང་ཡེ་ཤེས་རྣམ་གཉིས་ཀྱི་འཁོར་ཏེ། ཐོགས་པ་མེད་པ་ནི་སྤོབས་པ་སོ་སོ༌[^821]ཡང་དག་པར་རིག་པ་བཞིའོ། །

[Block 810]
སྟོབས་ནི་སྟོབས་བཅུའོ། །

[Block 811]
མི་འཇིགས་པ་ནི་མི་འཇིགས་པ་བཞིའོ། །

[Block 812]
མ་འདྲེས་པ་ནི་བཅོ་བརྒྱད་དོ། །

[Block 813]
དབང་པོ་དང་སྟོབས་ནི་ལྔ་ལྔའོ། །

[Block 814]
བྱང་ཆུབ་ཀྱི་ཡན་ལག་ནི་བདུན་ནོ། །

[Block 815]
བསམ་གཏན་ནི་བཞིའོ། །

[Block 816]
རྣམ་པར་ཐར་པ་ནི་བརྒྱད་དོ། །

[Block 817]
ཏིང་ངེ་འཛིན་ནི་གསུམ་མོ། །

[Block 818]
སྙོམས་པར་འཇུག་པ་ནི་དགུའོ། །

[Block 819]
དེ་དག་གི་མཚན་ཉིད་དང་རྣམ་གྲངས་བཤད་པ་ནི་མདོ་དང་གཙུག་ལག་ལས་རྒྱས་པར་བཤད་པ་བཞིན་ནོ། །

[Block 820]
མདོ་ལས་རྨད་དུ་བྱུང་བའི་ཆོས་དང་ལྡན་པ་ཞེས་པ་ནས་ཡང་དག་པར་སྟོན་པ་རྣམས་སོ་ཞེས་པའི་བར་དུ་ནི་ངེས་པའི་ཚིག་སྟོན་ཏེ། འགྲེལ་པ་ལས་སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་རྣམ་པ་བདུན་སྟོན་པ་ལ་འདི་དང་པོ་སྟེ། འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཆོས་རྣམས་ཤིན་ཏུ་ཟབ་མོར་འཇུག་པའོ། །

[Block 821]
མདོ་ལས་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་གྱིས་ཤིག་ཅེས་པའི་བར་དུ་ནི་ཚིག་ཕུན་སུམ་ཚོགས་པ་དང་། མིང་དང་མཚན་མ་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏེ། དེ་བཞིན་གཤེགས་པས་གསུང་སྙན་པ་ཡིད་དུ་འོང་བས་ཆོས་སྟོན་ཏེ། དེ་ནི་འབྲུག་སྒྲ་ལྟར་ཤིན་ཏུ་ཟབ་པ་གསུང་གསལ་ཞིང་དག་པ་རྒྱང་དུ་སྒྲོག་ཅིང་ཐོས་པ་རྣམས་དགའ་བ་སྐྱེ་བ་དང་། སེམས་ལ་ཞེན་པར་དད་ཅིང་གུས་པ་སྐྱེ་བའི་གསུང་དང་། བདེ༌[^822]བའི་དོན་གོ་སླ་བའི་གསུང་དང་། ཉན་པ་རྣམས་མི་སྐྱོ་ཞིང་ཆོས་རྣམ་པར་འབྱེད་པ་ལ་མཁས་པའི་གསུང་ངོ་། །མིང་དང་མཚན་ཉིད་ཕུན་སུམ་ཚོགས་པ་ནི་དེ་ཙམ་གྱིས་ཆོག་གིས་ཞེས་པ་སྟེ། སེམས་ཅན་ཆོས་ཀྱི༌[^823]སྣོད་དུ་གྱུར་པ་རྣམས་སྨིན་པར་གྱུར་ཟིན་པའི་ཕྱིར་ཏེ། ཆོས་ཀྱི་སྣོད་ལ་ཡང་ཡང་དག་པ་དང་ཡང་དག་པ་མ་ཡིན་པ་རྣམ་པ་གཉིས་ཏེ། ཡང་དག་པ་ནི་ཤཱ་རིའི་བུ་ལ་སོགས་པའོ། །

[Block 822]
ཡང་དག་པ་མ་ཡིན་པ་ནི་ང་རྒྱལ་ཅན་རྣམས་སོ། །

[Block 823]
ཆོས་ཡང་དག་པའི་སྣོད་དུ་གྱུར་པ་ནི་འཕགས་པ་རྣམས་ནི་དམ་པའི་ཆོས་ཀྱི་དགའ་བས་སེམས་རྒྱས་པར་གྱུར་པའི་ཕྱིར་མཆོག་ཅེས་བཀའ་སྩལ་པ་དང་། ཆོས་ཡང་དག་པ་མ་ཡིན་པའི་སྣོད་ཅན་རྣམས་ཀྱང་རང་གི་འཕགས་པའི་སེམས་ཐོབ་པ་ཙམ་དུ་སེམས་ཤིན་ཏུ༌[^824]རྣམ་པར་གྲོལ་བའི་ཆོས༌[^825]ཐོབ་པས་ཆོག་པར་སེམས་པས་ཆོག་ཅེས་གསུངས་པའོ། །

[Block 824]
མདོ་ལས་ཤཱ་རིའི་བུ་དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནས་ངོ་མཚར་རབ་ཏུ་ཐོབ་པ་སྟེ་ཞེས་པའི་བར་དུ་ནི་འདི་བཤད་པར་འོས་པ་སྟོན་ཏེ། འཕགས་པ་ཤཱ་རིའི་བུ་ལ་སོགས་པ་དབང་པོ་སྨིན་པ་རྣམས་ཡོན་ཏན་རྨད་ཀྱི་ཆོས་རྣམས་བཤད་པར་འོས་པའི་ཕྱིར་ངོ་མཚར་རབ་ཏུ་ཐོབ་པའོ། །

[Block 825]
མདོ་ལས་ཤཱ་རིའི་བུ་དེ་ཙམ་ཞེས་པ་ནས་ཤཱ་རིའི་བུ་དེ་བཞིན་གཤེགས་པ་ཉིད་མཁྱེན་ཏོ་ཞེས་པའི་བར་དུ་ནི་ཚད་མེད་པའི་རྣམ་པ་ཕུན་སུམ་ཚོགས་པ་སྟོན་ཏེ། དེ་བཞིན་གཤེགས་པའི་སྙིང་པོ་ནི་མི་འགྱུར་བས་ཆོས་ཀྱི་སྐུའི་རང་བཞིན་ཏེ། འདུས་བྱས་དང་འདུས་མ་བྱས་ཀྱི་ཆོས་ཐམས་ཅད་མཁྱེན་པའི་ཕྱིར་རྣམ་པ་ཚད་མེད་པ་མཁྱེན་པའོ། །

[Block 826]
ཚིག་དེ་དག་གིས་གོང་དུ་སྨོས་པའི་ཐབས་མཁས་པ་དང་ཡེ་ཤེས་མཐོང་བ་ལ་སོགས་པའི་ཚིག་གི་དོན་རྣམས་མདོ་སྡེ་ཉིད་ཀྱིས༌[^826]བཀྲོལ་བ་དང་བཅས་སུ་བསྟན་ཏེ། གོ་རིམས་བཞིན་དུ་སྦྱར་ཞིང་ཆུད་པར་བྱའོ། །

[Block 827]
མདོ་ལས་ཆོས་དེ་དག་གང་ཡིན་པ་དང་ཞེས་པ་ནས་དེ་བཞིན་གཤེགས་པ་ཉིད་མངོན་སུམ་སྟེ། མི་མངོན་པ་མ་ཡིན་ནོ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པ་ཡང་ཆོས་ཐམས་ཅད་མངོན་དུ་གཟིགས་ཤིང་མཁྱེན་ནས་ཆོས་སྟོན་ཏོ། །

[Block 828]
ཚིག་གི་དོན་རྣམ་པ་ལྔ་པོ་དེ་ནི་ལན་བཞིར་བཟླས་ཏེ་བཤད་པར་བྱའོ། །

[Block 829]
དེ་ལ་ཆོས་གང༌[^827]ཡིན་ཞེས་པ་ནི་ཐེག་པ་རྣམ༌[^828]གསུམ་ལ་འཇུག་པ་བཀྲི་བའི་དོན་བསལ༌[^829]ཏེ་ངེས་པའི་དོན་གང་ཡིན་པ་ལ་འཇུག་པ་དང་། ཆོས་དེ་དག་ཇི་ལྟ་བུ་ཡིན་པ་ནི་ཐེག་པ་གཅིག་པུ་ལ་དོན་རྣམ་པ་སྣ་ཚོགས་སུ་སྟོན་པའོ། །

[Block 830]
ཆོས་དེ་དག་ཅི་འདྲ་བ་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གསུམ་གྱི་སྒོར་ཞུགས་པ་ལ་སྤྱོད་པ་རྣམ་པར་དག་པ་བསྒྲུབ༌[^830]པའོ། །

[Block 831]
མཚན་ཉིད་ཇི་ལྟ་བུ་ཡིན་པ་ནི་ཐེག་པ་རྣམ་པ༌[^831]གསུམ་གྱི་མཚན་ཉིད་གཅིག་ཏུ་བསྟན་པའོ། །

[Block 832]
ངོ་བོ་ཉིད་ཅི་ཡིན་པ་ནི་མཐར་ཐེག་པ་གཅིག་ཏུ་ཟད་དེ་གཉིས་དང་གསུམ་གྱི་ངོ་བོ་ཉིད་མེད་པར་བསྟན་པའོ། །

[Block 833]
ཡང་འདི་མན་ཆད་ཚིག་དེ་དག་ལས་གཞན་དུ་གྲོལ༌[^832]ན་ཆོས་དེ་དག་གང་ཡིན་ཞེས་པ་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་པའི་ཆོས་སོ། །

[Block 834]
ཆོས་དེ་དག་ཇི་ལྟ་བུ་ཡིན་པ་ནི་རྒྱུ་དང་རྐྱེན་གྱིས༌[^833]བསྐྱེད་པ་དང་། རྒྱུ་དང་རྐྱེན་གྱིས་མ་བསྐྱེད་པ་སྟེ། དེ་ལ་རྒྱུ་དང་རྐྱེན་གྱིས་བསྐྱེད་པ་ནི་འདུས་བྱས་ཀྱི་ཆོས་སོ། །

[Block 835]
རྒྱུ་དང་རྐྱེན་གྱིས་མ་བསྐྱེད་པ་ནི་འདུས་མ་བྱས་པའི་ཆོས་སོ། །

[Block 836]
[^834]དེ་དག་ཇི་འདྲ༌[^835]བ་ནི་རྟག་པ་དང་མི་རྟག་པའི་ཆོས་ཏེ། དེ་ཡང་རྐྱེན་གྱིས་མ་བསྐྱེད་པ་ནི་རྟག་པའི་ཆོས་སོ། །

[Block 837]
རྐྱེན་གྱིས་བསྐྱེད་པ་ནི་མི་རྟག་པའི་ཆོས་སོ། །

[Block 838]
མཚན་ཉིད་ཇི་ལྟ་བུ་ཡིན་པ་ནི་སྐྱེ་བ་དང་། གནས་པ་དང་འཇིག་པའི་ཆོས་ཀྱི་མཚན་ཉིད་དོ།[^836] །མཚན་ཉིད་དེ་གསུམ་དང་ལྡན་པ་ནི་འདུས་བྱས་མི་རྟག་པའི་ཆོས་སོ། །

[Block 839]
མཚན་ཉིད་དེ་གསུམ་དང་བྲལ་བ་ནི་འདུས་མ་བྱས་རྟག་པའི་ཆོས་སོ། །

[Block 840]
ངོ་བོ་ཉིད་ཅི་ཡིན་པ་ནི་ཕུང་པོ་ལྔའི་ངོ་བོ་ཉིད་དང་ཕུང་པོ་ལྔ་དང་བྲལ་བའི་ངོ་བོ་ཉིད་ཀྱི་ཆོས་ཏེ། ཕུང་པོ་ལྔ་ནི་སྐྱེ་བ་ལ་སོགས་པའི་མཚན་ཉིད་དོ། །

[Block 841]
ཕུང་པོ་ལྔ་དང་བྲལ་བ་ནི་སྐྱེ་བ་མེད་པ་ལ་སོགས་པའོ། །

[Block 842]
ཡང་བཤད་པ་གསུམ་ནི་ཚིག་དེ་ལྔ་ལས་དང་པོའི་གཉིས་ནི་གོང་དུ་བཤད་པ་དག་དང་འདྲ། ཆོས་དེ་དག་ཅི་འདྲ་ཞེས་པ་ནི་རང་བཞིན༌[^837]མེད་པ་སྟེ་རྟེན་ཅིང་འབྲེལ་ཏེ་འབྱུང་བའི༌[^838]ཆོས་སོ། །

[Block 843]
མཚན་ཉིད་ཇི་ལྟ་བུ་ཡིན་པ་ནི་བལྟར༌[^839]རུང་བའི་མཚན་ཉིད་ཀྱི་ཆོས་རྣམས་སོ། །

[Block 844]
ངོ་བོ་ཉིད་ཇི་ལྟ་བུ་ཡིན་པ་ནི་ཕུང་པོ་ལྔ་གཟུང་བ་དང་འཛིན་པའི་ཆོས་ཏེ། ཀུན་འབྱུང་གི་ངོ་བོ་ཉིད་དམ་ལམ་གྱི་བདེན་པས་གཟུང༌[^840]བའོ། །

[Block 845]
ཡང་ཆོས་དེ་དག་ལ་བཤད་པ་བཞི་སྟེ། ཆོས་སྟོན་པའི་བྱེད་པ་ལ༌[^841]བརྟེན་ཏེ་བཤད་པ་ནི༌[^842]ཆོས་དེ་དག་གང་ཡིན་ཞེས་པ་ནི་མིང་དང་ཚིག་དང་འབྱུང་བའི་ཚོགས་ཀྱི༌[^843]བཤད་པའི་ཆོས་སོ། །
--- END BLOCKS ---
