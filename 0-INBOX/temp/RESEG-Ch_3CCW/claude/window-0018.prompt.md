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
[Block 631]
རང་གི་ཕྱོགས་ཁས་ལེན་པ་ཡོད་ན་ནི་དེའི་ཚེ་དེ་གཟུགས་པའི་ཕྱིར་གཞན་རྣམས་དང་རྩོད་པར་གྱུར་ན་དེ་དག་ལ་ནི་དེ་ལྟ་བུ་ཡང་མེད་པས་དེ་བས་ན་རྩོད་མེད་ཆེ་བའི་བདག་ཉིད་ཅན་ནོ། །

[Block 632]
གལ་ཏེ་དེ་དག་ལ་རང་གི་ཕྱོགས་མེད་དུ་ཟིན་ཀྱང་གཞན་གྱི་ཕྱོགས་གཞིག་པ་མེད་མི་སྲིད་དེ།

[Block 633]
དེ་བས་ན་གཞན་གྱི་ཕྱོགས་ཡོད་དང་། །བདག་གི་ཕྱོགས་ཀྱང་མེད་དུ་མི་རུང་ངོ་། །

[Block 634]
ཕྱོགས་ཤིག་ཡོད་ན་ནི་བདག་གི༌[^372]ཕྱོགས་སམ་གཞན་གྱི་ཕྱོགས་མེད་པར༌[^373]ཡང་འགྱུར་ན། གང་གི་ཚེ་ཕྱོགས་ཡེ་མེད༌[^374]དེའི་ཚེ།

[Block 635 [VERSE]]
གང་རྣམས་ལ་ནི་ཕྱོགས་མེད་པ། །
དེ་ལ་གཞན་ཕྱོགས་ག་ལ་ཡོད། །

[Block 636]
གང་གི་ཚེ་དེ་ལྟར་དངོས་པོ་མེད་པས་བདག་དང་གཞན་གྱི་ཕྱོགས་མེད་པ་དེའི་ཚེ་དེ་ལྟར་མཐོང་བ་རྣམས་ཀྱི་ཉོན་མོངས་པ་རྣམས་ངེས་པར་འགག་པར་འགྱུར་རོ། །ཇི་ལྟ་ཞེ་ན། དེ་དག་འདི་ལྟར།

[Block 637 [HEADING]]
### ཚིགས་བཅད་ང་གཅིག་པ། ^1-52-0

[Block 638 [VERSE]]
གང་ཡང་རུང་བའི་གནས་རྙེད་ནས། །
ཉོན་མོངས་སྦྲུལ་གདུག༌[^375]གཡོན་ཅན་གྱིས། །
ཟིན་པར་འགྱུར་རོ་གང་གི་སེམས། །
གནས་མེད་དེ་དག་ཟིན་མི་འགྱུར། །

[Block 639]
འདོད་ཆགས་ལ་སོགས་པ་ནི་རང་བཞིན་གྱིས་འདུ་བྱེད་ཀྱི་ནགས་ཐིབས་པོ་ན་རྒྱུ་བ་དགེ་བའི་ཕྱོགས་ཀྱི་སྲོག་གི་བར་ཆད་བྱེད་པ་ལྟ་བ་ལ་སོགས་པའི་མིག་གི་དབང་པོའི་ཕུག་ཏུ་གནས་བཅས་པ་ཡུལ་གྱི་རླུང་ལ་ཡིད་ཆགས་པ་ཡུན་རིང་པོ་ནས་རྗེས་སུ་འབྲང་བའོ། །

[Block 640]
གཡོན་ཅན་ནི་གྱ་གྱུ་ལྟར་འགྲོ་བ་སྟེ། །འཛིན་པ་ལ་བརྩོན་པས་དེ་དག་ནི་སྦྲུལ་ལོ། །

[Block 641]
གནས་བརྟེན་པར་བྱ་བ་རྒྱུ་འགའ་ཞིག་རྙེད་ནས་འགའ་ཞིག་ལ་འཛིན་ཏོ། །

