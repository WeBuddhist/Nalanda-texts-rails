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
[Block 2731]
ཚེ་རབས་གཞན་དུ་ལས་སྐྱེ་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་བསད་པ་ལ་སོགས་པའི་སྦྱོར་བ་བྱས་ནས་ཐོག་མར་ཤི་བར་གྱུར་པའི་སྲོག་ཆགས་པ༌[^1867]ལ་སོགས་པ་མི་བསྐྱེད་དེ་སྦྱར་བ་ཙམ་ཉིད་ལས་དེར་ལྟུང་བའོ། །

[Block 2732]
ཕམ་པར་གྱུར་པ་གསུམ་པའི་ཞུ་བའི་སྐབས་སོ།། །།

[Block 2733]
སྦོམ་པོ་ནི་ཁོ་བོ་འཆི་བར་འོང་ངོ་ཞེས་དེ་སྐད་ཟེར་བ་ལ་ཡིད་མི་ཆེས་ཤིང་དེ་བཞིན་ཉིད་དུ་སྒྲུབ་པར་བྱེད་ནའོ་ཞེས་བྱ་བ་ལ། སྦོམ་པོ་ནི་ཞེས་བྱ་བའི་ཚིག་དང་པོར་སྨོས་པ་ནི་དབང་དུ་བྱ་བ་བསྟན་པའི་ཕྱིར་ཏེ། གལ་ཏེ་ནད་པ་ན་རེ་བདག་ལ་ཁྲུས་དང་བསྐྱོད་པ་ལ་སོགས་པ་ཅུང་ཟད་བྱེད་ན་གདོན་མི་ཟ་བར་ཁོ་བོ་འཆི་བར་འོང་ཞེས་དེ་སྐད་ཟེར་བ་ལ་ཡིད་མ་ཆེས་ཤིང་དེ་གཞན་ཉིད༌[^1868]དུ་ཁྲུས་ལ་སོགས་སྒྲུབ་པར་བྱེད་ན་སྦོམ་པོའོ། །

[Block 2734]
ངེས་པར་འདིར་ལྟུང་བར་འགྱུར་བ་ལ་ཡང་རྩུབ་པས་ཉེ་བར་གནས་པ་ཞེས་བྱ་བ་ལྟུང་བ་འདིའོ། །

[Block 2735]
ནད་པ་ཤི་བླའོ་ཞེས་གཡོག་མི་བྱེད་ནའོ་ཞེས་བྱ་བ་ནི་སྦོམ་པོ་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །

[Block 2736]
མེད་པར་བྱ་བ་མི་འཕྲོད་པ་སྦྱིན་ནའོ་ཞེས་བྱ་བ་ནི་ནད་པ་ལ་ཞེས་བྱ་བ་དང་རྗེས་སུ་འབྲེལ་ལོ། །

[Block 2737]
འདིར་ཡང་ཡིད་མ་ཆེས་པའི་ཕྱིར་ཤེས་པར་གྱུར་པ་ན་རྩུབ་པ་ཉིད་ལ་ཉེ་བར་གནས་པའོ། །

[Block 2738]
འདིར་འཆད་པར་འགྱུར་བ་ལ་ཡང་སྦོམ་པོའོ། །

[Block 2739]
འབྲས་ཡོངས་སུ་མ་སྨིན་པ་བརྟོལ་ནའོ་ཞེས་བྱ་བ་ནི་འདིར་ཡང་ངེས་པར་རྩུབ་པ་ཉིད་ཉེ་བར་གནས་པ་ཞེས་བྱ་བ་ལྟུང་བ་འདིའོ། །

[Block 2740]
དོང་དུ་འཇུག་པ་དང་སྒོ་གླེགས་ཀྱིས་བཙིར་བ་ལ་སོགས་པས་ཉོན་མོངས་པར་བྱེད་པའོ་ཞེས་བྱ་བ་ལ། འདི་ནི་གསད་པའི༌[^1869]སྦྱོར་བའི་རྣམ་པ་སྟེ་དེ་བས་ན་འདིར་སྦོམ་པོའོ། །

