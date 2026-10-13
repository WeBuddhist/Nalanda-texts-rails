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
[Block 3571]
གཞན་དག་ལ་རབ་ཏུ་སྟོན་པ་ན་གདུལ་བྱ་རྣམས་ལ་བསྟན་པའོ། །

[Block 3572]
ཡི་གེའི་དོན་ནི་ཆོས་བསྟན་པ་ཙམ་ཡིན་པས་སོ། །

[Block 3573]
ཆོས་ཐམས་ཅད་སྟོང་པའོ་ཞེས་པ་ནི་རྣམ་པར་ཐར་པའི་སྒོ་ནས་ཞེས་ཚིག་གི་ལྷག་མའོ། །

[Block 3574]
སྤྱིའི་དོན་ནི། མདོ་སྡེ་པ་ལ་སོགས་པའི་འགྱོད་པ་བཟློག་པས་སོ། །

[Block 3575]
སྣང་བ་གསུམ་གྱི་ངོ་བོ་ཉིད་ཅེས་པ་ནི་སྣང་བ་ལ་སོགས་པའི་རང་བཞིན་ནོ། །

[Block 3576]
ཁམས་ཕྲ་བ་ནི་འོད་གསལ་བའོ། །

[Block 3577]
སྐད་ཅིག་རེ་རེ་ཞིང་ཞེས་པ་ལ། སྐད་ཅིག་དང་ཐང་ཅིག་དང་ཡུད་ཙམ་མིག་བཙུམས་དང་ཐལ་མོ་བརྡེབས་པ་ལ་སོགས་པའོ། །

[Block 3578]
རྗེས་སུ་མྱོང་བ་ལ་སོགས་པས་འདོད་ཆགས་དང༌[^2270]བྲལ་བ་ལ་སོགས་པས་རང་བཞིན་གྱི་ཚོགས་བརྒྱ་དྲུག་ཅུ་དེའི་བདག་ཉིད་ཀྱིས་ཉམས་སུ་མྱོང་ནས་སླར་ཡང་འོད་གསལ་བ་ཉིད་དུ་འཇུག་པར་བྱ་ཞེས་བསྟན་ཏོ། །

[Block 3579]
ཇི་སྐད་དུ།

[Block 3580 [VERSE]]
ཆུ་འཛིན་དུ་མ་སྣ་ཚོགས་པ། །
མདོག་དང་དབྱིབས་ནི་ཐ་དད་པ། །
ནམ་མཁའི་དབྱིངས་ལས་བྱུང་ནས་ནི། །
དེ་ཉིད་དུ་ནི་ཐིམ་འགྱུར་བཞིན། །

[Block 3581 [VERSE]]
དེ་བཞིན་རང་བཞིན་ཐམས་ཅད་ནི། །
སྣང་བ་གསུམ་གྱི་རྒྱུ་ཅན་ཏེ། །
མ་ལུས་ཡུལ༌[^2271]ལ་འཇུག་ནས་ནི། །
འོད་གསལ་བར་ཡང་འཇུག་པར་འགྱུར། །

[Block 3582]
ཞེས་འབྱུང་ངོ་། །སྦས་པ་ནི་ཡེ་ཤེས་གསུམ་རྣམ་པར་སྤྱོད་པས་སོ། །

[Block 3583]
རིལ་པོར༌[^2272]འཛིན་པ་དང་རྗེས་སུ་གཞིག་པའི་རིམ་གྱིས་ཞེས་པ་ནི་རེ་ཞིག་དང་པོ་རྣལ་འབྱོར་པས་ལྟེ་བར་རྩིབས་བརྒྱད་པའི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་འཁོར་ལོ་ལ་འོད་འབར་བའི་ཡི་གེ་རཾ་ལ་བལྟས༌[^2273]ཏེ། དེ་ལས་བྱུང་བའི་འོད་ཟེར་གྱི་ཚོགས་ཀྱི་སྤྱི་བོ་ནས་རྐང་པའི་བར་དུ་བསྲེག་པར་བྱ་སྟེ། འོད་གསལ་བའི་རང་བཞིན་དུ་གནས་པ་གང་ཡིན་པ་དེ་ནི་རིལ་པོར་འཛིན་པ་ཞེས་བྱ་བའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 3584]
འོད་ཟེར་གྱི་ཚོགས་དེ་ཉིད་ཀྱིས་བརྟན་པ༌[^2274]དང་གཡོ་བའི་འཇིག་རྟེན་གྱི་ཁམས་དང་པོ་སྣང་བ་མེད་པར་བྱས་ལ། ཕྱིས་བདག་ཉིད་ཀྱང་དེ་བཞིན་དུ་བྱ་བ་གང་ཡིན་པ་དེ་ཉིད་རྗེས་སུ་གཞིག་པའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 3585]
དེ་དག་གིས་སྣང་བ་མེད་པར་བྱས་པ་ནི་འོད་གསལ་བར་བྱས་པའོ། །

[Block 3586]
མཐར་ཐུག་པ་ན༌[^2275]དེ་ཁོ་ན་ཉིད་བཞི་པ་བསྟན་པས་སོ། །

[Block 3587]
དོན་ཡོད་པར༌[^2276]གྲུབ་པ་ཞེས་བྱ་བ་ནི་བྱ་བ་ནན་ཏན་གྲུབ་པའི་ཡེ་ཤེས་ཅན་ནོ། །

