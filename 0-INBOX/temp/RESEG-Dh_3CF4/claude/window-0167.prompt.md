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
[Block 5846]
གྱ་གྱུ་ཚུལ་ཞིག་པ་མཐོང་བ་གང་ཡིན་པ་དེ་ནི་གྱ་གྱུ་ཚུལ་ཞིག་གལ་ཏེ་མཐོང་གྱུར་པའོ། །

[Block 5847]
སྔ་མ་དང་ཕྱི་མ་གཉིས་འགལ་བ་ཡིན་པས་སྔ་མ་དང་ཕྱི་མ་གཉིས་འཁྲུལ་པར་སྣང་བའི་ཕྱིར་རོ། །

[Block 5848]
གང་དུ་ལེགས་པར་སྤྱོད་པ་མ་མཐོང་བ་དེ་ནི་ལེགས་པར་སྤྱོད་པ་གལ་ཏེ་མ་མཐོང་བ་སྟེ། དགེ་བའི་ཆོས་མ་མཐོང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5849]
རྒྱུ་གསུམ་གྱིས་ནི་སླར་བཟློག་པར༌[^3745]མི་འགྱུར་ཏེ། ཁྱོད་ལ་འཇིགས་པར་འགྱུར་བའམ། བདེ་བ་ལ་ཆགས་པའམ་ཁྱོད་ལ་སྙིང་རྗེ་མེད་པར་གྱུར་པ་སྟེ། རྒྱུ་གསུམ་པོ་འདི་དག་ནི་ཡོད་པར་གྱུར༌[^3746]ན་ནི་ཕུབ་དང་། མཚོན་ཆ་མེད་པར་ཁྱོད་ཀྱི་གན་དུ་འོངས་པ་ཡང་མ་ཡིན་ཏེ། དེ་བས་ན་གང་གི་ཕྱིར་སྔར་ཉིད་མི་འོང་བ་ཉིད་དོ་དེ་བས་ན་དེ་ཉིད་དུ་འོང་བའི་རྒྱུ་ཉིད་དུ་རྟོགས་པར་བྱའོ། །

[Block 5850]
བྲམ་ཟེ་དེའི་དོན་བྱས་ནས་སླར་ཡང་ང་བདག་ཁྱོད་ཀྱི་དྲུང་དུ་འོང་ངོ་། །ཅིའི་ཕྱིར་ཞེ་ན། ཁྱོད་དང་ལྷན་ཅིག་བཤེས་ཤིང་འདྲིས་པའི་ཕྱིར་དང་། གང་གི་ཕྱིར་བདག་ཅག་ལྟ་བུ་ནི་དེ་ལྟ་བུའི་བརྫུན་གྱི་ཚིག་མི་སྨྲ་བ་དེའི་ཕྱིར་རོ། །

[Block 5851]
དེ་ལ་མགུ་བར་བྱ་བ་ནི་ལེགས་པར་སྨྲ་བ་དེ་ལ་ལེགས་པར་སྦྱིན་པའོ། །

[Block 5852]
ཚིག་སྙན་པ་ནི་ལེགས༌[^3747]པར་གསུངས་པའི་སྦྱིན་པ་ལ་གང་གིས་མཆོད་པའོ། །

[Block 5853]
བཀུར་སྟི་ནི་ལེགས་པར་བཤད་པ་སྟོན་པ་ལ་ལུས་ཀྱིས་མཆོད་པའོ། །

[Block 5854]
ཚིགས་བཅད་གཅིག་ལ་སྲང་སྟོང་དུ་བྱས་པར་སྟོན་ཏེ། [^3748]དེའི་ཐད་དུ་བརྩིས་པ༌[^3749]ཞེས་སྨོས་པ་ནི་དེ་དང་ཚད་མཉམ་པའི་ནོར་བཞག་སྟེ། གསེར་ལ་སོགས་པ་གལ་ཏེ་འདོད་པས་དེ་ལ་མཆོད་པར་བྱས་སོ། །

