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
བླ་གོས་ནི་ངེས་པ་མེད་པ་དང་། མཐང་གོས་ཀྱང་ངེས་པ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 947]
རྐྱེན་དེ་ལྟ་བུ་དག་མེད་པར་མ་དྲས་པ༌[^820]དེས་གྲོང་དང་ཁྱིམ་གཞན་དག་ཏུ་འདུག་པ་དང་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེས་ཞེས་བྱ་བ་ནི་སྣམ་སྦྱར་དེས་སོ། །

[Block 948]
འདིར་གཞུང་ནི། བཙུན་པ་ཆོས་གོས་མ་དྲས་པས༌[^821]གྲོང་ཁྱེར་དུ་འཇུག་པར་རུང་ངམ་ཞེས་བྱ་བ་ལ་སོགས་པའོ། །

[Block 949]
འདིར་སྣམ་སྦྱར་གྱི་དགོངས་པ་ཡང་ལུང་དང་རིགས་པ་འདི་དང་སྔ་མ་གཉིས་ཀྱིས་ནི་འདིར་ཆོས་གོས་ཞེས་སྨོས་པ་ནི་སྣམ་སྦྱར་ཡིན་པར་དགོངས་པར་རིགས་སོ། །

[Block 950]
དེ་བས་ན་འདི་ལྟར་འདིར་མདོར་བྱས་པའོ། །

[Block 951]
མུ་སྟེགས་ཀྱི་འདུག་གནས་སུ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བ་ནི་རྐྱེན་དེ་ལྟ་བུ་མེད་པར་སྣམ་སྦྱར་མ་དྲས་པ་དེས་མུ་སྟེགས་ཅན་གྱི་འདུག་གནས་སུ་འཇུག་པ་དང་འདུག་པར་མི་བྱ་སྟེ། ཉེ་བར་ཞུགས་པའི་ཆོ་ག་འདི་འདུག་གནས༌[^822]དེ་ན་མུ་སྟེགས་ཅན་དག་ཉེ་བར་མི་འཁོད་ཀྱང་མངོན་པར་འདོད་པ་ཡོད་བཞིན་དུ་དཔེར་བྱས་སོ། །

[Block 952]
འཁོད་ན་འདུག་པ་དང་འཇུག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་རྐྱེན་དེ་ལྟ་བུ་དག་ཡོད་ཀྱང་མུ་སྟེགས་ཅན་གྱི་འདུག་གནས་དེར་འདུག་པར་མི་བྱའོ་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 953]
འདི་ལྟར་ཆོས་གོས་མ་དྲས་པ་ནི་ཀུན་དུ་རྒྱུ་ལ་སོགས་པ་མུ་སྟེགས་ཅན་རྣམས་ཀྱི༌[^823]གོས་དང་འདྲ་བ་བསྟེན་པས་དེར་ཞུགས་པ་དང་འདུག་པར་འགྱུར་བ་གང་ཡིན་པ་དེའི་ཕྱོགས་ཀྱི་ནང་དུ་བསྟེན་པ་ཡིན་པར་དོགས་པར་འགྱུར་བས་ན་འདིར་དེ་དག་ག་པར་མཛད་དོ། །

[Block 954]
འདིར་གཞུང་ནི་བཙུན་པ་ཀུན་དུ་རྒྱུའི་འདུག་གནས་སུ་སྣམ་སྦྱར་མ་མཆིས་པར་མཆིར་རུང་ངམ། ཉེ་བ༌[^824]འཁོར་མི་རུང་ངོ་། །གལ་ཏེ་ཀུན་དུ་རྒྱུ་དག་ཕྱི་རོལ་དུ་བྱུང་བར་གྱུར་ན་ནི་རུང་ངོ་ཞེས་བྱ་བ་ཡིན་ནོ། །

[Block 955]
སྤུ་ཅན་ཆོས་གོས་གསུམ་ཉིད་དུ་བྱིན་གྱིས་མི་བརླབ་བོ། །

