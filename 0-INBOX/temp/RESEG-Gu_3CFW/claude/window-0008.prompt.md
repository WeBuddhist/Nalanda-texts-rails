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
[Block 281]
མཚོན་གྱིས་མ་དྲས་པའི་གོས་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། དེ་ལྟ་བས་ན་དགེ་སློང་དག་གིས་ཁྱིམ་བདག་གི་གོས་མཚོན་གྱིས་མ་དྲས་པ་དག་ཁ་དོག་ངན་པར་བྱ་སྟེ། བཅང་བར་གནང་ངོ་ཞེས་གསུངས་པ་ཡིན་གྱི་ཁ་དོག་ངན་པར་བྱས་པ་དང་བྲལ་བ་ལྟུང་བྱེད་དུ་གསུངས་པ་ནི་མ་ཡིན་ཏེ། ལྷག་མ་ཡང་འདི་དང་ཉེ་བར་སྦྱར་བའོ། །

[Block 282]
དྲས་ཤིང་དྲུབས་པ༌[^280]ཆོས་གོས་ཉིད་དུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་གསུངས་ན། རྣམ་པ་གང་གིས་དྲུབས་པ་གང་ཞེ་ན། དེའི་ཕྱིར་སྣམ་ཕྲན་སྦྲེལ༌[^281]གཞི་ཉིད་དང་ལྷག་མ་མཉམ་པ་ཉིད་དང་། དབུས་ནས་གཞན་དུ་གླེགས་བུའི་འཕྲོ་ཕྱོགས་ཕྱོགས་སུ་ལྟ་བ༌[^282]ཉིད་དང་མཐའ་བསྐོར་བ་ཉིད་དག་གིས་སོ་ཞེས་བྱ་པ་སྨོས་ཏེ། གདིང་བ་སྒྲུབ་པར་བྱེད་པའི་དུམ་བུ་རྣམས་ལ་ཕྱེད་དང་གསུམ་གྱི་དཀྱིལ་འཁོར་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པའི་ཆོ་ག་གསུངས་སོ། །

[Block 283]
དེའི་ཕྱིར་དེ་སྲིད་དུ་སྒྲུབ་པར་བྱེད་པའི་དུམ་བུའི་དབང་དུ་བྱས་ནས་མདོ་འདི་བྱས་སོ། །

[Block 284]
གླེགས་བུ་འཕྲོ་བཟུང་པའི་དབུས་ནས་སྣམ་ཕྲན་རྣམས་ལ་ལྷག་མ་གང་ཡིན་པ་དེ་ནི་འདིར་ལྷག་མ་ཉིད་དུ་གསུངས་སོ། །

[Block 285]
ཕྱོགས་ཕྱོགས་སུ་ཞེས༌[^283]ཟློས་བུར་བྱ་སྟེ། [^284]དབུས་ཀྱི་སྣམ་ཕྲན་གཞན་རྣམས་མངོན་པར་ཁྱབ་པར་བསྒྲུབ་པའི་དོན་དུ་སྣམ་ཕྲན་སྦྲེལ་གཞི༌[^285]ཉིད་དོ། །

[Block 286]
ལྷག་མ་མཉམ་པ་ཉིད་དང་དབུས་ནས་གཞན་གླེགས་བུ་འཕྲོ་ཕྱོགས་ཕྱོགས་སུ་ལྟ་བ༌[^286]ཉིད་ཅེས་བྱ་བ་དེའི་དངོས་པོ་ནི་དེ་ཉིད་དོ། །

[Block 287]
གླེགས་བུའི་འཕྲོ་ཕྱོགས་ཕྱོགས་སུ་ལྟ་བ༌[^287]ཉིད་ཅེས་བྱ་བ་ནི། རྒྱུད་གཞན་གྱི་ཁོངས་སུ་གཏོགས་པའི་གླེགས་བུའི་འཕྲོ༌[^288]དེའི་དངོས་པོ་དང་མཐའ་སྐོར་ཉིད་དག་གིས་སྦྱིན་པ་རྗེས་སུ་སོང་བ་ཉིད་དེ་དེ་ལྟར་རྣམ་པ་བཞི་པོ་འདི་རྣམས་ཀྱི་ཞེས་བྱ་བ་ནི་འདིའི་དོན་ཏོ། །

