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
[Block 771]
དེ་ལ་བདག་ཉིད་སློབ་པར་བྱེད་པ་ནི། བྱང་ཆུབ་སེམས་དཔའ་ཆོས་ཀྱིས༌[^575]རྗེས་སུ་འབྲང་བ་དང་། དད་པས་རྗེས་སུ་འབྲང་བའོ། །

[Block 772]
དེ་ལ་ཆོས་ཀྱིས༌[^576]རྗེས་སུ་འབྲང་བ་ནི་རྣམ་པ་གསུམ་དུ་སློབ་སྟེ། མོས་པ་མང་པོ༌[^577]ཉིད་ཀྱི་བསམ་པའི་རྒྱུན་ཉིད་དང་། སྦྱོར་བ་ཉིད་དང་།[^578] ཆོས་ཚོལ་བ་ལ་སྦྱོར་བ་ཉིད་ལའོ། །

[Block 773]
དད་པས་རྗེས་སུ་འབྲང་བ་ནི་རྣམ་པ་བཞི་སྟེ། བདག་ཉིད་ཀྱིས་བསླབ་པའི་སྔར་ཆོས་ཀྱིས༌[^579]རྗེས་སུ་འབྲང་བ་ལ་བསྟན་པའི་བསླབ་པ་རྣམ་པ་གསུམ་དང་།

[Block 774]
བཞི་པ་གདམས་ངག་རྗེས་སུ་བསྟན་པ་འཛིན་པའོ། །

[Block 775]
གཞན་བསླབ་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། གཞན་རྣམ་པ་གཉིས་ནི་ཞུགས་པ་དང་མ་ཞུགས་པ་ཞེས་བྱ་བའོ། །

[Block 776]
དེ་ལ་གཞན་ཞུགས་པ་དབང་པོ་རྣོན་པོ་ལ་བསྟན་པ་དང་། དད་པས་རྗེས་སུ་འབྲང་བ་ལ་བསྟན་ཅིང་གདམས་ངག་རྗེས་སུ་བསྟན་པའོ། །

[Block 777]
མ་ཞུགས་པ་རྣམས་ལ་ནི། ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་དང་། [^580]ཐབས་དང་བཅས་པ་ཞེས་བྱ་བ་སྟེ། དེ་ལ་དང་པོར་བདག་ཉིད་མོས་པ་ལ་སློབ་པར་བྱེད་དོ། །

[Block 778]
དེ་ནས་ནི་ཆོས་ཚོལ་ལོ། །

[Block 779]
དེ་ནས་ནི་བསྒྲུབ༌[^581]སྟེ། ཆོས་ཀྱིས༌[^582]རྗེས་སུ་འབྲང་བ་ནི་དེ་ལྟར་བདག་ཉིད་གང་དང་གང་ལ་སློབ་པ་དེ་ལ་གཞན་དག་ཀྱང་འཛུད་པར་བྱེད་དེ། བདག་ཉིད་ཀྱང་མོས་པ་ལ་སློབ་པར་བྱེད། ཆོས་ཚོལ་བར་བྱེད་ལ། གཞན་ཕ་རོལ་དག་ལ་ཡང་མོས་པ་བསྐྱེད་པར༌[^583]བྱ་བའི་དོན་དུ་ཆོས་སྟོན་པར་བྱེད་དོ། །

[Block 780]
བདག་ཉིད་ཀྱི༌[^584]སྒྲུབ་པར་བྱེད་ཅིང་གཞན་དག་གིས་ཀྱང་རྟོགས་པར་བྱ་བའི་ཕྱིར་གདམས་ངག་དང་རྗེས་སུ་བསྟན་པ་སྦྱིན་པ་སྟེ། དེ་ལྟར་རེ་ཞིག་ཞུགས་པ་རྣམས་ཀྱིའོ། །

[Block 781]
ཡང་མ་ཞུགས་པ་རྣམས་ལ་ནི་བདག་ཉིད་བསྒྲུབ་པ༌[^585]ལ་སློབ་པ་ནི་ལུས་དང་ངག་དང་ཡིད་ཀྱི་ལས་ཐབས་དང་བཅས་པ་ལ་སློབ་པར་བྱེད་པ་ཉིད་དོ། །