[Block 956]
དེ་བགོ་བའི་ཆོས༌[^825]གོས་སུ་མི་བསྟེན་ནོ་ཞེས་བྱ་བ་སྤུ་ཅན་དེ་བགོ་བར་མི་བྱའོ། །

[Block 957]
སེང་བདག་བདག་གིར་བྱའོ་ཞེས་བྱ་བ་ནི་རུང་བར་བྱ་སྟེ་བཅང་བ༌[^826]ལ་འདིར་བདག་གིར་བྱའོ་ཞེས་བྱ་བའི་སྒྲས་གསུངས་སོ། །

[Block 958]
དེའི༌[^827]རྣམ་པ་བཞིའོ་ཞེས་བྱ་བ་ནི་སེང་བ་དེའོ། །

[Block 959]
བཞི་གང་ཞེ་ན། དེའི་ཕྱིར་བལ་ལས་བྱས་པ་དང་ཟར་མ་ལས་བྱས་པ་དང་དུ་གུ་ལ་ལས་བྱས་པ་དང་རས་བལ་ལས་བྱས་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། འདི་ལ་ལེགས་པར་མ་ཡིན་པའི་ངོ་བོ་ཉིད་དུ་ཚོགས་ལ་སོགས་པ་རྣམས་སུ་འགྱུར་རོ། །

[Block 960]
དེ་བས་ན་གཞན་མི་རུང་བ་ནི་མ་ཡིན་མོད་ཀྱི་འདིར་རྣམ་པ་བཞི་སྨོས་པ་མཐོང་བ་ཡིན་ནོ། །

[Block 961]
སྤུ་དམའ་བ་ལ་སོགས་པ་རས་ཀྱི་རྣམ་པ་ཡང་བ་གཞན་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ཡང་། སྤུ་དམའ་བ་ལ་སོགས་པའི་རྣམས་ལ་ཡང་ངོ་། །གཞན་དག་ཀྱང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ལྟ་བུའི་སྤུ་ཅན་ལ་སོགས་པ་ལ༌[^828]འདི་ལྟར་བརྒལ་བར་བྱས་པ་རྣམས་ལ་ངོ་བོ་བསྟན་པར་བྱེད་དེ་སྤུ་དམའ་བ་ལ་སོགས་པ་ཞེས་བྱ་བའི་མཐར་ཐུག་པ་དེ་བཟུང་བ་ཡིན་ནོ། །

[Block 962]
ལ་བ་ཡང་ངོ་ཞེས་བྱ་བ་ཡང་བདག་གིར་བྱར་རུང་ངོ་ཞེས་བྱ་བའི་ལྷག་མའོ། །

[Block 963]
དེ་སྤུ་དམའ་བ་མ་ཡིན་པའི་ཕྱིར་བརྩམས་སོ། །

[Block 964]
གནོད་པ་མེད་ན་སྤུ་ཕྱིར་བསྟན་ཏེ་བགོ་བར་མི་བྱ་སྟེ། གཞན་དུ་ནའོ་ཞེས་བྱ་བ་ལ། གནོད་པ་མེད་ན་ཞེས་བྱ་བ་ནི་དྲི་མ་དང་ཤིག་ལ་སོགས་པ་རྣམས་ཀྱིས་སོ། །

[Block 965]
འདིར་གཞུང་ནི། དྲི་མ་ཅན་དང་ཤིག་ཅན་ལ་ལྟུང་བ་མེད་དོ་ཞེས་གསུངས་པ་ཡིན་ཏེ། དེ་ཡང་དཔེ་ཙམ་དུ་རྣམ་པར་གནས་པ་ཡིན་ནོ་ཞེས་བྱ་བ་ནི་ཐམས་ཅད་བསྙེགས་པར་བྱས་པ་ཡིན་ནོ། །

[Block 966]
དེ་ཞེས་བྱ་བ་ནི་ལ་བ་དེའོ། །

