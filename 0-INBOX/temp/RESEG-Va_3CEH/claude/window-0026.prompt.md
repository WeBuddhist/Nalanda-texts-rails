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
ཐོས་པ་དང་དོན་གྱིས་ངོམས་མི་མྱོང་བ་ཞེས་བྱ་བ་ནི་གང་ཐོས་པ་མང་པོ་ཉིད་ཡིན་ན་ཡང་བཏང་སྙོམས་དང་བཅས་པར་མི་འགྱུར་བའོ། །

[Block 912]
སྤྱོད་ལམ་ཐམས་ཅད་དུ་བྱང་ཆུབ་ཀྱི་སེམས་ཡོངས་སུ་སྦྱོང་བར་བྱེད་པ་དང་ཞེས་བྱ་བའི་ཚིག་གི་དོན་ནི་སྤྱོད་ལམ་ཡོངས་སུ་དག་པའི་མདོ༌[^617]བཞིན་ནོ། །

[Block 913]
ཁྱད་པར་དུ་འགྲོ་བའི་ལས་ཞེས་བྱ་བ་ལ། ཕན་པའི་ལྷག་པའི་བསམ་པ་འཕེལ་བར་བྱེད་པའི་རྒྱུར་གྱུར་པ་ཡོངས་སུ་རྫོགས་པ་སྦྱོར་བའི་ལས་དྲུག་པོ་འདི་དག་མང་དུ་བྱས་པས་རྫོགས་པར་འགྱུར་རོ། །

[Block 914]
གུས་པར་བྱས་ཏེ་དགོན་པ་ལ་གནས་ཞེས་བྱ་བ་ནི་དེ་ལ་གནས་པ་ན་བདེན་པ་མ་ཡིན་པའི་རྣམ་པར་རྟོག་པ་ཡོངས་སུ་སྤོང་བའོ། །

[Block 915]
འཇིག་རྟེན་གྱིས༌[^618]སྣ་ཚོགས་ཞེས་བྱ་བ་ནི་གང་དང་གང་བྱེད་པ་ལ་སོགས་པའོ། །

[Block 916]
འགྲུབ་པར་སྦྱོར་བ༌[^619]ལས་ཞེས་བྱ་བ་ནི་དེའི་རྫོགས་པར་བྱེད་པའི་ལས་ཀྱི་རྟགས་སོ། །

[Block 917]
མཐུ་ཐོབ་པ་ཞེས་བྱ་བ་ནི་མངོན་པར་ཤེས་པ་དྲུག་གོ། །

[Block 918]
ཡེ་ཤེས་ལ་རྟོན་པ་ཞེས་བྱ་བ་ནི་ཡེ་ཤེས་ལ་རྟོན་གྱི་རྣམ་པར་ཤེས་པ་ལ་ནི་མ་ཡིན་ཏེ། སོ་སོ་རང་གིས་རིག་པའི་བདག་ཉིད་ཀྱིས༌[^620]ཡེ་ཤེས་བསྐྱེད་ནས་ཡེ་ཤེས་དེ་ལ་མངོན་སུམ་དུ་སྦྱོར་བའི་ཚུལ་གྱིས་ཆོས་ལ་རབ་ཏུ་གནས་པའོ། །

[Block 919]
དེ་ལ༌[^621]འཇོག་པའི་ལས་ཞེས་བྱ་བ་ནི་ཕན་པ་དང་བདེ་བ་བྱ་བའི་ལྷག་པའི་བསམ་པ་གང་གིས་ཕན་པ་དང་བདེ་བ་དེ་ཉིད་ལ་སེམས་ཅན་རྣམས་རབ་ཏུ་འགོད་པར་བྱེད་པའོ། །

[Block 920]
དེ་ལ་ཚོགས་ཡོངས་སུ་སྡུད་པའི་ཡོན་ཏན་ཞེས་བྱ་བ་གང་གིས་ཚུལ་ཁྲིམས་འཆལ་བ་ཡང་ཡོངས་སུ་གཏོང༌[^622]བར་མི་བྱེད་ཅིང་ཐམས་ཅད་དུ་སྤོང་བ་མ་ཡིན་ཏེ། མི་དགེ་བ་ལས་བསླངས༌[^623]ནས་དགེ་བ་ལ༌[^624]སྦྱོར་བར་བྱེད་པའོ། །

