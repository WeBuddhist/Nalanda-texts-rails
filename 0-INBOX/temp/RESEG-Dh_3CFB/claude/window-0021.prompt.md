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
གཅིག་པུ་དེས་དེ་རྣམས་ཀྱི་ཐ་སྙད་པ་ཉིད་སེལ་ཏམ། ཅི་སྟེ་ཐ་དད་པ་ཉིད་ནི་དེ་དག་ལ་གཅིག་གི་རྣམ་པར་ཤེས་པ་མི་བསྐྱེད་པ༌[^577]ཉིད་ཀྱི་རྒྱུ་ཡིན་པར་བརྗོད་དོ། །

[Block 737 [VERSE]]
གལ་ཏེ་དུ་མའང་གཅིག་ལྟོས་ནས། །
ཐ་དད་མིན་བློ་སྐྱེད་ཅེ་ན། །

[Block 738]
ཐ་དད་པའི་ཕྱིར་དུ་མས་གཅིག་གི་ཤེས་པ་མི་བསྐྱེད་དོ་ཞེས་ནི་མི་སྨྲ་སྟེ། ཐ་དད་པས་སྐྱེ་བ་ལ་འགལ་བ་མེད་དོ། །

[Block 739]
འོ་ན་ཅི་ཞེ་ན། བྲལ་བས་འགལ་ཏེ། དེས་ན་གཅིག་དང་ལྷན་ཅིག་པས་སྐྱེད་པར༌[^578]བྱེད་པ་ཁོ་ནའོ་ཞེ་ན། དེ་ལྟར་ན་འོ་ན་ནི།

[Block 740 [VERSE]]
དེ་དག་རེ་རེ་མེད་པར་ཡང་། །
དེ་གཅིག་གིས་ཀྱང་བསྐྱེད་བྱ་བའི། །
བློ་ལ་དེ་རྣམས་ནུས་མེད་ཕྱིར། །
བློ་ཡིས་འཛིན་པ་མེད་པ་ཡིན། །

[Block 741]
དེ་ནི་འདི་ལྟར༌[^579]ཤེས་པ་དེ་ལ་བསལ་བ༌[^580]རྣམས་ཀྱི་ནུས་པ་རྟོགས་ཏེ། དེ་རྣམས་ལས་རེ་རེ་མེད་ཀྱང་དེ་ཡོད་པའི་ཕྱིར་དང་། སྤྱི་མེད་ན་མེད་པའི་ཕྱིར་ལ་གཞན་དུ་མ༌[^581]ཡོད་པའི་ཕྱིར་རོ། །

[Block 742]
འདི་ནི་ཉེས་པ་མེད་དེ་ཇི་ལྟར་སྔོན་པོ་ལ་སོགས་པ་ལ་རེ་རེ་བསལ༌[^582]ཀྱང་མིག་གི་རྣམ་པར་ཤེས་པ་སྐྱེ་ལ་དེ་དག་གི་ཚོགས་པ་ལ་ཡང་ནུས་པ་མེད་པ་མ་ཡིན་པ་དེ་བཞིན་དུ་འདི་ལ་ཡང་སོ་སོར་རེ་རེ་བསལ་ན་ཡང་སྐྱེ་བས་དུས་ཐམས་ཅད་དུ་ནུས་པ་མེད་པ་མ་ཡིན་ནོ་ཞེ་ན། མི་མཐུན་པར༌[^583]ཉེ་བར་བཀོད་པ་སྟེ། འདི་ལྟར།

[Block 743 [VERSE]]
སྔོ་སོགས་མིག་གི་རྣམ་ཤེས་ལ། །
ནུས་པ་སོ་སོར་མཐོང་བའི་ཕྱིར། །
ཚོགས་ལའང་ནུས་གྲུབ་བསལ་བ༌[^584]ལས། །
ཇི་ལྟར་ཡང་ན་དེ༌[^585]ལྟར་མིན། །

[Block 744]
དབང་པོ་ལ་སོགས་པ་ལ་མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོ་སོའི་ནུས་པ་ཡང་མཐོང་བས་ཚོགས་པ་ལ་ཡང་ནུས་པ་མི་འགལ་ལོ། །

