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
[Block 3256]
དེ་བས་ན་དེའི་འོག་ཏུ་འཐབས་པ་ཉིད་དང་ཡུན་རིང་པོར་འཐབས་པ་ཉིད་ལ་འདིས་ཉམས་པར་མ་བྱས་པ་ཉིད་ཅེས་བྱ་བ་ཤེས་པར་མི་བྱ་སྟེ་དེའི་ཕྱིར་འདི་ལ་སྨད་པར་བྱའོ། །

[Block 3257]
གལ་ཏེ་དེ་དབང་བ་ཆུང་མ་མ་ཡིན་པར་བསྒྲགས་པ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་གང་དུ་འདི་ལ་ཕྲད་པ་དེ་གལ་ཏེ་དེ་ནི་དེའི་དབང་དུ་འགྱུར་རོ། །

[Block 3258]
ཆུང་མ་མ་ཡིན་པ་ཞེས་བྱ་བ་རྗེས་སུ་བཅུག་པ་ཉིད་ལ་ཉམས་པ་ཉིད་དེ་འཐབས་པ་ཙམ་འགའ་ཞིག་གིས་དེ་ཉམས་པར་མ་ཟད་དོ། །

[Block 3259]
འཐབས་པ་ཉིད་ཀྱི་མོད་ལ་དང་། འོག་ཏུ་དང་དུམ་པ་བཅད་པ་ཉིད་དང་རྡེའུ་གསུམ་གཏོར་བ་ཉིད་དང་ཆོ་ག་བཏང་བ་ཉིད་དང་ཆུང་མ་མ་ཡིན་པར་བསྒྲགས་པ་ཉིད་དང་། དྲིལ་བསྒྲགས་པ་ཉིད་དག་ནི་སྲོག་དང་ལྡན་པ་ཉིད་དག་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་སྤྲད་པར་བྱ་བ་སྲོག་དང་ལྡན་པ་ཉིད་ཇི་སྙེད་སྤྲད་པར་འདོད་པ་དེ་རྣམས་ལ་ལྟུང་བ་དེ་སྙེད་པ་དེ་རྣམས་དེ་བཞིན་དུ་བསྐྱེད་པའོ། །

[Block 3260]
དེའི་འོག་ཏུ་འཐབས་པ་ལ་སོགས་པའི་ཆོས་ཇི་ཙམ་པ་འདི་རྣམས་ཡོད་པར་གྱུར་པ་ལ་འཇུག་པ་དེ་སྙེད་རྣམས་ལ་ཞེས་བྱ་བ་འདི་ལ་དེ་སྟོན་པའོ། །

[Block 3261]
བར་དུ་བསྒྲིབ་པ༌[^2231]བཞིན་དུ་འདི་རྣམས་ལ་ཡིད་ལ་གནས་པ་ལས༌[^2232]སོ་སོར་འདའ་བར་བྱེད་པ་ལ་ལྟུང་བ་སྐྱེད་པར་བྱེད་པའོ།[^2233] །དེ་བས་ན་འདི་རྣམས་ཡང་དག་པར་ཤེས་ཤིང་འདིས༌[^2234]ཞེས་བྱ་བ་ཤེས་པར་བྱའོ། །

[Block 3262]
དེའི་དུས་ལ་དེའི་རྗེས་ཀྱིས༌[^2235]སྒྲ་རིགས་པར༌[^2236]བྱའོ། །

[Block 3263]
ཇི་ལྟར་དེའི་འོག་ཏུ་སྤངས་པ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 3264]
དེའི་དང་པོ་གསུམ་ལ༌[^2237]ཉེས་བྱས་ཀྱི་དབང་དུ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་ཆུང་མ་དེ་དབང་བ་དེའི་དང་པོ་གསུམ་པོར༌[^2238]འཐབས་པ་ཉིད་ཀྱི་མོད་ལ་དང་འོག་ཏུ་དང་། དུམ་པ་བཅད་པ་ཉིད་ལ་ཏི༌[^2239]ལི་ཏིན་ཏ་ལི་ཀ་དུམ་པ་བཅད་པ་ཉིད་ལ་ནི་ཉེས་བྱས་ཀྱི་དབང་དུ་བྱས་པ་ཉིད་དོ། །

