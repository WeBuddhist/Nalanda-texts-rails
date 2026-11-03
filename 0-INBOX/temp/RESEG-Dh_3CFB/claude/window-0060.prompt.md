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
[Block 2101]
དེ་བས་ན་གདོན་མི་ཟ་བར་འཇིག་པ་དང་འབྲེལ་པར་རུང་བ་ཕྱིས་ཕུལ་དུ་བྱུང་བ་ཉེ་བར་བྱེད་པས་མེས་སྔ་ན་མེད་པ་བསྐྱེད་པའི་ཕྱིར། སྔ་མའི་གནས་སྐབས་ཅན་དེ་སྣང་བར་འགྱུར་རོ། །

[Block 2102]
ཤིང་འཇིག་པ་ཞེས་བྱ་བ་ཡང་ཤིང་མེད་པ་ཉིད་བརྗོད་པ་ཡིན་ལ། མེད་པ་ནི་འབྲས་བུ་ཡང་མ་ཡིན་ནོ། །

[Block 2103]
དེ་བྱེད་པ་ཡང་བྱེད་པ་པོ་ཉིད་མ་ཡིན་པའི་ཕྱིར་ལྟོས་པར་བྱ་བ་མ་ཡིན་ནོ། །ཞེས་བྱ་བ་ཡང་བཤད་ཟིན་ཏོ། །

[Block 2104]
རང་གི་ངོ་བོ་མེད་པ་དེ་ལས་ཐ་དད་པ་ཡིན་ན། དེ་ལས་བཟློག་པའི་དངོས་པོའི་ངོ་བོ་ཉིད་བསྒྲུབ་པར་འགྱུར་བའི་ཕྱིར་ཇི་ལྟར་ཞིག་པ་ཞེས་བྱ། དེ་བས་ན་གཞན་ནི་གཞན་གྱི་འཇིག་པ་མ་ཡིན་ནོ། །

[Block 2105]
བླ་སྟེ་ཅི་ཕྱིར་ཤིང་མི་སྣང་། །དོན་གཞན་འབྱུང་བ་དང་ཤིང་མཐོང་བ་འདི་ལ་འགལ་བ་ཅི་ཡོད།། །།

[Block 2106]
བམ་པོ་དགུ་པ།

[Block 2107]
གལ་ཏེ་དེ་གཟུང་ཕྱིར་ནའང་མིན། །གང་ཕྱིར་དེས་ན་སྒྲིབ་བྱེད་མེད། །

[Block 2108]
གལ་ཏེ་དོན་གཞན་དེས་ཡོངས་སུ་གཟུང་བའི་ཕྱིར། ཤིང་མི་སྣང་བ་ཡིན་ན་དེ་ནི་ཤིང་ལ་སྒྲིབ་པར་བྱེད་དོ་ཞེས་བྱ་བར་འཐོབ་ན། དེ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2109]
སྒྲིབ་པར་བྱེད་པ་ནི་མཐོང་བའི་གེགས་བྱེད་པར་འགྱུར་གྱི། ཐོགས་པར་བྱེད་པ་ལ་སོགས་པ་རྫས་ཀྱི་ནུས་པ་དག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2110]
ཐམས་ཅད་ལ་གེགས༌[^1514]བྱེད་པ་ཡིན་ན་ཡང་དེ་འདི་ཉིད་ཀྱིས་ནུས་པ་ཐམས་ཅད་ཉམས་པའི་ཕྱིར། རྫས་འཇིག་པར་འགྱུར་བ་མ་ཡིན་ནམ། དེ་ལ་ཡང་མེ་དང་འདྲ་བར་ཐལ་བ་དང་། ཐུག་པ་མེད་པར་འགྱུར་རོ། །

