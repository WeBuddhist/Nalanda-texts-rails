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
[Block 1751]
ཕྱིས་ཅིའི་ཕྱིར་སྟོབས་དང་མི་ལྡན་པ་ཉིད་དུ་འགྱུར། གང་གི་ཕྱིར་ན་འདི་ཆོས་དང་ལྷན་ཅིག་ཏུ་མི་རྟག་པ་ཉིད་ཀྱིས་འཇོམས། བྱ་བ་བྱས་ཟིན་པས་ཡང་མི་ནུས་ཏེ་སྐྱེ་བ་བཞིན་ནོ། །

[Block 1752]
སྐྱེ་བས་ནི་མི་ནུས་པར་རིགས་ཏེ། སྐྱེ་བས་བསྐྱེད་པར་བྱ་བ་ད་ལྟ་ཉིད་དུ་ཁྱེར་ཏེ་འོངས་ནས་ཡང་བཀུར་བར་ནི༌[^828]མི་ནུས་སོ། །

[Block 1753]
གནས་པས་ནི་གནས་པར་བྱ་བ་ཡེ་གནས་པར་བྱ་བར་ཡང༌[^829]ནུས་སོ། །

[Block 1754]
དེ་ལྟ་བས་ན་གང་མི་ནུས་པ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1755]
ཡང་ན་འདི་ལ་བགེགས་བྱེད༌[^830]པ་ཡང་གང་ཞིག་ཡིན་ཏེ། [^831]རྒ་བ་དང་མི༌[^832]རྟག་པ་ཉིད་དེ་དག་ཁོ་ན་ཡིན་ནོ། །

[Block 1756]
གལ་ཏེ་དེ་དག་སྟོབས་དང་ལྡན་པ་ཞིག་ཡིན་ན་ནི་སྔོན་ཁོ་ན་ཡིན་ནོ། །

[Block 1757]
གནས་པའི་བྱ་བ་ལོག་ན་ཡང་དེ་དག་ཀྱང་མི་གནས་ལ་ཆོས་དེ་ཡང་མི་གནས་ན་ཇི་ལྟར༌[^833]གང་ལ་བྱ་བ་བྱེད་པ༌[^834]ནུས་པར་འགྱུར། ཡང་ན་དེ་དག་གིས་ཅི་ཞིག་བྱ་སྟེ། གནས་པས་ཡོངས་སུ་གཟུང་བའི་ཕྱིར་ཆོས་སྐྱེས་པ་ཙམ་དེ་མ་ཞིག་པར་གྱུར༌[^835]པ་ཡིན་ལ། དེས་དེ༌[^836]ཡལ་བར་བཏང་ན་ནི་ངེས་པར་མི་གནས་པས་འདི་ཉིད་འདིའི་འཇིག་པ་ཡིན་ནོ། །

[Block 1758]
རེ་ཞིག་ཆོས་སྐྱེས་པ་གཅིག་ལ་མི་འཇིག་པ་ནི་གནས་པ་ཡིན་ལ། འཇིག་པ་ནི་མི་རྟག་པ་ཉིད་ཡིན་ལ། གཅིག་ལ་རྒ་བ༌[^837]ནི་རྣམ་པ་ཐམས་ཅད་དུ་མི་སྲིད་དེ། རྒ་བ་ཞེས་བྱ་བ་ནི་གཞན་ཉིད་དུ་འགྱུར་ཞིང་རྣམ་པར་འགྱུར་བ་ཡིན་ན་དེ་ཉིད་ལས་དེའི་རྣམ་པ་གཞན་ཉིད་དུ་ནི་རུང་བ་མ་ཡིན་ནོ། །

[Block 1759]
འདིར་སྨྲས་པ།

[Block 1760 [VERSE]]
དེ་བཞིན་ན་ནི་རྒ་མི་འགྱུར། །
གཞན་དུ་འགྱུར་ན་དེ་གཞན་ཉིད། །
དེ་ལྟ་བས་ན་དངོས་གཅིག་ལ། །
རྒ་ཞེས་བྱ་བ་མི་འཐད་དོ། །

