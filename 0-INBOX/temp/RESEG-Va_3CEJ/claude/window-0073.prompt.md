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
[Block 2556]
ཚངས་པ་ཆེན་པོའི་ཆུ་ཞེང་དང་དབྱིབས་ཀྱི་ལུས༌[^1337]དང་། ཚིག་ཏུ་བརྗོད་པ་དང་། གོས་གྱོན་པ་ཡང་གཞན་ཡིན་ལ། དེའི་འཁོར་གྱི་ཡང་གཞན་ཡིན་པས་ན་ལུས་ཐ་དད་པ་དག་ཡིན་ནོ། །

[Block 2557]
མདོ་ལས་དེ་དག་འདི་སྙམ་དུ་བདག་ཅག་གིས་སེམས་ཅན་འདི་ཚེ་རིང་ཞིང་དུས་རིང་པོར་གནས་པར༌[^1338]མཐོང་ལ༌[^1339]ཞེས་བྱ་བ་ནས་སེམས་ཅན་འདི་ཡང་སེམས་ལ་འདི་སྙམ་དུ་ཀྱེ་མ་སེམས་ཅན་གཞན་དག་ཀྱང་འདིར་བདག་དང་སྐལ་བ་མཉམ་པར་སྐྱེ་བར་གྱུར་ཅིག་སྙམ་དུ་སྨོས༌[^1340]ལ། བདག་ཅག་ཀྱང་འདིར་སྐྱེས་པས་ཞེས་བྱ་བར་ཤེས་སོ་ཞེས་གང་གསུངས་པ། དེ་དག་གིས་དེ་ཇི་ལྟར་མཐོང་ཞེ་ན། ཁ་ཅིག་ན་རེ་འོད་གསལ་ལ་གནས་པ་རྣམས་ཀྱིས་ཏེ། དེ་དག་ནི་དེ་ནས་ཤི་འཕོས་པ་ཡིན་ནོ་ཞེས་ཟེར་རོ། །

[Block 2558]
དེ་ནི་བསམ་གཏན་གཉིས་པའི་སྙོམས་པར་འཇུག་པ་མ་ཐོབ་ན་ནི་ཇི་ལྟར་ན་དེའི་ས་པའི་སྔོན་གྱི་གནས་རྗེས་སུ་དྲན། འོན་ཏེ་ཐོབ་ན་ནི་ཇི་ལྟར་ན་ཚངས་པ་ཆེན་པོ་ལ་དམིགས་པའི་ཚུལ་ཁྲིམས་དང་བརྟུལ་ཞུགས་མཆོག་ཏུ་འཛིན་པའི་ལྟ་བ་ལ་ཞེན་པ་དག་ཡིན། གཞན་དག་ན་རེ་སྲིད་པ་བར་མ་ལ་གནས་པ་དག་གིས་མཐོང་ངོ་ཞེས་ཟེར་རོ། །

[Block 2559]
དེ་ན་ཡང་བགེགས་བྱེད༌[^1341]པ་མེད་པའི་ཕྱིར་དུས་རིང་པོར་གནས་པ་མི་སྲིད་ན་ཇི་ལྟར་ན་དེ་དག་འདི་སྙམ་དུ་བདག་ཅག་གིས་སེམས་ཅན་འདི་ཚེ་རིང་ཞིང་དུས་རིང་པོར་གནས་པ་མཐོང་ངོ་སྙམ་དུ་ཤེས་པར་འགྱུར། དེ་ལྟ་བས་ན་དེ་ན་གནས་པ་དེ་དག་ཁོ་ནས་དེའི་སྔོན་གྱི་ཚུལ་རྗེས་སུ་དྲན་ཞིང་དེ་ལྟར་དུས་རིང་པོར་གནས་པ་མཐོང་ངོ་། །མཐོང་ནས་ཀྱང་ཕྱིས་དེ་དག་མཐོང་ངོ་སྙམ་དུ་ཤེས་པ་ཡིན་ནོ། །

[Block 2560 [HEADING]]
##### ལུས་གཅིག་ཅིང་འདུ་ཤེས་ཐ་དད་པ། ^3-1-3-3-0

[Block 2561]
སེམས་ཅན་གཟུགས་ཅན་ལུས་གཅིག་ཅིང་འདུ་ཤེས་ཐ་དད་པ་དག་ཀྱང་ཡོད་དེ། འདི་ལྟ་སྟེ་འོད་གསལ་གྱི་ལྷ་རྣམས་སོ། །

[Block 2562]
འདི་ནི་རྣམ་པར་ཤེས་པ་གནས་པ་གསུམ་པའོ་ཞེས་གསུངས་ཏེ། འདིར་ནི་མཐའ་སྨོས་པས་བསམ་གཏན་གཉིས་པ་མཐའ་དག་སྨོས་པར་རིག་པར་བྱའོ། །

