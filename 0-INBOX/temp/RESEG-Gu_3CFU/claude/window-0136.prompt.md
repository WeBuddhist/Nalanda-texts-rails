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
གསོ་སྦྱོང་ཐ་དད་པ་དང་རྙེད་པ་ཐུན་མོང་བའི་ལས་བྱའོ་ཞེས་བྱ་བ་ལ། ཐ་དད་པར་ཞེས་བྱ་བ་ནི་སོ་སོར་རོ། །

[Block 4762]
ཉེ་འཁོར་གྱི་གཙུག་ལག་ཁང་དང་ལྷན་ཅིག་ཏུ་གཙུག་ལག་ཁང་དེར་གསོ་སྦྱོང་ཐ་དད་པར་རྙེད་པ་གཅིག་པའི་ལས་ཀྱིས་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4763]
འགྲོ་བ་ན་དངོས་པོ་རྣམས་ཉེ་འཁོར་གྱི་གཙུག་ལག་ཁང་རྣམས་སུ་གདམས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་གཏད་པ་ན་གང་གི་ཚེ་འཕོངས་པ་ལ་སོགས་པའི་དབང་གིས་གཙུག་ལག་ཁང་ནས་འགྲོ་བར་འདོད་པ་མལ་སྟན་དང་སྣོད་ལ་སོགས་པའི་དངོས་པོ་རྣམས་ཉེ་འཁོར་གྱི་གཙུག་ལག་ཁང་རྣམས་སུ་གདམས་པར་བྱ་ཞེས་བྱ༌[^3252]བའི་དོན་ཏོ། །

[Block 4764]
གཉུག་མར་གནས་ན་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཏམས་པའི་དངོས་པོ་ལ་གང་དུ་གཏམས་པ་དེར་གཉུག་མར་གནས་པའི་དགེ་སློང་རྣམས་ཀྱིས་སྦྱིན་པར་བྱའོ། །

[Block 4765]
གནས་གཞན་གྱི༌[^3253]རྫས་གནས་གཞན་དུ་མི་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ངེས་པའི་རྙེད་པ་ལ་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བའི་མདོའི་ཕྱོགས་ཀྱི་རྗེས་སུ་བརྗོད་པའོ། །

[Block 4766]
འདི་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་ཅེས་བྱ་བའི་ཆོ་ག་འདིའི་ཡུལ་བསྟན་པའི་དོན་དུ་བརྗོད་དོ། །

[Block 4767]
སིལ་བུ་རྣམས་ལ་དེ་ལ་སོགས་པའི་སྟོབས་ཀྱིས་མི་སྦྱིན་པ་ཞེས་བྱའོ། །

[Block 4768]
འདི་ཡང་སྤང་བ་ནི་གནས་མལ་གྱི༌[^3254]ལྟུང་བྱེད་ལས།

[Block 4769]
མི་སྟེར་ན་དེ་དག་གི་སྦྱིན་པར་བྱ་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་དག་གི་ཞེས་བྱ་བ་ནི་གང་རྣམས་ཀྱི་རྫས་དེ་རྣམས་གཞན་ལ་སྦྱིན་པར༌[^3255]དེ་རྣམས་ལ་སྟེར་བ་མེད་པར་གྱུར་པ་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་དོ། །

[Block 4770]
ཁྱིམ་བདག་དེ་ཉིད་ཡིན་ཡང་ངེས་པ་ལ་གཞིག་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དེ་དང༌[^3256]ཁྱིམ་བདག་དེ་ཉིད་གནས་གཞན་དུ་སྦྱིན་བདག་དུ་གྱུར་ན་གང་གི་དངོས་པོ་དེ་གནས་གཞན་ལ་དངོས་པོར་གྱུར་ན་དེ་ལྟར་ན་ཡང་གང་ཞིག་གང་ལ་ངེས་པ་དེ་ནི་དེ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4771]
མི་སྟེར་ན་མཐུས་གཟུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་མི་སྣང་ན་ཡོད་པའམ་མེད་པའི་རྫས་བྱིན་པ༌[^3257]ལ་སྦྱིན་པར་བྱ་བ་ཉིད་ཅེས་བྱ་བའོ། །

