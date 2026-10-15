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
[Block 3606]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་དབྱུང་བ་ལ་སོགས་པ༌[^2358]ཐུག་པ་མཚན་གྱུར་ཏེ༌[^2359]དགེ་སློང་མར་གྱུར་ན། ཅི་དེས་གཉིས་ཀའི་དགེ་འདུན་ལ་ཟླ་བ་ཕྱེད་མགུ་བ་སྤྱད་པ་སྤྱད་པར་བགྱིད༌[^2360]འཚལ་ལམ། སྤྱད་པར་བྱ་དགོས་སོ། །

[Block 3607]
བཙུན་པ་རེ་ཞིག་དགེ་སློང་མ་གཉིས་ཀའི་དགེ་འདུན་ལ་མགུ་བ་སྤྱོད་པ་མཚན་གྱུར་ཏེ། དགེ་སློང་དུ་གྱུར་ན་ཅི་དེས་དགེ་འདུན་ལ་ཞག་དྲུག་མགུ་བ་སྤྱད་པ་སྤྱད་པར་བགྱིད་འཚལ་ལམ། སྤྱད་པར་བྱ་དགོས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3608]
མདོ་སྔ་མ་ཤོས་ཀྱིས་ནི་ལུས་ཀྱི་ཉེས་པ་བཅབས་པ༌[^2361]ཉམས་པ་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 3609]
ཕྱི་མའི༌[^2362]སྤྱད་པ༌[^2363]ཡང་སྤྱད་པར་བྱ་བ་ཉིད་དོ། །

[Block 3610]
ཡང་གང་གི་ཕྱིར་བྱས་པ་ནི་དེ་ཉིད་ཡིན་ནོ། །

[Block 3611]
ཞིང་མ་ཡིན་པ་ཉིད་ལ་ནི་ཉམས་སོ། །

[Block 3612]
དེའི་ཚེ་ན་འབྱུང་བའི་མཚན་མ་ལོངས་སྤྱོད་པ་རྣམས་ཀྱིས་མཚན་མ་འདི་ལ་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདིར་རྣམས་པར༌[^2364]གཞག་པའོ། །

[Block 3613]
འདི་ལ་ཆོ་ག་རྣམས་གྱུར་ཏོ་ཞེས་བྱ་བ་ལ། འདི་ལ་ཞེས་བྱ་བ་ནི་མཚན་གྱུར་པ་ལའོ། །

[Block 3614]
མཚན་གྱུར་པ་འདི་ལ་ཆོ་ག་སྤྱད་པ་རྣམས་གྱུར་པ་དེའི་ཕྱིར། དེ་དག་རྣམ་པར་གཞག་པར་མཛད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3615]
དེའི་ཚེ་ལུས་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་གི་ཚེ་དེའི༌[^2365]ཚེ་ན་འབྱུང་བའི་གཞིའི་དགོས་པ་དེ་ནི་བདག་ཉིད་གང་ཡིན་པ་དེའི་དབང་གིས་ལྟུང་བ་དང༌[^2366]ལྟུང་བ་མེད་པ་སྐྱེས༌[^2367]པའོ། །

[Block 3616]
འདི་ལྟ་སྟེ་དཔེར་ན་གསད་པར༌[^2368]བྱ་བ་དགྲ་བཅོམ་པ་ཉིད་མ་ཡིན་པའི་གནས་སྐབས་ལ་གསད་པའི༌[^2369]སྦྱོར་བ་བརྩམས་ནས། དགྲ་བཅོམ་པ་ཉིད་ཐོབ་པའི་གནས་སྐབས་སུ་གསད་པའི༌[^2370]མཚམས་མེད་པ༌[^2371]ལས་ཀྱི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ། །

[Block 3617]
སྐྱེས་པའི་ལུས་ལ་རེག་པའི་སྦྱོར་བ་བརྩམས་པ༌[^2372]ན་བུད་མེད་ཉིད་དུ་འགྱུར༌[^2373]ན། དེའི་ལུས་ལ་རེག་པ་ལས་སྙོམས་པར་ཞུགས་པ་ལ་བུད་མེད་ལ་རེག་པའི་ལྟུང་བ་གང་ཡིན་པ་དེ་འགྲུབ་པར་འགྱུར་རོ། །

