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
[Block 1576]
འཕགས་པའི་ཡང་འདི་ནི་འདོད་ཆགས་དང༌[^710]བྲལ་བས་ཐོབ་པར་བྱ་བ་མ་ཡིན་ཏེ། འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། སྦྱོར་བས་འཐོབ། འདི་ནི་སྦྱོར་བས་འཐོབ་པར་བྱ་བ་ཁོ་ན་ཡིན་པས། འདས་པ་ཡང་མི་འཐོབ་ལ་མ་འོངས་པ་ཡང་མི་འཐོབ་སྟེ། དེ་ནི་སེམས་ཀྱི་སྟོབས་ཀྱིས་འཐོབ་པའི་ཕྱིར་རོ། །

[Block 1577]
ཅི་བཅོམ་ལྡན་འདས་ཀྱི་ཡང་སྦྱོར་བ་ལས་བྱུང་བ་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 1578]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། ཐུབ་པའི་བྱང་ཆུབ་ཀྱིས་ཐོབ་བྱ། །སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱིས་ནི་འདི་ཟད་པ་མཁྱེན་པ་དང་དུས་མཉམ་དུ་བརྙེས༌[^711]སོ། །

[Block 1579]
སངས་རྒྱས་རྣམས་ཀྱི་ནི་སྦྱོར་བ་ལས་བྱུང་བ་ཞེས་བྱ་བ་ཅུང་ཟད་ཀྱང་མེད་དེ། དེ་དག་གི་ཡོན་ཏན་འབྱོར་པ་མངོན་སུམ་དུ་འགྱུར་བ་ཐམས་ཅད་ནི་བཞེད་པ་ཙམ་ལ་རག་ལུས་པ་ཡིན་པས་དེ་ལྟ་བས་ན་དེ་དག་གི་ཐམས་ཅད་ནི། འདོད་ཆགས་དང་བྲལ་བས་བརྙེས་པ་ཡིན་ནོ། །

[Block 1580]
ད་ནི་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་འགོག་པའི་སྙོམས་པར་འཇུག་པ་མ་བསྐྱེད་ན་ཟད་པ་མཁྱེན་པའི་དུས་སུ་གཉི་གའི་ཆ་ལས་རྣམ་པར་གྲོལ་བར་ཇི་ལྟར་འགྲུབ་ཅེ་ན། འགྲུབ་སྟེ། བསྐྱེད་ཟིན་པ་བཞིན་དུ་དེ་ལ་མངའ་བའི་ཕྱིར་རོ། །

[Block 1581]
ནུབ་ཕྱོགས་པ་དག་ན་རེ་དེ་ནི་དང་པོ་ཁོ་ནར་བྱང་ཆུབ་སེམས་དཔའ་སློབ་པའི་གནས་སྐབས་ན་སྐྱེད་པར་བྱེད་དོ་ཞེས་ཟེར་རོ། །

[Block 1582]
ཡང་འདི་ཅིའི་ཕྱིར་མི་འདོད་ཅེ་ན། དེ༌[^712]ལྟར་ན་གནས་བརྟན་ཉེ་བསྲུངས་ཀྱི་ལུགས༌[^713]ཀྱི་ཚིག་ནི་དེ་བཞིན་གཤེགས་པ་ནི་འགོག་པའི་སྙོམས་པར་འཇུག་པ་བསྐྱེད་ནས་ཟད་པ་མཁྱེན་པ་སྐྱེད་པར༌[^714]མཛད་དོ་ཞེས་བརྗོད་པར་བྱའོ། །ཞེས་བྱ་བ་འབྱུང་བ་འདི་ཚད་མར་བྱས་པ་ཡིན་ནོ། །

[Block 1583]
དང་པོར་མ་ཡིན། ཁ་ཆེ་བ་རྣམས་ན་རེ་དེ་ལྟར་བསྐྱེད་དུ་མི་རུང་ངོ་ཞེས་ཟེར་རོ། །ཅིའི་ཕྱིར་ཞེ་ན། སྐད་ཅིག་མ། སུམ་ཅུ་རྩ་བཞིས་འཐོབ༌[^715]ཕྱིར་རོ། །

