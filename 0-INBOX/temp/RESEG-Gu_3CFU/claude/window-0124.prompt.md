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

[Block 4346]
ལྕགས་ཀྱི་གར་བུ་ལ་ལུ་གུ་རྒྱུད་གདགས་པར་བྱའོ་ཞེས་གསུངས་པ་ཐམས་ཅད་ལ་ཡང་ཇི་ལྟ་བུ་ཞིག་བཅང་བར་བགྱི། ཉེ་བ་འཁོར་རིན་པོ་ཆེའི་རང་བཞིན་ལས་བྱས་པ་མ་གཏོགས་སོ་ཞེས་བཀའ་སྩལ་པ་དེ་ལྟ་བུའི་ཚིག་ཡོད་དོ། །

[Block 4347]
ར་གན་དང་ཟངས་དང་འཁར་བ་དང་ཤིང་གི་ལྷུང་བཟེད་དང༌[^2974]བདག་གིར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ལྷུང་བཟེད་ཅེས་བྱ་བའི་སྒྲར༌[^2975]ར་གན་ལ་སོགས་པ་སོ་སོ་དང་སྦྱར་རོ། །

[Block 4348]
དེ་དག་བདག་གིར་བྱས་པའམ་གཞན་ཡང་རུང་སྟེ། གལ་ཏེ་ཡོངས་སུ་སྤྱད་དགོས་པར་གྱུར་ན་སྨན་ཕོར་གྱིས་ཡོངས་སུ་སྤྱད་པས་སོ་ཞེས་བྱ་བ་ལ། དེ་དག་ཅེས་བྱ་བ་ནི་ར་གན་ལ་སོགས་པའི་ལྷུང་བཟེད་ལའོ། །

[Block 4349]
འབྲུ་མར་གྱི་སྣོད་ཀྱི་རྣམ་པ་ཉིད་ཀྱིས་ཤིན་ཏུ་འདི་མཐུན་པ་ཉིད་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་འདི་འཆང་བ་དང་། མངོན་པར་རྗེས་སུ་ཡི་རང་བའོ། །

[Block 4350]
གཞན་ཡང་རུང་སྟེ་ཞེས་བྱ་བ་ནི་བདག་གིར་མ་བྱས་པར་གན་ལ་སོགས་པའི་ལྷུང་བཟེད་འདི་ལ་ཡང༌[^2976]ཡོངས་སུ་སྤྱད་དགོས་པ་སྨན་དང་སྨན་ཕོར་གྱི་རིགས་པ་ཉིད་ཀྱིས་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4351]
སྨན་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ཡོངས་སུ་སྤྱད་དགོས་པ་བསལ་བའི་གཙོ་བོ་འདི་སྨན་དང་སྨན་ཕོར་གྱིས་ཡོངས་སུ་སྤྱད་དགོས་པའི་ཚིག་གོ། །

[Block 4352]
གསུངས་པའི་སྨན་དང་འབྲེལ་པ་ཉིད་ཀྱི༌[^2977]འབྲས་བུ་ངེས་པར་སྤྱོད་པ༌[^2978]ལ་ནི་མ་ཡིན་ཞེས་ཏེ། གཞན་དུ་ན་ཡང་མ་ཡིན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4353]
འདིར་གཞུང་ནི་ཉེ་བར་མ་བཞག་པ་དེ་རྣམས་ནི་ཉེ་བར་གཞག་པར་མི་བྱའོ་ཞེས་གསུངས་པའོ། །

[Block 4354]
གཞག་པར་བྱས་པ་ནི་སྨན་ཕོར་ཡོངས་སུ་ལོངས་སྤྱོད་པར༌[^2979]བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4355]
བྱིན་གྱིས་བརླབ་ཏུ་རུང་བ་ནི་གཉིས་ཏེ། ལྕགས་ལས་བྱས་པ་དང་ས་ལས་བྱས་པའོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ཅེས་བྱ་བར་སྦྱར་རོ། །

[Block 4356]
ལྷུང་བཟེད་འབའ་ཞིག་པ་འདིར་བསྟན་པའི་རིན་པོ་ཆེའི་ངོ་བོ་བརྗོད་པར་བྱ་སྟེ། ནོར་བུ་དང་མུ་ཏིག་དང་བཻ་ཌཱུརྱ་དང་མན་ཤེལ་དཀར་པོ་དང་བྱི་རུ༌[^2980]དང་དངུལ་དང་གསེར་དང་། རྡོའི་སྙིང་པོ་དང་སྤུག་དང་དམར་པོ་དང་གཡས་སུ་འཁྱིལ་བ་ལ་སོགས་པ་ནི་རིན་པོ་ཆེའི༌[^2981]ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་ནོར་བུ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^2982]ཤེལ་དག་འཕངས་སོ། །

[Block 4357]
སོགས་པ་ཞེས་སྨོས་པ་ནི་སངས་རྒྱས་ཀྱི་སྐུ་གདུང་ལ་སོགས་པ་དག་བསྡུ་བའོ། །

