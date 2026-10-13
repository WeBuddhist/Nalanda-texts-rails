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
མདོ་ལས་འདུ་ཤེས་དང་། སེམས་དང་། ལྟ་བ་ཕྱིན་ཅི་ལོག་ཏུ་གསུངས་པ་དེ་ལ་ལྟ་བ་ཁོ་ན་ཕྱིན་ཅི་ལོག་ཡིན་ལ། སེམས་དང་འདུ་ཤེས་དེའི་དབང་གིས། །ལྟ་བ་ཕྱིན་ཅི་ལོག་གི་དབང་གིས་འདུ་ཤེས་དང་སེམས་ཕྱིན་ཅི་ལོག་ཏུ་བཤད་དོ། །

[Block 2732 [HEADING]]
### ང་རྒྱལ་བདུན། ^5-3-0

[Block 2733]
ཡང་ལྟ་བའི་ཕྲ་རྒྱས་ཁོ་ན་ལ་དབྱེ་བ་ཡོད་ཀྱི་གཞན་ལ་མེད་དམ་ཞེ་ན། ཡོད་པ་འདི་ལྟ་སྟེ། ང་རྒྱལ་བདུན། ང་རྒྱལ་དང་། ལྷག་པའི་ང་རྒྱལ་དང་། ང་རྒྱལ་ལས་ཀྱང་ང་རྒྱལ་དང་། ངའོ་སྙམ་པའི་ང་རྒྱལ་དང་། མངོན་པའི་ང་རྒྱལ་དང་། ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་དང་། ལོག་པའི་ང་རྒྱལ་ལོ། །

[Block 2734]
དེ་ལ་ཆུང་ངུ་ལས་བདག་ཁྱད་པར་དུ་འཕགས་པའམ་མཉམ་པ༌[^1085]དང་མཉམ་མོ་སྙམ་དུ་སེམས་ཁེངས་པ་ནི་ང་རྒྱལ་ལོ། །

[Block 2735]
མཉམ་པ་བས་བདག་ཁྱད་པར་དུ་འཕགས་སོ་སྙམ་པ་ནི་ལྷག་པའི་ང་རྒྱལ་ལོ། །

[Block 2736]
ཁྱད་པར་དུ་འཕགས་པ་བས་ཀྱང་བདག་ཁྱད་པར་དུ་འཕགས་སོ་སྙམ་པ་ནི་ང་རྒྱལ་ལས་ཀྱང་ང་རྒྱལ་ལོ། །

[Block 2737]
འཇིག་ཚོགས་ལ་ལྟ་བ་སྔོན་དུ༌[^1086]འགྲོ་བས་ངའོ་སྙམ་པ་ནི་ངའོ་སྙམ་པའི་ང་རྒྱལ་ལོ། །

[Block 2738]
རྟོགས་པའི་ཁྱད་པར་མ་ཐོབ་པ་ལ་བདག་གིས་ཐོབ་བོ་སྙམ་པ་ནི་མངོན་པའི་ང་རྒྱལ་ལོ། །

[Block 2739]
ཆེས་ཁྱད་པར་དུ་འཕགས་པ་བས་བདག་ཅུང་ཟད་ཅིག༌[^1087]གིས་དམན་ནོ་སྙམ་པ་ནི་ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་ལོ། །

[Block 2740]
ཡོན་ཏན་མ་ཡིན་པ་དང་ལྡན་པ་ལ་བདག་ནི་ཡོན་ཏན་དང་ལྡན་ནོ་སྙམ་པ་ནི་ལོག་པའི་ང་རྒྱལ་ལོ། །

[Block 2741]
བསྟན་བཅོས་ལས་ང་རྒྱལ་གྱི༌[^1088]རྣམ་པ་དགུ་གང་དག་བཤད་པ་དེ་དག་ནི། རྣམ་དགུ་གསུམ་པོ། །དེ་ལ་དང་པོ་གསུམ་ནི་བདག་མཆོག་དང་མཉམ་པ་དང་། དམན་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ལྟ་བ་ལ་བརྟེན་པ༌[^1089]གསུམ་ནི་ལྷག་པའི་ང་རྒྱལ་དང་། ང་རྒྱལ་དང་། ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་དག་གོ། །

