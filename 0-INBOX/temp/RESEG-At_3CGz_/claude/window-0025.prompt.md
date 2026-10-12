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
[Block 876]
མཚན་མ་མེད་པའི་ལྷག་མཐོང་རྣམ་པར་མི་རྟོག་པའི་ཡེ་ཤེས་འབྱུང་ཞེས་ཏེ་ཞེས་པ་དང་། ཡང་དེ་ཉིད་ལས་མཚན་མ་དང་བཅས་པའི་ཞི་གནས་ལ་བརྟེན་པ་པས༌[^482]ནི་མཚན་མ་མེད་པའི་ཞི་གནས་ལ་དམིགས་ནས་ལྷག་མཐོང་སྐྱེད་པའི༌[^483]ཕྱོགས་འདི་བསྔགས་ཏེ། དེ་ལ་གནས་པ་བརྟན་པ་དང་། ཞི་གནས་འབའ་ཞིག་གིས༌[^484]ཉོན་མོངས་པ་སེལ་བ་དང་། རབ་ཏུ་གནོན་པར་འགྱུར་བས་དེ་ནི་འབྲས་བུ་དང་རྗེས་སུ་མཐུན་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ་ཞེས་གསུངས་སོ། །

[Block 877]
ཡང་དེ་ཉིད་ལས་ཇི་ལྟར་བསྒོམ་པ་ནི་འདིར་མི༌[^485]བརྗོད་དེ་གཞུང་མངས་པའི་འཇིགས་པ་དང་། བླ་མ་དམ་པས་ཉམས་སུ་མྱོང་བའི་མན་ངག་ལ་བརྟེན་པར༌[^486]རིགས་ཀྱི། བསྒོམ་པའི༌[^487]མན་ངག་ནི་ཡི་གེར་གནས་པས་ཤེས་པར་དཀའ་བའི་ཕྱིར་དང་། ཞིབ་ཏུ་ནི་ཞི་གནས་དང་ལྷག་མཐོང་བསྟན་པ་ལས་བཤད་པའི་ཕྱིར་རོ་ཞེས་གསུངས་སོ། །

[Block 878]
དེ་ལྟ་བུའི་རྣལ་འབྱོར་པས་ཞི་གནས་གྲུབ་པར་གྱུར་ནས། སྔར་བཤད་པའི་མངོན་པར་ཤེས་པ་ལྔ་པོ་དག་འགྲུབ་པར་འགྱུར་བ་ལ་ཐེ་ཚོམ་མེད་དོ་ཞེས་བླ་མ་གསུང་ངོ་། །གཞན་ཡང་མངོན་པར་ཤེས་པ་བསྐྱེད་པའི་ཐབས་སུ་གྱུར་བ་འཕགས་པ་སྤྱན་རས་གཟིགས་ཀྱིས་ཞུས་པའི་ཆོས་བདུན་པའི་མདོ་ལས་འབྱུང་བའི་བསླབ་པའི་གཞི་དེ་དག་ཀྱང་ཉམས་སུ་བླང་བར་བྱ་བ་དང་། མདོ་དེ་ཉིད་ཀྱང་དུས་དུས་སུ་ཁ་ཏོན་དུ་གདོན་པར་ཡང་བྱའོ། །

[Block 879]
འཕགས་པ་ཐོགས་མེད་ཀྱིས་ཀྱང་བྱང་ཆུབ་སེམས་དཔའ་མངོན་པར་ཤེས་པ་མྱུར་དུ་ཐོབ་པར་འདོད་པས་ཉིན་ལན་གསུམ་མཚན་ལན་གསུམ་དུ་ཕྱག་འཚལ་བ་དང་། མཆོད་པ་དང་སྡིག་པ་བཤགས་པ་དང་། རྗེས་སུ་ཡི་རང་བ་དང་། བསྐུལ་བ་དང་། གསོལ་བ་གདབ་པ་དང་། ཡོངས་སུ་བསྔོ་བ་ལ་བརྩོན་པར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 880]
གཞན་ཡང་འདོད་པ་ཆུང་བ་དང་ཆོག་ཤེས་པ་དང་། གསོ་སླ་བ་དང་རབ་ཏུ་དབེན་པ་ལ་སོགས་པ་ཞི་གནས་ཀྱི་ཚོགས་ཐམས་ཅད་དང་ལྡན་པའོ། །

