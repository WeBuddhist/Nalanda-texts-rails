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
[Block 4586]
དེས་ཞེས་བྱ་བ་ནི་ཕན་གདགས་པའི་ཕྱིར། དོགས་པ་མེད་པའི་རྒྱུ་བསྟན་ཏོ། །

[Block 4587]
མི་ཞེས་བྱ་བ་འདིས་ནི་སྐལ་བ་མི་མཉམ་པ་ཡིན་པས། དོགས་པའི་གནས་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4588]
ཡང་ན་རང་བཞིན་ཡོངས་སུ་དག་པ་དེས། ཉེས་པ་བྱས་པ༌[^2970]དོགས་པ་མེད་པ་སྟེ།

[Block 4589 [VERSE]]
ཕན་གདགས་པའི་ཕྱིར་ཡང་བག་ཕབ་པའོ། །
གཅན་གཟན་ཁྲོ་བོ་ཐགས་ཐོགས་མེད་པར་འོང་། །

[Block 4590]
ཞེས་བྱ་བ་ལ། གཅན་གཟན་ཁྲོ་བོ་འོང་བ་ནི་འབྱུང་བ་སྟེ། ནགས་ཀྱི་ཕྱོགས་སུ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 4591]
ཐགས་ཐོགས་མེད་པ་ནི་ཀུན་ནས་ཐར་བའི་ཕྱིར་རོ། །

[Block 4592]
ངལ་བས༌[^2971]གཉིད་ཀྱིས་ལོག་པ་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ངལ་བ་དང་གཉིད་ཀྱིས་ལོག་པ་གཉིས་ཀྱིས་གཅན་གཟན་ཁྲོ་བོ་བཟློག་པར་མི་ནུས་པ་བསྟན་པ་ཡིན་ནོ། །

[Block 4593]
ང་ལ་ཕན་པ་འབྱུང་བ་ཡིན་པས་ང་ལ་ཕན་པའོ། །

[Block 4594]
མི་དེ་ལ་མ་མཚོན་པ་གཞན་མེད་པས། ང་ཤི་བར་གྱུར་ན་ནི་གྲོགས་མེད་པའི་ཕྱིར། འགྲོ་བ་ལ་ཉམས་ཉེས༌[^2972]པར་འགྱུར་ཏེ། དེ་བས་ན་མི་དེ་རང་ལ་ཕན་པར་འགྱུར་བ་ཡིན་ནོ། །

[Block 4595]
དེའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཀུན་ནས་ཐར་པའི་ནགས་ཀྱི་ས་ཕྱོགས་དེར། གཅན་གཟན་ཁྲོ་བོ་ཐགས་ཐོགས་མེད་པར་འོང་། །ཞེས་བྱ་བ་ཡིན་ཏེ། ཐགས་ཐོགས་མེད་པར་འོང་བའི་ཕྱིར་རོ། །

[Block 4596]
[^2973]མིག་ལྟོས་ལ་བསྲུང་བར༌[^2974]གྱིས་ཞེས་བྱ་བ་ནི་གཅན་གཟན་ཁྲོ་བོ་དག་ལས་སོ། །

[Block 4597]
ང་དང་ཁྱོད་བདག་གཉིས༌[^2975]ཞེས་བྱ་བ་ནི་བདག་ལ་ཕན་པ་དང་།

[Block 4598 [VERSE]]
ཁྱོད་བདག་ཉིད་ལ་ཕན་པའི་ཕྱིར་རོ། །
ང་ནི་ངལ་ཞིང་ལུས་ཀྱང་རབ་ཏུ་རྨྱ། །

[Block 4599]
ཞེས་བྱ་བ༌[^2976]ནི་སྔར་བསྟན་པའི་ངལ་བ་ཉིད་དོ། །

[Block 4600]
ང་ནི་ཉལ་བར་འདོད་ཅེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་གཉིད་ལོག་པར་རོ། །

[Block 4601]
དུལ་བ་ལྟར་ཚུལ་འཆོས་པ་ལ་མཁས་པ་དེ་ན༌[^2977]རེ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་རྐྱང་པས་ནི་དེའི་ཕྱིན་ཅི་ལོག་པ་ཉིད་བསྟན་ཏེ། རབ་ཏུ་འབད་པས་རྙེད་པའི་རྩ་བ་དང་། ཞེས་བྱ་བའི་ཚིགས་བཅད་བཞིས་བསྟན་པའོ། །

[Block 4602]
རབ་ཏུ་འབད་པས་རྙེད་པ་ཞེས་བྱ་བ་ནི་བརྐོ་བ་ལ་སོགས་པའི་རབ་ཏུ་འབད་པས་སོ། །

[Block 4603]
ཅི་དགར་རྙེད་པས་ཞེས་བྱ་བ་ནི་འབྲས་བུ་རྙེད་པ་དེ་གཅིག་མ་ཡིན་པ་ཉིད་དུ་བསྟན་ཏེ། རྩ་བ་དང་། འབྲས་བུ་གཉིས་ཀྱིས་ནི་འཚོ་བ་ཙམ་ཡང་མི་ནུས་པར་བསྟན་ཏོ། །

