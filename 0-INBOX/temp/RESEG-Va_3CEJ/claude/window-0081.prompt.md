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
[Block 2836]
གཙུག་ལག་ལས།

[Block 2837 [VERSE]]
དང་པོར་ནུར་ནུར་པོ་ཡིན་ནོ། །
ནུར་ནུར་པོ་ལས་མེར་མེར་སྐྱེ། །
མེར་མེར་པོ་ལས་ནར་ནར་སྐྱེ། །
ནར་ནར་པོ་ལས་མཁྲང་འགྱུར་སྐྱེ། །

[Block 2838]
མཁྲང་ལས་རྐང་ལག་འགྱུས་པ་འདྲ།[^1559] །སྐྲ་སྤུ་སེན་མོ་ལ་སོགས་པ།[^1560] །

[Block 2839 [VERSE]]
དབང་པོ་གཟུགས་ཅན་རྣམས་དང་ནི། །
མཚམས་རྣམས༌[^1561]རིམ་གྱིས་སྐྱེ་བར་འགྱུར། །

[Block 2840]
ཞེས་འབྱུང་ངོ་། །ནུར་ནུར་པོ་དང་། མེར་མེར་པོ་དང་། ནར་ནར་པོ་དང་། མཁྲང་འགྱུར་དང་། རྐང་ལག་འགྱུས་པའི་གནས་སྐབས་དེ་དག་ནི་མངལ་གྱི་གནས་སྐབས་ལྔ་ཡིན་ནོ། །

[Block 2841]
ཡང་དུས་གཞན་ན༌[^1562]མངལ་གྱི་ཟུག་རྔུ་དེ༌[^1563]ཡོངས་སུ་སྨིན་པར་གྱུར་པ༌[^1564]མངལ་གྱི་ནང་ན་གང་དག་གིས་མངལ་གྱི་ཟུག་རྔུ་དེ་བསྒྱུར་ནས་མའི་ལུས་ཀྱི་མི་གཙང་བའི་སྒོ་ལོགས་སུ་ཁ་བསྟན་ནས་འཇོག་པར་བྱེད་པ་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པའི་རླུང་དག་ལྡང་སྟེ། དེ་གནས་ནས་སྦེད་པ་ན་མི་གཙང་བ་མཁྲང་བོ་དེ༌[^1565]ཤིན་ཏུ་ཆེན་པོ་འཚིར་བ༌[^1566]བཞིན་དུ་སྤོ་དཀའ་བ་ཡིན་ནོ། །

[Block 2842]
གལ་ཏེ་ན་རེས་འགའ་མའི་ཟས་དང་། གནས་པའི་བྱ་བ་མི་མཐུན་པར་སྤྱོད་པའམ་སྔོན་གྱི་ལས་ཀྱི་ཉེས་པས་མངལ་ཁོ་ནར་འཆི་བར་འགྱུར་རོ། །

[Block 2843]
དེ་ནས་འདི་དེ་ཤེས་པའི་བུད་མེད་དམ། གཞོན་ནུའི་སྨན་པས་མར་སར་རམ། ཏིལ་མར་འཇམ་ཙམ་མམ། ཤིང་ཤལ་མ་ལི་ལེགས་པར་བཏགས་པའི་ཕྱེ་མའམ། གཞན་ཡང་རུང་བས་ལག་པ་བསྐུས་ནས། དེ་ལ་མཚོན་རྣོན་པོ་སྲབ་མོ་བཏགས་ཏེ། རྐྱག༌[^1567]དོང་ལྟ་བུར་མི་བཟད་པ་དྲི་ང་བ་མུན་ཁུང་ལ་སོགས༌[^1568]པའི་འདམ་རྫབ་སྲིན་བུའི་རིགས༌[^1569]ཤིན་ཏུ་མང་པོ་སྟོང་ཕྲག་གི་གནས། རྟག་ཏུ་འཛག་པར་འགྱུར་བ། རྟག་ཏུ་བྱི་དོར་བྱ་དགོས་པ། ཁུ་ཆུ་དང་ཁྲག་དང་ཆུ་སེར་དང་དྲི་མས༌[^1570]ཀུན་ཏུ་མྱགས་པ། རྣམ་པར་མྱགས་པ། རུལ་པ། རྣགས་པ། འགྲེད་པ། མཐོང་ན་འཇིགས་སུ་རུང་བ་པགས་པ༌[^1571]རྡོལ་བ་སྲབ་མོས་གཡོགས་པ། སྔོན་གྱི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པ་ལུས་ཀྱི་རྨ་འཁྱིམས་པ་ཆེན་པོ་དེར་ལག་པ་བཅུག་སྟེ། ཡན་ལག་དང་ཉིང་ལག་བཅད་ནས་འབྱིན་ཏོ། །