[Block 2111]
འདིའི་ཐོགས་པར་བྱེད་པའི་ནུས་པ་ལ་སོགས་པ་ཉམས་པ་མེད་པ་དག་གཞན་ཡོད་པ་དེས་ཅི་ཞིག་འཇིག་པར་འགྱུར། གལ་ཏེ་མེ་ལས་བྱུང་བ་ཅན་གྱི་འཇིག་པ་ཞེས་བྱ་བས་དོན་གྱིས༌[^1515]ཡོངས་སུ་གཟུང་བའི་ཕྱིར།

[Block 2112 [VERSE]]
ཤིང་མ་མཐོང་བ་ཡིན་ན་ནི། །
སྐྱེ་ཕྱིར་འཇིག་པའི་འཇིག་ཅན༌[^1516]འགྱུར། །

[Block 2113]
དེ་ཕྱིར་ཤིང་ཡང་མཐོང་བར་འགྱུར། གདོན་མི་ཟ་བར་སྐྱེ་བ་དང་ལྡན་པ་ནི་འཇིག་པའི་སྒོ་ནས་འཇིག་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 2114]
འཇིག་པ་དེ་ལས་ཀྱང་ཤིང་ལ་སོགས་པ་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2115 [VERSE]]
གལ་ཏེ་གསོད་བྱེད་བསད་པ༌[^1517]ན། །
དཔེར་ན་ནག་པ་ཡང་སྲིན༌[^1518]མིན། །
འདི་ཡང་དེ་བཞིན་ཡིན་ཞེ་ན། །
གསོད་བྱེད་བསད་མེད་ཕྱིར་མ་ཡིན། །

[Block 2116]
གལ་ཏེ་འཇིག་པ་ཞིག་པ་ཡིན་དུ་ཟིན་ཀྱང་དངོས་པོ་ཕྱིར་ཐོབ་པ་མ་ཡིན་ཏེ། གསོད་པར་བྱེད་པ་བསང་དུ་ཟིན་ཀྱང་དེས་བསད་པའི་ཕྱིར་སྐྱེ་བ་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། གསོད་པར༌[^1519]བྱེད་པ་ནི་དེ་གསོད་པའི་བྱེད་པའི་རྒྱུ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2117]
འཇིག་པའི་རྒྱུ་མེད་པ་དང་དབྱུག་པ་ལ་སོགས་པ་ལ༌[^1520]ལོག་པ་ན། དངོས་པོར་འགྱུར་རོ་ཞེས་ནི༌[^1521]མི་སྨྲའོ། །

[Block 2118]
འོ་ན་ཅི་ཡིན་ཞེ་ན། ཤིན་ཏུ་དམིགས་སུ་མེད་པའི་མཚན་ཉིད་ཅན་གྱི་དངོས་པོ་མེད་པ་དེ་ལོག་པ་ན་རང་བཞིན་གནས་པ་ལས་རྣམ་པ་གཞན་ཅི་ཡོད། ནག་པའི་གསོད་པར་བྱེད་པ་འཇིག་པ་དང་མཚུངས་པ་མ་ཡིན་ནོ། །

[Block 2119]
འོ་ན་ཅི་ཡིན་ཞེ་ན། དབྱུག་པ་ལ་སོགས་པ་དང་མཚུངས་པ་ཡིན་ནོ། །

[Block 2120]
འཇིག་པ༌[^1522]འདྲ་བ་ནི་འདི་བསད་པ་ཡིན་ལ། དེ་ལོག་པ་ན་འདི་ཡང་འབྱུང་བ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2121 [VERSE]]
འཇིག་པ་གཞན་ཉིད་མ་ཡིན་ནའང་། །
ཤིང་ཉིད་འཇིག་པ་ཉིད་དུ་འགྱུར། །
དེ་ཡོད་ཉིད་ཕྱིར་རྒྱུ་ཅན་མིན། །
འདི་ལས་གཞན་པའི་རྣམ་པའང་མེད། །

[Block 2122]
ཤིང་ལས་འཇིག་པ་དོན་གཞན་དུ་འགྱུར་བ་ཉིད་མ་ཡིན་ན་དེ་ཉིད་དེར་འགྱུར་རོ། །

