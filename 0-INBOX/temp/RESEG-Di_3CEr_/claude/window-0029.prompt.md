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
[Block 1016]
དེ་བཞིན་དུ་ཨུཏྤ་ལའི་དྲི་བསུང་བ་ཉིད་ལས་དྲི་ཉིད་དང་། ཡོན་ཏན་ཉིད་དང་། བརྟེན་པ་ཉིད་དང་། ཡོན་ཏན་མ་ཡིན་པ་ཉིད་ལ་སོགས་པ་ཉིད་དུ་འགྲུབ་པ་ཡིན་ཏེ། དྲི་ཉིད་ལ་སོགས་པ་མེད་པ་ལ་མ༌[^759]མཐོང་བའི༌[^760]ཕྱིར་རོ། །

[Block 1017]
དེ་ལྟ་མ་ཡིན་ཏེ།

[Block 1018 [VERSE]]
གལ་ཏེ་ཞུགས་པ་བཞིན་གྲུབ་ན། །
དཀར་གཟུགས་ཡོན་ཏན་བརྟེན་པ་ལས། །
རིམ་པ་བཞིན་དུ་བཟློག་རིམ་ལ། །
གསུམ་གཉིས་གཅིག་ཏུ་རྟོགས་པར་འགྱུར། །

[Block 1019]
གཅིག་གི་ཚིག་ཏུ་སྨོས་པ་ནི་གཅིག་ཏུ་མ་བསྒྲུབས་པ༌[^761]འགལ་བ་མི་འཁྲུལ་བ་ཅན་ཡིན་པས་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་ཉིད་དུ་ཤེས་པར་བྱ་བའི་དོན་དུ་སྟེ་འདི་ལྟར་སྤྱི༌[^762]རྟག་པར་ཁས་ལེན་པ་ལ་མཉན་བྱ་ཉིད་དང་བྱས་པ་ཉིད་ཀྱི་སྒྲ་ལ་ཅི་འདི་རྟག་པ་ཡིན་ནམ། འོན་ཏེ་མི་རྟག་པ་ཡིན་ཞེས་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་སུ་འགྱུར་བ་ལྟ་བུའོ། །

[Block 1020]
ཅི་སྟེ་གཅིག་གི་ཚིག་ཏུ་བསྟན་པའི་ཕྱིར། །གཅིག་ཉིད་དུ་གོ་བར་བྱའོ་ཞེ་ན་མ་ཡིན་ཏེ། འགལ་བ་རྣམས་གཅིག་ལ་བརྗོད་པར་མི་འདོད་པས་སོ། །

[Block 1021]
བྱས་པ་ཉིད་དང་བརྩལ་མ་ཐག་ཏུ་འབྱུང་བ་ཉིད་ནི་གཉིས་པོ་གཅིག་ལ་གཏན་ཚིགས་ཉིད་དུ་འགྱུར་བ༌[^763]ཡིན་ཏེ། དཔེར་ན་བསླང་བའི་རྣམ་པ་དང་བྱ་བབས་པ་གཉིས་གཅིག་ཏུ་འདུས་པ་ལས་མཐོ་ཡོར་དུ་ཤེས་པ་ལྟ་བུའོ། །

[Block 1022]
དེ་ནི་བསྒྲུབ་བྱ་བཟློག་པ་ལ། །འགལ་བ། དེ་ཉིད་གཉིས་ཀའི་ཆར་རྣམ་པ་གཉིས་སུ་འཇུག་སྟེ། དེ་རྣམ་པར་བཅད་སྟེ༌[^764]བསྒྲུབ་པར་བྱ་བའི་དོན་དུ་གཞན་ལ་ཞུགས་པའི་ཕྱིར་བཟློག་པ་སྒྲུབ་པ་ཡིན་ཏེ། དཔེར་ན་གཏན་ཚིགས་དེ་དག་ཉིད་ལས་རྟག་པ་ཡིན་ནོ་ཞེས་སྒྲུབ་པར་བྱེད་པ་ལྟ་བུའོ། །

