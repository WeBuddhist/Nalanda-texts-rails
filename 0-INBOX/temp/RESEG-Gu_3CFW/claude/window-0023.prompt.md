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
སྟན་གདིང་བར་བྱའོ། །

[Block 807]
རྐང་པ་བཀྲུ་བར་འགྲོན༌[^720]དུ་གཉེར་བར་བྱའོ། །

[Block 808]
ཆུས་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་བཏུང་བའི་དོན་དུ་ཆུས་འགྲོན༌[^721]དུ་བསྙེན་པར་བྱའོ་ཞེས་བྱ་བ་དོན་གྱིས་རྟོགས་པར་བྱའོ། །

[Block 809]
ཕྱག་བྱའོ། །

[Block 810]
སྤྱོད་པ་བདེའམ་འདྲིའོ།[^722] །ཅི་ནུས་ཀྱིས་ཡང་དག་པར་དགའ་བར༌[^723]འགྱུར་བར་བྱའོ། །

[Block 811]
གནས་མལ༌[^724]རྐྱེན་དུ་འབབ་པ་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་མ་མོ་དག་ལས་མཐུན་པས་ལྷུང་བཟེད་དང་ཆོས་གོས་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 812]
དགེ་འདུན་གྱི༌[^725]གནས་བརྟན་གྱི་གན་དུ་འགྲོ་བར་བྱའོ་ཞེས་བྱ་བ་ནི་གློ་བུར་བའོ། །

[Block 813]
ཚིག་དེ་ནི་གློ་བུར་བ་ལམ་དུ་མི་འགྲོ་བ་དག་གི་ཕྱིར་གསུངས་པ་ཡིན་ནོ། །

[Block 814]
དེས་དེ་གནས་འཆའ་བ་ལ་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེས་དེ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་གནས་བརྟན་དེས་སོ། །

[Block 815]
དེ་ལ་ཞེས་བྱ་བ་ནི་གློ་བུར་དུ་འོངས་པ་དེ་ལའོ། །

[Block 816]
གལ་ཏེ་རྒན་ན་དེ་གནས་མལ་བསྟབས་པའི་ཕྱིར་དེའི་དགེ་སྐོས་ལའོ་ཞེས་བྱ་བ་ནི་དགེ་འདུན་གྱི་གནས་བརྟན་གྱིས་གནས་མལ་སྟོབས་པའི་དགེ་སྐོས་ལ་བསྒོ་བར་བྱའོ། །

[Block 817]
བབ་ཅོལ་དུ་གནས་མལ་གསོལ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདི་ནི་མ་མོ་དག་ལས་ལེགས་པར་སོ་སོར་བརྟགས་ཏེ་མནོད་པར༌[^726]བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 818]
གློ་བུར་དུ་འོངས་པའི་སྐབས་སོང༌[^727]ཟིན་ཏོ།། །།

[Block 819]
ཆོས་གོས་ཀྱི་མཐའ་ཟེགས་ན་མཐའ་སྐོར་གྱིས་གླན་ཞིང་ཕྱིར་བཅོས་སོ། །

[Block 820]
སྨྱུང་ཚམས༌[^728]ལྟ་བུ༌[^729]དག་གིས་དེའི་གཟུངས་གདབ་པོ་ཞེས་བྱ་བ་ནི་མཐའ་སྐོར་བསྡུས་པའོ། །

[Block 821]
རོའི་གོས༌[^730]ནི་བླ་གབ་མེད་པར་ཞེས་བྱ་བ་སྨོས་ན་ཕྱོགས་གང་དུ་ཞེ་ན། དེའི་ཕྱིར། ཤིང་ལྗོན་པ་ལ་སོགས་པའི་སྟེང་དུའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 822]
ཉི་མ་བདུན་ནམ་བརྒྱད་དམ་ཁ་ཅིག་ལས་ལྔའམ་དྲུག་བཞག་སྟེ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 823]
དེ་ལྟར་རོའི་གོས་ལའོ། །

[Block 824]
གོས་འཁྲུར་བཅུག་ནས་སྤྱད་པར་བྱའོ། །

[Block 825]
བདག་དུར་ཁྲོད་པའོ༌[^731]ཞེས་གོ་བར་བྱས་ནས་ཞེས་བྱ་བ་ལ་གོ་བར་བྱས་ནས་ཞེས༌[^732]བྱ་བ་ནི་བརྗོད་ན་དོན་གང་ལ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བདག་དུར་ཁྲོད་པའོ་ཞེས་འབོད་ནའོ། །

[Block 826]
གཙུག་ལག་ཁང་དང་ཁྱིམ་བདག༌[^733]ཏུ་འཇུག་པར་བྱའོ། །

[Block 827]
དུར་ཁྲོད་པས་བདག་གིར་བྱ་བ་མ་བཏང་བ་ལ་ཡང་སྤྱད་པ༌[^734]བསྟེན་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་དེ་སྐད་ཅེས་བརྗོད་པ་ན། བདག་གིར་བྱ་བ་མ་བཏང་བ་ལ་ཡང་དེ་ལྟར་ལོངས་སྤྱོད་པ་ཉིད་ཀྱིས་བསྟེན་པར༌[^735]བྱ་བའི་དོན་ཏོ། །

[Block 828]
ཁྱིམ་གྱི་སྒྲས་ནི་བྲམ་ཟེ་དང་ཁྱིམ་བདག་གི་ཁྱིམ་པ་གཟུང་བར་རིག་པར་བྱའོ། །གང་གིས༌[^736]ལོངས་སྤྱད་པར༌[^737]བྱ་ཞེ་ན། དེའི་ཕྱིར་བདག་གིར་བྱ་བ་མ་བཏང་བར་ཡང་ཞེས་བྱ་བ་སྨོས་ཏེ། དེའི་ལྷུང་བཟེད་ལ་རེག་པ་ཡོངས་སུ་མ་བཏང་ཞིང་སྦྱིན་པ་གང་ཡིན་པ་དེ་ལ་ཞེས་བྱ་བའི༌[^738]དོན་ཏོ། །

