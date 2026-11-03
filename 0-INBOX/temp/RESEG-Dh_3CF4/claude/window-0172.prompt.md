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
[Block 6021]
དམ་པ་རྣམས་ནི་སུས་ཀྱང་མི་བསྲིང༌[^3852]ངོ་། །ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་དམ་པ་དག་དང་འགྲོགས་ན་གཏན་དུ་བ༌[^3853]ཡིན་པའི་ཕྱིར་རོ། །

[Block 6022]
དུལ་བའི་ཚུལ་གྱིས༌[^3854]དགེ་ལ་བསྟན་པར༌[^3855]བྱ། །ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་ཇི་ལྟར་འདོད་ཀྱང་རུང་སྟེ་ཞེས་བྱ་བ་ཡིན་ཏེ། དམ་པ་དག་དང་འགྲོགས་པ་ནི་བརྟན་པའི༌[^3856]ཕྱིར་རོ། །

[Block 6023]
དགེ་བདག་ལ་བསྟེན་པ༌[^3857]ཇི་ལྟར་བྱ་ཞེ་ན། སྨྲས་པ། དུལ་བའི་ཚུལ་དུ་བྱ་ཞེས་བྱ་བ་ཡིན་ཏེ། འདིས་ནི་གུས་པར་བྱེད་པའི་སྦྱོར་བ་ཉིད་དུ་སྦྱོར་བ་ཡིན་ནོ། །

[Block 6024]
དམ་པ་དག་དང་འགྲོགས་པ་ལ་དེ་གཉི་གའི་ཕན་ཡོན་བསྟན་པའི་ཕྱིར་སྨྲས་པ། དེ་དང་ཉེ་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་འོག་མ་ཡིན་ནོ། །

[Block 6025]
ཆེད་དུ་མ་བསྒྲུབས་པར་ཡང་ཞེས་བྱ་བ་ནི་བསྟན་བཅོས་ཉན་པ་ལ་སོགས་པའི་བྱ་བ་མ་བྱས་པར་ཡང་སྟེ། མ་བསྲིངས་པ་དེ་ཙམ་སྟེ། མ་བསྲིངས་པ་དང་དུལ་བའི་ཚུལ་ཙམ་གྱིས་སོ། །

[Block 6026]
དེ་དང་ཉེ་ན་ཞེས་བྱ་བ་ནི་དགེ་བ་དེ་དང་ཉེ་ནའོ། །

[Block 6027]
སྐྱེ་བོ་དམ་པ་དེའི་ཡོན་ཏན་ནི་དེའི་ཡོན་ཏན་ནོ། །

[Block 6028]
དེའི་ཡོན་ཏན་ཉིད་མེ་ཏོག་ཡིན་པས་ཡོན་ཏན་མེ་ཏོག་གོ། །

[Block 6029]
དེའི་རྡུལ་ནི་ཡོན་ཏན་གྱི་རྡུལ་ཏེ། འདི་ནི་དམ་པ་དང་འགྲོགས༌[^3858]པའི་ཕན་ཡོན་ནོ། །

[Block 6030]
[^3859]དེ་ལྟར་རེ་ཞིག་ཇི་ལྟར་འདོད་པར་ཕྲད་ཀྱང་རུང་སྟེ། དམ་པ་དག་དང་ལན་ཅིག་ཙམ། །ཞེས་བྱ་བ་འདི་ནི་རྗེས་སུ་བསྟན་པ་སྟེ། དམ་པ་རྣམས་ཀྱི་ཕན་ཡོན་ནོ། །

[Block 6031]
ཡང་ན་སྐྱེ་བོ་དམ་པ་ནི་བདག་ཉིད་ལ་ཕན་པར་ཞུགས་པ་ཡིན་ཏེ། དེ་བས་ན་སུས་ཀྱང་མི་བསྲིང༌[^3860]ངོ་། །དགེ་བ་ལ་བསྟེན་པར༌[^3861]བྱ་ཞེས་བྱ་བ་ནི་གཞན་ལ་ཕན་པར་འཇུག་པའོ། །

