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
[Block 491]
ཕོ་དང་མོའི་དབང་པོ་དག་ནི་ལུས་ཀྱི་ཕྱོགས་གཅིག་གོ། །

[Block 492]
ལྷག་མ་ཁམས་ལྔ་པོ་དེ་དག་དང་ཆོས་ཀྱི་ཁམས་ཀྱི་ཕྱོགས་ནི་དབང་པོ་མ་ཡིན་པ་ཞེས་བྱ་བར་གྲུབ་པོ། །ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་བསྟན་པ་ཞེས་བྱ་སྟེ། མཛོད་ཀྱི་གནས་དང་པོའོ།། །།

[Block 493 [HEADING]]
## དབང་པོ་བསྟན་པ། ^2-0

[Block 494 [HEADING]]
### དབང་པོ་རྣམས་བཤད་པ། ^2-1-0

[Block 495 [HEADING]]
#### དབང་པོའི་དོན། ^2-1-1-0

[Block 496]
དབང་པོ་རྣམས་བཤད་པ་ལ། དབང་པོའི་དོན་ནི་དབང་ཕྱུག་དམ་པའོ། །

[Block 497]
འདི་དག་ལས་གང་ཞིག་གང་ལ་དབང་བྱེད་ཅེ་ན། ལྔ་པོ་རྣམས་ནི་དོན་བཞི་ལ་དབང་བྱེད། རེ་ཞིག་མིག་དང་རྣ་བ་དག་རེ་རེ་ཞིང་དོན་བཞི་བཞི་ལ་དབང་བྱེད་པ་ནི་ལོང་བ་དང་འོན་པ་དག་ནི་མི་མཛེས་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་ལུས་མཛེས་པར་བྱ་བ་དང་མཐོང་བ་དང་ཐོས་ནས་ཡ་ང་བ་ཡོངས་སུ་སྤོང་བའི་ཕྱིར་ལུས་ཡོངས་སུ་སྲུང་བ་དང་། མིག་དང་རྣ་བའི་རྣམ་པར་ཤེས་པ་མཚུངས་པར་ལྡན་པ་དང་བཅས་པ་དག་བསྐྱེད་པ༌[^198]དང་། གཟུགས་ལ་ལྟ་བ་དང་སྒྲ་ཉན་པ་དག་གི་ཐུན་མོང་མ་ཡིན་པའི་རྒྱུ་ཉིད་ལ་དབང་བྱེད་པའོ། །

[Block 498]
སྣ་དང་། ལྕེ་དང་། ལུས་ནི་སྔ་མ་བཞིན་དུ་ལུས་མཛེས་པར་བྱ་བ་ལ་དབང་བྱེད་པ་དང་། དེ་དག་གིས་ཁམ༌[^199]གྱི་ཟས་ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་ཕྱིར་ལུས་ཡོངས་སུ་སྲུང་བ་ལ་དབང་བྱེད་པ་དང་། རང་ལ་བརྟེན་པའི་རྣམ་པར་ཤེས་པ་སྐྱེད་པ་དང་། རང་གི་ལུས༌[^200]ཉམས་སུ་མྱོང་བ་ལ་སྔར་བཞིན་དུ་དབང་བྱེད་པའོ། །

[Block 499]
བཞི༌[^201]རྣམས་གཉིས་ལའོ།[^202] །

[Block 500]
རེ་ཞིག་ཕོ་དང་མོའི་དབང་པོ་དག་ནི་སེམས་ཅན་གྱི་བྱེ་བྲག་དང་། ཁྱད་པར་དག་ལ་དབང་བྱེད་དེ། དེ་ལ་སེམས་ཅན་གྱི་བྱེ་བྲག་ནི་མོ་དང་ཕོ་ཞེས་བྱ་བའོ།[^203] །

[Block 501]
སེམས་ཅན་གྱི་ཁྱད་པར་ནི་ནུ་མ་ལ་སོགས་པའི་དབྱིབས་དང་ང་རོ་དང་སྤྱོད་པ་གཞན་པ་ཉིད་དོ། །

