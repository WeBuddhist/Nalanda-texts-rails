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
[Block 2556]
ཆོམ་རྐུན་པ་ལས་སྦྱིན་བདག་གི་སེམས་ཀྱིས༌[^1734]ལེན་པ་ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ཆོམ་རྐུན་པ་དེའི་དྲུང་ནས་བླངས་པ༌[^1735]གང་ཡིན་པ་དེ་ལ་འདི་ནི་སྦྱིན་བདག་སྙམ་པའི༌[^1736]སེམས་ཀྱིས་ལེན་ན་དེ་ལ་ཉེས་པ་མེད་དོ། །

[Block 2557]
ཇི་ལྟར་གཞན་ལས༌[^1737]བླངས་པ་ལ་ཉེས་པ་མེད་པ་དེ་བཞིན་དུ་འདི་ལའོ། །

[Block 2558]
གང་གི་ཕྱིར་འདིས་བརྐུས་པ་དེ་ཉིད་ཀྱིས་འདི་འབྲེལ་པའོ། །

[Block 2559]
ནོར་འདི་ལ་འདི་ནི་བདག་པོ་སྟེ་དེ་ཉིད་ཀྱིས་འདི་གནང་བ་ཞེས་བྱ་བ་འདི་ལྟར་ཡོངས་སུ་མ་དག་པའི་སེམས་ཀྱིས་བླངས་པ་ལ་ལྟུང་བ་དང་བཅས་པ་ཉིད་དུ་འགྱུར་རོ། །

[Block 2560]
དེ་བས་ན་སྦྱིན་པ་པོའི་སེམས་ཀྱིས་ཞེས་བྱ་བ་འདི་ནི་བྱེ་བྲག་གོ། །

[Block 2561]
འོང་བ་རྐུ་ཐབས་ཅན་གྱི་ཆོམ་རྐུན་པར་མ་གྲགས་པ་ལས་བླང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་མ་ཤེས་པ་དང་གློ་བུར་དུ་གྱུར་པ་མ་གྲགས་པ་ལས་བླང་བར༌[^1738]མི་བྱའོ། །

[Block 2562]
རྐུ་བ་ཡང་དག་པར་སྲིད་པ་ལ་གླགས་གཅད་པའི༌[^1739]དོན་དུ་འདི་བཏགས་པའོ། །

[Block 2563]
གང་གི་ཕྱིར་རྐུ་བ་དེ་ལ་གང་ཞིག་ཤེས་པ་དེ་ནི་གྲགས་པ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 2564]
གྲགས་པ་ལས་བླངས་པ་ལ་ཆོམ་རྐུན་པ་ཉིད་ཀྱིས་འདི་བརྐུས་ཏེ་གཞན་གྱི་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའི་རྐུ་བ་ཡང་དག་པར་སྲིད་པ་ལ་གླགས་མེད་དོ། །

[Block 2565]
དེ་ལས་བླངས་པ་ནི་མཚོན་གྱིས་བཅད་པ་དང་ཁ་དོག་ངན་པར་བྱ་སྟེ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་གྲགས་པ་ལས་དེ་ལྟ་བུར་གྱུར་པ་ཉིད་འཛིན་པ་ལ་སུ་ཞིག་ལ་གློ་བུར་དུ་མ་བཅད་པ་ཡོད་པ་སྲིད་པར་འགྱུར་རོ་ཞེས་བྱ་བ་འདི་བཏགས་པའོ་དེ་ལྟར་བྱས་ཀྱང་སློང་ན་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་ལྟར་བརྐུས་པ་ལ་ཡང་མཚོན་གྱིས་གཅད་པ༌[^1740]དང་། ཁ་དོག་ངན་པར་བྱས་ཀྱང་སློང་ན་གང་ལས་དེ་བརྐུས་པ་དེས་ཤེས་ཏེ་གལ་ཏེ་སློང་བ་དེ་ལ་དེར་སྦྱིན་པར་བྱ་བའི་དོན་ཏོ། །

[Block 2566]
གནད་ལ་བསྒྲེ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། གཡོན་པོས་གནོད་པ་ནི་ཡོད་པའོ། །

[Block 2567]
གང་གི་ཚེ་ཚེ་དང་ལྡན་པ་སྤོང་བྱེད་ཀྱིས་བཟོད་པར་བྱ་བའི་ཕྱིར་ཁྱིམ་པ་རྣམས་ཀྱིས་འཕགས་པ་ཀུན་དགའ་བོ་ལ་ཁྱེའུ་དང་བུ་མོ་ངུ་བ་དག་སྡུད་དུ་བཅུག་སྟེ་གནོད་པར་བྱེད་པ་དེའི་ཚེ་ཐམས་ཅད་དུ་སྦྱར་བ་འདི་ཐམས་ཅད་ཀྱིས༌[^1741]བྱ་བ་ཉེ་བར་བཏགས་པའོ། །