[Block 1023]
འདི་ལ་ཡང་རྟག་པ་བཀག་པའི་སྒོ་ཉིད་ནས་བཟློག་པ་སྒྲུབ་པར་བྱེད་དོ། །

[Block 1024]
གལ་ཏེ་འདི་ན་མེ་ཡོད་པའི་ཕྱིར་གྲང་བའི་རེག་པ་ཡོད་དོ་ཞེས་བྱ་བ་འདི༌[^765]ཇི་ལྟར་འགལ་བར་འགྱུར་ཞེ་ན། ཇི་ལྟར་ན་མི་འགྱུར་ཏེ། གང་གི་ཕྱིར་གྲང་བའི་རེག་པ་བཀག་པ༌[^766]ཙམ་གྱིས་དྲོ་བར་མི་འགྲུབ་པའི་ཕྱིར་རོ་ཞེ་ན། གལ་ཏེ་དྲོ་བར་མི་བསྒྲུབ༌[^767]ཏུ་ཆུག་ན་ཡང༌[^768]གྲང་རེག་མ་ཡིན་པ༌[^769]ནི་འགྲུབ་པ༌[^770]ཉིད་དོ། །

[Block 1025]
དེ་ལྟ་ན་ནི་གང་གི་ཚེ་མེས་དྲོ་རེག་མ་ཡིན་པའི་འགལ་བ་བསྒྲུབ་པ༌[^771]ཉིད་ཀྱིས་དྲོ་བའི་རེག་པ་གྲུབ་པར་བརྗོད་པས་དོན་གྱི༌[^772]ཤུགས་ཀྱིས་གྲང་རེག་མ་ཡིན་པར་གྲུབ་པའི་ཕྱིར་འགལ་བར་བརྗོད་པ་ལ་འགལ་བ་མེད་དོ། །

[Block 1026]
ཅི་སྟེ་བྱས་པ་ཉིད་ནི་རྩོལ་བ་ལས་བྱུང་བ་དང་མ་བྱུང་བ་གཉིས་ཀ་དང་ཐ་མི་དད་པ་ཡིན་ལ། ཐ་མི་དད་ཐམས་ཅད་ལས་མ་ལོག་པར་ཞུགས་པས་མི་རྟག་པ་ཉིད་རྗེས་སུ་ཞུགས་པའི་ཤེས་པས༌[^773]ནི་རྟག་པ་བཀག་པ་ལ་མི་ལྟོས་པ་ཡིན་ནོ་ཞེ་ན།[^774] གལ་ཏེ་གང་ཞིག་གང་ལ་ཞུགས་པ་དེ་ནི་རྗེས་སུ་ཞུགས་པའི་ཤེས་པའི༌[^775]བྱེ་བྲག་དེ་རྣམ་པར་གཞིག་པའི་སྒོ་ནས་བྱེད་པར་ནུས་ན་ནི་དེ་ལྟར་འགྱུར་རོ། །

[Block 1027]
གང་དུ་ཞུགས་པ་ནི། དེའི་བྱེ་བྲག་ལ་རྨོངས་པའོ། །

[Block 1028]
དཔེར་ན་བྱས་པ་ཉིད་རྩོལ་བ་ལས་བྱུང་བ་དང་། མ་བྱུང་བ་གཉིས་ཀ་ལ་ཞུགས་པའི་ཕྱིར་གཉིས་ཀར་སྒྲ་ལ་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་ཡིན་ཏེ། གལ་ཏེ་བྱས་པའི་ཕྱིར་རྩོལ་བ་ལས་བྱུང་བའོ་ཞེས་སྒྲུབ་པའམ། ཡང་ན་བྱས་པ་ཡིན་པའི༌[^776]ཕྱིར་རྩོལ་བ་ལས་མ་བྱུང་ངོ་ཞེས་སྒྲུབ་ཀྱང་རུང་ངོ་། །དེ་བཞིན་དུ་རྩོལ་བ་ལས་བྱུང་བ་ཉིད་ལས་ཡོན་ཏན་ནམ་ཡོན་ཏན་མ་ཡིན་པར་སྒྲུབ་པ་ཡང་ངོ་། །གལ་ཏེ་དེ་ལྟ་ན་ནི་བྱས་པའི་ཕྱིར་མི་རྟག་གོ། །

