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

[Block 2876]
དེ་ནི་གསུམ་འདུས་ཚུན་ཆད་དོ། །

[Block 2877]
སྐྱེ་མཆེད་དྲུག་དོད་ནས་ཇི་སྲིད་དུ་དབང་པོ་དང་ཡུལ་དང་རྣམ་པར་ཤེས་པ་དང་གསུམ་མ་འདུས་པ་དེ་སྲིད༌[^1600]ཀྱི་གནས་སྐབས་དེ་ནི་སྐྱེ་མཆེད་དྲུག་ཅེས་བྱའོ་ཞེས༌[^1601]རེག་པ་བདེ་སྡུག་ལ་སོགས་ཀྱི༌[^1602]རྒྱུ་ཤེས་ནུས་པ་ཚུན་ཆད་དོ། །

[Block 2878]
རེག་པ་ནི་གསུམ་འདུས་ཏེ་དེས༌[^1603]ཇི་སྲིད་དུ་ཚོར་བ་གསུམ་གྱི་རྒྱུ་ཡོངས་སུ་གཅོད་པར་མ་ནུས་པའི་གནས་སྐབས་དེ་ནི་རེག་པ་ཞེས་བྱའོ། །

[Block 2879]
ཡོངས་སུ་གཅོད་ནུས་ནས་ནི། ཚོར་འཁྲིག་ཚུན་ཆད། ཚོར་བའི་གནས་སྐབས་ནི་ཇི་སྲིད་དུ་འཁྲིག་པའི་འདོད་ཆགས་ཀུན་ཏུ་མི་སྤྱོད་པའི་བར་རོ། །

[Block 2880]
སྲེད་པ་ནི། ལོངས་སྤྱོད་འཁྲིག་པའི་ཆགས་ཅན་གྱི། །འདོད་པའི་ཡོན་ཏན་དང་། འཁྲིག་པའི་འདོད་ཆགས་ཀུན་ཏུ་སྤྱོད་པའི༌[^1604]གནས་སྐབས་ཇི་སྲིད་དུ་ཡུལ་ཡོངས་སུ་ཚོལ་བ་ལ་མ་ཞུགས་པ་ནི་སྲིད་པ༌[^1605]ཞེས་བྱའོ། །

[Block 2881 [VERSE]]
ཉེ་བར་ལེན་པ་ལོངས་སྤྱོད་རྣམས། །
ཐོབ་པར་བྱ་ཕྱིར་ཡོངས་རྒྱུག་པའི། །

[Block 2882]
གནས་སྐབས་གང་དུ་ཡུལ་ཐོབ་པར་བྱ་བའི་ཕྱིར་ཡོངས་སུ་ཚོལ་བ་ལ་ཞུགས་ནས་ཐམས་ཅད་དུ་རྒྱུག་པ༌[^1606]དེ་ནི་ལེན་པ་ཞེས་བྱའོ། །

[Block 2883 [VERSE]]
དེ་ལྟར་ཡོངས་སུ་རྒྱུག་པ་ན། །
དེ་སྲིད་འབྲས་བུ་འབྱུང་འགྱུར་བའི། །
ལས་བྱེད་དེ་ནི་སྲིད་པ་ཡིན། །

[Block 2884]
དེ་ཡུལ་རྣམས་ཐོབ་པར་བྱ་བའི་ཕྱིར་ཡོངས་སུ་རྒྱུག་པ་ན་ཡང་སྲིད་པ༌[^1607]ལ་སོགས་པ༌[^1608]དེ་ནི་དེའི་སྲིད་པ་ཡིན་ནོ། །

[Block 2885]
ལས་དེས་ཡང༌[^1609]འདི་ནས་ཤི་འཕོས་ནས་ཚེ་ཕྱི་མར་ཉིང་མཚམས་སྦྱོར་བར་འགྱུར་ཏེ། ཉིང་མཚམས་སྦྱོར་བ་དེ་ནི་སྐྱེ་བ་ཡིན། འདི་ལ་རྣམ་པར་ཤེས་པའི་ཡན་ལག་གང་ཡིན་པ་དེ་ནི་ཚེ་གཞན་དུ་སྐྱེ་བ་ཡིན་ནོ། །

