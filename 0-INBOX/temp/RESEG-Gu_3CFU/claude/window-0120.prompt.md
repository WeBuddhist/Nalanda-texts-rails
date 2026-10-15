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
[Block 4201]
བལ་ནག་པོ་འབའ་ཞིག་ལ་ལྟུང་བ་མེད་དེ། དཀར་པོ་ལ་ནི་ལྟུང་བ་ཡོད་དོ་ཞེས་བྱ་བ་གོ་བཟློག་ནས་བརྗོད་དེ་འདིར་རྫས་ཀྱི་སྙིང་པོ་ཉིད༌[^2869]ཀྱི་གཙོ་བོ་ཅན་རྙེད་པར་དཀའ་བ་དང་། རིན་ཐང་ཆེ་བ་ཉིད་ཀྱི་ཚིག་རྣམ་པར་གནས་པ་ཡིན་གྱི་རྒྱ་ཆེ་བ་ལ་རྟོགས་པར་བྱ་བ་ཞེས་བྱ་བ་འདི་ལ་འདིར་ཁས་ཟས༌[^2870]གྱ་ནོམ་པར་བསྒོ་བར༌[^2871]བྱེད་པ་ལྟར་དོན་རྣམ་པར་གཞག་པས་སོ། །

[Block 4202]
ལུག་གི་བལ་དཀར་པོ་ནི༌[^2872]གང་ཡིན་འཁོབ་བལ་ནི༌[^2873]གང་ཡིན་ཞེ་ན་དེའི་ཕྱིར་གློ་དང་རྒྱབ་དང་གཉའ་བར་སྐྱེས་པ་ནི་སྔ་མའོ་ཞེས་བྱ་བ་ནི་གློ་དང་གཉིས་ལྡན་གྱིས་བསྡུ་བ་གཅིག་པའི་དངོས་པོའོ། །

[Block 4203]
སྔ་མ་ཞེས་བྱ་བ་ནི་དཀར་བའོ། །

[Block 4204]
མགོ་དང་། རྐང་པ་དང་། ལྟོ་བ་ནས་སྐྱེས་པ་ནི་ཕྱི་མའོ་ཞེས་བྱ་བ་ནི་འཁོབ་བལ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4205]
ཆ་གཉིས་བསྲེ་བའི་སྤང་བའོ། །

[Block 4206]
[^2874]མ་དག་པ་ནི་གསོལ་བར་མི་བྱའོ། །

[Block 4207]
རང་དག་རྟོག་ཏུ་འདོད་པར༌[^2875]བྱའོ། །

[Block 4208]
ཡང་ན་དགེ་སློང་བསྐོས་པ་དག་གོ་ཞེས་བྱ་བ་བཤད་ཟིན་ཏོ་ཞེས་བྱ་བ་དེ་ལ་སོ་སོར་བརྟགས་ནས་གང་ཞིག་གདིང་བའི་བྱ་བ་དེ་བརྗོད་པར་བྱ་སྟེ། ཆུ་དང་ཞེང་གཉིས་ཀར་ལྷག་པ་ཉིད་ཡིན་ན་གཅད་པར༌[^2876]བྱའོ། །

[Block 4209]
ཇི་སྐད་བཤད་པའི་ཚད་ལས་གལ་ཏེ་རིང་བ་དང་ཞེང་གདིང་བ་ལས་ལྷག་པར་གྱུར་ན་དེ་དག་ནི་གཅད༌[^2877]པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4210]
ཐུང་བ་ཉིད་དང་དོག་པ་ཉིད་དག་ནི་བསྐྱེད་པར་བྱའོ་ཞེས་བྱ་བ་ནི། ཅི་སྟེ་ཐུང་བ་དང་དོག་པར་གྱུར་ན་དེ་ནས་བསྐྱེད་པར་བྱའོ། །

[Block 4211]
རལ་ན་བཙེམ་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བརྟེན་པ་ལ་སོགས་པའོ། །

[Block 4212]
བུག་རྡོལ་དུ་གྱུར་ཏམ་ཤ་ཟད་པ་དག་ནི་སྦྱར་བར་བྱའོ་ཞེས་བྱ་བ་ནི། བུག་རྡོལ་དུ་གྱུར་པའམ་ཤ་ཟད་པ་ནི་མཐུག་པའི་ངོ་བོའི་ཕྱིར་བལ་རྣམས་སྦྱིན་པ་ནི་སྦྱར་བར་བྱའོ། །

