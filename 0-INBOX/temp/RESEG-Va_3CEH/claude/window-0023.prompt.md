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
[Block 806]
ཞེས་བྱ་བ་དང་སྦྱར་ཏེ། རྒྱུ་གང་གིས་གང་གི་ཕྱིར་མེད་པ་དེས་ན་ཆོས་རྣམས་ཡོད་པ་མ་ཡིན་ཞིང་གང་གི་ཕྱིར་སྣང་བ་དེས་ན་ཆོས་མེད་པ་ཡང་མ་ཡིན་ཏེ། ཆོས་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 807]
དེས་ན།

[Block 808 [VERSE]]
དེ་བཞིན་ཆོས་དང་ཆོས་མེད་མིན། །
གཉིས་སུ་མེད་པ་གཉིས་སུ་བསྟན། །

[Block 809]
ཆ་རེས་ཞེས་བྱ་བ་སྟེ་མཐའ་གཅིག་གིས་སོ། །

[Block 810]
མེད་པ་དང་ཡོད་པ་ཞེས་བྱ་བ་ནི་དངོས་པོ་དང་དངོས་པོ་མེད་པའོ། །

[Block 811]
རབ་ཏུ་བསྟན་ཞེས་བྱ་བ་ནི་བཤད་པའོ། །

[Block 812 [VERSE]]
གཉི་གའི་ཆ་ནི༌[^546]ཡོད་མིན་ཞིང་། །
མེད་པའང་མིན་ཞེས་བརྗོད་པར་མཛད། །

[Block 813]
ཅེས་བྱ་བ་ནི་གང་གི་ཕྱིར་གཉི་གའི་བདག་ཉིད་ཅན་གྱི་གཞན་གྱི་དབང་ཡོངས་སུ་བཟུང་ནས་ཡོད་པ་དང་མེད་པ་ཉིད་དུ་བསྟན་པའོ། །

[Block 814]
ཇི་ལྟར་སྣང་བ་དེ་བཞིན་མེད། །ཅེས་བྱ་བ་ནི་ཇི་ལྟར་དམིགས་པ་དེ་དང་དེ་བཞིན་དུ་མེད་པ་སྟེ། དེ་ཕྱིར་མེད་ཅེས་བརྗོད་པར་མཛད། །གང༌[^547]ཕྱིར་དེ་ལྟར་སྣང་གྱུར་པ། ཞེས་བྱ་བ་ལ། སྣང་བ་ཙམ་དུ་ཡོད་པའི་ཕྱིར། ཡོད་པ་ཞེས་བརྗོད་པས། དེ༌[^548]ཕྱིར་ཡོད་ཅེས་བརྗོད་པར་མཛད། །ཅེས་བྱ་བའོ། །

[Block 815]
གང་ལས་དགོངས་ན་ངོ་བོ་ཉིད་མེད་པར་བསྟན་པ་ཡིན་པ་དེ་སྟོན་པར་བྱེད་པ་ནི། རང་དང་ཞེས་བྱ་བ་ལ། གང་གི་ཕྱིར༌[^549]རང་ཉིད་རྐྱེན་མེད་པར་མི་འབྱུང་ཞེས་བྱ་བ་སྟེ། རེ་ཞིག་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ཀྱི་དགོངས་པ་གཅིག་ཡིན་ནོ། །

[Block 816]
ཆོས་རྣམས་ཀྱི་བདག་ཉིད་མེད་པའི་ཕྱིར་ཞེས་བྱ་བ་ནི་ཡང་འདིའི་དགོངས་པ་ནི་འདི་ཡིན་ཏེ། གང་འགགས་པ་དེ་ནི་དེའི་བདག་ཉིད་དུ་ཡང་མི་འབྱུང་བས་དེའི་ཕྱིར་ན་ཡང་ངོ་བོ་ཉིད་མེད་དེ།[^550] རང་གི་དངོས་ལ་མི་གནས་ཕྱིར། །ཞེས་བྱ་བ་ནི་བྱུང་བ་ཙམ་ཉིད་ན་སྐད་ཅིག་ཕྱི་མར་མི་གནས་པ་སྟེ། གནས་པར་མི་ནུས་པའི་ཕྱིར་ན་ཡང་ངོ་བོ་ཉིད་མེད་དོ། །

[Block 817]
དེ་ལྟ་བུ་ནི་རེ་ཞིག་ཉན་ཐོས་དང་ཐུན་མོང་གི་ཆོས་རྣམས་ཀྱི་ངོ་བོ་ཉིད་མེད་པ་ཉིད་དོ། །

[Block 818]
གཟུང་བ༌[^551]བཞིན་དུ་དེ་མེད་ཕྱིར། ། ཞེས་བྱ་བ་ནི་འདིས་ནི་ཉན་ཐོས་དང་ཐུན་མོང་མ་ཡིན་པ་སྟེ། གང་གི་ཕྱིར་ཇི་ལྟར་བྱིས་པས་ཡོངས་སུ་བཟུང་བའི་ཀུན་ཏུ་བརྟགས་པའི་ངོ་བོ་ནི་དེ་བཞིན་དུ་མེད་པས་དེ་ལས་དགོངས་ནས་ཐེག་པ་ཆེན་པོའི་ཚུལ་འདིར་ཆོས་ཐམས་ཅད་ཀྱི་ངོ་བོ་ཉིད་མེད་པའོ་ཞེས་གསུངས་སོ། །

