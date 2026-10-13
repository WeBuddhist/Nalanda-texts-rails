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
[Block 316]
གང་ཡང་དུས་གསུམ་དག་གི་ཞིང་གི་རྒྱན་ནི་ཞིང་མང་པོ་སྟེ། དེ་དག་མངོན་པར་བསྒྲུབ་ཅེས་བྱ་བ་ནི་རྫུ་འཕྲུལ་གྱི་སྟོབས་ཀྱིས་རྡུལ་གཅིག་གི་སྟེང་དུ་མངོན་པར་བསྒྲུབ༌[^166]པའོ། །

[Block 317]
དེ་ལྟར་མ་ལུས་ཕྱོགས་རྣམས་ཐམས་ཅད་དུ། །ཞེས་བྱ་བ་ནི་ཇི་ལྟར་མ་ལུས་པའི་ཕྱོགས་ཀྱི་རྡུལ་གྱི་སྟེང་དུ་སྒྲུབ་པ་དེ་བཞིན་དུ་ཡེ་ཤེས་ཀྱི༌[^167]སྐད་ཅིག་མ་གཅིག་གིས་ཞིང་མང་པོ་རྣམས་མངོན་པར་བསྒྲུབས༌[^168]ནས་འཇུག་པའོ། །

[Block 318]
ད་ལྟར་གྱི་སངས་རྒྱས་ཀྱི་ཞིང་ཐམས་ཅད་ཀྱི་ངོ་བོ་ཉིད་དང་། ཚད་དང་། ཁ་དོག་དང་། དབྱིབས་དག་སོ་སོར་ཐ་དད་པ་མང་པོ་མ་འདྲེས་པ་རྣམས་ཀྱང་རྡུལ་གཅིག་གི་སྟེང་དུ་བཞག་པར་མི་རུང་ན། སོ་སོར་ཐ་དད་པ་མང་པོ་རྣམས་རྡུལ་གཅིག་གི་སྟེང་དུ་ཕྱོགས་བཅུ་མཚམས་མེད་ཅིང་མ་འདྲེས་པར་ཇི་ལྟར་གཞག་པར་བྱ།[^169] དེ་ལྟ་བས་ན་འདི་ལ་ཇི་ལྟར་ཡིད་ཆེས་པར་བྱ་སྙམ་པ་ལ། དེའི་ལན་དུ་དེ་བས་ན༌[^170]ཆོས་ཐམས་ཅད་ནི་ཡོངས་སུ་མ་རྫོགས་པ་སྟེ། ངོ་བོ་ཉིད་མེད་པ་སྒྱུ་མ་ལྟ་བུ་མ་སྐྱེས་པ། མ་འགགས་པ། སྐྲ་ཤད་འཛིངས་པ་ལྟ་བུར་ཐོག་མ་ནས་ཞི་ཞིང་རང་བཞིན་གྱིས་སེམས་ལས་འདས་པ་ལ་ཇི་ལྟར་མོས་པར༌[^171]བརྟགས་པ་ཙམ་གྱིས་འབྱུང་བ་ནི་རྣམ་པ་སྣ་ཚོགས་དུ་མའི་གཟུགས་སུ་རབ་ཏུ་བསྒོམས་པས་རྣམ་པ་མང་པོའི་ཏིང་ངེ་འཛིན་དང་། རྣམ་པར་གྲོལ་བའི་ཁྱད་པར་གྱིས་བསམ་གྱིས་མི་ཁྱབ་པའི་རྣམ་པ་སྣ་ཚོགས་མྱོང་བས་ན་དངོས་པོ་འདི་དག་བར་དུ་གསལ་བར་སྣང་ངོ་། །འཇིག་རྟེན་ན་ཡང་སྔགས་ཅུང་ཟད་ཙམ་ལས་མཐུ་སྐྱེས་པའི་མིག་འཕྲུལ་གྱིས་རབ་ཏུ་བསྒྲུབས་ན་ངོ་མཚར་དང་ལྡན་པའི་སྒྱུ་མའི་མཛེས་པ༌[^172]ཡང་སྣང་ངོ་། །དེ་ལྟ་བས་ན་འདི་དག་ཐམས་ཅད་ནི་ཇི་ལྟར་སྨྲས་པ་བཞིན་ཡིད་ཆེས་པར་བྱ་སྟེ། [^173]འདི་ལྟར་ཡིད་གཉིས་ནི་ཅུང་ཟད་ཀྱང་མ་བྱེད་ཅིག །