[Block 745]
བསལ་བ༌[^586]རྣམས་ནི་སྤྱི་ལ་མི་ལྟོས་པར་ནམ་ཡང་དེ་ལྟར་རྗེས་སུ་འགྲོ་བའི་རྣམ་པར་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 746]
དེ་ལྟ་བས་ན་བསལ་བ༌[^587]རྣམས་ཀྱིས་དེ་ལ་མི་ནུས་པ་ཁོ་ན་ཡིན་པས་དེ་རྣམས་མི་འཛིན་པར་འགྱུར་རོ། །

[Block 747 [VERSE]]
གལ་ཏེ་དེ་དག་འགའ་ཞིག་ལ། །
ལྟོས་ནས་དེ་ནུས་འབའ་ཞིག་མིན། །

[Block 748]
འོན་ཏེ་ཐ་ག་པ་ཐག་ཟོང༌[^588]མེད་པར་རས་ཡུག་མི་འཐག་ལ། ཐ་ག་པ་ཐག་ཟོང༌[^589]རེ་རེ་མེད་ཀྱང་འཐགས་པས༌[^590]དེ་ཁོ་ན་ལས་རས་ཡུག་འབྱུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 749]
དེ་བཞིན་དུ་བསལ་བ༌[^591]རེ་རེ་བསལ་བ་ལ༌[^592]རྣམ་པར་ཤེས་པ་སྐྱེ་བ་ལ་ཡང་སྤྱི་འབའ་ཞིག་པ་དེ་ནི་རྒྱུ༌[^593]མ་ཡིན་ནོ། །

[Block 750]
འོ་ན་ཅི་ཞེ་ན། བསལ་བ༌[^594]རྣམས་ཀྱི་ནང་ནས་གཅིག་འབའ་ཞིག༌[^595]ལ་ལྟོས་ནས་རྣམ་པར་ཤེས་པ་བསྐྱེད་དོ་སྙམ་དུ་སེམས་ན། དེ་ལྟ་ཡིན་ན།

[Block 751 [VERSE]]
དེ་དག་དེ་གཅིག་ལ་ཕན་ན། །
ཇི་ལྟར་བློ་གཅིག་ཉིད་མ་ཡིན། །

[Block 752]
དོན་ཐ་དད་པ་རྣམས་དོན་གཅིག་ལ་སྦྱོར་བ་འགལ༌[^596]བས་འདི་ཐམས་ཅད་བརྩམས་པ་ཡིན་ལ། གལ་ཏེ་བསལ་བ༌[^597]དེ་དག་ཀྱང་སྤྱི་གཅིག་ལ་ཕན་འདོགས་པར་བྱེད་ན། དེ་རྣམས་ལ་རྣམ་པར་ཤེས་པས་གང་གིས་ན་དེ༌[^598]མི་བསྐྱེད་པའི་ཉེས་པ་ཅི་ཞིག་བྱས། དེ་ལ་བར་མ་དོར༌[^599]ལྷག་མ་སྤྱིས་ཅི་ཞིག་བྱ་སྟེ། ཇི་ལྟར་འདི་དག་ཐ་དད་ཀྱང་སྤྱི་གཅིག་ལ་ཕན་འདོགས་པའི་ནུས་པ་ཡོད་པ་དེ་བཞིན་དུ་རྣམ་པར་ཤེས་པ་དེ་གཅིག་ཁོ་ན་བསྐྱེད་ལ་རག་མོད། གཞན་ཡང་།

[Block 753 [VERSE]]
འདི་དེ་རྣམས་ཀྱི་འབྲས་བུར་འགྱུར། །
ཕན་འདོགས་གང་ཡིན་བསྐྱེད་པ་ཡིན། །

[Block 754]
སྔོན་རོལ་བཞིན་དུ་བོགས་མེད་པའི་བདག་ཉིད་འཛིན་པ་འདི་ལ་ནི་ཕན་པ་ཞེས་བྱ་བ་འགའ་ཡང་མེད་ན།[^600] ཧ་ཅང་ཐལ་བར་འགྱུར་རོ། །

[Block 755]
དོན་འགའ༌[^601]ཞིག་བསྐྱེད་ན་ནི་དེས་དེ་ལ་ཅི་ཞིག་བྱེད། །དེ་དེའི་རྟེན་ཉིད་ཡིན་དུ་ཕན་འདོགས་པ་མེད་པ་ལ་རྟེན་དང་བརྟེན་པའི་དངོས་པོ་འདི་ཅི་ཞིག་ཡོད།[^602] ཡང་ན་ནི་ཧ་ཅང་ཐལ་བར་འགྱུར་རོ། །

