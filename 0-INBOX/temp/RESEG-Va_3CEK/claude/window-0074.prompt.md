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
ཆོས་ཀྱི་མཆོག་རྣམས་ནི་ཆེན་པོ་ཡིན་ནོ། །

[Block 2592 [HEADING]]
###### ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ཞེས་བྱ་བའི་དོན། ^3-1-3-6-5-0

[Block 2593]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། ངེས་པར་འབྱེད་པས་ན་ངེས་པར་འབྱེད་པ་སྟེ། འཕགས་པའི་ལམ་མོ། །

[Block 2594]
དེས་ཐེ་ཚོམ་སྤོང་བའི་ཕྱིར་དང་། བདེན་པ་རྣམས་ལ་འདི་ནི་སྡུག་བསྔལ་ལོ་ཞེས་བྱ་བ་ནས་འདི་ནི་ལམ་མོ་ཞེས་བྱ་བའི་བར་དུ་རྣམ་པར་འབྱེད་པའི་ཕྱིར་རོ། །

[Block 2595]
དེའི་ཆ་ནི་མཐོང་བའི་ལམ་གྱི་ཕྱོགས་གཅིག་ཡིན་ཏེ། དེ་འདྲེན་པར་བྱེད་པ་ཉིད་ཀྱིས་ཕན་འདོགས་པའི་ཕྱིར་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་སོ། །

[Block 2596]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་ནི་རྣམ་པ་འདི་བཞི་ཆར་ཡང་། བསྒོམས་བྱུང་།[^1801] ཐོས་པ་དང་བསམས་པ་ལས༌[^1802]བྱུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 2597]
མི་ལྕོགས་མེད་པ་དང་། ཁྱད་པར་བསམ་གཏན་ས་པའོ། །

[Block 2598]
འདིའི་ས་པ་ནི་མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་བཞི་ཡིན་ཏེ། དེ་དག་གིས་བསྡུས་པའི་ཕྱིར་རོ། །

[Block 2599]
མཐོང་བའི་ལམ་གྱི་འཁོར་ཡིན་པའི་ཕྱིར་གོང་ན་མེད་དོ། །

[Block 2600]
དེ་མེད་པ་ནི་འདོད་པའི་ཁམས་ལ་དམིགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2601]
དེ་ཡང་སྔར་ཡོངས་སུ་ཤེས་པར་བྱ་ཞིང་སྤང་བར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2602]
དེ་དག་གི་རྣམ་པར་སྨིན་པ་ནི་གཟུགས་ཀྱི་ཁམས་ཀྱི་ཕུང་པོ་ལྔ་ཡིན་ནོ། །

[Block 2603]
ཡོངས་སུ་རྫོགས་པར་བྱེད་པ་དག་ཁོ་ན་ཡིན་གྱི་འཕེན་པར་བྱེད་པ་དག་ནི་མ་ཡིན་ཏེ། སྲིད་པའི་གཉེན་པོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2604]
གཉིས་ནི་འོག་ནའང་ཡོད་པའམ། འམ་ཞེས་བྱ་བའི་སྒྲ་ནི་ལུགས་ཐ་དད་པའི་དོན་ཏེ། བཙུན་པ་དབྱངས་སྒྲོགས་ཀྱི་ལྟར་ན་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་དང་པོ་གཉིས་ས་བདུན་པ་ཡིན་ཏེ། འདོད་པའི་ཁམས་ན་ཡང་ཡོད་དོ། །

[Block 2605]
བཞི་པོ་དེ་དག་ཐམས་ཅད་ཀྱང་། འདོད་རྟེན་གསུམ་ནི་མི་དག་གི་ནང་ཁོ་ན་དང་། གླིང་གསུམ་དུ་སྐྱེད་པར་བྱེད་དོ། །

[Block 2606]
སྔོན་བསྐྱེད་པ་རྣམས་ནི་ལྷ་དག་གི་ནང་དུ་མངོན་སུམ་དུ་བྱེད་དོ། །

[Block 2607]
བཞི་པ་ནི་ལྷ་དག་གི་ནང་དུ་ཡང་སྐྱེད་པར་བྱེད་དོ། །

