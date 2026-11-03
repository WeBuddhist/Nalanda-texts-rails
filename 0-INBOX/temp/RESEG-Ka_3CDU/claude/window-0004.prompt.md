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
[Block 141 [VERSE]]
ཉ་ཕྱིས་ལ་སོགས་ཆུ་བརྟགས་ཏེ། །
སྟེང་དང་བར་གཏིང་རིམ་བཞིན་ནོ། །
ཉ་ཕྱིས་ལ་སོགས་མེད་ན་ཡང་། །
ཁྱོར་བའམ་འདབ་མས་བུམ་པ་དགང་། །

[Block 142 [VERSE]]
ཆུ་ཡི་སྐྱེ་བོ་ཆེ་ཆུང་རྣམས། །
ཡུན་མི་རིང་བར་ནན་ཏན་བརྟག །
སྙིང་རྗེ་ཅན་གྱིས༌[^69]ཁུ་བ་རྣམས། །
རབ་ཏུ་བརྟགས་ཏེ་སྤྱད་པར་བྱ། །

[Block 143 [VERSE]]
སྲོག་ཆགས་ཡོད་ན་ལེགས་པར་བཙག །
སྲོག་ཆགས་རྣམས་ལ་གནོད་མི་བྱ། །
རྩྭ༌[^70]དང་ལྕི་བ་ཤིང་ལ་སོགས། །
དགོས་པ་གང་དང་གང་ཡང་རུང་། །

[Block 144]
དེ་དག་སྲོག་ཆགས་མེད་པར་བྱ། །སྡོམ་པས་སྲོག་ཆགས་གསད་པ༌[^71]སྲུང་།[^72] ། ཞེས་བྱ་བས་ཆུ་ལ་སོགས་པ་བརྟག་པར་བསྟན་ཏེ། དེ་དག༌[^73]དཀྱིལ་འཁོར་བྱས་ནས་གཡར་ཚུས་ཐོབ་པའི་འོག་ཏུ་ཅི་བྱ་ཞེ་ན། དེའི་ཕྱིར། ཉ་ཕྱིས་ལ་སོགས་ཆུ་བརྟགས་ཏེ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དེའི་འོག་ཏུ་ཆུ་ཚགས་ལྔ་འདུལ་བ་ལས་གསུངས་པའི་ཆུ་ཚགས་གང་ཡང་རུང་བ་ཅིག་གིས་ཆུ་བཙག་གོ། །

[Block 145]
དེ་ལ་ཆུ་ཚགས་ལྔ་ནི་རིལ་བ་དང་། གྲུ་གསུམ་པ་དང་། ཡུ་བ་ཅན་དང་། ཆོས་ཅན་ཞེས་བྱ་བ་དང་། གྲོལ་བར་བྱེད་པའི་རས་སོ། །

[Block 146]
དེ་ལྟར་ཆུ་བཙགས་ནས་བཙགས་པ༌[^74]ཙམ་གྱིས་ཀྱང་མི་ཆོག་སྟེ། ཉ་ཕྱིས་ལ་སོགས་པ་ཆུས་གང་བར་བཀང་ལ་སྲོག་ཆགས་ཡོད་དམ་མེད་བརྟག་གོ། །

[Block 147]
སོགས་པའི༌[^75]སྒྲས་ནི་དུང་ཕོར་རྣམས་ཀྱང་བསྡུས་སོ། །

[Block 148]
ཇི་ལྟར་བརྟག་ཅེ་ན། དེའི་ཕྱིར། སྟེང་དང་བར་གཏིང་རིམ་བཞིན་ནོ། །ཞེས་བྱ་བ་སྨོས་ཏེ། བརྟག་པའི་རིམ་པ་ནི་ཐོག་མར་ཆུའི་སྟེང་ན་སྲོག་ཆགས་ཡོད་དམ་མེད་བརྟག་གོ། །

[Block 149]
དེ་ནས་བར་དུ། དེ་ནས་གཏིང༌[^76]སྟེ་ཞབས་སུ་བརྟགས་ལ། སྲོག་ཆགས་མེད་ན་ནི་ཆུ་དེ་སྤྱད་དུ་རུང་ངོ་། །སྲོག་ཆགས་ཡོད་ན་ནི་ཆུ་དེ་སྤྱད་དུ་མི་རུང་བས་སླར་སྔ་མའི་གནས་སུ་དབོའོ། །

