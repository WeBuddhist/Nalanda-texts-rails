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

[Block 251]
དེ་ལས་གནས་གཞན་དུ་བཏིང་བ་ཞེས་བྱ་བ་ནི། བཏིང་བའི་ཕྱིར་རྣམ་པར་གཞག་པ་འདིའོ། །

[Block 252]
མཚམས་གཅིག་པའི་གནས་གཅིག་ཏུ་དེར་ཅིག་ཅར་དབྱར་གནས་པར་ཁས་བླངས་པ་དག་ལྷག་མ་རྣམས་གནས་པ་ཉིད་ཅེས་བྱ་བ་སྟེ་རྙེད་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 253]
དབྱར་རྣམས་ལ་མཚམས་གཅིག་པ་ཉིད་ལ་གནས་དུ་མའི་འོག་ཏུ་དབྱར་གྱི་ནང་དུ་མཚམས་གཅིག་པ་ཉིད་དམ། མཚམས་ཐ་དད་པ་ཉིད་དུ་གནས་གང་ཡང་རུང་བར་བཏིང་བའི་གནས་དེ་ཐམས་ཅད་ལ་གཏན་པ་བཏིང་བ༌[^244]ཉིད་ཅེས་བྱ་བ་གང་ཞིག་གསུངས་པ་དེ༌[^245]འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 254]
དེ་ནི་བཏིང་བའི་ཚེ་དེ་ན་གནས་པ༌[^246]དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གང་ཡང་རུང་བའི་གནས་དུ་མ་ཉིད་ལས་དེའི་འདུན་པས་གནས་ལ་མངོན་པར་བརྟན༌[^247]པའོ། །

[Block 255]
དེ་ཉིད་གནས་འདི་ཡིན་གྱིས་སྙམ་དུ་གནས༌[^248]གཞན་འདི་ལ་དེ་དང་ལྡན་པ༌[^249]ཉིད་དེ་གདིང་བའི་དུས་སུ་མཚམས་གཅིག་ན་གནས་པར་གྱུར་ན་གདིང་བའི་ཕྱིར་གནས༌[^250]གཞན་དུ་ཡང་བཏིང༌[^251]བར་རིག་པར་བྱའོ། །

[Block 256]
དེར་འདི་གདིང་བར་བྱ་སྟེ། ཇི་ལྟར་གནས་གཅིག་པ་ཉིད་ལ་མཚམས་གཅད་པར༌[^252]བྱ་སྟེ། མཚམས་འཕེལ་བ་ལའོ། །

[Block 257]
གདིང་བར་འགྱུར་བའི་གནས་ཉིད་ལ་གདིང་བར་བྱའོ་ཞེས་བྱ་བར་འགྱུར་རོ། །

[Block 258]
དེ་བས་ན་དེར་གནས་གཞན་ན་གནས་པ་སོ་སོར་ཉམས་སུ་མྱོང་བར་བྱེད་ཅིང་མི་འབྱུང་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 259]
དབྱར་གནས་པ་ཉིད་མཚམས་གཅིག་ཏུ་བྱེད་པ་ལ་དུ་མའི་གནས་ལ་གནས་གཅིག་ཏུ་གཏན་པ་བཏིང་བ་ལ་གནས་ལྷག་མ་རྣམས་ལ་ཡང་གཏན་པ་ཉིད་དུ་གསུངས་པ་གང་ཡིན་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 260]
བཏིང་ནས་མཚམས་ཐ་དད་པར་བྱས་ན་གང་ཡང་རུང་བ་དེའི་གནས་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མཚམས་གཅིག་ཏུ་བཏིང་ནས་མཚམས་ཐ་དད་པར་བྱས་ན་གནས་དུ་མ་དེ་ལས་གདིང་བའི་ལས་བྱས་པའི་གནས་གང་ཡིན་པ་དེ༌[^253]གནས་གང་ཡང་རུང་བར་གཞག་ན་ཡང་རང་གི་གནས་ཁོ་ན་གནས་པའི༌[^254]ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 261]
གང་དུ་བཏིང་བ་དེ་ཉིད་ནི་འདིའི་གནས་སོ་སྙམ་དུ་དོགས་པ་བསལ་བའི་ཕྱིར་གཏན་པ་གདིང་བར་བྱ་སྟེ། མཚམས་ཐ་དད་དུ་བྱེད་པ་ལ་ཐམས་ཅད་ལ་གཏན་པ༌[^255]གདིང་བ་ཉིད་ཅེས་བྱ་བ་གང་ཞིག་གསུངས་པ་དེ་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 262]
ཐ་དད་པ་ཉིད་ཡིན་ན་གནས་སོ་སོར་དེ་དབྱུང་ངོ་ཞེས་བྱ་བ་ནི། མཚམས་ཐ་དད་པ་ཉིད་ཡིན་ན་གནས་འདི་རྣམས་ལ་གནས་སོ་སོ་སོ་སོར་གཏན་པ་དེ་དབྱུང་དགོས་ཀྱི་ཐམས་ཅད་ཀྱིས་གནས་གཅིག་ཏུ་འདི་ཕྱུང་བ་ཉིད་ལ་གནས་གཞན་དང་འབྲེལ་བ་རྣམས་ཀྱི་གཏན་པ་དེ་རང་གི་གནས་སུ༌[^256]སྤོ་བར་བྱའོ། །

