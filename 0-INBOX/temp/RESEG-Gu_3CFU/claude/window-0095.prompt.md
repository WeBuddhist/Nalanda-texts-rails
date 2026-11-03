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
[Block 3326]
སྨྲས་པ་ཁྱོད་དུས་གང་གི་ཚེ་ཁོམ་པར་འགྱུར་བ་ཁོ་བོས་ཇི་ལྟར་ཤེས་པར་བྱ། སྨྲས་པ། ཁོ་མོའི་ཁྱིམ་ན་དགེ་སློང་ཁྱིམ་དུ་ཉེ་བར་འགྲོ་བ་ཡོད་དེ། དེས་ཁྱེད་ཀྱི༌[^2296]རྒྱབ་ཏུ་ཁུ་ཚུར་སྣུན་པར༌[^2297]བྱེད་ནའོ། །

[Block 3327]
དེ་ནས་དགེ་སློང་དེ་ཁྱིམ་དེར་ཞུགས་པ་ན་དེ་ལ་བུད་མེད་དེས་སྨྲས་པ། འཕགས་པ་ཁྱིམ་བདག་ཆེ་གེ་མོའི་རྒྱབ་ཏུ་ཁུ་ཚུར་བསྣུན་ནུས་སམ། དེས་ནུས་སོ་ཞེས་སྨྲས་ཏེ། དེ༌[^2298]སོང་ནས་ཁྱིམ་བདག་དེའི་རྒྱབ་ཏུ་ཁུ་ཚུར་བསྣུན་པ་དང་། དེས་སྨྲས་པ། [^2299]བཙུན་པ་ལ༌[^2300]ལེགས་སོ་ལེགས་སོ་དོན་གྲུབ་བོ། །

[Block 3328]
དེས་སྨྲས་པ། འདི་ཅི་ཞིག་ཡིན། སྨྲས་པ། བརྡའོ། །

[Block 3329]
དགེ་སློང་དེ་འགྱོད་པ་སྐྱེས་པ་དང་། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་འདུན་ལྷག་མའི་ལྟུང་བར་མི་འགྱུར་ཏེ། ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3330]
སྨྱན་བྱེད་པའི་འདུལ་བྱེད་རྣམས་སོ།། །།

[Block 3331]
སྤྱོད་ལམ་བཞིའི་སྣོད་མ་ཡིན་པ་ཉིད་ལ་ནི་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ༌[^2301]ནི་ཉེས་པ་ཡོད་པ་མ་ཡིན་པ་ནི་ཉེས་པ་མེད་པའོ། །

[Block 3332]
སྤྱོད་ལམ་བཞི་པོ་ལ་གནས༌[^2302]གང་ཡིན་པའི་སྣོད་མ་ཡིན་པ་ནི་སྣོད་མ་ཡིན་པ་ཞེས་བྱ་བ་གཞིར༌[^2303]མི་རུང་བའི་གནས་ཏེ། གནས་དེ་ལྟ་བུ་བྱེད་པ་ལ་ཉེས་པ་མེད་དོ། །

[Block 3333]
འཇིགས་པར༌[^2304]གྱུར་པ་ཉིད་ཀྱིས༌[^2305]དེ་ཙམ་དུ་རྒྱུག་ཅིང་ཡིད་ལ་ཞུགས་པས་འཇུག་པའི་དོན་ཉིད་ཀྱིས་ཡན་ལག་ཐམས་ཅད་རེངས་པས་ལངས་པར༌[^2306]གནས་པར་མི་ནུས་པ་དེ་ལ་དེའི་གནས་ལ་སྣོད་མ༌[^2307]ཡིན་པ་ཉིད་དོ། །

[Block 3334]
གང་དུ་འདུག་པས་གནས་པར་ནུས་པ་དེ་ལ༌[^2308]མལ་དུ་སྣོད་མ་ཡིན་པ་ཉིད་དོ། །

[Block 3335]
ཡང་དང་ཡང་དུ་འཆག་པ་ནི་འཆག་པའོ། །

