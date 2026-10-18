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
[Block 4866]
ན་བ་སྐྱེས་སོ་ཞེས་བྱ་བ་བཞིན༌[^3446]ནོ། །

[Block 4867]
མ་ཡིན་ཏེ། བཀག་པའི་ཕྱིར་རོ། །

[Block 4868]
བཅོམ་ལྡན་འདས་ཀྱིས་དོན་དམ་པ་སྟོང་པ་ཉིད་ཀྱི་མདོ་ཁོ་ན་ལས།

[Block 4869]
དགེ་སློང་དག་ལས་ནི་ཡོད་དོ། །

[Block 4870]
རྣམ་པར་སྨིན་པ་ནི་ཡོད་དོ། །

[Block 4871]
ཆོས་སུ་བརྡར་བཏགས་པ་མ་གཏོགས་པ་གང་ཞིག་ཕུང་པོ་འདི་རྣམས་འདོར་བར་བྱེད་ཅིང་ཕུང་པོ་གཞན་དག་ཉིང་མཚམས་སྦྱོར་བར་བྱེད་པའི་བྱེད་པ་པོ་ནི་མི་དམིགས་སོ་ཞེས་གསུངས་སོ། །

[Block 4872]
དབོ་ལས་སྐྱེས་ཀྱི་མདོ་ལས་ཀྱང་། དབོ་ལས་སྐྱེས་ལེན་ཅེས་མི་སྨྲའོ་ཞེས་གསུངས་ཏེ། དེ་ལྟ་བས་ན་ཕུང་པོ་རྣམས་ལེན་པར་བྱེད་པ་ཡང་འགའ་ཡང་མེད་ལ། འདོར་བར་བྱེད་པ་ཡང་མེད་དོ། །

[Block 4873]
རེ་ཞིག་ཁྱོད་མཆོད་སྦྱིན་པ་ནས་རྒ་བའི་བར་གང་གི་དབང་དུ་བྱས་ནས་དཔེར་བྱེད། གལ་ཏེ་གང་ཟག་ཡིན་ནོ་ཞེ་ན་ནི་དེ་མ་གྲུབ་བོ། །

[Block 4874]
འོན་ཏེ་སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་ཡིན་ནོ་ཞེ་ན་ནི་དེ་དག་སྐད་ཅིག་རེ་རེ་ལ་སྔོན་མེད་པ་ལས་སྐྱེ་བ་ཁོ་ན་ཡིན་ནོ། །

[Block 4875]
འོན་ཏེ་ལུས་ཡིན་ནོ་ཞེ་ན། དེ་ཡང་དེ་དང་འདྲ་ལ། ལུས་དང་། རིག་པ་དང་། རྟགས་བཞིན་དུ་ཕུང་པོ་དང་གང་ཟག་གཉིས་གཞན་ཉིད་དུ་ཡང་འགྱུར་རོ། །

[Block 4876]
རྒ་བ་དང་ན་བ་ཡང་ལུས་གཞན་ཁོ་ན་ཡིན་ནོ། །

[Block 4877]
གྲངས་ཅན་པའི་འགྱུར་བར་སྨྲ་བ་ནི་བཀག་ཟིན་ཏོ། །

[Block 4878]
དེ་ལྟ་བས་ན་འདི་དག་ནི་དཔེ་ངན་པ་ཡིན་ནོ། །

[Block 4879]
གལ་ཏེ་ཡང་ཕུང་པོ་རྣམས་ནི་སྔོན་མེད་པ་ལས་སྐྱེས་པ༌[^3447]ཡིན་ལ། གང་ཟག་ནི་མ་ཡིན་པར་འདོད་ན་ནི་དེ་དེ་དག་ལས་གཞན་པ་དང་། རྟག་པར་གསལ་བར་ཡོངས་སུ་བསྟན་པ་ཡིན་ནོ། །

[Block 4880]
ཕུང་པོ་ནི་ལྔའོ། །

[Block 4881]
གང་ཟག་ནི་གཅིག་གོ་ཞེས་སྨྲ་བས་ཇི་ལྟར་ན་གཞན་ཉིད་དུ་མི་བརྗོད། རེ་ཞིག་ཇི་ལྟར་ན་འབྱུང་བ་དག་ནི་བཞི་ཡིན། གཟུགས་ནི་གཅིག་ཡིན༌[^3448]ལ་འབྱུང་བ་རྣམས་ལས་གཟུགས་གཞན་ཡང་མ་ཡིན། སྨྲ་བ་འདི་ནི་ཕྱོགས་ལ༌[^3449]ཡོད་པ་ཡིན་ནོ། །

[Block 4882]
ཕྱོགས་གང་ལ་ཞེ་ན། འབྱུང་བ་ཙམ་པའི་ཕྱོགས་ལའོ། །

