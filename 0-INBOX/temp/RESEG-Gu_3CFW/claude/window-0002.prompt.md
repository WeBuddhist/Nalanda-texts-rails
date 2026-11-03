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
[Block 71]
མཐུད་མ་ཅན་དང་ལྷན༌[^69]རིངས་ཅན་དང༌[^70]ལྷན་པ་ཅན་དང་ཆག་ཅན་དང་ཟུངས་ཅན༌[^71]མ་ཡིན་པའོ། །

[Block 72]
བྱ་བ་འདིར་མ་ཡིན་པའོ་ཞེས་བྱ་བའི་སྒྲ༌[^72]འདི་ལྔ་ཆར་དང་སོ་སོར་སྦྱར་ཏེ། ཟུངས་ཅན་མ་ཡིན་ཏེའོ་ཞེས་བྱ་བའི་བར་དུའོ། །

[Block 73]
དེ་ལྟར་ཡང་ཐམས་ཅད་ལ་ཐུང་བ་ཉིད་དུ་བྱས་པ་ཉིད་དོ། །

[Block 74]
མཐུད་མ་ཅན་ཞེས་བྱ་བ་ལ། འདིར་གཞུང་ནི། ཚད་དུ་མཆོག་པ་དགེ་སློང་མང་པོ་དག་ལ་མཚམས་སྦྱར་བར་བྱེད་ཅིང་སྲ་བརྐྱང་འདིང་བར༌[^73]བྱེད་ན་བཏིང་ཞེས་བརྗོད་པར་བགྱིའམ། བཀའ་སྩལ་པ། མ་བཏིང་ཞེས༌[^74]བརྗོད་པར་བགྱིའོ་ཞེས་བྱ་བ་ལ་དེ་ལས་འདིར་གདིང་བར་བྱ་བ་བཀག་པའོ། །

[Block 75]
གདིང་བར་བྱ་བ་ནི་གང་ཞིག་དུམ་བུར་བྱ་སྟེ། བཙེམས་པར་མ་ཡིན་པ་དེའོ། །

[Block 76]
ལྷན་རིངས་ཅན་མ༌[^75]ཡིན་པ་ཞེས་བྱ་བ་ནི་གང་དུ་ལྷན་པ་རིང་པོར་གླན་པ་སྟེ། དེ་ལྟ་བུས་མ་གླན་པ་ནི་ལྷན་རིངས་ཅན་མ་ཡིན་པའོ། །

[Block 77]
ལྷན་པ་ཅན་ཞེས་བྱ་བ་ནི་གང་ལ་ཆུ་བུར་གྱི་རྣམ་པ་ལྟར་རློ་བ་ལྷན་པ་གཞན་གླན་པ་ཅན་མ་ཡིན་པའོ། །

[Block 78]
དེ་ནི་ཁ་ཅིག༌[^76]གིས་ལྷན་པ་ཞེས་བྱ་བར་བརྗོད་པ་ཡིན་ཏེ། འདི་ལ་དེ་ལས་དོན་ཐ་དད་པར་ཤེས་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 79]
གཡའ་བར༌[^77]བྱེད་པ་ཞེས་བྱ་བར་དབྱར་དང་བྱི་བའི་རྣམ་པ་གསད་པ༌[^78]ནི་འདིར་གཡའ་བར་བྱེད་པ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 80]
ཆ་ག་ཅན་ཞེས་བྱ་བ་ནི་ཆོས་གོས་དག་གི་མཐའ་ཐོག་ཐག་ཏུ་ཆ་ག་ཙམ་བཏབ་པ་སྟེ། གང་དུ་དེ་རྣམས་མེད་པ་དེ་ནི་ཆ་ག་མེད་པའོ། །

[Block 81]
ཐ་མ་ཟེགས་པ་དག་ལ་ཟུངས་ཅན་བྱད་པ༌[^79]དེ་གང་དུ་མེད་པ་དེ་ནི་ཟུངས་ཅན་མ་ཡིན་པའོ། །

[Block 82]
མཐའ་ཟེགས་པ་རྣམས་ལ་ཟུངས་ཅན་མ་བྱས་པ་ཉིད་ལ་ཡང་མི་མོས་པ་ཉིད་གཏན་པ་མ་ཡིན་པ་ཉིད་ཀྱི༌[^80]ཕྱིར་རིག་པར་བྱའོ། །

[Block 83]
སྤངས་པ་དང་རྒྱུ་མ་བཏགས་པ་དང་བྲལ་ཕྲད་མ་ཡིན་པའོ་ཞེས་བྱ་བ་ནི། འདིར་ཡང་མ་ཡིན་པ་ཞེས་བྱ་བའི་སྒྲ་སོ་སོར་སྦྱོར་ཏེ། ཉེ་བར་གནས་པ་དང་མི༌[^81]རུང་བ་བཀག་པ་དག་ལ་འདིར་སྤངས་པ་མ་ཡིན་པ་དང་བྲལ་ཕྲད་མ་ཡིན་པ་ཞེས་བྱ་བ་གྲངས་ཇི་ལྟ་བ་བཞིན་དུ་བསྡུ་བའོ། །

