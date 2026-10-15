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
[Block 2976]
དེ་དག་ལ་ཧ་ཅང་ཐལ་བར་གྱུར་པ་ལ་འགལ་ཚབས་དང་བཅས་པར་འགྱུར་བ༌[^2829]དམིགས་ཀྱིས་བསལ༌[^2830]བའི་ཕྱིར་གདོན་པ་ནི་མི་བྱ་བ་ཉིད་དོ། །

[Block 2977]
གཞན་དག་གིས་གནས་ནས་ཕྱུང་བ་སྤང་བར་བྱ་བ་ཁོ་ནའོ༌[^2831]ཞེས་བྱ་བ་སྨོས་ཏེ། རང་བཞིན་དུ་གནས་པ་དག་གིས་དེ་ལ་བསྡིགས་པར་བྱ་བ་ཁོ་ན་ཡིན་ཏེ། དེ་དང་ལྷན་ཅིག་བཅག་པ་དང་འདུག་པ་དང་འགྲོ་བ་ཇི་སྐད་བསྟན་པ་དག་ཀྱང་མི་བྱ་ཞིང་འདོན་པ་གཞན༌[^2832]མེད་ན་དེས་སོ་སོར་ཐར་པའི་མདོ་འདོན་པ་ཡང་ཉམས་སུ་མྱོང་བར་མི་བྱའོ། །

[Block 2978]
གཞན་ཡང་དེ་ལ་ལུས་སམ་ངག་གི༌[^2833]འདྲེ་བར་འགྱུར་བ༌[^2834]ཅུང་ཟད་མི་བྱའོ། །

[Block 2979]
དེའི་དུས་ཉིད་ཀྱི་རྒྱུ་ལས་བྱུང་བའི་རྙེད་པ་ཡང་མི་དབང་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་གནས་ནས་ཕྱུང་བའི་དུས་ཉིད་ཀྱི་ཚེ་ན་དགེ་འདུན་ལ་རྙེད་པ་བྱུང་བ་གང་ཡིན་པ་དེ་ནི་ཡང་གནས་ནས་ཕྱུང་བ་དེ་ལ་མི་འོས་པ་ཉིད་ཡིན་ཏེ། གནས་ནས་མ་ཕྱུང་བའི་མདུན་རོལ་དུ་ཇི་སྲིད་གནས་ཀྱི་རྒྱུ་ལས་བྱུང་བའི་རྙེད་པ་ལ་གལ་ཏེ་དེའི་ཚེ་དགེ་འདུན་གྱིས་ཐོབ་པ་ཉིད་དུ་འབྱུང་བར་འགྱུར་བའི་དབྱར་གནས་པ་ལ་སོགས་པའི་རྒྱུ་ལས་བྱུང་བའི་རྙེད་པ་གང་ཡིན་པ་དེ་དེ་དང་ལྡན་པ་ཉིད་ནི་དེ་ཡང་དབང་བ་ཉིད་ཡིན་ཏེ། [^2835]ཁྱིམ་པ་ཉིད་དུ་གྱུར་པ༌[^2836]ཡང་དེ་ལྟར་དབང་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2980]
ཅི་ཆ་གཅིག་མི་དབང་བ་ཉིད་དེ་གཏན་དུའམ་ཞེ་ན་དེའི་ཕྱིར་བྱེ་བ་བཞིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟར་བྱེ་བ༌[^2837]དག་ལས་དེ་སྨོས་པ་དེ་བཞིན་དུ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2981]
མ་ཚོར་བ་ལྟར་ཅིག་ཤོས་རྣམས་ལ་དེ་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་ལ་དེ་བསྟན་པའོ། །

[Block 2982]
བྱེ་བ་དག་ན་ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པ་ཡང་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་བྱེ་བ་རྣམས་ལ་ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང་མཐུན་པ་ཡང་གནས་ནས་ཕྱུང་བ་དེ་དང་འདྲ་སྟེ། གནས་ནས་ཕྱུང་བ་ལ་གང་དུ་སྤྱོད་པ་ཅི་བསྟན་པ་དེ་དག་ཐམས་ཅད་ཆོས་མ་ཡིན་པའི་ཕྱོགས་དང༌[^2838]མཐུན་པ་ལ་ཡང་བལྟ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2983]
རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པ་དག་ལ་ཡོངས་སུ་གནས་པ་དང་མགུ་བར་བྱ་བ་དང་བསླབ་པ་སྤྱོད་པ་དག༌[^2839]མི་འཆགས་སོ་ཞེས་བྱ་བ་ནི་རང་བཞིན་དུ་གནས་པ་མ་ཡིན་པ་དེ་རྣམས་ལ་མི་སྤྱད་པ་ཉིད་དོ། །

