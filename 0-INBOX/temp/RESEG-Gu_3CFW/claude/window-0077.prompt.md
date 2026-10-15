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
[Block 2696]
ཁས་མ་བླངས་པ་དག་ཁས་བླངས་པ་དག་དང་ལྷན་ཅིག་ལོངས་སྤྱོད་པར་བྱེད་པ་དག་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2697]
འཁོར་ལོ་བྱེ་བ་དག་ལས་ཐ་དད་པ་དག་ལ་ཡང་ཆོ་ག་འདི་རྣམ་པར་གཞག་པ་དེ་བས་ན་བྱེ་བྲག་མེད་པར་མདོར་བྱས་པ་སྟེ། ཐམས་ཅད་ཀྱི་དབང་དུ་བྱས་ནས་བསྟན་པའོ། །

[Block 2698]
ནན་ཏུར་བྱས་པ་གཞན་དག་ལ་དེ་གཉིས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་ནས་ཕྱུང་བ་ལས་གཞན་པའི་ནན་ཏུར་བྱས་པ་བསྡིགས་པ་དང་། སྨད་པ་དང་། བསྐྲད་པ་དང་། [^2513]ཕྱིར་འགྱེད་པ་བྱས་པའི་ཡུལ་དག་ལ་ལྷན་ཅིག་གནས་པར་མི་བྱ་བ་ཉིད་དང་ལྷན་ཅིག་ལོངས་སྤྱོད་པར་མི་བྱ་བ་ཉིད་དེ་གཉིས་མི་བྱའོ།[^2514] །འདིར་གཞུང་ནི་བསྡིགས་པའི་ལས་བགྱིས་པ་ལ་སྨད་པའི་ལས་བགྱིས༌[^2515]ན་བགྱིས་པར་བརྗོད་པར་བགྱིའམ། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བྱས་པར་བརྗོད་པར་བྱ་སྟེ།

[Block 2699]
བསྡིགས་པའི་ལས་ནི་བག་ཡངས་སུ་གྱུར་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པས་གནས་ནས་ཕྱུང་བ་ལས།

[Block 2700]
གཞན་པའི་ནན་ཏུར་བྱས་པ་དག་ལ་ནན་ཏུར་གཞན་འཆགས་པར་གསུངས་ནས། གནས་ནས་ཕྱུང་བ་ལ་བསྡིགས་པའི་ལས་བགྱིས་ན་བགྱིས་པར་བརྗོད་པར་བགྱིའམ། ཉེ་བ༌[^2516]འཁོར་མི་བྱ་སྟེ། [^2517]ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་ལོངས་མི་སྤྱོད་པར་བྱ་བའི་ཕྱིར་སོང་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2701]
དེ་བཞིན་དུ་གནས་ནས་ཕྱུང་བ་ལ་སྨད་པ་དང་། བསྐྲད་པ་དང་། ཕྱིར་འགྱེད་པའི་ལས་བགྱིས༌[^2518]ན་བགྱིས་པར་བརྗོད་པར་བགྱིའམ། ཉེ་བ༌[^2519]འཁོར་མི་བྱ༌[^2520]སྟེ། དེ་ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་ལོངས་མི་སྤྱད་པར་བྱ་བའི་ཕྱིར་སོང་བ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་གསུངས་པ་ཡིན་ཏེ་དེའི་ཕྱིར་མདོ་འདི་བྱས་སོ། །

[Block 2702]
དེས་འགྲོགས་བཤེས་ལ་བརྟེན་ཏེ་གནས་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ནན་ཏུར་བྱས་པ་དེས་འགྲོགས་བཤེས་ལ་བརྟེན་ཏེ་གནས་པར་བྱ་བ་ཉིད་ཡིན་པ་སྟེ། གང་གི་ཕྱིར་ཆད་པ་དང་བཅས་པ་ཉིད་ལ་ཡང་དེ་ལྟར་འགྱུར་རོ། །