[Block 319]
དེ་བཞིན་གཤེགས་པ་ལ་བསྙེན་བཀུར༌[^174]བྱ་བར་འཇུག་པ་དང་བརྒྱད་དེ། དེ་ཡང་གང་ཞེ་ན། གང་ཡང་མ་བྱོན་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། གང་མ་བྱོན་པ་ནི་ཕྱི་མ་མ་འོངས་པའི་མཐར་ཐུག་པ་རྣམས་སོ། །

[Block 320]
འཇིག་རྟེན་སྒྲོན་མ་ཞེས་བྱ་བ་ནི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས༌[^175]ཏེ། ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་གཞན་དང་གཞན་ན་ནམ་མཁའི་མཐའ་ཀླས་པ་ན༌[^176]བཞུགས་པ་བགྲང་བ་ལས་འདས་པའི་སངས་རྒྱས་ཀྱི་ཡེ་ཤེས་ཀྱི་སྤྱོད་ཡུལ་གྱིས་སྐད་ཅིག་གིས་དུས་མཉམ་པར་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་མངོན་པར༌[^177]རྫོགས་པར་སངས་རྒྱས་པ་སྟེ། དེ་ནས་འདི་བཞིན་དུ་དུས་མཉམ་པར་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་འགྱུར་བ་དང་། དེ་བཞིན་དུ་མྱ་ངན་ལས༌[^178]འདས་པ་སྟོན་པར་བཤད་དེ། དེ་དག་མངོན་སུམ་དུ་བྱང་ཆུབ་ཅེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 321]
དེ་དག་ཅེས་བྱ་བ་ནི་དེ་ལྟར་མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པར་མཛད་པ་དང་། དེ་དེ་བཞིན་དུ་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བར་མཛད་པ་དང་། མྱ་ངན་ལས་འདས་པ་རྣམ་པ༌[^179]རབ་ཏུ་སྟོན་པའི་མགོན་པོ་ཐམས་ཅད་ཀྱི༌[^180]ཞབས་ཀྱི༌[^181]དྲུང་དུ་ཡིད་མྱུར་བ་དང་། ཀུན་དུ་མྱུར་བ་ཞེས་བྱ་བའི་རྫུ་འཕྲུལ་གྱི་སྟོབས་གཉིས་ཀྱི༌[^182]མཐུས་ལུས་ཀྱི་སྤྲིན་གྱིས༌[^183]ཕྱོགས་བཅུ་བཀང་སྟེ། མཆོད་པའི་སྤྲིན་ནམ་མཁའ་ཁེབས་པའི་དམ་པ་བགྲང་བ་ལས་འདས་པ་ཐམས་ཅད་ཀྱིས་མཆོད་པ་དང་། བསྟོད་ཅིང་བརྗོད་པ་དང་། བསྐོར་བ་བརྒྱ་སྟོང་དུ་མ་བྱེད་ཅིང་འཁོར་བའི་མཐའི་བར་འགྲོ་བ་ནི་བསྙེན་པར་འཇུག་པའོ། །

[Block 322]
རིམ་པར་འཚང་རྒྱ་ཞེས་བྱ་བ་ནི་མངོན་པར་བྱང་ཆུབ་པའོ། །

[Block 323]
མྱ་ངན་ལས་འདས་པ་སྟོན་པ་ཞེས་བྱའམ།[^184] རབ་ཏུ་ཞི་མཐའ་ཞེས་བྱ་བ་ནི་ཚིག་ཁ༌[^185]བསྐང་བའི་ཕྱིར་རྣམ་གྲངས་སུ་རིག་པར་བྱ་སྟེ་གཙོ་བོར་བཤད་པའོ། །

[Block 324]
དེ་ཡང་ཆུ་ཟླའི་གཟུགས་བརྙན་བཞིན་དུ་དགའ་ལྡན་གནས་ཀྱི༌[^186]གཞལ་མེད་ཁང་ན་བཞུགས་པ་ལས་འཆི་འཕོ༌[^187]བསྟན་པ་དང་། མངལ་ན་གནས་པའི་ཚེ་དང་། ལྷས་ཕྱག༌[^188]བྱས་པ་དང་། བཟོ་བསྟན་པ་དང་། མངོན་པར་བྱུང་ནས་རབ་ཏུ་བྱུང་སྟེ་དཀའ་བ་སྤྱོད་པ་དང་། བྱང་ཆུབ་ཀྱི་སྙིང་པོར་བཞུད་ནས་བྱང་ཆུབ་ཀྱི་ཤིང་དྲུང་དུ་སེང་གེའི་གདན་ལ་བཞུགས་པས་བདུད་ཕམ་པར་མཛད་པའི་དུས་སུ་གོང་མ་བཞིན་ཉེ་བར་འགྲོ་བ་ནི་དེ་དག་གི་ཞབས་ཀྱི་དྲུང་དུ་ཡུད་ཙམ་གྱིས་སོ། །

