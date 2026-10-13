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
[Block 911]
མེད་པ་དེས་ན་རྟག་མ་ཡིན།[^655] །ཞེས་སོ། །

[Block 912]
མེད་པ་ཡང་མ་ཡིན་ཏེ། ངོ་བོ་ཉིད་མ་གྲུབ་པ་ཁོ་ནས་དངོས་པོ་མེད་པ་ཡང་མེད་པའི་ཕྱིར་རོ། །

[Block 913]
དངོས་པོ་རབ་ཏུ་མ་གྲུབ་ན། །དངོས་མེད་འགྲུབ་པར་ག་ལ་འགྱུར། །ཞེས་པའི་ཚིག་ལས་སོ། །

[Block 914]
ཡོད་མེད་ཀྱང་མ་ཡིན་ཏེ། གཅིག་ལ་འགལ་བའི་ཆོས་གཉིས་ཀྱི་བདག་ཉིད་ཅན་མེད་པའི་ཕྱིར་རོ། །

[Block 915]
དེ་བཞིན་དུ་འདུས་མ་བྱས་ལ་ཡང་བརྗོད་པར་བྱའོ། །

[Block 916]
འདུས་བྱས་འབའ་ཞིག་ཁོ་ན་ལ་གཅིག་དང་། གཞན་དང་། ཡོད་པ་དང་། མེད་པ་དང་། གཉི་ག་ཡང་མི་སྲིད་པ་འཐད་པར་མ་ཟད་ཀྱི། གཞན་ཡང་ངེས་པར་ཟག་པ་དང་བཅས་པ་དང་ཟག་པ་མེད་པ་དང་། གཟུགས་ཅན་དང་གཟུགས་མེད་པ་དང་། བསྟན་དུ་ཡོད་པ་དང་བསྟན་དུ་མེད་པ་དང་། ཐོགས་བཅས་དང་ཐོགས་མེད་དང་། རྒྱུ་དང་འབྲས་བུ་དང་། མཚན་གཞི་དང་། མཚན་ཉིད་དང་ཉེ་བར་ལེན་པ་དང་། ཉེ་བར་ལེན་པ་པོ་དང་། འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པ་ལ་སོགས་པ་དང༌[^656]དངོས་པོ་ཐམས་ཅད་ལ་ཡང་འདི་ལྟར་བརྟག་པའི་རྣམ་པར་གཞག་པ་ལས་ཤིན་ཏུ་མི་རྟོགས་ཏེ། ཇི་སྐད་དུ་སྨོས་པའི་དེ་ཉིད་དང་གཞན་ཉིད་ལ་སོགས་པའི་རྣམ་པ་ལས་བསམས་པའི་སྒོ་ནས་དགག་པའི་ངག་གི་གོ་སྐབས་ཐོབ་པར་བྱས་པས་སོ། །

[Block 917]
དེར་འདུས་པའི་ཕྱིར་ཡང་ངེས་པར་འདུས་བྱས་དང་འདུས་མ་བྱས་ལྟར་དེ་དག་དགག་པར་རིག་པར་བྱའོ་ཞེས་གསུངས་པ། མཚམས་འདིར་སྣ་ཚོགས་ཐམས་ཅད་འདུས། །ཞེས་པ་ལ། མཚམས་དང་ཁྲིམས་དང་དེའི་བར་དུ་ཞེས་པ་དོན་གཞན་མ་ཡིན་ནོ། །

[Block 918]
ཐམས་ཅད་ཀྱི་སྒྲ་ནི་ཟད་པར་གྱི་དོན་ཏོ། །

[Block 919]
སྣ་ཚོགས་ཀྱི་སྒྲ་ནི་རྣམ་པའི་དོན་ཏོ་ཞེས་རིག་པར་བྱའོ། །

[Block 920]
[^657]

[Block 921]
འདིར་སྨྲས་པ། ཇི་སྐད་དུ་སྨོས་པའི་འདུས་བྱས་ལ་སོགས་པ་རང་བཞིན་མེད་པར་བསྒྲུབ་པར་མི་ནུས་ཏེ། ལུང་དང་འགལ་བའི་ཕྱིར། འདི་ལྟར།

[Block 922 [HEADING]]
### ཚིགས་བཅད་སོ་གསུམ་པ། ^1-33-0

[Block 923 [VERSE]]
བླ་མ་བཅོམ་ལྡན་ལས༌[^658]གནས་དང་། །
ལས་ཀྱི་བདག་ཉིད་འབྲས་བུ་གསུངས། །
སེམས་ཅན་རང་གི་ལས་དང་ནི། །
ལས་ནི་རྣམ་པར་འཇིག་མེད་གསུངས། །