[Block 150]
གལ་ཏེ་ཉ་ཕྱིས་དང་དུང་ཕོར་མ་འབྱོར་ན་ཇི་ལྟར་བྱ་སྙམ་པ་ལ། དེའི་ཕྱིར། ཉ་ཕྱིས་ལ་སོགས་མེད་ན་ཡང་། །ཁྱོར་བའམ་འདབ་མས་བུམ་པ་དགང་།[^77] །ཞེས་བྱ་བ་སྨོས་ཏེ། ཉ་ཕྱིས་དང་དུང་ཕོར་མ་འབྱོར་ན་ཡང་ཁྱོར་བ༌[^78]བཀང་སྟེ་བརྟག་གོ། །

[Block 151]
འདིར་ཡང་སྟེང་དང་བར་གཏིང་རིམ་བཞིན་དུ་བརྟག་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 152]
འདིའི་སྐབས་སུ༌[^79]ཇི་ལྟར་བརྟག་ཅེ་ན། དེའི་ཕྱིར།

[Block 153 [VERSE]]
ཆུ་ཡི་སྐྱེ་བོ་ཆེ་ཆུང་རྣམས། །
ཡུན་མི་རིང་བར་ནན་ཏན་བརྟག །

[Block 154]
ཅེས་བྱ་བ་སྨོས་ཏེ། ཆུ་བརྟག་པ་ཡང་མིག་ནད་ཀྱིས་ཕོག་པའམ། མིག་ལིང་ཏོག༌[^80]གིས་ཁེབས་པས་ནི་མི་བརྟག་གི་མིག་གསལ་བས་ཆུ་ན་གནས་པའི་སྲོག་ཆགས་ཕྲ་མོ་དང་སྦོམ་པོ་རྣམས་ཡོད་དམ་མེད་བརྟག་གོ། །

[Block 155]
མིག་གསལ་བས་བརྟགས་ན་ཡང་ཡུན་རིང་དུ་མིག་བགྲད༌[^81]དེ་བལྟས་ན་མིག་ཟི་ཟི་པོར་འགྱུར་བས༌[^82]སྲོག་ཆགས་མི་མཐོང་བའི་ཕྱིར་ཡུན་མི་རིང་བར་ཡང་ནས་ཡང་དུ་མིག་གསལ་བས་བརྟག་སྟེ། སྲོག་ཆགས་མེད་པར་ཡིད་ཆེས་ཀྱི་བར་དུ་བརྟག་གོ། །

[Block 156]
དེ་བས་ན་ནན་ཏན་བརྟག་ཅེས་སྨོས་ཏེ། སྲོག་ཆགས་མེད་པར་ཡིད་ཆེས་ཤིང་ཐེ་ཚོམ་མེད་ཀྱི་བར་དུ་བལྟའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅིའི་ཕྱིར་དེ་ལྟར་བརྟག་ཅེ་ན། དེའི་ཕྱིར་སྙིང་རྗེ་ཅན་གྱིས་ཞེས་བྱ་བ་སྨོས་ཏེ། རབ་ཏུ་བྱུང་བ་རྣམས་ནི་སེམས་ཅན་གྱི་སྡུག་བསྔལ་སེལ་བར་བྱེད་པའི་སྙིང་རྗེ་དང་ལྡན་པ་ཡིན་པས། དེའི་ཕྱིར་སེམས་ཅན་གྱི་གནོད་པ་བསལ་བའི་དོན་དུ་སྲོག་ཆགས་ཡོད་དམ་མེད་བརྟག་གོ། །

[Block 157]
གལ་ཏེ་ཆུ་ལས་སྐྱེས་པའི་སྲོག་ཆགས་ནི་མེད་ཀྱི་སྦྲང་བུ་ལ་སོགས་པ་གློ་བུར༌[^83]དུ་འོངས་པས་ཆུ་དེ་སྲོག་ཆགས་དང་ལྡན་པར་གྱུར་པ་དང་། ཁ་ཟས་ཀྱི་ཁུ་བ་ལ་སོགས་པ་ལ་གློ་བུར༌[^84]གྱི་སྲོག་ཆགས་ཡོད་པར་གྱུར་ན་དེ་དག་དོར་བར་ཇི་ལྟར་བྱ་སྙམ་པ་ལ་ཁུ་བ་རྣམས་རབ་ཏུ་བརྟགས་ཏེ་སྤྱད་པར་བྱ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆུ་བཙགས་པ་དང་ཁ་ཟས་ཀྱི་ཁུ་བ་ལ་གློ་བུར་དུ་འོངས་པའི་སྲོག་ཆགས་ཡོད་པར་གྱུར་ན་ཡང་ཡོད་དམ་མེད་ལེགས་པར་བརྟགས་ཏེ་སྤྱད་པར༌[^85]བྱའོ། །

