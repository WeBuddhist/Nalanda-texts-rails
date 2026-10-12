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

[Block 811]
བྱམས་པ་དེ་དེ་བཞིན་ནོ། །

[Block 812]
ཇི་སྐད་སྨྲས་པ་དེ་བཞིན་ཏེ། གང་དག་མཆོག་གི་ཆོས་ཡོངས་སུ་སྤངས་ནས་ལས་ངན་པ་རྩོམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་ནི་ཤེས་རབ་ཤིན་ཏུ་ཆུང་བར་འགྱུར་རོ། །

[Block 813]
བྱམས་པ་ཁྱོད་ལ་བསྟན་ཏོ། །

[Block 814]
ཁྱོད་ཀྱིས་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 815]
གང་དག་ལ་བརྩོན་པ་མེད་པ་དང་། བསམ་གཏན་མེད་པ་དང་། སྤོང་བ་མེད་པ་དང་། ཁ་ཏོན་བྱ་བ་མེད་པ་དང་། མང་དུ་ཐོས་པ་ཡོངས་སུ་ཚོལ་བ་མེད་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེ་དག་ནི་དེ་བཞིན་གཤེགས་པའི་བསྟན་པ་ལ་རབ་ཏུ་བྱུང་བ་མ་ཡིན་ནོ། །

[Block 816]
བྱམས་པ་དེ་བཞིན་གཤེགས་པའི་བསྟན་པ་ནི་བསམ་གཏན་དང་། སྤོང་བས་རབ་ཏུ་ཕྱེ་བ། ཡེ་ཤེས་ཀྱིས༌[^458]འདུས་བྱས་པ། ཡེ་ཤེས་ཀྱིས་མཉམ་པར་བཞག་པ། མངོན་པར་བརྩོན་པས་རབ་ཏུ་ཕྱེ་བ་ཡིན་གྱི། ཁྱིམ་པའི་ལས་ཀྱི༌[^459]མཐའ་དང་། ཞལ་ཏ་བྱེད་པས་རབ་ཏུ་ཕྱེ་བ་ནི་མ་ཡིན་ནོ། །

[Block 817]
མི་རིགས་པ་བརྩོན་པ་དང་། འཁོར་བ་ལ་མངོན་པར་དགའ་བ་རྣམས་ཀྱི་ལས་ནི་འདི་ཡིན་ཏེ་འདི་ལྟར་ཞལ་ཏ་བྱེད་པ་དང་། འཇིག་རྟེན་པའི་བྱ་བས་གཟིངས་པ་སྟེ། དེ་ལ་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་འདོད་པ་བསྐྱེད་པར་མི་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 818]
བླ་མའི་ཞལ་ནས་ཀྱང་། དེ་ལྟར་ཐོས་པ་དང་ལྡན་པའི་བྱང་ཆུབ་སེམས་དཔས་ཆོས་སྨྲ་བ་ལས་ལྡོག་པར་བྱ་སྟེ། མངོན་པར་ཤེས་པ་མ་ཐོབ་བར་དུ་ཐོས་པ་ཙམ་གྱིས་གཞན་ལ་ཕན་གདགས་པར་མ་གསུངས་ཏེ་ཞེས་པ་དང་། ཡང་གསུངས་པ། དེ་བས་ན་མང་དུ་ཐོས་པ་ཙམ་གྱིས༌[^460]ཆོས་སྨྲ་བར་ནི་མི་བྱ་སྟེ། མངོན་པར་ཤེས་པ་ཐོབ་ནས་གཟོད་གཞན་གྱི་དོན་བྱ་སྟེ་ཞེས་པ་དང་།

[Block 819]
ཡང་དེ་ཉིད་ལས།

[Block 820]
མངོན་པར་ཤེས་པ་མ་ཐོབ་པར་སློབ་མ་ཡོངས་སུ་སྨིན་པར་མི་ནུས་ཀྱི་རང་ཉིད་འཆི་བར་ཟད་དེ། སློབ་དཔོན་ཞི་བའི་ལྷའི་ཞལ་ནས།

[Block 821 [VERSE]]
སེམས་ཅན་མོས་པ་སྣ་ཚོགས་པ། །
རྒྱལ་བས་ཀྱང་ནི་མི་མགུ་ན། །
བདག་འདྲ་ངན་པས་སྨོས་ཅི་དགོས། །
དེ་བས་འཇིག་རྟེན་བསམ་པ་བཏང་། །

[Block 822]
ཞེས་ཁུངས་དང་བཅས་ནས་ཏིང་ངེ་འཛིན་གྱི་ཚོགས་ཀྱི་ལེའུ་ལས་གསུངས་སོ། །

[Block 823]
དེ་བས༌[^461]དོན་འདི་ལ་དགོངས་ནས། སློབ་དཔོན་འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་ནས།

[Block 824 [VERSE]]
སྐྱེ་བ་ཀུན་དུ་རྗེས་འབྲང་བའི། །
མངོན་པར་ཤེས་པ་ལྔ་ཐོབ་ནས། །
རྟག་ཏུ་སེམས་ཅན་ཐམས་ཅད་ལ། །
ཀུན་དུ་ཕན་དང་བདེ་བ་བྱ། །

[Block 825]
ཞེས་གསུངས་སོ། །