[Block 2703]
འདིར་གཞུང་ནི་མི་གནས་པར་འདུག་པར་མི་བྱའོ་ཞེས་གསུངས་པ་དེའི་དོན་ཅི་ལགས། གང་ཟག་གང་ལ་འགྲོགས་བཤེས་སམ། གུས་པ་དང་ངོ་ཚ་ཤེས་པ་དང་། ཡིད་དུ་འཐད་པའི་སེམས་ཉེ་བར་གནས་པ་ཡོད་པ་དེ་ལ་གནས་དེར་འདུག་པར་བྱའོ་ཞེས་གསུངས་པའི་གཞུང་གནང་བ༌[^2521]ཡིན་ནོ། །

[Block 2704]
དེའི་ཕྱིར་མདོ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2705]
ནན་ཏུར་བྱས་པས་སམ་ཉམས་པ་བསྐྲད་པར་བྱ་བས༌[^2522]འགྱུར་བ་བརྟེན་ན་ཡོ་བྱད་ཀྱང་ཕྱུང་སྟེ་དེར་རོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གང་ལ་ནན་ཏུར་བྱས་པ་དེས་སམ། ཚུལ་ཁྲིམས་འཆལ་པ་ཉམས་པ༌[^2523]ལ་བསྐྲད་པར་བྱ་བ་དེས་ངོ་ཟུམ་དང་ཁྲོ་བ་ལ་སོགས་པར་འགྱུར་བ་བསྟན་པ༌[^2524]དེའི་ཚེ་དེའི༌[^2525]ཡོ་བྱད་ཀྱང་ཕྱུང་སྟེ་དོར་བར་བྱའོ། །

[Block 2706]
གླེང་གཞི་དག་ལས།

[Block 2707]
གཙུག་ལག་ཁང་ནས་ཞེས་བྱ་བ་ལ་སོགས་པ་ནས་དེ་ཉིད་གནས་པ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 2708]
མཐུས་བསྐྲད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་གང་ཟག་ནན་ཏུར་བྱ་བ་དང་། ཚུལ་ཁྲིམས་འཆལ་པ་དེ་གཉིས་སོ། །

[Block 2709]
འཇུས་པ་གཅད༌[^2526]པར་བྱའོ་ཞེས་བྱ་བ་ནི་གྲལ་ནས་བསྐྲད་པར་བྱ་བ་དག་ཀ་བ་ལ་སོགས་པ་གང་ལ་འཇུས་པ་དེ༌[^2527]ཡང་བཅད་པར༌[^2528]བྱའོ། །

[Block 2710]
དེ་རྡིབ་པའི་ཆོས་ཅན་མ་ཡིན་ན་དབྱུང་ངོ་ཞེས་བྱ་བ་ནི་གང་ལ་འཇུས་པ་བཅས་པར༌[^2529]བྱ་བ་དེ་རྡིབ་པར་འགྱུར་བ་ཉིད་མ་ཡིན་པ་དེ་དབྱུང་བར་བྱའོ། །

[Block 2711]
འདིར་གཞུང་ནི་དེ་ལ་ཀ་བ་གཅད་པར༌[^2530]བྱ་སྒོ་སྐྱེས་དབྱུང་བར་བྱ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེའི་ཕྱིར་མདོ་གཉིས་བྱས་སོ། །

[Block 2712]
དགེ་འདུན་གྱི་དེ༌[^2531]ཕྱིར་བཅོས་སོ་ཞེས་བྱ་བ་ནི་བཅད་པ་དང་དབྱུང་བ་ཡང་ངོ་། །ཇི་ལྟར་ཞེ་ན་དེའི་ཕྱིར་བཅོལ༌[^2532]ཏེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་སྦྱིན་པ་དག་ལའོ། །

