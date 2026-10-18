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
[Block 2871]
དངོས་པོ་མེད་པ་གང་ཡིན་པ་དེ་ནི་དངོས་པོ་མེད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པ་ཡིན་པས་དངོས་པོ་མེད་པའི་བདག་ཉིད་ཁོ་ན་ཞེས༌[^2074]བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2872]
ལམ་ནི་དངོས་པོ་མ་མཆིས་པའོ། །

[Block 2873]
རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ནི་དངོས་པོ་མ་མཆིས་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པས། དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་ཐོས་པ༌[^2075]ཞེས་བྱ་བ་གང་ཡང་མེད་དོ་ཞེས་བསྟན་ཏོ། །

[Block 2874]
བཅོམ་ལྡན་འདས་དངོས་པོ་བྱུང་བའམ། མ་བྱུང༌[^2076]བ་དེ་བཞིན་ཉིད་དང་། མ་ནོར་བ་དེ་བཞིན་ཉིད་ཅེས་བགྱི་བ་མ་མཆིས་སམ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་དམ། མ་ནོར་བ་དེ་བཞིན་ཉིད་ཀྱི་ངོ་བོ་ཉིད་འདས་པའམ་ཕྱིས་འབྱུང་བ་འམ་ད་ལྟར་བྱུང་བ། འདུས་བྱས་པ་དོན་དམ་པར་གང་ཡང་མཆིས་སམ་ཞེས་ཞུས་པའོ། །

[Block 2875]
རྨི་ལམ་ལྟ་བུ་ལ་སོགས་པ་དཔེ་དྲུག་པོ་དག་ནི་གོ་སླའོ། །

[Block 2876]
རབ་འབྱོར་དེ་ཇི་སྙམ་དུ་སེམས། ཆོས་དེ་དག་སྒྱུ་མ་ལྟ་བུ་འམ་རྨི་ལམ་ལྟ་བུ་དག༌[^2077]མ་ཡིན་ནམ་ཞེས་བྱ་བ་ལ་སོགས་པས་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་དང་། ཚངས་པའི་དབྱངས་ཀྱིས་དེ་དག་གི་མཐར་ཐུག་པའི་ཆོས༌[^2078]ཐམས་ཅད་ཀྱང་སྒྱུ་མ་ལྟ་བུ་སྟེ། དེ་བས་ན་ཐམས་ཅད་སྒྱུ་མ་ལྟ་བུ་ཡིན་པས་ཉེས་པ་མེད་དོ་ཞེས་བསྟན་པའོ། །

[Block 2877]
རབ་འབྱོར་འདི་ལྟར་ཆོས་དེ་དག་ཐམས་ཅད་ནི་མངོན་པར་འདུས་བྱས་པ་དང་། བསམ༌[^2079]པ་ཞེས་བྱ་བ་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་དགེ་བའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་མངོན་པར་འདུས་བྱས་པའོ། །

[Block 2878]
སེམས་པ་སྔོན་དུ་འགྲོ་བའི་ཕྱིར་བསམས་པ་སྟེ་དེ་བས་ན་ཀུན་བརྟགས་པའི༌[^2080]ཞེས་བསྟན་ཏོ། །

[Block 2879]
རབ་འབྱོར་འོན་ཀྱང་ཆོས་དེ་དག༌[^2081]ཐམས་ཅད་ཀྱང་ལམ་བསྒྲུབ་པ་དང་། ལམ་སྐྱེད་པར༌[^2082]བྱེད་པ་ཡིན་གྱི། འབྲས་བུ་ཐོབ་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་ཆོས་ཐམས་ཅད་གནས་རྣམ་པར་དག་པར་བྱེད་པ་ཡིན་པས། གནས་ཡོངས་སུ་དག་པར་བྱེད༌[^2083]ན་ལམ་གྱི་རྒྱུན༌[^2084]འགྱུར་རོ། །

[Block 2880]
གང་སྐྱེ་བ་མེད་པ་དང་། འགག་པ་མེད་པའི་བདག་ཉིད་ཅན་དངོས་པོ་མེད་པ་དེ་དག་ཕྲད་པ༌[^2085]ནི་འབྲས་བུ་ཐོབ་པར་བྱེད་པ་མེད་དེ། དེ་ནི་ངོ་བོ་ཉིད་དེ༌[^2086]བཅོས་མ་མ་ཡིན་པ་གནས་པའི་མཚན་ཉིད་ཡིན་ནོ་ཞེས་བསྟན་པའོ། །

[Block 2881]
སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་གཟུང་དུ་མེད་དོ་ཞེས་བྱ་བ་ནི་དངོས་པོའི་ཚུལ་དུའམ། དངོས་པོ་མེད་པའི་ཚུལ་དུ་གཟུང་དུ་མི་རུང་བའོ། །

