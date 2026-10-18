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
[Block 3991]
འདི་ལ་རྒྱུ་ཅི་ཞིག་ཡོད། རེ་ཞིག་སོ་སོ་ཡང་དག་པར་རིག་པ་ཐོབ་པའི་ཕྱིར་ཆོས་སྟོན་པར་མི་སྤྱོད་པ་ཡང་མ་ཡིན་ལ། དེ་དག་གིས་སྔོན་གྱི་སངས་རྒྱས་རྣམས་ཀྱི་བསྟན་པ་རྗེས་སུ་དྲན་ནས་ཡང་ཆོས་སྟོན་པར་སྤྱོད་དོ། །

[Block 3992]
ཐུགས་རྗེ་མེད་པར༌[^2254]ཡང་མ་ཡིན་ཏེ། སེམས་ཅན་ཐམས་ཅད་ལ་ཕན་གདགས་པའི་དོན་དུ་རྫུ་འཕྲུལ་སྟོན་པའི་ཕྱིར་རོ། །

[Block 3993]
སེམས་ཅན་རྣམས་སྐལ་བ་དང་མི་ལྡན་པའི་ཕྱིར་ཡང་མ་ཡིན་ཏེ། འདི་ལྟར་འཇིག་རྟེན་པའི་ལམ་གྱིས་འདོད་ཆགས་དང་བྲལ་བ་དག་ཀྱང་ཡོད་དོ། །

[Block 3994]
འོ་ན་ཇི་ལྟ་ཞེ་ན། སྔོན་གོམས་པའི་དབང་གིས་བསོད་སྙོམས༌[^2255]ལ་མོས་པའི་ཕྱིར་སེམས་ཅན་རྣམས་ཆོས་ཟབ་མོ་འཛིན་དུ་འཇུག་པའི་དོན་དུ་བྱེད་པར་མི་སྤྲོ་སྟེ། སྐྱེ་དགུ་རྒྱུན་ཕྱོགས་སུ་འགྲོ་བ་རྣམས་ནི་རྒྱུན་ཕྱོགས་ལས་བཟློག་པར་བཀྲི་བར་དཀའོ། །

[Block 3995]
རྣམ་པར་གཡེང་བ་དང་འདུ་འཛིས་སྐྲག་པས་འཁོར་ཡོངས་སུ་གཟུང་བར༌[^2256]འགྱུར་བ་སྤང་བའི༌[^2257]ཕྱིར་རོ། །

[Block 3996 [HEADING]]
##### འཁོར་ལོས་སྒྱུར་བ། ^3-2-5-8-0

[Block 3997]
འཁོར་ལོས་སྒྱུར་བ་རྣམས་ནམ་འབྱུང་ཞེ་ན།

[Block 3998 [VERSE]]
འཁོར་ལོས་སྒྱུར་བ་འབྱུང་བ་ནི། །
སྟོང་ཕྲག་བརྒྱད་ཅུ་ལས་མི༌[^2258]འཕྱི། །

[Block 3999]
མི་རྣམས་ཀྱི་ཚེ་དཔག་ཏུ་མེད་པ་ནས་བརྒྱད་ཁྲིའི་བར་དུ་འཁོར་ལོས་སྒྱུར་བ་རྣམས་འབྱུང་ངོ་། །འོག་ཏུ་ནི་མ་ཡིན་ཏེ། དེ་བས་ཐུང་བའི་ཚེ་ནི་ཕུན་སུམ་ཚོགས་པ་དེའི་སྣོད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 4000]
དེ་དག་ནི་རྒྱལ་སྲིད་འཁོར་ལོས་སྒྱུར་བའི་ངང་ཚུལ་ཅན་ཡིན་པས་འཁོར་ལོས་སྒྱུར་བ་རྣམས་སོ། །

[Block 4001]
དེ་དག་ཀྱང་རྣམ་པ་བཞི་སྟེ། གསེར་དངུལ་ཟངས་ལྕགས་འཁོར་ལོ་ཅན། །གང་དག་ལ་གསེར་དང་། དངུལ་དང་། ཟངས་དང་། ལྕགས་ཀྱི་འཁོར་ལོ་དག་ཡོད་པ་སྟེ། དེ་དག་གི་དང་པོ་ནི་མཆོག་ཡིན་ནོ། །

