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
[Block 946]
གཅིག་ལ་གཅིག་གམ་གཞན་དག་གིས་ཕན་འདོགས་པ་མེད་པ་ནི་རག་ལུས་པ་མེད་པའི་ཕྱིར་དང་། རག་ལུས་པ་མེད་པ་ཡང་འབྲེལ་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 947]
གལ་ཏེ་ཡང་ཕན་ཚུན་ཕན་འདོགས་པ་མེད་པ་དོན་གཅིག་ལ་འཕྲོད་པ་འདུ་བ་དག་ནི་གཅིག་པོ་དེ་ལ་ཕན་པར་བྱེད་པར་འགྱུར་ལ། མི་འགྱུར་ན་ནི་ཇི་སྐད་དུ་བསྟན་པའི་ཉེས་པར་ཐལ་པའི་ཕྱིར་རོ། །

[Block 948]
དེ་བས་ན་བདག་ཉིད་ལ་ཕན་པ༌[^808]བྱེད་པའི་སྒོ་ནས་བློས་གཞན་ལ་ཡང་སྦྲེལ་ནས་བརྗོད་པ་དེ་བས་ན་དེ་ལ་ཡང་རྒྱུ་དང་འབྲས་བུའི༌[^809]དངོས་པོར་བྱས་པ་ཁོ་ན་རག་ལུས་པ་ཡིན་ནོ། །

[Block 949]
དེ་བས་ན་རྟེན་འདི་ནི་ལྟོས་པ་མེད་པ་རང་གི་བདག་ཉིད་ལ་ཕན་པ་མི་བྱེད་པས། རྟེན་ཞེས་བྱ་བ་ནི༌[^810]དེ་གཡར་པོར་བྱས་པའི་རྒྱན་ལྟ་བུའོ། །

[Block 950]
འོན་ཏེ་དེ་ལྟ༌[^811]ཡིན་ན་ཇི་ལྟར་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་པའི་འཁར་གཞོང་རྒྱ་ཤུག་གི་འབྲས་བུའི་རྟེན་ཡིན་ཞེ་ན།

[Block 951 [VERSE]]
ལྟུང་བ་ཡི་ནི་ཚུལ་ཅན་གྱི། །
འབྲས་སོགས་དེ་ཡུལ་བསྐྱེད་པ་ནི། །
འཁར་གཞོང་ལ་སོགས་ནུས་པ་ཡིན། །

[Block 952]
རྫས་སྤྱིའི་ངོ་བོ༌[^812]ཉིད་ཀྱིས་ཡུལ་མི་འདྲ་བ་ཅན་རྒྱ་ཤུག་གི་འབྲས་བུ་བསྐྱེད་པའི་ཆོས་ཅན་གྱི་ཡུལ་དང་འདྲ་བར་འབྲས་བུ་བསྐྱེད་པ་ཉིད་ནི་རྟེན་གྱི་བྱ་བ༌[^813]ཡིན་པ་དེ་བས་ན། དེའི་སྐད་ཅིག་མ་སྔ་མའི་ལྷན་ཅིག་བྱེད་པའི་འཁར་གཞོང་ནི་དེ་ཉིད་ལ་རྒྱ་ཤུག་གི་འབྲས་བུ་བསྐྱེད་པ་ན་རྟེན༌[^814]ཞེས་བྱའི། གཞན་དུ་ན་འཁར་གཞོང་འདི༌[^815]ལ་རྒྱ་ཤུག་གི་འབྲས་བུ་དག་ཅེས་བྱ་བར་ཡང་མི་འགྱུར་རོ། །

[Block 953]
དེ་ནི་འདིར༌[^816]ཕན་པར་བྱེད་པས་བྱས་པའི་ཐ་སྙད་ནི་མ་ཡིན་ནོ། །

