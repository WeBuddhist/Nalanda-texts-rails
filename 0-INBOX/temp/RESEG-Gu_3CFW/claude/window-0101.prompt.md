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
[Block 3536]
གང་ཞིག་འདི་གདིང་བ་པོ་བསྟན་པ་སྟེ། འདིར་སྦེད་པའོ་ཞེས་བྱ་བར་རྗོད་པ་པོ༌[^3619]རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 3537]
གོས་དག་གོ་ཞེས་བྱ་བ་ནི་སྦེད་པ་པོ་བསྐོ་བར་བྱའོ། །

[Block 3538]
འགྱེད་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་གོས་སྦེད་པ་དང་འགྱེད་པ་པོ་དེ་གཉིས་བསྐོ་བར༌[^3620]བྱའོ། །

[Block 3539]
དགེ་སྐོས་དང་མངག༌[^3621]གཞུག་གོ་ཞེས་བྱ་བ་ནི༌[^3622]སྐོས་ཅི་རིགས་པར་སྦྱར་བའི་ཕྱིར་བསྡུས་པའོ། །

[Block 3540]
དགེ་སྐོས་ཀྱི་བྱ་བ་དང་བག་ཡངས་སུ་གྱུར་པ་དང་དེས་བྱ་བ་གང་ཡིན་པ་དེས་དེ་འགྲུབ་པའི་ཕྱིར་རོ། །

[Block 3541]
འདིར་གཞུང་ནི་དགེ་སློང་རྣམས་ཀྱི༌[^3623]ཟན་གྱི་གྲལ་དང་ཆོས་ཉན་སར་སུ་ཡང་སྟན་ཤོམ་པར་མི་བྱེད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། དགེ་སྐོས་བསྐོ་བར་བྱ་ཞིང་དགེ་སྐོས་ཀྱིས་ཀུན་དུ་སྤྱོད་པ༌[^3624]ཐམས་ཅད་བྱའོ། །

[Block 3542]
དགེ་སྐོས་ལ་བྱ་བ་ཅུང་ཞིག་བྱུང་བ་དེས་སུ་ཡང་མི་བྱེད་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། མངག༌[^3625]གཞུག་བསྐོ་བར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3543]
སྡེར་སྤྱད་འདྲིམ་མོ་ཞེས་བྱ་བ་ནི་བསྐོ་བར་བྱའོ།[^3626] །དེ་དག༌[^3627]འདྲིམ་པ་དང་ཟན་གྱུ་ནས་སྦ་བ་ནི་དེའི༌[^3628]ལས་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་དགེ་སློང་དེས་ཟན་གྱི་དོན་དུ་སྡེར་སྤྱད་འདྲིམ་པར་བྱའོ། །

[Block 3544]
འདིར་གཞུང་ནི་སྡེར་སྤྱད་འདྲིམ་པ་དེས་དགེ་སློང་རྣམས་ཀྱི༌[^3629]ཟན་གྱི་གྲལ་དུ་སྡེར་དག་བྲིམ་པར༌[^3630]བྱ་ཞིང་ཟན་ཟོས་ཟིན་ནས་བྲུབ་པར་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3545]
ཆུའི་ཞལ་ཏ་པའོ་ཞེས་བྱ་བ་ནི་ཆུ་སྦྱིན་པ་ལ་དེའི་བྱ་བ་ལ་བསྐོ་བར་བྱའོ་ཞེས་བྱ་བའི་དོན་གྱིས་ཤེས་པའོ། །

[Block 3546]
མཛེས་ཆོས་སོ་ཞེས་བྱ་བ་ནི་མཛེས་པར་བྱ་བའི་དོན་དུ་འཆོས་པ་ནི་མཛེས་ཆོས་ཀྱི་དོན་དུ༌[^3631]བསྐོ་བར་བྱའོ། །

