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
[Block 3151]
འདི་ནི་འདོད་མོད་ཀྱི་རེག་པ་དང་ཚོར་བ་དག་ཕན་ཚུན་ནམ༌[^1794]འབྲས་བུ་ཉིད་དུ་འདོད་པ་འདི་ནི་མདོ་ལས་མི་བཞེད་དེ། མིག་གི་འདུས་ཏེ་རེག་པ་ལ་བརྟེན་ནས་མིག་གི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི༌[^1795]ཚོར་བ་སྐྱེའོ། །

[Block 3152]
[^1796]མིག་གི་འདུས་ཏེ་རེག་པ་ལས་བྱུང་བའི་ཚོར་བ་ལ་བརྟེན་ནས་མིག་གི༌[^1797]འདུས་ཏེ་རེག་པ་སྐྱེ་བ་ནི་མ་ཡིན་ནོ་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3153]
སྐྱེད་པར་བྱེད་པའི་ཆོས་དང་འགལ་བའི་ཕྱིར་ཡང་རིགས་པ་མ་ཡིན་ཏེ། ཆོས་གང་ཞིག་ཆོས་གང་གི་སྐྱེད་པར་བྱེད་པར་གནས་པ་དེ་ནི་དེ་དང་དུས་ཐ་དད་པར་གྲགས་ཏེ། དཔེར་ན་ས་བོན་སྔ་ལ་མྱུ་གུ་འཕྱི་བ་དང་། འོ་མ་སྔ་ལ་ཞོ་འཕྱི་བ་དང་། བསྣུན་པ་སྔ་ལ་སྒྲ་འཕྱི་བ་དང་། ཡིད་སྔ་ལ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་འཕྱི་བ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 3154]
རྒྱུ་དང་འབྲས་བུ་དག་སྔ་ཕྱིའི་དངོས་པོར་མ་གྲུབ་པ་ཡང་མ་ཡིན་མོད་ཀྱི་ལྷན་ཅིག་པའི་དངོས་པོར༌[^1798]ཡང་འགྲུབ་སྟེ། དཔེར་ན་མིག་གི༌[^1799]རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་རྣམས་དང་། མིག་དང་གཟུགས་དག་དང་། འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པ་རྣམས་ལྟ་བུའོ། །

[Block 3155]
དེ་ལ་ཡང་དབང་པོ་དང་དོན་དག༌[^1800]སྔ་ལ༌[^1801]རྣམ་པར་ཤེས་པ་འཕྱི་བ་དང་། འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པ་རྒྱུ་ཚོགས་པ་སྔ་མ་ལས་ཕྱི་མ་འབྱུང་ངོ་ཞེས་བྱ་བར་འདོད་ན་དགག་པ་ཅི་ཞིག་ཡོད། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་འོ་ན་ནི་མྱུ་གུ་དང་གྲིབ་མ་དག་ཇི་ལྟ་བར་རེག་པ་དང་ཚོར་བ་དག་ཀྱང་དེ་དང་འདྲའོ་ཞེས་ཟེར་རོ། །

[Block 3156]
གཞན་དག་ན་རེ་རེག་པའི་འོག་ཏུ་ཚོར་བ་འབྱུང་སྟེ། དབང་པོ་དང་དོན་དག་ནི་སྔ་ལ་དེའི་འོག་ཏུ༌[^1802]རྣམ་པར་ཤེས་པ་སྟེ། གསུམ་འདུས་པ་དེ་ནི་རེག་པ་ཡིན་ནོ། །

[Block 3157]
རེག་པའི་རྐྱེན་གྱིས་སྐད་ཅིག་མ་གསུམ་པ་ཚོར་བ་འབྱུང་ངོ་ཞེས་ཟེར་རོ། །

[Block 3158]
དེ་ལྟ་ན་ནི་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་ལ་ཚོར་བ་ཡོད་པར་མི་འགྱུར་ལ། རྣམ་པར་ཤེས་པ་ཐམས་ཅད་རེག་པ་ཡིན་པར་ཡང་མི་འགྱུར་རོ། །

[Block 3159]
དེ་ནི་ཉེས་པ་མེད་དེ། རེག་པ་ཕྱི་མ་ལ་ཡོད་པའི་ཚོར་བ་རེག་པ་སྔ་མའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་པས་རེག་པ་ཐམས་ཅད་ཀྱང་ཚོར་བ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 3160]
རྣམ་པར་ཤེས་པ་ཐམས་ཅད་ཀྱང་རེག་པ་ཡིན་ནོ། །

