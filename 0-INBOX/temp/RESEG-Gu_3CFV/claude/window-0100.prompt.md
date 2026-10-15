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
[Block 3501]
འདིར་རྣམ་པ་གང་གིས་དེ་རྣམས་ནི་སོགས་པའི་སྒྲས་འཕངས་པའོ། །

[Block 3502]
དེ་བསྟན་པའི་དོན་དུ་འདིར་རྟགས་ལ་སོགས་པའི་གཞི་བརྗོད་པའོ། །

[Block 3503]
འདིར་གཞིའི་སྒྲ་ནི་རེ་རེ་ཞིང་སྦྱར་བར་བྱའོ། །

[Block 3504]
རྟགས་ཀྱི་གཞི་ལས་བྱུང་བ་དང་། སློང་བའི་གཞི་ལས་བྱུང་བ་དང་། སྣོད་ཀྱི་གཞི་ལས་བྱུང་བ་དང་། འཕྱར་གཡེངས་ཀྱི་གཞི་ལས་བྱུང་བ་དང་། འདོད་པའི་གཞི་ལས་བྱུང་བ་དང་། གནོད་པའི་གཞི་ལས་བྱུང་བ་དང་། མི་གུས་པའི་གཞི་ལས་བྱུང་བ་དང་། མི་སྦྱང་བའི༌[^2281]གཞི་ལས་བྱུང་བའོ། །

[Block 3505]
དེ་ལ་རབ་ཏུ་བྱུང་བའི་རྟགས་ཡང་དག་པར་ལེན་ཏོ་ཞེས་སྨོས་པའི་ཚིག་གང་ཡིན་པ་དེ་ནི་རེ་ཞིག་བླངས་པ་ཡིན་པ་དང་། [^2282]དེའི་ཕྱིར་མུ་སྟེགས་ཅན་གྱི་རྟགས་འཆང་བ་ལ་ནི་ཇི་ལྟར་ཁྱིམ་པའི་རྟགས་འཆང་བ་བཞིན་དུ་རབ་ཏུ་བྱུང་བའི་རྟགས་ཡང་དག་པར་བླངས་པ་ལས་འདས་པ་ཡིན་པས་དེ་ལ་ནི་བཤགས་པར་བྱ་བའི་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 3506]
རྫས་རུང་བ་མ་ཡིན་པ་ཆོས་གོས་ཚད་ལས་ཆུང་བ་དང་ཆེ་བའི་བདག་ཉིད་ཀྱི་ཡོ་བྱད་རྣམས་ལ་འཆང་བ་དང་འཆང་བར་བྱེད་དུ་བཅུག་པའམ།[^2283] སེན་མོ་བཅོས་པ་རྗེས་སུ་མ་གནང་བ་དག་དང་། ཆ་ལུགས་ཉམས་པར་གྱུར་པ་སྐྲ་ཆན་པས་བྲེགས༌[^2284]པར་གྱུར་པ་དག་དང་། རྗེས་སུ་མ་གནང་བའི་ཕྱོགས་ཀྱི་སྤུ་བྲེགས་པ༌[^2285]ལ་སོགས་པ་རྣམས་ནི་རྟགས་བླངས་པ་དེའི་ཕྱོགས་དང་མཐུན་པའི་ཚིག་གོ། །

[Block 3507]
ལྷུང་བཟེད་རུང་བ་མ་ཡིན་པ་ཐོགས་ཤིང་བསོད་སྙོམས་ལ་རྒྱུ་བ་ནི། རྟགས་སུ་གྱུར་པ་ཡིན་པ་དེ་ཡང་རབ་ཏུ་བྱུང་བ་གཞན་གྱི་རྟགས་སུ་གྱུར་པ་དང་། ཁྱིམ་པའི་རྟགས་དང་འདྲ་བའི་ལྷུང་བཟེད་འཆང་བ་ཡང་རྟགས་ཡང་དག་པར་བླངས་པ་ལས་འདས་པར་རིག་པར་བྱའོ། །

