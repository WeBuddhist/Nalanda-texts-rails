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
སྤྱོད་མཆོག་བསྟོད་པའི་གཞི་ཞེས་བསྟན་པའི་སྤྱོད་པའི༌[^410]མཆོག་གི་གཞི་དེ་ཉིད་ཀྱི་དབང་དུ་བྱས་ནས་སྨྲས་པ།

[Block 737 [VERSE]]
ཀྱེ་མའོ་རླབས་ཆེན་ཞེས་བྱ་བ་ནས། །
ཁྱོད་ཀྱིས་འགྲོ་བ་མགོན་བཅས་བགྱིས་པ་ལེགས། །

[Block 738]
ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། ཀྱེ་མའོ་རླབས་ཆེན་ཞེས་བྱ་བའི་བསྡུས་པའི་དོན་ནི་འདི་ཡིན་ཏེ། སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པས༌[^411]བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 739]
དང་པོའི་གཉིས་པོ་སྟེ། ཀྱེ་མའོ་རླབས་ཆེན་ཞེས་བྱ་བ་འདིས་ནི་སྦྱིན་པའི་དབང་པོ༌[^412]ལ་ཆགས་པ་མེད་པར་བསྟན་ཏོ། །

[Block 740]
ཨེ་མའོ་སྙིང་རྗེ་ཅན་ཞེས་བྱ་བ་འདིས་ནི་རབ་ཏུ་འཛིན་པར་བྱེད་པའི་སྙིང་རྗེ་དང་ལྡན་པ་སྟེ།

[Block 741 [VERSE]]
འདི་གཉིས་ཀྱི་ཕྱིར་སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པའོ། །
འདི་ཡི་སེམས་ནི་ཇི་ལྟར་རྣམ་དག་ལྟོས། །

[Block 742]
ཞེས་བྱ་བ་འདིས་ནི་འབྲས་བུ་ཡོངས་སུ་འགྱུར་བའོ། །

[Block 743]
ཨེ་མའོ་བདག་གི་བདེ་ལ་སེམས་མ་ཆགས། །ཞེས་བྱ་བ་འདིས་ནི་བདག་ལ་ཆགས་པ་མེད་པ་ཡིན་ཏེ། གཉིས་ཀས་ཀྱང་བསམ་པ་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའོ། །

[Block 744]
དེས་ན་དེ་ཉིད་བརྟན་ཞིང་དཔའ༌[^413]མཆོག་ཅེས་བྱ་བ་ཡིན་ཏེ། བརྟན་པ་ནི་བརྟན་པའི་བསམ་པ་སྟེ་སེམས་རྣམ་པར་དག་པ་དང་། བདག་ཉིད་གྱི་བདེ་བ་ལ་མ་ཆགས་པར་དེས་བསྟན་ཏེ། །[^414]དང་པོའི་གཉིས་པོ་འདིས་ནི་དཔའ་བ་སྟེ། སྦྱོར་བ་ཕུན་སུམ་ཚོགས་པ་དེས་སོ། །

[Block 745]
དེ་ལྟར་དང་པོའི་ཚིགས་བཅད་ཀྱིས་མིག་སྦྱིན་པའི་སྤྱོད་པ་གཞི་ལས་བསྟོད་པའི་དབང་དུ་བྱས་པའོ། །

[Block 746]
པདྨའི་སྤྱན་རྒྱས་ཞེས་བྱ་བ་ལ་སོགས་པ་འདིས་ནི་མིག་རྙེད་པའི་སྒོ་ནས་བསྟོད་པ་ཡིན་ཏེ། མགོན་དང་བཅས་པས་སོ། །

[Block 747]
བསོད་ནམས་ཚོགས་ནི་དོན་ཡོད་པ། །ཞེས་བྱ་བ་འདིས་ནི་དོན་གྱིས་ཏེ། བརྒྱ་བྱིན་གྱི་མཆོག་ལ་ལྟོས་པ༌[^415]མེད་པར་བདེན་པའི་བྱིན་གྱིས༌[^416]རླབས་ཀྱིས་རང་གི་མིག་སླར་རྙེད་པའོ། །

[Block 748]
བྱིན་གྱིས་ཞེས་བྱ་བ་ནི་བདེན་པའི་བྱིན་གྱིས་རླབས་ཀྱིས་སོ། །

[Block 749]
རྒྱལ་བ་ནི་བརྒྱ་བྱིན་མཆོག་ལ་མ་ལྟོས་པར༌[^417]རང་གི་མིག་སླར་རྙེད་པའོ། །

[Block 750]
བསམ་པ་དག་པ་ནི་དེ་ཚེ་དང་ནི་ད་ལྟར་སློང་རྣམས་ཀྱི་ཞེས་བྱ་བ་དང་། གང་ཡང་བདག་ལ་ཡ་གཅིག་མིག༌[^418]བསླངས་ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་བསྟན་པ་དེའི་དབང་དུ་བྱས་པའོ། །

[Block 751]
དེ་ལྟར་ཞེས་བྱ་བ་ནི་སློང་བ་རྣམས་ཀྱིས་འདི་ལྟའི་གནས་སྐབས་ཞེས༌[^419]གང་བཤད་པའི་ཚིགས་བཅད་དེས་བསྟན་ཏོ། །

[Block 752 [VERSE]]
དཔག་ཚད་བརྒྱ་ནི་ཁོར་ཡུག༌[^420]ཏུ། །
ཞེས་བྱ་བ་ནི་རིང་དུ་བསྟན་པའོ། །
བྲག་རི་རྣམས་ཀྱིས༌[^421]བར་བཅད་ཀྱང་། །

