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
ལུས་ཀྱི་བྱ་བས་དང་དུ་ལེན་ན་ཉེས་བྱས་སོ། །གང་ཞེ་ན།

[Block 2522]
འདིར་གཞུང་ནི་སྤྱིར་བསྟན་པ་ལས།

[Block 2523]
ཚིག་གིས་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2524]
བརྡའོ་མཚན་མའོ་ཞེས་བྱ་བ་ནི་སྐྱེས་པ་ཆགས་པ་ལ་བྱེད་པ་དང་ནོད་པ་ལ་ཞེས་བྱ་བར་སྦྱོར༌[^1612]རོ། །

[Block 2525]
བརྡ་ཞེས་བྱ་བ་ནི་དུས་ཚོད་ཀྱི་བརྡ་སྟེ། ཁོ་མོ་སྔ་དྲོ་སྟ་གོན་བྱེད་དོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་དུས་ཚོད་ཀྱི་བརྡས་དུས་འདེབས་པར་བྱེད་པར་རིག་པར་བྱའོ། །

[Block 2526]
མཚན་མས༌[^1613]ཞེས་བྱ་བ་ནི་ཁོ་མོ་གོས་འདི་ལྟ་བུ་གོན་པ་ཁྱོད་ཀྱིས་མཐོང་ན་སྟ་གོན་གྱིས་ཤིག་ཅེས་བྱ་བ་ལ་སོགས་པའི་མཚན་མ་བྱེད་པར་རིག་པར་བྱའོ། །

[Block 2527]
དེའི་འོང་བ་དང་འགྲོ་བའི་འཇུག་པ་བདག་གིར་བྱེད་ནའོ་ཞེས་བྱ་བ་ལ། འོང་བ་ཞེས་བྱ་བ་ནི་གང་ན་དེ་འདུག་པ་དེར་འོང་བའོ། །

[Block 2528]
འགྲོ་བ་ཞེས་བྱ་བ་ནི་དུས་མལ་བཏབ་པའི་གནས་སུ་འགྲོ་བའོ། །

[Block 2529]
སྐྱེས་པ་ཆགས་པར་གྱུར་པ་དེའི་འོང་བ་དང་འགྲོ་བའི་འཇུག་པ་བདག་གིར་བྱེད་ན་དགེ་སློང་མ་ལ་ནི་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2530]
ལུས་བཀན་པ་ནི་དགེ་སློང་ལ་ནི་སྦོམ་པོ་སྟེ། གཞན་ནི་ཚིག་ཏུ་མ་སྨྲས་ན་ནི་ཉེས་བྱས་སོ་ཞེས་བྱ་བ་དེའི་རྗེས་སུ་འབྲངས་ནས་ཤེས་པར་བྱའོ། །

[Block 2531]
བུད་མེད་ལ་ཚིག་ཏུ་སྨྲས་ན་ནི་དགེ་འདུན་ལྷག་མའོ། །

[Block 2532]
ལུས་བཀན་པའི་ཕམ་པར་འགྱུར་བའོ། །གང་ལ་ཁ་ན་མ་ཐོ་བ་འཆབ་པའི་ཕམ་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མའི་ཕམ་པར་འགྱུར་བ་འཆབ་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མ་དང་འབྲེལ་པའི་བརྒྱད་པོ་དག་ལས་གང་ཡང་རུང་བ་ལ་ཡང་ངོ་། །སུའི་ཕམ་པར་འགྱུར་བ་ཞེ་ན། དེའི་ཕྱིར་འདིར་དགེ་སློང་མའི་ཞེས་སྨོས་ཏེ། འདིར་ཉིན་མཚན་གྱི་མཐར་ནི་ཁ་ན་མ་ཐོ་བ་རྫོགས་པར་འགྱུར་ལ། མདུན་རོལ་དུ་ནི་ན་སྨད་དོ། །

[Block 2533]
འདིར་གཞུང་ནི་གཏམ་གྱི་གཞི་ལས།

