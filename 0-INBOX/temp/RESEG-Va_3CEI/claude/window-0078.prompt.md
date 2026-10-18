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
[Block 2731]
མདོ་ལས་འོད་སྲུངས་དེ་བཞིན་གཤེགས་པས༌[^2333]ཆོས་ཐམས་ཅད་རིག་པར་འཇོག་སྟེ་ཞེས་པ་ནས་དེ་ལྟར་འཇོག་གོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་བཤད་པས་ཕན་འདོགས་པ་སྟེ། དེ་བཞིན་གཤེགས་པ་ཐུགས་རྗེ་ཆེན་པོ་དང་། ཐབས་མཁས་པ་དང་ལྡན་པས་མཚན་མ་དང་བྲལ་བའི་ཆོས་སྟོན་པས་འགྲོ་བ་སྨིན་པར་བྱེད་དེ། ལུང་ནི་རིགས་པ་ཅན་རིག་པའི༌[^2334]གཞུང་བསྒྲུབས་པས༌[^2335]འབྲས་བུ་ཐོབ་པར་བྱེད་པ་ཉིད་ཡེ་ཤེས་ཀྱི་ས་ལ་འཇོག་པའོ། །

[Block 2732 [HEADING]]
###### ཆོས་ཀྱི་དོན་རྟོགས་པ་མི་མཐུན་པ། ^4-5-4-1-3-0

[Block 2733]
མདོ་ལས་ཆོས་ཐམས་ཅད་ཀྱི་དོན་གྱི་རིམ་པ་ལ་ཞེས་པ་ནས་དམ་པའི་མཆོག་ཐོབ་སྟེ་ཞེས་པའི་བར་དུ་ནི་ཆོས་སྟོན་པའི་རིམ་པ༌[^2336]གསུམ་དུ་མི་མཐུན་པའི་ཕྱིར་སེམས་ཅན་རྣམས་ནི་ཡོད་པ་དང་མེད་པར་ལྟ་བ་གཉིས་ལས་མི་འདའ་བ་དང་། ཡང་དག་པའི་དོན་གྱི་མཐའ་དང་། སེམས་ཅན་རྣམས་ཀྱི་སེམས་ཀྱི་སྤྱོད་པ་མི་མཐུན་པས་སྐྱེད་པ་སྟེ། མདོ་ལས་ཀྱང་ཡོད་པ་དང་མེད་པའི་ཕྱོགས་ལ་འཛུད་ཅིང་མོས་པ་དང་མཚན་ཉིད་གསུམ་གྱིས༌[^2337]ཡང་དག་པའི་མཐའ་ལ་འཇུག་པའོ་ཞེས་འབྱུང་སྟེ། སྤྱོད་པ་ཐམས་ཅད་དང་མཐུན་པར་འཇུག་པ་ལ་མཁས་པས་མཁྱེན་པ་ཐོགས་པ་མེད་པའི་ཕྱིར་སེམས་ཅན་གྱི་སེམས་ཀྱི་རིམ་པ་བཞིན་དུ་ཆོས་སྟོན་པའོ། །

[Block 2734 [HEADING]]
###### བདག་ཉིད་ཀྱིས་རིག་པར་དཀའ་བ། ^4-5-4-1-4-0

[Block 2735]
མདོ་ལས་འོད་སྲུངས་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར༌[^2338]ཞེས་པ་ནས་ཡེ་ཤེས་ལ་མངོན་པར་འཇོག་གོ་ཞེས་པའི་བར་དུ་ནི་སེམས་ཅན་རྣམས་ཀྱི་དེ་བཞིན་ཉིད་ཡང་དག་པ༌[^2339]ཇི་ལྟ་བ་བཞིན་རང་གིས་མི་ཤེས་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་གདོན་མི་ཟ་བའི་མཐའ་མཁྱེན་པ་སེམས་ཅན་གྱི་དབང་པོའི་རིམ་པ་མཁྱེན་པས་སེམས་ཅན་རྣམས་ལ་དེ་བཞིན་གཤེགས་པ༌[^2340]ཡེ་ཤེས་བསྟན་ཏེ། མ་བསྟན་པར་ནི་བདག་དང་གཞན་གྱི་མཚན་ཉིད་མི་ཤེས་པའོ། །

