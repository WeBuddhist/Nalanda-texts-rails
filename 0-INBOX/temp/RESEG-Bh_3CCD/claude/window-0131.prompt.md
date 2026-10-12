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
ཨོཾ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་དོན་དམ་པའི་དཀྱིལ་འཁོར་བསྒོམས་པའི༌[^2765]འོག་ཏུ་སྔགས་འདི་བརྗོད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4587]
ཆོས་འབྱུང་བ་ལ་གནས་པའོ་ཞེས་པ་ནི་བགེགས་བསྐྲད་པ་དང་སྟོང་པ་ཉིད་བསྒོམས་པའི༌[^2766]འོག་ཏུ་ཡི་གེ་ཧཱུྃ་གི་ས་བོན་ལས་བསྐྱེད་པའི༌[^2767]གཞིའི་དཀྱིལ་འཁོར་གྱི་རང་བཞིན་གྱི་ཆོས་འབྱུང་གི་ཕྱག་རྒྱའི་སྟེང་དུ་ཡེ་ཤེས་ཀྱི་ས་གཞི་འབྱུང་བ་ཆེན་པོ་བཞིའི་རང་བཞིན་དང་རི་རབ་ཡོངས་སུ་གྱུར་པ་ལས།

[Block 4588]
རིན་ཆེན་སྣ་བདུན་གྱི་གཞལ་ཡས་ཁང་པའི་ནང་ན་སྣ་ཚོགས་པདྨ་དང་། ཟླ་བ་དང་། ཉི་མའི་དཀྱིལ་འཁོར་དུ་སྐད་ཅིག་གིས་རྫོགས་པའི་ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱིས་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་རྣམ་པར་བསྒོམ་པ་ལ། དེ་ཉིད་རྡོ་རྗེ་ཕྲེང་བ་ལས་གསུངས་པའི་གཟུགས་ཕུང་གཏོགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་དོན་དམ་པའི་དཀྱིལ་འཁོར་དུ་བྱས་ལ། ཡབ་ཡུམ་རོ་གཅིག་པར་གྱུར་ནས་སྔགས་འདིས་བརྟན་པར༌[^2768]བྱས་ཏེ། ཡང་ཡི་གེ་གསུམ་ལས་བྱུང་བའི་པདྨ་དང་ཟླ་བ་དང་ཉི་མའི་སྟེང་དུ་ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་ཟླ་བའི་དཀྱིལ་འཁོར་ལ་སྔ་མའི་པདྨ་ལ་སོགས་པ་གསུམ་ཞུགས་ཏེ་ཆོས་ཀྱི་དབྱིངས་ཀྱི་སྔགས་ཀྱིས་རང་གི་སེམས་བརྟན་པར་བྱས་ལ། དེའི་སྟེང་དུ་ཡི་གེ་གསུམ་རྣམ་པར་བཀོད་ལ་དེ་ནས་སྤྲོ་བ་དང་བསྡུ་བ་སྔོན་དུ་འགྲོ་བར་རྡོ་རྗེ་བསྐྱེད་ལ། དེ་ཡོངས་སུ་གྱུར་པ་ལས་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པའི་ལྷའི་འཁོར་ལོ་གང་ཡང་རུང་བ་རྣམ་པར་བསྒོམས་ཏེ། ཡེ་ཤེས་སེམས་དཔའ་དང་ཏིང་ངེ་འཛིན་སེམས་དཔའ་དགོད་པའི་མཚན་ཉིད་ཀྱི་རྗེས་སུ་རྣལ་འབྱོར་བྱས་ལ་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་ཡིག་འབྲུ་དགོད་པའི་མཚན་ཉིད་ཀྱི་ཤིན་ཏུ་རྣལ་འབྱོར་རྫོགས་ནས༌[^2769]སྐུ་ལ་སོགས་པ་ལ་བྱིན་གྱིས་བརླབ་པའི་རྣལ་འབྱོར་ཆེན་པོ་བྱས་ཏེ། ཕྱག་རྒྱ་འདུས་ནས་རེག་བྱ་རྡོ་རྗེ་མའི་ཆོས་འབྱུང་གི་ནང་དུ་ཕྱུང་བའི་སྔགས་ཀྱིས་དཀྱིལ་འཁོར་པ་རྣམས་སྤྲུལ་ཏེ། དེ་ལས་ཀྱང་ཕྱི་རོལ་དུ་སྤྲོས༌[^2770]ལ་འགྲོ་བའི་དོན་བྱས་ནས་སླར་ཡང་གཤེགས་ཏེ། ཤར་ལ་སོགས་པའི་ཕྱོགས་དང་མཚམས་སུ་དཀྱིལ་འཁོར་པ་རྣམས་རིམ་གྱིས་བཞུགས་པར་བསམས་ལ། དབང་བསྐུར་བ་དང་རྒྱས་བཏབ་ཅིང་དེའི་འོག་ཏུ་འཆད་པར་འགྱུར་བའི་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་ཕྲ་མོའི་རྣལ་འབྱོར་བསྒོམ་པར་བྱའོ། །

