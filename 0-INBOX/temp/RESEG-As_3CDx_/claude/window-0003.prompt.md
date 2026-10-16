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
དུས་གཅིག་ན་ཞེས་བྱ་བ་ནི་དུས་གཅིག་གི་ཚེ་སྟེ། དེ་ཡང་ཉན་པའི་ཚེ་བར་ཆད་མེད་པའི་རྒྱུན་ལ་དུས་གཅིག་ཅེས་བྱའི། གཞན་དུ་ན་ཡི་གེ་དང་། རྩ་བ་དང་། ཚིག་གཟུང་བའི༌[^76]དུས་ཐ་དད་པའི་ཕྱིར༌[^77]ཅིག་ཅར༌[^78]བྱར་མི་རུང་ངོ་། །ཡང་ན་གཟུངས་ཐོབ་པས་ཡི་གེ་འབྲུ་གཅིག་ལ་ཆོས་ཐམས་ཅད་ཀྱི་རྣམ་གྲངས་ཡང་དག་པར་འཛིན་པའི་ཕྱིར་དུས་གཅིག་ཁོ་ན་ཡང་ཡིན་ནོ། །

[Block 107]
ཡང༌[^79]གཅིག་ཏུ་ན་རྣ་བའི་དབང་པོ་རྣམ་པར་དག་པ་ཐོབ་པས༌[^80]ཡི་གེ་འབྲུ་གཅིག་ཡོངས་སུ་རྟོགས་པས་གཞན་ལ་ཡང་ཐོགས་པ་མེད་པའི་ཕྱིར་ཡང་དུས་གཅིག༌[^81]ཁོ་ན་ཡིན་ནོ། །

[Block 108]
ཡང་རྣམ་གྲངས་གཞན་དུ་ན་དུས་ཞེས་བྱ་བའི་ཚོགས་པ་ལ་བྱ་སྟེ། དུས་གཅིག་ན་བཅོམ་ལྡན་འདས་འཁོར་དང་བཅས་པ་ཚོགས་སོ་ཞེས་ཚིག་འོག་མ་དང་སྦྱར་རོ། །

[Block 109]
དེ་ནི་དུས་ཕུན་སུམ་ཚོགས་པ་ཡིན་ཏེ། [^82]དེའི་ཕུན་སུམ་ཚོགས་པ་ནི་དེ་བཞིན་གཤེགས་པ་འཇིག་རྟེན་དུ་བྱུང་ཞིང་། མདོ་སྡེ་དཀོན་མཆོག་འདི་ལྟ་བུ་དག་མངོན་སུམ་དུ་ཐོས་པའི་སྐབས་ཡོད་པའོ། །

