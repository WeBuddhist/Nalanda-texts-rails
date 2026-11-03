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
ལན་དུ་སྔོན་དུ་འགྲོ་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་གསུངས་ཏེ། སངས་རྒྱས་ཀྱི་ཆོས་བྱེད་དོ་ཅོག་ཐམས་ཅད་བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་གི་དོན་སྒྲུབ་པའི་ཕྱིར་མ་ཡིན་གྱི། མཐའ་ཡས་པའི་སེམས་ཅན་རྣམས་འཁོར་བའི་དགོན་པ་ན་འཁྱམས་པ༌[^789]རྣམས་ལ་ཐུགས་བརྩེ་སྟེ། དེ་དག་བསྒྲལ་བའི་ཕྱིར་སངས་རྒྱས་སུ་བསྒྲུབས་པས༌[^790]དེ་དག་གི་རྒྱུ་སྙིང་རྗེ་ཆེན་པོ་ཡིན་པའི་ཕྱིར་སྔོན་དུ་འགྲོ་བ༌[^791]ཞེས་བྱ༌[^792]སྟེ། དེ་བས་ན་འབྲས་བུ་མི་ཟད་པས་རྒྱུ་ཡང་མི་ཟད་པའོ། །

[Block 912]
གཉིས་སུ་ན་བྱང་ཆུབ་སེམས་དཔའི་ཡོན་ཏན་ནོ། །

[Block 913]
ཚོགས་ཀྱི་ནང་ན་སྙིང་རྗེ་གཙོ་བོ་ཡིན་པས་ཐོག་མར་འགྲོ་བའོ༌[^793]ཞེས་བྱ༌[^794]སྟེ། སྲོག་གི་དབང་པོ་ལ་སོགས་པའི་དཔེས་བསྟན་པ་ལྟ་བུའོ། །

[Block 914]
ཆོས་ཐམས་ཅད་ཀྱི་མཆོག་ཏུ་གྱུར་པ་བཤད་ཟིན་ཏོ།། །།

[Block 915 [HEADING]]
#### ངེས་པའི་ཚིག། ^2-2-2-0

[Block 916]
ངེས་པའི་ཚིག་བསྟན་པའི་ཕྱིར། བཙུན་པ་ཤ་ར་དྭ་ཏིའི་བུ་སྙིང་རྗེ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་ཞེས་བྱ༌[^795]བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 917]
བདག་ཉིད་ཀྱིས་བྱ་བས་ན༌[^796]དེའི་ཕྱིར་སྙིང་རྗེ་ཆེན་པོ་ཞེས་བྱའོ་ཞེས་བྱ་བ་ལ། སྙིང་རྗེ་དེའི་ཚིག་གི་དོན་ནི་བྱ་བ་ཞེས་བྱ་བའི་སྒྲར་འགྲོ་བས་དགེ་བའི་རྩ་བ་ཐམས་ཅད་བདག་ཉིད་ཀྱི་བྱ་བ་ཡིན་པས་ངེས་པའི་ཚིག་ཏུ་ན་དེའི་ཕྱིར་སྙིང་རྗེ་ཞེས་བྱའོ། །

[Block 918]
རང་གི་བྱ་བས་ན་ཞེས་བྱ་བ་ནི་བདག་དང་གཞན་གྱི་དོན་ཀྱང་རང་ཉིད་ཀྱི་བྱ་བས་ན་དེའི་ཕྱིར་སྙིང་རྗེ་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 919]
གཞན་གྱི་སྐབས་མི་རྙེད་པས་ན་ཞེས་བྱ་བ་ནི་དགེ་བ་དང་ལས་སུ་བྱ་བ་ཐམས་ཅད་གཞན་གྱིས་བྱ་ཞིང་གཞན་ལ་བཅོལ་ཏེ་བྱེད་དུ་གཞུག་པ་མེད་པས་གཞན་གྱི་སྐབས་མི་རྙེད་པ་ཞེས་བྱ་སྟེ། དེ་བས་ན་སྙིང་རྗེ་ཆེན་པོའོ། །