[Block 2534]
དགེ་སློང་མ་མི་ཚངས་པར་སྤྱོད་པ་བྱེད་པ་མཐོང་ལ་དེ་བཅབས་ཤིང་འདུ་ཤེས་སྦས་ན་སྐྱ་རེངས་ཤར་ན་ཕམ་པར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2535]
འདི་ལ་ན་སྨད་ན་སྦོམ་པོ་སྟེ། དེ་བས་ན་སྡེ་པ་འདི་ལ་སྦོམ་པོ་ཞེས་རྟོགས་པར་བྱའོ། །

[Block 2536]
འཆབ་པའི༌[^1614]ཕམ་པར་འགྱུར་བའོ། །ཅི་ཞིག་བྱས་ན་བཟློག་པའི༌[^1615]ཕམ་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་གནས་ནས་ཕྱུང་བ་བཟོད་པ་གསོལ་བར་ངེས་པ་ཕྱག་བྱ་བའི་འོས་མ་ཡིན་པའི་སྡོམ་པ་བྱིན་པར༌[^1616]ཤེས་བཞིན་དུ་དེ་ལས༌[^1617]བཟློག་པ་ཉིད་མི་གཏོང་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་སྐད་བསྟན་ཏེ་དགེ་སློང་གྲེ་སྐྱེས་དགེ་སློང་མ་རྣམས་དང་འདྲེ་ཞིང་གནས་ནས་བཅོམ་ལྡན་འདས་ཀྱི༌[^1618]བཀས་དགེ་སློང་གི་དགེ་འདུན་གྱིས་གནས་ནས་ཕྱུང་བའི་ལས་བྱས་ཤིང་དགེ་སློང་མའི་དགེ་འདུན་གྱིས་ཀྱང་ཕྱག་བྱ་བའི་འོས་མ་ཡིན་པའི་སྡོམ་པ་བྱས་ནས། གཉིས་ཀའི་དགེ་འདུན་གྱིས་ཕྱི་རོལ་དུ་བྱས་པའི་དགེ་སློང་གི་དགེ་འདུན་ལ་བཟོད་པར་གསོལ་ལོ་ཞེས་ངེས་པར་གྱུར་ནས། སྦོམ་དགའ་མོས་དོན་དེ་ཤེས་བཞིན་དུ་ཕྱིར་བཟློག་པ་དེ་ལ༌[^1619]དགེ་སློང་མའི་དགེ་འདུན་གྱིས་བཞམས༌[^1620]ཏེ་བསྒོ་བ་ལ་སོགས་པ་གསོལ་བ་དང་། བཞིའི་ལས་ཀྱིས་བསྒོ་བ་ནི༌[^1621]བཟློག་པ་དེ་ཉིད་མ༌[^1622]གཏོང་བ་དེ་ལ་ཕམ་པར་འགྱུར་བ་བཅས་པ་ཡིན་ཏེ། དེ་བས་ན་འདིར་མདོ་འདི་བྱས་པ་ཡིན་ནོ། །

[Block 2537]
ཕྱག་བྱ་བ༌[^1623]མ་ཡིན་པའི་སྡོམ་པ་བྱས་ནས་ཞེས་བྱ་བ་ནི། དགེ་སློང་མ་རྣམས་ཀྱིས་བྱས་པ་ནི་ཕྱག་བྱ་བའི་འོས་མ་ཡིན་པའི་སྡོམ་པ་འདི་ལ་དེ་ལྟ་བས་ན་ཕྱག་བྱ་བའི་འོས་མ་ཡིན་པའི་སྡོམ་པ་བྱིན་པའོ། །

