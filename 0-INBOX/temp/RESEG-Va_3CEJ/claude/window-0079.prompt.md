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
[Block 2766]
མོ་ཞིག་ཡིན་ན་ནི་ཕ་ལ་མོའི་འདོད་ཆགས་སྐྱེའོ། །

[Block 2767]
བཟློག་པ་ནི་ཁོང་ཁྲོ་བ་སྐྱེ་བ༌[^1516]སྟེ། བཏགས་པ་ལས་འདི་སྐད་དུ་དེའི་ཚེ་དྲི་ཟ་ལ་སེམས་གཉིས་ལས་རྗེས་སུ་ཆགས་པ་དང་ལྡན་པའམ། ཁོང་ཁྲོ་བ་དང་ལྡན་པའི་སེམས་གང་ཡང་རུང་བའི༌[^1517]མངོན་དུ་གྱུར་པ་ཡིན་ནོ་ཞེས་འབྱུང་ངོ་། །དེ་ནི༌[^1518]གཉིས་ཀྱི༌[^1519]ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པས་ཡུལ་དེར་ཕྱིན་པ་དང་། དགའ་བར་འདོད་པའི༌[^1520]གནས་སྐབས་དེར་བདག་ཉིད་མོས་སོ། །

[Block 2768]
མངལ་གྱི་གནས་མི་གཙང་བ་དེར་ཕྱིན་ནས་དགའ་བ་སྐྱེས་ནས་གནས་སོ། །

[Block 2769]
དེ་ནས་དེའི་ཕུང་པོ་མཁྲང་པོར་འགྱུར་ལ་སྲིད་པ་བར་མ་ཡང་འགག་པར་འགྱུར་བས་ན་སྐྱེས་པ་ཡིན་ནོ། །

[Block 2770]
གལ་ཏེ་དེ་ཕོ་ཞིག་ཡིན་ན་ནི་མའི་ལྟོའི་གཡས་ཕྱོགས་སུ་སྙེས༌[^1521]ནས་རྒྱབ་རོལ་དུ་ཁ་བལྟས་ཏེ་ཙོག་ཙོག་པོར་སྐྱེའོ། །

[Block 2771]
གལ་ཏེ་མོ་ཞིག་ཡིན་ན་ནི་དེ་མའི་ལྟོའི་གཡོན་ཕྱོགས་སུ་སྙེས༌[^1522]ནས་ལྟོའི་མདུན་རོལ་དུ་ཁ་ལྟའོ། །

[Block 2772]
འོན་ཏེ་དེ་མ་ནིང་ཞིག་ཡིན་ན་ནི་དེ་འདོད་ཆགས་གང་དང་ལྡན་པ་དེ་བཞིན་དུ་གནས་སོ། །

[Block 2773]
སྲིད་པ་བར་མའི༌[^1523]དབང་པོ་ཐམས་ཅད་ཚང་བ་ཡིན་པའི་ཕྱིར་དབང་པོ་མ་ཚང་བ་མ་ཡིན་པ་སྟེ།[^1524] དེའི་ཕྱིར་མོར་གྱུར་པ་དང་། ཕོར་གྱུར་པ་ཞུགས་ནས་གནས་པའི༌[^1525]ལྟ་བ་བཞིན་དུ་གནས་སོ། །

[Block 2774]
ཕྱིས་ལུས་སྐྱེ་ཞིང་མ་ནིང་དུ་འགྱུར་རོ། །

[Block 2775]
ད་ནི་འདི་དཔྱད་པར་བྱ་སྟེ། ཅི་ལས་ཀྱི་དབང་གིས་ཁུ་ཆུ་དང་། ཁྲག་གི་འབྱུང་བ་ཆེན་པོ་དག་ཁོ་ན་འདིའི་དབང་པོའི་རྟེན་དུ་འགྱུར་རམ།

[Block 2776]
འོན་ཏེ་ལས་རྣམས་ལས།

