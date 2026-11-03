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
[Block 596]
གཞན་དང་ཞེས་བྱ་བ་ལ། གཞན་གྱི་སྒྲས་ནི་གླེགས་བམ་ལ་སོགས་པ་གསུམ་པོ་རྣམས་དང་འབྲེལ་པའོ། །

[Block 597]
སངས་རྒྱས་ཀྱི་བསྟན་བཅོས་ཀྱི་གླེགས་བམ་མྱུར་བར་འབྲི་བ༌[^532]མ་ཡིན་པ་ཚོན་ཆེན་པོ་རྣམས་ལས་གླེགས་བམ་ལ་སོགས་པ། གཞན་རྣམས་ནི་ཕྱི་རོལ་པའི་བསྟན་བཅོས་ཀྱི་གླེགས་བམ་མོ། །

[Block 598]
མྱུར་བར་བསྒྲུབ་པར༌[^533]བྱ་སྟེ། མྱུར་བར་འབྲི་བར་ཁར༌[^534]གསིལ་གྱི་ཡུ་བ་དང་། བཙག་དང་རམས་ལ་སོགས་པ་ཚོན་ཆེན་པོ་རྣམས༌[^535]ལས་ངེས་པར་གྲོལ་པའི་ཁ་དོག་ཅེས༌[^536]བྱ་བ་ནི་འདི་རྣམས་ཀྱིས་ཁ་དོག་གི་སྒྲ་འདི་བསྡུས་པར་བྱས་ཀྱི།[^537] ཚོན་རྩི་དང་ཁར་གསིལ༌[^538]གྱི་ཡན་ལག་ཏུ་གྱུར་པ་ཁ་དོག་བྱེད་པ་ལ་བསྡུ་བའི་དོན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 599]
གཉིས་པར་ཞེས་བྱ་བ་ནི་གོ་བར་འོས་པ་ཉིད་དུའོ། །

[Block 600]
འབྲས་དང་ཏིལ་དང་ནས་དང་མོན་སྲན་སྡེའུ་དང་མོན་སྲན་གྲེའུ་དང་། འབྲུ་གཞན་དང་བཟའ་བ་དང་བཏུང་བ་དག་ནི་གསུམ་པར་འོས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། གསུམ་པར་ཞེས་བྱ་བ་བཟའ་བར་འོས་པ་ཉིད་དོ། །

[Block 601]
གཞིར་གཏོགས་པའི་གོས་ཀྱི་གཞིའོ། །

[Block 602]
གླེགས་བུ་དང་གླེགས་བུ་ཕྱེད་པ་དག་མཉམ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཡང་འདིར་གླེགས་བུ་རྣམས་ཀྱང་སོ་སོ་མཉམ་པ་ཉིད་དང་། གླེགས་བུ་ཕྱེད༌[^539]རྣམས་ཀྱང་ལོགས་ཤིག་ཏུ་མཉམ་པ་ཉིད་ཅེས་བྱ་བ་རྟོགས་པར་བྱའོ། །

[Block 603]
གླེགས་བུ་ཡང་གླེགས་བུ་ཕྱེད་རྣམས་དང་ལྷན་ཅིག་ཚད་མཉམ་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 604]
མཉམ་པ་འདི་ནི་མཛེས་པ་ཉིད་དུ་བྱ་བའི་ཕྱིར་རོ། །

[Block 605]
གཞལ་བའི་ཕྱིར་དེའི་ཚད་ཀྱི་ཆག༌[^540]ཤིང་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི། དེའི་ཚད་ཀྱི་ཞེས་བྱ་བ་ནི། གླེགས་བུ་དང་གླེགས་བུ་ཕྱེད་ཀྱི་ཚད་ལ་དོན་གྱི༌[^541]དབང་གིས་འཆང་བ་འདིའོ། །

