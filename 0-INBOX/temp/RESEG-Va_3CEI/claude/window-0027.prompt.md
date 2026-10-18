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
མདོ་ལས་ཡང་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུས་ཞེས་པ་ནས་བདེ་བར་གཤེགས་པ༌[^953]བཤད་དུ་གསོལ་ཞེས་པའི་བར་དུ་ནི་འདས་པའི་དེ་བཞིན་གཤེགས་པ་གྲངས་མེད་པ་རྣམས་ཀྱིས༌[^954]སེམས་ཅན་གྱི་དོན་མཛད་པར༌[^955]སྟོན་པ་སྟེ། འདི་ཆོས་བཤད་པར་གསོལ་བ་གཉིས་པ༌[^956]སྔར་ནི་ཚིག་རྐྱང་པས་གསོལ། དེའི་འོག་ཏུ་ནི་ཚིགས་སུ་བཅད་པས་བསྡུས་པ་སྟེ། འདི་ནི་དང་པོའོ། །

[Block 947]
མདོ་ལས་དེ་ཅིའི་སླད་དུ་ཞེ་ན་ཞེས་པ་ནས་ཡིད་ཆེས་པ་དང་འཛིན་པ་མཆིས་སོ་ཞེས་པའི་བར་དུ་ནི་འདི་བསྟན་པར་འོས་པའི་རྒྱུ་བསྟན་པ་སྟེ། སྔོན་དེ་བཞིན་གཤེགས་པ་མཐོང་བའི་རྒྱུ་བཟང་པོ་ཡོད་པ་ཤེས་རབ་རྣོ་ཞིང་དབང་པོ་གསལ་བ་དོན་ཟབ་མོ་ལ༌[^957]མཁས་པའི་འཁོར་རྣམས་ཞེས་སྦྱར་རོ། །

[Block 948 [HEADING]]
##### ཚིགས་སུ་བཅད་པས་བསྡུས་པ། ^4-2-7-2-0

[Block 949]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུ་ཞེས་པ་ནས་ཁྱོད་ཀྱིས༌[^958]ཆོས་བསྟན་གང་གིས་འཚལ་བར་འགྱུར་ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པས་བསྡུས་པའོ། །

[Block 950 [HEADING]]
#### དགག་པ། ^4-2-8-0

[Block 951]
མདོ་ལས་དེ་ནི༌[^959]བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་གཡང་ས་ཆེན་པོར་ལྷུང་བར༌[^960]འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་དགག་པ་གསུམ་པ་སྟེ། ཐོས་པའི་རྒྱུ་དང་མི་ལྡན་པའི༌[^961]ང་རྒྱལ་ཅན་རྣམས་འཇིག་རྟེན་པའི་བསམ་གཏན་བཞི་ལ་གནས་པ་དགྲ་བཅོམ་པའི་འབྲས་བུ་མ་ཐོབ་པ་ཐོབ་པར་སེམས་པའི༌[^962]འཆི་བའི་དུས་ཀྱི་ཚེ་ན་འཕགས་པའི་ལམ་མེད་དོ་ཞེས་སྐུར་པས་སེམས་ཅན་དམྱལ་བའི་གཡང་ས་ཆེན་པོར་ལྷུང༌[^963]ངོ་ཞེས་པའོ། །

[Block 952 [HEADING]]
#### ཆོས་བཤད་པར་གསོལ་བ། ^4-2-9-0

[Block 953]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་སྨན་པ་དང་བདེ་བར་འགྱུར་རོ་ཞེས་པའི་བར་དུ་ནི་ཆོས་བཤད་པར་གསོལ་བ་གསུམ་པ་སྟེ། བཤད་པར་གསོལ་བ་དང་ཆོས་ཀྱི་སྣོད་དུ་རུང་བའི་གཏན་ཚིགས་སྨོས་ཏེ། འཕགས་པ་ཤཱ་རིའི་བུ༌[^964]བདག་ཉིད་ཚེ་རབས་ཀྱང་དྲན་ལ་གཞན་གྱི་དབང་པོའང་རྟོགས་པ་ཡིན་པས་ཆོས་ཀྱི་སྣོད་དུ་འགྱུར་བའི་གཏན་ཚིགས་ཀྱིས་གསོལ་ཏོ། །

