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
གང་ཡང་བསལ་ཏེ་འོངས་པས་བརྗོད་ན་ནི་གཏན་ཚིགས་མེད་པར་ཐལ་བར་འགྱུར་བས༌[^672]བརྗོད་པར་བྱའོ། །

[Block 877]
དེ་བསལ་བ་ལས་སྐྱེ་བ་ནི་མ་ཡིན་ཏེ། རྒྱུ་ལ་མེད་པས་ན་ཐ་དད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 878]
དེ་ལ་མེད་པ་སྔོན་དུ་སོང་བ་ཅན་གྱི་ཐ་དད་དམིགས་པར་འགྱུར་ན་ནི་རྗེས་སུ་འགྲོ་བ་དམིགས་པར་མི་འགྱུར་ཏེ། ཕྱིན་ཅི་ལོག་ཏུ་སྒྲོ་འདོགས་པ༌[^673]མི་འདོད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 879]
འདི་ལྟར་གང་གི་ཕྱིར་རྗེས་སུ་འགྲོ་བ་གཅིག་སྔོན་དུ་འགྲོ་བ་ཅན་ནི་མཐོང་ཞིང་དེ་མེད་པ་ལ་མ་མཐོང་བ་དེས་ན་གཅིག་སྔོན་དུ་སོང་བ་ཅན་ནོ། །

[Block 880]
དེ་ཁས་མི་ལེན་ཡང་རྗེས་སུ་འགྲོ་བ་མེད་པར་ཐལ་བར་འགྱུར་རོ། །

[Block 881]
དེ་ཡང་མེད་དོ་ཞེས་བྱ་བ་དེ་ཉིད་རྗེས་སུ་འགྲོ་བར་བརྗོད་པ་ཡིན་ནོ། །

[Block 882]
དེས་ན་རྣམ་ལྡན་ལས་གཞན་མིན། །རྗེས་སུ་འགྲོ་བ་ཡོད་པ་མ་ཡིན་ཏེ། ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ་ཞེས་པ་དང་། འདི་ལ་ཁྱད་པར་ཅི་ཡོད། ཡང་འདིར་ཐལ་བ་གཞན་བརྗོད་པ་གཙོ་བོར་ཡོད་པ་མ་ཡིན་ཏེ། ལོངས་སྤྱོད་པ་པོ་དང་ལོངས་སྤྱད་པར་བྱ་བ་དག་ཡོན་ཏན་དང་ཡོན་ཏན་ཅན་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ་ཞེས་པ་དང་། རྫས་ཡོད་པ་མ་ཡིན་ཏེ། ཡོན་ཏན་རྣམས་ཀྱང༌[^674]རྫས་སུའམ། །རྫས་རྫས་མ་ཡིན་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་དེ་ཇི་ལྟར་བསལ་ཏེ་འོངས་པ་ཡིན་འདི་ནི་བསལ་ཏེ་འོངས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར།

[Block 883 [VERSE]]
ཐལ་འགྱུར་ཕྱོགས་ཆོས་ཅན་མིན་ཕྱིར། །
ཁས་བླངས་སྔོན་དུ་སོང་བ་ལས། །
དེ་བཞིན༌[^675]རྟགས་དང་དམ་བཅའ༌[^676]ཡི། །
སྐྱོན་བརྗོད་སུན་འབྱིན་དུ་ཤེས་བྱ། །

[Block 884]
འདིར་གཙོ་བོ་ཡོད་པ་ཉིད་ཀྱིས་གཏན་ཚིགས་ཡོན་ཏན་རྣམས་ཀྱི་རྗེས་སུ་འགྲོ་བ་སྒྲུབ་པའི་ཕྱིར་འབྲས་བུ་གཅིག་པ་ཉིད་གཏན་ཚིགས་སུ་བརྗོད་དོ། །