[Block 2886]
དེ་ཕན་ཆད་ཚོར་བའི་བར་ནི་རྒ་ཤི་ཡིན། སྐྱེ་བ་ཕན་ཆད་ཚོར་བའི་གནས་སྐབས་ཀྱི་བར་ནི་རྒ་ཤི་སྟེ། འདི་ལ་ཡན་ལག་བཞི་པོ་མིང་དང་གཟུགས་དང་སྐྱེ་མཆེད་དྲུག་དང་། རེག་པ་དང་། ཚོར་བ་གང་དག་ཡིན་པ་དེ་དག་ཉིད་གཞན་དག་ཏུ་རྒ་ཤི་ཡིན་ནོ། །

[Block 2887]
དེ་ལྟར་ན་དེ་དག་ནི་ཡན་ལག་བཅུ་གཉིས་ཡིན་ནོ། །

[Block 2888 [HEADING]]
##### རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་རྣམ་པ་བཞི། ^3-1-11-2-0

[Block 2889]
རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་དེ་ནི་རྣམ་པ་བཞིར་བརྗོད་དོ། །

[Block 2890]
[^1610]སྐད་ཅིག་པ་དང་། རྒྱུན་ཆགས་པ་དང་། འབྲེལ་པ་ཅན་དང་། གནས་སྐབས་པའོ། །

[Block 2891 [HEADING]]
###### སྐད་ཅིག་པ། ^3-1-11-2-1-0

[Block 2892]
སྐད་ཅིག་མ༌[^1611]ཇི་ལྟ་བུ་ཞེ་ན། སྐད་ཅིག་མ་གཅིག་ལ་ཡན་ལག་བཅུ་གཉིས་ཡོད་པ་སྟེ། འདི་ལྟ་སྟེ། ཆགས་པའི་དབང་གིས་སྲོག་གཅོད་པའི་རྨོངས་པ་གང་ཡིན་པ་དེ་ནི་མ་རིག་པའོ། །

[Block 2893]
སེམས་པ༌[^1612]གང་དག་ཡིན་པ་དེ་དག་ནི་འདུ་བྱེད་རྣམས་སོ།[^1613] །དངོས་པོ་སོ་སོར་རྣམ་པར་རིག་པ་ནི་རྣམ་པར་ཤེས་པའོ། །

[Block 2894]
རྣམ་པར་ཤེས་པ་དང་ལྷན་ཅིག་འབྱུང་བའི་ཕུང་པོ་བཞི་ནི་མིང་དང་གཟུགས་སོ། །

[Block 2895]
མིང་དང་གཟུགས་ལ་རྣམ་པར་གནས་པའི་དབང་པོ་རྣམས་ནི་སྐྱེ་མཆེད་དྲུག་གོ། །

[Block 2896]
སྐྱེ་མཆེད་དྲུག་འདུས་པ་ནི་རེག་པའོ། །

[Block 2897]
རེག་པ་ཉམས་སུ་མྱོང་བ་ནི་ཚོར་བའོ། །

[Block 2898]
ཆགས་པ་གང་ཡིན་པ་དེ་ནི་སྲེད་པའོ། །

[Block 2899]
དེ་དང་མཚུངས་པར་ལྡན་པའི་ཀུན་ནས་དཀྲིས་པ་རྣམས་ནི་ལེན་པའོ། །

[Block 2900]
དེས་ཀུན་ནས་བསླང་བའི༌[^1614]ལུས་དང་། ངག་གི་ལས་ནི་སྲིད་པའོ། །

[Block 2901]
ལས་དེ་རྣམས་སྐྱེ་བ་ནི༌[^1615]སྐྱེ་བའོ། །

[Block 2902]
ཡོངས་སུ་སྨིན་པ་ནི་རྒ་བའོ། །

[Block 2903]
ཞིག་པ་ནི་ཤི་བའོ། །

[Block 2904 [HEADING]]
###### འབྲེལ་པ་ཅན། ^3-1-11-2-2-0

[Block 2905]
ཡང་སྨྲས་པ། སྐད་ཅིག་པ་དང་། འབྲེལ་པ་ཅན་ནི་རབ་ཏུ་བྱེད་པ་དག་ལས་ཇི་སྐད་འབྱུང་བ་བཞིན་ནོ། །

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
--- END BLOCKS ---
