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
[Block 4026]
དེ་ནི་འདིར་སིལ༌[^4139]བུའི་གཞུང་ལས།

[Block 4027]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། མལ་ཆ་དེ་ལས་འདི་ནི་རྒྱལ་པོ་གཟུགས་ཅན་སྙིང་པོའི་སྦྱིན་པར་བྱ་བའི་ཆོས་སོ་ཞེས་ཡི་གེར་བྲི་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4028]
གོས་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི་གནས་མལ་གྱི་ལྟུང་བྱེད་ཞུ་བ་ལས།

[Block 4029]
དགེ་འདུན་གྱི་གོས་དག་ལ་ཡང་འདི་ནི་ཆེ་གེ་མོའི་གཙུག་ལག་ཁང་མིང་འདི་ཞེས་བྱ་བའི་སྦྱིན་པར་བྱ་བའི་ཆོས་ཞེས་ཡི་གེར་བྲི་བར་བྱ་བ་ཡིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4030]
རྣམ་པ་དེ་ལྟར་གཞན་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ།

[Block 4031]
འདིར་གཞུང་ནི་སིལ༌[^4140]བུ་དག་ལས།

[Block 4032]
གནས་མལ་གྱི་རྣམ་པ་དེ་ལྟ་བུར་སྣོད་སྤྱད་དང་གཙུག་ལག་ཁང་དུ་ཞེས་བྱ་བ་ནི་གླེང་གཞི་ལས་ཏེ། གནས་མལ་གྱི་རྣམ་པ་དེ་ལྟར་སྣོད་སྤྱད་ལ་སོགས་པའི་དོན་གཞན་ལ་ཡང་བྱའོ། །

[Block 4033]
ཀློག་ཏུ་གཞུག་པའི་སྐབས་ཞར་ལ་བྱུང་བ་དང་བཅས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 4034]
ད་ནི་ཀློག་པར་བྱེད་པའི་སྐབས་བརྗོད་པར་བྱ་སྟེ། [^4141]སངས་རྒྱས་ཀྱི་བཀའ་སྡེབ་སྦྱོར་དང་ཚིག་དང་རིམ་པ་ལ་གཞོལ་བ་ཉིད་ཀྱིས་སྦྱར་ཏེ་ཀློག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། སྡེབ་སྦྱོར་ཞེས་བྱ་བ་ནི་སྡེབ་སྦྱོར་ཏེ། ཀླག༌[^4142]པའི་རྣམ་པ་དང་རིང་པོར་དྲང་བ་ལ་སོགས་པ་རྣམས་ལ་དེ་ལྟ་བུར་གྱུར་ཅིག་སྙམ་པ་ཉིད་ཀྱིས་སོ། །

[Block 4035]
དེ་ལ་གཞོལ་བ་ཉིད་ཅེས་བྱ་བ་ནི་དེ་དག་ཁོ་ན་ལྟ་བུར་བྱས་པར་གྱུར་ཅིག་སྙམ་པ་ལ་ཉེས་པ་འདི་ཡིན་ཏེ་གཞན༌[^4143]གྱི་དབང་གིས་འདི་འགྲུབ་པ༌[^4144]མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4036]
གཞན་ལ་ལེགས་པར་གོ་བར་བྱེད་ནུས་ཤིང་སངས་རྒྱས་ཀྱི་བཀའ་ལ་བརྩོན་པ་ཉིད་མི་གཏོང་ན་ཕྱི་རོལ་བའི་བསྟན་བཅོས་དག་གཟུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་ལ་གོ་བར་བྱེད་ནུས་ཤིང་སངས་རྒྱས་ཀྱི་བཀའ་ལ་བརྩོན་པ་ཉིད་མི་གཏོང༌[^4145]ན་ཚིག་དང༌[^4146]དོན་མི་གཏོང་ཞིང་བྱེ་བྲག་ཡོངས་སུ་མ་སྨོས་པས་ཤེས་པའོ། །

[Block 4037]
འདིར་གཞུང་ནི་དེའི་ཕྱིར་རྗེས་སུ་ཤེས་ཏེ། དགེ་སློང་རྣམས་ཀྱིས་འཇིག་རྟེན་རྒྱང་འཕེན་པའི༌[^4147]བསྟན་བཅོས་གཟུང་བར༌[^4148]བྱ་ཞེས་ཏེ། འདི་ནི་དཔེ་ཙམ་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ལྟར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །ཅི་ཐམས་ཅད་ཀྱི་བྱེ་བྲག་མེད་པར་རམ་ཞེ་ན། དེའི་ཕྱིར། གཞན་ལ་ལེགས་པར་གོ་བར་བྱེད་ནུས་ཤིང་ཞེས༌[^4149]སྨོས་ཏེ། གཞན་མགུ་བར་བྱེད་ནུས་པ་གང་ཡིན་པ་དེས་སོ། །

