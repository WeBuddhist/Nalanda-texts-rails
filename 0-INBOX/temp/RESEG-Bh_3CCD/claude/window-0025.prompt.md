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
དེ་ལྟར་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ཐོབ་པའི་རྣལ་འབྱོར་པ་ལ་རྒྱུ་དང་འབྲས་བུའི་བྱེ་བྲག་ཏུ་གནས་པའི་དངོས་པོ་ཐམས་ཅད་ངོ་བོ་གཅིག་ཁོ་ན་ཡིན་གྱི་བྱེ་བྲག་ཏུ་དེ་ལ་དེ་རྣམས་སྣང་བ་མ་ཡིན་ནོ། །

[Block 877]
བདག་ཅག་ལྟ་བུ་གཞལ་བར་བྱེད་པ་རྣམས་ཀྱིས་དེ་ལྟར་འདོད་པ་ལ་སྐྱོན་མེད་དོ། །

[Block 878]
ཡང་ན་སྲིད་པ་དང་མྱ་ངན་ལས་འདས་པའི་རྣམ་པར་རྟོག་པ༌[^603]ཕན་ཚུན་བྱེ་བྲག་ཏུ་རབ་ཏུ་འཇུག་པ་དེ་རྣམས་ཁོ་ན་རོ་གཅིག་པར་ཤེས་པས་ཏིང་ངེ་འཛིན་མངོན་དུ་འགྱུར་ཞེས༌[^604]རྒྱུ་དང་འབྲས་བུའི་བྱེ་བྲག་འདི་ནི་བརྟགས་པ་ཡིན་པས་གནོད་པ་གང་ཡང་མེད་དོ། །

[Block 879]
དེ་ལྟ་ན་གལ་ཏེ་ཏིང་ངེ་འཛིན་འདི་ཡིན་ན། ཇི་ལྟར་ལྡང་བར་འགྱུར་ཏེ། ལྡང་བ་མེད་ན་དེའི་ཚེ་སེམས་ཅན་གྱི་དོན་མེད་ཅེས་ཕན་ཚུན་འགལ་བ་ཐོབ་པར་འགྱུར་ཞེ་ན། སྨྲས་པ་ལྡང་བ་ཞེས་བྱ་བ་ནི་ཏིང་ངེ་འཛིན་ཉམས་པར་བྱེད་པ་ནི༌[^605]མ་ཡིན་ཏེ། འོན་ཀྱང་ཏིང་ངེ་འཛིན་ལ་ཞུགས་པ་ཉིད་ཀྱིས་འགྲོ་བའི་དོན་མཛད་པའོ། །

[Block 880]
གང་གི་ཕྱིར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས༌[^606]ཀྱི་སྤྱོད་ལམ་རྣམ་པ་བཞི་སྟེ། སྤྱོད་ལམ་གྱི་བཞུགས་པ་དང་། བསྟན་པའི་བཞུགས་པ་དང་། ཏིང་ངེ་འཛིན་གྱི་བཞུགས་པ་དང་། སོ་སོར་ཡང་དག་པའི་འཇུག་པའི་བཞུགས་པའོ། །

[Block 881]
དེ་ལ་སངས་རྒྱས་རྣམས་ཀྱི་སྐུའི་ཕྲིན་ལས་རྟག་ཏུ་མཉམ་པར་གཞག་པ༌[^607]གང་ཡིན་པ་དེ་ནི་སྤྱོད་ལམ་གྱི་བཞུགས་པའོ། །

[Block 882]
གང་གསུང་གི་ཕྲིན་ལས་རྟག་ཏུ་མཉམ་པར་གཞག་པ༌[^608]གང་ཡིན་པ་དེ་ནི་བསྟན་པའི་བཞུགས་པའོ། །

[Block 883]
གང་ཐུགས་ཀྱི་ཕྲིན་ལས་རྟག་ཏུ་མཉམ་པར་གཞག་པ༌[^609]གང་ཡིན་པ་དེ་ནི་ཏིང་ངེ་འཛིན་གྱི་བཞུགས་པའོ། །

