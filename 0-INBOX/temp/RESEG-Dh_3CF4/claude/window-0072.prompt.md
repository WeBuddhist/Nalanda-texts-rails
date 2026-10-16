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

[Block 2526 [VERSE]]
པདྨའི་སྤྱན་མངའ་སྤྱན་ནི་གཅིག་པུས་ཀྱང་། །
འཇིག་རྟེན་བདག་པོ་འཇིག་རྟེན་བགྱི་བ་འགྲུབ། །

[Block 2527]
ཅེས་བྱ་བ་དང་། ཅི་ནས་ཀྱང་མིག་དེ་དེའི༌[^1607]མིག་ཏུ་གནས་པར་གྱུར་པ་དང་། དེ་ནས་མིག་ཡ་གཅིག་ཕྱེ་སྟེ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2528]
དབང་པོས་ནི་ལོངས་སྤྱོད་ཅིང་ཟ་བར་བྱེད་པ་མ་ཡིན་གྱི། དབང་པོ་དེ་ལ་བརྟེན་ནས་ཡོངས་སུ་ལོངས་སྤྱོད་པ་ཡིན་ཏེ། གཞན་དུ་ན་ལོངས་སྤྱོད་པར་མི་ནུས་ཏེ་དེས་ན་ཡུལ་དམིགས་པ་དེ་ཉིད་ཀྱིས་ལོངས་སྤྱོད་པའོ། །

[Block 2529]
བྱམས་པའི་སྟོབས་བསྐྱེད་པ་ལ་ཡང་ནང་གི་སྦྱིན་པ་དབང་པོའི་དབྱེ་བ་ཤ་དང་ཁྲག་གི་སྦྱིན་པ་ཡིན་ཏེ། སྲོག་གི་སྦྱིན་པ་ནི་མ་ཡིན་པར་དེ་ཉིད་ལས་བསྟན་པ་སྟེ།[^1608] ལྷ་དང་མིའི་སྨན་གྱི་ཁྱད་པར་རྨ་སར་པ་སོས༌[^1609]པར་བྱེད་ནུས་པ་རྣམས་ཀྱིས་དེའི་ལུས་སྔོན་བཞིན་དུ་སྡུག་བསྔལ་མེད་པར་བྱས་ཞེས་པའི་ཚིག་གིས་སོ། །

[Block 2530]
ཡོངས་སུ་ལོངས་སྤྱོད་པ་ཉིད་དུ་བཤད་པའི་ཕྱིར། ལྷ་ཉིད་ཀྱི་སྐུ་འོ་བརྒྱལ་བར༌[^1610]མཛད་པ་བཏང་དུ་གསོལ། བདག་ཅག་ཀྱང་ཚིམ་པར་བགྱིས་ལགས་ཀྱིས་ཞེས་བྱ་བས༌[^1611]སོ། །

[Block 2531]
སྐྱོབ་པ༌[^1612]མ་ཡིན་ཏེ། གང་དེ་ལས་གཞན་ཡོངས་སུ་བསྐྱབ་པར༌[^1613]བྱ་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2532]
དེ་ལྟར་རེ་ཞིག་ནང་གི་སྦྱིན་པ་རྣམ་པ་བཞིའི་དབྱེ་བ་ཡིན་ཏེ། དེ་བས་ན་དེ་ལྟར་སྐྱེས་པའི་རབས་རྒྱུ༌[^1614]རྣམ་པ་བཞི་བཀོད་པ་ཡིན་ནོ། །

[Block 2533]
བཞི་པོ་དེའི་ནང་དུ་དེའི་རང་བཞིན་གཞན་ཡང་ཆུད་པ་ཡིན་ཏེ། དེའི་རིགས་དེས་སྐྱེས་པའི་རབས་གཞན་ཡང་རབ་ཏུ་འགྲུབ་བོ། །

[Block 2534]
དེ་གོ་བར་འདོད་པ་རྣམས་ལ་མཐའ་དག་གི་ཐབས་བསྟན་པ་ཡིན་ནོ། །

[Block 2535]
ད་ནི་ཕྱི་རོལ་གྱི་དངོས་པོའི་སྦྱིན་པའི་དབང་དུ་བྱས་ནས་སྐྱེས་པའི་རབས་ཅིག་ཤོས་བཞི་བསྟན་པ་ཡིན་ཏེ། ཇི་ལྟར་ཕྱི་རོལ་གྱི་སྦྱིན་པ་ཡིན་ཞེ་ན། རྣམ་པ་གསུམ་དུ་བརྩམས་པ་ཡིན་ཏེ། སྦྱིན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་དང་། ལེན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་དང་། སྦྱིན་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 2536]
ཕུན་སུམ་ཚོགས་པ་འདི་གསུམ་གྱི་དབང་དུ་བྱས་ན་ཚོང་དཔོན་གྱི་སྐྱེས་པའི་རབས་སུ་ལེན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་ནི་དེ་ཉིད་དུ་རང་སངས་རྒྱས་ཉོན་མོངས་པའི་བུད་ཤིང་ཐམས་ཅད་བསྲེགས་པ་དེའི་བསོད་ནམས་ཀྱི་ཚོགས་རྣམ་པར་འཕེལ་བར་འདོད་པ་ཞིག་དེའི་ཁྱིམ་དུ་བསོད་སྙོམས་ཀྱི་ཕྱིར་འོངས་སོ་ཞེས་པས་སོ། །