[Block 4589]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་ལྷ་རྣམས་ཀྱི་འཁོར་ལོ་ཞེས་སྨོས་ཏེ། ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི༌[^2771]འཁོར་ལོའི་ཕྱག་མཚན་ལས་བྱུང་བའི་རྣམ་པར་སྣང་མཛད་ཀྱི་སྤྲུལ་པའི་ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་བདག་ཉིད་ཀྱི་འཁོར་ལོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4590]
རིགས་དང་དེར་འབྲེལ་པའི་ལྷ་རྣམས་ཏེ་ཞེས་པ་ནི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་རིགས་ཀྱི་འབྲེལ་པ་དང་ལྡན་པའི་ལྷ་རྣམས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4591]
དེ་ཉིད་གནས་ཇི་ལྟ་བ་བཞིན་དུ་ཡང་དག་པར་གནས་པས་ན་ཞེས་པ་ལ་ཤར་ཕྱོགས་ལ་སོགས་པའི་གནས་ལ་ཉེ་བར་བཀོད་པས་སོ། །

[Block 4592]
རང་གི་བདག་པོའི་སྐུ་མདོག་དང་འདྲ་བའོ་ཞེས་པ་ནི་དབུས་ཀྱི་གཙོ་བོ་ལ་ལྟོས་པས་དབུས་ཀྱི་སའི་ཆ་ནི་བདག་པོ་དང་མཚུངས་པ་ཞེས་པའི་དོན་ཏོ། །

[Block 4593]
དེ་ལྟར་རྣམ་པར་སྣང་མཛད་ཀྱི་དཀྱིལ་འཁོར་གྱི་དབུས་ཀྱི་སའི་ཆ་ནི་དཀར་པོའོ། །

[Block 4594]
ཤར་དང་ལྷོ་དང་ནུབ་དང་བྱང་གི་སའི་ཆ་རྣམས་ནི་ནག་པོ་དང་སེར་པོ་དང་། དམར་པོ་དང་ལྗང་གུའོ། །

[Block 4595]
དེ་བཞིན་དུ་མི་བསྐྱོད་པའི་དཀྱིལ་འཁོར་གྱི་དབུས་ཀྱི་སའི་ཆ་ནི་ཁ་དོག་ནག་པོ་དང་ཤར་ལ་སོགས་པ་དཀར་པོ་དང་སེར་པོ་དང་། དམར་པོ་དང་ལྗང་གུའོ། །

[Block 4596]
རིན་ཆེན་འབྱུང་ལྡན་གྱི་དཀྱིལ་འཁོར་གྱི་དབུས་ཀྱི་སའི་ཆ་ནི་སེར་པོ་དང་། ཤར་ལ་སོགས་པ་དཀར་པོ་དང་ནག་པོ་དང་། དམར་པོ་དང་། ལྗང་གུའོ། །

[Block 4597]
སྣང་བ་མཐའ་ཡས་ཀྱི་དཀྱིལ་འཁོར་གྱི་དབུས་ཀྱི་སའི་ཆ་ནི་དམར་པོ་དང་ཤར་ལ་སོགས་པ༌[^2772]སྔ་མ་བཞིན་ནོ། །

[Block 4598]
འོན་ཀྱང་ནུབ་ནི་ནག་པོའོ། །

