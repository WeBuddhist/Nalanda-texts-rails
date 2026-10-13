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
[Block 3501]
ཡོངས་སུ་ཉམས་པ་སྲིད་པའི་ཕྱིར་མི་སྐྱེ་བ་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 3502]
ཅི་མི་གཡོ་བའི་ཆོས་ཅན་ལ་དེ་མི་སྐྱེ་བ་ཁོ་ན་ཡིན་ནམ་ཞེ་ན། དེ་ནི་དགྲ་བཅོམ་ཐམས་ཅད་ལ། །མི་གཡོ་བའི༌[^1380]ཆོས་ཅན་ལ་ཡང་རེས་འགའ་མི་སྐྱེ་བ་ཤེས་པ་ལས་མི་སྐྱེ་བ་ཤེས་པ་ཁོ་ན་སྐྱེ་ལ། རེས་འགའ་མི་སློབ་པའི༌[^1381]ཡང་དག་པའི་ལྟ་བ་སྐྱེའོ། །

[Block 3503 [HEADING]]
#### དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ། ^6-2-5-0

[Block 3504]
གང་དག་འབྲས་བུ་བཞིར་བཤད་པ་དེ་དག་གང་གི་འབྲས་བུ་ཡིན་ཞེ་ན། དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་ཡིན་ནོ། །

[Block 3505]
དགེ་སྦྱོང་གི་ཚུལ་ཞེས་བྱ་བ་འདི་ཅི་ཞིག་ཅེ་ན། དགེ་སྦྱོང་ཚུལ་ནི་དྲི་མེད་ལམ། །དགེ་སྦྱོང་གི་ཚུལ་ནི་ཟག་པ་མེད་པའི་ལམ་ཡིན་ནོ། །

[Block 3506]
དེས་ཉོན་མོངས་པ་ཞི་བར་བྱེད་པའི་སྒོ་ནས་དགེ་སྦྱོང་དུ་འགྱུར་རོ། །

[Block 3507]
དགེ་སྦྱོང་གི་ཚུལ་དེའི་འབྲས་བུ་འདི་དག་ཁོ་ན་མ་ཡིན་གྱི་དེ་ཅི་ཞེ་ན།

[Block 3508 [VERSE]]
འབྲས་བུ་འདུས་བྱས་འདུས་མ་བྱས། །
དེ་དག་བརྒྱད་ཅུ་རྩ་དགུའོ། །
གྲོལ་ལམ་ཟད་པ་རྣམས་དང་བཅས། །

[Block 3509]
མཐོང་བས་སྤང་བར་བྱ་བ་སྤོང་བར་བྱེད་པའི་རྣམ་པར་གྲོལ་བའི་ལམ་བརྒྱད་དང་། བསྒོམ་པས་སྤང་བར་བྱ་བ་སྤོང་བ་རེ་རེ་ཞིང་ཡང་ཉོན་མོངས་པ་རྣམ་པ་དགུ་དགུ་སྤོང་བར་བྱེད་པའི་དེ་སྙེད་ཁོ་ནའི་རྣམ་པར་གྲོལ་བའི་ལམ་དག་ནི་དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་འདུས་བྱས་པ་དག་ཡིན་ནོ། །

[Block 3510]
ཉོན་མོངས་པ༌[^1382]དེ་དག་གི་སྤངས་པ་ནི་འབྲས་བུ་འདུས་མ་བྱས་པ་དག་ཡིན་ནོ། །

[Block 3511]
འོ་ན་སྔར་གྱི་དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་བཞི་བཤད་པ་ཇི་ལྟར་ཞེ་ན། དེ་དག༌[^1383]ལ་ནི་འགལ་བ་མེད་དེ། གང་གི་ཕྱིར།

[Block 3512 [VERSE]]
འབྲས་བུ་བཞི་རྣམ་གཞག་པ་ནི། །
རྒྱུ་ལྔ་དག་ནི་སྲིད་ཕྱིར་རོ། །

[Block 3513]
འདི་ལྟ་སྟེ།

[Block 3514 [VERSE]]
འབྲས་ལ་སྔོན་ལམ་བཏང་བ་དང་། །
གཞན་ཐོབ་པ་དང་ཟད་བསྡོམས་དང་། །
ཤེས་པ་བརྒྱད་མཚན་ཐོབ་པ་དང་། །
རྣམ་པ་བཅུ་དྲུག་ཐོབ་པའོ། །

