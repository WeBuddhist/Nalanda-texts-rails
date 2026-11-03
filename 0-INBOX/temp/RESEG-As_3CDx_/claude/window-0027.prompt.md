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
[Block 946]
དེ་ལ་དཔེའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ནི་གདུལ་བའི་བསམ་པ་དང་། མོས་པ་ཐ་དད་པའི་དབང་དུ་མཛད་ནས་འཇིག་རྟེན་ལ་གྲགས་པའི་གཟུགས་དང་སྒྲ་དང་། དྲི་དང་། རོ་དང་། རེག་བྱ་དང་། ཆོས་རྣམས་ཀྱི་མཚན་གཞི་དང་མཚན་ཉིད་ཐ་དད་པ་དང་། ཐ་དད་པ་མ་ཡིན་པ་ཉིད་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་དང་ལྡན་པ་རྣམས་རྨོངས་སོ། །

[Block 947]
དེ་ལ་དུང་དང་གསེར་ནི་གཟུགས་སོ། །

[Block 948]
པི་ཝང་གི་སྒྲ་ནི་སྒྲའོ། །

[Block 949]
ཨ་ཀ་རུ་ནག་པོའི་དྲི་ནི་དྲིའོ། །

[Block 950]
ན་ལེ་ཤམ་གྱི་ཚ་བ་དང་ཨ་རུ་རའི་མངར་བ་ནི་རོའོ། །

[Block 951]
ཤིང་བལ་གྱི་འདབ༌[^742]མའི་འཇམ་པ་ནི་རེག་བྱའོ། །

[Block 952]
མར་ལ་སོགས་པ་ལྷག་མ་རྣམས་ནི་ཆོས་ཏེ། ཆོས་དེ་དག་ཀྱང་། གཟུགས་དང་། སེམས་དང་སེམས་ལས་བྱུང་བ་དང་། ཀུན་ནས་ཉོན་མོངས་པ་དང་རྣམ་པར་བྱང་བའི་ཆོས་རྣམས་དང་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 953]
དེ་དག་གི་ཚིག་གི་དོན་ནི་དུང་གི་འབྱུང་བ་དང་འབྱུང་བ་ལས་གྱུར་པ་འདུས་པའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་དཀར་པོ་ཉིད་དང་ཐ་དད་པ་ཡང་མ་ཡིན་ཐ་མི་དད་པ་ཡང་མ་ཡིན་ཏེ། དེའི་ཕྱིར་དུང་གི་རྫས་ནི་འབྱུང་བ་ལས་གྱུར་པ་ཁ་དོག་ཙམ་དུ་ཟད་པ་ཡང་མ་ཡིན་ནོ། །

[Block 954]
ལྷག་མ་རྣམས་ལ་ཡང་དེ་བཞིན་དུ་ཅི་རིགས་པར་སྦྱར་རོ། །

[Block 955]
བློ་གྲོས་ཤིན་ཏུ་རྣམ་དག་དེ་བཞིན་དུ་ཞེས་བྱ་བ་ལ་སོགས་པ༌[^743]དཔེས་མཚོན་པའི་དོན་ནི་གཏན་ཚིགས་སྔར་བསྟན་པ་བཞིན་དུ་སྦྱར་རོ། །

[Block 956]
བློ་གྲོས་ཤིན་ཏུ༌[^744]རྣམ་དག་ངས་ནི་དོན་དམ་པར་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་དོན་དམ་པའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་སྔར་བསྟན་པ་དེ་ཉིད་ཀྱི་མཇུག་བསྡུ་བ་བསྟན་ཏོ། །

