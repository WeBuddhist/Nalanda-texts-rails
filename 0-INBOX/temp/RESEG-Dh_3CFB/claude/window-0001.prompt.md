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
[Block 36]
དེ་དག་གི་གཏན་ཚིགས་ཡིན་ཏེ། དེ་དག་གི་འབྲས་བུ་ཉིད་དུ་ངེས་པའི་ཕྱིར་རོ། །

[Block 37]
གང་དག༌[^21]དེ་དག་མེད་ན་མི་འབྱུང་བ་དེ་དག་ཁོ་ནས་ཡིན་ནོ། །

[Block 38]
གལ་ཏེ་ཆ་ཤས་ཀྱིས་བསྐྱེད་པར་བྱ་བ་དང་། སྐྱེད་པ་ཡིན་པར་ཐལ་བར་འགྱུར་རོ་ཞེ་ན། མ་ཡིན་ཏེ། དེས་བསྐྱེད་པར་བྱ་བའི་ཁྱད་པར་དང་། རྟགས་ཀྱི་བྱེ་བྲག་གི་ཁྱད་པར་ཅན་གྱི་སྤྱི་རྣམས་གཟུང་ན་ཡིན་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 39]
སྤྱི་ཁྱད་པར་དུ་མ་བྱས་པ་བརྗོད་པར་འདོད་ན་ནི་འཁྲུལ་པའི་ཕྱིར་མི་འདོད་དོ། །

[Block 40]
རང་བཞིན་ཡོད་ཙམ་དང་། འབྲེལ་པ་ཅན་གྱི་ངོ་བོ་ཡང་གཏན་ཚིགས་ཡིན་ཞེས་བྱ་བར་སྦྱར་ཏེ། གཏན་ཚིགས་ཀྱི་དེའི་བདག་ཉིད་ནི་དེ་ཙམ་དང་འབྲེལ་པ་ཅན་ཁོ་ནའི་ཕྱིར་རོ། །

[Block 41]
གཞན་ལ་རག་ལས་པའི་ནི་མ་ཡིན་ཏེ། དེ་ཡོད་ན་ཡོད་པར་མ་གྱུར་པའི་ཕྱིས་འབྱུང་བ་ནི་ངེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 42]
རྒྱུ་རྣམས་ནི་འབྲས་བུ་ལ་འཁྲུལ་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 43]
ཚད་མ་རྣམས་ནི་མི་འཇུག་པ་མི་དམིགས་པ་ཡིན་ཏེ། མེད་ལ་མི་འཇུག་འབྲས་བུ་ཅན། ཡོད་པའི་ཤེས་པ་དང་། སྒྲ་དང་ཐ་སྙད་དགག་པའི་འབྲས་བུ་ཅན་ཡིན་ཏེ། དེ་དག་ནི་དམིགས་པ་སྔོན་དུ་འགྲོ་བ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 44]
འདི་ནི་ཡོད་པ་དང་མེད་པ་དགག་པ་དང་སྒྲུབ་པའི་གཏན་ཚིགས་དག་གི་འདྲ་བའི་ངོ་བོ་ཡིན་ཏེ། འདི་ལྟར་དམིགས་པ་ཉིད་ཡོད་པ་མ་ཡིན་ཏེ། དངོས་པོ་རུང་བའི་མཚན་ཉིད་ཡིན་པའམ། ཡང་ན་དེའི་རྟེན་ཅན་གྱི་ཤེས་པ་འཇུག་པ་ཡིན་ཏེ། དེ་ལས་ཡོད་པའི་ཤེས་པ་དང་སྒྲ་དང་ཐ་སྙད་འཇུག་པའི་ཕྱིར་རོ། །

[Block 45]
མི་དམིགས་པ་ནི་མེད་པ་རྣམས་ཀྱི་མེད་པ་ཡིན་ནོ། །

[Block 46 [VERSE]]
གཏན་ཚིགས་བྱེ་བྲག་ལ་ལྟོས་ནས། །
ལ་ལ་མེད་ཤེས་འབྲས་བུ་ཅན། །
གཏན་ཚིགས་ནི་མི་དམིགས་པའོ། །

