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
[Block 3956 [VERSE]]
རྒྱལ་པོ་ཆེན་པོ་ཉམས་ཉེས༌[^2556]པ། །
བོར་ཏེ་མཆི་བའི༌[^2557]ཆོས་མ་མཆིས། །

[Block 3957]
ཞེས་བྱ་བ་ནི་ངོ་ཚ་ཤེས་པའི་དབང་དུ་བྱས་པ་སྟེ། བདག་དང་ཆོས་ཀྱི་དབང་དུ་བྱས་ནས་ཁ་ན་མ་ཐོ་བ་ལ་འཛེམ༌[^2558]ཞེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 3958]
བདེ་བའི་ཚེ་ན་རྟག་ཏུ་ཁྱོད་བཀུར་ལ། །ཉམས་ཉེས༌[^2559]ཚེ་ན་ཞེས་བྱ་བ་སྟེ། ཕོངས་པར་གྱུར་བ་ནི༌[^2560]བདག་གིས་བོར་ན་ག་ལ་ཞིག་རུང་སྟེ། སྨྲས་པ། ཁྱོད་ནི་ཅིར་གྱུར་པ་ཞེས་བྱ་བ་ཡིན་ཏེ།

[Block 3959]
དང་པོ་ཁྱོད་ཇི་ལྟར་གྱུར་པ་དེ་ལྟར་བདག་ཉིད་ཀྱང་འགྱུར་བར་འཚལ་ལོ་ཞེས་བྱ་བའོ། །

[Block 3960]
དེའི་ལན་བྱང་ཆུབ་སེམས་དཔས་སྨྲས་པ། ཚང་མང་ཞེས་བྱ་བས་ནི་ངེས་པར་གསོད་པར་འགྱུར་བའི་དོན་ཏོ། །

[Block 3961]
བདེ་བར་གནས་ཞེས་བྱ་བས་ནི་སེམས་བདེ་བར་གནས་པའོ། །

[Block 3962]
གལ་ཏེ་སེམས་བདེ་བར་མི་གནས་ཀྱང་གཟུང་བ་ཡིན་ན་ནི། དེར་འགྲོ་བའི་རིགས་ན་གཟུང་བ་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 3963]
དེ་ལྟ་མོད་ཀྱི་གལ་ཏེ་མ་བཟུང་ཞིང་བདེ་བར་གནས་ཀྱང་བདག་གི་འགྲོ་བའི་རྗེས་སུ་འགྲོ་བ་ནི་དོན་གཞན་དག་ལས་ལྟོས་པ༌[^2561]ཡིན་ན་གང་ན༌[^2562]ཡང་མེད་དོ་ཞེས་བསྟན་པའི་ཕྱིར། དེ་ལྟར་བྱས་ན་ཅིར་འགྱུར་ལྟོས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3964]
འདིའི་འགྲོ་བ་ནི་བདག་དང་། ཁྱོད་འཆི་བ་དང་། གཉེན་བཤེས་རྣམས་དང་འདི་གསུམ་གྱི་དོན་མེད་པར་ཚིགས་བཅད་འདིས་བསྟན་པ་ཡིན་ནོ། །

[Block 3965]
གསུམ་པོ་འདི་མེད་པས་འཆི་བ་དམིགས་པ་ཉིད་དུ་བསྟན་པའི་ཕྱིར། བདེ་དང༌[^2563]མི་བདེ་མུན་ཁུང་བཞིན། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3966]
ཕན་པའི་དོན་ཞེས་བྱ་བ་ནི་སྔར་བཤད་པ་གསུམ་པོའི་འོ། །

[Block 3967]
ཆོས་དོན་ལེགས་པར་བགྱིས་ན་ནི། །ཞེས་བྱ་བའི་ཕྱེད་འོག་མས་ནི་ཆོས་དང་། དོན་གཉིས་བདག་གི་འདོད་པས་ངེས་པར་བསྒྲུབས་པ་སྟེ། བདག་ཉིད་ཀྱི་དོན་ཉིད་དུ་ཞེས༌[^2564]བསྟན་ཏོ། །

