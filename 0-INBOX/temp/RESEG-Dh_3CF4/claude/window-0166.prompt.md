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
[Block 5811]
ཤིང་རྟ་དང་། རྟ་དང་། གླང་པོ་ཆེ་དང་། དམག་མི་བརྟན་པ་ཉམས་པར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི། ཤིང་རྟ་དང་། རྟ་དང་། གླང་པོ་ཆེ་དང་། དམག་མི་བརྟན་པ་ཉམས་པར་གྱུར་པའོ། །

[Block 5812]
ཅི་ལེགས་མཛད་པ་ནི་གོ་ཆ་བགོ་བ་ལ་སོགས་པའོ། །

[Block 5813]
ངང་ཚུལ་གྱི་སྐྱོན་ཤེས་པ་གང་ཡིན་པ་དེ་ནི་དེ་སྟེ། ངང་ཚུལ་གྱི་སྐྱོན་ནི་མ་བསྔགས་པའི་དངོས་པོ་ཡིན་ནོ། །

[Block 5814]
སྔར་ཆབ་སྒོ་པས་བསྟེན་པའི༌[^3713]སྟེ། ལྷ་དེ་ལས་ཅི་ལེགས་པར་མཛད་ཅིང་བཀའ་གྲོས་མཛད་པའི་དུས་ལ་བབ་པོ་ཞེས་གསོལ་ཏོ་ཞེས་བྱ་བ་དེ་གཉི་ག་དུས་ལ་བབ་པ་ཉིད་དུ་བསྟན་པ་དེའི་དེ་ལྟར་མི་བྱ་བའི་རྒྱུ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། མི་ཤ་འདོད་པ་ཞེས་བྱ་བ་དང་། བདག་གིས་བརྒལ་བའི་གོ་སྐབས་ཞེས་བྱ་བའི་ཚིགས་བཅད་གཉིས་སྨོས་སོ། །

[Block 5815]
མི་ཤ་འདོད་པས་རྒྱལ་སྲིད་ཉམས་པར་གྱུར། །ཞེས་བྱ་བས་ནི་འདོད་པ་ཉམས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5816]
སྨྱོས་པ་ལྟ་བུར་གྱུར་པ་ནི་སྨྱོས་པ་བཞིན་དུ་གྱུར་པ་སྟེ། སྨྱོས་པ་ཞེས་བྱ་བ༌[^3714]འདིས་ནི་དོན་ཉམས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5817]
རང་གི་ཆོས་བཏང་ཞེས་བྱ་བས་ནི་ཆོས་ཡོངས་སུ་སྤངས་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5818]
རང་གི་ཆོས་བཏང་བ་ཉིད་ཀྱིས་བསོད་ནམས་དང་གྲགས་པ་ཡང་ཉམས་པ་ཉིད་དོ། །

[Block 5819]
འདིར་བསོད་ནམས་ཞེས་སྨོས་པ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་འབྲས་བུ་ལ་དགོངས་ཏེ། འདིས་ནི་འཇིག་རྟེན་ཕ་རོལ་གྱི་མངོན་པར་མཐོ་བའི་འབྲས་བུ་ཉམས་པ་ཉིད་དུ་སྟོན༌[^3715]ཏོ། །

[Block 5820]
གྲགས་པ་ཞེས་སྨོས་པས་ནི་མཐོང་བའི་ཆོས་ཀྱི་འབྲས་བུ་ཉམས་པ་ཉིད་དུ་སྟོན༌[^3716]ཏོ། །

[Block 5821]
མྱ་ངན་བྱ་བའི་གནས་སྐབས་གནས་པ་ལ། །ཞེས་བྱ་བའི་རྒྱུ་བཞི་པོ་དེ་དག་ཉིད་ཀྱིས་སོ། །

[Block 5822]
བདག་གིས༌[^3717]བརྒལ་བའི་སྒོ་སྐབས༌[^3718]ག་ལ་ཡོད། །ཅེས་བྱ་བས་ནི་ལྷ་དེ་ལ་ཅི༌[^3719]ལེགས་པར་མཛད་པར་གསོལ་ཞེས་བྱ་བ་དེའི་ལན་ནོ། །