[Block 921]
ཐེ་ཚོམ་མེད་པར་འདོམས་ཤིང་རྗེས་སུ་སྟོན་པ་ཞེས་བྱ་བ་ནི་གང་ལ་ཆ་གཅིག་གིས་གདམས་ངག་བྱས་པ་དེ་ལ་ཡང་བདག་གིས་ཁྱོད་ལ་བསྟན་པ་དེ་ལ་བདག་གིས་ལེགས་པར་བསྟན་པ་མ་ཡིན་ནོ་ཞེས་བརྗོད་པར་མི་བྱེད་པ་སྟེ། དེས་ན་དེའི་ཚིག་གཟུང་བར༌[^625]འོས་པར་འགྱུར་རོ།[^626] །ཆོས་དང་ཟང་ཟིང་གིས་སྡུད་པ་ཡང་གང་བདེན་པར་སྨྲ་བར་བྱེད་པའི་ཆོས་དང་ཟང་ཟིང་ཆོས་གོས་ལ་སོགས་པ་དེ་རྣམས་ཀྱིས་བསྡུས་པ་དེ་དག་གིས་ཀྱང་དེ་བཞིན་དུ་སྒྲུབ་པར་བྱེད་དོ། །

[Block 922]
སེམས་ཀུན་ནས་ཉོན་མོངས་པ་ཅན་མ་ཡིན་པ་ཞེས་བྱ་བ་ནི་གང་བྱང་ཆུབ་ཀྱི་སེམས་ཡོངས་སུ་བཟུང་ནས་སེམས་ཅན་གྱི་དོན་བྱེད་པ་ཡིན་གྱི། བདག་ཉིད་ཡོངས་སུ་སྤྱོད་པར་བྱེད་པ་ནི་མ་ཡིན་ནོ། །

[Block 923]
དེ་ལྟ་ན་ཡང་དགེ་བའི་རྩ་བ་འདིས་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས་སེམས་ཅན་རྣམས་ཉེ་བར་སྡུད༌[^627]པར་བྱེད་པར་ཤོག་ཤིག༌[^628]ཅེས་བྱ་བ་ལྟ་བུའོ། །

[Block 924]
དོན་འདི་དག་ཉིད་ཚིགས་སུ་བཅད་པས། དང་པོའི་ཚིག་ནི་ཉེར་བཟུང་ནས། །ཞེས་བྱ་བ་ལ་སོགས་པས་བསྟན་ཏོ། །

[Block 925]
དེ་ལྟར་རེ་ཞིག་ཤེས་བྱ་དང་། མཚན་ཉིད་རྣམ་པ་གཉིས་སོ། །

[Block 926]
[^629]

[Block 927 [HEADING]]
## ཤེས་བྱའི་མཚན་ཉིད་ལ་འཇུག་པ། ^3-0

[Block 928]
ཇི་ལྟར་འཇུག་པར་འགྱུར་བ་དེ་བསྟན་པར་བྱའོ། །

[Block 929 [HEADING]]
### ཤེས་བྱ་དང་མཚན་ཉིད་ལ་འཇུག་པ། ^3-1-0

[Block 930]
དེ་ལ་ཤེས་བྱ་དང་མཚན་ཉིད་ལ་འཇུག་པ་ཇི་ལྟ་བུ་ཞེ་ན། བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ལེགས་པར་བསགས་པའི་བྱང་ཆུབ་སེམས་དཔའོ་ཞེས་བྱ་བའོ། །

[Block 931]
ཡང་དེ་ནི་རིམ་པ་ཇི་ལྟ་བུས་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ཡོངས་སུ་རྫོགས་པར་བྱེད་ཅེ་ན། རྒྱུའི་སྟོབས་དང་། དགེ་བའི་བཤེས་གཉེན་གྱི་སྟོབས་དང་། ཡིད་ལ་བྱེད་པའི་སྟོབས་དང་། ཉེ་བར་སྟོན་པའི༌[^630]སྟོབས་ཀྱིས་སོ། །

[Block 932]
དེ་ལ་ཚིག་གཉིས་ཀྱིས་ནི་སྟོབས་གཉིས་ལ་གྲངས་བཞིན་དུ༌[^631]རིག་པར་བྱའོ། །

[Block 933]
དེ་ལ་ཡིད་ལ་བྱེད་པའི་སྟོབས་ཀྱིས་ནི་གཅིག་ཏུ་མོས་པར་བྱེད་པའོ། །

