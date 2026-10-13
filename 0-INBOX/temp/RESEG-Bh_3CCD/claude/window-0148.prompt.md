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
[Block 5181 [VERSE]]
སྟེང་དང་འོག་ཏུ་བཅས་པར་ནི། །
ཤེས་ནས་བློ་ནི་ངེས་པར་སྦྱར། །
བརྗོད་པ་ཡི་ནི་སྔགས་འདི་དག །
དངོས་མེད་ངོ་བོ་ཉིད་དུ་འབྱུང་། །

[Block 5182]
ཞེས་གསུངས་སོ། །

[Block 5183]
གཅིག་དང་དུ་མ་རྣམས༌[^3053]སྤངས་པ། །ཞེས་པ་ནི་ཡི་གེ་ཕྱི་མོ་ཐམས་ཅད་དེ་ཉིད་ཀྱི་ནང་དུ་བསྡུས་པའི་ཕྱིར་དང་། །དེ་ཉིད་ལ་ངག་གི་སྤྲོས་པ་ཐམས་ཅད་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 5184]
རྟེན་ཅིང་འབྲེལ་འབྱུང་ཆོས་སུ་གྲགས། །ཞེས་པ་ནི་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བའི་རང་བཞིན་གྱིས༌[^3054]ལས་དང་། ཉོན་མོངས་པ་དང་། སྐྱེ་བའི༌[^3055]ངོ་བོ་སྲིད་པ་གསུམ་གྱི་བདག་ཉིད་ཅན་གྱི་འཁོར་བའི་འཁོར་ལོའི་ཆོས་ཉིད་ཡིན་ཏེ། དེ་དག་སྟོང་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5185]
དེ་བཞིན་དུ། དངོས་པོ་ཀུན་གྱི་འབྱུང་གནས་གཅིག །ཅེས་པ་ནི་སེམས་ཅན་དང་སྣོད་ཀྱི་འཇིག་རྟེན་ཞེས་བྱ་བའི་འབྱུང་བའི་གནས་གཅིག་གོ། །

[Block 5186]
གང་ལས་འབྱུང་བ་ནི་འབྱུང་གནས་ཏེ་སྐྱེད་པའི༌[^3056]རྒྱུའོ། །

[Block 5187 [VERSE]]
དེ་ལ་ཁམས་གསུམ་ཐམས་ཅད་བསྐྱེད་པའོ། །
བརྗོད་པ་ཀུན་གྱི་རྒྱུ་ཡི་མཆོག །

[Block 5188]
ཅེས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 5189 [VERSE]]
སྲིད་པ་གསུམ་པོ་འདི་དག་ནི། །
མ་ལུས་མུན་པ་ལྟར་འགྱུར་ཏེ། །
གལ་ཏེ་སྒྲ་ཞེས་སྒྲོན་མ་ཡིས། །
ཐ་སྙད་འདི་དག་མི་གསལ༌[^3057]ན། །

[Block 5190]
ཞེས་འབྱུང་བས་སོ། །

[Block 5191]
བདག་ཉིད་འདི་ལྟར་བྱས་ན་ནི། །ཞེས་པ་ལ་འོད་གསལ་བ་གཅིག་པུ་ལས་འབྱུང་བའི་ཡི་གེ་ཨའི་རང་བཞིན་དུ་བྱས་ནས་སོ། །

[Block 5192]
ཆོས་ཀྱི་དཀྱིལ་འཁོར༌[^3058]བྲི་བར་བྱ། །ཞེས་པ་ནི་ཆོས་ཀྱི་དེ་བཞིན་གཤེགས་པ༌[^3059]བཞི་པོའི་དཀྱིལ་འཁོར་ནི་མེ་ལ་སོགས་པའི་དཀྱིལ་འཁོར་བཞི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5193]
དཀྱིལ་འཁོར་ཞེས་བྱ་བ་ནི་རིགས་ཀྱི་དོན་དུ་ཚིག༌[^3060]གཅིག་དང༌[^3061]སྦྱར་རོ། །

[Block 5194]
དེ་རྣམས་ཀྱི་ཁ་དོག་བཤད་པའི་ཕྱིར་དམར་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། དམར་པོ་ནི་མེའི་དཀྱིལ་འཁོར་ཏེ་ལྐོག་མར་རོ། །

[Block 5195]
ནག་པོ་ནི་རླུང༌[^3062]དཀྱིལ་འཁོར་ཏེ་ལྟེ་བར་རོ། །

[Block 5196]
སེར་པོ་ནི་སའི་དཀྱིལ་འཁོར་ཏེ་གསང་བར་རོ། །

[Block 5197]
དཀར་པོ་ནི་ཆུའི་དཀྱིལ་འཁོར་ཏེ་སྙིང་གར་རོ། །

[Block 5198]
མདོར་བསྡུས་པ་ནི་འབྱུང་བ་ཆེན་པོ་བཞིའི་ངོ་བོ་ཡིན་པས་སོ། །

[Block 5199]
བཞི་བཞི་ཡི༌[^3063]ནི་སྦྱོར་བ་ཡིས། །ཞེས་པ་ནི་དཀྱིལ་འཁོར་རེ་རེ་ལ་ཡང་ཆ་བཞིས་ཁྱབ་པའི་ཕྱིར་རོ། །

[Block 5200]
དེ་ལ་ལྐོག་མའི་དཀྱིལ་འཁོར་མེའི་ཁམས་ཀྱི་ངོ་བོ་ཡང་ས་དང་ཆུ་དང་རླུང་གི་ཁམས་ཀྱི༌[^3064]ཆས་ཁྱབ་པའོ། །

