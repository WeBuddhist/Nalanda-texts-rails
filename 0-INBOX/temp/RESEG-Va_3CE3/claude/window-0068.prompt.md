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
[Block 2381]
དེ་བཞིན་དུ་མཚན་མ་མེད་པ་ལ་སོགས་པ་ཡང་མངོན་པར་ཞེན་པར་འགྱུར་བ་ཞིག་ན། འདི་ལྟར་སྟོང་པ་ཉིད་ལ་སོགས་པ་ནི་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་མངོན་པར་ཞེན་པར་མི་འགྱུར་རོ། །

[Block 2382]
དེ་བཞིན་དུ་སངས་རྒྱས་དང་། ཉན་ཐོས་རྣམས་ཀྱང་མངོན་པར་ཞེན་པར་མི་འགྱུར་རོ་ཞེས་གསུངས་པའོ། །

[Block 2383]
རབ་འབྱོར་འདི་ལྟར་ཆོས་ཐམས་ཅད་མིང་དང་། མཚན་མ་ཙམ་དུ་ཟད་དོ༌[^1686]ཞེས་བྱ་བ་ནི་འདི་ལྟར་ཆོས་ཐམས་ཅད་མིང་དང་། མཚན་མ་ཙམ་དུ་ཟད་ན། འཇིག་རྟེན་རྣམས་ཀྱིས་དེ་ལྟར་མི་ཤེས་ཏེ། དེ་བས་ན་དེ་དག་གིས་རྟོགས་པར་བྱ་བའི་ཕྱིར་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་སྤྱོད་པར་འགྱུར་རོ། །

[Block 2384]
འདི་ལྟར་ཆོས་ཐམས་ཅད༌[^1687]མིང་དང་མཚན་མ་ཙམ་དུ་ཟད་དེ། དེའི་ཕྱིར་དེ་དག་རྟོགས་པས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཐོབ་པར་འགྱུར་རོ། །

[Block 2385]
གལ་ཏེ་ཆོས་འགའ་ཞིག་དངོས་པོ་ཡོད་ན། དེ་ལྟ་ན་ནི་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པར་མི་འགྱུར་རོ་ཞེས་བསྟན་པའོ། །

[Block 2386 [HEADING]]
##### ཐམས་ཅད་ཤེས་པ་ཉིད་དང་ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་དང་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད། ^1-2-7-39-0

[Block 2387]
རབ་འབྱོར་ཐམས་ཅད་ཤེས་པ་ཉིད་ཅེས་བྱ་བ་ནི་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་ཐམས་ཅད་ཀྱིའོ། །

[Block 2388]
ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ནི་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་རྣམས་ཀྱིའོ། །

[Block 2389 [HEADING]]
###### ཐམས་ཅད་ཤེས་པ་ཉིད། ^1-2-7-39-1-0

[Block 2390]
རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ནི༌[^1688]དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་རྣམས་ཀྱིའོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཐམས་ཅད་ཤེས་པ་ཉིད་ཅེས་བྱ་བ་ནི་འདུས་བྱས་ཐམས་ཅད་མི་རྟག་པའོ། །

[Block 2391]
ཟག་པ་དང་བཅས་པ་ཐམས་ཅད་སྡུག་བསྔལ་བའོ། །

[Block 2392]
ཆོས་ཐམས་ཅད་བདག་མེད་པའོ་ཞེས་ཐམས་ཅད་ཤེས་པ་ཉིད་རྣམ་པ་གསུམ་གྱིས་ཞུགས༌[^1689]ནས་ཆོས་དང་རྗེས་སུ་རྟོག་པའི༌[^1690]ཤེས་པའི་དབང་གིས་ཆོས་ཐམས་ཅད་ཀྱི་མཐར་གཏུགས་པའི་ཤེས་པ་ནི་ཐམས་ཅད་ཤེས་པ་ཞེས་བྱ་སྟེ། ཤེས་པ་དེ་ཡང་ཆོས་ཐམས་ཅད་རྣམ་པ་ཐམས་ཅད་དུ་ཤེས་པ་ནི་མ་ཡིན་གྱི། མཚན་ཉིད་གསུམ་དང་། བདེན་པ་བཞིའི་སྒོ་ནས་ཆོས་ཐམས་ཅད་ལ་རྨོངས་པ་མེད་པའི་ཕྱིར་ཉན་ཐོས་དང་། རང་སངས་རྒྱས་རྣམས་ཀྱི་ཤེས་པ་ལ་ཐམས་ཅད་ཤེས་པ་ཉིད་ཅེས་བྱའོ། །