[Block 2563]
དེ་ལྟ་མ་ཡིན་ན་འོད་ཆུང་རྣམས་དང་། ཚད་མེད་འོད་རྣམས་རྣམ་པར་ཤེས་པ་གནས་པ་གང་དུ་རྣམ་པར་གཞག་པར་འགྱུར་ལ། [^1342]དེ་ལ་ཁ་དོག་དང་། རྟགས་དང་། དབྱིབས་ཐ་མི་དད་པའི་ཕྱིར་ལུས་གཅིག་པ་དག་གོ། །

[Block 2564]
བདེ་བར་འདུ་ཤེས་པའི་ཕྱིར་དང་། བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་ཡང་མ་ཡིན་པར་འདུ་ཤེས་པའི་ཕྱིར་འདུ་ཤེས་ཐ་དད་པ་དག་སྟེ། དེ་དག་ནི་དངོས་གཞིའི་ས་ལ་ཡིད་བདེ་བའི་དབང་པོས་ཡོངས་སུ་སྐྱོ་ནས་ཉེར་བསྡོགས་ལས་བཏང་སྙོམས་ཀྱི་དབང་པོ་མངོན་དུ་བྱེད་ལ། ཉེར་བསྡོགས་ཀྱི་བཏང་སྙོམས་ཀྱི་དབང་པོས་ཡོངས་སུ་སྐྱོ་ནས་ནི་ཡང་དངོས་གཞིའི་ས་ལ་ཡིད་བདེ་བའི་དབང་པོ་མངོན་དུ་བྱེད་དེ། དཔེར་ན་དབང་ཕྱུག་དག་འདོད་པའི་དགའ་བས་ཡོངས་སུ་སྐྱོ་ནས་ཆོས་ཀྱི་དགའ་བ་ཉམས་སུ་མྱོང་བར་བྱེད་ལ། ཆོས་ཀྱི་དགའ་བས་ཡོངས་སུ་སྐྱོ་ནས་ནི་ཡང་འདོད་པའི་དགའ་བ་ཉམས་སུ་མྱོང་བར་བྱེད་པ་བཞིན་ནོ་ཞེས་གྲག་གོ། །

[Block 2565]
འདི་དགེ་རྒྱས་པ་དག་ལ་ཡང་ཐལ་བར་འགྱུར་བ་མ་ཡིན་ནམ་ཞེ་ན། མ་ཡིན་ཏེ། དེ་དག་ནི་བདེ་བ་དེས་ཡོངས་སུ་སྐྱོ་བ་མེད་དོ། །དེ་ཅིའི་ཕྱིར་ཞེ་ན། བདེ་བ༌[^1343]ནི་ཞི་བ་ཡིན་ལ། ཡིད་བདེ་བ་ནི་སེམས་གཡོ་བར་བྱེད་པ་ཡིན་པས་མ་ཞི་བ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2566]
མདོ་སྡེ་པ་རྣམས་ནི་མདོ་ལས་འོད་གསལ་བའི་ལྷའི་རིས་དེ་ན་སེམས་ཅན་གང་དག་སྐྱེས་ནས་རིང་པོ་མ་ལོན་པ་འཇིག་རྟེན་འདི་འཇིག་པ་ལ་མི་མཁས་ཤིང་འཆགས་པ་ལ་མི་མཁས་པ་དེ་དག་མེ་ལྕེ་དེ་མཐོང་ནས༌[^1344]མེ་ལྕེ་དེ༌[^1345]ཚངས་པའི་གཞལ་མེད་ཁང་སྟོང་པ་བསྲེགས་ནས༌[^1346]འདིར་འོང་བར་འགྱུར་ན་མི་རུང་ངོ་ཞེས་སྐྲག་ནས་ཡི་ཆད་ཅིང་སྐྱོ་བར་འགྱུར་རོ། །

