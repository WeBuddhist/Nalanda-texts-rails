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
[Block 456]
འོ་ན་མདོ་ལས་ཀྱང༌[^242]སེམས་ཅན་གྱི་ཚོགས་གསུམ་དུ་གསུངས་ཤིང་། རྡོའི་རིགས་ལ་དཔེར་མཛད་པ་དེ་ཇི་ལྟ་བུ། སེམས་ཅན་གྱི་རིགས་ཀྱང་རྣམ་པ་ལྔར་བཤད་པ་དེ་ཇི་ལྟ་བུ། སྨྲས་པ་དེ་ནི་རེ་ཞིག་པ་ལ་དགོངས་པ་ཡིན་ཏེ། རྗེ་བཙུན་གསེར་གླིང་པའི་ཞལ་སྔ་ནས། རིགས་ནི་རྣམ་པ་གཉིས་ཏེ། ཆོས་ཉིད་ཀྱི་རིགས་ཅན་དང་། སྒྲུབ་པའི་རིགས་ཅན་ནོ་ཞེས་གསུངས་པས༌[^243]སྒྲུབ་པའི་རིགས་ཅན་ལ་ནི་རེ་ཞིག་དེ་ལྟར་གནས་སོ། །

[Block 457]
ཆོས་ཉིད་ཀྱི་རིགས་ཅན་གྱི་དབང་དུ་བྱས་ན་ནི་དབྱེ་བ་གང་ཡང་མེད་དོ། །

[Block 458]
འདི་ལྟར་མཁས་པ་དག་གིས་ནི་སོ་སོ་ཐར་པའི་སྡོམ་པ་དེ་ངེས་པར་གཙོ་བོར༌[^244]བྱ་དགོས་པ་ཡིན་ཏེ། དེ་ཡང་འདི་ལྟར་ཆོས་ཀྱི་སྐུ་ནི་དུས་ཐམས་ཅད་དང་། དངོས་པོ་ཐམས་ཅད་ལ་ཁྱབ་པ་ཡིན་པ་དང་། ཡང་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་དེ་ཡང་འཁོར་ལོར༌[^245]བཞུགས་ལ། དེ་ཡང་ས་བཅུའི་དབང་ཕྱུག་ཆེན་པོ་རྣམས་ཁོ་ནའི་སྤྱོད་ཡུལ་ཡིན་ཞིང་དེ་ཡང་ཐེག་པ་ཆེན་པོའི་ཆོས་ཟབ་པ་དང་། རྒྱ་ཆེ་བ་འབའ་ཞིག་གསུངས་པ་ཡིན་ནོ། །

[Block 459]
སྤྲུལ་པའི་སྐུ་ནི་འདི་ལྟར་ཨུ་དུམ་བཱ་རའི་མེ་ཏོག་དང་འདྲ་བས་དུས་རེས་འགའ༌[^246]བ་ཡིན་ཏེ། མདོ་ལས་བསྐལ་པ་དེའི་རྗེས་ལ་སངས་རྒྱས་མི་འབྱུང་བའི་བསྐལ་པ་དྲུག་ཅུ་འབྱུང་བར་འགྱུར་རོ་ཞེས་གསུངས་སོ། །

[Block 460]
དེ་བས་ན་དེས་གསུངས་པའི་སོ་སོར༌[^247]ཐར་པའི་སྡོམ་པ་འདི་ཡང་དུས་རེས་འགའ་བ་ཡིན་པས་དཀོན་པའི་ཕྱིར་དང་། བདེ་འགྲོར་བགྲོད་པའི་རྒྱུའི་གཙོ་བོ་ཡིན་པ་དང་། སངས་རྒྱས་ཀྱི་བསྟན་པ་ནི་སྲོག་གཅོད་པ་ལ་སོགས་པ་སྡིག་པ་ལས་ལོག་པ་ཡིན་པ་དང་། སངས་རྒྱས་ཀྱི་བསྟན་པ་ནི་ཇི་སྲིད་སོ་སོར་ཐར་པའི་སྡོམ་པ་གནས་པ་དེ༌[^248]སྲིད་དུ་གནས་ཤིང་དེ་ལ་རག་ལུས་པ་ཡིན་པས་སོ་སོར་ཐར་པའི་སྡོམ་པ་དེ་དང་པོ་ཁོ་ནར་བསྟན་ཏོ། །

