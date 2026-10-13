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
ཞེས་གཞལ་ཡས་ཁང་པ་བསྒོམ་པའི་རིམ་པའོ། །

[Block 107]
དེ་ནས་གཞལ་ཡས་ཁང་པའི་དབུས་སུ་པདྨ་འདབ་མ་སྣ་ཚོགས་པ་དང་། དེའི་ཤར་ལ་སོགས་པའི་ཕྱོགས་སུ་སྣ་ཚོགས་པདྨ་བཞི་དང་། ཇི་སྲིད་སྒོ་བའི༌[^61]བར་དུ་སྣ་ཚོགས་པདྨ་སུམ་ཅུ་རྩ་གཉིས་བསྒོམ་པར་བྱའོ། །

[Block 108]
དབུས་ཀྱི་གདན་དང་མཱ་མ་ཀཱིའི་གདན་དང་། ཁྲོ་བོ་བཅུའི་ཉི་མའི་གདན་དུ་ཤེས་པར་བྱའོ། །

[Block 109]
ལྷག་མ་རྣམས་ནི༌[^62]ཟླ་བའི་གདན་ནོ། །

[Block 110]
དབུས་སུ་སྣ་ཚོགས་པདྨ་དང་ཉི་མའི་སྟེང་དུ་བཅོམ་ལྡན་འདས་ཁ་དོག་གནག་པ་ཞལ་གསུམ་པ་ཕྱག་དྲུག་པ། ཅུང་ཟད་མཆེ་བ་གཙིགས་ཤིང་ཚམ་དམ་པ་འོག་ནས་འཆད་པའི་ཕྱག་མཚན་འཛིན་པ་རྡོ་རྗེའི༌[^63]སྐྱིལ་མོ་ཀྲུང་གིས་བཞུགས་པ་བཅོམ་ལྡན་འདས་མ་རེག་བྱ་རྡོ་རྗེ་མ་དང་སྙོམས་པར་ཞུགས་པ། ཞི་བ་དང་སྒེག་པ་དང་ཁྲོ་བོའི་ཉམས་དང་ལྡན་པ་མྱུར་བའི་ཏིང་ངེ་འཛིན་གྱིས་རྫོགས་པ་མི་བསྐྱོད་རྡོ་རྗེ་བསྒོམ་པར་བྱའོ། །

[Block 111]
དེ་བཞིན་དུ་ཡང་ཤར་ལ་སོགས་པའི་ཕྱོགས་སུ་རྣམ་པར་སྣང་མཛད་ལ་སོགས་པ་ཞལ་གསུམ་པ་ཕྱག་དྲུག་པ༌[^64]དཀར་བ་ལ་སོགས་པའི་མདོག་དང་ལྡན་པ་ལ་སོགས་པ་དང་སྙོམས་པར་ཞུགས་པ་བསམ་པར་བྱའོ། །

[Block 112]
མཚམས་རྣམས་ལ་ཡང་སྤྱན་ལ་སོགས་པའི་རིགས་ཀྱི་ལྷ་མོ་རིགས་དང་རྗེས་སུ་མཐུན་པ་བསྒོམ་པར་བྱའོ། །

[Block 113]
ཕྱིའི་མཚམས་བཞི་ལ་གཟུགས་རྡོ་རྗེ་མ་ལ་སོགས་པ་དེ་བཞིན་དུ་བསམ་པར་བྱའོ། །

[Block 114]
ཤར་གྱི་སྣམ་བུ་ལ་སའི་སྙིང་པོ་དང་བྱམས་པ་དག་གོ། །

[Block 115]
ལྷོའི་སྣམ་བུ་ལ་ཕྱག་ན་རྡོ་རྗེ་དང་ནམ་མཁའི་སྙིང་པོའོ། །

[Block 116]
ནུབ་ཀྱི་སྣམ་བུ་ལ་འཇམ་དཔལ་དང་སྤྱན་རས་གཟིགས་ཀྱི་དབང་ཕྱུག་གོ། །

[Block 117]
བྱང་གི་སྣམ་བུ་ལ་སྒྲིབ་པ་ཐམས་ཅད་རྣམ་པར་སེལ་བ་དང་ཀུན་ཏུ་བཟང་པོ་དག་བསྒོམ་པར་བྱའོ། །

