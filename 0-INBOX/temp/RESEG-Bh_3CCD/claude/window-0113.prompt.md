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
[Block 3956]
གང་གི་དབང་གིས་གཞི་མཐུན་པའི་སྒོ་ནས་བ་ལང་དང་ཚོང་དཔོན་དག་བྱེད་པའི་ཚིག་དང་པོས་སོ་སོར་བསྟན་ཏོ། །

[Block 3957]
དགོས་པ༌[^2452]ནི་བ་ལང་དང་འདྲ་བར་རྨོངས་པར་གྱུར་པའི་ཚོང་དཔོན་ལ་མི་རྩི་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3958]
དེ་བཞིན་དུ་འདིར་ཡང་སྐུ་གསུང་ཐུགས་དང་བྱང་ཆུབ་ཀྱི་སེམས་ཕན་ཚུན་འགལ་བ་སྟེ་འདུས་བྱས༌[^2453]པ་དང་འདུས་མ་བྱས་པ༌[^2454]ཉིད་ཀྱིས་དོན་གཙོ་བོ་བཀག་པའོ། །

[Block 3959]
རྒྱུ་མཚན་ནི་དེ་ལ་དམིགས་པའི་ཡོན་ཏན་གྱི་འབྲེལ་པའོ། །

[Block 3960]
གང་གི་དབང་གིས་སྐུ་གསུང་ཐུགས་ནི་བྱང་ཆུབ་ཀྱི་སེམས་ཞེས་གཞི་མཐུན་པས་དོན་གཉིས་ཀ་ཡང་བྱེད་པའི་ཚིག་དང་པོས་བརྗོད་དོ། །

[Block 3961]
དགོས་པ་ནི་བྱང་ཆུབ་ཀྱི་སེམས་བཞིན་དུ་སྐུ་གསུང་ཐུགས་ཀྱང་སྟོང་པ་དང་སྒྱུ་མའི༌[^2455]རང་བཞིན་དུ༌[^2456]ཡོངས་སུ་ཤེས་པར་བྱ་བ་ཡིན་པས་ཉེ་བར་གདགས་པ་ནི་རིགས་པ་ཁོ་ནའོ། །

[Block 3962]
བྱ་བའི་རྒྱུད་ལ་སོགས་པ་ལ་གནས་པ་རྣམས་ལ་མི་བསྟན་པས་ན་ཞེས་པ་ནི་རྣལ་འབྱོར་གྱི་རྒྱུད་ཀྱི་བར་དུ་རྣལ་འབྱོར་པ་རྣམས་ལ་སྦ་བར་བྱའོ། །

[Block 3963]
སྒྲིབ་པ་ཐམས་ཅད་ལས་རྣམ་པར་གྲོལ་བས་ན་ཞེས་པ་ལ། ཉོན་མོངས་པ་དང་ཤེས་བྱའི་སྒྲིབ་པ་ལ་སོགས་པ་བྲལ་བ་སྟེ། བྱང་ཆུབ་སེམས་ཀྱིས་རྣམ་པར་རྟོག་པ་ཐམས་ཅད་ཉེ་བར་ཞི་བར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3964]
ཡོངས་སུ་དག་པ་ལྷའི་སྐུ་བསྐྱེད་པའི་ཕྱིར་ཞེས་པ་ནི་ཡོངས་སུ་དག་པའི་སྒྲ་འདིར་ནི་རྣམ་པ་གཉིས་ཏེ། གཅིག་ནི་སྔགས་ཀྱི་སྐུ་རྗོད་པར་བྱེད་པ་ཡིན་ཏེ། ཐ་མལ་པའི་ལུས་ལ་སོགས་པའི་རྣམ་པར་རྟོག་པ་ཟློག་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3965]
གཉིས་པ་ནི་ཡེ་ཤེས་ཀྱི་སྐུ་རྗོད་པར་བྱེད་པ་སྟེ། སྒྱུ་མ་ལ་སོགས་པའི་དཔེས་ཉེ་བར་མཚོན་པའི་ཕྱིར་རོ། །