[Block 3508]
རྫས་གཞན་ལས་བྱས་པ་དང་། ཚད་ལས་ཆུང་བ་དང་ཆེ་བ་དང་སྐྱ་བ་འཆང༌[^2286]བ་གང་ཡིན་པ་དེ་ནི་རྟགས་བླངས་པ་དེའི་ཕྱོགས་དང་མཐུན་པའོ། །

[Block 3509]
སློང་བའི་སྣོད་ཀྱི་གཞི་ལས་འབྱུང་བ་གང་ཡིན་པ་དེ་རྣམས་ནི་ས་ལེ་སྦྲམ་དང་དངུལ་ལ་སོགས་པ་ནི་མ་བྱིན་པ་ལེན་གྱི་ཕྱོགས་དང་མཐུན་པ་རྣམས་སོ། །

[Block 3510]
སློང་བའི་གཞི་ལས་བྱུང་བ་ནི་ཆོས་གོས་ལ་སོགས་པ་སློང་བའོ། །

[Block 3511]
སྣོད་ཀྱི་གཞི་ལས་བྱུང་བ༌[^2287]གང་ཡིན་པ་དེ་རྣམས་ནི་ཁབ་རལ་ལ་སོགས་པ་བྱེད་དུ་བཅུག་པའོ། །

[Block 3512]
ལོངས་སྤྱོད་ཀྱི་གཞི་ལས་བྱུང་བ༌[^2288]གང་ཡིན་པ་དེ་རྣམས་ནི་བཙོང་ཟ་བ་ལ་སོགས་པ་དུས་མ་ཡིན་པར་ཟ་བའི་ཕྱོགས་ཉིད་དོ། །

[Block 3513]
འཕྱར་གཡེང་གི་གཞི་ལས་བྱུང་བ་རྣམས་ནི། རྒྱུག་པ་དང་། མཆོང་བ་དང་། ཆུ་ལ་རྩེ་བ༌[^2289]ལ་སོགས་པ་རྣམས་ལ་གླུ་གར་དང་། རོལ་མོའི་སྒྲ་དང་། མེ་ཏོག་ཕྲེང་བ་དང་། དྲིས་བྱུག་པ་དང་། ཁ་དོག་འཆང་བ་དང་། མལ་སྟན་མཐོན་པོ་དང་། མལ་སྟན༌[^2290]ཆེན་པོའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་དོ། །

[Block 3514]
གང་ཞིག་འདི་ནི་ཁྱིམ་བྱེད་དུ་བཅུག་པའི་ཁ་ན་མ་ཐོ་བ་སྟེ། ཁང་པ་དང་ཁང་ཆེན་རྩིག་པར་གཏོགས་པར་འདོད་པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་དོ། །

[Block 3515]
ཁྱིམ་གྱི་འདོད་པའི་ཕྱོགས་ནི་དེའི་ཕྱིར་དེ་ལ་འདོད་པའི་དངོས་པོ་ཉིད་ལ་ཞུགས་པར་གྱུར་པ་ཉིད་ཀྱིས་འདི་ལ་རབ་ཏུ་བྱུང་བ་ཡང་དག་པར་བླངས་པའི་ཉམས་པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་དོ། །

[Block 3516]
ཁུ་བ་འབྱིན་པ་དང་། བཟང་བ་དང་འཁྲིག་པ་ཀུན་ཏུ་སྤྱོད་པ་རྣམས་ནི་འདོད་པའི་དངོས་པོ་ཉིད་དོ། །

[Block 3517]
གནོད་པའི༌[^2291]གཞི་ཉིད་ནི་མི་ཚངས་པར་སྤྱོད་པའི་ཕྱོགས་ཉིད་དོ། །

[Block 3518]
ཐལ་ལྕག་བརྡེགས་པ༌[^2292]དང་མཆིལ་ལྷམ་སྦ་བ་ལ་སོགས་པ་རྣམས་ནི་སྲོག་གཅོད་པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་དོ། །

