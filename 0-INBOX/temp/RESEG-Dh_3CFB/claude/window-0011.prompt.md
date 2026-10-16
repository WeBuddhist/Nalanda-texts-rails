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
དོན་གྱི་བདག་ཉིད་གཅིག་པ་དེ་ནི་མངོན་སུམ་པ་ཡིན་ཏེ། ཆོས་ཅན་མ་གྲུབ་ན་སྒྲུབ་པ་མི་སྲིད་པའི་ཕྱིར་རོ། །

[Block 387]
དཔེར་ན་མི་རྟག་པ་བསྒྲུབ་པར་བྱ་བ་ལ་སྒྲ་ལྟ་བུ་སྟེ། དེའི་མངོན་སུམ་ཁོ་ནས་གྲུབ་པས་རྣམ་པ་ཐམས་ཅད་འགྲུབ་སྟེ། དེ་ལས་གཞན་པ་མ་གྲུབ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 388]
འོན་ཏེ་ཡོད་ན་ནི་དེའི་ངོ་བོ་ཉིད་མ་ཡིན་ནོ། །

[Block 389]
གང་ཞིག་གང་དང་གྲུབ་པ་དང་བདེ་བ་གཅིག་པ་ཅན་མ་ཡིན་པ་དེ་ནི་དེའི་ངོ་བོ་ཉིད་ཡིན་པར་རིགས་པ་མ་ཡིན་ཏེ། ཐ་དད་པའི་ཐ་སྙད་ཀྱི་རྒྱུ་ནི་དེ་ཙམ་དུ་ཟད་པའི་ཕྱིར་རོ། །

[Block 390]
དེ་ལྟ་མ་ཡིན་ན་མེད་པར་ཐལ་བར་འགྱུར་རོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 391]
དེའི་ཕྱིར་ཆོས་ཅན་མངོན་སུམ་པ༌[^240]དེའི་ངོ་བོ་ཉིད་མཐའ་དག་ཡོངས་སུ་བཅད་པའི་ཕྱིར། དེ་ལ་ཚད་མ་གཞན་འཇུག་པའི་གོ་སྐབས་མེད་པར་འགྱུར་རོ། །

[Block 392 [VERSE]]
གཟུགས་ཆོས་མཐུན་པ་མཐོང་བ་ལས། །
ཉ་ཕྱིས་ལ་དངུལ་རྣམ་པ་ལྟར། །
གལ་ཏེ་འཁྲུལ་པའི་རྒྱུ་མཚན་གྱིས། །
ཡོན་ཏན་གཞན་སྦྱོར་མི་བྱེད་ན། །

[Block 393]
གལ་ཏེ་དངོས་པོ་དེ་ཁོ་ན་ཉིད་ཐམས་ཅད་མཐོང་བ་ཅན་ལ་ཡང་ཇི་ལྟར་ཉ་ཕྱིས་ལ་དངུལ་གྱི་རྣམ་པ་ལྟ་བུར་དེ་ལྟར་ངེས་པའི་གགས༌[^241]སུ་གྱུར་པའི་ཁྲུལ༌[^242]པའི་རྒྱུ་མཚན་གྱིས་ཡོན་ཏན་གཞན༌[^243]སྦྱོར་བར་མི་བྱེད་ནའོ། །

[Block 394]
ཉ་ཕྱིས་ལ་ནི་མཚུངས་པ་དང་། ཁྱད་པར་ཅན་དང་ངོ་བོས༌[^244]གཉིས་ཡོད་པ་ནི་མ་ཡིན་ཏེ། དེ་ལྟར་རྟོགས་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 395]
བྱེ་བྲག་ཏུ་མི་རྟོགས་ན་ནི་གཉིས་ཉིད་དུ་རྟག་པ་མི་རུང་བའི་ཕྱིར་དང་། ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 396]
དེ་ལྟ་བས་ན་ཉ་ཕྱིས་ཀྱི་གཟུགས་མཐོང་བས་ཁྱད་པར་ཁོ་ན་མཐོང་ལ། ངེས་པའི་རྐྱེན་མ་ཚང་བའི་ཕྱིར་གཏན་ལ་མ་ཕེབས་པས་དེའི་སྤྱི་མཐོང་ངོ་སྙམ་དུ་རློམ་པར་བྱེད་དོ། །