[Block 884]
གང་སངས་རྒྱས་རྣམས་ཀྱིས་མཐོང་བའི་ཆོས་ཀྱི་བདེ་བའི་བཞུགས་པ་དང་། ལྷ་ལ་སོགས་པའི་གནས་སུ་ཉེ་བར་གཤེགས་པ་ལ་ཐུགས་ཀྱི་ཕྲིན་ལས་རྟག་ཏུ་མཉམ་པར་གཞག་པ་གང་ཡིན་པ་དེ་ནི་སོ་སོར་ཡང་དག་པར་འཇུག་པའི་བཞུགས་པའོ། །

[Block 885]
མཉམ་པར་གཞག་པའི༌[^610]སྤྱོད་པ་ནི་བཞུགས་པ་སྟེ་གང་གི་ཕྱིར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྟག་ཏུ་མཉམ་པར་གཞག་པས༌[^611]སོ། །

[Block 886]
དེ་ལྟར་ཟུང་དུ་འཇུག་པའི་རིམ་པ་ལ་གནས་པའི་རྣལ་འབྱོར་པའི་ཏིང་ངེ་འཛིན་ལས་ལྡང་ཡང་རུང་མི་ལྡང་ཡང་རུང་ཁྱད་པར་གང་ཡང་མེད་དེ་ཞེས་ཏིང་ངེ་འཛིན་ཁོ་ན་ཡིན་ཏེ། ཏིང་ངེ་འཛིན་མ་ཡིན་པ་ལས་ལོག་པའི་ཕྱིར་རོ། །

[Block 887]
གལ་ཏེ་ཕྱོགས་གཉིས་ཀ་ལ་མཚུངས་པ་ཡིན་ན་དེ་ཅིའི་ཕྱིར་རྣམ་པར་མི་རྟོག་པར་གྱུར་ནས་ཀྱང་སེམས་ཅན་གྱི་དོན་བྱེད་ཅེ་ན། སྨྲས་པ་སྔོན་གྱི་སྨོན་ལམ་དང་ཐུགས་རྗེ་ཆེན་པོའི་ཤུགས་ཀྱིས་སེམས་ཅན་གྱི་དོན་མཛད་པ་ཡིན་གྱི་རྣམ་པར་རྟོག་པས་ནི་མ་ཡིན་ནོ། །

[Block 888]
སེམས་ཅན་རྣམས་ཀྱི་ཡང་དེ་ཕྲད་པ་ཙམ་གྱིས་རེ་བ་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་འགྱུར་ཏེ་ཡིད་བཞིན་གྱི་ནོར་བུ་དང་བུམ་པ་བཟང་པོ་བཞིན་ནོ། །

[Block 889]
ཇི་སྐད་དུ།

[Block 890 [VERSE]]
དེ་ནི་ཕྲད་པ་ཙམ་གྱིས་ནི། །
སྐྱེས་བུ་ཡིད་བཞིན་ནོར་བུ་ལྟར། །
རྩིག་པ་ལ་སོགས་རྣམས་ལས་ཀྱང་། །
ཇི་འདོད་བསྟན་པ་རྣམས་ནི་འབྱུང་། །

[Block 891]
ཞེས་འབྱུང་ངོ་། །

[Block 892]
དེ་བས་ན་སངས་རྒྱས་ཀྱི་ས་ལ་ཉོན་མོངས་པའི་དྲ་བ་ཟད་ནས་ཀྱང་སྔོན་གྱི་སྨོན་ལམ་གྱི་འཕེན་པའི་དབང་གིས་སྐུར་བྱུང་བ་དང་སེམས་ཅན་གྱི་དོན་ཡང་འབྱུང་སྟེ། རྫ་མཁན་གྱི་འཁོར་ལོ་བཞིན་ནོ། །

[Block 893]
ཇི་སྐད་དུ། སྐྱོན་རྣམས༌[^612]སྐྱེད་བྱེད་འཇིག་ཚོགས་ལྟ་བུའི་བུད་ཤིང་སྲེག་བྱེད་གང་། །རང་གཞན་བྱེ་བྲག༌[^613]ཡུལ་རྣམས་རྩ་ནས་འདོན་བྱེད་དེ་རྣམས་སྐྱོན་མེད་དེ། །སྐྱོན་མེད་པ་ཡང་ཐུགས་རྗེས་སྒྱུ་མའི་སྐྱེས་བུ་ལས་ལ་འཇུག །བློ་བཟང་སྔོན་གྱི་སྨོན་ལམ་དབང་གིས་འཁོར་ལོ་འཁོར་བཞིན་གནས། །ཞེས་འབྱུང་ངོ་། །ཀམ་པ་ལའི་ཞལ༌[^614]སྔ་ནས་ཀྱིས་ཀྱང་གསུངས་ཏེ།

