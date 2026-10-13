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
[Block 771]
སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་བ་ནི་ལག་པ་གཡས་པ་རྡོ་རྗེ་རྩེ་གསུམ་པའི་ཕྱག་རྒྱ་བཅས་ལ། ས་ལ་བརྡབ་ཅིང་ཨོཾ་སརྦ་པཱ་བཾ་ད་ཧ་ན་མཱ་མ་རཀྵ་རཀྵ་ཧཱུཾ་ཕཊ་སྭཱ་ཧཱ་ཞེས་བརྗོད་དོ། །

[Block 772 [HEADING]]
###### ཏིང་ངེ་འཛིན་གྱིས་སྦྱང་བ། ^1-10-1-3-3-0

[Block 773]
ཏིང་ངེ་འཛིན་ནི་ས་གཞི་དེ་མི་དམིགས་པར་བསྒོམ་ཞིང་ཤིན་ཏུ་དག་པར་བསམ་མོ། །ཁ་ཅིག་ཏུ་ནི་ལས་དང་བྱ་བས་སྦྱང་ངོ་། །ཁ་ཅིག་ཏུ་ནི་སྔགས་དང་ཕྱག་རྒྱས་སྦྱང་ངོ་། །ཁ་ཅིག་ཏུ་ནི་ཏིང་ངེ་འཛིན་ཙམ་མོ། །དེ་དག་ནི་ཅི་རིགས་པར་ཤེས་པར་བྱའོ། །

[Block 774 [HEADING]]
##### བྱིན་གྱིས་བརླབ་པ། ^1-10-1-4-0

[Block 775]
དེ་ནས་བྱིན་གྱིས་བརླབ་པ་ནི་ཁཾ་ལས་ས་གཞི་སྟོང་པ་ཉིད་དུ་བསམ། ལཾ་ལས་གསེར་གྱི་ས་གཞི་ཆེན་པོར་བྱིན་གྱིས་བརླབ། སུཾ་ལས་རི་རབ་རིན་པོ་ཆེ་སྣ་བཞིའི་རང་བཞིན་དུ་བྱིན་གྱིས་བརླབ།[^822] ཧཱུཾ་ལས་ས་གཞི་རྡོ་རྗེར༌[^823]བྱིན་གྱིས་བརླབ།[^824] ཨོཾ་བཛྲ་མེ་དི་ནཱི་བཛྲི་བྷ་བ་བནྡྷ་ཧཱུཾ་ཞེས་བརྗོད་དོ། །རྡོ་རྗེའི་ས་གཞིའི་རང་བཞིན་ནམ་མཁའི་ཁམས་རྣམ་པར་དག་པར་བསམ་མོ། །

[Block 776 [HEADING]]
##### ས་གཞི་ཡོངས་སུ་གཟུང་བ། ^1-10-1-5-0

[Block 777]
ས་གཞི་ཡོངས་སུ་གཟུང་བ་ནི་མེ་ལོང་ངོས་ལྟར་མཉམ་པའི་དཀྱིལ་འཁོར་གྱི་དབུས་སུ་འདུག་ལ། ཡན་ལག་དྲུག་གི་རྣལ་འབྱོར་རམ་སྦྱོར་བ་རྣམ་པ་གསུམ་བསྒོམ་སྟེ། བཟླས་པའི་མཐར་ཐུག་གི་བར་དུ་བྱའོ། །

[Block 778]
དེ་ཡང་འོག་ནས།

[Block 779 [VERSE]]
ཁྲུས་དང་གཙང་སྦྲ་དྲི་ཞིམ་ལུས། །
སྣ་ཚོགས་རྒྱན་གྱིས༌[^825]རྣམ་པར་བརྒྱན། །
སློབ་དཔོན་དཀྱིལ་འཁོར་འཇུག་པ་ཉིད། །
འབད་པས་ཧཱུཾ་ལས་རྡོ་རྗེ་ཅན། །

[Block 780]
བྱས་ཏེ་ཕྱི་ནས་དཀྱིལ་འཁོར་བྲི། །

[Block 781]
ཞེས་བྱ་བ་སའི་ཆོ་ག་དང༌[^826]འབྲེལ་ལོ། །

