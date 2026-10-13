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
གཞན་ཡང་བློ་དབང་ཐ་དད་ལས་ཐ་དད། །གང་ལ་གཅིག་ཡིན་གཞན་དུ་ན། །དབང་པོ་ཡང་ཐ་དད་བློ་ཡང་ཐ་དད་པ་ལས་གཞན་ཉིད་དུ་མི་བརྗོད་པར་འགྱུར་རོ། །

[Block 212]
དབང་པོ་ཡང་ཐ་དད་བློ་ཡང་ཐ་དད་པ་དེ་ལ་ནི་གཅིག་ཉིད་ཡིན་ནོ་ཞེས་པའི་གོ་སྐབས་མེད་དོ། །

[Block 213]
དེ་དག་གི་ཡོན་ཏན་ལ་སོགས་པ་ལ་མངོན་སུམ་གྱིས༌[^163]ཤེས་པ་སྐྱེ་བ་ལ་ཡང་གསལ་བར་རིག་པར་བྱའོ། །

[Block 214]
དེ་དག་གིས་ནི་རང་གི་རྟེན་དང་འབྲེལ་བའི་སྒོ་ནས་གཞི་ལ་སོགས་པ་དང་ཕྲད་པ་ཉིད་བརྗོད་པ་ཡིན་ཏེ། དེ་ལྟ་ན་ཡང་ཐམས་ཅད་དུ་ཕྲད་པ་ལས་ཤེས་པ་སྐྱེ་བ་ནི་མ་ཡིན་ནོ་ཞེས་རིགས་པ་ཅན་གྱིས་མངོན་སུམ་བརྟགས་པར་ཇི་ལྟ་བ་བཞིན་དུ་བརྗོད་ཟིན་ཏོ། །

[Block 215]
དེའི་ཕྱིར་བྱེ་བྲག་པའི་མངོན་སུམ་ནི་སྒྲུབ་པར་དཀའོ། །

[Block 216 [HEADING]]
#### གྲངས་ཅན་གྱི་མངོན་སུམ། ^1-4-4-0

[Block 217]
སེར་སྐྱ་བ་རྣམས་ཀྱིས་ནི་རྣ་བ་ལ་སོགས་པའི་འཇུག་པ་མངོན་སུམ་དུ་འདོད་དོ། །

[Block 218]
རྣ་བ་དང་པགས་པ་དང་མིག་དང་ལྕེ་དང་སྣ་རྣམས་ཡིད་ཀྱིས་བྱིན་གྱིས་བརླབས་ནས་ཡུལ་ལ་འཇུག་པ་སྟེ། སྒྲ་དང་རེག་བྱ་དང་གཟུགས་དང་རོ་དང་དྲི་ད་ལྟར་བ་རྣམས་ལ་གོ་རིམས་བཞིན་དུ་འཛིན་པ་ནི་མངོན་སུམ་གྱི་ཚད་མའོ་ཞེས་སོ། །

[Block 219]
དེ་དག་གི་ལྟར་ན་ཡང་དབང་པོ་རྣམས་ཀྱི་ཐུག་པ་མེད་པའམ། དེ་དག་གིས་ནི་དབང་པོ་གཞན་གྱི་གཟུང་བྱ་ཡུལ་མ་ཡིན་པ་ཉིད་ཀྱིས་རང་གི་ཡུལ་ལ་འཇུག་པའི་དབང་པོ༌[^164]འདོད་པ་ཡིན་ལ་ཡོན་ཏན་གསུམ་གྱི་འཕེལ་བ་དང་འགྲིབ་པ་ཙམ་གྱིས་ཐ་དད་ལས་སྒྲ་ལ་སོགས་པའི་རིགས་ཐ་དད་ཅེས་འདོད་དེ། སྒྲ་གཅིག་པུ་ཡང་ཡོན་ཏན་གྱི་འཕེལ་འགྲིབ་ཀྱི་ཐ་དད་ཀྱིས་ཐུག་པ་མེད་པའི་ཕྱིར་དབང་པོ་དཔག་ཏུ་མེད་པས་འཛིན་པར༌[^165]ཁས་བླང་བར་བྱའོ། །

