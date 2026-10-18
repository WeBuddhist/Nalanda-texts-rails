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
[Block 1506]
འོ་ན་ནི་དེ་དག་ཀྱང་རིགས་གསུམ་པ་ཡིན་ན་གང་དག་གི་མ་རྙེད་པ་ཡིན། ཐམས་ཅད་ཀྱི་ཡིན་ནོ། །

[Block 1507]
འོ་ན་ནི་ཉེས་པ་དེ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1508]
ལན་ཡང་དེ་ཉིད་ཡིན་ནོ། །

[Block 1509]
འོ་ན་ནི་འབད་པ་དོན་མེད་པར་འགྱུར་བས་མདོ་སྡེ་པ་རྣམས་ཀྱི་ཇི་ལྟ་བ་དེ་ལྟ་བུ་ནི་ལེགས་པ་ཡིན་ནོ། །

[Block 1510]
མདོ་སྡེ་པ་རྣམས་ཀྱི་ཇི་ལྟ་བུ་ཡིན། འཕགས་པའི་ཆོས་རྣམས་མ་སྐྱེས་པའི་རྒྱུད༌[^675]ནི་སོ་སོའི་སྐྱེ་བོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 1511]
ཡང་མ་ཐོབ་པ་འདི་ཇི་ལྟར་རྣམ་པར་ཉམས་པར་འགྱུར་ཞེ་ན། ཆོས་གང་གི་མ་ཐོབ་པ་གང་ཡིན་པ་དེ་ནི། དེ་ཐོབ་དང་། ས་འཕོས་ནས་ནི་རྣམ༌[^676]ཉམས་འགྱུར། །རེ་ཞིག་འདི་ལྟ་སྟེ། འཕགས་པའི་ལམ་གྱི་མ་རྙེད་པ་ནི་སོ་སོའི་སྐྱེ་བོ་ཉིད་དེ། དེ་ནི་དེ་རྙེད་པ་དང་ས་འཕོས་པ་ལས་རྣམ་པར་ཉམས་པར་འགྱུར་ཏེ། གཞན་དག་གི་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 1512]
རྣམ་པར་ཉམས་པར་འགྱུར་ཞེས་བྱ་བ་ནི་མ་ཐོབ་པ་དེ༌[^677]མ་ཐོབ་པ་སྐྱེ་ཞིང་ཐོབ་པ་འཆད་པར་འགྱུར་རོ། །

[Block 1513]
ཅི་མ་ཐོབ་པ་དང་ཐོབ་པ་དག་གི་ཡང་ཐོབ་པ་དང་། མ་ཐོབ་པ་ཡོད་དམ། སྨྲས་པ། གཉི་གའི་ཡང་གཉི་ག་ཡོད་དོ། །

[Block 1514]
དེ་ལྟ་ན་ཐོབ་པ་རྣམས་ཐུག་པ༌[^678]མེད་པར་ཐལ་བར་འགྱུར་བ་མ་ཡིན་ནམ། ཕན་ཚུན་ལྡན་པའི་ཕྱིར་ཐུག་པ་མེད་པར་ཐལ་བར༌[^679]མི་འགྱུར་རོ། །

[Block 1515]
ཆོས་བདག་ཉིད་གཏོགས་པ་གསུམ་སྐྱེ་སྟེ། ཆོས་དེ་དང་། དེའི་ཐོབ་པ་དང་། ཐོབ་པའི་ཐོབ་པའོ། །

[Block 1516]
དེ་ལ་ཐོབ་པ་སྐྱེས་པས་ཆོས་དེ་དང་། ཐོབ་པའི་ཐོབ་པ་དང་ལྡན་པར་འགྱུར་ལ། ཐོབ་པའི་ཐོབ་པ་སྐྱེས་པས་ཐོབ་པ་ཁོ་ན་དང་ལྡན་པར་འགྱུར་བས་དེའི་ཕྱིར་ཐུག་པ་མེད་པ་མ་ཡིན་ནོ། །

[Block 1517]
དེ་ལྟར་བྱས་ན་སྐད་ཅིག་མ་གཉིས་པ་ལ་དགེ་བའང་རུང་ཉོན་མོངས་པ་ཅན་ཡང་རུང་ཆོས་བདག་ཉིད་གཏོགས་པར་གསུམ་གྱི་ཐོབ་པ་གསུམ་སྐྱེ་བར་འགྱུར་ལ། དེ་དག་གི༌[^680]རྗེས་ཀྱི་ཐོབ་པ་ཡང་གསུམ་ཡིན་པས་དྲུག་ཏུ་འགྱུར་རོ། །

