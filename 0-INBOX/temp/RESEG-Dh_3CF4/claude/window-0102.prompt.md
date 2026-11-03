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
[Block 3571]
མི་རྣམས་ཀྱི༌[^2293]གྲགས་པ་དེ་ཉམས་པར་གྱུར་ན་ནི་དེ་ཕྱིས་ཡང་གྲགས་པར་འགྱུར་བ་ཞེས་བྱ་བ་ནི་འཕེལ་བར་འགྱུར་བའོ། །

[Block 3572]
སྦྲུལ་ནག་ཅེས་བྱ་བ་འདི་ནི་མཇུག་བསྡུ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། ལྷ་གཅིག་བདག་ནི་བཟློག་པར་མི་རིགས་སོ། །ཞེས་བྱ་བ་ནི་བཟློག་པ༌[^2294]རིགས་པ་ཡང་ཡིན་མོད་ཀྱི་འོན་ཀྱང་བདག་ནི་བཟློག་པར་མ་མཛད་ཅིག་ཅེས་པ་སྟེ། ངེས་པར་གཟུང་བ༌[^2295]མ་ཡིན་བ་དང་ངེས་པར་གཟུང་བའི་རྒྱུ་སྟེ། གུས་པར་མཁྱེན་ནས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་ཏེ། གུས་པར་མཁྱེན་ནས༌[^2296]ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱད་ཀྱིས་ནི་ངེས་པར་གཟུང་བ་མ་ཡིན་པའི་རྒྱུ་བསྟན་ཏེ། །ངེས་པར་གཟུང་བ༌[^2297]ནི། བདག་ནི་སེམས་ཀྱིས་རབ་ཏུ་བྱུང་། ། ཞེས་བྱ་བ་ཕྱེད་འོག་མས་བསྟན་ཏོ། །

[Block 3573]
བྱམས་པ་ཡིས་ཞེས་བྱ་བ་ནི་རྗེ་བོའི་ཡོན་ཏན་ནོ། །

[Block 3574]
གུས་པར་མཁྱེན་ནས་ཞེས་བྱ་བ་ནི་འབངས་ཀྱང་ཡོན་ཏན་གུས་པ་དང་ལྡན་པར་ཁྱོད་ཀྱིས་དེ་མི་ཤེས་པ་ཡང་མ་ཡིན་ཏེ། ཁྱོད་ཀྱིས༌[^2298]འབངས་ཀྱི་སྐྱེ་བོ་ལ་དེ་ལྟར་བགྱི་བ་རིགས་ཏེ། དེ་བས་ན་ཁྱོད་ཀྱིས་བཟློག་པའི་རིགས་སོ། །

[Block 3575]
བདག་ནི་རེ་ཞིག་བཟློག་པར་བྱ་བ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། སེམས་ཀྱིས༌[^2299]རབ༌[^2300]བྱུང་ཟིན་པའི་ཕྱིར་རོ། །

[Block 3576]
དེས་ན་རབ་ཏུ་བྱུང་བ་ནི་འདུ་འཛིའི་ཉོན་མོངས༌[^2301]ཅན་འཛིན་པ་མི་རིགས་པའི་ཕྱིར་རོ། །

[Block 3577]
དེ་ནས༌[^2302]དེ་ཡི་མཛའ་བོ་དང་། ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིག་གིས་ནི་མཛའ་བོ་ལ་སོགས་པ་དམན་པ་དང་། བར་མ་དང་། གོང་མ་དག་གིས་བཟློག་པའི་ལུས་དང་ངག་གི་ལས་ཀྱི་བྱ་བ་རྣམས་བསྟན་ཏོ། །

[Block 3578]
དེ་ལ་རྐང་པ་ལ་འཇུས་ཏེ་ཞེས་བྱ་བས་ནི་དམན་པ་རྣམས་ཀྱི་ལུས་ཀྱི་ལས་ཀྱི་བྱ་བ་བསྟན་ཏོ། །

[Block 3579]
ཁ་ཅིག་ཐལ་མོ་སྦྱར་ཏེ་ཞེས་བྱ་བས་ནི་རབ་དང་མཉམ་པ་བར་མའི་བསྟན་ཏོ། །

[Block 3580]
མགུལ་ནས་འཇུས་ཏེ་ཞེས་བྱ་བས་ནི་གོང་མ་རྣམས་ཀྱི༌[^2303]དབང་དུ་བྱས་པའོ། །

