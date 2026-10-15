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
[Block 4446]
དགེ་འདུན་གྱི་རྫས་དེ་སྤོགས་པ་ལ་དགེ་འདུན་གྱི་ལས་བྱེད་པ་ལ་གཏད་དོ་ཞེས་བྱ་བ་ལ་རྫས་དེ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་རྫས་སོ། །

[Block 4447]
སྤོགས་པ་ལ་ཞེས་བྱ་བ་ནི་ཉོ་བ་ལ་སོགས་པའི་སྤྱོད་པས་དགེ་འདུན་ལ་རྙེད་པ་བསྒྲུབ་བྱ་ཞེས་བྱ་བ་ལ་སོགས་པ་གང་ཡིན་པ་དེ་ལ་དབྱིག་གཏད་པར་བྱའོ། །

[Block 4448]
ཅི་རང་གི་དེ་གཏད་པར་བྱ་འམ་ཞེ་ན་མ་ཡིན་ཏེ། དེའི་ཕྱིར་དགེ་འདུན་གྱི་ལས་བྱེད་པ་ལ་གཏད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དམ་གཞག་པ༌[^3041]ལ་སོགས་པ་ལ་དེ་གཏད་པ་རྗེས་སུ་བསྒྲུབ་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4449]
འདི་བརྗོད་པར་བྱ་སྟེ། རྒན་རབས་རྒན་རབས་ལ་མ་ཞུས་པར་དགེ་འདུན་གྱི་དོན་དུ་བརྩོན་པར་མི་བྱའོ། །

[Block 4450]
དེའི་ཚིག་ཡི་གེར་བྲི་བའི་དམ་གཞག་ལ་ནན་ཏན་བྱའོ་ཞེས་བྱ་བ་ནི་དུས་ག་གེ་མོ་ཞིག་གི༌[^3042]ཚེ་འདི་ཙམ་ཞིག་གཏད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པ། གང་དུ་ཡི་གེར་བྲི་བའི་དམ་གཞག་གཏད་པ་འདི་ལ་བརྗོད་པར་བྱའོ། །

[Block 4451]
དེ་བཞིན་དུ་རྫས་དེར་རིན་ཐང་འདི་ཙམ་གྱིས་ཉོས་ནས་འདི་ཙམ་ཞིག་ཏུ་བཙོངས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^3043]གཏད་ནས་དུས་ཕྱིས་རྗེས་སུ་བསྒྲུབ་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏེ། [^3044]ཉོ་ཚོང་བྱེད་པའི་སྤང་བའོ།། །།

[Block 4452]
བྱིན་གྱིས་མ་བརླབས་པའི་ཆོས་གོས་འཆང་བའི་ཆོ་ག་གང་ཡིན་པ་ཡོད་ནའོ་ཞེས་བྱ་བ་དང་། ཞག་བཅུར་རྗེས་སུ་ཞུགས་པ་ཉིད་དོ་ཞེས་བྱ་བ་དང་། གཞན་གྱི་ཉི་མའི་དང་པོ་ལའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་ཉིད་ལྷུང་བཟེད་ལ་ཡོད་ནའོ་ཞེས་བྱ་བ་དང་། རང་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པའི་གཞུང་ནི་རང་ཉིད་ལ་ལྟོས་ནས་གོས་ཡོད་པའོ། །ཞེས་བྱ་བ་སྨོས་པའི་གནས་སུ་འདིར་ལྷུང་བཟེད་ཀྱིའོ་ཞེས་བྱ་བ་གཞུག་པར་བྱ་སྟེ། དེའི་ཕྱིར་ལྷུང་བཟེད་ཀྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱིན་གྱིས་མ་བརླབས་པའི་འོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4453]
ཡུལ་དང་ཡུལ་ཅན་གྱི་འབྲེལ་པ་ལ་དྲུག་པ་སྟེ། ལྷུང་བཟེད་དང་འབྲེལ་པའི་ཕྱིར་འདིར་ལྷུང་བཟེད་ལ་རང་ཉིད་ཅེས་བྱ་བ་བརྗོད་དོ། །

[Block 4454]
དེའི་ཕྱིར་གོས་ལ་ཞེས་བྱ་བ་འདི་དང་འདིའི་ཐ་དད་པའི་དོན་ཤེས་པར་མི་བྱའོ། །

[Block 4455]
འཁོར་གསུམ་ཁེབས་པའི་མཐར་ཐུག་པའི་ཚད་ཅེས་བྱ་བ་འདི་ལ་འདི་མི་སྲིད་པའི་ཕྱིར་བཟློག་པའོ། །