[Block 2984]
གང་གི་ཕྱིར་དེ་རྣམས་ལ་མི་འཆགས༌[^2840]པའི་ཕྱིར་རོ། །

[Block 2985]
དགེ་འདུན་མ་ཡིན་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི༌[^2841]ཡོངས་སུ་གནས་པ་ལ་སོགས་པ་མི་འཆགས་པ་སྟེ། སུ་དག་དགེ་འདུན་དུ་མ་གྱུར་པའི་གང་ཟག་གཅིག་གམ་གཉིས་སམ་གསུམ་དག་ལ་ཡང་མི་འཆགས་སོ། །

[Block 2986]
གནས་དེ་ན་འཁོད་པ་དག་ལས་ཡོངས་སུ་བཅད་པ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་ཡང་མི་འཆགས་སོ་ཞེས་བྱ་བར་སྦྱར་ཏེ། གནས་གང་དུ་ཡོངས་སུ་གནས་པ་ལ་སོགས་པ་དེ་དག་ལ་སྤྱད་པར༌[^2842]བྱ་བའི་གནས་དེ་ན་འཁོད་པའི་དགེ་སློང་དག་ལས་ལོགས་ཤིག་ཏུ་ཡོངས་སུ་བཅད་ཅིང་བཀར་བ༌[^2843]དག་ལས་ཡོངས་སུ་གནས་པ་ལ་སོགས་པ་སྤྱོད་པ་མི་འཆགས་སོ། །

[Block 2987]
མང་པོ་ཉིད་དུ་ཡོངས་སུ་སྤང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་དེ་ན༌[^2844]དགེ་སློང་མང་པོ་དག་འཁོད་པར་འདིར་སྤྱད་པར་དཀའོ་སྙམ་པའི་བློ་མང་བ་ཉིད་ཀྱིས༌[^2845]སྤྱོད་པ་སྤང་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2988]
གནས་བརྟན་དང་སོ་སོར་ཐར་པ་དང་བཅས་པ་ཉིད་དུ་འབད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་གང་ན་གནས་བརྟན་དང་བཅས་སོ་སོར་ཐར་པ་དང་བཅས་པའི་དགེ་འདུན་ཡོད་པའི་གནས་དེ༌[^2846]ཇི་ལྟར་སྤྱོད་པར་འགྱུར་བ་ཞིག་གུ་སྙམ་དུ་དེའི་དོན་དུ་འབད་པར་བྱའོ། །

[Block 2989]
མ་གྲུབ་ན་གཞན་དུ་ཡང་སྤྱད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2990]
གང་ན་གཞན་གསུམ་ལ་སོགས་པ་དེ་དག་གི་མིང་རྣམ་པ་ཐམས་ཅད་ཀྱི༌[^2847]སྤྱོད་པ་དེར་སྤྱོད་པར༌[^2848]མི་བྱའོ་ཞེས་བྱ་བ་ནི་རྣམ་པ་ཐམས་ཅད་ཀྱི༌[^2849]དེ་སྤྱོད་པ་དེར་ཞེས་བྱ་བ་གང་རྣམས་ལ་ཡོད་པ་དེ་རྣམས་ནི་རྣམ་པ་ཐམས་ཅད་སྤྱོད་པ་དེར་བྱ་བའོ།[^2850] །བསླབ་པ་ལ་སྤྱོད་པ་ཞེས་བྱ་བ་སྨོས་པས་སོ། །

