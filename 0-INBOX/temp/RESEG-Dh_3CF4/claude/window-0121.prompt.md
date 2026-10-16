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
འོ་ན་རྒྱུ་དེ་གང་ཡིན་ཞེ་ན། སྨྲས་པ། ཁྱོད་ནི་ཆོས་ཀྱི་སྣོད་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཡིན་ནོ། །

[Block 4237]
དེ་ནས་རྒྱལ་པོ་དེའི་ཁྱི་གནང་ཆེན་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་ནི་མི་མ་ཡིན་པ་ཁྱི་ཡང་ཟུག༌[^2719]པའི་ཚུལ་གྱིས་རྒྱུ་ཡོད་པ་ཡིན་ཏེ། དབྱེན་གྱི་ཚུལ་ངེས་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4238]
བྲི་བར་གྱུར་པ་ནི་ཡལ་བར་བོར་བའོ། །

[Block 4239]
གསུམ་པོ་འདི་ནི་བདག་གི་འགྲོ་བའི་རྒྱུ་ཡིན་ཏེ། གནས་ལ་ལྷག་པར་ཞེན་པ་དང་། གཞན་དུ་འགྲོ་བའི་གནས་མ་མཐོང་བ་དང་། བསྙེན་བཀུར་ཆུང་བར་ཡོངས་སུ་ཤེས་པའོ། །

[Block 4240]
ཕྱིས༌[^2720]བསྐྲད་པར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་སླད་ཀྱིས་བསྐྲད་པར་འགྱུར་བ་སྟེ། རྗེས་སུ་རྒྱལ་པོས་བསྐྲད་པ་དང་། སྤྱུགས་པར་འགྱུར་ཞེས་པའོ། །

[Block 4241]
མི་དགའ་བ་ནི་བརྩེ་བ་གཅོད་པའོ། །

[Block 4242]
མི་དགའ་བས་གདུངས་པའི་སེམས་གང་ཡིན་པ་དེ༌[^2721]ནི་མི་དགའ་བ་བཞིན་དུའོ། །

[Block 4243]
ལན་ཅིག་ཙམ་ཞིག་སྨ་བབ་གྱུར་པ་ཡིས། །ཞེས་བྱ་བ་ནི་བརྙས་པར་འགྱུར་བའོ།[^2722] །སྔོན་ཆད་ཕན་བཏགས་ཞེས་བྱ་བ་ནི་ཕན་བཏགས་པ་མང་དུ་བྱས་པ་སྟེ། ག་ལ་མཉམ་ཞེས་བྱ་བ་ནི༌[^2723]མཉམ་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4244]
དེས་ནི་དེའི་ཕྱིར། མི་དགའ་བཞིན་དུ་མ་ཆིས་སུ་ག་ལ་རུང་། །ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4245]
དེ་ལྟ་བས་ན་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བའི་ཚིག་གི་སྐབས་ཤེས་པར་བྱས་ནས་དེའི་ལན་བསྟན་པའི༌[^2724]ཕྱིར། བྱམས་པའི་རླན་མེད་ཅེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། བྱམས་པའི་རླན་མེད་པ་གང་ཡིན་པ་དེ་ནི་བྱམས་པའི་རླན་མེད་པའོ། །

[Block 4246]
བསྟན་དུ་མི་རུང་བ་ནི་གནས་པར་བྱ་བ་མ་ཡིན་པའོ། །ཅིའི་ཕྱིར་ཞེ་ན། རབ་ཏུ་བསྒྲིམས་ཏེ་དེའི་དོན་བསྒྲུབས་ཀྱང་རྙོག་པ་ཅན་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 4247]
རྙོག་པ་ཅན་དུ་གྱུར་པས་ན་དོན་ཆུང་བ་ཉིད་དེ། བྱམས་པའི་རླན་མེད་པ་དེས་ནའོ། །ཇི་ལྟ་བུ་ཞེ་ན། ཁྲོན་པ་སྐམ་པོ་བཞིན་དུ་བསྟེན་པར་མི་བྱའོ། །

[Block 4248]
ཇི་ལྟར་ཁྲོན་པ་སྐམ་པོ་ལ་ནི་ཆུ་འདོད་པ་དེས་རབ་ཏུ་བསྒྲིམས་ཏེ་བསྒྲུབས་ཀྱང་ཆུང་ཞིང་རྙོག་པ་ཅན་དེ་དང་དེར་འགྱུར་རོ། །