[Block 642]
གང་དག་དངོས་པོ་ཐམས་ཅད་དུ་མི་དམིགས་པས་ཉོན་མོངས་པའི་སྦྲུལ་གྱིས༌[^376]གནས་པའི་རྒྱུ་མ་ལུས་པར་བསྲེགས་ཤིང་དྲན་པ་དང་ཤེས་བཞིན་གྱི༌[^377]དབང་པོའི་ཕུག་རྣམས་བཀག་པ་དེ་དག་ཉོན་མོངས་པའི་སྦྲུལ་གྱིས་ཟིན་པར་འགྱུར་བའི་གནས་མེད་པར་བྱས་པས་གང་དག་གི་སེམས་ལ་གནས་པ་མེད་པ་ནི་ཟིན་པར་འགྱུར་ཏེ། དངོས་པོར་དམིགས་པ་མེད་ན་སེམས་ཀྱི༌[^378]ཕྱོགས་ཡོངས་སུ་མི་འཛིན་པའི་ཕྱིར་རོ། །

[Block 643]
དེའི་ཕྱིར་དེ་ལྟར་གང་དག་གིས་སེམས་ལ་དམིགས་པ་མེད་པ་དེ་དག་ཉོན་མོངས་པའི་སྦྲུལ་གདུག་པ་གཡོན་ཅན་གྱིས་ཀྱང་མི་ཚུགས་ཤིང་ཟིན་པར་མི་འགྱུར་རོ། །

[Block 644]
གང་དག་གཟུགས་ལ་སོགས་པའི་རང་བཞིན་དམིགས་ཀྱང་ཉོན་མོངས་པ་རྣམས་སྤང་དུ་རུང་བར་འདོད་པ་དེ་དག་ལ་ནི་ཉོན་མོངས་པ་རྣམས་སྤང་བར༌[^379]འགྱུར་བ་མེད་དོ་ཞེས་བསྟན་པའི་ཕྱིར།

[Block 645 [HEADING]]
### ཚིགས་བཅད་ང་གཉིས་པ། ^1-53-0

[Block 646 [VERSE]]
གནས་དང་བཅས་པའི་སེམས་ཡོད་ལ། །
ཉོན་མོངས་དུག་ཆེན་ཅིས་མི་འབྱུང་། །

[Block 647]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 648]
དངོས་པོར་དམིགས་ན་ནི་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པ་རྣམས་ཀྱི་འབྱུང་བ་གདོན་མི་ཟ་བར་མི་ཟློག་སྟེ༌[^380]འབྱུང་ངོ་། །

[Block 649]
ཇི་ལྟ་ཞེ་ན། གལ་ཏེ་དངོས་པོ་དེ་ཡིད་དང་མཐུན་པར་གནས་ན་ནི་དེའི་ཚེ་དེ་ལ་རྗེས་སུ་ཆགས་པ་བཟློག་པར༌[^381]དཀའ་བར་འགྱུར་རོ། །

[Block 650]
ཅི་སྟེ་མི་མཐུན་ན་ཡང་དེའི་ཚེ་དེ་ལ་ཁོང་ཁྲོ་བ་དང་། ཚིག་པ་ཟ་བ་བཟློག་དཀའ་བར་འགྱུར་རོ། །

[Block 651]
འོན་ཏེ་རྟོག་པ་དེ་གཉིས་ཀ་བསྩལ༌[^382]ཀྱང་དེའི་ཚེ༌[^383]རང་གི་ངོ་བོ་ལ་སྒྲོ་འདོགས་ཤིང་དམིགས་པ་ལས་བྱུང་བ་བཏང་སྙོམས་སུ་འགྱུར་བའི་ཡུལ་ལ་མ་རིག་པའི་བག་ལ་ཉལ་བ་བཟློག་དཀའ་བར་འགྱུར་རོ། །

[Block 652]
ཐ་མལ་པར་འདུག་པའི་གནས་ན༌[^384]ཀུན་ཏུ་འབྱུང་བའི་མ་རིག་པའི་བག་ལ་ཉལ་འཁོར་བའི་སྡུག་བསྔལ་འབྱུང་བ་དང་མཐུན་པ་གནོད་པའི་བདག་ཉིད་ཉོན་མོངས་པའི་སྦྲུལ་འབྱུང་བར་དམིགས་ནས།