[Block 4002]
གཉིས་པ་ནི་ཉེ་བའི་མཆོག་ཡིན་ནོ། །

[Block 4003]
གསུམ་པ་ནི་འབྲིང་ཡིན་ནོ།[^2259] །

[Block 4004]
བཞི་པ་ནི་ཐ་མའོ། །

[Block 4005 [VERSE]]
དེ་དག་གླིང་གཅིག་གླིང་གཉིས་དང་། །
གསུམ་དང་བཞི་ལ་མས་རིམ་བཞིན། །

[Block 4006]
གང་ལ་ལྕགས་ཀྱི་འཁོར་ལོ་ཡོད་པ་དེ་ནི་གླིང་གཅིག་གི་བདག་པོ་ཡིན་ནོ། །

[Block 4007]
གང་ལ་ཟངས་ཀྱི་ཡོད་པ་དེ་ནི་གཉིས་ཀྱིའོ། །

[Block 4008]
གང་ལ་དངུལ་གྱི་ཡོད་པ་དེ་ནི་གསུམ་གྱིའོ། །

[Block 4009]
གང་ལ་གསེར་གྱི་ཡོད་པ་དེ་ནི་གླིང་བཞི་ལ་དབང་བ་ཡིན་ཏེ། འདི་ནི་བཏགས་པ་ལས་བསྟན་པ་ཡིན་ནོ། །

[Block 4010]
མདོ་ལས༌[^2260]ནི་གཙོ་བོ་སྨོས་པའི་ཕྱིར་རྒྱལ་པོ་རྒྱལ་རིགས་སྤྱི་བོ་ནས་དབང་བསྐུར་བ་གང་ཞིག་ཚེས་བཅོ་ལྔ་ལ་གསོ་སྦྱོང་གི་དུས་དེ་ཁོ་ནར་མགོ་བཀྲུས་གསོ་སྦྱོང་བསྟེན་ནས་ཁང་བཟངས་ཀྱི་ཐོག་ཏུ་བློན་པོའི་ཚོགས་ཀྱིས་ཡོངས་སུ་བསྐོར་བ་ལ་ཤར་ཕྱོགས་ནས་འཁོར་ལོ་རིན་པོ་ཆེ་རྩིབས་སྟོང་པ། ལྟེ་བ་དང་བཅས་པ། མུ་ཁྱུད་དང་བཅས་པ། རྣམ་པ་ཐམས་ཅད་དུ་ཡོངས་སུ་རྫོགས་པ། མཛེས་པ། མཁན་བཟོས་མ་བྱས་པ། ལྷ་རྫས་ཐམས་ཅད་གསེར་གྱི་རང་བཞིན་འབྱུང་བར་འགྱུར་བ་དེ་ནི་འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་ཡིན་ནོ་ཞེས་གསེར་གྱི་འཁོར་ལོ་གཅིག་ཁོ་ནར༌[^2261]གསུངས་སོ། །

[Block 4011]
འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་དེ་དག་ནི་འདི་ལྟར་འབྱུང་སྟེ། ལྷན་ཅིག་གཉིས་མིན་སངས་རྒྱས་བཞིན། །མདོ་ལས་གང་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་གཉིས་སྔ་ཕྱི་མེད་པར་འཇིག་རྟེན་དུ་འབྱུང་བ་ནི་གནས་མ་ཡིན་ཞིང་གོ་སྐབས་མེད་དེ། འདི་ནི་གནས་མེད་ཀྱི། གཅིག་གང་ཡིན་པ་དེ་ནི་གནས་ཡོད་དོ། །

[Block 4012]
དེ་བཞིན་གཤེགས་པ་དག་ཇི་ལྟ་བར་འཁོར་ལོས་སྒྱུར་བ་དག་ཀྱང་དེ་བཞིན་ནོ་ཞེས་གསུངས་སོ། །

