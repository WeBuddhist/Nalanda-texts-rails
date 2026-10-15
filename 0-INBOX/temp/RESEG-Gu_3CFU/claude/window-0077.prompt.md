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
[Block 2696]
གྲོགས་ཇི་ལྟ་བུས་ཤེ་ན༌[^1819]དེའི་ཕྱིར་ངལ༌[^1820]སོར་གཞུག་གོ། །

[Block 2697]
སྣོད་སྤྱད་བླང་བར་བླའོ།[^1821] །གལ་ཏེ་ལྷན་ཅིག་ཏུ་གནས་སུ་ཕྱིན་པར་མི་ནུས་ལ་ཟན་དང་སྒོམ་གྱི་དུས་སུ་མ་ཡིན་ན་ལྷུང་བཟེད་བཀྲུ་བ་དང་བྱུག་རིས་གཞག་པ་དང་བྱིན་ལེན་དང་བརྟག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཁྱོད་ལ་གྲོགས་པོ་དང་མཉམ་པར་གནས་སུ་ཕྱིན་པར་མི་ནུས་ལ་ཟན་དང་སྐོམ་གྱི་དུས་སུ་མ་ཡིན་ན་ལྷུང་བཟེད་བཀྲུ་བ་དང་བྱུག་རིས་གཞག་པ་དང་བྱིན་ལེན་དང་བརྟག་པར་བྱའོ། །

[Block 2698]
གལ་ཏེ་དུས་སུ་ན་ཁྱེར་ཏེ་བསུ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཅི་སྟེ་དུས་ལ་ཡང་ཟས་དང་བཏུང་བ་དག་ལ་ཕྱིན་པར་ནུས་པ་མེད་ན་དེའི་ཕྱིར་ཁྱེར་ཏེ་བསུ་བར་བྱས་ཏེ་ཟན་དང་སྐོམ་དེ༌[^1822]བླངས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2699]
འདིར་ལྟུང་བས༌[^1823]ནི་ཕྱི་དྲོ་བཟུང༌[^1824]ངོ་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་གོ་བར་བྱའོ། །

[Block 2700]
ཕམ་པར་འགྱུར་བ༌[^1825]གསུམ་པའི་རྣམ་པར་འབྱེད་པའོ།། །།

[Block 2701]
མིའི་འགྲོ་བ་པའི་ལག་པ་གཅོད་པ༌[^1826]ནི་སྦོམ་པོའོ།[^1827] །ནགས་མེས་གཏོང་ནའོ་ཞེས་བྱ་བ་ནི༌[^1828]དེ་ལས་སྲོག་ཆགས་གསད་པར༌[^1829]མ་བསམས་ཀྱང་སྤྱིར་སྲོག་ཆགས་མང་པོ་ཡོད་པའི་བློས་འདི་ནི་སྦོམ་པོའོ།[^1830] །སྲོག་ཆགས་ཉུང་ངུའི་བློས་ནི་འདི་ཉེས་བྱས་སུ་རྣམ་པར་གཞག་པའོ། །

[Block 2702]
[^1831]མེད་པར་ངེས་པ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 2703]
སྲོག་ཆགས་རྣམས༌[^1832]ལ་མ་ལྟོས་པར་མཉམ་པར་སྤྱོད་པ་ཉིད་ཀྱི་ཕྱིར་འདིར་འདི་རྣམ་པར་ཤེས་པའོ། །

[Block 2704]
སྦྱོར་བ་ཐོབ་པའི་ཕྱིར་འདི་མ་སྨོས་སོ། །

[Block 2705]
འདིར་དངོས་གཞི་རྣམས་ལ་མཚན་ཉིད་ཇི་ལྟ་བར་རྟོགས་པར་བྱ་བ་ཉིད་དེ་གནོད་པ༌[^1833]མེད་པའི་ཕྱིར་སྲོག་གཅོད་པ་ནི་ནགས་ལ་མེས་གཏོང་དུ་འཇུག་པ་ལ་མེད་པ་ལ༌[^1834]ངེས་པ་ཡོད་པར་འགྱུར་བ༌[^1835]ལ་མི་སྐྱེད༌[^1836]དོ། །