[Block 3519]
ཁྲོ་བ་ལ་སོགས་པ་རྣམས་ལ་བརྫུན༌[^2293]དུ་སྨྲ་བའི་ཕྱོགས་ཉིད་དོ། །

[Block 3520]
དགེ་འདུན་འབྱེད་པ༌[^2294]ལ་སོགས་པའི་འཇིག་པ༌[^2295]གསུམ་ནི་གནོད་པའི་གཞི་ཉིད་དང་མཐུན་པ་ཉིད་དོ། །

[Block 3521]
གནས་པའི་གཞི་ལས་བྱུང་བ་ཞེས་བྱ་བ་ནི་གང་ཞིག་དགེ་འདུན་གྱིས་སྤངས་པའི་གང་ཟག་ནི་དགེ་འདུན་ལ་ཡང་མི་གུས་པར་གྱུར་པ་ཉིད་དང་། ཆོས་ལ་ཡང་མི་གུས་པར་གྱུར་པ་ཉིད་དོ། །

[Block 3522]
གང་ཞིག་བསྙེན་པར་མ་རྫོགས་པ་ཉིད་དང་ལྷན་ཅིག་ཉལ་བའི་བདག་ཉིད་ཅན་དེ་ལ་འདོད་ཆགས་དང་བྲལ་བ་མི་མཐུན་པའི་ཕྱོགས་སུ་གྱུར་པ་ཉིད་ཀྱིས་སྤང་བར་བྱ་བ་ཉིད་ཀྱི་ཕྱིར། སྡོམ་པ་མ་ལུས་པ་ཉམས་པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་དོ། །

[Block 3523]
ཁྱིམ་པ་དང་མུ་སྟེགས་ཅན༌[^2296]དང་ལྷན་ཅིག་ཉལ་བའི་གནས་ལ་རིག་པར་བྱ། མཚན་མི་མཐུན་པ་དང་ལྷན་ཅིག་ཏུ་གང་ཞིག༌[^2297]ཉལ་བའི་བདག་ཉིད་ཅན་གྱི་གནས་པ་ནི་དེ་ལ་མི་ཚངས་པར་སྤྱོད་པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་དོ། །

[Block 3524]
དེ་ཡང་གནས་པ་མ་ཡིན་པའི་གཞི་ཉིད་དོ། །

[Block 3525]
མ་གུས་པའི་གཞི་ལས་བྱུང་བ་ཉིད་ནི་སངས་རྒྱས་དང་། ཆོས་དང་། དགེ་འདུན་གྱི་ཕྱིར་མ་གུས་པས་སྐྱབས་སུ་འགྲོ་བ་ཞེས་བྱའོ། །

[Block 3526]
གང་ཞིག་རབ་ཏུ་བྱུང་བ་ཉིད་དང་། རབ་ཏུ་བྱུང་བའི་སྡོམ་པ་དག་གི༌[^2298]ཡན་ལག་དེ་ལ་ཉམས་པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་དོ། །

[Block 3527]
གལ་ཏེ་གང་ཟག་གི་ཕྱིར་བརྟེན་པ་ཡིན་ན་སྡོམ་པ་ཐམས་ཅད་འཇིག་པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་དོ། །

[Block 3528]
མཁན་པོའི་ཕྱོགས༌[^2299]འདི་ནི་བདག་གི་མཁན་པོའི་ཞེས་བྱ་བས་བླངས་པ་སྔོན་དུ་འགྲོ་བ་ཅན་གྱི་ཁས་བླངས་པ་གང་ཡིན་པ་དེ་ནི་འཇིག༌[^2300]པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་དོ། །

[Block 3529]
གལ་ཏེ་གང་ཟག་གཞན་ཡིན་ན་དེའི་ཕྱོགས་དང་མཐུན་པ་འདི་ལ་མ་གུས་པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་དོ། །

