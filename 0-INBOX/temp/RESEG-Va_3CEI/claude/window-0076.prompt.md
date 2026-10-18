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
[Block 2661]
མདོ་ལས།

[Block 2662]
དེ་ནས༌[^2272]དབུལ་པོ་དེས་ནི་དེ༌[^2273]མཐོང་བ། ། ཞེས་པ་ནས། ཁྱོད་ནི་གླ༌[^2274]ཡང་ཉིས་འགྱུར་སྦྱིན་པར་བྱས། །ཞེས་པ། འདིར་ནི་ཉེས་པར་གྱུར་ན་མི་རུང་སྟེ། །ཞེས་པ་ཡང་སྔོན་གྱི་སྤྱོད་པ་དང་བྲལ་ཏེ་ཆེན་པོ་སྤྱོད་དུ་མ་བཅུག་གམ་ཞེས་དོགས་པ་སྐྱེའོ།[^2275] །ཞར་བ་འཐེང༌[^2276]གྲུམ་ཅན་ཞེས་པ་ནི་ཐེག་པ་རྣམ་གཉིས་ཀྱི་བདེན་པ་སྟོན་པ་གཞུང་མ་རྫོགས་པའི་དཔེའོ། །

[Block 2663 [HEADING]]
###### **ཐེག་པ་རྣམ་གཉིས་དྲང་བའི་དཔེ།** ^4-4-2-2-1-2-1-5-0

[Block 2664]
མདོ་ལས།

[Block 2665]
མི་དེས་འདི་ལྟ་བུ་ཡི་སྒྲ་ཐོས་ནས། །ཞེས་པ་ནས། ང་ཡི་བུ་ཡིན་ཡང་དག་གདོན་མི་ཟ། །ཞེས་པའི་བར་དུ་ནི་ཉོན་མོངས་པའི་ཕྱག་དར་བྱས་ཤིང་ཕུང་པོ་ལྔའི་ཁང་པ་གཙང་མར་བྱས་པ་དང་། རྐང་པ་བསྐུ་ཞེས་པ། རྐང་པ་ནི་རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞིའོ། །

[Block 2666]
བསྐུ་བ་ནི་སྡོམ་པ་འཛིན་པའི་སྤྱོད་ལམ་མོ། །

[Block 2667]
མདོ་ལས།

[Block 2668]
དེ་ནི་ཁད་ཀྱིས༌[^2277]བགས་ཀྱིས༌[^2278]ཁྱིམ་དུ་བཅུག །ཞེས་པ༌[^2279]ནས། བགས་ཀྱིས༌[^2280]མི་དེ་དེས་ཡིད་རྣམ་པར་ཕབ། །ཅེས་པའི་བར་དུ་ནི་འདིས་འཕགས་པའི་གནས་སུ་སོན་པ་བསྟན་ཏེ། ལོ་ཉི་ཤུ་ཞེས་པ༌[^2281]ནི་ཚིག་ལྷུག་པའི་ནང་ནས་བསྟན་ཟིན་ཏོ། །

[Block 2669 [HEADING]]
###### **ཆེན་པོ་ལ་རེ་བ་མེད་པའི་དཔེ།** ^4-4-2-2-1-2-1-6-0

[Block 2670]
མདོ་ལས།

[Block 2671]
དེ་ནི་ཤེལ་ལམ་འགྲོན་བུ་མུ་ཏིག་ཀྱང་། །ཞེས་པ་ནས་ཆུང་ངུ་ལ་དད་པའི་ཡོན་ཏན་ཏེ། བཀོལ་བ་དེ་སྙེད༌[^2282]དེ་རིང་ཤིན་ཏུ་བདེ། །ཞེས་པའི་བར་དུ་ནི་རིན་པོ་ཆེ་སྣ་ཚོགས་བསྟན་པ་ཡང་ཆེན་པོ་བསྟན་ཀྱང་རེ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2672 [HEADING]]
###### **རྙེད་པ་ཆེན་པོ་རྙེད་པའི་དཔེ།** ^4-4-2-2-1-2-2-0

[Block 2673]
དབུལ་པོའི་བསམ་པ་རྗེས་སུ་ཤེས་པ་ལ་སོགས་པ་ནི་རྙེད་པ་ཆེན་པོ་རྙེད་པའི་དཔེའོ། །

[Block 2674]
འོག་ནས་ལོ་ཉི་ཤུ་ཞེས་པ་ནི་སློབ་པ་དང་མི་སློབ་པའི་འབྲས་བུ་ཐོབ་པ་ཞེས་ཀྱང་སྦྱར་རོ། །

