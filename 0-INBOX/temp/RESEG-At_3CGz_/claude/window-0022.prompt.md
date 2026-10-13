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

[Block 776]
འདི་ལྟར་ཚུལ་ཁྲིམས་འབའ་ཞིག་ཙམ་གྱིས་ནི་ཆོག་པར་ནི་མི༌[^443]བཟུང་སྟེ། ཏིང་ངེ་འཛིན་དང་། ཤེས་རབ་དག་ཀྱང་བསྐྱེད་དགོས་པ་ཡིན་ནོ། །

[Block 777]
འོན་ཀྱང་ཚུལ་ཁྲིམས་ལ་བརྟེན་ནས་ཏིང་ངེ་འཛིན་སྐྱེ་བར་འགྱུར་ཏེ།

[Block 778]
འཕགས་པ་ཟླ་བ་སྒྲོན་མའི་མདོ་ལས།

[Block 779]
ཉོན་མོངས་མེད་པའི་ཏིང་འཛིན་མྱུར་ཐོབ་སྟེ། །འདི་ནི་ཚུལ་ཁྲིམས་རྣམ་དག་ཕན་ཡོན་ཡིན། །ཞེས་གསུངས་སོ། །

[Block 780]
སློབ་དཔོན་ཞི་བའི་ལྷའི་ཞལ་ནས་ཚུལ་ཁྲིམས་ནི་ཏིང་ངེ་འཛིན་འགྲུབ་པ་ཡིན་ཏེ་ཞེས་པ་དང་། ཡང་དེ་བས་ན་ཏིང་ངེ་འཛིན་གྱི་རྒྱུའི་སྦྱོར་བ་གང་ཅི་ཡང་རུང་བ་དེ་དག་ནི་ཚུལ་ཁྲིམས་ཀྱི༌[^444]ནང་དུ་འདུས་པར་ཤེས་པར་བྱའོ། །

[Block 781]
དེ་བས་ན་ཏིང་ངེ་འཛིན་དོན་དུ་གཉེར་བས་དྲན་པ་དང་ཤེས་བཞིན་གྱི་ངང་ཚུལ་ཅན་དུ་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 782]
ཡང་ཚུལ་ཁྲིམས་དོན་དུ་གཉེར་བས་ཀྱང་ཏིང་ངེ་འཛིན་ལ་འབད་པར་བྱ་སྟེ་ཞེས་པ་དང་། ཡང་ཚུལ་ཁྲིམས་དོན་དུ་གཉེར་བ་གཉིས་གཅིག་གིས་གཅིག་འཕེལ་བར་བྱེད་པ་འདི་གཉིས་ཀྱིས་སེམས་ཡོངས་སུ་སྦྱང་བ་ཡོངས་སུ་གྲུབ་པོ་ཞེས་གསུངས་པས་ཚུལ་ཁྲིམས་མེད་པའི་ཏིང་ངེ་འཛིན་སྐྱེ་བར་མི་འགྱུར་བས་ན། དེའི་ཕྱིར་ཚུལ་ཁྲིམས་ལ་འབད་པར་བྱ་དགོས་སོ། །

[Block 783]
དེ་བས་ཚུལ་ཁྲིམས་ཕུན་སུམ་ཚོགས་པའི་ཏིང་ངེ་འཛིན་གྱིས༌[^445]མངོན་པར་ཤེས་པ་བསྐྱེད་ནས་གཞན་གྱི་དོན་བྱ་བ་དང་། ཚོགས་རྣམ་པ་གཉིས་བསགས་པའི་ཐབས་ནི་མངོན་པར་ཤེས་པ་ཡིན་པས་དེ་བསྟན་པའི་ཕྱིར།

[Block 784 [VERSE]]
བསོད་ནམས་ཡེ་ཤེས་རང་བཞིན་གྱི། །
ཚོགས་ནི་ཡོངས་སུ་རྫོགས་པ་ཡི། །
རྒྱུ་ནི་སངས་རྒྱས་ཐམས་ཅད་དག །
མངོན་ཤེས་བསྐྱེད་པ་ཉིད་དུ་བཞེད། །

[Block 785]
ཅེས་བྱ་བ་དེ་ཡིན་ནོ། །

[Block 786 [VERSE]]
ཚོགས་གཉིས་བསག་པར་འདོད་པ་དང་། །
རྟག་ཏུ་གཞན་དོན་བྱེད་འདོད་པས། །
མངོན་པར་ཤེས་པ་མ་བསྐྱེད་ན། །
དམུས་ལོང་གི་ནི་སྤྱོད་པ་དང་། །