[Block 3581]
འདི་གསུམ་ནི་ལུས་ཀྱི་ལས་ལས་བརྩམས་པའོ། །

[Block 3582]
བཟློག་པར་རྩོམ་པ་བཤད་པའོ། །

[Block 3583]
ཁ་ཅིག་ནི་སྤོབས་པའི་ཚུལ་གྱིས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ངག་གི་ལས་ལས་བརྩམས་ཏེ་བཟློག་པའི་དབང་དུ་བྱས་པ་སྟེ། ཁ་ཅིག་ནི་སྤོབས་པའི་ཚུལ་གྱིས་ཞེས་བྱ་བ་ནི་བར་མའི་དབང་དུ་བྱས་པའོ། །

[Block 3584]
ཁ་ཅིག་ནི་མཛའ་བོ་དང་ནང་མི་ཞེས་བྱ་བ་ནི་དམན་པའི་དབང་དུ་བྱས་པའོ། །

[Block 3585]
ལ་ལ་ནི་ཁྱིམ་ན་གནས་པའི་ཚུལ་གྱིས་ཞེས་བྱ་བ་ལ་སོགས་པས་ནི་གོང་མའི་དབང་དུ་བྱས་པའོ། །

[Block 3586]
མཛའ་བོར་འཐམས་པར་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་གཉིས་ཀྱིས་ནི༌[^2304]བྱང་ཆུབ་སེམས་དཔའ་ལ༌[^2305]ཕན་པར་འདོད་པ་དེས་ནགས་སུ་འགྲོ་བ་མི་རིགས་སོ་ཞེས་འགོག་པའི་དབང་དུ་བྱས་པའོ། །

[Block 3587]
མཛའ་བོར་འཐམས་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་དོན་ནི་མཛའ་བོ་བག་མེད་པ་ལས་མཛའ༌[^2306]བོ་རྣམས་ཀྱིས་ཕན་པའི་ཚིག་སྨྲས་པ་སྟེ། ཡུན་རིང་པོར་འཇུག་པའི་ཕྱིར་རོ། །

[Block 3588]
ཕན་པའི་ལམ་འདི་ལ་ནི་ལེགས་པ་དང་ཕན་པ་གཉིས་ལྷན་ཅིག་མི་འཐོབ་སྟེ། རྩུབ་པ་ཡིན་ན་ཡང་ཕན་པར་འགྱུར་བ་སྦྱར་བའི་རིགས་ཏེ། དེ་ལ་མ་སྦྱར་བར་གྱུར་ན་མི་དགེ་བར་འགྱུར་ཏེ། དགེ་བ་དང་མི་དགེ་བ་རྣམས་ལས་དགེ་བའི་ཆོས་མི་སྒོམ་ཞིང་། མི་དགེ་བའི་ཆོས་ལ་འཇུག་པར་འགྱུར་ཏེ། མི་ཕན་པར་སྒྲུབ་པའི་ཕྱིར་རོ། །

[Block 3589]
ནགས་པས་ཁྱིམ་དགའ་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིའི་དོན་ནི་ནགས་ན་གནས་པ་ལས༌[^2307]བདག་ལ་ཟློག་པར་བྱེད་དེ། ཇི་ལྟར་ལྡོག་པར་བྱེད་ཅེ་ན། སྡིག་པས་གོས་པ་བཞིན་དུ་སྟེ། དོགས་ཤིང་འཇིགས་པ་མེད་པར་རོ། །

[Block 3590]
ཇི་ལྟར་སྡིག་པས་གོས་པ་ནི་དོགས་ཤིང་འཇིགས་པ་མེད་པར༌[^2308]རྩུབ་པ་ཡིན་ན་ཡང་ཟློག་ཅིང་འགོག་པར་བྱེད་པ་དེ་བཞིན་དུ་འདི་དག་སེམས་ཞེས་བྱ་བ་ཡིན་ཏེ་མཛའ་བོ་ལ་སོགས་པ་རྣམས་སོ། །

[Block 3591]
ཐ་མལ་གནས་པའི་སེམས་ཞེས་བྱ་བ་ནི་ནད་མེད་པ་སྟེ། ནགས་པས་ཁྱིམ་དགའ་སྙམ་དུ་ཇི་ལྟར་སེམས་པའོ། །