[Block 2991]
ཡོངས་སུ་གནས་པ་དང་མགུ༌[^2851]བར་བྱ་བ་དང་བཅས་པ་རྣམས་ཉེ་བར་བསྡུ་བའི་ཕྱིར་རྣམ་པ་ཐམས་ཅད་ཀྱི་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2992]
གང་ན་བདག་ཉིད་ལས་གསུམ་པོ་ལ་སོགས་པ་དེ་དག་གི་མིང་རྣམ་པ་ཐམས་ཅད་སྤྱོད་པ་དེར་དེ་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གང་དུ་གཞན་ཡོངས་སུ་གནས་པ་སྤྱོད་པ་གསུམ་ཡོད་པ་དེར་ཡོངས་སུ་གནས་པར་སྤྱད་པ༌[^2852]མི་བྱའོ། །

[Block 2993]
གང་ན་གཞན་གསུམ་པོ་ལ་སོགས་པ་གཞི་ནས༌[^2853]ཡོངས་སུ་གནས་པ་སྤྱོད་པ་དེར་གཞི་ནས་ཡོངས་སུ་གནས་པ་སྤྱད་པར་མི་བྱའོ། །

[Block 2994]
གང་ན་གཞན་ཡང་གཞི་ནས་བསླང་སྟེ། ཡོངས་སུ་གནས་པ་དང་མགུ་བར་བྱ་བ་སྤྱོད་པ་དང་། གཞི་ནས་མགུ་བར་བྱ་བ་སྤྱོད་པ་དང་། ཡང་གཞི་ནས་བསླང་སྟེ་མགུ་བར་བྱ་བ་སྤྱོད་པ་དང་། བསླབ་པ་སྤྱོད་པ་དེར་བསླབ་པ་གང་ཞིག་ལ་ཞེས་བྱ་བ་དེ་ལ་འདི་བསྟན་པའོ། །

[Block 2995]
འདིར་གཞུང་ནི། གཙུག་ལག་ཁང་གཅིག་ཏུ་ཡོངས་སུ་གནས་པར་བྱེད་པ་བཞིས༌[^2854]ཡོངས་སུ་གནས་པར་བྱེད་པར་མི༌[^2855]བྱའོ། །

[Block 2996]
མགུ་བར་བྱ་བ་སྤྱོད་པ་བཞིས༌[^2856]མགུ་བར་བྱ་བ་སྤྱད་པར་མི་བྱའོ། །

[Block 2997]
གཞི་ནས་མགུ་བར་བྱ་བ་སྤྱོད་པ་བཞིས༌[^2857]གཞི་ནས་མགུ་བར་བྱ་བ་སྤྱད་པར་མི་བྱའོ། །

[Block 2998]
གཙུག་ལག་ཁང་དུ༌[^2858]བསླབ་པ་བྱིན་པ་བཞིས་བསླབ་པ་ལ་བསླབ་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2999]
དང་པོ་གཉིས་ཀྱིས༌[^2859]གཞན་དུ་སྐྱ་རེངས་འཆར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་སྤྱོད་པ་དང་མགུ་བ་སྤྱོད་པ་དང་བསླབ་པ་སྤྱོད་པ་ཞེས་བྱ་བ༌[^2860]གསུམ་སྨོས་པའི་དང་པོ་གཉིས་ཏེ། ཡོངས་སུ་གནས་པ་སྤྱོད་པ་དང་མགུ་བར་བྱ་བ་སྤྱོད་པ་གཉིས་ཀྱིས་གནས་གང་དུ་སྤྱད་པར་བྱ་བ་ཡང་དག་པར་བླངས་པའི་གནས་དེ་ལས་གཞན་པའི་མཚམས་སུ་སྐྱ་རེངས་འཆར་བར་མི་བྱའོ། །

[Block 3000]
བསླབ་པ་བྱིན་པ་ལ་ནི་ཆོ་ག་ཇི་སྲིད་འཚོའི་བར་དུ་དེ་ལ་འཇུག་པ་དང་བར་དུ་གཅོད་པར་གྱུར་པ་འདི་མེད་དོ། །

[Block 3001]
དེ་ནི་ཚེ་གཅིག་གིས༌[^2861]ཡིན་པས་ཚེ་གཅིག་ཏུ་ངེས་པ་མེད་པའི་ཕྱིར་སྔ་རོལ་དུ་ཇི་སྲིད་འཚོ་བ་ཞེས་བྱ་བ་མི་སྦྱོར་བའོ། །

