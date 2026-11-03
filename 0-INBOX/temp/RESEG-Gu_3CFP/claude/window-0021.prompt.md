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
ཅེས་བསྟན་པས་དེ་ལྟ་བས་ན་སྣང་བར་གྱུར་པ་ཉིད་ཀྱིས་སྣང་བར་གྱུར་བ་ཞེས་བརྗོད་པ་ཡིན་ནོ། །ཇི་ལྟར་དོན་དུ་གྱུར་བ་ཡིན་ཞེ་ན། སྨྲས་པ། དོན་ཐམས་ཅད་སྟོན་པའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ། དོན་ཐམས་ཅད་ནི་འདུས་བྱས་དང་འདུས་མ་བྱས་ལ་སོགས་པའོ། །

[Block 737]
འདི་ལྟར་རོ་ཞེས་སྟོན་པར་བྱེད་པའི་དོན་གྱིས་སྟོན་པ༌[^549]སྟེ། ཤེས་པར་འདོད་པས་སྟོན་པ་དེ་ཡང་བཅོམ་ལྡན་འདས་ལ༌[^550]མ་བརྟེན་པར་དེ་རྟོགས་པ་མེད་པས་སོ། །

[Block 738]
དེ་ཡང་ཇི་ལྟར་སློབ་དཔོན་མ་ཁོལ་གྱིས༌[^551]བསྟོད་པ་དེ་ཉིད་ལས།

[Block 739 [VERSE]]
དོན་ནི་དོན་དུ་མ་རིག་ཅིང་། །
དོན་མ་ཡིན་ཡང་དོན་མིན་དུ། །
བློ་ཡིས་ཆོས་ནི་མ་རྟོགས་པ། །
ཁྱོད་ལ་བརྟེན་ནས་རྟོགས་པ་ཡིན། །

[Block 740 [VERSE]]
ཕལ་ཆེར་དོན་མིན་སྤོང་འདོད་ཀྱང་། །
རྨོངས་པས་དོན་ནི་སྤོང་འགྱུར་ཏེ། །
མི་ཤེས་པ་ནི་དོན་འདོད་ཀྱང་། །
དོན་མ་ཡིན་པ་གྲུབ་པར༌[^552]འགྱུར། །

[Block 741]
ཁྱོད་ལ་བརྟེན་ནས་ཅི་རིགས་པར།

[Block 742 [VERSE]]
གཉི་ག་དག་ནི་རྟོགས་འགྱུར་ཏེ། །
དེ་དག་གཉི་ག་ཉེར་བསྟན༌[^553]པའི། །
དོན་དུ་གྱུར་པ་ཁྱོད་ལ་འདུད། །

[Block 743]
ཅེས་བསྟན་པས། དེས་ན་དོན་ཐམས་ཅད་སྟོན་པ་ཡིན་ཏེ། འདི་ནི་དོན་འདི་ནི་དོན་མ་ཡིན་པའོ་ཞེས་དགེ་བ་དང་མི་དགེ་བ་ལ་སོགས་པའི་དོན་རྟོགས་པར་འདོད་པ་དག་གིས་ཁྱོད་ལ་བརྟེན་པ་མེད་པར་རྟོགས་པ༌[^554]མེད་དོ། །ཇི་ལྟར་ཡེ་ཤེས་སུ་གྱུར་པ་ཡིན་ཞེ་ན། སྨྲས་པ། མི་རྟོགས་པའི༌[^555]ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། མི་རྟོགས་པའི༌[^556]ཞེས་བྱ་བ་ནི་མི་ཤེས་པའོ། །

[Block 744]
རྟོགས་པར་མཛད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་གོ་བར་བྱེད་པས་སོ། །

[Block 745]
འདིས་མི་ཤེས་པའི་གཉེན་པོར་བསྟན་ཏོ། །

