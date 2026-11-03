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

[Block 671]
ལོངས་སྤྱོད་པའི་རྒྱུ་ཆེན་པོ་ནི་འགྲེལ་པ་ལས་སྔོན་བཅོམ་ལྡན་འདས་རྒྱལ་བུ་མཛད་པ་ནས་ལོངས་སྤྱོད་ཆེན་པོ་སྤངས་ཏེ། ཁབ་ནས་བྱུང་བར་མཛད་ན་འགྲོ་བ་མ་རབས་རྣམས་ཀྱིས༌[^683]ཡུན་ད་སྲིད་དུ་སྐྱོ་བའི་སེམས་མི་སྐྱེད་པ་དེ་ངོ་མཚར་དུ་བསྟན་པའོ། །

[Block 672]
ལོངས་སྤྱོད་ཀྱང་རྣམ་པ་གཉིས་ཏེ། ཁྱིམ་ན་གནས་ཤིང་སྡོད་པས༌[^684]ལོངས་སྤྱོད་པ་དང་། ཁྱིམ་ནས་བྱུང་ནས་ཆོས་ལ་ལོངས་སྤྱོད་པའོ། །

[Block 673]
བཅོམ་ལྡན་འདས་ཁབ་ནས་མ་བྱུང་བའི་ཚེ་སེམས་ཅན་བསྒྲལ་བའི་ཆེད་དུ་འདོད་པ་ལ༌[^685]ལོངས་སྤྱོད་པ་དང་སྲས་མངའ་བར་ཡང་བསྟན་ཏོ། །

[Block 674]
མདོ་ལས་འདི་ལྟ་སྟེ་བློ་གྲོས་ཞེས་བྱ་བ་ནས་ཆོས་ཀྱི་བློ་གྲོས་ཀྱི་བར་དུ་གཞོན་ནུ་དེ་དག་ནི་ཤེས་རབ་ཆེ་བ་དང་། ཐུགས་རྗེ་ཆེ་བ་དང་། ཡོད་པ་དང་མེད་པ་ལ་མཁས་པ་དང་། དགེ་བ་ལ་འཇུག་ཅིང་སྡིག་པ་སྤོང་བ་ལས་མཚན་དུ་བཏགས་པ་ཤེ་དག༌[^686]གོ། །

[Block 675]
མདོ་ལས་མ་ཕམ་པ་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་ལོངས་སྤྱོད་ཅིང་དེ་དག་རྒྱལ་པོ་བྱེད་དོ་ཞེས་པའི་བར་དུ་ནི་གོ་སླ་བས་མ་བཤད་དོ། །

[Block 676]
མདོ་ལས་དེ་དག་གིས་བཅོམ་ལྡན་འདས་དེ་ཁབ་ནས་མངོན་པར་འབྱུང་བར་ཤེས་ཤིང་ཞེས་པ་ནས་དགེ་བའི་རྩ་བ་བསྐྱེད་པར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་རབ་ཏུ་བྱུང་བ་བསྟན་ཏེ། རྟེན་དམ་པ་དང་འགྲོགས་པ་དང་ཉོན་མོངས་པ་ལས་འབྱུང་བར་རྩོལ་བ་རྒྱུ་དམ་པ་ལ་སྦྱོར་ཞིང་བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་བསྒྲུབ༌[^687]པའོ། །

[Block 677]
མདོ་ལས་མ་ཕམ་པ་དེའི་ཚེ་ན་ཡང༌[^688]ཞེས་པ་ནས་སངས་རྒྱས་ཐམས་ཅད་ཀྱིས༌[^689]ཡོངས་སུ་ཟིན་པ་བཤད་ནས༌[^690]ཞེས་པའི་བར་དུ་ནི་དུས་མཐུན་པར་གྲུབ་པ༌[^691]བསྟན་ཏོ། །

[Block 678]
དེའི་ཚེ་སྐད་ཅིག་ཡུད་ཙམ་ཐང་ཅིག་ཅེས་པ་ནས་སེམས་མི་གཡོའོ་ཞེས་པའི་བར་དུ་ནི་སྤྱོད་ལམ་མཐུན་པ་བསྟན་ཏ། ཏིང་ངེ་འཛིན་དུ་ཞུགས་པ་དང་སྣོད་ཀྱི་འཇིག་རྟེན་དང་བཅུད་ཀྱི་འཇིག་རྟེན་ཏེ་འདི་དང་པོའོ། །

