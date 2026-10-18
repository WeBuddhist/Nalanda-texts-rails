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
[Block 2206 [HEADING]]
### མཐོང་བ་དང་བསྒོམ་པའི་ལམ། ^3-1-0

[Block 2207]
༄༅༅། །ཇི་སྐད་དུ་སྤངས་པ་ནི་ཡོངས་སུ་ཤེས་པའི་མིང་འཐོབ་པོ་ཞེས་བཤད་པ་དེ་ཡང་།

[Block 2208 [VERSE]]
བདེན་པ་མཐོང་དང་བསྒོམ་པ༌[^1628]ལས། །
ཉོན་མོངས་སྤངས་པ་ཞེས་བཤད་པ། །

[Block 2209 [HEADING]]
#### ལམ་ཟག་པ་མེད་པ་དང་ཟག་པ་དང་བཅས་པ། ^3-1-1-0

[Block 2210]
ཉོན་མོངས་པ་རྣམས་མཐོང་བས་སྤང་བར་བྱ་བ་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་ནོ་ཞེས་རྒྱས་པར་བཤད་པ། ད་ནི་མཐོང་བ་དང་བསྒོམ་པའི་ལམ་དེ་དག་ཅི་ཟག་པ་མེད་པའམ། ཟག་པ་དང་བཅས་པ་ཞེས་བརྗོད་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་འདི་དག༌[^1629]བརྗོད་དེ།

[Block 2211 [VERSE]]
བསྒོམ་པའི་ལམ་ནི་རྣམ་གཉིས་ཏེ། །
མཐོང་བ་ཞེས་བྱ་ཟག་པ་མེད། །
བསྒོམ་པའི་ལམ་ནི་རྣམ༌[^1630]གཉིས་ཏེ། །

[Block 2212]
འཇིག་རྟེན་པ་དང་། འཇིག་རྟེན་ལས་འདས་པའོ། །

[Block 2213]
མཐོང་བའི་ལམ་ནི་ཁམས་གསུམ་པའི་གཉེན་པོ་ཡིན་པའི་ཕྱིར་དང་། མཐོང་བས་སྤང་བར་བྱ་བ་རྣམ་པ་དགུ་ཅིག་ཅར་དུ་སྤང་བའི༌[^1631]ཕྱིར་འཇིག་རྟེན་ལས་འདས་པ་ཁོ་ན་ཡིན་ཏེ། འཇིག་རྟེན་པ་ལ་ནི་དེ་འདྲ་བའི་མཐུ་མེད་དོ། །

[Block 2214 [HEADING]]
#### བདེན་པ་རྣམས། ^3-1-2-0

[Block 2215]
བདེན་པ་མཐོང་བ་ལས་ཞེས་བཤད་པ། བདེན་པ་དེ་དག་ཀྱང་གང་ཞིག་ཅེ་ན། བདེན་པ་དག་ནི་བཞིར་བཤད་དོ། །གང་དུ་བཤད་ཅེ་ན། ཆོས་ཟག་པ་དང་བཅས་པ་དང་། ཟག་པ་མེད་པ་བསྟན་པར་ཟག་མེད་ལམ་གྱི་བདེན་པ་དང་ཞེས་ལམ་གྱི་བདེན་པ་རང་གི་མིང་གིས་བསྟན་ཏོ། །

[Block 2216]
སོ་སོར་བརྟགས་པས་འགོག་པ་གང་། །བྲལ་བའོ་ཞེས་འགོག་པའི་བདེན་བ་བསྟན་ཏོ། །

[Block 2217 [HEADING]]
##### བདེན་པ་དག་གི་རིམ་པ། ^3-1-2-1-0

[Block 2218]
སྡུག་བསྔལ་ཀུན་འབྱུང་འཇིག་རྟེན་དང་། །ཞེས་བྱ་བ་དེར་སྡུག་བསྔལ་དང་ཀུན་འབྱུང་གི་བདེན་པ་དག་བསྟན་ཏོ། །ཅི་འདི་དག་གི་རིམ་པ་འདི་ཁོ་ན་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 2219]
འོ་ན་ཇི་ལྟ་བུ་ཡིན་ཞེ་ན།

[Block 2220 [VERSE]]
སྡུག་བསྔལ་ཀུན་འབྱུང་དེ་བཞིན་དུ། །
འགོག་དང་ལམ་སྟེ་དེ་ལྟར་ན། །

[Block 2221]
དེ་དག་གི་རིམ་པ་ནི་འདི་ཡིན་ནོ། །