[Block 2538]
དགེ་སློང་གནས་ནས་ཕྱུང་བ་ཞེས་བྱ་བ་ནི། ཕྱག་བྱ་བའི་འོས་མ་ཡིན་པའི་སྡོམ་པ་བྱིན་པར་ཤེས་བཞིན་དུ་དགེ་འདུན་གྱིས༌[^1624]གནས་ནས་ཕྱུང་བ་བཟོད་པར་གསོལ་བར་ངེས་པར་ཤེས་ནས། དེ་ལས་བྱུང་བ་བཟོད་པར་གསོལ་བར་ངེས་ནས་དེ་ལས་བཟློག་པ་ཉིད་གང་ཡིན་པ་དེ་མི་གཏོང་ན་ཕམ་པར་ཞེས་བྱ་བའི་དོན་ཏོ། །ཇི་ལྟར་མི་གཏོང་བ་ལ་ཞེ་ན། དེའི་ཕྱིར་དབྱེན་ལ་བརྟུལ་བ་ཉིད་དང་འདྲའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟར་དགེ་འདུན་གྱི་དབྱེན་ལ་བརྟུལ་བར་བྱེད་པ་དེ་མི་གཏོང་བ་ལ་ལྟུང་བར་འགྱུར་བ་དེ་དང་འདྲའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2539]
དེ་དང་འདྲ་བར་བཞམས་པ༌[^1625]དང་གསོལ་བ་མངོན་དུ་བཏང་བའི་ལས་བྱས་ཏེ། ཇི་སྲིད་འདའ་བར་བྱེད་པ་དེ་སྲིད༌[^1626]ཐ་དད་པར་བརྗོད་པ་བསྒོ་བ༌[^1627]དང་འབྲེལ་པའི་རིམ་པ་དང་། དེའི་རྒྱུ་མཚན་འཇུག་པ་དང་འབྲེལ་པ་དེ་ཐམས་ཅད་འདིར་ཅི་རིགས་པར༌[^1628]རྟོགས་པར་བྱའོ། །

[Block 2540]
དགེ་སློང་མ་བཟློག་པ་ལ་ནི་འདི་ལ་ལྟུང་བྱེད་ཁོ་ནར་རིག་པར་བྱའོ། །

[Block 2541]
བཟློག་པའི་ཕམ་པར་འགྱུར་བའོ། །

[Block 2542]
དགེ་སློང་མའི་ཕམ་པར་འགྱུར་བ་རྣམས་རྫོགས་སོ།། །།

[Block 2543 [HEADING]]
## དགེ་སློང་མའི་དགེ་འདུན་ལྷག་མ་རྣམས། ^5-0

[Block 2544]
ཁུ་བ་འབྱིན་པར་གཏོགས་པའི༌[^1629]དགེ་འདུན་ལྷག་མ་དགེ་སློང་མ་རྣམས་ཀྱི༌[^1630]ལྟུང་བྱེད་དུ་རྣམ་པར་གཞག་ཟིན་ཏོ། །

[Block 2545]
རེག་པར་གཏོགས་པའི་ཕམ་པ་འཇུག་པ་ཉིད་ཀྱིས་སོ། །

[Block 2546]
དེ་བཞིན་དུ་བརྗོད་པ་དང་འབྲེལ་པའི་བསྙེན་བཀུར༌[^1631]བསྔགས་པ་འབྱུང་བའོ། །

[Block 2547]
གང་གི་ཕྱིར་བསྙེན་བཀུར་བསྔགས་པ་དང་འཁྲིག་པ་ལ་ནི་བུད་མེད་དོ། །

[Block 2548]
བསྙེན་བཀུར་བྱེད་པར་འགྱུར་བ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 2549]
འདིར་སྐྱེས་པ་ནི་གཡོག་ཕྲན༌[^1632]གྱི་ཆ་དང་བུད་མེད་ཀྱི་ཁང་པ་དང་གཙུག་ལག་ཁང་དང་འབྲེལ་པའི་འཇུག་པ་ལའོ། །

[Block 2550]
ཤིན་ཏུ་ཡང་འབྱུང་བ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་འདི་དག་ལ་མཐུ་དང་ལྡན་པའི་བྱེད་པ་པོ་ཉིད་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 2551]
བྱེད་དུ་བཅུག་པ་ཉིད་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། བདག་པོ་མེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2552]
བུད་མེད་རྣམས་ལ་ཁྱིམ་བྱེད་པའི་ཉོན་མོངས་པ་ལ་ནི༌[^1633]ཤིན་ཏུ་ཡང་གནས་པ་མ་ཡིན་ཏེ། སྐྱེས་པ༌[^1634]ནི་སྟོབས་དང་ལྡན་པ་ཉིད་དོ། །