[Block 1584]
བྱང་ཆུབ་སེམས་དཔའ་ནི་སེམས་ཀྱི་སྐད་ཅིག་མ་སུམ་ཅུ་རྩ་བཞིས་བྱང་ཆུབ་རྗེས་སུ་འཐོབ་པ༌[^716]སྟེ། བདེན་པ་མངོན་པར་རྟོགས་པ་ན་བཅུ་དྲུག་དང་། སྲིད་པའི་རྩེ་མོའི་འདོད་ཆགས་དང༌[^717]བྲལ་བ་ན་ཉོན་མོངས་པའི་རྣམ་པ་དགུ་སྤོང་བར་བྱེད་པ་ན་བར་ཆད་མེད་པ་དང་རྣམ་པར་གྲོལ་བའི་ལམ་དགུ་དགུ་སྐྱེ་བའི་ཕྱིར་བཅོ་བརྒྱད་དེ། དེ་དག་ནི་སུམ་ཅུ་རྩ་བཞིར་འགྱུར་རོ། །

[Block 1585]
ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ཀྱི་འདོད་ཆགས་དང་བྲལ་བ་དེ་ངེས་པ་ལ་འཇུག་པའི་ཕྱིར་ས་འོག་མ་པའི་ཉོན་མོངས་པ་རྣམས་ནི་ཡང་སྤང་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1586]
དེའི་ཕྱིར་བར་སྐབས་འདིར་མི་འདྲ་བའི་སེམས་མི་སྲིད་པས་འགོག་པའི་སྙོམས་པར་འཇུག་པ་མི་རུང་ངོ་ཞེས་ཟེར་རོ། །

[Block 1587]
ཞེས༌[^718]གྲག་གོ། །

[Block 1588]
གལ་ཏེ་བར་སྐབས་སུ་མི་འདྲ་བའི་སེམས་མངོན་དུ་བྱས་ན་ཅིར་འགྱུར་ཞེ་ན། བསམ་པ་ལྡང་བ་ཅན་དུ་འགྱུར་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་བསམ་པ་མི་ལྡང་བ་ཅན་ཡིན་ནོ། །

[Block 1589]
ཉི་འོག་པ་རྣམས་ན་རེ་བསམ་པ་མི་ལྡང་བ༌[^719]ཅན་ཡིན་པ་བདེན་མོད་ཀྱི། ཟག་པ༌[^720]མེད་པའི་ལམ་ལས་ནི་མ་ཡིན་ནོ། །

[Block 1590]
འོ་ན་ཅི་ཞེ་ན། ཟག་པ་ཟད་པ་མ་ཐོབ་ཀྱི་བར་དུ་རེ་ཞིག་སྐྱིལ་མོ་ཀྲུང་མི་གཞིག༌[^721]གོ་སྙམ་པའི་བསམ་པ་འདི་མི་ལྡང་བའི་ཕྱིར་ཏེ། སྟན་གཅིག་ཁོ་ན་ལ་དོན་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 1591]
སྔ་མ་ཁོ་ན་ཡིན་ནོ་ཞེས་ནི་བརྗོད་དོ། །

[Block 1592 [HEADING]]
##### སྙོམས་པར་འཇུག་པ་གཉིས་ཀྱི་ཁྱད་པར། ^2-3-5-3-0

[Block 1593]
སྙོམས་པར་འཇུག་པ༌[^722]འདི་གཉིས་ཀྱི་རྣམ་པའི་བྱེ་བྲག་མ་ཡིན༌[^723]མོད་ཀྱི། གཉི་ག་འདོད་དང་གཟུགས་རྟེན་ཅན། །འདུ་ཤེས་མེད་པ་དང་འགོག་པའི་སྙོམས་པར་འཇུག་པ་འདི་གཉི་ག་ཡང་འདོད་པའི་ཁམས་དང་གཟུགས་ཀྱི་ཁམས་སུ་སྐྱེད་དོ། །