[Block 2844]
དེ་ཡང་སྔོན་གྱི་ལས་ལན་གྲངས་གཞན་ལ་མྱོང་བར་འགྱུར་བས༌[^1572]ཤེད་དུ་ཁྲིད་པར་བྱེད་དོ། །

[Block 2845]
འོན་ཏེ་བདེ་བར་བཙའ་བར་འགྱུར་ན་ནི་དེ་ནས་འདི་བུ་འདོད་པའི་མའམ། དེའི་གཡོག༌[^1573]བུད་མེད་རྣམས་ཀྱིས་བཙས་མ་ཐག་པའི་ལུས་རྨ་སར་པ་ལྟ་བུ་མཚོན་དང་ཐལ་བའི་སྨན་ལྟ་བུའི་རེག་པ་དང་ལྡན་པའི་ལག་པ་གཉིས་ཀྱིས་བླངས་ནས་འཁྲུ་བར་བྱེད་དོ། །

[Block 2846]
ནུ་ཞོ་དང་མར་སར་གྱིས་སྐྱེད་པར་བྱེད་ཅིང་རིམ་གྱིས་ཁ་ཟས་རགས་པ་བཟའ༌[^1574]བར་གོམས་པར་ཡང་བྱེད་དོ། །

[Block 2847]
དེ་སྐྱེ་བའི་རྒྱུས་དབང་པོ་རྣམས་ཡོངས་སུ་སྨིན་ནས་ནི་ཡང་ཉོན་མོངས་པ་རྣམས་ཀུན་ཏུ་སྤྱོད་ཅིང་། ལས་རྣམས་ཀྱང་སྩོགས་པར་འགྱུར་རོ། །

[Block 2848]
དེ་དག་གི༌[^1575]ལུས་ཞིག་ནས་ཡང་སྔ་མ་བཞིན་དུ་སྲིད་པ་བར་མའི་རྒྱུན་གྱིས་འཇིག་རྟེན་ཕ་རོལ་ཏུ་འགྲོ་སྟེ།

[Block 2849 [HEADING]]
#### སྲིད་པའི་འཁོར་ལོ་ཐོག་མ་མེད། ^3-1-10-0

[Block 2850]
སྲིད་པའི་འཁོར་ལོ་ཐོག་མ་མེད། །རྣམ་པ་དེས་ན་ལས་དང་ཉོན་མོངས་པའི་རྒྱུ་ལས་བྱུང་བའི་སྐྱེ་བ་དང་། ཡང་དེ་ལས་བྱུང་བའི་ལས་དང་ཉོན་མོངས་པ་རྣམས་དང་། ཡང་དེ༌[^1576]ལས་སྐྱེ་བ་རྣམས་ཡིན་པས་ན་སྲིད་པའི་འཁོར་ལོ༌[^1577]ཐོག་མ་མེད་པ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 2851]
ཐོག་མ་ཞིག་བརྟགས༌[^1578]ན་ནི་དེའི་རྒྱུ་མེད༌[^1579]པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 2852]
རྒྱུ་མེད་པ་ཉིད་གཅིག་ཡིན་ན་ནི་འདི་ཐམས་ཅད་ཀྱང་རྒྱུ་མེད་པ་ཁོ་ནར་འགྱུར་བ་ཞིག་ན་ཡུལ་དང་དུས་སོ་སོར་ངེས་པ་ལས་མྱུ་གུ་ལ་སོགས་པ་ལ༌[^1580]ས་བོན་ལ་སོགས་པ་དང་། ཚོས་པ་ལ་སོགས་པ་ལ་མེ༌[^1581]ལ་སོགས་པའི་ནུས་པ་ཡང་མཐོང་བས་རྒྱུ་མེད་པ་ལས་འབྱུང་བ༌[^1582]ནི་མེད་དོ། །

[Block 2853]
རྒྱུ་རྟག་པ་ཡོད་པར་སྨྲ་བ་ནི་སྔར་བསལ་ཟིན་པ་ཉིད་དོ། །