[Block 3618]
བུད་མེད་ལ་སྦྱར་བར་སྐྱེས་པར་གྱུར་ན། དེར་སྙོམས་པར་ཞུགས་པ་ལས་སྐྱེས་པ་ཉིད་ལ་གང་ཡིན་པ་འདི་དང་། སྐྱེས་པར་གྱུར་པ་ལ་སྦྱར་ནས་བུད་མེད་ཀྱི་གནས་སྐབས་ལ་སྙོམས་པར་ཞུགས་པ་ལ་བུད་མེད་ཉིད་ལ་གང་ཡིན་པ་འདི་བུད་མེད་དུ་གྱུར་པ་ལ་སྦྱར་ཏེ། སྐྱེས་པའི་གནས་སྐབས་སུ་སྙོམས་པར་ཞུགས་པ་དང་། སྐྱེས་པ་ཉིད་ལ་གང་ཡིན་པ་འདི་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 3619]
གཞན་ལས་སྐྱེས་པ་ནི་རང་གི་འགྲོ་བ་ཉིད་མ་ཡིན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འགྲོ་བ་གཞན་མ་ཡིན་པ་ཞིང་དུ་གྱུར་པ་ལས་སྐྱེས་པའམ། གང་གི་འགྲོ་བར་གྱུར་པ་འདི་ནི་སྒྲུབ་པ་དེའི་འགྲོ་བ་ཉིད་མ་ཡིན་པ་དེ་བས་ན། མི༌[^2374]མ་ཡིན་པ་ཉིད་ལས་རང་གིས་ཕྲོགས་པ་ལ་ཕམ་པའོ། །

[Block 3620]
མིའི་འགྲོ་བ་པའི་བདག་ཉིད་དུ་གྱུར་པའམ། དུད་འགྲོ་མོའི་མངལ་ལས་སྐྱེས་པ་ལས་མི་མ་ཡིན་མོ་ཉིད་དོ། །

[Block 3621]
མི་མ་ཡིན་པའི་ངོ་བོ་འདི་ལ་སྦོམ་པོའོ། །

[Block 3622]
དུད་འགྲོའི་བདག་ཉིད་ཅན་ལ་ལྟུང་བྱེད་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 3623]
འགྲོ་བ་གཞན་གྱི་རྣམ་པ་བསྟེན་པ༌[^2375]གསད་པ༌[^2376]ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། རང་གི་འགྲོ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་རྗེས་སྙེག༌[^2377]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 3624]
དཔེར་ན་མི༌[^2378]སྨན་དང་སྔགས་ལ་སོགས་པའི་དབང་གིས་འགྲོ་བ་གཞན་གྱི་ལུས་ཀྱི་རྣམ་པ་བསྟེན་པ༌[^2379]མ་ཡིན་ནོ། །

[Block 3625]
གང་འདི་ལ་སྐྱེ་བ་པོའི་འགྲོ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 3626]
ཡང་དེ་གསད༌[^2380]པ་ལ་ཡང༌[^2381]དུད་འགྲོའི་རྣམ་པ་དང་། མི་མ་ཡིན་པའི་རྣམ་པ་དང་ལྡན་པ་ལ་མིའི་འགྲོ་བ་པ༌[^2382]དེའི་འདུ་ཤེས་ཀྱིས་སོ། །

[Block 3627]
དེའི་ཚེ་འབྱུང་བའི་རྣམ་པར་འགྲོ་བའི༌[^2383]འདུ་ཤེས་ཀྱི་ཡན་ལག་ཉིད་ལས་འགྲོ་བར་འདུ་ཤེས་པ་ལ་དེའི་འགྲོ་བའི་སྟོབས་ཀྱིས་སངས་རྒྱས་ཉིད་དང་དགྲ་བཅོམ་པ་ཉིད་དང་མ་དང་ཕ་ཉིད་ཀྱི་བློ་དང་འདྲ་བར་མཚམས་མེད་པའི་ལས་ལ་ཡན་ལག་མ་ཡིན་པ་ཉིད་ཀྱི༌[^2384]ཕྱིར་མངོན་པར་འདོད་པའི་སྲོག་ཆགས་ཙམ་པོ་ལ་འདིར་ཡན་ལག་ཉིད་ཀྱི་ཕྱིར་ལྟུང་བ༌[^2385]དངོས་གཞིའོ། །

[Block 3628]
སྦྱོར་བ་ནི་མིའི་འགྲོ་བར་འདུ་ཤེས་ན་སྦོམ་པོའོ། །

[Block 3629]
དེའི་ཚེ་ན་འབྱུང་བའི་རྣམ་པའི་འགྲོ་བར་འདུ་ཤེས་པ་ལ། འདུ་ཤེས་ཀྱི་སྦྱོར་བའི་ཡན་ལག་གོ། །

[Block 3630]
དེ་བས་ན་ཉེས་བྱས་སོ། །

[Block 3631]
དུད་འགྲོ་མི་མ་ཡིན་པའི་རྣམ་པ་དང་ལྡན་པ་དུད་འགྲོའི་འདུ་ཤེས་ཀྱིས་དེའི་ཚེ་ན་འབྱུང་བའི་རྣམ་པ་ལ་འགྲོ་བའི་འདུ་ཤེས་ཀྱི་ཡན་ལག་ལས་ལྟུང་བའི་དངོས་གཞིའོ། །

[Block 3632]
སྦྱོར་བའི་སྔོན་རོལ་དུ་ཉེས་བྱས་སོ། །

[Block 3633]
འོག་མ་ལ་ནི་གྲངས་ཇི་ལྟ་བ་བཞིན་དུ་ཉེས་བྱས་དང་སྦོམ་པོའི་ལྟུང་བ་དག་གོ། །