[Block 2567]
འོད་གསལ་བའི་ལྷའི་རིས་དེ་ན་སེམས་ཅན་གང་དག་སྐྱེས་ནས་རིང་དུ་ལོན་པ་འཇིག་རྟེན་འདི་འཇིག་པ་ལ་མཁས་ཤིང་འཆགས་པ་ལ་མཁས་པ་ལ༌[^1347]དེ་དག་སེམས་ཅན་སྐྲག་པ་དེ་དག་ལ་གྲོགས་པོ་དག་མ་འཇིགས་ཤིག །གྲོགས་པོ་དག་མ་འཇིགས་ཤིག །མེ་ལྕེ་འདི་ནི་སྔོན་ཡང་ཚངས་པའི་གཞལ་མེད་ཁང་སྟོང་པ་བསྲེགས་ནས་དེ་ཉིད་དུ་མེད་པར་གྱུར་ཏོ༌[^1348]ཞེས་དབུགས་འབྱིན་པར་བྱེད་དོ་ཞེས་དེ་དག་ཇི་ལྟར་འདུ་ཤེས་ཐ་དད་པ་དག་ཡིན་པར་བཤད་དེ། དེ་ལྟ་བས་ན་དེ་དག་མེ་ལྕེ་འོང་བ་དང་མེད་པར་འདུ་ཤེས་པའི་ཕྱིར་དང་། སྐྲག་པ་དང་མི་སྐྲག་པར་འདུ་ཤེས་པའི་ཕྱིར་འདུ་ཤེས༌[^1349]ཐ་དད་པ་དག་ཡིན་གྱི་བདེ་བ་དང་སྡུག་བསྔལ་དང་། [^1350]བདེ་བ་ཡང་མ་ཡིན་སྡུག་བསྔལ་ཡང་མ་ཡིན་པར་འདུ་ཤེས་པའི་ཕྱིར་ནི་མ་ཡིན་ནོ་ཞེས་འཆད་དོ། །

[Block 2568 [HEADING]]
##### ལུས་གཅིག་འདུ་ཤེས་གཅིག་པ། ^3-1-3-4-0

[Block 2569]
སེམས་ཅན་གཟུགས་ཅན་ལུས་གཅིག༌[^1351]འདུ་ཤེས་གཅིག་པ་དག་ཀྱང་ཡོད་དེ། འདི་ལྟ་སྟེ། དགེ་རྒྱས་ཀྱི་ལྷ་རྣམས་སོ། །

[Block 2570]
འདི་ནི་རྣམ་པར་ཤེས་པ་གནས་པ་བཞི་པའོ་ཞེས་གསུངས་ཏེ། འདུ་ཤེས་གཅིག་པ་དག་ཅེས་བྱ་བ་ནི། བདེ་བར་འདུ་ཤེས་པ་དག་གོ། །

[Block 2571]
དེ་ལ་བསམ་གཏན་དང་པོ་ན་ནི་ཉོན་མོངས་པ་ཅན་གྱི་འདུ་ཤེས་སུ་འདུ་ཤེས་གཅིག་པ་དག་ཡིན་ནོ། །

[Block 2572]
གཉིས་པ་ན་ནི་དགེ་བའི་འདུ་ཤེས་སུ་འདུ་ཤེས་ཐ་དད་པ་དག་ཡིན་ནོ། །

[Block 2573]
གསུམ་པ་ན་ནི་རྣམ་པར་སྨིན་པ་ལས་སྐྱེས་པའི་འདུ་ཤེས་སུ་འདུ་ཤེས་གཅིག་པ་དག་ཡིན་ནོ། །

[Block 2574 [HEADING]]
##### གཟུགས་མེད་པ་གསུམ། ^3-1-3-5-0

[Block 2575]
གཟུགས་མེད༌[^1352]པ་གསུམ་པོ༌[^1353]ནི་མདོ་ལས་ཇི་སྐད་འབྱུང་བ་སྟེ། དེ་ལྟར་ན་དེ་དག་གི་ནི་རྣམ་པར་ཤེས་པ་གནས་པ་བདུན་ཡིན་ནོ། །

[Block 2576]
འདི་ལ་རྣམ་པར་ཤེས་པ་གནས་པ་གང་ཡིན་ཞེ་ན། ཅི་རིགས་པར་དེ་དག་དང་ལྡན་པའི་ཕུང་པོ་ལྔ་དང་བཞི་ཡིན་ནོ། །

[Block 2577 [HEADING]]
##### ལྷག་མ་རྣམ་པར་ཤེས་པ་གནས་པ་མ་ཡིན་པ། ^3-1-3-6-0

[Block 2578]
ཅིའི་ཕྱིར་ལྷག་མ་རྣམ་པར་ཤེས་པ་གནས་པ་མ་ཡིན་ཞེ་ན། འདི་ལྟར། ལྷག་མ་དེ་འཇོམས་བྱེད་ལྡན། ལྷག་མ་གང་ཞིག་ཅེ་ན། ངན་འགྲོ་རྣམས་དང་། བསམ་གཏན་བཞི་པ་དང་། སྲིད་པའི་རྩེ་མོའོ། །

[Block 2579]
འདི་དག་ན་རྣམ་པར་ཤེས་པ་འཇོམས་པར་བྱེད་པ་དག་ཡོད་པས་དེའི་ཕྱིར་འདི་དག་ནི་རྣམ་པར་ཤེས་པ་གནས་པ་མ་ཡིན་ནོ། །

