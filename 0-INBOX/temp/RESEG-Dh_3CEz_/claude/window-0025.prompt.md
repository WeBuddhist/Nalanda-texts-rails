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
རབ་ཏུ་གནས་པ་ཡང་སྔོན་དུ་བསྙེན་པ་བྱ་སྟེ། རབ་མཐོང་སྔགས་ཀྱི་ཕ་རོལ་སོན། །ཞེས་བྱ་བ་ནི་དེ་ཡང་ཡན་ལག་དྲུག་གམ་ཏིང་ངེ་འཛིན་གསུམ་གྱིས་བྱས་ལ། དེ་ཡང་གསུམ་སྟེ།

[Block 877 [VERSE]]
གྲངས་ཀྱི་བསྙེན་པ་འབུམ་དང་ཁྲི། །
གཙོ་དང་འཁོར་ནི་ཚང་བར་བྱ། །

[Block 878]
དུས་ཀྱི་བསྙེན་པ་ཟླ་བ་དྲུག་གོམས་པ་ལ་སོགས་པ༌[^926]ཅི་རིགས་པར་ཤེས་པར་བྱའོ། །མཚན་མ་ནི་ལྷས་གནང་བའམ། རྨི་ལམ་གྱི་བར་དུ་བཟང་པོ་འབྱུང་བ་དང་། སློབ་དཔོན་མཚན་ཉིད་དང་ལྡན་པ་ལ། ལན་གཉིས་དང་གསུམ་གྱི་བར་དུ་གསོལ་བ་གདབ་པར་བྱའོ། །སྔར་སའི་ཆོ་ག་ཡང་ལེའུ་བཅུ་པ་ལྟར་བྱ་སྟེ། དེའི་སྔོན་དུ་བགེགས་བསལ་བའི་དོན་དུ་ཅི་གསུངས་སྦྱིན་སྲེག་བྱས་ནས་ཞེས་པ་ཆོ་ག་བཞིན་བྱའོ། །

[Block 879]
སྟ་གོན་ལ་སོགས་བྱས་ནས་ནི། བྱ་བ་བདག་ཉིད་ལ་ལྡན་པ་ཕུན་སུམ་ཚོགས་པར་བྱ་བ་ནི་ཡན་ལག་དྲུག་གམ་སྦྱོར་བ་གསུམ་བྱས་ལ། དེ་ནས་སའི་ལྷ་མོ་ལྷག་པར་གནས་པ་ནི་རླུང་མཚམས་སུ་མཎྜལ་ཅིག་བྱས་ལ་མེ་ཏོག་གི་ཚོམ་བུ་ཅིག་བཀྲམ་སྟེ། པཾ་ལས་བུམ་པ་དེ་ལས་སའི་ལྷ་མོ་སྐུ་མདོག་སེར་བ་གཡས་པས་ཁས་ལེན་པ་གཡོན་པས་བུམ་པ་བསྣམས་པ་ཅིག༌[^927]བསྐྱེད་དེ། རང་བཞིན་པ་སྤྱན་དྲངས་ནས་མཆོད་པ་བྱས་ནས། མ་མ་རིན་ཆེན་ཞེས་བྱ་བ་དང་། ས་དང་ཕ་རོལ་ཕྱིན་པ་ཞེས་པ༌[^928]གཞན་ནས་བྱུང་བ་དང་ཚིག་གཉིས་ཀྱིས་དཔང་པོར་གསོལ་པ། བསྟིམ་པའམ་ཡང་ན་དཔང་པོར་བཞུགས་སོ། །

[Block 880]
ལྷ་ལྷག་པར་གནས་པ་ནི་དཀྱིལ་འཁོར་ཁང་པའམ་གཞན་དུ་མཎྜལ་སྦྱོར་བ་ལྔས་བྱུགས་ལ། གཙོ་བོའི་གནས་སུ་དྲིའི་ཐིག་ལེ་གྲུ་བཞི་བྱ། གཞན་ལ་ཟླུམ་པོ་བྱ། པདྨ་དང་ཟླ་བ་བསམས་ལ་མེ་ཏོག་ཚོམ་བུ་རང་རང་གི་སྔགས་བཟླས་ཤིང་ལྷ་མོར་མོས་ལ། དེ་ལ་མར་མེ་དང་ལྷ་བཤོས་ལ་སོགས་པ་བཀྲམ་སྟེ། སློབ་དཔོན་གྱིས་ས་བོན་ཙམ་མམ་ཕྱག་མཚན་ལས་ལྷར་བསྐྱེད་ལ། ཡེ་ཤེས་འཁོར་ལོ་མདུན་དུ་བཀུག་པ་ལ་བླ་ན་མེད་པའི་མཆོད་པ་བྱས་ལ་དགུག་གཞུག་ལ་སོགས་པ་བྱ། དེ་ལ་སྐྱེ་མཆེད་བྱིན་གྱིས་བརླབ་པ༌[^929]དང་། སྐུ་གསུང་ཐུགས་བྱིན་གྱིས་བརླབ༌[^930]དབང་བསྐུར་མཆོད་བསྟོད་བདུད་རྩི་མྱངས་ནས་བཟླས་པ་མཐར་ཐུག་པའི་བར་དུ་བྱས་ལ། རབ་གནས་ཀྱི་དོན་དུ་ཚིག་བསྒྱུར་ལ་བྱའོ། །

