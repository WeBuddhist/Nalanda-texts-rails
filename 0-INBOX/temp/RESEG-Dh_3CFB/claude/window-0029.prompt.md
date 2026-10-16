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
གལ་ཏེ་འཕྲོད་པ་འདུ་བ་མངོན་པར་བསལ་བ་ཡིན་ནོ་ཞེ་ན། དེའི་ལན་ནི་དེའི་འཕྲོད་པ༌[^864]འདུ་བ་ནི་མི་རུང་བའི་ཕྱིར་རོ་ཞེས་བྱ་བས་བཤད་ཟིན་ཏོ། །

[Block 1017]
འདི་ནི་བསལ་བ་དང་ལྷན་ཅིག་འཕྲོད་པ་འདུ་བ་ཙམ་དུ་སྐྱེས་པ་ཡིན་གྱི༌[^865]ཁྱད་པར་འགའ་ཞིག་ཀྱང་མ་ཡིན་པ་སྔ་མ་བཞིན་དུ་ཕྱིས་ཀྱང་ཤེས་པའི་རྒྱུ་ཉིད་དུ་མི་འགྱུར་རོ། །

[Block 1018]
འཕྲོད་པ་འདུ་བ་ཁོ་ན་ལས་ཤེས་པའི་རྒྱུ་ཉིད་ཡིན་ན་ནི་གཞན་རང་གི་རྟེན་ལ་འཕྲོད་པ་འདུ་བ་དག་ཀྱང་མཐོང་བར་འགྱུར་བ་དེ་བས་ན་བསལ་བར་བྱེད་པ་ཉིད་ནི་ཤེས་པའི་རྒྱུ་ཉིད་ཡིན་ནོ། །

[Block 1019]
དེ་ཡང་སྒྲོན་མ་ལ་སོགས་པ་དང་འདྲ་བའི་ཕྱིར། ཐལ་བར་འགྱུར་བ་དེ་ཉིད་དོ། །

[Block 1020]
དེ་བས་ན་སྤྱིའི་གནས་པ་ནི། རྟེན་མ་ཡིན་པ་དང་། བསལ་བ་མ་ཡིན་པས་ན་མི་གནས་པའི་ཕྱིར་ཤེས་པའི་རྒྱུ་མ་ཡིན་ནོ། །

[Block 1021]
དེ་ཉིད་ཀྱི་ཕྱིར།

[Block 1022 [VERSE]]
རིགས་ནི་གསལ་བ་ལས་གཞན་ནམ། །
གཞན་མིན་ཡོད་ཉིད་གང་དེ་དག །
སྔོན་མིན་གསལ་བ་དག་ལ་ནི། །
ཇི་ལྟར་སྤྱི་ནི་རྟོགས་པ་ཡིན། །

[Block 1023]
ཉིད་ཀྱི་སྒྲ་ནི་ཡོད་པ་ཁོ་ནའོ་ཞེས་ངེས་པར་བཟུང་བའི་དོན་ཏོ། །

[Block 1024]
དངོས་པོ་ཡོད་པ་ནི་རང་གི་ནུས་པ་ཉིད་ཀྱིས་གཞན་ལ་རང་གི་ངོ་བོའི་རྗེས་སུ་བྱེད་པ་ཅན་གྱི་བློ་སྐྱེད་པར་བྱེད་པ་དེ་དང་འབྲེལ་པ་ལ་རག་ལུས་པ་ཡིན་གྱི། གཞན་དུ་ན་ཧ་ཅང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1025]
དེ་ཡང་སྤྱི་ཡོད་པ་ནི་དེ་ཉིད་གཞན་གྱི་ཕྱོགས་ལ་ཡོད་པ་མ་ཡིན་ཏེ།

[Block 1026 [VERSE]]
གཅིག་ལ་ཡོད་པ་མཐོང་བ་ནི། །
གཞན་ལ་མཐོང་བ་མི་སྲིད་ཕྱིར། །

