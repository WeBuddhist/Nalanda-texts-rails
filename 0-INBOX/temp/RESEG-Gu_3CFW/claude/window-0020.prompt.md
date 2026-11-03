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
[Block 701]
གཙུག་ལག་ཁང་དུ་མི་བྱའོ། །

[Block 702]
དེའི་སྟེང་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་གཙུག་ལག་ཁང་གི་སྟེང་དུའོ། །

[Block 703]
ཚོན་གྱི་ལས་དེ་བྱེད་པ་དེ་ནི་དེའི་གནས་ཡིན་གྱིས་བང་རིམ་ལ་སོགས་པ་ནི་མ་ཡིན་ནོ། །

[Block 704]
འཐོར་འཐུང་བྱ་བའི་ཉེན་ཀོར༌[^628]དུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཚོན་གྱི་ལས་མི་བྱའོ། །

[Block 705]
ཕྱོགས་དེར་ཞལ་ཞལ་བྱའོ། །

[Block 706]
གལ་ཏེ་རྡོ་ཐལ་གྱིས་བྱུགས་པ་ཡིན་ན་བཀྲུའོ། །

[Block 707]
གལ་ཏེ་བརྩམས་པ་ན་རླུང་དང་ཆར་འོང་ན་ཁྱམས་སུ་བྱའོ། །

[Block 708]
བྱས་ཟིན་ནས་ཕྱོགས་དེར་ལྕི་བའམ་སས༌[^629]བྱུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^630]བྱས་ཟིན་ནས་ཞེས་བྱ་བ་ནི་ཚོན་གྱི་ལས་སོ། །

[Block 709]
བཅག་པ་དང་བརྡབས་པས་རུང་བར་མ་གྱུར་པ་སྤྱད་པ་བསྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གོས་བཅག་པ་དང་། བརྡབས་པས་རུང་བར་མ་གྱུར་ཅིང་མ་གྲུབ་པ་དང་འདྲ་བ་མ་གྲུབ་པའི་གོས་བསྟེན་པར་མི་བྱའོ། །

[Block 710]
ཡང་འདིར་རུང་བ་གང་ཡིན་པ་གང་དུ་བསྟེན་པར་མི་བྱ་ཞེ་ན། དེའི་ཕྱིར་འདི་ལ་འཚེར་བ་ཉམས་པ་ནི་རུང་བ་ཡིན་ནོ། །

[Block 711]
ཆུས་བརླན་པ་ཉིད་ནའོ། །

[Block 712]
ཟིལ་པས་བརླན་ནས་ལག་པས་མཉེ་བས་ཉམས་པར་བྱ་བ་ལའོ། །

[Block 713]
ཤམ་ཐབས་བགོས་པའི༌[^631]སྟེང་དུ་སྐ་རགས་བཅིང་ངོ་ཞེས་བྱ་བ་ནི་ཤམ་ཐབས་བགོས་པའི་སྟེང་དུ་སྐ་རགས་བཅིང་བར་བྱའོ། །ཅི་ཞིག་བཅིང་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཤུར་བུའམ་ལྕག་པོད༌[^632]དམ། རྒྱ་ཅང༌[^633]ངམ་ཤུར་བུ་ཕྲེ་འུས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། །སྐུད་པ་མང་པོ་ལས་བཏགས་པ་སྲབ་ལ་ཞེང་ཆེ་བ་དང་། ལྷས་མ་གྲུ༌[^634]བཞིར་འདུག་པ་དང་། སྐུད་པ་མང་པོས་བཏགས་པ་ཉིད་ལ་བར་ཁོང་སྟོང༌[^635]དུ་འདུག་པ་དང་། སྐུད་པ་ཕྲ་མོ་ལས་བཏགས་པ་མདོ་མདོར་བུ་གུ་ལྔའམ་དྲུག་རིམ་དུ་བྱས་པ་བཏོད་པ༌[^636]རྣམས་གོ་རིམས་ཇི་ལྟ་བ་བཞིན་དུའོ། །

[Block 714]
སྐ་རགས་མ་བཅིངས་པར་གྲོང་དུ་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། ཤམ་ཐབས་བགོས་པའི་སྟེང་དུ་སྐ་རགས་མ་བཅིངས་པར་གྲོང་དུ་འཇུག་པར་མི་བྱ་བ་སྟེ།[^637] འདི་ནི་ཤམ་ཐབས་བརླག་པར་འགྱུར་པ་སྤང་བའི་ཕྱིར་རོ། །