[Block 4013]
འདིར་ནི༌[^2262]འདི་དཔྱད་པར་བྱ་སྟེ། ཅི་འདིར་སྟོང་གསུམ་གྱི་འཇིག་རྟེན་གྱི་ཁམས་ལ་འཇིག་རྟེན་དུ་འདོད་དམ། འོན་ཏེ་འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་ཡིན་ཞེ་ན། ཁ་ཅིག་ན་རེ་གཞན་དུ་སངས་རྒྱས་དག་མི་འབྱུང་ངོ་། །ཅིའི་ཕྱིར་ཞེ་ན། བཅོམ་ལྡན་འདས་ཀྱི་མཐུ་ཐོགས་པ་ཡོད་པར་འགྱུར་དུ་འོང་ངོ་། །

[Block 4014]
བཅོམ་ལྡན་འདས་གཅིག་ཁོ་ནས་ཐམས་ཅད་དུ་ཡང༌[^2263]སྤྱོད་དོ། །

[Block 4015]
གང་དུ་བཅོམ་ལྡན་འདས་གཅིག་གིས་གདུལ་བྱ་རྣམས་གདུལ་བར་མི་སྤྱོད་པ་དེ་ནི་གཞན་གྱིས་ཀྱང་མི་སྤྱོད་དོ། །

[Block 4016]
མདོ་ལས་ཀྱང་། ཤཱ་རིའི་བུ་གལ་ཏེ་ལ་ལ་ཞིག་ཁྱོད་ཀྱི་ཐད་དུ་འོངས་ནས་འདི་སྐད་དུ། ད་ལྟར་དགེ་སློང་ངམ། བྲམ་ཟེ་གང་ཡང་རུང་། དགེ་སྦྱོང་གཽ་ཏ་མ་དང་འདི་ལྟ་སྟེ། མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་བྱ་བ་ལ་མཉམ་ཞིང་མཉམ་པ་འགའ་ཞིག་ཡོད་དམ་ཞེས་འདྲི་བར་འགྱུར་ན། དེ་སྐད་དུ་དྲིས་ན་ཇི་སྐད་དུ་ལན་གདབ། བཙུན་པ་གལ་ཏེ་ལ་ལ་ཞིག་བདག་གི་ཐད་དུ་མཆིས་ནས་འདི་སྐད༌[^2264]དུ་འདྲི་བར་འགྱུར་ན། དེ་ལ་བདག་གིས་འདི་སྐད་ཅེས་ད་ལྟར་དགེ་སློང་ངམ། བྲམ་ཟེ་ཡང་རུང་། བཅོམ་ལྡན་འདས་དང་མཉམ་ཞིང་མཉམ་པ་ནི་འགའ་ཡང་མེད་དོ་ཞེས་དྲིས་པའི་ལན་གདབ་པར་བགྱིའོ། །

[Block 4017]
བཙུན་པ་དེ༌[^2265]ཅིའི་སླད་དུ་ཞེ་ན། གང་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་གཉིས་སྔ་ཕྱི་མེད་པར་འཇིག་རྟེན་དུ་འབྱུང་བ་ནི་གནས་མ་ཡིན་ཞིང་གོ་སྐབས་མེད་དེ། འདི་ནི་གནས་མེད་དོ་ཞེས་བཅོམ་ལྡན་འདས་ལས་ཐོས་ཤིང་མངོན་སུམ་དུ་བཟུང་བའི་སླད་དུའོ་ཞེས་གསུངས་སོ་ཞེས་ཟེར་རོ། །

[Block 4018]
འོ་ན་གང་བཅོམ་ལྡན་འདས་ཀྱིས་ཚངས་པའི་མདོ་ལས།

[Block 4019]
ང་ནི་སྟོང་གསུམ་གྱི༌[^2266]འཇིག་རྟེན་གྱི་ཁམས་ཀྱི་བར་འདི་ལ་དབང་བསྒྱུར༌[^2267]རོ་ཞེས་གང་གསུངས་པ་ཇི་ལྟར་དྲང་ཞེ་ན། བསྟན་པ་འདི་ནི༌[^2268]དགོངས་པ་ཅན་ཡིན་ནོ། །

[Block 4020]
འདི་ལ་དགོངས་པ་གང་ཡིན་ཞེ་ན། མངོན་པར་འདུ་མཛད་པ་མི་མངའ་བར་དེ་སྲིད་དུ་རྣམ་པར་གཟིགས་པའི་ཕྱིར་རོ། །