[Block 954]
འོ་ན་ཅི་ཡིན། ལྡན་པ༌[^817]བྱས་ན་ཡིན་ནོ་ཞེ་ན། དེ་དག་ཉིད་ཀྱི་ལྡན་པ་དེ་ཡང་གང་ཡིན། དེ་དག་གིས་བསྐྱེད་པའམ། འཕྲོད་པ་འདུ་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 955]
དེ་གཅིག་ཉིད་ལ་འཕྲོད་པ་འདུ་བས་ཅི་མི་བསྐྱེད་དམ་ཞེ་ན།[^818] དེ་ལ་ནུས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 956]
ཐ་དད་པ༌[^819]ནུས་པ་མེད་པ་དེ་ནི་དེ་ལ་བཅས་པ་ཡིན་དུ་ཟིན་ཀྱང་དེ་འདྲ་བ་ཉིད་ཀྱིས་ཕན་འདོགས་པ་མེད་པའི་ཕྱིར། ལྡན་པས་དེ་དང་ལྡན་པར་མི་འགྱུར་རོ། །

[Block 957]
གཞན་དེ་ལ༌[^820]ཕན་པ་བྱེད་པས་ཁྱད་པར་དུ་འབྱུང་བའི་ཕྱིར་ནུས་པ་ཡིན་ནོ། །

[Block 958]
བསྐྱེད་པར་བྱ་བ་དང་བསྐྱེད་པར་གྱུར་པ་མ་ཡིན་པ་དག་གི་ཕན་པར་བྱེད་པ་འདི་ཡང་ཅི་ཡིན། རང་གི་འབྲས་བུ་གྲུབ་ཟིན་པ་འབྲས་བུ་ཉིད་མ་ཡིན་པའི་ཕྱིར་དང་། གཞན་གྱི་ངོ་བོའི་བྱ་བ་དེ་ལ་ཡང་ཕན་པར་བྱེད་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 959]
བྱེད་པ་མེད་པ་རྣམ་པ་གཉི་ག་ཡང་ཅུང་ཞིག་བྱེད་པ་ཉིད་དུ་ཕན་འདོགས་པ་ཉིད་མེད་པའི་ཕྱིར་རོ་ཞེས་མང་དུ་བསྟན་ཏོ། །

[Block 960]
དེ་བས་ན་དངོས་པོ་ཐམས་ཅད་ཀྱི་འབྲེལ་པ་ཉིད་དག་ནི་བསྐྱེད་པར་བྱ་བ་དང་ཉེ་བར་མཁོ་བའི་ཁྱད་པར་གྱི་དབང་དང་རབ་ཏུ་དབྱེ་བས་རྒྱུ་དང་འབྲས་བུའི་དངོས་པོ་ཡིན་པའི་ཕྱིར། རྣམ་པར་གཞག་པར་བྱའོ། །

[Block 961]
དེའི་ཕྱིར༌[^821]འཁར་གཞོང་ལ་སོགས་པ་དག་ནི་རྟེན་གྱི་ངོ་བོ་ཉིད་ཀྱང་རྒྱ་ཤུག་གི་འབྲས་བུ་ལ་སོགས་པ་བསྐྱེད་པར་ནུས་པ་ཁོ་ན་ཡིན་ན་དེ་ཡང་འདི་ལ་མི་སྲིད་དོ། །

[Block 962]
སྤྱི་ལ་སྐྱེད་པར་བྱེད་པའི་ཁྱད་པར་གྱི་མཚན་ཉིད་ཅན་གྱི་རྟེན་གྱི་ངོ་བོ་སྤྱི་ལ་རྟེན་ནི་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ནི་བསྐྱེད་པར་བྱ་བ་ཉིད་མ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 963]
དེ་མེད་ན་ཡང་གནས་པའི་ཕྱིར། གནས་མིན། འོན་ཀྱང་རྟེན་ནི་སྤྱི་འཇོག་པར་བྱེད་པ་ཡིན་པ་དེ་བས་ན་གནས་པའི་རྒྱུ་ཉིད་ཡིན་པའི་ཕྱིར་རྟེན་ཉིད་ཡིན་གྱི། སྐྱེད་པར་བྱེད་པའི་ཕྱིར་ནི་མ་ཡིན་ནོ། །