[Block 6032]
དེ་ནི་རབ་ཏུ་བརྟན་པ༌[^3862]ཉིད་དུ་འགྱུར། །ཞེས་བྱ་བ་དེ་རྗེས་སུ་བསྟན་པ་ལས་བརྩམས་ཏེ། རྒྱལ་པོའི་ཤིང་རྟ་རིན་ཆེན་གསེར་གྱིས་བརྒྱན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། ལུས་ཀྱང་རྒས་པས་མི་སྡུག་པར་ཡང་འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི་ཕྱི་རོལ་གྱི་དངོས་པོར་འགྱུར་བ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 6033]
ནོར་བུ་གསེར་གྱིས་བརྒྱན་ཞེས༌[^3863]སྨོས་པ་ནི་གཟུགས་གནས་པ་ཉིད་དུ་རིགས་པ་ཡིན་ན་ཡང་ཕྱིས་རྒས་པས་མི་སྡུག་པར་འགྱུར་བ་ཡིན་ན་གཞན་དག་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་པའོ། །

[Block 6034]
རྒྱལ་པོ་ཞེས་སྨོས་པས་ནི་མངོན་པར་སྦྱར་བའི་ཁྱད་པར་དང་ལྡན་པའི་ཤེས་པ་ཡིན་ཏེ། དེའི་ཤིང་རྟ་བསྟན་པའི༌[^3864]ཕྱིར་རོ། །

[Block 6035]
རྒྱལ་པོའི་ལུས་རིན་པོ་ཆེ་གསེར་གྱིས་བརྒྱན་པ་ཡང་རྒས་པས་མི་སྡུག་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི་ནང་གི་དངོས་པོ་ཡང་རྣམ་པར་འགྱུར་བ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 6036]
དམ་པ་རྣམས་ཀྱི་ཆོས་ནི་རྒས་མི་འགྱུར། །ཞེས་བྱ་བ་འདིས་ནི་གང་སྔར་བསྟན་པའི་རབ་ཏུ་བསྟན་པ༌[^3865]ཉིད་དུ་འགྱུར་ཞེས་བྱ་བ་དེའི་རྒྱུ་ཉིད༌[^3866]བསྟན་ཏོ། །ཅིའི་ཕྱིར་དམ་པ་རྣམས་ཀྱི་ཆོས་རྒས་པར་མི་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ། དགེ་བ་རྣམས་ནི་གང་གི་ཕྱིར་ཡོན་ཏན་ལ་རྗེས་སུ་ཆགས་པ༌[^3867]བརྟན་པར་འགྱུར་བས་དམ་པ་རྣམས་ཀྱི་ཆོས་ནི་རྒས་པར་མི་འགྱུར་བ་སྟེ། ཡོན་ཏན་ལ་གོམས་པར་བྱ་བའི༌[^3868]ཕྱིར། སྐྱེ་བོ་འགྲོགས་པ་དེ་དག་ལ་ཡོན་ཏན་གཞན་དུ་མི་འགྱུར་ཏེ། དེ་གོམས་པར་བྱས་པས་ཇི་ལྟར་གཞན་དུ་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 6037]
འདྲིས་པར་བྱ་བ་མི༌[^3869]དགོས་པར། །ཞེས་བྱ་བ༌[^3870]དེ་རྗེས་སུ་བསྟན་པ་ལས་བརྩམས་ཏེ། ནམ་མཁའ་དང་ནི་ས་གཞིའི་བར་ཡང་རིང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་ཡིན་ཏེ། ནམ་མཁའ་བར་རབ་ཏུ༌[^3871]རིང་བ་ཡིན་ཏེ།

[Block 6038 [VERSE]]
གང་ལས་ཤེ༌[^3872]ན་ས་ལས་སོ། །
ས་ཡང་རབ་ཏུ་རིང་བ་ཡིན་ཏེ།
གང་ལས་ཤེ༌[^3873]ན་ནམ་མཁའ་དང་ངོ་། །

[Block 6039]
ཕ་རོལ་ཚུ་རོལ་འགྲམ་ཡང་རིང་བ་ཡིན་ཏེ། ཕ་རོལ་དང་ཕ་རོལ་མ་ཡིན་པའོ། །

[Block 6040]
ཡང་ན་ས་དང་ནམ་མཁའ་གཅིག་རིང་བ་ཡིན་ནོ། །

[Block 6041]
དེ་བཞིན་དུ་ཕ་རོལ་དང་ཚུ་རོལ་གྱི་འགྲམ་ཡང་ཕ་རོལ་དང་ཚུ་རོལ༌[^3874]གྱི་འགྲམ་ཉིད་དོ། །

[Block 6042 [VERSE]]
ཤར་ནུབ་གཉིས་ཀྱི་རི་བར་དེ་བས༌[^3875]རིང་། །
ཕལ་དང་དམ་པའི་ཆོས་ཀྱང་དེ་བས་རིང་། །

