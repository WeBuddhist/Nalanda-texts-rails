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
[Block 316]
དེ་བས་ན་སྔགས་ཐུན་མོང་མ་ཡིན་ནོ། །

[Block 317]
ཡིད་ལ་བྱེད་པའི་ཁྱད་པར་ཐུན་མོང་བ་ཡང་མ་ཡིན་ཏེ། ཞི་བ་ལ་ནི་བྱམས་པ་ཡིད་ལ་བྱེད་དོ། །

[Block 318]
རྒྱས་པ་ལ་ནི་སྙིང་རྗེ་ཡིད་ལ་བྱེད་དོ། །

[Block 319]
དབང་ལ་ནི་དགའ་བ་ཡིད་ལ་བྱེད་དོ། །

[Block 320]
དྲག་པོ་ལ་ནི་བཏང་སྙོམས་ཡིད་ལ་བྱེད་དོ། །

[Block 321]
སྤྱོད་པ་ཐུན་མོང་བ་ཡང་མ་ཡིན་ཏེ། ཞི་བ་ལ་ནི༌[^166]སྦྱིན་པ་ལ་སྤྱོད་དོ། །

[Block 322]
རྒྱས་པ་ལ་ནི་སྙན་པར་སྨྲ་བ་ལ་སྤྱོད་དོ། །

[Block 323]
དབང་ལ་ནི་དོན་སྤྱོད༌[^167]ལ་སྤྱོད་དོ། །

[Block 324]
དྲག་པོ་ལ་ནི་དོན་མཐུན་པ༌[^168]ལ་སྤྱོད་དོ། །

[Block 325]
དེ་བས་ན་འདི་ནི་ཐུན་མོང་གི་དངོས་གྲུབ་མ་ཡིན་ནོ། །

[Block 326]
གཞན་ཡང་འདི་ནི་མཆོག་ཡིན་ཞེས་པའམ། རྒྱུ་ཐུན་མོང་མ་ཡིན་པ་ལས་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 327]
ལུང་གཞན་ལས་ཀྱང་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་མཆོག་གི་དངོས་གྲུབ་ཅེས་བྱ་བ་ནི་རྒྱུ་ཐུན་མོང་བ༌[^169]མ་ཡིན་པ་ལས་གྲུབ་པ་འབྱུང་ངོ་ཞེས་འབྱུང་བ་ལྟ་བུའོ། །

[Block 328]
རྒྱུ་ཐུན་མོང་བ་ལས་གྲུབ་ཀྱང་མཆོག་ཡིན་ནོ་ཞེས་པ་འམ། རྒྱུ་ཐུན་མོང་མ་ཡིན་པ་ལས་གྲུབ་ཀྱང་ཐུན་མོང་ཡིན་ནོ་ཞེ་ན་ནི་ཧ་ཅང་ཡང༌[^170]ཐལ་བར་འགྱུར་རོ་ཞེས་སྨྲས་པ་དེ་ནི་མ་ཡིན་ཏེ། འདི་ནི་རྫོགས་པའི་རིམ་པ་ལ་སྨྲ་བ་ནི་ལྟོས་པའི༌[^171]ཕྱིར་རོ། །

[Block 329]
ཐམས་ཅད་ཀྱང་ཀུན་རྫོབ་ཀྱི་རྣམ་པ་ཅན་ལ་བརྟེན་པའི་ཕྱིར་ཐུན་མོང་མ་ཡིན་པ་ཡང་མ་ཡིན་ནོ། །

[Block 330]
ལྷ་ཐུན་མོང་མ་ཡིན་པ་ཡང་མ་ཡིན་ཏེ། ཞི་བ་ལ་སོགས་པ་སོ་སོའི་ལས་འདྲེ་བར་བྱེད་ཅིང་འོན་ཀྱང་རྫོགས་པའི་རིམ་པ་དང་། ཐུན་མོང་དུ་གྱུར་པའི་ཕྱིར་དེ་ལ་དེ་སྐད་ཅེས་བྱའོ། །

