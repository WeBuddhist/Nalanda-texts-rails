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
[Block 3851]
དེ་ཉིད་བསྟན་པར་བྱ་བའི་ཕྱིར། གླེང་གཞི་ཞེས་བྱ་བ་ལ་སོགས་པ་སྨོས་པ་ལ། གླེང་གཞི་ནི་དང་པོའི་ཚིག་དང་དེའི་ལྷག་མར་གྱུར་པ་ལེའུ་དང་པོའོ། །

[Block 3852]
དབང་དུ་མཛད་ནས་ཀྱང་ཞེས་པ་ནི་དེ་ལ་བརྟེན་པས་སོ། །

[Block 3853]
དོན་གང་ཞེས་པ་ནི་རིམ་པ་གཉིས་ཀྱི་མཚན་ཉིད་དོ། །

[Block 3854]
བསྟན་པ་ཞེས་པ་ནི་སོ་སོར་བསྟན་པའོ། །

[Block 3855]
དེ་ཉིད་དུ་ནི༌[^2393]ཞེས་པ་ནི༌[^2394]གླེང་གཞིའི་ཚིག་ཁོ་ན་ལའོ། །

[Block 3856]
རྒྱུད་ཀྱི་དོན་ཞེས་པ་ནི་རྒྱུད་ཕྱི་མ་དང་ལྷན་ཅིག་ཏུ་ལེའུ་བཅུ་བདུན་གྱི་བདག་ཉིད་ཅན་གྱི་དཔལ་གསང་བ་འདུས་པའི་རྒྱུད་ཀྱི་དོན་བསྟན་ཏོ། །

[Block 3857 [VERSE]]
ཨརྒ་ལས་སྦྲང་ཐོབ་འགྱུར་ན། །
ཅི་ཡི་ཕྱིར་ནི་རི་ལ་འགྲོ། །
འདོད་པའི་དོན་ནི་རྙེད་འགྱུར་ན། །
མཁས་པ་གང་གིས༌[^2395]ཡང་འབད་བྱེད། །

[Block 3858]
ཅེས་ཚིག་ལས་གླེང་གཞིའི་ཚིག་ཙམ་ཡོངས་སུ་ཤེས་པས་རྣལ་འབྱོར་པ་བྱ་བ་བྱས་པར་འགྱུར་ཞེས་ཅིའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས༌[^2396]ལེའུ་བཅུ་བདུན་གྱི་བདག་ཉིད་བསྟན་ཞེ་ན། སྨྲས་པ། ལྷག་མ་ཞེས་པ་ལ། གླེང་གཞིའི་ཚིག་ལས་གཞན་ཐམས་ཅད་རྒྱུད་ཀྱི་ལུས་ནི་ལྷག་མའོ། །

[Block 3859]
དགོས་པ༌[^2397]ལས་གཞན་ནི་ལྷག་མ་ཡིན་ཞེས་འབྱུང་ངོ་། །ཞར་ལ་བྱུང་བ་ཞེས་པ་ནི་གླེང་གཞིའི་ཚིག་གིས་རྒྱུད་ཀྱི་དོན་ཤེས་ཀྱང་དེའི་སྤོབས་པའི་མཚན་ཉིད་ནི་ཞར་ལ་བྱུང་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3860]
ཇི་སྐད་དུ། སྒྲུབ་པའི༌[^2398]དེ་རྣམས་ནི་ལེགས་པར་གཟུང་བ་ཡིན་ཏེ། གང་གི་མཚན་ཉིད་དང་སྤྲོས་པ་ཡོད་པའོ་ཞེས་འབྱུང་ངོ་། །དེ་བཞིན་དུ། ཡང་རྒྱས་པར་བཤད་པ་ནི་ཤིན་ཏུ་གསལ་བར་འགྱུར་རོ་ཞེས་འབྱུང་བས་སོ། །

