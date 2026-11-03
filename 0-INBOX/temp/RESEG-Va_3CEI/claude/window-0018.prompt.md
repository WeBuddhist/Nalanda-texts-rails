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
[Block 631 [HEADING]]
###### དོན་གཞན་ལས་གླེང་སྟེ་ལན་གདབ་པ། ^4-1-10-2-3-0

[Block 632]
མདོ་ལས་རིགས་ཀྱི་བུ་རྣམས་བདག་གིས་དྲན་པ་འདས་པའི་དུས་བསྐལ་བ་གྲངས་མེད་པའི་ཡང་གྲངས་མེད་པ་ཞེས་པ་ནི་རྒྱུ་བརྒྱད་སྦྱར༌[^657]དུམ་བུ་གཉིས་སུ་ཕྱེ་སྟེ། ཚིག་ལྷུག་པ་དང་ཚིགས་སུ་བཅད་པས་བསྡུ་བའོ། །

[Block 633]
སྔར་རྒྱུན་གྱིས༌[^658]ན་དོན་གཞན་ལས་གླེངས་ཏེ་ལན༌[^659]བཏབ། རྒྱུ་གཅིག་གིས་སྔོན་གྱི་ལུགས་ལས་དྲས༌[^660]ཏེ་ལན་བཏབ།

[Block 634 [HEADING]]
###### **ངོ་མཚར་དུ་གྱུར་པ་ལས་བསྟོད་དེ་ལན་བཏབ་པ།** ^4-1-10-2-3-1-0

[Block 635]
དང་པོ་ལ་ཡང་རྣམ་པ་གསུམ་སྟེ། ངོ་མཚར་དུ་གྱུར་པ་ལས་བསྟོད་དེ་ལན་བཏབ་པ་དང་། ཕྱིས་ཁྱད་པར་དུ་གྱུར་པ་ལས་ལན་བཏབ་པ་དང་། ཕྱི་མ་ལྔས་ནི་དོན་མཐུན་པ་ལས་དྲས༌[^661]ཏེ་ལན་བཏབ། ངོ་མཚར་དུ་གྱུར་པ་ལས་བསྟོད་དེ་ལན་བཏབ་པ་ནི་འགྲེལ་པ་ལས་ཡ་མཚན་མངོན་དུ་གྱུར་པའི་རྒྱུ་དང་སྦྱར་རོ། །

[Block 636]
གྲངས་མེད་པའི་ཡང་གྲངས་མེད་པ་ཞེས་པ་ནི་བསྐལ་པའི་དུས་ཡུན་རིང་བས་སྟེ། བསྐལ་པ་གྲངས་མེད་པ་ཞེས་པ་ནི་གྲངས་ཀྱི་མཐའ་ལྔ་བཅུ་རྩ་གཉིས་ལ་གྲངས་མེད་པ་ཞེས་བྱའོ། །

[Block 637]
ཡང་ན་བསྐལ་པ་ཞེས་པ་ནི་ལྷའི་ཚེ་དང་སྦྱར་བའི་བསྐལ་པ་དང་། ལོ་དང་དུས་མི་མཐུན་པའི་བསྐལ་པ་ཞེས་འདིར་བསྐལ་པ་ཞེས་པ་ནི་ལོ་དང་སྦྱར་ཏེ། དེ་བཞིན་གཤེགས་པ་རྣམས་ཀྱི་བསྐལ་པ་ཆེན་པོ་ན༌[^662]བརྒྱ་ལམ་ན་ལན་གཅིག་འབྱུང་བས། འཇམ་དཔལ་གྱིས༌[^663]ཐོས་པའི་དུས་ཧ་ཅང་ཡུན་རིང་བའི་ཕྱིར་རོ། །

[Block 638]
མདོ་ལས་རྒྱང་རིང་བ་དཔག་ཏུ་མེད་པ་བསམ་གྱིས་མི་ཁྱབ་པ་བསྐྱང༌[^664]དུ་མེད་པ། ཚད་མེད་པ་དེའི་ཕ་རོལ་གྱི་ཡང་ཆེས༌[^665]ཕ་རོལ་ཏུ་གྱུར་པ་དེའི་དུས་དེའི་ཚེ་ན་ཞེས་པ་ནས་སངས་རྒྱས་བཅོམ་ལྡན་འདས་འཇིག་རྟེན་དུ་བྱུང་སྟེ་ཞེས་པའི་བར་དུ་ནི་ཉི་ཟླ་སྒྲོན༌[^666]མ་དེ་བཞིན་གཤེགས་པ་ནི་ཉི་མ་ལ་དོན་རྣམ་པ་གཉིས་ཏེ། སྣང་བའི་དོན་དང་སྨིན་པའི་དོན་ཏོ། །

