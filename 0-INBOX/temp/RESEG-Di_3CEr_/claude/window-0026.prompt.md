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

[Block 916]
ཕྱོགས་ཀྱི་ཆོས་དེ་ཉིད་རྣམ་པ་གསུམ་དུ་དབྱེ་སྟེ། མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་དང་མེད་པ་དང་ཡོད་མེད༌[^692]གཉིས་ཀར་རོ། །

[Block 917]
དེ་བཞིན་དུ་མཐུན་པའི་ཕྱོགས་ལ། །[^693]དེ་ལྟ་མ་ཡིན་ན་དེ་གཉིས་ཉིད་སླར་བཟླས་པར་འགྱུར་རོ། །

[Block 918]
ཡང་དེ་དག་རེ་རེ་ལ་ཡང་གསུམ་གསུམ་དུ་དབྱེ་བར་བྱ་སྟེ། གང་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་དེ་ཉིད་མི་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་དང་། མེད་པ་དང་། ཡོད་མེད་གཉིས་ཀར་རོ། །

[Block 919]
དེ་བཞིན་དུ་མཐུན་པའི་ཕྱོགས་ལ་མེད་པ་དང་གཉིས་ཀ་ལ་ཡང་དབྱེ་བ་དེ་ཉིད་དོ། །

[Block 920]
གང་གི་ཚེ་འདི་ལྟར་མི་རྟག་པ་ཉིད་ནམ་མཁའ་ལ་སོགས་པའི་ཕྱོགས་ལ་ཡོད་པར་ཁས་མི་ལེན་པ་དེའི་ཚེ་མི་མཐུན་པའི་ཕྱོགས་ལ་མེད་པ་ཉིད་ཅེས༌[^694]དེ་དང་མ་འབྲེལ་བར་ཇི་ལྟར་བརྗོད་ཅེ་ན། དེའི་ཚེ་ཡང་ཐེ་ཚོམ་མེད༌[^695]པ་ཉིད་དེ་དེ་མེད་པ་ཡིན་པའི་ཕྱིར་དེ་ལ་འཇུག་པ་མེད་པས་སྐྱོན་དེ་མེད་པ་ཉིད་དོ། །

[Block 921 [HEADING]]
##### ཕྱོགས་ཀྱི་ཆོས་དགུ་པོའི་དཔེར་བརྗོད། ^3-2-2-4-0

[Block 922]
ཕྱོགས་ཀྱི་ཆོས་དགུ་པོ་དེ་དག་གི་དཔེར་བརྗོད༌[^696]རིམ་པ་བཞིན་དུ་བསྟན་པར་བྱ་སྟེ། དགུ་པོ་འདི་ཡང་མིག་དགུ་ལ་རིམ་པ་བཞིན་བྲིས་ནས་ཕྲེང་གིས་གྱེན་མཐུར་ལ་མཐུན་ཕྱོགས་ཀྱི་གསུམ་མོ། །

[Block 923]
འཕྲེད་ལ་ནི་མི་མཐུན་ཕྱོགས་ཀྱི་གསུམ་མོ། །

[Block 924]
ཕྱོགས་བཞིས་རང་བཞིན་དང་འབྲས་བུ་ལ་སོགས་པར་ཤེས་པར་བྱའོ། །

[Block 925]
སྒྲ་རྟག་སྟེ། གཞལ་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 926]
མི་རྟག་སྟེ་བྱས་པའི་ཕྱིར་རོ། །

[Block 927]
མི་རྟག་པའི་ཕྱིར་རྩོལ་བ་ལས་བྱུང་བའོ། །

[Block 928]
བྱས་པའི་ཕྱིར་རྟག་པའོ། །

[Block 929]
རྟག་སྟེ་མཉན་བྱ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 930]
རྟག་སྟེ་རྩོལ་བ་ལས་བྱུང་བའི་ཕྱིར་རོ། །

[Block 931]
མི་རྟག་པའི་ཕྱིར་རྩོལ་བ་ལས༌[^697]བྱུང་བའོ། །

[Block 932]
རྩོལ་བ་ལས་བྱུང་བའི་ཕྱིར་མི་རྟག་པའོ། །

[Block 933]
རྟག་སྟེ། རེག་པར་བྱ་བ༌[^698]མ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་རྣམས་ཏེ། དེ་དག་གི་བསྡུ་བའི་ཚིགས་སུ་བཅད་པ་ནི།

[Block 934 [VERSE]]
གཞལ་བྱ་བྱས་དང་མི་རྟག་དང་། །
བྱས་དང་མཉན་བྱ་རྩོལ་ལས་བྱུང་། །
མི་རྟག་རྩོལ་བྱུང་རེག་བྱ་མིན། །
དེ་དགུ་རྟག་པ་ལ་སོགས་ལའོ། །

[Block 935]
དེ་ལྟར་དབྱེ་བ༌[^699]

[Block 936 [HEADING]]
#### གཏན་ཚིགས་དང་འགལ་བ་དང་མ་ངེས་པ། ^3-2-3-0

[Block 937]
རྣམས་གཏན་ཚིགས་དང༌[^700]འགལ་བ་དང་། མ་ངེས་པ་ཉིད་དུ་བརྗོད་པར་བྱ་སྟེ།

