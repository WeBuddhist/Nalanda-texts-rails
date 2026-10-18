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
གཟུགས་ལ་སོགས་པ་ཡུལ་གྱི་ཁམས་དྲུག་པོ་དེ་དག་ནི་ཕྱིའི་ཡིན་ནོ། །

[Block 667]
བདག་མེད་ན་ཇི་ལྟར་ན་ནང་གི་འམ། ཕྱིའི་ཡིན་ཞེ་ན། སེམས་ནི་ངར་འཛིན་པའི་རྟེན་ཡིན་པའི་ཕྱིར་བདག་ཅེས་ཉེ་བར་འདོགས་ཏེ།

[Block 668 [VERSE]]
མཁས་པས་བདག་ཉིད་ཤིན་ཏུ་ནི། །
དུལ་བས་མཐོ་རིས་ཐོབ་པར༌[^267]འགྱུར། །

[Block 669]
ཞེས་གསུངས་ལ།

[Block 670]
བཅོམ་ལྡན་འདས་ཀྱིས་གཞན་ལས།

[Block 671 [VERSE]]
སེམས་དུལ་བ་ནི་ལེགས་པ་སྟེ། །
སེམས་དུལ་བས་ནི་བདེ་བ་འདྲེན། །

[Block 672]
ཞེས་སེམས་དུལ་བ་ཡིན་པར་གསུངས་པས་དེའི་ཕྱིར་མིག་ལ་སོགས་པ་ནི་སེམས་བདག་ཏུ་གྱུར་པའི་རྟེན་གྱི་དངོས་པོར་ཉེ་བར་གྱུར་པའི་ཕྱིར་ནང་གི་ཉིད་ཡིན་ནོ། །

[Block 673]
གཟུགས་ལ་སོགས་པ་རྣམས་ནི་ཡུལ་དུ་གྱུར་པའི་ཕྱིར་ཕྱི་རོལ་གྱི་ཉིད་ཡིན་ནོ། །

[Block 674]
དེ་ལྟ་ན། འོ་ན་ནི་རྣམ་པར་ཤེས་པའི་ཁམས་དྲུག་པོ་དག་ནང་གི་ཡིན་པར་མི་འགྱུར་ཏེ། དེ་དག་ཡིད་ཀྱི་ཁམས་ཉིད་དུ་མ་གྱུར་པ་ནི་སེམས་ཀྱི་རྟེན་དུ་མི་འགྱུར་རོ་ཞེ་ན། གང་གི་ཚེ་ཡིན་པ་དེའི་ཚེ་ན་ཡང་དེ་དག་ཉིད་དེ་དག་ཡིན་ཏེ་མཚན་ཉིད་ལས་ནི་མི་འདའོ། །

[Block 675]
དེ་ལྟ༌[^268]མ་ཡིན་ན་ཡིད་ཀྱི་ཁམས་འདས་པ་ཁོ་ན་ཡིན་པར་འགྱུར་གྱི་མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བ་ཡིན་པར་ནི་མི་འགྱུར་བ་ཞིག་ན་ཁམས་བཅོ་བརྒྱད་པོ་དག་ནི་དུས་གསུམ་པ་ཡིན་པར་ཡང་འདོད་དོ། །

[Block 676]
གལ་ཏེ་ཡང་རྣམ་པར་ཤེས་པ་མ་འོངས་པ་དང་ད་ལྟར་བྱུང་བ་ཡིད་ཀྱི་ཁམས་ཀྱི༌[^269]མཚན་ཉིད་མ་ཡིན་པར་གྱུར་ན་འདས་པའི་དུས་ན་ཡང་ཡིད་ཀྱི་ཁམས་སུ་རྣམ་པར་གཞག་པར་མི་འགྱུར་ཏེ། མཚན་ཉིད་ནི་དུས་རྣམས་སུ་འཁྲུལ་པ་མེད་དོ། །

[Block 677 [HEADING]]
#### བརྟེན་པ་དང་བཅས་པ་དང་དེ་དང་མཚུངས་པ། ^1-3-16-0

