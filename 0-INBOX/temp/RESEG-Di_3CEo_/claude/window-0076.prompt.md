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
[Block 2661 [VERSE]]
རིགས་པས༌[^1062]རབ་ཏུ་བཅུག་པའི་ལས། །
རྣམ་གསུམ་ཀུན་སློང་བཅས་པ་ནི། །
ཡིག་འབྲུ་རྒྱ༌[^1063]དང་བགྲངས་བཅས་པའི། །
སྙན་དངག་གྲངས་ཏེ་གོ་རིམས་བཞིན། །

[Block 2662]
རིགས་པས་བཅུག་པ་ཞེས་བྱ་བ་ནི་ཐབས་ཀྱི་བྱེ་བྲག་གིས་བཅུག་པའོ། །

[Block 2663]
ལས་རྣམ་གསུམ་ཞེས་བྱ་བ་ནི། ལུས་དང་། ངག་དང་། ཡིད་ཀྱི་ལས་སོ། །

[Block 2664]
དེ་ལ་རེ་ཞིག་ཡིག༌[^1064]འབྲུ་དང་། རྒྱ་ནི་ལུས་ཀྱི་ལས་རིགས་པས་རབ་ཏུ་བཅུག་པ་ཀུན་ནས་སློང་བ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 2665]
བགྲང་བ་དང་སྙན་ངག་ནི་ངག་གི་ལས་ཏེ། དེ་ལྟ་ན་དེ་དག་ནི་ཕུང་པོ་ལྔའི་རང་བཞིན་ཡིན་ནོ། །

[Block 2666]
གྲངས་ནི་ཡིད་ཀྱི་ལས་ཏེ། ཡིད་ཀྱིས་ཆོས་རྣམས་སྡོམ་པར་བྱེད་པ་གང་ཡིན་པའོ། །

[Block 2667 [HEADING]]
#### ཆོས་ཀྱི་རྣམ་གྲངས། ^4-3-17-0

[Block 2668]
ད་ནི་ཆོས་ཀྱི་རྣམ་གྲངས་ཁ་ཅིག་བརྗོད་པར་བྱ་སྟེ། བསྒྲིབས་ངན་ཁ་ན་མ་ཐོ་བཅས། །ཉོན་མོངས་ཅན་ཆོས། ཉོན་མོངས་པ་ཅན་གྱི་ཆོས་རྣམས་ཀྱི་རྣམ་གྲངས་དག་གོ། །

[Block 2669]
དྲི་མེད་དགེ་གྱ་ནོམ། གྱ་ནོམ་པ་ཞེས་བྱ་བ་ནི་དགེ་བ་ཟག་པ་མེད་པའི་རྣམ་གྲངས་ཡིན་ནོ། །

[Block 2670]
ངན་པ་དང་གྱ་ནོམ་པ་ལས་གཞན་པའི་བར་མ་ཞེས་བྱ་བར་གྲུབ་བོ། །

[Block 2671]
འདུས་བྱས་དགེ་བསྟན་བྱ། བསྟེན་པར་བྱ་བ་ཞེས་བྱ་བ་ནི་འདུས་བྱས་ཀྱི་ཆོས་དགེ་བ་རྣམས་ཀྱི་རྣམ་གྲངས་ཡིན་ནོ། །

[Block 2672]
ལྷག་མ་རྣམས་ནི་བསྟན་པར༌[^1065]བྱ་བ་མ་ཡིན་པར་འགྲུབ༌[^1066]བོ། །

[Block 2673]
ཆོས་གཞན་ཐམས་ཅད་ནི་བླ་མ་དང་བཅས་པ་ཡིན་གྱི། ཐར་པ་བླ་ན་མེད་པ་ཡིན། །མྱ་ངན་ལས་འདས་པ་ལས་ཆེས་ཁྱད་པར་དུ་འཕགས་པ་ནི་མེད་ཀྱི་དེ་ནི་དགེ་བ་དང་རྟག་པ་ཡིན་པའི་ཕྱིར་ཐམས་ཅད་ལས་ཁྱད་པར་དུ་འཕགས་པ་ཡིན་ནོ། །