[Block 47]
དེའི་བྱེ་བྲག་ནི་ཁྱད་པར་ཏེ། དམིགས་པའི་མཚན་ཉིད་ཀྱིར་འགྱུར་བའི༌[^22]ཡོད་པ་ཅན་ཡིན་ནོ། །

[Block 48]
འདིར་མི་དམིགས་པའི་རྟགས་ཀྱིས་མེད་པ་བསྒྲུབ་པར་བྱ་བ་ཡིན་ན། དམིགས་པ་མེད་པ་ཡང་མི་དམིགས་པ་གཞན་གྱིས༌[^23]བསྒྲུབ་པར་བྱ་དགོས་པས་ཐུག་པ་མེད་པར་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རྟོགས་པར་བྱེད་པ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 49]
འོན་ཏེ་དམིགས་པ་མེད་པར་ཡང་མི་དམིགས༌[^24]པར་འགྱུར་ན་ནི། དེ་བཞིན་དུ་ཡོད་པ་མེད་པར་ཡང་འགྱུར་ཏེ། མི་དམིགས་པ་དོན་མེད་པ་ཡིན་ནོ། །

[Block 50]
ཅི་སྟེ་གཞན་དམིགས་པས་མི་དམིགས་པ༌[^25]འགྲུབ་པས་མི་དམིགས་པ་མངོན་སུམ་གྱིས་གྲུབ་པོ་ཞེ་ན། དེ་བཞིན་དུ་གཞན་ཡོད་པས་ཀྱང་མེད་པ་ཅི་སྟེ་མི་འགྲུབ། གང་གི་ཚེ་མེད་པ་དག་གི་མེད་པ་དེ་ལྟ་བུའི་མི་དམིགས་པ་ཁོ་ན་ཡིན་པ་དེའི་ཚེ་ནི་ཡུལ་གྲུབ་ཏུ་ཟིན་ཀྱང་རྨོངས་པས་ཡུལ་ཅན་ཤེས་པ་དང་། སྒྲ་དང་ཐ་སྙད་དག་ཁོང་དུ་མི་ཆུད་པ་ཡུལ་རབ་ཏུ་བསྟན་པས་བརྡ་ལ་འཇུག་པར་བྱེད་དེ། དཔེར་ན་འདི་ནི་བ་ལང་ཡིན་ཏེ་ལྐོག་ཤལ་ལ་སོགས་པ་འདུས་པའི་བདག་ཉིད་ཡིན་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 51]
དེ་ལྟ་ཡིན་དང་དཔེ་མ་གྲུབ་པར་རྒོལ་བ་ཡང་བསལ་བ་ཡིན་ནོ། །

[Block 52]
ཡུལ་རྟོགས་སུ་ཟིན་ཀྱང་ཡུལ་ཅན་མ་རྟོགས་པ་དག་སྣང་བའི་ཕྱིར་རོ། །

[Block 53]
དེ་ལྟར་མི་དམིགས་པ་འདི་གཉིས་ནི་རང་དང་བཟློག་པའི་རྒྱུ་མེད་པ་དང་། ཡོད་པ་དག་གི་ཕྱིར་ཡོད་པའི་ཐ་སྙད་དགག་པའི་འབྲས་བུ་ཅན་ཉིད་དུ་འདྲ་སྟེ། གཅིག་ལ་ནི་ཐེ་ཚོམ་ཡོད་པའི་ཕྱིར་ལ། གཞན་ལ་ནི་བཟློག་པའི་ཕྱིར་རོ། །

