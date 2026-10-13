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
གང་སྒྲུབ་པར་འདོད་པའི་ཆོས་ཀྱི༌[^603]ཁྱད་པར་དུ་བྱས་པའི་ཆོས་ཅན་དེ་ལ་བསྒྲུབ་པར་བྱ་བའི༌[^604]ཆོས་དང་འགལ་བའི་མངོན་སུམ་དང་། རྗེས་སུ་དཔག་པ་དང་། ལུང་དང་། གྲགས་པ་རྣམས་ཏེ། ཆོས་གཞན་གྱིས་མ་བསལ་བའོ། །

[Block 772]
དེ་ལྟར་ན་བསྒྲུབ་པར་བྱ་བ་ཁ་ན་མ་ཐོ་བ་མེད་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 773]
དེ་ལྟ་མ་ཡིན་ན་ནི་དེ་ལྟར་སྣང་བ་སྟེ། དཔེར་ན་སྒྲ་མཉན་དུ་མི་རུང་ངོ་། །བུམ་པ་རྟག་གོ། །

[Block 774]
ཚད་མས་གཞལ་བར༌[^605]བྱ་བའི་དོན་སྒྲུབ་པར་མི་བྱེད་དོ་ཞེས་པ་ལྟ་བུ་དམ་བཅའ་བ་ཙམ་དང་འགལ་བ་དང་། གང་ཡང་ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་རྗེས་སུ་དཔག་པ་ནི་ཡོད་པ་མ་ཡིན་ཞིང་སྒྲར་གྲགས་པ་དང་འགལ་བའི་དོན་སྦྱོར་བ་ནི་རི་བོང་ཅན་ནི་ཟླ་བ་མ་ཡིན་ཏེ་ཡོད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུ་སྟེ། དེ་དག་གིས་ནི་ཆོས་ཀྱི་རང་གི་ངོ་བོ་བསལ་བའི་སྒོ་ཙམ་ཅིག་བསྟན་པ་ཡིན་ནོ། །

[Block 775]
ཕྱོགས་འདིས་ནི་ཆོས་དང་ཆོས་ཅན་གྱི་བྱེ་བྲག་གི་རང་གི་ངོ་བོ་བསལ་བ་ཡང་མཚོན་པར་རིག་པར་བྱ་སྟེ། འདི་ལྟར་དཔེར་ན་ཡན་ལག་ཅན་ནི་ཡན་ལག་ལས་གཞན་མ་ཡིན་ཏེ། སྲང་མཐོ་དམན་གྱི་བྱེ་བྲག་མ་བཟུང་བའི་ཕྱིར་རོ། །

[Block 776]
ཡན་ལག་དང་ཡན་ལག་ཅན་དག་ནི་གཞན་མ་ཡིན་ཏེ། མངོན་སུམ་མ་ཡིན་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 777]
རྫས་ནི་ཡོད་པ་མ་ཡིན་ཏེ། ཡོན་ཏན་གྱི་རྫས་རྣམས་ཀྱི་རྫས་རྫས་མ་ཡིན་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 778]
གཉིས་ཀའི་རང་གི་ངོ་བོའི་བྱེ་བྲག་ནི། དཔེར་ན་སྨྲ་བའི་དོན་ཐམས་ཅད་བརྫུན་ནོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 779]
སྨྲ་བ་ཡོད་མོད་ཀྱིས་ཀྱང་སྨྲས་པ་དང་སྨྲ་བའི་བདག་ཉིད་བརྫུན་པ་ཉིད་དུ་འགྱུར་བའི་ལྟ་ན་ནི་དེའི་སྨྲ་བའི་བདག་ཉིད་དང་ཡང་བརྫུན་པ་ཉིད་གཉིས་ཀ་རྣམ་པ་ཐམས་ཅད་དུ་བསལ་བར་འགྱུར་རོ། །