[Block 4883]
དེ་ལྟ་ན་ཡང་ཇི་ལྟར་འབྱུང་བ་ཙམ་གཟུགས་ཡིན་པ་དེ་བཞིན་དུ་ཕུང་པོ་ཙམ་གང་ཟག་ཡིན་པར་ཁས་བླངས་པ་ཡིན་ནོ། །

[Block 4884 [HEADING]]
#### སྲོག་དེ་ཉིད་ལུས་ཡིན་པའམ་གཞན་ཡིན་ནོ་ཞེས་ལུང་མ་བསྟན་པ། ^6-2-11-0

[Block 4885]
གལ་ཏེ་ཕུང་པོ་ཙམ་གང་ཟག་ཡིན་ན་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་སྲོག་དེ་ཉིད་ལུས་ཡིན་པའམ། གཞན་ཡིན་ནོ་ཞེས་ལུང་མ་བསྟན་ཞེ་ན། འདྲི་བ་པོའི་བསམ་པ་ལ་ལྟོས་པའི་ཕྱིར་ཏེ། དེས་ན༌[^3450]ནི་ནང་གི་བྱེད་པའི་སྐྱེས་བུ་སྲོག་གི་རྫས་གཅིག་པོ་དྲིས་སོ། །

[Block 4886]
དེ་ཡང་འགའ་ཡང་མེད་ན་འདི་ཇི་ལྟར་གཞན་ཉིད་དམ་གཞན་མ་ཡིན་པ་ཉིད༌[^3451]ལུང་བསྟན་པར་བྱ་སྟེ། རུས་སྦལ་གྱི་ཡུལ་བཤོར༌[^3452]རམ་འཇམ་ཞེས་བྱ་བ་བཞིན༌[^3453]ནོ། །

[Block 4887]
མདུད་པ་འདི་ནི་སྔ་མ་དག་ཁོ་ནས་ཀྱང་བཀྲོལ་ཟིན་ཏེ། རྒྱལ་པོ་དེས་འདུ་སྦྱིན་གནས་བརྟན་ཀླུ་སྡེའི་ཐད་དུ་འོངས་ནས་བཙུན་པ་དགེ་སྦྱོང་རྣམས་ནི་སྨྲ་བ་མང་བ་མ༌[^3454]ལགས་སོ། །

[Block 4888]
གལ་ཏེ་གང་དྲིས་པ་དེ་ཉིད་ལན་འདེབས་ན་བདག་འདྲི་བར་འཚལ་ལོ་ཞེས་སྨྲས་སོ། །

[Block 4889]
དྲིར་གསོལ་ཞེས་སྨྲས་པ་དག༌[^3455]ཅི་ལགས། སྲོག་དེ་ཉིད་ལུས་ལགས་སམ། སྲོག་ཀྱང་གཞན་ལགས༌[^3456]ལ་ལུས་ཀྱང་གཞན་ལགས་ཞེས་དྲིས་སོ། །

[Block 4890]
གནས་བརྟན་གྱིས་འདི་ནི་ལན་མི་གདགས་པ༌[^3457]ཡིན་ནོ་ཞེས་སྨྲས་པ་དང་། དེས་སྨྲས་པ། བདག་གིས་སྔ་ནས་བཙུན་པ་གཞན་ལུང་བསྟན་པར་མི་བྱའོ་ཞེས་དམ་འཆར་གསོལ་བ༌[^3458]མ་ལགས་སམ།

[Block 4891]
ཅིའི་སླད་དུ་འདི་སྐད་དུ་འདི་ནི་ལན་མི་གདབ་པ་ཡིན་ནོ་ཞེས་གཞན་ཁོ་ན་གསུངས།

[Block 4892]
གནས་བརྟན་གྱིས་སྨྲས་པ། རྒྱལ་པོ་ཆེན་པོ་རྒྱལ་པོ་རྣམས་ནི་སྨྲ་བ་མང་བ་ལགས་སོ། །

[Block 4893]
གལ་ཏེ་གང་དྲིས་པ་དེ་ཉིད་ལན་འདེབས་ན་བདག་ཀྱང་འདྲི་བར༌[^3459]འཚལ་ལགས་སོ། །

[Block 4894]
དྲིར་གསོལ་ཞེས་སྨྲས་པ་དང་། ཁྱོད་ཀྱི་སླས་ལ་ཤིང་ལྗོན་པ་ཨ་མྲ་འབྲས་བུ་ཡོད་པ་གང་ཡིན་པ་དེའི་འབྲས་བུ་རྣམས་ཅི་སྐྱུར་རམ་འོན་ཏེ་མངར་ལགས༌[^3460]ཞེས་དྲིས་སོ། །

[Block 4895]
བདག་གི་སླས་ལ་ཤིང་ལྗོན་པ་ཨ་མྲ་ཉིད་འགའ་ཡང་མེད་དོ་ཞེས་སྨྲས་སོ། །

[Block 4896]
བདག་གིས་སྔ་ནས་རྒྱལ་པོ་ཆེན་པོ་གཞན་ལུང་བསྟན་པར་མི་བྱའོ་ཞེས་དམ་འཆར་གསོལ་བ༌[^3461]མ་ལགས་སམ།