[Block 3861]
གལ་ཏེ་དེ་ལྟ་ཡིན་ན་བཤད་པའི་རྒྱུད་དང་། རྒྱུད་ཕྱི་མ་དང་། ཡན་ལག་གི་རྒྱུད་བཅོམ་ལྡན་འདས་ཀྱིས་ཅིའི་ཕྱིར་གསུངས་ཤེ་ན། སྨྲས་པ། འདིར་ནི་བསྐལ་པ་དང་པོ་འདི་ལ་བཅོམ་ལྡན་འདས་ཀྱིས་ཞལ་གྱི་མན་ངག་ཁོ་ན་གསུངས་ཏེ། དེ་ཙམ་གྱིས་གདུལ་བྱ་རྣམས་ཀྱི་དངོས་གྲུབ་ཐོབ་པར་འགྱུར་རོ། །

[Block 3862]
དེའི་རྗེས་སུ་ཞལ་གྱི་མན་ངག་འཛིན་པར་ནུས་པ་མེད་པར་གཟིགས་ནས་རྩ་བའི་རྒྱུད་རྣམས་གསུངས་པས་གླེགས་བམ་དུ་གྲགས་སོ། །

[Block 3863]
དེའི་ཡང་རྗེས་སུ་རྩ་བའི་རྒྱུད་ཀྱིས་ཀྱང་རྟོགས་པ་མེད་པས་རྒྱུད་ཕྱི་མ་ཡན་ལག་གི་རྒྱུད་གསུངས་སོ། །

[Block 3864]
དེའི་རྗེས་སུ་རྒྱུད་ཕྱི་མ་དང༌[^2399]ཡན་ལག་གི་རྒྱུད་ཀྱིས་གང་གསལ་བར་མ་གྱུར་པས་བཤད་པའི་རྒྱུད་རྣམས་ཀྱང༌[^2400]གསུངས་ཏེ། གང་གི་ཚེ་དེ་རྣམས་ཀྱིས་ཀྱང་རྟོགས་པར་མ་གྱུར་ན་དེའི་ཚེ་སྔོན་གྱི་སློབ་དཔོན་ཁྱད་པར་དུ་གྱུར་པ་རྣམས་ཀྱིས་འགྲེལ་པ་དང་། དཀའ་འགྲེལ་དང་། ཊཱི་ཀཱ་དང་། རྒྱན་ལ་སོགས་པ་བྱས་པ་དང་། བྱེད་པར་ཡང་འགྱུར་རོ། །

[Block 3865]
དེའི་ཕྱིར་ན་དུས་ཀྱིས༌[^2401]དབྱེ་བ་དང་། གདུལ་བྱའི་བློའི་བྱེ་བྲག་ལ་བརྟེན་ཏེ། བཅོམ་ལྡན་འདས་ཀྱིས༌[^2402]ཆོས་བསྟན་པ་ནི་མདོར་བསྡུས་པ་དང་རྒྱས་པར་གསུངས་པ་ཞེས་ཞར་ལ་གསུངས་པ་ལ་སྐྱོན་མེད་དོ། །

[Block 3866]
སྐུ་དང་གསུང་དང་ཐུགས་གསང་བ་ལ་གཟིགས་ནས་ཞེས་པ་ལ་དོན་ནི་འདི་ཡིན་ཏེ། བསྐྱེད་པའི་རིམ་པའི་ཕྱོགས་སུ་རིགས་ལྔ་ཉེ་བར་བསྡུས་པའི་རིགས་གསུམ་གྱི་ངོ་བོ་དེ་ཁོ་ན་ཉིད་བསྟན་པས་སྐུ་གསུང་ཐུགས་སོ། །

[Block 3867]
གསང་བ་ནི་དེ་ཡང་ཉེ་བར་སྡུད་པར་བྱེད་པ་རྡོ་རྗེ་འཆང་ཆེན་པོའི་ངོ་བོ་ཉིད་སོ་སོར་བསྟན་པས་སོ། །