[Block 4604]
ཕན་པར་བྱས་ཀྱང་བཟའ་བ་ཉིད་དུ་བསྟན༌[^2978]ཏེ།

[Block 4605 [VERSE]]
འདིའི་རང་བཞིན་ནི་དེ་འདྲ་བའི་ཕྱིར་རོ། །
ཕོངས་པར་གྱུར་ན་ཆོས་ནི་གྲུབ་པ་ཡིན། །

[Block 4606]
ཞེས་བྱ་བ་ནི། དེའི་ཕྱིར་འཇིག་རྟེན་པ་རྣམས་ཀྱི་ཆོས༌[^2979]སྨྲ་བ།

[Block 4607 [VERSE]]
དྲག་པོ་དང་ནི༌[^2980]འཇམ་པ་སྟེ། །
གང་ཡང་རུང་བའི་ལས་ཀྱིས་ནི། །
བདག་ཉིད་ཕོངས་པའི༌[^2981]ཚེ་ན་སྤྱད། །
དེ་འོག་ཆོས་ནི་སྤྱད་པར་བྱ། །

[Block 4608]
ཞེས་བྱ་བ་ཡིན་ཏེ། རྒྱུ་དེའི་ཕྱིར་རོ། །

[Block 4609]
ཆགས་པ་ཉིད་སྐྱོན་ཡིན་པས་ཆགས་པའི༌[^2982]སྐྱོན་ནོ། །

[Block 4610]
དེས་རྨོངས་པའི་བློ་གང་ཡིན་པ་དེ་ནི་ཆགས་པའི་སྐྱོན་གྱིས་བློ་རྨོངས་པའོ། །

[Block 4611]
བདག་ཉིད་ངན་པ་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི་སྙིང་རྗེ་མི་གཏོང་བའི་རྒྱུ་བཞི་མེད་པར་བསྟན་ཏེ། བདག་ཉིད་ངན་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། འཇུངས་པ་མེད་པའི་རང་བཞིན་མེད་པར་བསྟན་པ་ནི། ཆགས་པའི་སྐྱོན་གྱིས་བློ་རྨོངས་པ། །ཞེས་བྱ་བ་འདིས་སོ། །

[Block 4612]
རབ་ཏུ་བརྟན་པ་དང་ལྡན་པ་ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པ་སྟེ། སྙིང་རྗེ་མི་གཏོང་བའི་རྒྱུ་དེའི་མི་མཐུན་པའི་ཕྱོགས་སྙིང་རྗེ་དང་། དེས་པའི་ངོ་བོ་སྤངས་ཞེས་བྱ་བས་བརྟན་པ་མེད་པར་སྟོན་ཏོ། །

[Block 4613]
བྱས་པའི་དྲིན་ནི་བརྗེད་ཅེས་བྱ་བ་འདིར། སྔར་བསྟན་པའི་བྱས་པ༌[^2983]གཟོ་བ་དེའི་མི་མཐུན་པའི་ཕྱོགས་བསྟན་ཏོ། །

[Block 4614]
ཆོས་ཀྱི་འདུ་ཤེས་ནི་ཉམས་ཞེས་བྱ་བ་ནི། སྔར་བསྟན་པའི་ཆོས་ཀྱི་འདུ་ཤེས་ནི་མ་ཉམས་ཞེས༌[^2984]བྱ་བ་དེའི་མི་མཐུན་པའི་ཕྱོགས་བསྟན་ཏོ། །

[Block 4615]
བཞི་པོ་འདི་དག་སྔར་བསྟན་པ་ལྟར་མ་ཡིན་པ༌[^2985]ཅིའི་ཕྱིར་གོ་རིམས་འདི་ལྟར་བཀོད་ཅེ་ན། ད་ལྟར་འདི་ནི་རྐྱེན༌[^2986]གྱི་རྒྱུ་ལས་སྐྱེས་པའི་ཕྱིར། བྱས་པ་མི་གཟོ་བ་དང་། ཆོས་ཀྱི་འདུ་ཤེས་ལས༌[^2987]ཉམས་པ་གཉིས་ཀྱི་དང་པོར། བདག་ཉིད་ངན་པ་ཆགས་པའི་སྐྱོན་གྱིས་ནི༌[^2988]བློ་རྨོངས། །ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4616]
གཞན་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 4617]
རྒྱུ་བཞི་པོ་འདིས་ཀྱང་། སྙིང་རྗེ་དང་། དེས་པའི་ངོ་བོ་ཉིད་རབ་ཏུ༌[^2989]སྤངས་པ་ཡིན་ནོ། །

[Block 4618]
ཉམ་ཆུང་བ་ཡང་ཡིན་ལ་མི་བརྟན་པ་ཡང་ཡིན་པས་ཉམ་ཆུང༌[^2990]མི་བརྟན་ནོ། །

[Block 4619]
ཡང་ན་ཉམ་ཆུང་བས་མི་བརྟན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4620]
གཉིད་ལས་སངས་པར་བྱ་བའི་ཕྱིར། །ཞེས་བྱ་བ་ནི༌[^2991]ཆེད་དུ་སྟེ། དེ་སངས་པར་བྱ་བའི་ཆེད་ལྟ་བུར་རོ། །

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
--- END BLOCKS ---