[Block 678]
བརྟེན་པ་དང་བཅས་པའི་ཁམས་རྣམས༌[^270]ནི་དུ། དེ་དང་མཚུངས་པ་རྣམས་ནི་དུ་ཞེ་ན། རེ་ཞིག་གཅིག་ཏུ། ཆོས་ཞེས་བྱ་བ་ནི། བརྟེན་པ༌[^271]དང་བཅས། གང་ཞིག༌[^272]རྣམ་པར་ཤེས་པ་གང་གི་ཡུལ་དུ་ངེས་ལ་གལ་ཏེ་དེ་ལ༌[^273]རྣམ་པར་ཤེས་པ་དེ་སྐྱེས་པའམ་སྐྱེས་པའི༌[^274]ཆོས་ཅན་གྱི་ཡུལ་དེ་ནི་བརྟེན་པ་དང་བཅས་པ་ཞེས་བྱ་ལ། གང་ལ་ཡིད་ཀྱི་རྣམ་པར་ཤེས་པ་མཐའ་ཡས་པ་མ་སྐྱེས་པའམ་སྐྱེ་བར་མི་འགྱུར་བའི་ཆོས་ཀྱི་ཁམས་གང་ཡིན་པ་དེ་ནི་འགའ་ཡང་མེད་དེ། འདི་ལྟར་འཕགས་པའི་གང་ཟག་ཐམས་ཅད༌[^275]ནི་གདོན་མི་ཟ་བར་ཆོས་ཐམས་ཅད་ལ༌[^276]བདག་མེད་དོ་སྙམ་པའི་སེམས་འདི་སྐྱེའོ། །

[Block 679]
དེའི་དམིགས་པ་ཡང་རང་གི་ངོ་བོ་དང་ལྷན་ཅིག་འབྱུང་བ་མ་གཏོགས་པ་ཆོས་ཐམས་ཅད་ཡིན་ནོ། །

[Block 680]
སེམས་ཀྱི་སྐད་ཅིག་མ་དེ་ཡང་སེམས་ཀྱི་སྐད་ཅིག་མ་གཞན་གྱི་དམིགས་པ་མ༌[^277]ཡིན་པས་སྐད་ཅིག་མ་གཉིས་ཀྱི་དམིགས་པར་ནི་ཆོས་ཐམས་ཅད་འགྱུར་ཏེ། དེ་ལྟ༌[^278]བས་ན་ཆོས་ཀྱི་ཁམས་ནི་རྟག་ཏུ་བརྟེན་པ༌[^279]དང་བཅས་པ་ཡིན་ནོ། །

[Block 681]
ལྷག་མ་ནི། དེ་དང་མཚུངས་པ་དག་ཀྱང་ཡིན། །ཀྱང་ཞེས་བྱ་བའི་སྒྲ་ནི་བརྟེན་པ་དང་བཅས་པ་དག་ཀྱང་ཡིན་པའོ། །

[Block 682]
དེ་དང་མཚུངས་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞིག་ཅེ་ན། གང་ཞིག་རང་གི་ལས་མི་བྱེད། །གང་རང་གི་ལས་བྱེད་པ་དེ་ནི་བརྟེན་པ་དང་བཅས་པའོ་ཞེས་བཤད་པར་འགྱུར་རོ། །

[Block 683]
དེ་ལ་མིག་གང་གིས་གཟུགས་རྣམས་མཐོང་བ་དང་། ལྟ་བ་འམ་ལྟ་བར་འགྱུར་བའི་མིག་དེ་ནི་བརྟེན་པ་དང་བཅས་ཞེས་བྱ་སྟེ། དེ་བཞིན་དུ་ཡིད་ཀྱི་བར་ལ་ཡང་རང༌[^280]རང་གི་ཡུལ་ལ་བྱེད་པས་བརྗོད་པར་བྱའོ། །

[Block 684]
ཁ་ཆེ་བ་རྣམས་ཀྱི་ལྟར་ན་དེ་དང་མཚུངས་པའི་མིག་ནི་རྣམ་པ་བཞི་སྟེ། གཟུགས་རྣམས་མ་མཐོང་བར་འགགས་པ་དང་། འགག་པ་དང་། འགག་པར་འགྱུར་བ་གང་ཡིན་པ་དང་། མི་སྐྱེ་བའི་ཆོས་གང་ཡིན་པའོ། །

[Block 685]
ནུབ་ཕྱོགས་པ་རྣམས་ཀྱི་ལྟར་ན་རྣམ་པ་ལྔ་སྟེ། མི་སྐྱེ་བའི་ཆོས་དེ་ཉིད་རྣམ་པར་ཤེས་པ་དང་ལྡན་པ་དང་། ལྡན་པ་མ་ཡིན་པ་དང་རྣམ་པ་གཉིས་སུ་ཕྱེ་བའི་ཕྱིར་ཏེ། ལུས་ཀྱི་བར་དུ་ཡང་དེ་བཞིན་དུ་རིག་པར་བྱའོ། །