[Block 2706]
ཡོད་པའི་བློ་ལ་ཉེས་བྱས་ཙམ་པོར་འགྱུར་བ་ལ་ཡང་ཇི་ཙམ་དུ་ཉེས་བྱས་འདིར་རིགས་སུ་གྱུར་པ་གང་ཡིན་པ་རྣམས་ལ་སྤྱིའམ་བྱེ་བྲག་གཅིག༌[^1837]ཏུ་མ་ཟད་ཀྱི་དེ་རྣམས་ཤི་བ་ལ་དེའི་རིགས་ཡོངས་སུ་རྫོགས་པའི་རྗེས་ལ་ན་སྨད་པར་གྱུར་པའི་ལྟུང་བ་དེ་ཙམ་དག་ལ་སྐྱེད༌[^1838]པའོ། །

[Block 2707]
གལ་ཏེ་མིའི་འགྲོ་བ་པ་རྣམས་ལ་ཉེས་པ་ཡོད་ན་ནི་སྦོམ་པོའོ།[^1839] །ཅི་སྟེ་དུད་འགྲོ་རྣམས་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 2708]
གཞན་དུ་གནོད་པ་ལ་ནི་དེ་ལས་ཀྱང་ན་སྨད་པ་སྟེ་དེ་ཙམ་དག་ལ་མངོན་པར་འབྲེལ་བའི་ཕྱིར་གསོད་པ་དང་སྦ་བ་ལ་འདི་བཅད་ནས་འདིར༌[^1840]ལ་ལ་ཐམས་ཅད་གང་ཡིན་པ་འདི་ནི་རྒུད་པར་གྱུར་ཅིག་ཅེས་བྱ་བས།[^1841] དེ་རྣམས་ཤི་བ་ལ་ཇི་ལྟར་ཇི་ཙམ་དུ་སྲོག་ཆགས་དེ་དང་རྗེས་སུ་མཐུན་པའི་ལྟུང་བ་རྣམས་ཀྱང་དེ་ཙམ་མོ། །

[Block 2709]
རྣམ་པར་གཅད་པ༌[^1842]ལ་རི་དགས་རྣམས་ཉིད་ཤི་བར་གྱུར་ཅིག་ཅེས་བྱ་བས་གལ་ཏེ། དེ་མ་ཡིན་ན་དེར་མི་ལ་སོགས་པ་གཞན་རྣམས་མེད་པའམ་ཡོད་པར་གྱུར་པ་མ་བཟུང་བར་ཤེས་པ་ཉིད་ལ་མངོན་པར་བརྟེན་པའི་རི་དགས་རྣམས་ལ་ཇི་ལྟ་བར་བྱས་པའི་ཁ་ན་མ་ཐོ་བ་དང་མ་ཤེས་པའི་མི་ལ་སོགས་པ་རྣམས་ལ༌[^1843]ནི་མ་ཡིན་ནོ། །

[Block 2710]
གལ་ཏེ་ཤེས་པ་ཉིད་མི་རྣམས་ལ་ཡང་འདིར་དུད་འགྲོ་གཞན་རྣམས་ཡོད་དེ་དེ་ཡང་རི་དགས་རྣམས་ལ༌[^1844]ཇི་ལྟ་བར་བརྗོད་པ་མི་རྣམས་ཤི་བ་ལ་སྦོམ་པོ་དང་གཞན་རྣམས་ལ་ནི་ཉེས་བྱས་སོ། །

[Block 2711]
ཤི་བ་ལས་གཞན་པའི་གནོད་པ་གཉིས་ཀ་ལ་ཉེས་བྱས་ཉིད་དོ། །

[Block 2712]
སྐྲ་ཅན་འཚོང་ནའོ་ཞེས་བྱ་བ་ནི་མིའི་འགྲོ་བ་པ་འཚོང་ན་ནི་སྦོམ་པོའོ། །

[Block 2713]
འདིར་གཞུང་ནི་ཉེ༌[^1845]དགས་ཤ་ཟའི་བུ་གཅིག་བཟུང་སྟེ་བྲོ་གར་མཁན་ལ་བཙོངས་པ་ནས། ཇི་སྲིད་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་གིས་སྐྲ་ཅན་བཙོང་བར་མི་བྱའོ། །

