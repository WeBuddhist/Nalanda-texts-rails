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
[Block 5951]
བདེན་པ་སྨྲ་ཞེས་གྲགས་པ་དེ༌[^3800]ཇི་ལྟ་བུའི་བདེན་པ་ལ་གནས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ།

[Block 5952 [VERSE]]
འདི་ལྟར་བདེན་པ་བསྲུང་བའི་ཕྱིར། །
སྲོག་དང་རྒྱལ་སྲིད་གང་གཏོང་བ། །

[Block 5953]
ཞེས་བྱ་བ་སྨོས་ཏེ། གཟི་བྱིན་རབ་ཏུ་ཉམས་ཞེས་བྱ་བ་འདིས་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་སྡུག་བསྔལ་གྱི་འབྲས་བུ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5954]
འཕྲལ་གྱི་བདེན་པ་མི་འགྲུབ་པ། །ཞེས་བྱ་བ་ནི་མཐོང་བའི་ཆོས་ཀྱི་བདེན་པ་ཡང་མི་འགྲུབ་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5955]
འོན་ཀྱང་ཁྱོད་ནི་འཇིག་རྟེན་གཉི་ག་ལ་ཕན་པ་སྒྲུབ་པ་མ་ཡིན་ཏེ། གཞུང་ལུགས་ཀྱི་ཚུལ་ལ་ནི་ང་ཉིད་མཁས་སོ། །

[Block 5956]
ཆོས་ཀྱི་གཟི་ཕྱིན༌[^3801]རབ་ཏུ་ཉམས་སོ་ཞེས་བྱ་བ་དེས་ནི་ཅི་ཞིག་ཏུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ། [^3802]གཞུང་ལུགས་ཚུལ་སྤྱོད་ཅེས་བྱ་བའི༌[^3803]ཚིགས་བཅད་བརྩམས་སོ། །

[Block 5957]
ཤི་ནས་ནི་ངན་སོང་དུ་ལྟུང་བ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན།

[Block 5958 [VERSE]]
ཆོས་ཀྱི་གཟི་བྱིན་ཉམས་པའི་ཕྱིར་རོ། །
བརྫུན་སྨྲ་བཏང་ནས་བདེན་པ་ང་སྨྲ་སྟེ། །

[Block 5959]
ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་སྔར་བསྟན་པའི་དོན་སྡུད་པ་ཡིན་ཏེ། དེ་བས་ཤེས་ཞེས་བྱ་བ་སྤྱོད་པར་གྱུར༌[^3804]ན་ནི། ཆོས་ཀྱི་གཟི་བྱིན་ཉམས་པ་དང་། འཕྲལ་གྱི་བདེ་བ་མི་འགྲུབ་པ་དང་། ཤི་ནས་ངན་སོང་དུ་འགྲོ་བ་སྟེ། དེ་བས་ན་ཉེས་བ་དག་གིས་མི་རུང་བའི་ཚུལ་ཡིན་པའི་ཕྱིར། ཡོངས་སུ་དོར་བར་བྱའོ། །

[Block 5960]
མཁས་སྨྲ་བ༌[^3805]ཞེས་བྱ་བ་ནི་ལུགས་ཀྱི་བསྟན་བཅོས་ལ་མཁས་པའོ། །

[Block 5961]
གྲགས་དང༌[^3806]བདེ་བའི་དོན་དང་འགལ་བ་གང་། །ཞེས་བྱ་བ་ལ་གྲགས་པ་སྨོས་པས་ནི་མཁས་པ་ནི་མཆོད་པར་འོས་པའི་ཕྱིར་རོ།[^3807] །བདེ་བ་སྨོས་པས་ནི་འདོད་པ་རྣམས་གཟུང༌[^3808]ངོ་། །རེ་ཞིག་འདིས་ཅི་དང་འགལ་བ་ཡིན་ཞེ་ན། མཐུན་པ་དྲུག་གང་བསྟན་པ་དེ་སྟོན་པ་ཡིན་ཏེ། འགལ་བའི་དོན་དང་། གནོད་པ་དང་། མཐུན་པའི་དོན་དང་། འགལ་བའི་གནོད་པ་དང་། དོན་དང་མཐུན་པའི་གནོད་པ་དང་། འདི་བཞི་ནི་གཞུང་བཟང་པོ་ཞེས་མཁས་པ་མི་སྨྲ་སྟེ། དེ་ལྟར་དོན་དང་རྗེས་སུ་མཐུན་པ་དང་། གནོད་པ་དོན་དང༌[^3809]རྗེས་སུ་མཐུན་པར་བྱའོ་ཞེས་བྱ་བ་དང་། དང་དུ་ལེན་པར་གྱུར་པ་ཡིན་ཏེ། དེས་ན་ཕངས་པའི་སྲོག་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྩམས་པ་ཡིན་ཏེ། ཕངས་པའི་སྲོག་ཅེས་བྱ་བ་འདིས་ནི་ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུ་ཡོངས་སུ་སྤངས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5962]
ནང་མི་མཆི་མས་འཇུ་བ་ཞེས་བྱ་བས་ནི་བཟོད་པའི་འབྲས་བུ་སྤངས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5963]
རྒྱལ་སྲིད་བདེ་བ་ཡིད་དུ་འོང་བ་ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པའི་འབྲས་བུ་སྤངས་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5964]
[^3810]དེ་ལྟར་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི༌[^3811]འབྲས་བུ་གསུམ་པོ་ཡོངས་སུ་སྤངས་པ་ཡིན་ཏེ༌[^3812]ཞེས་བསྟན་ཏོ། །

