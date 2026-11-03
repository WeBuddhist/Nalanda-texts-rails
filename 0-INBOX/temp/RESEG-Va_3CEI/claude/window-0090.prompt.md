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
[Block 3151]
མྱ་ངན་ལས་འདས་པ་ཆེན་པོའི་མདོ་ལས་ཀྱང་། མྱ་ངན་ལས་འདས་པ་ནི་ཇི་ལྟ་བུ། མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ནི་ཇི་ལྟ་བུ་ཞེས་དྲིས་པ་དང་། ཉན་ཐོས་དང་རང་སངས་རྒྱས་བསྐལ་པ་བརྒྱད་ཁྲིའམ། དྲུག་ཁྲིའམ། བཞི་ཁྲིའམ། ཉི་ཁྲིའམ། ཁྲི་གཅིག་གི་བར་དུ་བཞུགས་པའི་གནས་དེ་ནི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 3152]
འཕགས་པ་ཆོས་ཀྱི་རྒྱལ་པོའི་གནས་དེ་ནི་མྱ་ངན་ལས་འདས་པ་ཆེན་པོ་ཞེས་གསུངས་སོ།། །།

[Block 3153]
དམ་པའི་ཆོས་པུཎྜ་རཱི་ཀའི་འགྲེལ་པ། [^2671]བམ་པོ་བརྒྱད་པ་སྟེ་ཐ་མ།[^2672]

[Block 3154 [HEADING]]
#### དོན། ^4-7-9-0

[Block 3155]
མདོ་ལས་དགེ་སློང་རྣམས་གང་གི་ཚེ་ན་ཞེས་པ་ནས་བསམ་གཏན་ཆེན་པོ་དང་ལྡན་པ་གཟིགས་ན་ཞེས་པའི་བར་དུ་ནི་རྣམ་པ་གསུམ་དུ་དབྱེ་སྟེ། དོན་དང་། དཔེ་དང་། བསྡུ་བའོ། །

[Block 3156 [HEADING]]
##### ངེས་པའི་དོན། ^4-7-9-1-0

[Block 3157]
དང་པོ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། སྔར་ནི་ངེས་པའི་དོན་བསྟན་ཕྱིས་ནི་དྲང་བའི་དོན་བསྟན་ཡང་སྤྱིར་ནི༌[^2673]རྣམ་པ་གཉིས་ཏེ། དབང་པོ་སྨིན་པའི་དུས་དང་། ཐེག་པ་གཅིག་ཏུ་བཤད་པའོ། །

[Block 3158]
དབང་པོ་སྨིན་པ་ཡང་མྱ་ངན་ལས་འདའ་བའི༌[^2674]དུས་སུ་བསྟན་པ་དང་། ཉོན་མོངས་པ་ཟད་ཅིང་རྣམ་པར་བྱང་བ་བསྟན་པ་དང་། ཐེག་པ་རྣམ་པ་གསུམ་ཉོན་མོངས་པ་ལས་འབྱུང་བར་བསྟན་པ་དང་སྟོང་པ་ཉིད་རྟོགས་པ་དང་། ཏིང་ངེ་འཛིན་ལ་མཉམ་པར་འཇོག་པ་སྟེ། ཏིང་ངེ་འཛིན་ནི་བསམ་གཏན་བཞི་དང་། དགུ་ལས་ལྡང་བ་དང་། འཇུག་པ་བསྟན་ཏོ། །

[Block 3159]
མདོ་ལས་དགེ་སློང་རྣམས་དེ་བཞིན་གཤེགས་པ་ཞེས་པ་ནས་གསུམ་དུ་ལྟ་སྨོས༌[^2675]པའི་བར་དུ་ནི་ཐེག་པ་གཅིག་པོའི་དོན་བསྟན་ཏེ། དགོངས་པ་ངེས་པར་འགྲེལ་པ་ལས་ནི་ཐེག་པ་རྣམ་བཞིར་བསྟན་པ་ནི་ངེས་པའི་དོན་ཏེ། ཐེག་པ་གཅིག་པུ་སྟོན་པ་ནི་བཀྲི་བའི་དོན་ཞེས་སྟོན་ཏེ། འདིས༌[^2676]ནི་བྱང་ཆུབ་ཀྱི་སེམས་ལས་ལོག་པ་རྣམས་ཟློག༌[^2677]པའི་དོན་དུ༌[^2678]སྟོན་པས་འདིར་ཐེག་པ་གཅིག་པུ༌[^2679]འདི་ངེས་པའི་དོན་དུ་སྟོན་ཏོ། །

