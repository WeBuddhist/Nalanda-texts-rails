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
[Block 2031 [VERSE]]
འགྱོད་དང་ཕྲག་དོག་ཁོང༌[^1486]ཁྲོ༌[^1487]དང་། །
རྣམ་འཚེ་ཁོན་དུ་འཛིན་པ་དང་། །
འཆབ་པ༌[^1488]ཡིད་མི་བདེ་བ་དང་། །

[Block 2032]
མཚུངས་པར་ལྡན་པ༌[^1489]ཞེས་བྱ་བར་སྦྱར་ཏེ། འདི་དག་ནི་སྐྱོ་བའི་རྣམ་པར་འཇུག་པའི་ཕྱིར་དང་ཡིད་ཀྱི་ས་པ་ཡིན་པའི་ཕྱིར་དང་།[^1490] སེར་སྣ་དག་གི༌[^1491]བཟློག་པ་ཡིན། །ཡིད་བདེ་བ་དང་མཚུངས་པར་ལྡན་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2033]
[^1492]ཆགས་པའི་རྒྱུ་ལས་བྱུང་བ༌[^1493]དགའ་བའི་རྣམ་པར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 2034]
གཡོ་དང་སྒྱུ་དང་རྒྱགས་འཆབ་གཉིད།[^1494] །གཉི་ག་དང་ལྡན། ཡིད་བདེ་བ་དང་ཡིད་མི་བདེ་བ་དག་དང་མཚུངས་པར་ལྡན་ཏེ། རེས་འགའ་ནི་ཡིད་བདེ་བ་དག་གིས་ཕ་རོལ་པོ་འདྲིད་པར་བྱེད་ལ། རེས་འགའ་ནི་ཡིད་མི་བདེ་བ་དག་གིས་ཏེ། གཉིད་ཀྱི་བར་དུ་ཡང་དེ་དང་འདྲའོ། །

[Block 2035]
བདེ་དག་དང་། རྒྱགས་པ། བསམ་གཏན་གསུམ་པ་ན་ནི་བདེ་བ་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 2036]
མན་ཆད་ན་ནི་ཡིད་བདེ་བ་དང་མཚུངས་པར་ལྡན་ནོ། །

[Block 2037]
ཡན་ཆད་ན་ནི་བཏང་སྙོམས་དང་མཚུངས་པར་ལྡན་ནོ།[^1495] །འདི་ལྟར་བཏང་སྙོམས་ཀུན་དུ་འགྲོ། །ཐམས་ཅད་བཏང་སྙོམས་དང་མཚུངས་པར་ལྡན་ཏེ། དེ་ནི་མ་རིག་པ་བཞིན་དུ་གང་ལ་ཡང་འགག་པ༌[^1496]མེད་དོ། །

[Block 2038]
བཞི་པོ་གཞན་ནི་ལྔ་དག་དང་། །ངོ་ཚ་མེད་པ་དང་། ཁྲེལ་མེད་པ་དང་། རྨུགས་པ་དང་། རྒོད་པ་དང་། ཀུན་ནས་དཀྲིས་པ་བཞི་པོ་འདི་དག་ནི་དབང་པོ་ལྔ་ཆར་དང་མཚུངས་པར་ལྡན་ཏེ། མི་དགེ་བའི་ས་མང་པོ་པ་ཡིན་པའི་ཕྱིར་དང་། ཉོན་མོངས་པའི་ས་མང་པོ་པ༌[^1497]ཡིན་པའི་ཕྱིར་རོ། །

[Block 2039 [HEADING]]
### སྒྲིབ་པ་ལྔ། ^2-31-0

[Block 2040]
མདོ་ལས།

