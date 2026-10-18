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
[Block 2906]
རབ་ཏུ་བྱེད་པ་དག་ལས་ཇི་སྐད་དུ་འབྱུང་ཞེ་ན། རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་གང་ཞེ་ན། འདུས་བྱས་ཀྱི་ཆོས་ཐམས་ཅད་དོ། །

[Block 2907]
རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི་ཆོས་རྣམས་གང་ཞེ་ན། འདུས་བྱས་ཀྱི་ཆོས་ཐམས་ཅད་དོ་ཞེས་འབྱུང་ངོ་། །

[Block 2908 [HEADING]]
###### གནས་སྐབས་པ་དང་རྒྱུན་ཆགས་པ། ^3-1-11-2-3-0

[Block 2909]
གནས་སྐབས་པ་ནི་བཅུ་གཉིས་དང་ལྡན་པའི་ཕུང་པོ་ལྔའི་གནས་སྐབས་ཚེ་གསུམ་བར་ཆད་མེད་པར་འབྲེལ་པ་དག་ཡིན་ནོ། །

[Block 2910]
དེ་ཉིད་རྒྱུན་ཆགས་པ་ཡང་ཡིན་ནོ། །

[Block 2911]
དེ་རྣམས་ལས་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་གང་ལས༌[^1616]དགོངས་ཤེ་ན། འདི་ནི་གནས་སྐབས་པར་འདོད་ལོ། །

[Block 2912]
གལ་ཏེ་ཡན་ལག་དང་ཡན་ལག་ལ་ཕུང་པོ་ལྔ་ཆར་ཡོད་ན་ཅིའི་ཕྱིར་མ་རིག་པ་ལ་སོགས་པའི་ཆོས་རྣམས་ཁོ་ནར་བསྒྲགས་ཤེ་ན། གཙོ་བོའི་ཕྱིར་ན་ཡན་ལག་བསྒྲགས། །མ་རིག་པ་གཙོ་བོ་ཡིན་པའི་གནས་སྐབས་སུ་ནི་མ་རིག་པར་བཤད་ལ། འདུ་བྱེད་གཙོ་བོ་ཡིན་པར་ནི་འདུ་བྱེད་ནས་རྒ་ཤི་གཙོ་བོ་ཡིན་པའི་བར་དུ་ནི་རྒ་ཤི་ཁོ་ན་བཤད་པས་ཉིས་པ༌[^1617]མེད་དོ། །

[Block 2913]
[^1618]ཡང་ཅིའི་ཕྱིར་མདོ་སྡེ་ལས་ནི་ཡན་ལག་བཅུ་གཉིས་སུ་གསུངས་ལ། རབ་ཏུ་བྱེད་པ་དག་ལས་ནི་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་གང་ཞེ་ན། འདུས་བྱས་ཀྱི་ཆོས་ཐམས་ཅད་དོ་ཞེས་གཞན་དུ་འབྱུང་ཞེ་ན། མདོ་ལས་གསུངས་པ་ནི་དགོངས་པ་ཅན་ཡིན་ནོ། །

[Block 2914]
ཆོས་མངོན་པ་ལས་ནི་མཚན་ཉིད་པ་ཡིན་ཏེ། དེ་བཞིན་དུ་གནས་སྐབས་པ་དང་། སྐད་ཅིག་པ་དང་། རྒྱུན་ཆགས་པ་དང་། འབྲེལ་པ་ཅན་དང་། སེམས་ཅན་དུ་སྟོན་པ་དང་། སེམས་ཅན་མ་ཡིན་པར་སྟོན་པ་ཞེས་བྱ་བ་ཐ་དད་པ་ཡིན་ནོ། །

[Block 2915 [HEADING]]
##### རྨོངས་པ་རྣམ་པ་གསུམ་བཟློག་པ། ^3-1-11-3-0

[Block 2916]
ཡང་ཅིའི་ཕྱིར་མདོ་ལས་སེམས་ཅན་དུ་སྟོན་པ་ཁོ་ན་གསུངས་ཤེ་ན།

[Block 2917 [VERSE]]
སྔོན་དང་ཕྱི་མཐའ་བར་དག་ལ། །
རྨོངས་པ་རྣམ་པར་བཟློག་ཕྱིར་རོ། །

[Block 2918]
དེ་ཉིད་ཀྱི་ཕྱིར་ཆ་གསུམ་པ་ཡིན་ནོ། །

