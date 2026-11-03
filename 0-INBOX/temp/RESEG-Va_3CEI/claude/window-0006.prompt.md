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
[Block 211]
བདུད་དང་མུ་སྟེགས་འདུལ་བར་འོས་པ་སྟེ། སེམས་ཤིན་ཏུ་རྣམ་པར་གྲོལ་བའི་ཡེ་ཤེས་ཀྱི་སྤོབས་པ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 212]
ཆོས་རྣམས་ལ་ཤེས་རབ་མྱུར་བར་འོས་པ་སྟེ། ཤེས་རབ་ཤིན་ཏུ་རྣམ་པར་གྲོལ་བའི་ཕྱིར་ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ལ་མཁས་པའོ། །

[Block 213]
ཆོས་འཆད་པ་ལ་ཧ་ཅང་མྱུར་བ་དང་བུལ་བའི་སྐྱོན་དང་བྲལ་བར་འོས་པ་སྟེ། ཆོས་འཆད་པ་ལ་མཁས་པ༌[^293]འབྲེལ་པ་སྐྱོ་བ་དང་བྲལ་བ་ཇི་ལྟར་རྟ་ཅང་ཤེས་བཞིན་སེམས་ཤིན་ཏུ་དུལ་བའི་ཕྱིར་རོ། །

[Block 214]
གཅིག་པུ་དབེན་པར་འོས་པ་སྟེ། ཟས་དང་གོས་ལ་སོགས་པ་ཡོ་བྱད་ཐམས་ཅད་མི་སོག༌[^294]མི་སྡུད་པས་ཆོག་ཤེས་པར་གནས་པ་ནི་ཇི་ལྟར་གླང་པོ་ཆེ་འདུ་འཛི་དང་བྲལ་བ་བཞིན་ནོ། །

[Block 215]
གཅིག་ཏུ་ན་བསམ་གཏན་རྣམས་ལ་མ་ཆགས་པ་སྟེ། བྱ་བ་བྱས་པས་རྟག་ཏུ་བླ་མའི་ས་ལ་བརྩོན་པའི་ཕྱིར་རོ། །

[Block 216]
རྟག་ཏུ་སྟོང་པ་ཉིད་ཀྱི་སྤྱོད་པའི་ཕྱིར་བྱེད་པ་བྱས་པས་བདག་དང་བདག་གིར་འཛིན་པ་དང་བྲལ་བའི་ཕྱིར་རོ། །

[Block 217]
རྟག་ཏུ་མཚན་མ་མེད་པའི་སྤྱོད་པ་དང་ལྡན་པས་ཁུར་ལྕི་བ་བོར་བའི་ཕྱིར་འགོག་པ་ཉིད་ལ་གནས་པའོ། །

[Block 218]
རྟག་ཏུ་སྨོན་པ་མེད་པའི་སྤྱོད་པ་དང་ལྡན་པས། རང་གི་དོན་བདེ་བ་ཐོབ་པའི་ཕྱིར་འཁོར་བ་ལ་སྨོན་པ་མེད་པར་གནས་པའོ། །

[Block 219]
འཇིག་རྟེན་རྣམས་ཀྱི་བསམ་གཏན་དགའ་བའི་རོ་ལ་ཆགས་པ་མེད་པའི་ཕྱིར་སྲིད་པར་སྦྱོར་བ་ཡོངས་སུ་སྤངས་པའོ།[^295] །ཆོས་རྣམས་ཀྱི་ཡོན་ཏན་ཁྱད་པར་ཅན་ལ། རྫུ་འཕྲུལ་གྱིས༌[^296]རོལ་པའི་ཕྱིར་བཀའ་ཡང་དག་པས་སེམས་ཤིན་ཏུ་རྣམ་པར་གྲོལ་བའོ། །

[Block 220]
དོན་དམ་པ་ཉིད་ཀྱི་ཡོན་ཏན་ལ་བདེ་བར་གནས་པ་སྟེ། སེམས་ཀྱི་དབང་པོ་ཐོབ་པས་འདུས་མ་བྱས་ལ་རེག་པའི་ཕྱིར་སེམས་ཀྱི་དབང༌[^297]ཐོབ་པའོ། །

[Block 221]
ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཤེས་པའི་ཕྱིར་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པའི་ཡོན་ཏན་ཐོབ་པར༌[^298]བྱེད་པའི་ཕྱིར་རོ། །

