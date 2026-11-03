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
[Block 3641 [VERSE]]
བརྒྱ་བྱིན་བྲམ་ཟེ་མྱོས་བྱེད་མ། །
ལེགས་པར་ཕ་རོལ་ཕྱིན་དང་ཉ། །
བྱ་དང་བུམ་པ་ཕྱུག་པོའི་བུ། །
དཀའ་ཐུབ་ཅན་དང་ཚོང་དཔོན་ནོ། །

[Block 3642]
ཞེས་པ་ལ། འདིར་ཡང་སྐྱེས་པའི་རབས་བཅུ་པོ་འདི་དག་གི་གོ་རིམས་བདག་གིས་འདི་ལྟར་མཐོང་སྟེ།

[Block 3643 [VERSE]]
བརྒྱ་བྱིན་བྲམ་ཟེ་མྱོས་བྱེད་མ། །
ལེགས་པར་ཕ་རོལ་ཕྱིན་དང་ཉ། །
བྱ་དང་བུམ་པ་ཚོང་དཔོན་དང་། །
ཕྱུག་པོའི་བུ་དང་དཀའ་ཐུབ་ཆེན། །

[Block 3644]
སྐྱེས་པའི་རབས་བཅུ་པོ་འདི་དག་གིས༌[^2340]བསྡུས་པའི་དོན་ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དབང་དུ་བྱས་པའོ། །

[Block 3645]
ཚུལ་ཁྲིམས་ཀྱང་རྣམ་པ་གཉིས་ཏེ། ཁྱིམ་པའི་ཕྱོགས་ལ་བརྟེན་པ་དང་། རབ་ཏུ་བྱུང་བའི་ཕྱོགས་ལ་བརྟེན་པ་དང་། [^2341]དེ་ལ་ཁྱིམ་པའི་ཕྱོགས་ལ་བརྟེན་པའི་ཚུལ་ཁྲིམས་ཀྱི་དབང་དུ་བྱས་པ་ནི་བདུན་ནོ། །

[Block 3646]
རབ་ཏུ་བྱུང་བའི་ཕྱོགས་ལ་བརྟེན་པ་ནི་གསུམ་མོ། །

[Block 3647]
དེ་ལ་ཁྱིམ་པའི་ཕྱོགས་ལ་བརྟེན་པའི་ཚུལ་ཁྲིམས་ནི། སྲོག་གཅོད་པ་དང་། མ་བྱིན་པ༌[^2342]ལེན་པ་དང་། འདོད་པས་ལོག་པར་གཡེམ་པ་དང་། བརྫུན་དུ་སྨྲ་བ་དང་། འབྲུའི་ཆང་དང་། བཅོས་པའི་ཆང་མྱོས་པར་འགྱུར་བ་འཐུང་བ༌[^2343]ལས་ལྡོག་པ་སྟེ། འདི་དག་ནི་བསླབ་པའི་གཞི་ལྔའོ། །

[Block 3648]
དེ་ལ༌[^2344]བརྒྱ་བྱིན་གྱི་སྐྱེས་པའི་རབས་སུ་ནི་སྲོག་གཅོད་པ་ལས་ལྡོག་པའི་དབང་དུ་བྱས་ནས། ལྷའི་དབང་པོ་དེ་རང་གི་སྲོག་ལ་མི་ལྟ་བས་དུད་འགྲོའི་སྐྱེ་གནས་སུ་གྱུར་པའི་སྲོག་གཅོད་པར་འཇུག་པ་ལས་ལྡོག་པ་སྟེ། དེ་ནི་སྲོག་གཅོད་པ་སྤངས་པ་ཡིན་ནོ། །

[Block 3649]
བྲམ་ཟེའི་སྐྱེས་པའི་རབས་སུ་རང་གི་བླ་མ་ལ་སོགས་པས་སྦྱོར་བ་བྱས་ཤིང་ཐོས་པའི་རྗེས་སུ་དཔག་པས་ཡང་དག་པར་བསྟན་ཀྱང་སྐྱེ་བོས༌[^2345]གཞན་དག་ལས་ཉེ་བར་རྟོག་པ༌[^2346]དང་། བདག་གི་དབང་དུ་བྱས་ནས། ངོ་ཚ་བ་ཉིད་ཀྱིས་མ་བྱིན་པར་ལེན་པ་ལས་ལོག་པ་དེ་ནི་མ་བྱིན་པར་ལེན་པ༌[^2347]སྤངས་པའོ། །

