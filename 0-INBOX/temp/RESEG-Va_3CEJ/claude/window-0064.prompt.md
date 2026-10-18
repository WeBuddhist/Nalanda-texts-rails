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
སྐྱེ་བ་ཞེས་བྱ་བ་ནི་མ་འོངས་པ་སྟེ། སྐྱེ་བ་ལ་མངོན་དུ་ཕྱོགས་པ་ཡིན་ནོ། །

[Block 2242]
དེ་ལ་ནི་སྐལ་བ་མཉམ་པ་དང་། ཀུན་ཏུ་འགྲོ་བ་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུ་རྣམས་བྱ་བ་བྱེད་དེ། རེ་ཞིག་རྒྱུའི་རྐྱེན་ནི་དེ་ལྟ་བུ་ཡིན་ནོ།[^1178] །དེ་ལས་གཞན་པའི་རྐྱེན་དག་དེ་ལས་བཟློག་པ་ཡིན། མཚུངས་པ་དེ་མ་ཐག་པ་དང་། དམིགས་པའི་རྐྱེན་དག་ནི་བྱེད་པའི་ཚུལ་གང་གིས་རྒྱུའི་རྐྱེན་རྣམ་པ་གཉིས་སུ་བྱས་ནས་བཤད་པ་དེ་ལས་བཟློག་པར་རིག་པར་བྱ་སྟེ། མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ནི་སྐབས་འབྱེད་པའི་ཕྱིར་སྐྱེ་བ་ལ་བྱ་བ་བྱེད་དོ། །

[Block 2243]
དམིགས་པའི་རྐྱེན་ནི་ད་ལྟར་གྱི་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཀྱིས་འཛིན་པའི་ཕྱིར་འགག་པ་ལ་བྱ་བ་བྱེད་དོ། །

[Block 2244]
བདག་པོའི་རྐྱེན་ནི་གནས་སྐབས་ཐམས་ཅད་དུ་མི་སྒྲིབ་པའི་ངོ་བོར་གནས་པས་འདིའི་བྱ་བ་ནི་འདི་ཉིད་ཡིན་ནོ། །

[Block 2245]
རྐྱེན་རྣམས་བྱེད་པ་དང་བཅས་པར་བཤད་ཟིན་ཏོ། །

[Block 2246 [HEADING]]
#### ཆོས་གང་ཞིག་རྐྱེན་དུ་ཞིག་གིས་སྐྱེད་པ། ^2-5-3-0

[Block 2247]
ཡང་ཆོས་གང་ཞིག་རྐྱེན་དུ་ཞིག་གིས་སྐྱེད༌[^1179]ཅེ་ན། བཞི་ཡིས་སེམས་དང་སེམས་བྱུང་རྣམས། །དེ་ལ་འདི་དག༌[^1180]རྒྱུའི་རྐྱེན་ནི་རྒྱུ་ལྔ་པོ་ཐམས་ཅད་དོ། །

[Block 2248]
མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ནི་སེམས་དང་སེམས་ལས་བྱུང་བ་སྔ་མ་གཞན་དག་གི་བར་དུ་མ་ཆོད་པ་རྣམས་སོ། །

[Block 2249]
དམིགས་པའི་རྐྱེན་ནི་ཅི་རིགས་པར་ཡུལ་ལྔ་པོ་དག་དང་ཆོས་ཐམས་ཅད་དོ། །

[Block 2250]
བདག་པོའི་རྐྱེན་ནི་རང་གི་ངོ་བོ་མ་གཏོགས་པ་ཆོས་ཐམས་ཅད་དོ། །

[Block 2251]
གསུམ་གྱིས་སྙོམས་པར་འཇུག་པ་གཉིས། །འགོག་པ་དང་འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་དག་ལ་ནི་དམིགས་པའི་རྐྱེན་མེད་དེ།

[Block 2252 [VERSE]]
དེ་དག་ནི་དམིགས་པར་བྱེད་པ་མ་ཡིན་ནོ། །
དེ་གཉིས་ཀྱི་རྒྱུའི་རྐྱེན་ནི་རྣམ་པ་གཉིས་ཏེ།
ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་ནི་སྐྱེ་བ་ལ་སོགས་པའོ། །

