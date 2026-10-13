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
[Block 3431]
དང་པོ་རྗེས་སུ་ཆགས་པར་བྱ་བའི་ཕྱིར། དེའི་པདྨ་ལ་ཧཱུཾ་གིས་བྱིན་གྱིས་རློབ་པའི༌[^2211]མིག་དང་ལྕགས་ཀྱུ་དང་བ་དན་དང་སྡིགས་མཛུབ་ཀྱི་ཕྱག་རྒྱ་རྣམས་ལས་གང་ཡང་རུང་བ་བཅུག་ལ། གྲང་བ་མ་ཡིན་པའི་རེག་པའི་བར་དུ་བསྐྱེད་པར༌[^2212]བྱས་ལ། བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་རྒྱུན་འབྱུང་བར་འགྱུར་བའི་ཚེ་འདོད་ཆགས་ཆེན་པོའི་དབང་གིས་རང་གི་མགྲིན་པ་ནས་བཟུང་སྟེ་རྣམ་པར་བསམས་ལ། དེ་དང་འཁྱུད་པ་དང་འོ་ལ་སོགས་པ་རྣམ་པ་བརྒྱད་དེའི་སྐད་འཇམ་པོ༌[^2213]དགའ་བའི་རང་བཞིན་ཐོས་ནས། ཨོཾ་སརྦ་ཏ་ཐཱ་ག་ཏ་ཨ་ནུ་རཱ་ག་ན་བཛྲ་སྭ་བྷཱ་ཝ་ཨཱཏྨ་ཀོ྅ཧཾ། ཞེས་འདིས་ནི་རྡོ་རྗེ་དང་པདྨ་ཡང་དག་པར་བཙིར་ལ། ཨོཾ་སརྦ་ཏ་ཐཱ་ག་ཏ་པཱུ་ཛ་བཛྲ་སྭ་བྷཱ་ཝ་ཨཱཏྨ་ཀོ྅་ཧཾ། ཞེས་བྱ་བའི་སྔགས་ཀྱིས་བསྐྱོད་ཅིང་། དམ་པ་དགའ་བའི་སྒྲས་ཕྱོགས་བཅུ་ན་གནས་པའི་དེ་བཞིན་གཤེགས་པ་བཀུག་ལ་ངག་གི་ལམ་དུ་འཇུག་པར་བྱས་ལ། རྩ་དབུ་མ་ནས་རྡོ་རྗེ་ནོར་བུའི་རྩེ་མོར་བྱང་ཆུབ་ཀྱི་སེམས་ཐིག་ལེར་བསམས་ཏེ། འདོད་ཆགས་དང་འདོད་ཆགས་བྲལ་བ་དང་འདོད་ཆགས་བར་མའི༌[^2214]རིམ་གྱིས་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་མྱོང་ནས་འཆད་པར་འགྱུར་བའི་བཛྲ་དྷྀཀ་ཅེས་བྱ་བ་ལ་སོགས་པའི་ཕྱུང་བའི་སྔགས་ཀྱིས་དེ་བཞིན་གཤེགས་པ་ལ་སོགས་པ་སྤྲོ་བར་མཛད་དོ་ཞེས་དགོངས་སོ། །

[Block 3432]
འོད་གསལ་བའི་ཏིང་ངེ་འཛིན་ལས་བཞེངས་ནས་ཞེས་བྱ་བ་ནི་བདེ་བ་ཆེན་པོའི་ཏིང་ངེ་འཛིན་ལས་སོ། །

[Block 3433]
ཉོན་མོངས་པ་ལྔས་ཁྱབ་པའི་སེམས་ཅན་གྱི་ཁམས་ལ༌[^2215]གཟིགས་ནས་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་ལ་སོགས་པའི་སྐྱོན་གྱིས་ཡོངས་སུ་ཁྱབ་པར་རྣམ་པར་གཟིགས་ནས་སོ། །

