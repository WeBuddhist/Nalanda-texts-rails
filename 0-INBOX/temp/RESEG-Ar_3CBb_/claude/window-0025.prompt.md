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
བསྟན་པ་འདི་དག་གང་ཞིག་གང་གིས་ཇི་ལྟར་ཡོངས་སུ་སྣང་བ་དེ་ལྟར་གནས་པ་ནི་མེད་དོ།[^419] །

[Block 877]
དེ་ཅིའི་ཕྱིར་ཞེ་ན། ཐམས་ཅད་རོ་གཅིག༌[^420]པའི་རང་བཞིན་ཅན་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 878]
རིགས་པ་འདིས་ནི་ཞེས་པ་ནི་མི་སླུ་བར་བྱེད་པའི་ཚད་མ་དེ་ལྟ་བུ་ཡོད་པའི་ཕྱིར་རོ་ཞེས་སོ།

[Block 879]
[^421] །འོ་ན་དེ་ལྟར་བསྟན་པ་ལ་དགོས་པ་ཅི་ཡོད་ཅེ་ན། ལས་དང་པོ་པའི་སེམས་ཅན་རྣམས་འཇུག་པར་བྱ་བའི་ཕྱིར་ཞེས་པ་ནི་ལས་དང་པོ་པ་ནི་འཇིག་རྟེན་པ་དང་མཐུན་པའི་ཆོས་ལ་འཇུག་པར་འགྱུར་རོ། །

[Block 880]
འཇིག་རྟེན་ན་ནི་རྒྱལ་པོ་དང་། འཁོར་དང་ཞུ་བ་པོ་ལ་སོགས་པ་སྣང་བར་བྱ་བ་དང་མི་མཐུན་པར་སྟོན་ཏོ། །

[Block 881]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་སྡུད་པ་པོ་ལ་སོགས་པ་ཡོངས་སུ་བསྟན་པ་ཉིད་དོ། །

[Block 882]
གཞན་ཡང་གང་གི་ཕྱིར་སྟོན་པ་དང་སྡུད་པ་པོ་ལ་སོགས་པ་མ་བསྟན་ན་མེད་པར་ཡོངས་སུ་རྟོགས་པར༌[^422]འགྱུར་རོ། །

[Block 883]
གང་ལ་གང་མེད་པ་དེ་ནི་འཇིག་རྟེན་པའི་བྱ་བ་དང་མི་མཐུན་པར་བསྟན་ཏོ། །

[Block 884]
གང་ཞིག་གང་དང་མི་མཐུན་པ་དེ་ལ་ནི་གང་ཟག་དད་པའི་རྗེས་སུ་འབྲང་བ་རྣམས་ཡོངས་སུ་ཚོལ་བར་བྱེད་དོ། །

[Block 885]
གང་ཞིག་གང་ཡོངས་སུ་ཚོལ་བར་བྱེད་པ་དེས་ནི་སྲིད་པར་འཛིན་པ་ཡོངས་སུ་སྤངས་པར་འགྱུར་རོ། །

[Block 886]
གང་ཞིག་གང་གིས་ཡོངས་སུ་སྤངས་པ་དེས་ནི་དེའི་དོན་ལ་སོམ་ཉི་ཟ་བར་འགྱུར་རོ། །

[Block 887]
གང་ལ་གང་གིས་ཇི་ལྟར་སེམས་པ་དེས་ནི་སྐུར་བ་འདེབས་པར་འགྱུར་རོ། །

[Block 888]
གང་ལ་གང་གིས་གང་ཞིག་བྱས་པ་དེས་ནི་ངན་སོང་གསུམ་པོ་ཡོངས་སུ་བླང་བར༌[^423]འགྱུར་ཏེ། གསང་བའི་བདག་པོ་དོན་རྒྱས་པའི་ཞེས་བྱ་བ་ལ་སོགས་པའི༌[^424]ཚིགས་སུ་བཅད་པ་དུ་མ་དག་གིས་ཀྱང་ལེགས་པར་བསྟན་པ་ཡིན་ཏེ། དེའི་ཕྱིར་སངས་རྒྱས་ཀྱི་རོལ་མོ་ཇི་སྐད་དུ་བཤད་པ་འདི་བསྟན་པ་ཡིན་ནོ། །

[Block 889]
དེ་ཡང་གང་ལས་ཤེས་ཤེ་ན་གསེར་འོད་དམ་པ་ལས།