[Block 3161]
འདི་ནི་རིགས་པ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 3162]
འདི་ལ་མི་རིགས་པ་ཅི་ཞིག་ཡོད་ཅེ་ན། འདི་ལྟ་སྟེ་རེག་པ༌[^1803]དམིགས་པ་ཐ་དད་པ་དག་རེག་པ་ཕྱི་མ་ལ་ཡོད་པའི་ཚོར་བ་རེག་པ་སྔ་མའི་རྒྱུ་ལས་བྱུང་བ་ཡིན་ནོ་ཞེས་བྱ་བ་སྟེ། ཇི་ལྟ་ཞེ་ན། རིགས་མི་འདྲ་བ་ལ་དམིགས་པའི་རེག་པ་ལས་བྱུང་བའི་ཚོར་བ་གཞན་ལ་དམིགས་པར༌[^1804]འགྱུར་བ་འམ། ཡང་ན་སེམས་གང་དང་མཚུངས་པར་ལྡན་པ་དེ་ལས་གཞན་པ་ལ་དམིགས་པར་འགྱུར། འོ་ན་ནི་དེའི་ཚེ་རེག་པ་ནི༌[^1805]གྱུར་པའི་རྣམ་པར་ཤེས་པ་ཚོར་བ་མེད་པ་ཡིན་ལ། དེའི་སྔོན་རོལ་གྱི་རྣམ་པར་ཤེས་པའི༌[^1806]ཚོར་བ་དང་བཅས་པ་གང་ཡིན་པ་དེ་ནི་རེག་པ་མ་ཡིན་ཏེ་རྐྱེན་མ་ཚང་བའི་ཕྱིར་རོ། །

[Block 3163]
དེ་ལྟ་ཡིན་ན་ཉེས་པ་ཅི་ཞིག་ཡོད། །སེམས་ཅན་ཐམས་ཅད་ལ་ས་མང་པོ་པ་བཅུ་ཡོད་དོ་ཞེས་བྱ་བ་ས་མང་པོ་པའི་ངེས་པ་ཉམས་པ་ཡིན་ནོ། །

[Block 3164]
ངེས་པ་འདི་ག་ལས༌[^1807]གྲུབ། བསྟན་བཅོས་ལས་སོ། །

[Block 3165]
ཁོ་བོ་ཅག་ནི་མདོ་ཚད་མར་བྱེད་པ་ཡིན་གྱི། ཁོ་བོ་ཅག་བསྟན་བཅོས་ཚད་མར་བྱེད་པ་ནི་མ་ཡིན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་མདོ་སྡེ་ལ་བརྟེན་པར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 3166]
ཡང་ན་སེམས་ཐམས་ཅད་ལ་ཡོད་དོ་ཞེས་བྱ་བ་འདི་ས་མང་པོ་པའི་དོན་མ་ཡིན་ནོ། །

[Block 3167]
འོ་ན་ས་མང་པོ་པའི་དོན་གང་ཡིན༌[^1808]ཞེ་ན། ས་ནི༌[^1809]གསུམ་སྟེ། རྟོག་པ་དང་བཅས་ཤིང་དཔྱོད་པ་དང་བཅས་པའི་ས་དང་། རྟོག་པ་མེད་ལ་དཔྱོད་པ་ཙམ་དང་། རྟོག་པ་ཡང་མེད་དཔྱོད་པ་ཡང་མེད་པའི་ས་དང་། དགེ་བའི་ས་དང་། མི་དགེ་བའི་ས་དང་། ལུང་དུ་མ་བསྟན་པའི་ས་དང་། ཡང་གསུམ༌[^1810]སྟེ། སློབ་པའི་ས་དང་། མི་སློབ་པའི་ས་དང་། སློབ་པ་ཡང་མ་ཡིན་མི་སློབ་པ་ཡང་མ་ཡིན་པའི་སའོ། །

[Block 3168]
དེ་ལ་གང་དག་ས་འདི་དག་ཐམས་ཅད་ན་ཡོད་པ་དེ་དག་ནི་ས་མང་པོ་པ་ཡིན་ནོ། །

[Block 3169]
གང་དག་དགེ་བ་ཁོ་ན་ལ་ཡོད་པ་དེ་དག་ནི་དགེ་བའི་ས་མང་པོ་པ་ཡིན་ནོ། །

[Block 3170]
གང་དག་ཉོན་མོངས་པ་ཅན་ཁོ་ན་ལ་ཡོད་པ་དེ་དག་ནི་ཉོན་མོངས་པའི་ས་མང་པོ་པ་ཡིན་ནོ། །