[Block 787 [VERSE]]
སྨྱོན་པའི་སྤྱོད་པ་ཉིད་དང་ནི། །
ཇི་ལྟར་བྱོལ་སོང་སྤྱོད་པ་བཞིན། །
རང་གི་དོན་ཡང་མི་གྲུབ༌[^446]ན། །
གཞན་དོན་འགྲུབ་པར་ཇི་ལྟར་རུང་། །

[Block 788]
ཞེས་པ་ནི་བསྡུས༌[^447]ནས་བསྟན་པའོ། །

[Block 789 [VERSE]]
ཇི་ལྟར་འདབ་གཤོག་མ་སྐྱེས་པའི། །
བྱ་ནི་མཁའ་ལ་འཕུར༌[^448]མི་ནུས། །
དེ་བཞིན་མངོན་ཤེས་ཐོབ་བྲལ༌[^449]བས། །
སེམས་ཅན་དོན་བྱེད་ནུས་མ་ཡིན། །

[Block 790]
མངོན་པར་ཤེས་པ་ཡང་མ་ཐོབ་ཅིང་བསྒོམས་པའི་ཤེས་རབ་ཀྱང་མ་སྐྱེས་པར་ཐོས་པའི་ཤེས་རབ་ཙམ་ལ་བརྟེན་ནས་ཆོས་བཤད་ཅིང་སློབ་མ་སྡུད་པ༌[^450]དེ་ནི་སྨྱོན་པ་ཡིན་ཏེ། ཇི་སྐད་དུ།

[Block 791]
རང་གི་ཚོད་ཀྱང་མི་ཤེས་པར། །སྨྲ་བ་ཇི་ལྟར་སྨྱོན་པ་མིན། །ཞེས་སོ། །

[Block 792]
འཕགས་པ་ལྷག་པའི་བསམ་པ་བསྐུལ་བའི་མདོ་ལས།

[Block 793]
སྨྲ་བ་ལ་དགའ་བ་དང་། སྨྲ་བ་ལ་དགའ་བའི་ཉེས་པ་མཐོང་བར་བྱའོ་ཞེས་པ་དང་། ཡང་དེ་ཉིད་ལས་སྨྲ་བ་ལ་དགའ་བའི་ཉེས་པ་གསུངས་པ།

[Block 794 [VERSE]]
ཐོས་པས་རྒྱགས་ནས་གུས་པར་མི་འགྱུར་ཏེ། །
རྣམ་པར་འགྱིད་པའི་སྨྲ་བ་རྣམས་ལ་ཆགས། །
བརྗེད་པར་འགྱུར་ཞིང་ཤེས་བཞིན་མེད་པར་འགྱུར། །
སྨྲ་ལ་དགའ་བའི་ཉེས་པ་འདི་དག་གོ། །

[Block 795 [VERSE]]
ནང་གི་སེམས་ལས་ཤིན་ཏུ་རིང་བར་འགྱུར། །
ལུས་དང་སེམས་ཀྱང་རབ་སྦྱངས་མ་ཡིན་འགྱུར། །
ཁེངས་པ་དང་ནི་དུད་པ་མང་པོར་འགྱུར། །
སྨྲ་ལ་དགའ་བའི་ཉེས་པ་འདི་དག་གོ། །

[Block 796 [VERSE]]
བྱིས་པ་དམ་པའི་ཆོས་བསམ་རབ་ཏུ་ཉམས། །
སེམས་ནི་མི་མཉེན༌[^451]ཤིན་ཏུ་རྩུབ་པར་འགྱུར། །
ཞི་གནས་ལྷག་མཐོང་དག་དང་རབ་ཏུ་རིང་། །
སྨྲ་ལ་དགའ་བའི་ཉེས་པ་འདི་དག་གོ། །

[Block 797 [VERSE]]
རྟག་ཏུ་བླ་མ་དག་ལ་གུས་པ་མེད། །
སྦགས་པའི་གཏམ་དག་ལ་ནི་དགའ་བ་སྐྱེད། །
སྙིང་པོ་མེད་ལ་གནས་ཤིང་ཤེས་རབ་ཉམས། །
སྨྲ་ལ་དགའ་བའི་ཉེས་པ་འདི་དག་གོ། །

[Block 798]
དེ་བཞིན་དུ་ཡང་གསུངས་པ།

[Block 799 [VERSE]]
བདག་ནི་སྒྲུབ་ཉམས་ད་ནི་ཅི་བྱ་ཞེས། །
འཆི་བའི་དུས་ཚེ་བྱིས་པ་མྱ་ངན་བྱེད། །
གཏིང་རྙེད་མ་གྱུར་ཤིན་ཏུ་སྡུག་བསྔལ་གྱུར།[^452] །
སྨྲ་ལ་དགའ་བའི་ཉེས་པ་འདི་དག་གོ། །

