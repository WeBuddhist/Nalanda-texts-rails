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
ཉེ་དུས་ཀྱང་ངོ༌[^280]ཞེས་བྱ་བ་མུ་སྟེགས་ཅན་དང་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 457]
འདིར་གཞུང་ནི་བདག་པོ་ཉེ་དུས་བགྱིད་དུ་སྩལ་པ༌[^281]ལགས་ན་ལྟུང་བ་ཅིར་འགྱུར། ཉེས་བྱས་ཀྱི་བྱེད་པ་པོར་འགྱུར་རོ། །

[Block 458]
ཁ་ཅིག་ནི་འདི་དག་ལ་ལྟུང་བ་མེད་ཅེས་ཟེར་ཏེ་དེ་ནི༌[^282]མི་རིགས་སོ། །

[Block 459]
གང་ཡང་རུང་བ་གཅིག་རབ་ཏུ་བྱུང་བ་ལ་བརྟེན་པའི་དོན་འཛིན་པ་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 460]
འདུག་གནས་གཅིག་ཏུ་ཟ་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 461]
བསོད་སྙོམས་ནི་བྱེད་པ་པོ་ཡིན་ཞེས་བྱ་བ་གསུངས་ན། དེ་ལ༌[^283]སུ་དང་འབྲེལ་པའི་བསོད་སྙོམས་འདི་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་སྟོབས་པའི་འོ་ཞེས་བྱ་བ་སྨོས་ཏེ། མ་གཏོགས་པ་ཉིད་བཟུང་བས་མ་བྱིན་པར་ལེན་པ་ཉིད་བསྐྱེད་པའོ། །ཇི་ལྟར་སྟོབས་པའི་ཞེ་ན། དེའི་ཕྱིར་ཡོངས་སུ་མ་སྤགས་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྒྱ་ཆེ་བ་ཙམ་རབ་ཏུ་བསྟན་པ་ལ་སྤགས་པ་གང་ཡིན་པ་དེ་ནི་སྦྱིན་པ་འཇུག་པས་མ་ཡིན་ནོ། །

[Block 462]
དེར་ཉེས་པ་འདི་བསྐྱེད་པ་སྟེ། གལ་ཏེ་ཡོངས་སུ་སྤྱོད་པ་འདི་ཡིན་ན༌[^284]འདི་ཙམ་སྦྱིན་པར་བྱ་ཞེས་བྱ་བ་སྤགས་པ་གང་ཡིན་པ་དེ་ལ་ནི་རྒྱ་ཆེ་བ་ཙམ་དུ་བསྟན་པས་སྤགས་པ་མ་ཡིན་པ་སྟེ། དེ་བས་ན་འདིར་ཉེས་པ་མེད་དོ། །

[Block 463]
ཅི་མ་སྤགས་པ་ཐམས་ཅད་ལ་སྟོབས་པ་བྱེད་པ་པོ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཅི་བདེར་མ་བྱས་པར་རོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྦྱིན་པ་ལ་འཇུག་པས་སྟོབས་པ་དེ་ཡིན་ཏེ། གང་ཞིག་ཅི་བདེར་མ་བྱས་པར་རོ་ཞེས་བྱ་བ་འདི་ལ་ཉེས་པ་མེད་དོ། །ཅི་འདི་ཐམས་ཅད་ལ་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཁྱིམ་པའི་འོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚད་ཇི་ཙམ་པ་ལ་དེ་དང་འབྲེལ་པའི་བསོད་སྙོམས་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་བྲེའུ་ཆུང་དག་གི་ཚད་ནི་འབྲས་ཐུག་པོ་ཆེ་མ་ག་དྷཱའི་བྲེའུ་ཆུང་གི་ཕྱེད་དང་ལྔ་བཙོས་པ་ཚོད་མ་མ༌[^285]གཏོགས་པ་ལས་ལྷག་པའི་བསོད་སྙོམས་ཏེ། གྲོགས་ཀྱི་སྐལ་བ་དང་བཅས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྲེའུ་ཆུང་ཕྱེད་དང་ལྔ་བཙོས་པ་ལས་ལྷག་པའི་བསོད་སྙོམས་ནི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 464]
བྲེའུ་ཆུང་དག་གི་ཚད་ནི་ཇི་ཙམ་ཞེ་ན། དེའི་ཕྱིར་བཙོས་པ་ཞེས་བྱ་བ་སྨོས་ཏེ། འབྲས་བཙོས་པ་མ་ག་དྷཱའི་བྲེའུ་ཆུང་གི་ཚད་བྲེ་གང་རྣམས་ལ་ཡོད་པ་དེ་རྣམས་ལའོ། །