[Block 325 [HEADING]]
#### སྟོབས། ^2-8-12-0

[Block 326]
སྟོབས་དེ་རྣམ་པ་བཅུ་གཉིས་པའོ། །

[Block 327]
དེ་དག་ཀྱང་རྣམ་པ་བཅུ་སྟེ་ཚིགས་བཅད་གཉིས་ཀྱིས་སོ། །དེ་ཡང་གང་ཞེ་ན། རྫུ་འཕྲུལ་སྟོབས་རྣམས་དང་ཞེས་བྱ་བ་ལ་སོགས་པ་སྟེ། འཕྲུལ་པར་བྱེད་པས་རྫུ་འཕྲུལ་ཞེས་བྱ་བས་ན་ཇི་ལྟར་འདོད་པ་ཕུན་སུམ་ཚོགས་པར་བྱེད་པ་སྟེ། ཆོ་འཕྲུལ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 328]
རྫུ་འཕྲུལ་ཇི་ལྟར་ཆོ་འཕྲུལ་དུ་ཤེས་པར་བྱ་ཞེ་ན། སོ་སོའི་སེམས་ཅན་རྣམས་ཀྱི་ཡིད་འཕྲོག་ཅིང་མགུ་བར་བྱེད་པས་ན་ཆོ་འཕྲུལ་ལོ། །

[Block 329]
དེའི་སྟོབས་ཀྱིས་གདོན་མི་ཟ་བས་ན་རྫུ་འཕྲུལ་གྱི་སྟོབས་སོ། །

[Block 330]
ཀུན་དུ་མྱུར་བའི་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་སེམས་དཔའི་གཞན་དུ་འགྲོ་བའོ།[^189] །

[Block 331]
འགྲོ་བ་ན༌[^190]ཀུན་དུ་མྱུར་བའི་རྫུ་འཕྲུལ་གྱིས་སྐད་ཅིག་གིས་ཕྱོགས་བཅུར་མི་ཐོགས༌[^191]པར་འགྲོ་བའོ། །

[Block 332]
ཐེག་པའི་སྟོབས་ཞེས་བྱ་བ་ནི་ཐེག་པ་ཆེན་པོའི་སྟོབས་ཀྱིས་ཏེ། དེ་བས་ན་ཐེག་པ་ཆེན་པོ་དེས་ཐེག་པས་ན་ཐེག་པ་ཆེན་པོའོ། །

[Block 333]
ཡང་ན་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོའི་ཐེག་པ་ཡིན་པས་ན། ཐེག་པ་ཆེན་པོ་སྟེ། དངོས་སུ་ན་སངས་རྒྱས་ཀྱི་བྱང་ཆུབ་ཐོབ་པར་བྱེད་པའི་ལམ་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་གཉིས་ལ་ཐེག་པ་ཞེས་བྱའོ། །

[Block 334]
ཡང་ན་ཕ་རོལ་ཏུ་ཕྱིན་པ་རྣམས་དང་བཅས་པ་ལ་ཐེག་པ་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 335]
དེ་དག་གི་སྟོབས་ནི་མི་མཐུན་པའི་ཕྱོགས་ཀྱི་སྟོབས་ཇི་སྙེད་པས་མི་ཆོམ༌[^192]པའོ། །

[Block 336]
ཀུན་ནས་སྒོའི་ཞེས་བྱ་བ་ནི་ཀུན་གྱི་སྒོ་སྟེ། ཇི་ལྟ་ཞེ་ན། དེའི་ལུས་དང་དམིགས་པ་ནི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་ཅིང་གཞན་ལ་ཕན་པར་མི་བྱེད་པ་གང་ཡང་མེད་པའོ། །

[Block 337]
དེ་ནི་འཕགས་པ་སྤྱོད་ཡུལ་ཡོངས་སུ་དག་པའི་མདོ་ལས༌[^193]ལྟོས་ཤིག །སྤྱོད་པའི་སྟོབས་རྣམས་ཞེས་བྱ་བ་ནི་སྤྱོད་པ་གཉིས་ཀ་བྱེ་བྲག་མེད་པའི་སྟོབས་ཏེ། བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པའི༌[^194]སྟོབས་དང་། ཀུན་དུ་བཟང་པོའི་སྤྱོད་པའི་སྟོབས་ཀྱིས་སོ།[^195] །

[Block 338]
ཀུན་དུ་ཡོན་ཏན་ཞེས་བྱ་བ་ནི་ཐོག་མ་དང་བར་མ་དང་ཐ་མར་དགེ་བའོ། །