[Block 2854]
དེ་ལྟ་བས་ན་འཁོར་བའི་ཐོག་མ་ནི༌[^1583]མེད་པ་ཁོ་ནའོ། །

[Block 2855]
སྐྱེ་བ་ནི་རྒྱུ་ལ་རག་ལུས་པའི་ཕྱིར༌[^1584]རྒྱུ་ཟད་པ༌[^1585]ལས་མཐའ་དང་ལྡན་པར་ནི་རིགས་ཏེ། ས་བོན་ཟད་པས་མྱུ་གུ་བཞིན་ནོ། །

[Block 2856 [HEADING]]
#### རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ། ^3-1-11-0

[Block 2857]
དེ་ལྟར་ཕུང་པོའི་རྒྱུན་སྐྱེ་བའི་གནས་སྐབས་གསུམ་པ༌[^1586]བསྟན་པ་གང་ཡིན་པ།

[Block 2858 [HEADING]]
##### ཡན་ལག་བཅུ་གཉིས་ཆ་གསུམ། ^3-1-11-1-0

[Block 2859 [VERSE]]
དེ་ནི་རྟེན་ཅིང་འབྲེལ་འབྱུང་བའི། །
ཡན་ལག་བཅུ་གཉིས་ཆ་གསུམ་མོ། །

[Block 2860]
དེ་ལ་ཡན་ལག་བཅུ་གཉིས་ནི་མ་རིག་པ་དང་། འདུ་བྱེད་དང་། རྣམ་པར་ཤེས་པ་དང་། མིང་དང་གཟུགས་དང་། སྐྱེ་མཆེད་དྲུག་དང་། རེག་པ་དང་། ཚོར་བ་དང་། སྲེད་པ་དང་། ལེན་པ་དང་། སྲིད་པ་དང་། སྐྱེ་བ་དང་། རྒ་ཤི་དང་།[^1587] ཆ་གསུམ་ནི་སྔོན་གྱི་མཐའ་དང་། ཕྱི་མའི་མཐའ་དང་། བར་དག་སྟེ། འདས་པ་དང་། མ་འོངས་པ་དང་། ད་ལྟར་བྱུང་བའི་སྐྱེ་བ་དག་ཡིན་ནོ། །

[Block 2861]
ཆ་གསུམ་པོ་འདི་དག་ཏུ་ཡན་ལག་བཅུ་གཉིས་ཇི་ལྟར་རྣམ་པར་གཞག་ཅེ་ན། སྔོན་དང་ཕྱི་མཐའི༌[^1588]གཉིས་གཉིས་པ། །[^1589]མ་རིག་པ་དང་། འདུ་བྱེད་རྣམས་ནི་སྔོན་གྱི་མཐར་རོ། །

[Block 2862]
སྐྱེ་བ་དང་། རྒ་ཤི་ནི་ཕྱི་མའི་མཐར་རོ། །

[Block 2863]
ལྷག་མ་བརྒྱད་ནི་བར་དུའོ། །

[Block 2864]
ཡང་ཅི་ཐམས་ཅད་ཀྱི་སྐྱེ་བ་འདི་ལ་ཡན་ལག་བརྒྱད་པོ་འདི་དག་ཡོད་དམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ནོ། །

[Block 2865]
འོ་ན་སུ་ལ་ཡོད་ཅེ་ན། ཡོངས་རྫོགས་ལྡན་ནོ། །

[Block 2866]
[^1590]འདི་ལ་ཡོངས་སུ་རྫོགས་པ་ཡོད་པས་ན་ཡོངས་སུ༌[^1591]རྫོགས་ལྡན་ནོ། །

[Block 2867]
འདིར་ནི་གང་ཟག་གང་ཞིག་གནས་སྐབས་ཀྱི་བྱེ་བྲག་འདི་ཐམས་ཅད་ལ་རེག་པ་དེ་ལ་དགོངས་པ་ཡིན་གྱི། གང་བར་མ་དོ་ཁོ་ནར་འཆི་བ་ཡང་མ་ཡིན་ལ། གཟུགས་དང་གཟུགས་མེད་པ་ན་སྤྱོད་པ་ཡང་མ་ཡིན་ཏེ། འདི་ལྟར་གླེང་གཞི་ཆེན་པོའི་རྣམ་གྲངས་ཀྱི་མདོ་ལས་ཀུན་དགའ་བོ་གལ་ཏེ་རྣམ་པར་ཤེས་པ་མའི་མངལ་དུ་ཞུགས་པར་མ་གྱུར་ན་ཞེས་གསུངས་པའི་ཕྱིར་འདོད་པ་ན་སྤྱོད་པའི་གང་ཟག་ཁོ་ནར་བསྟན་པ་ཡིན་ནོ། །

