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
[Block 3536]
དེ་ལ་འདོད་ཆགས་དང་མཚུངས་པར་ལྡན་པའི་སེམས་ནི་གཉིས་ཀྱིས༌[^2471]འདོད་ཆགས་དང་བཅས་པ་ཡིན་ནོ། །

[Block 3537]
དེ་ལས་གཞན་པ་ཟག་པ་དང་བཅས་པ་ནི་ལྡན་པའི་འདོད་ཆགས་དང་བཅས་པས་ན་འདོད་ཆགས་དང༌[^2472]བཅས་པ་ཡིན་ནོ། །

[Block 3538]
ཁ་ཅིག་ན་རེ་མདོ་འདིར་ནི་འདོད་ཆགས་དང་མཚུངས་པར་ལྡན་པའི་སེམས་ནི་འདོད་ཆགས་དང་བཅས་པ་ཡིན་ལ། འདོད་ཆགས་ཀྱི༌[^2473]གཉེན་པོར་ནི་འདོད་ཆགས་དང་བྲལ་བར་བཤད་པ་ཡིན་ཏེ། གལ་ཏེ་འདོད་ཆགས་དང་མཚུངས་པར་མི་ལྡན་པ་འདོད་ཆགས་དང་བྲལ་བ་ཡིན་ན་ནི་ཉོན་མོངས་པ་གཞན་དང་མཚུངས་པར་ལྡན་པ་ཡང་ཡིན་པར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 3539]
གཞན་དག་ན་རེ་དེ་ལྟ་ན་ནི་འོ་ན་དེའི་གཉེན་པོ་མ་ཡིན་པའི་སེམས་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་འདོད་ཆགས་དང་བཅས་པ་ཡང་མ་ཡིན་ལ། འདོད་ཆགས་དང་བྲལ་བ་ཡང་མ་ཡིན་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པར་འགྱུར་བས།[^2474] དེ་ལྟ་བས་ན༌[^2475]མདོ་འདིར་འདོད་ཆགས་དང་ལྡན་པས་ཀྱང་འདོད་ཆགས་དང་བཅས་པའི་སེམས་སུ་འདོད་པར་བྱ་སྟེ། གཏི་མུག་དང་བཅས་པ་དང་གཏི་མུག་དང་བྲལ་བའི་བར་དུ་ཡང་དེ་དང་འདྲ་བར་ཤེས་པར་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 3540]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས༌[^2476]ན་རེ་ཀུན་དུ་བསྡུས་པ་ནི་དམིགས་པ་ལ་མངོན་པར་སྡུད་པའི་ཕྱིར་དགེ་བ་ཡིན་ནོ། །

[Block 3541]
རྣམ་པར་གཡེང་བ་ནི་རྣམ་པར་གཡེང་བ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་ཉོན་མོངས་པ་ཅན་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3542]
ནུབ་ཕྱོགས་པ་རྣམས་ན་རེ་ཀུན་ཏུ་བསྡུས་པ་ནི་གཉིད༌[^2477]དང་མཚུངས་པར་ལྡན་པ་ཡིན་ནོ། །

[Block 3543]
རྣམ་པར་གཡེང་བ་ནི་ཉོན་མོངས་པ་ཅན་གཞན་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3544]
དེ་སྐད་དུ༌[^2478]མི་བརྗོད་དེ། ཉོན་མོངས་པ་ཅན་གྱི་གཉིད་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་སེམས་དེ་ཉིད་བསྡུས་པ་ཡང་ཡིན་ལ་རྣམ་པར་གཡེངས་པ༌[^2479]ཡང་ཡིན་པར་འགྱུར་རོ། །

[Block 3545]
བསྟན་བཅོས་ལས།

[Block 3546]
སེམས་ཀུན་དུ་བསྡུས་པ་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་རབ་ཏུ་ཤེས་སོ། །

[Block 3547]
དེ་ཤེས་པའི་ཤེས་པ་ནི་བཞི་སྟེ། ཆོས་ཤེས་པ་དང་། རྗེས་སུ་ཤེས་པ་དང་། ཀུན་རྫོབ་ཤེས་པ་དང་། ལམ་ཤེས་པའོ་ཞེས་འབྱུང་བ་དང་ཡང་འགལ་བར་འགྱུར་རོ། །

[Block 3548]
སེམས་ཞུམ་པ་ནི་ལེ་ལོ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་ཉོན་མོངས་པ༌[^2480]ཡིན་ནོ། །

[Block 3549]
རབ་ཏུ་བཟུང་བ་ནི་བརྩོན་འགྲུས་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་དགེ་བ་ཡིན་ནོ། །

[Block 3550]
ཆུང་ངུ་ནི་རྣམ་པར་བྱང་བ་ཆུང་ངུ་དག་གིས་བསྟེན་པའི་ཕྱིར་ཉོན་མོངས་པ་ཅན་ཡིན་ནོ། །

[Block 3551]
ཆེན་པོར་གྱུར་པ་ནི་དེ་ལས་བཟློག་པ་ཡིན་པའི་ཕྱིར་དགེ་བ་ཡིན་ནོ། །

