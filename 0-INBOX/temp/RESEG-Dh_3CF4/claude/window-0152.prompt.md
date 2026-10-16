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
[Block 5321]
ཁ་ཅིག་ནི་ཉེས་ཀྱང་ལེགས་པར་མཐོང༌[^3408]ཞེས་བྱ་བ༌[^3409]སྟེ། དེས་ན་དེའི་ཕྱིར་མ་བརྟགས་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 5322]
ཡུལ་ཅི་ཞིག་ལ་མ་བརྟགས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ། གཏན་ཚིགས་ཁྱད་པར་ཅན་ལ་སྟེ། ཁྱད་པར་གྱི་གཏན་ཚིགས་དག་ནི་གཏན་ཚིགས་ཁྱད་པར་ཅན་དག་སྟེ་དེ་ལའོ། །

[Block 5323]
དགོས་པའི་དོན་ཉིད་ཅེས་བྱ་བ་ནི། དེའི་དངོས་པོ་ཉིད་ཡིན་པས་དགོས་པའི་དོན་ཉིད་དོ། །

[Block 5324]
དགོས་པའི་དོན་ཡོད་པར་བརྟགས་པ་ཉིད། གཏན་ཚིགས་ཁྱད་པར་གྱིས་ཏེ། དེ་ལྟར་བརྟག་པ་བྱས་ན་ནི། དགོས་པའི་དོན་རྟོགས་པ་ཉིད་དུ་འགྱུར་ཞིང་ཉེས་པ་ཡང་ཉེས་པ་ཉིད་དུ་རྟོགས་སོ། །

[Block 5325]
ལེགས་པར་ཞུགས་ནས་ནི་ཞེས་བྱ་བ་ནི་ཆོས་ཁྲིམས་ལས་བཤད་པ་བཞིན་དུའོ། །

[Block 5326]
བསྟན་ངག༌[^3410]ལམ་དུ་ཞེས་བྱ་བ་ནི་ལུགས་ཀྱི་བསྟན་བཅོས་ཀྱི་ཚུལ་ཀྱིས་སོ། །

[Block 5327]
ཆོས་ཁྲིམས་དང་ལུགས་ཀྱི་བསྟན་བཅོས་ཀྱི་ཚུལ་གྱིས༌[^3411]བཀའ་ཁྲིམས་ཀྱི་བྱ་བས་ནན་ཏུར་བྱ་བ་དང་། ཕན་གདགས་པར་བྱ་བ་ལ་རྗེས་སུ་གཟུང་བར་བྱས་ན་དེ་དག་ཉིད་ཀྱི་ཆོས་དང་། སྲིད་དང་། བདེ་བར་འགྱུར་རོ། །

[Block 5328]
བཏུལ་ནས་ཞེས་བྱ་བ་ནི་གང་གི་ཕྱིར། དེ་ལྟར་བྱ་བ་དག་ལེགས་པར་བརྟགས་པའི་རྒྱུས་ཆོས་དང་། སྲིད་དང་། བདེ་བའི་དོན་ཉམས་པར་མི་འགྱུར་བས་དེའི་ཕྱིར་རོ། །

[Block 5329]
གྲགས་པར་གྱུར་པ་ཞེས་བྱ་བ་ནི། ཉེས་བ་མེད་པའི་རིགས་པ་སྟེ། གྲགས་པ་མ་ཡིན་པའི་རྒྱུས་སོ། །

[Block 5330]
ཉེས་པ་ཅིར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་སྨྲས་པ། ནགས་ཚལ་ན་གཏམ་ངན་པ་འཕེལ་ཞེས་བསྟན་པ་ཡིན་ཏེ། རང་གི་སྐྱེས་བུ་བྱེད་པའི་བསྲུང་བ་ཉམས་པར་སྟོན་ཏོ། །

[Block 5331]
ཁྱོད་ཀྱི་མཐུ་ཡིས་བསྲུང་བ༌[^3412]ཞེས་བྱ་བ་ནི། བདག་པོ་གཞན་མ་ཡིན་པ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5332]
ཕན་པའི་ཚུལ་མེད་ཅེས་བྱ་བ་ནི། འཇིག་རྟེན་ཕ་རོལ་པ༌[^3413]ལ་ཕན་པའོ། །

[Block 5333]
དམ་པས་སྨད་པ་ནི་འཇིག་རྟེན་འདིའི་གྲགས་པ་མ་ཡིན་པའོ། །

