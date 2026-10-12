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

[Block 741]
བཅོམ་ལྡན་འདས་བདག་ཅག་དེང་སླན་ཆད་དེ་བཞིན་གཤེགས་པའི་སྤྱན་སྔར་ཡི་དམ་འདི་ལྟ་བུ་བཅའ་བར་བྱའོ། །

[Block 742]
བཅོམ་ལྡན་འདས་གལ་ཏེ་བདག་གིས༌[^420]དེང་སླན་ཆད་བྱང་ཆུབ་སེམས་དཔའི་ཐེག་པའི་གང་ཟག་གི་ལྟུང་བ་མེད་པ་ཡང་རུང་སྟེ། གླེངས་ན་བདག་ཅག་གིས༌[^421]དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ལ་བསླུས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ་མདོ་ཉིད་དུ་བལྟ་བར་བྱའོ། །

[Block 743]
གཞན་ཡང་དེ་བསྔོ་བ་ཕྱིན་ཅི་མ་ལོག་པ་ཡིན་ཏེ། གསེར་འོད་དམ་པའི་བསྔོ་བ་དང་། བྱང་ཆུབ་སེམས་དཔའ་རྡོ་རྗེ་རྒྱལ་མཚན་གྱི་ཡོངས་སུ་བསྔོ་བ་ཆེན་པོ་བཅུ་དང་། གཞན་ཡང་འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་བསོད་ནམས་ཀྱི་ཚོགས་ཉི་ཤུ་པ་དང་། སྤྱོད་པ་ལ་འཇུག་པའི་བསྔོ་བའི་ལེའུ་ལ་སོགས་པའོ། །

[Block 744]
གཞན་ཡང་དེ་སྨོན་ལམ་ཕྱིན་ཅི་མ་ལོག་པ་ཡིན་ཏེ། འཕགས་པ་བཟང་པོ་སྤྱོད་པ་དང་། འཕགས་པ་ས་བཅུ་པའི་སྨོན་ལམ་ཆེན་པོ་བཅུ་དང་། བཅོམ་ལྡན་འདས་སྨན་གྱི་བླ་བཻ་ཌཱུརྱ་འོད་ཀྱི་རྒྱལ་པོའི་སྨོན་ལམ་ཆེན་པོ་བཅུ་གཉིས་དང་། སློབ་དཔོན་རྟ་དབྱངས་ཀྱིས་མཛད་པའི་སྨོན་ལམ་བདུན་ཅུ་པ༌[^422]ལ་སོགས་པའོ། །

[Block 745]
གཞན་ཡང་བླ་མའི་ཞལ་ནས་བྱུང་བའི་མདོ་སྡེ་མ་ལུས་པའི་དོན་བསྡུས་པ་ཕ་དང་མ་ལྟ་བུ་དང་། བུ་དང་བུ་མོ་ལྟ་བུའི་ཆོས་ལྔ་བཅུ་པོ་རྣམས་ཀྱང་སྐད་ཅིག་སྐད་ཅིག༌[^423]ལ་དྲན་པར་བྱའོ། །

[Block 746]
གཞན་ཡང་བྱང་ཆུབ་སེམས་དཔའ་དེས་དུས་གཅིག་ལ་རྟག་ཏུ་མདོ་སྡེ་མ་ལུས་པ་བཀླག་པར་ཡང་བྱའོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། ལས་དང་པོ་པ་གཉེན་པོ་ཤས་ཆུང་ཞིང་རྐྱེན་ལ་ལྟོས་པ༌[^424]ཡིན་པས་མདོ་སྡེ་བལྟ་བ་ལ་བརྩོན་པར་བྱའོ། །

[Block 747]
གཞན་ཡང་མདོ་སྡེའི་དོན་མ་ལུས་པར་བསྡུས་པ་ཡིན་པས་མདོ་ཀུན་ལས་བཏུས་པ་དང་། བསླབ་པ་ཀུན་ལས་བཏུས་པ་དང་། [^425]བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ་དང་། ཚུལ་ཁྲིམས་ཀྱི་ལེའུ་དང་། སྡོམ་པ་ཉི་ཤུ་པ་རྣམས་ཀྱང་དུས་དུས༌[^426]སུ་བལྟ་བ་དང་། མཉན་པ་དང་། བྲི་བར༌[^427]བྱའོ། །

