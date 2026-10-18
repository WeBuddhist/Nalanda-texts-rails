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
ཇི་ལྟར་ན་མདོ་དང་མི་མཐུན་པར་བྱས་པ་ཡིན་ཞེ་ན། མདོ་ལས་ཇི་ལྟར་ན་སེམས་ནང་དུ་ཀུན་དུ་བསྡུས་པ་ཡིན་ཞེ་ན། སེམས་གང་རྨུགས་པ་དང༌[^2497]གཉིད་དང་ལྷན་ཅིག་པར་གྱུར་ཅིང་ནང་དུ་ཀུན་དུ་འགོག་པ་དང་ལྷན་ཅིག་པར་གྱུར་ལ་ལྷག་མཐོང་དང་མཚུངས་པར་མི་ལྡན་པ་ཡིན་ནོ། །

[Block 3572]
ཇི་ལྟར་ན་ཕྱི་རོལ་དུ་རྣམ་པར་གཡེངས་པ༌[^2498]ཡིན་ཞེ་ན། སེམས་གང་འདོད་པའི་ཡོན་ཏན་ལྔ་རྣམས་ལ་རྗེས་སུ་གཡེངས་པ༌[^2499]ཡིན་ཞིང་རྣམ་པར་འཕྲོས་པ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 3573]
སེམས་དེ་ཉིད་ཀུན་དུ་བསྡུས་པ༌[^2500]ཡིན་ལ་རྣམ་པར་གཡེངས་པ་ཡང་ཡིན་པར་འགྱུར་རོ་ཞེས་ཀྱང་བཤད་པ་ཡིན་ནམ་ཞེ་ན། དེ་སྐད་དུ་ནི་བཤད་མོད་ཀྱི་རིགས་པར་བཤད་པ་ནི་མ་ཡིན་ཏེ། ཉོན་མོངས་པ༌[^2501]ཅན་གྱི༌[^2502]གཉིད་དང་ལྷན་ཅིག་པར་གྱུར་པ་རྣམ་པར་གཡེངས་པ་ཉིད་དུ་དམ་མ་བཅས་པའི་ཕྱིར་རོ། །

[Block 3574]
བསྟན་བཅོས་དང་འགལ་བར་འགྱུར་རོ་ཞེས་ཀྱང་བཤད་པ་མ་ཡིན་ནམ། བསྟན་བཅོས༌[^2503]དང་འགལ་བ་ནི་བླའི་མདོ་དང་འགལ་བ་ནི་མ་ཡིན་ནོ། །

[Block 3575]
ཇི་ལྟར་ན་ཚིག་དེ་རྣམས་ཀྱི་དོན་གྱི་ཁྱད་པར་མ་བཤད་པ་ཡིན་ཞེ་ན། སེམས་རྣམ་པར་གཡེངས་པ་དང་། ཞུམ་པ་དང་། རྒོད་པ་དང་རྣམ་པར་མ་ཞི་བ་དང་། མཉམ་པར་མ་བཞག་པ་དང་། མ་བསྒོམས་པ་དང་། རྣམ་པར་མ་གྲོལ་བ་རྣམས་ཀྱི༌[^2504]མཚན་ཉིད་ཀྱང་ཐ་མི་དད་པར་བཤད༌[^2505]པའི་ཕྱིར་ལ། ཀུན་དུ་བསྡུས་པ་དང་། རབ་ཏུ་བཟུང་བ་ལ་སོགས་པའི་མཚན་ཉིད་ཀྱང་ཐ་མི་དད་པར་བཤད་པའི་ཕྱིར་རོ། །

[Block 3576]
ཚིག་རྣམས་ཀྱི་དོན་གྱི་ཁྱད་པར་ནི་མ་བཤད་པ་མ་ཡིན་པ་ཉིད་དེ། ཉོན་མོངས་པ་ཅན་དུ་མཚུངས་ཀྱང་འདི་ལྟར་སེམས་ཉོན་མོངས་པ་ཅན་འདི་ནི་རྣམ་པར་གཡེངས་པ་ཡིན་ནོ། །

