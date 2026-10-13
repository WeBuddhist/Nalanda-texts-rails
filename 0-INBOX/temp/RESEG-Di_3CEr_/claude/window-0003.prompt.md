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
དམིགས་པའི་རྐྱེན་འབའ་ཞིག་ལས་ཤེས་པ་ནི་མ་ཡིན་ནོ། །

[Block 107]
སེམས་དང་སེམས་ལས་བྱུང་བ་རྣམས་གཞི༌[^60]ལས་སྐྱེ་བའོ༌[^61]ཞེས་གྲུབ་པའི་མཐའ་ལས་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 108 [VERSE]]
དམིགས་པའོ་ཞེ་ན་དྲན་སོགས་ཀྱི། །
ཤེས་པའང་གཞན་ལ་ལྟོས་མ་ཡིན། །

[Block 109]
གལ་ཏེ་དོན་དེ༌[^62]ལས་ཞེས་པ་འདིས་ཡུལ་ཙམ་ཡིན་ན་ནི་དྲན་པ་དང་། རྗེས་སུ་དཔག་པ་དང་མངོན་པར་འདོད་པ་ལ་སོགས་པའི་ཤེས་པ་ཡང་དམིགས་པར་བྱ་བ་གཞན་ལ་མི་ལྟོས་ཏེ། དུད་པ་ལ་སོགས་པ་དམིགས་ནས་མེ་ལ་སོགས་པའི་ཤེས་པ་སྐྱེ་བ་ནི་མ་ཡིན་ནོ། །

[Block 110]
གཟུགས་ལ་སོགས་པ་ཉིད་ལ་དམིགས་པ་ལ༌[^63]དོན་དུ་བརྗོད་པར་བྱ་གྲང་ན། ཅི་ཤེས་པ་སྐྱེ་བ་དེ་ལྟར་སྣང་བ་དེ་ལ་དེ་བཞིན་དུ་དམིགས་ནས་སྐྱེ་བ་ཡིན་ནམ། དེ་སྟེ་གཞན་དུ་སྣང་དུ་ཟིན་ཀྱང་ཇི་ལྟར་ཡོད་པའི་དེ་རྒྱུར་འགྱུར་བ་ཡིན་གྲང་། དེ་ལས་ཅིར་འགྱུར་ཞེ་ན། གལ་ཏེ་ཇི་ལྟ་བ་དེ་ལས་ཤེས་པ་སྐྱེ་ན་ནི་དེ་ལྟར་ན་བསགས་པ་ལ་དམིགས་པ་ཡིན་པའི་ཕྱིར་ལྔ་པོ་ཀུན་རྫོབ་པར་འགྱུར་ཏེ། དེ་ཉིད་ལ་དམིགས་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 111]
སྔོན་པོ་ལ་སོགས་པར་སྣང་བའི་ཤེས་པ་ལ་དོན་དེ་ལས་སྐྱེས་པའི་ཤེས་པ་མངོན་སུམ་དུ་འགྱུར་རོ་ཞེས་འདོད་པ་དེ་ལྟ་ན་ནི་ཚོགས་ལ་དེ་དག་ལ་ཁས་བླངས་པ་བདེན་ཡང་ཡོད་པའི་རྫས་ཀྱི་རྣམ་པ་ཉིད་ཐོབ་སྟེ། དེ་ཉིད༌[^64]རྫས་ལ་སོགས་པ་ཉིད་དུ་སྣང་བས་ན་རྫས་དང་གྲངས་ལ་སོགས་པའི་རྣམ་པ་ཡང་འཐོབ་བོ། །

[Block 112]
དེ་སྟེ་ཇི་ལྟར་ཡོད་པ་རྒྱུར་འགྱུར༌[^65]ན་ནི་དེ་ལྟར་རྫས་ལ་སོགས་པ་ནི་ཐལ་བའི་ཉེས་པར་མི་འགྱུར་ཏེ་དེ་ལྟར་ན་དེ་དག་མེད་པའི་ཕྱིར་རོ། །

[Block 113]
དེ་ལྟར་ན་ཡང་གངགང་ཡང༌[^66]ཐ་སྙད་དུ་བྱ་བ་སྟེ་དེ་ནི་འཐོབ་པར་མི་འགྱུར་ཏེ། དེ་དག་སོ་སོ་ལ་ཤེས་པ་ཡོད་པ༌[^67]མ་ཡིན་ནོ། །

[Block 114]
སོ་སོ་བ་དེ་དག་འདུས་པ་རྒྱུ་ཡིན་ཡང་དེ་འདུས་པར་ཡོད་པ་ལ་སོགས་པ་ནི་ཁས་མ་བླངས་སོ། །

[Block 115]
དེ་ཉིད་སྨྲས་པ། །

[Block 116 [VERSE]]
ཇི་ལྟར་སྣང་བ་དེ་ཡོད་མིན། །
དེ་ཡི་ཕྱིར་ན་དོན་དམ་དུ། །
སེམས་ཀྱི་དམིགས་པ་ལྔ་རྣམས་སོ། །
དེ་ལ་ཐ་སྙད་དུ་མ་བྱས། །

