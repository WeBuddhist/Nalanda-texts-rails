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
[Block 526 [VERSE]]
དེ་ནི་མ་ལུས་ཐོས་གྱུར་ལ། །
འཛིན་པ་ལ་ནི་རྣམ་པར་མཁས། །

[Block 527]
ཞེས་སྨོས་ཏེ་བཀའ་དང་བསྟན་བཅོས་ཐམས་ཅད་མ་ལུས་པར་ཐོས་པ་ནི་མ་ལུས་པར༌[^249]ཐོས་པའོ། །

[Block 528]
འཛིན་པ་ལ་ནི༌[^250]རྣམ་པར་མཁས། །ཞེས་པ་ནི་ཐོས་པ་ཙམ་གྱིས༌[^251]ཐམས་ཅད་ཁོང་དུ་ཆུད་པའོ། །

[Block 529]
སྐད་ཅིག༌[^252]ཙམ་གྱིས་བརྗེད༌[^253]འགྱུར་བ། །ཞེས་པ་ནི་བླ་མ་དང་བྲལ་བ་ཙམ་གྱིས་བརྗེད་པར༌[^254]འགྱུར་རོ། །

[Block 530]
དེའི་མིང་ཅི་ཞེ་ན། ཨུཏྤལ་ཞེས་བྱ་བའི་གང་ཟག་གོ། །ཞེས་སྨོས་ཏེ། ཨུཏྤལ་དང་འདྲ་བས་ཨུཏྤ་ལ་ལྟ་བུའི་གང་ཟག་གོ། །

[Block 531]
ཨུཏྤལ་ཞེས་བྱ་བ་འདི་ལ་མཐུན་པའི་ཆོས་ཅི་ཡོད་ཅེ་ན། ཇི་སྲིད་དུ་ཨུཏྤལ་ཞེས་བྱ་བ༌[^255]འདི་ནི་ཉི་མ་ཤར་བའི་ཚེ་ན་ཁ་འབྱེ་བར་འགྱུར་གྱི། གང་གི་ཚེ་ནུབ་པར་གྱུར་པའི༌[^256]དུས་ན་ནི་གང་ལ་འབྱེ་བར་འགྱུར་བའི་ཆོས་མེད་དོ། །

[Block 532]
པད་དཀར་ཞེས་བྱ་བའི༌[^257]གང་ཟག་འདི་ཡང་ཅི་ཞིག་ཡིན་ཞེ་ན། གཟུང་བྱ་མང་དུ་ཐོས་གྱུར་ཀྱང་། །ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པའི་སྒྲ་དཔག་ཏུ་མེད་པ་ཐོས་པར་གྱུར་ཀྱང་ཞེས་པའོ། །

[Block 533]
སྟོན་པ་ཡིས་ནི་ནུས་མེད་པ། །ཞེས་པ་ནི་བསམ་པ་དང་བརྗོད་པ་དང་བྲལ་ཞེས་པའོ། །

[Block 534]
བུམ་པའི་རས་བལ་ས་བོན་འདྲ། ཞེས་པ་ནི། བུམ་པའི་ནང་དུ་རས་བལ་གྱི་ས་བོན་བཅུག་པ་བསྟན་དུ་མེད་པ་བཞིན་ནོ། །

[Block 535]
པད་དཀར་ལྟ་བུའི་གང་ཟག་གོ། །ཞེས་པ་ནི་པདྨ་དཀར་པོ་ལ་ཆུས་མི་ཆགས་པ་བཞིན་ནོ། །

[Block 536]
པདྨ་ཞེས་བྱ་བའི་གང་ཟག་ཀྱང་གང་ཞིག་ཡིན་ཞེ་ན། དད༌[^258]དང་ལྡན་ཞིང་སྙིང་རྗེ་ཤེས། །ཞེས་པ་ལ་སོགས་པ་ནི༌[^259]ལྡན་ཞེས་བྱ་བ་ཀུན་ལ་སྦྱར་བར་བྱ་སྟེ། དད་པ་དང་ལྡན་པ་ནི་འདོད་པ་དང་། དང་བ་དང་། ཡིད་ཆེས་པ་དང་། [^260]དེ་དང་གང་ལྡན་པ་ནི་དེ་རྣམས་དང་མ་བྲལ་བ་སྟེ་དེ་ཉིད་དང་ལྡན་པའོ། །

[Block 537]
སྙིང་རྗེ་དང་ལྡན་པ་ནི་སྙིང་རྗེ་ཆེན་པོ་དང༌[^261]མ་བྲལ་བའོ། །ཤེས་རབ་དང་ལྡན་པ་ནི་ཤེས་རབ་ཆེན་པོ་དང་མ་བྲལ་བའོ། །