[Block 461]
འདི་ལྟར་འཇུག་པའི་གོ་རིམས་སུ༌[^249]བྱས་ན་ཡང་། སྔོན་ཆད་ཐེག་པ་ཆེན་པོའི་བག་ཆགས་མེད་པ་དག་ལ་ནི་སོ་སོར་ཐར་པ་རིས་བདུན་གང་ཡང་རུང་བའི་སྡོམ་པ་དེ་སྔོན་དུ་འགྲོ་བ་ཡིན་ནོ། །

[Block 462]
སྔོན་ཆད་ཐེག་པ་ཆེན་པོའི་བག་ཆགས་མེད་པའི་གང་ཟག་དག་ལ་ནི་སྡོམ་པ་དེ་མི་སྐྱེ་བ་ཉིད་ཀྱང་ཡིན་ནོ། །

[Block 463]
དེ་བས་རྩ་བ་ལས་སྐལ་བ་ཡོད་ཀྱི་གཞན་དུ་མིན་ཞེས་པ་ཡང་ལེགས་པར་སྨྲས་པར་འགྱུར་རོ། །

[Block 464]
དཀྱུས་ཉིད་ལ་འཇུག་པར་བྱ་སྟེ།

[Block 465 [VERSE]]
སོ་སོར་ཐར་པའི་རིས་བདུན་དུ། །
དེ་བཞིན་གཤེགས་པས་གསུངས་པ་ལ། །
ཚངས་སྤྱོད་དཔལ་ནི་མཆོག་ཡིན་ཏེ། །
དགེ་སློང་སྡོམ་པ་དག་ཏུ་བཞེད། །

[Block 466]
ཅེས་སྨྲས་ཏེ་རིས་བདུན་ལས་དགེ་སློང་གི་སྡོམ་པ་ནི་ཐུན་མོང་མ་ཡིན་ནོ་ཞེས་བདག་གིས་བསམས་སོ། །

[Block 467]
སྨྲས་པ་འདུལ་བའི་གཞུང་ཐམས་ཅད་དང་འཕགས་པ་དགྲ་བཅོམ་པ་རྣམས་ཀྱིས་མཛད་པ་ཡེ་ཤེས་ལ་འཇུག་པ་ལ་སོགས་པ་དང་། གཞན་དེ་དག་གིས་མཛད་པའི་བྱེ་བྲག་ཏུ་བཤད་མཛོད་ཆེན་པོ་དང་། དེའི་དོན་གཅེས་སྤྲས་སུ་བྱ་བ་མདོར་བསྡུས་པ་མངོན་པ་མཛོད་དག་ཏུ་རིས་བརྒྱད་དུ་བཀོད་ལ་འདིར་བདུན་དུ་བཤད་པ་དེ་ཇི་ལྟ་བུ་སྨྲས་པ་བདེན་ཏེ། གཞུང་དེར་དེ་ལྟར་བཤད་མོད་ཀྱི་འོན་ཀྱང་འཕགས་པ་ཐོགས་མེད་ཀྱིས་རྣལ་འབྱོར་སྤྱོད་པའི་སའི་གཞུང་ཐམས་ཅད་དང་། ཚུལ་ཁྲིམས་ཀྱི་ལེའུ་ལས་རིས་བདུན་དུ་བཀོད་དེ། འཕགས་པ་ཐོགས་མེད་ནི་ཆོས་ཀྱི་རྒྱུན་གྱི་ཏིང་ངེ་འཛིན་ཐོབ་ཅིང་ས་གསུམ་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཡིན་པ་དང་། འཕགས་པ་འཇམ་དཔལ་གྱི་རྩ་བའི་རྒྱུད་ཆེན་པོ་ལས་ལུང་བསྟན་པས་ཇི་སྐད་དུ།