[Block 4772]
ཆོ་ག་གཞན་པ༌[^3258]ལ་བསྒྲུབ་པ་གང་ཡིན་པ་དེ་བརྗོད་པའི་དོན་དུ་མདོ་འདི་བསྟན་པའོ།[^3259] །འདིར་མཐུས་བཟུང་བ་ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ཡང་འདི་བསྟན་པ་ཡང་རིག་པར་བྱའོ། །

[Block 4773]
གཡར་པོ་ཉིད་དུ་ནི་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་གཞན་གྱི་རྫས་ནི་གནས༌[^3260]གཞན་དུའོ། །

[Block 4774]
མཆོད་རྟེན་གཞན་ལ་བསྔོས་པའི་རྙེད་པ་མ་གྲུབ་པ་ལ་ནི་ཉེས་པ་མེད་དོ༌[^3261]བྱང་ཆུབ་ཆེན་པོ་དང་། ཆོས་ཀྱི་འཁོར་ལོ་དང་། ཆོ་འཕྲུལ་ཆེན་པོ་དང་། ལྷ་ལས་བབས་པ་རྣམས་ཀྱིས་དེ་དག་ལས་གཞན་ནི་མ་གཏོགས་སོ་ཞེས་བྱ་བ་ལ། མ་གྲུབ་པ་ལ་ཞེས་བྱ་བ་ནི་དེ་ཐོབ་པ་ལའོ། །

[Block 4775]
རྙེད་པ་དེ་ཞེས་བྱ་བ་ནི་མཆོད་རྟེན་གྱི་རྙེད་པ་ལའོ། །

[Block 4776]
འདིར་མཆོད་རྟེན་ཉིད་ཀྱི་ཚིག་ནི་སངས་རྒྱས་ཀྱི་བྱེ་བྲག་ཙམ་ལ་ཡིན་ཏེ། འདིར་གཟུགས་སྐུ་ལ༌[^3262]ནི་མ་བརྗོད་པ་མ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 4777]
ཧ་ཅང་ཐལ་བ་ལ་དམིགས་ཀྱིས་བསལ་བར་བརྗོད་པ་ནི་བྱང་ཆུབ་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། གནས་འདིའི་མཆོད་རྟེན་འདི་རྣམས་ནི་རྙེད་པ་ལ་མི་འགྲུབ་པ་མེད་ཀྱང་བཞི་པོ༌[^3263]འདི་རྣམས་ལས་གཞན་པའི་མཆོད་རྟེན་ལ་སྒྱུར་བར་བྱེད་པ་ནི་སྐྱོན་དང་བྲལ་བ་མ་ཡིན་ནོ། །

[Block 4778]
འདི་རྣམས་ལས་གཞན་ལ་མ་གྲུབ་པར་གྱུར་ཀྱང་ཉེས་པ་དང་བྲལ་བ་ཉིད་ཅེས་བྱའོ། །

[Block 4779]
རྙེད་པ་གང་ཞིག་བྱང་ཆུབ་ཆེན་པོ་དང་བལྟམ་པ༌[^3264]དང་ཆོས་ཀྱི་འཁོར་ལོའམ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་ལ་ངེས་པར་འབྱུང་བ་དེ་དྲན་པར་བྱ་ནུས་ལ། མཆོད་རྟེན་བཞི་པོ་དག་ལ་ཕུལ་བ་ནི་འདི་དག་དགེ་བའོ། །

[Block 4780]
གལ་ཏེ་མི་ནུས་ན་མཆོད་རྟེན་གཅིག་ཁོ་ན་ལ་དབུལ་བར་བྱའོ། །

[Block 4781]
ཁ་ཅིག་ལས་གཞན་ལ་ནི་མ་ཡིན་ནོ་ཞེས་འབྱུང་སྟེ། གང་ཞིག་འདིར་བལྟམ་པ༌[^3265]དང་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པ་དག་བཟུང་བ་ཡིན་གྱི་ཆོ་འཕྲུལ་ཆེན་པོ་དང་ལྷ་ལས་བབས་པ་དག་ནི་མ་ཡིན་ཏེ། དེ་ནི་ཡི་གེ་ཆད་པར་རིག་པར་བྱ་སྟེ། [^3266]ངེས་པ་རྣམས་ལ་ཆོ་ག་འདི་དང་ལྡན་པའི་ཕྱིར་དང་། བལྟམ་པ༌[^3267]དང་ཡོངས་སུ་མྱ་ངན་ལས་འདས་པའི་གནས་གཞན་ལ་ནི་མ་ངེས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4782]
བསྔོས་པ་ལས་བསྒྱུར་བའི་སྤང་བའོ།། །།