[Block 1027]
གལ་ཏེ་བློ་གཅིག་ཏུ་འབྱུང་བ་ཅན་དེ་ནི་བསལ་བ་གཞན་ལ་དེ་ལྟར་འགྲོ་ཞིང་ཡང་དག་པར་འཛིན་པ་ཡིན་ན། [^866]དེ་ལ་མཐོང་བ་ཅུང་ཞིག་གཞན་ལ་མཐོང་བར་འགྱུར་ན། དེ་ཡང་།

[Block 1028 [VERSE]]
གཞན་ཉིད་མིན་ན་རྗེས་འགྲོ༌[^867]མེད། །
གཞན་ཉིད་ན་ཡང་མི་རྟེན་ཕྱིར། །

[Block 1029]
ཡོད་པ་མི་སྲིད་དོ། །

[Block 1030]
རང་བཞིན་གྱི༌[^868]དེ་ཉིད་དམ་གཞན་ཉིད་ནི་རང་བཞིན་ལས་འདས་པ་མ་ཡིན་ཏེ། ངོ་བོ་དེར་གྱུར་པ་མ་ཡིན་པ་ནི་གཞན་ཉིད་ལས་མ་འདས་པའི་ཕྱིར་རོ། །

[Block 1031]
གཟུགས་ཀྱི་གཞན་འདི་ཉིད་གང་ཡིན་པ་དེ་ཉིད་མ་ཡིན་ཏེ། རྣམ་པ་གཞན་བཞིན་དུ་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 1032]
གལ་ཏེ་སྤྱིའི་ངོ་བོ་དེ་བཞིན་ཉིད་མ་ཡིན་ན་དེ་ཉིད་དེར་འགྱུར་ཏེ། དེ་ཉིད་མ་ཡིན་པ་དངོས་པོ་གཞན་དང་འདྲ་བར་གཞན་ཉིད་དུ་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1033]
བསལ་བའི་རང་བཞིན་གཅིག་ནི་བསལ་བ་གཞན་ལ་རྗེས་སུ་འགྲོ་བ་མ་ཡིན་ཏེ། བསལ་བ་གཞན་ཉིད་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1034]
དེ་བས་ན་སྤྱི་ཐ་དད་པ་མེད་པ་ལས་བློ་རྗེས་སུ་འགྲོ་བར་མི་འགྱུར་ཞིང་། ཐ་དད་པ་ལས་ཀྱང་མ་ཡིན་ཏེ། དེ་འགའ་ཞིག་ལ་ཡང་བརྟེན་པ༌[^869]མེད་པའི་ཕྱིར་རོ། །

[Block 1035]
འགའ་ཞིག་གིས་ཕན་བཏགས་པ་མེད་པར་རག་ལུས་པ་མེད་པས་ན་བསལ་བར་བྱ་བ་དང་། བསལ་བར་བྱེད་པའི་ངོ་བོ་ལ་སོགས་པ་ལས་འབྲེལ་པ་གཞན་ཡང་མེད་པའི་ཕྱིར་འབྲེལ་པ་མེད་པ་ཅན་ལས་ཀྱང་ཤེས་པ་སྐྱེ་བར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 1036]
དེ་བས་ན་དངོས་པོ་གཅིག་མཐོང་བས་གཅིག་ལ་གནས་པའི་ཤེས་པ་གཞན་ལ་གནས་པ༌[^870]འདོད་པ་འདིའི་དེ་ཉིད་དང་། གཞན་ཉིད་ལས་འདས་པའི་ཕྱིར་དེ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 1037]
དེའི་ཕྱིར་དོན་རྣམས་ལ་ངོ་བོ་གཅིག་ཏུ་རྟོགས་པ་འདི་ནི་རྣམ་པར་རྟོག་པའི་བག་ཆགས་ཀྱིས་ཀུན་ནས་བསླང་བ་འཁྲུལ་པ་ཁོ་ན་ཡིན་ཏེ། དངོས་པོ་ཐ་དད་པ་དང་། བག་ཆགས་ཀྱི་རང་བཞིན་ནི་དེའི་རྟེན་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ནི་དཔྱད་ཟིན་ཏོ། །