[Block 967]
གཞན་དུ་ན་ཞེས་བྱ་བ་ནི་སྤུ་མེད་པ་གྱོན་པ་ལ་གནོད་པ་མེད་པའོ། །

[Block 968]
དེ་དེ་བཞིན་དུ་གྱོན་པས་འཆག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་བཞིན་དུ་ཞེས་བྱ་བ་ནི་ཕྱིར་བཟློག་ཏུའོ། །

[Block 969]
འདི་ནི་གནོད་པ་ཡོད་ན་ཞེས་བྱ་བ་དམིགས་ཀྱིས་བསལ་ལོ། །

[Block 970]
འདིར་གཞུང་ནི། བཅོམ་ལྡན་འདས་ཀྱིས་དགེ་སློང་གིས་ལ་བ་སྤུ་ཕྱིར་བསྟན་ཏེ་བགོ་བར་མི་བྱའོ་ཞེས་གསུངས་པ་དང་། དགེ་སློང་དག་གིས་བ་གླང༌[^829]རྫིའི་ཁྱིམ་ནས་ལ་བའི་གོས་དག་རྙེད་ནས་དེ་དགེ་སློང་དེ༌[^830]དག་ཤིག་མང་བས་ཤིག་དག་གིས་ཟོས་པ་ན་མོས་པར་མ་གྱུར་པའི་སྐབས་དེ་དགེ་སློང་དག་གིས་བཅོམ་ལྡན་འདས་ལ་གསོལ་ནས་བཀའ་སྩལ་པ། ལ་བ་སྤུ་ཕྱིར་བསྟན་ཏེ་གྱོན་ལ་འདུག་པར་བྱ་ཞིང་ཉལ་བར་ཡང་བྱའོ། །

[Block 971]
བཅག་པར་མི་བྱའོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 972]
པར་སིག་གི་ལ་བ་དང་། བེའུ་ཕྲུག་དང་། པར་ཐང་ཁྲ་བོ་གང་ཟག་གིས་བདག་གིར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་རྙེད་པ་རྙེད་པ་ཡང་བྱེ་བྲག་མེད་པར་རྟོགས་པའོ། །

[Block 973]
འཆག་སར་པར་ཐང་གདིང་བ་མནོད་པར༌[^831]བྱའོ་ཞེས་བྱ་བ་ལ། གལ་ཏེ་ཁྲ་བོ་ཡིན་ན་བདག་གིར་མི་བྱའོ། །

[Block 974]
གལ་ཏེ་མ་ཡིན་ན་ཅི་དགར་བྱའོ། །

[Block 975]
ཁྲ་བོ་བདག་གིར་བྱེད་པ་བཀག་པ་ཡིན་པར་རྟོགས་པར་བྱའོ། །

[Block 976]
རྟག་ཏུ་མལ་གཅིག་ཏུ་བཅག་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་པར་ཐང་གིའོ། །

[Block 977]
ནུས་པ་ཉིད་ཡིན་ན་བཙེམས་པ༌[^832]དང་ལྷན་པ་རིང་པོར༌[^833]གླན་པས་ཕྱིར་བཅོས་པར་བྱའོ། །

