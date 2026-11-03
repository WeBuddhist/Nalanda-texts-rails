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
[Block 2836]
བསླབ་པའི་གཞི་སྔ་མ་བཅས་པ་ལ་ཡང་འདི་ཐོབ་པའོ། །

[Block 2837]
གནས་སྦྱིན་པ་ལ་ཡང་ལོ་བཅུའི་གནས་ལ་ཡང༌[^1844]ལོ་བཅུ་གཉིས་ལོན་པ་ཉིད་དགེ་སློང་མ་རྣམས་ལ་འདི་ལས་སྐྱེས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2838]
གཞན་གྱིས་གསོལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མི་ནུས་པ་ལོ་བཅུ་གཉིས་མ་ལོན་པས་གནང་བ་འདི་དག་གསོལ་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2839]
འདིར་ཡང་ཚིག་འདི་དག་ཉིད་མདོ་ལས་རྟོགས་པར་བྱའོ། །

[Block 2840]
གང་ཡང་ནུས་པ་ཞེས་བྱ་བ་དེ་འདིར་དངོས་ཀྱི་ཚིག་སྟེ། དོན་གཞན་དང་གཞན་ལས་ཐོབ་པར་བྱེད་པའོ། །

[Block 2841]
གང་ལ་འཁོར་ཉེ་བར་འཇོག་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གནང་བ་མ་ཐོབ་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མ་གང་གིས་སྔར་འཁོར་ཉེ་བར་གཞག་པའི་གནང་བ་མ་ཐོབ་པ་དེ་ལའོ། །

[Block 2842]
འཇུག་པ་གང་ལ་ཅི་ཞིག་བྱ་ན་དེ་ལ་དེར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་འཁོར་ཉེ་བར་འཇོག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སླར་དེ་ཉེ་བར་གཞག་པ་ནི་རབ་ཏུ་འབྱིན་པ་དང་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་དང་། དགེ་སློབ་མར་བྱེད་པ་དང་། གནས་སྦྱིན་པ་ཞེས་བྱ་བ་རྣམ་པ་བཞི་པོ་དག་གིས་ཤེས་པར་བྱ་བ་ཁྱད་པར་མེད་པ་ཉིད་ཀྱི༌[^1845]ཕྱིར་རིག་པར་བྱའོ། །

[Block 2843]
འཁོར་ཉེ་བར་འཇོག་པའི་ལྟུང་བྱེད་དོ། །

[Block 2844]
གང་ལ་འཁོར་མང་པོ་ཉེ་བར་འཇོག་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཅིག་ཤོས་ནི་འཁོར་མང་པོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཉེ་བར་འཇོག་པ་ལའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2845]
སྔར་གནང་བ་མ་ཐོབ་པ་ལའོ་ཞེས་བྱ་བ་དང་། འཁོར་མང་པོ་ཉེ་བར་འཇོག་ནའོ་ཞེས་བྱ་བ་གཉིས་ཀྱང་དོན་གྱིས་བསྒྱུར་ཏེ། འཁོར་མང་པོ་ཉེ་བར་འཇོག་པའི་ལྟུང་བྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2846]
འཁོར་མང་པོ་ཉེ་བར་འཇོག་པའི་ལྟུང་བྱེད་དོ། །

[Block 2847]
གང་ལ་ལོ་བཅུ་གཉིས་མ་ལོན་པར་ཉེ་བར་སྡུད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་སོ་བཟུང་བ་ལོ་བཅུ་གཉིས་ཉིད་ཀྱི་མདུན་རོལ་དུ་བསྙེན་པར་རྫོགས་པར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྔར་བསྙེན་པར་རྫོགས་པའི་ལོ་རྣམས་ཀྱི་དང་པོ་ནི་བཅུ་གཉིས་ཉིད་དོ་ཞེས་བསྟན་པས་དེའི་ཕྱིར། བུད་མེད་ཁྱིམ་སོ་བཟུང་བ་བག་མར་བཏང་བ་ནི་ན་ཚོད་བཅུ་གཉིས་ལོན་པའི་མདུན་རོལ་དུ་བསྙེན་པར་རྫོགས་པར་བྱེད་ན་ལྟུང་བྱེད་དུ་འགྱུར་རོ། །

