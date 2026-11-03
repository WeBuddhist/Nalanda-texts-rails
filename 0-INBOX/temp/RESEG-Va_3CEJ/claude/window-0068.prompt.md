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
[Block 2381 [HEADING]]
###### **གཟུགས་མེད་པ་ན་སྤྱོད་པའི་བཞི།** ^2-5-6-2-1-3-0

[Block 2382]
ད་ནི་གཟུགས་མེད་པ་ན་སྤྱོད་པའི་བཞི༌[^1246]བརྗོད་པར་བྱ་སྟེ། སྦྱོར་བ་ལས་བྱུང་བའི་མཇུག་ཐོགས་སུ་ནི་བདུན་ཏེ། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། རང་གི་བཞི་དང་། སློབ་པ་དང་། མི་སློབ་པའོ། །

[Block 2383]
དེ་ནི་སེམས་དྲུག་གི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་མ་གཏོགས་པ་རང་གི་གསུམ་དང་། སློབ་པ་དང་མི་སློབ་པ་དག་ལས་སོ། །

[Block 2384]
སྐྱེས་ནས་ཐོབ་པའི་མཇུག་ཐོགས་སུ་ནི་བདུན་ཏེ། རང་གི་བཞི་དང་། ས་འོག་མ་པའི་ཉོན་མོངས་པ་ཅན་དག་གོ། །

[Block 2385]
དེ་ནི་བཞི་ལས་ཏེ། རང་གི་དག་ཁོ་ན་ལས་སོ། །

[Block 2386]
ཉོན་མོངས་པ་ཅན་གྱི་མཇུག་ཐོགས་སུ་ནི་བརྒྱད་དེ། རང་གི་བཞི་དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བ་དང་། ཉོན་མོངས་པ་ཅན་དག་དང་། འདོད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་དག་གོ། །

[Block 2387]
དེ་ནི་བཅུའི་མཇུག་ཐོགས་སུ་འབྱུང་སྟེ། རང་གི་བཞི་དང་། འདོད་པ་དང་གཟུགས་ན་སྤྱོད་པའི་སྐྱེ་གནས༌[^1247]ཐོབ་པ་དང་། སྤྱོད་ལམ་པ་དང་། རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དག་ལས་སོ། །

[Block 2388]
རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པའི་མཇུག་ཐོགས་སུ་ནི་དྲུག་སྟེ། སྦྱོར་བ་ལས་བྱུང་བ་མ་གཏོགས་པ་རང་གི་གསུམ་དང་། འོག་མའི་ཉོན་མོངས་པ་ཅན་གསུམ་མོ། །

[Block 2389]
དེ་ནི་བཞི་ལས་ཏེ། རང་གི་དག་ཁོ་ན་ལས་སོ། །

[Block 2390 [HEADING]]
###### **སློབ་པ་དང་མི་སློབ་པ།** ^2-5-6-2-1-4-0

[Block 2391]
སློབ་པའི་མཇུག་ཐོགས་སུ་ནི་དྲུག་སྟེ། ཁམས་གསུམ་པའི་སྦྱོར་བ་ལས་བྱུང་བ་རྣམས་དང་། འདོད་པ་ན་སྤྱོད་པའི་སྐྱེ་གནས༌[^1248]ཐོབ་པ་དང་། སློབ་པ་དང་། མི་སློབ་པའོ། །

[Block 2392]
དེ་ནི་བཞི་ལས་ཏེ། སྦྱོར་བ་ལས་བྱུང་བ་གསུམ་དང་། སློབ་པ་ལས་སོ། །

[Block 2393]
མི་སློབ་པའི་མཇུག་ཐོགས་སུ་ནི་ལྔ་སྟེ། སློབ་པ་གཅིག་པུ༌[^1249]མ་གཏོགས་པ༌[^1250]སློབ་པའི་མཇུག་ཐོགས་ཇི་ལྟ་བ་བཞིན་དུ། དེ་ནི་ལྔ་ལས་ཏེ། སྦྱོར་བ་ལས་བྱུང་བ༌[^1251]གསུམ་དང་། སློབ་པ་དང་། མི་སློབ་པ་དག་ལས་སོ། །

[Block 2394]
ཅིའི་ཕྱིར་སྦྱོར་བ་ལས་བྱུང་བའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་ནི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་དང་། སྤྱོད་ལམ་པ་དང་། བཟོའི་གནས་པའི་སེམས་དག་འབྱུང་ལ། སྦྱོར་བ་ལས་བྱུང་བ་ནི་དེ་དག་ལས་མ་ཡིན་ཞེ་ན། དེ་དག་ནི་སྤྱོད་ལམ་དང་། བཟོ་མངོན་པར་འདུ་བྱ་བ་ལ་ཞུགས་པའི་ཕྱིར་དང་། སྟོབས་ཆུང་བ་དང་། མངོན་པར་འདུ་བྱ་བ་མེད་པར་འཇུག་པའི་ཕྱིར་སྦྱོར་བ་ལས་བྱུང་བའི་རྗེས་སུ་མཐུན་པ་མ་ཡིན་ནོ། །