[Block 934]
དེ་ཡང་ཐེག་པ་ཆེན་པོའི་བག་ཆགས་ཀྱི་རྒྱུ་ཅན་ནོ། །

[Block 935]
དེ་ལ་གཅིག་པུ༌[^632]ལྷག་པར་མོས་པ་ཡོད་ན་སྒྲུབ་པ་ལ་ཡང་དག་པར་འཇུག་གོ། །

[Block 936]
སྒྲུབ་པ་ལ་ཡང་དག་པར་གནས་ན་དགེ་བའི་རྩ་བ་ཉེ་བར་སོགས་པར་འགྱུར་ཏེ། དེ་ལྟར་ན་ཡིད་ལ་བྱེད་པའི་སྟོབས་ཀྱིས་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ལེགས་པར་སོགས་པར་འགྱུར་བས་གོ་རིམས་ཀྱི་ཚུལ་ནི་དེ་ལྟར་རོ། །

[Block 937]
དེ་ལྟར་ན་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་ལེགས་པར་བསགས་པ་ནི་ས་ལ་འཇུག་པར་འགྱུར་ལ། དེ་ལྟར་ཉེ་བར་བསྟན་པར་གྱུར་པ་ནི་ཉེ་བར་སྟོན་པའི༌[^633]སྟོབས་ཀྱིས་ཐེག་པ་ཆེན་པོའི་ཆོས་ཀྱི་རྒྱུ་ལས་བྱུང་བ་ཞེས་བྱ་བ་སྟེ། བསྟན་པའི་ཆོས་ལ་དམིགས་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །གང་གིས་འཇུག་ཅེ་ན། དགེ་བའི་རྩ་བའི་སྟོབས་བསྐྱེད་པ་དང་། རྣམ་པ་གསུམ་གྱིས་སེམས་སྦྱོང་བ་ཞེས་བྱ་བ་ནས། རྟག་ཏུ༌[^634]གུས་པར་བྱས་ཏེ་སྦྱོར་བ་དང་། བག་ཡོད་པས་འཇུག་གོ་ཞེས་བྱ་བའི་བར་གྱིས་སོ། །

[Block 938]
དགེ་བའི་རྩ་བའི་སྟོབས་སྐྱེད་པ༌[^635]ནི་ཡང་ཇི་སྐད་བསྟན་པའི་ཚིག་བརྒྱད་ལ་སྦྱར་བར༌[^636]བྱའོ། །

[Block 939]
དེ་ལ་ཞུམ་པ་གསུམ་གྱི་གཉེན་པོར་སེམས་སྦྱོང་བ་རྣམ་པ་གསུམ་སྟེ། དེ་ཡང་འདི་ལྟར་བྱང་ཆུབ་སེམས་དཔའ༌[^637]མཆོག་ཏུ་ཟབ་ཅིང་རྒྱ་ཆེ་བའི་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་རྟོགས་པར་དཀའ་བ་ཐོས་པ་ན་ཞུམ་པར་འགྱུར་ཏེ། དེའི་གཉེན་པོར་ནི་སེམས་སྦྱོང་བ་དང་པོའོ། །

[Block 940]
ཡང་བྱང་ཆུབ་སེམས་དཔས་མཆོག་ཏུ་ཟབ་ཅིང་རྒྱ་ཆེ་བ་རྟོགས་པར་དཀའ་བའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་སྒྲུབ་པ་ལ་ཞུམ་པར་འགྱུར་ཏེ། དེའི་གཉེན་པོར་སེམས་སྦྱོང་བ་གཉིས་པ་བསྟན་ཏེ། བསམ་པ་གང་གིས་སྦྱིན་པ་ལ་སོགས་པ་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་ལ་ཀུན་ཏུ་སྤྱོད་པའི༌[^638]བསམ་པ་ཞེས་བྱ་བ་དེ་ལ། བསམ་པ་ནི་དད་པ་དང་འདུན་པའོ། །

[Block 941]
ཡོད་པ་དང་། ཡོན་ཏན་དང་ལྡན་པ་དང་། ནུས་པ་ཉིད་དང་། ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་ཡིད་ཆེས་པ་ཉིད་དེ་ནི་བྱང་ཆུབ་སེམས་དཔའི་དད་པའོ། །

[Block 942]
དད་པས་བསྐྱེད་པའི་ནན་ཏན་བྱེད་པར་འདོད་པ་ཉིད་ནི་འདུན༌[^639]པའོ། །

