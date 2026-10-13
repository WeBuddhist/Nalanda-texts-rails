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
[Block 2101]
དེ་ལ་ངོ་བོ་ཉིད་ཀྱིས་མྱོང་བར་འགྱུར་བ་ནི་ཚོར་བ་རྣམས་སོ། །

[Block 2102]
མཚུངས་པར་ལྡན་པས་མྱོང་བར་འགྱུར་བ་ནི་རེག་པ་སྟེ། བདེ་བ་མྱོང་བར་འགྱུར་བའི་རེག་པ་ཞེས་བྱའོ། །

[Block 2103]
དམིགས་པ་མྱོང་བར་འགྱུར་བ་ནི་ཡུལ་རྣམས་ཏེ། ཇི་སྐད་དུ། མིག་གིས་གཟུགས་རྣམས་མཐོང་ནས་གཟུགས་སོ་སོར་ཡང་དག་པར་མྱོང་བ་ཞེས་བྱའོ། །

[Block 2104]
རྣམ་པར་སྨིན་པ་མྱོང་བར་འགྱུར་བ་ནི་ལས་ཡིན་ཏེ། མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཞེས་བྱའོ། །

[Block 2105]
མངོན་སུམ་དུ་གྱུར་པ་མྱོང་བར་འགྱུར་བ་ནི་ཇི་སྐད་དུ། གང་གི་ཚེ་བདེ་བའི་ཚོར་བ་ཉམས་སུ་མྱོང་བའོ། །

[Block 2106]
དེ་བས་ན་རྣམ་པར་སྨིན་པ་ཉམས་སུ་མྱོང་བར་འགྱུར་བ་ཡིན་པའི་ཕྱིར་ལས་ཀྱང་བདེ་བ་མྱོང་བར་འགྱུར་བ་ཞེས་བྱ་བ་ལ་སོགས་པར་བརྗོད་དོ། །

[Block 2107 [VERSE]]
དེ་ཡང་ངེས་དང་མ་ངེས་པ། །
མཐོང་བའི་ཆོས་ལ་སོགས་པ་ལ། །
མྱོང་འགྱུར་ཕྱིར་ན་ངེས་རྣམ་གསུམ། །

[Block 2108]
དེ་ནི་མ་ངེས་པ་དང་བཅས་པ་རྣམ་པ་བཞི་ཡིན་ནོ། །

[Block 2109]
ཁ་ཅིག་ལས་རྣམ་ལྔ་ཞེས་ཟེར། །མྱོང་བར་འགྱུར་བ་མ་ངེས་པ་ལ་རྣམ་པར་སྨིན་པ༌[^831]ངེས་པ་དང་མ་ངེས་པ་རྣམ་པ་གཉིས་སུ་ཕྱེ་ནས་སོ། །

[Block 2110]
གཞན་དག་མུ་ནི་བཞི་ཞེས་ཟེར། །གནས་སྐབས་ངེས་ལ་རྣམ་པར་སྨིན་པ༌[^832]མ་ངེས་པ་ཡང་ཡོད་དེ། མཐོང་བའི་ཆོས་ལ་སོགས་པ་ལ་མྱོང་བར་འགྱུར་ལ། རྣམ་པར་སྨིན་པ་ནི་མ་ངེས་པའི་ལས་གང་ཡིན་པའོ། །

[Block 2111]
རྣམ་པར་སྨིན་པ༌[^833]ངེས་ལ་གནས་སྐབས་དག་ཏུ་མ་ཡིན་པ་ཡང་ཡོད་དེ། དེ་ལས་བཟློག་པའོ། །

[Block 2112]
གཉིས་ཀ་ཡང་ཡོད་པ་དང་། གཉིས་ཀ་མེད་པ་ཞེས་བྱ་བ་བཤད་པའི་རྗེས་སུ་འབྲངས་ནས་ཤེས་པར་བྱའོ། །

[Block 2113 [VERSE]]
ལས་བཞི་པོ་དེ་དག་ལས། །
གསུམ་གྱིས་རིས་ནི་འཕེན་པར་བྱེད། །

[Block 2114]
མཐོང་བའི་ཆོས་ལ་མྱོང་བར་གྱུར་པའི༌[^834]ལས་ཀྱིས་ནི་རིས་མཐུན་པ་འཕེན་པར་མི་བྱེད་པའི་ཕྱིར་རོ། །

[Block 2115]
ཁམས་གང་ངམ༌[^835]འགྲོ་བ་གང་ན་ལས་ཀྱི་འཕེན་པ་དུ་ཞིག་ཡོད་ཅེ་ན།