[Block 606]
དེ་ལྟར་ཡང་གཞལ་བར་བྱ༌[^542]བའི་ཕྱིར་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་བས་ན་འདི་རྗེས་སུ་གནང་བ་སྟེ། ངེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 607]
གཅིག་གིས་དགོས་པའི་དོན་འགྲུབ་པར་འགྱུར་ན་དེ་ཙམ་འཆང་བ་ལ་ཉེས་བྱས་ཉིད་ནི་མ་ཡིན་ནོ། །

[Block 608]
དེ་ལྟར་ཡང་གཞན་ལས་ཆག༌[^543]ཤིང་ཁོ་ན་བཅང་བར་བྱའོ་ཞེས་གསུངས་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། ཆག༌[^544]ཤིང་བྱ་ཞིང་དེའི་ཚད་ཀྱི་གླེགས་བུ་བྱའོ། །

[Block 609]
གླེགས་བུའི་ཚད་ཀྱི་གླེགས་བུ་ཕྱེད་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 610]
གང་ཞིག་འདིར་ཆག༌[^545]ཤིང་གི་སྒྲ་ལས་དོན་ཐ་དད་པར་ཞེས༌[^546]བྱ་བ་མ་ཡིན་ནོ། །

[Block 611]
གང་གི་ཕྱིར་འདིར་སྲོག་ཤིང་ནི་ཆག༌[^547]ཤིང་དུ་གྱུར་པ་ཉིད་དུ་གསུངས་པ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 612]
གང་དུ་གདོང་གི་ཆག༌[^548]ཤིང་ལས་འདི་ལ་ཤིན་ཏུ་ཆེ་བ་ཉིད་བསྟན་པའི་དོན་དུ་ཆག༌[^549]ཤིང་གི་སྒྲའོ། །

[Block 613]
ཚལ་བུ་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་མཉམ་པ་ཉིད་དུ་བྱའོ། །

[Block 614]
དེའི་ཚད་ཀྱི་ཆག༌[^550]ཤིང་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི། གཞག་པའི་ཕྱིར་ཚལ་བུའི་ཚད་ཀྱི་ཆག༌[^551]ཤིང་བཅང་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ།[^552] །དེའི་ཚད་ནི་སོར་བཞིའོ་ཞེས་བྱ་བ་ལ་དེ་ལ་ཞེས་བྱ་བ་ནི་ཚལ་བུ་ལའོ། །

[Block 615]
བྱ་རོག་གི་མཐོ་གང་ངོ་ཞེས་བྱ་བ་ནི། མཐེ་བོའི་ལོགས་སུ་སོར་མོ་གང་ཡིན་པ་དེའི་དབུས་ཀྱི་ཚིགས་ཀྱི་ལོགས་སྟེངས་སུ་མཐེ་བོའི་ཚིགས་སུ་གཏད་དེ། གང་ཞིག་སོར་བཅུ་གཉིས་པར་གྱུར་པ་ཡིན་པ་དེ་ནི་བྱ་རོག་གི་མཐོ་གང་དང་འདྲ་བར་བརྗོད་པའོ། །

[Block 616]
འདིའི་ཚད་ནི་སོར་བཞི་ཁོ་ན་སྟེ། དེ་བས་ན་དེ་ཉིད་ལ་དེ་རྣམ་པ་གཞན་གྱིས་བསྟན་པའོ། །

[Block 617]
ཆུང་ཚད་ནི་སོར་གཉིས་སམ་ཕྱེད་དང་གསུམ་མམ་མཐེབ་སོར་གཅིག་གོ་ཞེས་བྱ་བ་ནི། སོར་གཉིས་ནི་ཐོབ་པའོ། །

[Block 618]
གང་གི༌[^553]ཕྱིར་ཆུང་བ་ནི་སོར་བཞི་པ་དང་། ཆུང་ཚད་ནི་སོར་ཕྱེད་དང་གསུམ་མོ། །