[Block 263]
ཡང་ན་རང་གི་གནས་ནས་འགའ་ཞིག་གཏན་པའི་དྲུང་དུ་གཞག་པར་བྱ་བ་སྟེ། གཞན་དུ་ན་དེས་སྐྱ་རེངས་འཆར་བའི་དུས་སུ་དབྱུང་བ་འགྲུབ་པོ་སྙམ་དུ་འདི་རྣམ་པར་གཞག་པར་རིག་པར་བྱའོ། །

[Block 264]
གང་ཞིག་སོ་སོར་མཚམས་འགུམས་པར་བགྱིད་ཅིང་སོ་སོར་བྱ་སྟེ། དབྱུང་བ་ལ་གནས་དེ་རྣམས་ཐམས་ཅད་གཏན་པ་ཕྱུང་བར་འགྱུར་རམ། ཉེ་བ༌[^257]འཁོར་མི་འགྱུར་ཏེ། གང་དག་འབྱིན་པར་བྱེད་པ་དེ་དག་གིས་ནི་གཏན་པ་དབྱུང་བར་འགྱུར་ལ། གང་དག་འབྱིན་པར་མི་བྱེད་པ་དེ་དག་གིས་ནི་གཏན་པ་ཕྱུང་བར་མི་འགྱུར་རོ། །

[Block 265]
མཚམས་གཅིག་པ་ཉིད་དུ་ནི་ཕྱུང་ན་ཐམས་ཅད་ཀྱིས༌[^258]གཏན་པ་ཕྱུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་དེ་བས་ན་འདིར་མདོར་བྱས་པ་ཡིན་ནོ། །

[Block 266]
བྱེ་བ༌[^259]ཉིད་ན་ཕྱོགས་སོ་སོའི་ཞེས་བྱ་བ་ནི་གནས་གཅིག་ཏུ་གཏོགས་པ་ཉིད་ཡིན་ན་དགེ་འདུན་བྱེ་ཞིང་ཕྱོགས་གཉིས་སུ་གྱུར་ན་ཕྱོགས་གཅིག་གིས༌[^260]ཕྱུང་བ་ཕྱོགས་ཅིག་ཤོས་ཀྱིས༌[^261]ཕྱུང་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 267]
འདིར་གཞུང་ནི་དགེ་སློང་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས་གཏན་པ་བཏིང་བའི་གནས་སུ་དགེ་འདུན་བྱེ༌[^262]ན། དེར་ཕྱོགས་གཅིག་གམ་ཅིག་ཤོས་ཀྱིས་གཏན་པ་འབྱིན་པར་བགྱིད་ན་དེ་དག་ཐམས་ཅད་ཀྱིས་གཏན་པ་ཕྱུང་བར་བརྗོད་པར་བགྱིའམ། ཉེ་བ༌[^263]འཁོར༌[^264]མི་བྱ་སྟེ་གང་དག་འབྱིན་པར་བྱེད་པ་དེ་དག་གིས་ནི་གཏན་པ་བྱུང་བར༌[^265]འགྱུར་ལ། གང་དག་མི་བྱེད་པ་དེ་དག་གིས་ནི་གཏན་པ་ཕྱུང་བར་མི་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 268]
མ་བཏིང་བས་ཕྱུང་བ་ནི་མ་ཕྱུང་བ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གནས་གཞན་དུ་དབྱར་གནས་པར་ཁས་བླངས་པ་གང་དག་ལ་གཏན་པ་བཏིང་བ་མེད་པ་དག་ནི་མ་བཏིང་བ་ཞེས་བྱ་བ་སྟེ། དེ་ནི་མ་ཕྱུང་བ་མ་ཡིན་ཏེ་ཕྱུང་བ་ཉིད་ཡིན་ནོ། །