[Block 4358]
ཆུ་ཤེལ་དང་མེ་ཤེལ་དག་ལ་ཡང་འདིར་ནོར་བུའི་ཚིག་གིས་གཟུང་བ༌[^2983]ཉིད་དོ། །

[Block 4359]
ནོར་བུར་གྱུར་པའི་ཁབ་ལེན་གང་ཡིན་པ་དེ༌[^2984]ཡང་འདིས་འཕངས་པ་ཉིད་དོ། །

[Block 4360]
རྡོ་བར་གྱུར་པ་ལ་ནི་མ་ཡིན་ཏེ། དེར་རིན་པོ་ཆེ་ཉིད་མེད་པའི་ཕྱིར་རོ། །

[Block 4361]
འདིར་ནོར་བུ་ལ་སོགས་པ་བརྗོད་པའི་རིན་པོ་ཆེ་ལ་དཔེ་ཉིད་དུ་རིག་པར་བྱ་སྟེ་གཞན་དུ་རིན་པོ་ཆེའི་སྙིང་པོ་ལ་སོགས་པའི་དངོས་པོ་ཉིད་ལ་འདྲ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4362]
དངུལ་ཞེས་བྱ་བ་ནི་དངུལ་སྐྱའོ། །

[Block 4363]
གསེར་ཞེས་བྱ་བ་ནི་ས་ལེ་སྦྲམ་མོ། །

[Block 4364]
མདོ་ལས་འདི་གཉིས་སྨོས་པ་གང་ཡིན་པ་དེ་ནི་དཔེ་ཡིན་ཏེ། ནོར་བུ་དང་མུ་ཏིག་དང་བཻ་ཌཱུརྱ་དང་དུང་དང་མན་ཤེལ་དཀར་པོ་དང་བྱི་རུ་དང་དངུལ་དང་ས་ལེ་སྦྲམ་དང་རྡོའི་སྙིང་པོ་དང་སྤུག་དང་དམར་པོ་དང་གཡས་སུ་འཁྱིལ་པ་ལ་སོགས་པ་ལ་རེག་པར་བྱེད་ན་སྤང་བའི་ལྟུང་བ་ཞེས་བྱ་བ་ཚིག་ཏུ་བརྗོད་པར་བྱ་བའི༌[^2985]ཕྱིར་རྣམ་པར་འབྱེད་པ་ལས་འདིར་དབྱིག་གམ་གསེར་རམ་ས་ལེ་སྦྲམ་དུ་གྱུར་པ་འདི་གཉིས་ཀ་ཡང་སྙད་གདགས་སུ་རུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4365]
འདིའི་དོན་འདི་རྫས་གཅིག་པུ་ཉིད་དེ་རིན་པོ་ཆེ་ཉིད་དུ་སྙད་གདགས་སུ་རུང་བ་དང་བཅས་པ་རྫས་ཉིད་དང་བཅས་ཆ་གཅིག་པུ་ཉིད་ལ་འདིས་བསྟན་པ་ཉིད་དོ། །

[Block 4366]
དེ་ལྟར་ན་ཡང་ཟངས་མའི་སྙད་གདགས་སུ་རུང་བ་ལ་ནི་ཉེས་བྱས་སུ་རྣམ་པར་གཞག་པའོ། །

[Block 4367]
དེ་བས་ན་འདི་ནི་དཔེ་ཡིན་ཏེ་རིན་པོ་ཆེའི་རང་བཞིན་མ་ཡིན་པ་གཞན་ལ་ཡང་སྙད་གདགས་སུ་རུང་བ་ལ་ནི་ཉེས་བྱས་ཞེས་རྟོགས་པར་བྱའོ། །

[Block 4368]
གང་ཞིག་དེ་མངོན་པར་རྟེན་པ་སྙད་གདགས་སུ་རུང་བའི་མངོན་མཚན་ཅན་ལ་འདིར་ངོ་བོ་སྟེ། སྐྱེས་པ་ལ་སོགས་པ་ནི་མ་ཡིན་ཏེ། འདི་ལྟ་བུའི་མཚན་ཉིད་ཅན་ཁྱད་པར་མེད་པའི་ཕྱིར་གཉིས་པོ་འདི་དག་ལ་སྙད་གདགས་སུ་རུང་བ་ཉོ་ཚོང་གི་བྱ་བ་ཉིད་ནི་འདིར་མངོན་མཚན་ཅན༌[^2986]ལ་གཙོ་བོ་སྟེ། དེ་ལྟར་ན་ཡང་སྙད་གདགས་སུ་རུང་བའི་ཟངས་ལ་རེག་ན་ཞེས་བྱ་བ་ལ། སྙད་གདགས་སུ་རུང་བའི་ཚིག་སྟེ་མངོན་མཚན་ཅན་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4369]
དེ་བས་ན་མངོན་མཚན་ཅན༌[^2987]མ་ཡིན་པ་ལ་ཡང་པ་ཎ་ཉིད་ཀྱིས་སྙད་གདགས་སུ་རུང་བའི་རིན་པོ་ཆེར་གྱུར་པ་མ་ཡིན་པ་ལ་གཙོ་བོ་ཉིད་དུ་འདིར་ཉེས་བྱས་སུ་བྱ་བ་ཉིད་རྟོགས་པར་བྱའོ། །

