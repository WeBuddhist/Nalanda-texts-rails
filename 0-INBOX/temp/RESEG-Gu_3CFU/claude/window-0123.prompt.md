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
[Block 4306]
ལན་ཇི་ལྟ་བར་འདི་རྣམས་ལ་གཙོ་བོ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 4307]
གང་གི༌[^2946]ཕྱིར་སྦྱིན་བདག་གི་ཤིན་ཏུ་གསལ་བ་བདག་པོ་ཉིད་དུ་ལྷག་པར་མོས་པས་ཞལ་ཏ་བྱེད་པའི་བདག་པོ་ཉིད་དུ་ཁས་ལེན་པ་ལ་གཞན་གྱི་བློ་དང་གཞན་གྱི་རྣམ་པར་རིག་བྱེད་དང་བདག་གིར་བྱེད་པ་ཉིད་ལ་ཤིན་ཏུ་གསལ་བ་ཉིད་དོ། །

[Block 4308]
གང་ཞིག་འདིར་ཞལ་ཏ་བྱེད་པ་ལ་བདག་པོ་ཉིད་དུ་ཁྱོད་ཀྱིས་ཁས་ལེན་ཞིང་འདི་ལྟར་སྤྲོ་བར་བྱེད་པ་འདི་འདིར་བདག་པོ་ཉིད་དུ་ཁས་ལེན་པར་རིག་པར་བྱའོ། །

[Block 4309]
ཡང་ཅིའི་ཕྱིར་བདག་ཏུ་བྱ་བ་མ་ཡིན་པ་ལ་གོ་བར་བྱེད་པ་དང་། བྱིན་གྱིས་བརླབས་པ་ཡོངས་སུ་སྐྱོང་བ་ཉིད་ཀྱིས་བདག་གི་འདི་གཙུག་ལག་ཁང་ལ་སོགས་པ་དང་འདྲ་བར་བསྲུང་བ་དང་བྱིན་གྱིས་བརླབ་པར༌[^2947]བགྱིའོ། །

[Block 4310]
འདིར་བདག་གི་བློ་ནི་འདི་ཡིན་ཏེ་བདག་ཏུ་བྱ་བས་ནི་མ་ཡིན་གྱི། བདག་ལ་བདག་ཏུ་བྱ་བའི་དབང་གིས་བསྒྲུབ་པ་ཡང་མ་ཡིན་ཏེ། འདི་སྐད་ཅེས་ཚེ་དང་ལྡན་པ་དགོངས་སུ་གསོལ་ཞེས་བྱ་བའི་ངོ་བོ་ལས་གང་ཞིག་བདག་དགེ་སློང་མིང་འདི་ཞེས་བགྱི་བས་དངོས་པོ་རུང་བ་མ་ལགས་པ་འདི་རྙེད་དེ་ཞེས་བྱ་བའི་ཚིག་འདི་དེ་ཇི་ལྟར་བདག་ཏུ་བྱ་བ་རུང་བ་ཉིད་ཁས་ལེན་པ་ནི་འདིར་བསྒྲུབ་པ་སྟེ། བདག་ཏུ་བྱ་བ་འོངས་པའི་དོན་དང་སྦྱར་བ་ནི་མ་ཡིན་ནོ། །

[Block 4311]
ཆོས་དང་ལྡན་པའི་དོན་མི་བདོག་པའི༌[^2948]རྐྱེན་ལས་གཞན་པ་ལ་མི་འཆགས་སོ་ཞེས་བྱ་བ་ལ། ཆོས་ལས་མི་འདའ་བའི་ཆོས་དང་ལྡན་པ་སྟེ། རང་གི་དོན་དུ་ཆོས་གོས་དང་སྨན་ལ་སོགས་པ་ཡོ་བྱད་དག་གོ། །

[Block 4312]
དེ་ནི་ཆོས་དང་ལྡན་པ་ཡང་ཡིན་ལ་དོན་ཡང་ཡིན་པས་ཆོས་དང་ལྡན་པའི་དོན་ཏེ། ཆོས་གོས་དང་སྨན་ལ་སོགས་པའི་དོན་ཏོ།[^2949] །དེའི་རྐྱེན་ཞེས་བྱ་བ་ནི་རྫས་གང་ཡིན་པ་སྟེ། རྫས་ཇི་ཙམ་གྱིས༌[^2950]ཆོས་དང་ལྡན་པའི་དོན་ཏེ། སྒྲུབ་པར༌[^2951]འགྱུར་བའོ། །