[Block 881]
དེ་ནས་བུམ་པ་དང་། ཡོ་བྱད་ཀུན་ལྷག་པར་གནས་པ་བྱ། དེ་ནས་ཡོན་བདག་སློབ་མ་དབང་བསྐུར་ནས། སྟ་གོན་ཟངས་ཀྱིས་བྱ། མི་བསྐུར་ན་སྦྱང་བ་དང་། སྤྲོ་བ་བསྐྱེད་པ༌[^931]ཙམ་བྱའོ། །

[Block 882 [VERSE]]
དེ་ནས་རབ་ཏུ༌[^932]གནས་པ་ལ། །
སྔ་བར་སྐུ་གཟུགས་སྦྱང་བ་དང་། །

[Block 883]
ཞེས་བྱ་བ་ནི་སྟ་གོན་བྱེད་པ་དང་ཉིན་གཅིག་པར་བྱ་བའོ། །

[Block 884 [HEADING]]
#### སྟ་གོན་བྱེད་པ། ^2-1-2-0

[Block 885]
སྟ་གོན་བྱེད་པ་ནི་གཉིས་ཏེ། རྟེན་སྦྱང་བ་དང་། མགོན་པོ་བསྡུ་བའོ། །

[Block 886 [HEADING]]
##### རྟེན་སྦྱང་བ། ^2-1-2-1-0

[Block 887]
རྟེན་སྦྱང་བ་ནི་སྟེགས་བུ་ཁྲུ་གང་དཔངས་སུ་ཁྲུ་ཕྱེད་པའི་སྟེང་དུ་སྐུ་གཟུགས་གྲལ་ནས་ཕྱུང༌[^933]ལ། སྦྱང་བ་ལྔ་ནི་དང་པོ་ཁྲུས་ཀྱིས་སྦྱང་སྟེ། འདག་ཆལ་ལ་སོགས་པས་བཀྲུས་ཏེ། དེ་ནས་མེའི་ནང་དུ་ཡུངས་ཀར་བླུགས་ཤིང་སྦྱང་བའི་སྔགས་བཟླས་ཤིང་བསྐོར་ཞིང་བྱའོ། །

[Block 888]
དེ་ནས༌[^934]ཆུའི་ནང་དུ་སྔ་མ་བཞིན་བྱའོ། །དེ་ནས་རྩྭ་དཱུར་བས་སྦྱང་ངོ་། །དེ་ནས་ཤུན་པ་ལྔས་དྲིལ་ཕྱིས་བྱའོ། །དེ་དག་མེད་ན་བ་བྱུང་ལྔ་དང་།འབྲུ་མར་བསྐུས་ལ་བག་ཕྱེས་དྲིལ་ཕྱིས་བྱའོ། །དེ་ནས་ལས་ཐམས་ཅད་པའི་བུམ་པ་ནས་ཁྲུས་བྱ། བཀྲ་ཤིས་གདོན་ཞིང་བྱབས་ལ་སྐུ་ཕྱིས་ལ་སྦྱང་ངོ་། །རས་རིས་དང་མཆོད་རྟེན་དང་ལྷ་ཁང་ལ་མེ་ལོང་ལ་ཁྲུས་བྱའོ། །

[Block 889 [HEADING]]
##### མགོན་པོ་བསྡུ་བ། ^2-1-2-2-0