[Block 3968]
རྗེ་བོ་ཡོངས་སུ་མ་བཏང་བར་སྤྱོད་ཅིང་། ཁྱོད་ལ་གློ་བ་ཉེ་བའི་ཕྱིར། །ཞེས་བྱ་བ་འདིས་ནི། རྗེ་བོའི་དོན་དུ་བདག་ཉིད་སྙིང་ཉེ་བར་སྟོན་ཏེ། དེས་ནི་གཉི་ག་ཡང་བསྟན་པ་ཡིན་ནོ། །

[Block 3969]
དེ་ལྟར་བྱས་ན་ཞེས་བྱ་བའི་ཚིགས༌[^2565]བཅད་འདི་སྨོས་པ་ལ་འཚོ་བར་གྱུར་ན་ནི་དོན་གཞན་འདི་དག་ཡོད་དོ༌[^2566]ཞེས་བསྟན་པ་སྟེ། དོན་གཞན་དེ་ཡོངས་སུ་བསྟན་པའི་ཕྱིར། མཛའ་བཤེས་ང་དང་ཕྲལ་བ་རྣམས། །ཞེས་བྱ་བ་སྨོས་ཏེ། བདག་གིས་བསྲུང་ཞིང་སྦ་བར་བྱ་བ་དེ་བྲལ་བར་གྱུར་ཀྱང་ཁྱོད་ཀྱིས་མཆོག་ཏུ་འབྱོར་པར་བྱེད་པར་འགྱུར་ཏེ། ཇི་ལྟ་བ་བཞིན་དུ་གསོལ་བ་གདབ་ཀྱང་མི་དགོས་པར་བློ་གྲོས་ཕུན་སུམ་ཚོགས་པའི་ཕྱིར་རོ། །

[Block 3970]
དེ་གཉིས་གཅིག་ལ་གཅིག་བྱམས་པ་ཉིད་ཡོན་ཏན་ཡིན་པས་དེ་བས་ན་གཅིག་ལ་གཅིག་བྱམས་པའི་ཡོན་ཏན་ནོ། །

[Block 3971]
དེ་གཟུགས་བཟང་བ་ཡིན་པས། དེའི་གཟུགས་བཟང་བ་སྟེ། དེའི་གཟུགས་བཟང་བ་དེས་སོ། །

[Block 3972]
བདེ་བར་འདུག་བཞིན་དུ་ཞེས་བྱ་བ་ནི་བག་ཚ་བ་མེད་པར་རོ། །

[Block 3973]
ཁྱོད་ནི་མ་ཟིན་བདེ་བར་འདུག །ཅེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་བསྡུས་པའི་དོན་ནི་རྒྱུ་རྣམ་པ་ལྔས་བྱ༌[^2567]རྣམས་ནམ་མཁའ་ལ་འགྲོ་བར་མི་ནུས་པ་ཡིན་ཏེ། དེ་མེད་ཀྱང་ཅིའི་ཕྱིར་ནམ་མཁའ་ལ་མི་འགྲོ་ཞེས་བྱ་བར་སྟོན་པ་ཡིན་ནོ། །

[Block 3974]
དེ་དག་ཀྱང་གང་ཞེ་ན། རྙིས་ཟིན་པ་དང་། རང་གི་དབང་མེད་པས་མི་བདེ་བར་འདུག་པ་དང་། སྤུ་མ་སྐྱེས་ཤིང་གཤོག་པ་མེད་པ་དང་། རྩོལ་བ་ཡོད་ཀྱང་སྟོབས་ཆུང་བ་དང་། འཇིགས་པའི་རྒྱུ་མ་མཐོང་བས་འགྲོ་བར་མི་འགྱུར་བ་སྟེ། ཉེས་པ་འདི་དག་མེད་ཀྱང་འཕུར་བར་མ་གྱུར་པའི་རྒྱུ་འདྲི་བ་ཡིན་ནོ། །

