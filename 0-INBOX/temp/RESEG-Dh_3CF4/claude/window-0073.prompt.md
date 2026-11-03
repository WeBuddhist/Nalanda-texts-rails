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
ཅེས་བྱ་བའི་ཚིག་གིས་སོ། །

[Block 2557]
གཞན་ཡང་།

[Block 2558 [VERSE]]
སྦྱིན་ལ་དགའ་བ་གོམས་བྱས་ཤིང་། །
སླར་བཟློག་པ༌[^1629]ནི་མ་བསླབས་པས། །
རབ་ཏུ་སྡུག་པའི་བུ༌[^1630]གཉིས་ཀྱང་། །

[Block 2559]
ཚམ་ཚོམ་མེད་པར་སྦྱིན་ཞེས་སྨྲས།[^1631] །ཞེས་བྱ་བ་དང་། གཞན་ཡང་ཕྱི་རོལ་གྱི་དངོས་པོ་སྦྱིན་པ་པོ་ཕུན་སུམ་ཚོགས་པའི་དབང་དུ་བྱས་ནས་བཤད་པ་དེ་ཐམས་ཅད་ཀྱང་སྦྱར་བར་བྱའོ། །

[Block 2560]
ད་ནི་ཚོང་དཔོན་ཟིལ་གྱིས་མནོན་པའི་སྐྱེས་པའི་རབས་ཀྱིས་སྦྱིན་པ་པོ་ཕུན་སུམ་ཚོགས་པ་དེའི་དབང་དུ་བྱས་ནས་བསྟན་པ་ཡིན་ནོ། །

[Block 2561]
ཕུན་སུམ་ཚོགས་པ་དེ་ཡང་དེ་ཉིད་དུ་བསྟན་ཏེ། འབྱོར་པ་ཟད་པར་གྱུར་ཀྱང་སྦྱིན་པ་ལས་མི་ལྡོག་པ་ཡིན་ཏེ། བརྒྱ་བྱིན་གྱིས་ནོར་རྣམས་མི་སྣང་བར་བྱས་ཀྱང་ལྟོས་པ༌[^1632]མེད་པས་སོ། །

[Block 2562]
དེ་ལྟར་རེ་ཞིག༌[^1633]གསུམ་གྱིས༌[^1634]ཕུན་སུམ་ཚོགས་པ་ཡིན་ཏེ། སྦྱིན་པ་པོ་དང་། སྦྱིན་པའི་དངོས་པོ་དང་། ལེན་པ་པོའོ། །

[Block 2563]
སྦྱིན་པ་པོ་དང་ལེན་པ་པོ་གཉིས་ཀྱིས༌[^1635]ཕུན་སུམ་ཚོགས་པ་ཡང་ལེན་པ་པོའི་ཡིན་གྱི། སྦྱིན་པ་པོའི་མ་ཡིན་ནོ། །

[Block 2564]
སྦྱིན་པའི་དངོས་པོས་ནི་སྦྱིན་པ་པོ༌[^1636]ཁྱད་པར་དུ་མི་བྱེད་དོ། །

[Block 2565]
སྦྱིན་པ་ནི༌[^1637]སྦྱིན་པ་པོའི་ཡིན་གྱི། ལེན་པ་པོའི༌[^1638]མ་ཡིན་ནོ། །

[Block 2566]
རྣམ་པ་འདིའི་ནང་དུ་ཐམས་ཅད་འདུས་པའི་ཕྱིར་གཞན་གྱི་ཕྱི་རོལ་གྱི་ཟང་ཟིང་སྦྱིན་པར་གཟུང་བ་ཡང་གྲུབ་པར་འགྱུར་རོ། །

[Block 2567]
སྦྱིན་པ་པོའི་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པ་ཡོངས་སུ་རྫོགས་པར་བསྟན་པའི་ཕྱིར་དེ་ལྟར་བསྟན་ཏོ། །

[Block 2568]
ད་ནི་ཆོས་ཀྱི་སྦྱིན་པའི་དབང་དུ་བྱས་ནས་ཨ་གསྟེའི༌[^1639]སྐྱེས་པའི་རབས་སུ་བརྒྱ་བྱིན་གྱིས་མཆོག་སྦྱིན་པར་བྱས་པ་ལས་ཕྱིར་ལེགས་པར་གསུངས་པ་བསྟན་པ་ཡིན་ཏེ། དེ་ཡང་དེ་ཉིད་དུ་བཤད་པ་སྟེ།

