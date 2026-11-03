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
ཆོས་གོས་དེ་ནི་གཞན་དག་གི་ལ་གཏེར་གྱི་གནས་ལྟ་བུ་ཡིན་པས། གང་གི་ཚེ་འདིང་བར༌[^219]བྱེད་པ་ཐམས་ཅད་ཀྱིས༌[^220]དེ་ཕྱུང་བར་འགྱུར་བ༌[^221]དེའི་ཚེ་ན་གཏན་པ་བཏིང་བའི་དུས་ལས་བྱུང་བའི་རྙེད་པར་བགོ་བར་བྱའི། དེ་མ་ཕྱུང་བའི་སྔོན་རོལ་དུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིར་སྟོན་ཏོ། །

[Block 212]
གཞིར་གཏོགས་པའི་སྲ་བརྐྱང་གི་གཞིའོ། །

[Block 213]
སྟོན་ཟླ་འབྲིང་པོའི་ཞེས་སྨོས་པས་སྟོན་ཟླ་འབྲིང་པོའི་ཚེས་བཅུ་དྲུག་ལ་གཏན་པ་བཏིང་བའི་དུས་ཡིན་ན་ཤོལ་གྱི་ཟླ་བ་ནི༌[^222]རྒྱལ་པོའི་རྗེས་སུ་འབྲང་བར་བྱའོ་ཞེས་སྨོས་པས་དེའི་རྗེས་སུ་འབྲང་བ་ལ་མངོན་པར་བརྟེན་པར་ཐལ་བའི་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དགག་དབྱེ་བ༌[^223]ཇི་ལྟ་བ་བཞིན་དུ་གདིང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་དགག་དབྱེའི་སྒྲས་ནི་དུས་ཉེ་བར་མཚོན་པར་བྱེད་པར་རིག་པར་བྱའོ། །

[Block 214]
ཇི་ལྟར་དགག་དབྱེའི་དུས་སུ་ཞེས་བྱ་བའོ། །

[Block 215]
དེ་ལྟ་བས་ན་རྩོད་པར་བྱེད་པའི་དབང་གིས་སྔོན་དུ་དགག་དབྱེ་བྱེད་པ་ལ་དེའི་འོག་ཏུ་གཏན་པ་བཏིང་བ་འདིས་བྱ་བ་ཉིད་དུ་སྟོན་པའོ། །

[Block 216]
དེ་ཡང་འདིར་དེའི་ཚེ་སྟོན་ཟླ་འབྲིང་པོའི་ཚེས་བཅུ་དྲུག་ལ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 217]
གང་གི་ཕྱིར་གཞན་དུ་དུས་དེ་ལ་ངེས་པར་མི་འགྲུབ་པའོ། །

[Block 218]
གསོ་སྦྱོང་གི་མཐའ་མ༌[^224]ཡིན་པ་ལ་མི་བྱའོ་ཞེས་བྱ་བ་ནི། གཏན་པ་གདིང་བ་ནི་ཞེས་བྱ་བར་སྦྱར་ཏེ། གསོ་སྦྱོང་དང་ཉེ་བར་གྱུར་པའི་དུས་སུ་འདིར་ནི་ཐ་མའི་སྒྲའོ། །

[Block 219]
གསོ་སྦྱོང་གི་མདུན་རོལ་དུ་གཏན་པ་དབྱུང་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 220]
དབྱུང་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གསོ་སྦྱོང་ཐ༌[^225]མ་ཡིན་པ་ལ་མི་བྱ་སྟེ། གཏན་པ་དབྱུང་བ་ཡང་གསོ་སྦྱོང་ཉིད་བྱས་ནས་རྗེས་སུ་བསྒྲུབ་པར་བྱའོ་ཞེས་བྱ་བ་ལ་འདིར་དེ་བྱེད་པའོ། །