[Block 1594]
གང་དག་འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་གཟུགས་ཀྱི་ཁམས་སུ་མི་འདོད་པ་དེ་དག་གི་ལྟར་ན་ཆོས་མངོན་པའི་གཞུང་གཟུགས་ཀྱི་སྲིད་པ་ཡིན་ལ། སྲིད་པ་དེ་རྣམས་དང༌[^724]འདྲིད་པ་ཅན་སྔ་མ་ཡིན་པ་ཡོད་དམ་ཞེ་ན། ཡོད་དེ། གཟུགས་ན་སྤྱོད་པའི་སེམས་ཅན་ལྷ་འདུ་ཤེས་ཅན་སེམས་མི་འདྲ་བ་ལ་གནས་པ་རྣམས་དང་། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་དང་། འགོག་པའི་སྙོམས་པར་འཇུག་པ་ལ་སྙོམས་པར་ཞུགས་པ་རྣམས་དང་། ལྷ་འདུ་ཤེས་མེད་པ་འདུ་ཤེས་མེད་པ་པ་ཐོབ་པ་རྣམས་ཀྱི་སྲིད་པ་གང་ཡིན་པའོ་ཞེས་འབྱུང་བ་འདི་དང་འགལ་ཏེ། དེའི་ཕྱིར་འདི་གཉི་ག་ཡང་འདོད་པ་དང་གཟུགས་ལ་བརྟེན་པ་དག་ཡིན་ནོ། །

[Block 1595]
དེ་ལ་ཡང་ཁྱད་པར་ནི་འདི་ཡོད་དོ། །

[Block 1596]
[^725]འགོག་པ་དང་པོར་མིའི་ནང་དུ། འགོག་པའི་སྙོམས་པར་འཇུག་པ་ནི་དང་པོ་ཉིད་དུ་མི་དག་གི༌[^726]ནང་དུ་སྐྱེད་དོ། །

[Block 1597]
ཕྱིས་ནི་སྔར་ཡོངས་སུ་ཉམས་པ་དག་གིས་གཟུགས་ཀྱི་ཁམས་སུ་ཡང་སྐྱེད་དོ། །ཅི་འདི་ལས་ཀྱང་ཡོངས་སུ་ཉམས་པ་ཡོད་དམ་ཞེ་ན། སྨྲས་པ་ཡོད་དོ། །

[Block 1598]
དེ་ལྟ་མ་ཡིན་ན་འཆར་བྱེད་ཀྱི་མདོ་ལས༌[^727]ཚེ་དང་ལྡན་པ་དག་འདི་ན་དགེ་སློང་ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པ་ཡང་ཡིན། ཏིང་ངེ་འཛིན་ཕུན་སུམ་ཚོགས་པ་ཡང་ཡིན། ཤེས་རབ་ཕུན་སུམ་ཚོགས་པ་ཡང་ཡིན་པ་དེ་ནི་ཡང་དང་ཡང་དུ་འདུ་ཤེས་དང་ཚོར་བ་འགོག་པ་ལ་སྙོམས་པར་འཇུག་པ་དང་ལྡང་བའི་གནས་དེ་ཡོད་དོ་ཞེས་བྱ་བར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་རབ་ཏུ་ཤེས་སོ། །

[Block 1599]
དེ་ནི་མཐོང་བའི་ཆོས་ཁོ་ན་ལ་དང་པོ་ཉིད་དུ་ཀུན་ཤེས་པ་ཐོབ་པར་ཡང་མི་བྱེད་ཅིང་འཆི་བའི་དུས་ཀྱི་ཚེ་ཡང་མ་ཡིན་ལ་ལུས་ཞིག་ནས་ཀྱང་ཁམ་གྱི་ཟས་ཟ་བའི་ལྷ་ལས་འདས་ཏེ། ཡིད་ལས་བྱུང་བའི་ལྷའི་ལུས་གང་ཡང་རུང་བ་ཞིག་ཏུ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 1600]
དེ་དེར་སྐྱེས་ནས་ཡང་དང་ཡང་དུ༌[^728]འདུ་ཤེས་དང་ཚོར་བ་འགོག་པ་ལ་སྙོམས་པར་འཇུག་པ་དང་ལྡང་བའི་གནས་དེ་ཡང༌[^729]ཡོད་དོ་ཞེས་བྱ་བར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ་ཞེས་འབྱུང་བ་དང་འགལ་ལོ། །