[Block 3547]
དེ༌[^3632]བལྟས་ཏེ་རབ་ཏུ་བྱུང་བ༌[^3633]རྣམས་མི་མཛེས་པ༌[^3634]བསྟེན་ན་སེ་གོལ་གྱི་སྒྲ་སྔོན་དུ་བཏང་སྟེ་མཛེས་པ་ལ་ངེས་པར་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་ནི་མཛེས་ཆོས་དེས་སོ། །

[Block 3548]
མཛེས་པ་ལ་ངེས་པར་སྦྱར་བའི་ངོ་བོ་ཉིད་བསྟན་པའི་ཕྱིར་འདི་ལྟ་སྟེ། ཟས་ལ་སྒྲ་བསྐྱུང་བ་ཉིད་དང་ཤིན་ཏུ་བསྡམས་པ༌[^3635]ཉིད་དང་ཤིན་ཏུ་ནོགས་ཐུག་པ་ཉིད་ཀྱིས་སོ། །

[Block 3549]
མཆོད་རྟེན་ལ་ཕྱག་བྱ་བ་ལ་སྒྲ་བསྐྱུང་བ་ཉིད་དང་རྒན་རིམས་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3550]
བང་རིམ་གྱི་ཞལ་ཏ་པའོ་ཞེས་བྱ་བ་ནི་བསྐོ་བར་བྱའོ། །

[Block 3551]
དེས་དང་པོར་ཟན་ཟོས་ཏེ་དབྱི་གུ༌[^3636]བླངས་ནས་ཟན་ཟ་བ་དག་ལ་ཁྭ་ཏ་དང་བྱེའུ་དང་ཕུག་རོན་ལ་སོགས་པ་དག་བཟློག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བང་རིམ་གྱི་ཞལ་ཏ་བ་དེས་སོ། །

[Block 3552]
ཁྭ་ཏ་ལ་སོགས་པ་དེ་དག་ནི་བང་རིམ་ལ་སོགས་པ༌[^3637]དག་ཏུ་གནས་འཆའ་བས་དེའི་ཕྱིར་དེས་ཤས་ཆེར་དེ་དག་ཟློག་པར་བྱེད་པས་བང་རིམ་གྱི་ཞལ་ཏ་བ་ཞེས་བྱའོ། །

[Block 3553]
གནས་མལ་དབོག་པ་དང་གནས་མལ་བྱི་བོ་དབོག་པའོ་ཞེས་བྱ་བ་ནི༌[^3638]དེ་གཉིས་དབོག་པ་སྤྲོ་བར་བྱ་སྟེ་གཅིག་གི༌[^3639]དངོས་པོའོ། །

[Block 3554]
གནས་མལ་ཞེས་བྱ་བ་ནི་ཁྲི་དང་ཁྲིའུ་ལ་སོགས་པ་ལ་རྟག་པར་གནས་པ༌[^3640]ལའོ། །

[Block 3555]
གནས་མལ་བྱི་བོ་ཞེས་བྱ་བ་ནི་ཁྲི་དང་ཁྲིའུ་དང་། [^3641]སྟན་ནང་ཚངས་ཅན་དང་མལ་ཆ་དང་སྟན་དང་གནས་མལ་ལ་སོགས་པ་མེད་པ་འདི་ལྟ་སྟེ། ཤིང་ལྗོན་པའི་དྲུང་དང་ནེའུ་གསིང་ལ་སོགས་པ་གཏན་གྱི་གནས་མལ་མ་ཡིན་པའོ། །

[Block 3556]
ཟས་རུང་བ་དང་བཅས་པ་ཉིད་ཡིན་ན་མི་དག་འོང་བ་ལ་སྒེའུ་ཆུང་སྲུང་བའོ༌[^3642]ཞེས་བྱ་བ་ནི་འཇིག་རྟེན་པ༌[^3643]ཞུགས་ནས་ཟས་རུང་བ༌[^3644]དང་བཅས་པ་ཉིད་ཅེས་བྱ་བ་ཤ་དང་བཅས་པ་ཉིད་ཡིན་ན། དེར་མི༌[^3645]གཞན་དག་འོང་བ་དགག་པའི་ཕྱིར། སྒེའུ་ཆུང་སྲུང་བ་སྤྲོ་བར་བྱ་སྟེ་བསྐོ་བར་བྱའོ། །

