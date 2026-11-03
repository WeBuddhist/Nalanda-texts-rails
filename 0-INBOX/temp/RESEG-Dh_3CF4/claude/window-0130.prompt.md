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
[Block 4551]
རི་དགས་འདྲ་བ་ཞེས་བྱ་བ་ནི་སྐྱེ་བོ་མེད་པའི་ཕྱིར་རོ། །

[Block 4552]
བཀྲ་བ་ནོར་བུ་ནི་ནོར་བུ་བཀྲ་བའོ། །

[Block 4553]
བཀྲ་བ་ནི་ནོར་བུ་ཉིད་སྐར་མ་ཡིན་པས། བཀྲ་བའི་ནོར་བུ་རིན་ཆེན་སྐར་མའོ། །

[Block 4554]
དེས་མཛེས་པའི་སྤྲིན་གང་ཡིན་པ་དེ་ནི་ནོར་བུ་རིན་ཆེན་སྐར་མ་བཀྲ་བས༌[^2953]མཛེས་པའོ། །

[Block 4555]
འདིར་འོངས་ཞེས་བྱ་བ་གློ་བུར་དུའོ། །

[Block 4556]
ཅིའི་ཕྱིར་ཞེས་བྱ་བ་ནི་གང་གི་རྒྱུས་སོ། །

[Block 4557]
ལྟ་ཞིང་ཞེས་བྱ་བ་ནི་གྱེན་དུ་ལྟ་བའོ། །

[Block 4558]
སུ་ཞིག་ཡིན་ཞེས་བྱ་བའི་ལན་ནི་བདག་ནི་མི་ཞིག་ལགས་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4559]
འདིར་འོངས་ཞེས་བྱ་བའི་ལན་ནི་ཤིང་འདིའི་འབྲས་བུ་ཚོལ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 4560]
ཅིའི་ཕྱིར་ཞེས་བྱ་བའི་ལེན་ནི་འདི་ལྟ་བུར༌[^2954]ནི་ཉམས་ཉེས༌[^2955]བྱུང༌[^2956]ཞེས་པའོ། །

[Block 4561]
དེ་བས་གཉེན་བཤེས་དང་ཡང་བྲལ། །ཞེས་བྱ་བ་འདིས་ནི་རྗེས་སུ་འབྲང་བ་མེད་པས་སྙིང་རྗེའི་གནས་སུ་སྟོན་ཏོ། །

[Block 4562]
ཉམས་ཉེས༌[^2957]ཆེན་པོ། ཞེས་བྱ་བ་འདིས་ནི་སྡུག་བསྔལ་ཉིད་དུ་སྟོན་ཏོ། །

[Block 4563 [VERSE]]
སྤྲེའུ་ཚོགས་མང་པོའི་མགོན་པོ་ཁྱོད། །
བདག་གི་སྐྱབས༌[^2958]ཀྱང་མཛད་དུ་གསོལ། །

[Block 4564]
ཞེས་བྱ་བ་འདིས་ནི་སྐྱབས་སུ་འགྲོ་བར་གསོལ་བ་འདེབས་པའོ། །

[Block 4565]
རྒྱུ་གསུམ་པོ་འདི་ཐམས་ཅད་ཀྱིས་ཀྱང་སྙིང་རྗེའི་གནས་ཉིད་དུ་སྟོན་ཏེ། ཕོངས་པ་དང་། སྡུག་བསྔལ་བ་དང་། རྗེས་སུ་འབྲང་བ་མེད་པས་སོ། །

[Block 4566]
སྙིང་རྗེ་ཆེན་པོ་ཞེས་བྱ་བ་ནི་སྔར་བསྟན་པའི་སྙིང་རྗེའི་གནས་ཐམས་ཅད་ཀྱིས་སོ། །

[Block 4567]
ཉམས་ཉེས༌[^2959]གྱུར་ཅིང་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ཀྱང་སྔར་བསྟན་པའི་སྙིང་རྗེའི་གནས་ཀྱི་རྒྱུ་གསུམ་བསྟན་པ་ཡིན་ནོ། །

[Block 4568]
ཉམས་ཉེས༌[^2960]གྱུར་ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་དང་ལྡན་པ་ཉིད་དུ་གྱུར་པའོ། །

[Block 4569]
གཉེན་བཤེས་རྣམས་དང་བྲལ་ཞེས་བྱ་བ་འདིས་ནི་རྗེས་སུ་འབྲང་བ་མེད་པ་ཉིད་དོ། །

[Block 4570]
ཐལ་མོ་སྦྱར་ནས་དམན་པས་གསོལ་བ༌[^2961]ནི། ཞེས་བྱ་བས་ནི་སྐྱབས་སུ་འགྲོ་བར་གསོལ་བ་དོན་དུ་གཉེར་བའོ།[^2962] །བརྩེ་བ་གཡེལ་བར་གྱུར་ཅེས་བྱ་བ་ནི་བརྟན་པ༌[^2963]ཉམས་པར་གྱུར་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4571]
དེ་ལྟ་བུའི་དུས་ན་དཀོན་པ་ཞེས་བྱ་བ་ནི་རྗེས་སུ་འབྲེང་བར༌[^2964]ཐམས་ཅད་ཀྱང་འཆི་བའི་དུས་ན་གན་དུ་འོང་བ་ནི་དཀོན་པའོ། །