[Block 753]
ཞེས་བྱ་བ་ནི་སྒྲིབ་གཡོགས་བསྟན་ཏོ། །

[Block 754]
དེ་གཉི་ག་མཐོང་བ་ནི་ལྷའི་མིག་གི་མཚན་ཉིད་ཡིན་ནོ། །

[Block 755]
བྲག་རི་རྣམས་ཀྱིས་བར་བཅད་ཀྱང་། །ཞེས་བྱ་བས་ནི་བར་དུ་གཅོད་པ་གཞན་བསྟན་པ་ཡང་རབ་ཏུ་འགྲུབ༌[^422]བོ། །

[Block 756]
ཡ་མཚན་ཆེ་ཞིང་སེམས་རབ་ཏུ་དགའ་བར་འགྱུར་བའི་མིག་གིས་ཞེས་བྱ་བ་ལ། ཡ་མཚན་ཆེ་བ་ནི་མིག་ཉམས་པ་ལས་ཡང་བསྐྱེད་པའོ། །

[Block 757]
སེམས་རབ་ཏུ་དགའ་བར་གྱུར་པས་ནི་དེས་ན་མགོན་དང་བཅས་པར་བྱས་པས་སོ། །

[Block 758]
རབ་ཏུ་སྦྱིན་པའི་བསོད་ནམས་ལས་གྱུར་པའི། །ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གསུམ་གྱིས་ནི་སྦྱིན་པ་རབ་ཏུ་བསྒྲུབས་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 759]
ཤི་བི་པ་རྣམས་དེ་ལྟར་རིག་བྱས༌[^423]ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་འདིས་ནི་ཡང་དག་པར་འཛིན་དུ་གཞུག་པའོ། །

[Block 760]
འཇིག་རྟེན་ཕན་ཕྱིར་སྦྱིན་པ་གང་བྱིན་པ། །[^424]ཞེས་བྱ་བའི་ཚིགས་བཅད་དེ༌[^425]འདིས་ནི་ཤི་བི་པ་རྣམས་དེ་ལྟར་རིག་བྱས་ནས་ཞེས་བྱ་བའི་ཚིག༌[^426]དེ་ཉིད་སྒྲུབ་པ་སྟེ། ཕྱི་རོལ་གྱི་ནོར་གྱི་སྦྱིན་པ་གྱིས་ཤིག་ཅེས་བྱ་བར་བཤད་པར་བྱའོ།[^427] །ལྷའི་མཐུ་ལྡན་ཞེས་བྱ་བ་ནི་ལྷའི་མཐུ་བཞིན་དུ་གང་གིས་ནུས་པས་མིག་གཉིས་ཀྱིས་མཐོང་བ་དེ་ནི་མིག་གིས་མཐོང་བས་དེ༌[^428]ལྷའི་མཐུའོ། །

[Block 761]
རབ་ཏུ་སྦྱིན་པའི་བསོད་ནམས་ལས་གྱུར་པ། །ཞེས་བྱ་བ་ནི་མིག་རབ་ཏུ་སྦྱིན་པའི་བསོད་ནམས་ལས་གྱུར་པ་སྟེ། ལྷའི་མཐུ་ལྡན་ཞེས་བསྟན་པ་དེའོ། །

[Block 762]
ལྷའི་མཐུ་ལྡན་ཞེས་བྱ་བ་དེ་ཉིད་བསྟན་པའི་ཕྱིར། །དཔག་ཚད་བརྒྱ་ནི་ཚུན་ཆད་དུ། །ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་ཡིན་ནོ། །

[Block 763 [VERSE]]
ཤིན་ཏུ་རིང་ན་གནས་པ་ཡང་། །
བལྟ་བར་བྱ་བ་གསལ་བར་མཐོང་། །

[Block 764]
ཞེས་བྱ་བ་ནི་ཉེ་བར་གནས་པ་བཞིན་དུ་རྣམ་པར་གསལ་བ་ཡིན་པའི་ཕྱིར་ཉེ་བར་གནས་པ་བཞིན་དུ་གསལ་བར་མཐོང་བའོ། །

[Block 765]
བལྟ་བར་བྱ་བ་ཞེས་བྱ་བ་ནི་ཕྱོགས་ཀུན་ཏུ་སྟེ། འོག་དང་སྟེང་དུ་ཡང་མངོན་སུམ་དུ་དམིགས་སོ། །

[Block 766]
སྦྱིན་པའི་མཐོང་བའི་ཆོས་ཀྱི་འབྲས་བུ་བསྟན་པ་དང་། ཕ་རོལ་ཏུ་མངོན་པར་མཐོ་བ་རབ་ཏུ་བསྒྲུབ་པའི་ཕྱིར། གང་ཕྱིར་མི་ཡི་མིག་ནི་ཞེས་བྱ་བའི་ཚིགས་བཅད་བསྟན་ཏེ། [^429]གཞན་དག་ལ་བརྩེ་བ་ནི་གཞན་དག་ལ་སྙིང་བརྩེ་བ་སྟེ་སྙིང་རྗེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 767]
འདིས་ནི་བཟོད་པ་བསྟན་ཏོ། །

[Block 768]
གཞན་ལ་བརྩེ་བ་དང་དུལ་བའི་ཚུལ་ནི་གཞན་ལ་བརྩེ་ཞིང་དུལ་བའོ། །

[Block 769]
དེ་ལས་སྐྱེས་པ་ནི་གཞན་ལ་བརྩེ་ཞིང་དུལ་བ་ལས་བྱུང་བའོ། །

[Block 770]
དེ་བས་ན་མངོན་པར་མཐོ་བ་སྦྱིན་པའི་འབྲས་བུ་སྟེ་ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པའོ། །

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
--- END BLOCKS ---
