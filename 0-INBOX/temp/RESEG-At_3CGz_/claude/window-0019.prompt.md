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
ཞེས་གསུངས་པ་དང་། ཡང་སློབ་དཔོན་ཞི་བ་ལྷའི་ཞལ་ནས་ཀྱང་།

[Block 667 [VERSE]]
དེ་རིང་སངས་རྒྱས་རིགས་སུ་སྐྱེས། །
སངས་རྒྱས་སྲས་སུ་བདག་གྱུར་ཏོ། །
རིགས་དང་མཐུན་པའི་ལས་བརྩམས་ཏེ།[^373] །
སྐྱོན་མེད་བཙུན་པའི་རིགས་འདི་ལ། །

[Block 668]
རྙོག་པར་མི་འགྱུར་དེ་ལྟར་བྱ། །ཞེས་གསུངས་པས། སྡོམ་པ་བླངས་པའི་བྱང་ཆུབ་སེམས་དཔའ་དེས་ཚུལ་ཁྲིམས་བསྲུང་ཞིང་སྤེལ་དགོས་པས།

[Block 669 [VERSE]]
རང་གི༌[^374]ལུས་ངག་སེམས་ནི་རྣམ་དག་རྒྱུ། །
འཇུག་པའི་སེམས་ཀྱིས་བདག་ཉིད་སྡོམ་གནས་པས།[^375] །

[Block 670]
ཞེས་སྨྲས་ཏེ།

[Block 671]
རང་གི་ལུས་ངག་སེམས་ནི་རྣམ་དག་རྒྱུ་མེད་དེ།[^376] །ཞེས་བྱ་བ་ནི་ཇི་སྐད་དུ་དེ་བཞིན་གཤེགས་པའི་སྙིང་རྗེའི་མདོ་ལས།

[Block 672]
ལུས་གཙང་བྱེད་དང་། ངག་གཙང་བྱེད་དང་། ཡིད་གཙང་བྱེད་དོ་ཞེས་གསུངས་པས་སྡོམ་པའི་ཚུལ་ཁྲིམས་ཀྱིས་ལུས་དང༌[^377]ངག་གཉིས་དག་པར་བྱེད་ལ། དགེ་བའི་ཆོས་སྡུད་པའི་ཚུལ་ཁྲིམས་དང་སེམས་ཅན་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་ཀྱིས་སེམས་དག་པར་བྱེད་དོ། །

[Block 673]
ཡང་ན་ཚུལ་ཁྲིམས་རེ་རེས་ཀྱང་ལུས་ལ་སོགས་པ་གསུམ་ཀ་དག༌[^378]པར་བྱེད་དོ། །

[Block 674]
ཡང་ན་སྲོག་གཅོད་པ་ལ་སོགས་པ་བདུན་སྤངས་པས་ནི་ལུས་དང་ངག་དག་པར་བྱེད་ལ། བརྣབ་སེམས་ལ་སོགས་པ་གསུམ་སྤངས་པས་ནི་སེམས་དག་པར་བྱེད་དོ། །

[Block 675]
གཞན་ཡང་དོན་འདི་ལ་དགོངས་ནས་མིའམ་ཅིའི་རྒྱལ་པོ་ལྗོན་པས་ཞུས་པའི་མདོ་ལས།

[Block 676]
ཆགས་པ་དང་ཞེ་སྡང་དང་གཏི་མུག་དང་བྲལ་བས་ལུས་ཡོངས་སུ་དག་པའི་ཚུལ་ཁྲིམས་དང་། བདག་གི་ལྷ་དཀོན་མཆོག་གསུམ་ལ་མི་སླུ་བའི་མཚན་ཉིད་ཀྱིས༌[^379]ངག་ཡོངས་སུ་དག་པའི་ཚུལ་ཁྲིམས་དང་། བརྣབ་སེམས་དང་གནོད་སེམས་དང་ལོག་པར་ལྟ་བ་མེད་པས་སེམས་ཡོངས་སུ་དག་པའི་ཚུལ་ཁྲིམས་དང་ཞེས་གསུངས་སོ། །

[Block 677]
དེ་ལྟ་བུ་ཡིན་པས་ན་ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་ལ་ལེགས༌[^380]པར་སློབ་པར་ཡང་འགྱུར་ཞིང་། དེ་ལ་གོམས་པའི་སྟོབས་ཀྱིས་ཚུལ་ཁྲིམས་དེ་ལ་དགའ་བ་དང་སྤྲོ་བ་དང་འདོད་པ་དང་དེ་ལ་བརྩོན་པ་དང་གུས་པ་ཆེར་འགྱུར་རོ་ཞེས་བསམས༌[^381]ནས་སྨྲ་བ་ནི།