[Block 2777]
དེ་དག་ལ་བརྟེན་ནས་འབྱུང་བ༌[^1526]ཁོ་ན་ཞིག་སྐྱེ་བར་འགྱུར་ཞེ་ན། ཁ་ཅིག་ན་རེ་དེ་དག་ཁོ་ན་ཡིན་ཏེ། ཁུ་ཆུ་དང་ཁྲག་དབང་པོ་མེད་པ་ན༌[^1527]ནི་འགག་ལ། ས་བོན་དང་མྱུ་གུ་འགག་པ་དང་། སྐྱེ་བའི་ཚུལ་དུ་དབང་པོ་དང་བཅས་པ་ནུར་ནུར་པོ་ཞེས་བྱ་བ་གང་ཡིན་པ་དེ་ནི་སྐྱེའོ། །

[Block 2778]
དེ་ལྟར་བཤད་ན་ཕ་མའི་ནུར་ནུར་པོ་མི་གཙང་བ་ལས་སྐྱེས་པ་ཞེས་བྱ་བ་དང་། དེ་བཞིན་དུ་དགེ་སློང་དག་ཁྱེད་ཀྱིས་ནི་ཡུན་རིང་པོ་ནས་དུར་ཁྲོད་སྐྱེད༌[^1528]དོ། །

[Block 2779]
ཁྲག་གི་ཐིགས་པ་བླངས་སོ་ཞེས་གསུངས་པའི་མདོའི་ཚིག་ལེགས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2780]
གཞན་དག་ན་རེ་འབྱུང་བ་གཞན་དག་ཁོ་ན་ཡིན་ཏེ། དཔེར་ན་ལོ་མའི་སྲིན་བུ་ལྟ་བུ་ཡིན་ལ། མི་གཙང་བ་ལ་བརྟེན་ནས་སྐྱེ་བ་ལ་དགོངས་ཏེ་གསུངས་པའི་ཕྱིར་མདོ་དང་ཡང་མི་འགལ་ལོ་ཞེས་ཟེར་རོ། །

[Block 2781]
རེ་ཞིག་སྒོ་ང་ལས་སྐྱེ་བ་དང་། མངལ་ནས་སྐྱེ་བའི་སྐྱེ་གནས་སུ་འཇུག་པ་ནི་དེ་ལྟ་བུའོ། །

[Block 2782]
གཞན་ལ་ནི་ཅི་རིགས་པར་བརྗོད་པར་བྱའོ་ཞེས་ཟེར་ཏེ། དེ་ལ་རིགས་པ་ནི་འདི་ཡིན་པར་སྣང་ངོ་། །དྲི་དང་གནས་ལ་མངོན་འདོད་གཞན། །དྲོད་གཤེར་ལས་སྐྱེ་བའི༌[^1529]སྐྱེ་གནས་སུ་སྐྱེ་བ་ནི་ལས་ཇི་ལྟ་བ་བཞིན་དུ་སྐྱེ་བའི་གནས་གཙང་མའམ་མི་གཙང་བར་དྲི་འདོད་པས་འགྲོའོ། །

[Block 2783]
རྫུས་ཏེ་སྐྱེ་བའི་སྐྱེ་གནས་སུ་སྐྱེ་བ་ནི་གནས་འདོད་པས་སོ། །ཇི་ལྟར་ན༌[^1530]དམྱལ་བ་དག་ཏུ་གནས་འདོད་ཅེ་ན། བློ་ཕྱིན་ཅི་ལོག་ཏུ་གྱུར་པའི་ཕྱིར་ཏེ། དེ་ནི་བདག་ཉིད་རླུང་དང་ཆར་པ་ཤིན་ཏུ་གྲང་མོ་དག་གིས་བཏབ༌[^1531]ནས་ཉེན་པ་དང་དམྱལ་བ་དག་ན་མེ་འབར་བ་མཐོང་སྟེ། དེའི་ཕྱིར་དྲོ་བར་འདོད་དེ་རྒྱུག༌[^1532]གོ། །

