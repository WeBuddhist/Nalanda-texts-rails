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
[Block 316]
དེ་བཞིན་དུ་རབ་ཏུ་མཛེས་པ་ལ་ཡང་བརྗོད་པར་བྱའོ་ཞེ་ན། བརྒལ་བ་འདི་ནི་མི་བཟད་པ་སྟེ།

[Block 317]
གྲགས༌[^258]ལས་དེ་ལྟར་བརྟགས་གྲངས༌[^259]ན། །སྒྲ་དེ་དབང་པོའི་ཡུལ་ལ་མིན། །

[Block 318]
འགྲོ་བའི་སྒྲ་ནི་བ་ལང་ཁོ་ན་ལ་གྲག་པས༌[^260]འགྲོ་བའི་སྒྲ་ལ༌[^261]མཚོན་པ་སྟེ། དེ་བཞིན་དུ་དམ་པ་དང་རབ་ཏུ་མཛེས་པར་བྱ་བའི་ཕྱིར་ཡོད་པའི་སྒྲས༌[^262]དབང་པོ་ལ་གནས་པ༌[^263]ནི་མ་ཡིན་ནོ། །

[Block 319]
དེའི་ཕྱིར་ཡོད་པའི་སྒྲ་ལས་དེ་ལྟར་བརྟགས་པ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 320 [VERSE]]
ཀུན་ཏུ་དོན་དང་ཕྲད་གང༌[^264]ན། །
གཟུགས་སྒྲ་བར་དུ་ཆོད་པ་དང་། །
ཆེན་པོའང་འཛིན་པར་མཐོང་བས་ན། །
བར་དུ་མ་ཆོད་པ་ལ་གནོད། །

[Block 321]
འདི་ལྟར་ཐམས་ཅད་དུ་དབང་པོས་དོན་ཐོབ་པར་བྱེད་པ་ལ་ནི་རག་ན། གང་འདི་གཟུགས་དང་སྒྲ་དག་ལས་ནི་བར༌[^265]དུ་ཆོད་བཞིན་པ་ལ་འཛིན་ཞིང་། དབང་པོའི་ཚད་ལས་ལྷག་པ་ལ་ཡང་འཛིན་པར་བྱེད་དོ། །

[Block 322]
[^266]དེ་ལྟར་གཉིས་ཀར་ཡང་མི་འགྱུར་བའི་ཕྱིར་དབང་པོ་ནི་དྲི་ལ་སོགས་པ་བཞིན་དུ་བར་དུ༌[^267]མ་ཆོད་པ་ན་འཛིན་པར་ནི༌[^268]མ་མཐོང་ངོ་། །

[Block 323 [HEADING]]
##### འགྲེལ་པ་བྱེད་མཁན་གྱི་འདོད་པ། ^1-4-5-2-0

[Block 324 [VERSE]]
བློ་ཡི་རྒྱུ་ཡི་ཚོགས་པ་རུ། །
བརྗོད་པ་བོར་ནས་གང་ལས༌[^269]དེ། །

[Block 325]
ཚད་མ། འགྲེལ་པ༌[^270]བྱེད་མཁན་གྱིས་ནི་དོན་གཞན་འབྲས་བུར་སྨྲ་སྟེ། ཚད་མའི་འབྲས་བུ་བློའི་སྐྱེ་བ་ལས་གཞན་དུ་མ༌[^271]མཐོང་བ་གང༌[^272]ལས་བློ་སྐྱེ་བར་གྲུབ་པ་དེ༌[^273]མངོན་སུམ་མོ་ཞེས་འདོད་དོ། །