[Block 2736]
ཡང་ཆོས་སྟོན་པ་ནི༌[^2341]སྔ་ཕྱིའི་མཚན་ཉིད་སྟོན་པ་ལ་མངའ་བརྙེས་པའི་ཕྱིར་སྟོན་པ་དང་། ཡང་ན་ཐབས་མཁས་པའི་ཡེ་ཤེས་ཀྱིས༌[^2342]སོ་སོའི་མཚན་ཉིད་སྟོན་པའོ། །

[Block 2737]
དེ་ལ་ཡང་རྣམ་པ་བཞི་སྟེ། བྱང་ཆུབ་དང་མྱ་ངན་ལས་འདའ་བའི་མཚན་ཉིད་འབྱེད་པ་ལ་མཁས་པ་ཐབས་མཁས་པའི་ཡེ་ཤེས་ཀྱིས༌[^2343]སེམས་ཅན་རྣམས་ཀྱི་སྤྱོད་པ་འབྱེད་པ་ལ་མཁས་པ་དང་། དེ་བཞིན་ཉིད་ཀྱི་མཚན་ཉིད་སེམས་ཅན་རྣམས་ལ་སྟོན་པར་མཁས་པ་དང་། བྱང་ཆུབ་ཀྱི་ཡེ་ཤེས་དང་འབྲས་བུ་སེམས་ཅན་རྣམས་ཀྱིས་རྟོགས༌[^2344]པར་བྱེད་པ་ལ་ཐོགས་པ་མེད་པར་འཛུད་པ་དང་། བདག་ཉིད་སྔོན་དེ་འདྲ་བའི་སྤྱོད་པ་ལ་ཞུགས་པའི་ཕྱིར་གཞན་ཡང་ཡེ་ཤེས་དེ་ལ་འཇོག་པའོ། །

[Block 2738]
ཡང་དེ་དབྱེ་བ་ལ་རྣམ་པ་བཞི་སྟེ། ཆོས་རྣམས་ཀྱི་བདེན་པ་ཉིད་ལ་ཐུག་པ་དང་། ཡོད་པ་དང་མེད་པ་ལ་མཁས་པ་དང་། ཡེ་ཤེས་སྐྱེ་བ་ལ་སེམས་དགའ་བ་དང་། བཀྲི་བ་དང་ངེས་པའི་དོན་སྟོན་པ་ལ་མཁས་པའོ། །

[Block 2739]
ཡང་ཐབས་མཁས་པའི་ཡེ་ཤེས་ནི་བདེན་པ་ཉིད་ནི་ཐ་སྙད་དང་བྲལ་བ་ན་ཚིག་གིས༌[^2345]མཚོན་ཅིང་སྟོན་པ་ནི་ཐབས་མཁས་པའི་ཡེ་ཤེས་སོ། །

[Block 2740]
ཡེ་ཤེས་ཀྱི་ས་ཞེས་པ་ནི་བརྟེན་པའི་དོན་ཏེ། སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་གཟིགས་པའི་གནས་ནི་ཡང་དག་པའི་མཐའོ། །

[Block 2741]
ཡང་ན་ལུང་ནི་རིགས་པ༌[^2346]ལ་གཞོལ་བ། རིགས་པ་ནི་སྤྱོད་པ་དང་མཐུན་པ། སྤྱོད་པ་ནི་འབྲས་བུ་དང་འབྲེལ་པ་དེ་སངས་རྒྱས་ཀྱི་ས་ཞེས་བརྗོད་དོ། །

[Block 2742]
དེ་བཞིན་གཤེགས་པས་གཟིགས་ཏེ་ཞེས་པ་ནི་ཡོད་པ་དང་མེད་པའི་ཆོས་རྣམས་གཟིགས་ཏེ། ཆོས་རྣམས་ནི་ཀུན་བརྟགས་པ་དང་། གཞན་གྱི་དབང་དང་། ཡོངས་སུ་གྲུབ་པའི་མཚན་ཉིད་དེ་གསུམ་མོ། །

[Block 2743]
སེམས་ཅན་རྣམས་ཀྱི་ལྷག་པའི་བསམ་པ་མཁྱེན་པ་ནི་སེམས་ཅན་རྣམས་ཀྱི་སྤྱོད་པ་དང་། དེའི་ལྷག་པའི་མོས་པ་དང་འཇུག་པ་ཐོགས་པ་མེད་པར་མཁྱེན་པའོ། །

[Block 2744]
ཆོས་རྣམས་ཀྱི་མཚན་ཉིད་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་གཟིགས་པ་དེ་སེམས་ཅན་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་སྟོན༌[^2347]པའོ། །