[Block 3588]
དམ་ཚིག་སྒྲོལ་མ་ནི་དམ་ཚིག་གི་རིགས་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3589]
དེའི་རྣམ་པར་ཐུགས་རྩེ་གཅིག་པ་ཞེས་པ་ནི་སྒྲོལ་མའི་བསྐྱེད་པའི་རིམ་པའི་མཚན་ཉིད་ཅན་ནོ། །

[Block 3590]
སྒྲ་ཇི་བཞིན་པ་ནི་བསྐྱེད་པའི་རིམ་པ་ཙམ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3591]
དོན་ཡོད་པར༌[^2277]གྲུབ་པ་ཞེས་བྱ་བ་ལ། དམ་ཚིག་ཉམས་པ་ལ་སོགས་པའི་སྐྱོན་བཟློག་པའི་དོན་དུ་རྩོལ་བ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3592]
དྲང་བའི་དོན་ནི་བསྐྱེད་པའི་རིམ་པ་ཙམ་འདོད་པས་སོ། །

[Block 3593]
རྡོ་རྗེ་ཡེ་ཤེས་ནི་བྱ་བ་ནན་ཏན་གྲུབ་པའི་ཡེ་ཤེས་སོ། །

[Block 3594]
ངེས་པའི་དོན་ནི་རྣམ་པར་དག་པའི་ངོ་བོ་ཉིད་དེ་ཁོ་ན་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3595]
སྒྲ་ཇི་བཞིན་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 3596]
ལྷ་མོ་བཞི་པོའི་དེ་དག་ལྷན་ཅིག་སྤྱོད་པ་སྟེ། དེ་བཞིན་གཤེགས་པ་རྣམས་སྙོམས་པར་ཞུགས་པར་མངོན་པར༌[^2278]འདོད་པའོ། །

[Block 3597]
དེ་རྣམས་དང་ལྷན་ཅིག་ཅེས་བྱ་བ་ལ་སོགས་པས་དེ་བཞིན་གཤེགས་པ་རྣམས་ལ་དེ་དང་ཡང་དག་པར་སྦྱོར་བས། བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཕུན་སུམ་ཚོགས་པ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 3598]
འདོད་པའི་དབང་ཕྱུག་ཡིན་པས་ཞེས་པ་ནི་འཁྱུད་པ་དང་འོ་བྱས་པ་དང་འཇིབ་པ་ལ་སོགས་པའི་མཚན་ཉིད་ཅན་ལོངས་སྤྱོད་པའི་མཆོག་གི་ཁྱད་པར་རྒྱུ་ཡིན་པས། བཙུན་མོ་མཆོག་གི་ཕུན་སུམ་ཚོགས་པའི་སྒྲས་སྤྱན་ལ་སོགས་པའི་རིགས་ཀྱི་ཡུམ་བཤད་དོ། །

[Block 3599]
སྒྲ་ཇི་བཞིན་པ་ནི་ལྷ་མོ་ཉེ་བར་སྡུད་པའི་དོན་ཙམ་སོ་སོར་བསྟན་པས་སོ། །

[Block 3600]
རྣམ་པར་སྣང་མཛད་ཉིད་ཀྱིས་དབང་བསྐུར་བའི་རྡོ་རྗེ་ཞེས་པ་ནི་འཕགས་པ་གཤིན་རྗེ་གཤེད་པོ་དཔལ་རྣམ་པར་སྣང་མཛད་ཀྱི་ཅོད་པན་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3601]
དཀྱིལ་འཁོར་བསྐྱེད་པ་གང་ཡིན་པ་ཞེས་པ་ནི་ཁྲོ་བོའི་རྒྱལ་པོ་རྣམས་སྲུང་བའི༌[^2279]འཁོར་ལོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3602]
སྒྲ་ཇི་བཞིན་པ་ནི་བསྐྱེད་པའི་རིམ་པ་ཙམ་བརྗོད་པས་སོ། །

[Block 3603]
དམྱལ་བ་ཞེས་པ་ནི་ཡི་དགས་ཀྱི་ལྷག་པར་བདག་པོའོ། །

[Block 3604]
ཁྲོ་བོ་ཆེན་པོའི་ཏིང་ངེ་འཛིན་གྱིས་ཞེས་པ་ནི་ཐབས་ལ་མཁས་པ་དང་ལྡན་པའི་ཁྲོ་བོའི་ཏིང་ངེ་འཛིན་གྱིས་ཞེས་བྱ་བའི་བར་རོ། །

[Block 3605]
དྲང་བའི་དོན་ནི་ཁྲོ་བོའི་རྣམ་པ་བརྗོད༌[^2280]པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3606]
རྨོངས་པའི་མུན་པ་སྟེ་ཞེས་པ་ནི་ཀུན་གཞི་རྣམ་པར་ཤེས་པའི་ངོ་བོ་ཉིད་དོ། །

[Block 3607]
མ་རིག་པ་ནི་དེའི་ཁྱད་པར་རོ། །

[Block 3608]
དོན་དམ་པའི་བདེན་པ་ཤེས་པ་ནི་ཕྱག་རྒྱ་དང་སྔགས་ཀྱིས་ཐོབ་པར་བྱ་བའི་སེམས་རྣམ་པར་དག་པའི་མཚན་ཉིད་ཅན་གྱི་འོད་གསལ་བས་སོ། །

[Block 3609]
ངེས་པའི་དོན་ནི་སེམས་རྣམ་པར་དག་པ་ཉིད་བསྟན་པས་སོ། །

[Block 3610]
སྒྲ་ཇི་བཞིན་པ་ནི་སྔ་མ་བཞིན་ནོ། །
--- END BLOCKS ---
