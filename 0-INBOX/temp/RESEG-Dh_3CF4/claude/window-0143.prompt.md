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
[Block 5006]
དམ་པའི་ཚུལ་ཞེས་བྱ་བ་འཇུག་པ་དང་། ལྡོག་པའི་ཚུལ་གྱིས་སོ། །

[Block 5007]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་རི་དགས་རུ༌[^3229]རུའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 5008 [HEADING]]
## སྤྲེའུའི་རྒྱལ་པོའི་སྐྱེས་པའི་རབས། ^29-0

[Block 5009]
དམ་པ་རྣམས་ཀྱི་ཚུལ་ནི་དམ་པའི་ཚུལ་ལོ། །

[Block 5010]
ཡང་ན་དམ་པ་ཉིད་ཚུལ་ཡིན་པས་དམ་པའི་ཚུལ་ལོ། །

[Block 5011]
དམ་པའི་རྗེས་སུ་འབྲང་བའི་ཚུལ༌[^3230]གང་ལ་ཡོད་པ་དེ་དག་ནི་དམ་པའི་ཚུལ་གྱི༌[^3231]རྗེས་སུ་འབྲང་པ་རྣམས་སོ། །

[Block 5012]
རོ་དང་། མཐུ་དང་། རྣམ་པར་སྨིན་པའི་ཡོན་ཏན་ནི་རོ་དང་། མཐུ་དང་། རྣམ་པར་སྨིན་པའི་ཡོན་ཏན་རྣམས་ཏེ། ཡོན་ཏན་རྣམ་པ་མང་པོ་གང་ཡིན་པ་དེ་དག་གི༌[^3232]ནི། རོ་དང་། མཐུ་དང་། རྣམ་པར་སྨིན་པའི་ཡོན་ཏན་རྣམ་པ་མང་པོ་དང་ལྡན་པའོ། །

[Block 5013]
རོ་ནི་མངར་བ་ལ་སོགས་པ་དྲུག་གོ། །

[Block 5014]
མཐུ་ནི་རྣམ་པ་གཉིས་ཏེ། དྲོ་བའི་ནུས་པ་དང་། བསིལ་བའི་ནུས་པའོ། །

[Block 5015]
རྣམ་པར་སྨིན་པ་ཡང་རྣམ་པ་གཉིས་སོ། །

[Block 5016]
གཞན་ཡང་རྣམ་པ་སྣ་ཚོགས་པའི་མེ་ཏོག་དང་། འབྲས་བུ་དང་། ལོ་མ་དང་། འདབ་མ་དང་། ལྡུམ་བུ་དེ་དག་གིས་བརྒྱན་པའོ། །

[Block 5017]
གཞན་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 5018]
གང་དུ་འབབ་ཆུ་ཤེལ་སྒོང༌[^3233]ལྟར་དང་ཞིང་གསལ་བ་འབབ་པ་གང་ཡིན་པ་དེ་ནི་འབབ་ཆུ་ཤེལ་སྒོང༌[^3234]ལྟར་དང་ཞིང་གསལ་བ་འབབ་པའོ། །

[Block 5019]
གཏོང་བ་དང་། སྙིང་རྗེ་ནི། གཏོང་བ་དང་། སྙིང་རྗེའོ། །

[Block 5020]
དེ་གཉིས་ལ་གོམས་པ༌[^3235]སྟེ་དེ་བས་ནའོ། །

[Block 5021]
གཏོང་བས་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཟུང་ངོ་། །སྙིང་རྗེས་ནི་ཚུལ་ཁྲིམས་དང་། བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཉིས་གཟུང་ངོ་། །གཏོང་བ་ལ་གོམས་པ་ནི། ཕྲག་དོག་དང་། འཇུངས་པ་ཉེ་བར་འོང་བར་མ་གྱུར་ཏེ། གཞན་གྱི་ཕུན་སུམ་ཚོགས་པ་ལ་སེམས་འཁྲུག་པའི་མཚན་ཉིད་ནི་ཕྲག་དོག་གོ། །

[Block 5022]
སེར་སྣ་ནི་སྦྱིན་པ་དང་མི་མཐུན་པའི་ཡིད་ཀྱིས་ཀུན་དུ་འཛིན་པ་སྟེ། དེ་གཉི་གའི་མི་མཐུན་པའི་ཕྱོགས་ནི་གཏོང་བ་ལ་གོམས་པའོ། །