[Block 686]
ཡིད་ནི་མི་སྐྱེ་བའི་ཆོས་ཁོ་ན་དེ༌[^281]འདྲ་བ་ཡིན་ནོ། །

[Block 687]
གཟུགས་གང་དག་མིག་གིས་མཐོང་བར་གྱུར་པ་དང་། མཐོང་བ་དང་། མཐོང་བར་འགྱུར་བ་དེ་དག་ནི་བརྟེན་པ༌[^282]དང་བཅས་པ་རྣམས་སོ། །

[Block 688]
དེ་དང་འདྲ་བ་ནི་རྣམ་པ་བཞི་སྟེ། གང་དག་མ་མཐོང་བ་ཉིད་དུ་འགགས་པ་དང་། [^283]འགག་པ་དང་། འགག༌[^284]པར་འགྱུར་བ་དང་། གང་དག་མི་སྐྱེ་བའི་ཆོས་རྣམས་ཏེ། དེ་བཞིན་དུ་རེག་བྱའི་བར་དག་ལ་ཡང་རང་གི་དབང་པོའི་བྱེད་པས་དེ་དང་འདྲ་བ་དག་ཏུ་རིག་པར་བྱའོ། །

[Block 689]
གཅིག་གི་མིག་བརྟེན་པ༌[^285]དང་བཅས་པ་གང་ཡིན་པ་དེ་ནི་ཐམས་ཅད་ཀྱི་ཡིན་ནོ། །

[Block 690]
དེ་དང་མཚུངས་པ་རྣམས་ཀྱང་དེ་བཞིན་ཏེ། ཡིད་ཀྱི་བར་དུ་ཡང་དེ་དང་འདྲའོ། །

[Block 691]
གཟུགས་ནི་གང་ཞིག་ལྟ་བ་དེའི་བརྟེན་པ་དང་བཅས་པ་ཡིན་ལ་གང་མི་ལྟ་བ་དེའི་ནི་དེ༌[^286]དང་མཚུངས་པ་ཡིན་ནོ། །ཅིའི་ཕྱིར་ཞེ་ན། གཟུགས་གང་ལ་གཅིག་ལྟ་བ་དེ་ལ་མང་པོ་ཡང་ལྟ་བར་འགྱུར་བ་སྲིད་པ་ཡོད་དེ། དཔེར་ན་ཟླ་བ་དང་བྲོ་གར་དང་གྱད་དག་ལ་ལྟ་བ་ལྟ་བུའོ། །

[Block 692]
གང་གཉིས་མིག་གཅིག་གིས་ལྟ་བར༌[^287]འགྱུར་བ་སྲིད་པ་ནི་མེད་དེ། དེའི་ཕྱིར་འདི་ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་རྒྱུད་གཅིག་གི་དབང་གིས་རྣམ་པར་གཞག་གོ། །

[Block 693]
གཟུགས་ནི༌[^288]ཐུན་མོང་ཡིན་པའི་ཕྱིར་རྒྱུད༌[^289]མའི་དབང་གིས་རྣམ་པར་གཞག་གོ །གཟུགས་ཇི་ལྟ་བ་དེ་བཞིན་དུ་སྒྲ་དང་དྲི་དང་རོ་དང་རེག་བྱའི་ཁམས་དག་ལ་ཡང་རིག་པར་བྱའོ། །

[Block 694]
སྒྲ་ནི་དེ་ལྟ་ཡིན་དུ་ཆུག་ན་དྲི་ལ་སོགས་པ་ནི་གང་དག་གཅིག་གིས་འཛིན་པ་དེ་དག་གཞན་གྱིས་མི་འཛིན་ཏེ། ཕྲད་ནས་འཛིན་པའི་ཕྱིར་རོ། །