[Block 1518]
སྐད་ཅིག་མ་གསུམ་པ་ལ་ནི་སྐད་ཅིག་མ༌[^681]

[Block 1519]
དང་པོ་དང་གཉིས་པ་ལ་སྐྱེས་པའི་རྫས་རྣམས་ཀྱི་ཐོབ་པ་དགུ་པོ་རྗེས་ཀྱི་ཐོབ་པ་དང་བཅས་པས་བཅོ་བརྒྱད་དུ་འགྱུར་རོ། །

[Block 1520]
དེ་ལྟར་ཐོབ་པ་རྣམས་གོང་ནས་གོང་དུ་སྤེལ་བའི་འགྲེས་ཀྱིས་བསྐྱེད་ན་སྲོག་ཆགས་གཅིག་ལ་ཡང་སྐད་ཅིག་སྐད་ཅིག་ལ་འདས་པ་དང་མ་འོངས་པའི་ཉོན་མོངས་པ་དང་། ཉེ་བའི་ཉོན་མོངས་པ་དང་། སྐྱེས་ནས་ཐོབ་པའི་དགེ་བའི་སྐད་ཅིག་མ་མཚུངས་པར་ལྡན་པ་དང་ལྷན་ཅིག་འབྱུང་བར་བཅས་པ་ཐོག་མ་དང་ཐ་མ་མེད་པའི་འཁོར་བར་གཏོགས་པ་ཐམས་ཅད་ཀྱི་མཐའ་ཡས་པ་དག་སྐྱེ་བར་འགྱུར་བས་སེམས་ཅན་རྣམས་ཀྱི་སོ་སོའི་རྒྱུད་ཀྱི་ལུས་ཀྱི་སྐད་ཅིག་མ་ལ་རྫས་མཐའ་ཡས་པ་ཅན་དག་འབྱུང་ངོ་། །ཀྱེ་མ་འདི་ནི་ཐོབ་པ་རྣམས་ཀྱི་དགའ་སྟོན་ཆེན་པོ་ཞིག་སྟེ། དེ༌[^682]ཐོགས་པ་མེད་པས་འདི་ལྟར་གོ་སྐབས་རྙེད་ཀྱི། དེ་ལྟ་མ་ཡིན་ན་སྲོག་ཆགས་གཉིས་པའི་ནི་ནམ་མཁའ་ལ་གོ་སྐབས་ཡོད་པར་མི་འགྱུར་རོ། །

[Block 1521 [HEADING]]
#### སྐལ་བ་མཉམ་པ། ^2-3-3-0

[Block 1522]
ཡང་སྐལ་བ་མཉམ་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན། སྐལ་མཉམ་སེམས་ཅན་འདྲ་བའོ། །

[Block 1523]
སྐལ་བ་མཉམ་པ་ཉིད་ཅེས་བྱ་བའི་རྫས་ནི་སེམས་ཅན་རྣམས་ཀྱི་འདྲ་བ་ཡིན་ཏེ། བསྟན་བཅོས་ལས་ནི་འདིའི་མིང་རིས་མཐུན་པ་ཞེས་འབྱུང་ངོ་། །དེ་ཡང་ཐ་དད་པ་མ་ཡིན་པ་དང་། ཐ་དད་པ་སྟེ། ཐ་དད་པ་མ་ཡིན་པ་ནི། སེམས་ཅན་ཐམས་ཅད་སེམས་ཅན་དུ་སྐལ་བ་མཉམ་པ་སྟེ། ཐམས་ཅད་ལ་ཡང་སེམས་ཅན་རེ་རེ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1524]
ཐ་དད་པ་ནི་སེམས་ཅན་དེ་དག་ཉིད་ཁམས་དང་ས་དང་འགྲོ་བ་དང་། སྐྱེ་གནས་དང་། རིགས་དང་། ཕོ་དང་། མོ་དང་། དགེ་བསྙེན་དང་། དགེ་སློང་དང་། སློབ་པ་དང་། མི་སློབ་པ་ལ་སོགས་པའི་བྱེ་བྲག་གིས་སོ་སོར་ངེས་པའོ། །

