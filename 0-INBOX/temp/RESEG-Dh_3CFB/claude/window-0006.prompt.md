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
སྲིད་ཀྱང་ཁྱད་པར་རྣམས་བལྟ་བར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 212]
དེ་ལྟ་བུ་དག་ནི་སྤང་བར་འོས་པ་ཡང་མ་ཡིན་ནོ། །

[Block 213]
ཚིག་རྣམས་ནི༌[^136]དེ་ལྟ་བུ་མ་ཡིན་ཏེ། ཁྱད་པར་བལྟར་རུང་བའི་ཕྱིར་རོ། །

[Block 214]
བལྟར་མི་རུང་བ་ཞིག༌[^137]ཡིན་ན་ཡང་ཁྱད་པར་མ་མཐོང་བ་རྣམས་རིགས་མི་མཐུན་པ་ཉིད་དུ་ཁས་ལེན་པ་འགལ་བའི་ཕྱིར་རོ། །

[Block 215]
དེའི་ཁྱད་པར་རྣམས་ནི་གཞན་ལ་ཡང་བྱ་བར་ནུས་པའི་ཕྱིར་རོ། །

[Block 216]
སྒྲ་མངོན་སུམ་པ་རྣམས་ལ་མངོན་སུམ་མ་ཡིན་པའི་ངོ་བོ་ཉིད་མེད་པའི་ཡང་ཕྱིར་རོ། །

[Block 217]
འཁྲུལ་པའི་རྒྱུ་མཚན་མེད་པའི་ཕྱིར་ཏེ། གནོད་པར་བྱེད་པ་མེད་པས་འཁྲུལ་པ་མི་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 218]
སྐྱེས་བུ་དག་ནི་ཁྱད་པར་མཐོང་བ་གནོད་པར་བྱེད་པ་ཡིན་པའི་ཕྱིར་མཚུངས་པ་མ་ཡིན་ནོ། །

[Block 219]
ཚིག་གི་ཁྱད་པར་གཞན་གྱི་ངོ་བོར་གྱུར་པ་ནི་དེའི་ཁྱད་པར་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 220]
དེའི་ཕྱིར༌[^138]ཁྱད་པར་མེད་པའི་རང་བཞིན་ཐམས་ཅད་སྐྱེས་བུས་བྱེད་དོ། །

[Block 221]
ཡང་ན་ནི་འགའ་ཡང་མ་ཡིན་ནོ། །

[Block 222]
གཞན་ཡང་། །

[Block 223 [VERSE]]
བདག་དང་ས་ལ་ཤེས་ཡོད་སོགས། །
མེད་པ་རབ་སྒྲུབ་བྱེད་མིན་པའི། །
མི་དམིགས་གང་ཡིན་དེ་ཁོ་ན། །
གཏན་ཚིགས་མེད་སྒྲུབ་ཡིན་ནམ་ཅི། །

[Block 224]
མི་དམིགས་པ་ཚད་མར་བྱེད་པ་འདིའི་བདག་དངོས་སུ་སྨྲ་བ་ཡང་དམིགས་པ་མེད་པར་འགྱུར་ཏེ། བདག་མངོན་སུམ་མ་ཡིན་པའི་ཕྱིར་དང་། འབྲས་བུ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 225]
དབང་པོ་ལ་སོགས་པ་ནི་འབྲས་བུ་རྣམ་པར་ཤེས་པ་རེས་འགག་པ༌[^139]ཡིན་པའི་ཕྱིར་ལྟོས་པ་དང་བཅས་པ་ཉིད་དུ་གྲུབ་པས་རབ་ཏུ་འགྲུབ་པར་བརྗོད་དེ། འདི་ལ་རྒྱུ་ཅི་ཞིག་ཡོད་དོ༌[^140]ཞེས་བྱ་བ་ཡིན་གྱི་འདི་ལྟ་བུར་གྱུར་བ་ཞིག་གོ་ཞེས་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 226]
འབྲས་བུ་བདེ་བ་ལ་སོགས་པ་རབ་ཏུ་བསྒྲུབས་པ་ནི་དེ་ལྟར་དོན་ཅུང་ཟད་ཀྱང་རྒྱས་པར་མི་བྱེད་དེ། [^141]གང་ཡང་རུང་བས་རྒྱུ་དང་ལྡན་པར་ཁས༌[^142]བླངས་པའི་ཕྱིར་རོ། །