[Block 5965]
དོན་འདི་ཇི་ལྟར་དོན་དང་མཐུན་པར་འགྱུར། །ཞེས་འདྲི་བ་ཡིན་ཏེ། དོན་དུ་འགྱུར་བ་ཅི་མཐོང་ན། །ཞེས་བྱ་བ་འདིས་ནི་ཇི་ལྟར་མཁས་པས་སྲོག་ཡོངས་སུ་གཏོང་བའོ། །

[Block 5966]
བདེན་པའི་ཚིག་ཅེས་བྱ་བ་དེ་ཉིད་བསྒྲུབ་པའི་ཕྱིར། དེ་བསྲུང་ཕྱིར་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དེ་བསྲུང་ཕྱིར་ནི་ཞེས་བྱ་བ་ནི་བདེན་པ་བསྲུང་བའི་ཕྱིར་རོ། །

[Block 5967]
དྲུང་དུ་འོངས་ཞེས་བྱ་བ་ནི། དེ་ལྟར་གཅིག་པུ་ཕུབ་དང་མཚོན་ཆ་མེད་པར་རོ། །

[Block 5968]
ངའི་ཞེས་བྱ་བ་ནི་གསད་པར༌[^3813]བྱ་བ་བཏང་བ་ལ་སོགས༌[^3814]པའོ། །

[Block 5969]
ཕྲེང་བ་མཛེས་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་ཕྱེད་ནི་ལོངས་སྤྱོད་པ་རྣམས་ཀྱི་ཡིད་དུ་འོང་བའི་དབང་དུ་བྱས་པའོ། །

[Block 5970]
བསོད་ནམས་ཀྱི༌[^3815]ཡོན་ཏན་ཡིན་པས་བསོད་ནམས་ཡོན་ཏན་ནོ། །

[Block 5971]
དེ་འགྲུབ་པ་ནི་བསོད་ནམས་ཡོན་ཏན་འགྲུབ་པ་སྟེ། བསོད་ནམས་ཡོན་ཏན་འགྲུབ་པ་དེས་ཁྱད་པར་དུ་འཕགས་པའོ། །

[Block 5972]
ཉོན་མོངས་པ་མེད་པར་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ངལ་བ་མེད་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5973]
དཀའ་ཐུབ་ནི་གང་གི་ཕྱིར་ཡོན་ཏན་འཕེལ་བའི་མཚན་ཉིད་དོ། །

[Block 5974]
མུ་སྟེགས་འགྲོ་བ་ཞེས་བྱ་བ་ནི་སྟེགས་ལ་བརྟེན་ནས་བསོད་ནམས་རབ་ཏུ་འགྲུབ་ཅིང་། ངན་པར་སྤྱོད་པ་དག་ལ་ཡིན་ཏེ། སྟེགས་དག་ཏུ་འགྲོ་བའི་ཉོན་མོངས་མེད་པར་བསོད་ནམས་ཐོབ་པ་ཡིན་པའི་ཕྱིར། འདིས་ནི་སྔར་བསགས་པའི་སྡིག་པ་བདེན་པ་ཉིད་ཀྱིས་དག་པར་བསྟན་ཏེ། དཀའ་ཐུབ་སྤྱོད་པ་དང་། མུ་སྟེགས་སུ་སྤྱོད་པ་འདི༌[^3816]གཉིས་ཀྱིས་བསོད་ནམས་དང་ཡོན་ཏན་འགྲུབ་པ་ཉིད་དུ་བསྟན་པ་ཡིན་ནོ། །

[Block 5975]
འགྲོ་བ་མཐའ་དག་ཁྱབ་པའི་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་མཐོང་བའི་ཆོས་གྱི་འབྲས་བུ་དང་། མངོན་པར་མཐོ་བ་དང་། ངེས་པར་ལེགས་པའི་དབང་དུ་བྱས་པའོ། །

[Block 5976]
འགྲོ་བ་མཐའ་དག་ཁྱད་པར་འཕེལ་བ་ནི་འགྲོ་བ་མཐའ་དག་ཁྱད་པར་འཕེལ་བའོ། །

