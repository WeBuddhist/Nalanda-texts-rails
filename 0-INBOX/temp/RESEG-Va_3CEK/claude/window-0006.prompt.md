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
ཡུལ་ཆེ་གེ་མོ་ཞིག་ཏུ་ཞེས་བྱ་བ་ནི་ཡུལ་ངེས་པའོ། །

[Block 212]
ཟླ་བའི་བར་དུ་ཞེས་བྱ་བ་ནི་དུས་ངེས་པའོ། །

[Block 213]
འཐབ་མོ༌[^149]མ་གཏོགས་སོ་ཞེས་བྱ་བ་ནི་ཚེ་ངེས་པ་སྟེ། དེ་ལྟར་མནོས་ན་ལེགས་པར་སྤྱད་པ་ཙམ་དུ་ནི༌[^150]འགྱུར་རོ། །ཇི་ལྟར་ན་མི་ནུས་པ་དག་ལས་སྡོམ་པ་འཐོབ་ཅེ་ན། སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྲོག་ལ་མི་གནོད་པའི་བསམ་པས་ཁས་བླང་བའི༌[^151]ཕྱིར་རོ། །

[Block 214]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་གལ་ཏེ་ནུས་པ་དག་ཁོ་ན་ལས་སྡོམ་པ་འཐོབ་ན་ནི་སེམས་ཅན་ནུས་པ་དང་མི་ནུས་པ་རྣམས་ནི་ཕན་ཚུན་འཕོ་བས་འཕེལ་བ་དང་འགྲིབ་པ་དང་ལྡན་པར་འགྱུར་ཏེ། དེ་ལྟར་ན་འཐོབ་པ་དང་གཏོང་བའི་རྒྱུ་དག་མེད་པར་ཡང་སྡོམ་པ་འཐོབ་པ་དང་གཏོང་བར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 215]
དེ་ལྟར་ནི་མི་འགྱུར་ཏེ། ཇི་ལྟར་སྔོན་མེད་པའི་རྩྭ་ལ་སོགས་པ་སྐྱེས་སམ་བསྐམས༌[^152]ན་སྡོམ་པ་འཕེལ་བ་དང་འགྲིབ་པར༌[^153]མི་འགྱུར་བ་དེ་བཞིན་དུ་ནུས་པ་དང༌[^154]མི་ནུས་པ་འཕོས་སུ་ཟིན་ཀྱང་མི་འགྱུར་རོ། །

[Block 216]
[^155]སེམས་ཅན་རྣམས་ནི་སྔོན་ཡང་ཡོད་ལ་ཕྱིས་ཀྱང་ཡོད་པའི་ཕྱིར་ལ་རྩྭ་ལ་སོགས་པ་ནི་མེད་པའི་ཕྱིར་རོ། །

[Block 217]
འདི་ལ་དེ་ལྟར་མི་ནུས་པར་གྱུར་པ་དང་ཟད་པར་ཅི་ཞིག་ཡོད་པ༌[^156]གང་གི་ཚེ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ནས་མེད་པ་ཁོ་ནར་གྱུར་པ་དེའི་ཚེ་ཇི་ལྟར་སྡོམ་པ་འགྲིབ་པར་མི་འགྱུར་ཏེ། ལན་འདི་ནི་མི་རུང་ངོ་། །དེ་ལྟ་བས་ན་གཏན་ཚིགས་སྔ་མ་ཉིད་བཟང་ངོ་། །དེ་ལྟར་ན་འོ་ན་ནི་སྔོན་གྱི་སེམས་ཅན་ནི༌[^157]སངས་རྒྱས་སུ་གྱུར་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་རྣམས་ལས༌[^158]སངས་རྒྱས་ཕྱི་མ་རྣམས་ཀྱིས་སོ་སོར་ཐར་པའི་སྡོམ་པ་མ་ཐོབ་པའི་ཕྱིར་ཇི་ལྟར་ཚུལ་ཁྲིམས་ཉུང་བར་མི་འགྱུར་ཞེ་ན། ཐམས་ཅད་ཀྱིས་སེམས་ཅན་ཐམས་ཅད་ལས་འཐོབ་པའི༌[^159]ཕྱིར་ཏེ། གལ་ཏེ་དེ་དག་ཀྱང་ཡོད་ན་ནི་དེ་རྣམས་ཀྱིས་དེ་དག་ལས་ཀྱང་ཐོབ་པར༌[^160]འགྱུར་རོ། །