[Block 222 [HEADING]]
###### **དོན་གྱི་མདོ་བསྡུ་བ།** ^4-1-5-5-1-3-0

[Block 223]
བསྡུ་བའི་དོན་ནི་གོང་དུ་སྨོས་པའི་ཚིག་བཅོ་ལྔ་པོ་ཡོན་ཏན་བཅུར་བསྡུ་བར་བྱ་སྟེ། བསྟན་དུ་ཡོད་པའི་འབྲས་བུ་དང་། བསྟན་དུ་མེད་པའི་འབྲས་བུ་སྟེ། དགྲ་བཅོམ་པའི་འབྲས་བུ་ལ་འདུས་བྱས་ནི་བསྟན་དུ་ཡོད་པ་འདུས་མ་བྱས་ནི་བསྟན་དུ་མེད་པའི་འབྲས་བུའོ། །

[Block 224]
ཡོན་ཏན་རྣམ་པ་བཅུ་ལ་ཟག་པ་ཟད་པ་དང་ཉོན་མོངས་པ་མེད་པ་ནི་འཆིང་བ་དང་བག་ལ་ཉལ་བ་གཉིས་སྤངས་པའི་ཕྱིར་རོ། །

[Block 225]
དབང་དུ་གྱུར་པ་དང་། སེམས་དང་ཤེས་རབ་རྣམ་པར་གྲོལ་བ་ནི་སེམས་དབང་དུ་གྱུར་པས་འཇིག་རྟེན་གྱི་ཡོན་ཏན་ཐམས་ཅད་ཟིལ་གྱིས་མནན་ཏེ། འཁྲུག་པ་སྣ་ཚོགས་ཞི་བའི་ཕྱིར་རོ། །

[Block 226]
དེ་བཞིན་གཤེགས་པའི་བསྟན་པའི་རྗེས་སུ་ཞུགས་པའི་ཕྱིར། རྟ་ཅང་ཤེས་ལྟ་བུ་ཞི་ཞིང་དུལ་བ་ཡིད་བཞིན་དུ་དབང་དུ་གྱུར་པའོ། །

[Block 227]
ཡོན་ཏན་ཁྱད་པར་ཅན་ཐོབ་པ་ནི་གླང་པོ་ཆེ་ལྟར་གཟི་བརྗིད་ཆེ་བས་མཐུ་དང་རྫུ་འཕྲུལ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 228]
བྱ་བ་བྱས་པ་ཡོན་ཏན་ཁྱད་པར་ཅན་ནི་བཅོམ་ལྡན་འདས་ལ་རིམ་གྲོ་དང་བསྟི་སྟང་བྱེད་པ་ནི་ཡང་དག་པའི་ཆོས་ཀྱི་རིམ་གྲོ་བྱེད་པ་ཡིན་གྱི་ནོར་རྫས་ཀྱིས་ནི་མ་ཡིན་ནོ། །

[Block 229]
ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་ནི་བྱེད་པ་བྱས་པ་རྫོགས་པ་སྟེ། སློབ་པའི་ས་རྣམས་རྫོགས་པས་འགོག་པའི་བདེན་པའི་མཐར་ཕྱིན་པའི་ཕྱིར་རོ། །

[Block 230]
ཤིན་ཏུ་འདས་པར་གྱུར་པའི་ཡོན་ཏན་ནི་ཁུར་བོར་བ་རང་གི་དོན་ཐོབ་པ་སྲིད་པའི་སྦྱོར་བ་ཡོངས་སུ་ཟད་པ་སྟེ། ཤི་འཕོའི་ཁུར་ལྕི་བ་བོར་བ་དང་། ལོག་པའི་འཚོ་བ་སྤངས་པས་ཁེ་དང་གྲགས་པ་མི་ཚོལ་བ་དང་། སྲིད་པའི་མདུད་པ་གཅོད་པ་སློབ་པའི་ས་ལས་འདས་པའི་ཕྱིར་རོ། །

[Block 231]
ཡོན་ཏན་བླ་མའི་ཡང་བླ་མ་སྡུད་པ༌[^299]ནི་ཡང་དག་པའི་ཡེ་ཤེས་ཀྱི་སེམས་རྣམ་པར་གྲོལ་བས་འདུས་མ་བྱས་ཀྱི་འབྲས་བུ་ལ་རེག་པའི་ཕྱིར་རོ། །