[Block 118]
སྒོ་རྣམས་སུ་གཤིན་རྗེ་གཤེད་ལ་སོགས་པ་དང་སྒོའི་མཚམས་སུ་མི་གཡོ་མགོན་ལ་སོགས་པ་དང་། སྟེང་དང་འོག་ཏུ་གཙུག་ཏོར་འཁོར་ལོས་སྒྱུར་བ་དང་གནོད་མཛེས་ཀྱི་རྒྱལ་པོ་བསྒོམ་པར་བྱའོ། །

[Block 119]
དེ་དག་གི་ཁ་དོག་དང་ཕྱག་མཚན་ལ་སོགས་པའི་བྱེ་བྲག་འོག་ནས་འཆད་པར༌[^65]འགྱུར་རོ་ཞེས་ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་ཉེ་བར་བསྟན་ཏོ། །

[Block 120]
དེ་ནས་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་འདི་དག་ཐམས་ཅད་ལྷའི་ངོ་བོ་ཉིད་ཐ་མལ་པའི་ལུས་རྣམ་པར་དག་པས་ཁྱད་པར་ཅན་གྱི་ལྷའི་རྣམ་པའི་བདག་ཉིད་ཡིན་ཡང་སྤྲོས་པ་ཡིན་པས། དེ་རྣམ་པར་དག་པར་བྱ་བའི་ཕྱིར་ཐམས་ཅད་སྟོང་པ་ཉིད་ངོ་བོ་ཉིད་དོན་དམ་པའི་དཀྱིལ་འཁོར་དུ་ཐིམ་པར་བྱའོ། །

[Block 121]
དེའི་རིམ་པ་འདི་ཡིན་ཏེ། གཟུགས་ཀྱི་ཕུང་པོ་སྤྱི་བོར་རྣམ་པར་སྣང་མཛད་དང་སྤྱན་མ་དང་གཟུགས་རྡོ་རྗེ་མ་དང་སའི་སྙིང་པོ་དང་བྱམས་པ་དང་གཤིན་རྗེ་མཐར་བྱེད་དང་མི་གཡོ་མགོན་རྣམས་འཇུག་པར་བྱའོ། །

[Block 122]
ཚོར་བའི་ཕུང་པོ་ལྟེ་བར་རིན་ཆེན་འབྱུང་ལྡན་དང་མཱ་མ་ཀཱི་དང་སྒྲ་རྡོ་རྗེ་མ་དང་ཕྱག་ན་རྡོ་རྗེ་དང་ནམ་མཁའི་སྙིང་པོ་དག་དང་ཤེས་རབ་མཐར་བྱེད་དང་འདོད་པའི་རྒྱལ་པོ་དག་འཇུག་པར་བྱའོ། །

[Block 123]
འདུ་ཤེས་ཀྱི་ཕུང་པོའི་མགྲིན་པར་འོད་དཔག་ཏུ་མེད་པ་དང་གོས་དཀར་མོ་དང་རྡོ་རྗེ་དྲི་མ་དང་འཇམ་དཔལ་དང་སྤྱན་རས་གཟིགས་ཀྱི་དབང་ཕྱུག་དང་པདྨ་མཐར་བྱེད་དང་དབྱུག་སྔོན་ཅན་འཇུག་པར་བྱའོ། །

[Block 124]
འདུ་བྱེད་ཀྱི་ཕུང་པོ་རྐང་པ་དག་ལ་དོན་ཡོད་གྲུབ་པ་དང་དམ་ཚིག་སྒྲོལ་མ་དང་རོ་རྡོ་རྗེ་མ་དང་སྒྲིབ་པ་ཐམས་ཅད་རྣམ་པར་སེལ་བ་དང་ཀུན་ཏུ་བཟང་པོ་དང་བགེགས་མཐར་བྱེད་དང་སྟོབས་པོ་ཆེ་རྣམས་འཇུག་པར་བྱའོ། །

[Block 125]
རྣམ་པར་ཤེས་པའི་ཕུང་པོ་སྙིང་གར་སྐུའི་དཀྱིལ་འཁོར་དེ་དག་ཐམས་ཅད་དང༌[^66]གཙུག་ཏོར་དང་གནོད་མཛེས་ཀྱང་འཇུག་པར་བྱའོ། །

[Block 126]
རྣམ་པར་ཤེས་པའི་ཕུང་པོ་ཡང་ནམ་མཁའི་དབྱིངས་ཞེས་བྱ་བ་འོད་གསལ་བ་ལ་འཇུག་པར་བྱའོ། །