[Block 3336]
དེ་བས་ན་གསུམ་རྣམས་ལ་གང་དུ་ཐ་མལ་པའི་འགྲོ་བ་བགྲོད་པར་གྱུར་པ་ལ་གོ་སྐབས་མེད་པ་དེ་ལ་འཆག་པའི་སྣོད་མ་ཡིན་པ་ཉིད་དོ། །

[Block 3337]
སྐྱིལ་མོ་ཀྲུང་བཅས་ནས་འདུག་པར་མི་ནུས་པ་དེ་ནི་གནས་པའི་སྣོད་མ་ཡིན་ནོ། །

[Block 3338]
དེ་བས་ན་སྐྱིལ་མོ་ཀྲུང་བཅིངས་པ་གང་གང་དུ་གླགས་མེད་པ༌[^2309]དེ་ལ་འདུག་པའི་སྣོད་མ་ཡིན་ནོ། །

[Block 3339]
མལ་ཙམ་ཉིད་དུ་ལན་གསུམ་དུ་ཐ་མལ་པས་འགྲོ་བ་བའི་རིམ་གྱིས༌[^2310]འཆག་པ་སྤྲོ་བ་དེ་བས་ན་རིང་བ་དང་ཞིང་གིས་སྐྱེས་པའི་ཚད་མཐའ་ནས་རྒྱར་ནི་སྐྱིལ་མོ་ཀྲུང་གི་ཚད་ཀྱི་དངོས་པོ་གང་ཡིན་པ་དེ་ལ་སོགས་པའི་ལྟུང་བ་བྱས་པ་ཉིད་དོ། །

[Block 3340]
གང་ཞིག་འདི་ལས་ཤིན་ཏུ་མ་ཆོག་པ་དེ་ལ་ནི་ལྟུང་བ་མེད་དོ། །

[Block 3341]
ས་གཞིའི་བདག་ཉིད་ཀྱིས་གཞི་དང་ཤིང་དང་རིན་ལ་སོགས་པའི་ཡོ་བྱད༌[^2311]བླངས་པ་དང་། མ་བླངས་པའི་གཞིའི་ཡོ་བྱད༌[^2312]ལས་ཁང་པ་དང་གཙུག་ལག་ཁང་བྱེད་པས་ཀུན་དུ་བསྒྲུབ་པ་ལ་ཡན་ལག་བཞི་པོ་ཐམས་ཅད་དུ་རུང་བ་ཉིད་དང་རྩོད་པ༌[^2313]མེད་པ་ཉིད་དང་། བརྩམ་དུ་རུང་བ་ཉིད་དང་། བརྟན་པ་ཉིད་ཅེས་བྱ་བ་ལས་འདའ་བར་བྱེད་པ་ལ༌[^2314]ཚད་ལས་ལྷག་པར་བྱེད་ན་མཐར་ནི་དགེ་འདུན་ལྷག་མར་འགྱུར་རོ། །

[Block 3342]
སྔར་ནི་སྦོམ་པོར་འགྱུར་རོ། །

[Block 3343]
ཡན་ལག་བཞི་པོ་མ་ཚང་བ་སྒྲུབ་པ༌[^2315]འདའ་བར་བྱེད་པ་ཚད་ཀྱི་མཐར་ནི་སྦོམ་པོར་འགྱུར་ལ། སྔར་ནི་ཉེས་བྱས་སུ༌[^2316]འགྱུར་རོ། །

[Block 3344]
འདའ་བར་མི་བྱེད་པ་ལ་ཡང་ཚང་བ་དང་མ་ཚང་བའི་ཡན་ལག་བཞི་པོ་མ་བསྒྲུབས་པ་ལ་མཐར་ནི་སྦོམ་པོ་སྟེ། སྔར་ནི་ཉེས་བྱས་སུ་འགྱུར་རོ། །

[Block 3345]
མ་བླངས་པའི་གཞིའི་ཡོ་བྱད་ཀྱི་ཚད་ལས་འདའ་བར་བྱེད་པ་ལ་ཡན་ལག་བཞི་པོ་མ་བསྒྲུབས་པ་ལ་མཐར་ནི་སྦོམ་པོ་སྟེ་སྔར་ནི་ཉེས་བྱས་སོ། །

