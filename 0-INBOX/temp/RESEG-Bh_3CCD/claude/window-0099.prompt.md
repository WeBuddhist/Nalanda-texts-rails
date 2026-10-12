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

[Block 3471]
ཞི་བའི་ཚུལ་ནི་ཞི་བའི་ལས་ཀྱི་རབ་འབྱམས་ཀྱི་ངོ་བོ་ཉིད་རྣམ་པར་སྣང་མཛད་ཡིན་ཞེས་མཚོན་པར་བྱེད་དོ། །

[Block 3472]
རྒྱལ་བའི་ངང་ཚུལ་ཅན་ཞེས་པ་ནི་སོ་སོའི་སྐྱེ་བོའི་ས་ལ་གནས་པའི་སེམས་ཅན་རྣམས་ལས་རྒྱལ་བ་སྟེ་བདུད་དོ། །

[Block 3473]
བདུད་ནི་ལྷའི་བུ་ལ་སོགས་པའི་བདུད་རྣམས་སོ། །

[Block 3474]
དེ་དག་ལས་རྩིབས་བཅུ་གཉིས་པའི་ཆོས་ཀྱི་འཁོར་ལོས་རྒྱལ་བས་ནི་ཛི༌[^2232]ན་ཛིཀ༌[^2233]གོ། །

[Block 3475]
སྡུག་བསྔལ་དང་། ཀུན་འབྱུང་བ་དང་། འགོག་པ་དང་། ལམ་སྟེ་བདེན་པ་བཞིའོ། །

[Block 3476]
སྡུག་བསྔལ་ནི་ཤེས་པར་བྱ་བ་དང་། ཀུན་འབྱུང་སྤང་བར་བྱ་བ་དང་། ལམ་བསྒོམ་པར་བྱ་བ་དང་། འགོག་པ་མངོན་དུ་བྱའོ།[^2234] །

[Block 3477]
སྡུག་བསྔལ་ཤེས་ཟིན་པ་དང་། ཀུན་འབྱུང་སྤོང་བ་དང་། ལམ་བསྒོམ་པ་དང་། འགོག་པ་མངོན་དུ་བྱས་སོ་ཞེས་མཐོང་བ་དང་བསྒོམ་པ་དང་མི་སློབ་པའི་ལམ་གྱིས་རྩིབས་བཅུ་གཉིས་པའོ། །

[Block 3478]
རྟེན་འབྲེལ་ཡན་ལག་བཅུ་གཉིས་པའི་མཚན་ཉིད་ཆོས་ཀྱི་འཁོར་ལོ་ཡིན་ཞེས་ལ༌[^2235]ལ་འདོད་དོ། །

[Block 3479]
དྲང་བའི་དོན་ནི་ཉན་ཐོས་དང་ཐེག་པ་ཆེན་པོའི་ལྟ་བ་ཙམ་བསྟན་པས༌[^2236]སོ། །

[Block 3480]
རྡོ་རྗེ་ལྟ་བུའི་ཏིང་ངེ་འཛིན་གྱིས་ཞེས་པ་ནི་ཀུན་དུ་འོད་ཀྱི་སའི་སྐད་ཅིག་མ་དང་པོས་ཐོབ་པར་བྱ་བའི་ཏིང་ངེ་འཛིན་གྱི་ཁྱད་པར་གྱིས་སོ། །

[Block 3481]
ངེས་པའི་དོན་གྱི་བཞི་པ་དང་ལྔ་པའི་རིམ་པ་དག་སོ་སོར་བསྟན་པའི༌[^2237]ཕྱིར་རོ། །