[Block 2116 [VERSE]]
ཐམས་ཅད་ན་ནི་འཕེན་པ་བཞི། །
ཐམས་ཅད་དུ་ལས་བཞི་འཕེན་ཏེ། །

[Block 2117]
དགེ་བའམ་མི་དགེ་བ་ཅི་རིགས་པར་རོ། །

[Block 2118]
སྤྱིར་བསྟན་པ་འདིའི་དམིགས་ཀྱིས་བསལ་བ་ནི་འདི་ཡིན་ཏེ། དམྱལ་བ་ན་ནི་དགེ་བའི་གསུམ། །མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བ་ནི་མེད་དེ། དེ་ན་དགེ་བའི་རྣམ་པར་སྨིན་པའི་སྐབས་མེད་པའི་ཕྱིར་རོ། །

[Block 2119 [VERSE]]
གང་ལས་འདོད་ཆགས་བྲལ་བརྟན་པའི། །
བྱིས་པ་དེར་སྐྱེས་མྱོང་མི་བྱེད། །

[Block 2120]
སོ་སོའི་སྐྱེ་བོ་ཡོངས་སུ་མི་ཉམས་པའི་ཆོས་ཅན་ཞིག་ན། དེ་ནི་ས་གང་ལས་འདོད་ཆགས་དང་བྲལ་བ་དེར་སྐྱེས་ནས་མྱོང་བར་འགྱུར་བའི་ལས་ནི་མི་བྱེད་དོ། །

[Block 2121]
འཕགས་པ་གཞན་དུའང་མྱོང་མི་བྱེད། །བརྟན་པ༌[^836]ཞེས་བྱ་བར་སྦྱར་ཏེ། དེ་ནི་དེར་ལན་གྲངས་གཞན་དུ་མྱོང་བར་འགྱུར་བའི་ལས་ཀྱང་མི་བྱེད་དོ། །

[Block 2122]
འདོད་རྩེའི་མི་བརྟན་པ༌[^837]ཡང་མིན། །འདོད་པའི་ཁམས་སམ་སྲིད་པའི་རྩེ་མོ་ལས་འདོད་ཆགས་དང་བྲལ་བའི་འཕགས་པ་ནི་དེར་སྐྱེས་ནས་མྱོང་བར་འགྱུར་བ་དང་། ལན་གྲངས༌[^838]གཞན་ལ་མྱོང་བར་འགྱུར་བའི་ལས་བྱེད་པར་ནི་རུང་བ་མ་ཡིན་ནོ། །

[Block 2123]
དེ་ནི་དེའི་ཚེ་འབྲས་བུ་ལས་ཡོངས་སུ་ཉམས་པ་ཡིན་ལ། འབྲས་བུ་ལས་ཡོངས་སུ་ཉམས་པ་ལ་ཡང་འཆི་བ་མེད་དོ། །

[Block 2124]
ཅི་སྲིད་པ་བར་མ་ལ་ཡང་ལས་ཀྱིས༌[^839]འཕེན་པ་ཡོད་དམ་ཞེ་ན། སྨྲས་པ། ཡོད་དེ།

[Block 2125 [VERSE]]
སྲིད་པ་བར་མ་འདོད་ཁམས་སུ། །
འཕེན་པ་རྣམ་པ་ཉི་ཤུ་གཉིས། །

[Block 2126]
ཇི་ལྟར་བྱས་པས་ཤེ་ན། ནུར་ནུར་པོ་དང་། མེར་མེར་པོ་དང་། ནར་ནར་པོ་དང་། གོར་གོར་པོ་དང་། རྐང་ལག་འགྱུས་པའི་གནས་སྐབས་ལྔ་དང་། བྱིས་པ་དང་། གཞོན་ནུ་དང་། དར་ལ་བབ་པ་དང་། དར་ལ༌[^840]ཡོལ་བ་དང་། རྒན་པོའི་གནས་སྐབས་ལྔ་དང་། གནས་སྐབས་བཅུ་པོ་འདི་དག་ལ༌[^841]ཉམས་སུ་མྱོང་བ་དང་། སྲིད་པ་བར་མར་ཉམས་སུ་མྱོང་བར་ངེས་པ་དང་མ་ངེས་པ་རྣམ་པ་ཉི་ཤུ་རྩ་གཉིས་འཕེན་པར་བྱེད་དོ། །

[Block 2127 [VERSE]]
དེ་ནི་མཐོང་ཆོས་འབྲས་བུ་ཡིན། །
དེ་ནི་རིས་གཅིག་ཁོ་ན་ཡིན། །