[Block 890]
སངས་རྒྱས་མྱ་ངན་མི་འདའ་ཞིང་། །ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ་སངས་རྒྱས་མྱ་ངན༌[^425]མི་འདའ་བ་ནི་རྟག་པ་ཆེན་པོའི་བདག་ཉིད་ཅན་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 891]
ཆོས་ཀྱང་ནུབ་པར་མི་འགྱུར་ཏེ། །ཞེས་པ་ནི་སེམས་ཅན་ལ་སྣང་བ་འབའ་ཞིག༌[^426]ཏུ་ཟད་ཀྱིས་ངེས་པར་ཆོས་ནུབ་པ་མེད་པར་འགྱུར་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 892]
འོ་ན་གང་གི་ཕྱིར་འབྱུང་ཞེ་ན།

[Block 893 [VERSE]]
སེམས་ཅན་རྣམས་ནི་གདུལ་བའི་ཕྱིར། །
བྱུང་ནས་མྱ་ངན་འདའ༌[^427]བར་སྟོན། །

[Block 894]
ཞེས་པ་ནི་དུས་ཉེ་བར་ལེན་པ་ཉིད་དེ་གང་གི་ཕྱིར་སེམས་ཅན་སྒྲིབ་པ་ཐམས་ཅད་དང་ལྡན་ཞིང་བློ་མ་སྨིན་པར་གྱུར་པ་དག་གི་ཕྱིར་དང་པོ་འབྱུང་བ་དང་། མཛད་པ་མཐར་ཕྱིན་པ་ལ་སོགས་པ་ནས་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བའི་བར་དུ་ཡོངས་སུ་རྫོགས་པར་བྱ་བའི་ཕྱིར་ཀུན་དུ་སྣང་བར་གྱུར་ཏོ། །

[Block 895]
དེ་བས་ན་ཞེས་པ་ནི་རིགས་པ༌[^428]དེའི་ཕྱིར་ཞེས་པའོ། །

[Block 896]
བརྒྱ་བྱིན་གྱིས་གསོལ་བ་ཞེས་པ་ནི་འདི་སྐད་ཅེས་བྱ་བ་ལ་སོགས་པའི་ཡི་གེ་གཉིས་ཡོངས་སུ་མ་ཤེས་ནས་དྲིས་པའོ། །

[Block 897]
ཅིའི་ཕྱིར་འདི་སྐད་ཅེས་བྱ་བའི༌[^429]ཞེས་པ་ནི་འདི་སྐད་ཅེས་བྱ་བ་འདི་ཅིའི་ཕྱིར་སྨོས་ཞེས་པའོ། །

[Block 898]
གང་གི་ཕྱིར་དང་པོ་རབ་ཏུ་སྦྱར་ཞེས་པ་ནི་བཀའ་དག་ལ་དང་པོར་སྦྱར་བ་ལ་དགོངས༌[^430]པ་ཅི་ཞིག༌[^431]ཡོད་ཅེས་པའོ། །

[Block 899]
གང་འདི་བདེ་གཤེགས་གསུང་ཡིན་ནམ། །ཞེས་པ་ནི་གང་གིས་བདག་གིས་ཞེས་བྱ་བ་དང་མ་འབྲེལ་པའི་ཉེས་པ་གཟིགས་པའོ། །

[Block 900]
ཉན་ཐོས་ཀྱི༌[^432]བཤད་པ་ཡིན་ནམ་ཅི་ཞེས་པ་ནི་བཀའ་མ་ཡིན་པའི་ཉེས་པ་བརྗོད་པའོ། །

[Block 901]
གཞན་ནི་གོ་སླའོ། །

[Block 902]
འདི་ནས་མར་ནི་ཡི་གེ་གཉིས་ཆོས་ཐམས་ཅད་ཀྱི་རྒྱུ་འམ་ས་བོན་དུ་བསྟན་པ་ཉིད་དེ། དེ་ལ་ཆོས་ཀྱི་ཕུང་པོ་བརྒྱད་ཁྲི་ཞེས་བྱ་བ༌[^433]ནི་བཤད་ཟིན་ཏོ། །

