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
[Block 596]
གཟུགས་ན་དྲུག་གོ། །

[Block 597]
འདོད་པའི་ཁམས་ན་མཚན་མ་མེད་པ་དག་གིས་རྙེད་པ་གང་དག་ཡིན་པ་ཉིད་དོ། །

[Block 598]
གོང་མར་གཅིག །གཟུགས་མེད་པའི་ཁམས་སུ་དང་པོ་ཉིད་དུ་སྲོག་གི་དབང་པོ་གཅིག་ཁོ་ན་རྣམ་པར་སྨིན་པ་ཐོབ༌[^234]བོ། །

[Block 599 [HEADING]]
#### གཏོང་བ། ^2-1-4-0

[Block 600]
རྙེད་པ་བཤད་ཟིན་ནས་གཏོང་བ་བརྗོད་པ།

[Block 601 [VERSE]]
གཟུགས་མེད་དག་ཏུ་འཆི་བ་ནི། །
སྲོག་དང་ཡིད་དང་བཏང་སྙོམས་ཉིད། །
འགག་པར་འགྱུར་རོ་གཟུགས་ན་བརྒྱད། །

[Block 602]
གཟུགས་ཀྱི་ཁམས་སུ་འཆི་བ་ན་གསུམ་པོ་དེ་དག་དང་། མིག་ལ་སོགས་པ་ལྔ་དང་དབང་པོ་བརྒྱད་འགག་གོ། །

[Block 603]
འདོད་པར་བཅུའམ་དགུའམ་བརྒྱད། །མཚན་གཉིས་པའི་ནི་བརྒྱད་པོ་དེ་དག་དང་ཕོ་དང་མོའི་དབང་པོ་དང་བཅུ་འགག་གོ། །

[Block 604]
མཚན་གཅིག་པ་ཞིག་ཡིན་ན་དགུའོ། །

[Block 605]
མཚན་མེད་པ་ཞིག་ཡིན་ན་བརྒྱད་དོ། །

[Block 606]
རིམ་གྱིས༌[^235]འཆི་བ་དག་ལ་བཞི། རིམ་གྱིས༌[^236]འཆི་ན་ལུས་དང་སྲོག་དང་ཡིད་དང་། བཏང་སྙོམས་ཀྱི་དབང་པོ་དག་འགག་གོ། །

[Block 607]
ཉོན་མོངས་པ་ཅན་དང་ལུང་དུ་མ་བསྟན་པའི་སེམས་ཀྱིས་འཆི་བ་ལ་ནི་ཚུལ་དེའོ། །

[Block 608]
དགེ་བའི་སེམས་ཀྱིས་ཀྱང་། དགེ་ལ་ཐམས་ཅད་དག་ཏུ་ལྔ། །ཐམས་ཅད་དུ་ཇི་སྐད་བཤད་པའི་དབང་པོ་རྣམས་དང་ལྷག་པར་དད་པ་ལ་སོགས་པའི་དབང་པོ་ལྔ་ནི་དགེ་བའི་སེམས་ཀྱིས་འཆི་བ་ལ་རིག་པར་བྱའོ། །

[Block 609 [HEADING]]
#### དགེ་སྦྱོང་གི་ཚུལ་གྱི་འབྲས་བུ་འཐོབ་པ། ^2-1-5-0

[Block 610]
དབང་པོའི་སྐབས་སུ་དབང་པོའི་ཆོས་ཐམས་ཅད་དཔྱད་པར་བྱ་སྟེ། དགེ་སྦྱོང་གི་ཚུལ་གྱི༌[^237]འབྲས་བུ་གང་ཞིག་དབང་པོ་དུ་དག་གིས་འཐོབ་ཅེ་ན། འབྲས་བུ་ཐ་མ་གཉིས་དགུས་འཐོབ། །རྒྱུན་དུ་ཞུགས་པ་དང་དགྲ་བཅོམ་པ་ཉིད་ཀྱི་འབྲས་བུ་དག་ནི་དབང་པོ་དགུས་ཐོབ་བོ། །

[Block 611]
དེ་ལ་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ནི་དད་པ་ལ་སོགས་པ་དང་། ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་མ་གཏོགས་པ་དང་། ཡིད་དང་བཏང་སྙོམས་ཀྱི་དབང་པོ་དག་དང་དགུས་འཐོབ་བོ། །