[Block 3171]
གཞན་དག་ན་རེ་དེ་དག་ནི་ཅི་རིགས་པར་རྣམ་གྲངས་ཀྱིས་ཡིན་གྱི། ཐམས་ཅད་ཅིག་ཅར་ནི་མ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 3172]
མི་དགེ་བའི་ས་མང་པོ་པ༌[^1811]རྣམས་ནི་འདོན་པའི་ཞར་ལ་དེ་ཁོང་ནས་དྲངས་ཀྱི་སྔོན་ནི་མ་བསྟན་ཏོ། །

[Block 3173]
གལ་ཏེ་རེག་པའི་འོག་ཏུ་ཚོར་བ་འབྱུང་ངོ་ཞེ་ན། མིག་དང་གཟུགས་རྣམས་ལ་བརྟེན་ནས༌[^1812]མིག་གི་རྣམ་པར་ཤེས་པ་དང་། གསུམ་འདུས་པའི་རེག་པ་དང་། ལྷན་ཅིག་སྐྱེས་པའི་ཚོར་བ་དང་། འདུ་ཤེས་དང་། སེམས་པ་སྐྱེའོ་ཞེས་གསུངས་པའི་མདོའི་ལན་གདབ་པར་བྱ་དགོས་སོ། །

[Block 3174]
ལྷན་ཅིག་སྐྱེས་པ་ཞེས་གསུངས་སོ། །

[Block 3175]
[^1813]རེག་པ་དང་ལྷན་ཅིག་སྐྱེས་པ་ཞེས་ནི་མ་གསུངས་ན། འདི་ལ་ལན་གདབ་ཏུ་ཅི་ཞིག་ཡོད། ལྷན་ཅིག་ཅེས་བྱ་བའི་སྒྲ༌[^1814]ནི་དེ་མ་ཐག་པ་ལ་ཡང་མཐོང་སྟེ། དཔེར་ན་བྱམས་པ་དང་ལྷན་ཅིག་པར་འགྱུར་བའི༌[^1815]དྲན་པ་ཡང་དག་པར༌[^1816]བྱང་ཆུབ་ཀྱི་ཡན་ལག་སྒོམ་པར་བྱེད་དོ་ཞེས་བྱ་བ་ལྟ་བུ་ཡིན་པས་འདི་ནི་ཁུངས་སུ་མི་རུང་ངོ་། །འོ་ན་མདོ་ལས་ཚོར་བ་གང་ཡིན་པ་དང་། སེམས་པ་གང་ཡིན་པ་དང་། འདུ་ཤེས་གང་ཡིན་པ་དང་། རྣམ་པར་ཤེས་པ་གང་ཡིན་པའི་ཆོས་དེ་དག་ནི་འདྲེས་པ་ཡིན་གྱི་མ་འདྲེས་པ་ནི་མ་ཡིན་ནོ་ཞེས་གང་གསུངས་པ་ཇི་ལྟར་དྲང་། དེ་ལྟ་བས་ན་ཚོར་བ་ལ་སོགས་པ་དག་ཀྱང་མ་འདྲེས་པའི་རྣམ་པར་ཤེས་པ་ནི་མེད་དོ། །

[Block 3176]
རེ་ཞིག་འདྲེས་པའི་དོན་ཅི་ཡིན་པ་འདི་དཔྱད་པར་བྱ་སྟེ། མདོ་དེ་ཉིད་ལས་འདི་སྐད་དུ། །གང་མྱོང་བར་བྱེད་པ་དེ་སེམས་པར་བྱེད་དོ། །

[Block 3177]
གང་སེམས་པར་བྱེད་པ་དེ། འདུས་ཏེ་ཤེས་པར་བྱེད་དོ། །

[Block 3178]
གང་འདུས་ཏེ་ཤེས་པར་བྱེད་པ་དེ་རྣམ་པར་ཤེས་པར་བྱེད་དོ་ཞེས་གསུངས་ན། ཅི་རེ་ཞིག་འདི་དེ་དག་གིས༌[^1817]དམིགས་པར་ངེས་པར་གསུངས་སམ། འོན་ཏེ་སྐད་ཅིག་མ་ལ་ངེས་པར་གསུངས་པ་དེ་མི་ཤེས་སོ། །

