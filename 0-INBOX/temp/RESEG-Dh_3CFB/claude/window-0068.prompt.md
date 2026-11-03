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
[Block 2381]
ཞེ་ན། འཁྲུལ་པ་ཙམ་ཕན་གདགས་པར་བྱ་བ་དང་། ཕན་འདོགས་པར་བྱེད་པ་མེད་པ་ཅན་ཡིན་པའི་ཕྱིར་དེའི་ངོ་བོ་ནི་ཤིན་ཏུ་ཐལ་བར་འགྱུར་ཏེ། འཁྲུལ་པས་གཞན་དག་ལ་ཡང་ཤེས་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 2382]
རྣམ་པ་ཐམས་ཅད་དུ་ཕན་འདོགས་པ་མེད་པ་ལ་ཡང་དེ་ལྟ་བུའི་ཤེས་པ་རིགས་པ་མ་ཡིན་ཏེ། ཐམས་ཅད་དག་ཕན་ཚུན་དེ་ལྟར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2383]
འཁྲུལ་པ་ཡང་འགའ་ཞིག་ལས་ཕན་བཏགས་པ་ཡོད་ཅིང་འགའ་ཞིག་ཉེ་བས་གཞན་དུ་འགྱུར་རོ། །

[Block 2384]
དེ་ཡང་བརྒྱུད་པས་ཕན་བཏགས་པ་མེད་ན་མི་འགྱུར་རོ། །

[Block 2385]
དེ་བས་ན་སྨྲ་བ་པོ་དང་ཉན་པ་པོ་གསལ་བའི་རྒྱུ་ཉིད་དུ་ཁྱད་པར་མེད་པའི་ཕྱིར། འབྲས་བུ་དང་ལྡན་པར་མཚུངས་པར་འགྱུར་རོ། །

[Block 2386]
གཞན་ཡང་།

[Block 2387 [VERSE]]
སྒྲ་ནི་རྣ་བའི་ཡུལ་ཡིན་ན། །
མངོན་པར་གསལ་མིན་སྒྲ་དག་ནི། །
བྱེད་རྣམས་དགོས་པའམ་ཡིད་བཟླས་པ། །

[Block 2388]
དོན་མེད་འགྱུར། རྣ་བའི་གཟུང་བའི་མཚན་ཉིད་ཅན་གྱི་སྒྲ་དེ་ལས་འདས་ན་ཐལ་ཆེས་པའི་ཕྱིར་རོ། །

[Block 2389]
དེ་ལྟར་ན་སྤྱི་ལ་ཡང་ཐལ་བར་འགྱུར་བ་མ་ཡིན་ནམ། སྒྲ་ཁོ་ན་ཞེས་ནི་མི་སྨྲའི། སྒྲ་ནི་གདོན་མི་ཟ་བར་དེའི་མཚན་ཉིད་ཅན༌[^1641]ཡིན་ཏེ། དེ་ལ་མཚན་ཉིད་གཞན་མེད་པའི་ཕྱིར་རོ། །

[Block 2390]
དེ་ལ་གལ་ཏེ་སྦྱོར་བ་པོའི་སྒྲའི་བདག་ཉིད་ཅན་གྱི་སྔགས་དག་གསལ་བའི་རྒྱུ་ཡིན་ན། མངོན་པར་གསལ་བ་མ་ཡིན་པའི་ཐོས་པའི་ཡུལ་ཅན་གྱི་སྦྱོར་བ་པོ་རྣམས་ཀྱི་བཟླས་པའམ། ཡིད་ཀྱི་བཟླས་པ་སྔགས་ཀྱི་འབྲས་བུ་དང་ལྡན་པ་མ་ཡིན་ཏེ། དེའི་ཚེ་རྣ་བས་དོན་ཅུང་ཟད་ཀྱང་ངེས་པར་བྱས་པ་མེད་དོ། །

[Block 2391]
སྒྲའི་བདག་ཉིད་ཅན་མ་ཡིན་པ་ཡང་སྔགས་མ་ཡིན་ནོ། །

[Block 2392 [VERSE]]
བརྒྱུད་པས་དེ་ལས་སྐྱེས་ཉིད་ཕྱིར། །
གལ་ཏེ་དེ་བློ་དེའི་གསལ་ཡིན། །