[Block 2741]
གཡང་ས་ནས་མཆོང་བ་དང་འཆི་བ་ལ་སོགས་པ་ལ་འཆི་བའི་དོན་དུ་བསྒྲུབ་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡང་གི་སྒྲས་ནི་སྦོམ་པོའོ་ཞེས་བྱ་བ་དེའི་རྗེས་སུ་བསྙག་པའི༌[^1870]ཕྱིར་རོ། །

[Block 2742]
འདིར་གཞན་ཤི་བ་ཡོད་པར་གྱུར་པ་ལ་ཕམ་པ་སྟེ་མེད་པར་གྱུར་ན་སྦྱོར་བ་ཉིད་ཀྱི་ཕྱིར་སྦོམ་པོ་འགྲུབ་པའོ། །

[Block 2743]
དེ་བས་ན་བདག་ཉིད་གསད་པ༌[^1871]ལ་གཡང་ས་དེར་བཏང་བ་ལ་སོགས་པ་ལ་བཟུང་བར་རྟོགས་པར་བྱའོ། །

[Block 2744]
འདིར་བདག་ཉིད་གསོད་པ་ལ་སྦོམ་པོ་སྟེ། དེ་བས་ན་འདི་ཤི་བ་ལ་བརྗོད་དོ། །

[Block 2745]
དེ་བས་ན་མེད་པར་གྱུར་པ་ལ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 2746]
ནད་པ་ལ་བབ་ཅོལ་དུ་མཚོན་དང་ཐག་པ་སྦྱིན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ནད་གཡོག་ལ་ཤི་བའི་ཡོ་བྱད་མ་ཡིན་ན་ཞེས་བྱ་བ་བརྗོད་ཟིན་ཏོ། །

[Block 2747]
ནད་གཡོག་མ་ཡིན་པའི་དོན་དུ་ནི་རྩོམ་པ་འདིའི༌[^1872]བབ་ཅོལ་དུ་ཞེས་བྱ་བའི་ཚིག་གིས་ཤི་བ་ལ་མ་ཡིན་པའི་ཡོ་བྱད་ཉིད་ཤེས་ནས་བྱ་བ་གཞན་གྱི་དོན་དུ་སྦྱིན་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2748]
འདིར་ནི་མཚོན་དང་ཐག་པའི་ཚིག་ནི་དཔེ་ཡིན་ཏེ་ཁབ་ལ་སོགས་པ་རྣམས་ཀྱང་བསྡུས་པ་ཡིན་ནོ། །

[Block 2749]
ཞལ་ཏ་བས་ཤེས་བཞིན་དུ་བྱའོ། །

[Block 2750]
གསང་སྔགས་ཀྱི་ཐལ་ལྕག་བྱ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཤེས་བཞིན་དང་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །ཤེས་བཞིན་དུ་ཞེས་བྱས་པས༌[^1873]གདོན་གྱིས་ཟིན་པ་ཐར་བར་བྱ་བའི་གསང་སྔགས་སྔོན་དུ་འགྲོ་བས་གདོང་དུ་ཐལ་ལྕག་གིས་བསྣུན་པ་ནི་ཐལ་ལྕག་བསྣུན་པའོ། །

[Block 2751]
ཤི་བ་དང་གནོད་པ་དང༌[^1874]གཞན་ལ་དགག་པའི་དོན་དུ་དེ་ལྟ་བུའི་རིགས་ཅན་གྱི་ཐ་སྙད་རྣམས་སོ། །

[Block 2752]
ཁོང་ནད་བསལ་བའི་ཕྱིར་དང་ཐོགས་པ་བསལ་བའི་ཕྱིར་བསྣུན་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་མགྲིན་པ་ལ་སོགས་པའི་ལུས་ལ་ཅུང་ཟད་ནུས་པ་ལུས་ལས་དོན་གཞན་དུ་གྱུར་པ་ནི་ཐོགས་པའོ། །

[Block 2753]
དེ་བསལ་བའི་ཕྱིར་བསྣུན་པ་གང་ཡིན་པ་དེ་ཡང་དག་པར་ཤེས་ཤིང་སྦྱིན་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2754]
དེར་འགྱུར་བས༌[^1875]ལེགས་པར་སོ་སོར་བརྟག་པར་བྱ་སྟེ་དྲིལ་བར་བྱའོ་ཞེས་བྱ་བ་ལ་དེར་གྱུར་པས་ཞེས༌[^1876]བྱ་བ་ནི་ཡང་དག་པར་ཤེས་པར་གྱུར་པ་ཤེས་བཞིན་ལ་གནས་པའོ། །