[Block 221]
ཚེས་བཅུ་དྲུག་ལ་ཡང་འདིར་ཉེ་བ་ཉིད་དུ་ཤེས་ན་ནི་བཅུ་དྲུག་གི་དེའམ། ཚེས་བཅོ་ལྔ༌[^226]གཏན་པ་དབྱུང་བར་ཐལ་བར་འགྱུར་བ་བསལ་བའི་ཕྱིར། འདི་ནི་ཉི་མ་དེ་ཉིད་ཀྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཏན་པ་དབྱུང་བ་འདི་ནི་གསོ་སྦྱོང་གི་ཉི་མ་ཚེས་བཅོ་ལྔ་ལ༌[^227]དབྱུང་བ་ཡིན་གྱི། ཚེས་བཅུ་དྲུག་ལ་དབྱུང་བ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 222]
བརྩམས་པ༌[^228]འདི་ནི་དུས་མ་ཡིན་པར་དབྱུང་བར་ཆེད་དུ་བྱས་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། གཞན་ལ་ནི་ངེས་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 223]
གསོ་སྦྱོང་མ་བྱས་པར་གཏན་པ་གདིང་བ་མི༌[^229]འབྱུང་ངོ་ཞེས་བྱ་བ་ཤེས་བཞིན་དུ་གསོ་སྦྱོང་གི་མཐའ་མ་ཡིན་པ་ལ་ཞེས་བྱ་བ་འདི་ལས་གསོ་སྦྱོང་བྱ་སྟེ་གཏན་པ་གདིང་བར་བྱ་ཞིང་ཡང་དགེ་སློང་གཞན་བྱུང་ན༌[^230]ཡང་གསོ་སྦྱོང་བྱེད་པ་ལ་ཇི་ལྟར་བསྒྲུབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཡང་གསོ་སྦྱོང་བྱས་ན་ཕྱུང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིས་ཀྱང་རྣམ་པ་གཞན་གྱིས་དབྱུང་བ་རང་འཇུག་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 224]
བཏིང་ནས་བྱེ་བ་དག་ལ་ནི་དེ་ཐ་དད་པར་འགྲུབ་པོ་ཞེས་བྱ་བ་ནི། གཏན་པ་བཏིང་བ་ནས་བྱེ་བ་དག་ལ་ནི་དེ་དག་ཐ་དད་པར་དབྱུང་བ་འདི་ལ་འགྲུབ་པོ། །འདི་ལ་གདིང་བ་གཅིག་ཡིན་པའི་ཕྱིར་ཕྱོགས་གཅིག་གིས་ཕྱུང་ན་ཕྱོགས་ཅིག༌[^231]ཤོས་ཀྱིས་ཀྱང་ཕྱུང་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 225]
གང་གིས་གང༌[^232]ཚེ་དེ་ལ་ཕྱུང་བའི་ལས་བྱས་པར་འགྱུར་བ་དེའི་ཚེ་འདི་ལ་འདི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 226]
ཆོས་སྨྲ་བ་དག་ཡོད་པས་དེ་གདིང་ངོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བའི་སྒྲས་ནི་ཆོས་སྨྲ་བ་པོ་བསྡུས་པ་སྟེ། གནས་གང་ན་དེ་ཡོད་པའོ། །

[Block 227]
ཆོས་སྨྲ་བ་དང་བཅས་པའི་གནས་ལ་ཆོས་སྨྲ་བ་པོ་རྣམས་ལ་རང་བྱུང་བ༌[^233]གདིང་བ་ཞེས་བྱ་བ་འདིར་དོན་ཏོ། །

[Block 228]
ཆོས་སྨྲ་བ་པོ་དེས་ནི་དབང་བྱེད་པ་ཉིད་ཡིན་པའི་ཕྱིར་ཏེ། དེ་རྣམས་ཀྱི་གནས་ཀྱི་རྒྱུ་ལས་དེའི་དོན་གྱི་ཕྱིར་བསྟན་པའོ། །

[Block 229]
དེ་ལྟ་བས་ན་མ་ཆོག་པ་དང་ཤིན་ཏུ་མ་ཆོག་པ་རྣམས་ལ་མི་སྐྱེད་པ༌[^234]ལ་མ་བྱས་པ་ཉིད་དུའོ། །

