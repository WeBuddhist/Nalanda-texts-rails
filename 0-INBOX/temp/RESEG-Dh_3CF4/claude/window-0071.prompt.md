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
[Block 2486]
[^1583]སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་མཆོད་སྦྱིན་གྱི་སྐྱེས་པའི་རབས་ཏེ་བཅུ་པའོ།། །།

[Block 2487 [HEADING]]
## སྐྱེས་པའི་རབས་བཅུ་པོ་འདི་དག་གི་གོ་རིམས། ^11-0

[Block 2488]
བདག་གིས་ནི་འདི་ཙམ་ཞིག་གོ་བར་ཟད་དེ། ལྷག་མ་ནི་གཞན་དག་ཏུ་བལྟ་བར་བྱའོ། །

[Block 2489]
སྡོམ་ལ།

[Block 2490 [VERSE]]
སྟག་མོ་ཤི་པི་ཀོ་སལ་བདག །
ཚོང་དཔོན་གཉིས་དང་རི་བོང་དང་། །
ཨ་གསྟ༌[^1584]དང་ཤ་བྱིན་དང་། །
ཐམས་ཅད་སྒྲོལ་དང་མཆོད་སྦྱིན་བྱེད། །

[Block 2491]
སྐྱེས་པའི་རབས་ཀྱི་རྒྱུད་ཀྱི་གོ་རིམས་རྣམ་པར་གཞག་པའི༌[^1585]རྒྱུ་ནི་རིམ་པ་གང་གིས་བཀོད་པའི་སྐྱེས་པའི་རབས་བཅུ་པོ་འདི་དག་གི་གོ་རིམས་ལྟར་ནི་བདག་གིས་མ༌[^1586]མཐོང་གི། །འདི་ནི་སློབ་དཔོན་དཔའ་བོས་བཀོད་པའི་རིམ་པ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། དེའི་གོ་རིམས་ཀྱི་བྱེད་པའི་སྦྱོར་བས་སོ། །

[Block 2492]
བདག་གིས་ནི༌[^1587]གོ་རིམས་ཀྱི་ཚུལ་འདི་ལྟར་རིགས་པར་མཐོང་སྟེ།

[Block 2493 [VERSE]]
སྟག་མོ་རི་བོང་ཤི་པི་དང་། །
ཤ༌[^1588]སྦྱིན་ཚོང་དཔོན་ཀོ་ས་ལ་བདག །
ཐམས་ཅད་སྒྲོལ་དང་ཟིལ་མི་ནོན། །

[Block 2494]
ཨ་གསྟ༌[^1589]དང་མཆོད་སྦྱིན་བྱེད། །སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དབང་དུ་བྱས་ནས་བཅུ་ཚན་དང་པོ་འདི་ཡིན་ཏེ། སྦྱིན་པ་རྣམ་པ་གསུམ་ལ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པས༌[^1590]བརྗོད་དེ། ཟང་ཟིང་གི་སྦྱིན་པ་དང་། ཆོས་ཀྱི་སྦྱིན་པ་དང་། མི་འཇིགས་པའི་སྦྱིན་པའོ། །

[Block 2495]
དེ་ལ་ཟང་ཟིང་གི་སྦྱིན་པའི་དབང་དུ་བྱས་ནས་སྐྱེས་པའི་རབས་བརྒྱད་ཡིན་ནོ། །

[Block 2496]
གཞན་གཉིས་ཀྱིས་ནི་ཆོས་ཀྱི་སྦྱིན་པ་དང་། མི་འཇིགས་པའི་སྦྱིན་པ༌[^1591]བསྟན་ཏོ། །

[Block 2497]
ཟང་ཟིང་གི་སྦྱིན་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། ནང་གི་སྦྱིན་པ་དང་ཕྱིའི་སྦྱིན་པའོ། །

[Block 2498]
ནང་གི་སྦྱིན་པ་ལས་བརྩམས་ནས་དང་པོ་བཞིའོ། །

[Block 2499]
ཕྱི་རོལ་གྱི་སྦྱིན་པ་ལས་བརྩམས་ནས་འོག་མ་བཞིའོ། །

[Block 2500]
དེ་ལ་ནང་གི་སྦྱིན་པའི་དངོས་པོ་ཡང་གཉིས་ཏེ། ལུས་དང་སྲོག་གོ། །

