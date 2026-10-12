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
[Block 4236]
དེའི་ཕྱིར་ན་དེ་ཡང་རྣམ་པར་དག་པར་བྱ་བར་རིགས་སོ། །

[Block 4237]
དེ་བས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་རིམ་པ་བཞིའི་འབྲས་བུ་ཟུང་དུ་འཇུག་པའི་རིམ་པའི་ཕན་ཡོན་ཙམ་བསྟན་ཏོ། །

[Block 4238]
བདེན་པ་གཉིས་ལྟ་བུར་བསྒོམ་པ་ནི་ཞེས་པ་ལ་ཀུན་རྫོབ་དང་དོན་དམ་པ་དབྱེར་མེད་པའི་ངོ་བོ་ཉིད་ཟུང་དུ་འཇུག་པའི་རིམ་པ་བསྒོམ་པའོ། །

[Block 4239]
དཀའ་བས༌[^2608]དམིགས་པ་ཡིན་པས་སོ། །ཞེས་པ་ནི་སྔོན་བསགས་པའི་དགེ་བའི་སྟོབས་དང་དགེ་བའི་བཤེས་གཉེན་དང་ཕྲད་པ་དང་རྗེས་སུ་མཐུན་པའི་གནས་སུ་སྐྱེ་བ་དང་བྱང་ཆུབ་སེམས་དཔའི་རིགས་དང་འབྲེལ་པ་དང་། སངས་རྒྱས་ཀྱིས་བྱིན་གྱིས༌[^2609]བརླབས་པས་ཐོབ་པར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4240]
དེས་ནི་ཀུན་རྫོབ་བདེན་པ་ཡང་དག་པར་རྟོགས་པའི་མཚན་ཉིད་ཅན་སྦས་པའི་དོན་བསྟན་ཏོ། །

[Block 4241]
སྦས་པ་ཞེས་པ་ལ་སེམས་རྣམ་པར་དག་པ་དང་བདག་བྱིན་གྱིས་རློབ༌[^2610]པའི་རིམ་པ་བརྗོད་པར་འདོད་པས་སོ། །

[Block 4242]
དོན་དམ་པའི་བདེན་པས༌[^2611]ཞེས་པ་ནི་ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་གྱི་རིམ་པས་ཐོབ་པར་བྱ་བ་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པས་ཐོབ་པར་བྱ་བ་ལའོ། །

[Block 4243]
སྒོམ་པ་མེད་པ་སྟེ་ཞེས་པ་ནི་སྒོམ་པའི་རིགས་པ༌[^2612]མ་ཡིན་ཏེ། གང་གི༌[^2613]ཕྱིར་སྒོམ་པ་ཞེས་བྱ་བ་ནི་སེམས་ཀྱི་རྣམ་པར་དཔྱོད་པའི་མཚན་ཉིད་ཅན་རྟོག༌[^2614]བཅས་ཀྱི་རྣམ་པར་ཤེས་པའི་ངོ་བོ་སྟེ་འདུས་བྱས་སོ། །

[Block 4244]
དོན་དམ་པའི་བདེན་པ་ནི་རྫས་སུ་མེད་པའི་ཕྱིར་འདུས་མ་བྱས་པའོ། །

[Block 4245]
འདུས་བྱས་པ་དང་འདུས༌[^2615]མ་བྱས་པའི་རྒྱུ་དང་འབྲས་བུའི༌[^2616]འབྲེལ་པ་མི་རིགས་ཏེ། བུམ་པ་དང་ནམ་མཁའ་བཞིན་ནོ། །

[Block 4246]
གང་གི༌[^2617]འདུས་བྱས་པ་ཉིད་འདུས་བྱས་པའི་རྒྱུ་འམ་འབྲས་བུར་འཐད་དེ་ནས་ཀྱི་ས་བོན་དང་ནས་ཀྱི་མྱུ་གུ་བཞིན་ནོ། །

[Block 4247]
དེ་བཞིན་དུ་ཡང་འཇིམ་པ་དང་དབྱུག་པ་དང་འཁོར་ལོ་དང་སྐུད་པ་དང་སྐྱེས་པའི་ལག་པའི་རྩོལ་བ་རྣམས་ཀྱིས་བུམ་པ་བཞིན་ནོ། །

