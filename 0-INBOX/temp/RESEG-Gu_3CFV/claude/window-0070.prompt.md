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
[Block 2451]
དཀན་གཟར་པོ་མ་ཡིན་པར་རོ། །

[Block 2452]
ལམ་གྱི་བཞི་མདོར་མི་བྱའོ། །

[Block 2453]
དེས་འབབ་ཆུ་དྲག་པོའི༌[^1551]རྒྱུན་ལས་བཟློག་སྟེ་ཆུ་མི་བཅུ་བར་རོ། །

[Block 2454]
བཤང་གཅི་ཡན་ཆད་ནི་མི་ན་བ་ལའོ། །

[Block 2455]
ལངས་ཏེ་བཤང་གཅི་མི་བྱའོ་ཞེས་བྱ་བ་འདིའི་གོང་རོལ་དུ་དེ་དག་ལ་ནི་མིན་བའོ་ཞེས་བྱ་བར་སྦྱར་བར་བྱའོ། །

[Block 2456]
དེར་བཤང་བ་དང་གཅི་བ་ལ་དེ་དང་ཡང་དག་པར་ལྡན་པའི་རྣམ་པ་དེ་རྣམས་ལ་མི་བྱའོ་ཞེས་སྦྱར་བར་བྱའོ། །

[Block 2457]
འདུག་པ་ལ་འགྲེང་སྟེ་ཆོས་མི་བཤད་པར་རོ། །

[Block 2458]
ཉལ་བ་ལ་འདུག་སྟེ་མི་བཤད་པར་རོ། །

[Block 2459]
སྟན་མཐོན་པོ་ལ་འདུག་པ་ལ་སྟན་དམའ་བ་ལ་འདུག་སྟེ་མི་བཤད་པར་རོ་ཞེས་བྱ་བ་ལ། འདིར་སྟན་ཞེས་པས་ནི་འདུག་པའི་ས་ཕྱོགས་ཀྱང་གཟུང་བར༌[^1552]རིག་པར་བྱའོ། །

[Block 2460]
ངན་པ་དང་བཟང་པོ་ཡང་དེ་བཞིན་ནོ་ཞེས་བྱ་བས་ནི་མཐོན་པོ་དང་དམའ་བ་གཉིས་གཏོགས་པར་བྱའོ། །

[Block 2461]
རྒྱ་ཆེ་བའི་སྟན་ལ་འདུག་ཅིང་ཆོས་ཉན་པར་བྱེད་ཅིང་བདག་ཉིད་ཤིན་ཏུ་དམའ་བ་ལ་འདུག་ཅིང་ཆོས་སྟོན་པར་བགྱིད་ན་སྒུར་མཆོག་གིས་ཞུས་པ་ལས།

[Block 2462]
དེ་ལྟར་ཆོས་བསྟན་པར༌[^1553]མི་བྱའོ་ཞེས་གང་ཞིག་བཅོམ་ལྡན་འདས་ཀྱིས་གསུངས་པ་དེ་བས་ན་མདོ་འདིའོ། །

[Block 2463]
མདུན་དུ་འགྲོ་བ་ལ་ཕྱི༌[^1554]ནས་འགྲོ་ཞིང་མི་བཤད་པར་རོ་ཞེས་བྱ་བ་ནི་ཇི་ལྟར་ལམ༌[^1555]མ་ཡིན་པ་ནས་སོ། །

[Block 2464]
ལམ་ནས་འགྲོ་བ་ལ་ལམ་གྱི༌[^1556]འགྲམ་ནས་འགྲོ་ཞིང་མི་བཤད་པར་རོ། །

[Block 2465]
མགོ་གཡོགས་པ་ལ་སོགས་པ༌[^1557]མ་ཡིན་ནོ་ཞེས་བྱ་བ་ལ་སོགས་པའི་སྒྲས་ནི་མཆོང་བ༌[^1558]ལ་སོགས་པ་རྣམ་པར་འབྱེད་པའི་གཞུང་ལས་གཟང་བ༌[^1559]རྣམས་སོ། །

[Block 2466]
གླང་པོ་ཆེ་དང་རྟ་ཞོན་པ་དང་ཁྱོགས་དང་བཞོན་པའི་སྟེང་ན་འདུག་པ་དང་། མཆིལ་ལྷམ་གྱོན་པ་ལ་མི་བཤད་པར་རོ་ཞེས་བྱ་བ་ནི་གླང་པོ་ཆེ་ལ་ཞོན་པ་ན་ཞེས་བྱ་བ་ལ་སོགས་པ་ལ་རེ་རེ་ནས་བཞོན་པའི་སྒྲས་འབབ་པ་མ་ཡིན་ཏེ། ང་རྒྱལ་གྱི༌[^1560]གནས་སུ་འབྲེལ་པ་ཉིད་ཀྱི༌[^1561]ཕྱིར་འདི་བཀག་པ་ཡིན་གྱི་མཐོན་པོའི་གནས་དང་འབྲེལ་པ་ཉིད་ཀྱིས༌[^1562]ནི་མ་ཡིན་ཏེ། དེར་བཀག་ཟིན་པ་ཉིད་ཀྱི་ཕྱིར་དེ་བས་ན་གནས་སྐབས་ཐམས་ཅད་དུ་འདི་བཀག་པའོ། །