[Block 468]
ཐོགས་མེད་སྐྱེས་བུ་དམ་པ་དེས། །བསྟན་བཅོས་ཀྱི་ནི་དེ་ཉིད་རིག །ཅེས་པ་དང་། ཡང་མགོན་པོ་མི་ཕམ་པ་ལ་མངོན་སུམ་དུ་སྡེ་སྣོད་མ་ལུས་པ་གསན་པ་ཡིན་པ་འདི་ལ་སུ་ཞིག་ཐེ་ཚོམ་ཟ། དེ་ལྟ་བུའི་སེམས་ཅན་ཆེན་པོ་དེ་ལ་ཡིད་སྡང་ཞིང་ཐེ་ཚོམ་ཟ་ན་རང་ཉིད་ཕུང་བར་ཟད་དོ། །

[Block 469]
རྗེ་བཙུན་བླ་མ་དཔལ་བྱང་ཆུབ་བཟང་པོས་ཀྱང་སྡོམ་པ་ཉི་ཤུ་པའི་འགྲེལ་པ་ལས།

[Block 470]
ཇི་སྐད༌[^250]དུ། དེ་ལ་སྡོམ་པའི་ཚུལ་ཁྲིམས་ནི་སོ་སོར་ཐར་པའི་རིས་བདུན་གྱི་སྡོམ་པ་བླངས་པའོ། །

[Block 471]
དེ་ལ་དགེ་སློང་དང་དགེ་ཚུལ་དང་། དགེ་སློང༌[^251]མའི་རབ་ཏུ་དབྱེ་བས་རབ་ཏུ་བྱུང་བའི་ཕྱོགས་ནི་རྣམ་པ་ལྔའོ། །

[Block 472]
ཁྱིམ་པའི་ཕྱོགས་གཉིས་ཏེ། དགེ་བསྙེན་དང་། དགེ་བསྙེན་མའི་དབྱེ་བས་སོ། །

[Block 473]
ཉིན་ཞག་གི༌[^252]བསླབ་པ་ནི་དཀའ་བ་སྤྱོད་པ་མ་ཡིན་པ་དང་། འདོད་པ་ལས་གཡེམ་པ་མ་ཡིན་པའི་ཕྱིར་དང་། ཡུན་རིང་པོར་རྗེས་སུ༌[^253]འབྲེལ་པའི་ཕྱིར་འདི་ནི་སོ་སོར༌[^254]ཐར་པའི་རིས་སུ་མི་འོས་པས་མ་བསྟན་ཏོ་ཞེས་གསུངས་ཏེ། བླ་མ་དེ་ནི་བྱང་ཆུབ་སེམས་དཔའི་སྡེ་སྣོད་ཀྱི་འདུལ་བ་འཛིན་པ་ཆེན་པོ་ཡིན་པ་དང་། འཕགས་པ་ཀླུ་སྒྲུབ་དང་སློབ་དཔོན་ཤཱན་ཏ་དེ་བའི་གཅིག་ནས་གཅིག་ཏུ་བརྒྱུད་པའི་བཀའི་གདམས་པ་ཡོད་པའི་ཕྱིར་མཁས་པ་ཆེན་པོ་དེའི་རྗེས་སུ་འབྲང་བར་བྱའོ། །

[Block 474]
སོ་སོར་ཐར་པ༌[^255]རིས་བདུན་པོ་དེ་དག་འདིར་ཅུང་ཞིག་བརྗོད་པར་བྱ་སྟེ། དགེ་བསྙེན་ནི་རྣམ་པ་གཉིས་ཏེ་འདོད་པས་ལོག་པར་གཡེམ་པ་སྤངས་པ་དང་། རང་གི་ཆུང་མ་ཡང་སྤངས་པའོ། །