[Block 678 [VERSE]]
ཚུལ་ཁྲིམས་བསླབ་པ་གསུམ་ལ་ལེགས་བསླབས༌[^382]ནས། །
ཚུལ་ཁྲིམས་བསླབ་པ་གསུམ་ལ་གུས་ཆེར་འགྱུར། །

[Block 679]
ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 680 [HEADING]]
## ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་གསུམ། ^7-0

[Block 681]
ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་གསུམ་ནི་སྡོམ་པའི་ཚུལ་ཁྲིམས་དང་། དགེ་བའི་ཆོས་སྡུད་པའི་ཚུལ་ཁྲིམས་དང་། སེམས་ཅན་གྱི་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་སོ། །

[Block 682 [HEADING]]
### སྡོམ་པའི་ཚུལ་ཁྲིམས། ^7-1-0

[Block 683]
དེ་ལ་སྡོམ་པའི་ཚུལ་ཁྲིམས་ནི་བཅས་པའི་ཁ་ན་མ་ཐོ་བ་སྲུང་བའི༌[^383]སོ་སོར་ཐར་པའི་རིས་བདུན་གྱི་སྡོམ་པ་དང་། རང་བཞིན་གྱི་ཁ་ན་མ་ཐོ་བ་སྲུང་བའི་མི་དགེ་བ་བཅུ་བསྲུང་བའོ། །

[Block 684 [HEADING]]
### དགེ་བའི་ཆོས་སྡུད་པའི་ཚུལ་ཁྲིམས། ^7-2-0

[Block 685]
དེ་ལ་དགེ་བའི་ཆོས་སྡུད་པའི་ཚུལ་ཁྲིམས་ནི་སྡོམ་པ་ཡང་དག་པར་བླངས་པའི་འོག་ཏུ་གང་ཅུང་ཟད་ལུས་དང་ངག་དང་ཡིད་ཀྱིས༌[^384]བྱང་ཆུབ་ཀྱི་ཕྱིར་དགེ་བ་བསགས་པ་སྟེ། དེ་ཡང་ཁྱད་པར་དུ་ཐོས་པ་དང་བསམ་པ༌[^385]དང་བསྒོམ་པ་རྣམས་ལ་གཅིག་ཏུ་དགའ་བས་མངོན་པར་སྦྱོར་བའོ།[^386] །

[Block 686]
དེ་བཞིན་དུ་དུས༌[^387]སུ་བླ་མ་རྣམས་ལ་གསོང་པོར་སྨྲ་བ་དང་། ཕྱག་བྱ་བ་དང་། ལྡང་བ་དང་། ཐལ་མོ་སྦྱོར་བ་དང་ཞེས༌[^388]དང་བཅས་པས་ཀུན་དུ་སྤྱོད་པ་དང་། བསྙེན་བཀུར་བྱེད་པ་དང་། ཡོན་ཏན་དང་ལྡན་པའི་བསྔགས་པ་བརྗོད་པ་དང་། བསོད་ནམས་ཐམས་ཅད་ལ་རྗེས་སུ་ཡི་རང་བ་དང་། གཞན་གྱིས་བརྙས་པ་ལ་བཟོད་པ་དང་། དགེ་བ་ཐམས་ཅད་བྱང་ཆུབ་ཏུ་བསྔོ་བ་དང་། དུས་དུས་སུ་ཡང་དག་པའི་སྨོན་ལམ་དག་སྣ་ཚོགས་པ་འདེབས་པ་དང་། མཆོད་པའི་རྣམ་པ་རྒྱ་ཆེན་པོས་དཀོན་མཆོག་གསུམ་ལ་མཆོད་པར་བྱེད་པ་དང་། དགེ་བ་ལ་བརྩོན་འགྲུས་བྱེད་པ་དང་། བག་མེད་པ་སྤངས་པ་དང་། དྲན་པ་དང་ཤེས་བཞིན་དང་ལྡན་པས་བསླབ་པའི་གཞི་རྣམས་བསྲུང་བ་དང་། དབང་པོའི་སྒོ་བསྡམས་པ་དང་། ཟས་ཀྱི་ཚོད་རིག་པ་དང་། ནམ་གྱི་ཆ་སྟོད་དང་ཆ་སྨད་ལ་མི་ཉལ་བར་རྗེས་སུ་བརྩོན་པ་དང་། སྐྱེས་བུ་དམ་པ་ལ་བརྟེན་པ་དང་། ཉེས་པ་དག་ཤེས་ཤིང་མཐོང་ནས་སྤང་བ༌[^389]དང་། ཉེས་པ་ཆོས་བཞིན་དུ་འཆགས་པ་དང་། དེ་ལྟ་བུའི་ཕྱོགས་དང་མཐུན་པའི་དགེ་བའི་ཆོས་རྣམས་སྲུང་བ་དང་སྤེལ་བ་སྟེ། དེ་ལྟར་ན་དགེ་བའི་ཆོས་སྡུད་པའི་ཚུལ་ཁྲིམས་ལ་གནས་ན་དགེ་བའི་ཆོས་ཀྱི་ཚུལ་ཤིན་ཏུ་བསྡུས་པར་འགྱུར་ཏེ། འདི་འདོད་པའི་ལོངས་སྤྱོད་ལ་ལྟ་བ་ཅུང་ཟད་ཙམ་ཡང་དང་དུ་ལེན་པར་མི་བྱེད་ན་མང་པོ་ལྟ་ཅི་སྨོས། ཕ་རོལ་ཏུ་ཕྱིན་པ་བཅུ་དང་། བསྡུ་བའི་དངོས་པོ་བཞི་དང་། ཚད་མེད་པ་བཞི་སྟེ། བྱང་ཆུབ་ཀྱི་སེམས་བཅུའི་བདག་ཉིད་ཡིན་ནོ། །

