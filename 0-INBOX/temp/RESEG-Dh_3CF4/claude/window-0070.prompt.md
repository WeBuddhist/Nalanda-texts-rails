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
[Block 2451]
འཐབ་པ་དང་རྩོད་པ་ཞེས་བྱ་བ་འདིས་ནི་མི་དགེ་བའི་ལམ་དག་གིས་བསྡུས་པ་ལས་ལྡོག་པ་བསྟན་ཏོ། །

[Block 2452]
བླ་མའི་ངག་ཉན་ཞིང་རྗེས་སུ་མཐུན་པར་ནི་བྱེད་ཅེས་བྱ་བ་འདིས་ནི་གང་ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པ་བླངས་ཤིང་སྤོང་བ་ལས་སྐྱེས་པའི་དབང་དུ་བྱས་པ་སྟེ། བླ་མས་ནི་མི་དགེ་བ་ལས་ལྡོག་པ་དང་། དགེ་བ༌[^1567]ལ་འཇུག་པ་བསྟན་ཏོ། །

[Block 2453]
བགོ་བཤའ་བྱེད་པ་ལ་ནི། བག་ཚ་བ་མེད་ཅེས་བྱ་བ་ནི་ནང་གི༌[^1568]ཕ་མ་ལ་སོགས་བའོ། །

[Block 2454]
གློ་བུར་དུ་འོངས་པ་ལ་ནི་དགའ་ཞེས་བྱ་བ་ནི་མགྲོན་ལ་མཉེས༌[^1569]གཤིན་པའོ། །

[Block 2455]
དུལ་བ་དང་གུས་པར་བྱ་བ་ལ་ནི་འབད་པར་གྱུར་ཞེས་བྱ་བ་ལ། དུལ་བ་ནི་ཉོན་མོངས་པ་ཉེ་བར་ཞི་བའོ། །

[Block 2456]
གུས་པར་བྱ་བ་ནི་ལུས་ངག་གི་ཡང་དག་པར་འཇུག་པའོ། །

[Block 2457]
ཚུལ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་བསྡུས་པའི་དོན་ནི་ཐ་མ་དང་། བར་མ་དང་། དམ་པའི་ཚུལ་ཁྲིམས་ལ་འཇུག་པའི་རྒྱུ་བསྟན་ཏེ། ཤི་བས་འཇིགས་ཤིང་ཞེས་བྱ་བ་ལ། གང་ཐ་མ་ནི་ཕྱུགས་ལྟར་བསད་པས་འཇིགས་པ་སྟེ། གང་ཐ་མ་ནི་དེས་ཚུལ་ཁྲིམས་སྲུང་བར་བྱེད་དོ། །

[Block 2458]
འཇིག་རྟེན་ཕ་རོལ་སེམས་ཞེས་བྱ་བ་ནི་ངན་འགྲོས་འཇིགས་པ་དང་། བདེ་འགྲོར་འགྲོ་བ་ལ་སྲེད་པས་སོ། །

[Block 2459]
རིགས་ཀྱིས་ང་རྒྱལ་ཞེས་བྱ་བ་ནི་བདག་གི་རིགས་མཐོ་བས་བསྙེམས་པའི༌[^1570]ཚུལ་ལོ། །

[Block 2460]
གྲགས་པ་བསྲུང་བ༌[^1571]དང་ཞེས་བྱ་བ་ནི་ཁྲེལ་ཡོད་པས་སྐྱོད་པ༌[^1572]སྟེ། གསུམ་ལས་བར་མའི་ཚུལ་ཁྲིམས་ལ་འཇུག་པའི་རྒྱུ་བསྟན་པའོ། །

[Block 2461]
བསམ་པ་དག་ཅིང་ཞེས་བྱ་བ་ནི་སྔོན་དགེ་བ་རྒྱུད་ལ་བསྟན་པ༌[^1573]དེས་སོ། །

[Block 2462]
ངོ་མཚར༌[^1574]ཤེས་པ་ཡིས་ཞེས་བྱ་བ་ནི་བདག་གི་དབང་དུ་བྱས་ནས་ཁ་ན་མ་ཐོ་བ་ལ་འཇིགས་པར་ལྟ་བའོ། །

[Block 2463]
དེ་གཉིས་ཀྱིས་ནི་དམ་པ་དག་ཚུལ་ཁྲིམས་ཀྱི་རྗེས་སུ་འཇུག་པ་བསྟན་ཏོ། །

[Block 2464]
ཚུལ་ཁྲིམས་དེའི་སེམས་ཀྱི་རྗེས་སུ་འཇུག་པའི་རྒྱུ་བསྟན་པའི་ཕྱིར། ཇི་ལྟ་ཇི་ལྟར་སྐྱེ་བོ་ཆོས་འབད་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ནོ། །

[Block 2465]
ཇི་ལྟར་ཆོས་ལ་འབད་པ་ནི་བསྟན་མ་ཐག་པ་ཉིད་ཀྱི་རྒྱུས་སོ། །

[Block 2466]
གཡོས་པར༌[^1575]མ་གྱུར་ཞེས་བྱ་བ་ནི་ཚུལ་ཁྲིམས་ལ་བརྟན་པར་གྱུར་པ་བསྟན་ཏོ། །

[Block 2467]
གྲོགས་དང་ལྡན་ཞིང་ཕུན་སུམ་ཚོགས་པའི་ཡོ་བྱད་གང་ལ་ཡོད་པ་དེ་ནི་གྲོགས་ལྡན་ཡོ་བྱད་ཕུན་སུམ་ཚོགས་པ་སྟེ་དེ་ལའོ། །

