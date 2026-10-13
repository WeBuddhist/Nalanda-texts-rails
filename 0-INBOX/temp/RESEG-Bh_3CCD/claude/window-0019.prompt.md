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
[Block 666]
འདི་ནི་ཐབས་དང་ཤེས་རབ་རོ་གཅིག་པའི་བདག་ཉིད་བུད་མེད་དང་སྐྱེས་པའི་ཐ་སྙད་དང་བྲལ་བའི་མ་ནིང་གི་བཟླས་པར་བཤད་དོ་ཞེས་རྡོ་རྗེ་བཟླས་པ་རྣམ་པ་བཅུ་གཅིག་པའོ། །

[Block 667]
[^445]

[Block 668]
རྡོ་རྗེ་འཆང་ཆེན་པོའི་བཟླས་པ་ལ༌[^446]ཡང་དབྱེ་བ་གཞན་བཤད་པར་བྱ་སྟེ། རེ་ཞིག་དང་པོ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཕྱག་རྒྱ་ཆེན་པོའི༌[^447]གཟུགས་སུ་བདག་ཉིད་བསམས་ཏེ། ལྐོག་མ་དང་སྙིང་ག་དང་ལྟེ་བ་དང་གསང་བ་དག་ཏུ་འབྱུང་བ་ཆེན་པོ་བཞིའི་རང་བཞིན་གྱི་དཀྱིལ་འཁོར་མྱུར་དུ་དགོད་དེ། དེ་རྣམས་ཀྱི་སྟེང་དུ་ཐུགས་ཀྱི་རྡོ་རྗེའི་ས་བོན་གྱི་ཆ༌[^448]རེ་རེ་རྣམ་པར་བཀོད་ལ། འཇུག་པ་ལ་སོགས་པའི་རིམ་པས་ཇི་སྲིད་སེམས་རྩེ་གཅིག་པའི་བར་དུ་བསམ་པར་བྱའོ། །

[Block 669]
དེ་ལ་ཆ་དགོད་པའི་རིམ་པ་འདི་ཡིན་ཏེ། སྙིང་གའི་པདྨར་ཡི་གེ་མགོ་མེད་དེ་དཔེར་ན་ཧའོ། །

[Block 670]
ལྐོག་མའི་པདྨར་མགོ་བོ་སྟེ། དཔེར་ན་ཨའོ། །

[Block 671]
གསང་བའི་པདྨར་དབྱངས་ཏེ་དཔེར་ན་ཨུའོ། །

[Block 672]
ལྟེ་བའི་པདྨར་དབྱངས་ཀྱི་མཐའ་སྟེ་དཔེར་ན་དབྱངས་ཀྱི་མཐའོ། །

[Block 673]
ཇི་སྐད་དུ། ལྷ་མོ་བཞི་ཡིས་ཞུས་པ་ལས་ཀྱང་།

[Block 674 [VERSE]]
མགོ་མེད་སྙིང་གའི་པདྨར་གནས། །
ཁ་ཡི་པདྨར་མགོ་བོ་སྟེ། །
གསང་བའི་པདྨར་དབྱངས་གནས་པ། །

[Block 675]
ལྟེ་བའི་པདྨར་དབྱངས་མཐའོ། །

[Block 676 [VERSE]]
འདི་ཉིད་འགྲོ་དང་འོང་བ་ཡིས། །
ཐིག་ལེ་རྣལ་འབྱོར་ལ་འཇུག་པའོ། །

[Block 677]
ཞེས་འབྱུང་ངོ་། །

[Block 678 [VERSE]]
རབ་ཏུ་བྱེད་པ་ལས་ཀྱང་། །
ཐབས་ཀྱི་དམ་པ་རབ་འཇུག་པའོ།[^449] །
རྣལ་འབྱོར་དངོས་གྲུབ་རབ་སྟེར་བའི། །
གསང་བའི་ཡི་གེ་བཤད་པར་བྱ། །

[Block 679 [VERSE]]
གང་ཞིག་བསམས་པ་ཙམ་གྱིས་ནི། །
རྣལ་འབྱོར་ཅན་ལ་མཆོག་སྟེར༌[^450]འགྱུར། །
དང་པོའི་ཡི་གེའི་སྦྱོར་བ་ཡིས། །
རྟག་ཏུ་དབུགས༌[^451]ནི་རྔུབ་པར་བྱེད། །

