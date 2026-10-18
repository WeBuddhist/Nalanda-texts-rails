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
[Block 2591]
དེ་ལ་དེ་བཞིན་གཤེགས་པའི་བསྲུང་བ༌[^1828]མེད་པ་གསུམ་གང་ཞེ་ན་ཞེས་བྱ་བ་ལ་སྲུང་བ༌[^1829]མེད་པ་གསུམ་ནི་གཞུང་ཉིད་ལས་གོ་སླའོ། །

[Block 2592 [HEADING]]
###### དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ། ^1-2-7-55-6-0

[Block 2593]
རྗེས་སུ་ཆགས་པ་དང་། ཁོང་ཁྲོ་བ་མེད་པས་དྲན་པ་ཉེ་བར་གཞག་པ་གསུམ་ནི་གོ་སླའོ། །

[Block 2594 [HEADING]]
###### བསྙེལ་བ་མི་མངའ་བའི་ཆོས་ཉིད། ^1-2-7-55-7-0

[Block 2595]
བསྙེལ་བ་མི་མངའ་བའི་ཆོས་ཉིད་ཅེས་བྱ་བ་ནི་གང་དང་གང་གི་ཚེ་ཇི་ལྟར་སེམས་ཅན་གྱི་དོན་མཛད༌[^1830]པ་དེའི་ཚེ། དེ་བཞིན་གཤེགས་པ་དེ་བཞིན་དུ་སྒྲུབ་པ༌[^1831]ནི་བསྙེལ་བ་མི་མངའ་བའི་ཆོས་ཉིད་དོ། །

[Block 2596 [HEADING]]
###### སྐྱེས་བུ་ཆེན་པོའི་མཚན་སུམ་ཅུ་རྩ་གཉིས། ^1-2-7-55-8-0

[Block 2597]
སྐྱེས་བུ་ཆེན་པོའི་མཚན་སུམ་ཅུ་རྩ་གཉིས་ཞེས་བྱ་བ་ནི་གཟུགས་ཚད་མར་འཛིན་པའི་གང་ཟག་རྣམས་དད་པ་བསྐྱེད་པའི་ཕྱིར་རྣམ་པར་དགོད་དོ། །

[Block 2598]
དེ་ལ་རིགས༌[^1832]དང་བསམ་པ་དང་། མོས་པ་དང་། སྨོན་ལམ་དང་། བརྩོན་འགྲུས་རྩོམ་པ་དང་། འཇུག་པ་དང་། ཡང་དག་པར་འགྲུབ་པ་དང་། ཤེས་རབ་དང་། ཐབས་ལ་སོགས་པ་ཆེ་བས་སྐྱེས་བུའི་བྱེད་པ་ཆེ་བའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་རྣམས་དང་། སངས་རྒྱས་རྣམས་ལ་སྐྱེས་བུ་ཆེན་པོ་ཞེས་བྱ་སྟེ། དེ་དག་སྐྱེས་བུ་ཆེན་པོ་ཡིན་པས༌[^1833]འདི་དག་གིས་བརྗོད༌[^1834]ཅིང་མངོན་པར་བསལ་བར༌[^1835]བྱེད་པའི་ཕྱིར་སྐྱེས་བུའི༌[^1836]ཆེན་པོའི་མཚན་རྣམས་སོ། །

[Block 2599]
འོ་ན་དེ་དག་གིས༌[^1837]ཡན་ལག་དང་། ཉིང་ལག་རྣམས་ལ་སྐྱེས་བུ་ཆེན་པོར་མངོན་པར་བྱེད་པ༌[^1838]གང་ལ་ཡང་བྱེ་བྲག་མེད་པའི་ཕྱིར། འདི་སྙེད་ཅིག་གོ་ཞེས་བྱ་བར་མི་རུང་བས་སུམ་ཅུ་རྩ་གཉིས་ཞེས་བྱ་བའི་གྲངས་དོན་མེད༌[^1839]པར་འགྱུར་རོ་ཞེ་ན། དེ་ཡང་བདེན་མོད་ཀྱི་འོན་ཀྱང་ཐོས་པ་དང་། དྲན་པ་དག་ལས་དེའི་རྗེས་སུ་འབྲང་བའི་དོན༌[^1840]དེ་ལྟ་བུའི་གྲངས་ངེས་པར༌[^1841]བསྟན་ཏེ། འདིར་ཡང་གྲངས་འདི་ཉིད་ཀྱིས་བསྟན་ཏོ། །

