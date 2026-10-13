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
[Block 281]
ཅིག་ཅར་བ་ཡིན་ན་ཡང་དབང་པོས༌[^218]ཤེས་པ་དང་། དེ་ཉམས་སུ་མྱོང་བར་བྱེད་པའི་ཡིད་གཉིས་ཀ་བསལ་བར༌[^219]ཁས་བླངས་པར་འགྱུར་རོ། །

[Block 282]
དེ་ལྟ་ན་ནི་ཡུལ་གྱི་རྒྱུ་མཚན་ཡུལ་ཅན་ལ་ཡང༌[^220]ཡོད་པར་འགྱུར་རོ། །

[Block 283]
དེ་ནི་ཚད་མའི་དབང་པོ་ཉམས་སུ་མྱོང་བའི་ཡིད་དེ་ནི་ཚད་མར་མ་བརྗོད་དེ༌[^221]དེས༌[^222]ནི་དེའི་གནས་སྐབས་ལ་ཞུགས་པ་པོ་ཡང་ཚད་མར་མ་བརྗོད་པའི་ཕྱིར་མྱངས་པར༌[^223]འགྱུར་རོ། །

[Block 284]
རང་རིག་ཏུ་འདོད་པ་ལ་སོགས་པ་ལ་ནི༌[^224]ཉེས་པ་མེད་དོ།[^225] །

[Block 285]
དྲན་པ་ཞེས་བྱ་བ་ནི་ལོང་བའི་གོམ་པ་ཉིད་དེ། དེ་ཡོད་པ་ལྟ༌[^226]ན་ནི་དྲན་པ་འདི་མངོན་སུམ་འཛིན་པའི་བྱེ་བྲག་གོ་ཞེས་བྱ་བར་འགྱུར་རོ། །

[Block 286]
དེ་ལྟ་ན་ཡང་བར་མཆོད་པའི་དབང་པོའི་ཡུལ་འཛིན་ན་ནི་དྲན་པར་མི་འགྱུར་ཏེ། ཡིད་ཀྱིས་ཉམས་སུ་མ༌[^227]མྱོང་བའི་ཕྱིར་རོ། །

[Block 287]
སྔར་ཡིད་ཀྱིས་ཕྱི་རོལ་གྱི་དོན་ཉམས་སུ་མྱོང་བ་ནི༌[^228]མེད་དོ། །

[Block 288]
དྲན་པ་ཉམས་པའམ། དྲན་པ་ཡིན་ནའང་གཞན་མཐོང་འགྱུར། །དབང་པོའི་འཇུག་པ་ཙམ་ཞིག་མྱོང་བའི་ཕྱིར་ཉམས་སུ་མ༌[^229]མྱོང་བའམ། དྲན་པ་ཉམས་པ༌[^230]ཞེས་བྱ་བའི་འམ་ཞེས་པའི་སྒྲ་རྣམས་རྣམ་པར་བརྟག་པའི་དོན་ཏོ། །

[Block 289]
ཇི་ལྟར་ཉམས་པར་འགྱུར་ཏེ། ཕྱི་རོལ་གྱི་དོན་ལ་དབང༌[^231]པོའི་འཇུག་པ་དང་ལྷན་ཅིག་ཏུ་སྐྱེས་པ་ཡིད་ཀྱིས་ཉམས་སུ་མྱོང་བ་འདོད་པ་ཡིན་ནོ་ཞེ་ན། གང་ཇི་སྐད་དུ་དོན་གཅིག་གིས་དབང་པོ་གཉིས་བསྐྱེད་པའི་ནུས་པ་ནི་བརྟག་པར་མི་ནུས་སོ་ཞེས་བརྗོད་པའི་ཕྱིར་དེ་ནི་ཉམས་པ་ཉིད་དོ། །

[Block 290]
ཉེས་པ་དེ་དག་ནི་ཡོད་པ་མ་ཡིན་ནོ།[^232] །