[Block 885]
འདིས་ཁས་བླངས་པ་ནི་གང་མ༌[^677]མཐོང་བའི་སྔོན་དུ་སོང་བའི་འབྲས་བུ་སྟེ། དེ་ཡོན་ཏན་གྱི་རྗེས་སུ་འགྲོ་བ་ཉིད་བཞིན་དུ་བྱས་ནས་ལོངས་སྤྱོད་པ་པོ་ལ་ཡང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་མ་ངེས་པའོ། །

[Block 886]
ཁས་མི་ལེན་ཡང་ལོངས་སྤྱོད་བྱ་བ་མ་ཡིན་པ་ནི་ཡོན་ཏན་མ་ཡིན་པའི་ཕྱིར་རྩ་བའི་གཏན་ཚིགས་མ་གྲུབ་པ་ཉིད་ཡིན་ནོ། །

[Block 887]
རྫས་ཀྱང་རྫས་ཉིད་དུ་ལྡན་པ་ལས་ཡིན་ཞིང་དེ་མེད་པ་ཁས་བླངས་པའི་ཡོན་ཏན་རྣམས་ཀྱང་རྫས་ཉིད་དུ་འགྱུར་ཏེ། ལྡན་པ་ཡོད་པས་ནའོ་ཞེས་ལྡན་པས་བསལ་བ་ཡིན་ཏེ། ལྡན་པའི་འདུ༌[^678]བ་གཅིག་པའི་ཕྱིར་རམ། ཐམས་ཅད་དུ་སོང་བའི་ཕྱིར་རོ། །

[Block 888]
ཅི་དེ༌[^679]དག་ཀྱང་རྫས་ཉིད་དུ་ཐལ་བར་འགྱུར་རོ། །

[Block 889]
རྫས་ཉིད་ཀྱང་ལྡན་པའམ་ལྡན་པ་ཡང་རྫས་ཉིད་དུ་ཁས་བླང་བར༌[^680]བྱ་སྟེ། རྫས་མ་ཡིན་པ་ཡང་རྫས་བཞིན་དུ་རྫས་ཡོད་པར་འགྱུར་རོ་ཞེས་དམ་བཅའ་བའི་སྐྱོན་ཡིན་ཏེ། རྫས་རྫས་མ་ཡིན་པ་ཉིད་ཀྱིས་བསལ་བའི་ཕྱིར་རོ། །

[Block 890]
ཅི་སྟེ་ཡང་ཡོན་ཏན་རྣམས་ཀྱང་རྫས་དང་ལྡན་པའི་ཕྱིར་རྫས་ཉིད་དུ་ཐལ་བར་འགྱུར་བ་ན་མ་ངེས་པ་ཉིད་དུ་འགྱུར་རོ་ཞེ་ན། དེ་སྐད་དུ་སྨྲ་བར་མི་ནུས་ཏེ་རྫས་ཉིད་དང་ལྡན་པའི་གཞན་རྫས་ཉིད་ཡིན་པ་ནི་མ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 891]
དེའི་ཕྱིར་ཉིད་དུ་འགྱུར་རོ་ཞེས་པ་འདི་དམ་བཅའ་བ་ཉིད་དུ་རིགས་སོ། །

[Block 892]
རྫས་ཀྱི་མཚན་ཉིད་ཀྱི་གཏན་ཚིགས་ལས་ཡོན་ཏན་ལ་སོགས་པ་གཞན་རྣམས་ལ་ཡང་ཐལ་བར་འགྱུར་རོ་ཞེས་ཐལ་བར་འགྱུར་གྲུབ་པས་ཆོག་གོ། །

[Block 893 [HEADING]]
#### ཕྱོགས་ཆོས་རྣམ་པ་དགུ། ^3-2-2-0

[Block 894]
ཕྱོགས་ཀྱི་ཆོས་ཉིད་གཏན་ཚིགས་སམ་གཏན་ཚིགས༌[^681]ལྟར་སྣང་བར་འགྱུར་ཏེ། དེ་དག་རྣམ་པར་ཕྱེ་བ་ནི་མཐུན་ཕྱོགས་ལ་ཡོད་མེད་རྣམ་གཉིས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 895 [HEADING]]
##### མཐུན་པའི་ཕྱོགས། ^3-2-2-1-0