[Block 679]
མདོ་ལས་མེ་ཏོག་མན་དཱ་ར་བ་ནས་རབ་ཏུ་འཁྲུག་པའི་བར་གྱིས་ནི་སྣོད་ཀྱི་འཇིག་རྟེན་བསྟན་ཏོ།[^692] །མ་ཕམ་པ་དེའི་ཚེ་འཁོར་དེར་ཞེས་པ་ནས་རྨད་དུ་དགའ་བར་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་འདིས༌[^693]ནི་བཅུད་ཀྱི་འཇིག་རྟེན་བསྟན་ཏོ། །

[Block 680]
མདོ་ལས་དེ་ནས་དེའི་ཚེ་བཅོམ་ལྡན་འདས་ཞེས་པ་ནས་ཤིན་ཏུ་ཁྱབ་པར་སྣང་བའི་བར་དུ་ནི་སྟོན་པ་མཐུན་པའི་རྒྱུ་སྟེ་འོད་གཏོང༌[^694]པ་དང་སྣང་བར་བྱ་བ་དང་སྲུང་བར་བྱེད་པ་བསྟན་ཏོ། །

[Block 681]
མདོ་ལས་མ་ཕམ་པ་འདི་ལྟ་སྟེ་ཞེས་པ་ནས་ངོ་མཚར་དུ་གྱུར་རྨད་དུ་གྱུར། ལྟད་མོ་རབ་ཏུ་བྱུང་ངོ་ཞེས་པའི་བར་དུ་ནི་དེ་ཡང་ཆོས་ཐོས་པར་དགའ་བ་དང་། སྔོན་གྱི་རྒྱུ་བསྟན་པར་འདོད་པའོ། །

[Block 682]
གཞན་ནི་གོ་སླ་བས་མ་བཤད་དོ། །

[Block 683]
མདོ་ལས་མ་ཕམ་པ་དེའི་ཚེ་ན་ཡང་བཅོམ་ལྡན་འདས་དེའི་བསྟན་པ་ལ་འོད་མཆོག་ཅེས་བྱ་བའི་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་པ་ནས་བརྒྱད་བརྒྱ་ཡོད་དོ་ཞེས་པའི་བར་དུ་ནི་དེ་དང་མཐུན་པས་ལན་བཏབ་པ་སྟེ། སྣང་བར་བྱེད་པའི་འཁོར་མདོ་འདི་ལས་གླེང་བ་དང་ཡུན་རིང་བ་དང་འཁོར༌[^695]སྐྱིད་པ་སྟེ་འདི་ནི་དང་པོའོ། །

[Block 684]
མདོ་ལས་བཅོམ་ལྡན་འདས་དེ་ཡང་ཞེས་པ་ནས་ལུས་སྐྱོ་བ་ཡང་མེད་སེམས་སྐྱོ་བ་ཡང་མེད་ཅེས་པའི་བར་དུ་འདི་དག་ནི་མདོ་འདི་གླེང་བ་དང་དུས་རིང་ཐུང་དང་འཁོར་བཞི་དགའ་ཞིང་མོས་པ་གོ་རིམས་བཞིན་དུ་སྦྱར་ཏེ། གཞན་ནི་གོ་སླ་བས་མ་བཤད་དོ། །

[Block 685]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཉི་ཟླ་སྒྲོན་མ་ཞེས་པ་ནས་མྱ་ངན་ལས་འདས་སོ་ཞེས་པའི་བར་དུ་ནི་ལྟས་ཀྱི་ལུགས་མཐུན་པ་བསྟན་པ་སྟེ། སངས་རྒྱས་མྱ་ངན་ལས་འདས་པ་ནི་ཐེག་པ་རྣམ་པ་གཉིས་ལས་ཁྱད་པར་དུ་བསྟན་པའི་ཕྱིར་ལྷག་མ་མ་ལུས་པའི་མྱ་ངན་ལས་འདས་པའོ། །

[Block 686]
མདོ་ལས་དེ་ནས་མ་ཕམ་པ་ཞེས་པ་ནས་ལུང་བསྟན་ནས་ཞེས་པའི་བར་ནི་དགེ་བའི་རྩ་བ་སྨིན་པའི་ཕྱིར་ལུང་བསྟན་པ་ཡིན་ནོ། །