[Block 4249]
རབ་ཏུ་དང་བ་ཉིད་ལ་བསྟེན་པའི་རིགས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དེ་ལས་ནི་དོན་གྲུབ་པ་ཉིད་དེ། འབད་པར་བསྒྲུབས༌[^2725]མི་དགོས་པ་དང་། དང་བ་ཉིད་ཡིན་ཏེ། ཇི་ལྟ་བུ་ཞེ་ན། སྟོན་ཀའི་མཚོ་ཆེན་པོའི་ཚུ་གཙང་བ་ལྟ་བུ་སྟེ། དེ་ནི་བསྟེན་པའི་རིགས་སོ། །

[Block 4250]
བདེ་བ་འདོད་ཅིང་ཉོན་མོངས་མི་འདོད་པས། །ཞེས་བྱ་བ་ནི་སེམས་ཀྱིས་སྔར་མྱོང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4251]
འདིས་ཀྱང་བློ་ཕྱིན་ཅི་ལོག་པར་བསྟན་ཏེ། གང་སྔར་བསྟན་པའི་ངན་ཅིང་བྱིས་པའི་ཆོས་ཞེས་བྱ་བའི་ཚིགས་བཅད་དེའི་གཉེན་པོ་འདིས་བསྟན་ཏོ། །

[Block 4252]
གུས་པར་བྱེད་ཀྱང་གཞན་དུ་ཕྱོགས་པ་དང་། །[^2726]ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ནི་སྔར་བསྟན་མ་ཐག་པའི་ཚིགས་བཅད་གསུམ་གྱི་གཉེན་པོ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4253]
གུས་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་གུས་པར་བྱེད་པའོ། །

[Block 4254]
དེ་བས་ན་གཞན་དུ་ཕྱོགས་པ་ནི་རྒྱབ་ཀྱིས་བལྟས་པའོ། །

[Block 4255]
འདི་ནི་རབ་ཏུ་བདེ་བ་འདོད་ཅིང་ཉོན་མོངས་མི་འདོད་པས་ཞེས་བྱ་བའི་ཚིགས་བཅད་དེའི་གཉེན་པོ༌[^2727]བསྟན་ཏོ། །

[Block 4256]
གཞན་དུ་ཕྱོགས་ཀྱང་ཞུམ་པས་དེ་ལ༌[^2728]ལྟ། །ཞེས་བྱ་བ་འདིས་ནི། བྱམས་པའི་རླན་མེད་ཅེས་བྱ་བའི་ཚིགས་བཅད་དེའི་གཉེན་པོ་བསྟན་ཏོ། །

[Block 4257]
སྔོན་ཆད་ཕན་བཏགས་དྲིན་དུ་མི་གཟོ༌[^2729]བ། །ཞེས་བྱ་བ་འདིས་ནི། ལན་ཅིག་ཙམ་ཞིག་སྨ༌[^2730]བབ་གྱུར་པ་ཡིས། །[^2731]ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་ཀྱི་གཉེན་པོ༌[^2732]བསྟན་ཏོ། བསླང་བ༌[^2733]དྲེགས་ན་ཞེས་བྱ་བ་ནི་བསླང་བ༌[^2734]ཉིད་དྲེགས་པ་ནི་བསླང་དྲེགས་པ་སྟེ། དེས་ནི་བྱམས་པ་མེད་པར་བྱེད་དོ་ཞེས་གཟུང་བར་བྱའོ། །

[Block 4258]
གནས་པའི་སྐྱོན་ཞེས་བྱ་བ་ནི་ལྷན་ཅིག་ཏུ་འདུག་པ་ལ་སོགས་པའི་སྐྱོན་ཡིན་ཏེ། དེས་ན་དེའི༌[^2735]ཉེས་པ་ཡིན་པའི་ཕྱིར་ད་ནི་རེ་ཞིག་འགྲོའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4259]
བར་ཆད་མང་ལ་གནོད་པ་དང་དགྲ་མང་བས་ཞེས༌[^2736]བྱ་བ་ནི་སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པའི་བར་ཆད་གང་ཡིན་པའི་རྒྱུ་བསྟན་ཏོ། །

