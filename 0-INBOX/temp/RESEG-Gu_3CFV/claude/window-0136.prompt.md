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
[Block 4761]
དེ་བྱ་བ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབ་པ་དེ་བྱ་བ་ལའོ། །

[Block 4762]
གནས་པར་ཁས་བླང་བ་ཉིད་ལ་གནས་པ་སྤང་བར་མི་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཁས་བླངས་པ་ཉིད་ལ་གནས་པའི་དགེ་སློང་སྤང༌[^3352]བར་མི་བྱ་བ་ཉིད་དོ། །

[Block 4763]
རྣམ་པར་གཞག་པ་འདི་སོ་སོར་བརྟེན་པར་གྱུར་པས་ན་དེ་ཤེས་པའོ། །

[Block 4764]
འདིར་གཞུང་ནི་དགེ་སློང་གནས་པར་ཁས་བླངས་པ༌[^3353]སྤང་བར་བགྱི་བ་དེ་དང་ལྷན་ཅིག་གནས་པར་བགྱིའམ། བཀའ་སྩལ་པ། དེ་དང་ལྷན་ཅིག་གནས་པར་བྱའོ། །

[Block 4765]
དགག་དབྱེ་བྱས་ནས་ནི་གནས་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4766]
གནས་པ་དེ༌[^3354]ནི་དཔེ་ཡིན་ནོ་ཞེས་བྱ་བ་སྔར་མདོ་ལས།

[Block 4767]
དམ་བཅས་ན་དབྱར་གནས་པ་དང་གནས་སུ་མི་འབྲེལ་བར་མི་བྱའོ་ཞེས་སྨོས་པ་དེ་ནི་དཔེ་ཙམ་དུ་ཟད་དེ། ཆོས་ལས་མི་འདའ་བའི་དོན་ལ་གནས་པའོ། །

[Block 4768]
གཞན་དག་ལ་ཡང་དམ་བཅས་པ་སྒྲུབ་པར༌[^3355]མི་བྱེད་ན་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4769]
འདི་སྐད་བསྟན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་དམ་བཅས་པ་སྒྲུབ་པར༌[^3356]མི་བགྱིད་པ་ལས་ཉེས་བྱས་སུ་གསུངས་ན། བཙུན་པ་དམ་བཅའ་བ་དུ་མཆིས། ཉེ་བ་འཁོར་ལྔ་སྟེ། ལྔ་གང་ཞེ་ན། དབྱར་དམ་བཅའ་བ་དང་། ལྷུང་བཟེད་དམ་བཅའ་བ་དང་། ཆོས་གོས་དམ་བཅའ་བ་དང་། བསོད་སྙོམས་དམ་བཅའ་བ་དང་། ནད་པའི་སྨན་དམ་བཅའ་བ་སྟེ། དེ་ལྟར་འདི་བསྡུ་བར་བྱས་པ་ཡིན་ནོ། །

[Block 4770]
འདིར་དབྱར་གྱི་ཚིག་ནི་དཔེ་ཙམ་དུ་ཟད་དེ།

[Block 4771]
རྣམ་པ་དེ་དག་དང་དམ་བཅས་པ་ལས།

[Block 4772]
འདིར་གཞན་ཡང་ཁ་འོག་ཏུ་ལུས་འཁྲུས་པར་མི་བྱེད་ན། ཡང་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་སྦྱར་རོ། །

[Block 4773]
གླེང་གཞི་ལ་སོགས་པར་གཏོགས་པའི་དབྱར་གྱི་གཞིའོ། །

[Block 4774]
དབྱར་གྱི་གཞི་རྫོགས་སོ།། །།

[Block 4775 [HEADING]]
## དགག་དབྱེའི་གཞི། ^13-0

[Block 4776]
མི་སྨྲ་བའི་ཡིད་དམ༌[^3357]བཅའ་བར་མི་བྱའོ། །

[Block 4777]
འདིས་དག་པ་དང་གྲོལ་བ་ཐོབ་བོ་སྙམ་ན་ཉེས་པ་སྦོམ་པོ་ཞེས་བྱ་བ་ལ། འདིས་ཞེས་བྱ་བ་ནི་མི་སྨྲ་བ་འདིས་སོ། །

[Block 4778]
དགེ་འདུན་འབྱེད་པ་ལ་བརྟུལ་བའི་ཕྱོགས་ལ་འདི༌[^3358]རིག་པར་བྱའོ། །

[Block 4779]
འདིར་གཞུང་ནི། མི་གཏི་མུག་ཅན་འདི་ནི་མུ་སྟེགས་ཀྱི་རྒྱལ་མཚན་ཏེ། འདི་ལྟ་སྟེ་མི་སྨྲའོ། །

[Block 4780]
དེ་ལྟ་བས་ན་དགེ་སློང་གིས་མི་སྨྲ་བའི་ཡིད་དམ་བཅས་ན་ཉེས་པ་སྦོམ་པོའོ། །

[Block 4781]
དགེ་སློང་མི་སྨྲ་བའི་ཡིད་དམ་བཅའ་བར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4782]
དབྱར་གནས་པའི་དགེ་འདུན་ལ་མཐོང་བ་དང་ཐོས་པ་དང་དོགས་པ་དག་གིས་དགག་དབྱེ་བྱའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཡང་རུང་བས་དབྱར་རལ་བ་ཡང་རུང་དབྱར་མ་རལ་བ་ཡང་རུང༌[^3359]སྟེ་དབྱར་གྱི་དུས་རྫོགས་པར་བྱའོ། །

