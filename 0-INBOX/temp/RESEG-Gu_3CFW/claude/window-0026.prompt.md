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
ལེ་ལོ་ཅན་ལ་ནི་བླངས་པ་དང་ཉེ་བར་སྤྱད་པ་བུ་ལོན་དུ་འགྱུར་རོ་ཞེས་བྱ་བ་ནི། ཚུལ་ཁྲིམས་འཆལ་པ་ལ། རྣམ་པ་ཐམས་ཅད་དུ་མི་འོས་པའི་ཕྱིར་རོ། །

[Block 912]
དེ་ནི་ཚུལ་ཁྲིམས་དང་ལྡན་པ་ལ་རིག་པར་བྱའོ། །

[Block 913]
མཚམས་ཀྱི་ནང་ཉིད་ན་གང་ཟག་གི་གཙུག་ལག་ཁང་ངམ་དེའི་རྙེད་པས་འཚོ་བ་ལ་ནི་དགེ་འདུན་གྱི་རྙེད་པ་འོས་སོ་ཞེས་བྱ་བ་ནི་གང་ཟག་གི་གཙུག་ལག་ཁང་ཡོད་པ་དེ་རྙེད་པས་འཚོ་བའོ། །

[Block 914]
གཙུག་ལག་ཁང་དེའི་མཚམས་ཀྱི་ནང་རོལ་དུ་རྙེད་པ་དེ་འོས་པ་ཡིན་ཏེ། ཇི་ལྟར་འགའ་ཞིག་གཙུག་ལག་ཁང་འདི་ལ་སུ༌[^791]གནས་པ་དེ་ལ་རྙེད་པ་འདི་ཙམ་ཞིག་ཁུད་པར་འབུལ་ལོ་ཞེས་དེའི་རྣམ་པ་ན་རྙེད་པ་དེའོ། །

[Block 915]
དེ་བས་ན་འདི་ལ་དགེ་འདུན་གྱིས་བགོ་བར་བྱ་བ་མ་ཡིན་ཏེ་རྙེད་པ༌[^792]བྱུང་ནའོ། །

[Block 916]
ངེས་པའི་གནས་ཁང་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི། རྙེད་པས་འཚོ་ཞིང་དགེ་འདུན་གྱི་རྙེད་པ་ལ་འོས་པའོ། །

[Block 917]
དེ་རེ་མོར་བསྐོའོ་ཞེས་བྱ་བ་ནི་རྙེད་པ་ངེས་པའི་གནས་ཁང་དེ་ཇི་ལྟར་བསྐྱེད་པ་ཉིད་ཀྱིས་ཞེས༌[^793]བྱ་བ་དེ་འདིར་ཐམས་ཅད་དུ་ཇི་ལྟར་བསྐྱེད་པ་ཞེས་བྱ་བ་འདི་ལས་གྲུབ་པ་རིག་པར་བྱའོ། །

[Block 918]
ལྕགས་ལས་བྱས་པའི་སྣོད་སྤྱད་དག་ལས་ལྷུང་བཟེད་དང་ལྷུང་བཟེད་ཆུང་ངུ་དང་ཚ༌[^794]སྣོད་དང་ཟོ་ཕོར་དང་ལྡེ་མིག་ཀྱོག་པོ་དང་གྲི་གུ་དང་ཁབ་དང་སེན་མོ་གཅོད་པ་དང་། ནལ་ཟེ་དང་ཐལ་ཕྱགས་དང་སྟ་རེ་དང་སླང་ང་དང་ཕོར་བུ་དག་ནི་བགོ་བར་བྱ་བ་ཉིད་དོ། །

[Block 919]
སའི་སྣོད་སྤྱད་དག་ལས་ནི་ལྷུང་བཟེད་དང་ལྷུང་བཟེད་ཆུང་ངུ་དང་སླང་ང༌[^795]དང་བུམ་པ་དང་བྱ་མ་བུམ་དང་། གཞོང་པ་དང་རིལ་བ་སྤྱི་བླུགས་དང་ཆུ་སྣོད་རྣམས་སོ་ཞེས་བྱ་བ་ནི་བགོ་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 920]
ཁྲི་ནི་རིན་པོ་ཆེ་ལས་བྱས་པ་ལ་སོགས་པ་མན་ཆད་ནས་ལྕགས་ལས་བྱས་པའི་བར་དག་གོ་ཞེས་བྱ་བ་ནི། ཁྲི་རིན་པོ་ཆེ་ལས་བྱས་པ་ནས་ལྕགས་ལས་བྱས་པའི་བར་ཡན་ཆད་བགོ་བར་བྱ་བ་ཉིད་ཡིན་ནོ། །ཇི་ལྟར་བགོ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཞེས་བྱ་བ་སྨོས་ཏེ། རིན་དུ་བཙོངས་ཏེ་བགོ་བར་བྱ་བའི་དོན་ཏོ། །

