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
[Block 4096]
རྒྱུན་དུ་ཞུགས་པའི་ནི་གདུགས་གཉིས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4097]
དེའི་ཞེས་བྱ་བ་ནི་གདུགས་དེའི་འོ། །

[Block 4098]
མཆོད་རྟེན༌[^4192]ཡོངས་སུ་རྫོགས་པར་གྱུར་པའི་གདུགས་ནི་ལྷག་མ་རྣམས་ལས་བྱེ་བྲག་ཏུ་གྱུར་པ་ཉིད་དོ་ཞེས་བྱ་བའི་དགོངས་པ་ཡང༌[^4193]མཐོང་བ་ཡིན་ནོ། །

[Block 4099]
འདིར་འབྲས་བུ་རྣམས་ནི་རྒྱུན་དུ་ཞུགས་པ་ལ་སོགས་པ༌[^4194]རྣམས་སོ། །

[Block 4100]
གང་གི༌[^4195]འབྲས་བུ་རྣམས་ཇི་སྙེད་ཐོབ་པ་དེ༌[^4196]སྙེད་ལས་གདུགས་རེ་རེས་ལྷག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4101]
གལ་ཏེ་ཡང་ཕལ་ཆེར་འདོད་ཆགས་དང་བྲལ་བ་དང་འདོད་པའི་འདོད་ཆགས་དང༌[^4197]བྲལ་བ་དག་ལ་འབྲས་བུ་གཞན་གཅིག་དང་གཉིས་ཐོབ་པ་མེད་ན། དེ་ལྟར་ཡང་དེའི་འབྲས་བུ་ཐོབ་པར་བྱ་བའི༌[^4198]སྤང་བྱ་རྣམས་ལ་ཟག་པ་དང་བྲལ་བ་ཐོབ་པ་རྙེད་པས་ཐོབ་པ་ལྟར་བལྟ་བར་བྱ་བ་ཉིད་དོ། །

[Block 4102]
ཉན་ཐོས་ཀྱི༌[^4199]མཆོད་རྟེན་ཕྱོགས་གང་དུ་བྱ་ཞེ་ན། དེའི་ཕྱིར། དེ་བཞིན་གཤེགས་པའི་ཕྱོགས་ཀྱི་ཡུལ་ཉིད་དུ་གང་དུ་དེ་དག་གནས་པར་གྱུར་པའི་ཕྱོགས། དེར་དེའི་འཁོར་དུ་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་བཞིན་གཤེགས་པའི་མཆོད་རྟེན་གྱི་ཕྱོགས་བཞི་པོ་དག་གང་ཡིན་པ་དེ་དག་གི་ཡུལ་ཡིན་ན། དེར་གལ་ཏེ་འབྲས་བུ་ཐོབ་པའི་ཉན་ཐོས་དེ་རྣམས་གལ་ཏེ་འཇུག་པ་ཉིད་དེ་བཞིན་གཤེགས་པའི་ངོས་སུ་ཡུལ་ཉིད་དུ་གྱུར་ན་ཕྱོགས་དེར་མཆོད་རྟེན་བྱ་སྟེ། གང་དུ་དེ་རྣམས་ལ་འཁོར་བྱིན་པ་ལ་གནས་པར་གྱུར་པས་སོ། །

[Block 4103]
འདི་ལ་རྒན་རིམས་སུ་མི་བྱ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་གྱི་ཕྱོགས་ལའོ། །

[Block 4104]
སོ་སོའི་སྐྱེ་བོ་རྣམས་ཀྱི་ནི་བྱི་བོའོ། །

[Block 4105]
དེ་དག་ལ་ནི་དགེ་འདུན་གྱི་ཀུན་དགའ་ར་བའི་ཕྱི་རོལ་དུ་བྱའོ། །

[Block 4106]
འཕགས་པ་ལ་ནི་མཆོད་རྟེན་གྱི་དུས་སྟོན་རིགས་སོ་ཞེས་བྱ་བ་ནི་འཕགས་པའི་གང་ཟག་ལ་མཆོད་རྟེན༌[^4200]གྱི་དུས་སྟོན་རིགས་སོ། །

[Block 4107]
ཉན་ཐོས་ཀྱི་མཆོད་རྟེན་ལ་ཕུལ་བ་ནི་ཚངས་པ་མཚུངས་པར་སྤྱོད༌[^4201]པ་དབང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་ལ་རས་དང་སྣམ་བུ་དང་རྫས་གང་ཡང་རྣམ་པ་གཞན་གང་དག་ཕུལ་བ་དེ་དག་ནི་དགེ་སློང་རྣམས་ཀྱིས་བགོ་བར་བྱའོ། །

[Block 4108]
འདིར་གཞུང་ནི་ཚངས་པ་མཚུངས་པར་སྤྱོད་པའི་རྫས་ལ་ནི་དགེ་སློང་ཚངས་པ་མཚུངས་པར་སྤྱོད་པ་དག༌[^4202]དབང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4109]
མུ་ཏིག་དག་ནི་བསྟན་པ་བཞིན་བྱའོ་ཞེས་བྱ་བ་ནི་དྲི་གཙང་ཁང་གི་ཞལ་ཞལ་དུ་བྱའོ་ཞེས་བསྟན་པ་བཞིན་དུ་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4110]
བུད་དུང་དག་ནི་སངས་རྒྱས་ལ་དབུལ་ལོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་བུད་དུང་གང་དག་ཡིན་པ་དེ་དག་ནི་འཛམ་བུའི་གྲིབ་མ་ལས་བྱུང་བའི་སྐུ་གཟུགས་ལ་དབུལ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4111]
དེ་ལས་ཞིག་རལ་བྱུང་བ་བཅོས་པའི་ཕྱིར་གཞག་པར་བྱའོ་ཞེས་བྱ་བ༌[^4203]ལ། དེ་ལས་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་གང་ལ༌[^4204]ཕུལ་བའི་རྫས་དེ་ལས་སོ། །