[Block 2675]
ཤིན་ཏུ་བདེ་ཞེས་པ་ནི་འབྲས་བུ་ཆེན་པོ་ཐོབ་པའི་ཕྱིར་ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ༌[^2283]ཀུན་དང་ལྡན་པའོ། །

[Block 2676 [HEADING]]
###### **དཔེ་དང་དོན་དུ་སྦྱོར་བ།** ^4-4-2-2-1-3-0

[Block 2677]
མདོ་ལས།

[Block 2678]
དེ་བཞིན་རྣམ་པར་འདྲེན་པས་བདག་ཅག་རྣམས། །ཞེས་པ་ནས།[^2284] ཁྱེད་ཀྱི་ཉན་ཐོས་ང་ཡི་བུ་ཡིན་ན། །ཞེས་པའི་བར་དུ་འདི་ནི་དཔེ་དང་དོན་དུ་སྦྱར་ཏེ་བསྟན་པའོ། །

[Block 2679]
ཆུང་ངུ་ལ་དད་པས་རེ་བ་མེད་པ་བསྟན་པ་ཡང་དེ་བཞིན་གཤེགས་པས༌[^2285]ཡེ་ཤེས་པའི་བསྐལ༌[^2286]པ༌[^2287]བསྟན་པ་སྟེ། ཟག་པ་མེད་པའི་གནས་ཉིད་ཀྱིས་ཆོག་པར་སེམས་པས་རེ་བ་མེད་པའོ། །

[Block 2680]
མདོ་ལས།

[Block 2681]
བདག་ལ་འཇིག་རྟེན་མགོན་གྱིས་བཀའ་སྩལ་པ། །ཞེས་པ་ནས། གང་གིས༌[^2288]ལམ་གོམས་སངས་རྒྱས་འགྱུར་བའོ། །ཞེས་པའི་བར་དུ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ཕྱེད༌[^2289]དུ་བསྟན་གྱི་ཉན་ཐོས་པའི་དོན་དུ་མ་བསྟན་པས་རེ་བ་མེད་པ་བསྟན་ཏེ། གང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ཞུགས་པ་རྣམས་ལ་ཤོད་ཅིག་པར་སྦྱར་རོ། །

[Block 2682]
མདོ་ལས།

[Block 2683]
དེ་ཕྱིར་བདེ་བར་གཤེགས་པས་བཀའ་སྩལ་ནས། །ཞེས་པ་ནས། བདག་གིས༌[^2290]བླ་ན་མེད་པའི་ལམ་བསྟན་ནས། །ཞེས་པའི་བར་དུ་ནི་ཐེག་པ་རྣམ་གཉིས་ཀྱང་དེ་བཞིན་གཤེགས་པའི་གསུང་ལ་བརྟེན་ཞེས་པའོ། །

[Block 2684]
མདོ་ལས།

[Block 2685]
དེ་ཕྱིར་བདེ་བར་གཤེགས་པས་བཀའ་སྩལ་ནས། །ཞེས་པ་ནས། །ལུང་ནི་མྱ་ངན་འདའ་བ༌[^2291]མཐར་ཐུག་པ། །ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་ལུང་བསྟན་པ་སྟེ། ཇི་ལྟར་གཅིག་གིས་ལུང་སྟོན་པ་བཞིན་གཞན་དག་ཀྱང་དེ་བཞིན་དུ་གསུངས་ཞེས་པའོ། །

[Block 2686]
ཆོས་ཀྱི་མཛོད་རྣམས་ཡང་དག་གསུངས་པ་ནི་རྒྱལ་བའི་སྲས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་བསྟན་པའོ། །

[Block 2687]
རྒྱལ་བའི་ཡེ་ཤེས་རབ་ཏུ་བཤད་མེད༌[^2292]ཀྱི། །ཞེས་པ་ནི་དཔེ་དང་དོན་དུ་སྦྱར་བའོ། །

[Block 2688]
འགོག་པ་དང་སྐྱེ་བ་རྣམ་པར་སྤངས་ན༌[^2293]ཐེག་པ་ཆེན་པོ་ལ་དད་པར་མ་གྱུར་པ་ནི་ཉན་ཐོས་ཀྱི་ཞི་བ་མྱ་ངན་ལས་འདས་པས་ཆོག་པར་སེམས་པའོ། །