[Block 2393]
ཡིད་ཀྱིས་བསམས་སུ་ཟིན་ཀྱང་ཐོས་པ་མེད་པས༌[^1642]སྔགས་སྣང་བ་ཅན་གྱི་བློ་ནི༌[^1643]མེད་དོ། །

[Block 2394]
དེ་བས་ན་སྒྲ་ལས་བྱུང་བ་ཉིད་ཡིན་པའི་ཕྱིར། དེ་ཡང་སྒྲའི་གསལ་བ་ཉིད་ཡིན་ནོ། །

[Block 2395]
དེ་ལྟར་ན་ཐུག་པ་མེད་པར་འགྱུར་ཏེ། སྒྲའི་དོན་གྱི་རྣམ་པར་རྟོག་པ་དག་ཀྱང་བརྒྱུད་པས་བསྐྱེད་པ་ཡོད་པའི་ཕྱིར། དེ་ཡང་དེ་ལྟར་འགྱུར།

[Block 2396 [VERSE]]
གལ་ཏེ་དོན་ཅན་ཡིན་མི་འགྲུབ། །
རྟོག་པའི༌[^1644]རྗེས་སུ་འགྲོ་ཕྱིར་རོ། །

[Block 2397]
སྒྲ་ལས་བྱུང་བ་ཅན་གྱི་བློ་ཐམས་ཅད་ནི་དེའི་གསལ་བ་ཡིན་ནོ་ཞེས་མི་སྨྲའི། དེའི་ཡུལ་ཅན་གང་ཡིན་པ་དེ་དའི་གསལ་བ་ཡིན་ནོ། །

[Block 2398]
ཡིད་ཀྱི་རྣམ་པར་རྟོག་པ་ནི་དེའི་ཡུལ་ཅན་ཉིད་དུ་གྲུབ་པ་མ་ཡིན་ཏེ། རང་གི་མཚན་ཉིད་ལ་ནི་རྣམ་པར་རྟོག་པ་རྣམས་མི་འཇུག་གོ་ཞེས་སྟོན་པར་འགྱུར་རོ། །

[Block 2399]
དེ་དག་ནི་ཕྱི་རོལ་གྱི་དོན་ཉེ་བ༌[^1645]ལ་ལྟོས་པ་མེད་པ་ཅན་བདག་ཉིད་ཇི་ལྟ་བ་བཞིན་དུ་རང་གི་རྣམ་པར་རྟོག་པའི་བག་ཆགས་སད་པ་ལས་འགྱུར་ཏེ། ཕྱི་རོལ་འགགས་ཤིང་མ་འོངས་སུ་ཟིན་ཀྱང་ཡོད་པའི་ཕྱིར་རོ། །

[Block 2400]
གང་ཞིག་གང་ཡོད་པ་ཉིད་ཉེ་བ་ལ་ལྟོས་པ་མེད་པ་དེ་ནི་དེའི་རྒྱུ་མ་ཡིན་ཞིང་རྒྱུ་མ་ཡིན་པ་ཡང་ཇི་ལྟར་ན་ཡུལ༌[^1646]ཡིན། དེ་བས་ན་ཡིད་ཀྱི་རྣམ་པར་རྟོག་པ་སྒྲའི་གསལ་བ་མ་ཡིན་ན་གང་ལས་དེ་དང་ལྡན་པ་སྦྱོར་བ་པོར་འགྱུར། དེ་ལས་བྱུང་བ་དེའི་ཡུལ་ཅན་གྱི་བློ་དེའི་གསལ་བ་ཡིན་ཞིང་། དེའི་རྟེན་སྦྱོར་བ་པོ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ཡང་ཉན་པ་ལ་ཡང་ཐལ་བར་འགྱུར་རོ་ཞེས་བྱ་བས་བཤད་ཟིན་ཏོ། །

[Block 2401]
དེའི་ཤེས་པ་ལ་སྦྱོར་བ་ཡིན་ན་ཡང་སྐྱེས་བུ་ལ་སྒྲ་བྱེད་པ་ཡིན་ཏེ། དེའི་ཤེས་པ་བསྐྱེད་པའི་ཕྱིར། སྒྲ་ལ་སྐྱེས་བུས༌[^1647]མ་ཡིན་པས། དེའི་བདག་ཉིད་ཅན་ལ་ཕན་གདགས་པར་བྱར་མེད་པའི་ཕྱིར་རོ། །

