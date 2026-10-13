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
[Block 736]
མ་རིག་ཀུན་དུ་གནས་པ་ནི། །ཇི་ལྟར་ལུས་ལ་ལུས་དབང་གིས། །

[Block 737]
དེ་ཕྱིར་ཀུན་ཀྱང་རྨོངས་པ་ཡིས།[^553] །ཉོན་མོངས་པས་དེ་འདིར་བསྣུན་ནོ། །ཞེས་བཤད་དོ། །

[Block 738]
གང་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས་འདི་སྐད་དུ་གསུངས་པ། ཉེ་བར་ལེན་པའི་ཕུང་པོ་ལྔ་པོ་འདི་ཉིད་ལ་བདག་ཅེས་ཡང་དག་པར་རྗེས་སུ་མཐོང་ངོ་ཞེས་བྱ་བའི་མདོ་དེ་ཡང་མཐར་འཛིན་པར་ལྟ་བ་དང་། འཇིག་ཚོགས་སུ་ལྟ་བ་དང༌[^554]ལྷན་ཅིག་ཏུ་གཞི་གཅིག་ལ་དམིགས་པར་འཐད་དོ་ཞེས་ཤིན་ཏུ་ངེས་པར༌[^555]སྒྲུབ་པའོ། །

[Block 739]
དེ་ལས་ཀྱང་འདི་ཤིན་ཏུ་འཐད་པས་དངོས་པོར་ཡོད་ན་ཡང་དེས་ན་གཉིས༌[^556]ཀ་ཁས་བླང་ངོ་ཞེས་བྱ་བར་འགྱུར་རོ་ཞེས་སོ། །

[Block 740]
འདིར་སྨྲས་པ། གལ་ཏེ་དངོས་པོ་ཡོད་ཀྱང་དེ་ལྟ་ན་ཡང་དེའི་རྟག་པ་དང་མི་རྟག་པ་དག་མེད་པས་ཐེར་ཟུག་པ་དང་རྒྱུན་ཆད་པར་ལྟ་བར་ཐལ་བ་མ་ཡིན་པ་ཇི་ལྟར་ཞེ་ན། གསུངས་པ།

[Block 741 [HEADING]]
### ཚིགས་བཅད་ཉེར་གཉིས་པ། ^1-22-0

[Block 742 [VERSE]]
རྒྱུན་གྱི་ཕྱིར་ན་འདི་ཡོད་དེ། །
རྒྱུ་བྱིན་ནས་ནི་དངོས་པོ་འགག །

[Block 743]
སྔར་བཞིན་འདི་ཡང་མ་གྲུབ་ཅིང་རྒྱུན་ཆད༌[^557]པར༌[^558]ཐལ་བར་འགྱུར། དེ་ལ་རྒྱུ་དང་འབྲས་བུའི་འབྲེལ་པ་འཇུག་པ་ལས་དུས་གསུམ་དུ་འདུས་བྱས་རྣམས་ཀྱི་སྐད་ཅིག་མའི་ཉེ་བར་ལེན་པ༌[^559]རབ་ཏུ་འབྱུང་བ་ལས་རྒྱུན་ཞེས་བརྗོད་དོ། །

[Block 744]
འདི་ལྟར་སཱ་ལུའི་ས་བོན་གྱི་མྱུ་གུ་དང་སྡོང་བུ་དང་ལྡུམ་བུ་རྣམས་བརྒྱུད་མར་རབ་ཏུ་འབྱུང་བ་ནི་ས་བོན་གྱི་རྒྱུན་ནོ། །

[Block 745]
དེ་བཞིན་དུ་གཞན་ལ་ཡང་ཤེས་པར་བྱའོ། །

[Block 746]
མྱུ་གུ་ལ་སོགས་པའི་རྒྱུན་དེ་ཡང་ས་བོན་གྱི་རྒྱུས་འཇུག་ལ། ས་བོན་གྱི་རྒྱུ་ཅན་གྱི་མྱུ་གུ་ལ་སོགས་པའི་རྒྱུན་དེ་ལས་ཀྱང་ས་བོན་དང་འདྲ་བའི་འབྲས་བུ་མཐར་འཇུག་གོ། །

[Block 747]
འབྲས་བུ་དེ་ཡང་ས་བོན་གྱི་རྒྱུ་ཅན་དུ་རྣམ་པར་གཞག་སྟེ། ཇི་ལྟར་བྱས་ན་འདིར་ས་བོན་འགགས་ལ། འདིའི་བདག་ཉིད་ཀྱི་རྒྱུན་ལས་འདྲ་བའི་འབྲས་བུ་སྐྱེད་པའི་ཕྱིར་དངོས་ཀྱི་འབྲས་བུའི་རྒྱུ་མྱུ་གུ་བྱིན་ནས་འགག་པར་འགྱུར་རོ། །

