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
ཅི་བྱུགས་པ༌[^677]སྦྱར་བས་སྐམས༌[^678]པས་ཡིན་ནམ་ཞེ་ན། དེ༌[^679]བསྐམས་པར་གྱུར་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ས་ཅི་ལྟ་བུ་དང་ཅི་ཞིག་བཏིང་བའི་ས་ལ་ལྷུང་བཟེད་བཞག་པ་ལ་འདིས་དགག༌[^680]ཅེ་ན། དེའི་ཕྱིར་ས་གཞི་བྱི་དོར་བྱས་པར་ཕུབ་མ་བཏིང་ཞིང་དུ་བ་འཆོར་བར་བྱེད་པ༌[^681]འབྲུ་མར་གྱི་ཚིགས་མ་ལ་སོགས་པའི་རྫས་བཀྲམ་པའི་སྟེང་དུ་ཁ་བུབ་ཏུ་བཞག་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཕུབ་མའི་སྟེང་དུ་སྣང་བའི་ངང་ཚུལ་ཅན་འབྱུང་བར་བྱེད་པའི་འབྲུ་མར་གྱི་ཚིགས་མ་ལ་སོགས་པའི་རྫས༌[^682]རྣམས་བཀྲམ་པ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །ཇི་ལྟར་གཞག་པར་བྱ་ཞེ་ན། དེའི་ཕྱིར་ཁ་བུབ་ཏུ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 947]
འདིའི་རྗེས་སུ་ཅི་བྱ་ཞེ་ན། དེའི་ཕྱིར་ལྕི་བ་དག་དང་སོགས་མ་བཅེར་ཏེ་སྦར་རོ། །

[Block 948]
ཏེ་པོར་གྲངས་ནས་དབྱུང་ངོ་ཞེས་བྱ་བ་སྨོས་ཏེ།[^683] ལྷུང་བཟེད་ཁ་དོག་རྫོགས་པ་ཕུན་སུམ་ཚོགས་པར་འགྱུར༌[^684]གྱི་བར་དུ་བཟླས་པར་བྱའོ་ཞེས་བྱ་བ་ལ། ཇི་སྲིད་དུ་ཁ་དོག་གྲུབ་པ༌[^685]དེ་སྲིད་དུ་བསྲེག་པ་སྦྱིན་པར་བྱའོ། །

[Block 949]
བྱི་དོར་བྱས་ཤིང་བྱི་དོར་བྱས་ཤིང་གཞུག་པར་བྱའོ་ཞེས་བྱ་བ་ནི་བསྲེག་པ༌[^686]རེ་རེ་ལ་བྱི་དོར་བྱ༌[^687]ཞེས་བྱ་བའི་དོན་ནོ། །

[Block 950]
སྲོག་ཆགས་རྣམས་ལ་སྙིང་བརྩེ་བས་ཉེ་ཀོར་ཕྱག་དར་དང་ཆག་ཆག་བྱའོ་ཞེས་བྱ་བ་ནི་ཆུས་ཉེ་འཁོར་ཉིད་ལའོ། །

[Block 951]
ལྷུང་བཟེད་མེད་པར་རབ་ཏུ་དབྱུང་བར་མི་བྱའོ་ཞེས་བྱ་བ་འདི་ཞར་ལ་འབྱུང་བ་ཡན་ལག་དང་བཅས་པའི་ལྷུང་བཟེད་ཀྱི་ཆོ་ག་བཤད་ཟིན་ཏོ།། །།

[Block 952]
རབ་ཏུ་འབྱུང་བའི་གཞི་གཞན་འབྲེལ་བས་བརྗོད་པར་བྱ་སྟེ། [^688]ལོ་ཚིགས་མི་ཤེས་ན༌[^689]མཚན་གྱི་ཉེ་འཁོར་དུ་སྤུ་སྐྱེས་པ་བསྙེན་པར་རྫོགས་པར་ཁས་བླངས་པར་བྱའོ་ཞེས་བྱ་བ་ལ། སྤུ་སྐྱེས་པ་ཞེས་བྱ་བ་ནི་སྤུ་སྐྱེས་པ་ལའོ། །