[Block 2393 [HEADING]]
###### ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད། ^1-2-7-39-2-0

[Block 2394]
ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ཅེས་བྱ་བ་འདི་ལ་བྱང་ཆུབ་སེམས་དཔའ་དང་པོ་སེམས་བསྐྱེད་པ་ནས་མོས་པས་སྤྱོད་པའི་ས་ནས་བཟུང་སྟེ། ས་ཆོས་ཀྱི་སྤྲིན་ལ་ཐུག་གི་བར་དུ་ཀུན་དུ་འགྲོ་བའི་དོན་དང་། མཆོག་གི་དོན་ལ་སོགས་པ་རབ་ཏུ་རྟོགས་པས་དེ་བཞིན་ཉིད་རྣམ་པར་སྤྱོད་པ་ལ་ཞུགས་པ་གནས་གྱུར་པའི་རྒྱུར་གྱུར་པ་དང་། སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པ་དང་། བདེ་བའི་ཕྱིར་ཞུགས་པའི་ཡེ་ཤེས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཀྱི༌[^1691]གྲོང་ཁྱེར་ཆེན་པོར་ཕྱིན་པར་བྱེད་པ་སྟེ། ལམ་གྱི་རྣམ་པ་ཤེས་པ་ཉིད་ཅེས་བྱའོ། །

[Block 2395 [HEADING]]
###### རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད། ^1-2-7-39-3-0

[Block 2396]
རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཅེས་བྱ་བ་ནི། སངས་རྒྱས་རྣམས་ཀྱི་ཡེ་ཤེས་ནམ་མཁའི་ཁམས་ཀྱི་མཐས༌[^1692]གཏུགས་པའི༌[^1693]སེམས་ཅན་གྱི་དོན་གྱི་རྒྱུན་མ་བཅད་པ། ཆོས་ཀྱི་སྐུ་རབ་ཏུ་རྟོགས་པ། བག་ཆགས་ཀྱི་མཚམས་སྦྱོར་བ་རབ་ཏུ་སྤངས་པ་འབྲས་བུའི་ཡེ་ཤེས་ཏེ། ཆོས་ཐམས་ཅད་ལ་རྣམ་པ་ཐམས་ཅད་དུ་ཞུགས་པའི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཅེས་བྱའོ། །

[Block 2397]
རབ་འབྱོར་རྣམ་པ་གཅིག་གིས་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཅེས་བྱ་སྟེ་འདི་ལྟར་ཞི་བའི་རྣམ་པས་ཞེས༌[^1694]བྱ་བ་ནི་གང་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས༌[^1695]ཡོངས་སུ་རྟོགས་པ་དང་། རྣམ་པར་རྟོག་པའི་རྣམ་པ་ཐམས་ཅད་རབ་ཏུ་ནུབ་ཅིང་སེམས་ཅན་གྱི་འཇིག་རྟེན་དང་། སྣོད་ཀྱི་འཇིག་རྟེན་མཐའ་དག་དང་། བྲལ་བ་ཁམས་གསུམ་དུ་གཏོགས་པའི་ཚུལ་ཁྲིམས་ཀྱིས༌[^1696]རྣམ་པར་རྟོག་པའི༌[^1697]སྤྲོས་པའི་དྲ་བ་འགགས་པར་གྱུར་པ་ན། ཆོས་ཀྱི་དབྱིངས་ཤིན་ཏུ་རྣམ་པར་དག་པ་མཉམ་པ་ཉིད་ཀྱི་རྣམ་པར་ཞུགས་པ་ལྷུན་གྱིས་གྲུབ་པའི༌[^1698]ཆོས་ཀྱི་སྐུའི་བདག་ཉིད་ཤིན་དུ་ཞི་བའི་རྣམ་པ་གང་ཡིན་པ་དེ། ཆོས་ཐམས་ཅད་ཀྱི་རྣམ་པ་ཡིན་པའི་ཕྱིར་རྣམ་པ་ཐམས་ཅད་ཅེས་བྱ་སྟེ། རྣམ་པ་དེ་ལྟ་བུར་ཞུགས་པའི་ཡེ་ཤེས་ཀྱི་རང་བཞིན༌[^1699]དེ་ལྟ་བུ་ལ་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་ཅེས་བྱའོ། །