[Block 127]
དེའི་རིམ་པ་ནི་རེག་བྱ་རྡོ་རྗེ་མ་དང་སྙོམས་པར་ཞུགས་པའི་དབང་གིས་ཚངས་པའི་བུ་ག་ན་གནས་པའི་རྩའི་འཁོར་ལོའི༌[^67]ནང་ནས་བྱང་ཆུབ་ཀྱི་སེམས་འཕོ་བའི་ཚེ། ཤེས་རབ་ཀྱི་ངོ་བོ་ཉིད་མཚན་མོའི་ཆ་སྟེ༌[^68]སྣང་བའོ། །

[Block 128]
ཡན་ལག་ཐམས་ཅད་ལ་ཁྱབ་པའི་དུས་སུ་ཉིན་མོའི་རང་བཞིན་ཐབས་ཀྱི་ངོ་བོ་ཉིད་སྣང་བ་མཆེད་པའོ། །

[Block 129]
རྡོ་རྗེ་ཆང༌[^69]ཟུངས་སུ་གནས་པའི་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཐིག་ལེ་གསུམ་འཕོ་བའི་གནས་སྐབས་སུ་མཚམས་ཀྱི་ངོ་བོ་ཉིད་ཤེས་རབ་དང་ཐབས་རོ་གཅིག་པའི་ཚུལ་ཅན་སྣང་བ་ཐོབ་པའོ། །

[Block 130]
དེའི་རྔས་ལ་གསང་བའི་རྡོ་རྗེའི་རྩེ་མོར་ནོར་བུའི་ཆར་བྱང་ཆུབ་ཀྱི༌[^70]སེམས་ཀྱི་བདེ་བ་ཉམས་སུ་མྱོང་བ་ཐོབ་པས་ཆགས་པ་དང་ཆགས་པ་དང་བྲལ་བ་དང་ཆགས་པ་བར་པ་རྣམས་སྤངས་པ་ཤེས་རབ་དང་ཐབས་དང་ཉེ་བར་ཐོབ་པ་དང་བྲལ་བ། ཐམས་ཅད་སྟོང་པའི་བདག་ཉིད་སྐད་ཅིག་མ་གང་ཤར་བ་དེ་འོད་གསལ་བའི་བདག་ཉིད་ཅན་སྐད་ཅིག་མ་ཡིན་པར་ཤེས་པར་བྱའོ། །

[Block 131]
སྣང་བ་ཉེ་བར་ཐོབ་པ་དང་འོད་གསལ་བའི་སྐད་ཅིག་མ་གཉིས་ཀྱི་བར་དུ་རྟགས་རྣམ་པ་ལྔ་དེ་ཁོ་ན་ཉིད་ལ་མཐོང་བ་ལ་མི་སླུ་བར༌[^71]བྱེད་པ་དེ་དག་བཤད་པར་བྱ་སྟེ། དེ་ལ་དང་པོ་སྨིག་རྒྱུའི་རྣམ་པ་དང་།

[Block 132]
གཉིས་པ་དུ་བའི༌[^72]རྣམ་པ་དང་།

[Block 133]
གསུམ་པ་མཁའ་སྣང་གི་རྣམ་པ་དང་།

[Block 134]
བཞི་པ་མར་མེའི་རྣམ་པ་དང་།

[Block 135]
ལྔ་པ་སྤྲིན་མེད་པའི་ནམ་མཁའ་དང་མཚུངས་པར་ཤེས་པར་བྱའོ། །

[Block 136]
དེ་ལ་ས་ཆུ་ལ་ཐིམ་པས་སྨིག་རྒྱུའི་རྣམ་པ་དང་། ཆུ་མེ་ལ་ཐིམ་པས་དུ་བའི་རྣམ་པ་དང་། མེ་རླུང་ལ་ཐིམ་པས་མཁའ་སྣང་གི་རྣམ་པ་དང་། རླུང་ནམ་མཁའ་ལ་ཐིམ་པས་མར་མེའི་རྣམ་པ་དང་། ནམ་མཁའ་འོད་གསལ་བ་ལ་ཐིམ་པས་སྤྲིན་མེད་པའི་ནམ་མཁའ་ལྟ་བུ་སྐྱེ་བར་འགྱུར་ཞེས་རྟགས་ཀྱི་དབྱེ་བའོ། །

