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
གང་དུ་རྗེས་དཔག་ལ་སོགས་འདི། །བཀག་པ་དེ་བཞིན་དེ་ཡང་བཀག །

[Block 737]
འདིར་རང་གི་འདོད་པ་རྗེས་སུ་དཔག་པ་ལ་སོགས་པ་ཅུང་ཟད་ཀྱང་བསྒྲུབས་པ་མེད་དོ།[^579] །

[Block 738]
འབྲེལ་བ་གཞན་མ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 739]
འདིར་ཅུང་ཟད་བརྗོད་པ་ནི་བྱེ་བྲག་པའི་འདོད་པ་ཁ་ཅིག་ལས་སོ། །

[Block 740]
དེས་ན་དེ་བཀག་པ་བཞིན༌[^580]དུ་འདི་ཡང༌[^581]བཀག་པར་རིག་པར༌[^582]བྱའོ། །

[Block 741 [HEADING]]
#### དོན་གྱི་གོ་བ། ^2-6-2-0

[Block 742]
དོན་གྱི་གོ་བ་གཉིས་ཀ་ལ་འགག་པར༌[^583]བརྗོད་པར་བྱ་སྟེ། དོན་གོ་རྣམས་ནི༌[^584]མཐའ་གཅིག་ཏུ།[^585] །ངེས་པ་དང་མཐའ་གཅིག་ཏུ་མ་ངེས་པའོ། །

[Block 743]
དེ་ལ་གང་མཐའ་གཅིག་ཏུ་ངེས་ཏེ། རྗེས་དཔག་གང་དུ་མཐའ་གཅིག་ཏུ་ངེས་པ་ཅན་གྱི༌[^586]གོ་བ་ནི་དཔེར་ན་དེ་འཚོད་པ་ལས་སྣོད་དང་རྟེན་ལ་སོགས་པའི་དོན་འཛིན་པ་ལྟ་བུ་སྟེ། དེ་ནི་འཚོད་པའི་རྟགས་ཉིད་ལས་ཁོང་དུ་ཆུད་པར་བྱེད་པའི་ཕྱིར་རྗེས་སུ་དཔག་པ་ལས་ཐ་དད་པ་མ་ཡིན་ནོ། །ཅིག་ཤོས་བརྫུན། མཐའ་གཅིག་ཏུ་མ་ངེས་པ་ཅན་ཉིད་ཀྱི་དོན་གྱིས་གོ་བས༌[^587]ནི་ཚད་མ་ཉིད་མ་ཡིན་ཏེ། ཐེ་ཚོམ་གྱི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 744]
དཔེར་ན་རྩོལ་བ་ལས་བྱུང་བའི་ཕྱིར་མི་རྟག་གོ་ཞེས་བརྗོད་པ་ལས་རྩོལ་བ་ལས་མ་བྱུང་བའི་ཕྱིར་རྟག་ཅེས་པ་མ་ངེས་པ་ཡིན་པ་བཞིན་ནོ། །

[Block 745 [HEADING]]
#### དངོས་པོ་མེད་པའི་ཚད་མ། ^2-6-3-0

[Block 746]
གང་འདི་སྐད་དུ་ནག་པ་ཁྱིམ་ན་མེད་པ་ལས་ཕྱི་རོལ་ན་ཡོད་པར་མཚོན་པར་བྱེད་པ་ནི་དངོས་པོ་མེད་པའི་ཚད་མ་ཉིད་དོ་ཞེས་བརྗོད་པ་དེ་ལ།

[Block 747 [VERSE]]
ནག་པ་ཁྱིམ་ན་མེད་པ་ལས། །
ཕྱི་ན་ཡོད་པ་མཚོན་པ་མིན། །
ཁྱིམ་གྱི་སྒྲ་ཡི་དོན་ལས་འདིར། །
ཕྱི་ན་ཡོད་པར་རབ་ཏུ་རྟོགས། །

[Block 748]
ནག་པ་ཁྱིམ་ན་མེད་ཅེས་བྱ་བ་འདི་ལ་ཁྱིམ་གྱི་སྒྲའི་སྦྱོར་བ་ཉིད་ལས་ནག་པ་ཕྱི་རོལ་ན་ཡོད་པར་དོན་གྱིས་གོ་བ༌[^588]ཡིན་གྱི། མེད་པ་ལས་ནི་མ་ཡིན་ནོ། །

[Block 749]
གལ་ཏེ་ཁྱིམ་དང་ཕྱི་རོལ་གཉིས་ཀ་ན༌[^589]མེད་ན་ནི་མེད་དོ་ཞེས་བྱ་བ་ཙམ་ཉིད་བརྗོད་པར་འགྱུར་རོ། །

[Block 750]
དེའི་ཕྱི་རོལ་དོན་གྱི་གོ་བ་ཉིད་ནི་དངོས་པོ་མེད་པའི་ཚད་མ་གཞན་མ་ཡིན་ནོ། །

[Block 751]
གཉེན་པོའི་ཕྱོགས་མ་གྲུབ་པ་ལས། །ཕྱོགས་གྲུབ་པ་རུ་བརྗོད་པ་ཡིན། །

