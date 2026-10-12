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
[Block 3151]
དེས་ན་དོན་འདི་ཡིན་ཏེ། རྡོ་རྗེ་གསུམ་ནི་སྐུ་ལ་སོགས་པའོ། །

[Block 3152]
དེ་རྣམས་ཀྱི་དམ་ཚིག་ནི་དབྱེར་མེད་པར་ཡོངས་སུ་ཤེས་པའོ། །

[Block 3153]
དེས་མཆོག་ཅེས་པ་ནི་ཟུང་དུ་འཇུག་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པ་བཅོམ་ལྡན་འདས་ཀྱི་ཁྱད་པར་རོ། །

[Block 3154]
ཡེ་ཤེས་དེ་བཞིན་གཤེགས་པ་ཀུན། །ཞེས་པ་ནི་རྡོ་རྗེ་གསུམ་ནི་བཙུན་མོའི་བྷ་གའི་ཁྱད་པར་རོ། །

[Block 3155]
དེ་བཞིན་གཤེགས་པ་ཀུན་ནི་ཕུང་པོ་ལྔའི་ཡེ་ཤེས་ཏེ། རོ་གཅིག་པ་ཉིད་དུ་རྟོགས་པ་ནི་འོད་གསལ་བའོ། །

[Block 3156]
ཡོན་ཏན་ཕུན་ཚོགས་བསམ་མི་ཁྱབ། །ཅེས་པ་ནི་བྱང་ཆུབ་ཀྱི་ཕྱོགས་ལ་སོགས་པ་སངས་རྒྱས་ཀྱི་ཡོན་ཏན་གྱི་ཚོགས་བསམ་གྱིས་མི་ཁྱབ་པ་གང་ལ་ཡོད་པ་དེ་ལ་འདི་སྐད་ཅེས་བྱའོ། །

[Block 3157]
དེས་ནི་ཆོས་ཀྱི་སྐུའི་ངོ་བོ་རྟག་ཏུ་དགའ་བའི་རང་བཞིན་ཅན་རིམ་པ་བཞི་པ་ངེས་པར་བསྟན་ཏོ། །

[Block 3158]
ཆད་པར་ལྟ་བ་སྤང་བར་བྱ་བའི་ཕྱིར་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ལ་མངོན་དུ་བྱེད་པའི་མཚན་ཉིད་བསྒོམ་པར་བྱ་བ་ཡིན་པས་དེ་བསྟན་པར་བྱ་བའི་ཕྱིར། ཡོད་མེད་ཅེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ལ། ཡོད་པ་དང་མེད་པ་དང་གཉི་ག་སྤངས་པ་དང་། གནས་དང་གནས་མ་ཡིན་པ་གཉི་ག་བྲལ་བ་སྟེ་ཟུང་དུ་འཇུག་པའི་ཏིང་ངེ་འཛིན་ཏོ། །

[Block 3159]
ནམ་མཁའ་གཅིག་པུའི་ངོ་བོ་འདིར། །ཞེས་པ་ནི་སྒྲིབ་པ་མེད་པའི་ཡེ་ཤེས་ཀྱི་དབྱིངས་ཀྱི་ངོ་བོར་རོ། །

[Block 3160]
ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་བསྒོམ།[^2050] །ཞེས་པ་ནི་རྟག་ཏུ་འཆར༌[^2051]ཞིང་དྲི་མ་མེད་པའི་འགྲོ་བ་གསུམ་པོ་སྐད་ཅིག་མ་གཅིག་གིས་ཡོངས་སུ་ཤེས་པའོ། །

[Block 3161]
འགྲོ་སྙིང་ཞེས་པ་ནི་གཡོ་བ་དང་མི་གཡོ་བའི་ངོ་བོ་ཉིད་ཁམས་གསུམ་གྱི་རྒྱུ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་དེ་ཁོ་ན་ཉིད་ཅེས་འོད་གསལ་བའི་ཁྱད་པར་རོ། །

[Block 3162]
རྣམ་དག་ཅེས་པ་ནི་བདེན་པ་གཉིས་ཀྱི་རྣམ་པར་རྟོག་པའི་དྲི་མ་དག་པར་བྱེད་པ་ཞེས་ཟུང་དུ་འཇུག་པའི་རིམ་པའི་ཁྱད་པར་རོ། །

[Block 3163]
ཐུབ་པ་ཆེན་པོ་ནི་བཅོམ་ལྡན་འདས་རྡོ་རྗེ་འཆང་ཆེན་པོ་བཞུགས་སོ་ཞེས་པ་ནི་མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ཀྱི་ཏིང་ངེ་འཛིན་ལ་བཞུགས་སོ། །

[Block 3164]
མཐར་ཐུག་པ་ཞེས་པ་ནི་རིམ་པ་ཐ་མ་སོ་སོར་སྟོན་པར་བྱེད་པ་ཡིན་ཏེ། དེ་ལས་གཞན་ལ་མི་སློབ་པའི་ཕྱིར་རོ། །

[Block 3165]
སློབ་མ་ལ་བཤད་པའོ་ཞེས་པ་ནི་རིན་པོ་ཆེ་ལྟ་བུའི་གང་ཟག་སྣོད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3166]
དེ་ཡང་སྔར་བཤད་ཟིན་ཏོ། །

[Block 3167]
བསྡུས་པའི་དོན་འདི་ཡིན་ཏེ། ཡི་གེའི་དོན་དང་སྤྱིའི་དོན་དག་གིས་བསྐྱེད་པའི་རིམ་པ་དང་སྦས་པ་དང་མཐར་ཐུག་པའི་རིམ་པ་དག་གིས་རིམ་པ་ལྔ་ཞེས་བྱ་བ༌[^2052]རྫོགས་པའི་རིམ་པ་བསྟན་ཏོ། །