[Block 3966]
རྡོ་རྗེའི་སྐུ་ཡང་ཡོངས་སུ་དག་པའི་ལྷའི༌[^2457]སྐུར་བརྗོད་པ་ཡིན་ཏེ། མི་གནས་པའི་མྱ་ངན་ལས་འདས་པའི་དབྱིངས་ཀྱིས་རྣམ་པར་རྟོག་པའི་སྤྲོས་པ་ཐམས་ཅད་སྤངས་པའི་ཕྱིར་རོ། །

[Block 3967]
འདིར་ནི་ཐམས་ཅད་གཟུང་བར་བྱ་སྟེ། བྱང་ཆུབ་ཀྱི་སེམས་ནི་སྟོང་པ་ཉིད་ཀྱི་རང་བཞིན་ཡིན་པའི་ཕྱིར་དང་། རྫོགས་པའི་རིམ་པ་སྟོན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3968]
བྱང་ཆུབ་ཆེན་པོའི་སེམས་བརྟན་པར་མཛད་པ་ན་ཞེས་པ་ལ། བྱང་ཆུབ་ཀྱི་སེམས་ཆེན་པོ་ནི་སྟོང་པ་ཉིད་ཀྱི་དེ༌[^2458]ཁོ་ན་ཉིད་དང་རྫོགས་པའི་རིམ་པའི་དེ་ཁོ་ན་ཉིད་དོ། །

[Block 3969]
ཆེན་པོ་ཡང་ཡིན་ལ་བྱང་ཆུབ་ཀྱི་སེམས་ཀྱང་ཡིན་པས་ན་བྱང་ཆུབ་ཀྱི་སེམས་ཆེན་པོའོ། །

[Block 3970]
དེས་ནི་སེམས་ཅན་གྱི་དོན་ཆེན་པོར་འགྱུར་རོ་ཞེས་བྱ་བའོ་ཞེས་པ་ནི་སེམས་ཅན་ནི་ཙནྡན་ལྟ་བུ༌[^2459]ལ་སོགས་པའི་གང་ཟག་རྣམས་སོ། །

[Block 3971]
ཆེན་པོ་ནི་རིན་པོ་ཆེ་ལྟ་བུའི་གང་ཟག་རྣམས་སོ། །

[Block 3972]
དེ་རྣམས་ཀྱི་དོན་ནི་རང་གི་བསམ་པ་དང་མཐུན་པའི་རྣམ་པར་གྲོལ་བའི་མཚན་ཉིད་དོ། །

[Block 3973]
གང་གི་ཕྱིར་ཙནྡན་ལྟ་བུ་ལ་སོགས་པ་གང་ཡིན་པ་དེ་རྣམས་བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པ་དང་། སྟོང་པ་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་ལ་ལྷག་པར་མོས་པས་གྲོལ་བར་འགྱུར་རོ། །

[Block 3974]
རིན་པོ་ཆེ་ལྟ་བུའི་གང་ཡིན་པ་དེ་རྣམས་ཀྱང་རྫོགས་པའི་རིམ་པའི་དེ་ཁོ་ན་ཉིད་ཡིད་ལ་བྱེད་པས་གྲོལ་བར་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3975]
དེ་ལྟ་བུའི་སེམས་ཀྱི་ཡོངས་སུ་རྟོག་པ་ཐུགས་ཀྱིས་མཁྱེན་ནས་ཞེས་པ་ནི་སངས་རྒྱས་རྣམས་ནི་མངོན་པར་ཤེས་པ་དྲུག་དང་ལྡན་པའི་ཕྱིར་རོ། །

[Block 3976]
སྒྲ་ཇི་བཞིན་པ་ནི་རིམ་པ་གཉིས་མདོ་ཙམ་བསྟན་པས་སོ། །