[Block 1038]
འོ་ན་ནི་གཙོ་བོ་དང་དབང་ཕྱུག་ལ་སོགས་པའི་འབྲས་བུའི་སྒྲ་དག༌[^871]ནི་དངོས་པོ་ཐ་དད་པར་འགྱུར་བ་མེད་པ་ཅན་ལ་ཇི་ལྟར་ཐ་དད་པ་མེད་པར་འཇུག་པར་འགྱུར། དེ་དག་ཀྱང་བརྡ་ཇི་ལྟ་བ་བཞིན་དུ་རྒྱུད་བག་ཆགས་ཀྱིས་ལེགས་པར་བྱས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 1039]
དོན་ཐམས་ཅད་མཐོང་བ་ན་དེ་ལས་ཐ་དད་པ་ལ་ལྟོས་པ་མེད་དུ་ཟིན་ཀྱང་དེ་ལྟར་ངེས་པར་བྱས་པ་ལས་དེ་ལྟ་བུ་མ་ཡིན་པ་ནི་རྣམ་པར་རྟོག་པ་རྣམ་པར་བཅད་ནས་ཉེ་བར་ལེན་པའི་སྟོབས་ཀྱིས་འབྱུང་བའི་རྣམ་པར་རྟོག་པ་ཅན་གྱིས༌[^872]ཀུན་ནས་བསླང་བ་དག་ནི་རྣམ་པར་རྟོག་པའི་རྣམ་པར་ཤེས་པའི་སྣང་བའི་དོན་ལ་འཇུག་པར་འགྱུར་གྱི། དེ་ལྟར་ཡོད་པ་མ་ཡིན་པ་དེ་དག་ལ་ནི་སྤྱི་ཐ་དད་པའམ། ཐ་དད་པ་མ་ཡིན་པ་ཅུང་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ནོ། །

[Block 1040]
དེ་ལྟ་བུར་གྱུར་པའི་རྣམ་པར་རྟོག་པ་གཞན་ལས་ཐ་དད་པ་ཡང་རྟོགས་པ་པོའི་བསམ་པའི་དབང་ལས་འགྱུར་རོ། །

[Block 1041]
གལ་ཏེ་དེའི་བསམ་པ་ཁོ་ན་ལས་ཅིའི་ཕྱིར་སྤྱིར་མི་འགྱུར་ཞེ་ན། དེས་ནི་འདི་གདོན་མི་ཟ་བར་མེད་ན་མི་འབྱུང་བ་ཉིད་ཀྱི་ཕྱིར་ཐ་དད་པར་འདོད་པར་བྱ་བ་ཡིན་ན་དེ་ཉིད་ནི་སྤྱིའི་འབྲས་བུའི་ནུས་པ་ཡིན་པའི་ཕྱིར། སྤྱི་རྟོག་པ་ནི་དགོས་པ་མེད་པ་ཡིན་ནོ། །

[Block 1042]
གལ་ཏེ་དངོས་པོ་ཡོད་པའམ་མེད་པ་དག་ལ་སྤྱིའི་བློ་འདི་ནི་དོན་དང་ལྡན་པ་མ་ཡིན་གྱི་བསླད་པ་ཁོ་ན་ཡིན་པའི་ཕྱིར། ཁོ་བོ་ཅག་འདིའི་ཡུལ་དཔྱོད་པ་ལ་གུས་པ་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 1043]
འགའ་ཞིག་ལ་འདིའི་མི་སླུ་བ༌[^873]ནི་དངོས་པོ་ལ་རྒྱུ་དང་འབྲས་བུའི་ངོ་བོའི་འབྲས་བུའི༌[^874]འབྲེལ་པ་ལས་ཡིན་གྱི། དེ་ལྟ་བུར་གྱུར་པའི་གཟུང་བ་ངེས་པ་ལས་ནི་མ་ཡིན་ཏེ། མངོན་སུམ་གྱིས་ཉམས་སུ་མྱོང་བ་བཞིན་ནོ། །

