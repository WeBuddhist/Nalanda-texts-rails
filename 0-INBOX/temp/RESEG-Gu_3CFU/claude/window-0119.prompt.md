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
[Block 4166]
གང་ཞིག་སྲིན་བལ་གྱི་སྤང་བ་ཞེ་ན། དེའི་ཕྱིར་སྲིན་བལ་གྱི་ལས་བྱས་སམ་བྱེད་དུ་བཅུག་ནའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བྱས་པ་འམ་བྱེད་དུ་བཅུག་པ་ལ་སྲིན་བལ་གྱི་གདིང་བ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4167]
ཐམས་ཅད་པ་འམ་སོ་སོ་བ་བྱས་པ་འམ་བྱེད་དུ་བཅུག་པ་དག་ལ་ཉེས་པ་དང་ལྡན་པ་ཉིད་དོ། །

[Block 4168]
གང་ཞིག་གནས་པ་ལ་མཐར་ཐུག་པས་འཁོར་གསུམ་གཡོགས་པ་ཉིད་དོ། །

[Block 4169]
དེ་ཉིད་འདི་སྤང་བར་བྱེད་པ་ཉིད་ལ་རྟོགས་པར་བྱའོ།[^2848] །འདི་ཙམ་ཉིད་ཀྱིས་འདིར་ཡང་མཐར་ཐུག་པར་གྱུར་པའི་དོན་ལ་བཀྲམ་པ་ལ་སོགས་པ་སྟེ། གང་ཞིག་མཐར་ཐུག་པའི་གོས་རྙིང་པར་གྱུར་པ་རྣམས་ལ༌[^2849]བརྐུས་ན་ལོངས་སྤྱོད་པ་རྣམས་ནི་བལ་ལས་བྱས་པ་རྣམས་ལ་སྤང་བར་བྱེད་པ་ཉིད་དུ་རྣམ་པར་གནས་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4170]
འདི་རྣམས་ལ་ཐམས་ཅད་ཕྱི་མ་དག་ལ་ཉེས་བྱས་ཉིད་དེ་ཆུང་བ་ལ་ཡང་འདིར་འཇུག་པས་རྗེས་སུ་མཐུན་པ་ཉིད་ཀྱང་བྱི་དོར་ལ་སོགས་པའི་དོན་དེ་ལ་དེ་ཙམ་དུའོ། །

[Block 4171]
སྟན་ལ་ནི་བཀྲམ་པ་ཉིད་བྱེད་པ་མཐར་ཐུག་པའི་དང་པོ་ཉིད་ཡིན་ནོ་ཞེས་བྱ་བ་ལས་གདིང་བ་ཉིད་ཐམས་ཅད་ཀྱི་དང་པོའོ། །

[Block 4172]
འདི་ཙམ་བྱས་པ་ལ་དངོས་གཞི་བསྐྱེད་པའོ། །

[Block 4173]
གཞན་ལ་ཡང་རྩོམ་པ་གཅིག་པར་གྱུར་པ་ཉིད་ཀྱི་ཕྱིར་འདི་ལས་ཐ་མི་དད་པ་ཉིད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 4174]
འདིར་གཞུང་ནི་ཞུ་བའི་ཡི་གེ་ཁ་ཅིག༌[^2850]ལས།

[Block 4175]
ཇི་ཙམ་གྱིས་ན་ལྟུང་བ་རྫོགས་པར་འགྱུར། གང་ཚུན་ཆད་བཀྲམ་པར་གྱུར་ནའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4176]
བྱས་ཟིན་པ་རྙེད་པ་དང་། ཡོངས་སུ་ལོངས་སྤྱོད་པ་དང་། མངོན་པར་འདུ་བྱེད་པ་ལ་ནི་ལྟུང་བ་མེད་དོ་ཞེས་བྱ་བ་ནི་བྱས་ཟིན་པ་རྙེད་པ་དང་། གཞན་གྱིས༌[^2851]བྱས་ཟིན་པ་ལོངས་སྤྱོད་པ་དང་རྙིང་བའི་བྱི་དོར་མངོན་པར་འདུ་བྱེད་པ་དག་ལ་ནི་ལྟུང་བ་མེད་དེ། འདིར་རྗེས་སུ་སྒྲུབ་པ༌[^2852]ལ་ཉེས་པ་དང་ལྡན་པ་ཉིད་དེ། བདག་གིར་བྱེད་པ་དང་ཡོངས་སུ་སྤྱོད་པ་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4177]
ལྡོག་པར་གྱུར་པ་གཞན་ལ་ཡང་མ་ཡིན་ནོ་ཞེས་བྱ་བ་འདི་བསྟན་པའི་ཕྱིར་ལྟུང་བ་མེད་པའི་བསྟན་པ་འདིའོ། །