[Block 5334]
དེ་བས་རྣམ་པར་བརྟགས་པའི་ལམ་དུ་འཇུག་པའི་རིགས། །ཞེས་གང་བཤད་པ་ལ། ཇི་ལྟར་རྣམ་པར་བརྟགས་པའི་ལམ་དུ་འཇུག་པར་བྱ་ཞེ་ན། སྨྲས་པ། སྲུང༌[^3414]མ་ཉུག༌[^3415]རུམ་བཅས་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། ལྷགས་པ་ལ་ཞེས་བྱ་བ་འདིས་ནི། བདག་ཉིད༌[^3416]བུད་མེད་ལ་འགྲོ་བ་བསལ་ཏོ། །

[Block 5335]
བདག་གི་ཞེས་བྱ་བ་ནི་རབ་ཏུ་བྱུང་པའོ། །

[Block 5336]
གནས་ཞེས་བྱ་བ་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི་ཐུན་མོང་དུ་སྟོན་ཏེ། [^3417]སྔོན་མ་མཐོང་བར་ཡང་འོང་བས་སོ། །

[Block 5337]
སྲུང༌[^3418]མ་ཉུག༌[^3419]རུམ་ཞེས་བྱ་བ་ནི་དབེན་པ་མ་ཡིན་པ་ཉིད་དུ་བསྟན་ཏོ། །

[Block 5338]
བདག་གིས་ནོངས་པ་ཅུང་ཟད་ཅེས་བྱ་བ་འདིས་ནི། བུད་མེད་ལ་འགལ་བར་གྱུར་པའོ། །

[Block 5339]
དེ་ནི་བདག་ལ་མེད་པ་ཉིད་མོད་ཀྱི། །དེ་སྟེ་བུད་མེད་རྣམས་བདག་གི་གནས་སུ་འོངས་པ་ཙམ་གྱིས། གལ་ཏེ་ནོངས་པར་གྱུར་ཀྱང་རྒྱན་གྱི་མཆོག །ཅེས་བསྟན་པ་ཡིན་ནོ། །

[Block 5340]
རྒྱན་གྱི་མཆོག་གི་བཟོད་པ་དེ་ཉིད་བསྟན་པའི་ཕྱིར། སྨྲས་པ། བཟོད་པས་བརྒྱན་ན་ཇི་ལྟར་མཛེས་པ་བཞིན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། བཟོད་པ་ལ་བརྟེན་ཅིག་པའོ། །

[Block 5341]
བཟོད་པའི་མན་ངག་བསྟན་པ་ཡིན་པས་བཟོད་པའི་མན་ངག་གོ། །

[Block 5342]
བཟོད་པའི་མན་ངག་བསྟན་པ་ཉིད་སྙད་བཏགས་པ་ཡིན་པས། བཟོད་པའི་མན་ངག་བསྟན་པར་སྙད་བཏགས་པའོ། །

[Block 5343]
ཉེས་པ་མེད་པ་ནི་སྐྱོན་མེད་པའོ། །

[Block 5344]
བྲམ་ཟེ་ལས་རབ་ཏུ་བྱུང་བ་ནི་ཡོན་ཏན་གྱི་ཞིང་ཉིད་དུ་སྟོན་ཏོ། །

[Block 5345]
བསོད་པར༌[^3420]བྱེད་པ་རྣམས་ཡོངས་སུ་སྲུང་བ་པོ་ནི། རྒྱལ་པོ་ཡིན་ན་འདི་ལྟར་ཅིའི་ཕྱིར་འཇུག་ཅེས་བྱ་བའོ། །

[Block 5346]
བཟོད་པའི་མན་ངག་བསྟན་པའི་རྩོལ་བ་དེ་ཉིད། བདག་འཇིགས་ནས་གསོལ་བ་ནི་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་འཇིགས་ནས་མི་གསོལ་ཞེ་ན། མི་འཇིགས་པའི་རྒྱུ་བསྟན་པའི་ཕྱིར། སེམས་ཅན་རྣམས་ནི་འཆི༌[^3421]འགྱུར་བའི། །ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་གཉིས་ཀྱི་རྒྱུས་འཆི་བས་འཇིགས་པ་ཡིན་ཏེ། དེ་གཉི་ག་ཡང་མེད་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར་སྨྲས་པ། འཇིག་རྟེན་གྱི་རང་བཞིན་ཡོངས་སུ་མ་ཤེས་ནས་བསོད་ནམས་མ་བྱས་པ་དང་། ངན་འགྲོར་འགྲོ་བའི་དགོས་པ་ཡོད་པའོ། །