[Block 782]
དེའི་རྗེས་ལ་ཚད་ཛི་ཙམ་དུ་ཞེ་ན།དཀྱིལ་འཁོར་ཁྲུ་གསུམ་ནི་ཆུང་བའི་ཚད་དོ། །དེ་ཡང་སྐུ་གསུམ་པའི་བདག་ཉིད་པས་སོ། །སོར་གསུམ་ནི་སྐུ་གསུང་ཐུགས་སོ། །དའི་རྗེས་ལ་བསྲུང་བའི་ཕྱིར། རྡོ་རྗེ་སེམས་དཔའ་བསྙེམས་བྱས་ནི་གསོལ་བ་གདབ་པའི་རྗེས་ལ་ལྡང་བ་དང་འགྱིང་བ་དང་། ཀུན་དུ་ལྟ་བ་དང་རྡོ་རྗེའི་འགྲོས་ཀྱིས་བསྐོར་བའོ། །

[Block 783]
གཡས་བརྐྱང་ཞེས་པ་ནི་གཡས་བརྐྱང་ལ་སོགས་པ་སྟང་སྟབས་རྣམས་བྱ་བའམ། གཙོ་བོའི་འདུག་ཚུལ་སྐྱིལ་ཀྲུང་ཕྱེད་པ་ཡིན་ཏེ་གཡོན་བསྐུམ་པས་གནས་སོ། །ཕྱག་གཉིས་དགྱེས་པའི་རྡོ་རྗེར་སྦྱར་བ་ནི་ཕྱག་གཉིས་པའི་ཧེ་རུ་ཀ་མ་ཡིན་ཏེ། རྡོ་རྗེ་དྲིལ་བུ་གཉིས་ཀྱི་ཕྱག་རྒྱ་དང་ལྡན་པར་སྦྱར་བའོ། །སློབ་དཔོན་དཀྱིལ་འཁོར་དུ་འཇུག་པ་ན། རེ་ཁཱའི་ནང་དུ་སོང་སྟེ་བལྟས་ནས་མེ་ཏོག་གི་ཕྲེང་བ་དབུལ་ལོ། །འདིར་ནི་དཀྱིལ་འཁོར་བསྒྲུབ་པ་དང་འབྲེལ་བའོ། །འདི་ཡང་སྔོན་དུ་ཤེས་པའི་གོ་རིམས་ཏེ་སློབ་དཔོན་གྱིས་ཇི་ལྟར་བྱས་ནས་འཇུག་ཅེ་ན། ཁྲུས་དང་གཙང་སྦྲ་ནི་ཆུ་དང་ས་ལ་སོགས་པའམ་ཏིང་ངེ་འཛིན་གྱིས་སོ། །

[Block 784]
ཡང་དྲི་ཞིམ་ལུས་ནི་གོས་སར་པའོ། །སྣ་ཚོགས་རྒྱན་ནི་རིན་པོ་ཆེའམ་རུས་པའི་རྒྱན་ནོ། །རྣམ་པར་བརྒྱན་ནི་མགུལ་རྒྱན་ལ་སོགས་པ་རིམ་པར་བཀོད་པའོ། །ཧཱུཾ་ཧཱུཾ་བསྙེམས་པ་ནི་ང་རྒྱལ་ལམ་ལྡང་བ་ལ་སོགས་པ་རྡོ་རྗེ་འགྲོས་ཀྱིས་དུས་བརྗོད་པའོ། །ཧི་ཧི་རྣམ་པར༌[^827]འཇིགས་པ་ནི་ཧ་ཧ་ལ་སོགས་པ་བརྒྱད་དེ་སྟང་སྟབས་ཀྱི་དུས་སུ་བརྗོད་པའོ། །

[Block 785 [HEADING]]
##### བསྲུང་བ། ^1-10-1-6-0

[Block 786]
དེའི་དོན་ནི་དེ་ཡིན་ཏེ་བསྲུང་བ་ནི་རྣམ་པ་དྲུག་སྟེ། རྡོ་རྗེ་བལྟ་བས་བསྲུང་བ་དང་། དེངས་ཤིག་པས་བསྲུང་བ་དང་། བཀའ་བསྒོ་བས་བསྲུང་བ་དང་། རྡོ་རྗེ་འགྲོས་ཀྱིས་བསྲུང་བ་དང་། སྟང་སྟབས་ཀྱིས་བསྲུང་བ་དང་། རྡོ་རྗེ་ཕུར་པས་བསྲུང་བའོ། །

[Block 787 [HEADING]]
###### རྡོ་རྗེ་བལྟ་བས་བསྲུང་བ། ^1-10-1-6-1-0