[Block 3265]
བྱེད་པ༌[^2240]པོ་ཉིད་ལ་གསུམ་པོ་ཉིད་ཀྱིས་སྦྱོར་བ་ཉིད་འདི་ལ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་བས་ན༌[^2241]སྦོམ་པོའི་ལྟུང་བ་ལ་ནི་འདིར༌[^2242]སྐུར་པ་འདེབས་པའོ། །

[Block 3266]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་ཆུང་མ་དང་པོ་གསུམ་པོ་ཆུ་ཚིགས་ཀྱིས་བྱིན་པ་དང་། རིན་ཆས་ཉོས་པ་དང་། བཙན་ཕྲོགས་སུ་ཐོབ་པ་འཐབས་པའི་མོད་ལ་ཡིན་པ་འཐབས་པའི་འོག་མ་ཡིན་པ༌[^2243]དང་། ཏི་ལི་ཏིན་ཏ༌[^2244]ལི་ཀ་དུམ་པ་མ་བཅད་པ་དང་། རྡེའུ་གསུམ་མ་གཏོར་བ་དང་། ཆོ་ག་མ་བཏང་བ་དང་། ཆུང་མ་མ་ཡིན་པར་མ་བསྒྲགས་པ་དང་། དྲིལ་མ་བསྒྲགས་པ་དག་གིས་སྡུམ་བྱེད་ཅིང་མཐུན་པར་གྱུར་ན་ཉེས་བྱས་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 3267]
དགེ་སློང་གིས་ཆུང་མ་དང་པོ་གསུམ་པོ་འཐབས་པའི་མོད་ལ་དང་འཐབས་པའི་འོག་ཏུ་ཡིན་ལ་ཏི་ལི་ཏིན་ཏ་ལི་ཀ་དུམ་པ་བཅད་པ་མ་ཡིན་ལ། ཇི་སྲིད་དྲིལ་མ་བསྒྲགས་པའི་བར་དག་གིས༌[^2245]སྡུམ་བྱེད་ཅིང་མཐུན་པར་གྱུར་ན་ཉེས་བྱས་གཉིས་སུ་འགྱུར་རོ། །

[Block 3268]
དགེ་སློང་གིས་ཆུང་མ་སྔ་མ་གསུམ་པོ་འཐབས་པའི་མོད་ལ་དང་། ཏི་ལི་ཏིན་ཏ་ལི་ཀ་དུམ་པ་བཅད་པ་ནས་ཇི་སྲིད་རྡེའུ་གསུམ་མ་གཏོར་གྱི་བར་ལ་དེ་སྲིད་དུ་སྔར་བཞིན་དུ་ཉེས་བྱས་གསུམ་དུ་འགྱུར་རོ། །

[Block 3269]
དགེ་སློང་ཆུང་མ་སྔ་མ་གསུམ་པོ་འཐབས་པའི་མོད་ལ་དང་། ཇི་སྲིད་དུ་རྡེའུ་གསུམ་གཏོར་བ་ཡིན་ལ། ཆོ་ག་མ་བཏང་བ་ནས་དེ་སྲིད་དུ་ཉེས་བྱས་གསུམ་དང་སྦོམ་པོ་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 3270]
དགེ་སློང་གིས་ཆུང་མ་སྔ་མ་གསུམ་པོ་འཐབས་པའི་མོད་ལ་དེ་ཇི༌[^2246]སྲིད་དུ་ཆོ་ག་བཏང་བ་ཆུང་མ་མ་ཡིན་པར་མ་བསྒྲགས་པ་དེ་སྲིད་དུ་ཉེས་བྱས་གསུམ་དང་སྦོམ་པོ་གཉིས་སུ་འགྱུར་རོ། །

