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
མོའི་དབང་སོགས་ལྡན། བརྒྱད་དང་། གང་ཞིག་མོའི་དབང་པོ་དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་བདུན་པོ་དེ་དག་དང་མོའི་དང་བརྒྱད་དང་ལྡན་ནོ། །

[Block 632]
སོགས་ཞེས་བྱ་བའི་སྒྲས་ནི་ཕོའི༌[^254]དབང་པོ་དང་། ཡིད་མི་བདེ་བ་དང་། དད་པ་ལ་སོགས་པ་གཟུང༌[^255]སྟེ། དེ་དག་དང་ལྡན་པ་ནི་རེ་རེ་ཞིང་ཡང་བརྒྱད་དང་ལྡན་པ་ཡིན་ཏེ། བདུན་པོ་དེ་དག་དང་། ཕོའི་དབང་པོ་དང་ལྡན་ནོ། །

[Block 633]
ཡིད་མི་བདེ་བའི་དབང་པོ་ཡང་དེ་དང་འདྲའོ། །

[Block 634]
དད་པ་ལ་སོགས་པ་དང་ལྡན་པ་ནི་ལྔ་པོ་དེ༌[^256]དག་དང་། བཏང་སྙོམས་དང་། སྲོག་དང་། ཡིད་དང་ལྡན་ནོ། །

[Block 635]
ཀུན་ཤེས་ལྡན་པ་ཡི། །དབང་པོ་ལྡན་ལ་བཅུ་གཅིག་ལྡན། །གང་ཞིག་ཀུན་ཤེས་པའི་དབང་པོ་དང་ལྡན་པ་དེ་ནི་གདོན་མི་ཟ་བར་བདེ་བ་དང་། ཡིད་བདེ་བ་དང་། བཏང་སྙོམས་དང་། སྲོག་དང་། ཡིད་དང་དད་པ་ལ་སོགས་པ་དག་དང་། ཀུན་ཤེས་པའི་དབང་པོ་དང་། བཅུ་གཅིག་དང་ལྡན་ནོ། །

[Block 636]
དེ་བཞིན་དུ་ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་དང་ལྡན་པ་ཡང་བཅུ་པོ་དེ་དག་ཉིད་དང་ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་དང་ལྡན་ནོ། །

[Block 637 [VERSE]]
ཀུན་ཤེས་བྱེད་པའི་དབང་ལྡན་ལ། །
བཅུ་གསུམ་ངག་དང་ལྡན་པ་ཡིན། །

[Block 638]
ཡིད་དང་། སྲོག་དང་། ལུས་ཀྱི་དབང་པོ་དག་དང་། ཚོར་བའི་དབང་པོ་བཞི་དག་དང་། དད་པ་ལ་སོགས་པ་དང་། ཀུན་ཤེས་པར་བྱེད་པའི་དབང་པོ་དང་ལྡན་ནོ། །

[Block 639]
གང་ཞིག་ནང་ན་ཉུང་བ་དང་ལྡན་པ་དེ་དབང་པོ་ཇི་སྙེད་ཅིག་དང་ལྡན་ཞེ་ན།

[Block 640 [VERSE]]
དགེ་མེད་ནང་ན་ཉུང་ལྡན་པ། །
ལུས་ཚོར་སྲོག་ཡིད་བརྒྱད་དང་ལྡན། །

[Block 641]
དགེ་བའི་རྩ་བ་ཀུན་དུ་ཆད་པ་སྟེ། དེ་ནང་ན་ཉུང་བ་དག་དང་ལྡན་ན་ཚོར་བ་ལྔ་དག་དང་། ལུས་དང་། ཡིད་དང་། སྲོག་དང་། དབང་པོ་བརྒྱད་དང་ལྡན་ནོ། །

[Block 642 [VERSE]]
ཇི་ལྟར་དགེ་བ་མེད་པ་ལྟར། །
གཟུགས་མེད་བྱིས་པའང་དེ་བཞིན་ཏེ། །
བཏང་སྙོམས་སྲོག་ཡིད་དགེ་རྣམས་དང་། །
སོ་སོའི་སྐྱེ་བོ་བཏང་སྙོམས་དང་། །

[Block 643]
སྲོག་དང་། ཡིད་དང་། དད་པ་ལ་སོགས་པ་ལྔ་དང་ལྡན་ནོ། །

