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
[Block 2136]
འདོད་པའི་ཁམས་ཁོ་ན་ན་འགོག་པ་མཐོང་བས་སྤང་བར་བྱ་བའི་རྣམ་པ་སྤངས་པ་ནི་ཡོངས་སུ་ཤེས་པ་གཅིག་ཡིན་ལ། ལམ་མཐོང་བས་སྤང་བར་བྱ་བའི་རྣམ་པ་སྤངས་པ་ཡང་གཅིག་ཡིན་ནོ། །

[Block 2137]
ཇི་ལྟར་འདོད་པ་ན་སྤྱོད་པའི༌[^1567]མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ཡོངས་སུ་ཤེས་པ་གསུམ་ཡིན་པ་ལྟར། དེ་བཞིན་གོང་མའི་དེ་གསུམ་ཉིད། །དེ་བཞིན་དུ་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པའི༌[^1568]མཐོང་བས་སྤང་བར་བྱ་བའི་རྣམ་པ༌[^1569]སྤངས་པ་ཡང་ཡོངས་སུ་ཤེས་པ་གསུམ་ཡིན་ཏེ། སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ནི་གཅིག་ཡིན་ནོ། །

[Block 2138]
འགོག་པ་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ནི་གཉིས༌[^1570]ཡིན་ནོ། །

[Block 2139]
ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ནི་གསུམ༌[^1571]ཡིན་ནོ། །

[Block 2140]
དེ་ལྟར་ན་ཁམས་གསུམ་པའི་ཕྱིར༌[^1572]མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ནི་ཡོངས་སུ་ཤེས་པ་དྲུག་ཡིན་ནོ། །

[Block 2141]
ཡོངས་སུ་ཤེས་པ་གཞན་གསུམ་སྟེ་ཐ་མའི་ཆ་དང་མཐུན་གཟུགས་དང་། ཟག་པ་ཀུན་ཟད། ཐ་མའི་ཆ་དང་མཐུན་པ་སྤངས་པ་ཡང་། ཡོངས་སུ་ཤེས་པ་གཅིག་ཡིན་ནོ། །

[Block 2142]
གཟུགས་ཀྱི་ཟག་པ་སྤངས་པ་ཡང་གཅིག་ཡིན་ཏེ། གཟུགས་ཀྱི་འདོད་ཆགས་ཟད་པའི་ཡོངས་སུ་ཤེས་པའོ། །

[Block 2143]
ཟག་པ་ཐམས་ཅད་སྤངས་པ་ཡང་གཅིག་ཡིན་ཏེ། ཀུན་དུ་སྦྱོར་བ་ཐམས་ཅད་ཡོངས་སུ་གཏུགས་པའི་ཡོངས་སུ་ཤེས་པའོ། །

[Block 2144]
ཅིའི་ཕྱིར་གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་བསྒོམ་པས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པའི་ཡོངས་སུ་ཤེས་པ་ནི་ཐ་དད་པར་བསྟན་ལ་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་ཀྱི་ནི་མ་ཡིན་ཞེ་ན། བསྒོམ་པས་སྤོང་བར༌[^1573]བྱ་བ་རྣམས་ཀྱི་གཉེན་པོ་མི་འདྲ་བའི་ཕྱིར་རོ། །

[Block 2145]
དེ་ལྟར་ན་ཡོངས་སུ་ཤེས་པ་ནི་དེ་དགུ་ཡིན་ནོ། །

[Block 2146 [HEADING]]
##### ཡོངས་སུ་ཤེས་པའི་འབྲས་བུ། ^2-38-2-2-0

[Block 2147]
དེ་དག་ལས།

[Block 2148]
སྔ་མ་དྲུག་བཟོད་འབྲས། མཐོང་བས་སྤང་བར་བྱ་བ་སྤངས་པའི་རང་བཞིན་གང་དག་ཡིན་པའོ། །

[Block 2149]
ལྷག་མ་རྣམས་ནི་ཤེས་པ་ཡིས།[^1574] །ཐ་མའི་ཆ་དང་མཐུན་པ་སྤངས་པ་ལ་སོགས་པའི་ཡོངས་སུ་ཤེས་པ་སྟེ། བསྒོམ་པའི་ལམ་གྱི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2150]
ཇི་ལྟར་ཡོངས་སུ་ཤེས་པ༌[^1575]བཟོད་པའི་འབྲས་བུ་ཡིན་ཞེ་ན། བཟོད་པ་རྣམས་ནི་ཤེས་པའི་འཁོར་ཅན་ཡིན་པའི་ཕྱིར་ཏེ། རྒྱལ་པོའི་འཁོར་ལ་རྒྱལ་པོ་ཉེ་བར་བཏགས་པ་བཞིན་པ་དང་། ཤེས་པ་དང་འབྲས་བུ་གཅིག་པའི་ཕྱིར་རོ། །

[Block 2151 [VERSE]]
མི་ལྕོགས་མེད་འབྲས་ཐམས་ཅད་དོ། །
བསམ་གཏན་རྣམས་ཀྱི་ལྔའམ་བརྒྱད། །