[Block 2848]
ལོ་བཅུ་གཉིས་མ་ལོན་པར་བསྙེན་པར་རྫོགས་པར་བྱེད་པའི་ལྟུང་བྱེད་དོ། །

[Block 2849]
གཞན་དུ་གང་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གཞན་ནི་ལོ་ཉི་ཤུའི་འོ༌[^1846]ཞེས་བྱ་བ་སྨོས་ཏེ། མདུན་རོལ་དུ་བསྙེན་པར་རྫོགས་པར་བྱེད་ན་ཉེ་བར་ལྟུང་བའོ། །

[Block 2850]
ལོ་ཞེས་སྨོས་པ་ནི་ལོ་རྣམས་ནི་ལོ༌[^1847]སྟེ་ཞེས་བྱ་བ་དོན་གྱིས་ཉེ་བར་བསྒྱུར་བ་ལ༌[^1848]ཉེ་བར་ལྟུང་བའོ། །

[Block 2851]
ཁྱིམ་སོ་བཟུང་བ་ལས་གཞན་པའི་ཁྱིམ་སོ་མ་བཟུང་བ་ནི་ན་ཚོད་ལོ་ཉི་ཤུ་ལོན་པའི་མདུན་རོལ་དུ་བསྙེན་པར་རྫོགས་པར་བྱེད་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2852]
འདིས་ནི་བྱེ་བྲག་ཙམ་བསྟན་པ་ཡིན་ཏེ། འདི་ལས་གཞན་པ་ཐམས་ཅད་འདི་དག་གི༌[^1849]བསྙེན་པར་རྫོགས་པའི་དངོས་པོ་ལྟུང་བྱེད་དུ་བསྒྲུབ་པར་རྟོགས་པར་ཤེས་པར་བྱའོ། །

[Block 2853]
ལོ་ཉི་ཤུ་མ་ལོན་པར༌[^1850]བསྙེན་པར་རྫོགས་པར་བྱེད་པའི་ལྟུང་བྱེད་དོ། །

[Block 2854]
གང་ལ་ཚིག་ལས་བཟླས་པའི་ལྟུང་བྱེད་གཉིས་སུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བསླབ་པ་མ་བྱིན་པ་གཉིས་མཁན་པོ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱིམ་སོ་བཟུང་བ་དང་བསླབ་པ་གནང་བ༌[^1851]མ་བྱིན་པ་ཉིད་མཁན་མོ༌[^1852]ཉིད་ཀྱིས་བསྙེན་པར་རྫོགས་པར་བྱེད་ན་ལྟུང་བྱེད་གཉིས་སུ་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 2855]
སྦོམ་དགའ་མོས་བུད་མེད་ཁྱིམ་སོ་བཟུང་བ་ལོ་བཅུ་གཉིས་ལོན་པ་ཞིག་དང་།

[Block 2856]
ཁྱིམ་སོ་མ་བཟུང་བ་ལོ་ཉི་ཤུ་ལོན་པ་གཅིག་བསླབ་པའི་སྡོམ་པ་མ་བྱིན་པར་བསྙེན་པར་རྫོགས་པར་བྱས་པ་ལས།

[Block 2857]
བསླབ་པའི་གཞི་གཉིས་སོ་སོར་བཅའ་བ་མཛད་པ་གང་ཡིན་པ་དེ་ལ༌[^1853]སྐྱེས་པའི་དབང་གིས་ཡུལ་ཐ་དད་པ་ལ་བརྟེན་ནས་བཅའ་བ་གཉིས་མཛད་པ་ཡིན་ནོ། །