[Block 2868]
གང་གི་ཚེ་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་སྔོན་གྱི་མཐའ་པ་དང་། ཕྱི་མའི་མཐའ་པ་ཞེས་རྣམ་པ་གཉིས་སུ་བརྗོད་པ་དེའི་ཚེ་ནི་ཚོར་བ་ལ་ཐུག་པའི་བར་ཡན་ལག་བདུན་ནི་སྔོན་གྱི་མཐའ་པ་ཡིན་ལ། ལྔ་ནི་ཕྱི་མའི་མཐའ་པ་ཡིན་ཏེ། སྔོན་དང་ཕྱི་མའི་མཐའ་དང༌[^1592]འབྲས་བུ་དང་རྒྱུ་དང་བཅས་པ་དག་སྨོས་པའི་ཕྱིར་རོ། །

[Block 2869]
ཡང་མ་རིག་པ་ལ་སོགས་པ་འདི་དག་གང་ཡིན་ཞེ་ན། མ་རིག་ཉོན་མོངས་སྔོན་གནས་སྐབས། །ཚེ་སྔ་མ་ལ་ཉོན་མོངས་པའི་གནས་སྐབས་གང་ཡིན་པ་དེ་ནི་འདི་ལ་མ་རིག་པ་ཞེས་བྱ་སྟེ། ལྷན་ཅིག་སྤྱོད་པའི་ཕྱིར་དང་། དེའི་དབང་གིས་དེ་དག་ཀུན་ཏུ་འབྱུང་བའི་ཕྱིར་རྒྱལ་པོ་གཤེགས་སོ་ཞེས་བྱས་ན་དེའི་ཞ༌[^1593]འབྲིང་པ་ཡང་འོང་བར་འགྲུབ་པ་བཞིན་ནོ། །

[Block 2870]
འདུ་བྱེད་དག་ནི་སྔོན་ལས་ཀྱི། །གནས་སྐབས་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཚེ་སྔ་མ་ལ་བསོད་ནམས་ལ་སོགས་པའི་ལས་ཀྱི་གནས་སྐབས་གང་ཡིན་པ་དེ་ནི་འདི་ལ་འདུ་བྱེད་རྣམས་ཞེས་བྱ་སྟེ།

[Block 2871 [VERSE]]
ལས་གང་གིས༌[^1594]འདིར་རྣམ་པར་སྨིན་པའོ། །
རྣམ་ཤེས་མཚམས་སྦྱོར་ཕུང་པོ་ཡིན། །

[Block 2872]
མའི་མངལ་དུ་ཉིང་མཚམས་སྦྱོར་བའི་སྐད་ཅིག་མ་ལ་ཕུང་པོ་ལྔ་ནི་རྣམ་པར་ཤེས་པ་ཡིན་ནོ། །

[Block 2873 [VERSE]]
མིང་དང༌[^1595]གཟུགས་ནི་དེ་ཕན་ཆད། །
སྐྱེ་མཆེད་དྲུག་དོད་ཚུན་ཆད་དོ། །

[Block 2874]
མཚམས་སྦྱོར་བའི༌[^1596]སེམས་ཕན་ཆད་ནས་ཇི་སྲིད་དུ་སྐྱེ་མཆེད་དྲུག་མ་དོད་ཀྱི་བར་གྱི་གནས་སྐབས་དེ་ནི་མིང་དང་གཟུགས་ཞེས་བྱའོ། །

[Block 2875]
སྐྱེ་མཆེད་བཞི་དོད༌[^1597]ཚུན་ཆད་དོ་ཞེས་བརྗོད་པར་བྱ་བ་ཡིན་པ་ལས་སྐྱེ་མཆེད་དྲུག་ཅེས་བརྗོད་པ་ནི་དེའི་ཚེ་དེ༌[^1598]རྣམ་པར་འཇོག་པའི༌[^1599]ཕྱིར་རོ། །
--- END BLOCKS ---