[Block 158]
དོར་བར་ནི་མི་བྱའོ། །

[Block 159]
ཐབས་ཇི་ལྟར་བྱ་ཞེ་ན། དེའི་ཕྱིར།

[Block 160 [VERSE]]
སྲོག་ཆགས་ཡོད་ན་ལེགས་པར་བཙག །
སྲོག་ཆགས་རྣམས་ལ་གནོད་མི་བྱ། །

[Block 161]
ཞེས་བྱ་བ་སྨོས་ཏེ། བཙགས་པ་དང་ཁ་ཟས་ཀྱི་ཁུ་བ་ལ་གློ་བུར་དུ་འོངས་པའི་སྲོག་ཆགས་ཡོད་ན་ལེགས་པར་མ་སྣད་པར་བཙགས་པར༌[^86]རིག་པ༌[^87]ནི་བཙག །ལག་པས་བསལ་བར་རིག་པ༌[^88]ནི་ལེགས་པར་བསལ་ལ་སོ་སོའི་གནས་སུ་མ་སྣད་མ་ཤི་བར་བསྐྱལ་བར་བྱའོ། །

[Block 162]
དེ་ལ་ཆུ་གྲང་མོ་ལ་གནས་པའི་སྲོག་ཆགས་རྣམས་ཆུ་དྲོན་མོ་ལ་བསྐྱལ་ན་གནོད་པར་འགྱུར་བས་ཆུ་གྲང་མོ་ཉིད་དུ་བསྐྱལ་ལོ། །

[Block 163]
ཆུ་དྲོན་མོ་ལ་གནས་པའི་སྲོག་ཆགས་རྣམས་ཆུ་གྲང་མོ་ལ་བསྐྱལ་ན་གནོད་པར་འགྱུར་བས༌[^89]ཆུ་དྲོན་མོ་ཉིད་དུ་བསྐྱལ་ལོ། །

[Block 164]
གལ་ཏེ་མ་བྱས་པར་སྲོག་ཆགས་དང་བཅས་པའི་ཆུ་འཐུངས་སམ། སྲོག་ཆགས་རྣམས་རང་རང་གི་གནས་མ་ཡིན་པར་བསྐྱལ་ཏེ། ཤི་བར་གྱུར་ན་སྲོག་ཆགས་ཀྱི་གྲངས་དུ་ཡོད་པའི་ཉེས་བྱས་ཀྱི་གྲངས་ཀྱང་དེ་སྙེད་ཅིག་འཐོབ་བོ། །

[Block 165]
ཆུ་བཙགས་ཏེ་བརྟགས་པ་དེ་ཡང་དེ་རིང་ལྟ་བུའི་ནང་པར་བརྟགས་ན། དེའི་ཕྱི༌[^90]དེ་ཉིད་ཀྱི་ནང་པར་གྱི་བར་དུ་སྤྱད་པར་བྱར་རུང་ངོ་། །ཆུ་རྣམ་པ་ལྔ་ནི་བདག་གིས་མ་བཙགས་མ་བརྟགས་ཀྱང་སྤྱད་དུ་རུང་བའི་ཆུ་སྟེ། ལྔ་གང་ཞེ་ན། ཁོ་ར་ཁོར་ཡུག་འདོམ་གང་དུ་བརྟགས་པའི་ཆུ་དང་། ཁྲོན་པ་ལ་སོགས་པ་དང་། དགེ་སློང་ཡོན་ཏན་ཅན་གྱི་ཆུ་དང་། དགེ་འདུན་གྱི་ཆུ་དང་། ཡིད་ཆེས་པའི་ཆུའོ། །

