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
ངེས་པའི་དོན་ཞེས་པ་ནི་སེམས་རྣམ་པར་དག་པ་དང་བདག་ལ་བྱིན་གྱིས་བརླབ་པ་དང་། མངོན་པར་བྱང་ཆུབ་པ་དང་། ཟུང་དུ་འཇུག་པའི་རིམ་པས༌[^2115]བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3292]
དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི་བར་དུ་བསྒོམ་པ་རྫོགས་པ་ན༌[^2116]དེ་ཉིད་ཡང་སྤྲོས་ཏེ། བསྟན་པར་བྱ་བའི་ཕྱིར། དོན་འདི་ཉིད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འདས་པ་དང་། མ་འོངས་པ་ཞེས་པ་ནི་དུས་གསུམ་གྱི་དེ་བཞིན་གཤེགས་པ་རྣམས་སོ། །

[Block 3293]
ཟླ་བ་དང་རྡོ་རྗེ་ལ་སོགས་པའི་རིམ་གྱིས་གཅིག་ཏུ་མཛད་པ་ནི་ཞེས་པ་ལ། ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་དུ་ཟླ་བ་དང་རྡོ་རྗེ་ལ་སོགས་པའི་སྟེང་དུ་རྣམ་པར་དགོད་ཅིང་བསྒོམ་པ་གང་ཡིན་པ་དེ་ནི་ཟིལ་གྱིས་གནོན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3294]
དེའི་དོན་དུ་རྡོ་རྗེ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པས་ཏིང་ངེ་འཛིན་གྱི་མིང་ངོ་། །དེ་ལ་སྙོམས་པར་ཞུགས་ཞེས་པ་ནི་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་དུ་བདག་པོ་ཉིད་དུ་གནས་སོ། །

[Block 3295]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཅེས་བྱ་བ་ལ་སོགས་པས་དབུས་ཀྱི་བདག་པོ་དེ་ཉིད་ཀྱིས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་དཀྱིལ་འཁོར་པ་རྣམས་མྱུར་དུ་བསྒོམ་པར་བསྟན་ཏོ། །

[Block 3296]
དེས་ཞེས་བྱ་བ་ནས་བརྩམས་ཏེ། རྡོ་རྗེ་སེམས་དཔའ་ཉིད་ཐོབ་པོ་ཞེས་བྱ་བའི་བར་དུ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་དཀྱིལ་འཁོར་པ་རྣམས་ཀྱིས་སེམས་ཅན་གྱི་དོན་གྱི༌[^2117]བྱ་བ་བསྟན་ཏོ། །

[Block 3297]
འདི་ལྟར་བཤད་པ་ཡིན་ཏེ། ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་མྱུར་དུ་བསྒོམ་ཞིང་དེ་མ་ཐག་ཏུ་འགྲོ་བ་ཐམས་ཅད་དེའི་རང་བཞིན་དུ་བྱའོ་ཞེས་པའི༌[^2118]དོན་ཏོ། །

[Block 3298]
སྤྱིའི་དོན་ཞེས་པ་ནི་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་དང་པོ་སྦྱོར་བའི་ཕྱོགས་གཅིག་བསྟན་པས་སོ། །

[Block 3299]
དོན་དམ་པའི་དཀྱིལ་འཁོར་བསྟན་པར་བྱ་བའི་ཕྱིར་ཏིང་ངེ་འཛིན་གང་གིས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་ཕུང་པོ་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པ་ཡོངས་སུ་འགོག་པར༌[^2119]བྱེད་པ་ཀུན་རྫོབ་ཀྱི་བྱང་ཆུབ་ཀྱི་སེམས་ལ་བརྟེན་པའི་བདེ་བ་ཆེན་པོའི་ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་པ༌[^2120]ཞེས༌[^2121]བསྟན་ཏོ། །