[Block 4248]
ཆོས་ཐམས་ཅད་ཀྱི་ཆོས་ཉིད་ཀྱི་ངོ་བོ་དོན་དམ་པའི་བདེན་པ་ལ་དེ་ལྟར་བསྒོམ་པ་མི་རིགས་ཏེ། །རྟག་པ་བསྐྱེད་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4249]
མ་གྲུབ་པ་འམ་མ་དག་པ་གང་ཡིན་པ་དེ་ཐོབ་པར་བྱ་བའམ་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་བསྒོམ་པར་བྱ་བ་ཡིན་ཏེ། གང་རང་བཞིན་གྱིས་གྲུབ་པའམ་རྣམ་པར་དག་པ་ཡིན་པ་དེ་ལ་སྒོམ་པས་དགོས་པ་མེད་དོ། །

[Block 4250]
གལ་ཏེ་ཡོད་ན་དོན་དམ་པ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 4251]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། [^2618]གཟོད་མ་ནས་དག་པའི་ཕྱིར་ཞེས་ཏེ། རྟག་པ་ནི་དྲི་མ་མེད་པ་ཟག་པ་མེད་པ་ནི་ཐོག་མ་ནས་དག་པའི་ཕྱིར་རོ། །

[Block 4252]
གལ་ཏེ་དེ་ལྟ་ཡིན་ན་མངོན་པར་བྱང་ཆུབ་པ་ཐོབ་པར་བྱ་བའི་ཕྱིར་ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་གྱི་རིམ་པའི་སྒོམ་པ་ཅིའི་ཕྱིར་བྱ་ཞེ་ན། སྨྲས་པ། ཕྱག་རྒྱའི་འབྲེལ་པའམ་ཏིང་ངེ་འཛིན་མངོན་དུ་བྱ་བས་འོད་གསལ་བ་ནི་སྐྱེ་བའམ་སྦྱང་བར་བྱ་བ་མ་ཡིན་ཏེ། དེ་ཉིད་གཟོད་མ་ནས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 4253]
ཕྱག་རྒྱ་དང་ཏིང་ངེ་འཛིན་ཙམ་གྱིས༌[^2619]གློ་བུར་གྱི་དྲི་མ་བསལ་བར་བྱ་བ་ཡིན་གྱི། དེ་ཁོ་ན་ཉིད་ཐོབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 4254]
དེ་ཁོ་ན་ཉིད་ནི་རང་སྣང་བ་སྟེ། ནམ་མཁའ་བཞིན་ནོ། །

[Block 4255 [VERSE]]
ཆུ་ཁམས་གསེར་དང་ནམ་མཁའ་ཡི། །
དག་པ་བཞིན་དུ་དག་པར་འདོད། །

[Block 4256]
ཅེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 4257]
དེས་ནི་འོད་གསལ་བ་ལ་འཇུག་པའི་མཚན་ཉིད་ཅན་གྱི་རིམ་པ་བཞི་པ་སྟོན་ཏོ། །

[Block 4258]
གང་ཀུན་རྫོབ་ཀྱི་བདེན་པའི་བདག་ཉིད་ཅན་ཞེས་བྱ་བ་ལ་རིམ་པ་གསུམ་པས་ཐོབ་པར་བྱ་བའི་སྒྱུ་མ་ལྟ་བུའི༌[^2620]སྐུ་སྒོམ་པ་དེ་ཡང་བསྒོམ་པར་བྱ་བ་མ་ཡིན་ཞེས་པ་ལ་བསམ་པར་བྱ་བ་མི་རིགས་སོ། །

[Block 4259]
མི་བདེན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་རིམ་པ་བཞི་པས་རྣམ་པར་དག་པ་ལ་ལྟོས་པའི་ཕྱིར་རོ། །

[Block 4260]
རྣམ་པ༌[^2621]ཞེས་བྱ་བ་ལ་སོགས་པ་འདིས་ཟུང་དུ་འཇུག་པའི་རིམ་པའི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 4261]
བདེན་པ་གཉིས་ཀྱི་བདག་ཉིད་ཞེས་བྱ་བ་ནི། །ཀུན་རྫོབ་དང་དོན་དམ་པ་དབྱེར་མེད་པའི་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 4262]
དངོས་པོའི་བསྒོམ་པར་བྱ་བ་མི་འགྱུར་ཏེ་ཞེས་པ་ནི་དེ་ཉིད་བསམ་པར་བྱ་བ་མ་ཡིན་ནོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། བདེན་པ་གཉིས་གཉིས་སུ་མེད་པར༌[^2622]མཐོང་བ་ཙམ་གྱིས་གྲོལ་བར་འགྱུར་བའི་ཕྱིར་རོ་ཞེས་པ་ནི་བདེན་པ་གཉིས་དབྱེར་མེད་པའི་རང་བཞིན་གྱི༌[^2623]མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་མངོན་དུ་གྱུར་པ་ཙམ་གྱིས་རྣམ་པར་གྲོལ་བ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 4263]
དེ་བས་ན་ཞེས་བྱ་བ་ལ་སོགས་པས་ཟུང་དུ་འཇུག་པའི་རིམ་པ་ཉེ་བར་བསྡུས་པ་བསྟན་ཏེ། སྒོམ་པ་པོ་ཞེས་པ་ནི་རྣལ་འབྱོར་པའོ། །

