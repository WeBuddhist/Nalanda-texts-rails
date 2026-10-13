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
[Block 2241]
དགེ་བའི་སེམས་ཀྱིས་ཀུན་ནས་བསླང་བའི་ཕྱིར་དང་། དེ་ཡང་གདོན་མི་ཟ་བར་མ་ཆགས་པ་ལ་སོགས་པ་དང་མཚུངས་པར་ལྡན་པའི་ཕྱིར་དགེ་བ་ཐམས་ཅད་རྩ་བ་གསུམ་ལས་སྐྱེས་པ་ཡིན་ནོ། །

[Block 2242]
དེ་མི་དགེ་བའི་ལས་ཀྱི་ལམ་གྱི་སྦྱོར་བ་སྤོང་བ་ནི་དགེ་བའི་ལས་ཀྱི་ལམ་གྱི་སྦྱོར་བ་ཡིན་ནོ། །

[Block 2243]
དངོས་སྤོང་བ་ནི་དངོས་ཡིན་ནོ། །

[Block 2244]
མཇུག་སྤོང་བ་ནི་མཇུག་ཡིན་ནོ། །

[Block 2245]
སྡོམ་པ་ལེན་པ་ན་ཡང་སྦྱོར་བ་དང་དངོས་དང་མཇུག་རྣམས་སྦྱར་བར་བྱའོ། །

[Block 2246]
སྦྱོར་བ་རྩ་བ༌[^892]གསུམ་ལས་སྐྱེས། །ཞེས་བྱ་བ་བཤད་ནས། གང་གིས་གང་ལ་མཐར་ཐུག་པ་དེ་བརྗོད་པར་བྱ་སྟེ།

[Block 2247 [VERSE]]
གསོད་དང་གནོད་སེམས་ཚིག་རྩུབ་པོ། །
ཞེ་སྡང་གིས་ནི་མཐར་ཕྱིན་བྱེད། །

[Block 2248]
ཡོངས་སུ་འདོར་བ་དང་རྩུབ་པའི་སེམས་མངོན་དུ་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2249 [VERSE]]
ལོག་གཡེམས༌[^893]བརྣབ་སེམས་མ་བྱིན་ལེན། །
ཆགས་པ་ཡིས་ནི་རྫོགས་པར་བྱེད། །
ལོག་པར་ལྟ་བ་གཏི་མུག་གིས། །

[Block 2250]
ཆེར་རྨོངས་པར་འགྱུར་བས་དེ་མཐར་ཕྱིན་པར་བྱེད་དོ། །

[Block 2251]
ལྷག་མ་གསུམ་གྱིས་རྫོགས་པར་འདོད། །བརྫུན་དུ་སྨྲ་བ་དང་། ཕྲ་མ་དང་། [^894]ཚིག་རྐྱལ་པ༌[^895]རྣམས་ནི་སྲིད་པ་བཞིན་དུ་གསུམ་གྱིས་མཐར་ཕྱིན་ཏོ། །

[Block 2252 [HEADING]]
##### ལས་ཀྱི་ལམ་གྱི་གཞི། ^4-3-9-2-0

[Block 2253]
གང་ལས་ཀྱི་ལམ་ཆ་བཞིར་བཤད་པ་དེ་དག་ནི་གསུམ་དང་། གསུམ་དང་། གཅིག་དང་། གསུམ་སྟེ་གོ་རིམས་བཞིན་དུ།

[Block 2254 [VERSE]]
གཞི་ནི་སེམས་ཅན་ལོངས་སྤྱོད་དང་། །
མིང་དང་གཟུགས་དང་མིང་ཡིན་ནོ། །

[Block 2255]
སྲོག་གཅོད་པ་ལ་སོགས་པའི་གཞི་ནི་སེམས་ཅན་ཡིན་ནོ། །

[Block 2256]
གཞན་གྱི་བུད་མེད་ཀྱི་གན་དུ་འགྲོ་བ་ལ་སོགས་པའི་གཞི་ནི་ལོངས་སྤྱོད༌[^896]ཡིན་ནོ། །

[Block 2257]
ལོག་པར་ལྟ་བའི་གཞི་ནི་མིང་དང་གཟུགས་སོ། །