[Block 232]
སེམས་ཅན་ལ་ཕན་འདོགས་པའི་ཡོན་ཏན་སྡུད་པ་ནི་སེམས་ཀྱི་དབང་དམ་པ་ཐོབ་པའི་ཕྱིར་རྫུ་འཕྲུལ་དང་མངོན་པར་ཤེས་པ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 233]
བླ་མའི་ཡང་བླ་མའི་ཡོན་ཏན་སྡུད་པའི༌[^300]ཡོན་ཏན་ཐམས་ཅད་ཀྱི་མཐར་ཕྱིན་པ་སྟེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་རྫོགས་པའི་ཕྱིར་རོ། །

[Block 234 [HEADING]]
###### ཉན་ཐོས་ཆེན་པོ་རྣམས་ཀྱི་མཚན་བཤད་པ། ^4-1-5-5-2-0

[Block 235]
ཡང་མདོ་ལས་འདི་ལྟ་བུ་ཞེས་བྱ་བ་ནས་ཆུ་བོ་འོད་སྲུངས་ཀྱི༌[^301]བར་དུ་སྟེ། འདི་མན་ཆད་ཉན་ཐོས་ཆེན་པོ་རྣམས་ཀྱི་མཚན་བཤད་པ་ལ་རྣམ་པ་གཉིས་ཏེ། སྔར་སོ་སོའི་མཚན་སྨོས་པ་དང་། ཡོན་ཏན་བསྡུ་བའོ། །

[Block 236]
ཉན་ཐོས་དེ་དག་གི་རིམ་པ་ནི་ལ་ལ་རབ་ཏུ་བྱུང་བ༌[^302]སྔ༌[^303]ཕྱི་ལས་བཀོད་པ་དང་། ལ་ལ་ཡོན་ཏན་ཆེ་བས་སྔར་བཞག་པ་ཡང༌[^304]ཡོད༌[^305]དེ། དེ་དག་ཀྱང་བཅོམ་ལྡན་འདས་དང་པོ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པའི་ཚེ་ཉན་ཐོས་ཆེན་པོ་ལྔ་རབ་ཏུ་བྱུང་ངོ་། །དེའི་འོག་ཏུ་གྲགས༌[^306]འཛིན་གྱི་འཁོར་ལྔ་བཅུ་རབ་ཏུ་བྱུང་ངོ་། །དེའི་འོག་ཏུ་ལྟེང་རྒྱས་འོད་སྲུངས་ཀྱི་འཁོར་ལྔ་བརྒྱ་དང་། ག་ཡ་འོད་སྲུངས་ཀྱི་འཁོར་སུམ་བརྒྱ་དང་། ཆུ་བོ་འོད་སྲུངས་ཀྱི་འཁོར་ཉིས་བརྒྱ་དང་། ཤཱ་རིའི་བུའི༌[^307]འཁོར་བརྒྱ་དང་། མཽད་གལ་གྱི་བུའི་འཁོར་བརྒྱ་རབ་ཏུ་བྱུང་བ་དང་། སྤྱིར་སྟོང་ཉིས་བརྒྱ་ལྔ་བཅུ་རབ་ཏུ་བྱུང་ངོ་། །ཉན་ཐོས་ཆེན་པོ་ལྔ་ཡང་དང་པོ་བཅོམ་ལྡན་འདས་མངོན་པར་བྱང་ཆུབ་ནས་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བའི་ཚེ་དང་པོར་ཅང་ཤེས་ཀཽཎྜི་ནྱས་བདེན་པ་དང་པོར་རྟོགས་ཏེ་ངས་ཀུན་ཤེས་སོ་ཞེས་སྨྲས་པ་ལས་རུས་ཀཽཎྜི་ནྱ༌[^308]ཀུན་ཤེས་སུ་བཏགས་སོ། །

[Block 237]
འོད་སྲུངས་ཆེན་པོ་ནི་དང་པོ༌[^309]དྲང་སྲོང་འོད་ཅན་གྱི་རིགས་ཏེ་འོད་སྲུངས་འདི་ཉིད་དང་པོ༌[^310]བཙས་པའི་ཚེ་ཡང་འོད་བྱུང་བའི་ཕྱིར་འོད་སྲུངས་ཞེས་བཏགས་ཏེ་འོད་སྲུངས་གཞན་ལས་དགར་བའི༌[^311]ཕྱིར་འོད་སྲུངས་ཆེན་པོ་ཞེས་བཏགས་སོ། །

