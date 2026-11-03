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
[Block 1051]
དེའི་ཚེ་འབྲེལ་པར༌[^628]མི་འགྱུར་བར་བྱ་བའི་ཕྱིར་ཅིག་ཅར་ཉིད་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བཀྲུ་བཤལ་བྱ་བ་དང་བསྐམ་པའི་དུས་དེ་ལ་བྲེལ་པར་མ་གྱུར་ཅིག་ཅེས་བྱ་བ་འདིའི་དོན་ཅིག་ཅར་ཉིད་དུ་འདི་བཀྲུ་བ་དང་བསྐམ་པར་མི་བྱའོ། །

[Block 1052]
སྣོད་རྣམས་ཀུན་ལ་དུས་གཅིག་ཏུ་མ་ཡིན་ནོ། །

[Block 1053]
ཆུ་དང་འབྲེལ་པའི་ལས་ནི་གནས་པས་བྱ་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདི་རྣམས་ལ་བརྩམ་པ་དང་གཞན་ལ་བརྗོད་པའོ། །

[Block 1054]
འདིར་གཞུང་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཆུ་བླང་བར་བྱའོ་ཞེས་གསུངས་པ་དང་། དགེ་སློང་གིས་སུས་བླང་བར་བྱ་མི་ཤེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གནས་པ་དག་གིས་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1055]
ཆུ་ཁང་གི་འཁོར་དུ་གཏོགས་པ་དང་ཆུ་ཚགས་ཀྱི་བྱ་བ་ཡང་འདི་རྣམས་ཉིད་ལ་རིགས་པ་ཡིན་གྱི་གཞན་དུ་ན་ཡང་ཞེས་བྱ་བ་འདི་བསྟན་པ་ཡིན་ནོ། །

[Block 1056]
སྲོག་ཆགས་དང་བཅས་པའི་ཆུ་དང་འབྲེལ་པ་ཕྲན་ཚེགས་ལ་སོགས་པའི་སྐབས་སོ།། །།

[Block 1057]
ཤེས་གཙོ་བོ༌[^629]ཞེས་བྱ་བ་ནི་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཉིད་དོ། །གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཞུགས་པ་འམ་ཕྱོགས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1058]
ཅི་ཞིག་ལ་ཞུགས་པའམ་ཕྱོགས་པ་ལ་ཞེ་ན་དེའི་སྤྱོད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཉིས་ཀྱིས་གཉིས་སྤྱོད་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1059]
གང་གི་སྤྱོད་པ་ལ་ཞེ་ན་དེའི་ཕྱིར་སྐྱེས་པ་དང་བུད་མེད་ཀྱིའོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཅི་གནས་སྐབས་འདི་ཐམས་ཅད་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་སྐྱེས་པ་དང་བུད་མེད་གཉིས་ཁྱིམ་པ་ཉིད་ཡིན་ནའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1060]
ཡང་དག་པར་སྦྱོར་བ་གཅིག་ལ་ཡང་ཁྱིམ་པ་ཉིད་མ་ཡིན་པ་ལ་མ་ཆོག་པའི་ཁ་ན་མ་ཐོ་བ་བསྐྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅི་དེ་གཉིས་གནས་གང་ན་འདུག་ཀྱང་རུང་ངམ་ཞེ་ན། དེའི་ཕྱིར་གནས་གཞན་ཉིད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལྟུང་བ་ལས་གཞན་གང་ཡིན་པ་དེའི་གནས་གང་ཞིག༌[^630]དེ་དང་འབྲེལ་པ་ཉིད་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1061]
གནོད་པར་གྱུར་པ་ལས་གཞན་མ༌[^631]ཡིན་གྱི་རང་གི་གནས་ཉིད་དུ་ནི་ཉེས་པ་འདི་མི་བསྐྱེད་ཅེས་བྱ་བ་འདི་ཤེས་པར་བྱའོ། །

[Block 1062]
གང་ཞིག་དགེ་སློང་གིས་ཁྱིམ་པ་ལ་གཡར་པོར་བྱིན་ཅིང་དེ་ལ་ཡང་ཁ་ན་མ་ཐོ་བ་འདིར་འགྱུར་རོ། །

[Block 1063]
གང་ཞིག་ཁྱིམ་པས་དགེ་སློང་དེ་ལ་ནི་ལྟུང་བ་མེད་པར་རིག་པར་བྱའོ། །

