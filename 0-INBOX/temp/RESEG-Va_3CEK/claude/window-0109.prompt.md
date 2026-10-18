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
[Block 3816]
ལྷག་མ་ཡང་གང་ཞིག་ཅེ་ན། འདོད་པའི་ཁམས་ལས་འདོད་ཆགས་དང་བྲལ་བའི་རྣམ་པར་གྲོལ་བའི་ལམ་དགུ་པ་དང་། ས་བདུན་ལས་འདོད་ཆགས་དང་བྲལ་བ་དང་། མངོན་པར་ཤེས་པ་དང༌[^2677]སྤེལ་མར་བསྒོམ་པ༌[^2678]དག་གིས༌[^2679]རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་དང་། མི་གཡོ་བ་རྟོགས་པར་བྱེད་པའི་རྣམ་པར་གྲོལ་བའི་ལམ་བརྒྱད་དང་། འདོད་ཆགས་དང༌[^2680]བྲལ་བའི་སྦྱོར་བ་དང་། ཁྱད་པར་ཅན་གྱི་ལམ་ཐམས་ཅད་དེ། དེ་དག་ཐམས་ཅད་ལ་ནི་ཟད་པ་དང་། མི་སྐྱེ་བ་ཤེས་པ་མ་གཏོགས་པ༌[^2681]ཤེས་པ་བརྒྱད་མ་འོངས་པ་འཐོབ་པས་འཐོབ་པ༌[^2682]སྟེ། སློབ་པ་ནི་དེ་ལྟ་བུ་ཡིན་ནོ། །

[Block 3817 [HEADING]]
#### མི་སློབ་པ། ^4-9-5-0

[Block 3818]
མི་སློབ་པའི་མངོན་པ༌[^2683]ཤེས་པ་ལ་སོགས་པའི་སྦྱོར་བ་དང་། རྣམ་པར་གྲོལ་བ་དང་། ཁྱད་པར་ཅན་གྱི་ལམ་རྣམས་ལ་ཤེས་པ་དགུའམ་བཅུ་འཐོབ་པོ། །མངོན་པར་ཤེས་པ་དང་སྤེལ་མར་བསྒོམ་པའི་བར་ཆད་མེད་པའི་ལམ་རྣམས་ལ་ནི་བརྒྱད་དམ་དགུ་འཐོབ་པོ། །མངོན་པར་ཤེས་པའི་རྣམ་པར་གྲོལ་བའི་ལམ་གཉིས་ནི་ལུང་དུ་མ་བསྟན་པའི་ཕྱིར་མ་འོངས་པ་ཅུང་ཟད་ཀྱང་མི་འཐོབ་བོ། །

[Block 3819 [HEADING]]
#### སོ་སོའི་སྐྱེ་བོ། ^4-9-6-0

[Block 3820]
སོ་སོའི་སྐྱེ་བོ༌[^2684]ནི་འདོད་པ་དང་། བསམ་གཏན་གསུམ་ལས་འདོད་ཆགས་དང་བྲལ་བའི་རྣམ་པར་གྲོལ་བའི་ལམ་ཐ་མ་རྣམས་དང་། བསམ་གཏན་གྱི་ས་པ་དག་གི་སྦྱོར་བ་རྣམས་དང་། མངོན་པར་ཤེས་པ་གསུམ་གྱི་རྣམ་པར་གྲོལ་བའི་ལམ་རྣམས་དང་། ཚད་མེད་པ་ལ་སོགས་པའི་ཡོན་ཏན་མངོན་པར་སྒྲུབ་པ༌[^2685]རྣམས་ལ༌[^2686]ཀུན་རྫོབ་ཤེས་པ་མ་འོངས་པ་དང་། ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་དག་གི་སྦྱོར་བ་རྣམས་དང་། མངོན་པར་ཤེས་པ་གསུམ་གྱི༌[^2687]རྣམ་པར་གྲོལ་བ་མ་གཏོགས་པ་ཕ་རོལ་གྱི་སེམས་ཤེས་པ་ཡང་འཐོབ་བོ། །