[Block 465]
ཚོད་མ་མ༌[^286]གཏོགས་ཞེས་བྱ་བ་ནི། འདིར་ཚོད་མ་བརྩི་བར་མི་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 466]
འདུས་ནས་ལེན་པ་ལ་གྲོགས་དང་ལྷན་ཅིག་ཏུ་ལེན་པ་གང་ཡིན་པ་དེ་ནི་དེའི་བརྩི་བར་བྱ་འམ༌[^287]འོན་ཏེ་མ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་གྲོགས་ཀྱི་སྐལ་བ་དང་ཡང་བཅས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདིར་གཞུང་ནི་འདོད་ན་དགེ་སློང་དེ་དག་གི་ལྷུང་བཟེད་གང་བ་གཉིས་སམ་གསུམ་བླང་བར་བྱའོ་ཞེས་ཐམས་ཅད་བྱེད་པ་པོ་ཉིད་ཀྱིས་གཉིས་སམ་གསུམ་གྱི་ཚིག་ཅེས་གསུངས་པ་ཡིན་ནོ། །

[Block 467]
གང་དུ་འདིའི་འོག་ཏུ་འདི་དང་འབྲེལ་པའི་བསོད་སྙོམས་བྱེད་པ་པོ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་ཟོས་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཅི་ཟོས་སོ་ཅོག་ཐམས་ཅད་ལའམ་ཞེ་ན། དེའི་ཕྱིར་མནོས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། རྙེད་པ་བཞག་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 468]
འདིར་གཞུང་ནི་ཞུ་བ་ལས་དེ་ཉིད་དུ་འདུག་ཅིང་དོན་ཇི་སྲིད་དུ་ཟོས་ཀྱང་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 469]
དེ་ལ་ནི་ཉེས་བྱས་ཀྱིའོ་ཞེས་བྱ་བ་ནི་བྱེད་པ་པོ་སྟེ་འདིར་ནི་མནོས་པ་ལའོ། །

[Block 470]
འདིར་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 471]
གཞན་གྱིས་མནོས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི། གཞན་ནོད་དུ་བཅུག་ལ་ཟོས་ན་ཡང་ཉེས་བྱས་ཀྱི་བྱེད་པ་པོ་ཡིན་ནོ། །

[Block 472]
འདིར་གཞུང་ནི་ཞུ་བ་ལས།

[Block 473]
ལྡེ་གུ་དག་དང་སྣུམ་ཁུར་དག་བསྟབས་པ་དེ་ལས་འོག་ཏུ་ལྷུང་བཟེད་གཉིས་སམ་གསུམ་ལས་ལྷག་པར་གཞན་ནོད་དུ་བཅུག་ན་ཉེས་བྱས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 474]
གཞན་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་འདི་ཡིན་ཏེ། དེ་ཉིད་དུ་འདུག་སྟེ་མ་བསྟབས་པར་ཟོས་ཀྱང་ལྟུང་བ་མེད་ཅེས་གསུངས་པ་ཡིན་ནོ། །

[Block 475]
འདིར་མདོ་འདི་ནི་ཉེས་བྱས་སུ་དོགས་པ་བསལ་བའི་ཕྱིར་བྱས་སོ། །

[Block 476]
ལས་སུ་མ་བྱས་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་འབྲས་ལ་སོགས་པ་རྔོ་བཏགས་མ་བྱས་པ་མནོས་ཏེ་ཟ་བ་ལ་ལྟུང་བ་མེད་པ་སྟེ། ཉེས་པ་མེད་པ་ལ་དགོངས་པ་ཡིན་གྱི་འབྲུ་ཙམ་པ་ལེན་པའི་ཉེས་པ་གཞན་ནི་ཡོད་དོ། །

[Block 477]
དེ་བས་ན་འདི་ལ་ཡང་འདིར་འདི་ལས་མེད་པར་རྟོགས་པར་མི་བྱའོ། །

[Block 478]
བླང་བར་བྱ་བ་གལ་ཏེ་མང་བ་ཉིད་ཡིན་ན་དགེ་སློང་དག་ལ་བགོ་བཤའ་བྱའོ་ཞེས་བྱ་བ་ནི། འདིར་བླང་བར་འོས་པ་བྲེའུ་ཆུང་ཕྱེད་དང་ལྔའི་མཐར་ཐུག་པ་དེ་དང་རྗེས་སུ་མཐུན་པའི་ཚོད་མ་དང་ལྷན་ཅིག་ཏུ་གང་ཡིན་པ་དེ་ལས་གལ་ཏེ་ལྷག་པ་ཡིན་པར་བླང་བར་བྱའོ། །