[Block 3160 [HEADING]]
##### དྲང་བའི་དོན། ^4-7-9-2-0

[Block 3161]
མདོ་ལས་དགེ་སློང་རྣམས་འདི་ནི་ཞེས་པ་ནས་མྱ་ངན་ལས་འདའ་བ༌[^2680]འཆད་དོ་ཞེས་པའི་བར་དུ་ནི་འདིས་དྲང་བའི༌[^2681]དོན་གྱི་གཏན་ཚིགས་བསྟན་ཏེ། སེམས་ཅན་དད་པ་མི་མཐུན་པ་རྣམས་སོ་སོའི་ཡིད་དང་མཐུན་པར་ཐབས་ཀྱི་ཆོས་སྟོན༌[^2682]ཏེ། སེམས་ཅན་དབང་པོ་ཞན་པ་འདོད་པ་རྣམ་ལྔ་ལས་ཟློག༌[^2683]པའི་དོན་ཙམ་དུ་འཁོར་བ་ལས་ཟློག་པ༌[^2684]བསྟན། དེ་ལས་བཟླ་བའི་ཕྱིར་ཐེག་པ་གཅིག་པོ་རིན་པོ་ཆེའི་འབྱུང་གནས་སུ་འཛུད༌[^2685]དོ། །

[Block 3162 [HEADING]]
#### དཔེ། ^4-7-10-0

[Block 3163 [HEADING]]
##### དྲང་བའི་དོན་གྱི་དཔེ། ^4-7-10-1-0

[Block 3164]
མདོ་ལས་འདི་ལྟ་སྟེ་དགེ་སློང་རྣམས་དཔེ་ལས་ཞེས་པ་ནས་ལྷག་པར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་དཔེ་འདིས་ནི་སྔར་དྲང་བའི་དོན་གྱི་དཔེ་བསྟན། ཕྱིས་ནི་ངེས་པའི་དོན་གྱི་དཔེ་སྟོན་ཏེ། དེ་དྲང་བའི་དོན་ལ་ཡང་དཔེ་རྣམ་པ་བཞི་སྟེ། མྱ་ངན་དགོན་པ་ལས་བསྒྲལ་བའི་དཔེ་དང་། འཁོར་རྣམས་སེམས་ནུར་བའི་དཔེ་དང་། ཚོང་དཔོན་ཐབས་མང་པོ་སྟོན་པའི་དཔེ་དང་། གླིང་དུ་ལྟ་བ་སྟོན་པའི་དཔེ་དང་།[^2686] འདི་ནི་དང་པོའོ། །

[Block 3165 [HEADING]]
###### མྱ་ངན་དགོན་པ་ལས་བསྒྲལ་བའི་དཔེ། ^4-7-10-1-1-0

[Block 3166]
དཔག་ཚད་ལྔ་བརྒྱ་ཞེས་པ་ནི་འགྲོ་བ་རྣམ་ལྔར་འཁོར་བའོ། །

[Block 3167]
རིན་པོ་ཆེའི་གླིང་ཞེས་པ་ནི༌[^2687]མྱ་ངན་ལས་འདས་པའི་གླིང་ངོ་། །མདོ་ལས་དེ་དག་ལས༌[^2688]མྱ་ངན་ལས་འདས་པའི༌[^2689]མཚན་མ་གཅིག་པོ་ཞེས་པ་ནས་དེ་དག་སྒྲོལ་ལོ་ཞེས་པའི་བར་དུ། མཚན་མ་ཞེས་པ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་ཏེ།[^2690] དེའི་ཡོན་ཏན་ཡང་ལྔའོ། །

[Block 3168]
གསལ་བ་ཞེས་པ་ནི་དབང་པོ་རྣོ་བའོ། །

[Block 3169]
མཁས་པ་ཞེས་པ་ནི་དགེ་ངན་འབྱེད་པའོ། །

[Block 3170]
རིག་པ་ཞེས་པ་ནི་དོན་དམ་པ་དང་ཀུན་རྫོབ་རིག་པའོ། །

[Block 3171]
དགེ་བ་ཞེས་པ་ནི་ཡོན་ཏན་ཐམས་ཅད་དང་ལྡན་པའོ། །

[Block 3172]
ལམ་ལ་སྒྲོལ་བ་ནི་འགྲོ་བ་རྣམ་ལྔ་ལས་སྒྲོལ་བའོ། །