[Block 2253]
སྐལ་བ་མཉམ་པའི་རྒྱུ་ནི་ས་མཚུངས་པའི་དགེ་བའི་ཆོས་སྔར་བྱུང་བ་རྣམས་སོ། །

[Block 2254]
མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ནི་སྙོམས་པར་འཇུག་པའི་སེམས་མཚུངས་པར་ལྡན་པ་དང་བཅས་པའོ། །

[Block 2255]
བདག་པོའི་རྐྱེན་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 2256]
སྙོམས་པར་འཇུག་པ་འདི་དག་ནི་སེམས་ཀྱི་མངོན་པར་འདུ་བྱེད་པ་ལས་སྐྱེ་བའི་ཕྱིར། སེམས་ཀྱི་མཚུངས་པ་དེ་མ་ཐག་པ་ཅན་དག་ནི་ཡིན་གྱི་སེམས་སྐྱེ་བ་ལ་བགེགས་བྱེད༌[^1181]པའི་ཕྱིར་མཚུངས་པ་དེ་མ་ཐག་པའི་རྐྱེན་ནི་མ་ཡིན་ནོ། །

[Block 2257]
གཞན་ནི་གཉིས་པོ་དག་ལས་སྐྱེ། །ཆོས་གཞན་ལྡན་པ་མ་ཡིན་པ་རྣམས་དང་གཟུགས་ཅན་རྣམས་ནི་རྒྱུ་དང་བདག་པོའི་རྐྱེན་དག་ལས་སྐྱེའོ། །

[Block 2258 [HEADING]]
#### འགྲོ་བ་ཐམས་ཅད་ཀྱི་རྒྱུ་གཅིག་པུ་དབང་ཕྱུག་ལ་སོགས་པ་མེད་པ། ^2-5-4-0

[Block 2259]
དངོས་པོ་རྣམས་ནི་ཇི་སྐད་བཤད་པའི་རྒྱུ་དང་རྐྱེན་རྣམས་ཁོ་ན་ལས་སྐྱེའི་འགྲོ་བ་ཐམས་ཅད་ཀྱི་རྒྱུ་གཅིག་པུ་དབང་ཕྱུག་དང་སྐྱེས་བུ་དང་། གཙོ་བོ་ལ་སོགས་པ་ནི་མེད་དོ་ཞེས་བྱ་བ་འདི་ལ་གཏན་ཚིགས་ཅི་ཞིག་ཡོད། གལ་ཏེ་གཏན་ཚིགས་ཀྱིས་བྱས་པའི་གྲུབ་པར་སེམས་ན་དེ་ཉིད་ཀྱིས་ཐམས་ཅད་ཀྱི༌[^1182]རྒྱུ་དབང་ཕྱུག་ལ་སོགས་པ་ཅིག་ཅར་དུ༌[^1183]ཞིག་ཡིན་ནོ་ཞེས་བྱ་བའི་སྨྲ་བ་འདི་བསྩལ་བ༌[^1184]མ་ཡིན་ནམ། གཞན་ཡང་། དབང་ཕྱུག་སོགས་མིན་རིམ་སོགས་ཕྱིར། །གལ་ཏེ་དབང་ཕྱུག་གམ། གཞན་ཡང་རུང་སྟེ་རྒྱུ་གཅིག་པུ་ཁོ་ན་ཞིག་ཡིན་ན་འགྲོ་བ་ཐམས་ཅད་ཅིག་ཅར་དུ་འབྱུང་བར་འགྱུར་བ་ཞིག་ན།

[Block 2260 [VERSE]]
དངོས་པོ་རྣམས་ནི་རིམ་གྱིས་འབྱུང་བ༌[^1185]ཡང་སྣང་ངོ་། །
དེ་ནི་འདི་ནི་ད་ལྟར་སྐྱེ་བར་གྱུར་ཅིག །