[Block 964]
དེ་ཡང་མི་རིགས་ཏེ། དེ་ནི་དེ་མེད་ན་ཡང་གནས་པའི་ཕྱིར་རོ། །

[Block 965]
དངོས་པོ་ལྟུང་བའི་ཆོས་ཅན་དག་གི་ལྟུང་བ་ལ་གེགས་བྱེད་པའི་ཕྱིར་སྐྱེད་པར་བྱེད་པ་མ་ཡིན་དུ་ཟིན་ཀྱང་འཇོག་པར་བྱེད་པ་ཡིན་པར་འགྱུར་རོ། །

[Block 966]
དེ་འདི་ལ་ཡང་གལ་ཏེ་འགའ་ཞིག་གེགས་བྱེད་པ་ལ་བརྒལ་ཞིང་བརྟག་པ༌[^822]མི་བྱེད་ན་འཇོག་པ་པོས་བྱས་པ་ལྟུང་བའི་གེགས༌[^823]བྱེད་པ་དེ༌[^824]ནི་དོན་གཞན་ཉིད་ལ་དོན་གཞན་ཉིད༌[^825]ཡིན་པ་དེ་ཉིད་ལ་འདི་ཉེ་བར་སྦྱོར་བའི་ཕྱིར་ལྟུང་བའི་གེགས༌[^826]བྱེད་པ་ཅི་ཡིན། གེགས་བྱེད་པ༌[^827]ལས་མི་ལྟུང་བ་ཡིན་ན་ཡང་བརྒལ་ཞིང་བརྟག་པ༌[^828]མཚུངས་པ་དང་ཐུག་པ་མེད་པར་འགྱུར་རོ། །

[Block 967]
དེ་བས་ན་ལྟུང་བ་མེད་པ་ནི་ལྟུང་བའི་གེགས་བྱེད་པ་ཡིན་ན་དེ་གང་ཞིག་གིས་ཇི་ལྟར་བྱེད། དངོས་པོ་མེད་པ་བྱེད་པ་ཡིན་ན༌[^829]ཞེས་བྱ་བ་ཡིན་ན་ནི་དངོས་པོ་མེད་པ་ཞེས་བྱ་བའི་བྱ་བ་འགའ་ཞིག་ཀྱང་ཡོད་པ་མ་ཡིན་ཏེ། དེ་ནི་འགའ་ཞིག་གིས་བྱ་བའི་ངོ་བོ་ཉིད་ཡིན་ན་དངོས་པོ་མེད་པར་མི་རུང་བའི་ཕྱིར་རོ། །

[Block 968]
དེ་བས་ན་དེ་ནི་དངོས་པོའི་བྱ་བ་འགོག་པ་སྟོན་པ་དང་། དངོས་པོར་མི་བྱེད་ཅེས་བྱ་བའི་དོན་ཏོ། །

[Block 969]
དེ་ལྟར༌[^830]འདི་ནི་ཅུང་ཞིག་ཀྱང་མི་བྱེད་ན་ཅུང་ཞིག་ཀྱང་མི་བྱེད་པ་གང་དང་གང་གིས་འཇོག་པར་བྱེད་པ་ཡིན། དེའི་ཕྱིར་འདི་ནི་འགའ་ཞིག་གིས་གེགས་མ་བྱས་པའི་ཕྱིར་འགའ་ཞིག་གི་ཚེ་ཡང་གནས་པ་མེད་དོ། །

[Block 970]
དེ་བས་ན་ལྟུང་བའི་གེགས་བྱེད་པ་ཞེས་བྱ་བ༌[^831]ཡང་དངོས་པོ་སྐད་ཅིག་མ་ཅན་དག་གི་ཉེ་བར་ལེན་པའི་ཡུལ་འདྲ་བར་འབྱུང་བ་དག་ལ་བྱའོ། །

[Block 971]
སྐྱེད་པར་མི་བྱེད་པ་ཡིན་ཡང་བླ་སྟེ་ལྟུང་བའི་ངང་ཚུལ་ཅན་དེའི་གེགས་བྱེད་པ་དེ་བྱེད་པའི་ཕྱིར་རོ། །

