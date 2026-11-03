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
[Block 666]
ཇི་ལྟ་བུ་ཞེ་ན། མཆོད་སྦྱིན་བྱས་པས་ཞེས་བྱ་བ་ལ་སོགས་པས་སོ། །

[Block 667]
གལ་ཏེ་འཇིག་རྟེན་འདིའི་འབྲས་བུ་གྲགས་པ་དང་། ཚིག་བཙུན་པོ་འདོད་ན་ནི་དེ་གཉི་ག་ཡང་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་ཕྱིར།

[Block 668 [VERSE]]
གྲགས་པས་ཀུན་ཏུ་རབ་ཏུ་གསལ་གྱུར་ཅིང་། །
མི་དབང་གཙུག་གི༌[^359]འོད་ཀྱིས་རྐང་བརྒྱན་པ། །
ཞེས་བྱ་བ་སྟེ་གོ་རིམས་བཞིན་དུ་སྦྱར་རོ། །
ཅི་ཞིག་འདོད་ཕྱིར་མིག་ནི་སྦྱིན་པར་བྱེད། །

[Block 669]
ཅེས་བྱ་བ་ནི་གང་གི༌[^360]དོན་དུ་བསྟན་པ་དེ་ཅི་ཞིག་མཐོང་ན། ཁྱོད་ཀྱིས་མིག་སྦྱིན་ཞེས་བྱ་བ་སྟེ། དེ་ཉིད་འདིར་ཡང་བསྟན་པ་ཡིན་ནོ། །

[Block 670]
ས་ཀུན་འཐོབ་ཕྱིར་དང་མཐོ་རིས་དང་ཐར་པ་སྟེ་འཇིག་རྟེན་ཕ་རོལ༌[^361]གྱི་འབྲས་བུའོ། །

[Block 671]
ས་ཀུན་ཐོབ་པ༌[^362]དང་མཐོ་རིས་འཐོབ་པ་ཞེས་བྱ་བ་འདི་གཉིས་ནི་མངོན་པར་མཐོ་བའི་དབང་དུ་བྱས་པའོ། །

[Block 672]
ཐར་པ་ནི་ཉན་ཐོས་དང་རང་སངས་རྒྱས་ཀྱི་འབྲས་བུ་སྟེ། འདིས་ནི་ངེས་པར་ལེགས་པ་འཐོབ་པའི་དབང་དུ་བྱས་པས་སོ། །

[Block 673]
གྲགས་པ་ནི་མཐོང་བའི་ཆོས་ཀྱི་འབྲས་བུའོ། །

[Block 674]
སློང་བ་རྣམས་མཐོང་བའི་ཆོས་ལ་འབྲས་བུའམ་དོན་མེད་པར་རོ།[^363] །འཇིག་རྟེན་བསྐྱབ་ཕྱིར་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་གོ་འཕང་ཐོབ་པར་བྱ་བའི་གནས་སྐབས་ཀྱི་དོན་ནོ། །

[Block 675]
སྨན་དཔྱད་ལས་བྱུང་བ༌[^364]ཞེས་བྱ་བའི་སྨན་དཔྱད་ལས་བྱུང་བ༌[^365]ཇི་ལྟ་བུ་ཞེ་ན། སྨྲས་པ་དལ་བུས་དང་མ་སྣད་པར་རོ། །

[Block 676]
ཡང་ན་སྨན་དཔྱད་ལས་བྱུང་བ་བཞིན་དུ་ཞེས་བྱ་བའི་སྨན་ཡིག་ལས་བྱུང་བ་བཞིན་དུ་སྟེ། ཕྱོགས་གང་དུ་མཚོན་གཏང་བར་བྱ་བ་དང་། ཇི་ལྟར་དབྱུང་བ་སྟོན་པ་ཡིན་ཏེ། དལ་བུས་བྱ་བ་དང་མ༌[^366]སྣད་པར་རོ། །