[Block 288]
ཇི་ཙམ་དུ་གྱོན་པའི་གོས་གང་ལ་ཆོས་གོས་ཀྱི་དོན་དུ་རྣམ་པ་དེ་ལྟ་བུར་བྱིན་གྱིས་བརླབ་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་མཐང་གོས་དང་བླ་གོས་དང་སྣམ་སྦྱར་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་གསུམ་ཆར་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 289]
དགེ་སློང་མས་ནི་ཤིང༌[^289]དཔུང་ཆད་དང་རྔུལ་གཟན་རྣམ་པ་གང་ཡང་རུང་བའོ་ཞེས་བྱ་བ་ནི་འདི་དག་དང་དེ་མ་ཐག་པའི་གསུམ་པོ་དགེ་སློང་མས་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 290]
རྣམ་པ་གང་ཡང་རུང་བ་ཞེས་སྨོས་པ་ནི༌[^290]དྲས་ཤིང་དྲུབས་པ་ཞེས་བྱ་བ་ལས་བཟློག་པའི་དོན་དུའོ། །

[Block 291]
འདིའི་གཞུང་ནི་ཕྲན་ཚེགས་དག་ལས།

[Block 292]
བསྙེན་པར་རྫོགས་པའི་ཆོ་ག་ལས་ཆོས་གོས་ལྔ་པོ་རྣམས་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དང་། དགེ་སློང་མའི་སོ་སོར་ཐར་པ་དང་།

[Block 293]
དེའི་རྣམ་པར་འབྱེད༌[^291]པ་དག་ལས།

[Block 294]
[^292]དགེ་སློང་མ་ཆོས་གོས་ཟིན་པས་གཏན་པ་ཕྱུང་ནས། གལ་ཏེ་ཆོས་གོས་ལྔ་པོ་གང་ཡང་རུང་བ་དག་ལས་ཆོས་གོས་གཅིག་དང་། ནུབ་གཅིག་མཚམས་ཀྱི་ཕྱི༌[^293]རོལ་དུ་བྲལ་ན་སྤང་བའི་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 295]
ཆོས་གོས་ལྔ་པོ་དག་ཅེས་བྱ་བ་ནི། སྣམ་སྦྱར་དང་། བླ་གོས་དང་། མཐང་གོས་དང་། ཤིང༌[^294]དཔུང་ཆད་དང་། རྔུལ་གཟན་ཞེས་བྱ་བ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 296]
བརྙན་པོ་ཡང་ཡོད་ཅིང་བདོག་ནའོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་ཆོས་གོས་དྲས་ཤིང་དྲུབས་པ་བརྙན་པོ་ཡང་ཡོད་ཅིང་བདོག་ན་དེའི་ཚེ་ཡང་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 297]
གལ་ཏེ་མི་བདོག་ན་ནི་དྲས་ཤིང་དྲུབས་པ་མ་ཡིན་པ་ལ་ཡང་བྱིན་གྱིས་བརླབ་པར་བྱ་སྟེ། ཆོས་གོས་བྱིན་གྱིས་མ་བརླབས༌[^295]པར་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 298]
དེ་དག་བཞག་སྟེ་སྐྱ་རེངས་འཆར་བ་འདའ་བར་མི་བྱའོ༌[^296]ཞེས་བྱ་བ་ནི། ཆོས་གོས་བྱིན་གྱིས་བརླབས་པ༌[^297]གསུམ་དང་འབྲལ་བར་མི་བྱ་སྟེ། བརྙན་པོ་ཡང་ཡོད་ཅིང་བདོག་ནའོ་ཞེས་བྱ་བ་འདི་དང་སྦྱར་བས་འབྲེལ་བར་རིག་པར་བྱའོ། །