[Block 2742]
གཉིས་པའི་གསུམ་ནི་བདག་བས་མཆོག་དང་། མཉམ་པ་དང་། དམན་པ་ཡོད་དོ་ཞེས་བྱ་བ་ནི་ཅུང་ཟད་སྙམ་པའི་ང་རྒྱལ་དང་། ང་རྒྱལ་དང་། ལྷག་པའི་ང་རྒྱལ་རྣམས་སོ། །

[Block 2743]
གསུམ་པའི་གསུམ་ནི་བདག་པས་མཆོག་དང་། མཉམ་པ་དང་། དམན་པ་མེད་དོ་ཞེས་བྱ་བ་ནི་ང་རྒྱལ་དང་། ལྷག་པའི་ང་རྒྱལ་དང་། ཅུང་ཟད་སྙམ་པའི༌[^1090]ང་རྒྱལ་དག་གོ། །

[Block 2744]
ཡང་ང་རྒྱལ་བདུན་པོ་འདི་དག་ཅི་ཞིག་གིས་སྤང་བར་བྱ་བ་ཡིན་ཞེ་ན། མཐོང་དང་བསྒོམ་པས་ཟད་བྱ་བ། །ཅི་འཕགས་པ་རྣམས་ལ་བསྒོམ་པས་སྤང་བར་བྱ་བ་མ་སྤངས་པ་གང་ཡིན་པ་དེ་ཀུན་དུ་སྤྱོད༌[^1091]དམ་ཞེ་ན། ངེས་པ་མེད་དེ། འདི་ལྟར་བསྒོམ་པས༌[^1092]སྤང་བར་བྱ་བ་ནི། །གསོད་སོགས་ཀུན་ནས་དཀྲིས་པའོ། །

[Block 2745]
ཉོན་མོངས་པ་ཀུན་ནས༌[^1093]དཀྲིས་པ་གང་གིས་ཆེད་དུ་བསམས་ཏེ། སྲོག་གཅོད་པར་བྱེད་པ་ནས་བརྫུན་དུ་སྨྲ་བར་བྱེད་པའི་བར་དེ་ནི་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 2746]
དེ་བཞིན་འཇིག་སྲེད། འཇིག་པའི་སྲེད་པ་ཡང་བསྒོམ་པས་སྤང་བར་བྱ་བ་ཡིན་ནོ། །

[Block 2747]
བསྒོམ་པས་སྤང་བར་བྱ་བ་ནི་ང་རྒྱལ་གྱི་རྣམ་པ་རྣམས་ཀྱང་ཡོད་དོ་ཞེས་བཤད་པ་ལ་ངའོ་སྙམ་པའི་ང་རྒྱལ་ཡང་ཡོད་མོད་ཀྱི། འཕགས་པ་ལ། རྣམ་སོགས་ངའོ་སྙམ་མི་འབྱུང་། །སོགས་པ་སྨོས་པས་ནི་འཇིག་པའི་སྲེད་པའི་བར་དུ་གཟུང་ངོ་། །ཅིའི་ཕྱིར་དེ་དག་མ་སྤངས་ཀྱང་མི་འབྱུང་ཞེ་ན། ལྟ་བས་རྒྱས་པར་འགྱུར་ཕྱིར་རོ། །

[Block 2748]
ང་རྒྱལ་གྱི་རྣམ་པ་རྣམས་དང་། ངའོ་སྙམ་པའི་ང་རྒྱལ་ནི་འཇིག་ཚོགས་ལ་ལྟ་བས་རྒྱས་པར་འགྱུར་རོ། །

[Block 2749]
དེ་བས་ན་འཇུག་པ་ཆད་པའི་ཕྱིར་ཡང་ལྡང་བར་མི་ནུས་སོ། །

[Block 2750]
གསོད་པ་ལ་སོགས་པའི་ཀུན་ནས་དཀྲིས་པ་ནི་ལོག་པར་ལྟ་བས་རྒྱས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2751]
འཇིག་པའི་སྲེད་པ༌[^1094]ཆད་པར་ལྟ་བས་རྒྱས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2752]
སྐྱེ་བའི་སྲེད་པའི་ཕྱོགས་ནི་རྟག་པར་ལྟ་བས༌[^1095]རྒྱས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2753]
མི་དགེའི་འགྱོད་པའང་མ་ཡིན་ནོ། །