[Block 677]
དེ་ལྟར་ཕྱུང་བ་ལ་རབ་ཏུ་དགའ་བ་བཞིན་དུ་ཞེས་འབྱིན་པ་དངོས་ཏེ། ལས་ཀྱི་དུས་ན་སེམས་དང་བ་གང་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ་དེ་སྟོན་པ་ཡིན་ཏེ། སྦྱོར་བའི་ཚེ་ན་མཆོག་ཏུ་དགའ་བ་དང་། བྱིན་ནས་ཀྱང་ཡིད་དགའ་བར་བྱེད་པ་སྟེ། གང་བཅོམ་ལྡན་འདས་ཀྱིས༌[^367]གསུངས་པ་དེ་སྟོན་ཏོ། །

[Block 678]
སློང་བ་ནི་དོན་བསྒྲུབ་པའི་ཕྱིར་སློང་མོ་པའི་མིག་ཏུ་གནས་པར་གྱུར་པ་ནི་མིག་གིས་མཐོང་བར་བྱ་བའོ།[^368] །པདྨ་དང་བྲལ་བའི་པདྨའི་མཚོ་གང་ཡིན་པ་དེ་ནི༌[^369]པདྨའི་མཚོའོ། །

[Block 679]
དེ་ལྟ་བུའི་བཞིན་གང་ལ་ཡོད་པ་དེ་ནི་པདྨ་མེད་པའི་པདྨའི་མཚོ་འདྲ་བའི་གདོང་ངོ་། །གཞན་ལ་མེད་པའི་རབ་ཏུ་དགའ་བར་གྱུར། །ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་དང་ཐུན་མོང་མ་ཡིན་པའི་དགའ་བ་ཡིན་ཏེ། དེ་ལྟར་ན་སྐྱེ་དགུ་དང་རྒྱལ་པོ་ནི་དེ་ལྟར་སྐྱེ་དགུ་བདེ་ལ་རྒྱལ་པོ་ཡང་བདེ། མི་བདེ་ན་ཡང་དེ་བཞིན་ནོ་ཞེས་པའི་ཚིག་གིས་རྒྱལ་པོ་ཉིད་མྱ་ངན་སྐྱེས་པ་ཡིན་མོད་ཀྱི། འོན་ཀྱང་དགའ་བ་སྐྱེ་བ་ཡིན་ཏེ། འདི་ནི་སྐྱེ་བོ་གཞན་ལ་མེད་པའི་དགའ་བའོ། །

[Block 680]
བྲམ་ཟེའང་མིག་དང་ལྡན་པར་མཐོང་། །ཞེས་བྱ་བ་ནི་འཁོར་གྱིས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 681]
འཁོར་གཞན་རྣམས་ལ་མེད་པའི་རབ་ཏུ་དགའ་བ་དེ་ཉིད་མེད་པར་བསྟན་པའི་ཕྱིར། རྒྱལ་པོའི་བཙུན་མོའི་འཁོར་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིའི་དོན་ཡིན་ནོ། །

[Block 682]
ཨེ་མའོ་བརྟན་ཞིང་ཞེས་བྱ་བ་ནི་རང་གི་བདེ་བ་ལ་འདོད་པ་མེད་པའི་བརྟན༌[^370]པའོ། །

[Block 683]
ཨེ་མའོ་སྙིང་སྟོབས་ཆེ་ཞེས་བྱ་བ་ནི་རང་གི་མི་བདེ་བ་ལ་འཇིགས་པ་མེད་པའོ། །

[Block 684]
དེ་གཉི་གས་ཀྱང་ཤེས་རབ་ཀྱི་ཡོན་ཏན་བསྟན་ཏོ། །

