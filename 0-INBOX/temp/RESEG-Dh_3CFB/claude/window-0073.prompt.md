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
གཞན་ཡང་སྐྱེས་བུ་འཆད་པ་པོའི་ཉུང་ཟད་འཆད་པའི་བརྒྱུད་པ་ཉིད་འདི་ལ་ཁྱེད་ཀྱིས་ཀྱང་མཉན་པར་བྱ་བ་ཡིན་ནོ།[^1751] །དེ་ལ་རྣམ་པར་སྡང་བ་དང་། མི་ཤེས་པ་དང་། སྤྱང་པོ་དག་གི་ནང་ནས་འགའ་ཞིག་གང་ལས་རུང་བར་འགྱུར་བའི་ཕྱིར་ཡིད་བརྟན་པར་བྱ་བ་མ་ཡིན་ནོ། །

[Block 2557]
དེ་བས་ན་སྐྱེས་བུས་མ་བྱས་པའི་བཤད་པ་ལས་མ་ཡིན་ཞིང་། བརྡ་ལས་བྱུང་བའི་འཇིག་རྟེན་གྱི་ཐ་སྙད་ལས༌[^1752]ཀྱང་རིག་བྱེད་ཀྱི་དོན་གྲུབ་པ་མ་ཡིན་ནོ། །

[Block 2558]
བརྡ་ལས་བྱུང་བ་མ་ཡིན་པ་ལ་ཡང་དོན་སྣ་ཚོགས་པ་ཅན་གྱི་སྒྲ་རྣམས་ཀྱི་ཐ་སྙད་མཐོང་བའི་ཕྱིར་མ་གྲུབ་པའི་དོན་ཅན་ནམ། རབ་ཏུ་མ་གྲགས་པའི་འགའ་ཞིག་གི་ཡང་བཤད་པ་མཐོང་བས་ཐམས་ཅད་དུ་དེའི་དོགས་པ་མི་ལྡོག་པའི་ཕྱིར་རོ། །

[Block 2559]
ཐམས་ཅད་དོན་ཇི་ལྟ་བ་བཞིན་དུ་ངེས་པར་སྦྱར་བ་ན་ཡང་རྗེས་སུ་མཐུན་པར་བརྡ་ཇི་ལྟ་བ་བཞིན་དུ་རྟོགས་པ་བསྐྱེད་པའི་ཕྱིར་དང་། འདོད་པ་དང༌[^1753]མི་འདོད་པ་དག་ལ་ཁྱད་པར་མེད་པའི་ཕྱིར་རོ། །

[Block 2560]
དོན་ཐམས་ཅད་ལ་ཁྱད་པར་མེད་པ་དག་ནི་ལྐོག་ཏུ་གྱུར་པ་དང་འབྲེལ་པ་ཅན་གྱི་དོན་གཅིག་ལྐོག་ཏུ་གྱུར་པ་མཐོང་བ་མ་ཡིན་པའི་སྐྱེས་བུ་ཐ་མལ་པ༌[^1754]ལ་སུ་ཞིག་རྣམ་པར་འབྱེད་པར་འགྱུར་ཞིང་། གང་ཞིག་འཇིག་རྟེན་གྱི་ཐ་སྙད་ལས་རྟོགས་པར་འགྱུར། གཞན་ཡང་བདག་ཉིད་ཀྱང་ཐམས་ཅད་དུ་གྲགས་པའི་རྗེས་སུ་འབྲང་བར་མི་བྱེད་དོ། །

[Block 2561]
འདི་ལྟར།

[Block 2562 [VERSE]]
འདི་ཉིད་ཀྱིས་བརྗོད་པར༌[^1755]གྱུར་པ། །
གྲགས་མིན་དོན་བརྗོད་མཐོ་རིས་དང་། །
ལྷ་མོ་ལ་སོགས་སྒྲ་མཐོང་ངོ་། །

