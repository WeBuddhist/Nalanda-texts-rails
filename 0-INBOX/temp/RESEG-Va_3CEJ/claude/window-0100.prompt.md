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
[Block 3501]
[^2005]ཇི་ལྟར་འཛམ་བུའི་གླིང་ལ་དཔག་ཚད་ཉིས་སྟོང་ཉིས་སྟོང་ཡོད་པ་བཞིན་ནོ། །

[Block 3502]
གཅིག་ལ་དཔག་ཚད་སུམ་བརྒྱ་ལྔ་བཅུའོ། །

[Block 3503]
ངོས་བཞི་པ་ལ་ནི་དཔག་ཚད་སུམ་བརྒྱ་ལྔ་བཅུའོ། །

[Block 3504 [HEADING]]
###### བ་ལང་སྤྱོད་གླིང། ^3-2-1-6-3-0

[Block 3505 [VERSE]]
བ་ལང་སྤྱོད་གླིང་ཟླུམ་པོ་སྟེ། །
སྟོང་ཕྲག་ཕྱེད་དང་བརྒྱད་ཡིན་ནོ། །

[Block 3506]
འདི་ནས་ནུབ་ཕྱོགས་ཀྱི་རི་རབ་ཀྱི་ངོས་རོལ་ན་བ་ལང་སྤྱོད་ཀྱི་གླིང་ཡོད་དེ། དཔག་ཚད་བདུན་སྟོང་ལྔ་བརྒྱའོ། །

[Block 3507]
དེ་ནི་ཟླ་བ་ཉ་བ༌[^2006]བཞིན་དུ་ཀུན་ནས་ཟླུམ་པོ་ཡིན་ཏེ། དེ་དབུས་སྟོང་ཕྲག་ཕྱེད་དང་གསུམ། །ཆུ་ཞེང་དུ་ནི་དཔག་ཚད་སྟོང་ཕྲག་ཕྱེད་དང་གསུམ་མོ། །

[Block 3508 [HEADING]]
###### སྒྲ་མི་སྙན། ^3-2-1-6-4-0

[Block 3509]
[^2007]སྒྲ་མི་སྙན་བརྒྱད་གྲུ་བཞིར༌[^2008]མཉམ། །འདི་ནས་བྱང་ཕྱོགས་ཀྱི་རི་རབ་ཀྱི་ངོས་ལ༌[^2009]བྱང་གི་སྒྲ་མི་སྙན་གྱི་གླིང་ཡོད་དེ། ཀུན་དུ་དཔག་ཚད་བརྒྱད༌[^2010]སྟོང་ཡོད་དོ། །

[Block 3510]
དབྱིབས་ནི་ཁྲིའུ་བཞིན་དུ་ཀུན་ནས༌[^2011]གྲུ་བཞི་སྟེ། ཇི་ལྟར་ངོས་གཅིག་ལ་དཔག་ཚད་ཉིས་སྟོང་ཡོད་པ་ལྟར་གཞན་དག་ཀྱང་དེ་དང་འདྲ་སྟེ། ཅུང་ཟད་ཀྱང་ལྷག་མ༌[^2012]མེད་དོ། །

[Block 3511]
གླིང་གང་གི་དབྱིབས་ཅི་འདྲ་བ་དེ་ན་གནས་པའི་མི་རྣམས་ཀྱི་གདོང་གི་དབྱིབས་ཀྱང་དེ་དང་འདྲའོ། །

[Block 3512 [HEADING]]
##### བར་གྱི་གླིང་བརྒྱད། ^3-2-1-7-0

[Block 3513]
ཡང་དེ་དག་གི་བར་བར་ན་བར་གྱི་གླིང་རྣམས་མངོན་པར་གྲུབ་པ་དེ་དག་ནི་གང་ཡིན། དུ་ཞིག་ནི་ཡོད་ཅེ་ན།

[Block 3514 [VERSE]]
དེ་ཡི་བར་གྱི་གླིང་བརྒྱད་ནི། །
ལུས་དང་ལུས་འཕགས་སྒྲ་མི་སྙན། །
སྒྲ་མི་སྙན་གྱི་ཟླ་དང་ནི། །
རྔ་ཡབ་དང་ནི་རྔ་ཡབ་གཞན། །

[Block 3515]
གཡོ་ལྡན་དང་ནི་ལམ་མཆོག་འགྲོ། །དེ་ལ་ལུས་དང་ལུས་འཕགས་ནི་ཤར་གྱི་ལུས་འཕགས་ཀྱི་གླིང༌[^2013]འཁོར་ཡིན་ནོ། །

[Block 3516]
སྒྲ་མི་སྙན་དང་སྒྲ་མི་སྙན་གྱི་ཟླ་ནི་བྱང་གི་སྒྲ་མི་སྙན་གྱིའོ། །

[Block 3517]
གཡོ་ལྡན་དང་ལམ་མཆོག་འགྲོ་ནི་ནུབ་ཀྱི་བ་ལང་སྤྱོད་ཀྱིའོ། །

[Block 3518]
རྔ་ཡབ་དང་རྔ་ཡབ་གཞན་ནི་འཛམ་བུའི་གླིང་གི༌[^2014]སྟེ། ཐམས་ཅད་ན་ཡང་མི་རྣམས་གནས་སོ། །

[Block 3519]
ཁ་ཅིག་ན་རེ། གཅིག་ན་སྲིན་པོ་དག་གནས་སོ་ཞེས་ཟེར་རོ། །

[Block 3520 [HEADING]]
##### རི་ནག་པོ་དང་གངས་རི་དང་མཚོ་མ་དྲོས་པ། ^3-2-1-8-0