[Block 326]
དེ་ལ་བརྗོད་པ་དེ་ལ༌[^274]ཡང་ཇི་ལྟ་བ་བཞིན་དུ་བརྗོད་པའི་བདག་ལ་སོགས་པ་དང་སྦྱོར་བ་དང་འདུ་བྱེད་པ་དང་བཅས་པ་དག་བོར་ནས་བློ་ལ་རྒྱུ་གཞན་ནི་མེད་ན་གང་གིས་མངོན་སུམ་ཉིད་ཀྱི་ཐ་སྙད་དུ་བྱས། ཅི་སྟེ་དོན་ཡིན་པའམ། ཅི་སྟེ་ཡང་དོན་ཁོ་ན་མངོན་སུམ་གྱི་རྒྱུའི་ཚོགས་པར་རྗོད་པར༌[^275]བྱེད་པ་དེ་ལྟ་ན། བློ་ཡི་སྐྱེ་བ་ཞེས་ཅིས་བསྣན། །འདི་སྐད་དུ་ཡོད་པ་དང་ཡང་དག་པར་ཕྲད་པ་སྐྱེས་བུའི་དབང་པོ་རྣམས་མངོན་སུམ་མོ་ཞེས་བཤད་པས་ཆོག་མོད། བློ་དང་སྐྱེ་བ་བསྣན་པས་ཅི་ཞིག་བྱ། གང་ལས་བྱུང་བ་དེ་ཞེས་པ་དེ་ཡང་རྣམ་པར་བརྟགས་པ༌[^276]ལས་ཡིན་ནོ། །

[Block 327]
གཞན་ཡང་།

[Block 328 [VERSE]]
དོན་དང་དབང་པོའི༌[^277]ཡིད་སྐྱེས་བུ། །
སྦྱོར་དང་འདུ་བྱེད་པ་ལས་གཞན། །
མངོན་སུམ་གྱི་ནི་བློ་བསྐྱེད་པའི། །
ཚོགས་པ་བརྗོད་པ་དེ་ཇི་ལྟ། །

[Block 329]
ཚོགས་པ་དེ་དག་གིས་མངོན་སུམ་དུ་སྐྱེད་པར་བྱེད་པ་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 330]
གང་དབང་པོ་དང་དོན་དུ་ཕྲད་པར་བརྟག་པ་དེ་ནི་མ་ཡིན་ཏེ། མངོན་སུམ་ཞེས་བྱ་བ་དེ་གཉིས་ལ་གནས་པའི་ཕྱིར་རོ། །

[Block 331]
ཡང་དག་པར་འདུ་བ་ཡང་མངོན་སུམ་མ་ཡིན་པ་ཉིད་དེ། འདི་སོ་སོར་སྒྲུབ་པར་བྱེད་པའོ་ཞེས་མི་བརྟག་གོ། །

[Block 332]
གལ་ཏེ་ཡང་བརྗོད་པ། བ་ལང་ཉིད་འདི༌[^278]རྟ་ཉིད་འདིའོ༌[^279]ཞེས་གང་ལས་ངེས་པར་འབྱུང་བ་དེ་མངོན་སུམ་མོ་ཞེ་ན། དེ་ཡང་རིགས་པ༌[^280]མ་ཡིན་ཏེ། གང་གི་ཕྱིར།

[Block 333 [VERSE]]
གླང་ཉིད་ཡོད་སྦྱོར་ལས་དོན་ནི། །
བ་གླང་ཉིད་སོགས་སུ་འཇལ་བྱེད། །
དབང་པོའི་བློ་ལ་དོན་རྣམས་དང་། །
སྦྱོར་བའི་ནུས་པ་ཡོད་མ་ཡིན། །

[Block 334]
བ་ལང་ཉིད་ཙམ་ལ་ལྟ་བ་སྟེ། ཁྱོད་ཀྱི་ལུགས་ཀྱི་དབང་པོའི་བློ་ལ་དེ་ཙམ་ལས༌[^281]བརྟེན་ནས་ལྟ་བའི་ནུས་པ་མེད་པར་འགྱུར་ཏེ། དེ་དག་སྦྱོར་བར་ནི་མི་བྱེད་ལ། མ་སྦྱོར་བར༌[^282]བ་ལང་ལ་སོགས་པ་ངེས་པར་ཡང་མི་རིགས་སོ། །

[Block 335]
དེའི་ཕྱིར་ཁྱད་པར་དུ་བྱ་བ་དང་ཁྱད་པར་དུ་བྱེད་པ་དང་བརྗོད་པར་བྱ་བ་དང་། རྗོད་པར་བྱེད་པའི་རྣམ་པར་རྟོག་པ་འདི་དག་ཐམས་ཅད་ཡིད་ཀྱིས་ཉེ་བར་འདོགས་པར་བྱེད་ཀྱིས༌[^283]དབང་པོའི་བློ༌[^284]ནི་མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན།