[Block 2568]
མ་བྱིན་པར༌[^1742]ལེན་པ་ལ་ཡང་འདི་སྦྱར་བ་ཡོད་དེ་རྡོ་རྗེ་ཕ་ལམ་གྱིས་བརྐུས་པ་ལ་གཏོང་བ་དང་སྦྱིན་དུ་འཇུག་པ་ལ་ནོར་ལ་ཁ་ན་མ་ཐོ་བ་ཉིད་དང་བཅས་པ་ཞེས་བྱ་བ་འདི་ལས་རྟོགས་པར་བྱའོ། །

[Block 2569]
གསང་སྔགས་དག་གིས་གཏོང་བ་ལ་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་རྫུ་འཕྲུལ་དང་འདྲ་བའི་རྣམ་པར་དག་པ་དང་སྐྱོན་མེད་པའི་སེམས་ཀྱིས༌[^1743]རྐུ་བའི་རྣམ་པ་ངེས་པ་གང་གིས་ཀྱང་བརྐུས་པ་ཆོམ་རྐུན་པ་རྣམས་ལས་གསང་སྔགས་རྣམས་གསང་སྔགས་ཀྱིས་གཏོང་བ་གང་ཡིན་པ་དེ་ནི་ཉེས་པ་དང་བཅས་པར་ཤེས་པར་བྱ་བ་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2570]
བྱི་བས་ཁྱེར་བ་བདག་པོས་བླངས་པ་ཡང་ངོ་ཞེས་བྱ་བ་གང་ཞིག་ལེན་པ་པོ་འདི་དེའི་རྫས་བྱི་བས་བརྐུས་པ་བླངས་པ་ལ་ཡང་ཉེས་པ་མེད་དོ། །

[Block 2571]
རང་གི་འདུ་ཤེས་ཉིད་ཀྱིས་དེ༌[^1744]ལེན་པ་ཞེས་བྱ་བ་འདིར་ཉེས་པ་དང་བྲལ་བ་ཉིད་དོ། །

[Block 2572]
དགེ་སློང་གཞན་གྱི་རྫས་ལ་དེའི་རྫས་སུ་ན་ཡང་ངོ༌[^1745]ཞེས་བྱ་བ་ནི་དགེ་སློང་གཞན་གང་ལ་ནོར་དེ་བརྐུས་པ་དེ་ལ་ནོར་ལེན་པར་བྱེད་པ་ལ་ཉེས་པ་མེད་དེ། རྐུ་སེམས་མེད་པའི་ཕྱིར་རོ། །

[Block 2573]
རྔོན་པ་དག་གིས་མངོན་པར་གཙེས་པར་གྱུར་པའི་རི་དགས་གནས་ཁང་དུ་ཞུགས་པ་བླངས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡོངས་སུ་བསྐྱབ་པ༌[^1746]ཙམ་དུ་འདི་བླངས་པ་སྟེ། བཟུང་བ་མ་ཡིན་ཞིང་གཏོང་བ་ཡང་མ་ཡིན་ནོ། །

[Block 2574]
དེ་བས་ན་འདིར་སྐྱོན་མེད་དོ། །

[Block 2575]
དེ་ཤི་ན་དེ་དག་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དེ་དག་གིས་གཙེས་པས་དེར་ཞུགས་ན་དེ་རྣམས་ལ་སྦྱིན་པར་བྱ་བ་ཉིད་དེ་རང་གིས་གཟུང་བར་བྱ་བ་ཉིད་དང་གཞན་ལ་སྦྱིན་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་དོ། །

[Block 2576]
ཕམ་པ་གཉིས་པའི་འདུལ་བྱེད་ཀྱི་སྐབས་སོ།། །།

[Block 2577 [HEADING]]
## ཕམ་པར་འགྱུར་བ་གསུམ་པ། ^4-0

[Block 2578]
ནད་པ་ལ་འཆི་བའི་སེམས་པ་དང་རྗེས་སུ་མཐུན་པའི་ཆོས་ཉེ་བར་བསྒྲུབ་པས་ཉེ་བར་བསྒྲུབ་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཉེ་བར་བསྒྲུབ་པ་གང་ཞིག་ཐོས་ནས་ནད་པ་འདི་འཆི་བའི་བསམ་པ་སྐྱེས་པར༌[^1747]འགྱུར་བའི་ཉེ་བར་བསྒྲུབ་པ་དེ་ནི་ནད་པའི་ཕྱིར་མི་བྱའོ། །

[Block 2579]
དཔེར་ན་ཁྱོད་དུག་ཟོས་པར་གྱུར་པ་ནི་བླའི་འདི་ལྟ་བུའི་མི་འཕྲོད་པ་ཟ་བར་བྱེད་པ་ནི་དེ་ལྟ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 2580]
ཉེས་པ་ཡོད་པ་ལ་ཕམ་པར་འགྲོ་བ་ལས་གཞན་བསྐྱེད་པའོ། །

[Block 2581]
ཉེས་པ་མེད་པ་ཡོད་པ་ཉིད་ལ་བཏགས་པ་འདི་ཡིན་ནོ། །