[Block 397]
དེའི་ཕྱིར་འདི་དངུལ་དུ་སྒྲོ་འདོགས་ཤིང་དེ་ལྟར་འདྲ་བ༌[^245]གཞན་སྐྱེ་བས་ཐ་དད་པ་ཉིད་དུ་མ་འཁྲིགས་པས་དེའི་ངོ་བོར་སྒྲོ་བཏགས་པའི་ཕྱིར་གནས་པར་འཁྲུལ་ལོ། །

[Block 398]
འདི་ལ་གཞན་གྱི་དངོས་པོ་ཇི་སྙེད་པ་རང་གི་རྒྱུ་མཚན་ཇི་ལྟ་བ་ལས་འབྱུང་བའི་སྒྲོ་འདོགས་པ་ཡང་དེ་སྙེད་ཁོ་ན་ཡིན་པས་དེ་རྣམ་པར་གཅོད༌[^246]པའི་ཚད་མ་རྣམས་འབྱུང་བ་ནི་འབྲས་བུ་དང་བཅས་པར་འབྱུང་ངོ་།[^247] །རྣམ་པར་གཅོད་པའི་འབྲས་བུ་ཅན་དེ་དག་ནི་དངོས་པོའི་ཆ་ཤས་མ་རྟོགས་པ་རྟོགས་པར་བྱ་བའི་ཕྱིར་འཇུག་པ་མ་ཡིན་ཏེ། [^248]ཆ་ཤས་མེད་པ་ལ་ཕྱོགས་གཅིག་མཐོང་བ་མི༌[^249]རུང་བའི་ཕྱིར་དེ་ནི་མཐོང་ཟིན་པའི་ཕྱིར་རོ། །

[Block 399 [VERSE]]
དེ་ཕྱིར་དངོས་པོ་མཐོང་བ་ཡི། །
ཡོན་ཏན་མཐའ་དག་མཐོང་བ་ཉིད། །
འཁྲུལ་པས་ངེས་པར་མི་བྱེད་པས། །
སྒྲུབ་པ་རབ་ཏུ་འཇུག་པ་ཡིན། །

[Block 400]
ཞེས་བྱ་བ་ནི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 401]
དེ་ལྟ་བས་ན་མཐོང་བ་ལ་མཐོང་བ་གཟུང་བའི་ཕྱིར། ཚད་མ་གཞན་འཇུག་པ་ནི་མ་ཡིན་ནོ། །

[Block 402 [VERSE]]
རྗེས་སུ་དཔག་པ་ལས་ཀྱང་དངོས། །
འཛིན་ན་ཆོས་གཅིག་ངེས་གྱུར་པས། །
ཆོས་ཅན༌[^250]འཛིན་ཏེ་སེལ་བ་ལ། །
ཉེས་པ་འདིར་ནི་ཐལ་མི་འགྱུར། །

[Block 403]
གང་ཞིག་མངོན་སུམ་གྱིས་མཐོང་བ་ལ་ཚད་མ་གཞན་མི་འཇུག་པ་འབའ་ཞིག༌[^251]ཏུ་མ་ཟད་ཀྱི། གང་གི་ཚེ་རྗེས་སུ་དཔག་པས་ཀྱང་བསྒྲུབས་པས༌[^252]དངོས་པོ་རྟོགས་པར་བྱེད་ཀྱི་རྣམ་པར་གཅོད་པར་བྱེད་པ་ནི་མ་ཡིན་པ་དེའི་ཚེ། ཆོས་གཅིག་ངེས་ན་དེ་དང་ཐ་མི་དད་པའི་ཕྱིར་ཆོས་ཐམས་ཅད་ངེས་པས་ཚད་མ་གཞན་མི་འཇུག་སྟེ། དེ་ངེས་ན་དེའི་བདག་ཉིད་མ་ངེས་པ་ནི་རིགས་པ་མ་ཡིན་ནོ།[^253] །གང་གི༌[^254]ཚེ་རྗེས་སུ་དཔག་པས་སྒྲོ་འདོགས་པ་རྣམ་པར་གཅོད་པར་བྱེད་པ་དེའི་ཚེ་ནི་གཅིག་གིས་སྒྲོ་འདོགས་པ་རྣམ་པར་བཅད་པས་གཞན་རྣམ་པར་བཅད་པ་བྱས་པ་མ་ཡིན་པའི་ཕྱིར་རོ།[^255] །དེའི་དོན་དུ་གཞན་འཇུག་པར་འགྱུར་རོ། །