[Block 957]
ཕྲ་བ། མཆོག་ཏུ་ཕྲ་བ། ཟབ་པ། མཆོག་ཏུ་ཟབ་པ། རྟོགས་པར་དཀའ་བ། མཆོག་ཏུ་རྟོགས་པར་དཀའ་བ་ཞེས་བྱ་བ་ལ། ཕྲ་བ་དང་། ཟབ་པ་དང་། རྟོགས་པར་དཀའ་བ་ཞེས་བྱ་བའི་ཚིག་གསུམ་ནི་ཕྲ་བ་ཉིད་བྱེ་བྲག་ཏུ་བྱ་བའི་ཕྱིར་ཟབ་པ་ཞེས་བྱ་བ་གསུངས་ལ། ཟབ་པ་ཉིད་བྱེ་བྲག་ཏུ་བྱ་བའི་ཕྱིར་རྟོགས་པར་དཀའ་བ་ཞེས་གསུངས་ཏེ། དེ་དག་ནི་ཉན་ཐོས་ལ་སོགས་པ་དང་ཐུན་མོང་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 958]
མཆོག་ཏུ་ཕྲ་བ་དང་། མཆོག་ཏུ་ཟབ་པ་དང་། མཆོག་ཏུ་རྟོགས་པར་དཀའ་བ་ཞེས་བྱ་བའི་ཚིག་གསུམ་ཡང་སྔ་མ་བཞིན་དུ་གཅིག་ལས་གཅིག་ཏུ་བྱེ་བྲག་ཏུ་བྱ་བ་ཡིན་ཏེ། དེ་དག་ནི་ཉན་ཐོས་ལ་སོགས་པ་དང་། ཐུན་མོང་མ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 959]
བསྙད་ཅིང་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གི་དོན་ནི་སྔར་བཤད་པ་བཞིན་དུ་སྦྱར་རོ། །

[Block 960]
དེ་དག་ནི་དཔེས་མཚོན་པའི་དོན་གྱི་མཇུག་བསྡུ་བའི་ཕྱིར་ཞར་ལ་བཟླས་པ་ཙམ་དུ་ཟད་ཀྱི། གཙོ་ཆེར་དཔེར་བསྟན་པའི་གནས་སྐབས་ཡིན་པས་ན་དེ་ནི་དེ་དག་གི་དཔེའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 961 [HEADING]]
##### དེ་དག་གི་དངོས་པོ་བསྡུ་བའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ། ^4-1-3-4-0

[Block 962]
དེའི་འོག་ཏུ་དེ་དག་གི་དངོས་པོ་བསྡུ་བའི་མཚན་ཉིད་རྣམ་པར་གཞག་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། དེ་དག་གི་དངོས་པོ་བསྡུ་བའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་ནི་དོན་དམ་པ་ཐ་དད་པ་དང་། ཐ་དད་པ་མ་ཡིན་པ་ཉིད་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་དང་ལྡན་པ་སྔར་བསྟན་པ་ཚིག་གི་དོན་དེ་དག་གི་དངོས་པོ་ཚིགས་སུ་བཅད་པས་མདོར་བསྡུས་པའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་གང་ཡིན་པའོ། །

[Block 963]
དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚེ་ཚིགས་སུ་བཅད་པ་འདི་དག༌[^745]བཀའ་སྩལ་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིགས་སུ་བཅད་པ་གཉིས༌[^746]གསུངས་ཏེ། དེ་ལ།

[Block 964 [VERSE]]
འདུ་བྱེད་ཁམས་དང་དོན་དམ་མཚན་ཉིད་ནི། །
གཅིག་དང་ཐ་དད་བྲལ་བའི་མཚན་ཉིད་དེ། །

[Block 965]
ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་དང་པོའི་རྩ་བ་གོང་མ་གཉིས་ཀྱིས་ནི་དོན་དམ་པའི་ཐ་དད་པ་དང་། ཐ་དད་པ་མ་ཡིན་པ་ཉིད་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་དང་ལྡན་པའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་སྔར་བསྟན་པའི་དངོས་པོ་བསྡུ་བ་བསྟན་ཏེ། དེས་རྣམ་པར་བྱང་བའི་ཕྱོགས་ཐམས་ཅད་ཀྱི་དངོས་པོ་བསྡུ་བ་ཡང་བསྟན་པ་ཡིན་ནོ། །

[Block 966 [VERSE]]
གཅིག་དང་ཐ་དད་ཉིད་དུ་གང་རྟོག་པ། །
དེ་དག་ཚུལ་བཞིན་མ་ཡིན་ཞུགས་པ་ཡིན། །

[Block 967]
ཞེས་བྱ་བ་རྩ་བ་འོག་མ་འདི་གཉིས་ཀྱིས་ནི་ཤིན་ཏུ་རྨོངས་པ་གཉིས་ཀྱིས་ཤིན་ཏུ་རྨོངས་ནས་དོན་དམ་པ་ལ་ཚུལ་བཞིན་མ་ཡིན་པས་སེམས་པའི་ཤིན་ཏུ་རྨོངས་པའི་མཚན་ཉིད་རྣམ་པར་གཞག་པའི་དངོས་པོ་བསྡུ་བ་བསྟན་ཏེ། དེས་ཀུན་ནས་ཉོན་མོངས་པའི་ཕྱོགས་ཐམས་ཅད་ཀྱི་དངོས་པོ་བསྡུ་བ་ཡང་བསྟན་པ་ཡིན་ནོ། །

