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
[Block 841]
གང་གི་ཚེ་དེ་གཉིས་ལྟུང་བ་འདི་ལ་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་རང་གིས་བླངས་ཏེ་ཟོས་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རང་གིས་བླངས་ཏེ་ཟོས་ནའོ། །

[Block 842]
མི་ན་བས་བླངས་པ་དང་སློང་དུ༌[^499]བཅུག་པ་ཉིད་དེ་ལ༌[^500]ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་ནི༌[^501]མི་ན་བས་རང་གིས་བླངས་པ་ཙམ་ལ་ཡང་དེ་གཉིས་ཉེས་བྱས་ཁོ་ནའི་བྱེད་པ་པོ་ཡིན་ལ་མིན་བར་གཞན་སློང་དུ་བཅུག་པ་ཉིད་ཡིན༌[^502]ན་སློང་དུ་བཅུག་ཏེ་ཟོས་པ་དེ་ལ་ནི་དེ་གཉིས་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 843]
མི་ན་བར་སློང་དུ་བཅུག་པ་ལ་ནི་ཉེས་བྱས་ཕྲ་མོར་འགྱུར་རོ། །

[Block 844]
ཅི་མི་ན་བར༌[^503]ཐམས་ཅད་ལ་དེ་གཉིས་ཁ་ན་མ་ཐོ་བ་འདིའི་བྱེད་པ་པོ༌[^504]ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཅི་བདེར་བསྟབས་པ་མ་བྱས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་ལ་སློང་བར་བྱེད་པ་དེས་མ་བྱས་པ་དེས་ནི་ཅི་བདེར་བསྟབས་པ་མ་བྱས་པ་ལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 845]
འདིར་གཞུང་ནི་དགེ་སློང་བསོད་སྙོམས་ལ་རྒྱུ་ཞིང་ཁྱིམ་དག་ཏུ་འགྲོ་བ་ན་བུད་མེད་ཀྱི་ཡུལ་ཟས་ཐོགས་ཏེ་ཕྱིར་བྱུང་བའི་ཚེ་དགེ་སློང་ཅང་མི་སྨྲ་བར་སྡོད་པ་ན་བུད་མེད་ཀྱི་ཡུལ་ན་རེ་འཕགས་པ་ཅི་བཞེད་ཅེས་འདྲི་ན་བསྟབས་པར་བརྗོད་པར་བྱ་སྟེ། ཅི་འདོད་པ་དེ་བླང་བར་བྱ་བ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 846]
སྦྱིན་བདག་གིས་ཅི་བདེར་བྱས་པ་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 847]
དེའི་ཕྱིར་ངན་པའམ་བསོད་པའམ་ཐ་མལ་པའམ་བཟང་པོ་ཐོབ་པ༌[^505]ནི་གལ་ཏེ་བླངས་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར་ཅི་བདེར་བསྟབས་པ་མ་བྱས་པ་ལ་འདི་ནི་བྱེད་པ་པོ་ཡིན་ཏེ། ཅི་བདེར་བསྟབས་པར༌[^506]བྱེད་པ་ཅིག༌[^507]ནི་འདིར་ངེས་པར་འབྱུང་བ་སྟེ། ཉེ་བར་བསྡུས་པ་ལ་བྱེད་པ་པོ་མ་ཡིན་ནོ། །

[Block 848]
དེ་ལས་རྙེད་པར་གྱུར་པ་ལ་ཡང་གལ་ཏེ་འདི་དང་འབྲེལ་པའི་བླངས་པ་མེད་ན་དེ་ལྟར་ཡང་འདི་བླངས་ཏེ་ཟོས་ན་དངོས་གཞིའི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 849]
ངན་པ་འདི་ལ་ཕྱེད་ཉིད་དོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་བླངས་ཏེ་ཟ་བ་འདི་ལ་བྱེད་པ་པོ་ཉིད་བསྟན་པ་དེར་ངན་པ་འདི་ལ་ནི་ཕྱེད་ཉིད་དེ་ཉེས་བྱས་སོ། །

[Block 850]
རང་གིས་བླངས་ཏེ་ཟ་བ་འདི་ལ་ནི་ཉེས་བྱས་ཕྲ་མོར་འགྱུར་ཏེ་སློང་དུ་བཅུག་པའི་སྦྱོར་བ་ལ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 851]
འདིར་གཞུར་ནི་དགེ་སློང་གིས་འོ་མ་ཐོབ་པ་ན་ཞོ་སློང་བར་བྱེད་ན། དེ་སློང་བ་ལ་ནི་ཉེས་བྱས་ལ་མ༌[^508]འཐུངས་ན་ནི་ལྟུང་བ་མེད་དོ། །