[Block 2600]
མཚན་འདི་རྣམས་ཀྱང་མདོར་བསྟན་པ་དང་། བཤད་པ་དང་། རྒྱུ་དང་། འབྲས་བུ་དང་། རྣམ་པ་བཞིས་བསྟན་ཏེ།

[Block 2601]
དང་པོ་ནི་མདོར་བསྟན་པའོ། །

[Block 2602]
དེའི་འོག་ཏུ་མཚན་དེ་རྣམས་འགྲེལ་པ་ནི་བཤད་པའོ། །

[Block 2603]
སྔོན་གྱི་ལས་སྨོས་པ༌[^1842]ནི་རྒྱུའོ། །

[Block 2604]
སྔ་ལྟས་སྨོས་པ་ནི་འབྲས་བུའོ། །

[Block 2605]
ཕྱག་དང་ཞབས་འཁོར་ལོའི་མཚན་དང་ལྡན་པ་ཞེས་བྱ་བ་ལ་འཁོར་ལོ་ནི་འཇིག་རྟེན་ན་རྣམ་པ་གཉིས་ཏེ། མཚོན་ཆའི་འཁོར་ལོ་དང་། འགྲོ་བ་འཇུག་པའི་འཁོར་ལོ་ཤིང་རྟ་ལ་སོགས་པའི་འཕང་ལོ༌[^1843]ལྟ་བུའོ། །

[Block 2606]
དེ་ཡང་ཕྱག་དང་ཞབས་གཉིས་ཀ་ལ་འབྱུང་ངོ་། །འདིའི་སྔོན་གྱི་ལས་ཀྱང༌[^1844]རྣམ་པ་གཉིས་ཏེ། བླ་མ་ལ༌[^1845]སྐྱེལ་ཞིང་བསུ་བའི་གྲངས་སུ་གཏོགས་པ་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པས་བསྡུས་པ་ནི་གཅིག་སྟེ། དེའི་འབྲས་བུས་འགྲོ་བར་འཇུག་པའི་འཁོར་ལོ་ཞབས་ཀྱི་མཐིལ་དུ་འབྱུང་ངོ་། །ཆོས་ཉན་པ་དང་། ཕྲེང་བ་རྒྱུད་པ༌[^1846]དང་། གཙུག་ལག་ཁང་དང་། མཆོད་རྟེན་གྱི་གན་དུ་འགྲོ་བ་དང་། གཡོག་བྱིན་པ་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པས་བསྡུས་པ་དེའི་འབྲས་བུས་ཕྱག་གི་མཐིལ་གཉིས་སུ༌[^1847]འབྱུང་ངོ་། །འཁོར་ལོ་རྩིབས་སྟོང་དང་ལྡན་པ་མུ་ཁྱུད་ཅན་ལྟེ་བ་དང་བཅས་པ་ཞེས་བྱ་བ་གང་གི༌[^1848]ཚེ་འདི་གསུམ་ཡོངས་སུ་མ་རྫོགས་པ་དེའི་ཚེ་ནི་མཚན་དེ་དག་གིས་འཁོར་ལོས་སྒྱུར་བར༌[^1849]གྱུར་ནས་རབ་ཏུ་འབྱུང་བར་འགྱུར་རོ། །

[Block 2607]
དེའི་ཚེ་ནི་མངོན་པར་རྫོགས་པར་འཚང་མི་རྒྱ་སྟེ། དཔེར་ན་རྒྱལ་པོ་ཤང་ཀ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 2608]
གང་གི་ཚེ་དེ་དག་ཐམས་ཅད་རྣམ་པ་ཐམས་ཅད་དུ་ཡོངས་སུ་རྫོགས་པར་གྱུར་པ་དེའི་ཚེ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་སྟེ། དེ་བས་ན་རྣམ་པ་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པ་དེ་ན་ཞེས་གསུངས་སོ། །