[Block 339]
བྱམས་པ་དག་གི་སྟོབས་ཞེས་བྱ་བ་ནི་སེམས་ཅན་གྱི་ཁམས་ཐམས་ཅད་ལ་བདེ་བར་སེམས་པས་ཁྱབ་པའོ། །

[Block 340]
ཀུན་དུ་ཁྱབ་པ་ཞེས་བྱ་བ་ནི་ཕྱོགས་བཅུར་ཁྱབ་པའོ། །

[Block 341]
བསོད་ནམས་སྟོབས་ཞེས་བྱ་བ་ནི་དག་ཅིང་གཙང་བར་བྱེད་པས་ན་བསོད་ནམས་སོ། །

[Block 342]
ཡང་ན་ཕྱི་ཕྱིར་ཞེས༌[^196]བསོད་པར་འགྱུར་བས་ན་བསོད་ནམས་སོ། །

[Block 343]
དེའི་སྟོབས་ནི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པ་བསྒོམས་པ་ལས་བྱུང་བ་སྟེ། འདི་སྐད་དུ།

[Block 344 [VERSE]]
བྱང་ཆུབ་སེམས་ཀྱི་བསོད་ནམས་གང་། །
གལ་ཏེ་དེ་ནི་གཟུགས་གྱུར་ན། །
ནམ་མཁའི་ཁམས་ཀྱང་གང་གྱུར་ཅིང་། །
དེ་བས་དེ་ནི༌[^197]ལྷག་པར་འགྱུར། །

[Block 345]
ཞེས་གསུངས་སོ། །

[Block 346]
དེ་བས་ན་ཐེག་པ་ཆེན་པོ་དང་ལྡན་པའི་དམ་པའི༌[^198]ཆོས་ཟབ་ཅིང་རྒྱ་ཆེ་བ་རྣམས་འཛིན་པ་དང་། ཀློག་པ་དང་། འཆད་པ་དང་། མོས་ནས་ཚིགས་བཅད་གཉིས་ཙམ་ཡང་བཟུང༌[^199]ནས་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་བསྔོ༌[^200]བར་གྱུར་པར༌[^201]དེའི་བསོད་ནམས་ཀྱི༌[^202]སྟོབས་སོ། །

[Block 347]
ཀུན་ནས་དགེ་བའི་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་ལ་དགེ་བ་དང་ཕན་པ་སེམས་ཤིང་སྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 348]
ཡེ་ཤེས་སྟོབས་ཞེས་བྱ་བ་ནི་ཤེས་པར་བྱ་བ་ཐམས་ཅད་ལ་ཤེས་པར་བྱེད་པ་ནི་ཡེ་ཤེས་སོ། །

[Block 349]
ཆགས་པ་མེད་པར་གྱུར་པའི་ཞེས་བྱ་བ་ནི་དུས་གསུམ་དུ་མི་ཐོགས་པའོ། །ཤེས་རབ་ཀྱི་སྟོབས་ཞེས་བྱ་བ་ནི་དངོས་པོ་རྣམས་ཇི་ལྟ་བ་བཞིན་རྟོགས༌[^203]པའོ། །

[Block 350]
ཐབས་ཀྱི་སྟོབས་ཞེས་བྱ་བ་ནི་བསྒྲུབ་པར༌[^204]བྱ་བའི་རིགས་པ་ནི་ཐབས་ཏེ་སྒྲུབ་པའི་སྟོབས་ལ་ཐོགས་པ་མེད་པའོ། །

[Block 351]
ཏིང་འཛིན༌[^205]སྟོབས་ཞེས་བྱ་བ་ནི་སྟོབས་དང་བྱེད་པའི་ཏིང་ངེ་འཛིན་ཏེ༌[^206]བསམ་གཏན་ནོ། །

[Block 352]
དེའི་མཐུས་འགྲོ་བ་ཐམས་ཅད་ཀྱི༌[^207]དོན་བྱ་བའི་ཕྱིར་མངོན་པར་ཤེས་པ་ལ་སོགས་པའི་ཡོན་ཏན་སྡུད་པ་ལ་མི་ཐོགས་པ་དེ་ནི་ཏིང་ངེ་འཛིན་གྱི་སྟོབས་སོ། །

[Block 353]
བྱང་ཆུབ་སྟོབས་རྣམས་ཞེས་བྱ་བ་ནི་བྱང་ཆུབ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་པ་སྟེ། དེ་ཐོབ་པར་བྱེད་པ་ནི་སྟོབས་སོ། །

[Block 354]
ཡང་དག་སྒྲུབ་པར༌[^208]བྱེད་ཅེས་བྱ་བ་ནི་དེའི་ཚོགས་སྒྲུབ་པའོ། །

[Block 355 [HEADING]]
#### གཉེན་པོ། ^2-8-13-0
--- END BLOCKS ---