[Block 2713]
མ་གྲུབ་ན་གཙུག་ལག་ཁང་གི་རྫས་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་བཅོལ་ཏེ་མ་གྲུབ་ན་གཙུག་ལག་ཁང་གི་རྫས་ཀྱིས་ཕྱིར་བཅོས་པར་བྱའོ། །

[Block 2714]
འཐབ་ཀྲོལ་བྱེད་པ་བསྐྲད་པ་ན་གཟུང་བར༌[^2533]མི་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་འཐབ་ཀྲོལ་བྱེད་པ་གཙུག་ལག་ཁང་ནས་བསྐྲད་པ་ནི་དགེ་སློང་གཞན་གྱིས་ཕྱིར་གཟུང་བར༌[^2534]མི་བྱ་སྟེ། དེ་ནི་ཕྲན་ཚེགས་དག་ལས་འབྱུང་བའོ། །

[Block 2715]
འཐབ་ཀྲོལ་ལ་འབད་པས་མ་ལོག་ན་ཉེ་བར་ཞི་བར་བྱ་བའི་ཕྱིར་གནས་ནས་དབྱུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཐ་མལ་པ་ཉེ་བར་ཞི་བར་བྱ་བའི་དོན་ལ་འབད་པས་མ་ལོག་ཅིང་མ་བཏང་ན་འཐབ་ཀྲོལ་ཉེ་བར་ཞི་བར་བྱ་བའི་ཕྱིར་དེ་གནས་ནས་དབྱུང་བའི་ལས་བྱའོ། །

[Block 2716]
ཡང་དང་ཡང་དུ་དོན་གཞན་དང་གཞན་གྱི་ཕྱིར་འཐབ་ཀྲོལ་སྐྱེད་པར་བྱེད་པ་ཉིད་ལ་ནི་བསྡིགས་པའི་ལས་བྱའོ། །

[Block 2717]
མི་གཏོང་བ་ལ་ནི་གནས་ནས་དབྱུང་བའི་ལས་བྱ་སྟེ། དེ་གཉིས་ཀྱི་ཡུལ་གྱི་བྱེ་བྲག་ནི་དེ་ཡིན་ནོ། །

[Block 2718]
འདིར་གཞུང་ནི་གླེང་གཞི་དག་ལས།

[Block 2719]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། འཐབ་ཀྲོལ་བྱེད་པ་དག་བཟློག་པར་བྱའོ། །

[Block 2720]
དེ་དག་བཟློག་པ་མི་འཁོད་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གལ་ཏེ་བཟློག་པ་ན་མི་འཁོད་ན་གནས་ནས་དབྱུང་བའི་ལས་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2721]
རྣམ་པར་གཏན་ལ་འབེབས་པ་ལས་གྱུར་པ་ལས༌[^2535]ཉེ་བར་ཞི་བས་སོ་ཞེས་བྱ་བ་ནི༌[^2536]རྣམ་པར་གཏན་ལ་འབེབས་པའི་དོན་ལ་འཐབ་མོ་གང་ལ་རྩོད་པའི་གཞི་ཉེ་བར་ཞི་བས་ཉེ་བར་ཞི་བ་བརྗོད་པར་གྱུར་པ་ལ། ཉེ་བར་མ་ཞི་བས་འཐབ་ཀྲོལ་གྱི་རྒྱུ་ཉེ་བར་བསྒྲུབ་པ་ལས་བཟློག་པའི་ཕྱིར། དེ་གཉིས་ཀ༌[^2537]ཞི་བར་བྱ་བའི་དོན་དུ་གནས་ནས་དབྱུང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2722]
གནས་པ༌[^2538]ལ་གནས་ཀྱིས་འབད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་སློབ་མ་ཉེ་གནས་ཀྱི་རྣམ་པར་གཏན་ལ༌[^2539]འབེབས་པ་ལས་གྱུར་པའི་འཐབ་མོ་ཉེ་བར་ཞི་བར་བྱ་བའི་ཕྱིར་ཡལ་བར་མི་འདོར་བར་འབད་པར་བྱ་བ་སྟེ། འདི་ལྟར་དེས་གཞན་ལ་བཅོལ་བས་འབད་པར་བྱ་བའམ། རང་གིས༌[^2540]ཉེ་བར་ཞི་བར་བརྗོད་པར་གྱུར་པ་ལས་ཀྱང་རུང་ངོ་ཞེས་བྱ་བ་བྱེ་བྲག་མེད་པར་ཤེས་པར༌[^2541]བྱའོ། །

