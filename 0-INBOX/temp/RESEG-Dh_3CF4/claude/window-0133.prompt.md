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
[Block 4656]
བརྩོན་འགྲུས་རབ་ཏུ་བསྐྱེད༌[^3016]ནས་ཀྱང་། །དེའི༌[^3017]མཐུ་རྩལ་གང་ཡིན་པ་དེ་ནི། བརྩོན་འགྲུས་རབ་ཏུ་བསྐྱེད་པའི་མཐུ་རྩལ་ཆེན་པོའོ། །

[Block 4657]
བཟློག་པ་ནི་དགག་པར་རིགས་པའོ། །

[Block 4658]
དེ་བས་ན་ཁྱོད་ཀྱིས་ཁྱད་པར་དུ་ཆེ་བའི་དཀའ་བ་བྱས་སོ་ཞེས་བྱ་བ་སྟོན་པ་ཡིན་ནོ། །

[Block 4659 [VERSE]]
བདག་གིས་དཀའ་བ་སྤྱད་དོ༌[^3018]སྙམ། །
ཞེས་བྱ་བའི་ཚིགས་བཅད་དོ། །
བཟང་པོ་ཁྱོད་ནི་མིར་གྱུར་ཀྱང་། །

[Block 4660]
ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་ཀྱི་དོན་ཡང་ངོ་མཚར་ཆེ་བར་རྟོགས་པ་དེ་བསྟན་པ་དང་། དེ་བསྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 4661]
བདག་གིས་དཀའ་བ་སྤྱད་དོ་སྙམ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་དེ་བསྒྲུབ་པའི༌[^3019]ཕྱིར་རོ། །

[Block 4662 [VERSE]]
འཆི་བདག་ཁ་ཡི་ནང་འདྲ་བའི། །
ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །
བདག་གི༌[^3020]དཀའ་བ་སྤྱད་དོ་སྙམ། །
ང་ནི་ང་རྒྱལ་སྐྱེས་པར་གྱུར། །

[Block 4663]
ཅེས་བྱ་བ་ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 4664 [VERSE]]
འཆི་བདག་ཁ་ཡི་ནང་འདྲ་བ། །
འཇིག་རྟེན་གཞན་ནས་བླངས་པ་བཞིན། །

[Block 4665]
ཞེས་བྱ་བ་སྟེ། དེ་བས་ན་ང་རྒྱལ་སྐྱེས་པར་གྱུར་པའོ། །

[Block 4666]
ཧ་ཅང་དཀའ་བ་ཁྱོད་སྤྱོད་ཀྱིས། །དེ་ཡང་རིང་དུ་སྤངས་པར་གྱུར།[^3021] །ཅེས་བྱ་བ་ནི། ཅིའི་ཕྱིར་ཞེ་ན། འདི་ལྟར།

[Block 4667 [VERSE]]
གཡང་ས་འདི་ནས་ངས་ཕྱུང་ན། །
ཁྱོད་ནི་གཞན་དུ་ལྷུང་བར་གྱུར། །

[Block 4668]
ཅེས་བྱ་བ་སྨོས་པའོ། །

[Block 4669 [VERSE]]
གཡང་ས་འདི་ནས་ཕྱུང་བ༌[^3022]ནི། །
འདིའི་རྩ་བའི་གཡང་ས་ནས་ཕྱུང་བའོ། །

[Block 4670]
གཞན་དུ༌[^3023]ལྷུང་བ་ནི་ངན་སོང་གི་སྐྱེ་བའི་ངོགས་ཀྱི་གཡང་སར་རོ། །

[Block 4671]
དེ་ལྟ་བུའི་དཀའ་བ་སྤྱད་པ་འདིའི་རྒྱུ་གང་ཡིན་ཞེ་ན། དེའི་རྒྱུ་བསྟན་པའི་ཕྱིར། སྤྱོད་པ་ངན་པ་ཁྱོད་ཅི་རུང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4672]
སྤྱོད་པ་ངན་པ་ནི། འཇུག་པ་ངན་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4673]
སྤྱོད་པ་ངན་པའི་མཚན་ཉིད་ཇི་ལྟ་བུ་ཞེ་ན། དེ་སྨྲས་པ། ཤིན་ཏུ་མི་བཟད༌[^3024]པའི་སྤྱོད་པ་ངན་པའོ། །ཇི་ལྟ་བུ་ཞེ་ན། དེ་བསྒྲུབ་པའི༌[^3025]ཕྱིར། གང་གིས་སྡུག་བསྔལ་རྣམས་སུ་ལྷུང་། །ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4674]
འགྲོ་བ་གང་ལྷུང་ཞེ་ན། སྨྲས་པ། བདེ་བ་འདོད་པ༌[^3026]རྣམས་ཡིན་ཏེ། མཐོང་བའི་ཆོས་ལ་བདེ་བ་འདོད་པས། །སྡིག་པ་རྣམས་བྱེད་དེ། དེ་ནི་མི་ཤེས་པ་ཞེས་བྱ་བས་བསྟན་ཏོ། །