[Block 4783]
ཞག་བདུན་པར་བྱིན་གྱིས་བརླབས་པའི་ཉི་མ་འདས་སོ་ཅོག་དགེ་སློང་ལ་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དེང་ཕྱིན་ཆད་དུ་ཉི་མ་དང་པོ་འདས་ཏེ་དེང་ཉི་མ་གཉིས་པ་ལགས་སོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །གང་དུ་གསོག་འཇོག་གི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བཟའ་བའི་ཕྱིར་འཆང་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གསོག་འཇོག་ཉིད་ཀྱི་རྒྱུ་མཚན་ལ་བརྟགས་པའི་ཕྱིར་ཡོངས་སུ་སྤྱོད་པ་ལ་ལྟུང་བྱེད་འདི་རྣམ་པར་གཞག་པར་བྱས་པའོ། །

[Block 4784]
གང་གི་ཕྱིར་སྤང་བ་ཡོངས་སུ་སྤྱད་པ་ལ་དོན་མེད་པ་གླགས་མེད་པ་ཉིད་དོ། །

[Block 4785]
འོ་ན་དེའི་འོག་ཏུ་ཡོངས་སུ་ལོངས་སྤྱད་པར་བྱ་བ་སྤང་བའི་ལྟུང་བྱེད་ཅེས་བྱ་བ་འདིར་མདོ་ལས་གསུངས་སོ་ཞེ་ན། བདེན་མོད་ཀྱི་འོན་ཀྱང་འདིའི་འཆང་བ་ལ་ཉེ་བར་མཚོན་པ་དོན་གྱིས་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 4786]
དེ་བཞིན་དུ་ལྟུང་བ་རྒྱས་པར་བཤད་པ་ནི་འདིར་འཆང་བ་ལ་ལྟུང་བ་བརྗོད་པའི་ཕྱིར་དགེ་སློང་ལ་ཚེས་གཅིག་ལ་སྨན་ཞིག་བྱུང་ལ་ཚེས་གཉིས་པ་ལ་ཡང་སྨན་ཕྱི་མ་ཞིག་བྱུང་ན་དགེ་སློང་དེས་ཉི་མ་བདུན་པོ་དེ་ཉིད་ཀྱི་ནང་དུ༌[^3268]སྔ་མ་ཤོས་བྱིན་གྱིས་བརླབ་པར༌[^3269]བྱ་ཞིང་ཕྱི་མ་ཤོས་གཏང་བར༌[^3270]བྱ་བའམ་གཞན་ལ་སྦྱིན་པར་བྱའོ། །

[Block 4787]
ཡང་ན་ཕྱི་མ་ཤོས་བྱིན་གྱིས་བརླབ་པར་བྱ་ཞིང་སྔ་མ་ཤོས་གཏང་བར༌[^3271]བྱ་བའམ་གཞན་ལ་སྦྱིན་པར་བྱའོ། །

[Block 4788]
བྱིན་གྱིས་མི་རློབ་པར་བྱད་དམ་གཏོང་བར་མི་བྱེད་དམ་གཞན་ལ་སྦྱིན་པར་མི་བྱེད་ན་ཉི་མ་བརྒྱད་པའི་སྐྱ་རེངས༌[^3272]ཤར་བ་ན་སྤང་བའི་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །ཇི་སྲིད་འཆང་ཞེ་ན། དེའི་ཕྱིར་དེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཞག་བདུན་པར་བྱིན་གྱིས་བརླབ་པར་བྱས་པ་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4789]
བྱིན་གྱིས་མ་བརླབས་པ༌[^3273]ནི་ཞག་བདུན་ལས་འདས་པར་འཆང་བར་བྱ་བ་ཉིད་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་རུང་བ་ལ༌[^3274]འཆང་བར་བཀག་པ་སྟེ། འཐད་པའི་ངོ་བོར་ནི་མ་ཡིན་ཏེ། དབྱིག་དང་གསེར་ལ་ཡང་དོན་ལ་བརྟེན་ནས་རྗེས་སུ་གནང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4790]
ནམ་གྱི་ཚེ་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྐྱ་རེངས༌[^3275]