[Block 3002]
འདུས་པའི་དགེ་འདུན་ལ་འདས་པ་དང་འབྱུང་བར་འགྱུར་བ་བརྗོད་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདུས་པའི་གཎྜཱི་བརྡུངས་པ་དེར་ཇི་སྙེད་འདུས་པ་དེ་སྙེད་འདུས་པ་དག་ལ་གང་ཞིག་འདུས་པ་དེ་གནས་པ་དེ་ལ་དགེ་འདུན་གྱིས་གང་ཡང་མ་འོངས་པ་འབྱུང་བར་འགྱུར་བ་དང་བྱུང་ཟིན་པ་དེ་དག་སྤྱོད་པར་གྱུར་པ༌[^2862]དང་། དེ་དག་སྤྱད་ཟིན་པ་ཞེས་བྱ་བ་བརྗོད་པར་བྱ་བ་ཉིད་དོ། །

[Block 3003]
འདིར་ལས་བཞིན་དུ་ཐམས་ཅད་མི་འཚོགས༌[^2863]ན་བརྗོད་པ་མི་འཆགས་པ་མ་ཡིན་ཏེ་དེ་ལྟ་བས་ན་ཇི་སྙེད་པ་འདུས་པ་དེ་སྙེད་པ་རྣམས་ལ་ཉེས་པ་དང་བྲལ་བར་རིག་པར་བྱའོ། །

[Block 3004]
དགེ་འདུན་ལས་ཞེས་སྨོས་པ་དེ་ནི་གང་ཟག་གི་འདུས་པ་བསལ་བའི༌[^2864]དོན་དུའོ། །

[Block 3005]
དུས་ཇི་ཙམ་ཞིག་བརྗོད་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་ཡུན་རིང་དུ་སྤྱད་པར་བྱ་བ་ཉིད་མ་ཡིན་ན་ཉིན་རེ་ཞིང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ་གལ་ཏེ་ཡོངས་སུ་གནས་པ་ཡུན་རིང་དུ་སྤྱད་པར་བྱ་བ་མ་ཡིན་ན་ཉིན་རེ་ལན་རེ་བརྗོད་པར་བྱ་བ་ཡིན་ནོ། །

[Block 3006]
འདི་ལ་ནི༌[^2865]གསུམ་མམ་བཞི་ཞིང་ངོ་ཞེས་བྱ་བ་ནི་ཡུན་རིང་དུ་སྤྱད་པར་བྱ་བ་ཉིད་འདི་ལ་ཉི་མ་གསུམ་མམ་བཞི་ཞིང་ལན་རེ་བརྗོད་པར་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 3007]
དེ་གཉིས་ལ་དོན་དེས་བརྙས་ཐབས་མི་བྱའོ༌[^2866]ཞེས་བྱ་བ་ནི་ཡོངས་སུ་གནས་པ་དང་མགུ་བར་བྱ་བ༌[^2867]སྤྱོད་པ་དེ་གཉིས༌[^2868]ལ་དགེ་འདུན་ལྷག་མ་དང་ཁ་ན་མ་ཐོ་བ་ཀུན་དུ་སྤྱོད་པའི་དོན་དེས་བརྙས༌[^2869]ཐབས་མི་བྱའོ། །

[Block 3008]
འཐབ་ཀྲོལ་བྱེད་པ་འོང་བར་ཐོས་ཤིང་གལ་ཏེ་དེས་འཇིགས་ན་དགེ་འདུན་ཚོགས་པའམ་གང་ཟག་ལ་ཕྱིར་བཏང་བར་བྱ་བ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་དུ་འཐབ་ཀྲོལ་བྱེད་ཅིང་རྒོལ་བའི་ངང་ཚུལ་ཅན་ལ་དེ་ལ་ཆེད་དུ་འགྲོ་བ་ཉིད་དུ་གནས་པ་དེ་འདིར་འཐབ་ཀྲོལ་བྱེད་པར་འགྱུར་སྙམ་དུ་འབྱུང་བར་འགྱུར་ལ་འཐབ་ཀྲོལ་བྱེད་པ་གཅིག་གམ་དུ་མ་འོང་བར་ཐོས་ཤིང་། གལ་ཏེ་དེ་དག་གིས་གླེང་བ་དང་དྲན་པར་བྱེད་པས་འཇིགས་ན་སྤྱོད་པ་དེས་འཁྲུག་པར༌[^2870]གྱུར་པའི་འཐབ་ཀྲོལ་བྱེད་པ་པོ་གཅིག་གམ་དུ་མ་འོང་བར་མ་ཐོས༌[^2871]པར་འབྱུང་ན། དགེ་འདུན་གྱི་དྲུང་ངམ་གང་ཟག་གམ་དེ་དང་མི་མཛའ་བ་ཉིད་དུ་གནས་པས་བདག་ཉིད་རང་བཞིན་དུ་གནས་པ་ལ་གཞག་པར་བྱའོ། །