[Block 746]
རྟོགས་པ་རྣམས་ཀྱི་ཐེ་ཚོམ་སྐྱེས་པ་གཅོད་པར་མཛད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཐེ་ཚོམ་སྐྱེས་པའི་ཤེས་པའི་གཉེན་པོ་འདི༌[^557]ཡིན་ཏེ། ངེས་པའི་ཤེས་པ་སྐྱེད་པར་བྱེད་པས་སོ། །

[Block 747]
ཟབ་མོའི་གནས་རྣམས་རྣམ་པར་འགྲེལ་པ་ཞེས་བྱ་བ་ནི། ཕྱིན་ཅི་ལོག་གི་ཤེས་པའི་གཉེན་པོར་གྱུར་པའི༌[^558]ཡང་དག་པའི་ཤེས་པ་སྐྱེད་པས་སོ། །

[Block 748]
གྲོལ་བ་རྣམས་ཡོངས་སུ་བྱང་བར་མཛད་པའི་ཕྱིར་ཏེ། བསྟན་པར༌[^559]མཛད་པའི་དོན་དུ་སྦྱོང་བར་མཛད་པའི་དོན་ཏོ། །

[Block 749]
འདིར་སློབ་དཔོན་མ་ཁོལ་གྱིས་བསྟོད་པ་དེ་ཉིད་ལས།

[Block 750 [VERSE]]
རྣམ་པ་ཐམས་ཅད་ཡོངས་མཁྱེན་པས། །
མཁྱེན་བྱ་ཐམས་ཅད་ཀུན་སྣང་བ། །
ཡེ་ཤེས་སྣང་བ་མཛད་པ་ཡི། །
ཡེ་ཤེས་གྱུར་ལ་ཕྱག་འཚལ་ལོ། །

[Block 751]
ཞེས་བྱ་བ་སྟེ། འདིས་ནི་རྣམ་པ་ཐམས་ཅད་མི་ཤེས་པ་དང་། ཐེ་ཚོམ་གྱི་ཤེས༌[^560]པ་དང་། ཕྱིན་ཅི་ལོག་གི་ཤེས་པ་རྣམས་ཀྱི་གཉེན་པོར་གྱུར་པ་རྟོགས་པའི་ཤེས་པ་དང་། ངེས་པའི་ཤེས་པ་དང་། ཡང་དག་པའི་ཤེས་པ་རྣམས་རྣམ་པར་སྦྱོང་བ་ཉིད་དོ། །ཇི་ལྟར་ཆོས་སུ་གྱུར་པ་ཡིན་ཞེ་ན། སྨྲས་པ། དེ་ཆོས་ཐམས་ཅད་ཀྱི་རྩ་བ་ཡིན་པའི༌[^561]ཕྱིར་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཆོས་ནི་མདོའི་སྡེ་དང་། དབྱངས་ཀྱིས་བསྙད་པ་དང་། ལུང་བསྟན་པ་དང་། ཚིགས་སུ་བཅད་པ་དང་། ཆེད་དུ་བརྗོད་པ་དང་། གླེང་གཞི་དང་། རྟོགས་པ་བརྗོད་པ་དང་། དེ་ལྟ་བུ་བྱུང་བ་དང་། སྐྱེས་པའི་རབས་དང་། ཤིན་ཏུ་རྒྱས་པ་དང་། ཆོས་རྨད་དུ་བྱུང་བ་དང་། གཏན་ལ་ཕབ་པ་ཞེས་བྱ་བ་སྟེ། གསུང་རབ་ཡན་ལག་བཅུ་གཉིས་སུ་གཏོགས་པའི་ཆོས་དེ་རྣམས་ནི་ཆོས་ཐམས་ཅད་ཀྱི་རྩ་བ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་བཅོམ་ལྡན་འདས་ཀྱིས་དང་པོར་བསྟན་པ་ཡིན་པའི་ཕྱིར་རྩ་བ་ཉིད་ཡིན་ནོ། །