[Block 2563]
མི་ལས་ཕུལ་དུ་བྱུང་བ་སྐྱེས་བུ་ཁྱད་པར་ཅན་གྱི་གནས་དང་། མི་ལས་འདས་པའི་བདེ་བའི་རྟེན་དང་། ཉེ་བར་མཁོ་བ་རྣམ་པ་སྣ་ཚོགས་པ་ཅན་ནི༌[^1756]མཐོ་རིས་སོ། །

[Block 2564]
དེར་གནས་པའི་ལྷའི་བུ་མོ་ལ༌[^1757]ལྷ་མོ་ཞེས་འཇིག་རྟེན་ན༌[^1758]བརྗོད་དོ། །

[Block 2565]
དེ་ལ་བརྟེན་པ་མེད་པར་དོན་གཞན་ཉིད་ལ་རྣམ་པར་རྟོག་པར་བྱེད་པ་ན་འདི་སྐྲ་གཞན་དག་ལ་ཇི་ལྟར་རབ་ཏུ་གྲགས་པ་ཚད་མར་འགྱུར། དེ་ལ་གལ་ཏེ་འགལ་བ་མེད་པའི་ཕྱིར་ཁས་ལེན་ཏོ་ཞེ་ན། མ་ཡིན་ཏེ། དབང་པོ་ལས་འདས་པ་འདི་ཡང་འགལ་བ་མ་གྲུབ་པའི་ཕྱིར་རོ། །

[Block 2566]
གཞན་དག་ལ་ཡང་འགལ་བ་མེད་པར་རྟོགས་པར་དཀའ་བ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2567]
མེའི་སྦྱིན་སྲེག༌[^1759]ལས་མཐོ་རིས་ཐོབ་པ་འགལ་དུ་ཟིན་ཀྱང་བློ་དམན་པའི་ཕྱིར༌[^1760]འདིས་ཤེས་པར་ཡང་མི་འགྱུར་རོ། །

[Block 2568]
འགལ་བ་དང་འགལ་བ་མེད་པ༌[^1761]དག་ནི་གནོད་པ་ཅན་དང་། [^1762]སྒྲུབ་པར་བྱེད་པའི་ཚད་མ་འཇུག་པ་ཡིན་ནོ། །

[Block 2569]
དེ་དག་ཀྱང་ལྐོག་ཏུ་གྱུར་པ་ལ་མངོན་པར་འདོད་པ་མ་ཡིན་ནོ། །

[Block 2570]
དེ་བས་ན་ཇི་ལྟར་ན་དེའི་དབང་གིས་རྟོགས་པ་ཡིན། ཚིག་འཇུག་པ་ཉིད་ཀྱི་ཕྱིར་ཡང་འགལ་བ་མེད་པ་མ་ཡིན་ཏེ། གཞན་དག་ལ་ཡང་ཐལ་བར་འགྱུར་བའི་ཕྱིར་རོ། །

[Block 2571]
ལུང་འདི་ནི་སྐྱེས་བུས་མ་བྱས་པ་ཡིན་ལ་དེ་ནི་འཇིག་རྟེན་གྱི་གྲགས་པ་ལས་དོན་གྲུབ་པ་ཡིན་ནོ། །

[Block 2572]
དེ་ལ་ཡང་འགལ་བ་དཔྱོད་པ་ན༌[^1763]ལུང་ནི་ཡིད་བརྟན་དུ་མེད་པར་འགྱུར་རོ། །

[Block 2573]
དེ་ཡོད་དུ་ཟིན་ཀྱང་དོན་དེ་བཞིན་དུ་མ་ཡིན་པའི་ངོ་བོ་ཉིད་ཡིན་པའི་ཕྱིར། ཚད་མ་མི་འཇུག་པས་གཞན་དག་ཀྱང་དོགས་པར་བྱ་བ་ཉིད་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2574]
མཐོ་རིས་འདོད་པས་མེ་ལ་སྦྱིན་སྲེག་སྦྱིན་པར་བྱའོ་ཞེས་བྱ་བ་འདི་ལ༌[^1764]ཁྱིའི་ཤ་ཟ་བའི་བརྗོད་པའི༌[^1765]རྣམ་པར་རྟོག་པར་འགྱུར་བ་ཞེས་བཤད་པ་གང་ཡིན་པ་དེ་མི་འགྱུར་ཏེ། ཡུལ་གཞན་དག་ཏུ་དེ་ལྟར་འདི་བཤད་པའི་ཕྱིར་རོ། །