[Block 404]
མ་རྟོགས་པ་ངེས་པར་འགྱུར་བ་ནི་ཕྱིན་ཅི་ལོག་སྔོན་དུ་འགྲོ་བ་ཅན་ཁོ་ན་ཡིན་པར༌[^256]ངེས་པ་མ་ཡིན་ནམ། དཔེར་ན་དུ་བ་གློ་བུར་བ་ལས་མེ་རྟོགས་པ་ལྟ་བུ་སྟེ། དེ་ལ་ནི་མེ་མ་ཡིན་པར་སྒྲོ་འདོགས་པར༌[^257]མི་སྲིད་དོ། །

[Block 405]
དེ་བས་ན་ཐམས་ཅད་ལ་རྣམ་པར་གཅོད་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ་ཞེ་ན། འདི་ལ་ཆོས་ཅན་རྟོགས་ན་ཐ་མི་དད་པའི་ཕྱིར་ཐམས་ཅད་རྟོགས་པར་འགྱུར་རོ། །

[Block 406]
འོན་ཏེ་ཐ་དད་ན་མ་འབྲེལ་པ་ནི་དེ་ལ༌[^258]རྟོགས་པ་མེད་དོ། །ཞེས་བཤད་ཟིན་ཏོ། །

[Block 407]
དེའི་ཕྱིར་དེ་ལ་ཡང་དེ་མཐོང་བ་ལ་དེའི་རང་གི་ངོ་བོ་མ་ངེས་པ་ནི་ག་ལས་ཤེ༌[^259]ན། ཕྱིན་ཅི་ལོག་ཁོ་ན་ལས་ཡིན་ནོ། །

[Block 408]
ད་ཡང༌[^260]ཕྱོགས་དེ་བློ་མེ་དང་ལྡན་པར་འཛིན་པ་དང་བྲལ་བས། དེས་དབེན་པའི་ངོ་བོར་ངེས་པར་བྱེད་པ་ན་ཇི་ལྟར་ཕྱིན་ཅི་ལོག་མ་ཡིན། དེའི་རྣམ་པར་སྒྲོ་འདོགས་པ་དང་ཐེ་ཚོམ་དང་བྲལ་བ་ནི་དེ་རྟོགས་པར་བྱ་བ་ལ་རྟོགས༌[^261]ཀྱི་རྗེས་སུ་འབྲང་བར་ཡང་མི་བྱེད། དེའི་རྗེས་སུ་འགྲོ་བ་དང་ལྡོག་པ་དག་ལ་གུས་པར་ཡང་མི་བྱེད་དོ། །

[Block 409 [VERSE]]
དེ༌[^262]ཕྱིར་དེ་ལྟར་རྟགས་སེལ་བའི། །
ཡུལ་ཅན་ཡིན་པར་རབ་ཏུ་བསྒྲགས། །
གཞན་དུ་ཆོས་ཅན་གྲུབ་གྱུར་ན། །
དེ་ལས་མ་གྲུབ་གཞན་ཅི་ཡོད།

[Block 410]
[^263] །ཅེས་བྱ་བ་ནི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པའོ། །

[Block 411 [VERSE]]
མཐོང་བ་འགའ་ལ༌[^264]ཤེས་པ་གང་། །
སྤྱི་ཡི་དོན་ཅན་རྣམ་རྟོག་པ། །
གཞན་གྱི་ཆ་སྒྲོ་མ་བཏགས་པ། །
དེ་ཙམ་སེལ་བའི་སྤྱོད་ཡུལ་ཅན། །

[Block 412]
གཟུགས་ལ་སོགས་པ་མཐོང་བའི་མཇུག་ཐོགས་སུ་རྟགས་ཅན་མ་ཡིན་པའི་ངེས་པའི་ཤེས་པ་སྐྱེ་བ་གང་ཡིན་པ་དེ་སྒྲོ་འདོགས་པ་མེད་ན་ཇི་ལྟར་རྣམ་པར་གཅོད་པའི་ཡུལ་ཅན་དུ་འགྱུར་ཞེ་ན། སྒྲོ་མ་བཏགས་པའི་ཡུལ་ལ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 413]
གང་ལ་འདིའི་སྒྲོ་འདོགས་པ་དཔེར་ན་བརྟེན་པའོ༌[^265]ཞེས་པའམ། བདག་དང་བཅས་པའོ་སྙམ་པའི་ཁྱད་པར་དེ་ལ་ངེས་པར་མི་འགྱུར་ཏེ། །ངེས་པ་དང་ནི་སྒྲོ་འདོགས་ཡིད།[^266] །གནོད་བྱ་གནོད་བྱེད་ངོ་བོའི༌[^267]ཕྱིར། །དངོས་པོ་ཐམས་ཅད་ལས་ཐ་དད་པ་མཐོང་ཡང་དེ་ཁོ་ན་བཞིན་དུ་མངོན་པར་ཤེས་པ་ནི་མ་ཡིན་ཏེ། ཁྱད་པར་འགའ་ཞིག་ལ་བར་དུ་གཅོད་པ་སྲིད་པའི་ཕྱིར། དཔེར་ན་ཉ་ཕྱིས་ཀྱི་དཀར་པོ་ཉིད་ལྟ་བུའོ། །

