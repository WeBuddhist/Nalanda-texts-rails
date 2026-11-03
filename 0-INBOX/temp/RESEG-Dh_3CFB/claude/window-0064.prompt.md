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
[Block 2241 [VERSE]]
སྐྱེས་བུས་མ་བྱས་ཤེས་བྱ་ཉིད། །
ཇི་བཞིན་དོན་ཤེས་སྒྲུབ་བྱེད་མིན། །
སྐྱེས་བུའི་ཉེས་པས་སྐྱོན་མེད་པའི། །
མེ་སོགས་རྣམ་པ་གཞན་དུའང་མཐོང་། །

[Block 2242]
རིག་བྱེད་པའི་སྒྲ་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་པ་ཡང་བླ་སྟེ། དེ་ལྟར་ན་ཡང་དེ་དག་དོན་ཇི་ལྟ་བ་བཞིན་མ་ཡིན་པའི་ཤེས་པའི་རྒྱུ་ཉིད་ཡིན་པར་བསམ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 2243]
སྐྱེས་བུའི་སྐྱོན་གྱིས་ཉེ་བར་བསྒྱུར་བ་ཉིད་དོན་དག་ལས་ཤེས་པ་འཁྲུལ་པ་མ་ཡིན་ཏེ། དེ་དང་བྲལ་བའི་སྒྲོན་མ་ལ་སོགས་པ་དག་གིས་ཀྱང་ཨུཏྤལ་ལ་སོགས་པ་དག་ལ་ལོག་པའི་རྣམ་པར་ཤེས་པ་བསྐྱེད་པའི་ཕྱིར་རོ། །

[Block 2244]
དེ་བས་ན་འདུས་བྱས་པ་ལ་ལྟོས་པ་མེད་པའི་སྒྲ་འདི་དག་ནི་ངོ་བོ་ཉིད་ཀྱིས་དོན་རྣམས་ལ་སློབ་པའི༌[^1586]རྒྱུར་འགྱུར་ཏེ། རང་བཞིན་གྱི་ཁྱད་པར་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2245]
ལོག་པར་བསལ་བ་ཅན་དག་ཀྱང་ངེས་པར་འགྱུར་ཏེ། མེ་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 2246]
གལ་ཏེ་ངེས་པའི་རྒྱུ་མེད་པའི་ཕྱིར་མི་རིགས་སོ་ཞེ་ན། ཕྱིན་ཅི་མ་ལོག་པ་བསལ་བ་ཅན་གྱི་ངེས་པ་ལ་རྒྱུ་ཅི་ཞིག་ཡོད། དེ་བས་ན་ངོ་བོ་ཉིད་ཀྱིས་དོན་ཇི་ལྟ་བ་བཞིན་དུ་བསལ་བའི་ངེས་པ་བཞིན་དུ་དོན་ཇི་ལྟ་བ་བཞིན་དུ་མ་ཡིན་པའི་བསལ་བའི་ངེས་པ་ཅིའི་ཕྱིར་མི་རྟོགས། ཡང་ན་མེ་ལ་སོགས་པ་དང་འདྲ་བར་དོན་དག་གཉི་གའི་ཤེས་པའི་རྒྱུ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2247]
མེ་ལ་སོགས་པ་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་དུ་ཟིན་ཀྱང་གཅིག༌[^1587]དོན་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པའི་རྒྱུ་ཡིན་ན་ཡང་ཐམས་ཅད་ལ་དེ་ལྟར་འགྱུར་བ་མ་ཡིན་ནོ།[^1588] །དེ་ལྟར་ན་སྒྲ་རྣམས་ཀྱང་སྐྱེས་བུས་མ་བྱས་པ་ཉིད་ཡིན་ན་ཡང་གཉི་གར་འགྱུར་རོ། །

