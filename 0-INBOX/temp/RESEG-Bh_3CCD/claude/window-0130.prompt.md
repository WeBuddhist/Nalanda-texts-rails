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
[Block 4551]
ལ་ལ་ན་རེ་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུའི་ངོ་བོ་ཡིན་ལ་དེ་བཞིན་གཤེགས་པ་རྣམས་ནི་སྤྲུལ་པའི་སྐུའི་རང་བཞིན་ཡིན་ནོ་ཞེས་ལོངས་སྤྱོད་རྫོགས་པ་དང་སྤྲུལ་པའི་སྐུ་གཉིས་དབྱེར་མེད་པའི་ཕྱིར་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཁོ་ནས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 4552]
དབྱེར་མེད༌[^2744]ཡང་འགྲོ་བའི་དོན་དུ་གཅིག་པའི་ཕྱིར་རོ། །

[Block 4553]
བྱང་ཆུབ་ཀྱི་སེམས་རབ་ཏུ་སྟོན་པ་ཞེས་པ་ལ་བྱང་ཆུབ་སེམས་ནི་བསྐྱེད་པའི་རིམ་པའི་ཕྱོགས་སུ་སྟོང་པ་ཉིད་དོ། །

[Block 4554]
དེ་གསལ་བར་བྱེད་པས་ན༌[^2745]བྱང་ཆུབ་ཀྱི་སེམས་རབ་ཏུ་སྟོན་པའོ། །

[Block 4555]
དེ་ནས་རྫོགས་པའི་རིམ་པའི་ཕྱོགས་སུ༌[^2746]རྡོ་རྗེ་བཟླས་པ་ལ་སོགས་པའི་རིམ་པ་ལྔས༌[^2747]ཐོབ་པར་བྱ་བའི་སྟོང་པ་ཉིད་དང་སྙིང་རྗེ་དབྱེར་མེད་པའི་ངོ་བོ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་གོ་འཕང་ནི་བྱང་ཆུབ་ཀྱི་སེམས་སོ། །

[Block 4556]
དེ་གསལ་བར་བྱེད་པས་ན་བྱང་ཆུབ་ཀྱི་སེམས་རབ་ཏུ་སྟོན་པའོ། །

[Block 4557 [VERSE]]
སྟོང་ཉིད༌[^2748]སྙིང་རྗེ་དབྱེར་མེད་པའི། །
བྱང་ཆུབ་སེམས་ཞེས་བཤད་པ་ཡིན། །
ཞེས་རྒྱུད་ཕྱི་མ་ལས་འབྱུང་ངོ་། །
ལེའུའི་སྒྲའི་དོན་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 4558]
སྒྲོན་མ་གསལ་བར་བྱེད་པའི་འགྲེལ་པའི་ཊཱི་ཀཱ་ལས་ལེའུ་གཉིས་པའོ།། །།

[Block 4559 [HEADING]]
## ལྷའི་ལེའུ་གསུམ་པ། ^3-0

[Block 4560]
རྣལ་འབྱོར་པ་རྣམ་པ་གཉིས་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པས་ལྷའི་ལེའུ་གསུམ་པ་བསྟན་པར་བྱ་སྟེ། གང་གི་ཕྱིར་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ལེའུ་ལས་སྟོང་པ་ཉིད་ཐོབ་ནས་དེ་ནས་བསྐྱེད་པའི་རིམ་པས་ལྷའི་འཁོར་ལོ་བསྒོམ་པར་བྱའོ། །

[Block 4561]
དེ་བཞིན་དུ་དང་པོ་སྦྱོར་བ་དང་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་ཡོངས་སུ་རྫོགས་ནས་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གསལ་བར་བྱ་བའི་ཕྱིར༌[^2749]ཕྲ་མོའི་རྣལ་འབྱོར་བསྒོམ་པར་བྱའོ། །

[Block 4562]
རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་པས་ཕྲ་མོའི་རྣལ་འབྱོར་བསྒོམ་པར་བྱ་བའི་ཕྱིར་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་བསྟན་པར་བྱའོ། །