[Block 4572]
ཚིག་འཇམ་པོས་ཞེས་བྱ་བ་ནི་བདག་ཉིད་ཀྱིས་ཡོངས་སུ་བསྐྱབ་པའི་ཡོན་ཏན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4573]
གཡང་སར་ལྷུང་བས་ཞེས་བྱ་བའི་ཚིགས་བཅད་འདིས་ཀྱང་སྔར་བསྟན་པའི་སྙིང་རྗེའི་རྒྱུ་གསུམ་སྟོན་ཏེ། དེ་ཡོངས་སུ་བསྐྱབ་ཅིང་བདེ་བར་འགྱུར་རོ་ཞེས་ཤེས་པར་བྱ་བའི་ཕྱིར་རོ། །

[Block 4574]
གཡང་སར་ལྷུང་བས་བདག་ནི་མཐུ་མེད་ཅིང་། །[^2965]ཞེས་བྱ་བ་འདིས་ནི་སྡུག་བསྔལ་ཅན་དུ་བསྟན་ཏོ། །

[Block 4575]
གཉེན་བཤེས་མེད་ཅེས་བྱ་བ་འདིས་ནི་རྗེས་སུ་འབྲང་བ་མེད་པ་ཉིད་དོ། །

[Block 4576]
མ་འཇིགས་ཤིག་ཅེས་བྱ་བ་ནི་སྐྱབས་འདོད་པ་སྟེ་སྐྱབས་སྒྲུབ་པར་བསྟན་ཏོ། །

[Block 4577]
རང་གི་ལུས་ལས་སྙིང་པོ་དག །ཅེས་བྱ་བ་ནི་སྙིང་པོ་མེད་པའི་ལུས་ལས་གཞན་གྱི་དོན་སྒྲུབ་པའི་སྙིང་པོའོ། །

[Block 4578]
དེ་བསྟན་པའི་ཕྱིར། སྒྲུབ་པར་བྱེད་པའི་སྙིང་པོ་དག །ཅེས་བྱ་བ་སྨོས་སོ། །

[Block 4579]
སྙིང་པོ་མེད་པ་ཞེས་བྱ་བ་ནི་ཆུ་ཤིང་གི་ཕུང་པོ་བཞིན་དུའོ། །

[Block 4580]
ཡང་ན་རྟག་པ་དང་། བདེ་བ་དང་། བདག་དང་། གཙང་བ་མེད་པའོ། །

[Block 4581]
རབ་ཏུ་ལྕི་བའི་ཁུར་གྱིས་ནོན་བཞིན་ཡང་། །ཞེས་བྱ་བ་ནི་སྡུག་བསྔལ་བར་གྱུར་ཀྱང་སྙིང་སྟོབས་ཆེ་བས་བརྟན་པ༌[^2966]མ་ཉམས་པའི་ཕྱིར་སྟེང་དུ་ཕྱིན་ཏོ། །

[Block 4582]
རབ་ཏུ་དགའ་བར་གྱུར་ཅེས་བྱ་བ་ནི་སེམས་ཀྱི་མི་དགའ་བ་མེད་པར་སྟོན་ཏོ། །

[Block 4583]
འདི་ལྟར་སྙིང་སྟོབས་ཆེ་བས་བརྟན་པ་མ་ཉམས་པར་ཞེས་བྱ་བ་ཡིན་ཏེ། དེ་བས་ན་དེའོ། །

[Block 4584]
ངལ་ཞིང་ཆད་པས་གོམས་པ༌[^2967]འཁྱོར་ཞིང་འདོར། །ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ཡོངས་སུ་ངལ་བ་ཡོད་པ་ཡིན་ཏེ། གང་གི་ཕྱིར་ཡང་རབ་ཏུ་ལྕི་བའི་ཁུར་གྱིས་ནོན་བཞིན་ཞེས་བྱ་བ་སྟེ་ལྕི་བའི་རྒྱུ་དེས་སོ། །

[Block 4585]
ངལ་བ་སོས་པར་བྱ་ཕྱིར་ཞེས་བྱ་བ་ནི་ལུས་ཀྱི་ངལ་བ༌[^2968]མེད་པར་བྱ་བའི་ཕྱིར་རོ།[^2969] །རང་བཞིན་ཡོངས་སུ་དག་པ་ཞེས་བྱ་བ་ནི་བདག་གི་རང་བཞིན་ཡོངས་སུ་དག་པས། གཞན་གྱི་བསམ་པ་ཡོངས་སུ་དག་པར་འཛིན་པའི་ཕྱིར་རོ། །

[Block 4586]
དེས་ཞེས་བྱ་བ་ནི་ཕན་གདགས་པའི་ཕྱིར། དོགས་པ་མེད་པའི་རྒྱུ་བསྟན་ཏོ། །

[Block 4587]
མི་ཞེས་བྱ་བ་འདིས་ནི་སྐལ་བ་མི་མཉམ་པ་ཡིན་པས། དོགས་པའི་གནས་ཉིད་དུ་བསྟན་ཏོ། །

[Block 4588]
ཡང་ན་རང་བཞིན་ཡོངས་སུ་དག་པ་དེས། ཉེས་པ་བྱས་པ༌[^2970]དོགས་པ་མེད་པ་སྟེ།

[Block 4589 [VERSE]]
ཕན་གདགས་པའི་ཕྱིར་ཡང་བག་ཕབ་པའོ། །
གཅན་གཟན་ཁྲོ་བོ་ཐགས་ཐོགས་མེད་པར་འོང་། །

[Block 4590]
ཞེས་བྱ་བ་ལ། གཅན་གཟན་ཁྲོ་བོ་འོང་བ་ནི་འབྱུང་བ་སྟེ། ནགས་ཀྱི་ཕྱོགས་སུ་འཇུག་པའི་ཕྱིར་རོ། །
--- END BLOCKS ---