[Block 117]
དམིགས་པ་ལ་སོགས་པ་ཡང་དམིགས་པར་བྱ་བ་ཉིད་དུ་ཐལ་བར་འགྱུར་ཏེ། དེ་དག་ནི་དོན་དམ་པར་ཡོད་པས་སོ། །

[Block 118]
གཞན་དུ་ན་ཡོད་པ་མ་ཡིན་པ་ཟླ་བ་གཉིས༌[^68]ལ་སོགས་པར་སྣང་བ་ཡང་སྔོན་པོ་ལ་སོགས་པར་སྣང་བའི་ཤེས་པའི་རྒྱུར་འགྱུར་རོ། །

[Block 119]
དོན་གྱི་ཚུལ་གྱིས་དབེན་པ་ཡང་བརྗོད་བྱ་མ་ཡིན། ཤེས་པ་ཐམས་ཅད་དོན་གྱི་ཚུལ་དང་བྲལ་ན་ཡང་ཐ་སྙད་དུ་བྱ་བར་མི་ནུས་སོ། །

[Block 120]
ཡུལ་འདིའི་ཡང་།

[Block 121 [VERSE]]
སྤྱི་ཡི་ཚུལ་གྱིས་བསྟན་པར་བྱ། །
དེས་ན་ཐ་སྙད་དུ་མི་བྱ། །

[Block 122]
རྣམ་པར་ཤེས་པ་ལྔ་རྣམས་ཀྱི་ཡུལ་དེའི༌[^69]ཚུལ་གྱིས་ཐ་སྙད་དུ་བྱ་བ་ཡིན་གྱི་རང་གི་ངོ་བོའི་ཚུལ་གྱིས་ཐ་སྙད་དུ་བྱ་བ་ནི་མ་ཡིན་ནོ། །

[Block 123]
སྤྱིའི་ངོ་བོའི་ཚུལ་ལས་ནི་གཟུགས་ལ་སོགས་པ་ཐ་སྙད་དུ་བྱེད་དོ། །

[Block 124]
དེའི་ཕྱིར་རྣམ་པར་ཤེས་པ་ལྔ་རྣམས་ཀྱི་ཡུལ་ནི་ཐ་སྙད་དུ་བྱ་བར་མི་ནུས་སོ་ཞེས་བྱ་བ་ནི་རྩོད་པ་སྒྲུབ་པ་ལའོ།[^70] །

[Block 125 [HEADING]]
#### རིགས་པ་ཅན་རྣམས་ཀྱི་མངོན་སུམ། ^1-4-2-0

[Block 126]
རིགས་པ་ཅན་རྣམས་ནི་དབང་པོ་དང་དོན་ཕྲད་པ་ལས་སྐྱེས་པའི་ཤེས་པ་ཐ་སྙད་དུ་བྱས་པ་མ་ཡིན་པ་འཁྲུལ་པ་མེད་པ་ཞེན༌[^71]པའི་བདག་ཉིད་ནི་མངོན་སུམ་མོ་ཞེས་ཟེར་རོ། །

[Block 127]
འདི་ཡང་རིགས་པ་མ་ཡིན་ཏེ་ཁྱད་པར་འདི་དག་ནི་མི་གཤའོ། །

[Block 128]
གང་གི་ཕྱིར།

[Block 129 [VERSE]]
དབང་པོ་ལས་བྱུང་དོན་བློ་ལས།[^72] །
ཐ་སྙད་ལ་སོགས་སྲིད་མ་ཡིན། །

[Block 130]
འཁྲུལ་པ་སྲིད་པའི་ཡུལ་ལ་ནི་ཁྱད་པར་དུ་བྱ་གྲང་ན། ཐ་སྙད་དུ་བྱ་བའི་ཡུལ་ལ༌[^73]ནི་རྗེས་སུ་དཔག་པ་ལས་ཡིན་གྱི། དབང་པོའི་བློ་ནི་ཐ་སྙད་ཀྱི་ཡུལ་ཉིད་དུ་སྲིད་པ་མ་ཡིན་ནོ།[^74] །

[Block 131]
དེའི་ཕྱིར་མ་འཁྲུལ་པའི་ཁྱད་པར་བསྟན་པར་མི་བྱ་བ་ཉིད་དོ། །

[Block 132]
དབང་པོའི་བློ་ཐ་སྙད་དུ་བྱ་བར་མི་ནུས་པ་དེའི་ཕྱིར་ཁྱད་པར་དུ་བྱ་བ་ཚིགས༌[^75]མི་བྱ་བ་ཉིད་དོ། །

[Block 133]
འཁྲུལ་པའི་ཁྱད་པར་ཉིད་ཀྱང་སྲིད་པ་མ་ཡིན་ཏེ། འཁྲུལ་པ་ནི་ཡིད་ལ་སྟེ། དེ་འཁྲུལ་པའི་ཡུལ་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 134]
ཞེན་པ༌[^76]ནི་ངེས་པ་སྟེ། དེ་སྤྱི་ལ་སོགས་པ་དང་ལྡན་པའི་དྲི་ལ་སོགས་པ་ལ་རྟོག་པར༌[^77]མི་བྱེད།[^78] མི་མཐོང་བ་དེ་བས༌[^79]མི་སྲིད་དོ། །