[Block 852]
དགེ་སློང་གིས་བསོད་པ་ཐོབ་པ་ན་ངན་པ་སློང་བར་བྱེད་ན་དེ་སློང་བ་ལ་ཡང་ཉེས་བྱས་ལ་ཟོས་པར་གྱུར་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 853]
ངན་པ་ཐོབ་པར་གྱུར་པ་ཉིད་ལ་ནི་ཐམས་ཅད་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་འདིས་ནི་ཕྱེད་ཚིག་གིས༌[^509]འདི་ལ་བྱས་པར་རིག་པར་བྱའོ། །

[Block 854]
ཟས་ཁྱེར་ཏེ་ཕྱིས་བྱུང་བས་ཅང་མི་སྨྲ་བའམ་ཕྱིར་སྤོང་བ་ལ་འོ་ན་ཅི་སློང་ཞེས་དྲིས་པ་ན་ཅི་བདེ་བར་བསྟབས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དྲིས་པ་འདི་ལ་ཅི་བདེ་བར་བསྟབས་པ་ཉིད་ཡིན་ནོ། །

[Block 855]
དེ་བས་ན་འདིར་བྱིས་པ༌[^510]ལས༌[^511]གང་འདོད་པ་དེ་བླང་བར་བྱའོ། །

[Block 856]
བསོད་པ་སློང་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 857]
རང་སྤྱོད་པའི་དོན་ཉིད་ལ་འཇུག་པ་དང་སྤྱོད་དུ་འཇུག་པ་དག་ལའོ་ཞེས་བྱ་བ་ནི་འདི་དག་ལ་གཞན་ཉེ་བར་སྤྱོད་པའི་དོན་ཉིད་ལ་སྟེ། དཔེར་ན་དགེ་འདུན་གྱི་གཙུག་ལག་ཁང་དུ་ལྷུང་བཟེད་དང་ཆོས་གོས་ལ་སོགས་པའི་ལས་ལ་དོན་མ་ཡིན་པ་ཉིད་ལ་ཡང་ངོ་། །འདི་ལྟ་སྟེ་དཔེར་ན་དོན་མེད་པར་ཆུ་ལ་སོགས་པ་ལ་སྤྱོད་པ་དང་། རྩྭ༌[^512]ལ་སོགས་པ་སྦེངས་པ༌[^513]དང་ཤིང་ལ་སོགས་པ་འཐུ་བ་ལ་སོགས་པ་ལ་སྔར་བསྟན་པའི་ལྟུང་བྱེད་ནི་བྱེད་པ་པོ་ཉིད་དོ། །

[Block 858]
གང་ལ་རང་འཇུག་པ་དང་གཞན་འཇུག་དུ་འཛུད་པར་བྱེད་ན་རང་སྤྱད་པའི་དོན་ཉིད་ལ་ཡང་སྨྲས་པ་ནི་དེ་ལ་ཤེས་གཙོ་བོ་ཞེས་བྱ་བ་སྟེ། དེ་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་ཉིད་དོ། །

[Block 859]
གང་ལ་འདུ་ཤེས་གཙོ་ཆེར་བྱེད་པ་པོ་འདི༌[^514]ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྲོག་ཆགས་དང་བཅས་པ་ཉིད་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 860]
གང་གི་སྲོག་ཆགས་དང་བཅས་པ་ཉིད་ལ་ཞེ་ན་དེའི་ཕྱིར་ཆུ་དང་མར་དང་སྦྲང་རྩི་དང་བུ་རམ་གྱི་དབུ་བ་དང་འོ་མ་དང་ཞོ་དང་མར་སར་པ་དང་ཚྭ་དང་འབྲུའི་ཚ༌[^515]དང་ཞོ་ག༌[^516]ཆུ་དང་། རྩ་བ་མོ་དང་ཤིང་ཏོག་དང་བཅའ་བར་བྱ་བ་ལ་སོགས་པ་ཉེ་བར་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྲོག་ཆགས་དང་བཅས་པའི་ཆུ་ལ་ཞེས་བྱ་བ་ལ། ཆུའི་ཚིག་ནི་སོ་སོར་ཐར་པར་དཔེར་མཚོན་པ་ཙམ་དུ་ཟད་ཀྱི་འདི་ནི་སྐྱེ་བའི་དབང་གིས་གནས་ཡིན་ཏེ། ཆུ་འདི་ལ་ཤིན་ཏུ་མང་དུ་འཇུག་པ་འདི་ལ་ལྟུང་བའི་ཕྱིར་རོ། །