[Block 1525]
ཆོས་ཀྱི་སྐལ་བ་མཉམ་པ་ནི་ཕུང་པོ་དང་སྐྱེ་མཆེད་དང་ཁམས་ཀྱི་སྒོ་ནས་སོ། །

[Block 1526]
གལ་ཏེ་སྐལ་བ་མཉམ་པ་ཞེས་བྱ་བའི་རྫས་ཁྱད་པར་མེད་པ་ཞིག་མེད་ན་ཕན་ཚུན་ཁྱད་པར་ཐ་དད་པའི་སེམས་ཅན་རྣམས་ལ་བྱེ་བྲག་མེད་པར་སེམས་ཅན༌[^683]ཞེས་བྱ་བའི་བློ་འཇུག་པ་དང་། འདོགས་པར་ཡང་མི་འགྱུར་ཏེ། ཕུང་པོ་ལ་སོགས་པའི་བློ་དང་འདོགས་པ་དག་ལ་ཡང་དེ་བཞིན་དུ་སྦྱོར་བར༌[^684]བྱའོ། །

[Block 1527]
འཆི་འཕོ་བར་ཡང་འགྱུར་ཞིང་སྐྱེ་བར་ཡང་འགྱུར་ལ། སེམས་ཅན་གྱི་སྐལ་བ་མཉམ་པ་ཉིད་འདོར་བར་ཡང་མི་འགྱུར་ཐོབ་པར་ཡང་མི་འགྱུར་བ་ཡོད་དམ་ཞེ་ན། མུ་བཞི་སྟེ། མུ་དང་པོ་ནི་གང་ནས་འཆི་འཕོ་བ་དེ་ཉིད་དུ་སྐྱེ་བ་ནའོ། །

[Block 1528]
གཉིས་པ་ནི་ངེས་པ་ལ་འཇུག་པ་ན་སྟེ། དེ་ནི་སེམས་ཅན་གྱི་སྐལ་བ་མཉམ་པ་ཉིད་འདོར་ཞིང་། འཕགས་པའི་སྐལ་བ་མཉམ་པ་ཉིད་འཐོབ་བོ། །

[Block 1529]
གསུམ་པ་ནི་འགྲོ་བ༌[^685]འཕོ་བ་ལས་སོ། །

[Block 1530]
བཞི་པ་ནི་རྣམ་པ་དེ་དག་མ་གཏོགས་པའོ། །

[Block 1531]
གལ་ཏེ་སོ་སོའི༌[^686]སྐྱེ་བོའི་སྐལ་བ་མཉམ་པ་ཉིད་ཅེས་བྱ་བའི་རྫས་ཤིག་ཡོད་ན་གོ་སོ་སོའི༌[^687]སྐྱེ་བོ་ཉིད་ཀྱིས་ཅི་ཞིག་བྱ་སྟེ། མིའི་སྐལ་བ་མཉམ་པ་ལས་ནི་མི་ཉིད་གུད་ན་བརྟག་ཏུ་མེད་དོ། །

[Block 1532]
འཇིག་རྟེན་གྱིས་ནི་སྐལ་བ་མཉམ་པ་ཉིད་གཟུགས་ཅན་མ་ཡིན་པའི་ཕྱིར་མི་མཐོང་བ་ཉིད་ལ། འདི་ཤེས་རབ་ཀྱིས་ཀྱང་ཡོངས་སུ་མི་ཆོད་མོད་ཀྱི། སེམས་ཅན་རྣམས་ཀྱི་རིགས་ཐ་མི་དད་པ་ཡང་ཁོང་དུ་ཆུད་དོ། །

[Block 1533]
དེ་ཡོད་དུ་ཆུག་ན་ཡང་དེ་ལས་ཇི་ལྟ་བུ་ཞིག་བྱེད། གཞན་ཡང་སེམས་ཅན་མ་ཡིན་པའི་སྐལ་བ་མཉམ་པ་ཉིད་ཀྱང་ཅིའི་ཕྱིར་མི་འདོད་དེ། སཱ་ལུ་དང་། ནས་དང་། མོན་སྲན་སྡེའུ་དང་། མོན་སྲན་གྲེའུ་དང་། ཨ་མྲ་དང་། ཤིང་པ་ན་ས་དང་། ལྕགས་དང་། གསེར་ལ་སོགས་པ་རྣམས་རང་གི་རིགས་འདྲ་བའི་ཕྱིར་རོ། །