[Block 4021]
མངོན་པར་འདུ་མཛད་ན་ནི་སངས་རྒྱས་རྣམས་ཀྱི་སྤྱན་གྱི་ཡུལ་མཐའ་ཡས་པ་ཡིན་ནོ། །

[Block 4022]
སྡེ་པ་གཞན་དག་ན་རེ་འཇིག་རྟེན་གྱི་ཁམས་གཞན་དག་ན་ཡང་སངས་རྒྱས་རྣམས་བཞུགས་སོ། །ཅིའི་ཕྱིར་ཞེ་ན། མང་པོ་ཞིག་མཉམ་དུ་ཚོགས་དག་ལ་ཞུགས་པར༌[^2269]སྣང་ལ། གཅིག་ཏུ་སངས་རྒྱས་མང་པོ་ཞིག་ཅིག་ཅར་འབྱུང་བར་ཡང་མི་རུང་ལ། འབྱུང་བ་ལ་བགེགས་བྱེད༌[^2270]པ་འགའ་ཡང་མེད་པས་གདོན་མི་ཟ་བར་འཇིག་རྟེན་གཞན་དག་ཏུ་འབྱུང་ངོ་། །འཇིག་རྟེན་གྱི་ཁམས་དག་ཀྱང་མཐའ་ཡས་པས་བཅོམ་ལྡན་འདས་ཀྱི་སྐུ་ཚེ་བསྐལ་པར་བཞུགས་ཀྱང་། འདིར་ཇི་ལྟ་བར་མཐའ་ཡས་པ་གཞན་དག་ཏུ་མཛད་པར་མི་སྤྱོད་ན་མིའི་ཚེས་ལྟ་སྨོས་ཀྱང་ཅི་དགོས། འདིར་བཅོམ་ལྡན་འདས་ཇི་ལྟར་མཛད་ཅེ་ན། གང་ཟག་འདིའི་དབང་པོ་འདི་ནི་དུས་འདི་སྲིད་ཀྱིས༌[^2271]ཡུལ་ཆེ་གེ་མོ་ཞིག་ཏུ་གང༌[^2272]འདི་ལ་བརྟེན་ནས་ཉེས་པ་འདི་ཡོངས་སུ་སྤངས་ཤིང་ཡན་ལག་འདི་ཉེ་བར་བསྒྲུབས་པའི་ཕྱིར་སྦྱོར་བ་འདིས་ནམ་སྐྱེས་པ་ནི་སྐྱེ་བར་འགྱུར་རོ། །

[Block 4023]
མ་རྫོགས་པ་ནི་ཡོངས་སུ་རྫོགས་པར་འགྱུར་རོ་ཞེས་བྱ་བར་མཁྱེན་པ་ལྟ་བུ་ཡིན་ནོ། །

[Block 4024]
འདི་ལ་ཁུངས་སུ་གང་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་གཉིས་སྔ་ཕྱི་མེད་པར་འཇིག་རྟེན་དུ་འབྱུང་བར་འགྱུར་བ་ནི་གནས་མ་ཡིན་ཞིང་གོ་སྐབས་མེད་དོ་ཞེས་བྱ་བའི་མདོ་འདི་ཕྱུང་བ་གང་ཡིན་པ་དེ་ཉིད་ཀྱང་འཇིག་རྟེན་གྱི་ཁམས་གཅིག་གི་དབང་དུ་མཛད་ནས་གསུངས་པ་ཞིག་གམ། འོན་ཏེ་ཐམས་ཅད་ཀྱི་དབང་དུ་མཛད་ནས་གསུངས་པ་ཞིག་ཅེས་དཔྱད་པར་བྱའོ། །

[Block 4025]
འཁོར་ལོས་སྒྱུར་བ་རྣམས་ཀྱང་འཇིག་རྟེན་གྱི་ཁམས་གཞན་དུ་ཡང༌[^2273]འབྱུང་བར་མི་འགྱུར་ཏེ། ལྷན་ཅིག་འབྱུང་བ་བཀག་པའི་ཕྱིར་སངས་རྒྱས་བཞིན་ནོ། །

