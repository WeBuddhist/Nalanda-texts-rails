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
[Block 3676]
དེ་དག་ཏུ་སྐྱེ། ལྷའི་རིས་དེ༌[^2098]དག་ཏུ་གྲངས་བཞིན་ཏེ། དེ་དག་ཀྱང་མྱུར་བ་ཉིད་དུ་སྐྱེའོ། །

[Block 3677]
གཟུགས་ཅན་རྣམས། ཀུན་རྫོགས་གོས་དང་བཅས་པ་ཉིད། །གཟུགས་ན་སྤྱོད་པའི་ལྷ་རྣམས་ནི་ལུས་ཀུན་རྫོགས་པ་དང་གོས་གྱོན་བཞིན་དུ་སྐྱེའོ། །

[Block 3678]
ལྷ་ཐམས་ཅད་ཀྱང་འཕགས་པའི་སྐད་དུ་སྨྲའོ། །

[Block 3679 [HEADING]]
##### འདོད་པ་སྐྱེ་བ་གསུམ། ^3-2-1-16-0

[Block 3680]
དེ་ལ་འདོད་པ་སྐྱེ་བ་གསུམ་པོ་ནི། །

[Block 3681]
འདོད་པའི་ལྷ་དང་མིར་བཅས་རྣམས། །འདོད་པའི་ཁམས་སུ་རིག་པར་བྱ་སྟེ། ཇི་ལྟ་ཞེ་ན་སེམས་ཅན་འདོད་པ་ཉེ་བར་གནས་པ་རྣམས་འདོད་པ་ཉེ་བར་གནས་པ་དག་ལ་དབང་ཕྱུག་གིས༌[^2099]དབང་བྱེད་པ་དག་ཀྱང་ཡོད་དེ། འདི་ལྟ་སྟེ་མི་རྣམས་དང་ལྷ་ཁ་ཅིག་གོ། །

[Block 3682]
དེ་དག་ཀྱང་ལྷའི་རིས་བཞི་རྣམས་སོ། །

[Block 3683]
སེམས་ཅན་འདོད་པ་སྤྲུལ་པ་རྣམས་འདོད་པ་རྣམས༌[^2100]སྤྲུལ་ཞིང་དབང་ཕྱུག་གིས༌[^2101]དབང་བྱེད་པ་དག་ཀྱང་ཡོད་དེ། [^2102]དཔེར་ན་འཕྲུལ་དགའི་ལྷ་རྣམས་ལྟ་བུའོ། །

[Block 3684]
སེམས་ཅན་འདོད་པ་གཞན་གྱིས་སྤྲུལ་པ་རྣམས་འདོད་པ་གཞན་གྱིས་སྤྲུལ་པ་དག་ལ་དབང་ཕྱུག་གིས༌[^2103]དབང་བྱེད་པ་དག་ཀྱང་ཡོད་དེ། འདི་ལྟ་སྟེ། གཞན་འཕྲུལ་དབང་བྱེད་ཀྱི་ལྷ་རྣམས་སོ། །

[Block 3685]
དེ་དག་ནི་ཇི་ལྟར་བྱུང་བ་ལ༌[^2104]ཡོངས་སུ་ལོངས་སྤྱོད་པ་ཉིད་ཀྱི་ཕྱིར་དང་། ཇི་ལྟར་འདོད་པ་བཞིན་བདག་ཉིད་ཀྱིས་སྤྲུལ་པ་ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པ་ཉིད་ཀྱི་ཕྱིར་དང་། ཇི་ལྟར་འདོད་པ་བཞིན་བདག་དང་གཞན་གྱིས་སྤྲུལ་པ་ལ་ཡོངས་སུ་ལོངས་སྤྱོད་པའི་ཕྱིར་འདོད་པ་སྐྱེ་བ་གསུམ་ཞེས་བྱའོ། །

[Block 3686 [HEADING]]
##### བདེ་བ་སྐྱེ་བ་གསུམ། ^3-2-1-17-0

[Block 3687]
གཟུགས་ཀྱི་ཁམས༌[^2105]ནི།

[Block 3688 [VERSE]]
བདེ་བ་སྐྱེ་བ་གསུམ་པོ་ནི། །
བསམ་གཏན་གསུམ་ལ་ས་དགུ་ཡིན། །