[Block 2569 [VERSE]]
ལེགས་པར་སྨྲས་པ་རིན་ཆེན་ལ། །
རིན་ནི་ཅི་ཡང་ཡོད་མ་ཡིན། །

[Block 2570]
ཞེས་བྱ་བ་ལ་སོགས་པ་དེས༌[^1640]བརྗོད་པ་ཐམས་ཅད་ཀྱིས་སོ། །

[Block 2571]
མི་འཇིགས་པའི་སྦྱིན་པ་ནི་མིའི་མཆོག་ཡིན་ཏེ། བརྟན་ཞིང་གཙང་ལ་ཚུལ་ཁྲིམས་ནོར་ལྡན་མི་མཆོག་ལ། །ཞེས་བྱ་བ་ལ་སོགས་པ་ཚིགས་བཅད་གཉིས་ཀྱིས་དེར་བསྟན་ཏེ་དེ་ནི་མི་འཇིགས་པའི་སྦྱིན་པའོ། །

[Block 2572]
དེ་བས་སྐྱེས་པའི་རབས་འདི་དག་ནི་གོ་རིམས་སུ་རིགས་པ་ཡིན་ཏེ། གོ་རིམས་འདིའི་རིམ་པས༌[^1641]ནི་གསུམ་པོ༌[^1642]བསྟན་པར་འགྱུར་རོ། །

[Block 2573]
སློབ་དཔོན་དཔའ་བོས་ནི་སྐྱེས་པའི་རབས་གོ་རིམས་ཚུལ་བཞིན་མ་བཀོད་པར་ཡི་གེར་བྲིས་ཤིང་བཞག་བ་ཡིན་ཏེ། དེ་ཡང་ཇི་ལྟར་ཞེན་འཇིག་རྟེན་ལས་གྲགས་པའི་གོ་རིམས་ཀྱིས་ཏེ། འཇིག་རྟེན་བརྗོད་པ་བཞིན་དུའོ། །

[Block 2574]
འདི་ནི་ཟང་ཟིང་གི་སྦྱིན་པ་ལ་སོགས་པའི་གོ་རིམས་ཡིན་ཏེ། ཟང་ཟིང་གི་སྦྱིན་པས་ནི་གཟུགས་དང་ལུས༌[^1643]རྗེས་སུ་བཟུང་བ༌[^1644]ཡིན་ནོ། །

[Block 2575]
ཆོས་དང་མི་འཇིགས་པའི་སྦྱིན་པ་གཉིས་ནི་མིང་དང་ལུས་ཀྱི་གོ་རིམས་སོམོ། །

[Block 2576]
ཡང་ན་ཟང་ཟིང་གི་སྦྱིན་པ་དང་པོར་གཟུང་ངོ་། །དེའི་འོག་ཏུ་ཆོས་དང་མི་འཇིགས་པའི་སྦྱིན་པ་རྣམ་པ་གཉིས་སོ། །

[Block 2577]
ཆོས་ཀྱི་སྦྱིན་པ་དང་པོར་སྨོས་པ་ནི་མི་འཇིགས་པའི་སྦྱིན་པ་ལས་གཙོ་བོ་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2578]
ཡང་ན་འདི་ལྟར་གོ་རིམས་ཡིན་ཏེ།

[Block 2579]
དང་པོ་ནི་མི་འཇིགས་པའི་སྦྱིན་པ་ལ། དེའི་འོག་ཏུ་ཆོས་ཀྱི་སྦྱིན་པ་ཡིན་ཏེ། ཐོག་མར་འཇིགས་པ་བསལ་ནས་དེའི་འོག་ཏུ་སེམས་བདེ་བ་དང་། ཆོས་ཀྱི་སྦྱིན་པས་འདོད་པའི་དོན་འགྲུབ་པར་བསྟན་པ་ཡིན་ནོ། །

[Block 2580]
[^1645]བཅུ་ཚན་དང་པོའོ།། །།

[Block 2581 [HEADING]]
## བརྒྱ་བྱིན་གྱི་སྐྱེས་པའི་རབས། ^12-0

[Block 2582]
དབང་ཕྱུག་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་ནི་མཐུ་དང་ནུས་པ་ཕུན་སུམ་ཚོགས་པ་ཞེས་བྱ་བ་ཡིན་ཏེ། མཐོ་བར་གྱུར་པ་དེས་གཞན་དག་ལ་སྙིང་བརྩེ་བ་ལྷོད་པར་མི་འགྱུར་བ༌[^1646]སྟེ་བདག་ཉིད་ཆེན་པོ་དེའོ། །