[Block 220]
ཡང་ན་དབང་གཅིག་འགྱུར། ཅི་སྟེ་དེར་ཡོན་ཏན་གསུམ་ཐ་མི་དད་པས་རིགས་གཅིག་ཉིད་ཡིན་ན་ནི་དེ་ལྟར་ན་སྒྲ་ཐ་དད་འཛིན་པ་བཞིན་རེག་པ་ལ་སོགས་པའང་འཛིན་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་དབང་པོ་གཅིག་ཉིད་དུ་འགྱུར་ཏེ། ཐམས་ཅད་དུ་ཡོན་ཏན་གསུམ་པོ་ཐ་མི་དད་པའི༌[^166]ཕྱིར་རོ། །

[Block 221]
ཡོན་ཏན་གསུམ་དང་བྲལ་བའི་སྒྲའི་རིགས་ནི་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 222]
གང་སྒྲ་ཉིད་དུ་གྱུར་པ་དེ་ནི་རེག་བྱ་ལ་སོགས་པ་ལ་མ་ཡིན་ནོ། །

[Block 223]
གང་གི་ཚེ་སྙིང་སྟོབས་ལ་སོགས་པའི་དབྱིབས་ཀྱིས་གནས་སྐབས་ཀྱི༌[^167]ཐ་དད་ཀྱི་སྒྲ་ལ་སོགས་པ་དག༌[^168]ཐ་དད་པ་ཇི་ལྟར་མེད། སྒྲའི་རིགས་ཐ་མི་དད་པར་མཚུངས་པའི་དབྱིབས་ཀྱི་གནས་སྐབས་ནི་ཡོད་པ་ཡིན་ལ། རེག་པ་ལ་སོགས་རྣམས་ལས་ཐ་དད་པ་སྟེ། རིགས་མཐུན་པའི་གཟུང་བར་བྱ་བའི་ཡུལ་ལ་རྣ་བ་འཇུག་པ་ཡིན་ནོ། །

[Block 224]
དེ་བཞིན་དུ་རེག་པ་ལ་སོགས་པ་ལ་ཡང་ངོ་། །དེའི་ཕྱིར་ཇི་སྐད་དུ་བརྗོད་པའི་སྐྱོན་དུ་ཐལ་བར་འགྱུར་རོ༌[^169]ཞེ་ན། དེ་ལྟ་ན་ཡང་རེག་བྱ་ནི་མིག་གི༌[^170]མཐུན་པའི་ཡུལ་དུ་འགྱུར་ཏེ། །གང་ཕྱིར་དབྱིབས་ནི་གཉིས་ཀྱི་གཟུང་བྱར༌[^171]རི་བོ་ལ་སོགས་པའི་དབྱིབས་ལ་མིག་དང་རེག་བྱ་དག་གི་ཤེས་པ་མཐོང་བའི་ཕྱིར་རང་གི་ཡུལ་དེ་ཁོ་ནར་འཇུག་གོ་ཞེས་པ་ནི་རྣམ་པར་གསལ་ཏེ། [^172]དབྱིབས་ཀྱིས་བྱས་པའི་རིགས་ཀྱི་བྱེ་བྲག་འདོད་པའི་ལྟར་ན་ནི་སྒྲ་ལ་སོགས་པ་ནི་རྣ་བ་ལ་སོགས་པས༌[^173]མི་འཛིན་པར་འགྱུར་ཏེ། གང་གི་ཕྱིར་ཞེ་ན། དབྱིབས་ནི་གསུམ་གྱི་སྤྱོད་ཡུལ་མིན། །དབྱིབས་ནི་རྣ་བ་དང་སྣ་དང་ལྕེ་རྣམས་ཀྱིས་གཟུང་བར་བྱ་བ་མ་ཡིན་པས། མཐོང་བཞིན་པའི་སྒྲ་དང་དྲི་དང་རོ་རྣམས་མངོན་སུམ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 225]
ཡུལ་གཅིག་ལ་དབྱིབས་མང་པོ་འཐོབ་པར་ཡང་འགྱུར་ཏེ། དབང་པོ་གཅིག་གི་ཡུལ་གྱི་དབྱེ་བ་ཡོད་ན་ནི་དེའི་བྱེ་བྲག་གི་རིགས་དུ་མ་ཡོད་པའི་ཕྱིར་ཡུལ་གཅིག་ཏུ་དབྱིབས་དུ་མ་མཐོང་བར་འགྱུར་རོ། །