[Block 2395]
འབྱུང་བའི་སེམས་ནི་མངོན་པར་འདུ་བྱ་བ་མེད་པར༌[^1252]འཇུག་པས་དེ་ནི་སྦྱོར་བ་ལས་བྱུང་བའི་སེམས་ཀྱི་མཇུག་ཐོགས་སུ་འབྱུང་བར་རིགས་སོ། །

[Block 2396]
དེ་ལྟ་ན་འོ་ན་ནི་ཉོན་མོངས་པ་ཅན་དག་ལས་ཀྱང་སྦྱོར་བ་ལས་བྱུང་བ་འབྱུང་བར་མི་འགྱུར་ཏེ། མི་མཐུན་པའི་ཕྱིར་རོ། །

[Block 2397]
འོན་ཀྱང་ཉོན་མོངས་པ་ཀུན་ཏུ་འབྱུང༌[^1253]བས་ཡོངས་སུ་སྐྱོ་བ་ལ་ནི་དེ་ཡོངས་སུ་ཤེས་པ་ལས་སྦྱོར་བ་ལས་བྱུང་བ་མངོན་དུ་འགྱུར་བར་རིགས་སོ། །

[Block 2398]
འདོད་པ་ན༌[^1254]སྤྱོད་པའི་སྐྱེ་གནས༌[^1255]ཐོབ་པ་ལ༌[^1256]ནི་གསལ་བའི་ཕྱིར་སློབ་པ་དང་། མི་སློབ་པ་དང་། གཟུགས་ན་སྤྱོད་པའི་སྦྱོར་བ་ལས་བྱུང་བའི་མཇུག་ཐོགས་སུ་འབྱུང་གི་མངོན་པར་འདུ་བྱ་བ་མེད་པར་འབྱུང་བའི་ཕྱིར་དེ་ལས་ནི་དེ་དག་མི་འབྱུང་ངོ་། །

[Block 2399]
གཟུགས་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་གྱི་མཇུག་ཐོགས་སུ་ནི་འདོད་པ་ན་སྤྱོད་པའི་སྐྱེ་གནས༌[^1257]ཐོབ་པ་འབྱུང་སྟེ། གསལ་བའི་ཕྱིར་རོ། །

[Block 2400]
གཟུགས་མེད་པ་ན་སྤྱོད་པའི་ཉོན་མོངས་པ་ཅན་གྱི་མཇུག་ཐོགས་སུ་ནི་གཟུགས་ན་སྤྱོད་པའི་སྐྱེ་གནས༌[^1258]ཐོབ་པ་མི་འབྱུང་སྟེ། མི་གསལ་བའི་ཕྱིར་རོ། །

[Block 2401 [HEADING]]
###### ཡིད་ལ་བྱེད་པ་གསུམ། ^2-5-6-2-2-0

[Block 2402]
ཡིད་ལ་བྱེད་པ་ནི་གསུམ་སྟེ། རང་གི་མཚན་ཉིད་ཡིད་ལ་བྱེད་པ་ནི་དཔེར་ན་གཟུགས་ནི་གནོད་པར་བྱར་རུང་བའི་མཚན་ཉིད་ཅན་ནོ་སྙམ་པ་དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 2403]
སྤྱིའི་མཚན་ཉིད་ཡིད་ལ་བྱེད་པ་ནི་རྣམ་པ་བཅུ་དྲུག་དང་ལྡན་པའོ། །

[Block 2404]
མོས་པ་ཡིད་ལ་བྱེད་པ་ནི་མི་སྡུག་པ་དང་། ཚད་མེད་པ་དང་། གཟུགས་ཅན་གྱི་རྣམ་པར་ཐར་པ་དང་། ཟིལ་གྱིས་གནོན་པའི་སྐྱེ་མཆེད་དང་། ཟད་པར་གྱི་སྐྱེ་མཆེད་ལ་སོགས་པ་དག་ལའོ། །

[Block 2405]
དེ་ལ་ཡིད་ལ་བྱེད་པ་རྣམ་པ་གསུམ་གྱི་མཇུག་ཐོགས་སུ་འཕགས་པའི་ལམ་མངོན་དུ་བྱེད་ལ། དེ་ལས་ཀྱང་ཡིད་ལ་བྱེད་པ་རྣམ་པ་གསུམ་སྟེ། དེ་ལྟ་ན་མི་སྡུག་པ་དང་། ལྷན་ཅིག་པའི་དྲན་པ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་སྒོམ་པར་བྱེད་དོ་ཞེས་བྱ་བ་འདི་རིགས་པ་ཡིན་ནོ། །