[Block 782]
གོ་རིམ་དེ་དག་གི༌[^586]བསྡུས་པའི་དོན་དེ་ལ། ཇི་ལྟར་ན་བྱང་ཆུབ་སེམས་དཔའི་མོས་པ་མང་བ་ཡིན་ཞེ་ན་ཞེས་བྱ་བ་ལ། འདིའི་བསྡུས་པའི་དོན་ནི་གང་ལ་མོས་པ་སྤྱད་པ་དང་གང་གིས་མོས་པ་ཞེས་བྱ་བའོ། །

[Block 783]
དད་པ་དང་དང༌[^587]བ་སྔོན་དུ་འགྲོ་བས་ཏེ། དད་པའི་མཚན་ཉིད་ནི་དང་བའོ། །

[Block 784]
ངེས་པ་གང་ལ་དེ་སྔོན་དུ་འགྲོ་བ་ཡོད་པ་ནི་རྒྱུ་དེས་ན་འདོད་པ་སྐྱེ་བར་འགྱུར་ལ། དེ་དང་ལྡན་པའི་མོས་པ་གང་ཡིན་ཞེ་ན། ངེས་པའི་དངོས་པོ་ལ་དེ་ཉིད་དུ་ངེས་པར་འཛིན་པའི་མཚན་ཉིད་དོ། །

[Block 785]
མོས་པའི་གནས་རྣམ་པ་བརྒྱད་ནི། དཀོན་མཆོག་དང་། ཡོན་ཏན་ལ་སོགས་པའི། །[^588]མོས་པའི་གནས་བརྒྱད་པོ་མདོར་བསྡུས་པ་ནི། མཆོག་ལ་མོས་པ་དང་། ཟབ་ཅིང་རྒྱ་ཆེ་བ་ལ་མོས་པ་དང་། རྒྱུ་དང་འབྲས་བུའི་མཚན་ཉིད་ཅན་གྱི་ཚོགས་ལ་མོས་པ་དང་། ཐོབ་པར་བྱ་བ་ལ་མོས་པའོ། །

[Block 786]
སངས་རྒྱས་དཀོན་མཆོག་གི་ཡོན་ཏན་ལ་མོས་པ་ནི། ཐོབ་པར་བྱ་བ་ལ་མོས་པའོ། །

[Block 787]
སྒྲུབ་པའི་ཐབས་ནི་སྒྲུབ་པའི་ཆོས་ཐོབ་པའི་ཐབས་སུ་གྱུར་པ་ལེགས་པར་གསུངས་པའི་བསྟན་པའི་ཆོས་སོ། །

[Block 788]
རྣམ་གྲངས་དེ་ལས་གཞན་ཡང་གནས་ལ་མོས་པ་བསྟན་པ་དང་། དེའི་རབ་ཏུ་དབྱེ་བ་ལ་མོས་པ་སྟེ། འདི་ལྟར་མདོར་བསྡུས་པ་གཞན་གནས་ལ་མོས་པས་བསྟེན་པ་དང་། རབ་ཏུ་དབྱེ་བ་ལ་བརྟེན་པའོ། །

[Block 789]
འདི་ལྟར་མདོར་བསྡུས་པ་གཞན་ཡང་དཀོན་མཆོག་གསུམ་གྱི་ཡོན་ཏན་དང་། དེའི་རབ་ཏུ་དབྱེ་བ་ལ་བརྟེན་པའོ། །

[Block 790]
དེ་ལས་གཞན་ཡང་བསྟན་པ༌[^589]རྣམ་པ་བདུན་ཏེ། ཇི་ལྟར་བྱས་ནས་ཤེ་ན་སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན་གྱི་ཡོན་ཏན་ལ་མོས་པ༌[^590]བྱས་པ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའི་མཐུ་ལ་མོས་པ་དང་། ཆོས་ཀྱི་ཡོན་ཏན་ལ་མོས་པ་བྱས་པ། དེ་ཁོ་ནའི་དོན་ལ་མོས་པ་སྟེ། དོན་དམ་པའི་ཆོས་ཡིན་པ་ཉིད་ཀྱིས་དེ་ཁོ་ནའི་དོན་ཏོ། །

