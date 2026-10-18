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
[Block 2591]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་འདྲི་བ༌[^2248]སྟེ། འདུན་པ་སྐྱེད་པ་དང་། འབད་དེ་བརྩོན་འགྲུས་རྩོམ་པ་དང་། སེམས་རབ་ཏུ་འཛིན་ཞིང་ཡང་དག་པར་རབ་ཏུ་འཇོག་པ་དེ་དག་ལ་ཅིའི་ཕྱིར་ཚུལ་བཞིན་ཞེས་བྱ་ཞེ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2592]
ལན་དུ་ཚུལ་བཞིན་རབ་ཏུ་སྦྱོར་བ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སྡིག་པ་མི་དགེ་བའི་ཆོས་རྣམས་ཀྱི་གཉེན་པོ་དང་། ཞུམ་པ་དང་རྒོད་པའི་གཉེན་པོ་བསྒོམ་པ་རྣམས་ནི་དེ་དང་མི༌[^2249]མཐུན་པ་སྡིག་པ་མི་དགེ་བའི་ཆོས་རྣམས་ལ་མི་འཇུག་སྟེ། དེ་བས་ན་དེ་དག་ནི་ཚུལ་བཞིན་གྱི་ཚིག་བླ་དགས་སོ། །

[Block 2593]
དེ་ལ་སྡིག་པ་མི་དགེ་བའི་ཆོས་གང་ཞེ་ན། གང་བསླབ་པ་གསུམ་མཐར་དབྱུང་བར་བྱ་བ་དང་མི་མཐུན་པའི་ཆོས་རྣམས་སོ། །

[Block 2594]
དེ་དག་དངོས་པོ་གང་ཡིན་པ་བསྟན་པའི་ཕྱིར། ཚུལ་ཁྲིམས་ཀྱི་མི་མཐུན་པའི་ཕྱོགས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 2595]
ཚུལ་ཁྲིམས་ཉམས་པ་དང་ཞེས་བྱ་བ་ནི་གང་ཡན་ལག་དྲུག་པའི་ཚུལ་ཁྲིམས་ཉམས་པ་ཉིད་སྡིག་པ་མི་དགེ་བའི་ཆོས་སོ། །

[Block 2596]
གང་དག་གཞན་གྱི༌[^2250]ཚུལ་ཁྲིམས་ཀྱང་ཉམས༌[^2251]པར་བྱེད་པ་ཞེས་བྱ་བ་ལ། གཞན་དག་ཚུལ་ཁྲིམས་ཉམས་པར་བྱེད་པའི་རྒྱུའི༌[^2252]ཆོས་རྣམས་ཀྱང་སྡིག་པ་མི་དགེ་བའི་ཆོས་ཞེས་བྱའོ། །དེ་ཡང་གང་ཞེ་ན། རྒྱུ་བཅུ་སྟེ། དང་པོ་ནས་ལེགས་པར་མ་བླངས་པ་དང་། ལྷོད་པར་བྱེད་པ་ལོག་པར་འཛིན་པ་དང་། བག་མེད་པ་དང་། ལེ་ལོས་ཡོངས་སུ་ཟིན་པ་དང་། ལོག་པར་སྨོན་པ༌[^2253]དང་། སྤྱོད་ལམ་ཉམས་པར་གྱུར་པ་དང་། འཚོ་བ་ཉམས་པར་གྱུར་པ་དང་། མཐའ་གཉིས་སུ་ལྟུང་བ་དང་། འབྱུང་བར་མི་བྱེད་པ་དང་། ཡི༌[^2254]དམ་བླངས་པ༌[^2255]ཉམས་པའོ། །

[Block 2597]
དེ་ལ་ཇི་ལྟར་དང་པོ་ནས་ལེགས་པར་མ་བླངས་ཤེ་ན། འདི་ལྟར་རྒྱལ་པོའི་འཇིགས་པས༌[^2256]སམ། རྐུན་པོའི་འཇིགས་པས༌[^2257]སམ། འཚོ་བ་མེད་པའམ། དེ་ལ་སོགས་པའི་རྐྱེན་གཞན་གྱི༌[^2258]ཕྱིར་བླངས་པའོ། །