[Block 881]
དེ་ལྟ་བུའི་རྣལ་འབྱོར་པ་ཞི་གནས་ལ་ལེགས་པར་གནས་པ་ནི་འདོད་པ་ཆུང་ཞིང་ཆོག་ཤེས་པར་འགྱུར་ཏེ།

[Block 882]
འཕགས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྟོང་ཕྲག་བརྒྱ་པ་ལས།

[Block 883]
དགེ་སློང་བསམ་གཏན་ལ་སེམས་ཅུང་ཞིག་བླན་པ་རྣམས་ནི་གོས་ཀྱི་འདུ་ཤེས་ཆུང་བ་ཡིན། ཟས་ཀྱི་འདུ་ཤེས་ཆུང་བ་དང་། པགས་པའི་མདོག་སྣུམ་པ་ཡིན་ཞེས་གསུངས་ཏེ། དེ་ལྟ་བུའི་བྱང་ཆུབ་སེམས་དཔའི་རྣལ་འབྱོར་པ༌[^488]དེ་ནི་འཇིག་རྟེན་པའི་ནོར་ལ་ཞེན་པ་སྤངས་ནས་འཕགས་པའི་ནོར་བདུན་ལ་འབད་པར་བྱེད་དོ། །

[Block 884]
དེ་རྗེས་སུ་དྲན་པ་དྲུག་ཡིད་ལ་བྱེད་དོ། །

[Block 885]
དྲུག་ལས་ཀྱང་རེ་ཞིག་སངས་རྒྱས་དང་ཆོས་དང་དགེ་འདུན་རྗེས་སུ་དྲན་པར་བྱེད་དོ།[^489] །

[Block 886]
དབང་པོ་རྣོན་པོ་དང་། དབང་པོ་རྟུལ༌[^490]པོའི་དབྱེ་བས་སོ། །

[Block 887]
དབང་པོ་རྣོན་པོས་རྗེས་སུ་དྲན་པར་བྱ་བ་ནི་འཕགས་པ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་མདོ་དང་། འཕགས་པ་སངས་རྒྱས་རྗེས་སུ་དྲན་པའི་མདོ་དང་། འཕགས་པ་ནམ་མཁའ་མཛོད་ཀྱི་མདོ་དང་། འཕགས་པ་བློ་གྲོས་མི་ཟད་པའི་མདོ་ལ་སོགས་པར་བལྟ་བར་བྱའོ། །

[Block 888]
དེ་ལ་དབང་པོ་རྟུལ་པོས་རྗེས་སུ་དྲན་པར་བྱ་བ་ནི་འཕགས་པ་དད་པའི་སྟོབས་བསྐྱེད་པའི་མདོ་དང་། འཕགས་པ་སངས་རྒྱས་བགྲོ་བ་དང་། ཆོས་བགྲོ་བ་དང་། དགེ་འདུན་བགྲོ་བའི་མདོ་དང་། འཕགས་པ་སངས་རྒྱས་རྗེས་སུ་དྲན་པའི་མདོ་དེ་ཉིད་དང་། སངས་རྒྱས་རྗེས་སུ་དྲན་པའི་མདོ་ཆུང་བ་དང་། ཐེག་པ་ཆེན་པོའི་མདོ་སྡེ༌[^491]གཞན་དུ་ཡང་བལྟ་བར་བྱའོ། །

[Block 889]
གཞན་ཡང་མདོའི་དགོངས་པ་འཆད་པ་ཡིན་པས། བསླབ་པ་ཀུན་ལས་བཏུས་པའི་དཀོན་མཆོག་གསུམ་རྗེས་སུ་དྲན་པའི་སྐབས་སུ་ཡང་བལྟ་བར་བྱའོ། །