[Block 2609]
དེ་ལ་མདོ་སྡེ་གཞན་དག་ལས་མཚན་གཞན་དང་གཞན་དཔལ་བེའུ་དང་། བཀྲ་ཤིས་དང་། སྡོང་རིས་དང་། བུམ་པ་གང་བ་དང་ཉ་སྦྲེལ་བ༌[^1850]དང་རྒྱལ་མཚན༌[^1851]དང་། དུང་དང་། ཁྲི་བཟང་པོ་དང་། གདུགས་དཀར་པོ་དང་། རྔ་ཡབ་ལ་སོགས་པ་དག་ཀྱང་མ་བསྟན་ཏམ་ཞེ་ན། [^1852]དེ་ཡང་བདེན་མོད་ཀྱི་གཙོ་བོར་གྱུར་པ་འཁོར་ལོའི་མཚན་དང་ལྡན་པ་བསྟན་ན་དེ་དག་ཀྱང་བསྟན་པར་འགྱུར་རོ། །

[Block 2610]
དེ་བཞིན་གཤེགས་པའི་ཞབས་གཉིས་ལ་མི་སྣང་བའི་མཚན་བཟང་པོ་ཐམས་ཅད་མེད་པ་ཡང་མ་ཡིན་གྱི། མཚན་གྱིས་འཁོར་ལོ༌[^1853]དེ་དག་ཉིད་བསྡུ་བའི་ཕྱིར། རྣམ་པ་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པའོ་ཞེས་བྱ་བར་བསྟན་ཏོ་ཞེས་ཁ་ཅིག་སྨྲའོ། །

[Block 2611]
དེ་ནི་གཡོག་འཁོར་ཤིན་ཏུ་མང་བའི་སྔ་ལྟས་སོ་ཞེས་བྱ་བ་ནི་འཁོར་ལོས་སྒྱུར་བ༌[^1854]དང་། སངས་རྒྱས་རྣམས་ཐུན་མོང་སྟེ། འཁོར་ལོ་ནི་མུ་ཁྱུད་ནས་བཟུང༌[^1855]སྟེ་རྩིབས་དང་ལྡན་པའི་དབང་གིས་གཡོག་འཁོར་ཤིན་ཏུ་མང་བ་དང་མཐུན་ནོ། །

[Block 2612]
ཞབས་ཤིན་ཏུ་གནས་པ་ཞེས་བྱ་བ་ནི༌[^1856]འདི་ལྟར་གཞན་དག་ནི་ས་མི་མཉམ་པའམ། རྐང་པའི་མཐིལ་མི་མཉམ་པ་དང་། འདོད་ཆགས་ལ་སོགས་པ་སྤྱོད་པའི་དབང་ངམ། རྐང་པའི་རྩེ་མོའམ། རྐང་པའི་ཟུར་གཉིས་སམ། རྟིང་པས་ས་ལ་འཛུགས་ཤིང་འགྲོ། །མཆོང་ཞིང་འགྲོ་ལ་དབུས་སུ་ཡང་སྐབས་འབྱུང་བར་འགྱུར་གྱི། སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། ཞབས་ཀྱི་མཐིལ་ཐམས་ཅད་མཉམ་པར་ས་ལ་འབབ་པར་གཤེགས་པ་དང་མཉམ་པར་ས་ལ་རེག་པ་ལ་ཞབས་ཤིན་ཏུ་གནས་པ་ཞེས་བྱ་སྟེ། ས་ཆེན་པོ་ཐམས་ཅད་ཀྱང་མཐོན་དམན་དང་། གསེག་མ་དང་། རྡོ་བ་དང་། ཆུ་དང་། འདམ་རྫབ་དང་། ཚེར་མ་དང་། ཁུང་ལ་སོགས་པ་མེད་པར་མཉམ་པས༌[^1857]གནས་ཤིང་། འཇིག་རྟེན་གྱི་ཁམས་བརྒྱ་སྟོང་དུ་མའི་དབང་གིས། ཐག་རིང་བ་དག་ཀྱང་ཉེ་བར་འགྱུར་རོ། །