[Block 110]
གལ་ཏེ་དེ་ལྟར་ན་ཡང་རྫོགས་ལྡན་གྱི་དུས་ལ་སོགས་པ་ནི་སྐྱེ་དགུའི་ཚེ་ལོ་དཔག་ཏུ་མེད་ཅིང་ལོངས་སྤྱོད་ཀྱི་འབྱོར་པ་ཕུན་སུམ་ཚོགས་པ༌[^83]ཡང་ཡིན་པས་དུས་ཕུན་སུམ་ཚོགས་པ་ཞེས་གདགས་སུ་རུང་གི །འདིའི་ཚེ་ནི་རྩོད་པའི་དུས་ལ་བབ་སྟེ། སྙིགས་མ་ལྔ་བདོ་བ་ཡིན་ན་ཇི་ལྟར་དུས་ཕུན་སུམ་ཚོགས་པ་གདགས་སུ་རུང་ཞེ་ན། རྫོགས་ལྡན་གྱི་དུས་ལ་སོགས་པའི་ཚེ་ན་སྐྱེ་དགུའི་ཚེ་ལོ་དཔག་ཏུ་མེད་ཅིང་ལོངས་སྤྱོད་ཀྱི་འབྱོར་བ་ཕུན་སུམ༌[^84]ཚོགས་པ་ཡིན་ཡང་སྐྱེ་དགུ་གཅིག་ཏུ༌[^85]བག་མེད་པར་སྤྱོད་ཅིང་། དཀོན་མཆོག་གསུམ་གྱི་མཚན་ཡང་མི་གྲག་པ་ཡིན་པས་དུས་ཕུན་སུམ་ཚོགས་པ་ཞེས་མི་གདགས་ལ། དུས་མཐའི་ཚེ་ན་ནི་ནད་ལ་སོགས་པའི་བར་གྱི་བསྐལ་པས་གཡེན་སྤྱོ་ཞིང་དགེ་བའི་མིང་ཡང་མི་གྲག་པས༌[^86]དེ་ནི་དུས་ཀྱི༌[^87]ཐ་ཆད་ཡིན་གྱི། འདིའི་ཚེ་ན་རྩོད་པའི་དུས་ལ་བབ་ཏུ་ཟིན་ཀྱང་དེ་བཞིན་གཤེགས་པ་འཇིག་རྟེན་དུ་བྱུང་ཞིང་མདོ་སྡེ༌[^88]དཀོན་མཆོག་འདི་ལྟ་བུ་དག་མངོན་སུམ་དུ་ཐོས་པའི་སྐབས་ཡོད་པ་དང་། མངོན་པར་རྟོགས་པ༌[^89]མང་བ་དང་། གང་གིས༌[^90]དཀོན་མཆོག་གསུམ་གྱི་མཚན་ཐོས་པ་ཙམ་དང་། སེ་གོལ་གཏོགས་པའི་ཡུད་ཙམ་ཞིག་དགེ་བའི་སེམས་བསྐྱེད་པ་དེ་དག་ཐམས་ཅད་ཀྱང་དུས་གཞན་ན་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་མངོན་པར་རྫོགས་པར་འཚང༌[^91]རྒྱ་བར་འགྱུར་རོ་ཞེས་དེ་བཞིན་གཤེགས་པས་ལུང་སྟོན༌[^92]པའི་གནས་སྐབས་ཡིན་པས་གཅིག་ཏུ་སྙིགས་མ་ལྔ་བདོ་བ་ཡང་མ་ཡིན་པས་དེའི་ཕྱིར་དུས་ཕུན་སུམ་ཚོགས་པ་ཞེས་གདགས་སུ་རུང་ངོ་། །

[Block 111 [HEADING]]
#### སྟོན་པ་ཕུན་སུམ་ཚོགས་པ། ^3-1-2-0

[Block 112]
གང་གིས༌[^93]བཤད་ཅེ་ན། སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་སྟེ། དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས། བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 113]
དེ་ལ་བཅོམ་ལྡན་འདས་ཞེས་བྱ་བ་ནི་ལེགས་པ་རྣམ་པ་དྲུག་པོ་རང་དབང་དང་། རབ་ཏུ་སྦྱངས་པ་དང་། གཟུགས་བཟང་བ་དང་། གྲགས་པ་དང་། དཔལ་དང་། ཆེ་བ་ཉིད་སོགས་པ་ལ་བྱ་སྟེ། སྒྲ་ངེས་པར་སྦྱོར་བ་ལས་ཇི་སྐད་དུ།

[Block 114 [VERSE]]
རང་དབང་དང་ནི་རབ་སྦྱངས་དང་། །
གཟུགས་བཟང་བ་དང་གྲགས་པ་དང་། །
དཔལ་དང་ཆེ་བ་ཉིད་སོགས་པ། །
དྲུག་པོ་རྣམས་ལ་ལེགས་བཤད་ནི། །

[Block 115]
ཞེས༌[^94]འབྱུང་བ་ལྟ་བུའོ། །

[Block 116]
དེ་དག་ཐམས་ཅད་དེ་བཞིན་གཤེགས་པ་ལ་རྣམ་པ་ཐམས་ཅད་དུ་བྲལ་བ་མེད་དེ་མངའ་བས་ན་དེའི་ཕྱིར་དེ་བཞིན་གཤེགས་པ་ལ་བཅོམ་ལྡན་འདས་ཞེས་བྱའོ། །

[Block 117]
དེ་ལ་རང་དབང་ཇི་ལྟ་བུ་ན་ཉོན་མོངས་པས་གཞན་གྱི་དབང་དུ་འགྱུར་བ་མེད་པའི་ཕྱིར་རོ། །