[Block 2406]
གཞན་དག་ན་རེ་སྤྱི་ཡིད་ལ་བྱེད་པ་ཁོ་ནའི་མཇུག་ཐོགས་སུ་འཕགས་པའི་ལམ་མངོན་དུ་བྱེད་ལ། དེ་ལས་ནི་རྣམ་པ་གསུམ་སྟེ། མི་སྡུག་པས་སེམས་བཏུལ་ནས་སྤྱི་ཡིད་ལ་བྱེད་པའི་མཇུག་ཐོགས་སུ་འཕགས་པའི་ལམ་མངོན་དུ་བྱེད་པ་དེའི་ཕྱིར་བརྒྱུད་པ་ལས་དགོངས་ནས་མི་སྡུག་པ་དང་ལྷན་ཅིག་པའི་དྲན་པ་ཡང་དག་བྱང་ཆུབ་ཀྱི་ཡན་ལག་སྒོམ་པར་བྱེད་དོ་ཞེས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 2407]
གཞན་དག་ན་རེ་འཕགས་པའི་ལམ་གྱི་མཇུག་ཐོགས་སུ་ཡང་སྤྱི་ཡིད་ལ་བྱེད་པ་ཁོ་ནའོ་ཞེས་ཟེར་རོ། །

[Block 2408]
རེ་ཞིག་མི་ལྕོགས་པ་མེད་པ་ལ་སོགས་པ་ས་གསུམ་ལ་བརྟེན༌[^1259]ནས་ངེས་པ་ལ་འཇུག་ན་ནི་ལམ་དེ་རྣམས་ཀྱི་མཇུག་ཐོགས་སུ་འདོད་པ་ན་སྤྱོད་པའི་སྤྱི་ཡིད་ལ་བྱེད་པ་མངོན་དུ་བྱེད་པ༌[^1260]པར་འགྱུར་ན། གལ་ཏེ་བསམ་གཏན་གཉིས་པ་ལ་སོགས་པ་ལ་བརྟེན་ནས༌[^1261]ངེས་པ་ལ་འཇུག༌[^1262]ན་གོ་ཇི་ལྟར་ཏེ། ཤིན་ཏུ་བསྐལ་པའི་ཕྱིར་འདོད་པ་ན་སྤྱོད་པ༌[^1263]ནི་མི་ནུས་སོ། །

[Block 2409]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་མ་གཏོགས་པར་དེ་དག་གི་ས་པ་ཡང་མི༌[^1264]ཐོབ་པོ། །འཕགས་པ་ནི་ཡང་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་མངོན་དུ་མཛད་པ་ཡང་མ་ཡིན་ཏེ། འབྲས་བུ་ཐོབ་ཟིན་པ་དེའི་སྦྱོར་བ་མངོན་དུ་བྱེད་པ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2410]
དེས་ནི་དེ་དང་འདྲ་བའི་སྤྱི་ཡིད་ལ་བྱེད་པ་གཞན་ཡང་འདི་ལྟ་སྟེ། འདུ་བྱེད་ཐམས་ཅད་ནི་མི་རྟག་པའོ། །

[Block 2411]
ཆོས་ཐམས་ཅད་ནི་བདག་མེད་པའོ། །

[Block 2412]
མྱ་ངན་ལས་འདས་པ་ནི་ཞི་བའོ་སྙམ་པ༌[^1265]འཐོབ་པར་འགྱུར་ཏེ། དེ་མངོན་དུ་བྱེད་པར་འགྱུར་རོ། །

[Block 2413]
དེ་སྐད་དུ་ནི་མི་བརྗོད་དོ། །

[Block 2414]
མི་ལྕོགས་པ་མེད་པ་ལ་བརྟེན་ནས་དགྲ་བཅོམ་པ་ཉིད་འཐོབ་པའི་ལྡང་བའི་སེམས་ནི་དེའི་ས་པའམ༌[^1266]འདོད་པ་ན༌[^1267]སྤྱོད་པ་ཡིན་ནོ། །

[Block 2415]
ཅི་ཡང་མེད་པའི་སྐྱེ་མཆེད་ལ་བརྟེན་ནས་འཐོབ་པ༌[^1268]ནི་དེའི་ས་པའམ་སྲིད་པའི་རྩེ་མོ་པ་ཡིན་ནོ། །

[Block 2416]
ས་ལྷག་མ་རྣམས་སུ་ནི་རང་གི་ས་པ་ཁོ་ནའོ། །

[Block 2417]
འདོད་པའི་ཁམས་ན༌[^1269]ནི་ཡིད་ལ་བྱེད་པ་གསུམ་སྟེ། ཐོས་པ་དང་བསམས་པ་ལས་བྱུང་བ་དང་། སྐྱེས་ནས་ཐོབ་པ་རྣམས་སོ། །

[Block 2418]
གཟུགས་ཀྱི་ཁམས་ན་ནི་གསུམ་སྟེ། ཐོབ་པ༌[^1270]དང་བསྒོམས་པ་ལས་བྱུང་བ་དང་། སྐྱེས་ནས་ཐོབ་པ་རྣམས་སོ། །

[Block 2419]
བསམས་པ་ལས་བྱུང་བ་ནི་མེད་དོ། །

[Block 2420]
གང་གི་ཚེ་དེ་དག་སེམས་པར་རྩོམ་པ་དེའི་ཚེ་དེ་དག་གི་ཏིང་ངེ་འཛིན་ཁོ་ན་ཉེ་བར་གནས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