[Block 5023]
གང་གི་ཕྱིར་སྙིང་རྗེ་བསྒོམས་པས་ནི། ཁྲོ་བ་ཉེ་བར་མ་གྱུར་ཏེ། ཁྲོ་བ་བཟློག་པས་ནི་ཚུལ་ཁྲིམས་དང་། བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྐྱེ་བར་འགྱུར་བའི་ཕྱིར་དེ་ལྟར་བསོད་ནམས་ཀྱི་ཚོགས་རྣམ་པ་གསུམ་བསྟན་ཏོ། །

[Block 5024]
དུད་འགྲོར་སྐྱེས་གྱུར་ཀྱང་ཞེས་བྱ་བ་ནི་བསམས་བཞིན་དུ་དུད་འགྲོའི་སྐྱེ་གནས་ཡོངས་སུ་བཟུང་བ་ཡིན་ནོ། །

[Block 5025]
དབང་ཐང་ལྷག་མས་ཞེས་བྱ་བ་ནི་གང་བདེ་འགྲོ་དག་ཏུ་སྤྱོད་པའི་ལྷག་མ་སྟེ། ལས་ལ་དབང་བ་དེས་དྲངས་པའོ། །

[Block 5026]
དམ་པ་རྣམས་ཞེས་བྱ་བ་ནི་དབང་ཐོབ་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སོ། །

[Block 5027]
ཕན་གདགས་འབྲེལ་པའི་མཛའ་བཤེས་ཀྱི་སྐྱེ་བོ་གང་ཡིན་པ་དེ་དག་ནི་ཕན་གདགས་འབྲེལ་པའི་མཛའ་བཤེས་ཀྱི་སྐྱེ་བོ་རྣམས་སོ། །

[Block 5028]
འདིས་ནི་འདི་སྐད་སྟོན་པ་ཡིན་ཏེ། འབྲེལ་པའི་མཛའ་བཤེས་སྐྱེ་བོ་དེ་དང་བྲལ་བ་རྣམས། །ཞེས་སྦྱར་རོ། །

[Block 5029]
བྱེས་ཡུལ་དུ་དོང་བ་ལྟ་བུ་ནི་དུད་འགྲོའི་སྐྱེ༌[^3236]གནས་སུ་བྱང་ཆུབ་སེམས་དཔའ་སྐྱེས་པའོ། །

[Block 5030]
ཕན་གདགས་འབྲེལ་བའི་མཛའ་བཤེས་ཀྱི་སྐྱེ་བོ་དང་བྲལ་བ་ལྟ་བུ་ནི་བདེ་འགྲོ་ལས་ཉམས་ཏེ། དུད་འགྲོའི་སྐྱེ་གནས་སུ་སྐྱེས་པའོ། །

[Block 5031]
ནོར་གྱི་ལྷག་མ་ལྟ་བུ་ནི་དབང་ཐོང་གི་ལྷག་མའོ། །

[Block 5032]
དེའི་དྲུང་ནས་ཞེས་བྱ་བ་ནི་ནགས་ཚལ་གྱི་བདག་པོ་དེའི་དྲུང་ནས་སོ། །

[Block 5033]
ཆུའི་ནང་ན་རྩེ་བའི་མཐའ་རྒྱ་མོས་བསྐོར་བའི་ངོས་ཤིག་ལ་ཆགས་སོ་ཞེས་བྱ་བའི་ཚིག་གིས་ནི་ཆུ་བོ་རྒལ་བ༌[^3237]ཉིད་དེ། ལུགས་ཀྱི་བསྟན་བཅོས་ལས་འབྱུང་བའི་ཚུལ་དུ་བདག་ཉིད་བསྲུང་བ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 5034]
ཁྲུས་རྩིས་བསྒོས་པ་ཡིན་ཏེ། དེ་གང་ཡིན་ཞེ་ན། ན་ཆུང་ངོ་། །རྨད་དུ་བྱུང་བ་ཞེས་བྱ་བ་ནི་འབྲས་བུ་དེ་སྔར་མ་སྤྱད་པའི་ཕྱིར་རོ། །

[Block 5035]
དེ་ག་ལས་བྱུང་བ་ནི་དེ་ག་ལས༌[^3238]བྱུང་བ་སྟེ། གང་ལས་བྱུང་བའོ། །

