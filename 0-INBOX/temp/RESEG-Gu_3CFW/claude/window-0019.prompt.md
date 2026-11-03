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
ཆུ་བདེ་བས་སོ་ཞེས་བྱ་བ་ལ། དེ་ནི་དྲི་མ་འདག་པའི་ཐབས་བསྟན་པའོ། །

[Block 667]
དེ་བས་ན་ཐབས་གཞན་གྱི་གནས་སུ་དེ་ལ་ནི་བསིལ༌[^601]བ་ཉིད་ནི་ཧ་ཅང་མི་གྲང་བ༌[^602]ནི་མ་ཡིན་ནོ། །

[Block 668]
ལག་པ་གཉིས་ཀྱིས་མཐར་གྱིས་བསྒྱུར་ཞིང་ངོ་ཞེས་བྱ་བ་ནི་བསྒྱུར་ཞིང་བཀྲུ་བར་བྱའོ། །

[Block 669]
མི་ནུས་ན་རྐང་པ་གཉིས་ཀྱིས་སོ། །

[Block 670]
དེ་ལྟར་ཁྱིམ་པས་བཀྲུར་རུང་ངོ་ཞེས་བྱ་བ་ལ། དེ་ལྟར་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་རང་གིས་བཀྲུ་བའི་ཆོ་ག་དེ་བསྟན་པ་དེ་ལྟར་རོ། །

[Block 671]
དེ་གཞན་དུ་འགྱུར་བར་སྤྱོད་པ་བསྲུང་བར་བྱའོ་ཞེས་བྱ་བ་ནི། ཆོ་ག་ཇི་སྐད་བསྟན་པ་ལས་གཞན་དུ་ཁྱིམ་པ་དེའི་ལོག་པར་སྤྱོད་པ་བསྲུང་བར་བྱའོ། །

[Block 672]
འདིར་གཞུང་ནི། གཞན་གྱི་ལག་པ་གཉིས་ཀྱིས་ཀྱང་མི་ནུས་ལ། རྐང་པ་གཉིས་ཀྱིས་ཀྱང་མི་ནུས་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དེ་དག་གིས་ཞལ་ཏ་བྱས་ཏེ་གཞན་གྱིས་བཀྲུ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 673]
མི་ནུས་ན་ཞེས་བྱ་བ་སྨོས་པ་ནི། གླེང་གཞི་ལས་བྱུང་བས་སོ། །

[Block 674]
དེ་བས་ན་འདིར་མ་བསྟན༌[^603]ནོ། །

[Block 675]
ཕྱག་དར་ཁྲོད་ལེགས་པར་བཀྲུས་པ་དང་། བཙེམ་པ༌[^604]དང་ཁ་བསྒྱུར་བ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ལེགས་པར་ཞེས་ཀུན་ལ་སྦྱར་བར་བྱས་ཏེ་ལེགས་པར༌[^605]བཀྲུ་བ་དང་ལེགས་པར་བཙེམ་པ་དང་ལེགས་པར༌[^606]ཁ་བསྒྱུར་བར་ཞེས་བྱའོ། །

[Block 676]
དང་བ་བསྐྱེད་པ་མ་ཡིན་པ་ཉིད་བསལ་བའི་དོན་དུ་འདི་ནི་འདུལ་བྱེད་དག་ལས་འདི་དང་མདོ་འོག་མའོ། །

[Block 677]
མི་གཙང་བས་གོས་པའི་ཆོས་གོས་མི་བཅང་ངོ་ཞེས་བྱ་བ་ནི། མི་བཅང་ངོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 678]
ཚོན་བཟང་བ་ཉིད་དུ་བྱ་བའི་ཕྱིར༌[^607]གྲིབ་མ་དང་ཉི་མ་འདྲེས་པར་གདུང་ཞིང་བསྐམ་པར༌[^608]བྱའོ་ཞེས་བྱ་བ་ལ༌[^609]གཞུང་ནི་རྣམ་པར་འབྱེད་པ་ཁ་ཅིག་དང་སྟན་གྱི་བསླབ་པའི་གཞི་ལས་པིབ་པ་ལའི་ཚོན་བླངས་ཏེ། ཆམ་ཆོམ༌[^610]བརྡུང་བར་བྱ་ཞིང་བསྐམས༌[^611]ཏེ་བསྐོལ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 679]
གཞན་དུ་བྱས་ན་ཚོན་ཉམས་པར་འགྱུར་ཏེ། དེ་ལྟར་བྱས་ན་འདི་གདུང་བར་བྱའོ། །

[Block 680]
དེའི་ཕྱིར་འདིར་པིབ་པ་ལ་ཞེས་སྨོས་པ་ནི་ཚོན་གཞན་གྱི་དཔེ་ཡིན་ཏེ་དེ་བས་ན་བྱེ་བྲག་མེད་པར་སྨོས་སོ། །