[Block 4264]
སྒོམ་པ་ནི་བསྒོམ་པའི༌[^2624]ཤེས་རབ་བསྒོམ་པར་བྱ་བ་ནི་བསྒོམ་དུ་རུང་བའི་མན་ངག་གོ། །

[Block 4265]
དེ་ལྟར་མངོན་པར་ཞེན་པ་ནི་འདི་ཉིད་རྣམ་པར་རྟོག་པའོ། །

[Block 4266]
ཟུང་དུ་འཇུག་པའི་རིམ་པ་རྟོགས་པ་རྣམས་ལ་ཞེས་པ་ནི་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ཐོབ་པའོ། །

[Block 4267]
རྣལ་འབྱོར་པ་རྣམས་ལ་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ་མི་སློང་བའི་ཕྱིར་རོ། །

[Block 4268 [VERSE]]
ཟུང་འཇུག་ཏིང་འཛིན༌[^2625]ལ་གནས་པས། །
སླར་ཞིང་གང་ལ་མི་སློབ་བོ། །
འདི་ནི་རྫོགས་པའི་རྣལ་འབྱོར་ཞེས། །
དེ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ། །

[Block 4269 [VERSE]]
རྣམ་པ་ཐམས་ཅད་མཆོག་ལྡན་པའི། །
ཐམས་ཅད་མཁྱེན་པ་དེ་ནས་འགྱུར། །
འདས་པ་དང་ནི་མ་འོངས་པ། །
ད་ལྟར་བྱུང་བ་སྲིད་གསུམ་ལ། །

[Block 4270 [VERSE]]
དེ་ཡིས་སྐད་ཅིག་མ་ལུས་པར། །
འོད་གསལ་རྣམ་དག་འཛིན་པས་མཐོང་། །

[Block 4271]
ཞེས་འབྱུང་ངོ་། །རྡོ་རྗེ་འཆང་ཆེན་པོས་གསུངས་ཏེ་ཞེས་བྱ་བ་ནི་སྡུད་པ་པོའི་ཚིག་གོ། །

[Block 4272]
མཐར་ཐུག་པ་ཞེས་བྱ་བ་ནི་འོད་གསལ་བ་ལ་འཇུག་པ་དང་ཟུང་དུ་འཇུག་པ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4273]
དེ་ལྟར་ཡི་གེའི་དོན་གྱིས་བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པའི་སྟོང་པ་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་བསྟན་པ་དང་། སྤྱིའི་དོན་གྱི་རྣམ་པར་ཐར་པའི་སྒོ་གསུམ་གྱི་སྒོམ་པས་མདོ་སྡེ་པ་ལ་སོགས་པའི་འགྱོད་པ་སེལ་བའི༌[^2626]མཚན་ཉིད་ཅན་གྱི་དོན་བསྟན་ཏོ། །

[Block 4274]
སྦས་པའི་དོན་གྱིས་སེམས་རྣམ་པར་དག་པ་དང་། བདག་ལ་བྱིན་གྱིས་བརླབ༌[^2627]པའི་རིམ་པ་དག་བསྟན་ཏོ། །

[Block 4275]
མཐར་ཐུག་པས་འོད་གསལ་བ་ལ་འཇུག་པ་དང་ཟུང་དུ་འཇུག་པའི་རིམ་པ་དག་བསྟན་ཏོ་ཞེས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཚིགས་སུ་བཅད་པའི་བསྐྱེད་པའི༌[^2628]རིམ་པའི་ཕྱོགས་གཅིག་དང་རྡོ་རྗེ་བཟླས་པ་མ་གཏོགས་པའི་རྫོགས་པའི་རིམ་པ་ཡང་བསྟན་ཏོ། །
--- END BLOCKS ---