[Block 954 [HEADING]]
##### ཤཱ་རིའི་བུ་ཉིད་སྲས་ཀྱི་ཐུ་བོ་ཡིན་པའི་སྒོ་ནས་ཆོས་བཤད་པར་གསོལ་བ། ^4-2-9-1-0

[Block 955]
མདོ་ལས་དེ་ནས་ཚེ་དང་ལྡན་པ་ཤཱ་རིའི་བུས་དེའི་ཚེ་ཞེས་པ་ནས། དེ་དག་ཁྱོད་ཀྱིས་ཆོས་བཤད་དད་པར་འགྱུར། །ཞེས་པའི་བར་དུ་ནི་ཚིགས་སུ་བཅད་པ་བཞི་ལ་དང་པོ་ཚིགས་བཅད་གཅིག་གིས་ནི་ཤཱ་རིའི་བུ་ཉིད་སྲས་ཀྱི་ཐུ་བོ་ཡིན་པའི་སྒོ་ནས་ཆོས་བཤད་པར་གསོལ་བ་དང་། དེའི་འོག་གི་ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་སྔོན་དེ་བཞིན་གཤེགས་པས་བྱིན་གྱིས་བརླབས་པ་ཤ་སྟག་གོ་ཞེས་གཞན་ལ༌[^965]གླེངས་ཏེ་གསོལ་བ་དང་། དེའི་འོག་གི་ཚིགས་བཅད་ཕྱེད་དང་གཉིས་ཀྱིས་ནི་བདག་དང་གཞན་གཉི་ག་ལས་གླེངས་ཏེ་གསོལ་བ་ལས་འདི་ནི་དང་པོའོ། །

[Block 956]
རྐང་གཉིས་ཀྱི་གཙོ་བོ༌[^966]ཞེས་པ་ནི་ལྷ་དང་མི་ཆོས་ཀྱི་སྣོད་དུ་གྱུར་པ་ཡིན་ལ་དེའི་གཙོ་བོ་བས་ན་བཅོམ་ལྡན་འདས་རྐང་གཉིས་ཀྱི་གཙོ་བོས་གསུངས་སོ། །

[Block 957 [HEADING]]
##### རྒྱུ་སྨིན་པ་ལས་གླེངས་ཏེ་ཆོས་བཤད་པར་གསོལ་བ། ^4-2-9-2-0

[Block 958]
མདོ་ལས། གང་དུ་ཁྱོད་ཀྱིས༌[^967]རྟག་པར་སྔོན་འཁོར་ན། །ཞེས་པ་ནས། གང་དག་དད་འགྱུར་ཁྱོད་ཀྱིས༌[^968]ཆོས་འདི་ལ། ཞེས་པའི་བར་དུ་ནི་རྒྱུ་སྨིན་པ་ལས་གླེངས་ཏེ། ཆོས་བཤད་པར་གསོལ་པའོ། །

[Block 959]
མདོ་ལས།

[Block 960 [HEADING]]
##### བདག་དང་གཞན་གཉི་ག་ལས་གླེངས་ཏེ་ཆོས་བཤད་པར་གསོལ་བ། ^4-2-9-3-0

[Block 961]
འདི་དག་བདག་འདྲ་བརྒྱ་ཕྲག་བཅུ་གཉིས་ཏེ། །ཞེས་པ་ནས། དེ་དག་དགའ་བའི་མཆོག་ཀྱང་བསྐྱེད་དུ་གསོལ། ཞེས་པའི་བར་དུ་ནི་བདག་དང་གཞན་གཉི་ག་ལས་གླེངས་ཏེ་ཆོས་བཤད་པར་གསོལ་བའོ། །