[Block 2598]
ཇི་ལྟར་ན་ལྷོད་པར་བྱེད་པ་ཞེ་ན།[^2259] འདི་ལ་ཁ་ཅིག་ཚུལ་ཁྲིམས་བླངས་ནས་ཀྱང་ངོ་ཚ་མེད་པ་དང་། འགྱོད་པ་ཆུང་བ་དང་། བསླབ་པའི་གནས་རྣམས་ལ་ལྷོད་པར་བྱེད་པའོ། །ཇི་ལྟར་ན་ལོག་པར་འཛིན་པ་གང་ཞེ་ན། ཁ་ཅིག་ལོག་པར་འཛིན་པ་དང་ལྡན་པ་ཡིན་ཏེ། གནས་མ་ཡིན་པ་ལ་འགྱོད་པར་གྱུར་ཅིང་འགྱོད་པ་དེས་དགེ་བའི་བར་དུ་གཅོད་པར་བྱེད་པའོ། །

[Block 2599]
ཇི་ལྟར་ན་བག་མེད་པ་དང་། ལེ་ལོས་ཡོངས་སུ་ཟིན་པ་ཡིན་ཞེ་ན། ལ་ལ་དག་དང་པོ་ནས་ཉེས་པ༌[^2260]མི་འབྱུང་བར་དམ་བཅའ་བ༌[^2261]མེད་ཅིང་ཉེས་པ་བྱུང་ནས་ཡང་སླར་ཆོས༌[^2262]བཞིན༌[^2263]གསོ་བར་མི་བྱེད་ལ། ཉལ་བ་དང་འཕྲེས་པ་དང་། གཉིད༌[^2264]ཀྱི་བདེ་བ་རྣམས་ལྷུར་ལེན་པར་བྱེད་པའོ། །ཇི་ལྟར་ན་ལོག་པར་སྨོན་པ་ཡིན་ཞེ་ན། ཚུལ་ཁྲིམས་སམ་བརྟུལ་ཞུགས་སམ། དཀའ་ཐུབ་འདིས་ལྷ་འམ། ལྷ་གང་ཡང་རུང་བ་འམ། རྙེད་པ་དང་བཀུར་སྟི་དང་ལྡན་པར༌[^2265]གྱུར་ཅིག་ཅེས་སྨོས༌[^2266]པའོ། །

[Block 2600]
ཇི་ལྟར་ན་སྤྱོད་ལམ༌[^2267]ཉམས་པར་གྱུར་པ་ཡིན་ཞེ་ན། དེ་ལ་ཁ་ཅིག་སྤྱོད་ལམ་དང་། འཕྲལ་གྱི༌[^2268]བྱ་བ་དང་། དགེ་བ་ལ་སྦྱོར་བ་རྣམས་འཇིག་རྟེན་དང་མི་མཐུན་ཞིང་འཇིག་རྟེན་དང་འགལ་བ་དང་། འདུལ་བ་དང་མི་མཐུན་ཞིང་འདུལ་བ་དང་འགལ་བར་བྱེད་པའོ། །ཇི་ལྟར་འཚོ་བ་ཉམས་པར་འགྱུར་བ༌[^2269]ཡིན་ཞེ་ན། འདི་ལ་ཁ་ཅིག་ཆོག་མི་ཤེས་པ། འདོད་པ་མང་བ༌[^2270]དང་། གསོ་དཀའ་བ་དགང་དཀའ་བ་སྟེ། ཆོས་མ་ཡིན་པ་ལྷུང་བཟེད་དང་ཆོས་གོས་ལ་སོགས་པ་ཚོལ་བར་བྱེད་པའོ། །ཇི་ལྟར་ན་མཐའ་གཉིས་སུ་ལྷུང་བ་ཞེ་ན། འདི་ལ་ཁ་ཅིག་འདོད་པའི༌[^2271]བསོད་ཉམས༌[^2272]ལ་ལྷག་པར་ཞེན་ནས། འདོད་པའི་ཆོས་རྣམས་ལ་བག་མེད་པར་སྤྱོད་པ་དང་། ལ་ལ་དག་ཚེར་མ་ལ་གནས་འཆའ་བ་དང་། ཐལ་བའི་ནང་ན་གནས་པ་ལ་སོགས་པ་དཀའ་ཐུབ་མི་བཟད༌[^2273]པར་འཛིན་པར་བྱེད་པའོ། །ཇི་ལྟར་ན་འབྱུང་བར་མི་བྱེད་པ་ཞེ་ན། ལ་ལ་དག་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་སམ་ལྟ་བ་མཆོག་ཏུ་འཛིན་པ་སྟེ། ཚུལ་ཁྲིམས་འདི་ཉིད་དམ། བརྟུལ་ཞུགས་འདི་ཉིད་ཀྱིས་ཐར་པ་དང་། གྲོལ་བར་འགྱུར་ཞེས་ལྟ་བའོ། །