[Block 2467]
མགོ་དོ་ཀེར་ཅན་དང་། ཞྭ་གྱོན་པ་དང་ཅོད་པན་ཅན་དང་ཕྲེང་བ་ཅན་དང་དཀྲིས་པ་ལ་མི་བཤད་པར་རོ། །

[Block 2468]
ལག་ན་ཁར་བ༌[^1563]དང་གདུགས་དང་མཚོན་དང་། རལ་གྲི་དང་དགྲ་སྟ་ཐོགས་པ་དང་གོ་ཆ་གྱོན་པ་ལ་མི་བཤད་པར་རོ། །

[Block 2469]
འགྲེང་སྟེ་བཤང༌[^1564]གཅི་མི་བྱ་བར་རོ། །

[Block 2470]
རྩྭ་སྔོན་པོ་ཡོད་པའི་ས་ཕྱོགས་སུ་ཡང་མི་བྱ་མི་དོར་བར༌[^1565]རོ་ཞེས་བྱ་བ་ནི་བཤང་གཅི་མི་བྱ་ཞེས་བྱ་བར་སྦྱར་རོ། །

[Block 2471]
མི་དོར་བར༌[^1566]རོ་ཞེས་བྱ་བ་ནི་རྩྭ་སྔོན་པོ་ཡོད་པའི་ས་ཕྱོགས་སུ་བཤང་གཅིའོ། །

[Block 2472]
མཆིལ་མ་དང་སྣབས་དང་། སྐྱུགས་པ༌[^1567]དང་རླུགས་པ་ཡང་ངོ་ཞེས་བྱ་བ་ནི་དེ་ཡང་རྩྭ་སྔོན་པོ་ཡོད་པའི་ས་ཕྱོགས་སུ་མི་བྱ་མི་དོར་བའོ། །

[Block 2473]
ཆུའི་ནང་དུ་མི་བྱ་བར་རོ་ཞེས་བྱ་བ་ནི་བཤང་གཅི་དང་མཆིལ་མ་ལ་སོགས་པ་མི་བྱ་བ་དང་མི་དོར་བའོ། །

[Block 2474]
གནོད་པ་བྱུང་བ་མ་གཏོགས་པར་ཤིང་ལ་མི་གང་ཙམ་ལས་མཐོར་མི་འཛེག་པར་རོ་ཞེས་བྱ་བ་ནི་མི་གང་ཙམ་ལས་མཐོར་མི་འཛེག་ཅེས༌[^1568]བྱ་བའི་དོན་ཏོ། །

[Block 2475]
བསླབ་པ་རྣམས་ཀྱིས་ཡུལ་གྱི་རབ་ཏུ་དབྱེ་བ་ནི་མདོར་བསྡུ་ན་རྣམ་པ་དགུ་སྟེ། གོས་བགོ་བ་དང་སྤྱོད་ཡུལ་དུ་འགྲོ་བ་དང་། དེར་སྟན་ལ་འདུག་པ་དང་། ཟས་བླང་བ་དང་། ཟན་བཟའ་བ་དང་། ལྷུང་བཟེད་སྤྱོད་པ་དང་། ཆོས་བསྟན་པ་དང་། སྒྲུབ་པའི་ཚུལ་དང་རྒྱུ་བ་སྟེ། དེ་རྣམས་གོ་རིམས་བཞིན་དུ་སྦྱར་བར་བྱའོ། །

[Block 2476]
བསླབ་པ་རྣམས་སོ། །

[Block 2477]
དགེ་སློང་གི་རྣམ་པར་འབྱེད་པ་རྫོགས་སོ།། །།

[Block 2478 [HEADING]]
## དགེ་སློང་མའི་ཕམ་པར་འགྱུར་བ་རྣམས། ^4-0

[Block 2479]
འདིར་གང་ཞིག་བྱེ་བྲག་མེད་པར་ཚུལ་ཁྲིམས་བཤད་ཟིན་པ་དང་། འཆད་པར་འགྱུར་བ་ལ་ཐམས་ཅད་དུ་བསྙེན་པར་རྫོགས་པ་དང་བཅས་པ་ལ་དེ་རིག་པར་བྱ་སྟེ། བྱེ་བྲག་མེད་པའི་ཕྱིར་ཐམས་ཅད་དུ་ལུས་ཀྱི་བསྙེན་པར་རྫོགས་པར༌[^1569]བྱ་བ་མ་ཡིན་པ་ཐམས་ཅད་ལས་ལྡོག་པ་དང་། བྱ་བ༌[^1570]ཐམས་ཅད་ལ་ཡང་དག་པར་ཞུགས་པ་ལ་རྣམ་པར་གཞག་པ་ཞེས་བྱ་བ་འདིའི་ངོ་བོའོ། །