[Block 685]
ཨེ་མའོ་སེམས་ཅན་ཕན་འདོགས་པ། །ཞེས་བྱ་བ་འདིས་ནི་སྙིང་རྗེའི་ཡོན་ཏན་སྟོན་ཏོ། །ཤེས་རབ་དང་སྙིང་རྗེ་དེ་གཉིས་ཀ་སྨོས་པ༌[^371]དེ་གཉིས་བསྒོམས་པས་བྱང་ཆུབ་པ་སྟེ། དེ་གཉིས་ཀ་ཡང་རྒྱུར་གྱུར་པའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའི་སྒྲུབ་པའོ། །

[Block 686]
མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་དང་། རབ་ཏུ་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་རྒྱུར་གྱུར་ཅིང་། དེ་གཉི་ག་ཡང་ཀུན་ནས་ཉོན་མོངས་པ་ཡང་མཐར་བྱེད་ཅིང་སྤོང་བས་ན་སེམས་དཔའ་ཆེན་པོའི་རབ་ཏུ་སྒྲུབ་པའོ། །

[Block 687]
དེ་བས་ན་ཞེས་བྱ་བ་ཉིད་སེམས་ཅན་ལ༌[^372]ཕན་འདོགས་པས་ནའོ། །

[Block 688]
ཡང་ན་ཤེས་རབ་དང་སྙིང་རྗེའི་ཡོན་ཏན་གཉིས་དང་ལྡན་པས་སོ། །

[Block 689]
ངོ་མཚར་ཆེ་བའི་སེམས་ཅན་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་བརྟན་པ་དང་། སྙིང་སྟོབས་ཆེ་བ་དང་། སེམས་ཅན་ལ་ཕན་འདོགས་པར་བྱེད་པ་སྟེ། སེམས་ཅན་ཞེས་བྱ་བ་ཉིད་སྨོས་པ་ཡིན་ནོ། །

[Block 690]
ཡུན་རིང་པོར་འདི་ལྟར་ཉོན་མོངས་སུ་གཞུག་པའི་མི་རིགས་ཞེས་བྱ་བ་འདི་ལྟར་བརྗོད་པར་འདོད་དེ། ཡོངས་སུ་ཉོན་མོངས་པ་ལ་འཇིགས་པ་མེད་པའི་རྒྱུར་གྱུར་པ། དེ་ཉིད་སེམས་ཅན་གྱི་ཡོན་ཏན་ཉིད་ཡིན་ཏེ། སེམས་ཅན་གྱི་ཡོན་ཏན་དུ་གཟུང་ངོ་། །མིག་གི་རྨ་ནི་སོས་ཞེས་བྱ་བ་ནི་མིག་གི་གནས་ཀྱི་རྨ་ཞེས༌[^373]བརྗོད་པ་ཡིན་ནོ། །

[Block 691]
མིག་གི་རྨ་ནི་སོས་ཞེས་བྱ་བའི་ཚིག་གིས་ནི་གནས་ཀྱིས་གནས༌[^374]པ་སྟོན་ཏེ། ཇི་ལྟར་རྒྱལ་པོ་མདུན་ས་ན་མི་སྣང༌[^375]ཡང་། རྒྱལ་པོའི་གནས་སུ་སྟོན་པ་དང་འདྲའོ། །

[Block 692]
བསྲབས༌[^376]ཤིང་སངས་པ་ཞེས་བྱ་བ་ལ་བསྲབས་པ༌[^377]ཡིན། སངས་པ་ཡིན་པས་བསྲབས་ཤིང་སངས་པའོ། །

[Block 693]
བཙུན་མོའི་འཁོར་དང་ཕོ་བྲང་འཁོར་གྱི་མི་རྣམས་ནི་བཙུན་མོའི་འཁོར་དང༌[^378]ཕོ་བྲང་འཁོར་གྱི༌[^379]མི་རྣམས་སོ། །

[Block 694]
བཙུན་མོའི་འཁོར་ཞེས་སྨོས་པས་ནི་བཙུན་མོའི་འཁོར་ན་སྤྱོད་པའི་སྐྱེ་བོ་ཡིན་པས་དེ་སྐད་ཅེས་བྱའོ། །