[Block 2601]
ཇི་ལྟར་ན་ཡི་དམ་བླངས་པ་ཉམས་པ་ཞེ་ན་ལ་ལ་དག་ཐམས་ཅད་ནས་ཐམས་ཅད་དུ་ངོ་ཚ་མེད་ཅིང་སྡིག་པ་མི་དགེ་བའི་ཆོས་བྱེད་པ་ལ་མི་འཛེམ༌[^2274]པ། ཚུལ་ཁྲིམས་ཉམས་པ་ཚིག་པའི་ཆོས་ཅན་ཁོང་དུ་རུལ་བ། ལུང་བོང་ལྟར་ཀུན་དུ་སྤྱོད་པ། དགེ་སྦྱོང་མ་ཡིན་པར་དགེ་སྦྱོང་དུ་ཁས་འཆེ་བ་དག་གོ། །

[Block 2602]
ཆོ་ག་ཉམས་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་ཉམས་པའོ། །

[Block 2603]
གང་དག་གཞན་གྱི་སེམས་ཀྱང་རྣམ་པར་གཡེང་བར༌[^2275]བྱེད་པའི་ཆོས་ཅི་ཡང་རུང་སྟེ་ཞེས་བྱ་བ་ནི་གཞན་དག་ཏིང་ངེ་འཛིན་ལས་ཉམས་པར་བྱེད་ཅིང་། སེམས་གཡེང་བར་འགྱུར་བའི༌[^2276]ཆོས་གང་ཡང་རུང་བ་རྣམས་ཀྱང་སྡིག་པ་མི་དགེ་བའི་ཆོས་ཞེས་བྱའོ། །

[Block 2604]
དེ་ཡང་ཆོས་གོས་དང་ལྷུང་བཟེད་ལ་སོགས་པའི་ཡོ་བྱད་ལ་ཆགས་པ་མང་བ་དང་། ལུས་ལ་ནད་མང་བ་དང་། ཁ་ཟས་ལ་མང་དུ་བརྐམ་པ༌[^2277]དང་། འདུ་འཛི་མང་པོའི་ནང་ན་གནས་པར་དགའ་བ་དང༌[^2278]འཇིག་རྟེན་གྱི་ཁམས་ཀྱི་བྱ་བ་མང་པོ་ལ་དགའ་བ་དང་། སྨྲ་བ་མང་པོ་ལ་མོས་པ་དང་། ཉལ་བ་དང་འཕྲེས་པ་ལ་སོགས་པ་ལ་དགའ་བའོ། །

[Block 2605]
གང་འདི་ལྟར་ཉམས་པ་ཞེས་བྱ་བ་ནི་རྟག་པ་འམ་ཆད་པར་ལྟ་བར་གྱུར་པའོ། །

[Block 2606]
གང་དག་གཞན་གྱི་ལྟ་བ་ཡང་ཉམས་པར་བྱེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་གཞན་དག༌[^2279]ལོག་པའི་ལྟ་བ་ལ་ཞེན་པར་འགྱུར་བའི༌[^2280]རྒྱུ་ཉོན་མོངས་པ་མངོན་དུ་འབྱུང་བ་དང་། སྒྲིབ་པ་དང་ཚོར་བར་འགྱུར་བའི་ཆོས་གོང་དུ་བཤད་པ་རྣམས་ཀྱང་སྡིག་པ་མི་དགེ་བའི་ཆོས་ཞེས་བྱའོ། །

[Block 2607 [HEADING]]
#### བརྩོན་འགྲུས་རབ་ཏུ་སྦྱངས་པ། ^8-2-2-0

[Block 2608]
བརྩོན་འགྲུས་རབ་ཏུ་སྦྱངས་པའི་བྱང་ཆུབ་སེམས་དཔའ་གང་ཞེ་ན། གང་ཡང་དག་པའི་སྤོང་བ་གཉིས་པ་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། མི་དགེ་བའི་ཆོས་སྐྱེས་པ་རྣམས་ཤིན་ཏུ་སྦྱངས་པ་སྒོམ༌[^2281]པར་བྱེད་པའོ། །

