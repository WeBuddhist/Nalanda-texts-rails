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

[Block 3611]
ཕྱི་བཞིན་མི་འབྲང་བ་དེ་བསན་པར་བྱ་བའི་ཕྱིར། རབ་ཏུ་བྱུང་བའི་རྗེས་སུ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། འདི་དག་ཅེས་བྱ་བ་ནི་མཆི་མས་འཇུ་བའོ། །

[Block 3612]
ཇི་ལྟར་བྱམས་པས་མཆི་མ་འབྱུང་བར་བྱེད་པ་དེ་བཞིན་དུ་རབ་ཏུ་འབྱུང་བ་ལ་ཡང་བྱ་བའི་རིགས་སོ། །ཅིའི་ཕྱིར་དེ་ལྟར་བྱ་བའི་རིགས༌[^2329]ཤེ་ན། སྨྲས་པ། ངོ་མཚར་བར་འགྱུར་བ་འདི་བཞིན་དུ་མི་འགྱུར་རམ་ཞེས་པ་སྟེ། དམ་པའི་སེམས་ལ་སྤྱོད་པ་དེའོ། །

[Block 3613]
ནགས་སུ་བདག་ཉིད་གཅིག་པུ་འགྲོ་ཡང་གྲོགས་ཤིན་ཏུ་རྙེད་པར་དཀའ་ལ། གཞན་དག་གིས་ནི་རྙེད་པར་སླའོ་ཞེས་བྱ་བ་དེའི་དབང་དུ་བྱས་ནས། ཡོན་ཏན་མེད་པ་ཞེས་བྱ་བ་དེའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3614]
ཕོངས་པར་གྱུར་པའི་ཚེ་ཞེས་བྱ་བ་ནི་བསད་པ༌[^2330]དང་། བཅིང་བ་དང་བརྡེག་པའི་ཕོངས་པར་གྱུར་པའོ། །

[Block 3615]
ཡོན་ཏན་ཡོད་བཞིན་ཞེས་བྱ་བ་ཕོངས་པ་ཉིད་བསྟན་པའི་ཕྱིར། ཡོན་ཏན་ཡོད་བཞིན་དུ༌[^2331]ཞེས་བྱ་བ་ཡིན་ཏེ། ནགས་སུ་འགྲོ་ཞིང་རབ་ཏུ་བྱུང་བ་དེ་ནི་ཕོངས་པ་བཞིན་དུ་ཕོངས་པར་གྱུར་པ་ཡིན་ནོ། །

[Block 3616]
ཐམས་ཅད་དུ་གྲོགས་ཡོད་ཀྱང་དེ་དག་ཉིད་ནགས་སུ་འགྲོ་ཞིང་རྗེས་སུ་འགྲོ༌[^2332]བ་མེད་པ་ཉིད་ཀྱི་དབང་དུ་བྱས་ནས། གླང་ཆེན་སྨྱོན་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་ཡིན་ཏེ། གང་ལ་རྗེས་སུ་མི་འགྲོ་བ་དང་། གང་གི་ཕྱིར་རྗེས་སུ་མི་འགྲོ་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 3617]
དེ་དག་མིན་ནམ་ང་ཡང་དེ་མ་ཡིན། །ཞེས་བྱ་བ་ནི་ཐེ་ཚོམ་གྱི་ཚིག་གོ། །

[Block 3618]
དེ་ལྟ་མོད་ཀྱི་བདག་གི་བྱམས་པ་མེད་པར་འགྱུར་བའི་རྒྱུ་ཅུང་ཟད་ཅིག་བྱས་ན་ནི། དེ་ལས་རྗེས་སུ་མི་འབྲང་བ་ཡིན་ཏེ། དེ་མེད་པར་བསྟན་པའི་ཕྱིར། དེ་ལྟར་བྱམས་པ་ཉམས་པར་འགྱུར་བའི་རྒྱུ། །ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3619]
འདི་ལྟར་འཁོད་བཞིན་དུ་ཞེས་བྱ་བ་ནི་རྒྱབ་ཀྱིས་བལྟས་པར་གནས་པའོ། །

[Block 3620]
འདི་ལྟར་གྱུར་པ་ཞེས་བྱ་བ་ནི་གླང་ཆེན་སྨྱོན་པ་ཞེས་བྱ་བའི༌[^2333]ཚིགས་བཅད་སྔར་བསྟན་པ་དེ་ཉིད་བདག་གི་ཡོན་ཏན་གང་གིས་སྔོན་དུ་འགྲོ་བར་བསྟོད་པ་དག་རུང་བར་འོང་ངམ་ཀྱེ་ཞེས་བྱའོ། །

[Block 3621]
བདག་ནི་ནགས་སུ་འགྲོ་ཕྱིར་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱི་ཉེས་པ་སྟོན་པ་ཡིན་ནོ། །