[Block 4563]
རྣལ་འབྱོར་པ་གཉིས་ཀྱི་ནི་བསྐྱེད་པ་དང་རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་པ༌[^2750]དག་གིས་སོ། །

[Block 4564]
ཕྲ་མོའི་རྣལ་འབྱོར་བསྒོམ་པ་གཉིས་བྱའོ་ཞེས་པ་ལ༌[^2751]བསྐྱེད་པའི་རིམ་པའི་རྣལ་འབྱོར་པས་རྡོ་རྗེ་ལ་སོགས་པ་ཕྲ་མོའི་རྣལ་འབྱོར་བསྒོམ་པ་དང་། རྫོགས་པའི་རིམ་པའི་རྣལ་འབྱོར་པས་ཀྱང་འདོད་ཆགས་དང་ཞེ་སྡང་དང༌[^2752]གཏི་མུག་གི་རིགས་ཀྱི་དབྱེ་བས་གསང་བ་དང་སྙིང་ག་དང་གདོང་གི་སྣ་རྩེར་ཕྲ་མོའི་ཐིག་ལེ་བསྒོམ་པར་བྱའོ།[^2753] །

[Block 4565]
དེ་ལ་འདོད་ཆགས་ཀྱི་རིགས་ཅན་གྱི་རྣལ་འབྱོར་པས་སྟོང་ཕྲག་བདུན་ཅུ་རྩ་གཉིས་ཀྱི་རྩའི་ཁོང་སྟོང་ནས་རྒྱུ་བའི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེ་རྡོ་རྗེ་ནོར་བུའི་རྩེའམ། །པདྨའི་ལྟེ་བའི་རྩེར་ཡུངས་ཀར་གྱི་འབྲུའི་ཚད་ཙམ་གྱི་ཐིག་ལེ་བསྒོམ་པར་བྱའོ། །

[Block 4566]
ཞེ་སྡང་གི་རིགས་ཀྱི༌[^2754]རྣལ་འབྱོར་པས་ཡི་གེ་གསུམ་ཆ༌[^2755]ཤས་བསྡུས་ནས་ཐུགས་རྡོ་རྗེ་འཆང་གི་ས་བོན་གྱི་ཐིག་ལེ་ཙམ་སྙིང་གར་དམིགས་ལ་སྔགས་ཀྱི་ཐིག་ལེ་བསྒོམ་པར་བྱའོ། །

[Block 4567]
གཏི་མུག་གི་རིགས་ཅན་གྱིས་དཀྱིལ་འཁོར་བཞི་པོ་ལས་གཡས་དང་གཡོན་དང་དམན་པ་དང་དལ་བུས་རྒྱུ་བའི་དབྱེ་བས་སྤྲོས་པའི་འོད་ཟེར་གྱི་ཚོགས་ཀུན་རྫོབ་ཀྱི་སྣ་རྩེར་ཐིག་ལེའི་གཟུགས་བསྒོམ་པར་བྱའོ། །

[Block 4568]
དེ་བཞིན་དུ་རིན་ཆེན་འབྱུང་ལྡན་དང་དོན་ཡོད་གྲུབ་པའི་རྣལ་འབྱོར་པ་དག་གིས་ཀྱང་སྨིན་མཚམས་དང་ལྟེ་བའི་དཀྱིལ་དུ་ཐིག་ལེ་བསྒོམ་པར་བྱ་བ་ནི་ཕྲ་མོའི་རྣལ་འབྱོར་རྟོགས་པར་བྱའོ། །

[Block 4569]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་ཞེས་པ་ལ་ཕུང་པོ་ལྔ་དང་དེ་རྣམས་བསྡུ་བར་བྱེད་པ་སྐུ་ལ་སོགས་པའོ། །

[Block 4570]
དེ་དག་ཉེ་བར་སྡུད་པར་བྱེད་པའི་ཕྱིར་སྐུ་གསུང་ཐུགས་ཀྱི་རྡོ་རྗེ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་སྟེ་དྲུག་པའོ། །