[Block 5201]
སྙིང་གའི་དཀྱིལ་འཁོར་ཆུའི་ཁམས་ཀྱི་ངོ་བོ་ཡང་ས་དང་མེ་དང་རླུང་གི་ཁམས་ཀྱི་ཆས་ཁྱབ་པའོ། །

[Block 5202]
ལྟེ་བའི་དཀྱིལ་འཁོར་རླུང་གི་རང་བཞིན་ཡང་ས་དང་མེ་དང་ཆུའི་ཁམས་ཀྱི་ཆས་ཁྱབ་པའོ། །

[Block 5203]
གསང་བའི་དཀྱིལ་འཁོར་སའི་རང་བཞིན་ཡང་ཆུ་དང་མེ་དང་རླུང་གི་ཁམས་ཀྱི༌[^3065]ཆས་ཁྱབ་པའོ། །

[Block 5204]
ས་ལ་སོགས་པ་འབྱུང་བ་ཆེན་པོ་རྣམས་ནི་ཕན་ཚུན་མེད་པར་མི་འབྱུང་བའི་འབྲེལ་པ་དང་ལྡན་པ་ཡིན་ཏེ།

[Block 5205 [VERSE]]
བྱས་པ་དང་མི་རྟག་པ་བཞིན་ནོ། །
གོས་དཀར་ལ་སོགས་ལེགས་པར་བྲི། །

[Block 5206]
[^3066]ཞེས་པ་ནི་སྣང་བ་མཐའ་ཡས་ལ་སོགས་པའི་དེ་བཞིན་གཤེགས་པ་བཞི་པོའི་བཙུན་མོ་ཁམས་བཞིར༌[^3067]བྱིན་གྱིས་བརླབ་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5207 [VERSE]]
ས་ནི་སྤྱན་མ་ཞེས་པ་སྟེ། །
ཆུ་ཡི་ཁམས་ནི་མཱ་མ་ཀཱི། །
གོས་དཀར་མ་ནི་མེར་བཤད་པ། །
རླུང་ནི་སྒྲོལ་མར༌[^3068]རབ་ཏུ་གྲགས། །

[Block 5208]
ཞེས་འབྱུང་ངོ་། །དེ་ཡི་དབུས་སུ་རང་གི་ལྷ། །ཞེས་པ་ནི་དཀྱིལ་འཁོར་བཞི་པོའི་ནང་ན་རང་གི་ལྷ་སྟེ་འོད་དཔག་ཏུ་མེད་པ་དང་མི་བསྐྱོད་པ་དང་དོན་ཡོད་གྲུབ་པ་དང་། རིན་ཆེན་འབྱུང་ལྡན་གྱི་བྱིན་གྱིས་བརླབས་པར༌[^3069]ཤེས་པར་བྱ་སྟེ། འདིར་ནི་པདྨའི་མགོན་པོ་ལྷ། །ཞེས་བྱ་བ་ལ་སོགས་པ་བཤད་པའི་ཕྱིར་རོ། །

[Block 5209]
སྦྱོར་བ་བཞི་ཡི་གོ་འཕང་མཆོག །ཅེས་པ་ནི་གྲུ་གསུམ་དང་ཟླུམ་པོ་དང་གཞུའི་དབྱིབས་དང་གྲུ་བཞི་པ་དང་ལྐོག་མ་དང་སྙིང་ག་དང་ལྟེ་བ་དང་གསང་བའི་གནས་དང་། དམར་པོ་དང་ནག་པོ་དང༌[^3070]སེར་པོ་དང་དཀར་པོའི་ཁ་དོག་ལ་སོགས་པ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 5210]
སྟེང་དང་ཟུར་དང་མཉམ་དང་འོག །ཅེས་པ་ནི་སྟེང་ནི༌[^3071]ལྐོག་མའོ། །

[Block 5211]
ཟུར་ནི་སྙིང་གའོ། །

[Block 5212]
མཉམ་པ་ནི་ལྟེ་བའོ། །

[Block 5213]
འོག་ནི་གསང་བའོ། །

[Block 5214]
ཡང་ན་སྟེང་ནི་མེའི་དཀྱིལ་འཁོར་གཡས་པའི་སྒོ་ནས་འབྱུང་བའོ། །

[Block 5215]
ཟུར་ནི་རླུང་གི་དཀྱིལ་འཁོར་གཡོན་ནས་རྒྱུ་བའོ། །

[Block 5216]
མཉམ་པ་ནི་ཆུའི་དཀྱིལ་འཁོར་གཉིས་ཀ་ལས་རྒྱུ་བའོ། །

[Block 5217]
འོག་ནི་སའི་དཀྱིལ་འཁོར་གཉིས་ཀ་ཁོ་ན་ལས་བྱུང་བ༌[^3072]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 5218]
གོས་དཀར་ལ་སོགས་ཞེས་པ་ནི་གོས་དཀར་ལ་སོགས་པའི་ལྷ་མོ་བཞིས་ཉེ་བར་མཚོན་པའི་དཀྱིལ་འཁོར་པ་བཞི་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 5219]
ཇི་བཞིན་དུ་ཞེས་པ་ནི་རིམ་པ་ཇི་ལྟ་བ་བཞིན་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5220]
མེ་དང་རླུང་དང་དབང་ཆེན་དང་ཆུ་སྟེ་ཞེས་པ་ནི་དཀྱིལ་འཁོར་རྣམས་ཀྱི་གནས་ཀྱི་རིམ་པས་ནི༌[^3073]མ་ཡིན་གྱི། འོན་ཀྱང་རླུང་རབ་ཏུ་རྒྱུ་བའི་རིམ་པས་སོ། །
--- END BLOCKS ---