[Block 2261]
འདི་ནི་འགག་པར་གྱུར་ཅིག །འདི་ནི་ཕྱིས་སྐྱེ་བར་གྱུར་ཅིག་ཅེས་དབང་ཕྱུག་གི་འདོད་པའི་དབང་གིས་ཡིན་ནོ། །

[Block 2262]
འོ་ན་ནི་འདོད་པ་ཐ་དད་པའི་ཕྱིར་རྒྱུ་དུ་མར་འགྲུབ་པར་འགྱུར་ལ། འདོད་པ་ཐ་དད་པ་དེ་ཡང་དེའི་རྒྱུའི༌[^1186]དབང་ཕྱུག་ལ་ཐ་དད་པ་མེད་པའི་ཕྱིར་ཅིག་ཅར་འབྱུང་བར་འགྱུར་རོ། །

[Block 2263]
འོན་ཏེ་རྒྱུ་གཞན་ལ་ལྟོས་ན་ནི་དབང་ཕྱུག་རྒྱུ་མ་ཡིན་པ་ཁོ་ནར་འགྱུར་ལ། དེ་དག་ཀྱང་རིམ་གྱིས་སྐྱེ་བ་ལ་རྒྱུ་གཞན་གྱི་བྱེ་བྲག་ལ་ལྟོས་པའི་ཕྱིར་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་བས་རྒྱུ་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་བྱེ་བྲག་མཐའ་ཡས་པ་ཐོག་མ་མེད་པ་ཉིད་དུ་ཁས་བླངས་པའི་ཕྱིར་དབང་ཕྱུག་གི་རྒྱུར་མོས་པ་འདི་ནི་ཤཱཀྱའི་སྲས་པོའི་ལུས༌[^1187]ཁོ་ན་ལས་མ༌[^1188]འདས་པ་ཡིན་ནོ། །

[Block 2264]
གལ་ཏེ་དབང་ཕྱུག་གི་འདོད་པ་རྣམས༌[^1189]ཅིག་ཅར་ཡིན་དུ་ཟིན་ཀྱང་འགྲོ་བ་ནི་ཅིག་ཅར་མ་ཡིན་ཏེ། འདོད་པ་ཇི་ལྟ་བར་སྐྱེ་བའི་ཕྱིར་རོ་ཞེ་ན་མ་ཡིན་ཏེ། དེ་དག་ལ་ཕྱིས་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 2265]
རེ་ཞིག་དབང་ཕྱུག་གི་འབྱིན་པའི་ཚེགས་འདི་རྙེད༌[^1190]ལ་དོན་ཅི་ཞིག་ཡོད། གལ་ཏེ་དགའ་བ་ཡིན་ནོ་ཞེ་ན། འོ་ན་ནི་ཐབས་མེད་པར་དེ་བྱེད་པར་མི་ནུས་པས་དེ་ལ་དབང་ཕྱུག་མ་ཡིན་པར་འགྱུར་ཏེ། གཞན་ལ་ཡང་དེ་ཁོ་ན་དང་འདྲའོ། །

[Block 2266]
གལ་ཏེ་ཡང་དབང་ཕྱུག་དམྱལ་བ་ལ་སོགས་པར་སྐྱེ་དགུ་གནོད་པ་མང་པོ་དང་འབྲེལ་པ་དག་ཕྱུང་ནས་དེས་དགའ་བར་འགྱུར་ན་ནི་དེ་ལྟ་བུའི་དབང་ཕྱུག་དེ་ལ་ཕྱག་འཚལ་ལོ། །

[Block 2267]
དེ་ལས་བརྩམས་ནས།

[Block 2268 [VERSE]]
གང་ཕྱིར་མ་ལུས་སྲེག་པ་དང་། །
གང་ཕྱིར་རྣོ་དང་གང་ཕྱིར་གཏུམ། །
གང་ཕྱིར་གདུང་ལྡན་གང་གི་ཕྱིར། །
ཤ་དང་ཁྲག་དང་རྐང་ཟ་བ། །

