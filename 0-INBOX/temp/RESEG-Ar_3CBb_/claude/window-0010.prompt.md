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
[Block 351]
གཉིས་པའི༌[^182]དབང་དུ་བྱས་པ༌[^183]ནི་ཐུན་མོང་མ་ཡིན་པའི་ཕྱིར་ཏེ། མཆོག་རྟོགས་པའི་བྱེ་བྲག་གིས་མ་ཡིན་གྱི་མཆོག་ཐོབ་པའི་བྱེ་བྲག་གིས་སོ། །

[Block 352]
མཆོག་ཐོབ་པ་ཞེས་བྱ་བ་ཡང་རྒྱུ་ཐམས་ཅད་ཀྱིས་ཐོབ་པ་ནི་མ་ཡིན་གྱི་རྫོགས་པའི་རིམ་པ་འབའ་ཞིག་གིས་ཉེ་བར་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 353]
འབའ་ཞིག་གིས་ཐོབ་ཀྱང་ཐུན་མོང༌[^184]ཡིན་ནོ་ཞེ་ན་ནི༌[^185]ཧ་ཅང་ཐལ་བར་འགྱུར་རོ། །

[Block 354]
དེ་བས་ན་འདི་ནི་མཆོག་གི་དངོས་གྲུབ་ཉིད་དོ། །

[Block 355]
རྒྱན་དང་པོ་བཤད་ཟིན་ཏོ།། །།

[Block 356]
འདི་ལ་ཡང་ཅིའི་ཕྱིར་རྒྱན་ཞེས་བྱ་ཞེ་ན། གང་ལ་གང་གིས་ཕན་འདོགས་པ་དང་། གང་ལ་གང་གིས་མཛེས་པར་བྱེད་པ་དང་། གང་ལ་གང་གིས་དགའ་བར་བྱེད་པ་དེ་ནི་དེའི་རྒྱན་ནོ། །

[Block 357]
རྒྱན་ཞེས་བྱ་བ་ཡང་དུ་ཞིག་ཅེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རྒྱན་ནི་རྣམ་པ་གཉིས་ཏེ་རང་བཞིན་གྱི་རྒྱན་དང་། གསལ་བའི་རྒྱན་ནོ། །

[Block 358]
རྒྱན་ཐམས་ཅད་ཀྱི་དཔེ་ནི་རྣམ་པ་གཉིས་ཏེ། རང་བཞིན་གྱི་རྒྱན་གྱི་དཔེ་ནི་བུ་མོ་བཞིན་མཛེས་པ་ལྟ་བུའོ། །

[Block 359]
གསལ་བའི་རྒྱན་ནི་དཔེར་ན་བུ་མོའི་རིན་པོ་ཆེ་ལྟ་བུའོ། །

[Block 360]
འདི་ལྟ་སྟེ་དཔེར་ན་ནོར་བུ་རིན་པོ་ཆེས་ནི་བུ་མོའི་བཞིན་མཛེས་པར་བྱེད་དོ། །

[Block 361]
བུ་མོའི་བཞིན་ལ་ཕན་འདོགས༌[^186]པར་བྱེད་དོ། །

[Block 362]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི༌[^187]གསང་བ་འདུས་པའི་གླེང་བསླང་བ་ལ་སོགས་པ་འདིས་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་བཤད་པ་ལ་ཕན་འདོགས་པར་བྱེད་དོ། །

[Block 363]
དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་རྒྱན་གྱི་དགོས་པ་ནི་སེམས་ཅན་རྒྱན་ལ་དགའ་བ་རྗེས་སུ་འཇུག་པར་བྱེད་པ་དང་། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་བཤད་པ་ཕུན་སུམ་ཚོགས་པ་ལ་ཕན་འདོགས་པར་བྱེད་དོ། །

[Block 364]
གླེང་བསླང་བ་ནི་འདས་ཟིན་ཏེ་ཞེས་པ་ནི་གླེང་བསླང་བ་རྣམ་པ་ལྔ་བཤད་ཟིན་ཞེས་པའོ། །

[Block 365]
དེ་ནས་རིགས་པ་རྣམ་པ་བཞི་བཤད་པ་བསྟན་པའི་ཕྱིར། རིགས་པ་ཡང་ནི་བཤད་པར་བྱ། །ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ་རྒྱུད་དག་དང་ནི་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་རྒྱུད་ནི་གང་དུ་རྟོགས། གླེང་གཞི་ནི་གང་ཞིག་ཡིན། ཅིའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱ། ཐབས་གང་གིས་ཐོབ་པར་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 366]
དང་པོའི་ལན༌[^188]བསྟན་པའི་ཕྱིར།

[Block 367 [VERSE]]
མི་ཡི་སྐྱེ་བར་འཁྲུངས་པ་ནི། །
རྒྱུད་ཅེས་བྱ་བར་བརྗོད་པ་ཡིན། །

[Block 368]
ཞེས་པ་མིའི་རྒྱུད་དུ་གཏོགས་ཞེས་པའོ། །