[Block 3821]
དེ་དག་ལ་ནི་གཞན་གྱི་སེམས་ཤེས་པ་ཡང༌[^2688]མི་འཐོབ་སྟེ། མཐོང་བའི་ལམ་གྱི་འཁོར་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3822]
སྔོན་མེད་པའི་ལམ་ཐོབ་པ༌[^2689]གཞན་ལ་ནི་ཀུན་རྫོབ་ཤེས་པ་ཁོ་ན་མ་འོངས་པ་འཐོབ་བོ། །

[Block 3823 [HEADING]]
### ས་དུ་པའི་ཤེས་པ་འཐོབ་པ། ^4-10-0

[Block 3824]
ཡང་ལམ་གང་ལ་ས་དུ་པའི་ཤེས་པ་ཐོབ༌[^2690]ཅེ་ན། རེ་ཞིག་ཀུན་རྫོབ་ཤེས་པ་ནི༌[^2691]ལམ་ས་གང་པའི༌[^2692]ཡིན་པ་དང་།

[Block 3825]
དང་པོ་ཉིད་དུ་ས་གང་འཐོབ་པ་ས་དེ་པའི་མ་འོངས་པ༌[^2693]འཐོབ་བོ། །

[Block 3826]
ཟག་པ་མེད་པའི་ལམ་གང༌[^2694]ཡིན་པ་འབའ་ཞིག་ཏུ་ཡང་མ་ཟད་དོ། །

[Block 3827]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན།

[Block 3828 [VERSE]]
གང་ལས་ཆགས་བྲལ་བྱ་ཕྱིར་གང་། །
འཐོབ་པ་དེར་ཡང་འོག་མའང༌[^2695]འཐོབ། །

[Block 3829]
ས་གང་ལས་འདོད་ཆགས་དང་བྲལ༌[^2696]བ་ལ་ཡང་ལམ་ཡང་སྦྱོར་བའི་ལམ་ལ་སོགས་པ་རྣམ་པ་གཉིས་ཡིན་ལ། འདོད་ཆགས་དང་བྲལ་བ་ས་གང་ཞིག་ཐོབ་པ༌[^2697]དེའི་ས་པ་དང་ས་འོག་མ་པའི་ཟག་པ་མེད་པའི་ཤེས་པ་རྣམས་འཐོབ་པར་འགྱུར་རོ། །

[Block 3830]
ཟད་པ་ཤེས་ལ་ཟག་བཅས་ཀྱང་། །ས་ཀུན་ཟད་པ་ཤེས་པ་ལ་ནི་ཟད་པ་ཤེས་པས་འཐོབ་པ་ཟག་པ་དང་བཅས་པའི་ཡོན་ཏན་མི་སྡུག་པ་དང་། དབུགས་འབྱུང་བ་དང་། རྔུབ་པ་རྗེས་སུ་དྲན་པ་དང་། དྲན་པ་ཉེ་བར་གཞག་པ་དང་། ཚད་མེད་པ་དང་། རྣམ་པར་ཐར་པ་ལ་སོགས་པ་ས་ཐམས་ཅད་སྤྲོག་མ་ཐག་པ་བཅད་དེ། དབུགས་ཕྱིན་པ་ལྟ་བུ་དང་། ཆོས་མཐུན་པ་འཐོབ་སྟེ། རྒྱལ་སྲིད་ཆེན་པོ་ཐོབ་ན། ཡུལ་གྱི་མི་རྣམས་ཀྱིས༌[^2698]དབུལ་བར་བྱ་བས༌[^2699]བསུ་བ་བཞིན་དུ་རང་གི་སེམས་ལ་རྒྱལ་སྲིད་ཆེན་པོ་ཉིད་འཐོབ་པ་ལ་དགེ་བའི་ཆོས་ཐམས་ཅད་འཐོབ་པ་རྣམས་ཀྱིས་བསུ་བའི་ཕྱིར་རོ། །

[Block 3831 [HEADING]]
### འཐོབ་པ་རྣམ་པ་བཞི། ^4-11-0

[Block 3832]
གང་ཅི་རྙེད་པ་དེ་ཐམས་ཅད་འཐོབ་བམ་ཞེ་ན། སྨྲས་པ། གང་སྔོན་མེད་པ་ལས་རྙེད་པ་ཡིན་པས། དེ་ཐམས་ཅད་ནི་འཐོབ་ཀྱི། སྔོན་རྙེད་ཟིན་པ་ནི་མི་འཐོབ་བོ། །