[Block 3577]
འདི་ནི་ཞུམ་པ་ཡིན་ནོ་ཞེས་བྱ་བ་རྒྱས་པར་དེའི་ཉེས་པའི་ཁྱད་པར་ཡང་དག་པར༌[^2506]བསྟན་པའི་ཕྱིར་ལ། དེ་བཞིན་དུ་དགེ་བ༌[^2507]ཡང་ཡོན་ཏན་གྱི་ཁྱད་པར་ཡང་དག་པར་བསྟན་པའི་ཕྱིར་དོན་གྱི་ཁྱད་པར་བཤད་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 3578]
མདོ་དང་འགལ་བ་མ་སྤངས་པའི་ཕྱིར་དེ་ནི་ཚིག་དེ་རྣམས་ཀྱི་དོན་མ་ཡིན་ནོ། །

[Block 3579]
གལ་ཏེ་མདོ་ལས་སེམས་དེ་ཉིད་ཞུམ་པ་ཡང་ཡིན་ལ་དེ་ཉིད་རྒོད་པ་ཡང་ཡིན་ནོ་ཞེས་བྱ་བར་བཤད་ན་ནི་གང་གི་ཚེ་སེམས་ཞུམ་པ་དང་ཞུམ་པར་དོགས་པ་དེའི་ཚེ་ཤིན་དུ་སྦྱངས་པ་དང་། ཏིང་ངེ་འཛིན་དང་། བཏང་སྙོམས་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་རྣམས་བསྒོམ་པའི༌[^2508]དུས་མ་ཡིན་ནོ། །

[Block 3580]
གང་གི་ཚེ་སེམས་རྒོད་པ་དང་རྒོད་པར་དོགས་པ་དེའི་ཚེ་ཆོས་རབ་ཏུ་རྣམ་པར་འབྱེད་པ་དང་། བརྩོན་འགྲུས་དང་། དགའ་བ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་རྣམས་བསྒོམ་པའི༌[^2509]དུས་མ་ཡིན་ནོ་ཞེས་པ་འདི་དག་གསུངས་པར་མི་འགྱུར་རོ། །

[Block 3581]
ཅི་འདི་ལ་བྱང་ཆུབ་ཀྱི་ཡན་ལག་རྣམས་སོ་སོར་བསྒོམ་མམ་ཞེ་ན། འདི་དག་ཡིད་ལ་བྱེད་པ་བསྒོམ་པ་ཡིན༌[^2510]པར་འདོད་ཀྱི་མངོན་སུམ་དུ་གྱུར་པ༌[^2511]ནི་མ་ཡིན་པས་ཉེས་པ་མེད་པ་ཉིད་དོ། །

[Block 3582]
འདི་ལས་ལེ་ལོ་ལྷག་པའི་སེམས་ནི་ཞུམ་པ་ཞེས་བཤད་ལ། རྒོད་པ་ལྷག་པ་ནི་རྒོད་པ་ཞེས་བཤད་པས་འགལ་བ་མེད་དེ། དེ་གཉིས་ཀྱང་ལྷན་ཅིག་པ་ཡིན་པའི་ཕྱིར་སེམས་དེ་ཉིད་ཞུམ་པ་ཡང་ཡིན་ལ་དེ་ཉིད་རྒོད་པ་ཡང་ཡིན༌[^2512]ཞེས་སྨྲའོ། །

[Block 3583]
བསམ་པ་ཅན་གྱི་ཚིག་ལ་ནི་བཟློག་པ་མེད་ཀྱི་མདོའི་དགོངས་པ་ནི་འདི་མ་ཡིན་ནོ་ཞེས་སྨྲའོ། །

[Block 3584]
འདོད་ཆགས་དང་ལྡན་པའི་སེམས་ཐམས་ཅད་འདོད་ཆགས་དང་བཅས་པ་ཡིན་ནོ་ཞེས་གང༌[^2513]བཤད་པ། འདོད་ཆགས་དང་ལྡན་པའི་སེམས་གང་ཞིག་ཡིན། གལ་ཏེ་འདོད་ཆགས་ཀྱི་ཐོབ་པ་དང་ལྷན་ཅིག་པ་ཡིན་ནོ་ཞེ་ན་ནི་སློབ་པའི་སེམས་ཟག་པ་མེད་པ་ཡང་འདོད་ཆགས་དང་བཅས་པར་འགྱུར་རོ། །