[Block 715]
ཁྲིས་གཅིག་གིས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི། གལ་ཏེ་སྐ་རགས་ཁྲིས་གཅིག་གིས་བཅིངས་ན་དེ་ལྟར་ན་ཡང་མི་རུང་བའོ། །

[Block 716]
ཚོམ་བུ་ཅན་དང་ཚར་ཚར་ཅན་དང་ཟླ་གམ་ཅན་དང་གསེར་སྐུད་ནི་རྒྱན་མ་ཡིན་པ་མ༌[^638]ཡིན་ནོ་ཞེས་བྱ་བ་ནི། རྒྱན་ཐོགས་པ་བསྟེན་པར་མི་བྱའོ་ཞེས༌[^639]སྨོས་པས་དེ་རྣམས་བཀག་པར་རིག་པར་བྱའོ། །

[Block 717]
ཁྲ་བོར་བྱས་པ་ཡང་དེ་དང་འདྲའོ་ཞེས་བྱ་བ་ནི། རྒྱན་བཞིན་དུའོ། །

[Block 718]
མདོ་འདི་ནི་གོས་ཀྱི་དོན་དུ་བྱས་པ་ཡིན་གྱི་རྩྭ་ལས་བྱས་པའམ། དེ་ལས་གཞན་པ༌[^640]ཡང་རྒྱན་ཉིད་ཀྱི་ཁོངས་སུ་གཏོགས་པའི་ཕྱིར་རོ། །

[Block 719]
གཞི་མ་བཏིང་བའི་སར་ཆོས་གོས་བཞག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི། འདིར་ཐམས་ཅད༌[^641]བར་དུ་གཅོད་པ་དང་། མ་ཉམས་པར་རས་སམ་ལོ་མ་ལ་སོགས་པ་གཞི་མ་བཏིང་བའི་ས་ལ་ཞེས་བྱ་བ་སྟེ། དེ་ནི་མ་རུང་བར༌[^642]འགྱུར་བ་སྤང་བའི་ཕྱིར་རོ། །

[Block 720]
འདིར་གཞུང་ནི་རྣམ་པར་འབྱེད་པའི་སྟན་གྱི་གཞི་ལས་དགེ་སློང་རྣམས་ཆོས་གོས་དག་གྱོན་ཏེ། ས་ལ་འཁོད་པ་ན་ཆོས་གོས་དག་མ་རུང་བར༌[^643]གྱུར་པ་ན། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དད་པས་སྦྱིན་པར་བྱས༌[^644]པ་ཆུད་གསན་པར་མི་བྱ་བར༌[^645]འདི་ལྟར་སྟན་ནང་ཚངས་ཅན་ལ་འདུག་པར་བྱའོ། །

[Block 721]
སྟན་ནང་ཚངས་ཅན་ཇི་ལྟ་བུ་མི་ཤེས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། རྩྭའི་ཆུན་པོ་བཅིངས་ཏེ་རས་མས་དཀྲི་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 722]
འདིར་སྟན་ནང་ཚངས་ཅན་ནི་དཔེ་ཙམ་དུ༌[^646]ཟད་དེ། སྟན་གཞན་ལ་ཡང་འདུག་པར་བྱའོ། །

[Block 723]
འདི་ནི་ཆོས་གོས་མ་རུང་བར༌[^647]འགྱུར་བ་སྤང་བའི་ཕྱིར་རོ་ཞེས་བྱ་བ་དེ་ལྟར་སྨོས་སོ། །

[Block 724]
མི་གཙང་བའི་ཕྱོགས་སུ་མི་གཞག་གོ་ཞེས་བྱ་བ་ནི། ས་མ་ཡིན་པར་གྱུར་པ་ལ་ཡང་ངོ་། །བཏུལ་བ་ཡོད་ན་ཁུར་ལྕི་བས་མི་མནན་ནོ་ཞེས་བྱ་བ་ནི། ཆོས་གོས་མནན་པར་མི་བྱའོ། །

[Block 725]
གཞན་དུ་སྤྱོད་པས་ཡོངས་སུ་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བའི་གཞུང་ནི། འདིར་མ་མོ་ལས་སྟོད་དུ་བགོ་བ་སྨད་དུ་བགོ་བ་དང་སྨད་དུ་བགོ་བ་སྟོད་དུ་བགོ་བས་ཡོངས་སུ་ལོངས་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་སོ། །

