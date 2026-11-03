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
[Block 386]
ངོ་བོ་ཉིད་ཀྱིས་མྱོང་བར་འགྱུར་བ་ནི་ཚོར་བ་རྣམས་སོ། །

[Block 387]
མཚུངས་པར་ལྡན་པས་མྱོང་བར་འགྱུར་བ་ནི་རེག་པ་སྟེ། བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པ་ཞེས་བྱ་བའོ། །

[Block 388]
དམིགས་པ་མྱོང་བར་འགྱུར་བ་ནི་ཡུལ་རྣམས་ཏེ། ཇི་སྐད་དུ། མིག༌[^277]གིས་གཟུགས་རྣམས་མཐོང་ནས་གཟུགས་སོ་སོར་ཡང་དག་པར་མྱོང་བར་འགྱུར་གྱི་གཟུགས་ལ་འདོད་ཆགས་སོ་སོར་ཡང་དག་པར་མྱོང་བ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་གསུངས་པ་སྟེ། དམིགས་པ་ན༌[^278]ཚོར་བས་དེ་དག་སོ་སོར་ཡང་དག་པར་མྱོང་བར་བྱེད་དོ། །

[Block 389]
རྣམ་པར་སྨིན་པ་མྱོང་བར་འགྱུར་བ་ནི་ལས་ཡིན་ཏེ། མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཞེས་བྱ་བ་རྒྱས་པར་འབྱུང༌[^279]བའོ། །

[Block 390]
མངོན་སུམ་དུ་གྱུར་པ་མྱོང་བར་འགྱུར་བ་ནི་ཇི་སྐད་དུ། གང་གི་ཚེ་བདེ་བའི་ཚོར་བ་མྱོང་བར་བྱེད་པ་དེའི་ཚེ༌[^280]ཚོར་བ་གཉིས་འགག་པར་འགྱུར་རོ༌[^281]ཞེས་གསུངས་པ་སྟེ། གང་གི༌[^282]ཚེ་བདེ་བའི་ཚོར་བ་འཇུག་པ་དེའི་ཚེ་གང་གིས་ན་དེ་མྱོང་བར་འགྱུར་བ༌[^283]གཞན་ནི་མེད་ཀྱི་དེས་མངོན་སུམ་དུ་བྱེད་ན་ནི་དེ་མྱོང་བར་འགྱུར་ཞེས་བྱ་སྟེ། དེའི་ཕྱིར་རྣམ་པར་སྨིན་པ་མྱོང་བར་འགྱུར་བ་ཡིན་པའི་ཕྱིར་ལས་ཀྱང་བདེ་བ་མྱོང་བར་འགྱུར་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^284]བརྗོད་དོ། །

[Block 391 [HEADING]]
### ངེས་པ་དང་མ་ངེས་པའི་ལས། ^1-26-0

[Block 392]
དེ་ཡང་ངེས་དང་མ་ངེས་པ། །བདེ་བ་མྱོང་བར་འགྱུར་བ་ལ་སོགས་པའི་ལས་རྣམ་པ་གསུམ་པོ་དེ་ཡང་ངེས་པ་དང་། མ་ངེས་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། གདོན་མི་ཟ་བར་མྱོང་བར་འགྱུར་བ་ནི་མ་ཡིན་ནོ། །

[Block 393 [VERSE]]
མཐོང་བའི་ཆོས་ལ་སོགས་པ་ལ། །
མྱོང་འགྱུར་ཕྱིར་ན་ངེས་རྣམ༌[^285]གསུམ། །

[Block 394]
མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བ་དང་། སྐྱེས་ནས་མྱོང་བར་འགྱུར་བ་དང་། ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བ་སྟེ། ལས་རྣམ་པ༌[^286]འདི་གསུམ་ནི་ངེས་པའོ། །