[Block 6043]
ཞེས་བྱ་བ་ནི་ཕན་ཚུན་དེ་བས་རིང་བའོ། །

[Block 6044]
ཅིའི་ཕྱིར་ནམ་མཁའ་དང་སའི་བར་རབ་ཏུ་རིང་བ་དང་། རྒྱ་མཚོའི་ཕ་རོལ་དང་ཚུ་རོལ་རབ་ཏུ་རིང་བ་དང་། ཤར་ནུབ་གཉིས་ཀྱི་རི་རབ་ཏུ་རིང་བ་སྟེ། ཅིའི་ཕྱིར་དཔེ་གསུམ་པོ་འདི་དག་ཉིད་གཟུང་གི། གཞན་མ་ཡིན་ཞེ་ན། ཆོས་འདི་ནི་ཚུལ་ཁྲིམས་དང་། ཏིང་ངེ་འཛིན་དང་། ཤེས་རབ་ཀྱི་མཚན་ཉིད་ཡིན་ཏེ། ནམ་མཁའ་དང་རིང་བ་ཉིད་ཀྱིས་ནི་ཚུལ་ཁྲིམས་ལས་བརྩམས་པ༌[^3876]ཡིན་ཏེ། ནམ་མཁའ་ལྟ་བུ་ནི་དམ་པ་རྣམས་ཀྱི་ཆོས་ཏེ། ཚུལ་ཁྲིམས་ཀྱི་མཚན་ཉིད་དོ། །

[Block 6045]
མི་དགེ་བ་ཐམས་ཅད་ཀྱིས་གོས་པའམ། སྤགས་པ་དེས་ན་ས་ལྟ་བུ་ནི་དམ་པ་མ་ཡིན་པའི་ཆོས་ཏེ། མི་གཙང་བ་ཐམས་ཅད་ཀྱིས་གོས་པ་དེས་སོ། །

[Block 6046]
ཏིང་ངེ་འཛིན་ནི་རྒྱ་མཚོའི་ཕ་རོལ་དང་ཚུ་རོལ་ལྟ་བུ་ཡིན་ཏེ། རྒྱ་མཚོའི་ཕ་རོལ་ལྟ་བུ་ནི་དམ་པ་རྣམས་ཀྱི་ཏིང་ངེ་འཛིན་གྱི་མཚན་ཉིད་ཀྱི་ཆོས་ཏེ། བསྟེན་པ་དག་ལ་རྗེས་སུ་འཛིན་པ་དང་སྦྱོར་བ་ནི་ཆུ་དང་འདྲ་བ་ཉིད་ཀྱི་ཕྱིར་དང་། སྤྱོད་པའི་ཚད་ཏིང་ངེ་འཛིན་ནི་སྤྱོད་པའི་མཐར་ཐུག་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 6047]
ཚུ་རོལ་གྱི་འགྲམ་ལྟ་བུ་ནི་དམ་པ་མ་ཡིན་པའི་ཆོས་ཏེ། དེ་གཉི་གའི༌[^3877]མེད་པའི་ཕྱིར་རོ། ། ཤེས་རབ་ལས་བརྩམས་ཏེ། ཤར་ནུབ་གཉིས་ཀྱི་རི་བར་དེ་བས་རིང་། །ཞེས་བྱ་བ་ཡིན་ཏེ། ཤར་གྱི་རི་ལྟ་བུ་ནི་དམ་པ་རྣམས་ཀྱི་མཚན་ཉིད་ཀྱི་ཆོས་ཏེ། ཇི་ལྟར་ཉི་མ་ཤར་བ་ལ་བརྟེན་པ་དེ་བཞིན་དུ་དམ་པ་རྣམས་ཀྱི་ཆོས་ཤེས་རབ་ཀྱི་ཉི་མ་འཆར་བའི་གནས་ཡིན་ནོ། །

[Block 6048]
ནུབ་པའི་རི་ལྟ་བུ་ནི་དམ་པ་མ་ཡིན་པ་རྣམས་ཀྱི་ཆོས་ཏེ། ཤེས་རབ་ཀྱི་ཉི་མ་ནུབ་པ་ལ་བརྟེན་པའོ། །