[Block 5823]
དེ་ལྟ་བུ་ལ་འཇིགས་སུ་ག་ལ་རུང་། །ཞེས་བྱ་བ་ནི་གང་སྔར་བསྟན་པའི༌[^3720]བཀའ་གྲོས་མཛད་པའི་དུས་ལ་བབ་པོ་ཞེས་བྱ་བ་དེའི་ལན་བསྟན་པ་ཡིན་ནོ། །

[Block 5824]
འཐབ་མོ༌[^3721]མེད་པས་ན་འཐབ་མོ༌[^3722]མེད་པའོ། །

[Block 5825]
འཐབ་མོ༌[^3723]ཡང་ཡིན་ལ་བརྒལ་བ་ཡང་ཡིན་པས་འཐབ་མོ༌[^3724]བརྒལ་བ་སྟེ་དེས་སོ། །

[Block 5826]
མངོན་དུ་ཞེས་བྱ་བ་ནི་རྩ་བ་ལས་སོ། །

[Block 5827]
རྗེས་སུ་གཟུང་བ༌[^3725]ཞེས་བྱ་བ་ནི་སྡིག་པ་གཞོམ་པ་ལའོ། །

[Block 5828]
དེ་ལས༌[^3726]ཞེས་བྱ་བ་ནི་བདག་གི་དྲུང་དུ་ཁོ་དག་འོངས་པའི་ཕྱིར་རོ། །

[Block 5829]
དམ་པ་རྣམས་ནི་དེ་ལྟར་མགྲོན་ཡང་བྱེད། །ཅེས་བྱ་བ་སྙིང་རྗེ་དང་ལྡན་པ་རྣམས་མགྲོན་བྱེད་པའི་ངང་ཚུལ་ཅན་ཡིན་ནོ། །

[Block 5830]
མི་དགའ་ཞིང་ཡིད༌[^3727]བློང་བས་མིག་མཆི་མས་གང་བ་དེ་ནི་མི་དགའ་ཞིང་ཡིད་བློང་བས་མིག་མཆི་མས་གང་བའོ། །

[Block 5831]
དྲི་མ་ཅན་གྱི་གོས་བསྲིངས་ཏེ། རྐེད་པ་བཅིངས་པ་གང་ཡིན་པ་དེ་ནི་གོས་དྲི་མ་ཅན་བསྲིངས་ཏེ་རྐེད་པ་བཅིངས་པའོ། །

[Block 5832]
རྔུལ་གྱིས༌[^3728]གོས་ཤིང་རིང་ལ་ཡེགས་པ༌[^3729]དེ་ལ༌[^3730]ཤིང་ཤུན་གྱི༌[^3731]ཐོད་ཀྱིས་བཅིངས་པ་སྟེ། རྔུལ་གྱིས་གོས་ཤིང་རྩུབ་པས་རིང་ཞིང་ཡེགས་པའི༌[^3732]སྐྲ་གང་ཡིན་པ་དེ་ཤིང་ཤུན་གྱི་ཐོད་ཀྱིས་བཅིངས་པའོ། །

[Block 5833]
ཁ་སྤུ་རིང་པོ་འཛིངས་པ༌[^3733]དེས་གདོང་ངམས༌[^3734]གནག་པར་གྱུར་པ་གང་ཡིན་པ་དེ་ནི་གདོང་གི་ཁ་སྤུ་རིང་པོས་ངམས་གནག༌[^3735]པར་གྱུར་པའོ། །

[Block 5834]
ཁྲོས་པ་དང་རྔམ་པ་ནི་ཁྲོས་ཤིང་རྔམ་པའོ། །