[Block 2575]
མ་ཡིན་ཏེ། དེའི་དོན་ཡོངས་སུ་ཤེས་པ་མེད་པའི་ཕྱིར་རོ། །

[Block 2576]
ཡུལ་གཞན་དག་ཏུ་ཡང་དེ་ལྟ་བུའི་དོན་གྱི་རྣམ་པར་རྟོག་པ་ནི་བཟློག་པ་མེད་པ༌[^1766]ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2577]
གལ་ཏེ་སྐྱེས་བུས་མ་བྱས་པའི་སྒྲའི་ཕུང་པོ་འདི་ལ་ལར་དོན་རྟོགས་པ་ཅན་དུ་འགྱུར་བ་དེའི་ཚེ་དེ་ལས་དོན་རྟོགས་པར་འགྱུར་རོ། །

[Block 2578]
དེ་དག་གིས་ཕལ་ཆེར་ཡང་ཐམས་ཅད་ལོང་བ་ཉིད་ཡིན་པའི་ཕྱིར། ཇི་ལྟར་འདོད་པ་བཞིན་དུ་བྱེད་དོ། །

[Block 2579]
དེའི་ཕྱིར།

[Block 2580 [VERSE]]
དེ་འདྲའི་སྒྲ་གཞན་དག་ལ་ནི། །
དེ་འདྲའི་རྣམ་རྟོག་ཉིད་དུ་འགྱུར། །

[Block 2581]
མཐོ་རིས་འདོད་པས་མེ་ལ་སྦྱིན་སྲེག་སྦྱིན༌[^1767]པར་བྱའོ། །ཞེས་བྱ་བའི་ངག་འདི་ཅི༌[^1768]འདྲ་བའོ། །

[Block 2582]
གཞན་ཡང་།

[Block 2583 [VERSE]]
གྲགས་པ་དག་ཀྱང་མི་རྣམས་ཚིག །
དེ་ནི་ཚད་མར་མི་འདོད་ན། །
དེ་ལས་ཡང་ཡང་དོན་རྟོགས་པ། །
སྡང་འདོད་དེས་ནི་ཅི་ཞིག་བྱ། །

[Block 2584]
སྐྱེ་བོའི་རབ་ཏུ་བརྗོད་པ་ལས་གཞན་དུ་རབ་ཏུ་གྲགས་པ་ཞེས་བྱ་བ་གཞན་ནི་མེད་དོ། །

[Block 2585]
སྐྱེ་བོ་དེ་དག་ཐམས་ཅད་ཇི་ལྟ་བ་དེ་ལྟ་བུ་ཅན་གྱི་ཚིག་ཅན་དུ་བསམ་པར་བྱ་བ་མ་ཡིན་པ་དེ་བས་ན་རབ་ཏུ་བརྗོད་པ་ནི་ཚད་མ་མ་ཡིན་ཏེ། འདོད་ཆགས་ལ་སོགས་པ་དང་། མ་རིག་པ་དང་ལྡན་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2586]
འགའ་ཞིག་གི་ཡང་དག་པའི་འཇུག་པ་མེད་པ་ན་ཕལ་ཆེར་དོན་དང་ལྡན་པར་འགྱུར་བ་མ་ཡིན་ཏེ། པར་སིག་མ་བག་མར་ལེན་པའི་ལོག་པའི་སྤྱོད་པ༌[^1769]བཞིན་ནོ། །