[Block 726]
བཤང་བ་དང་གཅི་བ་དང་མི་གཙང་བའི་བྱི་དོར་བྱ་བ་དག་ཏུ་བླ་གོས་བགོ་བ་བསྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བཤང་བ་དང་གཅི་བ་བྱ་བ་དང་། མི་གཙང་བའི་བྱི་དོར་བྱ་བ་དག་ཏུ་བླ་གོས་དག་བགོ་བར་མི་བྱའོ། །

[Block 727]
དེར་ཉལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེར་ཞེས༌[^648]བྱ་བ་ནི་བླ་གོས་དེའི་སྟེང་དུའོ། །

[Block 728]
བསོད་སྙོམས་ལ་རྒྱུ་བ་དང་། མཆོད་སྟོན༌[^649]དང་མཆོད་རྟེན་ལ་ཕྱག་བྱ་བ་དང་རྗེ་ས་བྱ་བ་དང་། དགེ་འདུན་ཚོགས་པ་དང་། གདམས་ངག་དང་ཆོས་མཉན་པ་ཉམས་སུ་མྱོང་བ་ལས་གཞན་པའི་བྱ་བ་ལ་སྣམ་སྦྱར་བགོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་བགོ་བར་མི་བྱ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 729]
དེ་ལ་འདུག་པའམ་ཉལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེ་བརྫིས་ནས་འདུག་པའམ་ཉལ་བར་མི་བྱའོ། །

[Block 730]
དེས་ན་གྲྭ་བརྫི་བ་ཡང་འདིར་བཀག་པ་ཡིན་ནོ། །

[Block 731]
མ་མོ་དག་ལས་དེ་དག་དང་མདོ་འོག་མ་གཉིས་སོ། །

[Block 732]
འགའ་ཡང་བསྐུར་བ་ལ་སྦྱར་བར༌[^650]མི་བྱའོ་ཞེས་བྱ་བ་ནི་དེའི་ནང་དུ་ཅི་ཡང་བཅུག་ནས་བསྐུར་བར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 733]
ལུས་ལ༌[^651]རེག་པར་བགོ་བར་མི་བྱའོ། །

[Block 734]
མཆན་ཁུང་གཡས་པའི་དྲོད་ཀྱིས་དེ༌[^652]མ་རུང་བར་འགྱུར་རོ་ཞེས་བྱ་བ་ནི། མཆན་ཁུང་གང་གི་དྲོད་ཀྱིས་འདི་ཉམས་པར་འགྱུར་རོ་ཞེ་ན།[^653] དེའི་ཕྱིར་གཡས་པའི་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 735]
དེ་ལྟར་མི་འགྱུར་བར་བྱ་བའི༌[^654]ཕྱིར་ཕྱོགས་དེར་གོས་གླན་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ལྟར་མི་འགྱུར་བར་བྱ་བའི་ཕྱིར་ཞེས་བྱ་བ་ནི། ཉམས་པར་འགྱུར་བ་མི་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 736]
ཕྱོགས་དེར་ཞེས་བྱ་བ་ནི་མཆན་ཁུང་གཡས་པའི་ཕྱོགས་དེར་རོ། །

[Block 737]
དེ་ལ་ཞེས་བྱ་བ་དེ་ནི་སྣམ་སྦྱར་དེ་ལའོ། །

[Block 738]
ཁྲུ་ཕྱེད་དང་དོ་དང་མཐོ་གང་ངོ་ཞེས་བྱ་བ་ནི། དེའི་ཚད་ནི་སྲིད་དུ་ཁྲུ་ཕྱེད་དང་དོ་ཞེང་དུ་མཐོ་གང་ངོ་། །ངོས་གཉིས་ཀར་སྐུད་པའི་ཟུངས་ཀྱིས་སྦྱར་རོ་ཞེས་བྱ་བ་ནི་ངོས་གཉིས་ཀར་མཉམ་པར་གླན་པར་བྱའོ་ཞེས་བྱ་བ་ནི༌[^655]དེའི་དོན་རྟོགས་པར་བྱའོ། །

[Block 739]
གཞན་དུ་ནི་གཉིས་ཀ་ལས།

[Block 740]
ངོས་གཉིས་ཀར་གླན་པར་བྱའོ་ཞེས་བྱ་བའོ། །
--- END BLOCKS ---