[Block 2398]
བག་ཆགས་ཀྱི་མཚམས་སྦྱོར་བ་སྤངས་པ་ཞེས་བྱ་བ་ནི་ལས་དང་ཉོན་མོངས་པའི་རྣམ་པར་རྟོག་པའི་བག་ཆགས་རྣམས་ལས།

[Block 2399]
འདིར་སེམས་ཅན་རྣམས་ཀྱི་རྒྱུ་དང་འབྲས་བུ་གཅིག་ནས་གཅིག་ཏུ་བར་མ་ཆད་པར་འབྱུང་བ་གང་ཡིན་པ་དེ། རྒྱུན་ཆད་པ་ལ་བག་ཆགས་ཀྱི་མཚམས་སྦྱོར་བ་སྤངས་པ་ཞེས་བྱའོ། །

[Block 2400 [HEADING]]
##### རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་མ་ཐོབ་པར་ཉོན་མོངས་པ་སྤངས་པ། ^1-2-7-40-0

[Block 2401]
རྣམ་པ་ཐམས་ཅད་མཁྱེན་པ་ཉིད་མ་ཐོབ་པར་ཉོན་མོངས་པ་སྤངས་པ་འདུས་མ་བགྱིས་ལགས་སམ་ཞེས་བྱ་བ་ནི་འགོག་པའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་དེ་སྐད་གསུངས་ཏེ། འགོག་པ་ནི་སྤོང་བ་ཙམ་དུ་ཟད་པས། ལུས་དང་ངག་གི་འགྱུར་བ་དག་ནི་འབྱུང་ངོ་། །

[Block 2402]
དེ་དག་ཀྱང་བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་རྣམས་ལ་གནོད་པར་འགྱུར་བ་ནི་མ་ཡིན་ཞེས་བྱ་བ་ནི་མེ་ལོང་ལ་ལྟ་བ་དང་།[^1700] མཆོང་ཞིང་འགྲོ་བ་ལ་སོགས་པ་དང་། པི་ལིན༌[^1701]ད་བད་སས་དམངས་མོའི་ཚིག་བརྗོད་པ་བཞིན་ཏེ། དེ་དག་ཀྱང་བྱིས་པ་སོ་སོའི་སྐྱེ་བོ་རྣམས་སམ་འཕགས་པ་རྣམས་གང་ལ་ཡང་གནོད་པར་ནི་མི་འགྱུར་རོ། །

[Block 2403 [HEADING]]
##### འཕགས་པའི་གང་ཟག་འདུས་མ་བྱས་ཀྱིས་རབ་ཏུ་ཕྱེ་བ། ^1-2-7-41-0

[Block 2404]
ཅི་ལམ་ལ་གནས་ཏེ་འམ། ལམ་མ༌[^1702]ཡིན་པ་ལ་གནས་ཏེ་ཞེས་བྱ་བ་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པ༌[^1703]ནི་བཅོམ་ལྡན་འདས་ཀྱིས་སླར་བཀའ་སྩལ་ཏེ།[^1704] ལམ་ནི་དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པས་གནས་སུ་མི་རུང་ངོ་ཞེས་བྱ་བའོ། །

[Block 2405]
བཅོམ་ལྡན་འདས་གལ་ཏེ་ལམ་དངོས་པོ་མ་མཆིས་ལ། མྱ་ངན་ལས་འདས་པ་ཡང་དངོས་པོ་མ་མཆིས་ན། འོ་ན་ཅིའི་སླད་དུ་འདི་སྐད་དུ་འདི་ནི་རྒྱུན་དུ་ཞུགས་པའོ། །

