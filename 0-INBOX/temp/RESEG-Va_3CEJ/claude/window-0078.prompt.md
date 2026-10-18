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
[Block 2731]
དེས་ན་འདི་ནི་སངས་རྒྱས་རྣམས་ཀྱིས་ཀྱང་དགག་པར་མི་སྤྱོད་དེ། ལས་སྟོབས་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 2732]
དབང་པོ་ཀུན་ཚང་། དབང་པོ་ལྔ་ཆར་ཚང་བའོ། །

[Block 2733]
ཐོགས་མེད་ལྡན། ཐོགས་པ་ནི་རྡུགས་པའོ། །

[Block 2734]
དེ་འདི་ལ་ཡོད་པས་ཐོགས་པ་དང་ལྡན་པའོ། །

[Block 2735]
ཐོགས་པ་མེད་པ་དང་ལྡན་པས་ན་ཐོགས་མེད་ལྡན་ཏེ། རྡོ་རྗེ་ལ་སོགས་པས་ཀྱང་མི་ཟློགས༌[^1484]པའི་ཕྱིར་རོ། །

[Block 2736]
འདི་ལྟར་ལྕགས་ཀྱི་ཐུ་ལུམ་འབར་བ་གཤགས་ནས༌[^1485]དེའི་ནང་ནས་བྱུང་བའི་སྲིན་བུ་དམིགས་སོ་ཞེས་གྲག་གོ། །

[Block 2737]
དེ་འགྲོ་བ་གང་དུ་སྐྱེ་བར་འགྱུར་བ་དེ༌[^1486]ལས་རྣམ་པ་ཐམས་ཅད་དུ་མི་ཟློགས༌[^1487]ཏེ། མིའི་སྲིད་པ་བར་མ་མེད་པར་གྱུར་ནས་ལྷའི་སྲིད་པ་བར་མའམ། གཞན་དུ་འགྱུར་བ་ནི༌[^1488]ནམ་ཡང་མེད་ཀྱི་འདི༌[^1489]འགྲོ་བ༌[^1490]གང་གི༌[^1491]དབང་དུ་བྱས་ནས་མངོན་པར་འགྲུབ་པ་དེ་ཁོ་ནར་སྐྱེ་བར་འགྱུར་གྱི་གཞན་དུ་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བར་ངེས་སོ། །

[Block 2738]
ཡང་ཅི་འདོད་པ་ན་སྤྱོད་པའི་སྲིད་པ་བར་མ་ཡང་ཁམ་གྱི་ཟས་ཟའམ་ཞེ་ན། སྨྲས་པ་དེ་བཞིན་ཏེ། རགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2739]
འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། དེ་ནི་དྲི་ཟའོ། །

[Block 2740]
དེ་ཉིད་ཀྱི་ཕྱིར་དྲི་ཟ་ཞེས་བྱའོ། །

[Block 2741]
དབང་ཆུང་བར་གྲགས་པ་ནི་དྲི་མི་ཞིམ་པ་ཟ་བའོ། །

[Block 2742]
དབང་ཆེ་བར་གྲགས་པ་ནི་དྲི་ཞིམ་པོ་ཟ་བའོ། །

[Block 2743 [HEADING]]
##### དུས་ཇི་སྲིད་ཀྱི་བར་དུ་གནས་པ། ^3-1-7-3-0

[Block 2744]
དུས་ཇི་སྲིད་ཀྱི་བར་དུ་གནས་ཤེ་ན། བཙུན་པ་ན་རེ་ངེས་པ་མེད་དེ། ཇི་སྲིད་དུ་སྐྱེ་བའི་ཚོགས་པ་མ་རྙེད་ཀྱི་བར་དུའོ། །

[Block 2745]
དེའི་ཚེ་འཕེན་པ་ལོགས་ཤིག་ན་མེད་དེ། [^1492]རིས་མཐུན་པ་གཅིག་པའི་ཕྱིར་རོ། །