[Block 2583]
ཡུན་རིང་མོ་ནས་བསོད་ནམས་སྤྱོད་པ་ལ་རབ་ཏུ་གོམས་ཞིང༌[^1647]ཞེས་བྱ་བ་ནི་ཡུན་རིང་མོ་ནས་བསོད་ནམས་ལ་རབ་ཏུ་གོམས་པ་སྟེ། བདག་དང་གཞན་ལ་ཕན་པ་སྒྲུབ་པའི་མཚན་ཉིད་ཀྱི་ལས་གང་ཡིན་པ་དེ་ནི་བསོད་ནམས་ཏེ། ཡུན་རིང་མོ་ནས་བསོད་ནམས་སྤྱོད་པ་ལ་རབ་ཏུ་གོམས་པའོ། །

[Block 2584]
འདིས་ནི་འདས་པའི་དུས་ཀྱི་བསོད་ནམས་ཀྱི་ཚོགས་བསྟན་ཏོ། །

[Block 2585]
སྦྱིན་པ་དང་། དུལ་བ་དང་། སྡོམ་པ་དང་། སྙིང་རྗེ་ལ་འདྲིས་པ་གང་ཡིན་པ་དེ་ནི་སྦྱིན་པ་དང་། དུལ་བ་དང་། སྡོམ་པ་དང་སྙིང་རྗེ་ལ་འདྲིས་པར་གྱུར་པ་སྟེ། འདིས་ནི་ད་ལྟར་བྱུང་བའི་དུས་སུ་བདག་དང་གཞན་ལ་ཕན་པ་སྒྲུབ་པའི་མཚན་ཉིད་བསྟན་ཏོ། །

[Block 2586]
གཞན་ལ་ཕན་པར་སྤྱོད་པ་ཁྱད་པར་ཅན་ལ་ངེས་པར་བྱེད་པ་གང་ཡིན་པ་དེ་ནི་གཞན་ལ་ཕན་པར་སྤྱོད་པ་ཁྱད་པར་ཅན་ལ་ངེས་པར་སྤྱོད་པའོ། །

[Block 2587]
འདིས་ནི་རྟག་ཏུ་གུས་པ་དང་སྦྱོར་བ་གཉིས་ཀྱིས་གཞན་ལ་ཕན་པ་སྒྲུབ་པ་བསྟན་ཏོ། །

[Block 2588]
དེ་ལ་རྟེན༌[^1648]བཅས་པ་ཞེས་བྱ་བ་ནི་མཚོན་པ་སྟེ། བདག་དང་གཞན་གྱི་སྒྲུབ་པ་ཁྱད་པར་ཅན་ཡང་དག་པར་བརྟེན་པའོ། །

[Block 2589]
ཡང་ཏོག་རྡོ་ཐལ་གསར་དུ་བསྐུས་པ་ཞེས་བྱ་བ་ལྟ་བུ་ནི་སྔར་བཤད་པའི་བྱང་ཆུབ་སེམས་དཔའོ། །

[Block 2590]
ཟླ་བའི་འོད་ཟེར་ལྟ་བུ་ནི་ལྷའི་དབང་པོའི་དཔལ་ལོ། །

[Block 2591]
དེ་གཉིས་དང་འདྲ་བར་གྱུར་པ་ཡིན་ནོ། །

[Block 2592]
རྟེན་དང་བརྟེན་པར་གྱུར་པ་ཉིད་དོ། །

[Block 2593]
ཚིག་རྐྱང་དང༌[^1649]ཚིགས་བཅད་དེ་དག་གིས་ནི་བྱང་ཆུབ་སེམས་དཔའ་བདག་ཉིད་ཀྱི་རྒྱུ་བསྟན་པའོ། །

[Block 2594]
ད་ནི་གང་གོང་དུ་བསྟན་པའི་དབང་ཕྱུག་ཕུན་སུམ་ཚོགས་པ་དང་རྗེས་སུ་མཐུན་པ་ཡིན་ཡང་སྙིང་རྗེ་ལྷོད་པར་མི་འགྱུར་རོ་ཞེས་བྱ་བ་དེ་ཉིད་སྒྲུབ་པའི་ཕྱིར། གང་གི༌[^1650]ཕྱིར་ལྷ་མ་ཡིན་རྣམས་ཞེས་བྱ་བ་ལ་སོགས་པའི་ཚིགས་བཅད་བརྩམས་པ་ཡིན་ནོ། །

[Block 2595]
སྐལ་བ་ཆེ་བ་ནི༌[^1651]བསོད་ནམས་ཀྱི་ཚོགས་ཀྱི་ཁྱད་པར་རོ། །
--- END BLOCKS ---