[Block 6049]
ཚིགས་བཅད་འདི་བཞི་ཐོས་པས། སུ་དཱ་སའི་བུ་དུལ་བར་གྱུར་ཏེ། བདག་ཉིད་ཀྱི་གནས་སྐབས་དང་། རྗེས་སུ་མཐུན་པའི་ཚིགས་བཅད་ཡིན་ཏེ། དེ་དག་གིས་སོ། །

[Block 6050]
ཇི་ལྟར་ཕྲད་ཀྱང་རུང་སྟེ། དགེ་བའི་བཤེས་གཉེན་དང་ཕྲད་ཅིང་བསྙེན་བཀུར་བྱས་ན་སྡུག་བསྔལ་ལས་ཐར་བ་དང་། དམ་པ་དག་དང་འགྲོགས་པའི་སྟོབས་ཡིན་པའི་ཕྱིར་ཡང་ངོ་། །དམ་པ་དང་དམ་པ་མ་ཡིན་པའི་ཆོས་འདི་གཉིས་ནི་རབ་ཏུ་བསྐལ་པ༌[^3878]ཡང་ཡིན་ཏེ། ནམ་མཁའ་དང་ནི་ས་གཞིའི་བར་ཡང་རིང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདི་དང་སྦྱར་རོ། །

[Block 6051]
འདྲིས་པར་བྱ་བ་མི་དགོས་པར། །ཞེས་གོང་དུ་བསྟན་པ་ལ་འདི་སྐད་སྨྲས་ཏེ།[^3879] དམ་པ་མ་ཡིན་པ་དང་འགྲོགས་པ་ལ་ཡང་འདྲིས་པར་བྱ་བ་མི་དགོས་པ་ཉིད་དུ་སྟོན་ཏེ། ཅིའི་ཕྱིར་དམ་པ་མ༌[^3880]ཡིན་པ་དང་འདྲིས་པར་བྱ་བ་མི་དགོས་པས་དམ་པ་མ་ཡིན་པ་དང་མི་འགྲོགས་པ་ཡིན་ཞེ་ན། དེས་ན་དམ་པ་དང་དམ་པ་མ་ཡིན་པའི་ཆོས་ནི་རབ་ཏུ་རིང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་བརྩམས་ཏེ། དམ་པ་དང་དམ་པ་མ་ཡིན་པའི་ཆོས་ཐག་རིང་བ་ནི། དམ་པ་དང་འགྲོགས་པ་ཡིན་ཡང་བསྐལ་པ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར་ཁྱོད་ཀྱི༌[^3881]ཚིགས་སུ་བཅད་པ་སྙན་པ་དང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 6052]
རབ་ཏུ་གསལ་བར་འཕགས་པའི་དོན་གྱི་ཚིག་གང་ཡིན་པ་དེ་ནི་ཚིག་དང་དོན་ཀྱང་རབ་ཏུ་གསལ་བར་འཕགས་པའོ། །

[Block 6053]
ཚིག་ཅེས་བྱ་བ་ནི་ལུས་སོ། །

[Block 6054]
དོན་རབ་ཏུ་གསལ་བར༌[^3882]འཕགས་པ་ནི་སྲོག་གོ། །

[Block 6055]
ཚིགས་སུ་བཅད་པ་ནི་ང་རྒྱལ་ལོ། །

[Block 6056]
སྙན་པ་ནི་རྒྱན་ཏེ། དེ་དེ་ལྟར་རྣམ་པ་བཞི་དང་ལྡན་པའི་སྙན་དངགས༌[^3883]བསྟན་པ་ཡིན་ནོ། །

[Block 6057]
གང་ལ༌[^3884]མཉན་པ་དང་། གང་མཉན་པ་དང་། མཉན་པ་དེའི་འབྲས་བུ་དང་བཅས་པ་དེའི་དབང་དུ་བྱས་ནས། ཁྱོད་ཀྱི་ཚིགས་སུ་བཅད་པ་སྙན་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 6058]
གང་ལས་མཉན་པ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ལས་སོ། །

[Block 6059]
གང་མཉན་པ་ཡིན་ཞེ་ན། ཡོན་ཏན་བཞི་དང་ལྡན་པའི་སྙན་དངགས་སོ།[^3885] །གང་ཉན་པ༌[^3886]ཡིན་ཞེ་ན། སུ་དཱ་སའི་བུའོ། །

[Block 6060]
མཉན་པ་དེའི་འབྲས་བུ་གང་ཡིན་ཞེ་ན། དེ་ཐོས་དགའ་བར་གྱུར་པའོ། །
--- END BLOCKS ---