[Block 2258]
བརྫུན་དུ་སྨྲ་བ་ལ་སོགས་པའི་གཞི་ནི་མིང་གི་ཚོགས་ཡིན་ནོ། །

[Block 2259]
གང་ཞིག་གིས་ཕ་རོལ་པོ་འཆི་བར་ངེས་པར་བྱས་ནས་དེ་དང་མགོ་མཉམ་དུའམ་སྔར་ཤི་བར་གྱུར་པ་དེ་ལ་ལས་ཀྱི་ལམ་དངོས་ཡོད་དམ། །འོན་ཏེ་མེད་ཅེ་ན།

[Block 2260 [VERSE]]
སྔ་དང་མཉམ་དུ་ཤི་བ་ལ། །
དངོས་མེད་ལུས་གཞན་སྐྱེས་ཕྱིར་རོ། །

[Block 2261]
ལུས་གང་གིས་དེ་ལ་སྦྱོར་བ༌[^897]བྱས་པ་དེ་ནི་ཆད་ལ་ལུས་གཞན་ཁོ་ན་ཞིག་བྱུང་སྟེ། དེ་ནི་སྦྱོར་བ་པོ་མ་ཡིན་པའི་ཕྱིར་ལས་ཀྱི་ལམ་དང་ལྡན་པར་རིགས་པ༌[^898]མ་ཡིན་ནོ། །

[Block 2262]
གང་དམག་གིས་གདབ་པ་དང་། ལིངས་འདེབས་པ་དང་། མ་འཁྲིགས་པར༌[^899]གདབ་པ༌[^900]དག་ཏུ་ཕ་རོལ་པོ་གསད་པར༌[^901]བྱ་བའི་ཕྱིར་མང་པོ་ཚོགས་པས་བཏབ་ལ། གཅིག་གཅིག༌[^902]གིས་སྲོག་གཅོད་ན་དེ་དང་སུ་ཞིག་ལྡན་པར་འགྱུར་ཞེ་ན།

[Block 2263 [VERSE]]
དམག་ལ་སོགས་པ་དོན་གཅིག་ཕྱིར། །
ཐམས་ཅད་བྱེད་པ་པོ་བཞིན་ལྡན། །

[Block 2264]
དོན་གཅིག་པའི་ཕྱིར་ཐམས་ཅད་བྱེད་པ་པོ་ཇི་ལྟ་བ་བཞིན་དུ་ལྡན་པར་འགྱུར་ཏེ། དེ་དག་ནི་དོན་གྱིས་ན། ཕན་ཚུན་དུ་སྦྱོར་བར༌[^903]བྱེད་པ་ཡིན་ནོ། །

[Block 2265 [HEADING]]
##### སྲོག་གཅོད་པ་ནས་ལོག་པར་ལྟ་བའི་བར་གྱི་མཚན་ཉིད། ^4-3-9-3-0

[Block 2266]
ཡང་སྲོག་གཅོད་པའི་མཚན་ཉིད་ནས་ལོག་པར་ལྟ་བའི་བར་གྱི་མཚན་ཉིད་ཅི་ཞེ་ན། །སྲོག་གཅོད་པ་ནི་བསམས་བཞིན་དུ་མ་ནོར་བར་ནི་གཞན་བསད༌[^904]པའོ། །

[Block 2267]
གལ་ཏེ་འདི་བསད་དོ་སྙམ་དུ་བསམས་ནས་གསོད་པར་བྱེད་ལ། གཞན་དང་མ་ནོར་བར་དེ་ཉིད་གསོད་པར་བྱེད་ན་དེ་ཙམ་གྱིས་སྲོག་གཅོད་པ་ཡིན་ནོ། །

[Block 2268 [VERSE]]
མ་བྱིན་ལེན་པ་གཞན་གྱི་ནོར། །
མཐུ་དང་འཇབ་བུས་བདག་གིར་བྱེད། །