[Block 681]
གོས་དག་མེད་པར་བསྐོལ་ལོ་ཞེས་བྱ་བ་ནི། ཚོན་ཡིན་ཏེ་ཆོས་གོས་དང་བཅས་པར་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 682]
བྱེ་བྲག་གསུམ་ཡན་ཆད་དུའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 683]
གང་གི་ཕྱིར།[^612] དེ་ལྟར་མང་བ༌[^613]ཉིད་དུ་འདོད་པ་ཉིད་ཡིན་ན་ལན་གསུམ་དུ་བྱའོ། །

[Block 684]
ཕྱི་མ་ཆེས་ངན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་དང་པོ་བསྐོལ་བ་བས་ཕྱིས་བསྐོལ་བ་ཤོས་སོ། །

[Block 685]
དེའི་ཕྱིར་ཐ་དད་པར་གཞག་གོ་ཞེས་བྱ་བ་ནི་བསྐོལ་བ་རྣམས་གཞག་པའོ། །

[Block 686]
འདི་ནི་དང་པོའི་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཡི་གེ་བྲི་བའོ། །

[Block 687]
སྔར་དང་པོ་དང་སྦྱར་རོ་ཞེས་བྱ་བ་ནི༌[^614]ཚོན་ནོ། །

[Block 688]
གོས་ཀུན་ནས་བསུབས་པ༌[^615]ལའོ་ཞེས་བྱ་བ་ནི། ཚོན་ལེགས་པར་འཛིན་པ་ཉིད་དུ་བྱ་བའི་ཕྱིར་ཚོན་གྱིས་བསྒོ་བའོ། །

[Block 689]
ཚོན་གྱིས་ཀུན་ནས་བསུབས་པའི་གོས་དེ་ལ་ཚོན་དང་སྦྱར་བར་བྱའོ། །

[Block 690]
དེ་བས་ན་དེ་ལས་ཐུན་ཇི་ཙམ་རན་པར་བཅུག་ཅིང་གཞོང་པར་བླུགས་སོ། །

[Block 691]
གཤེར་ཆེས་ན་འཇག༌[^616]ལ་སྐམ་ཆེས་ན་འདྲིས༌[^617]པར་འགྱུར་བས་དེའི་ཕྱིར་རན་པར་རོ་ཞེས་བྱ་བ་ནི་བླུགས་པའོ། །

[Block 692]
གཟར་ཐག་ཐང་བཅད་ཉིད་ལ་བསྐམས༌[^618]ན་བཟང་ངོ་ཞེས་བྱ་བ༌[^619]ནི་གཟར་ཐག་ཐང་བཅད་ཅིང་བརྒྱངས་པ་ལ་བསྐམས༌[^620]ན་བཟང་བའོ། །

[Block 693]
ཇི་ལྟར་ཞེ་ན། དེའི་ཕྱིར་མཐའ་དབྱར༌[^621]བས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཇི་ལྟར་མཐའ་དབྱར་བར༌[^622]བྱ་ཞེ་ན། དེའི་ཕྱིར་དབང་བུ་དག་གིས་སོ། །

[Block 694]
གཟུང་དཀའ་བ་རྣམས་ནི་རྩྭ༌[^623]བཏིང་བར་རོ་ཞེས་བྱ་བ་ནི། སྐམ་སར༌[^624]རོ། །

[Block 695]
ཚོན་ཕྱོགས་གཅིག་ཏུ་མི་འཚིགས་པར་བྱ་བའི་ཕྱིར་ཡང་དང་ཡང་བསྒྱུར་བར་བྱའོ་ཞེས་བྱ་བ་ནི། ཚོན་ཕྱོགས་གཅིག་ཏུ་སོང་བར་མ་གྱུར་ཅིག་སྙམ་དུ་འདི་ཡང་ནས་ཡང་དུ་བསྒྱུར་བཟློག་བྱའོ། །

[Block 696]
ཚོན་སར་པ་ནི་སར་པ་དག་ལ་བླུགས་ན་བཟང་ངོ་ཞེས་བྱ་བ་ནི། ཚོན་སར་པ་ནི་སར་པ༌[^625]དག་ལ་བླུགས་ན་བཟང་ངོ་། །རྙིང་པ་ནི་རྙིང་པ་དག་ལའོ། །

[Block 697]
སར་པ་རྣམས་ནི་ཉི་མ་ལ་བསྐམས༌[^626]ནའོ། །

[Block 698]
རྙིང་པ་རྣམས་ནི་གྲིབ་མ་ལའོ། །

[Block 699]
མི་འདྲིས་པར་བྱ་བའི་ཕྱིར་ཉི་མ་གཞན་ལ་ཆུའི་ཐུན་བླུགས་སོ། །

[Block 700]
བང་རིམ་དང་འཆག༌[^627]སར་ཚོན་གྱི་ལས་མི་བྱའོ། །

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
--- END BLOCKS ---