[Block 479]
འདིར་མང་པོ་ལ་ཡང་དག་པར་བསྟེན་པ་ལ་གཞུང་ནི་དགེ་སློང་དག་ལ་བགོ་བཤའ་བྱ་སྟེ། ལྷུང་བཟེད་གང་བ་གཉིས་སམ་གསུམ་བླངས་ནས་ཞེས་བྱ་བའི་ཚིག་གིས་རིག་པར་བྱའོ། །

[Block 480]
ལྷུང་བཟེད་དོ་གསུམ་ཙམ་ལས་ལྷག་པར་ལེན་པའི་ལྟུང་བྱེད་དོ།། །།

[Block 481]
ཇི་ཙམ་གྱིས་ཆོག་པ་བཟའ་བར་བྱའོ། །

[Block 482]
ཟས་བརྩམས་པས་ལྡང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། ཟས་ལ་བརྩམས་པའི་ངོ་བོ་གསུངས་པ་ནི། ཐ་ན་ལན་ཚྭ༌[^288]ཡན་ཆད་བཟའ་བར་བྱ་བ་གང་ཡང་རུང་བ་ཅུང་ཟད་ཅིག་བླངས་ན་རྣམ་པ་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་སྟེ། ཅུང་ཟད་ཅིག་ཅེས་བྱ་བ་ནི་ཉུང་དུ་ཡང་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 483]
གང་ཡང་རུང་བ་ཞེས་བྱ་བ་འདིས་ནི་འདི་སྟོན་པར་བྱེད་དེ། ལན་ཚྭ་ཡན་ཆད་ཅེས་བྱ་བ་སྟེ་ཇི་སྲིད་ལན་ཚྭ་ཞེས་བྱ་བའི་དོན་ཏེ། བླངས་ནས་ཞེས་བྱ་བ་ནི་ལེན་པ་ལའོ། །

[Block 484]
རྣམ་པ་དེ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཟས་ལ་མ་བསྐོས་པ་དེ་ཉིད་དོ། །ཤེས་གཙོ་བོ་སྤངས་པ་ཉིད་དང་ལྷག་བོར་མ་བྱས་པ་ཉིད་དག་ལའོ་ཞེས་བྱ་བ་འཆད་པར་འགྱུར་ཏེ། དེ་ལས་སྤངས་པ་གང་ཡིན་པ་དང་། སྤངས་པ་ཉིད་བྱེད་པ་བརྗོད་པར་བྱ་བ་ཡིན་ནོ། །

[Block 485]
དེ་བས་ན་སྤངས་པ་ནི་བཏང་བའོ་ཞེས་བྱ་བ་སྟེ། གང་གི་ཕྱིར་དེའི་ཚེ་ན་ཟས་ལ་སོགས་པ་ཡོངས་སུ་བཀང་བ་ཞེས་བྱ་བའོ། །

[Block 486]
འདི་གང་ལས་ཤེས་པ་ཡིན་ཞེ་ན། དེའི་ཕྱིར་འདུག་པའོ་ཞེས་བྱ་བ་སྨོས་སོ། །ཇི་ལྟ་བུ་ཞིག་ཅེ་ན། དེའི་ཕྱིར་རྩ་བ་ལ་སོགས་པ་བཅའ་བར་བྱ་བ་ལ་སོགས་པའི་ཟས་བརྩམས་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། སྤངས་པའི་རྩ་བ་ལ་སོགས་པ་དང་བཅའ་བར་བྱ་བ་ལ་སོགས་པའི་ཟས་གང་གིས་ཞེས་བྱ་བའི་དོན་ཏོ། །ཅི་ཅུང་ཟད་ཀྱང་མ་བྱས་པར་སྤངས་ནའང་ཞེ་ན། དེའི་ཕྱིར་རྩ་བ་དང་སྡོང་བུ་དང་འདབ་མ་དང་མེ་ཏོག་དང་འབྲས་བུ་བཅའ་བར་བྱ་བ་དང་ཐུག་པ་ལས་གཞན་པ་བཟའ་བར་བྱ་བ་རུང་བ༌[^289]དང་མི་རུང་བ་མ་འདྲེས་པའི་བྱིན་ལེན་སྟོབས་པ་འཐབ་པའི༌[^290]ཕྱོགས་ན་འགྲེང་བ་སྤང་བར་བྱས་ནས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གཞན་པ་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི་ཞུ་བ་ལས་བཙུན་པ་རེ་ཞིག་དགེ་སློང་བཟའ་བ་ལྔ་པོ་དག་མ་གཏོགས་པ་དེ་ལས་གཞན་པའི་དངོས་པོ་དག་སྤངས་པར་གྱུར་ནས་དེས་སླད་ཀྱི་བཟའ་བ་ལྔ་པོ་དག་འཚལ་བར་གྱུར་ན་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 487]
ཐུག་པ་ལས་ཞེས་བྱ་བ་ནི་གཞན་ནོ། །