[Block 331]
དེ་བས་ན་འདི་ནི་ཐུན་མོང་གི་དངོས་གྲུབ་པོ། །མཆོག་ཅེས་བྱ་བ་འདི་ཡང་གང་ཞིག་ཡིན་དེ་ཉིད་མི་ཤེས་སོ་ཞེ་ན། དེའི་ཕྱིར་སངས་རྒྱས་ཀྱང་ནི་མཆོག་ཡིན་ནོ། །ཞེས་སྨོས་ཏེ་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི༌[^172]གསང་བ་མཆོག་གི་དངོས་གྲུབ་ནི་ཆོས་ཀྱི་སྐུ་ལ་སོགས་པའོ། །

[Block 332]
ཆོས་ཀྱི་སྐུ་ཞེས་བྱ་བ་འདི་ཡང་གང་ཞིག་ཡིན་ཞེ་ན། དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་དོན་དམ་པ་ཆོས་ཀྱི་སྐུ་ནི་ཐོག་མ་མེད་པ་ཐ་མ་མེད་པ། དབུས་མེད་པ། བསྟན་དུ་མེད་པ། ཐོགས་པ་མེད་པ། ཁ་དོག་མེད་པ། དབྱིབས་མེད་པ། གྲངས་དང་། བགྲང་བ་དང་། ཤེས་པ་དང་། བརྗོད་པའི་ཡུལ་ལས་འདས་པ། དངོས་པོ་མཐའ་དག༌[^173]ཐམས་ཅད་དང་བྲལ་བ་སྟེ། དཀོན་ཅོག་བརྩེགས་པ་ལས་ཀྱང་། འོད་སྲུངས་ཡོད་ཅེས་བྱ་བ་འདི་ནི་མཐའ་གཅིག་གོ། །

[Block 333]
མེད་ཅེས་བྱ་བ་འདི་ནི་མཐའ་གཉིས་སོ། །

[Block 334]
རྟག་ཅེས་བྱ་བ་འདི་ནི་མཐའ་གཅིག་གོ། །

[Block 335]
མི་རྟག་ཅེས་བྱ་བ་འདི་ནི་མཐའ་གཉིས་སོ། །

[Block 336]
དབུ་མའི་ལམ་ནི་དམིགས་སུ་མེད་པའོ་ཞེས་འབྱུང་བ་དང་། འདུས་པ་ཆེན་པོ་རིན་པོ་ཆེ་ཏོག་ལས་ཀྱང་། ཅི་སྟེ་མཆིས་ཞེས་བགྱི༌[^174]ན་ནི་རྟག་པར་འགྱུར། མ་མཆིས་ཞེས་བགྱི༌[^175]ན་ནི་ཆད་པར་འགྱུར། དབུ་མའི་ལམ་ནི་དམིགས་སུ་མ་མཆིས་སོ་ཞེས་འབྱུང་བ་དང་། གཞན་དག་ལས་ཀྱང་།

[Block 337 [VERSE]]
ཡོད་དང་མེད་པ་འདི་ཡང་མཐའ་ཡིན་ཏེ། །
དག་དང་མ་དག་གཉིས་ཀྱང་མཐའ་རུ་འགྱུར། །
མཁས་པས་མཐའ་གཉིས་རྣམ་པར་སྤངས་ནས་ཀྱང་། །
དབུས་ལ༌[^176]རྟོག་ཅིང་གནས་པར་མི་བྱེད་དོ། །

[Block 338]
ཞེས་འབྱུང་བ་དང་། གཞུང་འདི་ཉིད་ལས་ཀྱང་། དངོས་པོ་མེད་པ་བསྒོམ་པའི་དངོས། །ཞེས་བྱ་བ་ལ་སོགས་པ་རྒྱ་ཆེར་གསུངས་སོ། །