[Block 4213]
བཅོས་དཀའ་བ་ཉིད་ཡིན་ན་སྦྱིན་ནོ་ཞེས་བྱ་བ་ནི་གནང་བ་ཞེས་བྱ་བ་དོན་གྱིས་སྨོས་པ་སྟེ། འདི་རྣམས་ལ་ཐབས་ཐམས་ཅད་ཀྱིས་སྦྱིན་པར་བྱ་བ་སོ་སོར་འདུས་བྱས་པའི་ཕྱིར་ནུས་པ་མ་ཡིན་པ་དེའི་ཚེ་སྟན་གཞན་བྱ་བའི་ཕྱིར་གནང་བ་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4214]
འདི་ལྟར་ལག་གི་བླའི་ཕྱིར་གསུངས་པ་ནི་གླེང་གཞིའི་དབང་གི་ཕྱིར་འདི་རྣམ་པར་གནས་པ་ཡིན་གྱི་གཞན་ལ་ཡང་གྲང་བས་རྣམ་པར་འཚེ་བར་འགྱུར་བ་ལ་ཉེ་བར་སྦྱར་དུ་རུང་བའི་ཕྱིར་སྤྱིར་མདོར་བྲིས་སོ། །

[Block 4215]
ཅི་ཞིག་བྱས་ན་ལོ་དྲུག་ཏུ་བཅང་བའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་གནང་བ་མ་ཐོབ་པ་གཞན་ཡོད་པའམ་རང་དགར་བཏང་བས་ལོ་དྲུག་མ་ལོན་པར་སྟན་བྱས་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱས་ཟིན་པ་ཉིད་ལ་གནང་བ་མ་ཐོབ་པ་ལ་གདིང་བ་ལོ་དྲུག་མ་ལོན་པར་དང་པོར་བྱས་ཟིན་པ་ཉིད་ནས་བརྩམས་ཏེ། གང་ལ་ཡོངས་སུ་རྫོགས་པ་དེར་གདིང་བ་གཞན་ཡོད་པ་ལ་རང་དགར་བཏང་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4216]
བརྩམས་པ༌[^2878]ཉིད་ནི་རྩོམ་པ་ཟིན་པ་དང་འདྲའོ་ཞེས་བྱ་བ༌[^2879]རྩོམ་པ་གཞན་ལ་ཟིན་པ་དང་འདྲ་བར་ཇི་ལྟར་ཉིད་དུ་མཐར་ཐུག་པ་ཡོད་པ་ལ་བྱ་བ་གཞན་ལ་ཉེས་བྱས་སུ་འགྱུར་ཏེ། དེ་བཞིན་དུ་རྩོམ་ནའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4217]
དེར་ཡོད་པ་ཉིད་ལ་ཡོད་པ་ཉིད༌[^2880]ཡིན་ཏེ། གང་ཞིག་དུས་མཉམ་པ་ལ་དེ་བས་ན་དུས་མཉམ་དུ་འདིས་བརྩམས་པ་ལ་ཉེས་བྱས་མ་བྱས་པ་ཉིད་མ་ཡིན་ཏེ། ལྷན་ཅིག་གམ་ཕྱིས་ཉེས་བྱས་ཉིད་དོ། །

[Block 4218]
སྦྱོར་བ་བྱས་པ་རྩོམ་པ་སྔར་གྱི་མཐར་ཐུག་པ་ལ་ཡང་ལྟུང་བ་མེད་པར་ཤེས་པར་བྱའོ། །

[Block 4219]
མེད་པ་ཉིད་དོན་གྱིས་བྱས་པ་བསྒྲུབ་པ་ཉིད་ཀྱིས་ཉེས་བྱས་བྱས༌[^2881]པ་མ་ཡིན་པའི་སྦྱོར་བ་མཐར་ཐུག་པ་ལ་ནི་འདིར་ལྟུང་བའོ། །

[Block 4220]
དེ་ལ་གང་ཞིག་གིས་ཕྱིས་བརྩམས་པ་ལ་མཐར་འགྲོ་བ་མ་ཡིན་པ་ཉིད་གང་ལ་ཡང་ཕྱིས་མཐར་གྱུར་པ་དེར་འདི་ཡོད་པར་བརྗོད་པར་རྣམ་པར་གནས་པའོ། །