[Block 2784]
ཡང་བདག་ཉིད་རླུང་ཚ་བ་དང་ཉི་མ་དང་མེའི་གདུང་བ་དག་གིས་ཉེན་པ་དང་དམྱལ་བ་དག་ན་བསིལ་བ་མཐོང་བས་བསིལ་བ་འདོད་པས་རྒྱུག༌[^1533]གོ། །

[Block 2785]
སྔོན་གྱི་སློབ་དཔོན་དག་ན་རེ་བདག་ཉིད་གནས་སྐབས་གང་གིས་དེར་སྐྱེ་བར་འགྱུར་བའི་ལས་བྱས་པའི་གནས་སྐབས་དེ་ཡིན་པ་དང་། སེམས་ཅན་དེ་དག་ཀྱང་མཐོང་ནས་རྒྱུག༌[^1534]གོ་ཞེས་ཟེར་རོ། །

[Block 2786]
དེ་ལ་ལྷའི་སྲིད་པ་བར་མ་ནི་སྟན་ལས་ལྡང་བ༌[^1535]བཞིན་དུ་གྱེན་དུ་འགྲོའོ། །

[Block 2787]
མི་དང་དུད་འགྲོ་དང་། ཡི་དགས་རྣམས་ཀྱི་ནི་མི་ལ་སོགས་པ་བཞིན་ནོ། །

[Block 2788 [VERSE]]
དམྱལ་བ་ཡི་ནི་སྤྱིའུ་ཚུགས་ཡིན། །
ཡང་དག་སྡོམ་དང་དཀའ་ཐུབ་ཅན། །
དྲང་སྲོང་རྣམས་ལ་སྐུར་འདེབས་པ། །
དེ་དག་སྤྱིའུ་ཚུགས་དག་ཏུ་ནི། །

[Block 2789]
དམྱལ་བ༌[^1536]ཁོ་ནར་ལྟུང་བར་འགྱུར། །ཞེས་ཚིགས་སུ་བཅད་དེ་འབྱུང་བའི་ཕྱིར་རོ། །

[Block 2790 [VERSE]]
བློ་ནི་ཕྱིན་ཅི་ལོག་གྱུར་པས། །
རྩེ་དགས་འགྲོ་བའི་ཡུལ་དུ་འགྲོ། །

[Block 2791 [HEADING]]
##### མངལ་དུ་འཇུག་པ་བཞི། ^3-1-7-5-0

[Block 2792]
ཞེས་བཤད་པ། ཅི་ངེས་པར་སྲིད་པ་བར་མ་པ་ཐམས་ཅད་མའི་མངལ་དུ་དེ་ལྟར་འཇུག་གམ་ཞེ་ན། སྨྲས་པ་མ་ཡིན་ནོ། །

[Block 2793]
འོན་ཀྱང་མདོ་ལས་མངལ་དུ་འཇུག་པ་ནི་བཞི་ཞེས་གསུངས་ཏེ། བཞི་གང་ཞེ་ན། གཅིག་ནི་ཤེས་བཞིན་དུ་འཇུག་གོ། །

[Block 2794]
གནས་པ་དང་འབྱུང་བ་ནི་ཤེས་བཞིན་དུ་མ་ཡིན་ནོ། །

[Block 2795]
གཞན་ནི་གནས་པ་ཡང་ཤེས་བཞིན་དུ་ཞེས་བྱ་བར་སྦྱར་ཏེ། ཡང་ཞེས་བྱ་བའི་སྒྲས་ནི་འཇུག་པ་ཡང་ངོ་། །གཞན་ནི། འབྱུང་བའང་། ཤེས་བཞིན་དུ་སྟེ། ཡང་ཞེས་བྱ་བ་ནི་འཇུག་པ་དང་། གནས་པའོ། །