[Block 3975]
ཚིག་དང་། འབྲུ་དང་། སྦྲེལ་ལེགས་པ་ནི་ཚིག་འབྲུ་སྦྲེལ་ལེགས་པའོ། །

[Block 3976]
ཚིག་འབྲུ་སྦྲེལ་ལེགས་པའི་སྒྲ་གང་ཡིན་པ་དེ་ནི་ཚིག་འབྲུ་རབ་ཏུ་གསལ་ཞིང་སྦྲེལ་ལེགས་པའོ། །

[Block 3977]
དེ་ལ་འབྲུ་སྨོས་པས་ནི་ཨ་ལ་སོགས་པའི་ཡི་གེ་གཟུང་ངོ་། །ཚིག་སྨོས་པས་ནི་ངོ་བོ་ཉིད་ཀྱི་ཚིག་བླ་དགས་སུ་གཟུང་ངོ་། །ཚིག་སྦྲེལ་ལེགས་པ་ཞེས་བྱ་བ་སྨོས་པས་ནི་ཁྱད་པར་གྱི་ཚིགས༌[^2568]བླ་དགས་སུ་གཟུང་ངོ་། །ཡིད་དུ་འོང་བ་ཞེས་བྱ་བ་ནི་མཉན་པར་འོས་པའོ། །

[Block 3978]
གང་གི༌[^2569]གཟི་བྱིན་གང་ལ་ཡོད་པ་ནི་གཟི་བྱིན་དང་ལྡན་པའོ། །

[Block 3979]
བརྟན་པའི་ཡོན་ཏན་གྱིས་གཟི་བྱིན་དང་ལྡན་པ་ནི་བརྟན་པའི་ཡོན་ཏན་གྱིས་གཟི་བྱིན་དང་ལྡན་པ་སྟེ། དེས་སྒྲ་སྒྲོགས་ཤིང་སྐད་ཆེར་ཕྱུང་བ་ཡིན་ནོ། །

[Block 3980]
དམ་དུ་ཟིན་ཞེས་བྱ་བ་ནི་ཕྱི་རོལ་གྱི་རྙི་ནི་མཚོན་ལ་སོགས་པས་གཅད་པར༌[^2570]ནུས་ལ། བརྩེ་བའི་ཞགས་པ་ནི་གཅད་པར་མི་ནུས་པའི་ཕྱིར་ཏེ། ཇི་ལྟ་བུ་ཞེ་ན། སྨྲས་པ། རྙིས་ནི་དེ་བས་ཞེས་བྱ་བ་ཡིན་ཏེ། ལུས་ཀྱི་འཆིང་བ་དང་། རྗེས་སུ་མཐུན་པའི་བརྩེ་བའི༌[^2571]ཞགས་པ་གང་ཡིན་པ་དེས་བཅིངས་པ་སྟེ། [^2572]འདོད་ཆགས་དང་བྲལ་བ་མ་གཏོགས་པས་གཅོད་པར་མི་ནུས་པའི་ཕྱིར་རོ། །

[Block 3981]
ང་ཡི་རྒྱལ་པོ་སྲོག་དང་འདྲ་བའི་གྲོགས། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་བསྡུས་པའི་དོན་ནི་གང་ཡོངས་སུ་མི་འདོར་བ་དང་། ཅིའི་ཕྱིར་ཡོངས་སུ་མི་འདོར་བ་སྟེ། དེ་གཉིས་ཚིགས་བཅད་འདིས་སྟོན་པ་ཡིན་ནོ། །

[Block 3982]
གང་ཡོངས་སུ་མི་འདོར་ཞེ་ན། རྗེ་བོའོ། །ཅིའི་ཕྱིར་ཡོངས་སུ་མི་འདོར་ཞེ་ན། བདེ་བར་སྦྱིན་པར་བྱེད་པའི་ཕྱིར་རོ། །