[Block 2745]
དེ་འདྲ་བར་སྟོན་པ་ཉིད་གདོན་མི་ཟ་བའི་ཡེ་ཤེས་ཏེ། དེ་འདྲ་བའི་བརྙེས་པས་སེམས་ཅན་རྣམས༌[^2348]ལ་ཆོས་གཅིག་སྟོན་པས་དབང་པོ་མི་མཐུན་པ་ཐེག་པ་རྣམ་ལྔར་གྱུར་པ་རྣམས་གཅིག་སྟེ། གཉིས་དང་གསུམ་དུ་མེད་དོ། །

[Block 2746 [HEADING]]
##### དཔེ། ^4-5-4-2-0

[Block 2747 [HEADING]]
###### སྤྱིའི་དཔེ། ^4-5-4-2-1-0

[Block 2748]
མདོ་ལས་འོད་སྲུངས་འདི་ལྟ་སྟེ་དཔེར་ན་ཞེས་པ་ནས་ཇི་སྙེད་སྐྱེས་པ་ཞེས་པའི་བར་དུ་ནི། དཔེ་དེ་དག་ལ་ཡང་རྣམ་པ་གཉིས་སུ་དབྱེ་སྟེ། སྤྱིའི་དཔེ་དང་། སོ་སོའི་དཔེའོ། །

[Block 2749]
འདི་ནི་དང་པོ་སྟེ། རི་དང་ས་ཞེས་པ་ས་ཡན་ཆད་ནི་བསྐྱེད་པར་བྱའོ། །

[Block 2750]
སྟོང་གསུམ་གྱི་སྟོང་ཆེན་པོ་ཞེས་པ་ནི་བསྐྱེད་པའི་གཞིའོ།[^2349] །ཤིང་རྩི་དེ་དག་ཀྱང་འཇིག་རྟེན་དང་། འཇིག་རྟེན་ལས་འདས་པའི་དགེ་བའི་ཆོས་རྣམས་ཀྱི་ས་བོན་གྱི་དཔེ་སྟེ། སྨན་དང་ནགས་ཞེས་པ་ཐེག་པ་རྣམ་ལྔའི་ས་བོན་སོ་སོ་མི་མཐུན་པར་གྱུར་པའི་དཔེའོ། །

[Block 2751 [HEADING]]
###### སོ་སོའི་དཔེ། ^4-5-4-2-2-0

[Block 2752]
མདོ་ལས་སྤྲིན་ཆུ་ཆེན་པོ་རྒྱས་པ་ལངས་ཞེས་པ་ནས། སྟོང་ཆེན་པོའི་འཇིག་རྟེན་གྱི་ཁམས་ཞེས་པའི་བར་དུ་ནི་དཔེ་དེ་དག་རྣམ་པ་བཞིར་དབྱེ་སྟེ་ཆོས་ཀྱི་རྒྱལ་པོ་འཇིག་རྟེན་དུ་བྱུང་བའི་དཔེ་དང་བསྟན་པས་ཕྱོགས་སུ་བརླན་པའི་དཔེ་དང་འབྲས་བུ་མི་མཐུན་པར༌[^2350]སྨིན་པའི་དཔེ་དང་དེ་ལྟར་བརླན་པར་མི་སེམས་པའི་དཔེ་དང་བཞིའོ། །

[Block 2753 [HEADING]]
###### **ཆོས་ཀྱི་རྒྱལ་པོ་འཇིག་རྟེན་དུ་བྱུང་བའི་དཔེ།** ^4-5-4-2-2-1-0

[Block 2754]
སྤྲིན་རྒྱས་པར་ལངས་ཞེས་པ་ནི་དཔེ་དང་པོ་དང་སྦྱར།

[Block 2755 [HEADING]]
###### **བསྟན་པས་ཕྱོགས་སུ་བརླན་པའི་དཔེ།** ^4-5-4-2-2-2-0

[Block 2756]
དེའི་འོག་མ་ནི་གཉིས་པ་དང་སྦྱར་ཏེ། སྤྲུལ་པའི་སྐུས་ཕན་པའི་དོན་མང་པོ་ལ་ཁྱབ་པར་ཁེབས་པ་ནི་སྤྲིན་གྱི་དོན་ཏོ། །

[Block 2757]
སྤྲིན་དེ་ཡང་ཡོན་ཏན་བཅུ་དང་ལྡན་པ་ནི་ཚིགས་སུ་བཅད་པའི་ནང་ནས་སྟོན་ཏོ། །

