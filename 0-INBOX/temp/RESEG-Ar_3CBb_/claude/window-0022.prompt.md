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
[Block 771 [VERSE]]
ཐམས་ཅད་དུ་ནི་རབ་ཏུ་སྟོན། །
ཞེས་བྱ་བ་དེ་ཉིད་ཀྱིས་བཤད་དོ། །
མངོན་སུམ་སངས་རྒྱས་འདྲ་བ་ཡི། །
སློབ་དཔོན་སྨོད་ཅིང་བཀུར༌[^362]མི་བྱེད། །

[Block 772]
ཞེས་པ་ནི་བླ་མའི་བསྲུང་བར་བྱ་བའི་སྡོམ་པ་ལ་ཕྱལ་བར་གཏོང་བའོ། །

[Block 773]
སྐད་ཅིག་གིས་ནི་ཁོང་ཁྲོ་ཞིང་། །ཞེས་པ་ནི་ཉེས་པ་མཐོང་ན་སྐད་ཅིག་ཙམ་གྱིས་ཁྲོ་བར་བྱེད་པའོ། །

[Block 774]
དེ་བཞིན་སྐད་ཅིག་གིས་རྗེས་ཆགས། །ཞེས་པ་ནི་བདག་ཉིད་དང་རྗེས་སུ་མཐུན་པའི་ལས་བྱུང་ན་ཆགས་པར་བྱེད་པའོ། །

[Block 775]
འདི་དག་གིས་ནི་བློ་མི་བརྟན་པ་བསྟན་ཏོ།[^363] །དེ་ནས་འདོད་པས་ལོག་པར་གཡེམ་པ་ལ་སོགས་པའི་ཉེས་པ་བསྟན་པའི་ཕྱིར། མ་དང་སྲིང་མོ་བུ་མོ་སྟེ། །ཞེས་པ་ནི་བདག་ཉིད་བསྐྱེད་པ་དང་། བདག་ཉིད་དང་ལྷན་ཅིག་ཏུ་བསྐྱེད་པ་དང་བདག་གིས་བསྐྱེད་པའོ། །

[Block 776]
དེ་དག་གིས་ནི་བགྲོད་པ་མ་ཡིན་ཏེ་དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱིས་རྨད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 777]
དེ་ལ་བགྲོད་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་ཉེས་པ་མཆོག་དང་ལྡན་པ་ཡིན་ཞེས་སྦྱར་རོ། །

[Block 778]
ཉེས་པ་གཞན་ཡང་ཡོད་པའི་ཕྱིར། །ཕ་མ་གསོད་ཅིང་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ་ཕ་མ་གསོད་པ་ནི་ཕ་མ་གསོད་པས་ཏེ། ཕ་མ་ལ་ངན་སེམས་ཀྱིས་ཚོན་རྡེག་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 779]
སྲོག་ཆགས་གཞན་ཡང་གསོད་པར་བྱེད། ཅེས་པ་ནི་འཇིག་རྟེན་གྱི་སྲོག་ཆགས་རགས་པ་དང་ཕྲ་བ་ལ་སོགས་པ་གསོད་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 780]
དེ་བཞིན་བརྫུན་གྱི་ཚིག་སྨྲ་ཞིང་། །ཞེས་པ་ནི་གང་ཞིག་བདེན་པར་སྨྲ་བ་སྤངས་པའོ། །

[Block 781]
ཁྱད་པར་དུ་ཡང་རྐུ་བར་བྱེད། །ཅེས་པ་ནི་གང་གིས་མ་བྱིན་པར་ལེན་པར་བྱེད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 782]
གཞན་གྱི་ཆུང་མའི་ཐད་འགྲོ་ཞིང་། །ཞེས་པ་ནི་གཞན་གྱི་ཆུང་མ་ལ་ཉེ་བར་སྦྱོར་བའོ། །

[Block 783]
སྨད་པ་གཞན་ཡང་བྱེད་པར་འགྱུར། །ཞེས་པ་ནི་བསྟན་བཅོས་ལས་སྨད་པའི་བྱ་བ་གཞན་ཐམས་ཅད་ལྷུར་ལེན་པར་འགྱུར་ཞེས་པའི་དོན་ཏོ། །

[Block 784 [VERSE]]
དེ་ཉིད་ཡེ་ཤེས་འབྱུང་བ་ཡི། །
དམ་ཚིག་རྣམས་ནི་དེས་མི་ཤེས། །