[Block 118]
རབ་ཏུ་སྦྱངས་པ་ནི་ཡེ་ཤེས་ཀྱི༌[^95]མེའི་གདུང་བས་ཉོན་མོངས་པའི་བུད་ཤིང་རབ་ཏུ་བསྲེགས་པའི་ཕྱིར་རོ། །

[Block 119]
གཟུགས་བཟང་བ༌[^96]ནི་སྐྱེས་བུ་ཆེན་པོའི་མཚན་མཆོག་སུམ་ཅུ་རྩ་གཉིས་ལ་སོགས་པ་མངའ་བའི་ཕྱིར་རོ། །

[Block 120]
གྲགས་པ་ནི་ཡོན་ཏན་གྱི་ཁྱད་པར་ཐམས་ཅད་ཕུན་སུམ་ཚོགས་པའི༌[^97]ཕྱིར་རོ། །

[Block 121]
དཔལ་ནི་འགྲོ་བ་ཐམས་ཅད་ཀྱིས་བསྟེན་པར༌[^98]བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 122]
ཆེ་བ་ཉིད་ནི་སེམས་ཅན་ཐམས་ཅད་ལ༌[^99]རྣམ་པ་ཐམས་ཅད་དུ་ཕན་པ་དང་བདེ་བ་མཛད་པ་རྒྱུན་མི་འཆད་པར་སྦྱོར་བའི་ཕྱིར་རོ། །

[Block 123]
ཚོགས་པ་ཞེས་བྱ་བ་ནི་ལྡན་པའི་དོན་ཏོ། །

[Block 124]
[^100]རང་དབང་ལ་སོགས་པ་དྲུག་ཅར༌[^101]དང་སྦྱར་རོ། །

[Block 125]
ཡང་ཚིག་གི་དོན་རྣམ་པ་གཅིག༌[^102]ཏུ་ན། བདུད་བཞི་བཅོམ་པས་ན་བཅོམ་ལྡན་འདས་ཞེས་བྱ་སྟེ། བདུད་བཞི་ནི་ཕུང་པོའི་བདུད་དང་། འཆི་བདག་གི་བདུད་དང་། ཉོན་མོངས་པའི་བདུད་དང་། ལྷའི་བུའི་བདུད་དོ། །

[Block 126]
བཅོམ་ལྡན་འདས་ནི་ཟག་པ་བཞི་པོ་ལྟ་བའི་ཟག་པ་དང་། སྲེད་པའི་ཟག་པ་དང་། མ་རིག་པའི་ཟག་པ་དང་། འདོད་པའི་ཟག་པ་ཟད་པས་དེ་དག་གོ་རིམ༌[^103]བཞིན་དུ་བཅོམ་པར་རིག་པར་བྱའོ། །

[Block 127]
དེ་ནི་སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་ཡིན་ཏེ། དེའི་ཕུན་སུམ་ཚོགས་པ་ནི་ལེགས་པ་དྲུག་དང་ལྡན་པ་དང་བདུད་བཞི་བཅོམ་པ་ལ་སོགས་པ་བཅོམ་ལྡན་འདས་ཉིད་ཀྱི་རྒྱུད་ལ་མངའ་བའི་ཡོན་ཏན་དང་ལྡན་པའོ། །

[Block 128]
དེ་ལྟར་དུས་ཕུན་སུམ་ཚོགས་པ་དང་། སྟོན་པ་ཕུན་སུམ་ཚོགས་པ་དེ་གཉིས་ནི་མདོ་སྡེ་ཐམས་ཅད་སྤྱིར་འདྲ་བར་བསྟན་པ་ཡིན་པས་ན་ཐུན་མོང་གི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པ་ཞེས་བྱའོ། །

[Block 129]
ཐུན་མོང་གི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་ཟིན་ཏོ།། །།

[Block 130 [HEADING]]
### ཐུན་མོང་མ་ཡིན་པའི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པ། ^3-2-0

[Block 131]
དེ་ལྟར་ཐུན་མོང་གི་གླེང༌[^104]གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པ་བསྟན་ནས། ད་ནི་ཐུན་མོང་མ་ཡིན་པའི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པའི་ཚིག་གི་དོན་ལ་སོགས་པ་བཤད་པར་བྱ་སྟེ། དེ་ཡང་གང་ན་ཅི་འདྲ་བ་ཞིག་ཇི་ལྟ་བུ་དག་དང་བཞུགས་པའི་རིམ་གྱིས་མདོ་འདིའི་གླེང་གཞིའི་ཁྱད་པར་རྣམ་པར་གཞག་པའོ། །