[Block 4783]
གང་གི་ཕྱིར་དབྱར་རལ་བ་ལ་དགག་དབྱེ་མི་བྱ་བ་མ་ཡིན་ནོ། །

[Block 4784]
དུས་གང་གི་ཚེ་ན་དེའི་ཕྱིར་དབྱར་རྣམས་ཀྱི་ཐ་མའི་ཉི་མ་ལའོ། །

[Block 4785]
སྤྱོད་ཡུལ་དུ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །གང་གི་དུས་ནས་ཤེ་ན། དེའི་ཕྱིར་གང་ཚུན་ཆད་ནས་བྱི་དོར་བྱེད་པ་ནས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྔར་དབྱར་གྱི་གཞིའི་སྐབས་སུ་ཞག་བཅུའམ་ཟླ་བ་ཕྱེད་ཀྱིས་འབྱུང་བར་འགྱུར་བ་ཉིད་ན་གཙུག་ལག་ཁང་བྱི་དོར་བྱའོ། །

[Block 4786]
ཁ་ཅིག་ལས་ནི་བདུན་ནམ་བརྒྱད་ན་ཞེའོ་ཞེས་སྨོས་པས་བྱི་དོར་བྱེད་པར་རྩོམ་པའི་དུས་གང་ཡིན་པ་དེའི་ཚེ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཇི་སྐད་བརྗོད་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དེང༌[^3360]ཕྱིན་ཆད་ཞག་འདི་ཙམ་ན་དགག་དབྱེ་མཛད་པར་འགྱུར་བ་ཁྱེད་ཅག་ལ་བརྗོད་པ་ཡིན་ནོ། །

[Block 4787]
གཙུག་ལག་ཁང་བརྒྱན་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཚུན་ཆད་ནས་བྱི་དོར་བྱ་བ་བསྟན་པ་སྟེ། དབང་དུ་བྱས་པས་ཤེས་པར་བྱའོ། །

[Block 4788]
ཁང་པ་བརྩེགས་པ༌[^3361]དག་བརྩིག༌[^3362]གོ། །

[Block 4789]
གཙང་ཁང་བྱུར་བུ་དག་ཀྱང་རི་མོ་བྲིའོ། །

[Block 4790]
མཆོད་རྟེན་དག་གསོ་བ་དང་བྱི་བྱད༌[^3363]བྱའོ། །

[Block 4791]
སེང་གེའི་ཁྲི་བརྒྱན་པར་བྱའོ། །

[Block 4792]
དོ་མོད་མཚན་ཐོག་ཐག་ཆོས་མཉན་པ་འབྱུང་བར་འགྱུར་གྱི།[^3364] དེར་ཚེ་དང་ལྡན་པ་དག་གི་ཚོགས་པ་སྦྱིན་པར་བྱའོ་ཞེས་སྤྱོད་ཡུལ་དུ་བརྗོད་ནས་མདོ་སྡེ་དང་། འདུལ་བ་དང་མ་མོ་འཛིན་པ་ལ་གསོལ་བ་བཏབ་པ་དག་གིས་ཚེས་བཅུ་བཞིའི་མཚན་ཐོག་ཐག་ཏུ་ཆོས་མཉན་པ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ལ། ཚེས་བཅུ་བཞི་ཞེས་བྱ་བ་ནི་གཞན་ཞེས་བྱ་བ་འོག་མའི་ཆོ་ག་བརྗོད་པ་ལས་ཤེས་པར་བྱའོ། །

[Block 4793]
གཞན་ལ་ནི་དེ་དག་གིས་ལས་ཀྱི་མདུན་རོལ་ཚུན་ཆད་དུ་ཆོས་དང་ལྡན་པའི་གཏམ་རྣམ་པར་གཏན་ལ་དབབ་པས་མཚན་མོ་འདའ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། གཞན་ལ་ཞེས་བྱ་བ་ནི་ཚེས་བཅོ་ལྔ་ལའོ། །

[Block 4794]
དེ་དག་གིས་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་དང་འདུལ་བ་དང་མ་མོ་འཛིན་པ་དག་གིས་སོ། །

[Block 4795]
མདུན་རོལ་དུ་ཞེས་བྱ་བ་ནི་དགག་དབྱེ་ལས་སོ། །

[Block 4796]
ཚུན་ཆད་དུ་ཞེས་བྱ་བ་ནི་ཆོས་དང་ལྡན་པའི་གཏམ་རྣམ་པར་གཏན་ལ་དབབ་པས་ཇི་སྲིད་དགག་དབྱེའི་ལས་རྩོམ་པ་ལ་ཐུག་པ་དེ་ཚུན་ཆད་དུ་མཚན་མོ་འདའ་བར་བྱའོ། །

[Block 4797]
དེ་ལ་ཡང་གང་གི་ཞེ་ན། དེའི་ཕྱིར་དགག་དབྱེའི་ལས་ནི་སྐྱ་རེངས་འཆར་བའི་མདུན་དུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལྟར་དགག་དབྱེའི་ལས་བྱའོ། །

[Block 4798]
ཇི་ལྟར་སྐྱ་རེངས་དང་པོ་མ་ཤར་བར༌[^3365]ལས་ཐམས་ཅད་ཟིན་པ་དེ་ལྟར་དགག་དབྱེའི་ལས་བྱའོ། །

[Block 4799]
མཐར་ཐུག་པའི་ཆ༌[^3366]དང་ལྡན་པའི་སྐྱ་རེངས་ཀྱི་ལས་ལ་མི་བྱ་བ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4800]
དགེ་སློང་དགག་དབྱེའི་བྱེད་པ་བསྐོ་བར་བྱའོ། །
--- END BLOCKS ---