[Block 2248]
མེ་ལ་སོགས་པ་དག་ནི་བྱས་པ་ཉིད་ཀྱི་ཕྱིར། རྐྱེན་ཇི་ལྟ་བ་བཞིན་དུ་གཞན་ལ་རྣམ་པ་གཞན་ཉིད་ཡིན་པ་བླ་སྟེ། སྒྲ་རྟག་པ་དག་ལ་ཡང་དེ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2249]
དེ་ལྟ་བུའི་རྣམ་པའི་ཆོས་དེ་ལ་ཡང་ཡོད་པ་མ་ཡིན་ནམ། དེ་དག་ཀྱང་བརྡའི་སྟོབས་ལས་རྣམ་པ་གཞན་དུ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 2250]
འབྲས་བུ་བསྐྱེད་པའི་རང་བཞིན་དུ་གནས་པ་ཡིན་ཡང་དེ་དག་བརྡ་ལ་སོགས་པ་ཡང་ལྟོས་པར་བྱ་བ་མེད་པའི་ཕྱིར། དེ་ལས་ཐམས་ཅད་ཀྱིས་ཐམས་ཅད་ཀྱི་ཚེ་དོན་རྣམས་རྟོགས་པར་འགྱུར་ན་ཡོད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 2251]
དེ་བས་ན་སྒྲ་རྣམས་ནི་གནས་པའི་རང་བཞིན་མ་ཡིན་ནོ། །

[Block 2252]
གཞན་ཡང་དེ་ན༌[^1589]མ་བྱས་པར་འདོད་ན།

[Block 2253 [VERSE]]
ཤེས་པ་ཉིད་ཀྱི་རྒྱུར་མི་འགྱུར། །
རྟག་པ་དག་ལས་དངོས་ནུས་པས། །
འགའ༌[^1590]ཡང་སྐྱེ་བ་ཡོད་མ་ཡིན། །

[Block 2254]
གལ་ཏེ་སྒྲ་མ་བྱས་པ་ཡིན་ན་དེ་ལས་དོན་ཤེས་པ་ཉིད་དུ་མི་འགྱུར་རོ། །ཤེས་པ་སྐྱེ་བ་དང་ཅིག་ཤོས་ཀྱི་དུས་དག་ཏུ་ངོ་བོར་མཚུངས་པའི་ཤེས་པ་བསྐྱེད་པ་ལ་ནུས་པ་ཡོད་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 2255]
དེ་ལྟར་ན་འདི་སྐྱེད་པར་བྱེད་པ་ཡིན་ལ་དེ་ལྟར་ན་ནི་མ་ཡིན་ནོ་ཞེས་ངོ་བོའི་ཁྱད་པར་རྣམ་པར་ཕྱེ་བར་བྱ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2256]
འདིའི་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་པ་ཅི་འདྲ་བ་དེ་འདྲ་བ༌[^1591]ཉིད་ནི་སྐྱེད་པར་བྱེད་པར་རིགས་པ་མ་ཡིན་ཞིང་གཞན་ལ་ལྟོས་པ་ཡང་བཀག་པ་ཉིད་ཡིན་ནོ། །

[Block 2257]
དེ་བས་ན་རྟག་པ་དག༌[^1592]ནི་འགའ་ཞིག་ཏུ་ཡང་ཤེས་པ་བསྐྱེད་པར་ནུས་པ་མ་ཡིན་ཏེ། འགའ་ཞིག་གི་ཚེ་མི་སྐྱེད་ན་རྟག་ཏུ་མི་བསྐྱེད་པར་ཐལ་བའི་ཕྱིར་དང་། འབྲས་བུ་རྟག༌[^1593]ཏུ་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2258]
དེ་དག་རྣམ་པ་འགའ་ཞིག་གིས་ཀྱང་བྱེད་པ་པོ་མ་ཡིན་ནོ་ཞེས་མང་དུ་བཤད་ཟིན་ཏོ། །

[Block 2259]
དེ་དག་གི་ནམ་མཁའ་ལ་སོགས་པ་རྟག་པ་དག་ཏུ་འདོད་པ་དག་གི་རྟོག་པ་གང་ཡིན་པ་དེ་ཡང་དེའི་རང་བཞིན་ཅན་དུ་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 2260]
དེ་ལྟར་ན།

[Block 2261 [VERSE]]
ཀུན་རྟོག་བག་ཆགས་ལས་བྱུང་བའི། །
སྒྲོ་བཏགས་སྤྱོད་ཡུལ་ཅན་བློ་དག །
འགའ་ཞིག་དེ་ལས་སྐྱེ་འགྱུར་གྱི། །
དོན་དེ་སྤྱོད་ཡུལ་ཅན་མ་ཡིན། །