[Block 2501]
སྦྱིན་པ་དེ་ཡང་གཉིས་ཀྱི་དོན་དུ་ཡིན་ཏེ། ཡོངས་སུ་ལོངས་སྤྱོད་པ་དང་ཡོངས་སུ་བསྐྱབ་པའི༌[^1592]ཕྱིར་རོ། །

[Block 2502]
དང་པོ་སྟག་མོའི་སྐྱེས་པའི་རབས་ལ་ནི་བཞི་པོ་འདི་དག་དང་ལྡན་པ་ཡིན་ཏེ། དེ་བས་ན་སྐྱེས་པའི་རབས་དེ་ཐོག་མར་བསྟན་ཏོ། །

[Block 2503]
སྲོག་སྦྱིན་པ་ཡང་བདག་ཉིད་འཆི་བ་མ་གཏོགས་པར་དེའི་ལོངས་སྤྱོད་པ་དང་ལུས་ཀྱི་སྦྱིན་པ་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 2504]
ལུས་ཀྱི་སྦྱིན་པ་ཡོད་པ་ཉིད་ཀྱིས་རང་གི་ལུས་སྦྱིན་པ་དེས་སྟག་མོ་ལོངས་སྤྱོད་པ་ཡོད་པར་རབ་ཏུ་རིག་པས༌[^1593]སོ། །

[Block 2505]
ཡོངས་སུ་སྐྱོབ་པ༌[^1594]ཡང་ཡོད་དེ་དེ་བས་ན་སྐྱེས་པའི་རབས་དེ་ཉིད་དུ་བཤད་པ་སྟེ། དེ་བས་ལུས་ཀྱིས་བསྲུང་བར༌[^1595]བྱ་བ་ནི།

[Block 2506 [VERSE]]
གཡང་སར་ལྟུང་ལ་ཐུག་པའི་སྲོག་ཡོད་པས། །
ཕྲུ་གུ་གསད༌[^1596]ལས་གཅན་མོ་བསྲུང་བ་དང་། །
གཅན་མོ་ལས་ཀྱང་དེ་ཡི་ཕྲུ་གུ་བསྲུང་། །

[Block 2507]
ཞེས་པ༌[^1597]ཡིན་ཏེ། དེ་བས་ལུས་ཀྱིས་བསྲུང་བར་བྱ་བ་ནི་ཞེས་བྱ་བ་འདིས་ནི་ལུས་ཀྱི་སྦྱིན་པ་ཡིན་ནོ། །

[Block 2508]
གཡང་སར་ལྷུང་ལ་ཐུག་པའི་སྲོག་ཡོད་པས། །ཞེས་བྱ་བ་འདིས་ནི་སྲོག་གི་སྦྱིན་པ་ཡིན་ནོ། །

[Block 2509]
ཕྲུ་གུ་གསད་ལས་གཅན་མོ་བསྲུང་བ་དང་། །ཞེས་བྱ་བ་འདིས་ནི་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་སྦྱིན་པ་ཡིན་ནོ། །

[Block 2510]
གཅན་མོ་ལས་ཀྱང་དེ་ཡི་ཕྲུ་གུ་བསྲུང་། །ཞེས་བྱ་བ་འདིས་ནི་ཡོངས་སུ་བསྐྱབ་པའི་སྦྱིན་པ་ཡིན་ཏེ། ནང་གི་རྣམ་པ་འདི་བཞི་ཡོད་པས་སྐྱེས་པའི་རབས་འདི་དང་པོར་སྨོས་པ་ཡིན་ནོ། །

[Block 2511]
གཉིས་པ་རི་བོང་གི་སྐྱེས་པའི་རབས་ཀྱིས་ནི་ནང་གི་ལུས་དང་སྲོག་གཉིས་ཀྱི་སྦྱིན་པས་ཡོངས་སུ་ལོངས་སྤྱོད་པ་ཡིན་ཏེ་ཡོངས་སུ་སྐྱོབ་པ་ནི་མ་ཡིན་ནོ། །

[Block 2512]
གང་།

[Block 2513 [VERSE]]
བདག་གི་ལུས་ནི་མེ་ལ་བསྲེགས་པ་འདི། །
སྣོམ༌[^1598]ལ་དེ་རིང་དཀའ་ཐུབ་ནགས་ན་བཞུགས། །