[Block 695]
ཡང་ན་བཙུན་མོའི་འཁོར་གྱི་སྒྲ་ཉིད་འཁོར་གྱི་མི་རྣམས་ལ་འཇུག་གོ། །

[Block 696]
བཙུན་མོའི་འཁོར་དང་ཕོ་བྲང་འཁོར་གྱི་མི་རྣམས་ཀྱི་མྱ་ངན་ནི༌[^380]བཙུན་མོའི་འཁོར་དང་ཕོ་བྲང་འཁོར་གྱི་མྱ་ངན་ནོ། །

[Block 697]
བསྲབས་ཤིང་སངས་པ༌[^381]ནི་བཙུན་མོའི་འཁོར་དང་ཕོ་བྲང་འཁོར་གྱི་མི་རྣམས་ཀྱི་མྱ་ངན་གང་ཡིན་པ་སྟེ། བཙུན་མོའི་འཁོར་དང་ཕོ་བྲང་འཁོར་གྱི་མི་རྣམས་ཀྱི་ཞེས་དེ་ལྟར་བསྡུ་བར་བྱའོ། །

[Block 698]
འདིར་རྒྱལ་པོ་ལ་ནི་མྱ་ངན་མེད་པ་ཡིན་ཏེ། འོན་ཀྱང་བཙུན་མོའི་འཁོར་དང་ཕོ་བྲང་འཁོར་གྱིས་ནི་རྒྱལ་པོ་དེ་མྱ་ངན་ཡོད་དེ། བཙུན་མོའི་འཁོར་ལ་སོགས་པའི་ཚིག་གི་འབྲེལ་པ་ཅུང་ཟད་ཡོད་དེ། སྐྱེ་དགུ་བདེ་ན་ནི་རྒྱལ་པོ་བདེ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 699]
དེ་བསྟན་པའི་ཕྱིར། རྒྱལ་པོ་དེ་ཉིད་ཀྱི༌[^382]མྱ་ངན་དང་བཅས་པ་ནི་གང་བཙུན་མོའི་འཁོར་ལ་སོགས་པ་ཡིན་ནོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 700]
རབ་ཏུ་དབེན་པ་འདོད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སྐྱེ་བ་གཞན་དུ་དབེན་པ་ལ་གོམས་པ་སྟོན་པའོ། །

[Block 701]
རྫིང་བུའི༌[^383]འགྲམ་ན་ཞེས་བྱ་བ་ནས་སྐྱིལ་མོ་ཀྲུང་བཅས་ཏེ་ཞེས་བྱ་བའི་བར་གྱི་ཚིག་གི་བསྡུས་པའི་དོན་ནི་མིག་གཉིས་མེད་པས་མིག་གི་ཡུལ་མ་བསྟན་ཏེ། རེག་བྱ་དང་། དྲི་དང་། སྒྲའི་ཡུལ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 702]
དེས་ཀྱང་ཡིད་དུ་འོང་བར་བསྟན་པ་ཡིན་ཏེ། ཇི་ལྟར་རིགས་པར་སྦྱར་བར་བྱའོ། །

[Block 703]
བརྒྱ་བྱིན་མདུན་དུ་འོངས་ནས་འདི་སུ་ཞེས་དྲིས་པ་སྟེ། མི་ལས་ཁྱད་པར་དུ་གྱུར་པ་ཞིག་ཡིན་པར་རྟོགས་སོ། །

[Block 704]
ཡང་ན་ལྷའི་དབང་པོ་ཉིད་ཀྱིས་རང་འོངས་པར་བརྡ་ཕྲད་པའི་ཕྱིར་རྐང་པའི་སྒྲ་བྱས་པར་གྱུར་ཏོ། །

[Block 705]
གཞན་དུ་ན་དྲི་བའི་སྐབས་མེད་པར་འགྱུར་རོ། །
--- END BLOCKS ---
