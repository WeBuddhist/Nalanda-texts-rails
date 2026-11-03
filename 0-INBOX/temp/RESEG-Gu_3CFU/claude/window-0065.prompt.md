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
[Block 2276]
བསྣན་པ༌[^1578]ལ་གང་ཞིག་མཚན་མ་ལ་ཇི་ལྟར་ཐོབ་པའི༌[^1579]གཞན་དུ་གཞག་པ་ཡང་དེ་ཉིད་དོ༌[^1580]ཞེས་བྱ་བ་ནི་དོར་བྱེད་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 2277]
ཐམས་ཅད་དུ་དབང་བྱེད་པའི་མདོ་ཡིན་ནོ། །

[Block 2278]
རྒྱན་གྱི་དབང་དུ་བྱེད་པ་ཉིད་མ་ཡིན་ནོ། །

[Block 2279]
དེ་ལ་གྲུབ་པ་ན་བརྐུས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་དེ་ལ་ཞེས་བྱ་བ་ནི་གྲངས་ལའོ། །

[Block 2280]
གྲུབ་པ་ན་ཞེས་བྱ་བ་ནི་ཐོབ་པ་སྟེ་ནོར་ལ་བརྐུས་པ་ཡིན་ནོ། །

[Block 2281]
དེ་བས་ན་འདིར་དོར་བྱེད་ན་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་དོ། །

[Block 2282]
ཐོབ་པའི་ཕྱིར་དེ་མ་ཐག་པའི་བྱ་བ་ལ་སྦྱོར་བ་ཉིད་དོ། །

[Block 2283]
སླར་ཐོབ་པ་ནི་འདིའི་བདག་ཉིད་དམ་དེ་ལས་གཞན་པའི་གང་ཟག་བསྟན་པ་དང་། བྱ་བ་འགའ་ཞིག་ལ་དེའི་ངེས་པར་སྦྱར་བས་སོ། །

[Block 2284]
ཚོམས་གཞན་དུ་བགྲང་བ་ཡང་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ཡང་རྙེད་པའི་ཕྱིར་བདག་ཉིད་ཚོམས་གཞན་དུ་བགྲང་བ་ཡང་དེ་དང་འདྲ་སྟེ། དེའི་གྲངས་ཀྱི་སྐབས་སུ་དོར་བྱེད་པ་དང་འདྲ་བར་བལྟ་བར་བྱའོ། །

[Block 2285]
འདིར་ཡང་བགྲང་བ་ནི་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་དེ་ཉེས་བྱས་ཉིད་དོ། །

[Block 2286]
གྲུབ་པའི་ཚེ་ནི་བརྐུས་པ་ཉིད་དོ།[^1581] །འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་རེ་ཞིག་བདག་ཉིད་ཚོམས་གཉི་གར་བགྲངས་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་སྦྱོར་བའི་ཉེས་བྱས་སུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2287]
སྔ་མ་ཉིད་ཕྱི་མ་དག་ལ༌[^1582]ཕྱི་མ་ཉིད་སྔ་མ་དག༌[^1583]ལ་བསྙོན་པ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་གི་སྒྲ་ནི་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་རྗེས་སུ་དྲང་བའི་དོན་དུའོ། །

[Block 2288]
སྔ་མའི་གྲངས་ལ་ཕྱི་མ་དག་ལ་ནི་ཚོམས་དག་ལ་ཐོག་མར་འདིར༌[^1584]བདག་ཉིད་བགྲང་བར་བྱས་པའི་ཚོམས་དེ་ལས་གཞན་དེ་རྣམས་ལས་བསྙོན་པའམ་གཞན་གྲངས་གཉིས་པ་གང་ཡིན་པ་དེ་ལ་ཚོམས་སྔ་མ་ཤོས་གང་ལ་དང་པོར་དེའི་གྲངས་བྱས་པ་དེའི་ཚོམས་ཡོངས་སུ་ཐོབ་པ་རྣམས་ལ་བསྙོན་པ་གང་ཞིག་དེ་ཡང་དེ་དང་འདྲ་བར་གྲངས་ཟིན་པ་དོར་བ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 2289]
འདིར་ཡང་ཚོམས་ལ་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་དེ་ཉེས་བྱས་སོ། །

