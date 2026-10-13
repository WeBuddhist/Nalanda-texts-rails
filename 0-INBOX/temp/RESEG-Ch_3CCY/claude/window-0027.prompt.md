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
སེམས་ཅན་རང་གི་ལས་ཀྱང་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་ཏེ། སེམས་ཅན་མི་རྣམས་ཀྱི་རང་གི་ལས་ལ་ལས་ནི་སྦྱིན་པ་སྦྱིན་པར་བྱེད་པའོ་ཞེས་བྱ་བའི་ཚིག་ལས་ལུས་ཞིག་ན་ནོར་དང་འབྲུ་ལ་སོགས་པ་འཇོག་པར་བྱེད་ལ། ལས་ནི་འཇིག་རྟེན་ཕ་རོལ་ཏུ༌[^671]རྗེས་སུ་འབྲང་བའི་ཕྱིར་ལས་ཀྱང་གང་གི་རང་གི་བདེ༌[^672]ནི་རང་གི་ལས་སོ། །

[Block 947]
དེས་ན་ཡང་དེའི་ལས་ཡོད་ལ། སེམས་ཅན་དེའང་ཡོད་པས་དངོས་པོ་རྣམས་རང་བཞིན་མེད་པ་མ་ཡིན་ནོ་ཞེས་བྱའོ། །

[Block 948]
ལས་རྣམ་པར་འཇིག་པ་མེད་པར་ཡང་དེ་བཞིན་གཤེགས་པས་གསུངས་ཏེ།

[Block 949 [VERSE]]
ལུས་ཅན་རྣམས་ཀྱི་ལས་རྣམས་ནི། །
སྐལ་བ༌[^673]བརྒྱར་ཡང་ཆུད་མི་ཟ། །
ཚོགས་པ་རྙེད་ནས་དུས་སུ་ནི། །
འབྲས་བུ་གདོན་མི་ཟ་བར་སྨིན། །

[Block 950]
ཞེས་བྱ་བ་ལ་སོགས་པས་ཀྱང་ལས་མེད་ན་ཆུད་མི་ཟ་བའི་ཚིག་རུང་བ་མ་ཡིན་ནོ། །

[Block 951]
དེའི་ཕྱིར་ལས་ཡོད་ལ་ལས་ཡོད་པའི་ཕྱིར་དངོས་པོ་རྣམས་རང་བཞིན་དང་བཅས་པའོ་ཞེས་བྱའོ། །

[Block 952]
འདིར་སྨྲས་པ། དངོས་པོ་རྣམས་ཀྱི་རང་བཞིན་མེད་པ་ལ་ལུང་འདིས་གནོད༌[^674]པ་མ་ཡིན་ཏེ། ཅིའི་ཕྱིར་ཞེ་ན། གང་གི་ཕྱིར་སྔར་ཉིད་དུ་དེ་ལྟ་བུ་ལ་སོགས་པའི་ལུང་འཇིག་རྟེན་གྱི་ཐ་སྙད་ཀྱི་དབང་གིས་གསུངས་སོ་ཞེས་བསྒྲུབས་པ་རྗེས་སུ་གནས་སོ། །

[Block 953]
འདི་དག་ཀྱང་གདོན་མི་ཟ་བར་ཁས་བླང་བར་བྱ་སྟེ། ཅིའི་ཕྱིར་ཞེ་ན། [^675]གང་གི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱིས།

[Block 954 [HEADING]]
### ཚིགས་བཅད་སོ་བཞི་པ། ^1-34-0

[Block 955 [VERSE]]
ལས་རྣམས་རང་བཞིན་མེད་གསུངས་ཏེ། །
མ་སྐྱེས་གང་དེ་ཆུད་མི་ཟ། །
དེ་ལས་ཀྱང་ནི་བདག་འཛིན་མེད། །
དེས་བསྐྱེད་འཛིན་པའང་རྣམ་རྟོག་ལས། །