[Block 968 [VERSE]]
སྐྱེ་བོའི་ས་ལ་ལྷག་མཐོང་དང་། །
ཞི་གནས་གོམས་པར་བྱས་པས་ནི། །

[Block 969]
ཞེས་བྱ་བའི་ཚིགས་སུ་བཅད་པ་གཉིས་པའི་རྩ་བ་གོང་མ་འདི་གཉིས་ཀྱིས་ནི་དེ་ལྟར་བསྡུ། ཉོན་མོངས་པའི་ཕྱོགས་ལ་གནས་པ་དེ་དག་གི་གཉེན་པོ་བསྒོམ་པའི༌[^747]དངོས་པོ་བསྡུ་བ་བསྟན་པའོ། །

[Block 970 [VERSE]]
གནས་ངན་ལེན་གྱི་འཆིང་བ་དང་། །
མཚན་མའི་འཆིང་བ་ལས༌[^748]གྲོལ་འགྱུར། །

[Block 971]
ཞེས་བྱ་བའི་རྩ་བ་འོག་མ་འདི་གཉིས་ཀྱིས་ནི་དེ་ལྟར་གཉེན་པོ་བསྒོམ༌[^749]པ་དེའི་ཕན་ཡོན་གྱི་དངོས་པོ་བསྡུ་བ་བསྟན་ཏེ། དེ་ནི་དེ་དག་གི་དངོས་པོ་བསྡུ་བའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ཡིན་ནོ། །

[Block 972]
ལེའུ་གསུམ་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 973 [HEADING]]
#### འཕགས་པ་རབ་འབྱོར་གྱི་ལེའུ། ^4-1-4-0

[Block 974]
དེ་ལྟར་ཐ་དད་པ་དང་ཐ་དད་པ་མ་ཡིན་པ་ཉིད་ལས་ཡང་དག་པར་འདས་པའི་མཚན་ཉིད་ཀྱིས་དོན་དམ་པའི་མཚན་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བ་བསྟན་ནས། ད་ནི་ཐམས་ཅད་དུ་རོ་གཅིག་པའི་མཚན་ཉིད་ཀྱིས་དོན་དམ་པའི་བདེན་པའི་མཚན་ཉིད་ཡོངས་སུ་ཤེས་པར་བྱ་བ་བསྟན་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཚེ་དང་ལྡན་པ་རབ་འབྱོར་ལ་བཀའ་སྩལ་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་འཕགས་པ་རབ་འབྱོར་གྱི་ལེའུ་བཞི་པ་འདི་གསུངས་སོ། །

[Block 975]
དེ་ལ་ལེའུ་བཞི་པ་འདིའི་བསྡུས་པའི་དོན་ནི་མདོར་བསྡུ་ན་ཐམས་ཅད་དུ་རོ་གཅིག་པའི་མཚན་ཉིད་བསྟན་པ་ཡིན་ནོ། །

[Block 976]
དེ་ཡང་རྣམ་པར་དབྱེ་ན་རྣམ་པ་བཞི་སྟེ། མངོན་པའི་ང་རྒྱལ་གྱི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་དང་། མངོན་པའི་ང་རྒྱལ་གྱི་གཉེན་པོའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་དང་། དེ་དག་གི་དཔེའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་དང་། དེ་དག་གི་དངོས་པོ་བསྡུས་པའི་མཚན་ཉིད་རྣམ་པར་གཞག་པའོ། །

[Block 977]
དེ་ལ་མངོན་པའི་ང་རྒྱལ་གྱི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ནི། རབ་འབྱོར་ཁྱོད་ཀྱིས༌[^750]སེམས་ཅན་གྱི་ཁམས་ན་གང་དག་མངོན་པའི་ང་རྒྱལ་ཅན་ཞེས་བྱ་བ་ནས། འདི་ནས་སླད་རོལ་པའི་མུ་སྟེགས་ཅན་རྣམས་ཀྱིས་སྨོས་ཀྱང་ཅི་འཚལ་ཞེས་གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 978]
མངོན་པའི་ང་རྒྱལ་གྱི༌[^751]གཉེན་པོའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ནི། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རབ་འབྱོར་དེ་དེ་བཞིན་ནོ། །