[Block 2587]
སྐྱེས་བུ་དེ་དག་ཉིད་ཀྱི་ཚིག༌[^1770]ལས་ཀྱང་ལྐོག་ཏུ་གྱུར་པའི་དོན་རྟོགས་པ་དེ་ལྟར་ན། ཇི་ལྟར་དེ་ཉིད་ཅིག་ཅར་སྡང་བར་བྱ་བ་དང་འདོད་པར་བྱ་བ་ཡིན།

[Block 2588 [VERSE]]
ཅི་སྟེ་གྲགས་པ་ལས་བརྒལ་བའི། །
རྟོག་ལ་རྒྱུ་མེད་ཉིད་ཡིན་ནོ། །
རབ་གྲགས་ཚད་མ་ཉིད་མིན་ཕྱིར། །
དེ་འཛིན་ལ་རྒྱུ་ཅི་ཞིག་ཡོད། །

[Block 2589]
གལ་ཏེ་ཕྲད་པ་བཟློག་པས་གཞན་དུ་འཇུག་པའི་ཡོན་ཏན་དང་། སྐྱོན་མཐོང་བ་ན༌[^1771]རིགས་པ་དེ་ལྟར་ན་རབ་ཏུ་གྲགས་པའི༌[^1772]རྗེས་སུ་འགྲོ་བ་ཡིན་ནོ་ཞེ་ན། མ་ཡིན་ཏེ། ཕྲད་པ་ནི་ཚད་མ་འཇུག་པའི་མཚན་ཉིད་ཅན་ཡིན་པའི་ཕྱིར་རོ། །

[Block 2590]
རབ་ཏུ་གྲགས་པའི་ཚད་མ་ཉིད་མ་ཡིན་པའི་སྒོ་ནས་རྟོགས་པར་གཟུང་བ་གང་ཡིན་པ་ནི་ཅིར་ཡང་མི་རུང་ངོ་། །ཐོབ་པར་དཀའ་བའི་རིགས་པ་ཉིད་ཀྱི་ཕྱིར་རོ། །

[Block 2591]
རང་དང་གཞན་གྱི་རྣམ་པར་རྟོག་པ་རྣམ་པ་གཉི་གའི་ཡང་འཇུག་པ་མཚུངས་པ་དེ་ལྟར་ན་རབ་ཏུ་གྲགས་པའི་རྗེས་སུ་བྱེད་པ་ཅི་ཞིག་ཡོད། གཞན་ཡང་།

[Block 2592 [VERSE]]
གྲགས་པ་ཉིད་ཀྱིས༌[^1773]སྒྲ་དོན་གྱི། །
ངེས་ལ་དོགས་པ་བསྐྱེད་པ་ནི། །
གང་ཕྱིར་དེ་ལ་སྒྲ་རྣམས་དོན། །
སྣ་ཚོགས་འཇུག་པ་ཅན་ཉིད་མཐོང་། །

[Block 2593]
སྒྲ་རྣམས་ནི་རབ་ཏུ་གྲགས་པ་ལས་དོན་གཅིག་ཏུ་ངེས་པ་མ་ཡིན་ཏེ། དེ་ཉིད་ལས་དོགས་པ༌[^1774]སྐྱེ་བའི་ཕྱིར་རོ། །

[Block 2594]
འཇིག་རྟེན་ལ་སྒྲའི་དོན་སྣ་ཚོགས་པ་ཅན་དུ་སྣང་བ་དང་།[^1775] འཇིག་རྟེན་གྱི་བརྗོད་པ་ནི་གྲགས་པ་ཡིན་ནོ། །

[Block 2595]
དེ་ཉིད་ཀྱི་ཕྱིར་དོན་སྣ་ཚོགས་པ་ཅན་ཡིན་པའི་ཕྱིར། དེ་ལས་དོན་གྱི་ངེས་པ་རིགས་པ་མ་ཡིན་ནོ། །
--- END BLOCKS ---