[Block 2882]
རབ་འབྱོར་གཉིས་ཀྱིས་མངོན་པར་རྟོགས་པར་འགྱུར་བ་མེད། གཉིས་སུ་མེད་པས་ཀྱང་མངོན་པར་རྟོགས་པར་འགྱུར་བ་མེད་ཅེས་བྱ་བ་ནི་གལ་ཏེ་འདུས་བྱས་སམ། འདུས་མ་བྱས་ཀྱི་དངོས་པོ་འགའ་ཞིག་མཐོང་ན་ནི་གཉིས་ཀྱིས༌[^2087]མངོན་པར་རྟོགས་པར་འགྱུར་རོ། །

[Block 2883]
གལ་ཏེ་རི་བོང་གི་རྭ་ལ་སོགས་པ་བཞིན་དུ་ཤིན་ཏུ་དངོས་པོ་མེད་པ་ཞིག་ཡིན་ན་ཡང་གཉིས་སུ༌[^2088]མེད་པས་མངོན་པར༌[^2089]རྟོགས་པར་འགྱུར་རོ། །

[Block 2884]
དེ་བས་ན་རྣམ་པ་དེ་གཉིས་ལས་བཟློག་པ་ནི་མཉམ་པ་ཉིད་རབ་ཏུ་རྟོགས་པ་སྟེ། མངོན་པར་རྟོགས་པའོ་ཞེས་བསྟན་པ་ཡིན་ནོ། །

[Block 2885]
ཡོངས་སུ་བརྗོད་པ་མེད་པ་ཞེས་བྱ་བ་ནི་མངོན་པར་བརྗོད་པར་བྱ་བ་དང་། རབ་ཏུ་བརྗོད་པར་བྱ་བ་མ་ཡིན་པ་ལ། རབ་འབྱོར་འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་བྱའོ་ཞེས་བྱའོ། །

[Block 2886]
དེ་བཞིན་གཤེགས་པས་ཆོས་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཞེས་བྱ་བས་ནི་ཤིན་ཏུ་མཐར་ཐུག་པ་གནས་གྱུར་པ། རྣམ་པར་རྟོག་པ་དང་། སྤྲོས་པ་ཐམས་ཅད་སྤངས་པ་ནི་མཉམ་པ་ཉིད་ལ་གནས་པའི་ཕྱིར་ཤེས་པར་བྱ་བ༌[^2090]ཉིད་ཀྱང་མེད་དེ༌[^2091]ཤེས་པར་བྱ་བར་འགྱུར་བའི་དོན་མི་གཟིགས་པས་ཅི་ཞིག་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པར་འགྱུར་ཞེས་བསྟན་པའོ། །

[Block 2887]
བཅོམ་ལྡན་འདས་དངོས་པོ་མ་མཆིས་པའི་ངོ་བོ་ཉིད་ཀྱི་ཆོས་རྣམས་ལ་མཉམ་པ་ཉིད་ཅེས་བགྱི་བ་གང་ཞིག་མཆིས་ཞེས་བྱ་བ་ནི་ཆོས་རྣམས་ཡོད་ན་མཉམ་པ་ཉིད་ཅེས་བྱ་བ་ཡང་ཡོད་དོ༌[^2092]སྙམ་དུ་དགོངས་པའོ། །

[Block 2888]
རབ་འབྱོར་འདིར་ནི་དེ་ཉིད་མཉམ་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཀྱི༌[^2093]ཆོས་རྣམས་ཀྱི་མཉམ་པ་ཉིད་ནི་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ། དེའི༌[^2094]དངོས་པོར་རྣམ་པར་རྟོག་པ་ཡང་སྤངས་པའི་ཕྱིར་རོ། །

[Block 2889]
རབ་འབྱོར་ཆོས་མཉམ་པ་ཉིད༌[^2095]ནི་དེ་བཞིན་གཤེགས་པའི་ཡུལ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཆོས་མཉམ་པ་ཉིད་ནི་གང་གི་ཡུལ་དུ་ཡང་མི་འགྱུར་ཏེ། དེ་བཞིན་གཤེགས་པ་ཡང་ཆོས་མཉམ་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་མི་གཟིགས་སོ། །

[Block 2890]
ཆོས་མཉམ་པ་ཉིད་ལ་བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་རྣམས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^2096]ནི་བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་རྣམས་དང་། འཕགས་པ་ཐམས་ཅད་དང་། དེ་བཞིན་གཤེགས་པའི་ཆོས་མཉམ་པ་ཉིད་ནི་མཚུངས་སོ། །

