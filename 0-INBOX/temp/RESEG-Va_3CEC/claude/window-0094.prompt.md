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
[Block 3291]
དེ་ནས་བཅོམ་ལྡན་འདས་ལ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བློ་གྲོས་མི་ཟད་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། ཁྱོད་འདྲ་བའི་སྐྱེས་བུ་དམ་པ་རྣམས་ལ་ཤིན་ཏུ་བཟོད་དོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས། འགལ་བ་སྟོན་པ་ལ་བཟོད་པར་གསོལ་བ་བསྟན་ཏོ། །

[Block 3292]
དེ་ནས་བཅོམ་ལྡན་འདས་ལ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། འདི་ཇི་ལྟ་བུར་གཟུང་བར་བགྱི་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས་མཚན་དྲི་བ་བསྟན་ཏོ། །

[Block 3293]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། སངས་རྒྱས་ཀྱི་བྱ་བས་ཉེ་བར་གནས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ཡན་ཆད་ཀྱིས༌[^2847]མཚན་དུ་བྱ་བར་བསྟན་ཏོ། །

[Block 3294]
མི་ཟད་པའི་ཆོས་ཀྱི་སྒོ་ཞེས་བྱ་བ་ནི་མདོ་སྡེ་འདི་ལས་མི་ཟད་པར་གཏོགས་པའི་ཆོས་དཔག་ཏུ་མེད་པ་འབྱུང་བ་ན༌[^2848]མི་ཟད་པའི་ཆོས་ཀྱི་སྒོ་ཞེས་བྱའོ། །

[Block 3295]
ཆེད་དུ་བརྗོད་པ་ཆེད་དུ་བརྗོད་ཅེས་བྱ་བ་ནི་དགའ་བ་དང་། གཟེངས་མཐོས་པའི་ཚིག་འདི་སྐད་དུ་སྨྲས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3296]
མི་ཟད་པའི་རྣམ་པས་བསྟན་ཞེས་བྱ་བ་ནི་མི་ཟད་པའི་ཚུལ་གྱིས་བསྟན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3297]
ཆོས་ཀྱི་དགབ་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཆོས་ཕྱིན་ཅི་མ་ལོག་པར་བཤད་པས། དེའི་ཕྱིར་བྱིན་པ་ནི་ཆོས་ཀྱི༌[^2849]དགབ་པའི་ཕྱིར་བྱིན་པའོ། །

[Block 3298]
ལེགས་སོ་ལེགས་སོ་ཞེས་ལན་གཉིས་སུ་སྨྲས་པ་ནི་དོན་རྣམ༌[^2850]པ་གཉིས་ཀྱི་ཕྱིར་ཏེ། གདོན་མི་ཟ་བ་དང་གཞན་མ་ཡིན་པའོ། །

[Block 3299]
གདོན་མི་ཟ་བ་ནི་ངེས་པར་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཀྱི་རྒྱུར་འགྱུར་བ།[^2851] ལེགས་སོ་ཞེས་བྱ་བ་དང་པོ་གསུངས་སོ། །

[Block 3300]
ཕྱིན་ཅི་མ་ལོག་པར་བཤད་དེ་དོན་གཞན་མ་ཡིན་པས་ལེགས་སོ་ཞེས་བྱ་བ་གཉིས་པ་གསུངས་སོ། །

[Block 3301]
ལེགས་པར་སྨྲས་སོ་ཞེས་བྱ་བ་ནི་ཕྱིན་ཅི་མ་ལོག་པར་བཤད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3302]
གསོལ་བ་ནི་བཅོམ་ལྡན་འདས་ཀྱི༌[^2852]སྐུ་ལ་གསོལ་བའོ། །

[Block 3303]
མཆོད་རྟེན་ལགས་སོ་ཞེས་པ༌[^2853]ནི་མྱ་ངན་ལས་འདས་པ་འདོད་པའི་སེམས་ཅན་རྣམས་དགེ་བ་བསགས་པར་བྱ་བའི་ཕྱིར་ཕྱག་འཚལ་བ་དང་བསྐོར་བའི་གནས་སུ་གྱུར་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3304]
འདི༌[^2854]ཞེས་བྱ་བ་ནི་བློ་གྲོས་མི་ཟད་པའིའོ། །

[Block 3305]
ཡང་དག་པའི་ཡོན་ཏན་བརྗོད་པ་ནི་དེའི་མཐུ་དང་ལྡན་པ་བདག་ཉིད་ཆེན་པོ་བརྗོད་པའོ། །

[Block 3306]
ལྟ་བ༌[^2855]ནི་ཤའི་མིག་གིས་སོ། །

[Block 3307]
ཕྱག་འཚལ་བ་ནི་ལུས་འདུད་པའོ། །

[Block 3308]
མཆོད་པ་ནི་མེ་ཏོག་ལ་སོགས་པས་སོ། །

[Block 3309]
བསྙེན་བཀུར་ནི་བསྐོར་བ་ལ་སོགས་པའོ། །

[Block 3310]
ཉན་པ་ནི་དངོས་པོ༌[^2856]ཉིད་དུ་ཚིག་དང་ཡི་གེ་ཉན་པའོ། །