[Block 4571]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ནི་མི་བསྐྱོད་པ་ལ་སོགས་པ་སྟེ་ཕྱག་རྒྱ་ལེགས་པར་སྦྱང་བའི་སྔོན་དུ་འགྲོ་བར་ཕྱུང་བའི་སྔགས་ཀྱི་རིམ་པས་དམ་ཚིག་གི་དཀྱིལ་འཁོར་དང་བསྒྲུབ་པའི༌[^2756]དཀྱིལ་འཁོར་སྤྲོས་ལ་ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་བདག་ཉིད་ཅན་གྱི་དེ་བཞིན་གཤེགས་པ་དང་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་ཁྲོ་བོ་རྣམས་སོ། །

[Block 4572]
དེ་རྣམས་ཀྱིས་སེམས་ཅན་གྱི་དོན་གྱི༌[^2757]ཕྱིར་ཞེས་པ་ནི་དེ་དག་གིས་འགྲོ་བའི་དོན་མཛད་པའི་ཕྱིར་རོ། །

[Block 4573]
ཕྱོགས་བཅུར་ཁྱབ་པ་ཞེས་པ་ལ་རེག་བྱ་རྡོ་རྗེ་མའི་ཆོས་འབྱུང་བའི་ནང་ནས་ཕྱི་རོལ་དུ་སྤྲོས་ཏེ་མངོན་པར་དགའ་བ་ལ་སོགས་པའི་སངས་རྒྱས་ཀྱི་ཞིང་དུ་འཇུག་པར་བྱ་བའི་ཕྱིར་ཕྱོགས་བཅུར་གཤེགས་པའོ། །

[Block 4574]
དེ་ཉིད་ནི་ཆོས་ཀྱི་ཆར་འབེབས་པས་ན༌[^2758]ཞེས་པ་ནི་ཉེ་བར་མཚོན་པ་ཙམ་ཡིན་ཏེ། །བརྟན་པ༌[^2759]དང་སྨིན་པ་དང་གྲོལ་བ་དང་སངས་རྒྱས་ཀྱི་ཞིང་ལ་འཇུག་པའི་ཕྱིར་རོ། །

[Block 4575]
དེ་ཉིད་ནི་སེམས་ཅན་བསམ་པ་སྣ་ཚོགས་པས་ཕྱེ་བ་ལ་ཞེས་པ་ནི་འདོད་ཆགས་ལ་སོགས་པའི་རིགས་ཅན་རྣམས་ཀྱིས་སེམས་ཅན་གྱི་བསམ༌[^2760]པའི་རྗེས་སུ་འབྲངས་ནས་བུད་མེད་དང་སྐྱེས་པའི་དབྱེ་བས་སྤྲོ་བ་དང་ཞི་བ་དང་དྲག་པོའི་གཟུགས་དང་སྒེག་པ་ལ་སོགས་པའི་ཉམས༌[^2761]དང་ལྡན་པའི་སྐུའི་དབྱེ་བས་ཀྱང་སྤྲོ་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4576]
སྐུ་དུ་མར་སྟོན་པའི་ཕྱིར་བཀོད་པའོ་ཞེས་པ་ནི་ཞལ་གསུམ་པ་ལ་སོགས་པ་དང་རིགས་སྣ་ཚོགས་པའི་རང་གི་སྐུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 4577]
གང་གི་ཕྱིར་རྡོ་རྗེ་འཆང་ཆེན་པོ་གཅིག་པུ་ཁོ་ན་ཆོས་ཀྱི་དབྱིངས་ཀྱི་རང་བཞིན་ཡིན་ན་ཡང་ཁ་དོག་ལྔ་དང་ཞི་བ་དང་དྲག་པོ་དང་ཕོ་དང་མོའི་དབྱེ་བས་རབ་ཏུ་སྣང་སྟེ། དེ་དོན་དམ་པར་དབྱེ་བ་ནི་མེད་དེ། འོད་གསལ་བའི་རང་བཞིན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4578]
དེ་ལྟ་བུའི་ཚུལ་གྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དང་པོའི་སྦྱོར་བ་ལ་སོགས་པའི་མཚན་ཉིད་ཅན་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4579]
རྡོ་རྗེ་ནི་དེ་བཞིན་གཤེགས་པ་རྣམས་སོ་ཞེས་པ་ལ་རྡོ་རྗེ་བཞིན་དུ་མེ་ལོང་ལྟ་བུ་ལ་སོགས་པའི་ཡེ་ཤེས་རྣམས་ཀྱིས༌[^2762]མི་ཕྱེད་པའི་ཕྱིར་རོ། །