[Block 780]
དེ་ལྟ་བུ་ནི་གཉིས་ཀའི་རང་གི་ངོ་བོ་བསལ་ཏོ། །

[Block 781]
ཅི་སྟེ་སྨྲ་བའི་བདག་ཉིད་ཀྱི་བརྫུན་པ་ཉིད་བསལ་བ་མ་ཡིན་ནོ་ཞེ་ན། དེ་ལྟ་ན་ནི་གཉིས་ཀའི་བྱེ་བྲག་བསལ་བ་ཡིན་ནོ། །

[Block 782 [HEADING]]
#### རིགས་པ་ཅན་རྣམས་ཀྱི་བསྒྲུབ་བྱ། ^3-1-2-0

[Block 783]
རིགས་པ་ཅན་རྣམས་ན་རེ། བསྒྲུབ་བྱ་སྟོན་ཞེས་པ་འདི་ལ། གྲུབ་པ་མེད་པར་དོན་གྱིས་བྱས། །བསྒྲུབ་བྱ་སྨོས་པས་ནི་གྲུབ་པ་ལོག་པ་ཙམ་དུ་བསྟན་པའི་ཕྱིར་བསྒྲུབ་བྱའི་བྱེ་བྲག་ཉིད་ནི་མ་ཡིན་པར་གནས་སོ། །

[Block 784]
དེ་ལྟ་ན་ནི་རྟགས་དང་དཔེ། །མ་གྲུབ་པ་ཡང་བསྒྲུབ་བྱར་འགྱུར། །

[Block 785]
དཔེར་ན་སྒྲ་རྟག་སྟེ། རེག་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་བློ་བཞིན་ནོ་ཞེས་བྱ་བ་དང་། དེ་བཞིན་དུ་མིག་གིས་གཟུང་བྱ་ཡིན་པའི་ཕྱིར་མི་རྟག་ཅེས་བྱ་བ་འདི་ཡང་བསྒྲུབ་བྱ་བསྟན་པའི་ཕྱིར་དམ་བཅའ་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 786]
འདི་ལ་ཡང་ཅི་ཆོས་བསྒྲུབ་བྱ་ཡིན་ནམ། ཅི་སྟེ་ཆོས་ཅན་ཡིན་ནམ། དེ་སྟེ་གཉིས་ཀ་ཡིན་ཞེས་བརྗོད་པར་བྱའོ། །

[Block 787]
དེ་ལས་ཅིར་འགྱུར་ཞེ་ན། བསྒྲུབ་བྱ་ཆོས་ཡིན་ཆོས་མཐུན་མེད། །གལ་ཏེ་ཆོས་ཅན༌[^606]མི་རྟག་པ་ཉིད་ཙམ་བསྒྲུབ་བྱ་ཡིན་པ༌[^607]ལྟ་ན་བསྒྲུབ་བྱའི་ཆོས་ཀྱི༌[^608]མཐུན་ཞེས་ནི་སྦྱར་དུ༌[^609]མི་བཏུབ་སྟེ། མི་རྟག་པ་ཉིད་ཀྱིས༌[^610]ཆོས་མཐུན་པའི་དངོས་པོ་ཅན་གྱི་དཔེ་མེད་པའི་ཕྱིར་རོ། །

[Block 788]
ཆོས་ཅན་བསྒྲུབ་བྱའི་རྟགས་དོན་མེད། །ཆོས་ཅན་བསྒྲུབ་བྱ་ཡིན་པ༌[^611]ལྟ་ན་ནི་སྒྲ་ནི་གྲུབ་པ་ཡིན་པའི་ཕྱིར་བསྒྲུབ་བྱ་སྒྲུབ་པའི་གཏན་ཚིགས་དགོད་པར་མི་བྱའོ། །

[Block 789]
གལ་ཏེ་གཉིས་ཀ་ཡིན་ན་ནི་སྐྱོན་ཡང་གཉིས་ཀའོ། །