[Block 226]
དབྱིབས་རྣམས་ལ་ཁྱད་པར་མེད་པར་མཚུངས་པའི་ཕྱིར་གསེར་ལ་སོགས་པའི་སྐྱོགས་རྣམས་དང་རྒྱན་རྣམས་ཀྱི་ཐ་དད་ཀྱང༌[^174]མེད་པར་འགྱུར་རོ། །

[Block 227]
དབྱིབས་མཚུངས་པར་ཡོད་པའི་ཕྱིར་གསེར་དང་སྒྲ་དང་སྙིང་སྟོབས་དང༌[^175]རྫས་ལ་སོགས་པ་རྣམས་ཀྱང་མཚུངས་པར་འགྱུར་རོ། །

[Block 228]
དེ་བཞིན་དུ་རང་རང་གི་ཡུལ་ལ་འཇུག་པ་ཡང་མི་འགྱུར། ཅི་དབང་པོའི་འཇུག་པས་རིགས་རང་ཙམ་འཛིན་པར་བྱེད་དམ། བདེ་བ་ལ་སོགས་པས༌[^176]ཁྱད་པར་དུ་བྱས་པའི་རིགས་འཛིན་པར་བྱེད། གལ་ཏེ་རིགས་རང་ཙམ་འཛིན་ན་ནི་དོན་གྱི་རང་བཞིན་འཛིན་པར་མི་འགྱུར་ཏེ། དེས་ནི་དབྱིབས་ཙམ་འཛིན་པ་ཡིན་པས་ན་སྒྲ་ལ་སོགས་པ་རྣམས་ཀྱི་བདེ་བ་ལ་སོགས་པའི་རང་བཞིན་མ་ངེས་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 229]
དབྱིབས་ཙམ་འཛིན་པ་ཉིད་ཡིན་ནོ། །

[Block 230]
དོན་གྱི་བྱེ་བྲག་འཛིན་པར་མི་འགྱུར་ཏེ། གང་གི༌[^177]དབྱིབས་ཙམ་གྱི་སྣང་བ་ཅུང་ཟད་ལ་དམིགས་ཀྱི་དོན་ཡུལ་གྱི་རང་གི་ངོ་བོ་ལ་མི་དམིགས་པས་སོ། །

[Block 231]
སྒྲ་ལ་སོགས་པའི་བྱེ་བྲག་ཀྱང་མི་འཛིན་པར་འགྱུར་རོ། །

[Block 232]
དེ་བཞིན་དུ་པི་ཝང་གི་སྒྲ་དང་རྔའི་སྒྲ་ཞེས་བྱ་བ་ལ་སོགས་པའི་བྱེ་བྲག་ཀྱང་མི་འཛིན་པར་འགྱུར་ཏེ། དེ༌[^178]དབྱིབས་གཞན་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 233]
དོན་འཛིན་ནོ་ཞེ་ན་ཡང་། ཡིད་བཞིན་རྣམ་པར་རྟོག་པ་ཡིན། །རང་གི་དོན་ཁྱད་པར་ཅན་དུ་བྱེད་ན་ཡང་ཁྱད་པར་དེ་འཛིན་པ་ན་ཡིད་ཀྱི་འཇུག་པ་བཞིན་དུ་རང་གི་ཡུལ་ལ་རྟོག་པ་དང་བཅས་པར་འགྱུར་རོ། །