[Block 166]
དེ་ལ་ཁོ་ར་ཁོར་ཡུག་འདོམ་གང་དུ་བརྟགས་པའི་ཆུ་ནི་ལྟེང་ཀའམ་མཚེའུ་ལ་སོགས་པའི་དབུས་སུ་པུས་མོ་ནུབ་ཙམ་དུ་སོང་ལ་སྲོག་ཆགས་ཡོད་དམ་མེད་བརྟགས་ཏེ་མེད་པར་གྱུར་ན་འདོམ་གང་ཁོ་ར་ཁོར་ཡུག་ཏུ་བརྟགས་པ་ཡིན་པར་སྤྱད་དུ་རུང་ངོ་། །ཁྲོན་པ་ལ་སོགས་པའི་ཆུ་ནི་ཁྲོན་པ་དང་ལྟེང་ཀ་དང་རྫིང་ལ་སོགས་པར་ཉ་ཕྱིས་གང་གི་ཆུ་བླངས་ཏེ། སྲོག་ཆགས་ཡོད་དམ་མེད་བརྟགས་ཏེ་མེད་ན་ཉིན་ཞག་གཅིག་གི་བར་དུ་སྤྱད་དུ་རུང་ངོ་། །དགེ་སློང་ཡོན་ཏན་ཅན་གྱི་ཆུ་ནི་དགེ་སློང་ཚུལ་ཁྲིམས་ལ་གནས་པ་སྡིག་པ་ལ་འཛེམ་པས་ཆུ་བཙགས་ཏེ་བཙགས་པ་ལ་བདག་གིས་མ་བརྟགས་མ་བཙགས་པར་སྤྱད་དུ་རུང་ངོ་། །དགེ་འདུན་གྱི་ཆུ་ནི་དགེ་འདུན་སྤྱིའི་ཆུ་ལྟ་བུ་བརྟགས་ནས་བཙགས་ཏེ༌[^91]བཞག་པ་ལ་ནི་བདག་གིས་མ་བརྟགས་མ་བཙགས་ཀྱང་སྤྱད་དུ་རུང་ངོ་། །ཡིད་ཆེས་པའི་ཆུ་ནི་བྲག་ཁའམ། རི་ཁ་གཟར་པོ་ནས་འབབ་པའི་ཆུའམ། སའི་འོག་ནས་གྱེན་དུ་རྡོལ་པའི༌[^92]ཆུ་མིག་ལྟ་བུ་ལ་སྲོག་ཆགས་ཡོད་མི་སྲིད་པས་ཡིད་ཆེས་པའི་ཆུ་ཞེས་བྱ་སྟེ་སྤྱད་དུ་རུང་ངོ་། །ཆུ་བཙགས་པའི་བསླབ་ཚིག༌[^93]ནི་དགེ་སློང་མོས་པ་ཅན་གྱི་སྲོག་ཆགས་དང་བཅས་པའི་ཆུས་ཆག་ཆག་དང་དཀྱིལ་འཁོར་ལ་སོགས༌[^94]བྱས་པ་ལས་བཅས་སོ། །

[Block 167]
དེའི་ཕྱིས༌[^95]དགེ་སྦྱོང་གིས་ཆུ་ཚགས་ལྔ་ལས་གང་ཡང་རུང་བ་ཅིག་མེད་པར་གནས་སུ་མི་རུང་ངོ་། །མེད་པར་གནས་ན་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 168]
ཆུ་ལ་དེ་ལྟར་བརྟགས་ཤིང་བཙགས་ནས་སྲོག་ཆགས་མེད་པར་བྱས་ཏེ་སྤྱད་ན། འོ་ན་རྩྭ་དང་ཤིང་ལ་སོགས་པ་ལ་སྲོག་ཆགས་ཡོད་ན་ཇི་ལྟར་སྤྱད་སྙམ་པ་ལ། དེའི་ཕྱིར།

[Block 169 [VERSE]]
རྩ༌[^96]དང་ལྕི་བ་ཤིང་ལ་སོགས། །
དགོས་པ་གང་དང་གང་ཡང་རུང་། །
དེ་དག་སྲོག་ཆགས་མེད་པར་བྱ། །

[Block 170]
ཞེས་བྱ་བ་སྨོས་ཏེ། མལ་གྱི་འོག་ཏུ་གདིང་བའི་རྩ༌[^97]ལ་སོགས་པ་དང་། དཀྱིལ་འཁོར་དང་ཁང་པ་བཀྲུ་བའི་ལྕི་བ་དང་། མེ༌[^98]བུད་པའི་ཤིང་དང་། སོགས་པའི་སྒྲས་ནི་ས་ལ་སོགས་པའི་ཡང་བསྡུས་ཏེ། དགེ་སྦྱོང་གིས་སྤྱད་པར་བྱ་བའི༌[^99]རྫས་གང་ཅི་ཡང་རུང་སྟེ་ཀུན་ལ་སྲོག་ཆགས་ཡོད་དམ་མེད་བརྟགས་ནས་སྲོག་ཆགས་ཡོད་ན་བཙགས་ལ་སྲོག་ཆགས་རྣམས་ཀྱང་རང་རང་གི་གནས་སུ་བདེ་བར་བསྐྱལ་ཏེ། སྲོག་ཆགས་མེད་པར་བྱས་ནས་སྤྱད་པར་བྱའོ། །

