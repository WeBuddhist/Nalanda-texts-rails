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
[Block 3921]
ཡུ་བ་ལ་གཞར་དུ་མི་རུང་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འདིར་དྲི་མ་བཀྲུ་བར་བྱ་བའི་ཕྱིར་ཡུ་བ་ལ་བྱི་དོར་བྱ་བར་རིག་པར་བྱ་སྟེ། །འདིར་དེ་ལྟར་བརྗོད་པར་བྱའོ། །

[Block 3922]
ཆད་ན་ཁྱིམ་དག་ཏུ་གཞག་གོ་ཞེས་བྱ་བ་ནི་ཆར་པ་ཆད་ན་དེའི་དྲུང་དུ་འདུག་པའི༌[^4041]ཁྱིམ་གང་ཡིན་པ་དེར་གདུགས་དེ༌[^4042]བཏགས་ཏེ་གཞག་གོ། །

[Block 3923]
འབྱུང་ཁར་བླང་ངོ་ཞེས་བྱ་བ་ནི་གདུགས་གང་དུ་གཞག་པའི་གྲོང་དེ་ནས་ཕྱིར་འབྱུང་ཁར་དེ་བླང་ངོ་། །གཙུག་ལག་ཁང་ན་གནས་པའི་སྐབས་བཤད་ཟིན་ཏོ།། །།

[Block 3924]
ད་ནི་གནས་གཞན་ན་གནས་པའི་སྐབས་བརྗོད་པར་བྱ་སྟེ། །རོལ་མོ་མཁན་གྱི་གནས་དང་། སྨད་འཚོང་མའི་གནས་དང་། ཆང་འཚོང་མའི་གནས་དང་། རྒྱལ་པོའི་ཕོ་བྲང་དང་། གདོལ་པའི་ཁྱིམ་གྱི་གནས་དག་བསྟེན་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། རོལ་མོ་ཞེས་བྱ་བ་ནི་གླུ་མཁན་ལ་སོགས་པ་རྩེ་འཇོའི༌[^4043]གནས་སོ། །

[Block 3925]
གདོལ་པའི་ཁྱིམ་གྱི་གནས་དག་ཞེས་བྱ་བ་ནི་གདོལ་པའི་གནས་དག་གོ། །

[Block 3926]
དེ་ལྟར་སྤྱོད་ཡུལ་མ་ཡིན་པའི་གནས་ལྔ་པོ་དེ་དག་ཏུ་འཇུག་པར་མི་བྱའོ། །

[Block 3927]
མི་གཙང་བའི་སྐྱབས༌[^4044]དང་ཉེ་བར་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འཇུག་པའི་ཕྱིར་སོང༌[^4045]ན་ཡང་དེའི་ཉེན་ཀོར༌[^4046]དུ་བསྡད་པར་མི་བྱའོ། །

[Block 3928]
འདིར་གཞུང་ནི་གླེང་གཞི་དག་ལས་དེ་ལྟ་བས་ན། དགེ་སློང་གིས་ཆབ་ཁུང་སར་སོང་ན་འདུ་འཛིས་གནས་པར་མི་བྱའོ། །

[Block 3929]
དེའི་ཉེ་འཁོར་དུ་ལུང་དབོག་པར༌[^4047]མི་བྱ་བཀླག་པར་མི་བྱ་ཁ་ཏོན༌[^4048]མི་བྱའོ་ཞེས་བྱ་བ་ལ་སོགས་པ་གསུངས་པ་ཡིན་ནོ། །

[Block 3930]
གོས་རིན་པོ་ཆེར་གྱུར་པས་དགོན་པར་གནས་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་ལ་བ་རིན་པོ་ཆེ་ལ་སོགས་པ་རིན་ཆེ་བས༌[^4049]སོ། །

[Block 3931]
ལྡུམ་བུ་ནི་མེ་རུ༌[^4050]ཀའི་ཕྱེ་མས་ལ་བ་ལ་སྲོག་ཆགས་དག་མི་འབྱུང་ངོ་། །ཤིང་ཀུན་གྱིས་ཀྱང༌[^4051]ངོ་ཞེས་བྱ་བ་ལ་ཤིང་ཀུན་གྱི༌[^4052]ཕྱེ་མས་ཀྱང་ལ་བ་ལ་སྲོག་ཆགས་དག་མི་འབྱུང་བའོ། །

[Block 3932]
ཤིང༌[^4053]ནིམ་པ་དང་བ་ཤ་ཀའི་ལོ་མ་དག་གིས་ཀྱང༌[^4054]ངོ་ཞེས་བྱ་བ་ནི་ཤིང་ནིམ་པ་དང་བ་ཤ་ཀའི་ལོ་མ་དག་གིས་ཀྱང༌[^4055]ངོ་ཞེས་བྱ་བའི་དོན་ནོ། །