[Block 752]
དེ་འདྲེན་པ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ལ། ཆོས་དེ་དག་རྣམས་དེས་འདྲེན་པ་ཡིན་ཏེ། དེ་འདྲེན་པ་ཡིན་པ་ནི། དེ་འདྲེན་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 753]
དེས་ན་གང་གི་ཕྱིར་བཅོམ་ལྡན་འདས་ཁོ་ན་ཆོས་དེ་འདྲེན་པ་ཡིན་པ་དེའི་ཕྱིར། བཅོམ་ལྡན་འདས་ནི་ཆོས་སུ་གྱུར་པའོ། །

[Block 754]
འོན་ཀྱང་སྟོན་པ༌[^562]ཉིད་ཀྱིས་སྟོན་པ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་སྟེ། དེ་ཉིད་སྟོན་པ་ཡིན་པས་ན་སྟོན་པ་ཡིན་པ་སྟེ། ཆོས་གང་རྣམས་དེའི་ཆོས༌[^563]ཡིན་པ་དེ་ལ་སྟོན་པ་ཡིན་པའོ། །

[Block 755]
དེ་བས་ན་དེའི་ངོ་བོ་ནི་སྟོན་པ་ཡིན་པ་ཉིད་དོ། །

[Block 756]
རྒྱུ་འདིས་ཀྱང་བཅོམ་ལྡན་འདས་ནི་ཆོས་སུ་གྱུར་པ་ཡིན་ཏེ། དེའི་ཕྱིར་ལྷ་དང་མི་རྣམས་ཀྱི་སྟོན་པ་ཞེས་བརྗོད་དོ། །

[Block 757]
ཚོགས་མཐའ་དག་རྣམ་པ་ཐམས་ཅད་དུ་མངོན་པར་རྫོགས་པར་ཐུགས་སུ་ཆུད་པ་ཞེས་བྱ་བ་ལ། མཐའ་དག་ནི་ཆོས་ཀྱི༌[^564]ཕུང་པོ་རྣམ་པ་གསུམ་མོ། །

[Block 758]
རྣམ་པ་ཐམས་ཅད་ནི་དགེ་བ་དང་མི་དགེ་བ་ལ་སོགས་པའི་རྣམ་པའོ། །

[Block 759]
དེ་དག་རྣམ་པ་ཉིད་ཀྱིས༌[^565]ཐུགས་སུ་ཆུད་པ་སྟེ། མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཞེས་བྱ་བའོ། །

[Block 760]
བདུད་དཔུང་དང་བཅས་པ་ཐམས་ཅད་ཀྱི་གཡུལ་ཆེན་པོ་བཅོམ་པས་ན་བཅོམ་ལྡན་འདས་ཏེ། བཅོམ་ལྡན་འདས་ཉག་གཅིག་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་དུ་འབྱུང༌[^566]ཞེས་བྱ་བ་ནི། སྡེ་པ་གཞན་ཁ་ཅིག་གི༌[^567]འདོད་པའོ། །

[Block 761]
དེའི་ལན་དུ་བརྩམས་པ་ནི། དེ་ལ་བསྐལ་པ་དུ་མར་ཡང་སངས་རྒྱས་གཅིག་ཀྱང་མི་འབྱུང་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 762]
རང་བཞིན་གྱིས་ཉོན་མོངས་པ་མེད་པའི་རྒྱུད་དང་། ཤེས་རབ་འཆལ་པའི་རྒྱུད་ཀྱིས༌[^568]ཀྱང་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་མི་ནུས་ཞེས་བྱ་བ་ནི། ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པས་ཟིལ་གྱིས་མནན་པའི་ཕྱིར་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ཀྱིས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 763]
ངོ་བོ་ཉིད་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། བྱང་ཆུབ་ཀྱི་ལེའུའི༌[^569]བསྡུས་པའི་དོན་དང་གོ་རིམ་དག་ནི་འདི་ཉིད་དུ་ཉེ་བར་བསྟན་ཟིན་པའི་ཕྱིར། ཡང་ཉེ་བར་བསྟན་པར་བྱ་བ་མ་ཡིན་པས་དེས་ན་མ་བྲིས་སོ། །