[Block 4897]
ཅིའི་སླད་དུ་འདི་སྐད་དུ་ཤིང་ལྗོན་པ་ཨ་མྲ་ཉིད་མེད་དོ་ཞེས་གཞན་ཁོ་ན་གསུངས།

[Block 4898]
དེས་སྨྲས་པ། ཇི་ལྟར་ན་ཤིང་ལྗོན་པ་མེད་པའི་འབྲས་བུ་རྣམས་སྐྱུར་བའམ་མངར་བ་ཉིད་དུ་ལུང་བསྟན་པར་བྱ། རྒྱལ་པོ་ཆེན་པོ་དེ་བཞིན་དུ་སྲོག་དེ་ཉིད་མེད་ན་ཅིའི་སླད་དུ་འདི་ལུས་ལས་གཞན་པ་ཉིད་དམ་གཞན་མ་ཡིན་པ་ཉིད་དུ་ལུང་བསྟན་པར་བགྱི་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 4899]
ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་མེད་པ་ཁོ་ནའོ་ཞེས་མ་གསུངས་ཤེ་ན། དྲི་བ༌[^3462]པོའི་བསམ་པ་ལ་ལྟོས་པའི་ཕྱིར་ཏེ། དེས་སྲོག་ཅེས་བྱ་བ་ཕུང་པོའི་རྒྱུན་གང་ཡིན་པ་དེ་ཡང་མེད་པར་གོ་བར་གྱུར་ན་ལོག་པར་ལྟ་བར་ལྟུང་བར་འགྱུར་ཏེ། རྟེན་ཅིང་འབྲེལ་པར་འབྱུང་བ་མི་ཤེས་པའི་ཕྱིར་རོ། །

[Block 4900]
དེ་ནི་དེ་བསྟན་པ་ཡང་མི་བཟོད་དོ། །

[Block 4901]
འདི་ནི་བཅོམ་ལྡན་འདས་ཀྱིས་ཀུན་དགའ་བོ་ཀུན་དུ་རྒྱུ་གནས་པ་དང་། རུས་མཐུན་པས་དྲི་བ་དྲིས་པ་དག་ཡོད་དོ་ཞེས་ལུང་བསྟན་ན་ནི་ཆོས་ཐམས་ཅད་བདག་མེད་པས་ཚིག་མ་ལེགས་པ་མ་ཡིན་ནམ། ཀུན་དགའ་བོ་ཀུན་དུ་རྒྱུ་གནས་པ་དང་རུས་མཐུན་པའི་དྲི་བ་དྲིས་པ་བདག་མེད་དོ་ཞེས་ལུང་བསྟན་ན་ནི་ཀུན་ཏུ་རྒྱུ་གནས་པ་དང་རུས་མཐུན་པའི་སྔ་ནས་ཀུན་དུ་རྨོངས་པ་ཡོད་པ་དག་གིས༌[^3463]བདག་སྔོན་ཡོད་པར་གྱུར་པ་ལས་ད་ནི་བདག་གི་དེ་ཡང་མེད་དོ་ཞེས་ཀུན་དུ་རྨོངས་པ༌[^3464]ཕྱིར་ཞིང་ཆེས་རྒྱས་པར་འགྱུར་བ་མ་ཡིན་ནམ། ཀུན་དགའ་བོ་བདག་ཡོད་ཅེས་བྱ་བ་ནི་རྟག་པའི་མཐར་འགྱུར་རོ། །

[Block 4902]
ཀུན་དགའ་བོ་བདག་མེད་ཅེས་བྱ་བ་ནི་ཆད་པའི་མཐར་འགྱུར་རོ་ཞེས་རྒྱས་པར་གསུངས་པ་གང་ཡིན་པ་འདི་ལས་ཀྱང་དེ་བཞིན་དུ་ངེས་པར་ཟུང༌[^3465]ཤིག །

[Block 4903]
འདིར་སྨྲས་པ།

[Block 4904 [VERSE]]
ལྟ་བའི༌[^3466]མཆེ་བས་སྨྲས་པ་དང་། །
ལས་རྣམས་འཇིག་པ་ལ༌[^3467]ལྟོས་ནས། །
སྟག་མོས་ཕྲུ་གུ་ཁྱེར་བ་ལྟར། །
རྒྱལ་བས་ཆོས་ནི་སྟོན་པར་མཛད། །

[Block 4905 [VERSE]]
བདག་ཡོད་ཉིད་དུ་ཁས་བླངས་ནས། །
ལྟ་བའི་མཆེ་བས་སྨས་པར༌[^3468]གྱུར། །
ཀུན་རྫོབ་རྟོག་པར་མ་གྱུར་ནས། །
དགེ་བ་ཕྲུ་གུ་ཉམས་བྱེད་འགྱུར། །
--- END BLOCKS ---