[Block 3515]
ལམ་སྔ་མ་བཏང་བ་དང་སྔོན་མེད་པའི་ལམ་ཐོབ་པ་ནི་ཞུགས་པ་དང་འབྲས་བུའི་ལམ་བཏང་བ་དང་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 3516]
སྤངས་པ་བསྡོམས་པ༌[^1384]དང་། ཐམས་ཅད་ཀྱི་བྲལ་བ་གཅིག་གི་ཐོབ་པ་རྙེད་པའི་ཕྱིར་རོ། །ཤེས་པ་བརྒྱད་ཅིག་ཅར་དུ་ཐོབ་པ་ནི་ཆོས་དང་རྗེས་སུ་ཤེས་པ་རྣམ་པ་བཞིའོ། །

[Block 3517]
རྣམ་པ་བཅུ་དྲུག་ཐོབ་པ་ནི་མི་རྟག་པ༌[^1385]ལ་སོགས་པའི་རྣམ་པ་དག་གོ། །

[Block 3518]
རྒྱུ་ལྔ་པོ་དེ་དག་ཡིན་ཏེ། གང་དག་གི༌[^1386]འབྲས་བུ་བཞིར་རྣམ་པར་གཞག་པ་གསུངས་པའོ། །

[Block 3519]
གལ་ཏེ་ཟག་པ་མེད་པའི་ལམ་ཁོ་ན་དགེ་སྦྱོང་གི་ཚུལ་ཡིན་ན་འཇིག་རྟེན་པའི་ལམ་གྱིས་ཐོབ་པའི་འབྲས་བུ་གཉིས་ཇི་ལྟར་དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུར་རུང་ཞེ་ན།

[Block 3520 [VERSE]]
འཇིག་རྟེན་པ་ཡིས་ཐོབ་འབྲས་ནི། །
བསྲེས་དང་ཟག་མེད་ཐོབ་འཛིན་ཕྱིར། །

[Block 3521]
དེ་ལ་མཐོང་བའི་ལམ་གྱིས་འབྲས་བུ་སྤངས་པ་ཡང་དེར་བསྲེ་བར་བྱ་སྟེ། ཐམས་ཅད་ཀྱི་ཐོབ་པ་དེའི་འབྲས་བུ་བསྡུས་པ་གཅིག་རྙེད་པའི་ཕྱིར་རོ། །གང་ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་གང་ཞེ་ན། ཀུན་དུ་སྦྱོར་བ་གསུམ་སྤངས་པ་དང་། འདོད་ཆགས་དང་། ཞེ་སྡང་དང་། གཏི་མུག་རྣམས་བསྲབས་པ་གང་ཡིན་པ་དེ་ཡིན་ནོ། །

[Block 3522]
ཕྱིར་མི་འོང་བའི་འབྲས་བུ་གང་ཞེ་ན། ཀུན་དུ་སྦྱོར་བ་ཐ་མའི་ཆ་དང་མཐུན་པའི་ལྔ་སྤངས་པ་གང་ཡིན་པ་དེ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 3523]
ཟག་པ་མེད་པའི་བྲལ་བ༌[^1387]ཐོབ་པས་ཀྱང་། སྤངས་པ་དེ་འཛིན་པར་ཡང་བྱེད་དེ། དེའི་སྟོབས་ཀྱིས་ཡོངས་སུ་ཉམས་པ་མི་འཆི་བའི་ཕྱིར་རོ། །

[Block 3524]
འདིའི་ཕྱིར་ཡང་འདི་དགེ་སྦྱོང་གི་འབྲས་བུ་ཉིད་དུ་རིགས་སོ། །

[Block 3525]
དགེ་སྦྱོང་གི་ཚུལ་དུ་བཤད་པ་གང་ཡིན་པ།

[Block 3526 [VERSE]]
དེ་ཉིད་ཚངས་ཚུལ་ཚངས་པ་ཡི། །
འཁོར་ལོ་ཚངས་པས་བསྐོར་ཕྱིར་རོ། །

[Block 3527]
བཅོམ་ལྡན་འདས་ནི་ཚངས་པའི་ཚུལ་བླ་ན་མེད་པ་དང་ལྡན་པའི་ཕྱིར་ཚངས་པ་ཡིན་ཏེ། འཁོར་ལོ་འདི་ནི་དེའི་ཡིན་པས་ན་ཚངས་པའི་སྟེ། དེས་བསྐོར་བའི་ཕྱིར་རོ། །

[Block 3528]
ཆོས་ཀྱི་འཁོར་ལོ་མཐོང་བའི་ལམ་རྒྱུ་བས་ན་འཁོར་ལོའོ། །