[Block 4599]
དོན་ཡོད་གྲུབ་པའི་དཀྱིལ་འཁོར་གྱི་སའི་ཆ་ནི་ལྗང་གུ་དང་། ཤར་ལ་སོགས་པ་སྔ་མ་བཞིན་ནོ། །

[Block 4600]
འོན་ཀྱང་བྱང་ནི་ནག་པོའོ། །

[Block 4601]
དེ་ལྟར་སངས་རྒྱས་སྤྱན་མ་ནས་བརྩམས་ཏེ་གནོད་མཛེས་ཀྱི་རྒྱལ་པོའི་བར་དུ་ལྷ་སུམ་ཅུ་རྩ༌[^2773]གཉིས་ཀྱི་བདག་ཉིད་ཅན་གྱི་དཀྱིལ་འཁོར་སུམ་ཅུ་རྩ་གཉིས་སུ་ཤེས་པར་བྱའོ། །

[Block 4602]
དེ་རྣམས་མདོར་བསྡུས་ན་སྟོང་ཕྲག་གཅིག་དང་ཉི་ཤུ་རྩ་བཞིའི་ལྷ་རྣམས་སུ་འགྱུར་རོ། །

[Block 4603]
དེ་རྣམས་བདག་པོ་ལ་ལྟོས་ཏེ་གནས་ཇི་ལྟ་བ་བཞིན་དུ་དགོད་པར་བྱའོ། །

[Block 4604]
ཁ་དོག་སྣ་ལྔའི་སའི་ཆ་དང་ལྡན་པའོ༌[^2774]ཞེས་པ་ལ། བདག་པོ་ལ་ལྟོས་ཏེ་ཤར་ལ་སོགས་པའི་ཕྱོགས་སུ༌[^2775]ཁ་དོག་ལྔ་དང་ལྡན་པའོ། །

[Block 4605]
ཐམས་ཅད་དུ་བཟང་པོའི༌[^2776]ཞེས་པ་ནི་ནང་གི་དཀྱིལ་འཁོར་གྱི་ཁྱད་པར་རོ། །

[Block 4606]
ཕྱིའི་དཀྱིལ་འཁོར་ནི་གྲུ་བཞི་པ་ཉིད་དོ། །

[Block 4607]
གཟུགས་རྡོ་རྗེ་ལ་སོགས་པ་དང་ལྡན་པའོ་ཞེས་པ་ནི་ལྷའི་སྣམ་བུ་དང་དྲ་བ་ཕྱེད་པ་དང་རིན་པོ་ཆེའི༌[^2777]ཕ་གུ་དང་པཉྩ་རཱ་ག་ལ་སོགས་པ་དང་ལྡན་པའོ། །

[Block 4608]
ལྷ་ལ་སོགས་པ་ཉེ་བར་བསྟན་པའི་མཆོད་པ་རྣམ་པ་ལྔ་དང་བཅས་པའོ་ཞེས་པ་ལ། ཤིན་ཏུ་དད་པ་ལས་འོངས་པའི་བརྒྱ་བྱིན་ལ་སོགས་པའི་ལྷའི་ཚོགས་ཀྱི་ལག་པས་འབུལ་བ་རྣམ་པ་སྣ་ཚོགས་པའི་མཆོད་པ་དང་བཅས་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4609]
མདོར་ན་ཞེས་པ་ནི་སྔར་བཤད་པའི་བསྐྱེད་པའི་རིམ་པས་སོ། །

[Block 4610]
ལྷའི་འཁོར་ལོ་འདི་ལྟར་བསམ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་གྱི་སྒོ་ནས་བསྐྱེད་པའི་དེ་བཞིན་གཤེགས་པ་ལ་སོགས་པའི་ལྷའི་འཁོར་ལོ་བསྒོམ་པར་བྱའོ། །

[Block 4611]
བདག་ཉིད་ནི་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོ་ལས་ལོགས༌[^2778]སུ་བདག་ཉིད་ཀྱང་ཐ་དད་པར་བསྒོམ་པར་མི་བྱའི། འོན་ཀྱང་དཀྱིལ་འཁོར་གྱི་བདག་པོའི་རང་བཞིན་དུ་བཞུགས་པར་བདག་ཉིད་བསམ་པར་བྱ༌[^2779]བའི་དོན་ཏོ། །