[Block 4038]
ཅི་དེ་ལ་གཞོལ་བ་ཁོ་ནས་དེ་གཟུང་བར༌[^4150]བྱའམ་ཞེ་ན། དེའི་ཕྱིར། སངས་རྒྱས་ཀྱི་བཀའ་ལ་བརྩོན་པ་ཉིད་མི་གཏོང་ན་ཞེས་བྱ་བ་སྨོས་ཏེ། རྣམ་པ་ཐམས་ཅད་དུ་སངས་རྒྱས་ཀྱི་བཀའ་ལ་བརྩོན་པ་གཏང་བར༌[^4151]མི་བྱའོ།[^4152] །དེའི་དུས་ནི༌[^4153]ཉི་མའི་སུམ་ཆ་བདེ་བ་མ་ཡིན་པའོ་ཞེས་བྱ་བ་ལ། དེའི་དུས་ཞེས་བྱ་བ་ནི་ཕྱི་རོལ་པའི་བསྟན༌[^4154]བཅོས་བཟུང༌[^4155]བདེའི་དུས་སོ། །

[Block 4039]
དེ་ཡང་བདེ་བ་མ་ཡིན་པ༌[^4156]ཞེས་བྱ་བའི༌[^4157]དུས་གང་གི་ཚེ་ལུས་དང་སེམས་ལས་སུ་རུང་བ་མ་ཡིན་པའོ། །

[Block 4040]
ལུས་ལ་གཟི་བརྗིད་དང་བཅས་པ་ཉིད་དེ་ལ་འདིར་བདེ་བར་འདོད་དེ་དེ་སངས་རྒྱས་ཀྱི་བཀའ་ལ་སྦྱར་བ་ནི་མཛེས་པ་ཞེས་བྱ་བར་བལྟ་བར་བྱའོ། །

[Block 4041]
མཚན་མོ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་། དེའི་དུས་སུམ་ཆ་བདེ་བ་མ་ཡིན་པའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4042]
གསང་སྔགས་ཕན་འདོགས་པར་བྱེད་པ་དག་གཟུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དུག་གི་གནོད་པ་ལ་སོགས་པ་སེལ་བར་བྱེད་པ་དག་གོ། །

[Block 4043]
སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གསང་སྔགས་གཟུང་བ་དག་ཐམས་ཅད་དུ་རྗེས་སུ་གནང་བའི་གསང༌[^4158]སྔགས༌[^4159]རྗེས་སུ་སྦྱར་བར་བྱའོ། །

[Block 4044]
གནོད་པ་བྱེད་པ་ནི་མི་བྱའོ་ཞེས་བྱ་བ་ནི། གསང་སྔགས་གནོད་པར་བྱེད་པ་ནི་གཟུང་བར་ཡང་མི་བྱའོ། །

[Block 4045]
སྦྱར་བར་ཡང་མི་བྱའོ། །

[Block 4046]
དེ་དག་གི་ཕྱག་གི་གནས་སུ་དཀོན་མཆོག་གསུམ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གསང་སྔགས་དེ་དག་ལ་ཕྱག་འཚལ་བ་བྱུང་བ་དེ་གང་ཡིན་པ་དེའི་གནས་སུ་དཀོན་མཆོག་གསུམ་ལ་ཕྱག་འཚལ་ལོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 4047]
ལྷ་གཞན་ལ་ཕྱག་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཁྱབ་འཇུག་ལ་སོགས་པ་ལའོ། །

[Block 4048]
འདིར་གཞུང་ནི་གསང་སྔགས་ནི༌[^4160]རྣམ་པ་གཉིས་ཏེ། ཕན་འདོགས་པ་དང་། གནོད་པ་བྱེད་པའོ། །

[Block 4049]
དེ་ལ་གནོད་པ་བྱེད་པ་གང་ཡིན་པ་དེ་དག་ནི༌[^4161]དགེ་སློང་རྣམས་ཀྱིས་བཀླག་པར་མི་བྱ་སྦྱར་བར་མི་བྱ། ཕན་འདོགས་པ་གང་ཡིན་པ་དེ་དག་ནི་དགེ་སློང་རྣམས་ཀྱིས་བཀླག་པར་བྱའོ། །

[Block 4050]
སྦྱར་བར་བྱའོ༌[^4162]ཞེས་གསུངས་པ་དང་། གསང་སྔགས་དེ་དག་ལ་ལྷ་གཞན་ལ་ཕྱག་འཚལ་བ༌[^4163]དག་སྔོན་དུ་བཏང་བ་བྱུང་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་གིས་འདི་ལ་ཕྱི་རོལ་པའི་ལྷ་ལ་ཕྱག་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4051]
མཆོད་པ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གླེང་གཞི་དག་ལས་འདི་དང་པོར་བྱ་སྟེ། རྗེས་སུ་གཟུང་བར༌[^4164]བྱ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 4052]
བཀུར་སྟི་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདི་ལས་ཕྱི་རོལ་པའི་ལྷ་ལའོ། །