[Block 2128]
དེ་ནི་རིས་མཐུན་པ་གཅིག་ཁོ་ན་ཡིན་ཏེ། སྲིད་པ་བར་མ་གང་ཡིན་པ་དང་། དེའི་རྒྱུ་ལས་བྱུང་བ་གནས་སྐབས་བཅུ་པོ་གང་དག་ཡིན་པ་དེ་ནི་ལས་གཅིག་གིས་འཕངས་པ་ཡིན་ནོ། །

[Block 2129]
དེའི་ཕྱིར་མཐོང་བའི་ཆོས་ཀྱི་མྱོང་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 2130]
ཡང་ངེས་པའི་ལས་ཅི་འདྲ་བར་རིག་པར་བྱ་ཞེ་ན།

[Block 2131 [VERSE]]
ཉོན་མོངས་རབ་དང་དྲག་པོ་དང་། །
ཡོན་ཏན་ཞིང་དང་རྒྱུན་ཆགས་སུ། །
བྱས་པ་གང་ཞིག་ཡིན་པ་དང་། །
ཕ་མ་གསོད༌[^842]གང་དེ་ངེས་སོ། །

[Block 2132]
ཉོན་མོངས་པ་དྲག་པོས་བྱས་པའི་ལས་གང་ཡིན་པ་དང་། རབ་ཏུ་དང་བ་དྲག་པོས་བྱས་པ་དང་། གང་རྒྱུན་དུ་བྱེད་པ་དང་། ཡོན་ཏན་གྱི་ཞིང་ལ་བྱེད་པ་དེ་ནི་ངེས་པ་ཡིན་པར་རིག་པར་བྱ་སྟེ། ཡོན་ཏན་གྱི་ཞིང་ནི་དཀོན་མཆོག་གསུམ་དང་། འབྲས་བུ་དང་སྙོམས་པར་འཇུག་པ་ཁྱད་པར་ཅན་ཐོབ་པའི་གང་ཟག་གོ། །

[Block 2133]
དེ་ལ་ཉོན་མོངས་པ་དང་རབ་ཏུ་དང་བ་དྲག་པོ་དང་། རྒྱུན་དུ་བྱེད་པ་མེད་པར་ཡང་དགེ་བའམ་མི་དགེ་བ་དང་། ཕ་མ་གསོད་པ་ཡང་ངེས་པར་འགྱུར་རོ། །

[Block 2134]
མཐོང་བའི་ཆོས་ལ་མྱོང་བའི་ལས་ཅི་འདྲ་བ་ཞེ་ན།

[Block 2135 [VERSE]]
མཐོང་ཆོས་འབྲས་བུ་ཅན་གྱི་ལས། །
ཞིང་དང་བསམ་པའི་ཁྱད་པར་ལས། །

[Block 2136]
མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་བའི་ལས་ཞིང་གི་ཁྱད་པར་ལས་འགྱུར་རོ། །

[Block 2137]
བསམ་པའི་ཁྱད་པར་ལས་ཀྱང་ངོ་། །ཡང་། ས་དེའི་འདོད་ཆགས་གཏན་བྲལ་ཕྱིར། །ཡང་དགེ་བའམ་མི་དགེ་བའི་ལས་ས་གང་ཡིན་པ་དེ་ལས་གཏན་དུ་འདོད་ཆགས་དང་བྲལ་བ་ཡིན་པའི་ཕྱིར་དེ་མཐོང་བའི་ཆོས་ལ་མྱོང་བར་འགྱུར་རོ། །

[Block 2138]
ལས་ཇི་ལྟ་བུ་ཞིག་ཅེ༌[^843]ན། རྣམ་སྨིན་ངེས་པ་གང་ཡིན་པའོ། །

[Block 2139]
དེའི་ངེས་པ་འདི་ཡིན་ཏེ། གནས་སྐབས་ངེས་པའི་ཡང་མ་ཡིན་ལ་མ་ངེས་པའི་ཡང་མ་ཡིན་ནོ། །

[Block 2140]
གང་ངེས་པར་མྱོང་པའི་ཞིང་དེ་ཁོ་ན་ཅི་མཐོང་བའི་ཆོས་ལ་མྱོང་བ་ཡིན་ཞེ་ན། ཡིན་ཏེ། དེ་དང་གང་ཟག་ཁྱད་པར་ཅན་གཞན་ཡང་འདི་ལྟ་སྟེ།
--- END BLOCKS ---
