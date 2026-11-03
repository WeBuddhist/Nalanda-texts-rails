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
[Block 386]
གང་ཞིག་འདུལ་བ་ལ་བྱ་བ་མ་ཡིན་པ་དེ་ནི་བར་ཆད་དོ། །

[Block 387]
གང་ཞིག༌[^259]དེ་ནི་བར་ཆད་མ་ཡིན་པའོ། །

[Block 388]
དེ་དག་ལ་མངོན་པར་ཤེས་པ་ཉིད་དོ། །

[Block 389]
གཉིས་པོ་འདི་ནི་འདུལ་བ་ལ་གནས་པའི་དོན་ཉིད་བསྟན་ཏོ། །

[Block 390]
སྨྲ་བ་པོ་ཉིད་ནི་སླར་སྨྲ་བའི་ཕྱིར་དང་རྟོགས་པའི་ཕྱིར་གཉིས་པོ་འདི་ལ་མཁས་པར་འགྱུར་བའི་ནུས་པ་འམ་ལེ་ལོ་མེད་པ་ཉིད་དོ། །

[Block 391]
རྗེས་སུ་སྟོན་པ་ཉིད་ནི་རྣམ་པར་བཟློག་པ་ལ་ཡང་དག་པར་གནས་པ་ཉིད་དང་རྗེས་སུ་མཐུན་པར་སྨྲ་བ་པོ་ཉིད་དེ། ལེ་ལོར་གྱུར་པ་ལ་ཡང་རབ་ཏུ་འཇུག་པ་དང་། རྗེས་སུ་མཐུན་པའི་སྨྲ་བ་པོ་དང་། རྗེས་སུ་སྟོན་པར་བྱེད་ཅེས་བྱ་བ་འདོན་པ་འདིས་ནི་འདོན་པ་འདིའི་དོན་འདི་བརྗོད་དོ། །

[Block 392]
ཁ་ཅིག་ནི་འདི་དག་གི༌[^260]གནས་ལ་གདམས་ངག་ཏུ་བྱེད་པ་དང་། རྗེས་སུ་སྟོན་པར་བྱེད་པ་ཞེས་བྱ་བ་འདོན་པ་ཡིན་ཏེ། དེ་ལ་རྗེས་སུ་སྟོན་པར་བྱེད་པར༌[^261]འགྱུར་ཞེས་བྱ་བ་འདི་དང་མཚུངས་པའོ། །

[Block 393]
གདམས་ངག་ཏུ་བྱེད་ཅེས་བྱ་བ་ནི་ཡིད་ལ་བྱེད་པའི་དོན་དུ་གདམས་ངག་གང་ཞིག་དེ་ལ་འདིས་བརྗོད་པའོ། །

[Block 394]
འདིའི་དོན་དུ་རབ་ཏུ་བྱུང་བ་ཉིད་དོ། །

[Block 395]
དེ་བས་ན་འདིར་བྱེ་བྲག་ཏུ་འཁོར་བསྡུས་པ་འདི་འོས་པ་ཡིན་ཏེ་ཞེས་བྱ་བ་འདིའི་ཉེ་བར་བསྡུས་པའོ། །

[Block 396]
ལྷན་ཅིག་འཛིན་དུ་འཇུག་ནུས་པ་ཉིད་ཀྱི༌[^262]གནས་སམ་ཉེ་བར༌[^263]གནས་འཛིན་དུ་འཇུག་ནུས་པ་ཉིད་འདི་དང་ལྷན་ཅིག་ཏུ་ཡན་ལག་བཞི་པོ་འདི་རྣམས་ཤེས་ནས་གཉིས་པོ་འདི་དག་ལྷན་ཅིག་སྦྱར་བས་ཏེ། གཅིག་ནི་གནས་ལ་བརྟེན་པ་འདིར་བཅུག་ནས་གཞན་ནི་ཉེ་བའི་གནས་ལ་གནས་པ་ཞེས་བྱ་བ་བསྟན་པའི་དོན་དུ་འམ་གྱི་སྒྲའོ། །