[Block 687 [HEADING]]
### སེམས་ཅན་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས། ^7-3-0

[Block 688]
སེམས་ཅན་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་ནི་འདི་ལ་སེམས་ཅན་གྱི་དོན་བྱ་བ་ཡིན་ཏེ། ནད༌[^390]ལ་སོགས་པའི་སྡུག་བསྔལ་ཅན་རྣམས་ལ་ནད་གཡོག་ལ་སོགས་པའི་གྲོགས༌[^391]བྱེད་པ་ཡིན་ནོ། །

[Block 689]
ལོང་བ་དག་གི་ལོང་ཁྲིད་དང་། འོན་པ་དག་ལ་ལག་བརྡས་སྟོན་པ་དང་། རྐང་ལག་མེད་པ་དག་ཁུར་བ་དང་། འདོད་པའི་འདུན་པ་ཅན་དག་གི་དེ་སེལ་བ་དང་། གཞན་གྱིས༌[^392]སྨ་ཕབ་ཅིང་ཕམ་པ་རྣམས་དེ་དག་གི༌[^393]སྡུག་བསྔལ་སེལ་བ་དང་། ལམ་གྱིས་ངལ་བ་དག་ལ་བཟའ་བ་དང་། བཏུང་བ་དང་། གོས་དང་། ཁང་པ་དག་གིས་ཕན་འདོགས་སོ། །

[Block 690]
གསོ་བའི་རིག་པས་ནད་པ་དག་ལ་ཟང་ཟིང་མེད་པའི་སེམས་ཀྱིས་མི་སྐྱོ་བར་ཕན་འདོགས་སོ། །

[Block 691]
མདོར་ན་སེམས་ཅན་གྱི་སྡུག་བསྔལ་ཐམས་ཅད་སེལ་བ་དང་། དེ་བསལ་བར་སེམས་བསྐྱེད་པ་དང་། དགེ་བ་ཐམས་ཅད་གཞན་གྱི་དོན་དུ་བསྔོ་བའོ། །

[Block 692]
འདི་དག་གི་དོན་རྒྱས་པར་ཚུལ་ཁྲིམས་ཀྱི་ལེའུ་རུ་བལྟ་བར་བྱའོ། །

[Block 693]
དེ་ལྟ་བུ་ཚུལ་ཁྲིམས་ཀྱི་སྡོམ་པ་རྣམ་པ་གསུམ་ནི་བསོད་ནམས་ཀྱི་ཚོགས་ཡིན་པས་ཚོགས་དེ་རྫོགས་པར་བྱའོ་སྙམ་དུ་བསམས་ནས།

[Block 694 [VERSE]]
དེ་བས་རྣམ་དག་རྫོགས་བྱང་ཆུབ། །
སེམས་དཔའི༌[^394]སྡོམ་པའི་སྡོམ་དག་ནི། །
འབད་པ་བྱས་པས་རྫོགས་བྱང་ཆུབ། །
ཚོགས་ནི་ཡོངས་སུ་རྫོགས་པར་འགྱུར། །