[Block 339]
འདི་ཉིད་ནི་མཆོག་ཡིན་པར་ཡང་ལུང་གིས་བཤད་དེ། [^177]ཆོས་རྣམས་རང་བཞིན་མེད་པ་དང་།

[Block 340 [VERSE]]
སྐུ་གསུམ་པོ་ཡི་ཁྱད་པར་གྱིས། །
ཐུན་མོང་ལས་ནི་མ་གྲུབ་ཕྱིར། །
འདི་ནི་མཆོག་ཏུ་གྱུར་པ་ཡིན། །

[Block 341]
ཞེས་གསུངས་སོ། །

[Block 342]
དེ་བས་ན་འདི་ནི་མཆོག་གི་དངོས་གྲུབ་བོ། །

[Block 343]
སངས་རྒྱས་ཞེས་སྨོས་པ་མ་ཡིན་ནམ། རྡོ་རྗེ་འཆང་ཆེན་པོ་ལ་སོགས་པ་མ་ཡིན་པ་ཆོས་ཀྱི་སྐུ་ལ་སོགས་པ་ཅིའི་ཕྱིར་མཆོག་གི་དངོས་གྲུབ་ཅེས་གྲགས་ཤེ་ན། འདི་ཉིད་སངས་རྒྱས་ཏེ་སྒྲིབ་པ་རྣམ་པ་གཉིས་སྤངས་པ༌[^178]དང་། བསོད་ནམས་དང་ཡེ་ཤེས་ཀྱི་ཚོགས་རྒྱས་པའི་ཕྱིར་རོ། །

[Block 344]
མཆོག་ཅེས་བྱ་བ་འདི་ཐུན་མོང་མ་ཡིན་པ་ཞིག་མ་ཡིན་ནམ། འདི་ཅིའི་ཕྱིར་ཐུན་མོང་པ་ལ་མཆོག་ཅེས་བྱ་ཞེ་ན། འདི་ནི་ཐུན་མོང་མ་ཡིན་པ་ཉིད་དེ། ཉན་ཐོས་ལ་སོགས་པ་དང་ཐུན་མོང་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 345]
གྲུབ་པའི་མཐའ་གཞན་དང་ཐུན་མོང་མ་ཡིན་པ་ནི་མ་ཡིན་ཏེ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ལ་སོགས་པ་དང་ཐུན་མོང་པའི་ཕྱིར་རོ། །

[Block 346]
རིགས་ཀྱིས༌[^179]ཐུན་མོང་མ་ཡིན་པ་ཡང་མ་ཡིན་ཏེ་འདི་ལྟར་རྡོ་རྗེའི་རིགས་དང་། ལས་ཀྱི་རིགས་ཀྱི་བར་དུ་ཐུན་མོང་དུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 347]
ཐབས་ཀྱིས་ཐུན་མོང་མ་ཡིན་པ་ཡང་མ་ཡིན་ཏེ། བསྐྱེད་པའི་རིམ་པ་དང་། རྫོགས་པའི་རིམ་པ་ལ་སོགས་པ་ཐབས་ཐམས་ཅད་པའི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 348]
བསྟན་དུ་མེད་པས་ཐུན་མོང་མ་ཡིན་པ་ཡང་མ་ཡིན་ཏེ། ཡུལ་དང་དུས་དང་གཉིས༌[^180]རང་བཞིན་གྱིས་སྐལ་བ༌[^181]ཐམས་ཅད་མཆོག་ཏུ་གྱུར་པའི་ཕྱིར་རོ། །

[Block 349]
དེ་བས་ན་མཆོག་གི་དངོས་གྲུབ་ཅེས་བྱ་བ་འདི་གང་ཞིག་ཡིན། ཅིའི་ཕྱིར་མཆོག་གི་དངོས་གྲུབ་ཅེས་བརྟག་ཅེ་ན།

[Block 350]
དང་པོ་ནི་བཤད་ཟིན་ཏོ། །

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
--- END BLOCKS ---