[Block 953]
ཕྱོགས་གང་དུ་ཞེ་ན། དེའི་ཕྱིར་མཚན་གྱི་ཉེ༌[^690]འཁོར་དུ་ཞེས་བྱ་བ་སྨོས་ཏེ་མཚན་མ་ཐམས་ཅད་ལའོ། །

[Block 954]
ལོ་ཚིགས་མི་ཤེས་པ་ནི་བསྙེན་པར་རྫོགས་པར་བྱེད་པར་ཁས་བླངས་པའོ། །

[Block 955]
བསྙེན་པར་རྫོགས་པར་བྱ་བ་ཁས་བླངས་པའི་དོན་དུ་ལོ་ཉི་ཤུ་ལོན་པ་ཉིད་དུ་མི་ཤེས་ན་དེའི་མཚན་གྱི་ཐན་ཀོར་དུ་སྤུ་སྐྱེས་པ་ཁས་བླངས་པས་ཞེས་བྱ་བའི་དོན་ཏོ། །

[Block 956]
འདིས་སྐྱེས་པའི་དངོས་པོ་མཚོན་པར་བྱེད་པས་ན་མཚན་མ་སྟེ་ཕོའི་དབང་པོའོ། །

[Block 957]
དེ་ནི་སྒྱུ་ཐབས་ཀྱིས་བརྟག་པར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ནི་ཞེས་བྱ་བ་ནི་མཚན་མ་ལ་སྤུ་བྱུང་བའོ།[^691] །སྒྱུ་ཐབས་སུ་ཇི་ལྟ་བུས་ཤེ་ན། དེའི་ཕྱིར་ཟུང༌[^692]ང་དང་གོས་ཀྱི༌[^693]གདང་མཐོན་པོ་ལ་འདུག་པའི་དངོས་པོ་དབབ་པ་ལ་སོགས་པས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ཟུང་ང་དང་གོས་ཀྱི་གདང་མཐོན་པོ་ལ་འདུག་པའི་གོས་ལ༌[^694]སོགས་པའི་དངོས་པོ་དབབ་པ་དང་འགེལ་བ་ལ་སོགས་པའོ།[^695] །བསྙེན་པར་རྫོགས་པར་འདོད་པ་ཤིང་ལ་འཛེག་ཏུ་མི་གཞུག་གོ། །

[Block 958]
མཚམས་ཀྱི༌[^696]ཕྱི་རོལ་དུ་མི་གཏོང༌[^697]ངོ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པར་འདོད་པ་ཞེས་བྱ་བ་ལ་འཇུག་པའོ། །

[Block 959]
སྣང་བའི་ཉེ་འཁོར་གྱི་ནང་ནི་འདིར་མཚམས་སུ་རྣམ་པར་གནས་པའོ། །

[Block 960]
སྣང་བའི་ཉེ་འཁོར་གྱི་ནང་དུ་བྱས་པ་ནི་བསྙེན་པར་རྫོགས་པའི་གནས་སུ་ཁྲིད་པ་ལ༌[^698]དེའི་གནས་ལས་སོ། །

[Block 961]
དེའི་གནས་ལས་ལྡང་བ་ཉིད་ལ་བསྙེན་པར་རྫོགས་པའི་གནས་སུ་དེའི་དོན་དུ་བྱ་བ་བྱེད་པའི་བསྟན་པ་ལ་ལྷག་པར་མོས་པ་ཚུལ་ཁྲིམས་དང་ལྡན་པའི་དགེ་སློང་འཁོར་དང་བཅས་པའི་གཙུག་ལག་ཁང་ན་གནས་པ་ལས་འགྲོ་བ་ན་དེའི་ལམ་ལ་ཞུགས་པས་སོ། །

[Block 962]
དུས་གཞན་ལ་གནས་པ་ལ་དེ་ལ་འདི་ལྟར་བྱ་བ་ཉིད་དང་། འཆགས་པ༌[^699]དང་ཤིན་ཏུ་འདུད་པའི་གནས་པས༌[^700]དེ་ལྟར་སྣང་བའི་ཉེ་ཀོར་དུ་བཀར་ཏེ་ཚོགས་ལ་མངོན་དུ་ཕྱོགས་པར་ཐལ་མོ་སྦྱར་ཏེ་གཞག་པར་བྱའོ་ཞེས་བྱ་བ་ལ་དེ་ཞེས་བྱ་བ་ནི་བསྙེན་པར་རྫོགས་པར་འདོད་པའོ། །