[Block 956]
དེ་ལ་མི་རྟག་དང་ལྡན་འདུས་བྱས་རྣམས། །ཞེས་གསུངས་པས་ན། ལས་ཀྱང་མི་རྟག་གོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ། གང་མི་རྟག་པ༌[^676]དེ་ཡང་རང་བཞིན་མེད་པའོ་ཞེས་གསུངས་པར་འགྱུར་ཏེ། ངོ་བོ་ཉིད་ནི་གཞན་དུ་མི་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 957]
དེ་ཡང་གལ་ཏེ་རང་བཞིན་ཡོད་པ་ལ་དགོངས་ནས་ལས་ཡོད་དོ་ཞེས་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པར་གྱུར་ན། སླར་ཡང་ལས་མི་རྟག་པར་གསུང་བར་མི་འགྱུར་ཏེ། དེ་ནི་མི་རྟག་པ་དང་རང་བཞིན་ཡོད་པ་འགལ་བའི་ཕྱིར་རོ། །

[Block 958]
བཅོམ་ལྡན་འདས་ཀྱིས་ཀྱང་། མ་རིག་པའི་རྐྱེན་གྱིས་འདུ་བྱེད་དུ་གསུངས་ལ། རང་བཞིན་ཡོད་བཞིན་པ་ལ་བརྟེན་ནས་སྐྱེ་བ་འཐད་པ་མ་ཡིན་ནོ། །

[Block 959]
དེའི་ཕྱིར་བཅོམ་ལྡན་འདས་ཀྱི་བཀའ་ནི་ལས་རང་བཞིན་མེད་པ་གསལ་བར་བྱེད་པ་ཉིད་དོ་ཞེས་བསྒྲུབ་པར་བྱ་བའི་ཕྱིར་གསུངས་པ། ལས་རྣམས་རང་བཞིན་མེད་གསུངས་པ། །ཞེས་བྱ་བ་ལ། གང་ཁོ་ནས་རང་བཞིན་མེད་པ་དེ་ཉིད་ཀྱིས་ན་མ་སྐྱེས་ལ། གང་ཡང་མ་སྐྱེས་པ་དེ་ཉིད་ཀྱིས་ན་དེ་ནི་འཇིག་པ་མེད་པར་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་སོ། །

[Block 960]
ལས་རྣམས་ཆུད་མི་ཟ་ཞེས་བྱ་བ་ལ་སོགས་པས་གང་ཡང་འདི་ལྟར་མི་འདོད་ན། དེ༌[^677]ལས་འདུས་བྱས་སུ་ཡང་ཁས་བླང་བར་མི་བྱ་སྟེ། འདི་དག་ཕན་ཚུན་འགལ་བའི་ཕྱིར་རོ། །

[Block 961]
གང་ཡང་འདི་ལྟར་ལས་རང་བཞིན་གྱིས་མ་སྐྱེས་ལ་དེས་ན་རང་བཞིན་མེད་པའི་ཕྱིར་རོ། །

[Block 962]
གང་ཞིག་ལས་ནི་འདི་དག་སྟེ། རྣམ་པར་ཤེས་པ་དང་མིང་དང་གཟུགས་དང་སྐྱེ་མཆེད་དྲུག་དང་རེག་པ་དང་ཚོར་བ་ཞེས་བྱ་བ་ཡན་ལག་ལྔས་རབ་ཏུ་འཇུག་པ་ནི། འཇིག་རྟེན་པས་བདག་ཏུ་མངོན་པར་རློམ་པའི་རྒྱུ་མཚན་ཏེ། དེ་ལ་བདག་གི་ཞེས་འདིར་འཛིན་པའོ་ཞེས་བྱའོ། །

[Block 963]
བདག་ཏུ་འཛིན་པའི་མིང་ཅན་དེ་ཡང་རང་བཞིན་མེད་པའི་ལས་ཀྱིས་བསྐྱེད་པའི་ཕྱིར་རང་བཞིན་མེད་པའོ་ཞེས་གསལ་བར་ཁོང་དུ་ཆུད་པར་བྱའོ། །

[Block 964]
ཡང་ན་འདི་སྙམ་དུ་སེམས་ན། རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་ཡན་ལག་ལྔ་པོ་རང་བཞིན་མེད་དེ། རང་བཞིན་མེད་པའི་ལས་ཀྱིས་བསྐྱེད་པའི་ཕྱིར་རོ་ཞེས་ཡིན་དུ་ཆུག་ན་ཡང་གང་ཡང་བདག་ཏུ་འཛིན་པ་དང་འཛིན་པའི་མཚན་ཉིད་ཅན་འདི་ཡང་རང་བཞིན་མེད་པའི་ལས་ཀྱིས་བསྐྱེད་པའི་ཕྱིར་རང་བཞིན་དང་བཅས་པར་འགྱུར་རོ་ཞེ་ན། འདི་དག་ཀྱང་མེད་དེ།