[Block 2746]
དེ་ལྟ་མ་ཡིན་ན་དེའི་ཚེ་ཟད་པས༌[^1493]འཆི་བའི་སྲིད་པར་ཡང་ཐལ་བར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 2747]
གལ་ཏེ་ཤའི་ཕུང་པོ་རི་རབ་ཙམ་དུ་གྱུར་ལ་དེ་དག་ཐམས་ཅད་སྲིན་བུ་རྣམས་ཀྱིས་གང་བར་གྱུར་ན། དེ་ཅི་དེ་དག་གི༌[^1494]སྲིད་པ་བར་མ་རྣམས་དེར་སྡོད་པ་ཁོ་ནར་གྱུར་ཏམ། དེ་དག་ག་ལས་འོངས་པ་བརྗོད་པར་བྱའོ་ཞེ་ན། འདི་མདོའམ་བསྟན་བཅོས་དག་ལས་ནི་མི་འབྱུང༌[^1495]མོད་ཀྱི། འདི་ལྟར་དྲི་དང་རོ་ལ་མངོན་པར་ཆགས་པའི་སྐྱེ་བོ༌[^1496]ཕྲ་མོ་ཚེ་ཐུང་ངུ་རྣམས་མཐའ་མེད་པས་དེ་དག་དྲི་ཚོར་ནས་དྲི་དང་རོ་ལ་མངོན་པར་ཆགས་པ་རྣམས་འཆི་བ་ན་སྲིན་བུའི་ངོ་བོར་འགྱུར་བའི་ལས་སད་པར་བྱས་ནས། སྲིད་པ་དེས་སྲིན་བུའི༌[^1497]ནད་དག་ཏུ་སྐྱེ་བར་འགྱུར་བར་མི༌[^1498]རུང་ངོ་། །ཡང་ན་གདོན་མི་ཟ་བར་དེའི་རྐྱེན་མང་པོ་ཁོ་ནའི་དུས་སུ་དེར་འགྱུར་བའི་ལས་རྣམས་རྣམ་པར་སྨིན་པ་མངོན་པར་འགྲུབ་པར་བྱ་བ་ལ་འཇུག་པ་རྙེད་ཀྱི་གཞན་དུ་ནི་མ་ཡིན་ཏེ། འདི་ལྟར་འཁོར་ལོས་སྒྱུར་བའི་ལས་ཡོད་དུ་ཟིན་ཀྱང་སྐྱེ་དགུའི་ཚེ་ལོ་བརྒྱད་ཁྲི་འམ། ཚེ་ལོ་ཆེས་མང་བ་ན་འཁོར་ལོས་སྒྱུར་བ་འབྱུང་གི༌[^1499]གཞན་དུ་མ་ཡིན་པ་ལྟ་བུའོ། །

[Block 2748]
དེ་ཉིད་ཀྱི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་སེམས་ཅན་རྣམས་ཀྱི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ནི་བསམ་གྱིས་མི་ཁྱབ་བོ་ཞེས་གསུངས་སོ། །

[Block 2749]
བཙུན་པ་དབྱིག་བཤེས་ན་རེ་ཞག་བདུན་དུ་གནས་སོ། །

[Block 2750]
གལ་ཏེ་དེ་སྲིད༌[^1500]ཀྱི་ཚོགས་པ་མ་རྙེད་ན་ཤི་འཕོས་ཤིང་ཤི༌[^1501]འཕོས་ནས་ཡང་དེ་ཉིད་དུ་སྐྱེ་བར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 2751]
གཞན་དག་ན་རེ་ཞག་བདུན་ཕྲག་བདུན་དུའོ་ཞེས་ཟེར་རོ། །

[Block 2752]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་དེ་ནི་སྲིད་པ་ཚོལ་བ་ཡིན་པའི་ཕྱིར་མྱུར་བ་ཁོ་ནས༌[^1502]སོང་སྟེ་ཉིང་མཚམས་སྦྱོར་བས་ན་དུས་ཐུང་ངུར་གནས་སོ།[^1503] །གང་གི་ཚེ་རྐྱེན་ཚོགས་པ་ཡང་མ་ཡིན་ལ་འདི་ངེས་པར་ཡུལ་དེར་སྐྱེ༌[^1504]བར་འགྱུར་བ་ཡང་ཡིན་ནོ༌[^1505]དེའི་ཚེ་ལས་རྣམས༌[^1506]ཁོ་ནས་རྐྱེན་དག་ཚོགས་པ་འདྲེན་པར་བྱེད་དོ། །

[Block 2753]
འོན་ཏེ་མ་ངེས་ན་ནི་དེ་ལས་གཞན་པའི་ཡུལ་དུ་སྐྱེ་བ་དེར་སྐྱེ་བར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 2754]
གཞན་དག་ན་རེ་དེ་འདྲ་བར་སྐྱེ་བར༌[^1507]འགྱུར་ཏེ། འདི་ལྟ་སྟེ་བ་ལང་དག་ནི་དབྱར་རྣམས་སུ་འཁྲིག་པ་མང༌[^1508]ལ། ཁྱི་རྣམས་ནི་སྟོན་ཀར་རོ། །

[Block 2755]
དོམ་རྣམས་ནི་དགུན་ཀར་རོ། །

[Block 2756]
རྟ་རྣམས་ནི་སོས་ཀར་རོ། །