[Block 538]
ཐོས་ནས་བློ་ཡི་ཁ་བྱེ་ལ། །ཞེས་པ་ནི་བློ་རྒྱ་ཆེན་པོར་གྱུར༌[^262]ཞེས་པའོ། །

[Block 539]
ཚིགས་མེད་འོད་མ་བཞིན་ཉན་པ། །ཞེས་པ་ནི་ཚིགས་པ༌[^263]མེད་པའི་འོད་མ་གས་པོ་ལྟར་ཉན་ཞེས་པའོ། །

[Block 540]
འདིས་ནི་དུས་ཐམས་ཅད་དུ་ཉན་པར་བྱེད་ཅིང་སྒོམ་པ༌[^264]དང་བཤད་པ་ལ་སོགས་པ་སྤངས་ཞེས་སྦྱར་རོ། །

[Block 541]
འདི་ཉིད་མིང་ཅི་ཡིན་ཞེ་ན། པདྨ་ཞེས་བྱ་བའི་གང་ཟག་གོ་ཞེས་སྨོས་ཏེ། ཚིགས་མེད་པ་ནི་དཔེར་ན་པདྨ་གས་པ་ལྟ་བུའོ་ཞེས་སྦྱར་རོ། །

[Block 542]
ཙནྡན་ལྟ་བུའི་གང་ཟག་ཅེས་བྱ་བ་འདི་ཡང་གང་ཞིག་ཡིན་ཞེ་ན།

[Block 543 [VERSE]]
ཐོས་པ་ཉུང་ཞིང་ང་རྒྱལ་ལྡན། །
ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ།
ཐོས་པ་ཉུང་བ་ནི་མ་ཐོས་པའོ། །

[Block 544]
ང་རྒྱལ་ལྡན་པ་ནི་བདག་ཐོས་པ་དང་ལྡན་པ་ཡིན་ཞེས་སྨྲ་བའོ།[^265] །རྩ་བ་མེད་པར་མང་དུ་སྨྲ། །ཞེས་པ་ནི་ངེས་པའི་ཤེས་པ་མ་སྐྱེས་པར་སྣ་ཚོགས་པ་སྨྲ་ཞེས་པའི་དོན་ཏོ། །

[Block 545]
རྗེས་སུ་གཟུང་བར༌[^266]མི་ནུས་པ། །ཞེས་པ་ནི་ཕྱིས་རང་གིས་འཛིན་པར་མི་ནུས་པའོ། །

[Block 546]
དེ་ཉིད་ཀྱི་མིང་ཅི་ཞེ་ན། ཙནྡན་ཞེས་བྱ་བའི་གང་ཟག་གོ་ཞེས་སྨྲ་སྟེ།[^267] ཙནྡན་དང་འདྲ་བས་ཙནྡན་ལྟ་བུའི་གང་ཟག་སྟེ།[^268] རི་མ་ལ་ཡའི་ཙནྡན་ལྟ་བུའོ། །

[Block 547]
ང་རྒྱལ་ལྡན་ཞེས་པ་ནི་དབྱར་གྱི་དུས་ཀྱི་ཙནྡན་ལྟ་བུའོ། །ཞེས་པའོ། །

[Block 548]
རྩ་བ་མེད་པར་མང་དུ་སྨྲ། །ཞེས་པ་འདིས་ནི་བ༌[^269]དོ་ལའི་རིའི་ཙནྡན་ལྟ་བུའོ་ཞེས་པའི་དོན་ཏོ། །

[Block 549]
རྗེས་སུ་གཟུང་བར་མི་ནུས་པ། །ཞེས་པ་ནི་ཙནྡན་སྦྲུལ་གྱི་སྙིང་པོ་ཅན་ལྟ་བུའོ་ཞེས་པའི་དོན་ཏོ། །

[Block 550]
འདི་དག་གིས་ནི་ཙནྡན་ལྟ་བུའི་གང་ཟག་བསྟན་ཏོ། །