[Block 2754]
འགྱོད་པ་ནི་མི་དགེ་བ་ཡང་བསྒོམ་པས་སྤང་བར་བྱ་བ་མ༌[^1096]ཡིན་ན་འཕགས་པ་ལ་དེ་མི་འབྱུང་སྟེ། ཐེ་ཚོམ་གྱིས་ཀུན་ནས་བསླང་བ༌[^1097]ཡིན་པའི་ཕྱིར་རོ། །

[Block 2755 [HEADING]]
### ཀུན་དུ་འགྲོ་བ་དང་ཀུན་དུ་འགྲོ་བ་མ་ཡིན་པ། ^5-4-0

[Block 2756]
ཡང་ཕྲ་རྒྱས་དེ་དག་ལས།

[Block 2757]
དུ༌[^1098]ཀུན་དུ་འགྲོ་བ་དང་། ཀུན་དུ་འགྲོ་བ་མ་ཡིན་པ་ནི་དུ་ཞེ་ན།

[Block 2758 [VERSE]]
སྡུག་བསྔལ་རྒྱུ་མཐོང་སྤང་བྱ་བ། །
ལྟ་དང་དེ་བཞིན་ཐེ་ཚོམ་དང་། །
གང་དེ་ལྷན་ཅིག་མ་འདྲེས་པའི། །
མ་རིག་གང་ཡིན་ཀུན་དུ་འགྲོ། །

[Block 2759]
དེ་ལྟར་ན་ལྟ་བ་བདུན་དང་། ཐེ་ཚོམ་གཉིས་དང་། མ་རིག་པ་གཉིས་དང་། ཕྲ་རྒྱས་བཅུ་གཅིག་པོ་དེ༌[^1099]དག་ནི་རང་གི་ཁམས་མཐའ་དག་ལ་དམིགས་པའི་ཕྱིར་སྐལ་བ༌[^1100]མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 2760]
དེ་དག་ལས་དགུ་གོང་དུ་དམིགས། ལྟ་བ་གཉིས་པོ་མ་གཏོགས་སོ། །

[Block 2761]
འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། མཐར་འཛིན་པར་ལྟ་བ་མ་གཏོགས་པ་ཕྲ་རྒྱས་གཞན་དགུ་ནི་སྐལ་བ༌[^1101]མི་མཉམ་པའི་ཁམས་ཀུན་དུ་འགྲོ་བ་དག་ཡིན་ནོ། །

[Block 2762]
ཕྲ་རྒྱས་ཀུན་དུ༌[^1102]འགྲོ་བ་མ་ཡིན་ཏེ། འོན་ཀྱང་།

[Block 2763 [VERSE]]
དེ་དག་དང་ནི་ལྷན་ཅིག་དང་། །
འབྱུང་དེའང་ཀུན་འགྲོ༌[^1103]ཐོབ་མ་གཏོགས། །

[Block 2764]
ཐོབ་པ་རྣམས་ནི་འབྲས་བུ་དུ་མའི་ཕྱིར་འདི་དག་ཏུ་མ་གཏོགས་སོ། །

[Block 2765 [HEADING]]
### ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་དང་ཟག་པ་མེད་པ་ལ་དམིགས་པ། ^5-5-0

[Block 2766]
ཕྲ་རྒྱས་འདི་དག་ལས་ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་དང་། ཟག་པ་མེད་པ་ལ་དམིགས་པ་ནི༌[^1104]དུ་ཞེ་ན།

[Block 2767 [VERSE]]
འགོག་དང་ལམ་མཐོང་སྤང་བྱ་བ། །
ལོག་ལྟ་ཐེ་ཚོམ་དེ་དག་དང་། །
ལྡན་དང་འབའ་ཞིག་མ་རིག་དང་། །
དྲུག་ནི་ཟག་མེད་སྤྱོད་ཡུལ་ཅན། །

[Block 2768]
ལྷག་མ་རྣམས་ནི་ཟག་པ་དང་བཅས་པ་ལ་དམིགས་པ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 2769]
དེ་ལ་ཡང་།

[Block 2770 [VERSE]]
རང་གི་ས་པའི་འགོག་པ་དང་། །
ལམ་ནི་ཕན་ཚུན་རྒྱུ་ཡིན་པས། །
ས་དྲུག་ས་དགུའི་ལམ་ནི་དེའི། །
སྤྱོད་ཡུལ་ཅན་གྱི་ཡུལ་ཡིན་ནོ། །
--- END BLOCKS ---