[Block 4260]
མཆི་བའི་སྐབས་དང་ལྡན་ན་ཞེས་བྱ་བ་ནི་རྐྱེན་ཚོགས་ནའོ། །

[Block 4261]
གལ་ཏེ་ཞེས་བྱ་བ་ནི་དགེ་ཤིས་པའོ།[^2737] །མངོན་པར་ཤེས་པ་ལྔ་ནི་མངོན་པར་ཤེས་པ་དྲུག་ལས་ཟག་པ་ཟད་པའི་མངོན་པར་ཤེས་པ་མ་གཏོགས༌[^2738]པའོ། །

[Block 4262]
སྙིང་བརྩེ་བས་རྗེས་སུ་འབྲང་བའི་ཚུལ་གང་ལ་ཡོད་པ་དེ་ནི་སྙིང་བརྩེ་བའི་དྲན་པ་བྱུང་བར་གྱུར་པ་སྟེ། སྙིང་བརྩེ་བ་ནི་སྙིང་རྗེ་སྟེ། མི་དགེ་བའི་རྒྱུ་ལས་བཟློག་པར་འདོད་པ་ཉིད་ནི་སྙིང་རྗེའོ། །

[Block 4263]
རྒྱུ་བརྟག་མི་བཟོད་པ་ཞེས་བྱ་བ་ལས་རྒྱུ་བསྟན་པར་མི་ནུས་པའི་ལྟ་བ་གང་ཡིན་པ་དེ་ནི་རྒྱུ་བརྟག་པ་མི་བཟོད་པའི་ལྟ་བའོ། །

[Block 4264]
འདིར་རྒྱུ་ནི་གང་ཡང་མེད་པར་འདོད་པ་སྟེ། མེད་པར་འདོད་པ༌[^2739]ཉི་ཚེ་ཙམ་དུ་ཟད་པར་ལྟ་བའོ། །

[Block 4265]
པདྨའི་སྡོང་བུ་ནི་འཇམ་པའོ། །

[Block 4266]
ལོ་མ་ནི་འཇམ་པའོ། །

[Block 4267]
ཁ་དོག་ནི་སྔོན་པོ་ལ་སོགས་པའོ། །

[Block 4268]
ཟེ་བ་ནི་འཇམ་པའོ། །

[Block 4269]
སྙིང་པོ་ནི་དབྱིབས་སོ། །

[Block 4270]
དེ་བཞིན་དུ་སེམས་ཅན་ལ་རྒྱུ་མེད་པར་ལྟ་བ་ནི་བྱའི་འདབ་མ་ཞེས་བྱ་བས་བསྟན་པ་ཡིན་ནོ། །

[Block 4271]
འགྲོ་བ་འདི་དག༌[^2740]ངོ་བོ་ཉིད་ཀྱིས་ངེས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ཕྱི་དང་ནང་གི་དངོས་པོ་རྣམས་ལ་བྱེད་པ་པོ་མེད་པར་ཡང་སྣ་ཚོགས་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 4272]
རྒྱུ་མེད་པར་འབྱུང་བར༌[^2741]མི་རིགས་ཞེས་བྱ་བ་ནི་ངོ་བོ་ཉིད་ཀྱིས་མེད་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4273]
གཅིག་གཅིག༌[^2742]ཡོད་ཅེས་བྱ་བ་ནི་རང་དགས་སྤྲུལ་པར༌[^2743]བྱེད་པ་སྟེ། འཇིག་རྟེན་སྣ་ཚོགས་སོ། །

[Block 4274]
ཕྱིས་ཀྱང་མཉམ་དུ་མེད་པར་བྱེད། །ཅེས་བྱ་བ་ནི། ཅིའི་ཕྱིར་ཞེ་ན། བྱེད་པ་པོ་རང་དགའི་ཁྱད་པར་གྱིས་ཤིང་རྟ་ལ་སོགས་པ་རྣམ་པ་སྣ་ཚོགས་པའི་དངོས་པོ་འབྱིན་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 4275]
[^2744]དེའི་ཡང་རང་དགའི་དབང་གིས་མི་སྣང་བར་བྱེད་པ་ལྟ་བུའོ། །
--- END BLOCKS ---