[Block 4178]
སྲིན་བལ་གྱི་སྤང་བ་རྣམ་པར་འབྱེད་པའོ།། །།

[Block 4179]
ཉུང་ངུ་དང་བསྲེས་པ་ཉིད་ནི་ན་སྨད་པ་ཉིད་དོ་ཞེས་བྱ་བ་ནི། བལ་དཀར་པོ་འམ། ཤ་ནའི་རས༌[^2853]ལ་སོགས་པ་ན་སྨད་པའི་རྫས་རྣམས་དང་འདྲེས་པའི་རས་བལ་གྱི་གདིང་བ་བྱེད་དུ་བཅུག་པ་ལ་ན་སྨད་པ་ཉིད་དེ། ཁ་ན་མ་ཐོ་བ་ཡོངས་སུ་མ་རྫོགས་པ་ཉིད་དེ་ཉེས་བྱས་སུ་འགྱུར་རོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4180]
རྫས་ཀྱི༌[^2854]ཚད་དེ་ལ་མ་སྐྱེས་པ་ཉིད་དེ་གང་གི་ཕྱིར་དངོས་གཞི་ལྡང་བ་ཞེས་བྱ་བའི་དོན་ནི་གདིང་བ་ཐམས་ཅད་ཀྱི་དབང་དུ་བྱེད་པ་འདི་ཁྱད་པར་ཡོངས་སུ་མ་བཟུང་བས་རྟོགས་པར་བྱའོ། །

[Block 4181]
རྫས་ཉམས་པ་ཉིད་ལ་ཡང་ངོ་ཞེས་བྱ་བ་ལ་ཡང་ངོ་ཞེས་བྱ་བའི་སྒྲས༌[^2855]ནི་ན་སྨད་པ༌[^2856]ཉིད་དོ་ཞེས་བྱ་བའི་རྗེས་སུ་སྙེགས༌[^2857]པར་བྱེད་དོ། །

[Block 4182]
འདིར་གཞུང་ནི། རེ་ཞིག་བཙུན་པ་དགེ་སློང་ཉམས་པའི་རས་བལ་གྱི་གདིང་བ་བྱེད་དུ་བཅུག་ན་ཅིར་འགྱུར། ཉེས་བྱས་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 4183]
འདྲ་བ་ཉིད་ཀྱི་ཕྱིར་ཐམས་ཅད་དུ་བལ་གྱིས་བྱས་པ་ལ་སོགས་པས་ཞེས་བྱ་བའོ། །

[Block 4184]
སྲིན་བལ་གྱི་སྤང་བ༌[^2858]ཞུ་བའོ།། །།

[Block 4185]
བལ་ནག་པོ་འབའ་ཞིག་གི་སྤང་བའི་ཆོ་ག་འདི་ཉིད་དོ་ཞེས་བྱ་བ་ཁས་བླངས་ནས་སྲིན་བལ་ཞེས་བྱ་བ་དེའི་གནས་སུ་བལ་ནག་པོ་འབའ་ཞིག་པའི་མིང་གཞན་བརྗོད་པར་བྱ་སྟེ། དེའི་ཕྱིར་ལུག་གི་བལ་ནག་པོ་འབའ་ཞིག་དག་གོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4186]
བྱས་པ་བྱེད་དུ་བཅུག་པ་དག་གི་གདིང་བ་ཞེས་བྱ་བ་དང་སྦྱར་བར་བྱའོ།། །།

[Block 4187]
ཅི་ཞིག་གིས༌[^2859]བལ་ནག་པོར་གྱུར་པ་ཡིན་ནོ།[^2860] །རང་བཞིན་གྱིས་སམ་ཁ་སྒྱུར་བས༌[^2861]སམ་གཉིས་ཀས་སམ་ཞེ་ན། དེའི་ཕྱིར་རང་བཞིན་གྱིས་སོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 4188]
གཞན་གྱིས་ནི་མ་ཡིན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4189]
སྔོན་པོ་དང་འདམ་ཁ་དང་ཁམ་པ་དག་ཀྱང་དེ་ཉིད་དོ་ཞེས་བྱ་བ་ནི་སྔོན་པོ་ལ་སོགས་པ་རྣམས་ཀྱི་བར་དུ་དེ་ཉིད་བལ་ནག་པོ་འབའ་ཞིག་དང་འདྲ་བར་རིག་པར་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4190]
བལ་ནག་པོ་འབའ་ཞིག་གི་སྤང་བའོ།། །།

[Block 4191]
དམན་པ་དང་བལ་ནག་པོའི་རྫས་བསྲེས་པ་དེ་ལས་སྟན་བྱེད་ན་ཉེས་བྱས་སུ་ཐལ་བར་འགྱུར་བ་བསལ་བའི༌[^2862]ཕྱིར་ཆ་གཉིས༌[^2863]བསྲེ་བའི་སྤང་བ་བཅའ་བ་མཛད་དོ། །