[Block 756]
ཕན་འདོགས་ན་ཡང་དེ་ཁོ་ན་ལ་དེ་འབྲེལ་པས་དེ་བྱེད་པའི་ཕྱིར་དེ་ལ་ཕན་པར་བྱེད་པ་གཞན་ཅི་དགོས། དེ་ལ་ལྟོས་པའི་རྟེན་གྱིས་དེ་ལ་སྦྱོར་ན་ནི་ཕན་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་ལ་ལྟོས་པ་ཞེས་བྱ་བ༌[^603]འདི་ཅི་ཞིག་ཡོད་དེ། དེ་ལས་སྐྱེ་བའི་ཆོས་ཅན་ནི་རང་བཞིན་འབྲེལ་པའི་ཕྱིར་ལྟོས་པ་ཞེས་བྱའོ། །

[Block 757]
བོགས་དབྱུང་དུ་མེད་པ་ཅན་གྱི་བདག་ཉིད་ཅན་ཡང་ཡིན་ལ། གཞན་དག་ལ་ལྟོས་སོ་ཞེས་བྱ་བ་འདི་ནི་ཉམས་པ་ཡིན་ནོ། །

[Block 758]
དེ་ལྟ་བས་ན་གང༌[^604]ཅུང་ཟད་འགའ་ཞིག་ལ་ལར་འབྲེལ་པ་དེ་ཐམས་ཅད་ནི་བསྐྱེད་པར་བྱ་བའི་ཁོངས་སུ་གཏོགས་སོ། །

[Block 759]
གཞན་གྱི་དངོས་པོ་བསྐྱེད༌[^605]ན་ནི་དེ་ལ་ཕན་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 760]
ཅུང་ཟད་ཀྱང་མི་བྱེད་པ་ལ་ཡང་ཕན་པར༌[^606]མེད་པའི་ཕྱིར་རོ། །

[Block 761]
དེའི་ཕྱིར་བསལ་བས༌[^607]ཕན་བཏགས་པའི་སྤྱིས་རྣམ་པར་ཤེས་པ་བསྐྱེད་ན་འདི་འདིའི་འབྲས་བུ་ཉིད་དུ་འགྱུར་བར་གསལ་ལོ།[^608] །འགའ་ཞིག༌[^609]གིས་ནུས་ན་ནི་བསལ་བ༌[^610]རྣམས་ཀྱིས་ནམ་ཡང་གང་ལ༌[^611]ཡང་ནུས་པར་མ་གྲུབ་པའི་ཕྱིར་གཟུང་བར་བྱ་བ་ཉིད་མ་ཡིན་ནོ། །

[Block 762]
གལ་ཏེ་རྣམ་པར་ཤེས་པ་ལ་སྣང་བའི་ཕྱིར་བསལ་བ༌[^612]རྣམས་ཀྱིས་ནུས་སོ་ཞེ་ན། ཕན་འདོགས་པར་མ་གྲུབ་པ་ཅན་རྣམས་ཇི་ལྟར་སྣང་སྟེ་དེ་ཉིད་སྤྱི་ཁས་ལེན་ན་བསམ་པར་བྱ་བ་ཡིན་ནོ། །

[Block 763]
འདི་ལྟར་ཕན་པར་བྱེད་པ་མ་ཡིན་པ་ནི་ཡུལ་མ་ཡིན་ཏེ། ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 764]
ཡུལ་མ་ཡིན་པ་ནི་རྣམ་པར་ཤེས་པ་ལ་མི་སྣང་ངོ་། །གལ་ཏེ་ཕན་པ་མེད་པ་ཡུལ་ཉིད་མ་ཡིན་ན་འདས་པ་ལ་སོགས་པ་ཡུལ་ཉིད་མ་ཡིན་ཏེ། མེད་པ་རྣམས་ལ་ཕན་འདོགས་པའི་མཐུ་མེད་པའི་ཕྱིར་རོ་ཞེ་ན། དེ་དག་གི་ཤེས་པ་རྣམས་ཡུལ་མེད་དུ་ཟད་མོད། ཡུལ་མེད་དུ་ཟད༌[^613]ཀྱང་ཉམས་སུ་མྱོང་བ་དེ་ལྟ་བུས་གཞག་པའི་བག་ཆགས་ལས་སྐྱེ་བའི་ཕྱིར་དེའི་རྗེས་སུ་བྱེད་པ་ནི་རྣམ་པར་ཤེས་པའི་བདག་ཉིད་དུ་གྱུར་པ་ཁོ་ན་ཡིན་ནོ། །

