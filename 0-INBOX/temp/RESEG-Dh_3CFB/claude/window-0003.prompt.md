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
[Block 106]
འདོད་ཆགས་ལ་སོགས་པ་ནི་བདག་དང་བདག་གིར་ཞེན་པ་སྔོན་དུ་འགྲོ་བ་ཅན་ཡིན་ཏེ། ཉེས་པ་ཐམས་ཅད་སྐྱེ་བའི་སྔོན་དུ་འགྲོ་བ་ནི་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 107]
ལུས་ལ་སོགས་པ་རྒྱུ་ཉིད་ནི་ཡིན་མོད་ཀྱི་འབའ་ཞིག་པ་རྣམས་ལ་ནི་ནུས་པ་མེད་པས་མི་མཐུན་པའི་ཕྱོགས་ལ་འཇུག་པ་མ་མཐོང་དུ་ཟིན་ཀྱང་རྗེས་སུ་དཔག་པ་ལྷག་མ་དང་ལྡན་པའི་ཕྱིར། ཐེ་ཚོམ་ཟ་བ་ཡིན་ནོ། །

[Block 108]
དེ་བཞིན་དུ།

[Block 109 [VERSE]]
མི་མཐུན་ཕྱོགས་ལ་མ་མཐོང་བ། །
ཙམ་གྱི་འབྲས་སྤྱི་མཐོང་བ་ལས། །
གཏན་ཚིགས་ཤེས་པ་ཚད་ལྟར་སྣང་། །
ཚིག་ལས་ཆགས་ཅན་ལ་སོགས་བཞིན། །

[Block 110]
གཡོ་བ་དང་ཚིག་ལ་སོགས་པ་ནི་འདོད་ཆགས་ལ་སོགས་པ་ཁོ་ནའི་འབྲས་བུ་མ་ཡིན་ཏེ། བརྗོད་པར་འདོད་པའི་སྤྱིའི་རྒྱུ་ཅན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 111]
གལ་ཏེ་དེ་ཉིད་འདོད་ཆགས་ཡིན་ནོ་ཞེ་ན། འདོད་པ་ཡིན་པའི་ཕྱིར་ཅུང་ཟད་ཀྱང་གནོད་པར་མི་འགྱུར་རོ། །

[Block 112]
འདོད་ཆགས་ནི་སེམས་ཀྱི་མངོན་པར་ཞེན་པ་རྟག་པ་དང་བདེ་བ་དང་བདག་དང་བདག་གིར་ལྟ་བས་འཕངས་པ་ཟག་པ༌[^64]དང་བཅས་པའི་ཆོས་ཀྱི་ཡུལ་ཅན་ཡིན་པར་སྨྲའོ། །

[Block 113]
སྙིང་རྗེ་ལ་སོགས་པ་ནི༌[^65]དེ་ལྟ་བུ་མ་ཡིན་ཏེ། གཞན་དུ་ཡང་སྲིད་པའི་ཕྱིར་རོ་ཞེས་བསྟན་པར་བྱའོ། །

[Block 114]
ཇི་ལྟར་ཆགས་པ་སྨྲ་བ་ལྟར་འདོད་ཆགས་དང་བྲལ་བ་ཡང་དེ་དང་འདྲ་བས་ཚིག་ཙམ་ལས་མི་རྟོགས་སོ། །

[Block 115]
ཁྱད་པར་ལས་ཀྱང་མ་ཡིན་ཏེ། བསམ་པ་ནི་རྟོགས་པར་དཀའ་བའི་ཕྱིར། ཐ་སྙད་འཆོལ་བས་ཐམས་ཅད་འཁྲུལ་པའི་ཕྱིར་རོ། །

[Block 116]
གལ་ཏེ་དགོས་པ་མེད་པའི་ཕྱིར་མི་སྨྲའོ་ཞེ་ན། མ་ཡིན་ཏེ། གཞན་གྱི་ཡོད༌[^66]ཡིན་པའི་ཕྱིར་རོ། །

[Block 117]
གལ་ཏེ་འདོད་ཆགས་དང་བྲལ་བའི་ཕྱིར་རིགས་པ་མ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། སྙིང་རྗེས་ཀྱང་འཇུག་པའི་ཕྱིར་རོ། །ཅི་སྟེ་དེ་ཉིད་འདོད་ཆགས་ཡིན་ནོ་ཞེ་ན། འདོད་པ་ཡིན་ཏེ། ཕྱིན་ཅི་མ་ལོག་པ་ལས་བྱུང་བའི་ཕྱིར་ཉེས་པ་མེད་དོ། །

[Block 118]
སྙིང་རྗེ་ནི་བདག་ཏུ་འཛིན་པ་མེད་ཀྱང་སྡུག་བསྔལ་གྱི་ཁྱད་པར་མཐོང༌[^67]ཙམ་གྱིས་གོམས་པའི་སྟོབས་ལས་སྐྱེ་བ་ཡིན་ཏེ། འདི་ལྟར་བྱམས་པ་ལ་སོགས་པ་ནི་སེམས་ཅན་དང་ཆོས་ལ་སོགས་པ་ལ་དམིགས་པ་ཡིན་པར་འདོད་དོ། །