[Block 3933]
རིམ་པ་དེར་སོང་ན༌[^4056]དེ་ལ་ཤིན་ཏུ་ཕན་པ་ཉིད་དོ་ཞེས་བྱ་བ་ལ། རིམ་པ་དེར་སོང་ན་ཞེས་བྱ་བ་ནི་རིམ་པ་དེ་ལ་ཤིན་ཏུ་ཕན་པ་ཉིད་དུ་འགྱུར་ཏེ། དེ་ཙམ་གྱི༌[^4057]མཐུས་རིམ་པ་གཞན་ལ་ཡང་ཤིན་ཏུ་ཕན་པའི་དྲི་འབྱུང་ངོ་། །དེ་རྣམས་ལ་ཡང་ཕན་པ་དེ༌[^4058]ཉིད༌[^4059]འབྱུང་བའོ། །

[Block 3934]
སྐམ་པ་ཡང་དེའི་དོན་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་གོས་སྐམ་པ་ཡང་སྲོག་ཆགས་མི་སྐྱེ་བ་དེའི་དོན་ཉིད་ཡིན་པའོ། །

[Block 3935]
འདིར་གཞུང་ནི་དུས་དུས༌[^4060]སུ་བསྐམ་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3936]
དགོན་པ་བས་ཕྱོགས་དང་ལམ་དང་། ཚེས་གྲངས་དང་ཉི་མ་དང་རྒྱུ་སྐར་དག་ལ་མཁས་པར་བྱའོ་ཞེས་བྱ་བ་ནི་དགོན་པ་པས་དེ་དག་ཤེས་པར་བྱ་བའོ། །

[Block 3937]
རྟག་ཏུ་མེ་དང་ཆུ་ཡོད་པར་རོ། །

[Block 3938]
ཕྱེ་དང་རས་མ་དག་དང་སྦྲང་རྩི་དང་ཞུན་མར་དག་ཅི་འབྱོར་པ་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། ཕྱེ་དང་ཞེས་བྱ་བ་ཐམས་ཅད་དུ་ཅི་འབྱོར་པ་ཞེས་བྱ་བ་ལྷག་མ་ཉིད་ལ་ཡང་རིག་པར་བྱའོ། །

[Block 3939]
འདིར་གཞུང་ནི་ཕྱེ་དང་སྦྲང་རྩི་དང་ཞུན་མར་ཅི་འབྱོར་པ་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3940]
གལ་ཏེ་ཟས་ལས་ལྷག་རོལ་བྱུང་ན་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གལ་ཏེ་ཟས་ལས་ལྷག་རོལ་ལུས་པར་གྱུར་ན་ཡང་ཉེ་བར་གཞག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3941]
དགེ་སློང་མས་དགོན་པར་གནས་པར་མི་བྱའོ། །

[Block 3942]
གྲོང་ཁྱེར་གྱི་ནང་དུ་དབྱར་ཁང་བྱའོ། །

[Block 3943]
དེས་དེའི་ཕྱིར་སྒོར༌[^4061]འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེའི་ཞེས་བྱ་བ་ནི་དབྱར་ཁང་དེའི་འོ། །

[Block 3944]
དེས་ཞེས་བྱ་བ་ནི་དགེ་སློང་མ་དེས་སོ། །

[Block 3945]
སྣང་གཡེལ་ཅན་དུ་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདུག་པར་ཏེ། འདིར་སྣང་གཡེལ་ཞེས་བྱ་བ་སྐར་ཁུང་འབའ་ཞིག་ཏུ་མ་ཟད་ཀྱི་གང་དུ་ཕྱི་རོལ་སྣང་བ་ཐམས་ཅད་ཡང་ཡིན་པར་རོ། །

[Block 3946]
ལམ་བཞི༌[^4062]མདོར་མི་བྱའོ། །

[Block 3947]
གོས་མེད་པ་ཅན་གྱིས་མི་བྱའོ་ཞེས་བྱ་བ་ནི་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 3948]
དབྱར་ཁང་ཞེས་སྨོས་པ་ནི་ལམ་གྱི་བཞི་མདོ་ལས་ལོག་པ་སྟེ། ཐམས་ཅད་དུ་ཆོ་ག་འདི་ཉིད་ཡིན་ནོ། །

[Block 3949]
དེ་ལ་རྔུལ་གཟན་ནི་གོས་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལ། དེ་ལ་ཞེས་བྱ་བ་ནི་དེ་ཐོག་མར་གསུངས་པའི་ཆོ་ག་ལའོ། །