[Block 861]
ཉེ་བར་སྦྱར་བ་དེ་དག་སྲོག་ཆགས་ཇི་ལྟ་བུ་དང་བཅས་པ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྣང་བ་དག་གིས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 862]
འདིར་གང་གི་ཚེ་འདིའི་བྱེད་པ་པོ་ཉིད་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཤི་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་སྲོག་ཆགས་དུ་མ་ཤི་ན་ཡང༌[^517]ཁ་ན་མ་ཐོ་བ་གཅིག་གི༌[^518]བྱེད་པ་པོ་ཉིད་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་སྲོག་ཆགས་རེ་རེའི་འོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྲོག་ཆགས་ཇི་སྙེད་སྦྱོར་བ་དེའི་དབང་གིས་སྲོག་བཅད་དེ་དུས་བྱས་ན་དེ་ཉིད་ཁོ་ནའི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 863]
སླར་སྤྱོད་པ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྤྱོད་པ་ན་ལུས་ཀྱི་ཉེ་བར་སྤྱོད་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་ནི་སྤྱད་པ་མཚན་ཉིད་ཀྱི་སྒོ་ནས་བསྟན་ནས། ད༌[^519]ནི་ངོ་བོའི་སྒོ་ནས་བསྟན་པའི་ཕྱིར། འདི་ལྟ་སྟེ་ཁྲུས་དང་བཏུང་བ་དང་སོ་ཤིང་དོར་བ་དང་ལག་པ་དང་རྐང་པ་བཀྲུ་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ལུས་ཀྱི་ཡོ་བྱད་དག་ཏུ་ཉེ་བར་སྤྱོད་པ་གང་ཡིན་པ་དེ་ལུས་ཀྱིས༌[^520]ཉེ་བར་སྤྱོད་པ་ཁོ་ན་ཡིན་པར་ཤེས་པར་བྱའོ་ཞེས་བྱ་བའི་ཕྱིར་ཡོ་བྱད་དག་ཏུ་ཉེ་བར་སྤྱད་པ་གང་ཡིན་པ་དེ་ནི་ལུས་ཀྱིར༌[^521]ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གང་གི་ཡན་ལག་ཏུ་གང་བྱེད་པ་དེ་ཉིད་ལ་དེ་བྱས་པར་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 864]
སླར་ལུས་ཀྱི་ཡོ་བྱད་དེ་དག་གང་དག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བཟའ་བར་བྱ་བ་དང་ལྷུང་བཟེད་དང་ཆོས་གོས་དང་གནས་དང་སོ་བཀྲུ་བ་དང་མེ་ལ་སོགས་པ་ནི་ལུས་ཀྱི་ཡོ་བྱད༌[^522]ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 865]
འོ་ན་ལུས་ཀྱི་ཡོ་བྱད་རྣམས་སུ་ཉེ་བར་སྦྱར་བ་གང་ཡིན་པར་བལྟ་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་དེ་དག་ཏུ་ནི་ས་དང་ལྕི་བ་དང་ཚོན་དང་རྩྭ༌[^523]དང་ཤིང་ལ་སོགས་པའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 866]
ལུས་ཀྱི་ཡོ་བྱད་དེ་དག་ཏུ་ཉེ་བར་སྦྱར་བ་དེ་དག་ལ་ཆུ་ལ་སོགས་པ་དགོས་པ་གང་ཡིན་ཞེ་ན། དེའི་ཕྱིར་དེ་དག་ཏུ་དགོས་པ་ནི་འདི་ལྟ་སྟེ་བྱི་དོར་བྱ་བ་དང་ཁ་བསྒྱུར་བ་དང་ཆག་ཆག་གདབ་པ་དང་། ཕྱག་དར་བྱ་བ་དང་ཞལ་ཞལ་བྱ་བ་དང་འུ་ཤ་དང་ཐང་དང་ཐུག་པ་རྣམས་བཏུང་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྦྱོར་བ༌[^524]འདི་རྣམས་ཞེས་བྱ་བ་འོག་ནས་འབྱུང་བ་འདི་རྣམས་ལ་ཐམས་ཅད་དུ་སོ་སོར་མངོན་པར་སྦྱར་བར་བྱའོ། །

[Block 867]
ཆུ་སྲོལ་བཀག་པ་དང་བསལ་བ་དག་ཀྱང་ངོ་། །ཤིང་དང་གཡེང་བ་དག་གཞུག་པ་དང་དྲ་བ༌[^525]དང་བཤལ་བ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 868]
འདིར༌[^526]ཤིང་དང་གཡེང་བ་ཞེས་བྱ་བ་ནི་དཔེ་ཙམ་དུ་རིག་པར་བྱའོ། །