[Block 1029]
བདག་མེད་དོ་ཞེས་བྱ་བ་ཡང་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་སུ་འགྱུར་ཏེ། གཉིས་ཀ་ལ་ཡོད་པའི་ཕྱིར་རོ་ཞེ་ན། གལ་ཏེ་མི་རྟག་པ་དང་བྲལ་བའི་བདག་མེད་པ༌[^777]ལ་བྱས་པ་ཡོད་པར་འགྱུར་ན་ནི་དེ་ལྟ་བུ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1030]
དེ་ལྟ༌[^778]ན་ཕན་ཚུན་ལོག་པ་ཉིད་ལས་འདིའི་ཁྱད་པར་དུ་འགྱུར་རོ། །

[Block 1031]
དེའི་ཕྱིར་སྒྲ་ལ༌[^779]བྱས་པ་ཉིད་མི་རྟག་པ་དང་བདག་མེད་པ༌[^780]ལ་སོགས་པ་མཐོང་བའི་ཕྱིར་དང་། དེ་མེད་པ་ལ་མ་མཐོང་བའི་ཕྱིར་སྤྱིར་ཡང་ངེས་པའི་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 1032]
ཕན་ཚུན་ལོག་པ་ལ་ཞུགས་ན་ནི་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 1033]
རྟག་པ་བཀག་པ་སྤངས་པའི་མི་རྟག་པ་ཉིད་གཞན་ནི༌[^781]ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1034]
གང་རིགས༌[^782]མཐུན་མཐའ་དག་ལས་ལོག་པ་དེའི་སྒོ་ནས་བསྒྲུབ་བྱ་ལ་ཤེས་པ་འཇུག་པར་བྱེད་པ་དེ་དག༌[^783]ནི་རིགས་ཀྱི། འདིར་གོར་མ་ཆགས་པར་མཐུན་ཕྱོགས་མཐའ་དག་ལ་ཡོད་པའོ་ཞེས་པ་ནི་མ་ཡིན་ཞིང་། ཐམས་ཅད་ལ་ཡོད་པར་འཛིན་པ༌[^784]ཡང་མི་སྲིད་དོ། །

[Block 1035]
གཏན་ཚིགས་ལ་ནི་རང་དང་འབྲེལ་པ་བོར་ནས་གཞན་དུ་རྟགས་ཅན་གྱི་ཤེས་པ་བསྐྱེད་པའི་ནུས་པ་ཡང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1036]
འདིར་ཡང་གཅིག་ལྟ་བུའི་དབང་དུ་བྱས་ནས་རིག་པར༌[^785]བྱ་སྟེ། འདི་ལྟར་ངག་གི་རྣམ་པར་རིག་བྱེད་ཀྱི་སྒྲའི་བྱས་པ་ལས་རང་གིས་ཀུན་ནས་སློང་བའི་ཤེས་པ་མཐོང་བའི་ཕྱིར་ལུས་ཀྱི་རྣམ་པར་རིག་བྱེད་བཞིན་རྩོལ་བ་ལས་བྱུང་བ་ཉིད་གོ་བར་བྱེད་དོ། །

[Block 1037]
དེ་ལྟར་ན་དང་པོ་གཉིས་ཡིན་པས་གཅིག་ཉིད༌[^786]འཛིན་པའི་བྱ་བ་ཅན་ཡིན་ནོ། །