[Block 397]
མཁན་པོ་གཞན་དུ་འཆག་པ་ལ་གནས་འཛིན་དུ་འཇུག་ནུས་པ་ཉིད་ཉེ་བར་སྦྱར་བ་ཡིན་ནོ། །

[Block 398]
མཁན་པོ་གཞན་དུ་གནས་པ་ལ་དེ་སྲིད་ཀྱི་དུས་ལ༌[^264]དགོངས་པས་འཇུག་པ་དང་གནས་པ་ལ་དགོངས་པ༌[^265]འགའ་ཞིག༌[^266]གི་དབང་གིས་ཉེ་བར་གནས་འཛིན་དུ་འཇུག་པ་ནུས་པ་ཉིད་དང་སྦྱར་རོ། །

[Block 399]
ལྟུང་བ་དང་ལྟུང་བ་མ་ཡིན་པ་དང་ཡང་བ་དང་ལྕི་བ་ཉིད་མངོན་པར་ཤེས་པ་ཉིད་དང་སོ་སོར་ཐར་པ་དང༌[^267]རྒྱས་པ་ཐོན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དེ་ལ་ལྟུང་བ་དང་ལྟུང་བ་མ་ཡིན་པ་དང་། མངོན་པར་ཤེས་པ་ཉིད་ལ་བྱ་བ་ཉིད་དང་། བྱ་བ་མ་ཡིན་པ་ཉིད་དང་རྣམ་པར་སྦྱར་བ་ལ་གནས་པའི་སླད་དུ་ཉེ་བར་སྦྱར་བ་ལ་དགོངས་སོ། །

[Block 400]
ཡང་བ་དང་ལྕི་བ་ཉིད་མངོན་པར་ཤེས་པ་ཉིད་ནི་ལྟུང་བ་སྦོམ་པོ་བཤགས་པ་ལ་དགོངས་པའོ། །

[Block 401]
སོ་སོར་ཐར་པ་དང་རྒྱས་པ་ཐོན་པ་ཉིད་ཀྱིས་ནི་འདུལ་བ་ལ་གནས་པའི་དོན་ཉིད་བསྟན་ཏོ། །

[Block 402]
རྒྱས་པའི་སྒྲ་འདིས་ནི་འདུལ་བ་མཐའ་དག་བསྡུས་པ་ཉིད་དོ། །

[Block 403]
སོ་སོར་ཐར་པ་དང་རྒྱས་པའི་སྒྲ་ནི་རྣམ་པར་འབྱེད་པ་ལས་ལྷག་པའི་གཞི་དང་ཕྲན་ཚེགས་ལ་སོགས་པ་སྟོན་པར་བྱེད་པ་ཞེས་བྱ་བ་ཤེས་པར་བྱ་བ་ཡིན་ཏེ། སོ་སོར་ཐར་པ་རྒྱས་པར་འགྱུར་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 404]
དང་པོ་ཐམས་ཅད་ལ་ཡང་སོ་སོར་ཐར་པ་ལས་འབྱུང་ངོ་། །གང་ཞིག་ཡང་དགེ་སློང་དང་དགེ་སློང་མ་རྣམས་ལྷན་ཅིག་ཏུ་ཞེས་བྱ་བ་འདི་ལས་རབ་ཏུ་འབྱུང་བའི༌[^268]གཞི་འབྱུང་བའོ། །

[Block 405]
གསོ་སྦྱོང་གི་ཚིག་ཚེ་དང་ལྡན་པ་རྣམས་ཞེས་བྱ་བ་ལ༌[^269]གསོ་སྦྱོང་གི་གཞི་འབྱུང་ངོ་། །གསོ་སྦྱོང་གི་བྱེ་བྲག་ནི་དགག་དབྱེ་སྟེ། དབྱར་མ་ཚང་བ་ཞེས་བྱ་བས་དབྱར་གྱི་གཞི་འབྱུང་ངོ་། །འདི་ཉིད་ཀྱི་ཕྱིར་དགག་དབྱེའི་གཞི་ལ་དབྱར་གནས་པ་དང་འབྲེལ་བས་རྣམ་པར་གཞག་པའོ། །