[Block 2468]
ཕོངས་པ་ཡང་ཡིན་ལ་རབ་ཏུ་མགུ་བ་ཡང་ཡིན་པས་ཕོངས་པ་རབ་ཏུ་མགུ་བའོ། །

[Block 2469]
དེའི་བསྟོད་པ་དེས༌[^1576]རབ་ཏུ་འཕེལ་བའི་ཚིག་ནི་ཕོངས་པས་རབ་ཏུ་དགའ་བས་བསྟོད་པའི་ཚིག་གོ། །

[Block 2470]
སྣ་ཚོགས་པ་ནི་རྣམ་པ་དུ་མའོ། །

[Block 2471]
གོས་དང་རྒྱན༌[^1577]རྣམས་ནི་གོས་དང་རྒྱན་ནོ། །

[Block 2472]
གོས་རྣམ་པ་སྣ་ཚོགས་པ་མང་པོ་དང་། རྒྱན་རྣམ་པ་སྣ་ཚོགས་བ་སྟེ། གོས་དང་རྒྱན་རྣམ་པ་སྣ་ཚོགས་པས་བརྒྱན་པ་གང་ཡིན་པ་དེ་ནི་རྣམ་མང་གོས་དང་སྣ་ཚོགས་རྒྱན་གྱིས་བརྒྱན་པའོ། །

[Block 2473]
སྐྱེ་བོ་ངེས་པར་ཆོས་སྤྱོད༌[^1578]ཅེས་བྱ་བ་ནི་ལྡོག་པའི་ཚུལ་དང་འཇུག་པའི་ཚུལ་གྱིས་ཚུལ་ཁྲིམས་ལ་འབད་པའོ། །

[Block 2474]
སྐྱེ་བོ་རབ་ཏུ་དགའ་བ་མང་པོས་གང་ཞིང་ཞེས་བྱ་བ་འདིས་ནི་སེམས་ཅན་གྱི་གྲངས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 2475]
མངོན་པར་མཐོ་བ་ཉམས་དགའ་བར་སྣང་བ་ཞེས་བྱ་བ་འདིས་ནི་སྐྱེ་བོ་མང་པོའི་འབྱོར་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 2476]
བརྒྱ་བྱིན་ནི་མཆོད་སྦྱིན་བརྒྱ་བའོ། །

[Block 2477]
གསོད༌[^1579]ཅིང་ཅེས་བྱ་བ་ནི་དེ་ལ་ཕྱུགས་དུ་མ་གསོད་པའི་ཕྱིར་ཏེ། དམན་པ་འབྲས་བུ་འདོད་པ་དེས་འཚེ་བ་ལ་ཞེན་པའོ། །

[Block 2478]
དམན་པ་དེའི་མི་མཐུན་པའི་ཕྱོགས་ཚུལ་ཁྲིམས་ཡིན་ཏེ། དམན་པའི་མི་མཐུན་པའི་ཕྱོགས་གྲགས་པའི་རྒྱན་གྱིས་བརྒྱན་པ་ནི་འབྲས་བུ་ལ་འདོད་པ་མེད་པས་གྲགས་པ་མངོན་པར་འཕེལ་བའོ། །

[Block 2479]
སྐྱེ་དགུ་བུ་བཞིན་དུ་སྐྱོབ་པ་ནི༌[^1580]སྲུང་བའོ། །

[Block 2480]
དེའི་དབང་དུ་གྱུར་པ་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་འདིར་དབང་དུ་གྱུར་པ་དང་། འཇིག་རྟེན་ཕ་རོལ་གྱི་ལོངས་སྤྱོད་ཀྱི་དབང་དུ་གྱུར་པའོ། །

[Block 2481]
འཇིག་རྟེན་བདེ་ལ་ཕྱོགས་ཤིང་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་གྱི་བདེ་བ་ལ་མངོན་དུ་ཕྱོགས་པ་ནི་ཇི་ལྟར་ཡང་བདག་ལ་དད་པའི་འཇིག་རྟེན་ཚུལ་ཁྲིམས་དང་ལྡན་པར་བྱས་པའོ། །

[Block 2482]
དེ་གཉིས་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་ཏེ། མཁས་པ་མ་ལགས་པ་ནི་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་ལ་འཇུག་པ་ཡོངས༌[^1581]མ་མཆིས་པའོ། །

[Block 2483]
གཞན་ལ་ཕན་ཞིང་བདེ་བ་ལ་འཇུག་པ་ཡོན་ཏན་ཡོངས་སུ་ཤེས་པས་ནི་གཞན་གྱི་དོན་དུ་དེ་གཉིས་ལ་འཇུག་པ་ཡིན་ཏེ། མཁས་ཤིང་ཡོངས་སུ་ཤེས་པས་སྙིང་སྟོབས་དང་ལྡན་ན་ནི་བདག་ལ་ཆགས་པ་མེད་པར་སྦྱིན་པ་དང་ཚུལ་ཁྲིམས་དེ་གཉིས་ལ་འཇུག་སྟེ། སྙིང་སྟོབས་མ་ཚང་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 2484]
ལེགས་པར་ཐོབ་པ་ནི་ཚེ་འདིར་ཡང་འཕེལ་བར་འགྱུར་ལ། འཇིག་རྟེན་ཕ་རོལ་དུ་ཡང་བདེ་འགྲོ་ཐོབ་པའོ། །

[Block 2485]
གྲགས་པ་དང་བདེ་བ་ཐོབ་བ་ནི་ཚེ་འདིར་ཡང་བདེ་བ་ཐོབ་ཅིང་འཇིག་རྟེན་ཕ་རོལ་དུ་ཡང་བདེ་བ་འཐོབ༌[^1582]པའོ། །

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
--- END BLOCKS ---