[Block 3521]
འདི་ནས་བྱང་དུ་རི་ནག་པོ། །དགུ་འདས་གངས་རིའོ། །

[Block 3522]
འཛམ་བུའི་གླིང་འདིའི་བྱང་ཕྱོགས་འཛམ་བུའི་གླིང་འདི་ཉིད་ན་རི་ནག་པོ་གསུམ་ཡོད་དོ། །

[Block 3523]
དེ་དག་འདས་ནས་ཡང་གསུམ་ཡོད་དེ། [^2015]དེ༌[^2016]འདས་ནས་ཡང་གསུམ་ཡོད་དོ། །

[Block 3524]
[^2017]རི་ནག་པོ་དགུ་འདས་པའི་ཕ་རོལ་ན་གངས་རི་ཡོད་དོ། །

[Block 3525]
དེ་ནས་ནི།

[Block 3526 [VERSE]]
སྤོས་ངད་ལྡང་བའི་ཚུ་རོལ་ན། །
ཆུ་ཞེང་ལྔ་བཅུ་ཡོད་པའི་མཚོ། །

[Block 3527]
གངས་རི་དེའི་ཕ་རོལ་རི་སྤོས་ཀྱི་ངད་ལྡང་བའི༌[^2018]ཚུ་རོལ་ན་མཚོ་མ་དྲོས་པ་ཞེས་བྱ་བ་གནས་པ༌[^2019]ལས་ཆུ་བོ་ཆེན་པོ་བཞི་པོ་གང་གཱ་དང་། སིན་དྷུ་དང་། སི་ཏ་དང་། པཀྵུ་འབབ་པ་ཡོད་དོ། །

[Block 3528]
དེའི༌[^2020]ཞེང་དུ་ཡང་དཔག་ཚད་ལྔ་བཅུ་ཡོད་ལ། ཆུར་ཡང་དཔག་ཚད་ལྔ་བཅུ་ཡོད་དེ། ཡན་ལག་བརྒྱད་དང་ལྡན་པའི་ཆུས་གང་ངོ་། །དེར་ནི་རྫུ་འཕྲུལ་དང་མི་ལྡན་པའི་མིས་འགྲོ་བར་དཀའོ། །

[Block 3529]
དེ་ཉིད་ཀྱི་དྲུང་ན་གང་ལ་འབྲས་བུ་མངར་པོ་དག་ཡོད་པ་ཤིང་འཛམ་བུ་ཞེས་བྱ་བ་མངོན་པར་འགྲུབ་སྟེ། དེའི་དབང་གིས་འདི་འཛམ་བུའི་གླིང་ཞེས་བྱ་བར་གྲགས་སོ། །

[Block 3530]
ཡང་ན་དེའི་འབྲས་བུའི་དབང་གིས་འཛམ་བུའི་གླིང་ཞེས་བྱ་བར་གྲགས་སོ། །

[Block 3531 [HEADING]]
##### དམྱལ་བའི་སྣོད་རྣམས་ཀྱི་གནས་པ། ^3-2-1-9-0

[Block 3532]
དམྱལ་བ་རྣམས༌[^2021]ནི་གང་རོལ་ན་ཡོད། ཚད་ནི་ཇི་ཙམ་ཞེ་ན།

[Block 3533 [HEADING]]
###### མནར་མེད་པ། ^3-2-1-9-1-0

[Block 3534 [VERSE]]
འདི་འོག་སྟོང་ཕྲག་ཉི་ཤུ་ན། །
མནར་མེད་པའོ་དེ་ཙམ་མོ། །

[Block 3535]
འཛམ་བུའི་གླིང་འདི་ཉིད་ཀྱི་འོག་དཔག་ཚད་ཉི་ཁྲི་ན་དམྱལ་བ་ཆེན་པོ་མནར་མེད་པ་ཡོད་དེ།

[Block 3536 [VERSE]]
[^2022]གནམ་འཕང་དང་རྒྱར་ནི་དཔག་ཚད་ཉི་ཁྲིའོ། །
དེའི་འོག་གཞི་ཡང་དེ་དང་འདྲ་སྟེ།
འདི་ནས་ནི་དཔག་ཚད་བཞི་ཁྲི་ཡོད་དོ། །

[Block 3537]
སྡུག་བསྔལ༌[^2023]བར་ཆད་མེད་པས་ན་མནར་མེད་པའོ། །

[Block 3538]
གཞན་དག༌[^2024]ནི་སྡུག་བསྔལ་བར་ཆད་དང་བཅས་པ་ཡིན་ཏེ། འདི་ལྟ་སྟེ། ཡང་སོས་ན་ནི་ལུས་རྣམས་བཅད་ཅིང་ཕུག་ལ་བཏགས་ཀྱང་རླུང་གྲང་མོ་དག༌[^2025]ལངས་ན་སེམས་ཅན་དེ་དག་ཡང་སོས་པར་འགྱུར་བས་དེའི་ཕྱིར་ཡང་སོས་ཡིན་ནོ། །

[Block 3539]
གཞན་དག་ན་རེ་དེ་ན་བདེ་བའི་གནས་སྐབས་མེད་པས་ན་མནར་མེད་པ༌[^2026]སྟེ། གཞན་དག་ན་ཡང་བདེ་བའི་ཚོར་བ་རྣམ་པར་སྨིན་པ་ལས་བྱུང་བ༌[^2027]ནི་མེད་ཀྱི་རྒྱུ་མཐུན་པར༌[^2028]བྱུང་བ་ནི་འགག་པ་མེད་དོ་ཞེས་ཟེར་རོ། །

[Block 3540 [HEADING]]
###### དམྱལ་བ་བདུན། ^3-2-1-9-2-0
--- END BLOCKS ---