[Block 1761]
གང་ཡང་སྡེ་པ་གཞན་དག་ན་རེ་འཇིག་པའི་རྒྱུ༌[^838]དང་ཕྲད་ནས་མི་རྟག་པ་ཉིད་ཀྱིས་འཇིག་པར་བྱེད་དོ་ཞེས་ཟེར་བ་དེའི་ནི་འཁྲུ་བ་དང༌[^839]ཕྲད་ནས་ལྷས་འཁྲུ་བར་བྱེད་དོ་ཞེས་བྱ་བ་ལྟ་བུར་འགྱུར་ཏེ། འཇིག་པའི་རྒྱུ༌[^840]དེ་ཉིད་ཀྱིས་འཇིག་ན་དེ་བརྟགས་པས་ཅི་ཞིག་བྱ། སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་སྐད་ཅིག་མ་ཉིད་དུ་ཁས་བླངས་པས་དེ་དག་གིས༌[^841]མི་རྟག་པ་ཉིད་འཇིག་པའི་རྒྱུ་ལ་མི་ལྟོས་པའི་ཕྱིར་གནས་པ་དང་མི་རྟག་པ་ཉིད་དག་དུས་ཐ་མི༌[^842]དད་པར་བྱ་བ་བྱེད་པར་འགྱུར་བས་ཅིག་ལ་དུས་གཅིག་ཏུ་གནས་པ་དང་འཇིག་པ་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 1762]
དེ་ལྟ་བས་ན་རྒྱུན་ལ་འདུས་བྱས་ཀྱི་མཚན་ཉིད་འདི་དག་གསུངས་པ་ཡིན་ཏེ། དེ་ལྟ་ན་མདོ་དེ་ལེགས་པར་དྲངས་པ་ཡིན་ནོ། །

[Block 1763]
གཞན་ཡང་གལ་ཏེ་མ་འོངས་པའི་སྐྱེ་བ་བསྐྱེད་པར༌[^843]བྱ་བ་སྐྱེད་པར་བྱེད་པ་ཡིན་ན་མ་འོངས་པ་ཐམས་ཅད་ཅིག་ཅར་ཅིའི་ཕྱིར་མི་བསྐྱེད། འདི་ལྟར།

[Block 1764 [VERSE]]
རྒྱུ་དང་རྐྱེན་དག་མེད་པར་ནི། །
སྐྱེ་བས་བསྐྱེད་བྱ་སྐྱེད་བྱེད་མིན། །

[Block 1765]
རྒྱུ་དང་རྐྱེན་ཚོགས་པ་མེད་པར་ནི་སྐྱེ་བས་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 1766]
འོ་ན་ནི་ཚོགས་པ་ཡོད་ན་ནི་འབྱུང་ལ་མེད་ན་ནི་མི་འབྱུང་བའི་ཕྱིར་རྒྱུ་དང་རྐྱེན་རྣམས་ཁོ་ནའི་མཐུ་ཡིན་པར་བལྟ་བར་བྱའི༌[^844]སྐྱེ་བ་ནི་མ་ཡིན་པས་རྒྱུ་དང་རྐྱེན་ཁོ་ན་སྐྱེད་པར་བྱེད་པ་དག་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 1767]
ཀྱེ་ཡོད་པ་ཐམས་ཅད་དམིགས་སམ་ཅི་ཆོས་ཀྱི་རང་བཞིན་ཕྲ་མོ་དག་ཡོད་བཞིན་དུ་ཡང་མི་དམིགས་སོ། །

[Block 1768]
སྐྱེ་བ་ཞིག་མེད་ན་སྐྱེས་ཞེས་བྱ་བ་ཉིད་དང་། གཟུགས་ཀྱི་སྐྱེ་བ་ཞེས་བྱ་བ་དྲུག་པའི་ཚིག་ཏུ་ཡང་མི་འགྱུར་ཏེ་དཔེར་ན་གཟུགས་ཀྱི་གཟུགས་ཞེས་མི་བྱ་བ་བཞིན་ནོ། །

[Block 1769]
དེ་བཞིན་དུ་མི་རྟག་པ་ཉིད་ཀྱི་བར་དུ་ཅི་རིགས་པར་བརྗོད་པར་བྱའོ། །