[Block 3311]
མོས་པ་ནི་སེམས་དང་ཞིང་ཡིད་ཆེས་པར་བྱེད་པའོ། །

[Block 3312]
ཡོངས་སུ་འདྲི་བ་ནི་གཞུང་ཐམས་ཅད་གླེབས་བམ༌[^2857]དུ་འདྲི་བའོ། །

[Block 3313]
འཛིན་པ་ནི་ཡི་གེ་དང་དོན་གཉིས་སེམས༌[^2858]ཀྱིས་བླངས་པའོ། །

[Block 3314]
འཆང་བ་ནི་དེ་ལྟར་བཟུང་ནས་བརྗེད་པར་བྱ་བ་མ་ཡིན་གྱི། དུས་ཐམས་ཅད་དུ༌[^2859]མི་བརྗེད་པར་འཆང་བའོ། །

[Block 3315]
ཀློག་པ་ནི་དེ་ལྟར་མི་བརྗེད་པར་གཟུང་བ༌[^2860]དང་། དེ་ཕྱིར་ཞིང་ཡི་གེ་ལྟ་ཞིང་ཀློག་པའོ། །

[Block 3316]
སྟོན་པ་ནི་ཇི་ལྟར་གཟུང་བའི༌[^2861]ཆོས་གཞན་ལ་ཡང་འཆད་པའོ། །

[Block 3317]
ཀུན་ཆུབ་པར་བྱེད་པ་ནི་གཟུང་བ༌[^2862]དང་འཆང་བ་དང་འཛིན་པ་དང་། [^2863]ཀློག་པ་དེ་དག་གང་ཡང་རུང༌[^2864]མགོ་འཇུག་ཏུ་ཕྱིན་པར་བྱེད་པའོ། །

[Block 3318]
གཞན་དག་ལ་ཡང་རྒྱ་ཆེར་རབ་ཏུ་སྟོན་པ་ནི། དོན་དང་ཚིག་དེ་དག་སེམས་ཅན་ཀུན་ལ་རྒྱ་ཆེར་སྤྲོས་ཏེ་བཤད་པའོ། །

[Block 3319]
རིགས་ཀྱི་བུའམ་རིགས་ཀྱི་བུ་མོ་ཞེས་བྱ་བ་ནི་རིགས་ལྔ་ལས་ཐེག་པ་ཆེན་པོའི་རིགས་དང་ལྡན་པ་ལ་བྱ་བར་དགོངས་སོ། །

[Block 3320]
བསྒོམ་པའི་རྣལ་འབྱོར་ལ་བརྩོན་པར་གནས་པ་ནི་བདག་ཉིད་མི་ཟད་པའི་དོན་བསྒོམ་པ་ལ་རྒྱུན་དུ་བརྩོན་པའོ། །

[Block 3321]
བྱང་ཆུབ་ཀྱི་སེམས་མ་བརྗེད་པ་ཞེས་བྱ་བ་ནི་གཞན་ལ་ཕན་པར་འདོད་པའི་བྱང་ཆུབ་ཀྱི་སེམས་དང་ལྡན་པའོ། །

[Block 3322]
བསྐྱོད་པར༌[^2865]མི་ནུས་པ་ནི་བཟོད་པ་དེ་དཀྲུགས་ཤིང༌[^2866]མེད་པར་བྱར་མི་ནུས་པའོ། །

[Block 3323]
ཆོས་ཐམས་ཅད་ཀྱི༌[^2867]རྗེས་སུ་སོང་བའི་བཟོད་པ་ཞེས་བྱ་བ་ནི་མི་ཟད་པའི་ཆོས་རྣམས་དང་མཐུན་པར་བཟོད་པའོ། །

[Block 3324]
སྦྱོར་བ་ནི་སེམས་པའོ། །

[Block 3325]
ངེས་པར་སེམས་པ་ནི་ཕྱིན་ཅི་མ་ལོག་པར་རྟོགས་པའོ། །

[Block 3326]
མི་གཡེང་བ་ནི་གཡེང་བ་མེད་པའོ། །

[Block 3327]
གཞན་གྱི་དྲིང༌[^2868]མི་འཇོག་པར་ཤེས་པ་ནི་གཞན་ལ་བརྟེན༌[^2869]མི་དགོས་པར་ཤེས་པའོ། །

[Block 3328]
རབ་ཏུ་རྣམ་པར་འབྱེད་པར༌[^2870]ཤེས་པ་ནི་མི་ཟད་པ་རྣམས་ཀྱི་མཚན་ཉིད་སོ་སོར༌[^2871]མ་འདྲེས་པར་དབྱེ་བ་ཤེས་པའོ། །

[Block 3329]
སངས་རྒྱས་ཀྱི་ཆོས་ནི་སྟོབས་དང་མི་འཇིགས་པ་ལ་སོགས་པའོ། །

[Block 3330]
རྒྱ་ཞེས་བྱ་བ་ནི་ས་བཅུར་འདྲེན་པར༌[^2872]བྱེད་པའི་གཞི༌[^2873]དང་རྟེན་ཡིན་ཏེ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