[Block 3552]
རྩ་བ་དང་། རིན་དང་། འཁོར་དང་། རྗེས་སུ་འབྲང་བ་དང་། སྟོབས་ཆེ་ཆུང་གི་ཡང་ཕྱིར་ཏེ། ཉོན་མོངས་པ་ཅན་ནི་མི་དགེ་བའི་རྩ་བ་གཉིས་ཀྱིས་རྩ་བ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 3553]
དགེ་བ་ནི་དགེ་བའི་རྩ་བ་གསུམ་གྱིས་སོ། །

[Block 3554]
ཉོན་མོངས་པ་ཅན་ནི་འབད་པས་བསྒྲུབ་པར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རིན་ཆུང་བ་ཡིན་ནོ། །

[Block 3555]
དགེ་བ་ནི༌[^2481]ཚོགས་ཆེན་པོས་བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རིན་ཆེ་བ་ཡིན་ནོ། །

[Block 3556]
ཉོན་མོངས་པ་ཅན་ནི་དེ་དང་འདྲ་བ་མ་འོངས་པ་འཐོབ་པའི་ཕྱིར་འཁོར་མང་བ་མ་ཡིན་ལ་ཕུང་པོ་གསུམ་གྱིས༌[^2482]རྗེས་སུ་འབྲང་བ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 3557]
དགེ༌[^2483]བ་ནི་འཁོར་མང་བ་ཡིན་ལ་ཕུང་པོ་བཞིས་རྗེས་སུ་འབྲང་བ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 3558]
ཡང་ཉོན་མོངས་པ་ཅན་ནི་སྟོབས་ཆུང་བ་ཡིན་ནོ། །

[Block 3559]
དགེ་བ་ནི་སྟོབས་ཆེ་བ་ཡིན་ནོ། །

[Block 3560]
སྡུག་བསྔལ་ལ་ཆོས་ཤེས་པའི་བཟོད་པ་གཅིག་གིས༌[^2484]ཀྱང་ཕྲ་རྒྱས་བཅུ་གཏན་དུ་འཇོམས་པར་བྱེད་པས་དེའི་ཕྱིར་ཡང་ཉོན་མོངས་པ་ནི་ཆུང་བ་ཡིན་ལ་དགེ་བ་ནི་ཆེན་པོར་གྱུར་པ་ཡིན་ནོ། །

[Block 3561]
རྒོད་པ་ནི་རྒོད་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་ཉོན་མོངས་པ་ཅན་ཡིན་ནོ། །

[Block 3562]
རྒོད་པ་མ་ཡིན་པ་ནི་དེའི་གཉེན་པོ་ཡིན་པའི༌[^2485]ཕྱིར༌[^2486]དགེ་བ་ཡིན་ནོ། །

[Block 3563]
རྣམ་པར་མ་ཞི་བ་དང་། རྣམ་པར་ཞི་བ་ཡང་དེ་དང་འདྲའོ། །

[Block 3564]
མཉམ་པར་མ་བཞག་པ་ནི་རྣམ་པར་གཡེང་བ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་ཉོན་མོངས་པ་ཅན་ནོ། །

[Block 3565]
མཉམ་པར་བཞག་པ་ནི་དེའི་གཉེན་པོ་ཡིན་པའི་ཕྱིར་དགེ་བ་ཡིན་ནོ། །

[Block 3566]
མ་བསྒོམས་པ་ནི་འཐོབ་པ་དང་བསྟེན་པའི་བསྒོམ་པ༌[^2487]དག་གིས༌[^2488]མ་བསྒོམས་པའི༌[^2489]ཕྱིར་ཉོན་མོངས་པ་ཅན༌[^2490]ནོ། །

[Block 3567]
བསྒོམས་པ་ནི་དེ་གཉིས་ཀྱིས་བསྒོམས༌[^2491]པའི་ཕྱིར་དགེ་བ་ཡིན་ནོ། །

[Block 3568]
རྣམ་པར་མ་གྲོལ་བ་ནི་རང་བཞིན་དང་རྒྱུད་རྣམ་པར་མ༌[^2492]གྲོལ་བ་དག་གིས་རྣམ་པར༌[^2493]གྲོལ་བའི་ཕྱིར་ཉོན་མོངས་པ་ཅན་ཡིན་ནོ། །

[Block 3569]
རྣམ་པར་གྲོལ་བ་ནི་དེ་གཉིས་ཀྱིས༌[^2494]རྣམ་པར་གྲོལ་བའི་ཕྱིར་དགེ་བ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3570]
དེ་ལྟ་ན་ནི་མདོ་དང་མི༌[^2495]མཐུན་པར་བྱས་པ་ཡང་ཡིན་ལ། ཚིག་དེ་རྣམས་ཀྱི་དོན་གྱི༌[^2496]ཁྱད་པར་ཡང་མ་བཤད་པ་ཡིན་ནོ། །

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
--- END BLOCKS ---
