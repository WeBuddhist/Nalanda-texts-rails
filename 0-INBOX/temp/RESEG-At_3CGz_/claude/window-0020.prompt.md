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
[Block 701]
སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པ་དང་བདེ་བ་མངོན་པར་བསྒྲུབ་པའི༌[^398]ཕྱིར་ཕན་འདོགས་པའོ། །

[Block 702]
བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཀྱི་འབྲས་བུ་ལེན་པར་བྱེད་པའི་ཕྱིར་འབྲས་བུ་ཆེ་བར་རིག་པར་བྱའོ་ཞེས་སྡོམ་པ་ཉི་ཤུ་པའི་འགྲེལ་པ་ལས་གསུངས་སོ། །

[Block 703]
དེ་ལྟར་བླ་མ་དམ་པ་ལས་བསླབ་པ་དེ་ལྟ་བུ་ལེགས་པར་བསླངས༌[^399]ཤིང་། ཆོས་དང་མཐུན་པར་བསྲུང་བའི་བྱང་ཆུབ་སེམས་དཔའི་ཚོགས་ཀྱི་ལམ་ཐར་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བ་བསྐྱེད་པར་འདོད་པ་དེ་ནི། ཚེ་རབས་སྔ་མའི་བག་ཆགས་བཟང་པོ་ཡོད་པ་ཡིན་ཏེ།

[Block 704]
མགོན་པོ་བྱམས་པས་དབུས་དང་མཐའ་རྣམ་པར༌[^400]འབྱེད་པ་ལས།

[Block 705 [VERSE]]
སྣོད་གྱུར་རྣམ་པར་སྨིན་བརྗོད་དང་། །
དེ་ཡི་དབང་གིས༌[^401]སྟོབས་དང་ནི། །
འདོད་དང་འཕེལ་དང་རྣམ་དག་སྟེ། །
འབྲས་བུ་རྣམས་ནི་གོ་རིམས་བཞིན། །

[Block 706]
ཞེས་གསུངས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ༌[^402]རྣམས་སྔོན་གྱི་སྐྱེ་བ་དག་ཏུ་དགེ་བ་ལ་གོམས་པར་བསླབས་པས༌[^403]ཚེ་འདིར་དེའི་སྣོད་དུ་གྱུར་པ་ནི་རྣམ་པར་སྨིན་པའི་འབྲས་བུའོ། །

[Block 707]
དེ་རྣམས་འདིར་བྱས་པའི་སྟོབས་ཅན་དུ་གྱུར་པ་ནི་བདག་པོའི་འབྲས་བུའོ། །

[Block 708]
དེ་ཉིད་ལ་ཕྱིར་ཞིང་འདུན་པ་ནི་རྒྱུ་མཐུན༌[^404]པའི་འབྲས་བུའོ། །

[Block 709]
འདིར་བསླབ་པ་དག་མངོན་པར་འཕེལ་བ་ནི་སྐྱེས་བུ་བྱེད་པའི་འབྲས་བུའོ། །

[Block 710]
དེའི་སྒྲིབ་པའི་དྲི་མ་རྣམས་དང་བྲལ་བ་ནི་བྲལ་བའི་འབྲས་བུའོ། །

[Block 711]
འདིར་བདག་པོའི་འབྲས་བུ་མ་གཏོགས་པ་བཞི་ནི་རིས་མཐུན་པའི་འབྲས་བུར་བགྲང་གི་འདི་ཉིད་ལ་རྫོགས་པ་ནི་མ་ཡིན་ནོ་ཞེས་བླ་མ་མཁས་པ་ཆེན་པོ་ཤཱན་ཏི་པས་གསུངས་སོ། །

[Block 712]
སློབ་དཔོན་མཁས་པ་ཆེན་པོ་ནོར་གྱི་རྩ་ལག་གི་ཞལ་ནས་ཀྱང་བྱང་ཆུབ་སེམས་དཔས༌[^405]བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་ཕན་ཆད་ཚེ་རབས་ཚེ་རབས་སུ།

[Block 713]
བདེ་འགྲོ་རིགས་མཐོ་སྐྱེ་དབང་ཚང་། །ཕོར་གྱུར་ཚེ་རབས་དྲན་མི་ལྡོག །

[Block 714]
བྱང་ཆུབ་སེམས་དཔའ་སེམས་ཅན་ལ་ཕན་པའི་དོན་དུ་སྡུག་བསྔལ་ལ་མི་སྐྱོ་བའོ། །