[Block 395]
དེ་ལྟར་ན་དེ་ནི་མྱོང་བར་འགྱུར་བ་མ་ངེས་པ་དང་བཅས་པ་སྟེ་ལས་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 396]
ཁ་ཅིག་ལས་རྣམ་པ༌[^287]ལྔ་ཞེས་ཟེར། [^288]གཞན་དག་ནི་མྱོང་བར་འགྱུར་བར་མ་ངེས་པ་ལ་རྣམ་པར་སྨིན་པར༌[^289]ངེས་པ་དང་མ་ངེས་པ་རྣམ་པ་གཉིས་སུ་ཕྱེ་ནས་ལས་རྣམ་པ་ལྔར་ཡོད༌[^290]དོ། །

[Block 397]
དེ་ལ་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བ་ནི་སྐྱེ་བ་གང་དུ་བྱས་པ་དེ་ཉིད་དུ་རྣམ་པར་སྨིན་པར་འགྱུར་བའོ། །

[Block 398]
སྐྱེས་ནས༌[^291]མྱོང་བར་འགྱུར་བ་ནི་སྐྱེ་བ་གཉིས་པ་ལའོ།[^292] །ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བ་ནི་དེ་ཕན་ཆད་དུའོ། །

[Block 399]
གཞན་དག་ན་རེ་ཆེས༌[^293]སྟོབས་དང་ལྡན་པའི་ལས་གང་ཡིན་པ་དེའི་རྣམ་པར་སྨིན་པ་ཆུང་ཆེས་པར་འགྱུར་དུ་འོང་བས་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཚེ་རབས་གཞན་དག་ན་ཡང་ཡོད་མོད་ཀྱི་རྩོམ་པའི་དབང་གིས་མིང་དེ་རྣམ་པར་གཞག་གོ་ཞེས་ཟེར་རོ། །

[Block 400]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ནི་དེ་མི་འདོད་དོ། །

[Block 401]
འབྲས་བུ་ཉེ་ལ་འབྲས་བུ་རིང་བ་མ་ཡིན་པའི་ལས་ཀྱང་ཡོད། བཟློག་པ་ཡང་ཡོད་དེ་ཕྱིའི་ས་བོན་བཞིན་ནོ། །

[Block 402]
ཇི་ལྟར་ལྕམ་པ་ལ་སོགས་པ་ནི་ཟླ་བ་ཕྱེད་དང་གཉིས་ཀྱིས་འབྲས་བུ་སྨིན་ལ། ནས་དང་གྲོ་ལ་སོགས་པ་ནི་ཟླ་བ་དྲུག་གིས་འབྲས་བུ་སྨིན་པ་བཞིན་ནོ། །

[Block 403]
གཞན་དག་མུ་ནི་བཞི་ཞེས་ཟེར། །དཔེས་སྟོན་པ་རྣམས་ནི་གནས་སྐབས་ངེས༌[^294]ལ༌[^295]རྣམ་པར་སྨིན་པར་མ་ངེས་པ་ཡང་ཡོད་དེ། མཐོང་བའི་ཆོས་ལ་སོགས་པ་ལ་མྱོང་བར་འགྱུར་ལ་རྣམ་པར་སྨིན་པ་ནི་མ་ངེས་པའི་ལས་གང་ཡིན་པའོ། །

[Block 404]
རྣམ་པར་སྨིན་པར་ངེས་ལ་གནས་སྐབས་དག་ཏུ་མ་ཡིན་པ་ཡང་ཡོད་དོ། །

[Block 405]
[^296]རྣམ་པར་སྨིན་པ་ནི༌[^297]ངེས་ལ་མྱོང་བར་འགྱུར་བ༌[^298]ནི་མ་ངེས་པའི་ལས་གང་ཡིན་པའོ། །

[Block 406]
གཉི་ག་ངེས་པ་ཡང་ཡོད་དེ། མཐོང་བའི་ཆོས་ལ་སོགས་པ་ལ་མྱོང་བར་འགྱུར་ལ་རྣམ་པར་སྨིན་པར་ཡང་ངེས་པའི་ལས་གང་ཡིན་པའོ། །