[Block 1770]
འོ་ན་ནི་དེས་ན་བདག་མེད་པའི་བློ་འགྲུབ་པར་བྱ་བའི་ཕྱིར་བདག་མེད་པ་ཉིད་ཅིག་ཀྱང་འདོད་པར་བྱས༌[^845]ལ། གཅིག་དང་། གཉིས་དང་། ཆེན་པོ་དང་། ཆུང་ངུ་དང་། ཐ་དད་པ་དང་ལྡན་པ་དང་། རྣམ་པར་ཕྱེ་བ་དང་། གཞན་དང་། གཞན་མ་ཡིན་པ་དང་། ཡོད་པ་ལ་སོགས་པའི་བློ་འགྲུབ་པར་བྱ་བའི་ཕྱིར་དང་། དྲུག་པར་བྱ་བའི་ཕྱིར་མུ་སྟེགས་བྱེད་ཀྱིས༌[^846]ཡོངས་སུ་བརྟག་པ༌[^847]གྲངས་དང་། ཚད་དང་། ཐ་དད་པ་ཉིད་དང་ལྡན་པ་དང་། རྣམ་པར་དབྱེ་བ་དང་། གཞན་ཉིད་དང་། གཞན་མ་ཡིན་པ་ཉིད་དང་། ཡོད་པ་ལ་སོགས་པ་དང་། གཟུགས་ཀྱི་ལྡན་པ༌[^848]ཞེས་བྱ་བ་ཡང་ཁས་བླང་བར་བྱ་དགོས་སོ། །

[Block 1771]
གཟུགས་ཀྱི་རང་བཞིན་ཞེས་བྱ་བ་དྲུག་པ་འདི་ཡང་ཇི་ལྟར་བརྟག །[^849]དེ་ལྟ་བས་ན་སྐྱེ་བ་ཞེས་བྱ་བ་འདི་ནི་མ་བྱུང་བ་ལས་བྱུང་བ་ཁོ་ནར་ཤེས་པར་བྱ་བའི་དོན་དུ་བརྟགས་པ༌[^850]ཙམ་མཛད་པ་ཡིན་ནོ། །

[Block 1772]
མ་བྱུང་བ་ལས་བྱུང་བའི་མཚན་ཉིད་ཀྱི་སྐྱེ་བ་དེ་ཡང་རྣམ་པ་མང་དུ་ཡོད་པས་དེ་བྱེ་བྲག་ཏུ་བྱ་བའི་ཕྱིར་གཟུགས་ཀྱི་སྐྱེ་བ་ཞེས་དྲུག་པར་མཛད་དེ། ཅི་ནས་ཀྱང་གཟུགས་ཞེས་བྱ་བ་ཁོ་ན་སྐྱེ་བར་ཤེས་པར་བྱའི༌[^851]གཞན་དུ་ནི་ཤེས་པར་མི་འགྱུར་བར༌[^852]བྱ་བ་ཡིན་ཏེ། དཔེར་ན་ཙན་དན་གྱི་དྲི་ལ་སོགས་པ་དང་། མཆི་གུའི༌[^853]ལུས་ཞེས་བྱ་བ་བཞིན་ནོ། །

[Block 1773]
དེ་བཞིན་དུ་གནས་པ་ལ་སོགས་པ་ལ༌[^854]ཡང་ཅི་རིགས་པར༌[^855]བྱའོ། །

[Block 1774]
གལ་ཏེ་སྐྱེ་བ་མེད་པར་སྐྱེ་ན་ནམ་མཁའ་ལ་སོགས་པ་འདུས་མ་བྱས་ཀྱང་ཅིའི་ཕྱིར་མི་སྐྱེ་ཞེ་ན། སྐྱེ་བ་ཞེས་བྱ་བ་ནི་མ་བྱུང་བ་ལས་འབྱུང་བ་ཡིན་ན་འདུས་མ་བྱས་ནི་རྟག་ཏུ་ཡོད་པའི་ཕྱིར་མི་སྐྱེའོ། །

[Block 1775]
ཡང་ཇི་ལྟར་ཆོས་ཉིད་ཀྱིས་ཐམས་ཅད་སྐྱེ་བ་དང་ལྡན་པར་མི་འདོད་པ་དེ་ལྟར་ཐམས་ཅད་མི་སྐྱེའོ་ཞེས་བྱ་བར་འདོད་པར་བྱའོ། །

[Block 1776]
ཡང་ན་ཇི་ལྟར་སྐྱེ་བ་དང་ལྡན་པར་མཚུངས་པ་ལས་དེ་དག་ལས་གཞན་པའི་རྐྱེན་རྣམས་ཀྱིས་དེ་དག་ལས་གཞན་པ༌[^856]བསྐྱེད་པར་ནུས་པ་མ་ཡིན་པ་དེ་བཞིན་དུ་ཐམས་ཅད་ཀྱིས་ཀྱང་འདུས་མ་བྱས་བསྐྱེད་པར་མི་ནུས་པར་འགྱུར་རོ། །

[Block 1777]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་སྐྱེ་བ་ལ་སོགས་པ་རྫས་ཀྱི་དངོས་པོར་གྲུབ་པ་ཉིད་དོ། །