[Block 2041]
འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་དང་། རྨུགས་པ༌[^1498]དང་། གཉིད་དང་། རྒོད་པ་དང་། འགྱོད་པ་དང་། ཐེ་ཚོམ་དང་སྒྲིབ་པ་ལྔ་གསུངས་པ་གང་དག་ཡིན་པ་དེ་ལ་ཅི་རྨུགས་པ་དང་། རྒོད་པ་དང་། ཐེ་ཚོམ་ཁམས་གསུམ་པ་དག་བཟུང༌[^1499]ངམ། འོན་ཏེ་འདོད་པ་དང་མཚུངས་པར་ལྡན་པ་དག་ཁོ་ན་གཟུང་ཞེ་ན།

[Block 2042]
མདོ་ལས།

[Block 2043]
འདི་ནི་མི་དགེ་བའི་ཕུང་པོ་མ་འདྲེས་པ་ཡོངས་སུ་རྫོགས་པ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། སྒྲིབ་པ་ལྔའོ་ཞེས་གཅིག་ཏུ་མི་དགེ་བར་གསུངས་པའི་ཕྱིར་དང་། [^1500]འདོད་ན་སྒྲིབ་རྣམས། ཡོད་ན༌[^1501]ཁམས་གཞན་ན་ནི་མེད་དོ། །

[Block 2044]
ཅིའི་ཕྱིར་རྨུགས་པ་དང་གཉིད་གཉིས་ཀྱང་སྒྲིབ་པ་གཅིག་ཏུ་བཤད་ལ། རྒོད་པ་དང་འགྱོད་པ་གཉིས་ཀྱང་གཅིག་ཏུ་བཤད་ཅེ་ན། མི་མཐུན་དང་། ཟས་དང་བྱ་བ་གཅིག་པའི་ཕྱིར། །གཉིས་གཅིག །གཉིས་གཅིག་ཏུ་བྱས་པ་ནི་གཉིས་གཅིག་གོ། །

[Block 2045]
མི་མཐུན་པ་དག༌[^1502]དང་། གཉེན་པོ་དང་། ཟས་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་དོན་གཅིག་གོ། །

[Block 2046]
མདོ་ལས་རྨུགས་པ་དང་། གཉིད་དག་གི་ཟས་ཀྱང་གཅིག །ཟས་མ་ཡིན་པ་ཡང་གཅིག་ཏུ་གསུངས་ཏེ། རྨུགས་པ་དང་གཉིད་ཀྱི་སྒྲིབ་པའི་ཟས་གང་ཞེ་ན། ཆོས་ལྔ་སྟེ། རྨྱ་བ་དང་། མི་དགའ་བ་དང་། བྱ་རྨྱང༌[^1503]དང་། ཁ་ཟས་ཀྱི་དྲོད་མི་ཟིན་པ་དང་། སེམས་ཞུམ་པ་ཉིད་དོ། །

[Block 2047]
རྨུགས་པ༌[^1504]དང་གཉིད་ཀྱི་སྒྲིབ་པའི་ཟས་མ་ཡིན་པ་གང་ཞེ་ན། སྣང་བའི་འདུ་ཤེས་སོ། །

[Block 2048]
འདི་གཉིས་ཀྱི་བྱ་བ་ཡང་གཅིག་སྟེ། འདི་གཉི་གས་ཀྱང་སེམས་ཞུམ་པར་བྱེད་དོ། །

[Block 2049]
རྒོད་པ་དང་འགྱོད་པ་དག་གིས་ཀྱང༌[^1505]ཟས་ཀྱང་གཅིག །ཟས་མ་ཡིན་པ་ཡང་གཅིག་ཏུ་གསུངས་ཏེ། རྒོད་པ་དང་འགྱོད་པའི༌[^1506]ཟས་གང་ཞེ་ན། ཆོས་བཞི་སྟེ། ཉེ་དུའི་རྣམ་པར་རྟོག་པ་དང་། ཡུལ་གྱི་རྣམ་པར་རྟོག་པ་དང་། མི་འཆི་བའི་རྣམ་པར་རྟོག་པ་དང་། སྔོན་དགོད་པ་དང་། རྩེས་པ་དང་། དགའ་བ༌[^1507]དང་། དགའ་མགུར་ཡོངས་སུ་སྤྱད་པ་རྣམས་རྗེས་སུ་དྲན་པ་ཡིན་ནོ། །