[Block 502]
གཞན་དག་ན་རེ་ནི་ཀུན་ནས་ཉོན་མོངས་པ་དང་རྣམ་པར་བྱང་བ་དག་ལ་དབང་བྱེད་དེ། དེ་དང་མི་ལྡན་པ་ལ་སྡོམ་པ་མ་ཡིན་པ་ལ་སོགས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 503]
སྲོག་གི་དབང་པོ་ནི་རིས་མཐུན་པར་མཚམས་སྦྱོར་བ་དང་། ཡང་དག་པར་འཛིན་པ་དག་ལ་དབང་བྱེད་དོ། །

[Block 504]
ཡིད་ཀྱི་དབང་པོ་ནི་ཡང་སྲིད་པར་མཚམས་སྦྱོར་བ་དང་། རང་གི་ངོ་བོ་དང་མཐུན་པར་བྱེད་པ་དག་ལ་དབང་བྱེད་དོ། །

[Block 505]
བདེ་བ་ལ་སོགས་པའི་དབང་པོ་ལྔ་གང་ཡིན་པ་དང་། དད་པ་ལ་སོགས་པ་བརྒྱད་གང་ཡིན་པ།

[Block 506 [VERSE]]
[^204]ལྔ་དང་བརྒྱད་པོ་དེ་རྣམས་ནི། །
ཀུན་ནས་ཉོན་མོངས་རྣམ་བྱང་དང་། །
གོ་རིམས་བཞིན་དུ་དབང་བྱེད་དེ། །

[Block 507]
བདེ་བ་ལ་སོགས་པ་ལྔ་པོ་དག་ནི་ཀུན་ནས་ཉོན་མོངས་པ་ལ་དབང་བྱེད་དེ། དེ་དག་ལ་འདོད་ཆགས་ལ་སོགས་པ་རྒྱས་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 508]
དད་པ་ལ་སོགས་པ་རྣམས་ནི། རྣམ་པར་བྱང་བ༌[^205]ལ་དབང་བྱེད་དེ། དེ་དག་ནི་རྣམ་པར་བྱང་བར་བྱེད་པའི༌[^206]ཕྱིར་རོ། །

[Block 509]
གཞན་དག་ན་རེ།

[Block 510 [VERSE]]
རང་གི་དོན་དང་ཐམས་ཅད་ལ། །
དམིགས་པར་དབང་བྱེད་ཕྱིར་དབང་དྲུག །

[Block 511]
མིག་ལ་སོགས་པ་ལྔ་པོ་དག་ནི་རང་རང་གི་དོན་ལ་དམིགས་པར་བྱ་བ་ལ་དབང་བྱེད་དོ། །

[Block 512]
སྒྲ་ཐོས་པ་ཡང་མེད་པ་དེའི་ཕྱིར༌[^207]ཐུན་མོང་གི་རྒྱུ་ཡིན་པའི་ཕྱིར་ཡིད་ནི་དོན་ཐམས་ཅད་ལ་དམིགས་པ་ལ༌[^208]དབང་བྱེད་དེ། དེའི་ཕྱིར་དེ་དག་ནི་སོ་སོར་དབང་པོའོ། །

[Block 513 [VERSE]]
མོ་ཉིད་ཕོ་ཉིད་ལ་དབང་ཕྱིར། །
ལུས་ལས་མོ་དང་ཕོ་དབང་དག །

[Block 514]
རྣམ་པར་བཞག་སྟེ། དོན་ཐ་དད་པ་དག་ནི་མ་ཡིན་ནོ། །

[Block 515]
མོའི་ངོ་བོ་ནི་མོ་ཉིད་དོ། །

[Block 516]
ཕོའི་ངོ་བོ་ནི་ཕོ་ཉིད་དོ། །

[Block 517]
དེ་ལ་ཕོ་དང་མོ་དག་གི་ང་རོ་ལ་སོགས་པ་གཞན་པའོ། །

[Block 518 [VERSE]]
རིས་གནས་ཀུན་ནས་ཉོན་མོངས་དང་། །
རྣམ་པར་བྱང་ལ་དབང་བྱེད་ཕྱིར། །
སྲོག་དང་ཚོར་བ་རྣམས་དང་ནི། །
དད་སོགས་ལྔ་ཡང་དབང་པོར་འདོད། །