[Block 2406]
འདི་ནི་ལན་ཅིག་ཕྱིར་འོང་བའོ་ཞེས་བཤད་ཅེས་བྱ་བ་ལ་སོགས་པས། འཕགས་པའི་གང་ཟག་རྣམས་དང་སངས་རྒྱས་བཤད་པ། ལམ་གྱི་དབང་གིས་བཤད་དམ། མྱ་ངན་ལས་འདས་པ་ཐོབ་པས་བཤད་གྲང་ན། གལ་ཏེ་གཉི་ག་མེད་ན་འཕགས་པའི་གང་ཟག་ཇི་ལྟར་རྣམ་པར་འགོད་ཅེས་དགོངས་པའོ། །

[Block 2407]
རབ་འབྱོར་དེ་དག་ཐམས་ཅད་ཀྱང་འདུས་མ་བྱས་ཀྱིས་རབ་ཏུ་ཕྱེ་བའོ་ཞེས་བྱ་བ་ནི་ལམ་དང་མྱ་ངན་ལས་འདས་པ་གཉིས་མེད་དུ་ཟིན་ཀྱང་། འདུས་བྱས་མེད་པའི་རང་བཞིན་དེ་བཞིན་ཉིད་ཀྱིས༌[^1705]རབ་ཏུ་ཕྱེ་བའོ་ཞེས་སླར་བཀའ་སྩལ་པའོ། །

[Block 2408]
བཅོམ་ལྡན་འདས་ཅི་ལགས་འདུས་མ་བགྱིས་པ་དེ་འདི་ནི་རྒྱུན་དུ་ཞུགས་པའོ་ཞེས་རབ་ཏུ་འབྱེད་པ་མཆིས་སམ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་འདུས་མ་བྱས་ཀྱིས་རབ་ཏུ་ཕྱེ་བས་འདུས་མ་བྱས་ཀྱིས༌[^1706]རབ་ཏུ་ཕྱེ་བའོ་ཞེས་དགོངས་ན།[^1707] ཅི་འདུས་མ་བྱས་པ་དེ་གང་ཟག་དེ་དག་རབ་ཏུ་འབྱེད་དམ། སྐྱེད་པར་འགྱུར་རམ་ཞེས་ཞུས་པའོ། །

[Block 2409]
རབ་འབྱོར་འདུས་མ་བྱས་ནི་རབ་ཏུ་འབྱེད་པ་མེད་མོད་ཀྱི་ཞེས་བྱ་བ་ནི་འདུས་མ་བྱས་སྐྱེད་པར་མི་བྱེད་མོད་ཀྱི། འོན་ཀྱང་གནས་གྱུར་པའི་དབང་གིས་དེ་བཞིན་ཉིད་ལ་འཇུག་པའི་བྱེ་བྲག་དང་། ཉོན་མོངས་པ་བག་ལ་ཉལ་བར༌[^1708]སྤོང་བའི་བྱེ་བྲག་གིས་དེ་དག་དེ་ལྟ་དེ་ལྟ་བུར་འགྱུར་བའི་ཕྱིར་འདུས་མ་བྱས་ཀྱིས༌[^1709]རབ་ཏུ་ཕྱེ་བའོ་ཞེས་བཤད་དོ་ཞེས་བསྟན་པའོ། །

[Block 2410 [HEADING]]
##### འཁོར་བའི་ཕྱི་མའི་མཐའ། ^1-2-7-42-0

[Block 2411]
བཅོམ་ལྡན་འདས་འོ་ན་ཇི་ལྟར་འཁོར་བའི་ཕྱི་མའི་མཐའ་མཆིས་པར་འགྱུར་ཞེས་བྱ་བ་ནི་སྔར་ཐོག་མ་དང་ཐ་མ་མེད་པ་སྟོང་པ་ཉིད་ལ་སོགས་པ་བཤད་པ་ལས།

[Block 2412]
འཁོར་བ་མེད་དོ་ཞེས་འཁོར་བའི་ཐོག་མ་དང་། ཐ་མ་དང་། དབུས་དམིགས་སུ་མེད་པ་སྨོས་ལ། ད་ནི་དགྲ་བཅོམ་པ་དག་འདུས་མ་བྱས་ཀྱིས་རབ་ཏུ་ཕྱེ་བར་འགྱུར་ན། འཁོར་བའི་ཕྱི་མའི་མཐའ་ཡོད་པར་འགྱུར་རོ་སྙམ་དུ་དགོངས་ནས་ཞུས་པའོ། །