[Block 2480]
གང་ཞིག་འདིར་འགའ་ཞིག་ཏུ་ཚུལ་ཁྲིམས་རྣམ་པར་གཞག་པ་ལ་མི་སྲིད་པའི་ཕྱིར། དེ་ལྟ་བུའི་རྟེན་འདི་གང་གི་ཕྱིར་འདིར་ཡོད་པ་ལ་ཉེས་དམིགས་སུ་འགྱུར་རོ་སྙམ་པ་དེ་ལྟ་བུ་ལ་སེམས་འཇོག་པ་འདི་ནི་བྱ་བ་དང་བྱ་བ་མ་ཡིན་པར་གྱུར་པ་གང་ཞིག་ཉེས་པ་ཆུང་བ་ཉིད་རྣམ་པར་གཞག་པ་དེ་ནི་ཤིན་ཏུ་ཆེ་བ་སྤོང་བའི་དོན་དུ་ནི་མ་ཡིན་ནོ། །

[Block 2481]
གང་ཞིག་ཉེས་པ་ཆེ་བ་ཉིད་དུ་རྣམ་པར་གཞག་པ་ཡང་ཡོད་དེ། དེ་ནི་ཤིན་ཏུ་ཆེན་པོ་སློང༌[^1571]བའི་ཕྱིར་རོ། །

[Block 2482]
དེ་བས་ན་དགེ་སློང་མ་ལ་ཡང་འདི་ཇི་ལྟར༌[^1572]སྲིད་པར་ཚུལ་ཁྲིམས་གཏོགས་པར་བྱའོ། །

[Block 2483]
དེ་ལ་གང་ཞིག་རྣམ་པར་འབྱེད་པར་གཏོགས་པ་མི་སྲིད་པའི་ཕྱིར་དང་། བར་དུ་གཅོད་པར་བྱེད་པའི་ཕྱིར་འདི་ལ་རྣམ་པར་གཞག་པ་མ་བྱས་པ་གང་ཞིག་ཡང་ཉེས་པ་མང་ཉུང་གིས་གང་མི་མཚུངས་པ་ཉིད་དུ་རྣམ་པར་གཞག་པ་དེ་རྣམས་ཐམས་ཅད་བརྗོད་པར་བྱ་སྟེ། དེ་ལ་ལྟུང་བ་ལ་སྦྱོར་བའི་ཚིག་ཡན་ཆད་དགེ་སློང་མ་རྣམས་ཀྱིའོ་ཞེས་བྱ་བ་ནི་འདི་ནས་བརྩམས་ཏེ། འོག་ནས་ཉམས་པ་དང་མ་སྐྱེས་པ་དག་ལྟུང་བ་ལ་སྦྱོར་ན་ཉེས་བྱས་སོ་ཞེས་འབྱུང་བའི་ཚིག་ཡན་ཆད་ནི་དགེ་སློང་མར་གྱུར་པ་ལ། དེ་རྟོགས་པ་པོའམ༌[^1573]བྱེད་པ་པོ་ལ་ལྟ་བར༌[^1574]བྱའོ། །

[Block 2484]
རེ་ཞིག་ཕམ་པར་འགྱུར་བ་རྣམས་ལ་གསུངས་པ་ཐམས་ཅད་འདིར་བལྟ་བར་བྱ་བ་སྟེ། བཞི་པོ་དག་གོ་ཞེས་བྱ་བ་ནི་མི་ཚངས་པར་སྤྱོད་པ་ལ་སོགས་པ་བཞི་ནི་དགེ་སློང་བཞིན་དུ་དགེ་སློང་མ་ལ་ཡང་ངོ་། །གཞན་གྱི་ལྟུང་བ་འཆབ་པ་དང་སྤངས་པའི་རྗེས་སུ་ཕྱོགས་པ་དག་གིས་ཚུལ་ཁྲིམས་གང་ལ་ལ་ཞིག་དང་ལུས་ཀྱི་རེག་པའི་འཇུག་པ་ཐམས་ཅད་ལ་ཕམ་པར་འགྱུར་བ་ཉིད་དོ། །

