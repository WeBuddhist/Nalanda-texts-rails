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
[Block 981]
འདི་ལྟར་གཞན་གྱི་དོན་བྱེད་པ་ཁྱད་པར་ཅན་ལས་བཟློག་པ་བསྒྲུབ་པའི༌[^736]ཕྱིར་དེ་ནི་འགལ་བ་ཉིད་དོ། །

[Block 982]
དེ་ལྟར་ན་འདུས་པ་གཞན་གྱི་དོན་བྱེད་པ་ལ་འདུས་པ་མ་ཡིན་པ་རྣམས་ཀྱི་དོན་བྱེད་པར་སྒྲུབ་འདོད་པ་འདི་ནི་གཞན་འདུས་པ་ཉིད་ཀྱི་རྟགས་ཡིན་ནོ། །

[Block 983]
དེའི་འདུས་པ་མ་ཡིན་པ་ཉིད་ནི་མངོན་སུམ་མམ་རྗེས་སུ་དཔག་པས་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 984]
དེ་ཡོད་པར་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 985]
འདི་ནི་ཐེ་ཚོམ་མ་ཡིན་ཏེ་ཁྱད་པར་ཅན་བཟློག་པའི་གཏན་ཚིགས་འདི་ཉིད་ཀྱིས་གཞན་འགལ་བ་མི་འཁྲུལ་བ་ཅན༌[^737]ཉིད་ལས་ཐ་དད་དུ་ཕྱེ་བ་ཡིན་ནོ། །

[Block 986]
དེ་བཞིན་དུ་མཐོང་བ་ལ་གནོད་པ་ནི་ཆོས་ཅན་གྱི་རང་གི་ངོ་བོའི་བྱེ་བྲག་ཕྱིན་ཅི་ལོག་ཏུ་བསྒྲུབ་པའི༌[^738]ཕྱིར་འགལ་བར་བརྗོད་པར་བྱ་སྟེ། དཔེར་ན་རྩོལ་བ་ལས་བྱུང་བའི་ཕྱིར་སྐྲ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དང་། མཉན་བྱ་མ་ཡིན་ནོ༌[^739]ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 987]
གཉིས་ཀ་བསྒྲུབ་བྱར་འགྱུར་བ་ནི་ཆོས་ཀྱི་ཁྱད་པར༌[^740]དུ་བྱས་པའི་ཆོས་ཅན་བསྒྲུབ་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 988]
དེ་ལ་གང་ཡང་རུང་བ་གཅིག་གམ༌[^741]གཉིས་ཀ་ཡང་རུང་སྟེ། རང་གི་ངོ་བོ་བྱེ་བྲག་ལས་ཕྱིན་ཅི་ལོག་ཏུ་སྒྲུབ་པའི་ཕྱིར་འགལ་བ་ཉིད་དུ༌[^742]རིགས་པ་ཡིན་ནོ། །

[Block 989]
གཉིས་ཀའི་དཔེར་བརྗོད་བསྟན་པར་བྱ་སྟེ། སྨྲ་བ་ཐམས་ཅད་བརྫུན་གྱི་དོན་ཅན༌[^743]ཏེ། མཚོན་བྱེད་ཡིན་པའི་ཕྱིར་རྨི་ལམ་གྱི་བྱ་བའི་རྣམ་པར་རིག་བྱེད་བཞིན་ནོ་ཞེས་བྱ་བ་ལ། གང་དེ་བཞིན་དུ་སྨྲ་བ་ཡོད་ན་ནི་སྨྲ་བ་དང་སྨྲ་བའི་བདག་ཉིད་ཡིན་པ་བརྫུན་གྱི་དོན་ཅན་ཉིད་ཡིན་པས་ན་སྤྱིར་བསྡོམས་པའི་དོན་ལ་སྐུར་པ༌[^744]བཏབ་པ་ཡིན་ནོ། །

[Block 990]
དེས་ན་དེའི་རང་གི་ངོ་བོ་དང་འགལ་བ་ཡིན་ནོ། །

[Block 991]
གལ་ཏེ་སྨྲ་བ་ཉིད་བརྫུན་གྱི་དོན་ཅན་མ་ཡིན་ན་ནི་དེའི་བྱེ་བྲག་དང་འགལ་བ་ཡིན་ནོ། །

[Block 992]
ཡང་བརྗོད་པ།