[Block 3585]
གལ་ཏེ་འདོད་ཆགས་ཀྱི་དམིགས་པ་ཡིན་ནོ་ཞེ་ན་ནི་དགྲ་བཅོམ་པའི་སེམས་ཟག་པ་དང་བཅས་པ་ཡང་འདོད་ཆགས་དང་བཅས་པ་ཞེས་བྱ་བར་གཟུང་བར༌[^2514]འགྱུར་ཏེ། འདོད་ཆགས་ཀྱི་དམིགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3586]
ཡང་ན་ཇི་ལྟར་དེ་ཟག་པ་དང་བཅས་པ་ཡིན། གལ་ཏེ་ཉོན་མོངས་པ་སྤྱི་པའི་དམིགས་པ་ཡིན་པའི་ཕྱིར་རོ་ཞེ་ན་ནི། [^2515]དེ་ལྟ་ན་ཡང་གཏི་མུག་དང་བཅས་པར་གཟུང་བར་འགྱུར་ཏེ། གཏི་མུག་གི་དམིགས་པ་ཡིན་པའི༌[^2516]ཕྱིར་རོ། །

[Block 3587]
གཞན་གྱི་སེམས་ཤེས་པ་ནི་ཐོབ་པ་ལ་དམིགས་པ་ཡང་མ་ཡིན་ལ། སེམས་དེ་ལ་དམིགས་པའི་འདོད་ཆགས་ལ་དམིགས་པ་ཅན་ཡང་མ་ཡིན་ནོ། །

[Block 3588]
དེ་ལྟ་བས་ན་འདིར༌[^2517]འདོད་ཆགས་དང་ལྡན་པས་འདོད་ཆགས་དང་བཅས་པའི་སེམས་སུ་འདོད་པར་མི་བྱའོ། །

[Block 3589]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། མདོའི་དགོངས་པ་ནི་འདོད་ཆགས་དང་མཚུངས་པར་ལྡན་པའི་སེམས་ནི་འདོད་ཆགས་དང་བཅས་པ་ཡིན་ལ། འདོད་ཆགས་དང་མཚུངས་པར་མི་ལྡན་པའི་སེམས་ནི་འདོད་ཆགས་དང་བྲལ་བ་ཡིན་ནོ་ཞེས་བྱ་བར་སྣང་ངོ་། །གང་ལས་འདིའི་སེམས་འདོད་ཆགས་དང་བྲལ་བ་ཡིན། ཞེ་སྡང་དང་བྲལ་བ་དང་། གཏི་མུག་དང་བྲལ་བ་ཡིན། འདོད་པའི་སྲིད་པ་དང་། གཟུགས་ཀྱི་སྲིད་པ་དང་། གཟུགས་མེད་པའི་སྲིད་པར་ཕྱིར་མི་ལྡོག་པའི་ཆོས་ཅན་ཡིན་ཞེས་གསུངས་པ་དེར་ནི་དེའི་ཐོབ་པ་དང་བྲལ་བ་ལས་དགོངས་ཏེ་གསུངས་པ་ཡིན་ནོ། །

[Block 3590]
ཉོན་མོངས་པ་གཞན་དང༌[^2518]མཚུངས་པར་ལྡན་པའི་སེམས་ཀྱང་འདོད་ཆགས་དང་མཚུངས་པར་མི་ལྡན་པའི་ཕྱིར་འདོད་ཆགས་དང་བྲལ་བ་ཡིན་པར་འགྱུར་རོ་ཞེས་བཤད་པ་མ་ཡིན་ནམ་དགོངས་པ་འདི་ནི༌[^2519]ཉེས་པ་མེད་དེ། དེ་ནི་འདོད་ཆགས་དང་བྲལ་བ་ཞེས་བྱ་བར་མི་གཟུང༌[^2520]ངོ་། །འོ་ན་ཅི་ལྟ༌[^2521]ཞེ་ན། ཞེ་སྡང་དང་བཅས་པ་དང་། གཏི་མུག་དང་བཅས་པ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པར་གཟུང་ངོ་། །ཞར་ལ་འོངས་པས་ཆོག་གོ། །