[Block 4192]
འདིར་ཡང་སྔར་བསྟན་པའི་ཆོ་ག་ཁས་བླངས་ནས་ཚད་ཀྱི་བྱེ་བྲག་འབའ་ཞིག་ཙམ་བརྗོད་པར་བྱ་སྟེ། དེ་དག་ཕྱེད་པས་ལྷག་པ་ཉིད་ནའོ་ཞེས་བྱ་བ་ནི་ལུག་གི་བལ་ནག་པོ་དེ་དག་ཕྱེད་ཀྱི་ཚད་ལས་ལྷག་པ་ཉིད་ན་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 4193]
གང་གི་ཚེ་དཀར་པོ་དང་། འཁོབ་བལ་དག་ནི་ལྷག་པར་གྱུར་ལ་ལུག་གི་བལ་ནག་པོ་དག་ནི་ཉུང་བ་འམ་མཉམ་པར་གྱུར་ན་ནི་དེའི་ཚེ་ལྟུང་བ་མེད་དོ། །

[Block 4194]
ཕྱེད་དཀར་པོ་དང་འཁོབ་བལ་དག་ལས་ཆ་མཉམ་པ་ཉིད་དུའོ་ཞེས་བྱ་བ་ལ། ཕྱེད་ལ་ཞེས་བྱ་བ་འདི་རྣམས་ཀྱི་ཕྱེད་ལ་འདིར་ཆ་མཉམ་པ་ཉིད་དེ། དཀར་པོ་དང་འཁོབ་བལ་དག་གི་དཀར་པོ་རྣམས་ལ་འདིར་ཤིན་ཏུ་རྒྱ་ཆེ་བ་ཉིད་དེ། དེ་རྣམས་ལ་མི་འཕེལ་བའི་དོན་དུ་ཚིག་འདི་ཡིན་གྱི་འཁོབ་བལ་དག་ལ་ནི་མ་ཡིན་ནོ། །

[Block 4195]
གང་གི་ཕྱིར་འདི་རྣམས་ཀྱི་འཕེལ་བ་ནི་ཉེས་པ་མེད་པ་སྟེ། འདིར༌[^2864]དཀར་པོ་རྣམས་འཕེལ་བ་དང་བཅས་པ་འདི་ལ་དུས་ཀྱི་འཕེལ་བ་ཉིད་སྤང་བར་བྱ་བ་ཉིད་དམ་གཅིག་པ་ཉིད་ལ་ཡང་འདི་ལ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 4196]
སྲིན་བལ་ལས་བྱས་པ་ལ་ཡང་རྫས་གཞན་གྱིས་བསྒྲུབ་པར་བྱ་བའི་ན་སྨད་པ་འདི་ཙམ་ལ་སྤང་བ་ཉིད་དོ། །

[Block 4197]
ན་སྨད་པའི་སྟན་ལ་ཉེས་བྱས་ཞེས་བྱ་བ་འདིའི་རྗེས་སུ་འབྲངས་པས་རྟོགས་པར་བྱའོ། །

[Block 4198]
ཤིན་ཏུ་རྙེད་པར་དཀའ་བ་ཉིད་ཀྱི་ཕྱིར་དང་། འདི་ནི་འདི་བས་ཤིན་ཏུ་རིན་ཐང་ཆེ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 4199]
ཅིའི་ཕྱིར་སླར་འདི་ལ་གསུངས་ཏེ། ཆུང་བ་ལ་ཡང་འདི་ལས་གདིང་བ་སྦྱིན་པར་བྱ་བ་མ་ཡིན་པ་ཉིད་ཀྱི་ཕྱིར་ཆུང་བ་ལ་ཡང་འདི་ལས༌[^2865]གདིང་བ་ལ་ཡང་གླེང་གཞི་ལས་འདི་ཉིད་ཀྱི་ཕྱིར་གང་དུ་རས་བལ་རྣམས་ནི་རྙེད་པར་དཀའ་བ་དང་། རིན་ཐང་ཆེ་བ་ཉིད་དེ༌[^2866]བལ་ནག་པོ་འདི་རྣམས་དང་དཀར་བ་དེ་ཅི་ཞིག་རྟོགས་པར་བྱ་བ་ཞེ་ན། རས་བལ་ལ༌[^2867]ནི་ལྟུང་བ་མེད་པའོ། །

[Block 4200]
བལ་གྱིས༌[^2868]བྱས་པ་ལ་ནི་ལྟུང་བས་དེ་ཡང་རས་བལ་ལས་བྱས་པ་ལ་ནི་ལྟུང་བ་མེད་པའོ། །

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
--- END BLOCKS ---