[Block 3482]
རྣམ་པར་སྣང་མཛད་ཅེས་བྱ་བ་ལ་སོགས་པས་ཛི་ན་ཛིཀ་ཅེས་སྤྲོ་བའི་རྗེས་སུ་ཆོས་འབྱུང་བའི་ཕྱག་རྒྱ་ནས་ཕྱི་རོལ་དུ་བྱུང་སྟེ། གཏི་མུག་ལ་སྤྱོད་པའི་སེམས་ཅན་གྱི་ཁམས་སྦྱངས་ནས་འོག་མིན་གྱི་གནས་སུ་བཞག་ནས་སླར་ཡང་གཤེགས་ཏེ། ཕྱོགས་བཅུར་གཟིགས་པ་སྔོན་དུ་འགྲོ་བས༌[^2238]བཅོམ་ལྡན་འདས་ཀྱིས་ཤར་ཕྱོགས་སུ༌[^2239]སྣ་ཚོགས་པདྨ་དང་ཟླ་བའི་གདན་ལ་འཁོར་ལོའི་སྟེང་དུ་རྡོ་རྗེ་དཀྱིལ་མོ་ཀྲུང་དུ་བཞུགས༌[^2240]པ། འཁོར་ལོ་ལ་སོགས་པ་ཕྱག་མཚན་དྲུག་འཛིན་པ་སྐུ་མདོག་དཀར་པོ་རྣམ་པར་སྣང་མཛད་བཞུགས་སོ་ཞེས་བསྟན་ཏོ། །

[Block 3483]
སྒྲ་ཇི་བཞིན་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 3484]
ཀུན་རྫོབ་བྱང་ཆུབ་ཀྱི་སེམས་ཞེས་པ་ནི་བདེ་བ་ཆེན་པོའི་རྒྱུ་མཐུན་པས་རིན་ཐང་མེད་པའི་ཕྱིར་རོ། །

[Block 3485]
དེ་ལས་བྱུང་བ་ཞེས་པ་ནི་དམ་ཚིག་གི་དཀྱིལ་འཁོར་གྱི་ནང་དུ་སྤྲོས་པའི་ཕྱིར་རོ། །

[Block 3486]
ཏིང་ངེ་འཛིན་ཡང་དེ་བཞིན་དུ་ཤེས་པར་བྱའོ། །

[Block 3487]
དྲང་བའི་དོན་ནི་བསྐྱེད་པའི་རིམ་པ་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3488]
དོན་དམ་པའི་བྱང་ཆུབ་ཀྱི་སེམས་ཏེ་ཞེས་པ་ནི། འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 3489]
དེ་ལས་བྱུང་བས་ན་ཞེས་པ་ནི་བདག་བྱིན་གྱིས་རློབ་པ་དང་ཟུང་དུ་འཇུག་པའི་རིམ་པ་དག་བརྗོད་པར་འདོད་པའི་ཕྱིར་རོ། །

[Block 3490]
ངེས་པའི་དོན་ནི༌[^2241]རྫོགས་པའི་རིམ་པ་སོ་སོར་བསྟན་པས་སོ། །

[Block 3491]
བསམ་པ་ཐམས་ཅད་ཡོངས་སུ་ཞེས་བྱ་བ་ལ་སོགས་པས་རིན་ཆེན་འབྱུང་ལྡན་གྱི༌[^2242]དོན་དང་ལྡན་པའི་མཚན༌[^2243]སོ་སོར་བསྟན་ཏོ། །

[Block 3492]
རེ་བ་ཐམས་ཅད་ཡོངས་སུ་རྫོགས་པར་བྱེད་པས་ན་ཞེས་པ་ནི་ནམ་མཁའ་མཛོད་ཀྱི་ཏིང་ངེ་འཛིན་གྱིས་སེམས་ཅན་རྣམས་ལ་དབུལ་བ་ཉིད་བཅོམ་པའི་ཕྱིར་རོ། །

[Block 3493]
དྲང་བའི་དོན་ནི་ལས་ཀྱི་རྒྱལ་བ་མཆོག་བརྗོད་པར་མཛད་པར་འདོད་པས་སོ། །

[Block 3494]
ཡང་དག་པའི་མཐའི༌[^2244]རིན་པོ་ཆེ་ཞེས་པ་ནི་རིམ་པ་བཞི་པས་ཐོབ་པར་བྱ་བའི་འོད་གསལ་བའི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 3495]
ངེས་པའི་དོན་ནི་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ། རྗོད་པར་བྱེད་པས་སོ། །