[Block 2891]
ཆོས་མཉམ་པ་ཉིད་ལས་ཀྱང་མི་གཡོ་ལ། ཆོས་རྣམས་རྣམ་པར་དགོད་པ་ཡང་མཛད་ཅེས་བྱ་བ་ནི་དོན་དམ་པའི་བདེན་པས་མི༌[^2097]གཡོ་ལ། ཀུན་རྫོབ་ཏུ་རྣམ་པར་དགོད་པ་མཛད་དོ། །

[Block 2892]
བཅོམ་ལྡན་འདས་ཅི་ལགས། ཆོས་ཉིད་འདུས་བགྱིད་ལགས་སམ། འོན་ཏེ་འདུས་མ་བགྱིད་ལགས་ཞེས་བྱ་བ་ཅི་ལས་དགོངས་ཤེ་ན། གང་གཟུགས་ལ་སོགས་པའི་ཆོས་འདི་རྣམས་ཀྱི་ཆོས་ཉིད་དེ་གལ་ཏེ་འདུས་མ་བྱས་ཡིན་ན་གཟུགས་ལ་སོགས་པ་འདུས་བྱས་རྣམས་ཀྱི་ཆོས་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 2893]
གལ་ཏེ་འདུས་བྱས་ཡིན་ན། གཟུགས་ལ་སོགས་པ་བཞིན༌[^2098]དེ་ཡང་ཀུན་བརྟགས་པ་སྟེ། སྐྱེ་བ་དང་འགག་པ་ཅན་དུ་འགྱུར་རོ་སྙམ་དུ་དགོངས་ནས་ཞུས་པའོ། །

[Block 2894]
བཅོམ་ལྡན་འདས་ཀྱིས། རབ་འབྱོར་དེ་ནི་འདུས་བྱས་ཀྱང་མ་ཡིན། འདུས་མ་བྱས་ཀྱང་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་སྐྱོན་གཉིས་སུ་འགྱུར་དུ་དོགས་པའི་ཕྱིར་གཉིས་བསལ་བ་གསུངས་པའོ། །

[Block 2895]
འདུས་བྱས་ལས་གུད་ན་ཡང་འདུས་མ་བྱས་དམིགས་སུ་མེད་ལ། འདུས་མ་བྱས་ལས་གུད་ན་ཡང་འདུས་བྱས་དམིགས་སུ་མེད་དེ༌[^2099]ཞེས་བྱ་བ་ནི་འདི་ལ་ཕུང་པོ་དང་། ཁམས་དང་། སྐྱེ་མཆེད་ལ་སོགས་པའི་དེ་བཞིན་ཉིད་མ་དག་པ་གང་ཡིན་པ་དེ་ཕུང་པོ་ལ་སོགས་པ་དེ་དག་ལ༌[^2100]ལོགས་ཤིག་ན་དམིགས་སུ་མེད་ལ། ཕུང་པོ་ལ་སོགས་པ་གང་ཡིན་པ་དེ་དག་ཀྱང་དེ་བཞིན་ཉིད་མ༌[^2101]གཏོགས་པར་གུད་ན་དམིགས་སུ་མེད་དེ། དེ་བཞིན་ཉིད་མ་དག་པ་ནི་དེ་ལས་དེ་ཉིད་དང་། གཞན་ཞེས་བརྗོད་དུ་མི་རུང་ངོ་། །གང་གི་ཕྱིར་དེ་ལྟར་གཉི་ག་ཡང་གཉི་ག་ལས་གུད་ན་དམིགས་སུ་མེད་པ་དེའི་ཕྱིར་དེ་གཉི་ག་ཡང་གཅིག་གོ་ཞེས་བརྗོད་དུ་མི་རུང་བས་ལྡན་པ་ཡང་མ་ཡིན་ནོ། །

[Block 2896]
ཐ་དད་དོ་ཞེས་ཀྱང་བརྗོད་དུ་མི་རུང་བའི་ཕྱིར་མི་ལྡན་པ་ཡང་མ་ཡིན་ནོ། །

[Block 2897]
གཟུགས་ཅན་མ་ཡིན་ཞིང་རྣམ་པར་མི༌[^2102]རྟོག་པའི་ཕྱིར་གཟུགས་མེད་པའོ། །

[Block 2898]
ཚིག་ལ་སོགས་པས་བསྟན་ཏུ་མི་རུང་བའི་ཕྱིར་བསྟན་དུ་མེད་པའོ། །

[Block 2899]
དབང་པོའི་ཡུལ་གྱི་ཐོགས་པ་མེད་པ་དང་། གཟུང་བ་དང་འཛིན་པ་མེད་པའི་ཕྱིར་ཐོགས་པ་མེད་པའོ། །