[Block 3689]
བསམ་གཏན་གསུམ་དག་ན་ས་དགུ་པོ་གང་དག་ཡིན་པ་དེ་དག་ནི་བདེ་བ་སྐྱེ་བ་གསུམ་ཡིན་ཏེ། ལྷ་དེ་དག་ནི་དབེན་པ་ལས་སྐྱེས་པ་དང་། ཏིང་ངེ་འཛིན་ལས་སྐྱེས་པའི་དགའ་བའི་བདེ་བ་དང་། དགའ་བ་མེད་པའི་བདེ་བས་བདེ་བར་གནས་པ་ན་ཡུན་རིང་མོ་ཞིག་ཏུ་གནས་ཏེ། དེའི་ཕྱིར་བདེ་བ་སྐྱེ་བ་དེ་དག་ནི་སྡུག་བསྔལ་བ་མེད་པ་དང་། ཡུན་རིང་པོར༌[^2106]བདེ་བའི་ཕྱིར་བདེ་བ་སྐྱེ་བ་དག་ཡིན་ནོ། །

[Block 3690]
བསམ་གཏན་ཁྱད་པར་ཅན་དུ་སྐྱེས་པ་ལ་ནི་དགའ་བ་དང༌[^2107]བདེ་བ་མེད་པའི་ཕྱིར་བདེ་བ་སྐྱེ་བ་ཉིད་དཔྱད་པར་བྱའོ། །

[Block 3691 [HEADING]]
##### ལྷ་རྣམས་ཀྱི་གནས་ཀྱི་ཐག། ^3-2-1-18-0

[Block 3692]
གང་དག་ལྷ་རྣམས་ཀྱི་གནས་ཉི་ཤུ་རྩ་གཉིས་བཤད་པ་དེ་དག་ལ་འོག་མ་ནས་གོང་མར་ཐག་ཇི་སྲིད་ཅེ་ན། དེ་དག༌[^2108]ཐམས་ཅད་དཔག་ཚད་ཀྱི་གྲངས་ཀྱིས༌[^2109]བགྲང་བར་ནི་སླ་བ་མ་ཡིན་མོད་གྱི་འོན་ཀྱང་།

[Block 3693 [VERSE]]
གནས་དང་གནས་འོག་ཇི་སྲིད་པ། །
དེ་ནས་དེ་ཡི་གོང་དེ་སྲིད། །

[Block 3694]
འཛམ་བུའི་གླིང་ནས་བཟུང་སྟེ་གོང་མའི་གནས་གང་ཡིན་པ་དེ༌[^2110]ནི་དེ་ནས་འོག་མ་འཛམ་བུའི་གླིང་དུ་ཇི་སྲིད་པར་དེ་ནས་གོང་མའི་གནས་གཞན་དུ་ཡང་དེ་སྲིད་དེ། འདི་ལྟ་སྟེ། འདི་ནས་དཔག་ཚད་བཞི་ཁྲི་ན་རྒྱལ་པོ་ཆེན་པོ་བཞིའི་རྩ་བའི་གནས་བང་རིམ་བཞི་པ་ཡོད་པ་དེ་ནས་འོག་མ་འཛམ་བུའི་གླིང་དུ། ཇི་སྲིད་པར་གོང་མ་སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས་ཀྱི་གནས་སུ་ཡང་དེ་སྲིད་དོ། །

[Block 3695]
དེ་ནས་ཀྱང་འོག་མ་འཛམ་བུའི་གླིང་དུ་ཇི་སྲིད་པར་གོང་མ་འཐབ་བྲལ་བ་རྣམས་ཀྱི་གནས་སུ་ཡང་དེ་སྲིད་དོ། །

[Block 3696]
དེ་ནས་ཀྱང་འོག་མ་འཛམ་བུའི་གླིང་དུ་ཇི་སྲིད་པར་གོང་མ་དགའ་ལྡན་པ་རྣམས་ཀྱི་གནས་སུ་ཡང་དེ་སྲིད་དོ། །

[Block 3697]
དེ་བཞིན་དུ་རྒྱས་པར་ཐམས་ཅད་གོ་རིམས་དང་མཐུན་པར་བྱ་སྟེ། ཤིན་དུ་མཐོང་བ་དག་ནས་འོག་མ་འཛམ་བུའི་གླིང་དུ་ཇི་སྲིད་པར་གོང་མ་འོག་མིན་པ་རྣམས་ཀྱི་གནས་སུ་ཡང་དེ་སྲིད་དོ། །

[Block 3698]
དེའི་གོང་ན་ནི་གནས་མེད་དོ། །

[Block 3699]
དེ་ཉིད་ཀྱི་ཕྱིར་དེ་དག་ནི༌[^2111]ཐུ་བོར་གྱུར་པའི་ཕྱིར་འོག་མིན་ཞེས་བྱའོ། །