[Block 218]
སྡོམ་པ་གང་ལས་འཐོབ་པ་བཤད་ཟིན་ཏོ། །

[Block 219 [HEADING]]
### སྡོམ་པ་མ་ཡིན་པ་གང་དག་ལས་འཐོབ་པ། ^1-17-0

[Block 220 [VERSE]]
སྡོམ་པ་མིན་པས༌[^161]ཐམས་ཅད་དང་། །
ཡན་ལག་ཀུན་ལས་རྒྱུས་མིན་ནོ། །

[Block 221]
སེམས་ཅན་ཐམས་ཅད་དང་ལས་ཀྱི་ལམ་ཐམས་ཅད་ལས་འཐོབ་སྟེ། སྡོམ་པ་མ་ཡིན་པ་མ་ཚང་བའི༌[^162]སྡོམ་པ་མ་ཡིན་པ་ཅན་ནི་མེད་དོ་ཞེས་གྲག་གོ། །

[Block 222]
རྒྱུ་ཐམས་ཅད་ཀྱིས་ནི་མ་ཡིན་ཏེ། སེམས་ཆུང་ངུ་ལ་སོགས་པ་ཅིག་ཅར་དུ་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 223]
གང་ཞིག་སེམས་ཆུང་ངུས་སྡོམ་པ་མ་ཡིན་པ་འཐོབ་སྟེ། སེམས་ཆེན་པོས་སྲོག་ཆགས་ཀྱི་སྲོག་གཅོད་པར་བྱེད་ན་ཡང་སྡོམ་པ་མ་ཡིན་པ་ནི་ཆུང་ངུ་ཁོ་ན་དང༌[^163]ལྡན་ལ། སྲོག་གཅོད་པའི་རྣམ་པར་རིག་བྱེད་ནི་ཆེན་པོ་དང་ལྡན་ནོ། །

[Block 224]
དེ་བཞིན་དུ་འབྲིང་དང་ཆེན་པོ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 225]
དེ་ལ་འདི་དག་ནི་སྡོམ་པ་མ་ཡིན་པ་ཅན་ཡིན་ཏེ། འདི་ལྟ་སྟེ། ཤན་པ་རྣམས་དང་། བྱ་གག་གསོད་པ་རྣམས་དང་། ཕག་གསོད་པ་རྣམས་དང་། བྱ་པ་རྣམས་དང་། ཉ་པ་རྣམས་དང་། རི་དགས་འཆོར་བ་རྣམས་དང་། ཆོམ་རྐུན་པ་རྣམས་དང་། གཤེད་མ་རྣམས་དང་། བཙོན་རྫི་རྣམས་དང་། གླང་པོ་ཆེ་འཆོར་བ་རྣམས་དང་། ཁྱི་འཆོར་བ་རྣམས་དང་། བ་ཀུ༌[^164]རི་འཆོར་བ་རྣམས་སོ། །

[Block 226]
རྒྱལ་པོ་དང་། བློན་པོ་དང་། ཤགས་ཟིན་པོ་རྣམས་ཀྱང་དོན་གྱིས་ན་སྡོམ་པ་མ་ཡིན༌[^165]ནོ། །

[Block 227]
དེ་ལ་གནས་པས་སྡོམ་པ་མ་ཡིན་པ་ཡོད་པའི་ཕྱིར་རམ། འདི་དག་ལ་སྡོམ་པ་མ་ཡིན་པ་ཡོད་པས་ན་སྡོམ་པ་མ་ཡིན་པ་ཅན་རྣམས་སོ། །

[Block 228]
ལུག་གསོད་པས་ན་ཤན་པ་རྣམས་ཏེ། གཞན་དག་ལ་ཡང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 229]
རེ་ཞིག་སྡོམ་པ་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པའི་བསམ་པས་ཞེས་སྨོས་པས་སེམས་ཅན་ཐམས་ཅད་ལས་ཐོབ་པར༌[^166]ཡང་རིགས་ན། ཤན་པ་ལ་སོགས་པར༌[^167]ཕ་དང་མ་དང་བུ་དང་བྲན་ལ་སོགས་པ་ལ་ལོག་པར་མ་ཞུགས་པའི་བསམ་པ་ཅན་འཚོ་བའི་ཕྱིར་ཡང་གསོད་པར་མི་འདོད་པ་རྣམས་གོ་ཇི་ལྟར་སེམས་ཅན་ཐམས་ཅད་ལས་སྡོམ་པ་མ་ཡིན་པ་འཐོབ་པར་རུང་། དེ་དག་ནི་མ་ལ་སོགས་པ་ལུག་ཏུ་གྱུར་པ་ཡང་གསོད་དོ། །