[Block 644]
ཡང་གང་ཞིག་ནང་ན་དབང་པོ་མང་པོ་དང་ལྡན་པ་དེ་ཇི་སྙེད་ཅིག་དང་ལྡན་ཞེ་ན།

[Block 645 [VERSE]]
མང་པོར་ལྡན་ན་བཅུ་དགུ་སྟེ། །
དྲི་མ་མེད་རྣམས་མ་གཏོགས་སོ། །

[Block 646]
མཚན་གཉིས། ཟག་པ་མེད་པ་གསུམ་མ་གཏོགས་པ་མཚན་གཉིས་པ་ནི་བཅུ་དགུ་དང་ལྡན་ནོ། །

[Block 647]
གཞན་ཡང་གང་ཞིག་ཅེ་ན། འཕགས་པ་ཆགས་བཅས་ཏེ། མཚན་གཅིག་དྲི་མེད་གཉིས་མ་གཏོགས། །སློབ་པ་འདོད་ཆགས་དང་མ་བྲལ་བ་མཚན་གཅིག་པ་ཀུན་ཤེས་པ་དང་ལྡན་པའི་དབང་པོ་དང་གཉིས་པོ་ལས་གང་ཡང་རུང་བ་གཅིག༌[^257]དང་ལྡན་པ་མ་གཏོགས་པ་བཅུ་དགུ་དང་ལྡན་པའོ། །

[Block 648 [HEADING]]
### ངེས་པར་ལྷན་ཅིག་སྐྱེ་བ། ^2-2-0

[Block 649]
དབང་པོ་རྣམས་ཀྱི་རབ་ཏུ་དབྱེ་བ་རྒྱས་པར་བཤད་ཟིན་ནས། འདི་དཔྱད་པར་བྱ་སྟེ། ཀྱི༌[^258]འདུས་བྱས་ཀྱི་ཆོས་འདི་དག་ཇི་ལྟར་མཚན་ཉིད་ཐ་དད་པ་དེ་བཞིན་དུ་ཐ་དད་པར་སྐྱེ་བ་ཞིག་ཡིན་ནམ། འོན་ཏེ་ཁ་ཅིག་ངེས་པར་ལྷན་ཅིག་སྐྱེ་བ་ཡང་ཡོད་ཅེ་ན། སྨྲས་པ། ཡོད་དེ། ཆོས་འདི་དག་ཐམས་ཅད་ནི་གཟུགས་དང་། སེམས་དང་སེམས་ལས་བྱུང་བ་དག་དང་། སེམས་དང་ལྡན་པ་མ་ཡིན་པ་དག་དང་། འདུས་མ་བྱས་པ་དང་ལྔར༌[^259]འགྱུར་རོ། །

[Block 650]
དེ་ལ་འདུས་མ་བྱས་ལ་ནི་སྐྱེ་བ་མེད་པ་ཉིད་དོ། །

[Block 651 [HEADING]]
#### ཆོས་གཟུགས་ཅན་རྣམས་ཀྱི་ངེས་པ། ^2-2-1-0

[Block 652]
ཆོས་གཟུགས་ཅན་རྣམས་ཀྱི་ངེས་པ་ནི་འདི་ཡིན་ཏེ། འདོད་ན་དབང་པོ་མེད་པ་དང་། སྒྲ་མེད་ཕྲ་རབ་རྡུལ་རྫས་བརྒྱད། །ཐམས་ཅད་ལས་ཕྲ་བའི་གཟུགས་ནི་བསགས་པའི་རྡུལ་ཕྲ་རབ་ཅེས་བྱ་སྟེ། དེ་འདོད་པའི་ཁམས་ན་སྒྲ་ཡང་མེད་དབང་པོ་ཡང་མེད་པ་ཞིག་ཡིན་ན་ནི་རྫས་བརྒྱད་དང་ལྡན་པར་སྐྱེ་སྟེ། འབྱུང་བ་ཆེན་པོ་བཞི་དང་། གཟུགས་དང་། དྲི་དང་། རོ་དང་། རེག་བྱ་རྣམས་སོ། །

[Block 653]
ལུས་དབང་ལྡན་ལ་རྫས་དགུའོ། །

[Block 654]
གང་རྫས་བརྒྱད་དང་། ལུས་ཀྱི་དབང་པོ་ཡོད་པ་དེ་ནི་དེ་ཉིད་དང་དགུའོ། །