[Block 965 [VERSE]]
ཅིའི་ཕྱིར་ན་གང་གི་ཕྱིར། །
དེས་བསྐྱེད་འཛིན་པའང་རྣམ་རྟོག་ལས། །

[Block 966]
གང་ཡང་འདི་བདག་ཏུ་སྒྲོ༌[^678]བཏགས་པས་བསྐྱེད་པའི་ངར་འཛིན་པ་དེ་ཡང་རང་བཞིན་མེད་པའི་ཚུལ་བཞིན་མ་ཡིན་པ་ཡིད་ལ་བྱེད་པའི་མཚན་ཉིད་ཅན་གྱི་རྣམ་པར་རྟོག་པས་བསྐྱེད་པའི་ཕྱིར་རང་བཞིན་མེད་པ་ཁོ་ནའོ་ཞེས་བྱ་བ་གྲུབ་བོ། །

[Block 967]
གདོན་མི་ཟ་བར་འདི་ནི་འདི་ལྟར་ཁས་བླང་བར་བྱ་སྟེ། འདི་ལྟ་སྟེ་ལས་ནི་རང་བཞིན་མེད་པའོ་ཞེས་གསུངས་སོ། །

[Block 968]
གཞན་དུ་ན།

[Block 969 [HEADING]]
### ཚིགས་བཅད་སོ་ལྔ་པ། ^1-35-0

[Block 970 [VERSE]]
གལ་ཏེ་ལས་ལ་རང་བཞིན་ཡོད། །
དེ་སྐྱེས་ཐེར་ཟུག་བདག་དངོས་འགྱུར། །
ལས་ཀྱང་སྡུག་བསྔལ་རྣམ་སྨིན་དུ། །
མི་འགྱུར་དེ་ཕྱིར་བདག་ཏུ་འགྱུར། །

[Block 971]
བདག་ཅེས་བྱ་བའི་དངོས་པོ་འདིའོ་ཞེས་བྱ་བ་རྣམ་པར་ཤེས་པ་ལ་སོགས་པའི་ཡན་ལག་ལྔ་པོ༌[^679]ཞེས་བརྗོད་དོ། །

[Block 972]
གལ་ཏེ་ལས་ལ་རང་བཞིན་ཡོད་ན་དེ་མི་རྟག་པར་མི་འགྱུར་ཏེ། རང་བཞིན་ནི་མི་འགྱུར་བའི་ཕྱིར་དང་། རྟག་པའི་ལས་ཀྱིས་བསྐྱེད་པ་ཡང་རྒྱུ་དང་འདྲ་བར་འབྲས་བུ་འཇུག་པས། རྟག་པའི་བདག་གི་དངོས་པོར་འགྱུར་ལ་རྟག་པ་ཉིད་དུ་གྱུར་ན་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་དེ་དག་གི་ལས་ཀྱིས་སྡུག་བསྔལ་གྱི་རྣམ་པར་སྨིན་པ་འབྱུང་བར་མི་འགྱུར་རོ། །

[Block 973]
ལས་ནི་མི་རྟག་པས་རྣམ་པར་སྨིན་པར་འབྱུང་སྟེ། གང་མི་རྟག་པ་དེ་སྡུག་བསྔལ་ལོ༌[^680]ཞེས་སྡུག་བསྔལ་གྱི་རྣམ་པར་སྨིན་པར་འགྱུར་ལ། རྟག་པར་གྱུར་ན་ལས་ལ༌[^681]སྡུག་བསྔལ་གྱི་རྣམ་པར་སྨིན་པར་མི་འགྱུར་རོ། །

[Block 974]
གང་མི་རྟག་པ་དེ་ཡང་བདག་མེད་པའོ་ཞེས་གསུངས་སོ། །

[Block 975]
གང་གི་ཚེ་ཡང་ལས་ཀྱི་འབྲས་བུ་དང་ལས་ཐེར་ཟུག་པ་ཡིན་ནམ།[^682] དེའི་ཕྱིར་བདག་ཏུ་འགྱུར་ལ། དེ་ལས་ཀྱང་ཆོས་ཐམས་ཅད་བདག་མེད་པའོ་ཞེས་སྟོན་པར་མི་རིགས་སོ། །