[Block 894 [VERSE]]
མི་ཤིགས༌[^615]ཁྱོད་ཀྱིས་མངོན་པར་བྱང་ཆུབ་ཐོབ་ནས་ནི། །
གང་ཚེ་མི་ཤིགས༌[^616]ཉིད་ཀྱང་ཡི་གེར་གསུངས་པ་ནི། །
དེ་ཚེ་རིང་དུ་ཉམས་པ་རྣམས་ཀྱི་ཇི་ལྟར་ནི། །
ལྕགས་ཀྱུ་མེད་པ་རྣམས་ཀྱིས་ལོག༌[^617]པའི་རྩོལ་བ་བྱེད། །

[Block 895]
ཅེས་འབྱུང་ངོ་། །ཟུང་དུ་འཇུག་པའི་རིམ་པའི་ཏིང་ངེ་འཛིན་ཏེ་རྫོགས་པའི་རིམ་པའོ། །

[Block 896]
[^618]

[Block 897]
དེ་ལྟར་བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པ་དག་ཡན་ལག་དང་དབྱེ་བར་བཅས་པ་ནི་རབ་ཏུ་བསྟན་ཏོ། །

[Block 898]
འགྲེལ་པ་མ་ལུས་པའི་དོན་དེ་ཉིད་ལ་བརྟེན་ཏེ་སློབ་དཔོན་ཟླ་བ་གྲགས་པས་འགྲེལ་པ་ལས་དོན་བསྟན་ཏོ།[^619] །

[Block 899]
དེ་བརྩམ་པ༌[^620]ལ་དང་པོ་རྣམ་པ་གསུམ་ཡིན་ཏེ། བྱ་བ་དང་བྱ་བའི་འབྲས་བུ་དང་། བྱ་བའི་འབྲས་བུའི་འབྲས་བུའོ། །

[Block 900]
དེ་ལ་རྡོ་རྗེ་ཕྲེང་བ་དང་། ལྷ་མོ་བཞིས་ཡོངས་སུ་ཞུས་པ་དང་། དགོངས་པ་ལུང་བསྟན་པ་དང་། ཡེ་ཤེས་རྡོ་རྗེ་ཀུན་ལས་བཏུས་པ་རྣལ་འབྱོར་གྱི་རྒྱུད་ཆེན་པོའི་བཤད་པའི་རྒྱུད་བཞི་པོ་ལས་ཡང་དག་པར་བཏུས་ཏེ། དཔལ་གསང་བ་འདུས་པའི་འགྲེལ་པ༌[^621]བྱེད་པ་གང་ཡིན་པ་དེ་བྱའོ། །

[Block 901]
བཤད་པའི་རྒྱུད་རྒྱས་པ་རྣམས་ལས་བློ་དམན་པ་རྣམས་ཀྱིས་དོན་གཟུང་བར༌[^622]མི་ནུས་ཏེ། དེ་རྣམས་ཀྱིས༌[^623]བདེ་བླག་ཏུ་གོ་བ་ནི་བྱ་བའི་འབྲས་བུའོ། །

[Block 902]
བདེ་བླག་ཏུ༌[^624]གོ་བས་ཕན་ཚུན་སློབ་དཔོན་དང་སློབ་མ་དག་གི༌[^625]འཆད་པ་པོ་དང་ཉན་པ་པོའི་འབྲེལ་པ་དང་བསྙེན་བཀུར་བྱེད་པ་དང་། བསྙེན་བཀུར་བྱ་བ་དང་། ཐོས་པ་དང་བསམ་པ་དང་བསྒོམ་པས༌[^626]རྟོགས་པས་ཟབ་ཅིང་རྒྱ་ཆེ་བ་བླ་ན་མེད་པས་སེམས་ཅན་མ་ལུས་པ་ལ་རྗེས་སུ་གཟུང་བར་བྱེད་པ་དཔལ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གོ་འཕང་ཐོབ་པ་ནི་བྱ་བའི་འབྲས་བུའི་འབྲས་བུའོ། །