[Block 2485]
དེ་ལ་གང་ལ་རེག་པའི་ཕམ་པར་འགྱུར་ཞེ་ན། དེའི་ཕྱིར་བདག་གིར་བྱེད་པ་ལའོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2486]
ཡན་ལག་གང་གིས་ཤེ་ན། དེའི་ཕྱིར་མིག་ནས་པུས་མོའི་བར་གྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ་མིག་གི་གནས་མན་ཆད་ནས་པུས་མོའི་ལྷ་ང་ཡན་ཆད་ཀྱི་བར་དེས་སོ། །

[Block 2487]
དེ༌[^1575]ཅི་ཞིག་བདག་གིར་བྱེད་པ་ལ་ཞེ་ན་དེའི་ཕྱིར་རེག་པའོ་ཞེས་བྱ་བ་སྨོས་ཏེ། ནོམ་པར་བྱེད་ཉུག་པར་བྱེད་ལ་ཞེས་གསུངས་པ་ནི་འདིའི་དཔེ་ཡིན་ཏེ། འདི་ལྟར་ནོམ་པར་བྱེད་ཉུག་པར་བྱེད་ལ་ཞེས་བྱ་བ་དེའི་རྣམ་པར་འབྱེད་པ་ནི་ལུས་ལ་ལུས་ཀྱིས་ཉེ་བར་གཞོལ་བར་བྱས་ལ་ཞེས་གསུངས་པ་ཡིན་ནོ། །གང་གི་རེག་པ་ཞེ་ན། དེའི་ཕྱིར་ཕོའི་འོ་ཞེས་བྱ་བ་སྨོས་སོ། །

[Block 2488]
ལུས་ཀྱི་དབང་པོའི་ཕྱོགས་ཀྱིས་བདག་གིར་བྱེད་པ་ལ་གསུངས་པ་དེ་ལ༌[^1576]བསམ་པ་གང་གིས་ཤེ་ན། དེའི་ཕྱིར་འཁྲིག་པའི་འདོད་ཆགས་ཀྱིས་སོ་ཞེས་བྱ་བ་སྨོས་ཏེ། བདེ་བ་ཉམས་སུ་མྱོང་བར་འདུན༌[^1577]པས་དེའི་ཀུན་ཏུ་ཆགས་པ་དང་མཚུངས་པར་ལྡན་པས༌[^1578]གང་ཞིག་འདི་སྐད་སྨོས་པ་དེ་ལ་ཚིག་འདིའོ། །

[Block 2489]
ལུས་ཀྱི་དབང་པོའི་ཕྱོགས་ཀྱིས་བདག་གིར་བྱེད་པ་ལ་གསུངས་པ་དེ་ལ་བསམ་པ་གང་གིས་ཤེ་ན། འདིར་མདོ་གཞན་ལས་སྐྱེས་པ་ཆགས་པར༌[^1579]འགྱུར་བ་ཞེས་བྱ་བ་ནི་ཆགས་པ་དང་། ཀུན་ནས་ཆགས་པ་དང་། ཀུན་ནས་འཁྲིག་ཅིང་འདོད་པའི་འདོད་ཆགས་ཀྱིས་ཟིལ་གྱིས་ནོན་པ་གང་ཡིན་པའོ་ཞེས་བྱ་བ་རྣམ་པར་འབྱེད་པ་ལས་འབྱུང་ངོ་། །གལ་ཏེ་ཡང་འདིར་ཆགས་པར་འགྱུར་བས་ཞེས་བྱ་བ་སྐྱེས་པ་ལ་ཡང་ཆགས་པར་གྱུར་པའི་ཚིག་ཏུ་བྱས་པ་དེ་ལྟར་ཡང་ཆགས་པར་མ་གྱུར་པའི་སྐྱེས་པ་ལ་ཡང་རྣམ་པར་འབྱེད་པ་ལས་ཆགས་པར་འགྱུར་བ་སྐྱེས་པ་མ་ཆགས་པས་པུས་མོ་ཡན་ཆད་མིག་མན་ཆད་ནོམ་པར་བྱེད་ཉུག་པར་བྱེད་པ་བདག་གིར་བྱེད་ན། ལྟུང་བ་ཕམ་པར་འགྱུར་རོ་ཞེས་གསུངས་པའི་ཕྱིར། ཕམ་པ༌[^1580]ཉིད་ཅེས་བྱ་བ་ལ་ཕོ་ལ་འདིར་ཆགས་པ་མངོན་པར་མི་བསྟན༌[^1581]ནོ། །

[Block 2490]
ཡན་ལག་གཞན་གྱིས་ནི་སྦོམ་པོའོ་ཞེས་བྱ་བ་ནི་མིག་ནས་པུས་མོའི་བར་ལས་གཞན་པའི་ཡན་ལག་གིས་ཕོའི་རེག་པ་འཁྲིག་པའི་འདོད་ཆགས་ཀྱིས་བདག་གིར་བྱེད་པ་ལ་ནི་ཉེས་པ་སྦོམ་པོར་འགྱུར་རོ། །
--- END BLOCKS ---