[Block 748]
གཞན་ཡང་ཐེག་པ་ཆེན་པོའི་མདོ་སྡེའི་དོན་དང་། སྔོན་གྱི་སློབ་དཔོན་ཆེན་པོ་རྣམས་དང་། ད་ལྟར་གྱི་བླ་མ་མཁས་པ་ཆེན་པོ་རྣམས་ཀྱི་དགོངས་པ་ཡིན་པས་བསྟན་བཅོས་འདི་ཉིད་ཀྱང་བལྟ་བ་དང་། མཉན་པ་དང་། བྲི་བར་བྱའོ། །

[Block 749]
གཞན་ཡང་ཉིན་ལན་གསུམ་མཚན་ལན་གསུམ་ཕུང་པོ་གསུམ་པ་གདོན་པར་བྱ་སྟེ།

[Block 750]
འཕགས་པ་དྲག་ཤུལ་ཅན་གྱིས་ཞུས་པ་ལས།

[Block 751]
དེས་ཉིན་ལན་གསུམ་མཚན་ལན་གསུམ་དུ་ཁྲུས་བྱས་ཏེ། གོས་གཙང་མ་བགོས་ནས་ཕུང་པོ་གསུམ་པ་གདོན་པར་བྱའོ་ཞེས་གསུངས་པ་དང་། འཕགས་པ་ཆོས་ཐམས་ཅད་འབྱུང་བ་མེད་པར་བསྟན་པའི་མདོ་ལས་ཀྱང་།

[Block 752]
ཉིན་དང་དེ་བཞིན་མཚན་མོ་ལན་གསུམ་དུ། །བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་མགོས་ཕྱག་འཚལ། ། ཞེས་གསུངས་པ་དང་། འཕགས་པ་དཀོན་མཆོག་སྤྲིན་ལས་ཀྱང་། དེ་ལྟར་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཉིན་ལན་གསུམ་མཚན་ལན་གསུམ་དུ་མཆོད་པར་བྱེད་དོ་ཞེས་གསུངས་པ་དང་། འཕགས་པ་ཉེ་བ༌[^428]འཁོར་གྱིས་ཞུས་པ་ལས་ཀྱང་། དེས་ཉིན་མཚན་དུ་བཤགས་པ་བྱེད་དོ་ཞེས་གསུངས་པ་དང་། འཕགས་པ་ཐོགས་མེད་ཀྱི་ཞལ་ནས་ཀྱང་། བྱང་ཆུབ་སེམས་དཔའ་མྱུར་དུ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་འདོད་པས༌[^429]ཉིན་ལན་གསུམ་མཚན་ལན་གསུམ་དུ་ཕྱག་འཚལ་བ་དང་། མཆོད་པ་དང་སྡིག་པ་སོ་སོར་བཤགས་པ་དང་། རྗེས་སུ་ཡི་རང་བ་དང་། བསྐུལ་བ་དང་། གསོལ་བ་གདབ་པ་དང་། ཡོངས་སུ་བསྔོ་བ་རྣམས་ཀྱང༌[^430]བྱའོ་ཞེས་གསུངས་སོ། །

[Block 753]
དེ་དག་གི་ཕན་ཡོན་ཡང་འཕགས་པ་སྤྱན་རས་གཟིགས་ཀྱི་མདོ་དང་ཆོས་བཤད་པ་བརྒྱ་པ། སློབ་དཔོན་དཔའ་བོའི༌[^431]རིན་པོ་ཆེ་ཕྲེང་བ་ལྟ་བུའི་གཏམ་དག་ཏུ་བལྟ་བར་བྱའོ། །

[Block 754]
དེ་ཡང་འཕགས་པ་བཟང་པོ༌[^432]སྤྱོད་པའི་གཞུང་གིས་ཀྱང༌[^433]བྱའོ། །

[Block 755]
ཡང་ན་ཕུང་པོ་གསུམ་པའི་མདོ་ཉིད་གདོན་པར་བྱའོ། །

