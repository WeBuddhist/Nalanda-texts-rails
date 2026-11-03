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
[Block 2661]
འདིར་ཚེགས་ཆུང་ངུས་ཞེས་བྱ་བ་ནི་ཆོས་གོས་ཀྱི་རིན་ཆུང་བ་མ་ཡིན་པ་བཀུར་བ༌[^1720]ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུ་རིགས་པ་ལས་མི་འདའ་བར་རིག་པར་བྱའོ། །

[Block 2662]
གཞན་དུ་ན་གལ་ཏེ་ཚེགས་དང་བཅས་ཤིང་རང་གི༌[^1721]དོན་དང་བཅས་པ་ཉིད་དུ་ལེན་ན་ནི་དགེ་འདུན་གྱི་ལྷག་མའོ། །

[Block 2663]
གཞན་གྱི་དོན་ཉིད་ཙམ་དུ་ཟད་ཀྱི་མངོན་པར་མི་འདོད་པ་ཉིད་ལ་རང་གི་ཆ་དང་འབྲེལ་པའི་བསམ་པ་མེད་པ་ཉིད་ལ་ནི་སྦོམ་པོར་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2664]
ཤི་བའི་ནོར་ལེན་པའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 2665]
གང་ལ་བཟོད་པ་གསོལ་དུ་འཇུག་པའི་དགེ་འདུན་གྱི་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་བཟོད་པ་གསོལ་དུ་འཇུག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བསྡིགས་པ་ལ་སོགས་པའི་ཆད་པའི་ལས་ལ་རྣམ་པར་གཞག་པའི་དགེ་སློང་མ་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་བཟོད་པ༌[^1722]གསོལ་དུ་འཇུག་ནའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2666]
འདིར་མཚམས་ཀྱི་ནང་དུ་བཟོད་པར་གསོལ་དུ་འཇུག་པ་ལ་ནི་སྡིག༌[^1723]ཤིན་ཏུ་ཆེ་བར་སྣང་སྟེ། དེ་བས་ན་དགེ་འདུན་ནམ་ཆད་པའི་ལས་བྱེད་པ་པོ་རྣམས་མེད་པ༌[^1724]ན་དེ་ལ་འདི་གཙོ་བོ༌[^1725]ཆེ་བ་ཡིན་ནོ། །

[Block 2667]
འདི་ལྟར་དེ་ནི་དབྱེན་གྱི་རྣམ་པར་ཚོགས་པ་མི་འཇིག་པར་འགྱུར་བའོ། །

[Block 2668]
བུད་མེད་རྣམས་ཀྱི་བསྒྲུབ་པ་ལ་ནི་སྟོབས་དང་ལྡན་པ་སྟེ། དེ་བཞིན་དུ་མཐུན་པ་འབྱེད་པར་འགྱུར་བ་ནི་ཤིན་ཏུ་ཡང་སྨད་པར་བྱ་བས་ན། འདི་རྣམས་ཤིན་ཏུ་སྤྱི་བརྟོལ་ཆེ་བ་ཡིན་པས། དེའི་ཕྱིར་ཁ་ན་མ་ཐོ་བར་འགྱུར་བའོ། །

[Block 2669]
ཡང་དགེ་སློང་མ་གང་ཞིག་དགེ་སློང་མ༌[^1726]གང་ལ་དགེ་སློང་མའི་དགེ་འདུན་མཐུན་པས་གནས་ནས་དབྱུང་བར་བྱ་བའི་ལས་བྱས་པར་ཤེས་བཞིན་དུ་དེ་མཚམས་ཀྱི་ཕྱི་རོལ་དུ་ཁྲིད་དེ་བཟོད་པར་བྱེད་ན། དགེ་འདུན་ལྷག་མའི་ལྟུང་བར་འགྱུར་རོ། །

[Block 2670]
དེའི་ཕྱིར་འདིར་གནས་ནས་དབྱུང་བའི་ལས་ཞེས་སྨོས་པ་ནི་ཆད་པའི་ལས་དག་གི་དཔེ་ཙམ་དུ་ཟད་དོ། །