[Block 3557]
འདིར་སྒེའུ་ཆུང་ཞེས་བྱ་བ་ནི་དགག་པ་སྒོ་བ་ཡིན་པར་རིག་པར་བྱའོ། །

[Block 3558]
འདིར་གཞུང་ནི་དགེ་སློང་དག་གྲལ་ན་ཟན་ཟ་བ་ན༌[^3646]མི་དག་འོངས༌[^3647]ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། སྒེའུ་ཆུང་སྲུང༌[^3648]བ་བསྐོ་བར་བྱའོ། །

[Block 3559]
ཤ་དག་འདྲིམ་པ་ན་བྲམ་ཟེ་དང་ཁྱིམ་བདག་དག་འཕྱ་ནས། བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། གང་གི་ཚེ་རུང་བ་ཡོད་པ་དེའི་ཚེ་སྒེའུ་ཆུང་སྲུང་བ༌[^3649]བསྐོ་བར༌[^3650]བྱའོ་ཞེས་བྱ་བ་གསུངས་པ་ཡིན་ནོ། །

[Block 3560]
གནས་མལ་གྱི་གཞིའོ།། །།

[Block 3561]
ཕྱག་བྱ་བའི་གནས་མུན་ཁྲོད་དུ་ཕྱག་དང་བཅས་པའི་ཚིག་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་ནི་ཕྱག་འཚལ་བའི་གནས་མུན་ཁྲོད་དུ་དགེ་སློང་གིས༌[^3651]ཕྱག་མི་བྱ་བར་ཕྱག་འཚལ་ལོ་ཞེས་བྱ་བའི་སྒྲ་དང་བཅས་པའི་ཚིག་བརྗོད་པར་བྱ་བ་ཡིན་གྱི་ཞེས་བྱ་བ་འདིར་སྨོས་ན། འདི་ནི་ཕྱག་འཚལ་བའི་ཚེ་མདུད་པ༌[^3652]མེད་པར་འདི་མི་རིགས་སོ་ཞེ་ན། བདེན་མོད་ཀྱི་དེའི་ཕྱིར་འདུད་པ་དང་བཅས་པར་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3562]
ཉེན་ཀོར་དུ་གྱུར་པ་གཞན་གྱིས༌[^3653]ཕྱག་བྱ་བར་བརྩམས་པ་ལ་ཕྱག་མི་བྱ་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་གྱིས་ཕྱག་བྱ་བར་བརྩམས་པ་ལ་ཉེན་ཀོར་དུ་གྱུར་པ་གཞན་གྱིས་ཕྱག་བྱ་བར་འོས་པ་ལ་གཞན་གྱིས་ཕྱག་མི་བྱ་བ་མ་ཡིན་ནོ། །

[Block 3563]
སིལ་བུ་དག་ལས་འདི་དང་པོར༌[^3654]བྱས་ནས་ཕྱག་འཚལ་བ་ཉིད་དོ༌[^3655]ཞེས་བྱ་བའི་མཐར་ཐུག་པའོ། །

[Block 3564]
འདིར་ཞུ་བ་དག་ལས།

[Block 3565]
མཐའ་དང་བཅས་པ་ལ་དོར་ནས་མི་བྱ་ཞེས་བྱ་བའི་བར་དུ་གསུངས་སོ། །

[Block 3566]
ཚངས་པའི་ཕྱག་གིས་ནི་དེ་བྱས་པ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཚངས་པའི་ཕྱག་ཅེས་བྱ་བ་ཐམས་ཅད་ལ་ཁྱབ་པ་ཐམས་ཅད་གནས་གཅིག་ཏུ་ཚོགས་པ༌[^3656]ལ་སྤྱིར་ཕྱག་བྱ་བ་བསྟན་པ་སྟེ་དེ་བྱས་ན༌[^3657]དེ་བྱས་པ་ཉིད་ཡིན་པའོ། །

