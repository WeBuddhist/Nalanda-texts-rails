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
[Block 771]
ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུ་ནི་གོམས་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 772]
བཟོད་པའི་འབྲས་བུ་ནི་འཁོར་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 773]
མངོན་པར་མཐོ་བའི་ཐབས་ཀྱང་རྣམ་པ་གསུམ་སྟེ། གང་ཕྱིར་མི་ཡི་མིག་ནི་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་པ་བསྒྲུབ༌[^430]པའི་ཕྱིར། སྦྱིན་དང་སྤྱད་པས་ནོར་རྣམས་དོན་ཡོད་བྱོས། །ཞེས་བྱ་བ་གཉིས་ཀ་བཟུང་བ་ཡིན་ནོ། །

[Block 774]
གསུམ་པ་ནི་མ་བྱིན་ཞིང་གཞག་པ༌[^431]དེ་བཟློག་པ་ཡིན་ཏེ། འཇིག་རྟེན་འདི་དང་གཞན་ལ་བདེ་བ་འབྱུང་བའི་ལམ་ཞེས་བྱ་བ་འཇིག་རྟེན་འདིར་ནི་གྲགས་པ་གཙོ་བོ་ཡིན་པས་འཇིག་རྟེན་འདིར༌[^432]བདེ་བ་འབྱུང་བའོ། །

[Block 775]
ལམ་ནི་གང་གི་ཕྱིར་ལོངས་སྤྱོད་དོ། །

[Block 776]
དེ་བས་ན་དོན་ཡོད་བྱོས་ཞེས་བྱ་བ་ཡིན་ཏེ། སྦྱིན༌[^433]དང་སྤྱད་པས་ནོར་རྣམས་དོན་ཡོད་ཞེས་བྱ་བའོ། །

[Block 777]
འདིར་དོན་གཉིས་པོ་དེ་རབ་ཏུ་བསྒྲུབ་པ་དང་སྐྱོན་བསྟན་པའི་ཕྱིར་བཤད་པ་སྟེ། མངོན་པར༌[^434]འདོད་པ་ནི་ཁྱད་པར་དུ་འཕགས་པའི་གཏེར་བསྟན་པའི་ཕྱིར་དང་། ངེས་པར་ལེགས་པའི་ལམ་ཉེ་བར་བསྟན་པའི་ཕྱིར། འཇིག་རྟེན་ཕན་ཕྱིར་ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ནོ། །

[Block 778]
སྙིང་པོ་མེད་པའི་ཞེས་བྱ་བ་ནི་སྙིང་པོ་མེད་པས་མི་གཅེས་པ་ནི་སྙིང་པོ་མེད་པའོ། །

[Block 779]
དེའི་སྙིང་པོ་ནི་གང་བྱིན་པའི་སྙིང་པོ་ཡོད་པ་སྟེ། བྱིན་པ་གང་ཡིན་པ་སྟེ་གང་བཏང་བ་དང༌[^435]སྙིང་པོའོ། །

[Block 780]
འཇིག་རྟེན་ཕན་ཕྱིར་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་ཉིད་དུ་མངོན་པར་འདོད་པ་སྟེ། འདིས་ནི་ཁྱད་པར་དུ་ངེས་པར་ལེགས་པའི་ལམ་བསྟན་ཏོ། །ཇི་ལྟར་སྦྱིན་པ་སྦྱིན་པར་བྱ་བ་ཡིན་ཞེ་ན། སྨྲས་པ། སྦྱིན་པ་བྱིན་ན་གཏེར་དང་འདྲ་བར་འགྱུར།[^436] །ཞེས་བྱ་བ་སྟེ། མངོན་པར་འདོད་པ་གང་ཡིན་པ་དེ་ཁྱད་པར་དུ་གྱུར་པའི་གཏེར་ཡིན་པས་བཏང་བ་བྱས་ན་ནི་འཁོར་བའི་སྐྱེ་བ་གཞན་དག་ཏུ་ཉེ་བར་ལོངས་སྤྱོད་པར་འགྱུར༌[^437]ཏེ། དེ་ལ་སྦྱིན་པ་བྱིན་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 781]
ཤིན་ཏུ་ཆུད་ཟོས་འགྱུར༌[^438]ཞེས་བྱ་བ་ནི་གཏེར་རྣམ་པར་ཉམས་པ་སྟེ། གཅིག་ཏུ་ཆུད་ཟོས་པ་གང་ཡིན་པ་དེ་ནི་ཤིན་ཏུ་ཆུད་ཟོས་འགྱུར་ཞེས་བྱའོ། །

[Block 782]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་ཡུལ་ཤི་བི་པའི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 783 [HEADING]]
## ཟན་དྲོན་ཆང་པ་བྱིན་པའི་སྐྱེས་པའི་རབས། ^3-0