[Block 5347]
དེ་གཉི་ག་ཡང་མེད་པ་སྟེ། སེམས་ཅན་རྣམས་ནི་འཆི་བར་འགྱུར་བའི༌[^3422]ཚུལ་འདིས་ངེས་པ་ཉིད་དུ་གནས། །ཞེས་བྱ་བ་ཡོངས་སུ་ཤེས་པའི་ཕྱིར། རྒྱུ་དང་པོ་མེད་དོ། །

[Block 5348]
བདག་གི་ཚུལ་ལའང་རྗེས་བལྟས༌[^3423]ན། །ཞེས་བྱ་བ་འདིས་ནི། བསོད་ནམས་བྱས་པའི་ཕྱིར།

[Block 5349]
གཉིས་པ་ཡང་མེད་པས་སོ། །

[Block 5350]
ཅི་སྡེ་དེ་གཉི་ག་མེད་ན་ཅིའི་ཕྱིར། དེ་ལྟར་བཟོད་པའི་མན་ངག་བསྟན་པར་ཐ་སྙད་བཏགས་ཤེ་ན། ཕྱི་ནས་ཆོས་ཀྱི་བདེ་བ་ལ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་བརྩམས་སོ། །

[Block 5351]
ཕྱི་ནས་ཆོས་ཀྱི་བདེ་བ་ལ་གནོད་པ་ཞེས་བྱ་བ་ལ། གནོད་དུ་དོགས་པ་ནི་ཆོས་མ་ཡིན་པར་མ་གྱུར་ཅིག་པའི་དོན་ཏོ། །

[Block 5352]
བདེ་བ་འཐོབ་ལ་ཕན་པའི་ཞེས་བྱ་བ་ནི། བདེ་བ་འཐོབ་པ་གཅིག་པུར་མ་ཟད་དེ། ཆོས་མ་ཡིན་པ་འཐོབ༌[^3424]ཅིང་གནོད་པའོ། །

[Block 5353]
དེ་ལྟ་མོད་ཀྱི་ཡོན་ཏན་རྣམས་ཀྱི་འབྱུང་གནས་སུ་གྱུར་པ་དང་། ཉེས་པ་རྣམས་ཀྱང་ཟློག་པར་བྱེད་པའི་ཕྱིར།

[Block 5354 [VERSE]]
རབ་ཏུ་བཟང་པོའི་སྐྱེས་བཞིན་དུ། །
དགའ་བས་བདག༌[^3425]ནི་བཟོད་པ་སྨྲ། །

[Block 5355]
ཞེས་བྱ་བ་སྟེ། དེ་ཉིད་བསྟན་པ་ནི་བཟོད་པ་ཡོན་ཏན་འབྱུང་གནས་ཞེས་བྱ་བའི་ཚིག་གོ། །

[Block 5356]
ཚུལ་འཆོས་ཀྱི༌[^3426]བརྟུལ་ཞུགས་ནི་གཡོའི་བརྟུལ་ཞུགས་སོ། །

[Block 5357]
མྱ་ངན་མི་བྱེད་དེ་བདག་ཉིད་ཆེན་པོའི་ཉམས་པའི་རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 5358]
བདག་ལ་གནོད་པ་བྱེད་པའི་རྒྱལ་པོ་ལ་ཡང་འཁྲུགས་པར་མི་བྱེད་དོ། །ཅིའི་ཕྱིར་མྱ་ངན་མི་བྱེད་ཅེ་ན། ལུས་ཀྱི་ཕུང་པོ་གནས་པའི་མཐའ་ཤེས་པའི་ཕྱིར་རོ། །ཅིའི་ཕྱིར་འཁྲུགས་པར་མི་བྱེད་ཅེ་ན། སྐྱེ་བོ་རྣམས་ལ་བཟོད་པ་གོམས་ཤིང་འདྲིས་པའི་ཕྱིར་རོ། །

[Block 5359]
དེའི་སེམས་ཞེས་བྱ་བ་ནི་རང་གི་སེམས་སོ། །

[Block 5360]
དེའི་ཕྱིར། དགའ་བའི༌[^3427]ཚུལ་གྱིས་ཡོངས་སུ་ཉམས་བར་མ་གྱུར་ཏོ། །
--- END BLOCKS ---
