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
[Block 1016]
གང་ཞིག་གི་ཞེ་ན། དགྲ་བཅོམ་པ་ཕོ་མོ་རབ་ཀྱི་མཐའི་བསམ་གཏན་ཐོབ་པ་དུས་དང་མི་སྦྱོར་བར་རྣམ་པར་གྲོལ་བ༌[^440]སྟེ། དེ་ནི་ཏིང་ངེ་འཛིན་ལ་ཡང་དབང་ཞིང་ཉོན་མོངས་པ་དག་གིས་ཀྱང་རྒྱུ༌[^441]ཉེ་བར་མ་བསྟན་པ་ཡིན་ནོ། །

[Block 1017]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཀྱིས། སྲོག་གི་འདུ་བྱེད་དག་བྱིན་གྱིས་བརླབས་ནས་ཚེའི་འདུ་བྱེད་དག་བཏང་ངོ་ཞེས་གསུངས་པ་དེ་དག་ལ་ཁྱད་པར་ཅི་ཞིག་ཡོད་ཅེ་ན། ཁ་ཅིག་ན་རེ་ཅུང་ཟད་ཀྱང་མེད་དེ། འདི་ལྟར་སྲོག་གི་དབང་པོ་གང་ཞེ་ན། ཁམས་གསུམ་པའི་ཚེ་ཡིན་ནོ་ཞེས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 1018]
ཁ་ཅིག་ན་རེ་ནི་སྔོན་གྱི་ལས་ཀྱི་འབྲས་བུ་ནི་ཚེའི་འདུ་བྱེད་དག་ཡིན་ལ། ད་ལྟར་བྱུང་བའི་ལས་ཀྱི་འབྲས་བུ་ནི་སྲོག་གི་འདུ་བྱེད་དག་ཡིན་ནོ་ཞེས་ཟེར་ཏེ། གང་དག་གིས་རིས་མཐུན་པར་གནས་པར་འགྱུར་བ་དེ་དག༌[^442]ནི་ཚེའི་འདུ་བྱེད་དག་ཡིན་ལ། གང་དག་གིས་དུས་གཞན་གྱི་བར་དུ་འཚོ་བ་དེ་དག་ནི་སྲོག་གི་འདུ་བྱེད་དག་ཡིན་ནོ། །

[Block 1019]
མང་པོའི་ཚིག་ནི་ཚེ་དང་སྲོག་གི་འདུ་བྱེད་ཀྱི་སྐད་ཅིག་མ་རྣམ་པ༌[^443]མང་པོ་རྣམས་ལ་གཏོང་ཞིང་བྱིན་གྱིས་རློབ་པའི་ཕྱིར་ཏེ། སྐད་ཅིག་མ་གཅིག་ལ་ནི་གཏོང་བ་འམ་བྱིན་གྱིས་རློབ་པ་མེད་དོ། །

[Block 1020]
ཁ་ཅིག་ན་རེ་དུས་གཞན་གྱི་བར་དུ་འདུག་པ༌[^444]ཚེའི་རྫས་གཅིག་པུ་ནི་མེད་དོ་ཞེས་བསྟན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 1021]
ཁ་ཅིག་ན་རེ་འདུ་བྱེད་མང་པོ་རྣམས་ལ་ཚེ་ཞེས་བྱ་བའི་ཚེའི་རྫས་གཅིག་པུ་ནི་མེད་དོ། །

[Block 1022]
དེ་ལྟ་མ་ཡིན་ན་འདུ་བྱེད་སྨོས་པ་མི་མཛད་པར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 1023]
ཡང་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ཚེའི་འདུ་བྱེད་དག་བཏང་ཞིང་བྱིན་གྱིས་བརླབས་ཤེ་ན། འཆི་བ་ལ་མངའ་བ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་ནི་བཏང་ལ། ཚེ་ལ་མངའ་བ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་ནི་ཟླ་བ་གསུམ་ཁོ་ན་བྱིན་གྱིས་བརླབས་ཏེ། ཕྱིན་ཆད་ནི་གདུལ་བའི་དོན་མེད་པའི་ཕྱིར་མ་ཡིན་ནོ། །