[Block 4612]
འཁོར་ལོའི་དཀྱིལ་དུ་ཞེས་པ་ལ་ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་ལྷའི་འཁོར་ལོའི་དབུས་སུའོ། །

[Block 4613]
བདག་པོར་གྱུར་པ་ཉིད་ཀྱིས་གཞག༌[^2780]གོ་ཞེས་པ་ནི་རྣལ་འབྱོར་བཞིས་བདག་ཉིད་ཀྱི་དང་པོ་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4614]
སྐད་ཀྱི་བྱིངས༌[^2781]བརྗོད་པ་ནི་དོན་དུ་མ་ཡིན་པས་བསྒོམ་པའི་སྒྲ་ནི་གཞག་པའི༌[^2782]དོན་ལ་འཇུག་གོ། །

[Block 4615]
དེ་ནས་ཞེས་བྱ་བ་ལ་སོགས་པས་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་རྗེས་སུ་འཇུག་པས་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་ཕྱག་རྒྱ་ཆེན་པོ་བསྒོམ་པ་བསྟན་ཏོ། །

[Block 4616]
གང་གི་ཕྱིར་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོ་ནི། ཤེས་པ་དང་ཤེས་བྱ༌[^2783]ཉེ་བར་བསྡུས་པའི་ངོ་བོ་ཆོས་ཐམས་ཅད་ཀྱི་ཆོས་ཉིད་ཀྱི་རང་བཞིན་ནོ། །

[Block 4617]
དེ་བས་ན་དེས་བྱིན་གྱིས་བརླབས་པའི་དེ་བཞིན་གཤེགས་པའི་སྐུ་རྣམས་ཀྱིས་བསོད་ནམས་ཀྱི་ཚོགས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་སྟེར་བར་འགྱུར་རོ། །

[Block 4618]
གཞན་དུ་ན་བརྟག་པར༌[^2784]བྱ་བ་ཙམ་དེ་རྣམས་ཀྱི་འབྲས་བུ་གང་ཡང་སྟེར་བར་མི་འགྱུར་རོ། །

[Block 4619]
དེ་ལ་རྗེས་སུ་ཞུགས་པའི་ལྷའི་སྐུ་བརྟགས་པ་ཡང་ཡོངས་སུ་དག་པའི་སྐུར་འགྱུར་རོ། །

[Block 4620]
དེ་ཉིད་ཀྱི་ཕྱིར་ལེའུ་བཅུ་གསུམ་པ་ལས་ཀྱང་། །

[Block 4621 [VERSE]]
རྡོ་རྗེ་སེམས་དཔའ་རྒྱལ་པོ་ཆེ། །
ཡང་དང་ཡང་དུ་བསྐུལ་བར་བྱ། །
དེ་ནི་སྔགས་རྣམས་ཐམས་ཅད་ཀྱི། །
རྒྱལ་པོ་རྟག་པ་མཆོག་ཡིན་ནོ། །

[Block 4622]
ཞེས་འབྱུང་ངོ་། །

[Block 4623 [VERSE]]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་། །
དེ་ནི་རང་བྱུང་བཅོམ་ལྡན་འདས། །
གཅིག་པུའི་བདག་ཉིད་ཆེ་བའི་ལྷ། །
མན་ངག་རྣམས་ནི་རབ་སྟེར་བས། །

[Block 4624]
རྡོ་རྗེ་སློབ་དཔོན་དེ་བས་ལྷག །ཅེས་འབྱུང་ངོ་། །

[Block 4625]
རྡོ་རྗེ་འཆང་གི་སྤྲུལ་པ་ཡི། །ཞེས་པ་ནི། རྡོ་རྗེ་འཆང་ཆེན་པོས་བསྐྱེད་ཅིང་། དེ་ལ་རྗེས་སུ་ཞུགས་ཏེ་དེའི་རྣམ་པ་ཉིད་དུ་འགྱུར་བའོ། །
--- END BLOCKS ---
