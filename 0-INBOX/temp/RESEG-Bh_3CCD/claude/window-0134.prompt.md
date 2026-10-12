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
[Block 4691 [VERSE]]
སྲིད་པའི་སྐྱོན་གྱིས་མ་གོས་པས། །
ཡེ་ཤེས་དེ༌[^2811]ནི་པདྨར་བཤད། །
རལ་གྲི་ཉོན་མོངས་དགྲ་གཅོད་པ། །
ཨུཏྤལ་དེ་ལས་སྐྱོབ་པའི་ཕྱིར། །

[Block 4692 [VERSE]]
འཁོར་བའི༌[^2812]དྲ་བ་ངེས་ཚིག་པའི། །
གང་ཕྱིར་ཡེ་ཤེས་ཉིད་སྐྱེས་པ། །
སངས་རྒྱས་རྗེས་གནང༌[^2813]སེམས་ཅན་གྱིས། །
རྡེག་པར་བྱེད་པ་ཐོབ་པར་བཤད། །

[Block 4693 [VERSE]]
ཆད་པས་གདུལ་ཕྱིར་དབྱུག་པ་སྟེ། །
སེམས་ཅན་འདུལ་བྱེད་དེ་ཤེས་ཡིན། །
ཕན་ཚུན་ཁྱབ་པ་མི་བྱེད་ཕྱིར། །
སྣ་ཚོགས་རྡོ་རྗེ་ཡིན་པར་བཤད། །

[Block 4694]
སྐུ་མདོག་དང་ཕྱག་མཚན་དང་ཡེ་ཤེས་ཀྱི་རང་བཞིན་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི། །འོན་ཀྱང་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་ཡང་དེའི་ངོ་བོ་ཉིད་དོ། །

[Block 4695 [VERSE]]
སེམས་ཅན་ཀུན་ལ་སྣང་བྱེད་ཕྱིར། །
རང་གི་རང་བཞིན་སྣང་བྱེད་པས། །
དེ་བཞིན་གཤེགས་ཞེས་དག་པ་ནི། །
དེ་ནི་རྣམ་པར་སྣང་མཛད་བཤད། །

[Block 4696 [VERSE]]
མ་རུངས་ཐམས་ཅད་སྐྱེ་བོ་དང་། །
བླ་མ་ལ་ནི་ལོག་པ་རྣམས། །
མི་སྟོན་པ་ཡི་རང་བཞིན་ཕྱིར། །
དེ་ནི་མི་བསྐྱོད་རབ་ཏུ་བཤད། །

[Block 4697 [VERSE]]
གང་ཕྱིར་སངས་རྒྱས་ལ་སོགས་པ། །
རིན་པོ་ཆེ་རྣམས་རབ་བྱུང་བས། །
སེམས་ཅན་དོན་ལྡན་ཡེ་ཤེས་ནི། །
རིན་ཆེན་འབྱུང་ལྡན་བཤད་པ་ཡིན། །

[Block 4698 [VERSE]]
མི་གནས་མྱ་ངན་ལས་འདས་པའི། །
སྲིད་དང་ཐར་པ་མི་དམིགས་པ། །
མཐའ་ཡས་ཡོན་ཏན་དང་ལྡན་པས། །
དེ་ནི་སྣང་བ་མཐའ་ཡས་བཤད། །

[Block 4699 [VERSE]]
སེམས་ཅན་ཀུན་གྱི་དོན་མཛད་པའི། །
གང་ཕྱིར་རང་ཉིད་གྲུབ་པས་ན། །
དོན་དང་བཅས་པའི་ཡེ་ཤེས་ཏེ། །
དོན་ཡོད་གྲུབ་པར་བཤད་པ་ཡིན། །

[Block 4700 [VERSE]]
ཁམས་གསུམ་པས་ནི་ཡོངས་བསྒོམས༌[^2814]པས། །
ཕྲ་བ་དང་ནི་རགས་པའི་གཟུགས། །
ཞིང་ཀུན༌[^2815]ལ་གནས་གཟིགས་པའི་ཕྱིར། །
དེས་ན་སངས་རྒྱས་སྤྱན་མར་བཤད། །

[Block 4701 [VERSE]]
གང་ཕྱིར་བདག་དང་བདག་གིར༌[^2816]ནི། །
དེ་བཞིན་གཤེགས་ཀུན་ཡེ་ཤེས་ཏེ། །
ཕན་ཚུན་ཁྱབ་པར་བྱེད་པ༌[^2817]ན། །
དེས་ནི་མཱ་མ་ཀཱི་རུ་བཤད། །