[Block 924]
མདོ་ལས་གསུངས་པ།

[Block 925 [VERSE]]
ནོར་དང་འབྲུ་དང་ས་ལེ་སྦྲམ། །
ནོར་བུའི་རྣ་རྒྱན་བ་ལང་རྟ། །
བྲན་དང་ལས་བྱེད་མངག་གཞུག་པ། །
གང་ཡང་གཞན༌[^659]པའི་ནོར་རྣམས་དང་། །

[Block 926 [VERSE]]
ཅུང་ཟད་ཁྱེར་ནས་འགྲོ་མིན་ཞིང་། །
ཐམས་ཅད་བོར་ནས་འགྲོ་བར་འགྱུར། །
ཐ་མའི་གནས་སྐབས་མངོན་གྱུར་པ། །
མི་ཡི་སྲིད་པ་སྤོང་བར་འགྱུར། །

[Block 927 [VERSE]]
ཅི་དེ་རང་གི༌[^660]ཅུང་ཟད་ཙམ། །
བླངས་ན༌[^661]དེ་ནི་འགྲོ་བར་འགྱུར། །
འདི་ཡིས་ཅི་ཞིག་མི་སྤོང་ན། །
ཇི་ལྟར་གྲིབ་མ་རྗེས་འགྲོ་བཞིན། །

[Block 928 [VERSE]]
གང་ཞིག་སྐྱེས་བུས༌[^662]འདིར་བྱས་པའི། །
སྡིག་པ་དང་ནི་བསོད་ནམས་གཉིས། །
དེ་ནི་དེ་ཡིས༌[^663]རང་གིར་འགྱུར། །
དེ་ཡང་བླངས་ནས་འགྲོ་བས་ན། །

[Block 929 [VERSE]]
འདི་དག་དེ་ཡིས་མི་སྤོང་སྟེ། །
ཇི་ལྟར་གྲིབ་མ་རྗེས་འགྲོ་བཞིན། །
ཇི་ལྟར་ལམ་ངན་ནས་འགྲོ་བ། །
འགྲོ་བ་པོ་འདིར་སྡུག་བསྔལ་འགྱུར། །

[Block 930 [VERSE]]
དེ་བཞིན་བསོད་ནམས་མ་བྱས་པའི། །
སེམས་ཅན་ངན་འགྲོར་འགྲོ་བར་འགྱུར། །
ཇི་ལྟར་ལམ་བཟངས་ནས་འགྲོ་བ། །
འགྲོ་བ་པོ་འདིར་བདེ་བས་འགྲོ། །

[Block 931 [VERSE]]
དེ་བཞིན་འདིར་བྱས་བསོད་ནམས་ཀྱིས། །
སེམས་ཅན་བདེ་འགྲོར་འགྲོ་བར་འགྱུར། །
སྐྱེས་བུ་ཡུན་རིང་འགྲོན༌[^664]བྱས་ནས། །
རིང་ནས་དགེ་བར་འོངས་པ་ན། །

[Block 932 [VERSE]]
གཉེན་འདུན་སྙིང་དགའ་འགྲོག་བཤེས༌[^665]རྣམས། །
འདིར་འོངས་པ་ལ་མངོན་པར་བསྟོད། །
དེ་བཞིན་བསོད་ནམས་བྱས་པ་ཡི། །
འཇིག་རྟེན་འདི་ནས་ཕ་རོལ་འགྲོ། །

[Block 933]
བསོད་ནམས་ཁོ་ན་མངོན་བསྟོད་དེ། །མཛའ་སྡུག་བཤེས་གཉེན་ལྟ་བུར་འོངས།[^666] །

[Block 934]
དེ་ཕྱིར་བསོད་ནམས་ཕུང་པོ་ནི། །ཕ་རོལ་འགྲོ་བ་རྣམས་ཀྱིས་བྱོས། །

[Block 935]
བསོད་ནམས་འཇིག་རྟེན་ཕ་རོལ་ཏུ།[^667] །

[Block 936 [VERSE]]
སྲོག་ཆགས་རྣམས་ཀྱིས་རབ་གནས་བརྗོད། །
བསོད་ནམས་ལྷ་རྣམས་བསྔགས་པར་བྱེད། །
ཞི་བའི་སྤྱོད་པའང་གང་སྤྱོད་པ། །
འདིར་ཡང་སྨོད་པར་མི་འགྱུར་ཞིང་། །