[Block 3591 [HEADING]]
##### གྲུབ་པའི་མཐའ། ^4-3-4-4-0

[Block 3592]
གྲུབ་པའི་མཐའ་བརྗོད་པར་བྱ་སྟེ། ཅི་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ཕ་རོལ་གྱི་སེམས་ཀྱི་རྣམ་པ་འམ་དམིགས་པ་འཛིན་ཞེ་ན། མི་འཛིན་ཏོ། །

[Block 3593]
དེ་ནི༌[^2522]རྣམ་པ་དང་དམིགས་པ་ལ་མི་ལྟོས་པ་ཡིན་ཏེ། སེམས་འདི་ཆགས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་ཤེས་ཀྱི་གཟུགས་ཆེ་གེ་མོ་ཞིག་ལ་ཆགས་སོ་ཞེས་བྱ་བར་ནི་མི་ཤེས་སོ། །

[Block 3594]
དེ་ལྟ་མ་ཡིན་ན། དེ་གཟུགས་ལ་དམིགས་པར་ཡང་འགྱུར་ལ། དེ་ལ་དམིགས་པའི་ཕ་རོལ་གྱི་སེམས་འཛིན་པ་ནི༌[^2523]རང་གི་ངོ་བོ་ཉིད༌[^2524]འཛིན་པར༌[^2525]ཡང་འགྱུར་རོ། །

[Block 3595]
གཞན་གྱི་སེམས་ཤེས་པ་ཐམས་ཅད་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་དང་། རྫས་ཀྱི་རང་གི་མཚན་ཉིད་དང་། ད་ལྟར་བྱུང་བ་དང་། ཕ་རོལ་གྱི་རྒྱུད་དང་འདོད་པ་དང་། གཟུགས་དང་ལྡན་པ་དང་། ལྡན་པ་མ་ཡིན་པའི་ཡུལ་ཅན་མཐོང་བའི་ལམ༌[^2526]བཀག་པ་དང་། བསྒོམ་པའི་ལམ་ལ་དམིགས་པ་དང་། སྟོང་པ་ཉིད་དང་མཚན་མ་མེད་པ་དང་མི་ལྡན་པ་དང་། ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པས་མ་བསྡུས་པ་དང་། བར་ཆད་མེད་པའི་ལམ་བཀག་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3596]
ཕ་རོལ་གྱི་སེམས་ཤེས་པ་བཤད་ཟིན་ཏོ། །

[Block 3597 [HEADING]]
#### ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པའི་རྣམ་པ། ^4-3-5-0

[Block 3598 [VERSE]]
ལྷག་མ་རྣམ་པ་བཅུ་བཞི་ཅན། །
སྟོང་དང་བདག་མེད་མ་གཏོགས་སོ། །

[Block 3599]
ལྷག་མ་ནི་ཟད་པ་དང་མི་སྐྱེ་བ་ཤེས་པ་དག་སྟེ། དེ་གཉིས་ནི་སྟོང་པ་དང་བདག་མེད་པའི་རྣམ་པ་དག་མ་གཏོགས་པ་རྣམ་པ་བཅུ་བཞི་ཅན་ཡིན་ནོ། །

[Block 3600]
དོན་དམ་པ་པ་དག་ཡིན་ཡང་དེ་དག་གི་སྟོབས་ཀྱི་རྗེས་སུ་ཐ་སྙད་འདོགས་པའི་སྒོ་ནས་བདག་གི་སྐྱེ་བ་ཟད་དོ། །

[Block 3601]
འདི་ལས་སྲིད་པ་གཞན་རབ་ཏུ་མི་ཤེས་སོ་ཞེས་ཀུན་རྫོབ་ལ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 3602 [HEADING]]
### ཟག་པ་མེད་པའི་རྣམ་པ། ^4-4-0

[Block 3603]
ཅི་ཟག་པ་མེད་པ་ལ་རང་གི་མཚན་ཉིད་ཀྱི་རྣམ་པ་ཡོད་དམ། འོན་ཏེ་མེད་ཅེ་ན། རེ་ཞིག་ཁ་ཆེ་བ་རྣམས་ཀྱི་ལྟར་ན།[^2527] དྲི་མེད་བཅུ་དྲུག་གཞན་རྣམས་མེད། །རྣམ་པ་བཅུ་དྲུག་ལས་མ༌[^2528]གཏོགས་པ་ཟག་པ་མེད་པའི་རྣམ་པ་མེད་དོ། །