[Block 2580]
འཇོམས་པར་བྱེད་པ་ཞེས་བྱ་བ་ཅི་ཞེ་ན། གང་གིས་རྣམ་པར་ཤེས་པ་འཇོམས་པར་བྱེད་པ་སྟེ། དེ་ལ་ངན་སོང་དག་ན་ནི་འཇོམས་པར་བྱེད་པ་སྡུག་བསྔལ་གྱི་ཚོར་བ་ཡིན་ཏེ། གནོད་པར༌[^1354]བྱེད་པ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2581]
བསམ་གཏན་བཞི་པ་ན་ནི་འདུ་ཤེས་མེད་པ་དང་། འདུ་ཤེས་མེད་པའི་སྙོམས་པར་འཇུག་པ་ཡིན་ནོ། །

[Block 2582]
སྲིད་པའི་རྩེ་མོ་ན་ནི་འགོག་པའི་སྙོམས་པར་འཇུག་པ་ཡིན་ཏེ། སེམས་ཀྱི་རྒྱུན༌[^1355]གཅོད་པའི་ཕྱིར་རོ། །

[Block 2583]
ཡང་སྨྲས་པ། གང་དུ་འདི་ན་གནས་པ་རྣམས་ན་འགྲོ་བར་འདོད་ལ། དེ་ན་གནས་པ་རྣམས་ནི་བསྐྱོད་པར་མི་འདོད་པ་དེ་རྣམ་པར་ཤེས་པ་གནས་པར་བཤད་ན། ངན་སོང་དག་ན་ནི་གཉི་ག་མེད་དོ། །

[Block 2584]
བསམ་གཏན་བཞི་པ་ན་ནི་སེམས་ཅན་རྣམས་བསྐྱོད་པའི་ཡིད་དང་ལྡན་པ་དག་ཡིན་ཏེ། སོ་སོའི་སྐྱེ་བོ་རྣམས་ནི་འདུ་ཤེས་མེད་པར་འཇུག་འདོད་ལ། འཕགས་པ་རྣམས་ནི་གནས་གཙང་མར་རོ། །

[Block 2585]
སྲིད་པའི་རྩེ་མོ་ནི་རྒྱུ་བ་མི་གསལ་བའི་ཕྱིར་རྣམ་པར་ཤེས་པ་གནས་པ་མ་ཡིན་ནོ། །

[Block 2586 [HEADING]]
#### སེམས་ཅན་གྱི་གནས་དགུ། ^3-1-4-0

[Block 2587]
རྣམ་པར་ཤེས་པ་གནས་པ་བདུན་པོ་ཇི་སྐད་བཤད་པ་དེ་དག་དང་། སྲིད་རྩེ་དང་།

[Block 2588 [VERSE]]
འདུ་ཤེས་མེད་པའི་སེམས་ཅན་རྣམས། །
སེམས་ཅན་གྱི་ནི་གནས་དགུར་བཤད། །

[Block 2589]
འདི་དག་ཏུ་སེམས་ཅན་རྣམས་རང་དགས་ཀུན་ཏུ་གནས་སོ། །

[Block 2590]
མི་འདོད་བཞིན་གནས་ཕྱིར་གཞན་མིན། །གཞན་གང་ཞེ་ན། ངན་སོང་རྣམས་ཏེ། དེ་དག་ཏུ་སེམས་ཅན་རྣམས་མི་འདོད་བཞིན་དུ་ལས་ཀྱི་སྲིན་པོ་དག་གིས་ཀུན་ཏུ་གནས་སུ་འཇུག་གི་དགའ་སྟེ་གནས་པ་ནི་མ་ཡིན་ནོ། །

[Block 2591]
དེའི་ཕྱིར་དེ་དག་ནི་སེམས་ཅན་རྣམས་ཀྱི་གནས་པ༌[^1356]མ་ཡིན་ཏེ་བཙོན་ར་བཞིན་ནོ། །

[Block 2592 [HEADING]]
#### རྣམ་པར་ཤེས་པ་གནས་པ་བཞི། ^3-1-5-0

[Block 2593]
མདོ་གཞན་ལས་ནི་རྣམ་པར་ཤེས་པ་གནས་པ་བདུན་ཞེས་གསུངས་སོ། །

[Block 2594]
གཞན་ལས་ནི་གནས་པ་དག་ནི་ཡང་བཞི་སྟེ། ཞེས་གསུངས་པ། བཞི་གང་ཞེ་ན། རྣམ་པར་ཤེས་པ་གནས་པ་གཟུགས་སུ་ཉེ་བར་འགྲོ་བ་དང་། ཚོར་བར་ཡང༌[^1357]ཉེ་བར་འགྲོ་བ་དང་། འདུ་ཤེས་སུ་ཉེ་བར་འགྲོ་བ་དང་། འདུ་བྱེད་དུ་ཉེ་བར་འགྲོ་བའོ། །

[Block 2595]
དེ་དག་གི་རང་བཞིན་ཅི་ཞེ་ན། དེ་དག་ནི་གོ་རིམས་བཞིན་དུ།
--- END BLOCKS ---