[Block 819]
ཐམས་ཅད་ངོ་བོ་ཉིད་མེད་པ་ཉིད་ནི་འདི་ལྟར་གྲུབ་པ་ཡིན་པ་སྟེ། སྐྱེ་བ་མེད་པ་ལ་སོགས་པས་སོ། །

[Block 820]
གང་གི་ཕྱིར་གང་ངོ་བོ་ཉིད་མེད་པ་དེ་ནི་མ་སྐྱེས་པའོ། །

[Block 821]
གང་མ་སྐྱེས་པ་དེ་ནི་མ་འགགས་པའོ། །

[Block 822]
གང་མ་སྐྱེས་པ༌[^552]མ་འགགས་པ་དེ་ནི་གདོད་མ་ནས་ཞི་བའོ། །

[Block 823]
གང་གདོད་མ་ནས་ཞི་བ་དེ་ནི་རང་བཞིན་གྱིས༌[^553]མྱ་ངན་ལས་འདས་པ་ཡིན་པས་སོ། །

[Block 824]
ཕྱི་མ་ཕྱི་མ་རྟེན༌[^554]བྱས་ཏེ། །ཞེས་བྱ་བ་ནི་ཕྱི་མ་ཕྱི་མའི་རྒྱུའི་ངོ་བོ་ཡིན་ནོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 825 [HEADING]]
### དགོངས་པ་དང་ལྡེམ་པོར་དགོངས་པ། ^2-19-0

[Block 826 [HEADING]]
#### དགོངས་པ། ^2-19-1-0

[Block 827 [HEADING]]
##### མཉམ་པ་ཉིད་ལ་དགོངས་པ། ^2-19-1-1-0

[Block 828]
མཉམ་པ་ཉིད་ལ་དགོངས་པ་ནི་ཇི་ལྟར་ཁ་ཅིག་མཉམ་པ་ཉིད་ཀྱི་ཆོས་ཉིད་ལ་བསམས་ནས་དེ་གང་ཡིན་པ་ནི་བདག་ཡིན་ལ་བདག་གང་ཡིན་པ་ནི་དེ་ཡིན་ནོ་ཞེས་སྨྲས་པ་ལྟར། བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་ཆོས་ཀྱི་སྐུ་མཚུངས་པ་ཐུགས་ལ་བཞག་ནས། ང་ཉིད་དེའི་ཚེ་དེའི་དུས་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་བསྟན་པ་ཡིན་གྱི། རྣམ་པར་གཟིགས་གང་ཡིན་པ་དེ་ནི་ཤཱཀྱ་ཐུབ་པ་ཉིད་ནི་མ་ཡིན་ཏེ། མཉམ་པ་ཉིད་ལ་དགོངས་པ་ནི་འདི་ཡིན་ནོ། །

[Block 829 [HEADING]]
##### དུས་གཞན་ལ་དགོངས་པ། ^2-19-1-2-0

[Block 830]
དུས་གཞན་ལ་དགོངས་པ་ཞེས་བྱ་བ་ལ། གང་སྙོམ་ལས༌[^555]མང་བ་རྣམས་ཐབས་ཀྱི༌[^556]རྣམ་པ་འདི་ཉིད་ཀྱིས་ཆོས་འདི་ལ་སྦྱོར་བར་བྱེད་པ་ཡིན་ཏེ། དེ་བཞིན་གཤེགས་པ་རིན་ཆེན་མང་གི་མཚན་བཟུང་བའི་རྒྱུ་ལས་བྱུང་བའི་དགེ་བའི་རྩ་བས༌[^557]དེ་དག་ཁྱད་པར་ཐོབ་པའི་རྒྱུར་འགྱུར་བ་ཙམ་ལ་དགོངས་ནས་ཡིན་གྱི་མཚན་བཟུང་བ་ཙམ་ཉིད་ཀྱིས་ངེས་པ་ལ་འཇུག་པར་འགྱུར་ཞིང་། བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པ༌[^558]མ་ཡིན་ཏེ། ཇི་ལྟར་པ་ཎ་གཅིག་པ་ཎ་སྟོང་དུ་སྒྱུར༌[^559]ཞེས་བརྗོད་པ་དེ་ནི་ཉི་མ་གཅིག་གིས་སམ། དུས་གཞན་དུ་ཞེས་བྱ་བའི་དོན་ཏེ། པ་ཎ་གཅིག་པོ་དེ་ཉིད་པ་ཎ་སྟོང་གི་རྒྱུར་གྱུར་པ་བཞིན་ནོ། །

[Block 831]
སྨོན་ལམ་བཏབ་པ་ཙམ་གྱིས་འཇིག་རྟེན་གྱི་ཁམས་བདེ་བ་ཅན་དུ་སྐྱེ་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ཡང་དེ་བཞིན་དུ་བལྟ་བར་བྱའོ། །