[Block 3592]
ཇི་ལྟར་སེམས་པ༌[^2309]དེ་ཉིད་སྒྲུབ་པའི་ཕྱིར་སྨྲས་པ།[^2310] ནགས་ན་གནས་པ་དོགས་ཤིང་ཞེས་བྱ་བ་དང་། སྡིག་པས་གོས་བཞིན་དུ་ཞེས་བྱ་བ་གཉིས་ཀྱིས་བསྟན་ཏོ། །

[Block 3593]
དེ་ནི་བྱང་ཆུབ་སེམས་དཔའ་ལ་ཕན་པར་འདོད་པའི་དབང་དུ་བྱས་ནས་ངུ་བ་ལ་ནགས་ཚལ་གནས་པ་ལ་ཞེས་བྱ་བ་ནི་ཆོས་བསྒྲུབ་པར་འདོད་པའོ། །

[Block 3594]
གསོན་བཞིན་དུ་ཞེས་བྱ་བ་ནི་ཤི་བ་ཡང་མ་ཡིན། ཤི་བར་འགྱུར་བ་ཡང་མ་ཡིན་པའི་དོན་ཏོ། །

[Block 3595]
ད་ནི༌[^2311]བདག་ཉིད་དང་བྲལ་བའི་མྱ་ངན་གྱི་རྒྱུ་ལ་ཡང་། ང་དང་བྲལ་བས་དེ་ལྟར་མི་དགའ་ན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། རབ་ཏུ་མི་འབྱུང་བའི་རྒྱུ་ནི་ཁྱིམ་ཡོངས་སུ་གཏང་བར་དཀའ་བའི༌[^2312]ཕྱིར་ང་དང་མི་འབྲལ་ན་ནི་ཞེས་བྱ་བའི་དབང་དུ་བྱས་ནས་ཚིགས་བཅད་ཀྱི༌[^2313]ཕྱེད་འོག་མས་བསྟན་ཏོ། །

[Block 3596]
ནང་མི༌[^2314]ཡོངས་སུ་གཏོང་བ་ཤིན་ཏུ་དཀའ་བ་ཡིན་ཡང་རབ་ཏུ་མི་འབྱུང་བ་ནི་མི་རིགས་སོ། །ཞེས་བསྟན་པའི་ཕྱིར། དེ་སྟེ་བདག་གི་མི་ལ་ཆགས་པའི་ཕྱིར། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3597]
དེ་ལྟར་ཅིས་མི་བྱེད་ཅེས་བྱ་བ་ནི་ཇི་ལྟར་ངའི་རྗེས་སུ་རབ་ཏུ་འབྱུང་བའི་རང་མི་ལ་ཆགས་པས༌[^2315]བགེགས༌[^2316]སུ་བྱེད་པ་ཡིན་ན་དེ་ལྟར་དགྲ་དང་དམག་འགྱེད༌[^2317]ཅིང་འཇུག་པ་ན་ཡང་རང་མེའི་སྐྱེ་བོ་མང་པོ་ལ་ཆགས་པས་བགེགས༌[^2318]ཅིའི་ཕྱིར་མི་བྱེད་ཅེས་པའོ།

[Block 3598]
[^2319] །ཕོངས་པར་གྱུར་པའི་ཚེ་ན་མཐོང་བར་གྱུར་པའི་མཛའ་བོའི་རང་བཞིན་གང་ཡིན་པ་དེ་ནི་ཕོངས་པར་གྱུར་པའི་ཚེ་མཐོང་བའོ། །

[Block 3599]
མཛའ་བོའི་རང་བཞིན་ནི་ཕོངས་པའི་ཚེ་རྗེས་སུ་འབྲང་བ་དང་ངུ་བའོ། །

[Block 3600]
དེ་ལ་ཕོངས་པའི་ཚེ་མཐོང་བ་ནི་སྔར་དུས་གཞན་གྱི་ཚེ་ན་ཡིན་ཏེ། སྔར་མཐོང་བའི་ཕྱིར་ཕོངས་པའི༌[^2320]རྗེས་སུ་འབྲང་བའོ། །

[Block 3601]
མཛའ་བོ་བརྟེན་པར༌[^2321]གྱུར༌[^2322]ཀྱང་ཞེས་བྱ་བ་ནི་ཡུན་རིང་པོ་ནས་འདྲིས་པར་གྱུར་ཀྱང་ངོ་། །གཡོ་ཉིད་གཡོ་ཡིན་པས་གཡོ་ཕྱི་བཞིན་མི་འབྲང་བ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་འགྲོ་བ་མེད་པ་སྟེ། མཆི་མས་འཇུ་ཞིང་འོང་བ་ཉི་ཚེར་ཟད་པའོ། །

