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
འདོད་ཆགས་དང་བྲལ་བའི་སྒོ་ནས་ནི༌[^2260]བདུན་ཅུ༌[^2261]རྩ་གསུམ་སྟེ། འཆིང་བ་མཐའ་དག་དང་ལྡན་པ་དང་འདོད་པ༌[^2262]ལས་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་དགུ་ནས་དེ་བཞིན་དུ་ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ལས་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་གྱི་བར་དུའོ། །

[Block 3257]
རྟེན་གྱི་སྒོ་ནས་ནི་དགུ་སྟེ། གླིང་གསུམ་དང་ལྷའི་རིས་དྲུག་ཏུ་སྐྱེས་པའོ། །

[Block 3258]
དབང་པོ་དང་རིགས་དང་ལམ་དང་འདོད་ཆགས་དང་བྲལ་བ་དང་རྟེན་གྱི་སྒོ་ནས་བསྡོམས༌[^2263]ན་ནི། འབུམ་བཞི་ཁྲི་བདུན་སྟོང་བརྒྱད་བརྒྱ་ཉི་ཤུ་རྩ་ལྔར་འགྱུར་ཏེ། གང་ཟག་གཞན་དག་ཀྱང་ཅི་རིགས་པར་དེ་བཞིན་དུ་བརྩི་བར་བྱའོ། །

[Block 3259 [HEADING]]
##### གཉི་གའི་ཆ་ལས་རྣམ་པར་གྲོལ་བ་དང་ཤེས་རབ་ཀྱིས་རྣམ་པར་གྲོལ་བ། ^3-2-13-1-0

[Block 3260]
གཉི་གའི་ཆ་ལས་རྣམ་པར་གྲོལ་བ་ཞེས་བྱ་བ་འདི་ནི་གང་། ཤེས་རབ་ཀྱིས༌[^2264]རྣམ་པར་གྲོལ་བ་ནི་གང་ཞེ་ན།

[Block 3261 [VERSE]]
འགོག་ཐོབ་གཉི་ག་ལས་རྣམ་གྲོལ། །
ཤེས་རབ་ཀྱིས་ནི་ཅིག་ཤོས་སོ། །

[Block 3262]
གང་འགོག་པའི་སྙོམས་པར་འཇུག་པ་ཐོབ་པ༌[^2265]དེ་ནི་གཉི་གའི་ཆ་ལས་རྣམ་པར་གྲོལ་བ་ཡིན་ཏེ། ཤེས་རབ་དང་ཏིང་ངེ་འཛིན་གྱི་སྟོབས་དག་གིས་ཉོན་མོངས་པ་དང་། སྙོམས་པར་འཇུག་པའི་སྒྲིབ་པ༌[^2266]ལས་རྣམ་པར་གྲོལ་བའི་ཕྱིར་རོ། །

[Block 3263]
ཅིག་ཤོས་ནི་ཤེས་རབ་ཀྱིས༌[^2267]རྣམ་པར་གྲོལ་བ་ཡིན་ཏེ། ཤེས་རབ་ཀྱི༌[^2268]སྟོབས་ཀྱིས་ཉོན་མོངས་པའི་སྒྲིབ་པ་འབའ་ཞིག་ལས་རྣམ་པར་གྲོལ་བའི་ཕྱིར་རོ། །

[Block 3264 [HEADING]]
#### སློབ་པ་ཡོངས་སུ་རྫོགས་པ། ^3-2-14-0

[Block 3265]
བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 3266 [VERSE]]
འདི་ལ་གང་ཞིག་ཉོན་མོངས༌[^2269]ལྔ་སྤངས་ཏེ། །
མི་འཕྲོགས་ཆོས་ལྡན་སློབ་པ་ཡོངས་སུ་རྫོགས། །

[Block 3267]
ཞེས་གང་གསུངས་པ། ཇི་ཙམ་གྱིས་ན་སློབ་པ་ཡོངས་སུ་རྫོགས་པ་ཡིན་ཞེ་ན།

[Block 3268 [VERSE]]
སྙོམས་འཇུག་དབང་པོ་འབྲས་རྣམས་ཀྱིས། །
སློབ་པ་ཡོངས༌[^2270]རྫོགས་ཞེས་བྱའོ། །

[Block 3269]
སློབ་པ་ཡོངས་སུ་རྫོགས་པ་ནི་རྣམ་པ་གསུམ་སྟེ། འབྲས་བུ་དང་། དབང་པོ་དང་། སྙོམས་པར་འཇུག་པ་ལས་སོ། །