[Block 920]
ངེས་པའི་ཚིག་བཤད་ཟིན་ཏོ།། །།

[Block 921 [HEADING]]
#### རྒྱུ་དང་རང་བཞིན། ^2-2-3-0

[Block 922]
རྒྱུ་དང་རང་བཞིན་བསྟན་པའི་ཕྱིར། གཡོ་བ་མེད་པ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 923]
ཚིག་སྔ་མ་སྔ་མ་ནི་རྒྱུའོ། །

[Block 924]
ཕྱི་མ་ཕྱི་མ་ནི་རང་བཞིན་ནོ། །

[Block 925]
དེ་ལ་སེམས་ཅན་རྣམས་ལ་བྲིད་ཅིང་སླུ་བར༌[^797]སེམས་པའམ། བྱ་བ་ཐམས་ཅད་ལ་སྙིང་ཐག་པ་ནས་བྱེད་པ་མ་ཡིན་གྱི་ངན་ངོན་ཙམ་གསོག་སྙིང་པོ་མེད་པར༌[^798]བྱེད་པ་ནི་གཡོ་སྟེ། དེ་ལྟ་བུ་མེད་པའི་རྒྱུ་ལས་སྙིང་རྗེ་ཆེན་པོ་བྱུང་བས་ན་སྙིང་རྗེ་ཆེན་པོ་ནི་བསམ་པ་ཐག་པ་ནས་བྱ་བ་སྟེ། སྙིང་རྗེ་དང་ལྡན་པ་ལ་སེམས་ཅན་བྲིད་ཅིང་སླུ་བ་མེད་ལ། བྱ་བ་ཐམས་ཅད་སྙིང་པོར་གྱུར་པ༌[^799]ཤ་སྟག་བྱེད་པའི་ཕྱིར་རོ། །

[Block 926]
རྒྱུ་མེད་པ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ལ། རྒྱུ་ནི་ཚིག་ཏུ་སྨྲས་ཀྱང་དོན་དུ་མི་སྒྲུབ་པ་སྟེ། དེ་ལྟ་བུ་མེད་པའི་སེམས་ལས་བྱུང་བས་ན། སྙིང་རྗེ་ཆེན་པོ་ནི་སྦྱོར་བ༌[^800]བྱ་བ་སྟེ། ཐམས་ཅད་སྒྲུབ་པར་བྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 927]
ཕྱིར་མི་ལྡོག་པ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ལ། བླ་ན་མེད་པའི་བྱང་ཆུབ་སྒྲུབ་པ་དང་། སེམས་ཅན་གྱི་དོན་བྱ་བ་ལ་སླར་ནུར་བ་མེད་པའི་སེམས་ཀྱི་རྒྱུ་ལས་བྱུང་བས་ན། སྙིང་རྗེ་ཆེན་པོ་ནི་ལྷག་པའི་བསམ་པས་བྱ་བ་སྟེ། ལྷག་པའི་བསམ་པ་དང་ལྡན་པ་རྣམས་ཀྱིས༌[^801]བྱ་བ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 928]
མ་བཅོས་པ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ནི་ལུས་དང་ངག་དང་ཡིད་ཀྱི་རང་བཞིན་གཞན་དུ་གནས་ལ་གཞན་དུ་བསྟན་པ༌[^802]ནི་བཅོས་པ་སྟེ། དེ་ལྟ་བུ་མེད་པར་རང་བཞིན་ཇི་ལྟར་གནས་པ་དེ་བཞིན་དུ་སྟོན་པའི་རྒྱུ་ལས་བྱུང་བས་ན་སྙིང་རྗེ་ཆེན་པོའི་རང་བཞིན་གྱིས༌[^803]རིག་པ་སྟེ་བདག་གིས་རང་བཞིན་ཇི་ལྟ་བ་ཉིད་ལས་གཞན་དུ་སྟོན་པར་མི་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 929]
ལམ་དྲང་པོ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ནི་རྟག་པ་དང་ཆད་པར་ལྟ་བ་དང་། ཡོད་པ་དང་མེད་པར་ལྟ་བའི་ལམ་ངན་པའི་དྲི་མ་ཐམས་ཅད་སྤངས་པ་མྱ་ངན་ལས་འདས་པར་འགྲོ་བར་བྱེད་པ། འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པའི་རྒྱུ་ལས་བྱུང་བས་ན་སྙིང་རྗེ་ཆེན་པོའི་རང་བཞིན་གྱིས་ཡོངས་སུ་དག་པ་སྟེ། ལམ་ངན་པའི་སྐྱོན་དང་མ་འདྲེས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 930]
གསལ་བ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ལ། སྨྲས་པའི་དོན་རླུང་བསྐུར༌[^804]ཏེ་གསལ་བར་མི་སྟོན་པ་ནི་གྱ་གྱུར་ཞེས་བྱ་སྟེ། དེ་ལྟ་བུ་མེད་པའི་མཚན་ཉིད་གསལ་བའི་རྒྱུ་ལས་འབྱུང་བས་ན་སྙིང་རྗེ་ཆེན་པོ་ནི་སེམས་གྱ་གྱུ་མེད་པའོ། །