[Block 3271]
དགེ་སློང་གིས་ཆུང་མ་སྔ་མ་གསུམ་པོ་ཇི་སྲིད་དུ་ཆུང་མ་མ་ཡིན་པར༌[^2247]བསྒྲགས་ནས་དྲིལ་མ་བསྒྲགས་པ་དག་གིས༌[^2248]སྡུམ་བྱེད་ཅིང་མཐུན་པར་གྱུར་ན་ཉེས་བྱས་གསུམ་དང་སྦོམ་པོ་གཉིས་དང་དགེ་འདུན་ལྷག་མ་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 3272]
དགེ་སློང་གིས་ཆུང་མ་སྔ་མ་ནས་ཇི་སྲིད་དྲིལ་བསྒྲགས་པའི་བར་དག་གིས༌[^2249]སྡུམ་བྱེད་ཅིང་མཐུན་པར་གྱུར་ན་ཉེས་བྱས་གསུམ་དང་སྦོམ་པོ་གཉིས་དང་དགེ་འདུན་ལྷག་མ་གཉིས་སུ་འགྱུར་རོ༌[^2250]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3273]
ཅིའི་ཕྱིར་འདིའམ་འདི་མི་སྤྲད། གྱོས་པོའི་གན་དུ་མི་འགྲོ་མི་བཀྲི་ཞེས་ཟེར་བ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ལ། ཀྱང་ངོ་ཞེས༌[^2251]བྱ་བའི་སྒྲ་ནི་ཉེས་བྱས་ཀྱི༌[^2252]དབང་དུ་བྱས་པ་ཉིད་དོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^2253]པའི་ཕྱིར་རོ། །

[Block 3274]
འདི་འམ་ཞེས་བྱ་བ་སྐྱེས་པའི་རྟགས་ཀྱིས༌[^2254]གནས་ལ་འདི་ཞེས་བྱ་བ་བུད་མེད་ཀྱི་རྟགས་བལྟ་བར་བྱའོ། །

[Block 3275]
ཅིའི་ཕྱིར་འདི་འམ་འདི་མི་སྤྲད༌[^2255]གྱོས་པོའི་གན་དུ་མི་འགྲོའོ༌[^2256]ཞེས་བྱ་བ་ནི་ཅིའི་ཕྱིར་བྱ་བ་དང་སྦྱར་རོ། །

[Block 3276]
འདི་ནི་ཅིའི་ཕྱིར་གྱོས་པོའི་གན་དུ་མི་འགྲོ་མི་བཀྲི་ཞེས་ཟེར་བ་འདི་ལ་ཡང་། ཅིའི་ཕྱིར་འདི་གྱོས་པོའི་གན་དུ་མི་འགྲོ་མི་བཀྲི་ཞེས་པའི་སྒྲ་ནི་རབ་ཏུ་དབྱེ་བ་ཉེ་བར་བསྟན་པའི་དོན་དུའོ། །

[Block 3277]
ཅིའི༌[^2257]ཕྱིར་བུ་མོ་འདི་མི་སྤྲད། ཅིའི་ཕྱིར་ཁྱེའུ་འདི་གྱོས་པོའི་གན་དུ་མི་འགྲོ། །ཅིའི་ཕྱིར་བུ་མོ་འདི་གྱོས་པོའི་གན་དུ་མི་འགྲོ་ཞེས་བྱ་བ་རྣམ་པ་དེ་ལྟ་བུ་དག་སྨྲ་བ་རྣམས་ལ་ཉེས་བྱས་ཀྱི་དབང་དུ་བྱས་པ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3278]
སྨྱན་བྱེད་པའི་དགེ་འདུན་ལྷག་མ་རྣམ་པར་འབྱེད་པའོ།། །།

[Block 3279]
མངལ་ན་གནས་པ་དང་མེད་པ་དང་ངེས་པ་དང་མི་བརྟེན་པ༌[^2258]དང་། ཉོས་པ་དང་མཐུན་པ་དང་བདག་གི་སྨྱན་བྱེད་པ་ནི་སྦོམ་པོའོ་ཞེས་བྱ་བ་ལ། སྨྱན་གྱི་ལས་ནི་སྨྱན་བྱེད་པའོ། །