[Block 639]
ཟླ་བ་ལ་དོན་རྣམ་པ་གཉིས་ཏེ། ཐེ་ཙོམ་སེལ་བའི་དོན་དང་བསིལ་བའི་དོན་ཏོ། །

[Block 640]
སྒྲོན་མ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ་མུན་པ་སེལ་བ་དང་། སྣང་བ་མཆེད་པའི་དོན་ནོ། །

[Block 641]
དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ཡོན་ཏན་གྱི་མཚན་རྣམ་པ་བཅུའོ། །

[Block 642]
དེ་བཞིན་གཤེགས་པ་ནི་སྔོན་གྱི་དེ་བཞིན་གཤེགས་པའི་ལུགས་བཞིན་དུ་གཤེགས་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པའོ། །

[Block 643]
ཡང་དེ་བཞིན་གཤེགས་པ་ནི་གང་ནས་ཀྱང་མ་བྱོན། གང་དུ་ཡང་མི་བཞུད་པའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་དེ་ཆོས་ཀྱི་སྐུའོ། །

[Block 644]
ཡང་ན་དེ་བཞིན་ཉིད་ཀྱི་བདེན་པ་ལས་བྱུང་བའི་ཕྱིར་དེ་བཞིན་གཤེགས་པའོ། །

[Block 645]
དགྲ་བཅོམ་པ་ཞེས་པ་ནི་ཉོན་མོངས་པའི་དགྲ་ཐམས་ཅད་བཅོམ་པའི་ཕྱིར་དགྲ་བཅོམ་པའོ། །ཤེས་བྱའི་སྒྲིབ་པ་ཐམས་ཅད་སྤངས་པའི་ཕྱིར་ཡང་དག་པར་རྫོགས་པ༌[^667]སྟེ། རིག༌[^668]པ་དང་ཞབས་སུ་ལྡན་པ་ནི་སྔོན་གྱི་གནས་དྲན་པའི་རིག་པ་དང་འཆི་འཕོ་ཤེས་པ་དང་། ཟག་པ་ཟད་པ་ཤེས་པའི་རིག་པ་ནི་རིག་པའོ། །

[Block 646]
བསྟན་པ་དང་། སྤྱོད་པ་དང་སྨོན་ལམ་རྣམ་པར་དག་པས་འཚོ་བ་དག་པར་གྱུར་པ་ནི་ཞབས་ཏེ། རིག་པ་དང་ཞབས་སུ་ལྡན་པའོ། །

[Block 647]
བདེ་བར་གཤེགས་པ་ནི་བདག་དང་གཞན་ལ་ཕན་འདོགས་པའི་ཡོན་ཏན་ཆེན་པོ་དང་ལྡན་པས་བྱང་ཆུབ་ཆེན་པོར་གཤེགས་པའི་ཕྱིར་བདེ་བར་གཤེགས་པའོ། །

[Block 648]
འཇིག་རྟེན་མཁྱེན་པ་ཞེས་པ་ནི་སྣོད་དང་བཅུད་ཀྱི་འཇིག་རྟེན་མ་ལུས་པར་མཁྱེན་པ་དང༌[^669]ཅི་འདུལ་བ་སོ་སོར་མཁྱེན་པ་དང་། སེམས་ཅན་གྱི་སྤྱོད་པ་བརྒྱད༌[^670]ཁྲི་བཞི་སྟོང་མི་མཐུན་པ་སོ་སོར་མཁྱེན་པ་དང་། སྣོད་ཀྱི་འཇིག་རྟེན་འཇིག་པ་དང་ཆགས་པ༌[^671]མཁྱེན་པ་དང་། སེམས་ཅན་སོ་སོའི་རང་བཞིན་དང་། རྒྱུ་རྐྱེན་ལ་སོགས་པ་ཀུན་མཁྱེན་པའོ། །

[Block 649]
བླ་ན་མེད་པ་སྐྱེས་བུ་འདུལ་བའི་ཁ་ལོ་སྒྱུར་བ༌[^672]ནི་ཟླ་མེད་པའི་ཕྱིར་བླ་ན་མེད་པ༌[^673]སྐྱེས་བུ་ཆེན་པོའི་མཚན་བཟང་པོ་དང་ལྡན་པ་ཕུལ་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 650]
ལྷ་དང་མིའི་མཁན་པོ་ནི་ལྷ་དང་མིས་དོན་ཟབ་མོ་ཆུད་པའི་སྐལ་བ་དང་ལྡན་པས་དེའི་མཁན་པོ་ཞེས་བྱའོ། །

