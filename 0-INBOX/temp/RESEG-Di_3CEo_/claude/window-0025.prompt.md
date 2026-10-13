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
[Block 876]
སེམས་ལས་བྱུང་བ་ཐམས་ཅད་དང་། བསམ་གཏན་གྱི་སྡོམ་པ་དང་། ཟག་པ་མེད་པའི་སྡོམ་པ་དང་། དེ་དག་དང་། སེམས་ཀྱི་སྐྱེ་བ་ལ་སོགས་པ་གང་ཡིན་པའི་ཆོས་དེ་དག་ནི་སེམས་ཀྱི་རྗེས་སུ་འཇུག་པ་ཞེས་བྱའོ། །

[Block 877]
དེ་དག་ཇི་ལྟར་སེམས་ཀྱི་རྗེས་སུ་འཇུག་ཅེ་ན། མདོར་བསྡུ་ན། དུས་དང་ནི། འབྲས་སོགས་དགེ་ལ་སོགས་པས་སོ། །

[Block 878]
རེ་ཞིག་དུས་ལས་ནི། སེམས་དང་ལྷན་ཅིག་སྐྱེ་བ་དང་། །གནས་པ་དང་། འགག་པ་གཅིག་པ་ཉིད་དང་། དུས་གཅིག་ཏུ་གཏོགས་པ་ཉིད་ཀྱིས་སོ། །

[Block 879]
འབྲས་བུ་ལ་སོགས་པས་ནི། འབྲས་བུ་དང་། རྣམ་པར་སྨིན་པ་དང་། རྒྱུ་མཐུན་པ་གཅིག་པ་ཉིད་ཀྱིས་ཏེ། དགེ་བ་ལ་སོགས་པས་ནི་དགེ་བ་ལ་སོགས་པའི་སེམས་ལ་དགེ་བ་ལ་སོགས་པ་ཉིད་ཀྱིས་སོ། །

[Block 880]
ལྷན་ཅིག་འབྱུང་བའི་རྒྱུ་བཤད་ཟིན་ཏོ། །

[Block 881 [HEADING]]
##### སྐལ་བ་མཉམ་པའི་རྒྱུ། ^2-3-1-3-0

[Block 882]
སྐལ་མཉམ་རྒྱུ་ནི་འདྲ་བའོ། །

[Block 883]
ཆོས་འདྲ་བ་རྣམས་ནི་ཆོས་འདྲ་བ་རྣམས་ཀྱི་སྐལ་པ་མཉམ་པའི་རྒྱུ་སྟེ། འདི་ལྟ་སྟེ། དགེ་བའི་ཕུང་པོ་ལྔ་པོ་དག་ནི་དགེ་བ་རྣམས་ཀྱི་ཡིན་ནོ། །

[Block 884]
དེ་བཞིན་དུ་ཉོན་མོངས་པ༌[^335]ཅན་དང་ལུང་དུ་མ་བསྟན་པ་དག་གོ། །ཅི་ཐམས་ཅད་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ། རང་རིས་ས་པའོ། །

[Block 885]
རིས་ནི་ལྔ་སྟེ། སྡུག་བསྔལ་མཐོང་བས་སྤང་བར་བྱ་བ་ནས་བསྒོམ་པས་སྤང་བར་བྱ་བའི༌[^336]བར་རོ། །

[Block 886]
ས་ནི་དགུ་སྟེ། འདོད་པའི་ཁམས་དང་། བསམ་གཏན་དང་གཟུགས་མེད་པ་བརྒྱད་དོ། །

[Block 887]
འདི་དག་ནི་རང་གི་རིས་དག་དང་རང་གི་ས་པ་ཡིན་ཏེ། རང་གི་རིས་རྣམས་ཀྱི་སྐལ་བ་མཉམ་པའི་རྒྱུ་སྟེ། དེ་དག་ཀྱང་ཐམས་ཅད་མ་ཡིན་ནོ། །