[Block 2758]
སྤྲུལ་པའི་སྐུ་གཅིག་གིས་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་དུ་སྨོན་ཅིང་ཁྱབ་པར་སྣང་བས་ཁེབས་ཞེས་པའི་དོན་ཏོ། །

[Block 2759]
དུས་གཅིག་ཏུ་ཆར་མཉམ་པར་ཕབ་ཞེས༌[^2351]པས་ནི་འབྲས་བུ་སོ་སོར་སྨིན་ཞེས་པའི་དོན་དང་གསུང་གཅིག་གིས་ཆོས་སྟོན་པའི་དོན་ཏོ། །

[Block 2760 [HEADING]]
###### **འབྲས་བུ་མི་མཐུན་པར་སྨིན་པའི་དཔེ།** ^4-5-4-2-2-3-0

[Block 2761]
མདོ་ལས་འདིའི་རྩྭ༌[^2352]དང་། ཤིང་ཕྲད་པོ༌[^2353]དང་ཞེས་པ་ནས་འཕེལ་ཞིང་རྒྱས་པར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་འབྲས་བུ་སོ་སོར་སྨིན་པའི་དཔེ་སྟེ། དེ་ལའང་དངོས་བརླན་ཏེ་སྨིན་པ་དང་། ཞར་ལ་སྨིན་པའོ། །

[Block 2762]
དེ་ལ་འདི་རིགས༌[^2354]རྣམ༌[^2355]གསུམ་ཡོད་པའི་ཕྱིར་ཐེག་པའང་རྣམ་གསུམ་དུ་འགྱུར་ཏེ། དེ་ལ་ཡང་མདོ་ལས་དཔེར་ན་མི་ནད་པ་གསུམ་ཞིག་ཡོད་པ་ལ་གཅིག་ནི་སྨན་པ་མཁས་པ་དང་ཕྲད་ཀྱང་རུང་མ་ཕྲད་ཀྱང་རུང་ངེས་པར་འཚོ་བ་དང་། ནད་པ་གཅིག་ནི་སྨན་པས་གསོས་ན་འཚོའི་མ་གསོས་ན་མི་འཚོ་བ་དང་། གཅིག་ནི་སྨན་པས་གསོས་ཀྱང་མི་འཚོ་བ་སྟེ། འབྲས་བུ་ཆེ་ཆུང་གི་རིམ་པའང་དེ་བཞིན་དུ་སྦྱར་རོ། །

[Block 2763]
སྡོང་བུ་ཆེན་པོ་དང་བར་མ་དང་། ཆུང་ངུ་ལ་སྨོས་པ་ཡང་ལུང་དང་། གཞུང་དང་། སྤྱོད་པ་དང་། འབྲས་བུའི་དཔེ་སྟེ། འབྲས་བུ་རིམ་པ་བཞིན་དུ་སྦྱར་རོ། །

[Block 2764]
ཆུ་རོ་གཅིག་པས་ཆུང་ངུ་བངས་པ་ནི་མི་ལྡོག་པའི༌[^2356]ས་ལ་གནས་པ་རྣམས་སོ། །

[Block 2765]
ཆེར་བངས་པ་ནི་རྣམ་པ་གཉིས་ཏེ་ས་བདུན་པ་མན་ཆད་ཆུང་ངུ༌[^2357]བངས་པ། [^2358]

[Block 2766]
བརྒྱད་པ་ཡན་ཆད་ནི་ཆེར་བངས་པའོ། །

[Block 2767]
དེ་ཡང་ས་དང་པོ་མན་ཆད་ནི་གཅིག་ཏུ་ཟག་པ་དང་བཅས་པའི་བསྒྲུབ་པའོ། །

[Block 2768]
ས་བདུན་པ་མན་ཆད་ནི་ཟག་པ༌[^2359]མེད་པ་གཉིས་ཀའི་བསྒྲུབ༌[^2360]པའོ། །

[Block 2769]
ས་བརྒྱད་པ་ཡན་ཆད་ནི་གཅིག་ཏུ་ཟག་པ༌[^2361]མེད་པའི་བསྒྲུབ་པའོ། །

[Block 2770]
ཡང་ན་ས་དང་པོ་མན་ཆད་ནི་ཆུང་ངུ་བངས་པ། ས་དང་པོ་ཡན་ཆད་ནི་མི་ལྡོག་པའི་ས་སྟེ་ཆེར་བངས་པའོ། །
--- END BLOCKS ---