[Block 993 [VERSE]]
ཆོས་དང་ཆོས་ཅན་རང་ངོའམ། །
དེ་ཡི་བྱེ་བྲག་ཡིན་ཡང་རུང་། །
ཕྱིན་ཅི་ལོག་ཏུ་སྒྲུབ་པའི་ཕྱིར། །
དེ་ལ་གནོད་པས་འགལ་བ་ཡིན། །

[Block 994]
གང་དུ་སློབ་དཔོན་གྱིས།

[Block 995]
ནང་ལ་འདུས་བསགས་ཉིད་མ་ཡིན། །དེ་བཞིན་གཞན་དོན་ཅན་མ་ཡིན། །ཞེས་དོགས་པ་བསུ་སྟེ། གསུངས་པ་དེ་ལ་འདུས་པ་ཉིད་ནི་མིག་ལ་སོགས་པ་ནང་གི་ཉིད་དང་ལྡན་པའི་གཏན་ཚིགས་སུ་བཀོད་པའི་གཏན་ཚིགས་ཀྱི་མཚན་ཉིད་དང་ལྡན་པ་བཀག་པ་སྟེ། དེ་ལྟར་ན་ནི་གཉིས་ཀ་མཐུན་ཕྱོགས་ལ་མི་འགྲུབ༌[^745]བོ། །

[Block 996]
འགལ་ཟླའི་ཕྱོགས་ལ་ནི་གཞན་ཐམས་ཅད་ཀྱི་དོན་བྱེད་པ་ཉིད་དུ་གྲུབ་པས་ན་འགལ་བ་སྔ་མ་ཉིད་ཀྱི་ཁོངས་སུ་འདུས་སོ། །

[Block 997]
དེ་ཉིད་གསལ་བར་བྱ༌[^746]བའི་ཕྱིར་

[Block 998 [HEADING]]
#### དོན་གཞན་གྱི་སྒོ་ནས་བརྗོད་པ། ^3-2-5-0

[Block 999]
དེ་དག་ཉིད་དུ་དོན་གཞན་གྱི་སྒོ་ནས་བརྗོད་པ།

[Block 1000]
ཐུན་མོང་དང་ནི་ཁྱད་པར་གྱི། །ཆོས་དང་བསྒྲུབ་བྱ་ལ་གཉིས་སོ། །

[Block 1001]
གང་བསྒྲུབ་བྱའི་ཆོས་ཀྱི་གོ་བྱེད་དེ་ནི་གསུམ་ཉིད་ཡིན་ཏེ། སྤྱི་དང་། ཁྱད་པར་དང་། གཉིས་ཀའི་ཆ་ཤས་རྣམས་སོ། །

[Block 1002]
རྣམ་པ་དགུ་ཉིད་དུ་ཕྱེ་བ་ཡང་གསུམ་པོ་དེ་དག་ཉིད་ལས་ཡིན་པར་བལྟ་བར་བྱའོ། །

[Block 1003]
དེ་ལ་དང་པོ་གཉིས་ཐེ་ཚོམ། །དངོས་པོ་ཀུན་གྱི་རང་རང་གི་བྱེ་བྲག་ཐ་དད་པ་ལ་སྤྱི་དང་ཁྱད་པར་གྱི་ཆོས་ཅན་གྱི༌[^747]མཐའ་གཅིག་ཏུ་ཐེ་ཚོམ་སྐྱེད་པར་བྱེད་དེ། དཔེར་ན་སྒྲ་རྟག་པའམ་མི་རྟག་པར་གྲུབ་པ༌[^748]ལ༌[^749]གཞལ་བྱ་ཡིན་པའི༌[^750]ཕྱིར་ཞེས་བྱ་བ་དང་། དེ་བཞིན་དུ་མཉན་བྱ་ཡིན་པའི་ཕྱིར་ཞེས་པ་བཞིན་ནོ། །

[Block 1004]
ལྷག་མ་ལྟོས་ནས་གསུམ་དུ་ཕྱེ། །བསྒྲུབ་བྱ་ལ་ལྟོས་ནས་གཉིས་ཀའི་ཆ་ལ་ནི་ཡང་དག་པ་དང་། ལོག་པར་རྟོགས་པ༌[^751]དང་ཐེ་ཚོམ་གྱི་གཏན་ཚིགས་ཉིད་དུ་ཡིན་ནོ། །ཅི་ཡང་རྒྱུ་གང་གི་ཕྱིར་ཞེ་ན།