[Block 4313]
དེ་མི་བདོག་པར་གྱུར་པ་ལ་རུང་བ་འདི་རྣམས་གྲགས་པའོ། །

[Block 4314]
ཆོས་དང་ལྡན་པའི་དོན་མི་བདོག་པ་དེའི་རྐྱེན་ལས་གཞན་དུ་གྲགས་པ་མ་ཡིན་ནོ། །

[Block 4315]
གལ་ཏེ་བདོག་པ་ཉིད་རེ་ཞིག་རྐྱེན་རྫས་སུ་གྱུར་ན་ཆོས་དང་ལྡན་པའི་དོན་མེད་པར་ཡང་ལྷག་པར་གནས་ན་རུང་བ་འདི་རྣམས་ཀྱང་སྐྱེ་བར་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4316]
དེར་བྱས་པ་ཉིད༌[^2952]ཡང་རུང་བ་འདི་རྣམས་ཆོས་འདི་མ་ཡིན་པ་ལ་ལྟུང་བ་ཉིད་ཀྱི་ཕྱིར་དེ་བྱེད་པ་དང་། དེ་ལ་རེག་པ་དང་རེག་པར་བྱེད་པ་དག་ལ་སྤང་བའི་ལྟུང་བྱེད་སྐྱེད་པ༌[^2953]ཁོ་ན་ཡིན་ནོ༌[^2954]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4317]
འདིར་ལུང་ནི་ཆོས་གོས་སེམས་པར་བྱེད་ཅིང་ཐོབ་པར་གྱུར་པ་རྣམས་སྦྱིན་པ་པོའི་ལག་ཏུ་ཡིད་བརྟན་པས་བཅང་བར་བྱ་ཞེས་བྱ་བ་ཆོས་གོས་ལ་སེམས་པར་བྱེད་པའི་ཚིག་ཅེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4318]
ཆོས་གོས་ཀྱི་དོན་དུ་སེམས་པར་བྱེད་པའི་ཚིག་ནི་དཔེར་ཤེས་པར་བྱའོ། །

[Block 4319]
དེ་ལྟར་ཡང་ལམ་དུ་མཛའ་བོའི་དོན་དུ་ཡང་གཟུང་བར༌[^2955]བྱ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆུ་དང་མེའི་དོན་དུ་ཆུ་ཤེལ་དང་མེ་ཤེལ་དག་བཅང་བར་བྱ་བར་གསུངས་སོ། །

[Block 4320]
སྦྱོར་བ་དང་ཡང་མི་མཐུན་པ་ཉིད་ཀྱི་ཕྱིར་རབ་ཏུ་བྱུང་བ་རྣམས་ཀྱི་ལུས་འཚོ་བར་བྱ་བའི་དོན་དུ་བསོད་སྙོམས་ཙམ་ལ་ཡང་འདི་རྣམས་ཀྱིས་ལྷག་པར་འཆང་བ་ལ་རུང་བ་རྣམས་ལ་མི་འཇུག་པས་རྣམ་པར་རྟོག་པ་ཙམ་མམ་ཚིག་སྦྱོར་བ་ཙམ་འདིར་སྤོང་བ་ལ་གཙོ་བོ་ཡིན་པས་གཞན་ཉིད་དུ་ཐོབ་པས་སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན་རྣམས་ལ་བྱ་བ་བྱེད་པར་འགྱུར་རོ། །

[Block 4321]
རྣམ་པར་ཉམས་པར་གྱུར་པ་ཚངས་པར་སྤྱོད་པ་དང་བཅས་པ་རྣམས་ལ་ཡོ་བྱད་བཅུ་གསུམ་རྣམས་ལས་ཅིག་ཤོས་མ་ཚང་བས་རྗེས་སུ་གཟུང་བར༌[^2956]བགྱིའོ། །

[Block 4322]
ཕོངས་པ་རབ་ཏུ་དབྱུང་བ་དང་བསྙེན་པར་རྫོགས་པའི་རྟོགས་པ་དང་ལྡན་པ་རྣམས་ལ་ལྷུང་བཟེད་དང་ཆོས་གོས་བསྒྲུབ་པར་བགྱི་ཞེས་བྱ་བའི་དོན་གང་ཡིན་པ་དེ་ལ་ནི་ཆོས་དང་མི་ལྡན་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 4323]
བདག་པོ་རིང་བ་ཉིད་ཡིན་ན་ཡང་ཉམས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་བདག་པོ་སྦྱིན་བདག་གམ་ཞལ་ཏ་བྱེད་པ་རིང་བ་ཉིད་ཡིན་ཏེ། ཡུལ་ཐག་རིང་པོ་ཉིད་དུ་སོང་ཞིང་ཡུལ་གྱིས༌[^2957]བསྐལ་པ་ཉིད་ཡིན་ཡང་རུང་བ་དག་ལ་ཉམས་པ་མེད་དོ། །