[Block 756]
ཡང་ན་བྱང་ཆུབ་སེམས་དཔའ་མཁས་པ་བློ་དང་ལྡན་པ་ཐོས་པས་བརྒྱན་པ་དེས་ནི་འཕགས་པ་བཟང་པོ༌[^434]སྤྱོད་པ་འདི་ཉིད་ལ་གནས་ནས་བླ་མའི་ཞལ་ལས་འབྱུང་བའི་གདམས་ངག༌[^435]གི་ཆོ་ག་རྒྱས་པར་བྱའོ། །

[Block 757]
དེ་བས་ན་སློབ་དཔོན་ཞི་བའི་ལྷའི་ཞལ་ནས།

[Block 758 [VERSE]]
ཉིན་དང་མཚན་མོ་ལན་གསུམ་དུ། །
ཕུང་པོ་གསུམ་པ་གདོན་པར་བྱ། །
རྒྱལ་དང་བྱང་ཆུབ་སེམས་བརྟེན་པས། །
ལྟུང་བའི་ལྷག་མ་དེས་ཞི་བྱ། །

[Block 759]
ཞེས་སྤྱོད་པ་ལ་འཇུག་པ་ལས་གསུངས་སོ། །

[Block 760]
དེ་ལྟ་བུའི་ཆོ་ག་དེའི་རྗེས་ལ་གསུམ་ལ་སྐྱབས་སུ་འགྲོ་བ་དང་། ལྟུང་བའི་ཉེས་པ་སོ་སོར་བཤགས་ལ། བྱང་ཆུབ་ཀྱི་སེམས་རྣམ་པ་གཉིས་བསྐྱེད་ནས། བདག་གིས༌[^436]ཐེག་པ་ཆེན་པོའི་མདོ་སྡེ་ནས་གསུངས་པའི་བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་མ་ལུས་པ་ཐམས་ཅད་ལ་བསླབ་པར་བྱའོ་ཞེས་མོས་པར་བྱའོ། །

[Block 761]
[^437]དེ་བས་ན་དེ་ལྟ་བུའི་ཉིན་དང་མཚན་དུ་དོན་མེད་པར་མི་གནས་པའི་རྣལ་འབྱོར་པ་དེ་ནི་ཕུན་སུམ་ཚོགས་པ་གསུམ་དང་ལྡན་ཏེ། བླ་མའི་ཞལ་ནས་འདི་སྐད་དུ་ཕུན་སུམ་ཚོགས་པ་གསུམ་གྱིས་བདེ་བ་ལ་རེག་པར་འགྱུར་ཏེ། འདི་ལྟར་སྦྱོར་བ་དང་། བསམ་པ་དང་། སྔོན་གྱི་རྒྱུ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 762]
དེ་ལ་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་ནི་ལུས་དང་ངག་དང་ཡིད་ཀྱི་ཉེས་པ་རྒྱུན་དུ་མི་བྱེད་ལ་སྡིག་པ་འཆགས་པའོ། །

[Block 763]
བསམ་པ་ཕུན་སུམ་ཚོགས་པ་ནི་འདི་ལྟར་བདག་ཆོས་ཀྱི་བསམ་པས་ཡིན་གྱི་ལོག་པར་འཚོ་བ་ལ་སོགས་པ་ཆོས་མ་ཡིན་པས་ནི་མ་ཡིན་ནོ། །

[Block 764]
བདག་ཀྱང་བྱང་ཆུབ་ཆེན་པོ་དོན་དུ་གཉེར་བ་ཡིན་གྱི། འཇིག་རྟེན་པའི་བདེ་བ་དོན་དུ་གཉེར་བ་མ་ཡིན། དེ་ལ་སྔོན་གྱི་རྒྱུ་ཕུན་སུམ་ཚོགས་པ་ནི་དེས་སྔོན་གྱི་དུས་སུ་བསོད་ནམས་བྱས་ཤིང་། དགེ་བ་བྱས་པས་ད་ལྟར་གོས་དང་ཟས་དང་ཡོ་བྱད་རྣམས་ཀྱིས་ཕོངས་པར༌[^438]མ་གྱུར་པ་ཡིན་ཞིང་གཞན་ལ་ཡང་བགོ་བཤའ་བྱེད་པའི་ངང་ཚུལ་ཅན་ཡིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 765]
འདི་ལྟར་ལས་དང་པོ་པའི་སློབ་མ་བློ་ཆུང་བ་དེ་དང་པོ་ཉིད་ནས་ལམ་ལ་འཇུག་པ་མི་བྱ་སྟེ། དེ་ལ་ཐོག་མར་བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་རྒྱ་ཆེན་པོ་བཀོད་པའི་མདོ་སྡེ་དང་། བསྟན་བཅོས་ཐམས་ཅད་བཤད་པར་བྱ་ཞིང་ཚུལ་དེ་མཁས་པར་བྱས་ནས། གཟོད་གང་ཟག་ལམ་ལ་འཇུག་པའི་ཆོ་ག་བྱའོ་ཞེས་བླ་མ་དག་གསུང་བ༌[^439]ཡིན་ནོ། །