[Block 132 [HEADING]]
#### གནས་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-0

[Block 133]
དེ་ནི་ཕུན་སུམ་ཚོགས་པ་རྣམ་པ་གསུམ་གྱིས་བསྟན་དེ།[^105] བཅོམ་ལྡན་འདས་ཀྱི༌[^106]གནས་ཕུན་སུམ་ཚོགས་པ་དང་། ཡོན་ཏན་ཕུན་སུམ་ཚོགས་པ་དང་། འཁོར་ཕུན་སུམ་ཚོགས་པ་དང་། དེ་ལ་གང་ན་བཞུགས་ཤེ་ན། གནས་ཕུན་སུམ་ཚོགས་པ་ན་སྟེ། དེའི་ཕྱིར་དེ་བསྟན་པའི་དབང་དུ་མཛད་ནས་གཞལ་མེད་ཁང་ཆེན་པོ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 134]
དེ་ལ་བཅོམ་ལྡན་འདས་ཀྱི་གནས་ཕུན་སུམ་ཚོགས་པ་ནི་སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པ་སྟེ། གཞལ་མེད་ཁང་ཆེན་པོ་བྱ་བའི་སྒྲ་ཉིད་ཀྱིས་བསྟན་ཏོ། །

[Block 135]
དེ་ནི་དང་པོ་ཁོ་ནས་བསྟན་དགོས་ཏེ། འཇིག་རྟེན་པ་ཐམས་ཅད་ལས་འདས་པ་ཐམས་ཅད་མཁྱེན་པའི་གནས་ཡིན་ནོ་ཞེས་ཡང་དག་པར་བསྟན་པའི་ཕྱིར་རོ། །

[Block 136]
དེ་བསྟན་པ་ཡང་གདུལ་བྱ་རྣམས་དེ་ལ་མོས་པ་བསྐྱེད་པ་དང་། སངས་རྒྱས་ཀྱི་ཞིང་ཡོངས་སུ་དག་པར་སྐྱེ་བར་སྨོན་ལམ་འདེབས་པ་དང་། རྒྱ་ཆེན་པོ་ལ་མོས་པའི་བྱང་ཆུབ་སེམས་དཔའ་རྣམས་དགའ་བ་ཡང་དག་པར་བསྐྱེད་པ་དང་། ལྷག་པའི་བསམ་པ་ལ་མོས་པ་རྣམས་ཀྱི་ལྷག་པའི་བསམ་པའི་ཁམས་བསྟན་པར་བྱ་བ་དང་། གང་དུ་བཞུགས་ཏེ་ཆོས་དཀོན་མཆོག་འདི་བཤད་པའི་གནས་དེ་ཡང་དག་པར་བསྟན་པའི་ཕྱིར་ཏེ། གཞན་དུ་ན་གང་དུ་བཞུགས་ཏེ་བཤད་པ་མི་ཤེས་པས་ཀུན་ལ་ཐེ་ཚོམ་དུ་འགྱུར་རོ། །

[Block 137]
དེའི་ཕུན་སུམ་ཚོགས་པ་ནི་རྣམ་པ་བཅོ་བརྒྱད་དུ་རིག་པར་བྱ་སྟེ། ཁ་དོག་ཕུན་སུམ་ཚོགས་པ་དང་། དབྱིབས་ཕུན་སུམ་ཚོགས་པ་དང་། ཚད་ཕུན་སུམ་ཚོགས་པ་དང་། ཡུལ་ཕུན་སུམ་ཚོགས་པ་དང་། རྒྱུ་ཕུན་སུམ་ཚོགས་པ་དང་། རང་བཞིན་ཕུན་སུམ་ཚོགས་པ་དང་། བདག་པོ་ཕུན་སུམ་ཚོགས་པ་དང་། ཞམ་འབྲིང་བ་ཕུན་སུམ་ཚོགས་པ་དང་། ཕྱོགས་ཕུན་སུམ་ཚོགས་པ་དང་། ལོངས་སྤྱོད་ཕུན་སུམ་ཚོགས་པ་དང་། བྱ་བ་སྒྲུབ་པ་ཕུན་སུམ་ཚོགས་པ་དང་། འཚེ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་དང་། ཕྱིར་རྒོལ་བ་མེད་པ་ཕུན་སུམ་ཚོགས་པ་དང་། གནས་ཕུན་སུམ་ཚོགས་པ་དང་། བདག་པོའི་གནས་ཀྱི་བྱེ་བྲག་ཕུན་སུམ་ཚོགས་པ་དང་། བཞོན་པ་ཕུན་སུམ་ཚོགས་པ་དང་། སྒོ་ཕུན་སུམ་ཚོགས་པ་དང་། རྟེན་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 138]
ཕུན་སུམ་ཚོགས་པ་རྣམ་པ་བཅོ་བརྒྱད་པོ་དེ་དག་ནི་མདོ་ལས།