[Block 2755]
དེ་ལྟར་སོ་སོར་བརྟག་པར་བྱ་སྟེ་རྡོ་བ་ལ་སོགས་པས་དྲིལ་བར་བྱའོ། །

[Block 2756]
ཇི་ལྟར་སུ་ཞིག་ལ་ཡང་གནོད་པར་མི་འགྱུར་བར་རོ། །

[Block 2757]
གནོད་པར་བྱ་བ་མེད་པར་ཤེས་པའི་ཕྱིར་སོ་སོར་རྟོག་པ་འདིའོ། །

[Block 2758]
དེ་བས་ན་གནོད་པ་བྱེད་པའི་རྡོ་བ་ལ་སོགས་པ་ལ་འདི་དྲིལ་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་བརྟག་པར་བྱའོ། །

[Block 2759]
ཕྱོགས་ཉུང་དུས་གདག་པ༌[^1877]ལྕི་བ་ལ་འབད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཉུང་བའི་གསུམ་གྱི་ཚོགས་བརྩོན་པ་ཆ་ཤས་སུ་གྱུར་པ་ལྕི་བའི་ཁུར་གདེག༌[^1878]པར་བྱ་བའི་དོན་ཏོ། །

[Block 2760]
སྤྱི་བོ་ཚུགས་སུ་འགྲོ་བར༌[^1879]མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྤྱི་བོ་ཚུགས་མཁན་ལྟར་རོ། །

[Block 2761]
མ་བསླབས་པས་བསླབས་པ༌[^1880]ལ་སྦྱར་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མཚོན་གྱི་ལས་ལ་སོགས་པ་གཞན་ལ་གནོད་པའི་ཕྱིར་ནུས༌[^1881]པ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 2762]
མཚོན་འཕང་བ༌[^1882]ལ་བསྒོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དཔེར་ན་མདའ་འཕངས༌[^1883]ཤིག་དང་བལྟ་བར་བྱའི༌[^1884]ཞེས་བྱ་བའོ། །

[Block 2763]
ནད་པ་མི་ནུས་པ་ལམ་དུ་མི་བཀྲིའོ་ཞེས་བྱ་བའོ། །

[Block 2764]
ཕམ་པ་གསུམ་པ་འདུལ་བྱེད་ཀྱི་སྐབས་སོ།། །།

[Block 2765 [HEADING]]
## ཕམ་པར་འགྱུར་བ་བཞི་པ། ^5-0

[Block 2766]
གང་དུ་ཕམ་པར་གྱུར་པ་བཞི་པ་ཞེས་བྱ་བ་ལ་ལྟོས་ནས་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་འདུ་ཤེས་བསྒྱུར་ཏེ་བདག་ཉིད་མིའི་ཆོས་བླ་མ་དང་ལྡན་པ་ཉིད་དུ་སྨྲ་ནའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འདི་བདེན་པར་གྱུར་པ་དང་མིང་དུ་གྱུར་པའི་དོན་བཟུང་སྟེ་བསྒྱུར་ཏེ་སྦ་བར་བྱས་ནས་འོག་ཏུ་བྱས་ཏེ་བརྫུན་པའི་དོན་གྱིས་འདུ་ཤེས་གཞན་གྱིས་བཀབ་ནས་བདག་ཉིད་མིའི་ཆོས་བླ་མ་དང་ལྡན་པ་ཉིད་དུ་བརྗོད་པ་ལ་ཅི་བདག་ཉིད་དམ་གཞན་ལ་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ལའོ། །

[Block 2767]
དེ་ཉིད་མཐོང་ངོ་བདག་མཐོང་ངོ་སྒྲ་ཐོས་སོ། །

[Block 2768]
བདག་གིས་ཐོས་སོ། །

[Block 2769]
འགྲོའོ། །

[Block 2770]
བདག་གི༌[^1885]དྲུང་དུ་འོང་ངོ་། །ལྷན་ཅིག་ཏུ༌[^1886]གཏམ་འདྲེའོ། །
--- END BLOCKS ---