[Block 238]
ལྟེང་རྒྱས་འོད་སྲུངས་དང་གཞན་ནི་ཆུ་དང་རི་དང་ཤིང་གི་འབྲས་བུ་ལས་བཏགས་ཏེ་མིང་ཙམ་དུ་ཟད་དོ། །

[Block 239]
མདོ་ལས་ཤཱ་རིའི་བུ་ནས་ཀ་པི་ནའི་བར་དུ་སྟེ་སོ་སོའི་མིང་བཤད་པ་ནི། ཤཱ་རིའི་བུ་ནི་མ་བྱ་ཤ་རི༌[^312]ཀའི་མིག་དང་འདྲ་བར་མིག་མཛེས་པའི་བུ་ཡིན་པས་ཤཱ་རིའི་བུ་ཞེས་བཏགས་སོ། །

[Block 240]
མཽད་གལ་ཆེན་པོ་ནི་སྔོན་དྲང་སྲོང་ཉིད༌[^313]རི་ལ་གནས་ཤིང་སྲན་མ་རྨེད་པ་ལས་རུས་སུ་ཆགས་ཏེ། མཽད་གལ་གྱི་མ་དེའི་རྒྱུད་ཡིན་པས་ན་མཽད་གལ་ཞེས་བཏགས་སོ།[^314] །རྫུ་འཕྲུལ་ཆེ་བའི་ཕྱིར་མཽད་གལ་ཞེས་བཏགས་སོ། །

[Block 241]
ཀཱ་ཏྱཱ་ཡ་ན་ཆེན་པོ་ནི་སྔོན་དྲང་སྲོང་ཞིག་ཏུ༌[^315]སྐྲ་བྲེགས་པ༌[^316]ལས་རུས་སུ་སོང་སྟེ།[^317] དེའི་རྒྱུ་ལས་རུས་ལས་མིང་དུ་བཏགས་པའོ། །

[Block 242]
འདི་མན་ཆད་ཉན་ཐོས་ཀྱི་རྣམས་ལ་ལ་ནི་སྐར་མ་ལས་བཏགས། ལ་ལ་ནི་སྔོན་གྱི་བྲམ་ཟེའི་རུས་ལས་བཏགས། ལ་ལ་ནི་དབྱིབས་འདྲ་བ་ལས་བཏགས་ཏེ། སྤྱིར་མིང་ཙམ་དུ་ཟད་དོ། །

[Block 243]
མདོ་ལས་སློབ་པ་དང་མི་སློབ་པ་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་དང་། །ཏིང་ངེ་འཛིན་དང་། །

[Block 244 [VERSE]]
ཤེས་རབ་ནི་བསླབ་པར༌[^318]བྱ་བ་དང་། །
དེ་གསུམ་ལ་གནས་པ་ནི་སློབ་པའོ། །

[Block 245]
དེ་གསུམ་རྫོགས་པར་གྱུར་པ་ནི་མི་སློབ་པའོ། །

[Block 246 [HEADING]]
###### འཕགས་པའི་ཡོན་ཏན་བསམ་གྱིས་མི་ཁྱབ་པ་བསྟན་པ། ^4-1-5-5-3-0

[Block 247]
མདོ་ལས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་སྟོང་ཕྲག་བརྒྱད་ཅུ་ཞེས་སྨོས་པ་ལྔ་པ་སྟེ། །འཕགས་པའི་ཡོན་ཏན་བསམ་གྱིས་མི་ཁྱབ་པ་བསྟན་པ་དེ་ཡང་རྣམ་པ་གསུམ་དུ་དབྱེའོ། །

[Block 248 [VERSE]]
དེའི་གྲངས་དང་དེའི་ཡོན་ཏན་དང་། །
དེ་དག་གི་མཚན་སོ་སོར་དབྱེ་བའོ། །

[Block 249 [HEADING]]
###### **དེའི་གྲངས།** ^4-1-5-5-3-1-0

[Block 250]
དེ་ལ༌[^319]བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་ཞེས་སྨོས་པ་དོན་རྣམ་པ་གཉིས་ཏེ། ཡེ་ཤེས་ཆེན་པོ་གཙོར་བྱས་པས་བདག་གི༌[^320]དོན་བསྟན་པ་དང་ཐུགས་རྗེ་ཆེན་པོ་གཙོར་བྱས་པས་གཞན་གྱི་དོན་བསྟན་པའོ། །
--- END BLOCKS ---