[Block 687]
མདོ་ལས་དགེ་སློང་རྣམས་དཔལ་གྱི་སྙིང་པོ་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་པ་ནས་སངས་རྒྱས་སུ་གྱུར་ཏོ་ཞེས་པའི་བར་དུ་ནི་ཡང༌[^696]སངས་རྒྱས་འཇིག་རྟེན་དུ་བྱུང་བ་དོན་རྣམ༌[^697]པ་ལྔའི་ཕྱིར་ཏེ། ཆོས་ཀྱི་འཁོར་ལོ་བསྐོར་བ་དང་ཕ་མ་བྱང་ཆུབ་ལ་དགོད་པ་དང་། མ་དད་པ་རྣམས་དད་པར་བྱ་བ་དང་བྱང་ཆུབ་ཏུ༌[^698]སེམས༌[^699]མ་བསྐྱེད་པ་རྣམས་སེམས་བསྐྱེད་པ་དང་། ལུང་མ་བསྟན་པ་རྣམས་ལུང་བསྟན་པའོ། །

[Block 688]
མདོ་ལས་དགེ་སློང་རྣམས་དཔལ་གྱི་སྙིང་པོ་ཞེས་པ་ནས་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་སུ་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པ་ཤིན་ཏུ་བསྟན་པས་ཆོས་འཛིན་པའི་རྒྱུའོ། །

[Block 689]
འགྲེལ་པ་ལས་བཅོམ་ལྡན་འདས་དེ་མྱ་ངན་ལས་འདས་ནས་བསྐལ་པ་གྲངས་མེད་པའི་འོག་ཏུ་དེ་བཞིན་གཤེགས་པས༌[^700]ཤིན་ཏུ་བསྟན་པའི་ཆོས་འཛིན་པར་འགྱུར་རོ། །

[Block 690]
མདོ་ལས་དེ་ལ་མ་ཕམ་པ་དེའི་སྲས་བློ་གྲོས་ལ་སོགས་པ་ཞེས་པ་ནས་མངོན་པར་སངས་རྒྱས་ནས༌[^701]ཞེས་པའི་བར་དུ་ནི་འཇུག་པར་ནུས་པའི་རྒྱུ་བསྟན་ཏེ། མཆོད་པ་དང་རིམ་གྲོ་ནི་ཆོས་དང་ཟང་ཟིང་གི་སྤྱོད་པས་སོ། །

[Block 691]
མདོ་ལས་དེ་དག་གི་ཐ་མ་མར་མེ་མཛད་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་ཡིན་ནོ༌[^702]ཞེས་པ་ནས་རིམ་གྲོར་བྱས་སོ་ཞེས་པའི་བར་དུ་ནི་དྲན་པའི་རྒྱུ་དང་བསྟན་པའི་རྒྱུ་དང་དག་པའི་རྒྱུ་བསྟན་ཏོ། །

[Block 692 [HEADING]]
###### སྔོན་གྱི་ལུགས་དང་སྦྱར་ཏེ་ལན་གདབ་པ། ^4-1-10-2-4-0

[Block 693]
མདོ་ལས་མ་ཕམ་པ་ཁྱོད་དེའི་དུས་ན་ཞེས་པ་ནས་ཆོས་སྨྲས་པ༌[^703]ཡིན་ནོ་ཞེས་པའི་བར་དུ་མཐུན་པའི་དོན་གྱིས་ལན་བཏབ་པ་དང་། སྔོན་གྱི་ལུགས་ལས་ལན་བཏབ་པ་སྟེ་འདི་ནི་ངའི་ཡིན་ནོ་ཞེས་པ་ནི་གཏན་ཚིགས་ཀྱི་རྒྱུ་སྨྲས་སོ། །

[Block 694]
མདོ་ལས་གང་ཡང་གྲགས་འདོད་བྱང་ཆུབ་སེམས་དཔའ་ཞེས་པ་ནས་སྙམ་བྱེད་དོ་ཞེས་པའི་བར་དུ་ནི་སྤྱིར་བསྡུས་ཏེ་ལན་བཏབ་པའོ། །

[Block 695 [HEADING]]
###### ཚིགས་སུ་བཅད་པས་བསྡུ་བ། ^4-1-10-2-5-0