[Block 3300]
འདིར༌[^2122]རྩ་ཕྲན་སྟོང་ཕྲག༌[^2123]བདུན་ཅུ་རྩ་གཉིས་ཀྱི་ཁོང་སྟོང་ཞེས་པ་ནི་ཕུང་པོ་ལྔའི་བདག་ཉིད་ཅན་ལུས་འདི་ལ་ཇི་སྙེད་ཀྱི་བ་སྤུ་ཡོད་པ་དེ་སྲིད་ཀྱི་རྩ་རྣམས་ཀྱི་དབུས་ཀྱི་ཁོང་སྟོང་ནི་ནམ་མཁའི་ཆའོ། །

[Block 3301]
ཐབས་ཀྱི་ཡེ་ཤེས་ནི་སྣང་བ་མཆེད་པའི་ཡེ་ཤེས་སོ། །

[Block 3302]
[^2124]ཕུང་པོ་ལ་སོགས་པ་ཞེས་པ་ནི་དེའི་རྒྱུར་གྱུར་པའི་འདོད་ཆགས་ལ་སོགས་པའི་རང་བཞིན་རྣམས་སོ། །

[Block 3303]
ཐབས་ཀྱི་ཡེ་ཤེས་ཤར་བས༌[^2125]ཞེས་པ་ནི་བཤད་མ་ཐག་པ་དེ་ཉིད་ཀྱིས་སོ། །

[Block 3304]
དབང་པོ་གཉིས་ཞེས་བྱ་བ་ལ་སོགས་པས་དམ་པ་དགའ་བའི་བདེ་བ་ཉམས་སུ་མྱོང་བ་ཐོབ་པར་གྱུར༌[^2126]ཏོ་ཞེས་བསྟན་ཏོ། །

[Block 3305]
དེས་ནི་འདོད་ཆགས་ལ་སོགས་པ་རྣམ་པར་དག་པའི་སྒོ་ནས་དོན་དམ་པའི་དཀྱིལ་འཁོར་བསྟན་ཏོ། །

[Block 3306]
སྦས་པ་ཞེས་པ་ནི་འདོད་ཆགས་ཀྱི་ཆོས་ཀྱི་མཚན་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3307]
ཕུང་པོ་ལྔ་རྣམས་སོ་ཞེས་པ་ནས་དེའི་ངོ་བོར་གནས་པར་གྱུར་པའོ༌[^2127]ཞེས་བྱ་བའི་བར་དུ་ནི་སྟོང་པ༌[^2128]གསུམ་གྱི་རིམ་པས་ཐམས་ཅད་སྟོང་པ་ལ་འཇུག་པ་བསྟན་ཏོ། །

[Block 3308]
མཐར་ཐུག་པ་ནི་འོད་གསལ་བ་ལ་འཇུག་པས་སོ། །

[Block 3309]
དེ་ལྟར་ལྷག་པར་མོས་པས་ཞེས་བྱ་བ་ལ་སོགས་པས་ལྷག་པར་མོས་པའི་སྦྱོར་བས་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཡོངས་སུ་རྫོགས་པར་བསྟན་ཏོ། །

[Block 3310]
དེ་ནི་ཉེ་བར་མཚོན་པ་ཡིན་ཏེ། དོན་དམ་པའི་དཀྱིལ་འཁོར་ཡང་རྫོགས་པར་མཛད་དོ། །

[Block 3311]
ཡོངས་སུ་དག་པ་དང་མ་དག་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་བསྐྱེད་པའི་རིམ་པ་དང་། བདག་བྱིན་གྱིས་རློབ་པའི༌[^2129]རིམ་པ་ལས་སྐྱེས་པ་དཀྱིལ་འཁོར་གྱི་འཁོར་ལོའི་བདག་པོ་སོ་སོར་བསྟན་པར༌[^2130]བྱེད་དོ་ཞེས་དགོངས་པའོ། །