[Block 715]
འཇིག་རྟེན་ན་ཟོང་གིས་མ་ཉོས་པའི་བྲན་ནི་བྱང་ཆུབ་སེམས་དཔའ་དེ་ཡིན་པས། བདག་ཉིད་ཆེན་པོ་དེ་ལ་འབྱོར་པའི་མཆོག་ཁྱད་པར་ཅན་ཡོད་ཀྱང་དེས་ང་རྒྱལ་དང་ཁེངས་པར་མི་འགྱུར་བར་སྙིང་རྗེས་གཞན་གྱི་དབང་དུ་གྱུར་པས་བདག་ཉིད་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དྲུང་ན་ཁྱི་ལྟ་བུ་དང་། བྲན་ལྟ་བུ་དང་། གདོལ་པ་ལྟ་བུར་ང་རྒྱལ་བཅག་ནས་གནས་པ་སྟེ། གཞན་གྱིས་བརྙས་པ་དང་གནོད་པར་བྱས་ཀྱང་བཟོད་ཅིང་། ངལ་བ་དང་བརྣགས་པ༌[^406]ཐམས་ཅད་ཉམས་སུ་ལེན་པ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 716]
དེ་ལྟ་བུའི་གང་ཟག་ནི་ཐེག་པ་ཆེན་པོ་པ་ཡིན་པར་ཤེས་སོ། །

[Block 717]
གཞན་ཡང་ཚེ་རབས་ཚེ་རབས་སུ་བྱང་ཆུབ་ཀྱི་སེམས་མ་ཉམས་པའི་རྟགས་ནི་མདོ་ལས་ཇི་སྐད་དུ་དེ་ངན་སོང་གསུམ་སྤངས་པ་ཡིན། ཡུལ་མཐའ་འཁོབ་སྤངས་པ་ཡིན། སྐྱེས་བུ་དམ་པ་ཡོད་པའི་ས་ཕྱོགས་སུ་སྐྱེ་བ་དང་། རིགས་མཐོན་པོར་སྐྱེ་བ་ཡིན། གཟུགས་བཟང་བ་ཡིན། ཤེས་རབ་ཆེ་བ་ཡིན། ནད་མེད་པ་ཡིན།

[Block 718 [VERSE]]
སྙིང་རྗེ་དང་ལྡན་པ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །
གཞན་ཡང་དེ་མི་ཁོམ་པ་བརྒྱད་སྤངས་ཤིང་།
ཁོམ་པའི་ཡོན་ཏན་བཅུ་དང་ལྡན་པ་ཡིན་ནོ། །

[Block 719]
གཞན་ཡང་རྟགས་ནི་དེ་རང་བཞིན་གྱིས་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་དང་ལྡན་པ་ཡིན་ཏེ། མདོ་ལས་དེ་མ་བསྟན་པའི་སྦྱིན་པ་ཅན་ཡིན་ཞེས་པ་ནས། དེ་མ་བསྟན་པའི་ཤེས་རབ་ཅན་ཡིན་ཞེས་པའི་བར་དང་ལྡན་པ་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 720]
གཞན་ཡང་སློབ་དཔོན་ཟླ་གྲགས་ཀྱི་ཞལ་ནས།

[Block 721 [VERSE]]
སོ་སོ་སྐྱེ་བོའི་དུས་ན་སྟོང་ཉིད་ཐོས། །
ནང་གི་དགའ་བ་ཡང་དང་ཡང་དུ་འབྱུང་། །
དགའ་བ་ལས་བྱུང་མིག་ནི་མཆི་མས་གང་། །
ལུས་ཀྱི་སྤུ་ལྡང་བ་ཡང་སྐྱེ་བར་འགྱུར། །

[Block 722 [VERSE]]
གང་ཡིན་དེ་ལ་བྱང་ཆུབ་ས་བོན་ཡོད། །
དོན་དམ་བདེན་པ་དེ་ལ་བསྟན་པར་བྱ། །
དེར་རྟོགས་པ་ཡི་ཡོན་ཏན་དེ་ལས་འབྱུང་། །

[Block 723]
ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 724]
སློབ་དཔོན་ནོར་གྱི་རྩ་ལག་གི་ཞལ་ནས་ཀྱང་བཤད་དེ། ཐར་པའི་ཆ་དང་མཐུན་པ་ནི། གང་ལ་བདག་མེད་པའི་གཏམ་དང་འཁོར་བའི་ཉེས་དམིགས་དང་། མྱ་ངན་ལས་འདས་པའི་ཡོན་ཏན་གྱི་གཏམ་བརྗོད་པ་ཐོས་ན་མཆི་མ་འཁྲུག་པ་དང་། སྤུ་ཟིང་བྱེད་པ་དེ་ལ༌[^407]ཐར་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བ་ཡོད་པར་ཤེས་པར་བྱ་སྟེ། དབྱར་མྱུ་གུ་སྐྱེ་བ་ལས་ན་ས་གཞིའི་གསེབ་ན་དེའི་ས་བོན་ཡོད་པར་ཤེས་པ་བཞིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 725]
དེ་ལྟར༌[^408]ན་འཕགས་པ་ལང་ཀར་གཤེགས་པ་ལས།