[Block 651]
སྒྲིབ་པ་ཐམས་ཅད་བསལ་ཏེ། ཆོས་ཐམས་ཅད་མངོན་དུ་གྱུར་པ་ནི་སངས་རྒྱས་སོ། །

[Block 652]
བཅོམ་ལྡན་འདས་ཞེས་པ་ནི་བདུད་རྣམ་བཞི་བཅོམ་ལ། དབང་ཕྱུག་ལ་སོགས་པ་ཡོན་ཏན་དྲུག་དང་ལྡན་པའི་ཕྱིར་བཅོམ་ལྡན་འདས་སོ། །

[Block 653]
མདོ་ལས་དེས་ཆོས་ཐམས་ཅད་ཅེས་པ་ནས་ཚངས་པར་སྤྱོད་པ༌[^674]ཡང་དག་པར་སྟོན་པ་ཞེས་པའི༌[^675]བར་དུ་ནི་ཆོས་ཁྱད་པར་ཅན་དུ་བསྟན་པའི་ཕྱིར་ཏེ། ཐོག་མར་དགེ་བ་ནི་ཐོས་པ་ཙམ་གྱིས་དགའ་བའོ། །

[Block 654]
བར་དུ་དགེ་བ་ནི་སྒོམ་པ་ལ་བར་ཆད་མེད་ཅིང་མཐའ་གཉིས་སྤངས་པའི་སྤྱོད་ཡུལ་དྲི་མ་དང་བྲལ་བས་འཇུག་པའོ། །

[Block 655]
ཐ་མར་དགེ་བ་ནི་སྤྱོད་པ་དང་སྒྲུབ་པའི་མཐར་ཕྱིན་པའི་འབྲས་བུ་ལ་གནས་པའོ། །

[Block 656]
ཡང་ན་ཐོག་མར་དགེ་བ་ནི་སྦྱིན་པ། བར་དུ་དགེ་བ་ནི་ཚུལ་ཁྲིམས། ཐ་མར་དགེ་བ་ནི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 657]
ཡང་ན་སྡུག་བསྔལ་ཤེས་པ་དང་ཀུན་འབྱུང་སྤངས་པ་ནི་ཐོག་མར་དགེ་བ། ཡང་དག་པའི་ལམ་བསྒོམ་པ་ནི་བར་དུ་དགེ་བ། འགོག་པ་མངོན་དུ་གྱུར་པ་ནི་ཐ་མར་དགེ་བ་སྟེ། ཉན་ཐོས་པ་དང་སྦྱར་རོ། །

[Block 658]
བྱང་ཆུབ་ནི་སེམས་མི་གཏོང་བ་དང་། ཐེག་པ་གཉིས་པར་མི་བསྔོ་བར་བླ་ན་མེད་པའི་ཡེ་ཤེས་ཐོབ་པ་ནི་བྱང་ཆུབ་སེམས་དཔའི་ཐོག་མ་དང་བར་མ་དང་ཐ་མར་དགེ་བའོ། །

[Block 659]
འཕགས་པའི་ལམ་ཡན་ལག་བརྒྱད་ཡང་དག་པའི་ངག་ལ་སོགས་པས་ཚིག་སྦྱར་ལེགས་ཤིང་དོན་ཟབ་མོ་དང་ལྡན་པས་མང་པོ་ལ་ཕན་པར་འགྱུར་བ། མུ་སྟེགས་ཀྱི་ལམ་དང་མ་འདྲེས་པ། དོན་དང་ཚིག་ཚང་བ་ཁྱད་པར་དུ་འཕགས་པ་ནི་དོན་བཟང་བ་ཚིག་འབྲུ་བཟང་བ་མ་འདྲེས་པ། ཡོངས་སུ་རྫོགས་པ་ཞེས་བྱའོ། །

[Block 660]
ཡོངས་སུ་དཀར་བ༌[^676]ནི་རྣམ་པར་གྲོལ་བར་འགྱུར་བའོ། །

[Block 661]
ཚངས་པར་སྤྱོད་པ་ནི་འཕགས་པའི་ཡན་ལག་བརྒྱད་དང་འགོག་པའི་བདེན་པ་དང་། ཚངས་པར་སྤྱོད་པ་སྟེ། ལམ་དེ་གཞན་དང་མ་འདྲེས་པའི་ཕྱིར་མ་འདྲེས་པའོ། །