[Block 937]
མཐོ་རིས་འགྲོ་ལ་རྗེས་ཡི་རང་། ། ཞེས་པ་མདོ་འདིར། ནོར་དང་འབྲུ་ལ་སོགས་པ་ཆུད་ཟོས་ཀྱང་ལས་གནས་པར་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་སོ། །

[Block 938]
སླར་ཡང་གསུངས་པ། བསོད་ནམས་མེ་ཡིས་མི་འཚིག༌[^668]ཅིང་། །རླུང་གིས་འཇིག་པའང་མ་ཡིན་ཏེ།[^669] །

[Block 939]
ཆུ་ཡིས་གཤེར་བ་མ་ཡིན་ལ། །ས་ལ་ནུབ་པར་མི་འགྱུར་རོ། །ཞེས་པ་འདིས་ཀྱང་གནས་པར་གསུངས་ལ། ཡོད་བཞིན་པ་མ་ཡིན་པའི་ནམ་མཁའི་མེ་ཏོག་ལ་གནས་པ་ཉེ་བར་བསྟན་པ་མི་འཐད་དོ་ཞེས་བྱའོ། །

[Block 940]
དེས་ན་འདུས་བྱས་དང་འདུས་མ་བྱས་བཞིན་ཆོས་ཐམས་ཅད་མེད་པར་གནས་པར་མི་ནུས་སོ། །

[Block 941]
ལས་ཀྱི་བདག་ཉིད་ཀྱང་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་ཏེ། དགེ་སློང་དག་མཐའ་གཅིག་ཏུ་གནག་པ་རྣམས་ཀྱི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཡང་མཐའ་གཅིག་ཏུ་གནག་པའོ། །

[Block 942]
མཐའ་གཅིག་ཏུ་དཀར་བའི་ལས་ཀྱི་རྣམ་པར་སྨིན་པ་ཡང་མཐའ་གཅིག་ཏུ་དཀར་བའོ། །

[Block 943]
འདྲེན་མ་རྣམས་ཀྱི་འདྲེན་མའོ་ཞེས་པའི་ཚིག་ལས།

[Block 944]
གང་གི་ལས་ཀྱི་བདག་ཉིད་རང་གི་ངོ་བོ་དེ། ལས་ཀྱི་བདག་ཉིད་ཀྱི་འབྲས་བུའོ། །

[Block 945]
ལས༌[^670]མེད་ན་ཡང་དེའི་རྒྱུ་དང་འབྲས་བུའི་ངེས་པར་མི་བརྗོད་པས། དེས་ན་ལས་ཡོད་པར་རིགས་ལ། དེ་ལས་དངོས་པོ་ཐམས་ཅད་གྲུབ་པོ་ཞེས་བྱའོ། །

[Block 946]
སེམས་ཅན་རང་གི་ལས་ཀྱང་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་ཏེ། སེམས་ཅན་མི་རྣམས་ཀྱི་རང་གི་ལས་ལ་ལས་ནི་སྦྱིན་པ་སྦྱིན་པར་བྱེད་པའོ་ཞེས་བྱ་བའི་ཚིག་ལས་ལུས་ཞིག་ན་ནོར་དང་འབྲུ་ལ་སོགས་པ་འཇོག་པར་བྱེད་ལ། ལས་ནི་འཇིག་རྟེན་ཕ་རོལ་ཏུ༌[^671]རྗེས་སུ་འབྲང་བའི་ཕྱིར་ལས་ཀྱང་གང་གི་རང་གི་བདེ༌[^672]ནི་རང་གི་ལས་སོ། །

[Block 947]
དེས་ན་ཡང་དེའི་ལས་ཡོད་ལ། སེམས་ཅན་དེའང་ཡོད་པས་དངོས་པོ་རྣམས་རང་བཞིན་མེད་པ་མ་ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 948]
ལས་རྣམ་པར་འཇིག་པ་མེད་པར་ཡང་དེ་བཞིན་གཤེགས་པས་གསུངས་ཏེ།

[Block 949 [VERSE]]
ལུས་ཅན་རྣམས་ཀྱི་ལས་རྣམས་ནི། །
སྐལ་བ༌[^673]བརྒྱར་ཡང་ཆུད་མི་ཟ། །
ཚོགས་པ་རྙེད་ནས་དུས་སུ་ནི། །
འབྲས་བུ་གདོན་མི་ཟ་བར་སྨིན། །

[Block 950]
ཞེས་བྱ་བ་ལ་སོགས་པས་ཀྱང་ལས་མེད་ན་ཆུད་མི་ཟ་བའི་ཚིག་རུང་བ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