[Block 2858]
དེའི་རྗེས་སུ་འགྲོ་བས་བསླབ་པའི༌[^1854]གཞི་གཉིས་བསྟན་པ་མཛད་པ་འདི་ཡུལ་ཐ་དད་པ༌[^1855]ལ་བརྟེན་པའོ། །

[Block 2859]
བུད་མེད་ལ་ནི་ཚིགས་གསུམ་ཡོད་དེ། དགེ་ཚུལ་མ་ཉིད་དང་། དགེ་སློབ་མ་ཉིད་དང་། དགེ་སློང་མ་ཉིད་རྣམས་སོ། །

[Block 2860]
དེ་ལྟ་བས་ན་ཚིགས་གཅིག་ལས་འདས་པར༌[^1856]འགྱུར་བ་ཞེས་བྱ་བ་དོན་གྱིས་འདི་དག་ལ་མིང་དང་ཚིགས་ལས་འདའ་བར་བྱེད་པ་ཞེས་བྱ་བའོ། །

[Block 2861]
ཚིགས་ལས་འདས་པའི་ལྟུང་བྱེད་གཉིས་སོ། །

[Block 2862]
གང་ལ་སྤྱད་པ་ལས་འདའ་བར་བྱེད་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དེ་ལས་མ་སྤྱད་པ༌[^1857]ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསླབ་པ་འདི་ལ་ལོ་གཉིས་སུ་ཇི་ལྟར་བྱས་པའི་མ་སྤྱད་པ༌[^1858]ཉིད་ལ་མཁན་མོ་ཉིད་ཀྱིས་བསྙེན་པར་རྫོགས་པར་བྱེད་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2863]
བསླབ་པའི་གཞི་འདི་ནི་སྦོམ་དགའ་མོས་གཞོན་ནུ་མ་ལོ་བཅོ་བརྒྱད་ལོན་པ་རབ་ཏུ་ཕྱུང་སྟེ། ལོ་གཉིས་སུ་དགེ་སློབ་མའི་བསླབ་པའི་སྡོམ་པ་བྱིན་ནས་ལོ་གཉིས་མ་ལོན་པ་ཁོ་ནར་བསྙེན་པར་རྫོགས་པར་བྱས་པ་ལས་བཅས་པ་ཡིན་ནོ། །

[Block 2864]
བསླབ་པ་ལ་མ་བསླབས་པ༌[^1859]བསྙེན་པར་རྫོགས་པར་བྱེད་པའི་ལྟུང་བྱེད་དོ། །

[Block 2865]
གང་ལ་གཞན་བསླབ་པའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྤྱད་པ་ཉིད་མི་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལོ་གཉིས་སུ་དགེ་སློབ་མའི་བསླབ་པ་ལ་སྤྱད་ཟིན་པ་ཉིད་ལ་མཁན་མོ་ཉིད་ཀྱིས་བསྙེན་པར་རྫོགས་པར་མི་བྱེད་ན་ཞེས་བྱ་བའི་དོན་ཏོ།[^1860] །དེ་ལྟར་ཡང་དགེ་སློང་མ་གང་གིས་ཆོས་དྲུག་དང་རྗེས་སུ་མཐུན་པའི་ཆོས་དྲུག་པོ༌[^1861]རྣམས་ལ་བསླབས་པ༌[^1862]བསྙེན་པར་རྫོགས་པར་མི་བྱེད་ན་ལྟུང་བྱེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2866]
འདིར་རྐྱེན་མ་ཚང་བའི་ཕྱིར་བསྙེན་པར་རྫོགས་པར་མི་བྱེད་པ་ལ་ནི་ཉེས་པ་རིགས་པ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་རྗེས་སུ་མི་མཐུན་པར་འབྱུང་བ་བསྙེན་པར་རྫོགས་པ་མ་ཡིན་པ༌[^1863]འདིའི་ངོ་བོའོ། །