[Block 3346]
ཚད་ལས་འདའ་བར་བྱེད་པ་ལ་ཡན་ལག་བཞི་པོ་ཐམས་ཅད་ཀྱིས་མ་བསྒྲུབས་པ་ལ་མཐར་ནི་ཉེས་བྱས་སུ་འགྱུར་ལ། སྔར་ཡང་ཉེས་བྱས་ཉིད་དོ། །

[Block 3347]
ཚད་ལས་འདའ་བར་མི་བྱེད་པ་ཡན་ལག་བཞི་པོ༌[^2317]ཐམས་ཅད་ཀྱིས་མ་བསྒྲུབས་པ་ལ་མཐར་ནི་ཉེས་བྱས་སུ་འགྱུར་ལ། སྔར་ཡང་ཉེས་བྱས་ཉིད་དོ་ཞེས་བྱ་བའི་རྣམ་པར་གཞག་པ་འདི་ལའོ། །

[Block 3348]
སྤྱོད་ལམ་བཞི་པོ་འགྲོ་བ་ལ་སོགས་པ་ཁང་པ་དང་གཙུག་ལག་ཁང་དག་ཚད་ལས་འདའ་བར་མ་བྱས་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 3349]
བསྐོས་པ༌[^2318]ཉིད་དང་མ་བསྐོས༌[^2319]པ་ཉིད་དག་ནི་གཙོ་བོ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གཙོ་བོ་མ་ཡིན་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3350]
བསྐོས་པ༌[^2320]ཉིད་ཅེས་བྱ་བ་ནི་གཞན་གྱིས་བྱེད་དུ་བཅུག་པ་ཉིད་དེ། དེའི་རྣམ་པ་ཉིད་བསྒྲུབ་པ་ཡིན་ནོ། །

[Block 3351]
གང་གི་རྣམ་པར་རང་གི་འདོད་པས་ཞེས་བྱ་བ་འདི་ལ་འདི་བསྟན་པའོ། །

[Block 3352]
འདིར་འདོད་པ་དང་འབྲེལ་བའི་ལྟུང་བ་བསྒྲུབ་པ་ལ་རྒྱུ་ཉིད་ཀྱི་ཕྱིར་བསྐོས་པའི༌[^2321]རྒྱུ་ལ་འདོད་པ་དང་འབྲེལ་པ་མེད་པའི་ཕྱིར་མ་ཆོག་པ་མེད་པས་གང་གིས་འདྲ་བ༌[^2322]ཉིད་མི་འདོད་པ་དེའི་འདོད་པ་ཟློག༌[^2323]པའི་དོན་དུ་མདོ་འདིའོ། །ཇི་ལྟར་ཞེ་ན། གང་གི་ཕྱིར་འདིར་ལྟུང་བ་འམ་འདྲ་བ་ཉིད་བསྒྲུབ་པ༌[^2324]མ་ཡིན་ཏེ། འདིར་འདོད༌[^2325]པ་འདི་ལ་བསྒྲུབ་པར་གནས་པའི་ཕྱིར་རོ། །

[Block 3353]
དེ་བས་ན་དགེ་སློང་རྗེས་སུ་གནང་བ་ཉིད་ལ་དངོས་གཞི་གྲུབ་པ་སྟེ། མངོན་པར་རྗེས་སུ་མ་གནང་བ་ཉིད་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3354]
བསྐོས་པ་ནི་རང་ཉིད་དང་འདྲའོ་ཞེས་བྱ་བ་ལ་བསྐོས་པས་བྱས་པ་ནི་སྐོ་བར་བྱེད་པ་རང་ཉིད་ཀྱིས་བྱས་པ་དང་འདྲའོ། །

[Block 3355]
ཇི་ལྟར་བདག་ཉིད་ཀྱིས་ཁང་པ་དང་གཙུག་ལག་ཁང་དག༌[^2326]ལོག་པ་ཉིད་དུ་སྒྲུབ་པར་བྱེད་པ་ཁ་ན་མ་ཐོ་བར་གྱུར་པ༌[^2327]དེ་བཞིན་དུ། བསྐོས་པས་ལོག་པ་ཉིད་དུ་སྒྲུབ་པར་བྱེད་ན་ཡང་སྐོ་བར་བྱེད་པ་ཉིད་ལ་ཁ་ན་མ་ཐོ་བར་འགྱུར་རོ་ཞེས་བྱ་བ་འདི་ལ་འདི་བྱེད་པའོ། །

