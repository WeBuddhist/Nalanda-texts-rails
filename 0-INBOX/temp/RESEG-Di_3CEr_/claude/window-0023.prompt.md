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
ལེགས་པར་མ་བསླབས་པ་རྣམས་ཀྱིས། །དེ་ནི་ཆོས་མི༌[^621]མཐུན་དཔེས་བརྗོད། །

[Block 807]
གང་གཏན་ཚིགས་ཀྱི་སྦྱོར་བ་འདི་དམ་བཅའ་བ་དང་འགལ་བར་བརྗོད་པ་ནི་རིགས་པ་མ་ཡིན་ཏེ། འདི་ལྟར་ཆོས་མི་མཐུན་པའི༌[^622]དཔེའི་སྦྱོར་བ་ཉིད་ཀྱིས་ཡིན་པས་ནའོ། །

[Block 808]
དེར་ནི་འདི་ལྟར་སྦྱོར་བ་བྱས་ནས་མཛེས་པར་འགྱུར་རོ། །

[Block 809]
སྒྲ་རྟག་སྟེ་ཐམས་ཅད་མི་རྟག་པའི་ཕྱིར་ཞེས་པ་ནི་ཐམས་ཅད་མ་ཡིན་པས༌[^623]མེད་པའི་ཕྱིར་ཞེས༌[^624]དོན་ནོ། །

[Block 810]
དེ་ལྟ༌[^625]ན་ནི་ཆོས་མི་མཐུན་པའི་དཔེས་བསྒྲུབ་བྱ་མེད་པ་ལས་གཏན་ཚིགས་མེད་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 811]
རྟག་ཉེར་འཇལ་གྱིས་འདིར་བསྒྲུབ་བྱ། །མ་ཡིན། ཉེ་བར་འཇལ་བས་ནི་འདིར་སྒྲ་ལ་ཐམས་ཅད་ཅེས་བྱ་བས་ཐམས་ཅད་ཅེས་བྱ་བས་ཐམས་ཅད་མ་ཡིན་པ་ཉིད་རྟགས་སུ་བརྗོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 812]
དེ་ནི་མ་གྲུབ་པ་སྟེ་ཐམས་ཅད་ཀྱི་ཁོངས་སུ་སྒྲ་ཡང་འདུས་པའི་ཕྱིར་རམ། །དམ་བཅའ་བའི་ཕྱོགས་གཅིག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 813]
གལ་ཏེ་ཐམས་ཅད་མི་རྟག་ཅེས་པ་ལ་ཐམས་ཅད་ཀྱི་སྒྲས་སྒྲ་དང་བཅས་སྟེ༌[^626]བརྗོད་ན་ནི་དེ་ལྟར་ན་ཐམས་ཅད་ཀྱི་ཁོངས་སུ་སྒྲ་ཡང་འདུས་པའི་ཕྱིར་ཐམས་ཅད་མ་ཡིན་པ་ཉིད་ནི་མེད་དོ། །

[Block 814]
ཇི་ལྟར་མེད་དེ། གང་གི་ཚེ་འདི་ཕྱོགས་གཅིག་ཡིན་པའི་ཕྱིར་ཐམས་ཅད་མ་ཡིན་པའོ་ཞེ་ན། དེ་ལྟ༌[^627]ན་ནི་གཞན་ལ་ཡང་ཕྱོགས་གཅིག་ཡིན་པ་ཉིད་དོ། །

[Block 815]
ཐམས་ཅད་མ་ཡིན་པས་སོ། །

[Block 816]
དེ་ལྟ༌[^628]ན་ནི་ཐམས་ཅད་མ་ཡིན་པ་མི་འདོད་པར་འགྱུར་རོ།[^629] །

[Block 817]
ཅི་སྟེ་དེ་ལྟ༌[^630]ན་ཡང་དམ་བཅའ་བའི་སྐྱོན་ཉིད་དུ་འགྱུར་ཏེ། མི་རྟག་པ་ཉིད་ཀྱིས་རྟག་པ་ཉིད་བསལ་བའི་ཕྱིར་ཞེ་ན། སྒྲ་ལ་ཡོད་པ་ཉིད་སེལ་བར་འགྱུར་བ་ནི་མ་ཡིན་པའི་ཕྱིར་སྒྲ་ལ་ཡོད་པར་བརྗོད་པ་ཡིན་པས་ནི་ཆོས་མི་མཐུན་པའི་དཔེའི་སྦྱོར་བ་ཉིད་དུ་སྦྱར་བར་བྱའོ། །