[Block 2609]
དེའི་དབང་དུ་བྱས་ནས་གང་ཡང་སྡིག་པ་མི་དགེ་བའི་ཆོས་སྐྱེས་པ་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སྡིག་པ་མི་དགེ་བའི་ཆོས་ནི་གོང་དུ་བཤད་པ་རྣམས་སོ། །

[Block 2610]
སྐྱེས་པ་ནི་མངོན་སུམ་དུ་གྱུར་པའོ། །

[Block 2611]
གོང་དུ་བཤད་པ་དང་མཐུན་པ་རྣམས་ནི་འདིར་མ་བཤད་དེ། སྔར་བཤད་པ་བཞིན་དུ་བལྟ་བར༌[^2282]བྱའོ། །

[Block 2612]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ་ནི་སྡིག་པ་མི་དགེ་བའི་ཆོས་སྐྱེས་པ་རྣམས་སྤང་བའི་ཕྱིར། འདུན་པ་བསྐྱེད་པ༌[^2283]ལ་སོགས་པ་ལ། ཅིའི་ཕྱིར་ཚུལ་བཞིན་ཡིད་ལ་བྱེད་པ་ཞེས་བྱ་ཞེ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2613]
མི་དགེ་བའི་ཆོས་དེ་དག་སེམས་ལ་ཕུང་པོར་གྱུར་པ་མེད་ཅེས་བྱ་བ་ནི་སྡིག་པ་མི་དགེ་བའི་ཆོས་སྐྱེས་པ་དེ་དག་སྐྱེས་མ་ཐག་ཏུ་འགགས་ཏེ་མེད་པར་གྱུར་བས་སེམས་ལ༌[^2284]བཅེར་ཞིང་ཕུང་པོར་གྱུར་པ་མེད་དེ། [^2285]དེ་བས་ན་ཕྱི་ནང་གི་ཡུལ་དང་ཕྱོགས་ན་མི་གནས་ཤིང་མིང་དང་མཚན་མར་གདགས་པར་མི་ནུས་ཞེས་བྱའོ། །

[Block 2614]
གལ་ཏེ་སྡིག་པ་མི་དགེ་བའི་ཆོས་སྐྱེས་པ་དེ་དག་མེད་པ་ཡིན་ན། དེ་དག་མེད་པས་སྤང་བའི་རྩོལ་བ༌[^2286]མི་དགོས་ལ། སྤང་བ་ཞེས་འབྱུང་བ་ཡང་ཇི་ལྟ་བུ་སྙམ་པ་ལ། སྡིག་པ་མི་དགེ་བའི་ཆོས་དེ་དག་སེམས་ལས༌[^2287]ཀུན་དུ་འབྱུང་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། སེམས་ལས༌[^2288]ཀུན་དུ་འབྱུང་བ་ནི་ཆོས་དེ་དག་སེམས་ལས༌[^2289]སྐྱེས་པའོ། །

[Block 2615]
ཇི་ལྟར་སྤང་བར༌[^2290]ཤེས་པ་ནི་སྤང་བར་ཤེས་པའོ། །

[Block 2616]
ཇི་ལྟར་སྤང་བ༌[^2291]ཤེས་པ་བསྟན་པའི་ཕྱིར་རྒྱུ་དང་དམིགས་པ་གང་གིས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། རྒྱུ་ནི་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་འམ། ཉོན་མོངས་པའི་བག་ཆགས་སོ། །

[Block 2617]
དམིགས་པ་ནི་ཉོན་མོངས་པ་སྐྱེ་བར་འགྱུར་བའི་ཡུལ་རྣམས་སོ། །

[Block 2618]
གང་གིས་སྡུག་པའི་རྣམ་པར་འདོད་ཆགས་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པའི་རྒྱུ་དང་དམིགས་པ་གང་གིས་རྒྱུ་དང་དམིགས་པ་བྱས་ནས་སྡུག་པར་འཛིན་པའི་རྣམ་པའི་འདོད་ཆགས་སྐྱེ་བ་འམ་ཞེས་བྱ་བ་ལ་སོགས་པར་སྦྱར་རོ། །

[Block 2619]
དེ་དག་ལ་ཞེས་བྱ་བ་ནི་ཉོན་མོངས་པ་སྐྱེ་བར་འགྱུར་བའི་ཡུལ་དང་དམིགས་པ་ལའོ། །