[Block 3270]
ཕྱིར་མི་འོང་བ་དད་པས་མོས་པ་ལུས་ཀྱིས༌[^2271]མངོན་སུམ་དུ་བྱེད་པ་མ་ཡིན་པ་ནི་འབྲས་བུ་ཁོ་ན་ལས་སོ། །

[Block 3271]
མཐོང་བས་ཐོབ་པ་འདོད་ཆགས་དང་མ༌[^2272]བྲལ་བ་ནི་དབང་པོ་ཁོ་ན་ལས་སོ། །

[Block 3272]
ཕྱིར་མི་འོང་བ་མཐོང་བས་ཐོབ་པ་ལུས་ཀྱིས་མངོན་སུམ་དུ་བྱེད་པ་མ་ཡིན་པ་ནི་འབྲས་བུ་དང་དབང་པོ་ལས་སོ། །

[Block 3273]
དད་པས་མོས་པ་ལུས་ཀྱིས་མངོན་སུམ་དུ་བྱེད་པ་ནི་འབྲས་བུ་དང་སྙོམས་པར་འཇུག་པ་ཁོ་ན་ལས་སོ། །

[Block 3274]
མཐོང་བས་ཐོབ་པ་ལུས་ཀྱིས༌[^2273]མངོན་སུམ་དུ་བྱེད་པ་ནི་འབྲས་བུ་དང་། དབང་པོ་དང་། སྙོམས་པར་འཇུག་པ་ལས་སོ། །

[Block 3275]
སྙོམས་པར་འཇུག་པ་ཁོ་ན་དང་། སྙོམས་པར་འཇུག་པ་དང་། དབང་པོ་ལས་ཡོངས་སུ་རྫོགས་པ་ཉིད་ནི་མེད་དོ། །

[Block 3276]
གཉིས་ཀྱིས༌[^2274]མི་སློབ་ཡོངས་སུ་རྫོགས། །དབང་པོ་དང་སྙོམས་པར་འཇུག་པ་ལས་སོ། །

[Block 3277]
འབྲས་བུ་ཡོངས་སུ་མ་རྫོགས་པ་ལ་ནི་མི་སློབ་པ་ཉིད་ཀྱང་མེད་པ་ཁོ་ན་ཡིན་པས་འདིའི་འབྲས་བུ༌[^2275]རྫོགས་པ་ནི་ཡོངས་སུ་རྫོགས་པ་ཉིད་དུ་རྣམ་པར་མ་བཞག་གོ། །ཤེས་རབ་ཀྱིས་རྣམ་པར་གྲོལ་བ་དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ་ནི་དབང་པོ་ཁོ་ན་ལས་སོ། །

[Block 3278]
གཉི་གའི་ཆ་ལས་རྣམ་པར་གྲོལ་བ་དུས་ཀྱིས༌[^2276]རྣམ་པར་གྲོལ་བ་ནི་སྙོམས་པར་འཇུག་པ་ཁོ་ན་ལས་སོ། །

[Block 3279]
གཉི་གའི་ཆ་ལས་རྣམ་པར་གྲོལ་བ་དུས༌[^2277]དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ་ནི་དབང་པོ་དང་སྙོམས་པར་འཇུག་པ་དག་ལས་སོ། །

[Block 3280 [HEADING]]
#### ལམ་རྣམ་པ་བཞི། ^3-2-15-0

[Block 3281]
འཇིག་རྟེན་པ་དང་འཇིག་རྟེན་ལས་འདས་པ་དང་། མཐོང་བ་དང་བསྒོམ་པ་དང་མི་སློབ་པའི༌[^2278]ལམ་རྣམས་དང་། སྦྱོར་བ་དང་། བར་ཆད་མེད་པ་དང་རྣམ་པར་གྲོལ་བའི་ལམ༌[^2279]དང་ཁྱད་པར༌[^2280]ཅན་གྱི་ལམ་རྣམས་ཞེས་བྱ་བ་ལམ་གྱི་བྱེ་བྲག་མང་པོ་ཞིག་བཤད་པ་དེ་དག་མདོར་བསྡུ་ན་ལམ་རྣམ་པ་དུ་ཞིག་ཡིན་ཞེ་ན། མདོར་ན་ལམ་ནི་རྣམ་པ་བཞི་སྟེ།

[Block 3282 [VERSE]]
ཁྱད་པར་ཅན་དང་རྣམ་གྲོལ་དང་། །
བར་ཆད་མེད་དང་སྦྱོར་ཞེས་བྱ། །

[Block 3283]
སྦྱོར་བའི་ལམ་ནི་གང་གི༌[^2281]མཇུག་ཐོགས་སུ་བར་ཆད་མེད་པའི་ལམ་སྐྱེ་བའོ། །