[Block 230]
རེ་ཞིག་དེ་དག་ཉིད༌[^168]ཡིན་པར་ཤེས་ནས་ནི་མི་གསོད་དོ། །

[Block 231]
[^169]འཕགས་མར་གྱུར་པ་རྣམས་ལ༌[^170]ཡང་ཕྱུགས་སུ་གྱུར་པའི༌[^171]གོ་སྐབས་མེད་ན་ཇི་ལྟར་ན༌[^172]དེ་དག་ལས་སྡོམ་པ་མ་ཡིན་པ་འཐོབ། གལ་ཏེ་མ་འོངས་པའི་ལུས་ལ་ལྟོས༌[^173]ཏེ་ད་ལྟར་གྱི་ལས་སྡོམ་པ་མ་ཡིན་པ་ཞིག་ཏུ་འགྱུར་ན་ནི་དེ་དག་ལུག་བུར་གྱུར་པ་རྣམས་ཀྱང་གཏན་མི་གསོད་པས་དེ་དག་ལས་སྡོམ་པ་མ་ཡིན་པར་མི་འགྱུར་རོ། །

[Block 232]
ཇི་ལྟར་ན་གསོད་པར་འདོད་བཞིན་དུ་དེ་དག་ལས་སྡོམ་པ་མ་ཡིན་པར་མི་འགྱུར། དེ་ནི་མ་ལ་སོགས་པ་ལ་ཡང་མཚུངས་ཏེ། ཇི་ལྟར་ན་གསོད་པར་མི་འདོད་བཞིན་དུ་དེ་དག་ལས་སྡོམ་པ་མ་ཡིན༌[^174]པར་འགྱུར། ཤན་པ་གང་ཞིག་ཚེར་ཡང་མ་བྱིན་པར༌[^175]མི་ལེན། རང་གི་ཆུང་མས་ཀྱང་ཆོག་ཤེས། ལྐུགས་པ་ཡང་ཡིན་ན་ཇི་ལྟར་ན་དེ་ཡན་ལག་ཐམས་ཅད་ལས་སྡོམ་པ་མ་ཡིན་པར་འགྱུར། བསམ་པ་ལོག་པར་ཞུགས་པའི་ཕྱིར་ཏེ། ལྐུགས་བཞིན་དུ་ངག་གིས་ཐོབ་པར་བྱ་བའི་དོན་ལུས་ཀྱིས་འཐོབ༌[^176]པར་ནུས་སོ། །

[Block 233]
འོ་ན་གང་ཞིག་གིས་བསླབ་པའི་གནས་གཉིས་སམ་གསུམ་ཞིག་ཡང་དག་པར་བླངས་ན་ཇི་ལྟ་བུར་འགྱུར། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་སྡོམ་པ་མ་ཡིན་པ་ལ་མ་ཚང་བ་དང་ཉི་ཚེ་བ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 234]
མདོ་སྡེ་པ་རྣམས་ན་རེ༌[^177]ནི་ཇི་ལྟར་ཁས་བླངས་པ་བཞིན་དུ་སྡོམ་པ་མ་ཡིན་པ་དང་རྣམ་པ་བརྒྱད་མ་གཏོགས་པ་སྡོམ་པ་ཡང་མ་ཚང་བ་ཡོད་ལ་ཉི་ཚེ་བ་ཡང༌[^178]ཡོད་དེ་ཚུལ་ཁྲིམས་དང་འཆལ་བའི་ཚུལ་ཁྲིམས་དེ་ཙམ་གྱིས༌[^179]གེགས་བྱེད་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 235]
སྡོམ་པ་མ་ཡིན་པ་གང་དག་ལས་འཐོབ་པ་དེ་ནི་བཤད་ཟིན་ཏོ། །

[Block 236 [HEADING]]
### སྡོམ་པ་མ་ཡིན་པ་ཇི་ལྟར་འཐོབ་པ། ^1-18-0

[Block 237 [VERSE]]
ཇི་ལྟར་འཐོབ་པ་མ་བཤད་པས། །
དེའི་ཕྱིར་འདི་བརྗོད་པར་བྱ་སྟེ།
སྡོམ་པ་མིན་པ་བྱ་བ་འམ། །
ཁས་ལེན་པ་ལས་འཐོབ་པར་འགྱུར། །