[Block 369]
ཅིའི་ཕྱིར་རྒྱུད་ཅེས་བྱ་ན་དེ་ཉིད་མིའི་སྐྱེ་བ་དང་འབྲེལ་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 370]
འདིས་ནི་ལྷ་དང་ལྷ་མ་ཡིན་གྱི་རྒྱུད་དུ་གཏོགས་པ་གསལ་བ༌[^189]ཡིན་ནོ། །

[Block 371]
གཉིས་པའི༌[^190]ལན་བསྟན་པའི་ཕྱིར།

[Block 372 [VERSE]]
བཙུན་མོའི་འཁོར་གྱི་ནང་ནས་ནི། །
ངེས་པར་འབྱུང༌[^191]བ་གླེང་གཞི་ཡིན། །

[Block 373]
ཞེས་སྨོས་ཏེ་ཁྱིམ་ནས་ཁྱིམ་མེད་པར་ངེས་པར་རབ་ཏུ་བྱུང་བའོ། །

[Block 374]
འདི་ལ་ཅིའི་ཕྱིར་ཐུབ་པ་ཆེན་པོ་ཞེས་བྱ་ཞེ་ན།

[Block 375 [VERSE]]
འདི༌[^192]ལས་སྡོམ་པ་བསྟན་པ་ནི། །
ངེས་པའི་ཚིག་ཅེས་བརྗོད་པ་སྟེ། །

[Block 376]
ཞེས་པ་འདུལ་བ་ལས་སྡོམ་པ་ཐམས་ཅད་ཐུབ་པའི་ཕྱིར་ཐུབ་པ་ཆེན་པོ་ཞེས་བྱའོ། །

[Block 377]
ལུང་གཞན་ལས་ཀྱང་།

[Block 378 [VERSE]]
དབང་པོའི༌[^193]སྒོ་བསྡམས་སྡོམ་པ་རྣམས། །
མ་ལུས་བརྩལ་མེད་ཐུབ་པས་ན། །
ཐུབ་པ་ཆེན་པོ་ཞེས་སུ་བཤད། །

[Block 379]
ཅེས་འབྱུང་བ་ལྟ་བུའོ། །

[Block 380]
འདིའི་རྒྱུ་གང་ཞིག་ཡིན་ཞེས་པའི་ལན་དུ། །

[Block 381 [VERSE]]
འབྲས་བུ་འདོད་པས་ཆོས་སྤྱོད་པ། །
དེ་ནི་རྒྱུ་ཞེས་བརྗོད་པ་སྟེ། །

[Block 382]
ཞེས་པ་འབྲས་བུ་ནི་མཆོག་དང་ཐུན་མོང་གི་དངོས་གྲུབ་པོ། །

[Block 383]
ཡང་ན་འབྲས་བུ་ནི་འདིར་ཕྱུག་པ་དང་། གཟུགས་བཟང་བ་དང་། སྟོབས་དང་མི་འཇིགས་པ་དང་གཟུངས་དང་ཏིང་ངེ་འཛིན་དང་། དེ་ལ་སོགས་པ་ཡོན་ཏན་གྱི་ཆོས་རྣམས་སོ། །

[Block 384]
དེ་ཐོབ་པར་བྱེད་པའི་རྒྱུ་ནི་སྦྱིན་པ་དང་།

[Block 385 [VERSE]]
ཚུལ་ཁྲིམས་དང་བཟོད་པ་ལ་སོགས་པའོ། །
འདི་ནི་འདོད་ཆགས་བྲལ་ཆོས་ཀྱི། །
རིགས་པ་རྣམ་པ་བཞིར༌[^194]འདོད་དོ། །

[Block 386]
ཞེས་པ་འདོད་ཆགས་དང་ལྡན་པའི་དབང་དུ་བྱས་པ་ནི་མ་ཡིན་གྱི། འདོད་ཆགས་དང་བྲལ་བའི་དབང་དུ་བྱས་པའི་ཕྱིར་རོ། །

[Block 387]
དེ་བས་ན་འདོད་རྒྱལ་གྱི་ཞགས་པས་ཟིན་པ་རྣམས་ནི་དགོས་པ་མེད་ཀྱང་རྩོམ་པར་འགྱུར་གྱི། དེ་བཞིན་གཤེགས་པ་ཐུགས་རྗེ་ཆེན་པོ་དང་ལྡན་པ་རྣམས་ནི་སེམས་ཅན་གྱི་དོན་དང་མི་ལྡན་པར་ནམ་ཡང་རྩོམ་མི་སྲིད་དོ། །

[Block 388]
དེ་བས་ན་དགོས་པ་ཐམས་ཅད་ནི་རྣམ་པ་གཉིས་ཏེ། འདོད་ཆགས་དང་བྲལ་བ་རྣམས་འདུལ་བ་དང་འདོད་ཆགས་དང་ལྡན་པ་རྣམས་འདུལ་བའོ། །

[Block 389]
དང་པོའི་དབང་དུ་བྱས་པ་ནི་བཤད་ཟིན་ཏོ། །

[Block 390]
གཉིས་པའི་དབང་དུ་བྱས་ནས་བཤད་པ།
--- END BLOCKS ---