[Block 4324]
བདག་ཉིད་ཀྱི་དོན་དུ་བཟའ་བ་བྱེད་དུ་གཞུག་ཏུ་རུང་ངོ་། །

[Block 4325]
དེ་བྱད་པ་ལ་དབུལ་བའི་ཕྱིར་ཀཱར་ཥཱ་པ་ཎ་བླང་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཕྲན་ཚེགས་རྣམས་ལས་འདི་ལ་སོགས་པའི་ལམ་དུ་བཟའ་བ་དང་རིན་པོ་ཆེ་ལ་སོགས་པ་རྣམས་འདི་སྤང་བའི་ཇི་སྲིད་དུ་སའི་རང་བཞིན་ཞེས་བྱ་བ་འདི་མཐར་དེ་བྱེད་པ་ཞེས་བྱ་བ་ནི་བཟའ་བ་བྱེད་པ་ལ་དབུལ་བའི་ཕྱིར་ཀཱར་ཥཱ་པ་ཎ་བླང་བ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4326]
འདིའི་ཆོས་དང་མི་ལྡན་པའི་དོན་མ་ཡིན་ཞེས་བྱ་བར་ཤེས་པར་བྱའོ་ཞེས་བྱ་བ་འདི་ལ་འདི་བསྟན་པ་སྟེ། རུང་བ་མེད་པས་ལེན་པ་རྗེས་སུ་གནང་བ་མ་ཡིན་ཞེས་བྱ་བའོ། །

[Block 4327]
འདི་ནི་རུང་བ་གཞན་བརྗོད་པ་སྟེ། དེ་བཞིན་དུ་རྗེས་སུ་གནང་བ་གཞན་རྣམས་ལ་ཡང་རིག་པར་བྱའོ། །

[Block 4328]
ལམ་རྒྱགས་ནི་རིན་པོ་ཆེ་མན་ཆད་ལས་སོ༌[^2958]ཞེས་བྱ་བ་ནི་རིན་པོ་ཆེ་མན་ཆད་ནས་ལམ་དུ་བཟའ་བ་ལེན་པ་རུང་བ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4329]
འདིར་གཞུང་ནི་དགེ་སློང་དག་གིས་ལམ་རྒྱགས་ཇི་ལྟ་བུ་མི་ཤེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བཟའ་བ་ལྔ་དང་བཅའ་བ༌[^2959]སྨོས་པ་ལྔ་དང་། རིན་པོ་ཆེ་ལྔ་དང་། རིན་པོ་ཆེར༌[^2960]སྨོས་པ་ལྔའོ། །

[Block 4330]
དེ་ལ་བཟའ་བ་ལྔ་གང་ཞེ་ན། འབྲས་ཆན་དང་། ཟན་དྲོན་དང་ཤ་དང་ཉ་ཤ་དང་སྣུམ་ཁུར་རོ། །

[Block 4331]
བཅའ་བར་སྨོས་པ་ལྔ་གང་ཞེ་ན། ཇི་ཙེ་དང་ཁྲེ་རྒོད་དང་རྒྱ་སྲན་དང་བྲ་རྒོད་དང་ཁྲེའོ། །

[Block 4332]
རིན་པོ་ཆེ་ལྔ་གང་ཞེ་ན། གསེར་དང་། དངུལ་དང་། བཻ་ཌཱུརྱ་དང་། ཤེལ་དང་། མུ་ཏིག་གོ། །

[Block 4333]
རིན་པོ་ཆེ་ལྔར་སྨོས་པ་གང་ཞེ་ན། ཞ་ཉེ་དང་རོ་ཉེ་དང་ཟངས་དང་། ཁྲོ་ཆུ་དང་། ལྕགས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4334]
མེའི་དོན་དུ་དགེ་སློང་གིས་མེ་ཤེལ་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ལ་འདི་ནི་ཆོས་དང་མི་ལྡན་པའི་དོན་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་འདི༌[^2961]བསྟན་པའོ། །