[Block 890]
དེ་ནས་མགོན་པོ་བསྡུ་བ་ནི་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་སྤྱན་དྲངས་ལ་མཆོད་པ་དང་བསྟོད་པ་བྱས་ལ་གསོལ་བ་གདབ་པར་བྱའོ། །དེ་ནས་ནང་པར་སྔ་བར་དབང་བསྐུར་ན་རྨི་ལམ་དྲིས་ཁ་སྦྱོར་ནམ་མཁའ་ལ་བཏེག་ལ། ཐིག་དང་ཚོན་དང་ཁ་སྦྱར་དབབ་པ་བསྲེའོ། །དེ་ནས་རྒྱན་དགྲམ་བུམ་པ་དགོད་པ་ལ་སོགས་པ་བྱའོ། །དེ་ནས་དཀྱིལ་འཁོར་བསྒྲུབ་པ་ནི་ཡན་ལག་དྲུག་གམ་སྦྱོར་བ་གསུམ་གྱི་བདག་ཉིད་ལ་ལྡན་པ་ཕུན་སུམ་ཚོགས་པ་ལས་ཀྱི་སློབ་མས་བྱས་ལ་བླ་མ་ལ་མོས་པ་འཕོ་བར་བསྒོམས་ནས། ས་བོན་ཕྱག་མཚན་ཙམ་ལས་ལྷ་བསྐྱེད། རང་བཞིན་གནས་ནས༌[^935]སྤྱན་དྲངས་པ་བསྲེས་ལ་མཆོད་བསྟོད་བདུད་རྩི་མྱང་བ་བྱའོ། །

[Block 891 [HEADING]]
#### ནང་དུ་གནས་པ། ^2-1-3-0

[Block 892]
དེ་ནས་ནང་དུ༌[^936]གནས་པ་ནི་བཞི་སྟེ་རབ་ཏུ་གནས་པ་དང་། མངའ་དབུལ་བ་དང་། སྤྱན་དབྱེ་བ་དང་། ཞལ་བསྲོ་བའོ། །

[Block 893 [HEADING]]
##### རབ་ཏུ་གནས་པ། ^2-1-3-1-0

[Block 894]
རབ་གནས་ལ་གཉིས་ཏེ། ཐུན་མོང་དང་ཁྱད་པར་གྱི་རབ་ཏུ་གནས་པའོ། །

[Block 895 [HEADING]]
###### ཐུན་མོང་གི་རབ་ཏུ་གནས་པ། ^2-1-3-1-1-0

[Block 896]
དེ་ལ་ཐུན་མོང་ནི་སྦྱང་བ་ལྔ་པོ་དང་མགོན་པོ་བསྡུས་པ་ལ་ཚིག་བསྒྱུར་ལ་བྱ། ཉིན་གཅིག་པ་དང་འདྲའོ། །དེ་ལ་རྟེན་རང་རང་གི་ལྷ་གང་ཡིན་པར་བསྐྱེད། མི་གསལ་ན་ལྷག་པའི་ལྷར་བསྐྱེད། པོ་ཏི་ལ་སྔགས་ནི་ཨ་ལས་རྡོ་རྗེ་ཆོས་སུ། མདོ་སྡེ་ནི་སྣང་བ་མཐའ་ཡས་སུ། ཡུམ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་མར་པྲ༌[^937]ལས་བསྐྱེད། མཆོད་རྟེན་ནམ་གཙུག་ལག་ཁང་ནི་བྷྲཱུཾ་ལས་གཞལ་ཡས་ཁང་ངམ། རྡོ་རྗེ་དབྱིངས་ཀྱི་དབང་ཕྱུག་མར་བསྐྱེད། ནམ་མཁར་བཞུགས་པའི་སངས་རྒྱས་རྣམས། སྐུ་གཟུགས་སྙིང་གར་རབ་ཏུ་གཞུག །[^938]ཇི་ལྟར་སངས་རྒྱས་ཐམས་ཅད་ནི། དགའ་ལྡན་གནས་ཞེས་བྱ་བ་སྟེ། སྔར་གྱི་སྟ་གོན་ནམ་མཁར་སྤྱན་དྲངས་པ་བསྟིམ་པ་ཙམ་བྱས་ཏེ། བྱིན་གྱིས་བརླབ།[^939] དབང་བསྐུར། མཆོད་བསྟོད་བྱས་ལ་བཞུགས་སོ། །

[Block 897 [HEADING]]
###### ཁྱད་པར་གྱི་རབ་གནས། ^2-1-3-1-2-0

[Block 898]
ཁྱད་པར་གྱི་རབ་གནས་ནི་དཀྱིལ་འཁོར་བ་རྣམས་བསྟིམས་ལ་ཡང་སྔ་མ་བཞིན་བྱའོ། །

[Block 899 [HEADING]]
##### སྤྱན་དབྱེ་བ། ^2-1-3-3-0

[Block 900 [HEADING]]
###### ཐུན་མོང་སྤྱན་དབྱེ། ^2-1-3-3-1-0

[Block 901]
སྤྱན་དབྱེ་བ་ནི་གཉིས་ཏེ། ཐུན་མོང་སྤྱན་དབྱེ་ནི་གསེར་གྱི་ཐུར་མ་ལ་ཚིགས་བཅད་དང་སྔགས་ཀྱིས་བྱ།