[Block 137]
དེ་ནས་བདེ་བ་ཆེན་པོ་ཞེས་བྱ་བའི་རྣམ་གྲངས་ཅན་འོད་གསལ་བ་འབྱུང་བར་འགྱུར་རོ། །

[Block 138]
དེ་ཉིད་ཀྱི་ཡབ་ཡུམ་གཉིས་ཀ་ཞུ་བར་གྱུར་ནས་ཟླ་བ་ཉ་བ༌[^73]བཞིན་དུ་གནས་པ་སྟོང་པ་ཉིད་གཅིག་པུའི་བདག་ཉིད་ཅན་དུ་གྱུར་པ། འོད་གསལ་བའི་རང་བཞིན་དུ་བསྒོམ་པར་བྱ་ཞེས་པ་འདི༌[^74]ནི་དོན་དམ་པའི་བདེན་པ་ལ་འཇུག་པའོ། །

[Block 139]
དེ་བརྟན་པར་བྱ་བའི་ཕྱིར་སྔགས་འདི་བརྗོད་པར་བྱ་སྟེ། ཨོཾ་ཤཱུ་ནྱ་ཏཱ་ཛྙཱ་ན་བཛྲ་སྭ་བྷཱ་བ་ཨཱཏྨ་ཀོ྅ཧཾ། ཞེས་དོན་དམ་པའི་དཀྱིལ་འཁོར་ཉེ་བར་བསྟན་པའོ། །

[Block 140]
ཇི་སྐད་དུ་རྩ་བའི༌[^75]རྒྱུད་ལས་ཀྱང་།

[Block 141 [VERSE]]
སྐུ་ཡི་རྡོ་རྗེར་ཆུད་པ་ཡི། །
སངས་རྒྱས་ཆོ་ག་བཞིན་བསམས་ཏེ། །
དོན་དམ་པ་ཡི་རྡོ་རྗེ་ཡིས། །
དེ་བཞིན་ཉིད་དུ་འཇུག་པར་བྱ། །

[Block 142 [VERSE]]
དེ་བཞིན་གཤེགས་པའི་ཚོགས་བསད་ན། །
དངོས་གྲུབ་ངེས་པར་ཐོབ་པར་འགྱུར། །

[Block 143]
ཞེས་འབྱུང་ངོ་། །དེའི་རྗེས་ལ་སྔོན་དུ་བཤད་པའི་པདྨའི་སྟེང་དུ་ཡི་གེ་གསུམ་ལས་བྱུང་བའི་ཉི་མ་དང་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་དེ་བཞིན་གཤེགས་པའི་རིགས་དང་རྗེས་སུ་མཐུན་པའི་ཁ་དོག་རྣམ་པར་བསྒོམས་ཏེ། དེའི་སྟེང་དུ་ཡི་གེ་གསུམ་ལས་བྱུང་བའི་ཟླ་བའི་དཀྱིལ་འཁོར་བསམས་ཏེ། འོག་གི་ཟླ་བ་དང་ཉི་མ་དང་པདྨ་དང་ཟླ་བའི་དཀྱིལ་འཁོར་དེ་ཉིད་དུ་བཞུགས་པར་བསམ་མོ། །

[Block 144]
རྣམ་པར་བྱང་བའི་ཞེན་པ་ཡོངས་སུ་བཟློག་པར་བྱ་བའི་ཕྱིར་སྔགས་འདི་བརྗོད་པར་བྱ་སྟེ། ཨོཾ་དྷརྨ་དྷཱ་ཏུ་ཛྙཱ་ན་བཛྲ་སྭ་བྷཱ་བ་ཨཱཏྨ་ཀོ྅ཧཾ། དེ་ནས་ཟླ་བའི་དཀྱིལ་འཁོར་གྱི་སྟེང་དུ་ཡི་གེ་གསུམ་པོ་སྔར་བཤད་པའི་ཁ་དོག་ཅན་རྣམ་པར་དགོད་དེ།

[Block 145]
ཡི་གེ་གཉིས་ཐུགས་ཀྱི་རྡོ་རྗེའི་ས་བོན་ལ་ངེས་པར་འཇུག་ཅིང་དེ་ཡོངས་སུ་གྱུར་པ་ལས།
--- END BLOCKS ---