[Block 653 [VERSE]]
གང་ཚེ་ཐ་མལ་འདུག་པ་ཡང་། །
ཉོན་མོངས་སྦྲུལ་གྱིས་ཟིན་པར་འགྱུར། །

[Block 654]
ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 655]
གང་གི་ཚེ་གཏི་མུག་དེ་རྟག་ཏུ་འབྱུང་བར་གྱུར་པ་དེ་ནི་ཀུན་ཏུ་རྨོངས་པ༌[^385]དེ་ཁོ་ན་མཐོང་བ་བསྒྲིབས་པའི་སོ་སོའི་སྐྱེ་བོ་དག་གཏི་མུག་གི་མཐུས་གྲུབ་པའི་དངོས་པོའི་རང་གི་མཚན་ཉིད་ལ་གདོན་མི་ཟ་བར།

[Block 656 [HEADING]]
### ཚིགས་བཅད་ང་གསུམ་པ། ^1-54-0

[Block 657 [VERSE]]
བྱིས་པ་བདེན་པར་འདུ་ཤེས་པས། །
གཟུགས་བརྙན་ལ་ནི་ཆགས་པ་བཞིན། །
དེ་ལྟར་འཇིག་རྟེན་རྨོངས་པའི་ཕྱིར། །
ཡུལ་གྱི་གཟེབ་ལ་ཐོགས་པར་འགྱུར། །

[Block 658]
ཇི་ལྟར་བྱིས་པ་འཇིག་རྟེན་གྱི་ཐ་སྙད་མི་ཤེས་པ་རང་བཞིན་གྱིས་རྣམ་པར་ཤེས་པ་བླུན་པ་དག་གཟུགས་བརྙན་དམིགས་པ་ན་དེ་ལ་དངོས་པོ་ཡོད་པར་འཛིན་ཞིང་ཆགས་པར་འགྱུར་ཏེ་ཅི༌[^386]ཡང་བྱེད་ཅིང་དེ་དང་རྩེ་བ་དེ་བཞིན་དུ་བྱིས་པ་མ་རིག་པ་དང་ལྡན་པ་གཏི་མུག་གི་མཐུས་སྐྱེས་པ་ལ། དངོས་པོ་ཡོད་པ་ཡང་དག་པར་རྩོད་པ་ལ་མངོན་པར་ཞེན་པ་ལུས་དང་ངག༌[^387]ཡིད་ཀྱིས༌[^388]འཇུག་པས། དེ་དང་དེ་ལ་མངོན་པར་ཞེན་པས། རྗེས་སུ་ཆགས་པ་དང་། ཁོང་ཁྲོ་བ་དང་། ང་རྒྱལ་ལ་སོགས་པས་རང་དབང་མེད་པར་འཇུག་པ་བྱིས་པ་བཞིན་དུ་ཅི་དང་ཅི་ཡང་བྱེད་ཅིང་འཁོར་བའི་གཟེབ་ལ་ཐོགས་པ་འཁོར་བའི་ངོ་བོ་ཉིད་མི་ཤེས་པ་དག་མི༌[^389]འཕགས་པ་རྣམས་ལ་སྙིང་བརྩེ་བའི་ཡུལ་དུ་སྣང་ངོ་། །ཤེས་རབ་ཀྱི་དྲག༌[^390]པའི་སྤྱན་དང་ལྡན་པ་འཕགས་པ་དག་ནི་ངོ་བོ་ཉིད་ཡང་དག་པ་ཇི་ལྟ་བ་བཞིན་དུ་གཟིགས་པས།

[Block 659 [HEADING]]
### ཚིགས་བཅད་ང་བཞི་པ། ^1-55-0

[Block 660 [VERSE]]
དངོས་པོ་གཟུགས་བརྙན་ལྟ་བུར་ནི། །
ཡེ་ཤེས་མིག་གིས་རབ་མཐོང་ན། །
བདག་ཉིད་ཆེན་པོ་དེ་དག་ནི། །
ཡུལ་གྱི་འདམ་ལ་མི་ཆགས་སོ། །