[Block 291]
དྲན་པའི་ཡིད་རྟག༌[^233]ཏུ་འཛིན་པར་བསྟན་པའི་ཆེད་དུ་ལྷན་ཅིག་ཁོ་ནར་སྐྱེ་བ་བཀག་པ་ཡིན་ནོ།[^234] །

[Block 292]
ལྷན་ཅིག་པར་གྲུབ་པ་ཉིད་ལ་ཅི་ཕྱི་རོལ་གྱི་དོན་ལ་དབང་པོ་དང་ཡིད་དག་གིས་ལྷན་ཅིག་ཏུ་འཛིན་པར༌[^235]བྱེད་དམ་ཞེས་འཛིན་ལུགས་ལ་བརྒལ་ཏེ། གང་གི་ཚེ་ལ་ལར་དུས་གཅིག་ཏུ་དབང་དང་ལྡན་པའི་ཡིད་འབྱུང་ངོ་ཞེས་སྔར་བརྗོད་པའི་ཕྱིར་རོ་ཞེ་ན། དེ་ལྟ་ན་ཡང་། དྲན་པ་ལྷག་པར་བརྗོད་ཕྱིར་ན། །རྣམ་བསལ། གལ་ཏེ་དྲན་པ་ལྷག་པར་བརྗོད་པར་བྱ་བའི་ཕྱིར་ཕྱི་རོལ་གྱི་དོན་ལ་ཡིད་དང་ལྷན་ཅིག་བཀག་པ་ཡིན་ན་ནི་དེ་ལྟ་ན་ཡང་གང་ཇི་སྐད་དུ་འདི་ལྟར་དབང་པོས་གཟུང་གི། རྗེས་ལ་ཡིད་ཀྱིས་འཛིན་པར་བྱེད་དེ། དེ་ལྟར་ཡིད་ཀྱིས་བཟུང༌[^236]ནས་དབང་པོ་ཇི་ལྟ་བ་བཞིན་དུ་རིག་པར་བྱེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྗོད་པ་དེ་རྣམ་པར་བསལ་བ༌[^237]ཡིན་ནོ། །

[Block 293]
དེའི་ཕྱིར་ཕྱི་རོལ་གྱི་དོན་ལ་དྲན་པ་ནི༌[^238]ཡོད་པ་མ་ཡིན་ནོ། །

[Block 294]
གལ་ཏེ་ཡིད་ཕྱི་རོལ་གྱི་དོན་ལ་དངོས་སུ་འཇུག་པ་དེ་ལྟ༌[^239]ན་ཡང་། དབང་གཞན་དོན་མེད༌[^240]འགྱུར། དབང་པོ་གཞན་རྣམས་ཕྱི་རོལ་གྱི་དོན་ལ་འཇུག་པ་དོན་མེད་པར་འགྱུར་ཏེ། སྐྱེས་བུའི་དོན་ཡིད་ཀྱིས་སྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 295]
དེའི་ཕྱིར་དེ་ལྟར་ཡུལ་གྱི་རང་བཞིན་ངེས་པར་གཟུང་བར་མི་ནུས་པའི་ཕྱིར་གྲངས་ཅན་གྱི་མངོན་སུམ་ཚད་མ་མ་ཡིན་ནོ། །

[Block 296 [HEADING]]
#### དཔྱོད་པ་རྣམས་ཀྱི་མངོན་སུམ། ^1-4-5-0

[Block 297 [HEADING]]
##### ཡོད་པ་དང་ཡང་དག་པར་ཕྲད་ནས་སྐྱེས་པ། ^1-4-5-1-0

[Block 298]
དཔྱོད་པ་རྣམས་ནི་ཡོད་པ་དང་ཡང་དག་པར་ཕྲད་ནས་སྐྱེས་པའི་སྐྱེས་བུའི་དབང་པོ་རྣམས་ཀྱི་བློ་དེ་མངོན་སུམ་མོ་ཞེས་ཟེར་རོ། །

[Block 299]
དེ་ལ།

[Block 300]
ཡོད་པའི་གསལ་བྱ་མེད་པ་སྟེ། །ཕྲད་ཅེས་པ་ལས་དེ་རིག་བྱ། །

