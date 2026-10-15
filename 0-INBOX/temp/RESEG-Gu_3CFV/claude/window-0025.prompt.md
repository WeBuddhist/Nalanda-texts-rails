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
[Block 876]
གོས་སྤུ་ཅན་དང་ལྷན་པ་ཅན་དག་ཤིང་གིས་བརྡུང་བ་དང་འཁྲུ་བར་བྱེད་ན་སྲོག་ཆགས་ཇི་སྙེད༌[^529]འཆི་བ་དེ་ཉིད་ཀྱི་ལྟུང་བྱེད་དུ་འགྱུར་ལ་མ༌[^530]འཆི་ན་ནི་ཉེས་བྱས་སོ། །

[Block 877]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གོས་སྤུ་ཅན་དང་ལྷན་པ་ཅན་དག་ཤིང་གིས་བརྡུངས་པ༌[^531]དང་བཀྲུ་བར་མི་བྱ་སྟེ་འཁྲུ་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ། །

[Block 878]
འོན་ཀྱང་རིམ་པ་གཅིག་པ་ནི་བཀྲུ་བར་བྱའོ། །

[Block 879]
དགེ་སློང་དག་གིས་བཀྲུ་བ་གཏན་བཏང་བ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གང་ན་སྲོག་ཆགས་ཀྱི་ཁམས༌[^532]མང་ལ་ཆུའི་ཁམས་ཉུང་བ་དེར་བཀྲུ་བར་མི་བྱའི་གང་ན་ཆུའི་ཁམས་མང་ལ་སྲོག་ཆགས་ཀྱི་ཁམས་ཉུང་བ་དེར་བཀྲུ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 880]
འདི་ནི་ཉེ་བར་ལོངས་མི༌[^533]སྤྱད་པ་མ་ཡིན་ནོ། །

[Block 881]
དེ་བས་ན་འདིར་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ནི་ལྟུང་བྱེད་དུ་འགྱུར་རོ་ཞེས་བྱ་བར་དགོངས་པར་རིག་པར་བྱའོ། །

[Block 882]
སྲོག་ཆགས་དང་བཅས་པའི་ཆུ་ལ་ལོངས་སྤྱོད་པའི་རྣམ་པར་འབྱེད་པའོ།། །།

[Block 883]
དཔྱང་ཚགས༌[^534]བཅབ་པར༌[^535]བྱའོ་ཞེས་བྱ་བ་ལ། དཔྱང་ཚགས༌[^536]ཞེས་བྱ་བ་འདི་ཡང་ཅི་ཞིག་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བཟེད་སྣོད་ཀྱི་སྟེང་གི་ནམ་མཁའ་ལ་གཞག་པར་བྱ་ཞིང་དགང་བ༌[^537]དང་བཙག་པར་བྱ་བའི་ཆུ་བཟེད་པར་བྱེད་པ་ཚགས་གདགས་པར་བྱ་བའི་ལྕགས་དག་བཏབ་པའི་ཤིང་བུ་གསུམ་དང་ལྡན་པ་ནི་དེ་ཞེས་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཆུ་ཟེད་པར༌[^538]བྱེད་པའི་ཚགས་གདགས་པར་བྱ་བའི་འོག་ཏུ་བུམ་པ་ལ་སོགས་པའི་སྣོད་གཞག་པར་བྱ་བ་གང་ཡིན་པའི་བཟེད་སྣོད་ཀྱི་སྟེང་གི་ནམ་མཁའ་ལ་གཞག་པར་བྱ་ཞིང་དགང་བ་དང་ཆུ་བཟེད་པར་བྱེད་པའི་ཚགས་གདགས་པར་བྱ་སྟེ། དེ་དབྱུང་བར་བྱ་བའི་དོན་དུ་གོང་དུ༌[^539]ལྕགས་གཟེར་དག་བཏབ་པ་དེ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 884]
འདིར་གཞུང་ནི་དཔྱང་ཚགས༌[^540]བྱ་ཞིང་དེའི་ཡ་ཐོག་ཏུ་ལྕགས་གཟེར་དག་གདབ་པར་བྱའོ། །

[Block 885]
དེ་ལ་ཆུ་ཚགས་གདགས་པར་བྱ་ཞིང་དེའི་འོག་ཏུ་བུམ་པ་གཞག་པར་བྱའོ། །