[Block 2796]
གཞན་ནི་ཐམས་ཅད་རྨོངས། ལ་ལ་ནི་ཐམས་ཅད་ཤེས་བཞིན་མ་ཡིན་པར་འགྱུར་ཏེ། འཇུག་པ་ཡང་ཤེས་བཞིན་མ་ཡིན་ལ་གནས་པ་དང་འབྱུང་བ་ཡང་ཤེས་བཞིན་མ་ཡིན་ནོ། །

[Block 2797]
མངལ་དུ་འཇུག་པ་དེ་བཞི་ནི་ཚིགས་སུ་བཅད་པ་བསྡེབ་པ་དང་མཐུན་པར་བྱ་བའི་ཕྱིར་བཟློག་སྟེ་བསྟན་ཏོ། །

[Block 2798]
སྒོ་ང་ལས་སྐྱེས་རྟག་ཏུའོ། །

[Block 2799]
སེམས་ཅན་སྒོ་ང་ལས་སྐྱེས་པ་ནི་རྟག་ཏུ༌[^1537]ཐམས་ཅད་རྨོངས་པ་ཁོ་ནར་འགྱུར་རོ། །

[Block 2800]
སྒོ་ང་ལས་སྐྱེས་པ་ཇི་ལྟར་སྐྱེ་གནས་སུ་འཇུག་ཅེ་ན། གང་ཞིག་སྐྱེ་བར་འགྱུར་བ་དེ་ཡང་སྒོ་ང་ལས་སྐྱེས་པ་ཞེས་བྱའོ། །

[Block 2801]
ཡང་ན་འབྱུང་བར་འགྱུར་བའི་མིང་གིས་བསྟན་ཏེ། དཔེར་ན་མདོ་ལས་འདུས་བྱས་མངོན་པར་འདུ་བྱེད་དོ་ཞེས་གསུངས་པ་དང་། འཇིག་རྟེན་ན་འབྲས་ཆན་འཚེད་དོ། །

[Block 2802]
ཕྱེ་འཐག་གོ་ཞེས་པ༌[^1538]ལྟ་བུ་སྟེ། དེ་ལྟ་བས་ན་དེ་ནི་ཉེས་པ་མེད་དོ། །

[Block 2803]
ཡང་ཇི་ལྟར་ན་ཤེས་བཞིན་མ་ཡིན་པར་མའི་མངལ་དུ་འཇུག་ཅིང་འབྱུང་བའི་བར་དུ་ཡིན་པའམ། ཇི་ལྟར་ན་ཤེས་བཞིན་དུ་ཡིན་ཞེ་ན། རེ་ཞིག་སེམས་ཅན་དབང་ཐང་ཆུང་བར་གྲགས་པ་མའི་མངལ་དུ་འཇུག་པ་ལ་འདི་སྙམ་དུ་རླུང་ལངས་པའམ། ཆར་པ་འབབ་པ་འམ། གྲང་བའམ། ཡུལ་ངན་ནམ། སྐྱེ་བོ་ཕལ་པོ་ཆེའི་ཚོགས་ཀུ་ཅོ་འདོན་པ་སྙམ་བྱེད་ནས། མ་ལ་རྩྭ་ཐིབས་པོའམ། ནགས་ཐིབས་པོའམ། རྩྭའི་སྤྱིལ་པོའམ། ལོ་མའི་སྤྱིལ་པོར་འཇུག་པའམ། ཤིང་དྲུང་ངམ། རྩིག་པའི་དྲུང་དུ་འགྲོའོ། །

[Block 2804]
གནས་ན་ཡང་འདི་དག་ཏུ་གནས་པར་བྱའོ། །

[Block 2805]
འབྱུང་ན་ཡང་འདི་དག་ནས་འབྱུང་ངོ་སྙམ་དུ་ལོག་པའི་འདུ་ཤེས་དང་མོས་པ་དག་འབྱུང་བར་འགྱུར་རོ། །
--- END BLOCKS ---