[Block 5855]
དེ་ཉིད་བསྟན་པའི་ཕྱིར། གནས་མ་ཡིན་པ་ལ་ལྷག་པར་གོད་པ་ནི་གནས་མ་ཡིན་པ་གོད་ཚབས་ཆེ་བའོ། །

[Block 5856]
དེ་ལས་བཟློག་པ༌[^3750]ནི་གནས་མ་ཡིན་པར་གོད་ཚབས་ཆེ་བ་དེ་ལ་དགག་པར་རྩོལ་བའི་སེམས་ཏེ། གནས་མ་ཡིན་པར་གོད་ཚབས་ཆེ་བ་དགག་པའི་བསམ་པའོ། །

[Block 5857]
ལེགས་པར་ཤེས་པར་བྱ་བའི་རིགས་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། འབངས་མང་པོ་གསོ་དགོས་པའི་ཕྱིར་རོ། །

[Block 5858]
རྒྱལ་པོའི་དཔལ་ཡང་ནོར་ཕུན་སུམ་ཚོགས་པ་ལ་ལྟོས་པའི་ཕྱིར་གོད་པ་ཚད་དང་ལྡན་པར་བྱ་བ་ཡིན་ཏེ། འདི་ལྟར་ཚིགས་བཅད་གཅིག་ལ་སྲང་སྟོང་དུ་བྱས་ཏེ་བྱིན་པས་ནོར་གྱི་དབང་ཕྱུག་གི་ནོར་ཡང་ཟད་པར་འགྱུར་རོ། །

[Block 5859]
འབངས་མང་པོ་གསོ་དགོས་སོ་ཞེས་བསྟན་པ་ལ། དེ་ནི་མི་ནུས་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། སྦྱིན་པ་དྲགས༌[^3751]ན་ཞེས་བྱ་བའི་ཕྱེད་དང་པོ་སྨོས་ཏེ། ནོར་གྱི་དབང་ཕྱུག་གི་ནོར་ཡོད་པ་ཡང་ཇི་སྲིད་ཅིག༌[^3752]ཏུ་ཐུག་པར༌[^3753]འགྱུར་ཞེས་བྱ་བ་བསྟན་པ་འདིས་ནི་ནོར་མེད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5860]
ནོར་མེད་ན་ནི་འབངས་མང་པོ་གསོ་བར་བྱ་བ་དེ༌[^3754]མི་ནུས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5861]
རྒྱལ་པོའི་དཔལ་ཡང་ནོར་ཕུན་སུམ་ཚོགས་པ་ལ་ལྟོས་སོ་ཞེས་བྱ་བ་དེ་བསྒྲུབ་པའི་ཕྱིར། ནོར་དང་རབ་ཏུ་ལྡན་ན་བསྒྲུབ་པར་ནུས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5862]
རྒྱལ་པོའི་དཔལ་ནོར་ཕུན་སུམ་ཚོགས་པ་ལ་ལྟོས་པ་ཅིའི་ཕྱིར་ཞེ་ན། ནོར་དང་རབ་ཏུ་ལྡན་ན་བསྒྲུབ་པར་ནུས་པའི་ཕྱིར་ཏེ། གང་ལ་ནོར་ཡོད་པ་དེ་ལ་རྒྱལ་པོའི་དཔལ་ཡོད་དེ། དེ་ལྟར་ན་ནོར་ཡོད་པ་ཉིད་ཀྱིས་རྒྱལ་པོའི་དཔལ་ཡོད་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5863]
ནོར་མེད་ན་ནི་རྒྱལ་པོའི་དཔལ་མེད་པའི་དབང་དུ་བྱས་ནས། ནོར་མེད་ན་ནི༌[^3755]རྒྱལ་པོའི་དཔལ་དེ་ཡང་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་འོག་མའོ། །