[Block 752]
གང་དུ་གྲངས་ཅན་པ་རྣམས་ཀྱིས༌[^590]གཞན་གྱི་ཕྱོགས་བཀག་ནས་རང་གི་ཕྱོགས་བསྒྲུབ་པར༌[^591]འདོད་པ༌[^592]ཐལ་བར་འགྱུར་པ་སེལ་བ་འདི་ཡང་སེལ་བ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 753]
རང་གི་དོན་གྱི་རྗེས་སུ་དཔག་པ་ངེས་པར་བསྟན་ཏོ། །

[Block 754]
ཚད་མ་ཀུན་ལས་བཏུས་པ་ལས་རང་གི་དོན་གྱི་རྗེས་སུ་དཔག་པ་སྟེ་ལེའུ་གཉིས་པའོ།། །།

[Block 755 [HEADING]]
## གཞན་གྱི་དོན་གྱི་རྗེས་སུ་དཔག་པའི་ལེའུ། ^3-0

[Block 756]
གཞན་དོན་རྗེས་སུ་དཔག་པ་ནི། །རང་གི༌[^593]མཐོང་དོན་རབ་གསལ་བྱེད། །

[Block 757]
ཇི་ལྟར་རང་ལ༌[^594]ཚུལ་གསུམ་པའི་རྟགས་ལས་རྟགས་ཅན་གྱི་ཤེས་པ་སྐྱེས་པ་དེ་བཞིན་དུ་གཞན་ལ་རྟགས་ཅན་གྱི་ཤེས་པ་བསྐྱེད་པར་འདོད་ནས་ཚུལ་གསུམ་པའི་རྟགས་བརྗོད་པ་ནི་གཞན་གྱི་དོན་གྱི་རྗེས་སུ་དཔག་པ་སྟེ། རྒྱུ་ལས་འབྲས་བུ་བརྟགས་པའི༌[^595]ཕྱིར་རོ། །

[Block 758]
འདིར་ཡང་ཚུལ་གང་ཡང་རུང་བ་ཅིག༌[^596]མ་སྨྲས་ན་ཡང་མ་ཚང་བ་བརྗོད་པར་འགྱུར་རོ། །

[Block 759 [HEADING]]
### བསྒྲུབ་བྱ་བསྟན་པ། ^3-1-0

[Block 760]
གལ་ཏེ་རྗེས་སུ་དཔག་པར་བྱ་བ་སྟོན་པ་ནི། །དམ་བཅའ་བ༌[^597]བྱ་སྟེ། རྟོག་གེའི་བསྟན་བཅོས་རྣམས་སུ་གཞན་གྱི་དོན་གྱི༌[^598]རྗེས་སུ་དཔག་པ། དགོད་པ་དེ་ཇི་ལྟར་ཡིན་ཞེ་ན། དེ་ཉིད་དྲི་བར་བྱའོ། །

[Block 761]
ཁོ་བོ་ཅག་ནི།

[Block 762 [HEADING]]
#### དཔག་བྱ་བསྟན་པ། ^3-1-1-0

[Block 763 [VERSE]]
དེ་ལ་དཔག་བྱ་བསྟན་པ་ནི། །
རྟགས་ཀྱི་དོན་གྱི་ཡུལ་དུ་འདོད། །

[Block 764]
ཡན་ལག་རྣམས་ནས་གང་རྗེས་སུ་དཔག་པར་བྱ་བ་བསྟན་པ་དེ༌[^599]ནི་ཁོ་བོ་ཅག་གི་སྒྲུབ་བྱེད་ཉིད་དུ་མི་འདོད་དེ། །དེ་ཉིད་ཐེ་ཚོམ་སྐྱེད་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 765]
འོན་ཀྱང་རྟགས་ཀྱི་དོན་དུ་ཡུལ་བསྟན་པའི་ཕྱིར་དེ་ནི་དེས་བསྒྲུབ་པར་བྱའོ། །

[Block 766]
དེ་ཡང་། རང་གི་ངོ་བོ་དང་ཉིད་ལྡན།[^600] །རང་དང་འདོད་འགྱུར། རང་གི་ངོ་བོ་ཁོ་ན་ཞེས་བྱ་བ་ནི་བསྒྲུབ་པར་བྱ་བའི་ངོ་བོས༌[^601]ཡིན་གྱི་གྲུབ་པ་ལས་སྒྲུབ་པའི་ངོ་བོས་ནི་མ་ཡིན་ནོ། །

[Block 767]
དེ་བཞིན་དུ་རྟགས་མ་གྲུབ་པ་དང་། དཔེ་ལྟར་སྣང་བ་དག་ཀྱང་ཡོངས་སུ་སྤངས་པར་བརྗོད་པ་སྟེ། དེ་དག་སྒྲུབ་པར་འོས་པའི་ངོ་བོར༌[^602]བརྗོད་པར་མི་བྱའོ། །

[Block 768]
རང་དང་འདོད་འགྱུར་ཞེས་སྨོས་པ་འདིས་ནི་རང་གི་བསྟན་བཅོས་ལ་ལྟོས་ནས་ཁས་བླངས་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 769]
དེ་ཡང་མ་བསལ་བའོ། །

[Block 770 [VERSE]]
མངོན་སུམ་དོན་དང་རྗེས་དཔག་དང་། །
ཡིད་ཆེས་གྲགས་པས་རང་རྟེན་ལའོ། །

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
--- END BLOCKS ---