[Block 1005]
དང་པོ་གཉིས་མཐའ་གཅིག་ཏུ་ཐེ་ཚོམ་དུ་འགྱུར་བ་ནི་འདི་ལྟར་དེ་དག་གཉིས་ནི་ཐམས་ཅད་ཀྱི།

[Block 1006]
རྗེས་སུ་ཞུགས་དང་མ་ཞུགས་ལས། །ལྡོག་དང་རྗེས་འགྲོ་གྲུབ་མིན་ཕྱིར། །

[Block 1007]
ཕྱོགས་དུ་མ་དག་ལས་གཅིག་རྣམ་པར་བཅད་པ༌[^752]ཡང་མ་ཡིན་ལ་ཅིག་ཤོས་སྒྲུབ་པར་གཏན་ལ་ཕབ་པ་ཡང་མ་ཡིན་པ་དེ་ནི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་དག་ལས་ཡིན་ཏེ། དེ་དག་ནི་ཆ་ཤས་གཅིག་དང་ཡང་མ་བྲལ་བ་ཡིན་པར་རྟོགས་སོ། །

[Block 1008]
གལ་ཏེ་དེ་ལྟ༌[^753]ན་ནི་གཅིག་ལ་ངེས་པར་ཞུགས་པ་དང་། ལོག་པའང་མིན་པ་རྟགས་སུ་འགྱུར། །འདི་ལྟར་གཉིས་ཀའི་ཆ་ལ༌[^754]གཅིག་ཏུ་ངེས་པར་ཞུགས་པ་མ་ཡིན་ཞིང་རྗེས་སུ་ཞུགས་པ་དང་ལོག་པ་དག་ནི་གཉིས་ཀའི་གཏན་ཚིགས་སུ་འགྱུར་རོ་ཞེ་ན།

[Block 1009 [VERSE]]
གལ་ཏེ་སྲིད་དུ་ནི་འགྱུར་ལ། །
གཉིས་ཀར་འགྱུར་བ་སྲིད་མ་ཡིན། །
ཡོད་པ་གཉིས་ཀ་མིན་པའང་མིན། །

[Block 1010]
གང་དོན་གཅིག་ལ་རྟག་པར་ཡང་འགྱུར་མི་རྟག་པར༌[^755]འགྱུར་བ་ནི་མི་སྲིད་དོ། །

[Block 1011]
དེ་བཞིན་དུ་ཡོད་པའི་དོན་རྟག་པ་ཡང་མ་ཡིན་མི་རྟག་པ་ཡང་མ་ཡིན་པ་ཡང་མ་ཡིན་ནོ། །

[Block 1012]
གལ་ཏེ་འདི་ལྟར་ཇི་ལྟར་ན་གཉིས་ཀའི་ཆ་སྟེ་འགལ་བའི་དོན་དུ་མ་ལ་འཇུག་ཅིང་ཐམས་ཅད་ཀྱི་རྗེས་སུ་འཇུག་པ་སྟེ༌[^756]ཤེས་བྱེད་ཀྱི་རྟགས་སུ་འགྱུར་ཞེ་ན། །དོན་གཞན་རྣམ་པར་བཅད་པའི་སྒོ་ནས་ཡིན་གྱི་དེའི་ཁྱད་པར་བཟུང་ནས་ནི་མ་ཡིན་ཏེ། འདི་ལྟར་དེ་ནི།

[Block 1013 [VERSE]]
གང་དུ་མེད་དེ་རྣམ་གཅོད་དུ། །
གྲུབ་དོན་དོན་བཞིན་སྒྲུབ་པར་བྱེད། །
གཅིག་དེ་གཞན་ལ་གཉིས་སུ་འཇུག །

[Block 1014]
གཉིས་ཀའི་ཆ་ལ་ནི་གང་ལ་མེད་པ་དེ་ལས་རྣམ་པར་གཅོད་དོ།[^757] །

[Block 1015]
དེའི་སྒོ་ནས་བསྒྲུབ་བྱའི་རིགས་མཐའ་དག་གམ་ཕྱོགས་གཅིག་ལ་ཞུགས་ནས་དོན་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པར་བྱེད་པའི་གཏན་ཚིགས་སུ་བརྗོད་པ་ཡིན་ཏེ། དཔེར་ན་སྒྲ་མི་རྟག་སྟེ་བྱས་པའི་ཕྱིར་ཞེས་བྱ་བ་དང་། རྩོལ་བ་ལས་བྱུང་བའི༌[^758]ཕྱིར་ཞེས་པ་ལྟ་བུའོ། །

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
--- END BLOCKS ---