[Block 1038]
དེར་ཡང་ནི་ཆོས་གཞན་བསྟན་པ་ལས་གྱུར་པ་ཉིད་ཀྱི་དེས་པ་ཡིན་གྱི། དེར་ནི་ཉིད༌[^787]ཀྱིས་ངེས་པར་བསྐྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 1039]
སྤྱི་དང་ཁྱད་པར་གྱི་ཆོས་དག་ནི་རྣམ་པར་མ་བཅད་པའི་གཏན་ཚིགས་ཡིན་པའི་ཕྱིར་དེ་ཉིད་ཆོས་གཞན་ངེས་པར་བྱེད་པའི་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 1040]
གཉིས་ཀའི་ཆ་ནི་གཞན་ལས་རྣམ་པར་བཅད་ནས་གང་ན་ཐེ་ཚོམ་ཡོད་པ་དེ་ན་གཞན་དང་ལྡན་ན་ངེས་པའི་གཏན་ཚིགས་ཡིན་ཏེ། འདི་ལྟར་འགྲེང་བ་དང་བྱ་བབས་པ་ལས་མཐོ་ཡོར་དུ་རྟོགས་པ་མཐོང་བ་ནི་ཁ་ཡར་བ་ལས་ངེས་པར་མི་ནུས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་དང་། རང་གིས་ཀུན་ནས་སློང་བ༌[^788]དང་བྱས་པ་དག་ལས་སོ་ཞེས་བྱ་བ་ནི་སྒྲ་རྟག་པར་སྨྲ་བ་རྣམས་ལའོ། །

[Block 1041]
དེའི་ཕྱིར་འདིར་གཅིག་ཉིད་གཟུང་བར༌[^789]བྱའོ། །

[Block 1042]
དེ་ནི་གང་ཞུགས་པ་ཉིད་ལ་ལྟོས་ནས་ཐེ་ཚོམ་སྐྱེད་པར་བྱེད་དེ། དཔེར་ན་ཅི་སྒྲ་འདི་བྱས་པའི་ཕྱིར་བུམ་པ་བཞིན་རྩོལ་བ་ལས་བྱུང་བ་ཡིན་ནམ། ཡང་ན་གློག་ལ་སོགས༌[^790]པ་བཞིན་མ་ཡིན་ཞེས་འགྱུར་གྱི་ནམ་མཁའ་ལ་སོགས་པ་བཞིན་ནམ་ཞེས་སྦྱོར་བར་བྱེད་པ་ནི་མ་ཡིན་ཏེ། འདི་ལྟར་བྱས་པ་ཉིད་ནམ་མཁའ་ལ་སོགས་པ་རྟག་པ་ཉིད་ལས་རྣམ་པར་བཅད་ནས་མི་རྟག་པ་ལ་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་སུ་འགྱུར་རོ། །

[Block 1043]
དོན་གཞན་རྣམ་པར་བཅད་པའི་གཏན་ཚིགས་གཞན་གྱིས་ཡོངས་སུ་གྱུར་པའི་དེ༌[^791]ལ་ཐེ་ཚོམ་དུ་གྱུར་པ་ནི་མ་ཡིན་ནོ། །

[Block 1044]
མ་ཡིན་པར་དགག་པ་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 1045]
གལ་ཏེ་འདི་རྟག་པ་མ་ཡིན་ལ་མི་རྟག་པའོ་ཞེས་བརྗོད་པ་ཡིན་ཏེ། དེ་ལྟ༌[^792]མ་ཡིན་ན་བུམ་པ་ལ་སོགས་པ་རང་རང་གི་ཚིག་བརྗོད་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 1046]
འདི་ལ༌[^793]ཡང་མེད་པར་དགག་པ་ལས་ཁྱད་པར་དུ་བསྒྲུབ་པར༌[^794]བྱ་རྒྱུའི་བྱ་བ་རྟག་པ་རྣམ་པར་བཀག་པ་དང་སྦྱར་བ་ཡིན་ནོ་ཞེས་བརྗོད་པར་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 1047]
རྟག་པ་ཞེས་ནི་མ་ཡིན་ནོ། །