[Block 2262]
རང་གི་མཚན་ཉིད་ཀྱི་ཡུལ་ཅན་གྱི་བློ་ནི་ངེས་པར་དེའི་རུང་བ་ཉིད་དུ་ཉེ་བའི༌[^1594]རྗེས་སུ་བྱེད་པའི་ངང་ཚུལ་ཅན་ཡིན་པས་ན། འདིའི་རྒྱུ་རུང་བ་དེ་ལ་ཡོད་ན་དེ་འགྱུར་བ་ཉིད་ཡིན་ནོ། །

[Block 2263]
དེ་ལྟར་ན་དེ་གལ་ཏེ་དངོས་པོ་རྟག་པ་རྣམས་ཀྱི་རང་གི་མཚན་ཉིད་ལ་འགའ་ཞིག་གི་ཤེས་པ་འགྱུར་ན་ཐམས་ཅད་ཐམས་ཅད་ཀྱི་ཚེ་འགྱུར་རོ། །

[Block 2264]
འབྲས་བུ་ཁྱད་པར་དུ་བྱས་པའི་བསལ་བ་ཅན་དག་ནི་རྣམ་པ་འགའ་ཞིག་གིས་འགའ་ཞིག་ལ་ཉེ་བར་སྦྱར་བ་ན། དེ་བསྐྱེད་པར་རུང་བའི་ཕུལ་དུ་བྱུང་བ་ཐོབ་པའི་རྒྱུའི་དངོས་པོའི་ཁྱད་པར་དུ༌[^1595]ལྟོས་པ་ཞེས་བྱ་བ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2265]
དེ་ལྟར་ན་འབྲས་བུའི་ཁྱད་པར་ཅན་མ་ཡིན་པ་རྟག་པའི་དངོས་པོ་དེའི་རྒྱུ་ལས་ལྟོས་པ་ཅན་འགའ་ཞིག་གིས་གཟུང་བར་འགྱུར་ན། གལ་ཏེ་འདིའི་འཛིན་པ་བསྐྱེད་པར་འགྱུར་ན་དེ་ཉིད་ཀྱིས་གཟུང་བ་གང་ཡིན་པ་དེ་རིགས་པ་ཡིན་ནོ། །

[Block 2266]
དེ་ཡང་སྲིད་པ་མ་ཡིན་ཏེ། བརྟན་པའི་རང་བཞིན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2267]
དེ་ལྟར་ན་ཐམས་ཅད་ཀྱིས་ཅིག་ཅར་གཟུང་བར་འགྱུར་བའམ། འགའ་ཞིག་གིས་ཀྱང་མ་ཡིན་པའི་ཕྱིར། འགའ་ཞིག་ཡོད་པ་མཐོང་ན། རྟག་པ་འགའ་ཞིག་ཀྱང་དབང་པོ་ལས་འདས་པར་འགྱུར་བ་མ་ཡིན་ན། དེ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2268]
དེ་བས་ན་ནམ་མཁའ་ལ་སོགས་པ་ལ་ཐམས་ཅད་ཀྱི་འཁྲུལ་པ་ཉིད་དོན་གྱི༌[^1596]ནུས་པ་ལ་ལྟོས་པ་མེད་པ་སྒྲོ་བཏགས་པའི་སྤྱོད་ཡུལ་ཅན་ནང་གི་ཉེ་བར་ལེན་པ་རྣམ་པར་རྟོག་པའི་བག་ཆགས་སད་པ་ལ་བརྟེན་ནས་ཕྱི་རོལ་གྱི་དོན་གྱིས་སྟོང་པ་དག༌[^1597]སྐྱེ་བར་འགྱུར་རོ། །

[Block 2269]
དེ་བས་ན་སྒྲ་ནི་གཞན་དུ་འགྱུར་བ་མ་ཡིན་པའི་ཆོས་ཅན་མ་ཡིན་ནོ། །

[Block 2270]
དེ་ཉིད་ཡིན་ན་ཡང་དོན་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་པ་ཅན་ཉིད་ཅེས་བྱ་བ་དེ་གང་ལས་ཡིན། མེ་ནི་ཁ་བའི་གཉེན་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་མེ་ནི་གྲང་བ་འཇོམས་པར་ནུས་པ་འཇིག་རྟེན་ལ་གྲགས་པ་བསྟན་པས་ཐམས་ཅད་དེ་ལྟར་འགྱུར་བ་མ་ཡིན་ནོ། །