[Block 826]
བླ་མའི་གདམས་ངག་མེད་པར་གཞུང་ཐོས་པ་ཙམ་ལ་བརྟེན་ནས་སྒོམ༌[^462]པར་བྱེད་པ་དེ་ཡང་འདིར་ཞར་ལ་བཀག་སྟེ། དེ་ལྟ་བུའི་རྣལ་འབྱོར་ལ་བརྩོན་པར་བྱས་ཀྱང་མངོན་པར་ཤེས་པ་ཡང་སྐྱེ་བར་མི་འགྱུར་ཞིང་། རྫོགས་པའི་བྱང་ཆུབ་ཆེན་པོ་ཡང་མི་འཐོབ་པའི་ཕྱིར་རོ། །

[Block 827]
དོན་འདི་ལ་དགོངས་ནས།

[Block 828]
བྲམ་ཟེ་ས་ར་ཧ་པ་ཆེན་པོས་དོན་དམ་པའི་རིགས་པ་ལས།

[Block 829]
བླ་མའི་མན་ངག་ཅེས་བྱ་བདུད་རྩིའི་རོ། །གང་གིས་ངོམས་པར་འཐུངས་པར༌[^463]མ་གྱུར་པ། །

[Block 830]
དེ་ནི་བསྟན་བཅོས་མང་པོའི་མྱ་ངམ་ཐང་དཀྱིལ་དུ། །སྐོམ་བཞིན་དུ་ནི་ངེས་པར་འཆི་བར་འགྱུར། །ཞེས་གསུངས་པ་དང་། འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་ནས་ཀྱང་། རྒྱུད་མང་རབ་ཏུ་ཐོས་ཤིང་ལུང་ལ་ལེགས་སྦྱངས༌[^464]ཀྱང་། །བླ་མའི་བསྙེན་བཀུར་དམན་ཕྱིར་དེ་ཉིད་ལུང་ཐོབ་མ་གྱུར་པ། །

[Block 831]
དེ་ནི་བདག་ཕན༌[^465]ཙམ་ལའང་དབང་མེད་བསྟན་བཅོས་མཆུ། །དེ་ནི་བསྟན་བཅོས་སྐྱོ་བའི་རྒྱུ་ཙམ་འབའ་ཞིག་ཡིན། །ཞེས་གསུངས་སོ། །

[Block 832]
མངོན་ཤེས་མེད་པ༌[^466]ལྡན་པའི་ཉིན་མཚན་གྱི།[^467] །ཞེས་པ་ལ་སོགས་པའི་ཤློ་ཀ་གཉིས་ནི་དཀྱུས་ཇི་ལྟ་བ་ཉིད་དོ། །

[Block 833]
འདི་ལྟར་རྫོགས་པའི་བྱང་ཆུབ་ཆེན་པོ་ནི་ཚོགས་རྣམ་པ་གཉིས་ལ་རག་ལས།

[Block 834]
ཚོགས་རྣམ་པ་གཉིས་ཀྱང་གཞན་གྱི་དོན་ལ་རག་ལས།

[Block 835]
དེ་ཡང་མངོན་པར༌[^468]ཤེས་པ་ཡང་ཞི་གནས་ལ་རག་ལས།

[Block 836]
ཞི་གནས་ཀྱང་ཚུལ་ཁྲིམས་ལ་རག་ལས་པས།

[Block 837]
དང་པོ་ཚུལ་ཁྲིམས་བསྟན་པ་ཡིན་ནོ། །

[Block 838]
དེ་བས་ན་ཚུལ་ཁྲིམས་ལས་ཞི་གནས་འབྱུང་ལ། ཞི་གནས་ལས་མངོན་པར་ཤེས་པ་འབྱུང་བས།

[Block 839 [VERSE]]
[^469] མངོན་ཤེས་འབྱུང་བར་མི་འགྱུར་ལ། །
དེ་ཕྱིར་ཞི་གནས་བསྒྲུབ་པའི༌[^470]ཕྱིར། །
ཡང་དང་ཡང་དུ་འབད་པར་བྱ། །

[Block 840]
ཞེས་སྨྲས་སོ། །

[Block 841]
མངོན་པར་ཤེས་པ་ནི་འདི་ལྟར་ལྷའི་མིག་གི་མངོན་པར་ཤེས་པ་དང་། ལྷའི་རྣ་བའི་མངོན་པར་ཤེས་པ་དང་། གཞན་གྱི་སེམས་ཤེས་པའི་མངོན་པར་ཤེས་པ་དང་། སྔོན་གྱི་གནས་རྗེས་སུ་དྲན་པ་དང་། རྫུ་འཕྲུལ་གྱི་མངོན་པར་ཤེས་པ་དང་། ཟག་པ་ཟད་པའི་མངོན་པར་ཤེས་པའོ།[^471] །

[Block 842]
དེ་ལྟ་བུའི་མངོན་པར་ཤེས་པ་དེ་དག་ཞི་གནས་ལས་འབྱུང་བ་ཡིན་པས་ཞི་གནས་བསྒྲུབ་པར་བྱ་སྟེ།

[Block 843 [VERSE]]
ཞི་གནས་ཡན་ལག་རྣམས༌[^472]ཉམས་པས། །
རབ་ཏུ་འབད་དེ་བསྒོམ༌[^473]བྱས་ཤིང་། །
ལོ་ནི་སྟོང་ཕྲག་དག་གིས་ཀྱང་། །
ཏིང་འཛིན་འགྲུབ་པར་མི་འགྱུར་རོ། །

[Block 844]
ཞི་གནས་ཡན་ལག་ཅེས་པ་ནི་བླ་མས་མཛད་པའི་ཏིང་ངེ་འཛིན་ཚོགས་ཀྱི་ལེའུའི་སྤང་བར་བྱ་བ་ལ་སོགས་པ་དགུའོ། །

[Block 845]
གཞན་ནི་གོ་སླའོ།[^474] །
--- END BLOCKS ---