[Block 1044]
དེ་ལྟར་ཡོད་པ་མ་ཡིན་ཡང་ཡོད་པའི་ཕྱིར་རོ་ཞེས་བསྟན་པར་བྱ་བ་དང་བསྟན་ཟིན་པ༌[^875]ཡིན་ནོ། །

[Block 1045]
ཐ་དད་པའི་ཡུལ་ཅན་འདི་ཡང་ཕལ་ཆེར་དངོས་པོ་ཐ་དད་པའི༌[^876]མཐོང་བའི་སྟོབས་ཀྱིས་དེ་དག་ལ་དངོས་པོར་ངེས་པའི་ཕྱིར་རོ། །

[Block 1046]
དེ་ལྟ་བུའི་ངོ་བོར་བརྟགས་ལ༌[^877]ཉིད་ནི་གཞན་ལ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 1047]
གཞན་ཡང་སྤྱི་དོན་གཞན་དུ་རྟོག་པ་འདི་རང་གི་རྟེན་ཙམ་ལ་ཡོད་པའམ། ནམ་མཁའ་ལ་སོགས་པ་འདྲ་བ་ཐམས་ཅད་ན་ཡོད་པར་རྟོག་པར་འགྱུར་གྲང༌[^878]ན། དེ་ལ་གལ་ཏེ་རང་གི་རྟེན་ཙམ་ལ་ཡོད་པ་དེའི་ཚེ། ཕྱོགས་བུམ་པ་ལ་སོགས་པས་སྟོང་པ་དག་ཏུ་བུམ་པ་ལ་སོགས་པ་འབྱུང་བ་ན་ཇི་ལྟར་ཡུལ་ཐ་དད་པ་ཅན་གྱི་རྫས་ལ་ཡོད་པའི་སྤྱི་ནི་དེ་དག་ལ་ཡོད་པར་འགྱུར་ཏེ། རང་གི་ཕྱིར་དེ་ནི་རྫས་སྔ་མ་ལས༌[^879]འགྱུར་བའི་རྫས་ལ་མི་འགྲོ་སྟེ། བྱ་བ་མེད་པ་ཉིད་དུ་ཁས་བླངས་པའི་ཕྱིར་རོ། །

[Block 1048]
གང་གི་ཕྱིར་གཞན་ན་གནས་པའི་དངོས་པོ་དེ་ལས་མི་གཡོ་བ་དེ་གཉི་གའི་བར་ལ་ཁྱབ་པ་མ་ཡིན་པ་ནི་ཡུལ་ཐ་དད་པའི་དངོས་པོ་དང་ལྡན་པར་རིགས་པ་མ་ཡིན་ནོ།[^880] །སྔ་མ། དེ་ནི་དེ་ན་ཡོད་པ་མིན། །ཕྱིས་ཡོད་མིན་ན་ཡང་། དེ་ལ་ཡང་སྐྱེ་བ་མེད་པས་འགའ་ཞིག་ལས་འོངས་པ་མེད་པ་དེ་ལྟར་ན། བླུན་པོ་ལས་གཞན་དུ་འགལ་བའི་ཁུར་འདེགས་པར་སུས་ནུས། གཞན་ཡང་ཆ་ཅན་མིན། རྟེན་སྔ་མ་ནི་སྤོང་མི་བྱེད་པ་སྟེ། སྐྱེ་བར་འགྱུར་བའི་ཡུལ་ལས་ཐ་དད་པའི་ཡུལ་ཏེ། དེ་དག་ལ་གནས་པ་ཞེས་བྱ་བ་ཡང་། ཨེ་མའོ་ཕོངས་པའི་རྒྱུ་ཉིད༌[^881]ཡིན། ཡུལ་ཐ་དད་པའི་དངོས་པོ་དག་གི་འབྲེལ་པ་ཅན་ནི་ཡན་ལག་དུ་མའི་བདག་ཉིད་ཅན་ནམ། གཅིག་གི་བདག་ཉིད་ཅན་གྱིས་རྣམ་པ་གཉིས་སུ་འགྱུར་ཏེ། ཡན་ལག་གཞན་དང་གཞན་དག་གིས་དེ་དང་འབྲེལ་པའི་ཕྱིར། སྣང་བ་དང་ཐག་པ་དང༌[^882]དབྱིག་པ་ལྟ་བུའོ། །