[Block 406]
ཚུལ་ཁྲིམས་ལ་གནས་པ་ལ་ནི་སྲ་བརྐྱང་ཞེས་བྱ་བ་སྲ་བརྐྱང་གི་གཞི་འབྱུང་ངོ་། །གོས་ཀྱི་མཐར་ཐུག་པའི་དགེ་སློང་ཞེས་བྱ་བས་གོས་ཀྱི་གཞི་འབྱུང་ངོ་། །གོས་ཀྱི་ཕྱོགས་ནི་ཀོ་ལྤགས་དང་སྨན་གྱི་ཕྱོགས་ཞེས་བྱ་བ་དེ་ལས་ལྡང་བར་བྱེད་དུ་འཇུག་པ་ཉིད་ཀྱིས་ཀོ་ལྤགས་ཀྱི་གཞི་འབྱུང་བ་དང་། དགེ་སློང་ནད་པ་རྣམས་ལ་བཅོམ་ལྡན་འདས་ཀྱིས་གང་ཞིག་སྨན་དེ་རྣམས་གནང་བ་ཞེས་བྱ་བ་དེས་སྨན་གྱི་གཞི་འབྱུང་བའོ། །

[Block 407]
ཚེ་དང་ལྡན་པ་རྣམས་མ་འོངས་པ་རྣམས་ལ་འདུན་པ་དང་ཡོངས་སུ་དག་པ་ཞུ་བར་གྱིས་ཤིག །དགེ་འདུན་དབྱེ་བའི་ཕྱིར་གཞན་དུ་འགྲོ་བར་མ་བྱེད་ཅིག་ཅེས་བྱ་བ་ལ་སོགས་པ་ལ་ཀཽ་ཤཱམྦཱིའི་གཞི་འབྱུང་བའོ། །

[Block 408]
དགེ་འདུན་དབྱེ་བའི་ཕྱིར་གཞི་དང་འདི་ལས་ཀྱང་རབ་ཏུ་འབྱུང་བ་ལ་སོགས་པའི་ལས་ཡང་དག་པར་མཚོན་པས་མ་ཐོབ་པ་ཉིད་འདིར་གནས་པ་ཞེས་བྱ་བའི་ཚིག་འདི་ལས་ཀྱི་གཞི་འབྱུང་ངོ་། །དགེ་སློང་ཀུན་ནས་འདོད་པས་དགེ་འདུན་ལ་ཡོངས་སུ་གནས་པར་བྱའོ་ཞེས་བྱ་བས་སྐྱ་བ་དང་དམར་བའི་གཞི་འབྱུང་ངོ་། །མི་འདོད་པ་ཉིད་ཀྱིས་བྱ་བ་ལ་སོགས་པས་སྤོང་བའི༌[^270]གཞི་འབྱུང་ངོ་། །གང་ཞིག་ལྟུང་བ་རྣམ་པར་གཞག་པའི་སླད་དུ་བྱེད་པ་བསྟན་པ་དང་། དགེ་འདུན་ལྷག་མ་སོ་སོར་བཤགས་པ་རྣམས་ལ་དེ་ནས་གསོ་སྦྱོང་གཞག་པའི་གཞི་འབྱུང་བའོ། །

[Block 409]
དགེ་སྦྱོང༌[^271]རྣམས་ཀྱི་གནས་པ་ནི་ཆེན་པོ་ཡིན་ཏེ་ཞེས་བྱ་བས་གནས་མལ་གྱི་གཞི་འབྱུང་ངོ་། །རྩོད་པ་ལ་ནུས་པའི་བསྟན་པ་དོར་ནས་ཀྱང་ལྟུང་བ་དང་དེ་གསོ་བའི་རྣམ་པར་གཞག་པས་རྩོད་པའི་གཞི་འབྱུང་ངོ་། །བརྗོད་པའི་ཡན་ལག་ཏུ་གྱུར་པ་དེའི་རིགས་ཅན་ཚུལ་ཁྲིམས་གཞན་བྱ་བ་རྣམ་པ་གཉིས་ཡིན་ན་སོ་སོར་ཐར་པ་དང་གཞི་རྣམས་ཀྱི་ལྷག་མའོ། །