[Block 3634]
མི་མ་ཡིན་པ་དུད་འགྲོའི་རྣམ་པ་དང་། མི་ཡིན༌[^2386]པའི་རྣམ་པ་དང་ལྡན་པ་ལ་མི་མ་ཡིན་པའི་འདུ་ཤེས་ཀྱིས་དེའི་ཚེ་ན་འབྱུང་བའི་རྣམ་པས་གནོད་པར་བྱེད་ཅིང་དངོས་གཞིའི་དུས་ན་སྦོམ་པོ་སྟེ། སྦོམ་པོའི་སྔོན་རོལ་དུ་ནི་ཉེས་བྱས་སོ། །

[Block 3635]
ཕྱི་མ་ལ་ནི་གྲངས་ཇི་ལྟ་བར་ཉེས་བྱས་དང་སྦོམ་པོའོ། །

[Block 3636]
མ་བྱིན་པར༌[^2387]ལེན་པ་དང་། ལུས་ཀྱིས་རེག་པ་དང་སློང་བ་དང་སྟན་རྣམས་ལ་འགྲོ་བའི་འདུ་ཤེས་ཀྱིས་བདག་ཉིད་ཀྱི་གང་ཡིན་པ་དེ་ལ་འགྲོ་བ་གཞན་གྱི་རྣམ་པ་ལ་བརྟེན་དུ་ཟིན་ཀྱང་། འགྲོ་བ་དེ་ཉིད་དུ་རྣམ་པར་གཞག་པར་རྣམ་པར་གནས་པ་ཡིན་ཏེ། དེའི་རང་བཞིན་གྱིས༌[^2388]འདི་ལ་བདག་པོ་ཉིད་ལ་སོགས་པ་དང་བཟའ་བ་དག་ལ་བརྟེན་པའི་ཕྱིར་རོ། །

[Block 3637]
གནས་སྐབས་གཞན་ཐོབ་པ་ནི་གཞན་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། དགྲ་བཅོམ་པ་ལ་སོགས་པའི་གནས་སྐབས་གཞན་ཐོབ་པ་ན། དེའི་རྒྱུད་ནི་གཞན་ཉིད་མ་ཡིན་པ་ནི་སེམས་ཅན་དེ་ལ་སེམས་ཅན་གཞན་ཉིད་མ་ཡིན་ནོ། །

[Block 3638]
སེམས་ཅན་གཞན༌[^2389]དུ་མཐར་ཐུག་པ་མངོན་པར་འདོད་པ་ཡིན་པ་ནི། མཐར་ཐུག་པ་བྱས་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 3639]
དེ་བཞིན་དུ་གནས་སྐབས་གཞན་ལ་སྦྱོར་བ་བྱས་ནས། སྦྱོར་བ་གཞན་གྱི་སྐབས་སུ་མཐར་ཐུག་པ་ཉིད་དོ། །

[Block 3640]
དགྲ་བཅོམ་པ་མ་ཡིན་པའི་གནས་སྐབས་སུ་སྦྱོར་བ་བྱས་ན༌[^2390]དགྲ་བཅོམ་པ་ཉིད་ཐོབ་པ་ནི༌[^2391]གསོད་པར་བྱེད་ན་དེ་ལ་ཕམ་པ་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་པར་འགྲུབ་བོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 3641]
ཉེས་པ་དེ་མེད་པ་ཉིད་ལ་འོང་བ་ནི་ཐ་དད་དོ་ཞེས་བྱ་བ་ནི་དེ་ལ་ནི་དེའི་ལས་ཀྱི་ཉེས་པ་སྐྱེད་པ༌[^2392]མ་ཡིན་པ་དེ་བས་ན་ཉེས་པ་དེ་མེད་པའོ། །

[Block 3642]
དེ་ཉིད་ཀྱི་གནས་སྐབས་ཅན་དུ་གྱུར་པ་ནི་ཐ་དད་པའོ། །

[Block 3643]
གང་ཞིག་དེར་དེའི་ཉེས་པ་ཉིད་ལ་བྱས་པ་དང་། གང་ཡང་དེའི་ཉེས་པ་ཉིད་མ་ཡིན་པ་དང་། གང་ཡང་སླར་དེའི་འོག་ཏུ་ཉེས་པ་དེ་ཡོད་པ༌[^2393]ལས་དེ་དག་ནི་ཕན་ཚུན་ཐ་དད་པར་ཤེས་པར་བྱའི༌[^2394]གཅིག་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 3644]
དུས་མ་ཡིན་པ་ཁོ་ན་སྟན༌[^2395]བརྩམས་ནས་ངལ་སོ༌[^2396]བར་བྱེད་པ་དེ་ཡང་བསྙེན་པར་རྫོགས་པར་བྱས་ནས་དུས་མ་ཡིན་པ་ཁོ་ནར་ཟིན་པར་བྱེད་པའོ། །

[Block 3645]
བུད་མེད་དུ་གྱུར་ནས་ཡང་སྐྱེས་པ་ཉིད་ཐོབ་ན་ཐ་དད་པ་ཉིད་དོ། །
--- END BLOCKS ---