[Block 2613]
སྔོན་གྱི་ལས་བསྟན་པ་ལ། ཡི་དམ་ལ་བརྟན་པས་ཞེས་བྱ་བ་ནི་བདེན་པ་དང་། གཏོང་བ་དང་། ཉེ་བར་ཞི་བ་དང་། ཤེས་རབ་ཀྱི༌[^1858]བྱིན་གྱི་རླབས༌[^1859]ཀྱི་དབང་གིས། རྩོམ་པ་ཐམས་ཅད་ལ་སུས་ཀྱང་མི་འཕྲོགས་པའི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 2614]
དེ་ནི་མི་གཡོ་བའི་སྔ་ལྟས་སོ་ཞེས་བྱ་བ་ནི་བདུད་དང་། ཕྱིར་རྒོལ་བ་དང་། མུ་སྟེགས་ཅན་ལ་སོགས་པ་ཐམས་ཅད་ཀྱིས་མི་གཡོས་པའོ། །

[Block 2615]
ཕྱག་དང་ཞབས་དྲ་བས་འབྲེལ་བ་ཞེས་བྱ་བ་ནི་ཕྱག་གི་སོར་མོའི་ཚིགས་དང་པོ་ནས་ཕྱག་སོར་གྱི་བར་ཕྲ༌[^1860]སེང་སེང་པོ་མེད་པ། སོར་གདུབ་ལ་སོགས་པའི་རྒྱན་ཀྱང་གཞུག་ཏུ་རུང་བ་སྟེ། རྣམ་པ་ཐམས་ཅད་དུ་མཛེས་པའི་དྲ་བས་འབྲེལ་བའོ། །

[Block 2616]
སྔོན་གྱི་ལས་དང་། བསྡུ༌[^1861]བའི་དངོས་པོ་བཞི་པོ་དག་ཀུན་དུ་བསྟེན་པས་ཞེས་བྱ་བ་ནི་སྦྱིན་པས་བསྡུ་བ་ལ་སོགས་པའི་དབང་གིས་ནི་ཕྱག་གཉིས་དྲ་བ་ཅན་དུ་གྱུར་ཏོ། །

[Block 2617]
དེ་ལས་གཞན་པ་དོན་སྤྱོད་པ་ལ་སོགས་པའི་དབང་གིས་ནི་ཞབས་གཉིས་དྲ་བ་ཅན་དུ་གྱུར་ཏོ་ཞེས་འཆད་དོ། །

[Block 2618]
ཡང་ན་ཕྱག་གཉིས་ཀྱིས་ནི་སྡུད་པར་འགྱུར་རོ། །

[Block 2619]
བསྡུས་པའི་སེམས་ཅན་རྣམས་ཀྱིས་ཞབས༌[^1862]གཏུགས་པ་ལས་གྱུར་ཏོ། །

[Block 2620]
སོར་མོའི༌[^1863]རྣམ་པ༌[^1864]སེང་སེང་པོ་མེད་པ༌[^1865]ཞེས་བྱ་བར་གཟུང་ངོ་། །ལེགས་པར་སྡུད༌[^1866]ཅིང་འཇམ་པར་གྱུར་པའི་ཕྱིར་འདི་དག་བསྡུ༌[^1867]བའི་དངོས་པོ་དང་མཐུན་ནོ། །