[Block 766]
འདིར་སྨྲས་པ།

[Block 767 [VERSE]]
དཀོན་མཆོག་གསུམ་གུས་ཡུལ་ལ་ཞེན་པ་སྤངས། །
འཆི་བ་རྗེས་དྲན་ཚུལ་ཁྲིམས་གཙོ་བོར་བྱེད། །
བླ་མ་ལ་གུས་དད་ལྡན་གཡོ་སྒྱུ་མེད། །
སྡིག་པའི་གྲོགས་སྤངས་ཐུན་ཚིགས་སྦྱོར་བར་ལྡན། །

[Block 768 [VERSE]]
ཐུན་ཚིགས་དྲུག་པ་དུམ་བུ་བཅོ་བརྒྱད་འགྱུར། །
སྔ་དྲོའི་ཐུན་ལ་དུམ་བུ་གསུམ་ཡོད་པའི། །
དུམ་བུ་དང་པོ་དུམ་བུ་བར་པ་ལ། །
ཉེས་པ་བྱུང་བ་དུམ་བུ་ཐ་མ་དེར། །

[Block 769 [VERSE]]
བྱང་ཆུབ་སེམས་བརྗེད་སེམས་དཔའ་ཉམས་པར་འགྱུར། །
ཕྱི་མ་ལྔ་ཡང་དེ་ཡིས་བསྒྲེ་བར་བྱ། །
དུམ་བུ་དུམ་བུར་ལེགས་པར་གསོ་བྱེད་པ། །
སྐྱེས་བུ་རབ་ཡིན་འབྲིང་ནི་གཉིས་ལགས་སོ།[^440] །

[Block 770 [VERSE]]
དུམ་བུ་ཐ་མར་གསོ་བ་ཐ་མ་སྟེ། །
རབ་ཀྱི་རབ་ནི་སྐད་ཅིག་དང་པོར་གསོ། །
རབ་ཀྱི་འབྲིང་ནི་སྐད་ཅིག་གཉིས་པར་གསོ། །
རབ་ཀྱི་ཐ་མ་སྐད་ཅིག་ཐ་མར་གསོ། །

[Block 771]
དེ་ལྟར་གྱུར་པས་སྐྱེས་བུ་རབ་འབྲིང་རྒྱུ།[^441] །ཕྱི་མ་ཀུན་ཡང་དེ་ཡིས་བསྒྲེ་བར་བྱ། །

[Block 772]
བླ་མ་མཁས་པ་ཆེན་པོ་ཁ་ཅིག་ནི་འདི་སྐད་དུ་གསུང་སྟེ།[^442] ཉེས་པ་བྱུང་བ་ཉིད་ཀྱི་རྗེས་ལ་གསོ་བྱེད་པ། །

[Block 773 [VERSE]]
སྐྱེས་བུ་རབ་ཡིན་སྐད་ཅིག་གཉིས་པ་སོགས། །
དེ་ཡི་རྗེས་ལ་གསོ་བ་འབྲིང་པོ་སྟེ། །
སྐྱེས་བུ་ཐ་མས་དུས་ཚིགས་དྲུག་པོར་གསོ། །

[Block 774]
ཞེས་གསུངས་སོ། །

[Block 775]
ལྷག་པའི་ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་བསྟན་ཟིན་ཏོ།། །།
--- END BLOCKS ---