[Block 2671]
དེ་བས་ན་དེ་ཉིད་སྐྱེད་པའི༌[^1727]དབང་གིས་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 2672]
གཞན་དུ་ན་ཆད་པའི་ལས་བྱས་པར༌[^1728]འཇུག་པ་འདི་ཉམས་པ༌[^1729]ཉིད་ཀྱི་ཕྱིར་འདིར་གནས་ནས་དབྱུང་བར་བྱ་བའི་ལས་བྱེ་བྲག་ཏུ་མ་སྨོས་སོ། །

[Block 2673]
བཟོད་པ་གསོལ་དུ་འཇུག་པའི་དགེ་འདུན་ལྷག་མའོ། །གང་ལ་སྤོང་བའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དཀོན་མཆོག་གཏོང་ངོ་། །འདི་དང་མཚུངས་པ་ཉིད་ཀྱི་དགེ་སློང༌[^1730]གཞན་དག་ཀྱང་ཡོད་ཀྱི།[^1731] དེ་དག་ལ་ཚངས་པར་སྤྱད་པ་ཉིད༌[^1732]སྤྱོད་དོ་ཞེས་བྱ་བའི་ཚིག་དེ་ལ་ཞུགས་པ་མི་གཏོང་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དཀོན་མཆོག་གཏོང་ངོ་ཞེས་བྱ་བ་ནི་གཞན་མུ་སྟེགས་ཅན་ལས་རབ་ཏུ་བྱུང་བའི་དགེ་སློང་མ་ནག་མོ་ཞེས་བྱ་བ་དགེ་སློང་མ་རྣམས་དང་ལྷན་ཅིག་འཐབ་ཀྲོལ་བྱེད་ཅིང་སངས་རྒྱས་གཏོང་ངོ་། །ཆོས་གཏོང་ངོ་། །དགེ་འདུན་གཏོང་ངོ་ཞེས་ཟེར་བ་དེ་ཉིད་ཡིན་ནོ། །

[Block 2674]
དེ་བས་ན་འདི་དང་མཚུངས་པ་ཉིད་ཀྱིས་ཞེས་སྨོས་པ་ཡིན་ནོ། །

[Block 2675]
དགེ་སྦྱོང་གཞན་དག་ཀྱང་ཡོད་ཀྱི༌[^1733]ཞེས་བྱ་བ་ནི་ཤཱཀྱའི་བུའི་དགེ་སྦྱོང་དག་ཉིད། ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཡོན་ཏན་དང་ལྡན་པ་དེས་པ། དགེ་བའི་ཆོས་ཅན་མ་ཡིན་གྱི། དགེ་སྦྱོང་དང་། བྲམ་ཟེ་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ཡོན་ཏན་དང་ལྡན་པ་དེས་པ། དགེ་བའི་ཆོས་ཅན་གཞན་དག་ཀྱང་ཡོད་ཀྱི༌[^1734]ཞེས་ཟེར་བ་ཡིན་ནོ། །

[Block 2676]
དེ་དག་ལ་ཚངས་པར་སྤྱད་པ་ཉིད་སྤྱོད་དོ་ཞེས་བྱ་བ་ལ་དེ་དག་ལ་ཞེས་བྱ་བ་ནི་དགེ་སྦྱོང་དང་བྲམ་ཟེ་གཞན་དེ་དག་ལའོ། །

[Block 2677]
ཚངས་པར་སྤྱད་པའི་དངོས་པོ་ཉིད་ཚངས་པར་སྤྱད་པ་ཉིད་སྤྱད་པ་སྟེ། དེ་དག་གི་དྲུང་དུ་ཚངས་པར་སྤྱད་པ་ཉིད་སྤྱད༌[^1735]དོ་ཞེས་ཟེར་བ་དེ་བསྡུ་བའོ། །