[Block 2900]
གཉི་ག་ཡང་མཚན་ཉིད་མེད་པར་མཚན་ཉིད་གཅིག་པའི་ཕྱིར། འདི་ལྟར་མཚན་ཉིད་མེད་པར་མཚན་ཉིད་གཅིག་པའོ། །

[Block 2901]
དེ་ལ་འདུས་བྱས་ནི་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་མཚན་ཉིད་མེད་པའོ། །

[Block 2902]
འདུས་མ་བྱས་ནི་མཚན་མ་མེད་པས་མཚན་མར་གཟུང༌[^2103]དུ་མི་རུང་བའི་ཕྱིར་མཚན་ཉིད་མེད་པའོ། །

[Block 2903]
དེ་དག་ཀྱང་དེ་བཞིན་གཤེགས་པས་འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་བརྗོད་ཀྱི༌[^2104]ཞེས་བྱ་བ་ནི་འདུས་བྱས་ཡོད་པ་མ་ཡིན༌[^2105]དུ་ཟིན་ཀྱང་འཇིག་རྟེན་གྱི་ཀུན་རྫོབ་ཏུ་ཐ་སྙད༌[^2106]འདོགས་ཤིང་འདུས་མ་བྱས་བརྗོད་དུ་མེད་པ་ཡིན་ཡང་ཐ་སྙད་དུ་བརྗོད་པའོ། །

[Block 2904]
དེ་སྐད་བཀའ་སྩལ་ནས་ཐ་སྙད་དེ་ཡོད་པ་མ་ཡིན་པར། དོན་དམ་པར་ནི་ལུས་ཀྱི་འདུ་བྱེད་དམ། ངག་གི་འདུ་བྱེད་དམ། ཡིད་ཀྱི་འདུ་བྱེད་གང་ཡང་མེད་དོ་ཞེས་བྱ་བས་སྟོན་ཏེ། ལས་རྣམ་པ་གསུམ་ཆར་ཡང་ཀུན་བརྟགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2905]
རབ་འབྱོར་སྟོང་པ་ཉིད་ནི་ཅི་ཡང་མེད། ཅུང་ཟད་ཀྱང་མེད་ཅེས་བྱ་བ་ནི་ཅི་ཡང་མི་བྱེད་པའི་ཕྱིར་ཅི་ཡང་མེད་པའོ། །

[Block 2906]
དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་ཅུང་ཟད་ཀྱང་མེད་པའོ། །

[Block 2907]
འདི་ནི་དེ་བཞིན་གཤེགས་པའི་ཁྱུ་མཆོག་ཏུ་གྱུར་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་བཞིན་གཤེགས་པའི་མཛད་པ་ནི་རྣམ་པར་རིག་པར་བྱ་བ་ཙམ་དུ་ཟད་དེ། གལ་ཏེ་སེམས་ཅན་རྣམས་བདག་ཉིད་ཀྱིས་ཤེས་པར་གྱུར་ན། དེ་བཞིན་གཤེགས་པ་མི་དམིགས༌[^2107]སོ་ཞེས་སྟོན་ཏོ། །

[Block 2908]
བཅོམ་ལྡན་འདས་ཅིའི་སླད་དུ་སྟོང་པ་ལགས་ཞེས་བྱ་བ་ནི་ཅི་ཞིག་མེད་པས་སྟོང་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2909]
དེ་ལ་འདུ་བྱེད༌[^2108]པ་གང་ཡིན་པ་དེས་སྟོང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལ་གང་འདུས་བྱས་སོ་ཞེས་འདུ་བྱེད༌[^2109]པ་མཚན་མར་འཛིན་པའི་བདག་ཉིད་དེ་མེད་པས་སྟོང་པའོ། །

[Block 2910]
རབ་འབྱོར་ལ་ལ་ཞིག་གི༌[^2110]སྤྲུལ་པ་སྤྲུལ་ན༌[^2111]ཞེས་བྱ་བ་ནི། སྤྲུལ་པ་འདི་སྤྲུལ་པ་གཞན་པ་གཞན༌[^2112]དག་སྤྲུལ་པ་བྱེད་དོ་ཞེས་བྱ་བ་དེ༌[^2113]སྟོང་པ་མ་ཡིན་པའི་དངོས་པོ་ཅུང་ཟད་ཀྱང་ཡོད་དམ་ཞེས་བྱ་བ་སྟེ། གང་གི་ཚེ་སྤྲུལ་པ་ཞིག་སྤྲུལ་པ་གཞན་སྤྲུལ་པར་བྱེད་པ་དེའི་ཚེ། སྤྲུལ་པ་དེ་ལ་སྟོང་པ་མ་ཡིན་པའི་ངོ་བོ་ཉིད་ཅི་ཡང་ཡོད་དམ་ཞེས་སྨྲས་པའོ། །
--- END BLOCKS ---