[Block 4580]
འདིར་དེ་བཞིན་གཤེགས་པའི་སྒྲ་ནི་ཉེ་བར་མཚོན་པ་ཡིན་ཏེ་དེས་ན་དེའི་རིགས་ལས་འབྱུང་བའི་ལྷ་མོ་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་ཁྲོ་བོ་རྣམས་ཀྱང་གཟུང་ངོ་། །དེ་སྐད་ཅེས་བྱ་བའི་ཏིང་ངེ་འཛིན་གྱི་གཞིའི་ལེའུ་ཞེས་བྱ་བ་ལ། ཏིང་ངེ་འཛིན་ནི་གཞི་ཅན་ནོ། །

[Block 4581]
ལེའུ་ནི་གཞིའོ། །

[Block 4582]
གཞི་དང་གཞི་ཅན་གྱི་དབྱེར་མེད་པར་བྱས་ནས་ཏིང་ངེ་འཛིན་གྱི་ལེའུ་ཞེས་བསྟན་ཏེ། ཚེམ་བུ༌[^2763]ངུ་བ་བཞིན་ནོ། །

[Block 4583]
ཚེམ་བུ༌[^2764]ལ་གནས་པའི་བུ་ཆུང་ངུ་བ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 4584]
དེ་ལྟར་ཞེས་བྱ་བ་ལ་སོགས་པས་ལེའུའི་མིང་དོན་དང་ལྡན་པ་བསྟན་ཏོ། །

[Block 4585]
ལྷ་རྣམས་བསྐྱེད་པའི་ཡན་ལག་དག་ཏུ་གྱུར་པའི་གསང་སྔགས་དང་པོར་སྟོན་པ་ནི་ཞེས་པ་ལ་དང་པོ་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་ཏུ་གྱུར་པའི་རྣལ་འབྱོར་གྱི་ཕྱོགས་གཅིག་པ་སྟོང་པ་ཉིད་བསྒོམ་པ་བརྟན་པར་བྱེད་པའི་མཚན་ཉིད་ཀྱི་སྔགས་དང་པོ་བསྟན་པར་བྱའོ་ཞེས་པའི་དོན་ཏོ། །

[Block 4586]
ཨོཾ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་དོན་དམ་པའི་དཀྱིལ་འཁོར་བསྒོམས་པའི༌[^2765]འོག་ཏུ་སྔགས་འདི་བརྗོད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4587]
ཆོས་འབྱུང་བ་ལ་གནས་པའོ་ཞེས་པ་ནི་བགེགས་བསྐྲད་པ་དང་སྟོང་པ་ཉིད་བསྒོམས་པའི༌[^2766]འོག་ཏུ་ཡི་གེ་ཧཱུྃ་གི་ས་བོན་ལས་བསྐྱེད་པའི༌[^2767]གཞིའི་དཀྱིལ་འཁོར་གྱི་རང་བཞིན་གྱི་ཆོས་འབྱུང་གི་ཕྱག་རྒྱའི་སྟེང་དུ་ཡེ་ཤེས་ཀྱི་ས་གཞི་འབྱུང་བ་ཆེན་པོ་བཞིའི་རང་བཞིན་དང་རི་རབ་ཡོངས་སུ་གྱུར་པ་ལས།