[Block 4221]
མཐར་ཐུག་ན་སྦྱར་བའི་ལྟུང་བར་མི་འགྱུར་བ་ཉིད་མ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་བརྩམས་པ་གཞན་ལ་གང་ཞིག་གཉིས་པ་རྩོམ་པར་བྱེད་པ་ལ་གལ་ཏེ་འདིར་སྔར་ཡོངས་སུ་རྫོགས་པར་གྱུར་ན་དེ་ལ་དངོས་གཞིའི་ལྟུང་བ་འདོད་པ་མ་ཡིན་ཏེ། དེ་ལ་གང་གི་སྔར་ཟིན་པར་བྱེད་ན་དེར་སྦྱོར་བ་ལ་ཡང་ལྟུང་བ་མ་ཡིན་པས་གནས་པར་བྱ་ཞེས་བྱ་བས་གང་ཞིག་འདོད་པ་དེའི་ཕྱིར་མདོ་འདིའོ། །

[Block 4222]
འདི་ནི་འཐད་པ་ཡང་དག་པར་བསྟན་པ་ཡིན་ཏེ། མཐར་འགྲོ་བ་ལ་ནི་སྦྱོར་བ་ལ་ལྟུང་བ་མེད་པར་བྱས་པ་ཉིད་ནི་མ་ཡིན་ཏེ། ལྟུང་བ་མེད་པར་བྱས་པ་ཉིད་དུ་གྱུར་པ་ལ༌[^2882]ཡང་ཡོངས་སུ་བསྒྱུར་བ་སྐྱེས་པ་མ་ཡིན་ནོ། །

[Block 4223]
དེ་བས་ན་འདིར་སྦྱོར་བ་ལ་ལྟུང་བ་མ་ཡིན་པར་བྱས་པ་ཉིད་དུ་རྟོགས་པར༌[^2883]བྱ་བ་མ་ཡིན་ཏེ་ཞེས་བྱ་བ་ནི་འདིའི་ངག་གི་དོན་ཏོ། །

[Block 4224]
རབ་ཏུ་བྱུང་བ་གཞན་གྱི་ནི་ཐ་དད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། སྔོན་དང་ཕྱིས་རབ་ཏུ་བྱུང་བ་དང་རབ་ཏུ་དབྱུང་བ་དག་ལ་རྒྱུན༌[^2884]གཅིག་པ་ཉིད༌[^2885]མ་ཡིན་པ་ཞེས་བྱ་བ་འདི་ཤེས་པར་གྱུར་པའི་དོན་ལ་འདི་རྗེས་སུ་བརྗོད་པའོ། །

[Block 4225]
རབ་ཏུ་བྱུང་བ་གཞན་བྱས་པ་མི་རྩོམ་པའམ༌[^2886]རྙེད་པ་མ་ཡིན་པ་གདིང་བ་ལ་གཞན་རབ་ཏུ་མ་བྱུང་བ་ལ་དུས་འོག་མ་ཡོངས་སུ༌[^2887]རྫོགས་པ་ལ་བྱ་བ་ཉིད་མེད་པ་འདི་བསྟན་པའི་དོན་དུ་གཅིག་བརྩམས་པ་ལ་གཞན་མཐར་ཐུག་པ་ལ་དངོས་གཞི་མེད་པ་ལ་ཇི་ལྟར་ཡང་ཁྱིམ་པའི་གནས་སྐབས་བཞིན་ཏེ། མི་རྩོམ་པ་འམ་ཐོབ་པར་བྱ་བ་ཉིད་མེད་པ་དེ་བཞིན་དུ་འདིར་ཡང་ཞེས་བྱ་བ་རྣམ་པར་གནས་པ་ཡིན་ནོ། །

[Block 4226]
འདིར་གཞུང་ནི་ཞུ་བ་ཁ་ཅིག༌[^2888]ལས་དགེ་སློང་འགའ་ཞིག་ཡོད་དེ། ལོ་དྲུག་གི་མདུན་རོལ་དུ་དེས་གདིང་བ་བྱེད་དུ་བཅུག་ན་ལྟུང་བ་མེད་པར་ཡང་འགྱུར་ལ༌[^2889]ལོ་དྲུག་གི་མདུན་རོལ་དུ་བབས་ཤིང་དེས་སླར་ཡང་བསྙེན་པར་རྫོགས་ནས་སྟན་གཞན་བྱེད་དུ་བཅུག་ན་ལྟུང་བ་མེད་པ་ཡིན་ནོ། །

[Block 4227]
བརྩམས་ཏེ་འབབས་པ་ཡང་དེ་བཞིན་ནོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4228]
ལོ་དྲུག་ཏུ་བཅང་བའི་སྤང་བའོ།། །།