[Block 869]
རིམ་པ་གཅིག་པ་ལས་གཞན་པ་སྤུ་ཅན་ལ་སོགས་པ་བཀྲུ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ལ། རིམ་པ་གཅིག་པ་ལས་གཞན་པ་ཞེས་བྱ་བ་ཆིག་རྐྱང་ལས་སོ། །

[Block 870]
གཞན་པ་ཞེས་བྱ་བ་ལ། འདི་ནི་ངོ་བོ་ལས་སྟོན་པར་བྱེད་པ་སྤུ་ཅན་ལ་སོགས་པས་ཞེས་བྱ་བས་སོ། །

[Block 871]
དེ་ཡང་སྲོག་ཆགས་ཀྱི་ཁམས་ལྷག་པར་མང་བའི་ཆུ་ལྟ་བུ་ཡང་སྦྱོར་བ་དག་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ཡང་ཞེས་བྱ་བ་ནི་གོས་རིམ་པ་གཅིག་པ་དེ་ཡང་ངོ་། །ཆུ་ཞེས་བྱ་བ་ནི་བཀྲུ་བ་ཡང་ངོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 872]
དེ་ལྟ་བུ་ཡང་ཞེས་བྱ་བ་ནི་རྣམ་པ་དེ་ལྟ་བུ་ཡང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 873]
འདིར་གཞུང་ནི་དགེ་སློང་གིས་སྲོག་ཆགས་དང་བཅས་པའི་ཆུས་ཆག་ཆག་འདེབས་སམ་ཕྱག་དར་བྱེད་པ་དང་འུ་ཤ་དང་ཐང་དང་ཐུག་པ་དག་བྱེད་ན་སྲོག་ཆགས་ཇི་སྙེད་འཆི་བ་དང་དེ་སྙེད་ཀྱི་ལྟུང་བྱེད་དུ་འགྱུར་ལ། མ༌[^527]འཆི་ན་ནི་ཉེས་བྱས་སོ། །

[Block 874]
དགེ་སློང་གིས༌[^528]སྲོག་ཆགས་དང་བཅས་པའི་ཆུའི་ཡུར་བ་འགོག་གམ་སེལ་བར་བྱེད་ན་སྲོག་ཆགས་ཇི་སྙེད་འཆི་བ་དེ་སྙེད་ཀྱི་ལྟུང་བྱེད་དུ་འགྱུར་ལ་མི་འཆི་ན་ནི་ཉེས་བྱས་སོ། །

[Block 875]
དགེ་སློང་གིས་སྲོག་ཆགས་དང་བཅས་པའི་ཆུར་ཤིང་འཛུད་དམ་འདྲེན་ནམ། ཆུའི་ནང་ནས་སྐམ་སར་བཤལ་ལ་གཡེང་བས་གཡེང་བར་བྱེད་དམ་འདྲེན་ནམ་ཆུའི་ནང་ནས་སྐམ་སར་བཤལ་བར་བྱེད་ན་སྔ་མ་བཞིན་ནོ། །

[Block 876]
གོས་སྤུ་ཅན་དང་ལྷན་པ་ཅན་དག་ཤིང་གིས་བརྡུང་བ་དང་འཁྲུ་བར་བྱེད་ན་སྲོག་ཆགས་ཇི་སྙེད༌[^529]འཆི་བ་དེ་ཉིད་ཀྱི་ལྟུང་བྱེད་དུ་འགྱུར་ལ་མ༌[^530]འཆི་ན་ནི་ཉེས་བྱས་སོ། །

[Block 877]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གོས་སྤུ་ཅན་དང་ལྷན་པ་ཅན་དག་ཤིང་གིས་བརྡུངས་པ༌[^531]དང་བཀྲུ་བར་མི་བྱ་སྟེ་འཁྲུ་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ། །

[Block 878]
འོན་ཀྱང་རིམ་པ་གཅིག་པ་ནི་བཀྲུ་བར་བྱའོ། །

[Block 879]
དགེ་སློང་དག་གིས་བཀྲུ་བ་གཏན་བཏང་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གང་ན་སྲོག་ཆགས་ཀྱི་ཁམས༌[^532]མང་ལ་ཆུའི་ཁམས་ཉུང་བ་དེར་བཀྲུ་བར་མི་བྱའི་གང་ན་ཆུའི་ཁམས་མང་ལ་སྲོག་ཆགས་ཀྱི་ཁམས་ཉུང་བ་དེར་བཀྲུ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 880]
འདི་ནི་ཉེ་བར་ལོངས་མི༌[^533]སྤྱད་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
