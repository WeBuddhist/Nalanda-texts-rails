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
[Block 4236 [HEADING]]
#### ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ་སོགས་པའི་མིང། ^5-1-4-0

[Block 4237]
འདི་བརྗོད་པར་བྱ་སྟེ། ཅི་ནམ་མཁའ་མཐའ་ཡས་སྐྱེ་མཆེད་ལ་སོགས་པ་དེ་དག་ནམ་མཁའ་ལ་སོགས་པ་ཁོ་ན་ལ་དམིགས་པ་ཡིན་པས་དེའི་ཕྱིར་དེ་སྐད་ཅེས་བྱའམ་ཞེ་ན། མ་ཡིན་ནོ། །

[Block 4238]
[^3057]འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། རེ་ཞིག་གསུམ་མོ། །

[Block 4239 [VERSE]]
[^3058]རྣམ་ཤེས་མཐའ་ཡས་མཁའ་མཐའ་ཡས། །
ཅི་ཡང་མེད་ཅེས་བྱ་དེ་ལྟར། །

[Block 4240]
སྦྱོར་ཕྱིར༌[^3059]གྲངས་བཞིན་དུ་ནམ་མཁའ་མཐའ་ཡས་སོ། །

[Block 4241]
རྣམ་པར་ཤེས་པ་མཐའ་ཡས་སོ། །

[Block 4242]
ཅི་ཡང་མེད་དོ་ཞེས་དེ་ལྟར་ཡིད་ལ་བྱེད་ཅིང་དེ་དག་ལ༌[^3060]རབ་ཏུ་སྦྱོར་བས་དེའི་ཕྱིར་དེ་དག་གི༌[^3061]མིང་དེ་དག་ཡིན་ནོ། །

[Block 4243]
དམན་ཕྱིར་འདུ་ཤེས་མེད། འདུ་ཤེས་མེད་པ་ཡང་མ་ཡིན་པའོ། །

[Block 4244]
འདུ་ཤེས་ཆུང་བའི་ཕྱིར་འདུ་ཤེས་མེད་འདུ་ཤེས་མེད་མིན་ཞེས་བཤད་དེ། དེ་ནི་འདུ་ཤེས་གསལ་བ་ཡང་མ་ཡིན་ལ་འདུ་ཤེས་མེད་པ་ཁོ་ན་ཡང་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4245]
གལ་ཏེ་དེ་ལ་ཡང་འདི་ལྟར་འདུ་ཤེས་ནི་ནད་དོ། །

[Block 4246]
འདུ་ཤེས་ནི་འབྲས་སོ། །

[Block 4247]
འདུ་ཤེས་ནི་ཟུག་རྔུའོ། །

[Block 4248]
འདུ་ཤེས་མེད་པ༌[^3062]ནི་ཀུན་དུ་རྨོངས་པའོ། །

[Block 4249]
འདི་ལྟར་འདུ་ཤེས་མེད། འདུ་ཤེས་མེད་མིན་སྐྱེ་མཆེད་འདི༌[^3063]ནི་ཞི་བའོ། །

[Block 4250]
འདི༌[^3064]ནི་གྱ་ནོམ་པའོ་ཞེས་བྱ་བར་སྦྱོར་བ་ཡོད་མོད༌[^3065]ཀྱི་ཅིའི་ཕྱིར་དེ་དག་གིས་དེ་ལ་དེ་ལྟར་འཛིན་ཞེས་བྱས་པ་དང་། འདུ་ཤེས་རྣམས་ཆུང་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་འདི་གདོན་མི་ཟ་བར་བརྗོད་དགོས་པར་འགྱུར་བས་དེ་ཉིད་བཤད་དོ། །

[Block 4251 [HEADING]]
#### སྙོམས་འཇུག་དངོས་གཞིའི་རྫས་བརྒྱད། ^5-1-5-0

[Block 4252]
དེ་ལྟར་སྙོམས་འཇུག་དངོས་གཞིའི་རྫས། །རྣམ་པ་བརྒྱད། དེ་ལྟར་ན་འདི་དག་ནི་སྙོམས་པར་འཇུག་པའི་དངོས་གཞིའི་རྫས་བརྒྱད༌[^3066]ཡིན་ཏེ། འདི་ལྟ་སྟེ། བསམ་གཏན་བཞི་དང་། གཟུགས་མེད་པ་བཞིའོ། །

[Block 4253]
དེ་དག་ལས་བདུན་རྣམ་པ་གསུམ། །སྲིད་པའི་རྩེ་མོ་ལས་གཞན་པ་བདུན་ནི་རྣམ་པ༌[^3067]གསུམ་ཡིན་ཏེ། རོ་མྱང་ལྡན་དང་དག་པ་དང་། །ཟག་མེད། རོ་མྱང་བ་དང་མཚུངས་པར་ལྡན་པ་རྣམས་དང་། དག་པ་པ་རྣམས་དང་། ཟག་པ་མེད་པ་རྣམས་སོ། །

[Block 4254]
བརྒྱད་པ་རྣམ་པ་གཉིས། [^3068]སྲིད་པའི་རྩེ་མོ་ནི་རོ་མྱང་བ་དང་མཚུངས་པར་ལྡན་པ་དང་། དག་པ་པ་ཡིན་གྱི་ཟག་པ་མེད་པ་ནི་མེད་དོ། །