[Block 829]
དགེ་འདུན་གྱི་གནས་མལ་ལ་སྤྱད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་དུར་ཁྲོད་པས་སོ། །

[Block 830]
མཆོད་རྟེན་ལས་འདོམ་གང་ཙམ་གྱིས་འགྱེད་དོ་ཞེས་བྱ་བ་ཡང་དུར་ཁྲོད་པས་སོ། །

[Block 831]
སྦྲང་ཡབ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། དེའི་ཕྱིར་བལ་ལས་བྱས་པ་དང་། ཤ་ན་ལས་བྱས་པའི་རས་མའམ་འདབ་མའི་དོག་པའོ། །

[Block 832]
གླང་པོ་ཆེ་དང་རྟ་དང་བ་ལང་གི་སྤུ་ལ་སོགས་པ་ལས་བྱས་པ་མི་རུང་ངོ་ཞེས་བྱ་བ། སྦྲང་བུ་དག་གསོད་པའི་བདག་ཉིད་གང་ཡིན་པ་དེ་ཡང་འདིར་བཀག་པ་ཡིན་ནོ། །

[Block 833]
བལ་ལ་སོགས་པ་ནི་དཔེ་ཙམ་དུ་ཟད་ཀྱི། [^739]དེ་བས་ན་གཞན་ཡང་རྟོགས་པར་བྱའོ། །

[Block 834]
འདིར་ཡང་སྦྲང་སྐྱབས་ནི་དོན་མཚུངས་པ་ཉིད་དེ་དེའི་ཕྱིར་དེ་དང་བཅས་པར་སྨོས་པར་གྱུར་ཅིག་ཅེས་བྱ་བ་འདིར་འདི་རྣམ་པར་གཞག་པའོ། །

[Block 835]
ཐམས་ཅད་དུ་གང་ཟག་གིས་འཁར་བ༌[^740]རྩི་ཅན་ཉིད་དང་ཁྲ་བོ་ཉིད་མི་རུང་ངོ་ཞེས་བྱ་བ་ལ། ཐམས་ཅད་དུ་ཞེས་བྱ་བ་ནི་སྦྲང་ཡབ་ཀྱི་ཡུ་བ་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི། འོན་ཀྱང་གཞན་ཐམས་ཅད་ལ་ཡང་ཕྱོགས་གཅིག་ཏུ་གྱུར་པ་དང་ཡན་ལག་ཏུ་གྱུར་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 836]
སྦྲང་སྐྱབས་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་བཅང་བར་བྱའོ་ཞེས་ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། དེའི་ཕྱིར། ཤིང་བུའི་སྟེང་དུ་རས་ཀྱིས་གཡོགས་པའོ༌[^741]ཞེས་བྱ་བ་སྨོས་སོ། །ཇི་ལྟར་ཤིང་བུལ་གཡོགས་པར༌[^742]བྱ་ཞེ་ན། དེའི་ཕྱིར་བཅིངས་པས༌[^743]སོ་ཞེས་སྨོས་སོ། །

[Block 837]
རས་ཇི་ཙམ་ཞིག་ཅེ་ན། ཁྲུ་བཞི་དང་དོ་པའོ་ཞེས་སྨོས་ཏེ། སྲིད་དུ་ཁྲུ་བཞི་ལ་ཞེང་ཁྲུ་དོ་པའི་ཚད་གང་ལ་ཡོད་པའི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 838]
རས་ཁྲུ་བཅུ་གཉིས་པས་གཡོག་གོ་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་གཡོགས་པར༌[^744]བྱ་ཞེ་ན། དེའི་ཕྱིར་འབྱར་བ་དང་བཅས་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རས་ཀྱི་མཐའ་མ་རྣམས་འབྱར་བ་ཞེས་བྱ་བ་འདི་སྐབས་ཉིད་ཀྱི་ཕྱིར་ཤེས་པར་བྱའོ། །

[Block 839]
དེའི་མ་མཐའ་ནི་མལ་ཆས་སྦྱར་རོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་གཡོགས་མའི་རས་དེ་ལའོ། །

[Block 840]
སྒོ་བསེགས་ཁར་འདོད་དོ་ཞེས་བྱ་བ་ནི། སྦྱང་སྐྱབས་ཀྱི་སྒོ་སྣོལ་མར་འདོད་པའོ། །

[Block 841]
ཚ་བར་ནི་བསིལ་བ༌[^745]སྦྱར་རོ། །

[Block 842]
བསིལ་ཡབ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། རླུང་བསྐྱབ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བསིལ་ཡབ་བོ། །

[Block 843]
འདིར་བཅོས་མ་ཉིད་ནི་གཙོ་བོ་སྟེ། གང་ཟག་ནི་མ་ཡིན་ནོ། །

[Block 844]
དེ་བས་ན་མ་ཞེན་པར་བྱས་པ་ནི་འདིར་མ་བསྡུས་པ་ཉིད་དོ། །

[Block 845]
བསིལ་ཡབ་མཁན་གྱིས་བྱས་པ་དང་། ཏ་ལའི་ཆང་བུའོ་ཞེས་བྱ་བ་ནི་སྐྱེད་པའི༌[^746]ཆ་བྱད་ནི་ཏ་ལའི་ལོ་མའི་ཚོགས་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