[Block 4702 [VERSE]]
སྐྱོན་ཀུན་འཕྲོགས་པའི་ཡེ་ཤེས་ནི། །
དེ་བཞིན་གཤེགས་པ་ཀུན་གྱི་མཆོག །
སེམས་ཅན་སྦྱང་བ་ལ་བརྩོན་པའི། །
གོས་དཀར་མོར༌[^2818]ནི་བཤད་པ་ཡིན། །

[Block 4703 [VERSE]]
རྟག་ཏུ་ཐུགས་རྗེ་ཆེན་པོ་ཡིས། །
འགྲོ་བ་འདོན་པའི་བསམ་པ་ཅན། །
སེམས་ཅན་སྒྲོལ་བ་ལ་བརྩོན་པ། །
སྒྲོལ་མ་ཤེས་རབ་ཏུ་ནི་གྲགས། །

[Block 4704 [VERSE]]
ས་ལ་སོགས་པའི་ཁམས་གྱུར་པ། །
སངས་རྒྱས་ཡེ་ཤེས་ཀྱིས་བརྗོད་པས། །
འདོད་པ་ཐམས་ཅད་ལོངས་སྤྱོད་ཕྱིར། །
སྤྱན་མ་ལ་སོགས་རབ་ཏུ་གྲགས། །

[Block 4705 [VERSE]]
འཆི་སོགས་འཇིགས་པ་ལས་གྲོལ་བའི། །
དེ་བཞིན་གཤེགས་པ་ཀུན་གྱི་མཆོག །
གདུལ་དཀའ་འདུལ་བའི་ཡེ་ཤེས་ནི། །
དེ་ཕྱིར་སྙིང་རྗེ་མཐར་བྱེད་བཤད། །

[Block 4706 [VERSE]]
དག་པས་སྤྱད་ན༌[^2819]འགྲོ་བ་ནི། །
ཐམས་ཅད་དགའ་བའི་རང་བཞིན་འགྱུར། །
སྲིད་པས་མི༌[^2820]གོས་རྟོགས་པའི་ཕྱིར། །
དེ་ནི་པདྨ་མཐར་བྱེད་བཤད། །

[Block 4707 [VERSE]]
ཡེ་ཤེས་དོན་ཀུན་སྒྲུབ་བྱེད་པ། །
སངས་རྒྱས་ཀུན་གྱི་རང་བཞིན་གྲུབ། །
བགེགས་ལ་སོགས་པས༌[^2821]མི་གནོད་པ། །
དེ་ཕྱིར་བགེགས་ནི་མཐར་བྱེད་བཤད། །

[Block 4708 [VERSE]]
རྨོངས་པའི་སེམས་ཅན་གྱིས་སྨྲས་པ། །
ལོག་པའི་ཤེས་པ་རྣམ་སྤྱད་ནས། །
ཡང་དག་ཡེ་ཤེས་ལ་འཇོག་པས། །
ཤེས་རབ་མཐར་བྱེད་བཤད་པ་ཡིན། །

[Block 4709 [VERSE]]
ཤེས་བྱ་མེད་པས་ཤེས་པ་མིན། །
སྙོམས་པར་ཞུགས་པ་བཤད་པ་ཡིན། །
ཆགས་པ་ལ་སོགས་གསུམ་སྦྱངས་པས། །
སྲིད་གསུམ་མངོན་འགྱུར༌[^2822]ཡེ་ཤེས་ནི། །

[Block 4710 [VERSE]]
སངས་རྒྱས་ཀུན་གྱི་རང་བཞིན་འགྲུབ། །
དེས་ནི་ཞལ་གསུམ་བཤད་པ་ཡིན། །

[Block 4711]
ཞེས་བྱ་བ་ལ་སོགས་པ་འབྱུང་ངོ་། །

[Block 4712]
དེས་ནི་དེ་བཞིན་གཤེགས་པ་ལྔ་ནི་ཡེ་ཤེས་ལྔའི་རང་བཞིན་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4713]
དེ་རྣམས་ཀྱི་ངེས་ཚིག་ནི། དེ་ལས་ཀྱང་ཇི་སྐད་དུ།

[Block 4714 [VERSE]]
ཇི་ལྟར་གཟུགས་བརྙན་མེ་ལོང་ལ། །
རང་གི་གཟུགས་ནི་གཉིས་སྣང་བ། །
ཆོས་སྐུར་དེ་བཞིན་ཡེ་ཤེས་ནི། །
མེ་ལོང་ཤེས་བྱ་སྣང་བ་ཡིན། །