[Block 3312]
རྟོག་པའི་རྣལ་འབྱོར་གྱི་རིམ་པ་རྫོགས་པར་བྱ་བའི་ཕྱིར། །ཏིང་ངེ་འཛིན་ལ་སྙོམས་པར་ཞུགས་པ་བསྟན་པར་བྱེད་དེ། སྐུ་ལ་སོགས་པའི་ངོ་བོ་ཉིད་ཡིན་པས་ཡི་གེ་གསུམ་པོ་ཁོ་ན་སྐུ་ལ་སོགས་པ་སྟེ་དབྱེར་མེད་པར་བརྟགས་པས༌[^2131]སོ། །

[Block 3313]
འདའ་བར་མི་བྱ་བས་ནི་བསྐྱེད་པའི་རིམ་པའི་རྣལ་འབྱོར་པ་རྣམས་ཀྱིས་དོར་བར་བྱ་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3314]
སྔགས་ཀྱི་ཡི་གེ་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པས་དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི༌[^2132]འོག་ཏུ་ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི་ཟླ་བ་དང་ཉི་མ་དང་པདྨ་གསུམ་པོ༌[^2133]རྣམ་པར་བསྒོམས་ཏེ། དེའི་སྟེང་དུ་ཡི་གེ་གསུམ་ལས་སྐྱེས་པའི་ཟླ་བའི་དཀྱིལ་འཁོར་ལ་ཟླ་བ་ལ་སོགས་པ་འཇུག་པར་བྱས་ལ། ཆོས་ཀྱི་དབྱིངས་བརྗོད་པའི་སྔགས་ཀྱིས་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་རྣམ་པར་སེམས་བརྟན་པར་བྱས་ལ། དེའི་སྟེང་དུ་ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི་རྡོ་རྗེ་རྩེ་ལྔ་པ་རྣམ་པར་བསྒོམས་པས་སྤྲོ་བ་དང་བསྡུ་བ་ཡང་བྱས་ཏེ། དེ་ཡོངས་སུ་གྱུར་པ་ལས་བྱུང་བའི་རྡོ་རྗེ་སེམས་དཔའ། དེའི་ཐུགས་ཀར་ཡེ་ཤེས་སེམས་དཔའ་དང་། ཏིང་ངེ་འཛིན་སེམས་དཔའ་བྱིན་གྱིས་བརླབས་ཏེ། མིག་ལ་སོགས་པ་དང་སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་བརླབས་ལ། སྣ་ཚོགས་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་ཞལ་གསུམ་པ་དང་། ཕྱག་དྲུག་པའི་གཟུགས་འཆང་བར་གྱུར་ཏོ། །

[Block 3315]
དེས་ནི་རྣལ་འབྱོར་བཞིའི་བདག་ཉིད་ཅན་དང་པོའི་སྦྱོར་བ་ཞེས་བྱ་བའི་ཏིང་ངེ་འཛིན་བསྟན་ཏོ། །

[Block 3316]
སྒྲུབ་ཐབས་ལས་བཤད་པའི་རིམ་པས༌[^2134]ཞེས་པ་ནི་མདོར་བསྡུས་པའི་སྒྲུབ་ཐབས་ནས༌[^2135]བཤད་པའི་རིམ་པས༌[^2136]སོ། །

[Block 3317]
རྣལ་འབྱོར་བཞིའི་རིམ་གྱིས། ཞེས་པ་ནི་རྣལ་འབྱོར་དང་། རྗེས་སུ་རྣལ་འབྱོར་དང་། ཤིན་ཏུ་རྣལ་འབྱོར་དང་། རྣལ་འབྱོར་ཆེན་པོའི་རིམ་པས་སོ།[^2137] །

[Block 3318]
སེམས་དཔའ་གསུམ་གྱི་མཐར་ཐུག་པའི་བར་གྱིས། ཞེས་པ་ནི་སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་ཀྱི་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་རྫོགས་པའི་མཐར་ཐུག་པའི་བར་རོ། །