[Block 269]
འདིར་གཞུང་ནི་བཙུན་པ། རེ་ཞིག་དབྱར་གནས་པའི་དགེ་སློང་གིས་གཏན་པ་བཏིང་ནས་མཚམས་ཀྱི་སླད་རོལ་དུ་མཆིས་ཤིང་ལྟོས་པ་མ་མཆིས་པར་གྱུར་ན་དགེ་སློང་གློ་བུར་བ་དག་ལྷགས་ཏེ་གཏན་པ་འབྱིན་པར་བགྱིད་ན་གཏན་པ་ཕྱུང་བར་བརྗོད་པར་བགྱིའམ། ཉེ་བ་འཁོར་ཕྱུང་བར་བརྗོད་པར་བགྱིའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 270]
དེ་མི་འབྱུང་བ་ཉིད་ཀྱིས་ཁ་བསྐང༌[^266]དུ་མི་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི༌[^267]གང་ལ་དགེ་འདུན་གྱིས་གཏན་པ་གདིང་བ་ལ་དེ་ལ༌[^268]ཁ་བསྐང༌[^269]དུ་མི་རུང་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 271]
འདིར་གཞུང་ནི་ཆོས་གོས་ཀྱི་གཞི་ཞུ་བ་ལས།

[Block 272]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་གིས་གཅིག་ཏུ༌[^270]དབྱར་གནས་པར་ཁས་ལེན་ཅིང་དེས་དབྱར་ཟླ་བ་གསུམ་པོ་དག་འདས་ནས་དགག་དབྱེ་བགྱིས་ཏེ༌[^271]དགེ་འདུན༌[^272]ལ་གཏན་པ་གདིང་བའི༌[^273]ཆོས་གོས་འབུལ་བར་བགྱིད་ཅིང་དེར་དགེ་སློང་གློ་བུར་བ་དག་ལྷགས་ཤིང་དེ་དག་གཏན་པ་འདིང་བའི༌[^274]རྗེས་སུ་ཞུགས་ཏེ། དོང་ན་ཆོས་གོས་དེ་སུས་ཐོབ་པར་འགྱུར་ལགས། ཉེ་བ་འཁོར་དགེ་སློང་དེ་ཉིད་ཀྱིས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 273]
མ་བཏིང་བ་ཉིད་ཀྱིས་དབྱུང་བར་མི་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ལ་གཏན་པ་བཏིང་བར་མི་འགྱུར་བ་དེ་ལ་དེ་འདིང་བར༌[^275]བྱེད་པའི་དགེ་འདུན་དེ་ལ་ཁ་བསྐང༌[^276]དུ་རུང་བའོ། །

[Block 274]
དགེ་སློང་གློ་བུར་བ་དག་འོངས་ཏེ་གཏན་པ༌[^277]འདིང་བར༌[^278]བགྱིད་ན་ཞེས་བྱ་བ་འདིར་དོན་གྱིས་འབྱུང་བ༌[^279]དེར་མདོར་བྱས་པའོ། །

[Block 275]
གཏན་པ་བཏིང་བ་སྣམ་སྦྱར་མེད་པར་གྲོང་དུ་འཇུག་པ་ལ་སོགས་པ་དང་སུམ་མདོ་ཚུན་ཆད་དུ་འདུག་པ་ལ་ཡང་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཇི་སྲིད་སུམ་མདོ་ཚུན་ཆད་དུ་འདུག་པ་དང་གྲོང་དུ་འཇུག་པ་ལ་སོགས་པ་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 276]
འོན་ཀྱང་འདི་ནི་དོན་ལས་ཐོབ་པས་གསལ་བར་བྱ་བའི་ཕྱིར་མདོར་བྱས་པའོ། །