[Block 696]
མདོ་ལས་དེ་ནས་འཇམ་དཔལ་ཞེས་པ་ནས་མཐའ་ཡས་བྱེ་བ་སྟོང་རྣམས་ཤེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་སུ་བཅད་པ་བཞི་བཅུ་རྩ་གསུམ་གྱི་དོན་སྔ་མ་རྣམས་བཟླས་ཏེ་སྔ་མའི་ལུགས་ཀྱི་ལྟས་བསྟན་ཏོ། །

[Block 697 [HEADING]]
###### **ལོངས་སྤྱོད་ཀྱི་རྒྱུ་ཆེ་བ།** ^4-1-10-2-5-1-0

[Block 698]
མདོ་ལས་དེའི་ཚེ་རྒྱལ་པོ་དེའི་སྲས་སུ་གྱུར་པ་དེའི༌[^704]ཞེས་པ་ནས་ཐམས་ཅད་རབ་ཏུ་བྱུང་ངོ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་ཚིགས་བཅད་སུམ་ཅུ་རྩ་བརྒྱད་ཀྱིས༌[^705]དོན་མཐུན་པའི་ལུགས་བསྟན་ཏེ། རྒྱུ་ལྔ་པ་དང་སྦྱར་རོ། །

[Block 699]
ཚིགས་སུ་བཅད་པ་ཉི་ཤུ་རྩ་དགུས་ནི་ལོངས་སྤྱོད་ཀྱི་རྒྱུ་ཆེ་བ་བསྟན། ཚིགས་སུ་བཅད་པ་དགུས་ནི་རྒྱུ་བཞི་པོ་བསྟན།

[Block 700]
དང་པོ་ལའང་རྣམ་པ་བཞི་སྟེ། དང་པོའི་ཚིགས་སུ་བཅད་པ་ཉི་ཤུས་ནི་ལྟས་མཐུན་པ་བསྟན། དེའི་འོག་མ་ཚིགས་སུ་བཅད་པ་བཞིས་ནི་མྱ་ངན་ལས་འདས་པ་མི་མཐུན་པ་བསྟན། ཡང་ཕྱེད་དང་གསུམ་གྱིས་ནི་ལུང་བསྟན་པ་བསྟན། ཚིགས་སུ་བཅད་པ༌[^706]གཉིས་ཀྱིས་ནི་མྱ་ངན་ལས་འདས་པ༌[^707]བསྟན་ཏོ། །

[Block 701]
དང་པོ་ལའང་རྣམ་པ་དྲུག་སྟེ་འཁོར་ཕུན་སུམ་ཚོགས་པ་དང་དུས་ཕུན་སུམ་ཚོགས་པ་དང་། སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པ་དང་། རྒྱུ་ཕུན་སུམ་ཚོགས་པ་དང་། ཐོས་པ་ཕུན་སུམ་ཚོགས་པ་དང་། ལམ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 702]
ཚིགས་བཅད་དང་པོ་གཉིས་ཀྱིས་ནི་ཁྱིམ་ན་གནས་པ་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས་ནི་རབ་ཏུ་བྱུང་བ་བསྟན་ཏོ། །

[Block 703]
མདོ་ལས།

[Block 704]
འཇིག་རྟེན་མགོན་པོ་དེ་ཡིས༌[^708]ཆོས་བཤད་པ། །ཞེས་པ་ནས། །སྲོག་ཆགས་སྟོང་ཕྲག་བྱེ་བ་དག་ལས༌[^709]བཤད། །ཅེས་པའི་བར་དུ་ནི་དུས་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏོ། །

[Block 705]
མདོ་ལས་རྣམ་པར་འདྲེན་པ་ཞེས་པ་ནས་བཞུགས་ནས་བསམ་གཏན་མཛད་ཅེས་པའི་བར་དུ་ནི༌[^710]སྤྱོད་ལམ་ཕུན་སུམ་ཚོགས་པ་བསྟན་ཏེ། དེ་ལ༌[^711]ཚིགས་བཅད་གཅིག་གིས་ནི་བསམ་གཏན་ལ་འཇུག་པ་བསྟན། དེའི་འོག་མ་གཉིས་ཀྱིས་ནི་སྣོད་དང་བཅུད་ཀྱི་འཇིག་རྟེན་བསྟན་ཏོ། །
--- END BLOCKS ---