[Block 2402]
དེ་ལྟར་ན་སྒྲ་རྣམས་ཀྱི་སྦྱོར་བ་པོ་ནི་སྐྱེས་བུས་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་སྙད་འདི་ནི་འཇིག་རྟེན་ལས་འདས་པ་ཡིན་ནོ། །

[Block 2403]
རྣམ་པ་ཐམས་ཅད་དུ་སྒྲའི་རང་བཞིན་ཅན་གྱི་སྔགས་དག་གི་སྦྱོར་བ་ལས་འབྲས་བུ་ཐོབ་པ་ཡིན་ན་ནི། ཡིད་ཀྱི་བཟླས་པ་དོན་མེད་པ་ཅན་ཡིན་ཏེ། རྣམ་པར་རྟོག་པ་ནི་སྒྲའི་ངོ་བོ་ལ་རེག་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2404 [VERSE]]
རང་དང་སྤྱི་ནི་རང་བཞིན་རྣམས། །
ངོ་བོ་གཅིག་ཏུ་བརྗོད་འདོད་པས། །
བརྡ་བྱེད་རྣམས་ཀྱིས་བརྗོད་པའི་ཕྱིར། །
འགལ་མེད་དངོས་ལ་མ་ཡིན་ནོ། །

[Block 2405]
བརྡ་བྱེད་པ་དག་ནི་རང་གི་མཚན་ཉིད་དབང་པོའི་ཡུལ་དང་། སྤྱིའི་མཚན་ཉིད་རྣམ་པར་རྟོག་པའི་སྣང་བའི་བརྡ་ཇི་ལྟ་བ༌[^1648]བཞིན་དུ་ཀུན་རྫོབ་ཏུ་གཅིག་ཏུ་བྱས་ན། [^1649]བརྡ་ཇི་ལྟ་བ་བཞིན་དུ་དོན་སྒྲུབ་པར་འགྱུར་རོ་ཞེས་བརྡ་གསལ་བར་བྱེད་པ་དེ་ལྟར་ན་ཡིད་ཀྱི་བཟླས་པ་ལ་སོགས་པ་ལ་སྐྱོན་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2406]
དངོས་པོའི་རང་བཞིན་ལས་འབྲས་བུ་ཐོབ་པ་ཡིན་ན་ཡང་དེའི་རང་བཞིན་ཅན་ལ་རིག་པ་མེད་པར་མི་འགྱུར་རོ། །

[Block 2407]
ཡི་གེ་དག་ལས་གཞན་པའི་གོ་རིམས་ཡོད་པ་མ་ཡིན་ནོ་ཞེས་བཤད་པ་གང་ཡིན་པ་དེ་ལ།

[Block 2408 [VERSE]]
གལ་ཏེ་གོ་རིམས་མེད་ན་ནི། །
རོ་དང་མཚོ་ཞེས་ཐོས་པ་ལ། །
འབྲས་བུ་ཐ་དད་ཞེས་མི་འགྱུར། །

[Block 2409]
རོ་དང་མཚོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་དག་ལ་ཡི་གེ་ཁྱད་པར་ནི་ཅུང་ཞིག་ཀྱང་མེད་ན། ཡི་གེ་ལས་ཐ་དད་པ་གཞན་མེད་ན་གང་ལས་འབྲས་བུ་ཐ་དད་འགྱུར། དེ་དག་གི་སྤོབས་པ་ཡང་ཐ་དད་པ་དང་། གོ་རིམས་ཀྱང་མི་འདྲ་བར་མཐོང་ན། རྒྱུ་ཐ་དད་པ་མེད་པར་འབྲས་བུ་ཐ་དད་པར་རིགས་པ་མ་ཡིན་ནོ། །

[Block 2410]
དེ་བས་ན་ཐ་དད་པ་དང་ལྡན་པ་ཡོད་པ་དེ་གང་ལས་རྟོགས་པ་ཐ་དད་པ་འདིར་འགྱུར། བདེན་ཏེ། དེ་ནི་སྐྱེས་བུའི་རྟེན་ཅན་ཡོད། །དེ་ལྟར།

[Block 2411 [VERSE]]
ཡི་གེ་ཀུན་སློང་ཤེས་པ་ལས། །
སྐྱེས་པ༌[^1650]ཤེས་པས་སྒྲ་གང་སྐྱེ། །
ཤེས་དེས་བསྐྱེད་པའི་ཤེས་པ་ཅན། །
དེ་ཡི་ཁྱད་པར་ཅན་དེ་ནི། །