[Block 818]
ཅི་སྟེ་སྒྲ་དང་བྲལ་བ་ཐམས་ཅད་དེ་སྒྲ་ཉིད་ཐམས་ཅད་མ་ཡིན་པའོ་ཞེ་ན། དེ་ཡང་དམ་བཅའ་བའི་དོན་གྱི༌[^631]ཕྱོགས་གཅིག་ཡིན་པའི་ཕྱིར་མ་གྲུབ་པ་སྟེ། དཔེར་ན་མི་རྟག་སྟེ་མི་རྟག་པའི་ཕྱིར་ཞེས་པ་བཞིན་ནོ། །

[Block 819]
སྒྲ་ཞེས་པ་མ་གྲུབ་པའི་དོན་ཉིད་ཡིན་པ་དེ་བཞིན་དུ་ཐམས་ཅད་ཡོད་པ་མ་ཡིན་པའི་ཕྱིར་ཞེས་པའི་གཏན་ཚིགས་ཀྱང་ངོ་། །ཅི་སྟེ་འདུས་པ་རྣམས་གཞན་གྱི་དོན་བྱེད་དེ། འདུས་པ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་དང་། དེ་བཞིན་དུ་འདུས་བྱས་མི་རྟག་སྟེ་འདུས་བྱས་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་དེ་དག་ལ་ཡང་དམ་བཅའ་བའི་དོན་གྱི་ཕྱོགས་གཅིག་གཏན་ཚིགས་སུ་འགྱུར་བ་མཐོང་ངོ་ཞེ་ན། འདིར་འདུས་པ་དང༌[^632]འདུས་བྱས་ཐམས་ཅད་ནི་དམ་བཅའ་བའི་དོན་མ་ཡིན་ཏེ། དཔེ་མེད་པར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 820]
འོན་ཀྱང་འདི་ལྟར་མིག་ལ་སོགས་པ་དང་། འདུས་བྱས་ཀྱི་ཕྱོགས་གཅིག་ཡིན་ནོ། །

[Block 821]
ཅི་སྟེ་ཡང་སྒྲ་ཉིད་ཐུན་མོང་མ་ཡིན་པར་འགྱུར་རོ་ཞེ་ན། དེ་ལྟར་འགྱུར་བའི་ནུས་པ་ནི་མེད་དོ། །

[Block 822]
དམ་བཅའ་བའི་དོན་གྱི་ཆོས༌[^633]ནི་ཐུན་མོང་མ་ཡིན་པ་སྟེ་མཉན་པར་བྱ་བ༌[^634]ཉིད་ཐུན་མོང་མ་ཡིན་པར་རིགས་ཀྱི་སྒྲ་ལ་ནི་སྒྲ་གཞན་མེད་པའི་ཕྱིར་དེ་ལྟ་མ་ཡིན་པས་མ་གྲུབ་པ་ཉིད་ཅེས་བྱ་བའི་གཏན་ཚིགས་ཀྱི་སྐྱོན་ཡིན་ནོ། །

[Block 823]
དཔེའི་སྐྱོན་ཡང་དམ་བཅའ་བའི་སྐྱོན་མ་ཡིན་ནོ། །

[Block 824]
རྩོད་པ་སྒྲུབ་པར་ནི་འདི་འགལ་བའི་གཏན་ཚིགས་ལྟར་སྣང་བ་ཉིད་ཀྱི་ཁོངས་སུ༌[^635]བསྡུས་ཏེ། མཚན་ཉིད་དེ་ལྟ་བུ་ལས་ནི། །འགལ་བ་དང་ལྡན་མིན། དེར་ནི་འགལ་བ་རྣམ་པ་གཉིས་སུ་བསྟན་ཏེ། དམ་བཅའ་བའི་དོན་དང་འགལ་བ་དང་། གྲུབ་པའི་མཐའ་དང་འགལ་བའོ། །

[Block 825]
དེ་གཉིས་ཀ་ཡང་འདིར་མི་སྲིད་དོ། །

[Block 826]
དེ་གཉིས་ཀ་ཡང་འགལ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བསྟན་པར་བྱའོ། །

[Block 827]
དེ་ལྟར་བསྒྲུབ༌[^636]བྱ་བསྟན་ནས།

[Block 828 [HEADING]]
### གཏན་ཚིགས་བསྟན་པ། ^3-2-0

[Block 829]
ད་ནི་གཏན་ཚིགས་བསྟན་པར་བྱ་སྟེ། དེ་ལ།

[Block 830 [VERSE]]
གང་ཞིག་བསྒྲུབ་བྱའི་ཆོས་ཀྱི་རྟགས། །
དེ་ལྟར་སྣང་བ་ཕལ་ཆེ་བས། །
དེས་ན་གཏན་ཚིགས་སོགས་དོན་གྱི། །
སྔོན་དུ་རྒྱས་པར་དེ་བསྟན་བྱ། །