[Block 2152]
བྱེ་བྲག་ཏུ་སྨྲ་བའི་ལུགས་ཀྱིས་ནི་བསམ་གཏན་གྱི༌[^1576]དངོས་གཞིའི་འབྲས་བུ་ཡོངས་སུ་ཤེས་པ་ལྔ་སྟེ། གཟུགས་དང་། གཟུགས་མེད་པ་ལ༌[^1577]སྤྱོད་པའི་ཉོན་མོངས་པ་སྤོངས་པའི༌[^1578]རང་བཞིན་གང་དག་ཡིན་པའོ། །

[Block 2153]
འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་སྤངས་པ་རྣམས༌[^1579]ནི་མི་ལྕོགས་པ་མེད་པའི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2154]
བཙུན་པ་དབྱངས་སྒྲོགས་ཀྱི་ལུགས་ཀྱིས་ནི་བརྒྱད་དེ། དེ་ནི་འདོད་ཆགས་དང་བྲལ་བས་འདོད་པ་ན་སྤྱོད་པའི་མཐོང་བས་སྤང་བར་བྱ་བ་རྣམས་སྤངས་པ་ཡང་བྲལ་བའི་ཐོབ་པ་ཟད་པ༌[^1580]མེད་པ་རྙེད་པའི་ཕྱིར་མཐོང་བའི་ལམ་གྱི་འབྲས་བུར་འདོད་དོ། །

[Block 2155]
ཐ་མའི་ཆ་དང་མཐུན་པ་སྤངས་པའི་ཡོངས་སུ་ཤེས་པ་ནི་མི་ལྕོགས་པ་མེད་པའི་འབྲས་བུ་ཁོ་ན་ཡིན་ནོ། །

[Block 2156]
བསམ་གཏན་ཁྱད་པར་ཅན་ཡང་བསམ་གཏན་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 2157]
གཟུགས་མེད་པ་རྣམས་ཀྱིས་ནི་ཉེ་བར༌[^1581]བསྡོགས་པ༌[^1582]གཅིག་ཡིན་ཏེ། ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ཀྱི་ཉེར་བསྡོགས་ཀྱི་འབྲས་བུ་ནི་གཅིག་ཡིན་ཏེ། གཟུགས་ཀྱི་འདོད་ཆགས་ཟད་པའི་ཡོངས་སུ་ཤེས་པའོ། །

[Block 2158]
གཟུགས་མེད་དངོས་གཞི་གསུམ་གྱི་ཡང་། །གཟུགས་མེད་པའི་དངོས་གཞི་གསུམ་གྱི་འབྲས་བུ་ཡང་གཅིག་ཁོ་ན་སྟེ། ཀུན་དུ་སྦྱོར་བ་ཐམས་ཅད་ཡོངས་སུ་གཏུགས་པའི་ཡོངས་སུ་ཤེས་པ་ཡིན་ནོ། །

[Block 2159]
ཡོངས་སུ་ཤེས་པ་དགུ་པོ་ཐམས་ཅད་འཕགས་པའི་ལམ་གྱི་འབྲས་བུ་ཡིན་ནོ། །

[Block 2160]
[^1583]གཉིས། འཇིག་རྟེན་པ་ཡི། ལམ་གྱི་འབྲས་བུ་ནི་གཉིས་ཏེ། ཐ་མའི་ཆ་དང་མཐུན་པ་དང་། གཟུགས་ཀྱི་འདོད་ཆགས་ཟད་པའི་ཡོངས་སུ་ཤེས་པ་དག་གོ། །

[Block 2161]
རྗེས་སུ་ཡང་། རྗེས་སུ་ཤེས་པའི་འབྲས་བུ་ཡང་ཡོངས་སུ་ཤེས་པ་གཉིས་ཏེ་ཐ་མ་དག་གོ། །

[Block 2162]
ཆོས་ཤེས་པ་ནི༌[^1584]གསུམ་ཡིན་ནོ། །

[Block 2163]
ཐ་མ་དག་ཁོ་ན་སྟེ། ཁམས་གསུམ་པའི་བསྒོམ་པས་སྤང་བར་བྱ་བའི་གཉེན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2164]
དེའི་ཕྱོགས་མཐུན་གྱི་དྲུག་དང་ལྔ། །ཆོས་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པའི་འབྲས་བུ་ནི་ཡོངས་སུ་ཤེས་པ་དྲུག་སྟེ། ཆོས་ཀྱི་བཟོད་པ་དང་ཤེས་པ་རྣམས་ཀྱི་འབྲས་བུ་གང་དག་ཡིན་པ་ཁོ་ནའོ། །

[Block 2165]
རྗེས་སུ་ཤེས་པའི་ཕྱོགས་དང་མཐུན་པ༌[^1585]ནི་ལྔ་ཡིན་ཏེ།[^1586] རྗེས་ཀྱི་བཟོད་པ་དང་ཤེས་པ་རྣམས་ཀྱི་འབྲས་བུ་གང་དག་ཡིན་པ་ཁོ་ནའོ། །