[Block 4112]
མཆོད་པར་རུང་བ་ཉིད་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལ་གཞག་པར་བྱའོ།[^4205] །འདིར་གཞུང༌[^4206]ནི། དེ་ལ་དབྱིག༌[^4207]དང་། གསེར་གང་ཡིན་པ་དེ་དག་མཆོད་རྟེན་དེ་ཉིད་ཞིག་རལ་དུ་གྱུར་པ་བཅོས་པའི་ཕྱིར་གཞག་པར་བྱའོ། །

[Block 4113]
མཆོད་པར་རུང་བའི་རྫས་དེ་དག་ནི་དུས་སྟོན་གྱི་ཚེ་མཆོད་པར་བྱ་བའི་ཕྱིར་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4114]
སངས་རྒྱས་ལ་ལྕགས་ལས་བྱས༌[^4208]པའི་མཆོད་རྟེན་བྱ་བ་ནི་ཆོས་དང་མཐུན་པའོ་ཞེས་བྱ་བ་ནི་རུང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4115]
དབུ་སྐྲ་དང་སེན་མོའི་མཆོད་རྟེན་གསེར༌[^4209]དང་དངུལ་དང་བཻ་ཌཱུརྱ་དང་ཤེལ་ལས་བྱས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་ཆོས་དང་མཐུན་པའོ། །

[Block 4116]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པ་དང་། སིལ་བུ་དག་དང་།

[Block 4117]
གླེང་གཞི་དག་ལས།

[Block 4118]
རབ་ཏུ་བྱུང་བའི་གནས་སུ་དགྲ་བཅོམ་པ་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནས་སྐུ་གཟུགས་བགྱིད་དུ་སྩལ་ལོ་ཞེས་བྱ་བའི་བར་དང་། དེ་ལ་ཞེས་བྱ་བ་ནས་མཐུན་པའི་འཁོར་བགྱིད་དུ་སྩལ་ཏོ་ཞེས་བྱ་བའི་བར་དང་། གྲོང་ཁྱེར་དུ་ཞུགས་ཏེ་ཞེས་བྱ་བ་ནས་ཡོངས་སུ་བསྐོར་ཏེ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 4119]
རབ་ཏུ་བྱུང་བའི་གནས་སུ༌[^4210]དགྲ་བཅོམ་པ་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་འདིའི༌[^4211]ནི་སིལ་བུ་དག་ལས་སོ། །

[Block 4120]
ལྷག་མ་ནི་གླེང་གཞི་དག་ལས་སོ། །

[Block 4121]
དེ་ལ་མཐུན་པའི་འཁོར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལ༌[^4212]ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཀྱི་མཆོད་རྟེན་དེ་ལའོ། །

[Block 4122]
དགའ་ལྡན་གྱི་གནས་ན་བཞུགས༌[^4213]པ་ལ་སོགས་པ་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པའི་མཐའི་བར་གྱི་སྤྱོད་པ་ནི་དེ་ཞེས་བྱའོ་ཞེས་བྱ་བ་ནི་མཐུན་པའི་འཁོར་ཞེས་བྱའོ། །

[Block 4123]
དཀར་རྩིས༌[^4214]དཀར་པོར་བྱའོ་ཞེས་བྱ་བ་ནི་ས་དཀར་པོ༌[^4215]ལ་སོགས་པས་སོ། །

[Block 4124]
མར་མེ་འཛིན་པ་བྱའོ། །

[Block 4125]
ལན་ཀན་གྱིས་བསྐོར་རོ། །

[Block 4126]
རྟ་བབས་བསྒྲེང་བར༌[^4216]བྱའོ། །

[Block 4127]
རྒྱལ་མཚན་གཟུགས་སོ། །

[Block 4128]
དེ་ནི་རྣམ་པ་བཞིའོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་རྒྱལ་མཚན་ནོ། །

[Block 4129]
སེང་གེའི་རྒྱལ་མཚན་དང་། ཆུ་སྲིན་གྱི་རྒྱལ་མཚན་དང་། ཀླུའི་རྒྱལ་མཚན་དང་། ཁྱུ་མཆོག་གི་རྒྱལ་མཚན་ནོ། །

[Block 4130]
གཙང་ཁང་གི་མུ༌[^4217]ཁྱུད་བྱའོ། །

[Block 4131]
དེར་རྟ་བབས་བསྒྲེང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དེར་ཞེས༌[^4218]བྱ་བ་ནི་གཙང་ཁང་གི་མུ་ཁྱུད་དེར་རོ། །

[Block 4132]
སྒོ་ཡབ་བྱའོ་ཞེས་བྱ་བ་ནི་སྒོ་ཡབ་བྱ་བའོ། །

[Block 4133]
གཙང་ཁང་གི༌[^4219]མུ་ཁྱུད་དེའི་མདུན་རོལ་དུ་སྒོ་ཡབ་ཀྱི་ཁྱམས་བྱ་བ་སྟེ་སྒོའི་དྲུང་དུ་ཁང་པ་བྱའོ། །

[Block 4134]
དེ་ལ་ལན་ཀན་གྱིས་བསྐོར་རོ་ཞེས་བྱ་བ་ལ།[^4220] དེ་ལ་ཞེས་བྱ་བ༌[^4221]ནི་སྒོ་ཡབ་དེ་ལའོ། །

[Block 4135]
ཀ་བ་རྣམས་བཙག༌[^4222]གིས་བསྐུའོ། །
--- END BLOCKS ---