[Block 1601]
དེར་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་ཡིད་ལས་བྱུང་བའི་ལུས་ཅན་གྱི་ལྷ་ནི་གཟུགས་ན་སྤྱོད་པ་ཡིན་པར་གསུངས་ལ། སྙོམས་པར་འཇུག་པ་འདི་ནི་སྲིད་པའི་རྩེ་མོ་པ་ཡིན་ན་དེ་ཇི་ལྟར་དེ་ཐོབ་པ་ཡོངས་སུ་མ་ཉམས་པ་གཟུགས་ཀྱི་ཁམས་སུ་སྐྱེ་བར་འགྱུར། སྡེ་པ་གཞན་དག་འགོག་པའི་སྙོམས་པར་འཇུག་པ་བསམ་གཏན་བཞི་པའི་ས་པ་ཡང་ཡིན་པར་འདོད་པ་དེ་དག་གི་ལྟར་ན་འདི་ཡོངས་སུ་ཉམས་པ་མེད༌[^730]བཞིན་དུ་ཡང་འགྲུབ་པ་འདྲ་མོད་ཀྱི། འདི་བསམ་གཏན་བཞི་པའི་ས་པ་ཡང་ཡོད་དོ་ཞེས་བྱ་བ་འདི་ནི་མི་འགྲུབ་བོ། །ཅིའི་ཕྱིར་ཞེ་ན། མདོ་ལས་མཐར་གྱིས་གནས་པའི་སྙོམས་པར་འཇུག་པ་དགུ་ཞེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 1602]
གལ་ཏེ་དེ་ངེས་པ་ཡིན་ན་ཇི་ལྟར་ཐོད་རྒལ་དུ་སྙོམས་པར་འཇུག་པ་དག་ཡིན་ཞེ་ན། འདི་ནི་རྩོམ་པ་དང་པོ་པ་ལས༌[^731]ངེས་པ་ཡིན་ཏེ། དགའ་མགུའི་དབང་ཐོབ་པ་དག་ཡིན་ན་ནི་རྣམ་པར་རྒལ་ཏེ་ཡང་སྙོམས་པར་འཇུག་གོ། །

[Block 1603]
དེ་ལྟར་ན་སྙོམས་པར་འཇུག་པ་འདི་གཉིས་ནི་ས་ལས་ཀྱང་ཁྱད་པར་ཡོད་དེ། བསམ་གཏན་བཞི་པ་དང་སྲིད་པའི་རྩེ་མོའི་ས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1604]
སྦྱོར་བ་ལས་ཀྱང་ངེས་པར་འབྱུང་བ་དང་གནས་པའི་འདུ་ཤེས་སྔོན་དུ་བཏང་བའི་ཡིད་ལ་བྱེད་པས་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 1605]
རྒྱུད་ལས་ཀྱང་སོ་སོའི་སྐྱེ་བོ་དང་འཕགས་པའི་རྒྱུད་ལ་སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 1606]
འབྲས་བུ་ལས་ཀྱང་འདུ་ཤེས་མེད་པ་པ་དང་སྲིད་པའི་རྩེ་མོའི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1607]
མྱོང་བར་འགྱུར་བ་ལས་ཀྱང་མྱོང་བར་འགྱུར་བར་ངེས་པ་དང་གཉི་ག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1608]
དང་པོ་སྐྱེད་པ་ལས་ཀྱང་ཁམས་གཉིས་དང་མིའི་ནང་དུ་སྐྱེད་པའི༌[^732]ཕྱིར་རོ། །