[Block 1024]
གང་ཡང་ངས་རྫུ་འཕྲུལ་གྱི་རྐང་པ་བཞི་པོ་དེ་ལྟར་བསྒོམས་པ་དག་གིས་འདོད་ན་བསྐལ་པ་འམ་བསྐལ་པ་བས་ལྷག་པར་བཞུགས་པར་བྱའོ་ཞེས་དམ་བཅས་པ་དེ་ཡང་སྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 1025]
བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ་ནི་ཕུང་པོ་དང་འཆི་བདག་གི་བདུད་དག༌[^445]ལས་རྒྱལ་བར་བསྟན་པའི་ཕྱིར་རོ་ཞེས་ཟེར་ཏེ། བྱང་ཆུབ་ཀྱི་ཤིང་དྲུང་དུ་ནི་ཉོན་མོངས་པ་དང་ལྷའི་བུའི་བདུད་དག་ལས་རྒྱལ་ལོ། །

[Block 1026]
ཞར་ལ་འོངས་པ་རྫོགས་སོ།། །།

[Block 1027 [HEADING]]
###### རྣམ་པར་སྨིན་པ་དང་རྣམ་པར་སྨིན་པ་མ་ཡིན་པ། ^2-1-4-2-2-0

[Block 1028]
དཀྱུས་མ་ཉིད་བརྩམ་པར་བྱ་སྟེ། བཅུ་གཉིས་གཉིས། བཅུ་གཉིས་གང་ཞེ་ན། ཐ་མ་བརྒྱད་དང་ཡིད་མི་བདེ། །མ་གཏོགས་པ་སྟེ། དད་པ་ལ་སོགས་པ་ཐ་མ་བརྒྱད་དང་། ཡིད་མི་བདེ་བ་མ་གཏོགས་པ་སྲོག་གི་དབང་པོ་ལས་གཞན་པ་བཅུ་གཉིས་ནི་རྣམ་པ་གཉིས་ཏེ། རྣམ་པར་སྨིན་པ་ཡང་ཡིན་ལ། རྣམ་པར་སྨིན་པ་མ་ཡིན་པ་ཡང་ཡིན་ནོ། །

[Block 1029]
དེ་ལ་མིག་ལ་སོགས་པ་བདུན་རྒྱས་པ་ལས་བྱུང་བ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་མ་ཡིན་ནོ། །

[Block 1030]
ལྷག་མ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་ཡིན་ནོ། །

[Block 1031]
ཡིད་དང་། སྡུག་བསྔལ་དང་། བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་ཀྱི་དབང་པོ་རྣམས་ནི་དགེ་བ་དང་ཉོན་མོངས་པ་ཅན་རྣམས་དང་། སྤྱོད་ལམ་པ་དང་བཟོའི་གནས་པ་དང་། སྤྲུལ་པ་རྣམས་ནི་ཅི་རིགས་པར༌[^446]རྣམ་པར་སྨིན་པ་མ་ཡིན་ནོ། །

[Block 1032]
ལྷག་མ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་ཡིན་ནོ། །

[Block 1033]
སྲོག་གི་དབང་པོ་དང་། མིག་ལ་སོགས་པ་བཅུ་གཉིས་མ་གཏོགས་པ་ལྷག་མ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་མ་ཡིན་པ་ཞེས་བྱ་བར་གྲུབ་པོ། །གལ་ཏེ་ཡིད་མི་བདེ་བ་རྣམ་པར་སྨིན་པ་མ་ཡིན་ན་ལས་ནི་གསུམ་སྟེ། ཡིད་བདེ་བ་མྱོང་བར་འགྱུར་བའི་ལས་དང་། ཡིད་མི་བདེ་བ་མྱོང་བར་འགྱུར་བའི་ལས་དང་། བཏང་སྙོམས་མྱོང་བར་འགྱུར་བའི་ལས་ཞེས་གསུངས་པའི་མདོ་འདི་ཇི་ལྟར་དྲང་ཞེ་ན། མཚུངས་པར་ལྡན་པ་མྱོང་བར་འགྱུར་བའི་དབང་དུ་མཛད་ནས་གསུངས་པ་ཡིན་ཏེ། ཡིད་མི་བདེ་བ་དང་མཚུངས་པར་ལྡན་པའི་ལས་ནི་ཡིད་མི་བདེ་བ་མྱོང་བར་འགྱུར་བ་སྟེ། དཔེར་ན་བདེ་བ་དང་མཚུངས་པར་ལྡན་པའི་རེག་པ་བདེ་བ་མྱོང་བར་འགྱུར་བ༌[^447]ཡིན་པ་བཞིན་ནོ། །