[Block 301]
ཡང་དག་པར་ཕྲད་པ་ནི་ཡོད་པ་ཁོ་ན་དང་ཡིན་པར་ངེས་པའི་ཕྱིར་མེད་པ་བསལ༌[^241]བར་བྱ་བའི་དོན་དུ་ཡོད་པ་སྨོས་པ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 302]
ལན་དུ་ཕྲད་པ་བསྟན་ཞེ་ན། ཅི་སྟེ་ཡང་། དབང་པོ་རྣམས་ཀྱིས་ནི་ཡང་དག་པར་ཕྲད་ནས་སོ་ཞེས་བརྗོད་པར་བྱ་བ་ལ་གང་གིས་སྦྱོར༌[^242]ཞིང་ཡང་དག་པར་ཕྲད་པར་བྱེད་ཅེས་དོགས་ན།[^243] ལན་དུ་ཕྲད་པར་གཟུང་བར་བྱས་པ་སྟེ། དེའི་དོན་དུ་ཡོད་པ་སྨོས་སོ་ཞེ་ན། དེ་ལྟ་ན་ནི་དབང་པོའི་ཁྱད་པར་དུ་བརྗོད་ཀྱིས། དབང་པོ་ཁྱད་པར་ཅན་དུ་བྱ་བའི་དོན༌[^244]དུ་སོ་སོར་སྦྱར་བ༌[^245]བརྗོད་པར་རིགས་སོ། །

[Block 303]
ཅི་སྟེ་ཡང་འདིར་བདག་ལ་སོགས་པ་དང་ཡིད་ལ་སོགས་པ་དང་ཡང་སྦྱོར་ཞིང་ཕྲད་པ་བརྗོད་པར་བྱ་སྟེ། དེ་སྤྱིའི༌[^246]སྒྲས་བརྗོད་པ་ཡིན་ནོ་ཞེ་ན།

[Block 304 [VERSE]]
དེ་ཡང་རིགས་པ་མ་ཡིན་ནོ།[^247] །
ཡོད་པ་ཙམ་དང་ཕྲད་པ་རུང་། །
མ་ཡིན་མིན་ཏེ་གང་གིས༌[^248]བརྗོད། །

[Block 305]
སྐྱེས་བུ་ལ་སོགས་པ་སྤྱིར་ཡོད་པ་ཙམ་དང་ཕྲད་པ་ཉིད་ནི་གྲུབ་པ་ཁོ་ན་སྟེ། དེའི་ཕྱིར་མེད་པ༌[^249]ལ་ནི་མི་འཇུག་སྟེ། གང་ཡང་སྨིག་རྒྱུ་ལ་སོགས་པ་ཡོད་པ་མ་ཡིན་པ་མངོན་སུམ་ལྟར་སྣང་བ་དེ་དང་ཡང་འགའ་ཞིག་ཏུ་ཕྲད་པར་འགྱུར་རོ།[^250] །

[Block 306]
ཡུལ་ཁྱད་པར་ཅན་དང་ཉི་མའི་གདུང་བ་དང་། འབྱུང་བའི་བྱེ་བྲག་རྣམས་ནི་ཡོད་པ་ཙམ་ཁོ་ན་སྟེ།

[Block 307]
དེ་མིག་གི་བློ་དང་ཕྲད་ནས་དོན་མེད་པའི་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་རྒྱུ་བ༌[^251]ལས།

[Block 308]
རིམ་གྱིས་འཁྲུལ་པའི་ཤེས་པ་འབྱུང་སྟེ། དེའི་ཕྱིར་དེ་དག༌[^252]དགག་པར་ཡོད་པ་སྨོས་པ་རིགས་པ་མ་ཡིན་ནོ། །

[Block 309]
ཅི་སྟེ་ཡོད་སྒྲ་དམ་པར་འདོད། །དབང་པོ་མཛེས་པར་བརྗོད་པ་ཡིན། །