[Block 414]
གང་ལ་རྟོགས་པ་པོའི་འཁྲུལ་པའི་རྒྱུ་མཚན་མེད་པ༌[^268]དེ་ཁོ་ན་ལ་ནི་དེ༌[^269]མཐོང་བ་ཁྱད་པར་མེད་ཀྱང་འདིའི་དྲན་པ་ངེས་པར་འགྱུར་ཏེ། སྒྲོ་འདོགས་པ་དང་ངེས་པ་དག་གནོད་པར་བྱ་བ་དང་གནོད་པར་བྱེད༌[^270]པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 415]
ངེས་པ།

[Block 416 [VERSE]]
འདི་ནི་སྒྲོ་འདོགས་དབེན་པ་ལ། །
འཇུག༌[^271]ཅེས་བྱ་བར༌[^272]ཤེས་པ་ཡིན། །

[Block 417]
དེས་དབེན་པ་ཉིད་གཞན་སེལ་བ་ཡིན་ནོ། །

[Block 418]
དེ་ལྟ་བས་ན་དེ་ཡང་དེ་ཙམ་གྱིས༌[^273]སེལ་བའི་སྤྱོད་ཡུལ་ཅན་ཡིན་གྱི་དངོས་པོའི་རང་གི་ངོ་བོ་ངེས་པར༌[^274]བྱེད་བའི་བདག་ཉིད་ནི་མ་ཡིན་ཏེ། དེ་ལྟར་ངེས་པ་ལ་ཡང་གཞན་མ་རྟོགས་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 419]
དེའི་རང་གི་ངོ་བོ༌[^275]ངེས་པ་ལ་ནི་དེ༌[^276]མི་རུང་བའི་ཕྱིར་རོ། །

[Block 420 [VERSE]]
ཆ་ཤས་སྒྲོ་འདོགས་ཇི་སྙེད་པ། །
དེ་བསལ་ཕྱིར་ནི་ངེས་པ་དང་། །
སྒྲ་ཡང་དེ་སྙེད་ཁོ་ན་དེས། །
དེ་དག་སྤྱོད་ཡུལ་ཐ་དད་ཅན། །

[Block 421 [VERSE]]
གཞན་དུ་དངོས་པོ་གཅིག་པུ་ལ། །
སྒྲ་འམ་བློ་གཅིག་གིས་ཁྱབ་ན། །
གཞན་ཡུལ་མ་ཡིན་དེ་ཡི་ཕྱིར། །
རྣམ་གྲངས་པ་ནི་ཉིད་དུ་འགྱུར། །

[Block 422]
ཞེས་བྱ་བ་ནི་བར་སྐབས་ཀྱི་ཚིགས་སུ་བཅད་པ་དག་གོ། །

[Block 423]
གང་གི་ལྟར་བློ་ཁྱད་པར་ནི།[^277] །སྣ་ཚོགས་ཅན་དོན་ཐ་དད་འཛིན། །གང་ཞིག་ཁྱད་པར་རྣམས་ནི་ཕན་ཚུན་དང་རྟེན༌[^278]ལས་ཐ་དད་པ་ཁོ་ན་ཡིན་ལ། དེའི་རྒྱུ་ཅན་གྱི་གཉེན་པོ༌[^279]དག་ནི་དེ་དག་གི་རྟེན༌[^280]ནམ་དེ་དག་ཁོ་ན་ལ་འཇུག་གོ། །

[Block 424]
དེ་བས་ན་ཐལ་པ་འདིར་མི་འགྱུར་རོ་སྙམ་དུ༌[^281]སེམས་པ་དེའི་ལྟར་ན་ཡང་། །

[Block 425 [VERSE]]
ཁྱད་པར་སྣ་ཚོགས་ལ་ཕན་པའི། །
ཡན་ལག་ནུས་ལས་མི་གཞན་པའི། །
བདག་ཉིད་བདག་ཉིད་ཀུན་གཟུང་ན། །
ཕན་བྱའི་བྱེ་བྲག་གང་མ་ངེས། །
--- END BLOCKS ---