[Block 227]
དེ་ལྟ་ཡིན་དང་། བདག་མི་དམིགས་པ་ཁོ་ནར་འགྱུར་ན། དེས་དེ་སེལ་བ་ན་ཅི་སྟེ་མི་དམིགས་པ་བསྒྲུབ་པ༌[^143]མ་ཡིན་ནོ་ཞེས་བསལ། ལྡོག་པ་ཇི་ལྟར་སྒྲུབ་པར་བྱེད། །ཡང་ལ་ལ་ནི་ས་ལ་ཤེས་པ་ཡོད་པར་མི་དམིགས་པར་འདོད་བཞིན་དུ་ཡང་མ་མཐོང་བས་ཚིག་ལ་སོགས་པ་ལྡོག་པར་སྨྲའོ། །

[Block 228]
གཞན་ནི་འོ་མ་ལ་སོགས་པ་ཞོ་ལ་སོགས་པ་སྟེ། གཞན་གྱི་དོན་མ་ཡིན་པ་དག་ལ་འདུས་པ་ཉིད་མ་མཐོང་བས་ལྡོག་པའོ། །

[Block 229]
འདི་ལ་འདུས་པ་དག་ནི་གདོན་མི་ཟ་བར་གཞན་གྱི་དོན་ཡིན་པར་འགྱུར་རོ། །ཞེས་བྱ་བའི་ངེས་པ་ཅི་ཞིག་ཡོད། འོ་མ་ལ་སོགས་པ་ལ་ཞོ་ལ་སོགས་པ་དམིགས་པ་རྗེས་སུ་དཔག་པ་ཁོ་ན་སྟེ། མི་ནུས་པ་ལས་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 230]
ཞེ་ན། ཡང་ནུས་པ་འདི་ཅི་ཡིན། ཅི་ཡོད་པ་དེ་ཉིད་ཡིན་ནམ།

[Block 231]
འོན་ཏེ་གཞན་ཉིད་ཅུང་ཟད་ཅིག་ཡིན། །གལ་ཏེ་དེ་ཉིད་ཡིན་ན་ནི། །

[Block 232]
དེ་ཁོ་ན་བཞིན་དུ་དམིགས་པར་འགྱུར་ཏེ། ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །ཅི་སྟེ་གཞན་ཞིག་ཡིན་ནོ་ཞེ་ན། ཇི་ལྟར་གཞན་ཡོད་ན་དེ་ཡོད་དེ། ཉེ་བར་གདགས་པ་ཙམ་དུ་ནི་འགྱུར་རོ། །

[Block 233]
འདི་ནི་འདི་དག་གི་ཕན་ཚུན་འགལ་བ་ཡིན་ནོ། །

[Block 234 [VERSE]]
དེ༌[^144]ཕྱིར་དེ་ཙམ་དང་འབྲེལ་པའི། །
ངོ་བོ་ཉིད་ཀྱིས་ངོ་བོ་ཉིད། །

[Block 235]
བཟློག་པར་འགྱུར་བའམ། དཔེར་ན་ཤིང་གིས་ཤིང་ཤ་པ་ལྟ་བུ་སྟེ། ཡལ་ག་ལ་སོགས་པ་དང་ལྡན་པའི་ཁྱད་པར་འགའ་ཁོ་ན་ཞིག་ལ་དེ་སྐད་དུ་གྲགས་པའི་ཕྱིར་དེ་ནི་དེའི་རང་གི་ངོ་བོ་ཡིན་ནོ། །