[Block 4715 [VERSE]]
དེ་བཞིན་གཤེགས་ཀུན་ཡེ་ཤེས་ནི། །
སྲོག་ཆགས་རྣམས་ཀྱི་རང་ལྷ་ཉིད། །
རང་ཉིད་གཅིག་ཏུ་རྟོགས་པའི་ཕྱིར། །
མཉམ་ཉིད་ཡེ་ཤེས་བཤད་པ་ཡིན། །

[Block 4716 [VERSE]]
གཟོད་མ་ནས་དག་མ་སྐྱེས་པའི། །
རང་བཞིན་ཉིད་ཀྱིས༌[^2823]འོད་གསལ་བ། །
ཕན་ཚུན་ཁྱབ་པར་བྱེད་པས་ན། །
སོ་སོར་རྟོག་པའི༌[^2824]ཡེ་ཤེས་བཤད། །

[Block 4717 [VERSE]]
ཀུན་དུ་རྟག་ཏུ་ཀུན་ནས་ནི། །
སངས་རྒྱས་མཛད་པ་རབ་འཇུག་པ། །
སངས་རྒྱས་ཀུན་མཛད་གཅིག་ཡིན་ཕྱིར། །
བྱ་བ་ནན་ཏན་གྲུབ་པར་བཤད། །

[Block 4718 [VERSE]]
ཉོན་མོངས་ཤེས་བྱའི་སྒྲིབ་པ་ཀུན། །
གང་ཚེ་གྲོལ་ན་དེ་ཚེ་ཡི། །
རྣལ་འབྱོར་པ་མཆོག་རྡོ་རྗེ་ཅན། །
ཤིན་ཏུ་རྣམ་པར་དག་ཅེས་བཤད། །

[Block 4719]
ཅེས༌[^2825]འབྱུང་ངོ་། །དེ་རྣམས་བསྐྱེད་པའི་ཞེས་བྱ་བ་ལ་སོགས་པ་ཞེས་པ་ནི། དང་པོའི༌[^2826]སྦྱོར་བའི་ཕྱོགས་གཅིག་ཏུ་གྱུར་པའི་དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི་འོག་ཏུ་པདྨ་ལ་སོགས་པ་བསྡུ་བར་བྱེད་པའི་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི༌[^2827]རྣམ་པའི་སེམས་བརྟན་པར་བྱ་བའི་ཕྱིར་ཆོས་ཀྱི་དབྱིངས་ཀྱི་སྔགས་བརྗོད་པའི་མཚན་ཉིད༌[^2828]ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4720]
གང་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ངོ་བོ་ཉིད་དུ་གྱུར་པ་ཞེས་བྱ་བ་ནི་སྟོང་པ་ཉིད་ཀྱི་ཡེ་ཤེས་ཀྱི་རང་བཞིན་ནོ། །

[Block 4721]
སྐྱེད་པར་མཛད་པ་སྟེ་ཞེས་པ་ནི་དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི༌[^2829]རིམ་པས་འོད་གསལ་བར་བྱས་ལ་ཡང་དེའི་ངོ་བོ་ཉིད་དུ་སྐུ་གསུང་ཐུགས་བསྐྱེད་པར་བྱའོ། །

[Block 4722]
བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་ངོ་བོ་ནི་རྡོ་རྗེ་འཆང་གི་སྐུ་གསུང་ཐུགས་ཞེས་བྱ་བའོ། །

[Block 4723]
ཨོཾ་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། ཨོཾ་ནི་སྐུ་གསུང་ཐུགས་ཉེ་བར་སྡུད་པར་བྱེད་པའི་ངོ་བོ་དོན་དམ་པའི་བདེན་པའི་རྣམ་པ་ཅན་རྡོ་རྗེ་འཆང་ཆེན་པོའོ། །

[Block 4724]
དྷརྨ་དྷཱ་ཏུ་ནི་ཆོས་ཐམས་ཅད་གཉིས་སུ་མེད་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4725]
སྭ་བྷཱ་བ་ནི་རང་བཞིན་གང་ལ་ཡོད་པ་དེ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་རང་བཞིན་ཁམས་གསུམ་གྱི་བདག་ཉིད་གཡོ་བ་དང་བརྟན་པའི་འགྲོ་བ་སྟེ། །དེའི་རྣམ་པ་བདག་ཡིན་ནོ་ཞེས་རྣལ་འབྱོར་པས་ང་རྒྱལ་བསྐྱེད་པར་བྱའོ། །