[Block 2123]
དེ་ཡང་སྔར་ཡོད་པ་ཉིད་ཀྱི་ཕྱིར། འདི་ལ་མེ་ལ་སོགས་པའི་ནུས་པ་ཅི་ཞིག་བྱ། དེ་བས་ན་དེ་ལ་ཕན་འདོགས་པའི་ཕྱིར་དེས་རྣམ་པ་འགའ་ཞིག་གིས་ཀྱང་ལྟོས་པར་འགྱུར་བ་མེད་དོ། །

[Block 2124]
འདིའི་འདི་ཞེས་བྱ་བའི་འགྲེལ་པ་རིགས་པ་མ་ཡིན་ཏེ། དེ་ནི་ཕན་འདོགས་པར་བྱེད་པའི་རྒྱུ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2125]
དེ་ལྟ་མ་ཡིན་ན་ཐལ་ཆེས་པའི་ཕྱིར་རོ། །

[Block 2126]
བརྒྱུད་པས་ཕན་འདོགས་པར་བྱེད་པ་ཡིན་ན་ཡང་། ཅི་ཕན་འདོགས་པར་བྱེད་པ་དོན་གཞན་དུ་གྱུར་པའམ། འོན་ཏེ་དེ་ཉིད་ཡིན་ནོ་ཞེས་གདོན་མི་ཟ་བར༌[^1523]རྣམ་པར་རྟོག་པ་འདི་འཇུག་པ་ཡིན་ནོ། །

[Block 2127]
དེ་ལས་དོན་གཞན་དུ་གྱུར་པ་ཉིད་ཡིན་པ་དང་། དེ་གཞན་མ་ཡིན་པ་ཉིད་མ་ཡིན་ན་ཡང་དེའི་ཞེས་བྱ་བ་ཕན་འདོགས་པར༌[^1524]བྱེད་པ་ཉིད་ལ་སོགས་པ་ཡང་དེའི་གནས་སྐབས་ཀྱིས༌[^1525]བརྒལ་ཞིང་བརྟག་པ་ཡིན་ནོ། །

[Block 2128]
དེ་བས་ན་ཡོད་པ་ཉིད་ཀྱི་ངོ་བོ་ནི་དེ་ཉིད་དང་གཞན་ཉིད་ལས་མ་འདས་པའི་ཕྱིར་དང་། ཕན་འདོགས་པ་སྐྱེད་པར་བྱེད་པའི་ངོ་བོ་སྒྲུབ་པར་བྱེད་པའི་མཚན་ཉིད་ཅན་ཉིད༌[^1526]ཡིན་པའི་ཕྱིར་དེ་དང་དེ་མ་ཡིན་པ་བྱེད་པ་དང་བྲལ་བ༌[^1527]བྱེད་པ་པོ་མ་ཡིན་པས་ན་འགའ་ཞིག་གི་རྒྱུ་མ་ཡིན་ཞིང་། རྒྱུ་མ་ཡིན་པ་ལ་ཡང་ལྟོས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2129]
དེ་བས་ན་དངོས་པོ་འདིའི་བདག་ཉིད་དེའི་རང་བཞིན་ཡིན་ནོ་ཞེས་བྱ་བར་གྲུབ་པོ། །

[Block 2130 [VERSE]]
གལ་ཏེའང་འཇིག་རྒྱུ་མེད་ཅན་ཡིན། །
རྟག་ཉིད་ཕྱིར་ན་དངོས་འཇིག་དག །
ལྷན་ཅིག་འབྱུང་བར་ཐལ་བར་འགྱུར། །
གང་ལས་མེ་ཉིད་རྟག་ཉིད་ཡིན། །