[Block 3009]
འདིར་གཞུང་ཁ་ཅིག་ལས་རྒན་པའི་མཐར་གནས་ཏེ་ཡོངས་སུ་གནས་པ་དང་མི་མཛའ་བ་ཉིད་དུ་གནས་པར་བྱའོ། །

[Block 3010]
དགེ་འདུན་ལ་ཕྱིར་བཏང་བའི་སྔགས་ནི་དགེ་འདུན་བཙུན་པ་རྣམས་གསན་དུ་གསོལ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3011]
གཞན་དུ་ཡང་གཉིས་པོ་འདི་དག་གང་ཟག་ལ་ཕྱིར་བཏང་བའི་སྔགས་ཀྱི༌[^2872]གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་བཅོམ་ལྡན་འདས་ཀྱིས་གལ་ཏེ་ཡོངས་སུ་གནས་པར་བྱེད་པའི་དགྲ་བོ་འོངས༌[^2873]ན། དེ་ཡོངས་སུ་གནས་པའི་སྤྱོད་པ་བག་ཡངས་སུ་བྱའོ་ཞེས་བཀའ་སྩལ་ན༌[^2874]དེས་ཇི་ལྟར་བག་ཡངས་སུ་བགྱི། ཉེ་བ༌[^2875]འཁོར་དགེ་སློང་དེས་ཆོས་གོས་ཕྲག་པ་གཅིག་ཏུ་སྟེ། འཆིལ༌[^2876]ལྷམ་དག་ཕུད་ནས་དགེ་སློང་གི་མདུན་དུ་ཙོག་པུར་འདུག་སྟེ་འདི་སྐད་ཅེས་བརྗོད་པར་བྱའོ།[^2877] །བདག་དགེ་སློང་ཡོངས་སུ་གནས་པར་བགྱིད་པའི་དགྲ་བོ་དགེ་སློང་མཆིས་ཏེ། བདག་མིང་འདི་ཞེས་བགྱི་བ་ཡོངས་སུ་གནས་པའི་སྤྱོད་པ་བག་ཡངས་སུ་བགྱིད་ཅིང་སླར་ཡང་ལེན་པར་བགྱིད་དོ། །

[Block 3012]
ཡང་བླངས༌[^2878]ཏེ་སྤྱོད་པར་བགྱིད་ན་ཚེ་དང་ལྡན་པ་དག་གིས་བདག་ངོ་ཚ་མ་མཆིས་པར༌[^2879]གཟུང་དུ་གསོལ། །དེ་བཞིན་དུ་ལན་གཉིས། ལན་གསུམ་དུ་བཟླསཏེ།[^2880] ཐབས་ཡིན་ནོ་ལེགས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3013]
དགྲ་བོ་སོང་ན་ཕྱིར་ཡང་དེ་བཞིན་དུ་བླང་བར་བྱ་སྟེ། དེ་ནི་ཡོངས་སུ་གནས་པ་དང་མགུ་བར་བྱ་བར་སྤྱོད་པ་ཡིན་ནོ་ཞེས་གསུངས་ཏེ། དེ་ལ་གཉིས་ཀའི་སྦྱོར་བ་ཞེས་བྱ་བ་འདི་གཉིས་ཀ་བསྡུས་པའོ། །

[Block 3014]
འཇིགས༌[^2881]དང་བྲལ་ན་དེ་ཉིད་དུ་ཕྱིར་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་དྲུང་ངམ་གང་ཟག་ལའོ། །

[Block 3015]
ས་གཞན་ན་གནས་པའི་གཞིའོ།། །།
--- END BLOCKS ---