[Block 3622]
ཅིའི་ཕྱིར་དེ་ལྟར་རྟོག་ཅེ་ན་དེའི་རྒྱུ་བསྟན་པའི༌[^2334]ཕྱིར། གང་དག་ཁྱིམ་གྱི་ཉེས་པ་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3623]
དེ་གང་ཡིན་ཞེ་ན། ཁྱིམ་གྱི་ཉེས་པ་གསལ་བར་མངོན་པ་དང་། དཀའ་ཐུབ་ཀྱི་ནགས་ཀྱི་ཡོན་ཏན་གསལ་བར་མངོན་པའོ། །

[Block 3624]
དེ་གསལ་བར་བསྟན་པའི་ཕྱིར། ཕྱི་མའི་ཚེ་དང་ཚེ་འདིའི་སྡུག་བསྔལ་རྒྱུ། །ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 3625]
ཕྱི་མའི་སྡུག་བསྔལ་གྱི་རྒྱུ་ནི་འདོད་པ་དེའི་ཆེད་དུ་ཉེས་པར་སྤྱོད་པ་དེ་ཉེས་པར་སྤྱད་པ་དེའི་རྒྱུ༌[^2335]ངན་འགྲོར་འགྲོ་བའི་ཕྱིར་རོ། །

[Block 3626]
ཚེ་འདིའི་སྡུག་བསྔལ་གྱི་རྒྱུ་ནི། གསད་པ༌[^2336]དང་། བཅིང་བ་དང་། བརྡེག་པ་ལ་སོགས་པ་སྡུག་བསྔལ་དུ་མའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3627]
དཀའ་ཐུབ་ཀྱི་ནགས་ནི་དེ་ལྟར་བཟློག་པ་སྟེ། འཇིག་རྟེན་འདི་དང་ཕ་རོལ་གྱི་བདེ་བའི་རྒྱུར་གྱུར་པའི་ཕྱིར་རོ། །

[Block 3628]
འཇིག་རྟེན་འདིར་བདེ་བའི་རྒྱུ་ནི་འདོད་པ་རྣམས་ལ་ཆེད་ཆེར་མི་འཛིན་པ་སྟེ། རང་གི་དོན་མཐོང་བའི་ཕྱིར་རོ། །

[Block 3629]
འཇིག་རྟེན་ཕ་རོལ་དུ་ནི་བདེ་འགྲོ་དང་མྱ་ངན་ལས་འདས་པ་ཐོབ་པའི་ཕྱིར་རོ། །

[Block 3630]
རང༌[^2337]གི་རྒྱུ་འདོད་པ་སྤོང་བར་མི་འདོད་པ་དེ་ནི་སྡུག་བསྔལ་གྱི་རྒྱུ་ཡིན་ནོ། །

[Block 3631]
དཀའ་ཐུབ་ཀྱི་ནགས་ན་ནི་དེ་རྣམས་ཀྱིས་བཟློག་པ་ཡིན་ཏེ། འདི་དག་སྤོང་བ་ཡིན་ནོ། །

[Block 3632]
དེའི་རྒྱུ་ཉེས་པ་དག་ལ་བདག་ཉིད་ཀྱི་བསྒྲུབ་པ་བསྟན་པའི་ཕྱིར། བདག་གི་མཛའ་བོ་འདི་རྣམས་ཞེས་བྱ་བའི་ཚིགས་བཅད་སྨོས་སོ། །

[Block 3633]
བསླུས་ཞེས༌[^2338]བྱ་བ་ནི་ཕྱིན་ཅི་ལོག་ལ་ཞེན་པའོ། །

[Block 3634]
ཞི་བར༌[^2339]མ་གྱུར་པ་ནི་མྱ་ངན་ལས་འདས་པར་མ་གྱུར་པའོ། །

[Block 3635]
ཉེས་པ་དེ་དག་ཅེས་བྱ་བ་ནི་ཁམས་གསུམ་གྱི་ཉོན་མོངས་པ་ཐམས་ཅད་དོ། །

[Block 3636]
མངོན་དུ་གཞོམ་པར་བྱ་ཞེས་བྱ་བ་ནི་བག་ཆགས་དང་བཅས་པ་གཞོམ་པར་བྱའོ་ཞེས་པའོ། །

[Block 3637]
དེ་ལྟར་གྱུར་པ་ནི་དམ་པ་རྣམས་སུ་དེ་དགེ་སློང་དང་དགེ་བསྙེན་རྣམས་སུ་གྱུར་པས་སོ། །

[Block 3638]
སློབ་དཔོན་དཔའ་བོས་མཛད་པའི་སྐྱེས་པའི་རབས་རྒྱ་ཆེར་བཤད་པ་ལས་ཚོང་དཔོན་གྱི་སྐྱེས་པའི་རབས་སོ།། །།

[Block 3639 [HEADING]]
## སྐྱེས་པའི་རབས་བཅུ་པོ་འདི་དག་གི་གོ་རིམས། ^22-0

[Block 3640]
སྡོམ་ལ།

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
--- END BLOCKS ---