[Block 234]
ཅི་སྟེ་བདེ་བ་ལ་སོགས་པས་ཁྱད་པར་དུ་བྱས་པའི་དབྱིབས་འཛིན༌[^179]ནི། དེ་ལྟ་ན་ཡང་གནས་སྐབས་དེའི་ཡིད་ཀྱི་འཇུག་པ་བཞིན་དུ་རྣམ་པར་རྟོག་པ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 235]
བདེ་བ་ལ་སོགས་པ་ཡང་སོ་སོར་འཛིན་པར་བྱེད་དམ། སྡོམ་པ་ཡང་འཛིན་པར་འགྱུར་གྲང་། དེ་ལ་རེ་ཞིག་སོ་སོར་ནི་མི་འཛིན་ཏེ། རང་གི་ཡུལ་ལ་འཛིན་པ་ལ་སོགས་པའི་དབང་པོའི་འཇུག་པ་ནི་སྒྲ་ལ་སོགས་པའི་གཟུང་བར་བྱ་བ་ལ་ཡིན་གྱི། སྙིང་སྟོབས་ལ་སོགས་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 236]
སྙིང་སྟོབས་ལ་སོགས་པ་དང་སྒྲ་ལ་སོགས་པའི་རང་བཞིན་སོ་སོ་ནི་མ་ཡིན་ནོ། །

[Block 237]
དེའི་ཕྱིར་དེ་དག་རྣམས་རྣ་བ་ལ་སོགས་པའི་འཇུག་པའི་གཟུང་བར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 238]
གཞན་མིན་ཞེ་ན། སྙིང་སྟོབས་ལ་སོགས་པ་སྒྲ་ལ་སོགས་པ་ལས་གཞན་ཉིད་ནི་མ་ཡིན་ཏེ། དེ་ཡང་གཟུང་བར་བྱ་བ་ཡིན་ནོ༌[^180]ཞེ་ན། འབྲས་མིན་པའམ། གལ་ཏེ་སྙིང་སྟོབས་ལ་སོགས་པ་སྒྲ་ལས་གཞན་མ་ཡིན་ན་ནི་ཐ་མི་དད་ཀྱི་ལུས་ཀྱི་སྒྲ་ལ་སོགས་པ་འབྲས་བུ་མ་ཡིན་ལ། སྙིང་སྟོབས་ལ་སོགས་པ་ལ༌[^181]ཡང་སྒྲ་ལ་སོགས་པའི་རྒྱུ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 239]
སྙིང་སྟོབས་སྒྲའི་རང་བཞིན་དུ་རྣམ་པར་གཞག་པར༌[^182]བྱས་ནས་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་བརྗོད་པ་དེ་ཡང་འགལ་བར་འགྱུར་རོ། །

[Block 240]
སྙིང་སྟོབས་ལ་སོགས་པ་ཕན་ཚུན་ཐ་མི་དད་དེ་སྒྲ་ལ་སོགས་པ་དང་གཅིག་པ་ཉིད་དུ་འགྱུར་ན་ནི་ཐ་མི་དད་ཀྱི་རང་བཞིན་ཡིན་པས་རྒྱུ་དང་འབྲས་བུ་དག་ཏུ་འདོད་པ་ལ་གནོད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་འམ་ཞེས་བརྟག་པའི་སྒྲའི་དོན་ཡིན་ནོ། །