[Block 619]
དེའི་བར་ནི་འབྲིང་ཚད་དུ་སྟེ་དེའི་བར་ནི་འབྲིང་དུའོ་ཞེས་འབྱུང་ངོ་། །གཞུང་ཁ་ཅིག་ལས་ནི་ཆེ་ཚད༌[^554]ནི་སོར་བཞི་འམ། བྱ་རོག་གི་མཐོ་གང་ངོ་། །ཆུང་ཚད་ནི་སོར་གཉིས་སམ་མཐེབ་སོར་གཅིག་གོ། །

[Block 620]
དེའི་བར་ནི་འབྲིང་ཚད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 621]
སུ་ཞིག་སྦྱོར་བ་ལ་ཐམས་ཅད༌[^555]སྦྱོར་བར་འགྱུར་བ་ཞེས་བྱ་བ་བསྡུས་ཏེ་ཉེ་བར་བཏགས་པ་འདི་བྱས་སོ། །

[Block 622]
ས་ལ་ཆོས་གོས་གདིང་བར་མི་བྱའོ། །

[Block 623]
དེའི་དོན་དུ་གཏན་པ་བྱའོ། །

[Block 624]
ཤིང་ལས་བྱས་པའམ་སྨྱིག་མ་ལས་བྱས་པ་གྲུ་བཞི་པ་རྟོད་པའི༌[^556]ཕྱིར་ཐི་གུ་གཞུག་པའི་བུ་ག་བཏོད་པ༌[^557]ནི་དེ་ཞེས་བྱ་བ་ནི་ཐང་བཅད་ཅིང་བཅིང་བའི་ཕྱིར་ཐ་གུ་གང་ཡིན་པ་དེ་རྟོད་པའི་བུ་ག་བཏོད་པར༌[^558]གྱུར་པ་དེ་ནི་གཏན་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 625]
ཆོས་གོས་ཇི་ཙམ་པར་རོ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་དང་འཚམས་པའི༌[^559]ཚད་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 626]
ཆོས་གོས་ཚད་ཐ་དད་པ་དུ་མ་ཡོད་པས་གཏན་པ་ཡང་དོན༌[^560]གྱིས་འཇུག་པའི་ཕྱིར་ཞེས་བྱ་བ་ནས་སོ། །

[Block 627]
ཡུ་བ་རྩི་ཅན་དང་ཁྲ་བོ་མི་བཅང་ངོ་ཞེས་དུ་མ་བྱ་དགོས་པར༌[^561]རིག་པར་བྱའོ། །

[Block 628]
གྲི་གུས་དྲའོ། །

[Block 629]
དེ་བཅང༌[^562]བར་བྱའོ་ཞེས་བྱ་བ་ལ།

[Block 630 [VERSE]]
དེ་ཞེས་བྱ་བ་ནི་གྲི་གུ་དེའོ། །
བྱ་རོག་གི་མཆུ་ལྟ་བུ་དང་།
བྱ་གག་གི་གཤོག་པ་ལྟ་བུར་རོ། །

[Block 631]
ལྕགས་ལས་བྱས་པ་ལས་གཞན་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི། ལྕགས་ཀྱི་རང་བཞིན་ཁོ་ན་ལས་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 632]
དོན་གྱིས༌[^563]འཇུག་པའི་ཕྱིར་ཞེས་བྱ་བ་བྱས་ནས་སོ། །

[Block 633]
ཡུ་བ་རྩི༌[^564]ཅན་དང༌[^565]ཁྲ་བོ་མི་བཅང་ངོ་ཞེས་བྱ་བ་ནི། ཡུ་བ་མི་བཅང་ངོ་ཞེས་བྱ་བའི་ཚིག་གི་ལྷག་མའོ། །

[Block 634]
སོར་དྲུག་གི་ཚད་ལས་ལྷག་པ་མི་བཅང་ངོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། གྲི་གུ་ནི་གསུམ་སྟེ། ཆེན་པོ་དང་འབྲིང་དང་ཆུང་ངུའོ། །

[Block 635]
ཆེན་པོ་ནི་སོར་དྲུག་གོ། །
--- END BLOCKS ---