[Block 3650]
བདག་ཉིད་ལ་རང་དབང་དུ་བྱིན་པར་འགྱུར༌[^2348]ཏེ། སྨད་འཚོང་མའི་གནས་སྐབས་སུ་བྱའོ་ཞེས་པས་བྱིན་ན་ཡང་བགྲོད་པ་མ་ཡིན་པར་འཇུག་པ་སྟེ། འདོད་པ་ལས་ལོག་པར་གཡེམ་པ་སྤོང་བ་ནི་མྱོས་བྱེད་མའི་སྐྱེས་པའི་རབས་སུ་བསྟན་ཏོ། །

[Block 3651]
བརྫུན་རྣམ་པ་གསུམ་གྱི་དབང་དུ་བྱས་ནས་སྐྱེས་པའི་རབས་གསུམ་ཡིན་ཏེ། གནོད་པ་བཟློག་པའི་ཕྱིར་དང་། གནོད་པ་བདག་གིས་ཐོབ་པ་ལ་འདོད་པའི་དོན་རྙེད་པའི་ཕྱིར་དང་། བརྫུན་སྨྲ་བ་ལ་གོམས་པར་མ༌[^2349]བྱས་པའོ། །

[Block 3652]
གནོད་པ་བཟློག་པ་ནི་བདེན་པའི་ཚིག་ཉིད་ཀྱིས་འགྱུར་བར་བསྟན་པའི་ཕྱིར། ལེགས་པར་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྐྱེས་པའི་རབས་སོ། །

[Block 3653]
བདག་ཉིད་ཀྱིས་ཕོངས་པའི་གནས་སྐབས་དང་ཕྲད་པར་གྱུར་ཀྱང་། བདེན་པའི་ཚིག་ཉིད་ཐར་པར་གྱུར་པ་བསྟན་པ་ནི་ཉའི་སྐྱེས་པའི་རབས༌[^2350]སོ། །

[Block 3654]
བདེན་པའི་ཚིག་ལ་གོམས་པས་ནི་མེའི་འཇིགས་པ་ལས་ཀྱང་ཐར་བར་བྱེད་ནུས་ན། གཞན་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས༌[^2351]བསྟན་པའི་ཕྱིར། སྲེག་པའི་ཕྲུ༌[^2352]གུའི་སྐྱེས་པའི་རབས་བསྟན་ཏོ། །

[Block 3655]
བུམ་པའི་སྐྱེས་པའི་རབས་སུ་ནི་ཆང་ལས་ལྡོག་པ་སྟེ། གཞན་ཡང་ལྡོག་པར་བྱེད་ན་བདག་ཉིད་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 3656]
ད་ནི་རབ་ཏུ་བྱུང་བའི་ཕྱོགས་ལ་བརྟེན་པ་ལས་བརྩམས་ཏེ་སྐྱེས་པའི་རབས་གསུམ་མོ། །

[Block 3657]
དེ་ལ་དང་པོར་རེ་ཞིག་ཚོང་དཔོན་གྱི་སྐྱེས་པའི་རབས་སུ་རྒྱ་ཆུང་ངུས་ཀྱང་སྙིང་སྟོབས་དང་ལྡན་པ་དག་ཁྱིམ་ཡོངས་སུ་གཏང་བ༌[^2353]ཡིན་ཏེ། ཕུན་སུམ་ཚོགས་པ་ཐམས་ཅད་བོར་ཞིང་ནགས་སུ་གནས་པ་སྟེ། ངེས་པར་འབྱུང་བར་འདོད་པས་ནང་མི་དང་། ཉེ་དུའི་སྐྱེ་བོ་དང་། མཛའ་བཤེས་ལ་སོགས་པའི་ཚོགས་ཀྱིས༌[^2354]བཟློག་པར་གྱུར་ཀྱང་མི་འདོད་ན། གཞན་དག་གིས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་བསྟན་པས་སོ། །

[Block 3658]
རྒྱལ་རིགས་ཕྱུག་པོའི་བུ༌[^2355]སྐྱེས་པའི་རབས་སུ་ནི་མཛའ་བཤེས་ཀྱིས༌[^2356]ལོངས་སྤྱོད་ལ་སོགས་པ་བསྟབས་ཀྱང་། དེ་ལ་ཆགས་པ་མེད་པ་དེས་རབ་ཏུ་བྱུང་བ་ལ་མངོན་པར་དགའ་བར་གྱུར་པ་བསྟན་པའི༌[^2357]ཕྱིར་རོ། །