[Block 410]
ཕྲན་ཚེགས་རྣམས་དང་མ་མོ་ལ་བརྟེན་པའི་གཞི་རྣམས་ཀྱི་རྒྱུ་ཅུང་ཟད་གསུངས་པ་ལ་སོགས་པ་རྣམས་ཀྱི་རྣམ་པར་མཚོན་པ་ནི་དྲི་བ་སྟེ། སྤྱོད་པ་རྣམ་པར་མཚོན་པ་ནི་དྲི་བ་དུལ་བར་བྱེད་པ་རྣམས་སོ། །

[Block 411]
[^272]དེ་ལྟར་འདི་ལས་ལྷག་མ་མེད་པའི་སོ་སོར་ཐར་པ་རྒྱས་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 412]
རྣམ་པར་འབྱེད་པ་ཙམ་གྱིས་འཇུག་པ་ལ་རབ་ཏུ་བྱུང་བ་ལ་སོགས་པར་བྱེད་པ་མ་ཡིན་ཏེ། འདི་ལྟར་བྱ་བ་ཉིད་རྣམས་ལ་ཡང་འདི་ཙམ་གྱིས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 413]
རྒན་པ་མེད་ན་གཞོན་པ་ལ་གནས་བཅའ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་རྒན་པ་ལྔ་པ་གང་ཡང་རུང་བ་ཅིག༌[^273]དང་མི་ལྡན་པར་གྱུར་ན་དེའི་ཆོ་ག་ནི་འདི་ཡིན་ནོ། །

[Block 414]
བཙུན་པ་དགེ་སློང་བསྙེན་པར་རྫོགས་པ་ནས་ལོ་དྲུག་ཅུ་ལགས་ལ། དེས་སོ་སོར་ཐར་པའི་མདོ་གདོན་པ་དང་རྒྱས་པར་བཀླགས་པ༌[^274]དང་ཐོན་པ་མ་ལགས་ན་དེས་ཀྱང་གཞན་ལ་གནས་པར༌[^275]མཆིས་པར་བགྱི་འམ་ཉེ་བ༌[^276]འཁོར་དེས་ཀྱང་གཞན་ལ་གནས་པས་འདུག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 415]
འདིར་ལོ་དྲུག་ཅུ་ལོན་པ་ཉིད་ཀྱང་རང་དབང་ཅན་མ་ཡིན་གྱི། ཤིན་ཏུ་མང་བ་ཉིད་སྟོན་པར་གནས་པ་ཡིན་ཞེས་བྱ་བ་ཁྱད་པར་མེད་པར་རྒན་པ་མེད་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 416]
འདུད་པ་འབའ་ཞིག་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ནི་ཕྱག་བྱ་བ་འབའ་ཞིག་མ་གཏོགས་པ་གནས་པའི་ཚུལ་ཁྲིམས་དེ་ལས་གཞན་པ་དག་ལ་རྒན་པས༌[^277]གཞོན་པ་ལས༌[^278]རྗེས་སུ་གནས་པར་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 417]
ལོ་ལྔ་ལོན་ཅིང་ལྷན་ཅིག་སྦྱོར་བ་ཐ་མ་དང་ལྡན་ན་གནས་མ༌[^279]བཅས་པར་ལྗོངས་རྒྱུར་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་དང་ལྟུང་བ་མ་ཡིན་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྷན་ཅིག་སྦྱར་བ་ཐ་མ་སྟེ། དེ་དང་ཡང་དག་པར་ལྡན་པའི་ལོ་ལྔ་ལོན་པས་གནས་མ་བཅས་པར་ལྗོངས་རྒྱུར་འགྲོ་བར་བྱའོ། །