[Block 726 [VERSE]]
དུ་བ་ལས་ནི་མེར་ཤེས་ཤིང་། །
ཆུ་སྐྱར་ལས་ནི་ཆུ་བཞིན་དུ། །
བློ་ལྡན་བྱང་ཆུབ་སེམས་དཔའ་ཡི། །
རིགས་ནི་མཚན་མ་རྣམས་ལས་ཤེས། །

[Block 727]
ཞེས་གསུངས་སོ། །

[Block 728]
དེ་ལྟར་སྡོམ་པ་སྲུང་བའི་བྱང་ཆུབ་སེམས་དཔའ་ལས་དང་པོ་པ༌[^409]དེས་དུས་ཐམས་ཅད་དུ་ལུས་དང་གནས་དང་ལོངས་སྤྱོད་ཐམས་ཅད་དང་འཁོར་བ་དང་མྱ་ངན་ལས་འདས་པའི་ཆོས་ཐམས་ཅད་རྨི་ལམ་ལྟ་བུར་ཤེས་པར་བྱ་སྟེ། རྨི་ལམ་ལྟ་བུའི་དཀོན་མཆོག་གསུམ་ལ་རྨི་ལམ་ལྟ་བུའི་སྲི་ཞུ་བྱ་བ་དང་། རྨི་ལམ་ལྟ་བུའི་འཁོར་བ་ལ་སྐྱོ་བར་བྱ་བ་དང་། རྨི་ལམ་ལྟ་བུའི་སེམས་ཅན་ལ་རྨི་ལམ་ལྟ་བུའི་སེམས་ཀྱིས༌[^410]སྙིང་རྗེ་བྱ་བ་དང་། རྨི་ལམ་ལྟ་བུའི་སེམས་ཅན་མགུ་བར་བྱ་བའོ། །

[Block 729]
སེམས་ཅན་ཐམས་ཅད་ཇོ་བོར་ཡིད་ལ་བྱ་བ་དང་། སྐྱེ་བ་མེད་པ་ཡིད་ལ་བྱ་བ་དང་། བྱང་ཆུབ་ཀྱི་སེམས་ཡིད་ལ་བྱ་བ་དང་། འཆི་བ་ཡིད་ལ་བྱ་བ་དང་། ཚུལ་ཁྲིམས་ཡིད་ལ་བྱ་བ་དང་། དངོས་པོ་ཐམས་ཅད་ལ་མ་ཆགས་པའི་ཡིད་ལ་བྱ་བ་དང་། དྲན་པ་དང་། ཤེས་བཞིན་དང་། བག་ཡོད་པ་དང་། ཚུལ་བཞིན་དུ་སེམས་པ་ཡིད་ལ་བྱའོ། །

[Block 730]
གཞན་ཡང་ལས་དང་པོ་པ་དེས་དུས་ཐམས་ཅད་དུ་ཐབས་ལ་མཁས་པར་བྱའོ། །