[Block 931]
སེམས་ཅན་ཐམས་ཅད་ལ་འདུད་པ་ལས་བྱུང་བ་ཞེས་བྱ་བ་ནི་སྙིང་རྗེ་ཅན་དེ་འཕགས་པ་དང་འཕགས་པ༌[^805]མ་ཡིན་པའི་སེམས་ཅན་དང་། སེམས་ཅན་བཙུན་པ་དང་། མི་བཙུན་པ་ཐམས་ཅད་ལ་རྟག་ཏུ་ཕྱག་འཚལ་བར་བྱེད་པས་སྙིང་རྗེ་ཆེན་པོ་ནི་ང་རྒྱལ་མེད་པའོ། །

[Block 932]
སེམས་ཅན་ཚད་མེད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གྱི་ཁམས་ནི་ཚད་མེད་དེ། འདི་ཙམ་ཞེས་གཅད་པར༌[^806]མི་ནུས་སོ། །

[Block 933]
དེ་ལྟར་སེམས་ཅན་ཚད་མེད་པ་ལ་སྙིང་རྗེ་ཆེན་པོས་དམིགས་ནས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཀྱི་འབྲས་བུ་ཐོབ་པས་ན། སྙིང་རྗེ་ཆེན་པོ་ནི་ཚད་མེད་པ་ལས་བྱུང་བའོ། །

[Block 934]
དེ་བཞིན་གཤེགས་པའི་སྐུ་འཐོབ་པ་ལས་བྱུང་བས་ཞེས་བྱ་བ་ནི་བདག་གི་ལུས་ལས་དང་ཉོན་མོངས་པས་བསྐྱེད་པ་འདི་ལ་མ་ཆགས་པར་དེ་བཞིན་གཤེགས་པའི་སྐུ་གསུམ་ཐོབ་པར་བྱའོ་ཞེས་དམིགས་པའི་རྒྱུ་ལས་བྱུང་བས་ན༌[^807]སྙིང་རྗེ་ཆེན་པོ་ནི་བདག་གི་ལུས་ལ་མི་ལྟ་བ་སྟེ། དོན་ཆེན་པོའི་ཕྱིར་བདག་གི་ལུས་ལ་གཅེས་པར་མི་འཛིན་པའོ། །

[Block 935]
སྡིག་པ་ཐམས་ཅད་མི་བྱ་བ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ནི་བདག་གི་དོན་དུ་སྲོག་གི་ཕྱིར་ཡང་སྲོག་གཅོད་པ་དང་། མ་བྱིན་པར༌[^808]ལེན་པ་ལ་སོགས་པའི་སྡིག་པ་ཐམས་ཅད་མི་བྱའོ་ཞེས་དམིགས་པའི་རྒྱུ་ལས་བྱུང་བ་ནི་སྙིང་རྗེ་ཆེན་པོ་ནི་སྲོག་ལ་ཡིད་མི་རྟོན་པ་སྟེ། སྲོག་གི་ཕྱིར་སྡིག་པ་མི་བྱེད་པའོ། །