[Block 299]
ཉིན་ཞག་འདའ་བར་བྱེད་ན་དེ་ལྟ་བུའི་རིགས་ཅན་རྣམས་ལ་འདའ་བར་བྱ་བ་ཉིད་དུ་རིགས་པ་དེ་བས་ན་སྐྱ་རེངས་འཆར་བ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཞན་མེད་ན་ཁ་མ་བསྒྱུར་བ་ལ་ཡང་བྱིན་གྱིས་བརླབ་པ༌[^298]འཆགས་སོ་ཞེས་བྱ་བ་ནི་ཁ་བསྒྱུར་བ་མེད་ན་ཆོས་གོས་གསུམ་པོ་འདི་ཁ་མ་བསྒྱུར་བ་ལ་ཡང་རྣམ་པར་རྟོག་པ་དོར་ནས་བྱིན་གྱིས་བརླབ་པའོ། །

[Block 300]
དེ་ལ་དོར་བས་དོགས་པ་ལ་གོ་སྐབས་ཉིད་དོ།[^299] །ཁ་བསྒྱུར་བ་ཉིད་ལ་ཡང་འདི༌[^300]འཆགས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་མེད་པས་རབ་ཏུ་མ་རྙེད་པ་ལ་ཁ་མ་བསྒྱུར་བའི་དོན་ལ་རུང་བས་ཅི་ཞིག་བསྒྱུར་པར༌[^301]བྱ་སྟེ། འདིར་ཡང་དོགས་པ་མེད་པ་ཁོ་ནའོ། །

[Block 301]
གང་གི་ཕྱིར་ལོངས་སྤྱོད་པ་ལ་ཁ༌[^302]བསྒྱུར་བ་ཉིད་དང་། ཡན་ལག་གི་ངོ་བོར་རུང་བ་ལ་ལོངས་སྤྱོད་པའི་ངེས་པ་ལ་ཡན་ལག་ཉིད་དོ། །

[Block 302]
ཁ་བསྒྱུར་བ་ཉིད་ནི་རུང་བའོ། །

[Block 303]
དེ་ལྟར་ཡང་དཀར་པོའི་བྱ་བ་ཉིད་བསལ་བས་དོན་འདི་རུང་བའི་གཞི་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 304]
དེ་ལྟ་བས་ན་ཁ་མ་བསྒྱུར་བ་ལ་ཡང་བྱིན་གྱིས་བརླབ་པ་འཆགས་པས་ན་དོན་འདི་བྱས་སོ། །

[Block 305]
མ་དྲས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གཞན་ཟིན་པ་ལ་ཡང་བྱིན་གྱིས་བརླབ་པ་འཆགས་སོ། །

[Block 306]
དེ་དྲང་བའི་དོན་དུ༌[^303]ཡང་གི་སྒྲའོ། །

[Block 307]
འདིར་གཞན་ཟིན་པ་ནི་དྲས་པ་གཞན་མ་ཟིན་པའོ། །

[Block 308]
དེ་ལ་གལ་ཏེ་འབྱོར་ན་ལྷན་ཐབས་གླན་ནོ་ཞེས་བྱ་བ༌[^304]དེ་ལ་ཞེས་བྱ་བ་ནི་མ་དྲས་པ་ལའོ། །

[Block 309]
གཞན་མ་ཟིན་པ༌[^305]བྱིན་གྱིས་བརླབ་པར་འདོད་པ་དང་། བྱིན་གྱིས་བརླབ་པ་ལ་དེའི་ཚེ་གཞན་མ་ཟིན་པ་ལའོ། །

[Block 310]
གལ་ཏེ་འབྱོར་ན་ཞེས་བྱ་བ་ནི་ལྷན་ཐབས་གླན་པ་སྦྱིན་པར་བྱའོ། །

[Block 311]
ཁྱིམ་དུ་རུང་བའི་རྣམ་པ་ལ༌[^306]ཡང་ངོ་ཞེས་བྱ་བ་ནི། གཞན་ཟིན་པ་མེད་ན་བྱིན་གྱིས་བརླབ་པ༌[^307]འཆགས་པའོ་ཞེས་བྱ་བ་འདི་ལ་ཡང་གི་སྒྲས་ནི་དགུག་པའོ། །