[Block 3173 [HEADING]]
###### ལྡོག་པའི་དཔེ། ^4-7-10-1-2-0

[Block 3174]
མདོ་ལས་དེ་དག་འགྲོ་བ་མང་པོ་ཞེས་པ་ནས་སླར་ལྡོག་གོ་ཞེས་པའི་བར་དུ་ནི་འདིས་ལྡོག་པའི་དཔེ་བསྟན་ཏེ། ཐེག་པ་ཆེན་པོའི་སྒྲུབ་པ་བསྐལ་པ་དྲུག་ཅུའི་བར་དུ་དཀའ་བ་སྤྱོད་པ་བྱང་ཆུབ་སེམས་དཔའ༌[^2691]སྤྱོད་པས་དུབ་པ་དང་། འཕགས་པའི་སྤྱོད་པས་སྐྲག་ཅིང་འབྲས་བུ་ཆུང་ངུ་ལ་གཞོལ་བར་སེམས་པའོ། །

[Block 3175 [HEADING]]
###### སྤྲུལ་པའི་གྲོང་ཁྱེར་བསྟན་པའི་དཔེ། ^4-7-10-1-3-0

[Block 3176]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཞེས་པ་ནས་གྲོང་ཁྱེར་མངོན་པར་སྤྲུལ་ཞེས་པའི་བར་དུ་ནི་སྤྲུལ་པའི་གྲོང་ཁྱེར་བསྟན་པའི་དཔེ་སྟེ། དེ་ལ་ཡང་སེམས་སུ་གཞུག་པ་དང་། གྲོང་ཁྱེར་བསྟན་པ་དང་། དེར་འཇོག་པ་དང་། གྲོང་ཁྱེར་དེའི་ཡོན་ཏན་བསྟན་པ་དང་བཞི་སྟེ། འདི་ནི་དང་པོའི་གཉིས་པ་དང་སྦྱར་རོ། །

[Block 3177]
ཐེག་པ་ཆེན་པོ་བསྡུས་པ༌[^2692]ལས་ཀྱང་ཇི་ལྟར་ལྷའི་རྔ་ཆེད་དུ་བསམས་པ༌[^2693]མེད་པ་འབད་པ་མེད་པར་སྒྲ་འབྱུང་བ་བཞིན་དེ་བཞིན་གཤེགས་པའི་ཐུགས་རྗེས་སེམས་ཅན་རྣམས་ལ་ཉིན་ལན་གསུམ་མཚན་ལན་གསུམ་གཟིགས་པ་ཡང་ལྷུན་གྱིས་གྲུབ་པའི་དབང་གིས་དགོངས་ཞེས་པའི་དོན་ཏོ། །

[Block 3178]
དཔག་ཚད་བརྒྱ་འམ་ཉིས་བརྒྱ་ཞེས་པ་ནི་འཁོར་བའི་གནས་དང་སྡུག་བསྔལ་གྱི་ས་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 3179]
གྲོང་ཁྱེར་ཞེས་པ་ནི་བསམ་གཏན་དང་ཏིང་ངེ་འཛིན་གྱི་གྲོང་ཁྱེར་ཏེ། ཐེག་པ་ཆེན་པོའི་མྱ་ངན་ལས་འདས་པ་ཉིད་དང་སྦྱར་རོ། །

[Block 3180]
མདོ་ལས་དེས་སྐྱེས་བུ་དེ་དག་ལ་ཞེས་པ་ནས་རིན་པོ་ཆེའི་གླིང་དེར་དོང་ངོ་ཞེས་པའི་བར་དུ་ནི་དེར་གནས་པ་དང་། འཇིགས་པ་མེད་པ༌[^2694]དང་། གྲོང་ཁྱེར་དེར་ཞུགས་པའི་ཡོན་ཏན་བསྟན་ཏོ། །

[Block 3181]
དེར་འཇུག་པའི་ཡོན་ཏན་ཡང་བདེ་བ་ཐོབ་པ་དང་། སྡུག་བསྔལ་ཞི་བར་གྱུར་པའོ། །

[Block 3182 [HEADING]]
###### དུབ་པ་རྣམས་བསྟི་བའི་དཔེ། ^4-7-10-1-4-0

