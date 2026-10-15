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
[Block 736]
མེད་ན་ཡུད་ཙམ་ཞིག་ཙོག་པུར༌[^522]འདུག་ལ་ཁྲུས་རས་ཀྱིས་ཕྱི་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འཇུག་པ༌[^523]ཇི་ཙམ་གྱིས་འགྲུབ་པས་ཁྲུས་རས་ཀྱིས་ཕྱིས་པས༌[^524]དོན་བསྒྲུབ་པ་དེ་ཙམ་གྱིས་འདི་ལ་ཇི་ཙམ་པའི་དུས་ཀྱི་ཚད་ཀྱིས་བསྒྲུབ་པ༌[^525]དེ་ཉེ་བར་མཚོན་པ་ནི་འདར་ནི་ཡུད་ཙམ་མོ། །

[Block 737]
ཆུང་བ་དག་གིས་དེ་ལ་ཡུད་ཙམ་ཞེས་བྱ་བ་འདི་བརྗོད་པའོ། །

[Block 738]
ཙོག་པུར་འདུག་པ་ཞེས་བྱ༌[^526]ནི་དེ་བཞིན་དུ་མྱུར་དུ་འགྲོ་བའི་ཆུ་ལ་ལུས་ལས་བསྒྲུབ༌[^527]པའོ། །

[Block 739]
འདིར་གནས་པའི་སྦས་པའི་ངོ་བོ་སྟེ། དེ་བས་ན་འདི་སྒྲེན་མོས་བསྟེན་པ༌[^528]རིགས་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ཡང་དག་པར་བསྟན༌[^529]པའོ། །

[Block 740]
བསྲོ་ཁང་བསྟེན་པར་བྱའོ། །

[Block 741]
བསྲོ་ཁང་གི་ཁང་པ་བྱ་བ་ནི་གྲམ་ས་ཆེ་བར་བཟང་ངོ་ཞེས་བྱ་བ་ནི་བསྲོ་ཁང་གི་དོན་དུ་ཁང་པ་ནི་ཁང་པ་སྟེ། གྲམས་ཆེ་བའི་ས་ཕྱོགས་ལ་ཁང་པ་བྱ་ཞེས་བྱ་བའོ། །

[Block 742]
འདིར་གཞུང་ནི་ཕྱོགས་རྣམས་ལ་འདི་སོང་བ་ལ་ཡང་མ་རྫོགས་པའི་དོན་བསྒྲུབ་པ༌[^530]ཡིན་ཏེ། གྲམ་ས་ཆེ་བ་ལ་ནི་ཡོངས་སུ་རྫོགས་པའི་དོན་སྒྲུབ་པར་བྱེད་པ་ཉིད་ཀྱི་ཕྱིར་རུང་བ་ཉིད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 743]
དེ་བཞིན་དུ་གནས་ལ་ཡང་རུང་བའི་སྒྲ་སྦྱོར་བར་རིག་པར༌[^531]བྱའོ། །

[Block 744]
བསྲོ་ཁང་གི་ཁང་པ་དེ་ལ་གང་ཞིག་བྱ་བ་དེ་ཉེ་བར་བསྟན་པའི་ཕྱིར། དཀྱིལ་དུ་སྐར་ཁུང་ཕྱི་རུབ་ལ་ནང་ཡངས་པ་རྒྱ་མཚོའི་རྣམ་པ་ལྟ་བུ་གདོད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁང་པ་ལ་བརྟེན་པའི་རྩིག་པའི་དབུས་སུ་སྟེང་འོག་དང་སྟེང་དུ་ཡང་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 745]
དེར་སྐར་ཁུང་དྲ་བ་ཅན་དང་སྒོ་གླེགས་དང་འཁོར་གཏན་དང་གནམ་གཟེར་དང་འཕྲེད་གཏན་དང་བཅས་པ་གཞུག་གོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས་བྱ་བ་ནི་སྐར་ཁུང་ལའོ། །

[Block 746]
དབྱུག་གུ་སྐམ་ཁ་ཡང་ཉེ་བར་གཞག་གོ་ཞེས་བྱ་བ་ནི་དེར་ཞེས་བྱ་བ༌[^532]འདི་དང་འབྲེལ་པ་ཉེ་བར་བསྒྲུབ་པའི་དོན་དུ་ཡང་གི་སྒྲའོ། །

[Block 747]
དབྱུག་གུ་སྐམ་ཁས་སྐར་ཁུང་གི་འཕྲེད་གཏན་གཞུག་པ་དང་དབྱེ་བའོ། །

[Block 748]
སྒོར་སྒོ་གླེགས༌[^533]དང་སྒོ་གཏན་དང་ཡང་མིག་དང་ལག་གཟུངས་ལེགས་པར་བྱའོ་ཞེས་བྱ་བ་ལ། སྒོར་ཞེས་བྱ་བ་ནི་བསྲོ་ཁང༌[^534]གི་སྒོ་ལའོ། །