[Block 84]
འདིར་གཞུང་ནི།

[Block 85]
བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 86]
རྒྱུ་མ་བཏགས་པ་ཞེས་བྱ་བ་ནི་རུང་བ་མ་ཡིན་པའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། སྤངས་པ་ཉེ་བར་གཞག་པ་ཞེས་བྱ་བ་ནི་འདིར་ཞུ་བ་ལས་ཀྱང་གསུངས་སོ། །

[Block 87]
ཆོས་གོས་གཞག་པ་གང་ཡིན་ཞེ་ན། འདིར་ཞུ་བ་ལས་ཆོས་གོས་གང་ཞག་བཅུ་འདས་པའམ་ཞག་གཅིག་བྲལ་བའོ་ཞེས་གསུངས་ཏེ། འདི་དག་གི་འཇུག་པ་ཙམ་ནི་འདི་རྒྱུ་མཚན་དུ་བྱས་ཏེ། གང་ཞིག་སྔར་སྤངས་པར་གྱུར་པ་དང་དེ་ལྟར་ནི་མི་རུང་བ་དེ་ཡིན་ཏེ། ཞག་ལོན་པར་བརྗོད་པར་ངེས་པའི་ཕྱིར་རོ། །

[Block 88]
བྲལ་ཕྲད་ཅེས་བྱ་བ་འདིས་ཕྱག་དར་ཁྱོད༌[^82]ཀྱང་བཀག་པའོ། །

[Block 89]
འདིར་བྲལ་ཕྲད་ཀྱི་སྒྲས༌[^83]ནི་ཐམས་ཅད་ཕྱག་དར་ཁྲོད་ཀྱི་དོན་ཅན་ཏེ། སྔར་བོར་བའི་ཚེ་ན་བདག་པོ་དང་བྲལ་བ་ཡིན་ལ་ཕྱིས་བླངས་པའི་ཚེ་ན་བདག་པོ་གཞན་དང་ཕྲད་པ་དེ་ཙམ་ཞིག་ཉེ་བར་བླངས་པའོ། །

[Block 90]
གང་ཞིག༌[^84]ཕྱིར་འདི་ལྟར་བྲམ་ཟེའི་བུ་མོས་ཞུས་པ་ལས།

[Block 91]
ཆོས་གོས་བྲལ་ཕྲད་གང་ཞེ་ན། ཆོས་གོས་གང་ལམ་ཀ་ནས་བྱུང་སྟེ། ལམ་དུ་བོར་བ་ལས་རྙེད་པ་གང་ཡིན་པའོ་ཞེས་གསུངས་པ་དེའི་དོན་མཐོང་བ་ཡིན་ནོ། །

[Block 92]
དྲས་ཤིང་དྲུབས་པའོ་ཞེས་བྱ་བ་ནི་བྱིན་གྱིས་བརླབ་ཏུ་མི་རུང་བ་ནི་མ་ཡིན་ནོ། །

[Block 93]
དེའི་ཕྱིར་སྦྱར་མ་ཉིད་ཀྱང་གང་གི་ཚེ་བྱིན་གྱིས་བརླབ་པར་གསུངས་པ་གང་ཡིན་པ་དེ་ཡང་འདིས་བསྡུས་པ་ཡིན་ནོ། །

[Block 94]
ཟིན་པའོ། །

[Block 95]
ལྔ་པའོ། །

[Block 96]
ལྷག་མ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཁྲུ་ལྔ་པོ་དག་ལ་འདི་ལ་དགེ་འདུན་གྱིས་ཁྱབ་པ་ཡིན་པའི་ཕྱིར། ལུས་འབའ་ཞིག་ལ་ནི་མ་ཡིན་ཏེ། དེའི་ཕྱིར་ལྷག་མ་ལ་ཉེས་པ་མེད་དོ། །

[Block 97]
གདིང་བ་ཞེས་བྱ་བའི་ཚད་ཇི་སྙེད་པ་དེ་ཙམ་གྱི་རྐྱེན་གྱི་ནང་དུ་འདུས་པ་ལས་ལྷག་མ་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 98]
ཡོ་བྱད་རྣམས་ལ་དེར་འབྱུང་བའི་ཕྱིར་བསྒྲུབ་པ་ནི་དགེ་འདུན་གྱི༌[^85]གནས་སུ་རྙེད་པའི་ཕྱིར་འབྱུང་བའི་ཞིང་རེ་རེ་ལ་སྲ་བརྐྱང་གདིང་བ་བསྐྱེད་པའོ། །

[Block 99]
འདིར་ཐམས་ཅད་དུ་དམན་པ་ནི་དགེ་འདུན་གྱིས་རྣམ་པར་གཞག་པ་རིགས་པ་ཡིན་ནོ། །

