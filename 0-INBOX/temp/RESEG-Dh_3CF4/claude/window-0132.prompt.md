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
[Block 4621]
གཉིད་སངས་པར་བྱ་བ་ནི། སད་པར་གྱུར་པའོ། །

[Block 4622]
མགོ་ལ་རིལ་གྱིས་ཕོག༌[^2992]པར་མ་གྱུར་ཏེ། །ཞེས་བྱ་བ་ནི། དེ་བས་ན་མགོ་བོ་ཕྱེ་མར་མ་གྱུར་ཏོ། །

[Block 4623]
གཞན་དུ་བརྗོད་པ་ནི་མགོ་དེ༌[^2993]ལ་ཕོག་པ༌[^2994]སྟེ། དེ་བས་ན་ཕྱེ་མར་ནི་མ་གྱུར་ཏེ་རྨ་ཕྱུང༌[^2995]བའོ། །

[Block 4624]
མགོ་བོ་མ་ཞོམ་སྟེ་ཞེས་བྱ་བ་ནི། མགོ་ཅུང་ཟད་ཞོམ་པའོ། །

[Block 4625]
སྐྱེངས་བཞིན་ཅན་དུ་ཞེས་བྱ་བ་ནི་བྱ་བ༌[^2996]མ་ཡིན་པ་བྱས་པས་སོ། །

[Block 4626]
སྐྱེངས་པར་གྱུར་པ་ནི་སྐྱེངས་པ་སྟེ། བརྩམས་པའི་ཁ་ན་མ་ཐོ་བའི་བྱ་བ་མ་ཡིན་པ་མ་གྲུབ་པས་སོ། །

[Block 4627]
དེས་གཟི་ཉམས་པ་གང་ཡིན་པ་དེ་ནི་སྐྱེངས་པས་གཟི་ཉམས་སོ། །

[Block 4628]
སྤོབས་པ་མེད་པ་ཞེས་བྱ་བ་ནི། འཇིགས་པ་མེད་པ་མ་ཡིན་པའོ། །

[Block 4629]
དེ་བས་ན་མི་དགའ་བས་ཞུམ་པར་གྱུར་པ་ནི་མི་དགའ་སྤ་གོང་ངོ་། །མི་དགའ་བ་ནི་གཞན་སྐྱོབ་པ༌[^2997]མེད་པའི་ཕྱིར་ཏེ། དེས༌[^2998]སྤ་གོང་བའོ། །

[Block 4630]
སྐྲག་པ་ནི་བྱང་ཆུབ་སེམས་དཔས་སྐད་ཆེར་ཕྱུང་ཞིང་མཆོངས་པས་སོ།[^2999] །རྒྱུ་དེས་འཇིགས་པ་དང་། སྐྲག་པ་སྐྱེས་པ་སྟེ། དེ་བས་ན་སྐྲག་པའོ། །

[Block 4631]
དུག་འབྱིན་པའི་མཚན་མ་གང་ཡིན་པ་ལུགས་ཀྱི་བསྟན་བཅོས་ལས་བརྗོད་པ་འདིར་ཡང་ངེས་པར་འབྱུང་བར་བཤད་དེ། དུག་འབྱིན་པས་ཁ་སྐམ་པ་དང་། སྐད་འགགས་པ་དང་། རྔུལ་འབྱུང་བ་སྟེ།

[Block 4632 [VERSE]]
མཚན་མ་འདི་དག་གཟུང་བ་ཡིན་ནོ། །
སྐྱེངས་པས་གཟི་ཉམས་སྤོབས་པ་མེད་པར་གྱུར། །

[Block 4633]
ཅེས་བྱ་བ་འདིས་ནི། ཁ་སྐམ་པ་བསྟན་ཏོ། །

[Block 4634]
མདོག་ཀྱང་ཉམས་ཞེས་བྱ་བ་འདིས་ནི། བཞིན་མདོག་སྔོ་བར་བསྟན་ཏོ། །

[Block 4635]
སྐད་འགགས་པ་ཞེས་བྱ་བ་འདིས་ནི་སྐད་འགགས་པ་ཉིད་བསྟན་ཏེ། གང་གི་ཕྱིར་གྲེ་བ་འགགས་ན་ནི་སྐད་འགགས་པར་འགྱུར་རོ། །

[Block 4636]
རྔུལ་གྱིས་གཤེར་ཞིང་ཞེས་བྱ་བ་འདིས་ནི། རྔུལ་ཉིད་བསྟན་ཏོ། །

[Block 4637]
དེ་གང་གིས༌[^3000]ལྟ་ཡང་ཡོང་མ་ནུས། །ཞེས་བྱ་བ་འདིས་ནི་རང་གི་ལས་ཐལ་བར་བསྟན་ཏེ། གང་གི་ཕྱིར་དེའི་ཚེ་ནི་ལྟ་བ་ལ་གནས་པར་ཡང་མི་ནུས་པ་སྟེ། འདིར་ནི་འདིའི་ཁྱད་པར་རོ། །

[Block 4638]
དེ་དག་གི༌[^3001]ནི་ལུགས་ཀྱི་བསྟན་བཅོས་ལས་བཤད་པའི་རྟགས་དག་གི་མཚན་མ་དང་བཅས་པ་ཡིན་ཏེ། འདི་དག་དང༌[^3002]མཚན་མ་དང་བཅས་པ་ནི་སྔར་བསྟན་པའི་རྒྱུ་དག་གོ། །

[Block 4639]
བློ་ལ་ངེས་པར་བྱས་ནས༌[^3003]ནི་འཁྲུལ་པ་མེད་པའི་རྟགས་མཐོང་བས་སོ། །