[Block 979]
དེ་དེ་བཞིན་ཏེ་ཞེས་བྱ་བ་ནས་རབ་འབྱོར་རྣམ་གྲངས་དེས་ཀྱང་ཁྱོད་ཀྱིས༌[^752]འདི་ལྟར་ཐམས་ཅད་དུ་རོ་གཅིག་པའི་མཚན་ཉིད་གང་ཡིན་པ༌[^753]ནི་དོན་དམ་པ་ཡིན་པར་རིག་པར་བྱའོ་ཞེས་གསུངས་པའི་ཚར་ཐར་མའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 980]
དེ་དག་གི་དཔེའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ནི། རབ་འབྱོར་འདི་ལྟ་སྟེ་དཔེར་ན་ནམ་མཁའ་ནི་ཞེས་བྱ་བ་ནས་ཐམས་ཅད་དུ་རོ་གཅིག་པའི་མཚན་ཉིད་ཡིན་པར་བལྟ་བར་བྱའོ་ཞེས་གསུངས་པའི་བར་གྱིས་བསྟན་ཏོ། །

[Block 981]
དེ་དག་གི་དངོས་པོ་བསྡུ་བའི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ནི། དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་དེའི་ཚེ་ཚིགས་སུ་བཅད་པ་འདི་བཀའ་སྩལ་ཏོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་སུ་བཅད་པ་གཅིག་གིས་དོན་དམ་པ་ཐམས་ཅད་རོ་གཅིག་པའི་མཚན་ཉིད་དང་ལྡན་པའི་ཚིག་གི་དོན་དེ་དག་གི་དངོས་པོ་བསྡུ་བ་བསྟན༌[^754]པ་དང་སྦྱར་རོ། །

[Block 982 [HEADING]]
##### མངོན་པའི་ང་རྒྱལ་གྱི་མཚན་ཉིད་རྣམ་པར་གཞག་པ། ^4-1-4-1-0

[Block 983]
དེ་ལ་དང་པོར་མངོན་པའི་ང་རྒྱལ་གྱི་མཚན་ཉིད་རྣམ་པར་གཞག་པ༌[^755]ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། མངོན་པའི་ང་རྒྱལ་གྱི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་ནི་གང་ཟག་ཁ་ཅིག་ཆོས་རྣམས་ཀྱི་དེ་བཞིན་ཉིད་དོན་དམ་པ་ཆོས་བདག་མེད་པ་ཐམས་ཅད་དུ་རོ་གཅིག་པའི་མཚན་ཉིད་དང་ལྡན་པ་ཁོང་དུ༌[^756]ཆུད་པར་ཕུང་པོ་ལ་སོགས་པ་དངོས་པོ་རེ་རེའི་མཚན་ཉིད་ཐ་དད་པ་རྟོགས་པ་ཙམ་གྱི་སྒོ་ནས། དོན་དམ་པ་རྟོགས་སོ་སྙམ་དུ་སེམས་ཤིང་རང་གི་ཤེས་པ་གཞན་ལ་བརྡ་སྤྲོད་པར་བྱེད་པ་གང་ཡིན་པའོ། །

[Block 984]
དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། རབ་འབྱོར་ཁྱོད་ཀྱིས༌[^757]སེམས་ཅན་གྱི་ཁམས་ན་གང་དག་མངོན་པའི་ང་རྒྱལ་ཅན་མངོན་པའི་ང་རྒྱལ༌[^758]གྱིས་མངོན་དུ་ཟིན་ཅིང་ཤེས་པ་བརྡ་སྤྲོད་པར་བྱེད་པའི༌[^759]སེམས་ཅན་ནི་ཇི་ཙམ་ཞིག༌[^760]ཡོད་པར་ཤེས་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 985]
དེ་ལ་འདིར་མངོན་པའི་ང་རྒྱལ་གྱི་མཚན་ཉིད་རྣམ་པར་གཞག་པ་ནི་རྣམ་པ་གསུམ་སྟེ་གཟུང་བའི་མངོན་པའི་ང་རྒྱལ་དང་། འཛིན་པའི་མངོན་པའི་ང་རྒྱལ་དང་། མཚན་ཉིད་རབ་ཏུ་དབྱེ་བའི་མངོན་པའི་ང་རྒྱལ་ལོ། །
--- END BLOCKS ---