[Block 2678]
གང་ཡང་རུང་བ་སྨོས་པ་ལ་དེ་དག་ཐམས་ཅད་སྨོས་པར་འགྱུར་ཞེས་བྱ་བ་ཕྱོགས་གཅིག་ཏུ་སྨོས་པ༌[^1736]འདི་ལ་ཡང་དངོས་གཞིའི་ལྟུང་བ་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 2679]
ཚིག་དེ་ལ་ཞུགས་པ་གང་ཡིན་པ་དེ་ནི༌[^1737]མི་གཏོང་བ་ལ་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་རོ། །ཇི་ལྟར་མི་གཏོང་ཞེ་ན། དེའི་ཕྱིར་དགེ་འདུན་གྱི་དབྱེན་ལ་ཞུགས་པ་ལྟར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཇི་ལྟར་དེ་ལ་སྦྱོར་བའི་ལྟུང་བ་རྣམས་དངོས་གཞིར་འགྱུར་བ་ལྟར་འདི་ལ༌[^1738]ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་འདའ་བར་བྱེད་པ་ཉིད་ཀྱིས་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 2680]
འོག་མ་དག་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འདི་ནས་བརྩམས་ཏེ། འོག་མའི་འཇུག་པ་རྣམས་ལས་དགེ་འདུན་གྱི་དབྱེན་ལ་ཞུགས་པ་ལྟར་མི་གཏོང་བ་ལ་དགེ་འདུན་གྱི་ལྷག་མར་འགྱུར་རོ། །

[Block 2681]
སྤོང་བའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 2682]
གང་ལ་འཐབ་ཀྲོལ་བྱེད་པའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མ་རྣམས་ལ་འདུན་པ་ལ་སོགས་པས་འགྲོ་བ་ཉིད་དུ་རྗེས་སུ་སྦྱོར་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མི་གཏོང་བ་ལའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྔར་བསྟན་པའོ། །

[Block 2683]
སོགས་པའི་སྒྲས་ནི་ཞེ་སྡང་དང་གཏི་མུག་དང་འཇིགས་པས་འགྲོ་བ་ཞེས་བྱ་བ་དག་ཀྱང་བསྡུས་པ་སྟེ། དེ་དག་གིས་ཁྱིམ་སུན་འབྱིན་པའི་དགེ་འདུན་ལྷག་མའི་རྗེས་སུ་འབྲངས་པས་ཤེས་པར་བྱའོ། །

[Block 2684]
ཤིན་ཏུ་ངོ་ཚ་བ་དང་བྲལ་བར༌[^1739]གྱུར་པའི་བུད་མེད་ཀྱི་ཚོགས་ཀྱི་མདུན་དུ་འདིར་འདི་རྒུད་པ་ཆེན་པོ་ཡིན་ཏེ། ཁྱད་པར་གྱི་མཐར་ཐུག་པའོ། །

[Block 2685]
འདི་ལས་ལྡོག་པ་དང་མི་འདོད་པ་དང་ཉེ་བར་ཕྲད་པས། ཉེ་བར་གནས་པ་གང་ཡིན་པ་དེ་ལ་དགེ་འདུན་སྨྲ་བར་བྱེད་པའི་མི་གཏོང་བ་དེ་བས་འདི་ཁ་ན་མ་ཐོ་བའོ། །

[Block 2686]
དོན་གང་ལ་འདུན་པ་ལ་སོགས་པས་འགྲོ་བ་ཉིད་ལ་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མ་རྣམས་དང་ལྷན་ཅིག་འཐབ་ཀྲོལ་དང་འཚང༌[^1740]འབྲུ་བ་དང་། རྩོད་པ་དང་འགྱེད་པ་བཟློག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འཐབ་ཀྲོལ་ཞེས་བྱ་བ་ནི་རྩུབ་མོ་སྨྲ་བ་དང་ཕྱིར་སྨྲ་བའོ། །

[Block 2687]
མཚང་འབྲུ་བ་ཞེས་བྱ་བ་ནི་རྩུབ་ཀྱང༌[^1741]རུང་འཇམ་པོ་ཡང་རུང་བའི་ཚིག་གི་བྱ་བས་ཅོ་འདྲི་བའོ། །

[Block 2688]
རྩོད་པ་ཞེས་བྱ་བ་ནི་ཁོན་དུ་འཛིན་ཅིང་གནས་པའོ། །

[Block 2689]
འགྱེད་པ་ཞེས་བྱ་བ་ནི་ཤགས་འགྱེད་པའོ། །