[Block 790]
འདི་ལ་ཡང་བསྒྲུབ་བྱ་བསྟན་པ་ཉིད་དམ་བཅའ་བའོ་ཞེས་ངེས་པ་གོང་དུ་སྦྱོར་བའམ། བསྒྲུབ་བྱ་བསྟན་པ་དམ་བཅའ་བ་ཉིད་དོ་ཞེས་ངེས་པར་བཟུང་བར་འོག་ཏུ་སྦྱོར་གྲང་། དེ་ལས་ཅིར་འགྱུར།

[Block 791]
གོང་དུ་ངོས་བཟུང༌[^612]དོན་མེད་འགྱུར། །ཅིག་ཤོས་ལྟར་ན་འདོད་མི་འགྱུར། །

[Block 792]
གལ་ཏེ་བསྒྲུབ་བྱ་བསྟན་པ་ཉིད་དོ་ཞེས་ངེས་བཟུང་གོང་དུ་སྦྱོར་ན་ནི་སྒྲུབ་བྱེད་དུ་བསྟན་པའི་རྟགས་ལ་སོགས་པ་འཕངས་ཟིན་པའི་ཕྱིར་གོང་དུ་ངེས་བཟུང་བྱས་པ་ལས་དོན༌[^613]མེད་དོ། །

[Block 793]
ཅི་སྟེ་བསྒྲུབ་བྱ་བསྟེན་པ༌[^614]དམ་བཅའ་བ་ཉིད་དོ་ཞེས་ངེས་བཟུང་འོག་ཏུ་སྦྱོར་ན་ནི་རྟགས་ཀྱི་དཔེར་བརྗོད་པའི་དོན་དུ་བསྟན་པ་ཡང་དམ་བཅའ་བར་འགྱུར་བའི་ཕྱིར་དམ་བཅའ་བ་རིགས་པ་དང་མི་ལྡན་ནོ། །

[Block 794 [HEADING]]
#### རྩོད་པ་སྒྲུབ་པའི་བསྒྲུབ་བྱ། ^3-1-3-0

[Block 795]
དེ་བཞིན་བསྒྲུབ་བྱ་བརྗོད་པ་ལའང་། །དེ་བཞིན་ཏེ་རིགས་པ་ཅན་རྣམས་ལ་སྐྱོན་བརྗོད་པ་དེ་བཞིན་དུ་རྩོད་པ་སྒྲུབ་པ་ལ་ཡང་། རྟགས་བསྒྲུབ་པར་བྱ་བ་དང་། དཔེ་ལྟར་སྣང་བ་བརྗོད་པར་ཡང་དམ་བཅའ་བར་ཐལ་བར་འགྱུར་རོ། །

[Block 796]
གལ་ཏེ་དེ་ནི་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ལ་ནི། ཕྱོགས་ལྷག་ཕྱིར་ན་སྲིད་མ་ཡིན། །རྩོད་པ་བསྒྲུབ་པ༌[^615]ནི་བསྒྲུབ་བྱར་བརྗོད་པ་ཙམ་དམ་བཅར༌[^616]འགྱུར་བ་མ་ཡིན་གྱི་འདི་ལྟར་ཕྱོགས་བསྒྲུབ་བྱ་ཡིན་ནོ། །

[Block 797]
ཕྱོགས་དེ་ཅི་ཞིག་རྣམ་པར་དཔྱད་པའི་འདོད་པའི༌[^617]དོན་ཏེ། དེ་ཕྱོགས་ཡིན་པས་བསྒྲུབ་བྱ་ཙམ་དེ་རྟགས་མ་གྲུབ་པ་ལ་སོགས་པར་བརྗོད་པ་ཡང་དམ་བཅའ་བར་འགྱུར་རོ་ཞེས་པའི་སྐྱོན་ནི་མེད་དོ་ཞེ་ན་སྐྱོན་ཇི་ལྟར་ན་མེད་དེ་དེ་ལ་ཡང་།