[Block 661]
ཆགས་པ་མེད་ན་དངོས་པོ་རྣམས་ལ་དེའི་བདག་ཉིད་དུ་ཆགས་ཤིང་འཇུག་པ་མེད་པས་ཡུལ་གྱི་འདམ་ལ་ཆགས་པར་མི་འགྱུར་ཏེ། འཕགས་པ་རྣམས་ནི་གཟུགས་བརྙན་ལ་བློ་བྱང་བ་དང་འདྲ་ཞིང༌[^391]ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 662]
དེའི་ཕྱིར་དེ་ལྟར་ཤིན་ཏུ་བྱིས་པའི་བློ་ཅན་དག་ནི་གཟུགས་བརྙན་ལ་བྱིས་པ་བཞིན་དུ་གདོན་མི་ཟ་བར།

[Block 663 [HEADING]]
### ཚིགས་བཅད་ང་ལྔ་པ། ^1-56-0

[Block 664 [VERSE]]
བྱིས་པ་རྣམས་ནི་གཟུགས་ལ་ཆགས། །
བར་མ་དག་ནི་འདོད་ཆགས་བྲལ། །

[Block 665]
གཟུགས་ཀྱི་རང་བཞིན་ཤེས་པ་ཡི།[^392] །བློ་མཆོག་དག་ནི་རྣམ་པར་གྲོལ། །དེ་ལ་བྱིས་པའི་མཚན་ཉིད་དང་ལྡན་པ་ནི་བྱིས་པ་སྟེ། དེ་ཡང་ཉེས་པར༌[^393]སེམས་པ་སེམས་པ་དང་། ཉེས་པར་སྨྲ་བ་སྨྲ་བ་དང་། ཉེས་པར་བྱེད༌[^394]པའི་ལས་བྱེད་པའོ། །

[Block 666]
དེ་ལ་ཉེས་པར་སེམས་པ་སེམས་པ་ནི་གང་དག་ལུས་མི་གཙང་བ་དང་སྐད་ཅིག་ཅིང་འཇིག་པའི་ངང་ཅན་ལ་གཙང་བ་དང་། མི་འཇིག་པའི་ངང་ཅན་དུ་སེམས་པའོ། །

[Block 667]
ཉེས་པར་སྨྲ་བ་སྨྲ་བ་ཞེས་བྱ་བ་ནི་བསྔགས་པར་མི་འོས་པ་རྟག་ཏུ་ཕན་གདགས་དགོས་པ་སྡུག་བསྔལ་གྱི་བདག་ཉིད་ཅན་གྱི་ལུས་ལ་མིང་དང་ཚིག་དང་ཡི་གེའི་ཚོགས་སྣ་ཚོགས་ཀྱིས་བསྔགས་པ་བརྗོད་པའོ། །

[Block 668]
ཉེས་པར་བྱེད་པའི་ལས་བྱེད་པ་ཞེས་བྱ་བ་ནི་མི་དགེ་བའི་རྣམ་པར་སྨིན་པ་སྡུག་བསྔལ་དུ་འགྱུར་བའི་ལས་རྩོམ་པའོ། །

[Block 669]
དེ་ལྟར་བྱིས་པ་དེ་དག༌[^395]མི་གཙང་བཞིན་དུ་གཟུགས་ལ་ཆགས་སོ། །

[Block 670]
བར་མ་ནི་གང་དག་མི་གཙང་བ་ལ་ཇི་ལྟར་གནས་པ་བཞིན་དུ་སྨོད་ཅིང་གཟུགས་ལ་སྡུག་བསྔལ་བརྒྱ་ཕྲག་དུ་མ་བསྩགས་པར་མཐོང་སྟེ། གཟུགས་ལ་འདོད་ཆགས་དང་བྲལ་བར་གྱུར་ནས་བསམ་གཏན་དང་གཟུགས་མེད་པའི་སྙོམས་པར་འཇུག་པ་འཐོབ་སྟེ། འདོད་པའི་ཁམས་ལས་ཤིན་ཏུ་འདས་པ་དེ་དག་ནི་བར་མའོ། །
--- END BLOCKS ---