[Block 788]
དེ་ལ་ལྟ་བས་བསྲུང་བ་ནི། སྔར་གྱི་ས་གཟུང་བའི་སློབ་དཔོན་ལ་གྲོགས་གཽ་རཱི་ལ་སོགས་པ་བཞིའི་ང་རྒྱལ་དང་ལྡན་པ་བཞི་ཡིས་མཆོད་པ་ཅིག་བྱས་ཏེ། དེ་བཞིན་གཤེགས་པ་ཀུན་ཞི་བ། །ཞེས་བྱ་བ་ལ་སོགས་པ་བསྟོད་པ་དང་། གསོལ་བ་བཏབ་པའི་རྗེས་ལ། སྔར་གྱི་དཀྱིལ་འཁོར་ལ་མཆོད་པ་ཅིག༌[^828]བྱས་ཏེ། མ་དང་ཊ་ལས་མིག་ཉི་ཟླར་བསྐྱེད། ཨ་ལས་རྐང་པ་རྡོ་རྗེར་བསྐྱེད་ལ་སྔར་གྱི་དཀྱིལ་འཁོར་ནམ་མཁའ་ལ་བཀོད་དེ་ཧཱུཾ་ཕཊ་ཅེས་བརྗོད་ལ། ཉི་མ་དང་ཟླ་བའི་མིག་གིས་གསད་པ༌[^829]དང་གསོ་བ་བྱའོ། །

[Block 789 [HEADING]]
###### དེངས་ཤིག་པས་བསྲུང་བ། ^1-10-1-6-2-0

[Block 790]
དེ་ནས་དེངས་ཤིག་པས་བསྲུང་བ་ནི་དབང་ལྡན་གྱི་མཚམས་སུ་ཕྱིན་ལ། །བདག་ཉིད་ཁྲོ་བོའི་ང་རྒྱལ་གྱིས་འདི་སྐད་བརྗོད་པར་བྱའོ། །ས་ཕྱོགས་འདིར་སློབ་དཔོན་འདི་ཞེས་བྱ་བ་སློབ་མ་འདི་ཞེས་བྱ་བ་རྫོགས་པའི་བྱང་ཆུབ་ལ་རྫོགས་པར་བྱ་བ་དང་། སེམས་ཅན་ཐམས་ཅད་བླ་ན་མེད་པའི་བྱང་ཆུབ་ཐོབ་པར་བྱ་བའི་ཕྱིར་དཀྱིལ་འཁོར་རྒྱལ་པོ་འདི་ཞེས་བྱ་བ་རྩོམ་གྱིས། །གང་སུ་ཡང་རུང་བས་ས་ཕྱོགས་འདི་ན་གནས་པའི་ལྷ་དང་། ལྷ་མ་ཡིན་དང་། གནོད་སྦྱིན་དང་། སྲིན་པོ་དང་། ཡི་དགས་དང་། ཤ་ཟ་དང་། བརྗེད་བྱེད་དང་། འབྱུང་པོ་དང་། གནོན་པོ་དང་། ནམ་མཁའ་ལྡིང་དང་། མིའམ་ཅི་དང་། རིག༌[^830]འཛིན་ལ་སོགས་པ་རྒན་པོ་དང་རྒན་མོ་དང་འཁོར་དང་གཡོག་ཏུ་བཅས་པ་རྣམས་འདིར་མ་གནས་པར་གཞན་དུ་དེངས་ཤིག །དེ་ལྟར་རྡོ་རྗེ་འཛིན་གྱི་བཀའ་ཐོས་ནས་མྱུར་བ་ཉིད་དུ་དེངས་ཤིག །གང་དག་མི་འགྲོ་བ་དེ་དག་ནི་ཕྱག་ན་རྡོ་རྗེ་རབ་ཏུ་འབར་བ་ཧཱུཾ་ཀ་ར་ཤིན་ཏུ་ཁྲོས་པས་ཡེ་ཤེས་ཀྱི་རྡོ་རྗེ་ཆེན་པོ་ཀུན་ནས་རབ་ཏུ་འབར་བས་མགོ་བོ༌[^831]ཚལ་པ་བརྒྱར་འགས་པར་འགྱུར་ཏ་རེ་ཞེས་ལན་གསུམ་བརྗོད་དོ། །

[Block 791 [HEADING]]
###### བཀའ་བསྒོ་བས་བསྲུང་བ། ^1-10-1-6-3-0