[Block 519]
སྲོག་གི་དབང་པོ་ནི་རིས་མཐུན་པར་གནས་པར་བྱ་བ་དང་། ཚོར་བ་རྣམས་ནི་ཀུན་ནས་ཉོན་མོངས་ལ་དང་། དད་པ་ལ་སོགས་པ་ལྔ་པོ་དག་ནི་རྣམ་པར་བྱང་བ་ལ་དབང་བྱེད་དེ། འདི་ལྟར་དེ་དག་ནི་ཉོན་མོངས་པ་རྣམས་ཀྱང་རྣམ་པར་གནོན༌[^209]ལ་ལམ་ཡང་འདྲེན་པར་བྱེད་དོ། །

[Block 520 [VERSE]]
མྱ་ངན་འདས་སོགས་གོང་ནས་གོང་། །
ཐོབ་པ་ལ་ནི་དབང་བྱེད་ཕྱིར། །
ཀུན་ཤེས་བྱེད་དང་ཀུན་ཤེས་དང་། །
དེ་བཞིན་ཀུན་ཤེས་ལྡན་དབང་པོ། །

[Block 521]
དེ་ལ་ཀུན་ཤེས་བྱེད་པའི་དབང་པོ་ནི་ཀུན་ཤེས་པའི་དབང་པོ་ཐོབ་པར་བྱ་བ་ལ་དང་། ཀུན་ཤེས་པའི་དབང་པོ་ནི་ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ༌[^210]ཐོབ་པར་བྱ་བ་ལ་དང་། ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་ནི་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བར་བྱ་བ་ལ་དབང་བྱེད་དོ། །

[Block 522]
སོགས་པའི་སྒྲ་ནི་རྣམ་གྲངས་གཞན་དུ་བསྟན་པར་བྱ་བའི་ཕྱིར་ཏེ། མཐོང་བ་དང་བསྒོམ་པས་སྤང་བར་བྱ་བའི་ཉོན་མོངས་པ་སྤོང་བ་དང་། མཐོང་བའི་ཆོས་ལ་བདེ་བར་གནས་པ་ལ་དབང་བྱེད་པའི་ཕྱིར་དབང་པོ་གསུམ་དག་གོ། །

[Block 523]
དབང་བྱེད་པའི་ཕྱིར་དབང་པོ་ཉིད་ཡིན་ན་གོ། །

[Block 524]
མ་རིག་པ་ལ་སོགས་པ་ཁ་བསྐང་དགོས་པ་ནི་མ་ཡིན་ཏེ། གང་གི་ཕྱིར་འདི་ལྟར་འདི་ནི་སེམས་ཀྱི་བརྟེན༌[^211]དང་དེའི་བྱེ་བྲག །

[Block 525 [VERSE]]
གནས་དང་ཀུན་ནས་ཉོན་མོངས་ཉིད། །
ཚོགས་དང་རྣམ་བྱང་ཇི་སྙེད་པ། །
དབང་པོ་རྣམས་ཀྱང་དེ་སྙེད་དུ། །

[Block 526]
འདོད་དེ། དེ་ལ་སེམས་ཀྱི་རྟེན་ནི་དབང་པོ་དྲུག་དག་ཡིན་ཏེ། སྐྱེ་མཆེད་དྲུག་པོ་ཡང་སེམས་ཅན་གྱི་རྫས་ཀྱི་གཞི་ཡིན་ནོ། །

[Block 527]
མོ་དང་ཕོའི་དབང་པོ་དག་གིས་ནི་དེ་མོ་དང་ཕོར་བྱེ་བྲག་ཏུ་འབྱེད་དོ། །

[Block 528]
སྲོག་གི་དབང་པོས་ནི་གནས་པར་བྱེད་དོ། །

[Block 529]
ཚོར་བ་རྣམས་ཀྱིས་ནི་ཀུན་ནས་ཉོན་མོངས་པར་བྱེད་དོ། །

[Block 530]
དད་པ་ལ་སོགས་པ་ལྔས་ནི་རྣམ་པར་བྱང་བ་ལ་སོགས་པའི་ཚོགས་སོག༌[^212]པར་བྱེད་དོ། །
--- END BLOCKS ---