[Block 4026]
འོན་ཏེ༌[^2274]བཟོད་ན་ནི་སངས་རྒྱས་རྣམས་འཇིག་རྟེན་དུ་འབྱུང་བ་ནི་བསོད་ནམས་ཀྱི་གཞི་ཡིན་པས་འདི་ཡང་ཅིའི་ཕྱིར་མི་བཟོད་དེ། གལ་ཏེ་མང་པོ༌[^2275]ཞིག་ཏུ་ཕལ་པོ་ཆེ་ཞིག་འབྱུང་བར༌[^2276]གྱུར་ན་ཡང་སྐྱོན་དུ་མི་འགྱུར་གྱི་འཇིག་རྟེན་ཕལ་ཆེར་མངོན་པར་མཐོ་བ་དང་ངེས་པར་ལེགས་པ་དང་ལྡན་པར་འགྱུར་རོ། །

[Block 4027]
འོན་ཏེ་གཅིག་ཏུ་ཡང་དེ་བཞིན་གཤེགས་པ་གཉིས་ཅིའི་ཕྱིར་འབྱུང་བར་མི་འགྱུར་ཞེ་ན། དགོས་པ་མེད་པའི་ཕྱིར་དང་། སྨོན་ལམ་གྱི་དབང་གིས་ཏེ། བྱང་ཆུབ་སེམས་དཔའ་རྣམས་ནི་འདི་སྐད་དུ་ཀྱེ་མ་བདག་ནི་འདྲེན་པ་མེད་པ་ལྡོངས་པའི་འཇིག་རྟེན་དུ་མགོན་མེད་པ་རྣམས་ཀྱི་མགོན་དུ་སངས་རྒྱས་སུ་འབྱུང་བར་གྱུར་ཅིག་ཅེས་སྨོན་ལམ་འདེབས་པར་བྱེད་དོ། །

[Block 4028]
གུས་པ་དང་རིངས་པར་བྱ་བའི་ཡང་ཕྱིར་རོ་ཞེས་ཟེར་རོ། །

[Block 4029]
[^2277]སངས་རྒྱས་གཅིག་ལ་ནི་ཤིན་ཏུ་ཡང་གུས་པར་འགྱུར་ལ། འདི་ལྟ་བུ་གཞན་ལ༌[^2278]ནི་རྙེད་པར་དཀའོ་སྙམ་དུ་སེམས་པ་ནི་འདི་གཤེགས་སམ་ཡོངས་སུ་མྱ་ངན་ལས་འདས་ན་མགོན་མེད་པར་འགྱུར་དུ་འོང་ངོ་ཞེས་བསྟན་པ་བསྒྲུབ་པ༌[^2279]ལ་ཤིན་ཏུ་རིངས་པར་ཡང་བྱེད་དོ། །

[Block 4030]
ཡང་འཁོར་ལོས་སྒྱུར་བའི་རྒྱལ་པོ་དེ་དག་གསེར་ལ་སོགས་པའི་འཁོར་ལོ་དག་གིས་ས་ལས་རྒྱལ་བར་བྱེད་པ་ན་ཇི་ལྟར་རྒྱལ་བར་བྱེད་ཅེ་ན། གོ་རིམས་བཞིན་དུ། ཕས་བསུ་རང་འགྲོ་གཡུལ་བཤམས་དང་། །མཚོན་བརྩམས་པས་རྒྱལ། གང་ལ་གསེར་གྱི་འཁོར་ལོ་ཡོད་པ་དེ་ལ་ནི་ཁམས་ཀྱི་རྒྱལ་ཕྲན་རྣམས་འབྱོར་པ་དང་། རྒྱས་པ་དང་། བདེ་བ་དང་། [^2280]གང་ལོ་ལེགས་པ་དང་། སྐྱེ་བོ་དང་། མི་ཕལ་པོ་ཆེས་བལྟམས༌[^2281]པའི་ལྗོངས་འདི་དག་ནི་ལྷའི་ལགས་ཀྱི་ལྷས་དེ་དག་རྗེས་སུ་བསྟན་དུ་གསོལ། བདག་ཅག་ནི་ལྷའི་ཞམ་འབྲིང་འཚལ་ལོ་ཞེས་ཕས་བསུ་བར་བྱེད་དོ། །
--- END BLOCKS ---