[Block 3983]
གྲོགས་པོ་ཅིའི་ཕྱིར་ཡོངས་སུ་མི་འདོར་ཞེ་ན། ཉམས་ཉེས༌[^2573]པར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3984]
འདི་གཉིས་ཀྱིས་ནི་ཕན་འདོགས་པ་དང་། སྙིང་རྗེའི་ཞིང་ཉིད་དུ་སྟོན་ཏེ། ཡོན་ཏན་རེ་རེ་ལས་རེ་རེ་ཙམ་ཡོད་ཀྱང༌[^2574]ཡོངས་སུ་གཏང་བར་བྱ་བ་མ་ཡིན་ན། ཡོན་ཏན་བཞི་དང་ལྡན་པ་ལྟ་སྨོས་ཀྱང་ཅི་དགོས་ཞེས་སྟོན་ཏོ། །

[Block 3985]
བཟང་པོ་བདག་ཅག་སྨྲས་པ་འདིས་ཞེས་བྱ་བ་ལ། གལ་ཏེ་བདེ་བ་ཞེས་བྱ་བའི་སྒྲ་ནི་དགེ༌[^2575]ཤིས་སོ། །

[Block 3986]
བདག་ཅག་བཏང་ན་ནི་ཞེས་བྱ་བ་ཡང་འདིར་དགེ་ཤིས་སོ། །

[Block 3987]
སྔར་བཤད་པའི་སྨྲས་པ་འདིས། གལ་ཏེ་བདེ་བ་འབྱུང་འགྱུར༌[^2576]ཞིང་། །ཞེས་བྱ་བའི་ལན་ནི། ང་ནི་ཁྱོད་ལ་གནོད་མི་བྱེད། །ཅེས་བྱ་བ་ཡིན་ནོ། །

[Block 3988]
བཏང་ན་ནི་ཞེས་བྱ་བ་དེའི་ལན་ནི། ཁྱོད་ནི་ང་ཡིས་གཟུང་བ་མེད། །ཅེས་བྱ་བ་ཡིན་ནོ། །

[Block 3989]
ཆོས་དང་ལྡན་པའི་གྲགས་པ་འཐོབ། །ཅེས་བྱ་བའི་ལན་ནི། དེ་བས་ཁྱོད་ནི་ཅི་བདེར་སོང་། །ཞེས་བྱ་བའི་ཚིགས་བཅད་ཕྱེད་འོག་མ་ཡིན་ནོ། །

[Block 3990 [VERSE]]
ང་ནི་ཁྱོད་ལ་གནོད་མི་བྱེད། །
ཅེས་བྱ་བ་དེའི་ལན་ནོ། །
[^2577]བདག་ནི་སྡུག་བསྔལ་མི་བཞེད༌[^2578]ན། །

[Block 3991]
ཞེས་བྱ་བའི་ཚིགས་བཅད་ཀྱི་ཕྱེད་དོ། །

[Block 3992]
དེ་བས་ཁྱོད་ནི་ཅི་བདེར་སོང་། །ཞེས་བྱ་བའི་ལན་ནི།

[Block 3993 [VERSE]]
གལ་ཏེ་གཅིག་གིས་མཉེས་གྱུར་ན། །
ཞེས་བྱ་བ་ཕྱེད་འོག་མ་ཡིན་ནོ། །
གལ་ཏེ་གཅིག་གིས་མཉེས་གྱུར་ན། །

[Block 3994]
ཞེས་བྱ་བ་ལ། འདི་བློ་དང་ན་ཚོད་ལ་སོགས་པ་མི་མཉམ་པ་དེ་ཁྱད་པར་ཡོད་དོ་ཞེས་རྟོག་པ་ལ། དེ་ཁྱད་པར་མེད་པར་བསྟན་པའི་ཕྱིར། བདག་ཅག་ཆུ་དང་ཞེང་ཡང་མཉམ། །ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3995]
ཆུ་དང་ཞེང་རྣམ་པ་གཉིས་ཀྱིས་ནི་བྱེ་བྲག་མེད་པ་སྟོན་ཏེ། [^2579]དེ་ཁྱད་པར་མེད་པས་སེམས་ཀྱང་ཁྱད་པར་མེད་དོ། །
--- END BLOCKS ---