[Block 230]
དེ་ལྟར་ན་ཡང་བྱས་པ་ཉིད་ཀྱང་གཞན་རྣམས་ཀྱི་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 231]
འདིར་གཞུང་ཡང་དེ་བཞིན་དུ་སྟེ། དབྱར་གནས་པའི་དགེ་འདུན་བྱེ་ན་གང་གིས་གཏན་པ་གདིང་བར་བགྱི། གང་དག་ཆོས་སྨྲ་བ་དག་གིས་སོ་ཞེས་གསུངས་པ་དང་། ལམ་ནས་དྲངས་པ་རྣམས་ལ་རང་བཞིན་དུ་གནས་པའི་གནས་ཀྱི་གཏན་པ་གདིང་བར་བྱེད་པ་དེ། སྤངས་པ་རྣམས་སྲ་བརྐྱང་མ་བཏིང་བ་ཞེས་བརྗོད་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 232]
དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས་ཀྱང་། དགེ་འདུན་བྱེ་ན་སུས་གཏན་པ༌[^235]བཏིང༌[^236]བར་བགྱི་བཀའ་སྩལ་པ། ཆོས་སྨྲ་བ་དག་གིས་ཏེ། ཆོས་སྨྲ་བ་དེས་ནི་དབང་བྱེད་པ་ཉིད་ཡིན་པའི་ཕྱིར་ཏེ། ཐམས་ཅད་ལ་ཡང་གདིང་བ་འབྱུང་བར་ནི་འགྱུར་ཏེ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 233]
འདི་ཉིད་ནི་དབང་དུ་བྱེད་པ་ལ་དགོངས་ནས་དེ་བྱ་བ་ཉིད་དུ་གསུངས་སོ། །

[Block 234]
མ་ཆོག་པའི་གནས་པ་ལ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་བརྩམས་པ་དེ་ལས་བསྒྲུབ་པར་བྱའོ། །

[Block 235]
དེར་གཞན་དག་གིས་བྱས་ཀྱང་གནས་ཀྱི་རྙེད་པ་ནི་དེ་དག་ལས་འོས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། དུས་འདིར་གནས་པ་ལ་འདི་སྦྱིན་པར་བྱའོ། །

[Block 236]
གནས་དེར་གནས་པའི་དགེ་འདུན་ལ་རྙེད་པ་འདིའོ། །

[Block 237]
དེ་ལྟར་གནས་ཡོངས་སུ་དག་པ་ལྟར་རྙེད་པ་དེ་ནི་གནས་ཀྱི་རྙེད་པའོ། །

[Block 238]
ཆོས་མ་ཡིན་པ་སྨྲ་བ་གཞན་དག་གིས་གཏན་པ་གདིང་བ་བྱས་ཀྱང་ཆོས་སྨྲ་བ་དེ་དག་ལ་གནས་ཀྱི་རྙེད་པ་འོས་པ་ཉིད་ཡིན་ཏེ། ཆོས་མ་ཡིན་པ་སྨྲ་བ་དག་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 239]
རང་བཞིན་དུ་གནས་པའི་གནས་སུ་དེ་སྤངས་པ་རྣམས་ལ་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ནི། རང་བཞིན་དུ་གནས་པའི་གནས་སུ་གཏན་པ་གདིང་བར་བྱེད་པ་དེ་བྱེད་བཞིན་པ་ལས་སྤངས་པ་རྣམས་ལ་མི་འབྱུང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 240]
བསམ་པ་གནས་པ་ནི་བཏིང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། བསམ་པ་ནི་བསམ་པའོ། །