[Block 1064]
དེ་བཞིན་དུ་དགོན་པ་ལ་ཡང་གལ་ཏེ་དགེ་སློང་སྔ་ན་གནས་པ་ཡིན་ན་ནི་དེ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 1065]
གཞན་ལ་ནི་ལྟུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་གང་ཞིག་གཞན་རབ་ཏུ་བྱུང་བ་འདི་ལ༌[^632]གཙུག་ལག་ཁང་གཅིག་གམ་གཞན་ན་གནས་པ་དེ་ལ་ནི་གནས་གཞན་ཉིད་ཡིན་པར་རིག་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 1066]
དེ་ལ་ཡང་རུང་བ་ཉིད་ཡོད་པ་ལ་ལྟུང་བ་འབྱུང་བར་འགྱུར་ཏེ། དེ་ལ་ཡང་གཞན་གྱི་དངོས་པོ་ལ་རྗེས་སུ་འབྲེལ་པ་ཞེས་གསུངས་པ་ཡིན་ནོ། །ཅི་གནས་གཞན་ཙམ་འབའ་ཞིག་ལ་འདི་རྣམ་པར་གཞག་གམ་ཞེ་ན། དེའི་ཕྱིར་གནས་གཞན་མེད་པ་ཉིད་ཀྱིས་སྤུད་དུ་རུང་བ་ཉིད་ཡིན་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ཉེ་བར་གནས་པ་ལ་སྤུད་དུ་རུང་བ་ཉིད་ཡིན་ན་དེ་ནི་འདིར་གཞན་མ་ཡིན་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པའོ། །

[Block 1067]
གཉིས་སྤུད་པ་ལས་བྱུང་བའི་འཇུག་པའི་ལ་གེགས་སུ་གྱུར་པ་གཞན་མེད་པས་རུང་བ་ཉིད་ལ་གཉིས་ཀྱིས་གཉིས་སྤུད་པའི་བདག་ཉིད་ཅན་སྦྱོར་བ་ལ་ཞེས་བྱ་བ་ནི། འདིར་དོན་གྱིས་གཞན་ཡོད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 1068]
ཅི་ཞིག་རྗེས་སུ་སྒྲུབ༌[^633]ན་དེ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་མངོན་སུམ་དུ་བརྣགས་པས་འདུག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕྱིས་གནོན་བྱས་ཏེ་སྟོབས་ཀྱིས༌[^634]གློ་བུར་དུ་བརྣགས་པས་ཞེས་བྱ་བ་འདིས་དེ་བསྡུས་པ་ཡིན་ཏེ། དེ་ནི་འདིར་བསྡུས་པའི་དོན་ཏོ། །

[Block 1069]
ཉལ་པོ་བྱེད་པར་ཤོམ་པའི་ཁྱིམ་ན་འདུག་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 1070]
ཤེས་གཙོ་བོ༌[^635]ཞེས་བྱ་བ་ལ་སོགས་པ་ནས་ཡང་དག་པར་སྦྱོར་བ་ཞེས་བྱ་བའི་མཐར་ལྟོས་ནས་སོ། །

[Block 1071]
ཅི་ཞིག་རྗེས་སུ་སྒྲུབ༌[^636]ན་འདིར་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན་དེ་ལ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དབེན་པར་བརྣགས་པས་འགྲེང་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཤིན་ཏུ་ལྕི་བའི་འཇུག་པ་ལ་ལྟུང་བ་མེད་པ་ནི་རིགས་པ་མ་ཡིན་པའམ། ན་སྨད་པ་དེ་བས་ན་མཐར་ཐུག་པའི་རྩེ་གཅིག་པ་ཉིད་ནི་འདིར་གནས་ཀྱི་ཚིག་དང་སྔ་མ་ནི་འདུག་པའི་ཚིག་གོ། །

[Block 1072]
སྟན་ལ་གནས་ཤིང་འདུག་པའི་ཉེས་པ་འདི་ནི་གཞན་ཏེ་འདུག་པ་ལ་ཡང་སྔ་མའོ་ཞེས་རིག་པར་བྱའོ། །

[Block 1073]
མངོན་སུམ་དུ་བརྣགས་པའི་གནས༌[^637]ལ་ཉེས་བྱས་ལ་རྣམ་པར་གནས་པ་ཉིད་དུ་རིག་པར་བྱ་བ་ཡིན་ནོ། །ཅི་གནས་ཐམས་ཅད་ན་འགྲེང་བའི་དགེ་སློང་ལའམ་ཞེ་ན། དེའི་ཕྱིར་སྐྱབས་ཡོད་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྩིག་པའམ་རིབ་མའམ་ཡོལ་བའམ་མུན་ནག་ལ་སོགས་པའི་བདག་ཉིད་ཅན་གེགས་སུ་གྱུར་པའི་མིག་གི༌[^638]ཡུལ་གང་ཡིན་པ་དེ་བསྒྲིབས་པ་སྟེ། དེ་བས་ན་མུན་ནག་གང་ལ་གནས་པ་ལ་སྣང་དུ་རུང་བ་ཉིད་མ་ཡིན་པ་དེ་ནི་བསྒྲིབས་པར་ཤེས་པར་བྱ་བ་ཡིན་ནོ། །ཅི་དགོས་པ་གང་ཡང་རུང་བ༌[^639]གནས་པ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་འཇིགས་པའི་དབང་གིས་མ་ཡིན་ནོ༌[^640]ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1074]
འདིར་གཞུང་ནི་གལ་ཏེ་འཇིགས་པར་གྱུར་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1075]
མངོན་སུམ་དུ་བརྣགས༌[^641]པས་འདུག་པ་ལ་ཡང་འཇིགས་པའི་དབང་གིས་ལྟུང་བ་མེད་ཅེས་བྱ་བ་འདིའི་རྗེས་སུ་འབྲངས་ནས་རྟོགས་པར་བྱའོ། །