[Block 4456]
དེ་ལྟར་ན་འདིར་མདོ་འདི་འབྱུང་བ་སྟེ་ཡོད་ནའོ་ཞེས་བྱ་བ་དང་རང་གི་ཉིད་དོ་ཞེས་བྱ་བ་དང་། ཞག་བཅུར་རྗེས་སུ་ཞུགས་པ་དེ་ཉིད་དོ་ཞེས་བྱ་བ་དང་། གཞན་གྱི་ཉི་མའི་དང་པོ་ལ་ལྷུང་བཟེད་བྱིན་གྱིས་མ་བརླབས་པ་དང་། བྱིན་གྱིས་བརླབས་པ་ཡོད་ནའོ་ཞེས་བྱ་བ་འདིར་བྱིན་གྱིས་མ་བརླབས་པ་དེའི་ཤན་ཚུན་ཆད་ནས་གཞན་དུ་ཞེས་བྱ་བའི་ཚིག་གིས་འདི་རྣམས་ནི་སྔར་གོས་འཆང་བའི་སྤང་བའི་སྐབས་སུ་བཤད་ཟིན་ཏོ། །

[Block 4457]
རབ་ཏུ་བྱུང་བ་ལ་ལྟོས་པའི་དོན་ཉིད་དུ་ངེས་པར་བྱས་པ་ནི་སྤངས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། གང་ཞིག་རབ་ཏུ་བྱུང་བ་ལ་ལྟོས་པའི་དོན་ཉིད་དུ་ལྷུང་བཟེད་བསྡོས་ཤིང་ངེས་པར་བྱས་པ་གང་ཡིན་པ་དེ་ནི་སྤང་བ་ཉིད་ཡིན་པས་དེའི་ཕྱིར་འཆང་ཡང་སྤང་བར་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4458]
སྐྱ་བ་དང་དཀར་བ་དང་། ཆེ་བ་རྣམས་ནི་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་རུང་བ་ཉིད་མ་ཡིན་པའི་ཕྱིར་འདི་རྣམས་ལ་བྱིན་གྱིས་བརླབ་པར་བྱ་བ་མ་ཡིན་པས་དེ་བས་ན་ན་སྨད་པ་ལ་ལྟུང་བ་བསྟན་པའོ། །

[Block 4459]
མ་ཚོས་པ་ཡང་ཆུང་ངུ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་རྗེས་སྙེགས༌[^3045]པའི་ཕྱིར་ཡང་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 4460]
མ་ཚོས་པ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ཀྱི་དོན་དུ་ཤིན་ཏུ་ཡང་མི་རུང་བ་ཉིད་དོ། །

[Block 4461]
དེའི་ཕྱིར་ན་ནག་པོར་གྱུར་ཀྱང་། འདི་ནི་མི་རུང་བ་ཉིད་དོ། །

[Block 4462]
འདིར་སྐྱ་བོའི་གཞུང་ནི་ཞུ་བ་ལས།

[Block 4463]
ལྷུང་བཟེད་མ་ཚོས་པ་འཆང་ན་ཉེས་བྱས་སོ། །

[Block 4464]
ལྷུང་བཟེད་དཀར་པོ་འཆང་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4465]
འདིར་སྐྱ་བོ་དང་། ཆེན་པོ་དག་ལ་ལྟུང་བ་མེད་དོ། །

[Block 4466]
ལྷུང་བཟེད་ཆུང་ངུ་ཡོད་དམ། ལྷུང་བཟེད་ཆེན་པོ་ཡོད་དམ། ལྷུང་བཟེད་སྐྱ་བོ་ཡོད་པར་གྱུར་ན་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4467]
སྨན་ཕོར་དུ་ཡོངས་སུ་སྤྱད་པའི་བསམ་པས་འཆང་ན་དེ་ལ་ལྟུང་བ་མེད་པར་གསུངས་པ་ཡིན་གྱི། ལྷུང་བཟེད་ཀྱི་དོན་དུ་ནི་འདི༌[^3046]རྣམས་ལ་འཆང་བར་བྱ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 4468]
འདི་ལ་མི་འོས་པ་བྱིན་གྱིས་བརླབས་པ་ལ་ཁ་ཟས་ལ་ཡོངས་སུ་ལོངས་སྤྱད་པའི་དོན་ཉིད་དུ་འཆང་བ་ལ་ཉེས་བྱས་ཏེ། གཞན་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བའི་རྣམ་པར་གཞག་པར་རིག་པར་བྱའོ། །

[Block 4469]
ལྷུང་བཟེད་ཆུང་ངུ་གཅིག་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ཆུང་ངུ་གཅིག་ལྷག་པར་འཆང་བ་ལ་ནི་ཉེས་པ་མེད་དོ། །

[Block 4470]
གང་ཞིག་ལྷུང་བཟེད་ཆུང་ངུས་ལྗོངས་རྒྱུར་འགྲོ་བར་བྱའོ་ཞེས་གསུངས་པའི་ཕྱིར་དེ་ནི་འདིའི་ཆེན་པོ་ཉིད་འཆང་བ་ལ་བསྟན་པའོ། །