[Block 3977]
ཁྱོད་ཀྱིས༌[^2460]ཞེས་བྱ་བ་ལ་སོགས་པ་ལ། སྐུ་གསུང་ཐུགས་ཀྱི་བདག་ཉིད་ཅན་སྔགས་ཀྱི་སྐུ་རྣམས་ཐ་མི་དད་པར་བསྟན་ཏོ། །

[Block 3978]
སྐུ་རྡོ་རྗེ་ལྟ་བུར་ནི༌[^2461]ཐུགས་ཀྱི༌[^2462]རྡོ་རྗེའི་ངོ་བོ་ཡང་ཡིན་ཏེ། སྐུ་རྟེན་མེད་པས་བརྟེན་པ་ཡང་སེམས་མི་གནས་པའི་ཕྱིར་རོ། །

[Block 3979]
ཐུགས་རྡོ་རྗེ་ལྟ་བུར་ཞེས་པ་ནི་སྐུ་རྡོ་རྗེའི་སྐུ་ཡང་ཐུགས་ཀྱི་རྡོ་རྗེ་འཛིན་པའི་སྐུའི་ངོ་བོ་ཡིན་ཏེ། སྐུ་ནི་སེམས་ཀྱི་སྣང་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3980]
ཚིག་ཏུ་བརྗོད་པ་ནི་ངག་ཏུ་སྨྲ་བ་སྟེ་ཞེས་པ་ལ། ཇི་སྲིད་ངག་གི༌[^2463]བརྗོད་པ་ནི་འཇིག་རྟེན་པའི་བརྡ་ལ་སོགས་པ་དང་འཇིག་རྟེན་ལས་འདས་པའི་ཁ་ཐོན་དང་ཀློག་པ་དང་། བཟླས་པ་ལ་སོགས་པ་གང་ཡིན་པ་དེ་རྣམས་གསུང་རྡོ་རྗེ་ལྟ་བུར་ཞེས་པ་ནི་གསུང་རྡོ་རྗེའི་སྐུའི་རང་བཞིན་གྱིས༌[^2464]ཐུགས་རྡོ་རྗེ་འཛིན་པའི་གཟུགས་ཁོ་ན་སྟེ་སེམས་ལས་ངག༌[^2465]བྱུང་བའི་ཕྱིར་རོ། །

[Block 3981]
དེ་ལྟར་ལྟེ་བའི་ཕྱོགས་ནས་འབྱུང་བའི་སྲོག་ཅེས་བྱ་བའི་རླུང་ཡིད་ཀྱིས་བསྐུལ་བའི་ཕྱི་རོལ་གྱི་དོན་གཟུང་བར་འདོད་པས་གནས་བརྒྱད་ཀུན་རེག་པས་ཡི་གེ་རྣམས་བསྐྱེད་པར་བྱ་སྟེ། ཡི་གེ་རྣམས་ཀྱིས་ཀྱང་ཚིག་དང་ཚིག་དེ་རྣམས་ཀྱིས་ཀྱང་ངག་ཆེན་པོ་འབྱུང་བར་འགྱུར་རོ། །

[Block 3982]
དེ་བས་ན་ངག་གི་སྤྲོས་པ་ཐམས་ཅད་འདི་སེམས་ཀྱི་རྩ་བ་ཅན་ཡིན་ནོ། །

[Block 3983]
ཇི་སྐད་དུ།

[Block 3984 [VERSE]]
ནམ་མཁའ་ལས་བྱུང༌[^2466]རླུང་ནི་ལུས་པོ་ལས། །
ཀུན་དུ་རྒྱུ་ཞིང་དབྱངས་ནི་ཁར་འབྱིན་པ། །
གནས་གཞན་རྣམས་ལ་རབ་ཏུ་དབྱེ་འགྱུར་བ། །
ཡི་གེ་ཉིད་དུ་གྱུར་པ་གང་དེ་སྒྲ། །

[Block 3985 [VERSE]]
ཡི་གེ་དེ་ནི་ཚངས་པ་དག་བྱེད་མཆོག །
གསང་བ་ལ་གནས་བྲམ་ཟེ་ཡང་དག་འདོད། །
དེ་ནི་ཡང་དག་རབ་ཏུ་སྦྱོར་བ་ན། །
ལེགས་ཐོབ་མངོན་པར་འབྱུང་བས་སྐྱེས་བུར་སྦྱར། །