[Block 475]
དེ་གཉིས་ཀའི་ཐུན་མོང་གི་བསླབ་པ་ནི་འདི་ལྟ་སྟེ། རྩ་བའི་ལྟུང་བར་གྱུར་པ་བཞི་དང་ཆང་སྤངས་པའོ། །

[Block 476]
ཁ་ཅིག་ན་རེ༌[^256]ལོག་པར་ལྟ་བ་སྤངས་པའོ་ཞེས་ཟེར་རོ། །

[Block 477]
དེ་ལ་ཆང་ནི་འདུལ་བ་འཛིན་པ་དག་རང་བཞིན་གྱི༌[^257]ཁ་ན་མ་ཐོ་བ་ཡིན་ནོ་ཞེས་འདོད་ལ། མངོན་པ་བདག༌[^258]ནི་བཅས་པའི་ཁ་ན་མ་ཐོ་བ་ཞེས་ཟེར་རོ། །

[Block 478]
དེ་དག་གི་གཞུང་རྒྱས་པ་ནི་འདིར་གཞག་གོ། །

[Block 479]
དེ་ལྟ་བུའི་བསླབ་པའི་གཞི་ལྔ་དང་། དེ་དག་གི་ཕྱོགས་སུ་གཏོགས་པའི་བསླབ་པའི་གཞི་བཞི་བཅུ་རྩ་ལྔ་སྟེ། བསླབ་པ་ལྔ་བཅུ་དང་ལྡན་པའི་དགེ་བསྙེན་སྐྱོན་མེད་པ་དང་། དེ་བཞིན་དུ་དགེ་ཚུལ་སྡོམ་པར་གྱུར་པ་འདི་ལྟ་སྟེ། བཤགས་པར༌[^259]བྱ་བ་དང་བསྡམ་པར་བྱ་བ་དང་ཉེས་པ་མེད་པའོ། །

[Block 480]
དགེ་སློང་གི་བསླབ་པ་ནི་ཉིས་བརྒྱ་ལྔ་བཅུ་རྩ་གསུམ་ལས།

[Block 481]
ཉི་ཤུ་རྩ་བདུན༌[^260]ནི་བཤགས་པར་བྱ་བར་འགྱུར་རོ། །

[Block 482]
ཉིས་བརྒྱ་བཅུ་གསུམ་ནི་བསྡམ་པར་བྱ་བར་འགྱུར་རོ། །

[Block 483]
བཅུ་གསུམ་ནི་ཉེས་པ་མེད་པར་འགྱུར་རོ། །

[Block 484]
བཅུ་གསུམ་མ་གཏོགས་པ་ལྷག་པ༌[^261]ཉིས་བརྒྱ་བཞི་བཅུ་བསྲུང་བའི་ཁ་ན་མ་ཐོ་བ་མེད་པའི་དགེ་ཚུལ་ཚུལ་དང་ལྡན་ཞིང་རྣམ་པར་དག་པ་དང་། དགེ་སློང་མ་ནི་ཆོས་དྲུག་དང་རྗེས་སུ་མཐུན་པའི་ཆོས༌[^262]དྲུག་ལེགས་པར་བསྲུང་བ་སྟེ་དགེ་སློང་མ་རྣམ་པར་དག་པ་དང་། དེ་བཞིན་དུ་དགེ་སློང་ཡང་ཇི་ལྟར་དམ་པའི་ཆོས་འདུལ་བའི་གཞུང་ལས་ཇི་སྐད་བཤད་པའི་བསླབ་པ་ཤིན་ཏུ་རྫོགས་པར་བྱ་བ་དང་དགེ་སློང་རྣམ་པར་དག་པ་དང་། དེ་བཞིན་དུ་དགེ་སློང་མ་ཡང་བསླབ་པའི་གཞི་ལྔ་བརྒྱ་དང་ལྡན་ཞིང་རྣམ་པར་དག་པའོ། །