[Block 896]
དེ་ལ་ཡོད་པ་གྲུབ་པ་ནི་བསྒྲུབ་པར་བྱ་བའི་ཆོས་ཀྱི་སྤྱིས་ཕྱོགས་པ༌[^682]དང་མཐུན་པའི་ཕྱོགས་མཚུངས་པའི་དོན་ཐམས་ཅད་ཕྱོགས་ཞེས་བྱ་བ་སྟེ་དེ་ཡང་བསྒྲུབ་བྱའི་ཆོས་སོ། །

[Block 897 [VERSE]]
ཐ་དད་མེད་པའི༌[^683]དེ་ཉིད་ཅེས། །
བྱས་ནས་གཞན་ལ་སྟོན་པར་བྱེད། །
མཐུན་པའི་ཕྱོགས་ལ་ཡོད་ཅེས་སོ། །

[Block 898]
གལ་ཏེ་འདི་ལྟར། མཐུན་ཕྱོགས་ཞེས་པ་ཕྱོགས་ལས་ཏེ། གལ་ཏེ་ཐ་དད་མེད་པ་དེ་ཉིད་ལ་མཐུན་ཕྱོགས་ཞེས་བརྗོད་ན་ནི་འདི་ལ་ཡང་མཐུན་པའི་ཕྱོགས་ལའོ་ཞེས་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 899]
གལ་ཏེ་དེ་ལྟར་འདི་ལ་དབྱེ་བ་མ་བརྗོད་ཅེ་ན། ཐ་དད་ཡོད་དུ་ཆུག་མོད། བུམ་པ་ལ་སོགས་པ་ལ་ཡོད་པ༌[^684]མི་རྟག་པ་ཉིད་ནི་བསྒྲུབ་བྱ་མ་ཡིན་ཏེ། དེའི་ཕྱིར། འདི་ལའང་ཐ་དད་ཅེས་མི་འདོད། །དེའི་ཕྱིར་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་ཅེས་པ༌[^685]རིགས་པ་ཡིན་ནོ། །

[Block 900 [HEADING]]
##### མི་མཐུན་པའི་ཕྱོགས། ^3-2-2-2-0

[Block 901]
འོ་ན་མི་མཐུན་པའི་ཕྱོགས་གང་ཡིན་ཞེ་ན་རྣམ་པ་གཞན་དུ་གྱུར་པ་ཉིད་ནི་ཡོད་པ་ཡིན་ཏེ། བསོད་ནམས་མ་ཡིན་པ་ཞེས་བརྗོད་པ་བཞིན་ནོ། །

[Block 902]
ཡོད་པ་བཀག་པ་ཙམ་མེད་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ལ་རེ་ཞིག །

[Block 903 [VERSE]]
དེ་གཞན་དང་ནི་དེ་འགལ་ཏེ། །
མི་མཐུན་ཕྱོགས་རྣམས་གཉིས་པ་ཡང་། །
རྟགས་མེད་པས་ནི་འགལ་བ་སྟེ། །

[Block 904]
རྣམ་པར་དཔྱད་པ་ལས་འགྱུར་ཡིན། གལ་ཏེ་ཡང་མཐུན་པའི་ཕྱོགས་ལ་སོགས་པ་ལས་གཞན་ཏེ།[^686] མི་མཐུན་པའི་ཕྱོགས་ཡོད་པ་དེས་ན་གཏན་ཚིགས་མེད་པར་འགྱུར་རོ། །

[Block 905]
འདི་ལྟར་གང་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པའི་བྱས་པ་ཉིད་ལ་སོགས་པ་དེ་ནི་མི་རྟག་པ་ལ་སོགས་པ་ལས་གཞན་དུ་སྡུག་བསྔལ་ལ་སོགས་པ་ལ་ཡང་ཡོད་པ་ཡིན་ནོ། །