[Block 3868]
རྫོགས་པའི་རིམ་པ་ལ་ཡང་ལུས་དང་ངག༌[^2403]ཡིད་རྣམ་པར་དག་པའི་ངོ་བོ་ཉིད་རྡོ་རྗེ་བཟླས་པ་དང་། སེམས་རྣམ་པར་དག་པ་དང་། བདག་བྱིན་གྱིས་རློབ་པའི་མཚན་ཉིད་དང་མན་ངག་བཞི་པའི་འོད་གསལ་བའི་མཚན་ཉིད་མངོན་པར་བྱང་ཆུབ་པའི་རིམ་པ་སོ་སོར་བསྟན་པའི་ཕྱིར། སྐུ་གསུང་ཐུགས་གང་ཡིན་པ་ལ་དེ་ཉེ་བར་བསྡུས་པ་མྱུར་དུ་ཡང་དག་པར་སྐྱེས༌[^2404]པའི་བདེ་བ་གཉིས་མི་ཕྱེད་པའི་མཚན་ཉིད་ཅན་མི་གནས་པའི༌[^2405]མྱ་ངན་ལས༌[^2406]འདས་པའི་ངོ་བོ་ཉིད་ཟུང་དུ་འཇུག་པའི་རིམ་པ་སོ་སོར་བསྟན་པར་བྱེད་པའི་ཕྱིར་གསང་བ་ཡང་ཡིན་པས་སྐུ་གསུང་ཐུགས་ཀྱི་གསང་བའོ། །

[Block 3869]
གཟིགས་ནས་ཞེས་པ་ནི་ཐོས་པ་དང་བསམ་པ་དག་གིས་སོ། །

[Block 3870]
ཐུགས་སུ་ཆུད་པར་ཞེས་པ་ནི་བསྒོམ་པས༌[^2407]སོ། །

[Block 3871]
མཛད་པ༌[^2408]ནི་རྡོ་རྗེ་འཆང་ཆེན་པོ་ལས་ཐོབ་ནས་དབྱངས་དེ་ཉིད་དང་ཚིག་དེ་ཉིད་དང་། དེ་དང༌[^2409]མཐུན་པའི་དོན་གྱིས་སྡུད་པ་པོས་རྣམ་པར་མཛད་པའོ། །

[Block 3872]
ཏིང་ངེ་འཛིན་གྱི་དཀྱིལ་འཁོར་ནི་པདྨའི་ནང་དུ་བསྐྱེད་ཅིང་སྤྲུལ་པའི་དཀྱིལ་འཁོར་རོ། །

[Block 3873]
གསང་བ་འདུས་པ་ཞེས་པ་ནི་སྔར་བཤད་པའི་དོན༌[^2410]དང་ལྡན་པ་ལའོ། །

[Block 3874]
བྱིན་གྱིས་རློབ་པ་ཞེས་པ་ནི་སྤྲོ་བ་དང་དགོད་པ་ལེའུ་གང་ལ་ཡོད་པ་དེ་ནི་དེ་བཞིན་གཤེགས་པ་ཐམས་ཅད་ཀྱི་ཏིང་ངེ་འཛིན་གྱི་དཀྱིལ་འཁོར་བྱིན་གྱིས་རློབ་པ་ཞེས་བྱའོ། །

[Block 3875]
ལེའུ་ཞེས་པ་ནི་འདི་ནི་གྲགས་པའི་སྒྲ་སྟེ་རྒྱུད་ཀྱི་དོན་ཡོངས་སུ་གཅོད་པའི་མཚན་ཉིད་སོ་སོར་བསྟན་པའོ། །

[Block 3876]
ཡང་ན་སྦྱོར་བ་ལ་གྲགས་པའི་སྒྲའོ། །

[Block 3877]
ཡན་ལག་གི་དོན་གྱི་དབྱེ་བའི་སྒོ་ནས་གཟུང་བར་བྱའོ། །

[Block 3878]
ཤ་སྦྲང་དང༌[^2411]མཆུ་སྙུང་ལ་སོགས་པའི་གནོད་པ་འཇོམས་པར་བྱེད་པ་གོས་སུ་གྲགས་པ་དེ་བཞིན་དུ། ཉོན་མོངས་པ་དང་ལས་དང་སྐྱེ་བའི་ཉེ་བར་འཚེ་བ་འཇོམས་པར་བྱེད་པས་ན། གོས་དང་འདྲ་བས་ན་གོས་སོ། །