[Block 921]
ཤིང་ལས་བྱས་པ་ནི༌[^796]ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཁྲི་ནི་བགོ་བར་བྱ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 922]
ཚོན་རྩི་ནི་ལྔ་ལས་གཞན་པའོ་ཞེས་བྱ་བ་ནི་ཚོན་ཆེན་པོ་ལྔ་ལས་གཞན་པ་དག་བགོ་བར་བྱ་བ་ཉིད་དོ། །

[Block 923]
ཚོན་ཆེན་པོ་རྣམས་ཐམས་ཅད་ཀྱི་ལྔ་པོ༌[^797]ཉིད་ནི་དཔེ་ཙམ་ཡིན་ཏེ། འདིར༌[^798]བསྡུས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །ཅི་གནས་སྐབས་ཐམས་ཅད་དམ་ཞེ་ན། དེའི་ཕྱིར་མ་བསྐོལ་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ་བཀོལ་བ༌[^799]ནི་ཁ་བསྒྱུར་བར་བྱ་བ་ལ་སྦྱར་བར་བྱ་བ་ཉིད་དོ་ཞེས་བྱ་བའི༌[^800]དོན་ཏོ། །

[Block 924]
ཁ་བསྒྱུར་བར་བྱ་བ་གང་ལ་སྦྱར་བར་བྱ༌[^801]ཞེ་ན། དེའི་ཕྱིར། དགེ་འདུན་གྱི་ལའོ། །

[Block 925]
ཀུན་དགའ་ར་བ་དང་གཙུག་ལག་ཁང་དང་དེ་དག་གི་གཞི་དང་གནས་མལ་དག་ནི་བཙོང་བར་བྱ་བ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཡང་ཞེས་བྱ་བའི་སྒྲས་ནི་བགོ་བར་བྱ་བ་ཡང་མ་ཡིན་པར་བསྟན་ཏོ། །

[Block 926]
དེ་དག་གི་གཞི་དང་ཞེས་བྱ་བ་ནི་ཀུན་དགའ་ར་བ་དང་གཙུག་ལག་ཁང་གིའོ། །

[Block 927]
གཞག་པར་བྱ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དེ་དག་གཏར་གཞག་པ་ཉིད་ཀྱང་མ་ཡིན་ཞེས་བྱ་བའི༌[^802]དོན་གྱིས་ཤེས་པར་བྱའོ། །

[Block 928]
བྱིན་གྱིས་བརླབ་པར་བྱ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གང་ཟག་དང་འབྲེལ་པ་ཉིད་ཀྱིས་སྙམ་དུ་དོན་གྱིས་ཤེས་པར་བྱའོ། །

[Block 929]
ཕ་མ་ལ་ཟས་དང་གོས་ཀྱིས་གཏང་བར༌[^803]བྱའོ་ཞེས་བྱ་བ་སྨོས་ན། ཇི་ལྟར་གཏང་བར༌[^804]བྱ་ཞེ་ན། དེའི་ཕྱིར། གལ་ཏེ་ལྷུང་བཟེད་དང་ཆོས་གོས་ལས་ལྷག་པའི་རྙེད་པ་མེད་པ༌[^805]ན་བསླངས་ཏེའོ། །

[Block 930]
མ་གྲུབ་ན་ཟན་གྱི་སྐལ་བ་ལས་ཕྱེད་སྦྱིན་ནོ་ཞེས་བྱ་བ་ལ། མ་གྲུབ་ན་ཞེས་བྱ་བ་ནི་བསླངས་པ་ལ་དེ་རུང་བའི་གང་ཟག་མ་བརྗོད་པའམ། བསླང་བར་མི་ནུས་པ་ལ་རྙེད་པ་སྟེ། ཕྲན་ཚེགས་ཀྱི་གཞི་ལ་སོགས་པར་གཏོགས་པའོ། །

[Block 931]
བྱེ་བྲག་ཤེས་པར་བྱ་བའི་ཕྱིར་ཆོས་གོས་དག་ལ་ཐིག་ལེ་བྱའོ་ཞེས་བྱ་བ་ནི་མི་ནོར་བར་བྱ་བའི་ཕྱིར་མཚན་མ་འདིའོ། །

[Block 932]
སྲི༌[^806]ཥུ་སྲི༌[^807]ཥུ་སྲི༌[^808]ཥུ་ཆག་ཆག་འདེབས་པར་བྱེད་པའོ་ཞེས་འདིར་ཟུར་ཆག་པའི་ཁམས་སོ། །

[Block 933]
འདིར་གཞུང་ནི་དགེ་སློང་དག་ཁྱེད་ཀྱིས། དགེ་སློང༌[^809]མཛེས་དགའ་བོའི་ཆོས་གོས་དག་ལ་ཐིག་ལེ་བྱོས་ཤིག་དང་འདི་ནི༌[^810]མཛེས་དགའ་བའོ། །