[Block 119]
དེ་དག་ཀྱང་རིགས་མཐུན་པ་ལ་གོམས་པས་འབྱུང་བ་ཅན་ཡིན་གྱི། འདོད་ཆགས་ལ་ལྟོས་པ་ཅན་ནི་མ་ཡིན་ནོ། །

[Block 120]
འདོད་ཆགས་ལ་སོགས་པ་ནི་དེ་ལྟ་མ་ཡིན་ཏེ། ཕྱིན་ཅི་ལོག་མེད་ན་མེད་པའི་ཕྱིར་རོ། །

[Block 121]
གལ་ཏེ་སྙིང་རྗེ་ཅན་གྱི་རྩོམ་པ་འབྲས་བུ་མེད་པ་ཡང་ཕྱིན་ཅི་ལོག་ལས་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། གཞན་གྱི་དོན་ཁོ་ན་འབྲས་བུ་ཉིད་དུ་འདོད་པའི་ཕྱིར་རོ། །

[Block 122]
འབྲས་བུའི་མཚན་ཉིད་ནི་འདོད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 123]
རྣམ་པ་ཐམས་ཅད་དུ་ཡང་དག་པ་མ་ཡིན་པ་སྒྲོ་འདོགས་པ་མ་ཡིན་པའི་ཕྱིར་ཉེས་པ་མེད་དོ། །

[Block 124]
དེ་ལས་གཞན་པས་ཉེས་པ་དང་ལྡན་པ་ཉིད་དུ་བསྒྲུབས༌[^68]ན་ནི་མི་འདོད་པ་ཅུང་ཟད་ཀྱང་མེད་དོ། །

[Block 125]
སྨྲ་བ་པོ་བདག་ལ་འདོད་ཆགས་ལ་སོགས་པ་མཐོང་བས་གཞན་ལ་དེ་རྗེས་སུ་དཔོག་ན་ནི་ཧ་ཅང་ཐལ་བར་འགྱུར་རོ། །

[Block 126]
འཁྲུལ་པའི་ཕྱིར་གཞན་རྗེས་སུ་མི་དཔོག་ན་ནི་འདི་ལ་མི་འཁྲུལ་ལོ་ཞེས་བྱ་བའི་ངེས་པ་ཅི་ཞིག་ཡོད། ཚིག་གིས་ནི་བྱེད་པའི་ཡོན་ཏན་དང་བརྗོད་པས༌[^69]འདོད་པ་ཉིད་དག་རྗེས་སུ་དཔོག་པར་བྱེད་དོ། །

[Block 127]
འདོད་ཆགས་བསྐྱེད་པར་རུང་བ་ཉིད་དང་བྲལ་བ་ལ་སྨྲ་བ་མ་མཐོང་བའི་ཕྱིར། [^70]དེ་རྗེས་སུ་དཔོག་ན་ཡང་ཧ་ཅང་ཐལ་བར་འགྱུར་རོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 128]
འདོད་ཆགས་ཀྱིས་ཕན་མི་འདོགས་ན་ནི། ཇི་ལྟར་དེའི་ནུས་པས་ཕན་འདོགས་པར་འགྱུར། ནུས་པས་ཕན་འདོགས་ན་ནི། དེ་ཉིད་ཀྱིས་ཕན་བཏགས་པར་འགྱུར་བ་ཞིག་ན། དེ་ནི་མེད་དོ་ཞེས་བཤད་ཟིན་ཏོ། །

[Block 129]
དེ་ལྟ་བས་ན་མེད་ན་མི་འབྱུང་བའི་འབྲས་བུ་ཁོ་ནས་རྒྱུ་རྗེས་སུ་དཔོག་པར་བྱེད་དོ།[^71] །དེ་ལ་རག་ལས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 130]
གཞན་ནི་མི་མཐུན་པའི་ཕྱོགས་ལ་མ་མཐོང་བ་ཡང་མ་ཡིན་ནོ། །

[Block 131]
ཐམས་ཅད་གཟིགས་པའི་གཟིགས་པ་ལོག་པས་ནི། ཐམས་ཅད་ན་མེད་པ་གོ་བར་བྱེད་དོ། །

[Block 132]
ལ་ལ་ན་དེ་ལྟར་མཐོང་བ་རྣམས་ཀྱང་དུས་དང་འདུ་བྱ་བའི་ཁྱད་པར་ལས་གཞན་དུ་སྣང་བའི་ཕྱིར་ཏེ། དཔེར་ན་སྒྱུ་རུ་རའི་ཤིང་དག་འོ་མས་བཅུས་ན་འབྲས་བུ་མངར་པོ་ཆགས༌[^72]ལ། ཕལ་ཆེར་ནི་དེ༌[^73]ལྟར་མི་སྣང་བ་ལྟ་བུའོ། །