[Block 5036]
དེ་བཙལ་བར་བསམས་པ་གང་ཡིན་པ་དེ་ནི། དེ་གང་ལས་བྱུང་བ་བསམས༌[^3239]པའོ། །

[Block 5037]
རང་གི་བློས་བརྟགས་ཏེ་ཞེས་བྱ་བ་ནི། བཀའ་ལ༌[^3240]གཏོགས་པ་དང་བཅས་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅིའི་ཕྱིར་ཞེ་ན། གལ་ཏེ་དེ་ལ་གནོད་པ་མཐོང་བར་གྱུར་ན་ནི། རོ་ལ་སྲེད་པ་དང་། སྟོབས་དང་ལྡན་པ་ཉིད་དུ་གྱུར་ཀྱང་ངོ་། །མི་རིང་བ་ནི་ཉེ་བའོ། །ཅིའི་ཕྱིར་ཞེ་ན། ཁ་དོག་དང་། དྲི་མ་ཉམས་པའི་ཕྱིར་ཏེ། དེ་ཡང་འབབ་ཆུའི་འགྲམ་མི་རིང་བ་ཞིག་ན་ཡོད་པ་ཉིད་དུ་ངེས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། རྨ་མེད་ཅིང་མ་སྣད་པའི་ཕྱིར་རོ། །

[Block 5038]
གལ་ཏེ་ཡུན་རིང་པོར་ཆུའི་ནང་དུ་ལྷུང་ན་ནི། འདི་ག་ལས་འབྱུང་བའི༌[^3241]གནས་ཤེས་པར་མི་ནུས་པ་སྟེ། འདི་ལྟར་འབབ་ཆུའི་འགྲམ་མི་རིང་བ་ཞིག་ན་ཞེས་སྨོས་པས་ཉེ་བར་གྱུར་པའི་ཕྱིར་དང་མི་རིང་བའི་ཕྱིར་ཤེས་པར་ནུས་ཏེ། འབབ་ཆུའི་འགྲམ་ན་འདུག་པར་ངེས་པའི་ཕྱིར། འབབ་ཆུ་དེའི༌[^3242]འགྲམ་ཐོག་ཐག་ཏུ་སོང་ན་དེ་ག་ལས་བྱུང་བ་ཤེས་པར་ནུས་པ་ཉིད་དོ། །

[Block 5039]
རིང་ནས་མཐོང་བ་ཡིན་ཏེ། ཇི་ལྟར་མཐོང་བ་ཡིན་ཞེ་ན། ཆུའི་ལྗིད་ཀྱིས་ནོན་པ་འདྲ་བ༌[^3243]ཞེས་བྱ་བ་དང་། རི་དང་ཉེ་ཡང་ཞེས་བྱ་བ་སྟེ། སྤྲིན་གྱི་མདོག་འདྲ་བའི་ཕྱིར་དང་། རི་ལྟར་མཐོ་བའི༌[^3244]ཕྱིར་རོ། །

[Block 5040]
ཤིང་ཨམྲའི་འབྲས་བུ་ས་ཧ་ཀ་ར་སྨིན་པའི་དེ་བས༌[^3245]ཀྱང་ལྷག་པ་དེ་ནི་ཨ་མྲའི་འབྲས་བུ་ས་ཧ་ཀ་ར་སྨིན་པའི་དྲི་བས་ཀྱང་ལྷག་པའོ། །

[Block 5041]
གང་གིས༌[^3246]འཇིགས་ཤིང་སྐྲག་པ་དང་། མྱ་ངན་ཡོངས་སུ་སྤངས་པ་དེ་ནི་འཇིགས་ཤིང་སྐྲག་པ་དང་། །མྱ་ངན་ཡོངས་སུ་བཏང་བའོ། །

[Block 5042]
འཇིགས་པ་སྤངས་པ་ནི་བཟློག་པའི་ཐབས་སྒྲུབ་པས་སོ། །

[Block 5043]
མྱ་ངན་སྤངས་པ་དེ་ནི། དེའི་སྐྱབས༌[^3247]སུ་འགྲོ་བར་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 5044]
སྐྲག་པ་སྤངས་པ༌[^3248]ནི་མི་འབྲོས་པའམ། མི་བྱེད་པས་སོ། །

[Block 5045]
ཡང་ན་སྤྲེའུ་འཁོར་དེ་དག་དབུགས་དབྱུང་བའི་ཕྱིར་འཇིགས་པ་མེད་པའོ། །
--- END BLOCKS ---