[Block 2166]
ཕྱོགས་དང་མཐུན་པ་སྨོས་པས་ནི་བཟོད་པ་དང་ཤེས་པ་རྣམས་བཟུང༌[^1587]ངོ་། །ཅིའི་ཕྱིར་སྤངས་པ་རེ་རེ་ཡོངས་སུ་ཤེས་པར་རྣམ་པར་མི་གཞག་ཅེ་ན། འདི་ལྟར་རེ་ཞིག་བཟོད་པའི་འབྲས་བུ་བྲལ་བ་ནི།

[Block 2167 [HEADING]]
##### ཡོངས་ཤེས་སུ་རྣམ་པར་གཞག་པ། ^2-38-2-3-0

[Block 2168 [VERSE]]
བྲལ་བའི་ཐོབ་པ་ཟག་མེད་དང་། །
སྲིད་རྩེ་ཉམས་པར་བྱས་པ་དང་། །
རྒྱུ་གཉིས་ཀུན་དུ་བཅོམ་པའི་ཕྱིར། །
ཡོངས་ཤེས་སུ་རྣམ་པར་གཞག་གོ། །

[Block 2169]
གང་ལ་རྒྱུ་འདི་གསུམ་ཡོད་པ་དེ་སྤངས་པའི་ཡོངས་སུ་ཤེས་པ་ཞེས་བྱ་ཞེ༌[^1588]ན། རེ་ཞིག་སོ་སོའི་སྐྱེ་བོ་ལ་ནི་བྲལ་བའི་ཐོབ་པ་ཟག་པ་མེད་པ་དང་། སྲིད་པའི་རྩེ་མོ་ཉམས་པར་བྱེད་པ་མེད་པས་འདིའི་སྤངས་པ་ཡོངས་སུ་ཤེས་པ་ཞེས་བྱ་བའི་མིང་མི་ཐོབ༌[^1589]པོ། །འཕགས་པ་ལ་ཡང་བཟོད་པའི་འབྲས་བུ་སྤངས་པ་གང་ཡིན་པ་དེ་ནི། དེ་ལ་ཇི་སྲིད་དུ་སྡུག་བསྔལ་ལ་རྗེས་སུ་ཤེས་པའི་བཟོད་པ་ལ་གནས་པ། དེ་སྲིད་དུ་བྲལ་བའི་ཐོབ་པ་ཟག་པ་མེད་པ་ཡོད་མོད་ཀྱི། སྲིད་པའི་རྩེ་མོ་མཉམ༌[^1590]པར་བྱས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2170]
སྡུག་བསྔལ་ལ་རྗེས་སུ་ཤེས་པ་ལ་ནི་གཉིས༌[^1591]ཡོད་མོད་ཀྱི། རྒྱུ་གཉིས་ཀུན་དུ་བཅོམ་པ་ནི་མ་ཡིན་ཏེ། རྒྱུ་ཀུན་འབྱུང་མཐོང་བས་སྤང་བར་བྱ་བ་ཀུན་དུ་འགྲོ་བ་མ་སྤངས་པའི་ཕྱིར་རོ། །

[Block 2171]
ཆོས་དང་རྗེས་སུ་ཤེས་པ་གཞན་དག་ལ་ནི་གསུམ་པོ་ཐམས་ཅད་ཡོད་པས། དེའི་ཕྱིར་གནས་སྐབས་དེ་དང་དེ་དག་ཏུ་དེ༌[^1592]སྤངས་པའི་ཡོངས་སུ་ཤེས་པའི་མིང་འཐོབ་པོ། །ཤེས་པའི་འབྲས་བུ་སྤངས་པ་ནི་རྒྱུ་གསུམ་པོ་དེ་དང་།

[Block 2172 [VERSE]]
བཞི་པ་ཁམས་ལས་འདས་པ་ལས། །
ཡོངས་སུ་ཤེས་པའི་མིང་འཐོབ་སྟེ། །

[Block 2173]
ཁམས་མཐའ་དག་ལས་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར། གང་གི་ཚེ་ཁམས་ལས་ཡང་དག་པར་འདའ་བ་ནའོ། །

[Block 2174]
གཉིས་པ༌[^1593]ཀུན་དུ་སྦྱོར་བ་དང་བྲལ་བ་རྒྱུ་ལྔ་པ་དེ༌[^1594]སྨྲས་པ། རྣམ་པ་གང་ཞིག་སྤངས་ལ་གལ་ཏེ་དེ་ལ་དམིགས་པའི་ཉོན་མོངས་པ་གཞན་དང་བྲལ་བར་གྱུར་ནའོ་ཞེས་བྱ་བ་ནི། དེ་ནི༌[^1595]རྒྱུ་གཉི་ག་ཡང་དག་པར་བཅོམ་པ་དང་། ཁམས་ལས་ཡང་དག་པར་འདས་པ་ལས་གཞན་མ་ཡིན་པར༌[^1596]མི་བརྗོད་དོ། །

[Block 2175 [HEADING]]
##### ཡོངས་སུ་ཤེས་པ་དུ་ཞིག་དང་ལྡན་པ། ^2-38-2-4-0
--- END BLOCKS ---