[Block 4053]
གནས་སུ་ཕྱིན་ན་མངོན་སུམ་དུ་འགྲེང་སྟེ་སེ་གོལ་གྱི་སྒྲས་གོ་བར་བྱས་ནས་གཙུག་ལག་གི་ཚིགས་སུ་བཅད་པ༌[^4165]གདོན་པས༌[^4166]དེ་ལ་ཕན་གདགས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་འདི་ལས་ཕྱི་རོལ་པའི་ལྷའི་གནས་སུ་ཕྱིན་ན་དེའི་མངོན་སུམ་དུ་འགྲེང་སྟེ། སེ་གོལ་གྱི་སྒྲས་གོ་བར་བྱས་ནས་སོ། །

[Block 4054]
བཟོ་རྗེས་སུ་སྒྲུབ་པ་དང་། བསླབ་པ་དང་། དེའི་སྣོད་ཉེ་བར་གཞག་པར་མི་བྱ་སྟེ། མཚོན་གྱི་ཤུབས་དང་ཁབ་རལ་དང་རམ་ཕྱིས་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི་སྨན་གྱི་གཞི་ལས་དགེ་སློང་གིས་རང་གིས༌[^4167]བཟོ་མི་བྱ་བ་དང་གཞན་ལ་བཟོ་བསླབ་པར་མི་བྱ་བ་དང་། བཟོ་སྤྱད་ཀྱི་སྣོད་ཉེ་བར་གཞག་པར་མི་བྱའོ། །

[Block 4055]
གྲི་ཤུབས་ལ་སོགས་པ་དང་ཁབ་རལ་དང་རམ་ཕྱིས་ནི་མ་གཏོགས་སོ་ཞེས་གསུངས་པ་དང་། འདིར་གཞུང་ནི་དགེ་སློང་གིས་དེ་ལྟ་བུའི་སྣོད་ཉེ་བར་གཞག་པར་མི་བྱའོ། །

[Block 4056]
སྔོན་སྨན་པ་ཡིན་ན་མཚོན་གྱི་སྣོད་དང་སྔོན་ཡི་གེ་པ་ཡིན་ན་རམ་ཕྱིས་དང་། སྔོན་བཟོ་མཁན་ལས་རབ་ཏུ་བྱུང་བ་ཡིན་ན་ཁབ་རལ་ནི་མ་གཏོགས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4057]
མུ་གཅིག་པ་ལ་བསོད་ནམས་ཀྱི་བསམ་པས༌[^4168]དགེ་བའི་གསོ་བ་ཉེ་བར་བསྒྲུབ་པར་བྱ་སྟེ། གླ་རྔན༌[^4169]གྱིས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་མུ་གཅིག་པ་དག་ལའོ། །

[Block 4058]
བཀྲུ་སྨན་བཏང་ནས་གཞན་དུ་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྨན་གཞན་ལ་བཀྲུ་སྨན་བཏང་ནས་དེ་ཉིད་དུ་བསྡད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ནོ། །

[Block 4059]
རྐྱེན་དེ་ལྟ་བུ་དག་བྱུང་ན༌[^4170]ཧ་ཅང་འཁྲུ་བ་ལ་སོགས་པའི་གཉེན་པོའི་ཆོ་ག་བསྟན་ཏེ་འོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི་གླེང་གཞི་དག་ལས་དེ་ལྟ་བས་ན་དགེ་སློང་གིས༌[^4171]གླ་རྔན་གྱིས༌[^4172]བཀྲུ་སྨན་བཏང་བར་མི་བྱའོ། །

[Block 4060]
བཀྲུ་སྨན་བཏང་ནས་གཞན་དུ་འགྲོ་བར་མི་བྱའོ། །

[Block 4061]
རྐྱེན་དེ་ལྟ་བུ་དག་བྱུང་ན༌[^4173]བསྒོ་སྟེ་འགྲོ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4062]
ཚངས་པ་མཚུངས་པར་སྤྱོད་པ༌[^4174]ལ་དབེན་པའི་ཕྱོགས་སུ་འདྲེག་མཁན་གྱི་བྱ་བ་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གིས་དགེ་སློང་ལ་དང་། དགེ་སློང་མས་དགེ་སློང་མ་ལའོ། །

[Block 4063]
ཁྲིའུ༌[^4175]ཡན་ལག་ཆག་པ་བཅོས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་ངོ་ཞེས་བྱ་བ་ཡང་དབེན་པའི་ཕྱོགས་སུ་བྱ་བའོ། །

[Block 4064]
འདིར་ཁྲི་ཞེས་སྨོས་པ་ནི་ཁྲིའུ་ལ་སོགས་པ་གཞན་དག་གི་དཔེ་ཡིན་ཏེ། ཁྲིའུ་ལ་སོགས་པ་གཞན་རྣམས་ལ་ཡང་འདི་རིགས་པའི་ཕྱིར་རོ། །

[Block 4065]
ཕྲེང་བའི་རིམ་པ་དག་བརྒྱུ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་དབེན་པའི་ཕྱོགས་སུ་བྱ་བའོ། །
--- END BLOCKS ---