[Block 748]
འབྲས་བུ་སྐྱེད་པའི་ནུས་པས་ཁྱད་པར་དུ་བྱས་པའི་མྱུ་གུ་སྐྱེད་པའི་རྒྱུའི་དངོས་པོར་ཡོངས་སུ་བསྒྲུབ་པས། རྒྱུ་བྱིན་ནས་འགགས་ཞེས་བརྗོད་དོ། །

[Block 749]
དེ་བཞིན་དུ་མྱུ་གུ་ལ་སོགས་པ་ནས་མེ་ཏོག་གི་མཐར་ཐུག་པ་རྣམས་རང་གི་རྒྱུ་ལས་ཐོབ་པའི་རྒྱུས་ས་བོན་དང་མཐུན་པའི་འབྲས་བུ་རིམ་གྱིས་རྫོགས་པར་བྱེད་དོ། །

[Block 750]
འབྲས་བུ་དེ་ཡང་ས་བོན་རྒྱུར་བྱས་པ་ཉིད་ལས་ཉེ་བར་སྐྱེའོ། །

[Block 751]
གལ་ཏེ་ས་བོན་དང་མྱུ་གུ་ལ་སོགས་པའི་རྒྱུན་འབྲས་བུ་སྐྱེད་པའི་ནུས་པས་མི་འཇུག་ན་མཐར༌[^560]ཡང་དེའི་རིགས་ཅན་གྱི་འབྲས་བུ་མི་འབྱུང་ངོ་ཞེས་བྱ་ལ། དེས་ན་མཐར་ཡང་འབྱུང་བཞིན་པའི་འབྲས་བུ་ས་བོན་གྱི་རྒྱུ་ཅན་ཉིད་དོ་ཞེས་རྣམ་པར་འཇོག་ལ། ཇི་སྐད༌[^561]དུ།

[Block 752 [VERSE]]
[^562]གང་ཕྱིར་ས་བོན་ལས་རྒྱུན་དང་། །
རྒྱུན་ལས་ཀྱང་ནི་འབྲས་བུ་འབྱུང་། །
དེའི་ཕྱིར༌[^563]ས་བོན་སྔོན་འགྲོའི་འབྲས། །
རྟག་མིན་ཆད་པ་ཡང་མ་ཡིན། །

[Block 753]
ཞེས་བསྟན་ཏོ། །

[Block 754]
དེ་ལ་ས་བོན་ནི་འབྲས་བུ་སྐྱེད་པར་ནུས་པའི་མྱུ་གུ་ལ་སོགས་པའི་རྒྱུན་གྱི་རྒྱུར་ཁོང་དུ༌[^564]ཆུད་པར་འགག་པར་འགྱུར་གྲང་ལ། མྱུ་གུ་ལ་སོགས་པའི་རྒྱུན་ཀྱང་མི་འཇུག་པར་འགྱུར་ན། དེའི་ཚེ་ཆད་པར་ལྟ་བར་འགྱུར་རོ། །

[Block 755]
ཡང་ན་མྱུ་གུ་ལ་སོགས་པ་འཇུག་ཀྱང་ས་བོན་རང་གི་ངོ་བོས་གནས་ན་དེ་ནི་རྟག་པར་ལྟ་བ་སྟེ། དེ་ལྟར་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བས་དེས་ན་རྒྱུན་ཡོད་ལ་རྒྱུན་ཅན་གྱི་རྒྱུའི་སྐད་ཅིག་མ་རྣམས་ཀྱང་འབྲས་བུའི་དོན་དུ་རྒྱུ་བྱིན་པའི་ཕྱིར་དང་། རང་གི་ངོ་བོས་མི་གནས་པའི་ཕྱིར་ཡང་རྟག་པ་དང་ཆད་པར་ལྟ་བར་ཐལ་བ་མེད་དོ་ཞེས་བྱའོ། །

[Block 756]
འདིར་ཡང་སློབ་དཔོན་གྱིས་སྐྱོན་བརྗོད།

[Block 757 [VERSE]]
[^565]སྔར་བཞིན་འདི་ཡང་མི་འགྲུབ་ཅིང་། །
རྒྱུན་ཆད་པར་ཡང་ཐལ་བར་འགྱུར། །

[Block 758]
ཞེས་བྱ་བ་ལ། འདིར་འདི་སྐད་དུ་རྟག་པ་དང་ཆད་པའི་སྐྱོན་སྤང་བའི་ཕྱིར། དེ་ནི་སྔར་བཞིན་དུ་མ་གྲུབ་སྟེ། ཇི་ལྟར་བྱས་ན་ཡོད་པ་ཉིད་ལ་རྒྱུ་དང་འབྲས་བུའི་འཇུག་པ་འབྱུང་བར་འགྱུར་རོ་ཞེས་འདིར་རྟོགས་ན། རྒྱུ་དང་འབྲས་བུ་འཇུག་པ་མི་སྲིད་པ་ཡང་སྔར་བསྟན་ཏེ།