[Block 418]
གཞན་དུ་ན་གསུམ་རིག་པ་ཡིན་ཡང་མི་བྱའོ་ཞེས་བྱ་བ་ལ། ཆོས་ལྔ་དང་མི་ལྡན་པ་དང་ལོ་ལྔ་མ་ལོན་པ་ཡང་ངོ་། །

[Block 419]
གང་གི་ཕྱིར་ལམ་དུ་འདུལ་བ་ཉམས་པར་གྱུར་པ་ཡིན་ཏེ། དེར་ལོ་ལྔ་ཚུལ་ཁྲིམས་ཀྱི་དངོས་པོ་དང་ལྡན་པའི་ཕྱིར་སྡུག་བསྔལ་གྱི༌[^280]རྣམ་པར་འགྱུར་བ༌[^281]འབྱུང་བ་ཡིན་ཏེ། ལོ་མ་ཚང་བ་ལ་ནི༌[^282]མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདིར་དགོངས་པ་མཐོང་བ་ཡིན་ནོ། །

[Block 420]
གསུམ་རིག་པ་ཡིན་ཡང་ཞེས་བྱ་བ་ནི་གནས་ལ་གནས་པའི་དོན་དུ་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པ་ལ༌[^283]ཡོངས་སུ་ཤེས་པ་གཉིས་དང་ཡོངས་སུ་འདུལ་བར་བྱེད་པའོ། །

[Block 421]
དེ་ལ་གལ་ཏེ་ཡང་འདི་ལ་ཆོས་ཉིད་མངོན་པར་ཤེས་པ་ཉིད་ཀྱི་ཕྱིར་དང་སྔོན་གྱི་གནས་ཤེས་པ་ཉིད་ཀྱིས་འཇུག་པ་ལ་ལྟ་བའི་ཕྱིར་དང་དཀའ་བ་ཆུང་ངུའི་རིག་པ་བསྟེན་པས་འོང་བ་ཕུན་སུམ་ཚོགས་པས་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པ་ཡོངས་སུ་ཤེས་པར་འགྲུབ་པར་འགྱུར་ཏེ། དེ་ལྟར་ན་ཡང༌[^284]ཡོངས་སུ་གདུལ་བར༌[^285]བྱ་བའི་དོན་དུ་གནས་ལ་གནས་པར་བྱའོ། །

[Block 422]
གང་གི་ཕྱིར་སྡུག་བསྔལ་བའི་ཐ་སྙད་ནི་འདུལ་བ༌[^286]ཉིད་དང་བཅས་པའི་དངོས་པོ་སྔོན་གྱི་རང་བཞིན་འཕྲོག༌[^287]པའི་ཕྱིར་རོ། །

[Block 423]
དགྲ་བཅོམ་པ་རྣམས་ལ་ནི་སྔོན་གྱི་རང་བཞིན་འཕྲོག་པ་ཐོས་པ་ཡིན་ཏེ། དགྲ་བཅོམ་པ་ལ་ལ་ཞིག་ནི་མཆོང་ཞིང་མཆོང་ཞིང་ཆུ་བོ་རྣམས་ལས་རྒལ་བར༌[^288]གྱུར་པ་དང་། ཚེ་དང་ལྡན་པ་པི་ལིན་དའི་བུས་གང་གཱའི་ལྷ་མོ་ལ་རླངས་མ་འདུག་ཤིག༌[^289]ཅེས་བྱ་བ་བརྗོད་པར་གྱུར་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 424]
གཞན་ཡང་འདིར་ནི་འདུལ་བ་ཡོངས་སུ་ཤེས་པར་ཅི་ནས་ཀྱང་བྱ་བ་མ་ཡིན་ཏེ། དཀའ་བ་ཉིད་ཀྱི་ཕྱིར་དང་། མང་བ་དང་ཕྲ༌[^290]མོ་དང་། [^291]གཅིག་ན་མི་གནས་པ་ལྟ་བ་དང་འབད་པ་རྣམས་ལ་བར་ཆད་མང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 425]
གང་གི་ཕྱིར་གནས་སྐབས་ནི་རྣམ་པ་སྣ་ཚོགས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