[Block 336]
རང་རང་རིག་པར་བྱ་བའི་དོན། །བསྟན་བྱ་མིན་ཚུལ་དབང་པོའི་ཡུལ། །

[Block 337]
ཆོས་དུ་མ་ཡོད་དུ་ཟིན་ཀྱང་དབང་པོའི་ཡུལ་ནི་གང་ཐུན་མོང་མ་ཡིན་པའི་བདག་ཉིད་དབང་པོ་ལ་སྣང་བ་སྟེ་འཐོབ་པར་བྱ་བའི་ཡུལ་ཡིན་ལ། རང་གི་སྣང་བའི་ཤེས་པ་སྐྱེས་པ་དེའི་བདག༌[^285]སོ་སོར་རིག་པར་བྱེད་དེ་ཤེས་པའི་རང་གི་ཆ་ཤས་བཞིན་ནོ། །

[Block 338]
དེ་ལྟ་བུ་བདག་ཉིད་ཀྱིས་བརྗོད་པར་བྱ་བ་ལ་སོགས་པ་ནི་བསྟན་པར་མི་ནུས་ཏེ། བརྗོད་པར་བྱ་བ་ལ་སོགས་པ་ནི་སྤྱིའི་ཡུལ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 339]
ཅི་སྟེ་ཡང་སྤྱིའི་རྣམ་པའི་ཚུལ་ནས་ཀྱང་དོན་དེ་ཉིད་ཡིན་ཏེ། དབང་པོའི་ཡུལ་ཡིན་པའི་ཕྱིར་དང་། རྣམ་པ་ཐམས་ཅད་ཀྱི་ངེས་པ་ཡིན་པའི་ཕྱིར་རོ་ཞེ་ན། དེ་ལྟ་ན་ཡང་།

[Block 340 [VERSE]]
དོན་མིན་ཤེས་པའང་རྣམ༌[^286]ཀུན་ཏུ། །
མངོན་སུམ་བློ་རུ་གནས་པར་འགྱུར། །

[Block 341]
མངོན་སུམ་གྱི་སྒྲ་ནི་གསུམ་ལ་འཇུག་སྟེ། ཚད་མ་དང་། ཤེས་པ་དང་། ཡུལ་རྣམས་ལའོ། །

[Block 342]
དེ་ཡང་ཚད་མ་ལ་ནི་དངོས་སུ་ཡིན་ལ་ཅིག་ཤོས་གཉིས་པོ་ལ་ནི་བརྟགས་ནས་སོ། །

[Block 343]
དེ་ལ་ཡུལ༌[^287]ནི་མངོན་སུམ་གྱིས་གཞལ༌[^288]བར་བྱ་བ༌[^289]ཡིན་པའི་ཕྱིར་མངོན་སུམ་ཞེས་གདགས་སོ། །ཤེས་པ་དབང་པོ་ལ་བརྟེན་པ་ཚད་མ་དང་མཚུངས་པ་ཡིན་པའི་ཕྱིར་མངོན་སུམ་དུ་གདགས་པར་རིགས་པ་ཡིན་ནོ། །

[Block 344]
གལ་ཏེ་གཟུགས་ལ་སོགས་པའི་སྤྱིའི་རྣམ་པ་ལ་དམིགས་པའི་བློ་ནི་དབང་པོ་ལ་མི་ལྟོས་པར་ཐ་མི་དད་དུ་ཉེ་བར་བརྟག་ཅིང་འཇུག་པར་བྱེད་དེ། །དབང་པོའི་གཞན་དབང་དུ་གྱུར་པ་མ་ཡིན་ནོ་ཞེ་ན། རྣམ་པ་ཐམས་ཅད་དུ་དོན་གྱི་ཤེས་པ་གཟུགས་ལ་སོགས་པའི་ཡོན་ཏན་ཉིད་ལ་སོགས་པའི་དོན་ཡོད་པའི་ཤེས་པས༌[^290]དབང་པོ་གཞན་གྱི་སྤྱོད་ཡུལ་ལ་ཡང་རྒྱུ་བར་བྱེད་ན་ནི་དབང་པོ་དུ་མ་དོན་མེད་པར་འགྱུར་རོ་ཞེས་སྔར་བརྗོད་ཟིན་ཏོ། །