[Block 749]
ཆུ་དྲོན་གཞག་པའི་ཕྱིར་ནང་གི་ཕྱོགས་སུ་གཞག་སྟེགས་བྱའོ་ཞེས་བྱ་བ་ལ། གཞག་སྟེགས་ནི་སྟེགས་བུ་སྟེ་གང་ལ་ཆུའི་བུམ་པ་རྣམས་འཇོག་པ་ཡིན་ནོ། །

[Block 750]
མེ་འབུད་པའི༌[^535]གནས་ཀྱི་སར་སོ་ཕག་གི་གཅལ་བྱའོ། །

[Block 751]
མེ་མི་འཆི་བའི་ཕྱིར་སྦ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཟླུམ་པོར་བྱ་བའོ། །

[Block 752]
དེའི་ཆེད་དུ་ལྕགས་ཀྱི་ཐལ་ཕྱགས་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་ཆེད་དུ་ཞེས་བྱ་བ་ནི་མེ་སྦ་བའི་ཆེད་དུའོ། །

[Block 753]
མེ་འབར་བ་ན་མི་རྨྱ་བར་བྱ་བའི་ཕྱིར་འཇུག་པ་བསྡད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བསྲོ་ཁང་ལའོ། །

[Block 754]
བོག་པ་མི་འབྱུང་བར་བྱ་བའི་ཕྱིར་ཕྱེ་དང་ཉུངས་མར་དུ་བསྲེས་པ་དག་མེར་བླུགས་སོ་ཞེས་བྱ་བ་ལ། མེའི་ངར་ནི་བོག་པའོ། །

[Block 755]
དྲི་མི་ཞིམ་པ་ཉིད་བསལ་བའི་ཕྱིར་བདུག་སྤོས་བླུགས་སོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དེའི་ཕྱེ་རྣམས་ཀྱིས་དྲི་མི་ཞིམ་པར་བྱས་པས་སོ། །

[Block 756 [VERSE]]
མཆི་མ་འཛག་ན་ནས་ཀྱི་བག་ཟན་གྱིས་བཅད་དོ། །
སྐྱུ་རུ་རའི་ཕྱེ་མ་སྦྲུས་པའི་ཆང་བུས་ཀྱང་ངོ་། །
དེར་རྩྭ་བམ་གྱི་སྟན་གདིང༌[^536]ངོ་ཞེས་བྱ་བ་ལ།
དེའི་བསྲོ༌[^537]ཁང་ལ་རྩྭ་བམ་གྱི་སྟན་གདིང་ངོ་། །

[Block 757]
འདི་ལ་ཆགས་པས་སྟན་གདིང་བའི་དོན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་ལ་གནང་བའོ། །

[Block 758]
ས་གཞིར་སྐྱེས་པ་ཉིད་ཀྱིས་སམ་སྦངས་པས་གཤེར་བའི་རྩྭ་གཤེར་བ་དག་དགྲམ་མོ་ཞེས་བྱ་བ་ནི་དེ་ལ་སྐྱེས་པ་ཉིད་ནི་གང་ཞིག་སྐྱེས་པ་ཉིད་ཀྱིས་གཤེར་བ་ཉིད་དོ། །

[Block 759]
དེ་མེད་ན་གང་ཞིག་སྐྱེས་པ༌[^538]སྦངས་པས་གཤེར་བ་ཉིད་དེ་ལ་བསྟེན་པར༌[^539]བྱའོ། །

[Block 760]
འདི་ལ་དོན་ནི་ཚབ་མེད་པའོ། །

[Block 761]
གཡན་པ་ཕྲུག་པའི་ཆེད་དུ་ལྕགས་ཀྱི་ཕྲུག༌[^540]སྤྱད་བྱ་བའོ།[^541] །རྫས་ཀྱི་གླས་ལུང་མིག་ནས་ཐག་གུས་བཏགས༌[^542]ཏེ་དབེན་པར་གཞག་གོ། །

[Block 762]
དེ་ལ་དྲི་མ་མེད་པ་ཉིད་དུ་བསྒྲུབ་པའི་ཕྱིར་མེས་རུང་བར་བྱའོ། །

[Block 763]
དེར་ཁྲུས་མི་བྱའོ་ཞེས་བྱ་བ༌[^543]ལ། དེར་ཞེས་བྱ་བ་ནི་བསྲོ་ཁང་ལའོ། །

[Block 764]
དེའི་ཆེད་དུ་ཁྲུས་ཁང་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་ཆེད་དུ་ཞེས་བྱ་བ་ནི་ཁྲུས་ཀྱི་ཆེད་དུའོ། །