[Block 5977]
འཇིག་རྟེན་གསུམ་ལས་འདའ་བའི་ཞེས་བྱ་བ་ནི་སའི་སྟེང་དང་། ནམ་མཁའ་དང་། མཐོ་རིས་ཏེ། དེ་ལྟ་བུའི་མཚན་ཉིད་ཀྱི་འཇིག་རྟེན་གསུམ་ལས་འདའ་བའི་ལམ་ནི་བདེ་བ་སྟེ། འདིས་ནི་མཐོང་བའི་ཆོས་ཀྱི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 5978]
ལྷའི་གནས་སུ་འཛུག་པའི་སྒོ་ཡང་ཡིན། །ཞེས་བྱ་བ་འདིས་ནི་བདེན་པ་མངོན་པར་མཐོ་བའི་ལམ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5979]
འཁོར་བའི་རྫོང་ལས་ཐར་པའི་ཟམ་པ༌[^3817]ཡིན། །ཞེས་བྱ་བ་འདིས་ནི་ངེས་པར་ལེགས་པའི་ལམ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5980]
ལྷ་ཡིས༌རབ་ཏུ་བསྒྲིབས༌[^3818]ཀྱང་གནས་མི་ནུས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ནི་བཅོས་སུ་མི་ནུས་པའི་ཕྱིར།[^3819] འཆི་བས་འཇིགས་པ་མེད་དོ་ཞེས་བྱ་བ་དེ་ཉིད་ཀྱི་དབང་དུ་བྱས་པའོ། །

[Block 5981]
དེ་ལྟར་ཞེས་བྱ་བ་ནི་འཆི་བ་བཅོས་སུ་མེད་པ་ཉིད་ཀྱིས་སོ། །

[Block 5982]
འཇིག་རྟེན་གྱི་ཆོས་ཀྱི་ཆོས་ཉིད་ལ་བརྟགས་ན་ཞེས་བྱ་བ་ཡིན་ཏེ། སྡིག་པ་བྱས་པས༌[^3820]རྗེས་སུ་འགྱོད་པར་འགྱུར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་ལྡོག་པ་མེད་པ་དང་འཇུག་པའི་ཚུལ་གྱི་དབང་དུ་བྱས་པའོ། །

[Block 5983]
སྡིག་པ་བྱས་ན་རྗེས་སུ་འགྱོད་པར་འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི་ལྡོག་པའི་ཚུལ་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5984]
དགེ་བའི་ལས་ཀྱང་ལེགས་པར་ཡོངས༌[^3821]མ་བྱས། །ཞེས་བྱ་བ་འདིས་ནི་འཇུག་པའི་ཚུལ་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5985]
ཕྱི་མའི་ཚེ་ལ་སྡུག་བསྔལ་འབྱུང་དུ་དོགས། །ཞེས་བྱ་བ་ནི་དེ་གཉིས་ཀའི་ཚུལ་མེད་པའི་ཕྱིར་རོ། །

[Block 5986]
གང་ལས༌[^3822]བདག་གི་ཡིད་ནི་འགྱོད་འགྱུར་བ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱིས་བདག་ནི་དེ་གཉི་གའི་དོན་གྱི་ཚུལ་མེད་པ་ཡིན་ཏེ།

[Block 5987 [VERSE]]
དེས་ན་འཆི་བའི་འཇིགས་པ་མེད་དོ་ཞེས་པའོ། །
ཕོངས་པ་རྣམས་ནི་སློང་དུ་འོངས་པ་ལ། །

[Block 5988]
ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་བསྟན་མ་ཐག་པ། དཀར་པོའི་ལས་ཀྱང་རབ་ཏུ་གོམས་བྱས་པ། །ཞེས་བྱ་བ་སྟེ། དཀར་པོའི་ཆོས་བྱས་པའི་ཕྱིར་རོ། །

[Block 5989]
ཆོས་ལ་གནས་པ་ཞེས་བྱ་བ་དེ་བསྟན་པའི་ཕྱིར། མགུ་བ་རྙེད་པར་འགྱུར་ཞེས་བྱ་བ་སྟེ། སློང་དུ་འོངས་པ་ལ་ནོར་ཐོབ་པས་མགུ་བ་ཡིན་ཏེ། ཕོངས་པ་རྣམས་མི་མགུ་བར་བྱས་པ་ནི་མེད་དེ་མ་དྲན་པའོ། །

[Block 5990]
བདག་གིས་བྱས་པར་ཡང་མི་དྲན་ཞེས་བྱ་བ་དེ་གང་ཡིན་ཞེ་ན་དེ་ཉིད་བསྟན་པའི་ཕྱིར། རིང་དུ་བརྟགས་ཏེ་བསམས་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །
--- END BLOCKS ---