[Block 100]
དེ་ལྟ་བས་ནི་འདིར་གཞིའི་ཚད་ཀྱི་འབྱོར་པ་ཇི་སྙེད་པ་དེའི་ཁུངས་སུ་བསྡུས་པ་དེ་ལས་ལྷག་པ༌[^86]མ་ཡིན་པ་ཞེས་བྱ་བ་འགྲུབ་བའོ། །

[Block 101]
ཁ་ཅིག་ན་རེ། ཆོས་གོས་སུམ༌[^87]ཕྲུགས་བཞི་པས་ལྷག་པར༌[^88]བཏིང་བ་ལ་ཡང་དོན་དེར་འབྱུང་བ་ཉིད་ཀྱི་ཕྱིར་ཡོ་བྱད་རྣམས་ལྷག་པར་འབྱོར་པ་མི་བརླག་པ་རྣམས་ཀྱིས་བརྟེན་པར་བྱ་སྟེ། བྱེ་བྲག་མེད་པའི་ཕྱིར་རོ། །

[Block 102]
ཡང་བདེ་བར་གཤེགས་པའི་ཆོས་གོས་ཤིན་ཏུ་ཆེན་པོ་ལ་ཡང༌[^89]འཕགས་པ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 103]
སྔར་མ་བཏིང་བའོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ལོ་གཞན་ལ་གཏན་པ་ཉིད་དུ་སྔར་མ་བཏིང་བ་ནི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 104]
བཏིང་བའོ་ཞེས་བྱ་བ་ནི་སྤྲོག་མའི་ནང་དུ་བཏིང་བ་སྟེ་བསྡུས་ཏེ་གཞག་པ་ནི་མ་ཡིན་ནོ།[^90] །དུ་མ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཆོས་གོས་སུམ༌[^91]ཕྲུགས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 105]
དགེ་འདུན་གྱི་ཚོགས་དུ་མ་ཡོད་པའི་ཕྱིར་ཆོས་གོས་སུམ་ཕྲུགས་དུ་མ་ཡང་འདིར་མཐུན་པ་ཡིན་ནོ། །

[Block 106]
དེ་ཇི་སྙེད་པའི་འདིང་བར་བྱེད་པའོ་ཞེས་བྱ་བ་ལ། དེའི་སྒྲས་ནི་ཆོས་གོས་སུམ་ཕྲུགས་ལ་བཟུང་ངོ་། །ཆོས་གོས་སུམ་ཕྲུགས་དེ་ཇི་སྙེད་པ་དེ་སྙེད་ཀྱི་གདིང་བར༌[^92]བྱེད་པའི་དགེ་སློང་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 107]
དེ་ནི་ཆོས་གོས་གཞན་བྱིན་གྱིས་བརླབ་པ་ཡིན་པས་དེའི་ཕྱིར་བྱིན་གྱིས་བརླབས་པ༌[^93]དག་ཕྱུང་ནས་སོ་ཞེས་བྱ་བ་ནི་ཚོགས་པ་ལ་མི༌[^94]བརྟེན་པས་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། རང་གི་རྫས་ནི་དོན་དུ་ངེས་པར་སྦྱར་བ་འདི་ཡིན་ཏེ། གང་གིས་ནི་མཐུན་པའོ། །

[Block 108]
བདག་པོས་མི་འདོར་བའི་རྫས༌[^95]དོན་ལ་ངེས་པར་སྦྱོར་བ་མ་ཡིན་ཏེ། དེ་ལྟ་བས་ན་བདག་པོ་རྣམས་ཀྱིས་འདིར༌[^96]འདོད་པས་བླང་བར་བྱའོ།[^97] །ཅི་ཚོགས་པ་རྗེས་སུ་བགྲང་བར་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་ཞག་མ་ལོན་པར་ཚོགས་པས་མོས་པར་བྱའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཚོགས་པ་ཁས་ལེན་པ་ལ་རྩོམ་པ་འདིའོ། །

[Block 109]
མངོན་སུམ་དུ་ཕྱོགས་པའི་དབང་གིས་ཚོགས་པ་འབྱོར་པའོ། །

[Block 110]
ཚོགས་པ་ལ་ཚོགས་པས་མངོན་དུ་ཕྱོགས་པ་ཉིད་ནི་ཤིན་ཏུ་སྟོབས་དང་ལྡན་པ་སྟེ། དེ་ལྟ་བས་ན་ཆོ་ག་འདི་གང་གི་ཚེ་ཞེ་ན། དེའི་ཕྱིར་ཞག་མ་ལོན་པར་ཞེས་བྱ་བ་སྨོས་ཏེ། ཞག་མ་ལོན་པ་ནི་ཉི་མ་གང་ལ་ཆོས་གོས་དེ་འབྱོར་པའི་ཉི་མ་དེ་ཉིད་ལ་བདག་པོ་རྣམས་ཀྱིས་ཚོགས་པ་དེ་ལ་འདོད་པར་བྱ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