[Block 962 [HEADING]]
#### ངེས་པར་ལུང་སྟོན་པ་དང་ཁས་བླང་ཞིང་ལུང་སྟོན་པ། ^4-2-10-0

[Block 963 [HEADING]]
##### ལུང་བསྟན་པ་རྣམ་གཉིས་གླེངས་པ། ^4-2-10-1-0

[Block 964]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས་ཞེས་པ་ནས་ངས་ཁྱོད་ལ་བཤད་དོ་ཞེས་པའི་བར་དུ་ནི་ལུང་བསྟན་པ་རྣམ་པ༌[^969]བཞི་ལས༌[^970]ངེས་པར་ལུང་སྟོན་པ་དང་། ཁས་བླང་ཞིང་ལུང་སྟོན་པ་སྟེ་དེ་ཡང་སྔར་ནི་ལུང་བསྟན་པ་རྣམ་གཉིས་གླེངས། དེའི་འོག་ཏུ་ནི་སྙིགས༌[^971]མ་རྣམ་པ་ལྔ་དང་སྦྱར། ཐེ་ཚོམ་རྣམ་བཞི་བསྩལ་བ༌[^972]ལ་འདི་ནི་དང་པོ་སྟེ། ཁས་བླངས་པས་ལུང་བསྟན་པ་ཡང་བཅོམ་ལྡན་འདས་ཀྱིས༌[^973]བཤད་པར་གནང་བ་དང་། ང་རྒྱལ་ཅན་གྱི་རྣམས་བསལ་བར་སྟོན༌[^974]ཏོ། །

[Block 965]
ལེགས་པར་ཤིན་ཏུ་ཉོན་ལ་ཡིད༌[^975]ལ་ཟུང་ཤིག༌[^976]པ་ནི་དབང་པོ་བསྡུས་ཏེ་བཀའ་ཉན་དུ་གཟུང་བའོ། །

[Block 966]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཀྱིས་ཚིག་དེ་གསུངས་མ་ཐག་ཏུ་ཞེས་པ་ནས་འཁོར་དེ་ནས་དོང་ངོ་ཞེས་པའི་བར་དུ་ནི་ང་རྒྱལ་ཅན་གྱི་རྣམས་དོང་བ་བསྟན་ཏོ། །

[Block 967]
མདོ་ལས་འདི་ལྟར་ང་རྒྱལ་ཅན་གྱི༌[^977]ཞེས་པ་ནས་འཁོར་དེ་ནས་དོང་ངོ་ཞེས་པའི་བར་དུ་ནི་ང་རྒྱལ་ཅན་དེ་དག་ཅིའི་ཕྱིར་དོང་བའི་གཏན་ཚིགས་བསྟན་ཏེ། ཐོབ་པར་དཀའ་བ་རྣམ་པ་ལྔ༌[^978]སྟེ། མིའི་ལུས་ཐོབ་པ་དང་ཡུལ་གྱི་དབུས་སུ་སྐྱེ་བ་དང་དབང་པོ་ཚང་བ་དང་། དེ་བཞིན་གཤེགས་པ་འཇིག་རྟེན་དུ་བྱུང་བ་མཐོང་བ་དང་། དམ་པའི་ཆོས་ཐོས་པ་འདི་དག་དཀའ་བ་ལས་རྙེད་པ་ཡིན་ན་ང་རྒྱལ་ཅན་གྱི་འཁོར་འདི་རྣམས་ཅིའི་ཕྱིར་སྟན་ལ༌[^979]ལངས་ཏེ་དོང་ངོ་ཞེས་པའོ། །

[Block 968]
དེ་ནི་རྣམ་པ་གཉིས་ཀྱི་ཕྱིར༌[^980]སྡིག་པའི་རྣམ་པར་སྨིན་པ་སྟུག་པ་དང་། ང་རྒྱལ་ཅན་དུ་གྱུར་པའི་ཕྱིར་ཏེ། སྡིག་པ་སྟུག་ཆེས་པ་ནི་ཉོན་མོངས་པའི་སྒྲིབ་པ་དང་། ལས་ཀྱི་སྒྲིབ་པ་དང་རྣམ་པར་སྨིན་པའི་སྒྲིབ་པ་སྟེ། དེ་ཉིད་རང་གི་སྐྱོན་དུ་གྱུར་པའོ། །