[Block 133]
དེས་ན་འདི་སྐད་དུ་བདག་ལྟ་བུའི་སྨྲ་བ་པོ་ནི༌[^74]འདོད་ཆགས་ཅན་ཡིན་ནོ་ཞེས་བརྗོད་པར་རིགས་པར༌[^75]འགྱུར་ཏེ། འདོད་ཆགས་སྐྱེ་བའི་རྐྱེན་གྱི་ཁྱད་པར་བདག་ཏུ་ལྟ་བ༌[^76]དང་། ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པ་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 134]
དེའི་ཚེ་ཡང་སྨྲ་བ་དཔེ༌[^77]བརྗོད་པ་ནི་དོན་མེད་དེ། [^78]དེའི་ཕྱིར་མི་མཐུན་པའི་ཕྱོགས་ལ་མ་མཐོང་བ་ནི་གཏན་ཚིགས་སུ་མི་རུང་ངོ་། །

[Block 135 [VERSE]]
མི་མཐུན་ཕྱོགས་ལ་མ་མཐོང་བ། །
ཙམ་གྱིས་འཁྲུལ་པ་མེད་པ་མིན། །
འཁྲུལ་པ་སྲིད་པ་ཅན་ཉིད་ཕྱིར། །
ཕྲུ་བའི་འབྲས་ནི་ཚོས་པ༌[^79]བཞིན། །

[Block 136]
མང་པོ་ཞིག་ཚོས་པ་མཐོང་དུ་ཟིན་ཀྱང་ཕྲུ་བའི་ནང་དུ༌[^80]འདུག་པ་ཙམ་གྱིས་ཚོས་པར་མི་འགྲུབ་སྟེ། འཁྲུལ་པ་མཐོང་བའི་ཕྱིར་རོ། །

[Block 137]
འདི་ལྟར་འདི་ལྟ་བུའི་རང་བཞིན་ལ། འདི་དང་ཚོགས་པའི༌[^81]རྒྱུ་འདྲ་བ་ཅན་དག་ནི་ཚོས་སོ་ཞེས་བྱ་བར་ནི་རུང་ངོ་། །དེ་ལྟ་མ་ཡིན་ན་ནི་རྗེས་སུ་དཔག་པ་དེ་ལྷག་མ་དང་ལྡན་པའི༌[^82]འཁྲུལ་པ་ཅན་ཡིན་ནོ། །

[Block 138 [HEADING]]
## ལྷག་མ་དང་ལྡན་པ། ^2-0

[Block 139]
ཡང་ལྷག་མ་དང་ལྡན་པ་ཞེས་བྱ་བ་འདི་ཅི་ཞིག་ཅེ༌[^83]ན།

[Block 140 [VERSE]]
གང་ཞིག་མ་མཐོང་བ་ཙམ་གྱིས། །
ལྡོག་པ་རབ་ཏུ་སྟོན་བྱེད་པ། །
དེ་ནི་ཐེ་ཚོམ་རྒྱུ་ཡིན་ཕྱིར། །
དེ་ལ་ལྷག་མ་ལྡན་ཞེས་བརྗོད། །

[Block 141]
དེའི་ལྡོག་པ་དེ་ནི་མ་ངེས་པས་མི་མཐུན་པའི་ཕྱོགས་ལ་འཇུག་པར་ཐེ་ཚོམ་ཟ་བར་འགྱུར་ཏེ། ལྡོག་པ་སྒྲུབ་པ་མ་མཐོང་བ་ཙམ་ནི་ཐེ་ཚོམ་གྱི༌[^84]རྒྱུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 142]
མི་དམིགས་པ་ཐམས་ཅད་ནི་རྟོགས་པར་བྱེད་པ་མ་ཡིན་ནོ། །

[Block 143]
དེའི་ཕྱིར་གཅིག་ལོག་པས་གཞན་ལྡོག་པར་འདོད་པས་ནི་དེ་གཉིས་རང་བཞིན་འབྲེལ་པ་འགའ་ཞིག་ཀྱང་འདོད་པར་བྱ་དགོས་སོ། །

[Block 144]
དེ་ལྟ་མ་ཡིན་ན་གཏན་ཚིགས་གོ་བར་བྱེད་པ་མ་ཡིན་པར་འགྱུར་རོ། །

[Block 145 [VERSE]]
གཏན་ཚིགས་ཀྱི་ནི་ཚུལ་གསུམ་ལའང་། །
དེ་ཡིས༌[^85]མ་གྲུབ་བཟློག་དོན་དང་། །
འཁྲུལ་པ་ཅན༌[^86]གྱི་གཉེན་པོར་ནི། །
ངེས་པ་བརྗོད་པར་མཛད་པ་ཡིན། །
--- END BLOCKS ---