[Block 2222]
དེ་བཞིན་ཞེས་བྱ་བའི་སྒྲ་ནི་རང་གི་ངོ་བོ་ནི་སྔར་ཇི་སྐད་བཤད་པ་དེ་ཁོ་ན་བཞིན་ནོ་ཞེས་རབ་ཏུ་བསྟན་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 2223]
དེ་ནི། དེ་དག་ཇི་ལྟར་མངོན་རྟོགས་རིམ། །བདེན་པ་གང་ཞིག་སྔར་མངོན་པར་རྟོགས་པ་དེ་སྔར་བསྟན་ཏོ། །

[Block 2224]
དེ་ལྟ་མ་ཡིན་ན་རྒྱུ་ནི་སྔར་བསྟན་ལ་འབྲས་བུ་ནི་ཕྱིས་བསྟན་པར་འགྱུར་རོ། །

[Block 2225]
ཁ་ཅིག་ནི་སྐྱེ་བ་དང་མཐུན་པ་བསྟན་ཏེ། དཔེར་ན་དྲན་པ་ཉེ་བར་གཞག་པ་དང་། བསམ་གཏན་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2226]
ཁ་ཅིག་ནི་རབ་ཏུ་བརྟག་པ་དང་མཐུན་པར་བསྟན་ཏེ། དཔེར་ན་ཡང་དག་པར་སྤོང་བ་རྣམས་ལྟ་བུ་སྟེ། གང་སྔར་ནི་སྐྱེས་པ་རྣམས་སྤང་བར་བྱ་བའི་ཕྱིར་འདུན་པ་སྐྱེད༌[^1632]ལ། ཕྱིས་ནི་མ་སྐྱེས་པ་རྣམས་མི་སྐྱེ་བར་བྱ་བའི་ཕྱིར་འདུན་པ་སྐྱེད་པའི༌[^1633]ངེས་པ་འདི་ནི་མེད་དོ། །

[Block 2227]
བདེན་པ་རྣམས་ནི་མངོན་པར་རྟོགས་པ་དང་མཐུན་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 2228]
ཅིའི་ཕྱིར་བདེན་པ་རྣམས་དེ་ལྟར་མངོན་པར་རྟོགས་ཤེ་ན། གང་ལ་ཆགས་པ་དང་། གང་གིས་གནོད་པ་བྱེད་པ་དང་། གང་ལས་ཐར་པ་དོན་དུ་གཉེར་བའི་སྡུག་བསྔལ་གྱི་བདེན་པ་དེ་ཉིད་ལ་དང་པོར་རྣམ་པར་དཔྱོད་པའི་གནས་སྐབས་ན་ཡོངས་སུ་རྟོག་ལ། ཕྱིས་འདིའི་རྒྱུ་ནི་གང་ཞིག་ཡིན་ཞེས་ཀུན་འབྱུང་གི་བདེན་པ་ལ་ཡོངས་སུ་རྟོག་གོ། །

[Block 2229]
འདིའི་འགོག་པ་ནི་གང་ཞིག་ཡིན་ཞེས་འགོག་པའི་བདེན་པ་ལ་ཡོངས་སུ་རྟོག་གོ། །

[Block 2230]
འདིའི་ལམ་ནི་གང་ཞིག་ཡིན་ཞེས་ལམ་གྱི་བདེན་པ་ལ་ཡོངས་སུ་རྟོག་སྟེ། ནད་མཐོང་བས་དེའི་གཞི་དང་ཟད་པ་དང་སྨན་ཚོལ་བ་བཞིན་ནོ། །

[Block 2231]
བདེན་པ་རྣམས་ཀྱི་དཔེ་འདི་ནི་མདོ་ལས་ཀྱང་བཤད་དོ།[^1634] །མདོ་གང་ལས་ཤེ་ན། ཡན་ལག་བཞི་དང་ལྡན་པའི་སྨན་པས༌[^1635]ཟུག་རྔུ་འབྱིན་པ་ཞེས་གསུངས་པ་དེ་ལས་བསྟན་ཏོ། །

[Block 2232]
སྔར་འཕངས་པའི་ཕྱིར་ཇི་ལྟར་རྣམ་པར་དཔྱོད་པའི་གནས་སྐབས་ན་བདེན་པ་ལ་ཡོངས་སུ་རྟོག་པ་དེ་ཁོ་ན་བཞིན་དུ་མངོན་པར་རྟོགས་པའི་གནས་སྐབས་ན་ཡང་བདེན་པ་མངོན་པར་རྟོགས་ཏེ། དཀྱུས་ས་བསྟན༌[^1636]པའི་རྟ་ཐགས༌[^1637]ཐོགས་མེད་པར་རྒྱུག་པ༌[^1638]བཞིན་ནོ། །