[Block 4640]
བདག་ལ་ཕན་པ་ལ་ཡང་མི་ལྟ་བ་ནི། ངན་པ་དེ་ཡིན་པས་ན། བདག་ལ་ཕན་པ་ལ་མི་ལྟ་བ་ངན་པའོ། །

[Block 4641]
དེ་བས་ན་བདག་ལ་ཕན་པ་ལ་མི་ལྟ་བ་དེས། ཡིད༌[^3004]ཆད་པ་ནི་ངན་པ་ཡིན་པའི་ཕྱིར་དང་། ངན་འགྲོར༌[^3005]འགྲོ་བའི་ཕྱིར་སྙིང་རྗེ་སྐྱེས་པའོ། །

[Block 4642]
འཁྲུག་པ་ནི་སེམས་ཀྱི་རྣམ་པར་འཁྲུག་པའོ། །

[Block 4643]
ཁྲོ་བ་ནི་ལུས་དང་། ངག་གི་འགྱུར་བའོ། །

[Block 4644]
ཁྲོ་བ་དང་།

[Block 4645 [VERSE]]
འཁྲུག་པ་ལས་བྱུང་བའི་སྐྱོན་ནི། །
ཁྲོ་བ་འཁྲུག་པའི་སྐྱོན་ནོ། །

[Block 4646]
མེད་པ་ནི་ཁྲོ་བ་དང་། འཁྲུག་པའི་སྐྱོན་གང་གིས་མེད་པ་དེ་ནི་ཁྲོ་བ་དང་། འཁྲུག་པའི་སྐྱོན་མེད་པ་སྟེ། ཡིད༌[^3006]ཆད་པའི་ཕྱིར་ཁྲོ་བ་དང་། འཁྲུག་པའི་སྐྱོན་ཡོངས་སུ་སྤངས་པའོ། །

[Block 4647]
སྙིང་རྗེ་སྐྱེས་པའི་ཕྱིར་མིག་མཆི་མས་གང་བའོ། །

[Block 4648]
འདི་འདྲ་བ་དག་ཅེས་བྱ་བ་ནི་ལས་འདི་འདྲ་བར་བྱས་པའོ། །

[Block 4649]
ཇི་ལྟར་ཞེས་བྱ་བ་ནི་སེམས་ཀྱིས༌[^3007]བསྐུལ་བར་སྟོན་པ་ཡིན་ནོ། །

[Block 4650]
བྱ་བ་ཇི་ལྟར་ཞེས་བྱ་བ་འདིས་ནི་སེམས་ཀྱིས༌[^3008]ངེས་པར་བྱས་པའོ། །

[Block 4651]
ཇི་ལྟ་བུར་ཡང་བརྩམས་པར་གྱུར། །ཅེས་བྱ་བ་ནི་ཡང་དག་པར་དཔྱད༌[^3009]པའོ། །

[Block 4652]
དེ་ལ་རེ་ཞིག་དང་པོ་ནི་སེམས་སྤྱོད་པ་ལ་འཇུག་པར་བྱ་བ་ཡིན་ཏེ། བྱའམ་མི་བྱ་ཞེས་བྱ་བ་དང་། འདི་ནི་དེ་བཞིན་དུ་བྱའོ་ཞེས་པ་དང་། དེའི་འོག་ཏུ་འདི་ནི་ངེས་པར༌[^3010]འདི་ལྟར་བྱའོ་ཞེས་སེམས་པ་ལ་འཇུག་པ་ཡིན་ནོ། །

[Block 4653]
དེའི་འོག་ཏུ་སེམས་པས་ལུས་དང་། ངག་གི་ལས་ལ་འཇུག་པར་བྱེད་དོ། །

[Block 4654]
འདི་ནི་རིམ་པ་མ༌[^3011]ཡིན་པའི་ཚུལ་དུ་བསྟན་ཏེ། །ཇི་ལྟར་ཞེ་ན། འདི་འདྲ་བདག་ལ་ཁྱོད་ཀྱིས་བྱས། །ཞེས་བྱ་བ་དེའི་ལས་མཐོང་བས་ངོ་མཚར་རྟོགས་ནས་དྲིས་པ་ཡིན་ཏེ། རྒྱུ་ནི་རེ་ཞིག་གཞག་གི་བསམ་པ་ཉིད་ཀྱང་དཀའ༌[^3012]ན་དེ་བྱེད་པ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། བསམ་པ་ལྟར༌[^3013]རེ་ཞིག་བཞག་ན་དཔྱད་ཅིང་བྱའོ་ཞེས་བྱ་བ་དེ་ཉིད་ཀྱང་ཤིན་ཏུ་དཀའ་བ་ཡིན་པས་ངོ་མཚར་དུ་རྟོགས་ནས་དྲིས་པ་ཡིན་ཏེ། དེ་བས་ན་འདི་དག་གི་རིམ་པ་ནི་གོ་རིམས་བཞིན་དུ་བསྟན་པའོ། །

[Block 4655]
ཇི་ལྟ་བུར་ཡང་བརྩམས་པར་གྱུར། །ཅེས་བྱ་བ་དེའི་དཀའ་བའི་རྒྱུ་བསྟན་པའི་ཕྱིར། ང་ལ་གནོད་པ༌[^3014]བྱེད་པ་ནི། །ཞེས་བྱ་བ་སྨོས་ཏེ། ང་ལ་གནོད་པ་བྱེད་པ་དེ་དང་འབྲེལ་པ༌[^3015]གཞན་དག་གོ། །

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
--- END BLOCKS ---
