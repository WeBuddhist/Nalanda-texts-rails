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
[Block 3291]
མི་བརྟན་པས༌[^2155]རྣམ་པར་འགྱུར་བའི་ལྟུང་བྱེད་དོ།། །།

[Block 3292]
ད་འདི་མན་ཆད་ནི་བླ་མར་གྱུར་པ་ལ་བརྙས་ཐབས་བྱེད་པའི་ལྟུང་བྱེད་གསུམ་སྟོན་ཏེ། དེ་རྣམས་ཀྱི་དང་པོ་ནི་དགེ་སློང་མའི་ཚོགས་པ༌[^2156]ལ་བརྙས་ཐབས་བྱེད་པ་ལའོ། །

[Block 3293]
ཚོགས་ཀྱི་སྒྲ་ནི་དགེ་འདུན་འདི་དང་འོག་མ་ལའོ། །

[Block 3294]
དགེ་སློང་མའི་ཚོགས་ཞེས་བྱ་བའི་རྣམ་པར་འབྱེད་པ་ནི་དགེ་སློང་མའི་དགེ་འདུན་ཞེས༌[^2157]གསུངས་པ་ཡིན་ནོ། །

[Block 3295]
གསུམ་མམ་གཉིས་སམ་གཅིག་པོ་རྣམས་ཀྱི་རྗེས་སུ་འབྲངས་པས་ཉེས་བྱས་སུ་རིག་པར་བྱའོ། །

[Block 3296]
བརྙས་ཐབས་བྱེད་པ་ཞེས་བྱ་བའི༌[^2158]མདོ་འདི་རྣམ་པར་འབྱེད་པ་ནི་བརྙས་ཐབས་བྱེད་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྟེ། དེ་བས་ན་འདིར་བརྙས་ཐབས་བྱེད་པ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3297]
རྣམ་པ་སྣ་ཚོགས་དག་གིས་སྨོན་པར་བྱེད་དེ། ཚུལ་འཆོས་པ་དང་། ཁ་གསག་དང་། གཞོགས་སློང་དང་། ཐོབ་ཀྱིས་འཇལ་གྱིས་འཚོ་བར་བྱེད་དོ། །

[Block 3298]
མི་གསལ་བ༌[^2159]རྨོངས་པ་མི་མཁས་པ་ཡིན་ནོ། །

[Block 3299]
ལྟུང་བ་ཡང་མི་ཤེས་ལྟུང་བ་མེད་པ་ཡང་མི་ཤེས་པ་ཡིན་ནོ། །

[Block 3300]
འདི་ལ་བྱིན་པའམ་བྱས་པའམ། བསྙེན་བཀུར་ཀུན་དུ་སྤྱད་པས་ཅི་བྱ། ལོག་པའི་ཆོས་ཀྱིས་ཀུན་ཏུ་དཀྲིས་པ་ཡིན་ནོ་ཞེས་གླེང་གཞི་ལས་གསུངས་པ་ཡིན་ནོ། །

[Block 3301]
དེ་བས་ན་འདི་ལྟ་བུའི་བརྙས་ཐབས་བྱེད་པ་ལ་ཡང་འདིའི་ངོ་བོ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 3302]
གང་ལ་བསླབ་པའི་གཞི་གཉིས་པ་དེ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་སྤྱོ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དགེ་སློང་མའི་ཚོགས་ལ་ཞེས་བྱ་བའི་རྗེས་སྙེག༌[^2160]པའི་ཕྱིར་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས་སྨོས་སོ། །

[Block 3303]
དགེ་སློང་མའི་ཚོགས་ལ་སྤྱོད་པར༌[^2161]བྱེད་པའི་གླེང་གཞི་ནི། འདིར་འཚོ་བའི་ཕྱིར་མགོ་བྲེགས་པ། མུ་གེའི་ཕྱིར་མགོ་བྲེགས་པ། སྡིག་པའི་ལས་ཅན། འཕགས་པ་མ་ཡིན་པ། ཟོལ་པ༌[^2162]མོ། །