[Block 3280]
སོ་སོར་འདི་ལ་མངལ་ལ་སོགས་པ་རྣམས་ལ་ཉེ་བར་ལྟུང་བའོ། །

[Block 3281]
མངལ་ན་གནས་པ་དང་མེད་པ་དང་ངེས་པ་དང་མི་བརྟེན་པ༌[^2259]དང་ཉོས་པ་དང་མཐུན་པ་དང་བདག་ནི་དེ་རྣམས་ཉིད་ཡིན་ཏེ། དེ་རྣམས་ཀྱི་སྨྱན་བྱེད་པ་ནི༌[^2260]སྦོམ་པོར་འགྱུར་རོ། །

[Block 3282]
དེ་ལ་མངལ་དང་མི་མཐུན་པའི་རབས་འབྱུང་བའི་ཕྱིར་འདིར་གང་དག་གིས་ཚར་གཅོད་པ་དེ་ནི་མེད་པ་ཞེས་བྱ་བར་བརྗོད་པ་ཡིན་ནོ། །

[Block 3283]
དེའི་མཐུན་པ་ཉིད་ཀྱིས་དེའི་སྨྱན་བྱེད་པར་རིག་པར་བྱའོ།[^2261] །དེ་བཞིན་དུ་མངལ་ལ་ཡང་སྟེ་མངལ་ན་གནས་པའི་སྨྱན་བྱེད་པ་ལ་ནི་སྦོམ་པོའི་ལྟུང་བ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3284]
འདིར་གཞུང་ནི་སྦྲུམ་མ་གཅིག་ནི་བུ་མོའི་སྦྱར་ཏེ།

[Block 3285]
གཉིས་པ་ནི་ཁྱེའུ་ལ་དེ་དག་གི་སྨྱན་བགྱིས༌[^2262]ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3286]
ཁྱིམ་བདག་བུ་མེད་པ་རྣམས་ཀྱི་སྨྱན་བགྱིས་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3287]
ངེས་པ་དང་ཞེས་བྱ་བ་ནི་དེ་དག་གི་སྨྱན་བྱེད་ན་སྦོམ་པོའོ། །

[Block 3288]
དགེ་སློང་མ་ལ་སྨྱན་བགྱིས༌[^2263]ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3289]
བརྟུལ་ཞུགས་ལ་གནས་པ་གཞན་ཐམས་ཅད་ལ་ཡང་དེ་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 3290]
མི་བསྟེན་པ༌[^2264]ཞེས་བྱ་བ་ནི་སྨྱན་བྱེད་པ་ལ་ཟ་མ་དང་མ་ནིང་ཕོ་དང་མ་ནིང་མོ་དག་ནི༌[^2265]སྨྱན་བྱེད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཐམས་ཅད་ཉེས་པ་སྦོམ་པོ༌[^2266]ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3291]
འདི་རྣམས་བསྟེན་པ་ལ་མོའི་དབང་པོའམ་ཕོའི་དབང་པོ་ཡོད་པ་མ་ཡིན་ཏེ། དེ་བས་ན་ཟ་མ་ལ་སོགས་པ་མི་བསྟེན་པ་རྣམས་སོ། །

[Block 3292]
འདིར་གཞུང་ནི་བུད་མེད་ཉོས་པ་ལ་སྨྱན་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3293]
མཐུན་པའི་སྨྱན་བྱེད་ན་དགེ་སློང་གིས་སྤྲིང་བ་མནོས་ཏེ་ལན་གྲངས་མང་པོ་འཕྲིན༌[^2267]ཕར་སྐྱེལ་བ་དང་ཚུར་སྐྱེལ་བར་བགྱིད་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3294]
བདག་གི་སྨྱན་བྱེད་པ་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱི་ཕྱིར་བདག་ཉིད་སྨྱན་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3295]
ཕྲིན་ཕར་སྐྱེལ་བའི་ཚིག་ལ་བདག་ཉིད་ལ་སྨྱན་བྱེད་པ་ལ་སྦོམ་པོའི་ཚིག་འདིའོ། །
--- END BLOCKS ---