[Block 2413]
རབ་འབྱོར་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཚད་མར་བྱས་ཀྱི་དོན་དམ་པར་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སོ་སོ་སྐྱེ་བོ་རྣམས་དང་། དགྲ་བཅོམ་པ་རྣམས་ཀྱི་དེ་བཞིན་ཉིད་ནི་དུས་ཐམས་ཅད་དུ་འཇུག་པའི་ཕྱིར་ཕྱི་མའི་མཐའ་མེད་མོད་ཀྱི། འོན་ཀྱང་གང་ཕུང་པོ་ལྔ༌[^1710]ཞེས་བྱ་བ་ཀུན་བརྟགས་པའི་ཆོས་དེ། རྒྱུན་ཆད་པ་ཉེ་བར་བཟུང་ནས་འཇིག་རྟེན་གྱི་ཐ་སྙད་དུ་དེ་ལྟ༌[^1711]བུ་དག་བཤད་དོ་ཞེས་བསྟན་པའོ།[^1712] །དེ་བས་ན་གང་དང་གང་གིས་མཐའ་ཆད་པ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 2414]
བཅོམ་ལྡན་འདས་ཆོས་ཐམས་ཅད་རང་གི་མཚན་ཉིད་ཀྱིས་སྟོང་པ་ལ་སྔོན་གྱི་མཐའ་མི་དམིགས་ན། ཕྱི་མའི་མཐའ༌[^1713]སྨོས་ཀྱང་ཅི་འཚལ་ཞེས་བྱ་བ་ནི་ཀུན་བརྟགས་པ་ཕུང་པོ་ལྔའི་ཆོས༌[^1714]དངོས་པོ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རང་གི་མཚན་ཉིད་ཀྱིས་སྟོང་སྟེ། སྒྱུ་མ་ལྟ་བུ་ཡིན་པའི་ཕྱིར་དེ་དག་སྐྱེ་བའི་འདུ་ཤེས་ཅན་རྣམས་ཀྱི་སྔོན་གྱི་མཐའ་ཡང་མེད་ན། འགག་པའི་འདུ་ཤེས་ཅན་རྣམས་ཀྱི་ཕྱི་མའི་མཐའ་ལྟ་ག་ལ་ཡོད་ཅེས་གསུངས་པའོ། །

[Block 2415]
རབ་འབྱོར་དེ་དེ་བཞིན་ནོ། །

[Block 2416]
དེ་དེ་བཞིན་ཏེ་ཞེས་བྱ་བ་ནི་ཆོས་ཐམས་ཅད་སྐྱེ་བ་མེད་ཅིང་འགག་པ་མེད་པའི་ཕྱིར་དེའི་ཚིག་ལ་རྗེས་སུ་ཡི་རང་བའོ། །

[Block 2417 [HEADING]]
##### ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བའི་དོན། ^1-2-7-43-0

[Block 2418 [HEADING]]
###### ཕ་རོལ་ཉིད། ^1-2-7-43-1-0

[Block 2419]
རབ་འབྱོར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་འདི་ནི་ཆོས་ཐམས་ཅད་ཀྱི་ཕ་རོལ་དམ་པ་སྟེ། དེའི་ཕྱིར་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱའོ་ཞེས་བྱ་བ་ལ། ཕ་རོལ་ཏུ་ཕྱིན་པ་ཞེས་བྱ་བ་ནི༌[^1715]འདིར་རྣམ་པར་རྟོག་པའི་དོན་བཞི་ཡོད་དེ་རེ་ཞིག་དང་པོར་ཕ་རོལ་ཏུ་ཕྱིན་པ༌[^1716]ཞེས་བྱ་བའི་སྒྲ་དང་དོན་མཚུངས་པ་པ༌[^1717]མཐའ་ཞེས་བྱ་བའི་སྒྲ་ཡང་ཡོད་དེ། ཕ་མཐའི་དངོས་པོ་ལ་ནི་ཕ་རོལ་ཉིད་ཅེས་བྱའོ། །

[Block 2420]
ཆོས་ཐམས་ཅད་ཀྱི་ཕ་མཐར་གྱུར་ཅིང་ཆོས་ཐམས་ཅད་ཀྱི་མཐར་ཐུག་པར་གནས་པའི་ཕྱིར་ཕ་རོལ་ཉིད་ཅེས་བྱའོ། །
--- END BLOCKS ---