[Block 2290]
གྲུབ་པའི་ཚེ་ནི་བརྐུས་པ་ཉིད་དོ། །

[Block 2291]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་རེ་ཞིག་བདག་ཉིད་བགྲང་དུ་སྩལ་བས༌[^1585]བསྙོན༌[^1586]ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་སྦྱོར་བའི་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2292]
སྐལ་བ་ཉིད་ནི་དེ་དག་གང་དུ་ཐམས་ཅད་ཀྱི་དང་པོར་བགྲངས་པ་དེར་རོ་ཞེས་བྱ་བ་ནི་གང་དུ་དེ་ཚོམས་ཐམས་ཅད་ཀྱི་དང་པོར་བགྲངས་པ་དེར་གཏོགས་སོ། །

[Block 2293]
དེ་ལ་སྐལ་བ་བླངས་པ་ལ༌[^1587]ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་དེ་ལ་འདི་ནི་བྱེད་པའོ། །

[Block 2294]
མི་དབང་བ་དབང་བར་སྒྲོགས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། ཡང་གི་སྒྲས་ནི་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་རྗེས་སུ་དྲང་བའི་དོན་དུའོ། །

[Block 2295]
འདིར་ཡང་དབང་བར་སྒྲོགས་པ་ནི་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་དེ་ཉེས་བྱས་སོ། །

[Block 2296]
གྲུབ་པའི་ཚེ་ན་ནི་བརྐུས་པ་ཉིད་དོ། །

[Block 2297]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་རེ་ཞིག་རྙེད་པ་གློ་བུར་བ་མི་དབང་བ་ལ་འདི་སྐད་ཅེས་བདག་ཀྱང་དབང་ངོ་ཞེས་དབང་བར་སྒྲོགས་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་པ་སྦོམ་པོར་སྦྱོར་བའི་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2298]
མ་བསྒོ་བར་སློང་བ་ཡང་ངོ་ཞེས་བྱ་བ༌[^1588]ནི་གྲངས་ཀྱི་སྐབས་སུ་དོར༌[^1589]བྱེད་པ་དེ་དང་འདྲ་བར་མ་བསྒོ་བར་སློང་བ་བལྟ་བར་བྱའོ། །

[Block 2299]
འདིར་ཡང་མ་བསྒོ་བར་སློང་བ་ནི་སྦྱོར་བའི་སྦྱོར་བ་ཉིད་དེ་ཉེས་བྱས་སོ། །

[Block 2300]
གྲུབ་པའི་ཚེ་ན་ནི་བརྐུས་པ་ཉིད་དོ། །

[Block 2301]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་རེ་ཞིག་ཁྱིམ་བདག་གི་ཁྱིམ་དུ་ཉེ་བར་མཆིས་པས། དེ་ཁྱིམ་བདག་དེའི་ཉེ་དུའི་ཐད་དུ་མཆིས་ནས་ཁྱིམ་བདག་ན་རེ་འདི་སྐད་ཅེས་དངོས་པོ་ཆེ་གེ་མོ་དང་མང་གེ་ཞིག་བྱིན་ཅིག་ཅེས་ཟེར་རོ་ཞེས་བགྱིས་ན་ལྟུང་བ་ཅིར་འགྱུར་ཉེས་པ་སྦོམ་པོར་སྦྱོར་བའི་ཉེས་བྱས་སུའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2302]
བརྙས་པ་དང་བསྐྱིས་པ་དང་གཏམས་པ་རྣམས་བསྙོན་པ༌[^1590]ནི་སྦྱོར་བའོ་ཞེས་བྱ་བ་ནི་བརྙས་པ་ལ་སོགས་པ་བསྙོན་པ་ནི་སྦྱོར་བ་སྟེ། མེད་པ་ནི་སྦྱོར་བ་མ་ཡིན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2303]
བརྣོགས་པ་ན་བརྐུས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བརྙས་པ་ལ་སོགས་པ་དེ་དག་གང་གི་ཚེ་བརྣོགས་ཤིང་མི་སྦྱིན་པར་ངེས་པ་དེའི་ཚེ་ན་བརྐུས་པ་ཡིན་ནོ། །