[Block 4471]
ལྷུང་བཟེད་འཆང་བའི་སྤང་བའོ།། །།

[Block 4472]
ཧ་ཅང་ཆགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་གཞུང་ནི་གནས་མལ་གྱི་གཞིར་རོ། །

[Block 4473]
ཡོ་བྱད་ཅེས་བྱ་བ་མདོ་དང་པོ་གཉིས་ཏེ་གོས་ཀྱི་གཞིར་རོ། །

[Block 4474]
ཡོ་བྱད་ལ་ཧ་ཅང་ལྷག་པར་ཆགས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4475]
རང་གི་ཞེས་བྱ་བར་སྦྱར་བར་གྱུར་པ་ཉིད་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 4476]
ཡོ་བྱད་ནི་ཆོས་གོས་ལ་སོགས་པའོ། །

[Block 4477]
གང་ལ་ཞེན་པ་དེ་བཅང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་ཞེན་པ་ཞེས་བྱ་བ་ནི། ལྷག་པར་ཆགས་པའོ། །

[Block 4478]
གང་དུ་ཞེས་བྱ་བར༌[^3047]ལྷུང་བཟེད་ལ་སོགས་པ་ལས་བྱུང་བ་དེ་བཅང་བར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4479]
ལྷུང་བཟེད་ཀྱང་མེད་ན་བསླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་ཡོད་པས་སློང་བའི་ཉེས་པ་གང་ཡིན་པ་དེ་མི་འབྱུང་ཞེས་བྱ་བ་བྱས་ཏེ། ཆོས་གོས་བླང་བར་རྗེས་སུ་གནང་བ་གང་ཡིན་པ་དེ་ལ་ལྟོས་པ་ནི། འདིར་ཡང་ནི༌[^3048]སྒྲའོ། །

[Block 4480]
མེད་པ་གང་ཞིག་ལྷུང་བཟེད་ཡོངས་སུ་ཚོལ་བའི་སོ་སོར་ཡང་དག་པར་ལྡན་པ་ཁ་ན་མ་ཐོ་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དེ་ཡོད་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྷུང་བཟེད་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4481]
གཞན་ལ་ནི་ལྟུང་བ་མེད་ཅེས་བྱ་བ། ལྟུང་བའི་ཡུལ་ཉིད་ཀྱི་ཕྱིར་འདིའི་ཆོ་ག་བསྒྲུབ་པའོ། །

[Block 4482]
ཇི་ལྟ་བུ་ཞིག་ཡོད་པ་ཉིད་ན་ཞེ་ན་དེའི་ཕྱིར། ལྷན་པ་བཞི་མན་ཆད་ནས་དེ་དག་རུང་ཞིང་། ཡོངས་སུ་སྤྱད་བཟོད་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྷན་པ་བཞི་མན་ཆད་ནས་ནུས་པ་ཉིད་ཀྱིས་ལྷན་པ་འདི་ཙམ་རྣམས་ཀྱིས་དེ་ནས་བརྩམས་ཏེ། འདི་ལྟ་བུ་ཇི་སྲིད་ལྷུང་བཟེད་ཡོངས་སུ་ལོངས་སྤྱད་པར་ནུས་པ་དེའི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4483]
ཅུང་ཟད་སྐྱོན་མེད་པ་ཡང་ཤིན་ཏུ་སྙི་བ་ཉིད་ཀྱི་ཕྱིར་དང་། འཇམ་པའི་ས་གཞི་རང་བཞིན་ཉིད་ཀྱི་ཕྱིར་ཡོངས་སུ་ལོངས་སྤྱད་པར་བཟོད་པར་འགྱུར་བ་དེ་བཟློག་པའི་དོན་དུ་ཡོངས་སུ་སྤྱད་པར་བཟོད་པའོ་ཞེས་བྱ་བའི་བྱེ་བྲག་གོ། །

[Block 4484]
དེ་ཡོད་པ་ཉིད་ན་ཇི་ཞིག་ལྷག་པར་སྤྱད་ན་ཁ་ན་མ་ཐོ་བ་ཅི་འདྲ་བ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་པ་ཉེ་དུ་མ་ཡིན་པ་ལས་བསླངས་པས་ཡོངས་སུ་བཙལ་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱིམ་པ་ཉེ་དུ་མ་ཡིན་པ་ལས་བསླངས་ཏེ་ཡོངས་སུ་བཙལ་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4485]
དེ་གཉིས་ནི་འོག་མ་གཉིས་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདིའི་འོག་མ་བསླབ་པའི་གཞི་གཉིས་པོ་གང་དག་ཡིན་པ་དེ་དག་ལ་ཡང་ཉེ་དུ་མ་ཡིན་པ་དང་། ཁྱིམ་པ་ཉིད་ཅེས་བྱ་བ་འདི་གཉིས་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