[Block 2514]
ཞེས་བྱ་བའི་ཚིག༌[^1599]གིས་ནང་གི་ལུས་ཀྱི་སྦྱིན་པའོ། །

[Block 2515]
བདག་ལ་ལུས་ལས་ལྷག་པའི་ནོར་ཡང་མེད། །ཅེས་བྱ་བའི་ཚིག་གིས་ནི་སྲོག་གི༌[^1600]སྦྱིན་པའོ། །

[Block 2516]
བདག་ཅག་ལྟ་བུས་གཞན་དག་གི །

[Block 2517 [VERSE]]
སྲོག་ཀྱང་གཅོད་པར་མི་བྱེད་ན། །
དེ་ལྟར་རབ་ཏུ་བྱམས་བརྟན་པ། །
ཁྱོད་ལྟ་བུ་ལ་སྨོས་ཅི་དགོས། །

[Block 2518]
ཞེས་བྱ་བའི་ཚིག་དེ་ཐོས་ནས་མེའི་ནང་དུ་བདག་ཉིད་ཞུགས་སོ། །

[Block 2519]
དེས་ན་སྲོག་གི་སྦྱིན་པ་དེས་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་སྦྱིན་པ་དེ་ཉིད་དུ་བཤད་པ་ཡིན་ནོ། །

[Block 2520]
བདག་གི་ལུས་ནི་མེ་ལ་བསྲེགས་པ་འདི། །སྣོམས་ལ་དེ་རིང་དཀའ་ཐུབ་ནགས་སུ་བཞུགས།[^1601] །ཞེས་བྱ་བའི༌[^1602]ཚིག་གིས་ནི་དེར་ཡོངས་སུ་བསྐྱབ་པ་ནི་མེད་དེ། བདག་ཉིད་འཆི་བ་དེ་ལས་གཞན་མ་རྙེད་པས་སོ། །

[Block 2521]
སྲམ་དང་ཅེ་སྤྱང༌[^1603]དང་། སྤྲེའུ་རྣམས་ཀྱིས་ནི་ཟས་རྙེད་པ་ཡིན་ཏེ། དེ་བས་ན་དེ་དག་གིས་དང་པོར་ཟས་བྱིན་པ་ཡིན་ནོ། །

[Block 2522]
[^1604]ད་ནི་ཤི་པི་པ་དང་། བྱམས་པའི་སྟོབས་བསྐྱེད་པའི་སྐྱེས་པའི་རབས་གཉིས་ཀྱིས་ནི་ལུས་ཀྱི་སྦྱིན་པ་ཉིད་བསྟན་པ་ཡིན་ཏེ་སྲོག་ནི་མ་ཡིན་ནོ། །

[Block 2523]
ཡོངས་སུ་ལོངས་སྤྱོད་པའི་སྦྱིན་པ་ཉིད་དེ། ཡོངས་སུ་བསྐྱབ་པའི་སྦྱིན་པ་ནི་མ་ཡིན་ནོ། །

[Block 2524]
ལུས་ཀྱི་སྦྱིན་པ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། དབང་པོའི་དབྱེ་བས་སྦྱིན་པ་དང་། དབང་པོའི་དབྱེ་བ་མེད་པས་སྦྱིན་པའོ། །

[Block 2525]
དེ་ལ་དབང་པོའི་དབྱེ་བས་སྦྱིན་པའི་དབང་དུ་བྱས་ནས་ཤི་བི༌[^1605]པའི་སྐྱེས་པའི་རབས་ལས༌[^1606]མིག་གི་སྦྱིན་པ་ཡིན་ནོ། །ཇི་ལྟར་དེ་ཡོངས་སུ་ལོངས་སྤྱོད་པར་འགྱུར་ཞེ་ན། དེའི་མིག་ཡོངས་སུ་ལོངས་སྤྱོད་པ་ནི་ཡུལ་ལ་དམིགས་པ་དེས་ཡུལ་ལ་དམིགས་ཤིང་ཡོངས་སུ་ལོངས་སྤྱོད་པ་ཡིན་ཏེ། དེ་དེ་ཉིད་དུ་བསྟན་པ།
--- END BLOCKS ---