[Block 4588]
རིན་ཆེན་སྣ་བདུན་གྱི་གཞལ་ཡས་ཁང་པའི་ནང་ན་སྣ་ཚོགས་པདྨ་དང་། ཟླ་བ་དང་། ཉི་མའི་དཀྱིལ་འཁོར་དུ་སྐད་ཅིག་གིས་རྫོགས་པའི་ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱིས་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་རྣམ་པར་བསྒོམ་པ་ལ། དེ་ཉིད་རྡོ་རྗེ་ཕྲེང་བ་ལས་གསུངས་པའི་གཟུགས་ཕུང་གཏོགས་པ་ཞེས་བྱ་བ་ལ་སོགས་པས་དོན་དམ་པའི་དཀྱིལ་འཁོར་དུ་བྱས་ལ། ཡབ་ཡུམ་རོ་གཅིག་པར་གྱུར་ནས་སྔགས་འདིས་བརྟན་པར༌[^2768]བྱས་ཏེ། ཡང་ཡི་གེ་གསུམ་ལས་བྱུང་བའི་པདྨ་དང་ཟླ་བ་དང་ཉི་མའི་སྟེང་དུ་ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་ཟླ་བའི་དཀྱིལ་འཁོར་ལ་སྔ་མའི་པདྨ་ལ་སོགས་པ་གསུམ་ཞུགས་ཏེ་ཆོས་ཀྱི་དབྱིངས་ཀྱི་སྔགས་ཀྱིས་རང་གི་སེམས་བརྟན་པར་བྱས་ལ། དེའི་སྟེང་དུ་ཡི་གེ་གསུམ་རྣམ་པར་བཀོད་ལ་དེ་ནས་སྤྲོ་བ་དང་བསྡུ་བ་སྔོན་དུ་འགྲོ་བར་རྡོ་རྗེ་བསྐྱེད་ལ། དེ་ཡོངས་སུ་གྱུར་པ་ལས་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པའི་ལྷའི་འཁོར་ལོ་གང་ཡང་རུང་བ་རྣམ་པར་བསྒོམས་ཏེ། ཡེ་ཤེས་སེམས་དཔའ་དང་ཏིང་ངེ་འཛིན་སེམས་དཔའ་དགོད་པའི་མཚན་ཉིད་ཀྱི་རྗེས་སུ་རྣལ་འབྱོར་བྱས་ལ་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་ལ་ཡིག་འབྲུ་དགོད་པའི་མཚན་ཉིད་ཀྱི་ཤིན་ཏུ་རྣལ་འབྱོར་རྫོགས་ནས༌[^2769]སྐུ་ལ་སོགས་པ་ལ་བྱིན་གྱིས་བརླབ་པའི་རྣལ་འབྱོར་ཆེན་པོ་བྱས་ཏེ། ཕྱག་རྒྱ་འདུས་ནས་རེག་བྱ་རྡོ་རྗེ་མའི་ཆོས་འབྱུང་གི་ནང་དུ་ཕྱུང་བའི་སྔགས་ཀྱིས་དཀྱིལ་འཁོར་པ་རྣམས་སྤྲུལ་ཏེ། དེ་ལས་ཀྱང་ཕྱི་རོལ་དུ་སྤྲོས༌[^2770]ལ་འགྲོ་བའི་དོན་བྱས་ནས་སླར་ཡང་གཤེགས་ཏེ། ཤར་ལ་སོགས་པའི་ཕྱོགས་དང་མཚམས་སུ་དཀྱིལ་འཁོར་པ་རྣམས་རིམ་གྱིས་བཞུགས་པར་བསམས་ལ། དབང་བསྐུར་བ་དང་རྒྱས་བཏབ་ཅིང་དེའི་འོག་ཏུ་འཆད་པར་འགྱུར་བའི་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཏིང་ངེ་འཛིན་གྱི་ཡན་ལག་ཕྲ་མོའི་རྣལ་འབྱོར་བསྒོམ་པར་བྱའོ། །

[Block 4589]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་ལྷ་རྣམས་ཀྱི་འཁོར་ལོ་ཞེས་སྨོས་ཏེ། ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི༌[^2771]འཁོར་ལོའི་ཕྱག་མཚན་ལས་བྱུང་བའི་རྣམ་པར་སྣང་མཛད་ཀྱི་སྤྲུལ་པའི་ལྷ་སུམ་ཅུ་རྩ་གཉིས་ཀྱི་བདག་ཉིད་ཀྱི་འཁོར་ལོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4590]
རིགས་དང་དེར་འབྲེལ་པའི་ལྷ་རྣམས་ཏེ་ཞེས་པ་ནི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་རིགས་ཀྱི་འབྲེལ་པ་དང་ལྡན་པའི་ལྷ་རྣམས་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །
--- END BLOCKS ---