[Block 3319]
བྱིན་གྱིས་བརླབས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^2138]དབུས་ཀྱི་བདག་པོའི་ཞལ་དང་ཕྱག་མཚན་གྱི་ཁྱད་པར་བསྟན་ཏོ། །

[Block 3320]
ཞལ་གསུམ་ལྟ་བུར༌[^2139]ཞེས་པ་ནི་ཕྱག་དྲུག་ལ་སོགས་པས་ཀྱང་ཉེ་བར་མཚོན་པར་བྱའོ། །

[Block 3321]
འཇིག་རྟེན་གྱི་ཁམས་ན་གནས་པ་རྣམས་ཀྱིས། །ཞེས་པ་ནི་སངས་རྒྱས་ཀྱི་ཞིང་མཐའ་ཡས་པ་ལ་གནས་པའི་འཁོར་ཐམས་ཅད་ཀྱིས་མཐོང་ངོ་ཞེས་བྱ་བའི་བར་རོ། །

[Block 3322]
དྲང་བའི་དོན་ཞེས་པ་ནི་རྣལ་འབྱོར་བཞིའི་བདག་ཉིད་ཅན་དང་པོའི༌[^2140]སྦྱོར་བའི་ཏིང་ངེ་འཛིན་དུ་བཤད་པས་སོ། །

[Block 3323]
འོད་གསལ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་རིལ་པོར་འཛིན་པ་དང་། རྗེས་སུ་གཞིག་པའི་ཏིང་ངེ་འཛིན་གྱི་ཐོབ་པར་བྱ་བའི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་མངོན་དུ་བྱས་ཏེ། ཀུན་རྫོབ་དང་དོན་དམ་པ་དབྱེར་མེད་པའི་ལྷའི་སྐུ་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་གྱི་མཚན་ཉིད་ཅན་བླངས་པར་གྱུར་ཏོ་ཞེས་བསྟན་ཏོ། །

[Block 3324]
ཆེན་པོའི་སྒྲའི་དོན་རྣམ་པ་དྲུག་སྟེ། མཆོག་ནི་དཔེར་ན་སྐྱེས་བུ་ཆེན་པོ་བཞིན་ཏེ་སྐྱེ་དགུ་ཐམས་ཅད་ཀྱི་མཆོག་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3325]
ཚད་མེད་པ་ནི་དཔེར་ན་རྒྱ་མཚོ་ཆེན་པོ་བཞིན་ཚད་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3326]
མཁས་པ་ནི་དཔེར་ན་བློ་གྲོས་ཆེན་པོ་དེ་མཁས་པ་ཆེན་པོ༌[^2141]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3327]
བརྩོན་པ་ནི་དཔེར་ན་ཆེན་པོར་འགྲོ་བ་སྟེ་བརྩོན་འགྲུས་ཀྱིས༌[^2142]ཀུན་དུ་འགྲོ་བའོ། །

[Block 3328]
སྤྲོ་བ་ནི་དཔེར་ན་ཆེན་པོ་དགེ་བ་སྟེ་དགེ་བའི་ལས་རྣམས་ལ་བརྩོན་པའོ། །

[Block 3329]
རྨད་བྱུང་བྱེད་པ་ནི་དཔེར་ན་བསྟན་བཅོས་ཆེན་པོ་བརྩམ་པ༌[^2143]བཞིན་སྔར་མེད་པ་སྤྲུལ་པ་ལ་མཁས་པའོ། །

[Block 3330]
འདིར་ནི་མཆོག་གི་དོན་གཙོ་བོ་ཡིན་ཏེ། ཐམས་ཅད་ཀྱི་མཆོག་ཏུ་གྱུར་པའི་རྣམ་པ་ཡིན་ཞེས་བྱ་བའི་དོན༌[^2144]ཏོ། །
--- END BLOCKS ---