[Block 759 [VERSE]]
འབྲས་བུ་ཡིན་ན་འབྲས་ལྡན་ལ། །
དེར་མེད་གྱུར་ན་རྒྱུ་མེད་མཚུངས། །
ཡོད་དང་མེད་པ་ན་ཡང་འགལ། །
དུས་གསུམ་དུ་ཡང་འཐད་མ་ཡིན། །

[Block 760 [VERSE]]
མ་རིག་འདུ་བྱེད་མེད་མི་འབྱུང་། །
དེ་མེད་འདུ་བྱེད་མི་འབྱུང་ཞིང་། །
དེ་དག་ཕན་ཚུན་རྒྱུ་ཅན་དེ། །
རང་བཞིན་གྱིས་ཀྱང་མ་གྲུབ་པོ། །

[Block 761]
གང་ཡང་།

[Block 762 [VERSE]]
གང་ཞིག་རང་ཉིད་རང་བཞིན་གྱིས། །
མ་གྲུབ་དེས་གཞན་ཇི་ལྟར་སྐྱེད། །
དེ་ཕྱིར་གཞན་ལས་གྲུབ་པ་ཡིས།

[Block 763]
[^566] །རྐྱེན་གཞན་དག་ནི་སྐྱེད་བྱེད་མིན། །དེས་ན་རྒྱུ་དང་འབྲས་བུ་དག་མ་གྲུབ་ན། རྒྱུན་ག་ལ་ཞིག༌[^567]རྒྱུ་བྱིན་པ་ག་ལ་ཞིག་ཅེས་པ་དང་། རྒྱུ་འགགས་ནས་སླར་མི་སྐྱེ་བས། རྒྱུ་རྒྱུན་ཆད་པར་ཐལ་བར་བརྟག་པ༌[^568]ཡང་མི༌[^569]རིགས་ཏེ། དེ་ལྟར་ཡང་དངོས་པོར༌[^570]ཁས་བླངས་ན་རྟག་པ་དང་ཆད་པའི་ལྟ་བར་ཐལ་ལོ་ཞེས་གནས་སོ། །

[Block 764]
འདིར་སྨྲས་པ། གལ་ཏེ་རྟག་པ་དང་ཆད་པར་ལྟ་བར་ཐལ་བས་རྟག་པ་དང་ཆད་པར་ཁས་མི་ལེན་ན། འདི་ལྟར་དངོས་པོ་ལས་སྐྱེ་བ་དང་འགག་པ༌[^571]ཡང་མེད་པར་ཐལ་ལ། དེ་མེད་ན་ཡང་དག་འདི་དག་སྐྱེ་བ་དང་འཇིག་པར་བསྟན་པས་བཅོམ་ལྡན་འདས་ཀྱིས་མྱ་ངན་ལས་འདས་པའི་ལམ་བསྟན་པ་གསུངས་པ།

[Block 765 [VERSE]]
མི་རྟག་དང་ལྡན་འདུས་བྱས་རྣམས། །
སྐྱེ་དང་འཇིག་པའི་ཆོས་ཅན་ཏེ། །
སྐྱེ་ཞིང་གང་ལ་འཇིག་འགྱུར་བ། །
དེ་དག་ཉེར་ཞི་བདེ་བའོ། །

[Block 766]
ཞེས་པས། དེ་འགག་པ་དང་། སྐྱེ་བ་དང་། འཇིག་པ་དག་མེད་པའི་སྟོང་པ་དག་ཉེ་བར་བསྟན་པ་མྱ་ངན་ལས་འདས་པའི་ལམ་དུ་མི་འཐད་དོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 767 [HEADING]]
### ཚིགས་བཅད་ཉེར་གསུམ་པ། ^1-23-0

[Block 768 [VERSE]]
སྐྱེ་འཇིག་བསྟན་ཕྱིར་མྱང་འདས་ཀྱི། །
ལམ་བསྟན་མ་ཡིན་སྟོང་ཉིད་ཕྱིར། །

[Block 769]
ཞེས༌[^572]པའོ། །