[Block 2131]
དེ་ལྟར་ནི་འགྱུར་ན་གང་གིས་འཇིག་པ་རྒྱུ་མེད་པ་ཅན་ཡིན་ན་ཡང་དེ་གདོན་མི་ཟ་བར་རྟག་པ་ཡིན་པས་ན་དངོས་པོ་དང་འཇིག་པ་དེ་མེད་པའི་མཚན་ཉིད་ཅན་དག་ལྷན་ཅིག་འབྱུང་བར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་ལ་རྟག་པ་དང་མི་རྟག་པའི་ཆོས་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 2132]
མེད་པ་ལ་རྣམ་པར་རྟོག་པ་འདི་ནི་ཡོད་པ༌[^1528]མ་ཡིན༌[^1529]ཏེ། དེ་དག་ནི་དངོས་པོའི་ཆོས་ཉིད་ཡིན་པའི་ཕྱིར། འཇིག་པ་ནི་ཅི་ཡང་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2133]
འབྱུང་བ་ནི་འགའ་ཞིག་དང་ལྷན་ཅིག་འབྱུང་བར་འགྱུར་ཞིང་། འཇིག་པ་ནི་མི་འགྱུར་བ་དེ་བས་ན་སྐྱོན་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2134 [VERSE]]
མེད་ལ་དངོས་འཇིག་མེད་ཉིད་ཀྱི། །
ཐལ་བར་འགྱུར་བའང་མི་རུང་སྟེ། །
གང་ཕྱིར་དངོས་པོ་འཇིག་པ་ཡིས།

[Block 2135]
[^1530] །འཇིག་པ་དག་ནི་མི་འདོད་དོ། །

[Block 2136]
ཇི་ལྟར་ན་མེད་པའི་འཇིག་པས་དངོས་པོ་འཇིག་པར་འགྱུར། །དེ་བས་ན་དངོས་པོ་འཇིག་པ་ཅན་དུ་མི་འགྱུར་རོ། ། ཞེས་བྱ་བ་ཡང་ཐལ་བར་འགྱུར་བ་ཉིད་མ་ཡིན་ཏེ། འཇིག་པ་ལས་དངོས་པོ་ཞིག་པ་ཁས་མི་ལེན་པའི་ཕྱིར་རོ། །

[Block 2137]
འཇིག་པ་ཞེས་བྱ་བ་ཅུང་ཞིག་ཀྱང་མེད་དོ་ཞེས་སྨྲ་བ་གང་ཡིན་པ་དེ་ཇི་ལྟར་དེ་ལས་དངོས་པོ་ཞིག་པར་འདོད། ད་ནི་འཇིག་པ་མེད་པ་ཡིན་ན་ཇི་ལྟར་དངོས་པོ་འཇིག་པ་ཞེས་བྱ། ད་ལྟར་བྱུང་བའི་གནས་སྐབས་འཇིག་པ་མེད་པ་ཅན་འཇིག་པར་མི་འགྱུར། [^1531]གང་ཞིག་གང་གིས་དེ་དང་ལྡན་པ་མ་ཡིན་པ༌[^1532]དེ་དེས་དེ་ལྟར་ཐ་སྙད་འདོགས་པ༌[^1533]འམ། ཤེས་པ་མ་ཡིན་ཏེ། དཔེར་ན་རྟ་ལ་རྭས་ཐ་སྙད་མི་འདོགས་པ་བཞིན་ནོ། །

[Block 2138]
འཇིག་པ་མེད་པ་ཉིད་མ་ཡིན་མོད་ཀྱི་དངོས་པོའི་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། དངོས་པོའི་སྐད་ཅིག་མར་གནས་པའི་ཆོས་ཅན་འཇིག་པ་ཡིན་ནོ། །

[Block 2139]
འདིའི་རང་བཞིན་དེ་དུས་ཕྱིས་འདི་འཇིག་པར་འགྱུར་བ་ཞེས་ངེས་པར་བྱས་ནས་ཇི་ལྟར་ཤེས་པ་བཞིན་དུ་ཐ་སྙད་འདོགས་པར་བྱེད་དོ། །ཞེས་བྱ་བ་ནི་བཤད་ཟིན་ཏོ། །

[Block 2140]
དངོས་པོ་ཅུང་ཞིག་ཀྱང་འགའ་ཞིག་གི་ཚེ་ཡང་འགྱུར་བ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