[Block 407]
གཉི་ག་མ་ངེས་པ་ཡང་ཡོད་དེ། མྱོང་བར་འགྱུར་བ་ཡང་མ་ངེས་ལ་རྣམ་པར་སྨིན་པར་ཡང་མ་ངེས་པའི་ལས་གང་ཡིན་པའོ་ཞེས་བྱ་བ་མུ་བཞིར་བྱེད་དེ་དེ་དག་གི་ལྟར་ན་ལས་རྣམ་པ་བརྒྱད་དེ། མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བར་ངེས་པ་དང་། མ་ངེས་པ་ནི༌[^299]མྱོང་བར་འགྱུར་བར་མ་ངེས་པའི་བར་དུ་ཡང་དེ་དང་འདྲའོ། །

[Block 408]
མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བ་ལ་སོགས་པ་ནི་ངེས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 409]
བཞི་པ་ནི་མ་ངེས་པ་ཡིན་ནོ་ཞེས་བརྗོད་དོ། །

[Block 410]
སྐད་ཅིག་མ་གཅིག་ལ་ལས་རྣམ་པ་བཞི་འཕེན་པར་འགྱུར་བ་ལྟ་ཡོད་དམ་ཞེ་ན། ཡོད་དེ། ཕ་རོལ་པོ་གསུམ་ལ་སྦྱར་ནས་བདག་ཉིད་འདོད་པས་ལོག་པར་གཡེམ་པ་ལ་ཞུགས་ཏེ། དེ་དག་ཅིག་ཅར་མཐར་ཕྱིན་པར་འགྱུར༌[^300]ནའོ། །

[Block 411 [HEADING]]
### ལས་ཀྱི་འཕེན་པ། ^1-27-0

[Block 412]
ལས་བཞི་པོ་དེ་དག་ལས།

[Block 413]
གསུམ་གྱིས་རིས་ནི་འཕེན་པར་བྱེད། །མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཀྱིས་ནི་རིས་མཐུན་པ་འཕེན་པར་མི་བྱེད་དོ། །

[Block 414]
ཁམས་གང་ངམ། འགྲོ་བ་གང་ན༌[^301]ལས་ཀྱི་འཕེན་པ་རྣམ་པ་དུ་ཞིག་ཡོད་ཅེ་ན། ཐམས་ཅད་ན་ནི་འཕེན་པ་བཞི། །ཁམས་གསུམ་པོ་ཐམས་ཅད་དང་། འགྲོ་བ་ཐམས་ཅད་ན་དགེ་བ་དང་མི་དགེ་བ་རྣམས་ཅི་རིགས་པར་ལས་བཞིའི་འཕེན་པ་ཡོད་དེ། སྤྱིར་བསྟན་པ་འདིའི་དམིགས་ཀྱིས་བསྟན་པ་ནི་འདི་ཡིན་ཏེ། དམྱལ་བ་ན་ནི་དགེ་བའི་གསུམ། །དམྱལ་བ་དག་ན་ནི་ལས་དགེ་བ་རྣམ་པ་གསུམ་གྱིས་འཕེན་པ་ཡོད་ཀྱི་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བ་ནི་མེད་དེ། དེ་ན་རྣམ་པར་སྨིན་པ་ཡིད་དུ་འོང་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 415 [VERSE]]
གང་ལས་འདོད་ཆགས་བྲལ་བརྟན་པའི། །
བྱིས་པ་དེར་སྐྱེས་མྱོང་མི་བྱེད། །

[Block 416]
སོ་སོའི་སྐྱེ་བོ་ཡིན་པ༌[^302]དེ་ཡང་བརྟན་པ་ཡིན་ཏེ། ཡོངས་སུ་མི་ཉམས་པའི་ཆོས་ཅན་ཞིག་ན་དེ་ནི་ས་གང་ལས་འདོད་ཆགས་དང་བྲལ་བ་དེར་སྐྱེས་ནས་མྱོང་བར་འགྱུར་བའི་ལས་མི་བྱེད་དོ། །