[Block 888]
འོན་ཀྱང་། སྔར་སྐྱེས་པ༌[^337]རྣམས་སྔར་སྐྱེས་པ་རྣམས་ནི་ཕྱི་མ་སྐྱེས་པ་དང་མ་སྐྱེས་པ་རྣམས་ཀྱི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ན། །[^338]མ་འོངས་པ་ཁོ་ན་སྐལ་བ་མཉམ་པའི་རྒྱུ་མ༌[^339]ཡིན་ནོ། །

[Block 889]
སྐལ་བ་མཉམ་པའི་རྒྱུ་ནི་རང་གི་ས་པ་ཡིན་ནོ་ཞེས་བཤད་པ་གང་ཡིན་པ་དེ་ཇི་ལྟར་ངེས་སམ་ཞེ་ན། དེ་ཟག་པ་དང་བཅས་པ་ནི་ངེས་སོ། །

[Block 890]
ས་དགུའི་ལམ་ནི་ཕན་ཚུན་དུ། སྐལ་པ་མཉམ་པའི་རྒྱུ་ཡིན་ནོ་ཞེས་བྱ་བར་སྐབས་དང་སྦྱར་ཏེ། མི་ལྕོགས་པ་མེད་པ་དང་། བསམ་གཏན་ཁྱད་པར་ཅན་དང་། བསམ་གཏན་བཞི་དང་། གཟུགས་མེད་པ་གསུམ་དག་གི་ལམ་གྱི་བདེན་པ་ནི་ཕན་ཚུན་དུ༌[^340]སྐལ་པ་མཉམ་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 891]
འདི་ནི་ས་དེ་དག་ཏུ་གློ་བུར་དུ་འོངས་པ་ཡིན་ལ་ཁམས་དེ་དག་ཏུ་གཏོགས་པ་མ་ཡིན་ཏེ། དེ་ཡང་།

[Block 892 [VERSE]]
མཉམ་དང་ཁྱད་པར་ཅན་གྱི་ཡིན། །
ཆུང་ངུའི་རྒྱུ་ནི་མ་ཡིན་ནོ། །

[Block 893]
ཅི་ལམ་ཁོ་ན་མཉམ་པ་དང་ཁྱད་པར་ཅན་དག་གི་སྐལ་བ་མཉམ་པའི་རྒྱུ་ཡིན་ནམ་ཞེ་ན། སྨྲས་པ། མ་ཡིན་ཏེ། འཇིག་རྟེན་པ་དག་ཀྱང་།

[Block 894 [VERSE]]
སྦྱོར་བྱུང་དེ་གཉིས་ཁོ་ནའི་ཡིན། །
ཐོས་དང་བསམས༌[^341]བྱུང་ལ་སོགས་པ། །

[Block 895]
ཐོས་པ་དང་། བསམས་པ༌[^342]དང་། བསྒོམས་པ་ལས་བྱུང་བ་སྦྱོར་བ་ལས་བྱུང་བའི་ཡོན་ཏན་དེ་དག་ཀྱང་མཉམ་པ་དང་ཁྱད་པར་ཅན་དག་ཁོ་ནའི་རྒྱུ་ཡིན་གྱི་དམན་པ་རྣམས་ཀྱི་ནི་མ་ཡིན་ནོ། །

[Block 896]
སྐལ་བ་མཉམ་པའི་རྒྱུ་བཤད་ཟིན་ཏོ། །

[Block 897 [HEADING]]
##### མཚུངས་པར་ལྡན་པའི་རྒྱུ། ^2-3-1-4-0

[Block 898 [VERSE]]
མཚུངས་ལྡན་རྒྱུ་ནི་སེམས་དག་དང་། །
སེམས་བྱུང་རྟེན་མཚུངས་ཅན་རྣམས་སོ། །

[Block 899]
གང་དག་ལ་རྟེན་མཚུངས་པ་ཐ་མི་དད་པར་ཡོད་པའི་སེམས་དང་སེམས་ལས་བྱུང་བ་དེ་དག་ནི་ཕན་ཚུན་མཚུངས་པར་ལྡན་པའི་རྒྱུ་ཡིན་ནོ། །

[Block 900 [HEADING]]
##### ཀུན་དུ་འགྲོ་བའི་རྒྱུ། ^2-3-1-5-0