[Block 612]
ཟག་པ་མེད་པ་གཉིས་ཀྱང་བྲལ་བས་ཐོབ་པ༌[^238]འདྲེན་པ་དང་གནས་པར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་རིམ་པ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 613]
དགྲ་བཅོམ་པ་ཉིད་ནི་དད་པ་ལ་སོགས་པ་དང་། ཀུན་ཤེས་བྱེད་པའི་དབང་པོ་མ་གཏོགས་པ་དག་དང་། ཡིད་ཀྱི་དབང་པོ་དང་། བདེ་བ་དང་། བཏང་སྙོམས་ཀྱི་དབང་པོ་རྣམས༌[^239]ལས་གང་ཡང་རུང་བ་ཞིག་དང་། དགུས་འཐོབ་བོ། །

[Block 614]
གཉིས་ནི་བདུན་དང་བརྒྱད་དང་དགུས། །དེ་ལ་རེ་ཞིག་གལ་ཏེ། ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་མཐར་གྱིས་ཐོབ༌[^240]ལ། དེ་ཡང་འཇིག་རྟེན་པའི་ལམ་གྱིས་ཐོབ༌[^241]ན་ནི་དད་པ་ལ་སོགས་པ་ལྔ་དང་། བཏང་སྙོམས་དང་། ཡིད་ཀྱི་དབང་པོ་དང་དབང་པོ་བདུན་དག་གིས་འཐོབ་པོ། །འོན་ཏེ་འཇིག་རྟེན་ལས་འདས་པས༌[^242]ནི་ཀུན་ཤེས་པའི་དབང་པོ་བརྒྱད་པ་ཡིན་ནོ། །

[Block 615]
ཅི་སྟེ་ཕལ་ཆེར་ལ་འདོད་ཆགས་དང་བྲལ་བ་ཞིག་གིས་འཐོབ་ན་ནི་དེ་དགུས་འཐོབ་སྟེ། དེ་གང་དག་ཁོ་ནས་རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་འཐོབ་པ་ཁོ་ན་བཞིན་ནོ། །

[Block 616]
གལ་ཏེ་ཕྱིར་མི་འོང་བའི་འབྲས་བུ་མཐར་གྱིས་ཐོབ༌[^243]ལ། དེ་འཇིག་རྟེན་དང་འཇིག་རྟེན་ལས་འདས་པ་དག་གིས་ཐོབ༌[^244]ན་ལན་ཅིག་ཕྱིར་འོང་བའི་འབྲས་བུ་བཞིན་དུ་བདུན་དང་བརྒྱད་ཀྱིས་འཐོབ་བོ། །

[Block 617]
ཅི་སྟེ་འདོད་ཆགས་དང་བྲལ་བ་ཞིག་གིས་ཐོབ༌[^245]ན་ནི་དེ་དགུས་འཐོབ་སྟེ། རྒྱུན་དུ་ཞུགས་པའི་འབྲས་བུ་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 618]
ཡང་འདིར་རྟེན་གྱི་བྱེ་བྲག་ལས་བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་ཀྱི་དབང་པོ་རྣམས་ལས་གང་ཡང་རུང་བ་ཞིག་ཡིན་ནོ། །

[Block 619]
འོ་ན་ཆོས་མངོན་པ་ལས་དབང་པོ་དུ་ཞིག་གིས་དགྲ་བཅོམ་པ་ཉིད༌[^246]འཐོབ་ཅེ་ན། སྨྲས་པ། བཅུ་གཅིག་གིས་ཞེས་བཤད་པ་ཇི་ལྟར་དགུ་དག་གིས་ཤེ༌[^247]ན། དེ་ནི་དགུ་ཁོ་ནས་འཐོབ་སྟེ།

[Block 620 [VERSE]]
བཅུ་གཅིག་དག་གིས་དགྲ་བཅོམ་ཉིད། །
འགའ་ཞིག་སྲིད་ཕྱིར་བཤད་པ་ཡིན། །

[Block 621]
གང་ཟག་འགའ་ཞིག་གིས་ཡོངས་སུ་ཉམས་ཤིང་ཡོངས་སུ་ཉམས་ནས་བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་ཀྱི་དབང་པོ་དག་གིས་དགྲ་བཅོམ་པ་ཉིད་འཐོབ་པ་སྲིད་པ་ཡོད་པས་དེའི་ཕྱིར་བཅུ་གཅིག་དག་གིས་ཞེས་གསུངས་སོ། །

[Block 622 [HEADING]]
#### དབང་པོ་དུ་དག་དང་ལྡན་པ། ^2-1-6-0

[Block 623]
དབང་པོ་གང་ཞིག་དང་ལྡན་ན་གདོན་མི་ཟ་བར་དབང་པོ་དུ་དག་དང་ལྡན་པ་ཞེས་བྱ་བ་འདི་དཔྱད་པར་བྱ་སྟེ། དེ་ལ།