[Block 171]
ཆུའི་སྐབས་སུ་བཤད་པ་རྣམས་ཀྱི་དོན་མདོར་བསྡུས་ཏེ་བསྟན་པའི་ཕྱིར། སྡོམ་པས་སྲོག་ཆགས་བསད་པ་བསྲུང་། །ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སྦྱོང་རྣམས་ནི་སྙིང་རྗེ་ཅན་ལ་ཁྲིམས་དང་ལྡན་པ་ཡིན༌[^100]པས་ཅི་ནས་ཀྱང་སེམས་ཅན་ཆེ་ཕྲ་ཀུན་གྱི་བསད་པ་བསྲུང་སྟེ། སེམས་ཅན་གང་ཡང་མི་བསད༌[^101]དོ། །ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 172 [HEADING]]
### མཁན་པོ་དང་སློབ་དཔོན་གྱི་ལས་སུ་བྱ་བ་བསྒྲུབ་པ། ^3-5-0

[Block 173 [VERSE]]
སྟན་ཆུ་ས་དང་སོ་ཤིང་དང་། །
འདག་པའི༌[^102]ཆལ་ཡང་སྟ་གོན་བྱ། །
ལྷུང་བཟེད་བཀྲུ་ལ་སོགས་པ་དང་། །
བླ་མའི་དགོས་པ་ཐམས་ཅད་བྱ། །

[Block 174]
ཞེས་བྱ་བས་མཁན་པོ་དང་སློབ་དཔོན་གྱི་ལས་སུ་བསྒྲུབ་པ་བསྟན་ཏེ། དེ་ལྟར་བརྟགས་པ་དང་བཙགས་པའི་འོག་ཏུ། བླ་མའི་དགོས་པ་ཐམས་ཅད་བྱ། །ཞེས་སྦྱར་ཏེ། བླ་མ་ནི་མཁན་པོ་དང་སློབ་དཔོན་ལ་བྱ་སྟེ། དེའི་དགོས་པ་ནི་མཁན་པོ་དང་སློབ་དཔོན་གྱི་ལས་སུ་བྱ་བ་རྣམས་ཉམས་སུ་བླང་སྟེ་བསྒྲུབ་བོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 175]
ཉམས་སུ་བླང་བ་དེ་དག་ཀྱང་གང་ཞེ་ན། དེ་བསྟན་པའི་ཕྱིར།

[Block 176 [VERSE]]
སྟན་ཆུ་ས་དང་སོ་ཤིང་དང་། །
འདག་པའི་ཆལ་ཡང་སྟ་གོན་བྱ། །

[Block 177]
ཞེས་བྱ་བ་སྨོས་ཏེ། མཁན་པོ་དང་སློབ་དཔོན་གྱི་ལས་སུ་བྱ་བ་ནི་ནང་པར་མཁན་པོ་དང་སློབ་དཔོན་གང་དུ་ཁ་གདོང་བཀྲུ་བའི་གནས་སུ་གདན་གདིང་བ་དང་། བཀྲུ་བའི་ཆུ་དང་སོ་ཤིང་དང་། འདག་པའི་ཆལ་ལ་སོགས་པ་སྟ་གོན་བྱ་སྟེ། གཤེགས་པ་དང་། བཤང་གཅི་བྱེད་པའི་གནས་སུ་ས་དང་འདབ་མ་དག་ཀྱང་སྟ་གོན་བྱས་ཏེ་བཞག་གོ། །

[Block 178]
དེ་ཙམ་ཞིག་བྱས་པས་ཆོག་གམ་ཞེ་ན། མི་ཆོག་པར་བསྟན་པའི་ཕྱིར། ལྷུང་བཟེད་བཀྲུ་ལ་སོགས་པ་དང་། །ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་མཁན་པོ་དང་སློབ་དཔོན་གྱི་ལྷུང་བཟེད་བཀྲུའོ། །

[Block 179]
སོགས་པའི༌[^103]སྒྲས་ནི་ཆོས་གོས་བཀྲུ་ཞིང་བཙེམ་པ་དང་གནས་བྱི་དོར་བྱ་བ་ལ་སོགས་པ་ལས་སུ་བྱ་བ་ཐམས་ཅད་བྱའོ། །

[Block 180 [HEADING]]
### ཞུ་བ། ^3-6-0
--- END BLOCKS ---