[Block 792]
དེ་ནས་བཀའ་བསྒོ་བའི་བསྲུང་བ་ནི།

[Block 793 [VERSE]]
ང་ནི་དཔལ་ལྡན་རྡོ་རྗེ་འཆང་། །
ཉོན་ཅིག་བར་ཆད་བགེགས་ཀྱི་ཚོགས། །
སྲུང་བའི་འཁོར་ལོའི་སྦྱོར་བ་ཡིས། །
ལུས་ངག་ཡིད་ལ་གནོད་པ་རྣམས། །

[Block 794]
འདིར་ནི་འཇིགས༌[^832]འཇོམས་གཞན་དུ་མིན། །ཞེས་རྡོ་རྗེའི་གནས་སུ་འཁོར་ལོ་དང་རིན་པོ་ཆེ་དང་། པདྨ་དང་རལ་གྲི༌[^833]སྦྱར་ལ་ཚིགས་སུ་བཅད་པ་ལྔ་སྦྱར་གྱིས༌[^834]བསྐྲད་པར་བྱའོ། །

[Block 795 [HEADING]]
###### རྡོ་རྗེ་འགྲོས་ཀྱིས་བསྲུང་བ། ^1-10-1-6-4-0

[Block 796]
རྡོ་རྗེ་འགྲོས་ཀྱིས༌[^835]བསྐྲད་པ་ནི་རྡོ་རྗེ་རྩེ་གཅིག་པ་དང་རྩེ་གསུམ་པ་དང་། སྣ་ཚོགས་རྡོ་རྗེའི་འགྲོས་ཀྱིས་དཀྱིལ་འཁོར་བསྐོར་ཞིང་བསྲུང་བར་བྱའོ། །

[Block 797 [HEADING]]
###### སྟང་སྟབས་ཀྱིས་བསྲུང་བ། ^1-10-1-6-5-0

[Block 798]
སྟང་སྟབས་ཀྱིས༌[^836]བསྲུང་བ་ནི་གཡས་བརྐྱང་དང་ནི་གཡོན་བརྐྱང་དང་། ས་ག་དང་ནི་ཟླུམ་པོ་དང་། །མཉམ་པའི་འདུག་སྟངས་རྣམ་པ་ལྔ། ཤར་ནས་བརྩམས་ཏེ་དབུས་ཀྱི་བར་དུ་བསྡུས་ནས་རྣམ་པ་ལྔ་པོ་བྱ། རྒྱས་པར་འདོད་ན་སྟང་སྟབས་ནི་དྲུག་ཅུ་རྩ་གཅིག་ལ་སོགས་ཏེ་སྒྱུ་འཕྲུལ་དྲ་བའི་ཚུལ་དུ་བྱ།

[Block 799 [HEADING]]
###### རྡོ་རྗེ་ཕུར་པས་བསྲུང་བ། ^1-10-1-6-6-0

[Block 800]
རྡོ་རྗེ་ཕུར་པས་བསྲུང་བ་ནི་ཕུར་བུ་རྣམ་པ་ལྔ། སྟོད་ཁྲོ་བོའི་རྣམ་པ་སྨད་ཕུར་བུ་རྩེ༌[^837]གཅིག་པར་བསྐྱེད་ལ། ཕུར་པའི་སྔགས་བརྒྱ་རྩ་བརྒྱད་བཟླས་ཏེ། །གྷ་གྷ་གྷཱ་ཏའི་སྔགས་ཀྱིས༌[^838]ཕྱོགས་བཞི་དབུས་དང་ལྔར་གདབ་པར་བྱའོ། །

[Block 801 [HEADING]]
#### སྟ་གོན་གྱི་ཆོ་ག། ^1-10-2-0

[Block 802]
སྟ་གོན་གྱི་ཆོ་ག་ནི་འོག་ནས་ཤེས་པར་བྱའོ། །

[Block 803 [HEADING]]
#### ནུབ་གསུམ་པ་ལ་འཇུག་པ། ^1-10-3-0