[Block 2674]
ལས་བསྟན་པ་ཞེས་བྱ་བ་མཛོད་ཀྱི་གནས་བཞི་པའོ།། །།

[Block 2675 [HEADING]]
## ཕྲ་རྒྱས་བསྟན་པ། ^5-0

[Block 2676]
ལས་ལས་འཇིག་རྟེན་སྣ་ཚོགས་སྐྱེས། །ཞེས་བཤད་པ་དེ་དག་ཀྱང་ཕྲ་རྒྱས་ཀྱི་དབང་གིས་བསགས་པར་འགྱུར་གྱི། ཕྲ་རྒྱས་མེད་པར་ནི་སྲིད་པ་མངོན་པར་འགྲུབ་པར་མི་ནུས་པས་དེའི་ཕྱིར། སྲིད་པའི་རྩ་བ་ཕྲ་རྒྱས་སུ་རིག་པར་བྱའོ། །

[Block 2677 [HEADING]]
### ཕྲ་རྒྱས་དྲུག། ^5-1-0

[Block 2678]
དེ་ཡང་དྲུག །

[Block 2679 [VERSE]]
འདོད་ཆགས་དེ་བཞིན་ཁོང་ཁྲོ་དང་། །
ང་རྒྱལ་མ་རིག་ལྟ་བ་དང་། །

[Block 2680]
ཐེ་ཚོམ་ཡིན་ཏེ། དེ་བཞིན་ཞེས་སྨོས་པ་ནི་འདོད་ཆགས་ཀྱི་དབང་གིས་གཞན་དག་དམིགས་པ་ལ། རྒྱས་པར་འགྱུར་བ་ཉིད་ཤེས་པར་བྱ་བའི་དོན་དུའོ། །

[Block 2681 [HEADING]]
#### འདོད་ཆགས་དབྱེ་བས་བདུན། ^5-1-1-0

[Block 2682]
དེ་དྲུག་ཀྱང་། འདོད་ཆགས་དབྱེ་བས་བདུན་དུ་བཤད། །གང་གི་ཕྱིར། ཁམས་གཉིས་ལས་སྐྱེས་སྲིད་འདོད་ཆགས། །གཟུགས་དང་གཟུགས་མེད་པའི་ཁམས་ནས་སྐྱེས་པའི་འདོད་ཆགས་ནི་སྲིད་པའི་འདོད་ཆགས་སོ། །

[Block 2683]
འདོད་པར་གཏོགས་པའི་ནི་འདོད་པའི་འདོད་ཆགས་སོ། །

[Block 2684]
ཡང་ཅིའི་ཕྱིར་གཟུགས་དང་གཟུགས་མེད་པའི་འདོད་ཆགས་ནི་སྲིད་པའི་འདོད་ཆགས་ཞེས་བྱ་ཞེ་ན།

[Block 2685 [VERSE]]
ཁ་ནི་ནང་དུ་བལྟས་ཕྱིར་དེ། །
ཐར་པའི་འདུ་ཤེས་བཟློག་ཕྱིར་བཤད། །

[Block 2686]
དེ་དག་ནི་ཕལ་ཆེར་སྙོམས་པར་འཇུག་པ་ལ་འདོད་ཆགས་པ་ཡིན་ལ། དེ་ཡང་ཁ་ནང་དུ་བལྟས་པ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་གཅིག་ཏུ་བྱས་སོ། །

[Block 2687]
ཁམས་དེ་གཉིས་ལ་ཐར་པ་ཡིན་ནོ་སྙམ་པའི་འདུ་ཤེས་བཟློག་པའི་ཕྱིར་སྲིད་པའི་འདོད་ཆགས་ཞེས་ཀྱང་གསུངས་སོ། །