[Block 770]
ཡང་ན་འདིའི་དོན་ནི་གཞན་ཏེ། གལ་ཏེ་འདི་སྙམ་དུ་སེམས་ན། དངོས་པོ་ཡོད་བཞིན་པ་མ་ཡིན་པའི་ཕྱིར་སྐྱེ་འཇིག་མེད་པར་འགྱུར་ན་མྱ་ངན་ལས་འདས་པའི་ལམ་བསྟན་པ་མེད་པར་ཐལ་ལོ་ཞེས་པའི་སྐྱོན་འདི་མེད་དེ། སྐྱེ་བ་དང་འཇིག་པ་ཡོད་བཞིན་པ་མ་ཡིན་པ་ལ་བསྟན་པ་འཐད་ཅིང་། གང་ལས་སྐྱེ་འཇིག་བསྟན་པ་ལས་མྱ་ངན་ལས་འདས་པ་ཐོབ་པར་བྱའོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ་མྱ་ངན་ལས་འདས་པའི་ལམ་བསྟན་པ་རྣམ་པར་གཞག་པ་མ་ཡིན་ནོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ།

[Block 771]
སྐྱེ་འཇིག་བསྟན་ཕྱིར་མྱང༌[^573]འདས་ཀྱི། །ལམ་བསྟན་མ་ཡིན་ཞེས་སོ། །

[Block 772]
སླར་ཡང་ཅིའི་ཕྱིར་ན་སྐྱེ་འཇིག་བསྟན་པ་ལས་ཐར་པ་མེད་ཅེས་ཉེ་བར་བསྟན་པར༌[^574]མྱ་ངན་ལས་འདས་པའི་ལམ་བསྟན་པར་ཡང་མི་འཐད་དོ་ཞེས་བསྟན་པའི་ཕྱིར་གསུངས་པ། སྟོང་ཉིད་ཕྱིར་ཞེས་པའོ། །

[Block 773]
སྐྱེ་བ་དང་འཇིག་པ་དག་སྟོང་ན་ཇི་ལྟར༌[^575]དག་བསྟན་པ༌[^576]མྱ་ངན་ལས་འདས་པའི་ལམ་བསྟན་པར་འགྱུར། སླར་ཡང་ཉེ་བར་དམིགས་བཞིན་པ་སྐྱེ་བོ་ཐམས་ཅད་ལ་གྲགས་པའི་སྐྱེ་བ་དང་འཇིག་པ་དག་ཇི་ལྟར་སྟོང་པ་ཉིད། ཇི་ལྟར་ཉེ་བར་མ་དམིགས་པ་དེ་དག་ཀྱང་སྟོང་པ་ཉིད་ལ་དེ་ལྟར་བསྟན་པའི་ཕྱིར་གསུངས་པ། འདི་དག་ཕན་ཚུན་བཟློག་པ་རུ།[^577] །མཐོང་བ་ཕྱིན་ཅི་ལོག་ལས་ཡིན། བདེན་ཏེ། སྐྱེ་བ་དང་འཇིག་པ་དག་སྟོང་པ་ཉིད་ཀྱི་ཕྱིར། དེ་དག་སྟོང་པ་ཉིད་ཡིན་ཀྱང་གང་འཇིག་རྟེན་པས་མཐོང་བ་ཕྱིན་ཅི་ལོག་པས་འཇུག་པའོ། །

[Block 774]
དེ་དག་འདི་ལྟར་ཇི་ལྟར་རྟོགས་ཤེ་ན། ཕན་ཚུན་བཟློག་པ་ལས་ཏེ། ཕྱིན་ཅི་ལོག༌[^578]པས་ན་ཕན་ཚུན་བཟློག་པ་སྟེ། གཞན་དུ་འགྱུར་བ་ཐོབ༌[^579]པའོ། །

[Block 775]
གལ་ཏེ་སྐྱེ་བ་དང་འཇིག་པ་དག་རང་གི་ངོ་བོས་ཡོད་ན་འདི་དག་ཕན་ཚུན་བྱས་པས་གཞན་དུ་འགྱུར་བར་མི་འགྱུར་ཏེ། སྐྱེ་བ་ལས་གཞན་པ་མ་སྐྱེས་པ་ལ་འཇིག་པ་མེད་ལ། སྐྱེ་བའི་དུས་ན་ཡང་སྐྱེ་བའི་དུས་དང་འགལ་བའི་འཇིག་པ་མི་རིགས་པའི་ཕྱིར་དང་། འཇིག་པ་དང་བྲལ་བ་ཡང་སྐྱེ་བ་མེད་པའི་ཕྱིར་དང་། འཇིག་པའི་དུས་སུ་ཡང་དེ་དང་འགལ་བའི་སྐྱེ་བ་མི་རུང་བའི་ཕྱིར་དང་། ཕན་ཚུན་ལས་དུས་གཅིག་ཏུ་སྐྱེ་བ་ཐོབ་པ༌[^580]འགལ་བ་དང་། ཕན་ཚུན་མེད་པས་འདི་དག་གསལ་བའི༌[^581]ཕྱིར་ཕན་ཚུན་བཟློག་པར་འགྱུར་རོ། །
--- END BLOCKS ---
