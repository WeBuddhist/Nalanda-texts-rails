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
[Block 4936]
མི་སྤྲོ་ན་གསོལ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་དུ་སོ་སོར་གོ་བར་བྱེད་པ་དང་ཁྱིམ་རྣམས་སུ་སོ་སོར་གོ་བར་བྱེད་པ་མི་སྤྲོ་ན་ཐམས་ཅད་ཀྱིས་དགེ་སློང་དང་དགེ་སློང་མ་འདི་གཉིས་སྡིག་ཅན་ཡིན་ནོ་ཞེས་ཁྱིམ་དུ་སོ་སོར་གོ་བར་བྱེད་པ༌[^3341]ཞེས་བྱ་བ་དེའི་དོན་དུ་གསོལ་བར་བྱའོ། །ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 4937]
འདུ་ཤེས་གང་ལ་ཞེ་ན། དེའི་ཕྱིར་ཉན་པ་པོ་མི་ཤེས་པ་ཉིད་དང་བསྙེན་པར་མ་རྫོགས་པ་ཉིད་དག་དང་ལྡན་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉན་པ་པོ་བསྙེན་པར་མ་རྫོགས་པ་ཉིད་ལ་ཕམ་པ་དང་དགེ་འདུན་ལྷག་མའི་ལྟུང་བ་གང་ཡིན་པ་དེ་འདི་ལས་ཤེས་པ་ཡིན་ཏེ། དེ་ལ་ཡང་ཉན་པ་པོས་མི་ཤེས་པ་ཉིད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4938]
ཅི་ཞིག་རྗེས་སུ་བསྒྲུབས་ན་གནས་ངན་ལེན་བརྗོད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4939]
བརྗོད་པར་བྱ་བ་ཅི་ཞིག་སྨྲས་པས་ཤེ་ན། དེའི་ཕྱིར་ཕམ་པར་འགྱུར་བ་དང་དགེ་འདུན་ལྷག་མ་དག་སོ་སོར་ཡང་རུང་བསྡུས་པ་ཡང་རུང་ངོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4940]
དོན་དུ་མ་ཉིད་ལ་ཚིག་ཐ་དད་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་དེའི་ཕྱིར་བསྡུས་པ་དེ་ཉིད་ལ་ལྟུང་བ་གཅིག་ཉིད་ཡིན་ཏེ་ཚིག་གཅིག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4941]
འདི་ལྟ་སྟེ་དཔེར་ན་འདིས་སྲོག་ཆགས་ལྔ་བསད་དོ་ཞེས་བྱ་བ་ལ་དོན་ལྔ་པོ་འདི་རྣམས་ལ་གནས་གཅིག་ཏུ་ཅིག་ཅར་བརྫུན་དུ་སྨྲ་བས་བརྫུན་དུ་སྨྲ་བའོ། །

[Block 4942]
འདི་དག་ལས་གཞན་པའི་ཁ་ན་མ་ཐོ་བ་བརྗོད་པ་ནི་འདིའི་རྗེས་སུ་འབྲང་བས་ཉེས་བྱས་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 4943]
བརྗོད་པར༌[^3342]བྱེད་པ་ཇི་ལྟ་བུ་ལ་ཞེ་ན། དེའི་ཕྱིར་བསྐོ་བ༌[^3343]མ་བྱས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བརྗོད་པའི་ཕྱིར་གང་ལ་བསྐོ་བ༌[^3344]མ་བྱས་པ་དེ་ལའོ། ། ཅི་གནས་སྐབས་ཐམས་ཅད་ལའམ་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་ལ་མ་གསོལ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་འདུན་ལ་བརྗོད་ནས་དེའི་ཕྱིར་གསོལ་བ་ལ་ནི་བརྗོད་ཀྱང་ལྟུང་བ་མེད་དོ། །

[Block 4944]
བདེན་པར་སྨྲས་པ་ལ་འདི་ཞེས་བྱ་བར་རིག་པར་བྱ་སྟེ། བརྫུན་དུ་སྨྲ༌[^3345]ན་ནི་ལྟུང་བ་གཞན་རྣམ༌[^3346]པར་གཞག་པའི་ཕྱིར་རོ། །

[Block 4945]
གནས་ངན་ལེན་པ་བརྗོད་པའོ། །

[Block 4946]
སྨྲ་བའི་ཕམ་པར་འགྱུར་བ་ལ་ཆོ་ག་གང་ཡིན་པ་དེ་ཉིད་མི་ཆོས་བླ་མ་བརྗོད་པའི་ལྟུང་བྱེད་དོ། །