[Block 4255]
དེ་ལ།

[Block 4256 [HEADING]]
##### རོ་མྱང་བ་དང་མཚུངས་པར་ལྡན་པ། ^5-1-5-1-0

[Block 4257 [VERSE]]
རོ་མྱང་མཚུངས་ལྡན་སྲེད་བཅས་སོ། །
རོ་མྱང་བ་ནི་སྲེད་པ་ཡིན་ནོ། །

[Block 4258 [HEADING]]
##### དག་པ། ^5-1-5-2-0

[Block 4259]
འཇིག་རྟེན་པ་ཡི་དགེ་བ་ནི། །

[Block 4260]
དག་པ། འཇིག་རྟེན་པའི་དགེ་བ་སྙོམས་པར་འཇུག་པའི་རྫས་ནི་དག་པ༌[^3069]ཞེས་བྱ་སྟེ། མ་ཆགས་པ་ལ་སོགས་པ་ཆོས་དཀར་པོ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 4261]
རོ་མྱང་བ་དང་མཚུངས་པར་ལྡན་པ་དེས་ཅི་ཞིག་རོ་མྱོང་བར་བྱེད་ཅེ་ན། དེ་ནི་དེས་མྱང་བྱ། སྙོམས་པར་འཇུག་པའི་རྫས་གང༌[^3070]འདས་མ་ཐག་པ་དེ་ནི་དེས༌[^3071]རོ་མྱོང་བར༌[^3072]བྱེད་དེ། རོ་མྱང་བར་བྱ་བ་གང་ཡིན་པ་དེ་ལས་ནི་ལངས་པ་ཡིན་ནོ། །

[Block 4262]
[^3073]གང་གིས་རོ་མྱོང༌[^3074]བར་བྱེད་པ་དེ་ལ་ནི་སྙོམས་པར་ཞུགས་པ་ཡིན་ནོ། །

[Block 4263 [HEADING]]
##### ཟག་མེད། ^5-1-5-3-0

[Block 4264]
ཟག་མེད་འཇིག་རྟེན་འདས་པའོ། །

[Block 4265]
འཇིག་རྟེན་ལས་འདས་པའི་སྙོམས་པར་འཇུག་པའི་རྫས་གང་ཡིན་པ་དེ་ནི་ཟག་པ་མེད་པ་ཡིན་ནོ་

[Block 4266 [HEADING]]
#### བསམ་གཏན་གྱི་ཡན་ལག། ^5-1-6-0

[Block 4267]
སྙོམས་པར་འཇུག་པའི་རྫས་དེ་དག་ལས་བསམ་གཏན་རྣམས་ཁོ་ན་ཡན་ལག་དང་ལྡན་པ་ཡིན་གྱི་གཟུགས་མེད་པ་རྣམས་ནི་མ་ཡིན་ནོ། །

[Block 4268 [HEADING]]
##### བསམ་གཏན་དང་པོ་ལ་ཡན་ལག་ལྔ། ^5-1-6-1-0

[Block 4269]
དེ་ལ་དང་པོ་ལ་ལྔ། བསམ་གཏན༌[^3075]པོ་ལ༌[^3076]ཡན་ལག་ལྔ་སྟེ། རྟོག་དཔྱོད་དང་། དགའ་བས༌[^3077]བདེ༌[^3078]དང་ཏིང་འཛིན༌[^3079]རྣམས། །རྟོག་པ་དང་། དཔྱོད་པ་དང་། དགའ་བ་དང་། བདེ་བ་དང་། སེམས་རྩེ་གཅིག་པ་ཉིད་དེ། དེ་ལྟར་ན་དེ་དག་ནི་ཡན་ལག་ལྔ་ཡིན་ནོ། །

[Block 4270]
ཏིང་ངེ་འཛིན་ནི་ཡན་ལག་ཀྱང་ཡིན་ལ་བསམ་གཏན་ཡང་ཡིན་ནོ། །

[Block 4271]
ལྷག་མ་རྣམས་ནི་ཡན་ལག་དག་ཡིན་ནོ་ཞེས་གྲག་གོ། །

[Block 4272]
ཡན་ལག་བཞི་པའི་དམག་ཇི་ལྟ་བར་ཡན་ལག་ལྔའི་བསམ་གཏན་ཡང་དེ་དང་འདྲའོ། །

[Block 4273 [HEADING]]
##### བསམ་གཏན་གཉིས་པ་ལ་ཡན་ལག་བཞི། ^5-1-6-2-0

[Block 4274]
གཉིས་པ་ལ་ནི་ཡན་ལག་བཞི། རབ་དང་དད་ནི་དགའ་ལ་སོགས། །བསམ་གཏན་གཉིས་པ་ལ་ཡན་ལག་བཞི་སྟེ། ནང་རབ་ཏུ་དང་བ་དང་། དགའ་བ་དང་། བདེ་བ་དང་།

[Block 4275]
སེམས་རྩེ་གཅིག་པ་ཉིད་དོ། །
--- END BLOCKS ---