[Block 943]
དེ་ལྟ་བུའི་དད་པ་དང་འདུན་པའི་ངོ་བོ་ཉིད་ཀྱི་བསམ་པ་ཐོབ་པར་གྱུར་པའི་བྱང་ཆུབ་སེམས་དཔའ་ནི་ཚེགས་ཆུང་ངུ་ཉིད་ཀྱིས༌[^640]ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་སྒོམ་པ་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ། །

[Block 944]
ཡང་བྱང་ཆུབ་སེམས་དཔས༌[^641]སངས་རྒྱས་རྣམས་ཀྱི་ཟབ་ཅིང་རྒྱ་ཆེ་བའི་ཆོས་རབ་ཏུ་འབྱེད་པ་ལ་མཁས་པར་གནས་པ་ན་འདི་ལྟར་སེམས་པར་བྱེད་དེ། འདི་ལྟར་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་སྐད་ཅིག་མ་གཅིག་ཏུ་གཏོགས་པ་ཐོབ་པར༌[^642]བྱའོ་ཞེས་བྱ་བ་ནི་རྟོགས་པར་དཀའོ་ཞེས་ཞུམ་པར་འགྱུར་བས་དེའི་གཉེན་པོར་སེམས་སྦྱོང་བ་གསུམ་པ་བདག་དགེ་བ་སྒྲིབ་པ་མེད་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། གང་གི་ཕྱིར་བདག་ས་བཅུ་པོ་ཐམས་ཅད༌[^643]དུ་ཡེ་ཤེས་ཀྱི་ཚོགས་ལེགས་པར་བསགས་པ་ལྟ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 945]
དགེ་བ་སྒྲིབ་པ་མེད་པ་དང་། ཞེས་བྱ་བ་ནི་འདོད་ཆགས་དང་བཅས་པའི་གནས་ངན་ལེན་བསྲབས་པར་བྱེད་ཅིང་དེ་བྲལ་བར་དཀའ་བའི་སྒྲིབ་པ་འབྱེད་པ་རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་ཏེ། ཏིང་ངེ་འཛིན་གྱི་བར་མཚམས་མེད་པས་སྒྲིབ་པ་ཐམས་ཅད་དང་བྲལ་ཞིང་དེའི་རྟེན་གནས་གྱུར་པ་དེས་ཐོབ་པར་འགྱུར་རོ་ཞེས་བྱའོ། །

[Block 946]
ཤི་བ་ཙམ་ཉིད་དང་ནི་རྣམ་པར་བྲལ་བ་ཉིད་ཆོས་མཐུན་པ་ཉིད་དུ་འདོད་དོ། །

[Block 947]
ཕུན་སུམ་ཚོགས་པ་ནི་རྣམ་པ་ཐམས་ཅད་མཁྱེན་པའོ། །

[Block 948]
ཐེ་ཚོམ་ཐམས་ཅད་ཐེ་ཚོམ་མེད་པར་གཟུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་མི༌[^644]གང་ཐེག་པ་ཆེན་པོའི་ཆོས་ཀྱི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ལ་བརྩམས་ནས་ངོ་བོ་ཉིད་གསུམ་སྟོན་པ་སྟེ། འདི་ལྟ་སྟེ། ཆོས་ཐམས་ཅད༌[^645]ངོ་བོ་ཉིད་མེད་པ། མ་སྐྱེས་པ། མ་འགགས་པ། གདོད་མ༌[^646]ནས་ཞི་བའོ། །

[Block 949]
ཆོས་ཐམས་ཅད་ནི་རང་བཞིན་གྱིས་མྱ་ངན་ལས་འདས་པའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་མེད་པའི་རྣམ༌[^647]གྲངས་ཀྱིས་ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་ཉེ་བར་གཟུང་བར༌[^648]བྱའོ། །

[Block 950]
སྒྱུ་མ་དང་། སྨིག་རྒྱུ་དང་། རྨི་ལམ་དང་། མིག་ཡོར་དང་། གཟུགས་བརྙན་དང་། ཆུ་ཟླ་དང་། སྤྲུལ་པ་བསྟན་པས་ནི་གཞན་གྱི་དབང་གི་ངོ་བོ་ཉེ་བར་གཟུང་བར༌[^649]བྱའོ། །
--- END BLOCKS ---