[Block 972]
རྫས་འགྲོ་བ་དང་ལྡན་པ་འཇོག་པར་བྱེད་པ་འགའ་ཞིག་ནི་ཡོད་པར་འགྱུར་ན། ཅི་བྱ་བ་མེད་པ་ནི་ཅི་གནས་པའི་མཚན་ཉིད་ཅན་དུ་འཇོག་པར་བྱེད་པར་འགྱུར། གནས་ན་ནི་དེའི་རང་བཞིན་ངོ་བོ་འཕོ་བ་མེད་པ་ཁོ་ན་ཡིན་ཏེ། དེ་ཡང་རྟེན་ལ་རག་ལུས་པ་མ་ཡིན་ཏེ།

[Block 973 [VERSE]]
རྟག་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །
དེ་ཡང་ཐ་དད་ཐ་དད་མེད། །
རྣམ་པར་སྤྱོད་པ༌[^832]མི་རིགས་ཉིད། །

[Block 974]
རྟེན་གྱི་རྒྱུ་ཅན་གྱི་སྤྱི་གནས་ཡིན་ཡང་བླ་སྟེ། དེ་སྤྱི་ལས་གཞན་པའམ། གཞན་མ་ཡིན་པ་ཞིག་ཏུ་འགྱུར་གྲང༌[^833]ན། གལ་ཏེ་གཞན་ཡིན་ན་དེ་ཉིད་དེའི་རྟེན་བྱེད་པ་ཡིན་ལ། དེ་ཡང་སྤྱི་ལ་རག་མ་ལུས་པའི་ཕྱིར། སྤྱིའི་རྟེན་གྱིས་ཅི་ཞིག་བྱེད། རག་ལས་པ་ཁོ་ན་ལ་རག་ལས་པ་ཞེས་ཇི་ལྟར་བརྗོད་པར་བྱ། གལ་ཏེ་གནས་པར་བྱེད་པར་ཤེས་པས་སོ་ཞེ་ན། དེ་ལ་ཡང་ཐལ་བ་མཚུངས་པ་དང་། ཐུག་པ་མེད་པར་འགྱུར་བ་དེ་བས་ན་ཕན་པ་བྱེད་པ་ངེས་པར་མ་བཟུང་བའི་ཕྱིར། འདི་ནི་འདིའི་གནས་པ་ཡིན་ནོ་ཞེས་བྱ་བར་ཤེས་པར་མི་འགྱུར་རོ། །

[Block 975]
གལ་ཏེ་སྐྱེད་པར་བྱེད་པ༌[^834]ཡིན་ནོ་ཞེ་ན། ཕན་མི་འདོགས་པའི་རྟེན་ལ་ལྟོས་པས་འདི་ལ་ཅི་ཞིག་བྱ། ལྟོས་པ་ཞེས་བྱ་བ་ནི་དེ་ལ་རག་ལུས་པ་ཡིན་ན་དེ་ཡང་སྤྱི་ཁྱད་པར་མེད་པ་ལ་མི་རིགས་པ་དང་། ཡན་གར་བས་བསྐྱེད་པའི་ཕྱིར། གནས་པའི་རྒྱུ་གཞན་ཡོད་པ་ནི་མ་ཡིན་ནོ། །

[Block 976]
སྤྱི་ལ༌[^835]གནས་པ་ཐ་དད་པ་མེད་པ་ཡིན་ན་ཡང་དེ་ནི་དེའི་རང་གི་ངོ་བོ་ཁོ་ན་ཡིན་ཏེ། དེ་ཡང་རྟག་ཏུ་ཡོད་པའི་ཕྱིར། འདི་ནི་འགའ་ཞིག་གིས་ཀྱང་གནས་པར༌[^836]བྱེད་པ་མ་ཡིན་ནོ། །

[Block 977]
དེ་བས་ན་སྤྱིའི་རྟེན་ཡོད་པ་མ་ཡིན་པ་དེའི་ཕྱིར་བརྟེན་པ༌[^837]འདི་ནི་གནས་པ་མེད་དོ། །