[Block 417 [VERSE]]
གཞན་དག༌[^303]རྣམ་པ་གསུམ་ནི་བྱེད་དོ། །
འཕགས་པ་གཞན་དུའང་མྱོང་མི་བྱེད། །

[Block 418]
བརྟན་པ་ཞེས་བྱ་བར་སྦྱར་ཏེ། འཕགས་པའི་གང་ཟག་ཡིན་ལ་ཡོངས་སུ་མི་ཉམས་པའི་ཆོས་ཅན་ཡང་ཡིན་ན་ས་གང་ལས་འདོད་ཆགས་དང་བྲལ་བ་དེར་སྐྱེས་ནས་མྱོང་བར་འགྱུར་བ་དང་། ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཀྱང་མི་བྱེད་དེ། འདི་ན༌[^304]ཡང་ས་འོག་མར་འོང་བར༌[^305]རུང་བ་མ་ཡིན་ནོ། །

[Block 419]
གང་དུ་སྐྱེས་པར་མ་ངེས་པ་དང་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བ་ནི་བྱེད་དོ། །

[Block 420]
འདོད་རྩེའི་མི་བརྟན་པ་ཡང་མིན། །འདོད་པའི་ཁམས་སམ། སྲིད་པའི་རྩེ་མོ་ལས་འདོད་ཆགས་དང་བྲལ་བའི་འཕགས་པའི་གང་ཟག་དེ་དག་ཏུ་ཡོངས་སུ་ཉམས་པའི་ཆོས་ཅན་ཡིན་ཡང་སྐྱེས་ནས་མྱོང་བར་འགྱུར་བ་དང་། ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བའི་ལས་བྱེད་པར་རུང་བ་ནི༌[^306]མ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་འབྲས་བུ་ལས་ཡོངས་སུ་ཉམས་པ་ལས་ནི་འཆི་བ་མེད་དོ་ཞེས་འོག་ནས་བཤད་པར་བྱའོ། །

[Block 421 [HEADING]]
### སྲིད་པ་བར་མ་ན་ལས་ཀྱི་འཕེན་པ། ^1-28-0

[Block 422]
ཅི་སྲིད་པ་བར་མ་ན་ཡང་ལས་ཀྱི་འཕེན་པ་ཡོད་དམ་ཞེ་ན་སྨྲས་པ། ཡོད་དེ།

[Block 423 [VERSE]]
སྲིད་པ་བར་མ་འདོད་ཁམས་སུ། །
འཕེན་པ་རྣམ་པ་ཉི་ཤུ་གཉིས། །

[Block 424]
འདོད་པ་ན་སྤྱོད་པའི་སྲིད་པ་བར་མ་ནི་ལས་རྣམ་པ་ཉི་ཤུ་རྩ་གཉིས་འཕེན་ཏེ། ཇི་ལྟར་བྱས་པས་ཤེ་ན། མངལ་གྱི་གནས་སྐབས་ལྔ་སྟེ། ནུར་ནུར་པོ་དང་། མེར་མེར་པོ་དང་། ནར་ནར་པོ་དང་། གོར་གོར་པོ་དང་། རྐང་ལག་འགྱུས་པའི་གནས་སྐབས་རྣམས་སོ། །

[Block 425]
སྐྱེས་པའི་གནས་སྐབས་རྣམ་པ༌[^307]ལྔ་སྟེ། བྱིས་པ་དང་། གཞོན་ནུ་དང་། དར་ལ་བབ་པ་དང་། དར་ཡོལ་བ་དང་། རྒན་པོའི༌[^308]གནས་སྐབས་རྣམས་སོ། །
--- END BLOCKS ---