[Block 3284]
བར་ཆད་མེད་པའི་ལམ་ནི་གང་གིས་སྒྲིབ་པ་རབ་ཏུ་སྤོང་བའོ། །

[Block 3285]
རྣམ་པར་གྲོལ་བའི་ལམ་ནི་དེས་སྤང་བར༌[^2282]བྱ་བའི་སྒྲིབ་པ་ལས་ངེས་པར་གྲོལ་པ་དང་པོ་ཉིད་དུ་སྐྱེ་བ་གང་ཡིན་པའོ། །

[Block 3286]
ཁྱད་པར་ཅན་གྱི་ལམ་ནི་དེ་དག་ལས་གཞན་པའི་ལམ་གང་ཡིན་པའོ། །ཅིའི་ཕྱིར་ལམ་ཞེས་བྱ༌[^2283]ཞེ་ན། དེ་ནས་དེར་འགྲོ་བའི་ཕྱིར་རམ། འདིས་མྱ་ངན་ལས་འདས་པ་ཚོལ་བའི་ཕྱིར་འདི་ནི་མྱ་ངན་ལས་འདས་པའི་ལམ་ཡིན་ནོ། །

[Block 3287]
རྣམ་པར་གྲོལ་བ་དང་ཁྱད་པར་ཅན་གྱི་ལམ་དག་ཇི་ལྟར་ན་ལམ་ཉིད་ཡིན་ཞེ་ན། དེ་དང་འདྲ་བ་དང་། ཆེས་ཆེ་བ་ཡིན་པའི་ཕྱིར་ཏེ། གོང་ནས་གོང་དུ་ཕྱིན་པར་བྱེད་པའི་ཕྱིར་རམ། ཕུང་པོའི་ལྷག་མ་མ་ལུས་པར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 3288]
ཡང་ལམ་ཉིད་མྱ་ངན་ལས་འདས་པ་སྒྲུབ་པར་བྱེད་པའི་ཕྱིར་སྒྲུབ་པ་ཞེས་གསུངས་སོ། །

[Block 3289 [HEADING]]
#### ལམ་སླ་བ་དང་དཀའ་བ། ^3-2-16-0

[Block 3290]
ལམ་ནི་བཞི་སྟེ། མངོན་པར་ཤེས་པ་བུལ་ལ་དཀའ་བའི་ལམ་ཡང་ཡོད། [^2284]མངོན་པར་ཤེས་པ་མྱུར་ལ་དཀའ་བའི་ལམ་ཡང་ཡོད་དེ། [^2285]དེ་བཞིན་དུ༌[^2286]སླ་བ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 3291]
དེ་ལ། བསམ་གཏན་དག་གི་ལམ་རྣམས་སླ། །བསམ་གཏན་བཞིའི་ལམ་ནི༌[^2287]སླ་བ་ཡིན་ཏེ། ཡན་ལག་གིས་ཡོངས་སུ་ཟིན་པ་དང་། ཞི་གནས་དང་ལྷག་མཐོང་མཉམ་པ་དག་གིས་འབད་མི་དགོས་པར་རང་གི༌[^2288]ངང་གིས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3292]
ས་གཞན་དག་གི་དཀའ་བ་ཡིན། །མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། གཟུགས་མེད་པ་རྣམས་ཀྱི་ལམ་ནི། ཡན་ལག་གིས་ཡོངས་སུ་མ་ཟིན་པའི་ཕྱིར་དང་། ཞི་གནས་དང་ལྷག་མཐོང་ཆུང་བའི་ཕྱིར་ལམ་དཀའ་བ་ཡིན་ཏེ། མི་ལྕོགས་པ་མེད་པ་དང་བསམ་གཏན་ཁྱད་པར་ཅན་ན༌[^2289]ནི་ཞི་གནས་ཆུང་ངོ་། །གཟུགས་མེད་པ་དག༌[^2290]ན་ནི་ལྷག་མཐོང་ཆུང་ངོ་། །ལམ་དེ་ཡང་རྣམ་པ་གཉིས་ཏེ།

[Block 3293 [VERSE]]
བློ་རྟུལ་མངོན་ཤེས་བུལ་བ་སྟེ། །
ཅིག་ཤོས་ཀྱི་ནི་མངོན་ཤེས་མྱུར། །

[Block 3294]
དབང་པོ་རྟུལ་པོ་ནི་ལམ་སླ་བའམ་དཀའ་བ༌[^2291]ཡང་རུང་སྟེ། མངོན་པར་ཤེས་པ་བུལ་བ་ཡིན་ནོ། །

[Block 3295]
དབང་པོ་རྣོན་པོ་ནི་མངོན་པར་ཤེས་པ་མྱུར་བ་ཡིན་ནོ། །
--- END BLOCKS ---