[Block 680 [VERSE]]
བརྒྱད་པའི་མཐའ་དང་ཡང་དག་ལྡན། །
ཡི་གེ་ཨུ་དང་ཐིག་ལེར་བཅས། །
རྣལ་འབྱོར་པ་ཡིས་དབུགས་གཏོང༌[^452]བྱེད། །
འདི་ནི་ཅི་དགའི་བཟླས་པར་བཤད། །

[Block 681]
རྡོ་རྗེ་བཟླས་པ༌[^453]རྣམ་པ་བཅུ་གཅིག་པོ་འདིས་ཐ་མལ་པའི་ངག་གི་བརྗོད་པའི་རྣམ་པར་རྟོག་པ་བཟློག་པས་འཇིག་རྟེན་ལས་འདས་པའི་ཏིང་ངེ་འཛིན་མངོན་དུ་གྱུར་པ་ན། གསུང་གི་རྡོ་རྗེའི་ཏིང་ངེ་འཛིན་ལ་འཇུག་པར་འགྱུར་རོ། །

[Block 682]
ཐ་མལ་པའི་ངག་ནི་རྣམ་པ་བཞི་སྟེ། མཚན་ཉིད་ཀྱི་ངག་དང་། རྨི་ལམ་གྱི་ངག་དང་། གནས་ངན་ལེན་པའི་མངོན་པར་ཞེན་པའི་ངག་དང་། ཐོག་མ་མེད་པའི་དུས་ཀྱི་རྣམ་པར་རྟོག་པའི་ངག་གོ། །

[Block 683]
ཇི་སྐད་དུ། དེ་ལ་བློ་གྲོས་ཆེན་པོ་མཚན་ཉིད་ཀྱི་ངག་ནི་རང་གི་རྣམ་པར་རྟོག་པའི་གཟུགས་ཀྱི་མཚན་མ་ལ་མངོན་པར་ཞེན་པ་ལས་འབྱུང་བའོ། །

[Block 684]
བློ་གྲོས་ཆེན་པོ༌[^454]རྨི་ལམ་གྱི་ངག་ནི་སྔར་མྱོང་བའི་ཡུལ་རྗེས་སུ་དྲན་པས༌[^455]རྟོག་པའི་ཡུལ་མེད་བཞིན་དུ་འབྱུང་བའོ། །

[Block 685]
བློ་གྲོས་ཆེན་པོ་གནས་ངན་ལེན་པའི་མངོན་པར་ཞེན་པས་བྱུང་བའི༌[^456]ངག་ནི་སེམས་ཅན་གྱི་སྔོན་བྱས་པའི་ལས་ཀྱི་དབང་ལས་འབྱུང་ངོ་། །བློ་གྲོས་ཆེན་པོ་ཐོག་མ་མེད་པའི་དུས་ནས་རྣམ་པར་རྟོག་པའི་ཚིག་ནི་ཐོག་མ་མེད་པའི་སྤྲོས་པ་ལ་མངོན་པར་ཞེན་པའི་གནས་ངན་ལེན་གྱི་རང་གི་ས་བོན་གོམས་པ་ལས་བྱུང་བ༌[^457]སྟེ། བློ་གྲོས་ཆེན་པོ་ངག་གི་རྣམ་པར་རྟོག་པའི་མཚན་ཉིད་བཞི་པོ་འདི་དག་གོ་ཞེས་མིའམ་ཅིའི་རྒྱལ་པོས་ཞུས་པ་ལས་བྱུང༌[^458]ངོ་། །དེ་བཟློག་པས་འཇིག་རྟེན་ལས་འདས་པའི་ངག་མངོན་དུ་གྱུར་པས་རྡོ་རྗེ་ལྟ་བུའི་ངག་རྫོགས་པར་གྱུར་པ་དང་། བསྟོད་པ་དང་སྨད་པ་ལ་སོགས་པའི་ཚིག་གི་ཚོགས་ཐོས་ནས། ཡིད་བདེ་བ་དང་ཡིད་མི་བདེ་བར་མི་འགྱུར་རོ་ཞེས་རྡོ་རྗེ་བཟླས་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 686 [HEADING]]
#### སེམས་རྣམ་པར་དག་པ། ^1-2-2-0

[Block 687]
ངག་རྣམ་པར་དག་པའི་འོག་ཏུ་སེམས་རྣམ་པར་དག་པ་ལ་འབད་པར་བྱ་སྟེ། དེ་ལ་ཐབས་ནི་གཉིས་ཏེ། སྔགས་ཀྱི་རིམ་པ་དང་། ཕྱག་རྒྱའི་རིམ་པའོ། །

[Block 688 [HEADING]]
##### སྔགས་ཀྱི་རིམ་པ། ^1-2-2-1-0