[Block 886]
ཆུ་སྣོད་ཀྱི་བུམ་པ་དག་དགང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 887]
གང་ཞིག་འདིར་ཆུ་སྣོད་ཀྱི་བུམ་པ་དགང་བར་བྱའོ་ཞེས་གསུངས་པའི་དོན་ནི་ཆུ་སྣོད་ཀྱི་ཆུས༌[^541]བུམ་པ་གང་བར་བྱ་ཞེས་གསུངས་པས་ཟེད༌[^542]སྣོད་དང་འདི་ལ་སོགས་པ་བྱེད་པས་ཞེས་བྱ་བ་དོན་གྱིས་རིག་པར་བྱའོ། །

[Block 888]
ཆུ་གནས་པར་བྱ་བའི་ཕྱིར་ཆུ་ཚགས་སུ་གཅལ་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཆུ་གནས་པར་བྱ་བའི་ཕྱིར་ཆུ༌[^543]ཚགས་དེའི་ནང་དུ་གཅལ་གཞུག་པར་བྱའོ། །

[Block 889]
གཅལ་ཅི་ཞིག་གཞུག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཕྱེ་མའམ་ལྕི་བའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 890]
ཡང་ན་ཚགས་རྟེན་སྣོད་དོ་ཞེས་བྱ་བ་ནི་ཆུ་གནས་པར་བྱ་བའི་ཕྱིར་ཆུ་ཚགས་ལ་ཡང་ན་ཚགས་རྟེན་སྣོད་གཞུག་གོ། །

[Block 891]
དེ་ཅི་འདྲ་བ་ཅིག༌[^544]ཅེ་ན་དེའི་ཕྱིར་ས་དང་ཟངས་མ་ལས་བྱས་པ་གང་ཡང་རུང་བའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ས་ལས་བྱས་པ་ཡང་རུང་ཟངས་མ་ལས་བྱས་པ་ཡང་རུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 892]
དེ་ནི་ཤིང་བུ་གསུམ་གྱི༌[^545]ཐོག་མ་ལ་གདགས་སོ་ཞེས་བྱ་བ་སྟེ་ཇི་ལྟར་ཞེ་ན། དེའི་ཕྱིར་བུ་གུར་ལུང་བྱས་ཏེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་བུ་ག་ཕུག་ནས་དོན་བསྒྲུབ་པ་ལ་ལྟོས་ནས་བུ་ག་དུ་མ་ཡང་བྱའོ་ཞེས་བྱ་བ་འདིས་ཁས་བླངས་པར་རིག་པར་བྱའོ། །

[Block 893]
ཕྱི་རོལ་གྱི་ངོས་སུ་ཚགས་རྟེན་སྣོད་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བཅིང་བ༌[^546]གང་དང་གང་མེད་པས་འདི་ལ་གནས་པ་མེད་ན་དེ་འདི་ལ་བྱའོ། །

[Block 894]
དེ་ཡང་སྐྱེས་པ་ལ་དགོངས་ནས་སྨོས་པ་ཡིན་ནོ།[^547] །དེ་ལྟར་དེ་ཅི་ཞིག་གིས་གདགས་ཤེ་ན། དེའི་ཕྱིར་སྔ་མ་ནི་ཐ་གུས་སོ། །

[Block 895]
ཕྱི་མ་ནི་ལྕགས་ཐག་འཇམ་པོས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྔ་མ་ས་ལས་བྱས་པ་ནི་ཐ་གུས་གདགས་སོ། །

[Block 896]
ཕྱི་མ་ཟངས་ཀྱིས་བྱས་པ་ནི་ལྕགས་ཐག་འཇམ་པོས་གདགས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 897]
དེ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི་བཅང་བར་བྱ་བའི་སྣོད་དོ། །

[Block 898]
འདིར་དེ་ཡན་ལག་ཉིད་ལྕགས་ཐག་དང་ཐ་གུ་བསྟན་ནོ། །

[Block 899]
དེ་བས་ན་འདི་དག་ལ་ཡང་འདིར་འཆང་བ་བསྟན་པར་རིག་པར་བྱའོ། །

[Block 900]
ཆུ་མི་འཛག་ན་ཤིང་ལེབ་ཀྱིས་ཆུ་ཚགས་ལ་དལ་བུ་དལ་བུས་གདབ་པར་བྱའོ། །