[Block 3529]
དེ་དང་ཆོས་མཐུན་པའི་ཕྱིར་མཐོང་བའི་ལམ་ནི་ཆོས་ཀྱི་འཁོར་ལོ་ཡིན་ནོ། །

[Block 3530]
འདིའི་ཆོས་མཐུན་པ་ཇི་ལྟ་བུ་ཞེ་ན། མྱུར་བར་འགྲོ་སོགས༌[^1388]རྩིབས་སོགས་ཕྱིར། །མྱུར་དུ༌[^1389]འགྲོ་བའི་ཕྱིར་དང་། འདོར་བ་དང་འཇུག་པའི་ཕྱིར་དང་། [^1390]མ་རྒྱལ་བ་ལས་རྒྱལ་བར་བྱེད་པའི་ཕྱིར་དང་། རྒྱལ་བ་རྣལ་དུ་འགོད་པའི་ཕྱིར་དང་། འཕར་བ་དང་འབབ་པའི་ཕྱིར་ཏེ། མྱུར་བར་འགྲོ་བ་ལ་སོགས་པ་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3531]
རྩིབས་ལ་སོགས་པ་དང་ཆོས་མཐུན་པའི་ཕྱིར་འཁོར་ལོ་ཞེས་བྱ་སྟེ། ཡང་དག་པའི་ལྟ་བ་དང་། རྟོག་པ་དང་། རྩོལ་བ་དང་། དྲན་པ་ནི་རྩིབས་ལྟ་བུ་ཡིན་ནོ། །

[Block 3532]
ཡང་དག་པའི་ངག་དང་། ལས་ཀྱི་མཐའ་དང་། འཚོ་བ་རྣམས་ནི་ལྟེ་བ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3533]
ཏིང་ངེ་འཛིན་ནི་མུ་ཁྱུད་ལྟ་བུ་ཡིན་ནོ། །

[Block 3534]
ཡང་ཁམས་གང་དུ་དགེ་སྦྱོང་གི་ཚུལ་གྱི༌[^1391]འབྲས་བུ་ཐོབ་ཅེ་ན། འདོད་པར་གསུམ་ཐོབ། གསུམ་པོ་ནི་འདོད་པའི་ཁམས༌[^1392]ཁོ་ནར་འཐོབ༌[^1393]པོ། །ཐ་མ་ནི་གསུམ་དུའོ། །

[Block 3535]
དགྲ་བཅོམ་པ་ཉིད་ནི་ཁམས་གསུམ་དུ་འཐོབ་པོ། །རེ་ཞིག་འབྲས་བུ་གཉིས་ནི་འདོད་ཆགས་དང་མ་བྲལ་བས༌[^1394]ཐོབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་གོང་མར་མི་ཐོབ་པར་ཡང་རིགས་པ༌[^1395]ན་གསུམ་པ་གོ༌[^1396]ཅིའི་ཕྱིར་མི་འཐོབ༌[^1397]ཅེ་ན། གོང་ན་མཐོང་ལམ་མེད། འདོད་པའི་ཁམས་ལས་གོང་ན་ནི་མཐོང་བའི་ལམ་མེད་ལ། དེ་མེད་པར་ཡང་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་ཐོབ་པ་མེད་པས་ཞེས་བྱ་བ་འདི་རེ་ཞིག་རིགས་པ་ཡིན་ནོ། །

[Block 3536]
མི་སྐྱོ་ལུང་ལས་འདིར་རྩོམ་ཞིང་། དེར་མཐར་ཕྱིན་ཞེས་འབྱུང་ཕྱིར་རོ། །

[Block 3537]
གཟུགས་ན་སྤྱོད་པའི་སོ་སོའི་སྐྱེ་བོ་རྣམས་ནི་སྙོམས་པར་འཇུག་པའི་བདེ་བ་ལ་ཆགས་པའི་ཕྱིར་དང་། ཀུན་དུ་མི་སྐྱོ་བའི་ཕྱིར་རོ། །

[Block 3538]
ཕྱིར་མི་འོང་བ༌[^1398]ལྔ་ནི་འདི༌[^1399]རྩོམ་པ་ནི་ལམ་རྩོམ་པ་སྟེ་དེར་མཐར་ཕྱིན་པར་འགྱུར་རོ། །

[Block 3539]
དེ་བས་ན་དེ་ལ་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་མེད་དེ།[^1400] །འདི་སྐད་དུ།

[Block 3540 [VERSE]]
གལ་ཏེ་མི་གཡོའི་ཟད་ཤེས་ལས། །
མི་སྐྱེའི་བློ་གྲོས་ཞེས་བཤད་དེ། །
--- END BLOCKS ---