[Block 3304]
ཕ་རོལ་སླུ་བ༌[^2163]ཡང་དག་པར་སྡོམ་པ་མ་ཡིན་པ་ཚུལ་ཁྲིམས་འཆལ་པའོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེ་བས་ན་སྤྱོ་བའི་རང་བཞིན་ནི་འདི་རྣམས་ཡིན་ནོ་ཞེས་རྟོགས་པར་བྱའོ། །

[Block 3305]
སྤྱོ་བའི་ཚིག་འདི་རྣམས་ལ་དོན་ཐ་དད་པ་ཉིད་དེ་ལོག་པའི་འཚོ་བའི༌[^2164]ཁོངས་སུ་ཚུལ་ཁྲིམས་འཆལ་བ་བསྡུས་པའི་ཕྱིར་རོ། །

[Block 3306]
དེ་བས་ན་ཐ་དད་པའི་ངེས་པ་ནི་སེམས་ཐ་དད་པའི་དབང་གིས་ཚིག་ལའོ། །

[Block 3307]
དེ་བས་ན་བརྙས་ཐབས་དང་སྤྱོ་བ་དག་ལ་དོན་ཐ་དད་པ་ཞེས་བྱ་བར་རྟོགས་པར་བྱའོ། །

[Block 3308]
གང་ལ་བསླབ་པའི་གཞི་གསུམ་པ་དེ་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་འཁོར་གཙོ་བོ་ལ་ཆུས་འཐོར་བ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འཁོར་གཙོ་བོ་ཞེས་བྱ་བའི་སྒྲས་ནི། འདིར་དགེ་སློང་ལ་བརྗོད་དོ། །

[Block 3309]
འཁོར་གཙོ་བོ་ཞེས་བྱ་བ་རྣམ་པར་འབྱེད་པ་ལས་དགེ་སློང་ཞེས་གསུངས་པའི་ཕྱིར་རོ། །

[Block 3310]
ལུས་ལ་ཐིགས་པ་ཙམ་གྱིས་ཕོག་པར་གྱུར༌[^2165]ན་ཡང་དེའི་ཚེ་ཆུས་གཏོར་བ་ཡིན་ནོ། །

[Block 3311]
བརྒྱལ་བ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་བརྒྱལ་བ་ལ་ཆུ་གཏོར་བ་ལ་ལྟུང་བ་མེད་དོ། །

[Block 3312]
ཁ་ན་མ་ཐོ་བ་འདི་ནི་ལོག་པར་བསྒྲུབ་པར་གྱུར་པའི་གཏོང་བ་ལ་ཞེས་བསྟན་པར་རིག་པར༌[^2166]བྱའོ། །

[Block 3313]
དགེ་སློང་ལ་ཐུ་ཞེས་མི་བྱའོ་ཞེས་བྱ་བ་ནི། འདིར་གཞུང་ནི། ཕྲན་ཚེགས་རྣམས་ལས་ཐུ༌[^2167]ཞེས་མི་བྱའོ་ཞེས་བྱ་བའི་དང་པོ་འདི་ནས་བསྟན་པ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་པ་ཡིན་ནོ། །

[Block 3314]
རབ་ཏུ་བྱུང་བ་འདི་པ་ལ་སྤྱོ་བར་མི་བྱའོ་ཞེས༌[^2168]བྱ་བ་ནི་དགེ་སློང་མའི་ཚོགས་ལ་སྤྱོ་བའི་ལྟུང་བྱེད་སྔར་ལོགས་ཤིག་ཏུ་བསྟན་ཟིན་པའི་ཕྱིར་རོ། །

[Block 3315]
ཆོས་འདི་པའི་རབ་ཏུ་བྱུང་བ་དགེ་སློང་ལ་སོགས་པ་ལ་ཆོས་འདི་པ་རབ་ཏུ་བྱུང་བའི་ཚིག་གིས་བསྡུས་ཏེ། འདི་ལ་སྤྱོ་བ་ལ་ཉེས་བྱས་སུ་རྣམ་པར་གཞག་པ་ཡིན་ཏེ། ལྕི་བའི་ཆོས་མ་ཡིན་པའི་ཕྱིར་མགུ་བར༌[^2169]སྤྱད་པ་ཡིན་ནོ། །

[Block 3316]
མགུ་བར་སྤྱད་པ་ཞེས་སྨོས་པས་ཟླ་བ་ཕྱེད་སྤྱད་པར་བྱའོ། །