[Block 901 [VERSE]]
ཀུན་འགྲོ་ཞེས་བྱ་ཉོན་མོངས་ཅན། །
རྣམས་ཀྱི་རང་སར་ཀུན་འགྲོ་ལྔ། །

[Block 902]
ཀུན་དུ་འགྲོ་བའི་ཆོས་སྔར་སྐྱེས་པ་རྣམས༌[^343]ནི་ཉོན་མོངས་པའི་ཆོས་ཕྱི་མ་རྣམས་ཀྱི་ཀུན་དུ་འགྲོ་བའི་རྒྱུ་ཡིན་ནོ། །

[Block 903]
དེ་དག་ཀྱང་འོག་ཏུ་བཤད་པར་བྱའོ། །

[Block 904]
འདི་ནི་ཉོན་མོངས་པ་ཅན་གྱི་ཆོས་ཀྱི༌[^344]ཐུན་མོང་གི་རྒྱུ་ཡིན་པས་ན། སྐལ་བ་མཉམ་པའི་རྒྱུ་ལོགས་ཤིག་ཏུ་རྣམ་པར་གཞག་སྟེ། རིས་གཞན་དག་གི་ཡང་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 905]
ཀུན་དུ་འགྲོ་བའི་རྒྱུ་བཤད་ཟིན་ཏོ། །

[Block 906 [HEADING]]
##### རྣམ་པར་སྨིན་པའི་རྒྱུ། ^2-3-1-6-0

[Block 907 [VERSE]]
རྣམ་སྨིན་རྒྱུ་ནི་མི་དགེ་དང་། །
དགེ་བ་ཟག་བཅས་རྣམས་ཁོ་ན། །

[Block 908]
ལུང་མ་བསྟན་པ་མ་ཡིན་ཏེ། སྟོབས་ཆུང་བའི་ཕྱིར་ས་བོན་རུལ་བ་བཞིན་ནོ། །

[Block 909]
ཟག་པ་མེད་པ་མ་ཡིན་ཏེ། སྲེད་པས་མངོན་པར་མ་བརླན་པའི་ཕྱིར་མངོན་པར་མ་བརླན་པའི་ས་བོན་དྲུང་པོ༌[^345]བཞིན་ནོ། །

[Block 910]
རྒྱུ་རྣམས་བཤད་ཟིན་ཏོ། །

[Block 911 [HEADING]]
#### དུས་ངེས་པ། ^2-3-2-0

[Block 912]
དུས་ངེས་པ་མ་བཤད་པས་དེ་བརྗོད་པ། ཀུན་འགྲོ༌[^346]སྐལ་མཉམ་དུས་གཉིས་པ། །འདས་པ་དང་ད་ལྟར་བྱུང་བ་ཁོ་ནའོ། །

[Block 913]
གསུམ་པོ་དག་ནི་དུས་གསུམ་པ། །ལྷན་ཅིག་འབྱུང་བ་དང་མཚུངས་པར་ལྡན་པ་རྣམས་དང་། རྣམ་པར་སྨིན་པའི་རྒྱུ་དག་ནི་དུས་གསུམ་པ་ཡིན་ནོ། །

[Block 914 [HEADING]]
#### འབྲས་བུ། ^2-3-3-0

[Block 915]
རྒྱུ་དེ་དག་གང་ཡིན་པའི་འབྲས་བུ་དེ་དག་གང་ཞེ་ན། འདུས་བྱས་བྲལ་བཅས་འབྲས་བུ་ཡིན། །དེ་ལྟ་ན་འོ་ན་ནི་འདུས་མ་བྱས་འབྲས་བུ་ཡིན་པའི་ཕྱིར་དེ་དག་གི་འབྲས་བུ་ཡིན་པའི་རྒྱུར་ཡང་འགྱུར་ལ། རྒྱུ་ཡིན་པའི་ཕྱིར་དེ་དག་གི་རྒྱུ་ཡིན་པའི་འབྲས་བུར་ཡང་འགྱུར་རོ། །
--- END BLOCKS ---