[Block 800 [VERSE]]
རྩྭ༌[^453]བསྐྱོད་བཞིན་དུ་འགྱུར་ཞིང་གཡོ་བ་སྟེ། །
དེ་ནི་དེ་ལྟར་ཐེ་ཚོམ་འགྱུར་དུ་ངེས། །
དེ་ནི་ནམ་ཡང་བློ་བརྟན་མི་འགྱུར་ཏེ། །
སྨྲ་ལ་དགའ་བའི་ཉེས་པ་འདི་དག་གོ། །

[Block 801 [VERSE]]
གར་ལ་ལྟ་བའི་ཁྲོད་ན་འདུག་པ་ཞིག །
དཔའ་བོ་གཞན་གྱི་ཡོན་ཏན་བརྗོད་པ་བཞིན། །
བདག་ཉིད་ནན་ཏན་ཉམས་པར་འགྱུར་བས་ཏེ། །
སྨྲ་ལ་དགའ་བའི་ཉེས་པ་འདི་དག་གོ། །

[Block 802 [VERSE]]
དེ་ནི་གཡོ་ལྡན་ཡང་ཞིང་རེ་ཆད་འགྱུར། །
ཕྱིར་ཞིང་ཕྱིར་ཞིང་རྣམ་པར་འགྱིད་པར༌[^454]འགྱུར། །
འཕགས་པའི་དམ་པའི་ཆོས་ལས་རབ་ཏུ་རིང་། །
སྨྲ་ལ་དགའ་བའི་ཉེས་པ་འདི་དག་གོ། །

[Block 803 [VERSE]]
མཐུ་ཆུང་བསྟི་སྟང་དག་གིས་དགར་འགྱུར་ཏེ། །
མི་ཤེས་ལྡན་པ་གཡོ་ཞིང་འགྱུར་བ་ཡིན། །
སྤྲེའུ་ལྟར་དེ་ཡི་སེམས་ནི་གཡོ་བར་འགྱུར། །
སྨྲ་ལ་དགའ་བའི་ཉེས་པ་འདི་དག་གོ། །

[Block 804]
ཞེས་འབྱུང་སྟེ། དེ་བཞིན་དུ་ཡང་།

[Block 805 [VERSE]]
ཡུན་རིང༌[^455]དུས་ནས་སྨྲ་ལ་དགའ་བས་ན། །
དེས་ནི་བདག་ཉིད་དགའ་བ་མི་འཐོབ་བོ། །
ཚིག་གང་དགའ་བ་མཐའ་ཡས་འཐོབ་འགྱུར་བ། །
ཚིག་གཅིག་ཙམ་ཞིག་བསམས༌[^456]ཀྱང་མཆོག་ཡིན་ནོ། །

[Block 806 [VERSE]]
བུ་རམ་ཤིང་ཤུན་སྙིང་པོ་ཅི་ཡང་མེད། །
དགའ་བར་བྱ་བའི་རོ་ནི་ནང་ན་འདུག །
ཤུན་པ་ཟོས་པས་མིས་ནི་བུ་རམ་རོ། །
ཞིམ་པོ་རྙེད་པར་ནུས་པ་མ་ཡིན་ནོ། །

[Block 807 [VERSE]]
ཤིང་གི་ཤུན་པ་དེ་བཞིན་སྨྲ་བ་སྟེ། །
རོ་ལྟ་བུ་ནི་འདི་ནི་དོན་སེམས་ཡིན། །
དེ་ལྟ་བས་ན་སྨྲ་ལ་དགའ་སྤངས༌[^457]ཏེ། །
རྟག་ཏུ་བག་ཡོད་བྱོས་ལ་དོན་སོམས་ཤིག །

[Block 808]
ཅེས་གསུངས་ཏེ། དེ་བཞིན་དུ་ཡང་གསུངས་པ། དེ་ནས་བཅོམ་ལྡན་འདས་ལ་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བྱམས་པས་འདི་སྐད་ཅེས་གསོལ་ཏོ། །

[Block 809]
གང་དག་མཆོག་གི་ཆོས་ཡོངས་སུ་སྤངས་ནས་ལས་ངན་པ་རྣམས་རྩོམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེ་ནི་ཤེས་རབ་ཤིན་ཏུ་ཆུང་ཞིང་ཤེས་རབ་རྣམ་པར་ཉམས་པར་འགྱུར་བ་ལགས་སོ། །

[Block 810]
དེ་སྐད་ཅེས་གསོལ་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བྱང་ཆུབ་སེམས་དཔའ་སེམས་དཔའ་ཆེན་པོ་བྱམས་པ་ལ་འདི་སྐད་ཅེས་བཀའ་སྩལ་ཏོ། །
--- END BLOCKS ---