[Block 139]
རིན་པོ་ཆེ་སྣ་བདུན་མཆོག་ཏུ་འབར་བ་བཀོད་པ། འཇིག་རྟེན་གྱི་ཁམས་དཔག་ཏུ་མེད་པ་རྒྱས་པར་འགེངས་པའི་འོད་ཟེར་ཆེན་པོ་རབ་ཏུ་བྱུང་བ༌[^107]ཞེས་བྱ་བ་ནས། རིན་པོ་ཆེའི་པདྨའི་རྒྱལ་པོ་ཡོན་ཏན་མཐའ་ཡས་པས་བརྒྱན་པའི་བཀོད་པ་ལ་བརྟེན་པ་ན་བཞུགས་ཏེ་ཞེས་གསུངས་པའི་བར་གྱི་ཚིག་བཅུ་དགུ་ལས་ཁ་དོག་ཕུན་སུམ་ཚོགས་པ་ནི་མདོའི་ཚིག་དང་པོ་གཉིས་དང་སྦྱར་རོ། །

[Block 140]
དབྱིབས་ཕུན་སུམ་ཚོགས་པ་ལ་སོགས་པ་ལྷག་མ་རྣམས་ནི་མདོའི་ཚིག་ལྷག་མ་རྣམས་དང་གོ་རིམ༌[^108]བཞིན་དུ་སྦྱར་རོ། །

[Block 141 [HEADING]]
##### ཁ་དོག་ཕུན་སུམ་ཚོགས་པ། ^3-2-1-1-0

[Block 142]
དེ་ལ་དང་པོ་ཁ་དོག་ཕུན་སུམ་ཚོགས་པ་བསྟན་པའི་དབང་དུ་མཛད་ནས། རིན་པོ་ཆེ་སྣ་བདུན་མཆོག་ཏུ་འབར་བ་བཀོད་པ་འཇིག་རྟེན་གྱི་ཁམས་དཔག་ཏུ་མེད་པ་རྒྱས་པར་འགེངས་པའི་འོད་ཟེར་ཆེན་པོ་རབ་ཏུ་འབྱུང་བ་ཞེས་བྱ་བ་གསུངས་སོ། །

[Block 143]
དེ་ལ་རིན་པོ་ཆེ་སྣ་བདུན་ཞེས་བྱ་བ་ནི་གསེར་དང་། དངུལ་དང་། བཻ་ཌཱུཪྻ་དང་། སྤུག་དང་། རྡོའི་སྙིང་པོ༌[^109]དང་། མུ་ཏིག་དམར་པོ་དང་། ཀེ་ཀེ་རུའོ། །

[Block 144]
མཆོག་ཏུ་འབར་བ་ཞེས་བྱ་བ་ནི་རིན་པོ་ཆེ་སྣ་བདུན་པོ་དེ་དག་ཉིད་ཁ་དོག་མཆོག་ཏུ་འབར་བའོ། །

[Block 145]
ཡང་ན་གཞལ་མེད་ཁང་ཆེན་པོའི་ཁྱད་པར་དེ་ཉིད་རིན་པོ་ཆེ་སྣ་བདུན་པོ་དེ་དག་གི་ཁ་དོག་མཆོག་ཏུ་འབར་བ་ལ་ཡང་བྱའོ། །
--- END BLOCKS ---