[Block 978]
འོན་ཀྱང་གསལ་བ་མ་ཡིན་པ་སྤྱི་ཡོད་དུ་ཟིན་ཀྱང་དེའི་གསལ་བ༌[^838]ནི་བསལ་པས་ཤེས་པའི་རྒྱུར་གྱུར་པའི་ཕྱིར། དེ་ལ་གནས་པར་འགྱུར་བ་ཡང་རིགས་པ་མ་ཡིན་ནོ། །

[Block 979]
གང་གི་ཕྱིར།

[Block 980 [VERSE]]
བདག་ཉིད་རྣམ་ཤེས་བསྐྱེད་རུང་ཕྱིར། །
གཞན་གྱི་ངོར་བྱེད་གང་ཡིན་དེ། །
བསལ་བྱ་ཡིན་ཏེ་རུང་ཉིད་ཀྱི། །
བྱེད་པ་པོ་ཡང་རྒྱུ་རུ་འདོད། །

[Block 981 [VERSE]]
དང་པོ་ཉིད་ནས་འདི་རུང་ཉིད། །
དེ་ལ་ལྟོས་པ་མི་རུང་སྟེ། །
འགྱུར་བའི༌[^839]མེད་པའི་སྤྱི་དེ་ནི། །
སྤྱི་དང་ལྡན་པ་གང་ལས་ཡིན། །

[Block 982]
བྱེད་པ་པོ་ལས་གསལ་བར་བྱེད་པ་ནི་ཁྱད་པར་ཅུང་ཞིག་ཀྱང་མེད་པ་ཡིན་ཏེ། གཞན་རང་གི་ཡུལ་ལ་རྣམ་པར་ཤེས་པ་བསྐྱེད་པར་ནུས་པ་རིགས་མཐུན་པའི་ཉེ་བར་ལེན་པ་ལ་ལྟོས་པའམ། ལྟོས་པ་མེད་པའི་དངོས་པོ་སྐྱེད་པར་བྱེད་པ་ཁོ་ན་གསལ་བར་བྱེད་པ་ཞེས་བྱའོ། །

[Block 983]
གཞན་དག་ཏུ་ནི་བསྐྱེད་པར་བྱ་བ་ལ་ཤེས་པ་སྐྱེ་བ་ནུས་པ་འཕངས་པ་མེད་པའི་ཕྱིར་སྐྱེད་པར་བྱེད་པ་ཙམ་གྱི་རྒྱུ་ཉིད་ཡིན་ནོ། །

[Block 984]
གལ་ཏེ་གང་ལས་རྣམ་པར་ཤེས་པ་བསྐྱེད་པར་རུང་བ་སོ་སོར་སྣང་བ་ཐོབ་པ་གང་ཡིན་པ་དེ་དེའི་བསྐྱེད་བྱར་མི་འགྱུར་ན། དེ་ནི་འདིའི་རང་བཞིན་དུ་གྱུར་པའི་རུང་བ་ཉིད་ནི་དང་པོ་ཉིད་ནས་ཡོད་པའི་ཕྱིར་རྣམ་པར་ཤེས་པ་སྐྱེད་པར་བྱེད་པ་དེ་ལ་ལྟོས་པ་མ་ཡིན་ནོ།[^840] །

[Block 985]
འདི་ནི་གཞན་དུ་འགྱུར་བ་ཉིད་ཡིན་ན་དེ་ཉིད་དེ་ལས་འགྱུར་བའི་ཕྱིར། གནས་པ་བཞིན་དུ་ཐལ་བར་འགྱུར་བ་དེ་བས་ན་གསལ་བར་བྱེད་པ་དེ་བྱེད་པ་མ་ཡིན་ཞིང་གཞན་ཡང་བྱེད་པ་མ་ཡིན་པ་དེ་ལྟར་ན་ཅུང་ཞིག་ཀྱང་མི་བྱེད་པ་དང་ལྟོས་པར་བྱ་བ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་འགལ་བ་ཡིན་ནོ། །
--- END BLOCKS ---