[Block 832 [HEADING]]
##### དོན་གཞན་ལ་དགོངས་པ། ^2-19-1-3-0

[Block 833]
དོན་གཞན་ལ་དགོངས་པ་ནི་ཐེག་པ་ཆེན་པོའི་ཆོས་ཀྱི་དོན་ཁོང༌[^560]དུ་ཆུད་པར་འགྱུར་རོ་ཞེས་བྱ་བའི་ངོ་བོ་ཉིད་གསུམ་གྱི་དོན་གྱི་མཚན་ཉིད་རང་གི༌[^561]ཁོང་དུ་ཆུད་པར་ནི་མི༌[^562]འགྱུར་རོ། །

[Block 834]
གལ་ཏེ་སྒྲ་ཇི་བཞིན་དུ་དོན་ཁོང་དུ་ཆུད་པ་འདི་བཅོམ་ལྡན་འདས་ཀྱིས་བཞེད་པ་ཡིན་ན་ནི་འདི་ལྟར་བྱས་པས༌[^563]ཀྱང་རྟོགས་པར་འགྱུར་བས་དེས་ན་དགོངས་པ་འདིའི་དོན་འདི་ནི། སངས་རྒྱས་མང་པོ་ལ༌[^564]བསྙེན་བཀུར་བྱས་པར་གྱུར་པས་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བའོ། །

[Block 835 [HEADING]]
##### གང་ཟག་གི་བསམ་པ་ལ་དགོངས་པ། ^2-19-1-4-0

[Block 836]
གང་ཟག་གི་བསམ་པ་ལ་དགོངས་པ་ནི་ཞེས་བྱ་བ་ལ། ཁ་ཅིག་ལ་སྦྱིན་པའི་བསྔགས་པ་གསུངས༌[^565]ལ། ཡང་དེ་ཉིད་ནི་མི་བསྔགས་པར་ཡང་མཛད་དོ། །

[Block 837]
དེ་ལ་འདི་ནི་གང་ཟག་གི་བསམ་པ་ལ་དགོངས་པ་ཡིན་ཏེ། གང་ཟག་གང་སེར་སྣ་ཅན་དུ་གྱུར་པ་དེ་ལ་ནི་སྦྱིན་པ་བསྔགས་པར་མཛད་ལ། གང་སྦྱིན་པ་ལ་མོས་པ་ཡོད་པ་དེ་ལ་དེ་ཉིད་བསྔགས་པར་མི་མཛད་དེ། དེས་ན་དགོངས་པ་འདི་མེད་ན་སྦྱིན་པ་ལ་བསྔགས་པ་དང་མ་བསྔགས་པ་འགལ་བ་ཉིད་ཀྱི་ཕྱིར་དགོངས་པ་འདི་ཉིད་ཀྱིས་ནི་སྦྱིན་པ་ལ་བསྔགས་པ་དང་མི་བསྔགས་པ་རིག་པར་འགྱུར་རོ། །

[Block 838]
དེ་བཞིན་དུ་ཚུལ་ཁྲིམས་ལ་སོགས་པ་ལ་ཡང་བལྟ་བར་བྱའོ། །

[Block 839]
སྒོམ་པ་ཁ་ཅིག་ཀྱང་ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་པའི་བསྒོམ༌[^566]པའོ། །

[Block 840 [HEADING]]
#### ལྡེམ་པོར་དགོངས་པ། ^2-19-2-0

[Block 841]
དགོངས་པ་དང་ལྡེམ་པོར་དགོངས་པ་ལ་ཐ་དད་དུ་བྱ་བ་ཅི་ཡོད་ཅེ་ན། བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང༌[^567]ཐུགས་ལ་བཞག་པ་སྟོན་པར་མཛད་པ་དེ་ནི་དགོངས་པ་ཡིན་ནོ། །

[Block 842]
གང་ཉིད་ཀྱིས༌[^568]ངེས་པར་བསྟན་པ་ལ་འཇུག་པར་མཛད་པ་དེ་ནི་ལྡེམ་པོར་དགོངས་པ་ཡིན་ནོ། །

[Block 843 [HEADING]]
##### བཞུགས་པ་ལ་ལྡེམ་པོར་དགོངས་པ། ^2-19-2-1-0

[Block 844]
དེ་ལ་བཞུགས་པ༌[^569]ལ་ལྡེམ་པོར་དགོངས་པ་ནི་གང་དུ་གང་ཟག་དང་ཆོས་ཀྱི་ངོ་བོ་དང་། ཁྱད་པར་དུ་ཀུན་རྫོབ་ཀྱི་བདེན་པའི་ཚུལ་དུ་སེམས་ཅན་རྣམས་བཞུགས་པའི༌[^570]ཕྱིར་བསྟན་པ་ལ༌[^571]ནི་བཞུགས་པ༌[^572]ལ་ལྡམ་པོར༌[^573]དགོངས་པའོ། །

[Block 845 [HEADING]]
##### མཚན་ཉིད་ལ་ལྡེམ་པོར་དགོངས་པ། ^2-19-2-2-0
--- END BLOCKS ---