[Block 241]
ལྷན་ཅིག་ཏུ་བྱ་བ་ལ་འདུན་པ་ཕུལ་བའི་དབང་གིས་ལྷག་མ་རྣམས་ཀྱིས་བྱས་ན་བྱས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བསམ་པ་གནས་པ་ནི་བཏིང་བ༌[^237]ཡིན་ལ་དེ་དང་བྲལ་བ་ནི་ཕྱུང་བ་ཡིན་པས་དེའི་ཕྱིར་འདུན་པ་ཕུལ་བའི་དབང་གིས་ན་འབུལ་ཞེས་བྱ་བ་སྨོས་པ་ལ། འདི་དག་མི་འབྱུང་བ་ཞེས་བྱ་བར་ཐལ་བའོ། །

[Block 242]
དེ་ལ་ལན་ནི་འདི་ཡིན་ཏེ། གཞན་དག་ལྷན་ཅིག་བྱ་བ་གང་ཡིན་པའི་བྱ་བར་འགྱུར་བ་དེ་གཞན་དག་གིས་བྱས་པ་ལ་འདུན་པ་ཕུལ་བར་བྱེད་པས་ཀྱང་དེ་དག་བྱས་པ་ཉིད་དོ། །

[Block 243]
དེ་འདུན་པ་རྗེས་སུ་ཕུལ་བས་ལམ་ལ་གནས་པར་འགྱུར་ཞེས་བྱ་བ་བྱས་སོ། །

[Block 244]
དེ་བས་ན་ཐལ་བ་འདི་ཡོད་པ་མ་ཡིན་ནོ༌[^238]ཞེས་བྱ་བ་འདི་གླེང་གཞི་དག་ལས༌[^239]དྲངས་པའོ། །

[Block 245]
དེ་དང་བྲལ་བ་ནི་ཕྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེའི་སྒྲས་ནི་བསམ་པ་གནས་པ་དེར༌[^240]གཟུང་བའོ། །

[Block 246]
དེའི་ཕྱིར་འདུན་པ་མ་ཕུལ་བ་ལ་ནི་འདུག་ཏུ་ཟིན་ཀྱང་གཉིད་ལོག་གམ་སྙོམས་པར་ཞུགས༌[^241]ན་མ་ཐོས་ཀྱི་བར་དུ་བཏིང་བ་དང་ཕྱུང་བ་མི་འབྱུང་ངོ་ཞེས་བྱ་བ་ལ། འདུག་ཏུ་ཟིན་ཀྱང་ཞེས་བྱ་བ་ནི། དགེ་འདུན་གྱི་ནང་དུའོ། །

[Block 247]
མ་ཐོས་ཀྱི་བར་དུའོ་ཞེས་བྱ་བ་ནི། ཇི་སྲིད་དུ་གཏན་པ་བཏིང་བའམ། ཕྱུང་བ་མ་ཐོས་ཀྱི་བར་དུའོ། །

[Block 248]
གང་གི་ཕྱིར་བསམ་པ་གནས་པ་ནི་བཏིང་བ་ཡིན་ལ། དེ་དང་བྲལ་བ་ནི་ཕྱུང་བ་ཡིན་པ་དེའི་ཕྱིར་འདུན་པ་མ་ཕུལ་བ་ལ་ནི་གཉིད་ལོག་གམ་སྙོམས་པར་ཞུགས་སུ་ཟིན་ཀྱང་ཐོས་པའི་མདུན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 249]
འདུག་ཏུ་ཟིན་ཀྱང་དེ་གཉིས་ཡོད་པ་ཡིན་ཏེ། དེ་བས་ན་བཏིང་བ་དང་ཕྱུང་བ་འབྱུང་བ་ཁོ་ནར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 250]
མཚམས་གཅིག་པ་ཉིད་ཡིན་ན་དེར་གནས་གཞན་དུ་གནས་པ་རྣམས་ཀྱང་བཏིང་བའི་ཕྱིར་གནས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དེར་ཞེས་བྱ་བ་གང་ཡང་རུང་བ་གཅིག་གི༌[^242]ནང་ན་གནས་དུ་མ་ཡོད་ན་གནས་ལ༌[^243]མངོན་པར་བརྟེན་པའོ། །
--- END BLOCKS ---