[Block 765]
ཁྲུས་ཆུ་ལྡུགས་པའི་ཆོས་གོས་དག་མི་ཉམས་པར་བྱ་བའི་ཕྱིར་སོ་ཕག་གིས་བསྒྲོན་པའི༌[^544]ཁྲུས་དོང་བྱའོ་ཞེས་བྱ་བ་ནི༌[^545]ཁྲུས་ཆུ་ལྡུགས་པའི་ཆོས་གོས་རྣམས་མི་ཉམས་པར་བྱ་བའི་ཕྱིར་དོང་དུ་ཞུགས་པས་ནི༌[^546]ཁྲུས་བྱ་བ་ལ་ཁ་ན་སྡོད་པས་ནི་ཆུ་བླུགས་པར་བྱ་སྟེ། དེ་བས་ན་ཉམས་པར་མི་འགྱུར་རོ། །

[Block 766]
དེ་ལ་སྟོར་ཁུང་གདོད་དོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་སྟོར་ཁུང་ལའོ། །

[Block 767]
ཆུ་ཧ་ཅང་ཚ་ན་ཕྱི་མ་རྣམས་ལ་སྦྲན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཆུ་ཚ་བར་ཤེས་ནས་ཕྱི་མ་རབ་ཏུ་བྱུང་བ་རྣམས་ལ་སྦྲན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 768]
དེར་གྲང་མོས་བསྲེའོ་ཞེས་བྱ་བ་ནི་ཆུ་ཚ་བ་ལའོ། །

[Block 769]
ཆག་ཆག་གིས༌[^547]ཆུ་ལ་སོགས་པར་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཆག་ཆག་གིས༌[^548]ཆུ་ལ་སོགས་པའི་དོན་དུ་ཡང་གྲང་མོས་འདི་ལ་བསྲེའོ། །

[Block 770]
ཐལ་བ་དང་བ་ལང་གི་ལྕི་བ་དང་སོ་ཤིང་གིས་བཀང་བའི་གྱོ་མོ་དག་གཞག་པར་བྱའོ། །

[Block 771]
གལ་ཏེ་ཉམས་དམས་པར་གྱུར་ན་ཁྱེའུ་སུས་བྱའོ། །

[Block 772]
དེར་ངོ་མི་ཤེས་པ་ཞིག་ཤན་བསྲེ་བས་ཉེ་བར་གནས་པར་གྱུར་ན་དེར་གཏོགས་པས་ངེས་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་དྲི་བར་བྱ་ཞིང་དེའི་ཆེད་དུ་མི་འཇུག་པར་བྱ་བའི་ཕྱིར་དགེ་སློང་བསྒོ་བ་བསྐོའོ༌[^549]ཞེས་བྱ་བ་ལ། ཤན་བསྲེ་བས་ཞེས་བྱ་བ་ནི་ཁོ་བོ་ཁྱེད་ཅག་ལས༌[^550]གང་ཡང་རུང་བ་ཞིག་ཡིན་ནོ་ཞེས་བྱ་བ་གསེབ་ཏུ་འཇུག་པར་བྱ་བས་སོ། །

[Block 773]
དེར་གཏོགས་པ༌[^551]ཞེས་བྱ༌[^552]ནི་བསྲོ་ཁང་ན་རྣམ་པར་གནས་པའི་དགེ་སློང་གིས་ཏེ་དེས་དྲི་བར་བྱའོ། །ཇི་ཞིག་གི་ཕྱིར་ཞེ་ན། ཇི་ཆོས་འདི་པའི་དགེ་སློང་ཞིག་གམ་འོན་ཏེ་འཚོ་བ་པ་ལ་སོགས་པ་ཞིག་ཡིན་ཞེས་ཏེ་དེ་ལྟར་ངེས་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་དྲི་བར་བྱ་ཞིང་། དེའི་ཆེད་དུ་སྒོ་བ༌[^553]བསྐོའོ༌[^554]ཞེས་བྱ་བ་འདི་མི་ཤེས་པ་ཤན་བསྲེ་བས་ཉེ་བར་གནས་པར་གྱུར་པ་དེ་ངེས་པར་ཤེས་པར་བྱ་བའི་ཕྱིར་དྲི་བར་བྱ་བ་དང་མི་འཇུག་པར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བའོ། །

[Block 774]
འདི་ནི་བདག་ཅག་ལས་གང་ཡང་རུང་བ་ཡིན་པས་ཞེས་བྱ་བའི་དྲི་བས་འདི་ཤེས་པ་ལའོ། །

[Block 775]
བསྒོ་བ་ཇི་ལྟ་བུ་ཞིག་ཅེ༌[^555]ན། དགེ་སློང་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ནི་དཔེ་ཡིན་གྱི་བསྙེན་པར་རྫོགས་པར་མ་བྱས་པའི་རབ་ཏུ་བྱུང་བ་ལ་ཡང་དགེ་སློང་མ་རྣམས་ལ་དེའི་ཕྱོགས་སུ་གྱུར་པའི་གང་ཟག་ལའོ། །
--- END BLOCKS ---