[Block 2050]
རྒོད་པ་དང་འགྱོད་པའི་སྒྲིབ་པའི་ཟས་མ་ཡིན་པ་གང་ཞེ་ན། ཞི་གནས་སོ། །

[Block 2051]
འདི་གཉིས་ཀྱི་བྱ་བ་ཡང་གཅིག་སྟེ། འདི་གཉི་གས་ཀྱང་སེམས་རྣམ་པར་མ་ཞི་བར་བྱེད་དོ། །

[Block 2052]
དེ་ལྟ་བས་ན་མི་མཐུན་པ་དང་། ཟས་དང་བྱ་བ་གཅིག་པའི་ཕྱིར་གཉིས་གཅིག་ཏུ་བཤད་དོ། །

[Block 2053]
གང་གི་ཚེ་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱང་སྒྲིབ་པ་ཡིན་ན་ཅིའི་ཕྱིར་ལྔ་ཁོ་ནར་བཤད་ཅེ་ན། ཕུང་པོ་གནོད་བྱེད་དང་། ཐེ་ཚོམ་ཕྱིར་ན་ལྔ་ཉིད་དོ། །

[Block 2054]
འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་དག་གིས་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕུང་པོ་ལ་གནོད་པར་བྱེད་དོ། །

[Block 2055]
རྨུགས་པ་དང་གཉིད་ཀྱིས་ནི་ཤེས་རབ་ཀྱི་ཕུང་པོ་ལ་གནོད་པར་བྱེད་དོ། །

[Block 2056]
རྒོད་པ་དང་འགྱོད་པས་ནི་ཏིང་ངེ་འཛིན་གྱི་ཕུང་པོ་ལ་གནོད་པར་བྱེད་དོ། །

[Block 2057]
ཏིང་ངེ་འཛིན་དང་ཤེས་རབ་དག་མེད་ན། བདེན་པ་དག་ལ་ཐེ་ཚོམ་ཟ་བར་འགྱུར་ཏེ། དེའི་ཕྱིར་ལྔར༌[^1508]བཤད་དོ། །

[Block 2058]
གཞན་དག་ན་རེ་རྟོག་པ་འདི་ལ༌[^1509]ནི་ཏིང་ངེ་འཛིན་གྱི་ཕུང་པོ་དང་འགལ་བ་རྒོད་པ་དང་འགྱོད་པའི་སྒྲིབ་པ་སྔར་སྨོས་པར་འགྱུར་ཏེ། དེའི་ཕྱིར་གྲངས་བཞིན་དུ་འདི་གཉིས་ཀྱི༌[^1510]ཏིང་ངེ་འཛིན་དང་ཤེས་རབ་ཀྱི་ཕུང་པོ་ལ་གནོད་པར༌[^1511]བྱེད་པ་ཡིན་ཏེ། ཏིང་ངེ་འཛིན་ལ་བརྩོན་པ་ནི་རྨུགས་པ་དང་གཉིད་ཀྱིས་འཇིགས་ལ། ཆོས་རབ་ཏུ་རྣམ་པར་འབྱེད་པ་ལ་བརྩོན་པ་ནི་རྒོད་པ་དང་། འགྱོད་པས་འཇིགས་སོ་ཞེས་ཟེར་རོ། །

[Block 2059]
གཞན་དག་ནི་གཞན་དུ་བརྗོད་དོ། །ཇི་སྐད་དུ་བརྗོད་ཅེ་ན། རྒྱུ་བར་གྱུར་པས་གཟུགས་སྡུག་པ་དང་མི་སྡུག་པའི་ཡུལ་དག་ལ་མཚན་མར་གཟུང་བའི་ཕྱིར་གནས་པར་གྱུར་པའི་ཏིང་ངེ་འཛིན་དུ་འཇུག་པ་ལ། དེ་སྔོན་དུ་འགྲོ་བའི་འདོད་པ་ལ་འདུན་པ་དང་། གནོད་སེམས་དག་དང་པོ་ཉིད་དུ་བར་ཆད་བྱེད་དོ། །