[Block 2714]
བྱེད་ན་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 2715]
གང་གིས་བརྐུས་པ་དེ་བླའི་གྲར༌[^1846]འབུལ་ནའོ་ཞེས་བྱ་བ་ཡང་སྦོམ་པོའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2716]
ཡོངས་སུ་དོར་བར་གྱུར་པ་ནི་བཏང་བ༌[^1847]འདིའོ། །

[Block 2717]
འཚོང་ན་ཞེས་བྱ་བ་འདི་ལ་སྦོམ་པོར་ཤེས་པའོ། །

[Block 2718]
འདི་གཉིས་ཀ་ལ་མངོན་པར་མ་བསམས་པས་གནོད་པ་གཅིག་པུ༌[^1848]འདི་ཉིད་ཁ་ན་མ་ཐོ་བ་མེད་པ་ཉིད་དོ། །

[Block 2719]
མངོན་པར་བསམས་པའི་གནོད་པ་ལ་ནི་དེ་བསྒྲུབ་པར་གྱུར་པ་ལ་གནོད་པ་ཇི་ལྟ་བར་ཁ་ན་མ་ཐོ་བའོ། །

[Block 2720]
ཕྲན་ཚེགས༌[^1849]ཀྱི་སྐབས་སོ།། །།

[Block 2721]
སྟོན་པས་བསྒོ་ནའོ༌[^1850]ཞེས་བྱ་བ་ནི་གསད་པའི་སེམས་ཀྱིས་གང་ཞིག་གསོད་པ་ལ་རང་གི་བསམ་པ་ཉིད་ཀྱིས་བསད་པ་དེའི་དོན་དུ་རྗེས་སུ་འབྲེལ་པས་སྟོན་པ་སུ་ཞིག་ལ་བརྗོད་པ་ནི་སྟོན་པའོ། །

[Block 2722]
གསོད་པར་བྱེད་པ་ལ་གསད་པའི༌[^1851]ཕྱིར་བསྒོ་བ་བྱས་པ་ཡིན་ཏེ། དེ་གསོད་པར་བྱེད་པ་ལ་བསད་དུ་ཟིན་ཀྱང་དེ་བསྟན་པ་དེས་གསད་པར༌[^1852]གྱུར་པས་འདིར་ཕམ་པ་བསྐྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2723]
མ་དང་མངལ་ན་གནས་པ་གཉིས་ནི་དཔེའོ་ཞེས་བྱ་བ་ནི་གསད་པར༌[^1853]བྱ་བ་མང་པོའི་རྗེས་སུ་གསོད་པར༌[^1854]བྱེད་པས༌[^1855]སུ་ཞིག་བགྲང་བ་དེ་རྣམས་ལ་གསད་པར༌[^1856]བྱ་བ་གང་ལ། གསོད་པའི་སེམས་ཉེ་བར་གནས་པར་གྱུར་ལ༌[^1857]དེ་བསྟན་པའི་ཕྱིར་མ་བསམས་པ་གཞན་ཐམས་ཅད་ཀྱང་སྟོན་པར་བྱེད་ཅིང་དེ་ནི་ཞར་ལ་སྦོམ་པོའོ། །

[Block 2724]
དེར་སྦོམ་པོ་དེ་ནི་མ་བསམས་པ་ལ་མ་དང་མངལ་ན་གནས་པ་དག་ལ་དཀུ་མཉེས་པ་ཞེས་བྱ་བ་འདིས་བསྟན་པར་རིག་པར་བྱ་སྟེ། འདིར་མ་དང་མངལ་ན་གནས་པ་གཉིས་ནི་དཔེ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2725]
[^1858]བདག་ཉིད་གསོད་ན་སྦོམ་པོ་ཞེས་བྱ་བ་ནི་གསད་པའི༌[^1859]ཕྱིར་རྗེས་སུ་བསྒྲུབ་པ་ལས་འདིར་ལྟུང་བ་རྣམ་པར་གཞག་པའི༌[^1860]བསད་པ་ལས་ནི་མ་ཡིན་ནོ། །

[Block 2726]
དེ་བས་ན་འདིར་ཚེ་རབས་གཞན་དུ་ལས་ཀྱིས༌[^1861]ལམ་སྐྱེ་བ་མེད་དོ། །