[Block 3183]
མདོ་ལས་དེ་ནས་དགེ་སློང་རྣམས་ཞེས་པ་ནས་བསིལ་བར་འདུ་ཤེས་སོ་ཞེས་པའི་བར་དུ་ནི་དུབ་པ་རྣམས་བསྟི་བའི་དཔེ་བསྟན་པ་སྟེ། དེ་ལ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 3184]
སྔར་སློབ་པ་རྣམས་སེམས་བསྡུ་ཞིང་བརྩོན་པ་བསྐྱེད་པ་དང་། ཕྱིས་མི་སློབ་པ་རྣམས་རྣམ་པར་གྲོལ་བའི་ལམ་ལ་གཟུད་ཅིང་ལྷག་མ་དང་བཅས་པའི་མྱ་ངན་ལས་འདས་པར་འགྱུར་བའི་འཆི་འཕོ་ལས་མ་བྲལ་བའི་ཕྱིར་གྲོང་ཁྱེར་དུ༌[^2695]ཞུགས་པའི་བསམ་པ་བསྐྱེད་པ་དང་། མི་སློབ་པའི་ས་ཐོབ་པ་འགོག་པ༌[^2696]དང་། ལམ་གྱི་མཐར་ཕྱིན་པ་དག་ཀྱང་རྒལ་བ་དང་བསིལ་བའི་འདུ་ཤེས་བསྐྱེད་པའོ། །

[Block 3185 [HEADING]]
##### ངེས་པའི་དོན་གྱི་དཔེ། ^4-7-10-2-0

[Block 3186]
མདོ་ལས་མཚན་མས༌[^2697]ངལ་སོས་པར་ཤེས་ནས་ཞེས་པ་ནས་ཁྱེད་འདོང་ངོ་ཞེས་པའི་བར་དུ་ནི། དཔེ་རྣམ་པ་གཉིས་ལ་འདི་ནི་ངེས་པའི་དོན་བསྟན་ཏེ། སྔར་ནི་སྤྲུལ་པ་བསྟན། ཕྱིས་ནི་ཡང་དག་པ་བསྟན་ཏེ། སྤྲུལ་པའི་གྲོང་ཁྱེར་ཞེས་པ་ནི་ཐེག་པ་རྣམ་པ༌[^2698]གཉིས་ཀྱི་གནས་ཏེ༌[^2699]བསྟི་བའི་གནས་དེ་བསྟི་བའི༌[^2700]གནས་དང་འདྲ་བར་བསྟན་པ༌[^2701]ཡིན་གྱི། ཐེག་པ་ཆེན་པོ་རིན་པོ་ཆེའི་འབྱུང་གནས་དེ་ནས་ཉེ་ཞེས་པར་དཔེ་སྨྲས་པ་ཡིན་ནོ། །

[Block 3187 [HEADING]]
##### དཔེ་དང་དོན་དུ་སྦྱར་བ། ^4-7-10-3-0

[Block 3188]
མདོ་ལས་དེ་བཞིན་དུ་དགེ་སློང་རྣམས་ཞེས་པ་ནས་སྤང་བར་བྱའོ་ཞེས་པའི་བར་དུ་ནི་དོན་ཕྱི་མ་དེང༌[^2702]སྦྱར་བ་སྟེ། སྔར་ནི་དྲང་བ་དང་སྦྱར་ཕྱིས་ནི་ངེས་པ་དང་སྦྱར་ཏེ། འཁོར་བ་དང་སྡུག་བསྔལ་ལས་རྒལ་བ༌[^2703]དང་སྤངས་པའོ། །

[Block 3189]
མདོ་ལས་དེ་ནས་སེམས་ཅན་འདི་དག་ཅེས་པ་ནས་མི་རུང་གི་ཞེས་པའི་བར་དུ་ནི་འདིས་ནི་བྱང་ཆུབ་སེམས་དཔའི༌[^2704]སྤྱོད་པ་དཀའ་བ་ལ་སེམས་ཞུམ་པ་བསྟན་པའོ། །

[Block 3190]
མདོ་ལས་དེ་བཞིན་གཤེགས་པས་ཞེས་པ་ནས་ས་གཉིས་བསྟན་ཏོ་ཞེས་པའི་བར་དུ་ནི་དཔེ་དང་དོན་དུ་སྦྱར་བ་སྟེ། ས་གཉིས་ཞེས་པ་ནི་དབང་པོ་གཉིས་ཀྱིས་བསླབ་པར་བྱ་བ་དང་། ཡེ་ཤེས་གཉིས་པས་ཆུད་པར་བྱ་བའི་སའོ། །
--- END BLOCKS ---