[Block 902 [HEADING]]
###### ཁྱད་པར་སྤྱན་དབྱེ། ^2-1-3-3-2-0

[Block 903]
ཁྱད་པར་སྤྱན་དབྱེ་ནི་ཡེ་ཤེས་དབབ་པ་ཞལ་བཞད་པའམ་སྐུ་ལྡེག་པའམ། སྙན་ཆ་འཁྲོལ་བའམ་ས་གཡོ་བའི་བར་དུ་བྱའོ། །

[Block 904 [HEADING]]
##### མངའ་དབུལ་བ། ^2-1-3-2-0

[Block 905]
མངའ་དབུལ་བ་ལ་གཉིས་ཏེ། ལྷ་ལྟར་མཆོད་པ་དང་། སློབ་མ་ལྟར་དབང་བསྐུར་བའོ། །

[Block 906 [HEADING]]
###### ལྷ་ལྟར་མཆོད་པ། ^2-1-3-2-1-0

[Block 907]
མཆོད་པ་ནི་མཆོད་པའི་ཁྱད་པར་དཔག་ཏུ་མེད་པ་རྒྱལ་པོ་གཅིག་གི་ཡོ་བྱད་དེ། གདུགས་དང་བ་དན་ལ་སོགས་པ་དང་སྤོས་དང་མེ་ཏོག་ལ་སོགས་པ་བརྒྱ་བས་ལྷག་ཅིང་བཅུ་ལས་མི་ཉུང་བར་བྱའོ། །རས་ཡུག་བརྒྱའམ་སྟོང་ངམ་པ་ལང་གི་ཁྱུ་བརྟགས་པ་དང་། རིན་པོ་ཆེ་སྣ་བདུན་ལ་སོགས་པ་འབུལ་ལོ། །

[Block 908 [HEADING]]
###### སློབ་མ་ལྟར་དབང་བསྐུར་བ། ^2-1-3-2-2-0

[Block 909]
སློབ་མ་ལྟར་དབང་བསྐུར་བ་ནི་ཆུ་ནས་བརྩམས་ནས་རིག་པའི་དབང་དང་བརྟུལ་ཞུགས་དང་རྗེས་སུ་གནང་བ་དང་། ལུང་བསྟན་པ་ལ་སོགས་པ་མཆོད་གནས་སུ་གཏད་པ་ཤིས་པ་བརྗོད་པར་བྱའོ། །

[Block 910 [HEADING]]
##### ཞལ་བསྲོ་བ། ^2-1-3-4-0

[Block 911]
ཞལ་བསྲོ་བ་ནི་རྒྱས་པའི་སྦྱིན་སྲེག་གམ་ཤིས་པའི་སྦྱིན་སྲེག་བྱའོ། །དགེ་འདུན་ལ་མཆོད་པ་དང་། ཡུལ་ཁྲིམས་ཀྱིས་ཤིས་པའི་སྟོན་མོ་བྱ། ནད་པ་ཡིན་ན་ཚོགས་ཀྱི་མཆོད་པ་དང་ཙཱ་རུའི་སྟོན་མོ་བྱའོ། །གཙུག་ལག་ཁང་ཡིན་ན་ནག་པོ་ཆེན་པོ་བསྒོམ་པར་བྱ་སྟེ། རྟེན་ཡོད་པའི་དྲུང་དུ་ཕྱིན་ལ་མཆོད་པ་དང་གཏོར་མ་བཤམས་ལ། དང་པོར་རང་བསྐྱེད་རང་བཞིན་པ་བསྟིམས་ལ་བྱིན་གྱིས་བརླབ་པ༌[^940]བྱས་ལ། མཆོད་བསྟོད་བྱས་ལ་བཀའ་བསྒོ་བ་བྱ། འདི་རྣམས་ཀྱི་ཆོ་ག་ནི་ལག་ཏུ་བླང་བའི་རིམ་པར༌[^941]ཤེས་པར་བྱའོ། །