[Block 551]
དེ་ནས་རིན་པོ་ཆེ་ལྟ་བུའི་གང་ཟག་བསྟན་ཏེ། [^270]ཚུལ་ཁྲིམས་དག་ཅིང་མཁས་ལ་སྒྲིན། །ཞེས་པ་ནི་བསླབ་པ་རྣམ་པ་གསུམ་གྱི་ཚུལ་ཁྲིམས་དང་། དགེ་བའི་ཆོས་སྡུད་པའི་ཚུལ་ཁྲིམས་དང་། སེམས་ཅན་གྱི་དོན་བྱེད་པའི་ཚུལ་ཁྲིམས་དང་། འདི་རྣམས་དང་ལྡན་པ་ནི་ཚུལ་ཁྲིམས་རྣམ་པར་དག་པ་སྟེ། གང་གི་ཚུལ་ཁྲིམས་ལ་སྐྱོན་མེད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 552]
མཁས་པ༌[^271]ནི་མཁས་པ་སྟེ། གང་གིས་གང་གི་བྱ་བ་ཐམས་ཅད་ལ་ཐོགས་པ་མེད་པ༌[^272]དེ་ལ་མཁས་པའོ། །ཤེས་རབ་ལྡན་པ་ནི་ཤེས་རབ་དང༌[^273]ལྡན་པ་སྟེ་ཤེས་རབ་མཆོག་དང་མ་བྲལ༌[^274]ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 553]
རྒྱུད་གཅིག་ལས༌[^275]ཐོས་ནས་ལེགས་པར་སྟོན་པ་ནི་ཡང་དག་པའི་གདམས་ངག་མ་ནོར་བར་ཐོས་ཤིང་དེ་ཉིད་དང་འབྲེལ་པའི་བྱ་བ་བྱེད་པ་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 554]
འདི་ཉིད་ཀྱི་མིང་ཅི་ཡིན་ཞེ་ན། རིན་ཆེན་ལྟ་བུའི་གང་ཟག་གོ། །ཞེས་པ་སྟེ་དཔེར་ན་རིན་པོ་ཆེའི་བུམ་པ་ལྟ་བུའོ་ཞེས་པའི་དོན་ཏོ། །

[Block 555]
གཞན་གོ་སླའོ། །

[Block 556]
བདེན་གཉིས་རྣམ་པར་ངེས༌[^276]བྱས་ཏེ།[^277] །ཞེས་པ་ནི་ཐམས་ཅད་ཀྱང་དོན་དམ་པའི་བདེན་པ་དང་ཀུན་རྫོབ་ཀྱི་བདེན་པར་འདུས་པའོ། །

[Block 557]
འདིར་རྒྱན་བདུན་ཡིན་པས་ན༌[^278]རྒྱན་བདུན་ནོ། །

[Block 558]
རྫོགས་པའི་རིམ་པ་སྒྲུབ་པའོ། །ཞེས་པ་འདི་ནི་ཟུང་དུ་འཇུག་པ་འབའ་ཞིག་གི་དབང་དུ་བྱས་པའོ། །

[Block 559]
བཤད་སྨྲ་ཤིན་ཏུ་རྙེད་པར་དཀའ། །ཞེས་པ་སྟེ་བཤད་པ་པོ་དང་སྨྲ་བ་པོ་ཤིན་ཏུ་རྙེད་པར་དཀའ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 560]
རྙེད་པར་དཀའ་བ་ཅིའི་ཕྱིར་ཞེ་ན། རྣལ་འབྱོར་རྒྱུད་ལས་གཞན་དུ་མིན། །ཞེས་བྱ་བ་སྨོས་ཏེ་རྣལ་འབྱོར་གྱི་རྒྱུད་ཁོ་ན་ལས་རྙེད་ཀྱི་གཞན་ལས་རྙེད་པ་མ་ཡིན་ནོ་ཞེས་བྱ་བའི༌[^279]དོན་ཏོ། །

[Block 561]
དེ་བས་རྡོ་རྗེ་སློབ་དཔོན་གྱིས། །ཞེས་པ་ནི་གོང་མ་དང་འབྲེལ་ཏོ། །

[Block 562]
གླེང་གཞི་རིམ་པ་སྦྱོར་བར་བཅས། །ཞེས་པ་ནི་གླེང་བསླང་བ་ལ་སོགས་པའོ། །

[Block 563]
རྒྱན་རྣམ་པ་བདུན་བཤད་པའི་རིགས་པའོ་ཞེས་པ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རྒྱུད་ཐམས་ཅད་ནི་རྒྱན་རྣམ་པ་བདུན་གྱི༌[^280]འཆིང་བ༌[^281]བཅིངས་ལ་རྒྱུད་ཤེས་པར་འདོད་པས་ཀྱང་དེ་ལ་བསླབ་པར༌[^282]བྱའོ་ཞེས་པའི་དོན་ཏོ། །

[Block 564]
རྒྱན་རྣམ་པ་བདུན་ཡང་ཡིན་ལ་བཤད་པའི་རིགས་པ་ཡང༌[^283]ཡིན་ན༌[^284]དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 565]
སྒྲོན་མ་གསལ་བ་ཞེས་བྱ་བའི་འགྲེལ་བཤད་ལས་རྒྱན་རྣམ་པ་བདུན་སྤྲོས་པ་དང་བཅས་པའི་བཤད་པའོ།། །།
--- END BLOCKS ---