[Block 764]
བྱང་ཆུབ་སེམས་དཔའ༌[^570]སའི་གཞིའི་རྣལ་འབྱོར་གྱི་གནས་ལས་བྱང་ཆུབ་སེམས་དཔའི་རིམ༌[^571]པར་ཕྱེ་བ་སྟེ་བདུན་པ་རྫོགས་སོ།། །།

[Block 765 [HEADING]]
## རིགས་རྣམ་པར་ཕྱེ་བ། ^3-0

[Block 766]
སྡོམ་ནི།

[Block 767 [VERSE]]
མོས་པ་མང་པོ༌[^572]ཉིད་དང་ནི། །
ཆོས་ཚོལ་བ་དང་སྟོན་པ་དང་། །
སྒྲུབ་པ་དང་ནི་དེ་བཞིན་དུ། །
ལེགས་པར་གདམས་ངག་རྗེས་བསྟན་དང་། །

[Block 768 [VERSE]]
ལུས་དང་ངག་དང་ཡིད་ཀྱི༌[^573]ལས། །
ཐབས་དང་བཅས་པ་ཕྱི་མ་ཡིན། །

[Block 769]
ཞེས་བྱ་བ་ནི། ཇི་ལྟར་བསླབ་པའི་དབང་དུ་བྱས་པ་ཡིན་ལ། བྱང་ཆུབ་སེམས་དཔའ༌[^574]གང་ལ་བསླབ་པར་བྱ་བ་ནི་སྔར་བསྟན་ཟིན་ཏོ། །

[Block 770]
བསྡུས་པའི་དོན་སྟོན་པ་བདུན་པོ་འདི་དག་གི་བསྡུས་པའི་དོན་ནི། བདག་ཉིད་ཇི་ལྟར་སློབ་པ་དང་། གཞན་དག་ལ་ཡང་ཞེས་བྱ་བ་ནི་བསྡུས་པའི་དོན་ཏོ། །

[Block 771]
དེ་ལ་བདག་ཉིད་སློབ་པར་བྱེད་པ་ནི། བྱང་ཆུབ་སེམས་དཔའ་ཆོས་ཀྱིས༌[^575]རྗེས་སུ་འབྲང་བ་དང་། དད་པས་རྗེས་སུ་འབྲང་བའོ། །

[Block 772]
དེ་ལ་ཆོས་ཀྱིས༌[^576]རྗེས་སུ་འབྲང་བ་ནི་རྣམ་པ་གསུམ་དུ་སློབ་སྟེ། མོས་པ་མང་པོ༌[^577]ཉིད་ཀྱི་བསམ་པའི་རྒྱུན་ཉིད་དང་། སྦྱོར་བ་ཉིད་དང་།[^578] ཆོས་ཚོལ་བ་ལ་སྦྱོར་བ་ཉིད་ལའོ། །

[Block 773]
དད་པས་རྗེས་སུ་འབྲང་བ་ནི་རྣམ་པ་བཞི་སྟེ། བདག་ཉིད་ཀྱིས་བསླབ་པའི་སྔར་ཆོས་ཀྱིས༌[^579]རྗེས་སུ་འབྲང་བ་ལ་བསྟན་པའི་བསླབ་པ་རྣམ་པ་གསུམ་དང་།

[Block 774]
བཞི་པ་གདམས་ངག་རྗེས་སུ་བསྟན་པ་འཛིན་པའོ། །

[Block 775]
གཞན་བསླབ་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། གཞན་རྣམ་པ་གཉིས་ནི་ཞུགས་པ་དང་མ་ཞུགས་པ་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