[Block 3659]
དཀའ་ཐུབ་ཅན་གྱི་སྐྱེས་པའི་རབས་སུ་ནི། སྨོན་ལམ་དང་། ཚངས་པར་སྤྱོད་པ་ལ་དགའ་ཞིང་ཆོག་ཤེས་པ་དང་། སེམས་འཁྲུགས་པ་མེད་པ་ལ་མངོན་དུ་ཕྱོགས་པའི་དབང་དུ་བྱས་ནས་བརྩམས་པའི་ཕྱིར་རོ། །

[Block 3660]
དེ་ལྟར་སྐྱེས་པའི་རབས་འདི་དག་གི་གོ་རིམས་ཀྱི་རྒྱུ་ནི་རིགས་པར་འགྱུར་ཏེ།[^2358] གཞན་ལ་ཡང་ཕན་པའི་ཕྱིར་བསྟན་པའོ། །

[Block 3661]
སྡེ་ཚན་གཉིས་པ་སྟེ། བཅུ་ཚན་གཉིས་པ་རྫོགས་སོ།། །།

[Block 3662 [HEADING]]
## གཙུག་ཕུད་བྱང་ཆུབ་ཀྱི་སྐྱེས་པའི་རབས། ^23-0

[Block 3663]
བྲམ་ཟེའི་རིགས་ཆེན་པོ་ཡོན་ཏན་ལ་གོམས་པའི་མཐུས་གྲགས་པ་རྒྱས་པ་ཞེས་བྱ་བ་འདིས༌[^2359]ནི་ཚུལ་ཁྲིམས་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་དང་། རྒྱུ་ལ་གོམས་པ་ཡང་བསྟན་ཏོ། །

[Block 3664]
འབྱོར་པའི་ཡོན་ཏན་ངེས་པ་ཞེས་བྱ་བ་འདིས་ནི་སྔ་མའི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 3665]
རྒྱལ་པོས་བཀུར་སྟི་བྱས་པ་དང་། འཇིག་རྟེན་པས་ལྷ་བཞིན་དུ་བཀུར་བ་ཞེས་བྱ་བ་འདིས་ནི་བཟོད་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་འབྲས་བུ་བསྟན་ཏོ། །

[Block 3666]
དེ་ལྟར་འདི་དག་གིས་ནི༌[^2360]བསོད་ནམས་ཀྱི་ཚོགས་བསགས་པ་ཉིད་དུ་བསྟན་པ་ཡིན་ཏེ། འདི་ལྟར་དེར་སྐྱེས་པ་ཡིན་པས། དེ་བས་ན༌[^2361]དེ་ཡང་དེའི་བསོད་ནམས་ཀྱི་ཚོགས་ཉིད་དུ་བསྟན་ཏོ། །

[Block 3667]
དེ་ལྟར་མང་དུ་ཐོས་པའི་ཡོན་ཏན་ལ་གོམས་པ་ཞེས་བྱ་བ་ལ་སོགས་པ་ནི་ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་སྦྱོར་བ་བསྟན་ཏོ། །

[Block 3668 [VERSE]]
མཁས་པ་རྣམས་ཀྱི་གྲགས་པ་ནི། །
མཁས་པ་ཉིད་ཀྱི་ནང་དུ་འཕེལ། །

[Block 3669]
ཞེས་བྱ་བ་ལ། དེའི་ནང་དུ་གྲགས་པ་ཅིའི་ཕྱིར་འཕེལ་ཞེ་ན། མཁས་པ་ནི་ཡོན་ཏན་རྟོག་པ་ལ་མཁས་པའི་ཕྱིར་ཏེ། རིན་ཆེན་ཤེས་ལ་རིན་ཆེན་དང་། [^2362]ཞེས་བྱ་བ་ཡིན་ཏེ། མཁས་པ་ཉིད་མཁས་པའི་ནང་དུ་གྲགས་པ་འཕེལ་བའོ། །ཅིའི་ཕྱིར་ཞེ་ན། དེ་ནི་རང་གི་ཡོན་ཏན་སྟོན་པར་ནུས་པའི་ཕྱིར་རོ། །ཅི་ལྟ་བུ་དག་ཅེ་ན། གཡུལ་ངོ་དག་ཏུ་དབའ་བོ་བཞིན། །ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 3670]
ཚེ་རབས་སྔ་མ་ལ་རབ་དུ་བྱུང་བ་ལ་གོམས་ཤིང༌[^2363]ཞེས་བྱ་བ༌[^2364]འདིས་ནི་རྒྱུ་མཐུན་པ་བསྟན་ཏོ། །