[Block 4675]
གང་གིས་སྡུག་བསྔལ་རྣམས་སུ་ལྷུང་། །ཞེས་བསྟན་པ་དེའི་སྡུག་བསྔལ་གྱི་རྣམ་པ་དུ་ཞེ་ན། དེའི་སྡུག་བསྔལ་གྱི་རྣམ་པ་བསྟན་པའི་ཕྱིར། བདག་ཉིད་ངན་འགྲོ་རྣམས་སུ་ལྷུང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 4676]
སྡུག་བསྔལ་ཡང་རྣམ་པ་གཉིས་ཏེ། འཇིག་རྟེན་ཕ་རོལ་གྱི་ངན་འགྲོའི་སྡུག་བསྔལ་དང་། མཐོང་བའི་ཆོས་ལ་བྱས་པའི༌[^3027]སྡུག་བསྔལ་ལོ། །

[Block 4677]
ངན་འགྲོ་རྣམས་སུ་ལྷུང་ཞེས་བྱ་བ་ནི། བདག་ཉིད་ཀྱི་འཇིག་རྟེན་ཕ་རོལ་གྱི་སྡུག་བསྔལ་ལོ། །

[Block 4678]
ད་ནི་མཐོང་བའི་ཆོས་ཀྱི་བདག་གིས་ཉེས་པར་བྱས་པའི་སྡུག་བསྔལ་ཡིན་ཏེ། ང་ལའང་མྱ་ངན་མེ་ཡིས་གཏོར། །ཞེས་བྱ་བ་སྟེ། མཐོང་བའི་ཆོས་ལ་བྱས་པའི་སྡུག་བསྔལ་ལོ། །

[Block 4679]
བདག་ཉིད་ཀྱི་མཐོང་བའི་ཆོས་ཀྱི་སྡུག་བསྔལ་ཡང་རྣམ་པ་གཉིས་ཏེ། གྲགས་པའི་དཔལ་ནི་མེད་པར་བྱས། །ཞེས་བྱ་བ་འདིས་ནི། སྔར་བཤད་པའི་གྲགས་པ་ཉམས་པའི་སྡུག་བསྔལ་བསྟན་ཏོ། །

[Block 4680]
ཡོན་ཏན་ལ༌[^3028]དགའ་བ་ནི་ཡོན་ཏན་ལ་དགའ་བའོ། །

[Block 4681]
འགལ་བར་གྱུར་པ་ནི༌[^3029]ཉམས་པར་བྱས་པའོ། །ཇི་ལྟར་གྲགས་པའི་དཔལ་ཉམས་པར་བྱས་ཤེ་ན། དེ་སྨྲས་པ། ངན་པར་སྨྲ་བའི་གཞིར་ཡང་གྱུར། །ཅེས་བྱ་བ་ཡིན་ཏེ། ངན་པར་སྨྲ་བའི་གཞིར་འགྲོ་བའི་རྒྱུའོ། །ཇི་ལྟར་ཡོན་ཏན་ལ་དགའ་བ་འགལ་བར་གྱུར་ཅེ་ན། སྨྲས་པ། ཡིད་ཀྱང་བརྟན་དུ་མ་རུང་ངོ་། །ཞེས་བྱ་བ་ཡིན་ཏེ།

[Block 4682 [VERSE]]
ཡིད་བརྟན་པ་ཉམས་པའི་རྒྱུས་སོ། །
དོན་ནི་ཅི་ཞིག་འགྲུབ་པར་འགྱུར། །

[Block 4683]
ཞེས་བྱ་བ་ནི། དེ་ལྟར་འཇིག་རྟེན་གཉི་ག་ལ་མི་ཕན་པའི་ལས་བྱས་པས་དོན་ཅི་ཞིག་འགྲུབ་པར་འགྱུར་བའོ། །

[Block 4684]
ཇི་ལྟར་འདི་ཉིད་ང་ཡི་ཡིད་ལ་གནོད༌[^3030]གྱུར་པ། ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་པའི་ཕྱིར། སྨྲས་པ། སྡིག་པ་ཅན་དུ་གྱུར་པ་ཞེས་བྱ་བ་ཡིན་ཏེ། འདིར་ངན་པར་སྤྱོད༌[^3031]པའོ། །