[Block 3833]
གང་རྣམ་པར་ཉམས་པ་ལས་ཡང་རྙེད་པ་དེ་ཡང་མི་འཐོབ་སྟེ། ཐོབ་པ༌[^2700]བཏང་བའི་ཕྱིར་རོ། །ཅི་འཐོབ་པ་རྙེད་པ་ཁོ་ན་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 3834]
འཐོབ་པ་ནི་རྣམ་པ་བཞི་སྟེ། ཉེན་པ༌[^2701]འཐོབ་པ་དང་། བསྟེན་པ༌[^2702]འཐོབ་པ་དང་། གཉེན་པོ་འཐོབ་པ་དང་། ཐག་བསྲིང་བ་འཐོབ་བའོ། །

[Block 3835]
དེ༌[^2703]ལ་རྙེད་པ་དང་བསྟེན༌[^2704]ཅེས་བྱ་བ་ནི། དགེ་བ་འདུས་བྱས་འཐོབ་བོ།[^2705] །གཉེན་པོ་དང་ནི་ཐག་བསྲིང་བའི།[^2706] །འཐོབ་པ་ཟག་དང་བཅས་པའི་ཡིན། །རྙེད་པ་དང་བསྟེན་པ༌[^2707]འཐོབ་པ་དག་ནི་དགེ་བ་འདུས་བྱས་རྣམས་ཀྱི་ཡིན་ཏེ། མ་འོངས་པ་རྣམས་ཀྱི་ནི་གཅིག་གོ། །

[Block 3836]
ད་ལྟར་བྱུང་བ་རྣམས་ཀྱི་ནི་གཉི་གའོ།[^2708] །གཉེན་པོ་དང་ཐག་བསྲིང་བ་འཐོབ་པ་དག་ནི། ཟག་པ་དང་བཅས་པའི་ཆོས་རྣམས་ཀྱི་ཡིན་ཏེ། དེ་ལྟར་ན་དགེ་བ༌[^2709]ཟག་པ་དང་བཅས་པ་རྣམས་ཀྱི་ནི་འཐོབ་པ་བཞི་ཡིན་ནོ། །

[Block 3837]
ཟག་པ་མེད་པ་རྣམས་དང་། ཉོན་མོངས་པ་ཐམས་ཅད་དང་། ལུང་དུ་མ་བསྟན་པ་རྣམས་ཀྱི་ནི་གཉིས༌[^2710]ཡིན་ནོ། །

[Block 3838]
ཆོས་མངོན་པ་པ་ཉི་འོག་པ་རྣམས་ཀྱི་ལྟར་ན་འཐོབ་པ་དྲུག་སྟེ། བཞི་པོ་དེ་དག་དང་། སྡོམ་པ་འཐོབ་པ་དང་། རྣམ་པར་འཇིག་པ་འཐོབ་པའོ། །

[Block 3839]
[^2711]སྔ་མ་ནི་དབང་པོ་རྣམས་ཀྱི་ཡིན་ལ། ཕྱི་མ་ནི་ལུས་ཀྱི་ཡིན་ཏེ།[^2712] དབང་པོ་དྲུག་པོ་འདི་དག་ཤིན་ཏུ་དུལ་བ་དང་། ཤིན་ཏུ་བསྒོམས་པ༌[^2713]ཞེས་བྱ་བའི་བར་དང་། དེ་བཞིན་དུ་ལུས་འདི་ལ་སྐྲ་ཡང་ཡོད་ཅེས་བྱ་བ༌[^2714]རྒྱས་པར་གསུངས་པ་ཡིན་ནོ། །

[Block 3840]
གང་དག་ཁ་ཆེ་བ་རྣམས་ན་རེ་དེ་གཉིས་ནི་གཉེན་པོ་དང་ཐག་བསྲིང་བ་འཐོབ་པའི་ཁོངས་སུ་འདུས་སོ་ཞེས་ཟེར་རོ། །