[Block 969]
སྐྱོན་དེ་གསུམ་གྱི་སྒྲིབ་པས༌[^981]འཕགས་པའི་འབྲས་བུ་མི་ཐོབ༌[^982]ཅེས་པའོ། །

[Block 970]
ང་རྒྱལ༌[^983]ཞེས་པ་ནི་ང་རྒྱལ་རྣམ་པ་བདུན་ལས་འདི་ནི་ལྷག་པའི་ང་རྒྱལ་དང་། མ་ཐོབ་པ་ཐོབ་པར་སེམས་ཤིང་ལོག་པའི་ང་རྒྱལ་དང་ལྡན་པའོ། །

[Block 971]
འཕགས་པའི་འབྲས་བུ་མ་ཐོབ་པ་དང་། འདུས་མ་བྱས་མ་རྟོགས་པས༌[^984]སྣོད་དུ་མ་གྱུར་པའི་ཕྱིར་ལངས་ཏེ་དོང་ངོ་ཞེས་སྦྱར་རོ། །

[Block 972]
མདོ་ལས་བཅོམ་ལྡན་འདས་ཅང་མི་གསུང་བར་བཞུགས་སོ་ཞེས་པ་ནི་ངེས་པའི་འབྲས་བུ་སྨིན་པ་ནི་བཅོམ་ལྡན་འདས་ཀྱི༌[^985]མཐུས་ཀྱང་བསྟང་བ་མི་མཛད་པ་བསྟན་ཏོ། །

[Block 973]
མདོ་ལས་དེ་ནས་བཅོམ་ལྡན་འདས་ཀྱིས༌[^986]ཞེས་པ་ནས་དེའི་དོན་བཤད་དོ་ཞེས་པའི་བར་དུ་ནི་འཁོར་མ་བརྟགས་པ༌[^987]བསལ་ཏེ། སྣོད་དུ་གྱུར་པ་འཁོར་དམ་པ་ཉི་ཚེ་ལ་ཆོས་བཤད་པར་དགོངས་པའོ། །

[Block 974 [HEADING]]
###### མ་ཐོས་པ་ཐོས་པར་བྱ་བ། ^4-2-10-1-1-0

[Block 975]
མདོ་ལས་བཅོམ་ལྡན་འདས་ལ་སླར་ཉན་ཏོ་ཞེས་པ་ནས་བརྒྱ་ལམ་ན་རེས་འགའ་འབྱུང་ངོ་ཞེས་པའི་བར་དུ་ནི་འདི་མན་ཆད་མ་ཐོས་པ༌[^988]ཐོས་པར་བྱ་བ་དང་། འདི་བཤད་པར་བྱ་བའི་ཆོས་ཤེས་པར་དཀའ་བ་བསྟན་པ་དང་། དེ་བཞིན་གཤེགས་པས་གསུངས་པའི་ཐབས་ལ་སོགས་པ་ལ་བསྟེན་པ༌[^989]དང་། ཐེག་པ་གཅིག་པོ་ལ་གནས་པར་བྱ་བ་དང་། འཛིན་པ་རྣམ་གཉིས་བསྩལ་བ༌[^990]སྟོན་ཏེ། འདིས་ནི་མ་ཐོས་པ༌[^991]ཐོས་པར༌[^992]བྱ་བ་དང་། ཐོས་པར་དཀའ་བ་དང་དེའི་དཔེ་བསྟན་ཏོ། །