[Block 135]
ཅི་སྟེ་དོན་ཇི་ལྟ་བ་ལ་སོགས་པའི་ཤེས་པའི་ལྡོག་འཚམས༌[^80]སུ་བརྗོད་དོ་ཞེ་ན། དེ་ལྟ་ན་ཁྱད་པར་དུ་བྱེད་པའི་ཚིགས༌[^81]རིགས་པ་མ་ཡིན་ཏེ། མ་འཁྲུལ་པའི་ཕྱིར་ཡང་དབང་པོའི་བློ་ཐམས་ཅད་རང་རང་གི་དོན་ཙམ་འཛིན་པར་བྱེད་པ་ཡིན་ནོ། །

[Block 136]
དེ་དག་གིས་ནི་བཤད་པའི་རྣམ་པར་རྟོག་པ་ལ༌[^82]ཡང་སོ་སོར་བརྗོད་དོ། །

[Block 137]
གང་སྨྲས་པ་ཞེན་པའི་བདག་ཉིད་ཅེས་པ་ལ་ཞེན་པ་ནི་འབྲས་བུ་ཡིན་ན་དེ་དབང་པོའི་བློ་ལ་མི་སྲིད་དེ། དོན་ཇི་ལྟ་བ་ལ་སོགས་པའི་ཤེས་པ་ཉིད་དངོས་ཀྱི་འབྲས་བུ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 138]
ཅི་སྟེ་ཐ་སྙད་དུ་བྱ་བ་མ་ཡིན་པ་ལ་སོགས་པ་སྨོས་པ༌[^83]ནི་ཤེས་པ་དེའི་རང་གི་ངོ་བོ་བསྟན་པར་བྱ་བའི་ཕྱིར་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ་མངོན་སུམ་གྱི་མཚན་ཉིད་བརྗོད་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་ལ། དེ་ལ༌[^84]དབང་པོ་དང་དོན་དུ་ཕྲད་པ་ཉིད་ཀྱིས་གྲུབ་པའི་ཕྱིར་རོ། །ཤེས་པའི་རང་གི་ངོ་བོ་བསྟན་པར་བྱ་བའི་ཕྱིར་ཡིན་ན་ཡང་ཡོན་ཏན་དང་རྫས་རྩོམ་པར་མི་བྱེད་པ་དང་། ནམ་མཁའ་ལ་སོགས་པ་ཤེས་པར་བྱ་བའི་ཡུལ་མ་ཡིན་པ་ཉིད་ཀྱང་བསྟན་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་ཧ་ཅང་ཐལ་བར་འགྱུར་རོ། །

[Block 139]
ཐམས་ཅད་དུ་ཕྲད་ནས་སྐྱེ་བ་མངོན་སུམ་དུ་འདོད་ན་ནི།

[Block 140 [VERSE]]
བར་དང་བཅས་པ་འཛིན་པ་དང་། །
ཤེས་པ་ལྷག་པའང་མི་ཐོབ༌[^85]འགྱུར། །

[Block 141]
རི་ལ་སོགས་པ་ལ་ནི་ཡུལ་དང་དབང་པོ་བར་མེད་པ་སྟེ་བར་དང་བཅས་པ་ཡིན་བཞིན་དུ་འཛིན་པ་མཐོང་མོད༌[^86]ཀྱི། དབང་པོ་ལྷག་པར་འཛིན་པ་ནི་རིགས་པ་མ་ཡིན་ནོ། །

[Block 142]
ཕྱི་རོལ་དུ་འཇུག་པའི་ཕྱིར་འཐད་པ་ཉིད་དོ། །

[Block 143]
དབང་པོ་གཉིས་ཀྱི༌[^87]རྟེན་ལས་ཕྱི་རོལ་དུ་འཇུག་པ་སྟེ། དེས་ན་ཡུལ་དེ༌[^88]བར་དང་བཅས་པ་ལྷག་པར་འཛིན་པ༌[^89]ཡང་འཐད་པ་ཡིན་ནོ་ཞེ་ན། དེ་ཡང་རིགས་པ་མ་ཡིན་ཏེ། གང་གི་ཕྱིར། རྟེན་ལས་དབང་པོ་ཕྱིར་མིན་པར། །གྲུབ་པོ་ཞེས་བྱ་བ་ཚིག་གི་ལྷག་མའོ། །

[Block 144]
དབང་པོ་ནི་རྟེན༌[^90]གྱི་ཡུལ་ཉིད་ལ་གནས་པ་སྟེ། དེར་གསོ་བ་ལ་སོགས་པ་ལ་རབ་ཏུ་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 145]
དེས་ན་དབང་པོ་ཁོ་ན་བར་དུ་ཆོད་པའི་དོན་འཛིན་པར་བྱེད་དོ། །
--- END BLOCKS ---