[Block 2412 [VERSE]]
རྣ་བས་ངེས་པར་འགྱུར་བ་ཡིན། །
དེ་ཐོས་ཐལ་བ་འཇུག་ཅན་ཏེ། །
དེ་དྲན་པ་ལས་ལྟོས་ན་ནི། །
ཕྱིས་ནི་བདག་ཉིད་ལ་དྲན་བྱེད། །

[Block 2413 [VERSE]]
དེ་ལྟར་དེ་རྒྱུ༌[^1651]འཛིན་སེམས་ཀྱི། །
ཡིག་རྣམས་རྒྱུ་དང་འབྲས་བུ་ཉིད། །
དེ་དག་སྐྱེས་བུས་བྱས་པ་ཉིད། །
གོ་རིམས་དག་ནི་ཡིན་ཞེས་བརྗོད། །

[Block 2414]
སེམས་ཀྱིས་ཀུན་ནས་བསླང་བ༌[^1652]ཅན་གྱི་ངག་གི་རྣམ་པར༌[^1653]རིག་བྱེད་ཡི་གེ་དང་ཚིག་དང་ངག་ཅེས་བྱ་བ། དེ་ལ་ཡི་གེས་ཀུན་ནས་སློང་བར་བྱེད་པའི་སེམས་དེ་མ་ཐག་པའི་རྐྱེན་གྱིས་ཡི་གེ་ཨ་ཀུན་ནས་སློང་བའི་སེམས་བསྐྱེད་པར་འགྱུར་རོ། །

[Block 2415]
དེ་བཞིན་དུ་ཡི་གེ་ར་དང་ཚེག་དྲག་གིས་ཀུན་ནས་སློང་བར་བྱེད་པ་སྔ་མ་སྔ་མའི་རྐྱེན་ཅན་ནོ། །

[Block 2416]
དེ་བས་ན་རྒྱུ་གཞན་དང་ལྡན་པའི་ཡི་གེ་དེ་དག་ནི་རང་གི་རྒྱུའི་གོ་རིམས་བཞིན་དུ་སྐྱེ་བ་ཅན་ཡིན་ནོ། །

[Block 2417]
ཐོས་པའི་དུས་སུ་ཡང་གང་གི་ཚེ་ངལ་བར་འཇུག་པ་ཅན་ཡི་གེ་སྔ་མ་ཤེས་པའི་ལྷན་ཅིག་བྱེད་པའི་རྐྱེན་ལ་ལྟོས་པ་ཅན་དག་གིས་རང་གི་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་དེའི་ཚེ། སྔ་མ་དྲན་པ༌[^1654]ལྟོས་པ་ཉིད་ཀྱིས་དྲན་པ་སྐྱེད་པར་བྱེད་དོ། །

[Block 2418]
རྒྱུ་དང་འབྲས་བུ་ཐ་དད་པ་ཅན་གྱི་རྐྱེན་ལས་བྱུང་བའི་ཆོས་ཅན་དང་། ཐ་དད་པར་བསྐྱེད་པའི་ཆོས་ཅན་དེ་དང་དེ་ནི་ཡི་གེ་རྣམས་ཀྱི་རང་བཞིན་ཡིན་ཏེ། སྐྱེས་བུས་འདུས་བྱས་པའི་ཁྱད་པར་གྱིས་ཐ་དད་པ་ནི་གོ་རིམས་ཞེས་བརྗོད་དོ། །

[Block 2419 [VERSE]]
དེ༌[^1655]ཕྱིར་ཡི་གེའི་ངོ་བོ་དེ། །
ཚིག་དང་ཚིག་ལ་གཞན་ཉིད་དེ། །
བྱེད་པའི་འདུ༌[^1656]བྱེད་ལས་ཐ་དད། །
འབྲས་བུའི་ཁྱད་པར༌[^1657]ལྷན་ཅིག་བྱེད། །

[Block 2420]
དེ་བས་ན་ཚིག་དག་ལ་ཡི་གེ་རྣམས་ཀྱི་རང་བཞིན་གཅིག་ཉིད་མ་ཡིན་ཏེ། བྱེད་པ་པོའི་སེམས་ཀྱི༌[^1658]འདུས་བྱས་པའི་ཁྱད་པར་གྱིས་ཐ་དད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