[Block 2723]
འཐབ་ཀྲོལ་གྱི་རྒྱུ་ཉེ་བར་བསྒྲུབ་པ་ལ་གནས་ནས་དབྱུང་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འཐབ་ཀྲོལ་གྱི་རྒྱུ་ཉེ་བར་སྒྲུབ་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ལ་གནས་ནས་དབྱུང་བའི་ལས་བྱ་བ་ཉིད་ཡིན་གྱི་འཐབ་ཀྲོལ་བྱེད་པ་འབའ་ཞིག་ལ་བྱ་བར་མ་ཟད་དེ། །གང་ཞིག་བདེ་ཞིང་གནས་པ་འཐབ་ཀྲོལ་གྱི་རྒྱུ་རྗོད་པར༌[^2542]བྱེད་གང་ཞིག་དགེ་སློང་མ་རྣམས་ཀྱིས་གནས་ནས་དབྱུང་བའི་ལས་བྱས་པ་སྟེ། དེ་ལྟ་བས་ན་མདོ་འདི་བྱས་སོ། །

[Block 2724]
དགེ་སློང་མའི་རྣམ་པར་འབྱེད་པ་ལས།

[Block 2725]
དེ་དང་འོག་མ་གཉིས་ཀྱི་ཡང་གཞུང་ནི་དེ་ཉིད་དོ། །

[Block 2726]
དགེ་སློང་མ་རྣམས་དང་འདྲེ་ཞིང་གནས་པ་ལ་ཡང་གནས་ནས་དབྱུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གང་དག་དགེ་སློང་མ་རྣམས་དང་ལྷན་ཅིག་འདྲེ་ཞིང་གནས་པ་ལ་འབད་པས་བཟློག་ཀྱང་མི་གཏོང་ན་དེ་ལ་ཡང་གནས་ནས་དབྱུང་བར་བྱའི་གཞན་ལ་བྱ་བ༌[^2543]འབའ་ཞིག་ཏུ་མ་ཟད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2727]
འདིས་གནས་ནས་དབྱུང་བ་ལ་དགེ་སློང་མས་ཕྱག་བྱ་བའི་འོས་མ་ཡིན་པའི་སྡོམ་པ་བྱའོ་ཞེས་བྱ་བ་ལ། འདིས་ཞེས་བྱ་བ་འདི་དགེ་སློང་མ་དང་འདྲེ་ཞིང་གནས་པའི་བདག་ཉིད་ཀྱིས་རྒྱུ་འདིས་གནས་ནས་ཕྱུང་བའི་དགེ་སློང་ལ་དགེ་སློང་མ་རྣམས་ཀྱིས་ཕྱག་བྱ་བའི་འོས་མ་ཡིན་པའི་སྡོམ་པ་བྱའོ། །

[Block 2728]
དགེ་སློང་མ་རྣམས་ལ་ནི་ལོག་པར་རྟོག་པ་འདི་ཡོད་པ་དེ་བས་ན་འཐབ་ཀྲོལ་དང་བསྐྲད་པ༌[^2544]ལ་སོགས་པའི་ལོག་པར་རྟོག་པ་ལ་དགེ་སློང་གནས་ནས་ཕྱུང་བ་ཉིད་ལ་བྱ་བ་ཉིད༌[^2545]དེ་ནི་དཔེ་ཙམ་དུ་ཤེས་པར་བྱའོ། །