[Block 3317]
དེ་ལ་གཉིས་ཀ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གང་ཞིག་རབ་ཏུ་བྱུང་བ་འདི་པ་དེ་ལ་སྤྱོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་པ་དེ་ལ་བརྙས་ཐབས་དང་སྤྱོ་བ་གཉིས་ཀ་ལ་ཡང༌[^2170]རིག་པར་བྱའོ། །

[Block 3318]
རབ་ཏུ་བྱུང་བ་འདི་པ་ལ་བརྙས་ཐབས་མི་བྱའོ་ཞེས་བྱ་བ་འདི་ཡང་འདིས་འཕངས་སོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3319]
དགེ་སློང་གི་མདུན་དུ་སྤྱོད་ཡུལ་དུ་རྒྱུ་བར་མི་བྱའོ། །

[Block 3320]
ཟམ་པ་མི་བརྟན་པར་དགེ་སློང་དང་ལྷན་ཅིག་འགྲོ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ཟམ་པ་བརྟན་པ༌[^2171]དང་མི་ལྡོག༌[^2172]པས་ལྟུང་བའི་བདག་ཉིད་ཅན་གྱི་ཉེས་དམིགས་མི་སྲིད་པས་ན་ལྟུང་བ་མེད་དོ། །

[Block 3321]
དགེ་སློང་མཐོང་མ་ཐག་ཏུ་སྟན་ལས་ལྡང་བར་བྱའོ། །

[Block 3322]
འདུག་པས་དེ་འགྲེང་བས༌[^2173]ཧ་ཅང་ཡུན་རིང་དུ་འདའ་བར་བྱེད་ན་སྟན་ལ་འདུག་ཏུ་གཞུག་གོ་ཞེས་བྱ་བ་ལ། འདུག་པས་ཞེས་བྱ་བ་ནི་སྟན་ལ་འདུག་ཏུ་གཞུག་གོ་ཞེས་བྱ་བ་དང་འབྲེལ་ལོ། །

[Block 3323]
དེ་ཞེས་བྱ་བ་ནི་དགེ་སློང་མའོ། །

[Block 3324]
གནས་སྐབས་གང་དུ་འཇུག་པར་འགྱུར༌[^2174]ཞེ་ན། དེའི་ཕྱིར་འགྲེང་བ་ཞེས་སྨོས་ཏེ། གནས་པས་ཞེས་བྱ་བའི་སྤྱོད་ལམ་གྱིས་དུས་འདའ་བར་བྱེད་པ་ལའོ། །

[Block 3325]
གནས་སྐབས་ཇི་ལྟ་བུས་དེ་སྟན་ལ་འདུག་ཏུ་གཞུག་ཅེ་ན། དེའི་ཕྱིར་འདུག་པས་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3326]
དགེ་སློང་ཞེས་བྱ་བ་འདི་ལ་འདིར་དགེ་སློང་རྣམས་ཀྱིས་ཞེས་བྱ་བ་ཡོངས་སུ་གྱུར་པ་ལ་བྱེད་པ་པོ་ཉིད་ཀྱི་ཚིག་གིས་འབྲེལ་ཏོ་སྙམ་དུ་ཤུགས་ཀྱིས་རྟོགས་པའོ། །

[Block 3327]
མི་བྱེད་ན་འདུག་པའི་ཕྱིར་ཞུས་ཏེ་དེ་ལ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། མི་བྱེད་ན་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་སྟན་ལ་འདུག་པར་མ་བྱས་པ་ལ། འདི་ལ་དེས་འདུག་པ་ལ་ངེས་པར་སྦྱར་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3328]
མཐོང་མ་ཐག་ཏུ་ཞེས་བྱ་བ་ནི་དགེ་སློང་དེའོ། །

[Block 3329]
དེ་ལ་འདུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་གིས་སོ། །

[Block 3330]
ཞུས་ཏེ་ཞེས་བྱ་བ་ནི་གནང་ན་སྟན་དེ་ལ་འདུག་པར་བྱ་སྟེ། དགེ་སློང་མས་ཞེས་བྱ་བའི་དོན་གྱིས་རྟོགས་པར་བྱའོ། །
--- END BLOCKS ---