[Block 1609]
ཡང་ཅིའི་ཕྱིར་འདི་དག་སེམས་དང་སེམས་ལས་བྱུང་བ་འགོག་པའི་རང་བཞིན་ཡིན་ན་འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་དང་། འདུ་ཤེས་དང་ཚོར་བ་འགོག་པའི་སྙོམས་པར་འཇུག་པ་ཞེས་བྱ་ཞེ་ན། དེ་དག་དང་མི་མཐུན་པས་དེ་དག་ལ་སྙོམས་པར་འཇུག་པར་སྦྱོར་བའི་ཕྱིར་ཏེ། ཚོར་བ་ལ་སོགས་པ་ཡང་ཤེས་མོད་ཀྱི་གཞན་གྱི་སེམས་ཤེས་པ་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1610]
ད་ནི་ཇི་ལྟར་འགགས་ནས་ཡུན་རིང་དུ་ལོན་པའི་སེམས་ལས་ཡང་སེམས་སྐྱེ་བར་འགྱུར་ཞེ་ན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་འདས་པ་ཡང་ཡོད་པའི་ཕྱིར་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་དུ་འདོད་དེ། [^733]སྔོན་གྱི་སློབ་དཔོན་གཞན་དག་ན་རེ་ནི་རེ་ཞིག་གཟུགས་མེད་པར་སྐྱེས་པ་རྣམས་ཀྱི་གཟུགས་འགགས་ནས་རིང་དུ་ལོན་ན་ཡང་གཟུགས་ཇི་ལྟར་སྐྱེ་ཞེ་ན། དེ་ནི་སེམས་ཁོ་ན་ལས་སྐྱེའི༌[^734]གཟུགས་ལས་ནི་མ་ཡིན།[^735] དེ་བཞིན་དུ་སེམས་ཀྱང་དབང་པོ་དང་བཅས་པའི་ལུས་འདི་ཁོ་ན་ལས་སྐྱེའི༌[^736]སེམས་ལས་ནི་མ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། སེམས་དང་དབང་པོ་དང་བཅས་པའི་ལུས་གཉིས་ནི་ཕན་ཚུན་ས་བོན་ཅན་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1611]
བཙུན་པ་དབྱིག་བཤེས་ཀྱིས་ནི་ཡོངས་སུ་དྲིས་པ༌[^737]ལས།

[Block 1612]
འདི་ནི་གང་གི་ལྟར་ན་འགོག་པའི་སྙོམས་པར་འཇུག་པ་སེམས་མེད་པ་པ༌[^738]ཡིན་པ་དེ་ལ་སྐྱོན་དུ་འགྱུར་གྱི་ཁོ་བོ་ནི་འགོག་པའི་སྙོམས་པར་འཇུག་པ་སེམས་དང་བཅས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1613]
བཙུན་པ་དབྱངས་སྒྲོགས་ན་རེ་དེ་ནི་མི་འཐད་དེ། བཅོམ་ལྡན་འདས་ཀྱིས་རྣམ་པར་ཤེས་པ་ཡོད་ན་གསུམ་འདུས་པ་ལས་རེག་པ། རེག་པའི་རྐྱེན་གྱིས་ཚོར་བ་དང་འདུ་ཤེས་དང་སེམས་པ་ཞེས་གསུངས་ཏེ། དེའི་ཕྱིར་འདི་ལ་འདུ་ཤེས་དང་ཚོར་བ་དག་ཀྱང་འགག་པར་མི་འགྱུར་རོ། །

[Block 1614]
འོན་ཏེ་ཚོར་བའི་རྐྱེན་གྱིས་སྲེད་པ་ཞེས་གསུངས་མོད་ཀྱི་དགྲ་བཅོམ་པ་ལ་ཚོར་བ་ཡོད་བཞིན་དུ་སྲེད་པ་མི་སྐྱེ་བ་དེ་བཞིན་དུ་རེག་པ་ཡོད་བཞིན་དུ་ཚོར་བ་ལ་སོགས་པ་མི་འབྱུང་ངོ་ཞེ་ན། ཁྱད་པར་དུ་བྱས་པའི་ཕྱིར་དེ་ནི་མ་ཡིན་ཏེ། མ་རིག་པའི་འདུས་ཏེ་རེག་པ་ལས་སྐྱེས་པའི་ཚོར་བ་ལ་བརྟེན་ནས་སྲེད་པ་སྐྱེས་སོ་ཞེས་གསུངས་ཀྱི། ཚོར་བ་སྐྱེས་པ༌[^739]ལ་རེག་པ་ནི་བྱེ་བྲག་ཏུ་མ་བྱས་པས་འདི་ནི་མི་འདྲའོ། །

[Block 1615]
དེ་ལྟ་བས་ན་བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་འགོག་པའི་སྙོམས་པར་འཇུག་པ་ནི་སེམས་མེད་པ་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །
--- END BLOCKS ---