[Block 5864]
དེ་ལྟར་འདི་གཉིས་ཀྱིས་དེ་ཡོད་ན་ནི་ཡོད་ལ་མེད་ན་ནི༌[^3756]མེད་པའི་ཕྱིར་རྒྱུ་དང་རྒྱུན་ཅན་གྱི་མཚན་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5865 [VERSE]]
ལེགས་པར་སྨྲས་པའི་མཆོད་པ་མང་ན་བརྒྱ། །
དེ་ལས་མང༌[^3757]ན་ནུས་པར་མི་འགྱུར་ཏེ། །

[Block 5866]
ཞེས་བྱ་བ་རྒྱལ་པོས་སྨྲས་པ་དེའི་ལན་ལས་བརྩམས་ཏེ། ལེགས་པར་སྨྲས་པ་རྣམས་ཀྱི་རིན་ཐང་ཞིག །ཅེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5867]
རིན་ཐང་གི་ཚད་ནི་རིན་ཐང་ངེས་པ་སྟེ། རིན་ཐང་གི་ཚད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 5868]
ཁྱོད་ཀྱང་དམའ་བར་ག་ལ་འགྱུར། །ཞེས་བྱ་བ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། ལེགས་པར་བཤད་པ་ལ་མཆོད་པ་སྦྱིན་པར་བྱ་བའི་དོན་དུ་ནི་རྒྱལ་སྲིད་ཀྱང་རིང་དུ་མཆོད་པ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5869]
རིན་ཐང་བཅད་པར་མི་ནུས་པའི་གཏན་ཚིགས་བསྟན་པའི་ཕྱིར། གང་ཞིག་ཐོས་ནས་ཡིད་ནི་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5870]
འདིའི་བསྡུས་པའི་དོན་ནི་ཐོག་མ་དང་། བར་མ་དང་།[^3758] ཐ་མ་དགེ་བའི་ཕྱིར། ལེགས་པར་བཤད་པའི་རིན་ངེས་པར་བཅད་དུ་མི་རུང་ངོ་ཞེས་སྟོན་ཏོ། །

[Block 5871]
ཐོག་མར་དགེ་བ་གང་ཞེ་ན། ཐོས་ཤིང་ཉན་པའི་ཚེ་ན་ཡིད་དགའ་བར་འགྱུར་བ་ཡིན་ཏེ། དེ་ཡང་། གང་ཞིག་ཐོས་ནས་ཡིད་ནི་དད་འགྱུར་བ། །ཞེས་བྱ་བ་འདིས་བསྟན་ཏོ། །

[Block 5872]
བར་དུ་དགེ་བ་གང་ཞེ་ན། བསམ་པ་དང་ལྡན་ཞིང་ཉེ་བར་གནས་པ་སྟེ། བསམ་པས་བསམས་པ༌[^3759]དེ་ནི་ལེགས་པར་དགའ་ལ་བརྟན་པར་འགྱུར་བའོ། །

[Block 5873]
ཐ་མར་དགེ་བ་གང་ཞེ་ན། བསྒོམས་པ༌[^3760]དེས་ཤེས་རབ་སྐྱེ་ཞིང་གཏི་མུག་མེད་པར་འགྱུར་བ་སྟེ། གཏི་མུག་ནི་མ་རིག་པ་སྤངས་པ་སྟེ། དེ་སྤངས་པའི་ཕྱིར་ཡང་བྱ་བ་བྱས་པའི་ཕྱིར་རོ། །

[Block 5874]
རང་གི་ཤས་ཀྱང་དེ་ནི་ཉོ་བའི་རིགས། །ཞེས་བྱ་བ་ནི་ནང་གི་ལུས་ཀྱིས་ཀྱང་ཉོ་བར་བྱ་བ་ཡིན་ན། ཕྱི་རོལ་གྱི་དངོས་པོ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 5875]
ཐོས་པ་གཏི་མུག་ཅེས་བྱ་བའི་ཚིགས་བཅད་འདི་ནི་འཇིག་རྟེན་ལས་འདས་པའི་ཡོན་ཏན་དང་རྗེས་སུ་མཐུན་པའི་དབང་དུ་བྱས་པ་སྟེ། གཏི་མུག་མུན་སེལ་ཞེས་བྱ་བས་ནི་མཐོང་བའི་ལམ་གྱི་རྒྱུས་མཐོང་བའི་ལམ་གྱི་མི་མཐུན་པ་མ་རིག་པ༌[^3761]སྤོང་བའི་གཉེན་པོ་ཐོས་པ་མ༌[^3762]ཡིན་པའི་ཕྱིར་རོ། །