[Block 310]
གང་ཡང་འདི་ལྟར་བརྟག་པར་བྱ་སྟེ། གང་དུ་དབང་པོ་གང་ཞིག་དམ་པར་གྲུབ་པ་དེ་ནི་གཞན་ལ་མི་འཇུག་སྟེ། དེས་ན་དེ་དང་ཡང་དག་པར་ཕྲད་པའམ། ཡང་ན་གང་དབང་པོ་རབ་ཏུ་མཛེས་པ་དང་ཕྲད་ནས་བརྗོད་པའོ་ཞེ་ན།

[Block 311]
དམ་པར་གྲུབ་དང་མཛེས་པ་སྟེ།[^253] །མིག་སྨན་ལ་སོགས་བཞིན༌[^254]ལས་ཀྱང་། །

[Block 312]
དེ་གྲུབ་ཅེས་བྱ་བ་ནི་ཚིག་ཁ་བསྐང་བའི་དོན་དུའོ། །

[Block 313]
རྡུལ་སོགས་པ་གཞན་གྱིས་ཀྱང་དབང་པོ་དམ་པར་སྒྲུབ༌[^255]པར་བྱེད་པ་སྟེ་དོན་ཙམ་འབའ་ཞིག་ལས་ནི་མ་ཡིན་ནོ། །

[Block 314]
དབང་པོའི་རབ་ཏུ་མཛེས་པ་ཡང་། མིག༌[^256]སྨན་དང་རྐང་པ་བྱུགས་པ༌[^257]ལ་སོགས་པ་ལས་ཀྱང་ཡིན་པས་དེ་དང་རབ་ཏུ་སྦྱར་བ་ཡང་མངོན་སུམ་དུ་འགྱུར་རོ། །

[Block 315]
གལ་ཏེ་དེ་དེ་ལྟར་ནི་མི་འགྱུར་ཏེ། དཔེར་ན་འགྲོ་བའི་སྒྲ་ལས་བ་ལང་མཚོན་གྱི་གཞན་ལ་འགྲོ་བའི་བྱ་བ་ཡོད་ཀྱང་མ་ཡིན་པ་དེ་བཞིན་དུ། དོན་ཁོ་ནས་དམ་པར་གྲུབ་ཅིང་མཚོན་པར་བྱེད་ཀྱི་གཞན་ལས་ནི་མ་ཡིན་ནོ། །

[Block 316]
དེ་བཞིན་དུ་རབ་ཏུ་མཛེས་པ་ལ་ཡང་བརྗོད་པར་བྱའོ་ཞེ་ན། བརྒལ་བ་འདི་ནི་མི་བཟད་པ་སྟེ།

[Block 317]
གྲགས༌[^258]ལས་དེ་ལྟར་བརྟགས་གྲངས༌[^259]ན། །སྒྲ་དེ་དབང་པོའི་ཡུལ་ལ་མིན། །

[Block 318]
འགྲོ་བའི་སྒྲ་ནི་བ་ལང་ཁོ་ན་ལ་གྲག་པས༌[^260]འགྲོ་བའི་སྒྲ་ལ༌[^261]མཚོན་པ་སྟེ། དེ་བཞིན་དུ་དམ་པ་དང་རབ་ཏུ་མཛེས་པར་བྱ་བའི་ཕྱིར་ཡོད་པའི་སྒྲས༌[^262]དབང་པོ་ལ་གནས་པ༌[^263]ནི་མ་ཡིན་ནོ། །

[Block 319]
དེའི་ཕྱིར་ཡོད་པའི་སྒྲ་ལས་དེ་ལྟར་བརྟགས་པ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 320 [VERSE]]
ཀུན་ཏུ་དོན་དང་ཕྲད་གང༌[^264]ན། །
གཟུགས་སྒྲ་བར་དུ་ཆོད་པ་དང་། །
ཆེན་པོའང་འཛིན་པར་མཐོང་བས་ན། །
བར་དུ་མ་ཆོད་པ་ལ་གནོད། །
--- END BLOCKS ---