[Block 1049]
ཡན་ལག་དང་བཅས་པ་མ་གཏོགས་པར༌[^883]ཡུལ་ཐ་དད་པ་དག་དང་འགའ་ཞིག་གིས་ཀྱང་ཅིག་ཅར་འབྲེལ་པ་རིགས་པ་མ་ཡིན་ཏེ། དེ་ལ་བདག་ཉིད་གཉིས་མེད་པའི་ཕྱིར་རོ། །

[Block 1050]
བདག་ཉིད་གཅིག་ལ་ཡང་ས་ཕྱོགས་དེར་གནས་པའི་འབྲེལ་པ་ཅན་གྱི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་ཏེ། གཞན་དུ་ན་དེ་དང་འབྲེལ་པ་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 1051]
བརྟེན་པ་གཅིག་པོ་གང་ལ་གནས་པ་དེ་ཉིད་ཀྱི༌[^884]ཚེ་བདག་ཉིད་དེས་དེ་ལ་གནས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་དེ་ནི་གཅིག་པོ་དེ་ལ་གནས་པ་དང་མི་གནས་པ་བདག་ཉིད་འགལ་བའི་ཕྱིར། རིགས་པ་མ་ཡིན་ནོ། །

[Block 1052]
གལ་ཏེ་ཐམས་ཅད་ལ་ཐམས་ཅད་དུ་རྣམ་པ་ཐམས་ཅད་ཀྱིས་གནས་པའི༌[^885]བདག་ཉིད་ཅན་ཡིན་ནོ་ཞེ་ན། དེ་ནི་རང་བཞིན་མཐོང་བའི་རྟེན་གྱི་ཤེས་པ་ནི་ཐམས་ཅད་ལ་རྣམ་པ་ཐམས་ཅད་དུ་འགྱུར་ལ། དེ་ལྟར་ན་ཡང་བ་ལང་ལ་ཡང་རྟ་ཡིན་ནོ་ཞེས་ཤེས་པར་འགྱུར་ཏེ། རྟ་ལ་གནས་པའི་བདག་ཉིད་ཅན་གྱི་རྫས་ཉིད་དང་འབྲེལ་པའི་ཕྱིར་དང་། དེའི་རང་བཞིན་རྟོགས་པས་དེ་ལྟར་རྣམ་པར་ངེས་པའི་ཕྱིར་དང་། གཅིག་པོ་དེ་ལ་ཡང་མ་མཐོང་བའི་རྣམ་པ་གཞན་མེད་པའི་ཕྱིར་རོ། །

[Block 1053]
དེའི་ཕྱིར་ཆ་མེད་པ་ཡུལ་དུ་མ་ལ་ཅིག་ཅར་བརྟེན་པ་མ་ཡིན་ནོ། །

[Block 1054]
རྟེན༌[^886]སྔ་མ་སྤངས་ནས་ཀྱང་ཡུལ་ཐ་དད་པ་ལ་གནས་པ་དེ་ཡང་མངོན་པར་འདོད་པ་མ་ཡིན་ནོ། །

[Block 1055 [VERSE]]
གཞན་པ༌[^887]གནས་པར་འགྱུར་བ་ནི། །
རང་གི་གནས་ལས་མི་གཡོ་བ། །
དེ་ལས༌[^888]གནས་གཞན་སྐྱེ་བ་ལ། །
གནས་ཤེས་ཤིན་ཏུ་རིགས་པར་ལྡན། །
--- END BLOCKS ---