[Block 785]
ཞེས་པ་ནི་གསང་བ་ཆེན་པོ་མཆོག་གི་དམ་ཚིག་རྒྱས་པ་དེ་ཉིད་ཀྱིས་མི་ཤེས་ཞེས་པའི་དོན་ཏོ། །

[Block 786 [VERSE]]
ཉེས་པ་ཅུང་ཟད་ཙམ་ལ་ཡང་། །
མངོན་སྤྱོད་དག་ནི་བྱེད་པར་འགྱུར། །

[Block 787]
ཞེས་པ་ནི་ཉེས་པ་ཕྲ་མོ་ཙམ་ལ་ཡང་དྲག་པོའི་ལས་རྩོམ་ཞེས་པའི་དོན་ཏོ། །

[Block 788]
རྟག་ཏུ་ཕྱི་རོལ་བསྟན་བཅོས་དགའ། །ཞེས་པ་ནི་གཞུང་འདི་པ་མ་ཡིན་པའི་བསྟན་བཅོས་ལ་གཞོལ་བ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 789]
རང་གི་དམ་ཚིག་ཡོངས་སྤངས་ཏེ། །ཞེས་པ་ནི་རང་གི་དམ་ཚིག་མི་བསྲུང་བའོ། །

[Block 790]
ལྕགས་ཀྱུ་མེད་པ་བཞིན་དུ་སྤྱོད། །ཅེས་པ་ནི་ཐབས་དང་བྲལ་བ་ཉིད་དོ། །

[Block 791]
སྔགས་དང་ཕྱག་རྒྱའི་སྦྱོར་བ་ཡི།[^364] །འཚོ་བ་དག་ནི་ངེས༌[^365]སྒྲུབ་བྱེད། །ཅེས་པ་ནི་སྔགས་དང་ཕྱག་རྒྱས་རང་གི་འཚོ་བ་ཡོངས་སུ་ཚོལ་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 792 [VERSE]]
གང་དུ་རྙེད་པ་ཐོབ་འགྱུར༌[^366]བར། །
དམ་པའི་ཆོས་ནི་འཆང་བར་འགྱུར། །

[Block 793]
ཞེས་པ་ནི་ཡུལ་དུ༌[^367]ཤེས་པ་དང་མི་ལྡན་ཞིང་རྙེད་པ་ཉེ་བར་ཐོབ་པར་འགྱུར་བར་དམ་པའི་ཆོས་འཆད་པར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 794]
དེས་ཅིར་འགྱུར་ཞེ་ན། སྔགས་པ་རྣམས་ནི་འགྲུབ་མི་འགྱུར། །ཞེས་སྨོས་ཏེ་དེ་ལྟ་བུའི་གང་ཟག་གིས་སྔགས་དང་ཕྱག་རྒྱའི་དངོས་གྲུབ་འགྲུབ་པ་མེད་ཀྱི་མནར་མེད་པའི་སྡུག་བསྔལ་ཆེན་པོ་སྐྱེད་ཅེས་པའི་དོན་ཏོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། རྣལ་འབྱོར་རབ་སྦྱོར་དམན་པའི་ཕྱིར། །ཞེས་སྨོས་ཏེ། རབ་ཏུ་སྦྱོར་བ་དམན་པ་ནི་རབ་ཏུ་སྦྱོར་བ་ཞན་པ་ཞེས་པའི་དོན་ཏོ། །

[Block 795]
དེ་རྣམས་གཟུང་བར་བྱ་བའི་ཕྱིར། །ཞེས་པ་ནི་དེ་རྣམས་ཀྱི་ངན་འགྲོའི་སྲིད་པ་དགག་པའི་ཕྱིར༌[^368]ཞེས་པའི་དོན་ཏོ། །

[Block 796]
གསང་བ་དགོངས་པས་བཤད་པ་ཡིན། །ཞེས་བྱ་བ་ནི་བཤད་ཟིན་ཏོ། །

[Block 797]
འདིས་ནི་བསྡུས་པའི་དོན་བསྟན་ཏོ་ཞེས་པ་ནི་འདི་ཉིད་ཀྱིས་བསྡུས་པའི་དོན་ཡིན་གྱི་རྒྱས་པར་བཤད་པ་ནི་མ་ཡིན་ནོ། །