[Block 2269]
གལ་ཏེ་གཞན་གྱི་བདག་གིར་བྱས་པ་ལ་མཐུ་དང་འཇབ་བུས་བདག་གིར་བྱེད་ཅིང་། གང་མཐུ་དང་འཇབ་བུས་བདག་གིར་བྱ་བར་བསམས་པ་དེ་ལས་གཞན་དུ་འདུ་ཤེས་ཀྱང་མ་འཁྲུལ་ན་དེ་ཙམ་གྱིས་མ་བྱིན་པར་ལེན་པ་ཡིན་ནོ། །

[Block 2270 [VERSE]]
བགྲོད་མིན་བགྲོད་པར་འདོད་པ་ཡིས། །
ལོག་པར་གཡེམ་པ་རྣམ་པ་བཞི། །

[Block 2271]
བགྲོད་པར་བྱ་བ་མ་ཡིན་པ་ལ་འགྲོ་བ་བགྲོད་པར༌[^905]བྱ་བ་མ་ཡིན་པ་གཞན་གྱིས་ཡོངས་སུ་བཟུང་བའམ། མའམ་བུ་མོ་ལ་སོགས་པའོ། །

[Block 2272]
ཡན་ལག་མ་ཡིན་པར་འགྲོ་བ་སྐྱེ་གནས་མ་ཡིན་པར་རོ། །

[Block 2273]
ཡུལ་མ་ཡིན་པར་འགྲོ་བ་སྣང་བའམ་མཆོད་རྟེན་ལ་སོགས་པའོ། །

[Block 2274]
དུས་མ་ཡིན་པར་འགྲོ་བ་སྦྲུམ་མ་འམ་བྱིས་པ་གསོ་བ་དང་། ངེས་པ་དང་བཅས་པའི་གན་དུ་འགྲོ་བ་ལ་སོགས་པའོ། །

[Block 2275 [VERSE]]
བརྫུན་ཚིག་འདུ་ཤེས་གཞན་བསྒྱུར་བའི། །
ཚིག་དོན་མངོན་པར་གོ་བའོ། །

[Block 2276]
དོན་སྨྲ་བ་གང་ཡིན་པ་དེ་ལས་འདུ་ཤེས་གཞན་དུ་བསྒྱུར་ལ། དེས་གང་གི་དབང་དུ་བྱས་ནས་སྨྲས་པའི་ཚིག་དེའི་དོན་ཡང་གོ་ན་ཚིག་དེའི་བརྫུན་དུ་སྨྲ་བ་ཡིན་ནོ། །

[Block 2277]
མདོ་ལས་ཐ་དད༌[^906]བཅུ་དྲུག་གསུངས་པ་དེ་ནི་མ་མཐོང་བ་ལ་མཐོང་ཞེས་སྨྲ་བ་ནས་མི་ཤེས་པར་ཤེས་སོ་ཞེས་པའི་བར་ལ་སོགས་པའོ། །

[Block 2278]
མཐོང་བ་དང་། ཐོས་པ་དང་། རྟོགས་པ་དང་། རྣམ་པར་ཤེས་པ་དག་གི་མཚན་ཉིད་ཅི་ཞེ་ན། མིག་རྣ་ཡིད་ཀྱི་རྣམ་ཤེས་དང་།

[Block 2279 [VERSE]]
གསུམ་གྱིས༌[^907]ཉམས་སུ་མྱོང་གང་དེ། །
མཐོང་ཐོས་རྣམ་པར་ཤེས་པ་དང་། །
རྟོགས་པ་ཡིན་ཏེ་རིམ་བཞིན་བཤད། །

[Block 2280]
མིག་གི་རྣམ་པར་ཤེས་པས་ཉམས་སུ༌[^908]མྱོང་བ་དེ་ནི་མཐོང་བ་དང་། རྣ་བའི་རྣམ་པར་ཤེས་པས་མྱོང་བ་དེ་ནི་ཐོས་པ་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པས༌[^909]མྱོང་བ་དེ་ནི་རྣམ་པར་ཤེས་པ་དང་། སྣ་དང་། ལྕེ་དང་། ལུས་ཀྱི་རྣམ་པར་ཤེས་པས་མྱོང་བ་ནི་རྟོགས་པ་ཞེས་བཤད་དོ། །
--- END BLOCKS ---