[Block 890]
དེ་ལྟ་བུའི་རྣལ་འབྱོར་པ་དེ་ལ་ལྷག་མཐོང་ཡང་སྐྱེ་བར་འགྱུར་ཏེ་འདིའི་དོན་འོག་ནས་འཆད་པར་འགྱུར་རོ། །

[Block 891]
དེ་བས་ཞི་གནས་དང་ལྷག་མཐོང་ལ་རྣལ་འབྱོར་དུ་བྱེད་པ་ནི་ལམ་ལ་གནས་པ་ཞེས་བྱ་བ་ཡིན་པས། དྲན་པ་ཉེ་བར་གཞག་པ་བཞི་དང་། ཡང་དག་པར་སྤོང་བ་བཞི་དང་། རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་དང་། དབང་པོ་དང་། སྟོབས་དང་། བྱང་ཆུབ་ཀྱི་ཡན་ལག་དང་། འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་པ་རྣམས་ལ་རིམ་གྱིས་གནས་པར་འགྱུར་རོ། །

[Block 892]
ལྷག་པའི་སེམས་ཀྱི་བསླབ་པ་བསྟན་ཟིན་ཏོ། །

[Block 893]
[^492]ད་ནི་ཐབས་དང་ཤེས་རབ་ཟུང་དུ་འབྲེལ་པར་ཤེས་པའི་ཤེས་རབ་ཀྱིས༌[^493]བསོད་ནམས་ཀྱི་ཚོགས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་གཉིས་ཟུང་དུ་འབྲེལ་པར་རྫོགས་པར་བྱའོ་སྙམ་དུ་བསམས༌[^494]ནས།

[Block 894 [VERSE]]
ཤེས་རབ་ཕ་རོལ་ཕྱིན་སྦྱོར་དང་། །
བྲལ་བས་སྒྲིབ་པ་ཟད་མི་འགྱུར། །

[Block 895]
ཞེས་པ་ལ་སོགས་པ་སྨྲས་ཏེ། ཞི་གནས་ཀྱིས་ནི་ལས་དང་ཉོན་མོངས་པ་དང་། རྣམ་པར་སྨིན་པ་དང་། ཆོས་ཀྱི་སྒྲིབ་པ་ལ་སོགས་པ་སྤོང་བར་མི་ནུས་ཏེ། ལྷག་མཐོང་གིས༌[^495]དེ་དག་སྤངས་ནས་ཟད་པར་འགྱུར་བས་ལྷག་མཐོང་བརྟེན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཚིག་གི་ལྷག་མའོ། །

[Block 896]
ད་ནི་ཐབས་དང་ཤེས་རབ་རྒྱས་པར་བཤད་པར་བྱ་སྟེ། གང་ཕྱིར་བཅིངས་པ་ཞེས་གསུངས་པས་ཞེས་པ་ནི་འཕགས་པ་ག་ཡ་མགོའི༌[^496]རིའི་མདོ་དང་། འཕགས་པ་དྲི་མ་མེད་པར་གྲགས་པའི་མདོ་ལས་ཐབས་དང་བྲལ་བའི་ཤེས་རབ་ནི་འཆིང་བའོ། །

[Block 897]
ཤེས་རབ་དང་བྲལ་བའི་ཐབས་ཀྱང་འཆིང་བའོ་ཞེས་གསུངས་སོ། །

[Block 898]
[^497]དེ་བས་གཉིས་ཀ་སྤང་མི་བྱ། །ཞེས་པ་ནི། དཔལ་ཡེ་ཤེས་གྲགས་པའི་ཞལ་ནས་འདི་སྐད་དུ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་ངོ་བོ་ཉིད་དང་། སྦྱིན་པ་ལ་སོགས་པའི་ཐབས་ལ་རབ་ཏུ་འཇུག་གོ། །