[Block 4947]
དེའི་ཕྱིར་དེའི་ཆོ་ག་ཡོད་པ་ཁས་བླངས་ནས་བྱེ་བྲག་སྨོས་པ་ནི་བདེན་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདུ་ཤེས་རྣམ་པར་མ་བཞག་ནས་ཡོད་པ་འམ་མེད་པའི་བླ་མའི་བདག་ཉིད་ཀྱིས་མིའི༌[^3347]ཆོས་ཀྱི་རིགས་པ་ཉིད་བརྗོད་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4948]
གང་ཟག་ཅི་འདྲ་བ་ལ་བརྗོད་ན་ཞེ་ན། དེའི་ཕྱིར་བདེན་པ་མ་མཐོང་བ་བསྙེན་པར་མ་རྫོགས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག་ལས་བདེན་པ་མཐོང་བ་ལྟ་བ་ཕུན་སུམ་ཚོགས་པ་ལ་བརྗོད་ན་ནི་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4949]
འཕྱ་བ་ཡོངས་སུ་བསལ་བའི༌[^3348]དོན་དུ་འདི་བཏགས་པའོ། །

[Block 4950]
ལྟ་བ་ཕུན་སུམ་ཚོགས་པ་ལས་གླགས་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 4951]
དེ་བས་ན་རིགས་པའི་ངོ་བོ་ཉིད་ཀྱི་རྣམ་པར་ངེས་ནས་བདེན་པ་མཐོང་བའི་ཚིག་བྱས་སོ། །

[Block 4952]
ཁྱིམ་པའི་མདུན་དུ་རྫུ་འཕྲུལ་རྣམ་པར་བསྟན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདུལ་བའི་དོན་ཉིད་ལ་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཕྲན་ཚེགས་དག་ལས་རྟོགས་པར་བྱའོ། །

[Block 4953]
དགེ་སློང་མས་སྟོན་པའི་སྤྱན་སྔར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྤྱན་སྔར་རྫུ་འཕྲུལ་རྣམ་པར་བསྟན་པར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 4954]
རྣམ་པ་འདི་གཉིས་ནི་ཕྲན་ཚེགས་ལས་འབྱུང་ངོ་། །མིའི་ཆོས་བླ་མ་བརྗོད་པའོ། །

[Block 4955]
གལ་ཏེ་བསྟན་པ་ཉིད་དུ་དགོས་ན་གསོལ་བ་སྔར་བཏང་བའི༌[^3349]དོན་བྱའོ་ཞེས་བྱ་བ་ནི་གསོལ་བ་བྱས་ནས་སྦྱིན་པར་བྱའོ། །

[Block 4956]
འདིས་ནི་མི་གཡོ་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་དེ་བསྡུས་པ་ཡིན་ནོ། །

[Block 4957]
གང་ལ་སྐུར་པ་འདེབས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དད་པ་ཕུལ་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་ཡང་དག་པར་རུང་བར་བྱས་ནས་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4958]
ལེགས་པར་རུང་བར་བྱས་ནས་ཞེས་བྱ་བ་ཁ་ཅིག་གིས་བྱས་པ་སྟེ། དེ་ནི་ཉམས་པར་ཡང་དག་པར་རིག་པར་བྱའོ། །

[Block 4959]
མི་སྲིད་པ་ཉིད་ཀྱི་ཕྱིར་བསྐྱེད་པས་བྱས་པའི་གྲོགས་དང་ས༌[^3350]དག་གིས་འཕགས་པའི་རྫས་ཀྱི་ཕྱིར་ལེགས་པར་རུང་བ་ཉིད་ལ་སྐྱེ་བ་ཉིད་ཡན་ལག་ཉིད་དུ་སོང་ནས་གནས་པར་བྱེད་ཅེས་བྱ་བའོ། །

[Block 4960]
འདིར་འདི་ཙམ་གྱི་དོན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4961]
རྣམ་པར་འབྱེད་པ་ལས་ཡང་དག་པར་རུང་བར་བྱ་སྟེ་ཞེས་བྱ་བའི་འདོད་པ་བྱིན་ནས་སོ། །

[Block 4962]
ཅི་ཞིག་བྱས་ན་སྐུར་པ་འདེབས་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་གིས༌[^3351]དགེ་འདུན་གྱི་ཟས་ཀྱི་རྙེད་པ་མ་ཡིན་པ་དགེ་སློང་གིས༌[^3352]གང་ཟག་ལ་ལོག་པར་བསྔོས་པ་ཡང་དག་པ་མ་ཡིན་པའི་དོན་ཉིད་གཞན་ལ་ཡང་མིང་མ་སྨོས་པར་བརྗོད་ན་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡང་དག་པ་མ་ཡིན་པའི་དོན་ཉིད་ཡོད་པ་ལ་ཟས་ཀྱི་རྙེད་པ་མ་ཡིན་པ་ལས་གཞན་དགེ་སློང་གི་དགེ་འདུན་གྱི་རྙེད་པ་ལ་དགེ་སློང་གིས༌[^3353]གང་ཟག་ལ་ལོག་པར་བསྔོས་པ་ཉིད་ཀྱིས་བརྗོད་པ་ལ་གཞན་ལ་ཡང་མིང་མ་སྨོས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4963]
གང་ཟག་ལ་ཞེས་བྱ་བ་ནི་འདིར་དགེ་སློང་ངམ་ཁྱིམ་པ་གཞན་ཡང་གང་ཟག་གི་སྒྲས་བཟུང་བ་ཤེས་པར་བྱའོ། །