[Block 2689]
བདག་ཅག་ནམ་ཡང་འདི་ལ་མི་སྨོན་པ། །ཞེས་པ་ནི་སྟོང་པ་ཉིད་དང་མཚན་མ་མེད་པ་དང་སྨོན་པ་མེད་པར༌[^2294]རིམ་པ་བཞིན་དུ་སྟོན་ཏེ། ཐེག་པ་ཆེན་པོའི་ཡེ་ཤེས་ལ་མི་རེ་ཞེས་པའི་དོན་ཏོ། །

[Block 2690]
མདོ་ལས།

[Block 2691]
ཡུན་རིང་སྟོང་པ་ཉིད་ལ་ཡོངས་སུ་བསྒོམས། །ཞེས་པ་ནས། [^2295]དེ་ལ་ནམ་ཡང་བདག་ཅག་འདོད་པ་མེད། །ཅེས་པའི་བར་དུ་ནི་ཉན་ཐོས་ཀྱི་མྱ་ངན་ལས་འདའ་བ༌[^2296]རྙེད་པས་དེ་བཞིན་གཤེགས་པའི་དྲིན་བསབ་པའི་ཕྱིར་གཞན་གྱི་ཆོས་བཤད་པ་ཐོས་ཀྱང་རེ་བ་མེད་པ་ནི་ལྷག་མ་དང་བཅས་པའི་མྱ་ངན་ལས་འདས་པ་ལ་གནས་པའི་ཕྱིར་རོ། །

[Block 2692]
མདོ་ལས།

[Block 2693]
བདག་ཅག་འཇིག་རྟེན་སློབ་དཔོན་རང་བྱུང་གི །ཞེས་པ་ནས། །བརྟུལ་ནས་ཡེ་ཤེས་འདི་དག་རབ་ཏུ་བྱིན།[^2297] །ཞེས་པའི་བར་དུ་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཉན་ཐོས་པའི་ཆེད་དུ་འདི་མ་བསྟན་ཏོ་ཞེས་ཚིག་བརྟུལ་བ་སྟེ། དབང་པོ་མ་སྨིན་པའི་ཕྱིར་རོ། །

[Block 2694]
ཇི་ལྟར་ནོར་མང་དུ་བདོག་པའི་སྐྱེས་བུ་ཆུང་ངུ་ལ་དད་པ་རྣམས་ཐབས་མཁས་པས་བགས་ཀྱིས་བརྟུལ༌[^2298]ཞིང་སྦྱིན༌[^2299]པ༌[^2300]ནི་དཔེ་དང་དོན་གཉི་ག་སྦྱར་ཏེ་ཕྱིས་ཐོབ་པར་འགྱུར་བ་བསྟན་པའོ། །

[Block 2695]
མདོ་ལས།

[Block 2696]
དེ་རིང་བདག་ཅག་འཕྲལ་ལ་ངོ་མཚར་གྱུར། །ཞེས་པ་ནས། ཚངས་པར་སྤྱོད་པ་མཆོག་རབ་རྣམ་དག་གང་། །ཞེས་པའི་བར་དུ་ནི། རེ་བ་མེད་པ་ལས་འབྲས་བུ་ཆེན་པོ་ཐོབ་པར་བསྟན་པ་དང་། དེ་ཡང་ལམ་བསྒོམས་པ༌[^2301]དང་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པའི་རྒྱུ་ལས་འབྲས་བུ་དེ་ཐོབ་ཅེས་པའོ། །

[Block 2697]
མདོ་ལས།

[Block 2698]
འདྲེན་པའི་བསྟན་པ་རྣམས་ལ་ཤིན་ཏུ་བསྙེན། །ཞེས་པ་ནས། འདི་འདྲ་བ་ཡི་དཀའ་བ་གང་མཛད་པ། །ཞེས་པའི་བར་དུ་ནི་འབྲས་བུ་ཆེན་པོ༌[^2302]མངོན་དུ་ཐོབ་སྟེ། འཕགས་པ་ཉན་ཐོས་སུ་ངེས་པ་གཞན་ལ༌[^2303]ཕན་འདོགས་པར་འོས་པ་མཆོད་པའི་གནས་སུ་གྱུར་པ་བསྟན་པའོ། །

[Block 2699]
དེ་བཞིན་གཤེགས་པའི་དྲིན་གྱི་ལན་ལྡོན་པ༌[^2304]ནི་གཞན་གྱིས༌[^2305]མ་ཡིན་གྱི༌[^2306]འདི་འདྲ་བ་ཐོབ་པ་ཞེས་སོ། །

[Block 2700 [HEADING]]
###### བཅོམ་ལྡན་འདས་ཀྱི་བཀའ་དྲིན་ཟབ་པ། ^4-4-2-2-2-0
--- END BLOCKS ---