[Block 4370]
དཔེར་ན་འགྲོན་བུ་རྣམས་ལ་སྟེ། འདི༌[^2988]རྣམས་ལ་ནི་སྤང་བར་བྱ་བ་ཉིད་མ་ཡིན་པར་ཤེས་པར་བྱ་སྟེ། རིན་པོ་ཆེ་ཉིད་ལ༌[^2989]རྫས་ལས་མེད་པའི་ཕྱིར་རོ། །

[Block 4371]
རིན་པོ་ཆེའི་རང་བཞིན་སྙད་གདགས་སུ་མི་རུང་བའི་མངོན་མཚན་ཅན་གྱི་རིན་པོ་ཆེ་དེ༌[^2990]ལ་སྙད་གདགས་སུ་མི་རུང་བ་ཉིད་ལ་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 4372]
ཐ་སྙད་རྫོགས་པ་ལ་ཡང་པ་ཎ་ཉིད་དུ་མངོན་མཚན་ཅན་ཉིད་ཀྱི༌[^2991]གཙོ་བོ་སྟེ། འདིར་རིན་པོ་ཆེའི་སྙིང་པོའི་བློ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4373]
གཞན་ཡང་ཡིད་ཆེས་པ་ལ་བདེ་བར་གནས་པ་ཉིད་སྤོབས་པ་ཡང་དག་པར་གནས་པའི་སྲེད་པ་དང་རྒྱགས་པ་དང་ང་རྒྱལ་རྣམས་ལ་དངོས་པོ་ཉིད་མ་ཡིན་སྟེ། བདག་ཏུ་བྱ་བ་ལ་རེག་པར་བྱེད་པ་དག་ལ་སྤང་བ༌[^2992]རྣམ་པར་གཞག་པ་ལ་རྒྱུ་ཡིན་ནོ། །

[Block 4374]
ཐ་སྙད་ལྷན་ཅིག་སྤྱོད་པ་དང་ཉོ་ཚོང་ལྷན་ཅིག་སྤྱོད་པ་འདི་བྱེད་པ་ཞེས་བྱ་བའི་ལན་རྣམ་པར་གཞག་པའོ། །

[Block 4375]
འདིར་ཐ་དད་པ་ལ་བཟུང་བ་སྟེ། འདི་འདིར་མཐར་ཐུག་པ་ཞེས་བྱ་བ་འདི་ནི་མདོར་བསྡུས་པའི་དོན་ཏོ། །

[Block 4376]
རིན་པོ་ཆེ་ལ་ཡང་ཁས་ལེན་པ་ཉིད་ཐམས་ཅད་དུ་བྱ་བ་བསྒྲུབ་པ་ལ་སྒྲིབ༌[^2993]བྱེད་དུ་གྱུར་པ་གཞི་བྱེད་པ་ལྷག་མ་ལ་ཡང་ཐོབ་པར་བྱེད་པ་པོ་རུང་བ༌[^2994]ལ་སོགས་པ་ཐམས་ཅད་ལ་འདི་རྣམ་པར་གཞག་པས་སོ། །

[Block 4377]
སྙད་གདགས་སུ་མི་རུང་བ་ལ་ནི་ན་སྨད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སྙད་གདགས་སུ་མི་རུང་བ་ནི་ཉོ་ཚོང་བྱར་མི་རུང་བ་སྟེ། དེ་ལ་རེག་པ་ལ་ཉེས་བྱས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4378]
འོག་མ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི༌[^2995]ཐ་སྙད་རྫོགས་པའི་བསླབ་པའི་གཞི་ལ་ཡང་ན་སྨད་པ་ཉིད་འདི་སྙད་གདགས་སུ་མི་རུང་བ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4379]
སྙད་གདགས་སུ་མི་རུང་བ་ཞེས་བྱ་བ་དེ་ཇི་ལྟ་བུ་ཞིག་ཡིན་པར་རིག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དེ་ནི་གས་པ་དང་ཆག་པ་དང་དུམ་བུ་དང་ཚིག་པ་དང་སྔོན་མ་སྤྱད་པ་དང་མ་བྱས་པ་དང༌[^2996]མཚན་དང་མི་ལྡན་པ་དང་བཅོས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ནི་ཞེས་བྱ་བ་ནི་སྙད་གདགས་སུ་མི་རུང་བའོ། །

[Block 4380]
གས་པ་ཉིད་དང་ཆག་པ་ཉིད་དང་ཞེས་བྱ་བ་ནི་སེར་ག་བྱུང་བ་སྟེ། འབྱར་ཀྱང་རུང་མ་འབྱར་ཀྱང་རུང་བ་དང་བུ་ག་བྱུང་བའོ། །
--- END BLOCKS ---