[Block 3602]
མཛའ་བོའི་རང་བཞིན་ནི་ངུ་བ་དང་ཕོངས་པ་རྗེས་སུ་འབྲང་བ་ཡིན་ཏེ། དེ་ལ་དེ་གཉིས་ལས་ཕོངས་པའི་རྗེས་སུ་འབྲང་བ་མེད་དོ། །

[Block 3603]
རབ་ཏུ་འབྱུང་བའི་མཚན་ཉིད་ནི་རབ་དུ་བྱུང་བ་དེ་ཕོངས་པ་ཉིད་ཡིན་ཏེ། ངུ་བར་འོས་པའི་ཕྱིར་རོ། །

[Block 3604]
གལ་ཏེ་ཕོངས་པ་མ་ཡིན་ན་ནི་རབ་དུ་བྱུང་བ་ལ་མི་ངུ་བ་ཡིན་ཏེ། དེས་ན་དེ་ཕོངས་པ་ཡིན་པས་ཕོངས་པ་དེའི་རྗེས་སུ་འབྲང་བར་བྱ་སྟེ་རྗེས་སུ་རབ་དུ་འབྱུང་བར་བྱའོ། །

[Block 3605]
ཇི་ལྟར་མཛའ་བོ་མྱ་ངན་གྱིས་གདུངས་ཤིང་ངུ་བ་ལ། མཛའ་བོས་མྱ་ངན་བྱ་བ་དང་ངུ་བ་ཡིན་ཏེ། དེ་བཞིན་དུ་འདིར་ཡང་འཇིགས་པ་མེད་པར་བྱ་བ་ཡིན་ཏེ། རྒྱུ་གཅིག་ལས་ནི་མཛའ་བོའི་རང་བཞིན་གཡོ་ཉིད་དུ་འགྲོ་བ་སྟེ། ཇི་ལྟར་ཤེས་ཤེ་ན། རྗེས་སུ་འགྲོ་བ་ནི་མེད་དེ། མཆི་མས་འཇུ་བ་ཉི་ཚེའོ། །

[Block 3606]
དེ་ཉིད་བསྟན་པའི་ཕྱིར། སླར༌[^2323]དུ་བཟློག་པའི་ཕྱིར་ནི་སྐད་འཛེར་ཞིང་།[^2324] །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3607]
ཇི་ལྟར་སྐད་འཛེར་བ༌[^2325]དང་བཅས་པ་དང་། མཆི་མ་དང་བཅས་པའི་མིག་དང་། མགོ་བོ་བཏུད་དེ་མཚུངས་པ་ལ་ཡང་བླ་མ་འདྲ་བ༌[^2326]ཕྱག་འཚལ་ཞིང་ཞེས་བྱ་བ་ཡིན་ཏེ། ཅིའི་ཕྱིར་བྱེད་ཅེ་ན། བཟློག་པ་དེའི་ཕྱིར་ཏེ། དེ་ལྟར་དེ་དག༌[^2327]ཐམས་ཅད་ནི་བཟློག་པའི་ཕྱིར་བྱེད་པ་ཡིན་གྱི། རྗེས་སུ་འགྲོ་བའི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 3608]
གལ་ཏེ་རྗེས་སུ་འགྲོ་བ་ཡིན་ན་ནི་ཅིའི་ཕྱིར་དེ་དག་ཉི་ཚེ་བྱེད་པ་ཡིན་ཏེ། རྗེས་སུ་འགྲོ་བར༌[^2328]མི་བྱེད་པའོ། །

[Block 3609]
གང་གི་ཕྱིར་རྗེས་སུ་འགྲོ་བར་མི་བྱེད་ཀྱི། བཟློག་པའི་ཕྱིར་བྱེད་པ་ཡིན་པས། དེ་བས་ན་མཛའ་བོའི་རང་བཞིན་ཏེ། གཡོ་དང་ཐབས་སུ་འགྱུར་བའོ། །

[Block 3610]
དེ་ལྟར་རེ་ཞིག་ཚིགས་བཅད་འདིས་ནི་གང་སྔར་བཤད་པའི་མཆི་མས་འཇུ་ཞིང་ངུ་བ་ཞེས་བྱ་བ་དེ་ཉིད་བསྒྲུབ་པ་ཡིན་ནོ། །
--- END BLOCKS ---