[Block 655]
དབང་པོ་གཞན་ལྡན་རྫས་བཅུའོ། །

[Block 656]
གང་ལ་མིག་ལ་སོགས་པ་གང་ཡང་རུང་བ་ཞིག་ཡོད་པ་དེ་ཁོ་ན་དང་བཅུ་པའོ། །

[Block 657]
དེ་དག་སྒྲ་དང་བཅས་པ་ཞིག་ཏུ་སྐྱེ་ན་ཡང་རྫས་དགུ་དང་། བཅུ་དང་། [^260]བཅུ་གཅིག་དང་ལྡན་ནོ། །

[Block 658]
རྫས་ཀྱི་སྒྲ༌[^261]ཡང་འདིར་འགྱུར་བའི༌[^262]རིགས་ཀྱི་དོན་ཏོ། །

[Block 659]
དེ་བཞིན་དུ་གཟུགས་ལ་སོགས་པ་སོ་སོར་འབྱུང་བ་བཞི་ལ་བརྟེན་པར་འདོད་དོ། །

[Block 660]
གཟུགས་ལ་སོགས་པ་རྫས་ཀྱི་སྒྲ་ནི་སྐྱེ་མཆེད་ཀྱི་དོན་ཅན་ནོ། །

[Block 661]
དེ་ལྟ་ན་ཡང་དབྱིབས་ལ་སོགས་པར༌[^263]གྲུབ་བོ། །

[Block 662 [HEADING]]
#### སེམས་དང་སེམས་ལས་བྱུང་བ། ^2-2-2-0

[Block 663]
གཟུགས་ཅན་རྣམས་ཀྱི་ངེས་པར་ལྷན་ཅིག་འབྱུང་བ་བཤད་ཟིན་ནས་ལྷག་མ་རྣམས་ཀྱི་བརྗོད་པར་བྱ་སྟེ།

[Block 664 [VERSE]]
སེམས་དང་སེམས་བྱུང་ངེས་ལྷན་ཅིག །
ཐམས་ཅད་འདུས་བྱས་མཚན་ཉིད་དང་། །

[Block 665]
ཐོབ་པའམ། ཐོབ་པ་དང་ནི་སེམས་ཅན་དུ་སྟོན་པ་ཁོ་ན་དང་ལྷན་ཅིག་སྐྱེའི་གཞན་དང་ནི་མ་ཡིན་ནོ་ཞེས་བྱེ་བྲག་ཏུ་བྱ་བའི་ཕྱིར་འམ༌[^264]ཞེས་བྱ་བའི་སྒྲ་སྨོས་སོ། །

[Block 666 [HEADING]]
##### སེམས་བྱུང་རྣམ་ལྔ། ^2-2-2-1-0

[Block 667]
སེམས་ལས་བྱུང་བ་རྣམས་ཞེས་བརྗོད་པ་སེམས་ལས་བྱུང་བ་དེ་དག་གང་ཞེ་ན། སེམས་བྱུང་རྣམ་ལྔ་སྟེ། ས་མང༌[^265]ལ་སོགས་ཐ་དད་ཕྱིར། །འདི་ལྟ་སྟེ། ས་མང་པོ༌[^266]དག་དང་། དགེ་བའི་ས་མང་པོ་པ་རྣམས་དང་། ཉོན་མོངས་པའི་ས་མང་པོ་པ་རྣམས་དང་། མི་དགེ་བའི་ས་མང་པོ་པ་རྣམས་དང་། ཉོན་མོངས་པ་ཆུང་ངུའི་ས་པ་རྣམས་སོ། །

[Block 668 [VERSE]]
ཚོར་དང་སེམས་པ་འདུ་ཤེས་དང་། །
འདུན༌[^267]དང་རེག་དང་བློ་གྲོས་དྲན། །
ཡིད་ལ་བྱེད་དང་མོས་པ་དང་། །
ཏིང་ངེ་འཛིན་སེམས་ཐམས་ཅད་ལ། །

[Block 669]
དེ་ལ་ཚོར་བ་ནི་བཤད་ཟིན་ཏོ། །

[Block 670]
སེམས་པ་ནི་སེམས་མངོན་པར་འདུ་བྱེད་པའོ། །
--- END BLOCKS ---