[Block 4726]
འདིས་ནི་བདག་ཉིད་ཟླ་བའི་དཀྱིལ་འཁོར་དང་འདྲ་བར་བྱིན་གྱིས་བརླབས་ལ་ཞེས་པ་ནི་ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི་པདྨ་ལ་སོགས་པ་གསུམ་གྱི་སྟེང་དུ་ཡི་གེ་གསུམ་ཡོངས་སུ་གྱུར་པ་ལས་སྐྱེས་པའི་ཟླ་བ་ལ་སྔར་བསྒོམས་པའི༌[^2830]པདྨ་ལ་སོགས་པ་གསུམ་དང་རོ་གཅིག་པར་གྱུར་པའི་ཟླ་བའི་དཀྱིལ་འཁོར་དང་འདྲ་བའི་སེམས་ཉིད་བྱིན་གྱིས་བརླབས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4727 [VERSE]]
ཡིད་མི་བདེ་བ་ལས་གྲོལ་བའི། །
རྣམ་རྟོག་མུན་པ་སེལ་བྱེད་ཅིང་། །
ཉོན་མོངས་དྲི་མ་ཀུན་ལས་དག །
ཟླ་བ་བཞིན་དུ་སེམས་ཟླ་བའོ། །

[Block 4728]
ཞེས་འབྱུང་ངོ་། །རྩ་བའི་རྒྱུད་ལས་ཀྱང་། བཅོམ་ལྡན་འདས་ཟླ་བའི་དཀྱིལ་འཁོར་དང་འདྲ་བའི་སེམས་མཐོང་ངོ་ཞེས་འབྱུང་ངོ་། །དེའི་སྟེང་དུ༌[^2831]ཡི་གེ་གསུམ་ལ་སོགས་པའི༌[^2832]ལྷའི་སྐུར་བསྐྱེད་དེ་ཞེས་པ་ལ་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་ཡང་ཡི་གེ་གསུམ་བཀོད་པ་དེ་ཡོངས་སུ་གྱུར་པ་ལས་རྡོ་རྗེ་རྩེ་ལྔ་པ་འམ་འཁོར་ལོ་ལ་སོགས་པ་བསྒོམས་ལ། །དེ་ལ་ཡང་ཡིག་འབྲུ་དགོད་ཅིང་སྤྲོ་བ་དང་བསྡུ་བའི་རིམ་པའི་གྲོ༌[^2833]བའི་དོན་བྱས་ལ་བཛྲ་ཨཱཏྨ་ཀོ྅ཧཾ་ཞེས་བྱ་བས་ང་རྒྱལ་བྱས་ལ། དེ་ཡོངས་སུ་གྱུར་པ་ལས་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་དང་གཅིག་ཏུ་གྱུར་པའི་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པའི་དེ་བཞིན་གཤེགས་པའི་ཕྱག་རྒྱའི་སྐུ་བསྒོམས་ལ། ཡེ་ཤེས་སེམས་དཔའ་དང་ཏིང་ངེ་འཛིན་སེམས་དཔའ་དགོད་ཅིང་ཕུང་པོ་དང༌[^2834]ཁམས་དང་སྐྱེ་མཆེད་རྣམ་པར་དག་པར་བྱ་སྟེ། སྐུ་ལ་སོགས་པ་བྱིན་གྱིས་བརླབ་པའི༌[^2835]མཚན་ཉིད་ཀྱི༌[^2836]རྣལ་འབྱོར་ཆེན་པོ་ཡོངས་སུ་རྫོགས་ཤིང་དབུས་ཀྱི་གཙོ་བོར་གྱུར་ནས།

[Block 4729]
དང་པོ་སྦྱོར་བའི་འོག་ཏུ་ཕྱག་རྒྱ་ལེགས་པར་སྦྱང་ཞིང་དཀྱིལ་འཁོར་པ་རྣམས་སྤྲུལ་ལ་དཀྱིལ་འཁོར་ལ་དགོད་དེ། དབང་བསྐུར་བ་དང་རྒྱས་གདབ་པའི་བར་དུ་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་ཡོངས་སུ་རྫོགས་ཏེ་ལས་ཀྱི་རྒྱལ་བ་མཆོག་གི་ཕྱོགས་གཅིག་པ་འཆད་པར་འགྱུར་བའི་རིམ་པས། ཕྲ་མོའི་རྣལ་འབྱོར་ཞེས་པ་ནི་འོག་ནས་འཆད་པར་འགྱུར་བའི་རིམ་པས་བསྒོམ་པར་བྱའོ། །

[Block 4730]
དྲང་བའི་དོན་ཏོ་ཞེས་པ་ནི་ཏིང་ངེ་འཛིན་གཉིས་འཆད་པར་འདོད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