[Block 2553]
དགེ་འདུན་གྱི་ལྷག་མ་འཇུག་པའི༌[^1635]ལྷག་མ་རྣམས་ནི་འདི་ལ་ཁ་ན་མ་ཐོ་བ་མ་ཆོག་པ་ལྷག་མ་རྣམས་དང་། ཁ་ན་མ་ཐོ་བ་མེད་པ་རྣམས་ལ་ནི་དགེ་སློང་ལ་དགེ་འདུན་གྱི་ལྷག་མ་འཇུག་པ་ཉིད་ཀྱིས་རྣམ་པར་གཞག་པ་བྱས་པ་ཡིན་ནོ། །

[Block 2554]
དེ་གཉིས་ཀྱང་བརྗོད་པར་བྱ་སྟེ་དེ་ལ་ཐུན་མོང་བ་ནི་མིང་ཙམ་རྣམ་པར་གཞག་པ་དག་ཅི་བསྟན་པའི་ཕྱིར་སྨྱན་བྱེད་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཞན་སྨྱན་བྱེད་པ་ནི་ངོ་བོ་བསྟན་པས་སོ། །

[Block 2555]
དགེ་འདུན་ལྷག་མ་ཁ་ན་མ་ཐོ་བ་འདིའི་མཚན་ཉིད་སྔར་ཇི་སྐད་བསྟན་པ་དེ་ཉིད་དགེ་སློང་མ་རྣམས་ཀྱི་ཡང་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2556]
སྐབས་འདི་དང་འོག་མ་དག་ལས་ཆོས་འདི་ནི་དང་པོས་ལྟུང་བར་འགྱུར་ལ་ཞེས་གསུངས་པའི་ཚིག་དེའི་རྣམ་པར་འབྱེད་པ་ནི་མདོ་ལས་ལྟུང་བར་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེའི་དོན་ནི་སྤྱད་པ་ཙམ་གྱིས་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་གྱི། ཡང་དང་ཡང་དུ་ཕྱིར་བཟློག་ཅིང་མི་གཏོང་བ༌[^1636]ལ་ནི་མ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2557]
འབྱུང་བར་འགྱུར་བས་ཏེ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ལྟུང་བ་ལས་འབྱུང་བ་དང་རྗེས་སུ་མཐུན་པ་དེ་ནི་ཕམ་པར་འགྱུར་བ་དག་ལྟར༌[^1637]ཕྱིར་བཅོས་སུ་མི་རུང་བ༌[^1638]མ་ཡིན་ནོ། །

[Block 2558]
དེ་ལྟར་ཡང་དེའི་རྣམ་པར་འབྱེད་པ་ནི་ལྟུང་བ་དང་བཅས་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2559]
འདིར་ཅུང་ཟད་དགེ་སློང་མ་ལ༌[^1639]བརྟེན་ཏེ་ཕྲན་ཚེགས་དག་ལས་ཅུང་ཟད་ལྷག་པར་གསུངས་པ་དག་བསྟན་པའི་ཕྱིར་དགེ་སློང་མ་ལ་ཁྱིམ་པ་མོ་ཉིད་ཀྱི་བསྔགས་པ་བརྗོད་ན༌[^1640]སྦོམ་པོའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྔགས་པ་བརྗོད་པ་ཞེས་བྱ་བ་ནི་གང་ཞིག་འབྲེལ་པ་བསྟན་པས་ཡང་དག་པར་འཛིན་དུ་འཇུག་པའོ། །

[Block 2560]
འདི་ཡང་འདོད་པ་ལ་བརྟེན་པ་དང་ཕན་ཡོན་བསྟན་པས་གང་ཡང་རུང་བའི་མངོན་པར་འདོད་པ་གླེང་གཞི་ལས་རྟོགས་པའོ། །
--- END BLOCKS ---