[Block 731]
འདི་ལྟར་བདག་གི་སྡིག་པ་གཞན་གྱི་སྡིག་པར་བྱས་ཏེ་འཆགས་པ་དང་། གཞན་གྱི་སྡིག་པ་བདག་གི་སྡིག་པར་བྱས་ཏེ་འཆགས་པ་དང་། བདག་གི་དགེ་བའི་རྩ་བ་གཞན་གྱི་དགེ་བའི་རྩ་བར་བྱེད་པ་དང་གཞན་གྱི་དགེ་བའི་རྩ་བ་བདག་གིར་བྱེད་པ་དང་། བདག་གི༌[^411]བདེ་བ་གཞན་གྱི་བདེ་བར་བྱེད་པ་དང་། གཞན་གྱི་སྡུག་བསྔལ་བདག་གིར་བྱེད་པ་དང་། བདག་གི་སྡུག་བསྔལ་གྱིས་གཞན་གྱི༌[^412]སྡུག་བསྔལ་བསལ་བ་དང་། གཞན་དག་བདེ་བ་མཐོང་བ་དང་ཐོས་པ་ན་དེ་ལ་ཡིད་དགའ་བ་དང་། གཞན་དག་སྡུག་བསྔལ་ལ༌[^413]ཐོས་སམ་མཐོང་ན། མ་ལ་བདག་གིས༌[^414]ནམ་ཞིག་ན་འདི་དག་སྡུག་བསྔལ་ལས་ཐར་བར་བྱ་སྙམ་དུ་ཡིད་གདུང་བ་དང་། འཇིག་རྟེན་གྱི་ཆོས་ལ་སེམས་བཏང་བ་དང་། གཞན་གྱི་རྙེད་པ་དང་བཀུར་སྟི་དང་། གྲགས་པ་སྙན་པ་ལ་ཕྲག་དོག་མི་བྱ་བ་དང་། བདག་ནི་འདི་ལྟར་རིགས་དང་། གཟུགས་དང་། འཁོར་དང་ཡོ་བྱད་དང་། རིག་པའི༌[^415]གནས་ལྔ་དང་། རྙེད་པ་དང་། བཀུར་སྟི་དང་། གྲགས་པ་སྙན་པ་དང་ལྡན་པ་ཡིན་ནོ་ཞེས་ང་རྒྱལ་དང་ཁེངས་པ་མེད་ཅིང་གཞན་དམན་པ་དག་ལ་བརྙས་པར་མི་བྱ་བ་དང་། བདག་གི༌[^416]དགེ་བའི་རྩ་བ་དེ་གཞན་དང་ཐུན་མོང་དུ་བྱས་ནས་བྱང་ཆུབ་ཆེན་པོར་ཡོངས་སུ་བསྔོ་བ་དང་། གཞན་གྱི༌[^417]དགེ་བའི་རྩ་བ་དེ་ཡང་བདག་དང་ཐུན་མོང་དུ་བྱས་ནས་བྱང་ཆུབ་ཆེན་པོར་ཡོངས་སུ་བསྔོ་བ་དང་། བདག་གི༌[^418]སྡིག་པ་ཡང་གཞན་གྱི་སྡིག་པ་དང་ཐུན་མོང་དུ་བྱས་ནས་སོ་སོར་བཤགས་པ་དང་། གཞན་གྱི་སྡིག་པ་ཡང་བདག་དང་ཐུན་མོང་དུ་བྱས་ནས་སོ་སོར་བཤགས་པའོ། །

[Block 732]
གཞན་ཡང་དེ་ཀུན་དུ་སྤྱོད་པ་ཕྱིན་ཅི་མ་ལོག་པ་ཡིན་ཏེ།

[Block 733]
འཕགས་པ་དཀོན་མཆོག་སྤྲིན་ལས།

[Block 734]
དེ་ཟ་ན། དེ་འཐུང་ན། དེ་འགྲོ་ན། དེ་ཉལ་ན། དེ་གློ་གཡས་པས་ཉལ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ་མདོ་དེ༌[^419]ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 735]
གཞན་ཡང་དེ་དམ་བཅའ་བ་ཕྱིན་ཅི་མ་ལོག་པ་ཡིན་ཏེ། སྔོན་གྱི་རྒྱལ་པོ་ནམ་མཁས་འདི་སྐད་དུ།

[Block 736 [VERSE]]
དི་རིང་ཕན་ཆད་ནམ་དུ་ཡང་། །
བདག་ལ་འདོད་ཆགས་སེམས་བྱུང་ན། །
ཕྱོགས་བཅུ་དག་ན་བཞུགས་པ་ཡི། །
སངས་རྒྱས་ཐམས་ཅད་བསླུས་པར་འགྱུར། །

[Block 737 [VERSE]]
ཐ་བའི་སེམས་དང་གནོད་སེམས་དང་། །
ཕྲག་དོག་དང་ནི་སེར་སྣ་དང་། །
དི་རིང་ཕན་ཆད་མི་བྱའོ། །
ཚངས་པར་སྤྱོད་ལ་གནས་བགྱི་ཞིང་། །

[Block 738 [VERSE]]
སྡིག་པ་འདོད་པ་ཡོངས་སུ་སྤང་། །
ཚུལ་ཁྲིམས་སྡོམ་དང་དེས་པ་ལ། །
སངས་རྒྱས་རྗེས་སུ་བསླབ་པར་བྱ། །

[Block 739]
ཞེས་གསུངས་པ་དང་།

[Block 740]
འཕགས་པ་ལྷག་པའི་བསམ་པ་བསྐུལ་བའི་མདོ་ལས།
--- END BLOCKS ---