[Block 906]
མཐུན་པའི་ཕྱོགས་དང་འགལ་བ་མི་མཐུན་པའི་ཕྱོགས་ཡིན་མོད་ཀྱིས་ཀྱང་དེས་གང་དེ་ལ་མེད་པ་ཉིད་རྣམ་པར་དཔྱད་ནས་བསྒྲུབ་བྱ་གོ་བར་བྱེད་དོ། །

[Block 907]
དེ་ལྟར་ན་ཡང་འདི་ནི་མེའི་དྲོ་བ་ཡོད་དོ་ཞེས་པས། གྲང་རེག་མེད་པར་མེའི་དྲོ་བ༌[^687]ལས་གོ་བར་བྱེད་དོ། །

[Block 908]
དེ་ནི་དྲོ་རེག་མ་ཡིན་པ་ལ་གྲོང་རེག་མ་ཡིན་པ་མེད་པ་ལ༌[^688]ཡང་མ་ཡིན་ནོ། །

[Block 909 [VERSE]]
མཐུན་ཕྱོགས་ལ་མེད་མིན་པ་ཉིད། །
མཚན་ཉིད་གཅིག་ཉིད་ཡིན་མོད་ཀྱང་། །
དོན་དུ་མ་ལ་འཇུག་པའི་རིགས། །

[Block 910]
གང་འདི་ལྟར་མཐུན་པའི་ཕྱོགས་སུ་མེད་པ༌[^689]མི་མཐུན་ཕྱོགས་ལ་མེད་པ་ཉིད་དོ་ཞེས་མཐུན་པའི་ཕྱོགས་ལ་མེད་པ་མ་ཡིན་པ་ནི་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་སྟེ། དེ་གཏན་ཚིགས་ཡིན་པས་ན་བྱས་པ་ཉིད་ནི། ཇི་ལྟར་མི་རྟག་པ་ཉིད་ཀྱི༌[^690]རྟགས་ཡིན་པ་བཞིན་དུ་བདག་མེད་པ་ལ་སོགས་པ་ལ་ཡང་སྦྱར་བར་བྱའོ། །

[Block 911]
འདི་ལྟར་དེ་བདག་མེད་པ་ལ་སོགས་པ་ལ་མེད་པ་མ་ཡིན་པ་ཡང་བདག་མེད་པ༌[^691]ལ་ཡོད་པ་ཡིན་ནོ། །

[Block 912]
ཅི་སྟེ་ཡང་འདི་ནི་སྤྱི་ལས་ཐེ་ཚོམ་དུ་འགྱུར་བ་ཡིན་ནོ་ཞེ་ན། བྱས་པ་ཉིད་སྤྱི་ཡིན་ཡང་རྟག་པ་དང་བདག་མེད་པ་ལ་སོགས་པ་རྣམས་ལ་བུམ་པ་ལ་སོགས་པ་བཞིན་དུ་ཐེ་ཚོམ་དུ་འགྱུར་བ་ནི་མ་ཡིན་ནོ། །

[Block 913]
སྤྱི་ལས་རྗེས་འགྲོ་བླུན་པོ་མིན། །སྤྱི་ཐམས་ཅད་ཐེ་ཚོམ་གྱི་རྒྱུ་མ་ཡིན་ཏེ། བུམ་པ་ནི་བྱས་པ་ཉིད་ཡིན་ལ་བུམ་པ་མ་ཡིན་པ་ལ་ཡང་མཐོང་བ་ཡིན་ནོ། །

[Block 914]
བྱས་པ་ཉིད་མི་རྟག་པ་ལ་སོགས་པ་ལ་ཡང་མེད་པར་མཐོང་བ་ནི་མ་ཡིན་ཏེ། ཐམས་ཅད་དུ་གཏན་ཚིགས་ཀྱི་མཚན་ཉིད་དང་ལྡན་པའི་ཕྱིར་རྣམ་པར་བཅད་པ་ལས་གཏན་ཚིགས་ཡིན་ནོ། །

[Block 915 [HEADING]]
##### རྣམ་པ་གསུམ་དུ་དབྱེ་བ། ^3-2-2-3-0
--- END BLOCKS ---