[Block 54]
དེ་ལ་དང་པོ་ནི་ཡོད་པའི་ཐ་སྙད༌[^26]དགག་པར་དགོངས་པའི་ཕྱིར་ཚད་མར་བཤད་ཀྱི། ལྡོག་པ་མཐོང་བ་ལ་སོགས་པ་ལ་ཉེ་བར་སྦྱོར་བ་ནི་མ་ཡིན་ཏེ། ཐེ་ཚོམ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 55]
གཉིས་པ་ནི་དེ་ལ་ཚད་མ་ཡིན་ཏེ། ངེས་པའི་འབྲས་བུ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 56 [VERSE]]
དེ་ཡང་སྦྱོར་བའི་བྱེ་བྲག་གིས། །
འགལ་དང་འབྲས་བུ་དག་གྲུབ་དང་། །
རྒྱུ་དང་ངོ་བོར་བལྟར་རུང་བའི། །
བདག་ཉིད་དག་ནི་མ་གྲུབ་པའི། །
མེད་དོན་ཅན་མི་དམིགས་རྣམ་བཞི། །

[Block 57]
དགག་པ་གང་ཇི་སྙེད་པ་ཐམས་ཅད་ནི་མི་དམིགས་པས་ཡིན་ནོ། །

[Block 58]
འདི་ལྟར་དེ་ནི་རྣམ་པ་གཉིས་ཀྱིས་བྱེད་དེ། འགའ་ཞིག་སྒྲུབ་པས༌[^27]སམ། དགག་པས་སོ། །

[Block 59]
བསྒྲུབས༌[^28]ན་ནི་འགལ་བའམ། མི་འགའ་བ་བསྒྲུབ་པར༌[^29]འགྱུར་ཏེ། མི་འགལ་བ་བསྒྲུབས༌[^30]ན་ནི་ལྷན་ཅིག་ཡོད་པར་འགལ་བ་མེད་པའི་ཕྱིར་བཀག་པ་མ་ཡིན་ནོ། །

[Block 60]
འགལ་བ་ཡང་མི་དམིགས་པ་མེད་པར་འགལ་བ་མི་རྟོགས་ཏེ། འདི་ལྟར་རྒྱུ་མ་གཏུགས་པ་ཅན་འབྱུང་བ་གཞན་ཡོད་ན་མེད་པའི་འགལ་བར་རྟོགས་ལ། དེ་ཡང་མི་དམིགས་པ་ལས་ཡིན་ནོ། །

[Block 61]
ཕན་ཚུན་དམིགས་པ་སྤངས་ཏེ། དམིགས་པའི་མཚན་ཉིད༌[^31]ཀྱང་འགལ་བ་ཡིན་ཏེ། རྟག་པ་དང་མི་རྟག་པ་བཞིན་ནོ། །

[Block 62]
དེ་ལ་ཡང་གཅིག་དམིགས་པས་གཞན་མི་དམིགས་པ་ཁོ་ནར་བརྗོད་དོ། །

[Block 63]
དེ་ལྟ་མ་ཡིན་ན་དམིགས་པ་མ་བཀག་པ་ཅན་མེད་པ་མི་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 64]
གཅིག་བཀག་པས་གཞན་མེད་པར་གྲུབ་པ་ལ༌[^32]ནི་མི་དམིགས་པ་གྲུབ་པ་ཁོ་ན་ཡིན་ཏེ། དགག་པ་ནི་མི་དམིགས་པའི་ངོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 65]
དོན་གཞན་དགག་པ་དེ་ལ་ཡང་རྒྱུ་དང་འབྲས་བུ་དག་གམ། གཉི་ག་མ་ཡིན་པ་ཞིག་ཡིན་ཏེ། དེ་ལ་གཉིས་ཀ་མ་ཡིན་པ་ནི་འབྲེལ་པ༌[^33]མེད་པའི་ཕྱིར་ཏེ། དེ་མེད་ན་གཞན་མེད་པར་འགྱུར་རོ། །ཞེས་བྱ་བ་དེར་ལྟ་ག་ལ་འགྱུར། འབྲས་བུ་མི་དམིགས་ཀྱང་། རྒྱུ་ནི་གདོན་མི་ཟ་བར་དེ་དང་ལྡན་པ་མ་ཡིན་པས་དེ་མེད་པར༌[^34]ལྟ་ག་ལ་འགྱུར། དེའི་ཕྱིར༌[^35]རྒྱུ་མི་དམིགས་པ་ཁོ་ན་མེད་པ་གོ་བར་བྱེད་པ་ཡིན་ནོ། །