[Block 3567]
ནང་དང་བཅས་པ་ལ་ཕྱག་མི་བྱའོ་ཞེས་བྱ་བ་ལ། འདིར༌[^3658]ནང་དང་བཅས་པ་ཞེས་བྱ་བ་ནི་གནོད་པ་བྱ་བའི་བསམ་པས་ཉེ་བར་གནས་པར་བྱ་བ་ཡིན་པར་རིག་པར་བྱའི། རྩོད་དོ་ཅོག་ཐམས་ཅད་ནི་མ་ཡིན་ནོ། །

[Block 3568]
དེ་བས་ན་གནོད་པར༌[^3659]བྱ་བའི་བསམ་པས་ཉེ་བར་གནས་པ་ལ་ཕྱག་བྱར་མི་རུང་གི་རྩོད་པ་གཞན་ལ་ནི༌[^3660]རུང་ངོ་། །འདིར་གཞུང་ནི་གཉིས་ལ་ཕྱག་བྱ་སྟེ། གློ་བུར་དུ་འོངས་པ་དག་དང་གཉུག་མར་གནས་པ་དག་གིས་ཕན་ཚུན་རྒན་རིམས་བཞིན་དུ་ཕྱག་བྱའོ། །

[Block 3569]
ནང་དང་བཅས་པ་དང་ཡོངས་སུ་གནས་པ་བྱེད་པ་ནི་མ་གཏོགས་སོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 3570]
ཕྱག་འཚལ་བ་ལ་ཨ་རོག་གྱ༌[^3661]ཞེས༌[^3662]བྱ་བར་མི་བྱའོ། །

[Block 3571]
འདས་པ་ལ༌[^3663]ཕྱག་བྱ་བ་ཡིན་པ་ལ་ཕྱག་མི་བྱ་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་སྔོན་འདས་པའི་དུས་ན་དེ་ཕྱག་བྱ༌[^3664]བ་ཉིད་དུ་འགྱུར་བ་ཡིན་ན། [^3665]ད་ལྟར་ཕྱག་བྱ་བ་ཉིད་མ་ཡིན་དུ་ཟིན་ཀྱང་སྔོན་གྱི་གནས་སྐབས་དེ་ཉིད་མངོན་སུམ་བྱས་ཏེ་ཕྱག་བྱར་རུང་བས་དེའི་ཕྱིར་དེ་ལ་ཕྱག་བྱ་བ་ཉིད་ཡིན་ནོ། །

[Block 3572]
འདི་ནི་དགེ་སློང་རྒན་པོ་ཁྲོས་པའི་དབང་གིས་སྡོམ་པ་རྒྱུན་ཆད་དེ་སྦྲུལ་དུ་གྱུར་པ་ལ། དགེ་སློང་ཅིག་ཤོས་ཀྱིས་སྔོན་གྱི་རྒྱུད་དེ་མངོན་སུམ་དུ་བྱ་སྟེ༌[^3666]འདུད་པར་བྱའོ་ཞེས་གསུངས་པའི་གླེང་གཞི་ཡིན་ཏེ། ཐམས་ཅད་ལ་བྱེ་བྲག་མེད་པས་བྱར་རུང་བས་འདིར་སྤྱིར་མདོར་བྱས་སོ། །

[Block 3573]
སྦགས་པ་ལ་ཕྱག་མི་བྱའོ། །

[Block 3574]
སྦགས་པས་ཕྱག་མི་བྱའོ། །

[Block 3575]
དེས་བདག་གིར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་སྦགས་པ་ལ་ཕྱག༌[^3667]མི་བྱ་བ་དང་། སྦགས་པས༌[^3668]གཞན་ལ་ཕྱག་མི་བྱ་བ་དང་། སྦགས་པས་ཕྱག་དེ་བདག་གིར་མི་བྱའོ། །
--- END BLOCKS ---