[Block 3496]
ནམ་མཁའ་ལྟར་གོས་པ་མེད་པའི་མཉམ་པ་ཉིད་ཀྱི་ཡེ་ཤེས་ཞེས་པ་ནི་སྐྱེ་བ་བཞིས་བསྡུས་པའི་སེམས་ཅན་ཐམས་ཅད་ཐ་དད་པ་རྣམས་གཅིག་ཏུ་ཡོངས་སུ་ཤེས་པའི་ཕྱིར་རོ། །

[Block 3497]
ནོར་གྱིས་དྲེགས་ཤིང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ནོར་མང་བའི་ཕྱིར་ང་རྒྱལ་གང་ལ་ཡོད་པ་དེ་རྣམས་ལ་ནམ་མཁའ་མཛོད་ཀྱི་ཏིང་ངེ་འཛིན་ལས་རིན་པོ་ཆེ་ལ་སོགས་པའི་ཆར་འབེབས་པའི་སྒོ་ནས་དྲེགས་པ་བཅག་པའི་ཕྱིར་རོ། །

[Block 3498]
བཅོམ་ལྡན་འདས་ཀྱི༌[^2245]གཡས་ཕྱོགས་སུ་བཞུགས་ཞེས་པ་ནི་སྔ་མ་བཞིན་དུ་རྡོ་རྗེ་དང་པདྨའི་ཏིང་ངེ་འཛིན་ལས་ཕྱུང་སྟེ། དེ་ནས་ཡང་ཕྱི་རོལ་དུ་གཤེགས་ཏེ། ང་རྒྱལ་ཅན་གྱི་སེམས་ཅན་གྱི་ཁམས་སྦྱངས་ཏེ་རིན་པོ་ཆེའི་འབྱུང་གནས་ཞེས་བྱ་བའི་སངས་རྒྱས་ཀྱི་ཞིང་ལ་རབ་ཏུ་གནས་པར་བྱས་ནས་སླར་ཡང་གཤེགས་ཏེ། ཞལ་གསུམ་པ་ཕྱག་དྲུག་པ་རིན་པོ་ཆེ་ལ་སོགས་པའི་ཕྱག་མཚན་འཛིན་པ་སྐུ་མདོག་སེར་པོ་བཅོམ་ལྡན་འདས་ཀྱི་གཡས་ཕྱོགས་སུ་སྣ་ཚོགས་པདྨ་དང་ཟླ་བ་དང་རིན་པོ་ཆེའི་གདན་ལ་བཞུགས་ནས་སོ། །

[Block 3499]
སྒྲ་ཇི་བཞིན་པ་ནི་སྔ་མ་བཞིན་ནོ། །

[Block 3500]
འདོད་ཆགས་ཀྱི་འདོད་ཆགས་རབ་ཏུ་སྤང་བའི་དོན་དུ་ཞེས་པ་ནི་འདོད་ཆགས་ནི་དེ་ཁོ་ན་ཉིད་ལ་ཆགས་པའོ། །

[Block 3501]
ཡང་འདོད་ཆགས་ནི་ཉོན་མོངས་པ་ཉིད་དོ། །

[Block 3502]
དོན་དེས་སྤོང་བ་སྟེ་གསལ་བའོ། །

[Block 3503]
མཆོག་ཏུ་དགའ་བ་ནི་འདོད་ཆགས་ཆེན་པོ་འོད་གསལ་བ་ཆེན་པོའི་རྒྱུ༌[^2246]མཐུན་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3504]
བྱང་ཆུབ་ཀྱི་སེམས་ཡིན་ལ་ཞེས་པ་ནི་ཀུན་རྫོབ་པའི་རྫས༌[^2247]ཀྱི་ཚུལ་ཅན་ཤུ་ཀྲའོ། །

[Block 3505]
དེ་ལས་བྱུང་བ་ནི་དམ་ཚིག་གི་དཀྱིལ་འཁོར་གྱི་རིམ་པས་རྫོགས་ཞེས་པའི་བར་དུའོ། །
--- END BLOCKS ---