[Block 3434]
ཉོན་མོངས་པའི་རང་བཞིན་ཡོངས་སུ་ཤེས་པ་ཞེས་པ་ནི་གཟོད༌[^2216]མ་ནས་མ་སྐྱེས་པའི་རང་བཞིན་དེ་ཁོ་ན་ཉིད་ཤེས་པའོ། །

[Block 3435]
བྱང་ཆུབ་ཡིན་ལ་ནི་རྡོ་རྗེ་འཆང་ཉིད་དོ། །

[Block 3436]
དེའི་ངོ་བོ་ཉིད་བདག་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདོད་ཆགས་ལ་སོགས་པ་ཉོན་མོངས་པ་ཡོངས་སུ་ཤེས་པའི་རང་བཞིན་རྡོ་རྗེ་འཆང་ཆེན་པོའི༌[^2217]བདག་ཡིན་ནོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3437]
གདུལ་བྱ་རྣམས་ཀྱིས༌[^2218]ཉོན་མོངས་པ་ཞེ་སྡང་རྣམ་པར་སྦྱང་བའི་ཞེས་པ་ནི་ཉེ་བར་མཚོན་པ་ཙམ་ཡིན་ཏེ། དེའི་འབྲེལ་པ་དང་ལྡན་པའི༌[^2219]ཁྲོ་བ་ལ་སོགས་པ༌[^2220]ཉེ་བའི་ཉོན་མོངས་པ་རྣམས་ཀྱང་རྣམ་པར་སྦྱང་བར་བྱ་བའི་ཕྱིར་ཞེས་པའི་ཐ་ཚིག་གོ། །

[Block 3438]
ཐུགས་རྗེ་ཆེན་པོའི་ཐབས་ནི་ཐུགས་རྗེ་ཆེན་པོའི་ཐབས་གང་ལ་ཡོད་པ་དེ་ནི་ཐབས་ཅན་ཏེ༌[^2221]ཁྲོ་བའོ། །

[Block 3439]
གང་གི་ཕྱིར་བཅོམ་ལྡན་འདས་ནི་ཐུགས་རྗེ་ཆེན་པོས་དྲག་པོའི་གཟུགས་མཛད་ཀྱིས་ཞེ་སྡང་གིས་ནི་མ་ཡིན་ནོ། །

[Block 3440]
ཇི་སྐད་དུ།

[Block 3441 [VERSE]]
ཤིན་ཏུ་མ་རུངས་གདུག་པ་ལ། །
ཞི་བ་ཉིད་དུ་མི་རིགས་སོ། །

[Block 3442]
ཞེས་དཔལ་བདེ་མཆོག་ལས་འབྱུང་བས་སོ། །

[Block 3443]
དེ་བས་ན་བཅོམ་ལྡན་འདས་སྙིང་རྗེ་ཆེན་པོས་ཁྱབ་པ་ཡང་གདུག་པ་འདུལ་བར་བྱ་བའི་ཕྱིར་ཕྱིའི་ཁྲོ་བོའི་གཟུགས་འཆང་བར་འགྱུར་རོ། །

[Block 3444 [VERSE]]
ཉི་མའི་འོད་ཀྱིས་བསྲོས་པའི༌[^2222]མཚོ་ཆེན་དང་མཚུངས་པ། །
སྙིང་རྗེ་ཆེན་པོ་ཅན་རྣམས་ཁྲོ་བོའི་སྐུ་དང་ལྡན། །

[Block 3445 [VERSE]]
ནང་ནི་གངས་དང་འདྲ་སྟེ༌[^2223]བསིལ་བ་སྟེ། །
འགྲོ་བ༌[^2224]འདུལ་ཞིང་ཕྱི་ཡི་ཁྲོ་བོར་སྣང་། །

[Block 3446]
ཞེས་འབྱུང་ངོ་། །འདོད་པའི་འབྲས་བུ་བསྐྱེད་པས་ན། །ཞེས་པ་ནི་འདོད་པའི་འབྲས་བུ་ནི་ཆོས་ཀྱི་དབྱིངས་ཀྱི་ཡེ་ཤེས་ཀྱི་མཚན་ཉིད་དོ། །