[Block 2919]
དེ་ལ་སྔོན་གྱི་མཐའ་ལ་རྨོངས་པ་ལ་ནི་འདི་ཇི༌[^1619]ལྟར༌[^1620]བདག་འདས་པའི་དུས་ན་བྱུང་བར་གྱུར་ཏམ། འོན་ཏེ་བྱུང་བར་མ་གྱུར་བདག་ཅི་ཞིག་ཏུ་ནི་བྱུང་བར་གྱུར། བདག་ཇི་ལྟར་ན་ནི་བྱུང་བར་གྱུར་སྙམ་པའི་ཐེ་ཚོམ་འདི་སྐྱེའོ། །

[Block 2920]
ཕྱི་མའི་མཐའ་ལ་རྨོངས་པ་ལ་ནི་འདི་ལྟར་ཅི་མ་འོངས་པའི་དུས་ན་འབྱུང་བར་འགྱུར་རམ་སྙམ་པ་རྒྱས་པར་ཐེ་ཚོམ་འདི་སྐྱེའོ། །

[Block 2921]
བར་དུ་རྨོངས་པ་ལ་ནི་འདི་ལྟར་ཅི་ཞིག་ཡིན། འདི་ཇི་ལྟར་ཡིན། ཡོད་པ་ནི་ཅི་ཞིག་ཡིན། འགྱུར་བ་ནི་ཅི་ཞིག་ཡིན་སྙམ་པའི་ཐེ་ཚོམ་འདི་སྐྱེའོ། །

[Block 2922]
དེ་ལྟར་ན༌[^1621]རྨོངས་པ་རྣམ་པ་གསུམ་པོ་འདི་བཟློག་པའི་ཕྱིར་མདོ་ལས་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་སེམས་ཅན་དུ་སྟོན་པ་ཁོ་ན་ཆ་གསུམ་དུ་བསྟན་ཏེ། [^1622]མ་རིག་པ་དང་། འདུ་བྱེད་རྣམས་དང་། སྐྱེ་བ་དང་། རྒ་ཤི་དང་། རྣམ་པར་ཤེས་པ་ནས་སྲིད་པའི་བར་དང་གོ་རིམས་བཞིན་ནོ། །

[Block 2923]
འདི་ལྟར་མདོ་ཉིད་ལས་དགེ་སློང་དག་དགེ་སློང་གིས་གང་ཕན་ཆད་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བ་དང་རྟེན་ཅིང་འབྲེལ་བར་འབྱུང་བའི༌[^1623]ཆོས་རྣམས་ཡང་དག་པའི་ཤེས་རབ་ཀྱིས་དེ་ལྟར་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་མཐོང་བ་དེ་ནི་ཅི་བདག་འདས་པའི་དུས་ན་བྱུང་བར་གྱུར་ཏམ་སྙམ་དུ་སྔོན་གྱི་མཐའ་ལ་འབྲང་བར་མི་འགྱུར་རོ་ཞེས་བྱ་བ༌[^1624]རྒྱས་པར་གསུངས་སོ། །

[Block 2924]
གཞན་དག་ན་རེ་ཕྱི་མའི་མཐའ་ལ་རྨོངས་པ་བཟློག་པའི༌[^1625]ཕྱིར་སྲེད་པ་དང་། ལེན་པ་དང་། སྲིད་པ་དག་ཀྱང་བསྟན་ཏེ། འདི་དག་ནི་དེ་ཁོ་ནའི༌[^1626]རྒྱུ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2925 [HEADING]]
##### ཉོན་མོངས་པ་དང་ལས་དང་གཞིའི་རང་བཞིན། ^3-1-11-4-0

[Block 2926 [HEADING]]
###### ཉོན་མོངས་པ། ^3-1-11-4-1-0

[Block 2927]
ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡན་ལག་བཅུ་གཉིས་པ་དེ་ནི་ཉོན་མོངས་པ་དང་། ལས་དང་བཞི༌[^1627]ངག་དང་། གསུམ་གྱི་རང་བཞིན་དུ་རིག་པར་བྱ་སྟེ། དེ་ལ་ཉོན་མོངས༌[^1628]གསུམ་མོ། །

[Block 2928]
ཡན་ལག་གསུམ་ནི་ཉོན་མོངས་པའི་རང་བཞིན་ཅན་ཏེ།[^1629] མ་རིག་པ་དང་། སྲེད་པ་དང་། ལེན་པ་རྣམས་སོ། །

[Block 2929 [HEADING]]
###### ལས། ^3-1-11-4-2-0

[Block 2930]
ལས་གཉིས་སོ། །

[Block 2931]
ཡན་ལག་གཉིས་ནི་ལས་ཀྱི་རང་བཞིན་ཡིན་ཏེ། འདུ་བྱེད་དང་། སྲིད་པའོ། །

[Block 2932 [HEADING]]
###### གཞི། ^3-1-11-4-3-0