[Block 934]
འདི་ནི་བཅོམ་ལྡན་འདས་སོ་ཞེས༌[^811]ཤེས་པར་འགྱུར་རོ་ཞེས་བྱ་བ༌[^812]གསུངས་པ་ཡིན་ནོ། །

[Block 935]
དེ་དག་ལ་མཚན་མ་གདབ་བོ༌[^813]ཞེས་བྱ་བ་ལ། དེ་དག་ལ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་དེ་དག་ལའོ། །

[Block 936]
སྣག་ཚའི་ཐིག་ལེ་ནི༌[^814]དེས་ཞེས་བྱ་བའོ༌[^815]ཞེས་བྱ་བ་ལ། དེས༌[^816]ཞེས་བྱ་བ་ནི་མཚན་མ་གདབ་པ་དེའོ། །

[Block 937]
ལུང་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་དག་ལ་གདགས་སོ་ཞེས་པར་སྦྱར་རོ། །

[Block 938]
ཁ་ཚར་དང་ཕུན་ཚར་གྱི་མཐའ་རང་ཆག་བྱའོ། །

[Block 939]
སྣམ་སྦྱར་མ་ཡིན་པ་དག་ལ་དྲས་ཏེ་བྱིན་གྱིས་བརླབ་པར་ངེས་པ་མེད་དོ་ཞེས་བྱ་བ་ནི། དྲས་ཤིང་དྲུབས་པ༌[^817]ཆོས་གོས་ཉིད་དུ་བྱིན་གྱིས་བརླབ་པར་བྱའོ་ཞེས་བྱ་བ་ལས་སྣམ་སྦྱར་གྱི་ཆོ་ག་གང་ཞིག་མི་འདོད་པ་འདི་དང་འདྲ་བའི༌[^818]དབྱེ་བས་སོ། །

[Block 940]
རྐྱེན་དེ་ལྟ་བུ་དག་ལ་དེ་དང་དེའི་རྒྱན་མེད་ན་གཞན་ལ་དངོས་གཞིའི་རྙེད་པ་མ་གྲུབ་པ་ལ། གདོད་ཁས་བླངས་པ་དབུལ་བ་ཞེས་བྱ་བ་ནི་ཕ་མ་དག་རུང་བའི་བསམ་པས་དྲས་ཤིང་དྲུབས་པ་མ་ཡིན་པ་ལ་ཡང་དེ་ཡོད་པར་འགྱུར་ཞེས་བྱ་བ་དེ་བས་ན་དེ་ལ་འདི་བྱེད་པའོ། །

[Block 941]
འདིར་གཞུང་ནི་བཙུན་པ་ཆོས་གོས་མ་དྲས་པ་བྱིན་གྱིས་བརླབ་ཏུ་རུང་ངམ། ཉེ་བ་འཁོར་མི་རུང་ངོ་། །རྐྱེན་དེ་ལྟ་བུ་དག་ན་ནི་རུང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 942]
འདི་ལྟར་འདིར་ཆོས་གོས་གསུངས་པ་ནི་སྣམ་སྦྱར་ཁོ་ན་ཡིན་པར་རྣམ་པར་གནས་པའི་ཕྱིར་རོ། །

[Block 943]
དེར་ཇི་ལྟར་མངོན་ཞེ་ན། འདི་ལྟར་བླ་གོས་དང་མཐང་གོས་གཉིས་མ་དྲས་པ༌[^819]གང་ཡིན་པ་དེས་ནི་ཆ་ལུགས་རྫོགས་པའི་ཕྱིར་རོ། །

[Block 944]
མ་མོ་ལས།

[Block 945]
སྣམ་སྦྱར་འདི་དྲ་བར་བྱའོ། །

[Block 946]
བླ་གོས་ནི་ངེས་པ་མེད་པ་དང་། མཐང་གོས་ཀྱང་ངེས་པ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 947]
རྐྱེན་དེ་ལྟ་བུ་དག་མེད་པར་མ་དྲས་པ༌[^820]དེས་གྲོང་དང་ཁྱིམ་གཞན་དག་ཏུ་འདུག་པ་དང་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས་བྱ་བ་ནི་སྣམ་སྦྱར་དེས་སོ། །

[Block 948]
འདིར་གཞུང་ནི། བཙུན་པ་ཆོས་གོས་མ་དྲས་པས༌[^821]གྲོང་ཁྱེར་དུ་འཇུག་པར་རུང་ངམ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 949]
འདིར་སྣམ་སྦྱར་གྱི་དགོངས་པ་ཡང་ལུང་དང་རིགས་པ་འདི་དང་སྔ་མ་གཉིས་ཀྱིས་ནི་འདིར་ཆོས་གོས་ཞེས་སྨོས་པ་ནི་སྣམ་སྦྱར་ཡིན་པར་དགོངས་པར་རིགས་སོ། །

[Block 950]
དེ་བས་ན་འདི་ལྟར་འདིར་མདོར་བྱས་པའོ། །
--- END BLOCKS ---