[Block 66]
རང་བཞིན་མི་དམིགས་པ་ནི་རང་མེད་པ་ཁོ་ན༌[^36]ཡིན་ཏེ། དེ་ལ་ནི་ཡུལ་ཅན་སྒྲུབ་པར་བྱེད་པ་འབའ་ཞིག་ཏུ་ཟད་དེ། [^37]འདི་ལ་ཡང་གང་གི་ཚེ་ཁྱབ་པར་བྱེད་པའི་ཆོས་མི་དམིགས་པས་ཁྱབ་པར་བྱ་བ་མེད་པར་སྟོན་པ་དེའི་ཚེ་ནི་མེད་པ་ཡང་ཡིན་ནོ། །

[Block 67]
དགག་པའི་ཡུལ་ཅན་གྱི་མི་དམིགས་པ་འདི་ནི་སྦྱོར་བའི་བྱེ་བྲག་གིས་རྣམ་པ་བཞི་ཡིན་ཏེ། འགལ་བ་གྲུབ་པས་ནི་དཔེར་ན་འདི་ནི༌[^38]གྲང་བའི་རེག་པ་མེད་དེ། མེ་ཡོད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 68]
འདིས་ནི་ཁྱབ་པར་བྱེད་པ་འགལ་བ་གྲུབ་པ་ཡང་བཤད་པར་རིག་པར་བྱ་སྟེ། དཔེར་ན་འདི་ན་བ་མོའི་རེག་པ་མེད་དེ། མེ་ཡོད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 69]
འགལ་བའི་འབྲས་བུ་གྲུབ་པས་ནི། དཔེར་ན་འདི་ན་གྲང་བའི་རིག་པ༌[^39]མེད་དེ་དུ་བ་ཡོད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 70]
རྒྱུ་མ་གྲུབ་པས་ནི༌[^40]དཔེར་ན་འདི་ན་དུ་བ་མེད་དེ༌[^41]མེད་པའི་ཕྱིར་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 71]
རང་བཞིན་མ་གྲུབ་པས་ནི་དཔེར་ན། འདི་ན་དུ་བ་མེད་དེ༌[^42]མི་དམིགས་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 72]
འདིས་ནི་ཁྱབ་པར་བྱེད་པའི་རང་བཞིན་མ་གྲུབ་པ་ཡང་བཤད་དེ། དཔེར་ན་འདི་ན་ཤིང་ཤ་པ་མེད་དེ་ཤིང་མེད་པའི་ཕྱིར་རོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 73]
མེད་པ་སྒྲུབ་པའི་མི་དམིགས་པ་འདི་ཐམས་ཅད་ལ་ཡང་བལྟར་རུང་བའི་བདག་ཉིད་དག་ཁོ་ན་དེ་དག་དང་། འགལ་བ་གྲུབ་པ་དང་མ་གྲུབ་པར་རིག་པར་བྱ་སྟེ། གཞན་དག་ལ་ནི་མེད་པ་དང་འགལ་བ་མི་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 74]
གལ་ཏེ་འགལ་བའི་འབྲས་བུ་དམིགས་པས་ཀྱང་མེད་པ་འགྲུབ་ན། དེའི་རྒྱུ་དམིགས་པས་ཅི་སྟེ་འགྲུབ་པར་མི་འགྱུར་ཞེ་ན།

[Block 75 [VERSE]]
དེ་དང་འགལ་བའི་རྒྱུ་མཚན་ནི། །
དམིགས་པ་སྦྱོར་བ་གང་ཡིན་ཏེ། །
རྒྱུ་མཚན་དག་ནི་འགལ་བ་ཉིད། །
མེད་ན་འཁྲུལ་པ་ཅན་ཡིན་ཏེ། །
--- END BLOCKS ---