[Block 936]
བྱང་ཆུབ་ཀྱི་སེམས་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་མི་དགེ་བའི་གནས་ནས་སྤྱོད༌[^809]དེ། དགེ་བའི་གནས་སུ་བཀོད་ནས་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཏུ་བསྒྲལ་ལོ་ཞེས་སེམས་བསྐྱེད་པའི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་རྒྱུ་ལས་བྱུང་བས་ན་སྙིང་རྗེ་ཆེན་པོ་ནི་ཕ་རོལ་སྲུང་བ༌[^810]སྟེ། སེམས་ཅན་ཐམས་ཅད་མི་དགེ་བའི་གནས་སུ་མི་གཏོང་བར་བྱེད་པའོ། །

[Block 937]
རང་གི་སེམས་ཡོངས་སུ་དག་པ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ལ། [^811]གཞན་གྱི་སྲོག་ལ་མི་གནོད་པ་དང་། ལོངས་སྤྱོད་ལ་སོགས་པ་ལ་མི་གནོད་པའི་སེམས་ནི་སེམས་ཡོངས་སུ་དག་པའོ། །

[Block 938]
དེ་ལྟར་ཡོངས་སུ་དག་པའི་སེམས་ཀྱི་རྒྱུ་ལས་བྱུང་བས་ན། སྙིང་རྗེ་ཆེན་པོ་ནི་སེམས་ཅན་སྲུང་བ༌[^812]སྟེ། སེམས་ཅན་གྱི་སྲོག་དང་། ལོངས་སྤྱོད་གང་ལ་ཡང་གནོད་པར་མི་བྱེད་པའོ། །

[Block 939]
སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྡུག་བསྔལ་སེལ་བ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ལ། སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྡུག་བསྔལ་ནི་མདོར་ན་གསུམ་སྟེ། ལོངས་སྤྱོད་ཀྱིས་ཕོངས་པའི་སྡུག་བསྔལ་དང་། བདེ་འགྲོར་སྐྱེས་ནས་ཡང་ན་བ་དང་ཚ་བའི་སྡུག་བསྔལ་དང་། ངན་སོང་དུ་སྐྱེས་པའི་སྡུག་བསྔལ་དང་། ཐར་པ་འདོད་པས་ཀྱང་དེའི་ལམ་སྟོན་པ་མེད་པའི་སྡུག་བསྔལ་ལོ། །

[Block 940]
སྡུག་བསྔལ་དེ་གསུམ་བསལ་བར་བྱའོ་ཞེས་དམིགས་པའི་རྒྱུ་ལས་བྱུང་བས་ན་སྙིང་རྗེ་ཆེན་པོ་ནི་དབུལ་པོ་ལ་སོགས་པ་ལ་ལྟ་བ་སྟེ། ལོངས་སྤྱོད་ཀྱིས་ཕོངས་པའི་སྡུག་བསྔལ་བསལ་བར་བྱའོ་སྙམ་པའི་དམིགས་པའི་རྒྱུ་ལས་བྱུང་བས་ན། དབུལ་པོ་ལ་ལྟ་བའོ། །

[Block 941]
བདེ་འགྲོར་སྐྱེས་ནས་ཡང་ན་བ་དང་ཚ་བའི་སྡུག་བསྔལ་དང་། ངན་སོང་དུ་སྐྱེས་པའི་སྡུག་བསྔལ་བསལ་བར་བྱའོ་སྙམ་པའི་དམིགས་པའི་རྒྱུ་ལས་བྱུང་བས༌[^813]སྡུག་བསྔལ་བ་ལ་ལྟ་བའོ། །

[Block 942]
ཐར་པ་འདོད་ཀྱང་དེའི་ལམ་སྟོན་པ་མེད་པའི་སྡུག་བསྔལ་བསལ་བར་བྱའོ་སྙམ་པའི་དམིགས་པའི་རྒྱུ་ལས་བྱུང་བས་ན་མགོན་མེད་པ་ལ་ལྟ་བའོ། །