[Block 2729]
དགེ་སློང་གི་དགེ་འདུན་གྱིས་དགེ་སློང་མ་སྤངས་པ་ལ་དགེ་སློང་མའི་དགེ་འདུན་གྱི༌[^2546]ལན་གདབ་པར་མི་རིགས་སོ། །

[Block 2730]
དེ་བས་ན་དགེ་སློང་མས་དགེ་སློང་ལ་སྐུར་བར་བྱ་བ་མ་ཡིན་པ་དང་། དགེ་སློང་མས་དགེ་སློང་ལ་འཐབ་ཀྲོལ་བྱེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལྕི་བའི་ཆོས༌[^2547]རྗེས་སུ་འབྲངས་པས་ཐོབ་པའོ། །

[Block 2731]
དེ་བས་ན་གནས་ནས་དབྱུང་བ་ཉིད་ལ་སྡོམ་པ་འདི་བྱ་བ་ཉིད་ཤེས་པ་འདིའོ། །

[Block 2732]
ནན་ཏུར་གྱི་རྒྱུ་གཞན་ལ་དེའི་དོན་དུ་བསམ་པ༌[^2548]གཞན་བྱེད་པ་ནི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་ནན་ཏུར་གྱི་རྒྱུ་གཞན་ཡོད་པ་ལ་དེའི་དོན་དུ་བསམ་པ་ཞེས་བྱ་བ་ནི་གང་གི་རྒྱུ་དེ་ཉེ་བར་གནས་པ་དེའི་བདག་ཉིད་རང་གི་ངོ་བོར་གྱུར་པའི་དོན་གང་ཡིན་པ་དེ་ནི་ནན་ཏུར་གཞན་གྱི་མིང་གིས་བསམ་པ་གང་ཡིན་པ་དེ་ནི་དེའི་དོན་དུ་བསམས་པ༌[^2549]སྟེ། ནན་ཏུར་གྱི་རྒྱུ་ཉེ་བར་གནས་པ་དེའི་དོན་ཏོ། །

[Block 2733]
གལ་ཏེ་བསྡིགས་པའི་ནན་ཏུར་གྱི་རྒྱུ་ཉེ་བར་གྱུར་པ་དེའི༌[^2550]དོན་དུ་བསམས་པས༌[^2551]བསྐྲད་པ་ལ་སོགས་པའི་མིང་གི་ནན་ཏུར་གྱི་ལས་བྱེད་ན་དེ་ལྟར་ན་ཡང་བསྡིགས་པའི་ནན་ཏུར་གྱི་ལས་ཉིད་འཆགས་པར་འགྱུར་རོ། །

[Block 2734]
གཞན་དུ་ན་མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་དེའི་མིང་གི༌[^2552]དོན་འདོད་པ་ཉིད་དུ་མི་སེམས་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2735]
འཐབ་ཀྲོལ་བྱེད་པ་ཉིད་ལ་སྐྲོད་པར་བྱེད་པའི་ལས་བྱེད་པ་ལ་གལ་ཏེ་འཐབ་ཀྲོལ་བྱེད་པ་ཉིད་སྐྲོད་པར་བྱེད་པའི་ཡིད༌[^2553]ཅན་གྱི་དོན་ལ་དགོངས་ནས་སྐྲོད་པར་བྱེད༌[^2554]ན་བསྐྲད༌[^2555]པར་བྱ་བ་དེ་འབྱུང་ངོ་། །གལ་ཏེ་ཁྱིམ་སུན་འབྱིན་པ་ཉིད་ཀྱི་དོན་ལ་དོགས་ནས་འཐབ་ཀྲོལ་བྱེད་པའི་རྒྱུ་ཡོད་པ་ལ་སྐྲོད་པའི་ལས་བྱེད་ན། དེས་ན་ལས་དེ་འབྱུང་བར་མི་འགྱུར་རོ། །
--- END BLOCKS ---