[Block 798]
གང་ཞིག་གང་དུ་གང་གི་ཕྱིར་བསྟན་པ་ཡིན་ཞེ་ན། དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པའི་དོན་མཐའ་དག་དང་། དེ་བཞིན་གཤེགས་པའི་གསང་བ་འདུས་པའི་བཤད་པ་མཐའ་དག་བསྡུས་པའི་དོན་འདི་ཉིད་ཀྱིས་བསྡུས་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 799]
འདིས་ཀྱང་བསྡུས་པ་ལ་དགའ་བ་རྣམས་འདི་ཙམ་གྱིས་ཚིམ་པར་འགྱུར༌[^369]ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 800 [HEADING]]
## ཡན་ལག་གི་དོན་རྣམ་པར་དབྱེ་བའི་ཕྱིར་རྒྱུད་ལ་འཇུག་པ། ^4-0

[Block 801]
དེ་ལྟར་བསྡུས་པའི་དོན་བསྟན་ནས་ཞེས་པ་ནི་རྒྱས་པར་བསྟན་པར་བཤད་པར་འདོད་པས་དེ་སྐད་ཅེས་བྱའོ། །

[Block 802]
ད་ནི་ཞེས་བྱ་བ་ནི་སྐབས་ལ་བབ་པའི་ཚིག་གོ། །

[Block 803]
ཡན་ལག་གི་དོན་རྣམ་པར་དབྱེ་བའི་ཕྱིར་ཞེས་པ་ནི་རྩ་བའི་དོན་མ་ཡིན་པའི་ཕྱིར་དེ་སྐད་ཅེས་བྱའོ། །

[Block 804]
རྒྱུད་ལ་འཇུག་པར་བྱ་སྟེ་ཞེས་པ་ནི་རྒྱུད་ཉིད་བཤད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 805]
འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་བྱ་བ་འདི་ཡང་གང་གིས་གང་ལ་བསྟན་ཞེ་ན། འདིར་སྡུད་པར་བྱེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ་སྡུད་པར་བྱེད་པ་ནི་སྡུད་པར་བྱེད་པ་སྟེ་དེ་བཞིན་གཤེགས་པའི་རྒྱུད་ཐོབ་པར་བྱེད་ཅེས་པའི་དོན་ཏོ། །

[Block 806]
ཐོས་པར༌[^370]བྱེད་པ་པོ་གང་ཡིན་ཞེ་ན། འཕགས་པ་ཕྱག་ན་རྡོ་རྗེ༌[^371]ཞེས་པ་སྟེ་དགོངས་པ༌[^372]ཐམས་ཅད་འབྱུང་བར་བྱེད་པའི་རྡོ་རྗེ་ཐོགས་པ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 807]
དེས་ཇི་སྐད་དུ་ཐོས་པ་ཐུགས་ལ་བཞག་ནས་ཞེས་པ་ནི་ལྷག་པ་དང་ཆད་པ་ལ་སོགས་པའི་ཉེས་པ་དང་བྲལ་བར་བྱས་ནས་ཞེས་པའི་དོན་ཏོ། །

[Block 808]
དེས་ཅི་བྱེད་ཅེ་ན། གདུལ་བྱ་རྣམས་ལ་བསྟན་པའི་ཕྱིར། །ཞེས་སྨོས་ཏེ་རང་གི་གདུལ་བྱ་སྨིན་པ་དང་གྲོལ་བར་བྱེད་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 809]
འདི་སྐད་བདག་གིས་ཐོས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་སྡུད་པ་པོ་རང་གི་ཚིག་ལེགས་པར་སྟོན་པ་ཡིན་ཏེ། འདི་སྐད་ཐོས་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 810]
འདི་སྐད་ཅེས་བྱ་བ་འདི་ཡང་། ཇི་སྐད་ཅེས་བྱ་བའི་ཚིག་ཡིན་ནོ༌[^373]ཞེ་ན། དེའི་ཕྱིར་འདི་སྐད་ཅེས་བྱ་བ་ནི་རྒྱུད་ཀྱི་དོན་མ་ལུས་པར་སྟོན་པའི་ཚིག་གི་ཕྲད་དོ་ཞེས་སྨོས་ཏེ་འདིས་ནི་བཤད་པར་བྱ་བའི་ཆོས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །
--- END BLOCKS ---