[Block 3179]
ཚེ་དང་དྲོད་དག་ལྷན་ཅིག་པ་ལ་འདྲེས་པ་ཞེས་གསུངས་པའི་ཕྱིར་སྐད་ཅིག་མ་ལ་ངེས་པ་ཡིན་པར་གྲུབ་བོ། །

[Block 3180]
གང་ཡང་མདོ་ལས་གསུམ་འདུས་པའི་རེག་པ་ཞེས་གསུངས་པས་དེ་ཡང་ཇི་ལྟར་ན་རྣམ་པར་ཤེས་པ་ནི་ཡོད་ལ། གསུམ་འདུས་པ་ནི་མ་ཡིན་པ་འམ། ཡང་ན་འདུས་པ་ཡིན་ལ་རེག་པ་མ་ཡིན། དེ་ལྟ་བས་ན་གདོན་མི་ཟ་བར་རྣམ་པར་ཤེས་པ་ཐམས་ཅད་ལ་རེག་པ་དང་། རེག་པ་དང་ལྷན་ཅིག་སྐྱེས་པའི་ཚོར་བ་ཡང་འདོད་པར་བྱའོ། །

[Block 3181]
ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་གཏམ་གྱིས་ཆོག་གི་དཀྱུས་མ་ཁོ་ན་རིམ་གྱིས་བརྗོད་པར་བྱའོ། །

[Block 3182]
སེམས་ལས་བྱུང་བ་ཚོར་བ་མདོར་བཤད་ཟིན་ཏོ། །

[Block 3183 [HEADING]]
###### ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་བཅོ་བརྒྱད། ^3-1-11-13-2-0

[Block 3184 [VERSE]]
དེ་ཡིད་ཉེ་བར་རྒྱུ་བ་ལས། །
རྣམ་པ་དག་ནི་ཡང་བཅོ་བརྒྱད། །

[Block 3185]
ཡང་སེམས་ལས་བྱུང་བའི་ཚོར་བ་དེ་ཉིད་ཡིད་ཀྱི༌[^1818]ཉེ་བར་རྒྱུ་བ་བཅོ་བརྒྱད་རྣམ་པར་གཞག་པ་ལས་རྣམ་པ་བཅོ་བརྒྱད་དུ་དབྱེའོ། །

[Block 3186]
ཡིད་ཀྱི་ཉེ་བར་རྒྱུ་བ་བཅོ་བརྒྱད་གང་ཞེ་ན། ཡིད་བདེ་བའི་ཉེ་བར་རྒྱུ་བ་དྲུག་དང་། ཡིད་མི་བདེ་བའི་ཉེ་བར་རྒྱུ་བ་དྲུག་དང་། བཏང་སྙོམས་ཀྱི་ཉེ་བར་རྒྱུ་བ་དྲུག་གོ། །

[Block 3187]
དེ་དག་ཇི་ལྟར་རྣམ་པར་བཞག །གལ་ཏེ་ངོ་བོ་ཉིད་ལས་ན༌[^1819]ནི་གསུམ་དུ་འགྱུར་ཏེ། ཡིད་བདེ་བ་དང་། ཡིད་མི་བདེ་བ་དང་། བཏང་སྙོམས་ཀྱི་ཉེ་བར་རྒྱུ་བ་དག་ཡིན་ནོ། །

[Block 3188]
འོན་ཏེ་མཚུངས་པར་ལྡན་པ་ལས་ན༌[^1820]ནི་ཡིད་དང་མཐུན་པར༌[^1821]ལྡན་པའི་ཕྱིར་གཅིག་ཏུ་འགྱུར་རོ། །

[Block 3189]
འོན་ཏེ་དམིགས་པ་ལས་ན་ནི་གཟུགས་ལ་སོགས་པ་ཡུལ་དྲུག་ལ་དམིགས་པའི་ཕྱིར་དྲུག་ཏུ་འགྱུར་རོ་ཞེ་ན། གསུམ་ཀར་ཡང་གཞག་སྟེ། དེ་དག་ལས་བཅོ་ལྔ་ནི་གཟུགས་ལ་སོགས་པ་ལ་ཉེ་བར་རྒྱུ་བ་ཡིན་ཏེ། གཟུགས་ལ་སོགས་པ་སོ་སོར་ངེས་པ་ལ་དམིགས་པའི་ཕྱིར་མ་འདྲེས་པ་ལ་དམིགས་པ་ཡིན་ནོ། །

[Block 3190]
ཆོས་ལ་ཉེ་བར་རྒྱུ་བ་གསུམ་ནི་རྣམ་པ་གཉི་ག་ཡིན་ནོ། །
--- END BLOCKS ---