[Block 938 [VERSE]]
དེར་གང་མཐུན་ཕྱོགས་ལ་ཡོད་གཉིས། །
དེ་མེད་པ་ལ་མེད་པ་སྟེ། །

[Block 939]
དེ་རྟགས། གཉིས་ཁོ་ན་གཏན་ཚིགས་ཏེ། གང་ཞིག་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་དེ་བསྒྲུབ་བྱ་མེད་པ་ལ་མེད་པ་སྟེ།[^701] གང་ཡང་མཐུན་པའི་ཕྱོགས་ལ་མེད་དེ། །གཉིས་བསྒྲུབ་བྱ་མེད་པ་ལ་མེད་པ་ཉིད་ནི་དང་པོ་དང་ཐ་མ༌[^702]གསུམ་པའོ། །

[Block 940]
[^703]དབུས་ན་མོའི་འདི་ལས་བཟློག་པ་ནི། འགལ་བ་སྟེ། ཕྱིན་ཅི་ལོག་ཏུ་སྒྲུབ་པའི་ཕྱིར་རོ།[^704] །

[Block 941]
དེ་ལྟ་བུའི་འགལ་བ་མི་མཐུན་པའི་ཕྱོགས་ལ་ཡོད་པ་གཉིས་པོ་ནི། མཐུན་པའི་ཕྱོགས་ལ་མེད་པ་སྟེ།

[Block 942]
གཉིས་པ་གསུམ་པོའི་ཤར་དང་། ནུབ་ན་མོའི་འགལ་བ་གཞན་ཡང་ཡོད་དེ། གང་བསྒྲུབ་བྱ་ལ་གནོད་པ་སྒྲུབ་པར་བྱེད་པའོ། །

[Block 943]
དཔེར་ན་ཐ་དད་རྣམས་ཀྱི་འདུས་པ་ཉིད་གཞན་གྱི་དོན་སྒྲུབ་པར་བྱེད་པ་ཉིད་ལ་འདུས་པ་ཡིན་པའི་ཕྱིར་གཞན་གྱི་དོན་སྒྲུབ་པོ་ཞེས་བྱ་བ་ལྟ་བུ་སྟེ། དེ་ནི་དུ་མའི་དོན་སྒྲུབ་པ་ཡིན་པའི་ཕྱིར་རྟགས་གཉིས་པོ་ནི༌[^705]ཁོངས་སུ་འདུས་པ་ཉིད་ཡིན་པས་ན་དགུ་པོ་ལས་ཕྱི་རོལ་དུ་གཞན༌[^706]པ་མ་ཡིན་ནོ། །

[Block 944]
གཞན་རྣམས་མ་ངེས་པའོ། །

[Block 945]
ལྷག་མ་རྣམ་པ་ལྔ་པོ༌[^707]ནི་གཏན་ཚིགས་སམ། འགལ་བ་ཉིད་དུ་མ་ངེས་པ་སྟེ། ཐེ་ཚོམ་གྱི་རྒྱུའོ་ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 946 [HEADING]]
#### བརྗོད་པར་འདོད་པའི་གྲངས་གཅིག་ཉིད། ^3-2-4-0

[Block 947]
གཏན་ཚིགས་ལ་སོགས་པ་འདི་དག་ཐམས་ཅད་ལ་ཡང་། བརྗོད་པར་འདོད་པའི་གྲངས་གཅིག་ཉིད། །རིགས་དང་རྫས་ལས་ཤེས་པར་བྱའོ་ཞེས་བྱ་བའི༌[^708]ཚིག་གི་ལྷག་མའོ། །

[Block 948]
གང་ཡང་གྲངས་གཅིག་ཅེས་པ་ནི་འདིར་གང་རིགས་དང་མཐུན་པར་ཡོད་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་དེ་བརྗོད་པར་འདོད་པ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། འགལ་བ་དག་ལ་ཐེ་ཚོམ་ཕྱིར། །གལ་ཏེ་གང་ཕྱིར་འགལ་བ་མཚན་ཉིད་གཉིས་སུ་བརྗོད་པ་དག་ལས་གྲངས་གཅིག་པར་ནི་མཐོང་བ་ཉིད་དེ། དཔེར་ན་སྒྲ་ལ་བྱས་པ་ཉིད་དང་། མཉན་བྱ་དག་ལ་རྟག་པ༌[^709]དང་མི་རྟག་པ་ཉིད་དུ་ཐེ་ཚོམ་ཟ་བ་ཡིན་ནོ་ཞེ་ན།

[Block 949 [VERSE]]
[^710]དེ་བཞིན་ཐེ་ཚོམ་རྟགས་ཉིད་ལས། །
གཅིག་ཏུ་ངེས་པར་མཐོང་མ་ཡིན། །

[Block 950]
དཔེར་ན་སྒྲ་ལ་མིག་གི༌[^711]གཟུང་བྱ་མ་ཡིན་པ་དང་མངོན་སུམ་པ་ཉིད་དག་ལས་སྒྲ་ནི་རྫས་ཀྱང་མ་ཡིན་ལ། ལས་ཀྱང་མ་ཡིན་ནོ་ཞེས་ངེས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