[Block 976]
འཁོར་ལོས་སྒྱུར་བའི༌[^993]རྒྱལ་པོ་ནམ་བྱུང་བའི་ཚེ་རྒྱ་མཚོ་བྲི་བར་གྱུར་པས་མེ་ཏོག་ཨུ་དུམ་བཱ་ར་འདི་འབྱུང་བ་བཞིན་སངས་རྒྱས་བཅོམ་ལྡན་འདས་འཇིག་རྟེན་དུ་བྱུང་བས་འཁོར་བའི་རྒྱུད་བསྲབས༌[^994]ཤིང་ཐེག་པ་ཆེན་པོའི་དོན་གསལ་བར༌[^995]འགྱུར༌[^996]ཞེས་པའི་དོན་ཏོ། །

[Block 977]
མདོ་ལས་ཤཱ་རིའི་བུ་དེ་བཞིན་དུ་ཞེས་པ་ནས་ང་ནི་གཞན་དུ་མི་སྨྲའོ་ཞེས་པའི་བར་དུ་ནི་དེ་བཞིན་གཤེགས་པའི་གསུང་ལ་ཡིད་ཆེས་པར་བྱ་བ་བསྟན༌[^997]ཏོ། །

[Block 978 [HEADING]]
###### བཤད་པར་བྱ་བའི་ཆོས་ཤེས་པར་དཀའ་བ། ^4-2-10-1-2-0

[Block 979]
མདོ་ལས་ཤཱ་རིའི་བུ་དེ་བཞིན་གཤེགས་པའི་ལྡེམ་པོ་དག་ནི་ཆུད་པར་དཀའོ་ཞེས་པ་ནི་བཤད་པར་བྱ་བ་བསྟན་ཏོ། །

[Block 980]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེས་པ་ནས་དེ་བཞིན་གཤེགས་པས་མཁྱེན་པའོ་ཞེས་པའི་བར་དུ་ནི་བཤད་པར་བྱ་བའི་དོན་མཚོན་པར་བྱ་བ་སྟེ། བརྟག་པ་དང་རྟོགས་པའི༌[^998]སྤྱོད་ཡུལ་ལས་འདས་པ་ནི་དེ་བཞིན་ཉིད་བདེན་པའི་དོན་ཏེ། ཚིག་གི་ཐ་སྙད་ཐམས་ཅད་ལས་འདས་པ་ཡིན་ན་བཅོམ་ལྡན་འདས་ཐབས་མཁས་པ་དང་ལྡན་པས་ཡི་གེ༌[^999]དང་ཚིག་འབྲུའི་སྒོ་ནས་ཐེག་པ་རྣམ་པ༌[^1000]གསུམ་གྱི་དོན་མཚོན་པའོ། །

[Block 981 [HEADING]]
###### གང་ལ་བརྟེན་པར་བྱ་བ། ^4-2-10-1-3-0

[Block 982]
མདོ་ལས་དེ་ཅིའི་ཕྱིར་ཞེ་ན་ཞེས་པ་ནས་འཇིག་རྟེན་དུ་བྱུང་སྟེ་ཞེས་པའི་བར་དུ་ནི་གང་ལ་བརྟེན་པར་བྱ་བའི་དོན་སྟོན་ཏེ། དེ་ཡང་བྱ་བ་གཅིག་པ་དེ་སྔར་གླེང་བ་དང་ཕྱིས་དགྲོལ་བ་ལ་འདི་ནི་དང་པོའོ། །

[Block 983 [HEADING]]
###### **གླེང་བ།** ^4-2-10-1-3-1-0

[Block 984]
གང་ལ་བརྟེན་པར་བྱ་བ་ནི་བཅོམ་ལྡན་འདས་ཉག་གཅིག་གིས་མཁྱེན་པའི་ཆོས་ཏེ་ཤེས་པར་དཀའ་བའི་དོན་ཏོ། །

[Block 985]
དོན་དེ་སེམས་ཅན་རྣམས་ལ་ཕན་གདགས་པའི་ཕྱིར་སོ་སོའི༌[^1001]དབང་པོ་དང་སྦྱོར་ཞིང་ཆོས་སྟོན་པ་མཛད་དོ། །
--- END BLOCKS ---