[Block 3530]
མི་སྦྱོང་བའི་གཞི་ནི་སྦྱོང་བར་མི་བྱེད་པ་སྟེ། བདག་ཉིད་དག་པར་བྱ་བའི་ཕྱིར་གསོ་སྦྱོང་དང་དགག་དབྱེ་དག་མི་བྱེད་པའོ། །

[Block 3531]
མི་གནས་པར་འདུག་པ་ལ་སོགས་པས་སྦྱོང་བར༌[^2301]མི་བྱེད་པའོ། །

[Block 3532]
གཞན་དུ་ན་འཇུག་པ་ཉིད་འགྲུབ་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ༌[^2302]འདི་རྣམས་ཀྱི་བྱ་བ་ཉིད་དོ། །

[Block 3533]
དེ་ལྟ་བས་ན་འདི་རྣམས་ལ་སྡོམ་པ་ཐམས་ཅད་འཇིག་པའི་ཕྱོགས་དང་མཐུན་པ་ཉིད་དུ་རིག་པར་བྱ་སྟེ། གསོ་སྦྱོང་བྱེད་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3534]
འདིའི་ཚིག་མེད་པའི་ཕྱིར་རྗེས་སུ་བསྒྲུབ་པར་བྱ་བ་ཤེས་པར་བྱའོ། །

[Block 3535]
དེ་ཉིད་ཀྱི༌[^2303]ཕྱིར་གཞན་དུ་ན་འཇུག་པ་བསྒྲུབ་པ་ཉིད་དུ་མི་འགྱུར་རོ་ཞེས་བྱ་བའི་རིགས་པ་ལས་ཐོབ་པའི་ཕྱིར་དང་དགག་དབྱེ་བསྒྲུབ་པའི་རྗེས་སུ་འབྲངས་པས་སྦྱོང་བར༌[^2304]རིག་པར་བྱའོ། །

[Block 3536]
མཚན་མཐུན་པ༌[^2305]བསྙེན་པར་རྫོགས་པ་ལ༌[^2306]གསོ་སྦྱོང་བྱེད་པ་འདི་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3537]
སྔགས་ནི་འདི་ཡིན་ཏེ། ཆེ་གེ་མོ་ཞིག་དགོངས་སུ་གསོལ། དེང་དགེ་འདུན་གྱི་གསོ་སྦྱོང་བཅོ་ལྔ་པ་ལགས་ཏེ། བདག་དགེ་ཚུལ་མིང་འདི་ཞེས་བགྱི་བའི་གསོ་སྦྱོང་ཡང་གསོ་སྦྱོང་བཅོ་ལྔ་པ་ལགས་ན། བདག་དགེ་ཚུལ་མིང་འདི་ཞེས་བགྱི་བ། བར་ཆད་ཀྱི་ཆོས་རྣམས་ཡོངས་སུ་དག་གོ་ཞེས་བདག་ཉིད་ཆེ༌[^2307]ཞེས་བྱ་བ་ལ་སོགས་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 3538]
བསླབ་པ་བྱིན་པ་ནི་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་ལྟུང་བ་ལ་སྦྱོར་བ་དགེ་སློང་འདྲ་བ་ཉིད་དོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3539]
འདིར་འདི་ལ་དགེ་སློང་མ་ཡང་དེ་བཞིན་དུ་ཕན་ཚུན་འདྲ་བ་ཉིད་དུ་རིག་པར་བྱའོ། །

[Block 3540]
དགེ་སློང་བཞིན་དུ་འདིས༌[^2308]ལྷག་པར་སྤྱོད་པ་ལ། དགེ་སློང་བཞིན་དུ་ཡང་གཞན་ལ་བརྡེག་པ་དང་། གཟས་པ་དང་། འགྱོད་པ་བསྐྱེད་པ་ལ་སོགས་པས་ལྟུང་བ་རྣམས་བསྐྱེད་དོ་ཞེས་བྱ་བའི་དོན་ཏོ། །
--- END BLOCKS ---