[Block 2060]
དེའི་འོག་ཏུ་ཏིང་ངེ་འཛིན་དུ་ཞུགས་པས་རིགས་པ་མ་ཡིན་པར་ཞི་གནས་ལྷག་མཐོང་བསྟན་པའི༌[^1512]ཕྱིར་གོ་རིམས་བཞིན་དུ་རྨུགས་པ་དང་། གཉིད་དང་། རྒོད་པ་དང་། འགྱོད་པ་དང་། ཐེ་ཚོམ་ནི་ཞི་གནས་དང་ལྷག་མཐོང་དག་ལ་བར་ཆད་བྱེད་ལ། ལངས་པ་ལ་ཡང་ཆོས་ལ་ངེས་པར་རྟོག་པའི་ཚེ་ཐེ་ཚོམ་གྱི༌[^1513]བར་ཆད་བྱེད་དེ། དེའི་ཕྱིར་སྒྲིབ་པ་ལྔར་བཤད་དོ་ཞེས་བརྗོད་དོ། །

[Block 2061 [HEADING]]
### ཉོན་མོངས་པ་སྤོང་བའི་རྣམ་པ་བཞི། ^2-32-0

[Block 2062]
འདི་དཔྱད་པར་བྱ་སྟེ། སྐལ་བ་མི་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་རྣམས་དང་། འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་རྣམས་གང་གི་ཚེ་དམིགས་པ་ཡོངས་སུ་ཤེས་པ་དེའི་ཚེ་ནི་སྤོང་བར་མི་འགྱུར་ལ། གང་གི་ཚེ་སྤོང་བར་འགྱུར་ལ༌[^1514]དེའི་ཚེ་ནི་དམིགས་པ་ཡོངས་སུ་མི་ཤེས་ན་ཇི་ལྟར་དེ་དག་སྤོང་ཞེ་ན། ཉོན་མོངས་པ་རྣམས་ནི་དམིགས་པ་ཡོངས་སུ་ཤེས་པས་ཟད་པར་ངེས་པ་མ་ཡིན་ནོ། །

[Block 2063]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། རྣམ་པ་བཞིས་སོ། །

[Block 2064]
རྣམ་པ་བཞི་པོ་གང་དག་གིས་ཤེ་ན། རེ་ཞིག་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་ནི། དམིགས་པ་ཡོངས་སུ་ཤེས་པ་དང་།

[Block 2065 [VERSE]]
དེ་ལ་དམིགས་པ་ཡང་དག་པར། །
ཟད་དང་དམིགས་པ་སྤངས་པས་སོ། །

[Block 2066 [HEADING]]
#### དམིགས་པ་ཡོངས་སུ་ཤེས་པ། ^2-32-1-0

[Block 2067]
དེ་ལ་དམིགས་པ་ཡོངས་སུ་ཤེས་པས་ནི་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་བ༌[^1515]མཐོང་བས་སྤང་བར་བྱ་བ་རང་གི་ས་ལ་དམིགས་པ་རྣམས་དང་། འགོག་པ་དང་ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ཟག་པ་མེད་པ་ལ་དམིགས་པ་རྣམས་ཟད་པར་འགྱུར་རོ། །

[Block 2068 [HEADING]]
#### དམིགས་པ་ཡང་དག་པར་ཟད་པ། ^2-32-2-0

[Block 2069]
དེ་ལ་དམིགས་པ་ཡང་དག་པར་ཟད་པས་ནི་སྐལ་བ་མི་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་རྣམས་ཟད་པར་འགྱུར་ཏེ། དེ་ལ་དམིགས་པ་ནི་སྐལ་བ་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་དག་ཡིན་པས་དེ་དག་སྤངས་ན་དེ་དག་ཀྱང་སྤང་བ༌[^1516]ཡིན་ནོ། །

[Block 2070 [HEADING]]
#### དམིགས་པ་སྤངས་པ། ^2-32-3-0
--- END BLOCKS ---