[Block 2688 [HEADING]]
#### ཕྲ་རྒྱས་བཅུ། ^5-1-2-0

[Block 2689]
ཡང་ཕྲ་རྒྱས་དྲུག་པོ་དེ་དག་བཅུར་ཡང་འཆད་དེ། ཇི་ལྟར་བྱས་ནས་ཤེ་ན།

[Block 2690 [VERSE]]
ལྟ་བ་ལྔ་སྟེ་འཇིག་ཚོགས་དང་། །
ལོག་དང་མཐར་འཛིན་ལྟ་བ་དང་། །
ལྟ་བ་དང་ནི་ཚུལ་ཁྲིམས་དང་། །
བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་དང་བཅུ། །

[Block 2691]
ཕྲ་རྒྱས་དྲུག་ལས་ལྟ་བ་རྣམ་པ་ལྔར་བྱས་ནས་བཅུར་འགྱུར་རོ། །

[Block 2692 [HEADING]]
#### དགུ་བཅུ་རྩ་བརྒྱད། ^5-1-3-0

[Block 2693]
ཡང་འདི་དག་བཅུ་པོ་ལས་དགུ་བཅུ་རྩ་བརྒྱད་དུ་འཆད་དེ། འདི་ལྟ་སྟེ།

[Block 2694 [VERSE]]
དེ་དག་བཅུ་དང་བདུན་བདུན་བརྒྱད། །
ལྟ་བ་གསུམ་གཉིས་མ་གཏོགས་པ། །
འདོད་ན་སྡུག་བསྔལ་ལ་སོགས་པ། །
མཐོང་བས་རིམ་བཞིན་སྤོང་བར་བྱེད། །

[Block 2695]
ཕྲ་རྒྱས་བཅུར་བཤད་པ་གང་དག༌[^1067]ཡིན་པ་དེ་དག་འདོད་པའི་ཁམས་ན་སྡུག་བསྔལ་མཐོང་བས་སྤང༌[^1068]བར་བྱ་བ་ནི་བཅུར༌[^1069]ཡོད་དོ། །

[Block 2696]
དེ་དག་ཉིད་ལས་ཀུན་འབྱུང་བ་མཐོང་བས་སྤོང་བར༌[^1070]བྱ་བ་བདུན་དང་། འགོག་པ་མཐོང་བས་སྤོང་བར༌[^1071]བྱ་བ་བདུན་ཏེ། འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། ཚུལ་ཁྲིམས༌[^1072]དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པ་མ་གཏོགས་སོ། །

[Block 2697]
ལམ་མཐོང་བས་སྤང་བར་བྱ་བ་ནི་བརྒྱད་དེ། འཇིག་ཚོགས་ལ་ལྟ་བ་དང་། མཐར་འཛིན་པར་ལྟ་བ་མ་གཏོགས་སོ། །

[Block 2698]
དེ་ལྟར་ན༌[^1073]འདོད་པ་ན་སྤྱོད་པའི་ཕྲ་རྒྱས་སུམ་ཅུ་རྩ་གཉིས་ཡིན་ནོ། །

[Block 2699]
དེ་བཞིན་དུ་གཟུགས་ཀྱི་ཁམས་ན་ཉི་ཤུ་རྩ་བརྒྱད། གཟུགས་མེད་པའི་ཁམས་ན་ཉི་ཤུ་རྩ་བརྒྱད་ཡིན་ནོ། །

[Block 2700]
འདོད་པའི་ཁམས་ན་མཐོང་བས་སྤོང་བར༌[^1074]བྱ་བ་སོ་གཉིས་ཡིན་ལ། བཞི་ནི་བསྒོམ་པས་སྤང༌[^1075]བྱ་ཡིན། །འདི་ལྟ་སྟེ། འདོད་ཆགས་དང་། ཁོང་ཁྲོ་བ་དང་། མ་རིག་པ་དང་། ང་རྒྱལ་ཏོ། །
--- END BLOCKS ---