[Block 2233 [HEADING]]
##### མངོན་པར་རྟོགས་པ་ཞེས་བྱ་བའི་དོན། ^3-1-2-2-0

[Block 2234]
མངོན་པར་རྟོགས་པ་ཞེས་བྱ་བའི་དོན་ནི་ཅི་ཞེ་ན། མངོན་པར་ཡང་དག་པར་རྟོགས་པའོ། །

[Block 2235]
ཅིའི་ཕྱིར་ཟག་པ་མེད་པ་ཁོ་ན་ཡིན་གྱི་ཟག་པ་དང་བཅས་པ་མ་ཡིན་ཞེ་ན། དེ་ནི་མྱ་ངན་ལས་འདས་པ་ལ་མངོན་དུ་ཕྱོགས་པར་ཡང་དག་པར་རྟོག་པ༌[^1639]སྟེ། ཡང་དག་པ༌[^1640]ཞེས་བྱ་བ་ནི་དེ་ཁོ་ན་ཉིད་དུའོ། །

[Block 2236]
དེ་ལ་ཉེ་བར་ལེན་པའི་ཕུང་པོ་འབྲས་བུར་གྱུར་པ་རྣམས་ནི་སྡུག་བསྔལ་གྱི་བདེན་པ་ཡིན་ནོ། །

[Block 2237]
རྒྱུར་གྱུར་པ་རྣམས་ནི་ཀུན་འབྱུང་གི་བདེན་པ་ཡིན་ཏེ། འདི་ལས་ཀུན་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2238]
དེ་ཉིད་ཀྱི་ཕྱིར་འདི་གཉིས་ནི་རྒྱུ་དང་འབྲས་བུར་གྱུར་པས་མིང་གི་སྒོ་ནས་བྱེ་བྲག་ཡོད་ཀྱི་རྫས་སུ་ནི་མ་ཡིན་ནོ། །

[Block 2239]
འགོག་པ་དང་ལམ་ནི་རྫས་སུ་ཡང་བྱེ་བྲག་ཡོད་དོ། །

[Block 2240 [HEADING]]
##### འཕགས་པའི་བདེན་པ། ^3-1-2-3-0

[Block 2241]
མདོ་ལས་འཕགས་པའི་བདེན་པ་རྣམས་ཞེས་འབྱུང་བ་དེའི་དོན་ཅི་ཞེ་ན། འདི་དག་ནི་འཕགས་པ་རྣམས་ལ་བདེན་པས།

[Block 2242]
དེ་ལྟ་བས་ན་མདོ་ཁོ་ན་ལས།

[Block 2243]
འཕགས་པའི་བདེན་པ་རྣམས་ཞེས་བཤད་དོ། །ཅི་འདི་དག་གཞན་རྣམས་ལ་བརྫུན་ནམ་ཞེ་ན། འདི་དག་ནི་ཕྱིན་ཅི་མ་ལོག་པའི་ཕྱིར་ཐམས་ཅད་ལ་བདེན་ན་འཕགས་པ་རྣམས་ཀྱིས་ནི་འདི་དག་ཇི་ལྟ་བ་དེ་ཁོ་ན་བཞིན་དུ་གཟིགས་ཀྱི་གཞན་དག་གིས་ནི་མ་ཡིན་པས་དེའི་ཕྱིར་འདི་དག་ནི་འཕགས་པ་རྣམས་ཀྱི་བདེན་པ་ཞེས་བྱ་བའི་ཕྱིན་ཅི་ལོག་ཏུ་མཐོང་བའི་ཕྱིར་འཕགས་པ་མ་ཡིན་པ་རྣམས་ཀྱི་ནི་མ་ཡིན་ཏེ།

[Block 2244]
ཚིགས་སུ་བཅད་པ་ལས།

[Block 2245 [VERSE]]
འཕགས་པས་བདེ་བར་གང་གསུངས་པ། །
དེ་ནི་གཞན་གྱིས་སྡུག་བསྔལ་རིག །
གཞན་གྱིས་བདེ་བར་གང་སྨྲས་པ། །
དེ་ནི་འཕགས་པས་སྡུག་བསྔལ་རིག །
--- END BLOCKS ---