[Block 2690]
གང་དང་ལྷན་ཅིག་འཐབ་ཀྲོལ་ལ་སོགས་པ་བྱེད་པ་ལ་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མ་རྣམས་དང་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་དགེ་སློང་དང་ལྷན་ཅིག་ལྕི་བའི་ཆོས་ཀྱི་ཁ་ན་མ་ཐོ་བར་རིག་པར་བྱའོ། །

[Block 2691]
གང་ཟག་གཞན་དང་ལྷན་ཅིག་ཏུ་འཐབ་རྩོད་ལ་སོགས་པ་བྱེད་པ་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 2692]
འཐབ་ཀྲོལ་བྱེད་པའི་དགེ་འདུན་ལྷག་མའོ། །

[Block 2693]
གང་ལ་བུད་མེད་དང་བསྟེན་པའི་དགེ་འདུན་ལྷག་མར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྡེ་ཞིང་གནས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མི་གཏོང་བ་ལའོ་ཞེས་བྱ་བ་དང་། དགེ་འདུན་གྱི་དབྱེན་ལ་ཞུགས་པ་ལྟར་རོ་ཞེས་བྱ་བའི་རྗེས་སུ་སྦྱར་རོ། །

[Block 2694]
སུ་དང་སྡེ་ཞིང་གནས་པ་ལ་ཞེ་ན། དེའི་ཕྱིར་དགེ་སློང་མ་དང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྷན་ཅིག་ཅེས་བྱ་བ་བདག་ཏུ་བྱ་བས་རྟོགས་པར༌[^1742]བྱའོ། །

[Block 2695]
གླེང་གཞིའི་དབང་གིས་དགེ་སློང་མ་དང་ཞེས་གསུངས་པར་ཟད་ཀྱི༌[^1743]ཁྱིམ་པ་མོ་དང་མུ་སྟེགས་ཅན་མོ་དང་དགེ་ཚུལ་མ་དང་དགེ་སློབ༌[^1744]མ་དང་ལྷན་ཅིག་སྡེ་ཞིང་གནས་པ་ནི་ཤིན་ཏུ་སྡིག་ཆེ་བའི་ཕྱིར་སྨོས་པ་ཡིན་ནོ། །

[Block 2696]
ཁྱིམ་པ་མོ་དང་མུ་སྟེགས་ཅན་མོ་དག་ལ་འདིར་སྡུག་བསྔལ་བ་དོན་འདིར༌[^1745]དགེ་སློང་མ་སྡེ་ཞིང་གནས་པ་ཞེས་བྱ་བ་འབྱུང་བར་དགའ་བ་ཉིད་ཀྱི་ཕྱིར་ཡང་མི་བསྟན༌[^1746]པའོ། །

[Block 2697]
སྐྱེས་པ་དང་ལྷན་ཅིག་སྡེ་ཞིང་གནས་པ་ལ་ཕམ་པའི་སྦྱོར་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2698]
རྣམ་པ་ཇི་ལྟར༌[^1747]སྡེ་ཞིང་གནས་པ་ལ་ཞེ་ན། དེའི་ཕྱིར་གཞོགས་སྟེགས་དང་འཕྱར་གཡེང་དང་རྩབ་ཧྲལ་གྱི་རྒྱུར་འགྱུར་བ་དག་གིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞོགས་སྟེགས་ལ་སོགས་པ་རྣམས་ཀྱི༌[^1748]དོན་ཐོ་འཚམས༌[^1749]པ་དང་ཀུན་དུ་རྩེ་བ་དང་། ཀུན་དུ་ཅ་ཅོ་འདོན་པ་རྣམ་གྲངས་ཇི་ལྟ་བ་བཞིན་དུ་དོན་བརྗོད་པའོ། །

[Block 2699]
ཆགས༌[^1750]དང་བཅས་པ་ཐམས་ཅད་ལ་འདུ་འཛིའི་སྐྱོན་ལ་འདིས་བསྡུས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 2700]
མཚན་ཉིད་ཇི་ལྟ་བར་ཡང་འདིར་ལྟུང་བ་གཞན་རྣམས་སྐྱེས་པའོ། །
--- END BLOCKS ---