[Block 798 [VERSE]]
རྣམ་པར་དཔྱད་པའི་འདོད་པ་འདི། །
མི་འདོད་པ་ལས་ལོག་པ་ཙམ། །

[Block 799]
དེ་ནི་མི་འདོད་པ་ལོག་པ་ཙམ་ཡིན་པར་བས་སོ། །

[Block 800]
དེས་ན་ཇི་ལྟར་བསྒྲུབ་བྱའི་བྱེ་བྲག་གོ་བར་བྱེད། རྣམ་པར་དཔྱད་པའི་འདོད་པ་ནི་འདི་རྟགས་ཡིན་ནམ་མ༌[^618]ཡིན་ཞེས་མིང་གི་གཟུང་བྱ་ལ་ཡང་དཔྱད་པར་ནུས་པའི་ཕྱིར་དེ་ཡང་དམ་བཅའ་བར༌[^619]བརྗོད་པ་ཡིན་ནོ། །

[Block 801]
བསྒྲུབ་བྱ་གཟུགས་བརྙན་དང་བཅས་པ་བསྟན་ཏོ། །

[Block 802 [HEADING]]
#### དམ་བཅའ་བ་གཏན་ཚིགས་དང་འགལ་བ། ^3-1-4-0

[Block 803]
རིགས་པ་ཅན་རྣམས་ན་རེ་དམ་བཅའ་བ་གཏན་ཚིགས་དང་འགལ་བ་དང་དམ་བཅའ་དང་འགལ་བ་ཞེས་བྱ་བ་དེ་དག་དམ་བཅའ་བའི་སྐྱོན་ཡིན་ཏེ། དཔེར་ན་སྒྲ་རྟག་པ་དེ༌[^620]ཐམས་ཅད་མི་རྟག་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ་ཞེས་ཟེར་རོ། །

[Block 804]
དམ་བཅའ་གཏན་ཚིགས་དང་འགལ་བ། །དམ་བཅའི་སྐྱོན་ཞེས་རིགས་པ་མིན། །

[Block 805]
འདིར་ནི་དམ་བཅའ་བ་དང་གཏན་ཚིགས་སུ་འགལ་ལོ་ཞེས་པ་གཉིས་ཀ་རིགས་པ་མ་ཡིན་ཏེ། ཇི་ལྟར་ཞེ་ན།

[Block 806]
ལེགས་པར་མ་བསླབས་པ་རྣམས་ཀྱིས། །དེ་ནི་ཆོས་མི༌[^621]མཐུན་དཔེས་བརྗོད། །

[Block 807]
གང་གཏན་ཚིགས་ཀྱི་སྦྱོར་བ་འདི་དམ་བཅའ་བ་དང་འགལ་བར་བརྗོད་པ་ནི་རིགས་པ་མ་ཡིན་ཏེ། འདི་ལྟར་ཆོས་མི་མཐུན་པའི༌[^622]དཔེའི་སྦྱོར་བ་ཉིད་ཀྱིས་ཡིན་པས་ནའོ། །

[Block 808]
དེར་ནི་འདི་ལྟར་སྦྱོར་བ་བྱས་ནས་མཛེས་པར་འགྱུར་རོ། །

[Block 809]
སྒྲ་རྟག་སྟེ་ཐམས་ཅད་མི་རྟག་པའི་ཕྱིར་ཞེས་པ་ནི་ཐམས་ཅད་མ་ཡིན་པས༌[^623]མེད་པའི་ཕྱིར་ཞེས༌[^624]དོན་ནོ། །

[Block 810]
དེ་ལྟ༌[^625]ན་ནི་ཆོས་མི་མཐུན་པའི་དཔེས་བསྒྲུབ་བྱ་མེད་པ་ལས་གཏན་ཚིགས་མེད་པར་བསྟན་པ་ཡིན་ནོ། །
--- END BLOCKS ---