[Block 978]
མི་ནུས་པ་ཉིད་ན་འཆགས་པ༌[^834]དེ་ཉིད་དུ་ལྕི་བ་དང་སས་བྱུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་གཞན་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་སྤུ་ཅན་ནས་བརྩམས་ཏེ་འདི་རྣམས་ལས་གཞན་སྤུ་ཅན་ཇི་ལྟར་བཅང་བར་བྱ་བ༌[^835]ཞེ་ན། དེའི་ཕྱིར༌[^836]སྦྱིན་བདག་ལ་ཡིད་བརྟེན༌[^837]པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། དེ་དབང་བའི་བསམ་པས་དེ་ལ་ཡིད་བརྟན་ཏེ་ལོངས་སྤྱོད་པ་ཉིད་ལ་མངོན་པར་བརྟེན་ནས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 979]
སྣམ་སྦྱར་དང་བླ་གོས་དང་། མཐང་གོས་དང་། ཤམ་ཐབས་དང་། ཤམ་ཐབས་ཀྱི་གཟན་དང་། རྔུལ་གཟན་དང་། རྔུལ་གཟན་གྱི་གཟན་དང་། གདོང་ཕྱིས་དང་། རྣག་གཟན་དང་། གཡན་པ་དགབ་པ་དང་། སྐྲ་བཟེད༌[^838]དང་། གདིང་བ་དང་། དབྱར་གྱི་གོས་རས་ཆེན་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་ཡོ་བྱད་བཅུ་གསུམ་པོ་དེ་དག་བཅང་བར་བྱ་སྟེ། ཆོས་གོས་གནང་བ་དེ་ཉིད་དུ་བྱིན་གྱིས་བརླབས་ཏེ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཉིད་དུ་ཞེས་བྱ་བ་ནི་གང་ཞིག་ཆོས་གོས་དེ་ཉིད་དང་། དབྱར་གྱི་གོས་རས་ཆེན་ལ་སོགས་པ་དེའི་དངོས་པོར་དེ་གནང་བའོ། །

[Block 980]
སྣམ་སྦྱར་ལ་སོགས་པའི་གོས་གནང་བ་དག་སྣམ་སྦྱར་ལ་སོགས་པ་དེ་ཉིད་ཀྱི་མིང་དུ་བྱིན་གྱིས་བརླབས་ཏེ་བཅང་བར་བྱའོ། །

[Block 981]
དེ་དག་གི་སྔགས་ནི། ཚེ་དང་ལྡན་པ་དགོངས་སུ་གསོལ་བདག་མིང་འདི་ཞེས་བྱ་བའི་ཆོས་གོས་བགྱིས་ལགས་པ་རུང་བར་སྤྱད་པར་འོས་པ་འདི་ཆོས་གོས་སྣམ་སྦྱར་དུ་བྱིན་གྱིས་བརླབ་པོ། །ལན་གསུམ་བཟླས། དེ་བཞིན་དུ་བླ་གོས་ནས་དབྱར་གྱི་གོས་རས་ཆེན་གྱི་མཐར་ཐུག་པ་རྣམས་ལ་ཡང་བརྗོད་པར་བྱའོ། །

[Block 982]
ཡོ་བྱད་ཀྱི་གོས་ཀྱང་ངོ་། །དེ་ནི་དཀར་པོ་ཉིད་དང་། ཁ་ཚར་དང་། ཕུན་ཚར་དང་བཅས་པ་ལ་ཡང་ཉེས་པ་མེད་དོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་ཡོ་བྱད་ཀྱི་གོས་འཆང་བ་དེའོ། །

[Block 983]
དགེ་འདུན་གྱི་ཡང་ངོ་ཞེས་བྱ་བ་ནི་ཡོ་བྱད་ཀྱི་གོས་ཀྱང་དཀར་པོ་དང་། ཁ༌[^839]ཚར་དང་ཕུན་ཚར་དང་བཅས་པ་འཆང་བ་ལ་ཡང་ཉེས་པ་མེད་པའོ། །

[Block 984]
འདིར་གཞུང་ནི། དེ་ལྟ་བས་ན་དགེ་འདུན་གྱིས༌[^840]གོས་དག་ནི་སར་པ་དང་། ཁར་ཚར༌[^841]དང་ཕུན་ཚར་རིང་པོ་དག་ཀྱང་བཅང་བར་གནང་ངོ་ཞེས་གསུངས་པ་ཡིན་ནོ། །

[Block 985]
གཞན་དུ་མ་ཡང༌[^842]རུང་བར་བྱ་སྟེ་བཅང་བར་བྱའོ་ཞེས་བྱ་བ་ནི་འདིར་འཆང་བའི་ཉེས་པ་མེད་པར་རྗེས་སུ་གནང་བར་བྱས་སོ། །
--- END BLOCKS ---