[Block 901]
བུམ་ཚགས་གཅེའུ་ཅན་ནི་ཚེགས་ཆུང་ངུ་ཞེས་བྱ་བ་ནི་དཔྱང་ཚགས༌[^548]ཡོད་ཀྱང་ཚེགས་ཆུང་ཞིང་སླ་བ་ཡིན་པས་དེ་ལ་འདོད་པ་བསྐྱེད་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 902]
བུམ་ཚགས་གཅེའུ་ཅན་ནི་དེ་ནས་དགའ་བར༌[^549]བྱ་བར་རིག་པར་ཞེས་བྱ་བས༌[^550]བསྟན་ཟིན་ཏོ། །

[Block 903]
བཅང་བ་ནི་རིགས་སམ་མི་རིགས་ཞེས་བྱ་བས་མ་བསྟན་ཏོ། །

[Block 904]
དེ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་དེ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་སྨོས་སོ། །དེ་ཅི་ལས་བྱས་པ་ཞེ་ན། དེའི་ཕྱིར་ས་འམ་ཟངས་ལས་བྱས་པའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 905]
དེའི་དབྱིབས་ཅི་འདྲ་ཞེ་ན། དེའི་ཕྱིར་དེ་ནི་བུམ་པའི་དབྱིབས་དང་ནང་པདྨའི་སྤུ་གུ༌[^551]ལྟ་བུ་དང་ལྡན་པས་འོག་སྦུབས་ཅན་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་རྣམས་ཀྱི་འོག་ཏུ༌[^552]རྩའི་སྦུབས་ཡོད་པས་ན་འོག་སྦུབས་ཅན་ནོ། །

[Block 906]
ནང་པདྨའི་སྦུ་གུ༌[^553]ལྟ་བུ་དང་ལྡན་པ་ཞེས་བྱ་སྟེ། པདྨའི་སྙིང་པོའི་ནང་ན་གནས་པའི་སྦུ་གུ༌[^554]དག་ལྟ་བུ་ནང་གི་སྦུ་གུ༌[^555]འོག་སྦུབས་ཅན་གང་ལ་ཡོད་པ་དེ་ནི་འོག་སྦུབས་ཅན་པདྨ་ལྟ་བུ་ནང་གི་བུ་ག་ལྟ་བུའོ། །

[Block 907]
པདྨའི་ལྟེ་བ་མེད་པར་པདྨ་ལྟ་བུ་ཉིད་འགྲུབ་པ་མ་ཡིན་ཏེ། དེ་བས་ན་འདི་ལ་ཚིག་འདིས༌[^556]ཀུན་ནས་ཐོབ་པར་རིག་པར་བྱའོ། །

[Block 908]
འདིར་གཞུང་ནི་བུམ་པའི་དབྱིབས་ལྟ་བུར་བྱ་ཞིང་དེའི་ནང་དུ་པདྨའི་རྣམ་པ་ལྟ་བུའི་བུ་ག་དག་གདོད༌[^557]པར་བྱའོ། །

[Block 909]
དེ་དག་བསྡུ་བའི་ཕྱིར་དེ་དག་གི་སྟེང་དུ་བུ་གུ་ཆེན་པོ་གཅིག་གདོད་པར་བྱའོ། །

[Block 910]
དེ་དག་ཉིད་བསྡུ་བའི་ཕྱིར་འོག་སྦུབས་ཅན་དུ་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 911]
འདིར་བུམ་པའི་བུ་ག་ཆེན་པོ་གཅིག་གདོད་པར་བྱའོ་ཞེས་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 912]
དེ་ཡང་འདིར་དོན་གྱིས་ཐོབ་པ་སྟེ་དེ་བས་ན་འདིར་མ་བསྟན་ཏོ། །

[Block 913]
དེ་དག་ཏུ་རས་མ་དགབ་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ་དེ་དག་ཏུ་ཞེས་བྱ་བ་ནི་ནང་གི་བུ་ག་རྣམས་ལའོ། །

[Block 914]
འདིར་གཞུང་ནི་དེ་དག་གི་སྟེང་དུ་རས་གཡོགས་ཏེ་ཆུ་བཙགས་པར༌[^558]བྱའོ་ཞེས་གསུངས་པ་ཡིན་གྱི་བུམ་པའི་བུ་ག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 915]
ཆུ་ཚགས་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བདག་གི་བ་འདི་ཤིན་ཏུ་བྱས་པ་ངེས་པར་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