[Block 976]
དེས་ན་གདོན་མི་ཟ་བར་ལས་རང་བཞིན་མེད་པར་རིག་པར་བྱའོ། །

[Block 977]
ཡང་ལས་རང་བཞིན་མེད་པའི་འཐད་པ་ཅི་ཞིག་ཏུ་རིག་པར་བྱ་ཞེ་ན། གསུངས་པ།

[Block 978 [HEADING]]
### ཚིགས་བཅད་སོ་དྲུག་པ། ^1-36-0

[Block 979 [VERSE]]
ལས་ནི་རྐྱེན་སྐྱེས་ཡོད་མིན་ཞིང་། །
རྐྱེན་མིན་ལས་སྐྱེས་ཅུང་ཟད་མེད། །
འདུ་བྱེད་རྣམས་ནི་དྲི་ཟ་ཡི། །
གྲོང་ཁྱེར་སྒྱུ་མ་སྨིག་རྒྱུར་མཚུངས། །

[Block 980]
གལ་ཏེ་ལས་ཞེས་བྱ་བ་ཅུང་ཟད་ཡོད་ན། ངེས་པར་དེ་ནི་རྐྱེན་ལས་སྐྱེས་པའང༌[^683]རྐྱེན་མེད་པ་ལས་སྐྱེ་བར་འགྱུར། རེ་ཞིག་གལ་ཏེ་རྐྱེན་ལས་སྐྱེ་བར་འདོད་ན། ངེས་པར་འབྲས་བུ་རྐྱེན་ལས༌[^684]ཡོད་པར་འགྱུར་ལ། མ་སྐྱེས་པ་རྐྱེན་ལ་ཡོད་པར་ནུས་པ་མ་ཡིན་ཏེ། འབྲས་བུ་མ་སྐྱེས་ན་ཡང་སའི་རྒྱུ་དང་རྐྱེན་ལ་དེའི་འབྲས་བུ༌[^685]རྐྱེན་ལ་མེད་པ་ཞིག་རྐྱེན་ལས་སྐྱེ་ན། དེའི་ཚེ་རྐྱེན་མ་ཡིན་པ་ལས་ཀྱང་སྐྱེ་བར་འགྱུར་ལ་དེ་དག་ཀྱང་མེད་དོ་ཞེས་བྱ་བས་དེས་ན་རྐྱེན་ལས་སྐྱེ་བའི་ལས་ཅུང་ཟད་མེད་དོ། །

[Block 981]
རྐྱེན་མེད་པ་ཡང་རྒྱུ་མེད་པས་འབྲས་བུ་ཅུང་ཟད་ཀྱང་མི་སྲིད་དོ་ཞེས་བྱའོ། །

[Block 982]
དེས་ན་ལས་མེད་དོ། །

[Block 983]
གང་གི་ཚེ་ལས་མེད་པ་དེའི་ཚེ་རྣམ་པར་ཤེས་པ་ལ་སོགས་པ་མེད་པར་གྱུར་པས་ཉེ་བར་ལེན་པ་མེད་པས་ཉེ་བར་ལེན་པ་པོ་ཡང་མེད་དོ་ཞེས་བྱ་སྟེ། འདུས་བྱས་ཐམས་ཅད་མི་རྟག་པ་ཆོས་ཐམས་ཅད་བདག་མེད་པའོ་ཞེས་བྱ་བར་འགྱུར་ཏེ། རང་བཞིན་ཁས་མ་བླངས་ན་ཐམས་ཅད་ལེགས་པར་གནས་པར་འགྱུར་རོ། །

[Block 984]
གལ་ཏེ་དངོས༌[^686]རྣམས་རང་བཞིན་མེད་པའོ། །ཞེས་འཆད་ན། འོ་ན་དེ་ལྟར་གྱུར་ན་དངོས་པོ་ཐམས་ཅད་མེད་དོ་ཞེས་བྱ་བ་ཐོབ་པར་འགྱུར་རོ། །

[Block 985]
སྨྲས་པ། རང་བཞིན་མེད་པའི་དོན་ནི་མེད་པའི་དོན་མ་ཡིན་ཏེ། འོན་ཀྱང་འཁྲུལ་བའི་དོན་ཏེ། བརྫུན་ཞིང་སླུ་བའི༌[^687]ཆོས་ཅན་ཉིད་ཀྱི་དོན་ཏོ། །
--- END BLOCKS ---