[Block 765]
ཡོད་པ་དང་མེད་པའི་རྗེས་སུ་བྱེད་པའི་ཕྱིར་ནུས་པ་ཡིན་གྱི་སྣང་བའི་ཕྱིར་ནི་མ་ཡིན་ཏེ། བསལ་བ༌[^614]ལ་མ་གཏོགས་པ་སྤྱི་མི་སྣང་བའི༌[^615]བྱེད་པ་ཡོད་པའི་ཕྱིར་དང་། སྒྲ༌[^616]ལ་སོགས་པ་ཉམས་པར་སྣང་ཡང་དེ་རྣམས་ལ་བྱེད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 766 [VERSE]]
གལ་ཏེ་ཐ་དད་མི་སྣང་བློ། །
ཐ་དད་རྣམས་ལ་མི་འདོད་ན། །

[Block 767]
དུ་མས་འབྲས་བུ་གཅིག་མི་བྱེད་དོ་ཞེས་ནི་མི་སྨྲའོ། །

[Block 768]
འོ་ན་ཅི་ཞེ་ན། དོན་ཐ་དད་པ་རྣམས་ལ་དེ་དག་གི་རྣམ་པར་གཞག་པ་ཅན་གྱིས༌[^617]བློ་ཐ་མི་དད་པར་སྣང་བར་མི་འགྱུར་རོ། །

[Block 769]
སྤྱི་འཛིན་པ་རྣམས་ལ་ནི་རང་གི་མཚན་ཉིད་མི་སྣང་བ་ཉིད་དེ། དེ་མེད་ཀྱང་དེ་དག་ཡོད་པའི་ཕྱིར་དང་། རང་གི་རྣམ་པར་ཤེས་པ་ལ་རྣམ་པ་གཞན་དུ་སྣང་བའི་ཕྱིར་དང་། གཅིག་ལ་རྣམ་པ་དུ་མ་མི་རུང་བའི་ཕྱིར་དང་། ཧ་ཅང་ཐལ་བར་འགྱུར་བའི༌[^618]ཕྱིར་རོ། །

[Block 770]
དེའི་ཕྱིར་འདི་ནི་དེ་ལས་བྱུང་ཞིང་དོན་ཐ་དད་པ་འཛིན་པ་ཡིན་ན་ཐ་མི་དད་པར་སྣང་བར་མི་འགྱུར་རོ། །

[Block 771]
དེ་མི་སྣང་བས་ཀྱང་ལྷག་པར་ཞེན་པའི་འཁྲུལ་པས་འཇིག་རྟེན་ཐ་སྙད་འདོགས་པར་བྱེད་དོ། །

[Block 772]
དེ་ལ་སྣང་བའི་རྣམ་པ་དེ་དོན་རྣམས་ལ་མེད་དེ། ཐ་དད་པའི་ཐ་མི་དད་པ་ནི་མ་གཏོགས་སོ། །

[Block 773]
དེ་ནི་མེད་པའི་ངོ་བོ་ཡིན་ཏེ། དེས་དེ་ཁོ་ན་འཛིན་པ་ན་དེ་ལྟར་བསླད་པར་འགྱུར་རོ་ཞེས་སྔར་བཤད་ཟིན་ཏོ། །

[Block 774]
གཞན་ཡང་སྤྱི་དངོས་པོར་སྨྲ་བའི། །ལྟར་ན་ཡང་གསལ་བ་རྣམས་ཐ་དད་པ་ཁོ་ན་ཡིན་ན་ཇི་ལྟར་དེ་དག་ལ་བློ་རྣམ་པ་ཐ་མི༌[^619]དད་པ་ཅན་ཡིན་ཏེ། ཀླན་ཀ་མཚུངས་སོ། །

[Block 775]
མཚུངས་པ་མ་ཡིན་ཏེ། དེ་ལ༌[^620]སྤྱི་ཐ་མི་དད་པའི་ཕྱིར་རོ་ཞེ་ན། དེ་ལ་དེ་ཡོད་ཀྱང་སྣང་བ་མི་རྟོགས་པ་མ་ཡིན་ནམ། དེ་ནི་ཁ་དོག༌[^621]དབྱིབས་སུ་སྣང་བར་ལྡན་པར་ཡིད་ཆེས་སོ། །
--- END BLOCKS ---