[Block 2537]
སྦྱིན་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་ཡང་དེ་ཉིད་དུ་བསྟན་ཏེ། དེས་དེའི་ལྟར༌[^1615]མཉན་ཏེ་དེ་བཞིན་དུ་བགྱིའོ་ཞེས་སྨྲས་ནས་བཟའ་བ་དང་བཅའ་བ་བཟང་པོ་ཁྱེར་ཏེ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2538]
སྦྱིན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་ཡང་དེ་ཉིད་དུ་བསྟན་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་དག༌[^1616]གི་སྐལ་པ་དང་བསོད་ནམས་ཀྱི་མཐུ་ལ་བརྟེན་ནས་སྦྱིན་པ་ལ་ཉེས་དམིགས་མེད་པར་ཡང་ཤེས་ཏེ། བུ་སྨད་དང་གཡོག་འཁོར་འགྲོར་མི་སྟེར་བར་འཐེན་པ་རྣམས་བོར་ནས་བློ་ལ་ཚམ་ཚོམ་མེད་ཅིང་སྦྱིན་པ་བྱེད་པར་འདོད་པ་སྐྱེས་ཏེ་དམྱལ་བའི་ནང་ནས༌[^1617]སོང་ངོ་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2539]
ད་ནི་ཀོ་ས་ལའི་བདག་པོའི་སྐྱེས་པའི་རབས་ལ་ནི་ཕུན་སུམ་ཚོགས་པ་གཉིས་ཡོད་དེ་སྦྱིན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་དང་། ལེན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་དང༌[^1618]ཀོ་ས་ལའི་བདག་པོ་ལ་ནི་སྦྱིན་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་མེད་དོ། །

[Block 2540]
དེ་ལ་སྦྱིན་པ་པོའི་ཕུན་སུམ་ཚོགས་པ་ཡང་དེ་ཉིད་དུ་བསྟན་ཏེ། ཚུལ་དང་ལྡན་ཡང་ནོར་ཙམ་གྱིས་ནི་མཐོ་བ་ལ། །ལས་ཀྱིས༌[^1619]མགུ་བར་བྱས་ནས་སྨན༌[^1620]ཚིས་འཚོ་བའི་ཞེས་བྱ་བ་དང་། གཞན་ཡང་དང༌[^1621]ཞིང་འཇམ་པའི་ཡིད་ཀྱིས་དེ་ལ་ཕྱག་འཚལ་ནས། །ཞེས་པའི་ཚིག་གིས་སོ། །

[Block 2541]
ལེན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་ཡང་དེ་ཉིད་དུ་བཤད་དེ།

[Block 2542 [VERSE]]
དགེ་སྦྱོང་བཞི་ཞིག་བསོད་སྙོམས་ཕྱིར་ནི་ལྷགས་པ་མཐོང་། །
དབང་པོ་དུལ་ཞིང་དགེ་སྦྱོང་དཔལ་གྱི་རྗེས༌[^1622]འབྲང་བ། །

[Block 2543]
ཞེས་བྱ་བ་ཡིན་ཏེ། བཞི་སྨྲོས་པ་ནི་སྦྱིན་པའི་གནས་དགེ་འདུན་དུ་བསྟན་པའི་ཕྱིར་ཏེ། དེ་བས་ན་ལེན་པ་པོ་ཕུན་སུམ་ཚོགས་པར་བསྟན་ཏོ། །

[Block 2544]
སྦྱིན་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་ནི་མེད་དེ། དེ་ཡང་དེ་ཉིད་དུ་བསྟན་པ། ཟན་དྲོན་ཁེངས་པ་རྩུབ་པོ་ལེན་ཚ༌[^1623]མེད་པའི་འབྲས་བུ་འབྱོར་པ་ཆེན་པོ་འདི་ལྟར་འགྱུར་ལ་ལྟོས།[^1624] །ཞེས་བྱ་བ་དང་། སྐྱེས་པའི་རབས་དེ་ཉིད་དུ་གཅིག་གི་བར་དུ་བྱས་པ་སྟེ། གང་གི་ཚེ་ལེན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་ཉི་ཚེ༌[^1625]བསྟན་པ་ཡིན་ཏེ། ཐུབ་པ་ཟག་པ་ཟད་ལ་གུས་པར་ཕུལ་བ་ཡིས། །ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2545]
སྦྱིན་པར་བྱ་བའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་ནི་མེད་དེ། ཟས་ལས་བགོ་སྐལ་བགོས་པའོ། །