[Block 2304]
དེ་ལ་བརྙས་ནས་གཞན་ལ་འདིར་སོ་སོར་དེ་མ་ཐག་པར་གྱུར་པའི་བྱ་བ་ལ་བྱ་བ་མེད་པ་ཞེས་བྱ་བ་དེ༌[^1591]ལ་བརྙས་པ་ཉིད་ལ་སྦྱོར་བ་ཉིད་དོ། །

[Block 2305]
བརྣོགས་པ་ལས་སྔ་རོལ་དུ་གྱུར་པའི་བསྙོན་པ་གང་ཞིག་ཕྱི་མ་ནི་མ་ཡིན་ཞིང་དུས་མཉམ་པར་ཡང་མ་ཡིན་པར་འདིར་མངོན་པར་འདོད་པ་ཞེས་བྱ་བ་འདི་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 2306]
དེ་ལ་བརྙས་ནས་ཞུགས་པ་ནི་བརྙན་པོར་ཞུགས་པའོ། །

[Block 2307]
བསྐྱིས་ནས་ཞུགས་པ་ནི་སོ་སོར་སྦྱིན་པར་བགྱི་ཞེས་བྱ་བས་རྙེད་པ་ནི་བསྐྱིས་ནས་རྙེད་པའོ། །

[Block 2308]
རབ་ཏུ་བསྐྱིས་ནས་རྙེད་པ་ཞེས་བྱ་བ་དྲང་སྲོང་གི་ཚིག་གང་ཡིན་པ་དེ་ལ་འདི་ཉམས་པའོ། །

[Block 2309]
ཡོངས་སུ་སྦྱོར་བ་ཞེས་བྱ་བ་འདི་གཞན་ཞུ་བ་ལས་འབྱུང་བ་ཡིན་ཏེ། ནོར་ཟད་པར༌[^1592]ཡོངས་སུ་སྦྱར་བའི་དོན་དུ་སྟེ། དེ་ལས་ནོར་བཟུང་བ་མ་བཏང་བ༌[^1593]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2310]
ཡོངས་སུ་འགྲོ་བར་བྱེད་པ་ཞེས་བྱ་བ་འདི་གཞན་དག་གིས་བརྗོད་པ་སྟེ། འདི་དང་ཆེ་གེ་མོ་ལས་འགྲོ་བ་བསྒྲུབ་པའི་དོན་དུ་ཞེས་བྱ་བ་ནི་འདིའི་དོན་ཏོ། །

[Block 2311]
འདི་གཉིས་ཀ་ཡང་ཐ་མི་དད་པར་བསྐྱིས་པ་ཞིག༌[^1594]བྱ་བ་བརྣོགས་པ་ན་བརྐུས་པ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 2312]
འདིས་ནི་འདིར་བརྐུ་བའམ༌[^1595]འོན་ཏེ་མ་ཡིན་སྙམ་དུ་ཡིད་གཉིས་ཟ་བར་གྱུར་པ་དེའི་ཚེ་ན་གང་ཞིག་གནས་ལ་འཕོ་བ་དེར་ནི་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །

[Block 2313]
དངོས་པོ་ཡོངས་སུ་རྫོགས་པ་དེ་ལ་ཕམ་པ་མི་བསྐྱེད་ཅེས་བྱ་བ་འདི་ཐལ་བར་རིག་པར་བྱའོ། །

[Block 2314]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་རེ་ཞིག་བསྙོན་པར་བྱས་ནས་རྐུ་ན་ལྟུང་བ་ཅིར་འགྱུར། གཡར་ནས་བསྙོན་པར་བྱེད་ན་ཉེས་པ་སྦོམ་པོར་རོ། །

[Block 2315]
དེ་གཉིས་ལན་འགའ་མཐར་འགྱུར་བ་ཡང༌[^1596]ཡོད་དེ་གང་གི་ཚེ་བརྣོགས་པ་ནའོ། །
--- END BLOCKS ---