[Block 963]
བཀར་ཏེ་ཞེས་བྱ་བ་ནི་གསང་སྟེ་སྟོན་པ་དེ་ལ་བསྐོ་བའི་ལས་མི་ཐོས་པར་བྱ་བའི་ཕྱིར་དགེ་འདུན་གྱི་དབུས་ཀྱི་ནང་ནས་ལོགས་ཤིག་ཏུ་གཞག་པ་ཡིན་པ་དེ་ནི་འདིར་བཀར་བའི་ཚིག་གིས་གཟུང་ངོ་། །བཀར་བ་ཡོད་པ་ལ་ཚོགས་ལ་མངོན་དུ་ཕྱོགས་པར་ཐལ་མོ་སྦྱར་ཏེ་གཞག་པར་བྱའོ། །

[Block 964]
དགེ་འདུན་གྱི་ནང་ནས་མ་བཀར་བར་དེ་མི་བྱའོ་ཞེས་བྱ་བའི་ཐ་ཚིག་གོ། །

[Block 965]
ཁྱིམ་པ་ལ་གནས་རྣམས་བརྗོད་པར་མི་བྱའོ། །

[Block 966]
བསྙེན་པར་རྫོགས་མ་ཐག་པ་ལ་མི་བརྗོད་པར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་རྣམས་ཞེས་བྱ་བ༌[^701]འཇུག་གོ། །

[Block 967]
ཁྱིམ་དུ་གནས་པ་ལ་གནས་རྣམས་བརྗོད་པར་མི་བྱ་སྟེ། ཇི་སྲིད་དུ་རབ་ཏུ་འབྱུང་བར་མི་འགྱུར་ཞེས་བྱ་བའོ། །

[Block 968]
འདིའི་འོག་ཏུ་གཞུང་ནི་འདི་ཡིན་ཏེ། བྲམ་ཟེའི་ཁྱེའུ་གཞན་ཞིག་རབ་ཏུ་བྱུང་བ་དང་བསྙེན་པར་རྫོགས་པ་ལ་མཁན་པོས་ཇི་སྲིད་དུ༌[^702]བསོད་སྙོམས་ལ་སོང་ཅིག༌[^703]ཅེས་བསྒོ་བ་དང་། དེས་བསྒོ་བ་ན་བདག་སློང༌[^704]མོ་ལ་རྒྱུ་བས་སྐྱོ་བ་སྟེ་རབ་ཏུ་བྱུང་ན་ཡང་བསོད་སྙོམས་བྱ་འམ་ཞེས་བསླབ་པ་ཕུལ་ཏེ་ཉམས་པར་གྱུར་པ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་བཀའ་སྩལ་པ། བསྙེན་པར་རྫོགས་པའི་དེ་མ་ཐག་ཏུ་གནས་བཞི་བརྗོད་པར་བྱའོ་ཞེས་བྱ་བ་འདི་ལ་བསྡུ་བ་འདི་ཡིན་ནོ། །

[Block 969]
གང་ན་གནས་མེད་པ་དེར་གསོ་སྦྱོང་ལ་བསྡད་པ་འམ་གནས་པར་ཁས་བླངས་པར༌[^705]མི་བྱའོ། །

[Block 970]
གནས་པར་ཁས་བླངས་པ༌[^706]སྔ་མ་རྗེས་སུ་བསྲུང་བར་མི་བྱའོ་ཞེས་བྱ་བ་ནི་གནས་མེད་པ་ལ་ཁས་བླངས་པ་ཕྱི་མས་དོན་བསྒྲུབ་པ་མཐོང་ཞིང་ཚིག་འདི་མཐོང་བ་ཡིན་ཏེ། དེ་ལ་སྔ་མ་ཞིག་པ་ལ་ཕྱི་མ་ཁས་བླང་བར་བྱའོ་ཞེས་བྱ་བ་ཤེས་པར་འགྱུར་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 971]
ཕྱི་མ་ལ་ཡང་ཟླ་བ་གཉིས་ལས་ལྷག་པའོ་ཞེས་བྱ་བ་ལ། ཕྱི་མ་ཞེས་བྱ་བ་ནི་ཁས་ལེན་པའོ། །