[Block 903]
དེ་ཡོད་པས་ཉན་པ་པོ་འཇུག་པར་འགྱུར་རོ། །

[Block 904 [HEADING]]
### བརྗོད་པ་ལ་སོགས་པ་རྣམ་པ་ལྔ། ^1-3-0

[Block 905]
དེ་བཞིན་དུ་གཞན་ཡང་བརྗོད་པ་ལ་སོགས་པ་རྣམ་པ་ལྔ་པོ་ཉན་པ་པོ་འཇུག་པར་བྱ་བའི་ཕྱིར་སྨྲ་བར་བྱ་སྟེ། རྗོད་པ་དང་བརྗོད་པར་བྱ་བ་དང་། འབྲེལ་པ་དང་། དགོས་པ་དང་། དགོས་པའི་དགོས་པའོ། །

[Block 906 [HEADING]]
#### རྗོད་པ། ^1-3-1-0

[Block 907]
དེ་ལ་རྗོད་པར་བྱེད་པ་འགྲེལ་པའི་མིང་ནི་སྒྲོན་མ་རབ་ཏུ་གསལ་བར་བྱེད་པའོ། །

[Block 908]
དཔལ་གསང་བ་འདུས་པའི་རྣལ་འབྱོར་གྱི་རྒྱུད་ཆེན་པོ་ཐོས་པ་ཆུང་བའི་སློབ་དཔོན་གྱིས་བཤད་པའི་མུན་པས་ཁེབས་པའི་རྡོ་རྗེའི་ཚིག་རྣམས་སྒྲོན་མ་ལྟར་གསལ་བར་བྱེད་ཅིང་ཇི་ལྟ་བ་བཞིན་དུ་མངོན་པར་གསལ་བར་བྱེད་པས་ན༌[^627]སྒྲོན་མ་གསལ་བའོ། །

[Block 909]
མཐའ་དྲུག་ཅེས་བྱ་བ་ནི༌[^628]དེ་ཉིད་ཀྱི་དོན་གྱི་སྒོ་ནས་མིང༌[^629]ཡིན་ཏེ། བརྗོད་པར་བྱ་བ་དྲུག་དུ་བསྟན་པའི་ཕྱིར་རྗོད་པར་བྱེད་པའོ། །

[Block 910 [HEADING]]
#### བརྗོད་པར་བྱ་བ། ^1-3-2-0

[Block 911]
བརྗོད་པར་བྱ་བ་ནི་སྔོན་དུ་བཤད་པའི་རིམ་པ་གཉིས་ཏེ། དེ་ལ་ཡང་དང་པོ་ལ་རྣམ་པ་གསུམ་སྟེ། ལུས་རྣམ་པར་དབེན་པའི་བར་དུའོ། །

[Block 912]
གཉིས་པ་ནི་རྣམ་པ་ལྔ་སྟེ་ངག་རྣམ་པར་དབེན་པ་ནས་བརྩམས་ཏེ་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་བར་དུའོ་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 913 [HEADING]]
#### འབྲེལ་པ། ^1-3-3-0

[Block 914]
འབྲེལ་པ་ཞེས་བྱ་བ་ནི་སྒྲ་དང་དོན་དག་གིས༌[^630]ཐབས་དང་ཐབས་ལས་བྱུང་བའི་མཚན་ཉིད་དམ། རྒྱུ་དང་འབྲས་བུའི་ཚུལ་ལམ། རྗོད་པ་དང་བརྗོད་པར་བྱ་བའི་མཚན་ཉིད་ངེས་པར་ཤེས༌[^631]པར་བྱའོ། །

[Block 915]
གལ་ཏེ་སྒྲ་དང་དོན༌[^632]དག་གིས་འབྲེལ་པ་གཙོ་བོ་ཡོད་པ་མ་ཡིན་ཡང་བློས་བྱས་པ་ཁོ་ནའོ། །
--- END BLOCKS ---