[Block 2608]
གསུམ་ནི་སྐྱེས་པ་དང་བུད་མེད་ཀྱི་གཉི་གའི་རྟེན་ཅན་དག་འཐོབ་བོ། །

[Block 2609]
ཆོས་མཆོག་བུད་མེད་ཀྱིས་གཉི་གའི་རྟེན་ཅན་འཐོབ་པར༌[^1803]འགྱུར། ཆོས་ཀྱི་མཆོག་ནི་བུད་མེད་ཁོ་ནས་གཉི་གའི་རྟེན་ཅན་འཐོབ་བོ། །

[Block 2610]
[^1804]སྐྱེས་པ༌[^1805]ནི་སྐྱེས་པའི་རྟེན་ཅན་འབའ་ཞིག་འཐོབ་སྟེ། བུད་མེད་ཉིད་ནི་སོ་སོར་བརྟགས་པ༌[^1806]མ་ཡིན་པས་འགོག་པ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 2611 [HEADING]]
###### ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་གཏོང་བ། ^3-1-3-6-6-0

[Block 2612]
ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་ཇི་ལྟར་སྟོང་ཞེ་ན། འཕགས་པས་དེ་དག་ས་བོར་ནས། །སྟོང་ངོ་། ། འཕགས་པ་ནི་ས་གང་དག་ཐོབ་པར་གྱུར་པའི་ས་དེ་དག་འདོར་བ་ན་དེ་དག་ཀྱང་གཏོང༌[^1807]གི་གཞན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 2613]
ས་འདོར་བ་ནི་ས་འཕོས་པའི་ཕྱིར་རོ། །

[Block 2614]
འཕགས་མིན་འཆི་བས་སོ། །

[Block 2615]
སོ་སོའི་སྐྱེ་བོ་ནི་ས་འཕོ་ཡང་རུང་མི་འཕོ་ཡང་རུང་སྟེ་རིས་མཐུན་པ་བཏང་བ་ཁོ་ནས་གཏོང༌[^1808]ངོ་། །

[Block 2616 [VERSE]]
དང་པོ་གཉིས་ཡོངས༌[^1809]ཉམས་པས་ཀྱང་། །
གཏོང༌[^1810]ལ་འཆི་བས་ཀྱང་གཏོང༌[^1811]སྟེ། །

[Block 2617]
སོ་སོའི་སྐྱེ་བོ་ཁོ་ན་ཡིན་གྱི་འཕགས་པ་ནི་དེ་གཉིས་ལས་ཡོངས་སུ་ཉམས་པ་མེད་དོ། །

[Block 2618]
བཟོད་པ་དང་ཆོས་ཀྱི་མཆོག་དག་ལས་ནི་སོ་སོའི་སྐྱེ་བོ་ཡང་ཡོངས་སུ་ཉམས་པ་མེད་དོ། །

[Block 2619]
དངོས་གཞིས་དེ་ཉིད་ལ་བདེན་མཐོང་། །གང་ཞིག་བསམ་གཏན་དངོས་གཞིའི༌[^1812]ས་པའི་ངེས་པར་འབྱེད་པའི་ཆ་དང་མཐུན་པ་རྣམས་སྐྱེད་པར་བྱེད་པ་དེས་ནི་ཚེ་འདི་ཉིད་ལ་གདོན་མི་ཟ་བར་བདེན་པ་རྣམས་མཐོང་བར་འགྱུར་ཏེ།

[Block 2620 [VERSE]]
ཡིད་འབྱུང་བ་ཤས་ཆེ་བའི་ཕྱིར་རོ། །
རྣམ་པར་ཉམས་ན་དངོས༌[^1813]མེད་འཐོབ། །

[Block 2621]
གང་གི་ཚེ་རྣམ་པར་ཉམས་པ་དག་གིས༌[^1814]ཡང་ཐོབ་པ་དེའི་ཚེ་སོ་སོར་ཐར་པའི་སྡོམ་པ་བཞིན་དུ་སྔོན་མེད་པ་དག་ཁོ་ན་འཐོབ་ཀྱི་སྔོན་བཏང་བ་དག་ནི་མ་ཡིན་ཏེ་མ་འདྲིས་པ་དང་འབད་དེ་བསྒྲུབ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2622]
མཚམས་སྟོན་པར་བྱེད་པ་ཞིག༌[^1815]ཡོད་ན་ནི་གོང་མ༌[^1816]སྐྱེད་པར་བྱེད་དོ། །