[Block 3671]
ཆོས་ལ་སེམས་པ་ཞེས་བྱ་བ་ནི་ཆོས་དང་ལྷན་ཅིག་པའི་དྲན་པ་ཡོད་པའི་ཕྱིར་རོ། །

[Block 3672]
[^2365]ཆོས་དང་བཅས་པའི་སེམས་སོ། །

[Block 3673]
དེར་གྱུར་པའི་ཆོས་ལ་སེམས་པ་ཉིད་དེ། དེ་བས་ན་ཆོས་དང་འགལ་བའི་ཕྱིར། ཁྱིམ་སྤངས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3674]
བློ་དང་ཤེས་རབ་རབ་ཏུ་གསལ་བའི་ཕྱིར། །ཞེས་བྱ་བ་འདིས༌[^2366]ནི་ཁྱིམ་གྱི་ཉེས་དམིགས་ཡོངས་སུ་ཤེས་པའི་ཕྱིར་རོ། །

[Block 3675]
རྒྱུ་འདི་གསུམ་གྱིས་ཁྱིམ་ལ་དགའ་བ་མེད་པར་འགྱུར་ཞིང་། དེ་དང་མི་མཐུན་པའི་ཕྱོགས་ནགས་ལ་ནི་མངོན་བར་དགའ་བ་ཡིན་ཏེ། ཁྱིམ་ན་གནས་པ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 3676]
གང་སྔར་བསྟན་པའི་ཆས་པ༌[^2367]སེམས་པ་ཞེས་བྱ་བ་དེ་བསྟན་པའི་ཕྱིར། ཁྱིམ་ཡོངས་སུ་མ་བཏང་ཞིང་། འདོད་པ་རྣམས་ལ་ཉེ་བར་ལོངས་སྤྱོད་པ་ལས་ནི་ཆོས་དང་འགལ་བ་ཡིན་ཏེ། འཐབ་མོ༌[^2368]ལ་སོགས་པ་མང་བའི་ཕྱིར་རོ། །

[Block 3677]
དེ་ལྟར་ཆོས་ལ་སེམས་པ་ནི་ཁྱིམ་ན་གནས་པ་ན་དགའ་བར་མ་གྱུར་པའོ། །ཤེས་རབ་དང་ལྡན་པའི་ཕྱིར་ཁྱིམ་ན་གནས་པ་ལ་དགའ་བར་མ་གྱུར་པ་དེ་བསྟན་པའི་ཕྱིར། རྒྱལ་པོ་དང་། རྐུན་པོ་ལ་སོགས་པ་ལྔ་དང་ཐུན་མོང་དུ་གྱུར་པར་ཤེས་པའི་ཕྱིར༌[^2369]དང་། ཆོག་མི་ཤེས་པར་ཡོངས་སུ་ཤེས་པའི་ཕྱིར་དང་། ཉེས་པ་དུ་མའི་གནས་སུ་གྱུར་པར་ཤེས་པའི་ཕྱིར་ཏེ། བློ་དང་ཤེས་རབ་རབ་ཏུ་གསལ་བའི་ཕྱིར། ཁྱིམ་ན་གནས་པ་ལ་དགའ་བར་མ་གྱུར་ཏོ། །

[Block 3678]
ཁྱིམ་པའི་ཆ་ལུགས་བོར་ནས་ཞེས་བྱ་བ་ལ། ཇི་ལྟར་ཁྱིམ་པའི་ཆ་ལུགས་བོར་ཞེ་ན། སྐྲ་དང་ཁ་སྤུ་བཟང་པོ་བྲེགས༌[^2370]པའི་ཕྱིར་དང་། [^2371]གོས་ཁ་དོག་བསྒྱུར་བ་ངུར་སྨིག༌[^2372]བགོས་པའི་ཕྱིར་རོ། །ཇི་ལྟར་རབ་ཏུ་བྱུང་བའི་ཆ་ལུགས་བླངས་ཤེ་ན། རབ་ཏུ་བྱུང་བའི་སྡོམ་པའི་དཔལ་ལ་གནས་པར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3679]
དེ་ཡང་དཀའ་ཐུབ་ཀྱི་ནགས་ཚལ་ན་གནས་མི༌[^2373]ནུས་པར་ཤེས་ནས་སོ། །

[Block 3680]
རབ་ཏུ་དཀའོ་ཞེས་བྱ་བ་ནི་བགྲོད་པར་དཀའ་བ་ཡིན་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