[Block 485]
དེ་དག་ཀྱང་སྡེ་པ་ཐ་དད་དེ། འདི་ལྟར་ཕལ་ཆེན་པའི་སྡེ་པ་དང་། ཐམས་ཅད་ཡོད་པར་སྨྲ་བའི་སྡེ་པ་དང་། གནས་བརྟན་པའི་སྡེ་པ་དང་། མང་པོས་བཀུར་བའི་སྡེ་པའོ། །

[Block 486]
དེ་དག་ཀྱང་བཅོ་བརྒྱད་དུ་གནས་ཏེ། འདི་ལྟར།

[Block 487 [VERSE]]
ཤར་དང་ནུབ་དང་གངས་རི་དང་། །
འཇིག་རྟེན་འདས་པར་སྨྲ་བའི་སྡེ། །
བཏགས་པར་ཡོད་པར་སྨྲ་བའི་སྡེ། །
ལྔ་ཚན་དགེ་འདུན་ཕལ་ཆེན་པ། །

[Block 488 [VERSE]]
བཞི་པ༌[^263]དག་ནི་འོད་སྲུངས་པ། །
ཆོས་སྲུང་སྡེ་དང་ས་སྟོན་སྡེ། །
རྣམ་པར་ཕྱེ་སྟེ་སྨྲ་བའི་སྡེ། །
མང་ཐོས་དགེ་འདུན་གོས་དམར་པོ། །

[Block 489 [VERSE]]
གཙུག་ལག་ཁང་ཆེན་ལ་གནས་དང་། །
རྒྱལ་བྱེད་ཚལ་ན་གནས་པ་དང་། །
འཇིགས༌[^264]མེད་རི༌[^265]ལ་གནས་པ་ཡི། །
གནས་བརྟན་པ་ཡི་སྡེ་པ་གསུམ། །

[Block 490 [VERSE]]
སར་སྒྲོགས་རིས་པའི་སྡེ་པ་དང་། །
སྲུང་བ་པ་ཡི་སྡེ་པ་དང་། །
གནས་མའི་བུ་ཡི་སྡེ་པ་སྟེ། །
མང་པོས་བཀུར་བའི་སྡེ་པ་གསུམ། །

[Block 491]
ཡང་གཞུང་ཁ་ཅིག་ལས་ནི་ཚུལ་དེ་ཉིད་ལས་བཏགས་པ༌[^266]ཡོད་པར་སྨྲ་བའི་སྡེ་པ་དེ་ཐམས་ཅད་ཡོད་པར་སྦྱར་ལ། མང་པོས་བཀུར་བའི་སྡེ་པ་ལ་ནི་གནས་མའི་བུའི༌[^267]སྡེ་པ་དང་། ཀུ་རུ་ཀུ་ལའི་སྡེ་པ་དང་། ས་སྒྲོགས་པའི་སྡེ་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 492]
ཡང་གཞུང་ཁ་ཅིག་ལས།

[Block 493 [VERSE]]
འོད་སྲུངས་ཞེས་བྱ་ཆོས་སྲུང་བ།[^268] །
ས་སྲུང་བ་དང་གཞི་ཀུན་ཡོད། །
ཤར་ནུབ་གངས་རི་བཏགས་པར༌[^269]སྨྲ། །
རྣམ་པར་ཕྱེ་སྨྲ་འཇིག་རྟེན་འདས། །

[Block 494 [VERSE]]
གོས་དམར་ཐོས་མང་སྲུང་བ་པ། །
ཀུ་རུ་ཀུ་ལ་གནས་མའི་བུ། །
རྒྱལ་བྱེད་པ་དང་འཇིགས་མེད་པ། །
གཙུག་ལག་ཁང་པ་ཆེན་པོ་པའོ། །

[Block 495 [VERSE]]
བཞི་དང་དྲུག་དང་ལྔ་དང་གསུམ། །
ཐ་དད་རྣམ་པ་བཅོ་བརྒྱད་འདོད། །
དེ་ལྟར་སྡེ་པ་བཅོ་བརྒྱད་དོ།[^270] །
ཤཱཀྱ་སེང་གེའི་བསྟན་པ་ནི། །
--- END BLOCKS ---