[Block 784]
སེམས་རབ་ཏུ་དང་བ་ལས་བྱུང་བ༌[^439]ཞེས་བྱ་བ་ནི་སེམས་དམ་པ་དང་ཁྱད་པར་དུ་གྱུར་པ་ལས་བྱུང༌[^440]བའོ། །

[Block 785]
ཆུང་ཞེས་བྱ་བ་ནི་སྦྱིན་པའི་དངོས་པོ་ཆུང་ཞེས་བྱ་བ་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 786]
རབ་ཏུ་བྱེད་པ་ནི་ཇི་ལྟ་བ་བཞིན་དུ་ཡོད་པའི་རྒྱལ་པོའི་ཡོན་ཏན་ནོ། །

[Block 787]
གྱུར་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཕུན་སུམ་ཚོགས་པ་ཡིན་ཏེ། འདིས་ནི་ཡོན་ཏན་དང་ལྡན་པར་བསྟན་ཏོ། །

[Block 788]
སྐལ་བ་ཕུན་སུམ་ཚོགས་པ་ཉིད་ཡོན་ཏན་ཡིན་པས་སྐལ་བ་ཕུན་སུམ་ཚོགས་པའི་ཡོན་ཏན་ནོ། །

[Block 789]
དེ་ཉིད་བཟང་པོ་སྟེ་བལྟ་ན་སྡུག་པར་གྱུར་པས་སོ། །

[Block 790]
ཟླ་བ་ལྟ་བུ་ནི་རྒྱལ་པོ་ཡིན་ལ། འོད་ལྟ་བུ་ནི་དེའི་ཡོན་ཏན་ནོ། །

[Block 791]
སྟོན་ཀ་ལྟ་བུ་ནི་སྐལ་བ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 792]
ཁྲོས་པའི་རྗེས་སུ་འབྲངས་པའི་དཔལ་དེ་ལ་གནས་ཏེ། གང་ལས་ཤེ་ན། འདི་ལྟར་དེའི་དགྲ་དྲེགས་པ་རྣམས་ཀྱང་བཏང་ཞེས་པས་སོ། །

[Block 793]
བྱམས་པའི་རྗེས་སུ་འབྲང་བའི་དཔལ་དུ་ཡང་འགྱུར་ཏེ། གང་ལས་ཤེ་ན། དེ་ལ་བརྟེན་པ་རྣམས་ལ་ཆགས་ཞེས་བྱ་བ་ཡིན་ཏེ། སྤྲོ་བ་ཕུན་སུམ་ཚོགས་པ་དང་ལྡན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 794]
དེའི་དགྲ་དྲེགས་པ་རྣམས་ཀྱང་བཏང་བས་དཔལ་ཞེས་བཤད་པ་དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ལ་ཉེས་པ་དང༌[^441]བཅས་ཏེ་མི་མཐུན་པ་ཡིན་པས་སྙིང༌[^442]རྗེའི་ཡོན་ཏན་དང་འགལ་བར་སྣང་ངོ་ཞེ་ན། དེའི་ལན་བསྟན་པའི་ཕྱིར། དེ་ནི་ཆོས་ཀྱི་བདག་ཉིད་གྱུར་པས་ན་ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ཏེ། གཞན་གྱི་གནོད་པ་ནི་གཞན་ལ་གནོད་པའོ། །

[Block 795]
དེས་གདུག་པ་ནི༌[^443]གཞན་ལ་གནོད་པའི༌[^444]གདུག་པའི་སེམས་སུ་མ་གྱུར་པའོ། །

[Block 796]
གལ་ཏེ་གཞན་ལ་གནོད་ཅིང་གདུག་པའི་སེམས་སུ་གྱུར་ན་ནི་སྙིང་རྗེའི་ཡོན་ཏན་དང་འགལ་བའི་སྐྱོན་དུ་འགྱུར་གྱི་དེ་མེད་པས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་སྨྲས་པ། ཆོས་ཀྱི་བདག་ཉིད་དུ་གྱུར་པ་ཞེས་པས་སོ། །

[Block 797]
དེ་ལྟ་ན༌[^445]ནི་ཇི་ལྟར༌[^446]དེའི་དགྲ་མཚོན་ཆ་བཏང་ཞེ་ན་དེ་བསྒྲུབ་པའི༌[^447]ཕྱིར། འབངས་ཀྱང་དེ་ལ་གློ་བ་ཉེ་བར་གྱུར། །ཞེས་བྱ་བ་ཡིན་ཏེ། གློ་བ་ཉེ་བ་ནི་དེའི་འབངས་རྗེ་ལ་སྙིང་ཉེ་བ་དེས་དཔལ་མངོན་པར་སྦྱོར་བར་བྱེད་དེ། བྱང་ཆུབ་སེམས་དཔའ་མ་ཡིན་པའོ། །