[Block 5835]
བགྲད་པ༌[^3736]དང་འཇིགས་འཇིགས་ལྟར་འདུག་པ་ནི་བགྲད་པ༌[^3737]དང་འཇིགས་འཇིགས་ལྟར་འདུག་པ་སྟེ། ཁྲོས་ཤིང་རྔམ་པ་གཉིས་ཀྱིས་བགྲད༌[^3738]པའི་མིག་གང་ལ་ཡོད་པ་དེ་ནི་ཁྲོས་ཤིང་རྔམ་པས་མིག་བགྲད༌[^3739]པའོ། །

[Block 5836]
གཅིག་པུ་ཕུབ་དང་མཚོན་མེད་ཅེས་བྱ་བས་ནི་སུ་དཱ་སའི་བུ་ལ་སྔར་བསྟན་པའི་བརྒལ་བ༌[^3740]མེད་པ་ཉིད་དུ་བསྟན་པའོ།[^3741] །རང་བཞིན་གྱིས་ཞི་བར་སྣང་བ་ཞེས་བྱ་བས་ནི་སྔར་བསྟན་པ་འདི་ལྟ་བུ་ལ་འཇིགས་སུ་ག་ལ་རུང་ཞེས་བྱ་བ་དེ་སྟོན་པ་སྟེ། འཇིགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 5837]
རྔམ་པ་དང་དྲེགས་པ་གཉིས་ཀྱིས་གཡེངས་པའི་སེམས་གང་ཡིན་པ་དེ་ནི་སེམས་རྔམ་ཞིང་དྲེགས་པས་གཡེངས་པའོ། །

[Block 5838]
སྲིན་པོ་དང་ཡི་དགས་གར་བྱེད་པ་བཞིན་དུ་འཇིགས་པ་ནི། སྲིན་པོ་དང་ཡི་དགས་གར་བྱེད་པ་བཞིན་དུ་འཇིགས་པའོ། །

[Block 5839]
འདོད་པ་ནི་ནོར་ལ་སོགས་པ་ལ་ཆགས་པའོ། །

[Block 5840]
ཤིར་དོགས་པ་ནི་སྲོག་གི་འཇིགས༌[^3742]པའོ། །

[Block 5841]
ཡ་རབས་ནི་བདེན་པ་ལ་སོགས༌[^3743]དང་འདྲ་བ་ཞེས་བྱ་བ་ནི་དེ་བས་ན་འདོད་པ་ལ་སོགས་པའི་ཕྱིར་ཡོངས་སུ་མི་གཏོང་བས་སོ། །

[Block 5842]
དམ་པ་རྣམས་ནི་བདེན་པ་སྲོག་གི་ཕྱིར་ཡང་མི་གཏོང་སྟེ། ཇི་ལྟར་མི་གཏོང་ཞེ་ན། དེའི་ཕྱིར་བདེན་པ་དང་འབྱོར་པའི་དོན་དེ་བདེ་བའོ། །

[Block 5843]
བདེན་པ་ཉམས་ན་ནི་ངན་འགྲོ་དག་ལས་སྲུན་མི་ནུས་པ་ཡིན་ཏེ། ཇི་ལྟར་དམ་པ་རྣམས་ཀྱི་བདེན་པ་སྲོག་དང་འདྲ་བ་ཡིན་ཞེ་ན། སྨྲས་པ། གསོན་ཞིང་བདེན་པ་ཉམས་པ་ནི་ངན་འགྲོ་ལས་སྲུན་མི་ནུས་པའི་ཕྱིར་ཏེ། དེའི་ཕྱིར་ནོར་དང་སྲོག་དག་ལས་མི་ནུས་ཤིང་། འཆི་བའི་དུས་སུ་ཡིད་ལ་གཅགས་ཏེ་འཆི་བའི་ཕྱིར་རོ། །

[Block 5844]
གྲགས་པ་ནི་མཐོང་བའི་ཆོས་ཀྱི་བདེན་པའོ། །

[Block 5845]
བདེ་བ༌[^3744]ནི་མཐོ་རིས་སུ་འགྲོ་བའོ། །

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
--- END BLOCKS ---