[Block 912]
ལ་ལ་ནི་རབ་ཏུ་གནས་པའི་ལྷ་ནི་གཤེགས་སུ་གསོལ་བར་འདོད་དོ། །བླ་མ་ནི་སྐུ་གཟུགས་ལ་སོགས་པར་ཕལ་ཆེར་ནི༌[^942]མི་གཤེགས༌[^943]སོ། །རྟེན་ཁྱད་པར་ཅན་མ་ཡིན་པ་ལ་ནི་ལན༌[^944]ཅིག་བྱིན་གྱིས་བརླབ་པ་ཙམ་བྱས་ལ་གཤེགས་སོ། །བརྟག་པ་ཕྱི་མ་འདི་ནི་མངོན་པར་རྟོགས་པས་མི་འཆིང་སྟེ། བརྟག་པ་སྔ་མའི་ཡན་ལག་ཏུ་སྟོན་ཏེ། དེ་ཡང་རབ་ཏུ་གནས་པ་ནི་ལེའུ་བཅུ་པའི་མ་ཚང་བ་འདི་ཡིས་ཁ་བསྐང་བར་བྱའོ། །

[Block 913]
ལེའུ་གཉིས་པ་ནི་བརྟག་པ་སྔ་མའི་རིམ་པ་གཉིས་སྤྱིར་ཤེས་པར་བྱ་བ་ཉམས་སུ་བླངས།[^945] ཉམས་སུ་བླངས༌[^946]པའི་འབྲས་བུའི་ཚུལ་གྱིས་གཏན་ལ་འབེབས་སོ། །ལེའུ་གསུམ་པ་ནི་གླིང་གཞིའི་དོན་དུ་གཏན་ལ་འབེབས་སོ། །ལེའུ་བཞི་པས་ནི་ཁ་འཐོར་གྱི་དོན་དཀའ་བ་གཏན་ལ་འབེབས་སོ། །ལེའུ་ལྔ་པས་ནི་ཧེ་རུ་ཀ་ཕྱག་བཅུ་དྲུག་པའི་མངོན་པར་རྟོགས་པའི་དཀྱིལ་འཁོར་དང་། རྡུལ་ཚོན་གྱི་དཀྱིལ་འཁོར་ལེའུ་གསུམ་པ་དང་། བཅུ་པའི་མ་ཚང་བ་གཏན་ལ་འབེབས་སོ། །དྲུག་པ་བདུན་པ་གཉིས་ཀྱིས་སྤྱིར་བྲིས་སྐུ་དང་གླེགས་བམ་ལ་བརྟེན་ནས་སྔར་ཚོགས་ཀྱི་འཁོར་ལོ་མ་བསྟན་པ་འདིར་གཏན་ལ་འབེབས་སོ། །ལེའུ་བརྒྱད་པས་ནི་འཇུག་པའི་གང་ཟག་དད་པ་ཅན་དང་གདུལ་བར་དཀའ་བའི་ཐབས་རྒྱུད་འདིར་འཇུག་པའི་ཐབས་སྟོན་ཏོ། །དགུ་པས་ནི་བགྲང་ཕྲེང་དང་ལས་སོ་སོའི་བཟའ་བའི་དམ་ཚིག་བསྟན་ཏོ། །བཅུ་པ་དང་བཅུ་གཅིག་པས་ནི་ཞེ་སྡང་ཅན་དང་། ཆགས་པ་ཅན་རྒྱུད་འདིར་འཇུག་པའི་ཚུལ་ལམ་ཐབས་བསྟན་ཏོ། །བཅུ་གཉིས་པས་ནི་དབང་བཞིའི་སྡོམ༌[^947]གྱི་ཚིག་དང་དབང་བསྐུར་བའི་ཚིགས་བཅད༌[^948]སྔར་མ་གསུངས་པའི་ཁ་སྐོང༌[^949]བསྟན་ཏོ། །རབ་གནས་ཀྱི་ལེའུ་བཤད་པ་སྟེ་དང་པོའོ།། །།

[Block 914 [HEADING]]
### བརྟག་པ་གཉིས་པའི་ལེའུ་གཉིས་པ། ^2-2-0

[Block 915]
ད་ནི་བརྟག་པ་སྔ་མའི་རིམ་པ་གཉིས་ཀྱིས་ཐོབ་པའི་ཐབས་དང་ཤེས་རབ་མི་ཕྱེད་པ་ཕྱག་རྒྱ༌[^950]ཆེན་པོ་ཇི་ལྟ་བུ་ཞེ་ན། དེའི་ཕྱིར་རྡོ་རྗེ་སྙིང་པོས་དྲིས་པའོ། །ཆོས་ཀུན་ཞེས་པ་ནི་གཟུགས་ལ་སོགས་པའི་རང་བཞིན་ནོ། །ནམ་མཁའ་ལྟ་བུ་ནི་ཤེས་རབ་ཟབ་མོའི༌[^951]དཔེའོ། །རྒྱ་མཚོ་ལྟ་བུས་ནི༌[^952]ལྷག་མ་སྟེ་ཐབས་ཟབ་པའི་དཔེའོ། །
--- END BLOCKS ---