[Block 1048]
དཔེར་ན་སྒྲ་རྟག་སྟེ་རེག་བྱ་མ་ཡིན་པའི་ཕྱིར་ཞེས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལྟ་བུ་འདི་ལ་ནི་ཐེ་ཚོམ་ལ་ལྟོས་ནས་བཀག་པ་ཡིན་ལ་སྔ་མ་ནི་བཟློག་པ་ལ་ལྟོས་ནས་ཡིན་ནོ། །

[Block 1049]
གང་གི་ཚེ་རྟག་པར་ཁས་མི་ལེན་པ་དེའི་ཚེ་ཡང་གཞན་གྱིས་ཀུན་ཏུ་བརྟགས་པ་ལ་ལྟོས་ནས་ཤིན་ཏུ་མཐར་གནས་པ་བཀག་སྟེ། [^795]འདིའི་དུས་ན་ཡོད༌[^796]བཞིན་པའི༌[^797]སྔོན་དང་ཕྱི་མཐར་གནས་པ་མ་ཡིན་པ་ལ་མི་རྟག་པ་ཡིན་ནོ་ཞེས་བརྗོད་པ་ལ་ཉེས་པ་མེད་དོ། །

[Block 1050]
གལ་ཏེ་འདི་ལྟར་ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་རྟག་པའི་ཞེས་བྱ་བ་ལྟ་བུ་ཐམས་ཅད་དུ་བསྒྲུབ་པར་བྱ་བ་གཉིས་ཀའི་ཆ་ལ་ལྟོས་པ་རྣམ་པ་གསུམ་པ་འདི་ཅི་ལྟར༌[^798]རྣམ་པར་གཅོད་པའི་གཏན་ཚིགས་ཡིན་ཞེ་ན། འདི་ཡང་གང་ལ་ལྟོས་པའི་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་དེ་གཞན་ལས་རྣམ་པར་བཅད་པ་ཡིན་ཏེ། འདི་ལྟར་གཉིས་ཀ་ལ་ཞུགས་པ་ཉིད་ཀྱང་ནམ་མཁའ་ལ་སོགས་པ་དང་། ལས་ལ་སོགས་པ་ལ་ལྟོས་ནས་ཐེ་ཚོམ་དུ་མ་ཡིན་གྱི་རྡུལ་ཕྲ་རབ་དང་བུམ་པ་ལ་སོགས་པ་ལ་ལྟོས་ནས་ནི་མ་ཡིན་ནོ། །

[Block 1051]
དེའི་ཕྱིར་བསྒྲུབ་བྱ་འདི་ལ་ཆོས་གཞན་ལུས་ཅན་ལས་རྣམ་པར་བཅད་པའི་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 1052]
འདི་ལྟར་སྒྲ་ལུས་ཅན་མ་ཡིན་པའི་ཕྱིར་བྱ་བ་དང་བྲལ་བའོ་ཞེས་བྱ་བ་དང་། བྱ་བ་དང་བཅས་པའོ་ཞེས་བྱ་བ་ལྟ་བུ་རྟག་པ་དང་མི་རྟག་པ་ཐམས་ཅད་ལས་ལོག་པའི་རྟགས༌[^799]ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 1053]
འདི་ནི་བསྒྲུབ་བྱ་གཉིས་ཀའི་ཆ་ལ་ལྟོས་ནས་ཡང་དག་པ་དང་། ལོག་པ་དང་། ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་སོ་ཞེས་བརྗོད་པ་ཡིན་ནོ། །

[Block 1054]
གཏན་ཚིགས་དེའི་གཟུགས་བརྙན་དང་བཅས་པ་བརྗོད་དོ། །

[Block 1055 [HEADING]]
### གཞན་གྱི་འདོད་པ་ལ་དཔྱད་པ། ^3-3-0
--- END BLOCKS ---