[Block 3356]
གང་གི་ཚེ་གནས་པར་གྱུར་ན་བསྐོས་བཞིན་པས་སྐོ་བ༌[^2328]པོས་བསྒྲུབ་པ་ལ་བསྐོས་པ་དེ་ནི་འདིར་རྒྱུར་རིག་པར་བྱའོ། །

[Block 3357]
ཇི་སྐད་བསྒོ་བ་བཞིན་མི་བྱེད་པ་ལ་ལུས་དང་ངག་གིས་ནོད་ནའོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་བསྒོ་བ༌[^2329]བཞིན་མི་བྱེད་པ་བསྐོ་བ་བྱས་པ་འམ་བྱེད་དུ་བཅུག་པ་དེ་ལ་ཇི་སྐད་བསྐོ་བའི་རྒྱུ་དེ་ལ་ལུས་སམ་ངག་གིས་ནོད་ན་རང་ཉིད་དེ་མི་ནོད་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 3358]
ཡིད་ཀྱིས་ནོད་པ་ལ་ཡང་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3359]
འདིར་གཞུང་ནི་གལ་ཏེ་དེ་ལ་འདི་སྐད་ཅེས་ལེགས་པར་བྱས་སོ། །

[Block 3360]
ཤིན་ཏུ་བྱས་སོ་ངས་ཁྱོད་ལ་འདི་ལྟར་བསྐོའོ༌[^2330]ཞེས་ཟེར་ཞིང་། དེས་དེ་ལ་ཤིང་ངམ་རྩྭ་འམ་ལྕི་བ་འམ་ས་འཇིམ་རྣམས་འབུལ་བར་བྱེད་དེ། གང་མི་རུང་བ་བྱེད་དུ་འཇུག་ན་གཉིས་ཀ་ལ་ཡང་གཞི་ཇི་ལྟ་བ་བཞིན་དུ་ལྟུང་བར་འགྱུར་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3361]
བྱས་པ་ནི་གཅིག་ཉིད་དོ་ཞེས་བྱ་བ་ནི་འདིར་བྱེད་པ་ཐམས་ཅད་རྗེས་སུ་བསྒྲུབ་པའི་ཕྱིར་གཅིག་པ་ཉིད་དེ། ལོ་ལ་སོགས་པའི་ཚད་ཀྱང་སྡོད་པ་ལ་གཞན་ལ་མི་ལྟོས་པས་མ་བཏང་བ་ནི་འདིར་སྡོད་ཅིང་བྱས་པ་ལྟུང་བ་མང་བ་ཉིད་མེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 3362]
མི་ལྟོས་པས་བཏང་བ་ནི་དུམ་བུ་ལ་སོ་སོ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3363]
དེ་ལྟར་ན༌[^2331]མི་ལྟོས་པས་བཏང་བ་ལ་སྔར་གྱི་ཆ་ཙམ་ལྟུང་བ་སྟེ། མི་ལྟོས་པས་བར་དུ་ཡེ་བཏང་བ་ལ་གང་ཞིག་ཕྱིས་ཡང་རྩོམ་པར་བྱུང་བ༌[^2332]ལ་ཡང་ཕྱི་མའི་ཆ་ལའོ། །

[Block 3364]
ཕྱིས་ཀྱང་བསམ་པ་གཞན་གྱིས་རྩོམ་པ་ལ་ནི་གཞན་ཉིད་དོ། །

[Block 3365]
གཙོ་བོ་མ་ཡིན་པར་མཐར་ཐུག་པ་ལ་གང་ཞིག་འདིར་གཞན་ཐམས་ཅད་ལ་ཆ་ཐམས་ཅད་ཀྱི་བདག་ཉིད་མེད་པར་ལྟུང་བ་བྱས་པ་ཉིད་ཅེས་བྱ་བ་འདིར་རྣམ་པར་གནས་པར་རིག་པར་བྱའོ། །
--- END BLOCKS ---