[Block 3447]
དེ་བསྐྱེད་པ་ནི་ཐོབ་པར་བྱེད་པས་སོ། །

[Block 3448]
སྔགས་ནི་དངོས་སུ་མི་བསྐྱེད་པ༌[^2225]བརྗོད་པར་བྱ་བ་ཡིན་ཞེས་སྟོན་པའོ། །

[Block 3449]
བློ་ལ་གཞག་པ་ནི་སྡུད་པ༌[^2226]པོའི་བློ་ལ་གནས་པའོ། །

[Block 3450]
སྙོམས་པར་ཞུགས་པ་ལས་ཞེས་པ་ནི་སྔར་བཤད་པའི་རེག་བྱ་རྡོ་རྗེ་མའི་པདྨ་དང་རྡོ་རྗེ་མཉམ་པར་སྦྱོར་བ་ལས་ཡང་དག་པར་འབྱིན་པར་མཛད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3451]
སྒྲ་ཇི་བཞིན་པ་ནི༌[^2227]མི་བསྐྱོད་པ་སྤྲོ་བ་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3452]
དཀྱིལ་འཁོར་ལ་སོགས་ཞེས་སོགས་པའི་སྒྲས་ཤེས་པར་བྱའོ། །

[Block 3453]
མངོན་པར་བྱང་ཆུབ་པ་རྣམ་པ་ལྔ་ཡང་དག་པར་སྟོན་པའི་ཞེས་པ་ལ། འོག་གི་རྩེ་ལྔ་རྣམ་པར་ཤེས་པ་ལྔའི་ངོ་བོ་ཉིད་སྟེང་གི་རྩེ་ལྔ་པོ་ཡེ་ཤེས་ལྔའི་ངོ་བོ་དག་གིས་སྦྱངས་པའི་ཕྱིར་རྡོ་རྗེ་རྣམ་པར་དག་པའོ། །

[Block 3454]
རྒྱུད་ཕྱི་མ་ལས་ཀྱང་།

[Block 3455 [VERSE]]
སྤང་བྱ་ལྔ་དང་རིག་པ་ལྔ། །
རྡོ་རྗེ་ཞེས་པར་བརྗོད་པའོ། །

[Block 3456]
ཞེས་འབྱུང་བས་སོ། །

[Block 3457]
དྲང་བའི་དོན་ནི་རྣམ་པར་དག་པ་དང་བཅས་པའི་ཕྱག་མཚན་ཙམ་བསྟན་པས་སོ། །

[Block 3458]
བདེ་བ་གཉིས་ཀྱི་བདག་ཉིད་ཅན། །ཞེས་པ་ནི་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་གྱི་ངོ་བོ་ཉིད་དོ། །

[Block 3459]
ངེས་པའི་དོན་ནི་འབྲས་བུར་གྱུར་པའི་དེ་ཁོ་ན་ཉིད་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3460]
དེས་ན་ནི་ཡོངས་སུ་དག་པ་དང་ཡོངས་སུ་མ་དག་པའི་མཚན་ཉིད་ལྷའི་རྣལ་འབྱོར་གཉིས་བསྟན་ཏོ། །

[Block 3461]
དེ་ལྟར་དཀྱིལ་འཁོར་པ་གཞན་རྣམས་ལ་ཡང་ཤེས་པར་བྱའོ། །