[Block 2727]
སེམས་གྱུར་པ་མེད་པར་ལེགས་པར་བྱས་ནས་ཉེས་བྱེད་དོ་ཞེས་བྱ་བ་ནི་མ་བསམས་པའི་འབྲས་བུ་གང་ཞིག་མ༌[^1862]ལེགས་པར་བྱས་པ་དཔེར་ན་གསད་པར༌[^1863]བྱ་བ་བསྟན་པ༌[^1864]དེ་ནི་ཉེས་བྱེད་དེ་ལེགས་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 2728]
དེ་བས་ན་སེམས་འགྱུར་བ་མེད་པ་ཉིད་ཡོད་ཀྱང་འདི་ནི་ཉེས་བྱས་སུ་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2729]
ཆེད་དུ་མ་བསམས་པར་གྲུབ་པ་ནི་བྱེད་པ་པོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་མ་བསམས་པའི་འབྲས་བུ་གང་ཞིག་ལས་སྐྱེ་བ་དཔེར་ན་བཞད༌[^1865]གད་ཀྱི་བསམ་པས་མཚོན་འཕངས་པས་ཤི་བའི་གསོད་པར་གཏོགས་པ་གྲུབ་པ་དེ་ནི་ལྟུང་བའི་བྱེད་པ་པོ་ཉིད་མ་ཡིན་ཏེ། དེ་ལ་ནི་མཚོན་འཕངས་པ་ལས་དེར་ལྟུང་བ་ཁོ་ན་སྟེ། ཤི་བ་ལས་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 2730]
འདིར་གཞུང་ནི་བཙུན་པ་དགེ་སློང་གིས་བཞད༌[^1866]གད་དུ་གཞན་ལ་མཚོན་འཕངས་པས་རྐྱེན་དེས་དུས་བགྱིས་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 2731]
ཚེ་རབས་གཞན་དུ་ལས་སྐྱེ་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་བསད་པ་ལ་སོགས་པའི་སྦྱོར་བ་བྱས་ནས་ཐོག་མར་ཤི་བར་གྱུར་པའི་སྲོག་ཆགས་པ༌[^1867]ལ་སོགས་པ་མི་བསྐྱེད་དེ་སྦྱར་བ་ཙམ་ཉིད་ལས་དེར་ལྟུང་བའོ། །

[Block 2732]
ཕམ་པར་གྱུར་པ་གསུམ་པའི་ཞུ་བའི་སྐབས་སོ།། །།

[Block 2733]
སྦོམ་པོ་ནི་ཁོ་བོ་འཆི་བར་འོང་ངོ་ཞེས་དེ་སྐད་ཟེར་བ་ལ་ཡིད་མི་ཆེས་ཤིང་དེ་བཞིན་ཉིད་དུ་སྒྲུབ་པར་བྱེད་ནའོ་ཞེས་བྱ་བ་ལ། སྦོམ་པོ་ནི་ཞེས་བྱ་བའི་ཚིག་དང་པོར་སྨོས་པ་ནི་དབང་དུ་བྱ་བ་བསྟན་པའི་ཕྱིར་ཏེ། གལ་ཏེ་ནད་པ་ན་རེ་བདག་ལ་ཁྲུས་དང་བསྐྱོད་པ་ལ་སོགས་པ་ཅུང་ཟད་བྱེད་ན་གདོན་མི་ཟ་བར་ཁོ་བོ་འཆི་བར་འོང་ཞེས་དེ་སྐད་ཟེར་བ་ལ་ཡིད་མ་ཆེས་ཤིང་དེ་གཞན་ཉིད༌[^1868]དུ་ཁྲུས་ལ་སོགས་སྒྲུབ་པར་བྱེད་ན་སྦོམ་པོའོ། །

[Block 2734]
ངེས་པར་འདིར་ལྟུང་བར་འགྱུར་བ་ལ་ཡང་རྩུབ་པས་ཉེ་བར་གནས་པ་ཞེས་བྱ་བ་ལྟུང་བ་འདིའོ། །

[Block 2735]
ནད་པ་ཤི་བླའོ་ཞེས་གཡོག་མི་བྱེད་ནའོ་ཞེས་བྱ་བ་ནི་སྦོམ་པོ་ཞེས་བྱ་བ་དང་སྦྱར་རོ། །
--- END BLOCKS ---