[Block 5876]
ཐོས་པ་ནི་སྒྲོན་མའོ། །

[Block 5877]
ཐོས་པ་ནི་ནོར་གྱི་མཆོག་སྟེ། འཇིག་རྟེན་ལས་འདས་པའི་འཕགས་པའི༌[^3763]ནོར་གྱི་རྒྱུས་དེའི་ཚེ་དང་བཤེས་པའོ། །

[Block 5878]
ཐོས་པ་ནི་ཀུན་དུ་རྨོངས་པའི་སྒྲ་འཇོམས་པའི་མཚོན་ཆ་ཡིན་ཏེ། བསྒོམ་པའི་ལམ་གང་གི་བག་ཆགས་དང་བཅས་པ་སྤོང་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 5879]
ཐོས་པ་ནི། ཐབས་ཚུལ་མན་ངག་སྟོན་པའི་གྲོགས་ཀྱི་མཆོག །ཅེས་བྱ་བ་ཡིན་ཏེ། དེ་ལ་ལྷག་པར་བསྒོམ་པས༌[^3764]སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་སྤོང་བར་སྒྲུབ་པ་ནི་གཞན་གྱིས་བསྟན་པ་མེད་པར་ཐོས་པའི་འབྲས་བུ་ཉིད་ཀྱིས་བསྒོམ་པའི་ལམ་བསྒྲུབ་པའི་ཐབས་སྟོན་པའི་ཕྱིར་རོ། །

[Block 5880]
ད་ནི་མཐོང་བའི་ཆོས་ཉིད་ལ་ཕན་འདོགས་པའི་དབང་དུ་བྱས་ནས་ཕོངས་པར་གྱུར་ཀྱང་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 5881]
མཐོང་བའི་ཆོས་ལ་ཕན་འདོགས་པ་ཡང་རྣམ་པ་གཉིས་ཏེ། ཕོངས་པ་ལས་བཟློག་པའི༌[^3765]ཕན་འདོགས་པ་དང་།

[Block 5882 [VERSE]]
ཕན་ཡོན་སྐྱེད་པར་བྱེད་པའི་ཕན་འདོགས་པའོ། །
ཕོངས་པར་གྱུར་ཀྱང་མི་འགྱུར་མཛའ་བོ་ཡིན། །

[Block 5883]
ཞེས་བྱ་བ་ནི། བཅིང་པ་ལ་སོགས་པའི་ཕོངས་པ་སེལ་བའི་ཕྱིར་རོ། །

[Block 5884]
སེམས་ཀྱི་ནད་མྱ་ངན་གྱི་མཚན་ཉིད་ལ་ཐོས་པ་ནི་སྨན་ཡིན་ཏེ། མྱ་ངན་སེལ་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 5885]
ཐོས་པ་ནི་དཔུང་ཡིན་ཏེ་སོ་སོར་བརྟགས་ཏེ་ཡང་དག་པར་བླངས་ནས་འདོད་ཆགས་ལ་སོགས་པ་ཉེས་པ་རྣམས་ཀྱི་དཔུང་འཇིག་པར་བྱེད་པའི་རྒྱུར་གྱུར་པ་སྟེ། དེ་ཡང་འདོད་ཆགས་ལ་སོགས་པའི་ཉེས་པ་སོ་སོར་བརྟགས༌[^3766]པའི་སྟོབས་ཀྱི༌[^3767]ཟིལ་གྱིས་མནན་པ་ཡིན་པའི་ཕྱིར་ཉེས་པ་འཇོམས་པས་དཔུང་གི་མཆོག་གོ། །
--- END BLOCKS ---