[Block 4791]
བརྒྱད་པ་ཤར་ནའོ་ཞེས་བྱ་བ༌[^3276]སྨོས་ཏེ། འདིར་ཚད་ནི་བླངས་པ་ཉིད་ན་འབྱུང་བ་ཞེས་བྱ་བ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 4792]
ཉེ་བར་ལོངས་སྤྱད༌[^3277]པར་བྱ་བ་མ་ཡིན་པ་ལ་ཉེ་བར་ལོངས་སྤྱོད་པའི་དོན་དུ་འཆང་བ་ཞེས་བྱ་བ་འདི་ནི་ཁ་ན་མ་ཐོ་བའོ། །

[Block 4793]
བྱིན་ལེན་མ་བྱས་པ་དང་རུང་བ་མ་ཡིན་པ་དང་བརྟག་པ་གཞན་དང་རྫས་གཞན་དང་འདྲེས་པ་ཉིད་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་གཞན་ཡང་མི་རུང་བ་ཉིད་དུ་གྱུར་པ་ལ་ཉེ་བར་ལོངས་སྤྱད་པར་བྱ་བ༌[^3278]ཉིད་མ་ཡིན་ནོ། །

[Block 4794]
དེ་བཞིན་དུ་དུས་སུ་རུང་བ་དང་ཐུན་ཚོད༌[^3279]དུ་རུང་བ་དང་འཚོ་བའི་བར་དུ་འཆང་བ་རྣམས་ལ་སྐྱོན་གྱིས་རུང་བ་མ་ཡིན་པ་ཉིད་དུ་འགྱུར་བའམ།[^3280] ཞག་བདུན་པ་ལས་བྱེ་བྲག་འགའ་ཡང་མེད་དོ། །

[Block 4795]
གང་གི་ཕྱིར་འདིར་དེ་རྣམས་ལོངས་སྤྱད་པར་བྱ་བ་མ་ཡིན་པ་རྣམས་ལ་ལོངས་སྤྱད༌[^3281]པའི་དོན་དུ་འཆང་བས༌[^3282]ཉེས་པ་འདི་མེད་པར་འགྱུར་བའམ་ན་སྨད་པ་མེད་པ་ཉིད་དོ། །

[Block 4796]
དེ་ལྟ་བས་ན་འདིར་སྨོས་པ་ནི་དཔེ་ཙམ་དུ་ཟད་པར་རིག་པར་བྱའོ་ཞེས་བྱ་བ་འདི་རྣམ་པར་གཞག་པ་འདི་རྟོགས་པར་བྱའོ། །གང་ཞེ་ན། དེའི་ཕྱིར་བཟའ་བར་བྱ་བ་རུང་བ་མ་ཡིན་པ་ཉིན་མཚན་འདས་པ་ནི་འདིར་ཟོས་པ་དང་འདྲ་བར་རྣམ་པར་གཞག་གོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བཟའ་བར་བྱ་བ་ཟོས་པ་ལྟར་ཞེས་བྱ་བ་འདིར་རྣམ་པར་གཞག་པའོ། །

[Block 4797]
རུང་བ་མ་ཡིན་པ་ཉིན་མཚན་འདའ་བར་བྱེད་ན་ལྟུང་བ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྐྱ་རེངས༌[^3283]

[Block 4798]
བརྒྱད་པ་ཤར་ནའོ་ཞེས་བྱ་བ་ནི་འདིར་དོན་ཏོ། །

[Block 4799]
འདིར་ཉིན་ཞག་ལ་ཉིན་མཚན་ཞེས་བྱ་བ་བརྗོད་པ་ཡིན་ནོ། །

[Block 4800]
ཉིན་མཚན་འདའ་བར་བྱེད་པ་ནི་ནང་དུ་ཞག་ལོན་པ་དང་ནང་དུ་བཙོས་པ་ལ་སོགས་པ་རུང་བའི་བཟའ་བ་ཇི་ལྟ་བུ་ཐོས་པ་ལ་ཁ་ན་མ་ཐོ་བ་དེ་ལྟ་བུ་འདིར་འཆང་བ་ལ་རིགས་པ་ཡིན་གྱི་ལྷག་པ་ནི་མ་ཡིན་ནོ། །
--- END BLOCKS ---