[Block 1778]
རི་དགས༌[^857]དག་ཡོད་ཅེས་ཏེ་ནས་མི་རྨོ་བ་མ་ཡིན་པ་དང་སྦྲང་བུ་དག་ཡོད་ཅེས་ཏེ་ལ་དུ༌[^858]མི་བཟའ་བ་མ་ཡིན་པ་ལྟར་སུན་འབྱིན་པ་དག་ཡོད་ཅེས་ཏེ་ལུང་དོར་དུ་མི་རུང་བས༌[^859]དེ་ལྟ་བས་ན་སྐྱོན་རྣམས་ལ་ཡང་ལན་གདབ་པར་བྱ་ལ། གྲུབ་པའི་མཐའི་རྗེས་སུ་འབྲང་བར་ཡང་བྱའོ་ཞེས་ཟེར་རོ། །

[Block 1779]
མཚན་ཉིད་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 1780 [HEADING]]
#### མིང་གི་ཚོགས་ལ་སོགས་པ། ^2-3-8-0

[Block 1781]
མིང་གི་ཚོགས་ལ་སོགས་པ་གང་ཞེ་ན།

[Block 1782 [VERSE]]
མིང་གི་ཚོགས་ལ་སོགས་པ་ནི། །
མིང་དང་ངག་དང་ཡི་གེའི་ཚོགས། །

[Block 1783]
སོགས་པ་སྨོས་པས་ནི་ཚིག་དང་ཡི་གེའི་ཚོགས་གཟུང་ངོ་། །དེ་ལ་མིང་བྱེད་པ་ནི་མིང་སྟེ། དཔེར་ན་གཟུགས་སྒྲ་ཞེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 1784]
ངག་ནི་ཚིག་སྟེ། དཔེར་ན། ཀྱེ་མ་འདུ་བྱེད་རྣམས་མི་རྟག །ཅེས་བྱ་བ་དེ་ལྟ་བུ་ལ་སོགས་པ་ཇི་ཙམ་གྱིས༌[^860]དོན་ཡོངས་སུ་རྫོགས་པ་སྟེ། གང་གིས་བྱ་བ་དང་ཡོན་ཏན་དང་དུས་ཀྱི་འབྲེལ་བའི་ཁྱད་པར་རྟོགས་པར་འགྱུར་རོ། །

[Block 1785]
ཡི་གེ་ནི་ཡི་གེ་སྟེ། དཔེར་ན་ཨ་ཨཱ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལྟ་བུའོ། །

[Block 1786]
ཡི་གེ་རྣམས་ཀྱང་ཡི་གེ༌[^861]འབྲུའི་ཡན་ལག་དག་གི་མིང་དག་མ་ཡིན་ནམ༌[^862]ཞེ་ན། ཡི་གེ༌[^863]འབྲུའི་ཡན་ལག་རྣམས་གོ་བར་བྱ་བའི་ཕྱིར་ཡི་གེ་རྣམས་བྱས་པ་ནི་མ་ཡིན་གྱི། ཇི་ལྟར་ན་མིང་ཐོས་པ་བྲིས་པས་གོ་བར་འགྱུར་ཞེས་ཡི་གེ་རྣམས་གོ་བར་བྱ་བའི་ཕྱིར་ནི་ཡི་གེའི༌[^864]འབྲུ་རྣམས་བྱས་པ་ཡིན་པས། ཡི་གེ་རྣམས་ནི་དེ་དག་གི་མིང་མ་ཡིན་ནོ། །

[Block 1787]
མིང་ལ་སོགས་པ་དེ་དག་གི་ཚོགས་ནི་མིང་ལ་སོགས་པའི་ཚོགས་དག་ཡིན་ཏེ། མང་པོའི་དོན་གང་ཡིན་པའོ། །

[Block 1788]
དེ་ལ་མིང་གི་ཚོགས་ནི་དཔེར་ན་གཟུགས་སྒྲ་དྲི་རོ་རེག་བྱ་དག་ཅེས་བྱ་བ་སྟེ། དེ་ལྟ་བུ་ལ་སོགས་པའོ། །

[Block 1789]
ཚིག་གི་ཚོགས་ནི་དཔེར་ན་འདུ་བྱེད་ཐམས་ཅད་མི་རྟག་པ་དག་གོ། །

[Block 1790]
མྱ་ངན་ལས་འདས་པ་ནི་ཞི་བའོ་ཞེས་བྱ་བ་སྟེ། དེ་ལྟ་བུ་ལ་སོགས་པའོ། །
--- END BLOCKS ---