[Block 899]
དེ་ཡང་འཕགས་པ་ག་ཡ་མགོའི་རི༌[^498]ལས་གཉིས་པོ་འདི་དག་ནི་བྱང་ཆུབ་སེམས་དཔའི་ལམ་མདོར་བསྡུས་པ་སྟེ། འདི་ལྟ་སྟེ། ཐབས་དང་ཤེས་རབ་པོ་ཞེས་གསུངས་པ་སྟེ། ཐབས་ནི་སྦྱིན་པ་ལ་སོགས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་དང་། ཚད་མེད་པ་དང་། བསྡུ༌[^499]བའི་དངོས་པོ་དང་དེ་ལ་སོགས་པའི་དབྱེ་བས༌[^500]ཕྱེ་བ་སྟེ། དེ་ཉིད་ཀྱང་འཕགས་པ་བློ་གྲོས་མི་ཟད་པ་དང་། དཀོན་མཆོག་སྤྲིན་ལ་སོགས་པའི་མདོ་ལས་གསུངས་པའོ། །ཤེས་རབ་ནི་ཐབས་དེ་ཕྱིན་ཅི་མ་ལོག་པར་ཡོངས་སུ་གཅོད་པའི་རྒྱུའོ། །

[Block 900]
དེས་ཀྱང་ཐབས་ཡང་དག་པར་བརྟགས་ནས། ཕྱིན་ཅི་མ་ལོག་པས། བདག་དང་གཞན་གྱི་དོན་ཇི་ལྟ་བ་བཞིན་དུ་ཉམས་སུ་ལེན་པས་སྔགས་ཀྱིས༌[^501]ཟིན་པའི་དུག་དང་འདྲ་བས་ཀུན་ནས་ཉོན་མོངས་པར་མི་འགྱུར་རོ། །

[Block 901]
དེ་ཡང་མདོ་སྡེ་དེ་ཉིད་ལས་ཐབས་ནི་བསྡུ་བ་ཤེས་པའོ། །ཤེས་རབ་ནི་ཡོངས་སུ་གཅོད་པ་ཤེས་པའོ་ཞེས་གསུངས་པ་དང་། འཕགས་པ་དད་པའི་སྟོབས་བསྐྱེད་པའི་མདོ་ལས་ཀྱང་། ཐབས་ལ་མཁས་པ་གང་ཞེ་ན། གང་ཆོས་ཐམས་ཅད་ཀྱི་བསྡུ་བ་ཤེས་པའོ། །ཤེས་རབ་གང་ཞེ་ན། གང་ཆོས་ཐམས་ཅད་དབྱེར་མེད་པར་ཤེས་པ་ལ་མཁས་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 902]
འདི་དག་ནི་ས་ལ་གནས་པས་ཀྱང་བརྟེན་པར་བྱ་བ་ཡིན་པས། ཤེས་པར་བྱ་བ་ཙམ་འབའ་ཞིག་ནི་མ་ཡིན་ནོ། །

[Block 903]
གང་གི་ཕྱིར་ས་བཅུ་ལ་སོགས་པའི་མདོ་ལས།

[Block 904]
ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྷག་མ་རྣམས་ལ་ཡང་མི་སྤྱོད་པ༌[^502]མ་ཡིན་ནོ་ཞེས་གསུངས་པས། བྱང་ཆུབ་སེམས་དཔའ་ས་བཅུ་ཐམས་ཅད་དུ་ཡང་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཐམས་ཅད་ལ་ཀུན་དུ་སྤྱད་པར་བྱའོ་ཞེས་གསུངས་སོ། །

[Block 905]
དེ་ཡང་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་གཅིག་ཏུ་དགའ་བའི་བྱང་ཆུབ་སེམས་དཔའི་དབང་དུ་བྱས་ནས།

[Block 906]
འཕགས་པ་ཡོངས་སུ་རྒྱས་པའི་མདོ་ཆོས་ཐམས་ཅད་བསྡུས་པ་ལས།