[Block 2620]
འདི་དག་ཅེས་བྱ་བ་ནི་འདོད་ཆགས་ལ་སོགས་པའི་ཉོན་མོངས་པ་དག་ཡིན་ནོ། །

[Block 2621]
ཐ་སྙད་བཏགས་པའི་གཟུང༌[^2292]གིས་ཞེས་བྱ་བ་ནི་མི༌[^2293]སྡུག་པས་འདོད་ཆགས་ཞི་བར་བྱེད་ཅེས་བྱ་བ་ལ་སོགས་པ་ནི་ཐ་སྙད་དུ་བཏགས་པ་ཙམ་དུ་ཟད་ཀྱི༌[^2294]དོན་དམ་པར་ན་དེ་ལ་སྤང་བར༌[^2295]བྱ་བ་དང་། སྤོང་བར་བྱེད་པ་གཉི་ག་མེད་དོ༌[^2296]ཆོས་ཐམས་ཅད་སྟོང་པ་ཉིད་དུ་མཉམ་པར་གནས་ཤིང་། འཕགས་པའི་ཡེ་ཤེས་ཀྱིས་མངོན་སུམ་དུ་གྱུར་པས་ན་སྤང་བར་བྱ་བ་མེད་དོ། །

[Block 2622]
དེ་ཅིའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཐ་སྙད་ལ་སྙེགས་ཏེ། གཉེན་པོས་མི་མཐུན་པའི་ཕྱོགས་སྤོང་བའི་ཕྱིར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2623 [HEADING]]
#### བརྩོན་འགྲུས་ཐོབ་པ། ^8-2-3-0

[Block 2624]
བརྩོན་འགྲུས་ཐོབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་ཡང་དག་པར་སྤོང་བ་གསུམ་པ་ལ་རབ་ཏུ་ཞུགས་པ་སྟེ། [^2297]དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་ཐོབ་པའི་བསྒོམ་པར་བྱ་བ་ལ་སྒོམ་པར་བྱེད་པའོ། །

[Block 2625]
དེའི་དབང་དུ་བྱས་ནས་གང་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་བསྐྱེད་པའི་ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། དགེ་བའི་ཆོས་ནི་ཚུལ་ཁྲིམས་ལ་སོགས་པ་བསླབ་པ་གསུམ་པོ༌[^2298]མ་སྐྱེས་པ་ནི་མངོན་དུ་མ་གྱུར་པའོ། །

[Block 2626]
བསྐྱེད་པའི༌[^2299]ཕྱིར་བྱ་བ་ནི་མངོན་དུ་བྱ་བའི་ཕྱིར་རོ། །

[Block 2627]
དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་བྱ་བ༌[^2300]ནི་དགེ་བའི་ཆོས་མ་སྐྱེས་པ་རྣམས་བསྐྱེད་པའི༌[^2301]ཕྱིར་འདུན་པ་བསྐྱེད་པ་ལ་སོགས་པ་ལ་ཅིའི་ཕྱིར། ཚད་མེད་པའི་ཚིག་ཤིན་ཏུ་བསྟན་པ་ཞེས་བྱ༌[^2302]ཞེ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2628]
དགེ་བའི་ཆོས་ནི་སྦྱིན་པ་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་སོ། །

[Block 2629]
འདུན་པ་ནི་དགེ་བའི་ཆོས་ཐམས་ཅད་ཀྱི༌[^2303]རྩ་བའོ༌[^2304]ཞེས་བྱ་བ་ལ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སྒྲུབ་པའི་དགེ་བའི་ཆོས་ནི་ཚད་མེད་དེ། དེ་སྒྲུབ་པར་འདུན་པ་ཡང་ཚད་མེད་པས་དེ་བས་ན། དེ་ནི་ཚད་མེད་པའི་ཚིག་ཤིན་ཏུ་བརྟན༌[^2305]པའོ། །

[Block 2630]
དགེ་བའི་ཆོས་བསྒྲུབ་པར༌[^2306]འདུན་པ་ལས་བསྒྲུབ་པ༌[^2307]འབྱུང་ཞིང་དགེ་བའི་ཆོས་སྐྱེ་བར་འགྱུར་བས་ན། འདུན་པའི་དགེ་བའི་ཆོས་ཐམས་ཅད་ཀྱི་རྩ་བ་ཞེས་བྱའོ། །
--- END BLOCKS ---