[Block 2269]
དེ་ཕྱིར་དྲག་པོ་ཞེས་བྱའོ། །ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདི་ཡང་ལེགས་པར་སྨྲས་པ་ཡིན་ནོ། །

[Block 2270]
ཡང་འགྲོ་བའི་རྒྱུ་གཅིག་ཏུ་ཡོངས་སུ་བཟུང་བས་དོན་གཞན་དག་གི་སྐྱེས་བུའི་བྱེད་པ་མངོན་སུམ་ནི་བསྙོན་པར་འགྱུར་རོ། །

[Block 2271]
རྒྱུ་རྣམས་དང་བཅས་པའི་དབང་ཕྱུག་ལ་ཡང་རྒྱུར་རྟོག་པ་རྣམས་ནི་གུས་པས་སྨྲ་བ་འབའ་ཞིག་ཏུ་ཟད་དེ། རྒྱུ་རྣམས་ལས་གཞན་གྱིས༌[^1191]བྱེད་པ་མི་སྣང་བའི་ཕྱིར་རོ། །

[Block 2272]
དབང་ཕྱུག་དེ་ལྷན་ཅིག་བྱེད་པའི་རྒྱུ་དང་པོ༌[^1192]རྣམས་ལ་ཡང་དབང་ཕྱུག་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 2273]
འོན་ཏེ་དང་པོ་བྱུང་བ་དབང་ཕྱུག་གི་རྒྱུ་ལས་བྱུང་བ་ཡིན་ནོ་ཞེ་ན། དེ་ཡང་རྒྱུ་གཞན་ལ་མི་ལྟོས་པའི་ཕྱིར་དབང་ཕྱུག་བཞིན་དུ་ཐོག་མ་མེད་པ༌[^1193]ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 2274]
དེ་བཞིན་དུ་གཙོ་བོ་ལ་ཡང་ཅི་རིགས་པར་བརྗོད་པར་བྱའོ། །

[Block 2275]
དེ་ལྟ་བས་ན༌[^1194]འཇིག་རྟེན་གྱི་རྒྱུ་གཅིག་པུ་ནི་མེད་ཀྱི་འདི་ནི་རང་གི་ལས་རྣམས་ཁོ་ནས་སྐྱེ་བ་དེ་དང་དེར་སྐྱེ་བར་བྱེད་དོ། །

[Block 2276]
ཉོན་མོངས་བློ་མ་སྦྱངས་པ་རྣམས༌[^1195]ནི་རང་རང་གི་རྣམ་པར་སྨིན་པའི་འབྲས་བུ་དང་། སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུ་ཉམས་སུ་མྱོང་བ་ན་ལོག་པར་གཞན་དབང་ཕྱུག་ཏུ་ཡོངས་སུ་རྟོག་པར་བྱེད་དོ། །

[Block 2277]
དེ་ནི་རྫོགས་སོ།། །།

[Block 2278 [HEADING]]
#### འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པའི་རྒྱུའི་རྐྱེན། ^2-5-5-0

[Block 2279]
ཡང་། གཞན་ནི་གཉིས་པོ་དག་ལས་སྐྱེ། །ཞེས་གང་བཤད་པ་དེ་ཇི་ལྟར་ན་འབྱུང་བ་རྣམས་འབྱུང་བ་རྣམས་ཀྱི་རྒྱུའི་རྐྱེན་ཡིན་ཞེ་ན། དེ་ཡི་འབྱུང་བ་རྣམ་པ་གཉིས། ། འབྱུང་བའི་རྒྱུ་ཞེས་བྱ་བའི་ཐ་ཚིག་སྟེ། སྐལ་བ་མཉམ་པ་དང་ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་དག་གིས་སོ། །

[Block 2280]
འབྱུང་ལས་གྱུར་པའི་རྣམ་པ་ལྔ། །བྱུང་བ་རྣམས་འབྱུང་བ་ལས་གྱུར་པའི་ནི་རྒྱུ༌[^1196]རྣམ་པ་ལྔ་ཡིན་ཏེ། ཇི་ལྟ་ཞེ་ན།
--- END BLOCKS ---