[Block 907]
བྱམས་པ་གང་ཡང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱི༌[^503]བྱང་ཆུབ་ཀྱི་ཕྱིར་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་ཡང་དག་པར་གཟུང་བར་བྱ་བ་དེ་ལ། སྐྱེས་བུ་བླུན་པོ་རྣམས་འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན༌[^504]པ་འབའ་ཞིག་ལ་བསླབ་པར་བྱ་སྟེ། ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྷག་མ་རྣམས་ཀྱིས༌[^505]ཅི་ཞིག་དགོས་ཞེས་ཟེར་ཞིང་། དེས་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལྷག་མ་གཞན་སྨོད་པར་སེམས་པར་འགྱུར་རོ་ཞེས་བྱ་བ་རྒྱ་ཆེར་གསུངས་པ་དང་། འཕགས་པ་རྣམ་པར་སྣང་མཛད་མངོན་པར་བྱང་ཆུབ་པ་ལས་ཀྱང་། ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་འདི་ནི་སྙིང་རྗེ་ཆེན་པོའི་རྩ་བ་ཅན། བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་རྒྱུ་ཅན། ཐབས་ཀྱི་མཐར་ཕྱིན་པའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 908]
དེ་བས་ན་གཉིས་ཀ་ཡང་དུས་ཐམས་ཅད་དུ་བརྟེན་པར་བྱའོ། །

[Block 909]
དེ་ལྟར་ན་བཅོམ་ལྡན་འདས་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པ་གྲུབ་པ་ཡིན་ནོ། །

[Block 910]
དེ་ཡང་སྦྱིན་པ་ལ་སོགས་པའི་ཐབས་ཀྱིས་ནི་གཟུགས་ཀྱི་སྐུ་དང་། ཞིང་དང་། འཁོར་ལ་སོགས་པའི་ལོངས་སྤྱོད་ཆེན་པོའི་འབྲས་བུ་ཕུན་སུམ་ཚོགས་པ་ཡོངས་སུ་འཛིན་པར་མཛད་པས། བཅོམ་ལྡན་འདས་མྱ་ངན་ལས༌[^506]འདས་པ་ལ་གནས་པར་མི་མཛད་དོ། །ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ནི་ཕྱིན་ཅི་ལོག་སྤངས་པས་འཁོར་བར༌[^507]གནས་པར་མི་མཛད་དོ། །

[Block 911]
འཁོར་བ་ནི་ཕྱིན་ཅི་ལོག་གི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 912]
གང་ཡང་ཆོས་ཀྱི་རྣམ་གྲངས་གཟིངས་ལྟ་བུར་ཤེས་པས་ཆོས་རྣམས་ཀྱང་སྤང་བར་བྱ་བས་ན། ཆོས་མ་ཡིན་པ་ལྟ་ཅི་སྨོས་ཞེས་གསུངས་པ་ནི། དེ་ལ་ཕྱིན་ཅི་ལོག་ཏུ་མངོན་པར་ཞེན་པ་སྤང་བར་བྱའོ་ཞེས་གསུངས་ཀྱི། དགོས་པའི་དོན་རྫོགས་པའི་དོན་དུ་ཡང་གནས་པར༌[^508]མི་བྱའོ་ཞེས་གསུངས་པ་ནི་མ་ཡིན་ནོ། །

[Block 913]
དེ་ཡང་ཆོས་ཡོངས་སུ་གཟུང་བར་བྱ་སྟེ། ལོག་པ་ནི་གཟུང་བར༌[^509]མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 914]
དེ་བས་ན།

[Block 915 [VERSE]]
དུས་ཀུན་དུ་ནི་ཐབས་དང་ནི། །
ཤེས་རབ་ཕ་རོལ་བདག་ཅན་ནི། །
བརྟེན་བྱ༌[^510]གང་ཕྱིར་དེ་ལས་ནི། །
མི་གནས་མྱ་ངན་འདས་པར་འགྱུར། །
--- END BLOCKS ---