[Block 2757]
བ་མེན་དང་། ཅེ་སྤྱང་དང་། བོང་བུ་དང་། དྲེད་མོ་རྣམས་ལ་ནི་དུས་མེད་པས་དུས་གཞན་པ༌[^1509]བ་ལང་རྣམས་ཀྱི་ནང་དུ་སྐྱེ་བར་འགྱུར་བ་གང་ཡིན་པ་དེ་ནི་བ་མེན་རྣམས་ཀྱི་ནང་དུ་སྐྱེའོ། །

[Block 2758]
[^1510]ཁྱི་རྣམས་ཀྱི་ནང་དུ་གང་ཡིན་པ་དེ་ནི་ཅེ་སྤྱང་རྣམས་ཀྱི་ནང་དུའོ། །

[Block 2759]
རྟ་རྣམས་ཀྱི་ནང་དུ་གང་ཡིན་པ་དེ་ནི་བོང་བུ་རྣམས་ཀྱི་ནང་དུའོ། །

[Block 2760]
དོམ་རྣམས་ཀྱི་ནང་དུ་གང་ཡིན་པ་དེ་ནི་དྲེད་མོ་རྣམས་ཀྱི་ནང་དུ་སྐྱེ་བར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 2761]
འཕེན་པ་གཅིག་པའི་ཕྱིར་རིས་གཞན་གྱི་སྲིད་པ་བར་མས་རིས༌[^1511]མཐུན་པ་གཞན་དུ་སྐྱེ་བར་མི་ནུས་པས་དེ་ནི་བརྗོད་པར་བྱ་བ་མ༌[^1512]ཡིན་ནོ། །

[Block 2762 [HEADING]]
##### འགྲོ་བའི་ཡུལ་དུ་འགྲོ་བ། ^3-1-7-4-0

[Block 2763]
ཡང་འགྲོ་བའི་ཡུལ་དུ་ཕྱིན་པར་བྱ་བའི་ཕྱིར་འབྱུང་བའི་སྲིད་པ་བར་མ་དེ་ནི།

[Block 2764 [VERSE]]
བློ་ནི་ཕྱིན་ཅི་ལོག་གྱུར་པས། །
རྩེ་དགས་འགྲོ་བའི་ཡུལ་དུ་འགྲོ། །

[Block 2765]
ད༌[^1513]ནི་ལས་ཀྱི་མཐུ་ལས་བྱུང་བའི་མིག་གིས་རང་གི་སྐྱེ་བའི་ཡུལ་ཐག་རིང་པོ་ན་འདུག་ཀྱང་མཐོང་ངོ་། །དེས་དེ་ན་ཕ་མ་ཉལ་པོ་བྱེད་པ་དེ་མཐོང་ནས་ཕོ་ཞིག་ཡིན་ན་ནི་དེས༌[^1514]མ་ལ་ཕོའི༌[^1515]འདོད་ཆགས་སྐྱེའོ། །

[Block 2766]
མོ་ཞིག་ཡིན་ན་ནི་ཕ་ལ་མོའི་འདོད་ཆགས་སྐྱེའོ། །

[Block 2767]
བཟློག་པ་ནི་ཁོང་ཁྲོ་བ་སྐྱེ་བ༌[^1516]སྟེ། བཏགས་པ་ལས་འདི་སྐད་དུ་དེའི་ཚེ་དྲི་ཟ་ལ་སེམས་གཉིས་ལས་རྗེས་སུ་ཆགས་པ་དང་ལྡན་པའམ། ཁོང་ཁྲོ་བ་དང་ལྡན་པའི་སེམས་གང་ཡང་རུང་བའི༌[^1517]མངོན་དུ་གྱུར་པ་ཡིན་ནོ་ཞེས་འབྱུང་ངོ་། །དེ་ནི༌[^1518]གཉིས་ཀྱི༌[^1519]ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པས་ཡུལ་དེར་ཕྱིན་པ་དང་། དགའ་བར་འདོད་པའི༌[^1520]གནས་སྐབས་དེར་བདག་ཉིད་མོས་སོ། །

[Block 2768]
མངལ་གྱི་གནས་མི་གཙང་བ་དེར་ཕྱིན་ནས་དགའ་བ་སྐྱེས་ནས་གནས་སོ། །

[Block 2769]
དེ་ནས་དེའི་ཕུང་པོ་མཁྲང་པོར་འགྱུར་ལ་སྲིད་པ་བར་མ་ཡང་འགག་པར་འགྱུར་བས་ན་སྐྱེས་པ་ཡིན་ནོ། །

[Block 2770]
གལ་ཏེ་དེ་ཕོ་ཞིག་ཡིན་ན་ནི་མའི་ལྟོའི་གཡས་ཕྱོགས་སུ་སྙེས༌[^1521]ནས་རྒྱབ་རོལ་དུ་ཁ་བལྟས་ཏེ་ཙོག་ཙོག་པོར་སྐྱེའོ། །
--- END BLOCKS ---