[Block 791]
དགེ་འདུན་གྱི་ཡོན་ཏན་ལ་མོས་པའི་སྟོབས་ཉིད་ཀྱིས་རྒྱུ་དང་འབྲས་བུ་ལ་མོས་པ་སྟེ། རྒྱུ་འདི་ལས་འབྲས་བུ་འདི་འཐོབ་པོ་ཞེས་བྱ་བའོ། །

[Block 792]
ལམ་རབ་ཏུ་བསྒོམ་པ༌[^591]ཉིད་ཀྱིས་བྱང་ཆུབ་སེམས་དཔའི་གནས་སྐབས་ཀྱི་ཐོབ་པར་བྱ་བ་ལ་མོས་པ་སྟེ། སངས་རྒྱས་དཀོན་མཆོག་གི་ཡོན་ཏན་ལ་མོས་པ་ལས་རབ་ཏུ་བྱུང་བའོ། །

[Block 793]
ཆོས་དཀོན་མཆོག་གི་ཡོན་ཏན་ལ་མོས་པ་ལས་བྱུང་བ་ནི་ཐོབ་པར་བྱ་བའི་ཐབས་ལ་མོས་པའོ། །

[Block 794]
འདིར་ཐོབ་པའི་ཐབས་ནི་སྒྲུབ་པའི་ཆོས་ཏེ། བྱང་ཆུབ་ཀྱི་ཕྱོགས་ཀྱི་ཆོས་ཐམས་ཅད་དོ། །

[Block 795]
ལེགས་པར་གསུངས་པ་ལ་མོས་པ་ནི། ཆོས་དཀོན་མཆོག་གི་ཡོན་ཏན་ལ་མོས་པ༌[^592]བྱས་པ་ཉིད་དེ། བསྟན་པའི་ཆོས་ལ་ཆོས་ཞེས་བྱས༌[^593]ནས་སོ། །

[Block 796]
མོས་པ་ལ་གོམས་པ་ལན་མང་དུ་བྱེད་པ་དང་ཞེས་བྱ་བ་ནི། ཇི་སྲིད་བཟོད་པ་ཆེན་པོ་མ་བསྐྱེད་ཀྱི༌[^594]བར་དུའོ། །

[Block 797]
བཟོད་པ་དྲག་པོ་ཡོད་པ་ནི་ལྷག་པའི་བསམ་པ་དག་པ༌[^595]ཉེ་བར་གནས་པའི་གནས་སྐབས་སུ། [^596]རྒྱུ་དང་འབྲས་བུ་ཡང་དག་པར་སྟོན་པའི་རྣམ་པ་ཞེས་བྱ་བ་ལ། ཡང་དག་པར༌[^597]ཞེས་བྱ་བ་ནི། ཕྱིན་ཅི་མ་ལོག་པའོ། །

[Block 798]
རྒྱུ་དང་འབྲས་བུ་ནི་རྗེས་སུ་མཐུན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 799]
བྱས་པ་ཆུད་མི་ཟ་ཞིང་བསལ་བར༌[^598]བྱེད་ཅེས་བྱ་བ་ལ། བྱས་པའི་ལས་རྣམས་ཀྱིས་ངེས་པར་འབྲས་བུ་སྦྱིན་པའོ། །

[Block 800]
མ་བྱས་པ་དང་ཕྲད་པར་མི་འགྱུར་བ་ཞེས་བྱ་བ་ནི། མ་བྱས་པའི་ལས་རྣམས་ལས༌[^599]འབྲས་བུ་འབྱུང་བར་མི་འགྱུར་བའོ། །