[Block 804]
དེའི་རྗེས་ལ་ཐིག་བྲི་བའི་ཕྱིར་ཐིག་སྐུད་སར་པ་ནི་གཞན་དུ་ལོངས་མ་སྤྱད་པའོ། །ཚད་ནི་ཉིས༌[^839]འགྱུར་དང་ཉི་ཤུ་ཆའོ། །མཛེས་པ་ནི་དྲི་ཞིམ་པོའི་སྣོད་ཀྱིས་མཛེས་པའོ། །རང་འདོད་ལྷའི་གཟུགས་ཀྱིས༌[^840]ནི་དགྱེས་པའི་རྡོ་རྗེ་དང་གྲོགས་བདག་མེད་མའམ་གཽ་རཱིས་སོ། །ཤེས་རབ་ཅན་གྱིས་གདབ་པ་ནི༌[^841]ལས་དང་བྱ་བ་ལ་མཁས་པས་སའི་ཆ་དབྱེ་བ་ལས་མ་འདས་པའོ། །

[Block 805 [HEADING]]
##### ཐིག་སྒྲུབ་པའི་ཆོ་ག། ^1-10-3-1-0

[Block 806]
དེ་ལ་ཐིག་སྒྲུབ་པའི་ཆོ་ག་ནི་རས་བལ་རིན་ལ་མ་རྩེགས་པར༌[^842]ཉོས་ལ། ཁྱེའུ་དང་བུ་མོ་གཞོན་ནུ་མས་བཀལ་ཏེ། སྲད་བུ༌[^843]ལྔ་ཁ་དོག་སོ་སོར་བསྒྱུར་ནས་སྣོད་གཙང་མའི་ནང་དུ་ཕྱོགས་སོ་སོར་བཞག་སྟེ། བྷྲཱུཾ་ཨཱཾ་ཛྲཱིཾ་ཁཾ་ཧཱུཾ་བཀོད་ལ་དེ་བཞིན་གཤེགས་པ་ལྔར་བསྐྱེད། རང་བཞིན་པ་སྤྱན་དྲངས་ལ་བསྟིམ། ཨ་ནྱོ་ནྱ་ཨ་ནུ་ག་ཏ་ལ་སོགས་པས་བཟླས་ལ་བསྒྲིལ་བར་བྱའོ། །

[Block 807]
དེ་ལ་མཆོད་པ་ལྔས་མཆོད། །ཐིག་སྒྲུབ་པའི་རིམ་པའོ། །དེ་ནས་བདག་ཉིད་གྲོགས༌[^844]དང་བཅས་པས༌[^845]ཡེ་ཤེས་ཀྱི་ཐིག་གདབ་པ་དང་ལས་ཀྱི་ཐིག་གདབ་པར་བྱའོ། །དེས་ཅིར་འགྱུར་ཞེ་ན། འོག་ནས་སྟོན་པས་དཀྱིལ་འཁོར་འདི་སྐད་གསུངས་ཞེས་བྱ་བར་སྦྱར་རོ། །དེའི་རྗེས་ལ་ཚོན་བསྟན་པར་བྱ་བའི་ཕྱིར། རྡུལ་ཚོན་དམ་པའི་ཚོན་དང་ནི་རིན་ཆེན་ལྔའི་ཕྱི་མར་འབྲེལ་ལོ། །ཡང་འབྲིང་པོ་ནི་ཡང་ན་འབྲས་བུ་ལ་སོགས་པར་འབྲེལ་ལོ། །ཐ་མ་ནི་སོ་ཕག་དང་ས་ལ་སོགས་པའི་ཚོན་ཏེ་བརྟག་པ་ཕྱི་མར་ཤེས་པར་བྱའོ། །

[Block 808 [HEADING]]
##### ཚོན་སྒྲུབ་པ། ^1-10-3-2-0

[Block 809]
ཚོན་སྒྲུབ་པ་ནི་ཚོན་རྩི་ཁ་དོག་ལྔ་ཕྱོགས་སོ་སོར་བཞག་ལ་སྔར་གྱི་ཡིག་འབྲུ་ལྔ་ཡིས་དེ་བཞིན་གཤེགས་པ་ལྔར་བསྐྱེད་རང་བཞིན་པ་བསྟིམ། མཆོད་པ་རྣམ་པ་ལྔས་མཆོད། བཛྲ་ས་མ་ཡའི་སྔགས་བཟླས་ལ་ཚོན་རྩི་སྤར་རོ། །གཟི་བསྐྱེད་དེ་དབང་ལྡན་གྱི༌[^846]མཚམས་ནས་ཚིགས་སུ་བཅད་པ་རེ་བརྗོད་ཅིང་མཐོ་གང་ཙམ་དྲང་བར་བྱའོ། །

[Block 810]
དེ་ཡང་།
--- END BLOCKS ---