[Block 236]
རང་གི་ངོ་བོ་ཡོངས་སུ་བོར་ནས་ཀྱང་ཇི་ལྟར་ཡོད་པར་འགྱུར་ཏེ། རང་གི་ངོ་བོ་ཁོ་ན་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 237]
དེའི་ཕྱིར་དེ་ནི་རང་བཞིན་འབྲེལ་པའི་ཕྱིར་འཁྲུལ་པ་མེད་དོ། །

[Block 238]
རྒྱུ་ཡིས་ནི། འབྲས་བུ་འཁྲུལ་པ་མེད་པའི་ཕྱིར། །རྒྱུ་ལྡོག་པ་ལས་འབྲས་བུ་ལྡོག་པར་བྱེད་དོ། །

[Block 239]
གཞན་དུ་ན་དེ་ནི་དེའི་འབྲས་བུ་ཉིད་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 240]
རྒྱུ་དང་འབྲས་བུའི་ངོ་བོ་གྲུབ་པ་ནི་ངོ་བོ་ཉིད་ངེས་པར་བྱེད་དེ། དེ་བས་ན་གཉི་ག་རང་བཞིན་འབྲེལ་པ་ཁོ་ནས་ལྡོག་གོ། །

[Block 241 [VERSE]]
དེ་ལྟ་མིན༌[^145]ན་གཅིག་ལོག་པས། །
ཇི་ལྟར་གཞན་ནི་ལྡོག་པར་འགྱུར། །
མི་ལ་རྟ་མི༌[^146]བདོག་ཅེས་ཏེ། །
ཕྱུགས་ཀྱང་བདོག་པ་མིན་ནམ་ཅི། །

[Block 242 [VERSE]]
དེ་བཞིན་གཅིག་ཅིག་ཉེ་བའི་ཕྱིར། །
ཇི་ལྟར་གཞན་ནི་ཉེ་བར་འགྱུར། །
མི་ལ་ཕྱུགས་ནི་བདོག་ཅེས་ཏེ། །
དེ་བཞིན་རྟ་ཡང་བདོག་གམ་ཅི། །

[Block 243]
དེའི་ཕྱིར་རང་བཞིན་འབྲེལ་པ་ཁོ་ནས་གཏན་ཚིགས་ཀྱིས་བསྒྲུབ་པར་བྱ་བ་གོ་བར་བྱེད་དོ། །

[Block 244]
དེའི་ངོ་བོའི་མཚན་ཉིད་དམ། །དེ་ལས་བྱུང་བའི་མཚན་ཉིད་ཡིན་ནོ། །

[Block 245]
མེད་ན་མི་འབྱུང་བ་ཉིད་དཔེ་དེ་དག་གིས་རབ་ཏུ་སྟོན་ཏོ། །

[Block 246 [VERSE]]
དེ་ཕྱིར་ཆོས་མི་མཐུན་དཔེ་ལ། །
ངེས་པར་འདི་ལ་གཞི་མི་འདོད། །
དེ་དག་མེད་ནའང་དེ་མེད་ཅེས། །
བརྗོད་པ་ལས་ཀྱང་དེ་རྟོགས་ཕྱིར། །

[Block 247]
འདི་ལྟར།

[Block 248 [VERSE]]
དཔེ་ལ་དེ་ཡི་ངོ་བོ་དང་། །
རྒྱུ་དངོས་དེ་དག་མི་ཤེས་ལ། །

[Block 249]
སྟོན་ཏེ། དཔེ་ལ་ནི༌[^147]བསྒྲུབ་པར་བྱ་བའི་ཆོས་ནི་དེའི་ངོ་བོར་དེ་ཙམ་དང་འབྲེལ་པས་དེའི་རང་གི་ངོ་བོ་ཉིད༌[^148]སྟོན་ཏོ། །

[Block 250]
བྱས་པའི་ངོ་བོ་ཉིད་སྐྱེད་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་མི་རྟག་པའི་ངོ་བོ་ཉིད་མེད༌[^149]ན་སྐྱེད་པར་བྱེད་དོ་ཞེས་ཚད་མ་དཔེས་རབ་ཏུ་སྟོན་ཏོ། །
--- END BLOCKS ---