[Block 3950]
དཔུང་པ་གཉིས་མ་གཡོགས་པར་ཁྱིམ་པའི་དྲུང་དུ་མི་བྱའོ་ཞེས་བྱ་བ༌[^4063]ནི་རྔུལ་གཟན་གྱི་གོས་ཉིད་གོན་དུ་ཟིན་ཀྱང་དཔུང་པ་གཉིས་མ་གཡོགས་པར་ཁྱིམ་པའི་དྲུང་དུ་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3951]
དེའི་སྐྱིལ་མོ་ཀྲུང་གི་གནས་སུ་སྐྱིལ་མོ་ཀྲུང་ཕྱེད་དོ་ཞེས་བྱ་བ་ལ། སྐྱིལ་མོ་ཀྲུང་གི་གནས་སུ་སྐྱིལ་མོ་ཀྲུང་ཕྱེད་ཀྱིས་འདིར་ཏིང་ངེ་འཛིན་ལ་འདུག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3952]
ཟག་བྱེད་ཀྱི་སྒོར་སྲོག་ཆགས་མི་འཇུག་པར་བྱ་བའི་ཕྱིར་གོས་ལ་སོགས་པས༌[^4064]གཡོག་གོ། །

[Block 3953]
དགེ་སློང་དག་གིས་དགེ་སློང་མ་གཙུག་ལག་ཁང་དུ་འཇུག་པ་བཟློག་པར་མི་བྱའོ། །

[Block 3954]
དེ་དག་གཏམ་མི་འདྲེ་བ་དང་མི་གདམས་པ་དང་གསོ་སྦྱོང་དང་དགག་དབྱེ་གཞག་པ་དག་གིས་ཡོངས་སུ་གདུལ་བར་བྱའོ། །

[Block 3955]
དེས་དགེ་སློང་རྗེས་སུ་གནང་བ་བྱེད༌[^4065]དུ་མ་བཅུག་པར་གཙུག་ལག་ཁང་དུ་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་སྨོས་ན། དགེ་སློང་གིས་དེ་ལ་ཇི་ལྟར་རྗེས་སུ་གནང་བར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཁྱོད་ནད་དང་བཅས་པ་མ་ཡིན་ན་རྗེས་སུ་གནང་ངོ་ཞེས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3956]
[^4066]དེ་བཞིན་དུ་རྗེས་སུ་གནང་བར་བྱ་བའམ་ཞེ་ན། དེའི་ཕྱིར་དྲི་བ་ཞེ་འགྲས་པ་མེད་པ་ཉིད་ངེས་པར་ཤེས་པར་བྱས་ཏེའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དྲི་བ་གང་གིས་དེ་ལ་ཞེ་འགྲས་པ་མེད་ཅིང་དྲི་བ་དེ་ཤུགས་ཀྱིས་ཤེས་པར་བྱའོ། །

[Block 3957]
གནས་ཀྱི༌[^4067]ཡང་དག་པར་སྦྱོར་བའི་སྐབས་བཤད་ཟིན་ཏོ།། །།

[Block 3958]
ད་ནི་སྦ་བའི་རྣམ་པར་གཞག་པ་དང་ཡོངས་སུ་བསྐྱབ་པའི་སྐབས་བརྗོད་པར་བྱ་སྟེ། འཕྲེད་གཏན་དང་གནམ་གཟེར་དང་། འཁོར་གཏན་དང་སྒོ་ལྕགས་དང་ལྡེ་མིག་ཀྱོག་པོ་དག་གཙུག་ལག་ཁང་བསྡམས་པའི༌[^4068]ཕྱིར་ཡང་དག་པར་སྦྱར་རོ་ཞེས་བྱ་བ་ལ།

[Block 3959]
འདིར་གཞུང་ནི་སིལ༌[^4069]བུ་དག་ལས།

[Block 3960]
བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སློང་དག་ལྔ་པོ་འདི་དག་ནི་སྡོམ་པར་བྱེད་པ་དག་ཡིན་ཏེ་ལྔ་གང་ཞེ་ན། འཕྲེད་གཏན་དང་གནམ་གཟེར༌[^4070]དང་འཁོར་གཏན་དང་སྒོ་ལྕགས་དང་ལྡེ་མིག་ཀྱོག་པོ༌[^4071]སྟེ། དེ་དག་གཙུག་ལག་ཁང་ན་བདོག་ན་དེ་དག་ཐམས་ཅད་དགེ་སྐོས་ཀྱིས་བཅང་བར་བྱའོ་ཞེས་གསུངས་པ་དང་། རྣམ་པར་འབྱེད་པ་ལས་ཀྱང་དགེ་འདུན་གྱི༌[^4072]གནས་བརྟན་དགེ་སློང་གིས་དགེ་སྐོས་ལ་ཚེ་དང་ལྡན་པ་ཁྱོད་ཀྱིས་སྒོ་བཅད་དམ། གཙུག་ལག་ཁང་སོ་སོར་བརྟགས་སམ་ཞེས་བྲི་བར་བྱའོ་ཞེས་གསུངས་པ་དང་མ་མོ་ལས་ཀྱང་། བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་རྣམས་ལ་གནས་མལ་བསྲུང་བའི་ཕྱིར་ལྡེ་མིག་འཁྱོག་པོ་རྗེས་སུ་གནང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །
--- END BLOCKS ---