[Block 312]
ཁྱིམ་དུ་རུང་བའི་རྣམ་པ་འདི་ལ་ཡོད་པས་ན་ཁྱིམ་དུ་རུང་བའི་རྣམ་པའོ། །

[Block 313]
རུང་བས་ཀྱང་དགེ་སློང་གི༌[^308]ཆོས་གོས་ཀྱི་རྣམ་པ་ཉིད་དུ་མ་རེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 314]
ཕྱིང་བ་དང་ལ་བ་དང་བེའུ་ཕྲུག་དང་ཀླམ་དང་སེངས་པ་རྣམས་ནི་མི་དྲ་བར་ལྷན་ཐབས་སུ་ཀླན༌[^309]ཞིང་དྲུབ་པོ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་ཉིད་དུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ། །

[Block 315]
སྤུ་ཅན་ནི་ཆོས་གོས་ཉིད་དུ་བྱིན་གྱིས་བརླབ་པར་མི་བྱའོ་ཞེས་གསུངས་མོད་ཀྱི། སྤུ་ཅན་ནི་ལ་བ་དང་བེའུ་ཕྲུག་དག་ལ་འདི་དག་སྤུ་བྱི་བ་ཡང་སྲིད་པས་འདིར་དེ་གཉིས་གཟུང་བར་རིག་པར་བྱའོ། །

[Block 316]
འདིར་གཞུང་ནི་དགེ་སློང་དག་ལྔ་པོ་དག་ནི་མི་འདྲ་བ་དག་ཡིན་ཏེ། ཕྱིང་པ་ཐམས་ཅད་དང་། ལ་བ་ཐམས་ཅད་དང་། བེའུ་ཕྲུག་ཐམས་ཅད་དང་། ཀླམ་ཐམས་ཅད་དང་། གོས་སེངས་པ་ཐམས་ཅད་དང་། ལྷན་ཐབས་གླན་ཏེ་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 317]
དེ་ལ༌[^310]ཅུང་ཟད་ཀྱང་ནུས་པར་བྱ་བ་མ་ཡིན་མོད་ཀྱི་འདིར་བྱིན་གྱིས་བརླབ་པར༌[^311]བྱ་བ་ཉིད་ཀྱིས་ཁས་བླངས་པ་རྟོགས་པའི་ཕྱིར་ཞེས་བྱ་བ་འདི་ལྟར་ཤེས་པ་ཡིན་ནོ། །

[Block 318]
གནས་མལ་མི་གཙང་བས་གོས་པར་གྱུར་ན་དེའི་མོད་ལ་སྦྱར་བར༌[^312]བྱའོ། །

[Block 319]
དགེ་འདུན་གྱི་རྩྭའི་ཁྲི་དང་ཁྲིའུ་མ་གཏོགས་པ་སྟན་ཡན་ཆད་ལ་དེ་མ་ཡིན་པའི་གདིང་བ་མེད་པ་དང་གདིང་གཡོགས་ལ་ཡང་བར་ཆད་མ་བཅུག་པ་ཉེ་བར་སྤྱད་པར༌[^313]མི་བྱའོ་ཞེས་བྱ་བ་ལ༌[^314]ཁྲི་དང་ཁྲིའུ་མ་གཏོགས་པ་ཞེས་བྱ་བ་ནི་ཁྲི་དང་ཁྲིའུ་ལས་གཞན་པའོ། །

[Block 320]
རྩྭའི་ཁྲི་དང་ཁྲིའུ་ཞེས་བྱ་བ་ནི་འདིར་རྩྭ་མུན་ཛ་དང་གྲེས་མའི་ཁྲི་དང་ཁྲིའུ་ལ་སོགས་པའི་ཐགས་མས་བརྒྱུས་པ་ལ་སྨོས་སོ། །
--- END BLOCKS ---