[Block 972]
ཟླ་བ་གཉིས་ལས་ལྷག་པ་གནས་མེད་ན་བསྲུང་བར་མི་བྱའོ་ཞེས་བྱ་བའི་རྗེས་སུ་དགག་པའི་དོན་དུ་ཡང་གི་སྒྲའོ། །

[Block 973]
ཟླ་བ་གཉིས་མ་བསྟེན་པས༌[^707]ཀྱང་གནས་པར་བྱ་ཞེས་བྱ་བ་འདིར་ཤེས་པར་འགྱུར་རོ། །

[Block 974]
གནས་དང་ལས་དང་ཉེ་གནས་ཀྱི་སྟ་གོན་གྱིས་དེ་བཙལ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། དེ་ཞེས་བྱ་བ་ནི་གནས་སོ། །

[Block 975]
གནས་ལ་སོགས་པའི་སྟ་གོན་རྣམས་ཀྱིས་གནས་འདི་ཡོངས་སུ་བཙལ་བར་བྱའོ། །

[Block 976]
གནས་ལ་སྟ་གོན་ནི་གནས་ཁང་ལ་སྟ་གོན་ནོ། །

[Block 977]
གནས་ལ༌[^708]འོས་པའི་དགེ་འདུན་ལ་གང་ཟག་མང་བ་ཉིད་ཀྱི་ཕྱིར་བཙལ་བར་བྱའོ་ཞེས་བྱ་བ༌[^709]ནི་མང་པོའི་ཚིག་གོ། །

[Block 978]
མེད་ན་གཞོན་ནུའི་ནང་ནས་ཆེས༌[^710]རྒན་པ་ལ་ཞུ་བར་བྱའོ་ཞེས་བྱ་བ་ལ། མེད་ན་ཞེས་བྱ་བ་ནི་གནས་པའོ། །

[Block 979]
དབྱར་གནས་ལ་མ་བསྟེན་པ༌[^711]ཞེས་བྱ་བའི་ཆེད་དུ་བརྗོད་པའི་ཚིག་འདི་ལ་གནས་སུ་བྱ་བ་རྣམས་ལ་ནང་དུ་ལོ་གཅིག་ཏུ་སློབ་དཔོན་དུས༌[^712]ལས་འདས་པར་གྱུར་ནས་དབྱར་བཅུག༌[^713]ནས་གཙུག་ལག་ཁང་དུ་མི་གནས་པར་བྱས་ནས་སོང་བར་གྱུར་པ་རྣམས་ལ་གཙུག་ལག་ཁང་ན་གནས་མེད་ཀྱང་མི་བྱ་སྟེ་བྱེད་ན་འགལ་ཚབས་ཅན་དུ་འགྱུར་རོ། །

[Block 980]
འོན་ཀྱང་གང་ཞིག་དེ༌[^714]རྣམས་ལས་ཤིན་ཏུ་རྒན་པ་དེ་ལ་ཞུ་བར་བྱ་ཞིང་དེའི་འོག་ཏུ་དགག་དབྱེ་ལ་གནས་ཀྱི་སློབ་དཔོན་ཡོངས་སུ་བཙལ་བར་བྱ་བ་གསུངས་པའི་གཞུང་འདི་ལ་འདི་ནི་བསྡུ་བ་ཡིན་ནོ། །

[Block 981]
དོན་གྱིས༌[^715]དེ་རྣམས་ཀྱི་ཆེས་རྒན་པའི་གཞོན་ནུ་དེ་གནས་སོ། །

[Block 982]
ཆེས་རྒན་པ་དེ་ལ་ནི་གཞོན་ནུ་ལ་གནང་བར་འགྱུར་ཏེ། གནས་ལ་མི་གནས་པ་ཞེས་བྱ་བར་རིག་པར་བྱའོ། །

[Block 983]
ཡོད་ན་ཡང་རེ་ཞིག་གི་གནས་དེ་ཉིད་ཀྱིས་སོ་ཞེས་བྱ་བ་ནི་གནས་ལའོ། །

[Block 984]
ཡོད་ན་ཡང་རྟེན་ནི་རྟེན་ལའོ། །

[Block 985]
གཞོན་ནུའི་ཆེས་རྒན་པ་ལ་ཞུ་བར་བྱའོ། །
--- END BLOCKS ---