[Block 831 [VERSE]]
མཐུན་ཕྱོགས་ལ་ཡོད་མེད་རྣམ་གཉིས། །
ཕྱོགས་ཀྱི་ཆོས་ལ་ཡང་རྣམ་གསུམ། །
མི་མཐུན་ཕྱོགས་ལའང་སོ་སོར་ནི། །
ཡོད་མེད་གཉིས་ཀའི་བྱེ་བྲག་ཕྱིར། །

[Block 832]
གང་གི་ཕྱིར་འདིར་ཕྱོགས༌[^637]ཆོས་རྣམ་པ་དགུར་བསྟན་པ་དེའི་ཕྱིར་དེ་ཉིད་སྔར་བརྟག་པར་བྱའོ། །

[Block 833 [HEADING]]
#### ཕྱོགས་ཀྱི་ཆོས། ^3-2-1-0

[Block 834]
རེ་ཞིག་ཅི་སྟེ་འདིར་ཕྱོགས་ཀྱི་ཆོས་སུ་འགྱུར་ཞེ་ན། ཇི་ལྟར་ནི༌[^638]མི་འགྱུར། །གང་གི་ཕྱིར་ཆོས་ཅན་ནི་གྲུབ་ཟིན་པའི་ཕྱིར་སྒྲུབ་པར་མི་འདོད་པས་ན་ཉེས་པ་མེད་དོ། །

[Block 835]
གང་གི་ཕྱིར།

[Block 836 [VERSE]]
བསྡུས་པ་བསྒྲུབ་བྱ་ཡིན་པའི་ཕྱིར། །
ཆོས་དང་ཆོས་ཅན་ཁ་ཡར་བ། །
དངོས་སུ་ཡིན༌[^639]ཡང་དེ་ཕྱོགས་གཅིག །
ཡིན་ཕྱིར་བསྒྲུབ་བྱར་རྟགས༌[^640]ནས་བརྗོད། །

[Block 837]
བསྡུས་པའི་དོན་རྗེས་སུ་དཔག་པར་བྱ་བ་ཡིན་པར་ནི་སྔར་བཤད་ཟིན་ཏོ། །

[Block 838]
དེ་དངོས་ཀྱི་བསྒྲུབ་བྱ་བསྡུས་པའི་ཡན་ལག་གི་དོན་ཆོས་ཙམ་དང་ཆོས་ཅན་ཁ་ཡར་བ་ལ་ནི་ཉེ་བར་བཏགས་ནས་ཡིན་པར་བརྗོད་དོ། །

[Block 839]
དེའི་ཆོས་ཡིན་པའི་ཕྱིར་ཉེས་པ་མེད་དོ། །

[Block 840]
དཔེར་ན་རས་ཡུག་ཚིག་གོ་ཞེས་བྱ་བ་བཞིན་ནོ། ། འདི་ལ་ཡང་གཉིས་ཀ་ལ་གྲུབ་ཆོས་དེ་ལས། །

[Block 841 [VERSE]]
ཐ་སྙད་ཡིན་ཕྱིར་གཉིས་ཀ་ལའམ། །
གང་ཡང་རུང་བ་ལ་བཟློག་པའམ། །
ཐེ་ཚོམ་ཆོས་གྲུབ་འདོད་མ་ཡིན། །

[Block 842]
འདིར་གཉིས་ཀ་ལ་ཕྱིན་ཅི་ལོག་ཏུ་གྲུབ་པ་ནི། དོན་གྱི་ཤུགས་ཀྱིས་གཏན་ཚིགས་ཉིད་དུ་མི་འདོད་དེ། དཔེར་ན་སྒྲ་མི་རྟག་སྟེ། མིག་གི་གཟུང་བྱ་ཡིན་པའི་ཕྱིར་ཞེས་བྱ་བ་ལྟ་བུའོ། །

[Block 843]
གང་ཡང་རུང་བ་ལ་སྟེ་གཅིག་ཏུ་ཕྱིན་ཅི་ལོག་ཏུ་ཡང༌[^641]གྲུབ་པ་ནི་དཔེར་ན་མངོན་པར་གསལ་བར་སྨྲ་བ་ལ་བྱས་པ་ཉིད་ལྟ་བུའོ། །

[Block 844]
གཉིས་ཀའམ་གང་ཡང་རུང་བ་ལ་ཐེ་ཚོམ་དུ་གྱུར་པ་ནི་དཔེར་ན་དུད་པ་ཉིད༌[^642]ཐེ་ཚོམ་ཟ་བ་ལས་མེ་སྒྲུབ་པ་ལྟ་བུའོ། །

[Block 845]
ཆོས་གྲུབ་པ་ནི་དཔེར་ན་བདེ་བ་ལ་སོགས་པ་ཐམས་ཅད་ཡོད་པའི་ཕྱིར་བདག་ཁྱད་པར་ཡོད་དོ་ཞེས་བྱ་བ་ལྟ་བུའོ། །
--- END BLOCKS ---