[Block 277]
འདིར་གཞུང་ནི། བཙུན་པ་གཏན་པ་བཏིང་བའི་གནས་ན་རྐྱེན་དུ་དག་བག་ཡངས་སུ་འགྱུར་ལགས། ཉེ་བ་འཁོར་བཅུ་སྟེ། བཅུ་གང་ཞེ་ན། ཡང་ཡང་ཟ་བ་དང་། འདུས་ཤིང་ཟ་བ་དང་། མ་སྨྲས་པར་རྒྱུ་བ་དང་། སྨད་གཡོགས་སྟོད་གཡོགས་དང་བཅས་པས་ཅི་བདེར་ལྗོངས་རྒྱུ་བ་དང་། མཚན་མོ་འབྲལ་བ་མེད་པ་དང་། ཞག་བཅུ་འདའ་བར་མེད་པ་དང་། ཟླ་བ་འདའ་བར་མེད་པ་དང་། །གོས་ཇི་ཙམ་གྱིས་ཆོག་པ་སློང་བ་དང་གོས་རུང་བར་བྱས་པ་དག་ཇི་ཙམ་འདོད་པ་དག་འཆང་བ་དང་། སྟོན་ཟླ་འབྲིང་པོའི་ཚེས་བཅུ་དྲུག་ནས་དཔྱིད་ཟླ་ར་བ་ཉའི་བར་དུ་དབྱར་གནས་པའི་དགེ་འདུན་གྱི་རྙེད་པ་མི་བགོ་བའོ་ཞེས་གསུངས་པ་དང་། གཞན་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་ཇི་སྐད་དུ་དགེ་སློང་གིས་ཁྱིམ་གཞན་དུ་སྨད་གཡོགས་དང་སྟོད་གཡོགས་ཀྱིས་འདུག་པར་བྱའོ་ཞེས་གསུངས་ནས། བཙུན་པ་སུམ་མདོ་དང་བཞི་མདོ་དག་ཏུ་སྨད་གཡོགས་དང་སྟོད་གཡོགས་ཀྱིས་མཆིས་སུ་རུང་ངམ། ཉེ་བ་འཁོར་གཏན་པ་བཏིང་པར་རུང་ངོ་ཞེས་གསུངས་པ་དེ་གཉིས་ཀའི་འདིར་བསྡུས་པ་ཡིན་ནོ། །

[Block 278]
གཏན་པའི་གཞི་ཞུ་བ་ལ་སོགས་པའི་སྐབས་སོ། །

[Block 279]
སྲ་བརྐྱང་གི་གཞི་རྫོགས་སོ།། །།

[Block 280 [HEADING]]
## གོས་ཀྱི་གཞི། ^2-0

[Block 281]
མཚོན་གྱིས་མ་དྲས་པའི་གོས་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། དེ་ལྟ་བས་ན་དགེ་སློང་དག་གིས་ཁྱིམ་བདག་གི་གོས་མཚོན་གྱིས་མ་དྲས་པ་དག་ཁ་དོག་ངན་པར་བྱ་སྟེ། བཅང་བར་གནང་ངོ་ཞེས་གསུངས་པ་ཡིན་གྱི་ཁ་དོག་ངན་པར་བྱས་པ་དང་བྲལ་བ་ལྟུང་བྱེད་དུ་གསུངས་པ་ནི་མ་ཡིན་ཏེ། ལྷག་མ་ཡང་འདི་དང་ཉེ་བར་སྦྱར་བའོ། །

[Block 282]
དྲས་ཤིང་དྲུབས་པ༌[^280]ཆོས་གོས་ཉིད་དུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་གསུངས་ན། རྣམ་པ་གང་གིས་དྲུབས་པ་གང་ཞེ་ན། དེའི་ཕྱིར་སྣམ་ཕྲན་སྦྲེལ༌[^281]གཞི་ཉིད་དང་ལྷག་མ་མཉམ་པ་ཉིད་དང་། དབུས་ནས་གཞན་དུ་གླེགས་བུའི་འཕྲོ་ཕྱོགས་ཕྱོགས་སུ་ལྟ་བ༌[^282]ཉིད་དང་མཐའ་བསྐོར་བ་ཉིད་དག་གིས་སོ་ཞེས་བྱ་པ་སྨོས་ཏེ། གདིང་བ་སྒྲུབ་པར་བྱེད་པའི་དུམ་བུ་རྣམས་ལ་ཕྱེད་དང་གསུམ་གྱི་དཀྱིལ་འཁོར་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པའི་ཆོ་ག་གསུངས་སོ། །

[Block 283]
དེའི་ཕྱིར་དེ་སྲིད་དུ་སྒྲུབ་པར་བྱེད་པའི་དུམ་བུའི་དབང་དུ་བྱས་ནས་མདོ་འདི་བྱས་སོ། །

[Block 284]
གླེགས་བུ་འཕྲོ་བཟུང་པའི་དབུས་ནས་སྣམ་ཕྲན་རྣམས་ལ་ལྷག་མ་གང་ཡིན་པ་དེ་ནི་འདིར་ལྷག་མ་ཉིད་དུ་གསུངས་སོ། །

[Block 285]
ཕྱོགས་ཕྱོགས་སུ་ཞེས༌[^283]ཟློས་བུར་བྱ་སྟེ། [^284]དབུས་ཀྱི་སྣམ་ཕྲན་གཞན་རྣམས་མངོན་པར་ཁྱབ་པར་བསྒྲུབ་པའི་དོན་དུ་སྣམ་ཕྲན་སྦྲེལ་གཞི༌[^285]ཉིད་དོ། །
--- END BLOCKS ---