[Block 943]
བློ་མི་འགྱུར་བ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ཁས་བླངས༌[^814]ཤིང་དམ་བཅས་པ་ལས་འགྱུར་བ་མེད་པའི་སེམས་ལས་བྱུང་བས་ན་སྙིང་རྗེ་ཆེན་པོ་ནི་དམ་བཅས་པ་བརྟན་པ་སྟེ། དམ་བཅས་པ་ལས་གཞན་དུ་མི་འགྱུར་བའོ། །

[Block 944]
བདག་དང་སངས་རྒྱས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། བདག་ནི་དགེ་བ་བྱེད་པའི་གང་ཟག་གམ། ཚུལ་ཁྲིམས་བླངས་པའི་གང་ཟག་གོ། །

[Block 945]
སངས་རྒྱས་ནི་སྟོན་པ་དེ་བཞིན་གཤེགས་པའོ། །

[Block 946]
ལྷ་ནི་ཚུལ་ཁྲིམས་ལེན་པའི་ཚེ་ན་དབང་དང་། སྲུང་མར་གྱུར་པའི་ལྷ་རྣམས་སོ། །

[Block 947]
ཚུལ་ཁྲིམས་ཉམས་པར་བྱས་སམ་སྡིག་པ་བྱས་པ་ནི་དེ་གསུམ་ཆར་བསླུས་པ་ཡིན་ཏེ། སྙིང་རྗེ༌[^815]ནི་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པ་བདག་དང་སངས་རྒྱས་དང་། ལྷ་གསུམ་མི་བསླུ་བའི་རྒྱུ་ལས་བྱུང་བས་ན་བདེན་པ་ལ་ལྟ་སྟེ་བདེན་པར་བྱེད་པའོ། །

[Block 948]
ལེགས་པར་བྱས་པའི་ལས་ལས་བྱུང་བ་ཞེས་བྱ་བ་ནི་ལུས་ཀྱིས་སྲོག་མི་གཅོད། མ་བྱིན་པར་མི་ལེན། འདོད་པས་ལོག་པར་མི་གཡེམ་པ་ལ་སོགས་པ་དགེ་བ་བཅུའི་ལས་ལས་བྱུང་བས་ན། སྙིང་རྗེ་ཆེན་པོ་ནི་སྤྱོད་པ་དག་པ་སྟེ། ལུས་དང་ངག་དང་ཡིད་ཀྱི་སྤྱོད་པ་ལ་སྐྱོན་མེད་པའོ། །

[Block 949]
ཕ་རོལ་བདེ་བ་རབ་ཏུ་སྦྱིན་པ་ལས་བྱུང་བ་ཞེས་བྱ་བ་ནི་བདག་གི་བདེ་བ་དང་ལོངས་སྤྱོད་ཐམས་ཅད་ཀྱང་སེམས་ཅན་གཞན༌[^816]ལ་གཏོང་བའི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་རྒྱུ་ལས་བྱུང་བས་ན་སྙིང་རྗེ་ཆེན་པོ་ནི་བདག་གི་བདེ་བ་གཏོང་བ་སྟེ། བདག་བདེ་བ་ལ་གནས་པར་མི་བྱེད་པའོ། །

[Block 950]
སྲེད་པ་མེད་པ་ལས་བྱུང་བས་ན་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གཞན་ལ་མི་བདེ་བར་གྱུར་པ༌[^817]གཞན་གྱི་ལུས་དང་ལོངས་སྤྱོད་ལ་ཆགས་པ་མེད་པའི་ཚུལ་ཁྲིམས་ཀྱི་རྒྱུ་ལས་བྱུང་བས་ན་སྙིང་རྗེ་ཆེན་པོ་ནི་གཞན་གྱི་བདེ་བ་བསྐྱེད་པ་སྟེ། གཞན་གྱི་ལུས་དང་ལོངས་སྤྱོད་འཕྲོག་པ་ལ་སོགས་པའི་མི་བདེ་བ་སྐྱེད་པར༌[^818]མི་བྱེད་པའོ། །
--- END BLOCKS ---