[Block 695]
ཞེས་བྱ་བ་འདི་ཡིན་ནོ། །

[Block 696]
དེ་བས་ན་རྫོགས་པའི་བྱང་ཆུབ་ཐོབ་པར་འདོད་ཅིང་དེའི་རྒྱུ་བསོད་ནམས་རྫོགས་པར་འདོད་ན་བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པ༌[^395]འབད་པ་དང་རྩོལ་བ་བྱས་པས་བསོད་ནམས་ཀྱི་ཚོགས་རྫོགས་པར་འགྱུར་རོ་ཞེས་ཤེས་པར་བྱའོ། །

[Block 697]
སྡོམ་པའི་སྡོམ་དག་ནི་ཞེས་པ་ནི་འཕགས་པ་ཐོགས་མེད་ཀྱི་ལུགས་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པ་དང་། སློབ་དཔོན་ཞི་བའི་ལྷའི་ལུགས་ལ་གནས་པའི་བྱང་ཆུབ་སེམས་དཔའི་སྡོམ་པའོ། །

[Block 698]
དེ་ལྟ་བུའི་ཤིང་རྟ་ཆེན་པོའི་ལམ་གཉིས་ལ་གནས་ནས་འབད་པ་དང་། བརྩོན་པར་བྱས་ན་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་གཉིས་རྫོགས་པར་བྱས་ཏེ། མངོན་པར་རྫོགས་པར་བྱང་ཆུབ་པར་འགྱུར་རོ་ཞེས་བླ་མ་དག་གསུངས་པ༌[^396]ཡིན་ནོ། །

[Block 699]
བླ་མའི་ཞལ་ནས་དེ་ལྟ་བུའི་ཚུལ་ཁྲིམས་ཀྱི་བསླབ་པ་གསུམ་ནི་ཡང་དག་པར་བླངས་པ་དང་། རྗེས་སུ་བསྲུངས་པས༌[^397]བདག་དང་གཞན་གྱི་དོན་དང་། ཕན་པ་དང་བདེ་བར་འགྱུར་བའི་ཕྱིར་དགེ་བའོ། །

[Block 700]
བྱང་ཆུབ་སེམས་དཔའི་བསླབ་པ་དཔག་ཏུ་མེད་པ་བསྡུས་པའི་ཕྱིར་དཔག་ཏུ་མེད་པའོ། །

[Block 701]
སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་པ་དང་བདེ་བ་མངོན་པར་བསྒྲུབ་པའི༌[^398]ཕྱིར་ཕན་འདོགས་པའོ། །

[Block 702]
བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཀྱི་འབྲས་བུ་ལེན་པར་བྱེད་པའི་ཕྱིར་འབྲས་བུ་ཆེ་བར་རིག་པར་བྱའོ་ཞེས་སྡོམ་པ་ཉི་ཤུ་པའི་འགྲེལ་པ་ལས་གསུངས་སོ། །

[Block 703]
དེ་ལྟར་བླ་མ་དམ་པ་ལས་བསླབ་པ་དེ་ལྟ་བུ་ལེགས་པར་བསླངས༌[^399]ཤིང་། ཆོས་དང་མཐུན་པར་བསྲུང་བའི་བྱང་ཆུབ་སེམས་དཔའི་ཚོགས་ཀྱི་ལམ་ཐར་པའི་ཆ་དང་མཐུན་པའི་དགེ་བའི་རྩ་བ་བསྐྱེད་པར་འདོད་པ་དེ་ནི། ཚེ་རབས་སྔ་མའི་བག་ཆགས་བཟང་པོ་ཡོད་པ་ཡིན་ཏེ།

[Block 704]
མགོན་པོ་བྱམས་པས་དབུས་དང་མཐའ་རྣམ་པར༌[^400]འབྱེད་པ་ལས།

[Block 705 [VERSE]]
སྣོད་གྱུར་རྣམ་པར་སྨིན་བརྗོད་དང་། །
དེ་ཡི་དབང་གིས༌[^401]སྟོབས་དང་ནི། །
འདོད་དང་འཕེལ་དང་རྣམ་དག་སྟེ། །
འབྲས་བུ་རྣམས་ནི་གོ་རིམས་བཞིན། །
--- END BLOCKS ---