[Block 3168]
དེ་བས་ན་བཞུགས་པའི་ཚིག་ཉིད་ཀྱིས་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། བཞུགས་པའི་ཕྱོགས་གཅིག་དང་ལྡན་པའི་ཚིག་ནི་བཞུགས་པའི་ཚིག་གོ། །

[Block 3169]
བར་གྱི་སྒྲའི་དབྱེ་བར་བྱས་པའི་ལས་འཛིན་པའོ། །

[Block 3170]
རྒྱུད་མ་ལས་པའི༌[^2053]དགོངས་པ། ཞེས་པ་ནི་ལེའུ་བཅོ་བརྒྱད་ཀྱི་བདག་ཉིད་ཀྱི་རྒྱུད་ཀྱི་དོན་རིམ་པ་གཉིས་མ་གཏོགས་པར་གཞན་མི་དམིགས་པའི་ཕྱིར་རོ། །

[Block 3171]
ཡོད་ན་ཡང་དེ་ཉིད་དུ་འདུས་པའོ། །

[Block 3172]
འཁོར་ཕུན་སུམ་ཚོགས་པ་བསྟན་པར་བྱ་བའི་ཕྱིར། བརྗོད་ཀྱིས་མི་ལང་བའི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་ཏེ། འཁོར་ཕུན་སུམ་ཚོགས་པ་ནི་ཉན་པ་པོ་ཕུན་སུམ་ཚོགས་པའོ། །

[Block 3173]
སྟོན་ཏེ་ཞེས་པ་ནི་སྡུད་པ་པོས་ཞེས༌[^2054]ཚིག༌[^2055]ལྷག་མ་སྟེ་འཆད་པ་པོ་དང་གནས་ཕུན་སུམ་ཚོགས་པ་དག་ནི་གླེང་གཞིའི་ཚིག་ཉིད་དུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3174]
བརྗོད་ཀྱིས་མི་ལང་བ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་མང་བ་ཙམ་དུ་དགོངས་པའི་ཕྱིར་རོ། །

[Block 3175]
ཡང་བརྗོད་ཀྱིས་མི་ལང་བ༌[^2056]ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་དེ་ལ་གཟུགས་ནི་མི་ངོམས་པའོ། །

[Block 3176]
ཡོན་ཏན་ནི་སྦྱིན་པ་ལ་སོགས་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་མཚན་ཉིད་དོ། །

[Block 3177]
དེ་ཡང་ངག་གི་སྤྱོད་ཡུལ་ལས་འདས་པའོ། །

[Block 3178]
དེ་དག་ཅེས་པ་ནི་གྲངས་དང་གཟུགས་ལ་སོགས་པའི་ཡོན་ཏན་དཔག་ཏུ་མེད་པའི་ཕྱིར་རོ། །

[Block 3179]
སངས་རྒྱས་ཀྱི་ཞིང་གི༌[^2057]ཞེས་བྱ་བ་ལ་སོགས་པས་དཔེ་བསྟན་ཏོ། །

[Block 3180]
གང་གིས་ཞེས་བྱ་བ་ལ་སོགས་པས༌[^2058]དཀྱིལ་འཁོར་པ༌[^2059]སྨོས་ཏེ། དེ་ཙམ་རྒྱུད་འདི་རུ་བསྒོམ་པར་བྱ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3181]
འདི་ལྟ་སྟེ་ཞེས་བྱ་བ་ལ་སོགས་པས་དེ་དག་ཁོ་ན་གསུངས་སོ། །

[Block 3182]
དམ་ཚིག་རྡོ་རྗེ་ནི་དོན་ཡོད་པར་གྲུབ་པ་ཞེས་པ་ལ། དམ་ཚིག་གི་རིགས་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3183]
ཇི་སྐད་དུ།

[Block 3184 [VERSE]]
ཞེ་སྡང་གཏི་མུག་འདོད་ཆགས་དང་། །
ཡིད་བཞིན་ནོར་བུ་དམ་ཚིག་ནི། །
འདི་དག་རིགས་ནི་ལྔ་པོ་སྟེ། །
འདོད་དང་ཐར་པ་རབ་བསྒྲུབ༌[^2060]པའོ། །

[Block 3185]
ཞེས་འབྱུང་ངོ་། །འདིར་ཡང་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་རིགས་དང་རིགས་ཅན་རྣམས་ལ་བྱེ་བྲག་མེད་པའི་ཕྱིར་རོ། །

[Block 3186]
བྱང་ཆུབ་སེམས་དཔའི་སྒྲ་ནི་ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ་དང་སྤྲུལ་པའི་སྐུ་དབྱེར་མེད་པའི་ཕྱིར་རོ། །

[Block 3187]
དབྱེར་མེད་པ་ཡང་བྱ་བ་གཅིག་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3188]
དེ་ལྟར་སྐུ་རྡོ་རྗེ་ལ་སོགས་པ་སྔ་མ་བཞིན་ནོ། །

[Block 3189]
ཏིང་ངེ་འཛིན་རྡོ་རྗེ་ནི་ནམ་མཁའི་སྙིང་པོ་ཞེས་པ་ལ། རིན་ཆེན་འབྱུང་ལྡན་གྱི་རིགས་ནམ་མཁའ་མཛོད་ཀྱི་ཏིང་ངེ་འཛིན་གཙོ་བོར༌[^2061]གྱུར་པའི་ཕྱིར་རོ། །

[Block 3190]
རྒྱལ་བ་རྡོ་རྗེ་ནི་བྱམས་པ་ཞེས་པ་ལ། །མ་འོངས་པའི་དུས་སུ་ཆོས་ཀྱི་རྒྱལ་སྲིད་ལ་མངའ་མཛད་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