[Block 2623]
མེད་ན༌[^1817]ནི་གཞི་ཁོ་ནས་སྐྱེད་པར་བྱེད་དོ། །

[Block 2624]
རྣམ་པར་ཉམས་པ་དང་ཡོངས་སུ་ཉམས་པ་འདི་དག་གི་རང་བཞིན་ཅི་ཞེ་ན། ཉམས་པ་གཉིས་ནི་མི་ལྡན་པ། །ཉམས་པ༌[^1818]གཉི་ག་ཡང་མི་ལྡན་པའི་རང་བཞིན་ཡིན་ལ། ཡོངས་སུ་ཉམས་པ་ནི་ཉེས་པས་བྱས་པ་ཡིན་གྱི་རྣམ་པར་ཉམས་པ་ནི་གདོན་མི་ཟ་བ༌[^1819]ཡིན་ནོ། །

[Block 2625]
དྲོ་བར་གྱུར་པ་ཐོབ༌[^1820]པ་ནི་ཡོངས་སུ་ཉམས་ཀྱང་ངེས་པར་མྱ་ངན་ལས་འདས་པའི༌[^1821]ཆོས་ཅན་ཡིན་ནོ། །

[Block 2626]
ཐར་པའི་ཆ་དང་མཐུན་པ་དང་ཁྱད་པར་ཅི་ཡོད་ཅེ་ན། བར་ཆད་བྱེད་པ་མེད་ན་བདེན་པ་མཐོང་བ་ལ་ཆེས་ཉེ་བ་ཉིད་ཡིན་ནོ། །

[Block 2627]
རྩེ་མོ་ཐོབ་པ་རྩ་མི་འཆད། །རྩེ་མོ་ཐོབ་པ་ནི་ཡོངས་སུ་ཉམས་ཀྱང་དགེ་བའི་རྩ་བ་རྣམས་ཀུན་ཏུ་མི་འཆད་ཀྱི་ངན་སོང་དུ་ཡང་འགྲོ་ལ་མཚམས་མེད་པ་དག་ཀྱང་བྱེད་དོ། །

[Block 2628]
བཟོད་ཐོབ་ངན་སོང་མི་འགྲོའོ། །

[Block 2629]
བཟོད་པ་ལས་ནི་རྣམ་པར་ཉམས་ཀྱང་ངན་སོང་དུ་མི་འགྲོ་སྟེ། དེར་འགྲོ་བའི་ལས་དང་ཉོན་མོངས་པ་ཐག་བསྲིངས་པའི་ཕྱིར་རོ། །

[Block 2630]
བཟོད་པ་ཐོབ་པ་ཁོ་ནས་འགྲོ་བ་དང་། སྐྱེ་གནས་དང་། སྐྱེ་བ་དང་། ལུས་དང་། སྲིད་པ་དང་། ཉོན་མོངས་པ་རྣམས་ལས༌[^1822]ཁ་ཅིག་གིས༌[^1823]མི་སྐྱེ་བའི་ཆོས་ཉིད་ཐོབ་སྟེ། ངན་སོང་གི་འགྲོ་བ་རྣམས་དང་། སྒོ་ང་ལས་སྐྱེས་པ༌[^1824]དང་། དྲོད་གཤེར་ལས་སྐྱེས་པའི༌[^1825]སྐྱེ་གནས་དག་དང་། འདུ་ཤེས་མེད་པའི་སེམས་ཅན་དག་དང་། བྱང་གི་སྒྲ་མི་སྙན་དང་། ཚངས་པ་ཆེན་པོར་སྐྱེ་བ་རྣམས་དང་། ཟ་མ་དང་། མ་ནིང་དང་མཚན་གཉིས་པའི་ལུས་རྣམས་དང་བརྒྱད་པ་ལ་སོགས་པའི་སྲིད་པ༌[^1826]རྣམས༌[^1827]དང་། མཐོང་བས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་རྣམས་ཀྱི་མི་སྐྱེ་བའི་ཆོས་ཉིད་འཐོབ་བོ། །
--- END BLOCKS ---