[Block 488]
མི་རུང་བ་མ་འདྲེས་པ་ཞེས་བྱ་བ་ནི། གང་ཞིག་དེར་རུང་བ་དེས་འདི་ལ་རུང་བ་ཉིད་ཤེས་པར་མི་བྱ་སྟེ་ཞེས་བྱ་བའི་དོན་དུ་འདི་ཡིན་ནོ། །

[Block 489]
སྟོབས་པ་འཐོབ་ཕྱོགས་ནས་འགྲེང་བ་ཞེས་བྱ་བ་ནི་གཞན་ལས་བྱིན་ལེན་མི་འཐོབ་པ་དང་བྱིན་ལེན་ལས་བཟློག་པ་གང་ཡིན་པ་དེ་ལ་འདིར་ཡན་ལག་ཉིད་ཀྱི་ཕྱིར་འདི་ཤེས་པ་ཡིན་ཏེ། འཐོབ་པའི་ཕྱོགས་ནས་འགྲེང་བ་འདི་ལྟ་བུའི་ཁ་ཟས་ལ་བྱིན་ལེན་བྱེད་ཅིང་བཟློག་པར་བྱ་སྟེ། ཁ་ཟས་སྤངས་པ་དང་འདུག་པ་ཆོག་ཤེས་པའི་གནས་ལ་སྤངས་པ་གང་ཡིན་པ་དེ་ནི་སྤངས་པ་ཡིན་ཞེས་བྱ་བ་ནི་འདིར་བསྡུས་པའི་དོན་ཏོ། །

[Block 490]
གསོལ་ཅིག་ཅེས་བྱ་བ་ཡང་དེ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་ཞེས་བྱ་བ་ནི་དེ་ལ་སྦྱིན་པར་གྱུར་པ་གང་ཡིན་པ་དེ་ཙམ་འདིས་རྣམ་པར་མ་སྤྱད་པ་ལ་བརྟེན་པར༌[^291]གྱུར་པ་དེ་བས་ན་གཞན་དེ་ལས༌[^292]བཟློག་པ་ཉིད་དོ། །

[Block 491]
སོང་ཤིག་ཅེས་བྱ་བ་ཡང་ངོ་། །འཚལ་ལགས་སོ་ཞེས་བྱ་བས་ཀྱང་ངོ་ཞེས་བྱ་བ་ལས་བཟློག་པ་ནི་ཀྱང་ངོ་ཞེས་བྱ་བའི་སྒྲ་ནི་སྔར་ཡང་ངོ་ཞེས་བྱ་བའི་རྗེས་བསྙགས་པའི་ཕྱིར་རོ། །

[Block 492]
རེ་ཞིག་ཅེས་བྱ་བའི་སྒྲ་ཉེ་བར་སྦྱར་ན་ནི་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདི་གསུམ་རེ་ཞིག་སྒྲ་ལ་ཉེ་བར་མཚམས་སྦྱར་བ་ལ་བཟློག་པར་མི་འགྱུར་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 493]
ཆོག་གོ་ཞེས་བྱ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལ་ཡང་རེ་ཞིག་ཅེས་བྱ་བའི་སྒྲ་ཉེ་བར་སྦྱར་ན་སྤངས་པ་མ་ཡིན་ན་སླར་གཞན་དག་ལ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 494]
ཐུག་པ་ལས་ཀྱང་ཞེས་བྱ་བ་གང་ཞིག་བརྗོད་པ་དེ་ལ་སླར་བརྗོད་པར་འདོད་ནས༌[^293]ཁ་གཟར་གྱེན་དུ་འགྲེང་དུ་མི་བཏུབ་པ་ཉིད་ཀྱི་ཐུག་པ་དག་ནི་ཐུག་པ་ཉིད་དོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁ་གཟར་གྱེན་དུ་གནས་པ་གང་ཡིན་པ་དེ་གལ་ཏེ་ཐུག་པ་ལ་གྱེན་དུ་འགྲེང༌[^294]དུ་མི་བཏུབ་ན་དེ་ལྟར་ན་འདི་ལ་ནི་ཐུག་པ་ཉིད་དོ། །

[Block 495]
སོར་མོ་ལྔ་མི་མངོན་པ་ནི་སྐྱོ་མའོ་ཞེས་བྱ་བ་ནི་ཐུག་པ་ཉིད་ལེན་དུ་བཅུག་པ་ལ་ཞེས་བྱ་བ་འདི་དང་འབྲེལ་པ་བརྗོད་པར་བྱའོ། །
--- END BLOCKS ---