[Block 3986]
ཞེས་བཤད་པའི་ཕྱིར་རོ། །

[Block 3987]
དེ་ལྟར་སྐུ་རྡོ་རྗེ་ལ་སོགས་པའི་རྣལ་འབྱོར་པ་རྣམས་ལ། སྐུ་ལ་སོགས་པའི་རྣམ་པ་གསུམ་གྱི་ཕན་ཚུན་དབྱེར་མེད་པ་ཉིད་བསྟན་ཏོ། །

[Block 3988]
སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཅེས་པ་ནི་བགེགས་བསྐྲད་པའི་དེ་ཁོ་ན་ཉིད༌[^2467]དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི་རིམ་པས་ཐོབ་པའི་སྟོང་པ་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་ཀྱིས་སོ། །

[Block 3989]
གཅིག་ཏུ་བྱས་ནས་ཞེས་པ་ནི་ངོ་བོ་ཉིད་མེད་པ་བསྒོམ་པར་བྱའོ། །

[Block 3990]
དགོངས་པ་ནི་འདི་ཡིན་ཏེ། བགེགས་བསྐྲད་པའི་བསྒོམ་པས་ཐུགས་རྡོ་རྗེ་འཆང་བསྒོམ་པ་དང་གཞལ་ཡས་ཁང་པའི་བསྒོམ་པས་སྐུ་རྡོ་རྗེ་འཆང་བསྒོམ་པ་དང་། ལྷག་པར་མོས་པའི་དཀྱིལ་འཁོར་གྱིས་གསུང་རྡོ་རྗེ་འཆང་གི་རང་བཞིན་གྱི༌[^2468]སྐུ་བསྒོམ་པའོ། །

[Block 3991]
སྐུ་གསུང་ཐུགས་ཀྱི་རྡོ་རྗེ་འཆང་གི་སྐུ་རྣམས་བསྒོམས་ནས་ཡང་རྡོ་རྗེ་ཕྲེང་བ་ལས་གསུངས་པའི་དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི་རིམ་པས་སྟོང་པ་ཉིད་དུ་གྱུར་པར་རྣམ་པར་བསམ་པར་བྱ་བ་དང་། ཨོཾ་ཤཱུ་ནྱ་ཏཱ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྔགས་ཀྱང་བརྗོད་དོ། །

[Block 3992]
དྲང་བའི་དོན་ནི་བསྐྱེད་པའི་རིམ་པའི་ཡན་ལག་ཏུ་གྱུར་པ་དང་པོ་སྦྱོར་བའི་ཏིང་ངེ་འཛིན་གྱི་ཕྱོགས་གཅིག་པའི་རྣལ་འབྱོར་ཞེས་བྱ་བའི་ཡན་ལག་དོན་དམ་པའི་དཀྱིལ་འཁོར་གྱི་རང་བཞིན་སྟོང་པ་ཉིད་ཀྱི་དེ་ཁོ་ན་ཉིད་རབ་ཏུ་བསྟན་པའི་ཕྱིར་རོ། །

[Block 3993]
རྫོགས་པའི་རིམ་པ་བསྟན་པའི་ཕྱིར་ཡིད་ཀྱི་རང་བཞིན་གྱི་ལུས་གཅིག་པ་ཞེས་བསྟན་ཏོ། །

[Block 3994]
སེམས་གསུམ་པོ་ཞེས་བྱ་བ༌[^2469]ལ། ཀུན་གཞི་ལ་སོགས་པ་རྣམ་པར་ཤེས་པ་གསུམ་པའོ། །

[Block 3995]
ཁམས་ཕྲ་བ་ནི་འོད་གསལ་བ་དང་ལྷན་ཅིག་ཏུའོ། །
--- END BLOCKS ---