[Block 345]
དེའི་ཕྱིར་ཐུན་མོང་མ་ཡིན་པའི་ཡུལ་གྱི་རང་གི་ངོ་བོ་ཉིད་དབང་པོའི་སྤྱོད་ཡུལ་ཡིན་ནོ། །

[Block 346]
དེ་ལྟར་ན་རེ་ཞིག་གང་ལས་བློ་སྐྱེས་པ་དེ་མངོན་སུམ་ཡིན་པར་ནི་མི་རིགས་སོ། །

[Block 347]
ཅི་སྟེ་བློ་ཡི་སྐྱེ་བ་འདོད། །བློའི་སྐྱེ་བ་ཉིད་ཀྱི་ཕྱི་རོལ་གྱི་དོན་ལ་མངོན་སུམ་མོ་ཞེས་ཐོས་ཏེ། དེའི་ཚེ་དོགས་པ་བསུ་ནས་ལན་བརྗོད་པ།

[Block 348 [VERSE]]
དོན་གཞན་འབྲས་བུར་སྨྲ་བ་ཡིས། །
དོན་གཞན་ཐོབ་པར་འགྱུར་མ་ཡིན། །
ཇི་ལྟར་བྱས་ན་ཞེ་ན།
དོན་གྱི་བློ་ཤར་འབྲས་ཡིན་ན། །

[Block 349]
དེ་ལས་གཞན་འབྲས་མེད་པས་སོ། །

[Block 350]
ལྷག་པར་རྟོགས་ཤིང་ཁོང་དུ་ཆུད་པས་ནི་འབྲས་བུ་ཡིན་ལ། ཚད་མ་ནི་བློ་ལས་གཞན་མ་ཡིན་པས་བློ་ཚད་མ་ཉིད་ལས༌[^291]འབྲས་བུ་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 351 [VERSE]]
བློ་ཡི་སྐྱེ་བ་གཞན་ཡིན་ནོ།[^292] །
འཕྲོ་འདུ་རང་གི་རྒྱུ་ལས་ཏེ། །
ཚད་མ་འཕྲོད་པ་འདུ་བ་ལས། །
བྱེ་བྲག་པ་རྣམས་ཀྱི་ནི་བློ། །

[Block 352]
[^293]རང་གི་རྒྱུ་ལས་སྐྱེས་པའི་འབྲས་བུའི་ཆོས་འཕྲོད་པ་འདུ་བ་དང་ཡོད་པ་ལ་སོགས་པ་ཡིན་ལ་གལ་ཏེ་འཕྲོད་པ་འདུ་བ་དེ་ལས་དབང་པོའི་བློ་སྐྱེ་བར་འདོད་ན་ནི་འཕྲོད་པ་འདུ་བ་མངོན་སུམ་དུ་འགྱུར་ལ། དེ་ནི་རྟག་པ་ཡིན་པའི་ཕྱིར་འགའ་ཞིག་ཏུ་ཡང་སྐྱེ་བ་མ་ཡིན་ནོ། །

[Block 353]
དེའི་ཕྱིར་གཉིས་ཀའི་ལྟར་ཡང་ཚད་མ་དེ་སྦྱར་བར་མི་བྱའོ། །

[Block 354]
ཅི་སྟེ་གཞན་མིན་འདི་དོན་མེད། གལ་ཏེ་བློ་དང་སྐྱེ་བ་གཞན་ཉིད་མ་ཡིན་ན་ནི་དེ་ལྟར་ན་བློ་ཉིད་མངོན་སུམ་སྟེ། དེ་བས་ན་སྐྱེ་བ་སྨོས་པ་དོན་མེད་པར་འགྱུར་རོ། །

[Block 355 [VERSE]]
སྐྱེས་བུ་རྣམ་པར་གྱུར་ནས་བློ། །
བསྐྱེད་ན་མི་རྟག་པ་རུ་འགྱུར། །
--- END BLOCKS ---