[Block 2271]
འཇིག་རྟེན་ནི་རང་གི་འདོད་པས་བྱས་པའི་བརྡའི་རྗེས་སུ་ཐ་སྙད་འདོགས་པའི་ཕྱིར། འཇིག་རྟེན་འདིར་རང་གི་བརྡའི་རྗེས་སུ་བྱེད་པས་ཅི་དེ་ལྟར་རྟོགས་སམ། འོན་ཏེ་རང་བཞིན་གནས་པ་ལས་ཡིན་ཞེས་ཐེ་ཚོམ་ཟ་བ་ཉིད་ཡིན་ནོ། །

[Block 2272]
འཇིག་རྟེན་གྱི་འདོད་པས་སྒྲ་དག་གཞན་དུ་གྱུར་པ་ཡིན་ན་ཡང་གཞན་ལ་ཡང་རྣམ་པ་གཞན་དུ་སྣང་བའི་ཕྱིར། འཇིག་རྟེན་གྱི་གྲགས་པའི་རྗེས་སུ་བྱེད་པ་ལ་ཡང་དེ་དག་རྣམ་པ་གཞན་དུ་འགྱུར་བ་ཉིད་སྲིད་དོ། །

[Block 2273]
དེ་བས་ན་འགའ་ཞིག་ཕྱིན་ཅི་མ་ལོག་པར་མཐོང་དུ་ཟིན་ཀྱང་ཐམས་ཅད་དེ་དག་དེ་ལྟ་བུའི་ངོ་བོར་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 2274]
དེ་དག་མ་བྱས་པའི་རང་བཞིན་ཅན་ཡིན་ན་ཡང་འགའ་ཞིག་ལོག་པ་ཉིད་དུ་ངེས་པས་ཀྱང་འགྱུར་བའི་ཕྱིར། རང་བཞིན་ཡོངས་སུ་ཤེས་པ་མེད་པ་ལས་ཐམས་ཅད་ལ་ཐེ་ཚོམ་དུ་འགྱུར་རོ། །

[Block 2275 [VERSE]]
གལ་ཏེ་བྱས་པ་ལོག་པ་ཉིད། །
མཐོང་བ་ཉིད་ཀྱི་ཕྱིར་ན་ཚིག །
མ་བྱས་བདེན་དོན་ཅན་ཡིན་ཏེ། །
ལྡོག་པས་འགལ་བ་ཁྱབ་ཕྱིར་རོ། །

[Block 2276]
ཅི་སྟེ་ལོག་པའི་དོན་ཅན་གྱི་ཚིག་གང་ཡིན་པ་དེ་མ་ལུས་པའི་བྱས་པ་ཡིན་པའི་ཕྱིར། གཏན་ཚིགས་ལྡོག་པས་བསྒྲུབ་པར་བྱ་བ་ལོག་པ་ལ་ཁྱབ་པའི་ཕྱིར་གཞན་ལ་མི་སྲིད་པས་ན། མ་བྱས་པ་ནི་བདེན་པའི་དོན་ཅན་ཡིན་ནོ་ཞེས་བྱ་བར་རྗེས་སུ་འགྲོ་བ་མེད་པར་འགྱུར་རོ། །

[Block 2277]
གང་ལ་གང་གིས་མ་ཁྱབ་ན། དེ་ལ་ལྡོག་པར་དོགས་པར་བྱ་བ༌[^1598]ན། འགལ་བ་དག་ནི་གཅིག་ལ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2278]
མེད་ན་ཡང་རིགས་མི་མཐུན་པ་ལ་རྣམ་པ་གཞན་མེད་པས་འདོད་པའི་དོན་གྲུབ་པའི་ཕྱིར་དང་། དེ་སྒྲུབ་པའི་བྱེད་པ་ཉིད་ཡིན་པའི་ཕྱིར། རྟགས་ཀྱི་རྗེས་སུ་འགྲོ་བ་བསྟན་པ་དོན་མེད་པ་ཡིན་ཏེ། ལྡོག་པ་ཙམ་ཉིད་ཀྱིས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2279]
དེ་ནི་བདེན་ཏེ་གལ་ཏེ་གཏན་ཚིགས་བསྒྲུབ་པར་བྱ་བའི་མི་མཐུན་པའི་ཕྱོགས་ལ་ཁྱབ་པར་བྱ་བ་དང་། ཁྱབ་པར་བྱེད་པའི་ངོ་བོ་གྲུབ་པར་འགྱུར་ན་དེ་ཡང་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 2280]
འདི་ལྟར།
--- END BLOCKS ---