[Block 798]
དེ་བདག་གི་ཚེ་སྔ་མ་འདས་པ་ཞེས་བྱ་བ་ལ། འདས་པ་ཞེས་སྨོས་པས་ནི། སྔ་མའི་ཁྱད་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 799]
བདག་གི་ཞེས་སྨོས་པས་ནི། ཚེ་རྗེས་སུ་དྲན་པའི་ཁྱད་པར་བསྟན་པའི་ཕྱིར་ཏེ། གཞན་གྱི་སྐྱེ་བ་དྲན་པ་དགག་པའོ། །

[Block 800]
རབ་ཏུ་སྐྱོ་བར༌[^448]གྱུར་ནས། ཞེས་བྱ་བ་ནི། འཁོར་བའི་གནས་སྐབས་རྟོགས་ཤིང་ཚེ་སྔ་མ་ལ་དབུལ་བ་དེ་རྗེས་སུ༌[^449]དྲན་པའི་རྒྱུས་ས། །སྦྱིན་པ་ཁྱད་པར་ཅན་ཞེས་བྱ་བ་ལ་ཅིའི་ཕྱིར་ཁྱད་པར་ཅན་ཡིན་ཞེ་ན། ཚེ་རབས་སྔ་མ་ལ་སྦྱིན་པ་དང་། ཚུལ་ཁྲིམས་ལ་སོགས་པ་ཡང་དག་པར་བླང་བ༌[^450]དང་། བདག་གི་སྐྱེ་བ་རྗེས་སུ་དྲན་པའི་རྒྱུས་སྦྱིན་པ་ལ་སོགས་པའི་ཡོན་ཏན་དང་ལྡན་པ་སྟེ། ཅིའི་ཕྱིར་འབྲས་བུ་དང་འབྲེལ་ཅེ་ན་མངོན་སུམ༌[^451]དུ་གྱུར་པས་སོ། །

[Block 801]
དེ་ལ་དགེ་སྦྱོང་དང་། བྲམ་ཟེ་དང་། ཕོངས་པ་དང་། སློང་བ་ཉིད་སྨོས་པ་ནི་ཡོན་ཏན་འབྱུང་བའི་ཞིང་གི་དབྱེ་བ་བསྟན་པའི་ཕྱིར་ཏེ། དགེ་སྦྱོང༌[^452]དང་བྲམ་ཟེ་ནི་འཇིག་རྟེན་པ་རྣམས་ཀྱི༌[^453]ཡོན་ཏན་གྱི་ཞིང་དུ་ཡང་དག་པར༌[^454]འདོད་པའི་ཕྱིར་རོ། །

[Block 802]
དོན་དམ་པ་དང་ཀུན་རྫོབ་གཉིས་སོ། །

[Block 803]
ཕོངས་པ་དང་སློང་བ་སྨོས་པས་ནི་རང་གི་འཚོ་བས་འཇིགས་པ་དང་། སློང་བ་དེ་ཉིད་ཀྱི་འཚོ་བའི་དབྱེ་བས་སྙིང་རྗེའི་ཞིང་གི་དབྱེ་བ་བསྟན་པའོ། །

[Block 804]
བདེ་བའི་རྒྱུ་དང་གཞིར་གྱུར་པ་ཞེས་བྱ་བ་ནི་སྦྱིན་པ་པོ་དང་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 805]
བདེ་བའི་རྒྱུ་ཞེས་བྱ་བ་ལ་བདེ་བ་ནི་ལུས་དང་སེམས་ཀྱིས༌[^455]མྱོང་བ་གང་ཡིན་པའོ། །

[Block 806]
དེའི་རྒྱུ་ནི་ལོངས་སྤྱོད་དོ། །

[Block 807]
དེའི་གཞིར་གྱུར་པ་ནི་སྦྱིན་པར་བྱ་བ་ཡིན་ཏེ། སྦྱིན་པའི་དངོས་པོ་དམ་པའོ། །

[Block 808]
འདིས་ནི་སྦྱིན་པའི་དངོས་པོ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། སྦྱིན་པ་ཐམས་ཅད་བྱིན་པར་སྟོན་ཏོ། །

[Block 809]
དེ་དག་གིས་ནི་གང་དག་ལ་སྦྱིན་པ་དང་གང་གི་ཕྱིར་སྦྱིན་པ་དེ་བསྟན་པ་ཡིན་ནོ། །

[Block 810]
བདེ་བའི་རྒྱུ་དང་གཞིར་གྱུར་པ་ཞེས་བྱ་བ་ལ། ཚུལ་ཁྲིམས་དང་གསོ་སྦྱོང་ནི་བདེ་བའི་རྒྱུ་སྟེ། ཚུལ་ཁྲིམས་ཀྱི་འབྲས་བུ་མངོན་པར་མཐོ་བ་ཕུན་སུམ་ཚོགས་པའོ། །
--- END BLOCKS ---