[Block 2582]
མི་ཤེས་པ་ལས༌[^1748]འཆི་བའི་དགྲ་བོ་མ་སྨྲས་པར་དེའི་ནད་གཡོག་ཏུ་མི་གཞག་གོ་ཞེས་བྱ་བ་ནི་འདི་ལ་ཁྱོད་ཀྱི་དགྲ་བོས་འཆི་བའི་ཕྱིར་རྗེས་སུ་སྒྲུབ་པ༌[^1749]པོས་འཆི་བ༌[^1750]རྗེས་སུ་དབྱུང་བར་བྱའོ། །

[Block 2583]
དེ་ལྟར་བསྒོ་བར་མ་བྱས་པར་ནད་པ་ལ་ནད་གཡོག་མི་ཤེས་པ་ཉེ་བར་གཞག་པར་མི་བྱའོ། །

[Block 2584]
གནས་ཡོད་ན་མི་གཞག་གོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་མི་ཤེས་པ་དེ་མེད་པར་ཡོངས་སུ་འཇུག་ན་འདི་ནི་གཞག་པར་བྱ་བ་མ་ཡིན་པ་ཁོ་ནའོ། །

[Block 2585]
དེའི་ངོ་བོ་ཡིད་ཆེས་པ་ལ༌[^1751]དེའི་ཚིག་གོ། །

[Block 2586]
སླར་དགེ་སློང་གི་ནད་པ་ལ་མི་ཤེས་པའི་ནད་གཡོག་ཉེ་བར་གཞག་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2587]
གལ་ཏེ་དེའི་ངོ་བོ་ཡིད་ཆེས་པར་གྱུར༌[^1752]ན་སྦས་ནས་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་བསྟན་པ་འདིར་སྦ་བའོ། །

[Block 2588]
འཆི་བའི་འཚོག་ཆས་མི་གཞག་གོ་ཞེས་བྱ་བ་ནི་ནད་པ་ལ་ཞེས་སྦྱར་བར་བྱའོ། །

[Block 2589]
དེ་ཡང་མཚོན་ལ་སོགས་པའོ། །

[Block 2590]
དེ་འཆི་བའི་ཕྱིར་རྗེས་སུ་བསྒྲུབ་པ་ལས་ནད་གཡོག་གིས་བཟློག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་ནད་པའོ། །

[Block 2591]
རྫས་ཀྱི་ཕྱིར་གཞན་འཆི་བར་འདོད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལྷུང་བཟེད་དང་། ཆོས་གོས་ལ་སོགས་པའི་རྫས་ཐོབ་པར་བྱ་བའི་དོན་དུའོ། །

[Block 2592]
བྱ་བ་མ་ཡིན་པ་བྱེད་པ་ལ་སེམས་ཀྱིས་རྗེས་སུ་ཡི་རང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། བྱ་བ་མ་ཡིན་པ་ཉིད་བྱེད་པ་ནི་བྱ་བ་མ་ཡིན་པ་ཉིད་བྱེད་པའོ། །

[Block 2593]
རང་ངམ་གཞན་གྱིས་འདས་པའམ་མ་འོངས་པའམ།[^1753] ད་ལྟར་བྱུང་བ་ལ་དེའི་རྗེས་སུ་ཡི་རང་བར༌[^1754]སེམས་ཀྱིས་མ་བྱས་པ་ཉིད་དམ་ལུས་ཀྱི་བྱ་བས་ཀྱང་མ་ཡིན་ཞེས་བྱ་བ་སྟེ། འདི་དག་ལ་སེམས་སྔོན་དུ་འགྲོ་བ་ཉིད་ཀྱི་ཕྱིར་གྲུབ་པ་དམན་པའི་དེ་ཉིད་བརྗོད་པ་ལ་གཞན་དུ་གཏམ་གང་ཡང་མེད་དོ་ཞེས་བྱ་བ་རྟོགས་པའི་ཕྱིར་རོ། །

[Block 2594]
གཞུང་ཁ་ཅིག་ལས་ཚེ་དང་ལྡན་པ་ཉེ་སྡེའི་དབང་དུ་མཛད་ནས་གསུངས་པ། ཉེ་སྡེ་ཁྱོད་ཀྱིས་མངལ་ན་གནས་པ་རླུགས་པར་བྱས་པ་བདེན་ནམ། བཙུན་པ་མ་ལགས་ཏེ་འདི་ལྟར་བདག་གིས་རྗེས་སུ་ཡི་རང་བར་ནི་བགྱིས་སོ། །

[Block 2595]
བཀའ་སྩལ་པ། དགེ་སློང་དག་དགེ་སློང་ཉེ་སྡེ་ལ་ལྟུང་བ་མེད་དེ་སླར་དགེ་སློང་གིས༌[^1755]མངལ་ན་གནས་པ་རླུགས་པར་མི་བྱའོ། །
--- END BLOCKS ---