[Block 3879]
འདིར་བཅོམ་ལྡན་འདས་ཀྱིས་རྟེན་ཅིང་འབྲེལ་པ་ཡན་ལག་བཅུ་གཉིས་པའི་མཚན་ཉིད་སྲིད་པའི་འཁོར་ལོ་གསུངས་པ་འདི་ལྟ་སྟེ། མ་རིག་པ་དང་། འདུ་བྱེད་དང་། རྣམ་པར་ཤེས་པ་དང་། མིང་དང་གཟུགས་དང་། སྐྱེ་མཆེད་དྲུག་དང་། རེག་པ་དང་། ཚོར་བ་དང་། སྲེད་པ་དང་། ཉེ་བར་ལེན་པ་དང་། སྲིད་པ་དང་། སྐྱེ་བ་དང་། རྒ་ཤིའོ། །

[Block 3880]
དེ་ལ་དང་པོ་དང་བརྒྱད་པ་དང་དགུ་པ་ནི་མ་རིག་པ་དང་། སྲེད་པ་དང་ལེན་པ་ནི༌[^2412]ཉོན་མོངས་པ་ཞེས་བྱ་བའོ། །

[Block 3881]
གང་གི་ཕྱིར་ཉོན་མོངས་པ་ཐམས་ཅད་ཀྱི་རྩ་བ་ནི་མ་རིག་པའོ། །

[Block 3882]
གང་གི་ཕྱིར་མི་རྟག་པ་དང་། མི་གཙང་བ་དང་སྡུག་བསྔལ་བ་དང་། བདག་མེད་པ་རྣམས་སུ་རྟག་པ་དང་གཙང་བ་དང་། བདེ་བ་དང་བདག་ཏུ་སྣང་བ་ནི་མ་རིག་པ་སྟེ། གཏི་མུག་ཆེན་པོའི་མུན་པའི་མཚན་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3883]
དེ་དང་ལྷན་ཅིག་སྤྱོད་པ་ནི་སྲིད་པ༌[^2413]དང་དགའ་བ་དང་ཆགས་པར་བཅས་པ་གང་གིས་སྲིད་པའི་ལོངས་སྤྱོད་རྣམས་ལ་འདོད་པ་སྐྱེ་བའོ། །

[Block 3884]
དེ་དག་སྲིད་པ་སྔ་མ་མ་རིག་པ་དང་སྲིད་པ་དག་གི༌[^2414]འགྲོ་བ་རིགས་དྲུག་གི་སྲིད་པའི་འཁོར་ལོ་མ་ལུས་པའི་རྩ་བ་ཡིན་ནོ། །

[Block 3885]
ཇི་སྐད་དུ།

[Block 3886 [VERSE]]
བདག་ཡོད་པ་ནི་གཞན་གྱི་འདུ་ཤེས་ཏེ། །
རང་དང་གཞན་གྱི་དབྱེ་བས་ཆགས་སྡང་བྱུང་། །
དེ་གཉིས་ཕན་ཚུན་ཀུན་དུ་འབྲེལ་པ་ལས། །
སྐྱོན་རྣམས་ཐམས་ཅད་རབ་ཏུ་སྐྱེ་བར་འགྱུར། །

[Block 3887]
ཞེས་འབྱུང་ངོ་། །

[Block 3888]
ལེན་པ་ཡང་དེ་དག་རྒྱས་པའི་མཚན་ཉིད་ཕུང་པོ་སོ་སོར་ལེན་པའོ། །

[Block 3889]
དེ་ལྟར་ཉོན་མོངས་པ་དེ་དག་གོ། །

[Block 3890]
དེ་བཞིན་དུ་གཉིས་པ་དང་བཅུ་པ་སྟེ་འདུ་བྱེད་དང་སྲིད་པ་དག་ནི་ལས་སོ། །
--- END BLOCKS ---