[Block 4335]
དེ་མ་སྦས་པར་གཞག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཏོར་བའི༌[^2962]སྐྱོན་བསལ་བའི༌[^2963]དོན་དུ་སྦ་བའོ། །

[Block 4336]
མ་སྦྱིན་པར་ལེན་པ་ལ་བསྟན་པར་མི་བྱའོ། །

[Block 4337]
དེའི་འབྲས་བུ་ཕྱུང་ནས་དེ་ལ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་མེ་ཤེལ་དེའི་འབྲས་བུ་མེ་ཞེས་བྱ་བ་ཕྱུང་ནས་རྐུན་པོ་དེ་ལ་མེ་སྦྱིན་པར་བྱའོ། །

[Block 4338]
ཆུའི་དོན་དུ་ཆུ་ཤེལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་ནི་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^2964]པའི་ཕྱིར་རོ། །

[Block 4339]
བསྲུང་བའི་ཆོ་ག་ནི་འདྲའོ་ཞེས་བྱ་བ་ནི་མེ་ཤེལ་དེ༌[^2965]འདི་མ་སྦས་པར་གཞག་པར་མི་བྱ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 4340]
ཡོ་བྱད་རྗེས་སུ་གནང་བར་རིན་པོ་ཆེ་བདག་གིར་བྱ་བའི་ཤན་བསྲེ་བར༌[^2966]མི་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་རྒྱ་ལ་སོགས་པའི་འཚོག་ཆས་ནི་ཡོ་བྱད་དེ་དེ་ནི་རྗེས་སུ་གནང་བ་ཡིན་ནོ། །

[Block 4341]
དེའི་རྗེས་སུ་གནང་བའི་ཁོངས་སུ་རིན་པོ་ཆེ་བདག་གིར་བྱ་བའི་ཤན་བསྲེ་བ༌[^2967]གཞུག་པར་མི་བྱ་བ་ཉིད་དོ། །

[Block 4342]
དེ་བས་ན་རིན་པོ་ཆེའི་རང་བཞིན་ལ་ཡང་འདིར་རྗེས་སུ་གནང་བ་ཉིད་དོ། །

[Block 4343]
གནོད་པར་བྱེད་པ༌[^2968]སྤང་བའི་ཆོ་ག་ལ་ཞེས་བྱ་བ་འདོད་པ་ལ། དོན་ནི་འདི་ཡིན་ཏེ། རྒྱ་ལ་སོགས་པ་རྗེས་སུ་གནང་བ་གང་ཡིན་པ་དེ་ལ་རིན་པོ་ཆེའི་རང་བཞིན་གྱི་རྒྱ་ལ་སོགས་པ་ལ་བདག་ཏུ་བྱེད་པ་གང་ཡིན་པ་དེའི་མཐའ་བྱས་པ་ཉིད་ནི་མ་ཡིན་ཏེ་རྗེས་སུ་མ་གནང་བ་ཉིད་དོ། །

[Block 4344]
དེ་ལ་རིན་པོ་ཆེའི་རང་བཞིན་བདག་ཏུ་བྱ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4345]
དེ་ལྟར་ཡང་ཕྲན་ཚེགས་རྣམས་ལ་འདིར་རྒྱ་ལ་སོགས་པ་ལ་རིན་པོ་ཆེའི་རང་བཞིན་བཀག་པའི་གཞུང་ངོ་། །གླེང་གཞི་རྣམས་ལས་ཀྱང་གསུངས་ཏེ། ཇི་སྐད་དུ་བཅོམ་ལྡན་འདས་ཀྱིས་དུད་པའི་སྨན་གཅེའུ་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་དང་། ཞུས་པ༌[^2969]ཇི་ལྟ་བུ་བཅང་བར་བགྱི། བཀའ་སྩལ་པ། ཉེ་བ་འཁོར་རིན་པོ་ཆེ་ལས་བྱས་པ་མ་གཏོགས་སོ།[^2970] །སྣར་བླུགས་པའི་སྤྱད༌[^2971]དང་འཕུལ་བའི་བཏུང་ཕོར་དང་ཁབ་དང་ཁབ༌[^2972]རལ་དང་མིག་སྨན་གྱི་གབ་ཙེ་དང་། སྨན་ཕོར་དང་རྐང་རྟེན༌[^2973]དང་ཁྲིའུ་དང་སྨན་གྱི་ནལ་ཟེ་བཅང་བར་བྱའོ། །
--- END BLOCKS ---