[Block 4229]
ཅི་ཞིག་བྱས་ན་མཐོ་གང་གིས་སྤང་བར་འགྱུར་ཞེ་ན།

[Block 4230]
དེའི་ཕྱིར་གདིང་བ་རྙིང་པ་ལས།

[Block 4231]
བདེ་བར་གཤེགས་པའི་མཐོ་གང་གིས་མ་གླན་པའི་གདིང་བ་སར་པ་སྤྱོད་ནའོ་ཞེས་བྱ་བ་ནི། གདིང་བ་སར་པ་གང་ལ་གདིང་བ་རྙིང་པ་ལས་བདེ་བར་གཤེགས་པའི་མཐོ་གང་གིས་མ་གླན་པ་དེ་ནི་གདིང་བ་ལས་བདེ་བར་གཤེགས་པའི་མཐོ་གང་གིས་མ་གླན་པ་སྟེ། ཡོངས་སུ་ལོངས་མ་སྤྱད་པའི་སར་པ་ཞེས་བྱ་བ་ནི་སར་པ་རྙེད་ཀྱང་རྙེད་པ་བྱས་པ་ལ་ཡང་སྦྱིན་པ་ཉིད་མཐོང་བ་རྫས་རྙིང་པ༌[^2890]ལ་ཡང་འདིར་སྦྱིན་པར་བྱ་བ་ཉིད་དོ། །

[Block 4232]
འདིར་བྱས་པ་ཉིད་ཀྱི་སར་པ་ཉིད་དུ་བརྗོད་དེ་རྫས་ལ་ནི་མ་ཡིན་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4233]
ཅི་མཉམ་པ་ཉིད་ལ་ཡང་གདིང་བ་ལས་ཁྲུ་གང་མ་གླན་པར་སར་པ་ལོངས་སྤྱོད་པ་ལ་ལྟུང་བ་འདི་ཡིན་ནམ་ཞེ་ན། དེའི་ཕྱིར་གལ་ཏེ་དེ་ཡོད་ནའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4234]
ཅི་གལ་ཏེ་རིལ་གྱིས་མི་བདོག༌[^2891]ན་ཡང་། དེའི་ཕྱིར་ལྟུང་བ་འདིར་འགྱུར་རམ་ཞེ་ན། དེའི་ཕྱིར་དེ་ཙམ་ན༌[^2892]ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། གལ་ཏེ་བདེ་བར་གཤེགས་པའི་མཐོ་གང་ཙམ་ཞིག་ཡོད་ན་ཡང་ངོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4235]
ཅི་གལ་ཏེ་སྲ་བ་དེ་ཙམ་ཞིག་ཡོད་ན་འམ་ཞེས། དེའི་ཕྱིར་བཅོས་པར་ནུས་ན་ཡང་ངོ་། །མཐུད་ཅིང་སྦྱར་དུ་རུང་བས་ཀྱང་ངོ༌[^2893]ཞེས་བྱ་བ་ནི༌[^2894]བཅོས་པར་རུང་བ་ཡང་གལ་ཏེ་དེ་ཙམ་དུ་གྱུར་ན་མཐུད་པས་སམ། དམ་དུམ་དུ་སྦྱར་དུ་རུང་ན་དེས་ཀྱང་གཟུང༌[^2895]བར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4236]
དེ་ལྟར་ཡང་མེད་པ་ཉིད་ལ་ལྟུང་བ་མེད་ཅེས་བྱ་བ་འདིར་སྐྱེས་པར་རིག་པར་བྱའོ། །

[Block 4237]
མཐོ་གང་གི་སྤང་བའོ།། །།

[Block 4238]
ཅི་ཞིག་བྱས་ན་བལ་ཐོགས་པའི་སྤང་བར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་ཁྱེར་བ་མེད་ན་དཔག་ཚད་གསུམ་ལས་ལྷག་པར་ལུག་གི་བལ་ཁྱེར་ནའོ། །

[Block 4239]
ཡོད་ན་ཡང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཁྱེར་བ་མེད་ན་དཔག་ཚད་གསུམ་ལས་འདས་པར་ཁུར་བ་ཡོད་པ་ལ་ཁུར་བ་ཉིད་དུ་བརྩམས་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4240]
འགྲོ་བ་ནི་གཉིས་སུ་གསུངས་ཏེ། ལྟུང་བ་དང་བཅས་པ་དང་། ལྟུང་བ་མེད་པའོ། །
--- END BLOCKS ---