[Block 689]
དེ་ལ་སྔགས་ཀྱི་རིམ་པ་ནི་འདི་ལྟར་རིག་པར་བྱ་སྟེ།

[Block 690]
དང་པོ་སེམས་ནི་རྣམ་པ་བརྒྱད་དེ་ཀུན་གཞི་རྣམ་པར་ཤེས་པ་དང་། ཉོན་མོངས་པ་ཅན་དང་། སྒོ་ལྔ་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའོ། །

[Block 691]
རྣམ་པར་ཤེས་པ་བརྒྱད་པོ༌[^459]དེ་དག་མདོར་བསྡུས་པས་གསུམ་དུ་འགྱུར་ཏེ།

[Block 692 [VERSE]]
རྣམ་པར་སྨིན་པའི་རྣམ་ཤེས་དང་། །
ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་དང་། །
འཇུག་པའི་རྣམ་པར་ཤེས་པའོ། །

[Block 693]
རྣམ་པར་ཤེས་པ་གསུམ་པོ་དེས་ནི༌[^460]སེམས་ཅན་གྱི་ཁམས་འཁོར་བའི་ས་རུ་འགྲོ་བ་དང་། འོང་བ་དག་གིས་འཁོར་བར་བྱེད་དོ། །

[Block 694]
ཇི་སྐད་དུ།

[Block 695 [VERSE]]
དམྱལ་བ་ནས་ནི་ཡི་དགས་གནས་སུ་འགྲོ། །
སླར་ཡང་ལྷ་ཡི་གནས་སུ་སྐྱེ་བར་འགྱུར། །

[Block 696]
ཞེས་འབྱུང་ངོ་། །དེ་རྣམས་གནས་གྱུར་པ་ལས་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་སྔོན་དུ་བྱས་པས་ཐར་པར་འགྱུར་ཏེ། ཇི་སྐད་དུ།

[Block 697 [VERSE]]
འདོད་ཆགས་ལ་སོགས་ཀྱིས་གོས་པའི། །
སེམས་ཉིད་འཁོར་བར་བཤད་པ་སྟེ། །
དེ་ལས་རྣམ་པར་དབེན་པ་ནི། །
རྒྱལ་བས་མདོར་བསྡུས་ཐར་པ་གསུངས། །

[Block 698]
ཞེས་འབྱུང་ངོ་། །རྣམ་པར་ཤེས་པ་གསུམ་པོ་དེའི་བརྡ་འདི་དག་ཡིན་ཏེ། སེམས་དང་ཡིད་དང་རྣམ་ཤེས་དང་། སྣང་བ་དང་སྣང་བ་མཆེད་པ་དང་སྣང་བ་འཐོབ་པ་དང་། ཤེས་རབ་དང་ཐབས་དང་ཉེ་བར་ཐོབ་པའོ། །

[Block 699]
ཟླ་བ་དང་ཉི་མ་དང་མུན་པའོ། །

[Block 700]
མཚན་མོ་དང་ཉིན་མོ་དང་མཚམས༌[^461]དང་སྟོང་པ་དང་ཤིན་ཏུ་སྟོང་པ་དང་སྟོང་པ་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 701]
དེ་ལ་འཇུག་པའི་རྣམ་པར་ཤེས་པ་གནས་གྱུར་པ་ལ་གཉེན་པོ་ནི་སྟོང་པ་ཉིད་དང་སྣང་བའི་ཡེ་ཤེས་སོ། །

[Block 702]
ཉོན་མོངས་པ་ཅན་གྱི་ཡིད་གནས་གྱུར་པ་ལ་གཉེན་པོ་ནི་སྣང་བ་མཆེད་པ་དང་ཤིན་ཏུ་སྟོང་པའོ། །

[Block 703]
ཀུན་གཞི་རྣམ་པར་ཤེས་པ་གནས་གྱུར་པ་ལ་གཉེན་པོ་ནི་སྣང་བ་ཐོབ་པ་དང་ཆེན་པོ་སྟོང་པའོ། །

[Block 704]
ཡེ་ཤེས་གསུམ་པོ་དེ༌[^462]རོ་གཅིག་པར་བྱེད་པ་འོད་གསལ་བའི་ཡེ་ཤེས་ཐམས་ཅད་སྟོང་པའི་ངོ་བོའོ། །

[Block 705]
རྣམ་པར་ཤེས་པ་གསུམ་པོའི་རང་བཞིན་ནི་བརྒྱད་ཅུའོ། །
--- END BLOCKS ---