[Block 2621]
མྱུར་དུ་འདུ་བ་ཞེས་བྱ་བ་ནི་འཁོར་བརྒྱད་ཆོས་བཤད་པ་ལ༌[^1868]མྱུར་དུ་འདུའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 2622]
ཁ་ཅིག་ནི་ཕྱག་དང་། ཞབས་དྲ་བས་འབྲེལ་བ་ལ་གཞན་དུ་འཆད་དེ། སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱི་ཕྱག་མཐེ་བོ་གཉིས་མ་གཏོགས་པར། སོར་མོ་ཐམས་ཅད་ཀྱི་རྩེ་མོ་མཉམ་པ་ཡིན་ཏེ། སོར་མོ་དག་ཀྱང་ནས་དང་ནས༌[^1869]སུ་འབྲེལ་བའི་མཚན་ཉིད་ཅན་ལ། མཉམ་པར་གནས་ཏེ། སྐར་ཁུང་གི་དྲ་བ་དང་། ཀ་བའི༌[^1870]རྩེ་མོ་མཉམ་པ་བཞིན་དུ་སོར་མོ་ཐམས་ཅད་ལ། ནས་ཀྱི་མཚན་ཐམས་ཅད་མཉམ་པར་སྣང་ཞིང་། དྲ་བ་བཞིན་དུ་སྣང་བའི་ཕྱིར་ཕྱག་དང་ཞབས་དྲ་བས་འབྲེལ་བ་ཞེས་འཆད་དོ། །

[Block 2623]
སེམས་ཅན་ཕྲ་མོ་དག །དེ་བཞིན་གཤེགས་པའི་ཞབས་གཉིས༌[^1871]ཀྱིས་རེག་ན་ཤིན་ཏུ་བདེ་བར་འགྱུར་ཞིང་། ཤི་འཕོས་ན་ཡང་ལྷའི་རིས༌[^1872]སུ་སྐྱེ་བར་འགྱུར་ཏེ། ཞབས་དྲ་བ་ཅན་གྱི་མཚན་དེ་ལ་མཐུ་དེ་ལྟ་བུ་དག་ཀྱང་ཡོད་དོ་ཞེས་ཟེར་རོ། །

[Block 2624]
ཕྱག་དང་ཞབས་འཇམ་ཤིང་གཞོན་ཤ་ཆགས་པ་ཞེས་བྱ་བ་ལ། འཇམ་པ་ནི་མཉེན་པའོ། །

[Block 2625]
གཞོན་ཤ་ཆགས་པ་ནི་མདོག་ཕུན་སུམ་ཚོགས་པའི་ཕྱིར་རོ། །

[Block 2626]
བདུན་མཐོ་བ་ཞེས་བྱ་བ་ནི་ཕྱག་དང་ཞབས་ཀྱི་བོལ་གཉིས་དང་། དཔུང་མགོ་གཉིས་དང་ལྟག་པ་སྟེ། དེ་དག་ཤས་རྒྱས་པའི་ཕྱིར་རོ། །

[Block 2627]
སྔོན་གྱི་ལས་ནི་བཟའ་བ་དང་། བཏུང་བ་དང་། བལྡགས་པ༌[^1873]དང་། བཅའ་བ་གྱ་ནོམ་པ་རྣམས་ཞེས་བྱ་བ་ནི་གྱ་ནོམ་པ་བྱིན་པས་ཕྱག་དང་། ཞབས་འཇམ་ཞིང་གཞོན་ཤ༌[^1874]ཆགས་པར་འགྱུར་རོ།[^1875] །བཟའ་བའི་དངོས་པོ་མང་དུ་བྱིན་པས་ནི་བདུན་མཐོ་བར་གྱུར་ཏོ། །

[Block 2628]
ཡང་ན་ཞབས་གཉིས་ཀྱིས༌[^1876]གཤེགས་ནས། ཕྱག་གཉིས་ཀྱིས་བྱིན་པའི་ཕྱིར་རོ། །

[Block 2629]
ཡང་ན་ཕྱག་གཉིས་ཀྱིས་བྱིན་ནས་སེམས་ཅན་རྣམས་བདག་གི་ཞབས་ལ་གཞོལ་བར་བྱས་པའི་ཕྱིར་ཕྱག་དང་ཞབས་གཉིས་དེ་ལྟ་བུར་གྱུར༌[^1877]ཏོ། །

[Block 2630]
བདུན་མཐོ་བ་ནི་ཁམས་བདུན་ཚིམ་པར་བྱས་པ་དང་མཐུན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