[Block 3841 [HEADING]]
### སངས་རྒྱས་ཀྱི་ཆོས་མ་འདྲེས་པ་བཅོ་བརྒྱད། ^4-12-0

[Block 3842]
གང་ཟག་ཐམས་ཅད་ཀྱིས་ཟད་པ་ཤེས་པའི་ཚེ།

[Block 3843 [VERSE]]
ཡོན་ཏན་འཐོབ་པའི་ཕྱིར༌[^2715]བཤད་ཀྱི། །
སངས་རྒྱས་ཆོས་ནི་མ་འདྲེས་པ། །
སྟོབས་ལ་སོགས་པ་བཅོ་བརྒྱད་དོ། །

[Block 3844]
གང་དག་སངས་རྒྱས་ཁོ་ནས་ཟད་པ་མཁྱེན་པའི་ཚེ་བརྙེས་པར་འགྱུར་གྱི་གཞན་གྱིས་ནི་མ་ཡིན་པའོ། །

[Block 3845]
བཅོ་བརྒྱད་གང་ཞེ་ན། སྟོབས་བཅུ་དང་། མི་འཇིགས་པ་བཞི་དང་། དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ་དང་། ཐུགས་རྗེ་ཆེན་པོའོ། །

[Block 3846]
ཐུན་མོང་མ་ཡིན་པས་ན་མ་འདྲེས་པ་ཞེས་བྱའོ། །

[Block 3847 [HEADING]]
#### སྟོབས་བཅུ། ^4-12-1-0

[Block 3848 [HEADING]]
##### རང་བཞིན། ^4-12-1-1-0

[Block 3849]
དེ་ལ། གནས་དང་གནས་མིན་ཤེས་པ་བཅུ། །གནས་དང་གནས་མ་ཡིན་པ་མཁྱེན་པའི་སྟོབས་ནི་ཤེས་པ་བཅུ་ཡིན་ནོ། །

[Block 3850]
ལས་འབྲས་ལ་བརྒྱད། ལས་དང་རྣམ་པར་སྨིན་པའམ་མཁྱེན་པའི་སྟོབས་ནི་ཤེས་པ་བརྒྱད་དེ། འགོག་པ་དང་ལམ་ཤེས་པ་དག༌[^2716]མ་གཏོགས་སོ། །

[Block 3851]
བསམ་གཏན་སོགས། དབང་པོ་མོས་དང་ཁམས་ལ་ནི། དགུའོ། །

[Block 3852]
བསམ་གཏན་དང་། རྣམ་པར་ཐར་པ་དང་། ཏིང་ངེ་འཛིན་དང་། སྙོམས་པར་འཇུག་པ་མཁྱེན་པའི་སྟོབས་ནི་ཤེས་པ་དགུ་ཡིན་ཏེ། འགོག་པ་ཤེས་པ་མ་གཏོགས་སོ། །

[Block 3853]
དབང་པོ་མཆོག་དང་མཆོག་མ་ཡིན་པ་མཁྱེན་པའི་སྟོབས་དང་། མོས་པ་སྣ་ཚོགས་མཁྱེན་པའི་སྟོབས་དང་། ཁམས་སྣ་ཚོགས་མཁྱེན་པའི་སྟོབས་ཀྱང་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 3854]
ལམ་དག་ལ་བཅུའམ། འམ་ཞེས་བྱ་བའི་སྒྲ་ནི་དགུ་འམ་ཞེས་ལུགས་ཐ་དད་པའི་དོན་ཏེ། གལ་ཏེ་ལམ་དེ༌[^2717]འབྲས་བུ་དང་བཅས་པར་གཟུང༌[^2718]ན་ནི་ཐམས་ཅད་དུ་འགྲོ་བའི་ལམ་མཁྱེན་པའི་སྟོབས་ཤེས་པ་བཅུའོ།[^2719] །གལ་ཏེ་མ་ཡིན་ན་ནི་དགུ་སྟེ།

[Block 3855 [VERSE]]
འགོག་པ་ཤེས་པ་མ་གཏོགས་སོ། །
གཉིས་ནི་ཀུན་རྫོབ་ཤེས་པ་ཡིན། །
--- END BLOCKS ---