[Block 1034]
འོ་ན་ནི་ཡིད་བདེ་བ་དང་བཏང་སྙོམས་མྱོང་བར་འགྱུར་བའི་ལས་དག་ཀྱང་དེ་དང་འདྲ་བར་འགྱུར་རོ་ཞེ་ན། ཇི་ལྟར་དགའ་བ་དེ་ལྟར་ཡིན་ལ་རག་སྟེ། མཚུངས་པར་ལྡན་པ་ཡིན་ན་ཡང་ཉེས་པ་མེད་ལ། རྣམ་པར་སྨིན་པ་ཡིན་ན་ཡང་ཉེས་པ་མེད་དོ། །

[Block 1035]
གོ་སྐབས་མེད་པས་ན་དེ་ནི་དེ་ལྟར་ཤེས་སོ། །

[Block 1036]
ཡིད་མི་བདེ་བ་རྣམ་པར་སྨིན་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་རིགས་པ༌[^448]ཅི་ཞིག་ཡོད་ཅེ་ན། ཡིད་མི་བདེ་བ་ནི་ཀུན་ཏུ་རྟོག་པའི་ཁྱད་པར་དག་གིས་སྐྱེད་པར་བྱེད་པ་ཡིན་གྱི༌[^449]རྣམ་པར་སྨིན་པ་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 1037]
ཡིད་བདེ་བ་ཡང་དེ་དང་འདྲ་བས་རྣམ་པར་སྨིན་པ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 1038]
འོ་ན་གལ་ཏེ་ཡིད་མི་བདེ་བ་རྣམ་པར་སྨིན༌[^450]པར་གྱུར་ན་མཚམས་མེད་པ་བྱེད་པ་རྣམས་དེའི་ཕྱིར་ཡིད་མི་བདེ་བ་སྐྱེད་པས་ལས་དེ་རྣམ་པར་སྨིན་པར་འགྱུར་རོ་ཞེ་ན། ཡིད་མི༌[^451]བདེ་བ་ཡང་དེ་དང་འདྲ་སྟེ། གལ་ཏེ་ཡིད་བདེ་བ་རྣམ་པར་སྨིན་པར་གྱུར་ན་བསོད་ནམས་བྱེད་པ་རྣམས་དེའི་ཕྱིར་ཡིད་བདེ་བ་སྐྱེད་པས༌[^452]ལས་དེ་རྣམ་པར་སྨིན་པར་འགྱུར་རོ། །

[Block 1039]
འོ་ན་འདོད་ཆགས་དང་བྲལ་བ་རྣམས་ལ་ཡིད་མི་བདེ་བ་མི་སྲིད་པའི་ཕྱིར་ཏེ། རྣམ་པར་སྨིན་པ་ནི་དེ་ལྟ༌[^453]མ་ཡིན་ནོ་ཞེ་ན། དེ་དག་གི་ཡིད་བདེ་བ་ལུང་དུ་མ་བསྟན་པ་རྣམ་པར་སྨིན་པ་ཡང་ཇི་ལྟ་བུ་ཞིག་ཡིན། བྱེ་བྲག་ཏུ་སྨྲ་བ་རྣམས་ན་རེ། ཅི་འདྲ་ཡང་རུང་སྟེ། ཡིད་བདེ་བ་ལ་རྣམ་པར་སྨིན་པའི་གོ་སྐབས་ཡོད་ཇི༌[^454]སྲིད་དུ་ཟིན་ཀྱང་། ཡིད་མི་བདེ་བ་ནི་རྣམ་པ་ཐམས་ཅད་དུ་ཡང་ཀུན་དུ་མི་འབྱུང་བས་ཡིད་མི་བདེ་བ་ལ་རྣམ་པར་སྨིན་པ་མེད་ཅེས་ཟེར་རོ། །

[Block 1040]
དེ་ལ་བརྒྱད་པ་སྲོག་གི་དབང་པོ་དང་། གཞན་རྣམས་བདེ་འགྲོ་ན་ནི་བདེ་བ༌[^455]རྣམ་པར་སྨིན་པ་ཡིན་ལ། ངན་འགྲོ་བ༌[^456]ནི་མི་བདེ་བའི་རྣམ་པར་སྨིན་པ་ཡིན་ནོ། །

[Block 1041]
ཡིད་ཀྱི་དབང་པོ་ནི་གཉིས་ཀར༌[^457]གཉི་གའི་རྣམ་པར་སྨིན་པ་ཡིན་ནོ། །