[Block 2867]
འདི་ནི་བསླུ་བར་གྱུར་པ་ཡིན་ཏེ། གང་ཞིག་བརྟུལ་ཞུགས་རྫོགས་པ་ཉིད་ལ་གང་གི་དོན་དུ་བརྟུལ་ཞུགས་སྦྱིན་པ་དེ་མ་གྲུབ་པའོ་སྙམ་པ་དེ་བས་ན་འདི་ཁ་ན་མ་ཐོ་བའོ། །

[Block 2868]
བསླབ་པ་ལ་བསླབ་པ་བསྙེན་པར་རྫོགས་པར་མི་བྱེད་པའི་ལྟུང་བྱེད་དོ། །

[Block 2869]
གང་ལ་ཆོས་འཚོང་བའི་ལྟུང་བྱེད་དུ་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་ཁོ་མོ་ལ་གོས་བྱིན་པ་ལྟ་ན་དེའི་ཕྱིར་ཁྱོད་བསྙེན་པར་རྫོགས་པར་བྱའོ་ཞེས་བསྙེན་པར་རྫོགས་པར་འདོད་པ་ལ་ཟེར་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ལྟར་ཡོད་པར་གྱུར་པ་ལ་ཆོས་གང་འཚོང་བར་འགྱུར་ཞེས་བྱ་བ་ཆོས་འཚོང་བའི་ཞེས་བྱ་བ་འདི་བརྗོད་པའི་དོན་ཉིད་ནི་རྙེད་པ་སྟེ། འདིར་མཐུ་དང་ལྡན་པའི་ཆོས་ལ་སྒྱིད་ལུག་པ་དེ་བས་ན་འདིར་ཁ་ན་མ་ཐོ་བའོ། །

[Block 2870]
དེའི་ཕྱིར་འདིར་གོས་ཞེས་སྨོས་པ་ནི་མཚོན་པ་ཙམ་ཡིན་ཏེ། ཤིན་ཏུ་མཆོག་ཏུ་གྱུར་པའི་དོན་ཁས་བླངས་པ་ལ་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་ཏེ། དེར་སེར་སྣའི་ཆོས་ལ་ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2871]
ཤིན་ཏུ་དམན་པའི་ཐ་མ་རྐང་པ་ཉེད་པ་ལ་ཡང་ལྟུང་བྱེད་ཁོ་ནའོ། །

[Block 2872]
འདིར་ཤིན་ཏུ་ཡང་ཆོས་ལ་ལྟུང་བ་ཉིད་སྐྱེ་བར་འགྱུར་རོ། །

[Block 2873]
བདེ་བར་གཤེགས་པའི་ཆོས་སུ་འགྱུར་བའི་དོན་འདི་ལ་སངས་རྒྱས་ཀྱི་བཀའ་ཀློག་པ་ལ་སོགས་པ་ལ་ཉེས་བྱས་སུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2874]
སྡོམ་པ་གཞན་སྦྱིན་པའི་ཕྱིར་ཀློག་པ་ལ་སོགས་པ་སྟེ། དེ་ཁོ་མོ་ལ་ཆོས་གོས་སྟེར་བལྟ་ན་དེའི་ཕྱིར་ཁྱོད་རབ་ཏུ་དབྱུང་བར་བྱའོ་ཞེའམ། ཀློག་ཏུ་གཞུག་གོ་ཞེས་བྱ་བ༌[^1864]ལ་སོགས་པ་ཟེར་བ་ལ་ནི་ཉེས་བྱས་སུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2875]
བུད་མེད་རྣམས་ཀྱི་ཉེས་པ་ཅི་ཡང་རུང་བ་དང་། སེར་སྣའི་ཆོས་ལ་ཡང་དག་པར་གནས་པ་དེ་དང་འདྲ་བའི་སྐྱེས་པ་དགེ་སློང་འདིར་ན་སྨད་པའོ། །
--- END BLOCKS ---