[Block 2546]
སྦྱིན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་ཡང་མེད་དེ། བྲན་མོ་བགྱིད་པའི་ཚེ་ན་ཞེས་པའི་ཚིག་གིས་སོ། །

[Block 2547]
གུས་པར་ཕུལ་བ་ནི་དུས་ཚོད་དེ་ཙམ་ན་གུས་པ་ཡོད་པའོ། །

[Block 2548]
དེའི་ཕྱིར་འབྲས་བུ་ཆུང་བ་སྟེ་བུད་མེད་དུ་གྱུར་པའོ། །

[Block 2549]
ད་ནི་སྦྱིན་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་དང་། སྦྱིན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་ནི་ཐམས་ཅད་སྒྲོལ་གྱི་སྐྱེས་པའི་རབས་ཡིན་ཏེ། སྦྱིན་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་ནི་ཕྱི་རོལ་གྱི་དངོས་པོ་སེམས་ཅན་དང་སེམས་ཅན་མ་ཡིན་པའི་གྲངས་སུ་འགྲོ་བའི་རྣམ་པ་ཐམས་ཅད་དེ། ཕྱི་རོལ་གྱི་སྦྱིན་པའི་དངོས་པོའོ། །

[Block 2550]
སེམས་ཅན་གྱི་གྲངས་སུ་འགྲོ་བའི་ཕྱི་རོལ་གྱི་སྦྱིན་པ་ནི་གླང་པོ་རིན་པོ་ཆེ་དང་། རྟ་ཆས་དང་བཅས་པ་ལ་སོགས་པ་མཐའ་དག་སྦྱིན་པའོ། །

[Block 2551]
སེམས་ཅན་མ་ཡིན་པ་ནི་བུ༌[^1626]སྨད་དང་བཅས་པ་ཡིན་ཡང་དེ་ལ་མ་ལྟོས་པར༌[^1627]ཤིང་རྟ་སྦྱིན་པའོ། །

[Block 2552]
བུ་སྦྱིན་པ་དང་། ཆུང་མ་སྦྱིན་པ་ནི་བདག་ཉིད་གྱི་ཕྱི་རོལ་གྱི་སྦྱིན་པའི་དངོས་པོ་ཁྱད་པར་དུ་གྱུར་པའོ། །

[Block 2553]
སྦྱིན་པ་པོ་ཕུན་སུམ་ཚོགས་པའི་ཁྱད་པར་དུ་གྱུར་པ་དེ་ཉིད་དུ་བསྟན་ཏེ།

[Block 2554 [VERSE]]
འཇིག་རྟེན་དོན་དུ་ང་ཡི་ལུས་འཛིན་ན། །
ཕྱི་རོལ་ནོར་ལྟ་སྨོས་ཀྱང་ཅི་ཞིག་དགོས། །

[Block 2555 [VERSE]]
ཤི་བི་པ་རྣམས་ཐམས་ཅད་ཀྱིས། །
ང་ནི་བསད་དམ་སྤྱུགས༌[^1628]ཀྱང་རུང་། །
མི་སྦྱིན་པར་ནི་ང་མི་བྱེད། །
དཀའ་ཐུབ་ཚལ་དུ་འགྲོར་ཟད་མོད། །

[Block 2556]
ཅེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2557]
གཞན་ཡང་།

[Block 2558 [VERSE]]
སྦྱིན་ལ་དགའ་བ་གོམས་བྱས་ཤིང་། །
སླར་བཟློག་པ༌[^1629]ནི་མ་བསླབས་པས། །
རབ་ཏུ་སྡུག་པའི་བུ༌[^1630]གཉིས་ཀྱང་། །

[Block 2559]
ཚམ་ཚོམ་མེད་པར་སྦྱིན་ཞེས་སྨྲས།[^1631] །ཞེས་བྱ་བ་དང་། གཞན་ཡང་ཕྱི་རོལ་གྱི་དངོས་པོ་སྦྱིན་པ་པོ་ཕུན་སུམ་ཚོགས་པའི་དབང་དུ་བྱས་ནས་བཤད་པ་དེ་ཐམས་ཅད་ཀྱང་སྦྱར་བར་བྱའོ། །

[Block 2560]
ད་ནི་ཚོང་དཔོན་ཟིལ་གྱིས་མནོན་པའི་སྐྱེས་པའི་རབས་ཀྱིས་སྦྱིན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་དེའི་དབང་དུ་བྱས་ནས་བསྟན་པ་ཡིན་ནོ། །
--- END BLOCKS ---