[Block 4685]
ངན་པར་སྤྱོད་པ་འདི་ནི་ངས་མེད་པར་བྱ་བར་མི་ནུས་ཏེ། འདི་མེད་པར་ཞེས་སྨོས་སོ། །

[Block 4686]
ངན་པར་སྤྱོད་པ་འདི་ཇི་ལྟར་མེད་པར་གྱུར་ཏེ། དེའི་འབྲས་བུ་རྗེས་སུ༌[^3032]མྱོང་བས་དེའི་འབྲས་བུ་མྱོང་བ་བསལ་བར་མི་ནུས་སོ། །

[Block 4687]
བརྟེན༌[^3033]དུ་མི་རུང་དོགས་པར་གྱུར་ཀྱང་ཞེས་བྱ་བ་དེ་བཤད་པའི་ཕྱིར། ཁྱོད་ནི་གཅིག་པུ་ལུས་ཀྱང་ཉམ་ཆུང་ལ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་ཕྱེད་དང་པོས་བསྟན་ཏོ། །

[Block 4688]
རྒྱུ་བཞིས་དོགས་པར་གྱུར་པ༌[^3034]ཡིན་ཏེ། གྲོགས་མེད་པའི་ཕྱིར་དང་། བདག་ཉིད་ཉམ་ཆུང་བའི་ཕྱིར་དང་། ལམ་མི་ཤེས་པའི་ཕྱིར་དང་། འཇིགས་པ་དང་བཅས་པའི་གནས་སུ་འཁྱམ་པའོ། །

[Block 4689]
གང་དང་ལྷན་ཅིག་འགྲོ་བ་དང་། གང་འགྲོ་ཞིང་སྟོབས་དང་ལྡན་པ་དང་། གང་ནས༌[^3035]འགྲོ་བ་ཤེས་པ་དང་། གང་གནས་སུ་འགྲོ་བ་སྟེ། སྐྱོན་བཞི་པོ་འདི་དག་དང་ལྡན་པའི་ཕྱིར་དོགས་པར་འགྱུར་བ་ཡིན་ཏེ། གང་དོགས་པ་དེ་ལ་བརྟེན༌[^3036]ཏོ། །

[Block 4690]
གང་ལས་དོགས་པ་དེ་ལས་བརྩམས་ཏེ། འགའ་ཞིག་འོངས་ནས་ཞེས་བྱ་བ་སྨོས༌[^3037]ཏེ། འགའ་ཞིག་ཅེས་བྱ་བ་གཅན་གཟན༌[^3038]ཁྲོ་བོ་རྣམས་ལའོ། །

[Block 4691]
དགོན་པ་བགྲོད༌[^3039]དཀའ་འཇིགས་པ་འོང༌[^3040]ལ་ཞེས་བྱ་བ༌[^3041]གྲོང་གི་གན་དུ་ཕྱིན་པའོ། །ཇི་ལྟར་གྲོང་གི་གན་དུ་ཕྱིན་པར་ཤེས་པར་བྱ་ཞེ་ན། དགོན་པ་དང་ནགས་ཀྱི་མཐའ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4692]
བདེ་བར་སོང་ཞེས་བྱ་བ་འཇིགས་པ་མེད་པར་ཅི་བདེར་དེངས་ཤིག་པའོ། །

[Block 4693]
སྡིག་པའི་ལས་ཀྱང་ཡོངས་སུ་སྤང་བར་འབད་པར་གྱིས། །ཞེས་བྱ་བ་ནི། ཅིའི་ཕྱིར་ཞེ་ན། སྡུག་བསྔལ་གྱི་རྣམ་པར་སྨིན་པ་ནི་ངེས་པའི་ཕྱིར་རོ། །

[Block 4694]
འགྱོད་པའི་མེ་ཞེས་བྱ་བ་དང་། མཛེའི་ནད་ཅེས་བྱ་བ་འདི་གཉིས་ཀྱིས་ནི་མིང་དང་། གཟུགས་ལུས་ཀྱི་སྡུག་བསྔལ་བསྟན་ཏེ། དེའི་ལས་དང་། སྡིག་པ་མཐོང་བའི་ཆོས་ཉིད་ལ་དེ་ལྟར་སྡུག་བསྔལ་བར་འགྱུར་བ་ལས་བརྩམས༌[^3042]ཏེ། དེའི་ལས་ལུས་འཇིག་པ༌[^3043]ལ་ནི་མི་སྤྱོད་པས་སོ། །

[Block 4695]
རྨའི་ཞིགས་བ་ནི་རྨ་ཞིགས་པའོ། །
--- END BLOCKS ---