[Block 801]
ཕ་རོལ་ཀླན་ཀ་ཚོལ་བ་བརྗོད་པའི་ཡོན་ཏན་སྟོན་པའི་རྣམ་པ་དང་ཞེས་བྱ་བ་ནི། ཀླན་ཀ་ཚོལ་བ་ཞེས་བྱ་བ་ལ། འདིར་ཉེ་བར༌[^600]ཞེས་བྱ་བའི་སྒྲ་ནི་ཉེ་བར་བསྒྱུར་བའམ་བརྙས་པ་སྟེ། འདི་ལྟར་ཉེས་པ་བརྗོད་ཅིང་རྒོལ་བ་དང་། སྐྱོན་ནས་བརྗོད་ཅིང་ཉེ་བར་བརྗོད་པའམ། གཞན་དག་ལ་བརྙས་པའི་ཚིག་གིས་སྐྱོན་ནས་བརྗོད་ཅིང་སྨྲས་པའོ། །

[Block 802]
དེ་ཉིད་ནི་ཕན་ཡོན་ཏེ། དེས་སྟོན་པའི་རྣམ་པའོ། །

[Block 803]
འདི་ལྟ༌[^601]བུ་སྨྲ་བ་ལས་ཞེས་བྱ་བ་ལ། གཞན་ལས་འོས་པ་ནི་འདི་ལྟ་བུ་སྨྲས་པའོ།[^602] །དེ་ལྟ་བུ་ལས་ཐར་པ་ནི་དེ་ལྟ་བུ་སྨྲ་བ་ལས་ཐར་པའོ། །

[Block 804]
དེ་ཉིད་ནི་ཕན་ཡོན་ཏེ། གཞན་དག་གི་སྨྲས་པ༌[^603]ནི་སྐྱོན་འདི་དང་འདི་ལྟ་བུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 805]
སྐད་ཀྱི་དབྱིངས་ཀྱི་ངོ་བོ་སྒྲུབ་པ་རྣམ་པར་གཞག་པ་སྟོན་པའི་རྣམ་པ་ཞེས་བྱ་བ་ལ། དབྱིངས་ཀྱི་ངོ་བོ་རྣམ་པར་གཞག་པ་ནི་དབྱིངས་ཀྱི་ངོ་བོ་རྣམ་པར་གཞག་པ་སྟེ། དབྱིངས་ཀྱི༌[^604]ངོ་བོ་འདི་ཞེས་རྣམ་པར་གཞག་པ་དེ༌[^605]སྟོན་པའི་རྣམ་པའོ། །

[Block 806]
ཚིག་ལེགས་པར་སྦྱར་བ་ནི་ལེགས་པར་སྦྱར་བའི་བརྗོད་པ་སྟེ། ཕན་ཡོན་ནོ། །

[Block 807]
དབྱངས་སམ་ཡི་གེ་ཉམས་པ་དང་ལྡན་པའི་སྔགས་ཀྱིས་ནི། ཉམས་པས་དོན་མི་འགྲུབ་སྟེ། ངག་གི་རྡོ་རྗེ་དེས་སྒྲུབ་པ༌[^606]པོ་ཉིད་ཉམས་པར་བྱེད་དོ། །

[Block 808]
དེ་སྟོན་པའི་རྣམ་པ་ནི་ལེགས་པར་སྦྱར་བའི་ཐབས་ཀྱིས་ཏེ། འདི་ལྟ་བུའི་ཕན་ཡོན་སྟོན་པའི་རྣམ་པའོ། །

[Block 809]
ནད་ལ་མཁས་པ་སྟོན་པའི་རྣམ་པ་དང་ཞེས་བྱ་བ་ལ། ནད་འདིའི་མིང་ནི་འདིའོ་ཞེས་བྱ་བར་ནད་དེ་ལ་མཁས་པའོ། །

[Block 810]
ནད་ཅི་ལས་བྱུང་བ་ལ་མཁས་པ་སྟོན་པའི་རྣམ་པ་དང་ཞེས་བྱ་བ་ལ། འདི་ལས་ཀུན་དུ་བྱུང་བས༌[^607]ན་ནད་ཀུན་དུ་སློང་བ་ནི་ནད་ཅི་ལས་བྱུང་བའོ། །
--- END BLOCKS ---