[Block 4964]
བདག་ཉིད་གཅིག་པུ་མ་ཡིན་ནོ། །

[Block 4965]
འདིར་གཞན་བརྗོད་པ་ཚད་མ་གཉིས་ཀྱིས་མ་རྙེད་པ་བདག་ཉིད་མ་ཡིན་པ་དང་དགེ་སློང་ལ་སྔོ་བར༌[^3354]བྱེད་ཅེས་བྱ་བ་བརྫུན་དུ་སྨྲ་བས་གཞན་ལ་བརྗོད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4966]
བཟུང་ནས་མི་སྦྱིན་པ་དག་ལ་ཡང་མངོན་པར་བརྗོད་པ་འདི་ནི་ཤིན་ཏུ་སྡིག་ཆེ་བར་ཤེས་པར་བྱའོ། །

[Block 4967]
འདིར་ཁ་ཅིག་ནི་བདག་ཉིད་ལ་གང་ཟག་གིས༌[^3355]བསྔོ་བར་བྱ་ཞེས་བྱ་བའི་མདོ་བྱེད་པ་ཡིན་ནོ། །

[Block 4968]
འདིའི་རྣམ་པར་འབྱེད་པ་ནི་བདག་ཉིད་ལ་གང་ཟག་གིས༌[^3356]བསྔོ་བར་བྱ་ཞེས་བྱ་བ་བདག་ཉིད་ཀྱི་ཕྱིར་ཞེས་བྱ་བ་སྨོས་སོ་ཞེས་བྱ་བ་དེ་ནི་མི་རིགས་ཏེ་ཇི་ལྟར་བཤེས་ངོར་ཞེས་བྱ་བ་འདི་དང་འགལ་བའི་ཕྱིར་རོ། །

[Block 4969]
ཞུ་བ་ལས་ཀྱང་བཅོམ་ལྡན་འདས་ཀྱིས་ཡང་དགེ་སློང་གང་འདི་སྐད་ཅེས། ཚེ་དང་ལྡན་པ་བདག་གིས་འདི་ལྟར་བཤེས་ངོར་བྱས་ཏེ་དགེ་འདུན་གྱི་རྙེད་པ་བསྔོས་པ་གང་ཟག་ལ་སྔོ་བར༌[^3357]བྱེད་དོ་ཞེས་ཟེར་ན་ཞེས་གསུངས་ཏེ། [^3358]དགེ་འདུན་གྱི་རྙེད་པར་བསྔོས་པ་དག༌[^3359]གིས་ཤེས་པ་ཡིན་ནོ། །

[Block 4970]
ཇི་ལྟར་བཤེས་ངོར་བྱས་པའི་དགེ་སློང་རྣམས་ཀྱིས་སྔོ་བར༌[^3360]བྱེད་ཅེས་གསུངས་སོ། །

[Block 4971]
ཡི་གེ་གཞན་ལས་ཤེས་པ་འདིར་རྟགས་ནི་བསྔོ་བར་བྱ་ཞེས་གསུངས་པའོ། །

[Block 4972]
རིང་དུ་མ་འབྲེལ་བ་ཉིད་དགེ་སློང་གི་དགེ་འདུན་ལས་ཟས་ཀྱི་རྙེད་པ་མ་ཡིན་པ་ཞེས་བྱ་བའོ། །

[Block 4973]
ཟས་ཀྱི་ཡིན་པར་གྱུར་པའི་དགེ་འདུན་གྱིས་རྙེད་པ་ལ་དགེ་སློང་རྣམས་ཀྱི་ཡང་དགེ་འདུན་གང་ཡིན་པ་སྟེ། གཞན་རྣམས་ནི་མ་ཡིན་ནོ། །

[Block 4974]
འདིར་ཟས་ཀྱི་རྗེས་སུ་འབྲངས༌[^3361]པས་འདི་ལ་ཉེས་བྱས་སུ་རྟོགས་པར་བྱའོ། །

[Block 4975]
རྙེད་པ་ཞེས་བྱ་བ་ལ་རྙེད་པ་ནི་རྣམ་པ་གཉིས་ཏེ། གོས་ཀྱི་རྙེད་པ་དང་ཟང་ཟིང་གི་རྙེད་པའོ། །
--- END BLOCKS ---