[Block 3700]
གཞན་དག་ན་རེ་ཐོག་མཐའ༌[^2112]ཞེས་བྱ་སྟེ། ཐོགས་པ་ནི་བསགས་པར་གནས་པའི་གཟུགས་ཏེ། དེ་ནི་འདིར་མཐར་ཐུག་གོ་ཞེས་ཟེར་རོ།[^2113] །ཡང་ཅི་གནས་འོག་མར་སྐྱེས་པ་རྣམས་གོང་མའི་གཞལ་མེད་ཁང་དུ་དོང་ནས་མཐོང་བར་འགྱུར་རམ་ཞེ་ན།

[Block 3701 [VERSE]]
རྫུ་འཕྲུལ་གཞན་བརྟེན༌[^2114]མ་གཏོགས༌[^2115]པར། །
དེ་དག་གོང་མ་མཐོང་བ་མེད། །

[Block 3702]
རྫུ་འཕྲུལ་གྱིས་སམ། གཞན་ལ་བརྟེན་ནས་ཏེ། རྫུ་འཕྲུལ་དང་ལྡན་པའམ། དེ་ན་གནས་པའི་ལྷས་ཁྲིད་པར་གྱུར་ན་སུམ་ཅུ་རྩ་གསུམ་པ་རྣམས་འཐབ་བྲལ་བའི་ནང་དུ་འགྲོ་བར་འགྱུར་ཏེ། ལྷག་མ་རྣམས་ཀྱང་དེ་དང་འདྲའོ། །

[Block 3703]
གོང་དུ་སྐྱེས་པ་འོངས་པ་མཐོང་བར་འགྱུར་གྱི། ཁམས་གོང་མ་པ་ཡང་མ་ཡིན་ལ། ས་གོང་མ་པ་ཡང་མ་ཡིན་ཏེ། དཔེར་ན་ཡུལ་མ་ཡིན་པའི་ཕྱིར་རེག་བྱ་རེག་པར་མི་འགྱུར་བ་བཞིན་ནོ། །

[Block 3704]
དེ་ཉིད་ཀྱི་ཕྱིར་རང་གི་ལུས་ཀྱིས་མི་འོང་ངོ་། །འོ་ན་ཇི་ལྟ་བུ་ཞེ་ན། ས་འོག་མའི་སྤྲུལ་པས་སོ། །

[Block 3705]
སྡེ་པ་གཞན་དག་ན་རེ། དེའི་འདོད་པས་འདི་ན་འཁོད་པ་བཞིན་དུ་མཐོང་བར་འགྱུར་རོ་ཞེས་ཟེར་རོ། །

[Block 3706]
ཡང་འཐབ་བྲལ་བ་ལ༌[^2116]སོགས་པའི་གཞལ་མེད་ཁང་དེ་དག་གི་ཚད་ཇི་ཙམ་ཞེ་ན། རེ་ཞིག་ཁ་ཅིག་ན་རེ་བཞི་རྣམས་ཀྱིས་ནི་རི་རབ་ཀྱི་རྩེ་མོ༌[^2117]དེ་ཙམ་མོ་ཞེས་ཟེར་རོ། །

[Block 3707]
གཞན་དག་ན་རེ་གོང་མ་གཉིས་འགྱུར༌[^2118]རོ་ཞེས་ཟེར་རོ། །

[Block 3708]
ཁ་ཅིག་ན་རེ་བསམ་གཏན་དང་པོའི་ནི་གླིང་བཞི་པ་ཙམ་མོ། །

[Block 3709]
གཉིས་པའི་ནི་སྟོང་ཆུང་ངུའི་འཇིག་རྟེན་གྱི་ཁམས་ཙམ་མོ། །

[Block 3710]
གསུམ་པའི་ནི་སྟོང་གཉིས་པ་ཙམ་མོ། །

[Block 3711]
བཞི་པའི་ནི་སྟོང་གསུམ་པ་ཙམ་མོ་ཞེས་ཟེར་རོ། །

[Block 3712]
གཞན་དག་ན་རེ་དང་པོ་ལ་སོགས་པ་ནི་སྟོང་ལ་སོགས་པའི་ཚད་ཙམ་མོ། །

[Block 3713]
བཞི་པ་ནི་ཚད་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 3714 [HEADING]]
##### སྟོང་ཆུང་ངུ་དང་སྟོང་གཉིས་པ་དང་སྟོང་གསུམ། ^3-2-1-19-0

[Block 3715]
ཡང་སྟོང་ཆུང་ངུའི་འཇིག་རྟེན་གྱི་ཁམས་འདི་ཅི། སྟོང་གཉིས་པ་འམ། སྟོང་གསུམ༌[^2119]པ་ནི་ཅི་ཞེ་ན།
--- END BLOCKS ---