[Block 1076]
འཇིགས་པས་གནས་པས་ཀྱང་མཐོ་བཙམས་པའི༌[^642]སེམས་ལ་མངོན་དུ་ཕྱོགས་པར་གྱུར་པ་འདིར་ཤིན་ཏུ་ཚར་བཅད་པ་ལ་རྩེ་གཅིག་པར་གནང་བར་བྱའོ། །

[Block 1077]
ཅི་གནས་དེར་འགྲེང་པ་ཐམས་ཅད་དངོས་གཞིའི་བྱེད་པ་པོ་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཚོར་བྱ་དང་ཚོར་བྱེད་ཉིད་ཀྱིས་མ་ཚོར་ན་ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དང་འདྲ་བའི་རྫས་བྱུང་བ་ཉིད་ལ་སོགས་པ་གང་དུ་སྒྲིབ་པ་སྒྲ་བཟུང་བ༌[^643]ལ་ཡང་སྒྲིབ་པ་རྣམ་པ་ཐམས་ཅད་དུ་རིག་པར་བྱ་བ་ཉིད་ལ་གནས་པ་གང་ལ་ཚོར་བ་བྱེད་པ་པོ་ཉིད་ལ་ཡང་དག་པར་སྦྱོར་བ་མེད་པའི་གནས་སྐབས་དེ་ལ་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1078]
གནས་གཞན་ལ་སེམས་གཏོད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡང་དག་པར་སྦྱོར་བ་པོ་ཉིད་གནས་ནས་གནས་གཞན་དུ་སེམས་གཏོད་པ་སྟེར་བ་ལ་མཐོང་བའམ་ཐོས་པས་དང་ད་ལྟར་བྱུང་བར་གྱུར་པའི་མངོན་སུམ་དུ་བརྣགས་པ༌[^644]དང་དབེན་པར་བརྣགས་པ༌[^645]ལ་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 1079]
བསླབ་པའི་གཞི་འདི་གཉིས་ཀྱང་འདི་ནས་བརྩམས་ནས་ལྷག་མར་གྱུར་པའི་གཞུང་ཞེས་བྱ་བ་ཤུགས་ཀྱིས་རྟོགས་པར་བྱའོ། །

[Block 1080]
འོ་ན་ནི་ཅི་ཙམ་ལ་འདི་དག་གིས་གནས་པ་གཅིག་པ་ཉིད༌[^646]ཅེས་བྱ་བ་འདི་ལ་བརྗོད་པར་བྱ་སྟེ། འདི་ལ་མཐོང་བའི་སྤྱོད་ཡུལ་གྱི་མཐའ་ཚུན་ཆད༌[^647]ནི་གནས་ཀྱི་མཐའ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། འདི་དག་གི་མིག་གི་སྤྱོད་ཡུལ་གྱི་མཐའ་ཚུན་ཆད་ནི་གནས་ཀྱི་མཐའ་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 1081]
མཛོད་ལ་འདི་ལྟར་སོ་སོར་གནས་པ་ཉིད་ཐོབ་པ་བསྐྱེད་པར་བྱ་སྟེ། མཛོད་ནི་ཁོངས་སུ་གཏོགས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཁྱིམ་གཅིག་པར་གྱུར་པ་ཉིད་ལ་ཁྱམས་ཀྱི་བདག་ཉིད་ཅན་གྱི་ཁང་ཁྱིམ་དང་ལྷན་ཅིག་ཅེས་བྱ་བ་འདིས་ཤེས་པ་ཡིན་ཏེ། གཅིག་ཏུ་ཉེ་བར་སྤྱོད་པའི་ཁང་པ་རྣམས་ལ་གཞན་སྒོ་བསྐྱབ་པ༌[^648]ལ་ལྟ་བ༌[^649]ལྟུང་བར་འགྱུར་བ་ཡིན་ཏེ། དེ་ལ་གནས་ནས་གཞན་ཉིད་བསྟན་པའི་དོན་དུ་བརྗོད་པར་བྱ་སྟེ། ཁྱིམ་གཞན་ནི་ཐ་དད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ཉལ་པོ་བྱེད་པར་ཤོམ་པ་ཡང་ཞེས་བྱ་བ་འདིས་གལ་ཏེ་གཟའ་གཅིག༌[^650]པ་ཉིད་ཀྱི་བདག་ཉིད་ཅན་གྱི་གནས་བརྗོད་པ་ཉིད་ཀྱི་ཕྱིར་གཉེན་འདུན་ཐ་དད་པ་ཉིད་ལ་ཚིག་འདི་ཤེས་པར་བྱའོ། །