[Block 1534]
སྐལ་བ་མཉམ་པ་ཕན་ཚུན་ཐ་དད་པ་དེ་དག་ཀྱང་ཇི་ལྟར་བྱེ་བྲག་མེད་པར་སྐལ་བ་མཉམ་པ་ཉིད་དུ་འདོགས་པར་བྱེད། དེ་ལྟ༌[^688]ན་ནི་བྱེ་བྲག་པ་རྣམས་ཀྱིས་གསལ་བར་བྱས་པ་ཡིན་ཏེ། དེ་དག་གི་གྲུབ་པའི་མཐའ་ནི་སྤྱི་ཞེས་བྱ་བའི་དངོས་པོ་ཞིག་ཡོད་དེ། དེས་ན་རྣམ་པ་མི་འདྲ་བ་རྣམས་ལ་ཡང་ཤེས་པ་མཚུངས་པ་སྐྱེའོ་ཞེས་བྱ་བ་འདི་ཡིན་ནོ། །

[Block 1535]
དེ་དག་གཅིག་ཡིན་ཡང་དུ་མ་ལ་འཇུག་པ་འདི་ནི་དེ་དག་གི་ཁྱད་པར་ཡིན་ནོ། །

[Block 1536]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་གལ་ཏེ་གསལ་བར་བྱས་ཀྱང་རུང་། གལ་ཏེ་གསལ་བར་མ་བྱས་ཀྱང་རུང་སྟེ། མདོ་ལས་འབྱུང་བའི་ཕྱིར་སྐལ་བ་མཉམ་པ་ནི་ཡོད་པ་ཁོ་ན་སྟེ། བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་བརྒྱ་ལ་མི་རྣམས་དང་སྐལ་བ་མཉམ་པ་འདི་ལྟ་བུ་ཉིད་དུ་འོང་ན་ཞེས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 1537]
དེ་སྐད་གསུངས་མོད་ཀྱི་རྫས་གཞན་ནོ་ཞེས་ནི་མ་གསུངས་སོ། །

[Block 1538]
འོ་ན་ཅི་ཞེ་ན། གང་དག་ལ་མི་ལ་སོགས་པར་འདོགས་པའི་འདུ་བྱེད་དེ་ལྟ་བུར་གྱུར་པ་དེ་དག་ཁོ་ནར་ཟད་དེ། སཱ་ལུ་ལ་སོགས་པའི་སྐལ་བ་མཉམ་པ་དང་འདྲའོ། །

[Block 1539]
དེ་སྐད་དུ་ནི་མི་བརྗོད་དོ། །

[Block 1540 [HEADING]]
#### འདུ་ཤེས་མེད་པ་པ། ^2-3-4-0

[Block 1541]
ཡང་འདུ་ཤེས་མེད་པ་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞེ་ན།

[Block 1542 [VERSE]]
འདུ་ཤེས་མེད་པ་པ་འདུ་ཤེས། །
མེད་པར་སེམས་དང་སེམས་བྱུང་རྣམས། །

[Block 1543]
འགོག་པའོ། །

[Block 1544]
འདུ་ཤེས་མེད་པའི་ལྷ་རྣམས་ཀྱི་ནང་དུ་སྐྱེ་བ༌[^689]དག་གི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་འགོག་པ་གང་ཡིན་པ་དེ་ནི་འདུ་ཤེས་མེད་པ་པ་ཞེས་བྱ་བའི་རྫས་ཡིན་ཏེ། གང་གིས་མ་འོངས་པའི་དུས་ཀྱི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་དུས་གཞན་གྱི་བར་དུ་ཀླུང༌[^690]གི་ཆུ་འགོག་པ་བཞིན་དུ་འགོག་ཅིང་སྐྱེར་མི་སྟེར་བའོ། །

[Block 1545]
དེ་ཡང་གཅིག་ཏུ་རྣམ་པར༌[^691]སྨིན། །གང་གི་རྣམ་པར་སྨིན་པ་ཡིན་ཞེ་ན། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པའི་ཡིན་ནོ། །
--- END BLOCKS ---