[Block 1042]
བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་ཀྱི་དབང་པོ་རྣམས་ནི་དགེ་བའི་རྣམ་པར་སྨིན་པ་ཡིན་ནོ། །

[Block 1043]
སྡུག་བསྔལ་གྱི་དབང་པོ་ནི་མི་དགེ་བའི་རྣམ་པར་སྨིན་པ་ཡིན་ནོ། །

[Block 1044]
བདེ་འགྲོ་ན་མི་དགེ་བས་མཚན་གཉིས་པོ་དེའི་གནས་རྙེད་པ་ཡིན་གྱི་དབང་པོ་ནི་མ་ཡིན་ཏེ། དགེ་བས་འཕངས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 1045]
དེ་ནི་རྫོགས་སོ།། །།

[Block 1046 [HEADING]]
##### རྣམ་པར་སྨིན་པ་དང་བཅས་པ། ^2-1-4-3-0

[Block 1047]
འདི་བརྗོད་པར་བྱ་སྟེ། དབང་པོ་དུ༌[^458]ནི༌[^459]རྣམ་པར་སྨིན་པ་དང་བཅས་པ་དག་ཡིན། དུ་ནི་རྣམ་པར་སྨིན་པ་མེད་པ་དག་ཡིན་ཞེ་ན། གང་འདི་ཡིད་མི་བདེ་བ་བཤད་མ་ཐག་པ། དེ་གཅིག་ནི་རྣམ་པར་སྨིན་བཅས་དེ་གཅིག་པུ་ནི་རྣམ་པར་སྨིན་པ་དང་བཅས་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 1048]
ནི་ཞེས་བྱ་བའི་སྒྲ་ནི་ཁོ་ན་ཞེས་བྱ་བའི་དོན་དང་རིམ་པ་གཞན་དུ་སྦྱར་བ་ཡིན་པར་རིག་པར་བྱ་སྟེ། དེ་ནི་ལུང་དུ་མ་བསྟན་པ་ཡང་མེད་ལ། མཉམ་པར་གཞག་པ་མ་ཡིན་པའི་ཕྱིར་ཟག་པ་མེད་པ་ཡང་མེད་དེ། དེའི་ཕྱིར་ཡིད་མི་བདེ་བ་རྣམ་པར་སྨིན་པ་མེད་པ་མ་ཡིན་ནོ། །

[Block 1049]
བཅུ་རྣམ་གཉིས། རྣམ་པར་སྨིན་པ་དང་བཅས་པ་དག་ཀྱང་ཡིན། རྣམ་པར་སྨིན་པ་མེད་པ་དག་ཀྱང་ཡིན་ནོ། །

[Block 1050]
བཅུ་གང་ཞེ་ན། ཡིད་དང་ཚོར་གཞན་དད་ལ་སོགས། །ཚོར་བ༌[^460]གཞན་ཞེས་བྱ་བ་སྨོས་པས་ནི་ཡིད་མི་བདེ་བ་ལས་གཞན་པའི་ཚོར་བ་གཟུང༌[^461]ངོ་། །དད་ལ་སོགས་ནི་དད་པ་དང་བརྩོན་འགྲུས་དང་དྲན་པ་དང་ཏིང་ངེ་འཛིན་དང་ཤེས་རབ་པོ། །དེ་ལ་ཡིད་དང་བདེ་བ་དང་ཡིད་བདེ་བ་དང་བཏང་སྙོམས་མི༌[^462]དགེ་བ་ཟག་པ་དང་བཅས་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 1051]
ཟག་པ་མེད་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་མེད་པ་དག་ཡིན་ནོ། །

[Block 1052]
སྡུག་བསྔལ་གྱི་དབང་པོ་ནི་དགེ་བ་དང་མི་དགེ་བ་ནི་རྣམ་པར་སྨིན་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 1053]
ལུང་དུ་མ་བསྟན་པ་ནི་རྣམ་པར་སྨིན་པ་མེད་པ་ཡིན་ནོ། །

[Block 1054]
དད་པ་ལ་སོགས་པ་ཟག་པ་དང་བཅས་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་དང་བཅས་པ་ཡིན་ནོ། །

[Block 1055]
ཟག་པ་མེད་པ་རྣམས་ནི་རྣམ་པར་སྨིན་པ་མེད་པ་དག་ཡིན་ནོ། །
--- END BLOCKS ---