[Block 238]
སྡོམ་པ་མ་ཡིན་པ་ནི་རྒྱུ་རྣམ་པ་གཉིས་ཀྱིས་འཐོབ་སྟེ། དེའི་རིགས་སུ་སྐྱེས་པ་རྣམས་ནི་གསོད་པར་སྦྱོར་བའི་བྱ་བ་ལས་སོ། །

[Block 239]
གཞན་གྱི་རིགས་སུ་སྐྱེས་པ་རྣམས་ནི་བདག་ཅག་ཀྱང་འཚོ་བ་འདིས་འཚོ་བར༌[^180]བྱའོ་ཞེས་ཁས་ལེན་པ་ལས་སོ། །

[Block 240 [HEADING]]
### ལྷག་མའི་རྣམ་རིག་མིན་འཐོབ་པ། ^1-19-0

[Block 241 [VERSE]]
ལྷག་མའི་རྣམ་རིག་མིན་ཞིང༌[^181]དང་། །
ལེན་དང་གུས་པར་བྱེད་པས་འཐོབ། །

[Block 242]
གང་དུ་ཀུན་དགའི༌[^182]ར་བ་ལ་སོགས་པ་ཕུལ་བ་ཙམ་གྱིས་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྐྱེ་བར་འགྱུར་བ་དེ་ལྟ་བུའི་ཞིང་ཡང་ཡོད་དེ། འདི་ལྟ་སྟེ། རྫས་ལས་བྱུང་བའི་བསོད་ནམས་བྱ་བའི་དངོས་པོ་དག་ལྟ་བུའོ། །

[Block 243]
ཡང་ན༌[^183]སངས་རྒྱས་ལ་ཕྱག་མ་འཚལ་གྱི་བར་དུ་ཟས་མི་བཟའོ།[^184] །ཚེས་སམ་ཟླ་བ་གཅིག་གམ་ཟླ་བ་ཕྱེད་ཅིང་རྟག་ཏུ་ཟས་དག་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའི་ཡི་དམ་བཅས་པའམ། དགེ་བ་འམ་མི་དགེ་བ་གང་ལས་འདིའི་རྣམ་པར་རིག་བྱེད་མ་ཡིན་པ་སྐྱེ་བར་འགྱུར་བ་དེ་ལྟ་བུའི་གུས་པས་ལས་བྱེད་པ་ལས་སོ། །

[Block 244]
སྡོམ་པ་དང་སྡོམ་པ་མ་ཡིན་པ་རྣམས་ཇི་ལྟར་འཐོབ་པ་འདི་ནི་བཤད་ཟིན་ཏོ། །

[Block 245 [HEADING]]
### གཏོང་བ། ^1-20-0

[Block 246]
ད་ནི་གཏོང་བ་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་རེ་ཞིག །

[Block 247 [HEADING]]
#### སོ་སོར་ཐར་པའི་འདུལ་བ་གཏོང་བ། ^1-20-1-0

[Block 248 [VERSE]]
བསླབ་པ་ཕུལ་དང་ཤི་འཕོས་དང་། །
མཚན་ཉིད༌[^185]དག་ནི་བྱུང་བ་དང་། །
རྩ་བ་ཆད་དང་མཚན་འདས་ལས། །
སོ་སོར་ཐར་པའི་འདུལ་བ་གཏོང་། །

[Block 249]
འདིས་འདུལ་བར་བྱེད་པས་ན༌[^186]འདུལ་བ་སྟེ། དེས་དབང་པོ་འདུལ་བར་བྱེད་པའི་ཕྱིར་སོ་སོར་ཐར་པའི་སྡོམ་པ་ཡིན་པར་དགོངས་པའོ། །

[Block 250]
བསྙེན་གནས་མ་གཏོགས་པའི་སོ་སོར་ཐར་པའི་སྡོམ་པ་ནི་རྒྱུ་རྣམ་པ་བཞིས་གཏོང་བར༌[^187]འགྱུར་ཏེ། མི་བརྡ་ཕྲད་པའི་དྲུང་དུ་བསླབ་པའི་གཞི་རྣམས་བསམ་པ་ཐག་པ་ནས་སླར་ཕུལ་བ་དང་། རིས་མཐུན་པ་བཏང་བ་དང་། མཚན་ཉིད༌[^188]ཅིག་ཅར་དུ་འབྱུང་བ་དང་། དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པ་ལས་སོ། །
--- END BLOCKS ---