[Block 241]
གཞན་ཡང་། གཞན་ཉིད་མིན་ན་གཟུང་བྱ་མིན། །གལ་ཏེ་ཡང་བདེ་བ་ལ་སོགས་པ་སྒྲ་ལ་སོགས་པ་ལས༌[^183]གཞན་མ་ཡིན་པ་དེ་ལྟ་ན་ནི་སོ་སོར་གཟུང་བར་བྱ་བར་མི་འགྱུར་ལ།[^184] རྡུལ་ཕྲ་རབ་ཀྱང་གཟུང་བར་བྱ་བར་མི་འགྱུར་ཞིང་དེ་ལ༌[^185]ཙམ་ལ་སོགས་པ་ཡང་ངོ་། །གང་དོན་གཞན་མ་ཡིན་པའི་དབང་པོའི་ཡུལ་དེ་ཐམས་ཅད་དབང་པོའི་ཡུལ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 242]
འབྲས་བུ་ཉིད་ལ་སོགས་པར་འཛིན་པ་ནི་སྤྱིའི་ཡུལ་ཅན་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 243]
དེ་ལྟར་ན་རེ་ཞིག་སོ་སོར་ནི༌[^186]མི་འཛིན་ཏོ། །

[Block 244]
ཅི་སྟེ་སྡོམ་པ༌[^187]ལ་འཛིན་ན་ནི་དེ་ལྟ་ན་ཡང་དབང་པོ་ཐམས་ཅད་འཇུག་པར་འགྱུར་ཏེ་སྣ་ཚོགས་རྣམ་པར་རོ། །

[Block 245]
སྣ་ཚོགས་ཀྱི་རྣམ་པའི་གཟུང་བྱ་ལ་ཐ་མི་དད་པའི་རྣམ་པར་འཛིན་པ་ནི་འཐད་པ་མ་ཡིན་ཏེ། དེའི་དབང་གིས༌[^188]གཟུང་བར་བྱ་བ་ཡོངས་སུ་བཅད་པའི་ཕྱིར་རོ། །

[Block 246]
སྒྲ་ལ་སོགས་པ་ལ་ཐ་མི་དད་པར་འཛིན་པ་ཡང་མཐོང་ངོ་། །བདེ་བ་ལ་སོགས་པའི་ཡུལ་ཉིད་ཀྱང་མཚུངས་པར་འགྱུར། [^189]དབང་པོ་རྣམས་ཀྱི་ཡུལ་ཉིད༌[^190]མཚུངས་པར་འགྱུར་རོ། །

[Block 247]
དབང་པོ་རྣམས་རང་གི་ཡུལ་ལ་འཇུག་པར་མི་འགྱུར་ཏེ་བདེ་བ་ལ་སོགས་པ་ཡུལ་གཞན་ལ་རིགས་ཀྱི་བྱེ་བྲག་ཡོད་པའི་ཕྱིར་རོ། །

[Block 248]
དེ་ལྟ་ན་ཡང་དབང་པོ་གཅིག་ཉིད་དུ་ཐལ་པར་འགྱུར་རོ། །

[Block 249]
མ་ཡིན་ཏེ་རང་རང་གི་དབྱིབས་ཀྱིས་ཁྱད་པར་དུ་བྱས་པ་འཛིན་ནོ་ཞེས་བརྗོད་དོ་ཞེ་ན། དེ་སྐད་དུ་ནི་བརྗོད་ན་རིགས་པར་ནི་མི༌[^191]བརྗོད་དེ། གང་གི་ཕྱིར་དུ་མར་འཛིན་ཕྱིར་གཟུགས་ཀྱི་རིགས་གཅིག་ལ་ཡང་དབྱིབས་ཐ་དད་ཀྱི་སྒོ་ནས་དུ་མར་འཛིན་པར་བྱེད་པ༌[^192]ཡིན་གྱི་དབྱིབས་གཅིག་གི༌[^193]རྗེས་སུ་ཞུགས་ནས་འཛིན་པ་ནི་མ་མཐོང་ངོ་། །དེར་དབྱིབས་ཀྱི་ཐ་དད་ལས་རིགས་ཀྱི་ཐ་དད་འདོད་ན་ནི་དེ་ཉིད་དབང་པོ་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་བ་ཡིན་ནོ། །

[Block 250]
འདི་ལ༌[^194]ནི་གྲངས་ཅན་གྱི་བྱེ་བྲག་ལ༌[^195]ལས་མི་འདོད་དོ། །
--- END BLOCKS ---