[Block 3604]
གཞན་ཡོད་ཅེས་བྱ༌[^2529]བསྟན་བཅོས་ལས། །

[Block 3605]
གཞན་ཉི་འོག་པ་རྣམས་ན་རེ་ཡོད་དོ་ཞེས་ཟེར་རོ། །ཇི་ལྟར་ན༌[^2530]ཁོང་དུ་ཆུད་ཅེ་ན། བསྟན་བཅོས་ལས་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྟན་བཅོས་ལས་འདི་སྐད་དུ་མི་ལྡན་པའི་སེམས་ཀྱིས༌[^2531]འདོད་པ་དང་ལྡན་པའི་ཆོས་རྣམས་ཤེས་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན། ཤེས་པར་འགྱུར་ཏེ། རིགས་པས་བསྐྱེད་པའི་སྒོ་ནས་མི་རྟག་པ་དང་། སྡུག་བསྔལ་བ༌[^2532]དང་། སྟོང་པ་དང་། བདག་མེད་པ་དང་། རྒྱུ་དང་། ཀུན་འབྱུང་བ་དང་། རབ་ཏུ་སྐྱེ་བ་དང་། རྐྱེན་དང་། འདི་ནི་གནས་ཡོད་དོ། །

[Block 3606]
འདི་ནི་གཞི་ཡོད་དོ་ཞེས་བྱ་བར་ཤེས་པར་འགྱུར་རོ་ཞེས་འབྱུང་ངོ་། །གལ་ཏེ་གང་ལས་འདི་ནི་གནས་ཡོད་དོ། །

[Block 3607]
འདི་ནི་གཞི་ཡོད་དོ་ཞེས་དེ་སྙམ་དུ་ཤེས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདིའི་དོན་ནི་འདི་མ་ཡིན་ཏེ། འོན་ཀྱང་མི་རྟག་པ་ལ་སོགས་པ༌[^2533]ཤེས་པར་འགྱུར་བ་གང་ཡིན་པ་འདི་ནི་གནས་ཡོད་དོ། །

[Block 3608]
འདི་ནི་གཞི་ཡོད་དོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 3609]
ཞེ་ན། མ་ཡིན་ཏེ། གཞན་ནས་མི་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 3610]
གལ་ཏེ་འདི་བསྟན་བཅོས་ཀྱི་དོན་ཡིན་པར་འགྱུར་ན། འདི་སྐད་དུ་མཐོང་བས་སྤང་བར་བྱ་བའི་སེམས་ཀྱིས༌[^2534]འདོད་པ་དང་ལྡན་པའི་ཆོས་རྣམས་ཤེས་པར་འགྱུར་བ་ཡོད་དམ་ཞེ་ན། ཤེས་པར་འགྱུར་ཏེ། རིགས་པ་མ་ཡིན་པས་བསྐྱེད་པའི་སྒོ་ནས་བདག་དང་། བདག་གི་དང་། རྟག་པ་དང་། ཆད་པ་དང་། རྒྱུ་མེད་པ་དང་། བྱེད་པ་མེད་པ་དང་། སྐུར་བ་འདེབས་པ་དང་། མཆོག་དང་། གཙོ་བོ་དང་། ཁྱད་པར་དུ་འཕགས་པ་དང་། དམ་པ་དང་། དག་པ་དང་། གྲོལ་བ་དང་། ངེས་པར་འཛིན་པར་བྱེད་པ་དང་། ནེམ་ནུར་དང་། ཡིད་གཉིས་དང་། ཐེ་ཚོམ་དུ་ཤེས་པར་འགྱུར་ཞིང་། ཆགས་པ་དང་། སྡང་བ་དང་། རློམ་པ་དང་། རྨོངས་པར་འགྱུར་རོ་ཞེས་གང་གསུངས་པ་དེར་ཡང་འདི་སྐད་དུ་འདི་ནི་གནས་ཡོད་དོ། །
--- END BLOCKS ---