[Block 662]
མདོ་ལས་འདི་ལྟར་ཉན་ཐོས་རྣམས་ལ་ཞེས་པ་ནས་ཡེ་ཤེས་ཀྱི་མཐའི་བར་དུ་ཆོས་སྟོན་ཏོ་ཞེས་པའི་བར་དུ་ནི་འགྲོ་བ་ལ་ཕན་གདགས་པའི་ཕྱིར་ཆོས་སྟོན་པ་སྟེ། དེ་བཞིན་གཤེགས་པ་འཇིག་རྟེན་དུ་བྱུང་ནས་ཐེག་པ་རྣམ་པ་གསུམ་གྱིས༌[^677]ཆོས་སྟོན་པ་ནི་ཉན་ཐོས་པ་རྣམས་ལ་བདེན་པ་བཞི་བསྟན།[^678] རང་སངས་རྒྱས་ལ་རྟེན་ཅིང་འབྲེལ་པར༌[^679]འབྱུང་བ་བཅུ་གཉིས་བསྟན། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ལ་ཕ་རོལ་ཏུ་ཕྱིན་པ་དྲུག་སྟོན་པ་ཡང་དབང་པོའི་རིམ་པ་བཞིན་དུ་གྱུར་ཏོ། །

[Block 663 [HEADING]]
###### **ཕྱིས་ཁྱད་པར་དུ་གྱུར་པ་ལས་ལན་བཏབ་པ།** ^4-1-10-2-3-2-0

[Block 664]
མདོ་ལས་ཡང་རིགས་ཀྱི་བུ་ཉི༌[^680]ཟླ་སྒྲོན་མ་ཞེས་པ་ནས་འདི་ལྟ་བར་དྭ༌[^681]ཛའི་རིགས་སུ་མཐུན་པ་ཡང་དེ་བཞིན་གཤེགས་པ་སྟོང་ཕྲག་ཉི་ཤུ་བྱུང་ཞེས་པའི་བར་དུ་ནི་ཕྱིར་འབྱུང་བ་ཁྱད་པར་ཅན་ལས་དཔགས་ཏེ་ལན་བཏབ་པའོ། །

[Block 665]
འགྲེལ་པ་ལས་རྒྱུ་ཁྱད་པར་ཅན་མངོན་དུ་མཐོང་བའི་རྒྱུ་སྟེ། རིགས་དམ་པ་དང་མིང་དམ་པ་དང་ལྡན་པར་བསྟན་པའི་གཏན་ཚིགས་སྨོས་པའོ། །

[Block 666 [HEADING]]
###### **དོན་མཐུན་པ་ལས་དྲས་ཏེ་ལན་བཏབ་པ།** ^4-1-10-2-3-3-0

[Block 667]
མདོ་ལས་དེ་ལ་མ་ཕམ་པ་དེ་བཞིན་གཤེགས་པ་སྟོང་ཕྲག་ཉི་ཤུ་པོ་དེ་དག་ཅེས་པ་ནས་ཁབ་ན་གནས་ཤིང་རབ་ཏུ་མ་བྱུང་བའི་ཚེ་སྲས་བརྒྱད་ཡོད་དོ་ཞེས་པའི་བར་དུ་ནི་དོན་མཐུན་པ༌[^682]ལས་དྲིས་ཏེ་ལན་བཏབ་པའོ། །

[Block 668]
ཡང་རྒྱུ་རྣམ་པ་ལྔ་སྟེ་ལོངས་སྤྱོད་ཆེ་བའི་རྒྱུ་དང་། དེ་བཞིན་གཤེགས་པ་རྣམས་ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བའི་རྒྱུ་དང་། དེ་བཞིན་གཤེགས་པ་ཤིན་ཏུ་བསྟན་པའི་ཆོས་ཀྱི་འཁོར་ལོའི་རྒྱུ་དང་། འཇུག་པར་འགྱུར་བའི་རྒྱུ་དང་དྲན་པའི་རྒྱུའོ། །

[Block 669]
དེ་ལ་ཡང་རྣམ་པ་གཉིས་ཏེ། རྒྱུ་དང་པོ་ནི་བཅོམ་ལྡན་འདས་ཆོས་སྟོན་པའོ། །

[Block 670]
རྒྱུ་ཕྱི་མ་ནི་མྱ་ངན་ལས་འདས་པའི་སྤྱོད་པའོ། །
--- END BLOCKS ---