[Block 2933]
གཞི༌[^1630]བདུན། ཡན་ལག་བདུན་པོ་རྣམ་པར་ཤེས་པ་དང་། མིང་དང་། གཟུགས་དང་། སྐྱེ་མཆེད་དྲུག་དང་། རེག་པ་དང་། ཚོར་བ་དང་། སྐྱེ་བ་དང་། རྒ་ཤི་རྣམས་ནི་ལས་དང་ཉོན་མོངས་པའི་རྟེན་ཡིན་པའི་ཕྱིར་གཞིའི་ཡན་ལག་ཡིན་ནོ། །

[Block 2934]
ཇི་ལྟར་ཡན་ལག་བདུན་གཞི༌[^1631]ཡིན་པ་དེ་བཞིན་འབྲས་བུ་ཡིན། ཡན་ལག་བདུན་པོ་ཉིད་འབྲས་བུར་གྱུར་པ་དག་ཡིན་ནོ། །

[Block 2935]
ལྷག་མ་ལྔ་ནི་ལས་དང་ཉོན་མོངས་པའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རྒྱུར་གྱུར་པ་དག་ཡིན་ནོ། །

[Block 2936]
ཡང་ཅིའི་ཕྱིར་གཞི་རྣམ་པ་ལྔ་དང་ཉོན་མོངས་པ་རྣམ་པ་གཉིས་ཐ་དད་པའི་ཕྱིར་དབུས་སུ་ནི་རྒྱུ་དང་འབྲས་བུ་དག་རྒྱ་ཆེར་བསྐྱེད༌[^1632]ལ། མ་འོངས་པའི་དུས་སུ༌[^1633]ནི་རྣམ་པ་གཉིས་ཐ་དད་པའི་ཕྱིར་འབྲས་བུ་མདོར་བསྡུས། འདས་པའི་དུས་སུ་ནི་ཉོན་མོངས་པ༌[^1634]སྒོ་གཅིག་ཏུ་བསྟན་པའི་ཕྱིར་རྒྱུ་མདོར་བསྡུས་ཤེ་ན།

[Block 2937]
གཉིས་ཀྱི་རྒྱུ་འབྲས་མདོར་བསྡུས་པ། །བར་མའི་རྗེས་སུ་དཔག་པ་ལས།

[Block 2938]
[^1635] །བར་མ་ཁོ་ནས་སྔོན་གྱི་མཐའ་དང་ཕྱི་མའི་མཐའ་དག་གི་རྒྱུ་དང་འབྲས་བུ་རྒྱས་པར་རྗེས་སུ་དཔག་པར་ནུས་པས་མ་བཤད་དེ། ཡང་དོན་མེད་པའི་འབད་པ་མ་བྱས་སོ། །

[Block 2939 [HEADING]]
##### སྲིད་པའི་ཡན་ལག་ལུགས། ^3-1-11-5-0

[Block 2940]
གལ་ཏེ་ཡང་རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་ཡན་ལག་བཅུ་གཉིས་ཁོ་ན་ཡིན་ན་དེ་ལྟ་ན་གོ། །

[Block 2941]
མ་རིག་པའི་རྒྱུ་མ་བསྟན་པའི་ཕྱིར་འཁོར་བ་ཐོག་མ་ཅན་དུ་ཡང་འགྱུར༌[^1636]ལ། རྒ་ཤིའི་འབྲས་བུ་མ་བསྟན་པའི་ཕྱིར་མཐའ་དང་ལྡན་པར་ཡང་འགྱུར་བའམ། ཡང་ན་ནི་ཡན་ལག་གཞན་གྱིས་ཁ་བསྐང་དགོས་སོ། །

[Block 2942]
དེ་ལ་ཡང་གཞན་ཞིག་ཡོད་ན་ནི་ཐུག་པ་མེད་པར་འགྱུར་རོ་ཞེ་ན། ཁ་བསྐང་བར་བྱ་མི་དགོས་ཏེ། འདི་ལྟར་འདིར་བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 2943 [VERSE]]
ཉོན་མོངས་པ་ལས་ཉོན་མོངས་དང་། །
བྱ་བ་ཉིད་དོ་དེ་ལས་གཞི། །

[Block 2944]
དེ་ལས་གཞི་དང་ཉོན་མོངས་སྐྱེས།[^1637] །འདི་ནི་སྲིད་པའི་ཡན་ལག་ལུགས། །ཞེས་བསྟན་ཟིན་ཏོ། །

[Block 2945]
ཉོན་མོངས་པ་ལས་ཉོན་མོངས་པ་སྐྱེ༌[^1638]སྟེ། སྲེད་པ་ལས་ལེན་པའོ། །
--- END BLOCKS ---