[Block 3462]
སྔར་བཤད་པའི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པས་རེག་བྱ་རྡོ་རྗེ་མའི་པདྨ་ནས་བྱུང་སྟེ། ཞེ་སྡང་ལ་སྤྱོད་པའི་སེམས་ཅན་གྱི་ཁམས་རྣམ་པར་སྦྱངས་ཏེ། མངོན་པར་དགའ་བའི་འཇིག་རྟེན་གྱི་ཁམས་སུ་བཞག་ནས་སླར་ཡང་གཤེགས་ཏེ། ཕྱོགས་བཅུ་ལ་གཟིགས་པ་སྔོན་དུ་འགྲོ་བ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་སྐུ་དང་གསུང་དང་ཐུགས་རྡོ་རྗེ་ལ་མར་ལ་མར་ཐིམ་པ་བཞིན་དུ་གྱུར་ནས་མི་བསྐྱོད་པ་ཁོ་ན་ཨནྡྲ་ནཱི་ལ་དང་འདྲ་བའི་རྣམ་པ་ཞལ་གསུམ་པ་ཕྱག་དྲུག་པ་ཅུང་ཟད་མཆེ་བ་གཙིགས་པ། པདྨ་དང་ཉི་མའི་སྟེང་དུ་རྡོ་རྗེའི༌[^2228]སྐྱིལ་མོ་ཀྲུང་གིས་བཞུགས་པས་སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་ཅན་སྔོན་པོ་དང་དཀར་པོ་དང་དམར་པོའི་ཞལ་གསུམ་གྱི་ཉེ་བར་མཛེས་པ། རྡོ་རྗེ་དང་འཁོར་ལོ་དང་པདྨ་དང་དྲིལ་བུ་དང་ཡིད་བཞིན་ནོར་བུ་དང་། རལ་གྲི་འཛིན་པ། རྡོ་རྗེ་འཆང་ཆེན་པོའི་ཅོད་པན་ཅན་མདོག་ཁ་དོག་ལྔ་དང་ལྡན་པའི་འོད་ཟེར་གྱི་འཁོར་ལོ་སྤྲོ་བར་གྱུར་ཏོ། །

[Block 3463]
དེ་གསུམ་གྱི་བདག་ཉིད་ཅན་ཞེས་པ་ནི་སེམས་དཔའ་གསུམ་གྱི་བདག་ཉིད་ཅན་ནོ། །

[Block 3464]
བདེན་པ་གཉིས་ཀྱི་བདག་ཉིད་ཅན། །ཞེས་པ་ནི་ཡོངས་སུ་དག་པའི་ལྷའི་རྣལ་འབྱོར་གྱི་སྐབས་སུ་ཟུང་དུ་འཇུག་པའི་བདག་ཉིད་ཡིན་པས་སོ། །

[Block 3465]
གཅིག་ཏུ་གྱུར་པ་དེ་ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་དེའི་བདག་ཉིད་ཀྱིས་སོ། །

[Block 3466]
སྔ་མ་བཞིན་ནོ་ཞེས་ཁ་དོག་གི༌[^2229]ཁྱད་པར་རོ། །

[Block 3467]
རྡོ་རྗེ་འཆང་ཆེན་པོ་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གཅིག་གི་ངོ་བོར་རབ་ཏུ་གནས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 3468]
རྡོ་རྗེ་སེམས་དཔའ་ཆུང་བ་ཞེས་པ་ནི་དང་པོ་སྦྱོར་བའི་ལྷག་མའི༌[^2230]ཏིང་ངེ་འཛིན་གྱི་ལྷག་མར་གྱུར་པ་ཕྱག་རྒྱ་སྦྱར་བ༌[^2231]དང་མི་བསྐྱོད་པའི་དཀྱིལ་འཁོར་གྱི་བདག་པོ་ཉིད་སྟོན་པར་བྱེད་དོ། །

[Block 3469]
སྒྲ་ཇི་བཞིན་ཞེས་པ་ནི་བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པ་དང་དང་པོའི་སྦྱོར་བ་སྟོན་པར་བྱེད་པས་སོ། །

[Block 3470]
དང་པོའི་སྦྱོར་བའི་འོག་ཏུ་ཞེས་པ་ལ་སོགས་པས་དཀྱིལ་འཁོར་རྒྱལ་བ་མཆོག་སྟོན་པར་བྱེད་དེ། སེམས་ཅན་རྨོངས་པ་རྣམས་རྣམ་པར་སྦྱོང་བར་བྱ་བའི་ཕྱིར་ཞེས་པ་ནི་གཏི་མུག་གི་རིགས་ཅན་གདུལ་བྱ་རྣམས་སྦྱང་བར་བྱ་བའི་ཕྱིར་རོ། །
--- END BLOCKS ---