[Block 695]
དེ་ལྟ་བས་ན་དེ་དག་ཀྱང་ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་མིག་ལ་སོགས་པ་བཞིན་དུ་བསྒྲེ་བའི་རིགས་སོ་ཞེ་ན། དེ་ལྟ་བུ་ཡོད་མོད་ཀྱི་འོན་ཀྱང་དེ་དག་ལ་ཡང་སྲིད་པའི་ཕྱིར་ཐུན་མོང་བ་ཉིད་དེ། གཅིག་གིས༌[^290]སྣ་ལ་སོགས་པའི་རྣམ་པར་ཤེས་པ་བསྐྱེད་པར༌[^291]འགྱུར་བའི་དྲི་ལ་སོགས་པ་གང་དག་ཡིན་པ་དེ་དག་ཉིད་གཞན་དག་གི་ཡང་ཡིན་པ་སྲིད་པ་དེ་ནི་ཡོད་ཀྱི་མིག་ལ་སོགས་པ་ནི་དེ་ལྟ་མ་ཡིན་ནོ། །

[Block 696]
དེ་ལྟ་བས་ན་དེ་དག་ནི་གཟུགས་བཞིན་དུ་བསྒྲེའོ། །

[Block 697]
མིག་གི་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་དག་གི་བརྟེན་པ་དང་བཅས་པ་དང་དེ་དང་མཚུངས་པ་ཉིད་ནི་སྐྱེ་བ་དང་མི་སྐྱེ་བའི་ཆོས་ཡིན་པའི་ཕྱིར་ཡིད་ཀྱི་ཁམས་ཇི་ལྟ་བ་བཞིན་ནོ། །

[Block 698]
བརྟེན་པ་དང་བཅས་པ་ཞེས་བྱ་བའི་དོན་ཅི་ཞེ་ན། དབང་པོ་དང་ཡུལ་དང་རྣམ་པར་ཤེས་པ་རྣམས་ཕན་ཚུན་བརྟེན་པ་འམ། བྱེད་པ་ལ་བརྟེན་པ་ནི་བརྟེན་པའོ། །

[Block 699]
དེ་འདི་དག་ལ་ཡོད་པས་བརྟེན་པ་དང་བཅས་པ་རྣམས་སམ། འབྲས་བུ་རེག་པ་འདྲ་བའི་ཕྱིར་བརྟེན་པ་མཚུངས་པའོ། །

[Block 700]
གང་དག་བརྟེན་པ་དང་བཅས་པ་མ་ཡིན་པ་དེ་དག་ནི་བརྟེན་པ་དང་བཅས་པ་དེ་དག་དང་རིགས་འདྲ་བའི་ཕྱིར་དེ་དག་དང་མཚུངས་པ་དག་གོ། །

[Block 701 [HEADING]]
#### མཐོང་བས་སྤང་བར་བྱ་བ་ལ་སོགས་པ། ^1-3-17-0

[Block 702]
མཐོང་བས་སྤང་བར་བྱ་བའི་ཁམས་རྣམས་ནི་དུ། བསྒོམས་པས༌[^292]སྤང་བར་བྱ་བ་རྣམས་ནི་དུ། སྤང་བར་བྱ་བ་མ་ཡིན་པ་རྣམས་ནི་དུ་ཞེ་ན། རེ་ཞིག་གཟུགས་ཅན་བཅུ་ནི་བསྒོམས་པས༌[^293]སྤང་བྱ་ཡིན། ལྔ་ཡང་ཡིན་ཏེ་རྣམ་པར་ཤེས་པའི་ཁམས་ལྔ་པོ་དག་གོ། །

[Block 703]
ཐ་མའི༌[^294]གསུམ་རྣམ་གསུམ། ཡིད་ཀྱི་ཁམས་དང་། ཆོས་ཀྱི་ཁམས་དང་། ཡིད་ཀྱི་རྣམ་པར་ཤེས་པའི་ཁམས་དང་ཁམས་གསུམ་པོ༌[^295]འདི་དག་ནི་རྣམ་པ་གསུམ་པོ་འདི་དག༌[^296]སྟེ། ཕྲ་རྒྱས་བརྒྱད་ཅུ་རྩ་བརྒྱད་དང་། །དེ་དག་དང་ལྷན་ཅིག་འབྱུང་བ་དང་། དེ་དག་གི་ཐོབ་པ་རྗེས་སུ་འབྲང་བ་དང་བཅས་པ་རྣམས་ནི་མཐོང་བས་སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 704]
ཟག་པ་དང་བཅས་པ་ལྷག་མ་རྣམས་ནི་བསྒོམས་པས༌[^297]སྤང་བར་བྱ་བ་དག་ཡིན་ནོ། །

[Block 705]
ཟག་པ་མེད་པ་རྣམས་ནི་སྤང་བར་བྱ་བ་མ་ཡིན་པ་དག་གོ། །
--- END BLOCKS ---