[Block 903]
དེ་གང༌[^434]གི་གཞི་ཡི་གེ་གཉིས་ཡིན་པ་ཅིའི་ཕྱིར་ཞེ་ན་ཡི་གེ་ཨེ་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་ཏེ། འདིས་རིམ་པ་དང་པོའི༌[^435]བསླབ་པ་བཞི་བསྟན་ཏེ། ཨེ་ནི་མར་གྱུར་ལ་འདིས་ནི༌[^436]བུད་མེད་མཚོན་པར་བྱེད་པ་ཉིད་དེ། གང་གི་ཕྱིར་གང་གིས་གང་ལ་གང་ཞིག་བྱེད་པར་འགྱུར་བ་དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 904]
བ་ནི་ཕ་ཞེས་བྱ་བར་གྲགས། །ཞེས་བྱ་བ་ནི་བ་ཞེས་བྱ་བ་ཕ་མཚོན་པར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 905]
ཐིག་ལེ་དེར་ནི་སྦྱོར་བ་ཉིད། །ཅེས་པ་ནི་གང་ཞིག་གང་དང་གང་དུ་འབྲེལ་པར་འགྱུར་བ་དེའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 906]
འདི་དག་གིས་ནི་འདི་སྐད་དུ་སྟོན་པར་འགྱུར་ཏེ། གང་གིས༌[^437]སེམས་ཅན་སྐྱེ་བ་དང་མཐུན་པར་ལྷའི་སྐུ་རིམ་གྱིས་འབྱུང་བ་ཡབ་དང་ཡུམ་གཉིས་སུ་མེད་པར་སྟོན་པའི་བདག༌[^438]ཉིད་དོ། །

[Block 907]
ཡང་ན། ཨེ་ནི་པདྨ་བཞིན་དུ་གསུངས། །ཞེས་པ་ནི་པདྨ་དང་འདྲ་བའི་ཆོས་ཡོངས་སུ་གནས་པར་འགྱུར་བས་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 908]
བ་ནི་རྡོ་རྗེ་ཉིད་ཡིན་ནོ་ཞེས་པ་ནི་རྡོ་རྗེ་ཡོངས་སུ་བསྟན་པའི༌[^439]བརྡ་གང་ལ་ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 909]
ཐིག་ལེ་དེ༌[^440]ནི་ས་བོན་ཏེ། །ཞེས་པ་ནི་གང་ལ་བྱང་ཆུབ་སེམས་ཀྱི་ས་བོན༌[^441]ཡོད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ་དེས་ཅིར་འགྱུར་ཞེ་ན། དེ་ལས་འགྲོ་བ་གསུམ་པོ་སྐྱེ། །ཞེས་པ་ནི་གང་ལས་གང་གི་སྟོབས་ཀྱིས་སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་སྐྱེ་བར་འགྱུར་བ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 910]
དེ་དག་གིས་ནི་འདི་སྐད་དུ་སྟོན་པར་འགྱུར་ཏེ། གང་ཞིག་གིས་སེམས་ཅན་སྐྱེ་བའི་རིམ་པ་དང་མཐུན་པར་ལྷ་ཡབ་ཡུམ་སྙོམས་པར་ཞུགས་པ་ལས་རང་གིས༌[^442]སྤྲུལ་པའི་དཀྱིལ་འཁོར་རྒྱལ་པོ་མཆོག་ཡོངས་སུ་སྐྱེ་བར་འགྱུར་བ་གང་ཡིན་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 911]
ཨེ་ནི་ཤེས་རབ་ཉིད་འགྱུར་ལ། །ཞེས་པ་ནི་རླུང་ཉིད་དོ། །

[Block 912]
བ་ནི་རབ་དགའི་བདག་པོའོ།[^443] །ཞེས་པ་ནི་རྣམ་པ༌[^444]ཤེས་པ་ཉིད་དོ། །

[Block 913]
ཐིག་ལེ་མི་ཤིགས་དེ་ཉིད་དོ། །

[Block 914]
[^445]ཞེས་པ་ནི་འགྲོ་བ་ཐམས་ཅད་ཀྱི་སྙིང་གི་དབུས་ན༌[^446]རླུང་མི་ཤིགས་རྒྱལ་པོ་ཨ་ཐུང་ངུའི་ངོ་བོར་སྣང་བའོ། །

[Block 915]
དེ་ལས་ཡི་གེ་གཉིས་ཀྱང་སྐྱེ།[^447] །ཞེས་པ་ནི་ཨཱ་ལི་ཀཱ་ལིའི་སྡེ་ཚན་གྱི་ཡི་གེ་རྣམས་འབྱུང་བས་ཏེ་གང་ལ་གང་གིས་ཇི་ལྟར་ཡོངས་སུ་བྱེད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །
--- END BLOCKS ---