[Block 1082]
ཉལ་པོ་བྱེད་པར་ཤོམ་པའི་ཁྱིམ་ན་འགྲེང་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 1083]
ཕོ་ཡང་རུང་མོ་ཡང་རུང་བ་ལའོ་ཞེས་བྱ་བ་ནི་རྟགས༌[^651]འདི་དང་རབ་ཏུ་བྱུང་བ་འདི་མེད་པའི་གཅེར་བུའོ་ཞེས་འབྱུང་བ་དང་སྦྱར་རོ། །

[Block 1084]
འདི་ལ་འདིའི་རྣམ་པར་བརྗོད་པ་སྟེ། དེ་ལྟར་གྱུར་པའི་གཅེར་བུའི་གང་ཟག་ལ་ཡང་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 1085]
དེ་ལྟ་བུར་གྱུར་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ཅི་བུད་མེད་དུ་གྱུར་པའམ་སྐྱེས་པར་གྱུར་པ་གཅེར་བུ་ལ༌[^652]ཐམས་ཅད༌[^653]ཡང་མ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཉེ་དུ་དང་རབ་ཏུ་བྱུང་བ་ལ་ཡང་ལྟོས་པ་དང་ནད་པ་མ་གཏོགས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 1086]
འདིར་གཞུང་ནི་དགེ་སློང་འགའ་ཞིག༌[^654]གཅེར་བུ་པ་ལ་རང་གི་སུག་པ་ནས་བཟའ་བ་དང་བཅའ་བ་སྩལ་ལ་ལྟུང་བར་ཡང་མི་འགྱུར་བ་འགའ་ཞིག༌[^655]མཆིས་སམ། ཡོད་དེ་ཉེ་དུ་ལ་བྱིན་པ་དང་། རབ་ཏུ་བྱུང་བ་ལ་ལྟོས་པ་དང་ནད་པ་ལ་བྱིན་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 1087]
དེ་ཇི་ལྟ་བུར་གྱུར་པ་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རྟགས་འདི་དང་རབ་ཏུ་བྱུང་བ་འདི་མེད་པའི་གཅེར་བུའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་རྟགས་འདི་མེད་པའི་རྟགས་ཙམ་གྱི་རབ་ཏུ་བྱུང་བ་གང་ཡིན་པ་དེ་སྟེ་རབ་ཏུ་བྱུང་བ་མ་ཡིན་པ་དང་རྟགས་འདི་ལ་རབ་ཏུ་བྱུང་བ་ལ་ཉམས་པ་ཉིད་དུ་འགྱུར་བ་ཡིན་ཏེ།

[Block 1088]
དང་པོ་འདི་པའི་རབ་ཏུ་བྱུང་བ་ནི་གཅེར་བུ་པ་ཉིད་དོ། །

[Block 1089]
དེ་བས་ན་གཅེར་བུ་པ་ཞེས་བྱ་བ་འདི་ལས་འདི་པའི་རབ་ཏུ་བྱུང་བ་མ་ཡིན་པར་དགག་པ་གྲུབ་པ་ཉིད་དོ། །ཅི་ཞིག་ལྟ་བུར་གྱུར་པའི་གཅེར་བུ་པ་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ལུས་སམ་ལུས་དང་འབྲེལ་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་ཅི་ཞིག་ཅེས༌[^656]བྱ་བ་འདི་ལ་རང་གིས་བྱིན་ན་ཞེས་བྱ་བ་གསུངས་ན་དེ་ལ་གང་བྱིན་ན་ཞེ་ན། དེའི་ཕྱིར་བཅའ་བར་བྱ་བ་དང་བཟའ་བར་བྱ་བ་དག་གི༌[^657]ཞེས་བྱ་བ་སྨོས་སོ། ། ཅི་རྣམ་པ་གང་ཡང་རུང་བ་ཞིག་གམ་ཞེ་ན། དེའི་ཕྱིར་རུང་བ་དག་གོ་ཞེས་བྱ་བ༌[^658]སྨོས་སོ། །

[Block 1090]
དེ་དག་སུ་ལ་རུང་བ་ཞེ་ན། དེའི་ཕྱིར་རང་དང་དེ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་ཞེས་བྱ་བ་ནི་ལྟུང་བའི་ཚིག་གོ། །
--- END BLOCKS ---