[Block 624 [VERSE]]
བཏང་སྙོམས་དང༌[^248]ནི་སྲོག་དང་ནི། །
ཡིད༌[^249]དང་ལྡན་ལ་ངེས་གསུམ་ལྡན། །

[Block 625]
དེ་ནི་གདོན་མི་ཟ་བར་གསུམ་ཁོ་ན་སྟེ། འདི་དག་ནི་ཕན་ཚུན་མེད་ན་མི་ལྡན་པ་ཡིན་གྱི༌[^250]ལྷག་མ་རྣམས་དང་ནི་མ་ངེས་ཏེ། ལྡན་པ་ཡང་ཡོད།

[Block 626 [VERSE]]
མི་ལྡན་པ་ཡང་ཡོད་དོ། །
བདེ་ལུས་ལྡན་ལ༌[^251]བཞི་དག་དང་། །

[Block 627]
གང་བདེ་བ་དང་ལུས་ངག་དང་ལྡན་པ་དེ་ནི་དབང་པོ་བཞི་སྟེ། དེ་གསུམ་དང་འདི་དག་གི༌[^252]གཅིག་ལྷག་པས་སོ། །

[Block 628]
མིག་སོགས་ལྡན་པ་ལྔ་དང་ལྡན། །གང་ཞིག་མིག་གི་དབང་པོ༌[^253]ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་བཏང་སྙོམས་དང་། སྲོག་དང་། ཡིད་དང་། ལུས་ཀྱི་དབང་པོ་དག་དང་དེ་དང་དབང་པོ་ལྔ་དང་ལྡན་ཏེ། རྣ་བ་དང་། སྣ་དང་། ལྕེའི་དབང་པོ་དག་དང་ལྡན་པ་ཡང་དེ་དང་འདྲ་བར་རིག་པར་བྱའོ། །

[Block 629]
ཡིད་བདེ་ལྡན་ཡང་། གང་ཞིག་ཡིད་བདེ་བའི་དབང་པོ་དང་ལྡན་པ་དེ་ཡང་གདོན་མི་ཟ་བར་བཏང་སྙོམས་དང་། སྲོག་དང་། ཡིད་དང་། བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། དབང་པོ་ལྔ་དང་ལྡན་ནོ། །

[Block 630]
སྡུག་བསྔལ་ལྡན། བདུན་དང་། གང་ཞིག་སྡུག་བསྔལ་གྱི་དབང་པོ་དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་ལུས་དང་། སྲོག་དང་། ཡིད་དག་དང་། ཚོར་བའི་དབང་པོ་བཞི་དང་བདུན་དང་ལྡན་ནོ། །

[Block 631]
མོའི་དབང་སོགས་ལྡན། བརྒྱད་དང་། གང་ཞིག་མོའི་དབང་པོ་དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་བདུན་པོ་དེ་དག་དང་མོའི་དང་བརྒྱད་དང་ལྡན་ནོ། །

[Block 632]
སོགས་ཞེས་བྱ་བའི་སྒྲས་ནི་ཕོའི༌[^254]དབང་པོ་དང་། ཡིད་མི་བདེ་བ་དང་། དད་པ་ལ་སོགས་པ་གཟུང༌[^255]སྟེ། དེ་དག་དང་ལྡན་པ་ནི་རེ་རེ་ཞིང་ཡང་བརྒྱད་དང་ལྡན་པ་ཡིན་ཏེ། བདུན་པོ་དེ་དག་དང་། ཕོའི་དབང་པོ་དང་ལྡན་ནོ། །

[Block 633]
ཡིད་མི་བདེ་བའི་དབང་པོ་ཡང་དེ་དང་འདྲའོ། །

[Block 634]
དད་པ་ལ་སོགས་པ་དང་ལྡན་པ་ནི་ལྔ་པོ་དེ༌[^256]དག་དང་། བཏང་སྙོམས་དང་། སྲོག་དང་། ཡིད་དང་ལྡན་ནོ། །

[Block 635]
ཀུན་ཤེས་ལྡན་པ་ཡི། །དབང་པོ་ལྡན་ལ་བཅུ་གཅིག་ལྡན། །གང་ཞིག་ཀུན་ཤེས་པའི་དབང་པོ་དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་དང་། སྲོག་དང་། ཡིད་དང་དད་པ་ལ་སོགས་པ་དག་དང་། ཀུན་ཤེས་པའི་དབང་པོ་དང་། བཅུ་གཅིག་དང་ལྡན་ནོ། །
--- END BLOCKS ---
